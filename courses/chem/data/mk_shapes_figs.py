# data/mk_shapes_figs.py: plans the SVG figures of chem.shapes and checks label clearance.
# Run: py data/mk_shapes_figs.py   (prints each figure's SVG and any clearance problems)
import math, sys
sys.stdout.reconfigure(encoding='utf-8')

class Fig:
    def __init__(self, name):
        self.name = name
        self.out = []          # svg element strings
        self.segs = []         # (x1,y1,x2,y2,tag) line segments (for clearance)
        self.boxes = []        # (x0,y0,x1,y1,label)
        self.circles = []

    def f(self, v):
        s = f"{v:.1f}"
        return s[:-2] if s.endswith('.0') else s

    def text(self, x, y, s, cls='tl tc', anchor=None):
        w = 7.0 * len(s)
        if 'tc' in cls: x0 = x - w / 2
        elif anchor == 'end': x0 = x - w
        else: x0 = x
        self.boxes.append((x0, y - 10, x0 + w, y + 3, s))
        a = ' text-anchor="end"' if anchor == 'end' else ''
        self.out.append(f'<text class="{cls}" x="{self.f(x)}" y="{self.f(y)}"{a}>{s}</text>')

    def label(self, cx, cc, s, cls='tl tc'):
        """atom label centred on (cx, cc) (cc = visual centre); baseline = cc + 5"""
        self.text(cx, cc + 3.5, s, cls)
        return (cx, cc, 3.5 * len(s) + 5, 6.5 + 5)   # clip half-width/height incl. 5 px gap

    def line(self, p, q, cls='ln thick', marker=None, rect_a=None, rect_b=None, tag=''):
        (x1, y1), (x2, y2) = p, q
        def clip(a, b, rect):
            if rect is None: return a
            cx, cy, hw, hh = rect
            dx, dy = b[0] - a[0], b[1] - a[1]
            # find t where segment leaves rect centred at a (a == rect centre)
            ts = []
            if dx: ts.append(hw / abs(dx))
            if dy: ts.append(hh / abs(dy))
            t = min(ts)
            return (a[0] + dx * t, a[1] + dy * t)
        a = clip((x1, y1), (x2, y2), rect_a)
        b = clip((x2, y2), (x1, y1), rect_b)
        m = f' marker-end="url(#{marker})"' if marker else ''
        self.out.append(f'<path class="{cls}" d="M{self.f(a[0])} {self.f(a[1])}L{self.f(b[0])} {self.f(b[1])}"{m}/>')
        self.segs.append((a[0], a[1], b[0], b[1], tag or cls))
        return a, b

    def wedge(self, p, q, rect_a=None, rect_b=None, w=4.0):
        (x1, y1), (x2, y2) = p, q
        def clip(a, b, rect):
            cx, cy, hw, hh = rect
            dx, dy = b[0] - a[0], b[1] - a[1]
            ts = []
            if dx: ts.append(hw / abs(dx))
            if dy: ts.append(hh / abs(dy))
            t = min(ts)
            return (a[0] + dx * t, a[1] + dy * t)
        a = clip(p, q, rect_a); b = clip(q, p, (rect_b[0], rect_b[1], rect_b[2] + 3, rect_b[3] + 3))
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy)
        nx, ny = -dy / L * w, dx / L * w
        pts = [a, (b[0] + nx, b[1] + ny), (b[0] - nx, b[1] - ny)]
        self.out.append('<path class="fi" d="M%s %sL%s %sL%s %sZ"/>' % tuple(self.f(v) for pt in pts for v in pt))
        self.segs.append((a[0], a[1], b[0] + nx, b[1] + ny, 'wedge'))
        self.segs.append((a[0], a[1], b[0] - nx, b[1] - ny, 'wedge'))
        self.segs.append((b[0] + nx, b[1] + ny, b[0] - nx, b[1] - ny, 'wedge'))

    def dots(self, x, y, horizontal=True):
        d = 3.0
        for s in (-d, d):
            cx, cy = (x + s, y) if horizontal else (x, y + s)
            self.out.append(f'<circle class="fi" cx="{self.f(cx)}" cy="{self.f(cy)}" r="1.7"/>')
            self.circles.append((cx, cy, 1.7))

    def raw(self, s): self.out.append(s)

    def check(self, clearance=4.0):
        problems = []
        def dist_seg_box(seg, box):
            x1, y1, x2, y2, _ = seg
            n = max(2, int(math.hypot(x2 - x1, y2 - y1) / 0.5))
            best = 1e9
            for i in range(n + 1):
                t = i / n
                px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
                dx = max(box[0] - px, 0, px - box[2]); dy = max(box[1] - py, 0, py - box[3])
                best = min(best, math.hypot(dx, dy))
            return best
        for b in self.boxes:
            for s in self.segs:
                d = dist_seg_box(s, b)
                if d < clearance - 1e-6:
                    problems.append(f"{self.name}: label '{b[4]}' is {d:.1f}px from a {s[4]} segment ({s[0]:.0f},{s[1]:.0f})-({s[2]:.0f},{s[3]:.0f})")
        for i, a in enumerate(self.boxes):
            for b in self.boxes[i + 1:]:
                gx = max(a[0] - b[2], b[0] - a[2]); gy = max(a[1] - b[3], b[1] - a[3])
                if max(gx, gy) < clearance:
                    problems.append(f"{self.name}: labels '{a[4]}' and '{b[4]}' are {max(gx, gy):.1f}px apart")
        for c in self.circles:
            for b in self.boxes:
                dx = max(b[0] - c[0], 0, c[0] - b[2]); dy = max(b[1] - c[1], 0, c[1] - b[3])
                if math.hypot(dx, dy) < 3:
                    problems.append(f"{self.name}: dot ({c[0]:.0f},{c[1]:.0f}) touches label '{b[4]}'")
        return problems

    def bounds(self):
        xs = []; ys = []
        for b in self.boxes: xs += [b[0], b[2]]; ys += [b[1], b[3]]
        for s in self.segs: xs += [s[0], s[2]]; ys += [s[1], s[3]]
        for c in self.circles: xs += [c[0]]; ys += [c[1]]
        return min(xs), min(ys), max(xs), max(ys)

    def svg(self, alt, cap, cls='fig', pad=15):
        x0, y0, x1, y1 = self.bounds()
        x0 = math.floor(x0 - pad); y0 = math.floor(y0 - pad); x1 = math.ceil(x1 + pad); y1 = math.ceil(y1 + pad)
        if cls == 'fig small' and x1 - x0 < 300:
            extra = (300 - (x1 - x0)) / 2; x0 = math.floor(x0 - extra); x1 = math.ceil(x1 + extra)
        return (f'<figure class="{cls}"><svg viewBox="{x0} {y0} {x1 - x0} {y1 - y0}" role="img" aria-label="{alt}">'
                + ''.join(self.out) + f'</svg><figcaption>{cap}</figcaption></figure>'), (x1 - x0, y1 - y0)

