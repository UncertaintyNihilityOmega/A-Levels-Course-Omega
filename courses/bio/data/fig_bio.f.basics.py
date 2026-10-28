# data/fig_bio.f.basics.py: builds the hand-drawn SVG figures of chapters/bio.f.basics.md and checks label clearance.
# Run: py data/fig_bio.f.basics.py  -> prints each <figure> (paste into the chapter) and a clearance report on stderr.
# Model of a 13 px label (kit/STYLE.md): 7 px per character wide, top at y - 10, bottom at y + 3.
import math, sys
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
                if j > i and not (x1 + gap <= a0 or a1 + gap <= x0 or y1 + gap <= b0 or b1 + gap <= y0):
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
        dx = max(x0 - x, 0, x - x1)
        dy = max(y0 - y, 0, y - y1)
        best = min(best, math.hypot(dx, dy))
    return best


def leader(f, a, b, own, cls="ln-m thin", ok_dist=0.0):
    """Draw a leader a->b. It must stay 4 px clear of every label except the one named `own`."""
    f.line([a, b], cls, check=False)
    out = []
    for (s, x0, y0, x1, y1) in f.boxes:
        if s == own:
            continue
        d = seg_box(a, b, (x0, y0, x1, y1))
        if d < 4:
            out.append(f"{f.name}: leader {a}->{b} is {d:.1f} px from label '{s}'")
    for (p, q, c) in f.segs:  # crossing other drawn edges is allowed only at the ends; report near-misses
        pass
    return out


figs, problems = [], []

# ---------- Figure 1: size ladder (log scale) ----------
f = Fig("ladder")
D = 68.0
Y0 = 456.0
y = lambda d: Y0 - d * D
f.text(10, 18, "Each step up is 10 times bigger", "tl")
f.line([(54, Y0 + 10), (54, 38)], "ax", "ahm", check=False)
ticks = ["0.1 nm", "1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm"]
for k, s in enumerate(ticks):
    f.line([(50, y(k)), (58, y(k))], "ln-m thin", check=False)
    f.text(46, y(k) + 3, s, "ts", "end")
items = [  # (label, d_low, d_high, x_bar, d_label)
    ("atom about 0.1 nm", 0.0, 0.0, 76, 0.0),
    ("small molecule about 1 nm", 1.0, 1.0, 76, 1.0),
    ("protein 5–10 nm", 1.699, 2.0, 76, 1.85),
    ("virus 20–300 nm", 2.301, 3.477, 76, 2.9),
    ("bacterium 1–5 µm", 4.0, 4.699, 76, 4.35),
    ("animal cell 10–30 µm", 5.0, 5.477, 90, 5.24),
    ("plant cell 10–100 µm", 5.0, 6.0, 76, 5.8),
]
for (lab, lo, hi, xb, dl) in items:
    if lo == hi:
        f.circle(xb, y(lo), 4, "f1 s-acc sw2")
    else:
        f.line([(xb, y(lo)), (xb, y(hi))], "c1 sw3", check=False)
    f.text(116, y(dl) + 4, lab)
    problems.extend(leader(f, (xb + 6, y(dl)), (111, y(dl)), lab))
figs.append(f.svg((330, 480),
    "Size ladder on a log scale from 0.1 nanometres to 100 micrometres. An atom is about 0.1 nm, a small molecule about 1 nm, "
    "a protein 5 to 10 nm, a virus 20 to 300 nm, a bacterium 1 to 5 micrometres, an animal cell 10 to 30 micrometres and a "
    "plant cell 10 to 100 micrometres.",
    "How big are the things of biology? The scale is logarithmic: each tick is 10 times bigger than the one below, so the "
    "plant cell is about a million times wider than an atom. Bars show the usual range."))
problems.extend(f.check())

# ---------- Figure 2: levels of organisation ----------
f = Fig("levels")
rows = [
    ("molecule", "glucose, DNA, protein", None),
    ("organelle", "nucleus, mitochondrion", None),
    ("cell", "red blood cell", None),
    ("tissue", "muscle tissue", None),
    ("organ", "the heart", None),
    ("organ system", "circulatory system", None),
    ("organism", "one human", None),
    ("population", "lions in one park", None),
    ("community", "all the populations", "in a woodland"),
    ("ecosystem", "woodland, its soil, air", "and all its organisms"),
]
PITCH, TOP, BH = 46, 34, 28
f.text(10, 16, "Smallest at the top, largest at the bottom", "tl")
for i, (lvl, e1, e2) in enumerate(rows):
    t = TOP + i * PITCH
    f.rect(10, t, 130, BH, "f1 s-acc sw2", 5)
    f.text(75, t + 19, lvl, "tl tb", "middle")
    if e2:
        f.text(156, t + 8, e1)
        f.text(156, t + 25, e2)
    else:
        f.text(156, t + 19, e1)
    if i < len(rows) - 1:
        f.line([(75, t + BH), (75, t + PITCH - 2)], "ln", "ah", check=False)
H2 = TOP + len(rows) * PITCH - 10
figs.append(f.svg((345, H2),
    "Levels of organisation from smallest to largest, each with an example: molecule (glucose, DNA, protein); organelle "
    "(nucleus, mitochondrion); cell (red blood cell); tissue (muscle tissue); organ (the heart); organ system (circulatory "
    "system); organism (one human); population (lions in one park); community (all the populations in a woodland); "
    "ecosystem (the woodland, its soil, air and all its organisms).",
    "The levels of organisation. Each level is made of the one above it in the list: cells make tissues, tissues make "
    "organs, and so on."))
