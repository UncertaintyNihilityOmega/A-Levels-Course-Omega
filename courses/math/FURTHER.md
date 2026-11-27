# FURTHER: rules for the Further Mathematics extension (math.fm.*)

Rules for every session that writes, reviews or reads a `math.fm.*` chapter. COURSE.md applies in full unless this
file says otherwise. Exam facts and the 9231 learning outcomes (ids 1.1a … 4.5c) are in FACTS.md under "Further
Mathematics (9231)": grep them (`grep -n "^- 1.4" FACTS.md`), never assume. A Writer reads COURSE.md, this file,
kit/STYLE.md, the gold chapter **math.fm.roots** and its own `packages/Pn.md`.

## Scope
- Cambridge International AS & A Level Further Mathematics **9231**, syllabus 2026–2027 (version 5). The 2028–2030
  syllabus has the same papers and content (FACTS.md), so the chapters stay valid.
- Four papers: FP1 (Paper 1, 2 h, 75), FP2 (Paper 2, 2 h, 75), FM (Paper 3, 1 h 30, 50), FS (Paper 4, 1 h 30, 50).
  In course.json they are `FP1`, `FP2`, `FM`, `FS`; packages P19–P36; sidebar groups "Further Mathematics (9231)" (the
  overview), one per paper ("Further Pure Mathematics 1", "Further Pure Mathematics 2", "Further Mechanics",
  "Further Probability and Statistics") and "Further Maths exam preparation"; topic chapters
  `@level fm`, guides `guide`, mocks `mock`.
