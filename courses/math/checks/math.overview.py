# checks/math.overview.py: recomputes the numbers in the readiness check of the course map.
from fractions import Fraction as F
from math import sin, cos, radians, sqrt, isclose

assert F(5, 6) - F(1, 4) == F(7, 12) and F(5, 6) * F(1, 4) == F(5, 24) and (5 - 1, 6 - 4) == (4, 2)
x = 7.3
assert isclose((x + 3) * (x - 5), x * x - 2 * x - 15, abs_tol=1e-9) and (x + 3) * (x - 5) != x * x - 15
assert 8 ** (2 / 3) > 3.99 and isclose(8 ** (2 / 3), 4, abs_tol=1e-9) and F(16, 3) == 8 * F(2, 3)
assert 2 * 3 - 4 * 0 == 6 and F(4 * 1 + 6, 2) == 5          # 2y = 4x + 6 -> y = 2x + 3 (gradient 2, intercept 3)
assert isclose(10 * sin(radians(30)), 5, abs_tol=1e-9) and round(10 * cos(radians(30)), 2) == 8.66
assert round(10 / 0.866, 1) == 11.5 and 10 / sin(radians(30)) > 19.99
print("ok")
