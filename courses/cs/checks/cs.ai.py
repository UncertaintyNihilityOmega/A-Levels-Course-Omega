# checks/cs.ai.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (Dijkstra and A* tables, counts, paths, costs, matrices, quiz numbers).
import contextlib
import io
import math
import os
import pathlib
import re
import sys
import tempfile

CHAPTER_ID = "cs.ai"

# ---------------------------------------------------------------------------------------------
# Helper (copy unchanged into every checks file of this course; only CHAPTER_ID and INPUTS change)
# ---------------------------------------------------------------------------------------------
CHAPTER = pathlib.Path(__file__).resolve().parent.parent / "chapters" / f"{CHAPTER_ID}.md"
TEXT = CHAPTER.read_text(encoding="utf-8")
FENCES = list(re.finditer(r"^```(\w+)\n(.*?)^```", TEXT, re.S | re.M))


def run_python_blocks(inputs):
    """Run each ```python block in a fresh namespace inside a temporary folder.
    inputs: list of (text found in the block, [values the user types]). Typed values are echoed after
    the prompt, as a console shows them. If the next fence after a python block is ```output, the
    printed text must match it exactly (trailing spaces ignored)."""
    ran = 0
    with tempfile.TemporaryDirectory() as tmp:
        old = os.getcwd()
        os.chdir(tmp)
        try:
            for i, f in enumerate(FENCES):
                if f.group(1) != "python":
                    continue
                code = f.group(2)
                ran += 1
                typed = list(next((v for key, v in inputs if key in code), []))
                out = io.StringIO()

                def fake_input(prompt=""):
                    assert typed, f"python block {ran}: input() called but no typed value left"
                    value = typed.pop(0)
                    out.write(str(prompt) + value + "\n")
                    return value

                namespace = {"__name__": "__main__", "input": fake_input}
                with contextlib.redirect_stdout(out):
                    exec(compile(code, f"{CHAPTER_ID} python block {ran}", "exec"), namespace)
                assert not typed, f"python block {ran}: typed values not used: {typed}"
                nxt = FENCES[i + 1] if i + 1 < len(FENCES) else None
                if nxt is not None and nxt.group(1) == "output":
                    got = [line.rstrip() for line in out.getvalue().rstrip("\n").split("\n")]
                    want = [line.rstrip() for line in nxt.group(2).rstrip("\n").split("\n")]
                    assert got == want, f"python block {ran}: printed {got}, chapter shows {want}"
        finally:
            os.chdir(old)
    return ran


PAIRS = [("IF", "ENDIF"), ("WHILE", "ENDWHILE"), ("FOR", "NEXT"), ("REPEAT", "UNTIL"),
         ("CASE OF", "ENDCASE"), ("PROCEDURE", "ENDPROCEDURE"), ("FUNCTION", "ENDFUNCTION"),
         ("CLASS", "ENDCLASS")]


def lint_pseudocode_blocks():
    """Light checks on ```pseudocode blocks: Cambridge symbols, no Python syntax, balanced
    structures (blocks that are deliberate fragments contain a line '...' and skip the balance test)."""
    n = 0
    for f in FENCES:
        if f.group(1) != "pseudocode":
            continue
        n += 1
        code = f.group(2)
        lines = [re.sub(r"^\s*\d+\s{2,}", "", ln).split("//")[0] for ln in code.split("\n")]
        body = "\n".join(lines)
        for bad in ("<-", "==", "!=", "print(", "elif", "range(", "True", "False", "\t"):
            assert bad not in body, f"pseudocode block {n}: contains {bad!r}"
        if any(ln.strip() == "..." for ln in lines):
            continue
        words = [ln.strip() for ln in lines]
        for start, end in PAIRS:
            if start == "FOR":
                opened = sum(1 for w in words if re.match(r"FOR \w+ ←", w))
            elif start == "CASE OF":
                opened = sum(1 for w in words if w.startswith("CASE OF"))
            elif start in ("PROCEDURE", "FUNCTION"):
                opened = sum(1 for w in words if re.match(rf"(PUBLIC |PRIVATE )?{start} ", w))
            else:
                opened = sum(1 for w in words if re.match(rf"{start}\b", w))
            closed = sum(1 for w in words if re.match(rf"{end}\b", w))
            # a block of four lines or fewer may be a fragment (for example a corrected swap)
            assert opened == closed or len(words) <= 4, f"pseudocode block {n}: {start}/{end} {opened}/{closed}"
        types = sum(1 for w in words if re.match(r"TYPE \w+\s*$", w))
        assert types == sum(1 for w in words if w.startswith("ENDTYPE")), f"pseudocode block {n}: TYPE/ENDTYPE"
    return n


INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 2, f"expected 2 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 0

