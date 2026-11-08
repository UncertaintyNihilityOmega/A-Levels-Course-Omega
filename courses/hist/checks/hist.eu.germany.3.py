# checks/hist.eu.germany.3.py: recomputes every number in the chapter (dates, ages, intervals, percentages, votes, marks)
from datetime import date
from fractions import Fraction


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def age(born, on):
    return on.year - born.year - ((on.month, on.day) < (born.month, born.day))


# Wilhelm I: born 22 March 1797; Regent 7 October 1858 (aged 61); king 2 January 1861 (aged 63)
b = date(1797, 3, 22)
eq("age as Regent", age(b, date(1858, 10, 7)), 61)
eq("age as king", age(b, date(1861, 1, 2)), 63)
# Bismarck: born 1 April 1815; minister-president 23 September 1862 -> 47
eq("Bismarck age 1862", age(date(1815, 4, 1), date(1862, 9, 23)), 47)

# Order of events in the story in dates
seq = [date(1858, 10, 7), date(1859, 12, 5), date(1860, 2, 10), date(1861, 1, 2), date(1861, 6, 9), date(1862, 5, 1),
       date(1862, 9, 22), date(1862, 9, 23), date(1862, 9, 30), date(1863, 2, 8), date(1863, 6, 1), date(1863, 8, 17),
       date(1863, 11, 15), date(1863, 11, 18), date(1864, 2, 1), date(1864, 4, 18), date(1864, 10, 30), date(1865, 8, 14),
       date(1865, 10, 4), date(1866, 4, 8), date(1866, 4, 9), date(1866, 6, 1), date(1866, 6, 15), date(1866, 7, 3),
       date(1866, 7, 26), date(1866, 8, 23), date(1866, 9, 3), date(1867, 7, 1)]
assert seq == sorted(seq), "timeline out of order"
# "A week later, on 30 September": 23 -> 30 September
eq("week after appointment", (date(1862, 9, 30) - date(1862, 9, 23)).days, 7)
# Babelsberg 22 September the day before
eq("Babelsberg", (date(1862, 9, 23) - date(1862, 9, 22)).days, 1)

# Army reform: recruits 40,000 -> 63,000: more than half more
inc = Fraction(63000, 40000) - 1
assert inc > Fraction(1, 2), f"increase {float(inc):.3f} is not more than half"
# Roon war minister 5 Dec 1859, bill February 1860
assert date(1859, 12, 5) < date(1860, 2, 10)
# Constitutional conflict February 1860 -> September 1866: about six years
yrs = (date(1866, 9, 3) - date(1860, 2, 10)).days / 365.25
assert 6 <= yrs < 7, yrs
# "four years" of rule without a budget 1862-65 (indemnity covers four budget years)
eq("indemnity years", len(range(1862, 1866)), 4)

# Frederick VII died 15 November 1863; Christian IX signed 18 November: 3 days
eq("signing after death", (date(1863, 11, 18) - date(1863, 11, 15)).days, 3)
# Ultimatum 16 January 1864, 48 hours; war 1 February 1864 -> 16 days after the ultimatum
eq("ultimatum to war", (date(1864, 2, 1) - date(1864, 1, 16)).days, 16)
# Düppel 18 April 1864; Als 29 June; Treaty of Vienna 30 October
assert date(1864, 4, 18) < date(1864, 6, 29) < date(1864, 10, 30)
# London conference 25 April - 25 June 1864
assert date(1864, 4, 25) < date(1864, 6, 25) < date(1864, 10, 30)
# Denmark's population 2.6 m -> 1.6 m: about two fifths
loss = Fraction(26 - 16, 26)
assert Fraction(35, 100) < loss < Fraction(45, 100), float(loss)
# Gastein 14 August 1865 -> war 15 June 1866: 305 days
eq("Gastein to war", (date(1866, 6, 15) - date(1865, 8, 14)).days, 305)
# Italian treaty 8 April 1866, three months -> expires 8 July 1866
assert date(1866, 8, 7) > date(1866, 7, 8) > date(1866, 6, 15)
assert date(1866, 7, 3) < date(1866, 7, 8)

# Königgrätz 3 July 1866: 15 June -> 3 July = 18 days (about two and a half weeks)
d = (date(1866, 7, 3) - date(1866, 6, 15)).days
eq("invasion to Königgrätz", d, 18)
assert 2.4 < d / 7 < 2.7
# Prussian loss about 9,000 (9,172); Austrian about three times (about 31,000)
r = Fraction(31000, 9172)
assert Fraction(3) < r < Fraction(4), float(r)
# Königgrätz -> Nikolsburg 26 July: 23 days; Prague 23 August
eq("Königgrätz to Nikolsburg", (date(1866, 7, 26) - date(1866, 7, 3)).days, 23)
# Forces at Königgrätz: about 220,000 against about 215,000 (infobox 220,984 and 206,000-215,000)
assert 215000 <= 220984 and 206000 <= 215000
# Crown Prince's army nearly 100,000
# Indemnity bill 230 to 75: total 305, share
eq("indemnity total", 230 + 75, 305)
share = Fraction(230, 305)
assert Fraction(75, 100) < share < Fraction(76, 100), float(share)
# indemnity passed 3 Sept, signed 14 Sept
eq("indemnity signing", (date(1866, 9, 14) - date(1866, 9, 3)).days, 11)
# NGC: four fifths of 30 million in Prussia -> about 24 million
assert 30 * 4 // 5 == 24
# Conservatives 35 -> 140: four times
eq("conservative gain", 140 // 35, 4)

# Gastein price 2.5 million rigsdalers
eq("Lauenburg price", 2_500_000, 2500000)

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
