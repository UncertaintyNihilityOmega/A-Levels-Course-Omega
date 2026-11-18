# data/cs_ai_algos.py: Dijkstra and A* exactly as chapter cs.ai applies them by hand, plus every graph the chapter uses.
# Used by checks/cs.ai.py and by data/cs_ai_tables.py (which prints the Markdown tables pasted into the chapter).
# Tie-break rule (stated in the chapter): when two nodes have the same value, take the one that comes first alphabetically.
import math

INF = math.inf


def undirected(edges):
    adj = {}
    for a, b, w in edges:
        adj.setdefault(a, {})[b] = w
        adj.setdefault(b, {})[a] = w
    return adj


def directed(edges, nodes=()):
    adj = {n: {} for n in nodes}
    for a, b, w in edges:
        adj.setdefault(a, {})[b] = w
        adj.setdefault(b, {})
    return adj


def dijkstra(adj, start, goal=None):
    """Returns rows, visited order, dist, prev. A row is (visited node or None, {node: (dist, prev)} of the cells that
    changed in this step). Stops when the goal is selected (visited), or when no node can be reached."""
    dist = {n: INF for n in adj}
    prev = {n: None for n in adj}
    dist[start] = 0
    visited = []
    rows = [(None, {start: (0, None)})]
    while True:
        cand = [n for n in adj if n not in visited and dist[n] < INF]
        if not cand:
            break
        u = min(cand, key=lambda n: (dist[n], n))
        visited.append(u)
        changed = {}
        if u != goal:
            for v, w in sorted(adj[u].items()):
                if v not in visited and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    changed[v] = (dist[v], u)
        rows.append((u, changed))
        if u == goal:
            break
    return rows, visited, dist, prev


def trace_path(prev, goal):
    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = prev[n]
    return path[::-1]


def astar(adj, h, start, goal):
    """Returns rows, closed (expansion order), g, prev. A row is (expanded node, open list after, closed list after) where
    the open list is [(node, g, h, f)] sorted by (f, node)."""
    g = {start: 0}
    prev = {start: None}
    openl = {start}
    closed = []
    rows = [(None, [(start, 0, h[start], h[start])], [])]
    while openl:
        u = min(openl, key=lambda n: (g[n] + h[n], n))
        openl.remove(u)
        closed.append(u)
        if u != goal:
            for v, w in sorted(adj[u].items()):
                if v in closed:
                    continue
                if v not in g or g[u] + w < g[v]:
                    g[v] = g[u] + w
                    prev[v] = u
                    openl.add(v)
        snap = sorted(((n, g[n], h[n], g[n] + h[n]) for n in openl), key=lambda t: (t[3], t[0]))
        rows.append((u, snap, list(closed)))
        if u == goal:
            break
    return rows, closed, g, prev


def ties_in(rows_kind, rows):
    """Number of steps where the choice needed the alphabetical rule (two candidates tied)."""
    return None


def is_consistent(adj, h):
    return all(h[u] <= w + h[v] for u in adj for v, w in adj[u].items())


def is_admissible(adj, h, goal):
    d, *_ = dijkstra_all(adj, goal)
    return all(h[n] <= d[n] for n in adj if d[n] < INF)


def dijkstra_all(adj, start):
    rows, visited, dist, prev = dijkstra(adj, start, None)
    return dist, prev


def reverse(adj):
    rev = {n: {} for n in adj}
    for a in adj:
        for b, w in adj[a].items():
            rev[b][a] = w
    return rev


def all_paths_cost(adj, start, goal):
    out = []

    def dfs(n, seen, c, p):
        if n == goal:
            out.append((c, p))
            return
        for v, w in adj[n].items():
            if v not in seen:
                dfs(v, seen | {v}, c + w, p + [v])

    dfs(start, {start}, 0, [start])
    return sorted(out)


# ------------------------------------------------------------------ the chapter's graphs
# Coordinates of the town (kilometres), used for the figure and for the straight-line distances in the widget.
TOWN_POS = dict(A=(0, 4), B=(3, 7), C=(4, 1), D=(5, 5), E=(8, 7), F=(8, 2), G=(11, 4))
TOWN_EDGES = [("A", "B", 5), ("A", "C", 9), ("A", "D", 6), ("B", "D", 3), ("B", "E", 6), ("C", "D", 9),
              ("C", "F", 7), ("D", "E", 4), ("D", "F", 8), ("E", "G", 5), ("F", "G", 8)]
TOWN = undirected(TOWN_EDGES)
TOWN_H = {"A": 11, "B": 8, "C": 7, "D": 6, "E": 4, "F": 3, "G": 0}   # straight-line distance to G, whole km, rounded down


def straight_line(pos, goal):
    return {n: int(math.dist(pos[n], pos[goal])) for n in pos}


# Exam question 4 (Dijkstra, six depots P to U) and exam question 5 (A*, six nodes H to N).
Q4_POS = dict(P=(0, 3), Q=(3, 6), R=(4, 1), S=(6, 4), T=(9, 6), U=(10, 2))
Q4_EDGES = [("P", "Q", 5), ("P", "R", 8), ("P", "S", 9), ("Q", "S", 5), ("Q", "T", 6), ("R", "S", 5),
            ("R", "U", 9), ("S", "T", 8), ("S", "U", 9), ("T", "U", 5)]
