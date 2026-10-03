# COURSE: Mathematics (math)

Written by the Specialist (LEAD, 2026-10-03). Writers: read this file, kit/STYLE.md and the gold chapter
before every package. Exam facts and the syllabus learning outcomes are in FACTS.md: cover every outcome
listed for your chapter, and nothing marked "Not:" except in a clearly labelled board note.

## Scope and boards
- Main board: **Cambridge International AS & A Level Mathematics 9709** (syllabus 2026–2027). Papers: P1 and P3
  Pure, P2 Pure (AS only), P4 Mechanics, P5 Probability & Statistics 1, P6 Probability & Statistics 2.
- One chapter per syllabus topic, in syllabus order inside each group. P2 and P3 share chapters (`math.p3.*`):
  the AS-level parts come first, and anything that is Paper 3 only sits under a heading ending
  "(Paper 3 only)", e.g. `### Differentiating tan⁻¹ x (Paper 3 only)`. Chapters at level `a2` are wholly P3/P6.
- Further Mathematics 9231 appears only in the tour chapter `math.further`.
- Other boards go in one `:::board` box per chapter, 2–6 lines. Only state differences you are sure of:
  - **Edexcel IAL** (units P1–P4, M1–M3, S1–S3, D1): IAL mechanics uses g = 9.8; IAL puts complex numbers in
    Further Maths; projectiles and moments are in IAL M1/M2; regression and correlation are in IAL S1.
  - **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: three mixed 2-hour papers; proof; large data set;
    regression and hypothesis tests on correlation; projectiles and moments; no Poisson, no complex numbers
    (both are UK Further Maths); g = 9.8.
  - If you are not sure how another board treats a topic, say less, not more.

## Data values and conventions
- Mechanics: **take g = 10 m s⁻²** and say "Take \(g = 10\)" in every question that needs it. Mention once per
  mechanics chapter (in the board box) that Edexcel and UK boards use 9.8.
- Accuracy: 3 significant figures unless exact; angles in degrees to 1 d.p. Work with full calculator values and
  round only the final answer; in a multi-step example show intermediate values to 4 s.f.
- Probabilities to 3 s.f. (4 s.f. only when a question asks for it). Normal-table values: use the exact Φ
  (`statistics.NormalDist`) and round, as a candidate using the table's 4 d.p. would get the same 3 s.f.
