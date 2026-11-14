# checks/cs.structures.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.structures"

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


def out_after(marker, nth=1):
    """Lines of the first ```output fence after the nth occurrence of marker."""
    pos = -1
    for _ in range(nth):
        pos = TEXT.index(marker, pos + 1)
    for f in FENCES:
        if f.start() > pos and f.group(1) == "output":
            return [ln.rstrip() for ln in f.group(2).rstrip("\n").split("\n")]
    raise AssertionError("no output fence after " + marker)


def nth_table(marker, nth=1):
    pos = -1
    for _ in range(nth):
        pos = TEXT.index(marker, pos + 1)
    rows = []
    for line in TEXT[pos:].split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
        elif rows:
            break
    return rows[0], rows[1:]


INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 10, f"expected 10 python blocks, found {blocks}"
PSEUDO = lint_pseudocode_blocks()
assert PSEUDO == 16, f"pseudocode blocks: {PSEUDO}"

# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert "ABCDEFGH"[-3:] == "FGH" and str(42) == "42"

# ---------------------------------------------------------------------------------------------
# Files (pseudocode semantics simulated on in-memory "files")
# ---------------------------------------------------------------------------------------------
assert out_after("OPENFILE \"Visitors.txt\" FOR WRITE") == ["Amara", "Bilal", "Chen"]
files = {}
files["Visitors.txt"] = ["Amara", "Bilal", "Chen"]            # WRITE
assert len(files["Visitors.txt"]) == 3
files["Visitors.txt"].append("Dina")                           # APPEND
assert len(files["Visitors.txt"]) == 4
files["Visitors.txt"] = ["Emeka"]                              # WRITE again erases
assert len(files["Visitors.txt"]) == 1

notes = ["Buy rice", "Call the clinic", "Pay the bus fare"]
numbered = [f"{i}: {line}" for i, line in enumerate(notes, 1)]
assert numbered == ["1: Buy rice", "2: Call the clinic", "3: Pay the bus fare"]
assert out_after("print(file.read(), end=\"\")") == numbered

visits = [85, 120, 100, 143, 99, 101, 90]
assert (sum(1 for v in visits if v > 100), len(visits)) == (3, 7)
assert [v for v in visits if v > 100] == [120, 143, 101]
assert out_after("print(busy_days, \"busy days out of\", days)") == ["3 busy days out of 7"]

names = ["Amara", "Bilal", "Chen"]
assert ("Bilal" in names, "Zara" in names) == (True, False)

# Saving records: comma positions and the RIGHT length used by ShowResults
line = "Amina,78"
position = 1
while line[position - 1] != ",":
    position += 1
assert position == 6 and line[:position - 1] == "Amina"
assert len(line) - position == 2 and line[len(line) - (len(line) - position):] == "78"
results = [("Amina", 78), ("Tomas", 64), ("Ngozi", 91)]
shown = [f"{n} scored {m}" for n, m in results]
assert out_after("CALL ShowResults()") == shown

# ---------------------------------------------------------------------------------------------
# Stack
# ---------------------------------------------------------------------------------------------
class Stack:
    def __init__(self, size):
        self.size, self.top, self.items = size, 0, [None] * (size + 1)
        self.log = []

    def push(self, v):
        if self.top == self.size:
            return "Stack overflow"
        self.top += 1
        self.items[self.top] = v
        return None

    def pop(self):
        if self.top == 0:
            return "Stack underflow"
        v = self.items[self.top]
        self.top -= 1
        return v


s = Stack(5)
rows = []
for op in [("Push", 12), ("Push", 7), ("Push", 30), ("Pop",), ("Push", 5), ("Pop",), ("Pop",), ("Pop",), ("Pop",)]:
    before_items = list(s.items)
    before_top = s.top
    res = s.push(op[1]) if op[0] == "Push" else s.pop()
    rows.append((op, s.top if s.top != before_top else None,
                 {i: s.items[i] for i in range(1, 4) if s.items[i] != before_items[i]},
                 res if op[0] == "Pop" else None))
header, trows = nth_table("| Operation | TopPointer | Stack[1] |")
assert [r[0] for r in trows][1:] == [" ".join(str(x) for x in op) for op, *_ in rows]
assert [r[1] for r in trows] == ["0"] + ["" if t is None else str(t) for _, t, _, _ in rows]
for i in (1, 2, 3):
    assert [r[1 + i] for r in trows][1:] == [str(ch[i]) if i in ch else "" for _, _, ch, _ in rows]
assert [r[5] for r in trows][1:] == ["" if r is None else str(r) for *_, r in rows]
assert s.items[4] is None and s.items[5] is None             # Stack[4], Stack[5] never written

# Python stack block output: [12, 7, 5, 0, 0] 0
py = [0] * 5
top = 0
py[0], py[1], py[2] = 12, 7, 30
top = 3
top -= 1                                      # pop 30
top += 1
py[top - 1] = 5                               # push 5 overwrites 30
assert py == [12, 7, 5, 0, 0]
assert "".join(reversed("LIMA")) == "AMIL"

