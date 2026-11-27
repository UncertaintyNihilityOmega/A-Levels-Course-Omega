# checks/math.fm.exam.fp1.py: recomputes every number in the chapter
from math import isclose, floor
from fractions import Fraction

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def rh(x): return floor(x + 0.5)

eq("min per mark", 120 / 75, 1.6)
for marks, mins in [(5, 7), (8, 11), (9, 13), (13, 18), (15, 21), (16, 22)]:
    eq(f"{marks} marks", rh(marks * 1.4), mins)
eq("whole paper", 75 * 1.4, 105)
eq("spare", 120 - 75 * 1.4, 15)

# June 2025 9231/11 question sizes
q = [8, 7, 7, 9, 13, 16, 15]
eq("sum 2025", sum(q), 75)
assert len(q) == 7

# induction example: u1 = 5, u_{n+1} = 2u_n + 3, u_n = 2^(n+2) - 3
u = 5
for n in range(1, 25):
    eq(f"u_{n}", u, 2 ** (n + 2) - 3)
    u = 2 * u + 3
eq("base", 2 ** 3 - 3, 5)
# step algebra: 2(2^(k+2) - 3) + 3 = 2^(k+3) - 3
for k in range(1, 12):
    eq("step", 2 * (2 ** (k + 2) - 3) + 3, 2 ** (k + 3) - 3)
eq("marks of induction example", 1 + 1 + 1 + 1 + 1, 5)

# method of differences example
def S(n): return sum(Fraction(1, r * (r + 2)) for r in range(1, n + 1))
def formula(n): return Fraction(3, 4) - Fraction(2 * n + 3, 2 * (n + 1) * (n + 2))
for n in range(1, 40):
    assert S(n) == formula(n), n
    # survivors form
    assert S(n) == Fraction(1, 2) * (1 + Fraction(1, 2) - Fraction(1, n + 1) - Fraction(1, n + 2)), n
    assert Fraction(1, 2) * ((n + 2) + (n + 1)) == Fraction(2 * n + 3, 2)
eq("n=1 formula", float(formula(1)), 1 / 3)
eq("n=1 value", 3 / 4 - 5 / 12, 1 / 3)
for r in range(1, 20):
    assert Fraction(1, r * (r + 2)) == Fraction(1, 2) * (Fraction(1, r) - Fraction(1, r + 2))
eq("S inf", float(formula(10 ** 6)), 0.75, 1e-5)
eq("marks of differences example", 1 + 1 + 1 + 1 + 1, 5)

# the roots warning example: x^3 - 7x + 6 = 0 has sum of roots 0
eq("sum roots", 0, -(0) / 1)
# timing rule 3: twice the planned time for a 5-mark question at 1.4 min per mark
eq("twice planned time, 5 marks", 2 * 5 * 1.4, 14)
# roots of 2a+1: y = 2x + 1 gives x = (y - 1)/2
eq("x from y", (7 - 1) / 2, 3)
print("ok")
