# checks/cs.programming.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, outputs, function values, loop counts).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.programming"

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


INPUTS = [("Price: ", ["50"]),
          ("Hours worked", ["Amina", "8"]),
          ("Choice: ", ["2"]),
          ("Mark: ", ["63"]),
          ("Age: ", ["abc", "-4", "17"]),
          ("Rainfall in mm", ["12", "7", "20", "3", "-1"]),
          ("Word: ", ["Education"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 19, f"expected 19 python blocks, found {blocks}"
PSEUDO = lint_pseudocode_blocks()
assert PSEUDO == 35, PSEUDO

# ---- the pseudocode functions of the insert, written in Python (1-based positions) ----
def LEFT(s, n): return s[:n]
def RIGHT(s, n): return s[len(s) - n:]
def MID(s, x, n): return s[x - 1:x - 1 + n]
def LENGTH(s): return len(s)
def INT(x): return int(x)                     # truncation, positive numbers in Paper 2
def DIV(a, b): return a // b
def MOD(a, b): return a % b

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert (DIV(17, 5), MOD(17, 5)) == (3, 2) and 17 == 3 * 5 + 2
for mark in range(-3, 15):
    assert (mark >= 1 and mark <= 10) == (1 <= mark <= 10)

# ---------------------------------------------------------------------------------------------
# Tracing assignments
# ---------------------------------------------------------------------------------------------
cols = {"X": [], "Y": [], "OUTPUT": []}
X = 5; cols["X"].append(str(X))
Y = X * 2; cols["Y"].append(str(Y))
X = X + Y; cols["X"].append(str(X))
Y = X - Y; cols["Y"].append(str(Y))
cols["OUTPUT"].append(f"{X} {Y}")
assert (X, Y) == (15, 5)
header, rows = table_after("| X | Y | OUTPUT |")
for name, values in cols.items():
    assert column_values(header, rows, name) == values, name

# constant and sales tax
SALES_TAX = 0.06
assert round(50.00 * SALES_TAX, 10) == 3.0 and round(50.00 + 50.00 * SALES_TAX, 10) == 53.0

# ---------------------------------------------------------------------------------------------
# Operators, DIV and MOD
# ---------------------------------------------------------------------------------------------
assert (2 + 3 * 4, (2 + 3) * 4, 17 / 5) == (14, 20, 3.4)
seconds = 7384
hours, rest = DIV(seconds, 3600), MOD(seconds, 3600)
minutes, secs = DIV(rest, 60), MOD(rest, 60)
assert (hours, rest, minutes, secs) == (2, 184, 3, 4) and 2 * 3600 + 3 * 60 + 4 == 7384
assert (4729 % 10, 4729 // 10) == (9, 472) and (22 + 5) % 24 == 3
assert 6.50 * 8 == 52.0
truth = [(a, b, a and b, a or b, not a) for a in (True, False) for b in (True, False)]
assert truth == [(True, True, True, True, False), (True, False, False, True, False),
                 (False, True, False, True, True), (False, False, False, False, True)]

# ---------------------------------------------------------------------------------------------
# Built-in functions
# ---------------------------------------------------------------------------------------------
s = "computer"
assert (LEFT(s, 3), RIGHT(s, 3), MID(s, 4, 3), LENGTH(s)) == ("com", "ter", "put", 8)
assert s[4 - 1:4 - 1 + 3] == "put" and "Hi".upper() == "HI" and "Hi".lower() == "hi"
assert (str(87.5), float("23.45"), ord("A"), chr(65)) == ("87.5", 23.45, 65, "A")
assert (INT(27.5), INT(9.99), int(-2.5)) == (27, 9, -2)
# values eg: Nairobi
assert [LEFT("Nairobi", 4), MID("Nairobi", 3, 2), LENGTH("Nairobi"), RIGHT("Nairobi", 3).upper()] == ["Nair", "ir", 7, "OBI"]
assert (ord("C") + 1, chr(ord("C") + 1), int("12") * 2, INT(9.99)) == (68, "D", 24, 9)
assert MID("Kampala", 2, 3) == "amp" == "Kampala"[1:4]
# RAND: INT(RAND(6)) + 1 gives 1 to 6; INT(RAND(10)) gives 0 to 9
for k in range(0, 600):
    r = 6 * k / 600                          # every value from 0 up to (not including) 6
    assert 1 <= INT(r) + 1 <= 6 and 0 <= INT(r * 10 / 6) <= 9
import datetime
d = datetime.date(2027, 3, 14)
assert d.isoweekday() == 7 and d.isoweekday() % 7 + 1 == 1
assert datetime.date(2027, 3, 15).isoweekday() % 7 + 1 == 2          # Monday is 2

# ---------------------------------------------------------------------------------------------
# Selection: grade chain, wrong order, CASE menu
# ---------------------------------------------------------------------------------------------
def grade(mark):
    if mark >= 70:
        return "Distinction"
    else:
        if mark >= 50:
            return "Pass"
        else:
            return "Fail"


def grade_wrong_order(mark):
    if mark >= 50:
        return "Pass"
    else:
        return "Fail"                       # the 70 test after it can never be reached for 85


assert [grade(m) for m in (63, 70, 85, 49, 50)] == ["Pass", "Distinction", "Distinction", "Fail", "Pass"]
assert grade_wrong_order(85) == "Pass"


def meter(choice):
    return {1: 1.50, 2: 2.50, 3: 4.00}.get(choice, "Invalid choice")


assert (meter(1), meter(2), meter(3), meter(5)) == (1.5, 2.5, 4.0, "Invalid choice")

# ---------------------------------------------------------------------------------------------
# Iteration: FOR counts, STEP, WHILE / REPEAT
# ---------------------------------------------------------------------------------------------
assert list(range(10, 1, -2)) == [10, 8, 6, 4, 2] and list(range(1, 6)) == [1, 2, 3, 4, 5]
assert list(range(0, 21, 5)) == [0, 5, 10, 15, 20] and list(range(5, 0)) == []
assert list(range(3, 10, 2)) == [3, 5, 7, 9] and len(range(3, 10, 2)) == 4
assert list(range(10, 0, -3)) == [10, 7, 4, 1] and len(range(10, 0, -3)) == 4
assert sum(range(1, 11, 3)) == 22 == 1 + 4 + 7 + 10 and list(range(1, 11, 3)) == [1, 4, 7, 10]


def squares_while(count):
    out = []
    while count <= 5:
        out.append(count * count)
        count += 1
    return out


def squares_repeat(count):
    out = []
    while True:
        out.append(count * count)
        count += 1
        if count > 5:
            break
    return out


assert squares_while(1) == squares_repeat(1) == [1, 4, 9, 16, 25]
assert squares_while(9) == [] and squares_repeat(9) == [81]


def validate_age(values):
    data, out = list(values), []
    while True:
        age = data.pop(0)
        if age < 5 or age > 18:
            out.append("Age must be 5 to 18")
        if age >= 5 and age <= 18:
            break
    out.append(f"Accepted: {age}")
    return out


assert validate_age([3, 25, 12]) == ["Age must be 5 to 18", "Age must be 5 to 18", "Accepted: 12"]
assert validate_age([18]) == ["Accepted: 18"]


def bad_quantity(values):                    # the student's UNTIL condition
    data = list(values)
    while True:
        q = data.pop(0)
        if q < 1 or q > 10:
            break
    return q


def good_quantity(values):
    data = list(values)
    while True:
        q = data.pop(0)
        if q >= 1 and q <= 10:
            break
    return q


assert bad_quantity([5, 12]) == 12 and good_quantity([5, 12]) == 5

# ---------------------------------------------------------------------------------------------
# Totals, counts, highest and lowest (rainfall)
# ---------------------------------------------------------------------------------------------
def rainfall(values):
    data = list(values)
    rain = data.pop(0)
    if rain == -1:
        return "No readings"
    total = count = 0
    highest = lowest = rain
    while rain != -1:
        total += rain
        count += 1
        if rain > highest:
            highest = rain
        if rain < lowest:
            lowest = rain
        rain = data.pop(0)
    return count, total / count, highest, lowest


assert rainfall([12, 7, 20, 3, -1]) == (4, 10.5, 20, 3) and 12 + 7 + 20 + 3 == 42 and 42 / 4 == 10.5
assert rainfall([-1]) == "No readings"
assert min([0] + [12, 7, 20, 3]) == 0 and min([12, 7, 20, 3]) == 3        # starting Lowest at 0 is wrong

# ---------------------------------------------------------------------------------------------
# Nested loops: the grid
# ---------------------------------------------------------------------------------------------
lines, inner = [], 0
for row in range(1, 4):
    line = ""
    for column in range(1, 5):
        line = line + str(row * column) + " "
        inner += 1
    lines.append(line)
assert lines == ["1 2 3 4 ", "2 4 6 8 ", "3 6 9 12 "] and inner == 12 == 3 * 4

# ---------------------------------------------------------------------------------------------
# Strings: vowels, reverse, code validation, slice slip, efficiency
# ---------------------------------------------------------------------------------------------
def vowels(word):
    n = 0
    for position in range(1, LENGTH(word) + 1):
        letter = MID(word, position, 1)
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            n += 1
    return n


assert (vowels("banana"), vowels("rhythm"), vowels("education")) == (3, 0, 5)
assert vowels("Education".lower()) == 5

rev = ""
for position in range(LENGTH("stressed"), 0, -1):
    rev = rev + MID("stressed", position, 1)
assert rev == "desserts" == "stressed"[::-1]


def student_code(code):
    valid = True
    if LENGTH(code) != 6:
        valid = False
    else:
        for position in range(1, 3):
            letter = MID(code, position, 1)
            if letter < "A" or letter > "Z":
                valid = False
        for position in range(3, 7):
            if not MID(code, position, 1).isdigit():
                valid = False
    return valid


assert [student_code(c) for c in ("AB1234", "ab1234", "AB123", "A1B234")] == [True, False, False, False]
assert "computer"[4:7] == "ute" and "computer"[3:6] == "put" == MID("computer", 4, 3)


def contains_z_inefficient(word):
    found, comparisons = False, 0
    for position in range(1, LENGTH(word) + 1):
        comparisons += 1
        if MID(word, position, 1) == "z":
            found = True
    return found, comparisons


def contains_z_efficient(word):
    found, position, comparisons = False, 1, 0
    while not found and position <= LENGTH(word):
        comparisons += 1
        if MID(word, position, 1) == "z":
            found = True
        else:
            position += 1
    return found, comparisons


assert contains_z_inefficient("buzz") == (True, 4) and contains_z_efficient("buzz") == (True, 3)
assert contains_z_inefficient("zebra") == (True, 5) and contains_z_efficient("zebra") == (True, 1)
assert contains_z_inefficient("lamp") == (False, 4) and contains_z_efficient("lamp") == (False, 4)

# hoisting a constant calculation out of a loop gives the same count
max_mark, marks = 80, [31, 32, 12, 70, 33, 40]
assert sum(1 for m in marks if m >= max_mark * 0.4) == sum(1 for m in marks if m >= (pass_mark := max_mark * 0.4))

# ---------------------------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------------------------
assert (29 % 6, 29 // 6) == (5, 4)
assert (482 // 100, (482 // 10) % 10, 482 % 10) == (4, 8, 2)
assert [n for n in range(1, 21) if n % 3 == 0] == [3, 6, 9, 12, 15, 18]
assert [c for c in "AZaz" if c >= "A" and c <= "Z"] == ["A", "Z"]

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
assert 3 * 4 % 5 == 2 and 2 + 3 * 4 % 5 == 4                      # * and MOD at the same level, left to right
assert ((5 > 3) and not (2 > 4)) is True and "kampala"[:3].upper() == "KAM"


def doubling_while():
    out, number = [], 1
    while number <= 50:
        out.append(number)
        number = number * 2
    return out


def doubling_repeat():
    out, number = [], 1
    while True:
        out.append(number)
        number = number * 2
        if number > 50:
            break
    return out


assert doubling_while() == doubling_repeat() == [1, 2, 4, 8, 16, 32]
assert {"S": 600, "R": 1000, "W": 3500}.get("R") == 1000

sentence = "the quick brown fox"
spaces = sum(1 for position in range(1, LENGTH(sentence) + 1) if MID(sentence, position, 1) == " ")
assert (spaces, spaces + 1) == (3, 4) == (len(sentence.split(" ")) - 1, len(sentence.split(" ")))

# trace table of the nested loop
cols = {"Outer": [], "Inner": [], "Total": [], "OUTPUT": []}
total = 0
cols["Total"].append(str(total))
for outer in range(1, 4):
    cols["Outer"].append(str(outer))
    for inner_v in range(1, outer + 1):
        cols["Inner"].append(str(inner_v))
        total = total + inner_v
        cols["Total"].append(str(total))
cols["OUTPUT"].append(str(total))
assert total == 10
header, rows = table_after("| Outer | Inner | Total | OUTPUT |")
for name, values in cols.items():
    assert column_values(header, rows, name) == values, f"trace column {name}"
assert cols["Total"] == ["0", "1", "2", "4", "5", "7", "10"]


def locker(code):
    valid = True
    if LENGTH(code) != 4:
        valid = False
    else:
        letter = LEFT(code, 1)
        if letter < "A" or letter > "F":
            valid = False
        for position in range(2, 5):
            if not MID(code, position, 1).isdigit():
                valid = False
    return "Valid" if valid else "Invalid"


assert [locker(c) for c in ("C482", "G482", "C48", "C4a2", "c482", "A000", "F999")] == \
       ["Valid", "Invalid", "Invalid", "Invalid", "Invalid", "Valid", "Valid"]


def marks_program(values):
    data, out = list(values), []
    count, total, highest = 0, 0, 0
    mark = data.pop(0)
    while mark != 999:
        if mark >= 0 and mark <= 100:
            count += 1
            total += mark
            if mark > highest:
                highest = mark
        else:
            out.append("Ignored")
        mark = data.pop(0)
    if count == 0:
        out.append("No valid marks")
    else:
        out += [f"Valid marks: {count}", f"Mean: {total / count}", f"Highest: {highest}"]
    return out, (count, total)


out, (count, total) = marks_program([45, 120, 80, 62, -5, 100, 999])
assert out == ["Ignored", "Ignored", "Valid marks: 4", "Mean: 71.75", "Highest: 100"]
assert (count, total, 45 + 80 + 62 + 100, 287 / 4) == (4, 287, 287, 71.75)
assert marks_program([-1, 999])[0] == ["Ignored", "No valid marks"] and marks_program([999])[0] == ["No valid marks"]

# Stretch 1: palindromic numbers using DIV and MOD
def palindrome(number):
    original, reversed_number, steps = number, 0, []
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        steps.append(reversed_number)
        number = number // 10
    return reversed_number == original, steps


assert palindrome(1331) == (True, [1, 13, 133, 1331]) and palindrome(1234) == (False, [4, 43, 432, 4321])
for n in range(1, 20000):
    assert palindrome(n)[0] == (str(n) == str(n)[::-1]), n


# Stretch 2: prime test with Divisor * Divisor <= Number
def prime_fast(number):
    is_prime, divisor, tested = True, 2, 0
    while is_prime and divisor * divisor <= number:
        tested += 1
        if number % divisor == 0:
            is_prime = False
        else:
            divisor += 1
    return is_prime, tested


def prime_slow(number):
    return all(number % k != 0 for k in range(2, number))


for n in range(2, 3000):
    assert prime_fast(n)[0] == prime_slow(n), n
assert prime_fast(97) == (True, 8) and prime_fast(91) == (False, 6) and 91 == 7 * 13 and 10 * 10 == 100 > 97
assert len(range(2, 97)) == 95 and prime_fast(2) == (True, 0) and prime_fast(4) == (False, 1)

# ---------------------------------------------------------------------------------------------
# Quiz
# ---------------------------------------------------------------------------------------------
assert 17 / 5 == 3.4 and 17 // 5 == 3 and 17 % 5 == 2
assert MID("computer", 2, 3) == "omp" and "computer"[2:5] == "mpu"
assert max([0] + [-8, -3, -15]) == 0 and max([-8, -3, -15]) == -3
assert INT(9.99) == 9

print("ok")
