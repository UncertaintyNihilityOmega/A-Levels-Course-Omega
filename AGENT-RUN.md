# AGENT-RUN: building a course with agents (Organizer)

The default way to work down ROADMAP.md. An Organizer session at the project root runs the course's steps as
subagents: **1 Opus Specialist and up to 2 Sonnet Writers/Readers at a time**. Same kit, course STATUS.md and
packages as the classic method, so a course can switch methods at any point.

## Cost (Chemistry, 2026)
- Writer package 220–390k agent tokens (15–35 min); review 200–380k; Reader batch 250–320k; FIX round 100–140k;
  LEAD ~400k.
- 3 agents use a 5-hour window in about 2–3 packages plus a review. Chemistry (49 chapters) took about 7–8 windows.

## Automatic runs (default)
Runs are driven by an app **scheduled task**, so every step starts in a fresh session with an empty context and no
chat has to stay open. Set up once (ROADMAP queue item 1); the user then only keeps the desktop app open and the PC
awake (Windows: Sleep "Never" when plugged in).
- Task: `mcp__scheduled-tasks__create_scheduled_task`, taskId `zta-agent-run`, every 2 hours off the
  hour (`23 */2 * * *`; each start that stops at the lock costs about 1% of the 5-hour window), saved in Auto
  permissions. Its prompt is self-contained: work in the project root, read
  ORGANIZER.md, ROADMAP.md and this file, then follow "Each run" below.
- Lock: `.run/run.lock` (`.run/` is git-ignored; run state stays out of `.claude/`, where every write asks for
  permission even in Auto mode) holds `{"session": "<time started>", "beat": "<last update>", "id": "<session id>"}`
  (the id from `get_session("self")`). The lock is stale when its `beat` is 90 minutes old or more, or when
  `list_task_runs("zta-agent-run")` shows the lock's `id` as not `running` (it failed at a usage limit or ended).
  Stale: take over. Otherwise another session is running: stop at once.
- Each run:
  1. Lock check (above). Write the lock.
  2. `git status`; `check` every changed chapter; commit a checkpoint and push.
  3. The current course is ROADMAP "Now". Guard on that course. Read `status`; started-but-unfinished packages
     (`writing`) get resume agents; an interrupted review is re-run whole.
  4. Run the loop below until the course step is done, the usage gate blocks every start, or the usage limit stops
     the agents. Update the lock `beat` each time an agent reports and at least every 45 minutes (a background
     `sleep 2400` as the timer).
  5. Course finished: REVIEW FINAL, assembly, tick ROADMAP, set "Now" to the next item, start it in the same run.
     Queue empty or a step needs the user (a decision, a manual setting): write it in "Now", delete the lock, stop.
- Pause: the user disables the task in the app (or says "pause the runs"); set "Now" to say so.
- Manual runs (an Organizer chat the user keeps open, with a CronCreate hourly check) stay possible: use the same
  lock so the two never overlap.

## Usage gate (before every launch)
- Read the meter with `get_usage` (`mcp__ccd_session_mgmt__get_usage`) just before each agent launch.
- Writer (WRITE, FIX + WRITE, resume): only if the 5-hour window is at 70% or less and the weekly limit at 85% or less.
- Specialist (REVIEW, LEAD), Reader, FIX only: 5-hour at 75% or less, weekly at 85% or less.
- Otherwise start nothing: let running agents finish, check and commit them. If the 5-hour reset is under 30 minutes
  away, wait for it (background `sleep`) and go on; else write "waiting for the reset at <time>" in "Now", delete the
  lock and stop. A later scheduled run starts again once the gate allows it.
