# COURSE: Biology (bio)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Biology (9700)
- Syllabus: https://www.cambridgeinternational.org/Images/664560-2025-2027-syllabus.pdf
- Main board Cambridge International; Edexcel IAL, AQA and OCR differences go in :::board boxes.

## Data values and conventions
- Statistics in 9700: chi-squared, t-test, Spearman, Pearson, Simpson's index, Hardy–Weinberg, Lincoln index.
- Named diseases: cholera, malaria, tuberculosis, HIV/AIDS.

## What exists
- No chapters yet.
- widgets.js: none yet. Old plan wanted punnett, chisq, hardy.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Suggested merges (old ids become aliases in course.json)
| Keep | New title | Absorbs |
|---|---|---|
| bio.classification | Classification, biodiversity, conservation and ecosystems | bio.ecology |

### Old packages (chapter groups, topics, notes)
- **WP18** Biology: course map, from zero, topics 1-4: bio.overview, bio.f.basics, bio.cells, bio.molecules, bio.enzymes, bio.membranes. Topics: Topics 1 to 4. Notes: bio.overview: 9700 paper table from PLAN.md; Edexcel IAL WBI11-WBI16.
- **WP19** Biology: topics 5-10: bio.mitosis, bio.dna, bio.planttransport, bio.mammaltransport, bio.gasexchange, bio.disease. Topics: Topics 5 to 10. Notes: Named diseases: cholera, malaria, tuberculosis, HIV/AIDS (PLAN.md).
- **WP20** Biology: topics 11-15: bio.immunity, bio.respiration, bio.photosynthesis, bio.homeostasis, bio.control. Topics: Topics 11 to 15
- **WP21** Biology: topics 16-19, statistics, practical: bio.inheritance, bio.evolution, bio.classification, bio.genetech, bio.stats, bio.practical. Topics: Topics 16 to 19; statistics (chi-squared, t-test, Spearman, Pearson, Simpson's index, Hardy-Weinberg, Lincoln index); practical skills. Notes: bio.classification also covers UK-board ecology (energy transfer, nutrient cycles). punnett widget in inheritance, chisq widget in stats.

### Old widget specs
- Do NOT type element data: generate the element table with a Python script (e.g. the periodictable package) into widgets.js (W.ELEMENTS: Z, symbol, British name, Ar to 1 d.p. or [mass number] if no stable isotope, group, period, block, category; configuration computed by Aufbau for Z <= 36 with Cr and Cu exceptions). periodic: 18-column grid + f-block rows, colour by category/block, detail panel, search, scrolls inside its own box on phones. molar: brackets, hydrates (. or ·), coefficients; Mr and % by mass table; friendly errors (Co vs CO). ohm: V, R, internal r; I, terminal p.d., power; simple circuit drawing; I-V line. punnett: monohybrid, dihybrid, X-linked (X^H X^h x X^H Y); gametes, grid, genotype and phenotype ratios. chisq: O/E or ratio like 9:3:3:1; chi-squared, df, critical value at 0.05 for df 1-10 (3.84 5.99 7.81 9.49 11.07 12.59 14.07 15.51 16.92 18.31), conclusion. units: SI prefix table + converter (length, mass, time, volume incl. dm3 and L, energy J/kJ/eV/kWh, pressure Pa/kPa/atm/mmHg, temperature C/K) + standard-form helper.
