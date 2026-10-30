# data/fig_p20.py: hand SVG figures for P20 (bio.stats, bio.planning, bio.evaluation) and the clearance check.
# Run: py data/fig_p20.py   -> replaces every line "@@FIG name@@" in the three chapters by its <figure>, prints the report.
import math, os, re, sys
from math import sqrt
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(os.path.dirname(HERE), "chapters")
CW = {"tl": 7.0, "ts": 6.2}


class Fig:
    def __init__(self, name, vb):
        self.name, self.vb, self.parts, self.segs, self.boxes = name, vb, [], [], []

    def line(self, pts, cls, arrow=None, check=True):
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts)
        m = f' marker-end="url(#{arrow})"' if arrow else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{m}/>')
        if check:
            self.segs += [(a, b, cls) for a, b in zip(pts, pts[1:])]

    def poly(self, pts, cls, closed=True):
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts) + ("Z" if closed else "")
        self.parts.append(f'<path class="{cls}" d="{d}"/>')
        ring = pts + ([pts[0]] if closed else [])
        self.segs += [(a, b, cls) for a, b in zip(ring, ring[1:])]

    def rect(self, x, y, w, h, cls):
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"/>')
        p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
        self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def circle(self, cx, cy, r, cls):
        self.parts.append(f'<circle class="{cls}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:g}"/>')

    def text(self, x, y, s, cls="tl", anchor="start"):
        kind = "ts" if "ts" in cls.split() else "tl"
        w = len(s) * CW[kind] * (1.06 if "tb" in cls.split() else 1)
        h_top, h_bot = (10, 3) if kind == "tl" else (9, 3)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        a = {"middle": ' text-anchor="middle"', "end": ' text-anchor="end"'}.get(anchor, "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}"{a}>{s}</text>')
        self.boxes.append((s, x0, y - h_top, x0 + w, y + h_bot))

    def svg(self, label, caption):
        return (f'<figure class="fig small"><svg viewBox="0 0 {self.vb[0]} {self.vb[1]}" role="img" aria-label="{label}">'
                + "".join(self.parts) + f'</svg><figcaption>{caption}</figcaption></figure>')

    def check(self, gap=4.0):
        bad = []
        for i, (s, x0, y0, x1, y1) in enumerate(self.boxes):
            if x0 < 2 or y0 < 2 or x1 > self.vb[0] - 2 or y1 > self.vb[1] - 2:
                bad.append(f"{self.name}: '{s}' leaves the viewBox ({x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f})")
            for j, (t, a0, b0, a1, b1) in enumerate(self.boxes):
                if j > i and not (x1 + gap <= a0 or a1 + gap <= x0 or y1 <= b0 or b1 <= y0):
                    bad.append(f"{self.name}: labels '{s}' and '{t}' overlap")
            for (p, q, cls) in self.segs:
                d = seg_box(p, q, (x0, y0, x1, y1))
                if d < gap:
                    bad.append(f"{self.name}: '{s}' is {d:.1f} px from a {cls} edge {p}->{q}")
        return bad


def seg_box(p, q, box):
    x0, y0, x1, y1 = box
    best = 1e9
    for k in range(41):
        t = k / 40
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        best = min(best, math.hypot(max(x0 - x, 0, x - x1), max(y0 - y, 0, y - y1)))
    return best


FIGS, PROBLEMS = {}, []


def finish(f, label, caption):
    FIGS[f.name] = f.svg(label, caption)
    PROBLEMS.extend(f.check())


def axes(f, x0, x1, ytop, ybot, yticks, ymax, xticks=None, xmax=None):
    f.line([(x0, ytop), (x0, ybot), (x1, ybot)], "ax")
    sy = (ybot - ytop) / ymax
    for v in yticks:
        y = ybot - v * sy
        f.line([(x0 - 4, y), (x0, y)], "ln", check=False)
        f.text(x0 - 8, y + 3, f"{v:g}", "ts", "end")
    if xticks:
        sx = (x1 - x0 - 10) / xmax
        for v in xticks:
            x = x0 + v * sx
            f.line([(x, ybot), (x, ybot + 4)], "ln", check=False)
            f.text(x, ybot + 16, f"{v:g}", "ts", "middle")
    return sy


def errbar(f, cx, base, sy, m, e):
    f.rect(cx - 25, base - m * sy, 50, m * sy, "f1 s-acc sw2")
    top, bot = base - (m + e) * sy, base - (m - e) * sy
    f.line([(cx, top), (cx, bot)], "ln thick", check=False)
    f.line([(cx - 8, top), (cx + 8, top)], "ln thick", check=False)
    f.line([(cx - 8, bot), (cx + 8, bot)], "ln thick", check=False)


# ---------- 1. stats: bars with 95% CI error bars ----------
groups = [("control", 33.0, 3.3), ("fertiliser", 36.0, 3.5), ("fertiliser", 42.0, 3.1)]
tags = ["", "X", "Y"]
n = 10
f = Fig("stats-errbars", (340, 262))
sy = axes(f, 52, 324, 34, 206, [0, 10, 20, 30, 40, 50], 50)
f.text(6, 14, "mean stem length / mm")
for i, (nm, m, s) in enumerate(groups):
    cx = 112 + i * 85
    errbar(f, cx, 206, sy, m, 2 * s / sqrt(n))
    f.text(cx, 223, nm, "tl", "middle")
    if tags[i]:
        f.text(cx, 238, tags[i], "tl", "middle")
f.text(52, 256, "bars: mean ± 95% CI (n = 10)", "tl")
finish(f, "Bar chart of mean stem length in millimetres for three groups of ten seedlings, with error bars showing the 95% confidence interval: control 33.0, fertiliser X 36.0 and fertiliser Y 42.0. The error bars of the control and fertiliser X overlap; the error bars of fertiliser X and fertiliser Y do not.",
       "Mean stem length with error bars of mean ± 95% CI (± 2 SE). The bars of the control and fertiliser X overlap, so that difference may be due to chance. The bars of fertiliser X and fertiliser Y do not overlap, so that difference is probably significant.")

# ---------- 2. planning: tenfold serial dilution ----------
f = Fig("plan-serial", (340, 190))
f.text(8, 16, "Each time: 1 cm³ into 9 cm³ of water", "tl")
conc = ["0.10", "0.010", "0.0010", "0.00010"]
nm = ["stock", "tube 1", "tube 2", "tube 3"]
for i in range(4):
    cx = 45 + i * 83
    tube = [(cx - 17, 36), (cx - 17, 114), (cx - 10, 124), (cx + 10, 124), (cx + 17, 114), (cx + 17, 36)]
    lvl = 50 if i == 0 else 74
    liquid = [(cx - 17, lvl), (cx - 17, 114), (cx - 10, 124), (cx + 10, 124), (cx + 17, 114), (cx + 17, lvl)]
    f.poly(liquid, "f2 s-acc2 sw2")
    f.line(tube, "ln")
    f.text(cx, 146, conc[i], "tl", "middle")
    f.text(cx, 162, nm[i], "tl", "middle")
    if i < 3:
        f.line([(cx + 23, 84), (cx + 60, 84)], "ln", arrow="ah")
        f.text(cx + 41.5, 74, "1 cm³", "tl", "middle")
f.text(8, 183, "concentrations in mol dm⁻³", "tl")
finish(f, "Tenfold serial dilution of a 0.10 mol per cubic decimetre stock solution in four test tubes. Arrows labelled 1 cubic centimetre lead from each tube to the next. Tubes 1 to 3 start with 9 cubic centimetres of water. The concentrations are 0.10, 0.010, 0.0010 and 0.00010 mol per cubic decimetre.",
       "A serial dilution divides the concentration by the same factor in every tube. Each of tubes 1 to 3 holds 10 cm³ after mixing (1 cm³ of the previous solution and 9 cm³ of water), so the concentration falls tenfold each time. Remove 1 cm³ from the last tube so that every tube ends with 9 cm³.")

# ---------- 3. evaluation: bar chart with SE bars ----------
data = [("placebo", 0.90, 1.04), ("low dose", 1.40, 1.11), ("high dose", 2.90, 1.21)]
n = 12
f = Fig("eval-drugbars", (340, 262))
sy = axes(f, 52, 324, 34, 206, [0, 1, 2, 3, 4], 4)
f.text(6, 14, "mean fall in glucose / mmol dm⁻³")
for i, (nm, m, s) in enumerate(data):
    cx = 112 + i * 85
    errbar(f, cx, 206, sy, m, s / sqrt(n))
    f.text(cx, 223, nm, "tl", "middle")
f.text(52, 256, "bars: mean ± SE (n = 12 mice)", "tl")
finish(f, "Bar chart of the mean fall in blood glucose in mmol per cubic decimetre for three groups of twelve mice, with error bars showing one standard error: placebo 0.90, low dose 1.40 and high dose 2.90.",
       "Mean fall in blood glucose after four weeks, with error bars of mean ± 1 SE. Compare the placebo and low-dose bars, and the low-dose and high-dose bars.")

# ---------- 4. evaluation: lichen scatter ----------
dist = [5, 10, 20, 30, 50, 70, 90, 120, 150, 200]
cover = [3, 2, 6, 9, 8, 17, 22, 19, 31, 38]
f = Fig("eval-lichen", (340, 250))
x0, x1, yt, yb = 52, 324, 34, 200
sy = axes(f, x0, x1, yt, yb, [0, 10, 20, 30, 40], 40, xticks=[0, 50, 100, 150, 200], xmax=200)
sx = (x1 - x0 - 10) / 200
for d, c in zip(dist, cover):
    f.circle(x0 + d * sx, yb - c * sy, 3.2, "f1 s-acc sw2")  # 3.2: the 5 m and 10 m points must not overlap
f.text(6, 14, "lichen cover / %")
f.text(x1 - 2, 238, "distance from the road / m", "tl", "end")
finish(f, "Scatter graph of lichen cover in percent against distance from a road in metres for ten trees. Lichen cover rises from 3 percent at 5 metres to 38 percent at 200 metres; the points rise from left to right with some scatter.",
       "The ten trees of the lichen survey. Lichen cover tends to rise with distance from the road, but the rise is not a perfect straight line.")

if __name__ == "__main__":
    for ch in ("bio.stats", "bio.planning", "bio.evaluation"):
        p = os.path.join(CH, ch + ".md")
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        new = re.sub(r"^@@FIG ([a-z-]+)@@$", lambda m: FIGS[m.group(1)], txt, flags=re.M)
        if new != txt:
            open(p, "w", encoding="utf-8", newline="").write(new)
            print("figures placed in", ch)
    print("\n".join(PROBLEMS) or "clearance ok")
