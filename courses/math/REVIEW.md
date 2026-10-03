# REVIEW: Mathematics

Findings for the Writer, newest review at the bottom. One item per line:
`- [ ] <chapter-id>: <exactly what to change>`. The Writer fixes it and changes `[ ]` to `[x]`.
While any `- [ ]` line is open, `status` says FIX.


## REVIEW P1–P2 (2026-10-03)
- [x] math.p1.series: add one worked example in a real context (a salary rising by a fixed amount each year as an AP, and a car value falling by a fixed percentage each year as a GP), including "in which year does it first exceed / fall below …" found by testing values. Add a fifth quiz question on the GP condition b² = ac or on when S∞ exists, with distractors that are real slips.
- [x] math.p1.trig: in the plot of y = tan x and y = tan(x + 45°), add `--vline 90 --vline 270` so the asymptotes of y = tan x are visible. Add one worked example on a negative interval (e.g. solve 3 sin x = 2 for −180° ≤ x ≤ 180°, or a radian interval −π ≤ x ≤ π) that starts by sketching the graph and the horizontal line to count the solutions.
- [x] math.f.geometry: in the special-triangles SVG and the triangle-ABC SVG, change the label class `ts` to `tl` (add `halo` where a label touches a line) and crop each viewBox to the drawing plus about 15 px, so labels are readable at phone width.
- [x] math.p1.circular: add one exam-style worked example where the sector angle must first be found from a triangle with the cosine rule (three sides known, e.g. OA = OB = 7, AB = 10), then used for the arc, the sector and the segment (syllabus 1.4: lengths and angles in triangles).

## REVIEW P3–P4 (2026-10-03)
- [x] math.p3.integ: in "Overestimate or underestimate?", add a hand SVG (`fig wide`, two panels): a convex curve (e.g. y = 1/x² on 1 ≤ x ≤ 3) with 4 trapezia whose tops lie above the curve, labelled "overestimate", and a concave curve (e.g. y = ln x) with chords below it, labelled "underestimate". Use `tl` labels. Add one sentence that syllabus 2.5 accepts a sketch of the curve as the reason, so a second derivative is not always needed.
- [x] widgets.js (iteration): format very large or very small values like the others: a Unicode minus and "× 10ⁿ" (e.g. via W.fmt) instead of "-7.179e+8" and "-1.850e+26" in the table and "Last value".

## REVIEW P5–P6
No open items: the three wording fixes were made directly (see STATUS.md).

## REVIEW P7–P8
- [x] math.m.energy: the last worked example "(Exam style) A car of mass 1200 kg ... sin θ = 1/20 ... 60 kW ... 1500 N" repeats the earlier car-on-a-hill example with the same numbers. Give it new values (e.g. 1500 kg, 45 kW, resistance 900 N, sin θ = 1/30, acceleration asked at 15 m/s), recompute every answer and its marks, and update checks/math.m.energy.py.
- [x] math.m.momentum: quiz question 1 shows units only on the correct option ("12 kg m s⁻¹"), which gives it away. Write all four options the same way: "7 kg m s⁻¹", "1.33 kg m s⁻¹", "12 kg m s⁻¹", "6 kg m s⁻¹" (or none with units).
