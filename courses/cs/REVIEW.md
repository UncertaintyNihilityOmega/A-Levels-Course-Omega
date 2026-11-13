# REVIEW: Computer Science

Findings for the Writer, newest review at the bottom. One item per line:
`- [ ] <chapter-id>: <exactly what to change>`. The Writer fixes it and changes `[ ]` to `[x]`.
While any `- [ ]` line is open, `status` says FIX.


## REVIEW P1, P2, P3, P4 (2026-11-13)
Fixed in review: cs.data quiz feedback (43 and 52 were explained wrongly; 52 replaced by 180), cs.data BCD stretch remark (8 of 48 is one sixth, not one fifth), cs.media quiz feedback (128 000 distractors), cs.data figure (−128 label cramped), cs-binary (changing "Type the number as", or flipping a bit, now rewrites both inputs in the new base instead of leaving an error in the Add tab; 0 bits now have a visible button border). Checked by keyboard: cs-logic Gates and Expression (Test me, ? buttons, Check, Show the answers, bad expressions), cs-ip (address, mask, slider, prefix box), cs-binary (Convert, Add, bit buttons).
- [ ] cs.internet: widget cs-ip, the three binary rows are about 11 px and the network part is shown only by bold digits, which is hard to see; set those rows to 14 px monospace and colour the network digits with var(--sc) (keep the bar |).
- [ ] cs.internet: widget cs-ip, typing a prefix outside 8–30 (for example 31) in the number box shows the error but also rewrites the Subnet mask field (255.255.255.254) while the slider stays at 30; leave the mask field and slider at the last valid prefix until the box holds a valid one.
