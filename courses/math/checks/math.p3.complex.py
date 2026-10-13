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

# ---- v2 additions ----
import random
from math import cos, sin, asin, acos, degrees
random.seed(3)
# warm-up
assert 36 - 100 == -64; eq("W2", cos(pi / 3), 0.5); eq("W2b", sin(2 * pi / 3), sqrt(3) / 2)
# proof 1: conjugate root theorem, random real cubic
for _ in range(5):
    a = [random.randint(-5, 5) for _ in range(4)]; w = complex(random.randint(-3, 3), random.randint(1, 3))
    p = lambda z: sum(c * z**k for k, c in enumerate(a))
    cx("conj poly", p(w.conjugate()), p(w).conjugate(), 1e-9)
# proof 2: product in polar form
for _ in range(5):
    r1, r2, al, be = random.uniform(.5, 3), random.uniform(.5, 3), random.uniform(-3, 3), random.uniform(-3, 3)
    z1, z2 = r1 * (cos(al) + 1j * sin(al)), r2 * (cos(be) + 1j * sin(be))
    cx("polar prod", z1 * z2, r1 * r2 * (cos(al + be) + 1j * sin(al + be)), 1e-9)
    cx("polar div", z1 / z2, r1 / r2 * (cos(al - be) + 1j * sin(al - be)), 1e-9)
# long example A
p = lambda z: z**3 - 4 * z**2 + 14 * z - 20
cx("A (1+3i)^2", (1 + 3j)**2, -8 + 6j); cx("A (1+3i)^3", (1 + 3j)**3, -26 - 18j); cx("A root", p(1 + 3j), 0, 1e-9)
cx("A conj", p(1 - 3j), 0, 1e-9); cx("A third", p(2), 0)
for z in (0.3 + 1j, 2 - 1.5j, 4): cx("A factor", p(z), (z * z - 2 * z + 10) * (z - 2), 1e-9)
assert 1 * 1 + 3 * 3 == 10 and 10 * -2 == -20 and 0.5 * 6 * 1 == 3
# long example B
x = 2 + sqrt(2); y = x - 1
eq("B circle", (x - 2)**2 + (y - 1)**2, 4); eq("B y", y, 1 + sqrt(2)); eq("B reject", sf(2 - sqrt(2), 2), 0.59); assert 2 - sqrt(2) < 1 < 2 + sqrt(2)
eq("B dist", sqrt(sqrt(2)**2 + sqrt(2)**2), 2, 1e-12); eq("B arg", cmath.phase(x + y * 1j - 1), pi / 4); eq("B max", sf(sqrt(5) + 2, 3), 4.24); eq("B max2", abs(2 + 1j) + 2, sqrt(5) + 2)
# spot the error
eq("SE r", abs(-2 + 2j), 2 * sqrt(2)); eq("SE arg", cmath.phase(-2 + 2j), 3 * pi / 4); cx("SE right", 2 * sqrt(2) * cmath.exp(3j * pi / 4), -2 + 2j)
cx("SE wrong", 2 * sqrt(2) * cmath.exp(-1j * pi / 4), 2 - 2j)
# exam practice
cx("E1", (4 - 3j) / (1 + 2j), -2 / 5 - 11 / 5 * 1j); cx("E1 num", (4 - 3j) * (1 - 2j), -2 - 11j)
for z in (3 + 4j, 3 - 4j): cx("E2", z * z - 6 * z + 25, 0, 1e-12)
cx("E3", (3 + 2j) * (2 - 1j), 8 + 1j); assert 2 * 3 + 2 == 8 and 2 * 2 - 3 == 1
q = lambda z: z**3 - 5 * z**2 + 7 * z + 13
cx("E4", q(3 - 2j), 0, 1e-12); cx("E4b", q(3 + 2j), 0, 1e-12); cx("E4c", q(-1), 0)
for z in (0.4 + 1j, 2): cx("E4 factor", q(z), (z * z - 6 * z + 13) * (z + 1), 1e-12)
cx("E5", (4 - 3j)**2, 7 - 24j); assert 16 - 9 == 7 and 2 * 4 * -3 == -24 and (16 - 16) == 0 and 16 * 9 == 144
z, w = 1 + sqrt(3) * 1j, -sqrt(3) + 1j
eq("E6 |z|", abs(z), 2); eq("E6 arg z", cmath.phase(z), pi / 3); eq("E6 |w|", abs(w), 2); eq("E6 arg w", cmath.phase(w), 5 * pi / 6)
eq("E6 |zw|", abs(z * w), 4); eq("E6 arg zw", cmath.phase(z * w), -5 * pi / 6); eq("E6 |z/w|", abs(z / w), 1); eq("E6 arg z/w", cmath.phase(z / w), -pi / 2)
eq("E6 7pi/6", 7 * pi / 6 - 2 * pi, -5 * pi / 6)
assert 4**2 + 3**2 == 25; eq("E7 phi", asin(3 / 5), atan(3 / 4)); eq("E7 greatest", sf(2 * atan(3 / 4), 3), 1.29); eq("E7 0.6435", sf(asin(3 / 5), 4), 0.6435)
eq("E7 max arg", max(cmath.phase(4 + 3j + 3 * cmath.exp(1j * t)) for t in [i * 2 * pi / 20000 for i in range(20000)]), 2 * atan(3 / 4), 1e-3)
eq("E7 min arg", min(cmath.phase(4 + 3j + 3 * cmath.exp(1j * t)) for t in [i * 2 * pi / 20000 for i in range(20000)]), 0, 1e-3)
# stretch
for k in (-1, 0, 1): cx("S1", cmath.exp(2j * pi * k / 3)**3, 1, 1e-12)
r = [cmath.exp(2j * pi * k / 3) for k in (-1, 0, 1)]
sides = [abs(r[i] - r[(i + 1) % 3]) for i in range(3)]; assert all(abs(s_ - sqrt(3)) < 1e-12 for s_ in sides)
eq("S1 area", sqrt(3) * sqrt(3) * sin(pi / 3) / 2, 3 * sqrt(3) / 4); eq("S1 3sf", sf(3 * sqrt(3) / 4, 3), 1.30); eq("S1 side", sqrt(1.5**2 + 3 / 4), sqrt(3))
for _ in range(5):
    t = random.uniform(-3, 3); z = cmath.exp(1j * t)
    cx("S2 a", z.conjugate(), 1 / z, 1e-12); w = (z - 1) / (z + 1); cx("S2 b", w.conjugate(), -w, 1e-12); eq("S2 re", w.real, 0, 1e-12)
z = (3 + 4j) / 5; eq("S2 |z|", abs(z), 1); cx("S2 d", (z - 1) / (z + 1), 0.5j, 1e-12); cx("S2 num", (-0.4 + 0.8j) * (1.6 - 0.8j), 1.6j, 1e-12)
print("ok")
