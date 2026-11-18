# checks/cs.translators.py: runs every Python block in the chapter, lints pseudocode, and recomputes every value, grammar decision and RPN result the chapter states.
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.translators"

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
assert blocks == 6, f"expected 6 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 2

from fractions import Fraction
import itertools

# ---------------------------------------------------------------------------------------------
# A small BNF engine that reads the grammars printed in the chapter (right recursion only)
# ---------------------------------------------------------------------------------------------
TEXT_BLOCKS = [f.group(2) for f in FENCES if f.group(1) == "text"]


def block_with(marker):
    found = [b for b in TEXT_BLOCKS if marker in b]
    assert found, f"no text block contains {marker!r}"
    return found[0]


def read_grammar(*blocks):
    grammar = {}
    for block in blocks:
        for line in block.split("\n"):
            if "::=" not in line:
                continue
            name, rhs = line.split("::=")
            alts = []
            for alt in rhs.split("|"):
                alts.append(re.findall(r"<\w+>|[^<\s]+", alt.strip()))
            grammar[name.strip()] = alts
    return grammar


def valid(grammar, start, text):
    memo = {}

    def ends(symbol, i):
        key = (symbol, i)
        if key in memo:
            return memo[key]
        memo[key] = set()
        result = set()
        if symbol.startswith("<"):
            for alt in grammar[symbol]:
                positions = {i}
                for item in alt:
                    positions = {j for p in positions for j in ends(item, p)}
                result |= positions
        elif text.startswith(symbol, i):
            result.add(i + len(symbol))
        memo[key] = result
        return result

    return len(text) in ends(start, 0)


digit_block = block_with("<digit> ::= 0|1|2|3|4|5|6|7|8|9\n")
integer_block = block_with("<integer> ::= <digit> | <digit><integer>")
G_INT = read_grammar(digit_block, integer_block)
assert valid(G_INT, "<integer>", "407") and not valid(G_INT, "<integer>", "12a") and not valid(G_INT, "<integer>", "")

# the derivation of 407 printed in the chapter: 2 steps per digit, 7 lines
deriv = [ln.strip() for ln in block_with("⇒ 40<digit>").split("\n") if ln.strip()]
assert len(deriv) == 7 == 2 * 3 + 1 and deriv[-1] == "⇒ 407"

G_TAG = read_grammar(block_with("<tag>    ::= <colour><number>"))
for s, want in [("G213", True), ("R", False), ("B40", False), ("3G", False)]:
    assert valid(G_TAG, "<tag>", s) == want, s

G_LOCK = read_grammar(block_with("<code>   ::= <block>-<number>"))
for s, want in [("B-27", True), ("D-304", True), ("E-5", False), ("C-1234", False), ("A27", False), ("B-", False)]:
    assert valid(G_LOCK, "<code>", s) == want, s
# the syntax diagram (figure 2) means one to three digits
for n in range(0, 6):
    assert valid(G_LOCK, "<number>", "7" * n) == (1 <= n <= 3), n

G_ID = read_grammar(block_with("<identifier> ::= <letter> | <letter><rest>"))
for s, want in [("MARK2", True), ("2MARK", False), ("", False), ("M", True), ("A1B2", True)]:
    assert valid(G_ID, "<identifier>", s) == want, s
assert valid(G_ID, "<identifier>", "TOTAL2") and not valid(G_ID, "<identifier>", "2TOTAL")

G_TRAY = read_grammar(block_with("<tray>  ::= <first><digit><digit><last>"))
for s, want in [("S42Z", True), ("R00X", True), ("S4Z", False), ("A42Z", False), ("S42Y", False)]:
    assert valid(G_TRAY, "<tray>", s) == want, s
G_ROOM = read_grammar(block_with("<room>   ::= <floor><number>"))
for s, want in [("G07", True), ("214", True), ("3", False), ("2A5", False)]:
    assert valid(G_ROOM, "<room>", s) == want, s
