# data/fig_bio.membranes.py: hand-drawn SVG figures of chapters/bio.membranes.md with a label-clearance check.
# Run: py data/fig_bio.membranes.py > scratch/membranes_figs.txt (figures on stdout, clearance report on stderr).
import sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p4 import Fig

figs = []

# ---------- Figure 1: fluid mosaic model (vertical layout, fig small: labels stay readable on phones) ----------
# The membrane runs down the page: outside of the cell on the left, inside on the right. u = across the membrane (x),
# v = along it (y). Every shape is also stored as an obstacle so that each leader line can be checked against all
# shapes except its own target.
import math as _m
f = Fig("mosaic")
W, H = 420, 520
R = 6.5
HX_OUT, HX_IN = 154, 234                  # x of the outer and inner head centres
TAIL_OUT, TAIL_IN = (161, 194), (196, 227)  # tail spans (x)
P_TOP, P_BOT = 140, 248                   # transmembrane protein extent (x)
VCOLS = [50 + 20 * k for k in range(22)]  # phospholipid positions along the membrane (y)
PROT = [(130, 174), (232, 258), (310, 358), (400, 430)]     # channel, glycoprotein, carrier, receptor (y ranges)
EXT = (262, 302)                          # extrinsic protein (y range), on the inner surface
CHOL_OUT = [110, 290, 450]
CHOL_IN = [70, 210, 370, 450]
GLYCO_V = 70
obst = []                                 # (name, kind, data)


def free(v):
    return not any(a - R - 2 < v < b + R + 2 for a, b in PROT)


def near(v, lst):
    return any(abs(v - c) < 9 for c in lst)


heads, tails = [], []
for v in VCOLS:
    if free(v) and not near(v, CHOL_OUT) and v != GLYCO_V:
        heads.append(f'<circle class="fm s-acc sw2" cx="{HX_OUT}" cy="{v}" r="{R}"/>')
        tails.append(f"M{TAIL_OUT[0]} {v-3}L{TAIL_OUT[1]} {v-3}M{TAIL_OUT[0]} {v+3}L{TAIL_OUT[1]} {v+3}")
        obst.append(("head", "c", (HX_OUT, v, R)))
        obst.append(("tails", "r", (TAIL_OUT[0], v - 3, TAIL_OUT[1], v + 3)))
    if free(v) and not near(v, CHOL_IN):
        heads.append(f'<circle class="fm s-acc sw2" cx="{HX_IN}" cy="{v}" r="{R}"/>')
        tails.append(f"M{TAIL_IN[0]} {v-3}L{TAIL_IN[1]} {v-3}M{TAIL_IN[0]} {v+3}L{TAIL_IN[1]} {v+3}")
        obst.append(("head", "c", (HX_IN, v, R)))
        obst.append(("tails", "r", (TAIL_IN[0], v - 3, TAIL_IN[1], v + 3)))
f.parts += heads
f.parts.append(f'<path class="ln" d="{"".join(tails)}"/>')

for v in CHOL_OUT:
    f.rect(164, v - 4, 30, 8, "fm2 s-acc sw2", 3)
    obst.append(("chol", "r", (164, v - 4, 194, v + 4)))
for v in CHOL_IN:
    f.rect(197, v - 4, 30, 8, "fm2 s-acc sw2", 3)
    obst.append(("chol", "r", (197, v - 4, 227, v + 4)))

# channel protein: two halves with a pore between them
for a, b in ((130, 148), (156, 174)):
    f.rect(P_TOP, a, P_BOT - P_TOP, b - a, "f1 s-acc sw2", 7)
