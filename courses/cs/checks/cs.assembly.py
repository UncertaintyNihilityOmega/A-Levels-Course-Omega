# checks/cs.assembly.py: every assembly trace in the chapter is rebuilt by the simulator in data/cs.asmsim.py
# (a small Python model of the Cambridge example instruction set) and compared with the chapter's table;
# every program block is assembled and run, and every number (shifts, masks, machine code) is recomputed.
import pathlib
import re
import runpy

CHAPTER_ID = "cs.assembly"
ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = (ROOT / "chapters" / f"{CHAPTER_ID}.md").read_text(encoding="utf-8")
FENCES = list(re.finditer(r"^```(\w+)\n(.*?)^```", TEXT, re.S | re.M))
SIM = runpy.run_path(str(ROOT / "data" / "cs.asmsim.py"))
run, trace, assemble, OPS = SIM["run"], SIM["trace"], SIM["assemble"], SIM["OPS"]


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


def block_after(marker, lang="text"):
    start = TEXT.index(marker)
    for f in FENCES:
        if f.start() > start and f.group(1) == lang:
            return f.group(2)
    raise AssertionError(f"no {lang} block after {marker!r}")


def check_trace(prog_marker, table_marker, drop_output=False, extra="", **kw):
    prog = block_after(prog_marker) + extra
    header, rows = table_after(table_marker)
    eh, er = trace(prog, **kw)
    if drop_output:
        eh = eh[:-1]
        er = [r[:-1] for r in er]
    assert header == eh, f"{table_marker!r}: header {header} != {eh}"
    assert rows == er, f"{table_marker!r}: trace differs\nchapter {rows}\nsimulator {er}"
    return run(prog, kw.get("inputs", ""))[1]


b8 = lambda v: format(v, "08b")

# ---------------------------------------------------------------------------------------------
# Warm-up, machine code
# ---------------------------------------------------------------------------------------------
assert b8(44) == "00101100" and 32 + 8 + 4 == 44 and ord("A") == 65 and 65 + 3 == 68 == ord("D")
assert format(104, "010b") == "0001101000" and 64 + 32 + 8 == 104
OPCODE = {"LDD": "000010", "ADD": "000111", "STO": "000110", "END": "010011"}
assert OPCODE["LDD"] + " " + format(104, "010b") == "000010 0001101000"
assert "000010 0001101000" in TEXT
assert [format(a, "010b") for a in (104, 105, 106)] == ["0001101000", "0001101001", "0001101010"]
for line in ("000010 0001101000", "000111 0001101001", "000110 0001101010", "010011 0000000000", "0000000000000111"):
    assert line in TEXT
assert format(7, "016b") == "0000000000000111"

# the instruction table mentions every instruction of the example set
table_text = TEXT[TEXT.index("| Instruction | Operand | Explanation |"):TEXT.index("Three notation rules")]
for op in OPS:
    assert f"`{op}`" in table_text, op
assert 0b00011001 == 25 == 0x19 and 25 == int("00011001", 2)

# ---------------------------------------------------------------------------------------------
# Addressing modes
# ---------------------------------------------------------------------------------------------
MEM = "200 205\n201 7\n202 31\n203 12\n204 50\n205 99\n"
got = {}
for ins in ("LDM #200", "LDD 200", "LDI 200", "LDX 200"):
    got[ins] = run("100 LDR #2\n101 " + ins + "\n102 END\n" + MEM)[1]["acc"]
assert got == {"LDM #200": 200, "LDD 200": 205, "LDI 200": 99, "LDX 200": 31}
header, rows = table_after("| Instruction | What the processor does | ACC afterwards |")
assert [int(r[2]) for r in rows] == [200, 205, 99, 31]
for ix, want in enumerate([12, 30, 25, 8, 41]):
    assert run(f"100 LDR #{ix}\n101 LDX 150\n102 END\n150 12\n151 30\n152 25\n153 8\n154 41")[1]["acc"] == want
assert 105 + 3 == 108 and 105 - 2 == 103 and 120 + 4 == 124

# ---------------------------------------------------------------------------------------------
# Traces
# ---------------------------------------------------------------------------------------------
fin = check_trace("The label `START` marks the first instruction", "Complete a trace table for the program",
                  watch=["TOTAL"], start_row=True)
assert fin["mem"][106] == 12 and fin["labels"] == {"START": 100, "FIRST": 104, "SECOND": 105, "TOTAL": 106}

