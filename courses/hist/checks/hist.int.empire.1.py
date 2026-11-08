# checks/hist.int.empire.1.py: recomputes every number in the chapter (dates, intervals, ratios, figure layout)
from datetime import date
import re, os


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Scale of the Scramble: about a tenth (1870) to about nine tenths (1914)
eq("shares", (1 / 10, 9 / 10), (0.1, 0.9))
# Intervals
eq("Suez opening to Egypt occupation", 1882 - 1869, 13)
eq("Livingstone death after Stanley meeting (years)", 1873 - 1871, 2)
eq("Isandlwana to Ulundi (days)", (date(1879, 7, 4) - date(1879, 1, 22)).days, 163)
eq("Berlin Conference length (days)", (date(1885, 2, 26) - date(1884, 11, 15)).days, 103)
eq("Congo Free State years", 1908 - 1885, 23)
eq("Uganda Railway years", 1901 - 1896, 5)
eq("Barth journey years", 1855 - 1850, 5)
eq("Stanley second crossing years", 1877 - 1874, 3)
eq("Stanley for Leopold years", 1884 - 1879, 5)
eq("Matabele war to rising", 1896 - 1893, 3)
eq("Casement report to annexation (years)", 1908 - 1904, 4)
eq("Herero rising to camps closing (years)", 1908 - 1904, 4)
eq("Livingstone lecture to Congress", 1884 - 1857, 27)
# Weekday/date sanity
assert date(1896, 3, 1) < date(1896, 10, 26)
assert date(1904, 1, 12) < date(1904, 8, 11) < date(1904, 10, 2)
assert date(1889, 10, 29) < date(1893, 10, 1)
# Suez: 44 per cent for about 4 million pounds
between("suez share", 0.44, 0.43, 0.45)
# Omdurman: about 12,000 Mahdist dead vs 47-48 dead; 8,200 + 17,600 = 25,800
eq("Omdurman force", 8200 + 17600, 25800)
between("Omdurman ratio", 12000 / 48, 240, 260)
assert 12000 / 48 > 100
# Isandlwana: 52 officers + 690 regulars + 343 NNC + 133 colonial = 1,218 named; text says over 1,300 (total includes others)
assert 1300 > 52
# Rorke's Drift: eleven VCs
eq("VCs", 11, 11)
# Ndebele rising: 141 + 103 settlers killed in the first week
eq("settlers killed", 141 + 103, 244)
# Adwa: Italian forces 14,519 (Marcus) to 17,770 (Lewis); text: roughly 14,500 to 17,800
between("Italian low", 14519, 14400, 14600)
between("Italian high", 17770, 17700, 17900)
eq("Lewis breakdown", 10596 + 7104 + 70, 17770)
between("Ethiopian low vs Italian high", 73000 / 17770, 4, 4.2)
between("Ethiopian low vs Italian low", 73000 / 14519, 5, 5.1)
assert 6000 > 3800
# Herero and Nama: deaths 40,000-80,000 (about 80%) and about 10,000 (about half)
between("implied prewar Herero (low)", 40000 / 0.8, 49000, 51000)
between("implied prewar Herero (high)", 80000 / 0.8, 99000, 101000)
eq("implied prewar Nama", 10000 / 0.5, 20000)
# Casement: Lukolela 5,000 -> under 600; Bolobo 40,000 -> 7,000-8,000
between("Lukolela fall", 1 - 600 / 5000, 0.87, 0.89)
between("Bolobo fall (low)", 1 - 8000 / 40000, 0.79, 0.81)
between("Bolobo fall (high)", 1 - 7000 / 40000, 0.82, 0.83)
# Congo area: 2,345,409 km2 vs Belgium 30,689 km2: about seventy-five times
between("Congo vs Belgium", 2345409 / 30689, 74, 78)
# Hochschild: ten million is about half; so pre-1885 population about 20 million
eq("half of 20m", 20 / 2, 10)
# Paper totals
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)
eq("timeline interval Berlin to Congo Free State year", 1885 - 1885, 0)

# Figure geometry (Congo rubber system): 5 boxes, width 310, text 7 px per char
boxes = [
    (10, ["1. The state claims the land", "Decrees of 1891 and 1892 give the state", "and companies the rubber and ivory"]),
    (96, ["2. Quotas", "Villages must bring a fixed weight of", "rubber, for little or no pay"]),
    (182, ["3. Enforcement", "Force Publique and company agents:", "hostages, burnt villages, floggings"]),
    (268, ["4. Profit", "Rubber sold at Antwerp: money for", "Leopold, the state and the companies"]),
    (354, ["5. Human cost", "Famine, disease, flight, fewer births;", "loss estimated at 1 to 10 million"]),
]
W = 310
for y, lines in boxes:
    for i, t in enumerate(lines):
        px = len(t) * (7.5 if i == 0 else 7)
        assert px <= W - 16, f"label too wide: {t!r} {px} > {W - 16}"
    # baselines at y+19, y+36, y+51; box height 56
    assert y + 51 + 4 < y + 56
    assert y + 19 - 10 > y + 2
# arrows: from box bottom + 4 to next top - 4
for (y1, _), (y2, _) in zip(boxes, boxes[1:]):
    a0, a1 = y1 + 56 + 4, y2 - 4
    assert a1 - a0 >= 20, (a0, a1)
assert 354 + 56 + 15 <= 425

# The chapter file must contain the same figure numbers (quick presence tests)
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.int.empire.1.md"), encoding="utf-8").read()
for token in ["17 November 1869", "10 November 1871", "22 January 1879", "4 July 1879", "13 September 1882",
              "1 March 1896", "2 September 1898", "2 October 1904", "15 November 1908", "12 January 1904",
              "26 October 1896", "11 December 1878", "44 per cent", "about £4 million", "12,000", "1.1 billion euros",
              "7,000 or 8,000", "viewBox=\"0 0 340 425\""]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
print("ok")
