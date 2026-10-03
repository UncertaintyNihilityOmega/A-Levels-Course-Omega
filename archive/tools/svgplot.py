#!/usr/bin/env python3
"""House-style SVG graph generator for the guide.

Example:
  python3 tools/svgplot.py --f "x**2-2*x-3" --x -3 5 --y -5 7 --pt "-1,0,(−1, 0)" --pt "3,0,(3, 0)" \
      --pt "1,-4,vertex (1, −4)" --vline 1 --caption "The graph of y = x² − 2x − 3" --label "y = x² − 2x − 3"

Prints a <figure class="fig">…</figure> snippet. Paste it inside a :::html block.
Functions use Python syntax with math names available (sin, cos, tan, exp, log, sqrt, pi, e, abs).
Classes used (styled by the page, theme-aware): ax, gr, c1, c2, c3, c4, ln, dash, f1, f2, tl, ts, tc, te, ti.
"""
import argparse, math

ap = argparse.ArgumentParser()
ap.add_argument('--f', action='append', default=[], help='function of x (python syntax); repeatable')
ap.add_argument('--label', action='append', default=[], help='legend/curve label for each --f, in order')
ap.add_argument('--x', nargs=2, type=float, default=[-5, 5])
ap.add_argument('--y', nargs=2, type=float, default=[-5, 5])
ap.add_argument('--w', type=int, default=560)
ap.add_argument('--h', type=int, default=320)
ap.add_argument('--xstep', type=float, default=None, help='tick spacing on x (default auto)')
ap.add_argument('--ystep', type=float, default=None)
ap.add_argument('--nogrid', action='store_true')
ap.add_argument('--noticks', action='store_true', help='hide numeric tick labels (sketch style)')
ap.add_argument('--pt', action='append', default=[], help='"x,y,label" marks a point; label optional')
ap.add_argument('--vline', action='append', default=[], type=float, help='dashed vertical line x=…')
ap.add_argument('--hline', action='append', default=[], type=float, help='dashed horizontal line y=…')
ap.add_argument('--shade', default=None, help='"f_index,a,b" shade area under curve f between x=a and x=b (index from 0)')
ap.add_argument('--xlabel', default='x')
ap.add_argument('--ylabel', default='y')
ap.add_argument('--caption', default='')
ap.add_argument('--legend', default='tr', help='tr or tl')
ap.add_argument('--alt', default='')
ap.add_argument('--deg', action='store_true', help='x in degrees for trig functions')
a = ap.parse_args()

W, H = a.w, a.h
ml, mr, mt, mb = 34, 18, 14, 26
x0, x1 = a.x; y0, y1 = a.y
def px(x): return ml + (x - x0) / (x1 - x0) * (W - ml - mr)
def py(y): return mt + (y1 - y) / (y1 - y0) * (H - mt - mb)
def nice(span):
    raw = span / 8
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag: return m * mag
    return 10 * mag
xs = a.xstep or nice(x1 - x0)
ys = a.ystep or nice(y1 - y0)
def fmt(v):
    if abs(v) < 1e-9: return '0'
    s = ('%.4f' % v).rstrip('0').rstrip('.')
    return s.replace('-', '−')

env = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
env['abs'] = abs
if a.deg:
    for fn in ('sin', 'cos', 'tan'):
        env[fn] = (lambda f: (lambda t: f(math.radians(t))))(getattr(math, fn))

out = []
out.append(f'<figure class="fig"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{a.alt or a.caption}">')
# grid
if not a.nogrid:
    g = []
    k = math.ceil(x0 / xs)
    while k * xs <= x1 + 1e-9:
        X = px(k * xs); g.append(f'M{X:.1f} {mt}V{H-mb}'); k += 1
    k = math.ceil(y0 / ys)
    while k * ys <= y1 + 1e-9:
        Y = py(k * ys); g.append(f'M{ml} {Y:.1f}H{W-mr}'); k += 1
    out.append(f'<path class="gr" d="{" ".join(g)}"/>')
# axes
ax_y = py(0) if y0 <= 0 <= y1 else py(y0)
ax_x = px(0) if x0 <= 0 <= x1 else px(x0)
out.append(f'<path class="ax" d="M{ax_x:.1f} {H-mb+4}V{mt-6}" marker-end="url(#ahm)"/>')
out.append(f'<path class="ax" d="M{ml-4} {ax_y:.1f}H{W-mr+6}" marker-end="url(#ahm)"/>')
out.append(f'<text class="tl ti" x="{W-mr+2:.0f}" y="{ax_y-7:.0f}" text-anchor="end">{a.xlabel}</text>')
out.append(f'<text class="tl ti" x="{ax_x+7:.0f}" y="{mt+4:.0f}">{a.ylabel}</text>')
if not a.noticks:
    k = math.ceil(x0 / xs)
    while k * xs <= x1 + 1e-9:
        v = k * xs
        if abs(v) > 1e-9:
            X = px(v); out.append(f'<text class="ts tc" x="{X:.1f}" y="{ax_y+15:.0f}">{fmt(v)}</text>')
        k += 1
    k = math.ceil(y0 / ys)
    while k * ys <= y1 + 1e-9:
        v = k * ys
        if abs(v) > 1e-9:
            Y = py(v); out.append(f'<text class="ts te" x="{ax_x-5:.0f}" y="{Y+4:.1f}">{fmt(v)}</text>')
        k += 1
    out.append(f'<text class="ts te" x="{ax_x-5:.0f}" y="{ax_y+14:.0f}">0</text>')
