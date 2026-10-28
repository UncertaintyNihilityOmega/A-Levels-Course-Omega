# data/fig_lipids.py: hand-drawn SVG figures of chapters/bio.lipids.md with label-clearance checks.
# Run: py data/fig_lipids.py > scratch/lipids_figs.txt   (figures on stdout, clearance report on stderr)
import math, sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p3 import ChemFig, trim, finish, LEAD

figs = []
problems = []


def inlet(f, x, y, s, cls="ts"):
    """Letter inside an atom circle: written without a clearance box."""
    f.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="middle">{s}</text>')


def zig(x, y, n, dx=14, amp=8):
    pts = [(x, y)]
    for k in range(n):
        x += dx
        pts.append((x, y - amp if k % 2 == 0 else y))
    return pts


# ---------------- Figure 1: water molecules and hydrogen bonds ----------------
f = ChemFig("water")
f.text(10, 16, "Four water molecules", "tl tb")
RO, RH, LEN = 14, 10, 31
mol = {"M1": (96, 84), "M2": (206, 84), "M3": (96, 188), "M4": (206, 188)}
H = {}
for k, (x, y) in mol.items():
    hs = []
    for ang in (-7, 97):
        a = math.radians(ang)
        hs.append((x + LEN * math.cos(a), y + LEN * math.sin(a)))
    H[k] = hs
hb = [("M1", 0, "M2"), ("M1", 1, "M3"), ("M2", 1, "M4"), ("M3", 0, "M4")]
for a, i, b in hb:
    p = H[a][i]
    q = mol[b]
    f.line([trim(p, q, RH + 2), trim(q, p, RO + 2)], "ln-m thin dash", check=False)
for k, (x, y) in mol.items():
    for h in H[k]:
        f.line([(x, y), h], "ln thick", check=False)
for k, (x, y) in mol.items():
    f.circle(x, y, RO, "f2 s-acc2 sw2")
    inlet(f, x, y + 4.5, "O", "tl")
    for h in H[k]:
        f.circle(round(h[0], 1), round(h[1], 1), RH, "f1 s-acc sw2")
        inlet(f, round(h[0], 1), round(h[1], 1) + 4.5, "H", "tl")
f.text(206, 52, "δ−", "tl", "middle")
f.text(254, 88, "δ+", "tl")
f.text(10, 252, "Solid line: covalent bond (strong).", "tl")
f.text(10, 268, "Dashed line: hydrogen bond between", "tl")
f.text(10, 284, "molecules (weak).", "tl")
f.text(10, 304, "O is slightly negative (δ−); each H is", "tl")
f.text(10, 320, "slightly positive (δ+).", "tl")
figs.append(f.svg((330, 332),
    "Four water molecules, each an oxygen atom joined by covalent bonds to two hydrogen atoms. Dashed lines are hydrogen bonds "
    "from a hydrogen atom of one molecule to the oxygen atom of a neighbouring molecule. The oxygen is labelled slightly negative "
    "and the hydrogen slightly positive.",
    "Water molecules are polar: O is slightly negative (δ−) and H slightly positive (δ+). The δ+ hydrogen of one molecule is attracted "
    "to the δ− oxygen of another, forming a hydrogen bond."))
problems.extend(f.check())

# ---------------- Figure 2: saturated and unsaturated fatty acids ----------------
f = ChemFig("fatty")
f.text(10, 16, "Saturated fatty acid", "tl tb")
y0 = 58
f.text(24, y0 + 4, "COOH", "tl", "middle")
f.line([(42, y0), (52, y0)], "ln")
chain = zig(52, y0, 11)
f.line(chain, "ln")
f.text(10, 94, "Only single C–C bonds: a straight tail.", "tl")
f.text(10, 124, "Unsaturated fatty acid", "tl tb")
y1 = 156
f.text(24, y1 + 4, "COOH", "tl", "middle")
f.line([(42, y1), (52, y1)], "ln")
part1 = zig(52, y1, 6)
f.line(part1, "ln")
dbl = part1[-2:]
f.line([(dbl[0][0] + 1, dbl[0][1] + 4), (dbl[1][0] + 1, dbl[1][1] + 4)], "ln")
sx, sy = part1[-1]
loc = zig(0, 0, 5)
th = math.radians(55)
tail = [(sx + x * math.cos(th) - y * math.sin(th), sy + x * math.sin(th) + y * math.cos(th)) for x, y in loc]
f.line([part1[-1]] + tail[1:], "ln")
f.text(10, 258, "One C=C double bond puts a kink in the tail.", "tl")
f.text(150, 146, "C=C double bond", "tl")
f.line([(150, 150), (dbl[1][0] + 1, dbl[1][1] + 1)], LEAD, check=False)
f.text(40, 198, "the kink", "tl")
f.line([(100, 194), (128, 164)], LEAD, check=False)
figs.append(f.svg((330, 270),
    "Two fatty acids drawn as zigzag chains, each with a COOH group at the left. The saturated fatty acid has only single bonds "
    "and a straight tail. The unsaturated fatty acid has one C=C double bond, shown by a doubled line, which bends the tail.",
    "A saturated fatty acid has no C=C bonds and a straight tail. Each C=C double bond in an unsaturated fatty acid puts a kink in the tail. "
    "Each corner of the zigzag is a carbon atom; hydrogen atoms are not drawn."))
problems.extend(f.check())

# ---------------- Figure 3: triglyceride formation ----------------
f = ChemFig("trigl")
GX = 34


