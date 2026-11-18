# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.exam.p2"

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
import tempfile
from fractions import Fraction

assert run_python_blocks([]) == 0
try:
    lint_pseudocode_blocks()
    raise SystemExit("the spot-the-error block should be unbalanced")
except AssertionError as err:  # block 4 is the student answer with the missing NEXT, on purpose
    assert "pseudocode block 4: FOR/NEXT 1/0" in str(err), err

# pace: 120 / 75 = 1.6 minutes a mark
RATE = Fraction(120, 75)
assert RATE == Fraction(8, 5)
for m, txt, rd in [(4, "6.4", 6), (6, "9.6", 10), (8, "12.8", 13), (10, "16.0", 16), (12, "19.2", 19)]:
    assert f"{float(m * RATE):.1f}" == txt, m
    assert int(m * RATE + Fraction(1, 2)) == rd, m
    assert f"| {m} | {txt} | {rd} |" in TEXT, m
assert r"\(12 \times 1.6 = 19.2\)" in TEXT and "so about 19 minutes" in TEXT

# DIV and MOD facts in the technique check
assert (17 // 5, 17 % 5) == (3, 2) and (10 // 3, 10 % 3) == (3, 1)

# trace: even digits of 4683 (one row per change)
number, total, rows, digit = 4683, 0, [("Number", 4683), ("Total", 0)], None
while number > 0:
    digit = number % 10
    rows.append(("Digit", digit))
    if digit % 2 == 0:
        total += digit
        rows.append(("Total", total))
    number = number // 10
    rows.append(("Number", number))
out = f"Even total: {total}"
rows.append(("OUTPUT", out))
assert total == 18 and number == 0
header, trows = table_after("| Number | Digit | Total | OUTPUT |")
assert header == ["Number", "Digit", "Total", "OUTPUT"]
got = []
for r in trows:
    filled = [(header[i], c) for i, c in enumerate(r) if c != ""]
    assert len(filled) == 1, r
    k, v = filled[0]
    got.append((k, v if k == "OUTPUT" else int(v)))
assert got == rows, (got, rows)
assert [v for k, v in rows if k == "Digit"] == [3, 8, 6, 4]
assert [v for k, v in rows if k == "Total"] == [0, 8, 14, 18]
assert [v for k, v in rows if k == "Number"] == [4683, 468, 46, 4, 0]


# ValidCode, translated from the pseudocode (positions start at 1)
def valid_code(code):
    def mid(s, x, y):
        return s[x - 1:x - 1 + y]
    if len(code) != 6:
        return False
    for index in range(1, 3):
        if ord(mid(code, index, 1)) < 65 or ord(mid(code, index, 1)) > 90:
            return False
    for index in range(3, 7):
        if not mid(code, index, 1).isdigit():
            return False
    return True


assert valid_code("KT4021") and not valid_code("kt4021") and not valid_code("K14021")
assert not valid_code("KT402") and not valid_code("KT40211") and not valid_code("KT40A1")
assert ord("A") == 65 and ord("Z") == 90 and ord("0") == 48 and ord("9") == 57


# ProcessReadings, translated, with a real file
def process_readings(folder):
    count, highest = 0, None
    with open(os.path.join(folder, "Readings.txt")) as src, open(os.path.join(folder, "Alerts.txt"), "w") as alerts:
        for line in src.read().split("\n"):
            if line == "":
                continue
            value = float(line)
            count += 1
            if count == 1 or value > highest:
                highest = value
            if value > 30.0:
                alerts.write(line + "\n")
    return count, highest


with tempfile.TemporaryDirectory() as tmp:
    with open(os.path.join(tmp, "Readings.txt"), "w") as f:
        f.write("24.5\n31.0\n28.5\n33.5\n29.0\n")
    assert process_readings(tmp) == (5, 33.5)
    assert open(os.path.join(tmp, "Alerts.txt")).read() == "31.0\n33.5\n"
    with open(os.path.join(tmp, "Readings.txt"), "w") as f:
        f.write("-5.0\n-2.5\n")
    assert process_readings(tmp) == (2, -2.5)  # a start at 0.0 would have given the wrong highest

# spot the error: one B0, total 3 of 4
assert 4 - 1 == 3

print("ok")
