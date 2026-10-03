# A Level Guide — build plan (resume file)

User request: comprehensive, zero-knowledge A Level guide artifact; deep on Maths, Physics, Chemistry,
Biology, Engineering, Business; short summaries for other subjects; a preparation roadmap.
Board choice (user answered): **Cambridge-first, all boards** (CAIE main reference; note Edexcel IAL / AQA / OCR differences).
User wants maximal effort ("use all session limits but stop before 100%") -> publish incrementally.

## Architecture
- content/*.md : chapters in Markdown + extensions (see FORMAT below)
- src/manifest.json : subjects, groups, file order
- src/style.css, src/app.js, src/widgets.js : shell
- build.js : md -> html, KaTeX -> MathML (build time), glossary + quiz aggregation, math font subset
- dist/index.html : publish this with Artifact (no doctype/head/body; starts with <title>)
- dist/test.html : local wrapper for Playwright screenshots

## FORMAT
- Chapter header lines: `@chapter id`, `@title`, `@level` (Start/Pre/AS/A2/Guide), `@paper`, `@time`, `@summary`
- Math: \( inline \)  and \[ display \]  (NOT $ — business uses $ for money). Chemistry: \(\ce{H2O}\)
- Blocks: `:::type Title` ... `:::` types: def, eg, tip, warn, exam, analogy, key, note, board, try, quiz
- try: lines `Q: ...` / `A: ...`
- quiz: `? question`, `- wrong`, `+ right`, `> explanation`
- Mark-scheme marks in examples: [M1] [A1] [B1]
- Links to chapters: [text](#chapter.id)
- Widgets: <div class="widget" data-w="graph" data-f="..." ...></div>

## Research facts (verified Oct 2026)
- CAIE 9709: P1 1h50/75 (AS60/AL30), P2 1h15/50 (AS only), P3 1h50/75 (AL30), P4 Mech 1h15/50, P5 S1 1h15/50, P6 S2 1h15/50 (each AS40/AL20)
  AS routes P1+P2, P1+P4, P1+P5; AL: 1,3,4,5 or 1,3,5,6 (not 4+6). Formula list MF19.
- CAIE 9702/9701/9700: P1 MCQ 1h15/40 (31/15.5), P2 AS structured 1h15/60 (46/23), P3 practical 2h/40 (23/11.5), P4 AL structured 2h/100 (38.5), P5 planning 1h15/30 (11.5)
- 9702 topics 1-11 AS, 12-25 AL incl. medical physics + astronomy & cosmology
- 9701 topics 1-22 AS, 23-37 AL; Nernst E = E° + (0.059/z) log([ox]/[red])
- 9700 AS 1-11, AL 12-19; diseases: cholera, malaria, TB, HIV/AIDS; stats: chi2, t-test, Spearman, Pearson, Simpson's D, Hardy-Weinberg, Lincoln index
- 9609 Business: P1 1h15/40 (AS40/AL20), P2 1h30/60 (AS60/AL30), P3 1h45/60 (AL30), P4 1h15/40 (AL20)
- 9708 Econ: P1 MCQ 1h/30 (33/17), P2 2h/60 (67/33), P3 MCQ 1h15/30 (17), P4 2h/60 (33)
- 9706 Accounting: P1 MCQ 1h/30 (28/14), P2 1h45/90 (72/36), P3 1h30/75 (30), P4 1h/50 (20)
- 9231 FM: FP1 2h/75, FP2 2h/75, FM 1h30/50, FS 1h30/50; AS = P1+P3 or P1+P4
- UCAS tariff A*56 A48 B40 C32 D24 E16; AS a20 b16 c12 d10 e6; EPQ A*28..E8
- UCAS 2027 entry: 15 Oct 2026 (Oxbridge/medicine), 13 Jan 2027 equal consideration
- ESAT (UAT-UK, Pearson VUE, 40 min modules, 27 MCQ each): Cambridge, Imperial, Oxford (replaced PAT for 2027 entry), UCL EEE. Sittings Oct 12-16 2026, Jan 4-8 2027
- TMUA: Cambridge, Oxford (replaced MAT), Imperial, LSE, Warwick, Durham, UCL Econ. TARA replaced Oxford TSA. UCAT (medicine), LNAT (law) unchanged.
- CAIE results June 2026 series: 11 Aug 2026. AS can be carried forward within 13 months.
- Engineering: no CAIE Engineering A Level; OCR D&T: Design Engineering H404 (NEA 50%); Eduqas A Level Electronics (2 x 2h45 papers 40% each + NEA 20%); BTEC/T Level; V Levels (England, first teaching Sept 2027)
- Isaac Physics is now Isaac Science (isaacscience.org)
- Turkey: British Council (Istanbul, Ankara) + Pearson-approved schools; Cambridge: May/June, Oct/Nov; Edexcel IAL: Jan, May/June, Oct/Nov

## Status
(see bottom; updated as work proceeds)

## Status log
- Artifact URL: https://claude.ai/artifact/V8KUdftuzroYvq7cp4KPWd (publish dist/index.html with files {"backup.json": "dist/backup.json"})
- Session 1: 15 parallel agents hit the usage limit; container restarted from snapshot; ALL agent drafts lost.
- Session 2 approach: small waves (4-5 agents), agents save each chapter immediately, rebuild + backup + republish after each wave.
- Waves: A start+roadmap+widgets(core) | B maths | C physics+sci widgets | D chemistry | E biology | F eng+business(+biz widgets) | G econ, accounting, other
- v1 published 18:08: start(5), roadmap(15), quadratics, widgets graph/unitcircle/stats/planner/timer/ucas
- Handoff 2026-10-01: project moved to the local folder 'Zero to A'; see HANDOFF.md / SESSION.md. NEXT: WP0
