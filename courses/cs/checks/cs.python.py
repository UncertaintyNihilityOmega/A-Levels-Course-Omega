# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.python"

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


INPUTS = [("Choose", ["x", "9", "4"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 17, f"expected 17 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 3

# ---------------------------------------------------------------------------------------------
# Numbers in the text (every Python block above has already been run and its output compared)
# ---------------------------------------------------------------------------------------------
assert 150 / 75 == 2 and 25 * 2 == 50 and 30 * 2 == 60 and 20 + 25 + 30 == 75
assert (17 // 5, 17 % 5) == (3, 2)

# translation table: slices and functions
word = "Computer"
assert word[2:2 + 4] == "mput" == word[2:6] and word[:3] == "Com" and word[3:] == "puter"
assert word[-2:] == "er" and word[:3] == "Com"
assert "Computer"[2:6] == "mput"                      # quiz
assert list(range(1, 6)) == [1, 2, 3, 4, 5] and list(range(10, 1, -2)) == [10, 8, 6, 4, 2]
assert [chr(ord("a") + 2), chr(66), ord("A")] == ["c", "B", 65]

# program 1 of the translation example (pseudocode semantics, 1-based array)
marks = [71, 45, 88, 50, 62, 38]
total = sum(marks)
assert total == 354 and total / 6 == 59.0 and total % 10 == 4 and total // 10 == 35
assert sum(1 for m in marks if m >= 50) == 4

# program 2 (REPEAT ... UNTIL): the body runs first
value, count = 3, 0
while True:
    value *= 2
    count += 1
    if value > 100:
        break
assert (count, value) == (6, 192)

# program 3: grade and swap
def grade(m): return "A" if m >= 80 else ("B" if m >= 50 else "C")
low, high = 90, 40
low, high = high, low
assert (low, grade(low), high, grade(high)) == (40, "C", 90, "A")

# circular queue arithmetic
assert (5 + 1) % 6 == 0 and 6 % 6 == 0

# debugging stretch: the corrected average
good = [m for m in [72, -1, 58, 90, 64] if m >= 0]
assert sum(good) == 284 and sum(good) / len(good) == 71.0
assert "10" < "9" and "5" + "3" == "53" and 5 + 3 == 8 and 7 / 2 == 3.5 and 7 // 2 == 3 and -7 // 2 == -4

# seats: 20 seats, 3 booked
assert 4 * 5 - 3 == 17

# payroll
assert 40 * 20 == 800 and 35 * 22 == 770 and 40 * 30 + 150 == 1350 and 800 + 770 + 1350 == 2920

# orders
assert 40 + 25 == 65 and 15 + 35 == 50

# trace question
vals = [4, 7, 1, 9]
tot = 0
for i in range(1, len(vals)):
    if vals[i] > vals[i - 1]:
        tot += vals[i]
assert tot == 16 and vals[len(vals) - 1] == 9 and vals[-2] == 1

print("ok")
