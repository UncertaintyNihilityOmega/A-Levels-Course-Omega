# data/fig_carbs.py: hand-drawn SVG figures of chapters/bio.carbs.md with label-clearance checks.
# Run: py data/fig_carbs.py > scratch/carbs_figs.txt   (figures on stdout, clearance report on stderr)
import math, sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p3 import ChemFig, haworth, trim, finish, ell_pts, LEAD

figs, problems = [], []
NUM = {1: (49, -3, "start"), 2: (31, 41, "start"), 3: (-31, 41, "end"), 4: (-47, -3, "end"), 5: (-12, -27, "start")}


def numbers(f, cx, cy, off=NUM):
    for c, (dx, dy, an) in off.items():
        f.text(cx + dx, cy + dy, str(c), "ts", an)


# ---------------- Figure 1: alpha- and beta-glucose ----------------
f = ChemFig("rings")
AL = {1: [("d", "OH"), ("u", "H", 18)], 2: [("d", "OH"), ("u", "H")], 3: [("u", "OH"), ("d", "H")],
      4: [("d", "OH"), ("u", "H")], 5: [("u", "CH₂OH", 16)]}
BE = {1: [("u", "OH", 18), ("d", "H")], 2: [("d", "OH"), ("u", "H")], 3: [("u", "OH"), ("d", "H")],
      4: [("d", "OH"), ("u", "H")], 5: [("u", "CH₂OH", 16)]}
for k, (cy, subs, title, note) in enumerate([
        (84, AL, "α-glucose", ["OH on carbon 1 is", "below the ring"]),
        (232, BE, "β-glucose", ["OH on carbon 1 is", "above the ring"])]):
    f.text(10, cy - 66, title, "tl tb")
    V = haworth(f, 100, cy, subs)
    numbers(f, 100, cy)
f_alpha_note = None
f.text(196, 70, "OH on carbon 1", "tl")
f.text(196, 84, "is below the ring", "tl")
f.line([(192, 90), (160, 100)], LEAD, check=False)
f.text(196, 213, "OH on carbon 1", "tl")
f.text(196, 227, "is above the ring", "tl")
f.line([(192, 221), (160, 212)], LEAD, check=False)
figs.append(f.svg((330, 306),
    "Haworth ring drawings of α-glucose and β-glucose. Each is a six-sided ring of five carbons and one oxygen, with carbon 6 "
    "(CH₂OH) above carbon 5. On carbon 1, the OH is below the ring in α-glucose and above the ring in β-glucose. On carbons 2 "
    "and 4 the OH is below the ring and on carbon 3 it is above the ring in both.",
    "α-glucose and β-glucose differ only in the position of the OH group on carbon 1: below the ring in α, above the ring in β. "
    "The other groups are the same in both."))
problems.extend(f.check())

# ---------------- Figure 2: maltose by condensation ----------------
f = ChemFig("maltose")
Lsubs = {1: [("d", "OH"), ("u", "H", 18)], 2: [("d", "OH"), ("u", "H")], 3: [("u", "OH"), ("d", "H")],
         4: [("d", "OH"), ("u", "H")], 5: [("u", "CH₂OH", 16)]}
f.text(10, 16, "Two α-glucose molecules", "tl tb")
haworth(f, 84, 92, Lsubs)
numbers(f, 84, 92)
haworth(f, 246, 92, Lsubs)
numbers(f, 246, 92)
f.text(165, 96, "+", "tl tb", "middle")
f.line([(165, 150), (165, 188)], "ln", "ah")
f.text(177, 164, "condensation", "tl")
f.text(177, 180, "(water removed)", "tl")
f.text(10, 214, "Maltose and water", "tl tb")
# maltose: ring A (left) joined to ring B through an oxygen between C1 of A and C4 of B
ax, bx, cy = 66, 214, 296
VA = {"O": (ax + 20, cy - 20), 1: (ax + 40, cy + 2), 2: (ax + 20, cy + 24), 3: (ax - 20, cy + 24),
      4: (ax - 40, cy + 2), 5: (ax - 20, cy - 20)}
