# Multiplayer server

If this is a multiplayer server, do these early.

## Server setup
- [ ] Set spawn protection
- [ ] Set a world border

## Server config

Server settings and world-level config live here. For the files themselves (`server.properties`, `allowlist.json`, `permissions.json`) and moving them to the Linux box, see [server migration](server-migration.md#verified-facts-this-plan-relies-on).

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
- **New golems only spawn while someone is within that range of the farm.** So put the iron farm where people actually spend time: near the home base and the sorter.

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
