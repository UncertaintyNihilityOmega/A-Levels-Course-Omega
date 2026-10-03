# COURSE: Mathematics (math)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Mathematics (9709); Further Mathematics (9231) in one tour chapter
- Syllabus: https://www.cambridgeinternational.org/Images/697427-2026-2027-syllabus.pdf
- Main board Cambridge International; Edexcel IAL, AQA and OCR differences go in :::board boxes.

## Data values and conventions
- Cambridge 9709 Mechanics: take g = 10 m s⁻² and say so ("take g = 10"); Edexcel uses 9.8.
- Answers to 3 significant figures unless exact; angles in degrees to 1 d.p.
- Exam formula list: MF19 (know what is on it and what is not).

## What exists
- math.p1.quadratics is the model chapter for the whole guide (kit/EXAMPLE.md), approved by the user. Five drafts (math.overview, math.f.numbers, math.p1.functions, math.s2.poisson, math.m.forces) were written to old word limits and never reviewed: check them in LEAD. No checks/*.py exist yet.
- widgets.js: graph, unitcircle, stats (built). Old plan also wanted normal, binomial and projectile.

## Widgets other parts of the guide expect from this course
- `graph` is used by the Toolbox graph plotter (core chapter tools.grapher): keep its name and attributes (data-fns, data-x, data-y, data-params, data-edit).

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Suggested merges (old ids become aliases in course.json)
| Keep | New title | Absorbs |
|---|---|---|
| math.f.numbers | Numbers, powers, surds and standard form | math.f.powers |
| math.f.graphs | Graphs, geometry and trigonometry basics | math.f.geometry |

### Old packages (chapter groups, topics, notes)
- **WP1** Maths: course map, foundations, Pure 1 part 1: math.overview, math.f.numbers, math.f.algebra, math.f.graphs, math.p1.functions, math.p1.coord, math.p1.circular, math.p1.trig. Topics: Pure 1: 1.2 Functions, 1.3 Coordinate geometry, 1.4 Circular measure, 1.5 Trigonometry. Notes: math.overview: 9709 paper table, routes and MF19 from PLAN.md; link every maths chapter. Foundations are IGCSE level. Trig embeds the unitcircle widget; functions embeds a graph widget with transformation sliders. NOTE: math.f.numbers was written before the merge: append a '## Powers, roots, surds and standard form' section with an Edit instead of rewriting it. Chapters already done live in content/math-0.md and content/math-1.md (legacy multi-chapter files); write the missing ones as new per-chapter files.
- **WP2** Maths: Series, Differentiation, Integration, P2/P3 algebra, logs, trig: math.p1.series, math.p1.diff, math.p1.integ, math.p3.algebra, math.p3.logs, math.p3.trig. Topics: 1.6 Series, 1.7 Differentiation, 1.8 Integration; 2.1/3.1 Algebra, 2.2/3.2 Logarithmic and exponential functions, 2.3/3.3 Trigonometry. Notes: Chain rule and volumes of revolution are in P1. In P2/P3 chapters mark Paper 3-only parts clearly.
- **WP3** Maths: Pure 3: math.p3.diff, math.p3.integ, math.p3.numerical, math.p3.vectors, math.p3.diffeq, math.p3.complex. Topics: 3.4 Differentiation, 3.5 Integration, 3.6 Numerical solution of equations, 3.7 Vectors, 3.8 Differential equations, 3.9 Complex numbers. Notes: Newton-Raphson only as a UK-board note. Complex: one hand SVG for an Argand-diagram locus.
- **WP4** Maths: Probability and Statistics 1: math.s1.data, math.s1.perms, math.s1.prob, math.s1.drv, math.s1.normal, math.s.regression. Topics: 5.1 to 5.5 (Probability and Statistics 1). Notes: Probabilities to 3 s.f. Widgets: stats, binomial, normal. Regression is Edexcel IAL S1 / UK only: say so.
- **WP5** Maths: Probability and Statistics 2, Further Maths tour: math.s2.poisson, math.s2.linear, math.s2.crv, math.s2.sampling, math.s2.hypothesis, math.further. Topics: 6.1 to 6.5 (Probability and Statistics 2). Notes: math.further: 9231 paper table from PLAN.md and one mini worked example per Further topic (induction, matrices, roots, method of differences, polar, hyperbolic, Maclaurin, de Moivre, 2nd-order ODEs).
- **WP6** Maths: Mechanics: math.m.forces, math.m.kinematics, math.m.newton, math.m.momentum, math.m.energy, math.m.projectiles. Topics: 4.1 to 4.5 (Mechanics). Notes: Take g = 10 (Cambridge 9709). Projectiles and moments are Edexcel IAL M2 / UK (Cambridge has projectiles in Further Mechanics): say so; projectile widget. One force-diagram SVG per chapter at most.

### Old widget specs
- normal: mu, sigma, a, b; shade between/below/above; probability to 4 s.f.; Phi via erf with error < 1e-7. binomial: n 1-50, p; bars; highlighted range with cumulative probability; mean np, variance np(1-p); optional normal overlay. projectile: speed, angle, launch height 0-20 m, g presets 9.81/9.8/10; range, time of flight, max height; components at a chosen time; launch animation (respect reduced motion); faint previous paths + clear. wave: data-mode single (A, wavelength, f, v = f lambda) | superpose (two waves + resultant) | stationary (string fixed at both ends, harmonic slider, nodes/antinodes); play/pause, paused under reduced motion. halflife: n0, half-life; dashed half-life markers; lambda = ln2/t_half; N at a chosen t; seeded random decay of up to 400 dots vs the smooth curve.
