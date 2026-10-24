# data/mk_fig_p15b.py: figures for chem.complexes (writes data/p15_figs/*.svg.txt and checks label gaps).
import math, os, sys, itertools
sys.path.insert(0, os.path.dirname(__file__))
from p15_lib import Fig, tw, f, node, pt, link

OUT = os.path.join(os.path.dirname(__file__), 'p15_figs')
os.makedirs(OUT, exist_ok=True)

def save(name, fig, vb):
    open(os.path.join(OUT, name + '.svg.txt'), 'w', encoding='utf-8').write(fig.svg(vb, 'x'))

# ------------------------------------------------------------------ d-orbital splitting
def level(g, x0, x1, y, owner, cls='ln thick'):
    g.line(x0, y, x1, y, cls, owner=owner)

def split_panel(g, oy, geom):
    title = 'Octahedral complex' if geom == 'oct' else 'Tetrahedral complex'
    g.text(190, oy + 16, title, 'tl tc', owner='title' + geom)
    if geom == 'oct':
        y_up, y_low = oy + 55, oy + 125
        up_lab, low_lab = 'dz²  dx²−y²', 'dxy  dxz  dyz'
        n_up, n_low = 2, 3
    else:
        y_up, y_low = oy + 66, oy + 114
        up_lab, low_lab = 'dxy  dxz  dyz', 'dz²  dx²−y²'
        n_up, n_low = 3, 2
    y_free = (n_up * y_up + n_low * y_low) / 5.0
    # energy axis
    g.text(2, oy + 36, 'energy', 'tl', owner='en' + geom)
    g.line(10, oy + 152, 10, oy + 44, 'ax', extra=' marker-end="url(#ahm)"', owner='axis' + geom)
    # free ion: five degenerate lines
    for i in range(5):
        x = 24 + i * 15
        level(g, x, x + 11, y_free, 'free%s%d' % (geom, i))
    g.text(24 + 2 * 15 + 5.5, y_free + 28, 'free ion', 'tl tc', owner='freeion' + geom)
    g.text(24 + 2 * 15 + 5.5, y_free + 45, 'same energy', 'tl tc', owner='same' + geom)
    # split levels
    xs = [160 + i * 26 for i in range(3)]
    for i in range(n_up): level(g, xs[i], xs[i] + 20, y_up, 'up%s%d' % (geom, i))
    for i in range(n_low): level(g, xs[i], xs[i] + 20, y_low, 'low%s%d' % (geom, i))
    # connectors (dashed, from the right end of the free-ion lines)
    xe = 24 + 4 * 15 + 11 + 6
    g.line(xe, y_free, xs[0] - 6, y_up, 'ln-m thin dash', owner='conU' + geom)
    g.line(xe, y_free, xs[0] - 6, y_low, 'ln-m thin dash', owner='conL' + geom)
    c_up = xs[0] + (xs[n_up - 1] + 20 - xs[0]) / 2
    c_low = xs[0] + (xs[n_low - 1] + 20 - xs[0]) / 2
    g.text(c_up, y_up - 9, up_lab, 'tl tc', owner='uplab' + geom)
    g.text(c_low, y_low + 20, low_lab, 'tl tc', owner='lowlab' + geom)
    # delta E double arrow
    xa = 276
    ym = (y_up + y_low) / 2
    g.line(xa, ym - 4, xa, y_up, 'c2 sw2', extra=' marker-end="url(#ah)"', owner='dEu' + geom)
    g.line(xa, ym + 4, xa, y_low, 'c2 sw2', extra=' marker-end="url(#ah)"', owner='dEl' + geom)
    g.text(xa + 12, ym + 4, 'ΔE', 'tl', owner='dE' + geom)

def fig_split():
    g = Fig()
    split_panel(g, 0, 'oct')
    split_panel(g, 180, 'tet')
    return g

