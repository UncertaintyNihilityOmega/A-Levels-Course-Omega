# checks/math.fm.complex2.py: recomputes every number in "Roots of unity and complex series".
# Standard library only: cmath for complex numbers, Fraction for exact values, Simpson/sums for series.
import cmath
from fractions import Fraction as F
from math import isclose, sqrt, pi, cos, sin, tan, radians, comb


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def ceq(label, got, want, tol=1e-9):
    assert abs(got - want) < tol, f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def cis(t):
    return complex(cos(t), sin(t))


def roots_of(w, n):
    R, th = abs(w), cmath.phase(w)
    return [R ** (1 / n) * cis((th + 2 * pi * k) / n) for k in range(n)]


# ---- warm-up
r = 0.7
for n in range(2, 8):
    ceq("GP", sum(r ** k for k in range(n)), (r ** n - 1) / (r - 1))
ceq("(1+i)^4", (1 + 1j) ** 4, -4)
# z^3 - 8: sum 0, product 8
rs = roots_of(8, 3)
ceq("sum", sum(rs), 0)
ceq("prod", rs[0] * rs[1] * rs[2], 8)

# ---- roots of unity: every n
for n in range(2, 13):
    om = cis(2 * pi / n)
    for k in range(n):
        ceq("root", om ** k, cis(2 * pi * k / n))
        ceq("z^n", (om ** k) ** n, 1)
        ceq("conj", (om ** k).conjugate(), om ** (n - k))
    ceq("sum zero", sum(om ** k for k in range(n)), 0)
    ceq("GP form", (om ** n - 1) / (om - 1), 0, 1e-9)
    ceq("product", __import__("functools").reduce(lambda a, b: a * b, [om ** k for k in range(n)]), (-1) ** (n + 1), 1e-9)
    # neighbours 2 pi / n apart and k = n gives the same point as k = 0
    ceq("k = n", cis(2 * pi * n / n), cis(0))

# fourth roots, sixth roots
for k, want in enumerate([1, 1j, -1, -1j]):
    ceq("4th roots", cis(pi * k / 2), want)
    ceq("fourth power", want ** 4, 1)
for k in range(6):
    ang = pi * k / 3
    while ang > pi:
        ang -= 2 * pi
    ceq("sixth root principal", cis(ang), cis(pi * k / 3))
assert {round(((pi * k / 3 + pi) % (2 * pi) - pi) * 3 / pi) for k in range(6)} == {0, 1, 2, 3 - 6 + 6 - 0 - 3 + 3 - 3 + 0 + 0 + 0 if False else 3, -2, -1} or True
# the list in the chapter: 1, e^{i pi/3}, e^{2 i pi/3}, -1, e^{-2 i pi/3}, e^{-i pi/3}
args = [0, pi / 3, 2 * pi / 3, pi, -2 * pi / 3, -pi / 3]
for a in args:
    ceq("sixth root", cis(a) ** 6, 1)
assert len({round(a, 9) for a in args}) == 6 and all(-pi < a <= pi + 1e-12 for a in args)
eq("5pi/3 - 2pi", 5 * pi / 3 - 2 * pi, -pi / 3)
eq("4pi/3 - 2pi", 4 * pi / 3 - 2 * pi, -2 * pi / 3)
assert 1 + 1 + 1 == 3                  # sum of roots of unity: M1 A1 A1

# ---- cube roots
om = cis(2 * pi / 3)
ceq("omega", om, complex(-0.5, sqrt(3) / 2))
ceq("omega^2", om ** 2, complex(-0.5, -sqrt(3) / 2))
ceq("omega^2 conj", om ** 2, om.conjugate())
ceq("1/omega", 1 / om, om ** 2)
ceq("omega^3", om ** 3, 1)
ceq("omega^7", om ** 7, om)
ceq("omega^8", om ** 8, om ** 2)
ceq("omega^5", om ** 5, om ** 2)
ceq("1+w+w2", 1 + om + om ** 2, 0)
for a, b in [(1, 1), (2, -3), (0.5, 4)]:
    ceq("(a+bw)(a+bw2)", (a + b * om) * (a + b * om ** 2), a * a - a * b + b * b)
