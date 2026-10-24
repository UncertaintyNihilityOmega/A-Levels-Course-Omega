# data/mk_fig_p17.py: figures for chem.org.acyl and chem.org.nitrogen (P17).
# Writes data/p17_figs/<name>.svg.txt (the <svg> element only) and prints label/segment problems.
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from p15_lib import Fig, tw, f, node, pt, link

OUT = os.path.join(os.path.dirname(__file__), 'p17_figs')
os.makedirs(OUT, exist_ok=True)


def bounds(g, pad=14):
    xs, ys = [], []
    for (_, x0, y0, x1, y1) in g.boxes:
        xs += [x0, x1]; ys += [y0, y1]
    for (_, x0, y0, x1, y1) in g.segs:
        xs += [x0, x1]; ys += [y0, y1]
    return min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad


def save(name, g, label, vb=None):
    x0, y0, x1, y1 = bounds(g) if vb is None else vb
    vbs = '%s %s %s %s' % (f(x0), f(y0), f(x1 - x0), f(y1 - y0))
    open(os.path.join(OUT, name + '.svg.txt'), 'w', encoding='utf-8').write(g.svg(vbs, label))
    print('%s: viewBox %s' % (name, vbs))
    g.report(name)


def dbl(g, a, b, off=2.6, owner=None):
    """double bond between two descriptors (node or pt)"""
    dx, dy = b[1] - a[1], b[2] - a[2]
    L = math.hypot(dx, dy)
    nx, ny = -dy / L * off, dx / L * off
    for s in (-1, 1):
        a2 = (a[0], a[1] + s * nx, a[2] + s * ny, a[3], a[4])
        b2 = (b[0], b[1] + s * nx, b[2] + s * ny, b[3], b[4])
        link(g, a2, b2, 'plain', owner=owner)


def curly(g, x0, y0, cx, cy, x1, y1, owner, cls='c1 sw2', head='ahs-red'):
    g.path('M%s %sQ%s %s %s %s' % (f(x0), f(y0), f(cx), f(cy), f(x1), f(y1)), cls, ' marker-end="url(#%s)"' % head)
    pts = []
    for i in range(0, 9):
        t = i / 8
        pts.append(((1 - t) ** 2 * x0 + 2 * t * (1 - t) * cx + t * t * x1, (1 - t) ** 2 * y0 + 2 * t * (1 - t) * cy + t * t * y1))
    for p, q in zip(pts, pts[1:]):
        g.segs.append((owner, p[0], p[1], q[0], q[1]))


def arrow(g, x0, y0, x1, y1, owner, cls='ln'):
    g.line(x0, y0, x1, y1, cls, owner=owner, extra=' marker-end="url(#ah)"')


def ring(g, cx, cy, owner='ring', r=28):
    v = [(cx, cy - r), (cx + r * 0.866, cy - r / 2), (cx + r * 0.866, cy + r / 2), (cx, cy + r), (cx - r * 0.866, cy + r / 2), (cx - r * 0.866, cy - r / 2)]
    d = 'M' + 'L'.join('%s %s' % (f(x), f(y)) for x, y in v) + 'Z'
    g.path(d, 'ln thick')
    g.circle(cx, cy, 17, 'ln')
    for i in range(6):
        a, b = v[i], v[(i + 1) % 6]
        g.segs.append((owner, a[0], a[1], b[0], b[1]))
    return v


def lp(g, x, y, ux, uy):
    g.lonepair(x, y, ux, uy)


