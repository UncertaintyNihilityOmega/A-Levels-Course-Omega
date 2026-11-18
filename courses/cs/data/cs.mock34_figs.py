# data/cs.mock34_figs.py: the weighted graph of cs.mock.p3 Question 9 (Dijkstra), with its checks.
# Run: py data/cs.mock34_figs.py -> prints "ok" and writes data/cs.mock34_figs.txt (one "### name" block per figure).
# Checks: every label box is at least 4 px from every line, node and other label; no two edges cross.
import heapq
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
R = 16
CHW = 7.0
NODES = {"P": (38, 122), "Q": (118, 44), "R": (118, 200), "S": (222, 104), "T": (252, 202), "U": (330, 136)}
EDGES = [("P", "Q", 4), ("P", "R", 2), ("Q", "R", 1), ("Q", "S", 5), ("R", "S", 8), ("R", "T", 10),
         ("S", "T", 2), ("S", "U", 6), ("T", "U", 3)]
# label centre offsets from the edge midpoint (dx, dy), chosen by hand and verified below
OFF = {("P", "Q"): (-12, -10), ("P", "R"): (-12, 12), ("Q", "R"): (-14, 4), ("Q", "S"): (6, -12),
       ("R", "S"): (-12, 6), ("R", "T"): (0, 16), ("S", "T"): (14, 4), ("S", "U"): (6, -12), ("T", "U"): (14, 8)}


def dijkstra(src):
    dist = {n: 1e9 for n in NODES}
    dist[src] = 0
    prev = {}
    order = []
    heap = [(0, src)]
    done = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in done:
            continue
        done.add(u)
        order.append((u, d))
        for a, b, w in EDGES:
            for x, y in ((a, b), (b, a)):
                if x == u and d + w < dist[y]:
                    dist[y] = d + w
                    prev[y] = u
                    heapq.heappush(heap, (dist[y], y))
    return dist, prev, order


def box(cx, cy, text):
    w = CHW * len(text)
    return (cx - w / 2, cy - 6, cx + w / 2, cy + 7)        # baseline cy + 4: top about cy - 6


def seg_box_dist(p, q, b):
    x0, y0, x1, y1 = b
    best = 1e9
    for i in range(201):
        t = i / 200
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        best = min(best, math.hypot(max(x0 - x, 0, x - x1), max(y0 - y, 0, y - y1)))
    return best


def circ_box_dist(c, b):
    return math.hypot(max(b[0] - c[0], 0, c[0] - b[2]), max(b[1] - c[1], 0, c[1] - b[3])) - R


def box_gap(a, b):
    return math.hypot(max(a[0] - b[2], b[0] - a[2], 0), max(a[1] - b[3], b[1] - a[3], 0))


