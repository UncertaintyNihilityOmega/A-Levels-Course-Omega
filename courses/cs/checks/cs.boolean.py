# checks/cs.boolean.py: runs every Python block in the chapter and recomputes every Boolean fact,
# table and K-map the chapter states (laws, simplifications, adders, flip-flops, Karnaugh maps).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.boolean"

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



# ---------------------------------------------------------------------------------------------
# cs.boolean: the body of checks/cs.boolean.py (data/cs.boolean_body.py is appended to the shared helper above)
# ---------------------------------------------------------------------------------------------
import itertools
import sys

sys.path.insert(0, str(CHAPTER.parent.parent / "data"))
from cs_kmap_model import solve, term_text, covers, cost, prime_implicants  # noqa: E402

blocks = run_python_blocks([])
assert blocks == 1, f"expected 1 python block, found {blocks}"
assert lint_pseudocode_blocks() == 0

BITS = (0, 1)


def N(a):
    return 1 - a


def same(f, g, n):
    return all(f(*v) == g(*v) for v in itertools.product(BITS, repeat=n))


def tt(f, n):
    return [f(*v) for v in itertools.product(BITS, repeat=n)]


# ---------------------------------------------------------------------------------------------
# Notation and order of operations
# ---------------------------------------------------------------------------------------------
A_, B_, C_ = 1, 0, 0
assert (A_ | (B_ & C_)) == 1 and ((A_ | B_) & C_) == 0        # A + B.C = 1 but (A + B).C = 0
assert (1 | 1) == 1

# ---------------------------------------------------------------------------------------------
# The laws (every law in the table, every input)
# ---------------------------------------------------------------------------------------------
LAWS = {
    "identity and": (lambda a: a & 1, lambda a: a, 1), "identity or": (lambda a: a | 0, lambda a: a, 1),
    "null and": (lambda a: a & 0, lambda a: 0, 1), "null or": (lambda a: a | 1, lambda a: 1, 1),
    "idempotent and": (lambda a: a & a, lambda a: a, 1), "idempotent or": (lambda a: a | a, lambda a: a, 1),
    "complement and": (lambda a: a & N(a), lambda a: 0, 1), "complement or": (lambda a: a | N(a), lambda a: 1, 1),
    "double complement": (lambda a: N(N(a)), lambda a: a, 1),
    "commutative and": (lambda a, b: a & b, lambda a, b: b & a, 2), "commutative or": (lambda a, b: a | b, lambda a, b: b | a, 2),
    "associative and": (lambda a, b, c: (a & b) & c, lambda a, b, c: a & (b & c), 3),
    "associative or": (lambda a, b, c: (a | b) | c, lambda a, b, c: a | (b | c), 3),
    "distributive and": (lambda a, b, c: a & (b | c), lambda a, b, c: (a & b) | (a & c), 3),
    "distributive or": (lambda a, b, c: a | (b & c), lambda a, b, c: (a | b) & (a | c), 3),
    "absorption and": (lambda a, b: a & (a | b), lambda a, b: a, 2), "absorption or": (lambda a, b: a | (a & b), lambda a, b: a, 2),
    "de morgan and": (lambda a, b: N(a & b), lambda a, b: N(a) | N(b), 2),
    "de morgan or": (lambda a, b: N(a | b), lambda a, b: N(a) & N(b), 2),
    "de morgan 3": (lambda a, b, c: N(a & b & c), lambda a, b, c: N(a) | N(b) | N(c), 3),
    "de morgan 3 or": (lambda a, b, c: N(a | b | c), lambda a, b, c: N(a) & N(b) & N(c), 3),
}
for name, (f, g, n) in LAWS.items():
    assert same(f, g, n), name

# absorption table
header, rows = table_after("| A | B | \\(A \\cdot B\\) | \\(A + A \\cdot B\\) |")
assert [[int(x) for x in r] for r in rows] == [[a, b, a & b, a | (a & b)] for a in BITS for b in BITS]

# distributive eg table (8 rows, 8 columns)
header, rows = table_after("| A | B | C | \\(B \\cdot C\\) |")
want = [[a, b, c, b & c, a | (b & c), a | b, a | c, (a | b) & (a | c)] for a in BITS for b in BITS for c in BITS]
assert [[int(x) for x in r] for r in rows] == want
assert [r[4] for r in want] == [r[7] for r in want]

