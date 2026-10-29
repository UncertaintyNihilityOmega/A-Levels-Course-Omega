# data/fig_bio.biodiversity.py: figures of chapters/bio.biodiversity.md (random quadrat grid; belt transect up a shore; scatter graph for the Spearman example).
# Run: py data/fig_bio.biodiversity.py -> prints the <figure> lines (clearance report on stderr). py data/place_figs_p14.py bio.biodiversity places them.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["QUAD", "BELT", "SCAT"]

# ---------------------------------------------------------------- random quadrats on a 20 m x 20 m grid
q = Fig("quadrats")
PX0, PY0, S = 46, 30, 12          # plot origin (top-left) and px per metre
def qx(x): return PX0 + x * S
def qy(y): return PY0 + (20 - y) * S
for g in (0, 5, 10, 15, 20):
    q.line([(qx(g), qy(0)), (qx(g), qy(20))], "ln-m thin dash" if g not in (0,) else "ax")
    q.line([(qx(0), qy(g)), (qx(20), qy(g))], "ln-m thin dash" if g not in (0,) else "ax")
    q.text(qx(g), qy(0) + 16, str(g), "ts", "middle")
    q.text(PX0 - 8, qy(g) + 3, str(g), "ts", "end")
pts = [(3, 16), (11, 7), (17, 13), (6, 4), (14, 18)]
for i, (x, y) in enumerate(pts, 1):
    q.rect(qx(x) - 6, qy(y) - 6, 12, 12, "f1 s-acc sw2")
    if i == 5:
        q.text(qx(x) - 10, qy(y) + 4, str(i), "tl", "end")
    else:
        q.text(qx(x) + 12, qy(y) + 4, str(i), "tl")
q.text(qx(20), qy(0) + 34, "x / m", "tl", "end")
q.text(6, 14, "y / m", "tl")
H = qy(0) + 42
quad = q.svg((340, H),
    "A square grid 20 metres by 20 metres, with lines every 5 metres. Five small squares, numbered 1 to 5, mark the quadrats placed at random coordinates: 1 at x 3, y 16; 2 at x 11, y 7; 3 at x 17, y 13; 4 at x 6, y 4; 5 at x 14, y 18.",
    "Random sampling in a 20 m by 20 m area. Pairs of random numbers give an x and a y coordinate, and a quadrat (small square) is placed at each. The numbers show the order: (3, 16), (11, 7), (17, 13), (6, 4) and (14, 18).",
    "fig small")

# ---------------------------------------------------------------- belt transect up a shore
b = Fig("belt")
def ground(x): return 130 - (x - 70) * (80 / 260)
b.rect(10, 130, 60, 35, "f2 s-acc2 sw2")
b.text(40, 152, "sea", "tl", "middle")
b.poly([(70, 130), (330, 50), (330, 165), (70, 165)], "fm s-acc sw2")
b.line([(70, 130), (330, 50)], "ln-m thin dash", check=False)
for i, x in enumerate((100, 150, 200, 250, 300), 1):
    y = ground(x)
    b.rect(x - 7, y - 7, 14, 14, "f1 s-acc sw2")
    b.text(x, y - 15, str(i), "tl", "middle")
b.line([(70, 184), (326, 184)], "ln", arrow="ah")
b.text(70, 202, "increasing distance from the sea", "tl")
belt = b.svg((340, 214),
    "A side view of a shore. On the left is the sea, and to the right the land rises steadily. A dashed tape measure runs up the slope from the sea, and five numbered squares, 1 to 5, are quadrats placed at equal intervals along it. An arrow underneath points to the right and is labelled increasing distance from the sea.",
    "A belt transect up a shore. A tape measure runs up the slope, and a quadrat is placed at each regular interval (squares 1 to 5). Each quadrat records the species and a measurement of an abiotic factor, so the change along the gradient can be seen.",
    "fig small")

# ---------------------------------------------------------------- scatter graph (Spearman example)
s = Fig("scatter")
L, R, T, B = 48, 322, 26, 190
X0, X1, Y0, Y1 = 0, 18, 0, 16
def sx(v): return L + (v - X0) / (X1 - X0) * (R - L)
def sy(v): return B - (v - Y0) / (Y1 - Y0) * (B - T)
s.line([(L, T - 6), (L, B), (R + 4, B)], "ax")
for v in (0, 5, 10, 15):
    s.line([(sx(v), B), (sx(v), B + 4)], "ln", check=False)
    s.text(sx(v), B + 17, str(v), "ts", "middle")
for v in (0, 4, 8, 12, 16):
    s.line([(L - 4, sy(v)), (L, sy(v))], "ln", check=False)
    s.text(L - 8, sy(v) + 3, str(v), "ts", "end")
data = [(4, 2), (6, 5), (6, 3), (9, 8), (11, 7), (13, 12), (15, 14), (15, 10)]
for (x, y) in data:
    s.circle(sx(x), sy(y), 4.5, "f1 s-acc sw2")
s.text(R, B + 36, "soil water content / %", "tl", "end")
s.text(6, 12, "rushes per quadrat", "tl")
scat = s.svg((340, B + 46),
    "A scatter graph of the number of rushes per quadrat against soil water content in percent. Eight points rise from left to right: (4, 2), (6, 5), (6, 3), (9, 8), (11, 7), (13, 12), (15, 14) and (15, 10). The points show a positive relationship.",
    "The data for the Spearman example. The points rise from left to right: the number of rushes tends to be higher where the soil is wetter. The relationship is increasing, but not exactly a straight line, so a rank correlation is suitable.",
    "fig small")
print(quad)
print()
print(belt)
print()
print(scat)
print("\n".join(q.check() + b.check() + s.check()) or "clearance ok", file=sys.stderr)