- Log every agent in `.run/usage.log`, one line: date, step, model, 5-hour and weekly % at launch and at report, and
  the other agents running meanwhile. Once 6 agents are logged, set the thresholds here from the numbers (a launch
  must leave room for that step's typical share of the window).

## Start (manual run, or the first steps of an automatic run)
1. `git status` clean; `node courses/<c>/kit/zta.js status`.
2. Guard on: write the course id into `.run/guard-course.txt`. The PreToolUse hook in `.claude/settings.json`
   then blocks any subagent file access or command outside `courses/<c>` (and `..` and git). The Organizer's own
   calls are not checked.
3. Preview: headless by default. Start a preview server (`<c>-preview`, `site`) with preview_start only when the user
   says in this session that they are here or that the server may be used: the app asks to approve it in every new
   session, and nobody can approve it in night runs. Headless, the Specialist uses the kit tools (template below).
4. Manual runs only: a CronCreate check, hourly, off the hour (if agents run, do nothing; if a usage limit stopped
   them, checkpoint and resume with SendMessage; if none runs, continue the loop). It lives only in this session.
5. Launch agents with the templates below: `subagent_type` general-purpose, `model` opus (Specialist) or sonnet
   (Writer, Reader), `effort` high, `run_in_background` true.

## Loop
- No plan yet → Specialist LEAD alone; then answer its REQUESTS.md lines, sync, commit.
- Keep 2 Writers busy, one named package each, in `status` order. A fresh agent per package.
- When 3 packages are written (or the last ones), start the Specialist REVIEW for exactly those, while Writers go on
  (the kit allows 6 packages past the last review; at WAIT, wait).
- After a review: the next Writer does **FIX + WRITE Pn** (one FIX at a time; give FIX Writers disjoint chapters).
- Each time an agent reports: `check` its chapters, commit only its files (`git add` named paths), push, answer
  REQUESTS.md (engine fixes are the Organizer's), re-sync after engine changes.
- READER: batches of 7–9 chapters in course order, one Reader at a time. Early batches may start while late packages
  are still in review (their chapters are final). Give the Reader items to a FIX Writer every ~25 items, on chapters
  no other agent is editing.
- End: Specialist **REVIEW FINAL** (targeted: check/phone all, spot-check the FIX rounds, Next chain, mock totals,
  links), then the assembly session (ORGANIZER.md).

## Usage-limit stop
- Agents fail with a rate-limit error; nothing on disk is lost.
- After the reset: `git status`, `status`, `check` every changed chapter, commit a checkpoint, push.
- Automatic runs: the stopped agents belonged to the old session and cannot be resumed. Start a fresh resume agent
  per stopped package (usual template plus: "already claimed, do not claim"; what is on disk and passes `check`;
  what is missing). An interrupted review is re-run whole.
- Manual runs (same session): resume each stopped agent with **SendMessage** (it keeps its context): say the limit
  reset, what is on disk, and "do not claim again".

## End of the run
- Let running agents finish; check and commit their work.
- Guard off: delete `.run/guard-course.txt`. Stop the preview. Delete the CronCreate check and the lock.
- Update ROADMAP.md "Now"; tick the course.

## Prompt templates
Replace `<C>` (course id), `<PATH>` (`C:\Users\Uncertainty\Desktop\Claude_Test\A Levels Course\courses\<C>`),
`<SHPATH>` (the same with forward slashes), `<port>` and `<Pn>`. Every template starts with the common block.

### Common block (all agents)
```
Your course folder is `<PATH>` (the course folder). First read `<PATH>\CLAUDE.md`, the course's instruction file,
and follow its "Rules for every session" and "<STEP> (<ROLE>)" steps, with these differences because you run as an agent:
- Your shell does not start in the course folder. Use absolute paths with Read/Write/Edit, always pass `path:` = the
  course folder to Grep/Glob, and begin every Bash command with `cd "<SHPATH>" && …`.
- A guard blocks every file access and command outside the course folder (and `..` and git). That is intended;
  never work around it.
- No subagents, no git. Python is `py`. Edit chapters only with Write/Edit (never a script: heredocs eat backslashes).
- Save tokens without lowering quality: every tool call re-sends your whole context, so bundle commands (check and
  phone in one Bash call, one Python script per chapter's figures), and open screenshots only when you need to look.
- Do not leave background processes running when you finish.
```

### Writer additions (WRITE, FIX + WRITE)
```
- Do not use the browser tools at all: another agent uses the browser. Your checks are `node kit/zta.js check <id>`,
  `phone <ids>` and `widget <name> "…" --probe`. Check every SVG figure's coordinates and label positions with Python,
  then look at them once, at the end, with `node kit/zta.js shot <id>` and `shot <id> --phone` (headless PNGs in
  preview/shots/; open them with Read) and fix what you see. Dark shots only for a widget whose probe flagged something
  (the reviewer looks at dark mode).
- Other agents work on other packages at the same time. Touch only <Pn>'s files: its chapters, their checks and the
  widgets/<name>.js files it builds (generator scripts in data/, not scratch/). Never edit COURSE.md, course.json,
  FACTS.md, widgets.js, REVIEW.md, another package's files, or STATUS.md (the kit writes it).
Steps:
1. `node kit/zta.js claim <Pn>`. If it fails, report the message and stop.
2. Read COURSE.md (follow every rule), kit/STYLE.md, the gold chapter and packages/<Pn>.md. Your package file has the
   learning outcomes; grep FACTS.md only for a specific fact; grep earlier chapters only for specific terms.
3. Write each chapter in full, at the depth and with every section the gold chapter shows, then its checks file;
   `check <id>` must pass with no checklist notes. Save each chapter as soon as it is written. Then build the package's
   widgets and probe them clean (light, dark, phone, bad attributes; they must survive zero size).
4. `phone` for your chapters must pass. Then `node kit/zta.js done "WRITE <Pn>" "<chapters; widgets; notes for the reviewer>"`.
Reply in at most 6 lines: chapters with word counts and check results, widgets and probe results, anything left undone.
```
- **FIX + WRITE**: put "Part 1: FIX" first: the open REVIEW.md items and their chapters; make each change exactly as
  written, add new numbers to the checks, mark each `[x]`, check and phone those chapters, `done FIX "<what changed>"`.
- **FIX only** (Reader items): name the REVIEW.md headings to close, the chapters other agents are editing (never
  touch), "grep for the section each item names, then Read just that range".

### Reader additions (READER)
```
- Do not use the browser tools. Never edit chapters, checks, widgets or any file except READER.md and REVIEW.md
  (append only to REVIEW.md: re-read its end just before each append; if an Edit fails because the file changed,
  re-read and retry).
- Your batch: <ids> (in this order). Read READER.md first, then each chapter whole, as a student who knows only what
  the "Taught" lines say. File items under a heading "READER: <first id> to <last id>".
- If READER.md then covers every chapter, run `done READER "<n reader items>"`; otherwise do not run `done`.
Reply in at most 5 lines: chapters read, how many (reader) items you filed, the worst one.
```

### Specialist additions (LEAD, REVIEW, REVIEW FINAL)
Headless (default):
```
- No preview server and no browser tools. Look at pages with `node kit/zta.js shot <id>` (`--dark`, `--phone`) and
  Read the PNGs; test widgets with `node kit/zta.js widget <name> "…" --probe` (light, dark, phone, bad attributes,
  a11y) and check their maths in data/ scripts.
- Writer agents are writing other packages at the same time: do not touch their files. You may tighten COURSE.md or
  the notes of packages nobody has claimed yet.
```
With the preview server (only when the user allowed it this session; the Organizer has started it):
```
- Preview: http://localhost:<port> (never start or stop a server yourself; if it is down, use the headless kit tools).
  Run `node kit/zta.js preview`, then open `http://localhost:<port>/#<chapter-id>`. Prefer get_page_text, read_page
  and javascript_tool probes; screenshots only at scale 0.5. If the pane does not draw (the app window is hidden),
  use `node kit/zta.js shot <id>` (`--dark`, `--phone`) and Read the PNGs.
- Writer agents are writing other packages at the same time: do not touch their files. You may tighten COURSE.md or
  the notes of packages nobody has claimed yet.
```
- **LEAD**: packages of 2–3 chapters (core topics first, then skills, then exam readiness: a guide per paper, mixed
  practice, one mock per written paper with the real time, marks and question style). Every `packages/Pn.md` is
  self-sufficient. Each widget belongs to one package. FACTS.md records what each real paper prints and allows (from a
  recent question paper's front page). The gold chapter has every STYLE section and passes check and phone.
  `done LEAD`; reply with a 3-line summary, the package list, the gold chapter's results and REQUESTS.md lines.
- **REVIEW <Pa>, <Pb>, <Pc>**: look at every figure and widget (light, dark, phone, interactions), fix layout
  yourself, read and recompute at CLAUDE.md step 2 depth, judge depth, list the Writers' notes to confirm (end of
  each packages/Pn.md). `done "REVIEW <Pa>, <Pb>, <Pc>"`. Reply in at most 8 lines.
