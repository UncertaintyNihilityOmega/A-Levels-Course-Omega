# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.mixed.as"

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


import os
import sqlite3
import tempfile
from fractions import Fraction

assert run_python_blocks([]) == 0
lint_pseudocode_blocks()  # every pseudocode block balanced and free of Python syntax

# ---- the two sets: question counts and mark totals, and the pace sentences
sets = re.split(r"^:::try ", TEXT, flags=re.M)
p1 = next(s for s in sets if s.startswith("Paper 1 style"))
p2 = next(s for s in sets if s.startswith("Paper 2 style"))
m1 = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", p1, re.M)]
m2 = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", p2, re.M)]
assert len(m1) == 18 and sum(m1) == 90, (len(m1), sum(m1))
assert len(m2) == 12 and sum(m2) == 69, (len(m2), sum(m2))
assert 14 <= len(m1) <= 18 and 10 <= len(m2) <= 12
assert Fraction(90 * 6, 5) == 108 and float(69 * Fraction(8, 5)) == 110.4
assert r"\(90 \times 1.2 = 108\)" in TEXT and r"\(69 \times 1.6 = 110.4\)" in TEXT
assert len(re.findall(r"^Q: \[\d+ marks\] ★+ \(#cs\.\w+\)", p1, re.M)) == 18
assert len(re.findall(r"^Q: \[\d+ marks\] ★+ \(#cs\.\w+\)", p2, re.M)) == 12
import json
ids = {c["id"] for c in json.loads((CHAPTER.parent.parent / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT)) <= ids


# ---- P1 Q1: modulo-11 check digit
def checkdigit(code):
    n = len(code)
    total = sum(int(d) * w for d, w in zip(code, range(n + 1, 1, -1)))
    return total, total % 11, (11 - total % 11) % 11


assert checkdigit("41627") == (73, 7, 4)
assert [4 * 6, 1 * 5, 6 * 4, 2 * 3, 7 * 2] == [24, 5, 24, 6, 14] and 24 + 5 + 24 + 6 + 14 == 73
assert 73 == 11 * 6 + 7
t6 = sum(int(d) * w for d, w in zip("416724", [6, 5, 4, 3, 2, 1]))
assert t6 == 82 and t6 == 11 * 7 + 5 and t6 % 11 != 0
assert 4 * 6 + 1 * 5 + 6 * 4 + 7 * 3 + 2 * 2 + 4 * 1 == 82
assert sum(int(d) * w for d, w in zip("416274", [6, 5, 4, 3, 2, 1])) % 11 == 0

# ---- P1 Q2: conversions and two's complement
assert format(181, "08b") == "10110101" and 181 == 128 + 32 + 16 + 4 + 1 and format(181, "X") == "B5"
assert format(52, "08b") == "00110100" and format(75, "08b") == "01001011"
assert format(~75 & 0xFF, "08b") == "10110100" and format((~75 + 1) & 0xFF, "08b") == "10110101"
s = (52 + ((~75 + 1) & 0xFF)) & 0xFF
assert format(s, "08b") == "11101001" and s - 256 == -23 == 52 - 75
assert format(~s & 0xFF, "08b") == "00010110" and format((~s + 1) & 0xFF, "08b") == "00010111" and 0b00010111 == 23

# ---- P1 Q3: truth table
rows_ans = []
for t in (0, 1):
    for r in (0, 1):
        for m in (0, 1):
            rows_ans.append((t, r, m, int((t and not r) or m)))
header, rows = table_after("| T | R | M | V |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |")
assert [tuple(int(c) for c in r) for r in rows] == rows_ans
assert [v for *_, v in rows_ans] == [0, 1, 0, 1, 1, 1, 0, 1]

# ---- P1 Q5: bitmap
bits = 256 * 128 * 16
assert bits == 2 ** 19 and bits // 8 == 65536 == 2 ** 16 and bits // 8 // 1024 == 64 == 2 ** 6
assert 256 * 128 * 8 // 8 // 1024 == 32 and 2 ** 16 == 65536 and 2 ** 8 == 256


# ---- P1 Q10: RLE
def rle(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(f"{j - i}{s[i]}")
        i = j
    return " ".join(out)


assert len("AAAABBBCCCCCCAA") == 15 and rle("AAAABBBCCCCCCAA") == "4A 3B 6C 2A"
assert len(rle("ABCABCABC").split()) == 9 and 9 * 2 > 9


# ---- P1 Q12: assembly simulator
def run(prog, mem):
    acc, pc, flag = 0, 100, None
    while True:
        op, arg = prog[pc]
        pc += 1
        if op == "LDD":
            acc = mem[arg]
        elif op == "STO":
            mem[arg] = acc
        elif op == "AND":
            acc &= arg
        elif op == "OR":
            acc |= arg
        elif op == "CMP":
            flag = acc == arg
        elif op == "JPE":
            if flag:
                pc = arg
        elif op == "END":
            return mem


PROG = {100: ("LDD", 150), 101: ("AND", 0b01000000), 102: ("CMP", 0), 103: ("JPE", 108), 104: ("LDD", 151),
        105: ("OR", 0b00000010), 106: ("STO", 151), 107: ("END", None), 108: ("LDD", 151),
        109: ("AND", 0b11111101), 110: ("STO", 151), 111: ("END", None)}
for line in ["100   LDD 150", "101   AND B01000000", "102   CMP #0", "103   JPE 108", "104   LDD 151",
             "105   OR B00000010", "106   STO 151", "107   END", "108   LDD 151", "109   AND B11111101",
             "110   STO 151", "111   END"]:
    assert line in TEXT, line
assert format(run(PROG, {150: 0b01001000, 151: 0b10100001})[151], "08b") == "10100011"
assert format(0b01001000 & 0b01000000, "08b") == "01000000"
assert format(run(PROG, {150: 0b00001000, 151: 0b10100011})[151], "08b") == "10100001"
assert 0b11111101 == 255 - 2 and 0b01000000 == 1 << 6 and 0b10 == 1 << 1

# ---- P1 Q15: SQL on sample data
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE Customer (CustomerID TEXT, CustomerName TEXT, City TEXT);"
                 "CREATE TABLE Orders (OrderID TEXT, CustomerID TEXT, Total INTEGER);")
_, crow = table_after("| CustomerID | CustomerName | City |")
db.executemany("INSERT INTO Customer VALUES (?,?,?)", crow)
_, orow = table_after("| OrderID | CustomerID | Total |")
db.executemany("INSERT INTO Orders VALUES (?,?,?)", [(a, b, int(c)) for a, b, c in orow])
assert len(crow) == 3 and len(orow) == 6
sql = re.search(r"```text\n(SELECT Customer\.CustomerName.*?;)\n```", TEXT, re.S).group(1)
res = db.execute(sql).fetchall()
_, outrows = table_after("| CustomerName | SUM(Orders.Total) |")
assert [(a, int(b)) for a, b in outrows] == res == [("Amara Stores", 330), ("Chege Traders", 345)], res

# ---- quiz facts
assert 3 * 1024 == 3072 and 2 ** 7 - 1 == 127 and -(2 ** 7) == -128 and 2 ** 4 == 16
assert (1 ^ 1) == 0
byte = 0b01000001  # even parity: the count of 1s is even
flipped = byte ^ 0b00000011
assert bin(byte).count("1") % 2 == bin(flipped).count("1") % 2

# =============== Paper 2 style set
# Q3 trace
word, result, steps = "Level", "", []
for index in range(len(word), 0, -1):
    result += word[index - 1]
    steps.append((index, result))
assert steps == [(5, "l"), (4, "le"), (3, "lev"), (2, "leve"), (1, "leveL")]
assert (result == word) is False
_, trows = table_after('| Index | Result | OUTPUT |\n|---|---|---|\n| | "" | |')
assert [(r[0], r[1].strip('"')) for r in trows[1:6]] == [(str(i), r) for i, r in steps]
assert trows[0][1] == '""' and trows[6][2] == "Different"


# Q2 mean mass
def mean_mass(masses):
    total, count = 0.0, 0
    for m in masses:
        total += m
        count += 1
    return total / count if count > 0 else "No bags"


assert mean_mass([]) == "No bags" and mean_mass([2.0, 4.0]) == 3.0


# Q4 Sell
def sell(stock, code, sold):
    index, found = 0, False
    while index < len(stock) and not found:
        if stock[index]["code"] == code:
            found = True
        else:
            index += 1
    if not found:
        return "Item not found"
    if stock[index]["qty"] >= sold:
        stock[index]["qty"] -= sold
        return None
    return "Not enough stock"


stock = [{"code": "A1", "qty": 5}, {"code": "B2", "qty": 2}]
assert sell(stock, "A1", 5) is None and stock[0]["qty"] == 0
assert sell(stock, "B2", 3) == "Not enough stock" and sell(stock, "Z9", 1) == "Item not found"


# Q5 bubble sort, descending, efficient, as in the gaps
def bubble_desc(marks):
    marks, last, first_pass = list(marks), 5, None
    while True:
        swapped = False
        for i in range(last):                 # FOR Index <- 1 TO Last
            if marks[i] < marks[i + 1]:       # gap (b): <
                marks[i], marks[i + 1] = marks[i + 1], marks[i]
                swapped = True
        if first_pass is None:
            first_pass = list(marks)
        last -= 1
        if not swapped or last == 0:
            return marks, first_pass


final, first = bubble_desc([34, 71, 50, 88, 62, 45])
assert first == [71, 50, 88, 62, 45, 34] and final == [88, 71, 62, 50, 45, 34]


# Q6 TicketCost
def ticket_cost(tickets, price):
    total = Fraction(tickets) * Fraction(str(price))
    if tickets >= 10:
        total = total * Fraction(85, 100)
    return total


assert ticket_cost(12, 5.00) == 51 and ticket_cost(9, 5.00) == 45 and 12 * 5 == 60 and 60 * 85 // 100 == 51

# Q8 queue
queue = [None] * 7
state = {"front": 1, "rear": 0}


def enq(x):
    state["rear"] += 1
    queue[state["rear"]] = x


def deq():
    if state["front"] > state["rear"]:
        return -1
    item = queue[state["front"]]
    state["front"] += 1
    return item


enq(14)
enq(9)
a = deq()
enq(21)
b = deq()
assert (a, b, state["front"], state["rear"]) == (14, 9, 3, 3) and deq() == 21 and deq() == -1
_, qrows = table_after("| Operation | FrontPointer | RearPointer | Returned |\n|---|---|---|---|\n| start | 1 | 0 | |")
assert qrows[-1] == ["dequeue", "3", "3", "9"]


# Q9 AddName with a real file
def add_name(folder, new):
    path = os.path.join(folder, "Names.txt")
    found = False
    with open(path) as f:
        for line in f.read().split("\n"):
            if line == "":
                continue
            if line == new:
                found = True
                break
    if found:
        return "Already present"
    with open(path, "a") as f:
        f.write(new + "\n")


with tempfile.TemporaryDirectory() as tmp:
    with open(os.path.join(tmp, "Names.txt"), "w") as f:
        f.write("Ana\nBo\n")
    assert add_name(tmp, "Bo") == "Already present" and add_name(tmp, "Cy") is None
    assert open(os.path.join(tmp, "Names.txt")).read() == "Ana\nBo\nCy\n"


# Q11 test plan: ages 11 to 19 inclusive
def accepts(text):
    return text.isdigit() and 11 <= int(text) <= 19


assert accepts("15") and accepts("11") and accepts("19") and not accepts("ten")
assert not accepts("10") and not accepts("20")


# Q12 ValidProduct, translated from the pseudocode
def valid_product(code):
    def mid(s, x, y):
        return s[x - 1:x - 1 + y]
    if len(code) != 6:
        return False
    total = 0
    for index in range(1, 6):
        if not mid(code, index, 1).isdigit():
            return False
        total += int(mid(code, index, 1)) * (7 - index)
    check_char = code[-1]
    if check_char == "X":
        check_value = 10
    else:
        if not check_char.isdigit():
            return False
        check_value = int(check_char)
    return (total + check_value) % 11 == 0


assert 3 * 6 + 0 * 5 + 5 * 4 + 9 * 3 + 1 * 2 == 67 == 18 + 0 + 20 + 27 + 2 and 67 + 10 == 77 == 7 * 11
assert valid_product("30591X") and valid_product("520470") and valid_product("416274")
assert not valid_product("305910") and not valid_product("52047") and not valid_product("5204X0") and not valid_product("30591Y")
assert checkdigit("52047") == (66, 0, 0) and checkdigit("30591") == (67, 1, 10)

print("ok")
