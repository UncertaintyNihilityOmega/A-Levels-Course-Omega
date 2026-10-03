# Zero to A* — author's guide (read all of this before writing)

You are writing chapters for **Zero to A\***, a free, single-page interactive A Level course. It is aimed at a
student who knows **nothing** about the subject yet (many readers are self-studying, aged 15–19, and many speak
English as a second language, e.g. in Turkey), and it must take them all the way to **top-grade exam standard**.
The main reference board is **Cambridge International (CAIE)**; wherever Pearson Edexcel (International A Level,
IAL), AQA or OCR differ, say so.

The finished site is built from Markdown files in `content/` by `node build.js`. You only write your own content
files. **Never edit** `build.js`, `lib.js`, anything in `src/`, `tools/`, or another author's content file. Never run
`node build.js` (it overwrites shared output). Validate with the checker instead (see "Checking your work").

The gold-standard example of a finished chapter is **`content/math-1a.md` (Quadratics)**. Read it first,
and match its tone, structure and formatting. The list of valid chapter ids is in **`OUTLINE.md`** (read that, not
`src/outline.json`).

### SAVE YOUR WORK AS YOU GO (critical)
The machine can be stopped at any moment. Work that exists only in your head or in a scratch file is lost.
**Write each chapter into your content file as soon as it is drafted** (the first chapter with the Write tool; every
later chapter appended, e.g. with a short `python3` append or the Edit tool), then run the checker. Never draft
several chapters before saving, and never assemble the file only at the end. A finished chapter on disk is worth more
than a perfect plan. Keep thinking brief and spend your effort on the chapters themselves.

---------------------------------------------------------------------------------------------------------------------

## 1. Pedagogy: what every chapter must do

1. **Start from zero.** Open with the idea in plain English and a real-world hook (why it matters). Assume the reader
   has only basic school maths/science unless a "Before you start" link says otherwise. Define every technical word
   the first time it appears (in a `:::def` card for important terms, inline for minor ones).
2. **Build up in small steps.** Intuition → precise definition → rule/formula → worked examples (easy → exam level)
   → common mistakes → exam technique. Use analogies (`:::analogy`) where a concept is abstract.
3. **Reach real A Level depth.** Cover everything the Cambridge syllabus lists for the topic (and note extra content
   that Edexcel/AQA/OCR include). A student who masters the chapter should be able to answer real exam questions.
4. **Worked examples are the heart.** At least 3–5 per substantial chapter, graded in difficulty. Show every step,
   with reasons. The last one or two should be "exam style" with mark annotations `[M1]` `[A1]` `[B1]` placed where
   an examiner would award them (M = method, A = accuracy, dependent on M, B = independent mark). For essay subjects
   (Business, Economics), worked examples are model answers / paragraph builds showing knowledge → application →
   analysis → evaluation.
5. **Practice with full answers.** End each substantial chapter with a `:::try` block of 6–10 questions that ramp from
   easy to exam standard, each with a complete worked answer (not just the final number).
6. **Quick check.** Then a `:::quiz` with 3–6 multiple-choice questions (exactly one correct option, 3–5 options,
   plausible distractors that reflect real misconceptions, and an explanation line).
7. **Summary.** Finish with a `:::recap` of 5–9 bullet points: the facts a student must remember.
8. **Connect.** Link to prerequisite and follow-on chapters using the chapter ids in `src/outline.json`, e.g.
   `[Moles and stoichiometry](#chem.moles)`. Only link to ids that exist in the outline.

Guide/overview chapters (course maps, roadmap phases, "other subjects" summaries) are prose-led and do not need
`:::try`; they still benefit from tables, `:::tip`, `:::exam`, `:::warn` and a `:::recap`.

### Length (these targets override any longer numbers in a brief)
- Main topic chapters: **1,500–2,800 words** of prose, 3–5 worked examples, 5–8 practice questions, 3–4 quiz
  questions, 1–2 figures. Cover the whole syllabus point concisely; no filler, no repetition.
- Course-map / overview chapters: 800–1,400 words. "From zero" foundation chapters: 1,400–2,400 words.
- The checker prints a word count per chapter.

