# COURSE: Chemistry (chem)

Written by the Specialist (LEAD, 15 Oct 2026). Every Writer reads this file, kit/STYLE.md, the gold chapter
and its own `packages/Pn.md`. Nothing else is needed.

## Course and board
- Cambridge International AS & A Level Chemistry **9701**, syllabus for 2025, 2026 and 2027 (FACTS.md has every
  learning outcome, the Data section and the practical facts). Topics 1–22 are AS, 23–37 A Level.
- Papers (FACTS.md "Exam structure"): P1 multiple choice (40 four-choice questions, AS content), P2 AS structured,
  P3 Advanced Practical Skills, P4 A Level structured (AS knowledge assumed), P5 Planning, Analysis and Evaluation.
- Main board Cambridge. Other boards only in one `:::board` box per chapter (rule below).

## The plan (course.json)
49 chapters in teaching order: all AS chapters first, then A Level, then practical skills, then exam practice.
Groups: Start here · AS physical chemistry · AS inorganic chemistry · AS organic chemistry and analysis ·
A Level physical chemistry · A Level inorganic chemistry · A Level organic chemistry and analysis · Practical
skills · Exam practice. `chem.entropy` was merged into `chem.lattice` (alias).

Where a syllabus topic has an AS part and an A Level part, the plan says which chapter holds each part. Chapters
marked `@level as a2` (chem.group2, chem.org.isomerism) put the A Level part in its own final `##` section whose
heading ends "(A Level)", and say at its start that AS students can stop before it.

23 packages (P1–P23, 2–3 chapters each); packages/`Pn`.md lists everything. The gold chapter `chem.org.halogen` is
already written and belongs to no package. Never edit it.

## Gold chapter
**`chem.org.halogen` (Halogenoalkanes)**. Read it before writing: it shows the section order, the tone, how organic
marks are written (B1 per reagent, condition, arrow), how calculations are marked (B1 Mr, M1, M1, A1), the
spot-the-error format, mhchem use, and the three kinds of chemistry figure (skeletal formulas, curly-arrow mechanisms,
apparatus). Copy its SVG patterns instead of inventing new ones.

## Data values and conventions
- Use the Data booklet values (FACTS.md "Data booklet values"): R = 8.31 J K⁻¹ mol⁻¹, F = 9.65 × 10⁴ C mol⁻¹,
  L = 6.022 × 10²³ mol⁻¹ (write 6.02 × 10²³ only when 3 s.f. is clearly enough), e = 1.60 × 10⁻¹⁹ C,
  molar gas volume 24.0 dm³ mol⁻¹ at room conditions (22.4 at s.t.p.), Kw = 1.00 × 10⁻¹⁴ mol² dm⁻⁶ at 298 K,
  c = 4.18 J g⁻¹ K⁻¹. Standard conditions 298 K and 101 kPa. Bond energies, E⦵ values, electronegativities, IR, NMR
  shifts and first/successive ionisation energies: only the FACTS.md values.
- **Relative atomic masses**: the 9701 Periodic Table values to 1 d.p. (H 1.0, C 12.0, N 14.0, O 16.0, Na 23.0,
  Mg 24.3, Al 27.0, S 32.1, Cl 35.5, K 39.1, Ca 40.1, Fe 55.8, Cu 63.5, Zn 65.4, Br 79.9, Ag 107.9, I 126.9,
  Ba 137.3). Others: `py -c "import json;print({e['sym']:e['ar'] for e in json.load(open('data/elements.json',encoding='utf-8'))}['Mn'])"`.
  Never type an Ar from memory.
- Nernst equation in the Cambridge form \(E = E^{\ominus} + \dfrac{0.059}{z}\log\dfrac{[\text{oxidised}]}{[\text{reduced}]}\).
  Avogadro constant symbol L (the syllabus writes F = Le).
- Answers to 3 s.f. unless the data justify more (FACTS.md "Units and s.f."); pH to 2 d.p.; never reuse a rounded
  intermediate (keep 4+ s.f. in working, as the gold chapter does). Units always: mol dm⁻³, kJ mol⁻¹, cm³, dm³,
  J K⁻¹ mol⁻¹. No unit on Kc or Kp unless you work it out; when asked, give it (e.g. mol⁻² dm⁶).
- Spelling: sulfur, aluminium, caesium, ethanoic acid (never "acetic acid"), propanone, 2-methylpropan-2-ol,
  halogenoalkane (not haloalkane), manganate(VII), dichromate(VI), "precipitate" (ppt. only in tables).
