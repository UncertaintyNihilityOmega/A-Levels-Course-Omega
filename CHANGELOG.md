# Changelog

Versions: the guide is a snapshot (0.x, notes in this file only) until every course is built. GitHub Releases start
at v1 and go up in whole numbers (v1, v2, …).

Planned snapshots:
- 0.7.0: Computer Science and Engineering complete.
- 0.8.0: Business, Economics, Accounting and Other subjects complete.
- 0.9.0 (optional): "Sciences and technology" and "English and languages" (now parts of Other subjects) as full
  courses of their own.

## Unreleased
- New logo: the end of a log, "AΩ" in dark green Caudex on a white face with tree rings (app icons, favicon, top bar).
- Settings page (last in the sidebar): theme, text size, course colours, background and highlighter colours, return
  to default; export, import and clear progress; protect stored data; offline downloads (everything, core pages only,
  or chosen courses), with a notice when the offline copy is ready or updated.
- Settings: reading font (serif Literata or sans serif Atkinson Hyperlegible) and animations (follow the device, or
  off: no transitions, no drawn-in roadmap, widgets stay still).
- Computer Science (9618) complete: 49 chapters (AS and A Level theory, Python and pseudocode, a guide per paper,
  mixed practice and four mock papers), 16 widgets, and a "Computer Science: learn more online" page in the Toolbox.
- Faster loading: each chapter is its own file and search has its own index, so opening a chapter no longer loads
  its whole course and searching no longer loads every chapter (a History chapter: 0.7 s, was 2.2 s; first search:
  1.8 s, was 16.8 s).
- Findable pages: every chapter is also a plain web page (`p/<chapter>.html`) that search engines can read, with a
  sitemap; links shared in a chat show the title, a description and the icon.
- "Found a mistake on this page? Report it on GitHub" under every chapter (the page and build date are filled in).
- Engine self-test (39 checks) runs before every build on GitHub.
- Phone reading: an "On this page" button opens the chapter's sections in a sheet; a thin line under the top bar
  shows how far through the chapter you are; the guide remembers your section, so Home and the chapter take you back.
- Re-tests: a chapter you mark as learned brings its quiz questions back 1, 3, 7 and 21 days later on
  "What to revise next" (and a reminder on Home).
- Search shows results from the course you are reading first, then the others as they arrive; on a phone the
  results use the full width of the screen.
- Kit check: a note when a practice question reuses a worked example's numbers.
- Glossary: the letter links cover every letter (they stopped at E, the end of the first 600 terms).
- Whole-site check (`engine/sitecheck.js`) and a warning for dated facts that have passed; two dead links fixed.
- The guide is now called "Zero to A* Ω" (page titles, the installed app, shared links; file names and the progress
  backup keep the plain name `zero-to-a-star`).
- Sidebar: Business comes before Economics; lines separate the guide, the sciences, the business subjects, the
  humanities and the tools.
- Fixed: the Graph plotter and the Periodic table showed "being built" since chapters became separate files (a
  Toolbox page did not load the course file that holds its tool).
- Top bar and Home heading: the name is a hand-drawn wordmark, "ZERO TO A* Ω" in storybook capitals cut from the logo's wood (white
  with green rings in dark-green bark; the star and Ω in crimson).
- Settings: your own picture as the icon in the top bar and on the browser tab; sections in boxes; "On this page"
  (the list at the side, or the round button on a phone) lists the sections.

## 0.6.0 (2026-11-13)
- Biology complete: 64 chapters (Cambridge 9700), 17 widgets, five mock papers, links page; read through by a beginner Reader.
- History complete: 96 chapters (Cambridge 9489, 2027–2029; replaces Psychology, now a summary under Other subjects),
  Connections boxes, four mock papers, links page.
- Installable web app: manifest, icons and an offline service worker (add to home screen on iPhone, Android, Mac, PC);
  build and kit tools run on macOS.
- Accessibility pass to WCAG 2.2 AA: keyboard use of every page and widget, screen-reader labels for figures, widgets
  and maths, contrast in light and dark, focus outlines, text zoom to 200%, reduced motion.
- Mathematics and Physics read through by a beginner Reader: 169 and 109 items fixed (methods taught at first use,
  skipped steps shown, wrong lab steps and numbers corrected; Physics paper guides state the real front-page
  instructions; the Mathematics normal table checked against the real MF19).
- Phones: larger plot labels, table headings wrap, light theme keeps native controls light on a dark-mode device.
- Licence: content CC BY 4.0, code MIT, credit to UncertaintyNihilityOmega (was the Unlicense).
- About pages sit in each unbuilt course's own sidebar section until its first chapter is written.
- Home page and README: written by Claude, can make mistakes; report them as GitHub issues.

## 0.5.0 (2026-10-24)
- Chemistry complete: 49 chapters (Cambridge 9701), 23 widgets, five mock papers; read through by a beginner Reader.
- About pages for every course still to be built, linked from the home page.
- GitHub Pages: every push to `main` checks, builds and publishes the site.
- Checks: false-charge `\ce{}` fragments flagged; multiple-choice option format; mock marks clamped to the maximum.
- Exam facts: Cambridge science papers print the Periodic Table and important values only (no Data booklet).

## 0.4.0 (2026-10-15)
- Physics complete: 39 chapters (Cambridge 9702), five mock papers.
- "What to revise next" page; READER step; syllabus years on home cards; verified `:::links` in every topic chapter.

## 0.3.0 (2026-10-13)
- Mathematics complete: 62 chapters (Cambridge 9709).
- Mock papers with clock and self-marking, practice by paper, checklists and progress, hints, proofs.
- Phone-width checks; long inline maths wraps.

## 0.2.0 (2026-10-03)
- Restructure into core pages and per-course folders with their own kits; new engine (chunks, plots, formula sheets).
- "Marked script" design: examiner's margin, chalkboard dark mode, embedded fonts, fully offline.

## 0.1.0 (2026-10-01)
- First engine, Start Here, Roadmap, first widgets and Mathematics drafts.
