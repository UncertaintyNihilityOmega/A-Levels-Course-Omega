# checks/cs.security2.py: runs every Python block in the chapter and recomputes every number the chapter states (key counts, toy RSA and signature values, quiz options).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.security2"

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
assert blocks == 4, f"expected 4 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 0

import hashlib

# ---------------------------------------------------------------------------------------------
# Warm-up and key lengths
# ---------------------------------------------------------------------------------------------
assert 17 % 5 == 2 and 17 // 5 == 3
assert 2 ** 8 == 256 and 2 ** 16 == 65536 and len(str(2 ** 128)) == 39 and 2 ** 10 == 1024


def keys(n):
    return n * (n - 1) // 2


assert keys(10) == 45 and keys(40) == 780 and keys(12) == 66
assert 12 * 11 // 2 == 66 and 40 * 39 // 2 == 780 and 10 * 9 // 2 == 45
assert 90 == 10 * 9 and 100 == 10 * 10

# ---------------------------------------------------------------------------------------------
# The XOR toy: decrypting is the same function (the output block was run by the helper)
# ---------------------------------------------------------------------------------------------
def xor_cipher(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


cipher = xor_cipher(b"MEET AT NOON", b"K7")
assert cipher.hex() == "06720e636b761f1705780479" and xor_cipher(cipher, b"K7") == b"MEET AT NOON"

# ---------------------------------------------------------------------------------------------
# Toy RSA: n, e, d; each letter; a wrong key; a signature
# ---------------------------------------------------------------------------------------------
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = pow(e, -1, phi)
assert (n, e, d) == (3233, 17, 2753) and (e * d) % phi == 1
assert [pow(ord(c), e, n) for c in "HI"] == [3000, 1486]
assert [pow(c, d, n) for c in (3000, 1486)] == [72, 73]
assert [pow(c, d + 2, n) for c in (3000, 1486)] == [111, 928]
assert all(pow(c, d + 2, n) != m for c, m in zip((3000, 1486), (72, 73)))
# any message 0..n-1 round-trips, and signing then checking round-trips
assert all(pow(pow(m, e, n), d, n) == m and pow(pow(m, d, n), e, n) == m for m in range(n))


def short_digest(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16) % n


sig = pow(short_digest("Pay Ana 100"), d, n)
assert sig == 994 and pow(sig, e, n) == short_digest("Pay Ana 100")
assert short_digest("Pay Ana 900") != short_digest("Pay Ana 100")
assert pow(sig + 1, e, n) != short_digest("Pay Ana 100")

# the hash properties
h1 = hashlib.sha256(b"Pay Ana 100").hexdigest()
h2 = hashlib.sha256(b"Pay Ana 900").hexdigest()
assert h1[:16] == "ecd0d31ecc3e04e0" and h2[:16] == "2173670831b6a35b"
assert len(h1) == 64 and len(h1) * 4 == 256 and len(hashlib.sha256(b"x" * 10000).hexdigest()) == 64
assert sum(a != b for a, b in zip(h1, h2)) > 40       # a small change alters most of the digest

# ---------------------------------------------------------------------------------------------
# Stretch: the tiny key pair (7, 33) and (3, 33)
# ---------------------------------------------------------------------------------------------
N, E, D = 33, 7, 3
assert (E * D) % ((3 - 1) * (11 - 1)) == 1 and 3 * 11 == N
assert 5 ** 7 == 78125 and 78125 == 33 * 2367 + 14 and pow(5, E, N) == 14
assert 14 ** 3 == 2744 and 2744 == 33 * 83 + 5 and pow(14, D, N) == 5
assert 8 ** 3 == 512 and 512 == 33 * 15 + 17 and pow(8, D, N) == 17 and pow(17, E, N) == 8
assert pow(17, E, N) != 9
assert all(pow(pow(m, E, N), D, N) == m for m in range(N))

print("ok")