- Cambridge words: "relative atomic mass", "enthalpy change", "lattice energy (gas ions → solid)", "electrode
  (reduction) potential", "rate-determining step", "van der Waals' forces", "id-id forces", "pd-pd forces".
  Use the syllabus definitions in FACTS.md word for word in `:::def` cards where it gives one.

## Writing chemistry in this course (tested in the preview)
- **mhchem for every formula and equation**: `\(\ce{H2SO4}\)`, `\(\ce{Cu^2+(aq)}\)`, `\(\ce{SO4^2-}\)`,
  `\(\ce{[Cu(H2O)6]^2+}\)`, `\(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\)`, `\(\ce{CuSO4.5H2O}\)`, gas/precipitate arrows are
  not needed (write state symbols instead). Dipoles: `\(\ce{C^{\delta+}-Br^{\delta-}}\)`; in running text write
  plain "δ+" (`\(\delta+\)` renders with a gap).
- **Isotopes**: `\(\ce{^{35}Cl}\)`, `\(\ce{^{37}_{17}Cl}\)` (the engine rewrites them so they render correctly), or
  `\({}^{37}_{17}\mathrm{Cl}\)`.
- **Conditions on arrows**: `\(\ce{A ->[H2SO4][heat] B}\)` (above and below). Keep them short; "conc." inside
  mhchem becomes a dot, so write "concentrated" in the sentence instead.
- **Long equations**: an inline `\(\ce{…}\)` wraps on phones before each arrow and after each ` + ` (write them with
  spaces: `A + B -> C`). Put the key equation of a section in display maths `\[\ce{…}\]`. Run `phone` after every chapter.
- Electron configurations as plain text with Unicode superscripts: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s², [Ar] 3d⁶ 4s²
  (3d written before 4s, the Cambridge order).
- Standard sign: `\(\Delta H^{\ominus}_{\mathrm{f}}\)`, `\(E^{\ominus}_{\mathrm{cell}}\)`, `\(S^{\ominus}\)`.
- Equilibrium expressions: `\(K_c = \dfrac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}\)`; partial pressures `\(p_{\ce{NH3}}\)`.
- ICE ("initial, change, equilibrium") tables: a Markdown table with short cells, or `\[\begin{array}{lccc} … \end{array}\]`
  for four columns or fewer.
- Organic equations: condensed structural formulas in `\ce` (`CH3CH2CH2Br`, `CH3CH(OH)CH3`, `(CH3)3CBr`); [O] and [H]
  are allowed for organic redox: `\(\ce{CH3CH2OH + [O] -> CH3CHO + H2O}\)`.
