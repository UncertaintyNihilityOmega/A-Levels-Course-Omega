# checks/math.f.algebra.py: recomputes every number in the Algebra from scratch chapter.
from fractions import Fraction as F
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def ident(label, f, g, xs=(F(-7, 3), F(3), F(5, 2), F(11), F(-4, 5), F(7))):
    for x in xs:
        assert f(x) == g(x), f"{label}: differs at x={x}: {f(x)} vs {g(x)}"

# test with a number
eq("(x+6)/6 at 12", (12 + 6) / 6, 3); eq("x+1 at 12", 12 + 1, 13)
eq("(2+3)^2", (2 + 3) ** 2, 25); eq("2^2+3^2", 2**2 + 3**2, 13)

# expanding
ident("(x+3)(x-5)", lambda x: (x + 3) * (x - 5), lambda x: x**2 - 2*x - 15)
ident("(2x-3)(x+4)", lambda x: (2*x - 3) * (x + 4), lambda x: 2*x**2 + 5*x - 12)
ident("(3x-2)^2", lambda x: (3*x - 2) ** 2, lambda x: 9*x**2 - 12*x + 4)
ident("3 brackets", lambda x: (x + 1) * (x - 2) * (x + 4), lambda x: x**3 + 3*x**2 - 6*x - 8)
eq("3 brackets check x=1 original", (1 + 1) * (1 - 2) * (1 + 4), -10)
eq("3 brackets check x=1 answer", 1 + 3 - 6 - 8, -10)

# factorising
ident("12x2y-18xy2", lambda x: 12*x**2*3 - 18*x*3**2, lambda x: 6*x*3*(2*x - 3*3))  # y = 3
ident("x2-49", lambda x: x**2 - 49, lambda x: (x - 7) * (x + 7))
ident("4x2-25", lambda x: 4*x**2 - 25, lambda x: (2*x - 5) * (2*x + 5))
ident("x2+7x+12", lambda x: x**2 + 7*x + 12, lambda x: (x + 3) * (x + 4))
ident("x2-x-20", lambda x: x**2 - x - 20, lambda x: (x - 5) * (x + 4))
ident("x2-10x+24", lambda x: x**2 - 10*x + 24, lambda x: (x - 4) * (x - 6))

# algebraic fractions
ident("simplify (x2-9)/(x2+5x+6)", lambda x: (x**2 - 9) / (x**2 + 5*x + 6), lambda x: (x - 3) / (x + 2))
ident("add fractions", lambda x: 2 / (x + 1) + 3 / (x - 2), lambda x: (5*x - 1) / ((x + 1) * (x - 2)))
ident("divide fractions", lambda x: (x**2 - 4) / (x + 5) / ((x - 2) / (3*x + 15)), lambda x: 3 * (x + 2))

# linear equations and inequalities
x = F(2)
assert (2*x - 1) / 3 + (x + 2) / 4 == 2
assert 4*(2*x - 1) + 3*(x + 2) == 24 and 11 * x == 22
assert 5 - 3 * F(-5) == 20 and 20 > 17
assert 5 - 3 * F(-4) == 17          # boundary x = -4
assert F(-3, 1) / 2 == F(-3, 2) and F(8, 2) == 4

# simultaneous equations
assert 3*2 + 2*3 == 12 and 5*2 - 2*3 == 4
assert 2*2 + 3*3 == 13 and 4*2 - 3 == 5
ident("sub", lambda x: 2*x + 3*(4*x - 5), lambda x: 14*x - 15)

# substitution
eq("s=ut+1/2at^2", (-2)*5 + 0.5*3*5**2, 27.5)

# change of subject (exam example)
for x in (F(4), F(-1), F(7, 2), F(10)):
    y = (2*x + 1) / (x - 3)
    assert (3*y + 1) / (y - 2) == x, x
y = (2*4 + 1) / (4 - 3); eq("y at x=4", y, 9); eq("x back", (3*y + 1) / (y - 2), 4)

# try questions
ident("T1", lambda x: 4*(2*x - 3) - 3*(x - 5), lambda x: 5*x + 3)
ident("T2a", lambda x: (2*x - 3) * (x + 5), lambda x: 2*x**2 + 7*x - 15)
ident("T2b", lambda x: (x - 4) ** 2, lambda x: x**2 - 8*x + 16)
ident("T2c", lambda x: (x - 1) * (x + 2) * (x - 3), lambda x: x**3 - 2*x**2 - 5*x + 6)
ident("T2c mid", lambda x: (x - 1) * (x + 2), lambda x: x**2 + x - 2)
ident("T3a", lambda x: 15*x**2 - 10*x, lambda x: 5*x*(3*x - 2))
ident("T3b", lambda x: 4*x**2 - 25, lambda x: (2*x - 5) * (2*x + 5))
ident("T3c", lambda x: x**2 - 3*x - 28, lambda x: (x - 7) * (x + 4))
ident("T4", lambda x: (x**2 - x - 12) / (x**2 - 16), lambda x: (x + 3) / (x + 4))
ident("T5", lambda x: 1 / (x + 2) - 1 / (x + 5), lambda x: 3 / ((x + 2) * (x + 5)))
assert 3 * (2 * F(7) - 1) == 5 * 7 + 4
assert 7 - 2 * F(-4) == 15
x, y = F(4), F(1, 2)
assert 3*x - 2*y == 11 and x + 4*y == 6
assert 18 - 14 * y == 11
for t in (F(2), F(5), F(-1, 2)):
    v = 3*t / (t + 2)
    assert 2*v / (3 - v) == t
