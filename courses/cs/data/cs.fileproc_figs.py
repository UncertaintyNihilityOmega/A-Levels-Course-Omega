# data/cs.fileproc_figs.py: builds the two SVG figures of chapters/cs.fileproc.md and checks their geometry.
# Run: py -X utf8 data/cs.fileproc_figs.py   (prints the SVG blocks to paste into the chapter)
from itertools import combinations

CHAR = 7.0  # px per character of a 13 px label


def overlap(a, b, gap=4):
    return not (a[2] + gap <= b[0] or b[2] + gap <= a[0] or a[3] + gap <= b[1] or b[3] + gap <= a[1])


def label_box(x, y, text, anchor="start"):
    w = len(text) * CHAR
    if anchor == "middle":
        x0 = x - w / 2
    else:
        x0 = x
    return (x0, y - 10, x0 + w, y + 3)


# ---------------------------------------------------------------- Figure 1: try / except / else / finally
W1, H1 = 350, 310
out = []
boxes = {}
labels = []


def box(name, x, y, w, h, text):
    out.append(f'<rect class="fm s-acc sw2" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>')
    out.append(f'<text class="tl tb tc" x="{x + w / 2:g}" y="{y + 22}">{text}</text>')
    assert len(text) * CHAR + 16 <= w, (text, w)
    boxes[name] = (x, y, x + w, y + h)


box("try", 100, 12, 150, 34, "try block")
box("else", 15, 118, 140, 34, "else block")
box("except", 195, 118, 140, 34, "except block")
box("finally", 100, 206, 150, 34, "finally block")
box("go", 100, 272, 150, 30, "program continues")
arrows = [
    (140, 46, 90, 118),   # try -> else
    (210, 46, 260, 118),  # try -> except
    (90, 152, 140, 206),  # else -> finally
    (260, 152, 210, 206),  # except -> finally
    (175, 240, 175, 272),  # finally -> go
]
for x1, y1, x2, y2 in arrows:
    out.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#ah)"/>')
# labels on the two branches
lab_none = (15, 86, "none")
lab_exc = (252, 86, "exception")
for x, y, t in (lab_none, lab_exc):
    out.append(f'<text class="tl halo" x="{x}" y="{y}">{t}</text>')
    labels.append(label_box(x, y, t))


def seg_x(a, y):
    x1, y1, x2, y2 = a
    return x1 + (x2 - x1) * (y - y1) / (y2 - y1)


for lab in labels:
    for a in arrows[:2]:
        for y in (lab[1], lab[3]):
            xx = seg_x(a, y)
            assert not (lab[0] - 4 <= xx <= lab[2] + 4), ("label touches arrow", lab, a)
names = list(boxes)
for a, b in combinations(names, 2):
    assert not overlap(boxes[a], boxes[b], 4), (a, b)
for lab in labels:
    for b in boxes.values():
        assert not overlap(lab, b, 4), (lab, b)
    assert lab[0] >= 0 and lab[2] <= W1
for x1, y1, x2, y2 in arrows:
    assert ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 >= 20
svg1 = (f'<svg viewBox="0 0 {W1} {H1}" role="img" aria-label="A flow diagram of try and except. The try block runs first. If there is no exception, control passes to the optional else block. If an exception is raised, control passes to the matching except block. Both routes then reach the optional finally block, which always runs, and the program continues.">'
        + "".join(out) + "</svg>")

# ---------------------------------------------------------------- Figure 2: a random file of fixed-length records
W2, H2 = 350, 150
out = []
RL = 25
x0, bw, by, bh = 20, 78, 52, 36
rects = []
for i in range(4):
    x = x0 + i * bw
    out.append(f'<rect class="fm s-acc sw2" x="{x}" y="{by}" width="{bw}" height="{bh}"/>')
    t = f"record {i + 1}"
    out.append(f'<text class="tl tc" x="{x + bw / 2:g}" y="{by + 23}">{t}</text>')
    assert len(t) * CHAR + 8 <= bw
    rects.append((x, by, x + bw, by + bh))
tick_labels = []
for i in range(5):
    x = x0 + i * bw
    out.append(f'<line class="ln-m thin" x1="{x}" y1="{by + bh}" x2="{x}" y2="{by + bh + 10}"/>')
    t = str(i * RL)
    out.append(f'<text class="tl tc" x="{x}" y="{by + bh + 26}">{t}</text>')
    tick_labels.append(label_box(x, by + bh + 26, t, "middle"))
seek_x = x0 + 2 * bw
out.append(f'<text class="tl tc" x="{seek_x}" y="22">seek(50)</text>')
seek_box = label_box(seek_x, 22, "seek(50)", "middle")
out.append(f'<line class="ln" x1="{seek_x}" y1="30" x2="{seek_x}" y2="{by}" marker-end="url(#ah)"/>')
out.append(f'<text class="tl" x="20" y="{by + bh + 52}">position = (n − 1) × 25</text>')
formula = label_box(20, by + bh + 52, "position = (n − 1) × 25")
for a, b in combinations(rects, 2):
    assert not overlap(a, b, 0) or a[2] == b[0] or b[2] == a[0]
for t in tick_labels:
    assert t[0] >= 0 and t[2] <= W2
    assert not overlap(t, formula, 4)
    for u in tick_labels:
        if u is not t:
            assert not overlap(t, u, 4)
assert seek_box[3] + 4 < 30 and seek_box[2] <= W2 and formula[3] < H2
svg2 = (f'<svg viewBox="0 0 {W2} {H2}" role="img" aria-label="A random file drawn as four boxes in a row, record 1 to record 4, each 25 bytes long. Tick marks below show where each record starts: byte 0, 25, 50, 75, and the end of the file at byte 100. An arrow labelled seek(50) points at the start of record 3. The formula under the picture is position equals n minus 1, times 25.">'
        + "".join(out) + "</svg>")

print("FIGURE 1\n" + svg1 + "\n\nFIGURE 2\n" + svg2 + "\n\ngeometry ok")