# ---------------------------------------------------------------- acyl chlorides
def fig_acyl():
    g = Fig()
    # ethanoyl chloride
    c = pt(65, 55); me = pt(30, 75)
    o = node(g, 65, 22, 'O', 'O1'); cl = node(g, 100, 75, 'Cl', 'Cl1')
    link(g, me, c, 'plain', owner='b1'); dbl(g, c, o, owner='co1'); link(g, c, cl, 'plain', owner='ccl1')
    g.text(140, 56, 'ethanoyl chloride', 'tl', owner='n1')
    g.text(140, 74, 'CH₃COCl', 'tl', owner='f1')
    # propanoyl chloride (carbonyl carbon at the lower vertex, O below)
    yb = 130
    m = pt(30, yb + 20); ch2 = pt(65, yb); c2 = pt(100, yb + 20)
    o2 = node(g, 100, yb + 48, 'O', 'O2'); cl2 = node(g, 135, yb, 'Cl', 'Cl2')
    link(g, m, ch2, 'plain', owner='b2a'); link(g, ch2, c2, 'plain', owner='b2b'); dbl(g, c2, o2, owner='co2'); link(g, c2, cl2, 'plain', owner='ccl2')
    g.text(178, yb + 22, 'propanoyl chloride', 'tl', owner='n2')
    g.text(178, yb + 40, 'CH₃CH₂COCl', 'tl', owner='f2')
    # benzoyl chloride
    cy = 290
    v = ring(g, 60, cy)
    top_right = pt(v[1][0], v[1][1])
    cc = pt(v[1][0] + 30.3, v[1][1] - 17.5)
    o3 = node(g, cc[1], cc[2] - 34, 'O', 'O3'); cl3 = node(g, cc[1] + 33, cc[2] + 19, 'Cl', 'Cl3')
    link(g, top_right, cc, 'plain', owner='b3'); dbl(g, cc, o3, owner='co3'); link(g, cc, cl3, 'plain', owner='ccl3')
    g.text(190, cy - 6, 'benzoyl chloride', 'tl', owner='n3')
    g.text(190, cy + 12, 'C₆H₅COCl', 'tl', owner='f3')
    save('acyl_structures', g, 'Skeletal formulas of ethanoyl chloride, propanoyl chloride and benzoyl chloride, each with a C=O group and a Cl atom on the same carbon')


# ---------------------------------------------------------------- addition-elimination mechanism
def fig_mech():
    g = Fig()
    # panel 1: H2O + CH3COCl
    C = pt(170, 90)
    O = node(g, 170, 54, 'O', 'Oc')
    ME = node(g, 133, 111, 'CH₃', 'me1')
    CL = node(g, 207, 111, 'Cl', 'cl1')
    dbl(g, C, O, owner='co')
    link(g, C, ME, 'plain', owner='cme'); link(g, C, CL, 'plain', owner='ccl')
    g.text(54, 66, 'H₂O', 'tl tc', owner='h2o')
    # lone pair on the O of water (right side of its label)
    g.circle(70, 58, 1.7, 'fi'); g.circle(70, 64, 1.7, 'fi')
    curly(g, 74, 60, 112, 46, 156, 82, 'arrow1')
    curly(g, 173, 72, 205, 70, 181, 50, 'arrow2')
    g.text(181, 87, 'δ+', 'tl ta', owner='dplus')
    g.text(190, 40, 'δ−', 'tl ta', owner='dminus')
    # step 1 arrow
    arrow(g, 170, 136, 170, 176, 'step1')
    g.text(180, 160, 'step 1', 'tl', owner='s1')
    # panel 2: intermediate (plus shape), then products
    cy = 232 + 36
    C2 = pt(95, cy)
    O2 = node(g, 95, cy - 38, 'O⁻', 'Om')
    ME2 = node(g, 51, cy, 'CH₃', 'me2')
    CL2 = node(g, 139, cy, 'Cl', 'cl2')
    W2 = node(g, 95, cy + 38, 'H₂O⁺', 'wp')
    link(g, C2, O2, 'plain', owner='c2o'); link(g, C2, ME2, 'plain', owner='c2me'); link(g, C2, CL2, 'plain', owner='c2cl'); link(g, C2, W2, 'plain', owner='c2w')
    # lone pair on O- (right) and the arrow to the C-O bond
    g.circle(112, cy - 44, 1.7, 'fi'); g.circle(112, cy - 38, 1.7, 'fi')
    curly(g, 117, cy - 45, 128, cy - 22, 99, cy - 20, 'arrow3')
    curly(g, 118, cy - 3, 127, cy - 24, 139, cy - 15, 'arrow4')
    arrow(g, 168, cy, 206, cy, 'step2')
    g.text(187, cy - 8, 'step 2', 'tl tc', owner='s2')
    # product: ethanoic acid protonated + Cl-
    C3 = pt(265, cy)
    O3 = node(g, 265, cy - 36, 'O', 'Op')
    ME3 = node(g, 231, cy + 19, 'CH₃', 'me3')
    W3 = node(g, 301, cy + 19, 'OH₂⁺', 'w3')
    dbl(g, C3, O3, owner='c3o'); link(g, C3, ME3, 'plain', owner='c3me'); link(g, C3, W3, 'plain', owner='c3w')
    g.text(265, cy + 64, '+ Cl⁻', 'tl tc', owner='clm')
    arrow(g, 265, cy + 76, 265, cy + 110, 'step3')
    g.text(275, cy + 98, 'loses H⁺', 'tl', owner='s3')
    g.text(265, cy + 134, 'CH₃COOH + HCl', 'tl tc', owner='prod')
    save('acyl_mechanism', g, 'Addition-elimination mechanism of ethanoyl chloride with water: water attacks the delta-plus carbon, a tetrahedral intermediate forms, then the C=O bond reforms and chloride leaves, giving ethanoic acid and hydrogen chloride')


