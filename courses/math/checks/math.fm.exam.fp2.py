# checks/math.fm.exam.fp2.py: recomputes every number in the chapter
from math import isclose, floor, pi, sin, cos, exp
from fractions import Fraction

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def rh(x): return floor(x + 0.5)

eq("min per mark", 120 / 75, 1.6)
for marks, mins in [(5, 7), (7, 10), (10, 14), (14, 20), (15, 21)]:
    eq(f"{marks} marks", rh(marks * 1.4), mins)
eq("whole paper", 75 * 1.4, 105)
eq("spare", 120 - 75 * 1.4, 15)

q25 = [5, 7, 6, 9, 10, 15, 10, 13]
q26 = [5, 7, 11, 8, 10, 10, 10, 14]
eq("sum 2025", sum(q25), 75)
eq("sum 2026", sum(q26), 75)
assert len(q25) == 8 and len(q26) == 8
# June 2026 question parts
eq("q2 2026", 4 + 3, 7)
eq("q3 2026", 4 + 7, 11)
eq("q4 2026", 3 + 5, 8)
eq("q5 2026", 4 + 4 + 2, 10)
eq("q8 2026", 3 + 4 + 7, 14)

# reduction formula I_n = int_0^{pi/2} x^n sin x dx = n (pi/2)^(n-1) - n(n-1) I_{n-2}
def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3
I = lambda n: simpson(lambda x: x ** n * sin(x), 0, pi / 2)
for n in range(2, 8):
    eq(f"I_{n}", I(n), n * (pi / 2) ** (n - 1) - n * (n - 1) * I(n - 2), 1e-9)
eq("I_0", I(0), 1, 1e-9)
eq("I_2", I(2), pi - 2, 1e-9)
eq("marks of reduction example", 1 + 1 + 1 + 1 + 1 + 1 + 1, 7)

# second order DE: y'' + 4y' + 3y = 6 e^{-2x}, y(0) = 0, y'(0) = 1
A, B, lam = Fraction(7, 2), Fraction(5, 2), -6
assert (4 - 8 + 3) * lam == 6
assert A + B + lam == 0
assert -A - 3 * B - 2 * lam == 1
assert A + 3 * B == 11 and A + B == 6 and 2 * B == 5
y = lambda x: float(A) * exp(-x) + float(B) * exp(-3 * x) + lam * exp(-2 * x)
h = 1e-5
for x in (0.0, 0.4, 1.3):
    d1 = (y(x + h) - y(x - h)) / (2 * h)
    d2 = (y(x + h) - 2 * y(x) + y(x - h)) / h ** 2
    eq("DE", d2 + 4 * d1 + 3 * y(x), 6 * exp(-2 * x), 1e-4)
eq("y(0)", y(0), 0)
eq("y'(0)", (y(h) - y(-h)) / (2 * h), 1, 1e-6)
eq("marks of DE example", 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1, 8)
# auxiliary roots
for m in (-1, -3):
    assert m * m + 4 * m + 3 == 0
# reduction formula boundary terms: I_n = n (pi/2)^(n-1) - n(n-1) I_(n-2), checked numerically for n = 2..5
import math as _m
def _I(n, N=20000):
    h = (_m.pi / 2) / N
    return sum((k * h) ** n * _m.sin(k * h) * (1 if k in (0, N) else (4 if k % 2 else 2)) for k in range(N + 1)) * h / 3
for _n in range(2, 6):
    eq("reduction n=%d" % _n, _I(_n), _n * (_m.pi / 2) ** (_n - 1) - _n * (_n - 1) * _I(_n - 2), 1e-7)
# x dy/dx - 4y = x^3 -> dy/dx - (4/x) y = x^2: P = -4/x, integrating factor x^-4
eq("IF check", _m.exp(-4 * _m.log(2.0)), 2.0 ** -4)
print("ok")
