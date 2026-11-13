# ROADMAP: build queue and current state

## Now
- Automatic runs on: app scheduled task `zta-agent-run` (every 2 hours, Auto mode; prompt in
  `~/.claude/scheduled-tasks/zta-agent-run/SKILL.md`), fresh Organizer session per run, lock `.run/run.lock`.
- History (`hist`, 9489, 96 chapters) complete Nov 13: REVIEW FINAL done, assembled (links page `tools.l.hist`,
  History section on the resources page). Its COURSE.md has the course rules; history in git.
- Reader pass done Nov 13: Mathematics (169 items) and Physics (109 items, 4 batches; phys.dc added to P5), all
  FIXed; site check 0 errors, strict build passes. Release v0.6.0 tagged (CHANGELOG).
- Now: queue item 5, Computer Science (`cs`, 9618): Specialist LEAD next, guard on `cs`.
- User check with a screen reader (not testable here): VoiceOver on iPhone and Mac (rotor headings, a chapter, search,
  a quiz, a widget with a canvas), and NVDA or Narrator on Windows if available.
- User check in Safari (not testable on the PC), on the published site: iPhone Share → Add to Home Screen (icon and
  name "Zero to A*"); open it in flight mode (home, a chapter in each course, search); portrait and landscape: the
  notch and home bar cover no text, menu or toast; dark mode from the system and from the theme button (status bar
  matches); Mac Safari File → Add to Dock, then the same offline open. Progress in the home-screen app is separate
  from Safari's.
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
6. [ ] **Further Mathematics** (`math.fm.*`, an extension of the Maths course): LEAD for the extension
   (`courses/math/FURTHER.md`) → packages P19+ → reviews → READER for the new chapters → FIX → REVIEW FINAL.
   Before its LEAD, set math STATUS.md `FINAL` back to `open` and rewrite courses/math/COURSE.md as rules (30 KB).
7. [ ] **Engineering** (`eng`).
8. [ ] **Economics** (`econ`), then **Business** (`bus`), then **Accounting** (`acc`): shared-topic owners in their COURSE.md.
9. [ ] **Other subjects** (`other`), including the Psychology summary (`other.psychology`).
10. [ ] Final assembly: whole-site check, link check of every `:::links` URL, phone pass.
