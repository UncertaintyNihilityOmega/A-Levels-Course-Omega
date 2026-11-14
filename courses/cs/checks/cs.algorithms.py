# checks/cs.algorithms.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, fares, truth tables, note counts).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.algorithms"

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


INPUTS = [("Pages read (0 to finish)", ["12", "30", "25", "0"]),
          ("Student (Y or N)", ["30", "Y"]),
          ("At night (Y or N)", ["7", "Y"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 3, f"expected 3 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 12

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
count = 4
count = count + 1
assert count == 5
age, member = 65, False
assert (age >= 60 and member) is False

# ---------------------------------------------------------------------------------------------
# Identifier rules and the identifier-table example (fine for a late book)
# ---------------------------------------------------------------------------------------------
KEYWORDS = {"IF", "FOR", "WHILE", "REPEAT", "OUTPUT", "INPUT"}


def legal(name):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name) is not None and name.upper() not in KEYWORDS


assert [legal(n) for n in ("Total 1", "total_1", "1stTotal", "FOR")] == [False, True, False, False]
assert legal("DaysLate") and legal("Days_Late") and not legal("Days Late") and not legal("2ndTry")

DAILY_FINE = 0.25


def library_fine(days_late):
    fine = days_late * DAILY_FINE
    if fine > 5.00:
        fine = 5.00
    return fine


assert 12 * DAILY_FINE == 3.0 and library_fine(12) == 3.0
assert 30 * DAILY_FINE == 7.5 and library_fine(30) == 5.00

# ---------------------------------------------------------------------------------------------
# Worked example 1: the reading club (WHILE with a sentinel)
# ---------------------------------------------------------------------------------------------
def reading_club(values):
    """Returns (days, total, trace columns) following the pseudocode line by line."""
    cols = {"Total": [], "Days": [], "Pages": [], "OUTPUT": []}
    data = list(values)
    total = 0
    cols["Total"].append(str(total))
    days = 0
    cols["Days"].append(str(days))
    pages = data.pop(0)
    cols["Pages"].append(str(pages))
    while pages != 0:
        total = total + pages
        cols["Total"].append(str(total))
        days = days + 1
        cols["Days"].append(str(days))
        pages = data.pop(0)
        cols["Pages"].append(str(pages))
    cols["OUTPUT"].append(f"Days: {days}")
    cols["OUTPUT"].append(f"Total pages: {total}")
    return days, total, cols


days, total, cols = reading_club([12, 30, 25, 0])
assert (days, total) == (3, 67) == (3, 12 + 30 + 25)
header, rows = table_after("| Total | Days | Pages | OUTPUT |")
for name, values in cols.items():
    assert column_values(header, rows, name) == values, f"trace column {name}"
assert len(rows) == 14
assert reading_club([0])[:2] == (0, 0)             # the loop runs zero times


def reading_club_repeat(values):
    """The student's REPEAT version (Spot the error)."""
    data = list(values)
    total = days = 0
    while True:
        pages = data.pop(0)
        total += pages
        days += 1
        if pages == 0:
            break
    return days, total


assert reading_club_repeat([12, 30, 25, 0]) == (4, 67)       # Days is 4, not 3
# marks of the Spot-the-error answer: B1 B1 B0 B0 B1 B1 of 6
assert [1, 1, 0, 0, 1, 1].count(1) == 4

# ---------------------------------------------------------------------------------------------
# Worked example 2: the museum price (nested selection)
# ---------------------------------------------------------------------------------------------
def museum_price(age, student):
    if age < 5:
        return 0.00
    else:
        if age < 18:
            return 4.00
        else:
            if student == "Y":
                return 6.00
            else:
                return 10.00


assert museum_price(30, "Y") == 6.00
assert museum_price(4, "N") == 0.00 and museum_price(5, "N") == 4.00
assert museum_price(17, "N") == 4.00 and museum_price(18, "N") == 10.00
assert museum_price(18, "Y") == 6.00 and museum_price(3, "Y") == 0.00 and museum_price(10, "Y") == 4.00

# ---------------------------------------------------------------------------------------------
# Stepwise refinement: the taxi fare
# ---------------------------------------------------------------------------------------------
BASE_FARE, FREE_KM, RATE_PER_KM, NIGHT_CHARGE = 3.00, 2, 1.50, 2.00


def taxi_fare(distance, at_night):
    fare = BASE_FARE
    if distance > FREE_KM:
        fare = fare + (distance - FREE_KM) * RATE_PER_KM
    if at_night == "Y":
        fare = fare + NIGHT_CHARGE
    return fare


assert 7 - 2 == 5 and 5 * 1.50 == 7.50 and 3.00 + 7.50 + 2.00 == 12.50
assert taxi_fare(7, "Y") == 12.5 and taxi_fare(7, "N") == 10.5 and taxi_fare(2, "N") == 3.0

# ---------------------------------------------------------------------------------------------
# Logic statements: conditions, negation, De Morgan
# ---------------------------------------------------------------------------------------------
for n in range(-5, 40):
    inside = n >= 10 and n <= 20
    assert (n < 10 or n > 20) == (not inside)
    assert not (n < 10 and n > 20)                          # "outside" written with AND is never true
    assert (n >= 10 or n <= 20) is True                      # OR is true for every number
    assert (n > 10 and n < 20) == (11 <= n <= 19)            # leaves out 10 and 20
    valid_age = n >= 5 and n <= 18
    assert (n < 5 or n > 18) == (not valid_age)              # UNTIL condition vs WHILE condition
    assert (n <= 5 or n >= 18) == (not valid_age) or n in (5, 18)
assert (5 <= 5 or 5 >= 18) is True and (18 <= 5 or 18 >= 18) is True   # the wrong WHILE condition includes 5 and 18
for a in (False, True):
    for b in (False, True):
        assert (not (a and b)) == ((not a) or (not b))
        assert (not (a or b)) == ((not a) and (not b))
codes = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
assert all((c != "X" or c != "Z") for c in codes)           # OR would be true for every code
assert [c for c in codes if c != "X" and c != "Z"] == [c for c in codes if c not in "XZ"]

# ---------------------------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------------------------
def pick(first, second):
    return first if first > second else second


assert pick(7, 3) == 7 and pick(3, 7) == 7

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
# Q1 identifier table: IsDistinction is a BOOLEAN holding a comparison
for mark in (79, 80, 95):
    assert isinstance(mark >= 80, bool)


# Q4 the score flowchart as pseudocode (WHILE version) and as REPEAT version
def score_while(values):
    data, out = list(values), []
    score = data.pop(0)
    while score < 0 or score > 100:
        out.append("Invalid")
        score = data.pop(0)
    out.append("Pass" if score >= 40 else "Fail")
    return out


def score_repeat(values):
    data, out = list(values), []
    while True:
        score = data.pop(0)
        if score < 0 or score > 100:
            out.append("Invalid")
        if score >= 0 and score <= 100:
            break
    out.append("Pass" if score >= 40 else "Fail")
    return out


for seq in ([150, -3, 72], [35], [40], [39], [100], [0], [-1, 101, 0]):
    assert score_while(seq) == score_repeat(seq)
assert score_while([150, -3, 72]) == ["Invalid", "Invalid", "Pass"] and score_while([35]) == ["Fail"]
assert score_while([40]) == ["Pass"] and score_while([39]) == ["Fail"]


# Q5 flowchart from REPEAT pseudocode: count the odd numbers before 0
def odd_count(values):
    data = list(values)
    count = 0
    while True:
        number = data.pop(0)
        if number % 2 == 1:
            count += 1
        if number == 0:
            break
    return count


assert odd_count([3, 8, 5, 0]) == 2


# Q6 structured English to pseudocode
def five_prices(prices):
    total, steps = 0, []
    for price in prices:
        if price > 50:
            total = total + price - 5
        else:
            total = total + price
        steps.append(total)
    return total, steps


total, steps = five_prices([60, 20, 50, 80, 10])
assert total == 210 == 55 + 20 + 50 + 75 + 10 and steps == [55, 75, 125, 200, 210]

# Q7 flowchart errors: the correct algorithm
marks = [10, 20, 30, 40, 50]
count, total = 1, 0
for m in marks:
    total += m
    count += 1
assert (total, total / 5, count) == (150, 30.0, 6) and total / (count - 1) == 30.0


# Q8 till condition
def ok(not_expired, amount, pin_correct):
    return not_expired and amount > 0.00 and amount <= 500.00 and pin_correct


def not_ok(not_expired, amount, pin_correct):
    return (not not_expired) or amount <= 0.00 or amount > 500.00 or (not pin_correct)


for ne in (False, True):
    for amt in (-1.0, 0.0, 0.01, 250.0, 500.0, 500.01):
        for pc in (False, True):
            assert (not ok(ne, amt, pc)) == not_ok(ne, amt, pc)

# Stretch 1: notes of 50, 20 and 10 (smallest number of notes)
def notes(amount):
    fifties = amount // 50
    amount = amount % 50
    twenties = amount // 20
    amount = amount % 20
    tens = amount // 10
    return fifties, twenties, tens


assert notes(180) == (3, 1, 1) and sum(notes(180)) == 5 and 3 * 50 + 20 + 10 == 180
best = {0: 0}
for amt in range(10, 1010, 10):
    best[amt] = min(best[amt - v] + 1 for v in (10, 20, 50) if amt - v >= 0)
for amt in range(10, 1010, 10):
    f, t, n10 = notes(amt)
    assert 50 * f + 20 * t + 10 * n10 == amt and f + t + n10 == best[amt], amt
assert 180 // 50 == 3 and 180 % 50 == 30 and 30 // 20 == 1 and 30 % 20 == 10 and 10 // 10 == 1

# Stretch 2: REPEAT versus WHILE on the same data
def version_a(values):
    data, total, runs = list(values), 0, 0
    while True:
        number = data.pop(0)
        total += number
        runs += 1
        if number == 0:
            break
    return total, runs


def version_b(values):
    data, total, runs = list(values), 0, 0
    number = data.pop(0)
    while number != 0:
        total += number
        runs += 1
        number = data.pop(0)
    return total, runs


assert version_a([4, 6, 0]) == (10, 3) and version_b([4, 6, 0]) == (10, 2)
assert version_a([0]) == (0, 1) and version_b([0]) == (0, 0)

print("ok")