### Writing style
- **British English** spelling (colour, organise, metre, analyse, programme, sulfur (IUPAC/Cambridge spelling), aluminium).
- Short, clear sentences. Active voice. Speak to the reader as "you". Warm and encouraging, never patronising.
- No emojis. No filler phrases ("It's worth noting", "In conclusion", "Let's dive in"). No exclamation-mark hype.
- Avoid em-dash asides; use commas, colons or new sentences.
- Use **bold** for a key word when first introduced (if it is not in a `:::def` card).
- Use real units, real data, realistic numbers. Never write lorem ipsum or placeholders.
- **Original writing only.** Do not copy text from textbooks, websites or past papers. Write original questions "in
  the style of" exam questions; do not reproduce real past-paper questions.

### Accuracy (non-negotiable)
- **Verify every calculation with Python** (`python3 -c "..."`) before you write the answer. Check rounding and
  significant figures. Quiz answers must be unambiguous and correct.
- Cambridge conventions: Maths answers to **3 significant figures** unless exact; angles in degrees to 1 d.p.
  **Cambridge 9709 Mechanics uses g = 10 m s⁻²** (state "take g = 10"); Edexcel uses 9.8; **Physics 9702 uses
  g = 9.81 m s⁻²**. Physics/Chemistry data values must match the Cambridge data sheets (e.g. e = 1.60 × 10⁻¹⁹ C,
  h = 6.63 × 10⁻³⁴ J s, c = 3.00 × 10⁸ m s⁻¹, N_A = 6.02 × 10²³ mol⁻¹, R = 8.31 J K⁻¹ mol⁻¹, F = 9.65 × 10⁴ C mol⁻¹,
  molar gas volume 24.0 dm³ mol⁻¹ at room conditions, specific heat capacity of water 4.18 J g⁻¹ K⁻¹).
- Use the syllabus's own terminology and definitions where they exist (e.g. "water potential", "standard enthalpy
  change of formation", "electromotive force"). If you are not sure of a fact, leave it out rather than guess.
- Board facts verified in Oct 2026 are in `PLAN.md` (paper structures etc.). Do not invent exam dates or fees.

---------------------------------------------------------------------------------------------------------------------

## 2. File format

A content file is Markdown with a few extensions. It contains one or more chapters.

```
@group Pure Mathematics 1          <- sidebar group heading (use the group named in your brief)
@chapter math.p1.functions         <- chapter id: EXACTLY as in your brief / src/outline.json
@title Functions
@level as                          <- start | pre | as | a2 | "as a2" | guide | tool | ref | sum | ext
@paper CAIE P1 · Edexcel IAL P2 · AQA/OCR/Edexcel Pure      <- where it is examined (short)
@time 5–7 hours                    <- realistic study time for a beginner
@summary One or two sentences: what the chapter covers, in plain English. May contain \(maths\).

...chapter body...

@chapter math.p1.coord             <- next chapter starts
...
```
- The `@` lines must be at the very top of each chapter, one per line, before any body text.
- Write `@group` only when the group changes (it applies to following chapters). Chapters must appear in the order
  given in your brief.
- The chapter title is the only `<h1>`. In the body use `##` for sections and `###` for subsections (`####` rarely).
- Levels: `pre` = foundations below A Level; `as` = AS (first year); `a2` = A Level second year; `as a2` if a chapter
  spans both (mark the A2 part clearly inside with a heading or a `:::note A Level only`).

### Maths and science notation
- Inline maths: `\( ... \)`  Display maths: `\[ ... \]`  (KaTeX/LaTeX syntax). **Never use `$`** for maths.
  Dollar signs are literal text (prices in Business/Economics are fine: "$4.50").
- Use maths markup for every formula, variable and unit-with-number in technical text: `\(v = u + at\)`,
  `\(3.0 \times 10^{8}\,\mathrm{m\,s^{-1}}\)`, `\(x^2\)`. Upright units with `\mathrm{}` and a thin space `\,`.
