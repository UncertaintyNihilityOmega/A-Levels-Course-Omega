# data/fig_bio.enzymes2.py: hand-drawn SVG figures of chapters/bio.enzymes2.md with a label-clearance check.
# Run: py data/fig_bio.enzymes2.py > scratch/enzymes2_figs.txt (figures on stdout, clearance report on stderr).
import sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p4 import Fig, sh

figs, problems = [], []
E, S, I = "f1 s-acc sw2", "f2 s-acc2 sw2", "f3 s-acc sw2"
ROW = 150
SUB = [(90, 62), (150, 62), (150, 70), (145, 70), (135, 92), (105, 92), (95, 70), (90, 70)]
FIT = [(95, 70), (105, 92), (135, 92), (145, 70)]
LOOSE = [(104, 70), (112, 78), (128, 78), (136, 70)]       # active site distorted by a bound inhibitor
INH = [(98, 66), (142, 66), (145, 70), (135, 92), (105, 92), (95, 70)]   # fits the active site closely
SIDE = [(200, 82), (214, 82), (222, 91), (214, 100), (200, 100)]          # binds on the side of the enzyme


def enzyme(notch):
    return [(40, 70)] + notch + [(200, 70), (200, 112), (40, 112)]


# ---------- Figure 1: how the two kinds of inhibitor bind ----------
f = Fig("inhibitors")
titles = ["1  No inhibitor: substrate binds", "2  Competitive inhibitor in the active site",
          "3  Non-competitive inhibitor elsewhere"]
for r in range(3):
    oy = r * ROW
    f.text(10, oy + 16, titles[r], "tl tb")
    f.poly(sh(enzyme(FIT if r < 2 else LOOSE), 0, oy), E)
    if r == 0:
        f.poly(sh(SUB, 0, oy), S)
        f.text(232, oy + 50, "substrate", "tl")
        f.leader((228, oy + 46), (152, oy + 66))
        f.text(10, oy + 130, "active site occupied", "tl")
        f.leader((100, oy + 116), (115, oy + 94))
    elif r == 1:
        f.poly(sh(SUB, 0, oy - 32), S)
        f.poly(sh(INH, 0, oy), I)
        f.text(232, oy + 38, "substrate", "tl")
        f.leader((228, oy + 34), (154, oy + 34))
        f.text(232, oy + 74, "competitive", "tl")
        f.text(232, oy + 88, "inhibitor", "tl")
        f.leader((228, oy + 82), (146, oy + 82))
        f.text(10, oy + 130, "active site blocked", "tl")
        f.leader((100, oy + 116), (115, oy + 94))
    else:
        f.poly(sh(SUB, 0, oy - 32), S)
        f.poly(sh(SIDE, 0, oy), I)
        f.text(232, oy + 38, "substrate", "tl")
        f.leader((228, oy + 34), (154, oy + 34))
        f.text(232, oy + 122, "non-competitive", "tl")
        f.text(232, oy + 136, "inhibitor", "tl")
        f.leader((236, oy + 108), (221, oy + 100))
        f.text(10, oy + 130, "active site changed shape", "tl")
        f.leader((100, oy + 116), (115, oy + 80))
figs.append(f.svg((345, 3 * ROW + 24),
    "Three stages. 1: with no inhibitor the substrate fits the active site and forms an enzyme–substrate complex. "
    "2: a competitive inhibitor, with a shape like the substrate, sits in the active site, so the substrate cannot bind. "
    "3: a non-competitive inhibitor binds to the enzyme away from the active site and changes the shape of the active "
    "site, so the substrate no longer fits.",
    "How inhibitors bind. A competitive inhibitor competes with the substrate for the active site. A non-competitive "
    "inhibitor binds somewhere else on the enzyme and changes the shape of the active site, whatever the substrate "
    "concentration."))
problems.extend(f.check())

# ---------- Figure 2: immobilised enzyme column ----------
g = Fig("column")
g.line([(100, 12), (100, 46)], "ln", "ah")
g.text(112, 22, "milk (lactose) in", "tl")
g.rect(60, 50, 80, 130, "fp ln")
for ry, row in enumerate(range(66, 166, 18)):
    for cx in ([76, 94, 112, 130] if ry % 2 == 0 else [85, 103, 121]):
        g.circle(cx, row, 8, "f2 s-acc2 sw2")
g.rect(60, 172, 80, 10, "fm s-acc sw2")
g.line([(100, 182), (100, 214)], "ln", "ah")
g.text(112, 204, "product out", "tl")
g.text(112, 218, "(no enzyme)", "tl")
g.text(160, 96, "alginate beads", "tl")
g.leader((156, 92), (142, 98))
g.text(160, 164, "glass wool", "tl")
g.leader((156, 160), (142, 175))
g.circle(300, 120, 38, "fp s-acc sw2")
for cx, cy in [(285, 105), (312, 100), (298, 125), (322, 128), (280, 138), (305, 146)]:
    g.circle(cx, cy, 4, "f1 s-acc sw2")
g.text(300, 176, "enzyme in", "tl", "middle")
g.text(300, 190, "alginate gel", "tl", "middle")
figs.append(g.svg((350, 232),
    "A column of alginate beads. Milk containing lactose enters at the top, flows between beads that hold the enzyme "
    "trapped in alginate gel, passes a glass wool plug and leaves at the bottom as product with no enzyme in it. A "
    "magnified bead shows enzyme molecules trapped in the gel.",
    "An immobilised enzyme column. The enzyme stays in the beads, so the liquid leaving the column holds the product "
    "but no enzyme, and the beads can be used again. The circle on the right shows one bead magnified."))
problems.extend(g.check())

for s in figs:
    print(s)
    print()
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