def wavy(x0, y0, x1, y1, amp=4.0, n=3):
    """wavy arrow path from (x0,y0) to (x1,y1)"""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    px, py = -uy, ux
    seg = L / (2 * n)
    d = 'M%s %s' % (f(x0), f(y0))
    for i in range(2 * n):
        s = 1 if i % 2 == 0 else -1
        cx = x0 + ux * seg * (i + 0.5) + px * amp * s * 2
        cy = y0 + uy * seg * (i + 0.5) + py * amp * s * 2
        ex = x0 + ux * seg * (i + 1); ey = y0 + uy * seg * (i + 1)
        d += 'Q%s %s %s %s' % (f(cx), f(cy), f(ex), f(ey))
    return d

def fig_promote():
    g = Fig()
    y_up, y_low = 50, 130
    xs = [150 + i * 26 for i in range(3)]
    g.text(2, 14, 'energy', 'tl', owner='en')
    g.line(10, 150, 10, 24, 'ax', extra=' marker-end="url(#ahm)"', owner='axis')
    for i in range(2): level(g, xs[i], xs[i] + 20, y_up, 'u%d' % i)
    for i in range(3): level(g, xs[i], xs[i] + 20, y_low, 'l%d' % i)
    g.text(xs[1] + 28, y_up + 4, 'higher set', 'tl', owner='hs')
    g.text(xs[2] + 28, y_low + 4, 'lower set', 'tl', owner='ls')
    ex = xs[0] + 10
    g.line(ex, y_low - 3, ex, y_low - 24, 'c1 sw2', extra=' marker-end="url(#ahs-red)"', owner='e0')
    g.line(ex, y_up - 3, ex, y_up - 24, 'c1 sw2 dash', extra=' marker-end="url(#ahs-red)"', owner='e1')
    g.line(130, y_low - 8, 130, y_up + 2, 'ln', extra=' marker-end="url(#ah)"', owner='prom')
    g.text(122, (y_low + y_up) / 2 + 4, 'promotion', 'tl', anchor='end', owner='promlab')
    g.path(wavy(36, 52, 104, 52, 3.0, 3), 'c3 sw2', ' marker-end="url(#ah)"')
    g.text(36, 38, 'light absorbed', 'tl', owner='light')
    g.text(36, 76, 'ΔE = hf', 'tl', owner='dE')
    return g

# ------------------------------------------------------------------ octahedral projection helpers
SC = 1.0
VEC = {  # screen vector, depth, for the six octahedral directions (names are axes)
    '+z': (0, -44, 0), '-z': (0, 44, 0),
    '+y': (44, 0, 0), '-y': (-44, 0, 0),
    '+x': (-28, 24, 1), '-x': (28, -24, -1),
}

def oct_panel(g, cx, cy, ligs, metal, tag, scale=1.0):
    """ligs: dict direction -> label (text ligand drawn as label). returns positions"""
    m = node(g, cx, cy, metal, owner='M' + tag)
    for d, lab in ligs.items():
        dx, dy, depth = VEC[d]
        dx, dy = dx * scale, dy * scale
        L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        ex, ey = cx + dx, cy + dy
        w = tw(lab); hw, hh = w / 2, 6.5
        tx = hw / abs(ux) if abs(ux) > 1e-9 else 1e9
        ty = hh / abs(uy) if abs(uy) > 1e-9 else 1e9
        e = min(tx, ty)
        lc = (ex + ux * (6.5 + e), ey + uy * (6.5 + e))
        node(g, lc[0], lc[1], lab, owner='L%s%s' % (tag, d))
        kind = 'plain' if depth == 0 else ('wedge' if depth > 0 else 'hash')
        link(g, m, pt(ex, ey), kind, owner='b%s%s' % (tag, d), gap=6)

def fig_oct_iso():
    g = Fig()
    base = {'+z': 'NH₃', '-z': 'NH₃', '+y': 'NH₃', '-y': 'NH₃', '+x': 'NH₃', '-x': 'NH₃'}
    trans = dict(base); trans['+z'] = 'H₂O'; trans['-z'] = 'H₂O'
    cis = dict(base); cis['+z'] = 'H₂O'; cis['+y'] = 'H₂O'
    oct_panel(g, 85, 92, trans, 'Co', 'tr')
    oct_panel(g, 255, 92, cis, 'Co', 'ci')
    g.text(85, 180, 'trans', 'tl tc'); g.text(255, 180, 'cis', 'tl tc')
    return g

