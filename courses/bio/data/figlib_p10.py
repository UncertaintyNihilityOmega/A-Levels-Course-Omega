# data/figlib_p10.py: shared helpers for the P10 figure scripts (fig_bio.immunity.py, fig_bio.antibodies.py).
# Same Fig class as data/fig_bio.enzymes.py (label boxes: 7 px per character, top at y - 10, bottom at y + 3) plus
# blobs, point-in-polygon tests and a leader check: every leader must END inside (or on) the shape it names.
import math, sys
sys.stdout.reconfigure(encoding="utf-8")

CW = {"tl": 7.0, "ts": 6.2}


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


def inside(pt, poly, tol=0.0):
    """Point in polygon (ray casting); a point within tol of an edge also counts."""
    x, y = pt
    n, c = len(poly), False
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
        if tol and seg_pt((x1, y1), (x2, y2), pt) <= tol:
            return True
    return c


def seg_pt(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((r[0] - p[0]) * dx + (r[1] - p[1]) * dy) / L))
    return math.hypot(p[0] + t * dx - r[0], p[1] + t * dy - r[1])


def rect_poly(x, y, w, h):
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


def circ_poly(cx, cy, r, n=24):
    return [(cx + r * math.cos(2 * math.pi * k / n), cy + r * math.sin(2 * math.pi * k / n)) for k in range(n)]


def blob(cx, cy, R, phase=0.0, bay=0.0, arms=0.0, n=72, bw=0.5, ac=0.95):
    """Smooth cell outline. bay > 0 cuts a notch on the right (theta = 0) with two arms either side."""
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / n
        th = math.atan2(math.sin(t), math.cos(t))
        r = R * (1 + 0.05 * math.sin(3 * t + phase) + 0.03 * math.sin(5 * t + 2 * phase))
        r *= 1 - bay * math.exp(-(th / bw) ** 2)
        r *= 1 + arms * math.exp(-((abs(th) - ac) / 0.3) ** 2)
        pts.append((round(cx + r * math.cos(t), 1), round(cy + r * math.sin(t), 1)))
    return pts


def strip(center, width):
    """Polygon around a polyline (thick chain)."""
    left, right = [], []
    n = len(center)
    for i, (x, y) in enumerate(center):
        a = center[max(i - 1, 0)]
        b = center[min(i + 1, n - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        left.append((round(x + nx * width / 2, 1), round(y + ny * width / 2, 1)))
        right.append((round(x - nx * width / 2, 1), round(y - ny * width / 2, 1)))
    return left + right[::-1]


class Fig:
    def __init__(self, name):
        self.name, self.parts, self.segs, self.boxes, self.problems = name, [], [], [], []
        self.shapes = {}

    def poly(self, pts, cls, closed=True, check=True, name=None):
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts) + ("Z" if closed else "")
        self.parts.append(f'<path class="{cls}" d="{d}"/>')
        if check:
            ring = pts + ([pts[0]] if closed else [])
            self.segs += [(a, b, cls) for a, b in zip(ring, ring[1:])]
        if name:
            self.shapes[name] = pts

    def line(self, pts, cls, arrow=None, check=True):
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts)
        m = f' marker-end="url(#{arrow})"' if arrow else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{m}/>')
        if check:
            self.segs += [(a, b, cls) for a, b in zip(pts, pts[1:])]

    def rect(self, x, y, w, h, cls, rx=0, name=None, check=True):
        r = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{r}/>')
        p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
        if check:
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]
        if name:
            self.shapes[name] = rect_poly(x, y, w, h)

    def circle(self, cx, cy, r, cls, name=None, check=True):
        self.parts.append(f'<circle class="{cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        p = circ_poly(cx, cy, r, 24)
        if check:
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:] + p[:1])]
        if name:
            self.shapes[name] = p

    def text(self, x, y, s, cls="tl", anchor="start"):
        kind = "ts" if "ts" in cls.split() else "tl"
        w = len(s) * CW[kind] * (1.06 if "tb" in cls.split() else 1)
        h_top, h_bot = (10, 3) if kind == "tl" else (9, 3)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        a = {"middle": ' text-anchor="middle"', "end": ' text-anchor="end"'}.get(anchor, "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}"{a}>{s}</text>')
        self.boxes.append((s, x0, y - h_top, x0 + w, y + h_bot))

    def leader(self, a, b, target, cls="ln-m thin"):
        """Leader from a (at the label) to b, which must lie in the named shape."""
        self.line([a, b], cls, check=False)
        poly = self.shapes[target]
        if not inside(b, poly, tol=1.5):
            self.problems.append(f"{self.name}: leader end {b} is not on '{target}'")
        for (s, x0, y0, x1, y1) in self.boxes:
            d = seg_box(a, b, (x0, y0, x1, y1))
            if seg_box(a, a, (x0, y0, x1, y1)) <= 6:
                continue  # the leader's own label
            if d < 4:
                self.problems.append(f"{self.name}: leader {a}->{b} touches label '{s}' ({d:.1f} px)")

    def svg(self, vb, label, caption, size="fig small"):
        self.vb = vb
        body = "".join(self.parts)
        return (f'<figure class="{size}"><svg viewBox="0 0 {vb[0]} {vb[1]}" role="img" aria-label="{label}">'
                f'{body}</svg><figcaption>{caption}</figcaption></figure>')

    def check(self, gap=4.0):
        bad = list(self.problems)
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
