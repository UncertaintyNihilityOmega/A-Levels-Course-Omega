# data/fig_bio.movement.py: hand-drawn SVG figures of chapters/bio.movement.md with a label-clearance check.
# Run: py data/fig_bio.movement.py > scratch/movement_figs.txt (figures on stdout, clearance report on stderr).
import sys, math
sys.path.insert(0, __file__.rsplit("data", 1)[0] + "data")
from figkit_p4 import Fig

figs, probs = [], []

# ---------- Figure 1: plant cell turgid / flaccid / plasmolysed ----------
f = Fig("plantcell")
PH = 104
panels = [("1  Turgid: wall pushed outwards", 148, 20, False),
          ("2  Flaccid: wall not stretched", 140, 24, False),
          ("3  Plasmolysed: membrane pulled away", 140, 24, True)]
for i, (title, w, x0, plasmo) in enumerate(panels):
    y0 = i * PH
    f.text(10, y0 + 16, title, "tl tb")
    wy, wh = y0 + 28, 66
    f.rect(x0, wy, w, wh, "fp ln sw3", 10)                      # cell wall
    if plasmo:
        f.rect(x0 + 18, wy + 12, w - 36, wh - 24, "f2 s-acc2 sw2", 8)    # shrunken cytoplasm and membrane
        f.rect(x0 + 30, wy + 22, w - 60, wh - 44, "fp ln", 6)           # vacuole
    else:
        f.rect(x0 + 3, wy + 3, w - 6, wh - 6, "f2 s-acc2 sw2", 8)       # cytoplasm and membrane against the wall
        if i == 0: f.rect(x0 + 16, wy + 14, w - 32, wh - 28, "fp ln", 6)   # vacuole, large (turgid)
        else: f.rect(x0 + 26, wy + 20, w - 52, wh - 40, "fp ln", 6)        # vacuole, smaller (flaccid; review 2026-10-28)
panels_x = 172
# labels, panel 1
f.text(panels_x + 10, 52, "cell wall", "tl")
f.leader((panels_x + 6, 49), (20 + 148 - 2, 49))
f.text(panels_x + 10, 72, "vacuole", "tl")
f.leader((panels_x + 6, 69), (20 + 120, 69))             # ends inside the vacuole (review P4/P5/P7)
# labels, panel 2
f.text(panels_x + 10, PH + 60, "membrane", "tl")
f.text(panels_x + 10, PH + 74, "touches the wall", "tl")
f.leader((panels_x + 6, PH + 57), (24 + 138, PH + 57))
# labels, panel 3
f.text(panels_x + 10, 2 * PH + 48, "gap filled with", "tl")
f.text(panels_x + 10, 2 * PH + 62, "external solution", "tl")
f.leader((panels_x + 6, 2 * PH + 51), (24 + 134, 2 * PH + 51))
f.text(panels_x + 4, 2 * PH + 92, "cell surface membrane", "tl")
f.leader((panels_x + 1, 2 * PH + 89), (24 + 104, 2 * PH + 82))   # ends on the membrane, not in the gap (review)
figs.append(f.svg((330, 3 * PH - 4),
    "Plant cells in three states. 1: turgid, the cell surface membrane presses against a stretched cell wall. 2: flaccid, "
    "the membrane just touches the wall, which is not stretched. 3: plasmolysed, the membrane and cytoplasm have shrunk "
    "and pulled away from the wall, leaving a gap filled with the external solution. Labels name the cell wall, vacuole, "
    "membrane, the gap and the cell surface membrane.",
    "Plant cells in solutions of different water potential. In pure water the cell takes in water and becomes turgid; with "
    "no net movement it is flaccid; in a solution with a lower water potential than the cell it loses water and the "
    "membrane pulls away from the wall (plasmolysis)."))
probs += f.check()

# ---------- Figure 2: red blood cells ----------
g = Fig("rbc")
RH = 100


def star(cx, cy, r1, r2, n=16):
    return [(round(cx + (r1 if k % 2 == 0 else r2) * math.cos(k * math.pi / n), 1),
             round(cy + (r1 if k % 2 == 0 else r2) * math.sin(k * math.pi / n), 1)) for k in range(2 * n)]


rows = [("1  In a concentrated solution", "crenated"), ("2  In a solution of equal ψ", "normal"),
        ("3  In pure water", "burst")]
for i, (title, kind) in enumerate(rows):
    y0 = i * RH
    g.text(10, y0 + 16, title, "tl tb")
    cx, cy = 62, y0 + 62
    if kind == "crenated":
        g.poly(star(cx, cy, 25, 20, 14), "f1 s-acc sw2")
    elif kind == "normal":
        g.circle(cx, cy, 25, "f1 s-acc sw2")
        g.circle(cx, cy, 10, "fp ln")
    else:
        for a0 in (10, 130, 250):
            pts = [(round(cx + 28 * math.cos(math.radians(a)), 1), round(cy + 28 * math.sin(math.radians(a)), 1))
                   for a in range(a0, a0 + 91, 15)]
            g.line(pts, "c1 sw3")
