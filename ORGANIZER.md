# ORGANIZER: rules for the Project Organizer (Opus, project root)

There is no CLAUDE.md at the root: course sessions would load it. Start every Organizer session with:
1. Read this file and ROADMAP.md.
2. `node engine/status.js` and `grep -n "\- \[ \]" courses/*/REQUESTS.md` (open requests).
3. Do what the user asks; with no task, take the next ROADMAP.md step.

## Roles

| Role | Model | Works in | Does | Owns |
|---|---|---|---|---|
| Organizer | Opus | project root | engine, design, kits, assembly, git, answers REQUESTS.md | `engine/`, `core/`, `FACTS.md`, root docs, `.github/` |
| Specialist | Opus | `courses/<c>` | LEAD (plan + gold chapter), REVIEW (every 3 packages), REVIEW FINAL | `COURSE.md`, `course.json`, `FACTS.md`, `packages/` |
| Writer | Sonnet | `courses/<c>` | WRITE one package (2–3 chapters, checks, widgets); FIX | `chapters/`, `checks/`, `widgets/` |
| Reader | Sonnet | `courses/<c>` | READER: 6–8 chapters per batch as a beginner; files `(reader)` items | `READER.md` |

## Rules

- Course sessions and agents read only their own course folder and never run git.
- The Organizer edits a course's files only to answer a request, to fix a build error, or at assembly, and records
  it in that course's REQUESTS.md (answer under the line, tick it).
- The design ("marked script") is frozen: change it only when the user asks.
- After any change to `engine/`, kit sources, templates or a `course.json`: `node engine/sync.js`.
- Commit each finished step with a clear message, then `git push`. Pushing to `main` publishes the site.
- Docs and memory hold rules and current state only, as short lists. History lives in git commits.
  ROADMAP.md "Now" is the only status record.
- Exam facts are verified against the syllabus and a real recent question paper (what each paper prints and allows).
- Token use: a fresh Organizer chat per course run; agents bundle tool calls; the gold chapter and chapter depth are
  never cut to save tokens.
- User decisions: chapters stay long and comprehensive; Writers run at high effort and read the whole gold chapter;
  every course plan includes paper guides, mixed practice and one mock per written paper; no in-site flashcards
  (`:::links` send students to verified external sites); the user tests with a student only after the whole project.

## Building a course

- **Classic method** (default): the user runs one chat per step in `courses/<c>`, with PROMPTS.md.
- **Agent method** (only when the user asks): the Organizer runs the steps as agents, following AGENT-RUN.md.
- Cycle: LEAD → Writers claim packages → REVIEW every 3 packages → FIX → READER batches → FIX → REVIEW FINAL.

## Assembly session

1. `node engine/status.js`; answer open REQUESTS.md lines.
2. `node engine/check.js --py` and `node engine/build.js --strict`; `node courses/<c>/kit/zta.js phone` for each
   changed course. Fix engine problems; send course problems back through REVIEW.md or REQUESTS.md.
3. Spot-check the site ("site" launch config): a new chapter per course, a widget, dark mode, phone width, search.
4. Update ROADMAP.md "Now", commit, push.

## Environment (Windows PC)

- Python is `py` (`python` is the Windows Store alias). `engine/util.js` `runPython` tries py, python3, python and
  sets PYTHONUTF8 (the console code page cannot print − or ²).
- Edit LaTeX-heavy text with Write/Edit, never shell heredocs or sed (they eat backslashes).
- The browser pane cannot open `file://` pages: use the "site" launch config (port 5100) or `<c>-preview`
  (5101–5111). When the app window is hidden the pane cannot draw: use `kit/zta.js shot`.
- git: local user.name/email, `core.autocrlf false`. Remote `origin` is the public GitHub repository.

Engine reference: [engine/README.md](engine/README.md).
