# figures for P19 (chem.analysis2, chem.practical). Run from the course folder: py data/mk_fig_p19.py
# Writes scratch/p19_figs.txt (one <figure> per block) and prints overlap checks.
import sys, math
sys.path.insert(0, 'data'); sys.stdout.reconfigure(encoding='utf-8')
from fig import Fig, text_w, seg_rect_dist

OUT = {}


def T(f, x, y, s, a='s', cls='tl', box=True):
    """text; a = 's' start, 'm' middle, 'e' end; y = baseline"""
    w = text_w(s)
    if a == 'm':
        f.parts.append('<text class="%s tc" x="%s" y="%s">%s</text>' % (cls, f.f(x), f.f(y), s))
        cx = x
    elif a == 'e':
        f.parts.append('<text class="%s" x="%s" y="%s" text-anchor="end">%s</text>' % (cls, f.f(x), f.f(y), s))
        cx = x - w / 2
    else:
        f.parts.append('<text class="%s" x="%s" y="%s">%s</text>' % (cls, f.f(x), f.f(y), s))
        cx = x + w / 2
    if box:
        f.labels.append((cx, y - 4, w, 13.0, s))


def L(f, x1, y1, x2, y2, cls='ln', head=None, tag=''):
    mk = ' marker-end="url(#%s)"' % head if head else ''
    f.parts.append('<path class="%s" d="M%s %sL%s %s"%s/>' % (cls, f.f(x1), f.f(y1), f.f(x2), f.f(y2), mk))
    f.segs.append((x1, y1, x2, y2, tag or cls))


def P(f, pts, cls='ln', closed=False, tag=''):
    d = 'M' + 'L'.join('%s %s' % (f.f(x), f.f(y)) for x, y in pts) + ('Z' if closed else '')
    f.parts.append('<path class="%s" d="%s"/>' % (cls, d))
    for i in range(len(pts) - 1):
        f.segs.append((pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], tag or cls))


def report(name, f, vb):
    bad = f.check(vb=vb)
    print(name, 'OK' if not bad else bad)


# ---------------------------------------------------------------- 1. TLC plate
def tlc():
    f = Fig()
    X0, X1, YT, YB = 120, 250, 26, 246
    BASE, FRONT = 200, 50           # baseline and solvent front (y); 20 px per cm
    P(f, [(X0, YT), (X1, YT), (X1, YB), (X0, YB)], 'ln thick', closed=True, tag='plate')
    f.parts.append('<rect class="fa" x="100" y="222" width="170" height="30"/>')
    L(f, X0, BASE, X1, BASE, 'ln-m thin dash', tag='baseline')
    L(f, X0, FRONT, X1, FRONT, 'ln-m thin dash', tag='front')
    lanes = [145, 185, 225]
    spots = {0: [110], 1: [110, 146], 2: [146]}
    for i, x in enumerate(lanes):
        for y in spots[i]:
            f.parts.append('<ellipse class="fm2" cx="%d" cy="%d" rx="8" ry="5"/>' % (x, y))
            f.segs.append((x - 8, y, x + 8, y, 'spot'))
        f.parts.append('<circle class="fi" cx="%d" cy="%d" r="1.8"/>' % (x, BASE))
    for x, s in zip(lanes, ['X', 'mixture', 'Y']):
        T(f, x, 18, s, 'm')
    T(f, 110, FRONT + 4, 'solvent front', 'e')
    T(f, 110, BASE + 4, 'pencil baseline', 'e')
    T(f, 110, 238, 'solvent level', 'e')
    # distance arrows
    L(f, X1, 110, 282, 110, 'ln-m thin dash', tag='lead spot')
    L(f, 282, BASE, 282, 114, 'ln', 'ah', tag='arrow spot')
    L(f, X1, FRONT, 312, FRONT, 'ln-m thin dash', tag='lead front')
    L(f, 312, BASE, 312, FRONT + 4, 'ln', 'ah', tag='arrow front')
    T(f, 282, 168, '4.5 cm', 'm', 'tl halo')
    T(f, 312, 124, '7.5 cm', 'm', 'tl halo')
    return f, (0, 0, 340, 262)


# ---------------------------------------------------------------- 2. GLC chromatogram
PEAKS = [(1.8, 0.6, 4.0, '1'), (3.5, 1.0, 6.0, '2'), (5.4, 0.8, 2.5, '3')]   # Rt/min, base/cm(=min), height/cm