# ---------------------------------------------------------------- amines: classes
def fig_amines():
    g = Fig()
    # primary: ethylamine
    a = pt(30, 70); b = pt(65, 50); n = node(g, 100, 70, 'NH₂', 'n1')
    link(g, a, b, 'plain', owner='p1'); link(g, b, n, 'plain', owner='p2')
    g.text(150, 58, 'ethylamine', 'tl', owner='t1')
    g.text(150, 76, 'primary (1°)', 'tl ta', owner='t1b')
    # secondary: dimethylamine
    y = 140
    a = pt(30, y + 20); n = node(g, 65, y, 'NH', 'n2'); c = pt(100, y + 20)
    link(g, a, n, 'plain', owner='s1'); link(g, n, c, 'plain', owner='s2')
    g.text(150, y + 10, 'dimethylamine', 'tl', owner='t2')
    g.text(150, y + 28, 'secondary (2°)', 'tl ta', owner='t2b')
    # tertiary: trimethylamine
    y = 230
    n = node(g, 65, y, 'N', 'n3')
    a = pt(65, y - 34); b = pt(35, y + 17); c = pt(95, y + 17)
    link(g, n, a, 'plain', owner='q1'); link(g, n, b, 'plain', owner='q2'); link(g, n, c, 'plain', owner='q3')
    g.text(150, y + 2, 'trimethylamine', 'tl', owner='t3')
    g.text(150, y + 20, 'tertiary (3°)', 'tl ta', owner='t3b')
    save('amine_classes', g, 'Skeletal formulas of ethylamine (primary), dimethylamine (secondary) and trimethylamine (tertiary)')


# ---------------------------------------------------------------- lone pair availability
def fig_lonepair():
    g = Fig()
    # row 1 ethylamine
    y = 0
    a = pt(30, y + 60); b = pt(65, y + 40); n = node(g, 100, y + 60, 'NH₂', 'n1')
    link(g, a, b, 'plain', owner='r1a'); link(g, b, n, 'plain', owner='r1b')
    g.circle(97, y + 45, 1.7, 'fi'); g.circle(103, y + 45, 1.7, 'fi')
    g.text(150, y + 46, 'alkyl group pushes electrons', 'tl', owner='l1a')
    g.text(150, y + 64, 'towards N: lone pair free', 'tl', owner='l1b')
    # row 2 phenylamine
    cy = 150
    v = ring(g, 60, cy)
    bot = pt(v[3][0], v[3][1])
    n2 = node(g, 60, cy + 70, 'NH₂', 'n2')
    link(g, bot, n2, 'plain', owner='r2b')
    g.circle(40, cy + 63, 1.7, 'fi'); g.circle(40, cy + 69, 1.7, 'fi')
    curly(g, 38, cy + 58, 38, cy + 44, 57, cy + 44, 'arrow5')
    g.text(120, cy + 56, 'lone pair drawn into', 'tl', owner='l2a')
    g.text(120, cy + 74, 'the ring: less available', 'tl', owner='l2b')
    # row 3 ethanamide
    y = 285
    me = pt(30, y + 60); c = pt(65, y + 40); o = node(g, 65, y + 6, 'O', 'o3'); n3 = node(g, 100, y + 60, 'NH₂', 'n3')
    link(g, me, c, 'plain', owner='r3a'); dbl(g, c, o, owner='r3co'); link(g, c, n3, 'plain', owner='r3cn')
    g.circle(104, y + 47, 1.7, 'fi'); g.circle(110, y + 47, 1.7, 'fi')
    curly(g, 104, y + 42, 92, y + 28, 72, y + 41, 'arrow6')
    curly(g, 59, y + 30, 40, y + 22, 54, y + 12, 'arrow7')
    g.text(150, y + 38, 'lone pair spread over', 'tl', owner='l3a')
    g.text(150, y + 56, 'N, C and O: not available', 'tl', owner='l3b')
    save('lonepair', g, 'Lone pair on nitrogen in ethylamine, phenylamine and ethanamide: free in ethylamine, drawn into the ring in phenylamine and spread over the C=O group in ethanamide')