G_DISC = read_grammar(block_with("<code>   ::= <series>-<digit><digit>"))
for s, want in [("KM-41", True), ("P-5", False), ("MK-3", False), ("P-14", True), ("KMP-11", False)]:
    assert valid(G_DISC, "<code>", s) == want, s

bad_pin = read_grammar(block_with("<pin>   ::= <digit>|<digit>|<digit>|<digit>"))
assert valid(bad_pin, "<pin>", "1") and not valid(bad_pin, "<pin>", "1234")
good_pin = dict(bad_pin)
good_pin["<pin>"] = [["<digit>"] * 4]
assert valid(good_pin, "<pin>", "1234") and not valid(good_pin, "<pin>", "123")

G_TIME = read_grammar(block_with("<time>    ::= <hour>:<minute>"))
for h, m in itertools.product(range(100), range(100)):
    text = f"{h:02d}:{m:02d}"
    assert valid(G_TIME, "<time>", text) == (h <= 23 and m <= 59), text
assert not valid(G_TIME, "<time>", "7:45") and not valid(G_TIME, "<time>", "07:455")
assert all(not (h <= 23) for h in (24, 37, 99))      # accepted by <hour> ::= <digit><digit> but not hours

G_BITS = {"<bit>": [["0"], ["1"]], "<bits>": [["<bit>"], ["<bit>", "<bits>"]]}
assert valid(G_BITS, "<bits>", "1011") and not valid(G_BITS, "<bits>", "102") and not valid(G_BITS, "<bits>", "")

# ---------------------------------------------------------------------------------------------
# Code generation and optimisation
# ---------------------------------------------------------------------------------------------
memory = {200: 40, 201: 6}
acc = memory[200]
assert acc == 40
acc += memory[201]
assert acc == 46
acc -= 5
assert acc == 41
memory[202] = acc
assert memory[202] == 41 == 40 + 6 - 5
assert 60 * 60 * 24 == 86400
assert 1000 - 1 == 999

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
stack, popped = [], []
stack.append(4)
stack.append(9)
popped.append(stack.pop())
stack.append(2)
popped.append(stack.pop())
assert popped == [9, 2] and stack == [4]
assert 3 + 4 * 2 == 11 and 4 * 2 == 8

# ---------------------------------------------------------------------------------------------
# RPN: an independent converter (precedence climbing, then post-order), evaluator and stack-size counter
# ---------------------------------------------------------------------------------------------
PREC = {"+": 1, "-": 1, "*": 2, "/": 2}


def convert(text):
    toks = re.findall(r"\d+|[A-Za-z]|[-+*/()]", text)
    pos = 0

    def peek():
        return toks[pos] if pos < len(toks) else None

    def primary():
        nonlocal pos
        t = toks[pos]
        pos += 1
        if t == "(":
            node = expr(1)
            assert toks[pos] == ")"
            pos += 1
            return node
        return t

    def expr(minimum):
        nonlocal pos
        left = primary()
        while peek() in PREC and PREC[peek()] >= minimum:
            op = toks[pos]
            pos += 1
            left = (op, left, expr(PREC[op] + 1))
        return left

    tree = expr(1)
    assert pos == len(toks)
    return tree


def post(tree):
    return [tree] if isinstance(tree, str) else post(tree[1]) + post(tree[2]) + [tree[0]]


def rpn_of(text):
    return " ".join(post(convert(text)))


def evaluate(rpn, values):
    st = []
    shown = []
    for t in rpn.split():
        if t in PREC:
            b, a = st.pop(), st.pop()
            st.append({"+": a + b, "-": a - b, "*": a * b, "/": a / b}[t])
        else:
            st.append(Fraction(values[t]) if t in values else Fraction(int(t)))
        shown.append([int(v) if v.denominator == 1 else v for v in st])
    assert len(st) == 1
    return st[0], shown


