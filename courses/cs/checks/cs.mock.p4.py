# checks/cs.mock.p4.py: Mock Paper 4: marks, links, and every model program written to a temporary folder, run, and its output compared
# (the helper below is the course's standard one; only CHAPTER_ID changes).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.mock.p4"

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


# =============================================================================================
# Mock Paper 4: totals, links, and every model program written out, run in a temporary folder with the
# source files of the question, and its printed output compared with the output in the mark scheme.
# =============================================================================================
import json
from fractions import Fraction

lint_pseudocode_blocks()
ROOT = CHAPTER.parent.parent

# ---- structure: three questions of 20, 25 and 30 marks, 2 h 30 min, links to real chapters
marks = [int(x) for x in re.findall(r"^Q: \[(\d+) marks\]", TEXT, re.M)]
assert marks == [20, 25, 30] and sum(marks) == 75, marks
assert "@time 2 h 30 min" in TEXT and "**2 hours 30 minutes**" in TEXT
assert Fraction(150, 75) == 2 and Fraction(30 * 9, 5) == 54 and "1.8 minutes per mark" in TEXT
assert "a 30-mark question deserves about 54 minutes" in TEXT
assert "**75 marks**" in TEXT and "Question 1 is 20 marks, Question 2 is 25 marks and Question 3 is 30 marks" in TEXT
ids = {c["id"] for c in json.loads((ROOT / "course.json").read_text(encoding="utf-8"))["chapters"]}
assert set(re.findall(r"\(#(cs\.[\w.]+)\)", TEXT)) <= ids
assert len(re.findall(r"^Q: \[\d+ marks\] \(#cs\.\w+\)", TEXT, re.M)) == 3
assert TEXT.rstrip().endswith("Next: [Computer Science: the course map](#cs.overview)") and "cs.overview" in ids
BLOCKS = re.findall(r"^:::try\n(.*?)^:::$", TEXT, re.M | re.S)
assert len(BLOCKS) == 3
for block, total in zip(BLOCKS, marks):
    q, a = block.split("\nA:", 1)
    parts = [int(x) for x in re.findall(r"\[(\d+)\]\s*$", q, re.M)]
    assert sum(parts) == total, (total, parts)
    assert len(re.findall(r"\[B1\]", a)) == total, (total, len(re.findall(r"\[B1\]", a)))
    # one mark scheme part per question part, each with its own mark count
    for letter, n in zip("abcdef", parts):
        seg = re.search(rf"^\({letter}\)(.*?)(?=^\([a-f]\)|\Z)", a.lstrip(), re.M | re.S)
        assert seg is not None, letter
        assert len(re.findall(r"\[B1\]", seg.group(1))) == n, (total, letter, n)


def build_program(answer):
    """The model program of a question: the python blocks in order. A block that starts with four spaces is a
    list of methods to add to the end of the first block (the class Department of Question 3)."""
    blocks = [m.group(1) for m in re.finditer(r"^```python\n(.*?)^```", answer, re.M | re.S)]
    main = [b for b in blocks if not b.startswith("    ")]
    extra = [b for b in blocks if b.startswith("    ")]
    if extra:
        main[0] = main[0].rstrip("\n") + "\n\n" + "\n".join(extra)
    return "\n\n".join(main)


def run_question(question, answer, files):
    with tempfile.TemporaryDirectory() as tmp:
        old = os.getcwd()
        os.chdir(tmp)
        try:
            for name, text in files.items():
                with open(name, "w", newline="\n") as fh:
                    fh.write(text)
            ns = {"__name__": "__main__"}
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                exec(compile(build_program(answer), "model program", "exec"), ns)
            produced = {n: open(n).read() for n in os.listdir(".")}
        finally:
            os.chdir(old)
    want = "".join(m.group(1) for m in re.finditer(r"^```output\n(.*?)^```", answer, re.M | re.S))
    got = out.getvalue()
    assert [l.rstrip() for l in got.rstrip("\n").split("\n")] == [l.rstrip() for l in want.rstrip("\n").split("\n")], (got, want)
    return ns, got, produced


# ---- Question 1: the linked list in global arrays
q1, a1 = BLOCKS[0].split("\nA:", 1)
ns, out1, _ = run_question(q1, a1, {})
assert out1.split("\n")[:-1] == ["List: 15 28 40 51 62", "28 deleted", "99 not found", "List: 15 40 51 62",
                                 "Free pointer: 3", "List: 15 33 40 51 62", "Free pointer: 5"]