# De Morgan table
header, rows = table_after("| A | B | NOT(A AND B) | NOT A OR NOT B |")
want = [[N(a & b), N(a) | N(b), N(a | b), N(a) & N(b)] for a in BITS for b in BITS]
assert [[int(x) for x in r[2:]] for r in rows] == want
assert [r[0] for r in want] == [r[1] for r in want] and [r[2] for r in want] == [r[3] for r in want]

# De Morgan example: NOT(NOT A . B) = A + NOT B
assert same(lambda a, b: N(N(a) & b), lambda a, b: a | N(b), 2)

# universal gates
nand = lambda a, b: N(a & b)
assert same(lambda a: nand(a, a), lambda a: N(a), 1)
assert same(lambda a, b: N(nand(a, b)), lambda a, b: a & b, 2)
assert same(lambda a, b: nand(N(a), N(b)), lambda a, b: a | b, 2)
assert same(lambda a, b: nand(nand(a, a), nand(b, b)), lambda a, b: a | b, 2)

# ---------------------------------------------------------------------------------------------
# Simplifications
# ---------------------------------------------------------------------------------------------
assert same(lambda a, b: (a & b) | (a & N(b)), lambda a, b: a, 2)                         # eg 1
assert same(lambda a, b, c: (a & b) | (a & b & c) | (N(a) & b), lambda a, b, c: b, 3)     # eg 2: X = B
assert same(lambda a, b: (a & b) | (a & b), lambda a, b: a & b, 2)
assert same(lambda a, b: N(a | b) | N(a & b), lambda a, b: N(a) | N(b), 2)               # eg 3
assert same(lambda a, b: N(a) | N(b), lambda a, b: N(a & b), 2)
assert same(lambda a, b: N(a | b) | N(a & b), lambda a, b: N(a & b), 2)
# the absorption step used in eg 3: NOT A + NOT A.NOT B = NOT A
assert same(lambda a, b: N(a) | (N(a) & N(b)), lambda a, b: N(a), 2)
# shortcut A + NOT A . B = A + B and its dual
assert same(lambda a, b: a | (N(a) & b), lambda a, b: a | b, 2)
assert same(lambda a, b: a & (N(a) | b), lambda a, b: a & b, 2)
# A.B + A.NOT B.C = A.(B + C)
assert same(lambda a, b, c: (a & b) | (a & N(b) & c), lambda a, b, c: a & (b | c), 3)
assert same(lambda a, b, c: (a & b) | (a & N(b) & c), lambda a, b, c: (a & b) | (a & c), 3)
# sum of products from a truth table: X = 1 for rows 011, 100, 101, 111
ROWS_X = {3, 4, 5, 7}
fx = lambda a, b, c: 1 if (a * 4 + b * 2 + c) in ROWS_X else 0
sop = lambda a, b, c: (N(a) & b & c) | (a & N(b) & N(c)) | (a & N(b) & c) | (a & b & c)
assert same(fx, sop, 3)
assert same(fx, lambda a, b, c: (a & N(b)) | (b & c), 3)
# the intermediate lines of the algebra
assert same(sop, lambda a, b, c: (a & N(b) & (N(c) | c)) | (b & c & (N(a) | a)), 3)
header, rows = table_after("| A | B | C | X | Product for the row |")
assert [[int(x) for x in r[:4]] for r in rows] == [[a, b, c, fx(a, b, c)] for a in BITS for b in BITS for c in BITS]
assert [r[4] for r in rows if r[3] == "1"] == [
    "\\(\\text{NOT } A \\cdot B \\cdot C\\)", "\\(A \\cdot \\text{NOT } B \\cdot \\text{NOT } C\\)",
    "\\(A \\cdot \\text{NOT } B \\cdot C\\)", "\\(A \\cdot B \\cdot C\\)"]

# ---------------------------------------------------------------------------------------------
# Half adder and full adder
# ---------------------------------------------------------------------------------------------
half = lambda a, b: (a ^ b, a & b)
header, rows = table_after("| A | B | S (sum) | C (carry) |")
assert [[int(x) for x in r] for r in rows] == [[a, b, *half(a, b)] for a in BITS for b in BITS]
assert half(1, 1) == (0, 1)


def full(a, b, cin):
    s1, c1 = half(a, b)
    s, c2 = half(s1, cin)
    return s, c1 | c2, (s1, c1, c2)


