# checks/phys.overview.py: recomputes the numbers in the course map (FACTS.md exam structure).
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

marks = {1: 40, 2: 60, 3: 40, 4: 100, 5: 30}
eq("AS marks", marks[1] + marks[2] + marks[3], 140)
eq("A Level marks", sum(marks.values()), 270)

# weights: AS qualification and A Level qualification each add up to 100%
eq("AS weights", 31 + 46 + 23, 100)
eq("A Level weights", 15.5 + 23 + 11.5 + 38.5 + 11.5, 100)
# each A Level weight is half of the AS weight for Papers 1-3
for name, a, al in (("P1", 31, 15.5), ("P2", 46, 23), ("P3", 23, 11.5)):
    eq("half " + name, a / 2, al)

# assessment objectives
eq("AO total", 40 + 40 + 20, 100)

# Paper 3 is two 20-mark questions, Paper 5 two 15-mark questions
eq("P3 questions", 2 * 20, marks[3])
eq("P5 questions", 2 * 15, marks[5])

# guided learning hours and the sample plan
eq("AS weeks at 9 h", 180 / 9, 20)
eq("A Level extra hours", 360 - 180, 180)

# topic count: 11 AS topics + 14 A Level topics = 25
eq("topics", 11 + 14, 25)
eq("A Level topics 12-25", 25 - 12 + 1, 14)

# sample plan: AS weeks 1-20, A Level weeks 21-44
eq("AS plan weeks", 20 - 1 + 1, 20)
eq("A Level plan weeks", 44 - 21 + 1, 24)

print("ok")
