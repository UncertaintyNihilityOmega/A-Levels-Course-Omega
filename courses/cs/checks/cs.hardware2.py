# checks/cs.hardware2.py: runs every Python block in the chapter and recomputes every number it states
# (pipeline timing diagrams and cycle counts, jump cost, SIMD steps, parallel speed-up, virtual machine load).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.hardware2"

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




# ---------------------------------------------------------------------------------------------
# Every Python block runs and prints exactly what the chapter shows
# ---------------------------------------------------------------------------------------------
blocks = run_python_blocks([])
assert blocks == 1, blocks


def table_after(marker, which=0):
    """Rows of the Markdown table that starts with the header line `marker` (the which-th occurrence)."""
    idx = -1
    for _ in range(which + 1):
        idx = TEXT.index(marker, idx + 1)
    lines = TEXT[idx:].split("\n\n")[0].split("\n")
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    return rows[0], rows[2:]


# warm-up and small numbers
assert 8 * 0.5 == 4.0 and 20 * 0.5 == 10.0 and 1 / 2e9 == 0.5e-9
assert 1 / 4e9 == 0.25e-9 and 8 * 0.25 == 2.0 and 1 / 2.5e9 == 0.4e-9

# RISC / CISC example: cycles chosen in the text
assert 1 * 6 == 6 and 4 * 1 == 4 and 6 > 4

# pipeline: the cycle counts and the timing diagrams, built from a cycle-by-cycle model
STAGES = ["IF", "ID", "OF", "EX", "WB"]
K = 5


def pipelined(n):
    return K + n - 1


def sequential(n):
    return K * n


def diagram(n):
    cycles = pipelined(n)
    rows = []
    for i in range(n):
        row = [""] * cycles
        for s, name in enumerate(STAGES):
            row[i + s] = name
        rows.append(row)
    return rows


assert (pipelined(4), sequential(4)) == (8, 20) and (pipelined(1), sequential(1)) == (5, 5)
assert (pipelined(10), sequential(10)) == (14, 50) and (pipelined(1000), sequential(1000)) == (1004, 5000)
assert (pipelined(3), sequential(3)) == (7, 15) and (pipelined(5), sequential(5)) == (9, 25)
assert round(5000 / 1004, 2) == 4.98

for marker, n in (("| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |", 4), ("| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |", 5)):
    # every table with this header that is fully shown (not the blank question tables)
    pos = 0
    shown = 0
    while True:
        try:
            idx = TEXT.index(marker + chr(10), pos)
        except ValueError:
            break
        pos = idx + 1
        lines = TEXT[idx:].split("\n\n")[0].split("\n")
        rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines][2:]
        names = [r[0] for r in rows]
        stage_cells = [r[1:] for r in rows]
        filled = sum(1 for r in stage_cells for c in r if c)
        if filled == K * n:  # a complete diagram
            assert stage_cells == diagram(n), (marker, stage_cells)
            shown += 1
        else:  # a question table: only the first row is filled
            assert filled == K and stage_cells[0][:K] == STAGES, marker
    assert shown >= 1, marker
assert TEXT.count("| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |" + chr(10)) == 2  # the timing diagram and the worked-example question
assert TEXT.count("| Instruction | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |") == 2

# four instructions in progress in cycle 4
d4 = diagram(4)
assert [d4[i][3] for i in range(4)] == ["EX", "OF", "ID", "IF"]


# the jump model: a jump at instruction b is settled at the end of EX; K - 2 = 3 instructions are flushed
def with_jump(n, b):
    return pipelined(n) + (K - 2 if 0 < b < n else 0)


assert with_jump(6, 3) == 13 == 10 + 3 and with_jump(8, 4) == 15 and with_jump(8, 4) - pipelined(8) == 3 and pipelined(8) == 12
assert with_jump(6, 0) == 10 and sequential(6) == 30 and round(30 / 13, 1) == 2.3 and round(sequential(8) / with_jump(8, 4), 2) == 2.67
assert 3 + 3 == 6  # the jump (cycle 3 start) finishes EX at cycle 6
assert 15 * 0.4 == 6.0

# laundry analogy
assert 3 * 3 == 9 and 3 + 3 - 1 == 5

# SIMD
assert 1024 // 8 == 128 and 4096 // 16 == 256 and 4096 // 256 == 16

# limits to parallel speed-up
assert 10 + 90 / 100 == 10.9 and round(100 / 10.9, 1) == 9.2
assert round(10 + 90 / 1000, 2) == 10.09 and round(100 / 10.09, 1) == 9.9 and 100 / 10 == 10
assert 180 / 2000 == 0.09 and round(20 + 180 / 2000, 2) == 20.09
assert round(20 + 180 / 1_000_000, 5) == 20.00018 and 10 + 90 / 1_000_000 > 10

# server consolidation
assert 6 * 12 == 72 and 6 * 2 == 12 and 72 + 12 == 84 and 100 - 84 == 16

# clock numbers in the practice section
assert round(1 / 4, 2) == 0.25

# the five stages and their short names appear in the chapter
for s in STAGES:
    assert f"| {s} |" in TEXT or f"{s}" in TEXT
for term in ("SISD", "SIMD", "MISD", "MIMD", "RISC", "CISC", "hypervisor"):
    assert term in TEXT
assert TEXT.count(":::def ") >= 13

# the time for a program: 1 000 000 instructions at 2 GHz
cyc = 1 / 2e9
assert abs(cyc - 0.5e-9) < 1e-18
assert pipelined(1_000_000) == 1_000_004 and sequential(1_000_000) == 5_000_000
assert round(1_000_004 * 0.5) == 500_002 and 5_000_000 * 0.5 == 2_500_000.0
assert round(5_000_000 / 1_000_004, 1) == 5.0

# the stall example: SUB needs R3, written by ADD in cycle 5, so it may read it in cycle 6
add_wb = 5
sub_if, sub_id = 2, 3
sub_of = max(sub_id + 1, add_wb + 1)
assert sub_of == 6
sub_row = [""] * 8
sub_row[sub_if - 1], sub_row[sub_id - 1] = "IF", "ID"
for c in range(sub_id + 1, sub_of):
    sub_row[c - 1] = "stall"
sub_row[sub_of - 1], sub_row[sub_of], sub_row[sub_of + 1] = "OF", "EX", "WB"
hdr, rows = table_after("| Instruction in the pipeline | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
assert rows[0][1:] == ["IF", "ID", "OF", "EX", "WB", "", "", ""] and rows[1][1:] == sub_row, rows
assert sub_row.index("WB") + 1 == 8 and pipelined(2) == 6 and 8 - 6 == 2

# the interrupt example: 204, 205 and 206 are the three instructions in IF, ID and OF behind the one that was completed
assert [203 + k for k in (1, 2, 3)] == [204, 205, 206] and K - 2 == 3

print("ok")
