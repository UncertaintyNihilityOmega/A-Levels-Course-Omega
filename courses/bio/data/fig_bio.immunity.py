# data/fig_bio.immunity.py: builds the hand-drawn SVG figures of chapters/bio.immunity.md and checks them.
# Run: py data/fig_bio.immunity.py  -> writes data/out_immunity.json (name -> <figure> line) and a report on stderr.
# data/place_figs_p10.py pastes the output over the <figure data-ph="..."> placeholder lines of the chapter.
import json, sys
sys.path.insert(0, "data")
from figlib_p10 import *

out, problems = {}, []
E, B, N, L, A, D = "f1 s-acc sw2", "f2 s-acc2 sw2", "fm s-acc sw2", "f3 s-acc2 sw2", "fa s-acc2 sw2", "fh s-mute sw2"

# ============ Figure 1: phagocytosis, four stacked panels ============
PH = 132
f = Fig("phago")
titles = ["1  Chemotaxis", "2  Recognition and binding", "3  Engulfing (endocytosis)", "4  Digestion and antigen display"]
for i, t in enumerate(titles):
    f.text(8, i * PH + 14, t, "tl tb")

# panel 1
oy = 0
cell = blob(62, oy + 74, 30, 0.4)
f.poly(cell, E, name="cell1")
f.circle(66, oy + 72, 10, N, name="nuc1")
f.rect(120, oy + 66, 36, 16, B, rx=8, name="bact1")
for k, (x, y) in enumerate([(102, 60), (110, 72), (104, 88), (126, 56), (138, 51), (150, 57)]):
    f.circle(x, oy + y, 2.5, D, name=f"dot1{k}")
f.line([(56, oy + 32), (100, oy + 32)], "ln", "ah")
f.text(178, oy + 82, "bacterium")
f.leader((176, oy + 79), (152, oy + 74), "bact1")
f.text(178, oy + 50, "chemicals released")
f.leader((176, oy + 47), (151, oy + 56), "dot15")
f.text(14, oy + 124, "phagocyte")
f.leader((46, oy + 112), (46, oy + 96), "cell1")

# panel 2
oy = PH
f.poly(blob(62, oy + 74, 30, 0.4), E, name="cell2")
f.circle(56, oy + 70, 10, N)
f.rect(100, oy + 48, 22, 52, B, rx=9, name="bact2")
import math
for k, y in enumerate([58, 74, 90]):
    edge = 62 + math.sqrt(900 - (y - 74) ** 2)
    f.rect(round(edge - 2, 1), oy + y - 4, round(97 - (edge - 2), 1), 8, L, name=f"rec{k}")
    f.circle(100, oy + y, 3.5, A, name=f"ant{k}")
f.text(178, oy + 78, "bacterium")
f.leader((176, oy + 75), (116, oy + 74), "bact2")
f.text(6, oy + 124, "receptor")
f.leader((48, oy + 113), (92, oy + 91), "rec2")
f.text(108, oy + 124, "antigen")
f.leader((112, oy + 113), (100, oy + 91), "ant2")

# panel 3: two arms (pseudopodia) reach round the bacterium, which sits in a pocket of the cell
oy = 2 * PH
body = blob(66, oy + 74, 34, 0.9, n=72)
ang = lambda p: math.atan2(p[1] - (oy + 74), p[0] - 66) % (2 * math.pi)
left = sorted([q for q in body if 1.0 <= ang(q) <= 2 * math.pi - 1.0], key=ang)
arms = [(98, 43), (108, 47), (113, 55), (110, 58), (100, 60), (90, 62), (84, 67), (82, 74), (84, 81), (90, 86), (100, 88),
        (110, 90), (113, 93), (108, 101), (98, 105)]
cell3 = left + [(x, oy + y) for (x, y) in arms][::-1][::-1]
# the polygon runs: lower-right arc point -> round the left -> upper-right arc point; the arms close it in the order
# upper arm, pocket, lower arm, so reverse the arm list when the arc ends at the upper end
cell3 = left[::-1] + [(x, oy + y) for (x, y) in arms[::-1]]
f.poly(cell3, E, name="cell3")
f.circle(44, oy + 74, 11, N)
f.rect(88, oy + 66, 18, 16, B, rx=8, name="bact3")
rod = [(88 + 18 * k / 9, oy + 66) for k in range(10)] + [(88 + 18 * k / 9, oy + 82) for k in range(10)] + [(88, oy + 66 + 16 * k / 8) for k in range(9)] + [(106, oy + 66 + 16 * k / 8) for k in range(9)]
gap = 99
for (x, y) in rod:
    if inside((x, y), cell3):
        problems.append(f"phago: rod point {(x, y)} inside the cell outline in panel 3")
    for a_, b_ in zip(cell3, cell3[1:] + cell3[:1]):
        gap = min(gap, seg_pt(a_, b_, (x, y)))
print("panel 3 rod gap to cell", round(gap, 1), file=sys.stderr)
f.text(178, oy + 78, "bacterium")
f.leader((176, oy + 75), (103, oy + 74), "bact3")
f.text(178, oy + 118, "pseudopodium")
f.leader((176, oy + 115), (100, oy + 97), "cell3")

# panel 4
oy = 3 * PH
cell4 = blob(70, oy + 74, 34, 0.9)
f.poly(cell4, E, name="cell4")
f.circle(48, oy + 66, 10, N)
f.circle(90, oy + 76, 16, "fm2 s-acc sw2", name="phago4")
for (x, y) in [(84, 72), (94, 80), (88, 84)]:
    f.circle(x, oy + y, 2.6, B)