obst.append(("channel", "r", (P_TOP, 130, P_BOT, 148)))
obst.append(("channel", "r", (P_TOP, 156, P_BOT, 174)))
# glycoprotein
f.rect(P_TOP, 232, P_BOT - P_TOP, 26, "f1 s-acc sw2", 8)
obst.append(("glycoprotein", "r", (P_TOP, 232, P_BOT, 258)))
# carrier protein: binding site open to the outside (left)
f.poly([(140, 310), (140, 326), (172, 334), (140, 342), (140, 358), (248, 358), (248, 310)], "f1 s-acc sw2")
obst.append(("carrier", "r", (140, 310, 248, 358)))
# receptor protein with the ligand bound
f.poly([(140, 400), (140, 408), (162, 408), (162, 422), (140, 422), (140, 430), (248, 430), (248, 400)], "f1 s-acc sw2")
obst.append(("receptor", "r", (140, 400, 248, 408)))
obst.append(("receptor", "r", (162, 400, 248, 430)))
obst.append(("receptor", "r", (140, 422, 248, 430)))
f.circle(156, 415, 5, "f3 s-acc2 sw2")
obst.append(("ligand", "c", (156, 415, 5)))
# extrinsic protein on the inner surface
f.rect(242, 262, 26, 40, "f2 s-acc2 sw2", 10)
obst.append(("extrinsic", "r", (242, 262, 268, 302)))


def chain(pts, links, name):
    for a, b in links:
        f.line([pts[a], pts[b]], "ln-m", check=False)
    for p in pts:
        f.circle(p[0], p[1], 4, "fa s-acc2 sw2")
        obst.append((name, "c", (p[0], p[1], 4)))


# glycolipid: carbohydrate chain on a lipid head
f.circle(HX_OUT, GLYCO_V, R, "fm s-acc sw2")
obst.append(("head", "c", (HX_OUT, GLYCO_V, R)))
f.line([(TAIL_OUT[0], GLYCO_V - 3), (TAIL_OUT[1], GLYCO_V - 3)], "ln")
f.line([(TAIL_OUT[0], GLYCO_V + 3), (TAIL_OUT[1], GLYCO_V + 3)], "ln")
obst.append(("tails", "r", (TAIL_OUT[0], GLYCO_V - 3, TAIL_OUT[1], GLYCO_V + 3)))
chain([(138, 70), (126, 64), (114, 72), (102, 66)], [(0, 1), (1, 2), (2, 3)], "gl-chain")
f.line([(147, 70), (142, 70)], "ln-m", check=False)
# carbohydrate chain of the glycoprotein
chain([(128, 245), (116, 237), (116, 253), (104, 237), (104, 253)], [(0, 1), (0, 2), (1, 3), (2, 4)], "gp-chain")
f.line([(140, 245), (132, 245)], "ln-m", check=False)

# 7 nm bracket under the membrane
f.line([(147, 492), (241, 492)], "ln-m thin")
f.line([(147, 486), (147, 498)], "ln-m thin")
f.line([(241, 486), (241, 498)], "ln-m thin")
f.text(194, 513, "7 nm", "tl", "middle")

# side labels
f.text(4, 16, "outside the cell", "tl")
f.text(416, 16, "inside the cell", "tl", "end")
leads = []


def lab(x, y, s, a, b, target, anchor="start"):
    f.text(x, y, s, "tl", anchor)
    f.leader(a, b)
    leads.append((s, a, b, target))


lab(4, 74, "glycolipid", (78, 71), (101, 67), "gl-chain")
f.text(4, 242, "carbohydrate", "tl")
f.text(4, 256, "chain", "tl")
f.leader((70, 250), (110, 246))
leads.append(("carbohydrate chain", (70, 250), (110, 246), "gp-chain"))
lab(4, 419, "ligand", (50, 415), (151, 415), "ligand")
lab(284, 154, "channel protein", (280, 151), (249, 139), "channel")
lab(284, 194, "hydrophilic head", (280, 191), (241, 190), "head")
lab(284, 214, "cholesterol", (280, 211), (228, 210), "chol")
lab(284, 249, "glycoprotein", (280, 246), (249, 246), "glycoprotein")
lab(284, 290, "extrinsic protein", (280, 287), (269, 287), "extrinsic")
lab(284, 338, "carrier protein", (280, 335), (249, 335), "carrier")
lab(284, 419, "receptor protein", (280, 416), (249, 416), "receptor")
lab(284, 464, "hydrophobic tails", (280, 461), (214, 460), "tails")
lab(284, 484, "phospholipid", (280, 481), (242, 472), "head")