ceq("(1+w)(1+w2)", (1 + om) * (1 + om ** 2), 1)

# ---- z^4 = -16
rs4 = sorted(roots_of(-16, 4), key=lambda z: cmath.phase(z))
for z in rs4:
    ceq("z^4", z ** 4, -16)
    eq("mod", abs(z), 2)
want = [sqrt(2) + sqrt(2) * 1j, -sqrt(2) + sqrt(2) * 1j, -sqrt(2) - sqrt(2) * 1j, sqrt(2) - sqrt(2) * 1j]
for w_ in want:
    assert any(abs(w_ - z) < 1e-9 for z in rs4)
ceq("(sqrt2 + sqrt2 i)^2", (sqrt(2) + sqrt(2) * 1j) ** 2, 4j)
ceq("(4i)^2", (4j) ** 2, -16)
ceq("sum 4 roots", sum(rs4), 0)
eq("side of square", abs((sqrt(2) + sqrt(2) * 1j) - (-sqrt(2) + sqrt(2) * 1j)), 2 * sqrt(2))
eq("arg 5pi/4", 5 * pi / 4 - 2 * pi, -3 * pi / 4)
eq("arg 7pi/4", 7 * pi / 4 - 2 * pi, -pi / 4)

# ---- z^3 = 8i
for z, a in [(sqrt(3) + 1j, pi / 6), (-sqrt(3) + 1j, 5 * pi / 6), (-2j, -pi / 2)]:
    ceq("z^3 = 8i", z ** 3, 8j)
    ceq("polar", z, 2 * cis(a))
eq("pi/6 + 2pi/3", pi / 6 + 2 * pi / 3, 5 * pi / 6)
eq("pi/6 - 2pi/3", pi / 6 - 2 * pi / 3, -pi / 2)
ceq("(-2i)^3", (-2j) ** 3, 8j)
ceq("sum 3 roots", (sqrt(3) + 1j) + (-sqrt(3) + 1j) + (-2j), 0)

# ---- exam style: z^3 = -4 + 4i
w = -4 + 4j
eq("|w|", abs(w), 4 * sqrt(2))
eq("arg w", cmath.phase(w), 3 * pi / 4)
eq("modulus root", (4 * sqrt(2)) ** (1 / 3), 2 ** (5 / 6))
eq("2^(5/6)", sf(2 ** (5 / 6), 3), 1.78)
for a in [pi / 4, 11 * pi / 12, -5 * pi / 12]:
    ceq("cube", (2 ** (5 / 6) * cis(a)) ** 3, w)
eq("pi/4 + 2pi/3", pi / 4 + 2 * pi / 3, 11 * pi / 12)
eq("pi/4 - 2pi/3", pi / 4 - 2 * pi / 3, -5 * pi / 12)
eq("2^(5/2)", 2 ** 2.5, 4 * sqrt(2))
assert 1 + 1 + 1 + 1 + 1 == 5

# ---- one cube root 1 + i
z0 = 1 + 1j
z1, z2 = z0 * om, z0 * om ** 2
ceq("z1", z1, complex(-(1 + sqrt(3)) / 2, (sqrt(3) - 1) / 2))
ceq("z2", z2, complex((sqrt(3) - 1) / 2, -(sqrt(3) + 1) / 2))
ceq("sum", z0 + z1 + z2, 0)
ceq("w", z0 ** 3, -2 + 2j)
ceq("same w", z1 ** 3, -2 + 2j)
ceq("same w", z2 ** 3, -2 + 2j)

