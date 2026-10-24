# data/mk_fig_p15a.py: figures for chem.transition (writes data/p15_figs/*.svg.txt and checks label gaps).
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from p15_lib import Fig, tw, ligand_label, f, node, pt, link

OUT = os.path.join(os.path.dirname(__file__), 'p15_figs')
os.makedirs(OUT, exist_ok=True)

def save(name, fig, vb, label):
    open(os.path.join(OUT, name + '.svg.txt'), 'w', encoding='utf-8').write(fig.svg(vb, label))

def lobe(cx, cy, ang_deg, L, cls='fa'):
    """teardrop lobe from (cx, cy) along ang (degrees, screen y down), length L"""
    a = math.radians(ang_deg)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    k = L / 46.0
    def P(u, v):
        return (cx + ux * u * k + px * v * k, cy + uy * u * k + py * v * k)
    p0 = (cx, cy); c1 = P(11.5, -20); c2 = P(46, -18); p1 = P(46, 0); c3 = P(46, 18); c4 = P(11.5, 20)
    return 'M%s %sC%s %s %s %s %s %sC%s %s %s %s %s %sZ' % (
        f(p0[0]), f(p0[1]), f(c1[0]), f(c1[1]), f(c2[0]), f(c2[1]), f(p1[0]), f(p1[1]),
        f(c3[0]), f(c3[1]), f(c4[0]), f(c4[1]), f(p0[0]), f(p0[1]))

# ---------------------------------------------------------------- d orbitals
def fig_dorb():
    g = Fig()
    A = 66
    cx, cy = 82, 96
    for ang in (-45, -135, 45, 135):
        g.path(lobe(cx, cy, ang, 46), 'fa')
    g.line(cx, cy, cx + A, cy, 'ln-m thin'); g.text(cx + A + 9, cy + 4, 'x', 'ts tc')
    g.line(cx, cy, cx, cy - A, 'ln-m thin'); g.text(cx, cy - A - 9, 'y', 'ts tc')
    g.line(cx, cy, cx - A, cy, 'ln-m thin'); g.line(cx, cy, cx, cy + A, 'ln-m thin')
    g.circle(cx, cy, 2.5, 'fi')
    g.text(cx, 198, '3dxy', 'tl tc')
    cx, cy = 252, 96
    g.path(lobe(cx, cy, -90, 46), 'fa')
    g.path(lobe(cx, cy, 90, 46), 'fa')
    rx1, ry1, rx2, ry2 = 31, 11, 14, 4
    d = 'M%s %sA%s %s 0 1 0 %s %sA%s %s 0 1 0 %s %sZ' % (f(cx - rx1), f(cy), rx1, ry1, f(cx + rx1), f(cy), rx1, ry1, f(cx - rx1), f(cy))
    d += 'M%s %sA%s %s 0 1 0 %s %sA%s %s 0 1 0 %s %sZ' % (f(cx - rx2), f(cy), rx2, ry2, f(cx + rx2), f(cy), rx2, ry2, f(cx - rx2), f(cy))
    g.path(d, 'fa', ' fill-rule="evenodd"')
    g.line(cx, cy, cx + A, cy, 'ln-m thin'); g.text(cx + A + 9, cy + 4, 'x', 'ts tc')
    g.line(cx, cy, cx, cy - A, 'ln-m thin'); g.text(cx, cy - A - 9, 'z', 'ts tc')
    g.line(cx, cy, cx - 34, cy + 44, 'ln-m thin'); g.text(cx - 44, cy + 61, 'y', 'ts tc')
    g.circle(cx, cy, 2.5, 'fi')
    g.text(cx, 198, '3dz²', 'tl tc')
    return g

# ---------------------------------------------------------------- geometries
def complex_panel(g, cx, cy, metal, ligs, name_lines, ytxt):
    m = node(g, cx, cy, metal, owner='M' + metal + str(cx))
    for i, (dx, dy, kind, lab) in enumerate(ligs):
        L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        # ligand label: box edge 5 px beyond the bond end (bond end at distance L from the centre)
        ex, ey = cx + dx, cy + dy
        w = tw(lab); hw, hh = w / 2, 6.5
        tx = hw / abs(ux) if abs(ux) > 1e-9 else 1e9
        ty = hh / abs(uy) if abs(uy) > 1e-9 else 1e9
        ex_ = min(tx, ty)
        lc = (ex + ux * (6.5 + ex_), ey + uy * (6.5 + ex_))
        n = node(g, lc[0], lc[1], lab, owner='L%s%d%d' % (lab, cx, i))
        link(g, m, ('pt', ex, ey, 0, 0), kind, owner='b%d%d' % (cx, i), gap=6)
    for k, s in enumerate(name_lines):
        g.text(cx, ytxt + 17 * k, s, 'tl tc', owner='name%d%d' % (cx, k))

