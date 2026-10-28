# COURSE: Biology (bio)

Cambridge International AS & A Level Biology 9700, syllabus for exams in 2025, 2026 and 2027 (version 1, September
2022). Every Writer reads this file, kit/STYLE.md, the gold chapter `chapters/bio.enzymes.md` and their own
`packages/Pn.md`. Nothing else is needed. Paper details come only from FACTS.md (grep it: `grep -n "^- 8.2" FACTS.md`).
Your package file already holds the full outcome wording for your chapters.

## Gold chapter
**`bio.enzymes`** (Enzymes) is the model: copy its structure, tone, depth, mark style and figure style. It has every
kit/STYLE.md section. Read it whole before you write anything. Its plan is in packages/P4.md; the LEAD session
writes it before any Writer starts.

## Scope and papers (from FACTS.md)
- AS = topics 1–11 (Papers 1, 2, 3). A Level = topics 1–19 (adds Papers 4 and 5). AS content is assumed in Paper 4.
- Paper 1: 40 four-option multiple-choice questions, 1 h 15 min, 40 marks, one mark each, no penalty for a wrong
  answer. Paper 2: AS structured, 1 h 15 min, 60 marks. Paper 3: Advanced Practical Skills, 2 h, 40 marks, two or
  three questions (one investigation, one microscope and photomicrograph task). Paper 4: A Level structured, 2 h,
  100 marks. Paper 5: Planning, Analysis and Evaluation, 1 h 15 min, 30 marks, written.
- **Every paper allows a calculator. No paper has a data booklet, formula sheet or data table at the back.** A
  statistics formula is printed inside the question that needs it (A Level only), and a table of critical values is
  given when needed; degrees of freedom are never given. Never write "use the formula sheet" or "data booklet".
- `@paper` lines: AS topic chapters `CAIE 9700 Papers 1, 2 (and 3)`; A Level chapters `CAIE 9700 Paper 4 (and 5)`.
  Put Paper 3 only where the chapter has a practical the syllabus names; Paper 5 only for chapters with statistics or
  planning content. No other boards in `@paper`.

## Depth, tone and structure
- Readers are beginners who did GCSE or IGCSE science (or less). Start every idea from zero, then climb to full
  exam depth. Every learning outcome in your package notes must be taught, practised and examined in the chapter.
- Biology marks are mostly **marking points**: one creditworthy idea = one mark. Teach students to write in
  mark-scheme language: precise terms ("active site", "complementary shape", "enzyme–substrate complexes",
  "water potential gradient", "partially permeable membrane"), cause → effect chains, and data quoted with units.
- Each topic chapter: `:::why`, warm-up, sections built in small steps, `:::def` cards (syllabus wording), `:::key`
  boxes, figures, at least 4 `:::eg` (one a full exam-style question with marks, one in a real context such as a
  disease, crop, medicine or experiment), a `:::eg Spot the error`, `:::warn` and `:::exam` boxes, a `:::try` set
  (6–10 graded questions), `:::try Exam practice ★ to ★★★` (6–8 questions, data and graphs included, the last
  ones synoptic), `:::try Stretch for A*` (1–2 unfamiliar contexts), `:::quiz` (6+ questions, wrong options are
  real misconceptions), `:::checklist`, `:::recap`, `:::links`, `Next:`.
- Explanations questions ("Explain why …") are the heart of biology papers: in worked examples show the model answer
  built point by point, then say what a weaker answer misses.
- **Data handling** in every topic chapter: at least one question with a table or a `:::plot` graph to read,
  describe ("describe the trend", quoting figures with units, naming the turning point) and explain.
- Practical outcomes named in the syllabus ("investigate", "describe and carry out") get a `:::lab` box: aim,
  method in steps, variables (IV, DV, standardised), control, typical results, sources of error, safety.
- **AS chapters never use A Level terms or methods** (no statistics tests, no respiration stages, no Km in AS
  chapters other than bio.enzymes2, which is AS). If a link forward helps, one sentence pointing to the later chapter.
- **Practice questions never reuse a worked example's data or organism.** New numbers, new context.
- Length: as long as the topic needs (the gold chapter is about 790 lines, half of it practice). No padding.

## Format lessons from the gold chapter (each one cost a fix)
- Worked examples: no `[n marks]` in the `:::eg` title. The page adds up the tokens and shows the total. A Spot the
  error title may end with the marks available, `[3]`; its header then shows what the student scored.
- Data tables: the independent variable in the left column and one row per value (Cambridge layout). Table headings
  never wrap, so keep each table's headings under about 28 characters in total (`| time / s | oxygen / cm³ |`); put
  the long description in the sentence above. Tables work inside `:::eg` and inside a `:::try` question (blank line
  before and after).