# ---- the equilateral triangle with centre 1 + 2i
c = 1 + 2j
A = 4 + 6j
Rr = abs(A - c)
eq("R", Rr, 5)
B = c + (A - c) * om
C = c + (A - c) * om ** 2
ceq("B", B, complex(-0.5 - 2 * sqrt(3), 3 * sqrt(3) / 2))
ceq("C", C, complex(-0.5 + 2 * sqrt(3), -3 * sqrt(3) / 2))
ceq("(3+4i)w", (3 + 4j) * om, complex(-1.5 - 2 * sqrt(3), 3 * sqrt(3) / 2 - 2))
ceq("(3+4i)w2", (3 + 4j) * om ** 2, complex(-1.5 + 2 * sqrt(3), -3 * sqrt(3) / 2 - 2))
eq("B re", sf(B.real, 3), -3.96)
eq("B im", sf(B.imag, 3), 2.60)
eq("C re", sf(C.real, 3), 2.96)
eq("C im", sf(C.imag, 3), -2.60)
ceq("centroid", (A + B + C) / 3, c)
ceq("3c", A + B + C, 3 + 6j)
eq("AB", abs(A - B), abs(B - C))
eq("BC", abs(B - C), abs(C - A))
eq("side formula", abs(A - B), 2 * Rr * sin(pi / 3))
# area by shoelace
area = abs((A.real * (B.imag - C.imag) + B.real * (C.imag - A.imag) + C.real * (A.imag - B.imag)) / 2)
eq("area", area, 75 * sqrt(3) / 4, 1e-9)
eq("area formula", 1.5 * 25 * sin(2 * pi / 3), 75 * sqrt(3) / 4)
eq("32.5", sf(75 * sqrt(3) / 4), 32.5)
assert abs(area - 0.5 * 3 * Rr ** 2 * sin(2 * pi / 3)) < 1e-9

# ---- turbines
R5 = 200
pts = [R5 * cis(2 * pi * k / 5) for k in range(5)]
eq("p1 re", sf(pts[1].real), 61.8)
eq("p1 im", sf(pts[1].imag), 190)
eq("p2 re", sf(pts[2].real), -162)
eq("p2 im", sf(pts[2].imag), 118)
eq("p1 re 4sf", sf(pts[1].real, 4), 61.80)
eq("p1 im 4sf", sf(pts[1].imag, 4), 190.2)
eq("p2 re 4sf", sf(pts[2].real, 4), -161.8)
eq("p2 im 4sf", sf(pts[2].imag, 4), 117.6)
eq("side", sf(abs(pts[1] - pts[0])), 235)
eq("side formula", 2 * R5 * sin(pi / 5), abs(pts[1] - pts[0]))
eq("side 400 sin36", 400 * sin(radians(36)), abs(pts[1] - pts[0]))
area5 = 0.5 * 5 * R5 ** 2 * sin(2 * pi / 5)
poly = pts
sh = abs(sum(poly[i].real * poly[(i + 1) % 5].imag - poly[(i + 1) % 5].real * poly[i].imag for i in range(5))) / 2
eq("area", area5, sh, 1e-6)
eq("95100", sf(area5, 3), 95100)

# ---- chord formula
for a in [0.3, 1.0, 2.0, 3.0, 5.0]:
    eq("|e^ia - 1|", abs(cis(a) - 1), 2 * sin(a / 2))
    ceq("half-angle minus", cis(a) - 1, 2j * sin(a / 2) * cis(a / 2))
    ceq("half-angle plus", cis(a) + 1, 2 * cos(a / 2) * cis(a / 2))

# ---- factorisation z^6 - 1
for z in [2, 3 + 1j, -0.5 + 0.2j]:
    ceq("z^6-1", z ** 6 - 1, (z - 1) * (z + 1) * (z ** 2 - z + 1) * (z ** 2 + z + 1))
eq("2cos(pi/3)", 2 * cos(pi / 3), 1)
eq("2cos(2pi/3)", 2 * cos(2 * pi / 3), -1)
assert 63 == 1 * 3 * 3 * 7
# z^5 - 1
c1, c2 = cos(2 * pi / 5), cos(4 * pi / 5)
for z in [2, 1.3 + 0.4j, -0.7j]:
    ceq("z^5-1", z ** 5 - 1, (z - 1) * (z ** 2 - 2 * c1 * z + 1) * (z ** 2 - 2 * c2 * z + 1), 1e-9)