for a, b, c in itertools.product(BITS, repeat=3):
    s, cout, _ = full(a, b, c)
    assert a + b + c == 2 * cout + s                       # it really adds
    assert s == (a ^ b ^ c) == (1 if (a + b + c) % 2 else 0)
    assert cout == (1 if a + b + c >= 2 else 0)
    assert cout == (a & b) | (c & (a ^ b)) == (a & b) | (b & c) | (a & c)
    assert not (_[1] and _[2])                              # the two half-adder carries are never both 1
header, rows = table_after("| A | B | Cin | S1 (A XOR B) |")
want = []
for a, b, c in itertools.product(BITS, repeat=3):
    s, cout, (s1, c1, c2) = full(a, b, c)
    want.append([a, b, c, s1, c1, s, c2, cout])
assert [[int(x) for x in r] for r in rows] == want

# ripple-carry example 0110 + 0111, and the practice 101 + 011
def ripple(x, y, nbits):
    carry, out, table = 0, 0, []
    for i in range(nbits):
        a, b = (x >> i) & 1, (y >> i) & 1
        s, cout, _ = full(a, b, carry)
        table.append([i, a, b, carry, s, cout])
        out |= s << i
        carry = cout
    return out, carry, table


out, carry, table = ripple(0b0110, 0b0111, 4)
assert (out, carry) == (0b1101, 0) and out == 13 and 6 + 7 == 13
header, rows = table_after("| Bit | A | B | Cin | S | Cout |")
assert [[int(x) for x in r] for r in rows] == table
out2, carry2, table2 = ripple(0b101, 0b011, 3)
assert (out2, carry2) == (0b000, 1) and 5 + 3 == 8
start = TEXT.index("| Bit | A | B | Cin | S | Cout |", TEXT.index("Remember that the carry out of one adder"))
seg = TEXT[start:].split("\n")
rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg[2:5]]
assert [[int(x) for x in r] for r in rows] == table2
# full adder exam question: given rows
# the first table printed is the question's (with blanks); the answer table follows
start = TEXT.index("Add the three bits and write the total in binary.")
seg = TEXT[start:].split("\n")
rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg if ln.startswith("|")][2:10]
assert [[int(x) for x in r] for r in rows] == [[a, b, c, full(a, b, c)[0], full(a, b, c)[1]] for a, b, c in itertools.product(BITS, repeat=3)]

# ---------------------------------------------------------------------------------------------
# SR flip-flop from two NOR gates (settled by repeated evaluation)
# ---------------------------------------------------------------------------------------------
nor = lambda a, b: N(a | b)


def sr_step(s, r, q, nq):
    for _ in range(20):
        nq2 = nor(s, q)
        q2 = nor(r, nq2)
        if (q2, nq2) == (q, nq):
            return q, nq
        q, nq = q2, nq2
    raise AssertionError("did not settle")


assert sr_step(1, 0, 0, 1) == (1, 0)           # set
assert sr_step(1, 0, 1, 0) == (1, 0)
assert sr_step(0, 1, 1, 0) == (0, 1)           # reset
assert sr_step(0, 1, 0, 1) == (0, 1)
assert sr_step(0, 0, 1, 0) == (1, 0) and sr_step(0, 0, 0, 1) == (0, 1)   # hold
assert (nor(1, 1), nor(1, 1)) == (0, 0)                                   # S = R = 1: both outputs 0


def sr_run(seq, q, nq):
    out = []
    for s, r in seq:
        if (s, r) == (1, 1):
            q, nq = 0, 0              # both NOR gates see a 1
        else:
            q, nq = sr_step(s, r, q, nq)
        out.append((s, r, q, nq))
    return out


seq = [(0, 0), (1, 0), (0, 0), (0, 1), (0, 0), (1, 1)]
run = sr_run(seq, 0, 1)
header, rows = table_after("| Step | S | R | Q | NOT Q | What happened |")
assert [[int(x) for x in r[1:5]] for r in rows] == [list(t) for t in run]
assert run == [(0, 0, 0, 1), (1, 0, 1, 0), (0, 0, 1, 0), (0, 1, 0, 1), (0, 0, 0, 1), (1, 1, 0, 0)]
# the exam question: starts with Q = 1
run = sr_run([(0, 0), (0, 1), (0, 0), (1, 0), (1, 1)], 1, 0)
start = TEXT.index("The inputs (S, R) take these values in order")
start = TEXT.index("| S | R | Q | NOT Q |", start)
seg = TEXT[start:].split("\n")
rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg[2:7]]
assert [[int(x) for x in r] for r in rows] == [list(t) for t in run]

