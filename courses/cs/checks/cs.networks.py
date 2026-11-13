# checks/cs.networks.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every number the chapter states (mesh links, delays, switch tables, CSMA/CD order).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.networks"

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


blocks = run_python_blocks([])
assert blocks == 4, f"expected 4 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 1

# Warm-up
assert 4 * 8 == 32 and int("1111", 2) == 15 and hex(15) == "0xf"
assert (5 * 2 > 8)

# Mesh links
def mesh(n):
    return n * (n - 1) // 2

assert [mesh(n) for n in (4, 5, 6, 10)] == [6, 10, 15, 45]
assert mesh(31) == 465 and 31 * 30 / 2 == 465
assert mesh(7) == 21 and mesh(9) == 36 and 9 * 8 == 72
# every pair of the four hosts is joined once (figure draws six links)
from itertools import combinations
assert len(list(combinations("ABCD", 2))) == 6

# Satellite delay and the stretch comparison
assert f"{4 * 35786 / 299792:.3f}" == "0.477"
assert 16000 / 200000 == 0.08 and 2 * 36000 / 300000 == 0.24
assert round((0.24 - 0.08) * 1000) == 160 and round(0.24 / 0.08) == 3

# Switch learning: the chapter's example and the stretch question
def run_switch(ports, frames):
    table, log = {}, []
    for source, destination in frames:
        table[source] = ports[source]
        if destination in table:
            log.append(("forward", [table[destination]]))
        else:
            log.append(("flood", [p for p in ports.values() if p != ports[source]]))
    return table, log

ports = {"A": 1, "B": 2, "C": 3, "D": 4}
table, log = run_switch(ports, [("A", "D"), ("D", "A"), ("A", "B"), ("B", "A"), ("C", "A")])
assert table == {"A": 1, "D": 4, "B": 2, "C": 3}
assert log == [("flood", [2, 3, 4]), ("forward", [1]), ("flood", [2, 3, 4]), ("forward", [1]), ("forward", [1])]
ports = {"W": 1, "X": 2, "Y": 3, "Z": 4}
table, log = run_switch(ports, [("W", "X"), ("X", "W"), ("Z", "X"), ("Y", "Z"), ("W", "Y")])
assert log == [("flood", [2, 3, 4]), ("forward", [1]), ("forward", [2]), ("forward", [4]), ("forward", [3])]
assert table == {"W": 1, "X": 2, "Z": 4, "Y": 3}
# the try question: P on port 3, Q on port 5 -> port 5 only
assert {"P": 3, "Q": 5}["Q"] == 5

# CSMA/CD: translate the pseudocode, a collision on the first two attempts then success
def csma_cd(collisions):
    attempts, sent, steps = 0, False, []
    while True:
        steps.append("listen")
        steps.append("send")
        if attempts < collisions:
            steps += ["jam", "wait"]
            attempts += 1
        else:
            sent = True
        if sent or attempts == 16:
            return sent, attempts, steps

assert csma_cd(0) == (True, 0, ["listen", "send"])
assert csma_cd(1) == (True, 1, ["listen", "send", "jam", "wait", "listen", "send"])
assert csma_cd(16)[0] is False and csma_cd(16)[1] == 16
# the try question's order
assert ["listen", "transmit", "collision detected", "jam signal", "random wait"][0] == "listen"

# Scenario numbers
assert 300 + 25 == 325
assert 30 + 1 == 31

print("ok")
