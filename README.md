# Bleepbloop City

Minecraft server planning: plans, progress, and notes for building Bleepbloop City from first night to a base that lasts.

**Server edition:** Bedrock.
**Game version:** Wilderness Bound (Bedrock 26.50; Java 26.3 is the matching Java release). Straw beds, abandoned camps, and copper gear all matter in the first week. Back after a break? See [what's new since late 2024](notes/whats-new.md).

> A good base is a logistics problem first and a building project second. Get safe, get food, get a bed, then pick a site you will still want in a month.

## Status

**Where things stand lives in one place: [progress/tracker.md](progress/tracker.md).** Phase status, the first-session checklist, big-goal status, and achieved milestones are all there, and nowhere else.

- [Session log](progress/session-log.md): what happened each session
- [Session plan](progress/session-plan.md): the next sessions (60–90 minutes each; plan only, nothing checked until reported)

## Big goals

Long-term goals that span several phases. Their status is in the [tracker](progress/tracker.md#big-goals).

| Goal | Plan |
| --- | --- |
| A highly automated item sorter: hopper chest hall doing the sorting, copper golem gallery as the showpiece ([grouping](plans/storage-layout.md), [stages](plans/storage-stages.md)) | [plans/storage-and-sorting.md](plans/storage-and-sorting.md) |
| Nine building goals (grand architecture: mossy timber frames and oxidized copper towers; see [inspiration](plans/building-style.md#inspiration)): thatch cottage, copper storage hall, spawn town square, village glow-up, gatehouse and wall, farm district, Nether portal shrine, lighthouse/watchtower, mine entrance building | [plans/building-goals.md](plans/building-goals.md) |
| A happy ghast: a flying mount for 4 and a stand-on sky platform for the grand builds (from a Nether dried ghast) | [plans/happy-ghast.md](plans/happy-ghast.md) |
| A flying machine (end game) | [plans/flying-machine.md](plans/flying-machine.md) |
| Move the server to the AI server (container, automated backups, snapshot analysis) | [plans/server-migration.md](plans/server-migration.md) |
| Live API: tokenized connection from the server to Grok Bot | [plans/live-api.md](plans/live-api.md) |
| In-game chat assistant: ask "where is the nearest pig" (or the nearest diamond or village) and the local LLM answers privately, using read-only game tools; every player has unrestricted access, coordinates included | [plans/chat-assistant.md](plans/chat-assistant.md) |

## Repo map

| Folder | What's in it |
| --- | --- |
| [`plans/`](plans/) | The [master plan](plans/README.md), one file per phase, plus [building style](plans/building-style.md), [multiplayer server](plans/multiplayer-server.md), and the big goals: [storage and sorting](plans/storage-and-sorting.md) (+ [storage grouping](plans/storage-layout.md) and [stages](plans/storage-stages.md)), [building goals](plans/building-goals.md), [happy ghast](plans/happy-ghast.md), [flying machine](plans/flying-machine.md), [server migration](plans/server-migration.md), [live API](plans/live-api.md), and [chat assistant](plans/chat-assistant.md) |
| [`progress/`](progress/) | [Phase tracker](progress/tracker.md), the [session log](progress/session-log.md), and the [session plan](progress/session-plan.md) for Sessions 2–6 |
| [`notes/`](notes/) | [Coordinates](notes/coordinates.md), [resources and farms](notes/resources-and-farms.md), [ideas](notes/ideas.md), [what's new (2-year catch-up)](notes/whats-new.md), and [lore](notes/lore.md) (brainstorm: the Builders Before and their satellite) |
| [`templates/`](templates/) | Copy-paste templates for a [session log entry](templates/session-log-entry.md) and a [build/project](templates/build-project.md) |
| [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/) | Issue templates for tasks and ideas |

## How to use this repo

1. Work through the phases in order. Tick checkboxes in the phase file as you go.
2. When a phase starts or finishes, or a checklist item or milestone is reached, update [progress/tracker.md](progress/tracker.md). That is the only status file; everything else links to it.
3. After each play session, add an entry to [progress/session-log.md](progress/session-log.md).
4. Write down every important location in [notes/coordinates.md](notes/coordinates.md) the moment you find it.
5. Bigger builds get their own file from [templates/build-project.md](templates/build-project.md), or a GitHub issue.

## License

[MIT](LICENSE), except the two third-party images in [`assets/inspiration/`](assets/inspiration/), which belong to their creators and are not covered by the MIT license (see [CREDITS.md](CREDITS.md)).
