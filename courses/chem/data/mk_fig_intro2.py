import sys, math, json
sys.path.insert(0, 'data')
from fig import Fig

out = {}
# ---------- F5: displayed methyl propanoate ----------
f = Fig()
y = 66
xs = [24, 64, 104, 144, 184, 224, 264]
ks = ['h0', 'c1', 'c2', 'c3', 'o', 'c4', 'h4']
ls = ['H', 'C', 'C', 'C', 'O', 'C', 'H']
for k, x, l in zip(ks, xs, ls):
    f.atom(k, x, y, l); f.label(x, y, l)
for a, b in zip(ks, ks[1:]):
    f.bond(a, b, cls='ln')
for k, x in (('c1', 64), ('c2', 104), ('c4', 224)):
    f.atom(k + 'u', x, y - 38, 'H'); f.label(x, y - 38, 'H'); f.bond(k, k + 'u', cls='ln')
    f.atom(k + 'd', x, y + 38, 'H'); f.label(x, y + 38, 'H'); f.bond(k, k + 'd', cls='ln')
f.atom('co', 144, y - 38, 'O'); f.label(144, y - 38, 'O'); f.bond('c3', 'co', 2, cls='ln')
vb = (0, 12, 288, 112)
print('F5', f.check(vb=vb))
out['F5'] = f.svg(vb, 'Displayed formula of methyl propanoate: CH3 CH2 C double bond O, then O, then CH3, with every C–H bond drawn',
                  'The displayed formula of methyl propanoate. Every atom is shown, with every bond as a line; the carbon of the ester group has a C=O double bond and a single bond to the second oxygen.')

# ---------- F6: skeletal cyclohexene and 3-methylbutan-2-ol ----------
f = Fig()
cx, cy, R = 70, 66, 40
pts = []
for k in range(6):
    a = math.radians(-90 + 60 * k)
    pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for i, (x, yy) in enumerate(pts):
    f.atom('r%d' % i, x, yy)
for i in range(6):
    f.bond('r%d' % i, 'r%d' % ((i + 1) % 6), 2 if i == 0 else 1)
# chain
x0, y0 = 175, 100
c1 = (x0, y0); c2 = (x0 + 35, y0 - 20); c3 = (x0 + 70, y0); c4 = (x0 + 105, y0 - 20)
f.atom('a1', *c1); f.atom('a2', *c2); f.atom('a3', *c3); f.atom('a4', *c4)
f.atom('ao', c2[0], c2[1] - 40, 'OH'); f.label(c2[0], c2[1] - 40, 'OH')
f.atom('am', c3[0], c3[1] + 40)
f.bond('a1', 'a2'); f.bond('a2', 'a3'); f.bond('a3', 'a4'); f.bond('a2', 'ao'); f.bond('a3', 'am')
f.free_text(70, 152, '(a)', 'tl tc ta'); f.free_text(180, 152, '(b)', 'tl tc ta')
vb = (0, 8, 330, 156)
print('F6', f.check(vb=vb))
print([ (round(x,1),round(y,1)) for x,y in pts])
out['F6'] = f.svg(vb, 'Skeletal formulas of (a) cyclohexene, a six-membered ring with one double bond, and (b) a four-carbon chain with an OH group on the second carbon and a methyl group on the third',
                  'Two skeletal formulas for counting atoms: (a) a ring with one C=C, (b) a branched alcohol.')
json.dump(out, open('scratch/intro_figs2.json', 'w', encoding='utf-8'), ensure_ascii=False)
for k, v in out.items():
    print('=====', k); print(v)
