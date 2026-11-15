# wordmark.py: designs for a top-bar wordmark "ZERO TO A* Ω", drawn here by hand (no font files): storybook small
# capitals with spiky serifs, thick and hairline strokes, every letter a little crooked. The wood is the logo's:
# a white face with faint green rings inside dark-green bark; the star and the Ω are light crimson wood in dark
# crimson bark. The user chose example 1, "Log end" (2026-11-15): it is in shell.html (the top bar) between <!--wm--> and
# <!--/wm-->, and its colours are the .wm-* rules in style.css. app.js copies it into the heading of the Home page.
# Run: py engine/wordmark.py --shell      writes the wordmark into shell.html (after changing a letter or the rings)
#      py engine/wordmark.py [out.html]   a page of examples: rough bark, plank grain, more tilt
# Plain Python, no packages; the build does not run it.
import math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T, t = 0.21, 0.06          # thick and hairline strokes, as parts of the capital height

# ---------- pieces: every piece is a polygon [(x, y) …] in a box 1 high, y up, baseline 0 ----------
def seg(p, q, w1, w2=None):
    """a straight stroke from p to q, w1 wide at p and w2 at q"""
    w2 = w1 if w2 is None else w2
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy) or 1
    nx, ny = -dy / n, dx / n
    return [(p[0] + nx * w1 / 2, p[1] + ny * w1 / 2), (q[0] + nx * w2 / 2, q[1] + ny * w2 / 2),
            (q[0] - nx * w2 / 2, q[1] - ny * w2 / 2), (p[0] - nx * w1 / 2, p[1] - ny * w1 / 2)]

def curve(p0, p1, p2, w0, w1, w2, n=16):
    """a bent stroke along the quadratic curve p0, p1, p2; its width goes w0, w1, w2"""
    left, right = [], []
    for j in range(n + 1):
        u = j / n
        x = (1 - u) ** 2 * p0[0] + 2 * u * (1 - u) * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * u * (1 - u) * p1[1] + u * u * p2[1]
        dx = 2 * (1 - u) * (p1[0] - p0[0]) + 2 * u * (p2[0] - p1[0])
        dy = 2 * (1 - u) * (p1[1] - p0[1]) + 2 * u * (p2[1] - p1[1])
        m = math.hypot(dx, dy) or 1
        w = (1 - u) ** 2 * w0 + 2 * u * (1 - u) * w1 + u * u * w2
        left.append((x - dy / m * w / 2, y + dx / m * w / 2)); right.append((x + dy / m * w / 2, y - dx / m * w / 2))
    return left + right[::-1]

def arc(cx, cy, rx, ry, a0, a1, thin, thick, n=30):
    """part of a ring from angle a0 to a1 (degrees): thick at the sides, hairline at the top and bottom"""
    outer, inner = [], []
    for j in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * j / n)
        w = thin + (thick - thin) * abs(math.cos(a)) ** 1.4
        outer.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
        inner.append((cx + (rx - w) * math.cos(a), cy + (ry - w) * math.sin(a)))
    return outer + inner[::-1]

def oval(cx, cy, rx, ry, rot=0, n=36):
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    return [(cx + rx * math.cos(a) * c - ry * math.sin(a) * s, cy + rx * math.cos(a) * s + ry * math.sin(a) * c)
            for a in (2 * math.pi * j / n for j in range(n))]

def stem(x, y0=0.0, y1=1.0, w=T):
    """an upright thick stroke with a spiky serif to the left at its top and at its foot"""
    return [seg((x, y0), (x + 0.012, y1), w, w * 0.9),
            [(x - w / 2 - 0.17, y1 + 0.012), (x, y1), (x - w / 2 + 0.02, y1 - 0.09)],
            [(x - w / 2 - 0.19, y0 - 0.012), (x, y0), (x - w / 2 + 0.02, y0 + 0.09)],
            [(x + w / 2 + 0.11, y0 - 0.008), (x, y0), (x + w / 2 - 0.02, y0 + 0.07)]]

# ---------- the letters: (width, solid pieces, holes) ----------
def Z():
    return 0.84, [seg((0.05, 0.955), (0.78, 0.975), t * 1.3, t * 1.1), [(0.02, 1.0), (0.15, 0.95), (0.035, 0.6)],
                  seg((0.735, 0.975), (0.12, 0.03), T * 0.86, T * 1.02),
                  seg((0.06, 0.035), (0.8, 0.05), t * 1.2, t * 1.5), [(0.7, 0.0), (0.845, 0.02), (0.83, 0.4)]], []
