# checks/cs.hardware.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every number the chapter states (buffer sizes, disk speeds, the control-loop trace).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.hardware"

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


blocks = run_python_blocks([])
assert blocks == 2, f"expected 2 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 2

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert 2 ** 10 == 1024 and 300 * 2 == 600

# ---------------------------------------------------------------------------------------------
# Buffers: bit rate x seconds / 8
# ---------------------------------------------------------------------------------------------
def buffer_mb(mbit_per_s, seconds):
    return mbit_per_s * seconds / 8

assert (4 * 10, buffer_mb(4, 10)) == (40, 5.0)          # worked example
assert (2 * 30, buffer_mb(2, 30)) == (60, 7.5)          # exam practice

# ---------------------------------------------------------------------------------------------
# Hard disk: 7200 rpm
# ---------------------------------------------------------------------------------------------
rev_per_s = 7200 / 60
assert rev_per_s == 120
assert round(1000 / rev_per_s, 1) == 8.3 and round(1000 / rev_per_s / 2, 1) == 4.2

# ---------------------------------------------------------------------------------------------
# Greenhouse control loop (pseudocode semantics): trace of the first twelve minutes
# ---------------------------------------------------------------------------------------------
LOW, HIGH = 18.0, 22.0
temp, heater, trace = 19.0, False, []
for minute in range(1, 13):
    if temp < LOW:
        heater = True
    if temp > HIGH:
        heater = False
    trace.append((minute, temp, heater))
    temp += 2.0 if heater else -1.0
assert [t[1] for t in trace] == [19.0, 18.0, 17.0, 19.0, 21.0, 23.0, 22.0, 21.0, 20.0, 19.0, 18.0, 17.0]
assert [t[2] for t in trace] == [False, False, True, True, True, False, False, False, False, False, False, True]
# the prose: switches on at minute 3, off at minute 6, and 18.0 does not trigger the low limit
assert trace[2][1] < LOW and not trace[1][1] < LOW and trace[5][1] > HIGH and not trace[6][1] > HIGH
# the heater switches state twice in six minutes with two limits, but a single limit of 20.0 flips it far more often
def flips(low, high, minutes=60):
    t, h, n, last = 19.0, False, 0, False
    for _ in range(minutes):
        if t < low:
            h = True
        if t > high:
            h = False
        n += h != last
        last = h
        t += 2.0 if h else -1.0
    return n

assert flips(18.0, 22.0) < flips(19.5, 19.5)

print("ok")
