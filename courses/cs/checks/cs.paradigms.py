# checks/cs.datatypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.paradigms"

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


INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 1, f"expected 1 python block, found {blocks}"
assert lint_pseudocode_blocks() == 1

# ---------------------------------------------------------------------------------------------
# Simulators (assembly and Prolog-style), shared with other chapters through data/
# ---------------------------------------------------------------------------------------------
import runpy

ROOT = CHAPTER.parent.parent
SIM = runpy.run_path(str(ROOT / "data" / "cs.asmsim.py"))
PL = runpy.run_path(str(ROOT / "data" / "cs.prolog_sim.py"))
run, trace = SIM["run"], SIM["trace"]
query = PL["query"]


def block_after(marker, lang="text"):
    start = TEXT.index(marker)
    for f in FENCES:
        if f.start() > start and f.group(1) == lang:
            return f.group(2)
    raise AssertionError(f"no {lang} block after {marker!r}")


def answers(kb, goal, var):
    """All values of one variable, in order."""
    return [a[var] for a in query(kb, goal)]


# ---------------------------------------------------------------------------------------------
# Imperative example: passes
# ---------------------------------------------------------------------------------------------
NAMES = ["Chioma", "Dev", "Elif", "Femi", "Gita"]
MARKS = [64, 48, 91, 50, 37]
passed = [n for n, m in zip(NAMES, MARKS) if m >= 50]
assert passed == ["Chioma", "Elif", "Femi"] and len(passed) == 3
for n, m in zip(NAMES, MARKS):
    assert f"| {n} " in TEXT or f" {n} |" in TEXT
assert "| Marks | 64 | 48 | 91 | 50 | 37 |" in TEXT

# ---------------------------------------------------------------------------------------------
# Warm-up and addressing modes
# ---------------------------------------------------------------------------------------------
assert 150 + 2 == 152
MEM = "160 165\n161 7\n162 41\n163 12\n164 50\n165 99\n"
got = {}
for ins in ("LDM #160", "LDD 160", "LDI 160", "LDX 160"):
    got[ins] = run("100 LDR #2\n101 " + ins + "\n102 END\n" + MEM)[1]["acc"]
assert got == {"LDM #160": 160, "LDD 160": 165, "LDI 160": 99, "LDX 160": 41}
header, rows = table_after("| Instruction | Mode | Steps | ACC afterwards |")
assert [int(r[3]) for r in rows] == [160, 165, 99, 41]
assert 160 + 2 == 162 and 105 + 3 == 108 and 112 - 4 == 108 and 105 + 1 == 106
assert "| Contents | 165 | 7 | 41 | 12 | 50 | 99 |" in TEXT

# try: easy question and exam practice 2
got = {}
for ins in ("LDD 170", "LDI 170", "LDX 170"):
    got[ins] = run("100 LDR #1\n101 " + ins + "\n102 END\n170 172\n171 9\n172 14\n173 30")[1]["acc"]
assert got == {"LDD 170": 172, "LDI 170": 14, "LDX 170": 9} and 170 + 1 == 171
got = {}
for ins in ("LDM #180", "LDD 180", "LDI 180", "LDX 180"):
    got[ins] = run("100 LDR #1\n101 " + ins + "\n102 END\n180 183\n181 12\n182 35\n183 6\n184 77")[1]["acc"]
assert got == {"LDM #180": 180, "LDD 180": 183, "LDI 180": 6, "LDX 180": 12} and 180 + 1 == 181

# relative addressing
assert 210 + 5 == 215 and 208 - 4 == 204 and 308 - 4 == 304

# ---------------------------------------------------------------------------------------------
# Worked example: adding six numbers with IX
# ---------------------------------------------------------------------------------------------
prog = block_after("Plan the program in steps")
fin = run(prog)[1]
NUMS = [14, 9, 22, 5, 18, 7]
assert fin["labels"]["TOTAL"] == 119 and fin["mem"][119] == 75 == sum(NUMS) and fin["ix"] == 6 and fin["mem"][120] == 0
assert [fin["mem"][113 + i] for i in range(6)] == NUMS
header, rows = table_after("After each pass the values are these.")
assert header == ["Pass", "Number read", "IX", "TOTAL", "COUNT"]
total, expect = 0, []
for k, n in enumerate(NUMS, 1):
    total += n
    expect.append([str(k), str(n), str(k), str(total), str(6 - k)])
assert rows == expect and total == 75
# the loop runs exactly six times
steps, _ = run(prog)
assert sum(1 for s in steps if s["text"].strip().endswith("LDX NUMS")) == 6

# ---------------------------------------------------------------------------------------------
# Worked example: pointer (indirect addressing)
# ---------------------------------------------------------------------------------------------
prog = block_after("Trace this program. Show the accumulator")
fin = run(prog)[1]
assert fin["mem"][116] == 29 == 8 + 15 + 6 and fin["mem"][114] == 153 and fin["mem"][115] == 0
eh, er = trace(prog, watch=["PTR", "COUNT", "TOTAL"], cols=("ACC",), start_row=True, show_cmp=True)
header, rows = table_after("First pass:")
assert header == eh[:-1], (header, eh)
assert rows == [r[:-1] for r in er[:14]], (rows, er[:14])
header, rows = table_after("| After pass | Value read | PTR | COUNT | TOTAL |")
ptr, count, total, expect = 150, 3, 0, []
vals = {150: 8, 151: 15, 152: 6}
for k in range(1, 4):
    v = vals[ptr]
    total += v
    ptr += 1
    count -= 1
    expect.append([str(k), str(v), str(ptr), str(count), str(total)])
assert rows == expect

