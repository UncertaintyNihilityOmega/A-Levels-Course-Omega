# checks/math.p1.functions.py: recomputes every number in the Functions chapter.
from fractions import Fraction as F
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def same(label, f, g, xs=(-3, -1.5, 0, 0.5, 2, 4.25, 7)):
    for x in xs:
        eq(f"{label} at {x}", f(x), g(x), 1e-9)

# Notation
eq("f(4)", 2 * 4 + 3, 11)

# Range of x^2 - 4x + 1 on [0, 5]
f = lambda x: x * x - 4 * x + 1
same("completed square", f, lambda x: (x - 2) ** 2 - 3)
eq("f(0)", f(0), 1); eq("f(5)", f(5), 6)
vals = [f(i / 1000) for i in range(0, 5001)]
eq("min", min(vals), -3); eq("max", max(vals), 6)

# Horizontal line test figure
eq("cube root of 4", round(4 ** (1 / 3), 2), 1.59)

# Composite example
f = lambda x: 2 * x + 1; g = lambda x: x * x - 3
same("fg", lambda x: f(g(x)), lambda x: 2 * x * x - 5)
same("gf", lambda x: g(f(x)), lambda x: 4 * x * x + 4 * x - 2)
for x in (-2, 1):
    eq(f"gf({x})=6", g(f(x)), 6)
eq("f(1)", f(1), 3); eq("g(3)", g(3), 6)

# Inverse of (2x+1)/(x-3)
f = lambda x: (2 * x + 1) / (x - 3); fi = lambda x: (3 * x + 1) / (x - 2)
for x in (-5, 0, 1, 4, 10):
    eq(f"f^-1 f({x})", fi(f(x)), x, 1e-9)
same("2 + 7/(x-3)", f, lambda x: 2 + 7 / (x - 3), (-5, 0, 1, 4, 10))
eq("f(4)", f(4), 9); eq("f^-1(9)", fi(9), 4); assert F(28, 7) == 4

# Graph of an inverse: f(x) = (x-2)^2 + 1, x >= 2
f = lambda x: (x - 2) ** 2 + 1; fi = lambda x: 2 + sqrt(x - 1)
for a, b in ((2, 1), (4, 5)):
    eq(f"f({a})", f(a), b); eq(f"f^-1({b})", fi(b), a)

# Restricting a domain
f = lambda x: x * x - 4 * x + 7
same("x^2-4x+7", f, lambda x: (x - 2) ** 2 + 3)
for x in (2, 3.5, 6):
    eq("inverse +", 2 + sqrt(f(x) - 3), x)
for x in (-1, 0, 2):
    eq("inverse -", 2 - sqrt(f(x) - 3), x)

# Exam-style example: 3x^2 - 12x + 5
f = lambda x: 3 * x * x - 12 * x + 5
same("3(x-2)^2-7", f, lambda x: 3 * (x - 2) ** 2 - 7)
fi = lambda x: 2 + sqrt((x + 7) / 3)
for x in (2, 3, 5.5):
    eq("exam inverse", fi(f(x)), x)
eq("min of f", f(2), -7)

# Transformations exam example, minimum (2, -3)
mx, my = 2, -3
assert (mx - 1, my - 4) == (1, -7)
assert (mx, 2 * my) == (2, -6)
eq("f(3x) min x", mx / 3, F(2, 3))
assert (mx, -my) == (2, 3)
assert (mx, 3 * my) == (2, -9) and (mx + 2, 3 * my + 1) == (4, -8)

# Try it yourself
f = lambda x: 3 * x - 5
eq("try f(4)", f(4), 7); eq("try f(-2)", f(-2), -11); eq("try f=10", (10 + 5) / 3, 5)
g = lambda x: 2 * x * x - 8 * x + 3
same("g completed", g, lambda x: 2 * (x - 2) ** 2 - 5); eq("g(3)", g(3), -3)
f = lambda x: x + 4; g = lambda x: 3 * x * x
same("try fg", lambda x: f(g(x)), lambda x: 3 * x * x + 4)
same("try gf", lambda x: g(f(x)), lambda x: 3 * x * x + 24 * x + 48)
x = F(-11, 6); assert 3 * x * x + 4 == 3 * (x + 4) ** 2
f = lambda x: 5 / (x - 2); fi = lambda x: 2 + 5 / x
for x in (-3, 0, 3, 7):
    eq("try inverse 5/(x-2)", fi(f(x)), x)
f = lambda x: x * x - 6 * x + 10
same("try (x-3)^2+1", f, lambda x: (x - 3) ** 2 + 1)
for x in (3, 4, 9):
    eq("try inverse", 3 + sqrt(f(x) - 1), x)
eq("stretch 1/(1/2)", 1 / F(1, 2), 2)
same("x^2-6x+4", lambda x: x * x - 6 * x + 4, lambda x: (x - 3) ** 2 - 5)
f = lambda x: 3 * x - 2; g = lambda x: x * x + 1
same("try gf exam", lambda x: g(f(x)), lambda x: 9 * x * x - 12 * x + 5)
for x in (F(5, 3), F(-1, 3)):
    assert (3 * x - 2) ** 2 + 1 == 10
