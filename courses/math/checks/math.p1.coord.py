# checks/math.p1.coord.py: recomputes every number in the Coordinate geometry chapter.
from fractions import Fraction as F
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def grad(p, q): return F(q[1] - p[1], q[0] - p[0])
def mid(p, q): return (F(p[0] + q[0], 2), F(p[1] + q[1], 2))
def on_line(a, b, c, p): return a * p[0] + b * p[1] + c == 0
def on_circ(cx, cy, r2, p): return (p[0] - cx)**2 + (p[1] - cy)**2 == r2

# distance etc
eq("AB", sqrt(6**2 + 4**2), 2 * sqrt(13)); assert mid((-2, 1), (4, 5)) == (1, 3) and grad((-2, 1), (4, 5)) == F(2, 3)
assert (3 - (-1), 4 - 7) == (4, -3) and (3 + 4, 4 - 3) == (7, 1) and mid((-1, 7), (7, 1)) == (3, 4)

# lines
assert 2 * 3 - (-1) - 7 == 0                                   # y+1=2(x-3) -> 2x-y-7=0 passes (3,-1)? 6+1-7=0
assert grad((1, 5), (4, -1)) == -2 and on_line(2, 1, -7, (1, 5)) and on_line(2, 1, -7, (4, -1))
# 3x+4y=12
assert F(-3, 4) == -F(3, 4) and 12 / 3 == 4 and F(1, 2) * 4 * 3 == 6
# perpendicular through (2,5)
assert -1 / F(-3, 4) == F(4, 3) and on_line(4, -3, 7, (2, 5))
for x in (F(1), F(4), F(-5)):
    y = F(4, 3) * (x - 2) + 5; assert 4 * x - 3 * y + 7 == 0
# perpendicular bisector (1,2),(7,6)
assert mid((1, 2), (7, 6)) == (4, 4) and grad((1, 2), (7, 6)) == F(2, 3) and on_line(3, 2, -20, (4, 4))
for x in (F(0), F(2), F(10)):
    y = F(-3, 2) * (x - 4) + 4; assert 3 * x + 2 * y - 20 == 0

# exam eg: A(-2,1) B(6,5)
A, B = (-2, 1), (6, 5)
assert mid(A, B) == (2, 3) and grad(A, B) == F(1, 2)
assert on_line(2, 1, -7, (2, 3)) and 7 / 2 == 3.5
C = (F(7, 2), 0)
assert (C[0] - A[0])**2 + (C[1] - A[1])**2 == F(125, 4) == (B[0] - C[0])**2 + (B[1] - C[1])**2 == F(125, 4)
assert F(125, 4) == 31.25
eq("AB", sqrt(8**2 + 4**2), 4 * sqrt(5)); eq("CM", sqrt(1.5**2 + 3**2), 1.5 * sqrt(5))
eq("area", 0.5 * 4 * sqrt(5) * 1.5 * sqrt(5), 15)
eq("shoelace", abs(A[0]*(B[1]-0) + B[0]*(0-A[1]) + 3.5*(A[1]-B[1])) / 2, 15)

# circles
assert on_circ(3, -2, 25, (6, 2)) and (3, -2) == (3, -2)
# expand (x-3)^2+(y+2)^2=25 -> x2+y2-6x+4y-12=0
for x, y in ((6, 2), (3, 3), (-2, -2), (3, -7)):
    assert (x - 3)**2 + (y + 2)**2 - 25 == x**2 + y**2 - 6*x + 4*y - 12
# x2+y2+8x-2y+8
for x, y in ((0, 0), (1, 2), (-3, 5)):
    assert x**2 + y**2 + 8*x - 2*y + 8 == (x + 4)**2 + (y - 1)**2 - 9
