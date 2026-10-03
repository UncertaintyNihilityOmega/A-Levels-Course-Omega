# BRIEF — writing a Zero to A* chapter (lean edition)

Readers are complete beginners aged 15–19; many study alone and many speak English as a second
language. Goal: take them from zero to A*-level exam answers. Cambridge International is the main
board; put Edexcel International (IAL), AQA and OCR differences in one `:::board` box.

## The file
One chapter per file: content/<subject>/<chapter-id>.md. Start with these lines, one per line:

    @chapter math.p1.functions
    @title Functions
    @level as
    @paper CAIE P1 · Edexcel IAL P2 · UK Pure Year 1
    @time 5–7 hours
    @summary One or two plain sentences. May contain \(x^2\).

@level is one of: pre (foundations), as, a2, "as a2", guide, ref, sum, ext. Take the id and title from
OUTLINE.md (titles there are final). Link other chapters as [Quadratics](#math.p1.quadratics), only to
ids in OUTLINE.md.

## Size (hard limits)
| Chapter type | Words | Worked examples | Try-it | Quiz | Figures |
|---|---|---|---|---|---|
| Main-subject topic | 1,300–2,000 | 3 (the last one exam style with marks) | 5 | 3 | ≤ 1 hand SVG; `:::plot` as needed |
| Foundations (pre) | 1,200–1,800 | 3–4 | 5 | 3 | ≤ 1 |
| Course map (guide) | 600–900 | 0 | 0 | 0–2 | 0 |
| Economics / Accounting | 1,000–1,500 | 2 | 4 | 3 | ≤ 1 |
| Other-subjects summary | about 250 per subject | – | – | – | – |

## Order inside a topic chapter
1. `:::why` (2–3 sentences: why it matters)
2. "Before you start" with links to prerequisites (optional, one line)
3. 3–6 `##` sections, each: plain-English idea → `:::def` cards for key terms (exam-quality wording) →
   rules in `:::key` boxes (these also build the formula sheets) → `:::eg` worked examples
4. One or two `:::warn` (common mistakes) and one `:::exam` (exam technique) where they fit
5. `:::board` (2–4 lines, only if boards differ)
6. `:::try` (5 questions, easy → exam style; answers = key steps and the final answer)
7. `:::quiz` (3 questions)
8. `:::recap` (5–7 bullets), then "Next: [title](#id)"

In Business and Economics, worked examples are model answers built step by step (knowledge →
application → analysis → evaluation), plus calculations where the topic has them.

## Syntax
- Inline maths `\( … \)`, display maths `\[ … \]`. Never `$…$` for maths ($ is just a dollar sign).
  Units upright with thin spaces: `\(9.81\,\mathrm{m\,s^{-2}}\)`. Multi-line: `\begin{aligned} a &= b \\ c &= d \end{aligned}`.
- Chemistry: `\(\ce{2H2 + O2 -> 2H2O}\)`, `\(\ce{Cu^2+(aq)}\)`, `\(\ce{CH3COOH <=> CH3COO- + H+}\)`.
- Vectors: `\mathbf{a}`, `\overrightarrow{AB}`, `\begin{pmatrix}3\\-1\end{pmatrix}`. Never \vec, \overline, \cancel, \boxed.
- Blocks: a line `:::type Title` at column 0, a line `:::` to close, blank lines around. Types: def, eg, key,
  formula, tip, warn, exam, analogy, why, board, lab, note, steps, cols + col, try, quiz, recap, html, plot.
- Exam marks inside `:::eg`, written separately: `[M1] [A1] [B1]` (method, accuracy, independent).
- `:::try`: a line starting `Q:` begins a question, `A:` its answer; further lines continue them.
- `:::quiz`: `? question`, options `+ correct` (exactly one) and `- wrong`, then `> explanation`.
- Tables: Markdown pipes. Bold a key word the first time if it has no `:::def` card.

## Figures, cheapest first
1. Graphs of functions: a `:::plot` block. The build draws it; you write one line of options.

       :::plot The parabola y = x² − 2x − 3 crosses the x-axis at −1 and 3.
       --f "x**2-2*x-3" --x -3 5 --y -5 7 --pt "1,-4,vertex (1, −4)@e" --vline 1 --label "y = x² − 2x − 3" --legend tl
       :::

   Options: several --f (Python syntax: x**2, sin(x), exp(x), log(x), sqrt(x)); --x a b; --y a b;
   --pt "x,y,label@dir" (dir n s e w ne nw se sw); --vline; --hline; --shade "0,a,b"; --deg; --noticks;
   --nogrid; --xlabel; --ylabel; --label (one per --f); --legend tl|tr. Straight lines draw economics
   diagrams (use --noticks and point labels).
2. Only when a picture is essential (force diagram, circuit, cell, apparatus, mechanism): ONE small hand SVG
   (40 elements at most) inside `:::html`:
   `<figure class="fig"><svg viewBox="0 0 600 300" role="img" aria-label="…">…</svg><figcaption>…</figcaption></figure>`
   Classes only, never colours. Lines: ln, ln-m, c1, c2, c3, ax (+ dash, thin, thick). Fills (every filled
   shape needs one): f1, f2, f3, fm, fi, fa, fp. Text: tl, ts, tb, ti, tc, te, ta, tr, halo.
   Arrows: marker-end="url(#ah)" (also #ahr, #ah-<subject>). No ids, defs, markers, styles or images.
3. Widgets, at most one per chapter, inside `:::html`: `<div class="widget" data-w="NAME" …></div>`.
   graph (data-fns="a*x^2+b; 2x" data-x="-6,6" data-y="-5,10" data-params="a=1,-3,3,0.1"), unitcircle,
   stats (data-values), normal (data-mu data-sigma data-a data-b), binomial (data-n data-p),
   projectile (data-g data-speed data-angle), wave (data-mode=single|superpose|stationary),
   halflife (data-n0 data-half), units, periodic, molar (data-formula), ohm, punnett (data-cross="Aa x Aa"),
   chisq, supplydemand, breakeven (data-fc data-price data-vc), npv, ratios, planner, timer, ucas.

## Accuracy
- Recompute every number (examples, answers, quiz options) in the chapter's single python check.
- Cambridge values: Physics g = 9.81 m s⁻²; Maths mechanics g = 10; c = 3.00 × 10⁸ m s⁻¹;
  e = 1.60 × 10⁻¹⁹ C; h = 6.63 × 10⁻³⁴ J s; N_A = 6.02 × 10²³ mol⁻¹; R = 8.31 J K⁻¹ mol⁻¹;
  F = 9.65 × 10⁴ C mol⁻¹; molar gas volume 24.0 dm³ mol⁻¹ at room conditions; water 4.18 J g⁻¹ K⁻¹.
  Maths answers to 3 significant figures unless exact.
- Exam facts (papers, durations, weightings, admissions tests) only from PLAN.md. Never invent dates,
  fees or paper details; if unsure, leave it out.
- Original wording and original questions only. Never copy past papers or textbooks.

## Style
British English (colour, analyse, sulfur, aluminium). Short sentences, "you", warm and direct. Define every
new term. No emojis, no filler phrases, no em-dash asides, no hype.
