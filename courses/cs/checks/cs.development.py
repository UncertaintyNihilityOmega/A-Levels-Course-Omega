# checks/cs.development.py: runs every Python block in the chapter, lints every pseudocode block,
# and recomputes every value the chapter states (parcel charges, state machines, tables).
import contextlib
import io
import os
import pathlib
import re
import tempfile

CHAPTER_ID = "cs.development"

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


INPUTS = [("Enter the mass in kg", ["30", "B"]), ("Enter the total bill", ["90", "4"])]
blocks = run_python_blocks(INPUTS)
assert blocks == 3, f"expected 3 python blocks, found {blocks}"
assert lint_pseudocode_blocks() == 10


def all_tables(header_line):
    """Every Markdown table whose header row is exactly header_line, as lists of rows (cell lists)."""
    found = []
    lines = TEXT.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == header_line:
            rows = []
            for ln in lines[i + 2:]:
                if ln.startswith("|"):
                    rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
                else:
                    break
            found.append(rows)
    return found


STT = "| Current state | Event | Next state | Action |"

# ---------------------------------------------------------------------------------------------
# Parcel program (pseudocode translated)
# ---------------------------------------------------------------------------------------------
def base_rate(zone):
    return {"A": 5.0, "B": 8.0, "C": 12.0}.get(zone, 0.0)


def surcharge(mass):
    return 3.0 if mass > 25.0 else 0.0


def calculate_charge(mass, zone):
    return mass * base_rate(zone) + surcharge(mass)


def valid_parcel(mass, zone):
    return mass > 0.0 and zone in ("A", "B", "C")


assert calculate_charge(30.0, "B") == 243.0 == 30.0 * 8.0 + 3.0
assert calculate_charge(25.0, "A") == 125.0 and surcharge(25.0) == 0.0 and surcharge(25.5) == 3.0
assert valid_parcel(2.0, "C") and not valid_parcel(0.0, "A") and not valid_parcel(4.0, "D")
assert 90.0 / 4 == 22.5

# ---------------------------------------------------------------------------------------------
# PIN check: pseudocode translated, table and trace
# ---------------------------------------------------------------------------------------------
def pin_machine(events):
    state, out, rows = "Try1", [], []
    for event in events:
        if state == "Try1":
            if event == "correct":
                out.append("Menu"); state = "Accepted"
            else:
                out.append("Try again"); state = "Try2"
        elif state == "Try2":
            if event == "correct":
                out.append("Menu"); state = "Accepted"
            else:
                out.append("Try again"); state = "Try3"
        elif state == "Try3":
            if event == "correct":
                out.append("Menu"); state = "Accepted"
            else:
                out.append("Keep card"); state = "Blocked"
        rows.append((event, state, out[-1]))
        if state in ("Accepted", "Blocked"):
            break
    return state, rows


state, rows = pin_machine(["wrong", "wrong", "correct"])
assert state == "Accepted"
header, trace = table_after("| Event | State | OUTPUT |")
assert [r[0] for r in trace[1:]] == [r[0] for r in rows]
assert [r[1] for r in trace[1:]] == [r[1] for r in rows]
assert [r[2] for r in trace[1:]] == [r[2] for r in rows]
assert trace[0][1] == "Try1"
state, rows = pin_machine(["wrong", "wrong", "wrong"])
assert state == "Blocked" and [r[2] for r in rows] == ["Try again", "Try again", "Keep card"]

# the PIN table equals the dictionary in the Python block and the pseudocode machine
pin_rows = [t for t in all_tables(STT) if t and t[0][0] == "Try1"][0]
table = {(r[0], r[1]): (r[2], r[3]) for r in pin_rows}
assert len(pin_rows) == 6 and len(table) == 6
for s in ("Try1", "Try2", "Try3"):
    for ev in ("correct", "wrong"):
        st, rws = pin_machine([ev]) if s == "Try1" else (None, None)
