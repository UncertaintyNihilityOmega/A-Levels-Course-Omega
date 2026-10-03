# Zero to A* — widget author's guide

Widgets are small interactive tools embedded in chapters with `<div class="widget" data-w="NAME" data-…></div>`.
The page calls your initialiser the first time the chapter is shown:

```js
W.register('name', function (el, opts) {   // el = the .widget div, opts = its data-* attributes as strings
  const { body } = W.frame(el, 'Title shown in header', 'optional short subtitle');
  // build controls + outputs inside body
});
```

Write your widgets in **your own file only** (named in your brief, e.g. `src/widgets-math.js`). Never edit
`src/core.js`, `src/app.js`, `src/style.css`, `build.js`, `lib.js` or content files. Wrap your file in an IIFE:
`(function () { 'use strict'; ... })();`

## Hard constraints
- Plain ES2020 JavaScript in the browser. **No libraries, no imports, no network requests, no `eval` / `new Function`**
  (the page has a strict Content Security Policy). No `alert/confirm/prompt` (they are blocked).
- Never throw on bad input: validate and show a friendly message in a `.w-err` element.
- Must work at phone width (≈ 360–400 px) with no horizontal page overflow; controls wrap (`.w-row` already wraps).
- Must look right in **light and dark** themes: never hard-code colours. For DOM, use the CSS classes below. For
  canvas, read colours with `W.colors(el)` inside your draw function (it is passed as the 4th argument of
  `W.canvas` draw) and redraw on theme change (`W.canvas` does this automatically).
- Every form control needs an accessible label (`aria-label` or a `<label>`); give inputs stable `id`s only if you
  make them unique (e.g. prefix with a counter), since a widget can appear several times on the page.
- Keep each widget's state inside its closure. Persist only small conveniences with `W.store` (never required).
- Respect `prefers-reduced-motion` for any animation (`matchMedia('(prefers-reduced-motion: reduce)').matches`).
- Start in a useful **example state** (never an empty shell): pre-fill sensible example values from data attributes
  or defaults so the first view already shows a result.

## Helpers in `window.W` (from src/core.js — read that file)
- `W.frame(el, title, subtitle)` → `{root, body}`: the standard card with header; put content in `body`.
- `W.h(tag, props, ...children)` DOM builder (`class`, `style` object, `html`, `text`, `onclick`/`oninput` etc.).
- `W.slider({label, min, max, step, value, fmt, oninput})` → `{el, input, get, set}` labelled range input.
- `W.field({label, value, type, step, oninput, placeholder, width})` → `{el, input, get}` labelled input.
- `W.stat(label, highlight)` → `{el, set}` small output tile (`.w-stat`).
- `W.canvas(parent, {height, draw(ctx, w, h, colors)})` → `{redraw, cv, ctx}` hi-DPI canvas that redraws on resize
  and theme change. `colors` has: ink, ink2, ink3, rule, rule2, sheet, card, sc (subject colour), sc2, red, ok, pen, hl,
  font, mono.
- `W.axes(ctx, w, h, view, colors, opts)` draws a graph-paper grid, axes and tick labels for
  `view = {x0, x1, y0, y1}` and returns `{X, Y}` mapping functions (data → pixels). opts: `pad`, `xlabel`, `ylabel`,
  `fx`/`fy` tick formatters, `nx`/`ny`.
- `W.parse(expr, {degrees})` → `{f(scope), vars}` safe maths expression parser (`2x^2 - 3sin(x) + a`). Use `try/catch`.
- `W.parseParams("a=1,-5,5,0.1; b=0,-3,3")` → `[{name, value, min, max, step}]`.
- `W.fmt(x, sf)` number with true minus sign and sig figs; `W.fix(x, dp)`; `W.money(x, '$')`; `W.sup('-3')`;
  `W.ticks(a, b, n)`; `W.shuffle(arr)`; `W.esc(str)`; `W.store.get/set`; `W.onTheme(fn)`.

## CSS classes available (already styled)
`.w-b` body grid, `.w-row` wrapping flex row, `.w-ctl` labelled control column, `.w-lab` small caps label,
`.w-out` row of stats, `.w-stat` / `.w-stat.hi` output tiles, `.w-canvas` canvas frame, `.w-note` small grey note,
`.w-err` red error text, `.w-tabs` + `.w-tab[aria-selected="true"]` segmented buttons, `.btn` / `.btn.btn-sec` /
`.btn-sm` buttons, plain `table/th/td` inside `.w`. Inputs/selects/range sliders inside `.w` are styled
automatically. You may add **a small amount** of inline style for layout (grid templates, widths), using CSS
variables for colour (`var(--sc)`, `var(--ink-2)`, `var(--card)`, `var(--rule)`, `var(--red)`, `var(--ok)`,
`var(--hl-soft)`, `var(--sc-soft)`, `var(--f-mono)`), never literal colours.

## Quality bar
Clip canvas drawing to the plot area (`ctx.save(); ctx.beginPath(); ctx.rect(...); ctx.clip(); … ctx.restore()`) so curves never spill over axes labels or outside the frame. Labels in `.w-lab`/`.w-stat` are not upper-cased, so write variable names exactly as they should appear (e.g. `a`, `f(2)`, `Mean`).
Each widget should teach: label axes and quantities with units, show the key numbers (with sensible significant
figures), and include one short `.w-note` line explaining what to try or how to read it. Interactions must be smooth
(redraw on `input`, not only on `change`). Canvas drawings: crisp lines, readable 11–13px labels using
`colors.mono`/`colors.font`, subject colour for the main curve, `sc2` for a second series, `red` for highlights.

## Testing (required)
```
cd /home/claude/alevels
python3 tools/wtest.py src/widgets-YOURS.js 'graph|data-fns="a*x^2+b" data-params="a=1,-3,3,0.1; b=0,-5,5,0.5"' 'normal|' …
```
It writes a desktop-light and a phone-dark screenshot and prints console errors and overflow warnings. **Look at
both screenshots with your image tool** and fix anything clipped, overlapping, unreadable or broken. Also test edge
cases (empty input, invalid input, extreme slider values) by passing different attributes. Iterate until clean.

When done, reply with a short report: widgets implemented, their data attributes, and anything not done.