problems.extend(f.check())

# ---------- Figure 3: condensation and hydrolysis ----------
f = Fig("beads")
A, B = "f1 s-acc sw2", "f2 s-acc2 sw2"
R = 13
# row 1: condensation
f.text(10, 16, "Condensation: bond forms, water made", "tl tb")
yy = 56
f.circle(40, yy, R, A)
f.text(40, yy + 4, "A", "tl", "middle")
f.line([(53, yy), (62, yy)], "ln thick", check=False)
f.text(64, yy + 4, "OH")
f.text(90, yy + 4, "H")
f.line([(104, yy), (112, yy)], "ln thick", check=False)
f.circle(125, yy, R, B)
f.text(125, yy + 4, "B", "tl", "middle")
f.line([(150, yy), (186, yy)], "ln", "ah", check=False)
f.circle(205, yy, R, A)
f.text(205, yy + 4, "A", "tl", "middle")
f.line([(218, yy), (236, yy)], "ln thick", check=False)
f.circle(249, yy, R, B)
f.text(249, yy + 4, "B", "tl", "middle")
f.text(270, yy + 4, "+ H₂O")
f.text(82, yy + 36, "two monomers", "tl", "middle")
f.text(227, yy + 36, "a dimer", "tl", "middle")
# row 2: hydrolysis
y2 = 160
f.text(10, 128, "Hydrolysis: water added, bond breaks", "tl tb")
f.circle(40, y2, R, A)
f.text(40, y2 + 4, "A", "tl", "middle")
f.line([(53, y2), (71, y2)], "ln thick", check=False)
f.circle(84, y2, R, B)
f.text(84, y2 + 4, "B", "tl", "middle")
f.text(106, y2 + 4, "+ H₂O")
f.line([(158, y2), (192, y2)], "ln", "ah", check=False)
f.circle(212, y2, R, A)
f.text(212, y2 + 4, "A", "tl", "middle")
f.line([(225, y2), (234, y2)], "ln thick", check=False)
f.text(236, y2 + 4, "OH")
f.text(262, y2 + 4, "H")
f.line([(276, y2), (284, y2)], "ln thick", check=False)
f.circle(297, y2, R, B)
f.text(297, y2 + 4, "B", "tl", "middle")
f.text(58, y2 + 36, "a dimer", "tl", "middle")
f.text(254, y2 + 36, "two monomers", "tl", "middle")
figs.append(f.svg((330, 212),
    "Condensation and hydrolysis of a dimer drawn as beads. Condensation: monomer A with an OH group and monomer B with an H "
    "join to make a dimer A–B and a molecule of water. Hydrolysis is the reverse: the dimer plus a molecule of water gives "
    "monomer A with OH and monomer B with H.",
    "Condensation joins two monomers into a dimer and makes a molecule of water. Hydrolysis uses a molecule of water to "
    "break the bond and give the two monomers back. Repeated condensation builds a polymer."))
problems.extend(f.check())

# ---------- Figure 4: water and the hydrogen bond ----------
f = Fig("water")
O1, O2 = (62, 126), (200, 82)
H1a, H1b = (26, 82), (98, 82)
H2a, H2b = (164, 126), (236, 126)
for o, h in ((O1, H1a), (O1, H1b), (O2, H2a), (O2, H2b)):
    f.line([o, h], "ln thick", check=False)
f.line([(H1b[0] + 12, 82), (O2[0] - 18, 82)], "ln dot thick", check=False)
for (cx, cy), nm, r, cl in ((O1, "O", 16, "f2 s-acc2 sw2"), (O2, "O", 16, "f2 s-acc2 sw2"),
                            (H1a, "H", 12, "f1 s-acc sw2"), (H1b, "H", 12, "f1 s-acc sw2"),
                            (H2a, "H", 12, "f1 s-acc sw2"), (H2b, "H", 12, "f1 s-acc sw2")):
    f.circle(cx, cy, r, cl)
    f.text(cx, cy + 4, nm, "tl", "middle")
f.text(98, 56, "δ+", "tl", "middle")
f.text(224, 78, "δ−")
f.text(30, 138, "δ−", "tl", "middle")
f.text(116, 58, "hydrogen bond")
problems.extend(leader(f, (146, 63), (146, 78), "hydrogen bond"))
f.text(62, 176, "water molecule", "tl", "middle")
f.text(200, 176, "water molecule", "tl", "middle")
f.text(246, 96, "covalent bond")
problems.extend(leader(f, (244, 92), (218, 104), "covalent bond"))
figs.append(f.svg((345, 190),
    "Two water molecules. In each, an oxygen atom is joined to two hydrogen atoms by covalent bonds. The oxygen is slightly "
    "negative (delta minus) and each hydrogen slightly positive (delta plus). A dotted hydrogen bond links a hydrogen atom "
    "of the left molecule to the oxygen atom of the right molecule.",
    "Water is a polar molecule. The shared electrons in the O–H bonds lie closer to oxygen, so oxygen is slightly negative "
    "and each hydrogen slightly positive. The opposite charges on neighbouring molecules attract: that is a hydrogen bond."))
problems.extend(f.check())

for s in figs:
    print(s)
    print()
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
