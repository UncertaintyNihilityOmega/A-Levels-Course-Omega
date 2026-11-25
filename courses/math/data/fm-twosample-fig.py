# data/fm-twosample-fig.py: writes the paired-data SVG of math.fm.twosample and checks its coordinates.
# Run from the course folder: py data/fm-twosample-fig.py   (replaces the <svg>...</svg> inside the chapter's figure)
import re

bef = [45, 52, 38, 60, 49, 55, 41, 57]
aft = [42, 50, 37, 56, 47, 51, 40, 53]
XB, XA = 120, 250
Y = lambda v: round(200 - (v - 35) * 7)
mb, ma = sum(bef) / 8, sum(aft) / 8
rows = []
rows.append('<svg viewBox="0 0 360 240" role="img" aria-label="Paired data. Eight people are timed before and after practice. Eight points in the left column, labelled before, are joined by straight lines to eight points in the right column, labelled after. Every line slopes slightly downwards. The mean of the before column is 49.6 and the mean of the after column is 47.0, each shown by a short thick bar beside its column.">')
rows.append('<line class="ax" x1="8" y1="215" x2="8" y2="18"/>')
rows.append('<text class="tl" x="16" y="16">time (s)</text>')
rows.append('<g class="ln-m thin">')
for b, a in zip(bef, aft):
    rows.append(f'<line x1="{XB}" y1="{Y(b)}" x2="{XA}" y2="{Y(a)}"/>')
rows.append('</g>')
rows.append('<g class="f1 s-acc">')
for b in bef:
    rows.append(f'<circle cx="{XB}" cy="{Y(b)}" r="3.5"/>')
for a in aft:
    rows.append(f'<circle cx="{XA}" cy="{Y(a)}" r="3.5"/>')
rows.append('</g>')
yb, ya = round(200 - (mb - 35) * 7, 1), round(200 - (ma - 35) * 7, 1)
rows.append(f'<line class="c2 sw3" x1="92" y1="{yb}" x2="108" y2="{yb}"/>')
rows.append(f'<line class="c2 sw3" x1="262" y1="{ya}" x2="278" y2="{ya}"/>')
rows.append(f'<text class="tl" x="86" y="{round(yb + 4)}" text-anchor="end">mean 49.6</text>')
rows.append(f'<text class="tl" x="284" y="{round(ya + 4)}">mean 47.0</text>')
rows.append(f'<text class="tl" x="{XB}" y="232" text-anchor="middle">before</text>')
rows.append(f'<text class="tl" x="{XA}" y="232" text-anchor="middle">after</text>')
rows.append('</svg>')
svg = '\n'.join(rows)

# coordinate checks: labels clear of the axis, the bars and the points
assert 86 - 63 - 8 >= 12          # "mean 49.6" box (63 px wide) starts well right of the axis at x = 8
assert 284 + 63 <= 360 - 10       # "mean 47.0" stays inside the viewBox
assert 108 + 8 <= XB - 3.5        # before bar clear of the points
assert 262 - (XA + 3.5) >= 8
assert max(Y(v) for v in bef + aft) + 3.5 < 232 - 12   # lowest point above the column titles
assert 16 + 56 < XB - 3.5 - 4   # "time (s)" label (about 56 px wide) is left of the first column

path = 'chapters/math.fm.twosample.md'
s = open(path, encoding='utf-8', newline='').read()
new, n = re.subn(r'<svg viewBox="0 0 3[0-9]{2} 240".*?</svg>', lambda m: svg, s, count=1, flags=re.S)
assert n == 1
open(path, 'w', encoding='utf-8', newline='').write(new)
print('figure written;', 'mean bars at y', yb, ya)
