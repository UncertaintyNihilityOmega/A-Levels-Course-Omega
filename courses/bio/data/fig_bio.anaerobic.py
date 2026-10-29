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


# ---------- 1. the two pathways ----------
f = Fig("pathways")
f.line([(330, 8), (330, 340)], "ln-m thin dash", check=False)
f.text(10, 18, "Lactate fermentation (mammals)", "tl tb")
f.text(350, 18, "Ethanol fermentation (yeast)", "tl tb")
for cx in (190, 500):
    box(f, cx - 55, 34, 110, 26, ["glucose (6C)"])
    f.line([(cx, 60), (cx, 82)], ARR, "ah")
    box(f, cx - 85, 84, 170, 42, ["Glycolysis", "net 2 ATP"], BOX, True)
    f.line([(cx, 126), (cx, 154)], ARR, "ah")
    box(f, cx - 55, 156, 110, 28, ["pyruvate (3C)"])
# lactate branch
f.line([(190, 184), (190, 248)], ARR, "ah")
f.text(202, 204, "reduced NAD → NAD", "tl")
f.text(202, 218, "lactate", "tl")
f.text(202, 232, "dehydrogenase", "tl")
box(f, 135, 250, 110, 28, ["lactate (3C)"])
f.line([(182, 216), (40, 216), (40, 105), (101, 105)], "c3 sw2", "ah")
f.text(48, 170, "NAD", "tl")
f.text(48, 184, "regenerated", "tl")
f.text(190, 304, "no CO₂ is released", "tl", "middle")
# ethanol branch
f.line([(500, 184), (500, 222)], ARR, "ah")
f.text(512, 208, "CO₂ released", "tl")
box(f, 445, 224, 110, 28, ["ethanal (2C)"])
f.line([(500, 252), (500, 302)], ARR, "ah")
f.text(512, 270, "reduced NAD → NAD", "tl")
f.text(512, 286, "alcohol dehydrogenase", "tl")
box(f, 445, 304, 110, 28, ["ethanol (2C)"])
f.line([(494, 270), (350, 270), (350, 105), (411, 105)], "c3 sw2", "ah")
f.text(358, 170, "NAD", "tl")
f.text(358, 184, "regenerated", "tl")
done(f, (670, 344),
     "Two fermentation pathways side by side. Both begin with glycolysis, which makes a net 2 ATP and reduced NAD and gives pyruvate with three carbons. On the left, in mammals, lactate dehydrogenase uses reduced NAD to reduce pyruvate to lactate with three carbons, regenerating NAD, and no carbon dioxide is released. On the right, in yeast, pyruvate loses carbon dioxide to give ethanal with two carbons, and alcohol dehydrogenase uses reduced NAD to reduce ethanal to ethanol, regenerating NAD. In both, a return arrow takes the regenerated NAD back to glycolysis.",
     "Lactate fermentation and ethanol fermentation. In both, reducing a molecule made from pyruvate regenerates NAD, so glycolysis can continue and make its net 2 ATP without oxygen.",
     "fig")

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
f.text(322, 132, "water level", "tl", "end")
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
