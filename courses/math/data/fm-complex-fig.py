# data/fm-complex-fig.py: builds the two hand SVG figures of P25 and checks label boxes.
# Run: py data/fm-complex-fig.py   (prints both figures; paste them into the chapters)
from math import cos, sin, radians, pi, hypot

def pt(cx, cy, R, deg):
    return cx + R * cos(radians(deg)), cy - R * sin(radians(deg))

def box(x, y, text, anchor="start"):
    w = 7.2 * len(text)
    x0 = x if anchor == "start" else x - w / 2 if anchor == "middle" else x - w
    return (x0, y - 10, x0 + w, y + 3)

def overlap(a, b, pad=3):
    return not (a[2] + pad < b[0] or b[2] + pad < a[0] or a[3] + pad < b[1] or b[3] + pad < a[1])

# ---------------- figure 1: z, z^2, z^3 and z^-1 on the unit circle (theta = 50 degrees) ----------------
cx, cy, R = 150.0, 150.0, 100.0
th = 50
out = []
out.append('<figure class="fig small"><svg viewBox="20 20 270 260" role="img" aria-label="An Argand diagram with the unit circle. The point z on the circle makes an angle theta of 50 degrees with the real axis. The points z squared and z cubed lie on the same circle at angles 2 theta and 3 theta, each one a further rotation by theta. The point z to the power minus one lies at angle minus theta, below the real axis.">')
out.append(f'<line class="ln" x1="{cx-118}" y1="{cy}" x2="{cx+122}" y2="{cy}" marker-end="url(#ah)"/>')
out.append(f'<line class="ln" x1="{cx}" y1="{cy+112}" x2="{cx}" y2="{cy-118}" marker-end="url(#ah)"/>')
out.append(f'<circle class="ln-m thin dash" cx="{cx}" cy="{cy}" r="{R}" fill="none"/>')
labels = []
pts = {'z': 50, 'z²': 100, 'z³': 150, 'z⁻¹': -50}
for name, a in pts.items():
    x, y = pt(cx, cy, R, a)
    out.append(f'<line class="c1" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>' if a != -50 else f'<line class="c3 dash" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}"/>')
for name, a in pts.items():
    x, y = pt(cx, cy, R, a)
    out.append(f'<circle class="fi" cx="{x:.1f}" cy="{y:.1f}" r="3.5"/>')
# arcs radius 34 between successive rays
r0 = 34
for a0, a1 in [(0, 50), (50, 100), (100, 150), (0, -50)]:
    x0, y0 = pt(cx, cy, r0, a0)
    x1, y1 = pt(cx, cy, r0, a1)
    sweep = 0 if a1 > a0 else 1
    out.append(f'<path class="ln-m" d="M{x0:.1f} {y0:.1f}A{r0} {r0} 0 0 {sweep} {x1:.1f} {y1:.1f}" fill="none"/>')
# labels for arcs (theta), at radius 52 on the bisector
arc_labels = [('θ', 25), ('θ', 75), ('θ', 125), ('−θ', -25)]
tl = []
for t, a in arc_labels:
    x, y = pt(cx, cy, 54, a)
    anchor = 'middle'
    out.append(f'<text class="tl" x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle">{t}</text>')
    tl.append(box(x, y + 4, t, 'middle'))
# point labels, outside the circle
lab = {'z': (50, 'start', 8, 0), 'z²': (100, 'end', -4, -6), 'z³': (150, 'end', -4, -4), 'z⁻¹': (-50, 'start', 8, 12)}
for name, (a, anc, dx, dy) in lab.items():
    x, y = pt(cx, cy, R, a)
    lx, ly = x + dx, y + dy
    out.append(f'<text class="tl" x="{lx:.1f}" y="{ly:.1f}"' + (' text-anchor="end"' if anc == 'end' else '') + f'>{name}</text>')
    tl.append(box(lx, ly, name, anc))
out.append(f'<text class="tl" x="{cx+123}" y="{cy+16}" text-anchor="end">Re</text>'); tl.append(box(cx + 123, cy + 16, 'Re', 'end'))
out.append(f'<text class="tl" x="{cx+8}" y="{cy-112}">Im</text>'); tl.append(box(cx + 8, cy - 112, 'Im'))
out.append(f'<text class="tl tc" x="{cx+100}" y="{cy+14}">1</text>'); tl.append(box(cx + 100, cy + 14, '1', 'middle'))
out.append(f'<text class="tl" x="{cx-8}" y="{cy+16}" text-anchor="end">O</text>'); tl.append(box(cx - 8, cy + 16, 'O', 'end'))
out.append('</svg><figcaption>On the unit circle, multiplying by \\(z = \\cos\\theta + \\mathrm{i}\\sin\\theta\\) turns a point through \\(\\theta\\) anticlockwise. So \\(z^2\\) and \\(z^3\\) are at \\(2\\theta\\) and \\(3\\theta\\), and dividing by \\(z\\) turns it back: \\(z^{-1}\\) is at \\(-\\theta\\).</figcaption></figure>')
fig1 = "\n".join(out)

# label collision check (labels vs each other)
for i in range(len(tl)):
    for j in range(i + 1, len(tl)):
        if overlap(tl[i], tl[j]):
            print("OVERLAP fig1", i, j, tl[i], tl[j])