fin = check_trace("Trace this program until it ends", "Trace this program until it ends",
                  watch=[201, 202], start_row=True, show_cmp=True)
assert fin["mem"][202] == 12 == 6 * 2 and fin["mem"][201] == 0

fin = check_trace("The user types `q`", "The user types `q`", inputs="q")
assert fin["out"] == "Q" and ord("q") == 113 and ord("Q") == 81 and 113 - 32 == 81 and 97 - 65 == 32

fin = check_trace("Trace this program. Show IX", "Trace this program. Show IX",
                  watch=["TOTAL"], start_row=True, show_cmp=True)
assert fin["mem"][114] == 13 and fin["ix"] == 2

# the sum program in "Writing a program"
fin = run(block_after("Write assembly language to add the two numbers"))[1]
assert fin["mem"][152] == 12 + 30 - 5 == 37

# the spot-the-error trace: the right answer, and the student's wrong one
sp = block_after("Question: Location 150 holds 25.")
fin = run(sp)[1]
assert fin["mem"][151] == 45 == 20 + 25 and 20 + 150 == 170
header, rows = table_after("A student wrote this trace table")
assert rows[1][2] == "170" and rows[2][3] == "170"

# ---------------------------------------------------------------------------------------------
# Two-pass assembler
# ---------------------------------------------------------------------------------------------
sym = block_after("Use the program from the earlier trace")
_, labels, _ = assemble(sym)
header, rows = table_after("Pass 1 reads each line and records each label")
assert header == ["Label", "Address"] and {r[0]: int(r[1]) for r in rows} == labels == {"START": 100, "FIRST": 104, "SECOND": 105, "TOTAL": 106}
mem, labels, _ = assemble(sym)
header, rows = table_after("Pass 2 replaces each mnemonic")
expect = []
for addr in range(100, 105):
    item = mem[addr]
    if item[0] == "I":
        _, op, kind, val, src = item
        word = OPCODE[op] + " " + format(val if val is not None else 0, "010b")
        expect.append(word)
    else:
        expect.append(format(item[1], "016b"))
assert [r[2] for r in rows] == expect, (rows, expect)

# exam practice: symbol table for BEGIN
sy2 = block_after("An assembler uses two passes to translate it")
_, lab2, _ = assemble(sy2)
header, rows = table_after("A: (a) The symbol table:")
assert {r[0]: int(r[1]) for r in rows} == lab2 == {"BEGIN": 100, "AGAIN": 101, "LIMIT": 107, "TOTAL": 108}

# ---------------------------------------------------------------------------------------------
# Bit manipulation
# ---------------------------------------------------------------------------------------------
assert b8(0b00010110 << 1) == "00101100" and 0b00010110 << 1 == 44
assert b8(0b00010110 >> 2) == "00000101" and 22 // 4 == 5
assert b8((0b10010110 << 1) & 255) == "00101100" and 150 * 2 == 300 and (150 * 2) % 256 == 44
neg = 0b11110000
assert neg - 256 == -16 and b8(neg >> 1) == "01111000" and (neg >> 1) == 120
asr = lambda v, n: ((v >> n) | ((0xFF << (8 - n)) & 0xFF if v & 0x80 else 0)) & 0xFF
assert b8(asr(neg, 1)) == "11111000" and 0b11111000 - 256 == -8
assert b8((0b11111000 << 1) & 255) == "11110000" and 0b11110000 - 256 == -16
assert b8((0b01000000 << 1) & 255) == "10000000" and 0b10000000 - 256 == -128
rol = lambda v, n: ((v << n) | (v >> (8 - n))) & 0xFF
ror = lambda v, n: ((v >> n) | (v << (8 - n))) & 0xFF
x = 0b10010110
assert b8(rol(x, 1)) == "00101101" and b8(ror(x, 1)) == "01001011" and b8(rol(x, 3)) == "10110100" and rol(x, 8) == x
y = 0b10110110
assert b8(y & 0b00001111) == "00000110" and b8(y | 1) == "10110111" and b8(y ^ 0b11110000) == "01000110"
assert b8(1 << 3) == "00001000" and (~(1 << 2)) & 0xFF == 0b11111011 and (~(1 << 3)) & 0xFF == 0b11110111
assert 1 << 6 == 0b01000000 and 1 << 7 == 0b10000000

