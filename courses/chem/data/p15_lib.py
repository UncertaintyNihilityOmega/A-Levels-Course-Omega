# data/p15_lib.py: small helpers for the P15 figures (SVG snippets with label/segment overlap checks).
# Usage: fig = Fig(); fig.text(...); fig.line(...); print(fig.svg()); fig.report()
import math

SUB = '₀₁₂₃₄₅₆₇₈₉'
SUP = '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻'

def tw(s):
    """approximate width of a 13 px label"""
    w = 0
    for ch in s:
        if ch in SUB or ch in SUP: w += 6.0
        elif ch in 'il1|.,': w += 4
        elif ch.isupper() or ch in 'mwMW': w += 9.5
        elif ch in '+−-=°': w += 7.5
        elif ch == ' ': w += 4
        else: w += 7
    return w

def f(x):
    return ('%.1f' % x).rstrip('0').rstrip('.')

class Fig:
    def __init__(self):
        self.parts = []
        self.boxes = []   # (owner, x0, y0, x1, y1)
        self.segs = []    # (owner, x0, y0, x1, y1)

    # --- primitives
    def raw(self, s):
        self.parts.append(s)

    def text(self, x, y, s, cls='tl tc', owner=None, anchor=None, box=True):
        """anchor: None -> centred if 'tc' in cls; 'start' / 'end'"""
        w = tw(s)
        if 'tc' in cls:
            x0 = x - w / 2
        elif anchor == 'end':
            x0 = x - w
        else:
            x0 = x
        h_top = 10 if 'ts' not in cls else 9
        if box:
            self.boxes.append((owner or s, x0, y - h_top, x0 + w, y + 3))
        a = ' text-anchor="end"' if anchor == 'end' else ''
        self.parts.append('<text class="%s" x="%s" y="%s"%s>%s</text>' % (cls, f(x), f(y), a, s))

    def line(self, x0, y0, x1, y1, cls='ln', owner=None, extra='', seg=True):
        self.parts.append('<path class="%s" d="M%s %sL%s %s"%s/>' % (cls, f(x0), f(y0), f(x1), f(y1), extra))
        if seg:
            self.segs.append((owner or 'line', x0, y0, x1, y1))

    def path(self, d, cls, extra=''):
        self.parts.append('<path class="%s" d="%s"%s/>' % (cls, d, extra))

    def circle(self, x, y, r, cls):
        self.parts.append('<circle class="%s" cx="%s" cy="%s" r="%s"/>' % (cls, f(x), f(y), f(r)))

    def lonepair(self, x, y, ux, uy, owner=None):
        """two dots 6 px apart, perpendicular to the direction (ux, uy)"""
        px, py = -uy, ux
        for s in (-3, 3):
            self.circle(x + px * s, y + py * s, 1.7, 'fi')

    def wedge(self, x0, y0, x1, y1, w=6.0, owner=None):
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        px, py = -uy, ux
        a = (x1 + px * w / 2, y1 + py * w / 2)
        b = (x1 - px * w / 2, y1 - py * w / 2)
        self.parts.append('<path class="fi" d="M%s %sL%s %sL%s %sZ"/>' % (f(x0), f(y0), f(a[0]), f(a[1]), f(b[0]), f(b[1])))
        self.segs.append((owner or 'wedge', x0, y0, x1, y1))

    def hash(self, x0, y0, x1, y1, n=5, w=7.0, owner=None):
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        px, py = -uy, ux
        d = ''
        for i in range(1, n + 1):
            t = i / n
            cx, cy = x0 + dx * t * 0.97, y0 + dy * t * 0.97
            hw = (1.0 + (w / 2 - 1.0) * t)
            d += 'M%s %sL%s %s' % (f(cx + px * hw), f(cy + py * hw), f(cx - px * hw), f(cy - py * hw))
        self.parts.append('<path class="ln" d="%s"/>' % d)
        self.segs.append((owner or 'hash', x0, y0, x1, y1))

    def svg(self, vb, label):
        return '<svg viewBox="%s" role="img" aria-label="%s">%s</svg>' % (vb, label, ''.join(self.parts))

    # --- checks
    @staticmethod
    def _dist_rect_seg(r, s):
        x0, y0, x1, y1 = r
        sx0, sy0, sx1, sy1 = s
        best = 1e9
        L = max(1, int(math.hypot(sx1 - sx0, sy1 - sy0)))
        for i in range(L + 1):
            t = i / L
            px, py = sx0 + (sx1 - sx0) * t, sy0 + (sy1 - sy0) * t
            dx = max(x0 - px, 0, px - x1)
            dy = max(y0 - py, 0, py - y1)
            best = min(best, math.hypot(dx, dy))
        return best

    def report(self, name='', min_gap=4.0, own_gap=3.0, fixed=None):
        problems = 0
        for i, (o, *r) in enumerate(self.boxes):
            for j, (o2, *r2) in enumerate(self.boxes):
                if j <= i: continue
                gx = max(r2[0] - r[2], r[0] - r2[2])
                gy = max(r2[1] - r[3], r[1] - r2[3])
                if max(gx, gy) < min_gap:
                    print('  %s: labels too close: %r %r (gap %.1f)' % (name, o, o2, max(gx, gy)))
                    problems += 1
        for (o, *r) in self.boxes:
            for (so, *s) in self.segs:
                d = self._dist_rect_seg(r, s)
                same = (so == o)
                lim = own_gap if same else min_gap
                if d < lim:
                    print('  %s: label %r close to segment of %r (%.1f)' % (name, o, so, d))
                    problems += 1
        print('%s: %d label problems' % (name, problems))
        return problems