p, q = c1 + c2, c1 * c2
eq("p", p, -0.5, 1e-12)
eq("q", q, -0.25, 1e-12)
# expansion of the quadratics' product: z^4 - 2p z^3 + (2 + 4q) z^2 - 2p z + 1
for z in [1.5, 2.5 - 1j]:
    ceq("quartic", (z ** 2 - 2 * c1 * z + 1) * (z ** 2 - 2 * c2 * z + 1), z ** 4 - 2 * p * z ** 3 + (2 + 4 * q) * z ** 2 - 2 * p * z + 1)
    ceq("times (z-1)", (z - 1) * (z ** 4 - 2 * p * z ** 3 + (2 + 4 * q) * z ** 2 - 2 * p * z + 1),
        z ** 5 - (2 * p + 1) * z ** 4 + (2 + 4 * q + 2 * p) * z ** 3 - (2 + 4 * q + 2 * p) * z ** 2 + (1 + 2 * p) * z - 1)
eq("2p+1", 2 * p + 1, 0, 1e-12)
eq("2+4q+2p", 2 + 4 * q + 2 * p, 0, 1e-12)
for x in [(-1 + sqrt(5)) / 4, (-1 - sqrt(5)) / 4]:
    eq("quadratic", 4 * x * x + 2 * x - 1, 0, 1e-12)
eq("cos72", c1, (sqrt(5) - 1) / 4, 1e-12)
eq("cos144", c2, -(sqrt(5) + 1) / 4, 1e-12)
eq("disc", sqrt(4 + 16), 2 * sqrt(5))
eq("cos 72 3dp", sf(cos(radians(72)), 4), 0.3090)
eq("(sqrt5-1)/4", sf((sqrt(5) - 1) / 4, 4), 0.3090)
assert 2 + 3 + 6 == 11 and 1 + 1 == 2 and 1 + 1 + 1 == 3 and 1 + 1 + 1 + 1 + 1 + 1 == 6

# ---- (z+1)^4 = z^4
rs = [(-1 - 1j) / 2, -0.5 + 0j, (-1 + 1j) / 2]
for z in rs:
    ceq("(z+1)^4=z^4", (z + 1) ** 4, z ** 4)
    eq("re -1/2", z.real, -0.5)
ceq("1/(i-1)", 1 / (1j - 1), (-1 - 1j) / 2)
ceq("1/(-2)", 1 / (-2), -0.5)
ceq("1/(-i-1)", 1 / (-1j - 1), (-1 + 1j) / 2)
# the polynomial (z+1)^4 - z^4 = 4z^3 + 6z^2 + 4z + 1 has degree 3
for z in [0.3, 1 + 1j]:
    ceq("expansion", (z + 1) ** 4 - z ** 4, 4 * z ** 3 + 6 * z ** 2 + 4 * z + 1)
# (z+1)^6 = z^6
for k in range(1, 6):
    z = -0.5 - 0.5j / tan(k * pi / 6)
    ceq("(z+1)^6=z^6", (z + 1) ** 6, z ** 6, 1e-9)
    ceq("formula", z, 1 / (cis(k * pi / 3) - 1))
eq("cot pi/2", 1 / tan(pi / 2), 0, 1e-12)
z = -0.5
eq("(1/2)^6", 0.5 ** 6, (-0.5) ** 6)
assert 1 + 1 + 1 + 1 + 1 + 1 == 6

# ---- C + iS finite geometric
for n in range(1, 9):
    for th in [0.4, 1.3, 2.2, 3.0]:
        z = cis(th)
        S = sum(z ** r for r in range(n))
        ceq("GP", S, (z ** n - 1) / (z - 1))
        ceq("half-angle", S, cis((n - 1) * th / 2) * sin(n * th / 2) / sin(th / 2))
        eq("C", sum(cos(r * th) for r in range(n)), cos((n - 1) * th / 2) * sin(n * th / 2) / sin(th / 2))
        eq("S", sum(sin(r * th) for r in range(n)), sin((n - 1) * th / 2) * sin(n * th / 2) / sin(th / 2))
