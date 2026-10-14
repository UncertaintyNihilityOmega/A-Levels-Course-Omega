# AGENT-RUN: building a course with agents (Organizer only)

The **agent method** is the second way to build a course (PROJECT.md, "Two ways to build a course"). The user starts
it when they have usage to spare, typically before a usage window resets. One Organizer chat at the project root
runs the course's sessions as subagents: **1 Opus Specialist and up to 2 Sonnet Writers at a time**. It uses the
same kit, STATUS.md and packages as the classic method, so a course can switch methods at any point.

Only run it when the user asks for it in that chat. It is not the default.

## What it costs (Physics night, 2026-10-13/14)
- A Writer package costs 230–280k agent tokens and takes 15–25 minutes. A review costs 300–380k tokens and
  takes 15–30 minutes. LEAD took 400k tokens and 38 minutes.
- About 14k tokens per agent-minute, or 30–45k per minute with 2–3 agents running.
- **A Pro 5-hour window lasts about 1–1.5 hours** this way, which is about 3 packages (6 chapters), or a
  package plus a review. The whole night used about 16% of the weekly allowance.
- Tell the user these numbers when they ask how far a run will get.

## Start
1. `git status` must be clean. Read the course's `status` (`node courses/<c>/kit/zta.js status`).
2. **Guard on**: write the course id into `.claude/hooks/guard-course.txt` (e.g. `phys`). The PreToolUse hook in
   `.claude/settings.json` then refuses any subagent file access or command outside `courses/<c>` (and `..` and
   git). The Organizer's own calls are never checked. Without that file the guard does nothing.
3. Start the course's preview server: launch config `<c>-preview` (port 5101–5109), so the Specialist can look
   at pages. Only the Specialist uses the browser; Writers never do.
