# COURSE: Physics (phys)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Physics (9702)
- Syllabus: https://www.cambridgeinternational.org/Images/664565-2025-2027-syllabus.pdf
- Main board Cambridge International; Edexcel IAL, AQA and OCR differences go in :::board boxes.

## Data values and conventions
- g = 9.81 m s⁻² (9702). Data sheet values: c = 3.00 × 10⁸ m s⁻¹, e = 1.60 × 10⁻¹⁹ C, h = 6.63 × 10⁻³⁴ J s, N_A = 6.02 × 10²³ mol⁻¹, R = 8.31 J K⁻¹ mol⁻¹.
- Cambridge first law of thermodynamics: ΔU = q + W, with W the work done ON the system.
- Significant figures follow the data in the question.

## What exists
- No chapters yet.
- widgets.js: none yet. Old plan wanted wave, halflife, ohm, units, resistor.

## Widgets other parts of the guide expect from this course
- `units` (SI prefixes and unit converter) is used by the Toolbox calculators page (tools.calc): build it under that name.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Suggested merges (old ids become aliases in course.json)
| Keep | New title | Absorbs |
|---|---|---|
| phys.temperature | Thermal physics: temperature, ideal gases and thermodynamics | phys.gases, phys.thermo |

### Old packages (chapter groups, topics, notes)
- **WP8** Physics: course map, from zero, AS topics 1-5: phys.overview, phys.f.basics, phys.units, phys.kinematics, phys.dynamics, phys.forces, phys.energy. Topics: Topics 1 to 5. Notes: phys.overview: 9702 paper table from PLAN.md; Edexcel IAL units WPH11-WPH16 (WPH13 and WPH16 are written practical papers); AQA 7408 + Practical Endorsement. g = 9.81. units widget in phys.units; projectile widget in kinematics.
- **WP9** Physics: AS topics 6-11: phys.solids, phys.waves, phys.superposition, phys.electricity, phys.dc, phys.particles. Topics: Topics 6 to 11. Notes: wave widget (single / stationary); ohm widget in electricity; one circuit SVG in d.c. circuits.
- **WP10** Physics: A Level topics 12-19: phys.circular, phys.gravity, phys.temperature, phys.oscillations, phys.efields, phys.capacitance. Topics: Topics 12 to 19. Notes: phys.temperature covers topics 14, 15 and 16 (temperature, ideal gases, thermodynamics). Cambridge first law: dU = q + W with W the work done ON the system.
- **WP11** Physics: A Level topics 20-25 and practical skills: phys.magnetic, phys.ac, phys.quantum, phys.nuclear, phys.medical, phys.astro, phys.practical. Topics: Topics 20 to 25; Paper 3 and Paper 5 skills. Notes: halflife widget in nuclear. Practical: uncertainties, log graphs, planning.

### Old widget specs
- normal: mu, sigma, a, b; shade between/below/above; probability to 4 s.f.; Phi via erf with error < 1e-7. binomial: n 1-50, p; bars; highlighted range with cumulative probability; mean np, variance np(1-p); optional normal overlay. projectile: speed, angle, launch height 0-20 m, g presets 9.81/9.8/10; range, time of flight, max height; components at a chosen time; launch animation (respect reduced motion); faint previous paths + clear. wave: data-mode single (A, wavelength, f, v = f lambda) | superpose (two waves + resultant) | stationary (string fixed at both ends, harmonic slider, nodes/antinodes); play/pause, paused under reduced motion. halflife: n0, half-life; dashed half-life markers; lambda = ln2/t_half; N at a chosen t; seeded random decay of up to 400 dots vs the smooth curve.
- Do NOT type element data: generate the element table with a Python script (e.g. the periodictable package) into widgets.js (W.ELEMENTS: Z, symbol, British name, Ar to 1 d.p. or [mass number] if no stable isotope, group, period, block, category; configuration computed by Aufbau for Z <= 36 with Cr and Cu exceptions). periodic: 18-column grid + f-block rows, colour by category/block, detail panel, search, scrolls inside its own box on phones. molar: brackets, hydrates (. or ·), coefficients; Mr and % by mass table; friendly errors (Co vs CO). ohm: V, R, internal r; I, terminal p.d., power; simple circuit drawing; I-V line. punnett: monohybrid, dihybrid, X-linked (X^H X^h x X^H Y); gametes, grid, genotype and phenotype ratios. chisq: O/E or ratio like 9:3:3:1; chi-squared, df, critical value at 0.05 for df 1-10 (3.84 5.99 7.81 9.49 11.07 12.59 14.07 15.51 16.92 18.31), conclusion. units: SI prefix table + converter (length, mass, time, volume incl. dm3 and L, energy J/kJ/eV/kWh, pressure Pa/kPa/atm/mmHg, temperature C/K) + standard-form helper.
