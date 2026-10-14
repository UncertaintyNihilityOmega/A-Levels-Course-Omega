# COURSE: Physics (phys)

Read this, kit/STYLE.md, the gold chapter (chapters/phys.dc.md) and your own package file (packages/Pn.md).
Nothing else is needed: your package file copies in the syllabus outcomes, pitfalls, figures, data and widget specs.

## The gold chapter
**phys.dc (D.C. circuits)** is the model for every topic chapter: tone, depth, section order, figure style,
mark-scheme style, exam practice, stretch, quiz, checklist and check script (checks/phys.dc.py). Match it. Read
it once in full before you write anything; copy its SVG patterns (circuit symbols, arrows, labels) rather than
inventing new ones.

## Course
- Board: Cambridge International AS & A Level Physics **9702**, syllabus for 2025–2027. Topics 1–11 are AS
  (Papers 1, 2, 3); topics 12–25 are A Level (Paper 4, with AS knowledge assumed; Paper 5 is planning).
- One chapter per syllabus topic, in syllabus order, except topic 20, which is split into phys.magnetic
  (20.1–20.4) and phys.induction (20.5). Practical skills (Papers 3 and 5) have two chapters of their own.
- Exam facts (papers, times, marks, weightings, data sheet, command words) are in FACTS.md and copied into the
  package files that need them. State nothing about the exams that is not there. Never say how often a topic
  comes up or how many marks it is worth.
- Other boards: one short `:::board` box per chapter at most, about **content** differences you are sure of
  (e.g. "AQA writes the first law as Q = ΔU + W, with W the work done by the gas"). Never name other boards'
  paper numbers, never invent details. If unsure, write only about the Cambridge content.
- `@paper` lines: AS chapters `CAIE P1 · P2 (AS)` (add `· P3` when the chapter teaches a practical skill);
  A Level chapters `CAIE P4 (A Level)` (add `· P5` when relevant). Guides: `CAIE 9702`.

## Data values and conventions (non-negotiable)
- Use the **9702 data sheet values exactly** (FACTS.md, copied below), never "rounder" ones:
  g = 9.81 m s⁻² · c = 3.00 × 10⁸ m s⁻¹ · e = 1.60 × 10⁻¹⁹ C · 1 u = 1.66 × 10⁻²⁷ kg · m_p = 1.67 × 10⁻²⁷ kg ·
  m_e = 9.11 × 10⁻³¹ kg · N_A = 6.02 × 10²³ mol⁻¹ · R = 8.31 J K⁻¹ mol⁻¹ · k = 1.38 × 10⁻²³ J K⁻¹ ·
  G = 6.67 × 10⁻¹¹ N m² kg⁻² · ε₀ = 8.85 × 10⁻¹² F m⁻¹ (1/(4πε₀) = 8.99 × 10⁹ m F⁻¹) · h = 6.63 × 10⁻³⁴ J s ·
  σ = 5.67 × 10⁻⁸ W m⁻² K⁻⁴. Use T/K = θ/°C + 273.15 (273 is accepted when data are given to the nearest degree;
  say which you use). Use λ = 0.693/t½ as the syllabus writes it.
- Other values a question needs (mass of the Earth, radius of the Earth, speed of sound, specific heat capacity of
  water, …) are **given in the question**, as Cambridge does. Typical values to use: M_Earth = 5.97 × 10²⁴ kg,
  R_Earth = 6.37 × 10⁶ m, speed of sound in air 340 m s⁻¹ (or 330), c_water = 4200 J kg⁻¹ K⁻¹,
  1 eV = 1.60 × 10⁻¹⁹ J.
- **First law (Cambridge form): ΔU = q + W**, where q is the energy transferred **to** the system by heating and
  W is the work done **on** the system. Work done by a gas that expands is negative W. Never use any other form
  except inside a `:::board` box.
- Gravitational potential and gravitational potential energy are **negative** (zero at infinity).
- Significant figures: give final answers to the same number of s.f. as the least precise data (usually 2 or 3),
  never fewer than 2. Carry full precision through the working; round only at the end. Say so in the first
  examples of each chapter where it matters.
- Every numerical answer carries a unit. Units upright, with negative indices and thin spaces:
  `\(9.81\,\mathrm{m\,s^{-2}}\)`, `\(\mathrm{J\,kg^{-1}\,K^{-1}}\)`, `\(\mathrm{k\Omega}\)`, `\(\mu\mathrm{m}\)`,
  `\(^\circ\mathrm{C}\)`. Never "m/s" in maths. Symbols italic (default in maths), units upright.
- Cambridge spellings and abbreviations: p.d., e.m.f., r.m.s., a.c., d.c., c.r.o. (or "oscilloscope"),
  "acceleration of free fall", "gravitational field strength", "thermodynamic temperature", "specific latent heat
  of fusion", sulfur, aluminium, metre, litre.