# ---------------------------------------------------------------------------------------------
# JK flip-flop: two 3-input AND gates and the NOR latch, clocked
# ---------------------------------------------------------------------------------------------
def jk_step(j, k, clk, q, nq):
    s = j & clk & nq
    r = k & clk & q
    assert not (s and r)          # never both 1: no invalid state
    return sr_step(s, r, q, nq)


JK_TABLE = []
for j, k, q in itertools.product(BITS, repeat=3):
    q2, nq2 = jk_step(j, k, 1, q, N(q))
    assert nq2 == N(q2)
    assert q2 == (j & N(q)) | (N(k) & q)                    # characteristic equation
    JK_TABLE.append([j, k, q, q2])
    assert jk_step(j, k, 0, q, N(q)) == (q, N(q))           # clock low: holds
header, rows = table_after("| J | K | Q before the clock pulse | Q after the clock pulse | State |")
assert [[int(x) for x in r[:4]] for r in rows] == JK_TABLE
# JK trace
q, nq, got = 0, 1, []
for j, k in [(1, 0), (0, 0), (0, 1), (1, 1), (1, 1), (0, 0)]:
    q, nq = jk_step(j, k, 1, q, nq)
    got.append(q)
assert got == [1, 1, 0, 1, 0, 0]
header, rows = table_after("| Pulse | J | K | Q after the pulse | Why |")
assert [int(r[3]) for r in rows] == got
# toggling halves the clock frequency
q, nq, seq = 0, 1, []
for _ in range(6):
    q, nq = jk_step(1, 1, 1, q, nq)
    seq.append(q)
assert seq == [1, 0, 1, 0, 1, 0]

# ---------------------------------------------------------------------------------------------
# Karnaugh maps
# ---------------------------------------------------------------------------------------------
gray = [n ^ (n >> 1) for n in range(4)]
assert [format(g, "02b") for g in gray] == ["00", "01", "11", "10"]
assert all(bin(a ^ b).count("1") == 1 for a, b in zip(gray, gray[1:] + gray[:1]))     # cyclic: wrap-around works


def read_map(marker, header_text, nrows, ncols, rowbits, colbits):
    start = TEXT.index(marker)
    start = TEXT.index(header_text, start)
    seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:2 + nrows]
    cells = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg]
    heads = [c.strip() for c in TEXT[start:].split("\n")[0].strip().strip("|").split("|")][1:]
    ones = set()
    for r in cells:
        for h, v in zip(heads, r[1:]):
            if v == "1":
                ones.add(int(r[0] + h, 2))
    return ones


# cell-number tables
for hdr, rowvals in (("| A \\ BC | 00 | 01 | 11 | 10 |", None), ("| AB \\ CD | 00 | 01 | 11 | 10 |", None)):
    pass
start = TEXT.index("For three variables, one variable runs down the side")
seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:4]
cells = [[int(c) for c in ln.strip().strip("|").split("|")[1:]] for ln in seg]
assert cells == [[a * 4 + g for g in gray] for a in (0, 1)]
start = TEXT.index("For four variables, AB runs down the side")
seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:6]
cells = [[int(c) for c in ln.strip().strip("|").split("|")[1:]] for ln in seg]
assert cells == [[r * 4 + g for g in gray] for r in gray]

# 3-variable worked example: cells 3, 4, 5, 7
ones = [3, 4, 5, 7]
sol = solve(3, ones)
assert [term_text(g, 3) for g in sol] == ["A AND NOT B", "B AND C"] and cost(3, sol) == (2, 4)
assert sorted(term_text(p, 3) for p in prime_implicants(3, ones)) == ["A AND C", "A AND NOT B", "B AND C"]
assert read_map("Rows 011, 100, 101 and 111 are cells 3, 4, 5 and 7.", "| A \\ BC |", 2, 4, 1, 2) == set(ones)
assert covers(sol[0], 3) == [4, 5] and covers(sol[1], 3) == [3, 7]
assert same(fx, lambda a, b, c: (a & N(b)) | (b & c), 3)

# Cout and S of the full adder
cout_ones = [m for m in range(8) if full(m >> 2, (m >> 1) & 1, m & 1)[1]]
s_ones = [m for m in range(8) if full(m >> 2, (m >> 1) & 1, m & 1)[0]]
assert cout_ones == [3, 5, 6, 7] and s_ones == [1, 2, 4, 7]
sol = solve(3, cout_ones)
assert sorted(term_text(g, 3) for g in sol) == ["A AND B", "A AND C", "B AND C"] and cost(3, sol) == (3, 6)
assert all(len(covers(p, 3)) == 1 for p in prime_implicants(3, s_ones))              # no groups for S
assert read_map("Cout is 1 for rows 011, 101, 110 and 111, which are cells 3, 5, 6 and 7.", "| A \\ B Cin |", 2, 4, 1, 2) == set(cout_ones)

