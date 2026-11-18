# checks/cs.mock.p1.py: Mock Paper 1: marks, the circuit figure and every number in the mark schemes
# (the helper below is the course's standard one; only CHAPTER_ID changes).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.mock.p1"

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
# Mock Paper 1: totals, figure, and every number in the mark schemes
# =============================================================================================
import json
import sqlite3
import subprocess
import sys
from fractions import Fraction

assert run_python_blocks([]) == 0
lint_pseudocode_blocks()

# ---- structure: nine questions, 75 marks, the real paper's time, links to real chapters
marks = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", TEXT, re.M)]
assert marks == [8, 8, 8, 5, 8, 11, 9, 7, 11], marks
assert sum(marks) == 75 and len(marks) == 9
assert "@time 1 h 30 min" in TEXT
assert Fraction(75 * 6, 5) == 90 and "1.2 minutes per mark" in TEXT and "a 5-mark question deserves about 6 minutes" in TEXT
assert "Calculators must not be used" in TEXT and "No marks will be awarded for using brand names" in TEXT
ids = {c["id"] for c in json.loads((CHAPTER.parent.parent / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert len(re.findall(r"^Q: \[\d+ marks\] \(#cs\.\w+\)", TEXT, re.M)) == 9

# ---- the circuit figure: geometry checked by data/cs.mock_figs.py, and the chapter holds exactly its SVG
res = subprocess.run([sys.executable, str(CHAPTER.parent.parent / "data" / "cs.mock_figs.py")], capture_output=True, text=True)
assert res.returncode == 0 and res.stdout.startswith("ok"), res.stderr[-400:]
figtxt = (CHAPTER.parent.parent / "data" / "cs.mock_figs.txt").read_text(encoding="utf-8")
circuit = figtxt.split("### flow")[0].replace("### circuit\n", "").strip()
assert circuit in TEXT

# ---- Q1: two's complement, addition, BCD
assert format((-45) % 256, "08b") == "11010011" and format(45, "08b") == "00101101"
assert format(~45 & 255, "08b") == "11010010" and (~45 & 255) + 1 == 0b11010011
a, b = 0b01101001, 0b00110111
assert (a, b) == (105, 55) and a + b == 160 and format(a + b, "08b") == "10100000"
assert a + b > 127 and (a + b) - 256 == -96     # as 8-bit two's complement the result reads as -96
assert a < 128 and b < 128                       # both leftmost bits 0
bcd = " ".join(format(int(d), "04b") for d in "2058")
assert bcd == "0010 0000 0101 1000"

# ---- Q2: file sizes, RLE
bits = 1024 * 512 * 24
assert bits // 8 == 1572864 and Fraction(bits, 8 * 1024 * 1024) == Fraction(3, 2) and 1024 * 512 == 2 ** 19
assert "1\\,572\\,864" in TEXT
sbits = 8000 * 16 * 30
assert sbits == 3840000 and sbits // 8 == 480000 and sbits // 8 // 1000 == 480
assert "3\\,840\\,000" in TEXT and "480 000 bytes" in TEXT


def rle(s):
    out, i = "", 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out += f"{j - i}{s[i]}"
        i = j
    return out


pixels = "WWWWWWWWWBBBWWWWWWWWBBBB"
assert len(pixels) == 24 and rle(pixels) == "9W3B8W4B" and "`9W3B8W4B`" in TEXT and f"`{pixels}`" in TEXT

# ---- Q3: nothing numerical except the 29 other computers
assert 30 - 1 == 29 and "the other 29 keep working" in TEXT

# ---- Q5: truth table of X = (A XOR B) OR (B NOR C), and the conveyor expression
want = []
for A in (0, 1):
    for B in (0, 1):
        for C in (0, 1):
            P = A ^ B
            Q = int(not (B or C))
            X = P | Q
            want.append([A, B, C, P, Q, X])
got = []
for line in TEXT.split("\n"):
    cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else []
    if len(cells) == 6 and all(c in ("0", "1") for c in cells):
        got.append([int(c) for c in cells])
assert got == want, got
assert [r[3] for r in want] == [0, 0, 1, 1, 1, 1, 0, 0] and [r[4] for r in want] == [1, 0, 0, 0, 1, 0, 0, 0]
assert "P column is correct: 0 0 1 1 1 1 0 0" in TEXT and "Q column is correct: 1 0 0 0 1 0 0 0" in TEXT
for S in (0, 1):
    for G in (0, 1):
        for O in (0, 1):
            assert (S and (G or O)) == ((S and G) or (S and O))   # the accepted alternative is equivalent

# ---- Q6: simulate the assembly program and compare with the printed trace table
prog = {100: ("LDR", 0), 101: ("LDX", 200), 102: ("CMP", 0), 103: ("JPE", 108), 104: ("AND", 0b11011111),
        105: ("OUT", None), 106: ("INC", "IX"), 107: ("JMP", 101), 108: ("END", None)}
for line in ["100   LDR #0", "101   LDX 200", "102   CMP #0", "103   JPE 108", "104   AND B11011111", "105   OUT",
             "106   INC IX", "107   JMP 101", "108   END"]:
    assert line in TEXT, line
mem = {200: 103, 201: 0}
acc = ix = 0
flag = None
pc = 100
trace = []
while True:
    op, arg = prog[pc]
    row = {"addr": pc, "ACC": "", "IX": "", "OUT": ""}
    pc += 1
    if op == "LDR":
        ix = arg
        row["IX"] = ix
    elif op == "LDX":
        acc = mem[arg + ix]
        row["ACC"] = acc
    elif op == "CMP":
        flag = acc == arg
    elif op == "JPE":
        if flag:
            pc = arg
    elif op == "AND":
        acc &= arg
        row["ACC"] = acc
    elif op == "OUT":
        row["OUT"] = chr(acc)
    elif op == "INC":
        ix += 1
        row["IX"] = ix
    elif op == "JMP":
        pc = arg
    trace.append(row)
    if op == "END":
        break
assert [r["addr"] for r in trace] == [100, 101, 102, 103, 104, 105, 106, 107, 101, 102, 103, 108]
assert mem[200] == ord("g") == 103 and ord("A") == 65 and ord("G") == 71 and 103 & 0b11011111 == 71
assert 0b11011111 == 255 - 32 and ord("g") - ord("G") == 32
# the trace table in the answer (the one with the filled columns)
start = TEXT.index("(c)(i)\n\n| Instruction address | ACC | IX | OUTPUT |")
lines = [l for l in TEXT[start:].split("\n") if l.startswith("|")][2:14]
tab = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
assert len(tab) == 12
for r, t in zip(trace, tab):
    assert t == [str(r["addr"]), str(r["ACC"]), str(r["IX"]), str(r["OUT"])], (t, r)

# ---- Q8: the received block, even parity, one bit changed
sent_rows = ["1011001", "0110111", "1100010", "0001110"]
sent = [str(r.count("1") % 2) + r for r in sent_rows]
sent.append("".join(str(sum(int(s[i]) for s in sent) % 2) for i in range(8)))
assert sent == ["01011001", "10110111", "11100010", "10001110", "10000010"]
recv = [list(s) for s in sent]
recv[2][4] = "1"                                  # Byte 3, column 4 of 0..7 = bit 4 (columns: parity, bit 7 ... bit 1)
header = ["Parity bit", "Bit 7", "Bit 6", "Bit 5", "Bit 4", "Bit 3", "Bit 2", "Bit 1"]
assert header[4] == "Bit 4" and sent[2][4] == "0"
tbl = [l for l in TEXT.split("\n") if re.match(r"^\| (Byte \d|Parity byte) \|", l)]
assert len(tbl) == 5
for l, r in zip(tbl, recv):
    cells = [c.strip() for c in l.strip().strip("|").split("|")][1:]
    assert cells == r, (cells, r)
rowtot = [sum(map(int, r)) for r in recv]
coltot = [sum(int(r[i]) for r in recv) for i in range(8)]
assert [i for i, t in enumerate(rowtot) if t % 2] == [2] and rowtot[2] == 5
assert [i for i, t in enumerate(coltot) if t % 2] == [4] and coltot[4] == 3
assert "(5)" in TEXT and "(3)" in TEXT

# ---- Q9: the SQL query on the sample data
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE VET (VetID TEXT, VetName TEXT);"
                 "CREATE TABLE VISIT (VisitID INTEGER, VisitDate TEXT, PetID TEXT, VetID TEXT, Fee INTEGER);")
_, vrows = table_after("| VetID | VetName |")
db.executemany("INSERT INTO VET VALUES (?,?)", vrows)
_, wrows = table_after("| VisitID | VisitDate | PetID | VetID | Fee |")
db.executemany("INSERT INTO VISIT VALUES (?,?,?,?,?)", [(int(a), b, c, d, int(e)) for a, b, c, d, e in wrows])
assert len(vrows) == 3 and len(wrows) == 5
sql = re.search(r"```text\n(SELECT VISIT\.VisitDate.*?)\n```", TEXT, re.S).group(1)
out = db.execute(sql).fetchall()
assert out == [("2027-03-02", "Dr Silva", 2500), ("2027-03-04", "Dr Silva", 3200),
               ("2027-03-05", "Dr Rajan", 2200), ("2027-03-09", "Dr Perera", 4000)], out
assert "2027-03-02, Dr Silva, 2500; 2027-03-04, Dr Silva, 3200; 2027-03-05, Dr Rajan, 2200; 2027-03-09, Dr Perera, 4000" in TEXT
assert "four rows" in TEXT and len(out) == 4
# the 3NF design: every field of the original table sits in a table of the design
design = {"OWNER": ["OwnerID", "OwnerName", "OwnerPhone"], "PET": ["PetID", "PetName", "Species", "OwnerID"],
          "VET": ["VetID", "VetName"], "VISIT": ["VisitID", "VisitDate", "PetID", "VetID", "Fee"]}
original = ["VisitID", "VisitDate", "PetID", "PetName", "Species", "OwnerID", "OwnerName", "OwnerPhone", "VetID", "VetName", "Fee"]
assert set(f for fs in design.values() for f in fs) == set(original)
print("ok")