# ---------------------------------------------------------------------------------------------
# Exam practice: count the sevens; the chain
# ---------------------------------------------------------------------------------------------
prog = block_after("Eight numbers are stored in consecutive locations")
# the answer block follows the question text
prog = block_after("A: One possible answer:\n\n```text\n100  START:  LDR #0\n101          LDM #0\n102          STO FOUND")
fin = run(prog)[1]
LIST7 = [7, 3, 7, 7, 1, 9, 7, 2]
assert [fin["mem"][116 + i] for i in range(8)] == LIST7
assert fin["mem"][124] == 4 == LIST7.count(7) and fin["mem"][125] == 0 and fin["ix"] == 8

prog = block_after("Three numbers are held as a chain in memory.")
prog = block_after("The address 0 means")
prog = block_after("A: One possible answer:\n\n```text\n100  START:  LDM #0\n101          STO TOTAL\n102  LOOP:   LDI CUR")
fin = run(prog)[1]
assert fin["mem"][115] == 18 == 5 + 9 + 4 and fin["mem"][113] == 0

# ---------------------------------------------------------------------------------------------
# Declarative: the family
# ---------------------------------------------------------------------------------------------
FACTS = block_after("The facts are:")
RULES = block_after("A father is a male parent")
ANC = block_after("An **ancestor** is a parent")
FAM = FACTS + RULES
assert query(FAM, "father(kofi, ama)") == [{}]
assert query(FAM, "father(yaw, kwame)") == []
assert query(FAM, "parent(esi, kofi)") == []
assert query(FAM, "parent(kofi, ama)") == [{}]
assert answers(FAM, "parent(X, kwame)", "X") == ["ama"]
assert answers(FAM, "parent(kofi, X)", "X") == ["ama", "yaw"]
assert answers(FAM, "grandparent(kofi, X)", "X") == ["kwame", "esi"]
assert answers(FAM, "grandparent(kofi, W)", "W") == ["kwame", "esi"]
assert answers(FAM, "mother(M, kwame)", "M") == ["ama"]
SIB = "sibling(X, Y) IF parent(P, X) AND parent(P, Y) AND X \\= Y.\n"
assert "sibling(X, Y) IF parent(P, X) AND parent(P, Y) AND X \\= Y." in TEXT
assert answers(FAM + SIB, "sibling(ama, X)", "X") == ["yaw", "yaw"]
assert answers(FAM + ANC, "ancestor(kofi, X)", "X") == ["ama", "yaw", "kwame", "esi"]

# marks and the rule with a test
MK = block_after("They become facts, and a rule picks out the ones who passed.")
assert answers(MK, "passed(S)", "S") == ["chioma", "elif", "femi"]

# warn: any-versus-all prerequisites
PRE = ("requires(mechanics, calculus).\nrequires(mechanics, vectors).\ncompleted(imani, calculus).\n"
       "can_take(S, C) IF requires(C, R) AND completed(S, R).\n"
       "can_take_mechanics(S) IF completed(S, calculus) AND completed(S, vectors).\n")
assert query(PRE, "can_take(imani, mechanics)") == [{}]
assert query(PRE, "can_take_mechanics(imani)") == []
assert "can_take(S, C) IF requires(C, R) AND completed(S, R)." in TEXT

# bus eg
BUS = block_after("The relationships are *drives*")
assert answers(BUS, "serves_driver(miraflores, D)", "D") == ["marta"]

# spot the error
BAD = FACTS + block_after("A student wrote the rule below.")
assert answers(BAD, "grandparent(kofi, Z)", "Z") == ["ama", "yaw", "ama", "yaw"]

# try-easy: stock
STOCK = ("stock(rice, 40).\nstock(beans, 0).\nstock(maize, 12).\nin_stock(Item) IF stock(Item, Amount) AND Amount > 0.\n")
assert answers(STOCK, "in_stock(I)", "I") == ["rice", "maize"]

# exam practice: school (c)
SCH = ("teaches(rosa, maths).\nteaches(luis, science).\nstudies(class_7a, maths).\n"
       "taught_by(Class, Teacher) IF studies(Class, Subject) AND teaches(Teacher, Subject).\n"
       "teaches(rosa, physics).\nstudies(class_7a, science).\nstudies(class_8b, physics).\n")
assert answers(SCH, "taught_by(class_7a, T)", "T") == ["rosa", "luis"]
assert "taught_by(Class, Teacher) IF studies(Class, Subject) AND teaches(Teacher, Subject)." in TEXT

# exam practice: flights
FL = block_after("A travel company records flights between cities")
assert answers(FL, "via(lima, X)", "X") == ["bogota", "miami"]
CAN = "can_stay(Town) IF flight(From, Town, Cost) AND hotel(Town, Name, Rate).\n"
assert CAN.strip() in TEXT
assert answers(FL + CAN, "can_stay(T)", "T") == ["quito", "bogota", "bogota", "miami"]

# stretch: boss
BOSS = block_after("A: One possible answer:\n\n```text\nreports_to(dina, sam).")
assert answers(BOSS, "boss(dina, B)", "B") == ["sam", "luca", "mei"]
assert answers(BOSS, "boss(X, mei)", "X") == ["luca", "dina", "sam"]

# quiz
LIKES = "likes(ana, tea).\nlikes(ben, tea).\n"
assert answers(LIKES, "likes(Who, tea)", "Who") == ["ana", "ben"]

# every Prolog-style block of the chapter at least parses
for f in FENCES:
    if f.group(1) == "text" and re.search(r"\.\s*$", f.group(2).strip().split("\n")[0]) and not re.match(r"\d{3}\s", f.group(2)):
        PL["parse_program"](f.group(2))

print("ok")