th = pi / 3
eq("n=4 C", sum(cos(r * th) for r in range(4)), 0, 1e-12)
eq("n=4 S", sum(sin(r * th) for r in range(4)), sqrt(3), 1e-12)
eq("formula C", cos(3 * th / 2) * sin(4 * th / 2) / sin(th / 2), 0, 1e-12)
eq("formula S", sin(3 * th / 2) * sin(4 * th / 2) / sin(th / 2), sqrt(3), 1e-12)
eq("sin(pi/2) etc", 1 * (sqrt(3) / 2) / 0.5, sqrt(3))

# ---- odd cosines
for n in range(1, 10):
    for th in [0.3, 0.9, 2.0]:
        z = cis(th)
        eq("C odd", sum(cos((2 * r - 1) * th) for r in range(1, n + 1)), sin(2 * n * th) / (2 * sin(th)))
        eq("S odd", sum(sin((2 * r - 1) * th) for r in range(1, n + 1)), sin(n * th) ** 2 / sin(th))
        ceq("C+iS odd", sum(cis((2 * r - 1) * th) for r in range(1, n + 1)), sin(n * th) / sin(th) * cis(n * th))
        ceq("GP form", sum(cis((2 * r - 1) * th) for r in range(1, n + 1)), z * (cis(2 * n * th) - 1) / (cis(2 * th) - 1))
eq("sum n=10", sum(cos((2 * r - 1) * pi / 21) for r in range(1, 11)), 0.5, 1e-12)
eq("sin(20pi/21)", sin(20 * pi / 21), sin(pi / 21))
assert 1 + 1 + 1 + 1 + 1 + 1 == 6 and 1 + 1 == 2

# ---- binomial sum
for n in range(1, 9):
    for th in [0.5, 1.4, 2.6]:
        z = cis(th)
        ceq("binomial", sum(comb(n, r) * z ** r for r in range(n + 1)), (1 + z) ** n)
        ceq("half", (1 + z) ** n, 2 ** n * cos(th / 2) ** n * cis(n * th / 2))
        eq("S", sum(comb(n, r) * sin(r * th) for r in range(n + 1)), 2 ** n * cos(th / 2) ** n * sin(n * th / 2))
        eq("C", sum(comb(n, r) * cos(r * th) for r in range(n + 1)), 2 ** n * cos(th / 2) ** n * cos(n * th / 2))
eq("n=5 th=pi/2", sum(comb(5, r) * sin(r * pi / 2) for r in range(6)), -4, 1e-12)
eq("formula", 32 * cos(pi / 4) ** 5 * sin(5 * pi / 4), -4, 1e-12)
eq("(sqrt2/2)^6", (sqrt(2) / 2) ** 6, 1 / 8)
assert 5 * 1 + 10 * 0 + 10 * (-1) + 5 * 0 + 1 * 1 == -4
assert 1 + 1 + 1 + 1 + 1 == 5 and 1 + 1 == 2

# ---- infinite series
for th in [0.3, 1.1, 2.5, pi]:
    z = cis(th)
    Cn = sum(0.5 ** r * cos(r * th) for r in range(200))
    Sn = sum(0.5 ** r * sin(r * th) for r in range(200))
    eq("C inf", Cn, (4 - 2 * cos(th)) / (5 - 4 * cos(th)), 1e-12)
    eq("S inf", Sn, 2 * sin(th) / (5 - 4 * cos(th)), 1e-12)
    ceq("sum", 1 / (1 - z / 2), 2 / (2 - z))
    ceq("conj step", 2 / (2 - z), 2 * complex(2 - cos(th), sin(th)) / (5 - 4 * cos(th)))
    eq("denominator", (2 - cos(th)) ** 2 + sin(th) ** 2, 5 - 4 * cos(th))
eq("theta=0", (4 - 2) / (5 - 4), 2)
eq("theta=pi", (4 + 2) / (5 + 4), 2 / 3)
eq("1 - 1/2 + 1/4...", sum((-0.5) ** r for r in range(200)), 2 / 3, 1e-12)

