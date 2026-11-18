# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.fileproc"

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


INPUTS = [("Quantity:", ["two", "", "12"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 19, f"expected 19 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 5

# ---------------------------------------------------------------------------------------------
# Numbers in the text
# ---------------------------------------------------------------------------------------------
assert 250 * 40 == 10000 and 180 * 12 == 2160 and 140 * 0 == 0
assert 3 + 2 == 5

# Pseudocode: total of A100 sales (LEFT, MID, LENGTH as the insert defines them; strings count from 1)
def LEFT(s, n): return s[:n]
def MID(s, start, length): return s[start - 1:start - 1 + length]
def RIGHT(s, n): return s[-n:]

sales = ["A100,3", "B120,1", "A100,2", "A205,5"]
total = 0
for line in sales:
    if LEFT(line, 4) == "A100":
        total += float(MID(line, 6, len(line) - 5))
assert total == 5

# Pseudocode: sequential search with early stop, same stock lines as the Python
stock = ["A100,Rice,250,40", "A205,Beans,180,12", "A310,Maize flour,140,0", "B120,Cooking oil,520,8"]


def pseudo_search(target):
    found = too_far = False
    reads = 0
    line = ""
    i = 0
    while i < len(stock) and not found and not too_far:
        line = stock[i]
        i += 1
        reads += 1
        code = LEFT(line, 4)
        if code == target:
            found = True
        elif code > target:
            too_far = True
    return (line if found else "Not found"), reads


assert pseudo_search("A205") == ("A205,Beans,180,12", 2)
assert pseudo_search("A250") == ("Not found", 3)
assert pseudo_search("Z999") == ("Not found", 4)

# Pseudocode: random file update at address 2
records = [["A100", "Rice", 250, 40], ["A205", "Beans", 180, 12], ["A310", "Maize flour", 140, 0], ["B120", "Cooking oil", 520, 8]]
item = list(records[2 - 1])
item[3] = item[3] - 5
records[2 - 1] = item
assert records[1][3] == 7 and [r[3] for r in records] == [40, 7, 0, 8]

# Pseudocode: late entries in the visitors' log (answer to the 5-mark question)
log = ["Ana,09", "Bilal,12", "Chen,14", "Dina,08", "Emeka,17"]
assert sum(1 for l in log if float(RIGHT(l, 2)) >= 12) == 3

# ---------------------------------------------------------------------------------------------
# Random file: record length and positions
# ---------------------------------------------------------------------------------------------
assert 4 + 12 + 5 + 3 + 1 == 25 == len("A100".ljust(4) + "Rice".ljust(12) + "250".rjust(5) + "40".rjust(3) + "\n")
assert 4 * 25 == 100 and (3 - 1) * 25 == 50
assert (6 - 1) * 40 == 200 and (12 - 1) * 30 == 330 and (4 - 1) * 50 == 150

# ---------------------------------------------------------------------------------------------
# Parcels and rainfall
# ---------------------------------------------------------------------------------------------
grams = [2400, 850, 1200, 3100, 500]
assert sum(grams) == 8050 and sum(grams) / 1000 == 8.05 and max(grams) == 3100
assert sorted(grams, reverse=True) == [3100, 2400, 1200, 850, 500]
rain = [12, 31, 18, 9]
assert sum(rain) == 70 and len([r for r in rain if r > 10]) == 3 and sorted(rain, reverse=True) == [31, 18, 12, 9]

# try-easy: the output of the small try block
out = []
try:
    out.append(int("12"))
    out.append(int("x"))
    out.append("done")
except ValueError:
    out.append("bad")
assert out == [12, "bad"]
assert int("40\n") == 40 and "40\n" != "40" and "A100,Rice,250,40\n".split(",")[3] == "40\n"
assert int("B120,Cooking oil,520,8\n".strip().split(",")[2]) == 520

print("ok")
