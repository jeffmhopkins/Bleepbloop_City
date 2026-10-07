# Big goal: Automated item sorter with copper golems

**Goal:** A highly automated item sorter for the real base that makes heavy use of copper golems.
**Status:** ⬜ Not started
**Fits in:** grows out of the [Phase 4 storage wall](phase-4-the-base.md#1-storage-wall) and becomes the [Phase 5](phase-5-infrastructure.md) "proper storage system with item sorters".

> **Sources.** Every copper golem, copper chest, and hopper fact below was checked against the Minecraft Wiki on 2026-10-07:
> [Copper Golem](https://minecraft.wiki/w/Copper_Golem) · [Copper Chest](https://minecraft.wiki/w/Copper_Chest) · [Copper Golem Statue](https://minecraft.wiki/w/Copper_Golem_Statue) · [Honeycomb](https://minecraft.wiki/w/Honeycomb) · [Block of Copper](https://minecraft.wiki/w/Block_of_Copper) · [Hopper](https://minecraft.wiki/w/Hopper) · [Redstone Comparator](https://minecraft.wiki/w/Redstone_Comparator) · [Tutorial: Hopper (item sorter)](https://minecraft.wiki/w/Tutorial:Hopper#Item_sorter)
> If something behaves differently in-game, trust the game and fix this file.

## How copper golems work (verified)

### Making one
- Place a **block of copper** (any oxidation stage), then put a **carved pumpkin or jack o'lantern** on it. The pumpkin has to be placed last. It also works sideways or upside down.
- The copper block turns into a **copper chest**, and the golem appears where the pumpkin was. The chest and golem start at the same oxidation stage as the copper block.
- A waxed copper block works too, but the new golem and chest are **not** waxed.
- If the new copper chest ends up next to another copper chest facing the same way, the two merge into a large copper chest.
- **Wilderness Bound bonus:** oxidized copper golem statues and oxidized copper chests now generate in **abandoned camps** (Java 26.3 / Bedrock 26.50). Scrape a statue with an axe until it's unoxidized, then one more scrape brings it back to life as a golem.

### What they do
- **Pick up:** an empty-handed golem opens the nearest **copper chest** and takes up to **16 of the first item** it finds.
- **Drop off:** it then opens the nearest **wooden chest or trapped chest**. It only puts items in a chest that is **empty** or **already holds that same item type**.
- Each chest it checks takes **3 seconds**. It remembers up to 9 chests. If it checks 10 and still can't place (or find) anything, it wanders for 7 seconds, forgets, and starts over. It forgets its list every time it successfully drops something off.
- It doesn't remember where things go. It opens chests and looks every time.
- It matches item **type only**. It ignores durability, enchantments, custom names, and what's inside shulker boxes and bundles. On Java it can't tell potion types, tipped arrow types, or suspicious stew types apart; on Bedrock it can.
- It puts items in the frontmost open slot.
- Two golems won't open the same chest at the same time.

### Range and limits
- Search area is **65×17×65** around the golem (32 blocks out horizontally, 8 blocks up and down).
- It can't use a chest more than **1 block above** it or more than **2 blocks below** it. It will walk to reach chests if it can path there.
- It **only** uses wooden chests, trapped chests, and copper chests. It ignores barrels, ender chests, chest minecarts, chest boats, other containers, and items on the ground.
- A chest can't be opened if a cat is sitting on it, and a copper chest can't be opened if there's a conductive block directly on top of it. Copper chests themselves aren't conductive, so you can stack them.
- Golems keep working when you're more than 32 blocks away (they don't pause like most passive mobs).
- They can open non-iron doors, don't take fall damage, and sink and walk along the bottom in water.
- On Bedrock, a golem on a leash doesn't carry items.

### Oxidation, waxing, and scraping
- Unwaxed golems go through four stages: unoxidized → exposed → weathered → oxidized. Each stage takes about **7 hours to 7 hours 40 minutes of game time** (21–23 in-game days). The timer runs on game time, so it keeps going even if the golem's chunk isn't loaded.
- Once fully oxidized, an unwaxed golem soon turns into a **copper golem statue** and **drops whatever it's holding**. It can't turn into a statue while underwater or while standing on a partial block like a slab.
- **Wax it:** use a **honeycomb** on the golem. That stops oxidation and stops it from ever turning into a statue. Honeycomb comes from shearing a full bee nest or beehive (3 per shear; a campfire underneath keeps the bees calm).
- **Unwax it:** use an axe on a waxed golem.
- **Scrape it:** an axe on an unwaxed golem removes one oxidation stage. Lightning does the same to unwaxed golems.
- **Statues:** an axe removes one stage at a time. Scraping a fully unoxidized statue brings the golem back. Statues can also be waxed with honeycomb.
- Copper chests oxidize too. Golems use them **no matter their oxidation or wax state**. Wax them with honeycomb (in the crafting grid or by using it on the chest), or scrape them by using an axe while sneaking.

## Design considerations

### Golems vs. hopper sorters: use both
| | Copper golem sorting | Hopper/comparator item sorter |
| --- | --- | --- |
| Speed | Slow: up to 16 items per trip, 3 s per chest it checks | About 2.5 items per second per sorter line (5 with double-speed designs) |
| Setup | Copper block + pumpkin per golem; plain chests | 5 iron per hopper, comparators need nether quartz, redstone per slice |
| Filtering | Item type only; any **empty** chest accepts anything | Exact item per filter slice; needs an overflow chest at the end |
| Containers | Wooden/trapped chests only | Any container hoppers feed |
| Best for | Bulk and common categories, mixed loot dumps, "put it away" chores | High-volume items from farms (iron farm, sugar cane, mob drops) |

**Plan:** golems handle the everyday "dump and walk away" sorting. Hopper sorters handle the high-volume farm outputs where golems would fall behind.

### Rules that fall out of the mechanics
- **No empty destination chests.** A golem will put anything into an empty wooden chest, so seed every destination chest with at least one of the item(s) it should hold. Keep spare empty chests out of golem range or make them copper chests.
- **Category chests are just seeded chests.** A golem matches by item type, so a "wood" chest needs one of each wood item you want in it.
- **Overflow chest.** Put a seeded "junk/overflow" chest farther from the input than the real chests, and watch for golems giving up (the "can't place item" sound).
- **Keep the unsorted stuff in copper chests** and the sorted stuff in wooden chests. Golems only *take* from copper chests and only *deliver* to wooden/trapped chests.
- **Vertical layout:** destination chests within 1 block above and 2 below the golem's floor. A single floor or a short step is safer than tall chest walls.
- **Wax every golem and every input copper chest early**, or schedule scraping. A golem that becomes a statue drops its load on the floor.
- **No slabs, barrels, or ender chests in the sorting room** where golems are expected to deliver.
- **Separate golem rooms.** The search area is big (65×17×65). Keep golem rooms far enough from other chests (the storage wall, the workshop, farm chests) that golems don't wander off and fill them.

### Fitting it into the base
- **Input chest by the door:** the Phase 4 storage wall already calls for one input chest by the door. Make that a **copper chest**, so dumping inventory there feeds the golems automatically.
- **3-block service gap:** keep the 3-block gap behind the storage wall from [building style](building-style.md) for hopper lines and redstone, so the sorter can grow without tearing the front off.
- **Away from the pretty part:** Phase 5 says to build sorting systems away from the pretty part of the base so lag stays outside. The wiki notes that long hopper pipes can add steady lag, and water item streams can add more while items are flowing.
- **Doors:** golems open non-iron doors, so use iron doors (or no door) wherever golems must stay in.
- **Lighting and spawn control** as in Phase 4. The golem room counts as part of the build.

## Stages

### Stage 0 — Prototype (test one golem)
- [ ] Find copper (or raid an abandoned camp for an oxidized statue or copper chest)
- [ ] Get honeycomb (shear a bee nest with a campfire under it)
- [ ] Build one golem (copper block + carved pumpkin, pumpkin last)
- [ ] Wax the golem and its copper chest
- [ ] Place 3–4 seeded wooden chests nearby plus one overflow chest
- [ ] Dump mixed items in the copper chest and watch where they go
- [ ] Write down what surprised me in the notes below

### Stage 1 — Small golem room (storage wall helpers)
- [ ] Pick the room location and log it in [coordinates](../notes/coordinates.md)
- [ ] Make the input chest by the door a copper chest
- [ ] Seed one wooden chest per storage-wall category: wood, stone, ores, food, mob drops, redstone, junk
- [ ] 2–3 waxed golems
- [ ] Iron door / walls so golems stay in, room fully lit
- [ ] Check that no unseeded or empty wooden chests are in golem range

### Stage 2 — Full system
- [ ] Split categories into more specific seeded chests as storage grows
- [ ] More golems and more copper input chests where loot comes in (mine entrance, Nether portal room, farm outputs)
- [ ] First hopper/comparator sorter line for the highest-volume farm item, with an overflow chest at the end
- [ ] Route high-volume farm output into hopper sorters; route mixed loot into golem copper chests
- [ ] Item frames or signs on every chest
- [ ] Maintenance routine: check wax on golems and chests

### Stage 3 — Expansion
- [ ] Move or extend the system with the Phase 5 "proper storage system with item sorters", away from the pretty part of the base
- [ ] More hopper sorter slices as new farms come online (iron farm, sugar cane, mob grinder)
- [ ] Backup storage room (Phase 5 backups)
- [ ] Clean up anything that causes lag

## Materials (verified recipes only)

| Item | Recipe / source | Need |
| --- | --- | --- |
| Block of copper | 9 copper ingots | 1 per golem you build |
| Carved pumpkin or jack o'lantern | — | 1 per golem |
| Honeycomb | Shear a full bee nest or beehive (3 per shear) | 1 per golem, copper chest, or statue to wax |
| Copper chest | 8 copper ingots around 1 chest | 1 per extra input chest (each new golem also makes one) |
| Wooden chests | — | 1 per sorted item type or category, plus overflow |
| Hopper | 5 iron ingots + 1 chest | Several per hopper sorter slice and pipe |
| Redstone comparator | 3 redstone torches + 1 nether quartz + 3 stone | 1 or more per hopper sorter slice, depending on the design |
| Axe | — | For scraping oxidation and wax |

Exact counts depend on how many golems and categories I end up with. Fill in once the layout is picked.

## Open questions for Jeffrey

- [ ] How many sort categories to start with? The Phase 4 list (wood, stone, ores, food, mob drops, redstone, junk) or finer?
- [ ] Which edition are we playing mostly, Java or Bedrock? It changes how golems handle potions and arrows.
- [ ] Where does the sorting room go: under the base, behind the storage wall, or a separate building?
- [ ] Wax everything, or let some golems oxidize on purpose for looks and scrape them?
- [ ] Which farm outputs get hopper sorters first?
- [ ] Is anyone else on the server sharing this storage?

## Done when

- [ ] Dumping inventory into the copper input chest by the door gets everything sorted without me touching it
- [ ] Every golem and input copper chest is waxed (or on a scraping schedule)
- [ ] High-volume farm output goes through hopper sorters with an overflow chest
- [ ] No empty or unseeded wooden chests in any golem's range
- [ ] The system sits away from the pretty part of the base and runs without lag

## Notes

_Golem counts, chest layouts, what broke, and what worked go here._
