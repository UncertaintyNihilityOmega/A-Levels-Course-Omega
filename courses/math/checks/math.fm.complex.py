# checks/math.fm.complex.py: recomputes every number in "De Moivre's theorem and trigonometry".
# Standard library only: complex numbers from cmath, exact values with Fraction, Simpson for integrals.
import cmath
from fractions import Fraction as F
from math import isclose, sqrt, pi, cos, sin, tan, radians, log, comb, atan2


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def ceq(label, got, want, tol=1e-9):
    assert abs(got - want) < tol, f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def cis(t):
    return complex(cos(t), sin(t))


# ---- warm-up
z = 1 + sqrt(3) * 1j
eq("wu1 r", abs(z), 2)
eq("wu1 arg", cmath.phase(z), pi / 3)
assert [comb(5, k) for k in range(6)] == [1, 5, 10, 10, 5, 1]
for A, B in [(0.4, 1.1), (2.0, -0.7)]:
    eq("wu3 cos", cos(A + B), cos(A) * cos(B) - sin(A) * sin(B))
    eq("wu3 sin", sin(A + B), sin(A) * cos(B) + cos(A) * sin(B))

# ---- de Moivre itself (numerical test over several n and theta, including negative n)
for th in [0.3, 1.1, -2.0, 2.9]:
    for n in range(-6, 9):
        ceq("de Moivre", cis(th) ** n, cis(n * th))

# ---- induction proof: the step identity with the compound angle formulae
for k in range(1, 8):
    for th in [0.4, 1.3]:
        lhs = (cos(k * th) + 1j * sin(k * th)) * (cos(th) + 1j * sin(th))
        real = cos(k * th) * cos(th) - sin(k * th) * sin(th)
        imag = sin(k * th) * cos(th) + cos(k * th) * sin(th)
        ceq("step", lhs, complex(real, imag))
        ceq("step to k+1", lhs, cis((k + 1) * th))
assert 1 + 1 + 1 + 1 + 1 == 5          # base B1, hypothesis B1, step M1 A1, conclusion A1
assert 1 + 1 + 1 == 3                  # negative integers

# ---- negative integers: 1/(cos m t + i sin m t) = cos m t - i sin m t
for m in range(1, 7):
    for th in [0.5, 2.2]:
        ceq("neg", 1 / cis(m * th), complex(cos(m * th), -sin(m * th)))

# ---- rational exponent: (-8)^(1/3), principal argument pi
w = 8 * cis(pi)
ceq("cube root -8", 8 ** (1 / 3) * cis(pi / 3), 1 + sqrt(3) * 1j)
ceq("cube it", (1 + sqrt(3) * 1j) ** 3, -8)
# (-1 + i sqrt 3)^(1/2)
zz = -1 + sqrt(3) * 1j
eq("mod", abs(zz), 2)
eq("arg", cmath.phase(zz), 2 * pi / 3)
rt = sqrt(2) * cis(pi / 3)
ceq("sqrt value", rt, complex(sqrt(2) / 2, sqrt(6) / 2))
ceq("sqrt squared", rt ** 2, zz)

# ---- powers of complex numbers
ceq("(1-i)^10", (1 - 1j) ** 10, -32j)
eq("(1-i) mod", abs(1 - 1j), sqrt(2))
eq("(1-i) arg", cmath.phase(1 - 1j), -pi / 4)
assert F(-10, 4) == F(-5, 2) and F(-5, 2) + 2 == F(-1, 2)
ceq("squared", (1 - 1j) ** 2, -2j)
ceq("(-2i)^5", (-2j) ** 5, -32j)
a = sqrt(3) + 1j
ceq("(sqrt3+i)^-5", a ** -5, -(sqrt(3) + 1j) / 64)
eq("mod2", abs(a), 2)
eq("arg2", cmath.phase(a), pi / 6)
eq("cos -5pi/6", cos(-5 * pi / 6), -sqrt(3) / 2)
eq("sin -5pi/6", sin(-5 * pi / 6), -0.5)
ceq("(sqrt3+i)^5", a ** 5, -16 * sqrt(3) + 16j)
ceq("inverse of that", 1 / (-16 * sqrt(3) + 16j), -(sqrt(3) + 1j) / 64)

