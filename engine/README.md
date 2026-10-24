# Engine reference

## Build
- `site.js` builds `site/index.html` (core chapters, navigation, data) and one chunk per course, `site/c/<course>.js`,
  loaded on demand with `<script>` (works from `file://`). A chapter that embeds another course's widget also loads
  that chunk (`need` in the data).
- `lib.js` renders Markdown: markdown-it, KaTeX to MathML at build time, mhchem for `\ce{}`. `:::plot` is drawn by
  `plot.js`. `:::key` and `:::formula` boxes feed the formula sheets (`core.json` → `formulaSheets`).
- Fonts (Literata, Atkinson Hyperlegible Next) are subset woff2 in `fonts/`, embedded by `assets.js`; the maths font
  is subset by fontTools when Python has it, else embedded whole. The site is fully offline.
- `util.js`: course/core loading, `runPython` (py → python3 → python, UTF-8), `mathFontFace`, `writeSite`.

## Ids and links
- Course chapter ids start with `<course>.`; core ids are free (`home`, `start.*`, `about.*`, `road.*`, `tools.*`).
- `aliases` in `course.json` / `core.json` map old ids to new; links are rewritten. Unknown ids are build errors;
  planned-but-unwritten ids render as plain text.
- Widget names are global (from `W.register`); a name registered twice is a build error. `sync.js` gives every
  kit the full list (`zta:links` → `widgets`, end of LINKS.md), so a kit warns for another course's widget.

## Page features (documented for Writers in `kit-src/STYLE.md`)
- `:::links` (verified external links; `linkSheets` build pages such as `tools.l.math`), `:::proof`,
  `:::checklist` (ticks in localStorage `ticks`), `:::progress [paper]` (from `course.json` `papers`).
- `:::try` with `Q: [n marks] (#id)`, `H:` hints and `A:` answers. `[M1 A1]` shorthand becomes `[M1] [A1]`;
  `lint.js` fails an answer or `:::eg` whose marks differ from its `[n marks]`.
- `@level mock`: a timed paper with self-marking (`app.js` `initMock`, state in `mock:<id>`; marks are clamped to
  each question's maximum). Practice by paper with interleaving (`DATA.papers`).
- `practice.next` ("What to revise next", `app.js` `renderNext`) ranks chapters from marked mocks (`DATA.mocks`),
  the last 10 quiz answers per chapter (localStorage `quizlog`) and unticked checklist lines.
- Home: `app.js` `renderHome` lists courses from `DATA.subjects`. A course with no written chapter shows its core page
  `about.<id>` as its only sidebar entry ("About this course"; `ab`, `@foot none`); it drops out once a chapter exists.
- Long inline maths is split into one `<math>` per relation joined by `<wbr>`, so chains wrap on phones.
- `course.json` `years`: `status.js` warns in a syllabus's last exam year; home cards show it.

## Course workflow (`progress.js`, used by the kit and `status.js`)
- Course `STATUS.md` is state written only by the kit: a `Last:` line and one line per step
  (`LEAD`, `Pn: open|writing|written|reviewed`, `READER`, `FINAL`).
- `claim [Pn]`, `release Pn`, `done "<step>" "<summary>"`. `done "WRITE Pn"` also appends the summary to
  `packages/Pn.md` ("Writer's notes").
- Up to `AHEAD` (6) packages may be written or claimed past the last review; reviews take 3 packages (or the last ones).
- READER: after every package is reviewed; READER.md has one `## <id>` per non-mock chapter; then FIX, REVIEW FINAL.

## Checks
- `lint.js`: structure notes, marks totals, mock rules, `\ce{}` bond fragments that would render as a false charge.
- `check.js --py` runs every `checks/<id>.py` (standard library only).
- Kit (`kit-src/zta.js`, bundled by `sync.js` with esbuild): `phone` (headless 375 px), `widget <name> --probe`
  (headless light/dark/phone, JSON report in `<pre id="zta-probe">`), `shot <id> [--dark] [--phone]` (PNGs of a
  chapter's figures and widgets). Headless runs use Edge, falling back to Chrome, with `--lang=en-GB`.
- Widgets must survive drawing at zero size (`kit-src/WIDGETS.md`).
