# Progress tracker

**This is the one status file for the repo.** Phase status, the first-session checklist, big-goal and building-goal status, and milestones live here only; the README, the master plan, and the phase files link here instead of copying it. Update it when a phase starts or finishes or a checklist item is reached.

**Next sessions:** [session plan for Sessions 2–6](session-plan.md) (Session 2 played 2026-10-07; Session 3 reported 2026-10-10; Session 4 is next). It's a plan only: boxes here get ticked when Jeffrey reports them, not from the plan.

**Status key:** ⬜ Not started · 🟨 In progress · ✅ Done · ⏸️ On hold

| Phase | Status | Started | Finished | Notes |
| --- | --- | --- | --- | --- |
| [1 — First night](../plans/phase-1-first-night.md) | ✅ Done | 2026-10-06 | 2026-10-07 | Bed, chest, stone tools (Session 1); torches and a full food stack (Session 2) |
| [2 — Starter outpost](../plans/phase-2-starter-outpost.md) | 🟨 In progress | 2026-10-06 | | Initial hut done: crafting table, furnace, smoker, two double chests (reported 2026-10-10). ~15 wheat by water, still not mature; pen built, no cows yet. Some iron from caves: bucket (filled with water) and shield made; full copper armor; coal and copper stocked (Session 3). Iron pickaxe, iron tools and iron armor not reported; door, farm light and fence unconfirmed |
| [3 — Pick the real site](../plans/phase-3-pick-the-site.md) | ⬜ Not started | | | |
| [4 — The base that lasts](../plans/phase-4-the-base.md) | ⬜ Not started | | | |
| [5 — Infrastructure](../plans/phase-5-infrastructure.md) | ⬜ Not started | | | |

## First-session checklist

- [x] Bed set (2026-10-06)
- [x] Food farm planted (2026-10-07: ~15 starter wheat by water)
- [ ] Iron tools
- [ ] Site chosen
- [ ] Storage started (two double chests in the hut, reported 2026-10-10; group chests not yet)

## Big goals

