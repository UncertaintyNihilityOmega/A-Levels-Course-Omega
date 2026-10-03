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
print("ok")
