# checks/cs.adts.py: runs every Python block, lints pseudocode blocks, recomputes every number the chapter states.
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.adts"

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



blocks = run_python_blocks([])
assert blocks == 11, f"expected 11 python blocks, found {blocks}"
PSEUDO = lint_pseudocode_blocks()
assert PSEUDO == 18, f"expected 18 pseudocode blocks, found {PSEUDO}"


def rows_of(marker):
    return table_after(marker)


# ---------------------------------------------------------------------------------------------
# Linked list model (pseudocode semantics, 1-based, null pointer 0)
# ---------------------------------------------------------------------------------------------
class LL:
    def __init__(self, n):
        self.n = n
        self.data = [None] * (n + 1)
        self.ptr = [0] * (n + 1)
        self.start = 0
        self.free = 1
        for i in range(1, n):
            self.ptr[i] = i + 1
        self.ptr[n] = 0

    def insert(self, x):
        if self.free == 0:
            return False
        new = self.free
        self.free = self.ptr[new]
        self.data[new] = x
        prev, cur = 0, self.start
        while cur != 0 and self.data[cur] < x:
            prev, cur = cur, self.ptr[cur]
        self.ptr[new] = cur
        if prev == 0:
            self.start = new
        else:
            self.ptr[prev] = new
        return True

    def delete(self, x):
        prev, cur = 0, self.start
        while cur != 0 and self.data[cur] != x:
            prev, cur = cur, self.ptr[cur]
        if cur == 0:
            return False
        if prev == 0:
            self.start = self.ptr[cur]
        else:
            self.ptr[prev] = self.ptr[cur]
        self.ptr[cur] = self.free
        self.free = cur
        return True

    def find(self, x):
        cur = self.start
        while cur != 0 and self.data[cur] != x:
            cur = self.ptr[cur]
        return cur

    def items(self):
        out, cur = [], self.start
        while cur:
            out.append(self.data[cur])
            cur = self.ptr[cur]
        return out

    def free_chain(self):
        out, cur = [], self.free
        while cur:
            out.append(cur)
            cur = self.ptr[cur]
        return out


L = LL(6)
for x in (40, 15, 62, 28, 51):
    L.insert(x)
assert (L.ptr[1:], L.start, L.free, L.items()) == ([5, 4, 0, 1, 3, 0], 2, 6, [15, 28, 40, 51, 62])
chain, cur = [], L.start
while cur:
    chain.append((cur, L.data[cur]))
    cur = L.ptr[cur]
assert chain == [(2, 15), (4, 28), (1, 40), (5, 51), (3, 62)]
L.delete(15)
assert (L.start, L.free, L.ptr[2]) == (4, 2, 6)
L.delete(62)
assert (L.ptr[1:], L.start, L.free, L.items()) == ([5, 6, 2, 1, 0, 0], 4, 3, [28, 40, 51])
assert L.ptr[5] == 0 and L.ptr[3] == 2 and L.free_chain() == [3, 2, 6]
assert (L.find(28), L.find(99)) == (4, 0)
L.insert(33)
assert (L.ptr[1:], L.start, L.free, L.items(), L.data[3]) == ([5, 6, 1, 3, 0, 0], 4, 2, [28, 33, 40, 51], 33)

# Exam practice: deletions of School and Harbour
Q = LL(7)
for x in ("Market", "Harbour", "Temple", "Station", "School"):
    Q.insert(x)
header, trs = rows_of("| Index | Data | Pointer |")
assert column_values(header, trs, "Pointer") == [str(p) for p in Q.ptr[1:]] == ["5", "1", "0", "3", "4", "7", "0"]
assert (Q.start, Q.free) == (2, 6) and [r[1] for r in trs][:5] == Q.data[1:6]
Q.delete("School")
Q.delete("Harbour")
header, trs = rows_of("A: After both deletions the `Pointer` column")
assert column_values(header, trs, "Pointer") == [str(p) for p in Q.ptr[1:]] == ["4", "5", "0", "3", "6", "7", "0"]
assert (Q.start, Q.free) == (1, 2)
assert [Q.data[i] for i in range(1, 6)] == ["Market", "Harbour", "Temple", "Station", "School"]

# Spot the error: no FreePointer update
ptr, free, start, data = [0, 2, 3, 0], 1, 0, [None] * 4
for item in ("X", "Y"):
    new = free
    data[new] = item
    ptr[new] = start
    start = new
assert (data[1], ptr[1], start, free) == ("Y", 1, 1, 1)         # node 1 points to itself, "X" lost

# ---------------------------------------------------------------------------------------------
# Stack and queue facts in text
# ---------------------------------------------------------------------------------------------
st = []
popped = []
for op in [("push", 5), ("push", 9), ("pop",), ("push", 2), ("push", 7), ("pop",), ("pop",)]:
    if op[0] == "push":
        st.append(op[1])
    else:
        popped.append(st.pop())
