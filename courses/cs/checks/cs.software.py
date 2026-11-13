# checks/cs.software.py: runs every Python block in the chapter and recomputes every number it states
# (fragment jumps, the watch-window table, back-up totals, the stated error messages).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.software"

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



import subprocess
import sys

blocks = run_python_blocks([])
assert blocks == 5, f"expected 5 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 0

# Defragmentation figure and jump counts (the figure is generated by data/cs.software_fig.py)
before, after = "ABACBFACFBFC", "AAABBBCCCFFF"
assert sorted(before) == sorted(after)
assert [i + 1 for i, c in enumerate(before) if c == "A"] == [1, 3, 7]
assert [i + 1 for i, c in enumerate(before) if c == "B"] == [2, 5, 10]
assert [i + 1 for i, c in enumerate(before) if c == "C"] == [4, 8, 12]
assert [i + 1 for i, c in enumerate(before) if c == "F"] == [6, 9, 11]
assert after.index("AAA") == 0 and after.index("BBB") == 3 and after.index("CCC") == 6 and after.index("FFF") == 9

# Library block
import math, statistics
assert (math.sqrt(144), math.floor(7.9)) == (12.0, 7)
assert statistics.mean([4, 8, 15, 16, 23, 42]) == 18

# Watch-window example: the bug skips marks[0]
marks = [14, 9, 17, 12]
assert sum(marks) == 52 and sum(marks) / 4 == 13.0
total, rows = 0, []
for i in range(1, len(marks)):
    total += marks[i]
    rows.append((i, total))
assert rows == [(1, 9), (2, 26), (3, 38)] and total / len(marks) == 9.5
header, trows = table_after("| After the loop body runs |")
assert column_values(header, trows, "`i`") == [str(r[0]) for r in rows]
assert column_values(header, trows, "`total`") == [str(r[1]) for r in rows]

# Exam practice: the lowest-temperature program prints 18 3
temps = [21, 18, 25, 19]
lowest, position = temps[0], 0
for i in range(1, len(temps)):
    if temps[i] < lowest:
        lowest = temps[i]
    position = i
assert (i, lowest, position) == (3, 18, 3) and temps.index(18) == 1

# Try it: compression factor
assert 2 / 0.5 == 4

# Stretch: back-up totals
assert 400 * 5 // 100 == 20
assert 7 * 400 == 2800 and 400 + 6 * 20 == 520
assert ["Monday", "Tuesday", "Wednesday", "Thursday"].__len__() == 4   # incrementals up to Thursday night

# The error message shown in the chapter is what Python really prints
import tempfile, os
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "demo.py")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(['print("Step 1 done")', 'print("Step 2 done")', "print(10 / 0)", 'print("Step 4 never runs")']) + "\n")
    run = subprocess.run([sys.executable, "demo.py"], cwd=tmp, capture_output=True, text=True)
    assert run.stdout.splitlines() == ["Step 1 done", "Step 2 done"]
    err = run.stderr.strip().splitlines()
    assert err[0] == "Traceback (most recent call last):" and err[-1] == "ZeroDivisionError: division by zero"
    assert 'line 3, in <module>' in err[1] and err[2].strip() == "print(10 / 0)"

FIGS = (pathlib.Path(__file__).resolve().parent.parent / "data" / "cs.software_figs.txt").read_text(encoding="utf-8").split("\n\n")
assert len(FIGS) == 3 and all(f.strip().split("<figcaption>")[0] in TEXT for f in FIGS), "a figure differs from data/cs.software_figs.txt"
for brand in ("Windows", "Microsoft", "Google", "Apple", "Linux", "Android"):
    assert brand not in TEXT, brand

print("ok")