f.circle(92, oy + 56, 5, L, name="lys4")
f.circle(78, oy + 98, 5, L, name="lys4b")
f.circle(46, oy + 100, 3.5, A, name="ant4")
f.circle(36, oy + 90, 3.5, A)
f.text(178, oy + 62, "lysosome")
f.leader((176, oy + 59), (96, oy + 55), "lys4")
f.text(178, oy + 82, "phagosome")
f.leader((176, oy + 79), (102, oy + 78), "phago4")
f.text(178, oy + 102, "pieces of bacterium")
f.leader((176, oy + 99), (93, oy + 82), "phago4")
f.text(6, oy + 124, "antigen on surface")
f.leader((40, oy + 113), (46, oy + 102), "ant4")

f.vb = (330, 4 * PH)
problems.extend(f.check())
out["phago"] = f.svg(
    (330, 4 * PH),
    "Phagocytosis in four stages, each in its own panel. 1 Chemotaxis: a phagocyte with a nucleus moves towards "
    "chemicals released by a bacterium. 2 Recognition and binding: receptors on the phagocyte bind to antigens on the "
    "bacterium. 3 Engulfing: the surface membrane of the phagocyte folds round the bacterium with pseudopodia. 4 Digestion "
    "and antigen display: the bacterium is inside a phagosome, a lysosome has fused with the phagosome and its enzymes break "
    "the bacterium into pieces, and antigens from it are displayed on the surface of the cell.",
    "Phagocytosis. The arrow in panel 1 shows the direction in which the phagocyte moves. Antibodies attached to a pathogen "
    "(not drawn) make stage 2 easier. Only macrophages display antigens in stage 4. This is a drawing, not to scale.")

# ============ Figure 2: clonal selection and expansion ============
g = Fig("clonal")
W = 330


def box(x, y, w, lines, cls=E, name=None):
    h = 14 + 15 * len(lines)
    g.rect(x, y, w, h, cls, rx=6, name=name)
    for i, s in enumerate(lines):
        g.text(x + w / 2, y + 20 + 15 * i, s, "tl", "middle")
    return h


def arrow(x0, y0, x1, y1):
    g.line([(x0, y0), (x1, y1)], "ln", "ah")


LX, RX, CWD = 6, 176, 156          # left and right columns (x, x, width); centres 84 and 254
y = 6
hA = box(55, y, 220, ["Macrophage presents the", "antigen on its surface"], E, "A")
yB = y + hA + 26
arrow(165, y + hA + 2, 165, yB - 3)
hB = box(40, yB, 250, ["T-helper cell with a receptor", "complementary to the antigen", "binds to it: activated"], E)
yC = yB + hB + 26
arrow(165, yB + hB + 2, 165, yC - 3)
hC = box(40, yC, 250, ["T-helper cell divides by mitosis:", "a clone of T-helper cells forms", "and releases cytokines"], E)
yD = yC + hC + 40
arrow(84, yC + hC + 2, 84, yD - 3)
arrow(254, yC + hC + 2, 254, yD - 3)
g.text(94, yC + hC + 24, "cytokines")
g.text(264, yC + hC + 24, "cytokines")
hD = box(LX, yD, CWD, ["B-lymphocyte with a", "complementary", "receptor"], B)
box(RX, yD, CWD, ["T-killer cell with a", "complementary", "receptor"], B)
yE = yD + hD + 26
arrow(84, yD + hD + 2, 84, yE - 3)
arrow(254, yD + hD + 2, 254, yE - 3)
hE = box(LX, yE, CWD, ["Divides by mitosis:", "a clone of", "B cells"], E)
box(RX, yE, CWD, ["Divides by mitosis:", "a clone of", "T-killer cells"], E)
yF = yE + hE + 26
arrow(45, yE + hE + 2, 45, yF - 3)
arrow(125, yE + hE + 2, 125, yF - 3)
arrow(215, yE + hE + 2, 215, yF - 3)
arrow(295, yE + hE + 2, 295, yF - 3)
hF = box(LX, yF, 78, ["Plasma", "cells"], L)
box(92, yF, 76, ["Memory", "B cells"], L)
box(176, yF, 78, ["T-killer", "cells"], L)
box(260, yF, 70, ["Memory", "T cells"], L)
yG = yF + hF + 26
arrow(45, yF + hF + 2, 45, yG - 3)
arrow(215, yF + hF + 2, 215, yG - 3)
hG = box(LX, yG, 78, ["Secrete", "antibodies"], B)
box(176, yG, 150, ["Destroy infected", "body cells"], B)
g.vb = (W, yG + hG + 8)
problems.extend(g.check())
out["clonal"] = g.svg(
    g.vb,
    "Flow chart of the primary immune response. A macrophage presents the antigen. A T-helper cell with a complementary "
    "receptor is activated, divides by mitosis to form a clone and releases cytokines. The cytokines act on a B-lymphocyte "
    "and a T-killer cell that each have a receptor complementary to the antigen. The B cell divides by mitosis to form a "
    "clone that becomes plasma cells, which secrete antibodies, and memory B cells. The T-killer cell divides by mitosis "
    "to form a clone that becomes T-killer cells, which destroy infected body cells, and memory T cells.",
    "Clonal selection and clonal expansion. Only the few lymphocytes whose receptors are complementary to the antigen are "
    "selected; each selected cell divides by mitosis to make a clone. Memory cells are kept for the secondary response.")

json.dump(out, open("data/out_immunity.json", "w", encoding="utf-8"), ensure_ascii=False)
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