def max_stack(rpn):
    depth, best = 0, 0
    for t in rpn.split():
        depth += -1 if t in PREC else 1
        best = max(best, depth)
    return best


# the table of conversions in the chapter, and the same value from the infix and the RPN form
header, rows = table_after("| Infix | Reverse Polish |")
assert len(rows) == 5
values = {"A": 6, "B": 3, "C": 2}
for infix, rpn in rows:
    infix, rpn = infix.strip("`"), rpn.strip("`")
    assert rpn_of(infix) == rpn, (infix, rpn_of(infix))
    expected = eval(re.sub(r"([A-C])", lambda m: f"Fraction({values[m.group(1)]})", infix))
    assert evaluate(rpn, values)[0] == expected, infix

assert rpn_of("(A + B) * (C - D) / E") == "A B + C D - * E /"
assert "(((A B +) (C D -) *) E /)".replace("(", "").replace(")", "") == "A B + C D - * E /"


def table_rows(marker, nth):
    start = -1
    for _ in range(nth + 1):
        start = TEXT.index(marker, start + 1)
    out = []
    for line in TEXT[start:].split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                out.append(cells)
        elif out:
            break
    return out[1:]


def check_trace(rows_, rpn, vals, answer):
    value, shown = evaluate(rpn, vals)
    assert value == answer, (rpn, value)
    assert len(rows_) == len(shown), (rpn, len(rows_), len(shown))
    for (token, action, stack_text), want in zip(rows_, shown):
        got = [int(x) for x in stack_text.split(",")]
        assert got == want, (rpn, token, got, want)


HEAD = "| Token | Action | Stack (bottom to top) |"
check_trace(table_rows(HEAD, 0), "A B + C D - * E /", {"A": 3, "B": 5, "C": 9, "D": 4, "E": 2}, 20)
check_trace(table_rows(HEAD, 1), "W X + Y * Z -", {"W": 4, "X": 6, "Y": 3, "Z": 7}, 23)
assert evaluate("9 4 -", {})[0] == 5 and evaluate("4 9 -", {})[0] == -5

# RPN to infix example
assert evaluate("P Q R - S * +", {"P": 2, "Q": 7, "R": 3, "S": 5})[0] == 22 == 2 + (7 - 3) * 5
assert rpn_of("P + (Q - R) * S") == "P Q R - S * +"

# Spot the error: precedence
assert rpn_of("K * L + M * N") == "K L * M N * +"
vals = {"K": 2, "L": 3, "M": 4, "N": 5}
assert evaluate("K L * M N * +", vals)[0] == 26 and evaluate("K L * M + N *", vals)[0] == 50

# Try questions and exam practice
assert rpn_of("(P + Q) / R - S") == "P Q + R / S -"
assert evaluate("12 3 - 4 *", {})[0] == 36 and evaluate("6 2 / 3 4 * +", {})[0] == 15
assert rpn_of("X * (Y + Z)") == "X Y Z + *" and rpn_of("X * Y + Z / W") == "X Y * Z W / +"
assert rpn_of("(A + B * C) / (D - E)") == "A B C * + D E - /"
assert convert("(A + B * C) / (D - E)") == ("/", ("+", "A", ("*", "B", "C")), ("-", "D", "E"))

# Stretch: stack sizes
assert max_stack("P Q R S T + + + +") == 5
assert rpn_of("((P + Q) + R) + S") == "P Q + R + S +" and max_stack("P Q + R + S +") == 2
assert max_stack("A B + C D - * E /") == 3

# Quiz
assert evaluate("20 4 - 2 /", {})[0] == 8
assert (4 - 20) / 2 == -8 and 20 - 4 / 2 == 18 and (20 / 4) - 2 == 3
assert rpn_of("A - B - C") == "A B - C -" and rpn_of("A - (B - C)") == "A B C - -"

# Parse tree of A + B * 3: the multiplication sits below the addition
assert convert("A + B * 3") == ("+", "A", ("*", "B", "3"))

print("ok")
