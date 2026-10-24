# ROADMAP: build queue and current state

## Now
- No run active. Guard off (`.claude/hooks/guard-course.txt` absent). No scheduled task yet, no lock.
- Next step: queue item 1 (phone and Mac).
- Biology is planned (64 chapters, 24 packages). Its next LEAD session writes the gold chapter `bio.enzymes`, then
  runs `done LEAD`.
- Per-course numbers: `node engine/status.js`.

## Rules
- Work down the queue with automatic agent runs (AGENT-RUN.md "Automatic runs"): an hourly scheduled task starts a
  fresh Organizer session; 1 Opus Specialist + up to 2 Sonnet Writers, one course at a time, guard on that course.
- After each step: check, commit, push, update "Now". Tick a line when its item is done.
- A course ends with: REVIEW FINAL, the assembly session (ORGANIZER.md), guard off, preview stopped.
- A run stopped by a usage limit leaves a stale lock; the next hourly session checkpoints and continues.
- From 2027 `status.js` warns about syllabuses in their last exam year (math, phys, chem and bio end in 2027): plan
  update passes for the new syllabuses then.

## Done
- Mathematics (A Level, 62 chapters), Physics (39), Chemistry (49): complete.
- GitHub Pages: every push to `main` checks, builds and publishes the site.
- About pages for every unbuilt course (`core/about.<c>.md`): each is its course's only sidebar entry until the first chapter is written.

## Queue
1. [ ] **Phone, Mac and accessibility**: installable web app (manifest, icons, service worker for offline use, add to
   home screen), tested in Safari on iPhone and Mac; build and kit tools work on macOS (Python and browser paths).
   Accessibility pass: keyboard-only use of every page and widget, screen-reader labels (figures, widgets, maths),
   colour contrast in light and dark (WCAG AA), focus outlines, text zoom to 200%, reduced motion.
   Automation: create the `zta-agent-run` scheduled task and the lock (AGENT-RUN.md "Automatic runs"), test one run,
   then let it continue the queue from item 2.
2. [ ] **Biology** (`bio`): gold chapter + `done LEAD` → packages → reviews → READER → FIX → REVIEW FINAL.
3. [ ] **Reader pass** on Mathematics, then Physics (READER batches → FIX), as its own run.
4. [ ] **Further Mathematics** (`math.fm.*`, an extension of the Maths course): LEAD for the extension
   (`courses/math/FURTHER.md`) → packages P19+ → reviews → READER for the new chapters → FIX → REVIEW FINAL.
   Before its LEAD, set math STATUS.md `FINAL` back to `open` and rewrite courses/math/COURSE.md as rules (30 KB).
5. [ ] **Computer Science** (`cs`, 9618).
6. [ ] **Engineering** (`eng`).
7. [ ] **Economics** (`econ`), then **Business** (`bus`), then **Accounting** (`acc`): shared-topic owners in their COURSE.md.
8. [ ] **Psychology** (`psych`, 9990).
9. [ ] **Other subjects** (`other`).
10. [ ] Final assembly: whole-site check, link check of every `:::links` URL, phone pass.
