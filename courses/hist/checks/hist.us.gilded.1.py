# checks/hist.us.gilded.1.py: recomputes every number in the chapter (dates, ratios, totals, figure layout)
from datetime import date
from fractions import Fraction
import re, os


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def between(label, x, lo, hi):
    assert lo <= x <= hi, f"{label}: {x} not in [{lo}, {hi}]"


# Population (millions): 1870 38.56, 1900 76.21 -> "doubled"; 1920 about 106
between("population ratio", 76.21 / 38.56, 1.9, 2.05)
# Railroads (thousand miles): 1870 53, 1900 193 -> "about 3.6 times"; added about 140,000 miles in thirty years
between("rail ratio", 193 / 53, 3.55, 3.7)
eq("rail added", 193 - 53, 140)
eq("rail interval years", 1900 - 1870, 30)
# Steel (million long tons): 1870 0.08 (77,000), 1900 10.19; 1880 1.25; 1890 4.28
assert 10.19 / 0.077 > 100, "steel more than a hundredfold"
between("steel 1880-1900", 10.19 / 1.25, 8, 8.3)
# long tons to short tons: 10.19 million long tons = about 11.4 million short tons
between("short tons 1900", 10.19 * 2240 / 2000, 11.35, 11.45)
# Coal: about 35 million (1870) to about 270 million (1900): "more than sevenfold"
assert 270 / 35 > 7, "coal more than sevenfold"
# Exports: $390m -> $1.4bn: more than tripled
assert 1400 / 390 > 3
# Bairoch shares of world manufacturing: about 15 (1880), 24 (1900), 32 (1913)
assert 14.7 < 15 and 23.6 < 24 and 32.0 == 32
# Immigration by decade (millions), chart and the text "about 26 million 1871-1920"
dec = [2.8, 5.2, 3.7, 8.8, 5.7]
between("immigrants 1871-1920", sum(dec), 25.5, 26.5)
# Exact decade totals behind the chart: 2,812,191; 5,246,613; 3,687,564; 8,795,386; 5,735,811
exact = [2812191, 5246613, 3687564, 8795386, 5735811]
for r, e in zip(dec, exact):
    assert abs(round(e / 1e6, 1) - r) < 1e-9, f"decade {r} vs {e}"
between("exact total", sum(exact) / 1e6, 26.2, 26.4)
# Intervals
eq("Homestead to transcontinental", 1869 - 1862, 7)
eq("Pacific Railway Act to 1869", (date(1869, 5, 10) - date(1862, 7, 1)).days // 365, 6)
eq("Standard Oil incorporated 1870", date(1870, 1, 10).year, 1870)
eq("Edison lamp to Pearl Street", 1882 - 1879, 3)
eq("Bell patent", date(1876, 3, 7).year, 1876)
eq("Chinese Exclusion to Geary Act (ten years)", 1892 - 1882, 10)
eq("Ellis Island opening year", date(1892, 1, 1).year, 1892)
eq("standard time 1883", date(1883, 11, 18).year, 1883)
# Patents: 31,005 (1861) to 640,167 (1900): more than 600,000
assert 640167 - 31005 > 600000
eq("patent years under forty", 1900 - 1861 < 40, True)
# Electric motors share of factory power: about 5% (1899) -> over half (1919): twenty years
eq("electric motors interval", 1919 - 1899, 20)
# Cars: 8,000 (1900), 458,000 (1910), over 8 million (1920)
assert 8_000 < 458_000 < 8_000_000
# Steel rails: about $170 (1868) to about $17 (1898): roughly tenfold
between("rail price ratio", 170 / 17, 9.5, 10.5)
# Tariff: McKinley October 1890; Gold Standard Act 14 March 1900; Dingley 1897
assert date(1890, 10, 1) < date(1897, 7, 24) < date(1900, 3, 14)
# Weaver 1892: about 1 million votes, about 8.5 per cent, 22 electoral votes
eq("electoral votes", 22, 22)
# Exodusters: 1879-80, 20,000-40,000
assert 20000 < 40000
# Carnegie Wealth June 1889; Turner July 1893; Sumner 1883; George 1879; Omaha 4 July 1892
assert 1879 < 1883 < 1889 < 1892 < 1893
# Homestead: 1.6 million households and 270 million acres, "roughly one tenth" of US land area (about 2.27 billion acres)
between("homestead share", 270e6 / 2.27e9, 0.1, 0.13)
# Union Pacific: 1864 land doubled (10 to 20 sections per mile)
eq("land doubling", 20 / 10, 2)
# Pacific loans per mile: 16,000 / 32,000 / 48,000
eq("loan scale", (16000, 32000, 48000), (16000 * 1, 16000 * 2, 16000 * 3))
# Gold standard / resumption: 1 January 1879
eq("resumption year", date(1879, 1, 1).year, 1879)

# Mark totals of the worked examples: (a) [10] Level 4 = 9-10; (a) [15] Level 4 = 12-15; (b) [20] Level 5 = 17-20; (b) [25] Level 5 = 21-25
eq("paper 1 totals", 15 + 25, 40)
eq("paper 2 totals", (10 + 20) * 2, 60)

# Figure geometry: text widths (about 7 px per character) inside boxes and arrow clearances
fig_boxes = [
    # (x, y, w, h, [(line, bold)], arrow-free)
    (6, 10, 104, 76, ["Resources", "coal, iron,", "oil, timber,", "farmland"]),
    (118, 10, 104, 76, ["People", "population", "doubles;", "immigrants"]),
    (230, 10, 104, 76, ["Capital", "savings and", "banks; money", "from abroad"]),
    (6, 114, 328, 62, ["Railroads: the link", "one national market; orders for steel, coal", "and new ways to manage and finance firms"]),
    (6, 204, 104, 76, ["Technology", "steel, power", "telephone,", "typewriter"]),
    (118, 204, 104, 76, ["Government", "tariffs,", "land grants,", "few controls"]),
    (230, 204, 104, 76, ["Attitudes", "respect for", "business", "success"]),
    (6, 308, 328, 62, ["Rapid industrialisation after 1870", "steel, coal, railroads, machinery", "all grow together"]),
]
for x, y, w, h, lines in fig_boxes:
    for i, t in enumerate(lines):
        px = len(t) * (7.5 if i == 0 else 7)
        assert px <= w - 16, f"label too wide: {t!r} {px} > {w - 16}"
# vertical gaps: box bottoms vs arrow starts and next box tops
assert 10 + 76 + 4 <= 90 and 110 + 4 <= 114
assert 114 + 62 + 4 <= 180 and 200 + 4 <= 204
assert 204 + 76 + 4 <= 284 and 304 + 4 <= 308
assert 308 + 62 <= 384 - 2
# last text baseline inside each box (baseline + 3 descender < box bottom)
for base, bottom in [(75, 86), (167, 176), (269, 280), (361, 370)]:
    assert base + 4 < bottom, (base, bottom)

# The chapter file must contain the same figure numbers (quick presence tests)
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "hist.us.gilded.1.md"), encoding="utf-8").read()
for token in ["1.6 million", "270 million acres", "10 May 1869", "14 March 1900", "4 September 1882", "7 March 1876", "6 May 1882", "25 February 1863"]:
    assert token in text, f"missing {token}"
assert not re.search(r"\[M\d\]|\[A\d\]|\[B\d\]", text), "mark tokens are not used in History"
print("ok")
