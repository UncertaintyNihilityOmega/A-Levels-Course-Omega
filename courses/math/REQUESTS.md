# REQUESTS: Mathematics → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.


## v2 (2026-10-03): exam-readiness upgrade (plan agreed with the user)
- [ ] 2026-10-03 · `:::links Title` block. Each line is `- <kind>: [Title](https://…) · Site · note [paid] [unofficial]` with kind watch | practise | explore | read | papers. Render it grouped by kind with icons, an "online" badge (the site is offline), `target="_blank" rel="noopener noreferrer"`, and tags shown as small chips. The checker accepts only https URLs and known kinds · the user wants a links area under every lesson. Today every chapter carries the same lines in a `:::note Learn more online` box, as `- **Watch:** [..](..) · Site · note`. The Specialist will convert them to `:::links` once you tick this.
- [ ] 2026-10-03 · Aggregate every chapter's links into one course page "Learn more online", grouped by chapter and kind (like the formula sheet), and link it from road.resources · the user wants one page with all the course's links.
- [ ] 2026-10-03 · `:::proof Title` block: collapsed by default, headed "Why it's true", with a "not examined in 9709" badge (`:::proof examinable Title` drops the badge); it doesn't count towards the checklist minimums · proofs of the theorems in every chapter, without crowding the exam path.
- [ ] 2026-10-03 · `:::checklist` block of "I can…" lines (`- [ ] …`). Ticks are saved per viewer (localStorage) and rolled up into a progress view per paper (P1–P6) · self-tracking against the syllabus outcomes.
- [ ] 2026-10-03 · `H:` lines inside `:::try` between `Q:` and `A:`: progressive hints revealed one at a time before the answer · ★★★ exam questions.
- [ ] 2026-10-03 · A `mock` level and a paper mode for it: countdown timer from `@time`, answers hidden until "Finish", per-question self-marking (enter marks out of the [n] shown) totalling marks and %, and a "revise this" link per question (`Q: [3 marks] (#math.p1.trig) …`) · full original mock papers for P1–P6. Until then they are written as level `ref`.
- [ ] 2026-10-03 · practice.quiz: a mixed mode that interleaves quiz questions across the chapters of one paper (P1, P3, P4, P5, P6) · interleaved retrieval practice.
- [ ] 2026-10-03 · Widget efficiency: (a) let a course split widgets.js (≈100 KB) into `widgets/<name>.js`, one per widget; (b) shared helpers on `W`: axis frame with ticks, slider+number pair, readout table, theme palette, pointer drag, a reduced-motion-aware animation loop, a 3D projection (rotate/project), a seeded RNG, a step-through controller (Back/Next with keyboard); (c) `zta.js widget <name> --probe` that loads light/dark/phone headless and prints NaN/undefined text, overflow and console errors · eight new widgets are planned (proof, area, slopefield, vectors3d, sampling, incline, vt and new graph options); this cuts tokens and bugs.
