# Zero to A* — plan for finishing the project economically

*Written 1 October 2026 at the end of the setup sessions. This is the master plan for you, the owner. Each Claude work session follows the shorter **SESSION.md** (procedure) and **BRIEF.md** (how to write a chapter) instead of reading this file.*

---

## Start here: how to continue

1. In the Claude app, start a **new task** (do not continue the old conversation) and connect this folder, **Zero to A**.
2. If the app lets you pick a model, choose **Sonnet** for writing packages. It does this job well and uses your limit far more slowly than Opus. Keep Opus for untangling problems.
3. Paste this prompt:

> Continue my Zero to A* project. The folder "Zero to A" is connected. Stage SESSION.md, STATUS.md, dist\backup.json, vendor\node_modules.tgz and vendor\latinmodern-math.otf from it, read SESSION.md and follow it exactly to run the next work package. No clarifying questions, no task list, no subagents, no web searches (one syllabus fetch is fine). Commit every chapter to my folder, publish at the end, then stop and report in three lines.

4. When it reports back, glance at your usage meter. Then start another new task with the same prompt for the next package. **One package per task.**

The first package (WP0) upgrades the engine so every later package is cheap. Run it first.

---

## 1. Where the project stands

| | |
|---|---|
| Published page | **Zero to A\*** (private until you share it): https://claude.ai/artifact/V8KUdftuzroYvq7cp4KPWd, version 2 |
| Offline copy | `dist/zero-to-a-star.html` in this folder opens in any browser |
| Finished pages (27) | Home; Start Here (5 chapters); Preparation Roadmap (15 chapters, including the study-plan generator); Quadratics (the model chapter); Toolbox page shells (4); Practice page |
| Finished widgets (6) | Graph plotter, unit circle, statistics, **study planner**, Pomodoro timer, UCAS calculator |
| Engine | Markdown → one self-contained web page. Formulas render as real maths, light "exam paper" and dark "chalkboard" themes, search, progress tracking, glossary and practice quizzes built automatically |
| Still to do | 168 chapters in 28 content packages, 15 widgets in 3 packages, a one-time engine upgrade (WP0) and a final quality pass (WP32) |

---

## 2. Why it cost so much, and what changes

| What drove the cost | What happened | From now on |
|---|---|---|
| One very long conversation | The old conversation carries all the code, styling, research and agent instructions. Every single step re-reads all of it. | Each package runs in a **fresh, short conversation** that reads only SESSION.md and BRIEF.md (about 4,000 words together). |
| Many agents at once | 15 agents in parallel emptied the limit in minutes. Five agents used a whole window for 20 chapters and 6 widgets. | **No agents.** One conversation writes its own package, one chapter at a time. |
| Agent overhead | Each agent first read about 40,000 tokens of instructions, then took 55–70 steps, and its memory grew at every step. | **3 steps per chapter**: write it, check it, save it. |
| Most expensive model | Every agent ran on Opus. | **Sonnet** for writing. |
| Lost work | After the first limit hit, the cloud machine restarted. Drafts that had not been saved yet vanished (about 2.9 million tokens of work). | **Every finished chapter goes straight into this folder.** Nothing waits until the end of a session. |
| Heavy chapters | 2,500–4,000 words, 8–10 practice questions, hand-drawn diagrams. A single plotted graph is about 2,000 tokens of drawing code. | 1,300–2,000 words, 5 practice questions. **Graphs are generated from one line of text at build time.** Formula sheets are assembled automatically from each chapter's key-facts boxes. |
| Checking with screenshots | Rendering pages and reading images is expensive. | The automatic checker does the checking. Screenshots only for new widgets and in the final QA. |
| Long instructions per agent | Each agent got a long hand-written brief. | Each package fetches the **official Cambridge syllabus** once and uses its learning outcomes as the checklist. This is cheaper and more accurate. |

---

## 3. The new method in one paragraph

A work session restores the project from this folder into the cloud workbench (one small transfer), reads the two short manuals, and fetches the syllabus outcomes for its topics. It then writes each chapter in **one go**, runs the checker and a one-call numeric check, and **saves that chapter to this folder immediately**. At the end it builds the page, publishes it to the same link, saves the built files and a full backup here, adds one line to STATUS.md, and stops. A package is 4–8 chapters, so even if a limit hits mid-package you lose at most the chapter being written. `tools/status.py` always shows what is done and what comes next.

---

## 4. Scope: what stays, what is trimmed