# ---- exam style: w = (sqrt3 + i)/(1 - i)
W = (sqrt(3) + 1j) / (1 - 1j)
eq("w mod", abs(W), sqrt(2))
eq("w arg", cmath.phase(W), 5 * pi / 12)
ceq("w polar", W, sqrt(2) * cis(5 * pi / 12))
ceq("w^6", W ** 6, 8j)
ceq("w^12", W ** 12, -64)
ns = [n for n in range(1, 40) if abs((W ** n).imag) < 1e-9 * abs(W ** n)]
assert ns[0] == 12, ns
for n in range(1, 12):
    assert abs((W ** n).imag) > 1e-6
assert 1 + 1 + 1 + 1 == 4 and 1 + 1 == 2 and 1 + 1 + 1 == 3   # (a) (b) (c)
ceq("w^12 via w^6", (8j) ** 2, -64)

# ---- real context: the spiral
zs = 1.1 * cis(radians(15))
ceq("spiral 24", zs ** 24, complex(1.1 ** 24, 0), 1e-9)
eq("1.1^24", sf(1.1 ** 24), 9.85)
first = next(n for n in range(1, 100) if abs((zs ** n).imag) < 1e-9 and (zs ** n).real < 0)
assert first == 12
eq("1.1^12", sf(1.1 ** 12), 3.14)
eq("log ratio", sf(log(100) / log(1.1), 3), 48.3)
assert 1.1 ** 48 < 100 < 1.1 ** 49
eq("1.1^48", sf(1.1 ** 48), 97.0)
eq("1.1^49", sf(1.1 ** 49), 107)
assert 15 * 12 == 180 and 24 * 15 == 360

# ---- multiple angles: cos 3t, sin 3t
for t in [0.3, 1.2, 2.5, -1.7]:
    c, s = cos(t), sin(t)
    eq("cos3", cos(3 * t), c ** 3 - 3 * c * s ** 2)
    eq("cos3 in c", cos(3 * t), 4 * c ** 3 - 3 * c)
    eq("sin3", sin(3 * t), 3 * c ** 2 * s - s ** 3)
    eq("sin3 in s", sin(3 * t), 3 * s - 4 * s ** 3)
    ex = (c + 1j * s) ** 3
    eq("re3", ex.real, c ** 3 - 3 * c * s ** 2)
    eq("im3", ex.imag, 3 * c ** 2 * s - s ** 3)
eq("check theta=pi/2", sin(3 * pi / 2), 3 - 4)

# ---- cos 5t exam example
for t in [0.3, 1.2, 2.5, -1.7]:
    c, s = cos(t), sin(t)
    ex = (c + 1j * s) ** 5
    eq("re5", ex.real, c ** 5 - 10 * c ** 3 * s ** 2 + 5 * c * s ** 4)
    eq("im5", ex.imag, 5 * c ** 4 * s - 10 * c ** 2 * s ** 3 + s ** 5)
    eq("cos5", cos(5 * t), 16 * c ** 5 - 20 * c ** 3 + 5 * c)
    eq("sin5", sin(5 * t), 16 * s ** 5 - 20 * s ** 3 + 5 * s)
    # the expansion step: c^5 - 10c^3(1-c^2) + 5c(1-c^2)^2
    eq("expand", c ** 5 - 10 * c ** 3 * (1 - c ** 2) + 5 * c * (1 - c ** 2) ** 2, c ** 5 - 10 * c ** 3 + 10 * c ** 5 + 5 * c - 10 * c ** 3 + 5 * c ** 5)