def E():
    return 0.72, stem(0.2) + [seg((0.2, 0.965), (0.6, 0.972), t), [(0.52, 1.0), (0.66, 1.0), (0.635, 0.68)],
                              seg((0.2, 0.53), (0.47, 0.535), t), [(0.43, 0.67), (0.52, 0.53), (0.44, 0.39)],
                              seg((0.2, 0.032), (0.62, 0.03), t * 1.15), [(0.55, 0.0), (0.7, 0.0), (0.68, 0.33)]], []
def R():
    return 0.84, stem(0.2) + [arc(0.3, 0.725, 0.36, 0.275, 96, -96, t, T * 0.95),
                              curve((0.34, 0.47), (0.52, 0.3), (0.86, -0.07), 0.1, T * 1.05, 0.0)], []
def O():
    return 0.9, [oval(0.44, 0.5, 0.42, 0.525)], [oval(0.445, 0.5, 0.2, 0.42, -13)]
def Tt():
    return 0.84, [seg((0.03, 0.958), (0.8, 0.968), t * 1.2), [(0.0, 1.0), (0.13, 0.985), (0.02, 0.63)], [(0.7, 1.0), (0.83, 1.0), (0.815, 0.63)],
                  seg((0.42, 0.97), (0.41, 0.0), T * 0.9, T),
                  [(0.41 - T / 2 - 0.17, -0.012), (0.41, 0.0), (0.41 - T / 2 + 0.02, 0.09)], [(0.41 + T / 2 + 0.17, -0.012), (0.41, 0.0), (0.41 + T / 2 - 0.02, 0.09)]], []
def A():
    return 1.12, [seg((0.5, 1.03), (0.9, 0.0), T * 0.84, T * 1.04),                                   # the thick leg
                  curve((0.56, 1.0), (0.4, 0.42), (0.0, 0.03), 0.075, 0.06, 0.12), oval(0.03, 0.06, 0.075, 0.065),   # the swept leg and its ball
                  [(0.42, 0.985), (0.62, 1.03), (0.33, 1.13)],                                        # the spur at the top
                  seg((0.34, 0.37), (0.78, 0.375), t),
                  [(0.9 - T / 2 - 0.14, -0.012), (0.9, 0.0), (0.9 - T / 2 + 0.02, 0.08)], [(0.9 + T / 2 + 0.15, -0.012), (0.9, 0.0), (0.9 + T / 2 - 0.02, 0.08)]], []
def STAR():
    cx, cy, out = 0.36, 0.66, []
    for k, (ang, ln) in enumerate([(90, 0.36), (160, 0.33), (233, 0.35), (307, 0.33), (20, 0.35)]):
        a = math.radians(ang)
        ux, uy, px, py = math.cos(a), math.sin(a), -math.sin(a) * 0.088, math.cos(a) * 0.088
        # an asterisk's arm: narrow at the middle, widest near the end, then a point
        out.append([(cx - ux * 0.03, cy - uy * 0.03), (cx + ux * ln * 0.66 + px, cy + uy * ln * 0.66 + py), (cx + ux * ln, cy + uy * ln), (cx + ux * ln * 0.66 - px, cy + uy * ln * 0.66 - py)])
    return 0.72, out, []
def OMEGA():
    return 1.02, [arc(0.51, 0.585, 0.46, 0.445, -52, 232, t * 1.1, T * 0.98),
                  seg((0.33, 0.26), (0.36, 0.035), 0.16, 0.07), seg((0.69, 0.26), (0.66, 0.035), 0.16, 0.07),
                  seg((0.03, 0.035), (0.39, 0.04), t * 1.2), seg((0.63, 0.04), (0.99, 0.035), t * 1.2),
                  [(0.0, 0.0), (0.13, 0.0), (0.012, 0.3)], [(0.89, 0.0), (1.02, 0.0), (1.008, 0.3)]], []