# ---------------------------------------------------------------- glycine forms
def fig_glycine():
    g = Fig()
    def gly(y, nlab, olab, name, sub):
        N = node(g, 60, y + 20, nlab, 'N' + name)
        ca = pt(95, y); cc = pt(130, y + 20)
        o = node(g, 130, y - 14, 'O', 'O' + name)
        ox = node(g, 165, y, olab, 'X' + name)
        link(g, N, ca, 'plain', owner='a' + name); link(g, ca, cc, 'plain', owner='b' + name)
        dbl(g, cc, o, owner='c' + name); link(g, cc, ox, 'plain', owner='d' + name)
        g.text(208, y + 14, sub[0], 'tl', owner='s' + name)
        g.text(208, y + 32, sub[1], 'tl ta', owner='s2' + name)
    gly(60, 'H₃N⁺', 'OH', 'cation', ('low pH', 'charge +1'))
    gly(180, 'H₃N⁺', 'O⁻', 'zwit', ('at the pI', 'net charge 0'))
    gly(300, 'H₂N', 'O⁻', 'anion', ('high pH', 'charge −1'))
    for y in (136, 256):
        g.text(120, y, '↓ OH⁻    ↑ H⁺', 'tl tc', owner='tr%d' % y)
    save('glycine_forms', g, 'Glycine at low pH as a cation, at its isoelectric point as a zwitterion, and at high pH as an anion; adding OH minus moves down the figure and adding H plus moves up')


# ---------------------------------------------------------------- dipeptide
def fig_dipeptide():
    g = Fig()
    n1 = node(g, 30, 80, 'H₂N', 'n1'); ca = pt(65, 60); c1 = pt(100, 80)
    o1 = node(g, 100, 114, 'O', 'o1')
    n2 = node(g, 135, 60, 'NH', 'n2'); ca2 = pt(170, 80); c2 = pt(205, 60)
    me = node(g, 170, 114, 'CH₃', 'me')
    o2 = node(g, 205, 26, 'O', 'o2'); oh = node(g, 240, 80, 'OH', 'oh')
    link(g, n1, ca, 'plain', owner='b1'); link(g, ca, c1, 'plain', owner='b2'); dbl(g, c1, o1, owner='co1'); link(g, c1, n2, 'plain', owner='b3')
    link(g, n2, ca2, 'plain', owner='b4'); link(g, ca2, me, 'plain', owner='b5'); link(g, ca2, c2, 'plain', owner='b6')
    dbl(g, c2, o2, owner='co2'); link(g, c2, oh, 'plain', owner='b7')
    g.line(118, 70, 118, 52, 'ln-m thin', owner='ptr')
    # pointer label above the CO-NH link
    g.text(118, 44, 'peptide (amide) bond', 'tl tc', owner='pl')
    save('dipeptide', g, 'Skeletal formula of the dipeptide Gly-Ala, H2N-CH2-CO-NH-CH(CH3)-COOH, with the peptide (amide) bond between the C=O carbon and the NH nitrogen labelled')


# ---------------------------------------------------------------- electrophoresis strip at pH 7
def fig_strip():
    g = Fig()
    # strip
    g.raw('<rect class="fm" x="40" y="58" width="260" height="46" rx="4"/><rect class="ln-m thin" x="40" y="58" width="260" height="46" rx="4"/>')
    g.segs.append(('strip', 40, 58, 300, 58)); g.segs.append(('strip', 40, 104, 300, 104))
    g.raw('<rect class="fi" x="20" y="50" width="14" height="62" rx="3"/>')
    g.raw('<rect class="fi" x="306" y="50" width="14" height="62" rx="3"/>')
    g.segs.append(('el1', 20, 50, 34, 112)); g.segs.append(('el2', 306, 50, 320, 112))
    g.text(27, 38, '−', 'tl tc', owner='minus'); g.text(313, 38, '+', 'tl tc', owner='plus')
    g.text(27, 130, 'cathode', 'tl tc', owner='cath'); g.text(313, 130, 'anode', 'tl tc', owner='anod')
    g.line(170, 52, 170, 110, 'ln-m thin dash', owner='start')
    g.text(170, 40, 'start line', 'tl tc', owner='sl')
    for (x, lab) in ((106, 'Lys'), (174, 'Gly'), (254, 'Asp')):
        g.circle(x, 81, 8, 'fa')
        g.segs.append((lab, x - 8, 73, x + 8, 89))
        g.text(x, 128, lab, 'tl tc', owner='lab' + lab)
    g.text(170, 156, 'pH 7', 'tl tc', owner='ph')
    save('strip', g, 'Paper strip at pH 7 with the cathode on the left and the anode on the right: lysine has moved towards the cathode, glycine hardly at all, and aspartic acid towards the anode')


if __name__ == '__main__':
    for fn in (fig_acyl, fig_mech, fig_amines, fig_lonepair, fig_glycine, fig_dipeptide, fig_strip):
        fn()
