# checks/cs.f.basics.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (outputs, trace tables, error messages).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.f.basics"

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


INPUTS = [("Time in seconds", ["200"]), ("Your name", ["Amina"]), ("First number", ["3", "4"]),
          ("Price of one item", ["2.5", "4"]), ("What is 7 times 8", ["56"]),
          ("Enter a positive number", ["-3", "0", "7"]), ("Which times table", ["7"]),
          ("Guess the number", ["10", "20", "17"]), ("Enter a number", ["4096"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 29, f"expected 29 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 23

# ---------------------------------------------------------------------------------------------
# Failing programs shown in ```text blocks: run them and compare the error with the chapter
# ---------------------------------------------------------------------------------------------
def error_of(code):
    try:
        exec(compile(code, "shop.py", "exec"), {})
    except Exception as exc:
        return type(exc).__name__, str(exc)
    return None


for snippet in ("for count in range(1, 4)\n    print(count)\n",):
    assert snippet in TEXT
    try:
        compile(snippet, "loop.py", "exec")
        raise AssertionError("no syntax error")
    except SyntaxError as exc:
        assert exc.msg == "expected ':'" or exc.msg == "invalid syntax", exc.msg
assert "SyntaxError: expected ':'" in TEXT
zero = "total = 120\ncount = 0\naverage = total / count\nprint(average)\n"
assert zero in TEXT
assert error_of(zero) == ("ZeroDivisionError", "division by zero")
assert error_of('print("Total: " + 5)')[0] == "TypeError"
assert error_of('int("abc")')[0] == "ValueError"
assert error_of("print(scors)")[0] == "NameError"
assert 'print("Total: " + 5)' in TEXT and 'int("abc")' in TEXT
try:
    compile('print("Hello"\n', "x.py", "exec")
    raise AssertionError("expected a syntax error")
except SyntaxError:
    pass

# ---------------------------------------------------------------------------------------------
# Warm-up (GCSE)
# ---------------------------------------------------------------------------------------------
assert 29 % 6 == 5 and 4 * 6 + 5 == 29
n = 5
n = n * 2 - 3
n = n * 2 - 3
assert n == 11
assert not (25 > 10 and 25 < 20)

# ---------------------------------------------------------------------------------------------
# Arithmetic, types, strings
# ---------------------------------------------------------------------------------------------
assert 12.50 * 3 == 37.5
assert (17 + 5, 17 - 5, 17 * 5, 17 / 5, 17 // 5, 17 % 5) == (22, 12, 85, 3.4, 3, 2)
assert 17 == 3 * 5 + 2
assert (200 // 60, 200 % 60) == (3, 20)
assert (2 + 3 * 4, (2 + 3) * 4, 8 + 6 / 2, (8 + 6) / 2) == (14, 20, 11.0, 7.0)
assert 10 + 20 / 2 == 20.0 and (10 + 20) / 2 == 15.0
assert "3" + "4" == "34" and int("3") + int("4") == 7 and "10" < "9"
assert 2.5 * 4 == 10.0
assert int(3.9) == 3 and float(4) == 4.0
word = "computer"
assert len(word) == 8 and word[1:4] == "omp" and word[0:3] == "com"


def mid(s, x, y):
    return s[x - 1: x - 1 + y]


assert mid(word, 2, 3) == word[1:4] == "omp"
assert mid("computer", 4, 3) == "put"
assert len("Age: 15") == 7 and len("Lagos") * 2 == 10 and len(word) == 8

# Boolean table
table_header, table_rows = table_after("| A | B | A AND B |")
for a_text, b_text, and_text, or_text, not_text in table_rows:
    a, b = a_text == "TRUE", b_text == "TRUE"
    assert (a and b) == (and_text == "TRUE") and (a or b) == (or_text == "TRUE") and (not a) == (not_text == "TRUE")
assert len(table_rows) == 4

# Selection: order of the tests
def result_right(mark):
    return "High" if mark >= 70 else "Pass" if mark >= 40 else "Retake"


def result_wrong(mark):
    return "Pass" if mark >= 40 else "High" if mark >= 70 else "Retake"


assert result_right(58) == "Pass" and result_right(85) == "High" and result_wrong(85) == "Pass"

# Loops: range lists
assert list(range(1, 6)) == [1, 2, 3, 4, 5] and list(range(5)) == [0, 1, 2, 3, 4]
assert list(range(2, 11, 2)) == [2, 4, 6, 8, 10] and list(range(5, 0, -1)) == [5, 4, 3, 2, 1]
assert list(range(2, 9, 3)) == [2, 5, 8] and list(range(1, 10)) == list(range(1, 10)) and 10 not in range(1, 10)
assert sum(range(1, 6)) == 15
assert list(range(1, 5)) == [1, 2, 3, 4]

# ---------------------------------------------------------------------------------------------
# Trace of the savings loop, against the chapter's table
# ---------------------------------------------------------------------------------------------
savings, years, rows_s, years_s = 100, 0, [100], [0]
while savings < 1000:
    savings = savings * 2
    years = years + 1
    rows_s.append(savings)
    years_s.append(years)
assert (years, savings) == (4, 1600)
header, rows = table_after("| Savings | Years | OUTPUT |")
assert column_values(header, rows, "Savings") == [str(v) for v in rows_s]
assert column_values(header, rows, "Years") == [str(v) for v in years_s]
assert column_values(header, rows, "OUTPUT") == ["4 1600"]

# Try: Count/Total trace
total, counts, totals = 0, [], [0]
for count in range(1, 5):
    total += count
    counts.append(count)
    totals.append(total)
header, rows = table_after("| Count | Total | OUTPUT |")
assert column_values(header, rows, "Count") == [str(v) for v in counts]
assert column_values(header, rows, "Total") == [str(v) for v in totals]
assert column_values(header, rows, "OUTPUT") == ["10"] and total == 10
assert 6 * 2 + 1 == 13 and (23 // 5, 23 % 5) == (4, 3) and (7 // 2, 7 % 2, 7 / 2) == (3, 1, 3.5)
assert list(range(2, 21, 2))[0] == 2 and list(range(2, 21, 2))[-1] == 20

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
assert (47 // 10, 47 % 10, 47 / 4) == (4, 7, 11.75)


def discounted(quantity):
    cost = quantity * 2.5
    if cost > 50.0:
        cost = cost * 0.9
    return cost


assert discounted(10) == 25.0 and discounted(20) == 50.0 and discounted(30) == 67.5
assert 50.0 * 0.9 == 45.0

# Q4: trace of the Number/Steps loop
number, steps, nums, stepcounts = 5, 0, [5], [0]
while number > 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    steps += 1
    nums.append(number)
    stepcounts.append(steps)
assert nums == [5, 16, 8, 4, 2, 1] and steps == 5
header, rows = table_after("| Number | Steps | OUTPUT |")
assert column_values(header, rows, "Number") == [str(v) for v in nums]
assert column_values(header, rows, "Steps") == [str(v) for v in stepcounts]
assert column_values(header, rows, "OUTPUT") == ["5"]


def sentinel(values):
    total, count, it = 0, 0, iter(values)
    value = next(it)
    while value != 0:
        total += value
        count += 1
        value = next(it)
    return total, count


assert sentinel([5, 3, 4, 0]) == (12, 3) and sentinel([0]) == (0, 0)


def username(first, last):
    return (first[:3] + last).lower()


assert username("Amina", "Mwangi") == "amimwangi"


def total_fare(ages):
    total = 0.0
    for age in ages:
        if age < 12:
            total += 1.5
        elif age < 65:
            total += 3.0
        else:
            total += 1.0
    return total


assert total_fare([5, 30, 70, 12, 64, 65, 11, 40, 8, 90]) == 1.5 + 3 + 1 + 3 + 3 + 1 + 1.5 + 3 + 1.5 + 1
assert total_fare([11, 12, 64, 65]) == 1.5 + 3.0 + 3.0 + 1.0

# Stretch
tick = []
for k in range(1, 16):
    tick.append("TickTock" if k % 15 == 0 else "Tick" if k % 3 == 0 else "Tock" if k % 5 == 0 else str(k))
assert tick[:6] == ["1", "2", "Tick", "4", "Tock", "Tick"] and tick[-1] == "TickTock"
assert len(tick) == 15 and tick.count("TickTock") == 1


def digit_sum(value):
    total, rows = 0, [(value, 0)]
    while value > 0:
        total = total + value % 10
        value = value // 10
        rows.append((value, total))
    return total, rows


assert digit_sum(4096) == (19, [(4096, 0), (409, 6), (40, 15), (4, 15), (0, 19)])
assert 4 + 0 + 9 + 6 == 19
header, rows = table_after("| Number | Total | OUTPUT |\n|---|---|---|\n| 4096 |")
assert column_values(header, rows, "Number") == ["4096", "409", "40", "4", "0"]
assert column_values(header, rows, "Total") == ["0", "6", "15", "15", "19"]
assert column_values(header, rows, "OUTPUT") == ["19"]

# Spot the error: precedence of the mean
a_val, b_val = 10, 20
assert a_val + b_val / 2 == 20 and (a_val + b_val) / 2 == 15

# Quiz
assert 5 + 6 * 2 == 17 and (5 + 6) * 2 == 22 and 8 / 2 == 4.0 and 17 % 5 == 2
a_var = 5
b_var = a_var
a_var = 9
assert b_var == 5

print("ok")
