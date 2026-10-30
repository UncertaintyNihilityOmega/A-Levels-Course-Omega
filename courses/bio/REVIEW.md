# REVIEW: Biology

Findings for the Writer, newest review at the bottom. One item per line:
`- [ ] <chapter-id>: <exactly what to change>`. The Writer fixes it and changes `[ ]` to `[x]`.
While any `- [ ]` line is open, `status` says FIX.


## REVIEW P1, P2, P3 (2026-10-28), fixed by the reviewer
- [x] bio.microscopy: exam practice reused the worked example's 0.15 µm (now two ribosomes 0.08 µm apart); quiz reused 25 units = 6 divisions and 0.0065 mm (now 40 units = 12 divisions, 0.0048 mm); checks updated
- [x] bio.carbs: exam practice "humans digest starch but not cellulose" repeated the cow worked example; now a germinating pea seed (amylase, starch grains vanish, walls stay)
- [x] bio.lipids: worked example gave a hibernating bear 2000 kJ a day while practice gave a bear 7020 kJ a day; the example is now 7 hours of an adult's sleep; the sweat practice question is now a panting dog
- [x] widget bio-magnify (graticule): switching objective kept the cell at the same number of units, so the same cell changed length (220 µm to 55 µm); now the units scale ×4 and the length stays 150 µm; note reworded
- [x] bio.cells: cilium cross-section drew nine single microtubules; now nine pairs plus two (data/fig_bio.cells.py, stitched)

## REVIEW P4, P5, P7 (2026-10-29), fixed by the reviewer
Re-run whole after the interrupted review. Its partial edits (bio.enzymes2, bio.foodtests, bio.membranes, bio.movement,
bio.planttransport, bio.translocation, checks/bio.foodtests.py, data/fig_bio.movement.py, data/fig_bio.translocation.py,
widgets/bio-sav.js) are complete: every chapter figure matches its generator, all checks pass, bio-sav maths test and
probes pass. Writers' notes confirmed: both `--hline` draw in the non-competitive plot; leaf, marram and loading
figures are fair schematics; the water-loss plot says its data are invented. All 7 chapters pass `check` and `phone`.
- [x] widget bio-enzyme (kinetics): on phones the "Km = …" label ran into the x-axis label; now halfway down the drop line, and "half of Vmax" is shown only when it fits
- [x] widget bio-enzyme (pH): pepsin at pH 5 was called "too alkaline… extra OH⁻ ions"; stages now "below/above the optimum" with H⁺ wording
- [x] bio.movement: plant-cell figure leaders: "vacuole" ended on the wall, "cell surface membrane" ended in the gap; both now end on their part
- [x] bio.movement: Visking tubing results said the dilute glucose outside gives "brick-red"; now green, yellow or orange (lab box and exam answer); facilitated-diffusion plot alt text said it levels off "near 36" (it reaches about 31 on the plot)
- [x] bio.planttransport: transpiration figure had a numbered legend but no numbers on the arrows (added 1, 2, 3); potometer redrawn: shoot tube full of water, capillary dips into an open beaker instead of passing through its wall; water-loss plot curve cut short of the "time / h" label; exam question "explain two features" had a 3-feature answer (now "the structure")
- [x] bio.translocation: ringing figure label "roots (sink)" pointed at stem bark (now "below the ring: towards the roots (sink)"); quiz 63 cm in 30 min gave the worked example's 1.26 m h⁻¹ (now 54 cm → 1.08); exam answer named glycolysis (A Level term) in an AS chapter; stretch "cooled stem" question had no command word and an off-syllabus answer (rewritten: two reasons, then evaluate)
- [x] bio.foodtests: practice reused the serial-dilution example's 1.0% and 0.25% (now 0.8%/0.2% and 3.2% → 0.20%); checks updated
- [x] bio.enzymes2: practice reused the methanol/ethanol worked example (now malonate and succinate dehydrogenase) and the lactase-beads context (reuse question now invertase beads)
- COURSE.md: reuse rule now covers real contexts and answers; new figure rule (leaders end on their part, legend numbers on the drawing, apparatus works as drawn). REQUESTS.md: unchecked checkbox looks ticked in light-mode shots.
No items left for a Writer.

