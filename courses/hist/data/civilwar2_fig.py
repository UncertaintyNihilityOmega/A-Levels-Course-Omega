# Generates the secession-ladder SVG for hist.us.civilwar.2 (prints the <svg> element) and checks its layout.
W = 340
X, BW = 10, 320
boxes = [
    ("fp", ["6 November 1860", "Lincoln elected president", "(no Southern electoral votes)"]),
    ("fm2", ["20 December 1860", "South Carolina secedes"]),
    ("fm2", ["9 January–1 February 1861", "Mississippi, Florida, Alabama,", "Georgia, Louisiana, Texas secede"]),
    ("fm2", ["4–18 February 1861", "Confederate States formed at Montgomery;", "Jefferson Davis inaugurated 18 February"]),
    ("fp", ["4 March 1861", "Lincoln inaugurated: no purpose to", "interfere with slavery where it exists"]),
    ("fm2", ["12–15 April 1861", "Fort Sumter bombarded, then surrenders;", "Lincoln calls for 75,000 volunteers"]),
    ("fm2", ["17 April–8 June 1861", "Virginia, Arkansas, Tennessee and", "North Carolina secede"]),
]
GAP, PAD, LH = 30, 8, 17
y = 10
out = []
rects = []
for cls, lines in boxes:
    h = 2 * PAD + 2 + LH * len(lines) - 3
    rects.append((y, h))
    out.append(f'<rect class="{cls} s-acc sw2" x="{X}" y="{y}" width="{BW}" height="{h}" rx="5"/>')
    ty = y + PAD + 11
    for i, s in enumerate(lines):
        assert len(s) * 7 <= BW - 8, s
        bold = " tb" if i == 0 else ""
        out.append(f'<text class="tl{bold} tc" x="{X + BW // 2}" y="{ty}">{s}</text>')
        ty += LH
    assert ty - LH + 4 <= y + h, (lines, ty, y + h)
    y += h + GAP
H = y - GAP + 10
arrows = []
for (y1, h1), (y2, h2) in zip(rects, rects[1:]):
    a, b = y1 + h1, y2
    assert b - a >= 20
    arrows.append(f'<line class="ln" x1="{X + BW // 2}" y1="{a + 2}" x2="{X + BW // 2}" y2="{b - 2}" marker-end="url(#ah)"/>')
print(f'VIEWBOX 0 0 {W} {H}')
print(''.join(out) + ''.join(arrows))
