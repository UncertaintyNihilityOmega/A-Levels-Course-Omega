# FURTHER: starting notes for the Further Mathematics extension (Organizer, 2026-10-15)

The user asked for **Further Mathematics as an extended part of the Maths course**, not a separate course. Its
chapters live in this course (`math.fm.*`, group "Further Mathematics", `@level fm`) and build directly on the
Maths chapters: link them instead of re-teaching (math.p1.*, math.p3.*, math.m.*, math.s1.*, math.s2.*).

## For the Specialist LEAD of the extension
1. Syllabus: Cambridge International AS & A Level Further Mathematics (9231), 2026–2027 (the same years as this
   course's 9709 syllabus): https://www.cambridgeinternational.org/Images/697357-2026-2027-syllabus.pdf
   (update: https://www.cambridgeinternational.org/Images/729291-2026-2027-syllabus-update.pdf). A 2028–2030 syllabus
   exists (https://www.cambridgeinternational.org/Images/744603-2028-2030-syllabus.pdf): note what changes in
   `math.fm.overview`. One fetch each, outcomes per topic into FACTS.md under a "Further Mathematics (9231)" heading.
2. course.json already has a sketch of 31 `math.fm.*` chapters (Further Pure 1, Further Pure 2, Further Mechanics,
   Further Probability and Statistics, then a papers guide, mixed practice and four mocks). Check it against the
   syllabus, split or add chapters, keep ids where you can (aliases for renames).
3. Add packages **P19 onwards** (2–3 chapters each, teaching order), `packages/Pn.md` notes in the same style as
   P1–P18, `"years"` stays 2026–2027, and add the 9231 papers to `"papers"` with ids that do not clash with the 9709
   ones (e.g. `FP1`, `FP2`, `FM`, `FS`). Mocks: one per 9231 paper, with the real time, total marks and style.
4. Gold chapter: pick one Further Pure topic chapter and write it at full quality first (every kit/STYLE.md section,
   `check` and `phone` pass). Proofs use `:::proof` as in the rest of the course.
5. Widget ideas: `fm-polar` (r = f(θ) curves, area), `fm-matrix` (2×2 / 3×3 transformations, eigenvectors),
   `fm-argand` (de Moivre, roots of unity), `fm-de` (slope fields and solutions), `fm-pgf`. Names must not clash
   (kit/LINKS.md lists every widget).
6. `done LEAD "<summary>"` re-marks LEAD; the Organizer has already set FINAL back to open.