- Display maths in a worked example: one step per row (`\begin{aligned} … \\ &= … \end{aligned}`) so it fits phones.
- `:::plot` formulas are parsed as JavaScript: never a unary minus before `**` (`exp(0-((x-2)/1.3)**2)`, not
  `exp(-((x-2)/1.3)**2)`). Cut curves that run along the x-axis short with `+0*sqrt(a-x)`.
- Hand SVGs: copy the `Fig` class in `data/fig_bio.enzymes.py`. It writes the SVG and checks every label box against
  every edge, leader and other label (4 px clearance) before you paste the output into the chapter.

## Marks in biology answers (how `check` adds them)
- Each marking point ends with `[B1]`. Calculations use `[M1]` (method) and `[A1]` (answer). `check` adds the tokens in
  every answer and worked example and compares them with `[n marks]`, so **an answer carries exactly n tokens**.
- Mark schemes often accept "any 3 from 5". Write the n best points with tokens, then extra creditworthy points
  without tokens in brackets: `(Also credit: … ; … .)` Never put `max` inside brackets.
- Command words (syllabus page 50, meanings in FACTS.md): describe ≠ explain. "Describe" a graph = trend + figures
  with units; "explain" = biological reason. Teach this in every chapter's `:::exam` box at least once.

## Conventions and data
- British spelling and Cambridge terms: haemoglobin, sulfur, oesophagus, fibre, neurone, Purkyne tissue (syllabus
  spelling), Golgi body, reduced NAD and reduced NADP (never NADH/NADPH), triose phosphate (TP), glycerate
  3-phosphate (GP), ribulose bisphosphate (RuBP), rubisco, link reaction, Krebs cycle, ATP synthase, T-helper and
  T-killer cells, B-lymphocytes, plasma cells, tissue fluid, sieve tube elements, xylem vessel elements, Visking
  tubing, assimilates, Casparian strip, water potential (symbol \(\psi\), units kPa; pure water 0 kPa, all solutions
  negative; **solute and pressure potential are not used** at AS).
- Units: mm, µm, nm (1 mm = 1000 µm, 1 µm = 1000 nm); kPa for pressures and water potential; cm³ and dm³; °C; mol
  dm⁻³ or % (w/v) for concentrations. Write units upright: `\(25\,\mathrm{\mu m}\)` or plain "25 µm" in prose.
- Magnification: \(M = I/A\) (image size ÷ actual size, same units). Resolution: light microscope about 200 nm
  (0.2 µm); transmission electron microscope about 0.5 nm in practice. Do not quote other resolution values.
- Significant figures: an answer gets the same number as, or one more than, the least precise data (syllabus rule).
  Cambridge accepts that, so state the answer at the sig figs of the data and show the unrounded value in working.
- Formulae (`\ce{}` for chemistry in biology): `\(\ce{C6H12O6 + 6O2 -> 6CO2 + 6H2O}\)`. In `\ce{}` a hyphen at the
  end of a bond fragment renders as a negative charge: write the end bond outside `\ce` (`\(\ce{-CH2}\)–` style
  fragments as plain text "–CH₂–"). Ions: `\(\ce{Cl-}\)`, `\(\ce{HCO3-}\)`, `\(\ce{Ca^2+}\)`, `\(\ce{H+}\)`.
- Statistics values: critical values and formulae in FACTS.md ("Statistics"). Check scripts import
  `data/crit.py` (see its header) instead of typing table values.
- Never invent numbers for real biology that a reader could check (sizes, rates, concentrations): use well-known
  textbook values (red blood cell about 7 µm across; bacterium 1–5 µm (syllabus); human body temperature 37 °C;
  blood glucose about 4–6 mmol dm⁻³ normally; resting potential about −70 mV; action potential peak about +30 to
  +40 mV; energy density of respiratory substrates about 16 kJ g⁻¹ carbohydrate, 39 kJ g⁻¹ lipid, 17 kJ g⁻¹
  protein) or clearly invented data in a described experiment.

## Figures and widgets
- No photographs exist in this guide. Where the syllabus says "photomicrograph" or "electron micrograph", draw a
  clean labelled SVG of what the student would see, say in the caption that it is a drawing, and teach how to
  recognise the real thing in words ("in a photomicrograph the nucleus stains darkest …").
- Hand SVGs are **`class="fig small"` by default** (viewBox about 300–350 wide). Full-width figures had 7–8 px text on
  phones; use `fig` (viewBox 520–640) only for wide diagrams that need it, and `fig wide` only for multi-panel ones.
- Dark mode: a pale fill without an outline vanishes. Give every filled shape an outline (`f1 s-acc sw2`, or a `ln`
  stroke). Never name colours in captions or text.
