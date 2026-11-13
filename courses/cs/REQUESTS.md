# REQUESTS: Computer Science → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.

- [ ] 2026-11-13 · Code blocks: show a small language label on fenced blocks (```pseudocode → "Pseudocode", ```python → "Python", ```output → "Output", ```text → none) and, if cheap, light Python/pseudocode keyword highlighting · the page renders all fences identically, so beginners cannot tell pseudocode, Python and program output apart; chapters currently say it in the sentence before each block (COURSE.md rule)
- [ ] 2026-11-13 · Optional: let `check` warn on a ```python block not followed by an ```output block, and on `<-`/`==` inside ```pseudocode · the course checks files do this with a copied helper (checks/cs.datatypes.py); an engine check would catch Writers who forget