# ---------- setting the name: (letter, height, tilt°, lift, gap after, group) ----------
B, S, M = 25.0, 17.5, 15.0     # heights of the large capitals, the small capitals and the small word "TO"
def name(tilt=1.0, bounce=1.0):
    q, b = tilt, bounce
    return [(Z, B, -4 * q, 0, 3.0, 'a'), (E, S, 3 * q, .5 * b, 2.6, 'a'), (R, S, -2 * q, -.3 * b, 1.6, 'a'), (O, S, 5 * q, .6 * b, 8.5, 'a'),
            (Tt, M, -5 * q, 1.2 * b, 2.4, 'a'), (O, M, 5 * q, 2.0 * b, 9.0, 'a'), (A, B, 2 * q, 0, 6.5, 'a'),
            (STAR, B * 1.02, 6 * q, 1.0 * b, 3.6, 'b'), (OMEGA, B, -3 * q, 0, 0, 'b')]
BASE, H = 31.5, 42

def jit(x, y, k):
    """a small, fixed unevenness: the letters are cut by hand"""
    return (x + 0.13 * math.sin(x * 1.9 + y * 2.7 + k), y + 0.13 * math.sin(x * 2.3 - y * 1.7 + k * 2.1))

def area(p): return sum(p[i][0] * p[(i + 1) % len(p)][1] - p[(i + 1) % len(p)][0] * p[i][1] for i in range(len(p))) / 2

def lay(letters, x=4.5):
    """-> {'a': path d, 'b': path d}, width, spans. Solid pieces all wind one way and holes the other (non-zero fill)."""
    d, spans = {'a': '', 'b': ''}, {'a': [1e9, -1e9], 'b': [1e9, -1e9]}
    for k, (glyph, size, tilt, lift, gap, grp) in enumerate(letters):
        w, solids, holes = glyph()
        ca, sa = math.cos(math.radians(-tilt)), math.sin(math.radians(-tilt))   # y is flipped below, so the tilt is too
        def place(p):
            px, py = (p[0] - w / 2) * size, (p[1] - 0.4) * size
            return jit(x + w * size / 2 + px * ca - py * sa, BASE - lift - 0.4 * size - (px * sa + py * ca), k)
        for poly, hole in [(p, False) for p in solids] + [(p, True) for p in holes]:
            pts = [place(p) for p in poly]
            if (area(pts) > 0) == hole: pts.reverse()
            d[grp] += 'M' + 'L'.join('%.2f %.2f' % p for p in pts) + 'Z'
        spans[grp][0] = min(spans[grp][0], x); spans[grp][1] = max(spans[grp][1], x + w * size)
        x += w * size + gap
    return d, math.ceil(x + 4.5), spans

# ---------- wood ----------
def rings(cx, cy, r1, seed, step=2.3):
    """growth rings round (cx, cy), wobbling a little, every third one heavier (as in the logo)"""
    thin, heavy, k, r = '', '', 0, 1.6
    while r < r1:
        pts = []
        for j in range(49):
            a = 2 * math.pi * j / 48
            rr = r * (1 + 0.035 * math.sin(3 * a + k * 1.3 + seed) + 0.02 * math.sin(7 * a + k * 0.7))
            pts.append('%.1f %.1f' % (cx + rr * math.cos(a), cy + rr * 0.92 * math.sin(a)))
        p = 'M' + 'L'.join(pts) + 'Z'
        if k % 3 == 0: heavy += p
        else: thin += p
        r += step * (0.85 + 0.3 * ((k * 7 + seed) % 3) / 2); k += 1
    return thin, heavy

def grain(x0, x1, seed):
    """the long grain of a plank, bending round two knots"""
    knots = [(x0 + (x1 - x0) * 0.3, 14.0), (x0 + (x1 - x0) * 0.78, 27.0)]
    thin, heavy = '', ''
    for k in range(20):
        y, pts = 2.0 + k * 2.0, []
        for j in range(61):
            px = x0 - 2 + (x1 - x0 + 4) * j / 60
            py = y + 0.45 * math.sin(px * 0.16 + k * 1.7 + seed)
            for kx, ky in knots:
                dx, dy = px - kx, py - ky
                py += (1 if dy >= 0 else -1) * 3.2 * math.exp(-(dx * dx) / 40 - (dy * dy) / 26)
            pts.append('%.1f %.1f' % (px, py))
        if k % 3 == 0: heavy += 'M' + 'L'.join(pts)
        else: thin += 'M' + 'L'.join(pts)
    for kx, ky in knots:
        for r in (0.7, 1.5):
            heavy += 'M' + 'L'.join('%.1f %.1f' % (kx + r * 1.5 * math.cos(2 * math.pi * j / 16), ky + r * math.sin(2 * math.pi * j / 16)) for j in range(16)) + 'Z'
    return thin, heavy

