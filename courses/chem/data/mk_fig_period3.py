# data/mk_fig_period3.py: two sketches for chem.periodicity (no numbers on the axes).
# 1. radius of the Period 3 atoms and of their simple ions; 2. melting point of the Period 3 elements.
# Heights are ordered as the real data (typical metallic/covalent atomic radii; ionic radii; melting points in K)
# but are only a sketch. Run: py data/mk_fig_period3.py  (prints both figures; checks label clearance)
import sys
sys.stdout.reconfigure(encoding='utf-8')
def f(v):
    s = f"{v:.1f}"; return s[:-2] if s.endswith('.0') else s

# ---------- figure 1: radii ----------
rad_atom = [186, 160, 143, 118, 110, 104, 99]
ion = {0: 102, 1: 72, 2: 54, 4: 212, 5: 184, 6: 181}
ion_lab = {0: 'Na⁺', 1: 'Mg²⁺', 2: 'Al³⁺', 4: 'P³⁻', 5: 'S²⁻', 6: 'Cl⁻'}
assert rad_atom == sorted(rad_atom, reverse=True)
assert ion[0] > ion[1] > ion[2] and ion[4] > ion[5] > ion[6]
assert all(ion[i] < rad_atom[i] for i in (0, 1, 2)) and all(ion[i] > rad_atom[i] for i in (4, 5, 6))
X = lambda i: 100 + 75 * i
Y = lambda r: 250 - 0.95 * r
p = ['<path class="ax" d="M70 250H585" marker-end="url(#ahm)"/><path class="ax" d="M70 250V22" marker-end="url(#ahm)"/>',
     '<text class="tl" x="78" y="16">radius (not to scale)</text>']
for i, s in enumerate(['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']):
    p.append(f'<path class="ax" d="M{X(i)} 250v4"/><text class="tl tc" x="{X(i)}" y="271">{s}</text>')
pts = ' '.join(('M' if i == 0 else 'L') + f'{X(i)} {f(Y(r))}' for i, r in enumerate(rad_atom))
p.append(f'<path class="c1 sw2" d="{pts}"/>')
for i, r in enumerate(rad_atom):
    p.append(f'<circle class="fi" cx="{X(i)}" cy="{f(Y(r))}" r="4.5"/>')
for seg in ((0, 1, 2), (4, 5, 6)):
    d = ' '.join(('M' if k == 0 else 'L') + f'{X(i)} {f(Y(ion[i]))}' for k, i in enumerate(seg))
    p.append(f'<path class="c2 sw2 dash" d="{d}"/>')
for i in ion:
    cy = Y(ion[i]); up = i in (4, 6)
    p.append(f'<circle class="fp s-acc sw2" cx="{X(i)}" cy="{f(cy)}" r="4.5"/>')
    p.append(f'<text class="tl tc" x="{X(i)}" y="{f(cy - 11 if up else cy + 20)}">{ion_lab[i]}</text>')
p.append('<text class="tl tc" x="325" y="236">Si: no simple ion</text>')
p.append('<path class="c1 sw2" d="M170 44h26"/><circle class="fi" cx="183" cy="44" r="4.5"/><text class="tl" x="204" y="48">atom</text>')
p.append('<path class="c2 sw2 dash" d="M170 66h26"/><circle class="fp s-acc sw2" cx="183" cy="66" r="4.5"/><text class="tl" x="204" y="70">simple ion</text>')
# clearance checks (label boxes vs lines)
def seg_pts(a, b, n=200): return [(a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n) for t in range(n + 1)]
segs = []
for i in range(6): segs += seg_pts((X(i), Y(rad_atom[i])), (X(i + 1), Y(rad_atom[i + 1])))
for a, b in ((0, 1), (1, 2), (4, 5), (5, 6)): segs += seg_pts((X(a), Y(ion[a])), (X(b), Y(ion[b])))
boxes = [(X(i) - 3.5 * len(ion_lab[i]), (Y(ion[i]) - 11 if i in (4, 6) else Y(ion[i]) + 20) - 10, X(i) + 3.5 * len(ion_lab[i]), (Y(ion[i]) - 11 if i in (4, 6) else Y(ion[i]) + 20) + 3, ion_lab[i]) for i in ion]
boxes.append((325 - 59.5, 226, 325 + 59.5, 239, 'Si note'))
boxes.append((170, 36, 204 + 7 * 10, 76, 'legend'))
bad = 0
for b in boxes:
    for (x, y) in segs:
        if b[0] - 4 <= x <= b[2] + 4 and b[1] - 4 <= y <= b[3] + 4: print('CLASH', b[4], (round(x), round(y))); bad += 1; break
    if b[3] > 247 and b[4] != 'Si note': print('AXIS', b[4])