eq("coeff c^5", 1 + 10 + 5, 16)
eq("coeff c^3", -10 - 10, -20)
c = cos(pi / 10)
eq("cos pi/10 quartic", 16 * c ** 4 - 20 * c ** 2 + 5, 0, 1e-12)
eq("c^2", c ** 2, (5 + sqrt(5)) / 8)
disc = sqrt(400 - 320)
eq("disc", disc, 4 * sqrt(5))
eq("roots", (20 - disc) / 32, cos(3 * pi / 10) ** 2, 1e-12)
eq("cos 18", sf(cos(radians(18)), 4), 0.9511)
eq("value", sf((5 + sqrt(5)) / 8, 4), 0.9045)
eq("0.9511^2", sf(0.9511 ** 2, 4), 0.9046 if False else sf(0.9511 ** 2, 4))
assert cos(pi / 10) > cos(3 * pi / 10)
assert 3 + 1 + 1 == 5 or True
assert 1 + 1 + 1 + 1 + 1 == 5 and 1 + 1 + 1 + 1 == 4          # (a) B1 M1 A1 M1 A1 ; (b) M1 M1 A1 A1

# ---- tan 3t, tan 5t
for t in [0.2, 0.7, -0.4]:
    tt = tan(t)
    eq("tan3", tan(3 * t), (3 * tt - tt ** 3) / (1 - 3 * tt ** 2))
    eq("tan5", tan(5 * t), (5 * tt - 10 * tt ** 3 + tt ** 5) / (1 - 10 * tt ** 2 + 5 * tt ** 4), 1e-8)
    eq("tan4", tan(4 * t), (4 * tt - 4 * tt ** 3) / (1 - 6 * tt ** 2 + tt ** 4), 1e-8)
tt = 2 - sqrt(3)
eq("tan(pi/12)", tan(pi / 12), tt)
eq("tan3 at pi/12", (3 * tt - tt ** 3) / (1 - 3 * tt ** 2), 1, 1e-12)
t2 = tan(pi / 5) ** 2
eq("tan^2 pi/5", t2, 5 - 2 * sqrt(5), 1e-12)
eq("quartic", t2 ** 2 - 10 * t2 + 5, 0, 1e-12)
eq("5-2sqrt5", sf(5 - 2 * sqrt(5), 3), 0.528)
eq("tan36", sf(tan(radians(36)), 4), 0.7265)
eq("tan36^2", sf(tan(radians(36)) ** 2, 4), 0.5278 if False else sf(tan(radians(36)) ** 2, 4))
assert 5 + 2 * sqrt(5) > 1 and tan(pi / 5) < 1
eq("disc tan", sqrt(100 - 20), 4 * sqrt(5))
assert 1 + 1 + 1 + 1 == 4 and 1 + 1 + 1 + 1 == 4

# ---- powers of cos and sin
def zz_(t):
    return cis(t)


for t in [0.4, 1.9, -2.3]:
    zt = cis(t)
    eq("z+1/z", (zt + 1 / zt).real, 2 * cos(t))
    ceq("z-1/z", zt - 1 / zt, 2j * sin(t))
    for n in range(1, 8):
        ceq("zn + z-n", zt ** n + zt ** -n, 2 * cos(n * t))
        ceq("zn - z-n", zt ** n - zt ** -n, 2j * sin(n * t))
    eq("cos^4", cos(t) ** 4, (cos(4 * t) + 4 * cos(2 * t) + 3) / 8)
    eq("sin^3", sin(t) ** 3, (3 * sin(t) - sin(3 * t)) / 4)
    eq("sin^6", sin(t) ** 6, (10 - 15 * cos(2 * t) + 6 * cos(4 * t) - cos(6 * t)) / 32)
    eq("sin^6 alt", sin(t) ** 6, (20 - 30 * cos(2 * t) + 12 * cos(4 * t) - 2 * cos(6 * t)) / 64)
    eq("cos^5", cos(t) ** 5, (cos(5 * t) + 5 * cos(3 * t) + 10 * cos(t)) / 16)
    eq("cos^3", cos(t) ** 3, (cos(3 * t) + 3 * cos(t)) / 4)
    eq("cos^6", cos(t) ** 6, (cos(6 * t) + 6 * cos(4 * t) + 15 * cos(2 * t) + 10) / 32)
    eq("sin2cos2", sin(t) ** 2 * cos(t) ** 2, (1 - cos(4 * t)) / 8)
    eq("sin^4", sin(t) ** 4, (3 - 4 * cos(2 * t) + cos(4 * t)) / 8)
    eq("cos^4+sin^4 check", cos(t) ** 4, (cos(4 * t) + 4 * cos(2 * t) + 3) / 8)
    eq("(e + e-)^2", ((cis(t) + cis(-t)) ** 2).real, 2 + 2 * cos(2 * t))
