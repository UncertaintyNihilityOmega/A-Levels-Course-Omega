# data/fig_bio.cells.py: SVG figures of chapters/bio.cells.md. Run: py data/fig_bio.cells.py > scratch/c.html
# Prints each <figure> (paste into the chapter) and a clearance report on stderr.
import math, sys
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p2 import Fig, finish, ell_pts

figs, problems = [], []


def on(cx, cy, rx, ry, deg):
    t = math.radians(deg)
    return (cx + rx * math.cos(t), cy + ry * math.sin(t))


def outline(cx, cy, rx, ry, n=180):
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / n
        m = 1 + 0.025 * math.sin(3 * t + 0.6) + 0.02 * math.cos(5 * t)
        pts.append((cx + rx * m * math.cos(t), cy + ry * m * math.sin(t)))
    return pts


def edge_y(poly, x, bottom=True):
    best = None
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (x1 - x) * (x2 - x) <= 0 and x1 != x2:
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            best = y if best is None else (max(best, y) if bottom else min(best, y))
    return best


def edge_x(poly, y, right=True):
    best = None
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (y1 - y) * (y2 - y) <= 0 and y1 != y2:
            x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            best = x if best is None else (max(best, x) if right else min(best, x))
    return best


# ---------------------------------------------------------------- animal cell (named and lettered)
def animal(letters):
    f = Fig("animal-letters" if letters else "animal")
    f.tf = (330, 200, 212, 125, 0.6)   # REVIEW P2: 400-wide fig small so labels are about 11 px on a phone
    cell = outline(330, 200, 175, 150)
    f.smooth(cell, "f1 s-acc sw2")
    # nucleus
    f.ellipse(320, 185, 72, 62, "fm s-acc sw2")
    f.ellipse(320, 185, 66, 56, "ln", check=False)
    f.ellipse(312, 180, 17, 16, "fi", check=False)
    # rough ER (flattened sacs with ribosomes on the outside)
    for cy in (128, 141, 154):
        f.ellipse(215, cy, 34, 5.5, "f2 s-acc2 sw2", check=False)
        f.dots([(215 + dx, cy - 7) for dx in (-24, -12, 0, 12, 24)] + [(215 + dx, cy + 7) for dx in (-18, 0, 18)], 1.7, "fi")
    # smooth ER (tubes, no ribosomes)
    for oy in (0, 14, 28):
        pts = [(200 + 10 * i, 258 + oy + (5 if i % 2 else -5)) for i in range(9)]
        f.smooth(pts, "c3 sw2", False, check=False)
    # free ribosomes
    f.dots([(240, 92), (256, 100), (270, 90), (285, 100), (300, 92), (262, 112), (345, 100), (365, 112), (385, 98)], 2, "fi")
    f.dots([(340, 262), (362, 276), (330, 288), (372, 300), (350, 306), (310, 300), (300, 270)], 2, "fi")
    # mitochondria
    for (mx, my) in ((210, 222), (415, 290)):
        f.ellipse(mx, my, 24, 11, "f2 s-acc2 sw2", check=False)
        f.ellipse(mx, my, 20, 7.5, "fp ln", check=False)
        for dx in (-9, 0, 9):
            f.line([(mx + dx, my - 7), (mx + dx, my + 1)], "ln", check=False)
    # lysosome
    f.circle(240, 312, 9, "fa s-acc sw2", check=False)
    # Golgi body: stack of curved sacs and vesicles
    for k in range(4):
        pts = [(412 + 56 * i / 12, 206 + 11 * k + 6 * math.sin(math.pi * i / 12) * -1 + 0) for i in range(13)]
        f.smooth(pts, "c3 sw2", False, check=False)
    f.dots([(408, 258), (480, 214), (486, 238)], 4, "f2 s-acc2 sw2")
    # centrioles: two short tubes at right angles
    f.rect(384, 104, 8, 24, "f3 s-acc sw2", check=False)
    f.rect(396, 130, 24, 8, "f3 s-acc sw2", check=False)
    # microvilli on the lower surface
    for i in range(7):
        x = 268 + 17 * i
        by = edge_y(cell, x + 4, True)
        f.poly([(x, by - 3), (x, by + 14), (x + 1.5, by + 18), (x + 6.5, by + 18), (x + 8, by + 14), (x + 8, by - 3)], "f1 s-acc sw2", closed=False, check=False)
    mv_tip = (382, edge_y(cell, 374, True) + 10)
    items = [
        # key, letter, side, label y (figure coordinates), lines, target (drawing coordinates)
        ("mem", None, "L", 33, ["cell surface", "membrane"], (edge_x(cell, 75, False) + 1, 75)),
        ("rib", None, "L", 65, ["free", "ribosomes"], (236, 92)),
        ("rer", "B", "L", 93, ["rough ER"], (181, 141)),
        ("nucleolus", "nucleolus", "L", 115, ["nucleolus"], (298, 181)),
        ("mit", "D", "L", 139, ["mitochondrion"], (187, 223)),
        ("ser", "H", "L", 165, ["smooth ER"], (203, 268)),
        ("lys", "E", "L", 193, ["lysosome"], (230, 313)),
        ("cen", "F", "R", 81, ["centrioles"], (422, 134)),
        ("nuc", "A", "R", 105, ["nuclear", "envelope"], (389, 168)),
        ("gol", "C", "R", 139, ["Golgi body"], (472, 228)),
        ("mv", "G", "R", 232, ["microvilli"], (mv_tip[0], 358)),
    ]
    targets = [(k, f.P(*t)) for (k, _, _, _, _, t) in items]
    ys = {k: y for (k, _, _, y, _, _) in items}
    f.tf = None
    LX, RX = 96, 326
    for (key, letter, side, _, lines, _), (_, tgt) in zip(items, targets):
        if letters and (letter is None or key == "nucleolus"):
            continue
        ly = ys[key]
        anchor = "end" if side == "L" else "start"
        lx = LX if side == "L" else RX
        ax = lx + (4 if side == "L" else -4)
        if letters:
            f.text(lx, ly, letter, "tl tb", anchor)
            first = letter
        else:
            n = len(lines)
            for i, t in enumerate(lines):
                f.text(lx, ly - 7 * (n - 1) + 14 * i, t, "tl", anchor)
            first = lines[0]
        f.line([(ax, ly - 3), tgt], "ln-m thin", check=False)
        f.leads.append(((ax, ly - 3), tgt, first))
    return f


