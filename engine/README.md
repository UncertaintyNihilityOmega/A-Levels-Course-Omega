# Engine reference

## Build
- `site.js` builds `site/index.html` (core chapters, navigation, data) and, per course, three kinds of file, all
  loaded on demand with `<script>` (works from `file://`; loader `ZTA` in `core.js`):
  - `c/<course>.js`: the course's widgets, quiz questions and key terms (the base file). Every chapter of the course
    needs it; the glossary and the practice page load every base file. A chapter that embeds another course's widget
    also loads that course's base file (`need` in the data).
  - `c/<course>/<chapter>.js`: one chapter. Opening a chapter loads only this and the base file; when the browser is
    idle the next chapter is fetched ahead (not on a data-saving connection).
  - `c/<course>.search.js`: the course's chapters as plain text with their headings. Search loads these, never the
    chapters. Chapters inside index.html (core; every chapter of a kit preview, `inlineAll`) are indexed from the page.
  - Measured Nov 14 2026 (this PC, localhost, 381 chapters): a History chapter opens in 0.7 s and adds 1,800 page
    elements (one file per course: 2.2 s, 162,000); the first search takes 1.8 s with 72,000 elements on the page
    (before: 16.8 s, 1.13 million). Largest chapter file 449 KB. Cost: the search files add 16 MB to the offline copy
    (69 MB in all). Measure again after a change to the loader: nothing may load every chapter.
- `pages.js` (full site only) writes the findable pages: `p/<chapter>.html` (the chapter as a plain static page with
  a canonical URL and a link into the guide; quizzes and widgets become a note), `p/index.html`, `p/page.css` and
  `sitemap.xml` (URLs from package.json `homepage`). They are added after the PWA files, so the service worker does
  not precache them. `pwa.js` `head` adds the description and sharing tags of index.html.
- `util.js` `writeSite` removes files of an older build under `site/c` and `site/p`.
- `lib.js` renders Markdown: markdown-it, KaTeX to MathML at build time, mhchem for `\ce{}`. `:::plot` is drawn by
  `plot.js`. `:::key` and `:::formula` boxes feed the formula sheets (`core.json` → `formulaSheets`).
- Fonts (Literata, Atkinson Hyperlegible Next) are subset woff2 in `fonts/`, embedded by `assets.js`; the maths font
  is subset by fontTools when Python has it, else embedded whole. The site is fully offline.
- `util.js`: course/core loading, `runPython` (UTF-8; Windows py → python3 → python, macOS/Linux python3 → python),
  `mathFontFace`, `writeSite`.

## Installable web app (`pwa.js`, full site only; kit previews do not get it)
- `build.js` adds `manifest.webmanifest`, the icons (192, 512, maskable 512, apple-touch 180, favicon 32 + svg) and
  `sw.js`, and puts the <head> tags at `<!--HEAD-->` in `shell.html`. Colours come from `style.css` tokens.
- `icons.js` draws the icons from the brand mark (ring turned −9°, "A*") as shapes: no image files, no tools.
- URLs are relative (Pages serves the site under `/<repo>/`); the service worker's scope is the site folder.
- `sw.js` caches index.html (the fonts are embedded in it), every course file (`c/…`: a course's files are the paths
  `c/<course>.` and `c/<course>/`, the same rule in `settings.js`) and the icons. Cache name `zta-<hash of every
  file>`: a new build fills a new cache whole on install (skipping the HTTP cache), then old `zta-` caches are deleted.
  Network first; the cache when offline or after 4 s.
- The manifest link and service worker are added only on http(s): `file://` works as before.
- Safe areas (`viewport-fit=cover`): `env(safe-area-inset-*)` on `.app`, `.main`, `.toast` and the phone sidebar.
  `theme-color` follows the system and the theme button.
- After testing on port 5100, unregister the worker if a later session needs a plain server (it serves the cache
  when the server is down).

## Accessibility (WCAG 2.2 AA; Writer rules in `kit-src/STYLE.md` and `WIDGETS.md`)
- Shell: skip link, landmarks (banner, nav, main, aside), one h1 per page. After a navigation focus moves to the new
  page's h1 (or the linked section); the first load keeps focus where it is.
- Live text: the toast is `aria-hidden`; `#announce` (status) reads its message. Quiz results, mock steps and search
  counts are read the same way. Widgets: `W.stat`/`W.readout` are live, `W.say` for canvas results.
- Keyboard: the phone drawer is hidden (`visibility`) when closed, takes focus when opened, closes on Escape or when focus
  leaves; search is a combobox (arrows, Enter, Escape; Tab leaves and closes); answered quiz options stay focusable
  (`aria-disabled`); wide tables and equations that scroll sideways get `tabindex="0"` (`markScrollers`).
- Contrast: every token pair passes AA in light and dark (text 4.5:1, focus ring and input borders `--rule-ui` 3:1).
  Change a token only after measuring it in both themes.
- Motion: `prefers-reduced-motion` stops CSS animation and transitions; widgets use `W.animate`/`W.reducedMotion`.
- Figures: `lint.js` fails an SVG without `role="img"` + `aria-label` (or `aria-hidden`) and an `<img>` without `alt`;
  `plot.js` writes a description of each `:::plot` (axes, ranges, labels, points) unless `--alt` is given.
