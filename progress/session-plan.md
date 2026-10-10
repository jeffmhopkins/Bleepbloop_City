# Session plan: Sessions 2–6

**Status:** 📋 Plan only. Nothing here is checked off until Jeffrey reports it in the [session log](session-log.md). Sessions 2 (played 2026-10-07) and 3 (reported 2026-10-10) are marked below (✅ done, ⏳ partial or not reported); Session 3's carry-over is at the top of Session 4.
**Based on:** [Session 1 (2026-10-06)](session-log.md), the [tracker](tracker.md), and the phase files ([1](../plans/phase-1-first-night.md), [2](../plans/phase-2-starter-outpost.md), [3](../plans/phase-3-pick-the-site.md), [4](../plans/phase-4-the-base.md), [5](../plans/phase-5-infrastructure.md)).
**Server:** Bedrock 26.50 (Wilderness Bound). Mechanics below were checked on the [Minecraft Wiki](https://minecraft.wiki) (2026-10-07, rechecked 2026-10-08).
**Coordinates are on** (reported 2026-10-08), so depths below are plain Y values read off the screen, and every new place gets its X Y Z written in [coordinates](../notes/coordinates.md).
**Time box:** each session is planned for **60 minutes**, plus an optional **"if you have 90"** block.

Building shapes, sizes and looks are Jeffrey's design. This plan only says what each build needs to *do*.

## Where Session 1 left off

- **Have:** bed (spawn set), crafting table, furnace, one chest, stone tools, logs and cobble, 12 replanted trees, extra wool, a little food.
- **Missing:** lighting, a food stack, a farm, an animal pen, a second chest, iron, a confirmed base site, and recorded locations (coordinates were off then; they're on now).

## How a session fits in real time

- **A Minecraft day is 20 minutes:** 10 minutes of daytime, then sunset, night and sunrise ([Daylight cycle](https://minecraft.wiki/w/Daylight_cycle)). If you sleep at every dusk, a 60-minute session gets about four or five daytimes.
- **Sleep at dusk.** In multiplayer, everyone in the Overworld has to be in bed at once, unless the server's `playerssleepingpercentage` game rule is lowered ([Bed](https://minecraft.wiki/w/Bed)). Its value is still an [open server setting](../plans/multiplayer-server.md#open-server-settings-jeffrey-to-decide). **At the default (100%), one other player in the Overworld who isn't in bed blocks the night skip** (players in the Nether or the End don't count). This whole sleep-at-dusk rhythm depends on it: once a second person plays at the same time, either everyone sleeps together or nights don't get skipped. Skipping sleep for several nights brings phantoms.
- **Spend the first 2–3 minutes** of each session finishing the last session's carry-over items. Spend the last 5 minutes putting things in chests, writing the **X Y Z of every new place** in [coordinates](../notes/coordinates.md), and noting what got done for the session log.

## Why the wheat is slow

The Session 2 wheat still wasn't ready after Session 3. That fits how crop growth works on this server (checked on the wiki 2026-10-10: [Wheat Seeds](https://minecraft.wiki/w/Wheat_Seeds), [Tutorial: Crop farming](https://minecraft.wiki/w/Tutorial:Crop_farming), [Tick](https://minecraft.wiki/w/Tick), [Simulation distance](https://minecraft.wiki/w/Simulation_distance), [Bed](https://minecraft.wiki/w/Bed)):

- **Crops only grow while their chunk is ticking.** On Bedrock that means the chunk is within the simulation distance of a player (on a server, `tick-distance`; the multiplayer default is 4 chunks, about 64 blocks) or inside a [ticking area](../plans/multiplayer-server.md#ticking-area-iron-farm-and-item-sorter). When nobody is online, or you're off in the caves more than a few chunks away, the wheat doesn't grow at all. With about an hour of play per session and much of it spent caving, the field has had very little growing time.
- **Light 9 or more at the crop.** On Bedrock wheat can be planted in any light but needs light 9 to grow. Daylight covers the day; at night an unlit field stops, so torches around and in it keep it growing.
- **Sleeping doesn't grow crops.** Skipping the night jumps the clock to morning, but crops don't get the skipped time.
- **How long it takes:** wheat has 8 stages, and each step averages about 5 minutes in ideal conditions (hydrated farmland, planted in rows, lit) up to about 35 minutes in poor ones. So a field needs somewhere between about half an hour and a few hours of time *with you nearby*.
- **What helps:** do base jobs near the farm, light it, keep every block within 4 of water, and use **bone meal** (from skeleton bones), which pushes a crop 2 to 5 stages at once.

## Carry-over rule

**Anything unfinished rolls into the next session, at the top of its list.** If a session's 60-minute block isn't done, skip its "if you have 90" block. If a whole session slips, every later session shifts by one. Don't cram, and don't skip safety items to catch up.

## At a glance

| Session | Goal | Phases | Map thread |
| --- | --- | --- | --- |
| [2](#session-2-light-food-and-the-first-farm) | Light, a food stack, the wheat farm, an animal pen, a second chest | Finishes 1; advances 2 and 3 | Plant sugar cane |
| [3](#session-3-iron-age) | Staircase mine for iron and coal; iron pick, shield, bucket | 2 | Look for redstone (compass) |
| [4](#session-4-plant-the-flag) | Mark the real site near spawn, move the bed, Stage 0 storage chests, compass | 3, starts 4 | Compass; first locator map of base and spawn (90 block) |
| [5](#session-5-diamonds-and-the-enchanting-path) | Branch mine for diamonds, redstone and lapis; obsidian; scout a village | 4, prep for 5 | Zoomed-out local-area map on the scouting trip (90 block) |
| [6](#session-6-the-nether-gateway) | Enchanting table, a boxed Nether portal, a short quartz run | 4 and 5 | Wall map in item frames (90 block) |

## New content woven in

Jeffrey's last game was around October 2024, so this plan includes a few things added since then. Each is marked **(new)** and is optional unless it's in a core step. The full catch-up is in [what's new](../notes/whats-new.md).

- S2: a **bundle**, and pale garden and night-mob warnings.
- S3: **copper** tools and armor as a stopgap.
- S5: night mobs on the scouting trip, and cartographer maps.
- S6: a **dried ghast** stretch for the [happy ghast](../plans/happy-ghast.md).

## Map thread: a local-area map

Jeffrey wants a map of the local area. The steps are spread across Sessions 2–6, mostly in the "if you have 90" blocks, because each step depends on materials from earlier sessions: **sugar cane → paper**, **iron + redstone → compass**, **cows → leather → item frames**.

| Step | Session | Needs |
| --- | --- | --- |
| Plant sugar cane by water | 2 (during the farm step) | A few stalks found nearby |
| Compass | 4 (core, last 5 minutes), or 5 | 4 iron + 1 redstone dust |
| Cartography table + first locator map of base and spawn (zoom level 0) | 4, if you have 90 | 3 paper (2 for the table + 1 for the map) + the compass |
| Zoomed-out local-area map, filled on the scouting trip (level 2 or 3) | 5, if you have 90 | 1 paper + a compass for a new locator map, plus 1 paper per zoom level |
| Wall map by the base door or storage entrance | 6, if you have 90 | 1 item frame (leather) per map, plus 1 paper per clone |

**Verified Bedrock facts** ([Map](https://minecraft.wiki/w/Map), [Cartography Table](https://minecraft.wiki/w/Cartography_Table), [Paper](https://minecraft.wiki/w/Paper), 2026-10-07)
- **Paper:** 3 sugar cane make 3 paper.
- **Empty map vs empty locator map:**
  - On Bedrock, 9 paper crafts an **empty map**, which draws terrain but shows no player marker.
  - 8 paper around a compass crafts an **empty locator map**, which shows player markers.
  - At a cartography table it's much cheaper: 1 paper makes an empty map, and 1 paper + a compass makes an empty locator map.
  - A plain map can get its marker later by combining it with a compass.
- **Cartography table:** 2 paper + 4 planks. It zooms maps out (1 paper per level, versus 8 paper on a crafting table or anvil), clones them (map + empty map), and locks them (map + glass pane). On Bedrock it also makes empty maps, adds the compass marker, and renames maps for free.
- **Zoom levels:**

| Level | Covers | 1 map pixel = |
| --- | --- | --- |
| 0 | 128×128 blocks | 1 block |
| 1 | 256×256 | 2×2 blocks |
| 2 | 512×512 | 4×4 |
| 3 | 1024×1024 | 8×8 |
| 4 | 2048×2048 | 16×16 |

- **Zooming wipes the drawing:** changing a map's zoom resets its contents, so it has to be explored again. Locked maps can't be zoomed.
- **How a map fills in:**
  - Use (activate) it once, then **hold it in either hand** while you move. It records terrain around you (up to 128 blocks away in the Overworld), and only the surface, even if you're underground.
  - Changes to the world only show up when you go back there holding the map.
  - **Clones stay in sync**, so one copy can sit in a frame while you fill another.
- **Fixed grid:**
  - A new map doesn't center on you. It shows the fixed grid square you were standing in when you first used it, and maps of the same size never partly overlap.
  - Zoomed maps stay on the same grid. To cover a new area, start a level 0 map **inside** that area.
- **Seamless wall map:** put maps of the **same zoom level** from neighboring grid squares in item frames side by side. Framed maps expand to fill the frame, so the squares line up into one picture.
- **Markers on Bedrock:**
  - Only **locator** maps show players. In multiplayer they show every player, colored by join order, with a skin face when they're 10–80 blocks away. When you're off the map, your marker sits on the edge and, since 26.50, still shows which way you're facing.
  - A framed locator map shows a **green marker** for the frame on its clones.
  - **Banner markers are Java-only:** using a map on a banner does nothing on Bedrock.
  - Maps don't mark lodestones, and an Overworld map doesn't mark world spawn. So exact spots go in [coordinates](../notes/coordinates.md) as X Y Z.
- **Nether:** maps made there only show a red-and-gray pattern, so the Nether hub gets logged in coordinates, not mapped. On Bedrock, though, an **Overworld locator map carried into the Nether** shows where you are relative to the Overworld map. That helps line up the two portals.

**Works with the coordinates log.** The map shows the area at a glance; the exact X Y Z of each place goes in [coordinates](../notes/coordinates.md). When a map shows something new (a village, a cave mouth), go there and write down its coordinates. At level 0, 1 pixel is 1 block, so distances can be counted.

---

## Session 2: Light, food, and the first farm

**Goal:** finish Phase 1 (a lit shelter and a full stack of food), and get the Phase 2 farm, pen and second chest started.
**Result (2026-10-07):** ✅ Phase 1 finished. ⏳ Farm and pen started; cows, second chest, door, fence and light still open ([session log](session-log.md)).
**Advances:** Phase 1 (finishes it), Phase 2, Phase 3 (a first look at the site).

**Bring / have ready**
- Logs (for charcoal, planks, sticks, fences, a door and a chest) and the furnace.
- Stone tools: you need a hoe for the farm (2 cobble + 2 sticks).
- A few spare wool, for a banner if you find the site.

**60-minute plan**
- [ ] ⏳ **0:00–0:10 Light.** *(Done: charcoal and a stack of torches. Not reported: torch placement, door.)* Smelt logs into charcoal (planks or logs as fuel). Craft torches (1 coal or charcoal + 1 stick = 4 torches). Light the bed area and wherever you shelter, and add a door. Most monsters only spawn at block light 0, so every torch counts.
- [x] ✅ **0:10–0:25 Food stack.** *(Full stack.)* Hunt nearby cows, pigs, sheep and chickens and cook the meat in the furnace. Aim for a full stack (64). Break tall grass as you go to collect wheat seeds.
- [ ] ⏳ **0:25–0:45 Wheat farm.** *(About 15 wheat planted beside water, not mature yet. Fence and light not reported. A couple of sugar cane found; planting unconfirmed.)* Till the Phase 2 plot next to water and plant the seeds. Water hydrates farmland up to 4 blocks away. Fence it so mobs don't trample it, and keep it lit: on Bedrock, wheat needs light 9 to grow ([Wheat Seeds](https://minecraft.wiki/w/Wheat_Seeds)). **Sugar cane:** if you pass any, grab a few stalks and plant them on dirt or sand right next to the water. It's slow to multiply, and it gates paper for both books and maps.
- [ ] ⏳ **0:45–0:55 Animal pen.** *(Pen built; no cows yet because there's no wheat to lead them.)* Fence a pen with a gate. Cows and sheep follow you while you hold **wheat**, and chickens follow **seeds**. If there's no wheat yet, fence the pen where cows already graze, or wait for the first harvest in Session 3. Two cows minimum.
- [ ] ⏳ **0:55–1:00 Second chest + log it.** *(Not reported. No new landmarks given.)* Craft a chest (8 planks) and split your things into tools, food and blocks. Write the bed, spawn and tree-farm landmarks in [coordinates](../notes/coordinates.md).

**If you have 90**
- [ ] ⏳ **Site walk near spawn (daylight only).** *(Not reported.)* Check the two Phase 3 items that aren't confirmed yet: **flat or gently sloped ground**, and a **village** (or a plains, meadow or river edge). If one spot has both, mark it with a banner (6 wool of one color + 1 stick) or a tall pillar.
- [ ] ⏳ **Look at the mountain.** *(Not done: no iron search yet.)* Iron also generates high up (it shows up from Y=80 to the top of the world, so mountains have plenty), and emerald ore appears in mountain and cherry grove biomes ([Ore](https://minecraft.wiki/w/Ore)). Note any exposed iron or coal for Session 3.
- [ ] ⏳ **Abandoned camp.** *(Not reported.)* If you spot one, raid it and leave (copper gear, buckets, compasses, sometimes iron). Log it.
- [ ] ⏳ **(new) Bundle:** *(Not reported.)* if the cows dropped leather and you have string, 1 string + 1 leather makes a bundle. It holds a stack's worth of mixed items in one slot, which helps for the Session 3 mine (torches, food, odd ores). Optional: leather is also needed for books and item frames.

**Done when**
- [ ] ⏳ The bed area and shelter are lit, with a door. *(Torches made; door not reported.)*
- [x] ✅ A full stack of food is in the chest or your inventory.
- [ ] ⏳ The wheat is planted, fenced and lit. *(Planted; fence and light not reported.)*
- [ ] ⏳ A pen with a gate exists, with at least 2 cows in it (or the pen is built and cows come once there's wheat). *(Pen built, empty; gate not reported.)*
- [ ] ⏳ Two chests. *(Not reported.)*

**Safety and night**
- Light first, then food. Don't walk far at dusk; sleep instead.
- **(new) Pale gardens:** foggy forests with gray-white trees, often on mountain slopes. At night they release **creakings**, which can't be hurt and move only when you look away. Break their **creaking heart** (the block in a pale oak trunk) to kill them, or just leave. Don't go in after dark.
- **(new) Zombie horsemen** (a zombie with a spear on a zombie horse) now spawn in plains and savannas at night. Spears reach 4.5 blocks.
- **(new) Animals near the ice look different** (cold cows, pigs and chickens; mostly black sheep). The biome picks the look.
- If you die, dropped items stay on the ground for about 5 minutes. Keep the bed (your spawn) close to where you work.

**Repo boxes this should tick (once reported)**
- [Phase 1](../plans/phase-1-first-night.md): *Light it*, the shelter item, and *Done when: I have a stack of food*. That finishes Phase 1.
- [Phase 2](../plans/phase-2-starter-outpost.md): *Two chests*, *A door*, *Torches every 7–8 blocks*, *Till…*, *Fence it*, *Plant wheat*, *Pen with two cows minimum*.
- [Tracker](tracker.md) first-session checklist: *Food farm planted*. Phase 1 row → ✅.
- [Resources and farms](../notes/resources-and-farms.md): starter crop farm and animal pen rows. [Coordinates](../notes/coordinates.md): first bed, world spawn, tree farm.
- [Phase 3](../plans/phase-3-pick-the-site.md) (90 block): *Flat or gently sloped ground* and/or *A village…*, if confirmed.

---

## Session 3: Iron age

**Goal:** mine down for iron and coal, and come back with an iron pick, a shield and a bucket.
**Result (reported 2026-10-10):** ✅ Caves instead of a staircase: a little iron, a bucket (filled), a shield, lots of coal and copper, full copper armor. ✅ Initial hut done with a smoker and two double chests. ⏳ Iron pick, iron sword and axe, cows, sugar cane, farm light and fence, and X Y Z still open ([session log](session-log.md)).
**Advances:** Phase 2 (mining and iron upgrades).

**Bring / have ready**
- 2–3 stone picks, a stone sword, a full stack of food, and 1–2 stacks of torches.
- Cobble for blocking lava and water, plus a crafting table and furnace (or come back up to smelt).
- **Target depth: Y=16.** Watch the Y in the coordinates box. That's where iron is most common below ground (it generates from Y=−24 to Y=56, peaking around Y=16) ([Iron Ore](https://minecraft.wiki/w/Iron_Ore)). Redstone starts at Y=15 and below ([Redstone Ore](https://minecraft.wiki/w/Redstone_Ore)). Stone turns into deepslate between Y=8 and Y=0 ([Deepslate](https://minecraft.wiki/w/Deepslate)), so if you see deepslate you've gone below the target.

**Carry-over from Session 2 (do these first)**
- [ ] ⏳ **Cows into the pen** once the wheat is ready: hold wheat and the cows follow you. At least 2. *(Wheat still not mature.)*
- [x] ✅ **Second chest** if there isn't one yet (8 planks). *(Two double chests in the hut.)*
- [ ] ⏳ **Check the wheat field is fenced and lit** (light 9 on Bedrock), and add a door to the house if it doesn't have one. *(Not reported. Hut done; door not mentioned.)*
- [ ] ⏳ **Sugar cane:** *(Not reported.)* plant the stalks on dirt or sand right next to the water if they aren't in yet, and spread new stalks along the bank.

**60-minute plan**
- [ ] ⏳ **0:00–0:05 Prep.** *(Not reported.)* Eat, top up torches (craft more from coal as you find it), and set out at the start of a day.
- [ ] ⏳ **0:05–0:35 Staircase down.** *(Went into the caves instead: some iron, a bunch of coal and copper. No staircase or depth reported.)* Dig a staircase (never straight down) to about **Y=16**, lighting as you go. Mine every coal and iron ore you see, and **(new)** copper ore too. The big caves at spawn are faster but more dangerous; stay in lit sections. Coal ore needs any pickaxe; iron needs stone or better.
- [ ] ⏳ **0:35–0:45 Smelt and craft, in this order:** *(Bucket filled with water and shield made; iron pick not reported.)*
  - Iron pick (3 iron).
  - Bucket (3 iron), then fill it with water.
  - Shield (1 iron + 6 planks).
- [ ] ⏳ **0:45–0:55 More iron.** *(Not reported: only a little iron found.)* Keep mining for an iron sword (2) and axe (3). That's 12 iron total with the items above.
- [ ] ⏳ **0:55–1:00 Back up and store.** *(Two double chests in the hut; no X Y Z reported.)* Put the iron and coal in the chests. Write the X Y Z of the mine entrance, and of any other new place (cave mouths, camps, a good ore spot), in [coordinates](../notes/coordinates.md).

**If you have 90**
- [ ] ⏳ **Iron armor** *(Not reported.)*, in priority order: chestplate (8), leggings (7), helmet (5), boots (4). The full set is 24 iron.
- [ ] ⏳ **Smoker** *(✅ in the hut; blast furnace not reported.)* (furnace + 4 logs) to halve cooking time. **Blast furnace** (furnace + 5 iron + 3 smooth stone) to halve ore smelting; smooth stone is stone smelted again.
- [x] ✅ **(new) Copper as a stopgap:** *(Full set of copper armor.)* smelt the copper ore. **Copper armor** (24 ingots, 10 armor points vs. iron's 15) can cover you while iron goes to the pick, bucket and shield. Copper tools mine like stone (no diamonds or redstone) but faster and longer. Skip it if iron armor is already happening.
- [ ] ⏳ **Bank toward a compass:** *(No redstone reported.)* 4 iron + 1 redstone dust. Redstone ore only appears at Y=15 and below, so pick some up if you see it around Y=16 and lower.

**Done when**
- [ ] ⏳ An iron pick, a shield and a water bucket. *(Shield and water bucket ✅; iron pick not reported.)*
- [ ] ⏳ An iron sword and axe, or 5+ spare iron toward them. *(Not reported.)*
- [ ] ⏳ A stack of coal or charcoal for torches and smelting. *("A bunch of coal"; amount not given.)*

**Safety and night**
- **Never dig straight down, and never mine the block you're standing on.** Lava pools get common deeper down.
- The water bucket puts out fire and stops falls: carry it once you have it. Use the shield against skeletons and creepers.
- **(new) Sulfur caves** (yellow sulfur and red cinnabar) spawn **cave spiders** naturally (on Bedrock since 26.30; the bug that blocked them, MCPE-238004, is fixed), and their bite poisons on Normal and Hard. The pools there give Nausea near the gas. Note it and go around ([Sulfur Caves](https://minecraft.wiki/w/Sulfur_Caves), [Cave Spider](https://minecraft.wiki/w/Cave_Spider)).
- **(new) Sulfur cubes** are the most common spawn there on Bedrock (spawn weight 150, vs. 20 for cave spiders) and spawn **at any light level**, so torches won't keep them away. They're passive, but killing a big one splits it into **2 small ones** that grow back in 20 minutes. They pick up blocks dropped on the ground, and one holding **TNT** can be lit and explodes, so don't drop blocks or TNT near them ([Sulfur Cube](https://minecraft.wiki/w/Sulfur_Cube)).
- Caves have the same monsters day or night. Light every junction, and keep torches on one wall (for example the right side going in) so the way out is obvious.
- Come back up and sleep at dusk if the bed is near; otherwise wall yourself in and keep mining.

**Repo boxes this should tick (once reported)**
- [Phase 2](../plans/phase-2-starter-outpost.md): *Mine a staircase down to around Y=16*, *Iron pick*, *Iron tools*. Also *Iron armor*, *Smoker* and *Blast furnace* if the 90 block happened.
- [Tracker](tracker.md) first-session checklist: *Iron tools*.
- [Resources and farms](../notes/resources-and-farms.md): a row in the Mining table for the staircase mine. Its entrance X Y Z goes in [coordinates](../notes/coordinates.md).
- If iron armor is done and the farm is self-refilling, Phase 2's *Done when* boxes can close.

---

## Session 4: Plant the flag

**Goal:** confirm and mark the real base site near spawn, give it a door, light and a chest, move the bed, and start Stage 0 storage with chests for the groups you already have items in.
**Advances:** Phase 3 (picks the site and finishes it), Phase 4 (storage wall, food wing), Phase 2 farm expansion.

**Bring / have ready**
- **About 30 logs** (120 planks), plus whatever the room itself is built from. Recipes checked on the wiki ([Chest](https://minecraft.wiki/w/Chest), [Sign](https://minecraft.wiki/w/Sign), [Wooden Door](https://minecraft.wiki/w/Wooden_Door), [Stick](https://minecraft.wiki/w/Stick), [Torch](https://minecraft.wiki/w/Torch), [Planks](https://minecraft.wiki/w/Planks)): 1 log = 4 planks, 2 planks = 4 sticks.

| What | Recipe | Planks |
| --- | --- | --- |
| 10 chests (about 9 groups + 1 input) | 8 planks each | 80 |
| 10 sign labels | 6 planks + 1 stick = 3 signs; 4 crafts make 12 | 24 |
| Door | 6 planks = 3 doors | 6 |
| Sticks: 4 for signs + 16 for a stack of torches | 2 planks = 4 sticks; 5 crafts | 10 |
| **Total** | | **120 planks = 30 logs** |

  - The room's walls and roof are extra and depend on Jeffrey's design. Cobble or other stone saves the wood.
  - **Why not all 17 chests today:** the full Stage 0 (16 group chests + 1 input, 18 signs) comes to about **48 logs** before the room, and labeling and sorting 17 chests doesn't fit in 20 minutes. The other 7 groups (redstone, transport, brewing, potions, Nether, End, shulker boxes) mostly have nothing in them yet, so their chests wait until you have something for them.
- **Labels:** item frames need leather (8 sticks + 1 leather each), so until the cows give leather, signs work as temporary labels.
- Wool for a banner, a door, torches, and the bed (you pick it up and carry it).
- Wheat, seeds, and any carrots or potatoes you've found.
- For the 90-minute map step: the compass (or redstone to craft it) and about 3 paper (harvest the Session 2 sugar cane).

**Carry-over from Session 3 (do these first)**
- [ ] **Cows into the pen** once the wheat is ready (hold wheat; at least 2). If it still isn't ready, see [why the wheat is slow](#why-the-wheat-is-slow): light the field and spend time near it.
- [ ] **Iron pickaxe** if it isn't made yet: needs 3 more iron (the bucket and shield used 4). Grab it on any cave trip; the Session 5 branch mine needs iron picks.
- [ ] **Sugar cane:** plant it on dirt or sand right next to water if it isn't in yet, and spread it. It gates paper for the map and books.
- [ ] **Log X Y Z** of the hut, the wheat farm, the pen and the cave entrance in [coordinates](../notes/coordinates.md).

**60-minute plan**
- [ ] **0:00–0:10 Pick and mark the site** near spawn, using the Phase 3 checklist (flat-ish ground, plus what's already confirmed: ocean, caves, cherry trees, a second biome). Banner or pillar it, and write its X Y Z in [coordinates](../notes/coordinates.md). Check the Phase 3 "avoid" list: not on a stronghold, not inside a mansion, not on the looted camp.
- [ ] **0:10–0:30 A first functional room:** enclosed, lit, with a door. This can be the start of the [thatch-roof starter cottage](../plans/building-goals.md#1-thatch-roof-starter-cottage) or anything Jeffrey designs. All it needs today is walls, a door and light.
- [ ] **0:30–0:35 Move the bed,** only after the door, light and a chest are in, as Phase 3 says. Sleep in it once to set spawn.
- [ ] **0:35–0:55 Stage 0 storage, first part:** a labeled chest for each [item group](../plans/storage-layout.md#2-item-grouping-for-the-chest-walls) you already have items in, plus an input chest or barrel by the door, then sort everything into them. That's probably about 9 groups: stone, wood, farming & food, ores & metals, copper, decorative (wool, flowers), mob drops, tools & armor, and misc. Each group chest becomes that group's manual home until its wing of the hall is built.
  - **The other 7 group chests** go in the first time you bring home something for that group (for example redstone in Session 5, Nether blocks in Session 6). Until then, odd items go in misc. That matches Stage 0's done-when: everything you own has a group chest.
- [ ] **0:55–1:00 Compass.** If you have redstone from Session 3, craft one (4 iron + 1 redstone). A plain compass points to world spawn, which is home now. Otherwise this moves to Session 5. Before logging off, write the X Y Z of the new base, the bed and anything else new in [coordinates](../notes/coordinates.md).

**If you have 90**
- [ ] **Farm expansion near the new site:** a second wheat area and carrots or potatoes (from villages, zombies or shipwreck chests). Plant **sugar cane** on dirt or sand next to water, for paper and books later.
- [ ] **Animals:** breed the cows with wheat for leather (books and item frames), and lure chickens with seeds.
- [ ] **Food wing basics** (Phase 4): a composter, and a smoker if Session 3 didn't make one.
- [ ] Bring the starter crops and animals over if the old spot is far, or keep both and log both.
- [ ] **First map: base and spawn.** Needs the compass plus about 3 paper (sugar cane from Session 2). Craft a **cartography table** (2 paper + 4 planks), then make an **empty locator map** in it from 1 paper + the compass. That's much cheaper than the 8 paper + compass crafting recipe. Use the map, then walk around the new base and spawn while holding it until the area fills in. Anything new it shows gets its X Y Z in [coordinates](../notes/coordinates.md). See the [map thread](#map-thread-a-local-area-map).

**Done when**
- [ ] The site is chosen, marked and logged.
- [ ] The new site has a door, light and a chest, and the bed has moved there.
- [ ] Every group you have items in has a labeled chest (about 9), plus an input chest, and everything is sorted.

**Safety and night**
- Light the ground around the new room before night; mobs spawn on unlit ground right next to it.
- Don't sleep in the new bed until the room is enclosed and lit.
- Keep the old bed area lit too, as a fallback.

**Repo boxes this should tick (once reported)**
- [Phase 3](../plans/phase-3-pick-the-site.md): the remaining site checklist items, *Mark the site…*, *Record the coordinates…*, *Give the new site a door / light / a chest*, *Move the bed*, and all three *Done when* boxes. Phase 3 row → ✅.
- [Phase 4](../plans/phase-4-the-base.md) §1 storage wall: *Double chests in a row* (or the group chests), *Label them*, *One input chest by the door*. §3 food wing: *Composter* (90 block).
- [Tracker](tracker.md) first-session checklist: *Site chosen* and *Storage started*. Tracker: move *Storage sorter Stage 0* from Planned milestones to Achieved once every group you own items in has a chest (the empty groups and the test hopper slice come later). Phase 4 row → 🟨.
- [Phase 2](../plans/phase-2-starter-outpost.md): *Add carrots or potatoes*, *Add sheep*, *Add chickens* (90 block).
- [Coordinates](../notes/coordinates.md): *Real base*.
- [Phase 4](../plans/phase-4-the-base.md) §2 workshop: *Cartography table*; §7 local-area map: *First locator map of the base and spawn* (90 block).

---

## Session 5: Diamonds and the enchanting path

**Goal:** branch mine at diamond depth for diamonds, redstone and lapis, cast and mine obsidian, and (with 90) scout a village.
**Advances:** Phase 4 (mine entrance, enchanting prep), prep for Phase 5 (trading).
**Minimum haul: 5 diamonds and 4 obsidian.** That's 3 diamonds for the diamond pickaxe (3 diamonds + 2 sticks), which you need to mine obsidian at all, plus 2 diamonds and 4 obsidian for the enchanting table (1 book + 2 diamonds + 4 obsidian) ([Diamond Pickaxe](https://minecraft.wiki/w/Diamond_Pickaxe), [Obsidian](https://minecraft.wiki/w/Obsidian), [Enchanting Table](https://minecraft.wiki/w/Enchanting_Table)). Three diamonds gets the pick but not the table, so it's not a finished session.

**Bring / have ready**
- **Two iron picks** (Phase 4 says branch mine once you have iron picks to spare), a water bucket, a shield, iron armor, a stack of food, 2+ stacks of torches, cobble and a crafting table.
- **Target depth: Y=−59.** Watch the Y in the coordinates box. Deepslate diamond ore is most common at **Y=−58 and Y=−59** ([Diamond Ore](https://minecraft.wiki/w/Diamond_Ore)), and redstone gets more common the lower you go ([Redstone Ore](https://minecraft.wiki/w/Redstone_Ore)). Lapis peaks higher, around Y=0, so grab it on the way down ([Lapis Lazuli Ore](https://minecraft.wiki/w/Lapis_Lazuli_Ore)). Gold has an extra batch spread evenly from Y=−64 to Y=−48 ([Gold Ore](https://minecraft.wiki/w/Gold_Ore)), so pick up every bit for Session 6.
- **Don't use bedrock as a depth marker.** It fills Y=−64 to Y=−60 in a rough, random pattern ([Bedrock](https://minecraft.wiki/w/Bedrock)), so the first bedrock you see could be anywhere in that band. Go by the Y readout instead.

**60-minute plan**
- [ ] **0:00–0:10 Head down** from the new base's mine entrance; Phase 3 says mine from the real site, not the starter shack. Extend the Session 3 staircase or start a new lit one.
- [ ] **0:10–0:45 Branch mine** at **Y=−59** (by the coordinates box). Mine every diamond (iron pick or better), redstone, lapis and gold you see. Wall off lava with cobble.
- [ ] **0:45–0:55 Obsidian.** Pour water over a **lava source** to make obsidian ([Obsidian](https://minecraft.wiki/w/Obsidian)). It can only be mined with a **diamond pickaxe**, so craft one first (3 diamonds + 2 sticks). The enchanting table needs **4 obsidian**, and a Nether portal needs **10** (Session 6).
- [ ] **0:55–1:00 Back up and store.** Diamonds and valuables go in the group chests. Craft the compass now if Session 4 didn't. Write the X Y Z of the branch mine, the obsidian spot, and any village or other new place in [coordinates](../notes/coordinates.md).

**If you have 90**
- [ ] **Village scouting (daylight).** Follow the coast or a river from spawn. Log any village, and note librarians, fletchers and toolsmiths in [resources and farms](../notes/resources-and-farms.md) (Phase 5 trading hall). The village decides the remaining Phase 3 site item. **(new)** Village chests can hold bundles. A cartographer (once in the trading hall) sells maps to other villages.
- [ ] **Wider local-area map while scouting.** Start a fresh locator map at the base, then zoom it out at the cartography table (1 paper per level; zooming wipes what's drawn, so do it **before** filling). Level 2 covers 512×512 blocks and level 3 covers 1024×1024. Carry it on the village trip and swing past the mountain, the cherry grove, the cave entrance, the ocean and the ice so they all get drawn.
- [ ] **Enchanting materials:** an **enchanting table** is 1 book + 2 diamonds + 4 obsidian ([Enchanting Table](https://minecraft.wiki/w/Enchanting_Table)). A book is 3 paper + 1 leather, and paper is 3 sugar cane. Start a stockpile; bookshelves come later.

**Done when**
- [ ] At least 5 diamonds: 3 for a pick and 2 for the enchanting table. A diamond pick is crafted.
- [ ] At least 4 obsidian mined (14 if Session 6 will build a portal from mined blocks).
- [ ] Redstone and lapis in the chests. A compass is crafted.
- [ ] Gold for Session 6: at least 4 ingots for golden boots (or 5 for a helmet), plus any spares for piglin bartering. Spares are for luck only: fire resistance comes from brewing after the fortress run, not from barters.

**Safety and night**
- **Lava is the main danger this deep.** Never dig down or toward the unknown with an empty hand; keep the water bucket on your hotbar.
- Don't mine the block above lava or the block under your feet.
- **(new) Scouting at dusk:** be back before night. Zombie horsemen spawn in plains and savannas at night, and pale gardens release creakings.
- The deep dark (sculk, shriekers) is around this depth. If you hear or see sculk, leave quietly; don't explore it.
- Deepslate mines slower than stone, so pace yourself and keep track of time.

**Repo boxes this should tick (once reported)**
- [Phase 4](../plans/phase-4-the-base.md) §4 mine entrance: *A lit staircase…*, *Branch around Y=−59 (diamond level)…*, *Keep a safe path back up*.
- [Phase 3](../plans/phase-3-pick-the-site.md): *A village…*, if one turned up near the site.
- [Resources and farms](../notes/resources-and-farms.md): a branch mine row, and the village or villager rows. [Coordinates](../notes/coordinates.md): *Branch mine*, *Village*.
- [Phase 4](../plans/phase-4-the-base.md) §7 local-area map: *Zoomed-out local-area map* (90 block). New places it shows get their X Y Z in [coordinates](../notes/coordinates.md).

---

## Session 6: The Nether gateway

**Goal:** place the enchanting table, build a boxed Nether portal, and make one short **quartz grab next to the portal**. Quartz is needed for comparators (Stage 1 of the [item sorter](../plans/storage-layout.md#4-growth-stages)).
**Advances:** Phase 4 (enchanting), Phase 5 (Nether).
**Not this session:** exploring the Nether, or a fortress run for blaze rods. The repo's rule is no Nether exploring in iron armor without fire resistance, and there won't be any fire resistance yet, so this trip stays inside the limited-scope rule under Safety. The fortress comes later as one prepped run, and its blaze rods are how fire resistance gets brewed ([future session: blaze rods and brewing](#future-session-blaze-rods-and-brewing-fire-resistance)).

**Bring / have ready**
- **10 obsidian.** A portal frame is at least 4×5, and the four corners are optional ([Nether Portal](https://minecraft.wiki/w/Nether_Portal)). You can also cast obsidian in place with a water bucket and lava, or complete a ruined portal.
- **Flint and steel:** 1 iron + 1 flint (flint comes from gravel).
- **At least one piece of golden armor, worn the whole trip.** Piglins attack players who aren't wearing any gold armor ([Piglin](https://minecraft.wiki/w/Piglin)). Golden boots (4 gold ingots) are the cheapest piece; a helmet is 5 ([Golden Boots](https://minecraft.wiki/w/Golden_Boots), [Golden Helmet](https://minecraft.wiki/w/Golden_Helmet)).
- **Spare gold ingots for bartering** (optional, from the Session 5 gold). Piglins trade **1 gold ingot per barter**: drop one near a piglin or use it on one, and after it looks at it (about 8 seconds on Bedrock) it throws back a random item ([Bartering](https://minecraft.wiki/w/Bartering)). Per ingot, the chances include about **2.1%** (10 in 469) for a dried ghast, about **1.7%** (8 in 469) for a potion of Fire Resistance and another 1.7% for a splash one, plus common junk like gravel, blackstone and nether bricks. On average that's about 59 ingots for one specific fire resistance potion, or 29 for either kind, so a potion is a lucky bonus, not something to count on.
- **A fire resistance potion,** if you have one (from a barter, say), to drink if you catch fire. You almost certainly won't yet. Either way, this trip stays next to the portal.
- Full iron gear, a shield, food, a stack of cobble, a pick for quartz, and a few torches.
- **The water bucket stays home.** Water vanishes the instant it's poured in the Nether ([Water](https://minecraft.wiki/w/Water)), so it can't put out fire or stop a fall there.
- **No bed:** beds explode in the Nether. (A straw bed won't explode there; it just breaks and drops nothing.)
- **(new, stretch)** Room in your inventory for a **dried ghast**, which breaks instantly by hand. For later: **10 snowballs** from the snow by spawn (a shovel on snow) and the **water bucket**, to start a [happy ghast](../plans/happy-ghast.md).

**60-minute plan**
- [ ] **0:00–0:10 Enchanting table.** Place it in the base (1 book + 2 diamonds + 4 obsidian) and do a first low-level enchant with lapis. Bookshelves come later; a level-30 table needs 15.
- [ ] **0:10–0:25 Portal room.** The portal goes **in a room with a door, not in the open** (Phase 5), so nothing wanders through near the base. The room itself is Jeffrey's design, or the start of the [Nether portal shrine](../plans/building-goals.md#7-nether-portal-shrine). Build the frame and light it.
- [ ] **0:25–0:50 Quartz grab next to the portal.** Step through. If the arrival spot is exposed, box it in with cobble. Mine only the **nether quartz ore** you can reach while keeping the portal in sight. It generates from Y=10 to Y=117 in every Nether biome ([Nether Quartz Ore](https://minecraft.wiki/w/Nether_Quartz_Ore)), so there's usually some near the portal. Head back by 0:50. Bring back 20+ quartz if it's there; if not, come home with less.
  - **Barter if a piglin comes to you** (optional): while wearing gold, give it 1 ingot at a time. Don't go after piglins, and don't open chests or break gold ore, nether gold ore or gilded blackstone near them, because that angers them even when you're wearing gold.
  - **(new, stretch) Dried ghast:** only if you've landed in or next to a **soul sand valley** and a **Nether fossil** (big bone-block skeleton) is within sight of the portal. About 1 fossil in 3 has a dried ghast next to it. Grab it and go back. Don't go looking for one on this trip.
- [ ] **0:50–1:00 Log both sides.** Write the X Y Z of both portals in [coordinates](../notes/coordinates.md). Nether X and Z are the Overworld's divided by 8, and Y doesn't scale ([Nether Portal](https://minecraft.wiki/w/Nether_Portal)), so the numbers should roughly match that. If they don't, it's the linking trap below. Store the quartz.
  - **Portal linking trap** (checked on the wiki 2026-10-10, [Nether Portal: portal search](https://minecraft.wiki/w/Nether_Portal#Portal_search)):
    - **How linking works:** when you go through, the game converts your position (X and Z ÷ 8 going into the Nether, × 8 coming back; Y stays the same) and looks for an existing **lit** portal near that spot. On Bedrock the search reaches **128 blocks in both the Overworld and the Nether** (Java only searches 16 in the Nether). The closest one wins, measured in a straight line that includes Y. Only if there's none does the game build a new portal, within 16 blocks of the target.
    - **Symptom:** you come out somewhere unexpected: in an old portal, another player's portal, or a Nether portal nowhere near your X ÷ 8, Z ÷ 8.
    - **Why it bites on Bedrock:** 128 Nether blocks cover about 1,024 Overworld blocks, so a second Overworld portal within roughly 1,000 blocks of the first usually leads into the first one's Nether side. A ruined portal that someone completed and lit counts as a portal too (an unlit, broken one doesn't).
    - **Fix:** build the Nether-side portal by hand at the Overworld portal's **X ÷ 8, Z ÷ 8**, at a similar Y, and light it. After the first trip, compare the two portals' numbers; if the Nether side is far off, build a new one by hand at the right spot and break the wrong one.

**If you have 90**
- [ ] **Leather and books:** breed the cows and harvest the sugar cane toward books (enchanting) and item frames (proper Stage 0 labels).
- [ ] **Iron stockpile:** more mining or caving for iron. Storage Stage 1 needs a lot of hoppers at 5 iron each ([Stage 1 needs](../plans/storage-layout.md#stage-1-front-left-wing-machinery-core-and-the-whole-trunk)).
- [ ] **Wall map by the base door or storage entrance.** Each map needs an **item frame** (8 sticks + 1 leather), so this follows the leather above. Clone the filled maps at the cartography table (map + 1 empty map = 2 copies) so you keep one to carry. Frame the base map and the local-area map. Framed locator maps show a green marker for the frame on every clone. Where and how the wall looks is Jeffrey's call.
- [ ] **(new) If you brought back a dried ghast:** waterlog it at the base (place it in water or pour water on it). It turns into a ghastling in about **20 minutes**, which runs while you do the rest of this block. On Bedrock, **10 snowballs** grow the ghastling to an adult at once. Leave room for a 4×4×4 adult; where it lives is Jeffrey's call. The harness (3 leather + 2 glass + 1 wool) comes after Session 6.
- [ ] **Not yet: an iron farm.** On Bedrock, iron golems spawn only in villages with **at least 20 beds and 10 villagers** ([Iron Golem](https://minecraft.wiki/w/Iron_Golem)). Those have to be real beds: straw beds don't count for villagers ([Straw Bed](https://minecraft.wiki/w/Straw_Bed)). That makes it a Phase 5 project for after the trading hall work. For now, just log a village that could host it.

**Done when**
- [ ] The enchanting table is placed and has been used once.
- [ ] The portal is lit, inside a room with a door, and both portal locations are logged.
- [ ] Some nether quartz is in the chests.

**Safety and night**
- **Follow the repo's rule: don't explore the Nether in iron armor without fire resistance potions.** Without fire resistance, the trip follows this **limited-scope rule** (the one planned exception is the later [prepped fortress run](#future-session-blaze-rods-and-brewing-fire-resistance)):
  - Always keep the portal in sight. If you can't see it, you've gone too far.
  - Go straight back through the portal at the **first ghast**, the **first time you catch fire**, or if lava is between you and the portal.
  - No digging down, no crossing lava, no bridging out, and no following anything away from the portal.
  - Done by 0:50 whatever you have.
- Ghast fireballs can be blocked with cobble. Don't dig down; lava seas sit low in the Nether. Don't hit piglins or zombified piglins (whole groups retaliate).
- **(new)** Soul sand valleys have lots of skeletons and ghasts, and soul sand slows you down. That's why the dried ghast stays within sight of the portal.
- If something goes wrong, go straight back through the portal. Before leaving, make sure the portal room's door is closed.

**Repo boxes this should tick (once reported)**
- [Phase 4](../plans/phase-4-the-base.md) enchanting: progress toward *Level-30 enchanting table* (a first table, not level 30 yet; leave it unchecked until there are 15 shelves).
- [Phase 5](../plans/phase-5-infrastructure.md) §3 Nether: *Nether portal in a boxed room with a door*, *Mark portal and hub coordinates*. Phase 5 row → 🟨.
- [Coordinates](../notes/coordinates.md): both *Nether portal* rows.
- [Building goals](../plans/building-goals.md) #7, Nether portal shrine: only if the portal room is built as the shrine.
- [Phase 5](../plans/phase-5-infrastructure.md) §3: *Bring back a dried ghast* (stretch). §6 / [happy ghast](../plans/happy-ghast.md): *Find a dried ghast*, *Rehydrate it* (90 block).
- [Phase 4](../plans/phase-4-the-base.md) §7 local-area map: *Wall map near the base door*. [Phase 5](../plans/phase-5-infrastructure.md) §4: *A map on an item frame at the door* (90 block).

---

## After Session 6

Phase 4 keeps going: the workshop, perimeter and spawn control, the sugar cane farm, and 15 bookshelves. Phase 5's trading hall follows, along with stockpiling iron and quartz for [storage Stage 1](../plans/storage-layout.md#4-growth-stages). **(new) Happy ghast:** if Session 6 found a dried ghast, finish it next: snowballs, a harness (3 leather + 2 glass + 1 wool), first flight. If not, look again on the next Nether trip; piglin barters can also give one. See [happy-ghast.md](../plans/happy-ghast.md). The next plan should be drawn up from whatever actually got done, using the carry-over rule above.

### Future session: blaze rods and brewing (fire resistance)

This is the step that lets the Nether rule relax. It's its own session (or two), not part of Session 6.

**Why not barter for fire resistance first:** each gold ingot has an **8 in 469 (about 1.7%)** chance of a potion of Fire Resistance and the same chance of a splash one ([Bartering](https://minecraft.wiki/w/Bartering)). That's about **59 ingots on average for one specific potion**, or about **29 for either kind**. The gold budget before this point is 4 ingots for golden boots plus spares, so waiting on barters would stall the plan for a long time. Instead, the first fortress trip goes without fire resistance, and fire resistance gets brewed from what it brings back. A bartered potion is a bonus, not a gate.

1. **First fortress run: a prepped trip, no fire resistance needed.** It's the one planned exception to the Session 6 limited-scope rule, with its own limits. Nether fortresses are the only place blazes spawn ([Nether Fortress](https://minecraft.wiki/w/Nether_Fortress), [Blaze](https://minecraft.wiki/w/Blaze)).
   - **Bring:** the best armor you have (full iron by then), **golden boots** (or another gold piece, so piglins leave you alone), a **shield**, a full stack of food, **2+ stacks of cobble** for bridging with walls and for walling off lava and blazes, a spare pick, torches, and any bartered fire resistance potion. No water bucket and no bed (see Session 6).
   - **Blazes:** each volley is 3 small fireballs. A **shield blocks both the damage and the burning**, and breaking line of sight (a cobble wall) stops their attack ([Blaze](https://minecraft.wiki/w/Blaze)). Fight from behind cover.
   - **Potion:** if a barter gave you one, drink it before taking on the blazes or the moment you catch fire.
   - **Route:** write the X Y Z of the portal and every turn on the way, and bridge with walls rather than walking open lava edges.
   - **Return trigger:** go back the way you came once you have the blaze rods (a few is enough: 1 for the stand, the rest become powder) and some nether wart, or as soon as you're down to half your food or half your cobble, your armor is badly worn, or you catch fire with no potion left. Set a time limit too (for example 45 minutes).
   - **Bring back:** **blaze rods**, and **nether wart** (about 20 plants grow in soul sand gardens by fortress stairwells). Take some soul sand too if there's no other source nearby ([Nether Wart](https://minecraft.wiki/w/Nether_Wart)).
2. **Plant the wart** on soul sand at the base so you never need to go back for it.
3. **Brewing stand:** 1 blaze rod + 3 cobblestone (any stone-tier block). It runs on **blaze powder** (1 rod crafts 2 powder), and 1 powder fuels 20 brews ([Brewing Stand](https://minecraft.wiki/w/Brewing_Stand), [Blaze Powder](https://minecraft.wiki/w/Blaze_Powder)).
4. **Brew fire resistance:** a water bottle + nether wart makes an awkward potion. Add **magma cream** (blaze powder + slimeball, or dropped by magma cubes) to get Fire Resistance (3:00), and add redstone dust to extend it to 8:00 ([Magma Cream](https://minecraft.wiki/w/Magma_Cream), [Potion of Fire Resistance](https://minecraft.wiki/w/Potion_of_Fire_Resistance)).

**Gold is an ongoing side task**, not a gate. Pick up every gold ore while branch mining (gold has an extra band from Y=−64 to Y=−48), keep golden boots on hand for every Nether trip, and barter spare ingots near the portal for the odd bonus (fire resistance, a dried ghast). Don't break nether gold ore or any gold block near piglins: that angers them even when you're wearing gold ([Nether Gold Ore](https://minecraft.wiki/w/Nether_Gold_Ore)). The long-term answer is a **zombified piglin gold farm** in Phase 5 (see [resources and farms](../notes/resources-and-farms.md)).

**Not a fire resistance source: bastion remnants.** None of the four bastion chest loot tables (bridge, generic, hoglin stable, treasure) has any potion on Bedrock or Java ([Bastion Remnant: loot](https://minecraft.wiki/w/Bastion_Remnant#Loot), checked 2026-10-10). Bastions are also dangerous: **piglin brutes** live there, hit hard with golden axes, and attack you even when you wear gold, since they don't barter or get distracted by gold ([Piglin Brute](https://minecraft.wiki/w/Piglin_Brute)). Leave bastions until there's fire resistance and better gear.

Once fire resistance is on tap, real Nether exploring (the hub, more fortresses, bastions) can go in the plan.
