# data/cs_ai_figs.py: draws the hand SVG figures of chapter cs.ai and checks every label position.
# Run: PYTHONIOENCODING=utf-8 py data/cs_ai_figs.py  -> writes scratch/ai_figs.txt (figures pasted into the chapter by hand)
# and prints "figs ok" when no label touches a line, a node or another label.
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cs_ai_algos import *  # noqa: E402,F403

R = 17                 # node radius
CHW = 7.0              # a 13 px label: about 7 px per character, 13 px tall


def box(cx, cy, text, dy=4):
    w = CHW * len(text)
    return (cx - w / 2, cy + dy - 10, cx + w / 2, cy + dy + 3)     # x0, y0, x1, y1


def seg_box_dist(p, q, b):
    x0, y0, x1, y1 = b
    best = 1e9
    n = 80
    for i in range(n + 1):
        t = i / n
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        best = min(best, math.hypot(max(x0 - x, 0, x - x1), max(y0 - y, 0, y - y1)))
    return best


def box_box_gap(a, b):
    return math.hypot(max(a[0] - b[2], b[0] - a[2], 0), max(a[1] - b[3], b[1] - a[3], 0))


def circ_box_dist(c, b):
    return math.hypot(max(b[0] - c[0], 0, c[0] - b[2]), max(b[1] - c[1], 0, c[1] - b[3])) - R