def glc():
    f = Fig()
    X0, Y0, SX, SY = 30, 130, 35.0, 12.0
    f.parts.append('<path class="ax" d="M%d %dH322" marker-end="url(#ahm)"/>' % (X0, Y0))
    f.parts.append('<path class="ax" d="M%d %dV16" marker-end="url(#ahm)"/>' % (X0, Y0))
    f.segs.append((X0, Y0, 322, Y0, 'x axis')); f.segs.append((X0, Y0, X0, 16, 'y axis'))
    for t in range(0, 9):
        x = X0 + SX * t
        L(f, x, Y0, x, Y0 + 4, 'ln-m thin', tag='tick')
        T(f, x, Y0 + 17, str(t), 'm', 'ts')
    T(f, X0 + 8, 12, 'detector response', 's')
    T(f, 176, 190, 'retention time / min', 'm')
    for rt, b, h, lab in PEAKS:
        sig = b / 4.0
        pts = []
        t = rt - 3 * sig
        while t <= rt + 3 * sig + 1e-9:
            y = Y0 - SY * h * math.exp(-0.5 * ((t - rt) / sig) ** 2)
            pts.append((X0 + SX * t, y))
            t += sig / 3
        d = 'M' + 'L'.join('%s %s' % (f.f(a), f.f(b_)) for a, b_ in pts)
        f.parts.append('<path class="c1 sw2" d="%s"/>' % d)
        for i in range(len(pts) - 1):
            f.segs.append((pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], 'peak' + lab))
        xa = X0 + SX * rt
        L(f, xa, Y0 - SY * h + 2, xa, Y0, 'ln-m thin dash', tag='drop' + lab)
        T(f, xa, Y0 - SY * h - 7, lab, 'm')
        T(f, xa, Y0 + 36, '%.1f' % rt, 'm')
    return f, (0, 0, 340, 200)


# ---------------------------------------------------------------- 3. GLC apparatus blocks
def glc_blocks():
    f = Fig()
    labs = ['carrier gas (N₂ or He)', 'injector (vaporises sample)', 'column in a hot oven', 'detector', 'recorder (chromatogram)']
    y = 10
    for i, s in enumerate(labs):
        f.parts.append('<rect class="fm s-acc" x="40" y="%d" width="240" height="32" rx="8"/>' % y)
        f.segs.append((40, y, 280, y, 'box')); f.segs.append((40, y + 32, 280, y + 32, 'box'))
        T(f, 160, y + 21, s, 'm', box=False)
        if i < len(labs) - 1:
            L(f, 160, y + 32, 160, y + 32 + 22, 'ln', 'ah', tag='arrow')
        y += 32 + 22
    return f, (0, 0, 320, y - 22 + 10)


# ---------------------------------------------------------------- 4. 13C spectrum of methyl propanoate
def c13():
    f = Fig()
    X0, X1, Y0 = 20, 296, 130     # delta 220 at X0, 0 at X1
    sx = (X1 - X0) / 220.0
    xd = lambda d: X1 - d * sx
    f.parts.append('<path class="ax" d="M%d %dH%d"/>' % (X0 - 6, Y0, X1 + 14)); f.segs.append((X0 - 6, Y0, X1 + 14, Y0, 'axis'))
    for d in [200, 150, 100, 50, 0]:
        L(f, xd(d), Y0, xd(d), Y0 + 4, 'ln-m thin', tag='tick')
        T(f, xd(d), Y0 + 17, str(d), 'm', 'ts')
    T(f, (X0 + X1) / 2, Y0 + 38, 'δ / ppm', 'm')
    lines = [(175, 42, '175 C=O'), (52, 100, '52 OCH₃'), (27, 74, '27 CH₂'), (9, 48, '9 CH₃')]
    for d, h, lab in lines:
        x = xd(d)
        L(f, x, Y0, x, Y0 - h, 'c1 sw3', tag='line%d' % d)
    # labels: placed above lines; lines are 60+ px apart vertically only where x is close
    T(f, xd(175), Y0 - 42 - 7, '175 C=O', 'm')
    T(f, xd(52), Y0 - 100 - 7, '52 OCH₃', 'm')
    T(f, xd(27), Y0 - 74 - 7, '27 CH₂', 'm')
    T(f, xd(9), Y0 - 48 - 7, '9 CH₃', 'm')
    return f, (0, 0, 322, 176)


