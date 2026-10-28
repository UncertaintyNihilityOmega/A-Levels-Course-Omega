# data/fig_bio.enzymes.py: builds the hand-drawn SVG figures of chapters/bio.enzymes.md and checks label clearance.
# Run: py data/fig_bio.enzymes.py  -> prints each <figure> (paste into the chapter) and a clearance report.
# Model of a 13 px label (kit/STYLE.md): 7 px per character wide, top at y - 10, bottom at y + 3.
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


figs, problems = [], []

# ---------- Figure 1 and 2: lock and key, induced fit (three stacked rows) ----------
ROW = 125
SUB = [(90, 62), (150, 62), (150, 70), (145, 70), (135, 92), (105, 92), (95, 70), (90, 70)]
SUB_L = [(90, 62), (120, 62), (120, 92), (105, 92), (95, 70), (90, 70)]
SUB_R = [(120, 62), (150, 62), (150, 70), (145, 70), (135, 92), (120, 92)]


def enzyme(notch):
    return [(40, 70)] + notch + [(200, 70), (200, 112), (40, 112)]


FIT = [(95, 70), (105, 92), (135, 92), (145, 70)]          # complementary to the substrate
LOOSE = [(103, 70), (111, 86), (129, 86), (137, 70)]       # induced fit: not yet complementary
E, S = "f1 s-acc sw2", "f2 s-acc2 sw2"
LEAD = "ln-m thin"


def three_rows(name, first_notch, second_notch, titles, labels, label, caption):
    f = Fig(name)
    for r in range(3):
        oy = r * ROW
        f.text(10, oy + 16, titles[r], "tl tb")
        notch = first_notch if r != 1 else second_notch
        f.poly(sh(enzyme(notch), 0, oy), E)
        if r == 0:
            f.poly(sh(SUB, 0, oy - 32), S)
        elif r == 1:
            f.poly(sh(SUB, 0, oy), S)
        else:
            f.poly(sh(SUB_L, -30, oy - 30), S)
            f.poly(sh(SUB_R, 30, oy - 30), S)
        for (x, y, s, lead) in labels[r]:
            f.text(x, oy + y, s)
            if lead:
                f.line([(lead[0], oy + lead[1]), (lead[2], oy + lead[3])], LEAD, check=False)
                problems.extend(lead_check(f, (lead[0], oy + lead[1]), (lead[2], oy + lead[3])))
    figs.append(f.svg((330, 3 * ROW - 8), label, caption))
    problems.extend(f.check())


def lead_check(f, a, b):
    """A leader may touch only its own label: it must stay 4 px clear of every other label."""
    out = []
    for (s, x0, y0, x1, y1) in f.boxes:
        d = seg_box(a, b, (x0, y0, x1, y1))
        if 0 < d < 4 or (d == 0 and not (abs(a[0] - x0) < 6 or abs(a[0] - x1) < 6)):
            out.append(f"{f.name}: leader {a}->{b} touches label '{s}' ({d:.1f} px)")
    return out


three_rows(
    "lockkey", FIT, FIT,
    ["1  Substrate collides with the active site", "2  Enzyme–substrate complex forms",
     "3  Products leave; enzyme unchanged"],
    [[(214, 38, "substrate", (210, 34, 154, 34)), (214, 86, "active site", (210, 82, 126, 82)),
      (214, 106, "enzyme", None)],
     [(214, 74, "shapes are", (210, 70, 154, 66)), (214, 88, "complementary", None)],
     [(214, 40, "products", (210, 36, 184, 36)), (214, 82, "active site", (210, 78, 126, 80)),
      (214, 96, "free again", None)]],
    "Lock-and-key model in three stages. 1: a substrate whose shape is complementary to the active site approaches the "
    "enzyme. 2: the substrate fits exactly into the rigid active site, forming an enzyme–substrate complex. 3: two products "
    "leave and the active site is unchanged, ready for another substrate molecule.",
    "Lock-and-key hypothesis: the active site has a fixed shape that is already complementary to the substrate, like a "
    "lock that only one key fits. The enzyme comes out of the reaction unchanged.")

three_rows(
    "induced", LOOSE, FIT,
    ["1  Active site not quite complementary", "2  Active site changes shape to fit",
     "3  Products leave; shape returns"],
    [[(214, 38, "substrate", (210, 34, 154, 34)), (214, 86, "active site", (210, 82, 126, 80)),
      (214, 106, "enzyme", None)],
     [(214, 74, "moulds round", (210, 70, 154, 66)), (214, 88, "substrate;", None),
      (214, 102, "bonds strained", None)],
     [(214, 40, "products", (210, 36, 184, 36)), (214, 82, "active site", (210, 78, 124, 78)),
      (214, 96, "back to its", None), (214, 110, "first shape", None)]],
    "Induced-fit model in three stages. 1: the active site is close to, but not exactly, complementary to the substrate. "
    "2: as the substrate binds, the active site changes shape and moulds closely around it, straining bonds in the "
    "substrate. 3: the products leave and the active site returns to its original shape.",
    "Induced-fit hypothesis: the active site is flexible. Binding of the substrate changes its shape slightly so that it "
    "fits closely, which puts strain on bonds in the substrate. Compare stage 1 and stage 2 with the lock-and-key figure.")