def wordmark(k, letters, wood='rings', rough=False, bark=1.25):
    d, w, spans = lay(letters)
    tex = {}
    for g in 'ab':
        x0, x1 = spans[g]
        seed = 1 if g == 'a' else 4
        thin, heavy = rings(x0 + (x1 - x0) * (0.42 if g == 'a' else 0.55), 19.0, x1 - x0, seed) if wood == 'rings' else grain(x0, x1, seed)
        tex[g] = '<g class="r%s" clip-path="url(#w%dc%s)"><path class="rt" d="%s"/><path class="rh" d="%s"/></g>' % (g, k, g, thin, heavy)
    filt = ('<filter id="w%dr" x="-5%%" y="-15%%" width="110%%" height="130%%"><feTurbulence type="fractalNoise" baseFrequency="0.55" numOctaves="2" seed="7"/>'
            '<feDisplacementMap in="SourceGraphic" scale="0.9" xChannelSelector="R" yChannelSelector="G"/></filter>' % k) if rough else ''
    fa = ' filter="url(#w%dr)"' % k if rough else ''
    return ('<svg class="wm" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" aria-hidden="true">'
            '<defs><clipPath id="w%dca"><path d="%s"/></clipPath><clipPath id="w%dcb"><path d="%s"/></clipPath>%s</defs>'
            '<path class="ba" style="stroke-width:%g"%s d="%s"/><path class="fa" d="%s"/>%s'
            '<path class="bb" style="stroke-width:%g"%s d="%s"/><path class="fb" d="%s"/>%s</svg>') % (
        w, H, k, d['a'], k, d['b'], filt, bark * 2, fa, d['a'], d['a'], tex['a'], bark * 2, fa, d['b'], d['b'], tex['b'])

def header_svg(pre='wm'):
    """the chosen wordmark, small enough to sit inside index.html: each outline once, the rings as ellipses.
    pre: the start of its ids (the top bar and the Home page each hold a copy, so their ids must differ)"""
    d, w, spans = lay(name())
    out = ['<svg class="wm" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" aria-hidden="true" focusable="false"><defs>' % (w, H, w, H)]
    for g in 'ab':
        out.append('<path id="%s-%s" d="%s"/><clipPath id="%s-c%s"><use href="#%s-%s"/></clipPath>' % (pre, g, d[g], pre, g, pre, g))
    out.append('</defs>')
    for g in 'ab':
        x0, x1 = spans[g]
        cx, seed = x0 + (x1 - x0) * (0.42 if g == 'a' else 0.55), (1 if g == 'a' else 4)
        far = max(cx - x0, x1 - cx) + 3
        thin, heavy, k, r = '', '', 0, 1.6
        while r < far:
            e = '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>' % (cx + 0.5 * math.sin(k * 2.1 + seed), 19 + 0.5 * math.cos(k * 1.3 + seed),
                                                                      r * (1 + 0.03 * math.sin(k * 1.3 + seed)), r * 0.92 * (1 - 0.03 * math.sin(k * 1.3 + seed)))
            if k % 3 == 0: heavy += e
            else: thin += e
            r += 2.3 * (0.85 + 0.3 * ((k * 7 + seed) % 3) / 2); k += 1
        out.append('<use class="wm-b%s" href="#%s-%s"/><use class="wm-f%s" href="#%s-%s"/><g class="wm-r%s" clip-path="url(#%s-c%s)"><g class="wm-rt">%s</g><g class="wm-rh">%s</g></g>' % (g, pre, g, g, pre, g, g, pre, g, thin, heavy))
    return ''.join(out) + '</svg>'

