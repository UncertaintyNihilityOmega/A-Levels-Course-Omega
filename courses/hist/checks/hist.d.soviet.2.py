# checks/hist.d.soviet.2.py: recomputes every number in the chapter (ages, intervals, growth ratios, ranges, figure layout)
import os
import re
import sys
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "data"))
from p17_svg import check_svgs


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Leaders: birth and death dates -> ages in the chapter
eq("Brezhnev age at death", age(date(1906, 12, 19), date(1982, 11, 10)), 75)
eq("Kosygin age at death", age(date(1904, 2, 21), date(1980, 12, 18)), 76)
eq("Suslov age at death", age(date(1902, 11, 21), date(1982, 1, 25)), 79)
eq("Ustinov age at death", age(date(1908, 10, 30), date(1984, 12, 20)), 76)
eq("Tikhonov age when head of government (Oct 1980)", age(date(1905, 5, 14), date(1980, 10, 23)), 75)
eq("Andropov age at death", age(date(1914, 6, 15), date(1984, 2, 9)), 69)
eq("Chernenko age when chosen", age(date(1911, 9, 24), date(1984, 2, 13)), 72)
eq("Chernenko age at death", age(date(1911, 9, 24), date(1985, 3, 10)), 73)
eq("Gorbachev age when chosen", age(date(1931, 3, 2), date(1985, 3, 11)), 54)
eq("Khrushchev age when removed", age(date(1894, 4, 15), date(1964, 10, 14)), 70)
# Spans
eq("years Brezhnev led (Oct 1964 to Nov 1982)", age(date(1964, 10, 14), date(1982, 11, 10)), 18)
eq("Andropov in office: whole months (12 Nov 1982 to 9 Feb 1984)", (1984 - 1982) * 12 + (2 - 11) - (9 < 12), 14)
assert (date(1984, 2, 9) - date(1982, 11, 12)).days > 14 * 30 + 20  # 14 months and 28 days: 'fifteen months'
eq("days from Brezhnev's death to Chernenko's death", (date(1985, 3, 10) - date(1982, 11, 10)).days, 851)
assert 851 < 2.5 * 365.25  # 'under two and a half years'
eq("Gorbachev chosen the day after Chernenko died", (date(1985, 3, 11) - date(1985, 3, 10)).days, 1)
eq("Andropov elected two days after Brezhnev died", (date(1982, 11, 12) - date(1982, 11, 10)).days, 2)
eq("leaders lost 1980-85", len(["Kosygin", "Suslov", "Brezhnev", "Andropov", "Ustinov", "Chernenko"]), 6)
# Sputnik 1957 and Gagarin 1961 against 1964
eq("Sputnik years before 1964", 1964 - 1957, 7)
eq("Gagarin years before 1964", 1964 - 1961, 3)
# Growth: Western estimates (Encyclopedia of Russian History table; Ofer 1987 etc.)
g = {"1960-70": 4.9, "1970-80": 2.5, "1980-85": 1.8}
assert 0.5 < g["1970-80"] / g["1960-70"] < 0.53  # 'about half'
assert g["1980-85"] < 2 < g["1970-80"]
tfp = {"1970-80": -1.2, "1980-85": -1.0}
assert all(v < 0 for v in tfp.values())
# Defence burden: 9 (official 1989) to 15-17 (CIA/DIA 1989)
lo, hi = 9, 17
assert lo < 15 < hi
# Afghanistan
eq("war length in months (Dec 1979 to Feb 1989)", (1989 - 1979) * 12 + (2 - 12), 110)
eq("war length years", 110 // 12, 9)
eq("remaining months", 110 % 12, 2)
assert date(1979, 12, 12) < date(1979, 12, 24) < date(1979, 12, 27) < date(1989, 2, 15)
eq("days from the decision (12 Dec) to the storming of the palace (27 Dec)", (date(1979, 12, 27) - date(1979, 12, 12)).days, 15)
eq("Soviet dead rounded to the nearest 500", round(14453 / 500) * 500, 14500)
# Pope: elected 16 Oct 1978, visit 2-10 June 1979 = nine days; strikes in August 1980
eq("visit length (days inclusive)", (date(1979, 6, 10) - date(1979, 6, 2)).days + 1, 9)
eq("visit to strikes (months, June 1979 to Aug 1980)", (1980 - 1979) * 12 + (8 - 6), 14)
eq("1523 to 1978 (years since the last non-Italian pope)", 1978 - 1523, 455)
# Charter 77 and KOR
assert date(1976, 9, 23) < date(1977, 1, 6)
assert 242 < 1900
# Poland: 1970 price rises 12 Dec, Gomulka falls 20 Dec = 8 days
eq("days from price rises to Gomulka's fall", (date(1970, 12, 20) - date(1970, 12, 12)).days, 8)
assert date(1971, 5, 3) < date(1972, 5, 26) < date(1975, 8, 1)
eq("years from SALT I to the invasion of Afghanistan", 1979 - 1972, 7)
eq("years from Helsinki to the invasion", 1979 - 1975, 4)
eq("Kosygin reform 1965 to Prague 1968 (years)", 1968 - 1965, 3)
eq("10th plan calendar years", len(range(1976, 1981)), 5)
eq("Rashidov's years as Uzbek leader", 1983 - 1959, 24)
eq("SS-20 deployment to NATO decision (years)", 1979 - 1977, 2)
assert date(1983, 3, 8) < date(1983, 3, 23) < date(1983, 9, 1) < date(1983, 11, 23)

text = open(os.path.join(here, "..", "chapters", "hist.d.soviet.2.md"), encoding="utf-8").read()
eq("number of SVG figures", check_svgs(text), 1)
eq("number of timeline widgets", len(re.findall(r'data-w="hist-timeline"', text)), 1)
eq("number of chart widgets", len(re.findall(r'data-w="hist-chart"', text)), 1)
m = re.search(r'data-w="hist-chart".*?data-series="([^"]*)"', text)
vals = [float(x) for x in re.findall(r"=([\d.]+)", m.group(1))]
eq("chart values", vals, [4.9, 2.5, 1.8])
ev = re.search(r'data-events="([^"]*)"', text).group(1).split(" ;; ")
ds = [e.split(" | ")[0] for e in ev]
assert ds == sorted(ds), ds
for d in ds:
    parts = [int(x) for x in d.split("-")]
    if len(parts) == 3:
        date(*parts)
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 10)
eq("Table A + Table B", 15 + 15, 30)
for mm in re.finditer(r"^Q: \[30 marks\] ★+ (.*)$", text, re.M):
    assert mm.group(1).startswith("Assess") or "Evaluate" in mm.group(1), mm.group(1)
print("ok")