f = animal(False)
figs.append(f.svg((400, 244),
    "Animal cell as seen with a transmission electron microscope, with labels. The large nucleus has a double nuclear "
    "envelope and a dark nucleolus. Stacks of flattened sacs studded with ribosomes are the rough endoplasmic reticulum; "
    "tubes without ribosomes are the smooth endoplasmic reticulum. A Golgi body is a stack of curved sacs with vesicles "
    "nearby. Two mitochondria show folded inner membranes, a lysosome is a small round sac, and two centrioles lie at "
    "right angles. Finger-like microvilli project from the lower surface, and small dots are free ribosomes.",
    "An animal cell as a drawing of a transmission electron micrograph. Compare it with the plant cell below: this cell "
    "has centrioles and no cell wall, chloroplasts or large permanent vacuole."))
problems.extend(f.check())

f = animal(True)
figs.append(f.svg((400, 244),
    "The same animal cell with eight structures marked by letters. A is the nuclear envelope, B a stack of ribosome-studded "
    "sacs, C a Golgi body, D a mitochondrion, E a small round sac, F two short tubes at right angles, G finger-like "
    "projections from the lower surface and H smooth tubes.",
    "Structures A to H of an animal cell, for the identification example and the practice questions."))
problems.extend(f.check())

# ---------------------------------------------------------------- plant cell
f = Fig("plant")
f.tf = (350, 186, 232, 120, 0.6)   # REVIEW P2: 400-wide fig small
f.rect(160, 36, 331, 300, "fm s-acc sw2", 18)                      # cell wall (thick band)
f.rect(174, 50, 292, 272, "f1 s-acc sw2", 10)                      # cell surface membrane inside the wall
f.rect(491, 45, 49, 282, "f1 s-acc sw2", 12, check=False)         # neighbouring cell
f.ellipse(340, 180, 100, 105, "f2 s-acc2 sw2")                     # large permanent vacuole (outline = tonoplast)
f.ellipse(205, 288, 32, 26, "fm s-acc sw2")
f.ellipse(205, 288, 27, 21, "ln", check=False)
f.ellipse(200, 284, 8, 8, "fi", check=False)
for (cx, cy) in ((215, 120), (435, 150)):
    f.ellipse(cx, cy, 24, 12, "fok s-acc sw2", check=False)
    for dx in (-10, 0, 10):
        f.line([(cx + dx, cy - 6), (cx + dx, cy + 6)], "ln", check=False)