# Red/blue example
st = Stack(6)
st.push("red"); st.push("blue"); assert st.pop() == "blue"; st.push("green"); st.push("pink")
assert (st.top, st.items[1], st.items[2], st.items[3]) == (3, "red", "green", "pink")

# Practice: 8 3 9 pop pop 4 6
st = Stack(5)
for v in (8, 3, 9):
    st.push(v)
popped = [st.pop(), st.pop()]
st.push(4); st.push(6)
assert popped == [9, 3] and (st.top, st.items[1], st.items[2], st.items[3]) == (3, 8, 4, 6)

# ---------------------------------------------------------------------------------------------
# Linear and circular queues
# ---------------------------------------------------------------------------------------------
size = 6
q = ["_"] * size
front, rear = 1, 0
rows = [("start", front, rear, " ".join(q), "")]
for j in range(1, 7):
    rear += 1
    q[rear - 1] = f"J{j}"
    rows.append((f"Enqueue J{j}", None, rear, " ".join(q), ""))
for k in range(3):
    item = q[front - 1]
    front += 1
    rows.append(("Dequeue", front, None, "", item))
assert rear == size                                   # linear: full now
rows.append(("Enqueue J7", None, None, "", "Queue full"))
header, trows = nth_table("| Operation | FrontPointer | RearPointer | Queue | Result |")
assert len(trows) == len(rows) == 11
for got, want in zip(trows, rows):
    assert got[0] == want[0]
    assert got[1] == ("" if want[1] is None else str(want[1])), (got, want)
    assert got[2] == ("" if want[2] is None else str(want[2])), (got, want)
    assert got[3] == want[3] and got[4] == want[4], (got, want)
assert 6 - 3 == 3                                     # only 3 jobs held when refused

# Circular queue
q = ["_"] * 6
front, rear, count = 1, 0, 0
for j in range(1, 7):
    rear = rear % 6 + 1
    q[rear - 1] = f"J{j}"
    count += 1
assert (front, rear, count) == (1, 6, 6)
rows = [("after six Enqueues", front, rear, count, " ".join(q), "")]
for k in range(3):
    item = q[front - 1]
    front = front % 6 + 1
    count -= 1
    rows.append(("Dequeue", front, None, count, "", item))
assert count != 6
rear = rear % 6 + 1
q[rear - 1] = "J7"
count += 1
rows.append(("Enqueue J7", None, rear, count, " ".join(q), ""))
header, trows = nth_table("| Operation | FrontPointer | RearPointer | Count | Queue | Result |")
assert len(trows) == len(rows)
for got, want in zip(trows, rows):
    assert got[0] == want[0]
    for k in (1, 2, 3):
        assert got[k] == ("" if want[k] is None else str(want[k])), (got, want)
    assert got[4] == want[4] and got[5] == want[5], (got, want)
assert (front, rear, count) == (4, 1, 4) and rear == 6 % 6 + 1
assert out_after("for job in [\"J1\"") == ["J1 J2 J3", "['J7', 'J2', 'J3', 'J4', 'J5', 'J6'] 4 1 4"]
assert [(p, p % 6 + 1) for p in range(1, 7)] == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
assert (8 % 8 + 1) == 1

# Practice circular queue of 5: A B C D, dequeue x2, E, F
q = [None] * 5
front, rear, count = 1, 0, 0
for item in "ABCD":
    rear = rear % 5 + 1; q[rear - 1] = item; count += 1
assert (front, rear, count) == (1, 4, 4)
for _ in range(2):
    front = front % 5 + 1; count -= 1
assert (front, count) == (3, 2)
for item in "EF":
    rear = rear % 5 + 1; q[rear - 1] = item; count += 1
assert (front, rear, count) == (3, 1, 4)
live = [q[(front - 1 + k) % 5] for k in range(count)]
assert live == ["C", "D", "E", "F"] and 5 % 5 + 1 == 1

# ---------------------------------------------------------------------------------------------
# Linked list: simulate the pseudocode on 1-based arrays and compare with every table
# ---------------------------------------------------------------------------------------------
class LinkedList:
    def __init__(self, n):
        self.n = n
        self.data = [None] * (n + 1)
        self.ptr = [0] * (n + 1)
        self.start, self.free = 0, 1
        for i in range(1, n):
            self.ptr[i] = i + 1
        self.ptr[n] = 0

    def insert(self, item):
        if self.free == 0:
            return "List full"
        new = self.free
        self.free = self.ptr[new]
        self.data[new] = item
        prev, cur = 0, self.start
        while cur != 0 and self.data[cur] < item:
            prev, cur = cur, self.ptr[cur]
        self.ptr[new] = cur
        if prev == 0:
            self.start = new
        else:
            self.ptr[prev] = new
        return None

    def delete(self, item):
        prev, cur = 0, self.start
        while cur != 0 and self.data[cur] != item:
            prev, cur = cur, self.ptr[cur]
        if cur == 0:
            return item + " not found"
        if prev == 0:
            self.start = self.ptr[cur]
        else:
            self.ptr[prev] = self.ptr[cur]
        self.ptr[cur] = self.free
        self.free = cur
        return None

    def items(self):
        out, cur = [], self.start
        while cur != 0:
            out.append(self.data[cur])
            cur = self.ptr[cur]
        return out


