# COURSE: Accounting (acc)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Accounting (9706)
- Syllabus: https://www.cambridgeinternational.org/Images/697417-2026-2028-syllabus.pdf
- Main board Cambridge International. `:::board` boxes: one other board and one difference you are sure of, or none.

## Data values and conventions
- Money in $ as text. Ledger accounts and financial statements as Markdown tables (Dr/Cr columns).
- Show every calculation; ratios to 2 d.p. unless the question says otherwise.

## Scope (Organizer re-plan, 2026-10-15)
The user wants every course **comprehensive and really helpful**, at the depth of the finished Maths and Physics
courses. course.json now holds a fuller chapter sketch (36 chapters) built from the syllabus structure. It is a
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

## Shared topics with Business, Economics and Accounting (Organizer, 2026-10-15)
Students sit one board's exam, so every course keeps each topic its own syllabus needs, with examples and
questions in its own exam style. The **owner** writes the deepest treatment and builds the widget; the others write
their exam's angle in their own chapter and link to the owner for depth (ids in kit/LINKS.md). Build order:
Economics, then Business, then Accounting, so a widget exists before the later courses embed it.

| Topic | Owner (full chapter, widget) | Others |
|---|---|---|
| Demand, supply, equilibrium, surplus | econ.demand, econ.prices (`supplydemand`) | bus.marketing links |
| Elasticity (PED, YED, XED, PES) | econ.elasticity | bus.mix: pricing decisions, own short section + link |
| Market structures, competition policy | econ.firms, econ.efficiency | bus.external links |
| Inflation, unemployment, interest and exchange rates, the business cycle | econ.inflation, econ.unemployment, econ.money, econ.exchange | bus.external: the effect on firms |
| Labour markets and wages | econ.labour | bus.hrm, bus.motivation link |
| Costs, contribution, break-even | bus.costs (`breakeven`) | acc.marginal: CVP in accounting layout, embeds `breakeven`; econ.costs: cost theory |
| Investment appraisal (payback, ARR, NPV) | bus.investment (`npv`) | acc.investment: the full accounting treatment (and any extra methods 9706 lists), embeds `npv` |
| Ratio analysis | bus.ratios (`ratios`) | acc.analysis, acc.analysis2: accounting depth, embed `ratios` |
| Financial statements | acc.statements, acc.companies | bus.accounts: reading them for decisions, links |
| Budgets and variances | acc.budgets, acc.standard | bus.budgets: the AS business angle |

## Notes for this course
- The old plan had 6 chapters; 9706 needs far more. Check the paper list in the syllabus (multiple choice at AS and
  structured papers) and set the exam-readiness chapters and mocks to match it exactly (one mock per written paper).
- Ledger accounts and statements as Markdown tables with Dr/Cr columns; every calculation shown; ratios to 2 d.p.

## What exists
- No chapters yet. Accounting used to share a section with Economics; it is now its own course (sidebar section "Accounting").
- widgets.js: none yet.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
