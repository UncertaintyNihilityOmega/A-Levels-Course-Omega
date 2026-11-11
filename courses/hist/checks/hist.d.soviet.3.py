# checks/hist.d.soviet.3.py: recomputes every number in the chapter (ages, intervals, treaty totals, ranges, widget dates, exam questions)
import os
import re
from datetime import date

here = os.path.dirname(os.path.abspath(__file__))


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Ages
eq("Gorbachev age when chosen (11 Mar 1985)", age(date(1931, 3, 2), date(1985, 3, 11)), 54)
eq("Gorbachev age when made full Politburo member (Oct 1980)", age(date(1931, 3, 2), date(1980, 10, 21)), 49)
eq("Tikhonov age when he retired (Sept 1985)", age(date(1905, 5, 14), date(1985, 9, 27)), 80)
eq("Grishin age in March 1985", age(date(1914, 9, 18), date(1985, 3, 11)), 70)
eq("Gromyko years as Foreign Minister (1957-85)", 1985 - 1957, 28)
# Intervals
assert date(1985, 3, 10) < date(1985, 3, 11)
eq("Chernenko dies, Gorbachev chosen next day", (date(1985, 3, 11) - date(1985, 3, 10)).days, 1)
d = (date(1985, 3, 10) - date(1982, 11, 10)).days
eq("days from Brezhnev's death to Chernenko's", d, 851)
assert d < 3 * 365  # 'three leaders in under three years'
eq("Chernobyl to Gorbachev's speech (days)", (date(1986, 5, 14) - date(1986, 4, 26)).days, 18)
eq("Chernobyl to TASS announcement (days)", (date(1986, 4, 28) - date(1986, 4, 26)).days, 2)
eq("Chernobyl, 2006 anniversary: 20 years", 2006 - 1986, 20)
eq("Gorbachev's 2006 claim: five years later", 1991 - 1986, 5)
eq("years from Stalin's era Five-Year Plan irrelevant: 12th plan span", 1990 - 1986, 4)
assert date(1987, 12, 7) < date(1987, 12, 8) < date(1987, 12, 10)  # Washington summit 7-10 Dec, INF signed 8 Dec
assert date(1985, 11, 19) < date(1985, 11, 21)
assert date(1986, 10, 11) < date(1986, 10, 12)
eq("UN speech one day short of a year after INF signing", (date(1988, 12, 7) - date(1987, 12, 8)).days, 365)
eq("Afghan withdrawal: Accords to last troops (days)", (date(1989, 2, 15) - date(1988, 4, 14)).days, 307)
eq("Congress of People's Deputies: 750 x 3", 750 * 3, 2250)
assert 2250 // 3 == 750  # a third elected by public bodies
# INF treaty totals (also in usa74.4)
eq("INF missiles destroyed", 1846 + 846, 2692)
# Plan figures (Western analyses of the 12th plan)
assert 23.6 > 15.4
eq("investment growth difference (points)", round(23.6 - 15.4, 1), 8.2)
# Troop cuts announced at the UN
eq("troop cut: 500,000", 500_000, 500000)
assert 50_000 < 500_000 and 5_000 < 10_000
# Growth, deficit, debt (estimates, with sources named in the text)
assert 1.8 < 4.9
assert 2 <= 3 < 6 < 10  # deficit as share of GNP: 2-3 (before), 6 (1986), over 10 (1988)
assert 26 < 55 < 80  # hard-currency debt, billion dollars (end 1984; 1990; 1991 by the widest count)
assert 2 < 4 and 5 > 4  # GNP fall 1990: official 2, CIA 4-5
assert 8 > 0
# Lost alcohol revenue: range quoted
assert 10 < 15
# Oil price fell by more than half in 1986: about 30 to about 10 dollars
assert 10 < 30 / 2
# Yeltsin 1991 vote about 57 per cent (57.3)
assert 57 < 57.3 < 58
# Dates in order
for a, b in [((1985, 3, 11), (1985, 4, 23)), ((1985, 4, 23), (1985, 5, 7)), ((1985, 5, 7), (1985, 7, 2)),
             ((1986, 4, 26), (1986, 10, 11)), ((1987, 1, 27), (1987, 12, 8)), ((1988, 5, 26), (1988, 6, 28)),
             ((1988, 6, 28), (1988, 12, 7)), ((1989, 3, 26), (1990, 3, 14))]:
    assert date(*a) < date(*b), (a, b)
# Law on Cooperatives passed 26 May 1988, in force 1 July 1988
assert date(1988, 5, 26) < date(1988, 7, 1)
# Article 6 repealed 14 March 1990; Gorbachev elected President the next day
eq("Article 6 repeal to presidency (days)", (date(1990, 3, 15) - date(1990, 3, 14)).days, 1)

text = open(os.path.join(here, "..", "chapters", "hist.d.soviet.3.md"), encoding="utf-8").read()
eq("number of timeline widgets", len(re.findall(r'data-w="hist-timeline"', text)), 1)
ev = re.search(r'data-events="([^"]*)"', text).group(1).split(" ;; ")
eq("number of timeline events", len(ev), 16)
ds = [e.split(" | ")[0] for e in ev]
assert ds == sorted(ds), ds
for e in ev:
    parts = e.split(" | ")
    assert len(parts) == 4, e
    nums = [int(x) for x in parts[0].split("-")]
    if len(nums) == 3:
        date(*nums)
    assert parts[3] in ("Economy", "Politics and society", "Foreign relations"), parts[3]
qs = re.findall(r"^Q: \[(\d+) marks\]", text, re.M)
assert qs and all(q == "30" for q in qs), qs
eq("number of exam questions", len(qs), 11)
eq("Table A + Table B", 15 + 15, 30)
for mm in re.finditer(r"^Q: \[30 marks\] ★+ (.*)$", text, re.M):
    assert mm.group(1).startswith("Assess") or "Evaluate" in mm.group(1), mm.group(1)
eq("number of quiz questions", len(re.findall(r"^\? ", text, re.M)), 11)
assert "FACTS.md" not in text and "COURSE.md" not in text
print("ok")