for (mx, my) in ((205, 200), (440, 262)):
    f.ellipse(mx, my, 16, 8, "f2 s-acc2 sw2", check=False)
    f.ellipse(mx, my, 12, 5, "fp ln", check=False)
f.dots([(190, 235), (240, 330), (300, 310), (350, 312), (410, 300), (400, 120), (300, 60), (260, 70), (370, 62)], 2, "fi")
f.line([(466, 112), (505, 112)], "c3 sw3", check=False)             # plasmodesma through the wall
f.line([(466, 244), (505, 244)], "c3 sw3", check=False)
L = 112
items = [  # label y (figure coordinates), lines, target (drawing coordinates)
    (40, ["cell wall"], (167, 70)),
    (66, ["cell surface", "membrane"], (175, 99)),
    (92, ["chloroplast"], (192, 121)),
    (110, ["cytoplasm"], (184, 154)),
    (134, ["large permanent", "vacuole"], (300, 178)),
    (160, ["mitochondrion"], (210, 207)),
    (178, ["tonoplast"], (260, 241)),
    (196, ["nucleus"], (176, 288)),
    (214, ["nucleolus"], (196, 288)),
]
mapped = [(y, lines, f.P(*t)) for (y, lines, t) in items]
pd = f.P(485, 112)
f.tf = None
for ly, lines, tgt in mapped:
    n = len(lines)
    for i, t in enumerate(lines):
        f.text(L, ly - 7 * (n - 1) + 14 * i, t, "tl", "end")
    f.line([(L + 4, ly - 3), tgt], "ln-m thin", check=False)
    f.leads.append(((L + 4, ly - 3), tgt, lines[0]))
f.text(398, 16, "plasmodesma", "tl", "end")
f.line([(345, 20), pd], "ln-m thin", check=False)
f.leads.append(((345, 20), pd, "plasmodesma"))
figs.append(f.svg((400, 228),
    "Plant cell as seen with an electron microscope, with labels. A thick cell wall surrounds the cell surface membrane. "
    "A large permanent vacuole, bounded by the tonoplast, fills most of the cell. The cytoplasm holds a nucleus with a "
    "nucleolus, chloroplasts, mitochondria and ribosomes. At the right, a narrow strand of cytoplasm, a plasmodesma, "
    "passes through the wall into the neighbouring cell.",
    "A plant cell as a drawing of an electron micrograph. Compare it with the animal cell: this cell has a cell wall, "
    "chloroplasts, a large permanent vacuole and plasmodesmata, and no centrioles."))
problems.extend(f.check())

# ---------------------------------------------------------------- mitochondrion
f = Fig("mito")
cx, cy, rx, ry = 100, 100, 92, 58
f.ellipse(cx, cy, rx, ry, "f2 s-acc2 sw2")
f.ellipse(cx, cy, rx - 8, ry - 8, "fp ln")
for k in range(-4, 5):
    x = cx + k * 17
    half = (ry - 8) * math.sqrt(max(0, 1 - ((x - cx) / (rx - 8)) ** 2))
    if k % 2 == 0:
        f.line([(x, cy - half), (x, cy - half + 22)], "ln", check=False)
    else:
        f.line([(x, cy + half), (x, cy + half - 22)], "ln", check=False)