# ---------------------------------------------------------------- 5. n+1: triplet and quartet
def nplus1():
    f = Fig()
    Y0, U = 118, 20.0
    for cx, pat, title, sub in [(85, [1, 2, 1], 'triplet', 'n = 2'), (245, [1, 3, 3, 1], 'quartet', 'n = 3')]:
        k = len(pat)
        sp = 14.0
        f.parts.append('<path class="ax" d="M%d %dH%d"/>' % (cx - 70, Y0, cx + 70)); f.segs.append((cx - 70, Y0, cx + 70, Y0, 'axis'))
        for i, p in enumerate(pat):
            x = cx + (i - (k - 1) / 2.0) * sp
            L(f, x, Y0, x, Y0 - p * U, 'c1 sw3', tag='line')
            T(f, x, Y0 - p * U - 8, str(p), 'm', 'tl')
        T(f, cx, Y0 + 20, '%s: %d lines' % (title, k), 'm')
        T(f, cx, Y0 + 38, '%s neighbouring H' % sub, 'm')
    return f, (0, 0, 330, 170)


# ---------------------------------------------------------------- 6. 1H spectrum of ethyl ethanoate (predicted)
def h1_ee():
    f = Fig()
    X0, X1, Y0 = 20, 304, 134     # delta 12 at X0, 0 at X1
    sx = (X1 - X0) / 12.0
    xd = lambda d: X1 - d * sx
    f.parts.append('<path class="ax" d="M%d %dH%d"/>' % (X0 - 8, Y0, X1 + 18)); f.segs.append((X0 - 8, Y0, X1 + 18, Y0, 'axis'))
    for d in range(0, 13, 2):
        L(f, xd(d), Y0, xd(d), Y0 + 4, 'ln-m thin', tag='tick')
        T(f, xd(d), Y0 + 17, str(d), 'm', 'ts')
    T(f, (X0 + X1) / 2, Y0 + 54, 'δ / ppm', 'm')
    K, SP = 30.0, 5.0       # px per unit of area; spacing between lines of a multiplet
    sigs = [(3.9, 2, [1, 3, 3, 1], '2H', 'q'), (2.3, 3, [1], '3H', 's'), (1.3, 3, [1, 2, 1], '3H', 't')]
    for d, nh, pat, lab, nm in sigs:
        k = len(pat); tot = float(sum(pat))
        for i, p in enumerate(pat):
            x = xd(d) + (i - (k - 1) / 2.0) * SP
            h = K * nh * p / tot
            L(f, x, Y0, x, Y0 - h, 'c1 sw2', tag='line')
        T(f, xd(d), Y0 + 36, lab, 'm')
    # TMS
    L(f, xd(0), Y0, xd(0), Y0 - 40, 'c1 sw2', tag='tms')
    T(f, xd(0), Y0 - 47, 'TMS', 'm')
    return f, (0, 0, 330, 196)


# ---------------------------------------------------------------- 7. four isomers of C4H10O (skeletal)
def isomers():
    f = Fig()
    def mol(ox, oy, pts, subs, name, n):
        P(f, [(ox + a, oy + b) for a, b in pts], 'ln thick', tag='chain')
        for (x1, y1, x2, y2) in subs:
            L(f, ox + x1, oy + y1, ox + x2, oy + y2, 'ln thick', tag='sub')
        return
    # butan-1-ol : chain 0,20 35,0 70,20 105,0 then OH end at 140,20
    oy = 40
    mol(10, oy, [(0, 20), (35, 0), (70, 20), (105, 0), (131, 14)], [], 'a', 4)
    T(f, 10 + 136, oy + 22, 'OH', 's')
    T(f, 10 + 70, oy + 62, 'butan-1-ol', 'm'); T(f, 10 + 70, oy + 80, '4 peaks', 'm', 'tl ta')
    # butan-2-ol : OH up from C2
    ox = 190
    mol(ox, oy, [(0, 20), (35, 0), (70, 20), (105, 0)], [(35, 0, 35, -14)], 'b', 4)
    T(f, ox + 35, oy - 22, 'OH', 'm')
    T(f, ox + 52, oy + 62, 'butan-2-ol', 'm'); T(f, ox + 52, oy + 80, '4 peaks', 'm', 'tl ta')
    # 2-methylpropan-1-ol : HO-C1, C2 with CH3 down, C3
    oy2 = 178
    mol(10, oy2, [(14, 12), (35, 0), (70, 20), (105, 0)], [(70, 20, 70, 52)], 'c', 3)
    # replace first atom by OH: start chain at x=13
    T(f, 10 + 2, oy2 + 22, 'OH', 'm')
    T(f, 80, oy2 + 100, '2-methylpropan-1-ol', 'm'); T(f, 80, oy2 + 118, '3 peaks', 'm', 'tl ta')
    # 2-methylpropan-2-ol : centre (ox+35, oy2+20): up OH, down CH3, left/right CH3
    ox = 200
    cx_, cy_ = ox + 35, oy2 + 22
    P(f, [(cx_ - 32, cy_ + 14), (cx_, cy_), (cx_ + 32, cy_ + 14)], 'ln thick', tag='chain')
    L(f, cx_, cy_, cx_, cy_ - 14, 'ln thick', tag='oh')
    L(f, cx_, cy_, cx_, cy_ + 34, 'ln thick', tag='me')
    T(f, cx_, cy_ - 22, 'OH', 'm')
    T(f, cx_, oy2 + 100, '2-methylpropan-2-ol', 'm'); T(f, cx_, oy2 + 118, '2 peaks', 'm', 'tl ta')
    return f, (0, 0, 340, 310)