def pol(cx, cy, r, deg):
    """screen point at angle deg (0 = right, 90 = up) distance r"""
    a = math.radians(deg)
    return (cx + r * math.cos(a), cy - r * math.sin(a))

# ============ FIGURE 1: five shapes ============
def fig_shapes():
    F = Fig('shapes')
    cy = 95; L = 52
    names = [('CO₂', 'linear'), ('BF₃', 'trigonal planar'), ('CH₄', 'tetrahedral'), ('NH₃', 'pyramidal'), ('H₂O', 'non-linear')]
    xs = [64, 192, 320, 448, 576]
    # 1 CO2
    cx = xs[0]
    rc = F.label(cx, cy, 'C'); ro1 = F.label(cx - 56, cy, 'O'); ro2 = F.label(cx + 56, cy, 'O')
    for sgn, ro in ((-1, ro1), (1, ro2)):
        for off in (-2.5, 2.5):
            F.line((cx, cy + off), (cx + sgn * 56, cy + off), rect_a=rc, rect_b=ro)
    F.text(cx, cy - 20, '180°', 'tl tc ta')
    # 2 BF3
    cx = xs[1]
    rb = F.label(cx, cy, 'B')
    for ang in (90, 210, 330):
        px, py = pol(cx, cy, L, ang)
        rf = F.label(px, py, 'F')
        F.line((cx, cy), (px, py), rect_a=rb, rect_b=rf)
    F.text(cx, cy + 44, '120°', 'tl tc ta')
    # 3 CH4: plain up, plain down-left, wedge lower-right, dash upper-right
    cx = xs[2]
    rc = F.label(cx, cy, 'C')
    spec = [(90, 'plain'), (210, 'plain'), (322, 'wedge'), (28, 'dash')]
    for ang, kind in spec:
        px, py = pol(cx, cy, L, ang)
        rh = F.label(px, py, 'H')
        if kind == 'plain': F.line((cx, cy), (px, py), rect_a=rc, rect_b=rh)
        elif kind == 'wedge': F.wedge((cx, cy), (px, py), rc, rh)
        else: F.line((cx, cy), (px, py), cls='ln dash thick', rect_a=rc, rect_b=rh)
    F.text(cx - 6, cy + 44, '109.5°', 'tl tc ta')
    # 4 NH3: lone pair above, plain down-left, wedge down-right, dash right
    cx = xs[3]
    rn = F.label(cx, cy, 'N')
    F.dots(cx, cy - 16)
    for ang, kind in [(212, 'plain'), (318, 'wedge'), (22, 'dash')]:
        px, py = pol(cx, cy, L, ang)
        rh = F.label(px, py, 'H')
        if kind == 'plain': F.line((cx, cy), (px, py), rect_a=rn, rect_b=rh)
        elif kind == 'wedge': F.wedge((cx, cy), (px, py), rn, rh)
        else: F.line((cx, cy), (px, py), cls='ln dash thick', rect_a=rn, rect_b=rh)
    F.text(cx - 2, cy + 44, '107°', 'tl tc ta')
    # 5 H2O: two lone pairs above, two bonds down
    cx = xs[4]
    ro = F.label(cx, cy - 6, 'O')
    F.dots(cx - 14, cy - 22); F.dots(cx + 14, cy - 22)
    for sgn in (-1, 1):
        px, py = pol(cx, cy - 6, L - 4, 270 + sgn * 52.25)
        rh = F.label(px, py, 'H')
        F.line((cx, cy - 6), (px, py), rect_a=ro, rect_b=rh)
    F.text(cx, cy + 44, '104.5°', 'tl tc ta')
    for x, (n, s) in zip(xs, names):
        F.text(x, 172, n, 'tl tc'); F.text(x, 190, s, 'tl tc ta')
    return F

