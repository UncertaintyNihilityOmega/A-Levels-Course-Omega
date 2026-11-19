# checks/cs.mock.p3.py: Mock Paper 3: marks, links, the graph figure and every number and trace in the mark schemes
# (the helper below is the course's standard one; only CHAPTER_ID changes).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.mock.p3"

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


# =============================================================================================
# Mock Paper 3: totals, links, the graph figure, and every number and trace in the mark schemes
# =============================================================================================
import itertools
import json
import runpy
import subprocess
import sys
from fractions import Fraction

assert run_python_blocks([]) == 0
lint_pseudocode_blocks()
ROOT = CHAPTER.parent.parent

# ---- structure: twelve questions, 75 marks, the real paper's time, links to real chapters
marks = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", TEXT, re.M)]
assert marks == [7, 6, 6, 5, 7, 6, 6, 5, 8, 6, 5, 8], marks
assert sum(marks) == 75 and len(marks) == 12 and all(4 <= m <= 9 for m in marks)
assert "@time 1 h 30 min" in TEXT and "**1 hour 30 minutes**" in TEXT
assert Fraction(75 * 6, 5) == 90 and "1.2 minutes per mark" in TEXT and "a 5-mark question deserves about 6 minutes" in TEXT
assert "Calculators must not be used" in TEXT and "No marks will be awarded for using brand names" in TEXT
ids = {c["id"] for c in json.loads((ROOT / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert len(re.findall(r"^Q: \[\d+ marks\] \(#cs\.\w+\)", TEXT, re.M)) == 12
assert TEXT.rstrip().endswith("Next: [Mock Paper 4: Practical](#cs.mock.p4)") and "cs.mock.p4" in ids
# each question's part marks add up to its total, and its [B1] count equals it
for block in re.findall(r"^:::try\n(.*?)^:::$", TEXT, re.M | re.S):
    q, a = block.split("\nA:", 1)
    total = int(re.match(r"Q: \[(\d+) marks\]", q).group(1))
    parts = [int(x) for x in re.findall(r"\[(\d+)\]\s*$", q, re.M)]
    assert sum(parts) == total, (total, parts)
    assert len(re.findall(r"\[B1\]", a)) == total, (total, len(re.findall(r"\[B1\]", a)))


# ---- Q1: floating point, 10-bit mantissa, 4-bit exponent, point after the first mantissa bit
def twos(bits):
    v = int(bits, 2)
    return v - (1 << len(bits)) if bits[0] == "1" else v


def fp_value(mant, exp):
    return Fraction(twos(mant), 2 ** (len(mant) - 1)) * Fraction(2) ** twos(exp)


assert fp_value("0101100000", "0011") == Fraction(11, 2) == Fraction(55, 10)          # 5.5
assert fp_value("0101100000", "0011") == Fraction(11, 16) * 8
assert fp_value("1001100000", "0010") == Fraction(-13, 4)                              # -3.25
assert twos("1001100000") == -416 and -416 / 512 == -0.8125 and -0.8125 * 4 == -3.25
assert (~int("0110100000", 2) + 1) & 0x3FF == int("1001100000", 2)
assert format((~int("0110100000", 2)) & 0x3FF, "010b") == "1001011111"
assert bin(int("11.01".replace(".", ""), 2)) == "0b1101" and Fraction(13, 4) == Fraction(13, 16) * 4
assert "1001100000"[:2] == "10" and "0110100000"[:2] == "01"
assert fp_value("0001101100", "0100") == fp_value("0110110000", "0010") == Fraction(27, 8)  # 3.375
assert "0001101100"[:2] == "00" and "0110110000"[:2] == "01" and twos("0010") == 4 - 2

# ---- Q2: nothing to compute; the statements must be as printed
for s in ("TYPE Weekday = (Mon, Tue, Wed, Thu, Fri)", "DECLARE LessonDay : Weekday", "LessonDay ← Wed",
          "TYPE DayPointer = ^Weekday", "DECLARE NextLesson : DayPointer", "NextLesson ← ^LessonDay"):
    assert s in TEXT, s

# ---- Q4: four-stage pipeline, six instructions
assert 6 * 4 == 24 and 4 + (6 - 1) == 9

# ---- Q5: truth table, K-map, simplified expression
rows = [tuple(int(c) for c in r) for r in re.findall(r"^\| ([01]) \| ([01]) \| ([01]) \| ([01]) \|$", TEXT, re.M)]
assert len(rows) == 8, rows
table = {(a, b, c): x for a, b, c, x in rows}
assert sorted(table) == list(itertools.product((0, 1), repeat=3)) and sum(table.values()) == 5
for a, b, c in table:
    assert table[(a, b, c)] == int((not b) or (a and c)), (a, b, c)      # X = NOT B OR (A AND C)
gray = [(0, 0), (0, 1), (1, 1), (1, 0)]
kmap = [[table[(a, b, c)] for b, c in gray] for a in (0, 1)]
assert kmap == [[1, 1, 0, 0], [1, 1, 1, 0]]
assert "| 0 | 1 | 1 | 0 | 0 |" in TEXT and "| 1 | 1 | 1 | 1 | 0 |" in TEXT
assert "X = NOT B OR (A AND C)" in TEXT
# J = 1, K = 1 toggles: the next state of a JK flip-flop
def jk(q, j, k):
    return int((j and not q) or (not k and q))
assert jk(0, 1, 1) == 1 and jk(1, 1, 1) == 0 and jk(0, 1, 0) == 1 and jk(1, 0, 1) == 0


# ---- Q6: shortest remaining time, one millisecond at a time
def srt(procs):
    rem = {p: b for p, (a, b) in procs.items()}
    finish, t, run = {}, 0, []
    while rem:
        ready = [p for p in rem if procs[p][0] <= t]
        p = min(ready, key=lambda x: (rem[x], procs[x][0]))
        run.append(p)
        rem[p] -= 1
        t += 1
        if rem[p] == 0:
            del rem[p]
            finish[p] = t
    return finish, run


PROCS = {"P1": (0, 6), "P2": (1, 4), "P3": (2, 1)}
fin, run_order = srt(PROCS)
assert fin == {"P3": 3, "P2": 6, "P1": 11}, fin
assert run_order == ["P1", "P2", "P3", "P2", "P2", "P2", "P1", "P1", "P1", "P1", "P1"]
waits = {p: fin[p] - PROCS[p][0] - PROCS[p][1] for p in PROCS}
assert waits == {"P1": 5, "P2": 1, "P3": 0} and Fraction(sum(waits.values()), 3) == 2
for needle in ("| P1 | 0 | 6 |", "| P2 | 1 | 4 |", "| P3 | 2 | 1 |", "finishes at 3 ms", "finishes at 6 ms", "finishes at 11 ms"):
    assert needle in TEXT, needle

# ---- Q7: BNF with the printed rules, and RPN
def bnf_valid(s, minute_rule):
    return re.fullmatch(r"(0\d|1\d):" + minute_rule, s) is not None


MIN = r"[0-5]\d"
assert bnf_valid("07:45", MIN) and not bnf_valid("12:60", MIN) and bnf_valid("12:59", MIN) and not bnf_valid("24:00", MIN)
assert "<minute> ::= 0<digit> | 1<digit> | 2<digit> | 3<digit> | 4<digit> | 5<digit>" in TEXT


def rpn(expr):
    stack, snaps = [], []
    for item in expr.split():
        if item in "+-*/":
            b, a = stack.pop(), stack.pop()
            stack.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b}[item])
        else:
            stack.append(int(item))
        snaps.append(list(stack))
    return stack, snaps


st, snaps = rpn("9 2 - 4 *")
assert st == [28] and snaps == [[9], [9, 2], [7], [7, 4], [28]]
for row in ("| 9 | 9 |", "| 2 | 9, 2 |", "| - | 7 |", "| 4 | 7, 4 |", "| * | 28 |"):
    assert row in TEXT, row

# ---- Q9: the graph figure, Dijkstra's table
res = subprocess.run([sys.executable, str(ROOT / "data" / "cs.mock34_figs.py")], capture_output=True, text=True)
assert res.returncode == 0 and res.stdout.startswith("ok"), res.stderr[-400:]
svg = (ROOT / "data" / "cs.mock34_figs.txt").read_text(encoding="utf-8").split("### graph\n")[1].strip()
assert svg in TEXT
FIG = runpy.run_path(str(ROOT / "data" / "cs.mock34_figs.py"))
dist, prev, order = FIG["dijkstra"]("P")
assert [n for n, _ in order] == ["P", "Q", "R", "S", "T", "U"]
assert "| Q | 3 | P |\n| R | | |" in TEXT                   # the two rows printed in the question
for n, d, p in (("R", 4, "Q"), ("S", 8, "R"), ("T", 11, "S"), ("U", 15, "T")):
    assert dist[n] == d and prev[n] == p
    assert f"| {n} | {d} | {p} |" in TEXT
assert 3 + 1 + 4 + 3 + 4 == 15 and 3 + 1 == 4 < 5 and 4 + 4 == 8 < 3 + 7 and 8 + 3 == 11 < 4 + 9 and 11 + 4 == 15 < 8 + 8
assert "P, Q, R, S, T, U" in TEXT and "its length is 15 km" in TEXT
for n, c in (("PQ", 3), ("PR", 5), ("QR", 1), ("QS", 7), ("RS", 4), ("RT", 9), ("ST", 3), ("SU", 8), ("TU", 4)):
    assert f"{n[0]} to {n[1]} {c}" in TEXT, n

# ---- Q10: the binary tree in arrays and FindNode
_h, tbl = table_after("| Index | `LeftPtr`")
assert _h == ["Index", "`LeftPtr`", "`Data`", "`RightPtr`"] and [int(r[0]) for r in tbl] == list(range(1, 8))
LeftPtr = [0] + [int(r[1]) for r in tbl]
Data = [0] + [int(r[2]) if r[2] else 0 for r in tbl]  # node 7 is unused
RightPtr = [0] + [int(r[3]) for r in tbl]
RootPointer = 1
# the tree is what inserting 40, 25, 60, 31, 18, 52 into an empty tree builds
L2, D2, R2, nxt = [0] * 8, [0] * 8, [0] * 8, 1
for v in (40, 25, 60, 31, 18, 52):
    D2[nxt] = v
    if nxt > 1:
        cur = 1
        while True:
            side = L2 if v < D2[cur] else R2
            if side[cur] == 0:
                side[cur] = nxt
                break
            cur = side[cur]
    nxt += 1
assert (L2, D2[:7] + [0], R2) == (LeftPtr, Data[:7] + [0], RightPtr), (L2, D2, R2)


def find_node(target):
    visited, current = [], RootPointer
    while current != 0 and Data[current] != target:       # as in the mark scheme
        visited.append(current)
        current = LeftPtr[current] if target < Data[current] else RightPtr[current]
    if current != 0:
        visited.append(current)
    return visited, current


assert find_node(52) == ([1, 3, 6], 6) and find_node(35) == ([1, 2, 4], 0)
assert find_node(40) == ([1], 1) and find_node(18) == ([1, 2, 5], 5) and find_node(99) == ([1, 3], 0)
for s in ("Current ← RootPointer", "WHILE Current <> 0 AND Data[Current] <> Target", "Current ← LeftPtr[Current]",
          "Current ← RightPtr[Current]", "RETURN Current"):
    assert s in TEXT, s

# ---- Q12: the animal shelter knowledge base (the real Paper 3 form: 15 numbered clauses, three parts, NOT last)
PLQ = runpy.run_path(str(ROOT / "data" / "cs.prolog_sim.py"))["query"]
clauses = re.findall(r"^\| (\d+) `([^`]+)` \|", TEXT, re.M)
kb_rows = [(int(n), c) for n, c in clauses if c.endswith(").") and (c.startswith(("person(", "pet(", "allergic(", "visited(")))]
assert [n for n, _ in kb_rows] == list(range(1, 16)), kb_rows
KB = "\n".join(c for _, c in kb_rows) + "\n"
RULE = "may_adopt(Person, Pet) IF person(Person) AND pet(Pet) AND NOT allergic(Person, Pet).\n"
assert RULE.strip() in TEXT
ans = lambda kb, goal, var: [a[var] for a in PLQ(kb, goal)]
assert ans(KB, "allergic(kwame, X)", "X") == ["luna", "pepper"]            # the printed example
assert ans(KB, "visited(ines, X)", "X") == ["milo", "pepper"]              # part (b)
assert "(b) X = milo, pepper" in TEXT
assert ans(KB + RULE, "may_adopt(kwame, X)", "X") == ["milo", "biscuit"]
assert ans(KB + RULE, "may_adopt(zara, X)", "X") == ["luna", "biscuit", "pepper"]
NEW = "person(omar).\npet(rosie).\nvisited(omar, rosie).\n"
assert ans(KB + NEW + RULE, "may_adopt(omar, X)", "X") == ["milo", "luna", "biscuit", "pepper", "rosie"]
assert PLQ(KB + RULE, "may_adopt(kwame, luna)") == []                      # NOT fails for an allergy
WRONG = "may_adopt(P, Q) IF NOT allergic(P, Q) AND person(P) AND pet(Q)."   # NOT first: no results
assert PLQ(KB + WRONG, "may_adopt(P, Q)") == []

print("ok")

