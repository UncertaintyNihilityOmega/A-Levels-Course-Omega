# data/fig_bio.mitosis.py: builds the hand-drawn SVG figures of chapters/bio.mitosis.md and checks label clearance.
# Run: py data/fig_bio.mitosis.py -> prints each <figure> (paste into the chapter) and a clearance report on stderr.
import math, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from figkit_p6 import Fig, ellipse, arc_pts, xchrom, vchrom, LEAD

sys.stdout.reconfigure(encoding="utf-8")
figs, problems = [], []
CELL = "fp ln"


def lead(f, a, b):
    f.leader(a, b)


# ---------- Figure 1: chromosome structure (small) ----------
f = Fig("chromosome")
cx = 80
for dx in (-13, 13):                       # two sister chromatids (capsules)
    x = cx + dx
    pts = [(x - 11, 52), (x + 11, 52), (x + 11, 108), (x + 5, 120), (x + 11, 132), (x + 11, 188), (x - 11, 188),
           (x - 11, 132), (x - 5, 120), (x - 11, 108)]
    f.poly(pts, "fm s-acc sw2", check=False)
for dx in (-13, 13):                       # telomeres: caps at the four ends
    x = cx + dx
    f.rect(x - 11, 40, 22, 12, "f2 s-acc2 sw2")
    f.rect(x - 11, 188, 22, 12, "f2 s-acc2 sw2")
f.parts.append(f'<ellipse class="fi" cx="{cx}" cy="120" rx="9" ry="6"/>')
# labels
f.text(150, 62, "telomere")
lead(f, (146, 58), (cx + 15, 46))
f.text(150, 112, "sister chromatids")
lead(f, (146, 108), (cx + 22, 92))
f.text(150, 142, "centromere")
lead(f, (146, 138), (cx + 8, 122))
f.text(150, 24, "replicated chromosome", "tl tb")
# DNA wound round histones (below)
f.text(10, 226, "Zoom in on the DNA:", "tl tb")
beads = [60, 120, 180, 240]
by = 262
for bx in beads:
    f.circle(bx, by, 14, "f2 s-acc2 sw2")
path_pts = [(8, by + 6)]
for i, bx in enumerate(beads):
    top = i % 2 == 0
    pts = arc_pts(bx, by, 19, 19, 200, 340, 12) if top else arc_pts(bx, by, 19, 19, 160, 20, 12)
    path_pts += pts
path_pts.append((300, by + 6))
f.line(path_pts, "c1 sw2", check=False)
f.text(10, 300, "DNA", "tl")
lead(f, (36, 296), (50, by + 18))
f.text(150, 300, "histone proteins")
lead(f, (146, 296), (130, by + 12))
figs.append(f.svg((330, 312),
    "A replicated chromosome has two identical sister chromatids joined at the centromere, with a telomere at each end. "
    "Below, a zoom shows the DNA molecule wound round beads of histone proteins.",
    "A replicated chromosome (drawing). The two sister chromatids are identical copies of one DNA molecule, held together at "
    "the centromere. Telomeres cap all four ends. In the zoom, each DNA molecule is wound round histone proteins, then coiled "
    "again and again to make a short, thick chromosome."))
problems.extend(f.check())

# ---------- Figure 2: the cell cycle (small) ----------
f = Fig("cycle")
CX, CY, RO, RI = 165, 138, 68, 38
phases = [("G1", 0, 144), ("S", 144, 252), ("G2", 252, 324), ("M", 324, 342), ("C", 342, 360)]
fills = {"G1": "f1 s-acc sw2", "S": "f2 s-acc2 sw2", "G2": "f1 s-acc sw2", "M": "fm s-acc sw2", "C": "fm2 s-acc sw2"}


def pol(r, deg):                      # deg clockwise from 12 o'clock
    t = math.radians(deg)
    return (round(CX + r * math.sin(t), 1), round(CY - r * math.cos(t), 1))


for name, d0, d1 in phases:
    n = max(3, int((d1 - d0) / 6))
    outer = [pol(RO, d0 + (d1 - d0) * k / n) for k in range(n + 1)]
    inner = [pol(RI, d1 - (d1 - d0) * k / n) for k in range(n + 1)]
    f.poly(outer + inner, fills[name])
for name, deg in (("G1", 72), ("S", 198), ("G2", 288)):
    x, y = pol((RO + RI) / 2, deg)
    f.parts.append(f'<text class="tl tb" x="{x:g}" y="{y + 4:g}" text-anchor="middle">{name}</text>')