# ============ FIGURE 2: PF5 and SF6 ============
def fig_five_six():
    F = Fig('five_six')
    cy = 100; L = 52
    # PF5
    cx = 110
    rp = F.label(cx, cy, 'P')
    parts = [(90, 'plain'), (270, 'plain'), (180, 'plain'), (330, 'wedge'), (30, 'dash')]
    for ang, kind in parts:
        px, py = pol(cx, cy, L, ang)
        rf = F.label(px, py, 'F')
        if kind == 'plain': F.line((cx, cy), (px, py), rect_a=rp, rect_b=rf)
        elif kind == 'wedge': F.wedge((cx, cy), (px, py), rp, rf)
        else: F.line((cx, cy), (px, py), cls='ln dash thick', rect_a=rp, rect_b=rf)
    F.text(cx - 6, 190, 'PF₅', 'tl tc'); F.text(cx - 6, 208, 'trigonal bipyramidal', 'tl tc ta')
    # key list at right of PF5
    kx = 185
    F.text(kx, 66, '180°: axial to axial', 'tl')
    F.text(kx, 90, '120°: equatorial pair', 'tl')
    F.text(kx, 114, '90°: axial–equatorial', 'tl')
    # SF6
    cx = 420
    rs = F.label(cx, cy, 'S')
    parts = [(90, 'plain'), (270, 'plain'), (180, 'plain'), (0, 'plain'), (222, 'wedge'), (42, 'dash')]
    for ang, kind in parts:
        d = L if kind == 'plain' else L - 6
        px, py = pol(cx, cy, d, ang)
        rf = F.label(px, py, 'F')
        if kind == 'plain': F.line((cx, cy), (px, py), rect_a=rs, rect_b=rf)
        elif kind == 'wedge': F.wedge((cx, cy), (px, py), rs, rf)
        else: F.line((cx, cy), (px, py), cls='ln dash thick', rect_a=rs, rect_b=rf)
    F.text(cx, 190, 'SF₆', 'tl tc'); F.text(cx, 208, 'octahedral', 'tl tc ta')
    F.text(cx + 85, 66, '90°: adjacent F', 'tl'); F.text(cx + 85, 90, '180°: opposite F', 'tl')
    return F

# ============ FIGURE 3: dipoles ============
def dip(F, p, q, rect_a=None, rect_b=None, cross=True):
    if rect_a is not None: rect_a = (rect_a[0], rect_a[1], rect_a[2] + 3, rect_a[3] + 3)
    a, b = F.line(p, q, cls='ln thick', marker='ahs', rect_a=rect_a, rect_b=rect_b, tag='dipole')
    if cross:
        dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy)
        nx, ny = -dy / L * 4, dx / L * 4
        F.out.append('<path class="ln thick" d="M%s %sL%s %s"/>' % tuple(F.f(v) for v in (a[0] + nx, a[1] + ny, a[0] - nx, a[1] - ny)))
        F.segs.append((a[0] + nx, a[1] + ny, a[0] - nx, a[1] - ny, 'cross'))