- Readers have finished (or are finishing) 9709: FP1 and FP2 assume P1 and P3, FM assumes P4, FS assumes P5 and P6.
  `math.further` (the 9709 course's one-chapter tour of Further Maths) stays as it is; math.fm.overview links it.

## Building on the 9709 chapters (link, never re-teach)
- "Before you start" names the 9709 chapters the topic needs, as links, and the Warm-up draws its three questions
  from them (and from earlier fm chapters). Each answer names its chapter.
- When a 9709 idea is needed, recall it in one or two sentences with a link ("the scalar product, from
  [Vectors](#math.p3.vectors)") and go straight to the new 9231 content. Re-teach only what 9709 does not cover.
- Prerequisite map (ids from course.json): complex numbers `math.p3.complex`; vectors `math.p3.vectors`; partial
  fractions `math.p3.partial`; integration techniques `math.p3.inttech`, `math.p3.integ`; differentiation
  `math.p3.diff`, `math.p1.diff`; DEs `math.p3.diffeq`; series and binomial `math.p1.series`, `math.p3.algebra`;
  trig `math.p3.trig`, `math.p1.trig`; logs `math.p3.logs`; mechanics `math.m.forces`, `math.m.kinematics`,
  `math.m.newton`, `math.m.momentum`, `math.m.energy`; statistics `math.s1.*`, `math.s2.poisson`,
  `math.s2.linear`, `math.s2.crv`, `math.s2.sampling`, `math.s2.hypothesis`. Check an id in course.json before
  linking it.
- Inside the extension, link backwards freely ("as in [Roots of polynomial equations](#math.fm.roots)").

## 9231 conventions (in addition to COURSE.md)
- **File header**: `@level fm`; `@paper` starts "CAIE 9231 Paper 1" (2, 3, 4) and adds another board only when you
  are sure of it; `@time` realistic (most fm chapters are 5–8 hours).
- **Proof is examined in 9231.** Proof by induction (1.7), "prove" hyperbolic identities (2.1c), de Moivre for
  positive integers (2.5b), reduction formulae (2.4b), "show that" results and Ae = λe properties (2.2c) are written
  as `:::eg (Exam style)` with marks, never folded away. Induction follows the 9231 mark-scheme pattern: B1 base
  case, B1 inductive hypothesis ("Assume true for n = k"), M1 A1 inductive step, A1 conclusion ("so true for
  n = k + 1; true for n = 1, hence by induction true for all positive integers n").
- A `:::proof` (folded, badged as not examined) is only for results the syllabus does not ask students to prove
  (e.g. why the roots-and-coefficients relations hold, the derivation of the polar area formula). Every proof's
  algebra is checked numerically in `checks/<id>.py`.
- **Marks** as in 9231 mark schemes: M1, A1, B1, A1 FT (follow-through) and DM1 (a method mark that depends on an
  earlier M). Write them as tokens `[DM1]`, `[A1 FT]`, `[B1 FT]` (the engine counts and shows them since 20 Nov
  2026); `[M1] (dependent)` and `[A1] (FT)`, used before then, are also correct. The gold chapter explains both once.
- **Papers print MF19 and nothing else.** FACTS.md lists what MF19 gives a 9231 candidate (sums of r, r², r³,
  Maclaurin series, hyperbolic identities and log forms, inverse trig and hyperbolic derivatives and integrals,
  t = tan ½x, trajectory, Hooke's law and EPE, circular acceleration, centres of mass, pooled variance, PGF mean and
  variance, normal, t, χ² and Wilcoxon tables) and what must be learned. Each chapter's `:::exam` says which of its
  formulas are given and which must be learned. Never tell a reader a formula is "on the formula sheet" unless
  FACTS.md lists it.
- **Mechanics**: g = 10 (the 9231/31 front page says "use 10 m s–2"); "Take \(g = 10\)" in every question that
  needs it. Diagrams in the papers are "not to scale" figures: our hand SVGs follow COURSE.md Figures.
- **Statistics**: critical values come from the MF19 tables. `checks/<id>.py` recomputes them with the standard
  library only (no scipy): normal from `NormalDist().inv_cdf`; t and χ² by integrating the density (Simpson, 2000+
  strips) and bisecting for the percentage point; Wilcoxon critical values by counting all 2ⁿ sign patterns or all
  rank subsets. Compare with the table value to its printed accuracy and quote the table value in the chapter.
  State hypotheses in words and symbols, the test statistic, the critical value or p-value, the comparison, and a
  conclusion in context with "evidence" language ("there is sufficient evidence at the 5% level that …"); never
  "proves" or "accept H₁".
- **Matrices**: bold capitals \(\mathbf{M}\), \(\mathbf{I}\), \(\det \mathbf{M}\), \(\mathbf{M}^{-1}\); write
  matrices with `\begin{pmatrix} … \end{pmatrix}`. On phones a 3×3 matrix in display maths is fine; never put one
  inline. **Vectors** as COURSE.md; the vector product \(\mathbf{a} \times \mathbf{b}\); planes
  \(\mathbf{r} \cdot \mathbf{n} = p\). **Polar**: \((r, \theta)\) with \(r \geq 0\). **Hyperbolic**: \(\sinh x\),
  \(\cosh x\), \(\tanh x\), \(\sinh^{-1} x\) (also \(\operatorname{arsinh}\) once, as an alternative name).
  **Roots**: \(\alpha, \beta, \gamma, \delta\), \(\sum \alpha\), \(\sum \alpha\beta\), \(\sum \alpha\beta\gamma\).
- **Checks**: Python standard library only (`fractions.Fraction` for exact work, `complex` for complex numbers,
  hand-written 2×2 and 3×3 determinant, inverse and product helpers, Simpson for integrals, finite differences
  for derivatives). Recompute every number, every root, every coefficient and every mark total.
- **Board box**: UK Further Maths (AQA 7367, Edexcel 9FM0, OCR H245) and Edexcel IAL Further Pure share most Further
  Pure topics but split them differently. Name only differences you are sure of; otherwise describe 9231 only.
- **Exam practice**: questions in the 9231 style: several parts (a), (b), (c) that build on each other, "show that"
  with a given answer, "hence", "deduce", "find in exact form", "sketch, stating the coordinates of …". A ★★★ question
  is 8–15 marks with 3–5 parts, as in the real papers (FACTS.md: question sizes 5–16 marks).

## Gold chapter
**math.fm.roots** (Roots of polynomial equations, P19): structure, depth, marks, warm-up from 9709 chapters, the
board box, the MF19 note and the links box. Every fm topic chapter has the same sections in the same order
(COURSE.md "Sections of a topic chapter").

## Packages (teaching order: FP1, FP2, FM, FS, then exam preparation)
| Package | Chapters | New widget |
|---|---|---|
| P19 | roots (gold, written), series | none |
| P20 | matrices, transform, induction | fm-matrix |
| P21 | rational, graphs, polar | fm-polar |
| P22 | vectors, vectors2 | fm-planes |
| P23 | hyperbolic, diff, integ | fm-maclaurin |
| P24 | reduction, rectangles, arclength | none (uses `area`) |
| P25 | complex, complex2 | fm-demoivre |
| P26 | systems, matrices2 | none (uses fm-matrix, fm-planes) |
| P27 | de, de2 | fm-de |
| P28 | projectiles, com, rigid | fm-topple |
| P29 | elastic, circular, vertical | fm-vcircle |
| P30 | variable, impulse, oblique | fm-impact |
| P31 | crv, inference, twosample | fm-tdist |
| P32 | chisq, contingency | fm-chisq |
| P33 | nonpar, wilcoxon, pgf | fm-pgf |
| P34 | overview, exam.fp1, exam.fp2, exam.fm, exam.fs | none |
| P35 | mock.p1, mock.p2, mixed.pure | none |
| P36 | mock.p3, mock.p4, mixed.applied | none |

All ids are `math.fm.<name>`. A widget is built only by its own package; later packages embed it with the attributes
documented in its file. Widget names were checked against kit/LINKS.md (no clashes).

## Learn more online (verified links for `:::links`)
Use only these URLs (or ones already in a 9709 chapter's links box). Kinds and tags as in COURSE.md.
- watch: [Roots and coefficients of a cubic](https://www.examsolutions.net/tutorials/relationships-roots-coefficients-cubic-equation/) · ExamSolutions
- watch: [Roots and coefficients of a quadratic](https://www.examsolutions.net/tutorials/relationships-roots-coefficients-quadratic-equation/) · ExamSolutions
- watch: [Roots and coefficients of a quartic](https://www.examsolutions.net/tutorials/relationships-roots-coefficients-quartic-equation/) · ExamSolutions
- watch: [Method of differences](https://www.examsolutions.net/tutorials/method-differences/) · ExamSolutions
- watch: [Induction: divisibility proofs](https://www.examsolutions.net/tutorials/divisibility-and-multiple-test-proofs/) · ExamSolutions
- watch: [Invariant points](https://www.examsolutions.net/tutorials/matrices-invariant-points/) · ExamSolutions
- watch: [Area bounded by a polar curve](https://www.examsolutions.net/tutorials/area-bounded-polar-curve/) · ExamSolutions
- watch: [Shortest distance between two skew lines](https://www.examsolutions.net/tutorials/shortest-distance-between-two-skew-lines/) · ExamSolutions
- watch: [Hyperbolic identities](https://www.examsolutions.net/tutorials/hyperbolic-identities/) · ExamSolutions
- watch: [Maclaurin's series expansion](https://www.examsolutions.net/tutorials/maclaurins-series-expansion/) · ExamSolutions
- watch: [De Moivre's theorem](https://www.examsolutions.net/tutorials/de-moivres-theorem/) · ExamSolutions
- watch: [Eigenvalues and eigenvectors](https://www.examsolutions.net/tutorials/eigenvalues-and-eigenvectors/) · ExamSolutions
- watch: [Integrating factor: dy/dx + Py = Q](https://www.examsolutions.net/tutorials/solving-equations-form-dydx-py-q-using-integrating-factor/) · ExamSolutions
- watch: [Second order DEs equal to zero](https://www.examsolutions.net/tutorials/how-to-solve-second-order-linear-differential-equations-that-equal-zero/) · ExamSolutions
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · every Further Pure topic
- watch: [Projectiles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NhfzR6dcRPAo139k4Q_YmP-) · ExamSolutions (YouTube)
- watch: [Composite laminas playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiGwlCjUDNys8kZTVhE46ee) · ExamSolutions (YouTube)
- watch: [Toppling playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NgTf2HUkNHheRbMCrt00iyD) · ExamSolutions (YouTube)
- watch: [Horizontal circles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NjtPvBrbfB1Ge-Tk6pCf4xQ) · ExamSolutions (YouTube)
- watch: [Vertical circles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiWB2Brk-zazRkg-RvE_cJk) · ExamSolutions (YouTube)
- watch: [Newton's law of restitution playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiPDYYt5yYtsPqnSbtedvrN) · ExamSolutions (YouTube)
- watch: [Linear transformations](https://www.3blue1brown.com/lessons/linear-transformations) · 3Blue1Brown
- watch: [Matrix multiplication as composition](https://www.3blue1brown.com/lessons/matrix-multiplication) · 3Blue1Brown
- watch: [The determinant](https://www.3blue1brown.com/lessons/determinant) · 3Blue1Brown
- watch: [Cross products](https://www.3blue1brown.com/lessons/cross-products) · 3Blue1Brown
- watch: [Eigenvectors and eigenvalues](https://www.3blue1brown.com/lessons/eigenvalues) · 3Blue1Brown
- watch: [Euler's formula with introductory group theory](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown
- watch: [Differential equations, a tourist's guide](https://www.3blue1brown.com/lessons/differential-equations) · 3Blue1Brown
- read: [Polar coordinates](https://tutorial.math.lamar.edu/Classes/CalcII/PolarCoordinates.aspx) · Paul's Online Notes
- read: [Area with polar coordinates](https://tutorial.math.lamar.edu/Classes/CalcII/PolarArea.aspx) · Paul's Online Notes
- read: [Arc length](https://tutorial.math.lamar.edu/Classes/CalcII/ArcLength.aspx) · Paul's Online Notes
- read: [Surface area](https://tutorial.math.lamar.edu/Classes/CalcII/SurfaceArea.aspx) · Paul's Online Notes
- read: [Taylor series](https://tutorial.math.lamar.edu/Classes/CalcII/TaylorSeries.aspx) · Paul's Online Notes · Maclaurin is the case about 0
- read: [Linear first order equations](https://tutorial.math.lamar.edu/Classes/DE/Linear.aspx) · Paul's Online Notes
- read: [Second order equations](https://tutorial.math.lamar.edu/Classes/DE/IntroSecondOrder.aspx) · Paul's Online Notes
- read: [Intuitive understanding of Euler's formula](https://betterexplained.com/articles/intuitive-understanding-of-eulers-formula/) · BetterExplained
- read: [Hypothesis testing with two samples](https://openstax.org/books/introductory-statistics-2e/pages/10-introduction) · OpenStax
- read: [The chi-square distribution](https://openstax.org/books/introductory-statistics-2e/pages/11-introduction) · OpenStax
- read: [Roots of polynomials (Edexcel Core Pure notes)](https://www.savemyexams.com/a-level/further-maths/edexcel/17/core-pure/revision-notes/further-algebra-and-functions/roots-of-polynomials/roots-of-polynomials/) · Save My Exams [paid]
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · free booklets with answers: roots, series, induction, polar, hyperbolic, complex numbers
- practise: [Further integration booklets](https://madasmaths.com/archive_maths_booklets_further_topics_integration.html) · MadAsMaths · reduction formulae, arc length, surface area
- practise: [Linear algebra booklets](https://madasmaths.com/archive_maths_booklets_further_topics_linear_algebra.html) · MadAsMaths · matrices, vectors, planes
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths
- practise: [FP1 practice papers](https://madasmaths.com/archive_iygb_practice_papers_fp1_practice_papers.html) · MadAsMaths · full UK-style papers [unofficial]
- practise: [Roots of polynomials exam questions (Edexcel)](https://www.savemyexams.com/a-level/further-maths/edexcel/17/core-pure/topic-questions/further-algebra-and-functions/roots-of-polynomials/exam-questions/) · Save My Exams [paid]
- practise: [Matrices](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices) · Khan Academy
- practise: [Parametric equations, polar coordinates, and vector-valued functions](https://www.khanacademy.org/math/ap-calculus-bc/bc-advanced-functions-new) · Khan Academy · polar tangents and areas (the old precalculus polar unit is gone, 27 Nov 2026)
- practise: [Linear algebra](https://www.khanacademy.org/math/linear-algebra) · Khan Academy
- practise: [Differential equations](https://www.khanacademy.org/math/differential-equations) · Khan Academy
- practise: [Significance tests, one sample](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample) · Khan Academy
- practise: [Two-sample tests and intervals](https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples) · Khan Academy
- practise: [Chi-square tests](https://www.khanacademy.org/math/statistics-probability/inference-categorical-data-chi-square-tests) · Khan Academy
- explore: [Polynomials station](https://undergroundmathematics.org/polynomials) · Underground Mathematics
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · rational and polar curves
- explore: [Desmos 3D](https://www.desmos.com/3d) · Desmos · planes and lines
- explore: [GeoGebra 3D](https://www.geogebra.org/3d) · GeoGebra
- explore: [Projectile motion](https://phet.colorado.edu/en/simulations/projectile-motion) · PhET
- explore: [Collision lab](https://phet.colorado.edu/en/simulations/collision-lab) · PhET · e and oblique collisions
- explore: [Masses and springs](https://phet.colorado.edu/en/simulations/masses-and-springs) · PhET
- explore: [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · 2020+ papers and mark schemes [unofficial]
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor [unofficial]
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor [unofficial]
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams
- papers: [9231 past papers archive](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-mathematics-further-9231) · PapaCambridge [unofficial]

Links checked 20 November 2026.
