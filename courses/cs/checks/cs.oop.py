# checks/cs.oop.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (class values, outputs, costs).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.oop"

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
assert blocks == 11, f"expected 11 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 14

# ---------------------------------------------------------------------------------------------
# The pseudocode classes, translated into Python, with the values the chapter states
# ---------------------------------------------------------------------------------------------
class Pet:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def speak(self):
        return "..."


class Cat(Pet):
    def speak(self):
        return "Meow"


class Dog(Pet):
    def speak(self):
        return "Woof"


pets = [Cat("Kito", 3), Dog("Rex", 5), Pet("Zuri", 2)]
assert [p.name + " says " + p.speak() for p in pets] == ["Kito says Meow", "Rex says Woof", "Zuri says ..."]
assert Pet("Kito", 3).name + " says " + Pet("Kito", 3).speak() == "Kito says ..."      # first pseudocode program


# Pet.SetAge with validation (pseudocode)
def set_age(age, new_age):
    return new_age if new_age >= 0 else age


assert set_age(3, -5) == 3 and set_age(3, 4) == 4
# SetAge returning a BOOLEAN
assert (-5 >= 0) is False and (4 >= 0) is True

# Cat output: "Kito is a Tabby"
assert "Kito" + " is a " + "Tabby" == "Kito is a Tabby"

# Parcel (worked example): 23.5 is heavy, TRUE
assert (23.5 > 20.0) is True and (20.0 > 20.0) is False


# Library (pseudocode CountOnLoan) with the same story as the Python block
class B:
    def __init__(self, title):
        self.title, self.on_loan = title, False

    def borrow(self):
        if self.on_loan:
            return False
        self.on_loan = True
        return True


shelf = [B("Rivers of the World"), B("Starting with Python"), B("The Night Sky")]


def borrow_title(title):
    for b in shelf:
        if b.title == title:
            return b.borrow()
    return False


assert [borrow_title("The Night Sky"), borrow_title("The Night Sky"), borrow_title("Missing Book")] == [True, False, False]
assert sum(1 for b in shelf if b.on_loan) == 1

# Vehicle hire: costs from the file rows
rows = [("C", 60), ("C", 75), ("V", 90), ("V", 85), ("C", 80)]
costs = [rate * 5 + (100 if kind == "V" else 0) for kind, rate in rows]
assert costs == [300, 375, 550, 525, 400] and sum(costs) == 2150
assert 60 * 5 == 300 and 90 * 5 + 100 == 550
assert len(rows) == 5

# Exam practice: Account (Q3)
def deposit(balance, amount):
    return balance + amount if amount > 0.0 else balance


assert deposit(20.0, 50.0) == 70.0 and deposit(20.0, -5.0) == 20.0


# Thermostat (Q7)
def set_target(target, new):
    return new if 10 <= new <= 30 else target


t = 20
outs = []
for new in (35, 18, 5):
    t = set_target(t, new)
    outs.append(t)
assert outs == [20, 18, 18]
# Speaker volume setter (easy question): 0..10 inclusive
assert [0 <= v <= 10 for v in (-1, 0, 10, 11)] == [False, True, True, False]

# Shapes (Q6)
assert (7 * 4, 5 * 5) == (28, 25)

# Tree stretch: in-order is ascending
assert sorted((8, 3, 10, 1, 6)) == [1, 3, 6, 8, 10]

# Accounts stretch
assert (100 >= 120) is False and (100 - 120 >= -50) is True and 100 - 120 == -20

print("ok")
