# data/fig_bio.antibodies.py: builds the hand-drawn SVG figures of chapters/bio.antibodies.md and checks them.
# Run: py data/fig_bio.antibodies.py -> writes data/out_antibodies.json (name -> <figure> line); report on stderr.
import json, sys, math
sys.path.insert(0, "data")
from figlib_p10 import *

out, problems = {}, []
E, B, L = "f1 s-acc sw2", "f2 s-acc2 sw2", "f3 s-acc2 sw2"
VAR, AG = "fa s-acc2 sw2", "fh s-mute sw2"

# ============ Figure 1: antibody structure ============
f = Fig("antibody")
CX = 190
HW, LW = 18, 12            # strip widths: heavy chain, light chain
STEM = 18                  # distance of each heavy chain from the axis
HINGE, BOTTOM = 150, 250


def armpt(t, side):
    return (CX + side * (STEM + 62 * t), HINGE - 100 * t)


NRM = {-1: (-0.85, 0.527), 1: (0.85, 0.527)}       # outward normal of each arm
OFF = 21
def lpt(t, side):
    a = armpt(t, side)
    return (round(a[0] + NRM[side][0] * OFF, 1), round(a[1] + NRM[side][1] * OFF, 1))


for side in (-1, 1):
    f.poly(strip([(CX + side * STEM, BOTTOM), (CX + side * STEM, HINGE), armpt(1, side)], HW), E, name=f"heavy{side}")
for side in (-1, 1):
    f.poly(strip([lpt(0.12, side), lpt(1, side)], LW), B, name=f"light{side}")
for side in (-1, 1):
    f.poly(strip([armpt(0.55, side), armpt(1, side)], HW), VAR, name=f"hvar{side}")
    f.poly(strip([lpt(0.55, side), lpt(1, side)], LW), VAR, name=f"lvar{side}")
# disulfide bonds: two between the heavy chains below the hinge, one between each light chain and its heavy chain
for y in (172, 188):
    f.line([(CX - STEM, y), (CX + STEM, y)], "ln thick", check=False)
    f.shapes[f"ss{y}"] = strip([(CX - STEM, y), (CX + STEM, y)], 4)
for side in (-1, 1):
    p = armpt(0.12, side)
    n = NRM[side]
    q0 = (round(p[0] + n[0] * 3, 1), round(p[1] + n[1] * 3, 1))
    q1 = (round(p[0] + n[0] * (OFF + 4), 1), round(p[1] + n[1] * (OFF + 4), 1))
    f.line([q0, q1], "ln thick", check=False)
    f.shapes[f"hl{side}"] = strip([q0, q1], 4)
# antigens in the binding sites at the tips
for side in (-1, 1):
    h, l = armpt(1, side), lpt(1, side)
    cx, cy = (h[0] + l[0]) / 2 + side * 5, (h[1] + l[1]) / 2 - 12
    f.poly([(cx, cy - 9), (cx + 9, cy), (cx, cy + 9), (cx - 9, cy)], AG, name=f"ag{side}")
    if side == 1:
        AGR = (cx, cy)

# labels, left
LL = 4
f.text(LL, 14, "antigen-binding")
f.text(LL, 28, "site")
t_site = lpt(0.93, -1)
f.leader((38, 32), (t_site[0], t_site[1]), "lvar-1")
f.text(LL, 98, "variable")
f.text(LL, 112, "region")
tv = lpt(0.72, -1)
f.leader((62, 102), (tv[0], tv[1]), "lvar-1")
f.text(LL, 150, "light chain")
tl_ = lpt(0.3, -1)
f.leader((84, 147), (tl_[0], tl_[1]), "light-1")
f.text(LL, 176, "disulfide bond")
bar = f.shapes["hl-1"]
mid = ((bar[0][0] + bar[1][0] + bar[2][0] + bar[3][0]) / 4, (bar[0][1] + bar[1][1] + bar[2][1] + bar[3][1]) / 4)
f.leader((106, 173), (round(mid[0], 1), round(mid[1], 1)), "hl-1")
f.text(LL, 222, "constant region")
f.leader((114, 219), (CX - STEM - 2, 219), "heavy-1")
# labels, right
RX = 252
RT = 308
f.text(RT, 40, "antigen")
f.leader((RT - 2, 37), (AGR[0] + 6, AGR[1]), "ag1")
f.text(RX, 154, "hinge region")
f.leader((RX - 2, 151), (CX + STEM + 3, 152), "heavy1")
f.text(RX, 192, "disulfide bonds")
f.leader((RX - 2, 189), (CX + STEM - 4, 188), "ss188")
f.text(RX, 236, "heavy chain")
f.leader((RX - 2, 233), (CX + STEM + 3, 233), "heavy1")