- Chemistry: use mhchem inside maths delimiters: `\(\ce{H2SO4}\)`, `\(\ce{2H2 + O2 -> 2H2O}\)`,
  `\(\ce{CH3COOH <=> CH3COO- + H+}\)`, `\(\ce{Fe^3+}\)`, `\(\ce{Cu^2+(aq)}\)`, state symbols `\(\ce{NaCl(s)}\)`.
  `\ce{->[\text{heat}]}` for conditions over an arrow.
- Vectors: bold `\mathbf{a}`, or `\overrightarrow{AB}`, or column vectors `\begin{pmatrix}3\\-1\end{pmatrix}`.
  Do not use `\vec{}` or `\overline{}` (they render poorly). Avoid `\cancel`, `\boxed`, `\bbox`.
- Multi-line working: `\begin{aligned} ... &= ... \\ ... &= ... \end{aligned}` inside `\[ \]`.
- Units in prose without numbers can be plain text ("measured in newtons, N").

### Blocks
Blocks start with `:::type Optional title` on its own line **at column 0** and end with a line containing only `:::`.
Leave a blank line before and after each block. Blocks may contain Markdown, maths, tables and lists.

| Block | Use it for |
|---|---|
| `:::def Term` | A key term with its exact definition (shown as an index card; also feeds the glossary). One term per card. Title = the term. Body = the definition (1–3 sentences, examiner-quality wording). |
| `:::eg Title` | A worked example. Title = the question. Body = full solution. Use `[M1] [A1] [B1]` marks for exam-style ones. |
| `:::key Title` | Key facts / formulas to memorise (shown like a formula booklet box). |
| `:::formula Title` | A single important formula with its symbols explained. |
| `:::tip Title` | A helpful technique or shortcut. |
| `:::warn Title` | A common mistake and how to avoid it (red-pen box). |
| `:::exam Title` | Exam technique: what the question wants, where the marks are, command words. |
| `:::analogy` | An everyday analogy for an abstract idea. |
| `:::why` | Why this topic matters (use once, at the start). |
| `:::board` | Differences between Cambridge, Edexcel (IAL), AQA, OCR for this topic. |
| `:::lab Title` | Practical/required-practical notes (method, apparatus, safety, sources of error). |
| `:::note Title` / `:::story Title` / `:::career Title` | Asides: extra info, history of an idea, where it leads. |
| `:::steps` | A numbered procedure (write a normal `1.` `2.` list inside). |
| `:::cols` containing `:::col Title` blocks | Side-by-side comparison (e.g. mitosis vs meiosis). |
| `:::try Title` | Practice questions. Lines starting `Q:` begin a question, `A:` begins its answer. Continuation lines follow. |
| `:::quiz Title` | MCQs. `? question`, `+ correct option`, `- wrong option`, `> explanation`. Exactly one `+` per question. |
| `:::recap` | End-of-chapter summary bullets. |
| `:::html` | Raw HTML passed through unchanged: **use this for every SVG figure and every widget**. |

`:::try` format example:
```
:::try
Q: Solve \(x^2 - 9 = 0\).
A: \(x^2 = 9\), so \(x = 3\) or \(x = -3\).
Q: (Exam style) A second question can have
several lines, including display maths:
\[y = 2x + 1\]
A: Full worked answer here. [M1]
Second line of the answer. [A1]
:::
```
`:::quiz` format example:
```
:::quiz
? Which particle has a negative charge?
- proton
+ electron
- neutron
> Electrons carry a charge of −1.60 × 10⁻¹⁹ C; protons are positive and neutrons are neutral.
:::
```

### Tables
GitHub-style Markdown tables are encouraged for comparisons, data, and "AS vs A2" maps. Keep cells short.

---------------------------------------------------------------------------------------------------------------------

## 3. Diagrams (inline SVG)

Good diagrams matter: aim for **1–3 SVG figures per main chapter** where a picture explains the mechanism (force
diagrams, circuits, wave patterns, cells and organelles, the heart, apparatus, energy-level diagrams, graphs,
supply/demand diagrams, organisational charts, flowcharts). Only draw what is accurate.

