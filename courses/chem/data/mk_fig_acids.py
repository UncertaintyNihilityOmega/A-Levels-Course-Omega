# data/mk_fig_acids.py: builds the SVG for chem.acids (four titration sketches; indicator ranges) and checks label clearances.
# Run: py -X utf8 data/mk_fig_acids.py titr|ind
import sys
sys.path.insert(0, 'data')
from mk_fig_energetics import Fig, tw
from titration_model import ph_at, veq

CASES = [('strong acid + strong base', True, True, 'steep part:|pH 3 to 11', 'equivalence point', 'pH 7'),
         ('weak acid + strong base', False, True, 'steep part:|pH 6.5 to 11', 'equivalence point', 'pH above 7'),
         ('strong acid + weak base', True, False, 'steep part:|pH 3 to 7.5', 'equivalence point', 'pH below 7'),
         ('weak acid + weak base', False, False, 'no steep part:|pH 6.4 to 7.6', 'equivalence point', 'pH about 7')]

def curve_pts(a, b, ox, oy, n=26):
    x0, x1 = ox + 36, ox + 240
    yb, yt = oy + 175, oy + 30
    X = lambda v: x0 + (x1 - x0) * v / 50.0
    Y = lambda p: yb - (yb - yt) * p / 14.0
    vs = sorted(set([i * 50.0 / n for i in range(n + 1)] + [23.5, 24.25, 24.75, 25.25, 25.75, 26.5]))
    return [(X(v), Y(ph_at(v, a, b))) for v in vs], X, Y

def titr():
    f = Fig()
    out = []
    for k, (name, a, b, steep, eq1, eq2) in enumerate(CASES):
        ox, oy = 5, k * 230
        pts, X, Y = curve_pts(a, b, ox, oy)
        x0, x1 = ox + 36, ox + 240
        yb, yt = oy + 175, oy + 30
        f.add(f'<path class="ax" d="M{x0} {yb}V{yt-4}" marker-end="url(#ahm)"/>'); f.seg([(x0, yb), (x0, yt-4)])
        f.add(f'<path class="ax" d="M{x0} {yb}H{x1+8}" marker-end="url(#ahm)"/>'); f.seg([(x0, yb), (x1+8, yb)])
        f.label(ox + 140, oy + 8, name, 'middle', 'tl')
        f.label(x0 + 8, yt + 2, 'pH')
        for p in (0, 7, 14):
            f.add(f'<text class="ts" x="{x0-5}" y="{Y(p)+4:.0f}" text-anchor="end">{p}</text>')
        for v in (0, 25, 50):
            f.add(f'<text class="ts tc" x="{X(v):.0f}" y="{yb+14}">{v}</text>')
        f.label(ox + 140, yb + 30, 'volume of base added / cm³', 'middle')
        f.add(f'<path class="ln-m thin dash" d="M{x0} {Y(7):.0f}H{x1}"/>'); f.seg([(x0, Y(7)), (x1, Y(7))])
        d = 'M' + 'L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
        f.add(f'<path class="c1 sw2" d="{d}"/>'); f.seg(pts)
        # equivalence marker
        ex, ey = X(25), Y(ph_at(25.0, a, b))
        f.add(f'<circle class="fi" cx="{ex:.0f}" cy="{ey:.0f}" r="3.5"/>')
        # labels: placed to the right of the marker, below the curve
        l1, l2 = steep.split('|')
        f.label(ox + 158, yb - 44, l1, 'start'); f.label(ox + 158, yb - 26, l2, 'start')
        out.append((name, round(ex), round(ey), round(Y(7))))
    return f, out

def ind():
    f = Fig()
    X = lambda p: 20 + 300 * p / 14.0
    YA = 352
    for p in range(0, 15, 2):
        f.add(f'<path class="ln" d="M{X(p):.0f} {YA}V{YA+6}"/>')
        f.add(f'<text class="ts tc" x="{X(p):.0f}" y="{YA+20}">{p}</text>')
    f.add(f'<path class="ax" d="M20 {YA}H336" marker-end="url(#ahm)"/>')
    f.label(170, YA + 44, 'pH', 'middle')
    rows = [('methyl orange', 2.9, 4.6, 'fa'), ('bromophenol blue', 3.0, 4.5, 'fa'), ('thymol blue', 8.0, 9.6, 'fa'), ('thymolphthalein', 9.3, 10.5, 'fa')]
    f.label(10, 16, 'indicator ranges', 'start')
    for i, (n, a, b, c) in enumerate(rows):
        y = 40 + 40 * i
        f.label(20, y, n, 'start')
        f.add(f'<rect class="{c}" x="{X(a):.0f}" y="{y+6}" width="{X(b)-X(a):.0f}" height="16" rx="3"/>')
        f.label(round(X(b) + 8), y + 19, f'{a}–{b}', 'start', 'tl', False)
    f.label(10, 210, 'steep part of the curve', 'start')
    rows2 = [('strong acid + strong base', 3.0, 11.0, '3–11'), ('weak acid + strong base', 6.5, 11.0, '6.5–11'), ('strong acid + weak base', 3.0, 7.5, '3–7.5')]
    for i, (n, a, b, t) in enumerate(rows2):
        y = 234 + 40 * i
        f.label(20, y, n, 'start')
        f.add(f'<rect class="fm s-acc" x="{X(a):.0f}" y="{y+6}" width="{X(b)-X(a):.0f}" height="16" rx="3"/>')
        f.label(round(X(b) + 8), y + 19, t, 'start', 'tl', False)
    return f

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "titr"
    if which == "titr":
        f, out = titr(); print(out); f.check(); print(chr(10).join(f.out))
    if which == "ind":
        g = ind(); g.check(); print(chr(10).join(g.out))

def particles():
    """strong versus weak acid: what is in solution (ten formula units of HA)."""
    out = []
    def panel(ox, title, items):
        out.append(f'<path class="ln" d="M{ox+10} 10H{ox+260}a10 10 0 0 1 10 10V150a10 10 0 0 1-10 10H{ox+10}a10 10 0 0 1-10-10V20a10 10 0 0 1 10-10Z"/>')
        for (r, c, kind) in items:
            x = ox + 30 + 52 * c
            y = 44 + 30 * r
            cls = 'tl tc' if kind == 'HA' else 'tl tc ta'
            t = {'HA': 'HA', 'H': 'H⁺', 'A': 'A⁻'}[kind]
            out.append(f'<text class="{cls}" x="{x}" y="{y}">{t}</text>')
        out.append(f'<text class="tl tc" x="{ox+135}" y="188">{title}</text>')
    strong = [(r, c, 'H' if (r + c) % 2 == 0 else 'A') for r in range(4) for c in range(5)]
    weak_cells = [(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3)]
    weak = [(r, c, 'HA') for (r, c) in weak_cells[:8]] + [(1, 4, 'H'), (3, 0, 'A')]
    # a few more whole molecules to fill the gaps
    weak += [(0, 1, 'HA')]
    panel(5, 'strong acid: all HA split', strong)
    panel(290, 'weak acid: most HA stay whole', weak)
    return out

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'part':
    print(chr(10).join(particles()))