def seg_seg_cross(p1, p2, p3, p4):
    def o(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    d1, d2, d3, d4 = o(p3, p4, p1), o(p3, p4, p2), o(p1, p2, p3), o(p1, p2, p4)
    return d1 * d2 < 0 and d3 * d4 < 0


def graph_figure(title, pos, edges, scale, aria, caption, hvals=None, directed=False, small=True, offsets=None,
                 margin=26, lpad=0):
    P = {n: (x * scale[0], y * scale[1]) for n, (x, y) in pos.items()}
    xs = [p[0] for p in P.values()]
    ys = [p[1] for p in P.values()]
    minx, maxx = min(xs) - R - margin - lpad, max(xs) + R + margin
    miny, maxy = min(ys) - R - margin, max(ys) + R + margin + (14 if hvals else 0)
    P = {n: (x - minx, y - miny) for n, (x, y) in P.items()}
    P = {n: (round(x), round(y)) for n, (x, y) in P.items()}
    W, H = round(maxx - minx), round(maxy - miny)
    out = []
    segs = []
    for a, b, w in edges:
        pa, pb = P[a], P[b]
        d = math.dist(pa, pb)
        ux, uy = (pb[0] - pa[0]) / d, (pb[1] - pa[1]) / d
        if directed:
            x1, y1 = pa[0] + ux * R, pa[1] + uy * R
            x2, y2 = pb[0] - ux * (R + 3), pb[1] - uy * (R + 3)
            out.append(f'<line class="c1 sw2" x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" marker-end="url(#ah)"/>')
        else:
            out.append(f'<line class="ln" x1="{pa[0]}" y1="{pa[1]}" x2="{pb[0]}" y2="{pb[1]}"/>')
        segs.append((a, b, pa, pb))
    labels = []
    for a, b, w in edges:
        pa, pb = P[a], P[b]
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
        if directed:
            d = math.dist(pa, pb)
            nx, ny = -(pb[1] - pa[1]) / d, (pb[0] - pa[0]) / d
            mx, my = mx + nx * 13, my + ny * 13
        if offsets and (a, b) in offsets:
            mx, my = mx + offsets[(a, b)][0], my + offsets[(a, b)][1]
        mx, my = round(mx), round(my)
        t = str(w)
        out.append(f'<text class="tl tc halo" x="{mx}" y="{my + 4}">{t}</text>')
        labels.append(((a, b), box(mx, my, t)))
    for n, (x, y) in P.items():
        out.append(f'<circle class="f1 s-acc sw2" cx="{x}" cy="{y}" r="{R}"/>')
        out.append(f'<text class="tl tc tb" x="{x}" y="{y + 5}">{n}</text>')
    hlabels = []
    if hvals:
        for n, (x, y) in P.items():
            t = f"h = {hvals[n]}"
            half = CHW * len(t) / 2
            cands = {"s": (x, y + R + 15), "n": (x, y - R - 6), "e": (x + R + 4 + half, y + 1), "w": (x - R - 4 - half, y + 1)}
            chosen = None
            for k in ("s", "n", "e", "w"):
                cx, cy = cands[k]
                bx = (cx - half, cy - 10, cx + half, cy + 3)
                ok = bx[0] >= 2 and bx[2] <= W - 2 and bx[3] <= H - 2 and bx[1] >= 2
                ok = ok and all(seg_box_dist(pa, pb, bx) >= 4 for a, b, pa, pb in segs)
                ok = ok and all(box_box_gap(bx, eb) >= 4 for ek, eb in labels)
                ok = ok and all(circ_box_dist(c, bx) >= 4 for m, c in P.items() if m != n)
                ok = ok and all(box_box_gap(bx, ob) >= 4 for ob in hlabels)
                if ok:
                    chosen = (cx, cy, bx)
                    break
            assert chosen, f"no clear place for the h label of {n} in {title}"
            cx, cy, bx = chosen
            hlabels.append(bx)
            out.append(f'<text class="tl tc" x="{cx:.0f}" y="{cy:.0f}">{t}</text>')
    for i, (a, b, pa, pb) in enumerate(segs):
        for (c, d, pc, pd) in segs[i + 1:]:
            if len({a, b, c, d}) == 4:
                assert not seg_seg_cross(pa, pb, pc, pd), f"{title}: edges {a}{b} and {c}{d} cross"
        for m, cpt in P.items():
            if m not in (a, b):
                dmin = min(math.dist(cpt, (pa[0] + (pb[0] - pa[0]) * t / 100, pa[1] + (pb[1] - pa[1]) * t / 100)) for t in range(101))
                assert dmin > R + 6, f"{title}: edge {a}{b} passes node {m}"
    for (ek, eb) in labels:
        for a, b, pa, pb in segs:
            if (a, b) != ek:
                assert seg_box_dist(pa, pb, eb) >= 3, f"{title}: weight label of {ek} touches edge {a}{b}"
        for m, c in P.items():
            assert circ_box_dist(c, eb) >= 3, f"{title}: weight label of {ek} touches node {m}"
        for ek2, eb2 in labels:
            if ek2 != ek:
                assert box_box_gap(eb, eb2) >= 4, f"{title}: weight labels {ek} and {ek2} touch"
        assert eb[0] > 0 and eb[2] < W and eb[1] > 0 and eb[3] < H
    cls = "fig small" if small else "fig"
    html = (f'<figure class="{cls}"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{"".join(out)}</svg>'
            f'<figcaption>{caption}</figcaption></figure>')
    print(f"# {title}: viewBox {W} x {H}, {len(html)} characters")
    return html


def grid_figure(title, cols, rows, walls, order, path, start, goal, aria, caption, dset=(), cell=40):
    ox, oy = 26, 24
    W, H = ox + cols * cell + 12, oy + rows * cell + 12
    out = []
    for c in range(cols):
        out.append(f'<text class="tl tc ts" x="{ox + c * cell + cell // 2}" y="{oy - 8}">{"ABCDEFGH"[c]}</text>')
    for r in range(rows):
        out.append(f'<text class="tl tc ts" x="{ox - 12}" y="{oy + r * cell + cell // 2 + 4}">{r + 1}</text>')
    for r in range(rows):
        for c in range(cols):
            n = "ABCDEFGH"[c] + str(r + 1)
            x, y = ox + c * cell, oy + r * cell
            if n in walls:
                out.append(f'<rect class="fi s-acc sw2" x="{x}" y="{y}" width="{cell}" height="{cell}"/>')
                continue
            cls = "f1" if n in path else ("fm" if (n in order or n in dset) else "fp")
            out.append(f'<rect class="{cls} s-acc sw2" x="{x}" y="{y}" width="{cell}" height="{cell}"/>')
            txt = str(order.index(n) + 1) if n in order else ""
            if n in dset and n not in order:
                txt = "·"
            if n == start:
                txt = ("S " + txt).strip()
            if n == goal:
                txt = ("G " + txt).strip()
            if txt:
                assert CHW * len(txt) < cell - 6, f"{title}: label {txt} too wide for the cell"
                tag = "tl tc tb" if n in path else "tl tc"
                out.append(f'<text class="{tag}" x="{x + cell // 2}" y="{y + cell // 2 + 4}">{txt}</text>')
    html = (f'<figure class="fig small"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">{"".join(out)}</svg>'
            f'<figcaption>{caption}</figcaption></figure>')
    print(f"# {title}: viewBox {W} x {H}, {len(html)} characters")
    return html


def alist(edges):
    return ", ".join(f"{a} to {b} {w}" for a, b, w in edges)


figs = {}

figs["terms"] = graph_figure(
    "terms", dict(A=(0, 1), B=(1, 0), C=(1, 2), D=(2.4, 1)), SMALL_EDGES, (95, 80),
    "A weighted undirected graph with four vertices A, B, C and D and four edges. The edge from A to B has weight 4, A to C has weight 2, B to C has weight 5 and C to D has weight 3.",
    "A weighted graph with four vertices (A to D) and four edges. Each edge carries a weight. The neighbours of C are A, B and D.")

figs["directed"] = graph_figure(
    "directed", dict(S=(0, 0), T=(2, 0), U=(1, 1.6)), [("S", "T", 3), ("T", "U", 2), ("U", "S", 4)], (80, 70),
    "A directed weighted graph with three vertices S, T and U. An arrow goes from S to T with weight 3, an arrow from T to U with weight 2 and an arrow from U to S with weight 4.",
    "A directed graph: each edge is an arrow that can be followed in one direction only. You can go from S to T, but there is no edge from T back to S.",
    directed=True)

town_aria = "A road map drawn as a weighted graph with seven towns A to G. Roads and their lengths in kilometres: " + alist(TOWN_EDGES) + "."
figs["town"] = graph_figure(
    "town", TOWN_POS, TOWN_EDGES, (24, 40), town_aria,
    "The town graph used in the worked examples. The number on each edge is the length of the road in kilometres.", margin=16, lpad=34)
figs["town_h"] = graph_figure(
    "town_h", TOWN_POS, TOWN_EDGES, (24, 40),
    town_aria + " Beside each town is its straight-line distance h to G: A 11, B 8, C 7, D 6, E 4, F 3, G 0.",
    "The town graph again, with the straight-line distance h from each town to G written beside it. These are the h-values A* uses.",
    hvals=TOWN_H, margin=16, lpad=34)

figs["q4"] = graph_figure(
    "q4", Q4_POS, Q4_EDGES, (27, 28),
    "A weighted graph of six depots P to U with road lengths in kilometres: " + alist(Q4_EDGES) + ".",
    "The depot network for exam practice question 4. The numbers are distances in kilometres.")
figs["q5"] = graph_figure(
    "q5", Q5_POS, Q5_EDGES, (27, 28),
    "A weighted graph of six nodes H to N with edge weights: " + alist(Q5_EDGES) + ".",
    "The graph for exam practice question 5. The heuristic values h are in the table above the figure.")

rows, cl, g, p = astar(GRID, manhattan("F5", GRID), "A1", "F5")
path = trace_path(p, "F5")
dset = set(dijkstra(GRID, "A1", "F5")[1])
figs["grid"] = grid_figure(
    "grid", 6, 5, GRID_WALLS, cl, path, "A1", "F5",
    "A grid of 6 columns A to F and 5 rows 1 to 5. Solid cells are walls: B1, B2, B3, B4, D5 and F4. Twelve cells hold the order number in which A star expanded them, from 1 at A1 to 12 at F5, and all twelve are on the shortest path. Nine more cells carry a dot: Dijkstra's algorithm expanded them but A star did not. The shortest path goes down column A to A5, along row 5 to C5, up to C4, along row 4 to E4, then down to E5 and along to F5.",
    "A* on the grid from the start A1 (S) to the goal F5 (G). Solid cells are walls. The numbers give the order in which A* expanded each cell, and all 12 lie on the shortest path (11 moves). A dot marks a cell that Dijkstra's algorithm expanded but A* did not (9 cells). Blank cells were expanded by neither.",
    dset=dset)

pathlib.Path(__file__).resolve().parent.parent.joinpath("scratch", "ai_figs.txt").write_text(
    "\n\n".join(f"<!-- {k} -->\n{v}" for k, v in figs.items()), encoding="utf-8")
print("figs ok")