4. Launch agents with the templates below: `subagent_type` general-purpose, `model` opus (Specialist) or
   sonnet (Writer), `effort` high (the user's choice), `run_in_background` true.

## The loop (until the course is done or the usage limit stops it)
- Course not planned → Specialist **LEAD** alone. Then answer its REQUESTS.md lines, `node engine/sync.js`, and commit.
- Then keep **2 Writers** busy, each with one named package (in `status` order). Start a new agent for each
  package: a fresh context is cheaper than a long one.
- When `status` lists a REVIEW (2+ packages written), start the **Specialist REVIEW** for exactly those
  packages, while the Writers go on. The kit allows at most 4 packages past the last review (`AHEAD` in
  engine/progress.js). When it says WAIT, wait for the review.
- After a review: give its REVIEW.md items to the next Writer as **FIX + WRITE Pn** (only one agent at a time does FIX).
- **Each time an agent reports**: run `check` on its chapters yourself, then commit only that package's files
  (`git add` named paths, because other agents are mid-work). Answer REQUESTS.md lines (engine fixes are yours),
  and re-sync the kits after any engine change.
- At the end: Specialist **REVIEW FINAL**, then the assembly session from ORGANIZER.md.

## When the usage limit stops agents
The agents fail with a rate-limit error. Nothing on disk is lost.
1. When the user says to continue: `git status`, then `status`. Run `check` on every changed chapter, and commit a checkpoint.
2. For each interrupted session, start a **resume** agent (template below). Tell it which files exist and
   pass `check`, and which are missing. A claimed package stays `writing`, so the resume agent must not `claim`.
3. An interrupted review is re-run whole (it keeps the earlier edits).

## End of the run
- Let running agents finish (stopping them wastes what they have spent), check and commit their work.
- **Guard off**: delete `.claude/hooks/guard-course.txt`. Stop the preview server.
- Add a root STATUS.md line: what was done, chapters, the next step.

## Prompt templates
Replace `<C>` (course id), `<TITLE>` (course title), `<PATH>` (`C:\Users\Uncertainty\Desktop\Claude_Test\A Levels Course\courses\<C>`),
`<SHPATH>` (the same with forward slashes) and `<Pn>`. Every template starts with the **common block**.

### Common block (all agents)
```
Your course folder is `<PATH>` (the course folder). First read `<PATH>\CLAUDE.md`, the course's instruction file,
and follow its "Rules for every session" and "<STEP> (<ROLE>)" steps, with these differences because you run as an agent:
- Your shell does not start in the course folder. Use absolute paths with Read/Write/Edit, always pass `path:` = the
  course folder to Grep/Glob, and begin every Bash command with `cd "<SHPATH>" && …`.
- A guard blocks every file access and command outside the course folder (and `..` and git). That is intended;
  never work around it.
- No subagents, no git. Python is `py`. Edit chapters only with Write/Edit (never a script: heredocs eat backslashes).
```

### Writer additions (WRITE, FIX + WRITE, resume)
```
- Do not use the browser tools at all: another agent uses the browser. Your checks are `node kit/zta.js check <id>`,
  `phone <ids>` and `widget <name> "…" --probe`. Check every SVG figure's coordinates and label positions with Python,
  then look at them once with `node kit/zta.js shot <id>` (headless PNGs in preview/shots/; open them with Read) and fix
  what you see.
- Other agents work on other packages at the same time. Touch only <Pn>'s files: its chapters, their checks and the
  widgets/<name>.js files it builds. Never edit COURSE.md, course.json, FACTS.md, widgets.js, REVIEW.md, another
  package's files, or STATUS.md (the kit writes it).
Steps:
1. `node kit/zta.js claim <Pn>`. If it fails, report the message and stop.
2. Read COURSE.md (follow every rule under Figures, which the reviews add), kit/STYLE.md, the gold chapter and
   packages/<Pn>.md. Your package file has the learning outcomes; grep FACTS.md only for a specific fact.
3. Write each chapter in full, at the depth and with every section the gold chapter shows, then its checks file;
   `check <id>` must pass with no checklist notes. Then build the package's widgets and probe them clean
   (light, dark, phone, bad attributes).
4. `phone` for your chapters must pass. Then `node kit/zta.js done "WRITE <Pn>" "<chapters; widgets; notes for the reviewer>"`.
Reply in at most 6 lines: chapters with word counts and check results, widgets and probe results, anything left undone.
```
- **FIX + WRITE**: put a "Part 1: FIX" first. REVIEW.md has n open items in <chapters>. Make each change
  exactly as written, with small Edits, add new numbers to the checks, mark each `[x]`, check and phone those
  chapters, then `done FIX "<what changed>"`. Part 2 is the WRITE steps.
- **Resume**: "<Pn> is already claimed: do not run `claim`. Done and passing check: <files>. Missing: <files>.
  Do not reread the finished chapters whole; grep them only for links, widget embeds and the Next line."

### Specialist additions (LEAD, REVIEW, REVIEW FINAL)
```
- Preview: the course preview is served at http://localhost:<port> (if it is down, start the "<C>-preview" launch
  config with preview_start). Run `node kit/zta.js preview`, then open `http://localhost:<port>/#<chapter-id>` with
  the browser tools (you are the only agent using the browser). Prefer get_page_text, read_page and javascript_tool
  probes; screenshots only at scale 0.5; resize_window preset mobile for phone width, then reset it to desktop.
  If the pane does not draw (the app window is hidden while the user is away), use `node kit/zta.js shot <id>`
  (`--dark`, `--phone`) and open the PNGs in preview/shots/ with Read.
- Writer agents are writing other packages at the same time: do not touch their files. You may tighten COURSE.md
  or the notes of packages nobody has claimed yet.
```
- **LEAD**: the plan has packages of 2–3 chapters (core topics first, extras after). Every `packages/Pn.md` is
  self-sufficient (copy in the outcome numbers and text, pitfalls, example ideas, figures, proofs, widget specs).
  Each widget belongs to exactly one package. The gold chapter has every STYLE section and passes check and phone.
  Finish with `done LEAD`, then reply: a 3-line summary, the package list (`P1: ids (widgets: …)`), the gold
  chapter's check and phone results, and anything for the Organizer.
- **REVIEW <Pa>, <Pb>**: Writers cannot use the browser, so nobody has looked at their figures or widgets yet.
  Look at every figure and widget (light, dark, phone, interactions), fix layout yourself, then read and recompute
  at CLAUDE.md's step 2 depth. Judge depth and add what is missing, or list precise additions. List the Writers'
  reported deviations for the reviewer to confirm. Finish with `done "REVIEW <Pa>, <Pb>"` (exactly those packages).
  Reply in at most 8 lines.
