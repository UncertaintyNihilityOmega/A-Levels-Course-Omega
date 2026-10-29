# data/fig_bio.selection.py: builds the hand-drawn SVG figure of chapters/bio.selection.md (three kinds of selection) and checks label clearance.
# Run: py data/fig_bio.selection.py -> prints the <figure> (clearance report on stderr). data/place_figs_p14.py bio.selection places it.
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["SEL"]
X0, X1 = 44, 320            # x axis from 44 to 320
W = X1 - X0
PH = 160                    # height of one panel


def bell(mu, sd, peak, n=64):
    return lambda u: peak * math.exp(-((u - mu) / sd) ** 2 / 2)


def curve(fn, base, n=70):
    return [(round(X0 + W * i / n, 1), round(base - fn(i / n), 1)) for i in range(n + 1)]


f = Fig("selection")
OYS = [0, PH, 2 * PH]
# area-preserving curves (same area under before and after)
before_peak = 44
panels = [
    ("A  Stabilising selection", bell(0.5, 0.15, before_peak), bell(0.5, 0.15 * 0.6, before_peak / 0.6),
     "both extremes selected against"),
    ("B  Directional selection", bell(0.4, 0.14, before_peak), bell(0.6, 0.14, before_peak),
     "one extreme selected against"),
    ("C  Disruptive selection", bell(0.5, 0.14, before_peak),
     lambda u: bell(0.3, 0.09, before_peak * 0.14 / 0.09 / 2)(u) + bell(0.7, 0.09, before_peak * 0.14 / 0.09 / 2)(u),
     "intermediates selected against"),
]
for k, (title, fb, fa, note) in enumerate(panels):
    oy = OYS[k]
    base = oy + 134
    f.text(10, oy + 16, title, "tl tb")
    f.text(4, oy + 34, "frequency", "tl")
    f.line([(X0, oy + 44), (X0, base), (X1 + 6, base)], "ax")
    f.text(X1 + 4, base + 16, "phenotype", "tl", "end")
    f.line(curve(fb, base), "c2 dash sw2")
    f.line(curve(fa, base), "c1 sw2")
    f.text(X1, oy + 34, note, "tl", "end")
    if k == 1:
        mb, ma = X0 + W * 0.4, X0 + W * 0.6
        f.line([(mb, oy + 52), (ma - 12, oy + 52)], "ln", arrow="ah")
        f.text(ma - 2, oy + 56, "mean", "tl")
# legend
ly = 3 * PH + 14
f.line([(10, ly - 4), (40, ly - 4)], "c2 dash sw2", check=False)
f.text(48, ly, "before selection", "tl")
f.line([(176, ly - 4), (206, ly - 4)], "c1 sw2", check=False)
f.text(214, ly, "after selection", "tl")
fig = f.svg((340, 3 * PH + 28),
    "Three graphs of frequency against phenotype, each with a dashed bell-shaped curve before selection and a solid curve after selection. A, stabilising selection: both extremes are selected against, and the curve after selection is taller and narrower around the same mean. B, directional selection: one extreme is selected against, and the curve after selection has moved to the right, with an arrow showing the mean moving. C, disruptive selection: the intermediate phenotypes are selected against, and the curve after selection has two peaks, one on each side of the original mean.",
    "Three types of selection on a characteristic that varies continuously. The dashed curve is the distribution before selection and the solid curve is the distribution after selection. In A the mean stays the same and the spread falls; in B the mean moves; in C two peaks form.",
    "fig small")
print(fig)
print("\n".join(f.check()) or "clearance ok", file=sys.stderr)
