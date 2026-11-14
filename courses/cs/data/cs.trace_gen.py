# data/cs.trace_gen.py: builds widgets/cs-trace.js (the cs-trace widget) from data/cs-trace.tpl.js.
# Each program is a pseudocode listing plus a hand translation into Python that records one event per executed
# line (line number, what changed, output). Every run is also computed by a plain Python function and the two
# must agree, so the widget never shows a value the algorithm would not give.
# Run from the course folder:  py data/cs.trace_gen.py
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Ch(str):
    """A CHAR value (shown in single quotes)."""


def fmt(v):
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, Ch):
        return "'" + str(v) + "'"
    if isinstance(v, str):
        return '"' + v + '"'
    return str(v)


class Tracer:
    def __init__(self, names):
        self.names = names
        self.state = {}
        self.events = []
        self.outputs = []

    def at(self, line, note, out=None, **changes):
        changed = {}
        for k, v in changes.items():
            self.state[k] = v
            changed[k] = fmt(v)
        ev = {"line": line, "note": note, "set": changed}
        if out is not None:
            self.outputs.append(out)
            ev["out"] = out
        self.events.append(ev)

    def result(self, label, inputs):
        return {"label": label, "inputs": [fmt(i) if not isinstance(i, int) else str(i) for i in inputs],
                "events": self.events, "final": {k: fmt(v) for k, v in self.state.items()}, "outputs": self.outputs}


# ---------------------------------------------------------------------------------------------------------
# total: WHILE with a sentinel
# ---------------------------------------------------------------------------------------------------------
TOTAL_LINES = [
    "Total ← 0",
    "Days ← 0",
    "INPUT Pages",
    "WHILE Pages <> 0",
    "   Total ← Total + Pages",
    "   Days ← Days + 1",
    "   INPUT Pages",
    "ENDWHILE",
    'OUTPUT "Days: ", Days',
    'OUTPUT "Total pages: ", Total',
]


def total_run(inputs):
    t = Tracer(["Total", "Days", "Pages", "OUTPUT"])
    data = list(inputs)
    total = 0
    t.at(1, "Total starts at 0.", Total=0)
    days = 0
    t.at(2, "Days starts at 0.", Days=0)
    pages = data.pop(0)
    t.at(3, f"Reads {pages} from the list of typed values.", Pages=pages)
    while True:
        test = pages != 0
        word = "TRUE, so the body runs" if test else "FALSE, so the loop ends and the program jumps past ENDWHILE"
        t.at(4, f"Pages <> 0 is {word}.")
        if not test:
            break
        total = total + pages
        t.at(5, f"Total becomes {total}.", Total=total)
        days = days + 1
        t.at(6, f"Days becomes {days}.", Days=days)
        pages = data.pop(0)
        t.at(7, f"Reads {pages} from the list of typed values.", Pages=pages)
    t.at(9, "Outputs the number of days.", out=f"Days: {days}")
    t.at(10, "Outputs the total.", out=f"Total pages: {total}")
    return t, (days, total)


def total_direct(inputs):
    total = days = 0
    for p in inputs:
        if p == 0:
            break
        total += p
        days += 1
    return days, total


# ---------------------------------------------------------------------------------------------------------
# grade: nested IF
# ---------------------------------------------------------------------------------------------------------
GRADE_LINES = [
    "INPUT Mark",
    "IF Mark >= 50 THEN",
    "   IF Mark >= 70 THEN",
    '      Grade ← "Distinction"',
    "   ELSE",
    '      Grade ← "Pass"',
    "   ENDIF",
    "ELSE",
    '   Grade ← "Fail"',
    "ENDIF",
    "OUTPUT Grade",
]


