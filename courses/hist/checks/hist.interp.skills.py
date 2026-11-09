# checks/hist.interp.skills.py: recomputes every number in the chapter (mark totals, level bands, extract lengths, dates, figure layout)
import os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs

text = open(os.path.join(here, "..", "chapters", "hist.interp.skills.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Paper 3: Table A (AO4) 20 + Table B (AO1) 20 = 40; 1 h 15 min = 75 minutes
eq("paper total", 20 + 20, 40)
eq("paper minutes", 1 * 60 + 15, 75)
# half the marks per AO
eq("AO1 share", 20 / 40, 0.5)
# level bands (identical in both tables) and summed totals
bands = {6: (18, 20), 5: (15, 17), 4: (12, 14), 3: (9, 11), 2: (5, 8), 1: (1, 4)}
eq("level 6 total", (bands[6][0] * 2, bands[6][1] * 2), (36, 40))
eq("level 5 total", (bands[5][0] * 2, bands[5][1] * 2), (30, 34))
# model answers: totals and their levels
def level(m):
    for l, (lo, hi) in bands.items():
        if lo <= m <= hi:
            return l
    return 0
eq("L3 answer A", level(10), 3); eq("L3 answer B", level(10), 3); eq("L3 total", 10 + 10, 20)
eq("L5 answer A", level(16), 5); eq("L5 answer B", level(16), 5); eq("L5 total", 16 + 16, 32)
eq("L6 answer A", level(19), 6); eq("L6 answer B", level(18), 6); eq("L6 total", 19 + 18, 37)
# time plan: 10-12 minutes reading and 55 writing leaves a few minutes
between("spare minutes", 75 - 12 - 55, 3, 12)
between("spare minutes (short plan)", 75 - 10 - 55, 3, 12)

# practice extracts: word counts match their labels, all under the 600-word cap
def words(s):
    return len(re.findall(r"[A-Za-z’'-]+", s))
m = re.search(r"\*\*Practice extract C\*\* \(about (\d+) words\)\n\n(.*?)\n\n\*A summary", text, re.S)
n_c = words(m.group(2)); between("extract C words", n_c, int(m.group(1)) - 30, int(m.group(1)) + 30); assert n_c < 600
for k in "123":
    m = re.search(r"\*\*Practice extract %s\*\* \(about (\d+) words\)\n\n(.*?)\n\n\*A summary" % k, text, re.S)
    n = words(m.group(2)); between(f"extract {k} words", n, int(m.group(1)) - 25, int(m.group(1)) + 25); assert n < 600

# dates and ages used in the text
eq("Carr to Elton", 1967 - 1961, 6)
eq("Lefebvre to Cobban", 1964 - 1939, 25)
eq("Cobban to Furet", 1978 - 1964, 14)
eq("Ségur Ordinance", (1781, 5, 22), (1781, 5, 22))
eq("August Decrees span", 11 - 4, 7)
# 1788 budget used in the answers to exam practice
spend, revenue, interest = 629, 503, 318
eq("deficit 1788", spend - revenue, 126)
between("bread sous", 14.5 / 8, 1.7, 2.0)

# figure layout
eq("one svg", check_svgs(text), 1)
# widget: items parse into 10 statements with valid categories
w = re.search(r'data-cats="([^"]*)" data-items="([^"]*)"', text)
cats = [c.strip() for c in w.group(1).split(",")]
items = [i for i in w.group(2).split(" ;; ") if i.strip()]
eq("statements", len(items), 10)
for it in items:
    f = [x.strip() for x in it.split(" | ")]
    eq("fields", len(f), 3)
    assert f[1] in cats, f"unknown category {f[1]}"
print("ok")
