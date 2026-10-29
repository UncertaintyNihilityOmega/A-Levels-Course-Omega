# data/fig_bio.anaerobic.py: builds the hand-drawn SVG figures of chapters/bio.anaerobic.md and checks label clearance.
# Run: py data/fig_bio.anaerobic.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.anaerobic replaces the @@FIG_<NAME> placeholder lines of the chapter.
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["PATHWAYS", "RICE"]
figs, problems = [], []
BOX = "f1 s-acc sw2"
ARR = "c1 sw2"


def done(f, vb, label, caption, size="fig small"):
    figs.append(f.svg(vb, label, caption, size))
    problems.extend(f.check())


def box(f, x, y, w, h, lines, cls=BOX, bold=False):
    f.rect(x, y, w, h, cls)
    n = len(lines)
    for i, s in enumerate(lines):
        yy = y + h / 2 + 5 + (i - (n - 1) / 2) * 15
        f.text(x + w / 2, round(yy, 1), s, "tl tb" if bold else "tl", "middle")


# ---------- 1. the two pathways (stacked, fig small) ----------
f = Fig("pathways")
CX = 200


def top(oy, title):
    f.text(10, oy + 16, title, "tl tb")
    box(f, CX - 55, oy + 28, 110, 24, ["glucose (6C)"])
    f.line([(CX, oy + 52), (CX, oy + 64)], ARR, "ah")
    box(f, CX - 85, oy + 66, 170, 42, ["Glycolysis", "net 2 ATP"], BOX, True)
    f.line([(CX, oy + 108), (CX, oy + 120)], ARR, "ah")
    box(f, CX - 55, oy + 122, 110, 24, ["pyruvate (3C)"])


def loop(oy, ystart):
    f.line([(CX - 6, oy + ystart), (24, oy + ystart), (24, oy + 87), (CX - 89, oy + 87)], "c3 sw2", "ah")
    f.text(32, oy + 114, "NAD", "tl")
    f.text(32, oy + 128, "regenerated", "tl")


# lactate fermentation
top(0, "Lactate fermentation (mammals)")
f.line([(CX, 146), (CX, 208)], ARR, "ah")
f.text(CX + 12, 168, "reduced NAD → NAD", "tl")
f.text(CX + 12, 182, "lactate", "tl")
f.text(CX + 12, 196, "dehydrogenase", "tl")
box(f, CX - 55, 210, 110, 24, ["lactate (3C)"])
loop(0, 164)
f.text(CX, 258, "no CO₂ is released", "tl", "middle")
# ethanol fermentation
oy = 280
top(oy, "Ethanol fermentation (yeast)")
f.line([(CX, oy + 146), (CX, oy + 180)], ARR, "ah")
f.text(CX + 12, oy + 167, "CO₂ released", "tl")
box(f, CX - 55, oy + 182, 110, 24, ["ethanal (2C)"])
f.line([(CX, oy + 206), (CX, oy + 270)], ARR, "ah")
f.text(CX + 12, oy + 228, "reduced NAD → NAD", "tl")
f.text(CX + 12, oy + 242, "alcohol", "tl")
f.text(CX + 12, oy + 256, "dehydrogenase", "tl")
box(f, CX - 55, oy + 272, 110, 24, ["ethanol (2C)"])
loop(oy, 236)
done(f, (340, oy + 308),
     "Two fermentation pathways, one above the other. Both begin with glucose, which glycolysis converts to pyruvate with three carbons, making a net 2 ATP and reduced NAD. Top, in mammals: lactate dehydrogenase uses reduced NAD to reduce pyruvate to lactate with three carbons, regenerating NAD, and no carbon dioxide is released. Bottom, in yeast: pyruvate loses carbon dioxide to give ethanal with two carbons, and alcohol dehydrogenase uses reduced NAD to reduce ethanal to ethanol, regenerating NAD. In both, a return arrow takes the regenerated NAD back to glycolysis.",
     "Lactate fermentation and ethanol fermentation. In both, reducing a molecule made from pyruvate regenerates NAD, so glycolysis can continue and make its net 2 ATP without oxygen.")

# ---------- 2. rice ----------
f = Fig("rice")
f.rect(10, 140, 320, 100, "fm s-acc sw2")
f.rect(10, 240, 320, 70, "f1 s-acc sw2")
f.rect(146, 40, 48, 256, "f1 s-acc sw2")
f.poly([(146, 60), (40, 38), (146, 50)], "f2 s-acc2 sw2")
f.poly([(194, 60), (300, 38), (194, 50)], "f2 s-acc2 sw2")
f.line([(146, 262), (90, 298)], "ln thick", check=False)
f.line([(194, 262), (250, 298)], "ln thick", check=False)
for ey in (80, 106, 170, 196, 222, 248, 274):
    ellipse(f, 162, ey, 6, 10, "fp ln")
f.line([(182, 70), (182, 250)], "c1 sw2", "ah")
f.text(196, 30, "leaves above water", "tl")
f.leader((262, 34), (258, 42))
f.text(140, 98, "fast-growing", "tl", "end")
f.text(140, 112, "stem", "tl", "end")
f.leader((144, 95), (147, 95))
f.text(206, 104, "O₂ diffuses down", "tl")
f.leader((204, 100), (184, 102))
f.text(206, 176, "aerenchyma:", "tl")
f.text(206, 190, "air spaces", "tl")
f.leader((202, 172), (169, 171))
f.text(322, 122, "water level", "tl", "end")
f.leader((312, 127), (312, 140))
f.text(18, 196, "flood", "tl")
f.text(18, 212, "water", "tl")
f.text(18, 272, "soil", "tl")
f.text(170, 332, "roots: ethanol fermentation", "tl", "middle")
f.leader((170, 318), (170, 297))
done(f, (340, 344),
     "A rice plant growing in flooded soil. The stem grows fast so the leaves stay above the water level. The stem and root contain aerenchyma, which are air spaces, and an arrow shows oxygen diffusing down through them from the leaves to the roots. The roots in the waterlogged soil carry out ethanol fermentation.",
     "How rice is adapted to flooding: leaves held above the water by fast stem growth, aerenchyma that lets oxygen diffuse down to the roots, and ethanol fermentation in roots when oxygen is still short.")

print("\n\n".join(figs))
print("clearance ok" if not problems else "\n".join(problems), file=sys.stderr)
