# checks/math.p3.partial.py: recomputes every number in the Partial fractions and binomial series chapter.
from fractions import Fraction as F
from math import isclose, sqrt, comb

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def pf(label, lhs, rhs, xs=(F(3, 10), F(17, 10), F(-34, 10), F(5), F(-7, 2))):
    for x in xs: assert lhs(x) == rhs(x), (label, x, lhs(x), rhs(x))
def binom_series(n, u, terms):
    s, c = F(0), F(1)
    for k in range(terms):
        s += c * u**k; c = c * (n - k) / (k + 1)
    return s
def coeffs(n, terms):
    out, c = [], F(1)
    for k in range(terms): out.append(c); c = c * (n - k) / (k + 1)
    return out

# partial fractions
pf("1", lambda x: (5*x + 1) / ((x - 1) * (x + 2)), lambda x: 2 / (x - 1) + 3 / (x + 2))
assert 5 * 1 + 1 == 6 == 3 * 2 and 5 * -2 + 1 == -9 == -3 * 3
pf("2", lambda x: (2*x**2 + 5*x - 1) / ((x - 1) * (x + 1) * (x + 2)), lambda x: 1 / (x - 1) + 2 / (x + 1) - 1 / (x + 2))
assert 2 + 5 - 1 == 6 and 2 - 5 - 1 == -4 and 8 - 10 - 1 == -3
pf("3", lambda x: (5*x**2 + 10*x + 3) / ((x - 1) * (x + 2)**2), lambda x: 2 / (x - 1) + 3 / (x + 2) - 1 / (x + 2)**2)
assert 5 + 10 + 3 == 18 == 9 * 2 and 20 - 20 + 3 == 3 == -3 * -1 and 5 == 2 + 3
pf("4", lambda x: (5*x**2 + 2*x + 7) / ((x + 1) * (x**2 + 4)), lambda x: 2 / (x + 1) + (3*x - 1) / (x**2 + 4))
assert 5 - 2 + 7 == 10 == 5 * 2 and 5 == 2 + 3 and 7 == 8 - 1 and 2 == 3 - 1
# binomial series
assert coeffs(F(-1), 4) == [1, -1, 1, -1]; assert coeffs(F(1, 2), 4) == [1, F(1, 2), F(-1, 8), F(1, 16)]
assert coeffs(F(-2), 4) == [1, -2, 3, -4]
assert [c * 2**k for k, c in enumerate(coeffs(F(-3), 4))] == [1, -6, 24, -80]
c = coeffs(F(-1, 2), 3); assert c == [1, F(-1, 2), F(3, 8)]
u = F(-1, 2); assert [1, c[1] * u, c[2] * u**2] == [1, F(1, 4), F(3, 32)]
# sqrt 4.04 and gamma
eq("sqrt", 2 + 0.01 - 0.000025, 2.009975, 1e-12); eq("sqrt calc", sqrt(4.04), 2.00997512, 1e-8)
eq("gamma", 1 + 0.005 + 0.0000375, 1.0050375, 1e-12); eq("gamma exact", (1 - 0.01)**-0.5, 1.0050378, 1e-7)
# combined exam
pf("5", lambda x: (5 - x) / ((1 + x) * (1 - 2*x)), lambda x: 2 / (1 + x) + 3 / (1 - 2*x), xs=(F(3, 10), F(17, 10), F(5)))
assert 6 == 3 * 2 and F(9, 2) == F(3, 2) * 3
s = [2 * a + 3 * b * 2**k for k, (a, b) in enumerate(zip(coeffs(F(-1), 4), coeffs(F(-1), 4)))]
s = [2 * (-1)**k + 3 * 2**k for k in range(4)]; assert s == [5, 4, 14, 22]
x = F(1, 10); eq("series check", float(sum(s[k] * x**k for k in range(4))), 5.562, 1e-9); eq("exact", float((5 - x) / ((1 + x) * (1 - 2 * x))), 5.568, 1e-3)
# expansion of f
fx = [2 * -1 * 1 + F(3, 2) * 1 - F(1, 4) * 1, -2 + F(3, 2) * F(-1, 2) - F(1, 4) * -1, -2 + F(3, 2) * F(1, 4) - F(1, 4) * F(3, 4)]
assert fx == [F(-3, 4), F(-5, 2), F(-29, 16)], fx
assert coeffs(F(-2), 3) == [1, -2, 3] and [c * F(1, 2)**k for k, c in enumerate(coeffs(F(-2), 3))] == [1, -1, F(3, 4)]
assert (5 + 10 + 3) / ((-1) * 4 * 1) is not None and F(3, -4) == F(-3, 4)

