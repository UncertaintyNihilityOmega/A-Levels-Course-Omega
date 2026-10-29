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