**Kept in full:**
- **The six main subjects** (Mathematics, Physics, Chemistry, Biology, Engineering, Business) cover the whole Cambridge syllabus. Every topic chapter keeps the plain-English start, key-term cards, 3 worked examples (the last one marked like an exam), common mistakes, an exam tip, board differences, 5 practice questions with answers, 3 quick-check questions and a summary.
- Accuracy rules: Cambridge data values, every number re-computed, syllabus checklist per package.

**Trimmed:**
- **Chapter length.** Topic chapters are 1,300–2,000 words (was 2,500–4,000). Course maps are 600–900 words.
- **Economics and Accounting** (the business-related extras) are compact: 1,000–1,500 words.
- **Other subjects** become 3 summary chapters with about 250 words per subject, which is what you asked for.
- **20 merges of small neighbouring topics** (232 planned pages → 201), for example "Temperature", "Ideal gases" and "Thermodynamics" become one "Thermal physics" chapter. Old links keep working through aliases. The full list is in WP0.md.
- **Formula sheets** are generated automatically instead of written by hand.
- **Two minor widgets dropped** (resistor colour code, Hardy–Weinberg). Both calculations stay in the text.

---

## 5. The work packages

Packages run in this order. `tools/wp.json` holds the exact chapter list for each, and `python3 tools/status.py` shows progress.

| Package | Contents | Size |
|---|---|---|
| **WP0** | Engine upgrade: one file per chapter, merges and aliases, one-line graphs, automatic formula sheets | setup |
| **Milestone 1 — Mathematics** | | |
| WP1 | Course map, 3 foundation chapters, Functions, Coordinate geometry, Circular measure, Trigonometry | 8 |
| WP2 | Series, Differentiation, Integration, Algebra (P2/P3), Logarithms, Further trigonometry | 6 |
| WP3 | Further differentiation, Further integration, Numerical methods, Vectors, Differential equations, Complex numbers | 6 |
| WP4 | Data, Permutations, Probability, Binomial and geometric, Normal distribution, Regression (UK) | 6 |
| WP5 | Poisson, Linear combinations, Continuous RVs, Sampling, Hypothesis tests, Further Maths tour | 6 |
| WP6 | Forces, Kinematics, Newton's laws, Momentum, Energy, Projectiles and moments (UK) | 6 |
| WP7 | Widgets: normal, binomial, projectile, waves, half-life | 5 widgets |
| **Milestone 2 — Physics** | | |
| WP8 | Course map, Physics from zero, Units and uncertainty, Kinematics, Dynamics, Forces, Energy | 7 |
| WP9 | Solids, Waves, Superposition, Electricity, D.C. circuits, Particle physics | 6 |
| WP10 | Circular motion, Gravitation, Thermal physics, Oscillations, Electric fields, Capacitance | 6 |
| WP11 | Magnetism and induction, A.C., Quantum, Nuclear, Medical physics, Astronomy, Practical skills | 7 |
| **Milestone 3 — Chemistry** | | |
| WP12 | Course map, Chemistry from zero, Atomic structure, Moles, Bonding, States of matter | 6 |
| WP13 | Energetics, Redox, Equilibria, Kinetics, Lattice energy and entropy, Electrochemistry | 6 |
| WP14 | Acids and buffers, Rate equations, Period 3, Group 2, Group 17, Nitrogen and sulfur, Transition elements | 7 |
| WP15 | Organic introduction, Hydrocarbons, Halogenoalkanes, Alcohols, Carbonyls | 5 |
| WP16 | Acids and derivatives, Arenes, Nitrogen compounds, Polymers, Synthesis, Analysis, Practical | 7 |
| WP17 | Widgets: periodic table, formula mass, circuit, Punnett square, chi-squared, units | 6 widgets |
| **Milestone 4 — Biology** | | |
| WP18 | Course map, Biology from zero, Cells, Molecules, Enzymes, Membranes | 6 |
| WP19 | Mitosis, DNA and protein synthesis, Plant transport, Mammal transport, Gas exchange, Disease | 6 |
| WP20 | Immunity, Respiration, Photosynthesis, Homeostasis, Control and coordination | 5 |
| WP21 | Inheritance, Evolution, Classification and ecosystems, Gene technology, Statistics, Practical | 6 |
| **Milestone 5 — Engineering and Business** | | |
| WP22 | Engineering routes, Maths toolkit, Statics, Materials and beams, Dynamics, Fluids | 6 |
| WP23 | Thermodynamics, Electrical, Electronics and control, Design and manufacturing, Projects | 5 |
| WP24 | Business course map, Business from zero, Enterprise and ownership, Objectives, HRM, Motivation | 6 |
| WP25 | Marketing and research, Marketing mix, Operations, Finance and cash flow, Costs and break-even, Budgets | 6 |
| WP26 | External influences, Strategy tools, Organisation and leadership, Marketing strategy, Location and quality, Operations strategy | 6 |
| WP27 | Financial statements, Ratios, Investment appraisal, Writing top-band answers | 4 |
| WP28 | Widgets: supply and demand, break-even, investment appraisal, ratios | 4 widgets |
| **Milestone 6 — The rest** | | |
| WP29 | Economics: course map, Basic problem, Demand and supply, Elasticity, Market failure | 5 |
| WP30 | Economics: Firms and labour, AD/AS, Growth/unemployment/inflation, Policy, Trade and development | 5 |
| WP31 | Accounting (4 chapters) and Other subjects (3 summary chapters) | 7 |
| WP32 | Final quality pass, polish and publish | QA |