# ---------------------------------------------------------------------------------------------
# The algorithms and graphs (data/cs_ai_algos.py): every table in the chapter is compared with their output
# ---------------------------------------------------------------------------------------------
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "data"))
from cs_ai_algos import *  # noqa: E402,F403


def has(block, label):
    assert block in TEXT, f"{label}: table in the chapter differs from the computed one:\n{block}"


def count_in_text(block):
    return TEXT.count(block)


# --- the small graph: matrix, list, dictionary --------------------------------------------------
nodes = sorted(SMALL)
matrix = [[SMALL[a].get(b, 0) for b in nodes] for a in nodes]
assert matrix == [[0, 4, 2, 0], [4, 0, 5, 0], [2, 5, 0, 3], [0, 0, 3, 0]]
assert all(matrix[i][j] == matrix[j][i] for i in range(4) for j in range(4))
assert len(SMALL_EDGES) == 4 and sorted(SMALL["C"]) == ["A", "B", "D"]
assert 4 + 5 + 3 == 12 and 2 + 3 == 5 and 3 + 2 == 5          # paths A-B-C-D, A-C-D; S-T-U
assert min(c for c, p in all_paths_cost(SMALL, "A", "D")) == 5
assert all_paths_cost(SMALL, "A", "D")[0][1] == ["A", "C", "D"]
D3 = directed([("S", "T", 3), ("T", "U", 2), ("U", "S", 4)])
d_su = dijkstra(D3, "S", "U")[2]["U"]
d_us = dijkstra(D3, "U", "S")[2]["S"]
assert (d_su, d_us) == (5, 4)
assert "T" not in D3["U"] and "S" not in D3["T"]
assert math.factorial(9) // 2 == 181440                         # reachable arrangements of the 8-puzzle

# --- the town: Dijkstra ------------------------------------------------------------------------
assert len(TOWN_EDGES) == 11 and len(TOWN) == 7
rows, vis, dist, prev = dijkstra(TOWN, "A", "G")
tn = sorted(TOWN)
has(dijkstra_md(rows, tn), "town dijkstra")
has(final_md(tn, dist, prev, vis), "town final")
assert vis == ["A", "B", "D", "C", "E", "F", "G"] and len(vis) == 7
assert trace_path(prev, "G") == ["A", "D", "E", "G"] and dist["G"] == 15
assert 6 + 4 + 5 == 15 and 5 + 6 + 5 == 16
assert 5 + 3 == 8 and 5 + 6 == 11 and 6 + 4 == 10 and 6 + 8 == 14 and 6 + 9 == 15 and 9 + 7 == 16 and 10 + 5 == 15 and 14 + 8 == 22
paths = all_paths_cost(TOWN, "A", "G")
assert paths[0] == (15, ["A", "D", "E", "G"]) and paths[1][0] > 15
# first road out of A that looks cheapest (A-B, 5) is not on the best route
assert min(TOWN["A"], key=lambda n: TOWN["A"][n]) == "B" and "B" not in trace_path(prev, "G")

# --- the town: A* --------------------------------------------------------------------------------
assert TOWN_H == straight_line(TOWN_POS, "G")
for goal in TOWN_POS:
    h = straight_line(TOWN_POS, goal)
    assert is_consistent(TOWN, h), goal
assert is_admissible(TOWN, TOWN_H, "G")
assert dijkstra(TOWN, "D", None)[2]["G"] == 9 and TOWN_H["D"] == 6
assert all(TOWN_H[n] <= dijkstra(TOWN, n, None)[2]["G"] for n in TOWN)
arows, closed, g, p = astar(TOWN, TOWN_H, "A", "G")
has(astar_md(arows), "town astar")
assert closed == ["A", "D", "B", "E", "G"] and len(closed) == 5
assert trace_path(p, "G") == ["A", "D", "E", "G"] and g["G"] == 15
assert set(TOWN) - set(closed) == {"C", "F"}
# the figure's h labels and the heuristic in the chapter
assert [TOWN_H[n] for n in "ABCDEFG"] == [11, 8, 7, 6, 4, 3, 0]
assert 6 + 4 == 10 and 10 + 4 == 14 and 6 + 8 == 14 and 14 + 3 == 17 and 12 + 4 + 4 == 20
# the wrong-method warning: base on f instead of g
assert (6 + 6) + 4 + 4 == 20 and 6 + 4 + 4 == 14

# Dijkstra is A* with h = 0: same expansions as Dijkstra, and the Python program in the chapter agrees
zero = {n: 0 for n in TOWN}
zrows, zclosed, zg, zp = astar(TOWN, zero, "A", "G")
assert zclosed == vis and zg["G"] == 15

# the two algorithms agree on the cost for every start and goal pair of the town
for s in TOWN:
    for goal in TOWN:
        d_all = dijkstra(TOWN, s, None)[2]
        _, _, gg, _ = astar(TOWN, straight_line(TOWN_POS, goal), s, goal)
        assert gg[goal] == d_all[goal], (s, goal)

