# REQUESTS: Chemistry → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.

- [x] 2026-10-15 · Let inline `\ce{…}` break after `->`, `<=>` and ` + ` on phones · long inline equations overflow at 375 px, so COURSE.md makes Writers put every equation over ~30 characters in display maths
  - Organizer 2026-10-15: done (lib.js `splitCe`). An inline `\(\ce{…}\)` of 24+ characters is cut before each
    top-level arrow and after each ` + `, so it wraps on phones. Write ` + ` with spaces and arrows with a space before
    them. COURSE.md now says long equations may stay inline; display maths is still best for the key equation.
- [x] 2026-10-15 · `\ce{^{35}Cl}` and `\ce{^{14}_{6}C}` render with the superscript on top of the symbol · COURSE.md tells Writers to use `{}^{37}_{17}\mathrm{Cl}` instead; a fix would let mhchem isotopes work
  - Organizer 2026-10-15: done (lib.js `fixIsotopes`): `\ce{^{35}Cl}`, `\ce{^{37}_{17}Cl-}` and isotopes inside
    equations are rewritten as `{}^{35}\ce{Cl}` before rendering. Both forms work now; COURSE.md updated.
- [x] 2026-10-15 · A smaller arrowhead marker for curly arrows (the `#ahr` head is ~12 px, large next to 13 px atom labels) · organic mechanisms in about 12 chapters
  - Organizer 2026-10-15: done: `url(#ahs-red)` (red) and `url(#ahs)` (ink) are 60% of the normal head. The gold
    chapter's mechanisms now use `#ahs-red` (looked at with `shot`); COURSE.md updated.
- [x] 2026-10-15 · Please keep scratch/elements.py, scratch/elements.json and scratch/syl.txt (the 9701 Periodic Table and Data section text) when syncing; scratch/syllabus.pdf (4 MB) and scratch/pt.txt can go · the periodic, molar and chem-config widgets generate their element data from them
  - Organizer 2026-10-15: sync never touches scratch/, but scratch/ is not in git, so a fresh copy would lose them.
    elements.py and elements.json moved to **data/** (tracked); elements.py still reads scratch/syl.txt (kept, untracked:
    syllabus text). COURSE.md, FACTS.md, P1, P2, P7 and the gold check script now say data/elements.json.
- [x] 2026-10-23 · (Organizer change, from the P7 note) `shot chem.periodicity` gave no image for its two hand figures
  - Organizer 2026-10-23: the figures were fine. widgets/chem-trend.js looped forever when drawn at zero width
    (`while (perUnit * tstep < 22)` with perUnit 0): `shot` hides the widget while it photographs the figures, and on the
    site a hidden widget redrawn on a theme change would freeze the page. Now guarded (`perUnit > 0`); shot and probe pass.
    Widget rule: never loop on a measured size without checking it is positive.
- [x] 2026-10-23 · (from REVIEW P5, P6) keep a history of Writers' notes; headless shots show number inputs as "0,1"
  - Organizer 2026-10-23: `done "WRITE Pn"` now also appends the summary to packages/Pn.md ("## Writer's notes"), so a
    reviewer reads it there. Headless runs (probe, phone, shot) now pass `--lang=en-GB`, so number inputs use a decimal point.
    The black unchecked checkbox in shots is headless drawing only; ignore it.