# leader check: a leader may touch only its own target
def hit(shape, x, y, m):
    kind, d = shape
    if kind == "c":
        return _m.hypot(x - d[0], y - d[1]) < d[2] + m
    return d[0] - m < x < d[2] + m and d[1] - m < y < d[3] + m


lead_probs = []
for (s, a, b, target) in leads:
    for k in range(0, 41):
        t = k / 40
        x, y = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        for (name, kind, d) in obst:
            if name == target:
                continue
            if hit((kind, d), x, y, 1.0):
                lead_probs.append(f"mosaic: leader of '{s}' crosses a {name} at ({x:.0f},{y:.0f})")
                break
        else:
            continue
        break
figs.append(f.svg((W, H),
    "Fluid mosaic model of a cell surface membrane, drawn running down the page, with the outside of the cell on the left "
    "and the inside on the right. A bilayer of phospholipids has hydrophilic heads facing outwards and hydrophobic tails "
    "facing inwards, about 7 nm thick. Cholesterol rods sit between the tails. Transmembrane proteins include a channel "
    "protein with a pore, a carrier protein with a binding site, a glycoprotein with a carbohydrate chain on the outer "
    "surface and a receptor protein with a ligand bound. A glycolipid has a carbohydrate chain on its head. An extrinsic "
    "protein lies on the inner surface.",
    "The fluid mosaic model, turned on its side: the outside of the cell is on the left. The phospholipids move sideways in "
    "their own layer and the proteins are scattered through the bilayer like tiles in a mosaic. Carbohydrate chains are "
    "found only on the outer surface. This is a drawing of a very small part of a membrane, not to scale."))
f.problems = f.check() + lead_probs

# ---------- Figure 2: cell signalling ----------
g = Fig("signal")
g.text(10, 16, "1  A signalling cell secretes ligands", "tl tb")
g.rect(20, 30, 150, 58, "f1 s-acc sw2", 22)
g.circle(60, 59, 11, "fm s-acc sw2")
g.text(20, 106, "signalling cell", "tl")
for (x, y) in [(186, 42), (204, 58), (188, 76)]:
    g.circle(x, y, 5, "f3 s-acc2 sw2")
g.text(222, 62, "ligands", "tl")
g.leader((219, 59), (211, 59))
g.text(10, 134, "2  Ligands travel to the target cell", "tl tb")
g.line([(60, 146), (60, 182)], "c1 sw2", "ah")
g.text(76, 168, "in the blood", "tl")
g.text(10, 206, "3  Ligand binds to its receptor", "tl tb")
g.rect(14, 256, 140, 60, "f1 s-acc sw2", 20)
g.poly([(50, 256), (50, 238), (60, 238), (68, 248), (76, 238), (86, 238), (86, 256)], "f2 s-acc2 sw2")
g.poly([(60, 232), (76, 232), (68, 246)], "f3 s-acc2 sw2")
g.text(100, 226, "ligand", "tl")
g.leader((96, 223), (79, 233))
g.text(100, 248, "receptor", "tl")
g.leader((96, 245), (88, 247))
g.rect(176, 256, 140, 60, "f1 s-acc sw2", 20)
g.poly([(212, 256), (212, 238), (224, 238), (224, 246), (240, 246), (240, 238), (252, 238), (252, 256)], "f2 s-acc2 sw2")
g.poly([(224, 214), (240, 214), (232, 228)], "f3 s-acc2 sw2")
g.text(14, 336, "target cell:", "tl")
g.text(14, 350, "responds", "tl")
g.text(176, 336, "other cell:", "tl")
g.text(176, 350, "no response", "tl")
figs.append(g.svg((330, 362),
    "Cell signalling in three steps. 1: a signalling cell secretes ligand molecules. 2: the ligands travel in the blood to "
    "target cells. 3: a ligand binds to a receptor with a complementary shape on the target cell, which responds; a "
    "second cell with a differently shaped receptor does not bind the ligand and does not respond.",
    "Cell signalling. Only cells with receptors complementary to the ligand respond; other cells ignore it."))
g.problems = g.check()

for s in figs:
    print(s)
    print()
print("\n".join(f.problems + g.problems) if (f.problems or g.problems) else "clearance ok", file=sys.stderr)