f.text(CX, CY + 4, "cycle", "tl", "middle")
# outside labels
f.text(CX + RO + 8, 112, "G1: growth,")
f.text(CX + RO + 8, 126, "normal work")
f.text(CX + 0, CY + RO + 22, "S: DNA is copied", "tl", "middle")
f.text(CX - RO - 8, 112, "G2: growth", "tl", "end")
f.text(CX - RO - 8, 126, "and checks", "tl", "end")
f.text(CX - 62, 30, "mitosis", "tl", "end")
lead(f, (CX - 58, 26), pol(RO - 6, 333))
f.text(CX + 36, 30, "cytokinesis")
lead(f, (CX + 32, 26), pol(RO - 6, 351))
# arrow showing the direction (clockwise), drawn as a short arc just outside the ring
figs.append(f.svg((330, 250),
    "The cell cycle drawn as a ring, clockwise from the top: G1 phase (growth), S phase (DNA replication), G2 phase "
    "(growth and checks), then mitosis and cytokinesis. G1, S and G2 together are interphase.",
    "The cell cycle. G1, S and G2 together are interphase, which takes most of the cycle. Mitosis (division of the nucleus) is "
    "followed by cytokinesis (division of the cytoplasm). The sizes of the sectors are for a cell with a 20-hour cycle."))
problems.extend(f.check())


# ---------- Figures 3 and 4: the stages of mitosis in an animal cell (2n = 4), two panels each ----------
PH = 150


def cell(f, oy, rx=62, ry=62, cxx=72):
    ellipse(f, cxx, oy + 76, rx, ry, CELL)


def centriole(f, x, y):
    f.parts.append(f'<rect class="fi" x="{x - 2:g}" y="{y - 6:g}" width="4" height="12"/>')
    f.parts.append(f'<rect class="fi" x="{x - 6:g}" y="{y - 2:g}" width="12" height="4"/>')


def panel_title(f, oy, s):
    f.text(152, oy + 24, s, "tl tb")