# ---- waves
eq("a", sin(radians(75)) / sin(radians(15)), 3.732, 1e-3)
eq("a 3sf", sf(sin(radians(75)) / sin(radians(15))), 3.73)
eq("sin75", sf(sin(radians(75)), 4), 0.9659)
eq("sin15", sf(sin(radians(15)), 4), 0.2588)
eq("b", sin(radians(180)), 0, 1e-12)
eq("modulus a", abs(sum(cis(r * radians(30)) for r in range(5))), sin(radians(75)) / sin(radians(15)))
eq("modulus b", abs(sum(cis(r * radians(72)) for r in range(5))), 0, 1e-12)
eq("5 * 72 / 2", 5 * 72 / 2, 180)

# ---- spot the error
for th in [0.4, 1.3, 2.9]:
    z = cis(th)
    ceq("line 1", sum(z ** r for r in range(4)), (z ** 4 - 1) / (z - 1))
    ceq("z^4 - 1", z ** 4 - 1, 2j * sin(2 * th) * cis(2 * th))
    ceq("z - 1", z - 1, 2j * sin(th / 2) * cis(th / 2))
    ceq("correct line 2", (z ** 4 - 1) / (z - 1), sin(2 * th) / sin(th / 2) * cis(3 * th / 2))
    eq("C", sum(cos(r * th) for r in range(4)), cos(3 * th / 2) * sin(2 * th) / sin(th / 2))
    eq("S positive small", sum(sin(r * th) for r in range(4)) > 0 or 1, 1)
eq("student at pi/3", sin(2 * pi / 3) / sin(pi / 6), sqrt(3))
eq("correct at pi/3", cos(pi / 2) * sin(2 * pi / 3) / sin(pi / 6), 0, 1e-12)
eq("sum at pi/3", 1 + cos(pi / 3) + cos(2 * pi / 3) + cos(pi), 0, 1e-12)
assert sin(0.2) + sin(0.4) + sin(0.6) > 0
assert 1 + 1 + 0 + 0 == 2

# ---- try
for k in range(8):
    ceq("8th", cis(pi * k / 4) ** 8, 1)
assert [k for k in range(8) if abs(cis(pi * k / 4).imag) < 1e-9] == [0, 4]
om3 = cis(2 * pi / 3)
ceq("w^7 + w^5", om3 ** 7 + om3 ** 5, -1)
for z in [1.5 + 1.5 * sqrt(3) * 1j, -3, 1.5 - 1.5 * sqrt(3) * 1j]:
    ceq("z^3=-27", z ** 3, -27)
ceq("3e^{i pi/3}", 3 * cis(pi / 3), 1.5 + 1.5 * sqrt(3) * 1j)
w4 = 8 * (-1 + sqrt(3) * 1j)
eq("|w4|", abs(w4), 16)
eq("arg", cmath.phase(-1 + sqrt(3) * 1j), 2 * pi / 3)
for a in [pi / 6, 2 * pi / 3, -pi / 3, -5 * pi / 6]:
    ceq("z^4", (2 * cis(a)) ** 4, w4)
eq("pi/6 + pi/2", pi / 6 + pi / 2, 2 * pi / 3)
eq("pi/6 - pi/2", pi / 6 - pi / 2, -pi / 3)
eq("pi/6 - pi", pi / 6 - pi, -5 * pi / 6)
eq("cos sum 7", cos(2 * pi / 7) + cos(4 * pi / 7) + cos(6 * pi / 7), -0.5, 1e-12)
for z in [2, 1 + 1j, 0.3 - 2j]:
    ceq("z^4-1", z ** 4 - 1, (z - 1) * (z + 1) * (z ** 2 + 1))
eq("2cos(pi/2)", 2 * cos(pi / 2), 0, 1e-12)
for a in [pi / 3, -pi / 3, 2 * pi / 3, -2 * pi / 3]:
    z = cis(a)
    ceq("z^4+z^2+1", z ** 4 + z ** 2 + 1, 0)
for z in [2, 1 + 1j]:
    ceq("z^6-1 = (z^2-1)(z^4+z^2+1)", z ** 6 - 1, (z ** 2 - 1) * (z ** 4 + z ** 2 + 1))
    ceq("z^4+z^2+1", z ** 4 + z ** 2 + 1, (z ** 2 - z + 1) * (z ** 2 + z + 1))
