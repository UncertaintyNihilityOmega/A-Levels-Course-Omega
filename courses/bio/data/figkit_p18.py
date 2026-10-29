# data/figkit_p18.py: Fig class (as in fig_bio.enzymes.py) + place(): puts generated <figure>s into a chapter.
# A chapter holds @@FIG name@@ (alone on a line) or a figure line with data-fig="name"; place() replaces that whole line.
# Model of a 13 px label (kit/STYLE.md): 7 px per character wide, top at y - 10, bottom at y + 3.
import math, sys, os, re
sys.stdout.reconfigure(encoding="utf-8")

CW = {"tl": 7.0, "ts": 6.2}


class Fig:
    def __init__(self, name):
        self.name, self.parts, self.segs, self.boxes = name, [], [], []

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

    def rect(self, x, y, w, h, cls, rx=0, check=True):
        r = f' rx="{rx}"' if rx else ""
        self.parts.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{r}/>')
        p = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
        if check:
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def circle(self, cx, cy, r, cls, check=True):
        self.parts.append(f'<circle class="{cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>')
        p = [(cx + r * math.cos(t / 12 * math.pi), cy + r * math.sin(t / 12 * math.pi)) for t in range(25)]
        if check:
            self.segs += [(a, b, cls) for a, b in zip(p, p[1:])]

    def text(self, x, y, s, cls="tl", anchor="start"):
        kind = "ts" if "ts" in cls.split() else "tl"
        w = len(s) * CW[kind] * (1.06 if "tb" in cls.split() else 1)
        h_top, h_bot = (10, 3) if kind == "tl" else (9, 3)
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        a = {"middle": ' text-anchor="middle"', "end": ' text-anchor="end"'}.get(anchor, "")
        self.parts.append(f'<text class="{cls}" x="{x:g}" y="{y:g}"{a}>{s}</text>')
        self.boxes.append((s, x0, y - h_top, x0 + w, y + h_bot))

    def raw(self, s):
        self.parts.append(s)

    def svg(self, vb, label, caption, size="fig small"):
        self.vb = vb
        body = "".join(self.parts)
        return (f'<figure class="{size}" data-fig="{self.name}"><svg viewBox="0 0 {vb[0]} {vb[1]}" role="img" aria-label="{label}">'
                f'{body}</svg><figcaption>{caption}</figcaption></figure>')

    def check(self, gap=4.0):
        bad = []
        for i, (s, x0, y0, x1, y1) in enumerate(self.boxes):
            if x0 < 2 or y0 < 2 or x1 > self.vb[0] - 2 or y1 > self.vb[1] - 2:
                bad.append(f"{self.name}: '{s}' leaves the viewBox ({x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f})")
            for j, (t, a0, b0, a1, b1) in enumerate(self.boxes):
                if j > i and not (x1 + gap <= a0 or a1 + gap <= x0 or y1 + 1 <= b0 or b1 + 1 <= y0):
                    bad.append(f"{self.name}: labels '{s}' and '{t}' overlap")
            for (p, q, cls) in self.segs:
                d = seg_box(p, q, (x0, y0, x1, y1))
                if d < gap - 1e-9:
                    bad.append(f"{self.name}: '{s}' is {d:.1f} px from a {cls} edge {p}->{q}")
        return bad


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


def place(chapter, figs):
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.dirname(here), "chapters", chapter + ".md")
    lines = open(path, encoding="utf-8").read().split("\n")
    done = []
    for i, ln in enumerate(lines):
        m = re.fullmatch(r"@@FIG (\S+)@@", ln.strip())
        key = m.group(1) if m else None
        if key is None:
            m2 = re.search(r'<figure[^>]* data-fig="([^"]+)"', ln)
            key = m2.group(1) if m2 else None
        if key in figs:
            lines[i] = figs[key]
            done.append(key)
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    print("placed", done, "missing", [k for k in figs if k not in done])


def report(figs_objs):
    bad = []
    for f in figs_objs:
        bad += f.check()
    print("clearance problems:", len(bad))
    for b in bad:
        print("  ", b)
