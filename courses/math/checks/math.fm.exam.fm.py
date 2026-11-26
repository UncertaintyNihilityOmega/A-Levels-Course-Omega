# checks/math.fm.exam.fm.py: recomputes every number in the chapter
from math import isclose, floor, sqrt, cos
from fractions import Fraction

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def rh(x): return floor(x + 0.5)

eq("min per mark", 90 / 50, 1.8)
for marks, mins in [(5, 8), (6, 10), (7, 11), (9, 14), (10, 16)]:
    eq(f"{marks} marks", rh(marks * 1.6), mins)
eq("whole paper", 50 * 1.6, 80)
eq("spare", 90 - 50 * 1.6, 10)

q25 = [5, 6, 7, 7, 6, 9, 10]
q26 = [7, 5, 9, 8, 9, 6, 6]
eq("sum 2025", sum(q25), 50)
eq("sum 2026", sum(q26), 50)
assert len(q25) == 7 and len(q26) == 7
eq("q1 2026", 4 + 3, 7)
eq("q3 2026", 5 + 4, 9)
eq("q4 2026", 4 + 4, 8)
eq("q5 2026", 4 + 5, 9)
eq("q6 2026", 3 + 1 + 2, 6)

# vertical circle example: m = 0.4, a = 0.9, g = 10, u^2 = 27
m, a, g, u2 = 0.4, 0.9, 10, 27
eq("u2", 3 * a * g, 27)
for th in (0.3, 1.0, 2.0, 2.5):
    v2 = u2 - 2 * g * a * (1 - cos(th))
    eq("v2", v2, 9 + 18 * cos(th))
    T = m * g * cos(th) + m * v2 / a
    eq("T", T, 4 * (1 + 3 * cos(th)), 1e-9)
c = -1 / 3
eq("T slack", 4 * (1 + 3 * c), 0)
eq("v2 slack", 9 + 18 * c, 3)
eq("v slack", round(sqrt(3), 2), 1.73)
eq("marks vertical", 4 + 3, 7)

# elastic string example: l = 0.6, lam = 24, m = 0.5
l, lam, m = 0.6, 24, 0.5
for x in (0.0, 0.1, 0.3, 0.5):
    v2 = 2 * (m * g * (l + x) - lam * x * x / (2 * l)) / m
    eq("v2(x)", v2, 12 + 20 * x - 80 * x * x)
eq("equilibrium", lam * 0.125 / l, m * g)
eq("v2 max", 12 + 20 * 0.125 - 80 * 0.125 ** 2, 13.25)
eq("v max", round(sqrt(13.25), 2), 3.64)
x = (5 + sqrt(265)) / 40
eq("x max", round(x, 3), 0.532)
eq("v2 at x max", 12 + 20 * x - 80 * x * x, 0, 1e-9)
assert 80 * x * x - 20 * x - 12 < 1e-9 and abs(20 * x * x - 5 * x - 3) < 1e-9
eq("marks elastic", 3 + 3 + 2, 8)
print("ok")
