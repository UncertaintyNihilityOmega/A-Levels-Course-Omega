# checks/cs.processor.py: recomputes every number in the chapter, including the fetch-execute register table
# (from the assembly simulator in data/cs.asmsim.py, the same one cs.assembly uses).
import pathlib
import re
import runpy

CHAPTER_ID = "cs.processor"
ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = (ROOT / "chapters" / f"{CHAPTER_ID}.md").read_text(encoding="utf-8")
FENCES = list(re.finditer(r"^```(\w+)\n(.*?)^```", TEXT, re.S | re.M))
SIM = runpy.run_path(str(ROOT / "data" / "cs.asmsim.py"))
run = SIM["run"]


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


# ---------------------------------------------------------------------------------------------
# Warm-up and buses
# ---------------------------------------------------------------------------------------------
assert 2 ** 4 == 16 and format(10, "04b") == "1010" and format(10, "X") == "A" and 7 + 1 == 8
assert 2 ** 16 == 65536 and 2 ** 6 * 2 ** 10 == 64 * 1024 == 2 ** 16
assert 128 // 32 == 4 and 128 // 8 == 16 and 16 // 4 == 4
assert 100 * 50 == 5000 and 90 * 2 + 10 * 50 == 680
assert 2 ** 10 == 1024 and 2 ** 8 == 256 and 2 ** 32 == 4294967296 and 2 ** 32 // 2 ** 16 == 65536
assert 4 * 10 ** 9 == 4_000_000_000 and 2 * 10 ** 9 == 2_000_000_000
assert 2 ** 12 == 4096 and 4096 * 16 == 65536 and 4096 - 3000 == 1096
assert 4096 + 10000 == 14096 and 2 ** 13 == 8192 < 14096 <= 2 ** 14 == 16384

# ---------------------------------------------------------------------------------------------
# The fetch-execute table: rebuilt from the simulator, one register transfer per row
# ---------------------------------------------------------------------------------------------
prog = block_after("The program below adds two numbers")
assert prog.strip().split("\n") == ["100  LDD 200", "101  ADD 201", "102  STO 202", "103  END", "200  7", "201  5"]
steps, final = run(prog)
assert final["mem"][202] == 12 and final["acc"] == 12
header, rows = table_after("The first two instructions of the program")
assert header == ["Step", "Register transfer", "PC", "MAR", "MDR", "CIR", "ACC"]
assert rows[0] == ["start", "", "100", "", "", "", ""]
expected = []
n = 0
for s in steps[:2]:
    for txt, regs in s["micro"]:
        n += 1
        expected.append([str(n), f"`{txt}`"] + [str(regs.get(k, "")) for k in ("PC", "MAR", "MDR", "CIR", "ACC")])
assert rows[1:] == expected, f"fetch-execute table differs:\n{rows[1:]}\n{expected}"
assert len(expected) == 14
# steps 15 to 21 are the six transfers of STO 202 plus its fetch: seven rows
assert len(steps[2]["micro"]) == 7 and steps[2]["micro"][-1][1] == {"mem": {202: 12}}

# compare and conditional jump table: steps 1 to 11 are the CMP and JPE instructions
cj = block_after("compares the accumulator with 5 and jumps")
assert cj.strip().split("\n") == ["100  LDM #5", "101  CMP #5", "102  JPE 104", "103  END", "104  END"]
cs, cf = run(cj)
assert [s["addr"] for s in cs] == [100, 101, 102, 104]
header, rows = table_after("The table starts just after")
assert header == ["Step", "Register transfer", "PC", "CIR", "ACC", "SR"]
assert rows[0] == ["start", "", "101", "LDM #5", "5", ""]
exp = []
n = 0
for s in cs[1:3]:
    for txt, regs in s["micro"]:
        n += 1
        exp.append([str(n), f"`{txt}`"] + [str(regs.get(k, "")) for k in ("PC", "CIR", "ACC", "SR")])
assert rows[1:] == exp, f"compare table differs:\n{rows[1:]}\n{exp}"
assert run("100 LDM #5\n101 CMP #4\n102 JPE 104\n103 END\n104 END")[0][-1]["addr"] == 103

# execute-stage table
sm = run("100 LDM #5\n101 END")[0][0]["micro"][4:]
assert [m[0] for m in sm] == ["ACC ← 5"]
ld = run("100 LDD 200\n101 END\n200 7")[0][0]["micro"][4:]
assert [m[0] for m in ld] == ["MAR ← 200", "MDR ← [[MAR]]", "ACC ← [MDR]"]
ad = run("100 LDM #3\n101 ADD 201\n102 END\n201 4")[0][1]["micro"][4:]
assert [m[0] for m in ad] == ["MAR ← 201", "MDR ← [[MAR]]", "ACC ← [ACC] + [MDR]"]
so = run("100 LDM #3\n101 STO 202\n102 END")[0][1]["micro"][4:]
assert [m[0] for m in so] == ["MAR ← 202", "MDR ← [ACC]", "[[MAR]] ← [MDR]"]
jm = run("100 JMP 102\n101 END\n102 END")[0][0]["micro"][4:]
assert [m[0] for m in jm] == ["PC ← 102"]

# ---------------------------------------------------------------------------------------------
# Interrupt example: the instruction at 102 has just been executed
# ---------------------------------------------------------------------------------------------
ex = run("100 LDM #1\n101 INC ACC\n102 INC ACC\n103 INC ACC\n104 END")[0]
assert ex[2]["addr"] == 102 and [m for m in ex[2]["micro"] if "PC" in m[1]][0][1]["PC"] == 103

# ---------------------------------------------------------------------------------------------
# Exam practice: ADD 201 with ACC = 7 and location 201 = 5; the LDM #9 fetch
# ---------------------------------------------------------------------------------------------
q = run("100 LDM #7\n101 ADD 201\n102 END\n201 5")
assert q[0][1]["acc"] == 12
prog2 = block_after("The program below is stored in memory, starting at address 100")
assert prog2.strip().split("\n") == ["100  LDM #9", "101  STO 210", "102  END"]
s2, f2 = run(prog2)
fetch = s2[0]["micro"][:4]
assert [m[0] for m in fetch] == ["MAR ← [PC]", "PC ← [PC] + 1", "MDR ← [[MAR]]", "CIR ← [MDR]"]
assert fetch[0][1] == {"MAR": 100} and fetch[1][1] == {"PC": 101}
assert fetch[2][1] == {"MDR": "LDM #9"} and fetch[3][1] == {"CIR": "LDM #9"}
assert f2["mem"][210] == 9

print("ok")
