# data/mk_fig_p16.py: builds the hand SVG figures of P16 (chem.org.arenes, chem.org.phenol) and checks label clearances.
# Run: py data/mk_fig_p16.py   (prints each figure and any clash; the figures are pasted into the chapters).
import math, sys

def f(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s

class Fig:
    def __init__(self, name):
        self.name = name; self.el = []; self.texts = []; self.segs = []; self.pts = []
    def text(self, x, y, s, anchor="start", cls="tl", extra=""):
        a = {"start": "", "middle": " tc", "end": ""}[anchor]
        w = 7 * len(s)
        x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
        self.texts.append((x0, y - 10, x0 + w, y + 3, s))
        self.pts += [(x0, y - 10), (x0 + w, y + 3)]
        c = cls + (" tc" if anchor == "middle" else "")
        e = f' text-anchor="end"' if anchor == "end" else ""
        self.el.append(f'<text class="{c}" x="{f(x)}" y="{f(y)}"{e}>{s}</text>')
    def line(self, pts, cls="ln thick", closed=False, marker=None, ok=False):
        d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + ("Z" if closed else "")
        m = f' marker-end="url(#{marker})"' if marker else ""
        self.el.append(f'<path class="{cls}" d="{d}"{m}/>')
        seq = pts + ([pts[0]] if closed else [])
        for (a, b) in zip(seq, seq[1:]):
            self.segs.append((a, b, ok))
        self.pts += pts
    def raw(self, s): self.el.append(s)
    def curl(self, p0, c, p1, cls="c1 sw2", marker="ahs-red"):
        self.el.append(f'<path class="{cls}" d="M{f(p0[0])} {f(p0[1])}Q{f(c[0])} {f(c[1])} {f(p1[0])} {f(p1[1])}" marker-end="url(#{marker})"/>')
        prev = p0
        for i in range(1, 21):
            t = i / 20
            q = ((1-t)**2*p0[0]+2*t*(1-t)*c[0]+t*t*p1[0], (1-t)**2*p0[1]+2*t*(1-t)*c[1]+t*t*p1[1])
            self.segs.append((prev, q, "curl")); prev = q
        self.pts += [p0, p1]
        L = math.hypot(p1[0]-p0[0], p1[1]-p0[1])
        if L < 30: print(f"  WARN {self.name}: curly arrow only {L:.0f} px")
    def dots(self, cx, cy):
        self.el.append(f'<circle class="fi" cx="{f(cx-3)}" cy="{f(cy)}" r="1.7"/><circle class="fi" cx="{f(cx+3)}" cy="{f(cy)}" r="1.7"/>')
    def check(self):
        for i, a in enumerate(self.texts):
            for b in self.texts[i+1:]:
                if a[0] < b[2] + 3 and b[0] < a[2] + 3 and a[1] < b[3] + 3 and b[1] < a[3] + 3:
                    print(f"  CLASH {self.name}: text '{a[4]}' and '{b[4]}'")
        for t in self.texts:
            for (p, q, ok) in self.segs:
                d = rect_seg_dist(t[:4], p, q)
                lim = 3 if ok == "curl" else 3.5
                if d < lim and not (ok is True):
                    print(f"  NEAR {self.name}: text '{t[4]}' {d:.1f}px from a {'curly arrow' if ok == 'curl' else 'line'} {tuple(round(v) for v in p)}-{tuple(round(v) for v in q)}")
    def svg(self, cls, aria, cap, pad=15):
        xs = [p[0] for p in self.pts]; ys = [p[1] for p in self.pts]
        x0, y0 = math.floor(min(xs) - pad), math.floor(min(ys) - pad)
        x1, y1 = math.ceil(max(xs) + pad), math.ceil(max(ys) + pad)
        if x1 - x0 < 300:
            e = (300 - (x1 - x0)) / 2; x0 = math.floor(x0 - e); x1 = math.ceil(x1 + e)
        print(f"  {self.name}: viewBox {x0} {y0} {x1-x0} {y1-y0}")
        return (f'<figure class="{cls}"><svg viewBox="{x0} {y0} {x1-x0} {y1-y0}" role="img" aria-label="{aria}">'
                + "".join(self.el) + f'</svg><figcaption>{cap}</figcaption></figure>')

def rect_seg_dist(r, p, q):
    x0, y0, x1, y1 = r
    best = 1e9
    n = max(2, int(math.hypot(q[0]-p[0], q[1]-p[1]) / 2))
    for i in range(n + 1):
        t = i / n
        x = p[0] + (q[0]-p[0]) * t; y = p[1] + (q[1]-p[1]) * t
        dx = max(x0 - x, 0, x - x1); dy = max(y0 - y, 0, y - y1)
        best = min(best, math.hypot(dx, dy))
    return best

R = 28; RC = 17
def verts(cx, cy, flat=False, r=R):
    angs = [0, 60, 120, 180, 240, 300] if flat else [90, 30, -30, -90, -150, 150]
    return [(cx + r*math.cos(math.radians(a)), cy - r*math.sin(math.radians(a))) for a in angs]

def ring(F, cx, cy, flat=False, circle=True, kekule=False):
    v = verts(cx, cy, flat)
    F.line(v, "ln thick", closed=True, ok=True)
    if circle:
        F.raw(f'<circle class="ln" cx="{f(cx)}" cy="{f(cy)}" r="{RC}"/>')
    if kekule:
        # three inner parallel lines for the double bonds 1-2, 3-4, 5-6 (indices 0-1, 2-3, 4-5)
        for (i, j) in [(0, 1), (2, 3), (4, 5)]:
            a, b = v[i], v[j]
            mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
            ux, uy = (b[0]-a[0]), (b[1]-a[1]); L = math.hypot(ux, uy); ux /= L; uy /= L
            nx, ny = (cx-mx), (cy-my); nl = math.hypot(nx, ny); nx /= nl; ny /= nl
            p = (a[0]+ux*5+nx*5, a[1]+uy*5+ny*5); q = (b[0]-ux*5+nx*5, b[1]-uy*5+ny*5)
            F.line([p, q], "ln thick", ok=True)
    return v

def sub(F, v, idx, cx, cy, label, bond=18, gap=4, flat=False, bondcls="ln thick"):
    """Substituent label on vertex idx, radially outwards."""
    x, y = v[idx]
    dx, dy = x - cx, y - cy; L = math.hypot(dx, dy); dx /= L; dy /= L
    ex, ey = x + dx*bond, y + dy*bond
    F.line([(x, y), (ex, ey)], bondcls, ok=True)
    place_label(F, ex, ey, dx, dy, label, gap)
    return ex, ey

def place_label(F, ex, ey, dx, dy, label, gap=4):
    n = len(label)
    if abs(dy) > 0.75:      # above or below
        if dy < 0: F.text(ex, ey - gap, label, "middle")
        else: F.text(ex, ey + gap + 10, label, "middle")
    elif dx > 0:
        F.text(ex + gap, ey + 4, label, "start")
    else:
        F.text(ex - gap, ey + 4, label, "end")

# ---------------------------------------------------------------- arenes: naming figure
def fig_names():
    F = Fig("names")
    cw = 100
    rows = [
        [("methylbenzene", ["CH₃"], [0]), ("chlorobenzene", ["Cl"], [0]), ("nitrobenzene", ["NO₂"], [0])],
        [("phenol", ["OH"], [0]), ("phenylamine", ["NH₂"], [0]), ("benzoic acid", ["COOH"], [0])],
        [("2,4,6-tribromophenol", ["OH", "Br", "Br", "Br"], [0, 1, 3, 5]), ("1-phenylethanone", None, None),
         ("3-nitrobenzoic acid", ["COOH", "NO₂"], [0, 2])],
    ]
    names2 = {"1-phenylethanone": ("1-phenyl-", "ethanone"), "3-nitrobenzoic acid": ("3-nitro-", "benzoic acid"),
              "2,4,6-tribromophenol": ("2,4,6-tribromo-", "phenol")}
    ys = [60, 60 + 125, 60 + 125 + 135]
    for r, row in enumerate(rows):
        cy = ys[r]
        for c, (name, labs, idxs) in enumerate(row):
            cx = 62 + c * cw
            v = ring(F, cx, cy)
            if labs is None:
                # 1-phenylethanone: C(=O)CH3 on the top vertex
                tx, ty = v[0]
                cxp, cyp = tx, ty - 20
                F.line([(tx, ty), (cxp, cyp + 0)], "ln thick", ok=True)
                # O at 150 deg, CH3 at 30 deg from the carbonyl carbon, bonds 20 px
                ox, oy = cxp - 20*math.cos(math.radians(30)), cyp - 20*math.sin(math.radians(30))
                mx, my = cxp + 20*math.cos(math.radians(30)), cyp - 20*math.sin(math.radians(30))
                # double bond C=O: two parallel lines 5 px apart, perpendicular offset
                ux, uy = (ox-cxp), (oy-cyp); L = math.hypot(ux, uy); ux/=L; uy/=L
                nx, ny = -uy*2.5, ux*2.5
                F.line([(cxp+nx+ux*2, cyp+ny+uy*2), (cxp+ux*(L-6)*1+nx+ux*0+ux*0+nx*0, cyp+uy*(L-6)+ny)], "ln thick", ok=True)
                F.line([(cxp-nx+ux*2, cyp-ny+uy*2), (cxp+ux*(L-6)-nx, cyp+uy*(L-6)-ny)], "ln thick", ok=True)
                F.text(ox, oy - 1, "O", "middle")
                F.line([(cxp, cyp), (mx - 2, my + 1)], "ln thick", ok=True)
                F.text(mx + 2, my - 1, "CH₃", "start")
                bottom = cy + R
            else:
                for lab, i in zip(labs, idxs):
                    sub(F, v, i, cx, cy, lab, bond=16)
                bottom = cy + R + (18 + 14 if 3 in idxs else 0)
            n1, n2 = names2.get(name, (name, None))
            ny0 = ys[r] + R + 52 if r == 2 else ys[r] + R + 28
            if r == 2:
                ny0 = cy + R + 18 + 14 + 22
            F.text(cx, ny0, n1, "middle", "tl")
            if n2: F.text(cx, ny0 + 16, n2, "middle", "tl")
    F.check()
    return F.svg("fig small", "Skeletal formulas of nine benzene derivatives: methylbenzene, chlorobenzene, nitrobenzene, phenol, phenylamine, benzoic acid, 1-phenylethanone, 3-nitrobenzoic acid and 2,4,6-tribromophenol",
                 "Nine aromatic compounds. Each ring is a hexagon with a circle for the delocalised electrons; the carbon holding the main group is number 1, and the others are numbered round the ring.")

# ---------------------------------------------------------------- arenes: Kekule v modern
def fig_kekule():
    F = Fig("kekule")
    v = ring(F, 85, 80, circle=False, kekule=True)
    F.text(85, 135, "Kekulé model", "middle")
    F.text(85, 153, "3 × C=C, 3 × C–C", "middle")
    v2 = ring(F, 255, 80, circle=True)
    F.text(255, 135, "modern model", "middle")
    F.text(255, 153, "6 equal bonds", "middle")
    F.line([(135, 80), (205, 80)], "ln-m thin dash", ok=True)
    F.text(170, 76, "not", "middle")
    F.check()
    return F.svg("fig small", "Two drawings of benzene: the Kekulé model with alternating double bonds, and the modern model with a circle in the ring",
                 "Two ways to draw benzene. The Kekulé drawing implies three short C=C bonds and three longer C–C bonds; every bond in real benzene is the same length, so the circle is used.")

# ---------------------------------------------------------------- pi system seen from a tilt
def fig_pi(oxygen=False):
    F = Fig("pi_o" if oxygen else "pi")
    cx, cy = 130 if oxygen else 170, 112
    a, b = 70, 26
    LX, LY, LO = 13, 16, 20
    pts = [(cx + a*math.cos(math.radians(t)), cy + b*math.sin(math.radians(t))) for t in (0, 60, 120, 180, 240, 300)]
    order = sorted(range(6), key=lambda i: pts[i][1])
    for i in order:
        x, y = pts[i]
        F.raw(f'<ellipse class="fa" cx="{f(x)}" cy="{f(y-LO)}" rx="{LX}" ry="{LY}"/>')
        F.raw(f'<ellipse class="fa" cx="{f(x)}" cy="{f(y+LO)}" rx="{LX}" ry="{LY}"/>')
        F.pts += [(x-LX, y-LO-LY), (x+LX, y+LO+LY)]
    F.line(pts, "ln thick", closed=True, ok=True)
    if oxygen:
        ox, oy = pts[0][0] + 56, pts[0][1]
        F.line([pts[0], (ox - 12, oy)], "ln thick", ok=True)
        F.raw(f'<ellipse class="fa2" cx="{f(ox)}" cy="{f(oy-24)}" rx="{LX}" ry="{LY}"/>')
        F.raw(f'<ellipse class="fa2" cx="{f(ox)}" cy="{f(oy+24)}" rx="{LX}" ry="{LY}"/>')
        F.text(ox, oy + 4, "OH", "middle")
        F.dots(ox, oy - 24)
        F.pts += [(ox-LX, oy-24-LY), (ox+LX, oy+24+LY)]
        F.text(ox, oy + 62, "lone pair in a", "middle")
        F.text(ox, oy + 78, "p orbital on O", "middle")
    F.text(cx, cy - 68, "π electrons above", "middle")
    F.text(cx, cy + 80, "π electrons below", "middle")
    F.check()
    cap = ("Benzene seen from slightly above. Each carbon has one p orbital at right angles to the flat ring; neighbouring p orbitals overlap sideways, so the π electrons form one ring above and one below the plane of the σ bonds."
           if not oxygen else
           "Phenol seen from slightly above. The p orbital on oxygen that holds a lone pair is parallel to the ring's p orbitals, so it overlaps sideways with them and the lone pair joins the delocalised π system.")
    aria = ("Six p orbitals above and below a flat hexagonal ring of carbon atoms overlapping to form a delocalised pi system" if not oxygen else
            "The p orbital of the oxygen atom of phenol, holding a lone pair, overlapping with the six p orbitals of the benzene ring")
    return F.svg("fig small", aria, cap)

# ---------------------------------------------------------------- mechanism of nitration (stacked)
def fig_mech(E="NO₂", Ep="NO₂⁺", name="nitration"):
    F = Fig("mech_" + name)
    cx = 80
    # row A
    ya = 66
    ring(F, cx, ya)
    sx, sy = cx + RC*math.cos(math.radians(30)), ya - RC*math.sin(math.radians(30))
    tx = cx + 82
    F.text(tx, ya + 5, Ep, "start")
    F.curl((sx, sy), (cx + 52, ya - 38), (tx - 5, ya - 3))
    F.text(cx + 40, ya + 5, "+", "start")
    # arrow down
    F.line([(cx, ya + R + 10), (cx, ya + R + 44)], "ln", marker="ah", ok=True)
    F.text(cx + 12, ya + R + 31, "step 1 (slow)", "start")
    # row B: intermediate
    yb = ya + R + 44 + 12 + 40 + 20 + 28
    T = (cx, yb - R)
    v = verts(cx, yb)
    F.line([v[0], v[1], v[2], v[3], v[4], v[5]], "ln thick", closed=True, ok=True)
    a30 = (cx + RC*math.cos(math.radians(30)), yb - RC*math.sin(math.radians(30)))
    a150 = (cx + RC*math.cos(math.radians(150)), yb - RC*math.sin(math.radians(150)))
    F.raw(f'<path class="ln" d="M{f(a30[0])} {f(a30[1])}A{RC} {RC} 0 1 1 {f(a150[0])} {f(a150[1])}"/>')
    F.text(cx, yb + 5, "+", "middle")
    bl = 18
    hx, hy = T[0] - bl*math.cos(math.radians(30)), T[1] - bl*math.sin(math.radians(30))
    ex_, ey_ = T[0] + bl*math.cos(math.radians(30)), T[1] - bl*math.sin(math.radians(30))
    F.line([T, (hx, hy)], "ln thick", ok=True)
    F.line([T, (ex_, ey_)], "ln thick", ok=True)
    F.text(hx - 3, hy + 2, "H", "end")
    F.text(ex_ + 3, ey_ + 2, E, "start")
    mid = ((T[0] + hx)/2, (T[1] + hy)/2)
    F.curl((mid[0] + 0.5, mid[1] + 1), (cx - 38, yb - 22), (cx - 10, yb + 4))
    F.text(cx + 40, yb + 5, "intermediate", "start")
    # arrow down
    F.line([(cx, yb + R + 10), (cx, yb + R + 44)], "ln", marker="ah", ok=True)
    F.text(cx + 12, yb + R + 31, "step 2 (fast)", "start")
    # row C: product
    yc = yb + R + 44 + 12 + 40 + 20 + 28 - 12
    vc = ring(F, cx, yc)
    sub(F, vc, 0, cx, yc, E)
    F.text(cx + 44, yc + 5, "+ H⁺", "start")
    F.check()
    return F.svg("fig small", f"Electrophilic substitution of benzene: the delocalised ring donates a pair of electrons to the electrophile {Ep}, giving an intermediate cation with hydrogen and {E} on one carbon; the C–H bond electrons then return to the ring, releasing H+ and giving the substituted benzene",
                 f"Electrophilic substitution of benzene by {Ep}. Step 1: a pair of electrons from the delocalised ring forms a bond to the electrophile; the intermediate has a partial ring (the arc) and a positive charge. Step 2: the electrons of the C–H bond return to the ring and H⁺ leaves.")

# ---------------------------------------------------------------- phenol: where electron density is raised
def fig_delta():
    F = Fig("delta")
    cx, cy = 100, 80
    v = ring(F, cx, cy)
    sub(F, v, 0, cx, cy, "OH")
    # delta- labels outside the vertices 2, 4, 6 (indices 1, 3, 5)
    for i, (dx, dy, anchor) in {1: (1, 0, "start"), 3: (0, 1, "middle"), 5: (-1, 0, "end")}.items():
        x, y = v[i]
        if anchor == "start": F.text(x + 6, y - 4, "δ−", "start", "tl ta")
        elif anchor == "end": F.text(x - 6, y - 4, "δ−", "end", "tl ta")
        else: F.text(x, y + 22, "δ−", "middle", "tl ta")
    F.text(100, 140, "ring more electron-rich", "middle") if False else None
    F.check()
    return F.svg("fig small", "Phenol with the OH carbon numbered 1 and delta-minus marked at positions 2, 4 and 6 of the ring",
                 "In phenol the oxygen lone pair raises the electron density at carbons 2, 4 and 6 (the positions next to and opposite the OH group), so electrophiles attack there.")

# ---------------------------------------------------------------- phenol: azo coupling scheme
def fig_azo():
    F = Fig("azo")
    # Row 1: ring-N≡N+   +   ring-OH  (flat hexagons, para substituents)
    y1 = 56
    c1 = 50
    v = ring(F, c1, y1, flat=True)
    F.line([v[0], (v[0][0] + 14, y1)], "ln thick", ok=True)
    F.text(v[0][0] + 18, y1 + 4, "N≡N⁺", "start")
    F.text(v[0][0] + 18 + 7*4 + 8, y1 + 4, "+", "start")
    c2 = v[0][0] + 18 + 28 + 8 + 20 + 28
    v2 = ring(F, c2, y1, flat=True)
    F.line([v2[0], (v2[0][0] + 14, y1)], "ln thick", ok=True)
    F.text(v2[0][0] + 18, y1 + 4, "OH", "start")
    F.text(c1, y1 + 56, "benzenediazonium ion", "middle")
    F.text(c2 + 6, y1 + 56, "phenol", "middle")
    # arrow down with label
    ya = y1 + 80
    F.line([(c1 + 40, ya), (c1 + 40, ya + 38)], "ln", marker="ah", ok=True)
    F.text(c1 + 54, ya + 18, "NaOH(aq), below 10 °C", "start")
    # Row 2: product ring-N=N-ring-OH
    y2 = ya + 38 + 12 + 34
    d1 = 50
    w1 = ring(F, d1, y2, flat=True)
    nx1 = w1[0][0] + 14
    F.line([w1[0], (nx1, y2)], "ln thick", ok=True)
    F.text(nx1 + 3, y2 + 4, "N", "start")
    F.line([(nx1 + 13, y2 - 2.5), (nx1 + 27, y2 - 2.5)], "ln thick", ok=True)
    F.line([(nx1 + 13, y2 + 2.5), (nx1 + 27, y2 + 2.5)], "ln thick", ok=True)
    F.text(nx1 + 30, y2 + 4, "N", "start")
    d2 = nx1 + 48 + 28
    w2 = ring(F, d2, y2, flat=True)
    F.line([(nx1 + 42, y2), w2[3]], "ln thick", ok=True)
    F.line([w2[0], (w2[0][0] + 14, y2)], "ln thick", ok=True)
    F.text(w2[0][0] + 18, y2 + 4, "OH", "start")
    F.text(d2 - 10, y2 + 52, "4-hydroxyphenylazobenzene (an azo compound)", "middle") if False else None
    F.text(d2 - 40, y2 + 52, "an azo compound: Ar–N=N–Ar′", "middle")
    F.check()
    return F.svg("fig small", "Azo coupling: benzenediazonium ion reacts with phenol in sodium hydroxide solution below 10 degrees Celsius to give an azo compound in which the N=N group joins the two rings, with the OH group opposite it",
                 "Azo coupling. The diazonium ion attacks the ring of phenol at the position opposite the OH group (the 4-position), and the two rings end up joined by the N=N (azo) group.")

# ---------------------------------------------------------------- 2-naphthol
def fig_naph():
    F = Fig("naph")
    cx1, cy = 60, 70
    cx2 = cx1 + 2 * R * math.cos(math.radians(30))
    v1 = ring(F, cx1, cy); v2 = ring(F, cx2, cy)
    sub(F, v2, 1, cx2, cy, "OH")
    x, y = v2[0]
    F.text(x + 8, y - 6, "1", "start", "tl ta")
    F.text(cx2 + 70, cy + 4, "2-naphthol", "start")
    F.check()
    return F.svg("fig small", "Skeletal formula of 2-naphthol, two fused benzene rings with an OH group on carbon 2 and carbon 1 marked next to it",
                 "2-Naphthol: two fused rings with OH on carbon 2. The diazonium ion attacks carbon 1, next to the OH group.")

if __name__ == "__main__":
    out = {}
    for name, fn in [("names", fig_names), ("kekule", fig_kekule), ("pi", fig_pi), ("pi_o", lambda: fig_pi(True)),
                     ("mech", fig_mech), ("delta", fig_delta), ("azo", fig_azo), ("naph", fig_naph)]:
        print(name)
        out[name] = fn()
    import json
    with open("data/fig_p16.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
