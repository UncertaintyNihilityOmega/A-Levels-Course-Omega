# checks/cs.exam.p4.py: runs every Python block in the guide and recomputes every value it states.
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.exam.p4"

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


import json
from fractions import Fraction

ROOT = CHAPTER.parent.parent
assert run_python_blocks([]) == 3
assert lint_pseudocode_blocks() == 0
ids = {c["id"] for c in json.loads((ROOT / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\]\(#(cs\.[\w.]+)\)", TEXT)) <= ids

# pace
assert Fraction(150, 75) == 2 and r"\(150 \div 75 = 2\)" in TEXT
RATE = Fraction(9, 5)
for m, t in [(20, 36), (25, 45), (30, 54)]:
    assert m * RATE == t and f"| {m} | {t} |" in TEXT
assert sum(m * RATE for m in (20, 25, 30)) == 135 and 150 - 135 == 15 and 20 + 25 + 30 == 75
assert r"\(30 \times 1.8 = 54\)" in TEXT and "135, which leaves 15 minutes" in TEXT

# swimmers: the refused swimmer is the fastest overall; the fastest stored is Dev
data = [("Ana", 62.5), ("Ben", 58.2), ("Chi", 71.0), ("Dev", 55.9), ("Eli", 60.4), ("Fay", 59.8), ("Gus", 54.1)]
assert min(data, key=lambda x: x[1])[0] == "Gus" and min(data[:6], key=lambda x: x[1])[0] == "Dev"
assert len(data) == 7 and 6 + 1 == 7

# validation tests
def valid(t):
    try:
        s = float(t)
    except ValueError:
        return False
    return 30.0 <= s <= 300.0
assert [valid(t) for t in ["62.5", "30", "300", "29.9", "300.1", "fast", ""]] == [True, True, True, False, False, False, False]

# technique check
assert len([-1] * 19) == 19 and len([-1] * 20) == 20
try:
    ([-1] * 19)[19]
    raise SystemExit("expected IndexError")
except IndexError:
    pass
try:
    0 + "5"
except TypeError:
    pass
assert 0 + int(" 5\n".strip()) == 5
assert "5" + "3" == "53" and ("10" < "9") is True
assert -1 + 1 == 0 and 3 == 4 - 1  # TopPointer test for a stack of four: full at index 3
print("ok")
