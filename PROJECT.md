# Zero to A*: project overview

An offline, interactive A Level guide that takes a complete beginner to A* exam standard, built from Markdown
chapters into one local website. **Open `site/index.html`** (double-click; keep the `c` folder next to it).
Rebuild it with `node engine/build.js`.

## Who does what
| Role | Model | Chat opened in | Does |
|---|---|---|---|
| Project Organizer | Opus | this folder (the project root) | engine, design, kits, hard problems, assembling and checking the whole site, commits |
| `<Course>` Specialist | Opus | `courses/<c>` | **LEAD**: plans the course, writes the gold chapter. **REVIEW**: after every 2 Writer packages, and a final review |
| `<Course>` Writer | Sonnet | `courses/<c>` | **WRITE**: one package of 2–3 chapters per chat, plus its widgets and number checks; several Writer chats can run at once (each claims a package) |
| `<Course>` Reader | Sonnet | `courses/<c>` | **READER**: after every package is reviewed, reads the course in order as a beginner (6–8 chapters per chat) and files `(reader)` items in REVIEW.md where a student would get lost |

Courses, in build order (re-planned 2026-10-15 to cover each syllabus in full): `math`, `phys`, `chem`, `bio`,
`econ`, `bus`, `acc`, `eng`, `other`. Biology follows Chemistry so it can link chemistry chapters; Economics,
Business and Accounting share topics, so their COURSE.md files say which course owns each one (Economics first).
`eng` has no Cambridge syllabus, so its Specialist plans from the routes listed in its COURSE.md. `other` (summaries
of other A Levels) has a Specialist too since the re-plan.

Each course chat reads only its own folder. Its `CLAUDE.md` is loaded automatically and explains the three
session types; `node kit/zta.js status` tells it what to do next. The copy-paste prompts are in **PROMPTS.md**.

## How to start a course chat (Claude Code tab in the desktop app)
1. New session → choose the folder `A Levels Course\courses\<c>` (not the project root).
2. Pick the model: **Opus** for Specialist sessions, **Sonnet** for Writer sessions.
3. If it offers a worktree, decline it, so the files land in the real folder.
4. Paste the one-line prompt from PROMPTS.md. When the chat reports back, close it: one session = one step.

## Two ways to build a course
Both use the same course kit: `status`, `claim`, `done`, STATUS.md, REVIEW.md and the package notes. So a course
can switch between them at any point. For example, an agent run can stop at the usage limit and classic chats can
carry on the next day, or the other way round.

| | **Classic method** (the default) | **Agent method** (when you have usage to spare) |
|---|---|---|
| Who runs it | You: one chat per step, opened in `courses/<c>` (PROMPTS.md) | One Organizer chat at the root runs the steps as agents: 1 Opus Specialist + up to 2 Sonnet Writers at once |
| Your effort | Open a chat, paste the prompt, close it when it reports; repeat | One prompt; leave it open (overnight is fine) and say "continue" after a usage-limit stop |
| Speed | One package per chat, at your pace | About 3 packages per Pro 5-hour window, around the clock |
| Usage | Spread out; you choose when each step runs | Burns a Pro 5-hour window in about 1–1.5 hours (about 30–45k tokens a minute); best just before a window resets, or when spare usage would otherwise go unused |
| Checks | Writers look at their pages in the browser pane | Writers check headless; the Specialist reviews every figure in the browser; a guard keeps agents inside the one course folder |
| Commits | The Organizer commits at assembly | The Organizer commits each package as it lands |

The agent method's playbook (prompts, loop, recovery after a usage-limit stop, costs) is in **AGENT-RUN.md**. To
start one, see PROMPTS.md.

## Recommended order
1. Organizer O1–O3 (done): restructure, the redesign (approved and frozen) and the hand-off.
2. Mathematics (done, classic method). Physics LEAD and P1–P6 were done by the agent method (2026-10-14).
3. Then run courses one or two at a time, in the build order above, by either method. A Specialist REVIEW follows
   every two packages; when all are reviewed, Reader sessions read the course as a beginner, then FIX and REVIEW FINAL.
   Maths and Physics get their READER pass too (`status` lists it).
4. After a few packages, or when any REQUESTS.md has items, open an Organizer session to assemble: it builds
   and checks the site, answers requests, re-syncs the kits and commits.

## Usage tips
- All chats and agents share one usage pool. Running 1–3 course chats at a time is plenty.
- Measured costs: a Writer package costs about 230–280k tokens, a review 300–380k, and a LEAD about 400k.
- Keep each chat to its one step. A fresh chat is cheaper than a long one (the agent method does the same: one
  new agent per package).

## Map
| Path | What |
|---|---|
| `site/` | the finished guide (generated; not in git) |
| `core/` | Organizer chapters (Home, Start Here, Roadmap, Toolbox, Practice) and `core.json` (sidebar order) |
| `courses/<c>/` | one course: CLAUDE.md, COURSE.md, course.json, FACTS.md, chapters/, checks/, widgets.js, kit/ |
| `engine/` | build.js, check.js, status.js, sync.js, serve.js, lib/site/plot/lint, page template and styles, kit sources |
| `FACTS.md` | verified exam facts shared by every course |
| `ORGANIZER.md` | the Organizer's own procedures |
| `AGENT-RUN.md` | the agent method: how the Organizer runs a course with Specialist and Writer agents |
| `.claude/` | launch configs (site and each course's preview) and the agent guard hook (asleep unless an agent run is on) |
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