# ---------- Figure 3: energy profile ----------
f = Fig("energy")
f.line([(40, 228), (40, 12)], "ax", "ahm", check=True)
f.line([(36, 224), (330, 224)], "ax", "ahm", check=True)
f.text(48, 20, "energy", "tl")
f.text(330, 242, "progress of reaction", "tl", "end")
react, prod = 150, 196
f.line([(50, react), (110, react)], "ln")
f.line([(240, prod), (320, prod)], "ln")
f.text(52, react + 18, "substrate", "tl")
f.text(320, prod + 18, "products", "tl", "end")
no = bez((110, react), (150, react), (145, 40), (175, 40)) + bez((175, 40), (205, 40), (200, prod), (240, prod))[1:]
yes = bez((110, react), (150, react), (150, 100), (175, 100)) + bez((175, 100), (200, 100), (200, prod), (240, prod))[1:]
f.line(no, "c2 dash")
f.line(yes, "c1")
# activation energy arrows from the substrate level to each peak, with dashed guides to the peaks
f.line([(70, 40), (170, 40)], "ln-m thin dash")
f.line([(92, 100), (170, 100)], "ln-m thin dash")
f.line([(74, react - 2), (74, 44)], "ln", "ah")
f.line([(96, react - 2), (96, 104)], "ln", "ah")
f.text(66, 98, "A", "tl tb", "end")
f.text(88, 128, "B", "tl tb", "end")
f.text(220, 52, "without enzyme", "tl")
f.text(216, 110, "with enzyme", "tl")
figs.append(f.svg((345, 252),
    "Energy profile of a reaction. The substrate starts at a higher energy than the products. The dashed curve, without "
    "enzyme, rises to a high peak; the solid curve, with enzyme, rises to a lower peak. Arrow A is the activation energy "
    "without the enzyme and arrow B, which is shorter, is the activation energy with the enzyme. Both curves end at the "
    "same product energy.",
    "An enzyme lowers the activation energy: A is the activation energy without the enzyme and B, which is smaller, is the activation energy with it, so many more enzyme–substrate collisions "
    "have enough energy to react. The substrate and product energies, and so the overall energy change, are the same with "
    "or without the enzyme."))
problems.extend(f.check())

# ---------- Figure 4: catalase apparatus ----------
f = Fig("catalase")
f.rect(18, 112, 132, 92, "fm s-acc sw2", 6)                     # water bath
f.poly([(76, 74), (76, 102), (40, 190), (130, 190), (94, 102), (94, 74)], "fp ln", closed=False)
f.poly([(54.3, 156), (115.7, 156), (130, 190), (40, 190)], "f2 s-acc2 sw2")   # liquid in the flask
f.rect(72, 62, 26, 12, "fi")                                       # bung
f.line([(85, 62), (85, 40), (190, 40)], "ln")                     # delivery tube
f.rect(190, 28, 110, 24, "fp ln")                                  # syringe barrel
f.rect(244, 37, 92, 6, "fm s-acc sw2")                             # plunger rod
f.line([(244, 30), (244, 50)], "ln thick")                          # plunger head
for k in range(1, 6):
    f.line([(190 + k * 9, 28), (190 + k * 9, 34)], "ln-m thin", check=False)
f.text(245, 18, "gas syringe", "tl", "middle")
f.text(200, 72, "oxygen", "tl")
f.line([(222, 61), (222, 46)], LEAD, check=False)
f.text(104, 58, "bung", "tl")
f.text(160, 134, "hydrogen peroxide", "tl")
f.text(160, 150, "solution + yeast", "tl")
f.text(160, 166, "(contains catalase)", "tl")
f.line([(156, 150), (110, 174)], LEAD, check=False)
f.text(160, 198, "water bath, 30 °C", "tl")
problems.extend(lead_check(f, (156, 150), (110, 174)))
figs.append(f.svg((345, 215),
    "Apparatus: a conical flask in a water bath at 30 °C holds hydrogen peroxide solution and yeast, which "
    "contains catalase. A bung and delivery tube lead from the flask to a gas syringe, where the oxygen collects.",
    "Measuring the rate of product formation: the volume of oxygen in the gas syringe is read at regular intervals. An "
    "upturned measuring cylinder full of water in a trough can replace the gas syringe."))
problems.extend(f.check())

# ---------- Figure 5: colorimeter ----------
f = Fig("colorimeter")
f.rect(10, 8, 330, 92, "fm s-acc sw2", 8)                          # instrument case
f.circle(30, 54, 11, "fh s-mute sw2")                               # lamp
f.line([(44, 54), (80, 54)], "c4 dash", "ah")
f.rect(86, 34, 8, 40, "f2 s-acc2 sw2")                              # filter
f.line([(98, 54), (146, 54)], "c4 dash", "ah")
f.rect(150, 30, 30, 48, "fp ln")                                    # cuvette
f.rect(153, 44, 24, 32, "f2 s-acc2 sw2")                            # sample
f.line([(184, 54), (213, 54)], "c4 dash", "ah")
f.rect(219, 38, 18, 32, "fi")                                       # detector
f.line([(241, 54), (268, 54)], "ln")
f.rect(268, 34, 62, 40, "fp ln", 4)                                 # meter
f.text(299, 59, "0.45", "tl tb", "middle")
for x, a, b in [(30, "white", "light"), (90, "coloured", "filter"), (165, "cuvette", "+ sample"),
                (228, "light", "detector"), (300, "absorbance", "reading")]:
    f.text(x, 122, a, "tl", "middle")
    f.text(x, 136, b, "tl", "middle")
figs.append(f.svg((350, 146),
    "Colorimeter: white light from a lamp passes through a coloured filter, then through the sample in a cuvette, and "
    "reaches a light detector. A meter shows the absorbance, here 0.45.",
    "Inside a colorimeter. The filter lets through the colour of light that the sample absorbs most. The more coloured "
    "substance in the cuvette, the less light reaches the detector and the higher the absorbance."))
problems.extend(f.check())

for s in figs:
    print(s)
    print()
print("\n".join(problems) if problems else "clearance ok", file=sys.stderr)