# --- the stop-rule warning -------------------------------------------------------------------------
srows, svis, sdist, sprev = dijkstra(STOP, "S", "T")
has(dijkstra_md(srows, sorted(STOP)), "stop")
assert svis == ["S", "U", "V", "T"] and sdist["T"] == 7 and trace_path(sprev, "T") == ["S", "U", "V", "T"]
assert 3 + 2 + 2 == 7

# --- the grid ----------------------------------------------------------------------------------------
assert len(GRID) == 24 and 6 * 5 - len(GRID_WALLS) == 24
gh = manhattan("F5", GRID)
assert gh["A1"] == 9 and gh["C4"] == 4 and gh["C5"] == 3 and gh["D4"] == 3 and gh["E4"] == 2
assert is_consistent(GRID, gh) and is_admissible(GRID, gh, "F5")
grows, gclosed, gg, gp = astar(GRID, gh, "A1", "F5")
has(astar_compact_md(grows), "grid astar")
gpath = trace_path(gp, "F5")
assert gpath == ["A1", "A2", "A3", "A4", "A5", "B5", "C5", "C4", "D4", "E4", "E5", "F5"]
assert len(gclosed) == 12 and set(gclosed) == set(gpath) and gg["F5"] == 11
drows, dvis, ddist, dprev = dijkstra(GRID, "A1", "F5")
assert len(dvis) == 21 and ddist["F5"] == 11 and len(set(dvis) - set(gclosed)) == 9
assert set(GRID) - set(dvis) == {"E1", "F1", "F2"}
# Manhattan examples
assert manhattan("F5", {"C2": 0})["C2"] == 6 and manhattan("B1", {"D4": 0})["D4"] == 5 and manhattan("A4", {"D2": 0})["D2"] == 5
assert 7 + 4 == 11 and 6 + 3 == 9

# --- exam question 4 ------------------------------------------------------------------------------------
assert len(Q4_EDGES) == 10
qrows, qvis, qdist, qprev = dijkstra(Q4, "P", "U")
has(dijkstra_md(qrows, sorted(Q4)), "q4")
assert qvis == list("PQRSTU") and qdist["U"] == 16 and trace_path(qprev, "U") == ["P", "Q", "T", "U"]
assert 5 + 5 == 10 > 9 and 11 + 8 == 19 and 11 + 6 == 17 and 9 + 8 == 17 and 9 + 9 == 18 and 8 + 9 == 17 and 11 + 5 == 16
assert all_paths_cost(Q4, "P", "U")[0][0] == 16 and all_paths_cost(Q4, "P", "U")[1][0] > 16

# --- exam question 5 ------------------------------------------------------------------------------------
assert is_consistent(Q5, Q5_H) and is_admissible(Q5, Q5_H, "N")
q5rows, q5closed, q5g, q5p = astar(Q5, Q5_H, "H", "N")
has(astar_md(q5rows), "q5")
assert q5closed == ["H", "K", "L", "N"] and trace_path(q5p, "N") == ["H", "L", "N"] and q5g["N"] == 13
assert 5 + 9 == 14 and 8 + 5 == 13
# N's first g was 14 through K
first_open = {n: (gv, hv, fv) for n, gv, hv, fv in q5rows[2][1]}
assert first_open["N"] == (14, 0, 14)
assert [Q5_H[n] for n in "HJKLMN"] == [10, 8, 6, 4, 4, 0]

# --- exam question 6 (grid, five columns, four rows) --------------------------------------------------
eh = manhattan("E4", EXAM_GRID)
assert eh["A1"] == 7
erows, eclosed, eg, ep = astar(EXAM_GRID, eh, "A1", "E4")
assert eclosed[:6] == ["A1", "A2", "B2", "B3", "B4", "C2"], eclosed[:6]
assert [t[3] for r in erows[1:7] for t in [next(x for x in erows[erows.index(r) - 1][1] if x[0] == r[0])]] == [7] * 6
assert trace_path(ep, "E4") == ["A1", "A2", "B2", "B3", "B4", "C4", "D4", "E4"] and eg["E4"] == 7
assert is_consistent(EXAM_GRID, eh)
ascii_grid = ["     A  B  C  D  E",
              " 1   S  #  .  .  .",
              " 2   .  .  .  #  .",
              " 3   #  .  #  .  .",
              " 4   .  .  .  .  G"]
for r, line in enumerate(ascii_grid[1:], start=1):
    for c, ch in enumerate(line[5:].split()):
        cell = "ABCDE"[c] + str(r)
        assert (ch == "#") == (cell in EXAM_GRID_WALLS), cell
