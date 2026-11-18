# checks/cs.mock.p2.py: Mock Paper 2: marks, the insert, the flowchart and every model answer translated and run
# (the helper below is the course's standard one; only CHAPTER_ID changes).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.mock.p2"

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
# Mock Paper 2: totals, the insert's examples, the flowchart, and every model answer translated
# into Python and run on the question's data.
# =============================================================================================
import datetime
import json
import random
import subprocess
import sys
from fractions import Fraction

assert run_python_blocks([]) == 0
lint_pseudocode_blocks()

# ---- structure: seven questions, 75 marks, 2 hours, links to real chapters
marks = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", TEXT, re.M)]
assert marks == [8, 9, 9, 10, 11, 12, 16], marks
assert sum(marks) == 75 and len(marks) == 7
assert "@time 2 h" in TEXT and "**2 hours**" in TEXT
assert Fraction(75 * 8, 5) == 120 and Fraction(10 * 8, 5) == 16
assert "1.6 minutes per mark" in TEXT and "a 10-mark question deserves about 16 minutes" in TEXT
assert "Calculators must not be used" in TEXT and "No marks will be awarded for using brand names" in TEXT
assert "Refer to the insert for the list of pseudocode functions and operators" in TEXT
ids = {c["id"] for c in json.loads((CHAPTER.parent.parent / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert len(re.findall(r"^Q: \[\d+ marks\] \(#cs\.\w+\)", TEXT, re.M)) == 7
assert "- `Next" not in TEXT and TEXT.rstrip().endswith("(#cs.mock.p3)")

# ---- the insert: every example is true, using the Python equivalents of the insert's functions
LEFT = lambda s, x: s[:x]
RIGHT = lambda s, x: s[len(s) - x:]


def MID(s, x, y):
    assert 1 <= x <= len(s) and y >= 0 and x - 1 + y <= len(s), f"badly formed MID({s!r}, {x}, {y})"
    return s[x - 1:x - 1 + y]


LENGTH = len
assert LEFT("Tropical", 4) == "Trop" and RIGHT("Tropical", 3) == "cal" and MID("Tropical", 2, 3) == "rop"
assert LENGTH("Tropical") == 8 and "Tropical".upper() == "TROPICAL" and "Q".lower() == "q"
assert str(47.5) == "47.5" and int("47") == 47 and "12".isdigit() and not "1A".isdigit()
assert ord("A") == 65 and chr(66) == "B" and int(27.9) == 27 and 0 <= random.random() * 10 < 10
d = datetime.date(2027, 3, 14)
assert d.year == 2027 and d.isoweekday() % 7 + 1 == 1          # DAYINDEX: Sunday is 1
assert "Sun" + "day" == "Sunday" and 19 % 6 == 1 and 19 // 6 == 3
for text in ['`LEFT("Tropical", 4)` returns `"Trop"`', '`RIGHT("Tropical", 3)` returns `"cal"`',
             '`MID("Tropical", 2, 3)` returns `"rop"`', '`LENGTH("Tropical")` returns `8`',
             "`ASC('A')` returns `65`", "`CHR(66)` returns `'B'`", "`INT(27.9)` returns `27`",
             "`YEAR(14/03/2027)` returns `2027`", "`DAYINDEX(14/03/2027)` returns `1`",
             "`19 MOD 6` is `1`; `19 DIV 6` is `3`", '`TO_LOWER(\'Q\')` returns `\'q\'`']:
    assert text in TEXT, text

# ---- Q1: identifier table
assert "| `Points` | `ARRAY[1:6, 1:4] OF INTEGER` |" in TEXT and "| `HouseName` | `ARRAY[1:6] OF STRING` |" in TEXT
assert 6 * 4 == 24 and "6 rows (houses) and 4 columns (events)" in TEXT

# ---- Q2: the flowchart figure, the three errors, and the corrected program
res = subprocess.run([sys.executable, str(CHAPTER.parent.parent / "data" / "cs.mock_figs.py")], capture_output=True, text=True)
assert res.returncode == 0 and res.stdout.startswith("ok"), res.stderr[-400:]
figtxt = (CHAPTER.parent.parent / "data" / "cs.mock_figs.txt").read_text(encoding="utf-8")
flow_svg = figtxt.split("### flow\n")[1].strip()
assert flow_svg in TEXT


def flowchart(heights):
    """the flowchart as drawn, with its three errors; heights are typed in when INPUT runs"""
    total = taller = 0
    count = 1
    typed = list(heights)
    while count < 8:                      # error 1
        height = typed.pop(0)
        total = height                    # error 2
        if height >= 170:                 # error 3
            taller += 1
        count += 1
    return taller, total / 8, len(heights) - len(typed)


def corrected(heights):
    total = taller = 0
    typed = list(heights)
    for count in range(1, 9):
        height = typed.pop(0)
        total = total + height
        if height > 170:
            taller += 1
    return taller, total / 8


H = [165, 170, 172, 180, 168, 171, 175, 159]
assert corrected(H) == (4, 1360 / 8) and sum(H) == 1360
t_bad, mean_bad, read = flowchart(H)
assert read == 7                                 # error 1: only 7 heights are read
assert mean_bad == H[6] / 8 and mean_bad != corrected(H)[1]   # error 2: Total holds only the last height read
assert t_bad == 5 != corrected(H)[0]             # error 3: 170 counted as taller (and the 8th height is missed)
# each error on its own
only3 = sum(1 for h in H if h >= 170)
assert only3 == 5 and corrected(H)[0] == 4        # the athlete exactly 170 cm tall is the difference
assert sum(1 for h in H if h > 170) == 4
for needle in ["Count ← 1` with the test `Count < 8?`", "`Count <= 8?`", "`Total ← Total + Height`", "`Height > 170?`",
               "FOR Count ← 1 TO 8", "Mean ← Total / 8"]:
    assert needle in TEXT, needle

# ---- Q3: the trace table
temps = [28, 31, 35, 29, 36, 33, 30]


def run_q3(temps):
    rowsout = []
    highest, day, hot = temps[0], 1, 0
    rowsout.append(["", str(highest), str(day), str(hot), ""])
    for index in range(1, 8):
        r = [str(index), "", "", "", ""]
        if temps[index - 1] > 30:
            hot += 1
            r[3] = str(hot)
        if temps[index - 1] > highest:
            highest = temps[index - 1]
            day = index
            r[1], r[2] = str(highest), str(day)
        rowsout.append(r)
    rowsout.append(["", "", "", "", f"{day} {highest} {hot}"])
    return rowsout


start = TEXT.index("(a)\n\n| Index | Highest | Day | Hot | OUTPUT |")
lines = [l for l in TEXT[start:].split("\n") if l.startswith("|")][2:11]
tab = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
assert tab == run_q3(temps), (tab, run_q3(temps))
assert run_q3(temps)[-1][4] == "5 36 4"
t2 = temps[:]
t2[2] = 30
assert run_q3(t2)[-1][4] == "5 36 3" and "The output is 5 36 3" in TEXT
assert sum(1 for t in temps if t > 30) == 4 and max(temps) == 36 and temps.index(36) + 1 == 5
assert len(re.findall(r"\| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 7 \|", TEXT)) == 1

# ---- Q4: the stack
Stack = [14, 8, 21, None, None, None]
Top = 3


def Push(item):
    global Top
    if Top == 6:
        return False
    Top = Top + 1
    Stack[Top - 1] = item
    return True


def Pop():
    global Top
    if Top == 0:
        return -1
    item = Stack[Top - 1]
    Top = Top - 1
    return item


log = []
log.append(("Push(30)", Push(30), Top))
log.append(("Pop", Pop(), Top))
log.append(("Pop", Pop(), Top))
log.append(("Push(5)", Push(5), Top))
assert log == [("Push(30)", True, 4), ("Pop", 30, 3), ("Pop", 21, 2), ("Push(5)", True, 3)]
assert Stack[:3] == [14, 8, 5]
for name, value, top in log:
    v = {True: "TRUE"}.get(value, str(value))
    assert f"| `{name}` | {v} | {top} |" in TEXT, (name, v, top)
# full and empty stacks
Stack[:] = [1, 2, 3, 4, 5, 6]
Top = 6
assert Push(7) is False and Top == 6 and Stack == [1, 2, 3, 4, 5, 6]
Top = 0
assert Pop() == -1 and Top == 0
for n in range(1, 7):
    assert Push(n * 10) is True
assert Top == 6 and [Pop() for _ in range(6)] == [60, 50, 40, 30, 20, 10] and Pop() == -1

# ---- Q5: the efficient bubble sort of two parallel arrays
def sort_swimmers(SwimmerName, SwimTime):
    """SwimTime[1:8] and SwimmerName[1:8] as Python lists with element 0 unused"""
    passes, swaps_per_pass, first = 0, [], None
    Limit = 7
    while True:
        Swapped = False
        swaps = 0
        for Index in range(1, Limit + 1):
            if SwimTime[Index] > SwimTime[Index + 1]:
                TempTime = SwimTime[Index]
                SwimTime[Index] = SwimTime[Index + 1]
                SwimTime[Index + 1] = TempTime
                TempName = SwimmerName[Index]
                SwimmerName[Index] = SwimmerName[Index + 1]
                SwimmerName[Index + 1] = TempName
                Swapped = True
                swaps += 1
        passes += 1
        swaps_per_pass.append(swaps)
        if first is None:
            first = SwimTime[1:]
        Limit = Limit - 1
        if Swapped is False or Limit == 0:
            break
    return passes, swaps_per_pass, first


times = [60, 55, 62, 51, 58, 70, 66, 64]
names = list("ABCDEFGH")
pairs = dict(zip(names, times))
passes, swaps, first = sort_swimmers([None] + names, [None] + times)
assert first == [55, 60, 51, 58, 62, 66, 64, 70] and swaps == [5, 3, 1, 0] and passes == 4
assert "55, 60, 51, 58, 62, 66, 64, 70" in TEXT and "5 swaps" in TEXT and "5, 3 and 1 swaps" in TEXT and "4 passes" in TEXT
nm, tm = [None] + names, [None] + times
sort_swimmers(nm, tm)
assert tm[1:] == sorted(times) and all(pairs[n] == t for n, t in zip(nm[1:], tm[1:]))
assert "SwimTime holds 60, 55, 62, 51, 58, 70, 66, 64".replace("SwimTime", "`SwimTime`") in TEXT
random.seed(5)
for _ in range(300):
    data = [random.randint(40, 90) for _ in range(8)]
    nms = [f"S{i}" for i in range(8)]
    original = dict(zip(nms, data))
    nm, tm = [None] + nms[:], [None] + data[:]
    p, sw, _ = sort_swimmers(nm, tm)
    assert tm[1:] == sorted(data) and all(original[n] == t for n, t in zip(nm[1:], tm[1:]))
    assert p <= 8
_, _, _ = sort_swimmers([None] + names, [None, 1, 2, 3, 4, 5, 6, 7, 8])
assert sort_swimmers([None] + names, [None, 1, 2, 3, 4, 5, 6, 7, 8])[0] == 1     # sorted data: one pass only
assert sort_swimmers([None] + names, [None, 8, 7, 6, 5, 4, 3, 2, 1])[0] == 7      # worst case stops when the range is 0
for needle in ["Limit ← 7", "UNTIL Swapped = FALSE OR Limit = 0", "SwimTime[Index] > SwimTime[Index + 1]"]:
    assert needle in TEXT

# ---- Q6: CleanBranchFile, translated and run on a real file
def clean_branch_file(folder):
    """a faithful translation of the model answer; MID, LEFT, RIGHT raise errors on badly formed calls"""
    import os
    old = os.getcwd()
    os.chdir(folder)
    out = []
    try:
        Valid = Invalid = Total = 0
        fin = open("Branch.txt")
        fout = open("Clean.txt", "w")
        lines = fin.read().split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        pos = 0
        while not (pos >= len(lines)):          # NOT EOF
            Line = lines[pos]
            pos += 1
            IsValid = False
            if LENGTH(Line) > 4:
                if MID(Line, 4, 1) == ":":
                    Quantity = RIGHT(Line, LENGTH(Line) - 4)
                    if Quantity.isdigit():       # IS_NUM for these lines
                        IsValid = True
            if IsValid is True:
                Code = LEFT(Line, 3).upper()
                Total = Total + int(Quantity)
                Valid = Valid + 1
                fout.write(Code + ":" + Quantity + "\n")
            else:
                Invalid = Invalid + 1
        fin.close()
        fout.close()
        out = (Valid, Invalid, Total)
        return out, open("Clean.txt").read()
    finally:
        os.chdir(old)


sample = ["lim:12", "ACC:7", "NAI:105", "KUL9", "SYD:4B", "DEL:20"]
block = re.search(r"```text\n(lim:12\n.*?)\n```", TEXT, re.S).group(1).split("\n")
assert block == sample
with tempfile.TemporaryDirectory() as tmp:
    pathlib.Path(tmp, "Branch.txt").write_text("\n".join(sample) + "\n")
    (valid, invalid, total), clean = clean_branch_file(tmp)
assert (valid, invalid, total) == (4, 2, 144) and clean == "LIM:12\nACC:7\nNAI:105\nDEL:20\n"
assert 12 + 7 + 105 + 20 == 144 and "The output is 4, 2 and 144" in TEXT and "12 + 7 + 105 + 20 = 144" in TEXT
# short and odd lines never reach MID with a bad position: lines of 0 to 4 characters are invalid
with tempfile.TemporaryDirectory() as tmp:
    pathlib.Path(tmp, "Branch.txt").write_text("\n".join(["", "AB", "ABC", "ABC:", "ABCD", "ABC:5"]) + "\n")
    assert clean_branch_file(tmp)[0] == (1, 5, 5)
for needle in ["IF LENGTH(Line) > 4 THEN", "IF MID(Line, 4, 1) = ':' THEN", "RIGHT(Line, LENGTH(Line) - 4)",
               'WRITEFILE "Clean.txt", Code & ":" & Quantity']:
    assert needle in TEXT, needle

# ---- Q7: CountFree, BookSeats, SaveSeats and Main, translated and run
Seat = [[None] * 9 for _ in range(6)]       # Seat[Row][Col], rows 1..5 and columns 1..8


def CountFree(Row):
    Count = 0
    for Col in range(1, 9):
        if Seat[Row][Col] == "F":
            Count = Count + 1
    return Count


def BookSeats(Row, Number):
    if CountFree(Row) < Number:
        return False
    Booked = 0
    Col = 1
    while Booked < Number:
        if Seat[Row][Col] == "F":
            Seat[Row][Col] = "S"
            Booked = Booked + 1
        Col = Col + 1
    return True


def SaveSeats(path):
    with open(path, "w") as f:
        for Row in range(1, 6):
            Line = ""
            for Col in range(1, 9):
                Line = Line + Seat[Row][Col]
            f.write(Line + "\n")


def main_program(Row, Number, folder):
    for r in range(1, 6):
        for c in range(1, 9):
            Seat[r][c] = "F"
    msg = "Booked" if BookSeats(Row, Number) is True else "Not enough seats"
    SaveSeats(os.path.join(folder, "Seats.txt"))
    return msg


with tempfile.TemporaryDirectory() as tmp:
    assert main_program(2, 3, tmp) == "Booked"
    assert pathlib.Path(tmp, "Seats.txt").read_text() == "FFFFFFFF\nSSSFFFFF\nFFFFFFFF\nFFFFFFFF\nFFFFFFFF\n"
    assert CountFree(2) == 5 and CountFree(1) == 8
    assert BookSeats(2, 6) is False and CountFree(2) == 5            # too few: nothing changes
    Seat[2][5] = "S"                                                  # a gap: first free seats are used, not a block
    assert BookSeats(2, 3) is True and "".join(Seat[2][1:]) == "SSSSSSSF" and CountFree(2) == 1
    assert BookSeats(2, 1) is True and CountFree(2) == 0 and BookSeats(2, 1) is False
    assert main_program(5, 9, tmp) == "Not enough seats"
    assert pathlib.Path(tmp, "Seats.txt").read_text() == "FFFFFFFF\n" * 5
    assert len(pathlib.Path(tmp, "Seats.txt").read_text().split("\n")[0]) == 8
for needle in ["IF CountFree(Row) < Number THEN", "IF BookSeats(Row, Number) = TRUE THEN", "CALL SaveSeats()",
               "Line ← Line & Seat[Row, Col]", "5 rows of 8"]:
    assert needle in TEXT, needle
print("ok")
