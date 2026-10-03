# checks/math.p3.algebra.py: recomputes every number in the Modulus and polynomials chapter.
from fractions import Fraction as F
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def polydiv(n, d):
    """n, d: coefficient lists, highest power first. returns quotient, remainder"""
    n = [F(x) for x in n]; q = []
    while len(n) >= len(d):
        c = n[0] / d[0]; q.append(c)
        for i in range(len(d)): n[i] -= c * d[i]
        n.pop(0)
    return q, n
def ev(c, x): 
    r = F(0)
    for a in c: r = r * x + a
    return r

# modulus graph and equations
assert abs(2 * F(3, 2) - 3) == 0 and abs(2 * 0 - 3) == 3
assert abs(2 * 5 - 3) == 7 and abs(2 * -2 - 3) == 7
for x in (F(-1, 2), -3): assert abs(x - 2) == abs(3 * x + 4)
assert 8 * 1 == 8 and polydiv([8, 28, 12], [4])[0] == [2, 7, 3]
assert 2 * F(-1, 2)**2 + 7 * F(-1, 2) + 3 == 0 and 2 * 9 - 21 + 3 == 0
assert 3 * 1 - 18 + 15 == 0 and 25 - 30 + 5 == 0
assert abs(1 + 1) == 2 and 2 * 1 - 4 == -2 and abs(5 + 1) == 6 == 2 * 5 - 4
assert [x for x in (1, 5) if abs(x + 1) == 2 * x - 4] == [5]
assert [x for x in (1, 5) if abs(x + 1) == -(2 * x - 4)] == [1]
for x in (-1, 5): assert abs(2 * x - 1) == x + 4
assert abs(2 * -1 - 1) == 3 and -1 + 4 == 3 and abs(2 * 5 - 1) == 9 == 5 + 4
# inequalities
assert -1 < 4 and abs(2 * -1 - 3) == 5 and abs(2 * 4 - 3) == 5
assert (-2 + 2) == 0 and 8 / 2 == 4
assert abs(1 + 2) == 3 and abs(-5 + 2) == 3
assert abs(12.3 - 12.5) <= 0.2 + 1e-12 and abs(12.7 - 12.5) <= 0.2 + 1e-12
for x in (F(-2, 3), 4): assert (2 * x - 1)**2 == (x + 3)**2
assert (3 * F(-2, 3) + 2) == 0 and 4**2 * 3 - 40 - 8 == 0
assert abs(2 * 0 - 1) < abs(0 + 3) and abs(2 * 5 - 1) > abs(5 + 3) and not abs(2 * 1 - 1) > abs(1 + 3)
for x in (2, F(3, 2), 10, F(1, 2), -4, 1, -3): assert (abs(x - 3) < 2 * x) == (x > 1)
assert abs(2 - 3) == 1 < 4 and abs(1 - 3) == 2 == 2 * 1
# polynomial division
q, r = polydiv([2, -5, 1, 6], [1, -2]); assert q == [2, -1, -1] and r == [4]
q, r = polydiv([1, 2, -7, 3, 5], [1, 1, -1]); assert q == [1, 1, -7] and r == [11, -2]
f = lambda x: 2*x**3 - 3*x**2 - 11*x + 6
assert f(1) == -6 and f(F(-3, 2)) == 9 and f(3) == 0
eq("-6.75", -6.75 - 6.75 + 16.5 + 6, 9)
assert 2 * F(-27, 8) == F(-27, 4)
# solving cubics
g = [1, -4, 1, 6]; assert ev(g, 2) == 0 and polydiv(g, [1, -2])[0] == [1, -2, -3] and ev(g, 3) == ev(g, -1) == 0
h = [2, -3, -11, 6]; assert polydiv(h, [1, -3])[0] == [2, 3, -2] and ev(h, F(1, 2)) == 0 and ev(h, -2) == 0
k = [1, -1, -3, -1]; assert ev(k, -1) == 0 and polydiv(k, [1, 1])[0] == [1, -2, -1]
eq("1+sqrt2", ev([1, -1, -3, -1], 1 + sqrt(2)), 0, 1e-9); eq("1-sqrt2", ev([1, -1, -3, -1], 1 - sqrt(2)), 0, 1e-9)
assert 4 + 4 == 8
# exam: unknowns
a, b = 6, -1
assert a + b == 5 and 2 * a - b == 13 and 3 * a == 18
fa = [1, a, b, -6]; assert ev(fa, 1) == 0 and ev(fa, -2) == 12 and -8 + 4 * a - 2 * b - 6 == 12
assert polydiv(fa, [1, -1])[0] == [1, 7, 6] and ev(fa, -1) == 0 and ev(fa, -6) == 0
# exam: box
vol = lambda x: x * (30 - 2 * x) * (20 - 2 * x)
for x in (1, 2, 5): assert vol(x) == 4 * x**3 - 100 * x**2 + 600 * x
assert vol(3) == 1008 and 27 - 225 + 450 - 252 == 0
assert polydiv([1, -25, 150, -252], [1, -3])[0] == [1, -22, 84] and 484 - 336 == 148
eq("17.08", round(11 + sqrt(37), 2), 17.08); eq("4.917", round(11 - sqrt(37), 3), 4.917); eq("4.92", round(11 - sqrt(37), 2), 4.92)
eq("vol", vol(11 - sqrt(37)), 1008, 1e-6)
# try questions
assert 3 * 3 - 1 == 8 and F(-7, 3) * 3 - 1 == -8
assert (4 - 4)**2 == 0 and abs(1 - 4) == abs(1 + 2)
assert 2 * -4 + 1 == -7 and 2 * 3 + 1 == 7 and 3 - 4 == -1 and 4 - 3 == 1
assert 4**2 == 16
for x in (-1, -3): assert (x - 1)**2 == (3 * x + 5)**2
assert abs(-1 - 1) == 2 == 3 * -1 + 5 and abs(-3 - 1) == 4 and 3 * -3 + 5 == -4
f = [1, 0, -5, 3]; assert ev(f, 2) == 1 and ev(f, -1) == 7 and ev(f, F(1, 2)) == F(5, 8)
assert polydiv([1, 3, -4, -12], [1, 3]) == ([1, 0, -4], [0])
c = [1, 4, 1, -6]; assert ev(c, -2) == 0 and polydiv(c, [1, 2])[0] == [1, 2, -3] and ev(c, -3) == 0 and ev(c, 1) == 0
q, r = polydiv([2, -1, 0, 3, -1], [1, -1, 1]); assert q == [2, 1, -1] and r == [1, 0] or r == [F(1), F(0)], (q, r)
# exam try
a, b = 1, -13
fx = [2, a, b, 6]; assert ev(fx, 2) == 0 and ev(fx, -1) == 18 and 2 * a + b == -11 and a - b == 14
assert polydiv(fx, [1, -2])[0] == [2, 5, -3] and ev(fx, F(1, 2)) == 0 and ev(fx, -3) == 0
for x in (0, 3, 1, 10, 7):
    assert (abs(x + 1) < abs(2 * x - 5)) == (x < F(4, 3) or x > 6), x
assert 3 * 36 - 132 + 24 == 0 and 3 * F(16, 9) - 22 * F(4, 3) + 24 == F(16, 3) - F(88, 3) + 24 == 0
# quiz
assert 4 + 6 == 10 and 4 - 6 == -2
assert 2 - 3 == -1 and 2 + 3 == 5
assert 2**3 + 4 - 5 == 7 and -5 == 0 + 0 - 5 and (-2)**3 + 2 * -2 - 5 == -17
assert 27 - 27 + 3 * -2 + 6 == 0
print("ok")
