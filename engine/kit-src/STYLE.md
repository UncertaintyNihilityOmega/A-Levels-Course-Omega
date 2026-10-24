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

- `@level`: pre (foundations below A Level), as, a2, "as a2" (mark the A2 part inside), guide, ref, sum, ext,
  mock (a full mock paper: see "Mock papers" below).
- `@paper`: where it is examined, short. `@time`: realistic study time for a beginner.
- The title is the only h1. Use `##` for sections, `###` for subsections.
- Links: `[Quadratics](#math.p1.quadratics)`. Link only to ids in course.json or kit/LINKS.md. Links to
  chapters that are not written yet show as plain text until they are, so link freely to planned chapters.

## What a topic chapter does (adapt, don't force)
1. `:::why`: 2–3 sentences on why the topic matters.
2. **Before you start**: one line linking the prerequisite chapters (optional), then a **warm-up**:
   `:::try Warm-up` with 3 quick questions from *earlier* chapters, one-line answers, each naming its chapter.
3. Sections (`##`), each building up in small steps:
   plain-English idea and a hook → `:::def` cards for key terms (exam-quality wording) → the rule in a
   `:::key` or `:::formula` box (these also build the formula sheets) → a figure where a picture helps →
   `:::eg` worked examples, easy to exam level, at least one in a real context. A `:::proof` (5–12 lines, a
   reason on every line) sits next to a rule worth proving.
4. `:::warn` for common mistakes and `:::exam` for exam technique, where they fit. `:::analogy` for abstract ideas.
5. `:::board` (2–6 lines) when boards differ. Never in the first person.
6. **Spot the error**: `:::eg Spot the error`, a student's marked answer with one realistic slip; name the line,
   the lost mark and the fix.
7. `:::try`: practice from easy to exam style, each answer showing the key steps and the final answer. Then
   `:::try Exam practice ★ to ★★★`: 6–8 original exam-style questions, `Q: [n marks] ★★ …` (★ one method,
   ★★ two steps, ★★★ multi-part or synoptic, with 2–3 `H:` hints), answers marked line by line. Then
   `:::try Stretch for A*`: 1–2 problems in an unfamiliar context, with hints and full solutions.
8. `:::quiz`: multiple-choice questions whose wrong options are real misconceptions.
9. `:::checklist What you can now do`: 5–10 `- [ ] I can …` lines, one per learning outcome in FACTS.md.
10. `:::recap`: the facts a student must remember. Then `:::links` "Learn more online" (**every topic chapter**:
   students review on other sites and apps, so send them to the best ones): 3–6 links for this chapter's topic,
   at least one `practise` link (topic questions, flashcards, past-paper questions by topic) and one `watch` or
   `read` link for a second explanation. Use only URLs from COURSE.md's verified list, and end the block with its
   "Links checked …" line. Then a last line `Next: [Title](#id)` to the next chapter in course.json order.