## REVIEW P6, P8, P9 (2026-10-29)
All 9 chapters pass `check` and `phone`; every figure and widget looked at light, dark and phone (`shot`); widget probes
(bio-mitosis, bio-codon, bio-odc, bio-cardiac, with bad attributes) and the four logic tests in data/test_*.js pass.
Read whole: bio.oxygen and bio.heart (every worked example and answer); the rest by worked examples, practice stems,
keys and quizzes; numbers recomputed (Hill curve values, pressure graph readings, mitotic index, codon tables, zone areas).
Writers' notes confirmed: the Hill model, the pressure model and both widgets agree with the chapter values; bpm
rescaling gives the Stretch numbers (60 bpm 0.4/0.6 s, 150 bpm 0.3/0.1 s); antibiotics avoids "allele" and labels
invented data. Fixed by the reviewer:
- [x] bio.mammaltransport: capillary-bed figure was a 560-wide `fig` with 6 px labels on phones; redrawn 340 wide (data/fig_bio.mammaltransport.py, via data/review_capbed.py), and "gap between endothelium cells" now has a leader to a real gap instead of a legend entry with no symbol; red blood cell's pale centre drawn dashed so it no longer looks like a nucleus; capillary "lumen" leader ended on the wall edge
- [x] bio.oxygen: carbon dioxide transport figure was a 600-wide `fig` with 5 px labels on phones; redrawn 340 wide (data/fig_bio.oxygen.py); both dissociation plots had a "120%" tick on the saturation axis (now `--ystep 50`)
- [x] bio.antibiotics: penicillin figure "cross-links" leader ran through the enzyme circle (now from below to a rung)
- [x] bio.gasexchange: alveolus figure drew the red blood cell in the middle of the capillary although the caption says it is squeezed against the wall (moved); diffusion plot showed "0" and "0.5" overlapping at the origin (axis now from 0, curve cut at 0.5)
- [x] bio.heart: pressure graph used the opposite colours to widget bio-cardiac (aorta and ventricle swapped); now the same as the widget
- [x] bio.mitosis: ★★★ spindle-drug data question repeated the chemotherapy worked example's context and answer (and its 500 cells); now an X-ray / G2-check question with new data (checks updated)
- [x] bio.heart: ★★ right-ventricle question part (a) was the wall-thickness worked example again (now right ventricle versus right atrium); ★★ faulty-AVN question part (b) repeated the pacemaker worked example (now why the patient is breathless); aorta "stays above 9.8 kPa" when the table reaches 9.8 (now "never falls below")
- [x] bio.oxygen: ★★★ part (b) reused the altitude worked example (now a mole in a burrow)
- [x] bio.mammaltransport: ★★★ liver-disease oedema and the last quiz question repeated the starvation-oedema worked example's answer (now raised hydrostatic pressure from a weak heart, and a blocked lymph vessel)
- [x] bio.gasexchange: ★★ peak-flow question reused the asthma/reliever worked example (now recovery from bronchitis, same numbers; checks label updated)
- [x] bio.disease: ★ "describe how malaria is transmitted" was the Spot-the-error worked example's question (now why malaria passes in a transfusion but not by touch)
- [x] bio.antibiotics: try question "influenza: why will an antibiotic not help" was the cold worked example's answer (now why an antibiotic can act on a later bacterial chest infection)
- [x] bio.synthesis: try question GAA→GAG duplicated exam practice mutant 1 (now GGC→GGA; checks updated)
- COURSE.md: figure rule (any figure with text labels is `fig small`, 340 wide; leaders never cross another part) and reuse rule examples (a practice question that asks the worked example's question again in other words).
No items left for a Writer.

## REVIEW P10, P11, P12 (2026-10-29)
Read whole: bio.respiration and bio.limiting (every worked example and answer); the rest by worked examples, practice
stems, keys and quizzes; numbers recomputed (antibody curves, RQ equations and respirometer volumes, Krebs tallies,
Rf values, Calvin cycle counts, limiting-factor model curves, inverse square law). Every figure seen in light, dark and
phone; bio-limiting dragged, sliders and presets used, keyboard only; bio-rq both modes, presets, bad inputs, keyboard
only. Writers' notes confirmed: the widget model matches the chapter plots (plateau 40 and 70 at 25 °C, 36 at 15 °C);
30.5 kJ mol⁻¹ and "about 30" ATP are stated as required; the respiration ADP Stretch shares only the isolated-
mitochondria setting with the leaky-membrane example (accepted: different question and mark scheme). Fixed by the reviewer:
- [x] bio-limiting: the "these settings / start settings" legend was drawn on the canvas over the x-axis label and over low plateaus (Too hot, Cold day); now a line of text under the graph, shown only when the curve has moved
- [x] bio.limiting: quiz repeated the inverse-square worked example (10 cm to 20 cm, one quarter; now 30 cm to 15 cm, four times); "the light-dependent stage depends on light, not on temperature" (now "is affected little by temperature"); "isolated chloroplasts cannot fix carbon dioxide" (now: many are broken while grinding and lose the stroma enzymes); temperature plot x-axis ran to 64 °C with the curve stopping at 42 (now 0–50)
- [x] bio.respiration: quiz repeated the leaky-membrane worked example's question and answer (now: by which process protons pass through ATP synthase)
- [x] bio.photosynthesis: quiz Rf used the worked example's 8.0 cm solvent front (now 2.8 ÷ 7.0); Stretch on stopping CO₂ used algae, the organism of the light-off worked example (now bean leaf discs)
- [x] bio.immunity: ★★ antigen A/B part (a) asked the antibody-graph worked example's comparison again (now why anti-A falls between day 21 and 35); quiz "why T-killer cells for a virus inside cells" duplicated the second Stretch (now why the primary response is slow)
- [x] bio.antibodies: ★★★ rabies (antibodies plus vaccine) had the passive/active graph example's mark scheme (now an mRNA vaccine, synoptic with bio.synthesis); plot legend ran into the y-axis label on phones (shorter labels)
- [x] bio.anaerobic: ★★★ alcohol dehydrogenase question used rice, the worked example's plant (now maize seedlings); crucian carp stem said "other mammals and fish" (now "mammals and most other fish")
- [x] bio.energy: quiz respirometer gave RQ 0.50, not a real substrate value (now 25 and 3 mm, RQ 0.88, with matching distractors); RQ-of-seeds plot extended the line to day 0 and day 10 beyond the data (now days 2–8, caption says invented data)
- [x] bio.photosynthesis: chromatogram figure: "solvent level below the origin" sits under the paper with nothing drawn (its line is the paper's bottom edge). In data/fig_bio.photosynthesis.py draw the solvent as an outlined band (`f2 s-acc2 sw2`) across the bottom of the paper, below the origin line, and give the label a leader to it; paste the new figure line
- [x] bio.limiting: the last quiz question (grower raises CO₂, yield does not rise) repeats the last "Start easy" question. Replace it with one on the CO₂ graph: in dim light, raising CO₂ from 0.04% to 0.12% hardly changes the rate; + light is limiting, so too little ATP and reduced NADP; distractors: rubisco is denatured in dim light; carbon dioxide is toxic at 0.12%; carbon dioxide cannot dissolve in the water in the leaf in dim light (keep the explanation line)

## REVIEW P13, P14, P15 (2026-10-29)
Read whole: bio.dihybrid, and every worked example and answer of bio.nerves and the second half of bio.synapses; the
rest by worked examples, keys and quizzes. Numbers recomputed (all chi-squared tables, recombinant percentages,
dihybrid and sex-linked fractions, conduction speeds, refractory frequencies, sarcomere magnifications and bands,
biosensor calibration, urea concentration factor, amplification cascade). Every figure seen in dark (the Writers saw
light and phone); bio-actionpot, bio-sarcomere, bio-punnett (all four modes) and bio-chisq used with clicks and keyboard
only, phone and bad inputs. Writers' notes confirmed: the textbook kidney values and the simplified nephron are fine;
invented data are labelled (glucagon cascade, calcium synapse table, sweet pea and tomato crosses; the Mendel counts are
real); the synapses Stretch (three solutions, evaluate a conclusion, energy of the power stroke) is distinct enough
from the rigor mortis example, which only explains stiffness; the meiosis Stretch questions (Down syndrome, mule) give
the non-disjunction idea in the stem and need only taught ideas, so they stay as A* stretch. Fixed by the reviewer:
- [x] bio.inheritance: pedigree rule 4 said an affected father with an affected son "is not X-linked"; wrong for X-linked recessive when the mother is a carrier (now: the son's allele cannot come from his father, so autosomal only if the mother cannot carry it)
- [x] bio.nerves: the action potential figure numbered the phases 1 resting, 2 depolarisation, 3 peak, 4 repolarisation, 5 hyperpolarisation, while the key table and the widget use resting, depolarisation, repolarisation, hyperpolarisation, recovery; figure labels, list and alt text now match (also in data/fig_bio.nerves.py)
- [x] bio.nerves: frequency plot rose from 0 impulses at zero stimulus, ignoring the threshold (x-axis now "stimulus strength above threshold")
- [x] bio.dihybrid: quiz explanation for the ww epistasis question named genes E and B from the Labrador example
- [x] bio.hormones: barley grain figure: "gibberellin" floated 25 px from its dashed arrow (now beside it; also in data/fig_bio.hormones.py)
- [x] bio-punnett: in two-gene mode the four phenotype-name boxes overlapped each other and the last ran past the card (fixed width 12em in a narrower grid column; now width 100%, max 12em); the "Mother (X^H X^h) makes gametes" line now uses real superscripts (the select options keep X^H, which an option cannot format)
- [x] bio-chisq: on phones the class names broke inside words ("roun-d yello-w") and the empty-chart message was cut off at both ends; names now wrap at spaces, the table scrolls if needed, and the message is shorter on narrow canvases
- [x] bio-sarcomere: "thin and thick overlap" read 1.8 µm at the shortest length, more than the 1.6 µm A band (overlap now capped at the A band; data/test_bio-sarcomere.js updated)

## REVIEW P16, P17, P18 (2026-10-29)
Read whole: every worked example and answer of bio.genetech and bio.biodiversity; the rest by openings, keys,
quizzes and the items in the Writers' notes. Numbers recomputed (t = 5.86, Hardy–Weinberg sets, Spearman rush,
slug and altitude tables, Pearson moss and limpet r, Simpson X/Y and the sewage sites, Lincoln estimates, reserve
core areas, antelope growth, PCR copies, ladder interpolation 1414 and 1516/354 bp, plasmid digests, Bt cotton);
critical values match FACTS.md. All figures and the four widgets looked at in light, dark and phone; bio-gel run
(light and dark, mid-animation), every lane treatment, bad cuts, lengths out of range, Reset, keyboard only;
bio-ttest, bio-hardy (both tabs, all three inputs, N = 10/100/1000) and bio-diversity (three modes, edge cases).
Writers' notes confirmed: P16 lac Q4 table now separates strains 2/3/4, the sickle cell Q gives malaria in the
stem, organisms in quiz/practice differ from the examples, figures fine in dark; P17 Spearman critical values are
in the questions, Lincoln practice numbers differ from the shrimp 240, molecular clock label fixed (below), apple
maggot and palms are qualitative, Pearson formula as FACTS.md; P18 invented data labelled, gel figure fixed (below).
Fixed by the reviewer:
- [x] bio.evolution: molecular clock `:::plot` sat inside the `:::eg` (271 px on phones, x label on the tick numbers); moved after the example with a lead sentence, range 0–12 / 0–70, shorter point labels
- [x] bio.genetech: gel figure sample bands (ink fill) did not match bio-gel's green bands; now course-colour strokes that show in light and dark (data/fig_bio.genetech.py); caption now explains sample 2 (cut only at 1200 bp)
- [x] bio.genetech: plasmid figure drew nothing for step 4 although the alt text described glowing cells, and the plasmid in the bacterium had no gene; step 4 now shows a glowing cell with the plasmid and a cell with none, and the gene is marked in step 3
- [x] bio.genetech: PCR plot label "32 after 5 cycles" was drawn across the curve (now @nw)
- [x] bio.classification: hierarchy figure printed Homo and Homo sapiens upright (now italic, also in data/fig_bio.classification.py)
- [x] bio.selection: sickle cell answer had one token "[M1 A1]" (now "[M1] [A1]")
- [x] bio-hardy: p² showed 0.96 for 0.9604, so p² + 2pq + q² visibly did not add to 1 (4 significant figures now); drift tab drew two of the five lines in near-identical greens (theme series 4 skipped)
- [x] bio-diversity: on phones the Simpson species table was wider than the card, hiding the site-2 counts and the remove buttons (inputs now width 100% with min/max widths)
Open (Writer):
- [x] bio.genetech: the chapter has no `:::exam` box (COURSE.md: every chapter teaches describe ≠ explain in one); add one after the insulin example: "Explain the role of each enzyme" = name the enzyme, what it does, and why it is needed at that step, with the weak/strong pair from that example
- [x] bio.conservation: the chapter has no `:::key` box; add one after the extinction causes (habitat loss and fragmentation, climate change, overexploitation, invasive species, pollution, each with its effect) and one short in situ v ex situ summary
- [x] bio.genetech2: the chapter has no `:::key` box; add one for gene therapy (somatic v germ-line, vectors, ex vivo for SCID) and one for genetic screening (what a positive result does and does not mean)

## REVIEW P19, P20, P21 (2026-10-30)
Read whole: every worked example and answer of bio.stats, bio.evaluation, bio.exam.p24, bio.exam.p35 and bio.exam.p1;
the rest by openings, keys, exam boxes, quizzes and the Writers' notes. Numbers recomputed (aphid mean, root SD/SE/CI,
fertiliser CIs and the error-bar figure, woodlice 24.4, Daphnia t 6.49 from the widget data, Pearson 0.974/0.941,
barnacle and caddis rs, wheat t 2.55, maize 1.47, 0.95^20, cress 28%/45%, catalase CIs, lichen rs 0.964 and the
scatter coordinates, drug SE/CI and bar heights, lettuce t 7.7, HW carriers 792, both tangents in bio.maths, the
skewed-plot gamma mode/mean). Spearman critical values computed exactly (data/spearman_crit.py) and recorded in FACTS;
command-word meanings checked against the syllabus p50 table (scratch/syllabus.pdf) and recorded in FACTS. All
figures looked at in light and in dark + phone; bio-chisq and bio-ttest probed with the chapter data (match the text).
Writers' notes confirmed: P19 equipment and hazards described generically (fine: Paper 3 lists are not in FACTS),
practical2 specimen table correct, grid counts 6, 6, 4, 4 of 200 verified from the SVG; P20 Spearman critical values
are in the questions (n = 12 corrected), distribution plots looked at (fixed, below); P21 command words now verified
(one row corrected), p1 Q5 reuse of the cell drawing is fine, beetroot plan and catalase table original, mark totals ok.
Fixed by the reviewer:
- [x] bio.evaluation: Spearman critical value for n = 12 was 0.591 (an older table); exact two-tailed p = 0.05 value is 0.587 (spot-the-error example and check)
- [x] bio.evaluation: catalase example said "4.7 is above 4.0" for the A/C overlap; C's lower limit is 3.8
- [x] bio.evaluation: quiz "error bars show ± 0.5 SE" read as half an SE; now "± 1 SE, and each standard error is 0.5"
- [x] bio.evaluation: lichen scatter points for 5 m and 10 m overlapped (nine visible circles for ten trees); radius 3.2 (also data/fig_p20.py)
- [x] bio.stats: skewed-distribution curve stopped in mid-air at 80 (y ≈ 10) and the "mode" label sat on the rising curve; now x 0–120, A x² e^(−x/10), mode 20 and mean 30 (caption, alt and check updated), mode label above; normal curve runs to 90 (y ≈ 0)
- [x] bio.exam.p24: command-word table gave "sketch" a non-syllabus meaning ("freehand … proportions"); now the syllabus wording; enzyme plot y step 5 (x kept to 100 so the label clears the curve on phones)
- [x] bio.exam.p35: best-fit curve was drawn from the origin and past 10% (extrapolation, which the chapter forbids); now 2–10% only, y step 0.1. Gel electrophoresis link (loose fit for a practical-papers guide) dropped
- [x] bio.exam.p1: Golgi body (S) in the cell drawing sat on the cell outline at the rounded corner; moved up and right (data/fig_bio.exam.p1.py)
- [x] bio.practical: calibration `:::plot` was inside the `:::eg` (COURSE.md rule); moved after it with a lead sentence; "0" label at 60 °C sat on the curve (now @ne)
- [x] bio.practical2: "lowest power (the ×4 or the ×10 of this paper)": Paper 3 has ×10 and ×40 objectives only; quiz feedback now explains the ×13.5 option
- [x] bio.planning: no `:::exam` box (COURSE.md: describe ≠ explain in every chapter); added "Describe the method, explain the choices" after the range section
- [x] bio.maths: exam box gave "estimate" as a command word and a loose "calculate"; now the syllabus meanings of calculate and determine, with estimate as an extra word
- [x] bio.evolution (P17 open point): molecular-clock x label "time / million years" crowded the 10 and 12 ticks; now "time / 10⁶ years" with the caption explaining it (phone shot clear)
Open (Writer):
- [ ] bio.anaerobic: the yeast-rate `:::plot` (line ~215) is inside the methylene-blue `:::eg` (COURSE.md: a plot goes after the example); end the example after "describe and explain", put the plot after it with a lead sentence, and change any "below" in the example to "after this example"
- [ ] bio.energy: the RQ `:::plot` (line ~340) is inside the germinating-seeds `:::eg`; move it after the example with a lead sentence in the same way
