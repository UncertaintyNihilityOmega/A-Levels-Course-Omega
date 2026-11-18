# checks/cs.recursion.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, call counts, outputs).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.recursion"

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
assert blocks == 20, f"expected 20 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 19

import sys
from math import factorial as math_factorial

sys.setrecursionlimit(5000)

# ---------------------------------------------------------------------------------------------
# Pseudocode translated into Python, with call counters
# ---------------------------------------------------------------------------------------------
CALLS = {"n": 0}


def counted(fn):
    def wrapper(*args):
        CALLS["n"] += 1
        return fn(*args)
    return wrapper


def calls_of(fn, *args):
    CALLS["n"] = 0
    value = fn(*args)
    return value, CALLS["n"]


@counted
def Factorial(n):
    return 1 if n <= 1 else n * Factorial(n - 1)


@counted
def Power(base, exp):
    return 1 if exp == 0 else base * Power(base, exp - 1)


@counted
def FastPower(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = FastPower(base, exp // 2)
        return half * half
    return base * FastPower(base, exp - 1)


@counted
def Mystery(a, b):
    return 0 if b == 0 else a + Mystery(a, b - 1)


@counted
def Fib(n):
    return n if n <= 1 else Fib(n - 1) + Fib(n - 2)


@counted
def Ways(n):
    return 1 if n <= 1 else Ways(n - 1) + Ways(n - 2)


@counted
def Collect(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + Collect(n - 1)
    return Collect(n - 1)


@counted
def SumDigits(n):
    return n if n < 10 else (n % 10) + SumDigits(n // 10)


@counted
def CountDigits(n):
    return 1 if n < 10 else 1 + CountDigits(n // 10)


@counted
def HalveCount(n):
    return 0 if n <= 1 else 1 + HalveCount(n // 2)


# Factorial: the table of calls
assert calls_of(Factorial, 4) == (24, 4)
assert 4 * (3 * (2 * 1)) == 24 and (1, 2 * 1, 3 * 2, 4 * 6) == (1, 2, 6, 24)
assert Factorial(10) == 3628800 == math_factorial(10) and Factorial(6) == 720 and Factorial(5) == 120
assert calls_of(Factorial, 5) == (120, 5)       # quiz: five calls, not four or six
assert Factorial(0) == 1 and Factorial(1) == 1

# Sum of a list
SCORES = [4, 8, 15, 16, 23]
assert sum(SCORES) == 66 and 4 + (8 + (15 + (16 + (23 + 0)))) == 66

# Power
assert Power(2, 10) == 1024 and Power(3, 4) == 81
assert calls_of(Power, 2, 5) == (32, 6)
assert calls_of(Power, 2, 3) == (8, 4)
assert (2 * 1, 2 * 2, 2 * 4) == (2, 4, 8)
assert calls_of(Power, 2, 10) == (1024, 11)
assert calls_of(FastPower, 2, 10) == (1024, 6)
exps = []


def fast_exps(e):
    exps.append(e)
    if e == 0:
        return
    fast_exps(e // 2 if e % 2 == 0 else e - 1)


fast_exps(10)
assert exps == [10, 5, 4, 2, 1, 0]
assert FastPower(2, 1000) == 2 ** 1000

# Digits and strings
assert calls_of(CountDigits, 48271) == (5, 5)
assert calls_of(SumDigits, 274) == (13, 3) and SumDigits(27) == 9


def Reverse(s):
    return s if len(s) <= 1 else Reverse(s[1:]) + s[0]


assert Reverse("STACK") == "KCATS"
assert ["K", "KC", "KCA", "KCAT", "KCATS"] == [Reverse("STACK"[4 - k:]) for k in range(5)]

# Mystery
assert calls_of(Mystery, 5, 3) == (15, 4) and (5 + 5 + 5 + 0) == 15
assert (5 + 0, 5 + 5, 5 + 10) == (5, 10, 15)

# Output order: CountDown, CountUp, Both, Rise, Echo
def count_down_out(n):
    return [] if n <= 0 else [n] + count_down_out(n - 1)


def count_up_out(n):
    return [] if n <= 0 else count_up_out(n - 1) + [n]


assert count_down_out(3) == [3, 2, 1] and count_up_out(3) == [1, 2, 3]
assert count_up_out(4) == [1, 2, 3, 4] and [v * v for v in count_up_out(4)] == [1, 4, 9, 16]     # Rise(4)


def echo(n):
    if n > 1:
        return [n] + echo(n - 2) + [n]
    return ["end"]


assert echo(5) == [5, 3, "end", 3, 5]


def f_str(n):
    return "" if n == 0 else str(n) + f_str(n - 1)


assert f_str(4) == "4321"

# Collect, HalveCount
assert calls_of(Collect, 6) == (12, 7) and 6 + 4 + 2 == 12
assert HalveCount(8) == 3 and HalveCount(40) == 5
seq, v = [], 40
while v > 1:
    seq.append(v)
    v //= 2
seq.append(v)
assert seq == [40, 20, 10, 5, 2, 1]

# Stars and sum of squares
assert "*" * 4 == "****"
assert sum(i * i for i in range(1, 5)) == 30 == 16 + 9 + 4 + 1

# Spot the error: SumTo ignoring the result returns N, correct returns the triangle number
def sumto_bug(n):
    return 0 if n == 0 else n


def sumto(n):
    return 0 if n == 0 else n + sumto(n - 1)


assert sumto_bug(3) == 3 and sumto(3) == 6 and sumto(4) == 10

# Fibonacci
assert [Fib(i) for i in range(11)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
assert calls_of(Fib, 4) == (3, 9) and calls_of(Fib, 5) == (5, 15)
assert calls_of(Fib, 10) == (55, 177) and calls_of(Fib, 20) == (6765, 21891)
assert Fib(2) == 1 and Fib(3) == 2 and Fib(4) == 3          # call tree values
# calls = 2 * Fib(n + 1) - 1, and Fib(30) makes 2 692 537 calls; Fib(30) = 832 040
fibs = [0, 1]
for i in range(2, 40):
    fibs.append(fibs[-1] + fibs[-2])
assert [2 * fibs[n + 1] - 1 for n in (4, 5, 10, 20, 30)] == [9, 15, 177, 21891, 2692537]
assert fibs[30] == 832040 and fibs[20] == 6765
assert 1.6 < fibs[31] / fibs[30] < 1.62 and 1.6 < (2 * fibs[31] - 1) / (2 * fibs[30] - 1) < 1.62
assert 2692537 > fibs[30] and 21891 > fibs[20]

# Ways (staircase) and its call count
assert [Ways(i) for i in range(5)] == [1, 1, 2, 3, 5] and calls_of(Ways, 4) == (5, 9)

# Binary search: positions (1-based), mids and calls
CODES = [5, 9, 14, 20, 27, 33, 38, 44, 51, 60]


def bsearch(target):
    low, high, rows = 1, 10, []
    while True:
        if low > high:
            rows.append((low, high))
            return 0, rows
        mid = (low + high) // 2
        rows.append((low, high, mid, CODES[mid - 1]))
        if CODES[mid - 1] == target:
            return mid, rows
        if CODES[mid - 1] < target:
            low = mid + 1
        else:
            high = mid - 1


r38, rows38 = bsearch(38)
assert r38 == 7 and rows38 == [(1, 10, 5, 27), (6, 10, 8, 44), (6, 7, 6, 33), (7, 7, 7, 38)]
r30, rows30 = bsearch(30)
assert r30 == 0 and len(rows30) == 4 and rows30[-1] == (6, 5)
import math
assert math.floor(math.log2(1_000_000)) + 1 == 20

# Tree: in-order values and height of the chapter's tree
tree_values = sorted((40, 25, 60, 10, 30, 50, 70))
assert tree_values == [10, 25, 30, 40, 50, 60, 70]

# Hanoi: moves = 2**n - 1
assert [2 ** n - 1 for n in (2, 3, 5)] == [3, 7, 31]

# Memoised Fibonacci: 39 calls for fib(20)
memory, calls = {}, [0]


def fib_fast(n):
    calls[0] += 1
    if n <= 1:
        return n
    if n not in memory:
        memory[n] = fib_fast(n - 1) + fib_fast(n - 2)
    return memory[n]


assert (fib_fast(20), calls[0]) == (6765, 39)

# Python's recursion limit really is 1000 by default (the chapter prints it in a fresh interpreter)
import subprocess
out = subprocess.run([sys.executable, "-c", "import sys; print(sys.getrecursionlimit())"], capture_output=True, text=True).stdout
assert out.strip() == "1000"

print("ok")