# ------------------------------------------------------------------ square planar isomers
def sq_panel(g, cx, cy, labs, tag):
    m = node(g, cx, cy, 'Pt', owner='Pt' + tag)
    for (dx, dy), lab in zip(((-34, -30), (34, -30), (-34, 30), (34, 30)), labs):
        L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        w = tw(lab); tx = (w / 2) / abs(ux); ty = 6.5 / abs(uy); e = min(tx, ty)
        lc = (cx + dx + ux * (6.5 + e), cy + dy + uy * (6.5 + e))
        node(g, lc[0], lc[1], lab, owner='L%s%d%d' % (tag, dx, dy))
        link(g, m, pt(cx + dx, cy + dy), 'plain', owner='b%s%d%d' % (tag, dx, dy))

def fig_sq_iso():
    g = Fig()
    sq_panel(g, 85, 62, ['H₃N', 'Cl', 'Cl', 'NH₃'], 'tr')
    sq_panel(g, 255, 62, ['H₃N', 'NH₃', 'Cl', 'Cl'], 'ci')
    g.text(85, 138, 'trans', 'tl tc'); g.text(255, 138, 'cis', 'tl tc')
    return g

# ------------------------------------------------------------------ chirality check (3D, octahedron)
AXES = ['+x', '-x', '+y', '-y', '+z', '-z']
VEC3 = {'+x': (1, 0, 0), '-x': (-1, 0, 0), '+y': (0, 1, 0), '-y': (0, -1, 0), '+z': (0, 0, 1), '-z': (0, 0, -1)}
def name_of(v):
    for k, w in VEC3.items():
        if tuple(w) == tuple(v): return k
def rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            # determinant
            m = [[0] * 3 for _ in range(3)]
            for i in range(3): m[i][perm[i]] = signs[i]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1: mats.append(m)
    return mats
ROT = rotations()
def apply(m, v): return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))
def config_key(pairs, waters):
    return (frozenset(frozenset(p) for p in pairs), frozenset(waters))
def transform(cfg, f_):
    pairs, waters = cfg
    return (frozenset(frozenset(name_of(f_(VEC3[a])) for a in p) for p in pairs), frozenset(name_of(f_(VEC3[a])) for a in waters))
def is_chiral(pairs, waters):
    cfg = config_key(pairs, waters)
    mirror = transform(cfg, lambda v: (v[0], -v[1], v[2]))
    for m in ROT:
        if transform(cfg, lambda v, m=m: apply(m, v)) == mirror:
            return False
    return True

TRIS = [('+x', '-y'), ('+y', '-z'), ('+z', '-x')]
CIS2 = ([('+x', '+z'), ('+y', '-z')], ['-x', '-y'])
TRANS2 = ([('+x', '+y'), ('-x', '-y')], ['+z', '-z'])

# ------------------------------------------------------------------ optical isomers
def donor_dot(g, cx, cy, d, scale):
    dx, dy, depth = VEC[d]
    x, y = cx + dx * scale, cy + dy * scale
    r = 3.6 if depth > 0 else (2.4 if depth < 0 else 3.0)
    g.circle(x, y, r, 'fi')
    return x, y

