# Big goal: Live API (tokenized connection to the server)

**Goal:** A behavior pack on the Bedrock Dedicated Server sends live game events (joins, deaths, block placements, positions, inventories) to a small web service on Jeffrey's Linux box. Grok Bot reads that service through a **read-only, token-protected** API to keep Bleepbloop City's plans and logs current.
**Status:** ⬜ Not started
**Depends on:** [Server migration](server-migration.md) Stage 0 (the server must be BDS on the Linux box)

> **Sources (checked 2026-10-07):**
> [Scripting Bedrock Dedicated Server (Microsoft Learn)](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/scripting?view=minecraft-bedrock-stable) ·
> [@minecraft/server-net module](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/minecraft-server-net?view=minecraft-bedrock-stable) ·
> [HttpClient](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/httpclient?view=minecraft-bedrock-experimental) ·
> [ServerSecrets](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-admin/serversecrets?view=minecraft-bedrock-experimental) ·
> [WorldAfterEvents](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/worldafterevents?view=minecraft-bedrock-stable) ·
> [EntityInventoryComponent](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/entityinventorycomponent?view=minecraft-bedrock-stable) ·
> [System (runInterval)](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/system?view=minecraft-bedrock-stable) ·
> [Bedrock Wiki: Script Requests API](https://wiki.bedrock.dev/scripting/script-net) ·
> [Cloudflare Access service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/) ·
> [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve) · [Tailscale Funnel](https://tailscale.com/docs/features/tailscale-funnel)

## Verified facts about the Bedrock side

- **`@minecraft/server-net` is BDS-only.** It provides HTTP requests (plus WebSocket types). It does **not** work in the normal game client or on Realms. ([module docs](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/minecraft-server-net?view=minecraft-bedrock-stable))
- **It's pre-release.** The module is marked "still in pre-release… may change or be removed", and only beta version strings are listed (e.g. `1.0.0-beta.…`). The BDS scripting doc calls these "experimental… part of the Beta APIs program", so expect breakage on BDS updates and back up first. ([BDS scripting](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/scripting?view=minecraft-bedrock-stable))
- **Beta APIs experiment.** BDS's `config/default/permissions.json` lists the modules available "to worlds with the Beta APIs experiment enabled", so the world needs that experiment on. **Unsure:** the exact way to switch it on for an existing BDS world. Test on a *copy* of the world first, because experiments change the world.
- **The net module is not allowed by default.** BDS creates `config/default/permissions.json` on first run. The default list is `@minecraft/server-gametest`, `@minecraft/server`, `@minecraft/server-ui`, `@minecraft/server-admin`, `@minecraft/server-editor`, without `server-net`. ([BDS scripting](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/scripting?view=minecraft-bedrock-stable))
  - **Recommended:** give *only this pack* access by creating `config/<script-module-uuid>/permissions.json`. The folder name is the UUID of the `script` module in the pack's `manifest.json`. Keep `config/default` minimal:
    ```json
    { "allowed_modules": ["@minecraft/server", "@minecraft/server-admin", "@minecraft/server-net"] }
    ```
    (Example shape. Include whichever modules the pack actually imports.)
- **Variables and secrets.**
  - `variables.json` holds settings such as the ingest URL; scripts read it with `variables.get()` from `@minecraft/server-admin`.
  - `secrets.json` holds the ingest token, read with `secrets.get()`. Secrets are **not exposed to the script**: they resolve at request time inside objects like `HttpHeader`.
  - Both files go in `config/default/` or the pack's `config/<uuid>/` folder. ([BDS scripting](https://learn.microsoft.com/en-us/minecraft/creator/documents/bedrockserver/scripting?view=minecraft-bedrock-stable), [ServerSecrets](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-admin/serversecrets?view=minecraft-bedrock-experimental))
- **HTTP API.** `http.request(new HttpRequest(url))` with `method`, `headers` (`HttpHeader`), and a JSON `body`. The module also defines errors such as `HttpRequestLimitExceededError`, `RequestBodyTooLargeError`, `UriNotAllowedError`, and `TLSOnlyError`, so there are request limits and URI/TLS restrictions. **Unsure:** the exact limits and when TLS is required. Handle these errors, batch events, and test against the real ingest URL. ([HttpClient](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/httpclient?view=minecraft-bedrock-experimental))
- **Events available (stable `world.afterEvents`):** `playerJoin`, `playerLeave`, `playerSpawn` (first spawn vs. respawn flag), `entityDie`, `playerPlaceBlock`, `playerBreakBlock`, `playerDimensionChange`, `playerInventoryItemChange`, `blockContainerOpened` / `blockContainerClosed`, `entitySpawn`, `weatherChange`, and more. `chatSend` is pre-release only. ([WorldAfterEvents](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/worldafterevents?view=minecraft-bedrock-stable))
- **Inventory** comes from the player's inventory component (`EntityInventoryComponent` → `container`). **Positions** can be sampled on a timer with `system.runInterval`. **Unsure:** whether ender chest contents are readable from scripts. Assume they come from [world snapshots](server-migration.md#snapshot-pipeline-stage-2) instead.

## Components

```
BDS (container)                          Linux box                          Grok Bot (outside home network)
┌───────────────────────┐   POST JSON    ┌──────────────────────────┐   GET (read-only, token)
│ behavior pack         │ ─────────────▶ │ ingest/read web service  │ ◀──────────────────────── via tunnel
│ @minecraft/server-net │  (ingest token)│ SQLite/Postgres store    │
└───────────────────────┘                └──────────────────────────┘
```

### 1. Behavior pack ("bleepbloop-telemetry")
- [ ] `manifest.json` with a `script` module (its UUID names the `config/<uuid>/` folder) and dependencies on `@minecraft/server`, `@minecraft/server-admin`, `@minecraft/server-net` (beta versions matching the BDS build)
- [ ] `config/<uuid>/permissions.json` allowing those modules
- [ ] `config/<uuid>/variables.json`: `{ "ingestUrl": "http://bleepbloop-api:8080/ingest" }` (example; the container-network name or LAN address of the service)
- [ ] `config/<uuid>/secrets.json`: the **ingest** token. It lives only on the box and is never committed.
- [ ] Subscribe to events (below), queue them in memory, and POST a batch every few seconds and on player leave
- [ ] Position + inventory sample every 60 s per online player (`system.runInterval`)
- [ ] Catch and log `HttpRequestLimitExceededError` / network errors, and drop or retry with backoff

### 2. Events to send

| Event | Source | Why |
| --- | --- | --- |
| `join` / `leave` | `playerJoin`, `playerLeave` | Session log: who played, when |
| `spawn` | `playerSpawn` | First join vs. respawn (deaths) |
| `death` | `entityDie` (filter to players) | Session log "Deaths" |
| `block_placed` / `block_broken` | `playerPlaceBlock`, `playerBreakBlock` | Auto-check plan items (bed, chests, copper blocks…) |
| `dimension_change` | `playerDimensionChange` | Nether trips, portal location |
| `position` | `system.runInterval` sample | Coordinates (handy while coordinates are off in-game) |
| `inventory` | inventory component, sampled + on `playerInventoryItemChange` | Phase checklists (iron tools, food stack…) |

### 3. Payloads (EXAMPLE SHAPES, not a fixed format)

Batch from the pack to `POST /ingest`:
```json
{
  "server": "bleepbloop-city",
  "sent_at": "2026-10-07T18:00:00Z",
  "events": [
    { "type": "join",  "t": "2026-10-07T17:58:12Z", "player": { "id": "<player.id>", "name": "<gamertag>" } },
    { "type": "position", "t": "2026-10-07T17:59:00Z", "player": { "id": "<player.id>" },
      "dimension": "minecraft:overworld", "x": 0, "y": 64, "z": 0 },
    { "type": "block_placed", "t": "2026-10-07T17:59:30Z", "player": { "id": "<player.id>" },
      "block": "minecraft:chest", "x": 0, "y": 64, "z": 0, "dimension": "minecraft:overworld" },
    { "type": "death", "t": "2026-10-07T17:59:45Z", "player": { "id": "<player.id>" }, "cause": "<damage cause>" }
  ]
}
```

Inventory sample:
```json
{ "type": "inventory", "t": "2026-10-07T18:00:00Z", "player": { "id": "<player.id>" },
  "slots": [ { "slot": 0, "item": "minecraft:stone_pickaxe", "amount": 1 },
             { "slot": 1, "item": "minecraft:bread", "amount": 12 } ] }
```
(The values above are placeholders, not real game data.)

### 4. Ingest/read web service (on the Linux box)

Small service (any stack, e.g. Python FastAPI or Node) + SQLite to start.

| Method | Path | Auth | Purpose |
| --- | --- | --- | --- |
| `POST` | `/ingest` | **ingest token** (from the pack) | Accept event batches. Validate the schema and size, and reject unknown types. |
| `GET` | `/status` | read token | Server up? Players online, last event time, BDS version |
| `GET` | `/players` | read token | Known players: id, gamertag, last seen, online |
| `GET` | `/players/{id}` | read token | Last position, dimension, spawn info |
| `GET` | `/players/{id}/inventory` | read token | Latest inventory sample |
| `GET` | `/events?since=<ISO time>&type=<type>` | read token | Event stream for session logs (paged) |

- **Bearer tokens** (`Authorization: Bearer <token>`). Use **two separate tokens**: an **ingest** token (write, used only by the pack on the box) and a **read** token (Grok Bot, read-only). The read token can never call `/ingest`.
- **Rotation:** support two valid read tokens at once (current + next), so rotation means: add the new one, update Grok Bot's secret, then remove the old one. Rotate every 90 days or immediately if a token is exposed.
- **Store tokens as secrets:** environment variables or a secrets file on the box, hashed in the service config if possible. Never in git, never in chat.
- **Grok Bot's read token** will be handed over later through a **secure secret input**. It is never pasted into chat and never committed to any repo.
- **Rate limits:** e.g. 60 requests/min per token on read endpoints, and a body-size cap on `/ingest`.
- **Data retention (suggested):** raw position samples for 14 days, then down-sampled (hourly) for 90 days. Events (join/leave/death/block) for 1 year. Latest inventory per player kept, history for 30 days.

### 5. Network exposure: how Grok Bot reaches the service

Grok Bot's computer is **outside** Jeffrey's home network.

| Option | How it works | Pros | Cons |
| --- | --- | --- | --- |
| **Cloudflare Tunnel + Access service token** | `cloudflared` on the box publishes only the read API. A Cloudflare Access policy requires a **service token**: `CF-Access-Client-Id` + `CF-Access-Client-Secret` headers, or a single configurable header. | No inbound ports. Auth happens at Cloudflare before traffic reaches the box. Service tokens support rotation with a grace period (1 h–30 days), expiry, and revocation. | Needs a Cloudflare account. **Unsure:** whether a domain on Cloudflare is required for the hostname; check Cloudflare's tunnel docs. |
| **Tailscale Funnel** | Publishes a local port at a public `https://<node>.<tailnet>.ts.net` URL (ports 443/8443/10000, TLS only) | Easy, no domain needed | **Public to anyone with the URL**, so the app's bearer token is the only lock. Tailscale's docs warn against exposing sensitive data this way. |
| **Tailscale Serve** | Shares the port only inside the tailnet | Private | Grok Bot's computer would need to join Jeffrey's tailnet (a separate decision) |
| **Push-only** | The box pushes summaries/snapshots to a private GitHub repo or Google Drive on a schedule | **Nothing exposed**, and Grok Bot can already read GitHub and Drive | Not live (minutes to hours old) |

**Recommendation:**
1. **Start push-only.** It covers most of what's useful (the session log, tracker, maps) with zero inbound exposure. Same delivery as the [snapshot pipeline](server-migration.md#snapshot-pipeline-stage-2).
2. When live data is wanted, use **Cloudflare Tunnel + an Access service token**, *plus* the app's own read bearer token (two locks). Use Tailscale Funnel + bearer token only if Cloudflare isn't an option.

### 6. Security notes
- [ ] **Never expose BDS ports beyond the game port(s).** No script debugger, no admin ports, and no `/ingest` to the internet.
- [ ] The tunnel publishes **only** the read endpoints. `/ingest` listens only on the container network / localhost.
- [ ] Grok Bot's token is **read-only**. No endpoint can run commands, change the world, or touch BDS.
- [ ] Tokens live as secrets on the box (`secrets.json` for the pack, env/secret file for the service) and are rotated on a schedule.
- [ ] Rate limits + body-size caps, and log failed auth attempts.
- [ ] `server-net` access is granted only to this pack's `config/<uuid>/permissions.json`, not `config/default`.
- [ ] The repo is public: never commit tokens, URLs with tokens, `secrets.json`, or raw player data here.

## Stages

### Stage 3a — Pack + local service (no exposure)
- [ ] Enable Beta APIs on a **test copy** of the world first; confirm the world still loads
- [ ] Build the pack and per-pack `permissions.json` / `variables.json` / `secrets.json`
- [ ] Service with `/ingest` + read endpoints + SQLite, on the box only
- [ ] Verify events arrive: join, death, block placed, position, inventory

### Stage 3b — Push-only delivery
- [ ] Scheduled export of summaries (JSON) to the chosen private repo / Drive folder
- [ ] Grok Bot updates the session log from a pushed summary

### Stage 3c — Live read access
- [ ] Choose a tunnel (open question), and publish read endpoints only
- [ ] Create the read token and hand it to Grok Bot via secure secret input
- [ ] Rate limits, retention jobs, and a rotation runbook in place

## Open questions for Jeffrey

- [ ] OK to enable the **Beta APIs** experiment on the world (it's required for `server-net`, and pre-release APIs can change)?
- [ ] Preferred tunnel: Cloudflare Tunnel (do you have a Cloudflare account/domain?) or Tailscale?
- [ ] Service stack preference on the AI server (Python, Node, something else)?
- [ ] Where should pushed summaries go: private repo, Drive, or public repo (summaries only)?
- [ ] Are other players OK with position/inventory tracking? (Worth telling them.)

## Done when

- [ ] The behavior pack posts events from BDS to the service, with the net module allowed only for that pack
- [ ] Grok Bot can read `/status`, `/players`, `/events` with a read-only token through the chosen exposure method (or receives pushed summaries)
- [ ] Tokens are stored as secrets, rotation is documented and tested once, and rate limits and retention are running
- [ ] Nothing but the game port(s) and the protected read API is reachable from outside