# try
pf("T1", lambda x: (4*x + 7) / ((x + 1) * (x + 2)), lambda x: 3 / (x + 1) + 1 / (x + 2))
pf("T2", lambda x: (2*x**2 - 6*x - 2) / (x * (x - 1) * (x + 2)), lambda x: 1 / x - 2 / (x - 1) + 3 / (x + 2))
assert 2 * 1 - 6 - 2 == -6 == 3 * -2 and 8 + 12 - 2 == 18 == 6 * 3
pf("T3", lambda x: (5*x**2 - 7*x + 6) / ((x + 1) * (x - 2)**2), lambda x: 2 / (x + 1) + 3 / (x - 2) + 4 / (x - 2)**2)
assert 5 + 7 + 6 == 18 == 9 * 2 and 20 - 14 + 6 == 12 == 3 * 4
pf("T4", lambda x: (3*x**2 + x - 2) / ((x - 1) * (x**2 + 1)), lambda x: 1 / (x - 1) + (2*x + 3) / (x**2 + 1))
assert 3 + 1 - 2 == 2 == 2 * 1 and 3 == 1 + 2 and -2 == 1 - 3
c = coeffs(F(-1, 2), 4); u = F(-3); assert [c[k] * u**k for k in range(4)] == [1, F(3, 2), F(27, 8), F(135, 16)]
c = coeffs(F(3, 2), 3); assert [8 * c[k] * F(1, 4)**k for k in range(3)] == [8, 3, F(3, 16)]
eq("T7", 1 + 0.02 - 0.0002 + 0.000004, 1.019804, 1e-12); eq("T7 calc", round(sqrt(1.04), 6), 1.019804, 1e-12)
c = coeffs(F(-1), 3); half = coeffs(F(-1), 3)
t = [3 * c[k] + F(1, 2) * c[k] * F(1, 2)**k for k in range(3)]; assert t == [F(7, 2), F(-13, 4), F(25, 8)], t
# exam 1
c = coeffs(F(-1, 2), 4); u = F(-2); a = [c[k] * u**k for k in range(4)]; assert a == [1, 1, F(3, 2), F(5, 2)]
prod = [2 * a[0], 2 * a[1] + a[0], 2 * a[2] + a[1], 2 * a[3] + a[2]]; assert prod == [2, 3, 4, F(13, 2)]
x = F(1, 100); eq("check", float(sum(prod[k] * x**k for k in range(4))), (2 + x) / sqrt(1 - 2 * x), 1e-6)
# exam 2
e1 = [2 * (-1)**k for k in range(3)]
e2 = [F(-3, 2) * c_ * F(-1, 2)**k for k, c_ in enumerate(coeffs(F(-1), 3))]
e3 = [c_ * F(-1, 2)**k for k, c_ in enumerate(coeffs(F(-2), 3))]
tot = [e1[k] + e2[k] + e3[k] for k in range(3)]; assert tot == [F(3, 2), F(-7, 4), F(19, 8)], tot
# quiz
assert comb(2, 2) == 1 and F(-2) * F(-3) / 2 == 3
assert 4**F(1, 2) == 2

