# ROADMAP: the build queue (Organizer)

The user handed the whole build to the Organizer on 2026-10-15 ("I leave everything to you"). The Organizer works
down this list with agent runs (AGENT-RUN.md): 1 Opus Specialist + up to 2 Sonnet Writers, one course at a time,
guard on that course. After each step: check, commit, push, tick the line, add a STATUS.md line, start the next.
A scheduled check (CronCreate, hourly) resumes the run after a usage-limit stop.

1. [x] **Chemistry** (`chem`): complete 2026-10-24 (49/49 chapters, 23 packages, READER 82 items fixed, REVIEW FINAL).
2. [ ] **Biology** (`bio`): planned 2026-10-24 (64 chapters, 24 packages; FACTS, COURSE, packages done). Next: LEAD writes the gold chapter `bio.enzymes` and runs `done LEAD` → packages → reviews → READER → FIX → REVIEW FINAL.
3. [ ] **Reader pass on the finished courses**, as its own run: Maths, then Physics (READER batches → FIX).
   Chemistry and Biology have theirs inside their own runs.
4. [ ] **Further Mathematics** (`math.fm.*`, an extension of the Maths course): Specialist LEAD for the extension
   (courses/math/FURTHER.md has the starting notes) → packages P19+ → reviews → READER for the new chapters → FIX →
   REVIEW FINAL. Before its LEAD, set math STATUS.md `FINAL` back to `open` (Organizer edit).
5. [ ] **Computer Science** (`cs`, 9618).
6. [ ] **Engineering** (`eng`).
7. [ ] **Economics** (`econ`), then **Business** (`bus`), then **Accounting** (`acc`): shared-topic owners in their COURSE.md.
8. [ ] **Psychology** (`psych`, 9990).
9. [ ] **Other subjects** (`other`).
10. [ ] Final assembly: whole-site check, link check of every `:::links` URL, phone pass, STATUS line.

Every course run ends with: the assembly session from ORGANIZER.md for that course, guard off, preview stopped,
then the next course's guard on. From 2027 on, `node engine/status.js` warns about syllabuses in their last exam
year (math, phys, chem, bio end in 2027): plan an update pass for the newer syllabuses then.