fin = check_trace("Trace the program when location 109 holds", "Trace the program when location 109 holds",
                  show_cmp=True, binary=True, cols=("ACC",))
assert fin["out"] == "Y" and ord("N") == 78 and ord("Y") == 89
# the other branch: bit 3 clear gives N
st2 = block_after("Trace the program when location 109 holds").replace("B01101100", "B01100100")
assert run(st2)[1]["out"] == "N"

fin = check_trace("Write the program and trace it when the sensor byte", "Write the program and trace it when the sensor byte",
                  drop_output=True, show_cmp=True, binary=True, cols=("ACC",), watch=["LIGHTS"], start_row=True)
assert fin["mem"][109] == 0b01000101

# ---------------------------------------------------------------------------------------------
# Practice answers
# ---------------------------------------------------------------------------------------------
M2 = "150 153\n151 8\n152 20\n153 41\n154 5\n"
res = [run("100 LDR #1\n101 " + i + "\n102 END\n" + M2)[1]["acc"] for i in ("LDM #150", "LDD 150", "LDI 150", "LDX 150")]
assert res == [150, 153, 41, 8]

# try questions
assert 7 + 5 - 3 + 1 == 10 and 100 + 3 == 103 and b8(0b10110110 & 0b1111) == "00000110"
assert b8(0b00000101 << 3) == "00101000" and 5 << 3 == 40 and 5 * 8 == 40
assert run("100 LDM #9\n101 CMP #9\n102 JPN 104\n103 END\n104 END")[0][-1]["addr"] == 103
assert run("100 LDM #65\n101 ADD #2\n102 OUT\n103 END")[1]["out"] == "C"

# exam practice: the IN program for A and B
prog = block_after("A program reads a character from the keyboard.")
fin = check_trace("A program reads a character from the keyboard.", "The trace for the character A:", inputs="A",
                  show_cmp=True, cols=("ACC",))
assert fin["out"] == "*" and ord("*") == 42 and run(prog, "B")[1]["out"] == "C" and ord("B") == 66

# write a program: add and subtract
fin = run(block_after("A model answer:") + "\n150 12\n151 30")[1]
assert fin["mem"][152] == 37

# masks for each part of the status register question
assert 0b01000000 == 1 << 6 and 0b11111011 == 0xFF ^ (1 << 2) and 0b00000001 == 1 << 0 and 0b10000000 == 1 << 7
for value in range(256):
    assert (value | 0b01000000) >> 6 & 1 == 1 and (value & 0b11111011) >> 2 & 1 == 0
    assert (value ^ 1) & 1 != value & 1 and ((value & 0b10000000) == 0) == (value >> 7 == 0)
    assert ((value | 0b01000000) & ~0b01000000) == (value & ~0b01000000)

# array loop with IX: the model answer
prog = block_after("A model answer, which stores 75")
fin = run(prog)[1]
assert fin["mem"][160] == 12 + 30 + 25 + 8 == 75 and fin["mem"][161] == 0 and fin["ix"] == 4

# shifts question
assert b8(0b00001101 << 2) == "00110100" and 13 * 4 == 52 == 0b00110100
assert b8(0b11001000 >> 3) == "00011001" and 200 // 8 == 25 == 0b00011001
assert 0b11001000 - 256 == -56 and b8(asr(0b11001000, 1)) == "11100100" and 0b11100100 - 256 == -28
assert b8(rol(0b10110001, 2)) == "11000110"

# stretch: times ten
prog = block_after("Show that it works when location 130 holds 7")
for v in range(0, 26):
    fin = run(prog + f"\n130 {v}")[1]
    assert fin["mem"][131] == 10 * v
assert 7 * 2 == 14 and 7 * 8 == 56 and 56 + 14 == 70

# stretch: counting the 1 bits
prog = block_after("Use location 119 as a loop counter")
for value in range(256):
    text = prog.replace("B10110100", b8(value).join(["B", ""]))
    fin = run(text)[1]
    assert fin["mem"][118] == bin(value).count("1")
assert bin(0b10110100).count("1") == 4 and run(prog)[1]["mem"][118] == 4

# quiz
assert b8(10 << 2) == "00101000" and b8(10 << 1) == "00010100"
assert 0b10000100 - 256 == -124 and b8(0b10000100 >> 1) == "01000010" and b8(asr(0b10000100, 1)) == "11000010" and 0b11000010 - 256 == -62

print("ok")