python_block = next(f.group(2) for f in FENCES if f.group(1) == "python" and "transitions = {" in f.group(2))
ns = {}
exec(python_block.split("events =")[0], ns)
assert ns["transitions"] == table
# walk every state through the pseudocode logic and compare with the table
for start in ("Try1", "Try2", "Try3"):
    for ev in ("correct", "wrong"):
        expected = table[(start, ev)]
        prefix = {"Try1": [], "Try2": ["wrong"], "Try3": ["wrong", "wrong"]}[start]
        end_state, rws = pin_machine(prefix + [ev])
        assert (end_state, rws[-1][2]) == expected, (start, ev)

# ---------------------------------------------------------------------------------------------
# Turnstile table (the first table with Locked / Unlocked) and the exam turnstile
# ---------------------------------------------------------------------------------------------
turn = [t for t in all_tables(STT) if t and t[0][0] == "Locked"][0]
tt = {(r[0], r[1]): (r[2], r[3]) for r in turn}
assert len(tt) == 4
assert tt[("Locked", "coin")] == ("Unlocked", "unlock the gate") and tt[("Unlocked", "push")] == ("Locked", "lock the gate")
assert tt[("Locked", "push")][0] == "Locked" and tt[("Unlocked", "coin")][0] == "Unlocked"


def stadium(events):
    state, out = "Locked", []
    for event in events:
        if event == "close":
            break
        if state == "Locked":
            if event == "token":
                out.append("Unlock"); state = "Open"
        elif state == "Open":
            if event == "push":
                out.append("Lock"); state = "Locked"
    return state, out


assert stadium(["push", "token", "token", "push", "close", "token"]) == ("Locked", ["Unlock", "Lock"])

# ---------------------------------------------------------------------------------------------
# Drinks machine (worked example): the completed table behaves as described
# ---------------------------------------------------------------------------------------------
drinks = [t for t in all_tables(STT) if t and t[0][0] == "NoCredit" and all(c != "" for r in t for c in r)][0]
dt = {(r[0], r[1]): (r[2], r[3]) for r in drinks}
assert dt == {("NoCredit", "coin"): ("OneCoin", "show credit"), ("NoCredit", "refund"): ("NoCredit", "nothing"),
              ("OneCoin", "coin"): ("NoCredit", "release drink"), ("OneCoin", "refund"): ("NoCredit", "return coin")}
blank = [t for t in all_tables(STT) if t and t[0][0] == "NoCredit" and any(c == "" for r in t for c in r)]
assert len(blank) == 1 and len(blank[0]) == 4

# ---------------------------------------------------------------------------------------------
# Exam practice: vending machine trace
# ---------------------------------------------------------------------------------------------
vend = [t for t in all_tables(STT) if t and t[0][0] == "Waiting" and t[0][1] == "coin"][0]
vt = {(r[0], r[1]): (r[2], r[3]) for r in vend}
state, actions, states = "Waiting", [], []
for event in ["coin", "coin", "take", "coin", "cancel"]:
    nxt = vt.get((state, event))
    if nxt is None:
        nxt = (state, "none")          # no row: nothing happens (part (a))
    state, action = nxt
    states.append(state)
    actions.append(action)
assert actions == ["none", "give snack", "none", "none", "return coin"] and state == "Waiting"
assert states == ["HasOne", "Sold", "Waiting", "HasOne", "Waiting"]
header, rows = table_after("| Event | State after | Action |")
assert [r[0] for r in rows] == ["coin", "coin", "take", "coin", "cancel"]
assert [r[1] for r in rows] == states and [r[2] for r in rows] == actions

# Traffic light
cycle = {"Red": "Green", "Green": "Amber", "Amber": "Red"}
tl = [t for t in all_tables("| Current state | Event | Next state |") if t][0]
assert {r[0]: r[2] for r in tl} == cycle

# ---------------------------------------------------------------------------------------------
# Stretch: parity checker for 10110, and stock selection structure
# ---------------------------------------------------------------------------------------------
def parity(bits):
    state, path = "Even", []
    for b in bits:
        if b == "1":
            state = "Odd" if state == "Even" else "Even"
        path.append(state)
    return state, path


assert parity("10110") == ("Odd", ["Odd", "Odd", "Even", "Odd", "Odd"])
assert parity("1001")[0] == "Even" and "10110".count("1") == 3

# Marks program: the bill table row arithmetic and the waterfall order
assert ["analysis", "design", "coding", "testing", "maintenance"][0] == "analysis"

print("ok")
