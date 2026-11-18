# checks/cs.ml.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every number the chapter states (node outputs, XOR network, weight updates, regression, rewards).
import contextlib
import io
import os
import pathlib
import re
import tempfile
from fractions import Fraction as F

CHAPTER_ID = "cs.ml"

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


INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 4, f"expected 4 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 1


def step(total):
    return 1 if total >= 0 else 0


def relu(total):
    return max(0, total)


def node(inputs, weights, bias, activation):
    total = bias
    for x, w in zip(inputs, weights):
        total += x * w
    return total, activation(total)


# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert [(a != b) * 1 for a in (0, 1) for b in (0, 1)] == [0, 1, 1, 0]
assert 6 + 3 == 9
assert [4, 6, 5][1] == 6 and sum([4, 6, 5]) == 15

# ---------------------------------------------------------------------------------------------
# Reinforcement learning taste: V <- V + 0.5 (reward - V)
# ---------------------------------------------------------------------------------------------
V = F(0)
seen = []
for reward in (10, 10, 6):
    V = V + F(1, 2) * (reward - V)
    seen.append(V)
assert seen == [5, F(15, 2), F(27, 4)] and float(seen[2]) == 6.75

# ---------------------------------------------------------------------------------------------
# Network sizes
# ---------------------------------------------------------------------------------------------
assert 3 * 4 == 12 and 4 * 2 == 8 and 12 + 8 == 20
assert 4 * 5 + 5 * 3 == 35

# ---------------------------------------------------------------------------------------------
# One node: greenhouse
# ---------------------------------------------------------------------------------------------
rows = []
for x1, x2 in ((0, 0), (0, 1), (1, 0), (1, 1)):
    s, out = node([x1, x2], [2, 1], -2, step)
    rows.append((x1, x2, s, out))
assert rows == [(0, 0, -2, 0), (0, 1, -1, 0), (1, 0, 0, 1), (1, 1, 1, 1)]
for x1, x2, s, out in rows:
    line = f"| {x1} | {x2} | {2 * x1} + {x2} − 2 = {s} | {out} |".replace("-", "−")
    assert f"| {x1} | {x2} | {2 * x1} + {x2} − 2 = {str(s).replace('-', '−')} | {out} |" in TEXT, line
# pseudocode block translated: Inputs 3, 2, 1; Weights 2, -1, 4; Bias -7
Inputs, Weights, Bias = [None, 3, 2, 1], [None, 2, -1, 4], -7
Sum = Bias
for Index in range(1, 4):
    Sum = Sum + Inputs[Index] * Weights[Index]
Result = 1 if Sum >= 0.0 else 0
assert (Sum, Result) == (1, 1) and -7 + 6 - 2 + 4 == 1
assert node([3, 2], [2, -1], -3, relu) == (1, 1)

# ---------------------------------------------------------------------------------------------
# The XOR network
# ---------------------------------------------------------------------------------------------
def minus(n):
    return str(n).replace("-", "−")


table = []
for x1, x2 in ((0, 0), (0, 1), (1, 0), (1, 1)):
    s1, h1 = node([x1, x2], [1, 1], -1, step)
    s2, h2 = node([x1, x2], [1, 1], -2, step)
    so, o = node([h1, h2], [1, -1], -1, step)
    assert (s1, s2, so) == (x1 + x2 - 1, x1 + x2 - 2, h1 - h2 - 1)
    line = f"| {x1} | {x2} | {minus(s1)} | {h1} | {minus(s2)} | {h2} | {minus(so)} | {o} |"
    assert line in TEXT, line
    table.append(o)
assert table == [0, 1, 1, 0]

# ---------------------------------------------------------------------------------------------
# Training a node by hand (delta rule)
# ---------------------------------------------------------------------------------------------
def train_step(w, x, target, rate):
    out = sum(a * b for a, b in zip(w, x))
    err = target - out
    return out, err, [a + rate * err * b for a, b in zip(w, x)]


