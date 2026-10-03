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
print("ok")
