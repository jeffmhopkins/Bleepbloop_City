# Big goal: Move the server to the AI server (migration, backups, snapshots)

**Goal:** Move Bleepbloop City's Bedrock Dedicated Server (BDS) off Jeffrey's Windows machine and into a container on his home Linux box (the "AI server", which mainly runs LLMs). Add automated backups, and deliver world snapshots somewhere Grok Bot can read them to keep this repo up to date.
**Status:** see the [tracker](../progress/tracker.md).
**Companion spec:** [Live API (tokenized connection)](live-api.md) covers the real-time behavior pack, web service, and token auth.

This is written as a spec that Jeffrey, or his AI server, can build from. Anything marked **verify** or **unsure** needs checking on the real box before relying on it.

## Already built in jbrain2 (read 2026-10-10)

Jeffrey's AI box project, [jeffmhopkins/jbrain2](https://github.com/jeffmhopkins/jbrain2), now builds most of the server side of this plan. Its spec is [`docs/plans/MINECRAFT_BEDROCK_PLAN.md`](https://github.com/jeffmhopkins/jbrain2/blob/main/docs/plans/MINECRAFT_BEDROCK_PLAN.md) and the code is in [`deploy/minecraft/`](https://github.com/jeffmhopkins/jbrain2/tree/main/deploy/minecraft) (merged PRs #1593, #1594, #1595, #1596 and #1598). **Where a step below says "jbrain2:", follow jbrain2 and don't build a second copy here.** This repo only records how that maps onto Bleepbloop City. Stage progress is in the [tracker](../progress/tracker.md).

