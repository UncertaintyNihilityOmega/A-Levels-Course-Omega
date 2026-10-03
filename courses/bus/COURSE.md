# COURSE: Business (bus)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Business (9609)
- Syllabus: https://www.cambridgeinternational.org/Images/697371-2026-2028-syllabus.pdf
- Main board Cambridge International; Edexcel IAL, AQA and OCR differences go in :::board boxes.

## Data values and conventions
- Money in $ (written as text, e.g. $4.50, never in maths delimiters).
- Assessment objectives: knowledge, application, analysis, evaluation. Worked examples are model answers built step by step, plus calculations.

## What exists
- No chapters yet.
- widgets.js: none yet. Old plan wanted breakeven, npv, ratios.

## Widgets other parts of the guide expect from this course
- `breakeven` and `npv` are used by the Toolbox calculators page (tools.calc): build them under those names.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Suggested merges (old ids become aliases in course.json)
| Keep | New title | Absorbs |
|---|---|---|
| bus.enterprise | Enterprise, business structure and size | bus.structure, bus.size |
| bus.hrm | Human resource management and management | bus.management |
| bus.marketing | Marketing and market research | bus.research |
| bus.operations | Operations, inventory, capacity and outsourcing | bus.inventory |
| bus.finance | Business finance, sources of finance and cash flow | bus.cashflow |
| bus.org | Organisation, communication, leadership and HRM strategy | bus.leadership |

### Old packages (chapter groups, topics, notes)
- **WP24** Business: course map, from zero, topics 1-2: bus.overview, bus.f.basics, bus.enterprise, bus.objectives, bus.hrm, bus.motivation. Topics: 1.1 to 2.3. Notes: bus.overview: 9609 paper table (PLAN.md), assessment objectives (knowledge, application, analysis, evaluation); Edexcel IAL WBS11-WBS14. Worked examples = model paragraphs built step by step, plus calculations where relevant.
- **WP25** Business: marketing, operations, finance (AS): bus.marketing, bus.mix, bus.operations, bus.finance, bus.costs, bus.budgets. Topics: 3.1 to 5.5. Notes: breakeven widget in bus.costs; cash-flow forecast table in bus.finance.
- **WP26** Business: A Level strategy, people, marketing, operations: bus.external, bus.strategy, bus.org, bus.marketing2, bus.location, bus.opsstrategy. Topics: 6.1 to 9.3. Notes: One critical-path network SVG in bus.opsstrategy; elasticity calculations in bus.marketing2.
- **WP27** Business: accounts, ratios, investment, writing: bus.accounts, bus.ratios, bus.investment, bus.writing. Topics: 10.1 to 10.4. Notes: ratios and npv widgets. bus.writing: how 9609 papers are marked, with model answers.

### Old widget specs
- supplydemand: shift and tilt demand/supply, equilibrium, consumer/producer surplus, optional price ceiling/floor and indirect tax incidence; axes Price ($) and Quantity. breakeven: data-fc, data-price, data-vc + planned output; contribution, break-even output rounded up, break-even revenue, margin of safety, profit; chart. npv: investment, cash flows years 1-6 (editable), rate; payback (years and months), ARR, NPV with discount factors to 3 d.p. ratios: gross and operating margin, ROCE, current ratio, acid test, inventory turnover, receivables and payables days, gearing, dividend yield, P/E; formula + one-line meaning each; realistic example pre-filled.
