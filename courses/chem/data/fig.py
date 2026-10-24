# helper for organic skeletal / displayed figures (P9). Run from the course folder.
import math

CW = 7.0      # label char width
LH = 13.0     # label height
GAP = 4.0     # clear gap between bond end and label box


def text_w(s):
    # subscripts / superscripts narrower
    w = 0
    for ch in s:
        w += 5.5 if ch in '₀₁₂₃₄₅₆₇₈₉⁺⁻' else (3.5 if ch in 'Il1' else CW)
    return w


class Fig:
    def __init__(self):
        self.parts = []      # svg strings
        self.labels = []     # (cx, cy, w, h, text) boxes (centre)
        self.segs = []       # (x1,y1,x2,y2, tag)
        self.atoms = {}

    def f(self, v):
        s = ('%.1f' % v).rstrip('0').rstrip('.')
        return s if s != '-0' else '0'

    def atom(self, key, x, y, lab=None):
        self.atoms[key] = (x, y, lab)

    def label(self, x, y, s, cls='tl tc', box=True):
        # (x,y) = centre of the atom; text baseline y+4
        w = text_w(s)
        if 'tc' in cls.split():
            self.parts.append('<text class="%s" x="%s" y="%s">%s</text>' % (cls, self.f(x), self.f(y + 4), s))
        else:
            self.parts.append('<text class="%s" x="%s" y="%s">%s</text>' % (cls, self.f(x - w / 2), self.f(y + 4), s))
        if box:
            self.labels.append((x, y, w, LH, s))

    def free_text(self, x, y_base, s, cls='tl tc'):
        w = text_w(s)
        self.parts.append('<text class="%s" x="%s" y="%s">%s</text>' % (cls, self.f(x), self.f(y_base), s))
        cx = x if 'tc' in cls.split() else x + w / 2
        self.labels.append((cx, y_base - 4, w, LH, s))

    def _cut(self, a, b):
        # distance from atom a (towards b) to leave its label box + GAP
        x, y, lab = self.atoms[a]
        if not lab:
            return 0.0
        bx, by, _ = self.atoms[b]
        dx, dy = bx - x, by - y
        L = math.hypot(dx, dy)
        w = text_w(lab)
        tx = (w / 2) / abs(dx / L) if abs(dx) > 1e-9 else 1e9
        ty = (LH / 2) / abs(dy / L) if abs(dy) > 1e-9 else 1e9
        return min(tx, ty) + GAP

    def bond(self, a, b, order=1, cls='ln thick', off=2.6, ends=(True, True)):
        x1, y1, _ = self.atoms[a]
        x2, y2, _ = self.atoms[b]
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        ca, cb = self._cut(a, b), self._cut(b, a)
        if order > 1:
            ca = ca + 1.5 if ca else 0
            cb = cb + 1.5 if cb else 0
        sx, sy = x1 + ux * ca, y1 + uy * ca
        ex, ey = x2 - ux * cb, y2 - uy * cb
        nx, ny = -uy, ux
        offs = {1: [0], 2: [-off, off], 3: [-off * 1.4, 0, off * 1.4]}[order]
        d = []
        for o in offs:
            d.append('M%s %sL%s %s' % (self.f(sx + nx * o), self.f(sy + ny * o), self.f(ex + nx * o), self.f(ey + ny * o)))
            self.segs.append((sx + nx * o, sy + ny * o, ex + nx * o, ey + ny * o, a + b))
        self.parts.append('<path class="%s" d="%s"/>' % (cls, ''.join(d)))

    def wedge(self, a, b, w=7.0, hashed=False):
        # tip at a, wide end at b (b may be labelled)
        x1, y1, _ = self.atoms[a]
        x2, y2, _ = self.atoms[b]
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        ca, cb = self._cut(a, b), self._cut(b, a)
        sx, sy = x1 + ux * ca, y1 + uy * ca
        ex, ey = x2 - ux * cb, y2 - uy * cb
        nx, ny = -uy, ux
        if not hashed:
            self.parts.append('<path class="fi" d="M%s %sL%s %sL%s %sZ"/>' % (
                self.f(sx), self.f(sy), self.f(ex + nx * w / 2), self.f(ey + ny * w / 2), self.f(ex - nx * w / 2), self.f(ey - ny * w / 2)))
        else:
            n = 6
            d = []
            for i in range(1, n + 1):
                t = i / n
                px, py = sx + (ex - sx) * t, sy + (ey - sy) * t
                hw = (w / 2) * t
                d.append('M%s %sL%s %s' % (self.f(px + nx * hw), self.f(py + ny * hw), self.f(px - nx * hw), self.f(py - ny * hw)))
            self.parts.append('<path class="ln" d="%s"/>' % ''.join(d))
        self.segs.append((sx, sy, ex, ey, a + b))

    def raw(self, s):
        self.parts.append(s)

    def check(self, minclear=3.5, vb=None):
        bad = []
        # label box vs segments
        for (cx, cy, w, h, s) in self.labels:
            x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2 - 0.5, cy + h / 2 + 0.5
            for (a, b, c, d, tag) in self.segs:
                dist = seg_rect_dist(a, b, c, d, x0, y0, x1, y1)
                if dist < minclear:
                    bad.append('label %r vs seg %s: %.1f' % (s, tag, dist))
        # label vs label
        for i in range(len(self.labels)):
            for j in range(i + 1, len(self.labels)):
                A, B = self.labels[i], self.labels[j]
                dx = abs(A[0] - B[0]) - (A[2] + B[2]) / 2
                dy = abs(A[1] - B[1]) - (A[3] + B[3]) / 2
                if dx < 3 and dy < 3:
                    bad.append('labels %r and %r too close (dx %.1f dy %.1f)' % (A[4], B[4], dx, dy))
        if vb:
            x0, y0, w, h = vb
            for (cx, cy, lw, lh, s) in self.labels:
                if cx - lw / 2 < x0 + 2 or cx + lw / 2 > x0 + w - 2 or cy - lh / 2 < y0 + 1 or cy + lh / 2 > y0 + h - 1:
                    bad.append('label %r outside viewBox' % s)
            for (a, b, c, d, tag) in self.segs:
                for px, py in ((a, b), (c, d)):
                    if px < x0 or px > x0 + w or py < y0 or py > y0 + h:
                        bad.append('segment %s outside viewBox' % tag)
        return bad

    def svg(self, vb, aria, caption, cls='fig small'):
        x0, y0, w, h = vb
        return '<figure class="%s"><svg viewBox="%s %s %s %s" role="img" aria-label="%s">%s</svg><figcaption>%s</figcaption></figure>' % (
            cls, self.f(x0), self.f(y0), self.f(w), self.f(h), aria, ''.join(self.parts), caption)


def seg_pt_dist(px, py, a, b, c, d):
    dx, dy = c - a, d - b
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((px - a) * dx + (py - b) * dy) / L2))
    return math.hypot(px - (a + t * dx), py - (b + t * dy))


def seg_rect_dist(a, b, c, d, x0, y0, x1, y1):
    # min distance between segment and axis-aligned rectangle (0 if intersect)
    # sample the segment densely
    n = 60
    best = 1e9
    for i in range(n + 1):
        t = i / n
        px, py = a + (c - a) * t, b + (d - b) * t
        dx = max(x0 - px, 0, px - x1)
        dy = max(y0 - py, 0, py - y1)
        best = min(best, math.hypot(dx, dy))
    return best