fi = lambda x: (x + 2) / 3
eq("f(1)=f^-1(1)", f(1), fi(1)); eq("f(x)=x", f(1), 1)

# Quiz
f = lambda x: 2 * x + 1; g = lambda x: x - 4
same("quiz fg", lambda x: f(g(x)), lambda x: 2 * x - 7)
same("quiz gf", lambda x: g(f(x)), lambda x: 2 * x - 3)
# v2: warm-up
for y in (-2, 0, 7): eq("w1", 3 * ((y + 5) / 3) - 5, y)
for x in (-1, 0, 3): eq("w2", (x - 4) ** 2 - 13, x * x - 8 * x + 3)
for x in (-1, 0, 3): eq("w3", (2 * x + 1) ** 2 - 3, 4 * x * x + 4 * x - 2)

# v2: proof of the reflection: (a, b) -> (b, a); midpoint on y = x; joining gradient -1
for a, b in ((1, 4), (-2, 3), (5, -1.5)):
    eq("mid", (a + b) / 2, (b + a) / 2); eq("grad", (a - b) / (b - a), -1)

# v2: spot the error
fs = lambda x: (x - 2) ** 2 + 3
inv = lambda x: 2 + sqrt(x - 3)
for x in (2, 3.5, 6): eq("spot inverse", inv(fs(x)), x)
for y in (3, 4, 10): eq("spot inverse2", fs(inv(y)), y)
eq("spot range min", fs(2), 3)

# v2: exam practice
f1 = lambda x: x * x - 6 * x + 4
eq("x1 min", f1(3), -5); eq("x1 f0", f1(0), 4); eq("x1 f5", f1(5), -1)
assert max(f1(i / 100) for i in range(0, 501)) == 4 and min(f1(i / 100) for i in range(0, 501)) == -5
gg = lambda x: 2 * x * x - 1
eq("x2 gf(0)", gg(0 + 3), 17); eq("x2 gf(-6)", gg(-6 + 3), 17)
f3 = lambda x: (3 * x - 1) / (x + 2)
f3i = lambda x: (2 * x + 1) / (3 - x)
for x in (-5, -1, 0, 4): eq("x3 inverse", f3i(f3(x)), x, 1e-9)
for x in (-2.5, 0, 2, 5): eq("x3 form", f3(x), 3 - 7 / (x + 2), 1e-9)
for x in (-1, 0, 7): eq("x4 form", x * x - 10 * x + 31, (x - 5) ** 2 + 6)
f4i = lambda x: 5 + sqrt(x - 6)
for x in (5, 6.5, 9): eq("x4 inverse", f4i(x * x - 10 * x + 31), x)
# x5: transformations of the maximum (-1, 5)
eq("x5a", -1 / 2, -0.5); eq("x5b", 3 * 5 - 2, 13); eq("x5c", -1 - 4, -5); eq("x5d", -5, -5)
# x6
fg = lambda x: 1 / ((x * x - 1) - 2)
eq("x6 fg(2)", fg(2), 1); eq("x6 fg(-2)", fg(-2), 1); eq("x6 sq", 3 + 1, 4)
# x7: transformed curve
base = lambda x: x * x + 2 * x - 3
for x in (-2, 0, 1.5, 4):
    eq("x7 translation", base(x - 2) + 1, x * x - 2 * x - 2); eq("x7 stretch", 3 * (base(x - 2) + 1), 3 * x * x - 6 * x - 6)
eq("x7 min", 3 * 1 - 6 * 1 - 6, -9); eq("x7 orig min", base(-1), -4); eq("x7 after translation", -4 + 1, -3)
# x8
for x in (-1, 0, 3): eq("x8 square", (x - 2) ** 2 + 5, x * x - 4 * x + 9)
f8i = lambda x: 2 + sqrt(x - 5)
for x in (2, 4, 7): eq("x8 inverse", f8i(x * x - 4 * x + 9), x)
eq("x8 disc", 25 - 36, -11)
# stretch 1: self-inverse
fsi = lambda x: (x + 3) / (x - 1)
for x in (-4, 0, 2, 7, 11): eq("s1 ff", fsi(fsi(x)), x, 1e-9); eq("s1 form", fsi(x), 1 + 4 / (x - 1), 1e-9)
eq("s1 ff(7)", fsi(fsi(7)), 7)
# stretch 2
for a, b in ((3, -2), (-3, 4)):
    for x in (-2, 0, 3.5): eq("s2 ff", a * (a * x + b) + b, 9 * x - 8)
assert {a for a in (-3, 3)} == {a for a in range(-10, 11) if a * a == 9}
eq("quiz fg", (lambda x: 3 * x + 2)(4), 3 * 4 + 2); eq("quiz gf", 3 * (4 + 2), 18)
print("ok")