- Quantity symbols as in the syllabus: displacement s, velocity v, momentum p, moment/torque T, Young modulus E,
  stress σ, strain ε, wavelength λ, phase difference ϕ, resistivity ρ, flux Φ, work function Φ, decay constant λ,
  activity A, half-life t½ (`t_{1/2}`), attenuation coefficient μ, acoustic impedance Z, luminosity L,
  radiant flux intensity F, Hubble constant H₀.

## Mark-scheme style (Cambridge physics)
Physics mark schemes use four mark types. `check` counts all of them (tested: `[C1]` counts like `[M1]`).
- **C1** (compensation mark): the correct formula or substitution in a calculation. Implied by a correct answer.
  Use it on the formula/substitution line of every numerical answer: `\(I = 6.0/20\) [C1] \(= 0.30\,\mathrm{A}\) [A1]`.
- **A1**: the correct final answer with its unit (and sensible s.f.).
- **B1**: an independent mark for a statement, a definition, a reading, a named reason, a direction.
- **M1**: a method mark in "show that" questions and derivations, where the method itself is the point.
Definitions usually score 1–2 B1 marks, and each essential phrase earns one (look at the e.m.f. definition in
the gold chapter). "Explain" questions score one B1 per link in the chain of reasoning.

## Depth, tone and structure
- Readers start at zero: assume only what IGCSE Physics teaches, and re-teach that quickly where a chapter needs
  it (in a sentence, or link [Physics from zero](#phys.f.basics)). Then go all the way to A* exam depth.
- Follow STYLE.md's topic-chapter shape exactly, as the gold chapter does: `:::why` → **Before you start** +
  `:::try Warm-up` (3 questions from earlier chapters, each naming its chapter) → sections (idea → `:::def` →
  `:::formula`/`:::key` → figure → `:::eg` graded examples with C1/A1/B1 marks) → `:::warn`/`:::exam`/`:::tip`/
  `:::lab` where they fit → `:::board` → `:::eg Spot the error…` → `:::try Start easy, finish at exam standard`
  (6–10 questions) → `:::try Exam practice ★ to ★★★` (6–8 questions, `Q: [n marks] (#id) ★★ …`, 2–3 `H:` hints
  on ★★★ ones, every mark on its line) → `:::try Stretch for A*` (1–2 problems) → `:::quiz` (6–8, wrong options
  are real misconceptions, `>` explains each) → `:::checklist What you can now do` (one line per outcome group)
  → `:::recap` → `:::links` (optional) → `Next: [Title](#id)`.
- **Definitions** must be exam-quality and match the syllabus wording (the package file gives the key ones).
  Put each in a `:::def` card exactly once.
- **Derivations**: every syllabus outcome that says "derive" is examinable. Write it as
  `:::proof examinable <Title>` (5–12 lines, a reason on every line) and practise it in an exam question.
  Optional insight proofs use plain `:::proof`.
- **Practical work**: every "describe an experiment" outcome gets a `:::lab` block with `:::steps` inside:
  apparatus, what to vary and measure, how to make it accurate, the graph to plot and how the answer comes from
  its gradient or intercept (as in the gold chapter's internal-resistance lab).
- **Graphs**: physics lives on graphs. Every relationship the syllabus says to "sketch" or "analyse graphically"
  gets a figure, and you state what the gradient and the area under the graph mean wherever they mean something.
- Real contexts: cars, phones, sport, medicine, power stations, space missions, with realistic numbers.
- Short topics still need every exam angle (the P3 review had to add them): each relationship on its graph (what
  the gradient and the area mean, e.g. stress–strain gradient = E, energy against height), the standard variants of a
  formula that questions use (E_K = p²/2m), and a `:::lab` for a practical that fits even when no outcome says
  "describe an experiment".
- Long chapters are fine; padding is not. Big topics (kinematics, waves, superposition, electricity, fields,
  magnetic fields, quantum) will run to 5000–7000 words, small ones (temperature, thermodynamics) 3000–4000.

## Figures (physics conventions)
- Use `:::plot` for any graph of a function (s–t, v–t, I–V, decay, SHM, binding energy curve if a formula fits).
  Use `--xlabel "t / s" --ylabel "v / m s⁻¹"` style labels: **quantity / unit**, as Cambridge does.
  Piecewise graphs (a v–t graph made of straight segments) are hand SVGs.
- Hand SVGs (`:::html <figure class="fig">…`) for circuits, force diagrams, apparatus, field lines, wave diagrams.
  Copy the gold chapter's patterns:
  - wires `class="ln"`; components drawn **after** the wire with `class="fp s-ink sw2"` so the fill hides the wire
    behind them (resistor = 44×16 rect, meter = r 13 circle with a bold letter `class="tb tc"`, lamp = circle
    with a cross);
  - cell: long thin plate `ln` (positive) and short thick plate `ln thick`, with the wire broken between them;
  - junction dots `<circle class="fi" r="4">`; open output terminals `<circle class="fp s-ink sw2" r="4">`;
  - currents, forces, velocities: `class="c1"` with `marker-end="url(#ah-phys)"` (second vector `c2` with
    `#ah2-phys`, a third or a highlighted one `c3` with `#ahr`); labels `class="tl ta"` next to the arrow;
  - force diagrams: one arrow per force from the point of application, labelled with symbol and value
    (`W = 19.6 N`), length roughly proportional to size; never draw "resultant" arrows on a free-body diagram;
  - field lines: `c1`/`ln` paths with arrowheads part-way along (a short separate arrow path), never touching;
  - dimension arrows (a length l, a distance d): two `c1` arrows from the middle outwards, as in the
    potentiometer figure.
- viewBox about 520–640 wide, cropped to the drawing + about 15 px (check with the `getBBox` probe: the gold
  chapter's figures have no empty margins). Labels 13 px (`tl`) need room: keep the drawing compact so text stays
  readable at phone width.
- Every figure has a `figcaption` that says what to notice, and an `aria-label` that describes it.
- Lessons from the P1–P2 review (Writers cannot see the figures, so check these with coordinates before `check`):
  - A 13 px label is about 7 px per character wide and 13 px tall (baseline at `y`, top at `y − 10`). Work out
    each label's box and keep it at least 4 px clear of every line, arrow and other label it sits near, including
    the line it names ("gradient = a" was drawn on top of its own line; "120°" sat on "θ").
  - Never name colours in captions or text ("the blue arrow"): the palette changes between light and dark. Refer
    to arrows by their labels.
  - `marker-end` on a path with several `M…` subpaths draws **one** arrowhead: one `<path>` per arrow.
  - Free-body diagrams: label every force with its value when the text gives one ("drag 1.2 kN"), and keep a short
    force (friction) at least 30 px long so its arrowhead shows. Don't put a label across the body or another arrow.
  - Collisions: draw both bodies before and after, each with its own velocity arrow.
  - `:::plot`: the y-axis label sits at the top left, so `--legend tl` collides with it; use `--legend tr` and widen
    `--y` so the legend clears the curves. A point label `@s` on the x-axis collides with the tick numbers; use
    `--xstep` and `@se`/`@ne`.
  - Crop the viewBox to the drawing (+ about 15 px). A `fig small` drawn in a 400-wide viewBox with 100 px of empty
    space shows tiny on desktop and huge on a phone.
- Lessons from the P3–P4 review:
  - `thin` and `thick` do **not** change `c1`/`c2`/`c3` (their own stroke width wins). For a "thin wave + thicker sum" figure use
    `c1 sw2`, `c2 sw2 dash` and `c3 sw3`. `thin`/`thick` work on `ln`.
  - Draw the physical situation completely: a stationary wave fills the whole length L (vibrator to bridge), not one loop
    and a straight remainder; a slit seen side-on needs a small face-on inset; barriers as filled `fi` rects, not lines
    that look like wavefronts.
  - `:::plot` labels: `--label` text sits at the end of its curve and `@n`/`@ne` point labels sit next to the curve, so
    leave headroom (`--y` about 30% above the top of the curves) and never put two point labels within ~100 px of each
    other. Avoid three series in one plot (the 2nd and 3rd colours look alike in dark mode); label crests, not zero
    crossings on a mid-height axis (they sit on the tick numbers).
  - `fig small` only for drawings about 300 wide; a 400-wide viewBox in `fig small` makes 13 px labels unreadable.
  - Arrows shorter than about 20 px (a dimension `a` of 26 px split in two) show only arrowheads: enlarge the drawing.
- Widgets (P3–P4 lessons): never name colours in notes ("the red line"): say "the dashed line". Axis ranges must follow
  the values: a fixed window that squeezes the interesting region into a few per cent of the axis, or turns a pattern
  into a flat average, is a bug (zoom or pick from a few window sizes). Keep legends and labels off the curves (bottom
  strip or a corner the curves cannot reach). Do not stroke very short, thick canvas arcs (Chrome leaves stray marks):
  draw short chords instead.
- Rounding: never reuse a rounded intermediate (a gradient 0.452, a time 10.10 s) in a later step; the check
  script must compute from the unrounded value (g from the P1 data is 9.78, not 9.79).

## Widgets
- Names are global: this course's widgets are `phys-…`, except `units` (the Toolbox page expects that name).
- Each widget is built by exactly one package (named in course.json and in that package file) in
  `widgets/<name>.js`, one `W.register` per file, following kit/WIDGETS.md. The gold widget
  **widgets/phys-divider.js** is the pattern to copy (tabs, `W.sliderNum`, `W.slider` with `fmt`, `W.canvas` +
  `W.axes` with a clipped curve, `W.readout`, a `.w-note` that explains, defaults clamped and validated).
- A chapter may embed a widget another package builds (it shows a placeholder until built). Widgets from the
  maths course that work here: `projectile`, `vt` (velocity–time), `resultant`, `incline`, `graph`. Their
  attributes are not documented here, so embed them with no `data-` options only if your package file says to.
- Test every widget with `node kit/zta.js widget <name> '<attrs>' --probe`, including bad attributes.

## Course-wide rules
- Never edit COURSE.md, course.json, FACTS.md, other packages' files or widgets.js (Writers). Questions or
  problems with the plan go in REQUESTS.md (engine) or as a note in your `done` summary (for the reviewer).
- `checks/<id>.py` recomputes **every** number, using the data-sheet constants (define them once at the top).
  Use the gold check script as the model (helpers `eq`, `sf`, `par`).
- Numbers in the package files are suggestions, checked by the Specialist, but your check script is the judge: if
  a suggested value disagrees with your computation, use the computed value and say so in your `done` summary.
- Write questions and contexts in your own words: never copy a past-paper question or a textbook.
- Links between chapters: link the first mention of an earlier or later topic, e.g.
  `[Gravitational fields](#phys.gravity)`. Ids are in course.json; maths ids in kit/LINKS.md
  (useful: math.f.algebra, math.f.powers, math.f.graphs, math.f.geometry, math.p1.trig, math.p1.circular,
  math.p3.logs, math.p3.vectors, math.p1.diff, math.p1.integ, math.m.kinematics, math.m.forces).
- `:::links`: optional, and only URLs you can verify. These were checked on 13 October 2026 and may be used:
  PhET simulations `https://phet.colorado.edu/en/simulations/<name>` for: circuit-construction-kit-dc,
  circuit-construction-kit-ac, projectile-motion, forces-and-motion-basics, collision-lab, balancing-act,
  density, buoyancy, energy-skate-park-basics, hookes-law, wave-on-a-string, waves-intro, wave-interference,
  sound-waves, ohms-law, resistance-in-a-wire, rutherford-scattering, build-an-atom, gravity-and-orbits,
  gravity-force-lab-basics, my-solar-system, gas-properties, states-of-matter, pendulum-lab, masses-and-springs,
  charges-and-fields, coulombs-law, capacitor-lab-basics, faradays-law, faradays-electromagnetic-lab,
  magnet-and-compass, photoelectric, models-of-the-hydrogen-atom, alpha-decay, beta-decay, blackbody-spectrum,
  bending-light, curve-fitting, least-squares-regression. Physics & Maths Tutor:
  `https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-<1..5>/` (past papers, mark
  `[unofficial]`) and `https://www.physicsandmathstutor.com/physics-revision/a-level-cie/` (notes). Cambridge's
  9702 page: `https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-physics-9702/`.
  End the block with `Links checked 13 October 2026.`
- `Next:` follows course.json order: overview → f.basics → units → kinematics → dynamics → forces → energy →
  solids → waves → superposition → electricity → dc → particles → circular → gravity → temperature → gases →
  thermo → oscillations → efields → capacitance → magnetic → induction → ac → quantum → nuclear → medical → astro →
  practical → planning → exam.p1 → exam.p24 → mixed.as → mixed.a2.

## Packages (course.json)
Topic chapters first (AS, then A Level), extras after. Each package file is self-contained.
| Package | Chapters | Builds widgets |
|---|---|---|
| P1 | phys.units, phys.kinematics | units |
| P2 | phys.dynamics, phys.forces | phys-collide |
| P3 | phys.energy, phys.solids | phys-stretch |
| P4 | phys.waves, phys.superposition | phys-wave, phys-fringes |
| P5 | phys.electricity, phys.particles | phys-iv, phys-quarks |
| P6 | phys.circular, phys.gravity | phys-orbit |
| P7 | phys.temperature, phys.gases, phys.thermo | phys-gas |
| P8 | phys.oscillations, phys.efields | phys-shm |
| P9 | phys.capacitance, phys.magnetic | phys-rc |
| P10 | phys.induction, phys.ac | phys-ac |
| P11 | phys.quantum, phys.nuclear | phys-photo, phys-halflife |
| P12 | phys.medical, phys.astro | phys-star |
| P13 | phys.practical, phys.planning | phys-bestfit |
| P14 | phys.overview, phys.f.basics | – |
| P15 | phys.exam.p1, phys.exam.p24 | – |
| P16 | phys.mixed.as, phys.mixed.a2 | – |
phys.dc (gold) was written in LEAD with widgets/phys-divider.js.
