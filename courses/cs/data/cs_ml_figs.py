# data/cs_ml_figs.py: draws the hand SVG figures of chapter cs.ml (nested fields, 3-4-2 network, XOR network with
# weights, reinforcement-learning loop) and checks every label position.
# Run: PYTHONIOENCODING=utf-8 py data/cs_ml_figs.py  -> writes scratch/ml_figs.txt (pasted into the chapter by hand).
import math
import pathlib

CHW = 7.0


def box(cx, cy, text, anchor="c", dy=4):
    w = CHW * len(text)
    x0 = cx - w / 2 if anchor == "c" else (cx if anchor == "s" else cx - w)
    return (x0, cy + dy - 10, x0 + w, cy + dy + 3)


def seg_box_dist(p, q, b):
    x0, y0, x1, y1 = b
    best = 1e9
    for i in range(101):
        t = i / 100
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        best = min(best, math.hypot(max(x0 - x, 0, x - x1), max(y0 - y, 0, y - y1)))
    return best


def gap(a, b):
    return math.hypot(max(a[0] - b[2], b[0] - a[2], 0), max(a[1] - b[3], b[1] - a[3], 0))


def circ_gap(c, r, b):
    return math.hypot(max(b[0] - c[0], 0, c[0] - b[2]), max(b[1] - c[1], 0, c[1] - b[3])) - r


def inside(b, W, H):
    return b[0] >= 2 and b[2] <= W - 2 and b[1] >= 2 and b[3] <= H - 2


figs = {}

# ---- 1. nested fields ----------------------------------------------------------------------------------------
W, H = 340, 236
out = ['<ellipse class="fp s-acc sw2" cx="170" cy="118" rx="160" ry="108"/>',
       '<ellipse class="fm s-acc sw2" cx="170" cy="140" rx="118" ry="72"/>',
       '<ellipse class="f1 s-acc sw2" cx="170" cy="158" rx="72" ry="38"/>',
       '<text class="tl tc tb" x="170" y="42">Artificial intelligence</text>',
       '<text class="tl tc tb" x="170" y="88">Machine learning</text>',
       '<text class="tl tc tb" x="170" y="162">Deep learning</text>']
labels = [box(170, 42, "Artificial intelligence"), box(170, 88, "Machine learning"), box(170, 162, "Deep learning")]


def in_ellipse(px, py, cx, cy, rx, ry):
    return ((px - cx) / rx) ** 2 + ((py - cy) / ry) ** 2


for b, (cx, cy, rx, ry) in zip(labels, [(170, 118, 160, 108), (170, 140, 118, 72), (170, 158, 72, 38)]):
    for px in (b[0], b[2]):
        for py in (b[1], b[3]):
            assert in_ellipse(px, py, cx, cy, rx, ry) < 0.9, f"label corner outside its ellipse {b}"
# the AI label must lie outside the machine-learning ellipse, and the ML label outside the deep-learning ellipse
for px in (labels[0][0], labels[0][2]):
    for py in (labels[0][1], labels[0][3]):
        assert in_ellipse(px, py, 170, 140, 118, 72) > 1.1
for px in (labels[1][0], labels[1][2]):
    for py in (labels[1][1], labels[1][3]):
        assert in_ellipse(px, py, 170, 158, 72, 38) > 1.1
figs["nested"] = ('<figure class="fig small"><svg viewBox="0 0 %d %d" role="img" aria-label="Three nested ellipses. The largest is labelled Artificial intelligence. Inside it is Machine learning. Inside that is Deep learning.">%s</svg>'
                  '<figcaption>Deep learning is one kind of machine learning, and machine learning is one way of building artificial intelligence. Each inner idea is part of the one around it.</figcaption></figure>') % (W, H, "".join(out))

# ---- 2. a 3-4-2 network -----------------------------------------------------------------------------------------
W, H, R = 340, 256, 14
layers = [("x", [70, 125, 180], 60), ("h", [45, 100, 155, 210], 170), ("y", [85, 165], 280)]
nodes = []
for tag, ys, x in layers:
    nodes.append([(f"{tag}{i + 1}", x, y) for i, y in enumerate(ys)])
