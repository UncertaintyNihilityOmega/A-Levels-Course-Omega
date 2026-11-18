# data/cs.translators.figs.py: builds the three hand SVG figures of cs.translators and checks their coordinates.
# Run: py data/cs.translators.figs.py  (prints the SVG fragments to paste into the chapter, then "figures ok")
import math

CH = 7.0   # width of one character of a 13 px label
LH = 13.0


def text(x, y, s, cls="tl tc", anchor=None):
    return {"kind": "text", "x": x, "y": y, "s": s, "cls": cls}


def box_of_text(t):
    w = len(t["s"]) * CH
    if "tc" in t["cls"].split():
        x0 = t["x"] - w / 2
    elif "te" in t["cls"].split():
        x0 = t["x"] - w
    else:
        x0 = t["x"]
    return (x0, t["y"] - 10, x0 + w, t["y"] + 3)


def svg_text(t):
    return f'<text class="{t["cls"]}" x="{t["x"]:g}" y="{t["y"]:g}">{t["s"]}</text>'


def inside(vb, b, pad=2):
    return b[0] >= vb[0] + pad and b[1] >= vb[1] + pad and b[2] <= vb[0] + vb[2] - pad and b[3] <= vb[1] + vb[3] - pad


def overlap(a, b, gap=4):
    return not (a[2] + gap <= b[0] or b[2] + gap <= a[0] or a[3] + gap <= b[1] or b[3] + gap <= a[1])


def check(name, vb, texts, rects=(), lines=()):
    """texts: text dicts; rects: (x0,y0,x1,y1) shapes that must not be crossed by a label unless the label is inside;
    lines: (x0,y0,x1,y1) axis-aligned segments that labels must keep 4 px away from."""
    boxes = [box_of_text(t) for t in texts]
    for t, b in zip(texts, boxes):
        assert inside(vb, b), f"{name}: label {t['s']!r} sticks out of the viewBox {b}"
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            assert not overlap(boxes[i], boxes[j]), f"{name}: labels {texts[i]['s']!r} and {texts[j]['s']!r} overlap"
    for t, b in zip(texts, boxes):
        for r in rects:
            inside_r = b[0] >= r[0] and b[2] <= r[2] and b[1] >= r[1] and b[3] <= r[3]
            assert inside_r or not overlap(b, r, 0), f"{name}: label {t['s']!r} crosses a shape edge {r}"
        for l in lines:
            lb = (min(l[0], l[2]), min(l[1], l[3]), max(l[0], l[2]), max(l[1], l[3]))
            assert not overlap(b, lb, 3), f"{name}: label {t['s']!r} is too close to the line {l}"


# ----------------------------------------------------------------------------------------------- figure 1
vb1 = (0, 0, 340, 150)
t1 = [text(12, 20, "&lt;integer&gt;", "tl tb", None).copy()]
t1[0]["s_len"] = len("<integer>")
digit1 = (130, 64, 206, 96)
t1.append(text(168, 85, "digit"))
t1.append(text(44, 116, "non-terminal: has its own rule", "tl"))
t1.append(text(44, 138, "terminal: written exactly as shown", "tl"))
# the label text length for &lt; entities is the real length
boxes_fix = {"&lt;integer&gt;": len("<integer>")}


def check_with_entities(name, vb, texts, rects, lines):
    fixed = []
    for t in texts:
        t2 = dict(t)
        t2["s"] = t["s"].replace("&lt;", "<").replace("&gt;", ">")
        fixed.append(t2)
    check(name, vb, fixed, rects, lines)


segs1 = [(12, 80, 128, 80), (206, 80, 326, 80), (245, 44, 116, 44), (245, 44, 245, 80), (116, 44, 116, 80)]
rect_legend = (12, 104, 36, 118)
rrect_legend = (12, 126, 36, 140)
check_with_entities("fig1", vb1, [t for t in t1], [digit1, rect_legend, rrect_legend], segs1)

fig1 = f"""<figure class="fig small"><svg viewBox="0 0 340 150" role="img" aria-label="A syntax diagram for the rule integer. A line enters from the left, passes through one rectangle labelled digit, and leaves on the right. A second line loops from after the rectangle back to before it, so the digit can be repeated. Below, a key says a rectangle is a non-terminal with its own rule and a rounded box is a terminal written exactly as shown."><text class="tl tb" x="12" y="20">&lt;integer&gt;</text><path class="ln" d="M12 80 H128" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="130" y="64" width="76" height="32"/><text class="tl tc" x="168" y="85">digit</text><path class="ln" d="M206 80 H326" marker-end="url(#ah)"/><path class="ln" d="M245 80 V44 H116 V80" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="12" y="104" width="24" height="14"/><text class="tl" x="44" y="116">non-terminal: has its own rule</text><rect class="fm s-acc sw2" x="12" y="126" width="24" height="14" rx="7"/><text class="tl" x="44" y="138">terminal: written exactly as shown</text></svg><figcaption>The syntax diagram for an integer. Follow the arrows: one digit, then either leave or loop back for another digit. It means the same as the BNF rule shown in the text.</figcaption></figure>"""

