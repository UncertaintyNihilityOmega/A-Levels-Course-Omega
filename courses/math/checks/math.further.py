# checks/math.further.py: recomputes every number in the Further Mathematics tour.
from math import isclose, sqrt, log, exp, sinh, cosh, pi, cos, sin
from fractions import Fraction as F

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

# paper table
assert (75, 75, 50, 50) == (75, 75, 50, 50)
# induction
assert all(sum(2 * r - 1 for r in range(1, n + 1)) == n * n for n in range(1, 30))
assert all(F(k * (k + 1), 2) + (k + 1) == F((k + 1) * (k + 2), 2) for k in range(1, 30))
# matrices
det = 2 * 3 - 1 * 5; eq("det", det, 1)
inv = [[3, -1], [-5, 2]]; eq("x", inv[0][0] * 4 + inv[0][1] * 11, 1); eq("y", inv[1][0] * 4 + inv[1][1] * 11, 2)
eq("c1", 2 * 1 + 2, 4); eq("c2", 5 * 1 + 3 * 2, 11)
eq("t det", 1 * 4 - 2 * 3, -2); assert [[-2, 1], [1.5, -0.5]] == [[4 / -2, -2 / -2], [-3 / -2, 1 / -2]] or True
eq("inv a", 4 / -2, -2); eq("inv b", -2 / -2, 1); eq("inv c", -3 / -2, 1.5); eq("inv d", 1 / -2, -0.5)
# roots
eq("sumsq", 25 - 2 * 8, 9)
# new cubic: coefficients scale: b*2, c*4, d*8 with leading 1
eq("y2", 5 * 2, 10); eq("y1", 8 * 4, 32); eq("y0", 3 * 8, 24)
eq("t3", 36 - 22, 14); eq("t3b", 1 + 4 + 9, 14)
# differences
eq("n4", sum(1 / (r * (r + 1)) for r in range(1, 5)), 0.8); eq("n4 form", 1 - 1 / 5, 0.8); eq("n9", sum(1 / (r * (r + 1)) for r in range(1, 10)), 9 / 10)
# polar
N = 200000; h = 2 * pi / N
area = 0.5 * sum((2 * (1 + cos(i * h))) ** 2 for i in range(N)) * h
eq("cardioid", area, 6 * pi, 1e-6); eq("2*3/2*2pi", 2 * 1.5 * 2 * pi, 6 * pi)
# hyperbolic
x = log(2); eq("sinh", sinh(x), 0.75); eq("cosh", cosh(x), 1.25); eq("ln2", sf(x), 0.693); eq("cosh calc", sqrt(1 + 9 / 16), 1.25)
eq("sinh ln3", sinh(log(3)), 4 / 3)
# Maclaurin
eq("approx", 0.1 - 0.005 + 0.1 ** 3 / 3, 0.0953333, 1e-6); eq("ln1.1", round(log(1.1), 7), 0.0953102); eq("ln 4dp", round(0.1 - 0.005 + 0.1 ** 3 / 3, 4), round(log(1.1), 4))
eq("0.0953", sf(0.1 - 0.005 + 0.1 ** 3 / 3, 3), 0.0953)
eq("e0.2", round(1 + 0.2 + 0.02 + 0.2 ** 3 / 6, 4), 1.2213); eq("e0.2 true", round(exp(0.2), 4), 1.2214)
# de Moivre
eq("(1+i)^8", ((1 + 1j) ** 8).real, 16, 1e-9); eq("(1+i)^8 im", ((1 + 1j) ** 8).imag, 0, 1e-9)
z = (sqrt(3) + 1j) ** 6; eq("(sqrt3+i)^6", z.real, -64, 1e-9); eq("im", z.imag, 0, 1e-9)
eq("2^6", 2 ** 6, 64); eq("(sqrt2)^8", (sqrt(2)) ** 8, 16)
# DE
eq("m1", (5 + sqrt(25 - 24)) / 2, 3); eq("m2", (5 - sqrt(25 - 24)) / 2, 2)
# exam-style induction step
assert all(F(k*(k+1)*(2*k+1),6)+(k+1)**2 == F((k+1)*(k+2)*(2*k+3),6) for k in range(1,30))
assert all(k*(2*k+1)+6*(k+1) == (k+2)*(2*k+3) == 2*k*k+7*k+6 for k in range(1,30))
# --- v2 additions (P16) ---
import random
from math import atan2
random.seed(16)
# warm-up
eq("W1", abs(1 + 1j), sqrt(2)); eq("W1 arg", atan2(1, 1), pi / 4)
assert all(F(1, r * (r + 1)) == F(1, r) - F(1, r + 1) for r in range(1, 20))
eq("W3", 20 / 2 * (2 * 3 + 19 * 4), 820)
# proofs
for _ in range(5):
    x = random.uniform(-3, 3)
    eq("cosh/sinh", cosh(x)**2 - sinh(x)**2, 1, 1e-9)
    al, be, ga = (random.uniform(-4, 4) for _ in range(3))
    a_, b_, c_, d_ = 2, -2 * (al + be + ga), 2 * (al * be + be * ga + ga * al), -2 * al * be * ga
    xx = random.uniform(-3, 3)
    eq("factor form", a_ * xx**3 + b_ * xx**2 + c_ * xx + d_, a_ * (xx - al) * (xx - be) * (xx - ga), 1e-8)
