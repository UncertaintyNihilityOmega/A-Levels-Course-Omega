# ROADMAP: build queue and current state

## Now
- Automatic runs on: app scheduled task `zta-agent-run` (every 2 hours, Auto mode; prompt in
  `~/.claude/scheduled-tasks/zta-agent-run/SKILL.md`), fresh Organizer session per run, lock `.run/run.lock`.
- History (`hist`, 9489, 96 chapters) complete Nov 13: REVIEW FINAL done, assembled (links page `tools.l.hist`,
  History section on the resources page). Its COURSE.md has the course rules; history in git.
- Reader pass done Nov 13: Mathematics (169 items) and Physics (109 items, 4 batches; phys.dc added to P5), all
  FIXed; site check 0 errors, strict build passes. Release v0.6.0 tagged (CHANGELOG).
- Now: queue item 5, Computer Science (`cs`, 9618, 49 chapters in 22 packages): LEAD done Nov 13 (gold cs.datatypes);
  P1–P7 written (16 chapters; widgets cs-binary, cs-ip, cs-logic, cs-asm, cs-check, cs-sql); REVIEW P1–P4 done
  Runs Nov 14: cs-ip and cs.assembly FIXed; P8–P13 written (28 chapters; widgets also cs-trace, cs-stack, cs-float,
  cs-pipeline, cs-kmap, cs-sched); REVIEW P5–P8 done, no open items. Next: REVIEW P9–P12 (status lists P9–P13),
  WRITE P14, WRITE P15.
- Waiting for the 5-hour reset at 03:40 Nov 15 (Istanbul; 00:40 UTC): the gate blocks every start.
- App review, Nov 14 (user, in the run session): queue items 6 and 7 done (per-chapter files, search index, findable
  pages; numbers in engine/README.md "Build"); report-a-mistake link; engine self-test in CI (`node engine/test.js`);
  guard reads the course list from `courses/`; usage gate leaves room for running agents; finished courses' REVIEW.md
  cut to a pointer. Still open: items 8 and 9.
- USER (optional): tell Google about the pages: Google Search Console → add the site → Sitemaps → `sitemap.xml`.
- The `new-project` skill rewritten to this project's structure: `.run/new-project/SKILL.md` (and .zip); the user
  uploads it in claude.ai → Settings → Capabilities → Skills.
