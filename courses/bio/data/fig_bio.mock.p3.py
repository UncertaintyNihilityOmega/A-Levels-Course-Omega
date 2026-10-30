# data/fig_bio.mock.p3.py: hand-drawn SVG for chapters/bio.mock.p3.md (Mock Paper 3).
# Fig 1: slide S1 (root TS, low power, with an eyepiece graticule scale); Fig 2: photomicrograph P (root cortex,
# high power, line XY, scale bar); Fig 3: photomicrograph of stem TS (S2); Fig 4: carrot graph with best-fit line.
# Run: py data/fig_bio.mock.p3.py -> clearance report and the geometry used by checks/bio.mock.p3.py.
# data/place_figs_p24.py pastes the figures into the chapter (only the text after <!--FIG:name--> changes).
import math, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib_p19 import Fig, ellipse
import calc_p24 as C

sys.stdout.reconfigure(encoding="utf-8")

# ---- geometry shared with the check ----
PX = 6                      # px per graticule division in Fig 1
S1_CX, S1_CY, S1_R, S1_ENDO = 170, 140, 120, 48
SCALE_X0, SCALE_Y = 20, 292
SCALE_BAR_PX, XY_PX = 40, 56  # Fig 2: 50 um bar (40 px) and line XY (56 px)


def div(x):
    return (x - SCALE_X0) / PX


def fig1(problems):
    f = Fig("S1")
    cx, cy, R = S1_CX, S1_CY, S1_R
    f.poly([(round(cx + R * math.cos(2 * math.pi * k / 72), 1), round(cy + R * math.sin(2 * math.pi * k / 72), 1))
            for k in range(72)], "fp ln sw2")
    for ring_r, n in [(109, 49), (96, 43), (83, 37), (70, 31), (57, 25)]:        # cortex cells
        for k in range(n):
            th = 2 * math.pi * k / n + (ring_r % 7) * 0.1
            f.parts.append(f'<circle class="ln-m thin" cx="{cx + ring_r * math.cos(th):.1f}" '
                           f'cy="{cy + ring_r * math.sin(th):.1f}" r="6"/>')
    f.parts.append(f'<circle class="fp ln sw2" cx="{cx}" cy="{cy}" r="{S1_ENDO}"/>')        # endodermis
    f.parts.append(f'<circle class="ln-m thin" cx="{cx}" cy="{cy}" r="{S1_ENDO - 4}"/>')
    arm, wd = 34, 6
    cross = []
    for th in (0, 90, 180, 270):
        c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
        for (u, v) in ((wd, -wd), (arm, -wd), (arm, wd), (wd, wd)):
            cross.append((round(cx + u * c - v * s, 1), round(cy + u * s + v * c, 1)))
    # order points so the polygon is a plus sign
    pts = []
    for q in range(4):
        th = math.radians(90 * q)
        c, s = math.cos(th), math.sin(th)
        for (u, v) in ((wd, -wd), (arm, -wd), (arm, wd), (wd, wd)):
            pts.append((round(cx + u * c - v * s, 1), round(cy + u * s + v * c, 1)))
    f.poly(pts, "fm s-acc sw2", check=False)
    for th in (45, 135, 225, 315):                                            # phloem between the arms
        t = math.radians(th)
        f.poly(ellipse(cx + 27 * math.cos(t), cy + 27 * math.sin(t), 8, 5, 16, t + math.pi / 2), "fm2 s-acc sw2",
               check=False)
    # graticule strip: 50 divisions
    y = SCALE_Y
    f.line([(SCALE_X0, y), (SCALE_X0 + 50 * PX, y)], "ln", check=False)
    for d in range(51):
        h = 9 if d % 10 == 0 else (6 if d % 5 == 0 else 3)
        f.line([(SCALE_X0 + d * PX, y), (SCALE_X0 + d * PX, y - h)], "ln", check=False)
    for d in range(0, 51, 10):
        f.text(SCALE_X0 + d * PX, y + 15, str(d), "ts", "middle")
    f.text(170, y + 30, "eyepiece graticule divisions", "tl", "middle")
    # dashed lines from the edges and the endodermis down to the scale
    for name, x, anchor, dx in (("A", cx - R, "end", -5), ("C", cx - S1_ENDO, "end", -5),
                                ("D", cx + S1_ENDO, "start", 5), ("B", cx + R, "start", 5)):
        f.line([(x, cy), (x, y - 12)], "ln-m thin dash", check=False)
        f.text(x + dx, y - 26, name, "tl tb", anchor)
    f.text(10, 16, "Slide S1", "tl tb")
    label = ("Slide S1, a transverse section seen with the x10 objective. A large circular section with a wide cortex of "
             "round cells, a ring (the endodermis) around a central core, and in the core a plus-shaped group of "
             "xylem with four small groups of phloem between its arms. Below it a graticule scale from 0 to 50. Dashed "
             "lines from the outer edge (A and B) and from the ring (C and D) meet the scale.")
    cap = ("Fig. 2.1 Slide S1, drawn as it would look through the microscope (a drawing, not a photograph). A and B mark the "
           "outer edge of the section; C and D mark the ring around the central tissue.")
    f.vb = (340, 334)
    problems += f.check()
    return f.svg((340, 334), label, cap)


