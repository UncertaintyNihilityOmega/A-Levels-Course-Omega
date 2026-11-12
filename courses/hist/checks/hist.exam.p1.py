# checks/hist.exam.p1.py: recomputes every number in the chapter (paper facts, level ranges, timing, dates)
from datetime import date


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


# Paper 1: 40 marks = (a) 15 + (b) 25; 1 h 15 min = 75 min
eq("total marks", 15 + 25, 40)
eq("paper minutes", 1 * 60 + 15, 75)
# AOs: AO1 25% + AO3 75%
eq("AO split", 25 + 75, 100)
# a quarter and three quarters of 40 marks are whole numbers
eq("AO1 share of marks", 40 * 25 // 100, 10)
eq("AO3 share of marks", 40 * 75 // 100, 30)
# minutes per mark "about 1.9"
eq("minutes per mark", round(75 / 40, 1), 1.9)

# Suggested time plan sums to 75
plan = [8, 20, 4, 38, 5]
eq("time plan total", sum(plan), 75)
# (a) = plan 2 + write 18 = 20
eq("part (a) split", 2 + 18, 20)
# part (b) deserves more than half of the writing time: 38 of (18 + 38)
assert 38 / (18 + 38) > 0.5

# Table A levels: contiguous ranges, top 15
A = {4: (12, 15), 3: (8, 11), 2: (4, 7), 1: (1, 3)}
prev_lo = 16
for lvl in (4, 3, 2, 1):
    lo, hi = A[lvl]
    eq(f"Table A L{lvl} contiguous", hi, prev_lo - 1)
    prev_lo = lo
eq("Table A bottom", prev_lo, 1)
eq("Table A top", A[4][1], 15)

# Table B levels: contiguous ranges, top 25
B = {5: (21, 25), 4: (16, 20), 3: (11, 15), 2: (6, 10), 1: (1, 5)}
prev_lo = 26
for lvl in (5, 4, 3, 2, 1):
    lo, hi = B[lvl]
    eq(f"Table B L{lvl} contiguous", hi, prev_lo - 1)
    prev_lo = lo
eq("Table B bottom", prev_lo, 1)
eq("Table B top", B[5][1], 25)
# quiz: Level 4 of part (b) "just meets" -> lowest mark of the level
eq("quiz: Level 4 just meets", B[4][0], 16)
# spot the weak answer: Level 3 bottom of part (b)
eq("weak answer mark", B[3][0], 11)

# Rotation (FACTS): the Paper 1 topic by year and option
rot = {
    2027: ("France", "Gilded Age", "Imperialism"),
    2028: ("Germany", "Great Crash", "1919-29"),
    2029: ("Russia", "Civil War", "1929-39"),
}
eq("2028 European Paper 1", rot[2028][0], "Germany")
# every topic is Paper 1 in exactly one of the three years
for i in range(3):
    eq(f"option {i} topics distinct", len({rot[y][i] for y in rot}), 3)

# French Revolution dates in the ladder: 17, 20, 23, 27 June 1789
d17, d20, d23, d27 = (date(1789, 6, d) for d in (17, 20, 23, 27))
eq("Oath to royal session", (d23 - d20).days, 3)
eq("17 June to 23 June", (d23 - d17).days, 6)
eq("royal session to 27 June", (d27 - d23).days, 4)

# Specimen 2027: three sections, one question each
eq("sections", len(["European", "American", "International"]), 3)
# Provenance dates in the sources
eq("source A date", date(1789, 6, 20).isoformat(), "1789-06-20")
eq("source B date", date(1789, 6, 23).isoformat(), "1789-06-23")

print("ok")
