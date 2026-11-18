# ROADMAP: build queue and current state

## Now
- Automatic runs on: app scheduled task `zta-agent-run` (every 2 hours, Auto mode; prompt in
  `~/.claude/scheduled-tasks/zta-agent-run/SKILL.md`), fresh Organizer session per run, lock `.run/run.lock`.
- Queue item 5, Computer Science (`cs`, 9618, 49 chapters in 22 packages): all 22 packages written (49 chapters,
  16 widgets), P1–P19 reviewed, no open items. Waiting for the reset at 01:10 Nov 19 (5-hour window 80%). Next: REVIEW
  P20, P21, P22 (the last packages; P21: check that the insert table renders well inside the `:::exam` box at phone
  width; P22: cs.mock.p4 Question 3 methods (c)–(e) belong inside `Department`), then READER batches, FIX, REVIEW FINAL.
- Usage gate: weekly limit 95% for every launch (AGENT-RUN.md "Usage gate").
- Name: "Zero to A* Ω" (titles, installed app, shared links). Top bar and Home heading: the hand-drawn wordmark "Log end"
  (`engine/wordmark.py --shell` writes it into shell.html; colours in style.css `.wm-*`).
- Site check, Nov 15 (every page opened in the app at phone width, every built file and every external link
  checked): no script errors, no broken internal links. Left as they are:
  - widgets `breakeven` and `npv` on `tools.calc` show "being built" until Business and Accounting write them;
  - `https://www.nelsonmandela.org/` answered 526 (its server's certificate) on Nov 15; it is linked from
    hist.d.safrica.1–3: check it again at the final assembly and replace it if it is still down.
- Per-course numbers: `node engine/status.js` (it also lists dated facts in core pages that are now in the past).

## Rules
- Work down the queue with automatic agent runs (AGENT-RUN.md "Automatic runs"): a scheduled task (every 2 hours) starts a
  fresh Organizer session; 1 Opus Specialist + up to 2 Sonnet Writers, one course at a time, guard on that course.
- After each step: check, commit, push, update "Now".
- **The queue holds unfinished items only.** At the end of every run: move each finished queue item to "Done" (one
  line: its number, what it is, the date), delete finished lines from "Now", and put anything only the user can do
  under "For the user" (never in the queue). Queue numbers never change (commits and docs refer to them).
- **"Done" covers the current snapshot only.** It lists what was finished since the last CHANGELOG.md version, as
  short lines (queue number, date, decisions left out on purpose, user checks); what readers notice goes under
  "Unreleased" in CHANGELOG.md. When a snapshot is cut (its version heading written in CHANGELOG.md), empty "Done".
- A course ends with: REVIEW FINAL, the assembly session (ORGANIZER.md), guard off, preview stopped.
- A run stopped by a usage limit leaves a stale lock; the next scheduled session checkpoints and continues.
- From 2027 `status.js` warns about syllabuses in their last exam year (math, phys, chem and bio end in 2027): plan
  update passes for the new syllabuses then.
- User tasks ("For the user") are written as numbered steps: where to go, what to click or type, what should appear.
- Versions: 0.x snapshots are notes in CHANGELOG.md only (0.7.0 = Computer Science and Engineering; 0.8.0 = Business,
  Economics, Accounting and Other subjects; 0.9.0, optional = "Sciences and technology" and "English and languages"
  as full courses). GitHub Releases start at v1 and go up in whole numbers.

## Queue
5. **Computer Science** (`cs`, 9618): packages → reviews → READER → FIX → REVIEW FINAL → assembly.
10. **Further Mathematics** (`math.fm.*`, an extension of the Maths course): LEAD for the extension
   (`courses/math/FURTHER.md`) → packages P19+ → reviews → READER for the new chapters → FIX → REVIEW FINAL.
   Before its LEAD, set math STATUS.md `FINAL` back to `open` and rewrite courses/math/COURSE.md as rules (30 KB).
11. **Engineering** (`eng`).
12. **Business** (`bus`), then **Economics** (`econ`), then **Accounting** (`acc`): shared-topic owners in their COURSE.md
   (Business pages that use an Economics widget or link show a placeholder or plain text until Economics is written).
13. **Other subjects** (`other`), including the Psychology summary (`other.psychology`).
14. Final assembly: whole-site check, link check of every `:::links` URL, phone pass.
15. **Dated facts for 2028 entry** (Organizer, core pages): when UCAS and the test providers publish the 2028-entry
   dates (spring 2027), renew the deadlines and test sittings that `node engine/status.js` lists as past, in
   FACTS.md and the core pages.
16. **Fact-check upgrades** (Organizer, engine; from the Nov 15 look at the system):
   - each course's paper facts (time, marks, number of questions) in `course.json` `papers`, and a check that every
     mock's `@time` and `@total` match them (now compared by hand at REVIEW FINAL);
   - root FACTS.md keeps only facts shared by several courses; a course's own paper facts live in its FACTS.md alone
     (the root file has no line for 9618 or 9489, so the "update both copies" rule is already broken);
   - a `check` note when an expected number in `checks/<id>.py` is no longer in the chapter (a FIX changed the text
     but not the check; measured Nov 15: 94–97% of expected numbers are found, the rest are format differences).

## Done
Since 0.6.0 (Nov 13 2026). Earlier work: CHANGELOG.md; what readers see of the items below: its "Unreleased".
- 6 Site loading (Nov 14 2026; numbers in engine/README.md "Build").
- 7 Findable pages (Nov 14 2026).
- 8 Phone reading (Nov 15 2026).
- 9 Study aids and checks (Nov 15 2026). Left out on purpose: a smaller search index (the search files are the
  chapters' plain text; only giving up full-text search would shrink them) and the maths font in `p/page.css` (do it
  if a device shows the plain pages wrongly).
- User checks, Nov 15 2026: phone reading works on the user's phone; screen readers work on PC and phone, site and
  app; the site is verified in Google Search Console; the `new-project` skill shows in the app's skill list; the
  user's Nov 15 list (wordmark, name, sidebar order and lines, Graph plotter and Periodic table, Settings) is checked.
  The installed app keeps the published icon (tried on Android Chrome; the user accepts it).
- Project folder renamed to `A Levels Course Omega` (Nov 18 2026): docs and the scheduled task prompt updated.

## For the user
Things only you can do. None of them stops the automatic runs.
- **Google sitemap: wait, then look again.** The sitemap is published and valid (382 pages). "Couldn't fetch" is what
  Search Console usually shows for the first days of a new site.
  1. In 3 to 7 days open Google Search Console → Sitemaps.
  2. The status should read "Success" with about 382 discovered pages ("videos 0" is correct: the site has none).
  3. If it still says "Couldn't fetch": remove the sitemap (⋮ → Remove sitemap), then add it again as the full address
     `https://uncertaintynihilityomega.github.io/A-Levels-Course-Omega/sitemap.xml`. If that fails too, tell the Organizer.
- **Default colours of the courses and sidebar sections.**
  1. Try colours first: open the guide → Settings → "Course and section colours". A colour changes at once, on your
     device only. Look at a chapter, the sidebar and a figure, in paper and in chalkboard mode.
  2. To make a colour the default for everyone, open `engine/style.css`. Lines 36–50 (inside the first `:root {`) hold
     the paper-mode colours: `--c-math: #3442B4;` is the main colour of Mathematics, `--c2-math` its second colour in
     figures. The ids: start, road, math, phys, chem, bio, eng, bus, econ, acc, other, cs, hist, tools, practice.
  3. The chalkboard colours are the same names, written twice (lines 61–68 and 77–84): change both copies the same way.
  4. Save, run `node engine/build.js`, open `site/index.html` and look.
  5. Tell the Organizer "check the colours". It measures every colour against the page in both modes (text needs a
     contrast of 4.5 to 1), and for any that fail it proposes the nearest colour that passes and tells you which.
  6. Only then are the colours committed and published.
