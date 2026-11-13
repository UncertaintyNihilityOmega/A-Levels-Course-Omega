# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.datatypes"

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


INPUTS = [("How many tickets?", ["3"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 10, f"expected 10 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 32

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert sum(range(2, 9, 2)) == 20
assert (17 // 5, 17 % 5) == (3, 2)

# ---------------------------------------------------------------------------------------------
# Data types: string comparison and literals
# ---------------------------------------------------------------------------------------------
assert "10" < "9"
assert "Ali" < "Ben" < "Mia" and "zoe" > "Zoe" and "zoe" > "Mia"
assert 4.75 * 3 == 14.25

# ---------------------------------------------------------------------------------------------
# Arrays: bounds and element counts
# ---------------------------------------------------------------------------------------------
def count(lower, upper):
    return upper - lower + 1

assert count(1, 7) == 7 and count(0, 24) == 25 and count(0, 9) == 10 and 3 * 4 == 12

# Temps example (pseudocode translated, 1-based)
TEMPS = [None, 31, 33, 30, 28, 29, 32, 34]
assert TEMPS[4] == 28
total, highest, high_day, changes = 0, TEMPS[1], 1, [TEMPS[1]]
for index in range(1, 8):
    total += TEMPS[index]
    if TEMPS[index] > highest:
        highest, high_day = TEMPS[index], index
        changes.append((highest, index))
assert (total, total / 7, highest, high_day) == (217, 31.0, 34, 7)
assert changes == [31, (33, 2), (34, 7)]

# Freezer warning: starting the maximum at 0 gives a wrong answer
freezer = [-18, -17, -19]
assert max([0] + freezer) == 0 and max(freezer) == -17

# Sales example
SALES = [[12, 15, 9, 14], [8, 11, 13, 10], [20, 17, 16, 19]]
assert SALES[2 - 1][3 - 1] == 13
stall_totals = [sum(r) for r in SALES]
week_totals = [sum(SALES[r][c] for r in range(3)) for c in range(4)]
assert stall_totals == [50, 42, 72] and week_totals == [40, 43, 38, 43]
best_total, best_week = -1, 0
for c in range(4):
    if week_totals[c] > best_total:
        best_total, best_week = week_totals[c], c + 1
assert best_week == 2

# ---------------------------------------------------------------------------------------------
# Linear search trace (pseudocode semantics) against the chapter's trace table
# ---------------------------------------------------------------------------------------------
NAMES = [None, "Amara", "Bilal", "Chen", "Dina", "Emeka", "Farah", "Goran", "Hana"]


def linear_search(target, array=NAMES):
    found, index, compared = False, 1, []
    while not found and index <= len(array) - 1:
        compared.append(array[index])
        if array[index] == target:
            found = True
        else:
            index += 1
    return found, index, compared


found, index, compared = linear_search("Emeka")
assert (found, index, len(compared)) == (True, 5, 5)
header, rows = table_after("| SearchName | Found |")
assert column_values(header, rows, "Index") == ["1", "2", "3", "4", "5"]
assert column_values(header, rows, "Names[Index] compared") == compared
assert column_values(header, rows, "Found") == ["FALSE", "TRUE"]
assert column_values(header, rows, "OUTPUT") == ["Emeka found at position 5"]
found, index, compared = linear_search("Zara")
assert (found, index, len(compared)) == (False, 9, 8)

# ---------------------------------------------------------------------------------------------
# Bubble sort: pass table, comparison counts
# ---------------------------------------------------------------------------------------------
def basic_bubble(values):
    v, comps = list(values), 0
    for _ in range(len(v) - 1):
        for j in range(len(v) - 1):
            comps += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
    return v, comps


def efficient_bubble(values):
    v, boundary, comps, passes = list(values), len(values) - 1, 0, []
    while True:
        no_swaps = True
        for j in range(boundary):
            comps += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                no_swaps = False
        boundary -= 1
        passes.append(list(v))
        if no_swaps or boundary == 0:
            return v, comps, passes


start = [41, 17, 33, 8, 25]
# the four single swaps of pass 1 described step by step
v = list(start)
steps = []
for j in range(4):
    if v[j] > v[j + 1]:
        v[j], v[j + 1] = v[j + 1], v[j]
    steps.append(list(v))
assert steps == [[17, 41, 33, 8, 25], [17, 33, 41, 8, 25], [17, 33, 8, 41, 25], [17, 33, 8, 25, 41]]
_, comps, passes = efficient_bubble(start)
assert comps == 10 == 4 + 3 + 2 + 1
assert passes == [[17, 33, 8, 25, 41], [17, 8, 25, 33, 41], [8, 17, 25, 33, 41], [8, 17, 25, 33, 41]]
header, rows = table_after("| After pass | Array |")
assert [r[1] for r in rows] == [", ".join(map(str, p)) for p in [start] + passes]
assert basic_bubble(start) == ([8, 17, 25, 33, 41], 16)
assert efficient_bubble([1, 2, 3, 4, 5])[1] == 4

# Spot the error: swapping without Temp loses a value
h = [172, 165]
h[0] = h[1]
h[1] = h[0]
assert h == [165, 165]

# ---------------------------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------------------------
nums = [4, 9, 2, 7, 5]
assert [x for x in nums if x % 2 == 1] == [9, 7, 5]
stock = [5, 0, 12, 3]
assert (stock[2], len(stock)) == (12, 4)
v = [6, 2, 9, 4, 1]
for j in range(4):
    if v[j] > v[j + 1]:
        v[j], v[j + 1] = v[j + 1], v[j]
assert v == [2, 6, 4, 1, 9]
ten = [None] + list(range(100, 110))      # 10 elements, 1-based
assert len(linear_search(105, ten)[2]) == 6     # at position 6: 6 comparisons
assert len(linear_search(999, ten)[2]) == 10    # not there: all 10 compared
marks = [[12, 18, 15], [9, 14, 11], [20, 17, 19], [13, 10, 16]]
assert sum(r[1] for r in marks) == 59 == 18 + 14 + 17 + 10

# ---------------------------------------------------------------------------------------------
# Exam practice Q4: trace of the efficient bubble sort, every assignment recorded per column
# ---------------------------------------------------------------------------------------------
cols = {k: [] for k in ["Boundary", "NoSwaps", "J", "Temp", "Data[1]", "Data[2]", "Data[3]", "Data[4]"]}
data = [None, 15, 3, 11, 7]
for i in range(1, 5):
    cols[f"Data[{i}]"].append(str(data[i]))
boundary = 3
cols["Boundary"].append("3")
while True:
    no_swaps = True
    cols["NoSwaps"].append("TRUE")
    for j in range(1, boundary + 1):
        cols["J"].append(str(j))
        if data[j] > data[j + 1]:
            temp = data[j]
            cols["Temp"].append(str(temp))
            data[j] = data[j + 1]
            cols[f"Data[{j}]"].append(str(data[j]))
            data[j + 1] = temp
            cols[f"Data[{j + 1}]"].append(str(data[j + 1]))
            no_swaps = False
            cols["NoSwaps"].append("FALSE")
    boundary -= 1
    cols["Boundary"].append(str(boundary))
    if no_swaps or boundary == 0:
        break
assert data[1:] == [3, 7, 11, 15]
header, rows = table_after("| Boundary | NoSwaps | J | Temp |")
for name, values in cols.items():
    assert column_values(header, rows, name) == values, f"Q4 column {name}: {values}"

# ---------------------------------------------------------------------------------------------
# Stretch 1: improved linear search on sorted data
# ---------------------------------------------------------------------------------------------
def sorted_search(codes, target):
    index, finished, comps = 0, False, 0
    while not finished and index < len(codes):
        comps += 1
        if codes[index] >= target:
            finished = True
        else:
            index += 1
    return (index + 1 if finished and codes[index] == target else None), comps


codes = list(range(5, 5005, 5))           # 1000 sorted codes
assert len(codes) == 1000
assert sorted_search(codes, 999999) == (None, 1000)
assert sorted_search(codes, codes[-1]) == (1000, 1000)
assert sorted_search(codes, 1) == (None, 1)
assert sorted_search(codes, 50) == (10, 10) and sorted_search(codes, 52) == (None, 11)

# Stretch 2: counting grades with ASC/CHR (pseudocode translated)
grades = ["B", "A", "C", "B", "E", "B", "A"]
count5 = [None, 0, 0, 0, 0, 0]
for g in grades:
    position = ord(g) - ord("A") + 1
    count5[position] += 1
assert count5[1:] == [2, 3, 1, 0, 1]
assert [chr(ord("A") + i - 1) for i in range(1, 6)] == list("ABCDE")

print("ok")
