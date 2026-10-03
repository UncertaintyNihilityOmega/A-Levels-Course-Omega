# Zero to A*: project overview

An offline, interactive A Level guide that takes a complete beginner to A* exam standard, built from Markdown
chapters into one local website. **Open `site/index.html`** (double-click; keep the `c` folder next to it).
Rebuild it with `node engine/build.js`.

## Who does what
| Role | Model | Chat opened in | Does |
|---|---|---|---|
| Project Organizer | Opus | this folder (the project root) | engine, design, kits, hard problems, assembling and checking the whole site, commits |
| `<Course>` Specialist | Opus | `courses/<c>` | **LEAD**: plans the course, writes the gold chapter. **REVIEW**: after every 2 Writer packages, and a final review |
| `<Course>` Writer | Sonnet | `courses/<c>` | **WRITE**: one package of 4–8 chapters per chat, plus that package's widgets and number checks |

Courses: `math`, `phys`, `chem`, `bio`, `eng`, `bus`, `econ`, `acc`, `other`.
`other` has no Specialist: the Organizer planned it and a Writer does it. `eng` has no Cambridge syllabus,
so its Specialist plans from the routes listed in its COURSE.md.

Each course chat reads only its own folder. Its `CLAUDE.md` is loaded automatically and explains the three
session types; `node kit/zta.js status` tells it what to do next. The copy-paste prompts are in **PROMPTS.md**.

## How to start a course chat (Claude Code tab in the desktop app)
1. New session → choose the folder `A Levels Course\courses\<c>` (not the project root).
2. Pick the model: **Opus** for Specialist sessions, **Sonnet** for Writer sessions.
3. If it offers a worktree, decline it, so the files land in the real folder.
4. Paste the one-line prompt from PROMPTS.md. When the chat reports back, close it: one session = one step.

## Recommended order
1. Organizer O2: the redesign pass. Approve the look; after that the format is frozen.
2. **Math Specialist LEAD** first, then Math Writer P1, to calibrate how much usage a package costs.
3. Then run 2–3 courses side by side (for example Physics, Chemistry and Biology LEADs), each followed by
   its Writer packages, with a Specialist REVIEW after every two packages.
4. After a few packages, or when any REQUESTS.md has items, open an Organizer session to assemble:
   it builds and checks the site, answers requests, re-syncs the kits and commits.

## Usage tips
- All chats share one usage pool. Running 1–3 course chats at a time is plenty.
- With no word limits, cost grows with chapter length. Ask the first Math Writer chat for its package's
  cost (the share of your usage window it took) and plan from that.
- Keep each chat to its one step. A fresh chat is cheaper than a long one.

## Map
| Path | What |
|---|---|
| `site/` | the finished guide (generated; not in git) |
| `core/` | Organizer chapters (Home, Start Here, Roadmap, Toolbox, Practice) and `core.json` (sidebar order) |
| `courses/<c>/` | one course: CLAUDE.md, COURSE.md, course.json, FACTS.md, chapters/, checks/, widgets.js, kit/ |
| `engine/` | build.js, check.js, status.js, sync.js, serve.js, lib/site/plot/lint, page template and styles, kit sources |
| `FACTS.md` | verified exam facts shared by every course |
| `ORGANIZER.md` | the Organizer's own procedures |
| `REORG-PLAN.md` | the approved plan this structure comes from |
| `archive/` | the old docs, tools and builds (history only) |

## Commands (project root)
| Command | Does |
|---|---|
| `node engine/build.js` | builds `site/` (`--strict` exits 1 on errors, `--warn` prints warnings) |
| `node engine/check.js [course …] [--py]` | validates everything; checklist detail per course; `--py` runs every number check |
| `node engine/status.js` | one line per course: chapters, packages, reviews, next step |
| `node engine/sync.js` | refreshes every course's kit/, CLAUDE.md and LINKS.md |
| `node engine/serve.js` | serves `site/` at http://localhost:5100 (the "site" launch config) |

Requirements: Node 18+ (`npm install` once at the root), Python via `py`, and `py -m pip install fonttools brotli`
for the small maths font (without it the build embeds the whole font).