def fig_geom():
    g = Fig()
    oct_l = [(0, -44, 'plain', 'H₂O'), (0, 44, 'plain', 'H₂O'), (-44, 0, 'plain', 'H₂O'), (44, 0, 'plain', 'H₂O'),
             (-28, 24, 'wedge', 'H₂O'), (28, -24, 'hash', 'H₂O')]
    complex_panel(g, 85, 96, 'Cu', oct_l, ['[Cu(H₂O)₆]²⁺', 'octahedral, 90°'], 190)
    tet_l = [(0, -44, 'plain', 'Cl'), (-40, 22, 'plain', 'Cl'), (32, 34, 'wedge', 'Cl'), (42, -12, 'hash', 'Cl')]
    complex_panel(g, 255, 96, 'Cu', tet_l, ['[CuCl₄]²⁻', 'tetrahedral, 109.5°'], 190)
    return g

def fig_geom2():
    g = Fig()
    cx, cy = 85, 60
    m = node(g, cx, cy, 'Ag', owner='Ag')
    for s in (-1, 1):
        lab = 'NH₃' if s == 1 else 'H₃N'
        ex = cx + s * 38
        lc = ex + s * (5 + tw(lab) / 2)
        node(g, lc, cy, lab, owner='Lg%d' % s)
        link(g, m, pt(ex, cy), 'plain', owner='bAg%d' % s)
    g.text(cx, 128, '[Ag(NH₃)₂]⁺', 'tl tc'); g.text(cx, 145, 'linear, 180°', 'tl tc')
    cx, cy = 255, 60
    m = node(g, cx, cy, 'Pt', owner='Pt')
    for (dx, dy, lab) in ((-34, -30, 'H₃N'), (34, -30, 'NH₃'), (-34, 30, 'Cl'), (34, 30, 'Cl')):
        L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        w = tw(lab); tx = (w / 2) / abs(ux); ty = 6.5 / abs(uy)
        e = min(tx, ty)
        lc = (cx + dx + ux * (6.5 + e), cy + dy + uy * (6.5 + e))
        node(g, lc[0], lc[1], lab, owner='LPt%s%d%d' % (lab, dx, dy))
        link(g, m, pt(cx + dx, cy + dy), 'plain', owner='bPt%d%d' % (dx, dy))
    g.text(cx, 128, '[Pt(NH₃)₂Cl₂]', 'tl tc'); g.text(cx, 145, 'square planar, 90°', 'tl tc')
    return g

def fig_chelate():
    g = Fig()
    M = node(g, 85, 36, 'M', owner='M1')
    N1 = node(g, 50, 90, 'H₂N', owner='N1'); N2 = node(g, 120, 90, 'NH₂', owner='N2')
    C1 = pt(66, 134); C2 = pt(104, 134)
    link(g, M, N1, owner='MN1'); link(g, M, N2, owner='MN2')
    link(g, N1, C1, owner='NC1'); link(g, N2, C2, owner='NC2'); link(g, C1, C2, owner='CC')
    g.text(85, 196, 'en', 'tl tc'); g.text(85, 213, 'H₂NCH₂CH₂NH₂', 'tl tc')
    M = node(g, 255, 36, 'M', owner='M2')
    O1 = node(g, 222, 90, 'O', owner='O1'); O2 = node(g, 288, 90, 'O', owner='O2')
    C1 = pt(236, 134); C2 = pt(274, 134)
    link(g, M, O1, owner='MO1'); link(g, M, O2, owner='MO2')
    link(g, O1, C1, owner='OC1'); link(g, O2, C2, owner='OC2'); link(g, C1, C2, owner='CC2')
    for (c, ox, sgn) in ((C1, 224, -1), (C2, 286, 1)):
        O = node(g, ox, 172, 'O', owner='Od%d' % sgn)
        dx, dy = ox - c[1], 172 - c[2]
        L = (dx * dx + dy * dy) ** 0.5
        px, py = -dy / L, dx / L
        for off in (-2.6, 2.6):
            link(g, pt(c[1] + px * off, c[2] + py * off), O, owner='dbl%d%s' % (sgn, off))
    g.text(255, 196, 'ethanedioate', 'tl tc'); g.text(255, 213, 'C₂O₄²⁻', 'tl tc')
    return g

if __name__ == '__main__':
    g = fig_dorb(); g.report('dorb'); save('dorb', g, '0 4 340 204', 'x')
    g = fig_geom(); g.report('geom'); save('geom', g, '0 20 340 205', 'x')
    g = fig_geom2(); g.report('geom2'); save('geom2', g, '0 2 340 158', 'x')
    g = fig_chelate(); g.report('chelate'); save('chelate', g, '0 15 340 210', 'x')