OPTIONS = [
    ('1', 'Log end', 'The logo\'s wood: a white face with faint green growth rings, dark-green bark round every letter. The star and the Ω are light crimson wood in dark crimson bark.',
     lambda k: wordmark(k, name())),
    ('2', 'Log end, rough bark', 'The same, with thicker bark and an uneven, sawn edge.',
     lambda k: wordmark(k, name(), rough=True, bark=1.7)),
    ('3', 'Plank', 'Long grain that bends round two knots, as on a sawn board, instead of rings.',
     lambda k: wordmark(k, name(), wood='grain')),
    ('4', 'Log end, topsy-turvy', 'Option 1 with the letters tilted and bounced twice as much.',
     lambda k: wordmark(k, name(2.0, 1.9))),
]

LOGO = '<svg viewBox="0 0 100 100" width="34" height="34"><circle cx="50" cy="50" r="50" fill="#123220"/><circle cx="50" cy="50" r="43.5" fill="#fff"/><text x="50" y="66" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="42" fill="#1E4D2B">AΩ</text></svg>'
CSS = '''
body{margin:0;font:16px/1.5 "Segoe UI",system-ui,sans-serif;background:#EEF1F3;color:#1B2430}
main{max-width:900px;margin:0 auto;padding:20px 16px 60px}
h1{font-size:1.5rem;margin:.2em 0}h2{font-size:1.15rem;margin:0}p{margin:.3em 0 .8em;color:#485363}
.opt{background:#fff;border:1px solid #D8DDE3;border-radius:12px;padding:16px;margin:18px 0}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:10px}.pair>div{min-width:0}@media(max-width:640px){.pair{grid-template-columns:1fr}}
.bar{display:flex;align-items:center;gap:10px;height:60px;padding:0 18px;border:1px solid #D8DDE3;border-radius:8px;margin-bottom:10px}
.bar .wm{height:38px}.big{padding:14px 18px;border-radius:8px;border:1px solid #D8DDE3}.big .wm{height:auto;width:100%}
.light{background:#fff}.dark{background:#19231F;border-color:#2F3E39}
/* the wordmark: the same colours in paper and chalkboard mode */
.wm{display:block;overflow:visible}
.ba{fill:#123220;stroke:#123220;stroke-linejoin:miter;stroke-miterlimit:2.5}.fa{fill:#FFFFFF}
.bb{fill:#5E0A18;stroke:#5E0A18;stroke-linejoin:miter;stroke-miterlimit:2.5}.fb{fill:#E8455E}
.ra path{fill:none;stroke:#1E4D2B}.rb path{fill:none;stroke:#8E0F26}
.rt{stroke-width:.32;opacity:.5}.rh{stroke-width:.6;opacity:.55}.rb .rt{opacity:.6}.rb .rh{opacity:.7}
'''
def page():
    out = ['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Wordmark examples</title><style>%s</style><main>' % CSS,
           '<h1>Wordmark examples, drawn by hand</h1><p>Each example is shown at its real size in the top bar (paper and chalkboard mode), then enlarged.</p>']
    k = 0
    for num, title, note, make in OPTIONS:
        a = []
        for cls in ('light', 'dark'):
            k += 2
            a.append('<div><div class="bar %s">%s%s</div><div class="big %s">%s</div></div>' % (cls, LOGO, make(k), cls, make(k + 1)))
        out.append('<section class="opt"><h2>%s. %s</h2><p>%s</p><div class="pair">%s</div></section>' % (num, title, note, ''.join(a)))
    return ''.join(out) + '</main></html>'

if __name__ == '__main__':
    if '--shell' in sys.argv:
        for path, pre in ((os.path.join(HERE, 'shell.html'), 'wm'),):
            src, svg = open(path, encoding='utf-8').read(), header_svg(pre)
            new, n = re.subn(r'<!--wm-->.*?<!--/wm-->', lambda m: '<!--wm-->' + svg + '<!--/wm-->', src, flags=re.S)
            if n != 1: raise SystemExit('%s: the <!--wm--> … <!--/wm--> marks are missing' % path)
            open(path, 'w', encoding='utf-8', newline='').write(new)
            print('wordmark in %s: %d bytes' % (os.path.basename(path), len(svg)))
        sys.exit(0)
    dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '.run', 'wordmark-examples.html')
    html = page()
    open(dest, 'w', encoding='utf-8', newline='').write(html)
    print('%d examples, %d KB, name %d units wide -> %s' % (len(OPTIONS), len(html) // 1024, lay(name())[1], os.path.normpath(dest)))
