import sys, math
sys.path.insert(0, 'data')
from fig import Fig

out = {}

# ---------- F1: propan-1-ol displayed and skeletal ----------
f = Fig()
xs = [45, 87, 129, 171, 213, 255]
names = ['H1', 'C1', 'C2', 'C3', 'O', 'H2']
labs = ['H', 'C', 'C', 'C', 'O', 'H']
y = 50
for n, x, l in zip(names, xs, labs):
    f.atom(n, x, y, l); f.label(x, y, l)
for a, b in zip(names, names[1:]):
    f.bond(a, b, cls='ln')
for i, n in enumerate(['C1', 'C2', 'C3']):
    x = xs[i + 1]
    f.atom(n + 'u', x, y - 38, 'H'); f.label(x, y - 38, 'H'); f.bond(n, n + 'u', cls='ln')
    f.atom(n + 'd', x, y + 38, 'H'); f.label(x, y + 38, 'H'); f.bond(n, n + 'd', cls='ln')
f.free_text(150, 118, 'displayed formula', 'tl tc ta')
# skeletal
sk = [('a', 100, 170, None), ('b', 135, 150, None), ('c', 170, 170, None), ('o', 205, 150, 'OH')]
for k, x, yy, l in sk:
    f.atom(k, x, yy, l)
f.label(205, 150, 'OH')
for a, b in (('a', 'b'), ('b', 'c'), ('c', 'o')):
    f.bond(a, b)
f.free_text(150, 205, 'skeletal formula', 'tl tc ta')
vb = (0, 0, 300, 215)
print('F1 issues', f.check(vb=vb))
out['F1'] = f.svg(vb, 'Propan-1-ol drawn as a displayed formula, with every atom and bond, and as a skeletal formula, with a zigzag line and an OH group',
                  'Propan-1-ol, CH₃CH₂CH₂OH, as a displayed formula (every atom and every bond) and as a skeletal formula (each corner and line end is a carbon atom, hydrogen atoms on carbon are not drawn).')

# ---------- F2: skeletal formulas in two figures ----------
Dx, Dy = 35, 20
PITCH = 118
colx = [0, 170]
OY0 = 34


def chain(n, ox, oy, start_up=True):
    pts = []
    up = start_up
    for i in range(n):
        pts.append((ox + i * Dx, oy - Dy / 2 if up else oy + Dy / 2, up))
        up = not up
    return pts


def add_c(f, key, x, y, lab=None):
    f.atom(key, x, y, lab)
    if lab:
        f.label(x, y, lab)


def cellxy(idx):
    r, c = divmod(idx, 2)
    return 12 + colx[c], OY0 + r * PITCH


def title(f, idx, name, grp):
    ox, oy = cellxy(idx)
    f.free_text(ox + 70, oy + 62, name, 'tl tc')
    f.free_text(ox + 70, oy + 77, grp, 'tl tc ta')


def cell_chain(f, idx, k, start_up, x0=8):
    ox, oy = cellxy(idx)
    p = chain(3, ox + x0, oy + 30, start_up)
    for i, (x, y, u) in enumerate(p):
        add_c(f, k + str(i), x, y)
    return p


def tail_atom(f, k, p, lab, order=1, linear=False, frm=2):
    x, y, u = p[frm]
    sgn = (-1 if u else 1) if linear else (1 if u else -1)
    ex, ey = x + Dx, y + sgn * Dy
    add_c(f, k + 'x', ex, ey, lab)
    f.bond(k + str(frm), k + 'x', order)


# ---- figure A
fa = Fig()
p = cell_chain(fa, 0, 'a', False)
fa.bond('a0', 'a1', 2); fa.bond('a1', 'a2'); title(fa, 0, 'propene', 'alkene')
p = cell_chain(fa, 1, 'b', False); fa.bond('b0', 'b1'); fa.bond('b1', 'b2'); tail_atom(fa, 'b', p, 'Cl')
title(fa, 1, '1-chloropropane', 'halogenoalkane')
p = cell_chain(fa, 2, 'c', False); fa.bond('c0', 'c1'); fa.bond('c1', 'c2'); tail_atom(fa, 'c', p, 'OH')
title(fa, 2, 'propan-1-ol', 'alcohol')
p = cell_chain(fa, 3, 'd', False); fa.bond('d0', 'd1'); fa.bond('d1', 'd2'); tail_atom(fa, 'd', p, 'NH₂')
title(fa, 3, 'propylamine', 'amine (primary)')
p = cell_chain(fa, 4, 'e', True); fa.bond('e0', 'e1'); fa.bond('e1', 'e2')
tail_atom(fa, 'e', p, 'N', 3, linear=True); title(fa, 4, 'propanenitrile', 'nitrile')
vbA = (0, 0, 345, OY0 + 2 * PITCH + 86)
print('F2a issues', fa.check(vb=vbA))

