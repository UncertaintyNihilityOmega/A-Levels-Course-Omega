import sys, json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'data')
from fig import Fig, seg_rect_dist
out = {}

def add_c(f, key, x, y, lab=None):
    f.atom(key, x, y, lab)
    if lab:
        f.label(x, y, lab)

def curve(f, x0, y0, cx, cy, x1, y1, cls='c1 sw2', marker='ahs-red', tag='arrow'):
    f.raw('<path class="%s" d="M%s %sQ%s %s %s %s" marker-end="url(#%s)"/>' % (cls, f.f(x0), f.f(y0), f.f(cx), f.f(cy), f.f(x1), f.f(y1), marker))
    n = 20
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(((1-t)**2*x0 + 2*t*(1-t)*cx + t*t*x1, (1-t)**2*y0 + 2*t*(1-t)*cy + t*t*y1))
    for p, q in zip(pts, pts[1:]):
        f.segs.append((p[0], p[1], q[0], q[1], tag))

def line_arrow(f, x0, y0, x1, y1, cls='ln'):
    f.raw('<path class="%s" d="M%s %sH%s" marker-end="url(#ah)"/>' % (cls, f.f(x0), f.f(y0), f.f(x1)))
    f.segs.append((x0, y0, x1, y1, 'steparrow'))

def dots(f, x, y):
    f.raw('<circle class="fi" cx="%s" cy="%s" r="1.7"/><circle class="fi" cx="%s" cy="%s" r="1.7"/>' % (f.f(x-3), f.f(y), f.f(x+3), f.f(y)))

# ---------- F1 carbonyl shape and polarity ----------
f = Fig()
add_c(f, 'C', 100, 85, 'C'); add_c(f, 'O', 100, 40, 'O')
add_c(f, 'M', 62, 107, 'CH₃'); add_c(f, 'H', 138, 107, 'H')
f.bond('C', 'O', 2, cls='ln'); f.bond('C', 'M', cls='ln'); f.bond('C', 'H', cls='ln')
f.free_text(116, 72, 'δ+', 'tl ta'); f.free_text(116, 36, 'δ−', 'tl ta')
f.free_text(190, 52, 'trigonal planar', 'tl'); f.free_text(190, 69, 'angles about 120°', 'tl')
f.free_text(190, 90, 'C is δ+: attacked', 'tl'); f.free_text(190, 107, 'by nucleophiles', 'tl')
vb = (0, 15, 330, 120)
print('F1', f.check(vb=vb))
out['F1'] = f.svg(vb, 'Displayed formula of ethanal with the C=O carbon at the centre of a flat triangle of three bonds, labelled delta plus on carbon and delta minus on oxygen',
    'Ethanal, CH₃CHO. The carbon of C=O has three bonds in one plane (about 120° apart). Oxygen is more electronegative than carbon, so the C=O bond is polar.')

# ---------- F2 skeletal names ----------
f = Fig()
Dx, Dy = 35, 20
def cell(ox, oy, n, ups, ocar, name, grp, hald=False):
    pts = []
    for i in range(n):
        x = ox + i*Dx
        y = oy + (30 if ups[i] else 50)
        pts.append((x, y))
    for i, (x, y) in enumerate(pts):
        add_c(f, '%s%d' % (name, i), x, y)
    for i in range(n-1):
        f.bond('%s%d' % (name, i), '%s%d' % (name, i+1))
    x, y = pts[ocar]
    add_c(f, name+'O', x, y-36, 'O')
    f.bond('%s%d' % (name, ocar), name+'O', 2)
    if hald:
        add_c(f, name+'H', x+30, y+16, 'H')
        f.bond('%s%d' % (name, ocar), name+'H')
    f.free_text(ox+50, oy+88, name, 'tl tc')
    f.free_text(ox+50, oy+103, grp, 'tl tc ta')
# up = True means higher vertex (y smaller)
cell(10, 20, 4, [False, True, False, True], 3, 'butanal', 'aldehyde', hald=True)
cell(190, 20, 4, [False, True, False, True], 1, 'butanone', 'ketone')
cell(10, 150, 5, [False, True, False, True, False], 1, 'pentan-2-one', 'ketone')
cell(190, 150, 5, [True, False, True, False, True], 2, 'pentan-3-one', 'ketone')
vb = (0, 5, 345, 260)
print('F2', f.check(vb=vb))
out['F2'] = f.svg(vb, 'Skeletal formulas of butanal, butanone, pentan-2-one and pentan-3-one',
    'Skeletal formulas. In butanal the C=O carbon is at the end of the chain, so it is carbon 1. In a ketone the C=O carbon is inside the chain; the number in the name says which carbon it is, counting from the end that gives the lower number.')

