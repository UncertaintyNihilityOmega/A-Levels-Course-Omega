# Generates the binary search figure for cs.algorithms2 (prints the SVG; paste into the chapter).
V = [3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55]
TARGET = 35
X0, W, H, DY = 60, 24, 26, 46
rows = []
low, high = 1, 11
while low <= high:
    mid = (low + high) // 2
    rows.append((low, high, mid))
    if V[mid - 1] == TARGET:
        break
    if V[mid - 1] < TARGET:
        low = mid + 1
    else:
        high = mid - 1
assert rows == [(1, 11, 6), (7, 11, 9), (7, 8, 7), (8, 8, 8)]
parts = []
labels = []   # (x0, x1, y_top, y_bottom) boxes for the overlap check
for r, (lo, hi, mid) in enumerate(rows):
    y = 14 + r * DY
    parts.append(f'<text class="tl te" x="52" y="{y + 18}">pass {r + 1}</text>')
    for i in range(1, 12):
        x = X0 + (i - 1) * W
        cls = "f1" if i == mid else ("fm" if lo <= i <= hi else "fp")
        parts.append(f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="{W}" height="{H}"/>')
        parts.append(f'<text class="tl tc" x="{x + W // 2}" y="{y + 18}">{V[i - 1]}</text>')
        tag = ("L" if i == lo else "") + ("M" if i == mid else "") + ("H" if i == hi else "")
        if tag:
            parts.append(f'<text class="tl tc tb" x="{x + W // 2}" y="{y + H + 14}">{tag}</text>')
            assert len(tag) * 8 <= W + 4
parts.append(f'<text class="tl" x="14" y="{14 + 4 * DY - 4}">Target 35: found at position 8 on pass 4</text>')
height = 14 + 4 * DY + 6
svg = (f'<figure class="fig small"><svg viewBox="0 0 340 {height}" role="img" aria-label="Binary search for 35 in a sorted array of eleven numbers: 3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55. '
       'Pass 1 has Low 1, High 11, Mid 6 (26). Pass 2 has Low 7, High 11, Mid 9 (41). Pass 3 has Low 7, High 8, Mid 7 (30). Pass 4 has Low 8, High 8, Mid 8 (35), so 35 is found at position 8.">'
       + "".join(parts) +
       '</svg><figcaption>Each pass halves the part of the array still in play. The cell marked M is the middle one that is compared; L and H mark Low and High. Cells outside the current range are never looked at again.</figcaption></figure>')
print(svg)