Essay subjects (Business, Economics, the humanities) adapt 6–7: spot the weak paragraph, and model answers
built up mark band by mark band instead of M/A/B lines.

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
  conditions `\ce{->[\text{heat}]}`. A final `-` inside `\ce{}` is a negative charge: write a group's open bond
  outside it, `\(\ce{CH3CO}{-}\)`, never `\ce{CH3CO-}` (`check` flags `\ce{-CO-NH-}` and `\ce{[…]n-}`).
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
| `:::proof Title` | "Why it's true": a proof, folded away, badged "not examined"; `:::proof examinable Title` drops the badge. Never counts towards the checklist minimums |
| `:::checklist Title` | "I can …" lines, `- [ ] I can …`; readers tick them (saved in their browser) |
| `:::progress P1` | a live roll-up of the checklists in the chapters of paper P1 (`papers` in course.json); no id = every paper |
| `:::links` | "Learn more online": `- watch: [Title](https://…) · Site · why it helps [paid] [unofficial]`; kinds watch, practise, explore, read, papers; https only; other lines become a small note. Collected on one page per course |
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
In `:::try`, a question can carry its marks and a revise link, and hints that open one at a time before the answer:

    Q: [3 marks] (#math.p1.quadratics) Solve \(2x^2 - 3x - 2 = 0\).
    H: Multiply \(a\) and \(c\): you need two numbers with product −4 and sum −3.
    H: Factorise as \((2x + 1)(x - 2)\).
    A: \((2x + 1)(x - 2) = 0\) [M1] so \(x = -\tfrac12\) or \(x = 2\) [A1] [A1]

`[n marks]` shows as `[n]` beside the question; `(#id)` adds "Revise: <chapter>" under the answer. Both are optional.

Marks: M = method, A = accuracy (depends on M), B = independent mark. Put each mark at the end of the line
(or right after the display maths) that earns it: in worked examples and answers the page moves marks into
an examiner's margin level with that line, and the example's header shows the total. Tables: Markdown pipes, short cells.
Bold a key word the first time if it has no `:::def` card.
- Write marks as tokens: `[M1] [A1]` (or the shorthand `[M1 A1]`). Never a note inside the brackets
  ("[M1 for two correct]") and never inside maths (`\(… [\text{M1}]\)`): those show as plain text. Put a note
  after the marks in round brackets: `[M1] [A1] (M1 for any two correct)`.
- `check` adds up the marks in every answer and worked example and fails when they differ from its `[n marks]`.
- Spot-the-error marking: a wrong formula or method scores M0 (and so A0); a slip inside a right method keeps
  the M1. Name each mark once, on the line that earns or loses it.

### Mock papers (`@level mock`)
`@time` is the time allowed (`1 h 50 min`). Instructions go in a `:::exam` box, then **one `:::try` per question**
(bare `:::try`, no title; the page numbers them Question 1, 2, …), each `Q: [n marks] (#chapter-to-revise) …` and
`A:` the full mark scheme. Parts (a), (b), … need a blank line before them. The page adds a clock, hides every
answer until the reader presses Finish, then lets them enter their mark per question and lists the chapters to
revise. The header shows the total marks: it must match the real paper exactly.
Multiple-choice options: one paragraph each, with a blank line between them and a bold letter (`**A** …`).
Lines are not kept as line breaks, so options written on consecutive lines run together into one line.

### Phones (375 px)
`node kit/zta.js phone [id]` opens every chapter at phone width with all answers and hints open and lists
anything wider than the screen. The page wraps a long inline chain after each relation (=, <, ≤, ⇒, ≈ …), but
it cannot wrap a long sum with no relation in it, or a wide table cell: put those in `\[ … \]` (display
maths scrolls on its own) or a `\[\begin{aligned} … \\ … \end{aligned}\]` with one step per row.

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
     Labels use `tl` (`ts` only for axis tick numbers), with `halo` where a label touches a line.
   - Arrowheads: `marker-end="url(#ah)"`, also `#ahm`, `#ahr`, `#ahok`, `#ah-<course>`, `#ah2-<course>`; small heads for curly arrows in mechanisms: `#ahs` (ink) and `#ahs-red`.
   - Default `class="fig small"` with a viewBox about 300–350 wide: labels stay readable on phones. Use `fig`
     (viewBox 520–640) only when the drawing needs the width, and stack panels vertically rather than side by side.
     `class="fig wide"` only for wide multi-panel figures. Crop the viewBox to the drawing plus about 15 px.
     Check coordinates with Python.
   - Pale fills (`fm`, `fm2`, `fp`) need an outline (`s-acc sw2` or a line class), or they vanish in dark mode.
3. **Widgets** (interactive), inside `:::html`: `<div class="widget" data-w="NAME" data-…></div>`. The
   widgets this course has are in kit/WIDGETS.md and widgets.js. Text around a widget says what to try; the
   page must make sense without it.

### Figure and widget rules (most review fixes were these)
Writers cannot see their figures, so check these with coordinates (Python) before `check`, then look once with
`shot <id>` and `shot <id> --dark --phone`.
- **Label boxes.** A 13 px `tl` label is about 7 px per character wide and 13 px tall (baseline at `y`, top at `y − 10`).
  Keep every label box at least 4 px clear of every line, arrow and other label, including the line it names. End each
  arrow at least 10 px short of any other path or label, or its head seems to name it. Arrows under ~20 px show only a head.
- **Scale.** `fig` shows about 625 px wide, `fig small` about 360 px. Use a 520–640-wide viewBox in `fig` and about
  300–350 in `fig small`; anything between (280–420 in `fig`) shows labels at double size. Crop the viewBox to the
  drawing + about 15 px.
- **Classes.** Never name colours in captions, text or widget notes ("the blue arrow"): the palette changes in dark mode;
  name things by their labels or by "dashed". `fi` (ink) and `fp` (paper) swap brightness in dark mode, so never let them
  mean "dark" and "bright". `thin`/`thick` change `ln` only, not `c1`–`c3` (use `sw2`, `sw3`). `gr` nearly vanishes: draw
  reference lines with `ln-m thin dash`. `marker-end` on a path with several `M…` subpaths draws one head: one path per arrow.
  Give every arrow of the same quantity the same class.
- **`:::plot`.** The `--ylabel` sits at the top left and the `--xlabel` above the right end of the x-axis: a curve that ends
  near the x-axis or starts near the top left runs through them. Cut it short with a domain trick
  (`--f "300/x+0*sqrt(x-1)+0*sqrt(7.2-x)" --x 0 8`) and extend `--x` about 15%. Use `--legend tr`, not `tl`. Leave about
  30% headroom above the curves for `--label` and point labels; keep point labels ~100 px apart and off the tick numbers
  (`@se`/`@ne`, not `@s`, on the x-axis). Start `--y` at 0 unless the origin is far off. At most two series per plot.
- **Widgets.** Axis ranges must follow the values (a fixed window that squeezes the interesting part is a bug). Keep
  legends off the curves, one item per line from the second row down (the first row holds the `W.axes` y-label).
  `W.ticks` with `ny: 2` often returns only 0: use 3 or 4. A checkbox row needs
  `style: {display: 'flex', alignItems: 'center', gap: '8px'}` on its `.w-ctl` label with the text in a `.w-lab` span.
  Don't stroke very short thick canvas arcs (Chrome leaves marks): draw chords.
- **`:::board` boxes.** One board and one content difference you are sure of, every time. Never claims about a board you
  cannot verify ("other specifications", two boards at once); otherwise write only about the main board.
- **Rounding.** Never reuse a rounded intermediate in a later step; the check script computes from unrounded values.

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
  for binomial coefficients. Compute table values (critical values, percentage points) from exact inputs, never
  from rounded ones. Run Python as `py` (Windows); the kit sets UTF-8 output for you.
- Edit chapters only with the Write and Edit tools, never through a Python or shell script: heredocs eat
  backslashes (`\tfrac` becomes a tab + "frac") and break the maths silently. Row breaks in `aligned` are `\\`.
- Cambridge conventions: maths answers to 3 significant figures unless exact; angles to 1 d.p. The data
  values (g, physical constants, molar volume) for this course are in COURSE.md.
- Practice questions never reuse a worked example's data or wording: new numbers, new compound, new context.
- Exam-style questions give data the way the real paper does (FACTS.md: what each paper prints and allows). Never
  tell students to look a value up in a booklet the paper does not supply.
- AS chapters use only AS terms. A Level parts are labelled "(A Level)" and come last.
- Exam facts (papers, durations, weightings, dates) only from FACTS.md. Never invent dates, fees or
  paper details: if unsure, leave it out. No claims about how often a topic comes up or how many marks it is
  "worth" unless FACTS.md states them.
- Refer to another chapter by its title, as a link: "as in [Further trigonometry](#math.p3.trig)".
- Use the syllabus's own terms and definitions. If you are not sure of a fact, leave it out.
- Original wording and original questions only. Never copy past papers, mark schemes or textbooks.

## Style
British English (colour, analyse, programme, sulfur, aluminium). Short sentences, active voice, "you".
Warm and direct, never patronising. Define every new term. Real units, real data, realistic numbers.
No emojis, no filler ("It's worth noting", "Let's dive in", "In conclusion"), no em-dash asides, no hype.