assert -16 - 1 + 8 == -9
# diameter (-1,2),(5,-6)
assert mid((-1, 2), (5, -6)) == (2, -2); eq("AB", sqrt(6**2 + 8**2), 10)
# tangent at (6,2)
assert grad((3, -2), (6, 2)) == F(4, 3) and on_line(3, 4, -26, (6, 2))
for x in (F(0), F(2), F(10)):
    y = F(-3, 4) * (x - 6) + 2; assert 3 * x + 4 * y - 26 == 0
# right angle at C(6,1)
assert on_circ(2, -2, 25, (6, 1)) and grad((-1, 2), (6, 1)) == F(-1, 7) and grad((5, -6), (6, 1)) == 7 and F(-1, 7) * 7 == -1
assert on_circ(2, -2, 25, (-1, 2)) and on_circ(2, -2, 25, (5, -6))

# line-circle k
for k in (4, -4):
    assert (2 * k)**2 - 4 * 2 * (k**2 - 8) == 0
assert 4 * 3**2 - 8 * 3**2 + 64 == 64 - 36 and (-2)**2 + 2**2 == 8
# exam: circle x2+y2-6x+4y-12
for x, y in ((0, 0), (3, 3)):
    assert x**2 + y**2 - 6*x + 4*y - 12 == (x - 3)**2 + (y + 2)**2 - 25
for x in (3, -1):
    y = 2 * x - 3; assert on_circ(3, -2, 25, (x, y))
assert (3, 3) == (3, 2*3 - 3) and (-1, -5) == (-1, 2*(-1) - 3)
eq("AB2", sqrt(4**2 + 8**2), 4 * sqrt(5)); assert mid((3, 3), (-1, -5)) == (1, -1)
assert grad((3, -2), (1, -1)) == F(-1, 2) and F(-1, 2) * 2 == -1
# 5x2-10x-15 from (x-3)^2+(2x-1)^2-25
for x in (0, 1, 2, 7):
    assert (x - 3)**2 + (2*x - 1)**2 - 25 == 5*x**2 - 10*x - 15

# three points
A, B, D = (6, 2), (3, 3), (-2, -2)
assert mid(A, B) == (F(9, 2), F(5, 2)) and grad(A, B) == F(-1, 3)
assert F(5, 2) - 3 * F(9, 2) == -11
assert mid(A, D) == (2, 0) and grad(A, D) == F(1, 2)
assert 3 * 3 - 11 == -2 and -2 * 3 + 4 == -2 and 3 - 2 == 1
for p in (A, B, D): assert on_circ(3, -2, 25, p)

# try questions
eq("T1", sqrt(8**2 + 6**2), 10); assert mid((-3, 4), (5, -2)) == (1, 1)
assert on_line(1, 2, -4, (-2, 3))
assert grad((1, -2), (5, 6)) == 2 and 2 * 1 - 4 == -2
assert F(-2, 3) == F(-4, 6)
assert -1 / F(-2, 3) == F(3, 2) and on_line(3, -2, -7, (3, 1))
assert mid((-1, 4), (5, 0)) == (2, 2) and grad((-1, 4), (5, 0)) == F(-2, 3) and on_line(3, -2, -2, (2, 2))
assert 3**2 + 4**2 == 25
for x, y in ((0, 0), (1, 1)): assert x**2 + y**2 - 10*x + 6*y + 18 == (x - 5)**2 + (y + 3)**2 - 16
assert 25 + 9 - 18 == 16
assert 2*(-3)**2 + 12*(-3) + 18 == 0
assert 6**2 - 4 * 1 * 9 == 0
assert on_circ(1, -2, 20, (3, 2)) and grad((1, -2), (3, 2)) == 2 and on_line(1, 2, -7, (3, 2))
# last exam circle
assert 3**2 + 4**2 == 25 and grad((2, -1), (5, 3)) == F(4, 3) and on_line(3, 4, -27, (5, 3)) and 27 / 3 == 9
eq("AT", sqrt(4**2 + 3**2), 5); eq("area", 0.5 * 5 * 5, 12.5)
assert 100 - 64 == 36 and F(64, 36) == F(16, 9) and F(4, 3)**2 == F(16, 9)
# quiz
assert F(2, 5) * F(-5, 2) == -1
assert F(7 + 4, 2) == 5.5 and (3 - 1) / 2 == 1 and (2 * 7 - 4, 2 * 3 - (-1)) == (10, 7)
assert 16 * 25 - 20 * (25 - 5) == 100 - 4 * 25 == 0

