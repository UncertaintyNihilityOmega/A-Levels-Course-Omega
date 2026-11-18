# Generates the binary search tree and graph figures for cs.adts (prints the SVG fragments; paste into the chapter).
import math
R = 18
# ---- binary search tree: insertion order 27, 14, 35, 10, 31, 19, 42 -> in-order 10 14 19 27 31 35 42
nodes = {27: (170, 34), 14: (90, 100), 35: (250, 100), 10: (50, 166), 19: (130, 166), 31: (210, 166), 42: (290, 166)}
edges = [(27, 14), (27, 35), (14, 10), (14, 19), (35, 31), (35, 42)]
parts = []
for a, b in edges:
    (x1, y1), (x2, y2) = nodes[a], nodes[b]
    parts.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
for v, (x, y) in nodes.items():
    cls = "f1" if v == 27 else "fm"
    parts.append(f'<circle class="{cls} s-acc sw2" cx="{x}" cy="{y}" r="{R}"/>')
    parts.append(f'<text class="tl tc" x="{x}" y="{y + 5}">{v}</text>')
parts.append('<text class="tl" x="196" y="24">root</text>')
parts.append('<text class="tl tc" x="50" y="204">leaf</text>')
tree_h = 214
tree = (f'<figure class="fig small"><svg viewBox="0 0 340 {tree_h}" role="img" aria-label="A binary search tree of seven nodes. The root holds 27. Its left child holds 14, with children 10 and 19. Its right child holds 35, with children 31 and 42. Every value in a left subtree is smaller than its parent and every value in a right subtree is larger. The root and one leaf, 10, are labelled.">'
        + "".join(parts) +
        '</svg><figcaption>A binary search tree. The root is 27. The nodes 14, 10 and 19 form the left subtree of the root, and 35, 31 and 42 form its right subtree. Leaves (10, 19, 31, 42) have no children.</figcaption></figure>')
# label overlap checks: "root" box x 196..224, y 14..27 vs circle (170,34) r 18 -> circle spans x 152..188
assert 196 > 170 + R + 4
# leaf label y 194..207, circle bottom 166+18 = 184 -> 10 px clear
assert 204 - 10 - (166 + R) >= 4
assert max(y for _, y in nodes.values()) + R + 4 < tree_h
print(tree)
print()
# ---- weighted graph
g = {"A": (50, 95), "B": (140, 35), "C": (140, 155), "D": (235, 95), "E": (310, 95)}
ge = [("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "D", 8), ("D", "E", 3)]
parts = []
for a, b, w in ge:
    (x1, y1), (x2, y2) = g[a], g[b]
    parts.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
for a, b, w in ge:
    (x1, y1), (x2, y2) = g[a], g[b]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    parts.append(f'<text class="tl tc" x="{mx:g}" y="{my + 5:g}">{w}</text>')  # NOTE: the chapter's labels were moved off the lines by hand (see chapters/cs.adts.md)
for v, (x, y) in g.items():
    parts.append(f'<circle class="fm s-acc sw2" cx="{x}" cy="{y}" r="16"/>')
    parts.append(f'<text class="tl tc tb" x="{x}" y="{y + 5}">{v}</text>')
# weight labels must be at least 20 px from every circle centre
for a, b, w in ge:
    (x1, y1), (x2, y2) = g[a], g[b]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    for v, (x, y) in g.items():
        assert math.hypot(mx - x, my - y) >= 16 + 12, (a, b, v)
graph = ('<figure class="fig small"><svg viewBox="0 0 340 190" role="img" aria-label="A weighted undirected graph with five vertices A, B, C, D and E and six edges. A to B has weight 4. A to C has weight 2. B to C has weight 1. B to D has weight 5. C to D has weight 8. D to E has weight 3.">'
         + "".join(parts) +
         '</svg><figcaption>A weighted graph: five vertices (A to E) and six edges. The number on each edge is its weight, for example the distance in kilometres between two towns.</figcaption></figure>')
print(graph)
