# checks/math.p3.complex.py: recomputes every number in the Complex numbers chapter.
import cmath
from math import isclose, sqrt, pi, atan, atan2

def eq(label, got, want, tol=1e-9):
    assert abs(got - want) <= tol, f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def cx(label, got, want, tol=1e-9): eq(label, got.real, want.real, tol); eq(label, got.imag, want.imag, tol)

# arithmetic
z1, z2 = 3 + 2j, 1 - 4j
cx("sum", z1 + z2, 4 - 2j); cx("diff", z1 - z2, 2 + 6j); cx("prod", z1 * z2, 11 - 10j)
cx("div", (5 + 1j) / (2 - 1j), 9 / 5 + 7 / 5 * 1j); cx("num", (5 + 1j) * (2 + 1j), 9 + 7j)
# equate
a, b = 3, -1; cx("a+ib", (a + b * 1j) * (1 + 2j), 5 + 5j); eq("a-2b", a - 2 * b, 5); eq("2a+b", 2 * a + b, 5)
z = 2 + 4j; cx("z+2z*", z + 2 * z.conjugate(), 6 - 4j)
# roots
for r in (2 + 3j, 2 - 3j): cx("quad", r * r - 4 * r + 13, 0)
cx("disc", (4 + cmath.sqrt(16 - 52)) / 2, 2 + 3j)
f = lambda z: z**3 - 6 * z**2 + 13 * z - 10
for r in (2, 2 + 1j, 2 - 1j): cx("cubic", f(r), 0)
for zz in (0.3 + 1j, -2 + 0.5j): cx("factor", f(zz), (zz - 2) * (zz * zz - 4 * zz + 5))
# argand
w = -1 + sqrt(3) * 1j
eq("|w|", abs(w), 2); eq("arg w", cmath.phase(w), 2 * pi / 3); eq("2.09", sf(cmath.phase(w)), 2.09)
v = -2 - 2j; eq("|v|", abs(v), 2 * sqrt(2)); eq("arg v", cmath.phase(v), -3 * pi / 4); eq("-2.36", sf(cmath.phase(v)), -2.36)
# polar
p1, p2 = 1 + 1j, -1 + sqrt(3) * 1j
eq("|p1|", abs(p1), sqrt(2)); eq("a1", cmath.phase(p1), pi / 4)
eq("|prod|", abs(p1 * p2), 2 * sqrt(2)); eq("arg prod", cmath.phase(p1 * p2), 11 * pi / 12); eq("2.88", sf(cmath.phase(p1 * p2)), 2.88)
eq("|quot|", abs(p1 / p2), sqrt(2) / 2); eq("arg quot", cmath.phase(p1 / p2), -5 * pi / 12); eq("-1.31", sf(cmath.phase(p1 / p2)), -1.31)
# roots
cx("sqrt", (3 + 2j)**2, 5 + 12j); cx("(x2-9)(x2+4)", (3**2 - 9) * (3**2 + 4), 0 + 0j)
for x in (1.5, 2.0): eq("quartic", (x**4 - 5 * x * x - 36), (x * x - 9) * (x * x + 4))
# loci
for x in (-1.0, 0.0, 2.0, 5.0): eq("y=x", abs(complex(x, x) - 1), abs(complex(x, x) - 1j))
eq("circle", abs(5 + 2j - (3 + 2j)), 2)
eq("area", 0.5 * pi * 4, 2 * pi)
# impedance
Z1, Z2 = 3 + 4j, 1 - 2j
cx("Z1Z2", Z1 * Z2, 11 - 2j); cx("sum", Z1 + Z2, 4 + 2j)
Z = Z1 * Z2 / (Z1 + Z2); cx("Z", Z, 2 - 1.5j); cx("par", 1 / Z, 1 / Z1 + 1 / Z2)
cx("num", (11 - 2j) * (4 - 2j), 40 - 30j); eq("|Z|", abs(Z), 2.5); eq("argZ", sf(cmath.phase(Z)), -0.644); eq("atan", atan(-1.5 / 2), cmath.phase(Z))

# try
cx("T1", (2 + 3j) * (4 - 1j), 11 + 10j); cx("T2", (7 + 1j) / (1 + 1j), 4 - 3j)
for r in (-1 + 3j, -1 - 3j): cx("T3", r * r + 2 * r + 10, 0)
t4 = -sqrt(3) - 1j; eq("T4", abs(t4), 2); eq("T4 arg", cmath.phase(t4), -5 * pi / 6); eq("T4 sf", sf(cmath.phase(t4)), -2.62)
cx("T5", (3 + 1j)**2, 8 + 6j); eq("T5 q", (3**2 - 9) * (3**2 + 1), 0)
c1, c2 = 3 * cmath.exp(1j * pi / 6), 2 * cmath.exp(1j * pi / 3)
cx("T6 prod", c1 * c2, 6j); cx("T6 quot", c1 / c2, 1.5 * cmath.exp(-1j * pi / 6))
z7 = 3 + 2j; cx("T7", z7 + 2 * z7.conjugate(), 9 - 2j)
for x in (-1.0, 0.0, 3.0): eq("T8", abs(complex(x, -x) - 2), abs(complex(x, -x) + 2j))
f9 = lambda z: z**3 - 5 * z**2 + 11 * z - 15
eq("T9", 27 - 45 + 33 - 15, 0)
for r in (3, 1 + 2j, 1 - 2j): cx("T9 roots", f9(r), 0)
cx("T9 fac", f9(0.7 + 0.2j), (0.7 + 0.2j - 3) * ((0.7 + 0.2j)**2 - 2 * (0.7 + 0.2j) + 5))
# quiz
cx("Q1", (1 + 1j)**2, 2j); cx("Q2", (3 - 4j) * (3 + 4j), 25 + 0j); eq("Q3", cmath.phase(-1 - 1j), -3 * pi / 4)
print("ok")