assert "\n".join(ascii_grid) in TEXT
assert eclosed.index("B3") < eclosed.index("C2") and "B4" in eclosed[:5]
assert len(EXAM_GRID) == 16

# --- exam question 3: matrix -------------------------------------------------------------------------
M3 = [[0, 6, 0, 0, 3], [6, 0, 2, 0, 0], [0, 2, 0, 7, 0], [0, 0, 7, 0, 5], [3, 0, 0, 5, 0]]
assert all(M3[i][j] == M3[j][i] for i in range(5) for j in range(5))
assert M3[0][1] + M3[1][2] + M3[2][3] == 15

# --- stretch 1: an overestimating heuristic -----------------------------------------------------------
assert not is_admissible(OVER, OVER_H, "G")
orows, oclosed, og, op = astar(OVER, OVER_H, "S", "G")
has(astar_md(orows), "over")
assert oclosed == ["S", "B", "G"] and og["G"] == 8 and trace_path(op, "G") == ["S", "B", "G"]
odist = dijkstra(OVER, "S", "G")[2]
assert odist["G"] == 7 and dijkstra(OVER, "A", "G")[2]["G"] == 6
assert 1 + 20 == 21 and 4 + 4 == 8 and 1 + 6 == 7

# --- stretch 2: one-way streets -------------------------------------------------------------------------
D2 = directed([("S", "A", 2), ("A", "B", 3), ("B", "S", 1), ("S", "B", 9), ("B", "T", 4), ("A", "T", 8)])
r2, v2, d2, p2 = dijkstra(D2, "S", "T")
assert d2["T"] == 9 and trace_path(p2, "T") == ["S", "A", "B", "T"]
assert 9 + 4 == 13 and 2 + 8 == 10 and 2 + 3 + 4 == 9
assert dijkstra(D2, "B", "A")[2]["A"] == 3 and 1 + 2 == 3
assert D2["T"] == {}

# --- practice questions -----------------------------------------------------------------------------------
T1 = undirected([("W", "X", 1), ("W", "Y", 1), ("X", "Y", 1), ("Y", "Z", 1)])
assert len(T1) == 4 and sorted(T1["Y"]) == ["W", "X", "Z"]
T2 = {"A": {"B": 3, "D": 2}, "B": {"A": 3, "C": 4}, "C": {"B": 4, "D": 6}, "D": {"A": 2, "C": 6}}
assert [[T2[a].get(b, 0) for b in "ABCD"] for a in "ABCD"] == [[0, 3, 0, 2], [3, 0, 4, 0], [0, 4, 0, 6], [2, 0, 6, 0]]
assert 3 + 4 + 6 == 13
assert 7 + 5 == 12 and 9 + 2 == 11 and 11 < 12
T4 = undirected([("V", "W", 4), ("V", "X", 1), ("X", "W", 2), ("W", "Y", 5), ("X", "Y", 8), ("Y", "Z", 3), ("W", "Z", 9)])
t4rows, t4vis, t4dist, t4prev = dijkstra(T4, "V", "Z")
has(dijkstra_md(t4rows, sorted(T4)), "try 5")
assert t4vis == list("VXWYZ") and t4dist["Z"] == 11 and trace_path(t4prev, "Z") == list("VXWYZ") and 1 + 2 + 5 + 3 == 11
T6 = directed([("M", "N", 5), ("N", "M", 8), ("N", "O", 2), ("O", "M", 1)])
assert dijkstra(T6, "M", "O")[2]["O"] == 7 and dijkstra(T6, "O", "M")[2]["M"] == 1 and 5 + 2 == 7
T7 = {"A": (0, None), "B": (4, "A"), "C": (7, "B"), "D": (5, "A"), "E": (9, "D"), "F": (12, "E")}
node, route = "F", []
while node:
    route.append(node)
    node = T7[node][1]
assert route[::-1] == ["A", "D", "E", "F"] and T7["F"][0] == 12
assert T7["E"][0] == T7["D"][0] + 4 and T7["F"][0] == T7["E"][0] + 3 and T7["D"][0] == 5

# --- quiz numbers -------------------------------------------------------------------------------------
assert 9 + 4 == 13 and 9 - 4 == 5 and 9 * 4 == 36
assert abs(ord("D") - ord("A")) + abs(2 - 4) == 5 and 3 * 2 == 6
# --- the hand SVG figures in the chapter are exactly the ones data/cs_ai_figs.py drew and checked -------------
with contextlib.redirect_stdout(io.StringIO()):
    import cs_ai_figs
for key, html in cs_ai_figs.figs.items():
    assert html in TEXT, f"figure {key} in the chapter differs from data/cs_ai_figs.py"
assert TEXT.count("<svg ") == len(cs_ai_figs.figs) + 0 or TEXT.count("<svg ") == len(cs_ai_figs.figs)
print("ok")
