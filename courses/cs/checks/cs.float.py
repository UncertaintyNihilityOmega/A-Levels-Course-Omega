# checks/cs.float.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.float"

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


from fractions import Fraction as F
import math

INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 4, f"expected 4 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 0

# ---------------------------------------------------------------------------------------------
# Exact reference model of the Cambridge format
# ---------------------------------------------------------------------------------------------
def twos(bits):
    v = int(bits, 2)
    return v - (1 << len(bits)) if bits[0] == "1" else v


def mant(mbits):
    return F(twos(mbits), 1 << (len(mbits) - 1))


def val(mbits, ebits):
    return mant(mbits) * F(2) ** twos(ebits)


def normalised(mbits):
    return mbits[0] != mbits[1]


def limits(m, e):
    emax, emin = (1 << (e - 1)) - 1, -(1 << (e - 1))
    return {"largest": F((1 << (m - 1)) - 1, 1 << (m - 1)) * F(2) ** emax,
            "smallest": F(1, 2) * F(2) ** emin,
            "most_negative": -F(2) ** emax}


def bits_of(n, width):
    return format(n & ((1 << width) - 1), f"0{width}b")


def encode(x, m, e):
    x = F(x)
    if x == 0:
        return "0" * m, "0" * e
    emax, emin = (1 << (e - 1)) - 1, -(1 << (e - 1))
    neg, a = x < 0, abs(x)
    E = 0
    while a >= F(2) ** E:
        E += 1
    while a < F(2) ** (E - 1):
        E -= 1
    if neg and a == F(2) ** (E - 1):
        E -= 1
    y = a / F(2) ** E
    N = math.floor(y * (1 << (m - 1)) + F(1, 2))
    if not neg and N == 1 << (m - 1):
        N, E = 1 << (m - 2), E + 1
    if neg and N == 1 << (m - 2):
        N, E = 1 << (m - 1), E - 1
    assert emin <= E <= emax
    return bits_of(-N if neg else N, m), bits_of(E, e)


def shift_to_normalise(mbits, ebits):
    path = []
    e = twos(ebits)
    while not normalised(mbits):
        mbits, e = mbits[1:] + "0", e - 1
        path.append((mbits, bits_of(e, len(ebits))))
    return path


# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert twos("10110100") == -76 == -128 + 32 + 16 + 4
assert (-(2 ** 3), 2 ** 3 - 1) == (-8, 7)

# ---------------------------------------------------------------------------------------------
# Binary fractions
# ---------------------------------------------------------------------------------------------
def frac_bits(x, n):
    out, steps = "", []
    for _ in range(n):
        x *= 2
        d = int(x)
        steps.append((x, d))
        out += str(d)
        x -= d
    return out, steps


assert frac_bits(F(11, 16), 4)[0] == "1011"
assert [float(s[0]) for s in frac_bits(F(11, 16), 4)[1]] == [1.375, 0.75, 1.5, 1.0]
assert frac_bits(F(3, 8), 3)[0] == "011"
assert F(1, 2) + F(1, 8) + F(1, 16) == F("0.6875") and 4 + 1 + F(1, 4) == F("5.25")
assert int("1101", 2) == 13 and F(3, 8) == F("0.375") and 13 + F("0.375") == F("13.375")
tenth, steps = frac_bits(F(1, 10), 12)      # exact Fractions, not floats
assert tenth == "000110011001"
assert [d for _, d in steps][:6] == [0, 0, 0, 1, 1, 0]
assert [float(x) for x, _ in steps][:6] == [0.2, 0.4, 0.8, 1.6, 1.2, 0.4]
assert F(2, 10) == F(1, 5) and F("0.2") == F(1, 5)
# the remainder after step 5 is 0.2 again: the same as after step 1
rem = F(1, 10)
rems = []
for _ in range(6):
    rem = rem * 2
    rem -= int(rem)
    rems.append(rem)
assert rems[0] == rems[4] == F(1, 5)
# place value table
assert [float(F(1, 2 ** k)) for k in range(1, 8)] == [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125]
assert float(F(1, 128)) == 0.0078125

# fixed point
assert 4 + 1 + F(1, 2) + F(1, 8) == F("5.625")
assert 15 + F(15, 16) == F("15.9375") and float(F(1, 16)) == 0.0625

# ---------------------------------------------------------------------------------------------
# Format and conversions
# ---------------------------------------------------------------------------------------------
assert mant("01011000") == F(11, 16) and F(11, 16) == F("0.6875") and twos("0011") == 3
assert val("01011000", "0011") == F("5.5")
assert 4 + 1 + F(1, 2) == F("5.5")
assert [F(-1)] + [F(1, 2 ** k) for k in range(1, 8)] == [mant("10000000"), F(1, 2), F(1, 4), F(1, 8), F(1, 16), F(1, 32), F(1, 64), F(1, 128)]
# exponent place values -8 4 2 1: range -8..7
assert (twos("1000"), twos("0111")) == (-8, 7)