f.vb = (380, 262)
problems.extend(f.check())
out["antibody"] = f.svg(
    f.vb,
    "An antibody molecule, Y-shaped, made of four polypeptides. Two long heavy chains run down the stem and into the two "
    "arms; two shorter light chains lie alongside the arms. Disulfide bonds join the two heavy chains below the hinge region "
    "and join each light chain to a heavy chain. The tips of the arms are the variable regions, each with an "
    "antigen-binding site that has an antigen bound to it. The rest of the molecule is the constant region.",
    "The structure of an antibody. The two antigen-binding sites at the tips are identical and complementary to one antigen. "
    "The hinge lets the arms swing apart. This is a simplified drawing.")

# ============ Figure 2: hybridoma method ============
g = Fig("hybridoma")


def box(x, y, w, lines, cls=E, name=None):
    h = 14 + 15 * len(lines)
    g.rect(x, y, w, h, cls, rx=6, name=name)
    for i, s in enumerate(lines):
        g.text(x + w / 2, y + 20 + 15 * i, s, "tl", "middle")
    return h


def arrow(x0, y0, x1, y1):
    g.line([(x0, y0), (x1, y1)], "ln", "ah")


y = 6
h1 = box(40, y, 250, ["1  Inject a mouse with", "the antigen"], E)
y2 = y + h1 + 28
arrow(110, y + h1 + 2, 84, y2 - 3)
h2 = box(6, y2, 156, ["Spleen B cells:", "each makes one", "antibody but does", "not divide for long"], B)
box(176, y2, 156, ["Myeloma cells:", "tumour cells that", "divide indefinitely", "and make no antibody"], B)
y3 = y2 + h2 + 28
arrow(84, y2 + h2 + 2, 120, y3 - 3)
arrow(254, y2 + h2 + 2, 210, y3 - 3)
h3 = box(40, y3, 250, ["2  Fuse the two kinds of cell:", "each hybridoma cell divides", "indefinitely and makes", "the antibody"], L)
y4 = y3 + h3 + 24
arrow(165, y3 + h3 + 2, 165, y4 - 3)
h4 = box(40, y4, 250, ["3  Screen: test each hybridoma", "for the wanted antibody"], E)
y5 = y4 + h4 + 24
arrow(165, y4 + h4 + 2, 165, y5 - 3)
h5 = box(40, y5, 250, ["4  Clone the best hybridoma and", "grow it in a fermenter"], E)
y6 = y5 + h5 + 24
arrow(165, y5 + h5 + 2, 165, y6 - 3)
h6 = box(40, y6, 250, ["5  Collect and purify the", "monoclonal antibody"], B)
g.vb = (338, y6 + h6 + 8)
problems.extend(g.check())
out["hybridoma"] = g.svg(
    g.vb,
    "Flow chart of the hybridoma method. 1: a mouse is injected with the antigen. Spleen B cells that make antibody and "
    "myeloma cells that divide indefinitely are fused (2) to make hybridoma cells. 3: each hybridoma is screened for the "
    "wanted antibody. 4: the best hybridoma is cloned and grown in a fermenter. 5: the monoclonal antibody is collected "
    "and purified.",
    "The hybridoma method. A hybridoma cell has the antibody-making ability of a B cell and the endless division of a "
    "myeloma cell. All the cells in the clone are identical, so they make one kind of antibody.")

json.dump(out, open("data/out_antibodies.json", "w", encoding="utf-8"), ensure_ascii=False)
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