for (y, a, b) in [(RH * 0 + 52, "water leaves by osmosis;", "cell shrinks (crenated)"),
                  (RH * 1 + 52, "no net movement of", "water; normal shape"),
                  (RH * 2 + 52, "water enters by osmosis;", "cell bursts (lysis)")]:
    g.text(124, y, a, "tl")
    g.text(124, y + 16, b, "tl")
figs.append(g.svg((330, 3 * RH - 6),
    "Animal (red blood) cells in three solutions. 1: in a concentrated solution, water leaves by osmosis and the cell "
    "shrinks with a spiky outline (crenated). 2: in a solution with the same water potential as the cell there is no net "
    "movement of water and the cell keeps its normal shape. 3: in pure water, water enters by osmosis and the cell "
    "membrane bursts (lysis), drawn as a broken ring.",
    "Red blood cells have no cell wall, so they cannot resist water entering. In pure water the membrane is stretched until "
    "it bursts (lysis); in a concentrated solution the cell shrinks and its surface becomes crinkled (crenation)."))
probs += g.check()

# ---------- Figure 3: active transport by a carrier protein ----------
h = Fig("active")
AH = 118
titles = ["1  Ion and ATP bind to the carrier", "2  ATP hydrolysed; carrier changes shape",
          "3  Ion is released; carrier returns"]
OPEN_TOP = [(150, 40), (166, 40), (174, 58), (182, 40), (198, 40), (198, 82), (150, 82)]
OPEN_BOT = [(150, 40), (198, 40), (198, 82), (182, 82), (174, 64), (166, 82), (150, 82)]
for i in range(3):
    y0 = i * AH
    h.text(10, y0 + 14, titles[i], "tl tb")
    h.rect(10, y0 + 44, 310, 30, "fm s-acc sw2", 4)                       # membrane
    h.poly([(x, y + y0) for x, y in (OPEN_TOP if i != 1 else OPEN_BOT)], "f1 s-acc sw2")
    h.circle(137, y0 + 30, 4.5, "f3 s-acc2 sw2")                           # an ion outside (few)
    if i == 0:
        h.circle(174, y0 + 50, 4.5, "f3 s-acc2 sw2")                      # ion bound
        lab = "ATP"
    elif i == 1:
        h.circle(174, y0 + 70, 4.5, "f3 s-acc2 sw2")
        lab = "ATP → ADP + Pi"
    else:
        h.circle(174, y0 + 96, 4.5, "f3 s-acc2 sw2")
        lab = "ADP + Pi leave"
    h.text(214, y0 + 100, lab, "tl")
    h.leader((210, y0 + 97), (192, y0 + 84))
    for k in range(5):
        h.circle(24 + 20 * k, y0 + 90, 4.5, "f3 s-acc2 sw2")                # many ions inside
h.text(10, 36, "few ions outside", "tl")
h.text(10, 112, "many ions inside", "tl")
figs.append(h.svg((330, 3 * AH - 4),
    "Active transport in three stages. 1: an ion from the outside, where there are few ions, binds to a carrier protein "
    "and ATP binds too. 2: ATP is hydrolysed to ADP and phosphate and the carrier changes shape, so the binding site opens "
    "to the inside. 3: the ion is released inside the cell, where there are already many ions, and the carrier returns to "
    "its first shape.",
    "Active transport moves an ion from low to high concentration, against its concentration gradient. The energy comes "
    "from the hydrolysis of ATP, which makes the carrier change shape."))
probs += h.check()

# ---------- Figure 4: Visking tubing set-up ----------
v = Fig("visking")
v.rect(20, 20, 130, 180, "fp ln sw2", 6)                                  # beaker
v.rect(22, 76, 126, 122, "f2 s-acc2 sw2")                                 # water
v.rect(60, 44, 50, 128, "fp ln", 12)                                      # Visking bag
v.rect(63, 90, 44, 79, "f3 s-acc2 sw2", 10)                               # contents
v.line([(56, 52), (114, 52)], "ln sw3")                                   # thread tie
v.line([(56, 168), (114, 168)], "ln sw3")
v.text(162, 34, "thread tie", "tl")
v.leader((158, 31), (116, 50))
v.text(162, 70, "Visking tubing", "tl")
v.leader((158, 67), (111, 70))
v.text(162, 124, "water in beaker", "tl")
v.leader((158, 121), (130, 121))
v.text(162, 150, "starch + glucose", "tl")
v.text(162, 166, "solution inside", "tl")
v.leader((158, 147), (104, 147))
v.text(162, 192, "beaker", "tl")
v.leader((158, 189), (151, 189))
figs.append(v.svg((330, 214),
    "Visking tubing experiment: a beaker of water holds a bag of Visking tubing, tied at both ends with thread, filled with "
    "a starch and glucose solution. The bag hangs in the water with its tied top above the surface.",
    "Visking tubing is a partially permeable bag. After some time, samples of the water outside and of the solution "
    "inside are tested for glucose and starch."))
probs += v.check()

for s in figs:
    print(s)
    print()
print("\n".join(probs) if probs else "clearance ok", file=sys.stderr)