- Notation (match MF19 and Cambridge papers): \(\dfrac{dy}{dx}\), \(\dfrac{d^2y}{dx^2}\), \(f'(x)\), \(f''(x)\);
  \(\int \ldots \,dx\) with a thin space; \(\ln x\) (never \(\log_e\)); \(\sin^{-1}x\) for inverse trig;
  \(\binom{n}{r}\) for combinations, with \({}^{n}C_{r}\) mentioned once in Series and Perms;
  probability and distributions as in the finished chapters: \(P(A)\), \(P(A \mid B)\), \(A'\), \(B(n, p)\),
  \(\mathrm{Geo}(p)\), \(\mathrm{Po}(\lambda)\), \(N(\mu, \sigma^2)\), \(E(X)\), \(\mathrm{Var}(X)\), \(\Phi(z)\).
  Vectors: bold \(\mathbf{a}\), \(\overrightarrow{AB}\), columns with `pmatrix`, \(\mathbf{i}, \mathbf{j}, \mathbf{k}\).
  Complex: \(z^*\), \(\mathrm{Re}\,z\), \(\mathrm{Im}\,z\), \(|z|\), \(\arg z\) with \(-\pi < \arg z \le \pi\).
- Exam command words to model in examples: "show that", "hence", "exact", "express in the form", "state",
  "find the set of values", "sketch", "verify".
- MF19 is given in the exam (FACTS.md lists it). Each chapter's `:::exam` or `:::tip` says which of its formulas
  are on MF19 and which must be learned.

## Depth, tone and structure
- Follow the gold chapter **math.p1.diff** and the guide model math.p1.quadratics (kit/EXAMPLE.md). A typical
  P1/P3 topic chapter is 2500–4000 words with 8–14 worked examples, 8–10 try questions and 4–5 quiz questions.
  Big topics (Further integration techniques, Vectors, Complex numbers, Normal distribution) can run longer.
  Foundations (`pre`) chapters: 1800–2800 words, IGCSE level, ending at the point where the P1 chapter starts.
- Every chapter teaches from zero: plain idea → definitions → rule in a `:::key` box → examples from one-step
  to full exam question. At least **two** exam-style worked examples with `[M1] [A1] [B1]` marks per A Level
  chapter, written the way a mark scheme would credit them, and an exam-style try question at the end.
- Worked examples show every algebra line a student would need. Use `\begin{aligned}` for chains of working.
  End examples with a check where one is natural (substitute back, sketch sense check, units).
- Try answers: key steps and the final answer, not just a number. Put marks on the exam-style ones.
- Quiz distractors are real misconceptions (sign slips, forgetting the chain rule factor, using variance for
  standard deviation, degrees vs radians), and the explanation names the slip.
- `:::warn` for the 2–3 most common lost marks on the topic (examiner-report style, in our own words).
  `:::exam` for command words, accuracy, and what earns method marks.
- Tone: warm, direct, short sentences, "you". No history lessons beyond one sentence; no filler.
- Original questions only: invent fresh numbers; never reproduce past-paper questions.

## Figures and widgets
- Function graphs: **use `:::plot`** (see kit/STYLE.md). Do not hand-write long SVG paths for curves (the older
  drafts did; new chapters should not). Typical: one or two plots per Pure chapter.
- Hand SVG only for geometry, force diagrams, Argand loci, tree diagrams, box plots, histograms, v–t graphs made
  of straight segments, vector diagrams. Keep to the classes in kit/STYLE.md; check coordinates with Python.
  One or two per chapter at most.
- Embed a widget only where it teaches something a static figure cannot, with a sentence saying what to try.

## Chapter notes
P1–P6 are written and reviewed, so their notes were removed. Notes remain for the chapters still to write.

### Probability and Statistics
- **math.s2.linear**: \(E\) and \(\mathrm{Var}\) of \(aX + b\) and \(aX \pm bY\), sums of independent normals,
  the classic "\(X_1 + X_2\) vs \(2X\)" distinction, sums of Poissons.
- **math.s2.crv**: pdf properties, finding \(k\), probabilities as areas, mean, variance, median and percentiles,
  infinite domains (\(\frac{3}{x^4}\), \(x \ge 1\)). `:::plot` of a pdf with `--shade`.
- **math.s2.sampling**: populations and samples, randomness, unbiased estimates, \(\bar X\) distribution, CLT,
  confidence intervals for a mean and a proportion, interpreting intervals.
- **math.s2.hypothesis**: language, one/two-tailed, binomial and Poisson tests by direct probability and critical
  regions, normal approximations, test for a mean, Type I/II errors and their probabilities. Conclusions in
  context, never "accept H₀ is true".
- **math.s.regression** (ext): scatter diagrams, PMCC interpretation, least squares line from summary statistics
  (Edexcel IAL S1 style), interpolation vs extrapolation, UK hypothesis test for correlation in brief.

### Mechanics (take g = 10)
- **math.m.forces** (done; add a `resultant` widget after P8 builds it).
- **math.m.kinematics**: displacement, velocity, acceleration; s–t and v–t graphs (hand SVG of a trapezium v–t
  graph); suvat with direction conventions; two-particle problems; variable acceleration with calculus.
- **math.m.newton**: \(F = ma\), weight, motion on slopes (rough, up vs down), lifts, connected particles over a
  pulley and car–trailer (tension vs thrust), resistance, particle hitting the ground and string going slack.
- **math.m.momentum**: momentum, conservation, coalescing, direction changes; no impulse or restitution
  (mention them in the board box).
- **math.m.energy**: work done \(Fd\cos\theta\), KE, GPE, work–energy principle with resistances, curved paths,
  power \(P = Fv\), car on a hill with maximum speed and instantaneous acceleration.
- **math.m.projectiles** (ext): projectile motion, range, max height, trajectory equation, moments and
  equilibrium of a rigid rod. Embed `projectile`.
- **math.further** (ext): 9231 paper table from FACTS.md; one mini worked example per Further topic
  (induction, matrices, roots of polynomials, method of differences, polar, hyperbolic functions, Maclaurin
  series, de Moivre, second-order DEs); who should take it.

## Widgets
Existing (do not rename): `graph` (data-fns "f; g" up to 4, data-x "a,b", data-y "a,b", data-params
"a=1,-3,3,0.1; b=…", data-labels "…; …", data-points "x,y; x,y", data-deg, data-edit, data-h),
`unitcircle` (data-angle, data-rad), `stats` (data-values "3, 5, 7"). The Toolbox uses `graph`: never change
its attributes.

New widgets (build in the package named; follow kit/WIDGETS.md):
- Built and reviewed: **iteration** (P4), **argand** (P5), **discrete** and **normal** (P6). Embed them with the
  attributes used in existing chapters (grep `data-w="normal"` in chapters/); do not rebuild them.
- **projectile** (P8): speed, angle, launch height 0–20 m, g presets 10 / 9.8 / 9.81 (default 10); range, time
  of flight, max height; velocity components at a chosen time; launch animation (static under reduced motion);
  faint previous paths and a clear button.
- **resultant** (P8): up to 4 forces given as magnitude and angle (degrees from the positive x-axis); draws them
  from one point, shows the resultant (magnitude 3 s.f., direction 1 d.p.) and the component sums ΣX, ΣY;
  a checkbox "add the balancing force" draws the equilibrium force. `data-forces "12@0; 10@120"`.

## Rules added after REVIEW P1–P2 (apply from P3 on)
- **No exam-frequency or mark claims** ("worth 6 to 8 marks", "appears every year", "about 10 marks") unless
  FACTS.md states them. Five chapters had invented ones; they were removed.
- **Edexcel IAL units** (use these, or write "Edexcel IAL Pure" if unsure): P1 lines, radians/arcs/sectors,
  sine and cosine rules, trig graphs, basic differentiation and integration; P2 factor theorem and division,
  circles, binomial (positive n), AP/GP, trig identities and equations, exponentials and logs, stationary
  points, definite integrals and the trapezium rule; P3 functions and transformations, modulus, sec/cosec/cot,
  compound angles and R-form, eˣ and ln x, chain/product/quotient rules, numerical methods, further
  integration; P4 partial fractions, binomial for rational n, parametric and implicit differentiation,
  integration techniques, differential equations, vectors. Statistics: S1 data, probability, correlation and regression, discrete random variables, the normal distribution; S2 binomial and Poisson, continuous random variables, continuous uniform, hypothesis tests; S3 combinations of random variables, sampling, confidence intervals, chi-squared, Spearman. Mechanics: M1 kinematics, forces and friction, Newton laws, momentum and impulse, moments; M2 projectiles, work, energy and power, centres of mass, variable acceleration.
- **Figures**: SVG labels use `tl` (keep `ts` for axis tick numbers only), with `halo` where a label touches a
  line; crop the viewBox to the drawing plus about 15 px. Look at every figure at phone width before finishing.
- **Never edit chapter text through a Python heredoc** (`py - <<EOF`): it turns `\t` in `\tfrac` into a tab and
  silently breaks the maths. Use the Write and Edit tools.
- Each A Level chapter has at least one worked example in a real context, and trig-based chapters include at
  least one negative or radian interval.
- The `Next:` line follows course.json order (Series → Differentiation, not Integration).
- **"On MF19" claims**: check the MF19 list in FACTS.md before writing one. The trapezium rule and the laws of
  logarithms are NOT on MF19; ∫xⁿ dx, the product, quotient and parametric rules, the R-form's parts
  (compound angles) and the binomial series ARE. (Added after REVIEW P3–P4, which found two wrong claims.)
- Depth: P1–P2 chapters came in at 1600–2300 words with full syllabus coverage. Coverage and worked examples
  matter more than word count, but do not stop at the minimum: build each section from one-step to exam level.
- **Board boxes** (added after REVIEW P5–P6): never write in the first person ("I have not listed…"). For
  statistics, use the IAL S1/S2/S3 split above (the binomial distribution is IAL S2, not S1).

## Saving tokens (Writers: follow these, every message re-sends the whole session)
- **widgets.js is about 100 KB: never Read it whole.** Find the end with `grep -n "W.register" widgets.js`
  and `tail -n 15 widgets.js`, then add a new widget with one Edit just before the closing lines. To copy a
  pattern, Read only that widget's range (offset/limit).
- FACTS.md: grep the topic number (`grep -n "^- 5.4" FACTS.md`) instead of reading it. Never open other chapters.
- Browser: test with `javascript_tool` probes first (scrollWidth vs innerWidth, text containing NaN or
  undefined, `merror` count). Take screenshots only at `scale: 0.5`, at most one per widget per mode
  (light, dark, phone). Don't screenshot chapter pages unless a probe flags something.
- Run `check <id>` for the chapter you just wrote, not `check` for the whole course.

## v2: exam-readiness upgrade (LEAD v2, 2026-10-03; packages P9–P18)
The course teaches every outcome but is short of practice, exam training and proofs. v2 adds them. The engine
blocks requested in REQUESTS.md all exist (Organizer, 2026-10-03; syntax in kit/STYLE.md): `:::links`,
`:::proof`, `:::checklist`, `:::progress`, `H:` hints and `Q: [n marks] (#id)` in `:::try`, `@level mock`,
practice by paper (`papers` in course.json), and the widget helpers, `widgets/<name>.js` files and `--probe`
(kit/WIDGETS.md).

### Learn more online (every chapter; written by the Specialist)
Every chapter ends `:::recap` → `:::links` → `Next:`. Lines: `- watch: [Title](https://…) · Site · one-line
reason`, kinds watch / practise / explore / read / papers, tags `[paid]` and `[unofficial]`; a last plain line
"Links checked <date>." The boxes also build the page tools.l.math. Writers keep this box when editing and never
add unverified URLs. New links go in only after the Specialist's link check (HTTP 200, not a login or home page).

### New sections in every topic chapter (P10–P16, Writers)
Add them; don't rewrite the existing teaching. Order inside the chapter:
1. **Warm-up** right after "Before you start": `:::try Warm-up` with 3 quick questions from *earlier*
   chapters (course.json order), answers one line each, each naming its chapter.
2. **Proofs** in place, next to the rule they prove: `:::proof <what it proves>` (folded, badged "Not examined
   in 9709"; it never counts towards the checklist minimums). Short (5–12 lines) at the student's level, a reason on every line, ending with what it shows.
   Examinable proofs (trig identities, "show that" results) stay as `:::eg` with marks. The proof list per
   chapter is in the plan table below. Check each proof's algebra numerically in `checks/<id>.py` (identities
   at 3+ random values, sums against direct summation).
3. **Spot the error** before the try block: `:::eg Spot the error` showing a student's marked answer with
   one realistic slip; the working names the line, the lost mark (e.g. "A0: sign error") and the fix.
4. **Exam practice** after the existing try block: `:::try Exam practice ★ to ★★★` with 6–8 original
   exam-style questions (★ one method, ★★ two steps, ★★★ multi-part or synoptic), [n marks] in each `Q:`,
   and answers with M/A/B marks on the line that earns them. At least one ★★★ uses an earlier chapter's skill.
5. **Stretch for A\***: `:::try Stretch for A*`, 1–2 problems in an unfamiliar context (P3 is 55% AO2), with
   full solutions.
6. Leave the quiz, recap, links box and Next line as they are (add 1–2 quiz items if the chapter has < 5).
- Thin chapters (inttech, diffeq, vectors, complex, perms, prob, drv, normal): at least two more fully marked
  long exam examples (`:::eg (Exam style)`, 8–12 marks, several parts).
- Every new number goes into `checks/<id>.py`. Expect +1200–2000 words per chapter.

### Proofs per chapter (★ = embed the `proof` widget scene)
f.geometry: Pythagoras ★pythagoras, angle sum, sine rule, cosine rule ★cosinerule, ½ab sin C ·
f.powers: index laws; √2 irrational · p3.logs: laws of logs from index laws ·
p1.quadratics: completing the square ★completesquare → formula; discriminant; sum and product of roots ·
p1.functions: f⁻¹ as the reflection in y = x ★inverse · p1.coord: distance; m₁m₂ = −1 ★perp; circle equation ·
p1.circular: s = rθ, A = ½r²θ ★sector · p1.trig: sin² + cos² = 1 (embed `unitcircle`) ·
p3.trig: sin(A + B) ★compound, double angles, R-form · p1.series: AP sum ★apsum, GP sum ★gpsum, S∞,
Pascal's rule ★pascal · p1.diff: d/dx xⁿ (positive integer n) from the chord ★chordlimit; chain rule idea ·
p1.integ: area function's slope is f ★ftc; volume as discs ★discs · p3.diff: eˣ ★expderiv, sin x ★sinlimit,
product rule ★productrule, quotient from product + chain · p3.integ/inttech: by parts from the product rule,
∫f′/f, substitution from the chain rule · p3.partial: cover-up rule · p3.numerical: sign change and when it
fails · p3.vectors: a·b = |a||b|cos θ ★dotcosine · p3.complex: conjugate roots; modulus multiplies, args add
(embed `argand`) · p3.diffeq: separation via the chain rule · s1.perms/s1.prob: n!, ⁿCᵣ = ⁿPᵣ/r!,
multiplication rule ★tree · s1.drv: E(X) = np, E = 1/p for Geo(p) · s2.linear: E and Var of aX + b,
Var = E(X²) − μ² · s2.poisson: limit of B(n, λ/n) (embed `discrete`) · m.kinematics: suvat from the v–t graph
(embed `vt`) and by integration · m.energy: work–energy from F = ma · m.momentum: conservation from Newton 3 ·
m.projectiles: trajectory is a parabola; 45° maximum range (embed `projectile`).

### New chapters
- **math.calc** (guide, P9): degree/radian mode trap; full accuracy with ANS and memories; table mode for
  iteration, the trapezium rule and sign changes; stats mode for x̄, σ, Σx, Σx², regression; binomial, Poisson
  and normal functions **as checks** (the table/standardisation must still be shown); the equation solver as a
  check. Casio fx-991EX/fx-991CW and TI-30X Pro only, with key steps checked against the makers' manuals; if
  unsure of a keystroke, describe the menu in words. Opens with FACTS "Equipment" and "no marks for unsupported
  answers". Use a `:::tip` per model rather than long keystroke lists.
- **math.exam.skills** (guide, P9): show that / hence / hence or otherwise / exact / verify / state / sketch
  in maths; M, A, B and follow-through marks, and why "A1 cao" is lost; accuracy (3 s.f., 1 d.p., 4 s.f. working);
  presenting long answers; links to road.commands and road.technique.
- **math.exam.p1 / p23 / p4 / p5 / p6** (guide, P9): duration and marks (FACTS) → minutes per mark; which
  routes include the paper; the paper's MF19 entries and what must be learned; a topic list linking each
  chapter; the top lost marks gathered from the chapters' `:::warn` boxes; a 10-item final-week checklist.
  **No** grade boundaries, question-position or frequency claims.
- **math.proof** (ext, P16): deduction, exhaustion, counter-example, contradiction (√2, infinitely many
  primes), a taste of induction; board box: the UK A Level examines proof, 9231 examines induction.
- **Mixed practice** `math.mixed.*` (ref, P17–P18): 25–35 short, interleaved questions ordered ★ → ★★★, each
  `Q: [n marks] (#math.p1.quadratics) …` (the page shows "Revise: Quadratics" under the answer), answers with marks.
- **Mocks** `math.mock.pNa` (`@level mock`, P17–P18; kit/STYLE.md "Mock papers"): one original full paper. Marks and
  time **exactly** as FACTS (P1, P3 75 marks 1 h 50; P2, P4, P5, P6 50 marks 1 h 15) in `@time`; 9–11
  questions rising in difficulty, every syllabus area of the paper covered, the last two questions long and
  synoptic. Layout: `:::exam` instructions (MF19 allowed, calculator rules, 3 s.f.), then questions as one
  `:::try` per question, `Q: [n marks] (#chapter-to-revise) …`, the answer being the full mark scheme (M/A/B per line, accepted
  alternatives in brackets). End with a table "Question → chapter to revise". The check asserts the marks
  total and recomputes every answer. Never reuse past-paper questions or numbers.

### New widgets (kit/WIDGETS.md; test light, dark, phone, bad input)
- **proof** (P10, scenes added in P11–P16): `data-proof="<scene>"`. An SVG diagram plus a list of algebra
  lines; Back/Next buttons (and ←/→ keys) step through them, highlighting the part of the diagram each line uses.
  Sliders where a limit is involved (h → 0 for chordlimit/sinlimit/expderiv, n → ∞ for gpsum, strips for
  ftc/discs); no motion under reduced motion; the final step shows the result in a key-style box. One
  object per scene so new scenes are about 40 lines each.
- **area** (P10): `data-f`, `data-x "a,b"`, `data-n`, mode `riemann | trapezium | volume`; strips with
  the over/under estimate readout and the exact value; the volume mode draws the disc stack in oblique view.
- **graph** (P10): new optional `data-tangent "x0"` (draggable tangent and chord from x0 to x0 + h with an h
  slider) and `data-shade-between "f;g"`. Existing attributes unchanged (the Toolbox uses them).
- **slopefield** (P12): `data-f "x*y"` for dy/dx, axes ranges; draws the field; clicking draws the solution
  through that point (RK4); readout of the point.
- **vectors3d** (P12): `data-lines "a1,a2,a3|d1,d2,d3; …"`, `data-point`; drag to rotate, verdict
  parallel / intersecting (at …) / skew, optional foot of the perpendicular and angle between the lines.
- **sampling** (P14): population (uniform, skewed, normal, Bernoulli p); sample size n; draw 1 / 100 samples;
  histogram of x̄ with the N(μ, σ²/n) curve; CI mode drawing 95% intervals and counting how many contain μ.
- **incline** (P15): `data-angle`, `data-mu`, `data-mass`, applied force P at angle; force diagram with
  R, F, W components; state static / limiting / sliding up or down; acceleration (g = 10); optional second
  mass over a pulley at the top.
- **vt** (P15): `data-segs "0,0; 4,12; 10,12; 14,0"` (t, v points); drag points; shaded area = displacement,
  distance, acceleration of each segment; s–t graph below.

## Gold chapter
**math.p1.diff** (Differentiation, P1). Writers match its structure, depth, mark style and use of `:::plot`.

## Packages
| Package | Chapters | Widgets |
|---|---|---|
| P1 Foundations | overview ✓, f.numbers ✓, f.algebra, f.powers, f.graphs, f.geometry | (graph) |
| P2 Pure 1: functions to series | p1.functions ✓, p1.coord, p1.circular, p1.trig, p1.series | (unitcircle, graph) |
| P3 Pure 1 calculus, P2/3 algebra | p1.diff ✓ gold, p1.integ, p3.algebra, p3.logs, p3.trig | — |
| P4 Pure 2/3 calculus, numerical | p3.diff, p3.integ, p3.numerical, p3.partial | iteration |
| P5 Pure 3 | p3.inttech, p3.diffeq, p3.vectors, p3.complex | argand |
| P6 Statistics 1 | s1.data, s1.perms, s1.prob, s1.drv, s1.normal | discrete, normal |
| P7 Statistics 2, regression | s2.poisson ✓, s2.linear, s2.crv, s2.sampling, s2.hypothesis, s.regression | — |
| P8 Mechanics, Further tour | m.forces ✓, m.kinematics, m.newton, m.momentum, m.energy, m.projectiles, further | projectile, resultant |
| P9 Exam skills | calc, exam.skills, exam.p1, exam.p23, exam.p4, exam.p5, exam.p6 | — |
| P10 Deeper + proofs: Pure 1 | p1.quadratics … p1.integ (8) | proof, area, graph options |
| P11 Deeper + proofs: Pure 2/3 (1) | p3.algebra, logs, trig, diff, integ, numerical | (proof scenes) |
| P12 Deeper + proofs: Pure 3 | p3.partial, inttech, diffeq, vectors, complex | slopefield, vectors3d |
| P13 Deeper + proofs: Stats 1 | s1.data, perms, prob, drv, normal | (proof scene tree) |
| P14 Deeper + proofs: Stats 2 | s2.poisson, linear, crv, sampling, hypothesis, s.regression | sampling |
| P15 Deeper + proofs: Mechanics | m.forces … m.projectiles (6) | incline, vt |
| P16 Foundations, proof, overview | f.* (5), further, proof (new), overview | (proof scenes) |
| P17 Mocks P1–P3, mixed Pure | mock.p1a, p2a, p3a, mixed.pure1, mixed.pure3 | — |
| P18 Mocks P4–P6, mixed applied | mock.p4a, p5a, p6a, mixed.mech, stats1, stats2 | — |

✓ = finished in LEAD: do not rewrite; only add the widget or links the notes ask for.