VB = {"O": (bx + 20, cy - 20), 1: (bx + 40, cy + 2), 2: (bx + 20, cy + 24), 3: (bx - 20, cy + 24),
      4: (bx - 40, cy + 2), 5: (bx - 20, cy - 20)}
for V, subs in ((VA, {1: [("u", "H", 18)], 2: [("d", "OH"), ("u", "H")], 3: [("u", "OH"), ("d", "H")],
                       4: [("d", "OH"), ("u", "H")], 5: [("u", "CH₂OH", 16)]}),
                (VB, Lsubs | {4: [("u", "H")]})):
    f.line([V[5], trim(V["O"], V[5], 8)], "ln")
    f.line([trim(V["O"], V[1], 12), V[1]], "ln")
    f.line([V[1], V[2]], "ln")
    f.line([V[2], V[3]], "ln thick")
    f.line([V[3], V[4]], "ln")
    f.line([V[4], V[5]], "ln")
    f.atom(*V["O"])
    for c, lst in subs.items():
        for item in lst:
            f.sub(V[c][0], V[c][1], item[0], item[1], *(item[2:3]))
ox, oy = (VA[1][0] + VB[4][0]) / 2, cy + 22
f.line([VA[1], trim((ox, oy), VA[1], 9)], "ln")
f.line([VB[4], trim((ox, oy), VB[4], 9)], "ln")
f.atom(ox, oy)
numbers(f, ax, cy)
f.text(ox, 374, "1,4 glycosidic bond", "tl", "middle")
f.line([(ox, 362), (ox, oy + 10)], LEAD, check=False)
f.text(296, 328, "+ H₂O", "tl tb", "middle")
figs.append(f.svg((330, 384),
    "Condensation of two α-glucose molecules to form maltose. In the first row, two α-glucose rings stand side by side with a plus "
    "sign between them. An arrow labelled condensation, water removed, points down to the second row. There two glucose rings "
    "are joined through an oxygen atom between carbon 1 of the left ring and carbon 4 of the right ring, labelled 1,4 glycosidic "
    "bond, with a molecule of water as the second product.",
    "Maltose forms when the OH on carbon 1 of one α-glucose and the H of the OH on carbon 4 of another leave together as water. "
    "The oxygen left behind joins the two rings: a 1,4 glycosidic bond."))
problems.extend(f.check())

# ---------------- Figure 3: amylose, amylopectin, glycogen ----------------
f = ChemFig("storage")
R = 4.6


def beads(f, pts, links):
    f.multi([[pts[a], pts[b]] for a, b in links], "ln", check=False)
    for p in pts:
        f.circle(round(p[0], 1), round(p[1], 1), R, "f2 s-acc2 sw2")


def branch(start, direction, n, pts, links, step=13):
    prev = start
    ang = math.radians(direction)
    for _ in range(n):
        idx = len(pts)
        pts.append((round(pts[prev][0] + step * math.cos(ang), 1), round(pts[prev][1] + step * math.sin(ang), 1)))
        links.append((prev, idx))
        prev = idx
    return prev


f.text(10, 16, "Amylose: unbranched, coiled", "tl tb")
coil = [(round(30 + 5.4 * t + 15 * math.cos(t), 1), round(58 + 13 * math.sin(t), 1))
        for t in [k * 0.3 for k in range(0, 104)]]
f.line(coil, "c1 sw2", check=False)
f.text(10, 96, "1,4 glycosidic bonds only", "tl")

f.text(10, 126, "Amylopectin: a few branches", "tl tb")
pts = [(24 + 14 * i, 152) for i in range(15)]
links = [(i, i + 1) for i in range(14)]
branch(4, 62, 5, pts, links)
branch(10, 62, 5, pts, links)
beads(f, pts, links)
f.text(10, 234, "1,6 branch point", "tl")
f.line([(40, 221), (80, 160)], LEAD, check=False)