def prophase(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    ellipse(f, cx, cy, 34, 34, "ln-m thin dash")
    for (dx, dy, L, c, a) in [(-12, -14, 24, "c1", 30), (12, -6, 24, "c1", -40), (-8, 14, 16, "c2", 80), (14, 16, 16, "c2", 10)]:
        xchrom(f, cx + dx, cy + dy, L, c + " sw3", a)
    centriole(f, cx - 50, cy)
    centriole(f, cx + 50, cy)
    panel_title(f, oy, "1  Prophase")
    f.text(152, oy + 50, "chromosomes condense")
    lead(f, (148, oy + 46), (cx + 24, cy - 10))
    f.text(152, oy + 82, "nuclear envelope")
    f.text(152, oy + 96, "breaking down")
    lead(f, (148, oy + 78), (cx + 28, cy + 20))
    f.text(152, oy + 124, "centrioles move apart")
    lead(f, (148, oy + 120), (cx + 54, cy + 4))


def metaphase(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    ys = [-27, -9, 9, 27]
    for y, (L, c) in zip(ys, [(26, "c1"), (18, "c2"), (18, "c2"), (26, "c1")]):
        xchrom(f, cx, cy + y, L, c + " sw3", 0, 22)
        for px in (cx - 52, cx + 52):
            f.line([(px, cy), (cx + (-3 if px < cx else 3), cy + y)], "ln-m thin", check=False)
    centriole(f, cx - 52, cy)
    centriole(f, cx + 52, cy)
    panel_title(f, oy, "2  Metaphase")
    f.text(152, oy + 50, "chromosomes line up")
    f.text(152, oy + 64, "on the equator")
    lead(f, (148, oy + 46), (cx + 8, cy - 26))
    f.text(152, oy + 96, "spindle fibres attach")
    f.text(152, oy + 110, "to the centromeres")
    lead(f, (148, oy + 92), (cx + 30, cy + 2))


def anaphase(f, oy):
    cx, cy = 72, oy + 76
    cell(f, oy)
    ys = [-27, -9, 9, 27]
    for y, (L, c) in zip(ys, [(22, "c1"), (15, "c2"), (15, "c2"), (22, "c1")]):
        for side, off in (("left", -24), ("right", 24)):
            px = cx + off
            vchrom(f, px, cy + y, L, c + " sw3", side)
            pole = cx - 52 if side == "left" else cx + 52
            f.line([(pole, cy), (px, cy + y)], "ln-m thin", check=False)
    centriole(f, cx - 52, cy)
    centriole(f, cx + 52, cy)
    panel_title(f, oy, "3  Anaphase")
    f.text(152, oy + 50, "centromeres divide")
    lead(f, (148, oy + 46), (cx + 24, cy - 28))
    f.text(152, oy + 82, "chromatids pulled")
    f.text(152, oy + 96, "to opposite poles")
    lead(f, (148, oy + 78), (cx + 30, cy + 10))
    f.text(152, oy + 124, "spindle fibres shorten")
    lead(f, (148, oy + 120), (cx + 44, cy + 2))


def telophase(f, oy):
    cx, cy = 72, oy + 76
    pts = []
    for k in range(61):
        t = 2 * math.pi * k / 60
        x = 66 * math.cos(t)
        y = 54 * math.sin(t) * (1 - 0.3 * math.exp(-(x / 14) ** 2))
        pts.append((round(cx + x, 1), round(cy + y, 1)))
    f.poly(pts[:-1], CELL)
    for side in (-1, 1):
        nx = cx + side * 34
        ellipse(f, nx, cy, 19, 19, "ln")
        for (dy, L, c) in [(-9, 16, "c1"), (-3, 11, "c2"), (4, 11, "c2"), (10, 16, "c1")]:
            f.line([(nx - L / 2, cy + dy), (nx + L / 2, cy + dy)], c + " sw2", check=False)
    panel_title(f, oy, "4  Telophase")
    f.text(152, oy + 50, "nuclear envelopes")
    f.text(152, oy + 64, "re-form")
    lead(f, (148, oy + 46), (cx + 50, cy - 8))
    f.text(152, oy + 96, "chromosomes uncoil")
    lead(f, (148, oy + 92), (cx + 36, cy + 8))
    f.text(152, oy + 124, "cell starts to divide")
    lead(f, (148, oy + 120), (cx + 2, cy + 30))


for name, fn_a, fn_b, label, caption in [
    ("stages1", prophase, metaphase,
     "Two stages of mitosis in an animal cell with four chromosomes. Prophase: chromosomes condense, the nuclear envelope "
     "breaks down and the centrioles move to opposite poles. Metaphase: the chromosomes line up on the equator, each "
     "attached to spindle fibres by its centromere.",
     "Prophase and metaphase (drawings of an animal cell with four chromosomes). The two longer chromosomes are one "
     "pair, the two shorter ones another. In metaphase fibres from both poles are attached to the centromeres."),
    ("stages2", anaphase, telophase,
     "Two stages of mitosis in an animal cell with four chromosomes. Anaphase: the centromeres divide and the chromatids "
     "are pulled to opposite poles by the shortening spindle fibres. Telophase: a nuclear envelope re-forms around each "
     "group of chromosomes, the chromosomes uncoil and the cell starts to pinch in two.",
     "Anaphase and telophase. In anaphase each chromatid is now a chromosome, so the cell briefly has eight. In "
     "telophase there are two groups of four.")]:
    f = Fig(name)
    fn_a(f, 0)
    fn_b(f, PH)
    figs.append(f.svg((330, 2 * PH), label, caption))
    problems.extend(f.check())

# ---------- Figure 5: cytokinesis, animal v plant (small) ----------
f = Fig("cytokinesis")
f.text(10, 18, "Animal cell: cleavage furrow", "tl tb")
cx, cy = 100, 82
pts = []
for k in range(61):
    t = 2 * math.pi * k / 60
    x = 84 * math.cos(t)
    y = 44 * math.sin(t) * (1 - 0.55 * math.exp(-(x / 16) ** 2))
    pts.append((round(cx + x, 1), round(cy + y, 1)))
f.poly(pts[:-1], CELL)
for nx in (cx - 44, cx + 44):
    ellipse(f, nx, cy, 15, 15, "ln")
f.poly([(cx - 4, cy - 31), (cx + 4, cy - 31), (cx + 4, cy - 23), (cx - 4, cy - 23)], "fi", check=False)
f.poly([(cx - 4, cy + 23), (cx + 4, cy + 23), (cx + 4, cy + 31), (cx - 4, cy + 31)], "fi", check=False)
f.text(196, 62, "cleavage furrow:")
f.text(196, 76, "membrane pulled in")
f.text(196, 90, "by protein rings")
lead(f, (192, 70), (cx + 5, cy - 26))
f.text(10, 158, "Plant cell: cell plate", "tl tb")
x0, y0, x1, y1 = 20, 176, 180, 246
f.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], "fp ln sw2", check=True)
f.line([(100, y0 + 4), (100, y1 - 4)], "c2 sw3 dash", check=False)
for vy in range(y0 + 14, y1 - 8, 12):
    f.parts.append(f'<circle class="f2 s-acc2 sw2" cx="100" cy="{vy}" r="3"/>')
