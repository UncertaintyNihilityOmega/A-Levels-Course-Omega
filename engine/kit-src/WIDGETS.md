# WIDGETS: building interactive tools for this course

A widget is a small interactive tool inside a chapter: `<div class="widget" data-w="NAME" data-…></div>` in a
`:::html` block. This course's widgets live in **widgets.js** in the course folder, and only there. The
page calls your initialiser the first time a chapter that uses the widget is shown.

```js
(function () {
  'use strict';
  W.register('normal', function (el, opts) {   // el = the .widget div; opts = its data-* attributes as strings
    const { body } = W.frame(el, 'Normal distribution', 'Drag the bounds to shade an area');
    // build controls and outputs inside body
  });
  // more W.register(...) calls
})();
```

Widget names are global across the whole guide. Give every widget a clear lower-case name; if two courses
need similar tools, use course-flavoured names (`phys-wave`, not `wave`) unless COURSE.md says otherwise.
Shared study widgets that already exist everywhere: `planner`, `timer`, `ucas`. Widgets other courses have built
are listed at the end of kit/LINKS.md: use them freely in chapters, but never register the same name.

## Hard rules
- Plain modern JavaScript in the browser. No libraries, imports, network requests, `eval` or `new Function`,
  and no `alert`/`confirm`/`prompt`.
- Never throw on bad input: validate it and show a friendly message in a `.w-err` element.
- Works at phone width (360–400 px) without horizontal scrolling; controls wrap (`.w-row` already wraps).
- Looks right in light **and** dark mode: never hard-code colours. DOM: use the classes below. Canvas: read
  colours with the `colors` argument of `W.canvas` draw (it redraws on theme change automatically).
- Draw must survive zero size: a hidden widget is redrawn on theme change with width and height 0. Never loop
  on a measured size (`while (perUnit * step < 22)`) without checking it is positive first, or the page freezes.
- Every control has a label (`<label>` or `aria-label`). A widget can appear twice on a page: no fixed ids.
- State lives inside the widget's closure. `W.store` only for small conveniences.
- Respect `prefers-reduced-motion` for any animation.
- Start in a useful example state from the data attributes or sensible defaults, never an empty shell.

## Helpers in `window.W`
- `W.frame(el, title, subtitle)` → `{root, body}`: the standard card with a header.
- `W.h(tag, props, ...children)`: DOM builder (`class`, `style` object, `html`, `text`, `onclick`/`oninput`…).
- `W.slider({label, min, max, step, value, fmt, oninput})` → `{el, input, get, set}`.
- `W.field({label, value, type, step, oninput, placeholder, width})` → `{el, input, get}`.
- `W.stat(label, highlight)` → `{el, set}`: small output tile.
- `W.canvas(parent, {height, draw(ctx, w, h, colors)})` → `{redraw, cv, ctx}`: hi-DPI canvas. `colors`: ink,
  ink2, ink3, rule, rule2, sheet, card, sc (course colour), sc2, red, ok, pen, hl, font, mono.
- `W.axes(ctx, w, h, view, colors, opts)`: graph paper, axes and ticks for `view = {x0, x1, y0, y1}`; returns
  `{X, Y}` data→pixel functions. opts: `pad`, `xlabel`, `ylabel`, `fx`/`fy` tick formatters, `nx`/`ny`.
- `W.parse(expr, {degrees})` → `{f(scope), vars}`: safe maths expression parser (`2x^2 - 3sin(x) + a`). Use try/catch.
- `W.parseParams("a=1,-5,5,0.1; b=0,-3,3")` → `[{name, value, min, max, step}]`.
- `W.fmt(x, sf)`, `W.fix(x, dp)`, `W.money(x, '$')`, `W.sup('-3')`, `W.ticks(a, b, n)`, `W.shuffle(arr)`,
  `W.esc(str)`, `W.store.get/set`, `W.onTheme(fn)`.

Use these instead of writing your own (shorter widgets, fewer bugs):
- `W.sliderNum({label, min, max, step, value, oninput})` → `{el, get, set}`: slider plus a typed number box, in step.
- `W.readout([['area', 'Area'], ['err', 'Error']])` → `{el, set(key, text)}`: a two-column readout table.
- `W.palette(el)`: `W.colors` plus `series` (six theme colours for several curves, in order).
- `W.drag(el, {hit(x, y), move(thing, x, y), end(thing)})`: pointer dragging (mouse, pen, touch). `hit` returns
  what was grabbed (or null); x, y are CSS pixels inside `el` (use the canvas wrap `c.wrap`).
- `W.animate((dt, t) => { …; return false to stop }, {still})` → `{start, stop, reset, running}`: pauses while the
  page is hidden; under reduced motion `start()` calls `still()` once instead (draw the end state).
- `W.reducedMotion()` → true when the reader asked for less motion.
- `W.view3d({yaw, pitch, scale})` → `v` with `v.project(x, y, z, w, h)` → `[sx, sy, depth]` (x right, y into the
  page, z up); `W.orbit(c.wrap, v, c.redraw)` lets the reader drag to rotate.
- `W.rng(seed)` → `r()`, `r.int(lo, hi)`, `r.normal(mu, sd)`: seeded random numbers (same seed, same sequence).
- `W.stepper(root, {steps, onstep(i), labels})` → `{el, go(i), i}`: Back / Next with "Step 2 of 6", plus ←/→ keys
  while the widget has focus. Call `s.go(0)` once to draw the first step.

## Files
Small courses keep every widget in `widgets.js`. For many or large widgets, put each in its own file
`widgets/<name>.js` (same IIFE pattern, one `W.register` per file): the build adds them after widgets.js in name
order. Then a session only opens the file it is changing.

## Styled classes
`.w-b` body, `.w-row` wrapping row, `.w-ctl` labelled control, `.w-lab` small label, `.w-out` stats row,
`.w-stat` / `.w-stat.hi` output tiles, `.w-canvas` canvas frame, `.w-note` grey note, `.w-err` red error,
`.w-tabs` + `.w-tab[aria-selected="true"]` segmented buttons, `.w-read` readout table, `.w-stepper`, `.btn` / `.btn.btn-sec` / `.btn-sm`, plain
`table/th/td`. Inputs, selects and sliders inside `.w` are styled automatically. Inline style only for layout,
with CSS variables for colour (`var(--sc)`, `var(--ink-2)`, `var(--card)`, `var(--rule)`, `var(--red)`, `var(--ok)`).

## Quality bar
A widget teaches: axes and quantities labelled with units, key numbers with sensible significant figures,
and one `.w-note` line saying what to try. Redraw on `input`, not only `change`. Clip canvas drawing to the
plot area. Course colour for the main curve, `sc2` for a second series, `red` for highlights.

## Testing (every widget, every change)
1. `node kit/zta.js widget NAME 'data-a="1" data-b="2"' --probe` writes `preview/widget.html` and loads it
   headless (Edge or Chrome) in light, dark and phone width. It lists errors, text showing NaN / undefined /
   Infinity, anything sticking out of the widget or widening the page, and blank canvases. Fix until it passes.
   Probe edge cases too, by passing extreme or invalid attributes.
2. Then look once: start the "preview" server (the browser pane's launch config, or `node kit/zta.js serve`)
   and open `http://localhost:<port>/widget.html?dark&phone`. Check nothing is clipped, overlapping or
   unreadable, and that dragging and buttons work. Screenshots are expensive: one per widget is enough.
3. `node kit/zta.js preview` and open the chapter that uses it.