f.text(10, 262, "Glycogen: many more branches", "tl tb")
pts2 = [(24 + 14 * i, 320) for i in range(15)]
links2 = [(i, i + 1) for i in range(14)]
tips = []
for k, s in enumerate((2, 5, 8, 11)):
    sign = 1 if k % 2 == 0 else -1
    e = branch(s, 62 * sign, 4, pts2, links2)
    tips.append(e)
    branch(e - 2, 62 * sign - 40 * sign, 2, pts2, links2)
beads(f, pts2, links2)
f.text(86, 384, "free ends", "tl")
tx, ty = pts2[tips[0]]
f.line([(86, 378), (tx + 3, ty + 2)], LEAD, check=False)
figs.append(f.svg((330, 394),
    "Three schematic drawings of storage polysaccharides, each a chain of glucose units drawn as circles. Amylose is an unbranched "
    "chain coiled into a helix, with only 1,4 glycosidic bonds. Amylopectin is a long chain with a few 1,6 branch points. "
    "Glycogen has many more branches, so it has many free ends.",
    "Amylose is an unbranched coil. Amylopectin has a branch about every 24 to 30 glucose units; glycogen has one about every 8 "
    "to 12, so it has far more free ends where enzymes can work."))
problems.extend(f.check())

# ---------------- Figure 4: cellulose ----------------
f = ChemFig("cellulose")
f.text(10, 16, "Two cellulose chains side by side", "tl tb")
N = 7
for row, y in enumerate((64, 126)):
    hexes, flags, links = [], [], []
    for i in range(N):
        x = 34 + 40 * i
        hexes.append([(x + 14 * math.cos(math.radians(-90 + 60 * k)), y + 14 * math.sin(math.radians(-90 + 60 * k))) for k in range(6)])
        up = (i + row) % 2 == 0
        flags.append([(x, y - 14), (x, y - 22)] if up else [(x, y + 14), (x, y + 22)])
        f.circle(x, y - 24 if up else y + 24, 2.8, "fi")
        if i < N - 1:
            links.append([(x + 12.1, y), (x + 40 - 12.1, y)])
    f.multi(hexes, "f1 s-acc sw2", closed=True)
    f.multi(flags + links, "ln")
f.multi([[(x, 74), (x, 116)] for x in (54, 134, 214)], "ln-m thin dash", check=False)
f.text(10, 176, "Dot: the CH₂OH group. Alternate units are", "tl")
f.text(10, 192, "turned over, so the chain is straight.", "tl")
f.text(10, 212, "Dashed lines: hydrogen bonds between chains.", "tl")

f.text(10, 248, "From molecule to fibre", "tl tb")
f.line([(16, 270), (116, 270)], "ln")
f.text(130, 274, "one cellulose molecule", "tl")
f.rect(16, 288, 100, 36, "f1 s-acc sw2", 4)
f.multi([[(22, 294 + 5 * k), (110, 294 + 5 * k)] for k in range(6)], "ln-m thin", check=False)
f.text(130, 301, "microfibril: many chains", "tl")
f.text(130, 317, "joined by hydrogen bonds", "tl")
f.rect(16, 338, 100, 50, "f1 s-acc sw2", 4)
f.multi([[(22, 345 + 9 * k), (110, 345 + 9 * k)] for k in range(5)], "ln thick", check=False)
f.text(130, 367, "fibre: many microfibrils", "tl")
figs.append(f.svg((330, 400),
    "Cellulose. Top: two straight chains of β-glucose units, drawn as hexagons joined side by side, with alternate units turned "
    "over, shown by a dot above or below each unit. Dashed lines between the chains are hydrogen bonds. Bottom: one cellulose "
    "molecule, then a microfibril made of many chains, then a fibre made of many microfibrils.",
    "In cellulose, alternate β-glucose units are turned through 180°, so each chain is straight, and hydrogen bonds hold many chains "
    "side by side in microfibrils. Microfibrils are bundled into fibres."))
problems.extend(f.check())
finish(figs, problems)
