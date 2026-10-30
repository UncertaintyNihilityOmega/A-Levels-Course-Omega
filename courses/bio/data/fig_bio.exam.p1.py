# data/fig_bio.exam.p1.py: the labelled cell drawing of chapters/bio.exam.p1.md (letters P, Q, R, S) with a clearance check.
# Run: py data/fig_bio.exam.p1.py -> prints the <figure> line (paste into the chapter); problems go to stderr.
import math, sys
sys.stdout.reconfigure(encoding="utf-8")
src = open("data/fig_bio.enzymes.py", encoding="utf-8").read()
CW = {"tl": 7.0, "ts": 6.2}
start = src.index("class Fig:")
end = src.index("# ---------- Figure")
exec(src[start:end])

f = Fig("cell")
vb = (360, 236)
# cell outline
f.rect(50, 20, 250, 196, "f1 s-acc sw2", 36)
# P nucleus with nucleolus
f.circle(115, 85, 36, "f2 s-acc2 sw2")
f.circle(108, 85, 9, "fi")
f.text(24, 89, "P", "tl tb", "middle")
f.line([(36, 85), (88, 85)], "ln-m thin")
# Q rough ER: three wavy sheets with dots
for y in (50, 62, 74):
    f.parts.append(f'<path class="c2 sw2" d="M190 {y}Q205 {y-8} 220 {y}T250 {y}T278 {y}"/>')
    for x in (200, 218, 236, 254, 270):
        f.parts.append(f'<circle class="fi" cx="{x}" cy="{y-5 if (x // 18) % 2 else y+4}" r="1.8"/>')
f.text(336, 66, "Q", "tl tb", "middle")
f.line([(326, 62), (272, 62)], "ln-m thin")
# R mitochondrion
f.parts.append('<ellipse class="f2 s-acc2 sw2" cx="225" cy="152" rx="38" ry="17"/>')
f.parts.append('<path class="ln" d="M200 152L206 140L212 164L218 140L224 164L230 140L236 164L242 140L248 152"/>')
f.text(336, 156, "R", "tl tb", "middle")
f.line([(326, 152), (258, 152)], "ln-m thin")
# S Golgi body: four stacked curved sacs and two vesicles
# (REVIEW P21: moved up and right, clear of the rounded corner of the cell outline)
for y in (162, 170, 178, 186):
    f.parts.append(f'<path class="c2 sw3" d="M92 {y}Q124 {y-14} 156 {y}"/>')
f.parts.append('<circle class="f2 s-acc2 sw2" cx="166" cy="157" r="5"/>')
f.parts.append('<circle class="f2 s-acc2 sw2" cx="174" cy="176" r="5"/>')
f.text(24, 186, "S", "tl tb", "middle")
f.line([(36, 182), (94, 182)], "ln-m thin")
svg = f.svg(vb,
    "Drawing of an animal cell in a rounded outline. Four structures carry the letters P, Q, R and S. P is a large round "
    "structure with a darker dot inside, on the left. Q is three wavy parallel sheets studded with small dots, at the top "
    "right. R is an oval with a zigzag fold inside it, at the lower right. S is a stack of four curved flattened sacs "
    "with two small round vesicles beside it, at the lower left.",
    "An animal cell drawn from an electron micrograph. Four structures are labelled P, Q, R and S.")
print(svg)
bad = f.check()
print("\n".join(bad) if bad else "clearance ok", file=sys.stderr)