def grade_run(inputs):
    t = Tracer(["Mark", "Grade", "OUTPUT"])
    mark = inputs[0]
    t.at(1, f"Reads {mark} from the list of typed values.", Mark=mark)
    outer = mark >= 50
    t.at(2, f"Mark >= 50 is {'TRUE, so the first branch runs' if outer else 'FALSE, so the program jumps to the outer ELSE'}.")
    if outer:
        inner = mark >= 70
        t.at(3, f"Mark >= 70 is {'TRUE, so the first inner branch runs' if inner else 'FALSE, so the program jumps to the inner ELSE'}.")
        if inner:
            grade = "Distinction"
            t.at(4, 'Grade becomes "Distinction". The inner ELSE is skipped.', Grade=grade)
        else:
            grade = "Pass"
            t.at(6, 'Grade becomes "Pass".', Grade=grade)
    else:
        grade = "Fail"
        t.at(9, 'Grade becomes "Fail".', Grade=grade)
    t.at(11, "Outputs the grade.", out=grade)
    return t, grade


def grade_direct(inputs):
    m = inputs[0]
    return "Distinction" if m >= 70 else "Pass" if m >= 50 else "Fail"


# ---------------------------------------------------------------------------------------------------------
# validate: REPEAT with a fixed list of typed values
# ---------------------------------------------------------------------------------------------------------
VALIDATE_LINES = [
    "REPEAT",
    "   INPUT Age",
    "   IF Age < 5 OR Age > 18 THEN",
    '      OUTPUT "Age must be 5 to 18"',
    "   ENDIF",
    "UNTIL Age >= 5 AND Age <= 18",
    'OUTPUT "Accepted: ", Age',
]


def validate_run(inputs):
    t = Tracer(["Age", "OUTPUT"])
    data = list(inputs)
    t.at(1, "REPEAT starts the loop. The body always runs once before any test.")
    while True:
        age = data.pop(0)
        t.at(2, f"Reads {age} from the list of typed values.", Age=age)
        bad = age < 5 or age > 18
        t.at(3, f"Age < 5 OR Age > 18 is {'TRUE' if bad else 'FALSE'}.")
        if bad:
            t.at(4, "Outputs the error message.", out="Age must be 5 to 18")
        valid = age >= 5 and age <= 18
        t.at(6, f"The UNTIL condition Age >= 5 AND Age <= 18 is {'TRUE, so the loop ends' if valid else 'FALSE, so the loop goes round again'}.")
        if valid:
            break
    t.at(7, "Outputs the accepted age.", out=f"Accepted: {age}")
    return t, age


def validate_direct(inputs):
    for a in inputs:
        if 5 <= a <= 18:
            return a


# ---------------------------------------------------------------------------------------------------------
# countdown: FOR with STEP -2
# ---------------------------------------------------------------------------------------------------------
COUNTDOWN_LINES = [
    "FOR Count ← 10 TO 2 STEP -2",
    "   OUTPUT Count",
    "NEXT Count",
    'OUTPUT "Go!"',
]


def countdown_run(inputs):
    t = Tracer(["Count", "OUTPUT"])
    count = 10
    first = True
    while True:
        if first:
            t.at(1, "The FOR line sets Count to its start value, 10.", Count=count)
            first = False
        elif count >= 2:
            t.at(1, f"Count goes down by 2 to {count}, which has not passed the end value 2, so the body runs.", Count=count)
        if count < 2:
            t.at(1, f"Count would be {count}, which is past the end value 2, so the loop ends.")
            break
        t.at(2, f"Outputs {count}.", out=str(count))
        t.at(3, "NEXT Count sends the program back to the FOR line.")
        count -= 2
    t.at(4, "Outputs the message.", out="Go!")
    return t, None


def countdown_direct(inputs):
    return list(range(10, 1, -2)) + ["Go!"]


# ---------------------------------------------------------------------------------------------------------
# vowels: MID and LENGTH in a loop
# ---------------------------------------------------------------------------------------------------------
VOWELS_LINES = [
    "INPUT Word",
    "Vowels ← 0",
    "FOR Position ← 1 TO LENGTH(Word)",
    "   Letter ← MID(Word, Position, 1)",
    "   IF Letter = 'a' OR Letter = 'e' OR Letter = 'i' OR Letter = 'o' OR Letter = 'u' THEN",
    "      Vowels ← Vowels + 1",
    "   ENDIF",
    "NEXT Position",
    'OUTPUT Word, " has ", Vowels, " vowels"',
]


