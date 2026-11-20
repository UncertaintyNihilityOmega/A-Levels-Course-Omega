# COURSE: Mathematics (math)

Rules for every session in this course (Specialist, Writers, Readers). Read this file, kit/STYLE.md and the gold
chapter **math.p1.diff** before every package. Exam facts and the syllabus learning outcomes are in FACTS.md: cover
every outcome listed for your chapter, and nothing marked "Not:" except in a clearly labelled board note. History
(earlier plans, review findings, package tables) lives in git; this file holds rules only.

## Scope and boards
- **Mathematics 9709** (Cambridge International AS & A Level, syllabus 2026–2027): P1 and P3 Pure, P2 Pure (AS
  only), P4 Mechanics, P5 Probability & Statistics 1, P6 Probability & Statistics 2. Chapters `math.f.*`
  (foundations), `math.p1.*`, `math.p3.*`, `math.m.*`, `math.s1.*`, `math.s2.*`, guides, mixed practice, mocks.
- P2 and P3 share chapters (`math.p3.*`): the AS-level parts come first; anything that is Paper 3 only sits under a
  heading ending "(Paper 3 only)". Chapters at level `a2` are wholly P3/P6.
- **Further Mathematics 9231** is an extension inside this course: chapters `math.fm.*`, sidebar groups
  per 9231 paper (FURTHER.md), `@level fm`, packages P19 onwards. They build on the Maths chapters: link them
  (`[Complex numbers](#math.p3.complex)`) instead of re-teaching. Its plan and rules are in FURTHER.md (the
  extension's LEAD writes them); the rules in this file apply to it too unless FURTHER.md says otherwise.
- Other boards go in one `:::board` box per chapter, 2–6 lines, never in the first person. Only state differences
  you are sure of; if unsure, say less.
  - **Edexcel IAL**: g = 9.8. Pure units: P1 lines, radians/arcs/sectors, sine and cosine rules, trig graphs, basic
    differentiation and integration; P2 factor theorem and division, circles, binomial (positive n), AP/GP, trig
    identities and equations, exponentials and logs, stationary points, definite integrals, trapezium rule; P3
    functions and transformations, modulus, sec/cosec/cot, compound angles and R-form, eˣ and ln x,
    chain/product/quotient rules, numerical methods, further integration; P4 partial fractions, binomial for
    rational n, parametric and implicit differentiation, integration techniques, differential equations, vectors.
    S1 data, probability, correlation and regression, discrete random variables, normal; S2 binomial and Poisson,
    continuous random variables, continuous uniform, hypothesis tests; S3 combinations of random variables,
    sampling, confidence intervals, chi-squared, Spearman. M1 kinematics, forces and friction, Newton's laws,
    momentum and impulse, moments; M2 projectiles, work, energy and power, centres of mass, variable acceleration.
    Complex numbers are IAL Further Maths. If unsure of a unit, write "Edexcel IAL Pure".
  - **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: three mixed 2-hour papers; proof; large data set; regression
    and hypothesis tests on correlation; projectiles and moments; no Poisson, no complex numbers (both UK Further
    Maths); g = 9.8.

## Data values and conventions
- Mechanics: **take g = 10 m s⁻²** and say "Take \(g = 10\)" in every question that needs it; the board box says
  once per mechanics chapter that Edexcel and UK boards use 9.8.
- Accuracy: 3 significant figures unless exact; angles in degrees to 1 d.p. Work with full calculator values and
  round only the final answer; in multi-step examples show intermediate values to 4 s.f.
- Probabilities to 3 s.f. (4 s.f. only when asked). Normal-table values from the exact Φ (`statistics.NormalDist`),
  rounded. Critical values, z-values and percentage points are computed in `checks/<id>.py` from exact quantiles
  (`NormalDist().inv_cdf`), never from rounded inputs.
- Notation (match MF19 and Cambridge papers): \(\dfrac{dy}{dx}\), \(\dfrac{d^2y}{dx^2}\), \(f'(x)\), \(f''(x)\);
  \(\int \ldots \,dx\) with a thin space; \(\ln x\) (never \(\log_e\)); \(\sin^{-1}x\); \(\binom{n}{r}\) (mention
  \({}^{n}C_{r}\) once); \(P(A)\), \(P(A \mid B)\), \(A'\), \(B(n, p)\), \(\mathrm{Geo}(p)\), \(\mathrm{Po}(\lambda)\),
  \(N(\mu, \sigma^2)\), \(E(X)\), \(\mathrm{Var}(X)\), \(\Phi(z)\). Vectors: bold \(\mathbf{a}\),
  \(\overrightarrow{AB}\), columns with `pmatrix`, \(\mathbf{i}, \mathbf{j}, \mathbf{k}\). Complex: \(z^*\),
  \(\mathrm{Re}\,z\), \(\mathrm{Im}\,z\), \(|z|\), \(\arg z\) with \(-\pi < \arg z \le \pi\).
- Command words to model: "show that", "hence", "hence or otherwise", "exact", "express in the form", "state",
  "find the set of values", "sketch", "verify".
- Formula booklets: MF19 (9709) is given in the exam; FACTS.md lists what is on it. Check the list before any
  "on MF19" claim (the trapezium rule and the laws of logarithms are NOT on MF19). Each chapter's `:::exam` or
  `:::tip` says which of its formulas are given and which must be learned.
- **No exam-frequency, mark or grade-boundary claims** ("worth 6 to 8 marks", "appears every year") unless
  FACTS.md states them.

## Depth, tone and structure
- Chapters are long and comprehensive (user rule). A topic chapter is typically 4000–6000 words with 8–14 worked
  examples; coverage and examples matter more than word count, but build every section from one-step to exam level.
- Every chapter teaches from zero: plain idea → definitions → rule in a `:::key` box → examples from one-step to
  full exam question. At least two `:::eg (Exam style)` worked examples with `[M1] [A1] [B1]` marks, written the way
  a mark scheme credits them; at least one example in a real context; trig chapters include a negative or radian
  interval. Worked examples show every algebra line, with `\begin{aligned}` for chains, and end with a check where
  natural.
- Tone: warm, direct, short sentences, "you". At most one sentence of history; no filler.
- Original questions only: fresh numbers, never past-paper questions.
- `:::warn` for the 2–3 most common lost marks (in our own words); `:::exam` for command words, accuracy and
  method marks. Quiz distractors are real misconceptions and the explanation names the slip.

### Sections of a topic chapter, in order
1. Before you start, then **Warm-up**: `:::try Warm-up`, 3 quick questions from earlier chapters (course.json
   order), one-line answers each naming its chapter.
2. The teaching, with **proofs** in place next to the rule they prove: `:::proof <what it proves>` (folded, badged
   "Not examined"; never counts towards checklist minimums), 5–12 lines, a reason on every line. A proof the exam
   examines ("show that", trig identities, proof by induction in 9231) is an `:::eg` with marks instead. Check every
   proof's algebra numerically in `checks/<id>.py`.
3. **Spot the error**: `:::eg Spot the error`, a student's marked answer with one realistic slip; the working names
   the line, the lost mark and the fix. A wrong formula or method scores M0 (and so A0); an arithmetic slip inside a
   right method keeps the M1; later parts earn follow-through (ft).
4. The try block, then **Exam practice**: `:::try Exam practice ★ to ★★★`, 6–8 original questions `Q: [n marks] ★★ …`
   (★ one method, ★★ two steps, ★★★ multi-part or synoptic), answers with M/A/B marks on the line that earns them. At
   least one ★★★ uses an earlier chapter's skill and carries `(#that-chapter)`; every ★★★ has 2–3 `H:` hints.
5. **Stretch for A\***: `:::try Stretch for A*`, 1–2 problems in an unfamiliar context, with hints and full solutions.
6. Quiz (at least 5 items).
7. **I can…**: `:::checklist What you can now do`, 5–10 concrete lines `- [ ] I can …`, one per learning outcome.
8. `:::recap` → `:::links` → `Next:` (course.json order).

### Marks
- Write every mark as its own `[M1]`, `[A1]`, `[B1]` token on its line (never inside `\( … \)`, never
  "[M1 for two correct]"). The tokens in each answer add up to its `[n marks]`; in Spot the error, name each mark of
  the scheme once, so the marks shown, the `[n marks]` and the "scores k out of n" sentence agree. When you add to a
  chapter, recount the marks of its older examples too.

### Phone width
- Inline \( … \) does not wrap on phones: one relation per inline piece (about 30 characters), "\(a = b\), so
  \(c = d\)"; chains of three or more steps go in `\[\begin{aligned} … \end{aligned}\]`, also inside try answers.
- Row breaks in `aligned` are `\\` (check scripts that write LaTeX for lost backslashes).
- `node kit/zta.js phone <ids>` must pass. With the browser at mobile width, this lists any inline maths still too
  wide: `document.querySelectorAll('details').forEach(d=>d.open=true); [...document.querySelectorAll('math:not([display=block])')].filter(m=>m.getBoundingClientRect().right>377).map(m=>m.textContent.slice(0,50))`

### Links and naming
- Name chapters by title and link them: "as in [Further trigonometry](#math.p3.trig)".
- Every chapter ends with a `:::links` box (lines `- watch: [Title](https://…) · Site · reason`, kinds watch /
  practise / explore / read / papers, tags `[paid]` and `[unofficial]`, last line "Links checked <date>."). The boxes
  build the page tools.l.math. Writers keep the box when editing and add only URLs the Specialist has checked
  (HTTP 200, not a login or home page).

### Before `done`
- Count the `:::eg (Exam style)` examples of each chapter (`grep -c ":::eg (Exam style)"`): the check does not, and
  two is the minimum (three fm chapters of P21–P22 had one). No worked example may use a rule taught later in the
  chapter.
- Every Pure chapter has at least one `:::plot` or hand figure (`grep -c "^:::plot\|<svg"`): two P23–P24 chapters
  had none. A widget does not replace it.
- Grep FACTS.md for the newest real paper of your chapter's paper (for 9231/21: June 2025 and June 2026) and give
  each question shape your chapter covers its own worked `:::eg (Exam style)` with fresh numbers, not only an
  Exam practice question.

## Figures
- Function graphs: `:::plot` (kit/STYLE.md), one or two per Pure chapter; never long hand-written SVG curve paths.
- Hand SVG only for geometry, force diagrams, Argand loci, trees, box plots, histograms, straight-segment v–t graphs,
  vector diagrams; one or two per chapter; classes from kit/STYLE.md. Labels use `tl` (`ts` only for tick numbers),
  `halo` where a label touches a line; viewBox cropped to the drawing plus about 15 px. Check coordinates with
  Python and look at every figure at phone width.
- 3D figures in perspective: where one line passes behind another, leave a gap of about 15 px in the back line so
  skew lines do not look as if they meet; keep right-angle marks off the other lines.

## Widgets
- Embed a widget only where it teaches what a static figure cannot, with a sentence saying what to try.
- New widgets: one file `widgets/<name>.js` each (one `W.register`, kit/WIDGETS.md), on the `W` helpers. Probe with
  `node kit/zta.js widget <name> '…' --probe` (light, dark, phone, bad attributes, zero size). Names must not clash
  (kit/LINKS.md lists every widget).
- Existing widgets (never rename; embed with the attributes used in existing chapters, e.g. grep `data-w="normal"`):
  `graph` (the Toolbox uses it: never change its attributes; options `data-tangent`, `data-chord`,
  `data-shade-between`, `data-shade-x`), `unitcircle`, `stats`, `iteration`, `argand`, `discrete`, `normal`,
  `projectile`, `resultant`, `proof` (scenes in `widgets/proof.js`: add one `S.<name> = {…}` object per new scene),
  `area`, `slopefield`, `vectors3d`, `sampling`, `incline`, `vt`.
- **widgets.js (about 100 KB) holds the old widgets only: never Read it whole**; grep and Read just the range.

## Guides, mixed practice and mocks
- Paper guides (`math.exam.*`): duration and marks from FACTS → minutes per mark; routes; formula-booklet entries
  and what to learn; topic list linking each chapter; top lost marks from the chapters' `:::warn` boxes (grep);
  `:::checklist Final week`; `:::progress <paper>`. No grade boundaries, question-position or frequency claims.
- Mixed practice (`math.mixed.*`): 25–35 short interleaved questions ★ → ★★★, each `Q: [n marks] (#chapter) …`.
- Mocks (`@level mock`, kit/STYLE.md "Mock papers"): one original full paper per written paper, `@time` and total
  marks exactly as FACTS.md; 9–11 questions rising in difficulty, every area of the paper covered, the last two long
  and synoptic. `:::exam` instructions first, then **one bare `:::try` per question** (`Q: [n marks] (#chapter) …`,
  the answer is the full mark scheme with accepted alternatives), a blank line before each part (a), (b) and each
  stem line; end with a table "Question → chapter to revise". The check asserts the total and recomputes every
  answer.

## Working (Writers)
- Run `check <id>` for the chapter you wrote, not the whole course; every new number goes into `checks/<id>.py`.
- FACTS.md: grep the topic (`grep -n "^- 5.4" FACTS.md`) instead of reading it whole; grep other chapters for
  specific terms only.
- Never edit chapter text through a Python heredoc or sed (`\tfrac` becomes a tab): use Write and Edit.
- Browser (when allowed): `javascript_tool` probes first; screenshots at `scale: 0.5`, at most one per widget per
  mode.

## Gold chapters
- **math.p1.diff** (Maths): structure, depth, mark style, `:::plot`. The guide model is math.p1.quadratics
  (kit/EXAMPLE.md).
- Further Mathematics: the gold chapter named in FURTHER.md.
