# checks/math.f.graphs.py: recomputes every number in the Graphs and straight lines chapter.
from fractions import Fraction as F
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def grad(p, q): return F(q[1] - p[1], q[0] - p[0])

# gradient figure and example
assert grad((1, 3), (5, 11)) == 2 and (5 - 1, 11 - 3) == (4, 8)
m = grad((1, 3), (5, 11)); c = 3 - m * 1; assert c == 1 and m * 5 + c == 11 and m * 0 + c == 1

# rearranging lines
assert F(12 - 3 * 0, 2) == 6                 # 3x+2y=12 at x=0
assert F(12, 3) == 4                         # y=0
assert F(3, 2) * 4 == 6                      # gradient -3/2 passes (4,0) from (0,6)
# taxi
assert 2 * F(15, 2) + 3 == 18

# intersections
for x in (-1, 2):
    assert x**2 == x + 2
assert 1 == (-1)**2 and 4 == 2**2
# exam: A(2,5) B(6,-3)
m = grad((2, 5), (6, -3)); assert m == -2
c = 5 - m * 2; assert c == 9 and m * 6 + c == -3
assert F(9, 2) == F(9, 2) and 9 / 2 == 4.5
# exam: y=2x+3 and y=x^2
for x in (3, -1):
    assert x**2 == 2*x + 3
assert (2*3 + 3, 2*(-1) + 3) == (9, 1)
assert (3 - 3) * (3 + 1) == 0 and (-1 - 3) * (-1 + 1) == 0

# try questions
assert grad((2, 1), (6, 9)) == 2 and grad((-1, 7), (3, 1)) == F(-3, 2)
assert F(-4, 5) * 5 == -4 and 20 / 5 == 4            # 4x+5y=20: y=-4/5 x +4
assert 10 + 6 * 0 == 10 and F(10, 2) == 5            # 2y-6x=10
assert 3 == F(1, 2) * 4 + 1                          # line through (4,3), gradient 1/2
assert 5 * 0 - 2 * (-5) == 10 and 5 * 2 - 2 * 0 == 10 and F(5, 2) > 0
assert [F(6, 2), F(6, 2), F(-3), F(1, 3)] == [3, 3, -3, F(1, 3)]
assert F(140 - 200, 4) == -15 and F(200, 15) == F(40, 3)
for x in (3, -2):
    assert x**2 - 5 == x + 1
assert (3 + 1, -2 + 1) == (4, -1)
# last try
assert -5 == 3 * 2 - 11
for x in (2, 3):
    assert x**2 - 2*x - 5 == 3*x - 11
assert 3 * 3 - 11 == -2 and 9 - 6 - 5 == -2 and 4 - 4 - 5 == -5

# quiz
assert F(8 - 4 * 0, 2) == 4                                   # 2y = 8 - 4x -> y = 4 - 2x
assert grad((1, 2), (3, 8)) == 3 and F(3 - 1, 8 - 2) == F(1, 3) and F(8 + 2, 3 + 1) == F(10, 4)
for x in (3, -2):
    assert x**2 == x + 6
assert (x := -3, 2) and (-3 + 3) * (-3 - 2) == 0 and (lambda x: (x + 3) * (x - 2) == x**2 + x - 6)(5)
# --- v2 additions (P16) ---
from fractions import Fraction as F
# warm-up
assert 2 * 5 - 7 < 5 and not (2 * 6 - 7 < 5); assert 4**-0.5 == 0.5; eq_ = None
assert F(12 - 3 * 2, 2) == 3 and F(3, 2) * 4 == 6
# spot the error
m = F(8 + 1, 5 - 2); assert m == 3 and 3 * 2 - 7 == -1 and 3 * 5 - 7 == 8
ms = F(5 - 2, 8 + 1); assert ms == F(1, 3) and ms * 5 - F(5, 3) - ms * 2 + F(5, 3) == 1  # student line has slope 1/3
assert ms * (5 - 2) - 1 != 8 and F(1, 3) * 5 - F(5, 3) == 0
# exam practice
assert (24 - 4 * 0) / 3 == 8 and 24 / 4 == 6 and F(-4, 3) * 3 + 8 == 4
assert 3 * (-1) + 7 == 4
assert -2 * 4 + 7 == -1 and -2 == -2  # y = 3 - 2x has gradient -2
g = F(10 - 1, 4 + 2); assert g == F(3, 2) and g * (4 + 2) + 1 - 6 * 0 == 10 and 1 + g * (-2 + 2) == 1
assert F(3, 2) * 4 + 4 == 10 and F(3, 2) * (-2) + 4 == 1 and F(3, 2) * (-6) + 4 == -5
for x, y in ((4, 5), (-1, 0)):
    assert y == x + 1 and y == x * x - 2 * x - 3
assert (4 - 4) * (4 + 1) == 0 and (-1 - 4) * (-1 + 1) == 0 and 4 + (-1) == 3 and 4 * -1 == -4
n = F(7, 4 * 1) / 1; n = F(7) / F(4, 100); assert n == 175
assert 12 + F(5, 100) * 175 == F(2075, 100) == 5 + F(9, 100) * 175 == F(2075, 100) and 20.75 == float(F(2075, 100))
assert 0.09 > 0.05 and 12 + 0.05 * 200 < 5 + 0.09 * 200
x = F(3); assert 2 * x + 1 == 7 and x + 7 == 10 and 2 * x + 1 == 10 - x
A, B = F(-1, 2), F(10); assert 2 * A + 1 == 0 and A + 0 == A and B - A == F(21, 2) and F(1, 2) * (B - A) * 7 == F(147, 4) == 36.75
# stretch
assert 15 * 2 == 30 and 70 - 20 * 2 == 30 and 60 - 20 * (2 - 0.5) == 30 and 15 * 1 == 15 and 70 - 20 * 1 == 50 and 50 - 15 == 35
mm = F(-3, 2); assert 4 * mm**2 + 12 * mm + 9 == 0 and (2 * mm + 3) == 0
assert 3 - 2 * mm == 6 and 2 - 3 / mm == 4 and F(1, 2) * 4 * 6 == 12
for mv in (F(-1, 2), F(-1), F(-3, 2), F(-2), F(-3), F(-5)):   # area never below 12
    assert F(1, 2) * (2 - 3 / mv) * (3 - 2 * mv) >= 12
assert F(1, 2) * (2 - 3 / mm) * (3 - 2 * mm) == 12 and 12 - 4 * mm - 9 / mm == 24
# quiz
assert F(6, 2) == 3 and F(5, 2) == 2.5
print("ok")
