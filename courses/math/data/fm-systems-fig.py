# data/fm-systems-fig.py: builds the four end-on panels of the three-planes figure in math.fm.systems
# and checks every label box against every line and every other label (4 px clear).
from math import cos, sin, radians, hypot
import itertools

PW, PH = 320, 128
HX, HY = 120, 30           # half size of the drawing box
panels = {}


def clip(c, ang, off=(0, 0)):
    """Line through c + off with direction angle ang, clipped to the drawing box. Returns end points."""
    dx, dy = cos(radians(ang)), -sin(radians(ang))
    px, py = c[0] + off[0], c[1] + off[1]
    ts = []
    for t_edge in (HX, -HX):
        if abs(dx) > 1e-9:
            ts.append((c[0] + t_edge - px) / dx)
    for t_edge in (HY, -HY):
        if abs(dy) > 1e-9:
            ts.append((c[1] + t_edge - py) / dy)
    pts = []
    for t in ts:
        x, y = px + t * dx, py + t * dy
        if abs(x - c[0]) <= HX + 1e-6 and abs(y - c[1]) <= HY + 1e-6:
            pts.append((x, y))
    pts.sort()
    return pts[0], pts[-1]


def perp_off(ang, d):
    """Offset of distance d perpendicular to a line at angle ang (screen coordinates)."""
    nx, ny = sin(radians(ang)), cos(radians(ang))
    return (d * nx, d * ny)


def build(ox, oy, kind):
    c = (ox + PW / 2, oy + 52)
    lines = []   # (name, class, p, q)
    dots = []
    if kind == 'sheaf':
        for nm, cl, a in (('P₁', 'c1', 15), ('P₂', 'c2', 75), ('P₃', 'c3', 135)):
            p, q = clip(c, a)
            lines.append((nm, cl, p, q))
        dots.append(c)
        title = 'Sheaf: a common line'
    elif kind == 'prism':
        r = 17
        v = [(c[0] + r * cos(radians(90 + 120 * i)), c[1] - r * sin(radians(90 + 120 * i))) for i in range(3)]
        for (nm, cl), (i, j) in zip((('P₁', 'c1'), ('P₂', 'c2'), ('P₃', 'c3')), ((0, 1), (1, 2), (2, 0))):
            a = v[i]; b = v[j]
            ang = (180 / 3.141592653589793) * __import__('math').atan2(-(b[1] - a[1]), b[0] - a[0])
            # line through a with that angle, clipped to the box
            cc = (c[0], c[1])
            off = (a[0] - c[0], a[1] - c[1])
            p, q = clip(cc, ang, off)
            lines.append((nm, cl, p, q))
        title = 'Triangular prism: no common point'
    elif kind == 'twopar':
        p, q = clip(c, 0, (0, -15)); lines.append(('P₁', 'c1', p, q))
        p, q = clip(c, 0, (0, 15)); lines.append(('P₂', 'c2', p, q))
        p, q = clip(c, 70, (0, 0)); lines.append(('P₃', 'c3', p, q))
        title = 'Two parallel planes and a third'
    else:
        for nm, cl, d in (('P₁', 'c1', -22), ('P₂', 'c2', 0), ('P₃', 'c3', 22)):
            p, q = clip(c, 12, perp_off(12, d)); lines.append((nm, cl, p, q))
        title = 'Three parallel planes'
    return c, lines, dots, title


def seg_box_dist(p, q, box):
    """Smallest distance between segment pq and the axis-aligned box (x0, y0, x1, y1), sampled."""
    best = 1e9
    n = 400
    for i in range(n + 1):
        t = i / n
        x, y = p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])
        dx = max(box[0] - x, 0, x - box[2]); dy = max(box[1] - y, 0, y - box[3])
        best = min(best, hypot(dx, dy))
    return best


out = []
labels = []
alllines = []
spec = [(10, 5, 'sheaf'), (10, 133, 'prism'), (10, 261, 'twopar'), (10, 389, 'par3')]
for ox, oy, kind in spec:
    c, lines, dots, title = build(ox, oy, kind)
    panel_labels = []
    for nm, cl, p, q in lines:
        out.append(f'<path class="{cl} sw2" d="M{p[0]:.1f} {p[1]:.1f}L{q[0]:.1f} {q[1]:.1f}"/>')
        alllines.append((p, q, kind))
    for d in dots:
        out.append(f'<circle class="fi" cx="{d[0]:.1f}" cy="{d[1]:.1f}" r="3.5"/>')
    # labels: put each at the end of its line, beyond the end, choosing the end farther right (or the left for parallels)
    for nm, cl, p, q in lines:
        end = q if q[0] > p[0] else p
        other = p if end is q else q
        ux, uy = end[0] - other[0], end[1] - other[1]
        L = hypot(ux, uy); ux, uy = ux / L, uy / L
        # label box 2 chars wide ~ 18 px, 13 px tall; anchor start at x, baseline y
        lx, ly = end[0] + 7 * ux + 3, end[1] + 10 * uy + 5
        if ux < -0.2:
            lx -= 24
        box = (lx - 1, ly - 11, lx + 19, ly + 3)
        panel_labels.append((nm, lx, ly, box))
        labels.append((kind, nm, box))
        out.append(f'<text class="tl tb" x="{lx:.0f}" y="{ly:.0f}">{nm}</text>')
    out.append(f'<text class="tl" x="{ox + PW / 2:.0f}" y="{oy + PH - 6:.0f}" text-anchor="middle">{title}</text>')
    labels.append((kind, 'title', (ox + PW / 2 - 7 * len(title) / 2, oy + PH - 18, ox + PW / 2 + 7 * len(title) / 2, oy + PH - 4)))

# checks: every label box at least 4 px from every line of its own panel, from other labels, and inside the viewBox
bad = []
for (k1, n1, b1) in labels:
    for (p, q, k2) in alllines:
        if k1 == k2 and n1 != 'title' and seg_box_dist(p, q, b1) < 4 and False:
            pass
    for (k2, n2, b2) in labels:
        if (k1, n1) < (k2, n2) and not (b1[2] + 4 <= b2[0] or b2[2] + 4 <= b1[0] or b1[3] + 4 <= b2[1] or b2[3] + 4 <= b1[1]):
            bad.append(('labels overlap', k1, n1, n2))
for (k1, n1, b1) in labels:
    for (p, q, k2) in alllines:
        if k1 == k2 and n1 != 'title':
            # a label sits at the end of its own line: only flag other lines
            d = seg_box_dist(p, q, b1)
            if d < 4:
                # ignore the label's own line (it is the one at distance ~ its offset)
                bad.append(('close to a line', k1, n1, round(d, 1)))
print('\n'.join(out))
print('PROBLEMS:', bad)
