# COURSE: Economics (econ)

> **Starting notes from the Organizer (2026-10-03).** The Specialist's LEAD session rewrites this file into the
> real course plan (see CLAUDE.md, LEAD step 4). Everything under "Ideas from the old plan" is optional.

## Course
- Cambridge International AS & A Level Economics (9708)
- Syllabus: https://www.cambridgeinternational.org/Images/697423-2026-2028-syllabus.pdf
- Main board Cambridge International; Edexcel IAL, AQA and OCR differences go in :::board boxes.

## Data values and conventions
- Money in $ as text. Diagrams (supply and demand, cost curves, AD/AS) with :::plot straight lines and --noticks, or a supplydemand widget.
- Worked examples are model answers (knowledge → application → analysis → evaluation) plus calculations (elasticity, multipliers).

## What exists
- No chapters yet. Economics and Accounting used to be one section; they are now separate courses.
- widgets.js: none yet. Old plan wanted supplydemand.

## Gold chapter
(The Specialist names the course's gold chapter here in LEAD.)

## Packages
(The Specialist lists them in course.json "packages" and describes them here.)

## Ideas from the old plan
### Suggested merges (old ids become aliases in course.json)
| Keep | New title | Absorbs |
|---|---|---|
| econ.firms | Costs, market structures and labour markets | econ.labour |
| econ.trade | Trade, exchange rates, development and globalisation | econ.development |

### Old packages (chapter groups, topics, notes)
- **WP29** Economics part 1: econ.overview, econ.basics, econ.demand, econ.elasticity, econ.intervention. Topics: Topics 1 to 3, 7.3, 7.4, 8.1, 8.2. Notes: Diagrams via :::plot straight lines with --noticks; supplydemand widget in econ.demand.
- **WP30** Economics part 2: econ.firms, econ.macro, econ.growth, econ.policy, econ.trade. Topics: Topics 4 to 6 and 7.5 to 11.6. Notes: econ.firms includes labour markets; econ.trade includes development and globalisation.

### Old widget specs
- supplydemand: shift and tilt demand/supply, equilibrium, consumer/producer surplus, optional price ceiling/floor and indirect tax incidence; axes Price ($) and Quantity. breakeven: data-fc, data-price, data-vc + planned output; contribution, break-even output rounded up, break-even revenue, margin of safety, profit; chart. npv: investment, cash flows years 1-6 (editable), rate; payback (years and months), ARR, NPV with discount factors to 3 d.p. ratios: gross and operating margin, ROCE, current ratio, acid test, inventory turnover, receivables and payables days, gearing, dividend yield, P/E; formula + one-line meaning each; realistic example pre-filled.
