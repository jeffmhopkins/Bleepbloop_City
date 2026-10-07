# Multiplayer server

If this is a multiplayer server, do these early.

## Server setup
- [ ] Set spawn protection
- [ ] Set a world border

## Server config

Server settings and world-level config live here. For the files themselves (`server.properties`, `allowlist.json`, `permissions.json`) and moving them to the Linux box, see [server migration](server-migration.md#verified-facts-this-plan-relies-on).

### Game version and new game rules

- **Keep the server on the clients' version.** Bedrock **26.60** is scheduled for **October 27, 2026** ([wiki](https://minecraft.wiki/w/Bedrock_Edition_26.60)). When players' games update, plan to update the server to match the same day, or they may not be able to join.
- **Locator bar:** friends show as colored markers on the HUD, which helps with coordinates off. The Bedrock game rule is `playerwaypoints` (since 26.30): `everyone` (default) or `off` ([Game rule](https://minecraft.wiki/w/Game_rule)). Players can hide their marker by sneaking or wearing a carved pumpkin.
- **Group travel:** a harnessed [happy ghast](happy-ghast.md) carries 4 players.

### Ticking area: iron farm and item sorter

**Plan:** keep the [item sorter](storage-and-sorting.md) and the iron farm inside a permanently loaded area, so hoppers, furnaces, and item transport keep running when nobody is standing next to them. On Bedrock that's a **ticking area**, made with `/tickingarea` (Bedrock and Education only; Java uses `/forceload` instead).

**Commands** ([Commands/tickingarea](https://minecraft.wiki/w/Commands/tickingarea))
- **Box:** `tickingarea add <from: x y z> <to: x y z> [name] [preload]` loads every chunk that overlaps the rectangle.
- **Circle:** `tickingarea add circle <center: x y z> <radius: 0–4 chunks> [name] [preload]`. Despite the name it's a square: all chunks within *r* chunks of the center chunk, diagonals included, so radius 4 = 9×9 = 81 chunks ([Ticking area](https://minecraft.wiki/w/Ticking_area)).
- **Y is ignored.** A chunk is the full world height, but you still have to type some Y value.
- **List:** `tickingarea list` shows the current dimension; `tickingarea list all-dimensions` shows all of them. Listed coordinates snap to chunk corners or centers.
- **Remove:** `tickingarea remove <name>`, `tickingarea remove <x y z>` (every area containing that point), or `tickingarea remove_all`.
- **Preload:** `tickingarea preload <name|x y z> [true|false]`. Preloaded areas load before other chunks when the world starts. Without preload, an area loads after the world launches.
- **Example from the wiki:** `/tickingarea add circle ~ ~ ~ 2 Homebase`, run while standing in the center chunk, makes a 5×5-chunk area.
- **Coordinates:** coordinates are hidden on our server, so the easiest way is for an operator to run the circle form in-game with `~ ~ ~` while standing at the center. A console command needs real coordinates.

**Limits** ([Commands/tickingarea](https://minecraft.wiki/w/Commands/tickingarea), [Ticking area](https://minecraft.wiki/w/Ticking_area))
- Up to **10 ticking areas per world**. Adding an 11th fails.
- Each area can be up to **100 chunks**. A circle radius must be 0–4.
- **Permissions:**
  - The command needs operator level 1 and cheats; Microsoft Learn lists the permission as "Game Directors".
  - On BDS, cheats are controlled by `allow-cheats` in `server.properties` (default `false`).
  - The wiki says using commands makes a world ineligible for achievements.
  - **Unverified:** whether typing the command in the BDS console works with `allow-cheats=false`. Test it before changing the setting.
- **Persistence (implied, not stated):** the wiki says areas load when the world launches (preloaded ones first), which means they're saved with the world. Confirm with `tickingarea list` after the first server restart, and again after the [migration](server-migration.md).

**What keeps running with no player nearby** ([Ticking area](https://minecraft.wiki/w/Ticking_area), [Chunk § Bedrock](https://minecraft.wiki/w/Chunk))
- **At least one player has to be online in the same dimension (the Overworld).** With nobody online, or everyone in the Nether or End, the area doesn't tick.
- **Works:** redstone, as long as the whole circuit is inside the ticking area. Also water and lava flow, lava destroying items (the disposal), item despawn and hopper pickup, minecarts, crop and sapling growth, and mobs moving.
- The wiki says each chunk in the area updates "exactly as if it were perpetually in a player's chunk update range". That covers hoppers and furnaces, though the wiki doesn't list them by name.
- **Stops at the edge:** an entity (items in a stream, a minecart, a mob) that leaves the area freezes at the first outside chunk until a player loads it. So **every input and output link has to be inside the area.**
- **Mob spawning does NOT happen without a player.** The wiki: "Mob spawning does not occur in ticking area chunks without the presence of a player, as all forms of mob spawning attempts are done in a radius centered on a player." (The one exception is zombified piglins from portals.)

**Iron farm verdict: a ticking area alone does NOT make an AFK-free iron farm on Bedrock.**
- On Bedrock, village iron golems spawn only if the **village center is within a player's simulation distance** ([Iron Golem § Bedrock](https://minecraft.wiki/w/Iron_Golem)).
- The wiki's approximate maximum player distance from the village center is **8 × simulation distance + 32 blocks horizontally** and **8 × simulation distance + 12 blocks vertically**.
- On BDS, `tick-distance` (default **4**, range 4–12) sets how many chunks from a player are ticked ([server.properties](https://minecraft.wiki/w/Server.properties)). Treating that as the simulation distance (my reading, not stated outright) gives about **64 blocks horizontal / 44 vertical** at the default.
- **Village rules on Bedrock:**
  - At least 20 beds and 10 villagers.
  - 75% of villagers (not counting nitwits) have reached their workstation in the last day.
  - 100% of villagers are linked to a bed.
  - One extra golem per 10 more villagers.
  - About 1 spawn attempt every 35 s.
- **What the ticking area does do for the iron farm:** it keeps the kill and collection side running (lava, hoppers, the link to the sorter) and keeps villagers working, so iron already produced keeps flowing to the sorter.
- **New golems only spawn while someone is within that range of the farm.** So put the iron farm where people actually spend time: near the home base and the sorter. For a bot that stays at the farm, see [AFK bot options](#keeping-the-iron-farm-running-afk-bot-options).

**Spawn chunks: Bedrock doesn't have any documented always-loaded spawn chunks.**
- The wiki's spawn chunk page covers a Java-only mechanic and points Bedrock readers to ticking areas instead ([Spawn chunk](https://minecraft.wiki/w/Spawn_chunk)).
- Java itself removed spawn chunks in 1.21.9.
- The Bedrock chunk-loading section only lists chunks near players and chunks loaded by `/tickingarea` as active ([Chunk § Bedrock](https://minecraft.wiki/w/Chunk)).
- So the base being near world spawn doesn't keep anything loaded by itself.

**How to set it up**
- One ticking area covering **the sorter, the iron farm, and every link between them**: the input line, the farm-to-sorter item line, the smelter, overflow, and lava.
- **Put the iron farm close to the sorter so one area covers both, if it fits in 100 chunks** (a radius-4 circle = 81 chunks). If it doesn't fit, use two areas whose edges overlap or touch along the item line, so nothing crosses an unloaded chunk.
- That leaves 8–9 areas for later farms.
- Name it (e.g. `sorter`) and use `preload true` so it's loaded before the farm starts sending items.
- Leave chunk room on the sorter's open expansion end ([storage rule 8](storage-layout.md#adjacency-rules)) so later slices stay inside the area. Otherwise, extend or add an area when you add slices.
- Checklist:
  - [ ] Test whether `tickingarea` works from the BDS console with the current `allow-cheats` setting
  - [ ] Add the sorter + iron farm area, then check it with `tickingarea list`
  - [ ] Confirm it's still there after a server restart and after the Linux migration

#### Keeping the iron farm running: AFK bot options

**Short answer:** yes, very likely, but not with vanilla settings alone. Golems need a *player* near the village. That's a confirmed, unfixed Bedrock bug report: [MCPE-226025](https://mojira.dev/MCPE-226025), "Iron Golems do not spawn in tickingareas", still open in 26.40. So the job is to give the farm a player that never leaves. Ranked by ease:

| # | Option | How | Counts as a player for golems? | Main caveats |
| --- | --- | --- | --- | --- |
| 1 | **Canopy simplayer** (recommended first try) | [Canopy](https://github.com/ForestOfLight/Canopy) (MIT, v1.6.2 "for MC 26.50", 2026-09-16) on the server. Stand at the farm and run `/playerjoin <name>`. Turn on the `simplayerRejoining` global rule so it comes back after a restart. | **Likely, unverified.** It's a real `Player` entity, and Understudy (now part of Canopy) advertised "AFK your farms, load areas". An Understudy issue reports a simplayer loading an Overworld chunk well enough to run a mob switch ([Understudy #14](https://github.com/ForestOfLight/Understudy/issues/14)). Nobody we found has tested golem spawning specifically. | Needs the **Beta APIs** experiment (permanent, disables achievements). Not supported by Mojang: beta APIs can change in any update. |
| 2 | **Spare real device** | An old phone, tablet or PC logged into a second Microsoft account, parked at the farm. | **Yes**: it's a normal client. | Needs a second account and a device left running. Set `player-idle-timeout=0` (default 30 min kicks idlers) ([server.properties](https://minecraft.wiki/w/Server.properties)). |
| 3 | **Headless bot client** in a container next to BDS | [bedrock-protocol](https://github.com/PrismarineJS/bedrock-protocol) (Node) or [gophertunnel](https://github.com/Sandertv/gophertunnel) (Go) joins as a second account and just stands there. | Should, as a real connection, but **unverified**: a bot that sends no movement input may not be treated like an active client. | 26.50 NetherNet (details below). Second Microsoft account. Idle timeout. More code to maintain. |
| — | Endstone / LeviLamina | [Endstone](https://github.com/EndstoneMC/endstone) (BDS plugin platform, supports 1.26.52) has no built-in fake player that we found. Non-Script-API fake players such as LeviLamina's can crash BDS when a Script API pack is loaded ([Canopy #72](https://github.com/ForestOfLight/Canopy/issues/72)). | — | Set aside |

**Facts behind option 1** (Script API, 26.50)
- `@minecraft/server-gametest` has a top-level **`spawnSimulatedPlayer(location, name, gameMode)`**. Microsoft Learn: it "spawns a simulated player that isn't associated to a specific Test"; it stays until `disconnect()`. So **no GameTest needs to be running**. The module is still beta ([Microsoft Learn: server-gametest](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-gametest/minecraft-server-gametest?view=minecraft-bedrock-experimental)). Canopy uses exactly this call (`Understudy.js`).
- **Restarts:** a simulated player doesn't survive a restart on its own. Canopy's `simplayerRejoining` rule (default **off**) saves the online simplayers at shutdown and rejoins them at startup. `simplayerSaving` (default on) keeps their inventory and location ([Canopy wiki: Global Rules](https://github.com/ForestOfLight/Canopy/wiki/Global-Rules)).
- **Spawn it in the Overworld.** Canopy warns that simplayers spawned in another dimension don't load chunks unless a real player is in that dimension (a Mojang bug) ([Understudy #14](https://github.com/ForestOfLight/Understudy/issues/14)).
- **On BDS:** add `@minecraft/debug-utilities` to `config/default/permissions.json` ([Canopy wiki: Adding Canopy to Servers](https://github.com/ForestOfLight/Canopy/wiki/Installation-&-Updates#adding-canopy-to-servers)). Check that the allowed modules also cover what Canopy's manifest asks for: `server`, `server-ui`, `server-gametest`.
- **Beta APIs:**
  - On Bedrock, turning on an experiment **disables achievements**, and an experiment **can't be turned off** once the world has it. Turning one on for an existing world makes a copy first ([Experiments](https://minecraft.wiki/w/Experiments)).
  - BDS has no world-options screen, so turn it on in a client on a **copy** of the world, then put that copy on the server.
  - The world already loses achievements once cheats are on for `/tickingarea`.

**Facts behind option 3**
- 26.50 BDS defaults to the **NetherNet** transport. RakNet is still available with `transport=raknet` ([itzg README](https://github.com/itzg/docker-minecraft-bedrock-server#nethernet)). Our [migration notes](server-migration.md#verified-facts-this-plan-relies-on) record that 26.51 may only support NetherNet.
- bedrock-protocol joined BDS 1.26.51 over NetherNet only with `enable-lan-visibility=true`, and that test used `online-mode=false`. Direct HTTP signaling is still open ([bedrock-protocol #830](https://github.com/PrismarineJS/bedrock-protocol/issues/830)).
- gophertunnel merged NetherNet dialing in Aug 2026 (PRs #486, #508). We haven't tested it against our server.
- **Don't use `online-mode=false`** to get a bot in. With it off, players aren't authenticated to Xbox Live ([server.properties](https://minecraft.wiki/w/Server.properties)), so anyone who can reach the port can join under any name, including an allowlisted one. Use a second Microsoft account with normal sign-in and add it to the allowlist.

**Same bot as the future companion.** The [companion plan](live-api.md) already ranks Canopy simplayers (#2) and our own `SimulatedPlayer` script as the base for a follow-and-fight bot. bedrock-protocol and gophertunnel are #5 and #5b there. Installing Canopy for the farm is the first step of that plan too. The farm bot can stay parked while a second simplayer becomes the companion.

**Recommended path**
1. On a **copy** of the world (local client is fine): turn on Beta APIs, add Canopy, build or borrow a test village, and add a ticking area.
2. Run `/playerjoin IronBot` at the farm. Send your real player far away, then log off completely.
3. Watch the collection chest; a ~35 s spawn cycle shows up fast.
4. Test both ways: real player far away, and no real players online at all. A simulated player is the only "player" when nobody's online. Whether that satisfies the ticking area's "a player in the dimension" rule is **unverified**, and this test answers it.
5. If golems spawn, do it on the real server: Beta APIs on a copy, Canopy, `permissions.json`, `simplayerRejoining` on. Then check it after a server restart and after the Linux migration.
6. If they don't, fall back to option 2 (simplest) or option 3 (fully headless, more work).
- Checklist:
  - [ ] Simplayer test on a world copy: golems with real player far away
  - [ ] Simplayer test on a world copy: golems with no real players online
  - [ ] Decide: Canopy on the live world (Beta APIs permanent) vs. spare device vs. headless bot

## Public hub at spawn
- [ ] Map
- [ ] Rules
- [ ] Nether portal
- [ ] Community chests

## Personal bases and plots
- [ ] Keep personal bases a few hundred blocks out from spawn
- [ ] Claim or mark plots before someone else walls in the village

## Tips

- Straw beds are handy for travel because they do not steal your spawn point back at the base.

## Plots

| Player | Plot / base | Coordinates | Notes |
| --- | --- | --- | --- |
| | | | |

## Server rules

_Write the rules here._