def glycerol(f, ys):
    for i, (y, s) in enumerate(zip(ys, ["CH₂", "CH", "CH₂"])):
        f.text(GX, y + 4, s, "tl", "middle")
        if i < 2:
            f.line([(GX, y + 12), (GX, ys[i + 1] - 11)], "ln")


def tail(f, x, y):
    f.line(zig(x, y, 5), "ln")


f.text(10, 14, "Glycerol and three fatty acids", "tl tb")
RY = [62, 118, 174]
glycerol(f, RY)
for i, y in enumerate(RY):
    half = 3.5 * len(["CH₂", "CH", "CH₂"][i])
    f.line([(GX + half + 5, y), (64.5, y)], "ln")
    f.text(69.5, y + 4, "OH", "tl")
    f.text(134, y + 4, "HO", "tl")
    f.line([(153, y), (166, y)], "ln")
    f.text(174, y + 4, "C", "tl", "middle")
    f.line([(172, y - 10), (172, y - 20)], "ln")
    f.line([(176, y - 10), (176, y - 20)], "ln")
    f.text(174, y - 28, "O", "tl", "middle")
    f.line([(182.5, y)] + zig(183, y, 5)[1:], "ln")
f.line([(165, 196), (165, 232)], "ln", "ah")
f.text(177, 210, "3 condensation", "tl")
f.text(177, 226, "reactions", "tl")
f.text(10, 254, "Triglyceride and three water molecules", "tl tb")
PY = [310, 366, 422]
glycerol(f, PY)
for i, y in enumerate(PY):
    half = 3.5 * len(["CH₂", "CH", "CH₂"][i])
    f.line([(GX + half + 5, y), (64.5, y)], "ln")
    f.text(72.5, y + 4, "O", "tl", "middle")
    f.line([(81, y), (90, y)], "ln")
    f.text(98.5, y + 4, "C", "tl", "middle")
    f.line([(96.5, y - 10), (96.5, y - 20)], "ln")
    f.line([(100.5, y - 10), (100.5, y - 20)], "ln")
    f.text(98.5, y - 28, "O", "tl", "middle")
    f.line([(107, y)] + zig(108, y, 5)[1:], "ln")
f.text(196, PY[0] - 8, "hydrocarbon tail", "tl")
f.line([(192, PY[0] - 8), (182, PY[0] - 8)], LEAD, check=False)
f.text(72, 462, "ester bond", "tl", "middle")
f.line([(72, 452), (72, 432)], LEAD, check=False)
f.text(240, 462, "+ 3 H₂O", "tl tb", "middle")
figs.append(f.svg((330, 474),
    "Formation of a triglyceride. Top: a glycerol molecule (three carbons, each with an OH group) and three fatty acids, each "
    "with a HO group on a carboxyl group and a hydrocarbon tail. An arrow labelled 3 condensation reactions leads to the "
    "triglyceride below: the glycerol is joined to each fatty acid through an oxygen atom, an ester bond, and three molecules of "
    "water are released.",
    "Each OH of glycerol reacts with the HO of a carboxyl group. A molecule of water is removed and an ester bond (O–C=O) joins the "
    "fatty acid to the glycerol. Three fatty acids make three ester bonds and release three molecules of water. Hydrogen "
    "atoms on the carbons are not drawn."))
problems.extend(f.check())

# ---------------- Figure 4: phospholipid and bilayer ----------------
f = ChemFig("phospholipid")
f.text(10, 16, "A phospholipid", "tl tb")
f.circle(46, 56, 11, "f1 s-acc sw2")
f.multi([[(40, 67), (40, 110)], [(52, 67), (52, 110)]], "ln sw2", check=True)
f.text(78, 48, "phosphate head", "tl")
f.text(78, 64, "(hydrophilic, polar)", "tl")
f.line([(74, 56), (60, 56)], LEAD, check=False)
f.text(78, 94, "two fatty acid tails", "tl")
f.text(78, 110, "(hydrophobic, non-polar)", "tl")
f.line([(74, 100), (58, 100)], LEAD, check=False)
f.text(10, 148, "Phospholipids in water: a bilayer", "tl tb")
f.text(10, 176, "water", "tl")
xs = [30 + 20 * k for k in range(12)]
top, bot = 200, 268
f.multi([[(x - 4, top + 7), (x - 4, top + 32)] for x in xs] + [[(x + 4, top + 7), (x + 4, top + 32)] for x in xs], "ln", check=False)
f.multi([[(x - 4, bot - 7), (x - 4, bot - 32)] for x in xs] + [[(x + 4, bot - 7), (x + 4, bot - 32)] for x in xs], "ln", check=False)
for x in xs:
    f.circle(x, top, 7, "f1 s-acc sw2", check=False)
    f.circle(x, bot, 7, "f1 s-acc sw2", check=False)
f.text(10, 296, "water", "tl")
f.text(278, 230, "tails", "tl")
f.text(278, 246, "inside", "tl")
f.line([(274, 236), (262, 236)], LEAD, check=False)
figs.append(f.svg((330, 308),
    "Top: one phospholipid drawn as a round head with two tails; the head is a hydrophilic polar phosphate and the tails are "
    "hydrophobic fatty acids. Bottom: a bilayer in water. Two rows of phospholipids have their heads facing outwards towards water "
    "above and below and their tails pointing inwards, away from the water.",
    "In water, phospholipids form a bilayer: the hydrophilic heads face the water on both sides and the hydrophobic tails are hidden "
    "in the middle. Cell surface membranes are built on this structure."))
problems.extend(f.check())
finish(figs, problems)