w = [F(1), F(2)]
x = [2, 3]
out1, err1, w = train_step(w, x, 10, F(1, 20))
assert (out1, err1, w) == (8, 2, [F(12, 10), F(23, 10)])
out2, err2, w = train_step(w, x, 10, F(1, 20))
assert (out2, err2, w) == (F(93, 10), F(7, 10), [F(127, 100), F(2405, 1000)])
out3, err3, w = train_step(w, x, 10, F(1, 20))
assert (out3, err3) == (F(9755, 1000), F(245, 1000))
assert F(1, 20) * 2 * 2 == F(1, 5) and F(1, 20) * F(7, 10) * 2 == F(7, 100) and F(1, 20) * F(7, 10) * 3 == F(21, 200)
# a rate of 0.1 overshoots
o, e, w10 = train_step([F(1), F(2)], x, 10, F(1, 10))
assert w10 == [F(14, 10), F(26, 10)] and sum(a * b for a, b in zip(w10, x)) == F(106, 10)
# try-question: x 1, 2; w 3, 1; target 4; rate 0.1
o, e, wt = train_step([F(3), F(1)], [1, 2], 4, F(1, 10))
assert (o, e, wt) == (5, -1, [F(29, 10), F(8, 10)]) and sum(a * b for a, b in zip(wt, [1, 2])) == F(45, 10)
# exam question: x 4, 1; w 2, 3; target 15; rate 0.05
o, e, wq = train_step([F(2), F(3)], [4, 1], 15, F(1, 20))
assert (o, e, wq) == (11, 4, [F(28, 10), F(32, 10)])
assert sum(a * b for a, b in zip(wq, [4, 1])) == F(144, 10) and 15 - F(144, 10) == F(6, 10)

# ---------------------------------------------------------------------------------------------
# Practice nodes
# ---------------------------------------------------------------------------------------------
assert node([2, 5], [3, -1], -1, step) == (0, 1)
assert node([3, 1], [-2, 1], 0, relu) == (-5, 0)
assert node([1, 1], [2, 1], -2, step) == (1, 1)
assert node([3, 2], [2, -1], -3, step) == (1, 1)
# exam: ReLU network
s_h1, h1 = node([2, 1], [1, 2], 0, relu)
s_h2, h2 = node([2, 1], [-3, 1], 1, relu)
s_o, o = node([h1, h2], [2, 5], -1, relu)
assert (s_h1, h1, s_h2, h2, s_o, o) == (4, 4, -4, 0, 7, 7)

# ---------------------------------------------------------------------------------------------
# Regression
# ---------------------------------------------------------------------------------------------
def least_squares(xs, ys):
    n = len(xs)
    mx, my = F(sum(xs), n), F(sum(ys), n)
    sxy = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    sxx = sum((a - mx) ** 2 for a in xs)
    m = sxy / sxx
    return mx, my, sxy, sxx, m, my - m * mx


mx, my, sxy, sxx, m, c = least_squares([1, 2, 3, 4, 5], [3, 5, 4, 7, 6])
assert (mx, my, sxy, sxx, m, c) == (3, 5, 8, 10, F(4, 5), F(13, 5))
assert m * F(7, 2) + c == F(27, 5)
res = [b - (m * a + c) for a, b in zip([1, 2, 3, 4, 5], [3, 5, 4, 7, 6])]
assert [float(r) for r in res] == [-0.4, 0.8, -1.0, 1.2, -0.6] and sum(r * r for r in res) == F(18, 5) and sum(res) == 0
assert (-2) * (-2) + (-1) * 0 + 0 * (-1) + 1 * 2 + 2 * 1 == 8 and 4 + 1 + 0 + 1 + 4 == 10 and F(5) - F(4, 5) * 3 == F(13, 5)
assert abs(0.8 * 3.5 + 2.6 - 5.4) < 1e-12 and abs(0.8 * 0 + 2.6 - 2.6) < 1e-12 and abs(0.8 * 6 + 2.6 - 7.4) < 1e-12
# any other line through these points has a larger total of squared errors (spot check)
def sse(mm, cc):
    return sum((b - (mm * a + cc)) ** 2 for a, b in zip([1, 2, 3, 4, 5], [3, 5, 4, 7, 6]))
assert all(sse(F(4, 5) + dm, F(13, 5) + dc) > F(18, 5) for dm in (F(-1, 10), F(1, 10)) for dc in (F(-1, 10), F(1, 10), 0)) and sse(F(4, 5), F(13, 5)) == F(18, 5)
# stretch
mx, my, sxy, sxx, m, c = least_squares([2, 4, 6, 8], [10, 14, 13, 19])
assert (mx, my, sxx, sxy, m, c) == (5, 14, 20, 26, F(13, 10), F(15, 2))
assert m * 7 + c == F(166, 10)
assert (2 + 4 + 6 + 8) / 4 == 5 and (10 + 14 + 13 + 19) / 4 == 14 and 9 + 1 + 1 + 9 == 20 and 12 + 0 - 1 + 15 == 26
# regression practice
assert 3 * 5 + 4 == 19 and 2.5 * 8 + 10 == 30

# stretch: robot vacuum
V = F(0)
vs = []
for reward in (8, 8, 4):
    V = V + F(1, 4) * (reward - V)
    vs.append(V)
assert vs == [2, F(7, 2), F(29, 8)] and float(vs[2]) == 3.625

# quiz
assert 2 + 1 - 2 == 1 and 2 + 1 == 3
assert F(14, 10) * 2 + F(26, 10) * 3 == F(106, 10) and 1 * 2 + 2 * 3 == 8
print("ok")
