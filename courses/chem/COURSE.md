# COURSE: Chemistry (chem)

Written by the Specialist (LEAD, 15 Oct 2026; review lessons merged in 23 Oct 2026). Every Writer reads this file,
kit/STYLE.md, the gold chapter and its own `packages/Pn.md`. Nothing else is needed.

## Course and board
- Cambridge International AS & A Level Chemistry **9701**, syllabus for 2025, 2026 and 2027 (FACTS.md has every
  learning outcome, the Data section and the practical facts). Topics 1–22 are AS, 23–37 A Level.
- Papers (FACTS.md "Exam structure"): P1 multiple choice (40 four-choice questions, AS content), P2 AS structured,
  P3 Advanced Practical Skills, P4 A Level structured (AS knowledge assumed), P5 Planning, Analysis and Evaluation.
- Main board Cambridge. Other boards only in one `:::board` box per chapter (rule below).

## The plan (course.json)
49 chapters in teaching order (AS, A Level, practical skills, exam practice); groups and aliases are in course.json.
Chapters marked `@level as a2` (chem.group2, chem.org.isomerism) put the A Level part in a final `##` section whose
heading ends "(A Level)" and say at its start that AS students can stop before it.
23 packages (P1–P23); packages/`Pn`.md lists everything. The gold chapter belongs to no package: never edit it.

## Gold chapter
**`chem.org.halogen` (Halogenoalkanes)**. Read it before writing: section order, tone, organic marks (B1 per reagent,
condition, arrow), calculation marks (B1 Mr, M1, M1, A1), spot-the-error format, mhchem use, and the three kinds of
chemistry figure (skeletal formulas, curly-arrow mechanisms, apparatus). Copy its SVG patterns.

## Data values and conventions
- Data booklet values only (FACTS.md): R = 8.31 J K⁻¹ mol⁻¹, F = 9.65 × 10⁴ C mol⁻¹, L = 6.022 × 10²³ mol⁻¹
  (6.02 × 10²³ only when 3 s.f. is clearly enough), e = 1.60 × 10⁻¹⁹ C, molar gas volume 24.0 dm³ mol⁻¹ at room
  conditions (22.4 at s.t.p.), Kw = 1.00 × 10⁻¹⁴ mol² dm⁻⁶ at 298 K, c = 4.18 J g⁻¹ K⁻¹; standard conditions 298 K,
  101 kPa. Bond energies, E⦵, electronegativities, IR, NMR shifts and ionisation energies: only the FACTS.md values.
- **Ar**: the 9701 table to 1 d.p. (H 1.0, C 12.0, N 14.0, O 16.0, Na 23.0, Mg 24.3, Al 27.0, S 32.1, Cl 35.5,
  K 39.1, Ca 40.1, Fe 55.8, Cu 63.5, Zn 65.4, Br 79.9, Ag 107.9, I 126.9, Ba 137.3). Others:
  `py -c "import json;print({e['sym']:e['ar'] for e in json.load(open('data/elements.json',encoding='utf-8'))}['Mn'])"`.
  Never type an Ar from memory.
- Physical data (boiling points, densities) only from a standard table, rounded as printed (butane −0.5 °C); say in
  the checks file where they come from.
- Nernst in the Cambridge form \(E = E^{\ominus} + \dfrac{0.059}{z}\log\dfrac{[\text{oxidised}]}{[\text{reduced}]}\);
  Avogadro constant symbol L (F = Le). The mole is defined through the Avogadro constant, not "the atoms in 12 g of
  carbon-12".
- Answers to 3 s.f. unless the data justify more; data given to 2 s.f. give 2 s.f. (338 → 340 dm³); pH to 2 d.p.
  Keep 4+ s.f. in working and never reuse a rounded intermediate. Units always (mol dm⁻³, kJ mol⁻¹, cm³, dm³,
  J K⁻¹ mol⁻¹). No unit on Kc or Kp unless worked out; when asked, give it (e.g. mol⁻² dm⁶).
- Spelling: sulfur, aluminium, caesium, ethanoic acid (never "acetic acid"), propanone, 2-methylpropan-2-ol,
  halogenoalkane, manganate(VII), dichromate(VI), "precipitate" (ppt. only in tables). IUPAC names only
  (propan-2-ol, never "2-propanol").
- Cambridge words: "relative atomic mass", "enthalpy change", "lattice energy (gas ions → solid)", "electrode
  (reduction) potential", "rate-determining step", "van der Waals' forces", "id-id forces", "pd-pd forces". Syllabus
  definitions from FACTS.md word for word in `:::def` cards.

