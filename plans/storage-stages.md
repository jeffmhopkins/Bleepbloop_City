# Storage growth stages: one table per stage

**Part of:** [Storage and sorting](storage-and-sorting.md) · **Source of truth:** [storage-layout.md §3 (per-item allocation)](storage-layout.md#3-item-by-item-chest-allocation) and [§4 (growth stages)](storage-layout.md#4-growth-stages)
**Server:** Bedrock 26.50

Each stage below lists **only what that stage adds**. Every count comes straight from the §3 tables (generated from them, not retyped). If §3 or §4 changes, this file has to be regenerated.

**Units:** DC = double chest (54 slots), SC = single chest (27 slots), DC-eq = DC + SC ÷ 2. **★** = leave room to grow. Shapes and sizes are Jeffrey's design; this is counts and order only.

**How sorted:**
- **Hopper slice:** its own filter.
- **Mixed chest (manual, from overflow):** no filter; you move these from the overflow on the weekly review.
- **Smelter first:** filtered to the smelter; only the output gets a chest.
- **Manual:** unstackables or put away by hand.
- **Golem:** the gallery.

## Summary

| Stage | Phase | Adds DC-eq | Adds slices | Cumulative DC-eq / slices |
| --- | --- | --- | --- | --- |
| [Stage 0](#stage-0-manual-chests-by-group-plus-a-test-slice) | [Phase 4](phase-4-the-base.md#1-storage-wall) | 8.5 + test rig (temporary, not counted) | 1 test slice (not counted) | 0 / 0 |
| [Stage 1](#stage-1-input-router-overflow-and-bulk-slices) | Phase 4 → 5 | 29 | 15 | 29 / 15 |
| [Stage 2](#stage-2-rest-of-groups-15-plus-the-smelter-loop) | [Phase 5](phase-5-infrastructure.md) | 31.5 | 39 | 60.5 / 54 |
| [Stage 3](#stage-3-groups-610-12-14-plus-the-lava-disposal) | Phase 5 | 42.5 | 30 | 103 / 84 |
| [Stage 4](#stage-4-golem-gallery-showpiece) | Phase 5 | 6 | 0 | 109 / 84 |
| [Stage 5](#stage-5-end-group-shulker-boxes-and-the-unloader) | After the End | 4 | 3 | 113 / 87 |
| [Stage 6](#stage-6-expansion-ongoing) | Ongoing | +5.5 for golem module 2, then as needed | As needed | 118.5+ / 87+ |
| **Total through Stage 5** | | **113** | **87** | matches the §3 grand total |

**Why Stage 0 isn't counted:** its 17 chests (and the test rig) are the temporary Phase 4 storage wall. Once a group's items get hall chests (Stages 1–5), the old group chest is free to reuse as one of that group's mixed or manual chests, so counting it would double-count. The test slice is a prototype in a test area. Golem module 2 (Stage 6) is expansion on top of the 113.

## Stage 0: manual chests by group, plus a test slice

| Group | Item | Chests | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 1. Stone family | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 2. Wood family | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 3. Farming & food | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 4. Ores & metals | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 5. Copper | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 6. Decorative | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 7. Redstone | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 8. Transport | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 9. Mob drops | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 10. Brewing ingredients | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 11. Potions & tipped arrows (golem gallery, module 1) | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 12. Nether | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 13. End | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 14. Tools, armor & enchanting (manual) | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 15. Shulker boxes (manual) | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| 16. Misc / overflow | Everything in the group | 1 SC | Manual | Labeled with an item frame; temporary |
| — | Input chest by the door | 1 SC | Manual | Becomes input barrels in Stage 1 |
| — | Test hopper slice + its overflow chest (test area) | 1 slice + 1 SC | Hopper slice | Prototype from [Stackable Sorting](https://bedrockwiki.com/books/storage-tech/page/stackable-sorting); test with a junk item |

- **Stage adds:** 17 SC = 8.5 DC-eq, plus the test slice and its overflow chest. All temporary, not counted in the totals
- **Cumulative (counted):** 0 DC-eq / 0 slices
- **Phase:** [Phase 4](phase-4-the-base.md#1-storage-wall)
- **Needs:** wood for chests, item frames for labels, 1 slice's worth of hoppers and redstone parts.
- **Done when:** everything you own has a group chest, and the test slice sorts its item with nothing leaking past the overflow.

## Stage 1: input, router, overflow, and bulk slices

| Group | Item | Chests | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 1. Stone family | Cobblestone | 4 DC | Hopper slice | ★ room to grow. Bulk. Junk-to-lava candidate once full (your call) |
| 1. Stone family | Cobbled deepslate | 3 DC | Hopper slice | ★ room to grow. Bulk from deep mining |
| 1. Stone family | Dirt | 2 DC | Hopper slice | ★ room to grow. Bulk for terraforming |
| 1. Stone family | Stone | 1 DC | Hopper slice | Smelted cobble; makes smooth stone (blast furnaces) and stone bricks |
| 1. Stone family | Gravel | 1 DC | Hopper slice |  |
| 1. Stone family | Sand | 1 DC | Hopper slice | Feeds the smelter for glass |
| 2. Wood family | Main wood logs (your tree-farm species) | 3 DC | Hopper slice | ★ room to grow. Bulk from the tree farm |
| 2. Wood family | Main wood planks | 1 DC | Hopper slice |  |
| 3. Farming & food | Wheat | 2 DC | Hopper slice | ★ room to grow. Wheat-farm output |
| 3. Farming & food | Wheat seeds | 1 DC | Hopper slice | Farm surplus; compost extras |
| 3. Farming & food | Carrots | 1 DC | Hopper slice |  |
| 3. Farming & food | Potatoes | 1 DC | Hopper slice | Poisonous potatoes go to overflow (junk candidate) |
| 3. Farming & food | Sugar cane | 1 DC | Hopper slice | ★ room to grow. Paper (books, maps) and sugar |
| 4. Ores & metals | Coal | 2 DC | Hopper slice | ★ room to grow. Smelter fuel and torches |
| 4. Ores & metals | Iron ingots | 2 DC | Hopper slice | ★ room to grow. 5 per hopper; more once an iron farm runs |
| 16. Misc / overflow | Main overflow (end of the stream, in front of the lava) | 2 DC | Overflow | Weekly review; also where mixed-chest items wait. Promote anything that keeps showing up |
| 16. Misc / overflow | Non-stackable intake (from the split) | 1 DC | Manual | Sort by hand into groups 8, 14, 15 |

- **Stage adds:** 29 DC + 0 SC = **29 DC-eq**, **15 hopper slices**
- **Cumulative:** 29 DC-eq / 15 slices
- **Phase:** Phase 4 → 5
- **Also built:** input barrels and the router, the non-stackable split into a 1 DC intake, and the 2 DC main overflow at the end of the stream (no lava yet).
- **Needs:**
  - Iron for hoppers (5 iron ingots + 1 chest each). Count the chosen slice design's hoppers × 15, plus the input line.
  - Nether quartz for comparators (one Nether trip), and redstone.
  - Water for the item stream, and barrels.
  - A site near the home base, logged in [coordinates](../notes/coordinates.md).
  - Hopper locking when idle, for lag.
- **Done when:** dumping inventory into the input barrels sends bulk items to their chests, unstackables to the intake, and everything else to the overflow, with nothing lost.

## Stage 2: rest of groups 1–5, plus the smelter loop

| Group | Item | Chests | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 1. Stone family | Deepslate | 1 SC | Hopper slice | Silk Touch only |
| 1. Stone family | Granite | 1 SC | Hopper slice |  |
| 1. Stone family | Diorite | 1 SC | Hopper slice |  |
| 1. Stone family | Andesite | 1 SC | Hopper slice |  |
| 1. Stone family | Tuff | 1 SC | Hopper slice |  |
| 1. Stone family | Flint | 1 SC | Hopper slice | From gravel |
| 1. Stone family | Obsidian | 1 SC | Hopper slice |  |
| 1. Stone family | Red sand, coarse dirt, rooted dirt, mud, clay balls, moss blocks, podzol, mycelium, calcite, smooth basalt, dripstone blocks, pointed dripstone | 1 DC | Mixed chest (manual, from overflow) | Low volume; one chest for all of them |
| 1. Stone family | Sulfur, cinnabar, sulfur spikes (sulfur caves, added in 26.30) | 1 SC | Mixed chest (manual, from overflow) | Only once you find a sulfur cave |
| 2. Wood family | Main wood stripped logs | 1 SC | Hopper slice |  |
| 2. Wood family | Main wood saplings | 1 SC | Hopper slice | Tree-farm surplus; compost extras |
| 2. Wood family | Sticks | 1 SC | Hopper slice |  |
| 2. Wood family | Accent log #1, #2, #3 (the species you build with most after the main one) | 3 SC | Hopper slice | ★ room to grow. 1 chest each, 3 slices |
| 2. Wood family | All other logs (oak, spruce, birch, jungle, acacia, dark oak, mangrove, cherry, pale oak, poplar, minus the ones above) | 1 DC | Mixed chest (manual, from overflow) | Poplar was added in 26.50 |
| 2. Wood family | Other planks and stripped logs | 1 DC | Mixed chest (manual, from overflow) |  |
| 2. Wood family | Other saplings (incl. poplar saplings, mangrove propagules) | 1 SC | Mixed chest (manual, from overflow) |  |
| 2. Wood family | Sheared leaves | 1 SC | Mixed chest (manual, from overflow) |  |
| 2. Wood family | Bamboo | 1 SC | Hopper slice | Scaffolding |
| 2. Wood family | Signs and hanging signs (all woods) | 1 SC | Mixed chest (manual, from overflow) | Stack to 16 |
| 3. Farming & food | Hay bales | 1 DC | Hopper slice | Compressed wheat; also crafts straw beds (26.50) |
| 3. Farming & food | Bread | 1 SC | Hopper slice |  |
| 3. Farming & food | Baked potatoes | 1 SC | Hopper slice | Smoker output |
| 3. Farming & food | Cooked meat #1 and #2 (the two animals you farm, e.g. steak, cooked porkchop) | 2 SC | Hopper slice | 1 chest each; smoker output |
| 3. Farming & food | Raw meat and raw fish | — | Smelter first | Smoker first; the cooked result comes back to the router |
| 3. Farming & food | Other cooked food (cooked mutton, chicken, rabbit, cod, salmon) | 1 SC | Mixed chest (manual, from overflow) |  |
| 3. Farming & food | Pumpkins | 1 SC | Hopper slice | Carved pumpkins for golems |
| 3. Farming & food | Melon slices | 1 SC | Hopper slice | Glistering melon for brewing |
| 3. Farming & food | Apples | 1 SC | Hopper slice | Tree-farm drop |
| 3. Farming & food | Golden carrots | 1 SC | Hopper slice |  |
| 3. Farming & food | Eggs | 1 SC | Hopper slice (stack-16 filter) | Stack to 16. Brown and blue eggs are separate items: filter your chickens' color, add the others by hand |
| 3. Farming & food | Bone meal | 1 SC | Hopper slice |  |
| 3. Farming & food | Beetroot, beetroot seeds | 1 SC | Mixed chest (manual, from overflow) |  |
| 3. Farming & food | Sweet berries, glow berries, cocoa beans, kelp, dried kelp, dried kelp blocks, torchflower seeds, pitcher pods | 1 SC | Mixed chest (manual, from overflow) |  |
| 3. Farming & food | Brown mushrooms, red mushrooms, shelf mushrooms (26.50) | 1 SC | Mixed chest (manual, from overflow) | Stew ingredients |
| 3. Farming & food | Pumpkin pie, cookies, honey bottles | 1 SC | Mixed chest (manual, from overflow) | Honey bottles stack to 16 |
| 3. Farming & food | Stews and soups | — | Manual | Unstackable: they come out at the non-stackable split |
| 4. Ores & metals | Charcoal | 1 DC | Hopper slice | Tree-farm logs through the smelter |
| 4. Ores & metals | Raw iron, raw gold, raw copper | — | Smelter first | Blast furnace first; ingots come back to the router |
| 4. Ores & metals | Iron nuggets | 1 SC | Hopper slice |  |
| 4. Ores & metals | Gold ingots | 1 SC | Hopper slice |  |
| 4. Ores & metals | Gold nuggets | 1 SC | Hopper slice |  |
| 4. Ores & metals | Diamonds | 1 SC | Hopper slice | Never lava |
| 4. Ores & metals | Emeralds | 1 SC | Hopper slice | ★ room to grow. Grow it if you build a trading hall |
| 4. Ores & metals | Lapis lazuli | 1 SC | Hopper slice | Enchanting |
| 4. Ores & metals | Nether quartz | 1 SC | Hopper slice | 1 per comparator, and most filter slices use one |
| 4. Ores & metals | Storage blocks (iron, gold, diamond, emerald, lapis, coal, redstone blocks), amethyst shards | 1 SC | Mixed chest (manual, from overflow) |  |
| 4. Ores & metals | Ancient debris, netherite scrap, netherite ingots | 1 SC | Manual | Never lava (netherite doesn't burn and would clog the disposal). Put away by hand; don't dump into the input |
| 5. Copper | Copper ingots | 1 DC | Hopper slice | Golems, copper chests, copper building blocks |
| 5. Copper | Copper nuggets | 1 SC | Hopper slice | From smelting copper tools and armor; for copper torches, lanterns, chains |
| 5. Copper | Honeycomb | 1 SC | Hopper slice | Wax for golems and copper |
| 5. Copper | Blocks of copper (each oxidation and waxed state is its own item) | 1 SC | Mixed chest (manual, from overflow) | Golems can be built from any state |
| 5. Copper | Cut copper and its stairs and slabs, chiseled copper, copper grates, doors, trapdoors, bulbs, bars, chains, lightning rods, copper torches, copper lanterns | 1 DC | Mixed chest (manual, from overflow) | ★ room to grow. Many item types (oxidation states multiply them) |
| 6. Decorative | Glass | 1 DC | Hopper slice | Smelter output from sand |
| 6. Decorative | Torches | 1 SC | Hopper slice |  |
| 6. Decorative | Item frames | 1 SC | Hopper slice | For labeling every chest |

- **Stage adds:** 8 DC + 47 SC = **31.5 DC-eq**, **39 hopper slices**
- **Cumulative:** 60.5 DC-eq / 54 slices
- **Phase:** [Phase 5](phase-5-infrastructure.md)
- **Smelter loop:** raw iron, gold, and copper go to blast furnaces; raw meat and fish go to smokers. The output goes back to the router.
- **Needs:**
  - Blast furnaces (5 iron ingots + 1 furnace + 3 smooth stone) and smokers (4 logs + 1 furnace).
  - Fuel from the coal and charcoal slices.
  - Much more iron for hoppers: this is the biggest slice jump.
- **Done when:** raw ore and raw food dropped into the input come back as ingots and cooked food in their own chests, without you touching the furnaces.

## Stage 3: groups 6–10, 12, 14, plus the lava disposal

| Group | Item | Chests | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 6. Decorative | Main build block #1 (your pick) | 2 DC | Hopper slice | ★ room to grow. Bulk; whatever the hall and base are made of |
| 6. Decorative | Main build block #2 (your pick) | 2 DC | Hopper slice | ★ room to grow. Bulk |
| 6. Decorative | Glass panes | 1 SC | Hopper slice |  |
| 6. Decorative | White wool | 1 SC | Hopper slice | Sheep output; dye as needed |
| 6. Decorative | Colored wool (15 colors) | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Carpets (16 colors) | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Wool stairs and wool slabs (26.50; 16 colors each, 32 item types) | 1 DC | Mixed chest (manual, from overflow) | More types than a single chest has slots |
| 6. Decorative | Cushions (26.50, 16 colors) | 1 SC | Mixed chest (manual, from overflow) | Stack to 16 |
| 6. Decorative | Concrete (16 colors) | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Concrete powder (16 colors) | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Concrete stairs and slabs (26.50; 32 item types) | 1 DC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Terracotta, dyed terracotta, glazed terracotta (33 types) | 1 DC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Stained glass and stained glass panes (32 types) | 1 DC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Dyes (16) | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Bricks (item) and brick blocks | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Flowers, incl. wildflowers, cactus flowers, eyeblossoms, golden dandelions | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Foliage: leaf litter, short and tall dry grass, bushes, firefly bushes, ferns, vines, red shrubs (26.50) | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Lanterns, soul lanterns, iron chains, glow item frames | 1 SC | Mixed chest (manual, from overflow) |  |
| 6. Decorative | Banners, paintings, flower pots | 1 SC | Mixed chest (manual, from overflow) | Banners stack to 16 |
| 6. Decorative | Other decorative stone (mud bricks, packed mud, tuff bricks, resin bricks, sulfur and cinnabar bricks, polished variants, stairs/slabs/walls) | 1 DC | Mixed chest (manual, from overflow) | ★ room to grow. Promote any you start using a lot to its own slice |
| 7. Redstone | Redstone dust | 1 SC | Hopper slice | ★ room to grow |
| 7. Redstone | Hoppers | 1 SC | Hopper slice | Build stock for new slices |
| 7. Redstone | Comparators, repeaters, redstone torches | 1 SC | Mixed chest (manual, from overflow) |  |
| 7. Redstone | Pistons, sticky pistons, observers, droppers, dispensers, crafters | 1 SC | Mixed chest (manual, from overflow) |  |
| 7. Redstone | Levers, buttons, pressure plates, tripwire hooks, daylight detectors, target blocks, note blocks, redstone lamps | 1 SC | Mixed chest (manual, from overflow) |  |
| 7. Redstone | Slime blocks, honey blocks | 1 SC | Mixed chest (manual, from overflow) | ★ room to grow. Flying machine stock (end game) |
| 8. Transport | Rails | 1 SC | Hopper slice |  |
| 8. Transport | Firework rockets | 1 SC | Hopper slice | ★ room to grow. Elytra fuel later |
| 8. Transport | Powered, detector, activator rails | 1 SC | Mixed chest (manual, from overflow) |  |
| 8. Transport | Leads, name tags, dried ghasts | 1 SC | Mixed chest (manual, from overflow) |  |
| 8. Transport | Boats, chest boats, minecarts (all types) | 1 SC | Manual | Unstackable: from the non-stackable split |
| 8. Transport | Saddles, harnesses, horse armor (incl. copper), nautilus armor | 1 SC | Manual | Unstackable |
| 9. Mob drops | Rotten flesh | 1 DC | Hopper slice | ★ room to grow. Mob-farm bulk; junk-to-lava candidate |
| 9. Mob drops | Bones | 1 DC | Hopper slice | ★ room to grow. Mob-farm bulk; bone meal |
| 9. Mob drops | String | 1 DC | Hopper slice | ★ room to grow. Mob-farm bulk |
| 9. Mob drops | Gunpowder | 1 DC | Hopper slice | ★ room to grow. Mob-farm bulk; rockets |
| 9. Mob drops | Arrows | 1 SC | Hopper slice |  |
| 9. Mob drops | Spider eyes | 1 SC | Hopper slice |  |
| 9. Mob drops | Ender pearls | 1 SC | Hopper slice (stack-16 filter) | Stack to 16 |
| 9. Mob drops | Slimeballs | 1 SC | Hopper slice | Slime blocks for the flying machine |
| 9. Mob drops | Leather | 1 SC | Hopper slice | Books |
| 9. Mob drops | Feathers | 1 SC | Hopper slice |  |
| 9. Mob drops | Ink sacs, glow ink sacs | 1 SC | Mixed chest (manual, from overflow) |  |
| 9. Mob drops | Prismarine shards, prismarine crystals, nautilus shells, hearts of the sea, armadillo scutes, turtle scutes, rabbit hide, wind charges, breeze rods, cobwebs | 1 SC | Mixed chest (manual, from overflow) |  |
| 9. Mob drops | Mob-dropped tools, armor, bows | — | Manual | Unstackable: to the non-stackable intake, never lava |
| 10. Brewing ingredients | Nether wart | 1 SC | Hopper slice | ★ room to grow. Grow it if you build a wart farm |
| 10. Brewing ingredients | Blaze rods | 1 SC | Hopper slice |  |
| 10. Brewing ingredients | Blaze powder | 1 SC | Hopper slice |  |
| 10. Brewing ingredients | Glass bottles | 1 SC | Hopper slice |  |
| 10. Brewing ingredients | Sugar | 1 SC | Hopper slice |  |
| 10. Brewing ingredients | Glowstone dust | 1 SC | Hopper slice |  |
| 10. Brewing ingredients | Glistering melon slices, magma cream, ghast tears, fermented spider eyes, rabbit's feet, phantom membranes, pufferfish, dragon's breath | 1 SC | Mixed chest (manual, from overflow) |  |
| 12. Nether | Netherrack | 1 DC | Hopper slice | ★ room to grow. Grow it only if you build with it |
| 12. Nether | Blackstone | 1 SC | Hopper slice |  |
| 12. Nether | Basalt | 1 SC | Hopper slice |  |
| 12. Nether | Glowstone | 1 SC | Hopper slice |  |
| 12. Nether | Soul sand, soul soil | 1 SC | Mixed chest (manual, from overflow) |  |
| 12. Nether | Nether bricks (block) and nether brick (item) | 1 SC | Mixed chest (manual, from overflow) |  |
| 12. Nether | Crimson and warped stems, nether wart blocks, warped wart blocks, shroomlights, magma blocks, crying obsidian, gilded blackstone, crimson and warped fungi | 1 DC | Mixed chest (manual, from overflow) |  |
| 14. Tools, armor & enchanting (manual) | Tools and weapons (incl. copper tools, spears, maces, bows, crossbows, tridents, shields) | 1 DC | Manual | Unstackable |
| 14. Tools, armor & enchanting (manual) | Armor (incl. copper armor, turtle shells) | 1 DC | Manual | Unstackable |
| 14. Tools, armor & enchanting (manual) | Enchanted books | 1 DC | Manual | ★ room to grow. Unstackable |
| 14. Tools, armor & enchanting (manual) | Books | 1 SC | Hopper slice |  |
| 14. Tools, armor & enchanting (manual) | Bookshelves | 1 SC | Hopper slice |  |
| 14. Tools, armor & enchanting (manual) | Valuables: totems of undying, elytra, heavy cores, trial keys, ominous bottles, bottles o' enchanting | 1 SC | Manual | Never lava |
| 14. Tools, armor & enchanting (manual) | Music discs, goat horns, written books, books and quills | 1 SC | Manual | Discs, horns, books and quills are unstackable; written books stack to 16 |

- **Stage adds:** 18 DC + 49 SC = **42.5 DC-eq**, **30 hopper slices**
- **Cumulative:** 103 DC-eq / 84 slices
- **Phase:** Phase 5
- **Lava disposal:** behind the overflow, burning only when the overflow is full (or junk slices, if you pick a junk list).
- **Needs:**
  - Mob farms running (the four bulk mob-drop slices are sized for them).
  - Nether access for blaze rods and nether wart.
  - A lava source.
- **Before the lava goes live:** every never-lava item must have a slice or go out at the non-stackable split, and shulker shells and netherite stay out of the input.
- **Done when:** farm and mob output sorts hands-free, and the lava has only destroyed junk in testing.

## Stage 4: golem gallery showpiece

| Group | Item | Chests | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 5. Copper | Gallery spares: copper chests, carved pumpkins, copper golem statues | 1 SC | Manual | On Bedrock, statues that froze in survival don't stack (MCPE-225273) |
| 11. Potions & tipped arrows (golem gallery, module 1) | Gallery input copper chest | 1 SC | Golem | Fed by the router (brewing-stand potion filter + tipped-arrow slice) |
| 11. Potions & tipped arrows (golem gallery, module 1) | Display chests: Healing, Regeneration, Strength, Swiftness, Fire Resistance, Night Vision, Slow Falling, Splash Healing, Tipped arrows (1 type) | 9 SC | Golem | 1 chest per type (golems tell types apart on Bedrock). Potions are unstackable, so 27 per chest. Keep 1 in each |
| 11. Potions & tipped arrows (golem gallery, module 1) | Gallery overflow (farthest chest) | 1 SC | Golem | Drains to the main overflow, never back to the router |

- **Stage adds:** 0 DC + 12 SC = **6 DC-eq**, **0 hopper slices**
- **Cumulative:** 109 DC-eq / 84 slices
- **Phase:** Phase 5
- **Router side:** a brewing-stand potion filter and a tipped-arrow slice feed the gallery's copper chest.
- **Needs:**
  - A block of copper (9 copper ingots) and a carved pumpkin per golem, plus honeycomb (shear a bee nest with a campfire under it).
  - Optionally a spare copper chest (8 copper ingots + 1 chest).
  - Brewed potions (Nether access).
  - Iron doors and a glass viewing front.
- **First step:** test one golem with 3–4 seeded chests plus a farthest overflow, and check that glass doesn't break its line of sight.
- **Done when:**
  - The golem visibly sorts each potion type and the tipped arrows into its own display chest behind glass.
  - No empty or unseeded chest is in golem range, and no hopper drains a display chest.
  - The golem and its copper chest are waxed.

## Stage 5: End group, shulker boxes, and the unloader

| Group | Item | Chests | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 13. End | End stone | 1 DC | Hopper slice | ★ room to grow |
| 13. End | Purpur blocks | 1 SC | Hopper slice |  |
| 13. End | Shulker shells | 1 SC | Hopper slice | Never lava; 2 per shulker box |
| 13. End | Chorus fruit, popped chorus fruit | 1 SC | Mixed chest (manual, from overflow) |  |
| 13. End | End rods, eyes of ender | 1 SC | Mixed chest (manual, from overflow) |  |
| 15. Shulker boxes (manual) | Empty shulker boxes | 1 SC | Manual | ★ room to grow. The unloader returns empties here. Unstackable, never lava |
| 15. Shulker boxes (manual) | Packed boxes and kits | 1 SC | Manual | Never lava |

- **Stage adds:** 1 DC + 6 SC = **4 DC-eq**, **3 hopper slices**
- **Cumulative:** 113 DC-eq / 87 slices
- **Phase:** After the End
- **Shulker unloader:** feeds the input line and returns empty boxes to the group 15 chest.
- **Needs:**
  - End city trips for shulker shells; each box is 2 shulker shells + 1 chest.
  - A dispenser and a piston for the unloader.
- **Done when:** dropping a full shulker box at the input empties it into the sorter and returns the empty box, with no box ever reaching the lava.

## Stage 6: expansion (ongoing)

Expansion candidates. "Chests now" is the §3 starting allocation; add capacity at the open end as each one fills.

| Group | Item | Chests now | How sorted | Notes |
| --- | --- | --- | --- | --- |
| 11. Potions & tipped arrows | Golem module 2: 1 copper input chest + 9 display chests + 1 farthest overflow | +11 SC (+5.5 DC-eq) | Golem | More potion and tipped-arrow types (e.g. Water Breathing, Invisibility, Leaping); 1 waxed golem; keep 1 item in each chest |
| any | Mixed-chest items that keep filling the overflow | +1 slice each | Hopper slice | Promote to its own slice |
| 1. Stone family | Cobblestone | 4 DC (Stage 1) | Hopper slice | ★ grow first. Bulk. Junk-to-lava candidate once full (your call) |
| 1. Stone family | Cobbled deepslate | 3 DC (Stage 1) | Hopper slice | ★ grow first. Bulk from deep mining |
| 1. Stone family | Dirt | 2 DC (Stage 1) | Hopper slice | ★ grow first. Bulk for terraforming |
| 2. Wood family | Main wood logs (your tree-farm species) | 3 DC (Stage 1) | Hopper slice | ★ grow first. Bulk from the tree farm |
| 2. Wood family | Accent log #1, #2, #3 (the species you build with most after the main one) | 3 SC (Stage 2) | Hopper slice | ★ grow first. 1 chest each, 3 slices |
| 3. Farming & food | Wheat | 2 DC (Stage 1) | Hopper slice | ★ grow first. Wheat-farm output |
| 3. Farming & food | Sugar cane | 1 DC (Stage 1) | Hopper slice | ★ grow first. Paper (books, maps) and sugar |
| 4. Ores & metals | Coal | 2 DC (Stage 1) | Hopper slice | ★ grow first. Smelter fuel and torches |
| 4. Ores & metals | Iron ingots | 2 DC (Stage 1) | Hopper slice | ★ grow first. 5 per hopper; more once an iron farm runs |
| 4. Ores & metals | Emeralds | 1 SC (Stage 2) | Hopper slice | ★ grow first. Grow it if you build a trading hall |
| 5. Copper | Cut copper and its stairs and slabs, chiseled copper, copper grates, doors, trapdoors, bulbs, bars, chains, lightning rods, copper torches, copper lanterns | 1 DC (Stage 2) | Mixed chest (manual, from overflow) | ★ grow first. Many item types (oxidation states multiply them) |
| 6. Decorative | Main build block #1 (your pick) | 2 DC (Stage 3) | Hopper slice | ★ grow first. Bulk; whatever the hall and base are made of |
| 6. Decorative | Main build block #2 (your pick) | 2 DC (Stage 3) | Hopper slice | ★ grow first. Bulk |
| 6. Decorative | Other decorative stone (mud bricks, packed mud, tuff bricks, resin bricks, sulfur and cinnabar bricks, polished variants, stairs/slabs/walls) | 1 DC (Stage 3) | Mixed chest (manual, from overflow) | ★ grow first. Promote any you start using a lot to its own slice |
| 7. Redstone | Redstone dust | 1 SC (Stage 3) | Hopper slice | ★ grow first. |
| 7. Redstone | Slime blocks, honey blocks | 1 SC (Stage 3) | Mixed chest (manual, from overflow) | ★ grow first. Flying machine stock (end game) |
| 8. Transport | Firework rockets | 1 SC (Stage 3) | Hopper slice | ★ grow first. Elytra fuel later |
| 9. Mob drops | Rotten flesh | 1 DC (Stage 3) | Hopper slice | ★ grow first. Mob-farm bulk; junk-to-lava candidate |
| 9. Mob drops | Bones | 1 DC (Stage 3) | Hopper slice | ★ grow first. Mob-farm bulk; bone meal |
| 9. Mob drops | String | 1 DC (Stage 3) | Hopper slice | ★ grow first. Mob-farm bulk |
| 9. Mob drops | Gunpowder | 1 DC (Stage 3) | Hopper slice | ★ grow first. Mob-farm bulk; rockets |
| 10. Brewing ingredients | Nether wart | 1 SC (Stage 3) | Hopper slice | ★ grow first. Grow it if you build a wart farm |
| 12. Nether | Netherrack | 1 DC (Stage 3) | Hopper slice | ★ grow first. Grow it only if you build with it |
| 13. End | End stone | 1 DC (Stage 5) | Hopper slice | ★ grow first. |
| 14. Tools, armor & enchanting (manual) | Enchanted books | 1 DC (Stage 3) | Manual | ★ grow first. Unstackable |
| 15. Shulker boxes (manual) | Empty shulker boxes | 1 SC (Stage 5) | Manual | ★ grow first. The unloader returns empties here. Unstackable, never lava |

- **Stage adds:** +5.5 DC-eq for golem module 2, then as needed
- **Cumulative:** 118.5+ DC-eq / 87+ slices
- **Phase:** Ongoing
- Add slices at the open end. Grow the **★** items first, and promote mixed-chest items that keep filling the overflow.
- Expand the smelter as ore and food volume grows.
- Dress the hall as the [Copper storage hall](building-goals.md#2-copper-storage-hall).
- Add a backup storage room (Phase 5 backups), and clean up anything that causes lag.
- **Done when:** ongoing. There's no finish line; keep rule 8 (stream end and chest-wall ends open).

**Every stage keeps rule 8:** the end of the stream and the far ends of the chest walls stay open ([adjacency rules](storage-layout.md#adjacency-rules)).
