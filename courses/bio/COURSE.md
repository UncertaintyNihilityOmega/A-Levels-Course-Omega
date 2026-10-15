# COURSE: Biology (bio)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Biology (9700)
- Syllabus: https://www.cambridgeinternational.org/Images/664560-2025-2027-syllabus.pdf
- Main board Cambridge International. `:::board` boxes: one other board and one difference you are sure of, or none.

## Data values and conventions
- Statistics in 9700: chi-squared, t-test, Spearman, Pearson, Simpson's index, Hardy–Weinberg, Lincoln index.
- Named diseases: cholera, malaria, tuberculosis, HIV/AIDS.

## Scope (Organizer re-plan, 2026-10-15)
The user wants every course **comprehensive and really helpful**, at the depth of the finished Maths and Physics
courses. course.json now holds a fuller chapter sketch (41 chapters) built from the syllabus structure. It is a
sketch: check it against the syllabus in LEAD step 2, split any chapter that is still too big, add what is missing,
and keep these ids where you can (aliases for any you rename or merge).
- **Depth:** every topic chapter has every kit/STYLE.md section: worked examples with marks, exam practice ★ to ★★★,
  stretch, quiz, checklist, recap, and a "Learn more online" box.
- **Exam readiness** (the last packages): a guide per paper (or pair of papers), mixed practice for AS and A Level,
  and one mock per written paper, in the real paper's time, marks and question style.
- **Links:** students revise on other sites and apps too, so each topic chapter's `:::links` box sends them to the
  best free ones. LEAD builds the verified link list in COURSE.md (template LEAD step 4).
- **Syllabus years** are in course.json `"years"`. Plan for that syllabus; if the board has published a newer one
  for later exams, add a short note in the overview chapter about what changes.
- **One board** in `:::board` boxes: one board and one content difference you are sure of, or none.

## Notes for this course
- Papers (verify in the syllabus): 1 multiple choice (AS), 2 AS structured, 3 advanced practical skills, 4 A Level
  structured, 5 planning, analysis and evaluation. Mocks for all five; Papers 3 and 5 as written papers with supplied
  observations and data.
- Link chemistry rather than re-teach it: hydrogen bonding, energetics, rates and pH are in the Chemistry course
  (grep kit/LINKS.md for chem.bonding, chem.energetics, chem.kinetics, chem.acids2); statistics methods can link the
  maths course where a chapter exists.
- Widgets from the old plan (below) are still wanted: `punnett`, `chisq`, `hardy`, plus a magnification calculator.

## What exists
- No chapters yet.
- widgets.js: none yet. Old plan wanted punnett, chisq, hardy.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Old widget specs
- Do NOT type element data: generate the element table with a Python script (e.g. the periodictable package) into widgets.js (W.ELEMENTS: Z, symbol, British name, Ar to 1 d.p. or [mass number] if no stable isotope, group, period, block, category; configuration computed by Aufbau for Z <= 36 with Cr and Cu exceptions). periodic: 18-column grid + f-block rows, colour by category/block, detail panel, search, scrolls inside its own box on phones. molar: brackets, hydrates (. or ·), coefficients; Mr and % by mass table; friendly errors (Co vs CO). ohm: V, R, internal r; I, terminal p.d., power; simple circuit drawing; I-V line. punnett: monohybrid, dihybrid, X-linked (X^H X^h x X^H Y); gametes, grid, genotype and phenotype ratios. chisq: O/E or ratio like 9:3:3:1; chi-squared, df, critical value at 0.05 for df 1-10 (3.84 5.99 7.81 9.49 11.07 12.59 14.07 15.51 16.92 18.31), conclusion. units: SI prefix table + converter (length, mass, time, volume incl. dm3 and L, energy J/kJ/eV/kWh, pressure Pa/kPa/atm/mmHg, temperature C/K) + standard-form helper.
