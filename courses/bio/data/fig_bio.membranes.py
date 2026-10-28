# data/fig_bio.membranes.py: hand-drawn SVG figures of chapters/bio.membranes.md with a label-clearance check.
# Run: py data/fig_bio.membranes.py > scratch/membranes_figs.txt (figures on stdout, clearance report on stderr).
import sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p4 import Fig

figs = []

# ---------- Figure 1: fluid mosaic model (the one wide figure) ----------
f = Fig("mosaic")
W, H = 640, 300
HC_OUT, HC_IN, R = 140, 220, 7           # head centres of the outer and inner leaflet
T_OUT = (147, 180)                       # tail span, outer leaflet
T_IN = (182, 213)                        # tail span, inner leaflet
PROT = [(130, 174), (232, 258), (310, 358), (400, 430)]   # transmembrane proteins (x ranges)
EXT = (262, 306)                         # extrinsic protein on the inner surface
CHOL_OUT = [107, 287, 449, 490]          # cholesterol x (outer leaflet)
CHOL_IN = [71, 197, 377, 449]            # cholesterol x (inner leaflet)
GLYCOLIPID = 80
cols = [62 + 18 * k for k in range(24)]  # phospholipid columns

def free(x):
    return not any(a - R - 2 < x < b + R + 2 for a, b in PROT)

def near_chol(x, lst):
    return any(abs(x - c) < 9 for c in lst)

tails_out, tails_in, heads = [], [], []
for x in cols:
    if not free(x):
        continue
    if not near_chol(x, CHOL_OUT) and x != GLYCOLIPID:
        heads.append(f'<circle class="fm s-acc sw2" cx="{x}" cy="{HC_OUT}" r="{R}"/>')
        tails_out.append(f"M{x-3} {T_OUT[0]}L{x-3} {T_OUT[1]}M{x+3} {T_OUT[0]}L{x+3} {T_OUT[1]}")
    if not near_chol(x, CHOL_IN):
        heads.append(f'<circle class="fm s-acc sw2" cx="{x}" cy="{HC_IN}" r="{R}"/>')
        tails_in.append(f"M{x-3} {T_IN[1]}L{x-3} {T_IN[0]}M{x+3} {T_IN[1]}L{x+3} {T_IN[0]}")
f.parts += heads
f.parts.append(f'<path class="ln" d="{"".join(tails_out)}"/>')
f.parts.append(f'<path class="ln" d="{"".join(tails_in)}"/>')

# cholesterol: short rods between the tails, one leaflet each
for x in CHOL_OUT:
    f.rect(x - 4, 150, 8, 30, "fm2 s-acc sw2", 3)
for x in CHOL_IN:
    f.rect(x - 4, 183, 8, 30, "fm2 s-acc sw2", 3)

# channel protein: two halves with a pore between them
f.rect(130, 126, 18, 108, "f1 s-acc sw2", 7)
f.rect(156, 126, 18, 108, "f1 s-acc sw2", 7)
# glycoprotein: transmembrane protein with a branched carbohydrate chain
f.rect(232, 126, 26, 108, "f1 s-acc sw2", 8)
# carrier protein with a binding site open to the outside
f.poly([(310, 126), (326, 126), (334, 158), (342, 126), (358, 126), (358, 234), (310, 234)], "f1 s-acc sw2")
# receptor protein with the ligand bound in its binding site
f.poly([(400, 126), (408, 126), (408, 148), (422, 148), (422, 126), (430, 126), (430, 234), (400, 234)], "f1 s-acc sw2")
f.circle(415, 142, 5, "f3 s-acc2 sw2")
# extrinsic protein on the inner surface
f.rect(EXT[0], 228, EXT[1] - EXT[0], 26, "f2 s-acc2 sw2", 10)

def chain(pts, links):
    for a, b in links:
        f.line([pts[a], pts[b]], "ln-m", check=False)
    for p in pts:
        f.circle(p[0], p[1], 4, "fa s-acc2 sw2")

# glycolipid: carbohydrate chain on a lipid head
f.circle(GLYCOLIPID, HC_OUT, R, "fm s-acc sw2")
f.line([(GLYCOLIPID - 3, T_OUT[0]), (GLYCOLIPID - 3, T_OUT[1])], "ln")
f.line([(GLYCOLIPID + 3, T_OUT[0]), (GLYCOLIPID + 3, T_OUT[1])], "ln")
chain([(80, 124), (74, 112), (82, 100), (76, 88)], [(0, 1), (1, 2), (2, 3)])
f.line([(80, 133), (80, 128)], "ln-m", check=False)
# carbohydrate chain of the glycoprotein
chain([(245, 114), (237, 102), (253, 102), (237, 90), (253, 90)], [(0, 1), (0, 2), (1, 3), (2, 4)])
f.line([(245, 126), (245, 118)], "ln-m", check=False)

# 7 nm bracket on the left
f.line([(40, 133), (40, 227)], "ln-m thin")
f.line([(34, 133), (46, 133)], "ln-m thin")
f.line([(34, 227), (46, 227)], "ln-m thin")
f.text(4, 184, "7 nm", "tl")

# labels above the membrane
f.text(62, 20, "glycolipid", "tl")
f.leader((74, 26), (76, 82))
f.text(150, 62, "glycoprotein", "tl")
f.leader((198, 66), (237, 124))
f.text(270, 70, "carbohydrate chain", "tl")
f.leader((266, 68), (259, 97))
f.text(404, 70, "ligand", "tl")
f.leader((412, 76), (414, 134))
f.text(516, 30, "outside the cell", "tl")
# labels in the right margin
f.text(516, 128, "hydrophilic head", "tl")
f.leader((512, 125), (484, 136))
f.text(516, 165, "cholesterol", "tl")
f.leader((512, 162), (495, 162))
f.text(516, 200, "hydrophobic tails", "tl")
f.leader((512, 197), (482, 197))
# labels below the membrane
f.text(62, 288, "phospholipid", "tl")
f.leader((70, 277), (63, 228))
f.text(130, 262, "channel protein", "tl")
f.leader((165, 252), (165, 237))
f.text(360, 262, "receptor protein", "tl")
f.leader((415, 252), (415, 237))
f.text(156, 288, "extrinsic protein", "tl")
f.leader((250, 277), (272, 257))
f.text(290, 288, "carrier protein", "tl")
f.leader((334, 277), (334, 237))
f.text(516, 290, "inside the cell", "tl")
figs.append(f.svg((W, H),
    "Fluid mosaic model of a cell surface membrane, drawn across the page. A bilayer of phospholipids has hydrophilic heads "
    "facing outwards and hydrophobic tails facing inwards, about 7 nm thick. Cholesterol rods sit between the tails. "
    "Transmembrane proteins include a channel protein with a pore, a carrier protein with a binding site, a glycoprotein "
    "with a carbohydrate chain on the outer surface and a receptor protein with a ligand bound. A glycolipid has a "
    "carbohydrate chain on its head. An extrinsic protein lies on the inner surface. The outside of the cell is at the top.",
    "The fluid mosaic model. The phospholipids move sideways in their own layer and the proteins are scattered through "
    "the bilayer like tiles in a mosaic. Carbohydrate chains are found only on the outer surface. This is a drawing of a "
    "very small part of a membrane, not to scale.",
    size="fig"))
f.problems = f.check()

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
