# data/p23_fig.py: builds and checks the corporate-state figure for hist.d.italy.3
# label box = 7 px per character wide, 13 px tall; baseline y, top y-10
W = 340
boxes = []   # (x, y, w, h, cls, lines)
def box(x, y, w, h, cls, lines, bold_first=True):
    boxes.append((x, y, w, h, cls, lines, bold_first))

box(30, 10, 280, 46, "fm", ["Mussolini, Head of Government", "Ministry of Corporations (1926)"])
box(30, 80, 280, 46, "fm2", ["National Council of Corporations", "advises and coordinates (law of 1930)"])
box(30, 150, 280, 64, "fm2", ["22 corporations (law of 1934)", "one for each branch of the economy:", "employers, workers and party officials"])
box(10, 240, 150, 64, "fp", ["Employers' bodies", "Confindustria and", "other confederations"])
box(180, 240, 150, 64, "fp", ["Fascist unions", "the only unions the", "state recognises"])
box(30, 330, 280, 64, "fm", ["Labour courts (Rocco Law, 1926)", "settle disputes; strikes and", "lockouts are crimes"])
H = 394 + 15

arrows = [  # (x1,y1,x2,y2)
    (170, 56, 170, 80), (170, 126, 170, 150),
    (85, 240, 85, 214), (255, 240, 255, 214),
    (170, 330, 170, 214),
]
# fix: last arrow goes from labour courts up to corporations is long; instead place courts under the two bodies
arrows[-1] = (170, 330, 170, 304)

out = []
for (x, y, w, h, cls, lines, b) in boxes:
    out.append(f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    n = len(lines)
    # centre the block of lines vertically: line pitch 17
    top = y + (h - (n - 1) * 17) / 2 + 4
    for i, t in enumerate(lines):
        yy = round(top + i * 17)
        cl = "tl tb tc" if i == 0 else "tl tc"
        out.append(f'<text class="{cl}" x="{x + w/2:g}" y="{yy}">{t}</text>')
        wpx = len(t) * 7
        assert wpx <= w - 10, f"label too wide: {t!r} {wpx} > {w-10}"
        assert yy - 10 >= y + 2 and yy + 3 <= y + h - 2, f"label outside box: {t!r} y={yy}"
for (x1, y1, x2, y2) in arrows:
    assert abs(y2 - y1) >= 20, f"arrow too short {abs(y2-y1)}"
    out.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#ah)"/>')
# boxes must not overlap and stay inside the viewBox
for i, a in enumerate(boxes):
    assert a[0] >= 5 and a[0] + a[2] <= W - 5 and a[1] >= 5 and a[1] + a[3] <= H - 5
    for b in boxes[i+1:]:
        assert a[0] + a[2] <= b[0] or b[0] + b[2] <= a[0] or a[1] + a[3] <= b[1] or b[1] + b[3] <= a[1], (a, b)
print(f'VIEWBOX 0 0 {W} {H}')
print("\n".join(out))