def vowels_run(inputs):
    t = Tracer(["Word", "Vowels", "Position", "Letter", "OUTPUT"])
    word = inputs[0]
    t.at(1, f"Reads {fmt(word)} from the list of typed values.", Word=word)
    vowels = 0
    t.at(2, "Vowels starts at 0.", Vowels=0)
    n = len(word)
    for pos in range(1, n + 1):
        t.at(3, f"Position becomes {pos} (LENGTH(Word) is {n}).", Position=pos)
        letter = Ch(word[pos - 1])
        t.at(4, f"MID(Word, {pos}, 1) is {fmt(letter)}.", Letter=letter)
        hit = letter in "aeiou"
        t.at(5, f"Letter is {'a vowel, so the IF runs' if hit else 'not a vowel, so the IF is skipped'}.")
        if hit:
            vowels += 1
            t.at(6, f"Vowels becomes {vowels}.", Vowels=vowels)
        t.at(8, "NEXT Position goes back to the FOR line." if pos < n else "NEXT Position goes back to the FOR line, which finds Position past LENGTH(Word) and ends the loop.")
    t.at(9, "Outputs the result.", out=f"{word} has {vowels} vowels")
    return t, vowels


def vowels_direct(inputs):
    return sum(1 for c in inputs[0] if c in "aeiou")


PROGRAMS = {
    "total": ("Add up values until the sentinel 0 (a WHILE loop)", TOTAL_LINES, total_run, total_direct,
              [("Typed values 12, 30, 25, 0", [12, 30, 25, 0]), ("Typed value 0 only (the loop runs zero times)", [0])]),
    "grade": ("Grade a mark (a nested IF)", GRADE_LINES, grade_run, grade_direct,
              [("Mark 63", [63]), ("Mark 45", [45]), ("Mark 82", [82]), ("Mark 70 (on the boundary)", [70])]),
    "validate": ("Ask again until the age is valid (a REPEAT loop)", VALIDATE_LINES, validate_run, validate_direct,
                 [("Typed values 3, 25, 12", [3, 25, 12]), ("Typed value 18 (valid first time)", [18])]),
    "countdown": ("Count down in twos (a FOR loop with STEP -2)", COUNTDOWN_LINES, countdown_run, countdown_direct,
                  [("No input", [])]),
    "vowels": ("Count the vowels in a word (MID and LENGTH)", VOWELS_LINES, vowels_run, vowels_direct,
               [('Word "banana"', ["banana"]), ('Word "rhythm"', ["rhythm"]), ('Word "education"', ["education"])]),
}

out = {}
for name, (title, lines, run, direct, runs) in PROGRAMS.items():
    entries = []
    cols = None
    for label, inputs in runs:
        t, answer = run(inputs)
        expect = direct(inputs)
        if name == "countdown":
            got = [int(o) if o.isdigit() else o for o in t.outputs]
            assert got == expect, (name, got, expect)
        elif name == "total":
            assert answer == expect, (name, answer, expect)
            assert t.outputs == [f"Days: {expect[0]}", f"Total pages: {expect[1]}"]
        elif name == "vowels":
            assert answer == expect and t.outputs == [f"{inputs[0]} has {expect} vowels"]
        else:
            assert answer == expect, (name, answer, expect)
        for ev in t.events:
            assert 1 <= ev["line"] <= len(lines), (name, ev)
        r = t.result(label, inputs)
        r["inputs"] = [fmt(i) if isinstance(i, str) else str(i) for i in inputs]
        entries.append(r)
        cols = t.names
    out[name] = {"title": title, "lines": lines, "columns": cols, "runs": entries}

tpl = (ROOT / "data" / "cs-trace.tpl.js").read_text(encoding="utf-8")
assert "/*PROGRAMS*/null" in tpl
js = tpl.replace("/*PROGRAMS*/null", json.dumps(out, ensure_ascii=False, indent=None))
(ROOT / "widgets" / "cs-trace.js").write_text(js, encoding="utf-8")
(ROOT / "data" / "cs-trace.programs.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
print("ok", {k: [len(r["events"]) for r in v["runs"]] for k, v in out.items()})