## Writing chemistry in this course (tested in the preview)
- **mhchem for every formula and equation**: `\(\ce{H2SO4}\)`, `\(\ce{Cu^2+(aq)}\)`, `\(\ce{[Cu(H2O)6]^2+}\)`,
  `\(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\)`, `\(\ce{CuSO4.5H2O}\)`; state symbols instead of gas/precipitate arrows.
  Dipoles `\(\ce{C^{\delta+}-Br^{\delta-}}\)`; in running text plain "δ+" (`\(\delta+\)` renders with a gap).
- Isotopes `\(\ce{^{37}_{17}Cl}\)`. Arrow conditions `\(\ce{A ->[H2SO4][heat] B}\)`, short ("conc." becomes a dot:
  write "concentrated" in the sentence).
- Long inline `\ce` wraps on phones before each arrow and after each ` + ` (write the spaces). The key equation of
  a section goes in display maths `\[\ce{…}\]`. Run `phone` after every chapter.
- Electron configurations as plain text: 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s², [Ar] 3d⁶ 4s² (3d before 4s).
- `\(\Delta H^{\ominus}_{\mathrm{f}}\)`, `\(K_c = \dfrac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}\)`, `\(p_{\ce{NH3}}\)`.
  ICE tables: a Markdown table with short cells.
- Never put a name inside `\ce` (`\ce{-> 2-nitromethylbenzene}` prints italic letters): give the formula in `\ce` and the
  name in `\text{…}` or in the sentence. Captions use Unicode formulas ([Cu(H₂O)₆]²⁺), not `\ce`.
- Organic: condensed formulas in `\ce` (`CH3CH(OH)CH3`, `(CH3)3CBr`); [O] and [H] allowed for organic redox;
  radicals `\(\ce{Cl^.}\)`. In a worked example, number carbons as the name does (or say "the CH₂= carbon").
- Reagents and conditions: the reagent **and** the solvent and conditions every time ("NaOH in ethanol, heat";
  "H₂, Ni catalyst, heat"), each B1.

## Marks and answers in chemistry
- Calculations: B1 for a one-step value (an Mr), M1 per method step, A1 for the answer with unit and s.f. Recall:
  B1 per creditworthy point. Mechanisms: B1 per arrow, dipole, intermediate or transition state, and products.
- Explanations earn marks for named causes ("the C–I bond is weaker", not "iodine is more reactive"; "more
  shielding, larger radius, weaker attraction", not "it is bigger").
- AS exam practice: Paper 1 style (★) and Paper 2 style (★★/★★★); A Level: Paper 4 style, synoptic in ★★★.
- Exam-practice questions use **new numbers**, never a worked example's data (that tests memory, not method). A quiz
  may echo a try question. MCQ options are real misconceptions; at least one quiz question per chapter is a calculation.
- When a calculated value is compared with a table value, check that they really agree, and say why if not.

## Depth and tone
- Readers start from zero: build every idea in small steps. A topic chapter covers every FACTS.md outcome for its
  topics at full exam depth (the gold chapter is ~4500 words for 7 outcomes; big topics are longer).
- Explain *why* (energy, electrons, attraction, stability), then give the exam wording.
- At least one accurate real context per chapter. Never claim how often a topic appears or what it is worth.
- Keep the AS/A Level boundary: never use A Level ideas (rate constant, Ka, conjugate pairs, pH from −log₁₀[H⁺] and
  Kw, which is 25.1) to explain an AS idea. Say it in AS words, or mark it "(A Level link)" with a link
  (e.g. chem.acids2).
- Facts that went wrong before: Sc and Zn are d-block but not transition elements (write "d-block" or "Sc to Zn");
  transition-metal atoms and ions are not "free radicals"; the O and S ionisation-energy dips are spin-pair repulsion,
  never "a half-filled sub-shell is stable"; complex colour comes from a partly filled d sub-shell, not "unpaired electrons"
  (so never give MnO₄⁻, a d⁰ ion, as an example of d–d colour); observations in FACTS.md words ("dark blue solution",
  not "deep blue"); a data value used in two chapters keeps the same digits (chloroethanoic acid pKa 2.86 everywhere).

## Course-wide rules
- **Board boxes**: one board and one content difference you are sure of, never two boards, never "other
  specifications", never first person. Safe examples (packages say which goes where): AQA's Arrhenius equation
  (chem.rates2), atom economy (chem.moles), ozone depletion by CFCs (gold chapter), time-of-flight mass spectrometer
  (chem.analysis), NaBH₄ reduction mechanism (chem.org.carbonyl), biodiesel (chem.org.acids), fuel cells
  (chem.electrochem). Most chapters can have one: look for a safe one before leaving it out.
- **Links**: only ids in course.json or kit/LINKS.md (`grep -i "<word>" kit/LINKS.md`); planned chapters freely.
  Cross-course ids: phys.gases, phys.units, math.f.algebra, math.f.powers (grep first).
- **:::links**: only URLs you have checked, with descriptions that match the page's actual headings (not only the HTTP
  code). Known good: chemguide.co.uk pages (e.g. /mechanisms/nucsubmenu.html, /organicprops/haloalkanemenu.html,
  /organicprops/alcoholmenu.html), https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/ (unofficial).
  Khan Academy answers curl with a bot challenge: leave it out (the one in chem.f.basics was checked in a browser).
