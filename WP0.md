# WP0 — one-time engine upgrade (run before any content package)

Goal: make every later session cheap. Work in /home/claude/zta after the normal session start
(SESSION.md). Read build.js, lib.js, tools/check.js and tools/make_outline.py before editing (they are
short). Change them with Edit or small python patches, not full rewrites.

## 1. One chapter per file
- New chapters live in content/<subject>/<chapter-id>.md.
- build.js: find chapters by globbing content/**/*.md (recursive), render every file, then order and group
  chapters from src/outline.json (subject order, chapter order, group titles). Ignore @group lines. Keep the
  existing multi-chapter files working (home.md, start.md, roadmap-1.md, roadmap-2.md, math-1a.md,
  tools.md, practice.md); do not split or delete them. Replace the "missing files" message with a count of
  outline chapters not written yet.
- A chapter id that is not in the outline (after alias resolution) is an error; duplicate ids are errors.
- tools/check.js: accept any file under content/; validate each chapter id against the outline and aliases;
  drop the "expected chapters in this file" and order checks.

## 2. Merges and aliases
Edit tools/make_outline.py: remove the absorbed ids, give each surviving chapter its new title, add an
`aliases` map (old id → surviving id) to outline.json, then run it (it also regenerates OUTLINE.md,
including an Aliases section).

| Surviving id | New title | Absorbs |
|---|---|---|
| math.f.numbers | Numbers, powers, surds and standard form | math.f.powers |
| math.f.graphs | Graphs, geometry and trigonometry basics | math.f.geometry |
| phys.temperature | Thermal physics: temperature, ideal gases and thermodynamics | phys.gases, phys.thermo |
| chem.lattice | Lattice energy, entropy and Gibbs free energy | chem.entropy |
| bio.classification | Classification, biodiversity, conservation and ecosystems | bio.ecology |
| eng.overview | Engineering: routes, careers and course map | eng.what |
| eng.materials | Materials, stress and beams | eng.mechanics |
| eng.electronics | Electronics, digital systems and control | eng.control |
| bus.enterprise | Enterprise, business structure and size | bus.structure, bus.size |
| bus.hrm | Human resource management and management | bus.management |
| bus.marketing | Marketing and market research | bus.research |
| bus.operations | Operations, inventory, capacity and outsourcing | bus.inventory |
| bus.finance | Business finance, sources of finance and cash flow | bus.cashflow |
| bus.org | Organisation, communication, leadership and HRM strategy | bus.leadership |
| econ.firms | Costs, market structures and labour markets | econ.labour |
| econ.trade | Trade, exchange rates, development and globalisation | econ.development |
| acc.basics | Double entry, reconciliations and errors | acc.control |
| acc.statements | Financial statements and their analysis | acc.analysis |
| other.cs | Computer Science, Psychology and other sciences | other.psychology, other.pe, other.more |
| other.english | Humanities, languages and the arts | other.history, other.geography, other.sociology, other.law, other.politics, other.languages, other.arts, other.humanities |

build.js rewrites links href="#old" and href="#old--section" to "#new" before checking links; check.js
treats aliases as valid. The outline's "file"/"owner" fields are no longer used.

## 3. `:::plot` block
In lib.js add block type `plot` (and add it to BLOCK_TYPES): title = caption; body = one line of
tools/svgplot.py options. Split the options like a shell does (support "double-quoted" strings), run
`python3 tools/svgplot.py <options> --caption <title>` with child_process.execFileSync (cwd = project root)
and use stdout as the block's HTML. On failure record a checker error with the last line of stderr.

## 4. Automatic formula sheets
In lib.js, when rendering `:::key` and `:::formula` blocks, also push {chapter, title, html} to a new st.KEYS
list. In build.js, for each chapter tools.f.<x>, append after its body, for every chapter of the mapped
subject(s) in outline order that has KEYS: "## <chapter title>", its boxes, and a link "Revise: <chapter title>".
Map: tools.f.math→math, tools.f.phys→phys, tools.f.chem→chem, tools.f.bio→bio, tools.f.eng→eng,
tools.f.bus→bus and econ. Create content/tools/tools.f.<x>.md for all six (header lines from OUTLINE.md and
a 2–3 sentence intro saying Cambridge prints a formula or data list in the exam, but you must know when
and how to use each formula).

## 5. Check and finish
- `node build.js --warn | tail -n 20` → 0 errors. Run tools/check.js on an existing file and on a throwaway
  sample chapter that uses :::plot (delete the sample afterwards).
- Normal end-of-session steps (publish + commit). Also commit every changed engine file: build.js, lib.js,
  tools/check.js, tools/make_outline.py, src/outline.json, OUTLINE.md and content/tools/*.md.
- Write "DONE WP0" in the STATUS.md line.