def fig2(problems):
    f = Fig("P")
    R = 56 / (2 * math.cos(math.radians(30)))
    rowh = 1.5 * R
    cells = {}
    rnd = random.Random(11)
    for r in range(5):
        for c in range(5 if r % 2 == 0 else 4):
            cx = 30 + 56 * c + (0 if r % 2 == 0 else 28)
            cy = 56 + rowh * r
            cells[(r, c)] = (cx, cy)
    for (r, c), (cx, cy) in cells.items():
        pts = [(round(cx + R * math.cos(math.radians(30 + 60 * k)), 1), round(cy + R * math.sin(math.radians(30 + 60 * k)), 1))
               for k in range(6)]
        f.poly(pts, "fp ln", check=False)
    for (r, c), (cx, cy) in cells.items():
        z = (r, c) == (2, 2)
        nx, ny = cx + rnd.uniform(-9, 9), cy + (-13 if z else rnd.uniform(-12, 8))
        f.parts.append(f'<circle class="f2 s-acc2 sw2" cx="{nx:.1f}" cy="{ny:.1f}" r="6"/>')
        for g in range(rnd.choice([2, 3, 3, 4])):
            gx = cx + rnd.uniform(-18, 18)
            gy = cy + rnd.uniform(8, 19) if z else cy + rnd.uniform(-4, 20)
            if math.hypot(gx - nx, gy - ny) < 12:
                continue
            f.parts.append(f'<ellipse class="fm2 s-acc sw2" cx="{gx:.1f}" cy="{gy:.1f}" rx="5" ry="3.4"/>')
    # dashed box round the two cells (1,1) and (1,2)... (row 1 has 4 cells): use (0,1) and (0,2)
    (x1, y1), (x2, y2) = cells[(0, 1)], cells[(0, 2)]
    f.parts.append(f'<rect class="c3 dash" x="{x1 - 30:.1f}" y="{y1 - 34:.1f}" width="{x2 - x1 + 60:.1f}" height="68" rx="3"/>')
    # line XY across cell Z
    zx, zy = cells[(2, 2)]
    f.line([(zx - 28, zy), (zx + 28, zy)], "c2 sw2", check=False)
    f.text(zx - 33, zy + 5, "X", "tl tb", "end")
    f.text(zx + 33, zy + 5, "Y", "tl tb", "start")
    # scale bar
    by = 324
    f.line([(30, by), (30 + SCALE_BAR_PX, by)], "ln sw2", check=False)
    f.line([(30, by - 5), (30, by + 5)], "ln", check=False)
    f.line([(30 + SCALE_BAR_PX, by - 5), (30 + SCALE_BAR_PX, by + 5)], "ln", check=False)
    f.text(30 + SCALE_BAR_PX + 12, by + 4, "50 µm", "tl")
    label = ("Photomicrograph P, a drawing of root cortex at high power: about twenty thin-walled six-sided cells packed "
             "together, each with a small dark nucleus and a few small oval starch grains. A dashed box surrounds two "
             "neighbouring cells at the top. A thick line XY crosses the widest part of one cell near the middle, and a "
             "scale bar at the bottom is labelled 50 micrometres.")
    cap = ("Fig. 2.2 Photomicrograph P (drawn). The dashed box holds two neighbouring cells. XY crosses cell Z. The scale bar "
           "represents 50 µm.")
    f.vb = (340, 338)
    problems += f.check()
    return f.svg((340, 338), label, cap)


