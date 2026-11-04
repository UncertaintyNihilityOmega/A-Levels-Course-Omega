# data/fig_bio.mock.p1.py: builds the three small SVG figures of Mock Paper 1 (Q4 bacterial cell drawing,
# Q21 mitosis stage, Q37 antibiotic disc plate) with label-clearance checks; the Q16 plot is a :::plot.
# Run: py data/fig_bio.mock.p1.py -> prints the <figure>s (paste into chapters/bio.mock.p1.md) and a clearance report.
import math, os, sys
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "fig_bio.mock.p2.py"), encoding="utf-8").read()
exec(src.split('\nf = Fig("plantcell")')[0])  # Fig, seg_box, ellipse helpers

# ---------------------------------------------------------------- Q4: cell with a loop of DNA, drawn from an EM
SCALE_PX_PER_UM = 48
f = Fig("cell")
f.vb = (340, 200)
ox = 30
cell_x, cell_y, cell_w, cell_h = 70 + ox, 60, 120, 64
f.rect(cell_x, cell_y, cell_w, cell_h, "fp ln sw3", rx=30)
loop = ellipse(125 + ox, 92, 20, 13, 20)
f.poly(loop, "c1 sw2")
for dx, dy in [(100, 72), (112, 112), (160, 72), (170, 95), (162, 114), (98, 96), (136, 114), (140, 74)]:
    f.circle(dx + ox, dy, 2.2, "f3 s-acc")
fl = [(190 + ox + k * 5, round(92 + 8 * math.sin(k * 0.55), 1)) for k in range(15)]
f.line(fl, "c2 sw2", check=False)
f.line([(125 + ox, 41), (125 + ox, 78)], "ln-m thin", check=False)
f.text(125 + ox, 36, "X", "tl tb", "middle")
f.line([(cell_x, 160), (cell_x + SCALE_PX_PER_UM, 160)], "ln sw2", check=False)
f.line([(cell_x, 155), (cell_x, 165)], "ln sw2", check=False)
f.line([(cell_x + SCALE_PX_PER_UM, 155), (cell_x + SCALE_PX_PER_UM, 165)], "ln sw2", check=False)
f.text(cell_x + SCALE_PX_PER_UM / 2, 183, "1 µm", "tl", "middle")
bad = f.check()
print("Q4:", "\n".join(bad) if bad else "clearance ok", "| cell length um =", cell_w / SCALE_PX_PER_UM)
lab4 = ("A drawing from an electron micrograph of a small rod-shaped cell with a thick outer wall. Inside, a ring-shaped "
        "structure labelled X lies in the cytoplasm among many small dots, and a long wavy filament extends from one end. "
        "A scale bar below the cell is labelled 1 µm.")
print(f.svg(f.vb, lab4, "A cell drawn from an electron micrograph. The scale bar is 1 µm."))
print()

# ---------------------------------------------------------------- Q21: a cell during mitosis
f = Fig("mitosis")
f.vb = (340, 230)
f.poly(ellipse(170, 115, 125, 85, 24), "fp ln sw2")
poles = [(62, 115), (278, 115)]
ys = [64, 97, 133, 166]
for cy in ys:
    for px, py in poles:
        f.line([(px, py), (170 + (-4 if px < 170 else 4), cy)], "ln-m thin", check=False)
for cy in ys:
    f.line([(163, cy - 11), (177, cy + 11)], "c1 sw3", check=False)
    f.line([(177, cy - 11), (163, cy + 11)], "c1 sw3", check=False)
for px, py in poles:
    f.circle(px, py, 4, "f2 s-acc sw2")
lab21 = ("A drawing of one cell during mitosis with no nuclear envelope. Four chromosomes, each X-shaped and made of two "
         "joined chromatids, are arranged in a single row across the middle of the cell. Thin fibres run from a point at each "
         "end of the cell to the joined region of every chromosome.")
print(f.svg(f.vb, lab21, "A cell during mitosis (diagrammatic)."))
print()

# ---------------------------------------------------------------- Q37: antibiotic discs on an agar plate
PX_PER_MM = 2
f = Fig("plate")
f.vb = (340, 240)
cx, cy, R = 170, 120, 90
f.circle(cx, cy, R, "f1 s-acc sw2")
discs = {"W": (-31, -31, 30), "X": (31, -31, 18), "Y": (-31, 31, 12), "Z": (31, 31, 0)}
for name, (dx, dy, zr) in discs.items():
    if zr:
        f.circle(cx + dx, cy + dy, zr, "fp ln")
for name, (dx, dy, zr) in discs.items():
    f.circle(cx + dx, cy + dy, 6, "f3 s-acc sw2")
pos = {"W": (50, 40), "X": (290, 40), "Y": (50, 214), "Z": (290, 214)}
for name, (lx, ly) in pos.items():
    dx, dy, zr = discs[name]
    f.text(lx, ly, name, "tl tb", "middle")
    sx = lx + (10 if lx < cx else -10)
    sy = ly - 4 if ly > cy else ly + 2
    f.line([(sx, sy), (cx + dx + (-6 if lx < cx else 6) * 0.7, cy + dy + (-6 if ly < cy else 6) * 0.7)], "ln-m thin", check=False)
bad = f.check()
print("Q37:", "\n".join(bad) if bad else "clearance ok")
for name, (dx, dy, zr) in discs.items():
    print(f"  {name}: zone diameter {2 * zr / PX_PER_MM:g} mm")
lab37 = ("A circular agar plate covered with bacteria and four small paper discs labelled W, X, Y and Z, one in each quarter. "
         "Around disc W is a large clear circle, around X a smaller clear circle and around Y a very small clear ring. "
         "Around Z there is no clear area.")
print(f.svg(f.vb, lab37, "A plate seen from above after incubation."))
