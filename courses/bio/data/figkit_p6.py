# data/figkit_p6.py: shared helpers for the hand-drawn SVG figures of package P6 (copy of figkit_p4 with extra shapes).
# Same Fig class as data/fig_bio.enzymes.py: every label box is checked 4 px clear of every edge, leader and label.
# 13 px label model (kit/STYLE.md): 7 px per character wide, top at y - 10, bottom at y + 3.
import math, sys
sys.stdout.reconfigure(encoding="utf-8")

CW = {"tl": 7.0, "ts": 6.2}
LEAD = "ln-m thin"


def seg_box(p, q, box):
    x0, y0, x1, y1 = box
    best = 1e9
    for k in range(41):
        t = k / 40
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        dx = max(x0 - x, 0, x - x1)
        dy = max(y0 - y, 0, y - y1)
        best = min(best, math.hypot(dx, dy))
    return best


class Fig:
    def __init__(self, name):
        self.name, self.parts, self.segs, self.boxes, self.leads, self.problems = name, [], [], [], [], []

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

    def text(self, x, y, s, cls="tl", anchor="start"):
        kind = "ts" if "ts" in cls.split() else "tl"
        w = len(s) * CW[kind] * (1.06 if "tb" in cls.split() else 1)
        h_top, h_bot = (10, 3) if kind == "tl" else (9, 3)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        a = {"middle": ' text-anchor="middle"', "end": ' text-anchor="end"'}.get(anchor, "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}"{a}>{s}</text>')
        self.boxes.append((s, x0, y - h_top, x0 + w, y + h_bot))

    def leader(self, a, b):
        """A leader line a->b: it may touch only its own label (the one nearest a)."""
        self.parts.append(f'<path class="{LEAD}" d="M{a[0]:g} {a[1]:g}L{b[0]:g} {b[1]:g}"/>')
        self.leads.append((a, b))

    def svg(self, vb, label, caption, size="fig small"):
        self.vb = vb
        return (f'<figure class="{size}"><svg viewBox="0 0 {vb[0]} {vb[1]}" role="img" aria-label="{label}">'
                f'{"".join(self.parts)}</svg><figcaption>{caption}</figcaption></figure>')

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
            for (a, b) in self.leads:
                d = seg_box(a, b, (x0, y0, x1, y1))
                own = min(math.hypot(a[0] - min(max(a[0], x0), x1), a[1] - min(max(a[1], y0), y1)), 1e9) < 12
                if d < gap and not own:
                    bad.append(f"{self.name}: leader {a}->{b} is {d:.1f} px from label '{s}'")
        return bad


def bez(p0, p1, p2, p3, n=24):
    out = []
    for k in range(n + 1):
        t = k / n
        u = 1 - t
        out.append((round(u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0], 1),
                    round(u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1], 1)))
    return out


def sh(pts, dx, dy):
    return [(x + dx, y + dy) for x, y in pts]


def arc_pts(cx, cy, rx, ry, a0, a1, n=40):
    """Points on an ellipse arc, angles in degrees (0 = +x, clockwise on screen)."""
    return [(round(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * k / n)), 1),
             round(cy + ry * math.sin(math.radians(a0 + (a1 - a0) * k / n)), 1)) for k in range(n + 1)]


def ellipse(f, cx, cy, rx, ry, cls, check=True):
    pts = arc_pts(cx, cy, rx, ry, 0, 360, 48)
    f.poly(pts[:-1], cls, True, check)


def xchrom(f, cx, cy, L, cls, ang=0, spread=20):
    """Replicated chromosome: two sister chromatids crossing at the centromere (dot)."""
    for s in (-1, 1):
        a = math.radians(ang + s * spread)
        dx, dy = L / 2 * math.cos(a), L / 2 * math.sin(a)
        f.line([(cx - dx, cy - dy), (cx + dx, cy + dy)], cls, check=False)
    f.circle(cx, cy, 2.2, "fi") if False else f.parts.append(f'<circle class="fi" cx="{cx:g}" cy="{cy:g}" r="2.2"/>')


def vchrom(f, px, py, L, cls, toward, spread=28):
    """Separated chromatid pulled by its centromere (at px,py) towards a pole: V-shape opening away from the pole."""
    sgn = -1 if toward == "left" else 1          # arms trail on the opposite side of the pole
    for s in (-1, 1):
        a = math.radians(spread)
        f.line([(px, py), (px - sgn * L * math.cos(a), py + s * L * math.sin(a))], cls, check=False)
    f.parts.append(f'<circle class="fi" cx="{px:g}" cy="{py:g}" r="2.2"/>')
