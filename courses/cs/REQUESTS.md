# REQUESTS: Computer Science → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.

- [x] 2026-11-13 · Code blocks: show a small language label on fenced blocks (```pseudocode → "Pseudocode", ```python → "Python", ```output → "Output", ```text → none) and, if cheap, light Python/pseudocode keyword highlighting · the page renders all fences identically, so beginners cannot tell pseudocode, Python and program output apart; chapters currently say it in the sentence before each block (COURSE.md rule)
  - Organizer 2026-11-13: Done in the engine. ```pseudocode, ```python and ```output blocks show a small label above the box ("Pseudocode", "Python", "Output", in the callout-label style); output boxes have a dashed border; ```text stays plain. No keyword highlighting (the design is frozen and the label already tells them apart). The lead-in sentence before a block is now optional: keep it only when it says something the label does not ("Output, when the user types 3:").
- [x] 2026-11-13 · Optional: let `check` warn on a ```python block not followed by an ```output block, and on `<-`/`==` inside ```pseudocode · the course checks files do this with a copied helper (checks/cs.datatypes.py); an engine check would catch Writers who forget
  - Organizer 2026-11-13: Done. `check` notes a ```python block that prints and has no ```output block before the next ```python block or heading (blocks inside :::try and :::quiz are skipped, so "what does this print?" questions are fine), and "<-" or "==" in ```pseudocode outside strings and // comments. cs.datatypes passes with no notes.
