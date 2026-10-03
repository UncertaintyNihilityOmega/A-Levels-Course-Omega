# COURSE: Chemistry (chem)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Chemistry (9701)
- Syllabus: https://www.cambridgeinternational.org/Images/664563-2025-2027-syllabus.pdf
- Main board Cambridge International; Edexcel IAL, AQA and OCR differences go in :::board boxes.

## Data values and conventions
- N_A = 6.02 × 10²³ mol⁻¹, R = 8.31 J K⁻¹ mol⁻¹, F = 9.65 × 10⁴ C mol⁻¹, molar gas volume 24.0 dm³ mol⁻¹ at room conditions, specific heat capacity of water 4.18 J g⁻¹ K⁻¹, Kw = 1.00 × 10⁻¹⁴ mol² dm⁻⁶.
- Nernst equation in the Cambridge form E = E° + (0.059/z) log([oxidised]/[reduced]).
- IUPAC/Cambridge spelling: sulfur, aluminium. Use mhchem (\ce{}) for every formula and equation.

## What exists
- No chapters yet.
- widgets.js: none yet. Old plan wanted periodic and molar (generate element data with Python, never type it).

## Widgets other parts of the guide expect from this course
- `periodic` is used by the Toolbox page tools.periodic, and `molar` by tools.calc: build them under those names.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Suggested merges (old ids become aliases in course.json)
| Keep | New title | Absorbs |
|---|---|---|
| chem.lattice | Lattice energy, entropy and Gibbs free energy | chem.entropy |

### Old packages (chapter groups, topics, notes)
- **WP12** Chemistry: course map, from zero, topics 1-4: chem.overview, chem.f.basics, chem.atoms, chem.moles, chem.bonding, chem.states. Topics: Topics 1 to 4. Notes: chem.overview: 9701 paper table from PLAN.md; Edexcel IAL WCH11-WCH16. molar widget in moles.
- **WP13** Chemistry: energetics, redox, equilibria, kinetics, lattice/entropy, electrochemistry: chem.energetics, chem.redox, chem.equilibria, chem.kinetics, chem.lattice, chem.electrochem. Topics: Topics 5 to 8, 23 and 24. Notes: chem.lattice also covers entropy and Gibbs free energy. Nernst in Cambridge form E = E° + (0.059/z) log([oxidised]/[reduced]).
- **WP14** Chemistry: acids/buffers, rate equations, inorganic: chem.acids2, chem.rates2, chem.periodicity, chem.group2, chem.group17, chem.nitrogen, chem.transition. Topics: Topics 25, 26, 9, 10 (+27), 11, 12, 28. Notes: Kw = 1.00 x 10^-14. UK boards add the Arrhenius equation: board box only.
- **WP15** Chemistry: organic part 1: chem.org.intro, chem.org.hydrocarbons, chem.org.halogen, chem.org.alcohols, chem.org.carbonyl. Topics: Topics 13 to 17 (+ A Level 29 to 31). Notes: At most one mechanism SVG per chapter (curly arrows: marker-end url(#ahr)).
- **WP16** Chemistry: organic part 2, analysis, practical: chem.org.acids, chem.org.arenes, chem.org.nitrogen, chem.org.polymers, chem.org.synthesis, chem.analysis, chem.practical. Topics: Topics 18 to 22 and 32 to 37; practical skills. Notes: Synthesis: reaction-map table instead of a big SVG. Practical: ion and gas test tables.

### Old widget specs
- Do NOT type element data: generate the element table with a Python script (e.g. the periodictable package) into widgets.js (W.ELEMENTS: Z, symbol, British name, Ar to 1 d.p. or [mass number] if no stable isotope, group, period, block, category; configuration computed by Aufbau for Z <= 36 with Cr and Cu exceptions). periodic: 18-column grid + f-block rows, colour by category/block, detail panel, search, scrolls inside its own box on phones. molar: brackets, hydrates (. or ·), coefficients; Mr and % by mass table; friendly errors (Co vs CO). ohm: V, R, internal r; I, terminal p.d., power; simple circuit drawing; I-V line. punnett: monohybrid, dihybrid, X-linked (X^H X^h x X^H Y); gametes, grid, genotype and phenotype ratios. chisq: O/E or ratio like 9:3:3:1; chi-squared, df, critical value at 0.05 for df 1-10 (3.84 5.99 7.81 9.49 11.07 12.59 14.07 15.51 16.92 18.31), conclusion. units: SI prefix table + converter (length, mass, time, volume incl. dm3 and L, energy J/kJ/eV/kWh, pressure Pa/kPa/atm/mmHg, temperature C/K) + standard-form helper.