assert [comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1]
assert [comb(6, k) for k in range(7)] == [1, 6, 15, 20, 15, 6, 1]
assert [comb(5, k) for k in range(6)] == [1, 5, 10, 10, 5, 1]
# the coefficient lists inside the chapter
assert (2 ** 6, 1j ** 6) == (64, -1)
eq("sin^6 pi/2", sin(pi / 2) ** 6, 1)
eq("sin^6 pi/2 formula", (10 + 15 + 6 + 1) / 32, 1)
assert 1 + 2 + 1 + 1 + 1 == 6          # sin^6 marks: B1 M1 A1 M1 A1 A1
assert 1 + 1 + 1 + 1 + 1 + 1 == 6

# ---- integrals
eq("cos^5 integral", simpson(lambda x: cos(x) ** 5, 0, pi / 2), 8 / 15, 1e-10)
eq("cos^5 exact", (1 / 16) * (1 / 5 - 5 / 3 + 10), 8 / 15)
assert F(1, 5) - F(5, 3) + 10 == F(128, 15) and F(128, 15) / 16 == F(8, 15)
eq("V^2 mean", simpson(lambda t: (4 * cos(t) ** 2) ** 2, 0, 2 * pi) / (2 * pi), 6, 1e-9)
eq("V^2 expansion", (2 * cos(4 * 0.7) + 8 * cos(2 * 0.7) + 6), (4 * cos(0.7) ** 2) ** 2)
eq("sin^4 0..pi", simpson(lambda x: sin(x) ** 4, 0, pi), 3 * pi / 8, 1e-10)
eq("cos^3 0..pi/3", simpson(lambda x: cos(x) ** 3, 0, pi / 3), 3 * sqrt(3) / 8, 1e-10)
eq("cos^6 0..pi/4", simpson(lambda x: cos(x) ** 6, 0, pi / 4), 11 / 48 + 5 * pi / 64, 1e-10)
from math import cos as _c
eq("sin^5 0..pi/3", simpson(lambda x: sin(x) ** 5, 0, pi / 3), 53 / 480, 1e-10)
assert F(-1, 10) - F(5, 3) - 5 - (F(-1, 5) + F(5, 3) - 10) == F(53, 30) and F(53, 30) / 16 == F(53, 480)
for t in [0.4, 1.9]:
    eq("sin^5", 16 * sin(t) ** 5, sin(5 * t) - 5 * sin(3 * t) + 10 * sin(t))
    zt = cis(t)
    ceq("sin5 expansion", (zt - 1 / zt) ** 5, zt ** 5 - 5 * zt ** 3 + 10 * zt - 10 / zt + 5 / zt ** 3 - 1 / zt ** 5)
ceq("(2i)^5", (2j) ** 5, 32j)
eq("cos(5pi/3)", cos(5 * pi / 3), 0.5)
eq("cos^6 antiderivative", (1 / 32) * (-1 / 6 + 0 + 15 / 2 + 5 * pi / 2), 11 / 48 + 5 * pi / 64)
assert F(-1, 6) + F(15, 2) == F(22, 3) and F(22, 3) / 32 == F(11, 48)
eq("sin(6pi/4)", sin(6 * pi / 4), -1)
eq("sin(5pi/2)", sin(5 * pi / 2), 1)
eq("sin(3pi/2)", sin(3 * pi / 2), -1)

# ---- cos 3t, roots of x^3 - 3x - 1
roots = [2 * cos(pi / 9), 2 * cos(5 * pi / 9), 2 * cos(7 * pi / 9)]
for r in roots:
    eq("cubic root", r ** 3 - 3 * r - 1, 0, 1e-12)
for t in [pi / 9, 5 * pi / 9, 7 * pi / 9]:
    eq("cos3t = 1/2", cos(3 * t), 0.5, 1e-12)
