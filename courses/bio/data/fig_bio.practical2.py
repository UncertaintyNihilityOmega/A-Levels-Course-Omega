# data/fig_bio.practical2.py: hand-drawn SVG for chapters/bio.practical2.md
# (good v poor plan diagram, cell walls drawn with two and three lines, a counting grid).
# Run: py data/fig_bio.practical2.py -> prints the clearance report and the grid counts.
# data/place_figs_p19.py pastes the figures into the chapter.
import math, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib_p19 import Fig, lead_check, ellipse

sys.stdout.reconfigure(encoding="utf-8")
LEAD = "ln-m thin"


def circle_pts(cx, cy, r, n=48, wobble=0.0, seed=0):
    rnd = random.Random(seed)
    return [(round(cx + (r + rnd.uniform(-wobble, wobble)) * math.cos(2 * math.pi * k / n), 1),
             round(cy + (r + rnd.uniform(-wobble, wobble)) * math.sin(2 * math.pi * k / n), 1)) for k in range(n)]


# ---------------------------------------------------------------------------------------------------------
# Grid of cells: the counts are used by checks/bio.practical2.py
GRID_N, GRID_S, GRID_X, GRID_Y = 6, 48, 26, 12
SAMPLED = {"A": (0, 2), "B": (2, 4), "C": (3, 1), "D": (5, 3)}   # (row, column)


def grid_dots():
    rnd = random.Random(8)
    dots = []
    for r in range(GRID_N):
        for c in range(GRID_N):
            k = rnd.choice([4, 5, 5, 6, 6, 6, 7, 7])
            x0, y0 = GRID_X + c * GRID_S, GRID_Y + r * GRID_S
            got = []
            while len(got) < k:
                x, y = rnd.uniform(x0 + 6, x0 + GRID_S - 6), rnd.uniform(y0 + 6, y0 + GRID_S - 6)
                if any(math.hypot(x - a, y - b) < 10 for a, b in got):
                    continue
                if (r, c) in SAMPLED.values() and x < x0 + 18 and y < y0 + 21:
                    continue                      # keep the corner clear for the square's letter
                got.append((x, y))
            dots.append(((r, c), got))
    return dots


def grid_counts():
    d = dict(grid_dots())
    return {name: len(d[rc]) for name, rc in SAMPLED.items()}, sum(len(v) for v in d.values())