- Site, Nov 13 (user's requests): new logo (log end, "AΩ" in Caudex, dark green and white; engine/icons.js), and a
  Settings page (red, last in the sidebar; engine/settings.js): theme, text size, course colours, background,
  highlighter, return to default, export/import/clear progress, protect storage, offline downloads (everything,
  core only, per course; sw.js keeps the choice in the cache "zta.prefs").
  Engine: labelled code blocks and pseudocode/Python check notes (cs requests).
- USER (optional): GitHub Release page for v0.6.0 (tag is pushed; gh not installed, GitHub not signed in in the pane):
  sign in to github.com in the browser pane, or create it at Releases → Draft a new release → tag v0.6.0, notes from
  CHANGELOG.md 0.6.0.
- User check with a screen reader (not testable here): VoiceOver on iPhone and Mac (rotor headings, a chapter, search,
  a quiz, a widget with a canvas), and NVDA or Narrator on Windows if available.
- iPhone / Safari check done by the user (Nov 14): the app works.
- Per-course numbers: `node engine/status.js`.

## Rules
- Work down the queue with automatic agent runs (AGENT-RUN.md "Automatic runs"): a scheduled task (every 2 hours) starts a
  fresh Organizer session; 1 Opus Specialist + up to 2 Sonnet Writers, one course at a time, guard on that course.
- After each step: check, commit, push, update "Now". Tick a line when its item is done.
- A course ends with: REVIEW FINAL, the assembly session (ORGANIZER.md), guard off, preview stopped.
- A run stopped by a usage limit leaves a stale lock; the next scheduled session checkpoints and continues.
- From 2027 `status.js` warns about syllabuses in their last exam year (math, phys, chem and bio end in 2027): plan
  update passes for the new syllabuses then.

## Done
- Mathematics (A Level, 62 chapters), Physics (39), Chemistry (49), Biology (64), History (96): complete.
- GitHub Pages: every push to `main` checks, builds and publishes the site.
- About pages for every unbuilt course (`core/about.<c>.md`): each is its course's only sidebar entry until the first chapter is written.

## Queue
1. [x] **Phone, Mac and accessibility**: installable web app (manifest, icons, service worker for offline use, add to
   home screen), tested in Safari on iPhone and Mac; build and kit tools work on macOS (Python and browser paths).
   Accessibility pass: keyboard-only use of every page and widget, screen-reader labels (figures, widgets, maths),
   colour contrast in light and dark (WCAG AA), focus outlines, text zoom to 200%, reduced motion.
   Automation: create the `zta-agent-run` scheduled task and the lock (AGENT-RUN.md "Automatic runs"), test one run,
   then let it continue the queue from item 2.
2. [x] **Biology** (`bio`): gold chapter + `done LEAD` → packages → reviews → READER → FIX → REVIEW FINAL.
3. [x] **History** (`hist`, 9489; replaces Psychology, user's request 2026-11-07): gold chapter + `done LEAD` →
   packages → reviews → READER → FIX → REVIEW FINAL.
4. [x] **Reader pass** on Mathematics, then Physics (READER batches → FIX), as its own run.
5. [ ] **Computer Science** (`cs`, 9618). Before its LEAD: publish a GitHub release of the site (user, Nov 13).
6. [x] **Site loading** (Organizer, engine; user, Nov 14): one chunk per chapter (or per sidebar group) in place of one
   per course; a search index built at build time (titles, headings, text) so search never loads the chapters; quiz
   and glossary data in their own files so the practice and glossary pages do not load every course. Keep `file://`,
   the service worker and the offline choices in Settings working. Measured Nov 14 (this PC, localhost): `c/hist.js`
   12.0 MB (3.4 MB gzipped); one History chapter loads all 96 (2.2 s, 162k elements); focusing search loads every
   course (16.8 s, 1.13 million elements). Done when a chapter opens with only its own chunk and search stays fast
   at phone size; measure again and record the numbers in engine/README.md.
7. [x] **Findable pages** (Organizer, engine; user, Nov 14): the build also writes a small static page per chapter
   (title, summary, headings, link into the app) and `sitemap.xml`; description and sharing tags in `shell.html`.
   The offline `file://` site stays one `index.html`.
8. [ ] **Phone reading** (Organizer, engine; user, Nov 14): an "On this page" contents sheet at phone width, resume
   at the last section of a chapter (not only the last chapter), and a thin section progress bar. No content is cut.
   The design is frozen: show the user one chapter before applying it to all.
9. [ ] **Study aids and checks** (Organizer, engine; user, Nov 14; from the app review):
   - spaced re-testing: "What to revise next" offers a chapter's quiz questions again 1, 3, 7 and 21 days after it is
     marked as learned (dates in localStorage; no flashcards);
   - search results appear course by course as the search files arrive, the current course first; consider a
     smaller search index (the search files are 16 MB of the 69 MB offline copy);
   - a kit `check` note when a `:::try` question reuses the numbers of a `:::eg` in the same chapter (a repeated
     review finding);
   - the plain pages (`p/`) use the system maths font: embed the subset maths font in `p/page.css` if they look
     wrong on a device.
10. [ ] **Further Mathematics** (`math.fm.*`, an extension of the Maths course): LEAD for the extension
   (`courses/math/FURTHER.md`) → packages P19+ → reviews → READER for the new chapters → FIX → REVIEW FINAL.
   Before its LEAD, set math STATUS.md `FINAL` back to `open` and rewrite courses/math/COURSE.md as rules (30 KB).
11. [ ] **Engineering** (`eng`).
12. [ ] **Economics** (`econ`), then **Business** (`bus`), then **Accounting** (`acc`): shared-topic owners in their COURSE.md.
13. [ ] **Other subjects** (`other`), including the Psychology summary (`other.psychology`).
14. [ ] Final assembly: whole-site check, link check of every `:::links` URL, phone pass.