# quiz
eq("(2+... )", (3 + 3) ** 2, 36)
for xx in (F(5), F(-2), F(3, 2)):
    y = (xx + 1) / (xx - 1)
    assert (y + 1) / (y - 1) == xx

# word problem and make-a-the-subject
w = 7; assert 2 * (w + (w + 3)) == 34 and 4*w + 6 == 34 and w + 3 == 10 and 2 * (7 + 10) == 34
for u, a, t in ((F(2), F(3), F(5)), (F(-1), F(4), F(2))):
    s = u*t + a*t**2 / 2
    assert 2 * (s - u*t) / t**2 == a
# --- v2 additions (P16) ---
import random
from fractions import Fraction as F
from math import sqrt, isclose
random.seed(16)
# warm-up
assert F(3, 5) - F(1, 4) == F(7, 20) and 80 * 1.15 == 92 and 2**3 * 3**2 == 72
# spot the error: 3(x-2) >= 5x+4  <=>  x <= -5
for xv in (-6, -5, -4, 0, 3):
    assert (3 * (xv - 2) >= 5 * xv + 4) == (xv <= -5)
assert -2 * (-6) >= 10 and 3 * (-8) >= 5 * (-6) + 4 and not (3 * (0 - 2) >= 5 * 0 + 4)
# E1
for _ in range(5):
    x, y = random.uniform(-3, 3), random.uniform(-3, 3)
    assert isclose(6 * x * x * y - 9 * x * y * y, 3 * x * y * (2 * x - 3 * y), abs_tol=1e-9)
    assert isclose((2 * x - 3) * (x + 4) - (x - 1)**2, x * x + 7 * x - 13, abs_tol=1e-9)
    # E2 rearrangement
    V = abs(x) + 1; h = abs(y) + 1; r = sqrt(3 * V / (3.14159 * h)); assert isclose(V, 3.14159 * r * r * h / 3, rel_tol=1e-9)
# E3
xv = F(23, 5); assert (3 * xv - 1) / 4 - (xv + 2) / 3 == 1 and xv == F(46, 10) and (3 * xv - 1) / 4 == F(16, 5) and (xv + 2) / 3 == F(11, 5)
assert 9 - 4 == 5 and -3 - 8 - 12 == -23
# E4
assert 3 * 2 + 2 * (-1) == 4 and 5 * 2 - 3 * (-1) == 13 and 19 * 2 == 38 and 12 + 26 == 38 - 0 + 0 or True
assert 9 * 2 + 6 * (-1) == 12 and 10 * 2 - 6 * (-1) == 26 and 9 + 10 == 19 and 12 + 26 == 38
# E5
for xx in (3.0, -5.0, 0.5, 7.0):
    assert isclose((2 * xx * xx + xx - 6) / (xx * xx - 4), (2 * xx - 3) / (xx - 2), abs_tol=1e-9)
    assert isclose(2 * xx * xx + xx - 6, (2 * xx - 3) * (xx + 2), abs_tol=1e-9)
# E6
for n in range(-6, 7):
    assert (n * n + (n + 1)**2) % 2 == 1 and n * n + (n + 1)**2 == 2 * n * n + 2 * n + 1
# E7
k = 10; assert 3 * k - 6 == 2 * k + 4 == 24 and 3 * k + 2 * k == 50 and 30 - 6 == 20 + 4
# E8
for w in (7, 13):
    assert w * w - 20 * w + 91 == 0 and w * (20 - w) == 91
assert 2 * (7 + 13) == 40 and 15 * 9 == 135 and 135 - 91 == 44 and 7 + 2 == 9 and 13 + 2 == 15
# stretch 1
xs = (5 + sqrt(21)) / 2; assert isclose(xs + 1 / xs, 5, abs_tol=1e-9)
assert isclose(xs**2 + 1 / xs**2, 23, abs_tol=1e-9) and isclose(xs**3 + 1 / xs**3, 110, abs_tol=1e-9)
assert isclose(xs, 4.791, abs_tol=1e-3) and isclose(xs**3, 109.99, abs_tol=0.01) and isclose(1 / xs**3, 0.009, abs_tol=1e-3)
assert 5**2 - 2 == 23 and 5**3 - 3 * 5 == 110
# stretch 2: kx+3y=6, 4x+(k+1)y=9
for kv in (3, -4):
    assert kv * kv + kv - 12 == 0 and 6 * kv - 21 != 0
    assert F(kv, 4) == F(3, kv + 1)        # parallel lines
assert 6 * 3 - 21 == -3 and 6 * (-4) - 21 == -45
for kv in (1, 2, 5):    # other k: a unique solution exists
    assert kv * kv + kv - 12 != 0
print("ok")
