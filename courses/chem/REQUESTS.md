# REQUESTS: Chemistry → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.

- [ ] 2026-10-15 · Let inline `\ce{…}` break after `->`, `<=>` and ` + ` on phones · long inline equations overflow at 375 px, so COURSE.md makes Writers put every equation over ~30 characters in display maths
- [ ] 2026-10-15 · `\ce{^{35}Cl}` and `\ce{^{14}_{6}C}` render with the superscript on top of the symbol · COURSE.md tells Writers to use `{}^{37}_{17}\mathrm{Cl}` instead; a fix would let mhchem isotopes work
- [ ] 2026-10-15 · A smaller arrowhead marker for curly arrows (the `#ahr` head is ~12 px, large next to 13 px atom labels) · organic mechanisms in about 12 chapters
- [ ] 2026-10-15 · Please keep scratch/elements.py, scratch/elements.json and scratch/syl.txt (the 9701 Periodic Table and Data section text) when syncing; scratch/syllabus.pdf (4 MB) and scratch/pt.txt can go · the periodic, molar and chem-config widgets generate their element data from them