| Goal | Status | Started | Finished | Notes |
| --- | --- | --- | --- | --- |
| [Automated item sorter (hopper chest hall + golem gallery)](../plans/storage-and-sorting.md) | ⬜ Not started | | | Layout ([storage-layout.md](../plans/storage-layout.md)) is a draft recommendation, not built |
| [Happy ghast](../plans/happy-ghast.md) | ⬜ Not started | | | Phase 5; dried ghast is a Session 6 stretch |
| [Flying machine](../plans/flying-machine.md) | ⬜ Not started | | | End game |
| [Server migration to the AI server](../plans/server-migration.md) | 🟨 In progress | 2026-10-10 | | Built in jbrain2 (Jeffrey's AI box project). Stage progress in [Server migration stages](#server-migration-stages) below |
| [Live API (tokenized connection)](../plans/live-api.md) | ⬜ Not started | | | Needs migration first. jbrain2 already records join/leave events and play time, and has proved a stable-API script bridge (no Beta APIs) |
| [In-game chat assistant](../plans/chat-assistant.md) | ⬜ Not started | | | Needs migration first. jbrain2 plans the same feature as "Dave" (`/jb:dave`, its waves M5–M6, not built). Its owner-side PWA persona Minecraft_Dave (per-player goals, progress log, line-level memory, console `/locate`) merged in PR #1603 (2026-10-10); that is not the in-game assistant. PR #1613 (2026-10-10) gave it every raw server tool: reads run at once, changes and other console commands wait for Jeffrey's approval. PR #1615 (2026-10-10) added nearest-block search from the saved world files (diamonds confirmed by the game on jbrain2's test world) and per-player tricorder waypoints. PR #1619 (2026-10-10) built the in-game `/jb:dave` on its test setup: players ask in game, get private `tellraw` replies, can save, list and remove named places, and get read-only world searches; the web, console and server actions are held back. Not yet tried by a real player or with a live AI turn. 2026-10-11: Dave's story is canon in [lore](../notes/lore.md#dave-the-crew-and-the-tricorder): he's the satellite's AI, you're the crew, and the Tricorder is how he reaches you. That page is the source of truth; jbrain2 builds the welcome and Tricorder rules from it (not built yet). 2026-10-11: access policy gains its one lore exception, no Tricorder, no Dave (your own Tricorder only). 2026-10-11: jbrain2 PR #1633 (docs only) brought its plan in line with the lore: a Tricorder works only for its owner, it's locked to the inventory and re-beamed on every join or respawn if missing, and transport on request (own Tricorder plus one Power Pack) is Dave's one acting tool, endgame and not in the first build. Still plan only, not built. 2026-10-11: jbrain2 PR #1634 made saved places follow the lore: a place is saved only where the player stands (in game, or from the web while they're online with a position under a minute old; typed coordinates are ignored), and transport, once built, goes only to saved places. Transport itself is still not built. 2026-10-11: jbrain2 PR #1649 (merged 2026-10-11) built the Tricorder and Power Pack into every world: the Tricorder is bound to its owner, kept on death and re-beamed on waking, `/jb:dave` answers only through your own Tricorder, and the Power Pack (8 Ender Pearls around 1 Blaze Powder) gives a per-world keep-inventory switch that's off by default. Not yet tried by a real player. 2026-10-11: jbrain2 PR #1650 (merged 2026-10-11) built the deep-scan limit (its M17): in game, `mc_locate`, `mc_nearby` and `mc_find_block` count as deep scans, two per player per Minecraft day (from the world's own day count, so sleeping resets it); repeats within 256 blocks the same day and searches that find nothing are free, and the web chat stays unlimited. Tested on jbrain2's test setup only. 2026-10-11: jbrain2 PR #1651 (merged 2026-10-11) built its M18 and M19: a no-model fast path that answers exact simple asks (go home, save, forget or list places, where am I or another player, scans left, nearest structure or ore, which still uses a deep scan) with the lore's quick-answer lines, and an item guide (Tricorder, Power Pack, keep-on-death) that Dave learns per player as they first get Ender Pearls or a Power Pack. Tested on jbrain2's test setup only; not yet tried by a real player. 2026-10-11: Jeffrey verified the spawn crash site (pod, parachute and mothership) and the Tricorder's world-spawn arrow in game as a player on jbrain2's test world, not the Bleepbloop_City world; see [lore: first look](../notes/lore.md#first-look-test-world-2026-10-11). 2026-10-11: jbrain2 PR #1662 (merged 2026-10-11) built transport on request (its M10): in game, Dave's `mc_transport` takes the asker to one of their own saved places after a Yes/No form showing distance and cost, and spends one Power Pack only if the teleport lands; it refuses at no cost without your own Tricorder, a Power Pack, or a visit to that dimension. A per-world switch, on by default, controls it. Tested on jbrain2's test setup only; its M10 stays open for the Power Pack's lore line and the web toggle. 2026-10-11: jbrain2 PR #1667 (merged 2026-10-11) built wormhole gates (its M12): a Wormhole Seed (crafted with a chorus seed) planted in a diamond-block frame makes a gate that Dave's `mc_wormhole_aim` opens one-way to one of the player's saved places; anyone can walk through, re-aiming costs one Power Pack within 4 blocks of the gate, and mining the gate breaks it and loses the seed. Dave's aim tool and wormhole guide stay hidden until the player unlocks the seed. Tested on jbrain2's test setup only. 2026-10-12: jbrain2 PR #1671 (merged 2026-10-12) added shorter commands: `/dave`, `/d` and `/ai` all reach Dave (`/jb:dave` still works), and Dave's player-facing text now says `/dave`; lore already uses `/dave`. |

### Server migration stages

From jbrain2's merged Minecraft PRs #1593–#1596 and #1598 (read 2026-10-10). Details and the step-by-step mapping are in [server migration: already built in jbrain2](../plans/server-migration.md#already-built-in-jbrain2-read-2026-10-10).

| Stage | Status | Notes |
| --- | --- | --- |
| 0 — Migrate | 🟨 In progress | BDS 1.26.52.3 runs in jbrain2's `minecraft` container on the AI box, with a **fresh test world**. Internet play was opened by hand on 2026-10-11 (jbrain2 PR #1652): the router forwards TCP+UDP 19132 and UDP 19140–19144, and a phone on mobile data joined. World import, world slots, game rules and the allowlist are built in the PWA. The real Bleepbloop City world isn't imported yet, the allowlist defaults to off, and joining from Windows and the Xbox is still to be tested |
| 1 — Automated backups | 🟨 In progress | On-demand backups, automatic ones before update/load/import/reset/restore, 20 kept per world, pin, restore and download are built. **No schedule and no off-box copy**: backups stay in the same volume, which is left out of the box backups. No test restore of the real world yet |
| 2 — Snapshot analysis | ⬜ Not started | jbrain2's world index (M4) is planned, not built. Its map viewer (M8) wave 1 merged in PR #1623 (2026-10-11) on its test setup: a live web map (all three dimensions, tap for biome and X Z, pins, player and structure overlays) plus a saved structure sweep that runs the server's own `locate structure` on a 512-block grid and stores results outside the world folder. Wave 3 merged in PR #1630 (2026-10-11): Minecraft_Dave can show a map card in the jbrain2 web chat (focused on a death, player, saved place, structure or spot, with Copy X Z); it is web-only, not in game. Not yet run on our world |
| 3 — Live API | ⬜ Not started | See the Live API row above |

## Building goals

See [plans/building-goals.md](../plans/building-goals.md).

| # | Goal | Status | Started | Finished | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | [Thatch-roof starter cottage](../plans/building-goals.md#1-thatch-roof-starter-cottage) | ⬜ Not started | | | |
| 2 | [Copper storage hall](../plans/building-goals.md#2-copper-storage-hall) | ⬜ Not started | | | |
| 3 | [Spawn town square](../plans/building-goals.md#3-spawn-town-square) | ⬜ Not started | | | |
| 4 | [Village glow-up](../plans/building-goals.md#4-village-glow-up) | ⬜ Not started | | | |
| 5 | [Gatehouse and wall](../plans/building-goals.md#5-gatehouse-and-wall) | ⬜ Not started | | | |
| 6 | [Farm district](../plans/building-goals.md#6-farm-district) | ⬜ Not started | | | |
| 7 | [Nether portal shrine](../plans/building-goals.md#7-nether-portal-shrine) | ⬜ Not started | | | |
| 8 | [Lighthouse or watchtower](../plans/building-goals.md#8-lighthouse-or-watchtower) | ⬜ Not started | | | |
| 9 | [Mine entrance building](../plans/building-goals.md#9-mine-entrance-building) | ⬜ Not started | | | |

## Achieved

Only things that actually happened, with the date Jeffrey reported them. Add a row when a milestone below is reached (or anything else worth remembering).

| Date | Milestone |
| --- | --- |
| 2026-10-06 | Server started; first bed made, spawn set (Session 1) |
| 2026-10-07 | Phase 1 done: torches and a full food stack; first wheat planted and animal pen built (Session 2) |
| 2026-10-10 | First iron from the caves: bucket and shield; full copper armor; initial hut done with a smoker and two double chests (Session 3, reported 2026-10-10) |

## Planned milestones

Not reached yet. When one is, move it up to [Achieved](#achieved) with its date. Wording rule: **stages** are for the storage sorter and the server; **phases** are for the game.

**Storage sorter** ([growth stages](../plans/storage-layout.md#4-growth-stages), [one table per stage](../plans/storage-stages.md)):

- Stage 0: manual chests by group + one test hopper slice
- Stage 1: front-left wing (stone family, 13 slices) + router, input barrels, intake and overflow in Machinery; whole U trunk laid
- Stage 2: front-right wing (farming & food + brewing, 22 slices) + smokers running
- Stage 3: mid-left (ores, copper, redstone) + mid-right (wood, build blocks) wings, 30 slices + blast furnaces + lava (junk list) running
- Stage 4: golem gallery showpiece running behind glass (Dome)
- Stage 5: back-left (decor colors, Nether, End) + back-right (mob drops, tools/armor/enchanting, transport) wings, 22 slices + shulker unloader feeding the router
- Stage 5 expansion: ★ items grown into each wing's reserved room; hall dressed as the Copper storage hall (ongoing)
- Add-on: auto furnace (blast furnaces + smokers) running off the sorter
- Add-on: lava garbage disposal taking junk + overflow
- Add-on: shulker box auto unloader feeding the sorter

**Server** ([server migration](../plans/server-migration.md)):

- Stage 0: world migrated to the Linux container; Windows copy kept as rollback
- Stage 1: automated backups running; test restore done
- Stage 2: first snapshot analyzed (map + tracker update)
- Stage 3: live API events flowing; read access via token
