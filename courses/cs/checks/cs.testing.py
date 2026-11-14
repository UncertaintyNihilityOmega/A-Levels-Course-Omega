# checks/cs.testing.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, test plans, amended programs).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.testing"

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


INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 8, f"expected 8 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 13

# ---------------------------------------------------------------------------------------------
# Error types: the demonstration values
# ---------------------------------------------------------------------------------------------
marks = [14, 17, 12]
assert marks[0] + marks[1] + marks[2] / len(marks) == 35.0 and sum(marks) / 3 != 35.0
for code, exc in (("marks[3]", IndexError), ("sum(marks) / (len(marks) - 3)", ZeroDivisionError),
                  ("int('12.5')", ValueError), ("'Total: ' + 5", TypeError), ("totl", NameError)):
    try:
        eval(code)
    except exc:
        pass
    else:
        raise AssertionError(f"{code} should raise {exc.__name__}")
try:
    compile("for count in range(1, 4)\n    print(count)", "program", "exec")
except SyntaxError:
    pass
else:
    raise AssertionError("syntax error expected")

# ---------------------------------------------------------------------------------------------
# Dry run of the mean of positive readings (pseudocode translated, 1-based)
# ---------------------------------------------------------------------------------------------
READINGS = [None, 4, -2, 6, 0, 5, -1]


def faulty_mean(readings=READINGS):
    total, count, rows = 0, 0, [("", "", "0", "0")]
    for index in range(1, 7):
        old_total = total
        if readings[index] > 0:
            total += readings[index]
        count += 1
        rows.append((str(index), str(readings[index]), str(total) if total != old_total else "", str(count)))
    return total / count, rows


mean, rows = faulty_mean()
assert mean == 2.5
header, table = table_after("| Index | Readings[Index] | Total | Count | Mean | OUTPUT |")
assert [r[:4] for r in table[:7]] == [list(r) for r in rows]
assert column_values(header, table, "Total") == ["0", "4", "10", "15"]
assert column_values(header, table, "Count") == ["0", "1", "2", "3", "4", "5", "6"]
assert column_values(header, table, "Mean") == ["2.5"] and column_values(header, table, "OUTPUT") == ["Mean of the positive readings: 2.5"]


def fixed_mean(readings):
    total = count = 0
    for r in readings:
        if r > 0:
            total += r
            count += 1
    return total / count if count > 0 else None


assert fixed_mean([4, -2, 6, 0, 5, -1]) == 5.0 == 15 / 3 and fixed_mean([-3, 0, -8]) is None

# ---------------------------------------------------------------------------------------------
# Grade function: white-box paths and black-box boundary table
# ---------------------------------------------------------------------------------------------
def grade(mark):
    if mark >= 70:
        return "Distinction"
    if mark >= 40:
        return "Pass"
    return "Fail"


def grade_slip(mark):
    if mark > 70:
        return "Distinction"
    if mark >= 40:
        return "Pass"
    return "Fail"


assert [grade(m) for m in (85, 55, 20)] == ["Distinction", "Pass", "Fail"]
assert [grade_slip(m) for m in (85, 55, 20)] == ["Distinction", "Pass", "Fail"]     # white-box tests miss the slip
assert grade_slip(70) == "Pass" != grade(70)                                         # the black-box test finds it
header, rows = table_after("| Test data | Expected result |")
assert [(int(r[0]), r[1]) for r in rows] == [(m, grade(m)) for m in (0, 39, 40, 69, 70, 100)]

# ---------------------------------------------------------------------------------------------
# ValidQuantity: pseudocode translated (IS_NUM, STR_TO_NUM, INT) against the test plan
# ---------------------------------------------------------------------------------------------
def is_num(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def valid_quantity(entry):
    if not is_num(entry):
        return False
    number = float(entry)
    if number != int(number):
        return False
    return number >= 1 and number <= 100


plan_tables = [t for t in re.findall(r"(\| Test \| Purpose \| Test data \| Type \| Expected result \| Actual result \|\n(?:\|.*\n)+)", TEXT)]
assert len(plan_tables) == 2
for chunk, nrows in zip(plan_tables, (5, 11)):
    assert len([ln for ln in chunk.strip().split("\n")]) == nrows
full = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in plan_tables[1].strip().split("\n")[2:]]
assert len(full) == 9
for number, purpose, data, kind, expected, actual in full:
    entry = "" if data == "(nothing typed)" else data
    want = {"Accepted": True, "Rejected": False}[expected]
    assert valid_quantity(entry) == want, f"test {number}: {data}"
    if kind == "normal" or kind == "extreme/boundary":
        assert want is True
    else:
        assert want is False and kind.startswith("abnormal")
    assert actual == ""
# the first (short) plan is the first three rows of the full plan
short = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in plan_tables[0].strip().split("\n")[2:]]
assert short == full[:3]


def valid_slip(entry):
    if not is_num(entry):
        return False
    number = float(entry)
    if number != int(number):
        return False
    return 1 < number <= 100


fails = [data for _, data, _ in [(1, "50", True), (2, "1", True), (3, "100", True), (4, "0", False), (5, "101", False),
                                   (6, "-20", False), (7, "12.5", False), (8, "ten", False), (9, "", False)]
         if valid_slip(data) != valid_quantity(data)]