assert mid((7, 3), (1, -5)) == (4, -1) and (4 + 7, -1 + 3) == (11, 2)
# v2: warm-up
eq("w1", sqrt(25 + 144), 13); eq("w2", (11 - 2) / (4 - 1), 3); eq("w3a", 5 * 5 - 4 * 5 - 5, 0); eq("w3b", 1 + 4 - 5, 0)

# v2: proofs. Perpendicular gradients: OA^2 + OB^2 = AB^2 exactly when m1*m2 = -1
import random
random.seed(11)
for _ in range(8):
    m1 = random.uniform(-5, 5); m2 = -1 / m1
    eq("perp pyth", (1 + m1 ** 2) + (1 + m2 ** 2), (m1 - m2) ** 2, 1e-9)
    m3 = m2 + 0.7
    assert abs((1 + m1 ** 2) + (1 + m3 ** 2) - (m1 - m3) ** 2) > 1e-6
# circle general form: expand (x-a)^2 + (y-b)^2 - r^2
for a, b, r in ((3, -2, 5), (-1.5, 2, 3), (0, 4, 2)):
    g, f_, c = -a, -b, a * a + b * b - r * r
    for x, y in ((0, 0), (1.3, -2.2), (4, 4)):
        eq("circle expand", (x - a) ** 2 + (y - b) ** 2 - r * r, x * x + y * y + 2 * g * x + 2 * f_ * y + c, 1e-9)
    eq("circle radius", sqrt(g * g + f_ * f_ - c), r)

# v2: spot the error: x^2 + y^2 + 6x - 4y - 12 = 0
g, f_, c = 3, -2, -12
eq("spot r", sqrt(g * g + f_ * f_ - c), 5)
for x, y in ((2, 2), (-3, 7), (-8, 2), (-3, -3)):
    eq("spot on circle", (x + 3) ** 2 + (y - 2) ** 2, 25); eq("spot expand", x * x + y * y + 6 * x - 4 * y - 12, 0)
eq("spot rhs", 12 + 9 + 4, 25)

# v2: exam practice
eq("x1 AB", sqrt(4 ** 2 + 3 ** 2), 5); eq("x1 mid", (1 + 5) / 2, 3); eq("x1 midy", (-2 + 1) / 2, -0.5); eq("x1 grad", 3 / 4, 0.75)
# x2: line through (3,-2) gradient -2/5: 2x + 5y + 4 = 0
eq("x2 point", 2 * 3 + 5 * -2 + 4, 0); eq("x2 grad", -2 / 5, -0.4); eq("x2 given grad", -2 / 5, -2 / 5)
# x3: perp bisector of (-2,3), (4,7)
eq("x3 mid", (-2 + 4) / 2, 1); eq("x3 midy", (3 + 7) / 2, 5); eq("x3 grad", 4 / 6, 2 / 3); eq("x3 perp", -1 / (2 / 3), -1.5)
eq("x3 line passes mid", 3 * 1 + 2 * 5 - 13, 0)
# equidistant: (x, y) on 3x + 2y - 13 = 0, e.g. x = 3 -> y = 2
for x in (-1, 3, 5):
    y = (13 - 3 * x) / 2
    eq("x3 equidistant", (x + 2) ** 2 + (y - 3) ** 2, (x - 4) ** 2 + (y - 7) ** 2, 1e-9)
