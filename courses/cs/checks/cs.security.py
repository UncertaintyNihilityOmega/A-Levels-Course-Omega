# checks/cs.security.py: runs every Python block, translates the pseudocode algorithms, and recomputes every check digit,
# parity bit, parity block and checksum in the chapter.
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.security"

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


INPUTS = [("Enter age", ["25", "9", "15"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 7, f"expected 7 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 7

# The two figures in the chapter are exactly the ones data/cs.security_fig.py built and checked
FIGS = (pathlib.Path(__file__).resolve().parent.parent / "data" / "cs.security_figs.txt").read_text(encoding="utf-8").split("\n\n")
assert len(FIGS) == 2 and all(f.strip() in TEXT for f in FIGS), "figure in the chapter differs from data/cs.security_figs.txt"


# ---------------------------------------------------------------------------------------------
# Check digits (modulo 11 and modulo 10)
# ---------------------------------------------------------------------------------------------
def m11_total(code):
    n = len(code)
    return [int(d) * (n + 1 - i) for i, d in enumerate(code)]


def m11(code):
    prods = m11_total(code)
    total = sum(prods)
    rem = total % 11
    digit = (11 - rem) % 11
    return prods, total, rem, "X" if digit == 10 else str(digit)


def valid11(full):
    n = len(full)
    prods = [(10 if ch == "X" else int(ch)) * (n - i) for i, ch in enumerate(full)]
    return sum(prods) % 11 == 0


prods, total, rem, cd = m11("4829316")
assert prods == [32, 56, 12, 45, 12, 3, 12] and total == 172 and rem == 7 and cd == "4"
assert 11 * 15 == 165 and 11 - rem == 4
assert 172 + 4 == 176 == 11 * 16 and valid11("48293164")
assert not valid11("48293614") and m11("4829361")[3] == "X"
prods, total, rem, cd = m11("627093")
assert prods == [42, 12, 35, 0, 27, 6] and total == 122 and rem == 1 and cd == "X" and valid11("627093X")
prods, total, rem, cd = m11("7352")
assert total == 66 == 11 * 6 and rem == 0 and cd == "0" and valid11("73520")
assert m11("2749")[1:] == (68, 2, "9") and 10 + 28 + 12 + 18 == 68 and valid11("27499")
prods, total, rem, cd = m11("3926175")
assert prods == [24, 63, 12, 30, 4, 21, 10] and total == 164 and rem == 10 and cd == "1" and 11 * 14 == 154
assert valid11("39261751")
assert 8 * 6 + 9 * 5 + 1 * 4 + 3 * 3 + 6 * 2 + 0 * 1 == 118 and 118 % 11 == 8 and not valid11("891360")
assert valid11("819360") and m11("81936")[3] == "0"          # the code the clerk meant to type


def m10(code):
    prods = [int(d) * (3 if (len(code) - 1 - i) % 2 == 0 else 1) for i, d in enumerate(code)]
    total = sum(prods)
    return prods, total, total % 10, str((10 - total % 10) % 10)


assert m10("315806") == ([3, 3, 5, 24, 0, 18], 53, 3, "7")
assert m10("4271")[1::2] == (20, "0") and m10("4721")[1::2] == (30, "0")

# What the key box claims: modulo 11 catches every single wrong digit and every swap of neighbours
import itertools, random
rng = random.Random(11)
for _ in range(400):
    n = rng.randint(3, 9)        # weights n + 1 down to 1 must not include 11
    code = "".join(str(rng.randint(0, 9)) for _ in range(n))
    full = code + m11(code)[3]
    assert valid11(full)
    for i in range(len(full)):
        for d in "0123456789X":
            if i < len(full) - 1 and d == "X":
                continue
            if d != full[i]:
                changed = full[:i] + d + full[i + 1:]
                assert not valid11(changed), (full, changed)
    for i in range(len(full) - 1):
        if full[i] != full[i + 1]:
            swapped = full[:i] + full[i + 1] + full[i] + full[i + 2:]
            assert not valid11(swapped), (full, swapped)
# ... and modulo 10 (weights 1, 3) misses a swap exactly when the digits differ by 5
for a, b in itertools.product(range(10), repeat=2):
    base, swapped = f"{a}{b}", f"{b}{a}"
    undetected = m10(base)[3] == m10(swapped)[3]
    assert undetected == (a == b or abs(a - b) == 5), (a, b)
# stretch 1: swapping neighbours with weights w and w-1 changes the total by a - b
for w, a, b in itertools.product(range(2, 12), range(10), range(10)):
    assert (a * w + b * (w - 1)) - (b * w + a * (w - 1)) == a - b


# pseudocode translation of the check digit algorithm
def pseudo_check(code):
    total = 0
    for position in range(1, 8):
        digit = int(code[position - 1])
        weight = 9 - position
        total += digit * weight
    remainder = total % 11
    check = (11 - remainder) % 11
    return code + ("X" if check == 10 else str(check))


assert pseudo_check("4829316") == "48293164" and pseudo_check("3926175") == "39261751"

# ---------------------------------------------------------------------------------------------
# Parity bytes
# ---------------------------------------------------------------------------------------------
def pbyte(ch, even=True):
    bits = format(ord(ch), "07b")
    ones = bits.count("1")
    p = ones % 2 if even else 1 - ones % 2
    return str(p) + bits


assert format(ord("A"), "07b") == "1000001" and ord("A") == 65 == 64 + 1
assert pbyte("A") == "01000001" and pbyte("T") == "11010100" and pbyte("A", False) == "11000001" and pbyte("T", False) == "01010100"
assert format(ord("K"), "07b") == "1001011" and pbyte("K") == "01001011"
assert "01101001".count("1") == 4
assert format(ord("J"), "07b") == "1001010" and pbyte("J") == "11001010"
assert [b.count("1") for b in ["01100111", "10110010", "11000001", "00001011"]] == [5, 4, 3, 3]
assert "10110100".count("1") == 4
assert "1101001".count("1") == 4 and "0110101".count("1") == 4      # even-parity bit 0; odd-parity bit 1
assert [bin(ord(c))[2:].count("1") for c in "SECURED"] == [4, 3, 3, 4, 3, 3, 2]

# SECURED block: the table in the chapter
header, rows = table_after("| Byte | Character | Parity bit |")
sent = [pbyte(c) for c in "SECURED"]
assert column_values(header, rows, "Whole byte")[:7] == sent
assert [r[1] for r in rows[:7]] == list("SECURED")
cols = [sum(int(r[c]) for r in sent) % 2 for c in range(8)]
parity_byte = "".join(map(str, cols))
assert parity_byte == "01010011" and rows[7][-1] == parity_byte
assert [int(r[0]) for r in sent] == [0, 1, 1, 0, 1, 1, 0] and sum(int(r[0]) for r in sent) == 4
assert [int(r[1]) for r in sent] == [1] * 7


def analyse(block):
    """block: list of strings (rows) with even parity expected in every row and column."""
    bad_rows = [r + 1 for r, row in enumerate(block) if row.count("1") % 2 == 1]
    bad_cols = [c for c in range(len(block[0])) if sum(int(row[c]) for row in block) % 2 == 1]
    return bad_rows, bad_cols


recv = list(sent) + [parity_byte]
recv[3] = recv[3][:3] + ("0" if recv[3][3] == "1" else "1") + recv[3][4:]
assert recv[3] == "01000101" and recv[3].count("1") == 3 and analyse(recv) == ([4], [3])
assert sum(int(r[3]) for r in recv) == 3
recv[3] = sent[3]
assert analyse(recv) == ([], [])


def table_block(marker):
    header, rows = table_after(marker)
    return ["".join(r[1:]) for r in rows]


# worked example: error at byte 2, Bit 5
blk = table_block("Find the byte and the bit that is wrong")
assert blk == ["11000011", "11001011", "01000100", "11000101", "10001101"]
assert [r.count("1") for r in blk] == [4, 5, 2, 4, 4]
assert [sum(int(r[c]) for r in blk) for c in range(8)] == [4, 4, 0, 0, 2, 3, 2, 4]
assert analyse(blk) == ([2], [5])
fixed = blk[1][:5] + "1" + blk[1][6:]
assert fixed == "11001111" == pbyte("O")                      # byte 2 was the letter O
original = [pbyte(c) for c in "CODE"]
cp = "".join(str(sum(int(r[c]) for r in original) % 2) for c in range(8))
assert original == ["11000011", "11001111", "01000100", "11000101"] and cp == "10001101"

# Exam practice, last question: block for SAFE with the bit at byte 3, Bit 6 flipped
blk = table_block("(#cs.security) A block of four bytes is sent with a parity byte")
safe = [pbyte(c) for c in "SAFE"]
sp = "".join(str(sum(int(r[c]) for r in safe) % 2) for c in range(8))
assert safe == ["01010011", "01000001", "11000110", "11000101"] and sp == "00010001"
assert blk == ["01010011", "01000001", "11000100", "11000101", "00010001"]
assert blk[2].count("1") == 3 and analyse(blk) == ([3], [6])
assert sum(int(r[6]) for r in blk) == 1 and [sum(int(r[c]) for r in blk) for c in range(8)] == [2, 4, 0, 2, 0, 2, 1, 4]
assert blk[2][:6] + "1" + blk[2][7:] == "11000110" == safe[2]

# four corner errors escape block parity
test = [list(r) for r in safe + [sp]]
for r, c in [(0, 2), (0, 5), (2, 2), (2, 5)]:
    test[r][c] = "0" if test[r][c] == "1" else "1"
assert analyse(["".join(r) for r in test]) == ([], [])
# two errors in different rows and columns: two failing rows and two failing columns
test = [list(r) for r in safe + [sp]]
for r, c in [(0, 2), (2, 5)]:
    test[r][c] = "0" if test[r][c] == "1" else "1"
br, bc = analyse(["".join(r) for r in test])
assert len(br) == 2 and len(bc) == 2
# two errors in one row: no failing row, two failing columns
test = [list(r) for r in safe + [sp]]
for r, c in [(1, 2), (1, 5)]:
    test[r][c] = "0" if test[r][c] == "1" else "1"
br, bc = analyse(["".join(r) for r in test])
assert br == [] and len(bc) == 2
# every single flip in the SECURED block is located exactly
base = list(sent) + [parity_byte]
for r in range(8):
    for c in range(8):
        test = [list(x) for x in base]
        test[r][c] = "0" if test[r][c] == "1" else "1"
        assert analyse(["".join(x) for x in test]) == ([r + 1], [c])

# ---------------------------------------------------------------------------------------------
# Checksum
# ---------------------------------------------------------------------------------------------
data = [52, 200, 117, 83]
assert sum(data) == 452 and 452 - 256 == 196 == sum(data) % 256
assert sum([52, 200, 119, 83]) == 454 and 454 - 256 == 198 != 196
assert sum([200, 52, 117, 83]) % 256 == 196
assert 10 + 20 + 250 == 280 and 280 - 256 == 24 == (10 + 20 + 250) % 256

# ---------------------------------------------------------------------------------------------
# Other facts
# ---------------------------------------------------------------------------------------------
def shift_encrypt(text, key):
    return "".join(chr((ord(c) - 65 + key) % 26 + 65) for c in text)


assert shift_encrypt("HELLO", 3) == "KHOOR" and shift_encrypt("KHOOR", 23) == "HELLO" and 26 - 3 == 23
assert (82, 28) == (82, 28) and 0 <= 28 <= 100
assert 0 <= 71 <= 100 and 0 <= 14 <= 100 and 11 <= 14 <= 19 and not (11 <= 71 <= 19) and 11 <= 17 <= 19
assert 0 <= 41 <= 50 and 0 <= 14 <= 50
assert "S1043" in ["S1042", "S1043", "S1077"]

print("ok")