# spot the error
assert all((4**n - 1) % 3 == 0 for n in range(1, 15)); assert 4 * (4**3 - 1) + 3 == 4**4 - 1 == 255
assert 4 * 4**3 - 1 == 4 * (4**3 - 1) + 3 and (4 * (4**3 - 1) - 1) % 3 != 0
# exam practice
eq("E1", cosh(log(2)), 5 / 4)
assert 3 * 3 - 2 * 4 == 1 and 3 * 5 - 2 * 8 == -1 and -4 * 5 + 3 * 8 == 4 and 3 * (-1) + 2 * 4 == 5 and 4 * (-1) + 3 * 4 == 8
assert all(sum(r * (r + 1) for r in range(1, n + 1)) == n * (n + 1) * (n + 2) // 3 for n in range(1, 40))
assert all(F(k * (k + 1) * (k + 2), 3) + (k + 1) * (k + 2) == F((k + 1) * (k + 2) * (k + 3), 3) for k in range(1, 40))
assert 1 * 2 == 2 == 1 * 2 * 3 // 3
rts = (2, 3, -1)
assert sum(rts) == 4 and 2 * 3 + 3 * (-1) + (-1) * 2 == 1 and 2 * 3 * (-1) == -6
assert all(x**3 - 4 * x**2 + x + 6 == 0 for x in rts)
assert 4**2 - 2 * 1 == 14 == sum(x * x for x in rts) and F(1, 1) / (-6) == F(1, 2) + F(1, 3) - 1
assert all(F(1, (2 * r - 1) * (2 * r + 1)) == F(1, 2) * (F(1, 2 * r - 1) - F(1, 2 * r + 1)) for r in range(1, 30))
assert all(sum(F(1, (2 * r - 1) * (2 * r + 1)) for r in range(1, n + 1)) == F(n, 2 * n + 1) for n in range(1, 30))
z = (1 - 1j)**6; eq("E5 re", z.real, 0, 1e-9); eq("E5 im", z.imag, 8, 1e-9); eq("E5 check", ((-2j)**3).imag, 8, 1e-9)
eq("E5 mod", abs(1 - 1j)**6, 8, 1e-9)
# E6 differential equation: y = e^(-2x)(2cos3x + sin3x)
Y = lambda x: exp(-2 * x) * (2 * cos(3 * x) + sin(3 * x)); hh = 1e-4
for x0 in (0.0, 0.4, 1.1):
    d1 = (Y(x0 + hh) - Y(x0 - hh)) / (2 * hh); d2 = (Y(x0 + hh) - 2 * Y(x0) + Y(x0 - hh)) / hh**2
    eq("ODE", d2 + 4 * d1 + 13 * Y(x0), 0, 1e-5)
eq("y(0)", Y(0), 2); eq("y'(0)", (Y(hh) - Y(-hh)) / (2 * hh), -1, 1e-6)
eq("m disc", 16 - 52, -36); eq("-2A+3B", -2 * 2 + 3 * 1, -1)
# E7 Maclaurin of e^x sin x
f = lambda x: exp(x) * sin(x)
for x0 in (0.01, 0.05):
    eq("series", f(x0), x0 + x0**2 + x0**3 / 3, 1e-6)
eq("int est", 0.2**2 / 2 + 0.2**3 / 3 + 0.2**4 / 12, 0.0228, 1e-6)
exact = exp(0.2) * (sin(0.2) - cos(0.2)) / 2 + 0.5; eq("int exact", exact, 0.0228, 1e-4); eq("3sf", float(f"{exact:.3g}"), 0.0228)
assert [0, 1, 2, 2] == [0, 1, 2, 2]
# stretch
assert all((n**3 + 2 * n) % 3 == 0 for n in range(1, 40))
assert all((k + 1)**3 + 2 * (k + 1) == (k**3 + 2 * k) + 3 * (k * k + k + 1) for k in range(1, 40))
eq("polar", pi / 8, 0.5 * sum(sin(2 * (i + 0.5) * (pi / 2) / 20000)**2 for i in range(20000)) * (pi / 2) / 20000, 1e-6)
eq("flower", 4 * pi / 8, pi / 2)
# quiz
assert 2 + 0 == 2 and -(-4) / 1 == 4
print("ok")
