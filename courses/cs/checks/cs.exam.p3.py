# checks/cs.exam.p3.py: lints every pseudocode block and recomputes every value the guide states.
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.exam.p3"

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
from fractions import Fraction

ROOT = CHAPTER.parent.parent
PL = runpy.run_path(str(ROOT / "data" / "cs.prolog_sim.py"))
query = PL["query"]

assert run_python_blocks([]) == 0
assert lint_pseudocode_blocks() == 2
ids = {c["id"] for c in json.loads((ROOT / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT)) <= ids

# ---- pace
RATE = Fraction(90, 75)
assert RATE == Fraction(6, 5)
for m, txt, rnd in [(4, "4.8", 5), (6, "7.2", 7), (7, "8.4", 8), (9, "10.8", 11)]:
    assert float(m * RATE) == float(txt) and int(m * RATE + Fraction(1, 2)) == rnd
    assert f"| {m} | {txt} | {rnd} |" in TEXT, m
assert Fraction(90, 12) == Fraction(15, 2) and r"\(90 \div 12 = 7.5\)" in TEXT
assert r"\(7 \times 1.2 = 8.4\)" in TEXT and r"\(90 \div 75 = 1.2\)" in TEXT


# ---- floating point, 8-bit mantissa and 4-bit exponent
def twos(bits, n):
    v = int(bits, 2)
    return v - (1 << n) if bits[0] == "1" else v


def fp_value(m, e):
    return Fraction(twos(m, len(m)), 1 << (len(m) - 1)) * Fraction(2) ** twos(e, len(e))


def fp_encode(x, mbits=8, ebits=4):
    """normalised pattern for x (a Fraction), mantissa truncated towards zero"""
    for exp in range(-(1 << (ebits - 1)), (1 << (ebits - 1))):
        man = Fraction(x) / Fraction(2) ** exp
        if Fraction(1, 2) <= man < 1 or -1 <= man < Fraction(-1, 2):
            scaled = man * (1 << (mbits - 1))
            if scaled.denominator != 1:
                scaled = Fraction(int(scaled))
            mv = int(scaled) & ((1 << mbits) - 1)
            return format(mv, f"0{mbits}b"), format(exp & ((1 << ebits) - 1), f"0{ebits}b")
    raise ValueError


m, e = fp_encode(Fraction(-15, 4))
assert (m, e) == ("10001000", "0010") and fp_value(m, e) == Fraction(-15, 4)
assert fp_encode(Fraction(15, 4)) == ("01111000", "0010")
assert format(~0b01111000 & 0xFF, "08b") == "10000111" and format((~0b01111000 + 1) & 0xFF, "08b") == "10001000"
assert Fraction(-1) + Fraction(1, 16) == Fraction(-15, 16) and Fraction(-15, 16) * 4 == Fraction(-15, 4)
assert 2 + 1 + Fraction(1, 2) + Fraction(1, 4) == Fraction(15, 4)
frac, bits = Fraction(3, 10), ""
for _ in range(10):
    frac *= 2
    bits += str(int(frac))
    frac -= int(frac)
assert bits == "0100110011"
m3, e3 = fp_encode(Fraction(3, 10))
assert (m3, e3) == ("01001100", "1111")
assert float(fp_value(m3, e3)) == 0.296875 and fp_value(m3, e3) != Fraction(3, 10)
assert "0.296875" in TEXT and "0.0100110011" in TEXT
assert fp_value("10100000", "0010") == -3 and Fraction(-1) + Fraction(1, 4) == Fraction(-3, 4)
assert fp_value("00110100", "0100") == fp_value("01101000", "0011") == Fraction(13, 2)

# ---- K-map
ONES = {0b0000, 0b0001, 0b0010, 0b0101, 0b1000, 0b1001, 0b1010}


def z(a, b, c, d):
    return int((not b and not d) or (not b and not c) or (not a and not c and d))


for n in range(16):
    a, b, c, d = (n >> 3) & 1, (n >> 2) & 1, (n >> 1) & 1, n & 1
    assert z(a, b, c, d) == (n in ONES), n
header, rows = table_after("| AB \\ CD | 00 | 01 | 11 | 10 |\n|---|---|---|---|---|\n| 00 | 1 | 1 | 0 | 1 |")
gray = [0b00, 0b01, 0b11, 0b10]
for ri, row in enumerate(rows):
    for ci, cell in enumerate(row[1:]):
        n = (gray[ri] << 2) | gray[ci]
        assert int(cell) == (n in ONES), (ri, ci)
assert sum(int(c) for r in rows for c in r[1:]) == 7
groups = [{0, 2, 8, 10}, {0, 1, 8, 9}, {1, 5}]
for i, g in enumerate(groups):
    rest = set().union(*[x for j, x in enumerate(groups) if j != i])
    assert ONES - rest, i
assert set().union(*groups) == ONES and all(g <= ONES for g in groups)
assert (groups[0] - groups[1] - groups[2]) == {2, 10} and groups[1] - groups[0] - groups[2] == {9}
assert groups[2] - groups[0] - groups[1] == {5}

# ---- Dijkstra
EDGES = [("S", "A", 4), ("S", "B", 2), ("A", "B", 1), ("A", "C", 5), ("B", "C", 8), ("B", "D", 10), ("C", "D", 2),
         ("C", "T", 6), ("D", "T", 3)]
adj = {}
for u, v, w in EDGES:
    adj.setdefault(u, {})[v] = w
    adj.setdefault(v, {})[u] = w
INF = float("inf")
dist = {v: INF for v in adj}
prev = {}
dist["S"] = 0
done = []
steps = []
while len(done) < len(adj):
    cur = min((v for v in adj if v not in done), key=lambda v: (dist[v], v))
    done.append(cur)
    ch = {}
    for nb, w in adj[cur].items():
        if nb not in done and dist[cur] + w < dist[nb]:
            dist[nb] = dist[cur] + w
            prev[nb] = cur
            ch[nb] = f"{dist[nb]} {cur}"
    steps.append((cur, ch))
assert [s[0] for s in steps] == ["S", "B", "A", "C", "D", "T"]
header, rows = table_after("| Step | Visit | S | A | B | C | D | T |")
assert header[2:] == ["S", "A", "B", "C", "D", "T"] and rows[0][2:] == ["0"] + ["∞"] * 5
for r, (cur, ch) in zip(rows[1:], steps):
    assert r[1] == cur
    for k, v in enumerate(header[2:]):
        assert r[2 + k] == ch.get(v, ""), (cur, v, r[2 + k], ch.get(v, ""))
assert dist["T"] == 13 and 2 + 1 + 5 + 2 + 3 == 13
path, v = ["T"], "T"
while v != "S":
    v = prev[v]
    path.append(v)
assert path[::-1] == ["S", "B", "A", "C", "D", "T"]
assert 2 + 1 == 3 and 3 + 5 == 8 and 8 + 2 == 10 and 8 + 6 == 14 and 10 + 3 == 13

# ---- linked list deletion
Data = [None, 30, 10, 50, 20, 40, None]
Pointer = [None, 5, 4, 0, 1, 3, 0]
for line in ["| Data | 30 | 10 | 50 | 20 | 40 | |", "| Pointer | 5 | 4 | 0 | 1 | 3 | 0 |"]:
    assert line in TEXT
Start, Free = 2, 6


def walk():
    out, c = [], Start
    while c != 0:
        out.append(Data[c])
        c = Pointer[c]
    return out


def freelist():
    out, c = [], Free
    while c != 0:
        out.append(c)
        c = Pointer[c]
    return out


assert walk() == [10, 20, 30, 40, 50] and freelist() == [6]


def delete_item(target):
    global Start, Free
    previous, current = 0, Start
    while current != 0 and Data[current] != target:
        previous, current = current, Pointer[current]
    if current == 0:
        return False
    if previous == 0:
        Start = Pointer[current]
    else:
        Pointer[previous] = Pointer[current]
    Pointer[current] = Free
    Free = current
    return True


assert delete_item(99) is False and walk() == [10, 20, 30, 40, 50]
assert delete_item(30) is True
assert walk() == [10, 20, 40, 50] and Pointer[4] == 5 and Pointer[1] == 6 and Free == 1 and freelist() == [1, 6]
assert delete_item(10) is True and Start == 4 and walk() == [20, 40, 50] and freelist() == [2, 1, 6]


# ---- RPN
def rpn_eval(expr, trace=None):
    stack = []
    for tok in expr.split():
        if tok in ("+", "-", "*", "/"):
            right, left = stack.pop(), stack.pop()
            if tok == "+":
                stack.append(left + right)
            elif tok == "-":
                stack.append(left - right)
            elif tok == "*":
                stack.append(left * right)
            else:
                stack.append(Fraction(left, right))
        else:
            stack.append(Fraction(int(tok)))
        if trace is not None:
            trace.append((tok, [int(x) for x in stack]))
    assert len(stack) == 1
    return stack[0]


tr = []
assert rpn_eval("9 3 / 4 2 + * 5 -", tr) == 13
assert [s for _, s in tr] == [[9], [9, 3], [3], [3, 4], [3, 4, 2], [3, 6], [18], [18, 5], [13]]
header, rows = table_after("| Token | Action | Stack, bottom to top |")
assert [", ".join(str(x) for x in s) for _, s in tr] == [r[2] for r in rows]
assert [t for t, _ in tr] == [r[0] for r in rows]
for P, Q, R, S, T in [(2, 3, 4, 8, 2), (5, 1, 7, 9, 3), (1, 1, 1, 6, 6)]:
    assert rpn_eval(f"{P} {Q} + {R} * {S} {T} / -") == Fraction((P + Q) * R) - Fraction(S, T)
assert "P Q + R * S T / -" in TEXT and "(((P + Q) * R) - (S / T))" in TEXT
assert 9 // 3 == 3 and 4 + 2 == 6 and 3 * 6 == 18 and 18 - 5 == 13
assert rpn_eval("2 3 + 4 *") == (2 + 3) * 4

# ---- declarative rule
KB = """teaches(ortiz, maths).
teaches(khan, physics).
teaches(ortiz, computing).
room(maths, r12).
room(physics, r5).
room(computing, r7).
works_in(Teacher, Room) IF teaches(Teacher, Subject) AND room(Subject, Room).
"""
for line in KB.strip().split("\n"):
    assert line in TEXT, line
assert [a["R"] for a in query(KB, "works_in(ortiz, R)")] == ["r12", "r7"]

print("ok")