f.circle(128, 104, 8, "c3 sw2", check=False)                          # circular DNA
f.dots([(150, 124), (160, 118), (142, 116), (90, 102), (104, 112)], 2.4, "fi")    # 70S ribosomes
X0 = 206
f.label(X0 + 6, 14, "outer membrane", (X0 + 2, 11), on(cx, cy, rx, ry, -52), "start")
f.label(X0 + 6, 38, "inner membrane", (X0 + 2, 35), on(cx, cy, rx - 8, ry - 8, -30), "start")
f.label(X0 + 6, 62, "cristae", (X0 + 2, 59), (cx + 4 * 17 + 1, 80), "start")
f.label(X0 + 6, 90, "matrix", (X0 + 2, 87), (178, 90), "start")
f.label(X0 + 6, 112, "circular DNA", (X0 + 2, 109), (137, 105), "start")
f.label(X0 + 6, 138, "70S ribosomes", (X0 + 2, 135), (162, 122), "start")
figs.append(f.svg((330, 176),
    "Longitudinal section of a mitochondrion. A smooth outer membrane surrounds an inner membrane that is folded into "
    "cristae. The fluid inside, the matrix, contains a small loop of circular DNA and small 70S ribosomes.",
    "A mitochondrion. The double membrane, the folded inner membrane (cristae), the matrix, circular DNA and 70S ribosomes "
    "are the features to recognise in an electron micrograph.", "fig small"))
problems.extend(f.check())

# ---------------------------------------------------------------- chloroplast
f = Fig("chloroplast")
cx, cy, rx, ry = 100, 92, 92, 60
f.ellipse(cx, cy, rx, ry, "f2 s-acc2 sw2")
f.ellipse(cx, cy, rx - 8, ry - 8, "fp ln")
for gx in (50, 82, 114, 146):
    for j in range(4):
        f.rect(gx - 13, 66 + j * 7, 26, 5, "f1 s-acc sw2", 2, check=False)
for gx in (50, 82, 114):
    f.line([(gx + 13, 78), (gx + 19, 78)], "ln-m thin", check=False)
f.ellipse(150, 118, 14, 9, "fm s-acc sw2", check=False)             # starch grain
f.circle(118, 128, 8, "c3 sw2", check=False)                          # circular DNA
f.dots([(86, 128), (96, 136), (78, 138), (100, 124)], 2.4, "fi")
X0 = 206
f.text(X0 + 6, 14, "envelope (two", "tl")
f.text(X0 + 6, 28, "membranes)", "tl")
f.line([(X0 + 2, 11), on(cx, cy, rx, ry, -40)], "ln-m thin", check=False); f.leads.append(((X0 + 2, 11), on(cx, cy, rx, ry, -40), "envelope (two"))
f.label(X0 + 6, 62, "granum", (X0 + 2, 59), (160, 76), "start")
f.label(X0 + 6, 88, "thylakoid", (X0 + 2, 85), (160, 88), "start")
f.label(X0 + 6, 112, "stroma", (X0 + 2, 109), (172, 100), "start")
f.label(X0 + 6, 150, "starch grain", (X0 + 2, 147), (160, 122), "start")
f.label(X0 + 6, 172, "circular DNA", (X0 + 2, 169), (127, 131), "start")
f.label(X0 + 6, 194, "70S ribosomes", (X0 + 2, 191), (101, 138), "start")
figs.append(f.svg((330, 206),
    "Section of a chloroplast. Two membranes form the envelope. Inside, stacks of flattened sacs called thylakoids form "
    "grana, joined by single thylakoids, and the fluid around them is the stroma. A starch grain, a loop of circular DNA "
    "and small 70S ribosomes lie in the stroma.",
    "A chloroplast. The double membrane (envelope), grana (stacks of thylakoids), stroma, starch grains, circular DNA and "
    "70S ribosomes identify it.", "fig small"))
problems.extend(f.check())

# ---------------------------------------------------------------- secretory pathway
f = Fig("secretory")
for cy in (26, 40, 54):
    f.ellipse(90, cy, 70, 6.5, "f2 s-acc2 sw2", check=False)
    f.dots([(90 + dx, cy - 8) for dx in (-50, -25, 0, 25, 50)], 1.8, "fi")
f.dots([(90, 96)], 8, "f2 s-acc2 sw2")
f.line([(90, 64), (90, 80)], "ln", "ah", check=False)
f.line([(90, 106), (90, 126)], "ln", "ah", check=False)
for k in range(4):
    pts = [(42 + 96 * i / 12, 146 + 11 * k + 7 * math.sin(math.pi * i / 12) * -1) for i in range(13)]
    f.smooth(pts, "c3 sw2", False, check=False)