Wrap each figure in a `:::html` block:
```
:::html
<figure class="fig"><svg viewBox="0 0 600 300" role="img" aria-label="Short description">
  ... shapes ...
</svg><figcaption>One or two sentences explaining what the figure shows.</figcaption></figure>
:::
```
Rules (the page restyles these classes for light and dark mode, so **never hard-code colours**: no `fill="#..."`,
`stroke="red"` or `style="color..."`):
- **No `id` attributes, no `<defs>`, no `<marker>`, no `<style>`, no `<script>`, no `<foreignObject>`, no images.**
- Arrowheads: add `marker-end="url(#ah)"` (ink) to a line/path. Others available: `url(#ahm)` (muted),
  `url(#ahr)` (red), `url(#ahok)` (green), `url(#ah-SUBJ)` and `url(#ah2-SUBJ)` (subject primary/secondary colour),
  where SUBJ is one of: math, phys, chem, bio, eng, bus, econ, road, start, other, tools.
- Lines/strokes: `class="ln"` (ink, 2px), `ln-m` (muted 1.4px), `c1` (subject colour, 2.6px), `c2` (second
  colour), `c3` (red), `c4` (grey), `ax` (axis), `gr` (faint grid). Modifiers: `thin`, `thick`, `dash`, `dot`,
  `sw1|sw2|sw3` (stroke width), `s-ink|s-acc|s-acc2|s-red|s-mute` (stroke colour only).
  Lines with these classes have `fill: none` already. A closed shape that needs both a fill and an outline: use a
  fill class plus a stroke class, e.g. `<rect class="f1 s-acc sw2" .../>`.
- Fills: `f1` (subject tint), `f2` (second tint), `f3` (red tint), `fm` (card grey), `fm2` (rule grey), `fi` (ink),
  `fa` (solid subject colour), `fa2`, `fp` (paper), `fr` (red), `fok` (green tint), `fh` (highlighter yellow).
  **Every filled shape needs a fill class** (otherwise it renders black).
- Text: plain `<text>` is ink 14px. Classes: `tl` (13px muted label), `ts` (11.5px small), `tb` (bold), `ti`
  (italic, for variables), `tc` (centred), `te` (right-aligned), `ta` / `ta2` (subject colours), `tr` (red),
  `tp` (paper colour, for text on a dark fill), `halo` (paper outline so text stays readable over lines).
  Use Unicode for maths in SVG text: x², θ, Δ, λ, →, ⇌, −, ×, μ, Ω, ½. No LaTeX inside SVG.
- Size: use a viewBox about 560–680 wide. Font sizes above are in viewBox units, so keep the viewBox no wider than
  ~700 or the text gets small on phones. Leave margins so nothing is clipped. Check coordinates with Python.
- Add `class="fig wide"` on the figure for wide multi-panel diagrams, `class="fig small"` for small ones.
- **Function graphs**: generate them with the house tool, then paste the output into a `:::html` block:
  `python3 tools/svgplot.py --f "x**2-2*x-3" --x -3 5 --y -5 7 --pt "1,-4,vertex (1, −4)@e" --vline 1 --label "y = x² − 2x − 3" --legend tl --caption "…"`
  (`--f` repeatable; `--pt "x,y,label@dir"` with dir n/s/e/w/ne/nw/se/sw; `--hline`, `--shade "0,a,b"`, `--deg`,
  `--noticks`, `--nogrid`, `--xlabel`, `--ylabel`, `--w`, `--h`). Run `python3 tools/svgplot.py -h` for options.
  For supply/demand, cost curves etc. you can use it with straight-line functions and `--noticks`.

## 4. Interactive widgets

You may embed interactive tools (0–2 per chapter, only where they genuinely help). Put each in a `:::html` block:
`<div class="widget" data-w="NAME" ...></div>`. Available widgets and their data attributes:

