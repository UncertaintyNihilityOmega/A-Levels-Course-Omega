# checks/hist.interp.holocaust.2.py: recomputes every number in the chapter (intervals in the debate, practice-extract lengths, widget items, figure layout)
import os, re, sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs

text = open(os.path.join(here, "..", "chapters", "hist.interp.holocaust.2.md"), encoding="utf-8").read()


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# intervals in the historiography
eq("Hilberg to Eichmann trial (same year)", 1961 - 1961, 0)
eq("Hilberg 1961 to Arendt 1963", 1963 - 1961, 2)
eq("Jackel Weltanschauung to Dawidowicz", 1975 - 1969, 6)
eq("Broszat article to Mason labels", 1981 - 1977, 4)
eq("Schleunes to Browning Fateful Months", 1985 - 1970, 15)
eq("Browning Ordinary Men to Goldhagen", 1996 - 1992, 4)
eq("Goldhagen to Gross Neighbors", 2001 - 1996, 5)
eq("Browning Origins years after Ordinary Men", 2004 - 1992, 12)
eq("Longerich German original 1998 to English 2010", 2010 - 1998, 12)
eq("Friedlander volumes interval", 2007 - 1997, 10)
eq("Hitler 1919 letter to 1941: years Intentionalists must explain", 1941 - 1919, 22)
eq("Hitler's prophecy to 12 December 1941 (years)", 1941 - 1939, 2)
eq("Willikens speech to Kershaw essay (years)", 1993 - 1934, 59)
eq("Hitler Hubris to Nemesis", 2000 - 1998, 2)
eq("Dawidowicz 1975 to Wyman 1984", 1984 - 1975, 9)
eq("Wasserstein 1979 to Wyman 1984", 1984 - 1979, 5)
eq("Wyman to Rubinstein", 1997 - 1984, 13)
eq("Gerlach 12 December 1941 to Wannsee (days)", (date(1942, 1, 20) - date(1941, 12, 12)).days, 39)
eq("Chelmno to Wannsee (days)", (date(1942, 1, 20) - date(1941, 12, 8)).days, 43)
eq("Jozefow date weekday (13 July 1942 was a Monday)", date(1942, 7, 13).weekday(), 0)
eq("Jedwabne weekday (10 July 1941 was a Thursday)", date(1941, 7, 10).weekday(), 3)
eq("Warsaw uprising start to Sobibor revolt (days)", (date(1943, 10, 14) - date(1943, 4, 19)).days, 178)
eq("Czerniakow suicide day after deportations began", (date(1942, 7, 23) - date(1942, 7, 22)).days, 1)
eq("Auschwitz bomb request refusal to Monowitz raid (days)", (date(1944, 8, 20) - date(1944, 7, 4)).days, 47)
eq("Hamburg Wehrmacht exhibition 1995 to 1999 (years)", 1999 - 1995, 4)
eq("Eichmann trial year to hanging year", 1962 - 1961, 1)

# numbers used in text
eq("Battalion 101 shot and deported", 38000 + 45000, 83000)
between("Jozefow dozen of 500", 12 / 500, 0.02, 0.03)
between("Gross 1,600 against IPN 340", 340 / 1600, 0.21, 0.22)
between("Romanian commission range", 380000 - 280000, 100000, 100000)
eq("Jager report figure", 137346, 137346)
eq("Warsaw ration", 181, 181)
between("polls: six million of 9.5 million", 6 / 9.5, 0.6, 0.66)

for needle in ["1,500", "38,000", "45,000", "340", "1,600", "137,346", "280,000", "380,000", "181 calories",
               "13 July 1942", "10 July 1941", "12 December 1941", "31 July 1941", "23 October", "8 December 1941"]:
    assert needle in text, f"missing figure in chapter: {needle}"

# practice extract lengths (stated as "about N words")
def words(s):
    return len(re.findall(r"[A-Za-zÀ-ÿ'’\-]+", s))

for letter, stated in [("L", 190), ("M", 150), ("N", 150), ("P", 160), ("Q", 150), ("R", 150), ("S", 150), ("T", 170)]:
    m = re.search(r"\*\*Practice extract " + letter + r"\*\* \(about (\d+) words\)\s*\n\s*\n(.+?)\n\s*\n\*A summary", text, re.S)
    assert m, f"extract {letter} not found"
    assert int(m.group(1)) == stated, f"extract {letter} stated length {m.group(1)}"
    n = words(m.group(2))
    between(f"extract {letter} actual words vs stated {stated}", n, stated * 0.8, stated * 1.2)

# widgets
m = re.search(r'data-w="hist-sort"[^>]*data-cats="([^"]+)"[^>]*data-items="([^"]+)"', text)
assert m, "sort widget missing"
cats = m.group(1).split(",")
items = [i.strip().split(" | ") for i in m.group(2).split(" ;; ")]
eq("sort categories", cats, ["Intentionalist", "Structuralist", "Functionalist", "Synthesis"])
for it in items:
    assert len(it) == 3 and it[1] in cats, it
eq("sort items", len(items), 12)
for c in cats:
    eq("items per category " + c, sum(1 for it in items if it[1] == c), 3)

# figure layout
eq("svg figures checked", check_svgs(text), 1)

print("ok")