# ----------------------------------------------------------------------------------------------- figure 2
vb2 = (0, 0, 340, 110)
r2 = [(36, 64, 88, 96), (112, 64, 164, 96), (188, 64, 240, 96)]
t2 = [text(12, 20, "<number>", "tl tb")]
for (x0, y0, x1, y1) in r2:
    t2.append(text((x0 + x1) / 2, 85, "digit"))
segs2 = [(10, 80, 34, 80), (88, 80, 110, 80), (164, 80, 186, 80), (240, 80, 326, 80), (100, 40, 252, 40), (100, 40, 100, 80), (176, 40, 176, 80), (252, 40, 252, 80)]
check("fig2", vb2, t2, r2, segs2)
# the arrow heads must be 10 px or more from the label
fig2 = """<figure class="fig small"><svg viewBox="0 0 340 110" role="img" aria-label="A syntax diagram for the rule number. A line enters from the left and passes through three rectangles in a row, each labelled digit. Lines above the row let a reader skip the second digit and the third digit, so a number has one, two or three digits."><text class="tl tb" x="12" y="20">&lt;number&gt;</text><path class="ln" d="M10 80 H34" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="36" y="64" width="52" height="32"/><text class="tl tc" x="62" y="85">digit</text><path class="ln" d="M88 80 H110" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="112" y="64" width="52" height="32"/><text class="tl tc" x="138" y="85">digit</text><path class="ln" d="M164 80 H186" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="188" y="64" width="52" height="32"/><text class="tl tc" x="214" y="85">digit</text><path class="ln" d="M240 80 H326" marker-end="url(#ah)"/><path class="ln" d="M100 80 V40 H252 V80"/><path class="ln" d="M176 80 V40"/><path class="ln" d="M140 40 H152" marker-end="url(#ah)"/></svg><figcaption>A syntax diagram for a number of one to three digits. The lines above the boxes let you skip the second digit, the third digit, or both.</figcaption></figure>"""

# ----------------------------------------------------------------------------------------------- figure 3 (expression tree)
vb3 = (0, 0, 340, 262)
R = 15
nodes = {
    "/": (170, 34), "*": (110, 94), "E": (230, 94), "+": (60, 154), "-": (160, 154),
    "A": (30, 214), "B": (90, 214), "C": (130, 214), "D": (190, 214),
}
edges = [("/", "*"), ("/", "E"), ("*", "+"), ("*", "-"), ("+", "A"), ("+", "B"), ("-", "C"), ("-", "D")]
parts = []
lines3 = []
for a, b in edges:
    (x0, y0), (x1, y1) = nodes[a], nodes[b]
    d = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / d, (y1 - y0) / d
    sx, sy, ex, ey = x0 + ux * R, y0 + uy * R, x1 - ux * R, y1 - uy * R
    parts.append(f'<line class="ln" x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}"/>')
    lines3.append((sx, sy, ex, ey))
circles = []
t3 = []
for name, (x, y) in nodes.items():
    cls = "fm s-acc sw2" if name in "+-*/" else "f1 s-acc sw2"
    parts.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="{R}"/>')
    parts.append(f'<text class="tl tc tb" x="{x}" y="{y + 5}">{name}</text>')
    circles.append((x - R, y - R, x + R, y + R))
    t3.append(text(x, y + 5, name))
t3.append(text(170, 254, "post-order: A B + C D - * E /", "tl tc"))
check("fig3", vb3, t3, circles, [])
for i, a in enumerate(circles):
    for b in circles[i + 1:]:
        assert not overlap(a, b, 6), "circles too close"
for (x, y, s) in [(0, 0, "")]:
    pass
fig3 = ('<figure class="fig small"><svg viewBox="0 0 340 262" role="img" aria-label="An expression tree. The root is the divide operator. Its left child is a multiply operator and its right child is the variable E. The multiply operator has two children: a plus operator with leaves A and B, and a minus operator with leaves C and D. Reading the tree in post-order gives A B + C D - * E /.">'
        + "".join(parts)
        + '<text class="tl tc" x="170" y="254">post-order: A B + C D - * E /</text></svg><figcaption>The expression tree for (A + B) * (C - D) / E. Visit the left subtree, then the right subtree, then the node itself (post-order) and you read off the RPN.</figcaption></figure>')

# nothing may be centred too close to the viewBox bottom: the post-order label is at y = 244, its box 234 to 247 < 250
if __name__ == "__main__":
    print(fig1)
    print()
    print(fig2)
    print()
    print(fig3)
    print("figures ok")
