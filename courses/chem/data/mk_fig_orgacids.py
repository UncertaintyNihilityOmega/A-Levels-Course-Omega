import sys, json
sys.path.insert(0, 'data')
sys.stdout.reconfigure(encoding='utf-8')
from fig import Fig, text_w
out = {}
def add_c(f, key, x, y, lab=None):
    f.atom(key, x, y, lab)
    if lab: f.label(x, y, lab)

# G1 methyl propanoate with parts
f = Fig()
pts = {'a': (20, 80), 'b': (55, 100), 'c': (90, 80), 'e': (125, 100), 'd': (160, 80)}
for k, (x, y) in pts.items():
    add_c(f, k, x, y, 'O' if k == 'e' else None)
add_c(f, 'o', 90, 44, 'O')
for a, b in (('a', 'b'), ('b', 'c'), ('c', 'e'), ('e', 'd')): f.bond(a, b)
f.bond('c', 'o', 2)
# brackets
def bracket(x0, x1, y):
    f.raw('<path class="ln-m thin" d="M%d %dV%dH%dV%d"/>' % (x0, y-6, y, x1, y-6))
    f.segs.append((x0, y-6, x0, y, 'br')); f.segs.append((x0, y, x1, y, 'br')); f.segs.append((x1, y-6, x1, y, 'br'))
bracket(12, 105, 132); bracket(114, 168, 132)
f.free_text(58, 153, 'acid part', 'tl tc ta'); f.free_text(58, 169, 'propanoate', 'tl tc')
f.free_text(145, 153, 'alcohol part', 'tl tc ta'); f.free_text(145, 169, 'methyl', 'tl tc')
f.free_text(100, 200, 'methyl propanoate', 'tl tc')
vb = (-75, 25, 330, 190)  # centred in review P11
print('G1', f.check(vb=vb))
out['G1'] = f.svg(vb, 'Skeletal formula of methyl propanoate with the left part, from the acid, marked propanoate and the right part, from the alcohol, marked methyl',
  'Methyl propanoate. The part with the C=O carbon comes from propanoic acid and gives the ending -oate. The part on the single-bonded oxygen comes from methanol and is named first, as methyl.')

# G2 hydrolysis flow
f = Fig()
def box(cx, cy, w, h, lines):
    f.raw('<rect class="fm" rx="8" x="%s" y="%s" width="%s" height="%s"/>' % (f.f(cx-w/2), f.f(cy-h/2), f.f(w), f.f(h)))
    x0, y0, x1, y1 = cx-w/2, cy-h/2, cx+w/2, cy+h/2
    for s in ((x0,y0,x1,y0),(x1,y0,x1,y1),(x1,y1,x0,y1),(x0,y1,x0,y0)): f.segs.append(s+('box',))
    n = len(lines)
    for i, s in enumerate(lines):
        yc = cy + (i - (n-1)/2) * 16
        f.free_text(cx, yc + 4, s, 'tl tc')
def arrow(x0, y0, x1, y1):
    f.raw('<path class="ln" d="M%s %s%s%s" marker-end="url(#ah)"/>' % (f.f(x0), f.f(y0), 'H'+f.f(x1) if y0 == y1 else 'V'+f.f(y1), ''))
    f.segs.append((x0, y0, x1, y1, 'arrow'))
box(38, 35, 52, 26, ['ester']); arrow(72, 35, 198, 35)
f.free_text(135, 27, 'dilute acid', 'tl tc'); f.free_text(135, 56, 'heat; reversible', 'tl tc')
box(265, 35, 112, 26, ['acid + alcohol'])
box(38, 125, 52, 26, ['ester']); arrow(72, 125, 198, 125)
f.free_text(135, 117, 'NaOH(aq)', 'tl tc'); f.free_text(135, 146, 'heat', 'tl tc')
box(265, 125, 118, 44, ['carboxylate salt', '+ alcohol'])
arrow(265, 152, 265, 180)
f.free_text(256, 171, 'dilute acid', 'tl', ) if False else None
f.raw('<text class="tl" x="256" y="171" text-anchor="end">dilute acid</text>'); f.labels.append((256-text_w('dilute acid')/2, 167, text_w('dilute acid'), 13, 'dilute acid'))
box(265, 205, 118, 26, ['carboxylic acid'])
vb = (0, 5, 340, 225)
print('G2', f.check(vb=vb))
out['G2'] = f.svg(vb, 'Flow chart: an ester heated with dilute acid gives a carboxylic acid and an alcohol in a reversible reaction; heated with aqueous sodium hydroxide it gives a carboxylate salt and an alcohol, and adding dilute acid then gives the carboxylic acid',
  'Hydrolysis of an ester. Acid hydrolysis is reversible and gives the acid directly. Alkaline hydrolysis goes to completion but gives the carboxylate salt; acidifying turns the salt into the carboxylic acid.')
json.dump(out, open('scratch/p11_acids.json', 'w', encoding='utf-8'), ensure_ascii=False)
for k in out: print(out[k])