| Our step | What jbrain2 has (as merged) |
| --- | --- |
| Container, image, limits, restart | A `minecraft` service in the stock jbrain stack: `debian:trixie-slim` plus a stdlib Python wrapper that downloads Mojang's BDS into the `jbrain_minecraft` volume. 2 GB `mem_limit`, 60 s stop grace. Not the itzg image. BDS 1.26.52.3 runs on the box. |
| Network and ports | **Host network** (NetherNet needs the box's real address and LAN broadcast). The game is on the LAN only; nothing is forwarded from the router yet (internet play is jbrain2's R1, not built). The wrapper's control port (19180) is on the LAN too, behind a bearer token. |
| Version pinning | The first install follows `MC_BDS_VERSION` (default `latest`). After that a start **keeps the installed version** unless auto-update is turned on (off by default). The Minecraft screen shows running vs latest version with Mojang's release notes. |
| Updating BDS | **Update** takes a backup first, and a failed backup installs nothing. If the new version doesn't log "Server started." within 2 minutes, the old version is reinstalled and the world restored from that backup. |
| Getting the world in | **Import a `.mcworld`** into one of 5 world slots from the PWA. The sidecar checks for `level.dat` and unsafe paths, refuses over 1 GB, backs up an occupied slot first, and sets `level-name` itself. Over 100 MB only uploads on the LAN. The world brings its own seed, game mode, difficulty and cheats setting from `level.dat`. |
| Server settings | Difficulty applies live; game mode and cheats apply at the next restart. All 39 game rules (for example `playersSleepingPercentage`, `showCoordinates`, `playerWaypoints`) can be set per world, live on the loaded world and re-applied on every start. `online-mode=true` is forced. |
| Allowlist | Add or remove gamertags from the PWA (live when the server runs). `allow-list` is still **`false` by default** (`MC_ALLOW_LIST`), and switching it on applies at the next restart. |
| Backups (Stage 1) | Hot `.mcworld` snapshots via `save hold`/`query`/`resume`, on demand, plus automatic ones before an update, load, import, reset or restore. 20 unpinned backups kept per world (automatic ones go first, then the owner's); pinned ones are kept forever. Restore into any slot, and download. **Not scheduled** (that's jbrain2's M7), and **not off the box**: they live in the same `jbrain_minecraft` volume, which is left out of the box backups. A download from the PWA is the only off-box copy, and the screen shows when the last one happened. |
| Snapshot analysis (Stage 2) | Not built. jbrain2's M4 (world index) and M8 (maps) are planned. Its debug API deliberately has no world download, so snapshots won't reach Grok Bot from jbrain2 by themselves. |

**Not covered by jbrain2:** the Windows rollback copy, carrying over `permissions.json` (operator levels: no route manages it), carrying over the Windows `server.properties` (the wrapper writes its own), an off-box copy, scheduled backups, and a test restore on the real world.

> **Sources (checked 2026-10-07):**
> [Getting Started with BDS (Microsoft Learn)](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/getting-started?view=minecraft-bedrock-stable) ·
> [/save command (Minecraft Wiki)](https://minecraft.wiki/w/Commands/save) ·
> [itzg/docker-minecraft-bedrock-server README](https://github.com/itzg/docker-minecraft-bedrock-server) (community image) ·
> [uNmINeD downloads](https://unmined.net/downloads/) ·
> [bedrock-viz](https://github.com/bedrock-viz/bedrock-viz) ·
> [Amulet-Core](https://github.com/Amulet-Team/Amulet-Core) / [docs](https://amulet-core.readthedocs.io) ·
> [Chunker](https://github.com/HiveGamesOSS/Chunker)
> The BDS download also ships `bedrock_server_how_to.html`, the authoritative local manual for backups and transport. Read it on the box.

## Verified facts this plan relies on

- **Platforms:** BDS runs on Windows and Ubuntu Linux. Ubuntu is the only officially supported Linux distribution. On Linux it starts with `LD_LIBRARY_PATH=. ./bedrock_server`. ([Microsoft Learn](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/getting-started?view=minecraft-bedrock-stable))
- **World location:** worlds live in `worlds/<level-name>/`. Only one world is active at a time, set by `level-name` in `server.properties`, which must match the folder name exactly, case included. Existing worlds can be copied into `worlds/`. ([Microsoft Learn](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/getting-started?view=minecraft-bedrock-stable))
- **Config files to carry over:** `server.properties`, `allowlist.json` (gamertags, optional XUIDs), and `permissions.json` (operator levels). Behavior/resource packs live either in the top-level `behavior_packs/` and `resource_packs/` (all worlds) or inside the world folder (that world only). ([Microsoft Learn](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/getting-started?view=minecraft-bedrock-stable))
- **Ticking areas** (the always-loaded area for the sorter and iron farm) are world data, set with `/tickingarea`. Check `tickingarea list` after the move. See [Server config: ticking area](multiplayer-server.md#ticking-area-iron-farm-and-item-sorter).
- **Client/server versions must match**, or players get "Outdated Client/Server". ([Microsoft Learn](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/getting-started?view=minecraft-bedrock-stable))
- **Ports changed in 26.50.** Per the itzg README (citing BDS's own `bedrock_server_how_to.html`), BDS 1.26.50+ uses the **NetherNet** transport by default:
  - **TCP 19132** for signaling.
  - **One UDP port per connected player** from a range (pin it with a fixed range).
  - **UDP 7551** for LAN discovery.
  - The old RakNet UDP 19132/19133 setup is only used if `transport=raknet`. That README also reports 26.51 logging NetherNet as the only supported transport.
  - Microsoft Learn's getting-started page still lists UDP 19132/19133, so **verify** in `bedrock_server_how_to.html` for the exact version you run. ([itzg README, NetherNet section](https://github.com/itzg/docker-minecraft-bedrock-server#nethernet))
- **The allowlist is off by default.** Microsoft documents `allow-list` as defaulting to `false` ([BDS server.properties](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/server-properties)). Set `allow-list=true` explicitly in the `server.properties` the container uses, and keep `online-mode=true`, which the allowlist depends on. With it on, only gamertags in `allowlist.json` can join, so add everyone (`allowlist add <Gamertag>`) before the first join.
- **Safe live backups** use `save hold` → poll `save query` → copy → `save resume`. ([Minecraft Wiki /save](https://minecraft.wiki/w/Commands/save))
  - `save hold` prepares a backup and returns immediately.
  - Poll `save query` until it reports the files are ready. It then lists every file as `path:length`.
  - **Copy only those files and truncate each copy to the listed length.** The server keeps writing during the copy, and the lengths mark the consistent snapshot. A plain zip of the live `db/` folder is *not* guaranteed consistent.
  - `save resume` lets the server go back to normal file housekeeping.
  - Simplest alternative: `stop`, copy, start.
- **Don't read the live LevelDB.** Analyze copies from backups only.

## Target architecture

```
Linux "AI server" (home)
├── container: bedrock-server   (BDS, restart: unless-stopped)
│   ├── volume: /data           (BDS install + worlds/ + config/ + server.properties …)
│   ├── limits: memory + CPU (see below)
│   └── ports: TCP 19132 + fixed UDP range (NetherNet), nothing else exposed
├── backup job (cron/systemd timer) → save hold/query/resume → truncated copy → zip
│   └── /backups/<world>/<timestamp>.zip  (retention policy below)
├── snapshot publisher → private repo release asset OR Google Drive folder
└── (Stage 3) live API web service, see live-api.md
```

- **jbrain2:** the box already runs its own image instead (see [Already built in jbrain2](#already-built-in-jbrain2-read-2026-10-10)). The notes below are kept for reference.
- **Container image:** the community **itzg/minecraft-bedrock-server** image is one option. ([README](https://github.com/itzg/docker-minecraft-bedrock-server))
  - It needs `EULA=TRUE` and keeps everything under `/data`.
  - `VERSION=LATEST` auto-upgrades on restart. **Pin a version instead** so the server never jumps ahead of players' clients.
  - It ships a `send-command` helper for console commands (output goes to the container logs), and it supports `ALLOW_LIST_USERS` and `OPS`/`MEMBERS` env vars.
  - Building your own Ubuntu-based image with the official zip is the other option (open question).
- **Volume:** mount `/data` (or at least `worlds/`) as a named volume or bind mount on the Linux disk, so backups and analysis read from the host.
- **Restart policy:** `unless-stopped` (or a systemd unit) so it comes back after reboots.
- **Resource limits (rough guidance, not official numbers; tune on the box):**
  - 2–4 GB RAM for a handful of players.
  - 1–2 CPU cores.
  - Lower view distance to trim load.
  - Watch CPU contention with LLM inference: pin or limit the container, and leave a core free.
  - **Unsure:** official BDS minimum specs. Microsoft Learn's getting-started page lists OS versions, not RAM.

## Migration checklist (Stage 0)

### Prepare
- [ ] Record the current BDS version on Windows and the world name (`level-name`)
- [x] Install Docker (or chosen tooling) on the Linux box. **jbrain2:** done, the `minecraft` service runs in its Docker Compose stack
- [x] Decide image: itzg community image vs. own Ubuntu image. **jbrain2:** its own `debian:trixie-slim` image with a Python wrapper
- [ ] Read `bedrock_server_how_to.html` for this version (transport, ports, backup notes)

### Back up on Windows
- [ ] In the Windows BDS console: `save hold`
- [ ] Repeat `save query` until it says files are ready, and keep the file list
- [ ] Copy exactly the listed files from `worlds/`, truncating each to its listed length (or simply `stop` the server and copy the whole world folder)
- [ ] `save resume` (if you didn't stop)
- [ ] Also copy `server.properties`, `allowlist.json`, `permissions.json`, `config/` (if any), and any `behavior_packs/` / `resource_packs/`
- [ ] Zip it all, label it with the date, and keep it as the **rollback copy**

### Set up the container
- [ ] Create the container with the same BDS version as Windows (pinned). **jbrain2:** the container exists and runs BDS 1.26.52.3, and it keeps that version until **Update** is pressed. Check that the Windows client version matches it
- [x] Start it once so it creates its folders, then stop it. **jbrain2:** done; a fresh test world is in slot 1
- [ ] Copy the world in. **jbrain2:** use **Minecraft → Worlds → Import** with a `.mcworld` instead of copying folders. A `.mcworld` is a zip of the world folder's contents (`level.dat`, `levelname.txt`, `db/`…). From a Windows client world, use Play → pencil (Edit) → Export World. Not done yet
- [x] Check `level-name` matches the folder exactly. **jbrain2:** set by the sidecar when a slot is loaded
- [ ] Re-enter the allowlist and operators. **jbrain2:** add gamertags on the Minecraft screen's allowlist and turn `allow-list` on (applies at the next restart). Operators (`permissions.json`) have no PWA control yet
- [x] Set resource limits and restart policy. **jbrain2:** 2 GB `mem_limit` and a 60 s stop grace in its compose file
- [ ] Open the firewall only for the game ports. **jbrain2:** the container uses the host network; the game and the token-guarded control port (19180) are reachable on the LAN, and nothing is forwarded from the router

### Test and cut over
- [ ] From another device on the LAN: `curl http://<linux-box-ip>:19132/v1/join` should return name, version, and player count (NetherNet; per the itzg README)
- [ ] Join from a client and check: inventory, spawn/bed, builds near spawn, allowlist, op permissions
- [ ] Stop the Windows server (don't delete it)
- [ ] Point players at the new address (update router port forwarding if players join from outside)
- [ ] Keep the Windows copy and rollback zip for at least two weeks

**Rollback:** stop the container, start Windows BDS with the rollback copy. Anything built after cutover would need the latest Linux backup copied back.

## Automated backups (Stage 1)

**jbrain2** has on-demand backups, safety backups before risky actions, retention, restore and download (see [the table above](#already-built-in-jbrain2-read-2026-10-10)). Still missing for this stage: a **schedule**, an **off-box copy**, and a **test restore** of the real world. Until those exist, download a backup from the Minecraft screen after each session and keep it off the box (for example on Drive).

- [ ] Backup script on the host:
  1. `send-command save hold` (or write to the console)
  2. Poll `save query` and read the file list from the logs or console
  3. Copy the listed files and truncate them to their lengths
  4. `save resume`
  5. Zip to `/backups/<world>/<YYYY-MM-DD_HHMM>.zip`
- [ ] Schedule: every 6 hours while the server is up, plus one before every BDS upgrade
- [ ] Retention (suggested): keep all from the last 48 h, 1/day for 14 days, 1/week for 8 weeks
- [ ] Off-box copy of at least the daily backup (a second disk or cloud)
- [ ] **Test a restore** into a scratch container once a month

## Snapshot pipeline (Stage 2)

**jbrain2:** not built. Its world index (M4) and maps (M8) are planned, and a world copy can only leave the box as a download from the PWA. So for now a snapshot reaches Grok Bot only if Jeffrey downloads one and puts it where Grok Bot can read it.

After each backup (or once a day), deliver the latest zip somewhere Grok Bot can already reach:

| Option | How | Notes |
| --- | --- | --- |
| **Private GitHub repo** (e.g. a separate `Bleepbloop_City-data` repo) | Upload the zip as a **release asset**, or commit derived JSON/PNGs | Grok Bot already has GitHub access. Keep raw zips as release assets, not in git history. |
| **Google Drive folder** | The host uploads the zip to a shared folder | Grok Bot can already read Drive. |
| Public `Bleepbloop_City` repo | Commit map images / summaries | ⚠️ **Public:** maps, base locations, and inventories would be visible to anyone |

> **⚠️ Decision for Jeffrey:** this repo is **public**. Raw world data, map renders (which show base locations), and player inventories should go to a **private repo or Drive**. Only commit to this public repo what you're happy for anyone to see (e.g. checklists auto-ticked from snapshots, or cropped maps).

### What Grok Bot does with each snapshot
- [ ] Download and unzip the snapshot (never the live world)
- [ ] Render maps:
  - **uNmINeD CLI**: lists support for Bedrock up to 26.50, with Linux x64/ARM64 CLI builds. ([downloads](https://unmined.net/downloads/))
  - **bedrock-viz**: Google-Maps-style web viewer and overlays. **Unsure** whether it reads 26.50 worlds; its repo hasn't been updated since 2024, so test it. ([repo](https://github.com/bedrock-viz/bedrock-viz))
- [ ] Analyze with **amulet-core** (Python library that reads and writes Bedrock and Java saves). **Unsure** whether the current release supports 26.50 worlds, so test it. ([repo](https://github.com/Amulet-Team/Amulet-Core), [docs](https://amulet-core.readthedocs.io)) Targets:
  - Player inventory, ender chest, and spawn. Players are stored by an internal ID; map each one to a gamertag once and keep the mapping in the private store.
  - Chest totals (e.g. how full the storage wall is)
  - Detect built blocks to auto-check plan items (bed, farm, chests, copper golems…)
  - Animal counts near base; villages
- [ ] Update `progress/tracker.md` and `progress/session-log.md` from the diffs since the last snapshot
- [ ] Commit map images to wherever Jeffrey decides (private by default)
- **Chat assistant reuse:** the [chat assistant](chat-assistant.md#structure-and-ore-search-world-files--seed) uses the same consistent-copy method for its own **on-box** snapshots (more often, never uploaded) to index ores and structures for `/ask`.
- **Chunker** (Hive Games, open source) converts worlds between Java and Bedrock. It isn't needed for this migration, but it's noted in case a Java copy is ever wanted. ([repo](https://github.com/HiveGamesOSS/Chunker))

## Stages

### Stage 0 — Migrate
- [ ] Everything in the migration checklist above
- [ ] Players can join the Linux server, and the Windows copy is kept as rollback

### Stage 1 — Automated backups
- [ ] Backup script + schedule + retention + off-box copy
- [ ] One successful test restore

### Stage 2 — Snapshot analysis
- [ ] Decide where snapshots go (private repo / Drive / public)
- [ ] Automated upload after backups
- [ ] Grok Bot renders a map and posts a status update from a snapshot
- [ ] Gamertag ↔ player ID mapping stored privately

### Stage 3 — Live API
- [ ] See [live-api.md](live-api.md)

## Open questions for Jeffrey

- [x] Container tooling: answered by jbrain2 (Docker Compose, its own `debian:trixie-slim` image)
- [ ] World name and current BDS/client version on Windows? (The box runs BDS 1.26.52.3; jbrain2 sets `level-name` itself)
- [ ] Where should snapshots and maps go: private repo, Google Drive, or (parts of) this public repo?
- [ ] Do players join from outside your home network? (Affects port forwarding after cutover.)
- [ ] How much RAM/CPU can the AI server spare while LLMs run?

## Done when

- [ ] The server runs in a container on the Linux box with limits, a restart policy, and a mounted world volume
- [ ] Backups run automatically with retention, and a restore has been tested
- [ ] Snapshots arrive somewhere Grok Bot can read, and a map + tracker update has been produced from one
- [ ] The Windows copy has been kept until the new setup proved stable