assert fails == ["1"]
# the slip passes every test except the extreme one
assert all(valid_slip(d) == valid_quantity(d) for d in ["50", "100", "0", "101", "-20", "12.5", "ten", ""])

# Test data tables: 1 to 100 and the examples in the exam answers
assert all(valid_quantity(str(v)) for v in (1, 50, 100)) and not any(valid_quantity(str(v)) for v in (0, 101, -20))


def in_range(v, lo, hi):
    return lo <= v <= hi


assert in_range(5, 5, 18) and in_range(18, 5, 18) and not in_range(4, 5, 18) and not in_range(19, 5, 18) and in_range(12, 5, 18)
assert in_range(0, 0, 50) and in_range(50, 0, 50) and not in_range(51, 0, 50) and in_range(25, 0, 50)        # spot the error
assert in_range(0, 0, 8) and in_range(8, 0, 8) and not in_range(9, 0, 8) and in_range(4, 0, 8)              # exam Q4
assert in_range(1, 1, 20) and in_range(20, 1, 20) and not in_range(0, 1, 20) and not in_range(21, 1, 20) and in_range(10, 1, 20)
assert in_range(99, 10, 99) and not in_range(9, 10, 99) and not in_range(100, 10, 99) and in_range(50, 10, 99)

# ---------------------------------------------------------------------------------------------
# Amending a program (Prices): original and amended
# ---------------------------------------------------------------------------------------------
PRICES = [None, 3.5, 12.0, 8.25, 20.0, 4.75, 15.5, 9.0, 11.0]
total, count = 0.0, 0
for i in range(1, 9):
    total += PRICES[i]
    if PRICES[i] > 10.0:
        count += 1
assert (total, count) == (84.0, 4)
total, count, highest, high_pos = 0.0, 0, PRICES[1], 1
for i in range(1, 9):
    total += PRICES[i]
    if PRICES[i] > 10.0:
        count += 1
    if PRICES[i] > highest:
        highest, high_pos = PRICES[i], i
if total > 80.0:
    total -= 5.0
assert (total, count, high_pos, highest) == (79.0, 4, 4, 20.0)

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
# Q2: the three errors in the Marks program, shown by translation
def marks_program(marks, bug_index=False, divisor=5, threshold_ok=True):
    total = 0
    for index in range(1, 6):
        total += marks[index + 1 if bug_index else index]
    mean = total / divisor
    return "Pass" if mean >= 50 else "Fail"


M = [None, 20, 30, 40, 50, 60]
try:
    marks_program(M, bug_index=True)
except IndexError:
    pass
else:
    raise AssertionError("Marks[6] should be outside the array")
assert marks_program(M, divisor=5) == "Fail" and marks_program(M, divisor=4) == "Pass"     # mean 40.0 and 50.0
assert sum(M[1:]) / 5 == 40.0 and sum(M[1:]) / 4 == 50.0

# Q7: digit sum with the faulty condition
def digit_sum(number, limit):
    total = 0
    rows = [(number, 0)]
    while number > limit:
        total += number % 10
        number //= 10
        rows.append((number, total))
    return total, rows


total, rows = digit_sum(472, 10)
assert total == 9 and rows == [(472, 0), (47, 2), (4, 9)]
header, table = table_after("| Number | Sum | OUTPUT |")
assert [(int(r[0]), int(r[1])) for r in table[:3]] == rows and table[3][2] == "9"
total, rows = digit_sum(472, 0)
assert total == 13 and [r[1] for r in rows] == [0, 2, 9, 13] and sum(int(c) for c in "472") == 13

# Q8: café sales
SALES = [None, 120, 80, 150, 95, 110, 60, 175]
total, high_day, over = 0, 1, 0
for day in range(1, 8):
    total += SALES[day]
    if SALES[day] > SALES[high_day]:
        high_day = day
    if SALES[day] > 100:
        over += 1
assert (total, high_day, over) == (790, 7, 4)

# Stretch 1: password function and the eight tests
def valid_password(p):
    return 8 <= len(p) <= 12 and any(c.isdigit() for c in p)


rows = [[c.strip(" `") for c in ln.strip().strip("|").split("|")] for ln in
        TEXT[TEXT.index("| Test data | Length | Has a digit | Type | Expected result |"):].split("\n")[2:10]]
assert len(rows) == 8
for data, length, digit, kind, expected in rows:
    p = "" if data == "(nothing typed)" else data
    assert len(p) == int(length), data
    assert any(c.isdigit() for c in p) == (digit == "yes"), data
    assert valid_password(p) == (expected == "accepted"), data
    assert kind.startswith("abnormal") == (expected == "rejected") or kind in ("normal", "extreme"), data

# Stretch 2: shipping function, paths and values
def shipping(mass, express, remote):
    cost = 5.0
    if mass > 10.0:
        cost = cost + 4.0
    if express:
        cost = cost * 2
    if remote:
        cost = cost + 3.0
    return cost


assert shipping(12.0, True, True) == 21.0 == (5.0 + 4.0) * 2 + 3.0
assert shipping(12.0, True, False) == 18.0
assert len({(m > 10.0, e, r) for m in (5.0, 12.0) for e in (True, False) for r in (True, False)}) == 8 == 2 ** 3

print("ok")