# ---------- F3 mechanism (stacked, fig small) ----------
f = Fig()
L = 150
def struct(cx, cy, prefix):
    add_c(f, prefix+'C', cx, cy, 'C')
    add_c(f, prefix+'L', cx-50, cy, 'H₃C'); add_c(f, prefix+'R', cx+50, cy, 'CH₃')
    f.bond(prefix+'C', prefix+'L', cls='ln'); f.bond(prefix+'C', prefix+'R', cls='ln')
def down(x, y0, y1, label):
    f.raw('<path class="ln" d="M%s %sV%s" marker-end="url(#ah)"/>' % (f.f(x), f.f(y0), f.f(y1)))
    f.segs.append((x, y0, x, y1, 'steparrow'))
    f.raw('<text class="tl" x="%s" y="%s">%s</text>' % (f.f(x+12), f.f((y0+y1)/2+4), label))
    w = text_w(label); f.labels.append((x+12+w/2, (y0+y1)/2-1, w, 13, label))
from fig import text_w
# stage A
cA = 95
struct(L, cA, 'a')
add_c(f, 'aO', L, cA-50, 'O'); f.bond('aC', 'aO', 2, cls='ln')
f.free_text(L-28, cA-15, 'δ+', 'tl ta'); f.free_text(L-28, cA-45, 'δ−', 'tl ta')
curve(f, L+3.5, cA-25, L+28, cA-29, L+11, cA-49, tag='pi')
add_c(f, 'cn', L, cA+70, 'CN⁻')
dots(f, L-6, cA+59)
curve(f, L-5.5, cA+54, L-23, cA+28, L-2, cA+14, tag='nuc')
down(L, cA+95, cA+137, 'step 1 (slow)')
# stage B
cB = 340
struct(L, cB, 'b')
add_c(f, 'bO', L, cB-50, 'O⁻'); f.bond('bC', 'bO', cls='ln')
add_c(f, 'bN', L, cB+50, 'CN'); f.bond('bC', 'bN', cls='ln')
oy = cB-50
dots(f, L-1, oy-11)
curve(f, L+1, oy-16, L+40, oy-44, L+84, oy-13, tag='O-H')
f.free_text(L+36, oy+4, '+', 'tl')
add_c(f, 'H', L+85, oy, 'H'); add_c(f, 'cn2', L+132, oy, 'CN')
f.bond('H', 'cn2', cls='ln')
curve(f, L+107, oy+3, L+104, oy+28, L+128, oy+17, tag='H-C')
down(L, cB+75, cB+117, 'step 2 (fast)')
# stage C
cC = 555
struct(L, cC, 'd')
add_c(f, 'dO', L, cC-50, 'OH'); f.bond('dC', 'dO', cls='ln')
add_c(f, 'dN', L, cC+50, 'CN'); f.bond('dC', 'dN', cls='ln')
f.free_text(L+75, cC+4, '+ CN⁻', 'tl')
vb = (50, 25, 310, 610)
print('F3', f.check(vb=vb))
out['F3'] = f.svg(vb, 'Mechanism of nucleophilic addition of HCN to propanone, in three stages from top to bottom: cyanide ion attacks the delta-plus carbon and the C=O pi bond moves onto oxygen to give an alkoxide ion; the O minus then takes a hydrogen ion from HCN, giving 2-hydroxy-2-methylpropanenitrile and regenerating cyanide ion',
    'Nucleophilic addition of HCN to propanone, read from top to bottom. Step 1: a lone pair on the carbon of CN⁻ forms a bond to the δ+ carbon, and the C=O π bond moves onto oxygen. Step 2: a lone pair on O⁻ takes H⁺ from HCN, and the H–C bond breaks to give CN⁻ again, so CN⁻ is a catalyst.', cls='fig small')
json.dump(out, open('scratch/p11_carbonyl.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(out['F3'])
