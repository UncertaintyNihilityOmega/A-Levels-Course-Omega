# checks/hist.interp.ww1.2.py: recomputes every number in the chapter (date arithmetic, practice-extract lengths, widget items, mark totals, figure layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs

text = open(os.path.join(here, "..", "chapters", "hist.interp.ww1.2.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# intervals in the historiography
eq("Taylor eight years after Fischer", 1969 - 1961, 8)
eq("Versailles to Fay", 1928 - 1919, 9)
eq("Fischer article to book", 1961 - 1959, 2)
eq("centenary", 2014 - 1914, 100)
eq("Fischer age at publication of Griff", 1961 - 1908, 53)
eq("Ritter lifespan", 1967 - 1888, 79)
eq("Joll lecture to book", 1984 - 1968, 16)
eq("Joll lecture weekday (25 April 1968 was a Thursday)", date(1968, 4, 25).weekday(), 3)
eq("Mainz agreement years after 1945", 1951 - 1945, 6)
eq("Historikertag years after Griff", 1964 - 1961, 3)
eq("Erdmann edition years after Fischer's book", 1972 - 1961, 11)
eq("Afflerbach and Stevenson conference to book", 2007 - 2004, 3)
eq("Lloyd George War Memoirs span", 1936 - 1933, 3)
# Reichstag, January 1912: SPD 110 seats of 397, 34.8 per cent of the vote: largest party
between("SPD seat share", 110 / 397, 0.27, 0.28)
# Balkan, July: 1914 dates used in worked answers
eq("blank cheque to Marne programme (days)", (date(1914, 9, 9) - date(1914, 7, 5)).days, 66)
eq("1912 council to July 1914 (years)", 1914 - 1912, 2)
# Russia's Great Programme completion about 1917: three to four years after 1913
eq("programme horizon", 1917 - 1913, 4)

# practice extracts: word counts match their labels and are under the 600-word cap
def words(s):
    return len(re.findall(r"[A-Za-z’'-]+", s))
for k in "FGHJK":
    m = re.search(r"\*\*Practice extract %s\*\* \(about (\d+) words\)\n\n(.*?)\n\n\*A summary" % k, text, re.S)
    assert m, f"extract {k} not found"
    n = words(m.group(2))
    between(f"extract {k} words", n, int(m.group(1)) - 25, int(m.group(1)) + 25)
    assert n < 600

# Paper 3 mark totals used in the worked answers
bands = {6: (18, 20), 5: (15, 17), 4: (12, 14), 3: (9, 11), 2: (5, 8), 1: (1, 4)}
def level(m):
    for l, (lo, hi) in bands.items():
        if lo <= m <= hi:
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
