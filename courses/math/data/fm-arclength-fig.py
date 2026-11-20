# data/fm-arclength-fig.py: the chord figure of math.fm.arclength (prints SVG lines, checks label boxes).
X = lambda t: 40 + 250 * t
Y = lambda t: 190 - 150 * t * t
tp, tq = 0.45, 0.8
P = (X(tp), Y(tp)); Q = (X(tq), Y(tq)); R = (Q[0], P[1])
pts = [(X(t / 20), Y(t / 20)) for t in range(4, 20)]
path = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
labels = []
def lab(name, x, y, t, w=None):
    w = w or 7 * len(t)
    labels.append((name, x, y - 10, x + w, y + 3))
    return f'<text class="tl halo" x="{x}" y="{y}">{t}</text>'
o = [f'<path class="c1 sw2" fill="none" d="{path}"/>',
     f'<line class="c2 sw2" x1="{P[0]:.1f}" y1="{P[1]:.1f}" x2="{Q[0]:.1f}" y2="{Q[1]:.1f}"/>',
     f'<line class="ln-m thin dash" x1="{P[0]:.1f}" y1="{P[1]:.1f}" x2="{R[0]:.1f}" y2="{R[1]:.1f}"/>',
     f'<line class="ln-m thin dash" x1="{R[0]:.1f}" y1="{R[1]:.1f}" x2="{Q[0]:.1f}" y2="{Q[1]:.1f}"/>',
     f'<path class="ln-m thin" fill="none" d="M{R[0]-8:.1f} {R[1]:.1f} L{R[0]-8:.1f} {R[1]-8:.1f} L{R[0]:.1f} {R[1]-8:.1f}"/>',
     f'<circle class="fi" cx="{P[0]:.1f}" cy="{P[1]:.1f}" r="3.5"/>', f'<circle class="fi" cx="{Q[0]:.1f}" cy="{Q[1]:.1f}" r="3.5"/>',
     lab("P", 82, 148, "P (x, y)"), lab("Q", 100, 80, "Q (x + δx, y + δy)"),
     lab("ds", 164, 114, "δs"), lab("dx", 186, 178, "δx"), lab("dy", round(Q[0]) + 8, 134, "δy")]
print(P, Q, R)
print("\n".join(o))
for i in range(len(labels)):
    for j in range(i + 1, len(labels)):
        a, b = labels[i], labels[j]
        if not (a[3] + 4 < b[1] or b[3] + 4 < a[1] or a[4] + 4 < b[2] or b[4] + 4 < a[2]):
            print("OVERLAP", a[0], b[0])
# distance of each label box from the nearest drawn line (sampled), at least 4 px
import math
def seg(p, q, n=200):
    return [(p[0] + (q[0] - p[0]) * k / n, p[1] + (q[1] - p[1]) * k / n) for k in range(n + 1)]
lines = pts + seg(P, Q) + seg(P, R) + seg(R, Q)
for (name, x0, y0, x1, y1) in labels:
    dmin = 1e9
    for (px, py) in lines:
        dx = max(x0 - px, 0, px - x1); dy = max(y0 - py, 0, py - y1)
        dmin = min(dmin, math.hypot(dx, dy))
    print(name, "min gap", round(dmin, 1))
