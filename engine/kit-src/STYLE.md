# STYLE: how to write a Zero to A* chapter

This file is the same in every course. Course-specific guidance (depth, data values, board notes, the
chapter plan) is in COURSE.md. A finished model chapter is in kit/EXAMPLE.md.

## Readers and goal
Complete beginners aged 15–19. Many study alone, and many speak English as a second language. Take
them from zero to A*-level exam answers. Cambridge International (CAIE) is the main board. Put
Edexcel International (IAL), AQA and OCR differences in one `:::board` box.

There is **no word limit**. A chapter is as long as the topic needs to go from zero to full exam
depth, and no longer. Every paragraph must teach something: no filler, no repetition, no padding.

## The file
One chapter per file: `chapters/<id>.md`, named exactly after its id. The id, title, level and group come
from course.json. Start with these lines, one per line, then a blank line:

    @chapter math.p1.functions
    @title Functions
    @level as
    @paper CAIE P1 · Edexcel IAL P2 · AQA/OCR Pure Year 1
    @time 5–7 hours
    @summary One or two plain sentences saying what the chapter covers. May contain \(x^2\).

- `@level`: pre (foundations below A Level), as, a2, "as a2" (mark the A2 part inside), guide, ref, sum, ext.
- `@paper`: where it is examined, short. `@time`: realistic study time for a beginner.
- The title is the only h1. Use `##` for sections, `###` for subsections.
- Links: `[Quadratics](#math.p1.quadratics)`. Link only to ids in course.json or kit/LINKS.md. Links to
  chapters that are not written yet show as plain text until they are, so link freely to planned chapters.

## What a topic chapter does (adapt, don't force)
1. `:::why`: 2–3 sentences on why the topic matters.
2. **Before you start**: one line linking the prerequisite chapters (optional).
3. Sections (`##`), each building up in small steps:
   plain-English idea and a hook → `:::def` cards for key terms (exam-quality wording) → the rule in a
   `:::key` or `:::formula` box (these also build the formula sheets) → a figure where a picture helps →
   `:::eg` worked examples, easy to exam level.
4. `:::warn` for common mistakes and `:::exam` for exam technique, where they fit. `:::analogy` for abstract ideas.
5. `:::board` (2–6 lines) when boards differ.
6. `:::try`: practice from easy to exam style, each answer showing the key steps and the final answer.
7. `:::quiz`: multiple-choice questions whose wrong options are real misconceptions.
8. `:::recap`: the facts a student must remember. Then a last line `Next: [Title](#id)`.

Coverage: everything the syllabus lists for the topic (FACTS.md has the learning outcomes), at full
exam depth. A student who masters the chapter can answer real exam questions on it.

Guide chapters (course maps, overviews) are prose-led: tables, `:::tip`, `:::exam`, `:::warn`, `:::recap`, no
`:::try`. A course map has: what the subject is and who it suits; the Cambridge paper table (paper,
duration, marks, weighting, content); an AS/A2 topic map linking every chapter; board differences;
assessment objectives; a study order and pace; how to reach A*; resources.

### Checklist the kit checks (`node kit/zta.js check`)
For pre/as/a2/ext chapters: @summary, @level, @time, @paper (not for pre), a `:::why`, at least one `:::def`,
at least 3 `:::eg` (and in maths and science at least one exam-style example with marks), at least 5 `:::try`
questions, at least 3 `:::quiz` questions, a `:::recap`, a `Next:` line, and `checks/<id>.py`. These are
minimums, not targets: a big topic has more. The checker lists anything missing as a note.

In Business and Economics, worked examples are model answers built step by step (knowledge →
application → analysis → evaluation), plus calculations where the topic has them.

## Syntax
- Inline maths `\( … \)`, display maths `\[ … \]`. Never `$…$` for maths ($ is just a dollar sign).
  Units upright with thin spaces: `\(9.81\,\mathrm{m\,s^{-2}}\)`. Multi-line working:
  `\[\begin{aligned} a &= b \\ c &= d \end{aligned}\]`.
- Chemistry: `\(\ce{2H2 + O2 -> 2H2O}\)`, `\(\ce{Cu^2+(aq)}\)`, `\(\ce{CH3COOH <=> CH3COO- + H+}\)`,
  conditions `\ce{->[\text{heat}]}`.
- Vectors: `\mathbf{a}`, `\overrightarrow{AB}`, `\begin{pmatrix}3\\-1\end{pmatrix}`. Never `\vec`, `\overline`,
  `\cancel`, `\boxed`.
- Blocks: a line `:::type Title` at column 0, a line `:::` to close, blank lines around. Blocks can nest
  (e.g. `:::steps` inside `:::eg`).

| Block | Use |
|---|---|
| `:::def Term` | one key term, exact definition (1–3 sentences); feeds the glossary |
| `:::eg Question` | worked example, every step with a reason; exam marks `[M1] [A1] [B1]` where an examiner gives them |
| `:::key Title` / `:::formula Title` | rules and formulas to learn (with symbols explained); feed the formula sheet |
| `:::tip`, `:::warn`, `:::exam`, `:::analogy`, `:::why`, `:::board`, `:::lab`, `:::note`, `:::story`, `:::career` | callouts |
| `:::steps` | a numbered procedure (write a `1.` `2.` list inside) |
| `:::cols` with `:::col Title` inside | side-by-side comparison |
| `:::try Title` | `Q:` starts a question, `A:` its answer; following lines continue them |
| `:::quiz Title` | `? question`, `+ correct` (exactly one), `- wrong` (2–4), `> explanation` |
| `:::recap` | end-of-chapter summary bullets |
| `:::plot Caption` | a function graph (see Figures) |
| `:::html` | raw HTML: hand-drawn SVG figures and widgets |