def chelate_panel(g, cx, cy, pairs, waters, mirror, tag, scale=0.8):
    sgn = -1 if mirror else 1
    def P(d):
        dx, dy, depth = VEC[d]
        if mirror: d = {'+y': '-y', '-y': '+y'}.get(d, d)   # reflect y (the horizontal axis)
        return d
    m = node(g, cx, cy, 'Ni', owner='Ni' + tag)
    pos = {}
    allpos = set(a for p in pairs for a in p) | set(waters)
    for d in AXES:
        dx, dy, depth = VEC[d]
        if mirror: dx = -dx          # literal mirror image about the vertical line
        x, y = cx + dx * scale, cy + dy * scale
        pos[d] = (x, y, depth)
        kind = 'plain' if depth == 0 else ('wedge' if depth > 0 else 'hash')
        if d in waters:
            L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
            lab = 'H₂O'; w = tw(lab); hw, hh = w / 2, 6.5
            tx = hw / abs(ux) if abs(ux) > 1e-9 else 1e9
            ty = hh / abs(uy) if abs(uy) > 1e-9 else 1e9
            e = min(tx, ty)
            lc = (x + ux * (6.5 + e), y + uy * (6.5 + e))
            node(g, lc[0], lc[1], lab, owner='W%s%s' % (tag, d))
            link(g, m, pt(x, y), kind, owner='bw%s%s' % (tag, d), gap=6, w=6.0)
        else:
            link(g, m, pt(x, y), 'thin', owner='bn%s%s' % (tag, d), gap=6)
            r = 3.6 if depth > 0 else (2.4 if depth < 0 else 3.0)
            g.circle(x, y, r, 'fi')
    for (a, b) in pairs:
        (x0, y0, _), (x1, y1, _) = pos[a], pos[b]
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ox, oy = mx - cx, my - cy
        L = math.hypot(ox, oy) or 1
        k = 15
        qx, qy = mx + ox / L * k, my + oy / L * k
        g.path('M%s %sQ%s %s %s %s' % (f(x0), f(y0), f(qx), f(qy), f(x1), f(y1)), 'ln thick')
        # record the arc as a few segments for the label check
        for t in (0.25, 0.5, 0.75):
            ax = (1 - t) ** 2 * x0 + 2 * t * (1 - t) * qx + t * t * x1
            ay = (1 - t) ** 2 * y0 + 2 * t * (1 - t) * qy + t * t * y1
            g.segs.append(('arc' + tag, ax, ay, ax + 0.1, ay + 0.1))
    return pos

def fig_optical():
    g = Fig()
    xm = 170
    # row 1: [Ni(en)3]2+ and mirror image
    chelate_panel(g, 90, 78, TRIS, [], False, 'a1')
    chelate_panel(g, 250, 78, TRIS, [], True, 'a2')
    g.line(xm, 10, xm, 150, 'ln-m thin dash', owner='mirror1')
    g.text(xm, 170, 'mirror', 'tl tc', owner='mirlab1')
    g.text(90, 190, '[Ni(en)₃]²⁺', 'tl tc', owner='n1'); g.text(250, 190, '[Ni(en)₃]²⁺', 'tl tc', owner='n2')
    # row 2: cis-[Ni(en)2(H2O)2]2+ and mirror image
    chelate_panel(g, 90, 290, CIS2[0], CIS2[1], False, 'b1')
    chelate_panel(g, 250, 290, CIS2[0], CIS2[1], True, 'b2')
    g.line(xm, 222, xm, 362, 'ln-m thin dash', owner='mirror2')
    g.text(xm, 382, 'mirror', 'tl tc', owner='mirlab2')
    g.text(90, 402, 'cis-[Ni(en)₂(H₂O)₂]²⁺', 'tl tc', owner='n3'); g.text(250, 402, 'cis-[Ni(en)₂(H₂O)₂]²⁺', 'tl tc', owner='n4')
    return g

if __name__ == '__main__':
    print('tris chiral:', is_chiral(TRIS, []), '| cis2 chiral:', is_chiral(*CIS2), '| trans2 chiral:', is_chiral(*TRANS2))
    g = fig_split(); g.report('split'); save('split', g, '0 0 340 345')
    g = fig_promote(); g.report('promote'); save('promote', g, '0 0 340 165')
    g = fig_sq_iso(); g.report('sqiso'); save('sqiso', g, '0 10 340 150')
    g = fig_oct_iso(); g.report('octiso'); save('octiso', g, '0 25 340 170')
    g = fig_optical(); g.report('optical', min_gap=3); save('optical', g, '0 0 340 415')
    for n in ['split', 'promote', 'sqiso', 'octiso', 'optical']:
        gg = globals()['fig_' + {'sqiso': 'sq_iso', 'octiso': 'oct_iso'}.get(n, n)]()
        xs = [b[1] for b in gg.boxes] + [b[3] for b in gg.boxes] + [s[1] for s in gg.segs] + [s[3] for s in gg.segs]
        ys = [b[2] for b in gg.boxes] + [b[4] for b in gg.boxes] + [s[2] for s in gg.segs] + [s[4] for s in gg.segs]
        print(n, 'x', round(min(xs)), round(max(xs)), 'y', round(min(ys)), round(max(ys)))