- **Facts**: outcomes and data from FACTS.md; colours, observations and test results from its qualitative-analysis
  notes, in their words. Unsure of a fact (melting point, colour, condition)? Leave it out or say it qualitatively.
- **Numbers**: every number in `checks/<id>.py`; Ar from data/elements.json (`json.load`) or the values above.
- **Practicals**: syllabus apparatus only (pipette, burette, volumetric flask, balance to 0.01 g, gas syringe…);
  short, specific safety lines.
- `@paper`: "CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4" for AS topics, "CAIE 9701 Paper 4" for A Level.

## Figures (with kit/STYLE.md "Figures" and "Figure and widget lessons")
Writers cannot see their figures. Plan coordinates in Python, then `shot <id>` and `shot <id> --dark --phone`.
- **Hand SVGs are `fig small`** (viewBox 300–350 wide, so 13 px text on a phone). Use `fig` (viewBox 520–640, never
  380–500) only when the drawing really needs ~600 px: a wide `fig` prints 7–8 px text on a phone. Stack flow charts vertically (boxes ~150 wide, a recycle loop down the side,
  labels in 2–3 short lines); multi-panel pictures in rows; split long labels. Figure scripts (data/mk_fig_*.py)
  emit 300–350-wide viewBoxes too; data/mk_fig_period3.py is stale, do not rerun it.
- Crop the viewBox to the drawing + ~15 px. A 13 px `tl` label is ~7 px per character wide, 13 px tall (baseline at
  y, top at y − 10): keep it ≥ 4 px clear of every line and label. End ordinary arrows ≥ 10 px short of anything
  they do not point at.
- Classes only: never colours, ids, `<defs>`, `<marker>`, `<style>`. Never name colours in captions, text or widget
  notes ("the labelled arcs", "dashed"). `thin`/`thick` change `ln` only; `sw2`/`sw3` on `c1`–`c3`. One path per
  arrow (several `M` subpaths get one head). Same quantity, same class.
- `:::plot`: `--legend tr`; ~30% headroom; point labels ~100 px apart and off tick numbers; `--y` from 0 unless the
  origin is far off; at most two series; cut curves that would cross the axis labels (STYLE.md domain trick).

### Chemistry figure conventions (copy the gold chapter's SVG)
- **Skeletal formulas**: zigzag `ln thick` with 35 px horizontal steps and ±20 px vertical (bond ~40 px, 120°);
  heteroatoms as `tl` text (`tc`), bond ends ~5 px short of the label. OH and NH₂ are drawn; H on carbon is not
  (the aldehyde H may be). Wedge = filled `fi` triangle, hash = `ln` strokes of growing length; bonds ≥ 25 px so
  wedges read. Benzene: a regular hexagon of side ~28 px with an inner circle of radius ~17 px, never alternating
  double bonds.
- **Displayed formulas**: atoms `tl tc`, bonds `ln` stopping ~6 px short of each label; double bond two **parallel** lines
  5 px apart (offset both ends by the same perpendicular vector; data/mk_fig_p15_review.py); every atom and bond.
- **Curly-arrow mechanisms**: `<path class="c1 sw2" d="M x0 y0 Q cx cy x1 y1" marker-end="url(#ahs-red)"/>`, one path
  per arrow, ≥ ~30 px long, starting **at a lone pair or the middle of a bond**, ending ~5–8 px from the receiving
  atom or bond. Lone pairs: two `<circle class="fi" r="1.7">` 6 px apart. Dipoles `δ+`/`δ−` in `tl ta`; charges in
  the text (`C⁺`, `Br⁻`). Transition states in square brackets (`ln`), partial bonds `ln dash`, charge outside the
  top-right corner; intermediates not bracketed. At most three structures per row; multi-step mechanisms stacked
  (gold SN1 figure), step arrows `ln` + `#ah` labelled "step 1 (slow)". Free-radical steps are equations, not drawings.
- **Dot-and-cross**: each symbol inside its own circle, ≥ ~8 px from any other circle's line (move it outwards from
  an overlap); outer atoms labelled at ~1.3 × the centre distance; shared electrons in the overlap, a double bond's
  four in one column when the overlap is narrow.