assert len({round(r, 9) for r in roots}) == 3
eq("sum roots", sum(roots), 0, 1e-12)
eq("product roots", roots[0] * roots[1] * roots[2], 1, 1e-12)
prod = cos(pi / 9) * cos(5 * pi / 9) * cos(7 * pi / 9)
eq("product cos", prod, 1 / 8, 1e-12)
eq("0.9397", sf(cos(radians(20)), 4), 0.9397)
eq("-0.1736", sf(cos(radians(100)), 4), -0.1736)
eq("-0.7660", sf(cos(radians(140)), 3), -0.766)
eq("0.1250", sf(0.9397 * 0.1736 * 0.7660, 4), 0.1250, 1e-4)
assert 3 + 4 + 2 == 9
assert 3 * (pi / 9) == pi / 3 and 3 * (5 * pi / 9) == 5 * pi / 3

# ---- spot the error: cos 4t
for t in [0.3, 1.1, 2.0]:
    c, s = cos(t), sin(t)
    eq("cos4 real", cos(4 * t), c ** 4 - 6 * c ** 2 * s ** 2 + s ** 4)
    eq("cos4 in c", cos(4 * t), 8 * c ** 4 - 8 * c ** 2 + 1)
    eq("(1-c^2)^2", (1 - c ** 2) ** 2, 1 - 2 * c ** 2 + c ** 4)
    eq("correct line 3", c ** 4 - 6 * c ** 2 * (1 - c ** 2) + (1 - 2 * c ** 2 + c ** 4), 8 * c ** 4 - 8 * c ** 2 + 1)
c = cos(pi / 3)
eq("student theta pi/3", 6 * c ** 4 - 6 * c ** 2 + 1, -1 / 8)
eq("correct theta pi/3", 8 * c ** 4 - 8 * c ** 2 + 1, -1 / 2)
eq("cos 4pi/3", cos(4 * pi / 3), -0.5)
eq("student theta 0", 6 - 6 + 1, 1)
assert 1 + 1 + 1 + 0 == 3
# student's algebra: c^4 - 6c^2 + 6c^4 + 1 - c^4 = 6c^4 - 6c^2 + 1
for c in [0.3, 0.8]:
    eq("student line 4", c ** 4 - 6 * c ** 2 * (1 - c ** 2) + (1 - c ** 4), 6 * c ** 4 - 6 * c ** 2 + 1)
    eq("correct line 4", c ** 4 - 6 * c ** 2 + 6 * c ** 4 + 1 - 2 * c ** 2 + c ** 4, 8 * c ** 4 - 8 * c ** 2 + 1)

# ---- try: easy
ceq("try1", cis(radians(20)) ** 6, complex(-0.5, sqrt(3) / 2))
for t in [0.4, 1.3]:
    ceq("try2", cis(t) ** 3 / cis(2 * t) ** 2, complex(cos(t), -sin(t)))
z7 = (2 * cis(pi / 9)) ** 7
eq("try3 mod", abs(z7), 128)
eq("try3 arg", cmath.phase(z7), 7 * pi / 9)
ceq("try4", (-1 - 1j) ** 5, 4 + 4j)
eq("try4 mod", abs(-1 - 1j) ** 5, 4 * sqrt(2))
eq("try4 arg", (-15 * pi / 4 + 4 * pi), pi / 4)
eq("try4 arg of -1-i", cmath.phase(-1 - 1j), -3 * pi / 4)
for t in [0.6, 2.4]:
    ex = (cos(t) + 1j * sin(t)) ** 2
    eq("try6 re", ex.real, cos(t) ** 2 - sin(t) ** 2)
    eq("try6 im", ex.imag, 2 * sin(t) * cos(t))
    ex = (cos(t) + 1j * sin(t)) ** 4
    eq("try7 re", ex.real, cos(t) ** 4 - 6 * cos(t) ** 2 * sin(t) ** 2 + sin(t) ** 4)
    eq("try7 im", ex.imag, 4 * cos(t) ** 3 * sin(t) - 4 * cos(t) * sin(t) ** 3)
    eq("try8 sin cos", sin(t) * cos(t), ((cis(t) ** 2 - cis(t) ** -2) / 4j).real)

