# REVIEW: Mathematics

Findings for the Writer, newest review at the bottom. One item per line:
`- [ ] <chapter-id>: <exactly what to change>`. The Writer fixes it and changes `[ ]` to `[x]`.
While any `- [ ]` line is open, `status` says FIX.

All 182 items of the finished course are closed. The full list is in git (last complete copy: commit 53190a2).

## REVIEW P19, P20, P21, P22 (20 Nov 2026)
- [ ] math.fm.rational: only one `:::eg (Exam style)` (COURSE.md asks for at least two). Turn "Find the set of values taken by y = (x² − 3x + 6)/(x − 1)" into an exam-style example with M/A marks on the lines that earn them, in the 2027 specimen shape "Show that y ≤ a or y ≥ b at all points on C" [4]; recount marks and update checks/math.fm.rational.py.
- [ ] math.fm.graphs: only one `:::eg (Exam style)`. Mark the example "Find the exact set of values of x for which 2x/(x + 1) …" (section "Inequalities with rational functions in exact form") as `(Exam style)` with [M1] [A1] [B1] marks: critical values, sign table, final set; recount the chapter marks.
- [ ] math.fm.vectors: only one `:::eg (Exam style)` (5 marks). Make the roof example (plane through P, Q, R) a multi-part exam-style question with marks: (a) the plane in Cartesian form, (b) its distance from the origin, (c) the height above (3, 3); or add a new one in the June 2025 Q6 shape. Update the checks.
- [ ] math.fm.vectors2: the first `(Exam style)` example (line meets plane, then "(b) the acute angle") uses \(\sin\varphi = |\mathbf{b}\cdot\mathbf{n}|/(|\mathbf{b}||\mathbf{n}|)\) "from the next section", before it is taught. Move the whole example to the end of "The angle between a line and a plane" (after the warn "Sine, not cosine") and drop the forward-reference sentence.
- [ ] math.fm.polar: the third `(Exam style)` example (circle r = 4cos θ cut by the line r = 3sec θ) has the same geometry and the same answer, 4π/3 − √3, as the example just before it (r = 2 and r = sec θ). Change its numbers so the segment and the answer differ (for example the circle r = 8cos θ and the line r = 2sec θ, meeting at θ = ±π/3, with the region of the circle to the right of the line: 32π/3 + 4√3, which contains the centre), redo the working and its check line, and update checks/math.fm.polar.py.
- [ ] fm-polar (widgets/fm-polar.js): the θ slider has step 0.01, so its end is θ = 6.280, not 2π: with "Shade the area" on, the full cardioid reads 4.7060 instead of 3π/2 = 4.7124 (the chapter tells students to check 3π/2 there). Make the last step land exactly on the range end (step = range/N, or snap the maximum). Also the "initial line" label is drawn over the curve at (2, 0) and hides the tick "2": put it beyond the outermost ring.
- [ ] fm-matrix (widgets/fm-matrix.js): the view is fixed at about −10 to 10, so in the first embed of math.fm.transform (unit square, shear 1, 2, 0, 1) the square and its image fill a tiny corner of the grid. Scale the view to fit the object and its image (with a minimum of about ±3) and keep it fixed while a preset animates. At phone width the inputs wrap as a, b, c on one row and d alone below: lay them out as a 2×2 grid (a b / c d), like the matrix.
- [ ] fm-planes (widgets/fm-planes.js): in math.fm.vectors (`data-planes="3,-2,1,6"`) the default view looks almost along the plane, so the plane is a thin sliver and its normal lies flat across the screen. Choose the starting view from the planes (turn until the first normal makes at least about 30° with the screen), and print distances to 3 s.f. ("1.60", not "1.6").
Reviewer's notes (no action): the Writers' notes are confirmed. P19: MF19 lists Σr, Σr², Σr³ but not partial fractions or
differences; the board box holds (Pearson's June 2024 WFM01 examiner report names the method of differences); the
link to math.fm.induction is there. P20: fm-matrix in dark mode and Show A⁻¹ by keyboard work. P21: drawing only
r ≥ 0 matches FACTS 1.5a and the 2027 specimen paper (polar curve given on 0 ≤ θ ≤ π); fm-polar in dark is fine;
graphs now has a 9231-only board box. P22: fm-planes in dark is fine; the skew-lines figure now breaks l₁ behind l₂
and the line–plane figure has its right-angle mark off the line. Fixed in this review: polar (bearing sentence, cusp
wording, cosec notation, MF19 double-angle wording, figure crop), vectors and vectors2 quiz explanations, plot labels in rational and graphs, the series partial-sums caption. FACTS.md
now records the 2027 specimen Paper 1 (printed answer booklet).