# shading
if a.shade:
    i, sa, sb = a.shade.split(',')
    f = a.f[int(i)]; sa = float(sa); sb = float(sb)
    pts = []
    n = 200
    for j in range(n + 1):
        x = sa + (sb - sa) * j / n
        y = eval(f, env, {'x': x})
        pts.append(f'{px(x):.1f} {py(max(min(y, y1), y0)):.1f}')
    out.append(f'<path class="f1" d="M{px(sa):.1f} {ax_y:.1f}L{"L".join(pts)}L{px(sb):.1f} {ax_y:.1f}Z" opacity="0.8"/>')
# guide lines
for v in a.vline:
    out.append(f'<path class="ln-m dash" d="M{px(v):.1f} {mt}V{H-mb}"/>')
for v in a.hline:
    out.append(f'<path class="ln-m dash" d="M{ml} {py(v):.1f}H{W-mr}"/>')
# curves (clipped to the plot window by interpolation)
cls = ['c1', 'c2', 'c3', 'c4']
def fval(f, x):
    try:
        y = eval(f, env, {'x': x})
        if isinstance(y, complex) or y != y or abs(y) == float('inf'): return None
        return y
    except Exception:
        return None
for idx, f in enumerate(a.f):
    segs, cur = [], []
    n = 320
    prev = None
    for j in range(n + 1):
        x = x0 + (x1 - x0) * j / n
        y = fval(f, x)
        inside = y is not None and y0 <= y <= y1
        if prev is not None and y is not None and prev[1] is not None:
            px_, py_ = prev
            # jump (asymptote) detection
            if abs(y - py_) > (y1 - y0) * 1.2:
                if cur: segs.append(cur); cur = []
                prev = (x, y); continue
            pin = y0 <= py_ <= y1
            if pin and not inside:
                yb = y1 if y > y1 else y0
                t = (yb - py_) / (y - py_)
                cur.append((px(px_ + t * (x - px_)), py(yb))); segs.append(cur); cur = []
            elif inside and not pin:
                yb = y1 if py_ > y1 else y0
                t = (yb - py_) / (y - py_)
                cur = [(px(px_ + t * (x - px_)), py(yb))]
        if inside:
            cur.append((px(x), py(y)))
        elif y is None and cur:
            segs.append(cur); cur = []
        prev = (x, y)
    if cur: segs.append(cur)
    d = ' '.join('M' + 'L'.join(f'{X:.1f} {Y:.1f}' for X, Y in s_) for s_ in segs if len(s_) > 1)
    out.append(f'<path class="{cls[idx % 4]}" d="{d}"/>')
# labels for curves (legend, top-left or top-right of the plot)
for idx, lab in enumerate(a.label):
    if a.legend == 'tl':
        out.append(f'<text class="tl halo {"ta" if idx == 0 else "ta2"}" x="{ml+8}" y="{mt+16+idx*18}">{lab}</text>')
    else:
        out.append(f'<text class="tl halo {"ta" if idx == 0 else "ta2"}" x="{W-mr-6}" y="{mt+16+idx*18}" text-anchor="end">{lab}</text>')
# points: label may end with @n @s @e @w @ne @nw @se @sw to choose its position
DIRS = {'n': (0, -11, 'middle'), 's': (0, 19, 'middle'), 'e': (9, 4, 'start'), 'w': (-9, 4, 'end'),
        'ne': (7, -9, 'start'), 'nw': (-7, -9, 'end'), 'se': (7, 17, 'start'), 'sw': (-7, 17, 'end')}
for p_ in a.pt:
    parts = p_.split(',')
    x, y = float(parts[0]), float(parts[1])
    lab = ','.join(parts[2:]) if len(parts) > 2 else ''
    X, Y = px(x), py(y)
    out.append(f'<circle class="fi" cx="{X:.1f}" cy="{Y:.1f}" r="4"/>')
    if lab:
        d = None
        if '@' in lab:
            lab, d = lab.rsplit('@', 1)
        if d not in DIRS:
            d = 'ne' if X < W * 0.7 else 'nw'
        dx, dy, anc = DIRS[d]
        out.append(f'<text class="tl halo" x="{X+dx:.1f}" y="{Y+dy:.1f}" text-anchor="{anc}">{lab}</text>')
out.append('</svg>')
if a.caption: out.append(f'<figcaption>{a.caption}</figcaption>')
out.append('</figure>')
print(''.join(out))
