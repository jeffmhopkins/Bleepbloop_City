# Lore: the Builders Before and the eye that stayed up

**Status:** 💭 Brainstorm. **Everything on this page is a proposal, not canon.** Pick what you like, cross out what you don't, and the picks move to [Canon so far](#canon-so-far) at the bottom.
**Why it exists:** to give the [in-game chat assistant](../plans/chat-assistant.md) a place in the world, so that `/ask` feels like part of the story and not a bolted-on bot.
**Ground rules:** everything is tied to real Bedrock 26.50 content (mechanics checked on [minecraft.wiki](https://minecraft.wiki)). The satellite is a made thing in orbit, nothing more mystical than that. Nothing here sets building shapes or sizes; where a build is mentioned, it's only *what it means*, never what it looks like.

## Core premise

Long before the first villager planted wheat, a people we call **the Builders Before** wired the whole world together. They ran copper through the hills, poured power into the rock, and kept their memories in crystal. Then they were gone. What's left of them is in the ground: every ore vein you mine is a piece of their old machine, broken down and half-reclaimed by stone.

One thing of theirs still works. High above the world, past where any ghast can fly, their **satellite** is still in orbit. It's patient and a little damaged, and it's been waiting a very long time for someone to talk to it. That's who answers when you type `/ask`.

**Why they vanished** is left open on purpose. Pick one, mix two, or let the satellite refuse to say until much later:

- **They left through the End.** The End cities are their last colony, empty now except for the shulkers they left on guard. The elytra hanging in the end ships is their flight tech, abandoned on the way out.
- **The sculk took them.** They dug too deep, and what they found under the deepslate spread. The ancient cities are where they made their last stand. The warden is what they left on guard, or what they turned into.
- **They burned out in the Nether.** Their forges were down there, and ancient debris is all that's left of them. The piglins hoard their gold without knowing what it was for.
- **They became the villagers.** They didn't die out, they forgot. Villagers still trade in emeralds and still build iron golems without knowing why.
- **Even the satellite doesn't know.** That part of its memory is sealed (see [Unsealing](#unsealing-the-archive)), and opening it is the very last step.

**Name options for the civilization** (pick one):

| Name | Feel |
| --- | --- |
| **The Builders Before** | Plain and humble; it fits a world about building |
| **The Firstwrights** | Older and more like a myth; "wright" is an old word for maker |
| **The Old Makers** | What villagers might call them around a campfire |

## Ores as remnants

One idea per ore. Each one leans on something the ore actually does in the game.

| Ore | What it was to the Builders |
| --- | --- |
| **Copper** | Their wiring and conduits. Oxidizing green is the world slowly reclaiming it, and big copper veins in granite are old cable runs. |
| **Iron** | Their structure. Big iron veins in tuff are buried girders, and tuff is the same stone the trial chambers are built from. |
| **Gold** | Their finest contacts and connectors. Piglins hoard it in the Nether because they remember it mattered, not why. |
| **Redstone** | Their power. It still holds a faint charge, which is why the ore lights up when you touch it or walk on it. |
| **Lapis** | Their ink. The enchanting table's runes are the Standard Galactic Alphabet, and lapis lets you read them, so enchanting is reading Builder script. |
| **Emerald** | Their tokens or keys. It's found only in mountains, and villagers still trade in it without knowing why it's worth anything. |
| **Diamond** | Memory crystals. They sit deepest because that's where the archive was kept; deep fossils (below Y=-8) are laced with diamond ore. |
| **Amethyst** | Resonance and signal. A block of amethyst next to a sculk sensor re-sends any vibration it hears, like a relay, and a spyglass needs an amethyst shard. |
| **Nether quartz** | Their timing and sensing parts. That's why it goes into comparators, observers and the daylight detector. |
| **Ancient debris / netherite** | Their alloy, buried in the Nether. It shrugs off blasts, and netherite gear floats in lava and won't burn, because it was made to survive the forge. |
| **Coal** | Their spent fuel. Fossils above Y=0 are laced with coal ore, a hint that something was here even before them. |

## Their ruins, as real structures

Every one of these is a real Bedrock structure you'll run into anyway. The lore just tells you whose it was.

| Structure | What it was | Fits because |
| --- | --- | --- |
| **Trial chambers** | Proving halls. The Builders tested whoever would inherit their tech here, and the vaults still only open for someone who earns a trial key. | They're built almost entirely from **copper and tuff**, the two Builder materials, and they're the only place breezes spawn. Cartographers sell trial chamber maps, as if the villagers remember where they are. |
| **Ancient cities** | Their deepest archive, or the place they made their last stand against the sculk. The warden is the archive's guard. | At the city's center is a huge frame shaped like a portal, made of reinforced deepslate you can't mine, and **it does nothing**. That's the strongest mystery hook in the game. **Echo shards** are only found here, and they make the recovery compass. |
| **Trail ruins** | A Builder road town, buried and half-forgotten. Brushing suspicious gravel is careful excavation. | Rare trims found here are the **Wayfinder, Raiser, Shaper and Host**, which read like old guild marks or ranks. Pottery sherds can be their picture-writing. |
| **Strongholds** | A gate station. The libraries were records, and the End portal was the way out. | An eye of ender drifts toward the stronghold as though it's following an old signal, and the portal room is the one place the old gate still works. |
| **End cities** | Their last colony, empty now except for the shulkers left on guard. | The **elytra** in end ships is the closest thing to Builder flight that survives. That makes a nice bridge to the [flying machine](../plans/flying-machine.md) goal. |

**Not Builder-made (suggested):** abandoned camps (new in 26.50) are recent travelers' tents. When a camp has an oxidized copper golem statue, those travelers found it and hauled it around. Villages, outposts and mansions belong to the people who came after.

## The satellite

### Talking to it

- You call it with **`/ask`**, like `/ask "where is the nearest pig"` (or plain `/ask` for a text box). It's a private line: the answer reaches **only the person who asked**, so in-world it **whispers**.
- While the LLM works, the plan sends a private "Thinking…" line. That could be flavored as something like *"The sky is listening…"* (proposal; the text is a pack setting).
- **`/bb:find`**, the no-LLM fallback, is the bare signal: when the satellite's voice is quiet (the AI server is down), its raw beacon still answers simple questions.

### Three ways it knows the world

These are the real limits dressed as lore. The satellite knows the world in three different ways, and each one matches how the tools actually work.

**1. Live sight: only near living souls.** It sees **through** living players, or wherever something keeps the land awake. In game terms, that's loaded chunks: about 64 blocks around each online player, plus any ticking areas. So:

- "Nearest pig" really means *the nearest pig any soul is near.* Outside that, it honestly answers that it can't see.
- Because it sees through people and not from the sky, it works in the **Nether and the End** too, wherever someone is standing. (Compasses spin there; the satellite doesn't.)
- **Ticking areas** (like the iron farm's) become **anchors**: places where the land is kept awake, so the satellite can always see them.

**2. The world as it was made: the seed.** This is its oldest memory, the Builders' original plan of the land.
- It can find a cherry grove far away, because the biome tool reads the seed.
- It can point to where **Builder ruins and villages were laid down**, even in land nobody has walked: trial chambers, ancient cities, trail ruins, monuments, villages and more.
- Some of that memory is blurred. It can't place strongholds, Nether fortresses, bastions or End cities with confidence; those are the structures seed prediction gets wrong on Bedrock. So it might say *"my oldest map is torn there"*, until someone walks near one and it remembers it (way 3).
- It remembers the world *as it was made*, so anything built, burned or failed to form since won't show. That matches the real tools.

**3. What it has seen: the saved world.** Every place a soul has walked, the satellite remembers. That's the saved world on the server.
- This is where **ore-sight** comes from. It can name the nearest diamond (or any ore) **in explored land**, and it can confirm that a predicted ruin really stands there.
- Its memory runs a little behind (the snapshots are minutes old), so it might say *"as of a few minutes ago."*
- **Unwalked land keeps its ores hidden.** The Builders' plan says where the ruins were built, but not where every crystal lies. To find diamonds there, someone has to go near first. (Matches the real limit: individual ores can't be predicted from the seed on Bedrock.)

**It answers its Keeper fully.** To you (the owner) it answers everything. For other travelers, it **won't reveal a soul without consent** unless you decide otherwise; that's the still-open policy for other players.

### Coordinates: the Grid

The server keeps coordinates off, but **your** answers include exact coordinates from day one (decided: you're the owner, no restrictions). In-world, that's the satellite's old **grid**, its GPS, answering its Keeper.

- **The Grid unsealing** can still be a story beat: the moment the grid opens *for everyone*, if you ever give other players coordinates or turn on the game's own coordinates.
- **Milestone ideas for that beat** (proposals): bring back an echo shard from an ancient city, open a vault in a trial chamber, or finish the [local-area map](../plans/phase-4-the-base.md#7-local-area-map) so the satellite has something to calibrate against.

### Unsealing the archive

In the story, the satellite's features come back in stages, as it unseals more of its memory. Each stage maps to a step in the [chat-assistant build steps](../plans/chat-assistant.md#build-steps-in-order), so the lore rolls out at the same pace as the code.

> **The seals are pure flavor.** They never gate what you can ask. Once a tool is built, you can use it right away, in any order, with no milestones, quests or unlocks. The seals only give the build order a story.

| Seal | In-world | Build step |
| --- | --- | --- |
| **First Seal: the Eye** | It wakes up and can see living creatures near you. | Step 1 MVP: `find_nearest_entity`, distance + direction |
| **The Bare Signal** | Even when its voice is silent, the beacon answers. | Step 2: `/bb:find`, no LLM |
| **Second Seal: Land and Sky** | It reads the ground and weather around you, remembers where you sleep, and recalls the world's first map. | Step 3: `count_entities`, `time_and_weather`, `inventory_count`, `my_spawn_point`, `biome_here`, `find_nearest_block`, `locate_biome` |
| **Third Seal: Names** | It learns the names you give places, so it can say "toward the village." | Step 4: landmarks |
| **The Grid** | GPS: exact positions (see above). Speaking aloud in chat with `!ask` fits here too. | Step 1 for you (`coords` mode); Step 5: `!ask` prefix, coordinates for others if you allow it |
| **Fourth Seal: Memory** | It starts remembering every place a soul has walked. | Step 6: world snapshot pipeline + index |
| **Fifth Seal: Deep Sight** (ore-sight) | It looks into the stone of explored land and names the nearest diamond, iron, or ancient debris. | Step 7: `find_nearest_ore` |
| **Sixth Seal: The Old Map** | It recalls where the Builders laid down their ruins, even in unwalked land, and says whether it has seen them or only remembers the plan. | Step 8: `find_structure` (seed prediction, confirmed against the saved world) |
| **A Body** (someday) | It sends something down to walk beside you. | The companion bot in the [Live API](../plans/live-api.md) plan |
| **The Last Seal** | What happened to the Builders. | Story only; open whenever you like |

**Satellite name options** (pick one or none): *the Eye*, *the High Archive*, *the Sentinel*, or a gamertag-style name for the bot such as **Orbit** or **Relay**.

## Tie-ins to the existing plans

- **Copper golems are Builder helpers.** The [golem gallery](../plans/storage-and-sorting.md) under the storage hall dome becomes a place where the Builders' little workers sort again. Real mechanics back this up:
  - Fully oxidized golems turn into **statues**, which is the helpers going dormant.
  - Scraping a statue with an axe, or a **lightning strike**, removes oxidation, so the sky literally wakes them.
  - Waxing with honeycomb keeps them from ever going dormant again.
  - A statue found in an abandoned camp is a Builder helper someone carried off.
- **Compasses point at the old beacon.** A plain compass points to world spawn, and your home base is going near spawn. So the lore can say the Builders' ground beacon was here, and Bleepbloop City is built on their first site.
  - A **lodestone** retunes a compass to a new point, like setting up a relay.
  - A **recovery compass** (eight echo shards around a compass) points to where you last died: *the satellite remembers where you fell.*
- **The cartography table translates its data.** A locator map needs a compass, so every locator map is the satellite's view printed on paper. The [local-area map](../plans/phase-4-the-base.md#7-local-area-map) becomes the first real survey, and a cartographer villager selling explorer maps is a villager who still keeps scraps of the satellite's charts.
- **Your copper castle towers could be relays** (just a suggestion; no shapes implied). Lightning rods are copper, and lightning strikes clean the oxidation off them and off the copper around them. A tower that attracts sky-fire fits a satellite relay. The copper aging green on your [towers](../plans/building-style.md#inspiration) is the same reclamation as the copper in the ground.
- **The spyglass is the one Builder instrument you can still make:** an amethyst shard and two copper ingots, signal and wiring together.
- **Amethyst and sculk are the old network.** Sculk sensors hear vibrations and amethyst blocks pass them along. If you ever build wireless redstone with it, it can be "rewiring the Builders' relays."

## Open questions for Jeffrey

- [ ] **What happened to the Builders?** The End, the sculk, the Nether, becoming villagers, or sealed until the end? (See [Core premise](#core-premise).)
- [ ] **Is the satellite friendly?** Options: a loyal servant waiting for the Builders' heirs; a neutral archivist that just answers; or something slowly waking with its own agenda. Why its oldest map is torn exactly where the strongholds and Nether forts should be could be a clue.
- [ ] **Villager connection:** are villagers the Builders' descendants who forgot, or just later settlers? Are illagers a group that rejected the satellite?
- [ ] **Names:** Builders Before, Firstwrights or Old Makers? And does the satellite get a name, or just "the satellite"?
- [ ] **The Grid for everyone:** you already get coordinates. Does anyone else ever get them (the open other-player policy in the [plan](../plans/chat-assistant.md#access-policy)), and if so, is a milestone the story beat for it?
- [ ] **How much in-game?** Lore only in this file, or also in-world (signed books in a lectern, item-frame labels, the satellite's own replies in character)?

## Canon so far

Nothing is canon yet. As Jeffrey picks ideas, list them here with the date.

- **2026-10-07:** Chosen direction: an ancient vanished civilization, ores as their remnants, and the AI as their satellite still in orbit.