for i, b1 in enumerate(boxes):
    for b2 in boxes[i + 1:]:
        if b1[0] < b2[2] + 4 and b2[0] < b1[2] + 4 and b1[1] < b2[3] + 4 and b2[1] < b1[3] + 4: print('OVERLAP', b1[4], b2[4]); bad += 1
print('fig1 problems', bad, file=sys.stderr)
print('<figure class="fig"><svg viewBox="40 4 560 280" role="img" aria-label="Sketch of the radius of the atoms Na to Cl, which falls steadily, and of their simple ions: Na+, Mg2+ and Al3+ are smaller than their atoms and get smaller, then the negative ions P3-, S2- and Cl- are larger than their atoms and get smaller. There is a big jump up between Al3+ and P3-. Silicon has no simple ion">' + ''.join(p) + '</svg><figcaption>A sketch (not to scale) of the radius of the Period 3 atoms and their simple ions. Atomic radius falls across the period. The positive ions are smaller than their atoms, the negative ions are larger, and each set of ions also gets smaller from left to right.</figcaption></figure>')

# ---------- figure 2: melting point ----------
K = {'Na': 371, 'Mg': 923, 'Al': 933, 'Si': 1683, 'P₄': 317, 'S₈': 388, 'Cl₂': 172, 'Ar': 84}
names = list(K)
assert K['Na'] < K['Mg'] < K['Al'] < K['Si'] and K['S₈'] > K['P₄'] > K['Cl₂'] > K['Ar']
X2 = lambda i: 90 + 68 * i
Y2 = lambda k: 250 - 0.125 * k
q = ['<path class="ax" d="M60 250H590" marker-end="url(#ahm)"/><path class="ax" d="M60 250V22" marker-end="url(#ahm)"/>',
     '<text class="tl" x="68" y="16">melting point (not to scale)</text>']
cls = {'Na': 'fa', 'Mg': 'fa', 'Al': 'fa', 'Si': 'fa2'}
for i, n in enumerate(names):
    top = Y2(K[n])
    q.append(f'<rect class="{cls.get(n, "f1 s-acc sw2")}" x="{X2(i) - 22}" y="{f(top)}" width="44" height="{f(250 - top)}"/>')
    q.append(f'<text class="tl tc" x="{X2(i)}" y="268">{n}</text>')
for a, b, t in ((0, 2, 'giant metallic'), (3, 3, 'giant covalent'), (4, 7, 'simple molecular')):
    x0, x1 = X2(a) - 22, X2(b) + 22
    q.append(f'<path class="ln-m" d="M{x0} 280v4H{x1}v-4"/><text class="tl tc" x="{(x0 + x1) / 2}" y="302">{t}</text>')
print('<figure class="fig"><svg viewBox="40 4 560 312" role="img" aria-label="Sketch of the melting points of the Period 3 elements: sodium lowest of the three metals, then magnesium and aluminium higher, silicon the highest of all, then a sharp fall to the simple molecular P4, S8, Cl2 and Ar, in the order S8 above P4 above Cl2 above Ar">' + ''.join(q) + '</svg><figcaption>A sketch (not to scale) of the melting points of the Period 3 elements. The metals rise from Na to Al, silicon (a giant covalent structure) is the highest, and the simple molecular substances are much lower: S₈ > P₄ > Cl₂ > Ar.</figcaption></figure>')