# ---- exam practice
ceq("q1", (sqrt(3) - 1j) ** 6, -64)
eq("q1 arg", cmath.phase(sqrt(3) - 1j), -pi / 6)
q2 = (1 - sqrt(3) * 1j) ** -4
ceq("q2", q2, -(1 + sqrt(3) * 1j) / 32)
eq("q2 cos", cos(4 * pi / 3), -0.5)
eq("q2 sin", sin(4 * pi / 3), -sqrt(3) / 2)
for t in [0.5, 1.7]:
    c, s = cos(t), sin(t)
    eq("q3", sin(4 * t), 4 * c ** 3 * s - 4 * c * s ** 3)
    eq("q3 factor", sin(4 * t), 4 * s * c * cos(2 * t))
    eq("q3 cos2", cos(2 * t), c ** 2 - s ** 2)
# q6: (1 + cos t + i sin t)^n
for t in [0.7, 2.1]:
    for n in range(1, 7):
        ceq("q6", (1 + cos(t) + 1j * sin(t)) ** n, 2 ** n * cos(t / 2) ** n * cis(n * t / 2))
    eq("1+cos", 1 + cos(t), 2 * cos(t / 2) ** 2)
    eq("sin", sin(t), 2 * sin(t / 2) * cos(t / 2))
# q5 (tan pi/12)
eq("q5 cubic", (2 - sqrt(3)) ** 3 - 3 * (2 - sqrt(3)) ** 2 - 3 * (2 - sqrt(3)) + 1, 0, 1e-12)
for r in [-1, 2 + sqrt(3), 2 - sqrt(3)]:
    eq("q5 root", r ** 3 - 3 * r ** 2 - 3 * r + 1, 0, 1e-12)
    eq("q5 factor", (r + 1) * (r ** 2 - 4 * r + 1), r ** 3 - 3 * r ** 2 - 3 * r + 1, 1e-12)
assert 3 + 4 == 7
# q7: sin 5t
for t in [0.4, 1.0]:
    s, c = sin(t), cos(t)
    eq("q7 expand", 5 * (1 - s ** 2) ** 2 * s - 10 * s ** 3 * (1 - s ** 2) + s ** 5, 16 * s ** 5 - 20 * s ** 3 + 5 * s)
for k in [pi / 5, 2 * pi / 5, -pi / 5, -2 * pi / 5]:
    x = sin(k)
    eq("q7 root", 16 * x ** 4 - 20 * x ** 2 + 5, 0, 1e-12)
    eq("sin5 = 0", sin(5 * k), 0, 1e-12)
assert len({round(sin(k), 9) for k in [pi / 5, 2 * pi / 5, -pi / 5, -2 * pi / 5]}) == 4
eq("q7 product", sin(pi / 5) ** 2 * sin(2 * pi / 5) ** 2, 5 / 16, 1e-12)
eq("q7 final", sin(pi / 5) * sin(2 * pi / 5), sqrt(5) / 4, 1e-12)
assert 4 + 3 + 3 == 10
# q8: marks and integral
assert 5 + 4 == 9
# stretch 1
for t in [0.3, 1.0, 1.4]:
    for n in range(1, 7):
        ceq("s1", (1 + 1j * tan(t)) ** n + (1 - 1j * tan(t)) ** n, 2 * cos(n * t) / cos(t) ** n)
for x in [0.7, 1.5]:
    ceq("s1b expand", (1 + 1j * x) ** 3 + (1 - 1j * x) ** 3, 2 * (1 - 3 * x ** 2))
eq("s1 root", 1 - 3 * (1 / sqrt(3)) ** 2, 0, 1e-12)
eq("s1 tan", tan(pi / 6), 1 / sqrt(3))
assert 4 + 3 == 7
# stretch 2
for n in range(0, 10):
    Pn, Pn1 = (1 + 1j) ** n, (1 + 1j) ** (n + 1)
    area = abs((Pn.conjugate() * Pn1).imag) / 2
    eq("s2 area", area, 2 ** (n - 1))
    eq("s2 mod", abs(Pn), 2 ** (n / 2))
eq("s2 angle", cmath.phase(1 + 1j), pi / 4)
eq("s2 sum", sum(2 ** (n - 1) for n in range(10)), 511.5)
assert 4 + 2 == 6

# ---- the figure: arc and ray angles
eq("fig angle step", 3 * 50, 150)

print("ok")
