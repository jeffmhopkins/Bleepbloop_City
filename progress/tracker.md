# Progress tracker

**This is the one status file for the repo.** Phase status, the first-session checklist, big-goal and building-goal status, and milestones live here only; the README, the master plan, and the phase files link here instead of copying it. Update it when a phase starts or finishes or a checklist item is reached.

**Next sessions:** [session plan for Sessions 2–6](session-plan.md) (Session 2 played 2026-10-07; Session 3 is next). It's a plan only: boxes here get ticked when Jeffrey reports them, not from the plan.

**Status key:** ⬜ Not started · 🟨 In progress · ✅ Done · ⏸️ On hold

| Phase | Status | Started | Finished | Notes |
| --- | --- | --- | --- | --- |
| [1 — First night](../plans/phase-1-first-night.md) | ✅ Done | 2026-10-06 | 2026-10-07 | Bed, chest, stone tools (Session 1); torches and a full food stack (Session 2) |
| [2 — Starter outpost](../plans/phase-2-starter-outpost.md) | 🟨 In progress | 2026-10-06 | | Crafting table, furnace, ~15 wheat by water, pen built (no cows yet). Second chest and door unconfirmed; no iron yet |
| [3 — Pick the real site](../plans/phase-3-pick-the-site.md) | ⬜ Not started | | | |
| [4 — The base that lasts](../plans/phase-4-the-base.md) | ⬜ Not started | | | |
| [5 — Infrastructure](../plans/phase-5-infrastructure.md) | ⬜ Not started | | | |

## First-session checklist

- [x] Bed set (2026-10-06)
- [x] Food farm planted (2026-10-07: ~15 starter wheat by water)
- [ ] Iron tools
- [ ] Site chosen
- [ ] Storage started (one chest so far)

## Big goals

| Goal | Status | Started | Finished | Notes |
| --- | --- | --- | --- | --- |
| [Automated item sorter (hopper chest hall + golem gallery)](../plans/storage-and-sorting.md) | ⬜ Not started | | | |
| [Happy ghast](../plans/happy-ghast.md) | ⬜ Not started | | | Phase 5; dried ghast is a Session 6 stretch |
| [Flying machine](../plans/flying-machine.md) | ⬜ Not started | | | End game |
| [Server migration to the AI server](../plans/server-migration.md) | ⬜ Not started | | | Container + backups + snapshots |
| [Live API (tokenized connection)](../plans/live-api.md) | ⬜ Not started | | | Needs migration first |
| [In-game chat assistant](../plans/chat-assistant.md) | ⬜ Not started | | | Needs migration first; shares the Live API pack |

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
