# data/fig_bio.mock.p2.py: builds the labelled plant cell SVG of Question 1 in chapters/bio.mock.p2.md and checks label clearance.
# Run: py data/fig_bio.mock.p2.py -> prints the <figure> (paste into the chapter) and a clearance report.
import math, sys
sys.stdout.reconfigure(encoding="utf-8")

CW = {"tl": 7.0, "ts": 6.2}


class Fig:
    def __init__(self, name):
        self.name, self.parts, self.segs, self.boxes = name, [], [], []

    # shapes: every edge is recorded for the clearance check
    def poly(self, pts, cls, closed=True, check=True):
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts) + ("Z" if closed else "")
        self.parts.append(f'<path class="{cls}" d="{d}"/>')
        if check:
            ring = pts + ([pts[0]] if closed else [])
            self.segs += [(a, b, cls) for a, b in zip(ring, ring[1:])]

    def line(self, pts, cls, arrow=None, check=True):
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts)
        m = f' marker-end="url(#{arrow})"' if arrow else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{m}/>')
        if check:
            self.segs += [(a, b, cls) for a, b in zip(pts, pts[1:])]

    def rect(self, x, y, w, h, cls, rx=0):
        r = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{r}/>')
        p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
        self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def circle(self, cx, cy, r, cls):
        self.parts.append(f'<circle class="{cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        p = [(cx + r * math.cos(t / 12 * math.pi), cy + r * math.sin(t / 12 * math.pi)) for t in range(25)]
        self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def text(self, x, y, s, cls="tl", anchor="start", leader_ok=()):
        kind = "ts" if "ts" in cls.split() else "tl"
        w = len(s) * CW[kind] * (1.06 if "tb" in cls.split() else 1)
        h_top, h_bot = (10, 3) if kind == "tl" else (9, 3)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        a = {"middle": ' text-anchor="middle"', "end": ' text-anchor="end"'}.get(anchor, "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}"{a}>{s}</text>')
        self.boxes.append((s, x0, y - h_top, x0 + w, y + h_bot))

    def svg(self, vb, label, caption, size="fig small"):
        self.vb = vb
        body = "".join(self.parts)
        return (f'<figure class="{size}"><svg viewBox="0 0 {vb[0]} {vb[1]}" role="img" aria-label="{label}">'
                f'{body}</svg><figcaption>{caption}</figcaption></figure>')

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
    """Shortest distance from segment pq to an axis-aligned box (0 if they meet)."""
    x0, y0, x1, y1 = box
    best = 1e9
    for k in range(41):
        t = k / 40
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        dx = max(x0 - x, 0, x - x1)
        dy = max(y0 - y, 0, y - y1)
        best = min(best, math.hypot(dx, dy))
    return best




def ellipse(cx, cy, rx, ry, n=36):
    return [(round(cx + rx * math.cos(2 * math.pi * k / n), 1), round(cy + ry * math.sin(2 * math.pi * k / n), 1)) for k in range(n)]


f = Fig("plantcell")
f.vb = (340, 250)
# cell wall (thick outline) and cytoplasm
f.rect(90, 35, 160, 190, "fp ln sw3", rx=6)
# large permanent vacuole
f.poly(ellipse(150, 135, 42, 70), "f1 s-acc sw2")
# nucleus with nucleolus
f.circle(215, 70, 22, "f2 s-acc sw2")
f.circle(209, 66, 6, "f3 s-acc sw2")
# chloroplasts (one labelled) and a mitochondrion
f.poly(ellipse(222, 130, 22, 11), "f3 s-acc sw2")
f.poly(ellipse(205, 207, 20, 9), "f3 s-acc sw2")
f.poly(ellipse(222, 180, 15, 8), "f2 s-acc sw2")
# leaders and labels A to E
for letter, (lx, ly), (ex, ey), side in [
    ("A", (38, 56), (91, 52), "L"),
    ("C", (38, 140), (122, 135), "L"),
    ("D", (290, 60), (222, 66), "R"),
    ("B", (290, 128), (230, 129), "R"),
    ("E", (290, 186), (230, 181), "R"),
]:
    if side == "L":
        f.line([(lx + 14, ly - 4), (ex, ey)], "ln thin")
    else:
        f.line([(lx - 6, ly - 4), (ex, ey)], "ln thin")
    f.text(lx, ly, letter, "tl tb")
bad = f.check()
print("\n".join(bad) if bad else "clearance ok")
label = ("A plant cell drawn from an electron micrograph. A is the cell wall at the left edge. C is the large central vacuole. "
         "D is the nucleus at the top right, B is a chloroplast and E is a mitochondrion, both at the right.")
cap = "A drawing of a plant cell as seen in an electron micrograph (not to scale). The structures are labelled A to E."
print(f.svg((340, 250), label, cap))