- Reagents and conditions questions: name the reagent **and** the solvent and conditions every time ("NaOH in ethanol,
  heat"; "KCN in ethanol, heat under reflux"; "H₂, Ni catalyst, heat"). Mark each as B1.

## Marks and answers in chemistry
- Calculations: B1 for a value read or calculated in one step (an Mr), M1 for a method step, A1 for the correct
  answer with unit and s.f. Recall answers: B1 per creditworthy point. Mechanisms: B1 per arrow, dipole, intermediate
  or transition state, and products (see the gold chapter's SN2 question).
- Explanations earn marks for named causes: "the C–I bond is weaker" (not "iodine is more reactive"); "more
  shielding, larger atomic radius, weaker attraction between nucleus and outer electron" (not "it is bigger").
- Exam practice for AS chapters: Paper 1 style (one-step recall/calculation, ★) and Paper 2 style (structured,
  ★★/★★★). For A Level chapters: Paper 4 style, synoptic with AS topics in ★★★.
- MCQ quiz options are real misconceptions; at least one quiz per chapter needs a calculation.

## Depth and tone
- Readers start from zero, so build every idea in small steps. A topic chapter is long: it covers every outcome in
  FACTS.md for its topics at full exam depth. The gold chapter is about 4500 words for 7 outcomes; big topics
  (bonding, equilibria, transition elements, electrochemistry) will be longer.
- Explain *why* chemistry happens (energy, electrons, attraction, stability), then give the exam wording.
- One real context per chapter at least (industry, medicine, environment, the lab), always accurate.
- Never claim how often a topic appears or how many marks it is worth.

## Course-wide rules
- **Board boxes**: one board and one content difference you are sure of, never two boards at once, never "other
  specifications". Safe examples (each package says which box goes where, so none is repeated): AQA's A Level
  uses the Arrhenius equation (chem.rates2); AQA teaches percentage atom economy (chem.moles) and ozone depletion by
  CFCs (gold chapter); AQA explains how a time-of-flight mass spectrometer works (chem.analysis). If you are not sure, leave
  the board box out. Never in the first person.
- **Links**: only ids in course.json or kit/LINKS.md (`grep -i "<word>" kit/LINKS.md`). Link planned chapters freely.
  Useful cross-course ids: phys.gases, phys.units, math.f.algebra, math.f.powers (grep before using).
- **:::links**: only URLs you have checked. If you cannot check a URL, leave the block out. Known good (checked
  15 Oct 2026): https://www.chemguide.co.uk/mechanisms/nucsubmenu.html,
  https://www.chemguide.co.uk/organicprops/haloalkanemenu.html,
  https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/ (past paper questions by topic, unofficial).
- **Facts**: syllabus outcomes and data from FACTS.md; colours, observations and test results from the qualitative
  analysis notes in FACTS.md, in their words ("pale blue ppt. soluble in excess giving dark blue solution").
  If you are not sure of a fact (a melting point, a colour, a condition), leave it out or say it qualitatively.
- **Numbers**: every number in `checks/<id>.py`; take Ar values from data/elements.json in the check script
  (`json.load`) or copy the 1 d.p. values above.
- **Practicals**: describe procedures with the apparatus listed in the syllabus (pipette, burette, volumetric flask,
  balance to 0.01 g, thermometer at 1 °C, gas syringe or collection over water, crucible on a pipe-clay triangle).
  Safety lines are short and specific (fume cupboard for toxic gases, gloves for corrosive reagents, no flames near
  ethanol).
- `@paper` line: "CAIE 9701 Papers 1 and 2 (AS)" for AS topics, "CAIE 9701 Paper 4" for A Level topics (add
  "; assumed knowledge in Paper 4" for AS topics as the gold chapter does).

## Figures (read with kit/STYLE.md "Figures" and "Figure and widget lessons")
Writers cannot see their figures. Plan coordinates in Python, then `shot <id>` and `shot <id> --dark --phone`.

### Lessons from earlier courses that apply here
- Label boxes: a 13 px `tl` label is ~7 px per character wide, 13 px tall (baseline at y, top at y − 10). Keep it
  ≥ 4 px clear of every line and label. End ordinary arrows ≥ 10 px short of anything they do not point at.
- Scale: `fig` shows ~625 px wide, `fig small` ~360 px. Use a 520–640-wide viewBox in `fig` and 300–350 in
  `fig small`; never 380–500 in `fig` (labels look huge). Crop the viewBox to the drawing + ~15 px.
- Classes only, never colours, ids, `<defs>`, `<marker>`, `<style>`. Never name colours in captions or text
  ("the red arrow"): name things by label or "dashed". `thin`/`thick` change `ln` only; use `sw2`/`sw3` on `c1`–`c3`.
  One path per arrow (a path with several `M` subpaths gets one head). Same quantity, same class.
- `:::plot`: `--legend tr`; ~30% headroom above curves; point labels ~100 px apart and off tick numbers; start
  `--y` at 0 unless the origin is far off; at most two series per plot; cut curves that would run through the
  axis labels (domain trick in STYLE.md).
- Widgets: axis ranges follow the values; legends off the curves; `W.ticks` with `ny` 3 or 4; checkbox rows as in
  STYLE.md; draw chords, not very short thick canvas arcs.
- One board and one difference in `:::board`; never reuse a rounded intermediate.

### Chemistry figure conventions (copy the gold chapter's SVG)
- **Skeletal formulas**: zigzag `<path class="ln thick">` with 35 px horizontal steps and ±20 px vertical (bond
  ~40 px, 120° angles); heteroatom labels as `tl` text (`tc` to centre), bond ends ~5 px short of the label box.
  A benzene ring: a regular hexagon of side ~28 px with a circle of radius ~17 px inside (`ln`), the Cambridge form;
  never draw benzene as alternating double bonds.
- **Displayed formulas**: atoms as `tl tc` text, bonds as `ln` lines that stop ~6 px short of each label. Double bond:
  two parallel lines 5 px apart. Draw all bonds; a displayed formula shows every atom and bond.
- **Curly-arrow mechanisms**: arrows `<path class="c1 sw2" d="M x0 y0 Q cx cy x1 y1" marker-end="url(#ahs-red)"/>`,
  one path per arrow, at least ~30 px long (the small head #ahs-red is ~7 px), starting **at a lone pair or the middle of a
  bond** and ending ~5–8 px from the atom (or bond middle) that receives the pair. Lone pairs: two
  `<circle class="fi" r="1.7">` dots 6 px apart beside the atom. Dipoles: `δ+`/`δ−` labels in `tl ta`. Charges in
  the text (`C⁺`, `HO⁻`, `Br⁻`). Transition states in square brackets drawn as `ln` paths, partial bonds `ln dash`,
  overall charge outside the top-right corner. Intermediates (carbocations, arenium ions) are not bracketed.
  At most three structures per row; two rows for two-step mechanisms (gold SN1 figure). Step arrows `ln` with
  `#ah`, with "step 1 (slow)" above them. Free-radical mechanisms are written as equations, not drawn: `\(\ce{Cl2 ->[UV] 2Cl^.}\)`,
  `\(\ce{Cl^. + CH4 -> CH3^. + HCl}\)` (mhchem `^.` gives the radical dot; tested).
- **Energy profiles** (reaction pathway diagrams): axes `ax` with `#ahm` heads, labelled "enthalpy" (y) and
  "progress of reaction" (x), no numbers on the axes; reactant and product levels as short horizontal `ln thick`
  lines with `\ce` text in `tl`; the hump a smooth `c1` path (cubic Béziers); ΔH and Eₐ as vertical double-headed
  arrows: two `c2` paths from the middle outwards, each with `#ah`; catalysed path `c1 dash`.
- **Energy cycles** (Hess, solution): each species is `tl tc` text, optionally on a `fm` rounded rect (`rx="8"`)
  sized to the text + 8 px; arrows `ln` with `#ah`, one path each, labelled beside the midpoint with `halo`. Born–Haber cycles are
  drawn as level diagrams: horizontal `ln` levels, vertical arrows up (endothermic) and down (exothermic), each
  labelled with its ΔH name and value; keep 30 px between levels.
- **Apparatus**: glassware outlines `ln` (round-bottomed flask as an arc path with an open neck, as in the gold
  reflux figure), liquids `fa`, solids `fm2`, water flow and gas arrows `ln` + `#ah`, heat `c2 sw2` + `#ah`.
  Labels to the side with a `ln-m thin` pointer line. Clamps and stands are not drawn.
- **Graphs**: `:::plot` for mathematical curves (Boltzmann-like shapes, first-order decay `exp(-k*x)`,
  concentration–time); a hand SVG for titration curves only if the `chem-titration` widget does not fit the text.
  Spectra (IR, mass, NMR) are hand SVG bar/peak drawings with a `ax` baseline and tick labels in `ts`; mass spectra
  as vertical `c1 thick` lines with m/e labels.
- Orbital shapes: s as a `fa2` circle, p as two `fa` ellipses (dumbbell) on `ax` axes; d orbitals the same way.

## Widgets
- Each widget is `widgets/<name>.js` (one `W.register` per file, IIFE). The package that owns it builds it; any
  chapter may use it. Names: `periodic`, `molar` (exact names, used by the Toolbox), the rest `chem-…`.
- Element data is generated by Python from the 9701 table: run `py data/elements.py` (it writes
  data/elements.json: z, sym, name, ar, group, period, block, cat, config/short for Z ≤ 36). Embed the data in
  the widget file with a Python script that writes the JS file; never type element data.
- Widgets owned by other courses that fit here: `phys-gas` (pV = nRT), `units`, `graph`. Never register them.
- Owner packages: periodic P1; chem-config, molar P2; chem-vsepr P3; chem-profile P4; chem-equilibrium P5;
  chem-titration, chem-boltzmann P6; chem-trend P7; chem-chiral P9; chem-orgmap, chem-ms P12; chem-bornhaber,
  chem-cell P13; chem-order P14; chem-dsplit P15; chem-electrophoresis P17; chem-nmr, chem-qa P19.
- Widgets you may embed before they exist (they show a placeholder until written): only those listed in your
  package notes. A page must make sense without its widget.

## Exam readiness (P20–P23)
- Paper guides: chem.exam.p1 (Paper 1), chem.exam.p24 (Papers 2 and 4); Paper 3 and Paper 5 skills are taught
  in chem.practical and chem.planning, which also act as their paper guides. Each guide sends readers to the
  board's real past papers and mark schemes (through their school, the Cambridge website, or the
  Physics & Maths Tutor topic collections linked above) without inventing details such as dates or prices.
- Mock papers: `@level mock`, one per written paper, totals exactly as FACTS.md (P1 40, P2 60, P3 40, P4 100,
  P5 30) and the real times (1 h 15 min, 1 h 15 min, 2 h, 2 h, 1 h 15 min). Show a part's marks in the question
  text as "(3 marks)" in round brackets, never a bare "[3]"; mark tokens go in the answer lines, and they must add up
  to the question's `[n marks]`.
