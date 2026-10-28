# data/figkit_p2.py: shared helpers for the hand-drawn SVG figures of bio.microscopy, bio.cells and bio.prokaryotes.
# Same Fig class as data/fig_bio.enzymes.py (label boxes are checked 4 px clear of every edge, leader and label),
# plus ellipse(), smooth() and a leader() that checks the leader against the other labels.
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


def ell_pts(cx, cy, rx, ry, n=36, rot=0.0):
    c, s = math.cos(rot), math.sin(rot)
    out = []
    for k in range(n + 1):
        t = 2 * math.pi * k / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        out.append((cx + x * c - y * s, cy + x * s + y * c))
    return out


class Fig:
    def __init__(self, name):
        self.name, self.parts, self.segs, self.boxes, self.leads, self.problems = name, [], [], [], [], []
        self.tf = None      # (sx, sy, ox, oy, k): maps drawing coordinates to the figure; text and leader starts are not mapped

    def P(self, x, y):
        if not self.tf:
            return (x, y)
        sx, sy, ox, oy, k = self.tf
        return (round(ox + (x - sx) * k, 1), round(oy + (y - sy) * k, 1))

    def K(self, v):
        return v * self.tf[4] if self.tf else v

    def my(self, y):
        return self.P(0, y)[1]

    def poly(self, pts, cls, closed=True, check=True):
        pts = [self.P(x, y) for x, y in pts]
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts) + ("Z" if closed else "")
        self.parts.append(f'<path class="{cls}" d="{d}"/>')
        if check:
            ring = pts + ([pts[0]] if closed else [])
            self.segs += [(a, b, cls) for a, b in zip(ring, ring[1:])]

    def smooth(self, pts, cls, closed=True, check=True):
        """Polyline through many points drawn as a path (use for curves computed in Python)."""
        self.poly([(round(x), round(y)) for x, y in pts], cls, closed, check)

    def line(self, pts, cls, arrow=None, check=True):
        pts = [self.P(x, y) for x, y in pts]
        d = "M" + "L".join(f"{x:g} {y:g}" for x, y in pts)
        m = f' marker-end="url(#{arrow})"' if arrow else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{m}/>')
        if check:
            self.segs += [(a, b, cls) for a, b in zip(pts, pts[1:])]

    def rect(self, x, y, w, h, cls, rx=0, check=True):
        x, y = self.P(x, y)
        w, h, rx = self.K(w), self.K(h), self.K(rx)
        r = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{r}/>')
        if check:
            p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def circle(self, cx, cy, r, cls, check=True):
        cx, cy = self.P(cx, cy)
        r = self.K(r)
        self.parts.append(f'<circle class="{cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        if check:
            p = ell_pts(cx, cy, r, r, 24)
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def ellipse(self, cx, cy, rx, ry, cls, rot=0.0, check=True):
        """Emits an <ellipse> element; the edge is recorded as a 48-gon for the clearance check."""
        cx, cy = self.P(cx, cy)
        rx, ry = self.K(rx), self.K(ry)
        tr = f' transform="rotate({math.degrees(rot):g} {cx:g} {cy:g})"' if rot else ""
        self.parts.append(f'<ellipse class="{cls}" cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}"{tr}/>')
        if check:
            p = ell_pts(cx, cy, rx, ry, 48, rot)
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def dots(self, pts, r, cls):
        """Small filled circles (ribosomes, vesicles): not checked against labels."""
        for x, y in pts:
            x, y = self.P(x, y)
            self.parts.append(f'<circle class="{cls}" cx="{x:g}" cy="{y:g}" r="{self.K(r):g}"/>')

    def text(self, x, y, s, cls="tl", anchor="start"):
        kind = "ts" if "ts" in cls.split() else "tl"
        w = len(s) * CW[kind] * (1.06 if "tb" in cls.split() else 1)
        h_top, h_bot = (10, 3) if kind == "tl" else (9, 3)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        a = {"middle": ' text-anchor="middle"', "end": ' text-anchor="end"'}.get(anchor, "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}"{a}>{s}</text>')
        self.boxes.append((s, x0, y - h_top, x0 + w, y + h_bot))

    def label(self, x, y, s, a, b, anchor="start", cls="tl"):
        """A label plus a leader from a (next to the label) to b (on the part)."""
        self.text(x, y, s, cls, anchor)
        b = self.P(*b)
        sv, self.tf = self.tf, None
        self.line([a, b], LEAD, check=False)
        self.tf = sv
        self.leads.append((a, b, s))

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
                if j > i and not (x1 + gap <= a0 or a1 + gap <= x0 or y1 + 0 <= b0 or b1 <= y0):
                    bad.append(f"{self.name}: labels '{s}' and '{t}' overlap")
            for (p, q, cls) in self.segs:
                d = seg_box(p, q, (x0, y0, x1, y1))
                if d < gap:
                    bad.append(f"{self.name}: '{s}' is {d:.1f} px from a {cls} edge {p}->{q}")
        for (a, b, own) in self.leads:
            for (s, x0, y0, x1, y1) in self.boxes:
                if s == own:
                    continue
                d = seg_box(a, b, (x0, y0, x1, y1))
                if d < gap:
                    bad.append(f"{self.name}: leader of '{own}' is {d:.1f} px from label '{s}'")
            ln = math.hypot(b[0] - a[0], b[1] - a[1])
            if ln < 8:
                bad.append(f"{self.name}: leader of '{own}' is only {ln:.0f} px long")
        return bad


def finish(figs, problems):
    for s in figs:
        print(s)
        print()
    print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