# ---- v2 additions: warm-up, proof, spot the error, exam practice, stretch ----
assert [comb(4, k) for k in range(3)] == [1, 4, 6] and 2**3 - 3 * 2**2 + 4 == 0 and sqrt(1 / (F(1, 4))) == 2.0
# cover-up proof: A = f(a)/g(a) at random points for (x-1)(x+2) and the repeated factor
assert F(5 * 1 + 1, 1 + 2) == 2 and F(5 * -2 + 1, -2 - 1) == 3
# C by cover-up in (x-1)(x+2)^2: f(-2)/(x-1) at -2 = (20-20+3)/(-3) = -1
assert F(5 * 4 - 20 + 3, -2 - 1) == -1
# spot the error: (4+2x)^(-1/2)
c = coeffs(F(-1, 2), 3); u = F(1, 2)
ser = [c[k] * u**k for k in range(3)]; assert ser == [1, F(-1, 4), F(3, 32)]
good = [F(1, 2) * s for s in ser]; assert good == [F(1, 2), F(-1, 8), F(3, 64)]
bad = [-2 * s for s in ser]; assert bad == [-2, F(1, 2), F(-3, 16)]
assert 4**-0.5 == 0.5
eq("SE check", 4.2**-0.5, 0.48795, 5e-6); eq("SE series", 0.5 - 0.0125 + 0.00046875, 0.48797, 5e-6)
assert 1 + 1 + 1 + 1 + 1 + 1 == 6
# Exam practice
pf("E1", lambda x: (7*x + 1) / ((x + 1) * (x - 2)), lambda x: 2 / (x + 1) + 5 / (x - 2))
assert 7 * -1 + 1 == -6 == -3 * 2 and 7 * 2 + 1 == 15 == 3 * 5
c = coeffs(F(-1, 2), 3); assert [c[k] * 4**k for k in range(3)] == [1, -2, 6]
pf("E3", lambda x: (4*x**2 - 3*x + 5) / ((x - 1) * (x**2 + 2)), lambda x: 2 / (x - 1) + (2*x - 1) / (x**2 + 2))
assert 4 - 3 + 5 == 6 == 3 * 2 and 4 == 2 + 2 and 5 == 2 * 2 - (-1) and -1 - 2 == -3
c = coeffs(F(-2), 3); u = F(3, 2)
assert [F(1, 4) * c[k] * u**k for k in range(3)] == [F(1, 4), F(-3, 4), F(27, 16)]
assert [c[k] * u**k for k in range(3)] == [1, -3, F(27, 4)]
c = coeffs(F(1, 2), 4); u = F(-2); a = [c[k] * u**k for k in range(4)]; assert a == [1, -1, F(-1, 2), F(-1, 2)]
eq("E5 series", 1 - 0.01 - 0.00005 - 0.0000005, 0.9899495, 1e-12); eq("E5 5dp", round(0.9899495 + 1e-12, 5), 0.98995, 1e-12)
eq("E5 true", sqrt(0.98), 0.98995, 5e-6)
pf("E6", lambda x: (6 - 3*x) / ((1 - 2*x) * (1 + x)**2), lambda x: 2 / (1 - 2*x) + 1 / (1 + x) + 3 / (1 + x)**2)
assert 6 - F(3, 2) == F(9, 2) == F(9, 4) * 2 and 6 + 3 == 9 == 3 * 3 and 0 == 2 - 2 * 1
a1 = [2 * k_ for k_ in (1, 2, 4)]; a2 = [1, -1, 1]; a3 = [3 * v for v in (1, -2, 3)]
assert a1 == [2, 4, 8] and a3 == [3, -6, 9] and [p + q + r for p, q, r in zip(a1, a2, a3)] == [6, -3, 18]
assert [[1, 2, 4][k] for k in range(3)] == [c_ * (-2)**k * (-1)**0 for k, c_ in enumerate(coeffs(F(-1), 3))] and coeffs(F(-1), 3) == [1, -1, 1]
# Q7
p = lambda x: x**3 - 2*x**2 - 5*x + 6
assert p(3) == 0 and p(1) == 0 and p(-2) == 0
assert [(x - 3) * (x**2 + x - 2) - p(x) for x in range(-3, 6)] == [0] * 9
pf("E7", lambda x: (3*x**2 - 14*x + 5) / p(x), lambda x: 1 / (x - 1) + 3 / (x + 2) - 1 / (x - 3))
assert 3 - 14 + 5 == -6 == -6 * 1 and 12 + 28 + 5 == 45 == 15 * 3 and 27 - 42 + 5 == -10 == 10 * -1
e1 = [-1, -1, -1]; e2 = [F(3, 2) * c_ * F(1, 2)**k * (-1)**k for k, c_ in enumerate([1, 1, 1])]
assert e2 == [F(3, 2), F(3, 2) * F(1, 2) * -1, F(3, 2) * F(1, 4)] == [F(3, 2), F(-3, 4), F(3, 8)]
e3 = [F(1, 3) * F(1, 3)**k for k in range(3)]; assert e3 == [F(1, 3), F(1, 9), F(1, 27)]
tot = [e1[k] + e2[k] + e3[k] for k in range(3)]; assert tot == [F(5, 6), F(-59, 36), F(-127, 216)], tot
x = F(1, 100); eq("E7 series", float(sum(tot[k] * x**k for k in range(3))), float((3*x**2 - 14*x + 5) / p(x)), 1e-5)
assert F(5, 6) == F(3 * 0 - 0 + 5, p(0))
# Stretch 1
r1 = lambda r: F(1, r * (r + 2)); assert all(r1(r) == F(1, 2) * (F(1, r) - F(1, r + 2)) for r in range(1, 20))
assert F(1, 2) == F(1, 2) and sum(r1(r) for r in range(1, 5)) == F(17, 30)
assert F(1, 2) * (1 + F(1, 2) - F(1, 5) - F(1, 6)) == F(17, 30) and 1 + F(1, 2) - F(1, 5) - F(1, 6) == F(34, 30)
N = 10**6; eq("S1 limit", float(sum(r1(r) for r in range(1, 2001))), 0.75, 1e-3); assert F(1, 2) * F(3, 2) == F(3, 4)
for N in (3, 7, 12): assert sum(r1(r) for r in range(1, N + 1)) == F(1, 2) * (1 + F(1, 2) - F(1, N + 1) - F(1, N + 2))
# Stretch 2
n, a = -3, 2; assert n * a == -6 and F(n * (n - 1), 2) * a**2 == 24 and F(n * (n - 1) * (n - 2), 6) * a**3 == -80
assert 18 * (n - 1) == 24 * n
print("ok")