```
:::try
Q: Solve \(x^2 - 9 = 0\).
A: \(x^2 = 9\), so \(x = 3\) or \(x = -3\).
:::

:::quiz
? Which particle has a negative charge?
- proton
+ electron
- neutron
> Electrons carry −1.60 × 10⁻¹⁹ C; protons are positive and neutrons are neutral.
:::
```
Marks: M = method, A = accuracy (depends on M), B = independent mark. Tables: Markdown pipes, short cells.
Bold a key word the first time if it has no `:::def` card.

## Figures, cheapest first
1. **Function graphs: `:::plot`.** The build draws it from one line of options; the title is the caption.

       :::plot The parabola \(y = x^2 - 2x - 3\) crosses the x-axis at −1 and 3.
       --f "x**2-2*x-3" --x -3 5 --y -5 7 --pt "1,-4,vertex (1, −4)@e" --vline 1 --label "y = x² − 2x − 3" --legend tl
       :::

   Options: `--f` (repeatable; Python syntax: `x**2`, `sin(x)`, `exp(x)`, `log(x)` = ln, `sqrt(x)`, `pi`, `e`, `abs(x)`),
   `--label` (one per `--f`), `--x a b`, `--y a b`, `--pt "x,y,label@dir"` (dir n s e w ne nw se sw),
   `--vline v`, `--hline v`, `--shade "0,a,b"` (area under curve 0), `--deg` (trig in degrees), `--noticks`,
   `--nogrid`, `--xlabel`, `--ylabel`, `--legend tl|tr`, `--xstep`, `--ystep`, `--w`, `--h`.
   Straight lines with `--noticks` and point labels draw economics diagrams (supply and demand, cost curves).
2. **A hand SVG**, when a picture is essential (force diagram, circuit, cell, apparatus, mechanism). Keep it
   small and accurate, inside `:::html`:
   `<figure class="fig"><svg viewBox="0 0 600 300" role="img" aria-label="…">…</svg><figcaption>…</figcaption></figure>`
   - Classes only, never colours, ids, `<defs>`, `<marker>`, `<style>`, images. The page restyles the classes for
     light and dark mode.
   - Lines: `ln`, `ln-m`, `c1`, `c2`, `c3`, `c4`, `ax`, `gr` (+ `dash`, `dot`, `thin`, `thick`).
   - Fills (every filled shape needs one): `f1`, `f2`, `f3`, `fm`, `fm2`, `fi`, `fa`, `fa2`, `fp`, `fr`, `fok`, `fh`.
     Outline plus fill: `<rect class="f1 s-acc sw2" …/>`.
   - Text: `tl`, `ts`, `tb`, `ti`, `tc`, `te`, `ta`, `ta2`, `tr`, `tp`, `halo`. Unicode maths in SVG text (x², θ, Δ, →).
   - Arrowheads: `marker-end="url(#ah)"`, also `#ahm`, `#ahr`, `#ahok`, `#ah-<course>`, `#ah2-<course>`.
   - viewBox about 560–680 wide so text stays readable on phones. Check coordinates with Python.
   - `class="fig wide"` for wide multi-panel figures, `class="fig small"` for small ones.
3. **Widgets** (interactive), inside `:::html`: `<div class="widget" data-w="NAME" data-…></div>`. The
   widgets this course has are in kit/WIDGETS.md and widgets.js. Text around a widget says what to try; the
   page must make sense without it.

## Accuracy (non-negotiable)
- Every number in the chapter (worked examples, try answers, quiz options, figure labels) is recomputed in
  `checks/<id>.py`. The kit runs it on every check; it must print `ok` and exit 0. A full model is at the end of kit/EXAMPLE.md; the pattern:

  ```python
  # checks/math.p1.quadratics.py: recomputes every number in the chapter
  from math import sqrt, isclose
  def eq(label, got, want, tol=1e-9):
      assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
  def sf(x, n=3): return float(f"{x:.{n}g}")   # n significant figures
  eq("eg2 root", sf((5 + sqrt(13)) / 2), 4.30)
  print("ok")
  ```
  Use `fractions.Fraction` for exact answers, `statistics.NormalDist` for the normal distribution, `math.comb`
  for binomial coefficients. Run Python as `py` (Windows); the kit sets UTF-8 output for you.
- Cambridge conventions: maths answers to 3 significant figures unless exact; angles to 1 d.p. The data
  values (g, physical constants, molar volume) for this course are in COURSE.md.
- Exam facts (papers, durations, weightings, dates) only from FACTS.md. Never invent dates, fees or
  paper details: if unsure, leave it out.
- Use the syllabus's own terms and definitions. If you are not sure of a fact, leave it out.
- Original wording and original questions only. Never copy past papers, mark schemes or textbooks.

## Style
British English (colour, analyse, programme, sulfur, aluminium). Short sentences, active voice, "you".
Warm and direct, never patronising. Define every new term. Real units, real data, realistic numbers.
No emojis, no filler ("It's worth noting", "Let's dive in", "In conclusion"), no em-dash asides, no hype.