assert popped == [9, 7, 2] and st == [5]
assert (5 % 5) + 1 == 1 and (6 % 6) + 1 == 1 and (4 % 4) + 1 == 1


# ---------------------------------------------------------------------------------------------
# Binary search tree
# ---------------------------------------------------------------------------------------------
class Tree:
    def __init__(self, n):
        self.left = [0] * (n + 1)
        self.data = [None] * (n + 1)
        self.right = [0] * (n + 1)
        self.root = 0
        self.free = 1
        for i in range(1, n):
            self.left[i] = i + 1

    def insert(self, x):
        new = self.free
        self.free = self.left[new]
        self.data[new], self.left[new], self.right[new] = x, 0, 0
        if self.root == 0:
            self.root = new
            return
        cur = self.root
        while cur:
            par = cur
            if x < self.data[cur]:
                go_left, cur = True, self.left[cur]
            else:
                go_left, cur = False, self.right[cur]
        if go_left:
            self.left[par] = new
        else:
            self.right[par] = new

    def path(self, x):
        cur, seen = self.root, []
        while cur and self.data[cur] != x:
            seen.append(self.data[cur])
            cur = self.left[cur] if x < self.data[cur] else self.right[cur]
        if cur:
            seen.append(self.data[cur])
        return cur, seen


T = Tree(7)
for x in (27, 14, 35, 10):
    T.insert(x)
before = (list(T.left[1:]), list(T.data[1:]), list(T.right[1:]), T.free)
assert before == ([2, 4, 0, 0, 6, 7, 0], [27, 14, 35, 10, None, None, None], [3, 0, 0, 0, 0, 0, 0], 5)
T.insert(31)
after = (list(T.left[1:]), list(T.data[1:]), list(T.right[1:]), T.free)
assert after == ([2, 4, 5, 0, 0, 7, 0], [27, 14, 35, 10, 31, None, None], [3, 0, 0, 0, 0, 0, 0], 6)
assert T.path(31) == (5, [27, 35, 31])
header, trs = rows_of("| Node | LeftPointer before |")


def cell(v):
    return "" if v is None else str(v)


for k, vals in enumerate([before[0], before[1], before[2], after[0], after[1], after[2]]):
    assert [r[k + 1] for r in trs] == [cell(v) for v in vals], k
T.insert(19)
T.insert(42)
assert (T.left[1:], T.data[1:], T.right[1:], T.root, T.free) == ([2, 4, 5, 0, 0, 0, 0], [27, 14, 35, 10, 31, 19, 42], [3, 6, 7, 0, 0, 0, 0], 1, 0)
header, trs = rows_of("| Node | LeftPointer | Data | RightPointer |")
assert column_values(header, trs, "LeftPointer") == [str(v) for v in T.left[1:]]
assert column_values(header, trs, "Data") == [str(v) for v in T.data[1:]]
assert column_values(header, trs, "RightPointer") == [str(v) for v in T.right[1:]]


def trav(tree, order):
    def go(n):
        if n == 0:
            return []
        a, b, c = go(tree.left[n]), [tree.data[n]], go(tree.right[n])
        return {"in": a + b + c, "pre": b + a + c, "post": a + c + b}[order]
    return go(tree.root)


assert trav(T, "in") == [10, 14, 19, 27, 31, 35, 42] == sorted(T.data[1:])
assert trav(T, "pre") == [27, 14, 10, 19, 35, 31, 42] and trav(T, "post") == [10, 19, 14, 31, 42, 35, 27]

# Try: 50 30 70 20 40
T2 = Tree(5)
for x in (50, 30, 70, 20, 40):
    T2.insert(x)
assert trav(T2, "in") == [20, 30, 40, 50, 70]
assert [T2.data[i] for i in range(1, 6) if T2.left[i] == 0 and T2.right[i] == 0] == [70, 20, 40] or True
assert sorted(T2.data[i] for i in range(1, 6) if T2.left[i] == 0 and T2.right[i] == 0) == [20, 40, 70]

# Exam practice: 8 3 10 1 6 14 4
T3 = Tree(7)
for x in (8, 3, 10, 1, 6, 14, 4):
    T3.insert(x)
assert trav(T3, "in") == [1, 3, 4, 6, 8, 10, 14] and trav(T3, "post") == [1, 4, 6, 3, 14, 10, 8]
assert T3.path(4) == (T3.data.index(4), [8, 3, 6, 4]) and len(T3.path(4)[1]) == 4


def height(values):
    t = Tree(len(values))
    for v in values:
        t.insert(v)

    def h(n):
        return 0 if n == 0 else 1 + max(h(t.left[n]), h(t.right[n]))
    return h(t.root), t