Q4 = undirected(Q4_EDGES)
Q5_POS = dict(H=(0, 2), J=(3, 5), K=(4, 0), L=(6, 3), M=(9, 5), N=(10, 1))
Q5_EDGES = [("H", "J", 7), ("H", "K", 5), ("H", "L", 8), ("J", "L", 8), ("J", "M", 6), ("K", "L", 5),
            ("K", "N", 9), ("L", "M", 4), ("L", "N", 5), ("M", "N", 8)]
Q5 = undirected(Q5_EDGES)
Q5_H = {"H": 10, "J": 8, "K": 6, "L": 4, "M": 4, "N": 0}

# The small graph used for terms, the matrix and the list.
SMALL_EDGES = [("A", "B", 4), ("A", "C", 2), ("B", "C", 5), ("C", "D", 3)]
SMALL = undirected(SMALL_EDGES)

# Why Dijkstra must not stop when the target first gets a distance.
STOP_EDGES = [("S", "T", 10), ("S", "U", 3), ("U", "V", 2), ("V", "T", 2)]
STOP = undirected(STOP_EDGES)

# Stretch: a heuristic that overestimates.
OVER_EDGES = [("S", "A", 1), ("A", "G", 6), ("S", "B", 4), ("B", "G", 4)]
OVER = undirected(OVER_EDGES)
OVER_H = {"S": 6, "A": 20, "B": 4, "G": 0}


def grid_graph(cols, rows, walls):
    letters = "ABCDEFGH"

    def name(c, r):
        return letters[c] + str(r + 1)

    cells = {(c, r) for c in range(cols) for r in range(rows) if name(c, r) not in walls}
    adj = {name(c, r): {} for c, r in cells}
    for c, r in cells:
        for dc, dr in ((1, 0), (0, 1)):
            if (c + dc, r + dr) in cells:
                adj[name(c, r)][name(c + dc, r + dr)] = 1
                adj[name(c + dc, r + dr)][name(c, r)] = 1
    return adj


def manhattan(goal, nodes):
    gc, gr = "ABCDEFGH".index(goal[0]), int(goal[1:])
    return {n: abs("ABCDEFGH".index(n[0]) - gc) + abs(int(n[1:]) - gr) for n in nodes}


GRID_WALLS = {"B1", "B2", "B3", "B4", "D5", "F4"}      # worked example: 6 columns A-F, 5 rows 1-5, from A1 to F5
GRID = grid_graph(6, 5, GRID_WALLS)
EXAM_GRID_WALLS = {"A3", "B1", "C3", "D2"}             # exam question 6: 5 columns A-E, 4 rows 1-4, from A1 to E4
EXAM_GRID = grid_graph(5, 4, EXAM_GRID_WALLS)
WIDGET_GRID_WALLS = {"B1", "B2", "B3", "B4", "C6", "D2", "D5", "F4"}   # the cs-path widget: 6 x 6
WIDGET_GRID = grid_graph(6, 6, WIDGET_GRID_WALLS)


# ------------------------------------------------------------------ Markdown tables exactly as the chapter prints them
def dijkstra_md(rows, nodes):
    out = ["| Step | Visit | " + " | ".join(nodes) + " |", "|---|---|" + "---|" * len(nodes)]
    for i, (u, changed) in enumerate(rows):
        cells = []
        for n in nodes:
            if u is None:
                cells.append("0" if n in changed else "∞")
            elif n in changed:
                cells.append(f"{changed[n][0]} {changed[n][1]}")
            else:
                cells.append("")
        out.append(f"| {i} | {u if u else ''} | " + " | ".join(cells) + " |")
    return "\n".join(out)


def final_md(nodes, dist, prev, visited):
    out = ["| Node | Shortest distance | Previous node | Visited in order |", "|---|---|---|---|"]
    for n in nodes:
        d = dist[n] if dist[n] < INF else "∞"
        p = prev[n] if prev[n] else "none"
        k = visited.index(n) + 1 if n in visited else ""
        out.append(f"| {n} | {d} | {p} | {k} |")
    return "\n".join(out)


def astar_md(rows):
    out = ["| Step | Expand | Open list after the step (node: g + h = f) | Closed list |", "|---|---|---|---|"]
    for i, (u, snap, closed) in enumerate(rows):
        op = "; ".join(f"{n} {g}+{h}={f}" for n, g, h, f in snap) if snap else "empty"
        out.append(f"| {i} | {u if u else ''} | {op} | {' '.join(closed) if closed else 'empty'} |")
    return "\n".join(out)


def astar_compact_md(rows):
    out = ["| Step | Expand | g | h | f | Added to or updated in the open list (node: g + h = f) |", "|---|---|---|---|---|---|"]
    prev_open = {}
    for i, (u, snap, closed) in enumerate(rows):
        if u is None:
            n, g, h, f = snap[0]
            out.append(f"| 0 | | | | | {n} {g}+{h}={f} |")
            prev_open = {n: g for n, g, h, f in snap}
            continue
        # the node expanded was in the previous open list: find its numbers from the previous row
        pg, ph = rows[i - 1][1], None
        info = next(t for t in rows[i - 1][1] if t[0] == u)
        news = [t for t in snap if t[0] not in prev_open or prev_open[t[0]] != t[1]]
        txt = "; ".join(f"{n} {g}+{h}={f}" for n, g, h, f in news) if news else "none"
        out.append(f"| {i} | {u} | {info[1]} | {info[2]} | {info[3]} | {txt} |")
        prev_open = {n: g for n, g, h, f in snap}
    return "\n".join(out)
