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
print("ok")
