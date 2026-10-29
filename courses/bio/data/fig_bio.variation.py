# data/fig_bio.variation.py: builds the hand-drawn SVG figure of chapters/bio.variation.md (bar chart v histogram) and checks label clearance.
# Run: py data/fig_bio.variation.py -> prints the <figure> (clearance report on stderr). data/place_figs_p14.py bio.variation places it.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["VAR"]
BLOOD = [("O", 84), ("A", 76), ("B", 28), ("AB", 12)]          # invented sample of 200 students
HEIGHT = [(150, 2), (155, 6), (160, 14), (165, 24), (170, 26), (175, 16), (180, 8), (185, 4)]   # invented sample of 100 students
assert sum(v for _, v in BLOOD) == 200 and sum(v for _, v in HEIGHT) == 100

f = Fig("variation")
# ---- panel A: bar chart
f.text(10, 16, "A  Discontinuous: blood group", "tl tb")
f.text(4, 32, "number of students", "tl")
base, k = 150, 0.96
f.line([(44, 50), (44, base), (326, base)], "ax", check=True)
for v in (0, 50, 100):
    y = base - v * k
    f.text(38, y + 4, str(v), "ts", "end")
    if v:
        f.line([(40, y), (44, y)], "ax", check=False)
for i, (g, v) in enumerate(BLOOD):
    x = 58 + 72 * i
    f.rect(x, base - v * k, 44, v * k, "f1 s-acc sw2")
    f.text(x + 22, base + 17, g, "tl", "middle")
f.text(185, base + 36, "blood group", "tl", "middle")

# ---- panel B: histogram
oy = 206
f.text(10, oy + 16, "B  Continuous: height of 100 students", "tl tb")
f.text(4, oy + 32, "number of students", "tl")
base2, k2 = oy + 168, 3.0
f.line([(44, oy + 48), (44, base2), (326, base2)], "ax")
for v in (0, 10, 20, 30):
    y = base2 - v * k2
    f.text(38, y + 4, str(v), "ts", "end")
    if v:
        f.line([(40, y), (44, y)], "ax", check=False)
w = 280 / len(HEIGHT)
for i, (lo, v) in enumerate(HEIGHT):
    x = 44 + w * i
    f.rect(x, base2 - v * k2, w, v * k2, "f1 s-acc sw2")
for i in range(len(HEIGHT) + 1):
    f.text(44 + w * i, base2 + 19, str(150 + 5 * i), "ts", "middle")
f.text(185, base2 + 40, "height / cm", "tl", "middle")

fig = f.svg((340, base2 + 50),
    "Two graphs. Graph A, a bar chart with gaps between the bars: the number of students in a sample of 200 with each blood group. O has 84, A has 76, B has 28 and AB has 12. Graph B, a histogram with touching bars: the heights of 100 students in 5 cm classes from 150 to 190 cm. The bars rise to a peak of 26 in the 170 to 175 cm class and fall away on each side in a bell shape.",
    "Invented class data. A: discontinuous variation is shown in a bar chart, with gaps because the groups are separate categories. B: continuous variation is shown in a histogram, with no gaps because height is a measurement on a scale; the bell shape is a normal distribution.")
print(fig)
print("\n".join(f.check()) or "clearance ok", file=sys.stderr)
