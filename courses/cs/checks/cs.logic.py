# checks/cs.logic.py: runs every Python block, parses every logic expression and checks every truth table,
# against the chapter (rows, working columns, spot the error, exam answers).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.logic"

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



# ---------------------------------------------------------------------------------------------
# A small parser for the chapter's expressions: words AND OR NOT NAND NOR XOR, brackets, letters.
# NOT applies to the next item only; two different gates must be separated by brackets.
# ---------------------------------------------------------------------------------------------
GATES = {"AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "NAND": lambda a, b: 1 - (a & b),
         "NOR": lambda a, b: 1 - (a | b), "XOR": lambda a, b: a ^ b}


def evaluate(expr, env):
    toks = re.findall(r"\(|\)|[A-Za-z]+", expr)
    pos = 0

    def peek():
        return toks[pos] if pos < len(toks) else None

    def take():
        nonlocal pos
        pos += 1
        return toks[pos - 1]

    def operand():
        t = take()
        if t == "NOT":
            return 1 - operand()
        if t == "(":
            v = chain()
            assert take() == ")", f"unbalanced brackets in {expr!r}"
            return v
        assert t in env, f"unknown name {t!r} in {expr!r}"
        return env[t]

    def chain():
        v = operand()
        op = None
        while peek() in GATES:
            o = take()
            assert op in (None, o) and (o in ("AND", "OR") or op is None), f"ambiguous {expr!r}"
            op = o
            v = GATES[o](v, operand())
        return v

    v = chain()
    assert pos == len(toks), f"trailing text in {expr!r}"
    return v


def rows(names):
    n = len(names)
    return [dict(zip(names, [(i >> (n - 1 - k)) & 1 for k in range(n)])) for i in range(2 ** n)]


def table_rows(marker):
    """Header and rows (as lists of strings) of the first table after the marker."""
    start = TEXT.index(marker)
    out = []
    started = False
    for line in TEXT[start:].split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                out.append(cells)
            started = True
        elif started:
            break
    return out[0], out[1:]


def check_table(marker, inputs, columns):
    """columns: {column index: expression string}; also checks the row order and the row count."""
    header, body = table_rows(marker)
    assert len(body) == 2 ** len(inputs), f"{marker}: {len(body)} rows"
    for env, row in zip(rows(inputs), body):
        assert [int(c) for c in row[:len(inputs)]] == [env[k] for k in inputs], f"{marker}: row order {row}"
        for idx, f in columns.items():
            want = evaluate(f, env)
            assert int(row[idx]) == want, f"{marker}: column {idx} of row {row}: want {want}"


blocks = run_python_blocks([])
assert blocks == 2, f"expected 2 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 0

# the five two-input gates
header, body = table_rows("| A | B | A AND B | A OR B | A NAND B | A NOR B | A XOR B |")
for env, row in zip(rows("AB"), body):
    assert [int(c) for c in row[2:]] == [evaluate(f"A {g} B", env) for g in ("AND", "OR", "NAND", "NOR", "XOR")]
assert [GATES[g](1, 1) for g in ("AND", "OR", "NAND", "NOR", "XOR")] == [1, 1, 0, 0, 0]      # try Q1
assert 2 ** 3 == 8 and 2 ** 4 == 16 and 2 ** 5 == 32 and 2 ** 2 == 4 and 2 ** 1 == 2

# NAND is not "NOT A AND NOT B": that is NOR
for env in rows("AB"):
    assert evaluate("(NOT A) AND (NOT B)", env) == evaluate("A NOR B", env)
assert any(evaluate("(NOT A) AND (NOT B)", env) != evaluate("A NAND B", env) for env in rows("AB"))

# worked example: working columns
check_table("| A | B | C | P = A AND B | Q = NOT C | X = P OR Q |", "ABC",
            {3: "A AND B", 4: "NOT C", 5: "(A AND B) OR NOT C"})
assert sum(evaluate("(A AND B) OR NOT C", e) for e in rows("ABC")) == 5

# NOT binds to the next item only
e = {"A": 1, "B": 0}
assert (evaluate("NOT A AND B", e), evaluate("NOT (A AND B)", e)) == (0, 1)
assert evaluate("NOT A AND B", e) == evaluate("(NOT A) AND B", e)

# evaluating an expression
assert evaluate("(A OR B) AND NOT C", {"A": 0, "B": 1, "C": 0}) == 1
assert evaluate("(A OR B) AND NOT C", {"A": 1, "B": 0, "C": 1}) == 0

# circuit to expression: the four-gate XOR
check_table("| A | B | P = A OR B | Q = A AND B | R = NOT Q | X = P AND R |", "AB",
            {2: "A OR B", 3: "A AND B", 4: "NOT (A AND B)", 5: "(A OR B) AND NOT (A AND B)"})
for env in rows("AB"):
    assert evaluate("(A OR B) AND NOT (A AND B)", env) == evaluate("A XOR B", env)

# alarm
check_table("| A | B | C | P = A AND B | X = P OR C |", "ABC", {3: "A AND B", 4: "(A AND B) OR C"})
assert sum(evaluate("(A AND B) OR C", e) for e in rows("ABC")) == 5
assert all(evaluate("(A AND B) OR C", dict(e, C=1)) == 1 for e in rows("AB"))