def figures():
    figs, problems = {}, []

    # ----- Figure 1: good v poor plan diagram of a stem TS -------------------------------------------------
    f = Fig("plan")
    f.text(10, 16, "A  Good plan diagram", "tl tb")
    cx, cy, R = 105, 130, 80
    f.poly(circle_pts(cx, cy, R), "fp ln", check=False)
    bund = []
    for k in range(8):
        th = math.radians(22.5 + 45 * k)
        bx, by = cx + 52 * math.cos(th), cy + 52 * math.sin(th)
        pts = ellipse(bx, by, 11, 7, 20, th)
        f.poly(pts, "fp ln", check=False)
        bund.append((bx, by))
    f.text(cx, 232, "TS of a stem, low power", "tl", "middle")

    def lab(y, s, ex, ey):
        f.text(205, y + 4, s)
        f.line([(198, y), (ex, ey)], LEAD, check=False)
        problems.extend(lead_check(f, (198, y), (ex, ey), own=s))

    lab(70, "epidermis", cx + math.sqrt(R ** 2 - 60 ** 2), 70)
    lab(100, "cortex", cx + math.sqrt(70 ** 2 - 30 ** 2), 100)
    lab(130, "pith", cx + 8, 130)
    lab(156, "vascular bundle", bund[0][0] + 6, 156)

    # poor drawing
    oy = 262
    f.text(10, oy + 16, "B  Poor plan diagram", "tl tb")
    cx2, cy2 = 118, oy + 112
    f.poly(circle_pts(cx2, cy2, 54, 36, 2.2, 1), "ln", check=False)
    f.poly(circle_pts(cx2, cy2, 51, 36, 2.2, 2), "ln", check=False)
    rnd = random.Random(8)
    for k in range(16):                                     # cells drawn in the cortex
        th = 2 * math.pi * k / 16 + 0.1
        f.circle(round(cx2 + 43 * math.cos(th), 1), round(cy2 + 43 * math.sin(th), 1), 3.4, "fp ln thin")
    for k in range(6):                                      # bundles too big
        th = math.radians(10 + 60 * k)
        bx, by = cx2 + 25 * math.cos(th), cy2 + 25 * math.sin(th)
        f.poly(ellipse(bx, by, 11, 9, 16, th), "fm s-acc sw2", check=False)
    for k in range(-3, 4):                                  # shading in the pith
        f.line([(cx2 - 6, cy2 + 3 * k - 3), (cx2 + 6, cy2 + 3 * k + 3)], "ln-m thin", check=False)
    # labels with arrowheads that cross; one written on the drawing
    f.text(205, oy + 62, "epidermis")
    f.line([(200, oy + 58), (166, oy + 108)], "ln thin", arrow="ah", check=False)
    f.text(205, oy + 92, "cortex")
    f.line([(200, oy + 88), (156, oy + 78)], "ln thin", arrow="ah", check=False)
    f.text(205, oy + 142, "vascular bundle")
    f.line([(200, oy + 138), (146, oy + 128)], "ln thin", arrow="ah", check=False)
    f.text(cx2 - 5, cy2 + 24, "pith", "tl", "middle", )
    label = ("Two plan diagrams of a transverse section of a stem. A, the good drawing: a large circle for the outer edge "
             "with a ring of eight single-line outlines of vascular bundles, no cells, labelled epidermis, cortex, pith and "
             "vascular bundle with ruled lines that touch the structures. B, the poor drawing: small and off centre, "
             "with a doubled sketchy outline, a ring of cells drawn in the cortex, six bundles that are too large, "
             "hatched shading in the pith, and label lines with arrowheads that cross.")
    cap = ("A is a good plan diagram of a stem (a drawing of the structure, not a photograph). B has several faults "
           "for you to find.")
    figs["plan"] = f.svg((340, 440), label, cap)
    # (clearance for the poor panel's labels is not checked: they are meant to be poor)
    f.boxes = [b for b in f.boxes if b[0] not in ("epidermis", "cortex", "vascular bundle", "pith") or b[2] < 250]
    problems += [p for p in f.check() if "B  Poor" not in p]

    # ----- Figure 2: cell drawing, two- and three-line walls -------------------------------------------------
    g = Fig("walls")
    X0, T, B = 100, 40, 170
    g.rect(X0, T, 220, B - T, "fp ln")                              # outer face
    g.rect(X0 + 8, T + 8, 94, B - T - 16, "fp ln")                  # inner face, cell 1
    g.rect(X0 + 118, T + 8, 94, B - T - 16, "fp ln")                # inner face, cell 2
    g.line([(X0 + 110, T), (X0 + 110, B)], "ln", check=False)       # the middle line of the shared wall
    for off in (0, 110):
        g.rect(X0 + 20 + off, T + 16, 72, 74, "fm2 s-acc sw2")      # vacuole
        g.poly(ellipse(X0 + 55 + off, 146, 12, 9, 20), "f2 s-acc2 sw2")   # nucleus
    g.text(150, 22, "wall: two lines", "tl", "middle")
    g.line([(150, 26), (150, 44)], LEAD, check=False)
    problems += lead_check(g, (150, 26), (150, 44), own="wall: two lines")
    g.text(92, 88, "vacuole", "tl", "end")
    g.line([(96, 84), (150, 84)], LEAD, check=False)
    g.text(92, 124, "cytoplasm", "tl", "end")
    g.line([(96, 120), (114, 120)], LEAD, check=False)
    g.text(92, 154, "nucleus", "tl", "end")
    g.line([(96, 150), (146, 150)], LEAD, check=False)
    g.text(210, 196, "shared wall:", "tl", "middle")
    g.text(210, 210, "three lines", "tl", "middle")
    g.line([(210, 182), (210, 172)], LEAD, check=False)
    for a, b in [((96, 84), (150, 84)), ((96, 120), (114, 120)), ((96, 150), (146, 150))]:
        problems += lead_check(g, a, b)
    label2 = ("Drawing of two touching plant cells. The outer wall of each cell is drawn with two lines. The wall shared by "
              "the two cells is drawn with three lines, the middle one being the boundary between them. Each cell has a "
              "large vacuole, a thin layer of cytoplasm and a nucleus.")
    cap2 = ("Plant cell walls in a drawing. Draw a wall with two lines where a cell borders the outside, and with three "
            "lines where two cells touch. Only the structures that you can see are drawn.")
    figs["walls"] = g.svg((340, 218), label2, cap2)
    problems += g.check()

    # ----- Figure 3: counting grid ------------------------------------------------------------------------------
    h = Fig("grid")
    for r in range(GRID_N):
        for c in range(GRID_N):
            x0, y0 = GRID_X + c * GRID_S, GRID_Y + r * GRID_S
            cls = "fm s-acc sw2" if (r, c) in SAMPLED.values() else "fp ln thin"
            h.parts.append(f'<rect class="{cls}" x="{x0}" y="{y0}" width="{GRID_S}" height="{GRID_S}"/>')
    for name, (r, c) in SAMPLED.items():
        h.text(GRID_X + c * GRID_S + 5, GRID_Y + r * GRID_S + 15, name, "tl tb")
    for _, pts in grid_dots():
        for x, y in pts:
            h.circle(round(x, 1), round(y, 1), 3.2, "fi")
    h.text(170, 322, "A to D: the squares counted", "tl", "middle")
    label3 = ("A square grid of 6 by 6 equal squares over a field of cells shown as dots. Four squares, labelled A, B, C "
              "and D, are shaded: these are the squares in which the cells are counted.")
    cap3 = ("Estimating the number of cells by sampling. The cells in four of the 36 squares are counted, the mean per "
            "square is found, and it is multiplied by 36.")
    figs["grid"] = h.svg((340, 336), label3, cap3)
    problems += [p for p in h.check() if "overlap" in p or "leaves" in p]
    return figs, problems


if __name__ == "__main__":
    figs, problems = figures()
    print("\n".join(problems) or "clearance ok")
    print(grid_counts())