f.dots([(90, 212)], 8, "f2 s-acc2 sw2")
f.line([(90, 184), (90, 198)], "ln", "ah", check=False)
f.line([(90, 222), (90, 252)], "ln", "ah", check=False)
f.line([(20, 268), (74, 268)], "ln thick", check=False)
f.line([(106, 268), (160, 268)], "ln thick", check=False)
f.poly([(74, 268), (78, 262), (90, 258), (102, 262), (106, 268)], "f2 s-acc2 sw2", closed=False, check=False)
f.dots([(76, 296), (94, 304), (110, 292)], 2.6, "fi")
X0 = 182
f.text(X0, 22, "1  Protein made on", "tl tb"); f.text(X0, 36, "ribosomes, folds in", "tl"); f.text(X0, 50, "the RER", "tl")
f.text(X0, 90, "2  Vesicle carries", "tl tb"); f.text(X0, 104, "it to the Golgi", "tl"); f.text(X0, 118, "body", "tl")
f.text(X0, 148, "3  Golgi body", "tl tb"); f.text(X0, 162, "modifies and", "tl"); f.text(X0, 176, "packages it", "tl")
f.text(X0, 212, "4  Secretory", "tl tb"); f.text(X0, 226, "vesicle moves to", "tl"); f.text(X0, 240, "the surface", "tl")
f.text(X0, 275, "5  Vesicle fuses with", "tl tb"); f.text(X0, 289, "the membrane: the", "tl"); f.text(X0, 303, "protein is released", "tl")
figs.append(f.svg((340, 320),
    "The secretory pathway in five steps. 1: a protein is made on ribosomes on the rough endoplasmic reticulum and folds "
    "inside it. 2: a vesicle carries it to the Golgi body. 3: the Golgi body modifies and packages it. 4: a secretory "
    "vesicle moves to the cell surface membrane. 5: the vesicle fuses with the membrane and the protein is released "
    "outside the cell by exocytosis.",
    "From ribosome to exocytosis: the route of a secreted protein through the cell. Every step that moves or changes the "
    "protein uses ATP from respiration.", "fig small"))
problems.extend(f.check())

# ---------------------------------------------------------------- microvilli and cilia
f = Fig("ciliavilli")
f.text(10, 16, "Microvilli (surface area)", "tl tb")
f.line([(10, 100), (250, 100)], "c1 sw2", check=False)
for i in range(11):
    x = 22 + 21 * i
    f.poly([(x, 100), (x, 62), (x + 2, 58), (x + 9, 58), (x + 11, 62), (x + 11, 100)], "f1 s-acc sw2", closed=False, check=False)
f.rect(10, 100, 240, 16, "f1 s-acc sw2", check=False)
f.text(10, 144, "Cilia (movement)", "tl tb")
f.line([(10, 262), (230, 262)], "c1 sw2", check=False)
for i in range(8):
    x = 28 + 26 * i
    f.poly([(x, 262), (x + 1, 215), (x + 3, 190), (x + 6, 172), (x + 9, 172), (x + 8, 190), (x + 6, 215), (x + 5, 262)], "f1 s-acc sw2", closed=False, check=False)
f.rect(10, 262, 220, 16, "f1 s-acc sw2", check=False)
# cross-section of a cilium: nine pairs round two central tubes
ccx, ccy, cr = 286, 200, 20
for k in range(9):
    # REVIEW P1-P3: a pair of microtubules at each of the nine positions (the caption says nine pairs)
    for d in (-7, 7):
        px, py = on(ccx, ccy, cr, cr, 40 * k + d)
        f.dots([(px, py)], 2.4, "f2 s-acc2")
f.dots([(ccx - 4, ccy), (ccx + 4, ccy)], 3.4, "fm s-acc sw2")
f.ellipse(ccx, ccy, 28, 28, "ln", check=False)
f.text(326, ccy + 52, "cross-section", "tl", "end")
f.text(326, ccy + 66, "of one cilium", "tl", "end")
figs.append(f.svg((330, 290),
    "Two panels. Microvilli: many short finger-like projections of the cell surface membrane that increase the surface "
    "area. Cilia: longer hair-like projections that beat to move fluid; a cross-section of one cilium shows nine pairs "
    "of microtubules round two central microtubules.",
    "Microvilli (top) are short extensions of the cell surface that increase surface area for absorption or secretion. "
    "Cilia (below) are longer and move; each contains microtubules in a ring of nine pairs plus two in the centre.", "fig small"))
problems.extend(f.check())

finish(figs, problems)
