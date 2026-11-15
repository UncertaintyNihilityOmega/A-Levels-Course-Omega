# ROADMAP: build queue and current state

## Now
- Automatic runs on: app scheduled task `zta-agent-run` (every 2 hours, Auto mode; prompt in
  `~/.claude/scheduled-tasks/zta-agent-run/SKILL.md`), fresh Organizer session per run, lock `.run/run.lock`.
- Queue item 5, Computer Science (`cs`, 9618, 49 chapters in 22 packages): P1–P13 written (28 chapters, 12 widgets),
  P1–P12 reviewed, no open items. Next: WRITE P14 and P15 (two Writers), then REVIEW P13–P16 when four are written.
- Usage gate: weekly limit 95% for every launch (AGENT-RUN.md "Usage gate").
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
- A course ends with: REVIEW FINAL, the assembly session (ORGANIZER.md), guard off, preview stopped.
- A run stopped by a usage limit leaves a stale lock; the next scheduled session checkpoints and continues.
- From 2027 `status.js` warns about syllabuses in their last exam year (math, phys, chem and bio end in 2027): plan
  update passes for the new syllabuses then.

## Queue
5. **Computer Science** (`cs`, 9618): packages → reviews → READER → FIX → REVIEW FINAL → assembly.
10. **Further Mathematics** (`math.fm.*`, an extension of the Maths course): LEAD for the extension
   (`courses/math/FURTHER.md`) → packages P19+ → reviews → READER for the new chapters → FIX → REVIEW FINAL.
   Before its LEAD, set math STATUS.md `FINAL` back to `open` and rewrite courses/math/COURSE.md as rules (30 KB).
11. **Engineering** (`eng`).
12. **Economics** (`econ`), then **Business** (`bus`), then **Accounting** (`acc`): shared-topic owners in their COURSE.md.
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
- Mathematics (A Level, 62 chapters), Physics (39), Chemistry (49), Biology (64), History (96): complete.
- GitHub Pages: every push to `main` checks, builds and publishes the site.
- About pages for every unbuilt course (`core/about.<c>.md`): each is its course's only sidebar entry until the first chapter is written.
- 1 Phone, Mac and accessibility: installable web app, WCAG 2.2 AA pass, macOS tools, automatic runs (Nov 2026).
- 2 Biology (`bio`, 9700): complete (Nov 2026).
- 3 History (`hist`, 9489; replaced Psychology): complete (Nov 13 2026).
- 4 Reader pass on Mathematics and Physics: 169 and 109 items fixed; release v0.6.0 tagged (Nov 13 2026).
- 6 Site loading: one file per chapter, a search file per course (Nov 14 2026; numbers in engine/README.md "Build").
- 7 Findable pages: `p/<chapter>.html`, `sitemap.xml`, sharing tags (Nov 14 2026).
- 8 Phone reading: "On this page" sheet, reading progress line, resume at the last section (Nov 15 2026).
- 9 Study aids and checks: spaced re-tests, search results course by course, the reused-numbers check note
  (Nov 15 2026). Left out on purpose: a smaller search index (the search files are the chapters' plain text; only
  giving up full-text search would shrink them) and the maths font in `p/page.css` (do it if a device shows the
  plain pages wrongly).

## For the user
Things only you can do. None of them stops the automatic runs.
- **Look at phone reading on your phone.** The design is frozen, and this was applied to every chapter without the
  one-chapter preview the queue asked for. Open any chapter, try the round button at the bottom right, the line
  under the top bar, and "Pick up where you left off" on Home. Say if anything should change.
- **Tell Google about the pages** (optional). Google Search Console → add the site as a "URL prefix" property →
  verify with the "HTML tag" method (the code goes in package.json `googleSiteVerification`; give it to the
  Organizer or paste it there, then push) → Sitemaps → `sitemap.xml`.
- **GitHub Release page for v0.6.0** (optional; the tag is pushed). github.com → the repository → Releases → Draft a
  new release → tag v0.6.0 → notes from CHANGELOG.md 0.6.0.
- **Upload the `new-project` skill.** `.run/new-project.zip` → claude.ai → Settings → Capabilities → Skills.
- **Screen-reader check** (not testable here). VoiceOver on iPhone and Mac (rotor headings, a chapter, search, a
  quiz, a widget with a canvas), and NVDA or Narrator on Windows if available.