- Kit probe: `widget --probe` reports `a11y:` problems (unnamed controls, canvases without label or description,
  unlabelled svg, positive tabindex, repeated ids, text contrast).

## Ids and links
- Course chapter ids start with `<course>.`; core ids are free (`home`, `start.*`, `about.*`, `road.*`, `tools.*`).
- `aliases` in `course.json` / `core.json` map old ids to new; links are rewritten. Unknown ids are build errors;
  planned-but-unwritten ids render as plain text.
- Widget names are global (from `W.register`); a name registered twice is a build error. `sync.js` gives every
  kit the full list (`zta:links` → `widgets`, end of LINKS.md), so a kit warns for another course's widget.

## Page features (documented for Writers in `kit-src/STYLE.md`)
- Chapter footer: "Found a mistake on this page? Report it on GitHub" opens a new issue with the chapter id and the
  build date filled in (`site.js`, `opts.issues` from package.json `repository`; kit previews have none).
- `:::links` (verified external links; `linkSheets` build pages such as `tools.l.math`), `:::proof`,
  `:::checklist` (ticks in localStorage `ticks`), `:::progress [paper]` (from `course.json` `papers`).
- `:::try` with `Q: [n marks] (#id)`, `H:` hints and `A:` answers. `[M1 A1]` shorthand becomes `[M1] [A1]`;
  `lint.js` fails an answer or `:::eg` whose marks differ from its `[n marks]`.
- `@level mock`: a timed paper with self-marking (`app.js` `initMock`, state in `mock:<id>`; marks are clamped to
  each question's maximum). Practice by paper with interleaving (`DATA.papers`).
- `practice.next` ("What to revise next", `app.js` `renderNext`) ranks chapters from marked mocks (`DATA.mocks`),
  the last 10 quiz answers per chapter (localStorage `quizlog`) and unticked checklist lines.
- Spaced re-testing (`app.js` `renderRetests`, on `practice.next` and a line on Home): a chapter marked as learned
  (`done[id]` = the time) offers up to 6 of its quiz questions again 1, 3, 7 and 21 days later. localStorage `retest`
  = re-tests behind the reader per chapter; `DATA.ch[id].q` = its number of quiz questions. Unmarking resets it.
- Phone reading (`app.js` `buildToc`, `track`, `setSheet`; shown below 1200 px, where the rail is hidden): the round
  "On this page" button opens a bottom sheet with the contents list; a 3 px reading progress line sits under the top
  bar. `track` (on scroll) marks the current section in the rail and the sheet and saves it in localStorage `secs`
  (chapter → [section id, title]): Home's "Pick up where you left off" opens that section, and a chapter opened at
  its top shows "Last time you were at …".
- Search: on focus the search file of the course being read is fetched first, then the others; results are re-drawn
  as each arrives (`zta:search`), with a "Searching the other courses…" line until all are in. At phone width the
  results use the full screen width.
- Home: `app.js` `renderHome` lists courses from `DATA.subjects`. A course with no written chapter shows its core page
  `about.<id>` as its only sidebar entry ("About this course"; `ab`, `@foot none`); it drops out once a chapter exists.
- Long inline maths is split into one `<math>` per relation joined by `<wbr>`, so chains wrap on phones.
- `course.json` `years`: `status.js` warns in a syllabus's last exam year; home cards show it.

## Course workflow (`progress.js`, used by the kit and `status.js`)
- Course `STATUS.md` is state written only by the kit: a `Last:` line and one line per step
  (`LEAD`, `Pn: open|writing|written|reviewed`, `READER`, `FINAL`).
- `claim [Pn]`, `release Pn`, `done "<step>" "<summary>"`. `done "WRITE Pn"` also appends the summary to
  `packages/Pn.md` ("Writer's notes").
- Up to `AHEAD` (8) packages may be written or claimed past the last review; reviews take `REVIEW_SIZE` (4) packages
  (or the last ones).
- READER: after every package is reviewed; READER.md has one `## <id>` per non-mock chapter; then FIX, REVIEW FINAL.

## Checks
- `test.js`: engine self-test (CI runs it first). A tiny course built in memory: maths, links, aliases, marks, quiz
  data, chunks, the report link, and the errors that must stay errors. Add a check when a page feature is added.
- `lint.js` `reusedNumbers`: a note when a `:::try` question gives 3 or more numbers that are all in one `:::eg`
  question of the same chapter (not in essay courses).
- `lint.js`: structure notes, marks totals, mock rules, `\ce{}` bond fragments that would render as a false charge.
- `check.js --py` runs every `checks/<id>.py` (standard library only).
- Kit (`kit-src/zta.js`, bundled by `sync.js` with esbuild): `phone` (headless 375 px), `widget <name> --probe`
  (headless light/dark/phone, JSON report in `<pre id="zta-probe">`), `shot <id> [--dark] [--phone]` (PNGs of a
  chapter's figures and widgets). Headless runs use Edge, then Chrome, then Chromium, with `--lang=en-GB`; `ZTA_BROWSER` overrides. macOS: apps in
  `/Applications` or `~/Applications`.
- Widgets must survive drawing at zero size (`kit-src/WIDGETS.md`).
