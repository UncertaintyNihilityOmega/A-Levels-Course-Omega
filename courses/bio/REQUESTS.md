# REQUESTS: Biology → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.

- [x] 2026-10-24 · The board's site (cambridgeinternational.org/Images/…) returned 404 "Maintenance asset not found" for the 9700 syllabus URL in course.json; LEAD read the web-archive copy (https://web.archive.org/web/20260227154932id_/https://www.cambridgeinternational.org/Images/664560-2025-2027-syllabus.pdf). Please recheck the official URL before the site goes live · the paper guides and overview link the syllabus
- [x] 2026-10-24 · Plan only (user's change of scope): Biology LEAD planned 64 chapters in 24 packages; the gold chapter bio.enzymes and `done LEAD` are left for the next LEAD session · so status still shows LEAD
  - Organizer 2026-10-24: the official syllabus URL returns 200 again (the 404 was temporary maintenance); course.json keeps it.
    Plan-only noted: the next LEAD session writes the gold chapter bio.enzymes, then runs `done LEAD`.
- [x] 2026-10-28 · Let table headings (`th`) wrap on narrow screens (they are `white-space: nowrap`) · biology data tables need headings with units such as "rate of release of fatty acids / µmol min⁻¹"; at 375 px a two-column table with such a heading scrolls sideways, so COURSE.md now caps headings at about 28 characters
  - Organizer 2026-10-28: done. At 700 px and below `.prose th` wraps (engine/style.css); desktop is unchanged. On
    bio.overview at 375 px, sideways-scrolling tables went from 3 to 2. The 28-character cap can be relaxed at the next REVIEW.
- [x] 2026-10-28 · `:::plot` graphs render their axis labels, tick numbers and `--pt` labels at about 7 px on a 375 px phone (viewBox 560 scaled to 343 px), e.g. bio.carbs, bio.lipids, bio.proteins, bio.f.basics · hand SVGs are now 11–13 px there; could plots use a larger font (or a narrower viewBox) below 700 px?
  - Organizer 2026-10-28: done. Plots now carry `class="fig plot"`; at 700 px and below their labels are 17 and tick
    numbers 15 user units (engine/style.css), about 10.4 and 9.2 px on a 375 px phone (was 8 and 7). Desktop unchanged.
- [x] 2026-10-29 · In light mode an unchecked widget checkbox (W helper) draws as a solid dark square in the headless `shot`, so it looks ticked (bio-enzyme "Non-competitive inhibitor"; dark mode is fine). Please check in a real browser and, if real, style unchecked boxes with a light fill · readers may misread which inhibitor is on
  - Organizer 2026-10-29: real, not only headless. With the light theme chosen on a device in dark mode, the page
    kept `color-scheme: light dark` from the meta tag, so native controls (checkboxes, selects, scrollbars) drew
    dark. `:root` now sets `color-scheme: light` (engine/style.css); dark still sets `dark`. Re-shot: unchecked boxes are white.
- [x] 2026-10-29 · A `:::plot` inside a `:::eg` is drawn 271 px wide in a 341 px card on a 375 px phone (about 56 px empty on the right, and the `shot --phone` image shows a vertical line there), e.g. bio.anaerobic (yeast rates), bio.energy (RQ of seeds) · could plots inside a worked example use the card's full width on phones?
  - Organizer 2026-10-29: no change. The empty strip is the marks margin of the worked-example card and the line is
    its red margin rule (the frozen "marked script" design; every `:::eg` in every course has it). A plot that needs
    the full width goes just before the `:::eg`, or the plot keeps few labels so it reads at 271 px.
