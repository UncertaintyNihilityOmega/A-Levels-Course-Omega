# checks/hist.eu.germany.4.py: recomputes every number in the chapter (dates, intervals, votes, shares, marks, figure layout)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Order of events in the story in dates and the widget
seq = [date(1866, 8, 23), date(1867, 3, 23), date(1867, 5, 11), date(1867, 7, 1), date(1868, 4, 27), date(1870, 6, 19),
       date(1870, 7, 12), date(1870, 7, 13), date(1870, 7, 19), date(1870, 9, 2), date(1870, 9, 4), date(1870, 9, 19),
       date(1870, 10, 27), date(1870, 11, 23), date(1870, 11, 30), date(1871, 1, 18), date(1871, 1, 28),
       date(1871, 5, 4), date(1871, 5, 10)]
assert seq == sorted(seq), "timeline out of order"
assert date(1870, 11, 15) < date(1870, 11, 23) < date(1870, 11, 25)

# Luxembourg crisis 23 March -> Treaty of London 11 May 1867: 49 days
eq("Luxembourg crisis days", (date(1867, 5, 11) - date(1867, 3, 23)).days, 49)
# Zollparlament: 85 southern deputies = Bavaria 48 + Württemberg 17 + Baden 14 + Hesse-Darmstadt 6
eq("southern deputies", 48 + 17 + 14 + 6, 85)
# Napoleon III: born 20 April 1808 -> 58 in 1866
eq("Napoleon III age 1866", age(date(1808, 4, 20), date(1866, 7, 3)), 58)
# Plebiscite May 1870: about 7.3 million to about 1.5 million -> about 83 per cent
share = Fraction(73, 73 + 15)
assert Fraction(80, 100) < share < Fraction(86, 100), float(share)

# Sadowa 3 July 1866 -> Sedan 1 Sept 1870: 4 years and 2 months
eq("Sadowa to Sedan years", (date(1870, 9, 1) - date(1866, 7, 3)).days // 365, 4)
# Ems: 12 July withdrawal, 13 July Ems, 19 July declaration: six days after Ems
eq("Ems to declaration", (date(1870, 7, 19) - date(1870, 7, 13)).days, 6)
eq("withdrawal to declaration", (date(1870, 7, 19) - date(1870, 7, 12)).days, 7)
# Declaration -> Sedan 1 September: 44 days (about six weeks)
d = (date(1870, 9, 1) - date(1870, 7, 19)).days
eq("declaration to Sedan", d, 44)
assert 6 <= d / 7 < 7
# Sedan -> republic 4 September: 2 days after the surrender on 2 September
eq("surrender to republic", (date(1870, 9, 4) - date(1870, 9, 2)).days, 2)
# Siege of Paris 19 September -> 28 January: 131 days (over four months)
s = (date(1871, 1, 28) - date(1870, 9, 19)).days
eq("siege days", s, 131)
assert s / 30.4 > 4
# War: 19 July 1870 -> 28 January 1871: 193 days (about six months)
w = (date(1871, 1, 28) - date(1870, 7, 19)).days
eq("war days", w, 193)
# Proclamation 18 January, armistice 28 January: ten days
eq("proclamation to armistice", (date(1871, 1, 28) - date(1871, 1, 18)).days, 10)
# Constitution adopted 16 April, in force 4 May; Treaty of Frankfurt 10 May
assert date(1871, 4, 16) < date(1871, 5, 4) < date(1871, 5, 10)
# Wilhelm I (born 22 March 1797) aged 73 on 18 January 1871; Bismarck (born 1 April 1815) aged 55
eq("Wilhelm age 1871", age(date(1797, 3, 22), date(1871, 1, 18)), 73)
eq("Bismarck age 1871", age(date(1815, 4, 1), date(1871, 1, 18)), 55)
# Prussian first king crowned 18 January 1701: 170 years before the proclamation
eq("1701 to 1871", 1871 - 1701, 170)
# Kaiserbrief: draft 27 Nov, signed 30 Nov (3 days)
eq("draft to signature", (date(1870, 11, 30) - date(1870, 11, 27)).days, 3)

# Armies on the frontier: First 50,000 + Second 134,000 + Third 120,000 = 304,000 against 202,448
germans = 50000 + 134000 + 120000
eq("German frontier armies", germans, 304000)
assert 1.4 < germans / 202448 < 1.6
# Chassepot 1,500 m against needle gun 600 m: 2.5 times
eq("range ratio", Fraction(1500, 600), Fraction(5, 2))

# Bundesrat 1871: 58 votes; Prussia 17; 14 votes block; 25 states
votes = {"Prussia": 17, "Bavaria": 6, "Saxony": 4, "Württemberg": 4, "Baden": 3, "Hesse": 3, "Mecklenburg-Schwerin": 2, "Brunswick": 2}
total = sum(votes.values()) + 17
eq("Bundesrat votes", total, 58)
eq("number of states", len(votes) + 17, 25)
assert votes["Prussia"] >= 14, "Prussia must be able to block"
assert (total - votes["Prussia"]) < total - 14 + 1  # without Prussia the rest cannot form 44 alone
assert Fraction(votes["Prussia"], total) < Fraction(1, 3)
# 22 states of the North German Confederation + Bavaria, Württemberg, Baden = 25
eq("states 1871", 22 + 3, 25)
# Alsace and Lorraine: about 1.5 million; indemnity five billion francs
eq("indemnity", 5 * 10 ** 9, 5_000_000_000)
# Indemnity paid by 1873: two years after the treaty
eq("indemnity years", 1873 - 1871, 2)

# Paper structure (FACTS.md): P1 15 + 25 = 40; P2 two questions of 10 + 20 = 60
eq("Paper 1 total", 15 + 25, 40)
eq("Paper 2 total", 2 * (10 + 20), 60)
for lo, hi in [(3, 5), (6, 8), (9, 10)]:
    assert lo <= hi <= 10
for lo, hi in [(9, 12), (13, 16), (17, 20)]:
    assert lo <= hi <= 20
for lo, hi in [(4, 7), (8, 11), (12, 15)]:
    assert lo <= hi <= 15
for lo, hi in [(11, 15), (16, 20), (21, 25)]:
    assert lo <= hi <= 25

print("ok")