def net(F, p, q):
    a, b = F.line(p, q, cls='c2 sw2', marker='ah', tag='net')
    dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy)
    nx, ny = -dy / L * 4, dx / L * 4
    F.out.append('<path class="c2 sw2" d="M%s %sL%s %s"/>' % tuple(F.f(v) for v in (a[0] + nx, a[1] + ny, a[0] - nx, a[1] - ny)))
    F.segs.append((a[0] + nx, a[1] + ny, a[0] - nx, a[1] - ny, 'netcross'))

def fig_dipoles():
    F = Fig('dipoles')
    cy = 90; xs = [60, 185, 355, 512]
    # CO2: arrows from C towards each O (arrow tail at C, cross at tail)
    cx = xs[0]
    rc = F.label(cx, cy, 'C'); ro1 = F.label(cx - 58, cy, 'O'); ro2 = F.label(cx + 58, cy, 'O')
    dip(F, (cx, cy), (cx - 58, cy), rc, ro1); dip(F, (cx, cy), (cx + 58, cy), rc, ro2)
    # H2O
    cx = xs[1]
    ro = F.label(cx, cy - 22, 'O')
    for sgn in (-1, 1):
        px, py = pol(cx, cy - 22, 58, 270 + sgn * 52.25)
        rh = F.label(px, py, 'H')
        dip(F, (px, py), (cx, cy - 22), rh, ro)
    net(F, (cx + 62, cy + 22), (cx + 62, cy - 26))
    F.text(cx + 62, cy + 42, 'net dipole', 'tl tc')
    # CCl4 flat X
    cx = xs[2]
    rc = F.label(cx, cy, 'C')
    for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        px, py = cx + dx * 44, cy + dy * 34
        rcl = F.label(px, py, 'Cl')
        dip(F, (cx, cy), (px, py), rc, rcl)
    # CHCl3
    cx = xs[3] - 30
    rc = F.label(cx, cy, 'C')
    rh = F.label(cx - 44, cy - 34, 'H')
    F.line((cx, cy), (cx - 44, cy - 34), cls='ln thick', rect_a=rc, rect_b=rh)
    for dx, dy in ((1, -1), (-1, 1), (1, 1)):
        px, py = cx + dx * 44, cy + dy * 34
        rcl = F.label(px, py, 'Cl')
        dip(F, (cx, cy), (px, py), rc, rcl)
    net(F, (cx + 68, cy - 14), (cx + 94, cy + 6))
    F.text(cx + 98, cy - 28, 'net dipole', 'tl tc')   # direction of the sum (right, down)
    names = [('CO₂', 'non-polar'), ('H₂O', 'polar'), ('CCl₄', 'non-polar'), ('CHCl₃', 'polar')]
    xl = [xs[0], xs[1], xs[2], xs[3] - 30]
    for x, (n, s) in zip(xl, names):
        F.text(x, 160, n, 'tl tc'); F.text(x, 178, s, 'tl tc ta')
    return F

# ============ FIGURE 4: hydrogen bond between two water molecules ============
def fig_hbond():
    F = Fig('hbond')
    y = 100
    o1 = (90, y); hd = (140, y)
    rO1 = F.label(*o1, 'O'); rHd = F.label(*hd, 'H')
    F.line(o1, hd, rect_a=rO1, rect_b=rHd)
    hb = pol(90, y, 48, 270 - 14.5)    # other H of molecule 1, 104.5 deg from the O-H(d) bond (down-left)
    # direction of bond 2: rotate from 0deg (right) by -104.5 -> use angle 180+75.5 ... place down-left
    hb = pol(90, y, 48, 180 + 75.5 - 0)  # 255.5 deg: down, slightly left
    rHb = F.label(*hb, 'H')
    F.line(o1, hb, rect_a=rO1, rect_b=rHb)
    F.dots(90 - 4, y - 18); F.dots(90 - 22, y - 8, horizontal=False)
    o2 = (240, y)
    rO2 = F.label(*o2, 'O')
    for sgn in (-1, 1):
        px, py = pol(240, y, 48, sgn * 52.25)
        rh = F.label(px, py, 'H')
        F.line(o2, (px, py), rect_a=rO2, rect_b=rh)
    F.dots(225, y, horizontal=False); F.dots(240 - 6, y + 18)
    # hydrogen bond (dashed), 4 px clear of the labels
    F.line(hd, (219, y), cls='ln dash thick', rect_a=rHd, rect_b=None, tag='hbond')
    F.text(140, y - 24, 'δ+', 'tl tc ta'); F.text(88, y - 30, 'δ−', 'tl tc ta'); F.text(240, y - 30, 'δ−', 'tl tc ta')
    F.text(190, y + 46, 'hydrogen bond', 'tl tc')
    F.line((190, y + 30), (190, y + 8), cls='ln-m thin', tag='ptr')
    return F