# x4: circle x^2 + y^2 - 10x + 4y + 4 = 0
eq("x4 rhs", 25 + 4 - 4, 25)
for x, y in ((8, 2), (5, 3), (10, -2)): eq("x4 on", x * x + y * y - 10 * x + 4 * y + 4, 0)
eq("x4 radius grad", (2 + 2) / (8 - 5), 4 / 3); eq("x4 tangent grad", -3 / 4, -0.75)
eq("x4 tangent", 3 * 8 + 4 * 2 - 32, 0)
# the tangent has distance 5 from the centre
eq("x4 dist", abs(3 * 5 + 4 * -2 - 32) / 5, 5)
# x5
for k in (10, -10):
    eq("x5 disc", 16 * k * k - 20 * (k * k - 20), -4 * k * k + 400); eq("x5 zero", -4 * k * k + 400, 0)
    eq("x5 distance", abs(k) / sqrt(5), sqrt(20))
# x6: triangle A(1,1), B(4,2), C(3,5)
eq("x6 BA", (1 - 2) / (1 - 4), 1 / 3); eq("x6 BC", (5 - 2) / (3 - 4), -3); eq("x6 prod", (1 / 3) * -3, -1)
eq("x6 BA len", sqrt(10), sqrt(9 + 1)); eq("x6 BC len", sqrt(1 + 9), sqrt(10)); eq("x6 area", 0.5 * sqrt(10) * sqrt(10), 5)
eq("x6 centre", (1 + 3) / 2, 2); eq("x6 centrey", (1 + 5) / 2, 3); eq("x6 r2", (1 - 3) ** 2 + (1 - 5) ** 2, 20); eq("x6 r", sqrt(20) / 2, sqrt(5))
for x, y in ((1, 1), (4, 2), (3, 5)): eq("x6 on circle", (x - 2) ** 2 + (y - 3) ** 2, 5)
# x7: circle x^2 + y^2 - 2x + 4y - 13 = 0
eq("x7 rhs", 13 + 1 + 4, 18); eq("x7 r", sqrt(18), 3 * sqrt(2))
for k in (-8, -2, 0, 2.5, 5):
    D = (2 * k + 2) ** 2 - 8 * (k * k + 4 * k - 13)
    eq("x7 disc", D, -4 * (k + 9) * (k - 3)); assert (D > 0) == (-9 < k < 3), k
    eq("x7 disc2", D, -4 * k * k - 24 * k + 108)
for x in (-1, 0, 2): eq("x7 sub", x * x + (x + 1) ** 2 - 2 * x + 4 * (x + 1) - 13, 2 * x * x + 4 * x - 8)
r1, r2 = -1 + sqrt(5), -1 - sqrt(5)
eq("x7 chord", sqrt(((r1 - r2) ** 2) * 2), 2 * sqrt(10)); eq("x7 root", r1 * r1 + 2 * r1 - 4, 0)
# stretch 1: PA = 2 PB
for t in (0.3, 1.1, 2.0, 4.7):
    import math
    x, y = 4 + 2 * math.cos(t), 2 * math.sin(t)
    eq("s1 PA=2PB", sqrt(x * x + y * y), 2 * sqrt((x - 3) ** 2 + y * y), 1e-9)
for x, y in ((1, 2), (-3, 1), (4, 0)):
    eq("s1 expand", x * x + y * y - 4 * ((x - 3) ** 2 + y * y), -(3 * x * x + 3 * y * y - 24 * x + 36))
# stretch 2
eq("s2 r", 5, 5); eq("s2 dist", sqrt(16 + (5 - 2) ** 2), 5); eq("s2 eq", (0 - 4) ** 2 + (2 - 5) ** 2, 25); eq("s2 touch", (4 - 4) ** 2 + (0 - 5) ** 2, 25)
eq("s2 solve", 16 + 4 - 4 * 5, 0)
eq("quiz tangent grad", -1 / (2 / 5), -2.5)
print("ok")