# labels vs rays: distance from label centre to every ray segment (origin to point) must exceed 6
def dist_seg(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return hypot(px - (ax + t * dx), py - (ay + t * dy))
rays = [(cx, cy) + pt(cx, cy, R, a) for a in (50, 100, 150, -50)] + [(cx - 118, cy, cx + 122, cy), (cx, cy + 112, cx, cy - 118)]
for k, b in enumerate(tl):
    # sample the box corners and centre
    for (px, py) in [((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), (b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3])]:
        for r in rays:
            d = dist_seg(px, py, *r)
            if d < 3:
                print("LABEL NEAR LINE fig1", k, tl[k], r, round(d, 1))

# ---------------- figure 2: sixth roots of unity ----------------
cx2, cy2, R2 = 175.0, 150.0, 100.0
o = []
o.append('<figure class="fig small"><svg viewBox="10 20 310 260" role="img" aria-label="An Argand diagram with the unit circle and the six solutions of z to the power 6 equals 1 marked as the corners of a regular hexagon: 1, e to the i pi over 3, e to the 2 i pi over 3, minus 1, e to the minus 2 i pi over 3, and e to the minus i pi over 3. The angle between neighbouring roots is 60 degrees.">')
o.append(f'<line class="ln" x1="{cx2-125}" y1="{cy2}" x2="{cx2+132}" y2="{cy2}" marker-end="url(#ah)"/>')
o.append(f'<line class="ln" x1="{cx2}" y1="{cy2+112}" x2="{cx2}" y2="{cy2-118}" marker-end="url(#ah)"/>')
o.append(f'<circle class="ln-m thin dash" cx="{cx2}" cy="{cy2}" r="{R2}" fill="none"/>')
P = [pt(cx2, cy2, R2, 60 * k) for k in range(6)]
o.append('<polygon class="fm s-acc sw2" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in P) + '"/>')
for (x, y) in P:
    o.append(f'<line class="ln-m thin" x1="{cx2}" y1="{cy2}" x2="{x:.1f}" y2="{y:.1f}"/>')
for (x, y) in P:
    o.append(f'<circle class="fi" cx="{x:.1f}" cy="{y:.1f}" r="3.5"/>')
x0, y0 = pt(cx2, cy2, 30, 0); x1, y1 = pt(cx2, cy2, 30, 60)
o.append(f'<path class="ln-m" d="M{x0:.1f} {y0:.1f}A30 30 0 0 0 {x1:.1f} {y1:.1f}" fill="none"/>')
tl2 = []
xa, ya = pt(cx2, cy2, 46, 30)
o.append(f'<text class="tl" x="{xa:.1f}" y="{ya+4:.1f}" text-anchor="middle">π/3</text>'); tl2.append(box(xa, ya + 4, 'π/3', 'middle'))
names = ['1', 'e^{iπ/3}', 'e^{2iπ/3}', '−1', 'e^{−2iπ/3}', 'e^{−iπ/3}']
names = ['1', 'ω', 'ω²', 'ω³ = −1', 'ω⁴', 'ω⁵']
place = [(5, 17, 'start'), (8, -8, 'start'), (-6, -8, 'end'), (-4, -8, 'end'), (-6, 16, 'end'), (8, 16, 'start')]
for k, nm in enumerate(names):
    x, y = P[k]
    dx, dy, anc = place[k]
    lx, ly = x + dx, y + dy
    o.append(f'<text class="tl" x="{lx:.1f}" y="{ly:.1f}"' + (' text-anchor="end"' if anc == 'end' else '') + f'>{nm}</text>')
    tl2.append(box(lx, ly, nm, anc))
o.append(f'<text class="tl" x="{cx2+133}" y="{cy2+16}" text-anchor="end">Re</text>'); tl2.append(box(cx2 + 133, cy2 + 16, 'Re', 'end'))
o.append(f'<text class="tl" x="{cx2+8}" y="{cy2-112}">Im</text>'); tl2.append(box(cx2 + 8, cy2 - 112, 'Im'))
o.append('</svg><figcaption>The six solutions of \\(z^6 = 1\\) are the corners of a regular hexagon on the unit circle, with \\(\\omega = \\mathrm{e}^{\\mathrm{i}\\pi/3}\\). Neighbouring roots are \\(\\pi/3\\) apart.</figcaption></figure>')
fig2 = "\n".join(o)
for i in range(len(tl2)):
    for j in range(i + 1, len(tl2)):
        if overlap(tl2[i], tl2[j]):
            print("OVERLAP fig2", i, j, tl2[i], tl2[j])
rays2 = [(cx2, cy2) + P[k] for k in range(6)] + [(cx2 - 125, cy2, cx2 + 132, cy2), (cx2, cy2 + 112, cx2, cy2 - 118)]
for k, b in enumerate(tl2):
    for (px, py) in [((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), (b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3])]:
        for r in rays2:
            d = dist_seg(px, py, *r)
            if d < 3:
                print("LABEL NEAR LINE fig2", k, tl2[k], r, round(d, 1))
# polygon edges too
edges = [P[k] + P[(k + 1) % 6] for k in range(6)]
for k, b in enumerate(tl2):
    for (px, py) in [((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), (b[0], b[1]), (b[2], b[1]), (b[0], b[3]), (b[2], b[3])]:
        for e in edges:
            d = dist_seg(px, py, *e)
            if d < 3:
                print("LABEL NEAR EDGE fig2", k, tl2[k], round(d, 1))

import sys
open("scratch_fig1.svg", "w", encoding="utf-8").write(fig1) if False else None
import re
fix = lambda s: re.sub(r"class=\"tl\"([^>]*?) text-anchor=\"(end|middle)\"", lambda m: "class=\"tl " + ("te" if m.group(2) == "end" else "tc") + "\"" + m.group(1), s)
print(fix(fig1))
print("=====")
print(fix(fig2))
