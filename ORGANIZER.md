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
  (`:::links` send students to verified external sites); the user studies the guide themself and sends feedback
  (turn it into REVIEW.md items); testing with real students comes after the whole project.

## Building a course

- **Classic method** (when the user wants to drive a course by hand): one chat per step in `courses/<c>` (PROMPTS.md).
- **Agent method** (the user's default for the roadmap): an app scheduled task (every 2 hours) starts a fresh Organizer
  session that runs the next steps as agents (AGENT-RUN.md "Automatic runs").
- Cycle: LEAD → Writers claim packages → REVIEW every 3 packages → FIX → READER batches → FIX → REVIEW FINAL.

## Assembly session

1. `node engine/status.js`; answer open REQUESTS.md lines.
2. `node engine/check.js --py` and `node engine/build.js --strict`; `node courses/<c>/kit/zta.js phone` for each
   changed course. Fix engine problems; send course problems back through REVIEW.md or REQUESTS.md.
3. Spot-check the site ("site" launch config): a new chapter per course, a widget, dark mode, phone width, search.
4. Update ROADMAP.md "Now", commit, push.

## Environment (Windows PC)

- Python is `py` (`python` is the Windows Store alias). `engine/util.js` `runPython` tries py, python3, python
  (macOS: python3, python) and sets PYTHONUTF8 (the console code page cannot print − or ²).
- The engine and kit also run on macOS (Python and browser paths; see engine/README.md).
- Edit LaTeX-heavy text with Write/Edit, never shell heredocs or sed (they eat backslashes).
- The browser pane cannot open `file://` pages: use the "site" launch config (port 5100) or `<c>-preview`
  (5101–5111). When the app window is hidden the pane cannot draw: use `kit/zta.js shot`.
- git: local user.name/email, `core.autocrlf false`. Remote `origin` is the public GitHub repository.

Engine reference: [engine/README.md](engine/README.md).
