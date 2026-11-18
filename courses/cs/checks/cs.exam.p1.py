# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.exam.p1"

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


import sqlite3

assert run_python_blocks([]) == 0
assert lint_pseudocode_blocks() == 0

# paper facts: 8 questions of 4, 13, 7, 6, 13, 14, 11, 7 marks = 75
MARKS = [4, 13, 7, 6, 13, 14, 11, 7]
assert sum(MARKS) == 75 and len(MARKS) == 8
assert "4, 13, 7, 6, 13, 14, 11 and 7 marks, adding to 75" in TEXT

# pace: 90 / 75 = 1.2 minutes a mark
assert 90 / 75 == 1.2
from fractions import Fraction
RATE = Fraction(90, 75)
rows = {4: "4.8", 6: "7.2", 7: "8.4", 11: "13.2", 13: "15.6", 14: "16.8"}
rounded = {4: 5, 6: 7, 7: 8, 11: 13, 13: 16, 14: 17}
for m, txt in rows.items():
    assert float(m * RATE) == float(txt), m
    assert int(m * RATE + Fraction(1, 2)) == rounded[m], m
    assert f"| {m} | {txt} | {rounded[m]} |" in TEXT, m
paced = [int(m * RATE + Fraction(1, 2)) for m in MARKS]
assert paced == [5, 16, 8, 7, 16, 17, 13, 8] and sum(paced) == 90
assert "about 5, 16, 8, 7, 16, 17, 13 and 8 minutes" in TEXT
assert float(9 * RATE) == 10.8 and r"10.8\) minutes, so about 11" in TEXT

# file-size example: 1024 x 512, 16 bits
bits = 1024 * 512 * 16
assert bits == 2 ** 23 and bits // 8 == 2 ** 20 and bits // 8 // 2 ** 20 == 1
assert 1024 == 2 ** 10 and 512 == 2 ** 9 and 16 == 2 ** 4
# sound: 8000 Hz, 16 bits, 30 s, mono
sbits = 8000 * 16 * 30
assert sbits == 3_840_000 and sbits // 8 == 480_000 and 8000 * 30 == 240_000
assert r"3\,840\,000" in TEXT and r"480\,000" in TEXT

# binary sum in the technique check
assert 0b10110110 + 0b00001101 == 0b11000011 == 195 and 0b10110110 == 182
assert r"(\(182 + 13 = 195\))" in TEXT

# trace table of the assembly program
PROG = [("LDD", 122), ("ADD", 120), ("STO", 122), ("LDD", 121), ("SUB", 1), ("STO", 121),
        ("CMP", 0), ("JPN", 100), ("LDD", 122), ("OUT", None), ("END", None)]
mem = {120: 33, 121: 2, 122: 0}
acc, pc, flag, out = 0, 100, None, ""
trace = []
while True:
    op, arg = PROG[pc - 100]
    before_acc, before_mem = acc, dict(mem)
    nxt = pc + 1
    if op == "LDD":
        acc = mem[arg]
    elif op == "ADD":
        acc += mem[arg]
    elif op == "SUB":
        acc -= arg
    elif op == "STO":
        mem[arg] = acc
    elif op == "CMP":
        flag = acc == arg
    elif op == "JPN":
        if not flag:
            nxt = arg
    elif op == "OUT":
        out += chr(acc)
    row = {"addr": str(pc)}
    # the Instruction address column: ACC shown when the instruction writes it
    if op in ("LDD", "ADD", "SUB"):
        row["acc"] = str(acc)
    for a in (120, 121, 122):
        if mem[a] != before_mem[a]:
            row[a] = str(mem[a])
    if op == "OUT":
        row["out"] = chr(acc)
    trace.append(row)
    if op == "END":
        break
    pc = nxt
assert out == "B" and mem[122] == 66 and mem[121] == 0 and chr(66) == "B" and 33 * 2 == 66
header, trows = table_after("| Instruction address | ACC | 120 | 121 | 122 | OUTPUT |")
assert header == ["Instruction address", "ACC", "120", "121", "122", "OUTPUT"]
assert trows[0] == ["(start)", "", "33", "2", "0", ""]
trows = trows[1:]
assert len(trows) == len(trace) == 19, (len(trows), len(trace))
for got, want in zip(trows, trace):
    exp = [want["addr"], want.get("acc", ""), want.get(120, ""), want.get(121, ""), want.get(122, ""), want.get("out", "")]
    assert got == exp, (got, exp)
# addresses 100 to 107 appear twice
assert [r["addr"] for r in trace] == [str(a) for a in list(range(100, 108)) * 2 + [108, 109, 110]]

# SQL example, run on the data in the chapter
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE Bike (BikeID TEXT PRIMARY KEY, Model TEXT, DailyRate INTEGER);
CREATE TABLE Hire (HireID TEXT PRIMARY KEY, BikeID TEXT, HireDate TEXT, Days INTEGER);
""")
bh, brows = table_after("| BikeID | Model | DailyRate |")
db.executemany("INSERT INTO Bike VALUES (?,?,?)", [(r[0], r[1], int(r[2])) for r in brows])
hh, hrows = table_after("| HireID | BikeID | HireDate | Days |")
db.executemany("INSERT INTO Hire VALUES (?,?,?,?)", [(r[0], r[1], r[2], int(r[3])) for r in hrows])
assert len(brows) == 4 and len(hrows) == 7
sql = re.search(r"```text\n(SELECT Bike\.Model.*?;)\n```", TEXT, re.S).group(1)
result = db.execute(sql).fetchall()
oh, orows = table_after("| Model | SUM(Hire.Days) |")
assert [(r[0], int(r[1])) for r in orows] == result == [("Andes", 6), ("Pampa", 1), ("Sierra", 7)], result
assert "Coast" not in [r[0] for r in result]

print("ok")
