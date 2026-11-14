# checks/cs.usertypes.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (traces, totals, counts, sorted arrays).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.usertypes"

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


PSEUDO_BLOCKS = 15

INPUTS = []
blocks = run_python_blocks(INPUTS)
assert blocks == 7, f"expected 7 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == PSEUDO_BLOCKS, "pseudocode block count changed"

# ---------------------------------------------------------------------------------------------
# Warm-up and small facts
# ---------------------------------------------------------------------------------------------
assert 47 % 5 == 2

# ---------------------------------------------------------------------------------------------
# Pointer example: B copies the value, P^ follows the address (a one-cell memory model)
# ---------------------------------------------------------------------------------------------
memory = {"A": 10}
B = memory["A"]
P = "A"                      # P ← ^A stores the address
memory["A"] = 25
assert f"{B} {memory[P]}" == "10 25"
# Score/Ptr example: outputs 40 then 55
mem = {"Score": 40}
Ptr = "Score"
first = mem[Ptr]
mem["Score"] = 55
assert (first, mem[Ptr]) == (40, 55)
# practice: Stock/Backup/Link
mem = {"Stock": 12}
backup = mem["Stock"]
link = "Stock"
mem["Stock"] = 9
assert f"{backup} {mem[link]}" == "12 9"
# try: N becomes 8
mem = {"N": 7}
ptr = "N"
mem["N"] += 1
assert mem[ptr] == 8

# ---------------------------------------------------------------------------------------------
# Hashing: addresses, collisions, linear probing (generic)
# ---------------------------------------------------------------------------------------------
def store_all(keys, n, base):
    """Linear probing in a file of n slots numbered from base; returns (slots, tried per key)."""
    slots = [0] * n
    tried = {}
    for k in keys:
        a = k % n
        route = []
        while True:
            route.append(a + base)
            if slots[a] <= 0:
                slots[a] = k
                break
            a = (a + 1) % n
        tried[k] = route
    return slots, tried


# Worked example: 11 slots numbered 1..11, Key MOD 11 + 1
KEYS = [4023, 5117, 2064, 8830, 1479, 3306, 7712, 4045]
slots, tried = store_all(KEYS, 11, 1)
assert slots == [0, 7712, 5117, 0, 0, 1479, 3306, 2064, 4023, 8830, 4045]
header, rows = table_after("| Key | Key MOD 11 |")
assert [int(r[0]) for r in rows] == KEYS
assert [int(r[1]) for r in rows] == [k % 11 for k in KEYS] == [8, 2, 7, 8, 5, 6, 1, 8]
assert [int(r[2]) for r in rows] == [k % 11 + 1 for k in KEYS]
assert [[int(x) for x in r[3].split(", ")] for r in rows] == [tried[k] for k in KEYS]
assert [int(r[4]) for r in rows] == [tried[k][-1] for k in KEYS] == [9, 3, 8, 10, 6, 7, 2, 11]
assert tried[8830] == [9, 10] and tried[4045] == [9, 10, 11]
# 11 x 365 = 4015 etc. quoted in the text are not stated; the table is the claim.

# searches in that file
def search(keys_slots, key, n=11):
    a = key % n
    reads = []
    while len(reads) < n:
        reads.append(a + 1)
        if keys_slots[a] == key:
            return a + 1, reads
        if keys_slots[a] == 0:
            return 0, reads
        a = (a + 1) % n
    return 0, reads


assert search(slots, 4045) == (11, [9, 10, 11])
assert search(slots, 6000) == (0, [6, 7, 8, 9, 10, 11, 1]) and 6000 % 11 + 1 == 6
# student's mistake: blank slot 10 breaks the chain; a marker keeps it
broken = list(slots)
broken[9] = 0
assert search(broken, 4045)[0] == 0
marked = list(slots)
marked[9] = -1
assert search(marked, 4045) == (11, [9, 10, 11])

# Figure 1 (organisations): same six keys, 8 slots, Key MOD 8 + 1
ARRIVAL = [6045, 2171, 9308, 4417, 1052, 7734]
slots8, tried8 = store_all(ARRIVAL, 8, 1)
assert slots8 == [0, 4417, 0, 2171, 9308, 6045, 1052, 7734]
assert tried8[1052] == [5, 6, 7] and tried8[7734] == [7, 8]
assert [k for k in ARRIVAL if len(tried8[k]) == 1 and k % 8 + 1 == tried8[k][0]] == [6045, 2171, 9308, 4417]
assert sorted(ARRIVAL) == [1052, 2171, 4417, 6045, 7734, 9308]
header, rows = table_after("| Key in the index |")
assert [int(c) for c in header[1:]] == sorted(ARRIVAL)
assert [int(c) for c in rows[0][1:]] == [1, 2, 3, 4, 5, 6]

# Folding
assert (483 + 912, (483 + 912) % 11, (483 + 912) % 11 + 1) == (1395, 9, 10)
assert 11 * 126 == 1386 and 1395 - 1386 == 9

# ---------------------------------------------------------------------------------------------
# Random file, pseudocode translated: CreateFile, StoreAccount, FindAccount, DeleteAccount
# ---------------------------------------------------------------------------------------------
class RandomFile:
    """OPENFILE FOR RANDOM, SEEK, GETRECORD, PUTRECORD on a dict of records."""
    def __init__(self):
        self.records, self.pointer, self.gets = {}, None, 0

    def seek(self, address):
        self.pointer = address

    def get(self):
        self.gets += 1
        return dict(self.records[self.pointer])

    def put(self, record):
        self.records[self.pointer] = dict(record)


FILE = RandomFile()
SLOTS = 11