---

## 6. Budget and pacing

**What will it cost?** We will know after WP0 and WP1. The old method used about one full usage window for 20 chapters. The new one cuts cost in four ways at once: a cheaper model, about a third of the steps per chapter, much smaller conversations, and shorter chapters. Expect **at least three times as many chapters per window**, likely more. At three times, that is about 60 chapters per window: roughly three windows for the 168 chapters, plus one for widgets and the final pass. These are estimates, not promises.

**Calibrate once.** Note your usage meter before and after WP0 and WP1. If a package costs X% of a window, you can run about **85 ÷ X** packages per window and still stop before 100%.

**Stop rule.** If you are near your limit, type "usage is high". The session finishes the current chapter, saves it, publishes, and stops.

---

## 7. Safeguards

- **This folder is the master copy.** Every chapter is saved here as soon as it is written. Cloud restarts no longer lose work.
- **Two backups.** `dist/backup.json` (all sources in one file) is updated with every chapter, here and inside the published page.
- **Always resumable.** STATUS.md and `tools/status.py` tell any new session exactly where to pick up.
- **Quality gate.** The checker rejects broken maths, wrong formats, bad links and malformed quizzes. Every number is recomputed. The syllabus outcomes are the coverage checklist. WP32 re-checks a sample of worked examples, looks at the finished page on desktop and phone, and fixes what it finds.
- **The link always works.** Each package ends with a publish to the same address.

---

## 8. If you need it even cheaper

1. **Publish less often.** Publish every third package and read `dist/zero-to-a-star.html` locally in between.
2. **Shorter chapters.** 1,000–1,400 words each.
3. **Fewer widgets.** Keep only normal, binomial, periodic table, formula mass and break-even (saves about two packages).
4. **Do the extras last, or drop them.** Economics, Accounting and Other subjects (WP29–31).
5. **Automate.** Once two packages have gone smoothly by hand, a scheduled task can run the same prompt every few hours and use your limit windows while you are away. Your computer and the Claude app must be on.

---

## 9. What is in this folder

| Path | What it is |
|---|---|
| `HANDOFF.md` | This plan |
| `SESSION.md` | Step-by-step procedure every work session follows |
| `BRIEF.md` | How to write a chapter (short version of AUTHORING.md) |
| `WP0.md` | Spec for the one-time engine upgrade |
| `STATUS.md` | One line per session: what was done, what is next |
| `README.md` | Quick orientation |
| `PLAN.md` | Verified facts (paper structures, admissions tests, dates) checked in October 2026 |
| `OUTLINE.md`, `src/outline.json` | Every chapter id, title, level and group |
| `AUTHORING.md`, `WIDGETS.md` | Full author and widget guides (reference only) |
| `content/` | The chapters (Markdown) |
| `src/` | Page shell, styling, app code, widgets |
| `build.js`, `lib.js` | The builder (Markdown + maths → one web page) |
| `tools/` | Checker, graph generator, progress report, package list, backup, widget tester |
| `dist/index.html` | The built page as published |
| `dist/zero-to-a-star.html` | The same page as a standalone file to open offline |
| `dist/backup.json` | Every source file in one bundle (what sessions restore from) |
| `vendor/` | Maths font and pinned code libraries, so builds do not depend on downloads |

Do not edit `dist/` by hand; it is rebuilt every session.
