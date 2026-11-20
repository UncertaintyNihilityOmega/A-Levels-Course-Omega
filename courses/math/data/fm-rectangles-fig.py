# data/fm-rectangles-fig.py: prints the two hand SVG figures of math.fm.rectangles and checks label boxes.
from math import sqrt

def curve(f, X, Y, a, b, n=24):
    pts = []
    for i in range(n + 1):
        x = a + (b - a) * i / n
        pts.append((X(x), Y(f(x))))
    return "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)

labels = []   # (name, x, y, text)
def lab(name, x, y, t, cls="tl", anchor=None):
    w = 7 * len(t) if cls == "tl" else 6 * len(t)
    labels.append((name, x, y - 10, x + w, y + 3))
    return f'<text class="{cls} halo" x="{x}" y="{y}">{t}</text>' if cls == "tl" else f'<text class="{cls}" x="{x}" y="{y}">{t}</text>'

def fig_dec():
    X = lambda x: 40 + (x - 1) * 62
    Y = lambda y: 190 - y * 150
    f = lambda x: 1 / x
    o = []
    for r in range(1, 5):   # upper rectangles, height f(r) on [r, r+1]
        o.append(f'<rect class="fm s-acc" x="{X(r):.1f}" y="{Y(f(r)):.1f}" width="62" height="{190 - Y(f(r)):.1f}"/>')
    for r in range(1, 5):   # lower rectangles, height f(r+1) on [r, r+1]
        o.append(f'<rect class="ln-m thin dash" fill="none" x="{X(r):.1f}" y="{Y(f(r + 1)):.1f}" width="62" height="{190 - Y(f(r + 1)):.1f}"/>')
    o.append('<line class="ax" x1="30" y1="190" x2="300" y2="190" marker-end="url(#ah)"/>')
    o.append('<line class="ax" x1="40" y1="200" x2="40" y2="22" marker-end="url(#ah)"/>')
    o.append(f'<path class="c1 sw2" fill="none" d="{curve(f, X, Y, 1, 5)}"/>')
    for r in range(1, 6):
        o.append(f'<text class="ts" x="{X(r) - 3:.0f}" y="205">{r}</text>')
    o.append('<text class="tl" x="296" y="205">x</text>')
    o.append('<text class="tl" x="22" y="20">y</text>')
    for r in range(1, 5):
        o.append(lab(f"f{r}", round(X(r)) + 4, round(Y(f(r))) - 6, f"f({r})"))
    o.append(lab("curve", 214, 104, "y = 1/x"))
    return o

def fig_inc():
    X = lambda x: 40 + x * 62
    Y = lambda y: 190 - y * 70
    f = lambda x: sqrt(x)
    o = []
    for r in range(1, 5):   # upper rectangles, height f(r) on [r-1, r]
        o.append(f'<rect class="fm s-acc" x="{X(r - 1):.1f}" y="{Y(f(r)):.1f}" width="62" height="{190 - Y(f(r)):.1f}"/>')
    for r in range(2, 5):   # lower rectangles, height f(r-1) on [r-1, r]
        o.append(f'<rect class="ln-m thin dash" fill="none" x="{X(r - 1):.1f}" y="{Y(f(r - 1)):.1f}" width="62" height="{190 - Y(f(r - 1)):.1f}"/>')
    o.append('<line class="ax" x1="30" y1="190" x2="300" y2="190" marker-end="url(#ah)"/>')
    o.append('<line class="ax" x1="40" y1="200" x2="40" y2="22" marker-end="url(#ah)"/>')
    o.append(f'<path class="c1 sw2" fill="none" d="{curve(f, X, Y, 0, 4)}"/>')
    for r in range(0, 5):
        o.append(f'<text class="ts" x="{X(r) - 3:.0f}" y="205">{r}</text>')
    o.append('<text class="tl" x="296" y="205">x</text>')
    o.append('<text class="tl" x="22" y="20">y</text>')
    for r in range(1, 5):
        o.append(lab(f"f{r}", round(X(r - 1)) + 8, round(Y(f(r))) - 6, f"f({r})"))
    o.append(lab("curve", 232, 140, "y = √x"))
    return o

for name, fn in (("DEC", fig_dec), ("INC", fig_inc)):
    labels.clear()
    o = fn()
    print(name)
    print("\n".join(o))
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            a, b = labels[i], labels[j]
            if not (a[3] + 4 < b[1] or b[3] + 4 < a[1] or a[4] + 4 < b[2] or b[4] + 4 < a[2]):
                print("OVERLAP", a[0], b[0])
    for l in labels:
        print("label", l)