def ligand_label(fig, ex, ey, ux, uy, s, gap=5.0, owner=None):
    """place label s so its box edge is gap px beyond (ex, ey) in direction (ux, uy); returns the centre"""
    w = tw(s); h = 13.0
    hw, hh = w / 2, h / 2
    ex_t = hw / abs(ux) if abs(ux) > 1e-9 else 1e9
    ey_t = hh / abs(uy) if abs(uy) > 1e-9 else 1e9
    exit_d = min(ex_t, ey_t)
    cx, cy = ex + ux * (gap + exit_d), ey + uy * (gap + exit_d)
    fig.text(cx, cy + 3.5, s, 'tl tc', owner=owner or s)
    return cx, cy


def node(fig, x, y, s, owner=None, cls='tl tc'):
    """text node whose box centre is (x, y); returns a descriptor for link()"""
    fig.text(x, y + 3.5, s, cls, owner=owner or s)
    return ('box', x, y, tw(s) / 2, 6.5)

def pt(x, y):
    return ('pt', x, y, 0, 0)

def _exit(d, ux, uy):
    if d[0] == 'pt': return 0.0
    hw, hh = d[3], d[4]
    tx = hw / abs(ux) if abs(ux) > 1e-9 else 1e9
    ty = hh / abs(uy) if abs(uy) > 1e-9 else 1e9
    return min(tx, ty)

def link(fig, a, b, kind="plain", gap=6.0, owner=None, w=7.0):
    dx, dy = b[1] - a[1], b[2] - a[2]
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    ga = gap if a[0] == 'box' else 0
    gb = gap if b[0] == 'box' else 0
    sa = _exit(a, ux, uy) + ga
    sb = _exit(b, ux, uy) + gb
    x0, y0 = a[1] + ux * sa, a[2] + uy * sa
    x1, y1 = b[1] - ux * sb, b[2] - uy * sb
    o = owner or ('link%.0f_%.0f' % (a[1], a[2]))
    if kind == 'plain': fig.line(x0, y0, x1, y1, 'ln thick', owner=o)
    elif kind == 'thin': fig.line(x0, y0, x1, y1, 'ln', owner=o)
    elif kind == 'wedge': fig.wedge(x0, y0, x1, y1, w, owner=o)
    else: fig.hash(x0, y0, x1, y1, 5, w, owner=o)
    return (x0, y0, x1, y1)