for nx in (60, 140):
    ellipse(f, nx, (y0 + y1) / 2, 15, 15, "ln")
f.text(190, 196, "Golgi vesicles fuse")
f.text(190, 210, "to make the cell")
f.text(190, 224, "plate, which grows")
f.text(190, 238, "out to the wall")
lead(f, (186, 192), (105, 192))
figs.append(f.svg((330, 262),
    "Two cell divisions compared. Top: an animal cell in cytokinesis, pinched in the middle by a cleavage furrow between two "
    "nuclei. Bottom: a plant cell with a cell plate, built from fused vesicles, growing across the middle between two nuclei.",
    "Cytokinesis (drawings). An animal cell is pinched in two from the outside. A plant cell cannot pinch, because of its "
    "cell wall, so it builds a new wall and membranes across the middle from vesicles."))
problems.extend(f.check())

# ---------- Figure 6: five plant cells to identify (A-E) ----------
f = Fig("five")
W_, H_ = 96, 76
slots = {"A": (10, 28), "B": (118, 28), "C": (226, 28), "D": (64, 140), "E": (172, 140)}


def box(f, key):
    x, y = slots[key]
    f.poly([(x, y), (x + W_, y), (x + W_, y + H_), (x, y + H_)], "fp ln sw2")
    f.text(x + 2, y - 8, key, "tl tb")
    return x + W_ / 2, y + H_ / 2


# A: metaphase
cx, cy = box(f, "A")
for k, y in enumerate((-24, -8, 8, 24)):
    xchrom(f, cx, cy + y, 20 if k in (0, 3) else 14, ("c1" if k in (0, 3) else "c2") + " sw3", 0, 22)
# B: interphase
cx, cy = box(f, "B")
ellipse(f, cx, cy, 24, 24, "ln", check=False)
f.parts.append(f'<circle class="f2 s-acc2 sw2" cx="{cx + 6:g}" cy="{cy - 4:g}" r="5"/>')
for (dx, dy) in [(-12, -10), (-6, 10), (10, 12), (-14, 4), (14, -12), (0, -16)]:
    f.parts.append(f'<circle class="c1" cx="{cx + dx:g}" cy="{cy + dy:g}" r="1.2"/>')
# C: telophase with cell plate
cx, cy = box(f, "C")
f.line([(cx, cy - 34), (cx, cy + 34)], "c2 sw2 dash", check=False)
for side in (-1, 1):
    nx = cx + side * 26
    ellipse(f, nx, cy, 12, 16, "ln", check=False)
    for dy, L, c in [(-8, 12, "c1"), (-2, 9, "c2"), (4, 9, "c2"), (10, 12, "c1")]:
        f.line([(nx - L / 2, cy + dy), (nx + L / 2, cy + dy)], c + " sw2", check=False)
# D: anaphase
cx, cy = box(f, "D")
for y, (L, c) in zip((-24, -8, 8, 24), [(16, "c1"), (11, "c2"), (11, "c2"), (16, "c1")]):
    vchrom(f, cx - 22, cy + y, L, c + " sw2", "left", 28)
    vchrom(f, cx + 22, cy + y, L, c + " sw2", "right", 28)
# E: prophase
cx, cy = box(f, "E")
ellipse(f, cx, cy, 28, 28, "ln-m thin dash", check=False)
for (dx, dy, L, c, a) in [(-10, -12, 20, "c1", 25), (10, -6, 20, "c1", -35), (-8, 12, 14, "c2", 80), (12, 14, 14, "c2", 5)]:
    xchrom(f, cx + dx, cy + dy, L, c + " sw3", a)
figs.append(f.svg((330, 236),
    "Five drawings of plant cells in different stages of the mitotic cell cycle, labelled A to E, to be identified: "
    "A has chromosomes in a line across the middle; B has an intact nucleus with a nucleolus; C has two nuclei with a "
    "dashed line between them; D has two sets of V-shaped chromatids at opposite ends; E has condensed chromosomes in a "
    "nucleus whose envelope is dashed.",
    "Five cells from a root tip (drawings, not photographs), in a mixed-up order. Use them in the worked example."))
problems.extend(f.check())

for s in figs:
    print(s)
    print()
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
