# checks/hist.interp.coldwar.2.py: recomputes every number in the chapter (intervals in the historiography, practice-extract lengths, widget items, mark totals, figure layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs

text = open(os.path.join(here, "..", "chapters", "hist.interp.coldwar.2.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# intervals in the historiography
eq("Williams to Alperovitz", 1965 - 1959, 6)
eq("Williams to Gaddis 1972", 1972 - 1959, 13)
eq("Gaddis 1972 to Leffler 1992", 1992 - 1972, 20)
eq("Gaddis 1972 to Gaddis 1997", 1997 - 1972, 25)
eq("Maddox after Alperovitz", 1973 - 1965, 8)
eq("Tocqueville prediction to 1945 (years)", 1945 - 1835, 110)
eq("Truman Vice-President days", (date(1945, 4, 12) - date(1945, 1, 20)).days, 82)
eq("Kolko Limits of Power: 1972, argument to 1954", 1954 - 1945, 9)
eq("CWIHP founded the year the USSR ended", 1991, 1991)
eq("Katyn admission to the Soviet Union's end (years)", 1991 - 1990, 1)
eq("Nazi-Soviet secret protocols voided, December 1989", date(1989, 12, 24).year, 1989)
# context figures used in answers (same as chapter 1)
between("Soviet armed forces cut (about three-quarters)", 1 - 2.8 / 11.3, 0.74, 0.76)
between("Marshall Plan per year", 13 / 4, 3.2, 3.3)

# practice extracts: word counts match their labels and are under the 600-word cap
def words(s):
    return len(re.findall(r"[A-Za-z’'-]+", s))


for k in "LNPQRS":
    m = re.search(r"\*\*Practice extract %s\*\* \(about (\d+) words\)\n\n(.*?)\n\n\*A summary" % k, text, re.S)
    assert m, f"extract {k} not found"
    n = words(m.group(2))
    between(f"extract {k} words", n, int(m.group(1)) - 25, int(m.group(1)) + 25)
    assert n < 600
m = re.search(r"\*\*Practice extract M\*\* \(about (\d+) words\)\n\n(.*?)\n\n\*A summary", text, re.S)
assert m, "extract M not found"
between("extract M words", words(m.group(2)), int(m.group(1)) - 25, int(m.group(1)) + 25)

# Paper 3 mark totals used in the worked answers
bands = {6: (18, 20), 5: (15, 17), 4: (12, 14), 3: (9, 11), 2: (5, 8), 1: (1, 4)}


def level(mk):
    for l, (lo, hi) in bands.items():
        if lo <= mk <= hi:
            return l


eq("L3 answer", (level(10), level(10), 10 + 10), (3, 3, 20))
eq("L5 answer", (level(16), level(16), 16 + 16), (5, 5, 32))
eq("L6 answer", (level(19), level(18), 19 + 18), (6, 6, 37))
eq("paper total", 20 + 20, 40)

# sort widget: 12 statements, four categories, three each
m = re.search(r'data-cats="([^"]*)" data-items="([^"]*)"', text)
cats = [c.strip() for c in m.group(1).split(",")]
items = [i for i in m.group(2).split(" ;; ") if i.strip()]
eq("statements", len(items), 12)
counts = {c: 0 for c in cats}
for it in items:
    f = [x.strip() for x in it.split(" | ")]
    eq("fields", len(f), 3)
    assert f[1] in cats, f"unknown category {f[1]}"
    counts[f[1]] += 1
eq("balanced categories", sorted(counts.values()), [3, 3, 3, 3])

# figure layout
eq("one svg", check_svgs(text), 1)
print("ok")
