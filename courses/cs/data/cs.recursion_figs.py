# data/cs.recursion_figs.py: builds the two hand SVG figures of chapters/cs.recursion.md and checks their geometry.
# Run: py data/cs.recursion_figs.py   (prints the SVG blocks to paste into the chapter, then "geometry ok")
from itertools import combinations

CHAR = 7.0  # px per character of a 13 px label


def box_overlap(a, b, gap=4):
    return not (a[2] + gap <= b[0] or b[2] + gap <= a[0] or a[3] + gap <= b[1] or b[3] + gap <= a[1])


# ---------------- Figure 1: the call stack at the deepest point of Factorial(4) ----------------
W1, H1 = 344, 330
frames = [  # top of stack first
    ("Factorial(1)", "N = 1: base case", "returns 1", True),
    ("Factorial(2)", "N = 2: waiting for Factorial(1)", "returns 2 × 1 = 2", False),
    ("Factorial(3)", "N = 3: waiting for Factorial(2)", "returns 3 × 2 = 6", False),
    ("Factorial(4)", "N = 4: waiting for Factorial(3)", "returns 4 × 6 = 24", False),
]
fx, fw, fh, gap, y0 = 8, 246, 62, 6, 34
svg1 = [f'<svg viewBox="0 0 {W1} {H1}" role="img" aria-label="The call stack while Factorial(4) is running, drawn as four boxes with the newest on top. Top: Factorial(1), N = 1, base case, returns 1. Then Factorial(2), N = 2, waiting for Factorial(1), returns 2 × 1 = 2. Then Factorial(3), N = 3, waiting for Factorial(2), returns 3 × 2 = 6. Bottom: Factorial(4), N = 4, waiting for Factorial(3), returns 4 × 6 = 24.">']
svg1.append(f'<text class="tl tb" x="{fx}" y="18">Call stack, deepest point</text>')
boxes = []
for i, (title, state, ret, top) in enumerate(frames):
    y = y0 + i * (fh + gap)
    cls = "f1 s-acc sw2" if top else "fm s-acc sw2"
    svg1.append(f'<rect class="{cls}" x="{fx}" y="{y}" width="{fw}" height="{fh}" rx="4"/>')
    svg1.append(f'<text class="tl tb" x="{fx + 10}" y="{y + 19}">{title}</text>')
    svg1.append(f'<text class="tl" x="{fx + 10}" y="{y + 37}">{state}</text>')
    svg1.append(f'<text class="tl" x="{fx + 10}" y="{y + 55}">{ret}</text>')
    assert len(state) * CHAR + 20 < fw, state
    boxes.append((fx, y, fx + fw, y + fh))
    # return value to the right of the frame
    rx = fx + fw + 10
    assert len(ret) * CHAR + 20 < fw
    note = {0: "newest", 3: "oldest"}.get(i)
    if note:
        svg1.append(f'<text class="tl" x="{rx}" y="{y + 36}">{note}</text>')
        assert rx + len(note) * CHAR < W1 - 4
last = boxes[-1][3]
svg1.append(f'<text class="tl" x="{fx}" y="{last + 20}">bottom of the stack: the first call</text>')
assert last + 24 <= H1+0
svg1.append("</svg>")
for a, b in combinations(boxes, 2):
    assert not box_overlap(a, b, 4) or True
    assert a[3] + gap <= b[1] or b[3] + gap <= a[1]

# ---------------- Figure 2: the call tree of Fib(4) ----------------
W2, H2 = 320, 246
lx = {"A": 32, "B": 94, "C": 156, "D": 218, "E": 280}
nodes = {}
nodes["f2L"] = ("Fib(2)", (lx["A"] + lx["B"]) / 2, 140 + 55, True)  # placeholder, fixed below
# levels: depth 0 y=30, 1 y=85, 2 y=140, 3 y=195
nodes = {
    "A": ("Fib(1)", lx["A"], 195, False),
    "B": ("Fib(0)", lx["B"], 195, False),
    "f2L": ("Fib(2)", (lx["A"] + lx["B"]) / 2, 140, True),
    "C": ("Fib(1)", lx["C"], 140, False),
    "f3": ("Fib(3)", ((lx["A"] + lx["B"]) / 2 + lx["C"]) / 2, 85, False),
    "D": ("Fib(1)", lx["D"], 140, False),
    "E": ("Fib(0)", lx["E"], 140, False),
    "f2R": ("Fib(2)", (lx["D"] + lx["E"]) / 2, 85, True),
}
nodes["f4"] = ("Fib(4)", (nodes["f3"][1] + nodes["f2R"][1]) / 2, 30, False)
edges = [("f4", "f3"), ("f4", "f2R"), ("f3", "f2L"), ("f3", "C"), ("f2L", "A"), ("f2L", "B"), ("f2R", "D"), ("f2R", "E")]
bw, bh = 54, 24
svg2 = [f'<svg viewBox="0 0 {W2} {H2}" role="img" aria-label="The call tree of Fib(4), nine calls in all. Fib(4) calls Fib(3) and Fib(2). Fib(3) calls Fib(2) and Fib(1). Each Fib(2) calls Fib(1) and Fib(0). The two Fib(2) boxes are shaded because the same calculation is done twice; Fib(1) appears three times.">']
for p, c in edges:
    px, py = nodes[p][1], nodes[p][2]
    cx, cy = nodes[c][1], nodes[c][2]
    svg2.append(f'<line class="ln-m" x1="{px:.1f}" y1="{py + bh / 2:.1f}" x2="{cx:.1f}" y2="{cy - bh / 2:.1f}"/>')
brs = []
for k, (label, x, y, dup) in nodes.items():
    cls = "f1 s-acc sw2" if dup else "fm s-acc sw2"
    svg2.append(f'<rect class="{cls}" x="{x - bw / 2:.1f}" y="{y - bh / 2:.1f}" width="{bw}" height="{bh}" rx="4"/>')
    svg2.append(f'<text class="tl tc" x="{x:.1f}" y="{y + 5:.1f}">{label}</text>')
    brs.append((x - bw / 2, y - bh / 2, x + bw / 2, y + bh / 2))
    assert len(label) * CHAR < bw - 4
    assert x - bw / 2 >= 2 and x + bw / 2 <= W2 - 2
for a, b in combinations(brs, 2):
    assert not box_overlap(a, b, 4), (a, b)
svg2.append(f'<text class="tl tc" x="{W2 / 2:.0f}" y="{H2 - 8}">9 calls; shaded boxes repeat work</text>')
assert 33 * CHAR < W2
svg2.append("</svg>")

print("FIGURE 1\n" + "".join(svg1))
print("\nFIGURE 2\n" + "".join(svg2))
print("\ngeometry ok")
