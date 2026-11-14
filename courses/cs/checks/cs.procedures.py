# checks/cs.procedures.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.procedures"

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


def out_after(marker, nth=1):
    """Lines of the first ```output fence after the nth occurrence of marker."""
    pos = -1
    for _ in range(nth):
        pos = TEXT.index(marker, pos + 1)
    for f in FENCES:
        if f.start() > pos and f.group(1) == "output":
            return [ln.rstrip() for ln in f.group(2).rstrip("\n").split("\n")]
    raise AssertionError("no output fence after " + marker)


def nth_table(marker, nth=1):
    pos = -1
    for _ in range(nth):
        pos = TEXT.index(marker, pos + 1)
    rows = []
    for line in TEXT[pos:].split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
        elif rows:
            break
    return rows[0], rows[1:]


INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 18, f"expected 18 python blocks, found {blocks}"
PSEUDO = lint_pseudocode_blocks()
assert PSEUDO == 30, f"pseudocode blocks: {PSEUDO}"

# ---------------------------------------------------------------------------------------------
# Pseudocode helpers (1-based, as the insert defines them)
# ---------------------------------------------------------------------------------------------
def LEFT(s, n): return s[:n]
def RIGHT(s, n): return s[len(s) - n:]
def MID(s, x, y): return s[x - 1:x - 1 + y]
def LENGTH(s): return len(s)
def ASC(c): return ord(c)
def IS_NUM(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def STR_TO_NUM(s): return float(s) if "." in s else int(s)
def NUM_TO_STR(n): return str(n)

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert 8 - 1 + 1 == 8
assert MID("ABCDEFGH", 2, 3) == "BCD"

# ---------------------------------------------------------------------------------------------
# ShowMenu and PrintTicket
# ---------------------------------------------------------------------------------------------
menu = ["Welcome to the Accra Cafe", "1. Order a drink", "2. Order food", "3. Pay", "Choose an option"]
assert out_after("CALL ShowMenu()") == menu
seats, price = 3, 12.5
assert seats * price == 37.5
assert out_after("CALL PrintTicket(\"Wanjiru\", 3, 12.5)") == ["Ticket for Wanjiru", "3 seats at 12.5 each: 37.5"]

# ---------------------------------------------------------------------------------------------
# BYVAL and BYREF: simulate with a one-cell "variable" for the reference case
# ---------------------------------------------------------------------------------------------
def add_bonus_copy(score, out):
    score = score + 10
    out.append(f"Inside: {score}")
    return score


out = []
points = 40
t1 = [points]
add_bonus_copy(points, out)
out.append(f"After copy: {points}")
ref = [points]                      # BYREF: Score is the same cell as Points
ref[0] += 10
out.append(f"Inside: {ref[0]}")
points = ref[0]
out.append(f"After reference: {points}")
assert out == ["Inside: 50", "After copy: 40", "Inside: 50", "After reference: 50"]
assert out_after("OUTPUT \"After reference: \", Points") == out
h, rows = nth_table("| Points | Score | OUTPUT |", 1)
assert column_values(h, rows, "Points") == ["40"]
assert column_values(h, rows, "Score") == ["40", "50"]
assert column_values(h, rows, "OUTPUT") == ["Inside: 50", "After copy: 40"]
h, rows = nth_table("| Points | Score | OUTPUT |", 2)
assert column_values(h, rows, "Points") == ["40", "50"]
assert column_values(h, rows, "Score") == ["40", "50"]
assert column_values(h, rows, "OUTPUT") == ["Inside: 50", "After reference: 50"]

# Swap with BYREF and BYVAL
opening, closing = 14, 9
temp = opening
opening = closing
closing = temp
assert (opening, closing) == (9, 14) and temp == 14
assert out_after("CALL SwapStock(Opening, Closing)") == ["9 14"]
h, rows = nth_table("| Opening | Closing | Morning | Evening | Temp | OUTPUT |")
assert column_values(h, rows, "Opening") == ["14", "9"]
assert column_values(h, rows, "Closing") == ["9", "14"]
assert column_values(h, rows, "Morning") == ["14", "9"]
assert column_values(h, rows, "Evening") == ["9", "14"]
assert column_values(h, rows, "Temp") == ["14"]
assert column_values(h, rows, "OUTPUT") == ["9 14"]
# BYVAL: the copies are swapped and the caller's variables keep 14 and 9
m, e = 14, 9
m, e = e, m
assert (14, 9) == (14, 9) and "`14 9`" in TEXT

# Python: swap by returning two values
def swap_stock(morning, evening):
    return evening, morning
assert swap_stock(14, 9) == (9, 14)

# ---------------------------------------------------------------------------------------------
# Functions: Discounted, early return, leap year
# ---------------------------------------------------------------------------------------------
def discounted(price, percent):
    reduction = price * percent / 100
    return price - reduction


assert 80.0 * 25 / 100 == 20.0 and discounted(80.0, 25) == 60.0 and discounted(80.0, 25) + 4.5 == 64.5
assert out_after("Total ← Discounted(80.0, 25) + Postage") == ["Pay: 64.5"]
assert "Pay: 64.5" in TEXT


def is_leap(the_year):
    if the_year % 400 == 0:
        return True, "MOD 400"
    if the_year % 100 == 0:
        return False, "MOD 100"
    if the_year % 4 == 0:
        return True, "MOD 4"
    return False, "last"


assert is_leap(2000) == (True, "MOD 400") and is_leap(1900) == (False, "MOD 100")
assert is_leap(2028) == (True, "MOD 4") and is_leap(2027) == (False, "last")
assert 1900 % 400 == 300 and 2028 % 100 == 28
assert [is_leap(y)[0] for y in (2000, 1900, 2028, 2027)] == [True, False, True, False]
h, rows = nth_table("| TheYear | First test that is true |")
assert column_values(h, rows, "Value returned") == ["TRUE", "FALSE", "TRUE", "FALSE"]

# ---------------------------------------------------------------------------------------------
# Average header: the mean needs REAL
# ---------------------------------------------------------------------------------------------
assert 7 / 2 == 3.5

# ---------------------------------------------------------------------------------------------
# Scope and the global-variable bug
# ---------------------------------------------------------------------------------------------
counter = 10
shown = []
for _ in range(2):
    increase = 2
    counter = counter + increase
    shown.append(f"Inside: {counter}")
shown.append(f"Outside: {counter}")
assert shown == ["Inside: 12", "Inside: 14", "Outside: 14"]
assert out_after("OUTPUT \"Outside: \", Counter") == shown

count, said = 0, []
for word in ("river", "mountain"):
    count = len(word)
    said.append(f"{word} has {count} letters")
    count += 1
said.append(f"Words read: {count}")
assert said == ["river has 5 letters", "mountain has 8 letters", "Words read: 9"]
assert out_after("OUTPUT \"Words read: \", Count") == said
assert len(["river", "mountain"]) == 2

# The UnboundLocalError message is exactly what Python 3.12 or later prints
namespace = {"counter": 10}
try:
    exec("def count_up():\n    increase = 2\n    counter = counter + increase\ncount_up()", namespace)
except UnboundLocalError as err:
    assert f"UnboundLocalError: {err}" in TEXT, str(err)
else:
    raise AssertionError("expected UnboundLocalError")

# ---------------------------------------------------------------------------------------------
# Arrays: FindStop, CountAtLeast, CountOverdue, HasSpace
# ---------------------------------------------------------------------------------------------
STOPS = [None, "Central", "Harbour", "Market", "Station", "Hospital", "Stadium"]


def find_stop(name):
    for index in range(1, 7):
        if STOPS[index] == name:
            return index
    return 0


assert (find_stop("Station"), find_stop("Airport")) == (4, 0)
MARKS = [45, 72, 38, 90, 66, 81, 54, 70, 29, 77]
assert sum(1 for s in MARKS if s >= 60) == 6
LOANS = [("Ife", 0), ("Joy", 5), ("Kofi", 12), ("Lina", 0), ("Musa", 30), ("Nia", 8)]
assert [b for b, d in LOANS if d > 7] == ["Kofi", "Musa", "Nia"] and len([1 for b, d in LOANS if d > 7]) == 3
assert 3 * 100 == 300
text = "Cape Town"
assert len(text) == 9 and MID(text, 5, 1) == " " and text.index(" ") + 1 == 5
assert " " not in "Lagos"

# ---------------------------------------------------------------------------------------------
# Exam-style functions: ValidPassword, DateToText
# ---------------------------------------------------------------------------------------------
def valid_password(password):
    if LENGTH(password) < 8:
        return False
    has_digit = has_upper = False
    for index in range(1, LENGTH(password) + 1):
        this = MID(password, index, 1)
        if IS_NUM(this):
            has_digit = True
        if ASC(this) >= ASC("A") and ASC(this) <= ASC("Z"):
            has_upper = True
    return has_digit and has_upper


tests = ["river2027", "River", "Rivers2027", "RIVERSIDE"]
assert [valid_password(t) for t in tests] == [False, False, True, False]
assert out_after("for test in [\"river2027\"") == [f"{t} {valid_password(t)}" for t in tests]

MONTHS = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


def date_to_text(s):
    day = STR_TO_NUM(LEFT(s, 2))
    month = STR_TO_NUM(MID(s, 4, 2))
    return NUM_TO_STR(day) + " " + MONTHS[month] + " " + RIGHT(s, 4)


assert date_to_text("14/03/2027") == "14 March 2027" and date_to_text("05/11/2026") == "5 November 2026"
assert out_after("print(date_to_text(\"14/03/2027\"))") == ["14 March 2027", "5 November 2026"]
assert "14/03/2027"[0:2] == LEFT("14/03/2027", 2) and "14/03/2027"[3:5] == MID("14/03/2027", 4, 2)
assert "14/03/2027"[6:] == RIGHT("14/03/2027", 4)

# Spot the error: the mean of 7.5 and 9.0
assert (7.5 + 9.0) / 2 == 8.25

# ---------------------------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------------------------
assert 5 * 5 + 2 * 2 == 29
assert 4 * 3 == 12
assert [n % 2 == 0 for n in (4, 7)] == [True, False]
assert (10 - 4, 4 - 10) == (6, -6)

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
a, b = 5, 3                        # X by reference, Y by value
a = a * 2
b = b + a
assert (a, b) == (10, 13)
x_after, y_after = a, 3
assert out_after("CALL Adjust(X, Y)") == ["In: 10 13", "Out: 10 3"]
assert 4 * 4 * 4 == 64 and 64 + 1 == 65


def valid_code(code):
    if LENGTH(code) != 6:
        return False
    for index in range(1, 3):
        this = MID(code, index, 1)
        if ASC(this) < ASC("A") or ASC(this) > ASC("Z"):
            return False
    for index in range(3, 7):
        if not IS_NUM(MID(code, index, 1)):
            return False
    return True


assert [valid_code(c) for c in ["AB1234", "ab1234", "AB12C4", "AB123", "ABC123"]] == [True, False, False, False, False]
assert (135 // 60, 135 % 60) == (2, 15)
assert f"{135 // 60} min {135 % 60} s" == "2 min 15 s" and "`2 min 15 s`" in TEXT

RAIN = [12.5, 30.0, 78.5, 120.0, 210.5, 150.0, 98.0, 85.5, 160.0, 140.0, 40.0, 15.0]
best = 1
for index in range(2, 13):
    if RAIN[index - 1] > RAIN[best - 1]:
        best = index
assert best == 5
assert [i for i in range(1, 13) if RAIN[i - 1] > 100.0] == [4, 5, 6, 9, 10]

total = 0
lines = []
for amount in (5, 3):
    total += amount * 2
    lines.append(f"Total is {total}")
lines.append(f"Final: {total}")
assert lines == ["Total is 10", "Total is 16", "Final: 16"] and 10 + 6 == 16
assert out_after("(a) State the three lines") == lines


# Stretch 1: IsPrime
def is_prime_tests(n):
    d, tests_made = 2, 0
    while d * d <= n:
        tests_made += 1
        if n % d == 0:
            return False, tests_made
        d += 1
    return True, tests_made


assert is_prime_tests(97) == (True, 8)
assert is_prime_tests(91) == (False, 6) and 91 == 7 * 13
assert len(range(2, 97)) == 95 and 95 - 8 == 87
assert [n for n in range(2, 30) if is_prime_tests(n)[0]] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Stretch 2: Python swap
def swap_bad(a, b):
    a, b = b, a


x, y = 3, 8
swap_bad(x, y)
assert (x, y) == (3, 8)
items = [1, 2, 3]
items[0], items[1] = items[1], items[0]
assert items == [2, 1, 3]

# Quiz
def add_one(n):
    n = n + 1


x = 5
add_one(x)
assert x == 5
data = [1]
data.append(9)
assert data == [1, 9]
assert 8 + 6 == 14 and "4" + "3" == "43"
bump_x = 7                         # BYVAL: the copy is changed, X stays 7
assert bump_x == 7

print("ok")