# ---------------------------------------------------------------- 8. titration apparatus
def burette():
    f = Fig()
    P(f, [(120, 14), (120, 200)], 'ln', tag='tube'); P(f, [(140, 14), (140, 200)], 'ln', tag='tube')
    f.parts.append('<rect class="fa" x="121" y="70" width="18" height="130"/>')
    for k in range(6):
        y = 30 + 30 * k
        L(f, 113, y, 120, y, 'ln-m thin', tag='grad')
        T(f, 108, y + 4, str(10 * k), 'e', 'ts')
    L(f, 108, 205, 152, 205, 'ln thick', tag='tap')
    P(f, [(120, 200), (127, 224)], 'ln', tag='jet'); P(f, [(140, 200), (133, 224)], 'ln', tag='jet')
    P(f, [(117, 252), (117, 272), (70, 318), (190, 318), (143, 272), (143, 252)], 'ln', tag='flask')
    f.parts.append('<path class="fa" d="M95.5 292H164.5L190 318H70Z"/>')
    f.parts.append('<rect class="fm2" x="40" y="319" width="180" height="8"/>')
    T(f, 160, 209, 'tap', 's')
    L(f, 164, 106, 146, 106, 'ln-m thin', tag='ptr'); T(f, 170, 110, 'burette', 's')
    L(f, 196, 262, 148, 262, 'ln-m thin', tag='ptr'); T(f, 202, 266, 'conical flask', 's')
    L(f, 196, 300, 170, 300, 'ln-m thin', tag='ptr'); T(f, 202, 304, 'alkali + indicator', 's')
    T(f, 130, 346, 'white tile', 'm')
    return f, (0, 0, 340, 356)


# ---------------------------------------------------------------- 9. rate graph with best-fit line and gradient triangle
RATE_V = [10, 20, 30, 40, 50]
RATE_T = [130, 65, 43, 33, 26]
RATE_M, RATE_C = 0.7646, 0.0824          # least squares, recomputed in checks/chem.practical.py


def rategraph():
    f = Fig()
    X0, Y0, SX, SY = 50, 210, 4.5, 3.8
    xp = lambda v: X0 + SX * v
    yp = lambda v: Y0 - SY * v
    f.parts.append('<path class="ax" d="M%d %dH326" marker-end="url(#ahm)"/>' % (X0, Y0)); f.segs.append((X0, Y0, 326, Y0, 'ax'))
    f.parts.append('<path class="ax" d="M%d %dV24" marker-end="url(#ahm)"/>' % (X0, Y0)); f.segs.append((X0, Y0, X0, 24, 'ax'))
    for v in range(0, 61, 10):
        L(f, xp(v), Y0, xp(v), Y0 + 4, 'ln-m thin', tag='tick'); T(f, xp(v), Y0 + 17, str(v), 'm', 'ts')
    for v in range(0, 41, 10):
        L(f, X0, yp(v), X0 - 4, yp(v), 'ln-m thin', tag='tick'); T(f, X0 - 8, yp(v) + 4, str(v), 'e', 'ts')
    T(f, 190, Y0 + 38, 'volume of thiosulfate / cm³', 'm')
    T(f, X0 + 8, 18, '1000 / t / s⁻¹', 's')
    # best-fit line
    xa, xb = 5, 54
    L(f, xp(xa), yp(RATE_M * xa + RATE_C), xp(xb), yp(RATE_M * xb + RATE_C), 'c1 sw2', tag='fit')
    # triangle
    ya, yb = RATE_M * 10 + RATE_C, RATE_M * 50 + RATE_C
    L(f, xp(10), yp(ya), xp(50), yp(ya), 'ln-m thin dash', tag='tri'); L(f, xp(50), yp(ya), xp(50), yp(yb), 'ln-m thin dash', tag='tri')
    T(f, xp(30), yp(ya) + 17, 'Δx = 40', 'm', 'tl halo')
    T(f, xp(50) - 6, (yp(ya) + yp(yb)) / 2 + 4, 'Δy = 30.6', 'e', 'tl halo')
    for v, t in zip(RATE_V, RATE_T):
        x, y = xp(v), yp(1000.0 / t)
        P(f, [(x - 3.5, y - 3.5), (x + 3.5, y + 3.5)], 'c2 sw2', tag='pt'); P(f, [(x - 3.5, y + 3.5), (x + 3.5, y - 3.5)], 'c2 sw2', tag='pt')
    return f, (0, 0, 340, 262)