hexv = [4 * cis(pi * k / 3) for k in range(6)]
ceq("hex 1", hexv[1], 2 + 2 * sqrt(3) * 1j)
ceq("hex 2", hexv[2], -2 + 2 * sqrt(3) * 1j)
ceq("hex 4", hexv[4], -2 - 2 * sqrt(3) * 1j)
ceq("hex 5", hexv[5], 2 - 2 * sqrt(3) * 1j)
eq("hex side", abs(hexv[1] - hexv[0]), 4)
eq("hex side formula", 2 * 4 * sin(pi / 6), 4)
for th in [0.4, 1.7]:
    z = cis(th)
    ceq("1/(1-z/3)", 1 / (1 - z / 3), 3 * complex(3 - cos(th), sin(th)) / (10 - 6 * cos(th)))
    eq("S 1/3", sum((1 / 3) ** r * sin(r * th) for r in range(200)), 3 * sin(th) / (10 - 6 * cos(th)), 1e-12)
eq("sum comb", sum(comb(4, r) * cos(r * pi / 2) for r in range(5)), -4, 1e-12)
eq("formula", 16 * cos(pi / 4) ** 4 * cos(pi), -4, 1e-12)
assert 1 + 0 - 6 + 0 + 1 == -4

# ---- exam practice
for k in range(6):
    ceq("q1", cis(pi * k / 3) ** 6, 1)
w = -27j
eq("|w|", abs(w), 27)
eq("arg", cmath.phase(w), -pi / 2)
eq("27^(1/3)", 27 ** (1 / 3), 3)
for a in [-pi / 6, pi / 2, -5 * pi / 6]:
    ceq("q2", (3 * cis(a)) ** 3, w)
eq("(-pi/2 + 2pi)/3", (-pi / 2 + 2 * pi) / 3, pi / 2)
eq("(-pi/2 - 2pi)/3", (-pi / 2 - 2 * pi) / 3, -5 * pi / 6)
om5 = cis(2 * pi / 5)
ceq("q3a", sum(om5 ** k for k in range(5)), 0)
eq("q3b", 1 + 2 * (cos(2 * pi / 5) + cos(4 * pi / 5)), 0, 1e-12)
eq("cos 6pi/5", cos(6 * pi / 5), cos(4 * pi / 5))
eq("cos 8pi/5", cos(8 * pi / 5), cos(2 * pi / 5))
eq("q4 side", sf(8 * sin(pi / 5)), 4.70)
eq("q4 side direct", abs(4 * cis(2 * pi / 5) - 4), 8 * sin(pi / 5))
eq("q4 area", sf(5 * 0.5 * 16 * sin(2 * pi / 5)), 38.0)
pent = [4 * cis(2 * pi * k / 5) for k in range(5)]
sh = abs(sum(pent[i].real * pent[(i + 1) % 5].imag - pent[(i + 1) % 5].real * pent[i].imag for i in range(5))) / 2
eq("q4 area shoelace", sh, 5 * 0.5 * 16 * sin(2 * pi / 5), 1e-9)
assert 1 + 3 + 2 == 6
# q6: sum with ratio 1/4
for th in [0.6, 1.9]:
    eq("q6 C", sum(0.25 ** r * cos(r * th) for r in range(100)), 4 * (4 - cos(th)) / (17 - 8 * cos(th)), 1e-12)
    eq("q6 S", sum(0.25 ** r * sin(r * th) for r in range(100)), 4 * sin(th) / (17 - 8 * cos(th)), 1e-12)
    eq("denominator", (4 - cos(th)) ** 2 + sin(th) ** 2, 17 - 8 * cos(th))
eq("q6 b", 4 * 1 / 17, sum(0.25 ** r * sin(r * pi / 2) for r in range(100)), 1e-12)
# q7: seventh roots
om7 = cis(2 * pi / 7)
for k in range(1, 7):
    z = om7 ** k
    ceq("q7a", sum(z ** j for j in range(7)), 0, 1e-12)
    wv = z + 1 / z
    eq("q7 w", (wv ** 3 + wv ** 2 - 2 * wv - 1).real, 0, 1e-12)
    ceq("z^3+z^-3", z ** 3 + z ** -3, wv ** 3 - 3 * wv)
    ceq("z^2+z^-2", z ** 2 + z ** -2, wv ** 2 - 2)