# E1 (a), (b)
assert (twos("0011"), val("01011000", "0011")) == (3, F("5.5"))
assert mant("10110000") == F(-5, 8) == -1 + F(1, 4) + F(1, 8)
assert val("10110000", "0010") == F("-2.5") == -4 + 1 + F(1, 2)
# E2 (a), (b)
assert twos("1110") == -8 + 4 + 2 == -2
assert val("01100000", "1110") == F("0.1875") == F(1, 8) + F(1, 16)
assert twos("1101") == -3 == -8 + 4 + 1
assert mant("10100000") == F(-3, 4)
assert val("10100000", "1101") == F("-0.09375") == F(-3, 32)
assert F(-1) + F(1, 2) + F(1, 4) + F(1, 8) + F(1, 32) == F("-0.09375")      # 1.1110100000

# Denary to floating point examples
assert encode(F("6.25"), 8, 4) == ("01100100", "0011") and F("6.25") == 4 + 2 + F(1, 4)
assert encode(F("-3.5"), 8, 4) == ("10010000", "0010")
assert mant("10010000") == F(-7, 8) == -1 + F(1, 8) and F(-7, 8) * 4 == F("-3.5")
assert encode(F("0.15625"), 8, 4) == ("01010000", "1110") and F("0.15625") == F(1, 8) + F(1, 32)
assert encode(F(-4), 8, 4) == ("10000000", "0010") and mant("10000000") == -1
assert val("10000000", "0010") == -4
# the intermediate 1.1000000 (not normalised) really is -0.5 and the shifted pattern equal in value
assert mant("11000000") == F(-1, 2) and val("11000000", "0011") == -4
# two's complement steps for -3.5: invert 0.1110000 -> 1.0001111, +1 -> 1.0010000
assert bits_of(~int("01110000", 2) + 1, 8) == "10010000"
assert bits_of(~int("01000000", 2) + 1, 8) == "11000000"

# ---------------------------------------------------------------------------------------------
# Normalising
# ---------------------------------------------------------------------------------------------
assert [r for r in [val("00101100", "0100"), val("00010110", "0101")]] == [F("5.5")] * 2
assert val("01011000", "0011") == F("5.5")
assert val("00011010", "0100") == F("3.25") and mant("00011010") == F(13, 64)
assert F(1, 8) + F(1, 16) + F(1, 64) == F(13, 64) and F(13, 64) * 16 == F("3.25")
assert shift_to_normalise("00011010", "0100") == [("00110100", "0011"), ("01101000", "0010")]
assert val("01101000", "0010") == F("3.25") and mant("01101000") == F(13, 16) and F(13, 16) * 4 == F("3.25")
assert val("11100110", "0011") == F("-1.625") and mant("11100110") == F(-13, 64)
assert shift_to_normalise("11100110", "0011")[-1] == ("10011000", "0001")
assert val("10011000", "0001") == F("-1.625") and mant("10011000") == F(-13, 16)
assert shift_to_normalise("00101100", "0101") == [("01011000", "0100")]
assert val("00101100", "0101") == 11 == val("01011000", "0100")
assert val("01011000", "0101") == 22

# ---------------------------------------------------------------------------------------------
# Range and precision
# ---------------------------------------------------------------------------------------------
L84 = limits(8, 4)
assert L84["largest"] == 127 and L84["smallest"] == F(1, 512) and L84["most_negative"] == -128
assert float(L84["smallest"]) == 0.001953125
assert val("01111111", "0111") == 127 and val("01000000", "1000") == F(1, 512) and val("10000000", "0111") == -128
assert mant("01111111") == F(127, 128)
header, rows = table_after("| Format (12 bits) |")
for (m, e), row in zip([(9, 3), (8, 4), (7, 5)], rows):
    lim = limits(m, e)
    emin, emax = -(1 << (e - 1)), (1 << (e - 1)) - 1
    assert row[0] == f"{m} + {e}"
    assert int(row[1]) == m - 1
    assert row[2] == f"{emin} to {emax}".replace("-", "−") or row[2] == f"{emin} to {emax}"
    assert F(row[3]) == lim["largest"], (row, lim)
    smallest = F(1, 131072) if "/" in row[4] else F(row[4])
    assert smallest == lim["smallest"], (row, lim)
    assert F(row[5]) == F(1, 2 ** (m - 1))
header, rows = table_after("| Value | Mantissa | Exponent | Value in denary |")
assert len(rows) == 3

# Figure: 4-bit mantissa, 2-bit exponent
vals = sorted(F(n, 8) * F(2) ** E for E in range(-2, 2) for n in range(4, 8))
assert len(vals) == 16 and 4 * 4 == 16
gaps = [b - a for a, b in zip(vals, vals[1:])]
assert gaps[0] == F(1, 32) == F("0.03125") and gaps[-1] == F("0.25")
assert [float(F(1, 8) * F(2) ** E) for E in (-2, -1, 0, 1)] == [0.03125, 0.0625, 0.125, 0.25]
assert limits(4, 2)["smallest"] == F(1, 8) and limits(4, 2)["largest"] == F(7, 4)