- Keep every figure and widget generator script in **data/** (scratch/ is not backed up). Python that computes SVG
  coordinates goes in `data/fig_<chapter>.py`.
- Graphs of functions or data: `:::plot` (kit/STYLE.md). For data points, `--pt` labels; at most two series.
- Widgets: one file each, `widgets/<name>.js`, names start `bio-`. Each belongs to exactly one package (course.json).
  Rules learned in Chemistry: draw must survive zero width and height (return early if `w <= 0 || h <= 0`); state
  facts only from FACTS.md or the chapter that uses it; 3D views start from an asymmetric angle and show a depth cue;
  every animation must be clicked through and checked in the browser pane, not just probed.
- Widgets from other courses you may use: `normal`, `stats`, `sampling` (math), `units` (phys), `molar` (chem). Do not
  register those names.

## Multiple choice (quizzes, Paper 1 guide, Mock Paper 1)
- Options in mocks: one paragraph each, blank line between them, bold letter: `**A** …` (kit/STYLE.md "Mock papers").
  Four options A–D, exactly one correct.
- Paper 1 style: data, diagrams and tables in the stem; options that test a precise misconception; "Which row is
  correct?" tables with ✓ and ✗ (four rows A–D). Every option is plausible.

## Board boxes
- **Topic chapters: no `:::board` box.** We cannot verify topic-level differences between boards reliably, and a wrong
  claim is worse than none.
- The course map (bio.overview) and the paper guides may have one `:::board` box naming one board with one difference
  that is certain: AQA A Level Biology (7402) assesses practical skills in its written papers plus a separately
  reported practical endorsement, with no timed hands-on practical exam (unlike Cambridge Paper 3).

## Links to other courses (grep kit/LINKS.md for exact ids)
- Chemistry, link rather than re-teach: hydrogen bonding and polarity (chem.bonding), activation energy and catalysts
  (chem.kinetics, chem.energetics), buffers and pH (chem.acids, chem.acids2), amino acids and peptides
  (chem.org.nitrogen), condensation polymers (chem.org.polymers), electrophoresis (chem.org.nitrogen).
- Maths: normal distribution (math.s1.normal), data summaries (math.s1.data), hypothesis testing (math.s2.hypothesis).
- Formula sheet: tools.f.bio (Toolbox). Glossary: tools.glossary.

## Verified link list for `:::links` (each checked 200 on 24 October 2026)
Use only these URLs (or ones in your package notes). Mark paid sites `[paid]` and unofficial past papers `[unofficial]`.
- read + practise: Physics & Maths Tutor, CAIE A Level Biology topic notes and topic questions (free). Topic pages:
  `https://www.physicsandmathstutor.com/biology-revision/a-level-cie/<slug>/` with slug one of cell-structure,
  biological-molecules, enzymes, cell-membranes-transport, mitotic-cell-cycle, nucleic-acids-protein-synthesis,
  transport-in-plants, transport-in-mammals, gas-exchange-smoking, infectious-disease, immunity,
  energy-and-respiration, photosynthesis, homeostasis, control-and-coordination, inherited-change,
  selection-and-evolution, biodiversity-classification-conservation, genetic-technology, practical-skills.
- papers: Physics & Maths Tutor past papers by paper `[unofficial]`:
  `https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-1/` (…`cie-paper-2/` to `cie-paper-5/`).
- read + practise: Save My Exams, CAIE A Level Biology (9700, exams from 2025) `[paid]` (some notes free): topic pages
  `https://www.savemyexams.com/a-level/biology/cie/25/topics/<n>-<slug>/` with 1-cell-structure,
  2-biological-molecules, 3-enzymes, 4-cell-membranes-and-transport, 5-the-mitotic-cell-cycle,
  6-nucleic-acids-and-protein-synthesis, 7-transport-in-plants, 8-transport-in-mammals, 9-gas-exchange,
  10-infectious-diseases, 11-immunity, 12-energy-and-respiration, 13-photosynthesis, 14-homeostasis,
  15-control-and-coordination, 16-inheritance, 17-selection-and-evolution,
  18-classification-biodiversity-and-conservation, 19-genetic-technology. Also
  `https://www.savemyexams.com/a-level/biology/cie/25/flashcards/` and `…/cie/25/topic-questions/`.
- watch: Amoeba Sisters (YouTube) `https://www.youtube.com/@AmoebaSisters/videos`: short cartoon explanations (GCSE
  to AS level; say "a friendly first explanation").
- watch: Cognito, CAIE A Level Biology videos and questions `https://cognito.org/specifications/alevel/biology/cie`.
- read: OpenStax Biology 2e (free university-level textbook, beyond the syllabus in places):
  `https://openstax.org/books/biology-2e/pages/<n>-introduction` with n = 3 macromolecules, 4 cell structure, 5 plasma
  membranes, 6 metabolism and enzymes, 7 cellular respiration, 8 photosynthesis, 9 cell communication, 10 cell
  reproduction, 11 meiosis, 12 Mendel, 14 DNA structure and function, 15 genes and proteins, 16 gene expression,
  17 biotechnology and genomics, 18 evolution and speciation, 19 evolution of populations, 20 phylogenies,
  21 viruses, 22 prokaryotes, 30 plant form and physiology, 35 nervous system, 38 musculoskeletal system,
  39 respiratory system, 40 circulatory system, 41 osmotic regulation and excretion, 42 immune system,
  45 population and community ecology, 47 conservation biology.
- explore: PhET simulations `https://phet.colorado.edu/en/simulations/<slug>`: neuron, membrane-transport,
  gene-expression-essentials, natural-selection.
- explore: Learn.Genetics (University of Utah): `https://learn.genetics.utah.edu/content/basics/` (DNA, genes,
  proteins), `…/content/basics/transcribe/` (transcribe and translate a gene), `…/content/labs/gel/` (gel
  electrophoresis), `…/content/labs/pcr/` (PCR), `…/content/evolution/`, `…/content/cells/`.
- read: Khan Academy Biology `https://www.khanacademy.org/science/biology` (root page only).
- read: ZNotes CAIE notes `https://znotes.org/caie/as-biology-9700/` and `https://znotes.org/caie/a2-biology-9700/`.
End each `:::links` block with: `Links checked 24 October 2026.` (Khan Academy, PhET and ZNotes answer 200 even for wrong
paths, so only the exact URLs above count as checked: PhET slugs were confirmed through their simulation files.)

Links checked 24 October 2026.

## Packages
| Package | Chapters | Widgets |
|---|---|---|
| P1 Start here | bio.overview, bio.f.basics | – |
| P2 Cells and microscopes | bio.microscopy, bio.cells, bio.prokaryotes | bio-magnify |
| P3 Biological molecules | bio.carbs, bio.lipids, bio.proteins | – |
| P4 Food tests and enzymes | bio.foodtests, **bio.enzymes (gold, LEAD writes it)**, bio.enzymes2 | bio-enzyme |
| P5 Membranes | bio.membranes, bio.movement | bio-sav |
| P6 Cell cycle, DNA, protein synthesis | bio.mitosis, bio.dna, bio.synthesis | bio-mitosis, bio-codon |
| P7 Transport in plants | bio.planttransport, bio.translocation | – |
| P8 Transport in mammals | bio.mammaltransport, bio.oxygen, bio.heart | bio-odc, bio-cardiac |
| P9 Gas exchange, disease, antibiotics | bio.gasexchange, bio.disease, bio.antibiotics | – |
| P10 Immunity | bio.immunity, bio.antibodies | – |
| P11 Energy and respiration | bio.energy, bio.respiration, bio.anaerobic | bio-rq |
| P12 Photosynthesis | bio.photosynthesis, bio.limiting | bio-limiting |
| P13 Homeostasis and plant control | bio.homeostasis, bio.glucose, bio.hormones | – |
| P14 Nerves and muscles | bio.nerves, bio.synapses | bio-actionpot, bio-sarcomere |
| P15 Meiosis and crosses | bio.meiosis, bio.inheritance, bio.dihybrid | bio-punnett, bio-chisq |
| P16 Gene control, variation, selection | bio.genecontrol, bio.variation, bio.selection | bio-ttest, bio-hardy |
| P17 Evolution, classification, biodiversity | bio.evolution, bio.classification, bio.biodiversity | bio-diversity |
| P18 Conservation, genetic technology | bio.conservation, bio.genetech, bio.genetech2 | bio-gel |
| P19 AS skills | bio.maths, bio.practical, bio.practical2 | – |
| P20 A Level skills | bio.stats, bio.planning, bio.evaluation | – |
| P21 Paper guides | bio.exam.p1, bio.exam.p24, bio.exam.p35 | – |
| P22 AS mixed and mocks | bio.mixed.as, bio.mock.p1, bio.mock.p2 | – |
| P23 A Level mixed and Mock 4 | bio.mixed.a2, bio.mock.p4 | – |
| P24 Practical mocks | bio.mock.p3, bio.mock.p5 | – |
Topic packages P2–P18 come first (in that order); P1 and the skills packages P19–P20 can run any time; exam
readiness P21–P24 last (they draw on every chapter). Writers work two at a time; reviews take three packages.