lst, start, free = ns["List"], ns["StartPointer"], ns["FreePointer"]
walk, cur = [], start
while cur != -1:
    walk.append(lst[cur].Data)
    cur = lst[cur].Pointer
assert walk == [15, 33, 40, 51, 62]
freed, cur = [], free
while cur != -1:
    freed.append(cur)
    cur = lst[cur].Pointer
assert len(walk) + len(freed) == 10 and free == 5 and freed == [5, 6, 7, 8, 9]
assert [lst[i].Data for i in range(5)] == [40, 15, 62, 33, 51]       # 33 reused the node freed by 28 (index 3)
# the full-list message: eleven numbers into a list of 10
ns["AddItem"](1)  # 6 numbers now
for n in (2, 3, 4, 5):
    ns["AddItem"](n)  # 10 numbers
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns["AddItem"](99)
assert buf.getvalue() == "List full\n" and ns["FreePointer"] == -1
assert "List:" in a1 and "Free pointer:" in a1

# ---- Question 2: the film file
q2, a2 = BLOCKS[1].split("\nA:", 1)
src = re.search(r"Save the data below as `Films\.txt`.*?\n\n```text\n(.*?)```", q2, re.S).group(1)
assert len(src.strip().split("\n")) == 10
ns, out2, files = run_question(q2, a2, {"Films.txt": src})
lines = src.strip().split("\n")
good = []
for i, line in enumerate(lines, 1):
    f = line.split(",")
    try:
        t, d, m, r = f
        good.append((t, int(m), float(r)))
    except ValueError:
        assert i in (4, 7), i
assert len(good) == 8 and ns["FilmCount"] == 8
ref = sorted(good, key=lambda g: -g[2])                           # Python's sort is stable
got = [(ns["Films"][i].Title, ns["Films"][i].Minutes, ns["Films"][i].Rating) for i in range(8)]
assert got == ref and all(ns["Films"][i] is None for i in range(8, 12))
assert [g[0] for g in ref][:3] == ["Copper Sky", "Glass Mountain", "Salt Roads"]
assert [g[2] for g in ref] == [8.4, 8.4, 8.1, 7.8, 7.8, 7.5, 6.9, 6.2]
assert [g[0] for g in ref if g[1] > 120] == ["Copper Sky", "Salt Roads", "Red Lanterns"] and 134 > 120 and 127 > 120 and 122 > 120
longfile = re.search(r"`Long\.txt` then contains:\n\n```text\n(.*?)```", a2, re.S).group(1)
assert files["Long.txt"] == longfile == "Copper Sky\nSalt Roads\nRed Lanterns\n"
assert [g for g in good if g[1] > 120 and g[0] in ("Glass Mountain",)] == [] and 119 < 120
assert "min(N, FilmCount)" in a2

# ---- Question 3: the departments
q3, a3 = BLOCKS[2].split("\nA:", 1)
ns, out3, _ = run_question(q3, a3, {})
budgets = {"Head Office": 50000, "Sales": 120000, "Retail": 45000, "Online": 38000, "Finance": 60000, "Payroll": 15000, "IT": 80000}
assert sum(budgets.values()) == 408000 and 120000 + 45000 + 38000 == 203000
assert "Total budget: 408000" in out3 and "Sales total: 203000" in out3
assert ns["Company"].TotalBudget() == 408000 and ns["Payroll"].TotalBudget() == 15000 and ns["IT"].TotalBudget() == 80000
assert isinstance(ns["Retail"], ns["Department"]) and isinstance(ns["Sales"], ns["SalesDepartment"]) and not isinstance(ns["IT"], ns["SalesDepartment"])
assert ns["Sales"].GetTarget() == 90 and ns["Online"].Describe() == "Online: 38000 (target 25)" and ns["Finance"].Describe() == "Finance: 60000"
assert ns["Company"].FindDepartment("Online") is ns["Online"] and ns["Company"].FindDepartment("Legal") is None
assert ns["Sales"].FindDepartment("Payroll") is None                  # Payroll is not below Sales
assert not hasattr(ns["Company"], "Name") and not hasattr(ns["Company"], "Budget")   # attributes are private

print("ok")

