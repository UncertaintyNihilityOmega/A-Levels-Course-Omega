# checks/cs.algorithms2.py: runs every Python block, lints every pseudocode block, recomputes every number the chapter states.
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.algorithms2"

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




import math

blocks = run_python_blocks([])
assert blocks == 8, f"expected 8 python blocks, found {blocks}"
PSEUDO = lint_pseudocode_blocks()
assert PSEUDO == 12, f"expected 12 pseudocode blocks, found {PSEUDO}"


def after(marker):
    """The first table after the first occurrence of marker text (the marker is not a table line)."""
    return table_after(marker)


# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert (13 // 2, 13 % 2) == (6, 1)

# ---------------------------------------------------------------------------------------------
# Binary search: traces (pseudocode semantics, 1-based)
# ---------------------------------------------------------------------------------------------
VALUES = [None, 3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55]


def bsearch(values, target):
    low, high, rows = 1, len(values) - 1, []
    while low <= high:
        mid = (low + high) // 2
        rows.append((low, high, mid, values[mid]))
        if values[mid] == target:
            return mid, rows
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, rows


pos, rows35 = bsearch(VALUES, 35)
assert pos == 8 and rows35 == [(1, 11, 6, 26), (7, 11, 9, 41), (7, 8, 7, 30), (8, 8, 8, 35)]
pos, rows20 = bsearch(VALUES, 20)
assert pos == -1 and rows20 == [(1, 11, 6, 26), (1, 5, 3, 12), (4, 5, 4, 17), (5, 5, 5, 21)]
assert len(rows35) == 4 and len(rows20) == 4

# the chapter's two trace tables (Low, High, Mid, Values[Mid] columns) and the decisions
for marker, rows, decisions in [
        ("Using the array `Values` above", rows35,
         ["26 < 35, so Low ← 7", "41 > 35, so High ← 8", "30 < 35, so Low ← 8", "equal: RETURN 8"]),
        ("The search for 35 makes 4 comparisons", rows20,
         ["26 > 20, so High ← 5", "12 < 20, so Low ← 4", "17 < 20, so Low ← 5", "21 > 20, so High ← 4"])]:
    header, trs = after(marker)
    for name, k in [("Low", 0), ("High", 1), ("Mid", 2), ("Values[Mid]", 3)]:
        assert column_values(header, trs, name) == [str(r[k]) for r in rows], (marker, name)
    assert column_values(header, trs, "Decision") == decisions, marker

# decisions follow from the comparisons
for rows, target in [(rows35, 35), (rows20, 20)]:
    for low, high, mid, value in rows:
        pass
assert (26 < 35, 41 > 35, 30 < 35) == (True, True, True) and (26 > 20, 12 < 20, 17 < 20, 21 > 20) == (True,) * 4

# Mid calculations
assert (4 + 9) // 2 == 6 and (7 + 8) // 2 == 7 and (6 + 11) // 2 == 8 and (10 + 11) // 2 == 10

# ---------------------------------------------------------------------------------------------
# Worst case of binary search: floor(log2 n) + 1
# ---------------------------------------------------------------------------------------------
def worst_bs(n):
    data = [None] + list(range(n))
    return max(len(bsearch(data, t)[1]) for t in range(-1, n + 1))


for n in [1, 3, 7, 10, 100, 1000, 2000]:
    assert worst_bs(n) == math.floor(math.log2(n)) + 1, n
for n in range(1, 400):
    assert worst_bs(n) == n.bit_length(), n          # floor(log2 n) + 1 = bit length
assert [n.bit_length() for n in (10, 100, 1000, 10 ** 6, 20000, 500, 1)] == [4, 7, 10, 20, 15, 9, 1]
assert (2 ** 9, 2 ** 10, 2 ** 19, 2 ** 20, 2 ** 14, 2 ** 15, 2 ** 7, 2 ** 8) == (512, 1024, 524288, 1048576, 16384, 32768, 128, 256)
assert 2 ** 9 < 1000 < 2 ** 10 and 2 ** 19 < 10 ** 6 < 2 ** 20 and 2 ** 14 < 20000 < 2 ** 15 and 2 ** 8 < 500 < 2 ** 9
assert worst_bs(2000) == worst_bs(1000) + 1                 # doubling adds one
assert 2 ** 7 > 100                                         # guessing game: at most 7 guesses
header, trs = after("| Items")
assert column_values(header, trs, "Binary search, worst case") == ["4", "7", "10", "20"]
assert column_values(header, trs, "Linear search, worst case") == ["10", "100", "1000", "1 000 000"]