# ---------------------------------------------------------------- 10. temperature-time graph with extrapolation
TEMPS = [(0, 21.0), (1, 21.0), (2, 21.0), (3, 21.0), (5, 46.0), (6, 45.5), (7, 45.0), (8, 44.5), (9, 44.0), (10, 43.5)]


def tempgraph():
    f = Fig()
    X0, Y0, SX, SY = 50, 200, 26.0, 160.0 / 30
    xp = lambda t: X0 + SX * t
    yp = lambda v: Y0 - SY * (v - 20)
    f.parts.append('<path class="ax" d="M%d %dH326" marker-end="url(#ahm)"/>' % (X0, Y0)); f.segs.append((X0, Y0, 326, Y0, 'ax'))
    f.parts.append('<path class="ax" d="M%d %dV24" marker-end="url(#ahm)"/>' % (X0, Y0)); f.segs.append((X0, Y0, X0, 24, 'ax'))
    for t in range(0, 11, 2):
        L(f, xp(t), Y0, xp(t), Y0 + 4, 'ln-m thin', tag='tick'); T(f, xp(t), Y0 + 17, str(t), 'm', 'ts')
    for v in (20, 30, 40, 50):
        L(f, X0, yp(v), X0 - 4, yp(v), 'ln-m thin', tag='tick'); T(f, X0 - 8, yp(v) + 4, str(v), 'e', 'ts')
    T(f, 190, Y0 + 38, 'time / min', 'm')
    T(f, X0 + 8, 18, 'temperature / °C', 's')
    L(f, xp(0), yp(21.0), xp(4), yp(21.0), 'c1 sw2', tag='base')
    L(f, xp(4), yp(46.5), xp(10), yp(43.5), 'c1 sw2 dash', tag='extrap')
    L(f, xp(5), yp(46.0), xp(10), yp(43.5), 'c1 sw2', tag='cool')
    mid = (yp(21.0) + yp(46.5)) / 2
    L(f, xp(4), yp(46.5), xp(4), yp(21.0), 'ln-m thin dash', tag='vert')
    L(f, xp(4) - 0.01, mid, xp(4) - 0.01, yp(46.5) + 2, 'ln', 'ah', tag='dT')
    L(f, xp(4) - 0.01, mid, xp(4) - 0.01, yp(21.0) - 2, 'ln', 'ah', tag='dT')
    T(f, xp(4) - 8, mid + 4, 'ΔT = 25.5 °C', 'e', 'tl halo')
    T(f, xp(4), yp(46.5) - 14, 'zinc added at 4 min', 'm')
    T(f, xp(7.4), yp(37), 'extrapolate to 4 min', 'm')
    L(f, xp(7.4), yp(37) - 15, xp(7.4), yp(44.7) + 6, 'ln-m thin', tag='ptr')
    for t, v in TEMPS:
        x, y = xp(t), yp(v)
        P(f, [(x - 3.5, y - 3.5), (x + 3.5, y + 3.5)], 'c2 sw2', tag='pt'); P(f, [(x - 3.5, y + 3.5), (x + 3.5, y - 3.5)], 'c2 sw2', tag='pt')
    return f, (0, 0, 340, 252)


if __name__ == '__main__':
    out = []
    for name, fn in [('tlc', tlc), ('glc', glc), ('glcblocks', glc_blocks), ('c13', c13), ('nplus1', nplus1), ('h1ee', h1_ee), ('isomers', isomers), ('burette', burette), ('rategraph', rategraph), ('tempgraph', tempgraph)]:
        f, vb = fn()
        report(name, f, vb)
        out.append('### ' + name + ' ' + str(vb))
        out.append(''.join(f.parts))
    open('scratch/p19_figs.txt', 'w', encoding='utf-8').write('\n'.join(out))
    print('written')