# 4-variable worked example
ones4 = [0, 1, 2, 5, 6, 7, 8, 9, 10, 14]
sol = solve(4, ones4)
assert sorted(term_text(g, 4) for g in sol) == ["C AND NOT D", "NOT A AND B AND D", "NOT B AND NOT C"] and cost(4, sol) == (3, 7)
groups = {term_text(g, 4): covers(g, 4) for g in sol}
assert groups["NOT B AND NOT C"] == [0, 1, 8, 9] and groups["NOT A AND B AND D"] == [5, 7] and groups["C AND NOT D"] == [2, 6, 10, 14]
assert read_map("Use a Karnaugh map to find the simplest expression. [6 marks]", "| AB \\ CD |", 4, 4, 2, 2) == set(ones4)
f4 = lambda a, b, c, d: 1 if (a * 8 + b * 4 + c * 2 + d) in ones4 else 0
assert same(f4, lambda a, b, c, d: (N(b) & N(c)) | (N(a) & b & d) | (c & N(d)), 4)
# widget suggestions
assert [term_text(g, 4) for g in solve(4, [m for m in ones4 if m != 14])].__len__() == 4
assert [term_text(g, 4) for g in solve(4, [0, 2, 8, 10])] == ["NOT B AND NOT D"]
# figure: group 1 spans rows 00 and 10 (wrap) and columns 00, 01
assert gray.index(0) == 0 and gray.index(2) == 3

# spot the error: cells 1, 2, 3, 6
ones_e = [1, 2, 3, 6]
sol = solve(3, ones_e)
assert sorted(term_text(g, 3) for g in sol) == ["B AND NOT C", "NOT A AND C"]
fe = lambda a, b, c: 1 if (a * 4 + b * 2 + c) in ones_e else 0
assert same(fe, lambda a, b, c: (N(a) & c) | (b & N(c)), 3)
assert not same(fe, lambda a, b, c: N(a) | (a & b & N(c)), 3)                         # the student's answer
assert 0 in [m for m in range(8) if (N(m >> 2) | ((m >> 2) & ((m >> 1) & 1) & N(m & 1)))] and fe(0, 0, 0) == 0
# student's printed map (binary-order headings): values by label
start = TEXT.index("A student drew this map:")
seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:4]
cells = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg]
bad_heads = ["00", "01", "10", "11"]
bad_ones = {int(r[0] + h, 2) for r in cells for h, v in zip(bad_heads, r[1:]) if v == "1"}
assert bad_ones == set(ones_e)
assert read_map("The corrected map puts the headings", "| A \\ BC |", 2, 4, 1, 2) == set(ones_e)
# the 3 extra groups named in the answer
assert sorted(term_text(p, 3) for p in prime_implicants(3, ones_e)) == ["B AND NOT C", "NOT A AND B", "NOT A AND C"]

# De Morgan spot-the-error
fs = lambda a, b: N(a & b) & a
assert same(fs, lambda a, b: a & N(b), 2)
assert fs(1, 0) == 1 and (N(1) & N(0) & 1) == 0                                       # the check in the text

