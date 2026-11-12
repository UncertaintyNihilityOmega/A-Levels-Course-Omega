# checks/hist.exam.p2.py: recomputes every number in the chapter (paper facts, level ranges, timing, dates)
from datetime import date, timedelta


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 2: two questions of 10 + 20 = 30 marks; 60 marks; 1 h 45 min = 105 min
eq("marks per question", 10 + 20, 30)
eq("total marks", 2 * (10 + 20), 60)
eq("paper minutes", 1 * 60 + 45, 105)
eq("minutes per mark", round(105 / 60, 2), 1.75)
# AO split 50/50
eq("AO split", 50 + 50, 100)
# specimen: three sections, two questions each = six questions, answer two
eq("specimen questions", 3 * 2, 6)

# Suggested time plan sums to 105
plan = [6, 14, 32, 14, 32, 7]
eq("time plan total", sum(plan), 105)
eq("question total minutes", 14 + 32, 46)
share_a = 14 / 46
assert 0.28 < share_a < 0.35, f"part (a) share of question time {share_a:.2f} is not about a third"
# (b): plan 4 + write 28 = 32
eq("part (b) split", 4 + 28, 32)

# Table A levels (top 10) and Table B levels (top 20): contiguous
A = {4: (9, 10), 3: (6, 8), 2: (3, 5), 1: (1, 2)}
prev = 11
for lvl in (4, 3, 2, 1):
    lo, hi = A[lvl]
    eq(f"Table A L{lvl} contiguous", hi, prev - 1)
    prev = lo
eq("Table A bottom", prev, 1)
B = {5: (17, 20), 4: (13, 16), 3: (9, 12), 2: (5, 8), 1: (1, 4)}
prev = 21
for lvl in (5, 4, 3, 2, 1):
    lo, hi = B[lvl]
    eq(f"Table B L{lvl} contiguous", hi, prev - 1)
    prev = lo
eq("Table B bottom", prev, 1)
# "top two marks, 19-20" of Level 5
eq("top two marks", (B[5][1] - 1, B[5][1]), (19, 20))

# Rotation (FACTS): the two Paper 2 topics by year, European option; every topic on Paper 1 in one year only
p1 = {2027: "France", 2028: "Germany", 2029: "Russia"}
topics = {"France", "Germany", "Russia"}
p2 = {y: topics - {p1[y]} for y in p1}
eq("2027 P2 European", p2[2027], {"Germany", "Russia"})
eq("2028 P2 European", p2[2028], {"France", "Russia"})
eq("2029 P2 European", p2[2029], {"France", "Germany"})
# American: P1 Gilded 2027, Great Crash 2028, Civil War 2029
us = {"Civil War", "Gilded Age", "Great Crash"}
p1us = {2027: "Gilded Age", 2028: "Great Crash", 2029: "Civil War"}
eq("2027 P2 American", us - {p1us[2027]}, {"Civil War", "Great Crash"})
eq("2028 P2 American", us - {p1us[2028]}, {"Civil War", "Gilded Age"})
eq("2029 P2 American", us - {p1us[2029]}, {"Gilded Age", "Great Crash"})
# International: P1 Imperialism 2027, 1919-29 2028, 1929-39 2029
intl = {"Imperialism", "1919-29", "1929-39"}
p1i = {2027: "Imperialism", 2028: "1919-29", 2029: "1929-39"}
eq("2027 P2 International", intl - {p1i[2027]}, {"1919-29", "1929-39"})
eq("2028 P2 International", intl - {p1i[2028]}, {"Imperialism", "1929-39"})
eq("2029 P2 International", intl - {p1i[2029]}, {"Imperialism", "1919-29"})

# Russia 1917 (Old Style -> New Style is +13 days in 1917); Julian February 1917 has 28 days
def ns(m, d):
    # Old Style date in 1917 -> New Style date
    base = date(1917, m, d)
    return base + timedelta(days=13)


eq("23 Feb OS = 8 March NS", ns(2, 23), date(1917, 3, 8))
eq("2 March OS = 15 March NS", ns(3, 2), date(1917, 3, 15))
eq("tsar took command 23 Aug 1915 OS = 5 Sept NS", date(1915, 8, 23) + timedelta(days=13), date(1915, 9, 5))
# strike of 23 February became a general strike "within two days" (25 February)
eq("two days", (date(1917, 2, 25) - date(1917, 2, 23)).days, 2)
# strikes 23 Feb to abdication 2 March: 7 days (1917 is not a leap year in either calendar)
eq("strike to abdication", (date(1917, 3, 2) - date(1917, 2, 23)).days, 7)
# Nicholas II became Tsar in 1894
eq("tsar accession", 1894, 1894)
# June offensive 18 June, July Days 3-5 July
eq("offensive to July Days", (date(1917, 7, 3) - date(1917, 6, 18)).days, 15)

# Germany: wars of 1864, 1866, 1870 = three wars
eq("three wars", len([1864, 1866, 1870]), 3)
eq("Konigratz weekday check (3 July 1866 is a Tuesday)", date(1866, 7, 3).weekday(), 1)
eq("Sedan 1 Sept 1870", date(1870, 9, 1).isoformat(), "1870-09-01")
eq("Empire proclaimed 18 Jan 1871", date(1871, 1, 18).isoformat(), "1871-01-18")

print("ok")
