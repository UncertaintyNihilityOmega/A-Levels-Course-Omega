# data/mk_fig_hydrides.py: boiling point against period for the Group 14 and 16 hydrides (chem.shapes).
# Run: py data/mk_fig_hydrides.py  (prints the figure; checks label clearance)
import sys
sys.stdout.reconfigure(encoding='utf-8')
bp14 = [-162, -112, -88, -52]; bp16 = [100, -60, -41, -2]
n14 = ['CH₄', 'SiH₄', 'GeH₄', 'SnH₄']; n16 = ['H₂O', 'H₂S', 'H₂Se', 'H₂Te']
X0, Y0, YB = 80, 30, 265
def X(p): return 140 + 130 * (p - 2)
def Y(b): return round(Y0 + (120 - b) * (YB - Y0) / 320, 1)
p = []
p.append(f'<path class="ax" d="M{X0} {YB}H595" marker-end="url(#ahm)"/><path class="ax" d="M{X0} {YB}V22" marker-end="url(#ahm)"/>')
p.append(f'<text class="tl" x="{X0 + 8}" y="16">boiling point / °C</text>')
for t in (-150, -100, -50, 0, 50, 100):
    y = Y(t)
    p.append(f'<path class="ax" d="M{X0 - 4} {y}H{X0}"/><text class="ts" x="{X0 - 8}" y="{y + 4}" text-anchor="end">{str(t).replace("-", "−")}</text>')
p.append(f'<path class="ln-m thin dash" d="M{X0} {Y(0)}H590"/>')
for per in range(2, 6):
    p.append(f'<path class="ax" d="M{X(per)} {YB}v4"/><text class="ts tc" x="{X(per)}" y="{YB + 17}">{per}</text>')
p.append(f'<text class="tl tc" x="{(X(2) + X(5)) // 2}" y="{YB + 38}">period</text>')
boxes = []; pts = []
for series, bps, names, cc, fc, above in ((1, bp14, n14, 'c1', 'f1', False), (2, bp16, n16, 'c2', 'f2', True)):
    d = " ".join(("M" if i == 0 else "L") + f"{X(i + 2)} {Y(b)}" for i, b in enumerate(bps))
    p.append(f'<path class="{cc} sw2" d="{d}"/>')
    for i, (b, nm) in enumerate(zip(bps, names)):
        x, y = X(i + 2), Y(b)
        pts.append((x, y))
        p.append(f'<circle class="fi" cx="{x}" cy="{y}" r="4.5"/>')
        w = 7 * len(nm)
        if nm == 'H₂O':
            tx, ty, anc = x - 10, y + 5, 'end'; box = (tx - w, ty - 10, tx, ty + 3)
        elif nm == 'H₂S':
            tx, ty, anc = x - 8, y + 16, 'end'; box = (tx - w, ty - 10, tx, ty + 3)
        elif above:
            tx, ty, anc = x, y - 11, 'middle'; box = (tx - w / 2, ty - 10, tx + w / 2, ty + 3)
        else:
            tx, ty, anc = x, y + 21, 'middle'; box = (tx - w / 2, ty - 10, tx + w / 2, ty + 3)
        boxes.append((box, nm))
        p.append(f'<text class="tl" x="{tx}" y="{ty}" text-anchor="{anc}">{nm}</text>')
# legend (top right)
p.append('<path class="c1 sw2" d="M395 46h26"/><circle class="fi" cx="408" cy="46" r="4.5"/><text class="tl" x="430" y="50">Group 14 hydrides</text>')
p.append('<path class="c2 sw2" d="M395 68h26"/><circle class="fi" cx="408" cy="68" r="4.5"/><text class="tl" x="430" y="72">Group 16 hydrides</text>')
boxes.append(((395, 36, 430 + 7 * 17, 77), 'legend'))
# clearance: label boxes vs every line segment and other boxes
segs = []
for bps in (bp14, bp16):
    for i in range(3):
        segs.append((X(i + 2), Y(bps[i]), X(i + 3), Y(bps[i + 1])))
import math
def seg_hits_box(s, b, m=4):
    x1, y1, x2, y2 = s; bx0, by0, bx1, by1 = b[0] - m, b[1] - m, b[2] + m, b[3] + m
    for k in range(0, 201):
        t = k / 200; x = x1 + (x2 - x1) * t; y = y1 + (y2 - y1) * t
        if bx0 <= x <= bx1 and by0 <= y <= by1: return True
    return False
bad = 0
for b, nm in boxes:
    if nm != 'legend':
        for s in segs:
            if seg_hits_box(s, b): print('CLASH', nm, s); bad += 1
        # axis/tick-label zone and x-axis
        if b[0] < X0 + 6 or b[3] > YB - 3 or b[1] < 20: print('EDGE', nm, b); bad += 1
    for s in segs:
        if nm == 'legend' and seg_hits_box(s, b): print('CLASH legend', s); bad += 1
for i, (b1, n1) in enumerate(boxes):
    for b2, n2 in boxes[i + 1:]:
        if b1[0] < b2[2] + 4 and b2[0] < b1[2] + 4 and b1[1] < b2[3] + 4 and b2[1] < b1[3] + 4: print('OVERLAP', n1, n2); bad += 1
print('problems:', bad, file=sys.stderr)
svg = ('<figure class="fig"><svg viewBox="12 4 598 314" role="img" aria-label="Boiling point against period for the Group 14 hydrides CH4, SiH4, GeH4 and SnH4, which rise steadily from minus 162 to minus 52 degrees Celsius, and the Group 16 hydrides H2O, H2S, H2Se and H2Te, which rise from minus 60 to minus 2 degrees Celsius with water far above the trend at 100 degrees Celsius">'
       + "".join(p) + '</svg><figcaption>Boiling points of the Group 14 and Group 16 hydrides against period. Both groups rise as the molecules get larger, but H₂O sits far above the line that H₂S, H₂Se and H₂Te suggest.</figcaption></figure>')
print(svg)
