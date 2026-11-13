# checks/cs.data.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every number the chapter states (conversions, sums, ranges, sizes, BCD, characters).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.data"

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




def b(n, bits=8):
    return format(n, "0" + str(bits) + "b")


def twos(v, bits=8):
    return format(v & (2 ** bits - 1), "0" + str(bits) + "b")


def untwos(p):
    v = int(p, 2)
    return v - 2 ** len(p) if p[0] == "1" else v


def invert(p):
    return "".join("1" if c == "0" else "0" for c in p)


def add_cols(a, c, bits=8):
    """Column addition of two bit strings: (carries into each column, left to right; carry out; result)."""
    carry, into, res = 0, [], ""
    for i in range(bits - 1, -1, -1):
        s = int(a[i]) + int(c[i]) + carry
        into.insert(0, str(carry))
        res = str(s % 2) + res
        carry = s // 2
    return "".join(into), carry, res


def bcd(n):
    return " ".join(format(int(d), "04b") for d in str(n))


blocks = run_python_blocks([])
assert blocks == 5, f"expected 5 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 1

# --- Warm-up -------------------------------------------------------------------------------
assert (23 // 4, 23 % 4) == (5, 3) and 2 ** 4 == 16 and "3" + "4" == "34"

# --- Bits, patterns, place values ------------------------------------------------------------
assert 2 ** 8 == 256 and 2 ** 16 == 65536 and 2 ** 10 == 1024
assert sum(2 ** i for i in range(8)) == 255 == 2 ** 8 - 1
assert [b(n, 4) for n in range(9)] == ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000"]
header, rows = table_after("| Denary | 0 | 1 | 2 |")
assert rows[0] == ["Binary"] + [b(n, 4) for n in range(9)]
header, rows = table_after("| Place value | 128 | 64 |")
assert header[1:] == [str(2 ** i) for i in range(7, -1, -1)]
assert rows[0][1:] == [f"\\(2^{i}\\)" for i in range(7, -1, -1)]

# --- Prefixes ---------------------------------------------------------------------------------
header, rows = table_after("| Binary prefix | Symbol |")
want = [(10, 3), (20, 6), (30, 9), (40, 12)]
for row, (p2, p10) in zip(rows, want):
    assert row[2].replace(" ", "").endswith("=" + str(2 ** p2)), row
    assert row[5].replace(" ", "").endswith("=" + str(10 ** p10)), row
assert 2 ** 30 == 1073741824 and 2 ** 40 == 1099511627776 and 2 ** 20 == 1048576
assert 2 ** 30 / 10 ** 9 == 1.073741824            # "about 7% more"
drive = 500 * 10 ** 9 / 2 ** 30
assert f"{drive:.1f}" == "465.7"
assert 3 * 2 ** 20 == 3145728 and 8192 // 1024 == 8 and 8192 % 1024 == 0

# --- Binary and denary --------------------------------------------------------------------------
assert int("10101101", 2) == 173 == 128 + 32 + 8 + 4 + 1 and b(173) == "10101101"
n, remainders = 173, []
while n > 0:
    remainders.append((n, n // 2, n % 2))
    n //= 2
assert remainders == [(173, 86, 1), (86, 43, 0), (43, 21, 1), (21, 10, 1), (10, 5, 0), (5, 2, 1), (2, 1, 0), (1, 0, 1)]
header, rows = table_after("| Division | Whole-number answer | Remainder |")
assert [(int(r[0].split(" ÷")[0]), int(r[1]), int(r[2])) for r in rows] == remainders
left, bits_out, left_after = 173, "", []
for pv in [128, 64, 32, 16, 8, 4, 2, 1]:
    if left >= pv:
        bits_out += "1"
        left -= pv
    else:
        bits_out += "0"
    left_after.append(left)
assert bits_out == "10101101" and left_after == [45, 45, 13, 13, 5, 1, 1, 0]
assert b(5) == "00000101"

# Pseudocode division algorithm (translated), with the trace table
number, bits_str, trace, numbers = 13, "", [], [13]
while number > 0:
    bits_str = str(number % 2) + bits_str
    trace.append(bits_str)
    number = number // 2
    numbers.append(number)
assert bits_str == "1101" and trace == ["1", "01", "101", "1101"] and numbers == [13, 6, 3, 1, 0]
header, rows = table_after("| Number | Bits | OUTPUT |")
assert column_values(header, rows, "Bits") == ['""'] + [f'"{t}"' for t in trace]
assert column_values(header, rows, "Number") == [str(x) for x in numbers]
assert column_values(header, rows, "OUTPUT") == ["1101"]

# --- Hexadecimal -----------------------------------------------------------------------------------
assert format(173, "X") == "AD" and int("AD", 16) == 173 == 10 * 16 + 13
assert b(0xA, 4) == "1010" and b(0xD, 4) == "1101"
assert int("3F9", 16) == 1017 == 3 * 256 + 15 * 16 + 9
assert b(3, 4) + " " + b(15, 4) + " " + b(9, 4) == "0011 1111 1001"
assert divmod(205, 16) == (12, 13) and format(205, "X") == "CD" and 12 * 16 + 13 == 205
header, rows = table_after("| Hex | 0 | 1 | 2 |")
assert rows[0][1:] == [str(i) for i in range(8)] and rows[1][1:] == [b(i, 4) for i in range(8)]
header, rows = table_after("| Hex | 8 | 9 | A |")
assert header[1:] == ["8", "9", "A", "B", "C", "D", "E", "F"]
assert rows[0][1:] == [str(i) for i in range(8, 16)] and rows[1][1:] == [b(i, 4) for i in range(8, 16)]
assert (0xFF, 0x80, 0x00) == (255, 128, 0) and 2 ** 24 == 16777216
assert len("3C:52:82:1A:9F:07".replace(":", "")) == 12 == 48 // 4

# --- BCD ------------------------------------------------------------------------------------------
assert bcd(2057) == "0010 0000 0101 0111"
assert [int(x, 2) for x in "1001 0111 0011".split()] == [9, 7, 3]
assert bcd(59) == "0101 1001" and b(59) == "00111011" and int("01011001", 2) == 89
assert bcd(482) == "0100 1000 0010" and bcd(307) == "0011 0000 0111"
assert [int(x, 2) for x in "1001 0110".split()] == [9, 6] and [int(x, 2) for x in "1001 0101".split()] == [9, 5]
assert int("10010101", 2) == 149 and int("00010010", 2) == 18 and bcd(12) == "0001 0010"
assert int("1010", 2) == 10                                       # not a valid BCD nibble

# --- One's and two's complement ---------------------------------------------------------------------
assert b(25) == "00011001" and invert("00011001") == "11100110"
assert untwos("10110111") == -73 == -128 + 32 + 16 + 4 + 2 + 1 and 32 + 16 + 4 + 2 + 1 == 55
assert (-2 ** 7, 2 ** 7 - 1) == (-128, 127) and (-2 ** 15, 2 ** 15 - 1) == (-32768, 32767)
assert b(19) == "00010011" and invert("00010011") == "11101100" and twos(-19) == "11101101"
assert -128 + 64 + 32 + 8 + 4 + 1 == -19
assert format(int("11101101", 2), "X") == "ED"
assert untwos("11110110") == -10 == -128 + 64 + 32 + 16 + 4 + 2
assert invert("11110110") == "00001001" and int("00001010", 2) == 10
assert untwos("10000000") == -128
assert b(45) == "00101101" and invert("00101101") == "11010010" and twos(-45) == "11010011"
assert untwos("11010011") == -45 == -128 + 64 + 16 + 2 + 1 and untwos("11010010") == -46
assert int("11010010", 2) + 1 == int("11010011", 2)
assert (twos(-59), twos(59)) == ("11000101", "00111011") and (untwos("11000101"), untwos("01011101")) == (-59, 93)

# --- Addition, subtraction -----------------------------------------------------------------------------
assert b(78) == "01001110" and add_cols("00101101", "01001110") == ("00011000", 0, "01111011")
assert int("01111011", 2) == 123 == 45 + 78
assert (b(93), b(58)) == ("01011101", "00111010") and invert("00111010") == "11000101" and twos(-58) == "11000110"
assert add_cols("01011101", "11000110") == ("10111000", 1, "00100011") and int("00100011", 2) == 35 == 93 - 58 == 32 + 2 + 1

# --- Overflow ----------------------------------------------------------------------------------------------
assert add_cols(b(100), b(50)) == ("11000000", 0, "10010110") and untwos("10010110") == -106 == -128 + 16 + 4 + 2
assert (b(100), b(50)) == ("01100100", "00110010") and 150 > 127
assert (twos(-100), twos(-50)) == ("10011100", "11001110")
assert add_cols("10011100", "11001110") == ("00111000", 1, "01101010") and untwos("01101010") == 106 and -150 < -128
assert (b(200), b(100)) == ("11001000", "01100100")
assert add_cols("11001000", "01100100") == ("10000000", 1, "00101100") and int("00101100", 2) == 44 == 300 - 256
assert add_cols("11111111", "11111111") == ("11111110", 1, "11111110") and untwos("11111110") == -2
assert (100 + 50) & 255 == 150 and untwos(b((100 + 50) & 255)) == -106
assert untwos(b((-1 + -1) & 255)) == -2 == -1 + -1

# --- Characters ----------------------------------------------------------------------------------------------
assert 2 ** 7 == 128 and 2 ** 8 == 256
assert ord("A") == 65 and ord("a") == 97 and ord("a") - ord("A") == 32 and ord("0") == 48 and ord("9") == 57
assert ord("7") == 55 == ord("0") + 7 and int("7") == 7
assert ord("F") == 70 == 65 + 5 and chr(69) == "E" and 69 - 65 == 4
assert 5 * 8 == 40
assert [ord(c) for c in "Lagos"] == [76, 97, 103, 111, 115]
assert (len("Lagos".encode()), len("é".encode()), len("€".encode())) == (5, 2, 3)

# --- Try yourself --------------------------------------------------------------------------------------------------
assert (2 ** 10, 2 ** 10 - 1) == (1024, 1023)
assert b(106) == "01101010" and 64 + 32 + 8 + 2 == 106
assert int("11010110", 2) == 214 == 128 + 64 + 16 + 4 + 2
assert format(int("10111100", 2), "X") == "BC" and b(0x7E) == "01111110" and (b(7, 4), b(14, 4)) == ("0111", "1110")
assert int("2F", 16) == 47 and divmod(255, 16) == (15, 15) and format(255, "X") == "FF"
assert invert("00011010") == "11100101" and twos(-26) == "11100110" and untwos("11100110") == -26
assert -128 + 64 + 32 + 4 + 2 == -26 and untwos("10000001") == -127
assert add_cols("00110110", "00011011") == ("01111100", 0, "01010001") and int("01010001", 2) == 81 == 54 + 27
assert 2 * 1024 == 2048 and ord("d") == 100 and ord("D") == 68 == 100 - 32
assert divmod(77, 16) == (4, 13) and format(77, "X") == "4D" and 4 * 16 + 13 == 77

# --- Exam practice ------------------------------------------------------------------------------------------------------
assert b(203) == "11001011" and 128 + 64 + 8 + 2 + 1 == 203 and format(203, "X") == "CB"
assert 2048 // 4 == 512 and 2048 % 4 == 0 and 2 ** 20 > 10 ** 6
assert b(93) == "01011101" and 64 + 16 + 8 + 4 + 1 == 93 and invert("01011101") == "10100010" and twos(-93) == "10100011"
assert untwos("10100011") == -93
a1, a2 = "01101011", "00111001"
assert (untwos(a1), untwos(a2)) == (107, 57) and add_cols(a1, a2) == ("11110110", 0, "10100100")
assert untwos("10100100") == -92 and 107 + 57 == 164 > 127
assert (b(100), b(37), invert("00100101"), twos(-37)) == ("01100100", "00100101", "11011010", "11011011")
assert add_cols("01100100", "11011011") == ("10000000", 1, "00111111") and int("00111111", 2) == 63 == 100 - 37
assert ord("C") == 67 and 67 + 5 == 72 == ord("H") and 11 * 8 == 88 and 11 * 32 == 352 and len("Kumasi 2027") == 11
assert 352 // 88 == 4
assert untwos("10010110") == -106 == -128 + 16 + 4 + 2 and format(0b10010110, "X") == "96"
assert add_cols("10010110", "01101110") == ("11111100", 1, "00000100") and int("00000100", 2) == 4 == -106 + 110
assert invert("10000000") == "01111111" and int("01111111", 2) + 1 == 128 and twos(128) == "10000000" and untwos("10000000") == -128
assert 12 * 4 == 48 and 2 ** 39 == 549755813888 and 2 ** 40 == 1099511627776
assert 2 ** 39 < 10 ** 12 - 1 < 2 ** 40 and (10 ** 12 - 1).bit_length() == 40 and 48 - 40 == 8 and 8 / 48 == 1 / 6
# quiz
assert int("00101101", 2) == 45
assert twos(-1) == "11111111" and untwos("10000001") == -127 and untwos("11111110") == -2
assert add_cols("01100100", "01100100")[2] == "11001000" and untwos("11001000") == -56 and add_cols("01100100", "01100100")[1] == 0
assert round(10 ** 12 / 2 ** 40, 2) == 0.91

print("ok")