# ---- figure B: carbonyl family
fb = Fig()
# propanal: peak, valley, peak(CHO): =O up, H down-right
p = cell_chain(fb, 0, 'f', True); fb.bond('f0', 'f1'); fb.bond('f1', 'f2')
x, y, u = p[2]
add_c(fb, 'fo', x, y - 40, 'O'); fb.bond('f2', 'fo', 2)
add_c(fb, 'fh', x + Dx, y + Dy, 'H'); fb.bond('f2', 'fh')
title(fb, 0, 'propanal', 'aldehyde')
# propanone: valley, peak(C=O), valley
p = cell_chain(fb, 1, 'g', False, x0=22); fb.bond('g0', 'g1'); fb.bond('g1', 'g2')
x, y, u = p[1]
add_c(fb, 'go', x, y - 40, 'O'); fb.bond('g1', 'go', 2)
title(fb, 1, 'propanone', 'ketone')
# propanoic acid
p = cell_chain(fb, 2, 'h', True); fb.bond('h0', 'h1'); fb.bond('h1', 'h2')
x, y, u = p[2]
add_c(fb, 'ho', x, y - 40, 'O'); fb.bond('h2', 'ho', 2)
add_c(fb, 'hx', x + Dx, y + Dy, 'OH'); fb.bond('h2', 'hx')
title(fb, 2, 'propanoic acid', 'carboxylic acid')
# methyl propanoate
p = cell_chain(fb, 3, 'i', True, x0=2); fb.bond('i0', 'i1'); fb.bond('i1', 'i2')
x, y, u = p[2]
add_c(fb, 'io', x, y - 40, 'O'); fb.bond('i2', 'io', 2)
add_c(fb, 'ix', x + Dx, y + Dy, 'O'); fb.bond('i2', 'ix')
add_c(fb, 'ic', x + 2 * Dx, y); fb.bond('ix', 'ic')
title(fb, 3, 'methyl propanoate', 'ester')
vbB = (0, 0, 345, OY0 + 1 * PITCH + 86)
print('F2b issues', fb.check(vb=vbB))
out['F2a'] = fa.svg(vbA, 'Skeletal formulas of propene, 1-chloropropane, propan-1-ol, propylamine and propanenitrile, each labelled with its functional group',
                    'Five of the AS functional groups, each with a three-carbon example. Each corner or line end is a carbon atom. The C≡N group is a straight line (180°).')
out['F2b'] = fb.svg(vbB, 'Skeletal formulas of propanal, propanone, propanoic acid and methyl propanoate, each labelled with its functional group',
                    'The four functional groups that contain C=O. In an aldehyde the C=O carbon is at the end of the chain and carries an H; in a ketone it is inside the chain. A carboxylic acid has OH on the carbon of C=O; an ester has O–C there.')

# ---------- F3: heterolytic fission ----------
f = Fig()
y = 60
f.atom('c', 40, y, 'CH₃'); f.label(40, y, 'CH₃')
f.atom('b', 120, y, 'Br'); f.label(120, y, 'Br')
f.bond('c', 'b', cls='ln')
f.raw('<path class="c1 sw2" d="M81 55Q100 24 120 44" marker-end="url(#ahs-red)"/>')
f.raw('<path class="ln" d="M160 60H206" marker-end="url(#ah)"/>')
f.label(262, y, 'CH₃⁺ + Br⁻', 'tl tc')
f.free_text(150, 100, 'heterolytic fission', 'tl tc ta')
vb = (0, 10, 320, 105)
print('F3 issues', f.check(vb=vb))
out['F3'] = f.svg(vb, 'Heterolytic fission of the C–Br bond in bromomethane: a curly arrow from the middle of the bond to bromine gives a CH3 plus ion and a bromide ion',
                  'Heterolytic fission. The curly arrow starts at the bond and ends at Br: both electrons of the bond go to bromine, which becomes Br⁻, and carbon is left as CH₃⁺.')

# ---------- F4: shapes ----------
f = Fig()
# methane
cx, cy = 62, 58
f.atom('C', cx, cy, 'C'); f.label(cx, cy, 'C')
H = {'h1': (cx - 20, cy - 30), 'h2': (cx - 20, cy + 30), 'h3': (cx + 32, cy - 20), 'h4': (cx + 32, cy + 20)}
for k, (x, yy) in H.items():
    f.atom(k, x, yy, 'H'); f.label(x, yy, 'H')
f.bond('C', 'h1', cls='ln'); f.bond('C', 'h2', cls='ln')
f.wedge('C', 'h3'); f.wedge('C', 'h4', hashed=True)
# ethene
c1, c2 = (145, 58), (185, 58)
f.atom('E1', *c1, 'C'); f.label(*c1, 'C'); f.atom('E2', *c2, 'C'); f.label(*c2, 'C')
f.bond('E1', 'E2', 2, cls='ln')
for k, (x, yy) in {'e1': (126, 25), 'e2': (126, 91), 'e3': (204, 25), 'e4': (204, 91)}.items():
    f.atom(k, x, yy, 'H'); f.label(x, yy, 'H')
f.bond('E1', 'e1', cls='ln'); f.bond('E1', 'e2', cls='ln'); f.bond('E2', 'e3', cls='ln'); f.bond('E2', 'e4', cls='ln')
# ethyne
xs = [224, 262, 300, 338]
for i, (k, l) in enumerate(zip(['t1', 't2', 't3', 't4'], ['H', 'C', 'C', 'H'])):
    f.atom(k, xs[i], 58, l); f.label(xs[i], 58, l)
f.bond('t1', 't2', cls='ln'); f.bond('t2', 't3', 3, cls='ln', off=2.2); f.bond('t3', 't4', cls='ln')
for x, l1, l2 in ((62, 'methane: sp³', '109.5°'), (165, 'ethene: sp²', '120°'), (281, "ethyne: sp", "180°")):
    f.free_text(x, 124, l1, 'tl tc ta'); f.free_text(x, 140, l2, 'tl tc ta')
vb = (0, 8, 355, 142)
print('F4 issues', f.check(vb=vb))
out['F4'] = f.svg(vb, 'Three carbon shapes: methane with four single bonds at 109.5 degrees, ethene with 120 degrees in one plane, and ethyne with a straight 180 degree line',
                  'Bond angles at carbon. In CH₄ the plain bonds lie in the page, the wedge comes out of the page and the hashed bond goes behind it. All six atoms of ethene lie in one plane. Ethyne is linear.')

import json
json.dump(out, open('scratch/intro_figs.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in out.items():
    print('=====', k); print(v)