# kiln
check_table("| A | B | C | P | Q | X |", "ABC", {3: "A AND B", 4: "NOT C", 5: "(A AND B) AND NOT C"})
assert [e for e in rows("ABC") if evaluate("(A AND B) AND NOT C", e)] == [{"A": 1, "B": 1, "C": 0}]

# sum of products
check_table("| A | B | X |", "AB", {2: "(NOT A AND B) OR (A AND NOT B)"})
THREE = "((NOT A AND NOT B) AND C) OR ((A AND NOT B) AND NOT C) OR ((A AND B) AND NOT C)"
check_table("| A | B | C | X |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 1 |", "ABC", {3: THREE})
ones = [f"{e['A']}{e['B']}{e['C']}" for e in rows("ABC") if evaluate(THREE, e)]
assert ones == ["001", "100", "110"]
assert evaluate("(A AND NOT B) AND NOT C", {"A": 1, "B": 0, "C": 0}) == 1
for e in rows("ABC"):
    assert evaluate("((A AND NOT B) AND NOT C) OR ((A AND B) AND NOT C)", e) == evaluate("A AND NOT C", e)

# spot the error: correct P and X for (A XOR B) AND C, and the student's follow-through column
header, body = table_rows("| A | B | C | P | X |\n|---|---|---|---|---|\n| 0 | 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 0 | 0 |")
good_p = [evaluate("A XOR B", e) for e in rows("ABC")]
good_x = [evaluate("(A XOR B) AND C", e) for e in rows("ABC")]
assert good_p == [0, 0, 1, 1, 1, 1, 0, 0] and good_x == [0, 0, 0, 1, 0, 1, 0, 0]
student_p = [int(r[3]) for r in body]
student_x = [int(r[4]) for r in body]
assert student_p == [0, 0, 1, 1, 1, 1, 1, 1]
assert [p & e["C"] for p, e in zip(student_p, rows("ABC"))] == student_x          # follow-through holds
assert [i for i in range(8) if student_p[i] != good_p[i]] == [6, 7]

# try yourself
check_table("| A | B | NOT A | X |", "AB", {2: "NOT A", 3: "NOT A OR B"})
for e in rows("ABC"):
    assert evaluate("NOT (A OR B) AND C", e) == evaluate("(A NOR B) AND C", e)
assert evaluate("NOT (A OR B)", {"A": 0, "B": 0}) == 1 and evaluate("A NOR B", {"A": 1, "B": 0}) == 0

# exam practice
check_table("| A | B | C | P = A NAND B | Q = B NOR C | X = P XOR Q |", "ABC",
            {3: "A NAND B", 4: "B NOR C", 5: "(A NAND B) XOR (B NOR C)"})
TERM2 = "((NOT A AND B) AND NOT C) OR ((A AND B) AND C)"
check_table("| A | B | C | X |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 0 |\n| 0 | 1 | 0 | 1 |", "ABC", {3: TERM2})
assert [f"{e['A']}{e['B']}{e['C']}" for e in rows("ABC") if evaluate(TERM2, e)] == ["010", "111"]
check_table("| A | B | C | P | Q | X |\n|---|---|---|---|---|---|\n| 0 | 0 | 0 | 0 | 1 | 0 |\n| 0 | 0 | 1 | 0 | 0 | 0 |\n| 0 | 1 | 0 | 1 | 1 | 1 |", "ABC",
            {3: "A OR B", 4: "NOT C", 5: "(A OR B) AND NOT C"})
check_table("| A | B | NOT A | NOT B | (NOT A) OR (NOT B) | A NAND B |", "AB",
            {2: "NOT A", 3: "NOT B", 4: "(NOT A) OR (NOT B)", 5: "A NAND B"})
EXACT2 = "((NOT A AND B) AND C) OR ((A AND NOT B) AND C) OR ((A AND B) AND NOT C)"
check_table("| A | B | C | X |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 0 |\n| 0 | 1 | 0 | 0 |\n| 0 | 1 | 1 | 1 |", "ABC", {3: EXACT2})
assert all(evaluate(EXACT2, e) == (e["A"] + e["B"] + e["C"] == 2) for e in rows("ABC"))
# sprinkler expression (described circuit): NOT R, AND with D, OR with M
for e in rows("DRM"):
    assert evaluate("(D AND NOT R) OR M", e) == (e["M"] | (e["D"] & (1 - e["R"])))

# stretch 1: NAND only
def nand(a, b):
    return 1 - (a & b)

for a in (0, 1):
    assert nand(a, a) == 1 - a
    for b in (0, 1):
        assert nand(nand(a, b), nand(a, b)) == a & b
        assert nand(nand(a, a), nand(b, b)) == a | b
# stretch 2: half adder
check_table("| A | B | Sum | Carry |", "AB", {2: "A XOR B", 3: "A AND B"})
for a in (0, 1):
    for b in (0, 1):
        assert (a ^ b) + 2 * (a & b) == a + b

print("ok")