# ============ FIGURE 5: instantaneous and induced dipoles ============
def fig_idid():
    F = Fig('idid')
    cy = 70; r = 29; ax, bx = 95, 225
    for x in (ax, bx):
        F.out.append(f'<path class="ln" d="M{x - r} {cy}a{r} {r} 0 1 0 {2 * r} 0a{r} {r} 0 1 0 -{2 * r} 0"/>')
    F.text(ax - 15, cy + 5, 'δ−', 'tl tc ta'); F.text(ax + 15, cy + 5, 'δ+', 'tl tc ta')
    F.text(bx - 15, cy + 5, 'δ−', 'tl tc ta'); F.text(bx + 15, cy + 5, 'δ+', 'tl tc ta')
    a = F.line((ax + r + 10, cy), (bx - r - 10, cy), cls='ln', marker='ah', tag='arrow')
    F.text((ax + bx) / 2, cy - 12, 'attract', 'tl tc')
    F.text(ax, 128, 'instantaneous', 'tl tc'); F.text(ax, 146, 'dipole', 'tl tc')
    F.text(bx, 128, 'induced', 'tl tc'); F.text(bx, 146, 'dipole', 'tl tc')
    return F

CAPS = {
 'shapes': ("Drawings of carbon dioxide (linear, 180°), boron trifluoride (trigonal planar, 120°), methane (tetrahedral, 109.5°), ammonia (pyramidal, 107°) and water (non-linear, 104.5°)",
  "Shapes with two, three and four electron pairs. A plain line lies in the plane of the page, a filled wedge points towards you and a dashed line points away. Pairs of dots are lone pairs. The number under each drawing is its bond angle.", 'fig'),
 'five_six': ("Phosphorus pentafluoride, trigonal bipyramidal, with angles of 180°, 120° and 90°, and sulfur hexafluoride, octahedral, with angles of 90° and 180°",
  "PF₅ has five bonding pairs: two axial (up and down) and three equatorial. SF₆ has six bonding pairs along three axes at right angles. Wedges and dashes mean the same as in the previous figure.", 'fig'),
 'dipoles': ("Bond dipole arrows in carbon dioxide, water, tetrachloromethane and trichloromethane; the dipoles cancel in CO2 and CCl4 but not in H2O and CHCl3",
  "Each arrow is a bond dipole: the cross is at the δ+ end and the head points to the δ− end. In CO₂ and CCl₄ the dipoles cancel. In H₂O and CHCl₃ they do not, so a separate arrow shows the net dipole. The C–H bond is drawn as a plain line because it is almost non-polar. CCl₄ and CHCl₃ are drawn flat; the real molecules are tetrahedral.", 'fig'),
 'hbond': ("Two water molecules joined by a hydrogen bond: the hydrogen atom of one, labelled delta plus, points along a straight line at a lone pair on the oxygen atom of the other, labelled delta minus",
  "A hydrogen bond between two water molecules. The δ+ hydrogen of the left molecule points at a lone pair on the δ− oxygen of the right molecule, and O–H···O lies in a straight line. Dots are lone pairs.", 'fig small'),
 'idid': ("Two atoms, the first with an instantaneous dipole, the second with a dipole induced by the first, attracting each other",
  "An instantaneous dipole in one particle (electrons momentarily on the left) pushes the electrons of its neighbour away from it. The δ+ end of the first is attracted to the δ− end of the second.", 'fig small'),
}

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    figs = {'shapes': fig_shapes, 'five_six': fig_five_six, 'dipoles': fig_dipoles, 'hbond': fig_hbond, 'idid': fig_idid}
    for k, fn in figs.items():
        if which not in ('all', k): continue
        F = fn()
        probs = F.check()
        alt, cap, cls = CAPS[k]
        svg, size = F.svg(alt, cap, cls=cls)
        print(f'--- {k} viewBox size {size}')
        for p in probs: print('PROBLEM', p)
        if '-v' in sys.argv: print(svg)