def fig3(problems):
    f = Fig("S2")
    cx, cy, R = 170, 150, 125
    ring = lambda r, n=72: [(round(cx + r * math.cos(2 * math.pi * k / n), 1), round(cy + r * math.sin(2 * math.pi * k / n), 1))
                            for k in range(n)]
    f.poly(ring(R), "fp ln sw2", check=False)
    f.poly(ring(R - 6), "ln-m thin", closed=True, check=False)
    rnd = random.Random(2)
    for k in range(40):                                                       # cortex cells
        th = 2 * math.pi * k / 40
        f.parts.append(f'<circle class="ln-m thin" cx="{cx + 99 * math.cos(th):.1f}" cy="{cy + 99 * math.sin(th):.1f}" r="7"/>')
    for k in range(8):                                                        # bundles
        th = math.radians(22.5 + 45 * k)
        bx, by = cx + 70 * math.cos(th), cy + 70 * math.sin(th)
        f.poly(ellipse(bx, by, 17, 11, 20, th + math.pi / 2), "fm s-acc sw2", check=False)
        f.poly(ellipse(cx + 80 * math.cos(th), cy + 80 * math.sin(th), 7, 4.5, 14, th + math.pi / 2), "fm2 s-acc sw2", check=False)
    for gy in range(-3, 4):                                                   # large pith cells, packed
        for gx in range(-3, 4):
            x = gx * 24 + (12 if gy % 2 else 0)
            y = gy * 21
            if math.hypot(x, y) < 54:
                f.parts.append(f'<circle class="ln-m thin" cx="{cx + x:.1f}" cy="{cy + y:.1f}" r="11"/>')
    f.text(10, 16, "Photomicrograph S2", "tl tb")
    label = ("Photomicrograph S2, a drawing of a transverse section of a different plant organ, seen at low power. A "
             "circular section with a narrow outer band of small cells, a ring of eight separate oval groups of "
             "vascular tissue, and a wide central region of large rounded cells.")
    cap = "Fig. 2.3 Photomicrograph S2 (drawn), at the same low-power magnification as slide S1."
    f.vb = (340, 300)
    problems += f.check()
    return f.svg((340, 300), label, cap)


def fig4(problems):
    f = Fig("graph")
    X0, X1, Y0, Y1 = 52, 322, 24, 250             # plot area
    xmax, ymax, ymin = 0.60, 20.0, -25.0
    fx = lambda v: X0 + (v / xmax) * (X1 - X0)
    fy = lambda v: Y0 + (ymax - v) / (ymax - ymin) * (Y1 - Y0)
    for i in range(0, 13):
        v = i * 0.05
        f.line([(round(fx(v), 1), Y0), (round(fx(v), 1), Y1)], "gr", check=False)
    for j in range(0, 10):
        v = ymax - 5 * j
        f.line([(X0, round(fy(v), 1)), (X1, round(fy(v), 1))], "gr", check=False)
    f.line([(X0, Y0), (X0, Y1)], "ax", check=False)
    f.line([(X0, round(fy(0), 1)), (X1, round(fy(0), 1))], "ax", check=False)
    for i in range(0, 7):
        v = i * 0.1
        f.line([(round(fx(v), 1), Y1), (round(fx(v), 1), Y1 + 4)], "ax", check=False)
        f.text(round(fx(v), 1), Y1 + 16, f"{v:.1f}", "ts", "middle")
    for j in range(0, 10):
        v = ymax - 5 * j
        f.text(X0 - 6, round(fy(v), 1) + 3, ("−" if v < 0 else "") + str(int(abs(v))), "ts", "end")
    a, b = C.fit()
    a, b = round(a, 1), round(b, 1)
    f.line([(round(fx(0), 1), round(fy(a), 1)), (round(fx(0.5), 1), round(fy(a + b * 0.5), 1))], "c2 sw2", check=False)
    for c, p in zip(C.CONC, C.PC):
        x, y = fx(c), fy(p)
        f.line([(round(x - 4, 1), round(y - 4, 1)), (round(x + 4, 1), round(y + 4, 1))], "ln", check=False)
        f.line([(round(x - 4, 1), round(y + 4, 1)), (round(x + 4, 1), round(y - 4, 1))], "ln", check=False)
    f.text(10, 14, "change in mass / %", "tl")
    f.text(187, Y1 + 36, "concentration of sodium chloride / mol dm⁻³", "tl", "middle")
    label = ("Graph of the percentage change in mass of carrot cylinders against the concentration of sodium chloride "
             "solution from 0 to 0.60 mol dm-3. Six crosses fall on a falling straight line, from about +14 per cent at "
             "0.00 to about -19 per cent at 0.50, except the cross at 0.40, which is above the line. The line crosses "
             "zero change between 0.20 and 0.25.")
    cap = ("Fig. 1.1 Percentage change in mass against the concentration of sodium chloride solution, with the student's line of "
           "best fit.")
    f.vb = (340, 300)
    f.vb = (340, 300)
    problems += f.check()
    return f.svg((340, 300), label, cap), (a, b)


def figures():
    problems = []
    figs = {"s1": fig1(problems), "p": fig2(problems), "s2": fig3(problems)}
    g, line = fig4(problems)
    figs["graph"] = g
    return figs, problems, line


if __name__ == "__main__":
    figs, problems, line = figures()
    print("\n".join(problems) or "clearance ok")
    print("line", line, "A,B,C,D divisions:", div(S1_CX - S1_R), div(S1_CX + S1_R), div(S1_CX - S1_ENDO), div(S1_CX + S1_ENDO))