| `data-w` | What it does | Attributes |
|---|---|---|
| `graph` | Function plotter with optional sliders | `data-fns="a*x^2+b*x+c; 2x+1"` (`;`-separated, use `x`; letters a b c d k m n p q for sliders; functions sin cos tan ln log exp sqrt abs; `^` powers; implicit multiplication ok), `data-x="-6,6"`, `data-y="-8,10"`, `data-params="a=1,-3,3,0.1; b=0,-5,5,0.5"` (name=start,min,max,step), `data-labels="y = …; y = …"`, `data-deg="1"` (trig in degrees), `data-points="2,0; -2,0"` |
| `projectile` | Projectile motion explorer | `data-g="9.81"` (or 10), `data-speed="20"`, `data-angle="45"` |
| `unitcircle` | Unit circle and trig values | `data-deg="1"` |
| `normal` | Normal distribution area | `data-mu="0" data-sigma="1" data-a="-1" data-b="1"` |
| `binomial` | Binomial distribution bars | `data-n="10" data-p="0.3"` |
| `wave` | Wave / superposition explorer | `data-mode="single"` or `"superpose"` or `"stationary"` |
| `halflife` | Exponential decay / half-life | `data-n0="1000" data-half="5"` |
| `stats` | Summary statistics + box plot from typed data | `data-values="3,5,7,7,9,12"` |
| `units` | SI prefixes and unit converter | — |
| `ohm` | V = IR circuit explorer | — |
| `resistor` | Resistor colour code | — |
| `molar` | Relative formula mass from a formula | `data-formula="CuSO4.5H2O"` |
| `periodic` | Full periodic table | — |
| `punnett` | Genetic cross / Punnett square | `data-cross="Aa x Aa"` |
| `chisq` | Chi-squared test calculator | — |
| `hardy` | Hardy–Weinberg calculator | — |
| `supplydemand` | Supply and demand shifts | — |
| `breakeven` | Break-even chart and margin of safety | `data-fc="5000" data-price="20" data-vc="12"` |
| `npv` | Payback, ARR and NPV | — |
| `ratios` | Financial ratio calculator | — |
| `ucas` | UCAS tariff points | — |
| `planner` | Personal study-plan generator | — |
| `timer` | Study (Pomodoro) timer | — |

Text around a widget should tell the reader what to try ("Drag the slider until the discriminant is zero").
The page must make sense without the widget too.

---------------------------------------------------------------------------------------------------------------------

## 5. Chapter template (adapt, don't force)

```
@chapter subj.topic
@title …
@level as
@paper CAIE Paper 2 · Edexcel IAL Unit 1 · AQA/OCR Year 1
@time 6–8 hours
@summary …

:::why
…
:::

**Before you start**, … [links to prerequisites]

## The big idea (plain English + hook)
## Key terms and definitions (:::def cards, as they arise)
## Core sections, each: explanation → figure → rule → worked example(s)
## Common mistakes (:::warn) and exam technique (:::exam), placed where relevant
## Board differences (:::board)
:::try …  (6–10 questions with full answers)
:::quiz … (3–6 MCQs)
:::recap … (5–9 bullets)
Next: [following chapter](#id)
```

For **course-map (overview) chapters**, include: what the subject is and who it suits; the Cambridge paper
structure as a table (paper, duration, marks, weighting, what is tested); AS vs A Level content map (table of topics
with links to the chapters); how Edexcel IAL / AQA / OCR differ; skills and assessment objectives; a recommended
order and pace of study (e.g. weeks per topic); how to get an A*; common pitfalls; best resources (official
syllabus, past papers, and well-known free sites).

---------------------------------------------------------------------------------------------------------------------

## 6. Checking your work

After writing (and during, after each chapter), run:

```
cd /home/claude/alevels && node tools/check.js content/YOUR-FILE.md
```
Fix **every** error it reports (TeX errors, unknown blocks, missing `A:`, quiz without exactly one `+`, wrong chapter
id/order, unknown links, SVG problems, unknown widgets). Warnings (e.g. a quiz question with no explanation) should
also be fixed. The file is not finished until the checker shows a ✓ with no warnings.

Write large files in several steps (e.g. create the file with the first two chapters, then append further chapters
with additional writes or edits), running the checker as you go. Do not stop until all chapters in your brief are
complete, checked and verified.

When you finish, reply with a short report: the file(s) written, chapters and word counts, number of worked
examples / practice questions / quiz questions / figures, and anything you were unsure about.
