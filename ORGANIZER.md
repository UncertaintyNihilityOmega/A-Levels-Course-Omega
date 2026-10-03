# ORGANIZER: operating rules for the Project Organizer (Opus, project root)

There is deliberately **no CLAUDE.md at the project root**: Claude Code loads parent CLAUDE.md files into
child-folder sessions, so a root one would leak into every course chat. Read this file at the start of each
Organizer session instead, with STATUS.md and `node engine/status.js`.

## Ownership
- The Organizer owns `engine/`, `core/`, `FACTS.md`, the design, the kits and git. Course chats never run git.
- Specialists own their COURSE.md, course.json and FACTS.md; Writers own chapters/, checks/ and widgets.js.
- Change a course's files only to answer a request, to fix a build-breaking error, or at final assembly.
  Say what you changed in that course's REQUESTS.md.

## Phases (REORG-PLAN.md)
- O1 restructure + engine: done 2026-10-03 (commits 433d97a..HEAD).
- O2 redesign: done and approved 2026-10-03; the design is FROZEN (change it only if the user asks).
  "The marked script": blue-black ink on white, red pen for marks/mistakes, highlighter for exam tips,
  mark-scheme green for progress; dark mode is a chalkboard. Literata (reading) + Atkinson Hyperlegible Next
  (UI), subset woff2 in `engine/fonts/` embedded by `assets.js` (fully offline). Marks are grouped by lib.js
  and floated into an examiner's margin in `.eg-b`/`.ta-b`; worked examples are numbered with mark totals.
  Home's subject list is built by app.js from course data (`c:1` in DATA.subjects).
- O3 hand-off: done 2026-10-03. Full verification passed (build, check --py, an isolated phys copy running
  check/preview/widget/status, a throwaway :::plot chapter, the site in the browser pane). From here on, run
  assembly sessions as courses progress.

## Assembly session (repeat whenever courses have progressed)
1. `node engine/status.js` and `grep -n "\- \[ \]" courses/*/REQUESTS.md` (open requests).
2. `node engine/check.js --py`, then `node engine/build.js --strict`. Fix engine problems; send course problems
   back through that course's REVIEW.md (or REQUESTS.md answer).
3. Answer requests: engine changes go in `engine/`; re-run `node engine/sync.js` after any change to the
   engine, kit docs, templates or any course.json (LINKS.md lists every course's ids).
4. Spot-check the site in the browser pane ("site" launch config): a new chapter per course, a widget, dark
   mode, phone width, search.
5. Update STATUS.md (one line), commit with a clear message.

## Engine facts
- `engine/site.js` builds `site/index.html` (core chapters + nav + data) and `site/c/<course>.js` chunks that the
  page loads with `<script>` on demand (works from file://). A chapter that uses another course's widget loads
  that chunk too (`need` in the data).
- `engine/lib.js` renders Markdown (markdown-it + KaTeX → MathML at build time, mhchem). `:::plot` uses
  `engine/plot.js`. `:::key`/`:::formula` boxes feed the formula sheets (`core.json` → `formulaSheets`).
- Ids: course chapter ids start with `<course>.`; `aliases` in course.json/core.json map old ids to new ones and
  links are rewritten. Unknown ids are build errors; planned-but-unwritten links show as plain text.
- Widget names are global (from `W.register` calls); a name registered twice is a build error. `sync.js` puts
  every course's widget names in the kit (`zta:links` → `widgets`, and the end of LINKS.md), so a kit warns
  instead of "not built yet" for another course's widget and errors if a course registers a taken name.
  Re-sync after a course adds widgets so the other kits learn the new names. Tools pages in
  core use `graph` (math), `periodic` and `molar` (chem), `units` (phys), `breakeven` and `npv` (bus).
- The kit (`engine/kit-src/zta.js`) is bundled by `sync.js` with esbuild; `zta:assets` and `zta:links` are
  virtual modules (page files and all chapter ids). Kits are not in git; sync regenerates them.
- Exam-practice features (Maths v2 requests, 2026-10-03), all in lib.js/site.js/app.js and documented in STYLE.md:
  `:::links` (st.LINKS; core.json `linkSheets` builds pages like tools.l.math), `:::proof` (badge from course.json
  `proofBadge`; lint ignores proofs), `:::checklist` (ticks in localStorage `ticks`, keyed by a hash of chapter +
  text) and `:::progress [paper]` (filled by site.js from course.json `papers`), `Q: [n marks] (#id)` and `H:`
  hints in `:::try`, `@level mock` (article `data-level/data-min/data-marks`; app.js `initMock`, state in
  `mock:<id>`), practice by paper with interleaving (DATA.papers). Courses may split widgets into
  `widgets/<name>.js` (util.courseWidgets). `kit/zta.js widget <name> --probe` uses headless Edge/Chrome
  (`--dump-dom`) and reads a JSON report the test page writes into `<pre id="zta-probe">`.
- Python: always `py` (the `python` command is the Windows Store alias), with PYTHONUTF8=1 (the console code
  page cannot print − or ²); `engine/util.js runPython` handles both.