ll = LinkedList(7)
for name in ("Dina", "Farah", "Bilal"):
    ll.insert(name)
assert (ll.start, ll.free, ll.items()) == (3, 4, ["Bilal", "Dina", "Farah"])
before = (list(ll.data), list(ll.ptr))
ll.insert("Chen")
after = (list(ll.data), list(ll.ptr))
assert (ll.start, ll.free) == (3, 5) and ll.items() == ["Bilal", "Chen", "Dina", "Farah"]
header, trows = nth_table("| Index | Data before | Pointer before | Data after | Pointer after |")
assert len(trows) == 7
for i, row in enumerate(trows, 1):
    assert row == [str(i), before[0][i] or "", str(before[1][i]), after[0][i] or "", str(after[1][i])], row
changed = [i for i in range(1, 8) if (before[0][i], before[1][i]) != (after[0][i], after[1][i])]
assert changed == [3, 4]                          # Data[4], Pointer[4], Pointer[3]: three cells, two nodes
assert (after[0][4], after[1][4], after[1][3]) == ("Chen", 1, 4)
# Wrong order: Pointer[3] <- 4 first makes Pointer[4] <- Pointer[3] equal 4
ptr = list(before[1])
ptr[3] = 4
ptr[4] = ptr[3]
assert ptr[4] == 4
# Insert Amara at the front
ll.insert("Amara")
assert (ll.start, ll.free, ll.ptr[5]) == (5, 6, 3)
state_c = (list(ll.data), list(ll.ptr))
assert ll.items() == ["Amara", "Bilal", "Chen", "Dina", "Farah"]
ll.delete("Dina")
state_d = (list(ll.data), list(ll.ptr))
assert (ll.start, ll.free) == (5, 1) and ll.items() == ["Amara", "Bilal", "Chen", "Farah"]
header, trows = nth_table("| Index | Data | Pointer before | Pointer after |")
for i, row in enumerate(trows, 1):
    assert row == [str(i), state_c[0][i] or "", str(state_c[1][i]), str(state_d[1][i])], row
assert state_d[1][1:] == [6, 0, 4, 2, 3, 7, 0] and state_d[0][1] == "Dina"
assert out_after("print(list_items(), start_pointer, free_pointer)") == [
    "['Bilal', 'Dina', 'Farah'] 3 4",
    "['Amara', 'Bilal', 'Chen', 'Dina', 'Farah'] 5 6",
    "['Amara', 'Bilal', 'Chen', 'Farah'] 5 1",
    "Zara not found",
    "['Dina', 'Farah', 'Bilal', 'Chen', 'Amara', None, None] [6, 0, 4, 2, 3, 7, 0]"]

# Exam practice: Hana
EX = LinkedList(6)
EX.data[1:5] = ["Joy", "Alba", "Marta", "Ela"]
EX.ptr[1:7] = [3, 4, 0, 1, 6, 0]
EX.start, EX.free = 2, 5
assert EX.items() == ["Alba", "Ela", "Joy", "Marta"]
EX.insert("Hana")
assert (EX.data[5], EX.ptr[5], EX.ptr[4], EX.free, EX.start) == ("Hana", 1, 5, 6, 2)
assert EX.items() == ["Alba", "Ela", "Hana", "Joy", "Marta"]

# Stretch: Lee deleted, Mia added
ST = LinkedList(5)
ST.data[1:6] = ["Rao", "Sia", "Ana", "Ken", "Lee"]
ST.ptr[1:6] = [2, 0, 4, 5, 1]
ST.start, ST.free = 3, 0
assert ST.items() == ["Ana", "Ken", "Lee", "Rao", "Sia"]
assert ST.insert("Zed") == "List full"
ST.delete("Lee")
assert (ST.ptr[4], ST.ptr[5], ST.free) == (1, 0, 5)
ST.insert("Mia")
assert (ST.data[5], ST.ptr[5], ST.ptr[4], ST.free) == ("Mia", 1, 5, 0)
assert ST.items() == ["Ana", "Ken", "Mia", "Rao", "Sia"]

# Stretch: browser stacks
back, forward, current = [], [], "A"
for page in "BCD":
    back.append(current); forward = []; current = page
assert (back, current) == (["A", "B", "C"], "D")
for _ in range(2):
    forward.append(current); current = back.pop()
assert (current, back, forward) == ("B", ["A"], ["D", "C"])
back.append(current); forward = []; current = "E"
assert (current, back, forward) == ("E", ["A", "B"], [])

# Exam practice: sales file total and empty file
def sales(lines):
    total = n = 0
    for ln in lines:
        total += int(ln)
        n += 1
    return "No data" if n == 0 else f"Total: {total}"


assert sales([]) == "No data" and sales(["5", "7"]) == "Total: 12"

print("ok")
