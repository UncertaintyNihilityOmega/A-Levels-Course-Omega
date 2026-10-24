# P12 figure helpers and the synthesis flow charts (run from the course folder: py data/mk_fig_synthesis.py a|b). Prints SVG fragments and checks label clearance.
import math, json, sys

def f(v):
    s = ('%.1f' % v).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def tw(s):
    w = 0
    for ch in s:
        w += 5.5 if ch in '₀₁₂₃₄₅₆₇₈₉⁺⁻' else (3.5 if ch in 'Il1()' else 7.0)
    return w

# ---------- flow figures ----------
def flow_a():
    P = []
    cx, bw, bh = 95, 124, 28
    tops = [10, 80, 150, 230]
    names = ['ethene', 'ethanol', 'ethanoic acid', 'ethyl ethanoate']
    for t, n in zip(tops, names):
        P.append('<rect class="fm s-acc" x="%s" y="%s" width="%d" height="%d" rx="8"/>' % (f(cx - bw / 2), t, bw, bh))
        P.append('<text class="tl tc" x="%d" y="%s">%s</text>' % (cx, f(t + 19), n))
    # arrows between boxes
    for i in range(3):
        y0 = tops[i] + bh + 3
        y1 = tops[i + 1] - 3
        P.append('<path class="ln" d="M%d %sV%s" marker-end="url(#ah)"/>' % (cx, f(y0), f(y1)))
    P.append('<text class="tl" x="106" y="%s">steam, H₃PO₄</text>' % f((tops[0] + bh + tops[1]) / 2 + 4))
    P.append('<text class="tl" x="106" y="%s">K₂Cr₂O₇/H⁺,</text>' % f((tops[1] + bh + tops[2]) / 2 - 2))
    P.append('<text class="tl" x="106" y="%s">heat under reflux</text>' % f((tops[1] + bh + tops[2]) / 2 + 15))
    P.append('<text class="tl" x="106" y="%s">concentrated H₂SO₄,</text>' % f((tops[2] + bh + tops[3]) / 2 - 2))
    P.append('<text class="tl" x="106" y="%s">heat</text>' % f((tops[2] + bh + tops[3]) / 2 + 15))
    # ethanol branch to the ester
    yb = tops[1] + 14
    ye = tops[3] + 14
    P.append('<path class="ln" d="M160 %sH290V%sH162" marker-end="url(#ah)"/>' % (f(yb), f(ye)))
    P.append('<text class="tl" x="234" y="%s">ethanol</text>' % f((yb + ye) / 2 + 4))
    return '\n'.join(P)

def flow_b():
    P = []
    cx, bw, bh = 95, 124, 28
    tops = [10, 94, 178, 262]
    names = ['propan-1-ol', '1-bromopropane', 'butanenitrile', 'butanoic acid']
    cnt = ['3 carbons', '3 carbons', '4 carbons', '4 carbons']
    for t, n, c in zip(tops, names, cnt):
        P.append('<rect class="fm s-acc" x="%s" y="%s" width="%d" height="%d" rx="8"/>' % (f(cx - bw / 2), t, bw, bh))
        P.append('<text class="tl tc" x="%d" y="%s">%s</text>' % (cx, f(t + 19), n))
        P.append('<text class="tl ta" x="170" y="%s">%s</text>' % (f(t + 19), c))
    for i in range(3):
        y0 = tops[i] + bh + 3
        y1 = tops[i + 1] - 3
        P.append('<path class="ln" d="M%d %sV%s" marker-end="url(#ah)"/>' % (cx, f(y0), f(y1)))
    m = lambda i: (tops[i] + bh + tops[i + 1]) / 2
    P.append('<text class="tl" x="106" y="%s">HBr(g)</text>' % f(m(0) + 4))
    P.append('<text class="tl" x="106" y="%s">KCN in ethanol,</text>' % f(m(1) - 2))
    P.append('<text class="tl" x="106" y="%s">heat under reflux</text>' % f(m(1) + 15))
    P.append('<text class="tl" x="106" y="%s">dilute acid,</text>' % f(m(2) - 2))
    P.append('<text class="tl" x="106" y="%s">heat under reflux</text>' % f(m(2) + 15))
    return '\n'.join(P)

# ---------- IR ----------
X0, XS = 40, 0.08           # wavenumber 4000 -> x 40
YB, YF = 32, 150            # baseline, axis
def wx(w): return X0 + (4000 - w) * XS

def ir_curve(dips):
    # dips: (wn, half-width in wn (sigma), depth 0..0.95)
    pts = []
    x = 40.0
    while x <= 320.01:
        w = 4000 - (x - X0) / XS
        prod = 1.0
        for (c, s, d) in dips:
            prod *= (1 - d * math.exp(-0.5 * ((w - c) / s) ** 2))
        y = YB + (1 - prod) * 92
        pts.append((x, y))
        x += 2
    return pts

def ir_svg(title, dips, labels, fp=True):
    pts = ir_curve(dips)
    keep = []
    for i, (x, y) in enumerate(pts):
        flat = abs(y - YB) < 0.3
        pf = i > 0 and abs(pts[i-1][1] - YB) < 0.3
        nf = i < len(pts) - 1 and abs(pts[i+1][1] - YB) < 0.3
        if flat and pf and nf:
            continue
        keep.append((x, y))
    d = 'M' + 'L'.join('%s %s' % (f(x), f(y)) for x, y in keep)
    P = []
    P.append('<path class="ax" d="M40 %d H325" marker-end="url(#ahm)"/>' % YF)
    P.append('<path class="ax" d="M40 %d V16" marker-end="url(#ahm)"/>' % YF)
    for w in (4000, 3000, 2000, 1500, 1000, 500):
        x = wx(w)
        P.append('<path class="ln-m thin" d="M%s %d v4"/>' % (f(x), YF))
        P.append('<text class="ts tc" x="%s" y="%d">%d</text>' % (f(x), YF + 16, w))
    P.append('<text class="tl tc" x="180" y="%d">wavenumber / cm⁻¹</text>' % (YF + 36))
    P.append('<text class="tl" x="46" y="14">transmittance / %</text>')
    P.append('<path class="ln-m thin dash" d="M%s 22 V%d"/>' % (f(wx(1500)), YF))
    P.append('<text class="tl" x="%s" y="14">fingerprint</text>' % f(wx(1500) + 5))
    P.append('<path class="c1 sw2" d="%s"/>' % d)
    boxes = []
    for (wn, txt, yy) in labels:
        x = wx(wn)
        P.append('<text class="tl tc" x="%s" y="%s">%s</text>' % (f(x), f(yy), txt))
        w = tw(txt)
        boxes.append((x - w / 2, yy - 10, x + w / 2, yy + 3, txt))
    # clearance check: label boxes vs curve points
    bad = []
    for (x0, y0, x1, y1, t) in boxes:
        for (px, py) in pts:
            if x0 - 4 <= px <= x1 + 4 and y0 - 4 <= py <= y1 + 4:
                bad.append((t, px, py))
                break
    # fingerprint label vs curve and y label
    fx0, fx1 = wx(1500) + 5, wx(1500) + 5 + tw('fingerprint')
    for (px, py) in pts:
        if fx0 - 3 <= px <= fx1 + 3 and py < 22:
            bad.append(('fingerprint', px, py))
    ymin = max(y for _, y in pts)
    return '\n'.join(P), bad, ymin

if __name__ == '__main__':
    which = sys.argv[1]
    if which == 'a':
        print(flow_a())
    elif which == 'b':
        print(flow_b())
