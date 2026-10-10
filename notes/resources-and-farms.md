# Resources and farms

## Farms

| Farm | Type | Location | Status | Notes |
| --- | --- | --- | --- | --- |
| Tree farm (12 trees replanted for easier wood) | Trees | Not recorded yet | 🟨 Planted 2026-10-06 | Session 1. Plus 9 oak growing (Session 2, 2026-10-07) |
| Cherry tree farm (cherry trees replanted for more saplings) | Trees | Not recorded yet | 🟨 Replanted 2026-10-07 | Session 2. Cherry wood is going into the first house |
| Starter crop farm (9×9, wheat → carrots/potatoes) | Crops | Next to water (spot not recorded) | 🟨 Planted 2026-10-07 | Phase 2. About 15 wheat, still not mature as of Session 3 (reported 2026-10-10): crops only grow with a player nearby and in light 9+ ([why the wheat is slow](../progress/session-plan.md#why-the-wheat-is-slow)). Fence and light unconfirmed |
| Animal pen (cows, sheep, chickens) | Animals | Not recorded yet | 🟨 Built 2026-10-07, empty | Phase 2. Still empty as of Session 3 (reported 2026-10-10); lead cows in with wheat once it's ready |
| Starter sugar cane (by water) | Crops | Not recorded yet | 🟨 Started 2026-10-07 (unconfirmed) | A couple of stalks found in Session 2; planting by the water not confirmed. Paper for maps and books |
| Crop farm + composter (food wing) | Crops | | ⬜ Not started | Phase 4 |
| Animal barn with a gate | Animals | | ⬜ Not started | Phase 4 |
| Sugar cane farm | Auto / semi-auto | | ⬜ Not started | Books for enchanting; Phase 4–5 |
| Iron farm | Auto | | ⬜ Not started | Phase 5. Build it near the sorter, inside the [ticking area](../plans/multiplayer-server.md#ticking-area-iron-farm-and-item-sorter). On Bedrock, golems only spawn with a player nearby, so it isn't AFK-free. Fix: a parked bot ([AFK bot options](../plans/multiplayer-server.md#keeping-the-iron-farm-running-afk-bot-options)) |
| Mob grinder or spawner farm | Auto | | ⬜ Not started | Phase 5 |
| Mob switch or shard farm | End-game | | ⬜ Not started | After elytra |
| Wither skeleton farm | End-game | | ⬜ Not started | After elytra |
| Gold farm (zombified piglins) | Auto / semi-auto | | ⬜ Not started | Phase 5, after the first portal. Steady gold for golden armor and bartering. See [below](#gold-farm-zombified-piglins-bedrock) |

### Gold farm: zombified piglins (Bedrock)

Gold is an ongoing side task until this exists ([why](../progress/session-plan.md#future-session-blaze-rods-and-brewing-fire-resistance)). The build design is Jeffrey's call; these are the Bedrock mechanics it relies on, checked on the wiki 2026-10-10 ([Zombified Piglin](https://minecraft.wiki/w/Zombified_Piglin), [Tutorial: Zombified piglin farming](https://minecraft.wiki/w/Tutorial:Zombified_piglin_farming)):

- **Portal spawning:** each Nether portal block in the **Overworld** has a chance to spawn a zombified piglin when it gets a random tick: 0.05% on Easy, 0.1% on Normal, 0.15% on Hard, none on Peaceful. So the open [difficulty setting](../plans/multiplayer-server.md#open-server-settings-jeffrey-to-decide) changes the rate. Portal spawns don't count toward the mob cap.
- **Bedrock-only boost:** every portal block is ticked the moment a portal is lit, so a big portal (up to 23×23) that's repeatedly lit and put out spawns them quickly. That on/off cycling is what Bedrock gold farms are built around; Java farms need many more portals instead.
- **Where they appear on Bedrock:** one block east or south of the portal, depending on which way it faces. Slabs and light don't stop it. **Portals below Y=0 never spawn them.**
- **Other source:** they also spawn naturally in nether wastes and crimson forests (and fortresses), which is what Nether spawning-platform farms use.
- **Drops:** 0–1 gold nugget each (9 nuggets = 1 ingot), plus a 2.5% chance of a gold ingot when a player kills it, and the golden sword 25% of the time on Bedrock. A Looting sword raises all of these.
- **Shared anger:** hitting one makes every zombified piglin nearby hostile, so keep the kill spot enclosed and away from any portal they could walk back through.
- **Needs a player nearby,** like the iron farm: nothing spawns or ticks outside simulation distance.

## Mining

- Iron and coal: staircase down to around Y=16 (Phase 2).
- Branch mine: Y=-54 or around diamond level, once you have iron picks to spare (Phase 4).

| Mine | Location | Depth (Y) | Notes |
| --- | --- | --- | --- |
| Caves near base | Not recorded yet | Not recorded | Session 3 (reported 2026-10-10): a little iron, a bunch of coal and copper. No staircase mine yet. Write the entrance X Y Z in [coordinates](coordinates.md) |

## Villagers and trades

Priority: librarians for Mending and Unbreaking.

| Villager | Profession | Key trade | Locked? | Notes |
| --- | --- | --- | --- | --- |
| | Fletcher | | | |
| | Librarian | | | |
| | Toolsmith | | | |

## Storage layout

Storage wall chests: wood, stone, ores, food, mob drops, redstone, junk, plus one input chest by the door.

This grows into the big goal: [automated item sorter](../plans/storage-and-sorting.md) (hopper chest hall + copper golem gallery; [grouping](../plans/storage-layout.md)). Track it here as it gets built.

| Area | Type (golem / hopper sorter / manual) | Location | Golems | Notes |
| --- | --- | --- | --- | --- |
| Storage wall input chest | | | | Copper chest? |
| | | | | |
