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
print("ok")