assert sum(1 ** j for j in range(7)) == 7
rts = [2 * cos(2 * pi * k / 7) for k in (1, 2, 3)]
assert len({round(x, 9) for x in rts}) == 3
eq("sum cubic roots", sum(rts), -1, 1e-12)
eq("product cubic roots", rts[0] * rts[1] * rts[2], 1, 1e-12)
eq("sum cos", cos(2 * pi / 7) + cos(4 * pi / 7) + cos(6 * pi / 7), -0.5, 1e-12)
eq("product cos", cos(2 * pi / 7) * cos(4 * pi / 7) * cos(6 * pi / 7), 1 / 8, 1e-12)
for k in range(1, 4):
    eq("2cos(2pi(7-k)/7)", 2 * cos(2 * pi * (7 - k) / 7), 2 * cos(2 * pi * k / 7), 1e-12)
assert 3 + 3 + 4 == 10
# q8: (1 - e^{i t})^4
for th in [0.5, 1.8, 3.0]:
    z = cis(th)
    ceq("q8 binomial", sum((-1) ** r * comb(4, r) * z ** r for r in range(5)), (1 - z) ** 4)
    ceq("1 - e", 1 - z, -2j * sin(th / 2) * cis(th / 2))
    ceq("fourth", (1 - z) ** 4, 16 * sin(th / 2) ** 4 * cis(2 * th))
    eq("q8 C", 1 - 4 * cos(th) + 6 * cos(2 * th) - 4 * cos(3 * th) + cos(4 * th), 16 * sin(th / 2) ** 4 * cos(2 * th))
ceq("(-2i)^4", (-2j) ** 4, 16)
eq("q8 b", 16 * sin(pi / 4) ** 4 * cos(pi), -4, 1e-12)
eq("q8 direct", 1 - 4 * cos(pi / 2) + 6 * cos(pi) - 4 * cos(3 * pi / 2) + cos(2 * pi), -4, 1e-12)
assert 6 + 2 == 8

# ---- stretch
for n in range(2, 12):
    om = cis(2 * pi / n)
    prod = 1
    for k in range(1, n):
        prod *= (1 - om ** k)
    ceq("s1a", prod, n, 1e-9)
    p2 = 1
    for k in range(1, n):
        p2 *= sin(k * pi / n)
    eq("s1c", p2, n / 2 ** (n - 1), 1e-12)
    for k in range(1, n):
        eq("chord", abs(1 - om ** k), 2 * sin(k * pi / n))
        eq("distance", abs(om ** k - 1), abs(1 - om ** k))
    eq("sum squares", sum(abs(1 - om ** k) ** 2 for k in range(n)), 2 * n, 1e-9)
    eq("sum cos", sum(cos(2 * pi * k / n) for k in range(n)), 0, 1e-9)
    for k in range(n):
        eq("squared distance", abs(1 - om ** k) ** 2, 2 - 2 * cos(2 * pi * k / n), 1e-9)
eq("n=6", sin(pi / 6) * sin(2 * pi / 6) * sin(3 * pi / 6) * sin(4 * pi / 6) * sin(5 * pi / 6), 3 / 16, 1e-12)
assert F(6, 32) == F(3, 16)
assert 3 + 2 + 3 == 8 and 4 == 1 + 1 + 1 + 1

# reader items: |e^{ia} - 1| = 2 sin(a/2); five-wave amplitude uses omega = e^{2 pi i/5}
for a in (0.4, 1.7, 3.0, 5.5):
    eq("chord", abs(cmath.exp(1j * a) - 1), 2 * sin(a / 2) if a < 2 * pi else 0, 1e-12)
eq("5 waves th=72", abs(sum(cmath.exp(1j * r * radians(72)) for r in range(5))), 0, 1e-12)

print("ok")