- **Energy profiles**: `ax` axes (`#ahm`) "enthalpy" / "progress of reaction", no numbers; levels `ln thick`; hump a
  `c1` cubic path; ΔH and Eₐ as two `c2` paths from the middle outwards (`#ah`); catalysed path `c1 dash`.
- **Energy cycles and level diagrams** in `fig small` (~340 wide): species `tl tc` (optionally on a `fm` rect, `rx="8"`),
  arrows `ln` + `#ah`, short labels beside them ("(1) ΔHf"), values as lines of text under the cycle (see
  chem.energetics). Born–Haber: horizontal `ln` levels 30 px apart, arrows up (endothermic) and down (exothermic).
- **Apparatus**: glassware `ln` (round-bottomed flask as an arc with an open neck, gold reflux figure), liquids `fa`,
  solids `fm2`, water and gas arrows `ln` + `#ah`, heat `c2 sw2` + `#ah`; labels to the side with `ln-m thin`
  pointers; no clamps or stands. Condenser water in at the lower end; thermometer bulb level with the side arm.
- **Graphs**: `:::plot` for curves; titration curves by `chem-titration`. Spectra hand SVG on an `ax` baseline, `ts`
  ticks; mass spectra as `c1 thick` lines. Orbitals: s a `fa2` circle, p two `fa` ellipses on `ax` axes.

## Widgets
- Each widget is `widgets/<name>.js` (one `W.register` per file, IIFE), built by its owner package; any chapter may
  use it. Names: `periodic`, `molar` (exact, used by the Toolbox), the rest `chem-…`.
- Element data: `py data/elements.py` writes data/elements.json; embed it with a Python script that writes the JS
  file. Never type element data. Values keep their printed decimals (`ar.toFixed(1)` gives 23.0).
- **Keep every generator in data/** (scratch/ is not backed up): a widget built from data is `data/mk_<name>.py` +
  `data/<name>.tpl.js` (e.g. data/mk_cell.py, data/mk_bornhaber.py); a figure script is `data/mk_fig_<topic>.py`
  (helper data/fig.py; write outputs to scratch/). Fix a generated widget in its template too, then rerun the script.
- Other courses' widgets that fit: `phys-gas`, `units`, `graph` (never register them).
- Owners: periodic P1; chem-config, molar P2; chem-vsepr P3; chem-profile P4; chem-equilibrium P5; chem-titration,
  chem-boltzmann P6; chem-trend P7; chem-chiral P9; chem-orgmap, chem-ms P12; chem-bornhaber, chem-cell P13;
  chem-order P14; chem-dsplit P15; chem-electrophoresis P17; chem-nmr, chem-qa P19. Embed a widget before it exists
  only if your package notes list it; a page must make sense without its widget.
- Fit 375 px with no sideways scrolling: grids and tables switch to a compact layout below ~600 px (a
  `ResizeObserver` on the wrapper; see data/periodic.template.js); canvas drawings stay inside their area at 320 px.
  `W.field` builds a `<label>`: relabel via `el.querySelector('label')`.
- Axis ranges follow the values; legends off the curves; `W.ticks` with `ny` 3 or 4; checkbox rows as in STYLE.md;
  draw chords, not very short thick canvas arcs.
- A widget never prints a fact the theory cannot give: name a real colour, value or observation only for the cases
  FACTS.md or the chapter states (chem-dsplit names colours only for the Cu(II) and Co(II) complexes); otherwise show the trend.
- Dark mode: `sc` (course colour) and `red` look alike, so never use them for two different things in one plot.
- Test every mode: read the readout after each control and arrow key (chem-trend once printed 494.0 kJ mol⁻¹ and an
  electronegativity of "3"); for an animation, press the button in a probe and read the result.
- 3D models (`W.view3d`): start from an asymmetric view (a symmetric projection of a tetrahedron looks like a flat
  cross) and give a depth cue: near bonds thick, far bonds thin and dashed, nearer spheres larger, as in chem-chiral.

## Exam readiness (P20–P23)
- Paper guides: chem.exam.p1, chem.exam.p24 (Papers 2 and 4); chem.practical and chem.planning act as the Paper 3
  and 5 guides. Guides send readers to real past papers and mark schemes (school, Cambridge website, Physics & Maths
  Tutor) without inventing dates or prices.
- Mock papers: `@level mock`, one per written paper, totals exactly as FACTS.md (P1 40, P2 60, P3 40, P4 100, P5 30),
  real times (1 h 15 min, 1 h 15 min, 2 h, 2 h, 1 h 15 min). A part's marks in the question text as "(3 marks)",
  never a bare "[3]"; mark tokens go in the answer lines and add up to the question's `[n marks]`.
