# AGENT-RUN: building a course with agents (Organizer only)

Use only when the user asks for an agent run. One Organizer chat at the project root runs the course's steps as
subagents: **1 Opus Specialist and up to 2 Sonnet Writers/Readers at a time**. Same kit, STATUS.md and packages as
the classic method, so a course can switch methods at any point.

## Cost (Chemistry, 2026)
- Writer package 220–390k agent tokens (15–35 min); review 200–380k; Reader batch 250–320k; FIX round 100–140k;
  LEAD ~400k.
- 3 agents use a 5-hour window in about 2–3 packages plus a review. Chemistry (49 chapters) took about 7–8 windows.

## Start
1. `git status` clean; `node courses/<c>/kit/zta.js status`.
2. Guard on: write the course id into `.claude/hooks/guard-course.txt`. The PreToolUse hook in `.claude/settings.json`
   then blocks any subagent file access or command outside `courses/<c>` (and `..` and git). The Organizer's own
   calls are not checked.
3. Start the course preview: launch config `<c>-preview`.
4. Scheduled check: CronCreate, hourly, off the hour (prompt: "Scheduled hourly check …": if agents run, do nothing;
   if a usage limit stopped them, checkpoint and resume; if none runs, continue the loop). It lives only in this
   session and expires after 7 days.
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
- Resume each stopped agent with **SendMessage** (it keeps its context): say the limit reset, what is on disk, and
  "do not claim again". Start a fresh resume agent only if one cannot be resumed.

## End of the run
- Let running agents finish; check and commit their work.
- Guard off: delete `.claude/hooks/guard-course.txt`. Stop the preview. Delete the scheduled check.
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
```
- Preview: http://localhost:<port> (if it is down, start the "<C>-preview" launch config with preview_start; stop it
  when you finish). Run `node kit/zta.js preview`, then open `http://localhost:<port>/#<chapter-id>`. Prefer
  get_page_text, read_page and javascript_tool probes; screenshots only at scale 0.5. If the pane does not draw
  (the app window is hidden), use `node kit/zta.js shot <id>` (`--dark`, `--phone`) and Read the PNGs.
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
