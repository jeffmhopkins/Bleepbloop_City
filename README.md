# Bleepbloop City

Minecraft server planning: plans, progress, and notes for building Bleepbloop City from first night to a base that lasts.

**Server edition:** Bedrock.
**Game version:** Wilderness Bound (Bedrock 26.50; Java 26.3 is the matching Java release). Straw beds, abandoned camps, and copper gear all matter in the first week.

> A good base is a logistics problem first and a building project second. Get safe, get food, get a bed, then pick a site you will still want in a month.

## Status dashboard

**Current phase:** [Phase 1 — First night](plans/phase-1-first-night.md), in progress. Only a full stack of food is left. [Phase 2](plans/phase-2-starter-outpost.md) started early.

**Last session:** [Session 1, 2026-10-06](progress/session-log.md)

| Phase | Status |
| --- | --- |
| [1 — First night](plans/phase-1-first-night.md) | 🟨 In progress |
| [2 — Starter outpost](plans/phase-2-starter-outpost.md) | 🟨 In progress (started early) |
| [3 — Pick the real site](plans/phase-3-pick-the-site.md) | ⬜ Not started |
| [4 — The base that lasts](plans/phase-4-the-base.md) | ⬜ Not started |
| [5 — Infrastructure](plans/phase-5-infrastructure.md) | ⬜ Not started |

Full details and dates live in [progress/tracker.md](progress/tracker.md).

### First-session checklist

Everything else is optional until these five are done.

- [x] Bed set
- [ ] Food farm planted
- [ ] Iron tools
- [ ] Site chosen
- [ ] Storage started (one chest so far)

## Big goals

Long-term goals that span several phases.

| Goal | Plan | Status |
| --- | --- | --- |
| A highly automated item sorter with heavy use of copper golems | [plans/storage-and-sorting.md](plans/storage-and-sorting.md) | ⬜ Not started |
| Nine building goals (optional theme: cozy autumn village): thatch cottage, copper storage hall, spawn town square, village glow-up, gatehouse and wall, farm district, Nether portal shrine, lighthouse/watchtower, mine entrance building | [plans/building-goals.md](plans/building-goals.md) | ⬜ Not started |
| A flying machine (end game) | [plans/flying-machine.md](plans/flying-machine.md) | ⬜ Not started |
| Move the server to the AI server (container, automated backups, snapshot analysis) | [plans/server-migration.md](plans/server-migration.md) | ⬜ Not started |
| Live API: tokenized connection from the server to Grok Bot | [plans/live-api.md](plans/live-api.md) | ⬜ Not started |

## Repo map

| Folder | What's in it |
| --- | --- |
| [`plans/`](plans/) | The [master plan](plans/README.md), one file per phase, plus [building style](plans/building-style.md), [multiplayer server](plans/multiplayer-server.md), and the big goals: [storage and sorting](plans/storage-and-sorting.md), [building goals](plans/building-goals.md), [flying machine](plans/flying-machine.md), [server migration](plans/server-migration.md), and [live API](plans/live-api.md) |
| [`progress/`](progress/) | [Phase tracker](progress/tracker.md) and the [session log](progress/session-log.md) |
| [`notes/`](notes/) | [Coordinates](notes/coordinates.md), [resources and farms](notes/resources-and-farms.md), [ideas](notes/ideas.md), and [version features](notes/version-features.md) |
| [`templates/`](templates/) | Copy-paste templates for a [session log entry](templates/session-log-entry.md) and a [build/project](templates/build-project.md) |
| [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) | Issue templates for tasks and ideas |

## How to use this repo

1. Work through the phases in order. Tick checkboxes in the phase file as you go.
2. When a phase starts or finishes, update its row in [progress/tracker.md](progress/tracker.md) and the dashboard above.
3. After each play session, add an entry to [progress/session-log.md](progress/session-log.md).
4. Write down every important location in [notes/coordinates.md](notes/coordinates.md) the moment you find it.
5. Bigger builds get their own file from [templates/build-project.md](templates/build-project.md), or a GitHub issue.

**Status key:** ⬜ Not started · 🟨 In progress · ✅ Done · ⏸️ On hold