def Hash(key):
    return (key % SLOTS) + 1


def CreateFile():
    blank = {"AccountKey": 0, "Holder": "", "Balance": 0.0}
    for address in range(1, SLOTS + 1):
        FILE.seek(address)
        FILE.put(blank)


def StoreAccount(new, empty_test):
    address = Hash(new["AccountKey"])
    placed = False
    while not placed:
        FILE.seek(address)
        existing = FILE.get()
        if empty_test(existing["AccountKey"]):
            FILE.seek(address)
            FILE.put(new)
            placed = True
        else:
            address = (address % SLOTS) + 1


def FindAccount(search_key):
    address, tries, result, finished = Hash(search_key), 0, 0, False
    while not finished and tries < SLOTS:
        FILE.seek(address)
        existing = FILE.get()
        if existing["AccountKey"] == search_key:
            result = address
            finished = True
        elif existing["AccountKey"] == 0:
            finished = True
        else:
            address = (address % SLOTS) + 1
            tries += 1
    return result


def DeleteAccount(search_key):
    address = FindAccount(search_key)
    if address != 0:
        FILE.seek(address)
        FILE.put({"AccountKey": -1, "Holder": "", "Balance": 0.0})


def layout():
    return [FILE.records[a]["AccountKey"] for a in range(1, SLOTS + 1)]


CreateFile()
for k in KEYS:
    StoreAccount({"AccountKey": k, "Holder": "x", "Balance": 1.0}, lambda key: key == 0)
assert layout() == slots
FILE.gets = 0
assert FindAccount(4045) == 11 and FILE.gets == 3
FILE.gets = 0
assert FindAccount(6000) == 0 and FILE.gets == 7
DeleteAccount(8830)
assert layout()[9] == -1 and FindAccount(4045) == 11 and FindAccount(8830) == 0
# a store after the deletion reuses the marked slot (empty test <= 0): 8830 hashes to 9, goes to 10
StoreAccount({"AccountKey": 8830, "Holder": "x", "Balance": 1.0}, lambda key: key <= 0)
assert layout()[9] == 8830
# a full file does not loop for ever in FindAccount (Tries safeguard)
for a in range(1, SLOTS + 1):
    FILE.records[a]["AccountKey"] = 1000 + a
assert FindAccount(5) == 0

# Python struct block: sizes
import struct
assert struct.Struct("<i16sd").size == 28 and 11 * 28 == 308

# ---------------------------------------------------------------------------------------------
# Master file update (the Python block checks the output; assert the logic here too)
# ---------------------------------------------------------------------------------------------
master = {101: ("Aziz", 400), 105: ("Bea", 520), 110: ("Carlos", 380), 120: ("Dara", 610)}
master[105] = ("Bea", 560)
del master[110]
master[112] = ("Elif", 450)
assert sorted(master) == [101, 105, 112, 120]

# ---------------------------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------------------------
assert 85 % 13 == 7 and 13 * 6 == 78 and 85 - 78 == 7 and 85 % 13 + 1 == 8
s7, t7 = store_all([16, 23, 9], 7, 0)
assert (t7[16], t7[23], t7[9]) == ([2], [2, 3], [2, 3, 4]) and s7[2:5] == [16, 23, 9]

# ---------------------------------------------------------------------------------------------
# Exam practice
# ---------------------------------------------------------------------------------------------
s7, t7 = store_all([38, 27, 59, 16, 41, 70], 7, 1)
assert [k % 7 + 1 for k in [38, 27, 59, 16, 41, 70]] == [4, 7, 4, 3, 7, 1]
assert s7 == [41, 70, 16, 38, 59, 0, 27]
assert sum(1 for k in [38, 27, 59, 16, 41, 70] if len(t7[k]) > 1) == 3
header, rows = table_after("| Slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
assert [c for c in rows[0][1:]] == ["41", "70", "16", "38", "59", "empty", "27"]

# StorePart: 13 slots, addresses 0..12, PartNo MOD 13, next (Address + 1) MOD 13
PARTS = {a: 0 for a in range(13)}


def StorePart(part_no):
    address, placed = part_no % 13, False
    while not placed:
        if PARTS[address] == 0:
            PARTS[address] = part_no
            placed = True
        else:
            address = (address + 1) % 13
    return address


assert [StorePart(p) for p in [2606, 3118, 4521, 1170, 8203]] == [6, 11, 10, 0, 1]
PARTS = {a: 0 for a in range(13)}
PARTS[12] = 99
assert (12 + 1) % 13 == 0 and StorePart(12 + 13 * 5) == 0       # wrap from 12 to 0

# Stretch 1: multiples of ten
MULT = [120, 230, 340, 450, 560, 670, 780, 890]
assert {k % 10 for k in MULT} == {0}
s10, t10 = store_all(MULT, 10, 0)
reads10 = [len(t10[k]) for k in MULT]
assert reads10 == [1, 2, 3, 4, 5, 6, 7, 8] and sum(reads10) == 36 and s10[:8] == MULT
assert [k % 13 for k in MULT] == [3, 9, 2, 8, 1, 7, 0, 6] and len({k % 13 for k in MULT}) == 8
s13, t13 = store_all(MULT, 13, 0)
assert sum(len(t13[k]) for k in MULT) == 8

# Stretch 2: index of 50 entries for 5000 records in blocks of 100
assert 5000 // 100 == 50 and 50 + 100 == 150

# Quiz
assert 100 % 11 == 1 and 100 % 11 + 1 == 2 and 11 * 9 == 99
assert len({3, 5, 3, 7, 5}) == 3
assert len({"S", "E", "T", "S", "E", "T"}) == 3

print("ok")