out = []
for a, b in zip(nodes, nodes[1:]):
    for _, x1, y1 in a:
        for _, x2, y2 in b:
            out.append(f'<line class="ln-m thin" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
for layer in nodes:
    for name, x, y in layer:
        out.append(f'<circle class="f1 s-acc sw2" cx="{x}" cy="{y}" r="{R}"/>')
        out.append(f'<text class="tl tc tb" x="{x}" y="{y + 4}">{name}</text>')
        assert CHW * len(name) < 2 * R - 4
for text, x in (("Input layer", 60), ("Hidden layer", 170), ("Output layer", 280)):
    b = box(x, 242, text)
    out.append(f'<text class="tl tc" x="{x}" y="242">{text}</text>')
    assert inside(b, W, H)
    for layer in nodes:
        for name, nx, ny in layer:
            assert circ_gap((nx, ny), R, b) >= 4
# layer labels must not run into each other
bs = [box(x, 242, t) for t, x in (("Input layer", 60), ("Hidden layer", 170), ("Output layer", 280))]
assert all(gap(bs[i], bs[i + 1]) >= 4 for i in range(2))
figs["net342"] = ('<figure class="fig small"><svg viewBox="0 0 %d %d" role="img" aria-label="A neural network with three layers. The input layer has three nodes x1, x2 and x3. The hidden layer has four nodes h1 to h4. The output layer has two nodes y1 and y2. Every node in one layer is joined by a connection to every node in the next layer, which is 12 connections from the input layer to the hidden layer and 8 from the hidden layer to the output layer.">%s</svg>'
                    '<figcaption>A 3-4-2 network: three inputs, four hidden nodes and two outputs. Each of the 20 lines is a connection with its own weight.</figcaption></figure>') % (W, H, "".join(out))

# ---- 3. the XOR network with its weights ------------------------------------------------------------------------
W, H, R = 340, 240, 18
P = {"x1": (50, 70), "x2": (50, 160), "h1": (170, 70), "h2": (170, 160), "o": (290, 115)}
edges = [("x1", "h1", "1", 0.5), ("x1", "h2", "1", 0.2), ("x2", "h1", "1", 0.2), ("x2", "h2", "1", 0.5),
         ("h1", "o", "1", 0.5), ("h2", "o", "−1", 0.5)]
out = []
for a, b, w, t in edges:
    (x1, y1), (x2, y2) = P[a], P[b]
    out.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
lab = []
for a, b, w, t in edges:
    (x1, y1), (x2, y2) = P[a], P[b]
    mx, my = round(x1 + (x2 - x1) * t), round(y1 + (y2 - y1) * t)
    out.append(f'<text class="tl tc halo" x="{mx}" y="{my + 4}">{w}</text>')
    lab.append(((a, b), box(mx, my, w)))
for n, (x, y) in P.items():
    out.append(f'<circle class="f1 s-acc sw2" cx="{x}" cy="{y}" r="{R}"/>')
    out.append(f'<text class="tl tc tb" x="{x}" y="{y + 4}">{n}</text>')
biases = {"h1": ("bias −1", (170, 40)), "h2": ("bias −2", (170, 198)), "o": ("bias −1", (290, 160))}
for n, (t, (bx, by)) in biases.items():
    out.append(f'<text class="tl tc" x="{bx}" y="{by}">{t}</text>')
    lab.append((("bias", n), box(bx, by, t)))
for k, (key, b) in enumerate(lab):
    assert inside(b, W, H), key
    for a, c, w, t in edges:
        if (a, c) != key:
            assert seg_box_dist(P[a], P[c], b) >= 3, f"{key} touches edge {a}{c}"
    for n, (x, y) in P.items():
        assert circ_gap((x, y), R, b) >= 3, f"{key} touches node {n}"
    for key2, b2 in lab[k + 1:]:
        assert gap(b, b2) >= 4, f"{key} and {key2} touch"
figs["xor"] = ('<figure class="fig small"><svg viewBox="0 0 %d %d" role="img" aria-label="A neural network with two inputs x1 and x2, two hidden nodes h1 and h2, and one output node o. Every input is joined to both hidden nodes with weight 1. The hidden node h1 has bias minus 1 and h2 has bias minus 2. The weight from h1 to o is 1 and from h2 to o is minus 1. The output node has bias minus 1.">%s</svg>'
               '<figcaption>A 2-2-1 network with every weight and bias written on it. Each node adds up its weighted inputs and its bias, then outputs 1 if the total is 0 or more, and 0 otherwise.</figcaption></figure>') % (W, H, "".join(out))

# ---- 4. the reinforcement learning loop --------------------------------------------------------------------------
W, H = 320, 210
out = ['<rect class="fm s-acc sw2" x="90" y="16" width="140" height="42"/>',
       '<text class="tl tc tb" x="160" y="42">Agent</text>',
       '<rect class="fm s-acc sw2" x="90" y="150" width="140" height="42"/>',
       '<text class="tl tc tb" x="160" y="176">Environment</text>',
       '<line class="c1 sw2" x1="118" y1="62" x2="118" y2="146" marker-end="url(#ah)"/>',
       '<text class="tl te" x="108" y="108">action</text>',
       '<line class="c2 sw2" x1="202" y1="146" x2="202" y2="62" marker-end="url(#ah)"/>',
       '<text class="tl" x="212" y="98">reward</text>',
       '<text class="tl" x="212" y="116">new state</text>']
b1, b2, b3 = box(108, 108, "action", "e"), box(212, 98, "reward", "s"), box(212, 116, "new state", "s")
for b in (b1, b2, b3):
    assert inside(b, W, H)
    assert b[2] <= 118 - 4 or b[0] >= 202 + 4, b
assert gap(b2, b3) >= 4
figs["rl"] = ('<figure class="fig small"><svg viewBox="0 0 %d %d" role="img" aria-label="A loop between an agent and its environment. An arrow labelled action points down from the agent to the environment. An arrow labelled reward and new state points up from the environment to the agent.">%s</svg>'
              '<figcaption>The reinforcement learning loop: the agent acts, and the environment answers with a reward and a new state.</figcaption></figure>') % (W, H, "".join(out))

pathlib.Path(__file__).resolve().parent.parent.joinpath("scratch", "ml_figs.txt").write_text(
    "\n\n".join(f"<!-- {k} -->\n{v}" for k, v in figs.items()), encoding="utf-8")
for k, v in figs.items():
    print(k, len(v))
print("figs ok")