def cross(p1, p2, p3, p4):
    def o(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return o(p3, p4, p1) * o(p3, p4, p2) < 0 and o(p1, p2, p3) * o(p1, p2, p4) < 0


def edge_ends(a, b):
    (x1, y1), (x2, y2) = NODES[a], NODES[b]
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    return (x1 + ux * R, y1 + uy * R), (x2 - ux * R, y2 - uy * R)


def choose_offsets():
    """for each edge, the closest label position (perpendicular offset, then a slide along the edge) that keeps
    every clearance; the result is deterministic, and build() re-checks it."""
    chosen = {}
    for a, b, w in EDGES:
        (x1, y1), (x2, y2) = NODES[a], NODES[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        nx, ny = -uy, ux
        best = None
        for off in range(10, 30):
            for side in (1, -1):
                for slide in (0, -14, 14, -28, 28):
                    cx, cy = mx + side * nx * off + ux * slide, my + side * ny * off + uy * slide
                    bx = box(cx, cy, str(w))
                    ok = all(seg_box_dist(*edge_ends(c, e), bx) >= 5 for c, e, _ in EDGES)
                    ok = ok and all(circ_box_dist(NODES[n], bx) >= 5 for n in NODES)
                    ok = ok and all(box_gap(bx, o) >= 5 for o in chosen.values())
                    ok = ok and 4 <= bx[0] and bx[2] <= 356 and 4 <= bx[1] and bx[3] <= 242
                    if ok and (best is None or off + abs(slide) / 4 < best[0]):
                        best = (off + abs(slide) / 4, (round(cx - mx, 1), round(cy - my, 1)), bx)
            if best:
                break
        assert best, f"no place for label {a}{b}"
        OFF[(a, b)] = best[1]
        chosen[(a, b)] = best[2]
    return chosen


def build():
    choose_offsets()
    labels = {}
    for a, b, w in EDGES:
        (x1, y1), (x2, y2) = NODES[a], NODES[b]
        dx, dy = OFF[(a, b)]
        labels[(a, b)] = box((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, str(w))
    for (a, b), bx in labels.items():
        for c, d, _ in EDGES:
            p, q = edge_ends(c, d)
            gap = seg_box_dist(p, q, bx)
            assert gap >= 4, f"label {a}{b} is {gap:.1f} px from edge {c}{d}"
        for n, c in NODES.items():
            assert circ_box_dist(c, bx) >= 4, f"label {a}{b} touches node {n}"
        for (a2, b2), bx2 in labels.items():
            if (a2, b2) != (a, b):
                assert box_gap(bx, bx2) >= 4, f"labels {a}{b} and {a2}{b2} touch"
        assert bx[0] >= 4 and bx[2] <= 356 and bx[1] >= 4 and bx[3] <= 246, f"label {a}{b} outside the viewBox"
    for i, (a, b, _) in enumerate(EDGES):
        for c, d, _ in EDGES[i + 1:]:
            if len({a, b, c, d}) == 4:
                assert not cross(NODES[a], NODES[b], NODES[c], NODES[d]), f"edges {a}{b} and {c}{d} cross"
    for n, (x, y) in NODES.items():
        for a, b, _ in EDGES:
            if n not in (a, b):
                p, q = edge_ends(a, b)
                # distance from node centre to the segment
                best = min(math.hypot(p[0] + (q[0] - p[0]) * t / 200 - x, p[1] + (q[1] - p[1]) * t / 200 - y) for t in range(201))
                assert best >= R + 6, f"edge {a}{b} passes node {n}"
        assert R <= x <= 360 - R and R <= y <= 246 - R
    parts = []
    for a, b, w in EDGES:
        (x1, y1), (x2, y2) = NODES[a], NODES[b]
        parts.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    for n, (x, y) in NODES.items():
        parts.append(f'<circle class="f1 s-acc sw2" cx="{x}" cy="{y}" r="{R}"/><text class="tl tb tc" x="{x}" y="{y + 4}">{n}</text>')
    for a, b, w in EDGES:
        (x1, y1), (x2, y2) = NODES[a], NODES[b]
        dx, dy = OFF[(a, b)]
        parts.append(f'<text class="tl tc halo" x="{(x1 + x2) / 2 + dx:g}" y="{(y1 + y2) / 2 + dy + 4:g}">{w}</text>')
    aria = ("A graph with six labelled points P, Q, R, S, T and U joined by nine roads. The lengths in kilometres are: "
            "P to Q 4, P to R 2, Q to R 1, Q to S 5, R to S 8, R to T 10, S to T 2, S to U 6 and T to U 3.")
    return (f'<figure class="fig small"><svg viewBox="0 0 360 246" role="img" aria-label="{aria}">' + "".join(parts) +
            '</svg><figcaption>The road network for Question 9. Each number is the length of the road in kilometres.</figcaption></figure>')


if __name__ == "__main__":
    dist, prev, order = dijkstra("P")
    assert dist == {"P": 0, "R": 2, "Q": 3, "S": 8, "T": 10, "U": 13}, dist
    assert [n for n, _ in order] == ["P", "R", "Q", "S", "T", "U"], order
    path, n = ["U"], "U"
    while n != "P":
        n = prev[n]
        path.append(n)
    assert path[::-1] == ["P", "R", "Q", "S", "T", "U"]
    svg = build()
    (HERE / "cs.mock34_figs.txt").write_text("### graph\n" + svg + "\n", encoding="utf-8", newline="\n")
    print("ok")
