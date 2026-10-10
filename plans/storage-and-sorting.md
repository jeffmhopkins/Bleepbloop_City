# Big goal: Automated item sorter (hopper chest hall + copper golem gallery)

**Goal:** A highly automated item sorter for the real base. **Hopper filters fed by a water/ice item stream (a Bedrock chest hall) do the primary sorting**, and **copper golems are the showpiece**: a glass-fronted golem gallery at the front of the hall where a few waxed golems sort a small set of everyday items (potions and tipped arrows) into display chests you can watch.
**Role change (2026-10-07):** Jeffrey asked to make the golems "a visual thing in the front of the hall, not necessarily the primary sorting mechanism". The golem research below is still valid; it now applies to the gallery.
**Status:** see the [tracker](../progress/tracker.md).
**Hall layout:** [Jeffrey's sketch](storage-layout.md#hall-layout-jeffreys-sketch) and [item flow](storage-layout.md#item-flow): shulker unloader at the center of Machinery feeding the router below it, dump barrels to the right, smelter on the left, intake/overflow/lava on the right; a U-shaped under-floor stream down one side of the central aisle, under the Dome (golem gallery) at the entrance, and back up the other side; each wing a hallway with chest walls on both sides.
**Stages:** [one table per stage](storage-stages.md).
**Grouping:** see [storage-layout.md](storage-layout.md) for functional adjacency rules, the hard technical constraints, and the item groups for the chest walls. The building itself is a custom build Jeffrey designs; no shape or size is prescribed.
**Always loaded:** the sorter and iron farm go in a Bedrock ticking area so they run with nobody nearby. See [Server config: ticking area](multiplayer-server.md#ticking-area-iron-farm-and-item-sorter) (mob spawning still needs a player nearby).
**Showpiece build:** the [Copper storage hall](building-goals.md#2-copper-storage-hall) building goal is the home for this system.
> **Bedrock server.** Bleepbloop City runs on **Bedrock Edition** (26.50, Wilderness Bound). Every mechanic and design here has to be Bedrock-compatible. Redstone, hopper, and piston timing differ from Java, so many Java tutorials and schematics won't work as-is. Look for Bedrock-tested designs, and treat any Java-only note below as not applying.

**Fits in:** grows out of the [Phase 4 storage wall](phase-4-the-base.md#1-storage-wall) and becomes the [Phase 5](phase-5-infrastructure.md) "proper storage system with item sorters".

> **Sources.** Every copper golem, copper chest, hopper, and add-on fact below was checked against the Minecraft Wiki on 2026-10-07 and re-checked for Bedrock the same day:
> [Copper Golem](https://minecraft.wiki/w/Copper_Golem) · [Copper Chest](https://minecraft.wiki/w/Copper_Chest) · [Copper Golem Statue](https://minecraft.wiki/w/Copper_Golem_Statue) · [Honeycomb](https://minecraft.wiki/w/Honeycomb) · [Block of Copper](https://minecraft.wiki/w/Block_of_Copper) · [Hopper](https://minecraft.wiki/w/Hopper) · [Redstone Comparator](https://minecraft.wiki/w/Redstone_Comparator) · [Tutorial: Hopper (item sorter)](https://minecraft.wiki/w/Tutorial:Hopper#Item_sorter) · [Furnace](https://minecraft.wiki/w/Furnace) · [Blast Furnace](https://minecraft.wiki/w/Blast_Furnace) · [Smoker](https://minecraft.wiki/w/Smoker) · [Shulker Box](https://minecraft.wiki/w/Shulker_Box) · [Dispenser](https://minecraft.wiki/w/Dispenser) · [Dropper](https://minecraft.wiki/w/Dropper) · [Piston](https://minecraft.wiki/w/Piston) · [Cactus](https://minecraft.wiki/w/Cactus) · [Lava](https://minecraft.wiki/w/Lava)
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
- It matches item **type only**. It ignores durability, enchantments, custom names, and what's inside shulker boxes and bundles. **On Bedrock (our server) it *can* tell potion types, tipped arrow types, and suspicious stew types apart**; on Java it can't.
- It puts items in the frontmost open slot.
- Two golems won't open the same chest at the same time.

### Range and limits
- Search area is **65×17×65** around the golem (32 blocks out horizontally, 8 blocks up and down).
- It can't use a chest more than **1 block above** it or more than **2 blocks below** it. It will walk to reach chests if it can path there.
- It **only** uses wooden chests, trapped chests, and copper chests. It ignores barrels, ender chests, chest minecarts, chest boats, other containers, and items on the ground.
- A chest can't be opened if a cat is sitting on it, and a copper chest can't be opened if there's a conductive block directly on top of it. **On Bedrock, a bottom slab on top also blocks it** (on Java the lid phases through bottom slabs). Copper chests themselves aren't conductive, so you can stack them.
- **Bedrock:** golems don't interact with chests or copper chests they can't see, so keep a clear line of sight. Bedrock golems are a little wider than Java ones (0.6 vs 0.49 blocks) but can still path through 1-block-high passages.
- The wiki says golems keep working when you're more than 32 blocks away (they don't pause like most passive mobs). It doesn't say whether that differs on Bedrock, so test it on the server.
- They can open non-iron doors, don't take fall damage, and sink and walk along the bottom in water.
- On Bedrock, a golem on a leash doesn't carry items.

### Oxidation, waxing, and scraping
- Unwaxed golems go through four stages: unoxidized → exposed → weathered → oxidized. The wiki gives about **7 hours to 7 hours 40 minutes of game time** per stage (21–23 in-game days), running on game time even when the chunk isn't loaded. That figure comes from Java data; the wiki doesn't list Bedrock timing separately. Either way, wax them.
- Once fully oxidized, an unwaxed golem soon turns into a **copper golem statue** and **drops whatever it's holding**. It can't turn into a statue while underwater or while standing on a partial block like a slab.
- **Wax it:** use a **honeycomb** on the golem. That stops oxidation and stops it from ever turning into a statue. Honeycomb comes from shearing a full bee nest or beehive (3 per shear; a campfire underneath keeps the bees calm).
- **Unwax it:** use an axe on a waxed golem.
- **Scrape it:** an axe on an unwaxed golem removes one oxidation stage. Lightning does the same to unwaxed golems.
- **Statues:** an axe removes one stage at a time. Scraping a fully unoxidized statue brings the golem back. Statues can also be waxed with honeycomb.
- Copper chests oxidize too. Golems use them **no matter their oxidation or wax state**. Wax them with honeycomb (in the crafting grid or by using it on the chest), or scrape them by using an axe while sneaking.

## Design considerations

### Golems vs. hopper sorters: hoppers sort, golems show off
| | Copper golem sorting | Hopper/comparator item sorter |
| --- | --- | --- |
| Speed | Slow: up to 16 items per trip, 3 s per chest it checks | About 2.5 items per second per hopper (0.4 s cooldown) |
| Setup | Copper block + pumpkin per golem; plain chests | 5 iron per hopper, comparators need nether quartz, redstone per slice |
| Filtering | Item type only; any **empty** chest accepts anything | Exact item per filter slice; needs an overflow chest at the end |
| Containers | Wooden/trapped chests only | Any container hoppers feed |
| Best for | Bulk and common categories, mixed loot dumps, "put it away" chores | High-volume items from farms (iron farm, sugar cane, mob drops) |

**Bedrock hopper sorter notes** ([Tutorial: Hopper](https://minecraft.wiki/w/Tutorial:Hopper#Item_sorter), [Hopper](https://minecraft.wiki/w/Hopper))
- On Bedrock, a hopper pipe moving a full load at full speed lets a small percentage of items slip past the filters (bug MCPE-28890). Don't run stacked input at full speed through the filters, and keep an overflow chest.
- The wiki lists a **Bedrock-optimized hopper item sorter** and notes Bedrock filter-count tweaks for hybrid designs (e.g. 20 instead of 21 filler items). Use those, not the Java designs.
- On Bedrock, hopper chains with air or non-container blocks on top run *better* than ones topped by containers. That's the opposite of the Java composter-on-top trick.

**Plan (updated 2026-10-07):**
- **Hoppers are the primary system.** A Bedrock chest hall (1-wide slices, filters under a water/ice item stream) sorts everything stackable, from "dump and walk away" inventory to high-volume farm output.
- **Golems are the showpiece.** The golem gallery near the entrance sorts potions and tipped arrows, which golems can tell apart on Bedrock and hopper filters can't easily handle. It's small (about 2 golems), visible through glass, and doesn't carry the main load.

### Golem gallery rules (from the mechanics)
- **No empty destination chests.** A golem will put anything into an empty wooden chest, so seed every destination chest with at least one of the item(s) it should hold. Keep spare empty chests out of golem range or make them copper chests.
- **Category chests are just seeded chests.** A golem matches by item type, so a "wood" chest needs one of each wood item you want in it.
- **Overflow chest.** Put a seeded "junk/overflow" chest farther from the input than the real chests, and watch for golems giving up (the "can't place item" sound).
- **Keep the unsorted stuff in copper chests** and the sorted stuff in wooden chests. Golems only *take* from copper chests and only *deliver* to wooden/trapped chests.
- **Vertical layout:** destination chests within 1 block above and 2 below the golem's floor. A single floor or a short step is safer than tall chest walls.
- **Wax every golem and every input copper chest early**, or schedule scraping. A golem that becomes a statue drops its load on the floor.
- **No slabs, barrels, or ender chests in the sorting room** where golems are expected to deliver, and no bottom slabs on top of copper chests (Bedrock blocks them from opening).
- **Seal the golem gallery.** The search area is big (65×17×65). Keep the gallery sealed and far enough from other chests (the storage wall, the workshop, farm chests) that golems don't wander off and fill them.

### Fitting it into the base
- **Input by the door:** the Phase 4 storage wall calls for one input chest by the door. With hoppers primary, make the input **barrels** by the entrance (hoppers empty barrels, and golems ignore them). Copper chests are used only as the golem gallery's input, fed by the router.
- **3-block service gap:** keep the 3-block gap behind the storage wall from [building style](building-style.md) for hopper lines and redstone, so the sorter can grow without tearing the front off.
- **Away from the pretty part:** Phase 5 says to build sorting systems away from the pretty part of the base so lag stays outside. The wiki notes that long hopper pipes can add steady lag, and water item streams can add more while items are flowing.
- **Doors:** golems open non-iron doors, so use iron doors (or no door) wherever golems must stay in.
- **Lighting and spawn control** as in Phase 4. The golem gallery counts as part of the build.

## Grouping

The storage hall's architecture is Jeffrey's own grand custom build (see [building style: inspiration](building-style.md#inspiration)). The plan only fixes **what sits next to what** and **how items are grouped**. Full detail in **[storage-layout.md](storage-layout.md)**:
- Input next to the router, and the router feeding the start of the item stream.
- Filters directly behind the chest walls they fill, with 3-block service access behind every wall.
- Smelter, overflow, and lava together on the machine side, away from wood and showpiece areas.
- The golem gallery near the entrance as the showpiece, sealed from other chests.
- The expansion end kept open.

Key rules:
- **Golem gallery module = 1 copper input chest + 9 display chests + 1 overflow chest per golem.** The overflow is the **farthest** chest from the golem. The golem is pinned forward (trapdoor/chains or a minecart).
- **Never drain a golem display chest with a hopper** (an empty chest becomes a "put anything here" chest), and keep 1 item in each.
- **The router only feeds** hopper slices, the smelter, the non-stackable chest, or the gallery's **copper** chest. It never feeds golem display chests.

## Sorter add-ons

Jeffrey's ask: the item sorter also needs an **auto furnace**, a **shulker box auto unloader**, and a **garbage furnace**. All three hang off the sorter: items come *out of* the sorter into the add-on, and anything useful goes *back into* storage.

> **Bedrock reminder:** pick a Bedrock-tested design for each add-on. The notes below are verified mechanics and a rough layout, not a block-by-block build. Bedrock hoppers lock only on the C-tick and Bedrock pistons start 2 game ticks after activation (also C-tick only), so Java timing builds may misbehave. ([Hopper](https://minecraft.wiki/w/Hopper), [Piston](https://minecraft.wiki/w/Piston))

> **Golem trap to avoid:** if a hopper drains a wooden chest that golems deliver to, that chest ends up **empty**, and golems put *anything* into an empty chest. Don't feed add-ons straight from a golem destination chest. Put a hopper-sorter filter slice between the chest and the add-on, or keep that chest out of golem range.

### Auto furnace / smelter array

**What it does:** ores and raw food that come out of the sorter get smelted or cooked automatically, and the results go back into storage.

**Verified mechanics** ([Furnace](https://minecraft.wiki/w/Furnace), [Blast Furnace](https://minecraft.wiki/w/Blast_Furnace), [Smoker](https://minecraft.wiki/w/Smoker), [Hopper](https://minecraft.wiki/w/Hopper))
- A hopper pointing into the **top** of a furnace fills the ingredient slot. It will push *any* item, even ones that can't be smelted, so filter before the furnace.
- A hopper pointing into the **side** fills the fuel slot, and only accepts fuel.
- A hopper **below** pulls everything out of the output slot (plus empty buckets left over from lava fuel).
- A furnace takes 10 seconds per item. One coal burns 80 seconds, which is 8 items.
- **Blast furnace** (ores, Jeffrey's plan): twice as fast, but only smelts raw metal, ore blocks, ancient debris, and iron/gold/chainmail/copper tools and armor.
- **Smoker** (food, Jeffrey's plan): twice as fast (5 s per item), food only.
- Both burn fuel twice as fast, so you get the same number of items per fuel.
- XP from hopper-extracted items is stored in the furnace until a player takes an output item, or the furnace is broken.

**How it connects**
- **Input line:** sorter filter slices for raw ores/raw metal → hopper line over the **blast furnaces**; raw food → hopper line over the **smokers**; everything else smeltable (sand, cobble, etc.) → regular furnaces.
- **Fuel line:** a fuel chest → hoppers into the side of each furnace.
- **Output collection:** hoppers under each furnace → a collection line → back into the sorter input (or straight into the right storage chests).
- Spreading items evenly across an array varies by design. Pick a Bedrock furnace-array tutorial for this.

**Tasks**
- [ ] Pick a Bedrock-compatible furnace array design
- [ ] Ore filter slices in the sorter → blast furnace input line
- [ ] Raw food filter slices → smoker input line
- [ ] Fuel chest + fuel line into the sides
- [ ] Output hoppers → back into storage
- [ ] Spot to collect the stored XP

**Done when**
- [ ] Raw ores and raw food that enter the sorter come back out smelted/cooked in storage without me touching them
- [ ] Fuel is refilled from one chest

### Shulker box auto unloader

**What it does:** drop a full shulker box in, its contents get emptied into the sorter, and the empty box comes back out.

**Where:** at the center of the back Machinery section, at the head of the aisle, feeding straight down into the router directly below it ([hall layout](storage-layout.md#item-flow)). The dump barrels are to the router's right.

**Verified mechanics** ([Shulker Box](https://minecraft.wiki/w/Shulker_Box), [Dispenser](https://minecraft.wiki/w/Dispenser), [Hopper](https://minecraft.wiki/w/Hopper), [Tutorial: Hopper, special item filters](https://minecraft.wiki/w/Tutorial:Hopper#Potions,_books_and_shulker_boxes))
- Hoppers can both put items into and pull items out of a placed shulker box.
- A **dispenser can place a shulker box** as a block. If there's a block under the spot, the box faces up; if not, it faces the same way as the dispenser.
- A shulker box **pushed by a piston breaks and drops as an item**, keeping its contents. It can't be pulled by a sticky piston.
- A shulker box needs a clear half-block in front of its lid to open. On Bedrock, a redstone-conductive block there also blocks it.
- Hoppers and droppers **can't put a shulker box into another shulker box**. That lets you use a placed shulker box as a filter to separate shulker boxes from other items.
- On Bedrock, comparators can read how full a container is through a piston.

**How it connects (rough layout)**
1. **Input:** a hopper or chest where you drop full boxes → a dispenser.
2. The dispenser places the box. A hopper under it empties the box into the **sorter input line**.
3. When a comparator reads the box as empty, a piston pushes it, so it breaks and drops as an item.
4. A hopper collects the empty box → an **output chest** for empty boxes, not the sorter.
5. Exact timing and wiring vary. Pick a Bedrock shulker unloader tutorial rather than a Java one.

**Tasks**
- [ ] Get shulker shells (2 per box)
- [ ] Pick a Bedrock shulker box unloader design
- [ ] Build it next to the sorter input line
- [ ] Empty-box output chest
- [ ] Test with one box of cobble before trusting it with valuables

**Done when**
- [ ] A full shulker box dropped in comes out empty, and its items end up sorted

### Garbage disposal ("garbage furnace")

> **Decision (2026-10-07):** use **lava**. Netherite-related items won't burn, so keep them out of the junk path.

**What it does:** junk and overflow get destroyed automatically, so full chests never back up the sorter.

**Verified options** ([Lava](https://minecraft.wiki/w/Lava), [Cactus](https://minecraft.wiki/w/Cactus), [Furnace](https://minecraft.wiki/w/Furnace), [Hopper](https://minecraft.wiki/w/Hopper))
| Option | How it works | Watch out for |
| --- | --- | --- |
| **Lava** | Items dropped into lava are destroyed immediately | Netherite-related items don't burn. |
| **Cactus** | Destroys items that touch it | Has to sit on sand. It breaks if a solid block or lava is beside it. |
| **Furnace-style burner** | A hopper into a furnace's top pushes any item. Furnaces don't destroy items, though: unsmeltable items just sit there and clog it. | So a literal furnace isn't a disposal. "Garbage furnace" probably means a lava burner (a dropper or hopper feeding lava). |

**How it connects**
- **Junk category:** sorter filter slices for known junk (Jeffrey picks the list) → disposal.
- **Overflow / unsorted path:** the end of the sorter line → overflow chest → when that's full, overflow → disposal. That way the system never clogs.
- ⚠️ **Keep valuable categories out of it.** Anything that reaches the disposal is gone. Make sure every valuable item has its own filter slice *before* the overflow. Keep tools, armor, enchanted books, and shulker boxes on their own path. The unstackable and shulker box filters on the [hopper tutorial](https://minecraft.wiki/w/Tutorial:Hopper#Special_item_filters) can help.
- Golem side: a golem junk chest drained by a hopper becomes an empty chest, and golems will fill it with anything. See the golem trap note above.

**Tasks**
- [x] Decide the disposal type: lava (2026-10-07)
- [ ] Decide the junk list
- [ ] Filter slices for junk → disposal
- [ ] Overflow chest → overflow → disposal
- [ ] Valuables filtered out before the overflow
- [ ] Test with cobble/dirt first

**Done when**
- [ ] Junk and true overflow are destroyed automatically, the sorter never backs up, and nothing valuable has been lost in testing

## Stages

**Per-stage item tables:** [storage-stages.md](storage-stages.md) (one table per stage).

**The growth stages now live in one place: [storage-layout.md § Growth stages](storage-layout.md#4-growth-stages).** Each stage there lists what gets automated, the chests and slices added (from the [per-item allocation](storage-layout.md#3-item-by-item-chest-allocation)), its prerequisites, and a "done when".

Stages follow the **build order** of Jeffrey's hall. Every group has one wing in the [finished hall](storage-layout.md#final-layout-finished-hall), and each stage automates the groups living in the wings it builds.

| Stage | Wings built | Groups automated | Adds | Cumulative |
| --- | --- | --- | --- | --- |
| 0 | None (Phase 4 storage wall) | Manual chests by group, plus one test hopper slice | — | 0 / 0 |
| 1 | Front-left, plus Machinery core and the whole U trunk | 1 Stone family; overflow + intake | 20 DC-eq, 13 slices | 20 / 13 |
| 2 | Front-right, plus smokers ([auto furnace](#auto-furnace--smelter-array)) | 3 Farming & food; 10 Brewing | 18 DC-eq, 22 slices | 38 / 35 |
| 3 | Mid-left and mid-right, plus blast furnaces and the [lava disposal](#garbage-disposal-garbage-furnace) (junk list only until Stage 5) | 4 Ores & metals; 5 Copper; 7 Redstone; 2 Wood; 6 Decorative build blocks | 33.5 DC-eq, 30 slices | 71.5 / 65 |
| 4 | Dome | 11 Golem gallery (module 1) + spares | 6 DC-eq | 77.5 / 65 |
| 5 | Back-left and back-right, plus the [shulker unloader](#shulker-box-auto-unloader) above the router | 6 Decorative colors & finishes; 12 Nether; 13 End; 9 Mob drops; 14 Tools, armor & enchanting; 8 Transport; 15 Shulker boxes | 35.5 DC-eq, 22 slices | 113 / 87, then growth in every wing |

## Materials (verified recipes only)

| Item | Recipe / source | Need |
| --- | --- | --- |
| Block of copper | 9 copper ingots | 1 per golem you build |
| Carved pumpkin or jack o'lantern | — | 1 per golem |
| Honeycomb | Shear a full bee nest or beehive (3 per shear) | 1 per golem, copper chest, or statue to wax |
| Copper chest | 8 copper ingots around 1 chest | 1 per extra input chest (each new golem also makes one) |
| Wooden chests | — | 1 per sorted item type, plus overflow and gallery display chests |
| Hopper | 5 iron ingots + 1 chest | Several per hopper sorter slice and pipe |
| Redstone comparator | 3 redstone torches + 1 nether quartz + 3 stone | 1 or more per hopper sorter slice, depending on the design |
| Axe | — | For scraping oxidation and wax |
| Furnace | 8 cobblestone (or other stone-tier blocks) | Regular furnaces in the array |
| Blast furnace | 5 iron ingots + 1 furnace + 3 smooth stone | Ore line of the auto furnace |
| Smoker | 4 logs (or wood/stems) + 1 furnace | Food line of the auto furnace |
| Dispenser | 7 cobblestone + 1 bow + 1 redstone dust | Shulker unloader (places the box) |
| Dropper | 7 cobblestone + 1 redstone dust | Optional: feeding a lava disposal |
| Piston | 3 planks + 4 cobblestone + 1 iron ingot + 1 redstone dust | Shulker unloader (breaks the empty box) |
| Shulker box | 2 shulker shells + 1 chest | Test boxes for the unloader |

Chest counts per item are in the [per-item allocation](storage-layout.md#3-item-by-item-chest-allocation) (113 DC-eq, 87 filter slices through Stage 5). Hopper counts depend on the slice design you pick: multiply its hoppers per slice by the slices in each stage.

## Open questions for Jeffrey

- [ ] Item groups: is the [recommended group list](storage-layout.md#2-item-grouping-for-the-chest-walls) right, or finer/coarser?
- [x] **Golem role:** showpiece gallery at the front; hoppers do the main sorting (decided 2026-10-07).
- [ ] Golem gallery set: potions + tipped arrows, or something else?
- [x] Which edition? **Bedrock** (26.50). Golems can tell potion/arrow/stew types apart, and designs must be Bedrock-compatible.
- [x] **Garbage furnace:** lava (decided 2026-10-07).
- [ ] What counts as junk for the disposal (e.g. extra cobble, dirt, rotten flesh)?
- [ ] Should true overflow (unsorted leftovers) go to the disposal once the overflow chest fills, or stop and wait for me?
- [ ] Where does the storage hall go near the home base? (The architecture is Jeffrey's design; it just has to fit the [adjacency rules](storage-layout.md#1-functional-grouping).)
- [ ] Wax everything, or let some golems oxidize on purpose for looks and scrape them?
- [ ] Which farm outputs get hopper sorters first?
- [ ] Is anyone else on the server sharing this storage?

## Done when

- [ ] Dumping inventory into the input barrels by the door gets everything sorted by the hopper chest hall without me touching it
- [ ] The chest walls are labeled and grouped per [storage-layout.md](storage-layout.md#2-item-grouping-for-the-chest-walls), with room to grow
- [ ] The golem gallery runs at the front of the hall: waxed golems visibly sorting into display chests behind glass
- [ ] Every golem and copper chest is waxed (or on a scraping schedule)
- [ ] Auto furnace, shulker box unloader, and garbage disposal are all running off the sorter
- [ ] Every redstone build in the system is a Bedrock-tested design
- [ ] No empty or unseeded chests in any golem's range, and no hopper drains a golem display chest
- [ ] The machine side (smelter, overflow, lava) is kept away from wood and the showpiece areas, and the hall runs without noticeable lag

## Notes

_Golem counts, chest layouts, what broke, and what worked go here._