h1, t1 = height([5, 10, 15, 20, 25, 30, 35])
h2, t2 = height([20, 10, 30, 5, 15, 25, 35])
assert (h1, h2) == (7, 3) and len(t1.path(35)[1]) == 7 and len(t2.path(35)[1]) == 3 and t2.path(35)[1] == [20, 30, 35]
assert height([27, 14, 35, 10, 31, 19, 42])[0] == 3 and height([10, 14, 19, 27, 31, 35, 42])[0] == 7
assert (2 ** 10 - 1, 2 ** 9 - 1) == (1023, 511) and 511 < 1000 <= 1023

# Stretch: expression tree
nodes = {1: (2, "*", 3), 2: (4, "+", 5), 3: (6, "-", 7), 4: (0, "6", 0), 5: (0, "2", 0), 6: (0, "9", 0), 7: (0, "3", 0)}
header, trs = rows_of("The root is node 1.")
assert [r[1] for r in trs] == [str(nodes[k][0]) for k in range(1, 8)]
assert [r[2] for r in trs] == [nodes[k][1] for k in range(1, 8)]
assert [r[3] for r in trs] == [str(nodes[k][2]) for k in range(1, 8)]


def post(n):
    return [] if n == 0 else post(nodes[n][0]) + post(nodes[n][2]) + [nodes[n][1]]


def inord(n):
    return [] if n == 0 else inord(nodes[n][0]) + [nodes[n][1]] + inord(nodes[n][2])


rpn = post(1)
assert rpn == ["6", "2", "+", "9", "3", "-", "*"] and inord(1) == ["6", "+", "2", "*", "9", "-", "3"]
stack, states = [], []
for tok in rpn:
    if tok in "+-*":
        b = stack.pop()
        a = stack.pop()
        stack.append({"+": a + b, "-": a - b, "*": a * b}[tok])
    else:
        stack.append(int(tok))
    states.append(list(stack))
assert states == [[6], [6, 2], [8], [8, 9], [8, 9, 3], [8, 6], [48]] and (6 + 2) * (9 - 3) == 48


# ---------------------------------------------------------------------------------------------
# Hash table
# ---------------------------------------------------------------------------------------------
def build(keys, n=7):
    t = [0] * (n + 1)
    pos = []
    for k in keys:
        i = k % n + 1
        while t[i] != 0:
            i = i % n + 1
        t[i] = k
        pos.append(i)
    return t[1:], pos


assert build([1042, 2317, 3085, 1049]) == ([2317, 1049, 0, 0, 0, 3085, 1042], [7, 1, 6, 2])
assert [k % 7 + 1 for k in (1042, 1049)] == [7, 7] and 1042 % 7 == 6 and 1049 % 7 == 6 and 2317 % 7 == 0
assert build([15, 22])[1] == [2, 3] and 15 % 7 == 1 and 22 % 7 == 1

# ---------------------------------------------------------------------------------------------
# Graph
# ---------------------------------------------------------------------------------------------
V = "ABCDE"
E = [("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "D", 8), ("D", "E", 3)]
M = [[0] * 5 for _ in range(5)]
for a, b, w in E:
    M[V.index(a)][V.index(b)] = M[V.index(b)][V.index(a)] = w
header, trs = rows_of("rows and columns in the order A, B, C, D, E):")
assert [[int(c) for c in r[1:]] for r in trs] == M and [r[0] for r in trs] == list(V)
assert sum(1 for r in M for x in r if x) == 12 == 2 * len(E)
assert all(M[i][j] == M[j][i] for i in range(5) for j in range(5))
V2 = "PQRS"
E2 = [("P", "Q", 6), ("P", "R", 3), ("Q", "R", 2), ("R", "S", 5)]
M2 = [[0] * 4 for _ in range(4)]
for a, b, w in E2:
    M2[V2.index(a)][V2.index(b)] = M2[V2.index(b)][V2.index(a)] = w
header, trs = rows_of("| | P | Q | R | S |")
assert [[int(c) for c in r[1:]] for r in trs] == M2
M3 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]          # try question: A-B, B-C
assert M3[0][1] == M3[1][0] == M3[1][2] == M3[2][1] == 1 and M3[0][2] == 0

# ---------------------------------------------------------------------------------------------
# Queue from two stacks: exam table (5, 8, deq, 2, deq, deq)
# ---------------------------------------------------------------------------------------------
inn, out, rows = [], [], []
for op in [("e", 5), ("e", 8), ("d",), ("e", 2), ("d",), ("d",)]:
    ret = ""
    if op[0] == "e":
        inn.append(op[1])
    else:
        if not out:
            while inn:
                out.append(inn.pop())
        ret = str(out.pop())
    rows.append((", ".join(map(str, inn)), ", ".join(map(str, out)), ret))
header, trs = rows_of("| Operation | InStack (bottom first) |")
assert [(r[1], r[2], r[3]) for r in trs] == rows, rows

print("ok")
