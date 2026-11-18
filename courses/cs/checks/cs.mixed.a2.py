# checks/cs.mixed.a2.py: runs every Python block and recomputes every number in the practice sets.
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.mixed.a2"

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


def table_after(marker):
    """Rows of the first Markdown table after the text marker, as lists of cell strings."""
    start = TEXT.index(marker)
    rows = []
    for line in TEXT[start:].split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
        elif rows:
            break
    return rows[0], rows[1:]


def column_values(header, rows, name):
    k = header.index(name)
    return [r[k] for r in rows if r[k] != ""]


import json
import runpy
from collections import deque
from fractions import Fraction

ROOT = CHAPTER.parent.parent
SIM = runpy.run_path(str(ROOT / "data" / "cs.asmsim.py"))
PL = runpy.run_path(str(ROOT / "data" / "cs.prolog_sim.py"))
query = PL["query"]

assert run_python_blocks([]) == 5
assert lint_pseudocode_blocks() == 3
ids = {c["id"] for c in json.loads((ROOT / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert set(re.findall(r"\(#(cs\.[\w.]+)\)", TEXT)) <= ids

# ---- the two sets
sets = re.split(r"^:::try ", TEXT, flags=re.M)
p3 = next(s for s in sets if s.startswith("Paper 3 style"))
p4 = next(s for s in sets if s.startswith("Paper 4 style"))
m3 = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", p3, re.M)]
m4 = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", p4, re.M)]
assert len(m3) == 18 and sum(m3) == 121, (len(m3), sum(m3))
assert len(m4) == 5 and sum(m4) == 52, (len(m4), sum(m4))
assert len(re.findall(r"^Q: \[\d+ marks\] ★+ \(#cs\.\w+\)", p3, re.M)) == 18
assert len(re.findall(r"^Q: \[\d+ marks\] ★+ \(#cs\.\w+\)", p4, re.M)) == 5
assert float(121 * Fraction(6, 5)) == 145.2 and 52 * 2 == 104
assert r"\(121 \times 1.2 = 145.2\)" in TEXT and r"\(52 \times 2 = 104\)" in TEXT

# ---- Q2 hashing
SLOTS = {}
for key in [15, 22, 9, 31, 12]:
    s = key % 7 + 1
    while s in SLOTS.values():
        s = s % 7 + 1
    SLOTS[key] = s
assert SLOTS == {15: 2, 22: 3, 9: 4, 31: 5, 12: 6}
assert [15 % 7, 22 % 7, 9 % 7, 31 % 7, 12 % 7] == [1, 1, 2, 3, 5] and 29 % 7 == 1
assert "| Key stored | | 15 | 22 | 9 | 31 | 12 | |" in TEXT


# ---- floating point helpers
def twos(bits):
    v = int(bits, 2)
    return v - (1 << len(bits)) if bits[0] == "1" else v


def fp(m, e):
    return Fraction(twos(m), 1 << (len(m) - 1)) * Fraction(2) ** twos(e)


assert fp("01101000", "0011") == Fraction(13, 2) and Fraction(13, 16) * 8 == Fraction(13, 2)
assert 4 + 2 + Fraction(1, 2) == Fraction(13, 2)
assert fp("10110000", "0010") == Fraction(-5, 2) and format(~0b01010000 & 255, "08b") == "10101111"
assert format((~0b01010000 + 1) & 255, "08b") == "10110000" and 2 + Fraction(1, 2) == Fraction(5, 2)
assert fp("01111111", "0111") == 127 and Fraction(127, 128) * 128 == 127
best = max(fp(format(m, "08b"), format(e, "04b")) for m in range(256) for e in range(16)
           if format(m, "08b")[:2] in ("01", "10"))
assert best == 127

# ---- Q5 pipeline
assert 5 * 8 == 40 and 5 + 8 - 1 == 12 and 8 - 1 == 7

# ---- Q6 Boolean simplification
for a in (0, 1):
    for b in (0, 1):
        x = (a and b) or (a and not b) or ((not a) and b)
        assert int(bool(x)) == (a | b)
        assert int(bool(a or ((not a) and b))) == (a | b)

# ---- Q7 adders and flip-flop
for a in (0, 1):
    for b in (0, 1):
        assert (a ^ b, a & b) == ((a + b) % 2, (a + b) // 2)
assert divmod(1 + 1 + 1, 2) == (1, 1) and format(3, "b") == "11"


def jk(q, j, k):
    return {(0, 0): q, (0, 1): 0, (1, 0): 1, (1, 1): 1 - q}[(j, k)]


assert jk(0, 1, 1) == 1 and jk(0, 0, 0) == 0

# ---- Q8 round robin, time slice 3
procs = {"P1": (0, 6), "P2": (1, 3), "P3": (2, 3)}
remaining = {p: b for p, (a, b) in procs.items()}
queue, t, gantt, completion, arrived = deque(), 0, [], {}, set()


def arrive(upto):
    for p, (a, b) in sorted(procs.items(), key=lambda x: (x[1][0], x[0])):
        if a <= upto and p not in arrived:
            arrived.add(p)
            queue.append(p)


arrive(0)
while queue:
    p = queue.popleft()
    run = min(3, remaining[p])
    gantt.append((p, t, t + run))
    t += run
    remaining[p] -= run
    arrive(t)
    if remaining[p] > 0:
        queue.append(p)
    else:
        completion[p] = t
assert gantt == [("P1", 0, 3), ("P2", 3, 6), ("P3", 6, 9), ("P1", 9, 12)]
assert completion == {"P2": 6, "P3": 9, "P1": 12}
wait = {p: completion[p] - procs[p][0] - procs[p][1] for p in procs}
assert wait == {"P1": 6, "P2": 2, "P3": 4} and Fraction(sum(wait.values()), 3) == 4
assert "| Process running | P1 | P2 | P3 | P1 |" in TEXT


# ---- Q9 RPN
def rpn(expr, trace=None):
    st = []
    for tok in expr.split():
        if tok in ("+", "-", "*", "/"):
            r, l = st.pop(), st.pop()
            st.append({"+": l + r, "-": l - r, "*": l * r, "/": Fraction(l) / r}[tok])
        else:
            st.append(int(tok))
        if trace is not None:
            trace.append(list(st))
    return st[0]


tr = []
assert rpn("6 5 * 8 4 / +", tr) == 32 and 6 * 5 + Fraction(8, 4) == 32
assert tr[2] == [30] and tr[-2] == [30, 2] and tr[-1] == [32]
assert rpn("8 2 -") == 6 and 2 - 8 == -6

# ---- Q11 A* and Dijkstra
EDGES = [("S", "B", 6), ("B", "A", 2), ("B", "D", 4), ("A", "G", 5), ("A", "C", 4), ("A", "D", 6), ("C", "D", 3)]
H = {"S": 11, "A": 4, "B": 6, "C": 7, "D": 9, "G": 0}
adj = {}
for u, v, w in EDGES:
    adj.setdefault(u, {})[v] = w
    adj.setdefault(v, {})[u] = w
true = {v: 10 ** 9 for v in adj}
true["G"] = 0
for _ in range(10):
    for u in adj:
        for v, w in adj[u].items():
            true[u] = min(true[u], true[v] + w)
assert all(H[v] <= true[v] for v in adj) and all(H[u] <= w + H[v] for u in adj for v, w in adj[u].items())
g, prev, done, rows = {"S": 0}, {}, [], []
openset = {"S"}
while openset:
    f = {v: g[v] + H[v] for v in openset}
    assert sorted(f.values()).count(min(f.values())) == 1
    cur = min(openset, key=lambda v: f[v])
    openset.remove(cur)
    done.append(cur)
    rows.append((cur, g[cur], H[cur], g[cur] + H[cur]))
    if cur == "G":
        break
    for nb, w in adj[cur].items():
        if nb not in done and (nb not in g or g[cur] + w < g[nb]):
            g[nb] = g[cur] + w
            prev[nb] = cur
            openset.add(nb)
assert rows == [("S", 0, 11, 11), ("B", 6, 6, 12), ("A", 8, 4, 12), ("G", 13, 0, 13)]
header, trows = table_after("| Step | Town chosen | g | h | f |")
assert [(r[1], int(r[2]), int(r[3]), int(r[4])) for r in trows] == rows
assert g["D"] == 10 and g["D"] + H["D"] == 19 and g["A"] + 4 == 12 and 12 + 7 == 19
path, v = ["G"], "G"
while v != "S":
    v = prev[v]
    path.append(v)
assert path[::-1] == ["S", "B", "A", "G"] and 6 + 2 + 5 == 13
dist = {v: 10 ** 9 for v in adj}
dist["S"] = 0
dv = []
while len(dv) < len(adj):
    cur = min((v for v in adj if v not in dv), key=lambda v: (dist[v], v))
    dv.append(cur)
    if cur == "G":
        break
    for nb, w in adj[cur].items():
        dist[nb] = min(dist[nb], dist[cur] + w)
assert dv == ["S", "B", "A", "D", "C", "G"] and dist["D"] == 10 and dist["C"] == 12 and dist["G"] == 13

# ---- Q13 binary search
VALUES = [5, 9, 14, 21, 26, 33, 40, 47, 52, 61, 70, 84]
assert VALUES == sorted(VALUES) and len(VALUES) == 12
assert "| Value | 5 | 9 | 14 | 21 | 26 | 33 | 40 | 47 | 52 | 61 | 70 | 84 |" in TEXT
low, high, steps = 1, 12, []
while low <= high:
    mid = (low + high) // 2
    steps.append((low, high, mid, VALUES[mid - 1]))
    if VALUES[mid - 1] == 47:
        break
    if VALUES[mid - 1] < 47:
        low = mid + 1
    else:
        high = mid - 1
assert steps == [(1, 12, 6, 33), (7, 12, 9, 52), (7, 8, 7, 40), (8, 8, 8, 47)]
header, rows = table_after("| Low | High | Mid | Values[Mid] | Result |")
assert [tuple(int(c) for c in r[:4]) for r in rows] == steps


# ---- Q14 BST and circular queue
class N:
    def __init__(self, v):
        self.v, self.l, self.r = v, None, None


def ins(t, v):
    if t is None:
        return N(v)
    if v < t.v:
        t.l = ins(t.l, v)
    else:
        t.r = ins(t.r, v)
    return t


root = None
for v in [38, 20, 55, 12, 30, 47, 62, 25]:
    root = ins(root, v)


def nodes(t):
    if t:
        yield from nodes(t.l)
        yield t
        yield from nodes(t.r)


header, rows = table_after("| Node | Left child | Right child |")
table = {int(r[0]): (r[1], r[2]) for r in rows}
for n in nodes(root):
    assert table[n.v] == (str(n.l.v) if n.l else "none", str(n.r.v) if n.r else "none"), n.v
assert len(table) == 8 and [n.v for n in nodes(root)] == [12, 20, 25, 30, 38, 47, 55, 62]
Q, head, tail, count = [None] * 6, 1, 0, 0
for ch in "ABCD":
    tail = (tail % 5) + 1
    Q[tail] = ch
    count += 1
for _ in range(2):
    head = (head % 5) + 1
    count -= 1
for ch in "EFG":
    tail = (tail % 5) + 1
    Q[tail] = ch
    count += 1
assert Q[1:] == ["F", "G", "C", "D", "E"] and (head, tail, count) == (3, 2, 5)
assert "| F | G | C | D | E |" in TEXT


# ---- Q15 recursion
def digits(n, calls):
    calls.append(n)
    return 1 if n < 10 else 1 + digits(n // 10, calls)


calls = []
assert digits(4821, calls) == 4 and calls == [4821, 482, 48, 4]
assert [digits(n, []) for n in (4821, 482, 48, 4)] == [4, 3, 2, 1]
header, rows = table_after("| Call | N | Value returned |")
assert [(int(r[1]), int(r[2])) for r in rows] == [(4821, 4), (482, 3), (48, 2), (4, 1)]

# ---- Q17 declarative and low-level
KB = """flight(lima, cusco).
flight(lima, quito).
flight(quito, bogota).
flight(cusco, puno).
connects(X, Z) IF flight(X, Y) AND flight(Y, Z).
"""
for line in KB.strip().split("\n"):
    assert line in TEXT, line
assert [a["Where"] for a in query(KB, "connects(lima, Where)")] == ["puno", "bogota"]
assert query(KB, "connects(cusco, Where)") == []
prog = "100 LDR #2\n101 LDX 300\n102 ADD 301\n103 STO 303\n104 END\n300 10\n301 20\n302 30\n303 0"
for line in ["100   LDR #2", "101   LDX 300", "102   ADD 301", "103   STO 303", "104   END", "300   10", "301   20",
             "302   30", "303   0"]:
    assert line in TEXT, line
final = SIM["run"](prog)[1]
assert final["acc"] == 50 and final["mem"][303] == 50 and final["ix"] == 2 and 300 + 2 == 302 and 30 + 20 == 50

# ---- Paper 4: the expected output in each task equals what the model program prints
p4_start = TEXT.index(":::try Paper 4 style")
p4_fences = [f for f in FENCES if f.start() > p4_start]
expected = [f.group(2) for f in p4_fences
            if f.group(1) == "text" and TEXT[:f.start()].rstrip().endswith("The expected output is:")]
outputs = [f.group(2) for f in p4_fences if f.group(1) == "output"]
assert len(expected) == 5 and len(outputs) == 5
for e, o in zip(expected, outputs):
    assert e.strip() == o.strip()

# ---- quiz numbers
import math
assert 2 ** 9 == 512 < 1000 < 1024 == 2 ** 10 and math.floor(math.log2(1000)) + 1 == 10
assert [1042 % 7, 2056 % 7, 3011 % 7, 4077 % 7, 2113 % 7, 5023 % 7] == [6, 5, 1, 3, 6, 4]
quiz = re.search(r"^:::quiz.*?^:::", TEXT, re.S | re.M).group(0)
qs = re.split(r"^\? ", quiz, flags=re.M)[1:]
assert len(qs) == 11
for q in qs:
    assert len(re.findall(r"^\+ ", q, re.M)) == 1 and 2 <= len(re.findall(r"^- ", q, re.M)) <= 4

print("ok")