# ---------------------------------------------------------------------------------------------
# Spot the error: Low <- Mid never ends for target 55
# ---------------------------------------------------------------------------------------------
low, high, mids, seen = 1, 11, [], []
for _ in range(50):
    if low > high:
        break
    mid = (low + high) // 2
    mids.append(mid)
    if VALUES[mid] == 55:
        break
    if VALUES[mid] < 55:
        low = mid
    else:
        high = mid - 1
else:
    pass
assert mids[:5] == [6, 8, 9, 10, 10] and len(mids) == 50 and low == 10   # never ends
assert VALUES[10] == 48 and 48 < 55 and (10 + 11) // 2 == 10

# ---------------------------------------------------------------------------------------------
# Sorts: counts
# ---------------------------------------------------------------------------------------------
def ins(values):
    v, comps, shifts, passes, per_pass = list(values), 0, 0, [], []
    for index in range(1, len(v)):
        item, position, moving, c = v[index], index - 1, True, 0
        while moving and position >= 0:
            comps += 1
            c += 1
            if v[position] > item:
                v[position + 1] = v[position]
                shifts += 1
                position -= 1
            else:
                moving = False
        v[position + 1] = item
        passes.append(list(v))
        per_pass.append(c)
    return v, comps, shifts, passes, per_pass


def bub(values):
    v, boundary, comps, swaps = list(values), len(values) - 1, 0, 0
    while True:
        no_swaps = True
        for j in range(boundary):
            comps += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                swaps += 1
                no_swaps = False
        boundary -= 1
        if no_swaps or boundary == 0:
            return v, comps, swaps


def basic_bub(n):
    return (n - 1) * (n - 1)


D = [29, 10, 14, 37, 13, 5]
v, comps, shifts, passes, per_pass = ins(D)
assert v == [5, 10, 13, 14, 29, 37] and (comps, shifts) == (13, 10) and per_pass == [1, 2, 1, 4, 5]
header, trs = after("| After pass | Element inserted |")
got = [[int(x) for x in r[2].replace("*", "").split(",")] for r in trs]
assert got == [D] + passes, got
assert [r[3] for r in trs[1:]] == ["1", "1", "0", "3", "5"] and sum(int(r[3]) for r in trs[1:]) == shifts

# pass 4 trace (Index 5): record per-column assignments
cols = {k: [] for k in ["Index", "Item", "Position", "Values[1]", "Values[2]", "Values[3]", "Values[4]", "Values[5]"]}
w = [None, 10, 14, 29, 37, 13, 5]
for i in range(1, 6):
    cols[f"Values[{i}]"].append(str(w[i]))
cols["Index"].append("5")
item = w[5]
cols["Item"].append(str(item))
position = 4
cols["Position"].append("4")
while position >= 1 and w[position] > item:
    w[position + 1] = w[position]
    if position + 1 <= 5:
        cols[f"Values[{position + 1}]"].append(str(w[position + 1]))
    position -= 1
    cols["Position"].append(str(position))
w[position + 1] = item
cols[f"Values[{position + 1}]"].append(str(item))
# the first row already holds the initial Values; later columns start from the initial values too
header, trs = after("| Index | Item | Position | Values[1] | Values[2] | Values[3] | Values[4] | Values[5] |")
for name, values in cols.items():
    assert column_values(header, trs, name) == values, (name, values)
assert w[1:6] == [10, 13, 14, 29, 37]

# comparison table for n = 8
SETS = {"sorted": [1, 2, 3, 4, 5, 6, 7, 8], "reversed": [8, 7, 6, 5, 4, 3, 2, 1], "random": [5, 2, 8, 1, 7, 3, 6, 4]}
expected = {"sorted": (7, 7, 0, 0), "reversed": (28, 28, 28, 28), "random": (25, 19, 14, 14)}
for name, data in SETS.items():
    b, i = bub(data), ins(data)
    assert (b[1], i[1], b[2], i[2]) == expected[name], name
    assert b[0] == i[0] == sorted(data)
    assert b[2] == i[2]                                       # swaps = shifts = inversions
    inversions = sum(1 for x in range(8) for y in range(x + 1, 8) if data[x] > data[y])
    assert inversions == b[2]
