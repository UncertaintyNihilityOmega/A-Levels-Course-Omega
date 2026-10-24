# Zero to A*

A free, interactive A Level guide that takes a complete beginner to A* exam standard. Every course has
step-by-step chapters, worked examples marked the way examiners mark, practice questions with mark schemes,
interactive widgets, paper guides and full mock papers, plus a study roadmap and tools.

**Open it:** https://uncertaintynihilityomega.github.io/A-Levels-Course-Omega/

**Offline:** download the repository, run `npm install` and `node engine/build.js`, then open `site/index.html`.

## Courses

| Course | Syllabus | State |
|---|---|---|
| Mathematics | Cambridge International 9709 | complete (Further Mathematics planned) |
| Physics | Cambridge International 9702 | complete |
| Chemistry | Cambridge International 9701 | complete |
| Biology | Cambridge International 9700 | planned |
| Computer Science | Cambridge International 9618 | planned |
| Engineering | Maths and Physics routes (no single syllabus) | planned |
| Economics | Cambridge International 9708 | planned |
| Business | Cambridge International 9609 | planned |
| Accounting | Cambridge International 9706 | planned |
| Psychology | Cambridge International 9990 | planned |
| Other subjects | short guides to other A Levels | planned |

Chapter counts per course: `node engine/status.js`. Build queue: [ROADMAP.md](ROADMAP.md).

## Build

Requirements: Node 18+ and Python 3 (standard library only). Optional: `pip install fonttools brotli` makes the
embedded maths font smaller.

| Command | Does |
|---|---|
| `npm install` | installs the build dependencies (once) |
| `node engine/build.js [--strict]` | builds `site/` (`--strict`: exit 1 on any error) |
| `node engine/check.js [course …] [--py]` | lints every chapter (marks, links, structure); `--py` runs every number check |
| `node engine/status.js` | one line per course: chapters, packages, reviews, next step |
| `node engine/sync.js` | regenerates each course's kit, CLAUDE.md and LINKS.md |
| `node engine/serve.js` | serves `site/` at http://localhost:5100 |

Every push to `main` runs the checks, builds the site and publishes it to GitHub Pages
(`.github/workflows/pages.yml`).

## Repository

| Path | What |
|---|---|
| `core/` | guide-wide pages (Home, Start Here, About the subjects, Roadmap, Tools, Practice) and `core.json` (sidebar order) |
| `courses/<c>/` | one course: `course.json` (plan), `COURSE.md` (rules), `FACTS.md` (verified facts), `chapters/`, `checks/` (Python number checks), `widgets/`, `packages/` (writing briefs) |
| `engine/` | build, checks, page template, styles, widgets runtime, course kit sources ([engine/README.md](engine/README.md)) |
| `FACTS.md` | exam facts shared by every course |
| `ORGANIZER.md`, `AGENT-RUN.md`, `PROMPTS.md` | how the guide is written and maintained |
| `archive/` | superseded docs and builds (history only) |

## How it is made

The guide is written by Claude in four roles: an Organizer (engine, design, assembly), and per course a
Specialist (plans and reviews), Writers (write chapters) and a Reader (reads the course as a beginner and
reports where a student would get lost). Every number in a chapter is recomputed by a Python check, every
chapter is linted for marks and links, and every page is tested at phone width. Exam facts are checked against
the board's syllabus and real question papers.

## Licence

[The Unlicense](LICENSE): public domain. The embedded fonts are under the SIL Open Font License
(`engine/fonts/`).