# ---------------------------------------------------------------------------------------------
# Approximation
# ---------------------------------------------------------------------------------------------
mbits, ebits = encode(F(1, 10), 8, 4)
assert (mbits, ebits) == ("01100110", "1101")
assert val(mbits, ebits) == F(51, 512) == F("0.099609375") and F(51, 64) / 8 == F(51, 512)
assert F(1, 10) - F(51, 512) == F("0.000390625")
assert float((F(1, 10) - F(51, 512)) / F(1, 10)) == 0.00390625 and round(float((F(1, 10) - F(51, 512)) / F(1, 10)) * 100, 2) == 0.39
assert F(1, 10) * 8 == F(4, 5)           # 0.1 = 0.8 x 2^-3 : mantissa 0.11001100...
digits = frac_bits(F(4, 5), 12)[0]
assert digits[:12] == "110011001100" and digits[7:10] == "011"      # 0.1100110|011...
assert 200 > 127 and F(1, 1000) < F(1, 512)

# ---------------------------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------------------------
assert F(1, 2) + F(1, 4) + F(1, 16) == F("0.8125")
assert frac_bits(F("0.4375"), 4) == ("0111", [(F("0.875"), 0), (F("1.75"), 1), (F("1.5"), 1), (F("1.0"), 1)])
assert twos("1010") == -6 == -8 + 2
assert val("01010000", "0010") == F("2.5") and mant("01010000") == F("0.625")
assert [normalised(b) for b in ["01001100", "10110000", "11100000", "00110000"]] == [True, True, False, False]
assert encode(F("-1.75"), 8, 4) == ("10010000", "0001") and val("10010000", "0001") == F("-1.75")
assert F("-0.875") * 2 == F("-1.75")
assert bits_of(~int("01110000", 2) + 1, 8) == "10010000"

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
assert val("01101000", "0100") == 13 and 8 + 4 + 1 == 13
assert val("10110000", "1110") == F(-5, 32) == F("-0.15625")
assert F(-5, 8) * F(1, 4) == F(-5, 32)
assert 16 + 4 + 2 + F(1, 2) == F("22.5") and encode(F("22.5"), 8, 4) == ("01011010", "0101")
assert val("01011010", "0101") == F("22.5") and twos("0101") == 5
assert encode(F("-5.25"), 8, 4) == ("10101100", "0011") and val("10101100", "0011") == F("-5.25")
assert 4 + 1 + F(1, 4) == F("5.25")
assert bits_of(~int("01010100", 2) + 1, 8) == "10101100"
# 8 + 4 vs 9 + 3 vs 7 + 5 : one bit moved from mantissa to exponent -> range up, precision down
assert limits(7, 5)["largest"] > limits(8, 4)["largest"] and F(1, 2 ** 6) > F(1, 2 ** 7)
# 6 + 4 format
L64 = limits(6, 4)
assert (L64["largest"], L64["smallest"], L64["most_negative"]) == (124, F(1, 512), -128)
assert val("011111", "0111") == 124 and F(31, 32) * 128 == 124
assert val("010000", "1000") == F(1, 512) and val("100000", "0111") == -128
# repeated addition of 0.1
t = 0.0
for _ in range(10):
    t += 0.1
assert t != 1.0
# Stretch 1
X, Y = limits(12, 4), limits(10, 6)
assert X["largest"] == F("127.9375") and (1 - F(1, 2 ** 11)) * 2 ** 7 == F("127.9375")
assert Y["largest"] == 2143289344 and (1 - F(1, 2 ** 9)) * 2 ** 31 == 2143289344 == 2 ** 31 - 2 ** 22
assert X["smallest"] == F(1, 512) and float(X["smallest"]) < 0.002
assert Y["smallest"] == F(1, 2 ** 33) and 1.1e-10 < float(Y["smallest"]) < 1.2e-10
assert X["largest"] < 10_000_000 < Y["largest"] and Y["smallest"] < F(1, 1000)
assert (12 - 1, 10 - 1) == (11, 9)
# Stretch 2 : done above (16 values, gaps 0.03125 and 0.25)
assert F(1, 8) * F(1, 4) == F(1, 32) and F(1, 8) * 2 == F(1, 4)

# Quiz
assert twos("1101") == -3 and int("1101", 2) == 13 and -8 + 1 == -7 and -8 + 4 + 1 == -3
assert shift_to_normalise("00101100", "0101") == [("01011000", "0100")]
assert F(1, 10) == F(1, 10) and 100 + 100 > 127

assert encode(F("13.375"), 8, 4) == ("01101011", "0100") and F(107, 128) * 16 == F("13.375")
assert 13 + F(3, 8) == F("13.375") and int("1101", 2) == 13 and mant("01101011") == F(107, 128)

print("ok")