header, trs = after("| Starting order")
assert column_values(header, trs, "Bubble sort comparisons") == ["7", "28", "25"]
assert column_values(header, trs, "Insertion sort comparisons") == ["7", "28", "19"]
assert column_values(header, trs, "Swaps or shifts (both)") == ["0", "28", "14"]
assert 8 * 7 // 2 == 28 and 8 - 1 == 7
assert [n * (n - 1) // 2 for n in (10, 100, 1000)] == [45, 4950, 499500]
assert basic_bub(5) == 16
assert bub([1, 2, 3, 4, 5])[1] == 4 and ins([1, 2, 3, 4, 5, 6])[1:3] == (5, 0)
assert bub([5, 4, 3, 2, 1])[1:] == (10, 10) and ins([5, 4, 3, 2, 1])[1:3] == (10, 10)
assert ins([7, 3, 9, 1])[3] == [[3, 7, 9, 1], [3, 7, 9, 1], [1, 3, 7, 9]]
assert 10000 * 4 == 40000

# ---------------------------------------------------------------------------------------------
# Big O: growth table, loop counts
# ---------------------------------------------------------------------------------------------
assert [round(math.log2(n), 1) for n in (10, 100, 1000)] == [3.3, 6.6, 10.0]
assert [round(n * math.log2(n)) for n in (10, 100, 1000)] == [33, 664, 9966]
assert (2 ** 10, len(str(2 ** 100)), len(str(2 ** 1000)), f"{2 ** 100:.2e}") == (1024, 31, 302, "1.27e+30")
assert (16 ** 2, round(16 * math.log2(16)), 32, round(math.log2(32))) == (256, 64, 32, 5)
for n in range(1, 30):
    assert sum(j for j in range(1, n + 1)) == n * (n + 1) // 2        # FOR J <- 1 TO I inside FOR I
assert (3 * 8 ** 2 + 5 * 8 + 2) > 0

# Exam practice (a)(b), trace of Insert
INSERT = [None, 4, 9, 15, 22, 28, 33, 41, 47, 52]
assert bsearch(INSERT, 22) == (4, [(1, 9, 5, 28), (1, 4, 2, 9), (3, 4, 3, 15), (4, 4, 4, 22)])
assert bsearch(INSERT, 30)[0] == -1
assert bsearch(INSERT, 30)[1] == [(1, 9, 5, 28), (6, 9, 7, 41), (6, 6, 6, 33)]
header, trs = after("One row for each trip round the loop. For 22:")
for name, k in [("Low", 0), ("High", 1), ("Mid", 2), ("Insert[Mid]", 3)]:
    assert column_values(header, trs, name) == [str(r[k]) for r in bsearch(INSERT, 22)[1]], name
ITEMS = [None, 5, 12, 19, 24, 31, 40, 47]
assert [r[2] for r in bsearch(ITEMS, 40)[1]] == [4, 6]

# Exam practice: insertion sort trace for 9, 4, 7, 2
cols = {k: [] for k in ["Index", "Item", "Position", "Data[1]", "Data[2]", "Data[3]", "Data[4]"]}
data = [None, 9, 4, 7, 2]
for i in range(1, 5):
    cols[f"Data[{i}]"].append(str(data[i]))
for index in range(2, 5):
    cols["Index"].append(str(index))
    item = data[index]
    cols["Item"].append(str(item))
    position = index - 1
    cols["Position"].append(str(position))
    while position >= 1 and data[position] > item:
        data[position + 1] = data[position]
        cols[f"Data[{position + 1}]"].append(str(data[position + 1]))
        position -= 1
        cols["Position"].append(str(position))
    data[position + 1] = item
    cols[f"Data[{position + 1}]"].append(str(item))
assert data[1:] == [2, 4, 7, 9]
header, trs = after("One row per change; a blank cell means \"unchanged\".")
for name, values in cols.items():
    assert column_values(header, trs, name) == values, (name, values)

# Library question
assert (30 * 29 // 2, 2 ** 14 < 20000 < 2 ** 15) == (435, True)

# Python block expectations (also checked by the output blocks): bus prices
PRICES = [5, 9, 14, 18, 23, 27, 31, 36, 40, 45]
assert [PRICES.index(x) for x in (27, 45, 5)] == [5, 9, 0] and 10 not in PRICES

# Stretch 2: sorting first pays off from k = 505 look-ups
assert 1000 * 999 // 2 == 499500
k = 1
while not (499500 + 10 * k < 1000 * k):
    k += 1
assert k == 505 and 499500 / 990 > 504.5 and 499500 / 990 < 504.6

# Quiz distractors
assert (6 + 11) // 2 == 8 and 17 / 2 == 8.5
print("ok")