# ---------------------------------------------------------------------------------------------
# Try questions, exam practice, stretch
# ---------------------------------------------------------------------------------------------
assert same(lambda a, b: a | 1, lambda a, b: 1, 2) and same(lambda a: a & a, lambda a: a, 1)
assert same(lambda a, b, c: N(a | b | c), lambda a, b, c: N(a) & N(b) & N(c), 3)
assert half(1, 1) == (0, 1) and full(1, 0, 1)[:2] == (0, 1)
assert same(lambda a, b, c: (a | b) & (a | N(b)) & c, lambda a, b, c: a & c, 3)
xnor = lambda a, b: (a & b) | (N(a) & N(b))
assert same(lambda a, b: N(a & N(b)) & N(N(a) & b), xnor, 2)
assert same(lambda a, b: (N(a) | b) & (a | N(b)), xnor, 2) and same(xnor, lambda a, b: N(a ^ b), 2)
# the expansion steps of the practice question
assert same(lambda a, b: (N(a) | b) & (a | N(b)), lambda a, b: (N(a) & a) | (N(a) & N(b)) | (b & a) | (b & N(b)), 2)
# X ones 0, 1, 3, 7
ones_q = [0, 1, 3, 7]
sol = solve(3, ones_q)
assert sorted(term_text(g, 3) for g in sol) == ["B AND C", "NOT A AND NOT B"]
assert read_map("Rows 000, 001, 011 and 111 are cells 0, 1, 3 and 7.", "| A \\ BC |", 2, 4, 1, 2) == set(ones_q) if "Rows 000, 001, 011 and 111 are cells" in TEXT else True
start = TEXT.index("H: Rows 000, 001, 011 and 111 are cells 0, 1, 3 and 7.")
seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:4]
cells = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg]
assert {int(r[0] + h, 2) for r in cells for h, v in zip(["00", "01", "11", "10"], r[1:]) if v == "1"} == set(ones_q)
# 4-variable exam question
ones_q4 = [3, 4, 5, 7, 11, 12, 13, 15]
sol = solve(4, ones_q4)
assert sorted(term_text(g, 4) for g in sol) == ["B AND NOT C", "C AND D"] and cost(4, sol) == (2, 4)
assert sorted(term_text(p, 4) for p in prime_implicants(4, ones_q4)) == ["B AND D", "B AND NOT C", "C AND D"]
start = TEXT.index("The cells 4, 5, 12 and 13 form a block")
start = TEXT.index("| AB \\ CD |", start)
seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:6]
cells = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg]
assert {int(r[0] + h, 2) for r in cells for h, v in zip(["00", "01", "11", "10"], r[1:]) if v == "1"} == set(ones_q4)
assert [covers(g, 4) for g in sol if term_text(g, 4) == "C AND D"] == [[3, 7, 11, 15]]
assert [covers(g, 4) for g in sol if term_text(g, 4) == "B AND NOT C"] == [[4, 5, 12, 13]]
# stretch: XOR from four NAND gates
for a, b in itertools.product(BITS, repeat=2):
    n1 = nand(a, b)
    n2 = nand(a, n1)
    n3 = nand(b, n1)
    assert nand(n2, n3) == a ^ b
    assert n2 == N(a) | b and n3 == N(b) | a
assert same(lambda a, b: (N(a) | b) & (a | N(b)), xnor, 2)
assert same(lambda a, b: (N(a) | N(b)) & (a | b), lambda a, b: a ^ b, 2)
# stretch: comparator P > Q
ones_c = [m for m in range(16) if 2 * (m >> 3) + ((m >> 2) & 1) > 2 * ((m >> 1) & 1) + (m & 1)]
assert ones_c == [4, 8, 9, 12, 13, 14]
sol = solve(4, ones_c)
assert sorted(term_text(g, 4) for g in sol) == ["A AND B AND NOT D", "A AND NOT C", "B AND NOT C AND NOT D"] and cost(4, sol) == (3, 8)
assert [covers(g, 4) for g in sol if term_text(g, 4) == "A AND NOT C"] == [[8, 9, 12, 13]]
start = TEXT.index("Group cells 8, 9, 12 and 13 (A = 1, C = 0)")
start = TEXT.rindex("| AB \\ CD |", 0, start)
seg = [ln for ln in TEXT[start:].split("\n") if ln.startswith("|")][2:6]
cells = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in seg]
assert {int(r[0] + h, 2) for r in cells for h, v in zip(["00", "01", "11", "10"], r[1:]) if v == "1"} == set(ones_c)
assert (4 >> 2, (4 >> 2) & 3) == (1, 1) and 2 * (4 >> 3) + ((4 >> 2) & 1) == 1 and 2 * ((4 >> 1) & 1) + (4 & 1) == 0   # cell 4: P = 1, Q = 0
assert 2 * (14 >> 3) + ((14 >> 2) & 1) == 3 and 2 * ((14 >> 1) & 1) + (14 & 1) == 2                                    # cell 14: P = 3, Q = 2

# quiz facts
assert same(lambda a, b: a | (a & b), lambda a, b: a, 2) and (1 | 1) == 1
assert sum(1 for a, b, c in itertools.product(BITS, repeat=3) if a + b + c >= 2) == 4   # Cout is 1 in four rows
# S is 1 when an odd number of inputs are 1 (full adder row 1 + 1 + 1 = binary 11)
assert full(1, 1, 1)[:2] == (1, 1)

print("ok")
