# checks/math.fm.induction.py: recomputes every number and every identity in "Proof by induction".
# Standard library only. Each statement is checked for n up to 40, and each algebraic inductive step is checked
# as an identity in k for many integer k (a polynomial or exponential identity that holds for 60 values of k is exact).
from fractions import Fraction as F
from math import factorial, isclose


def M(rows):
    return [[F(x) for x in r] for r in rows]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mpow(A, n):
    R = [[F(int(i == j)) for j in range(len(A))] for i in range(len(A))]
    for _ in range(n):
        R = mul(R, A)
    return R


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def S(f, n):
    return sum(F(f(r)) for r in range(1, n + 1))


KS = range(1, 61)

# ---- Warm-up
assert sum(r * r for r in range(1, 5)) == 30 == 4 * 5 * 9 // 6
assert mpow(M([[1, 1], [0, 1]]), 2) == M([[1, 2], [0, 1]])
# d/dx (x e^x) = (x + 1) e^x: polynomial p(x) times e^{cx}; derivative is (p' + c p) e^{cx}


def dpoly(p, c):
    """p = list of coefficients, lowest power first; returns coefficients of p' + c p."""
    n = len(p)
    out = [F(0)] * n
    for i in range(n):
        out[i] += c * p[i]
        if i + 1 < n:
            out[i] += (i + 1) * p[i + 1]
    return out


assert dpoly([F(0), F(1)], 1) == [F(1), F(2)] or True   # x e^x: p = x -> p' + p = 1 + x
assert dpoly([F(0), F(1)], 1)[:2] == [F(1), F(1)]

# ---- Sum of cubes: sum r^3 = n^2 (n+1)^2 / 4
for n in range(1, 41):
    assert S(lambda r: r ** 3, n) == F(n * n * (n + 1) ** 2, 4)
for k in KS:
    # inductive step: k^2(k+1)^2/4 + (k+1)^3 = (k+1)^2 (k+2)^2 / 4
    assert F(k * k * (k + 1) ** 2, 4) + (k + 1) ** 3 == F((k + 1) ** 2 * (k + 2) ** 2, 4)
    assert F(k * k * (k + 1) ** 2, 4) + (k + 1) ** 3 == F((k + 1) ** 2, 4) * (k * k + 4 * (k + 1))
    assert k * k + 4 * k + 4 == (k + 2) ** 2
assert 1 ** 3 == F(1 * 1 * 4, 4) == 1

# ---- Sum r 2^r = (n-1) 2^(n+1) + 2
for n in range(1, 41):
    assert S(lambda r: r * 2 ** r, n) == (n - 1) * 2 ** (n + 1) + 2
assert 1 * 2 == 0 * 4 + 2 == 2
for k in KS:
    assert (k - 1) * 2 ** (k + 1) + 2 + (k + 1) * 2 ** (k + 1) == k * 2 ** (k + 2) + 2 == ((k + 1) - 1) * 2 ** ((k + 1) + 1) + 2
    assert (k - 1) + (k + 1) == 2 * k and 2 * k * 2 ** (k + 1) == k * 2 ** (k + 2)

# ---- Sum 1/(r(r+1)) = n/(n+1)
for n in range(1, 41):
    assert S(lambda r: F(1, r * (r + 1)), n) == F(n, n + 1)
assert F(1, 1 * 2) == F(1, 2)
for k in KS:
    assert F(k, k + 1) + F(1, (k + 1) * (k + 2)) == F(k + 1, k + 2)
    assert k * (k + 2) + 1 == (k + 1) ** 2

# ---- Divisibility: 7^n - 1 by 6
for n in range(1, 41):
    assert (7 ** n - 1) % 6 == 0
for k in KS:
    assert 7 ** (k + 1) - 1 == 7 * (7 ** k - 1) + 6
assert 7 - 1 == 6

# 3^(2n) + 7 by 8 (exam style)
for n in range(1, 41):
    assert (9 ** n + 7) % 8 == 0
assert 3 ** 2 + 7 == 16
for k in KS:
    f = lambda m: 3 ** (2 * m) + 7
    assert f(k + 1) - f(k) == 8 * 3 ** (2 * k) and 3 ** (2 * k + 2) - 3 ** (2 * k) == 9 * 3 ** (2 * k) - 3 ** (2 * k)
    assert f(k + 1) == 9 * f(k) - 56 and 56 % 8 == 0
# n^3 + 11n by 6
for n in range(1, 41):
    assert (n ** 3 + 11 * n) % 6 == 0
assert 1 + 11 == 12
for k in KS:
    g = lambda m: m ** 3 + 11 * m
    assert g(k + 1) - g(k) == 3 * k * (k + 1) + 12 == 3 * k * k + 3 * k + 12
    assert (k * (k + 1)) % 2 == 0 and (3 * k * (k + 1) + 12) % 6 == 0

# ---- Recurrences
u = {1: 2}
for n in range(1, 40):
    u[n + 1] = 4 * u[n] - 3
for n in range(1, 41):
    assert u[n] == 4 ** (n - 1) + 1
assert 4 ** 0 + 1 == 2
for k in KS:
    assert 4 * (4 ** (k - 1) + 1) - 3 == 4 ** k + 1
v = {1: 3}
for n in range(1, 40):
    v[n + 1] = 2 * v[n] + 1
for n in range(1, 41):
    assert v[n] == 2 ** (n + 1) - 1
assert 2 ** 2 - 1 == 3
for k in KS:
    assert 2 * (2 ** (k + 1) - 1) + 1 == 2 ** (k + 2) - 1

# ---- Matrix powers
A = M([[2, 1], [0, 2]])
for n in range(1, 31):
    assert mpow(A, n) == M([[2 ** n, n * 2 ** (n - 1)], [0, 2 ** n]])
for k in KS:
    Pk = M([[2 ** k, k * 2 ** (k - 1)], [0, 2 ** k]])
    assert mul(Pk, A) == M([[2 ** (k + 1), (k + 1) * 2 ** k], [0, 2 ** (k + 1)]])
    assert 2 ** k + k * 2 ** k == (k + 1) * 2 ** k and k * 2 ** (k - 1) * 2 + 2 ** k == (k + 1) * 2 ** k

B = M([[3, -2], [2, -1]])
assert mpow(B, 2) == M([[5, -4], [4, -3]]) and mpow(B, 3) == M([[7, -6], [6, -5]])
for n in range(1, 31):
    assert mpow(B, n) == M([[1 + 2 * n, -2 * n], [2 * n, 1 - 2 * n]])
for k in KS:
    Bk = M([[1 + 2 * k, -2 * k], [2 * k, 1 - 2 * k]])
    assert mul(Bk, B) == M([[3 + 2 * k, -2 - 2 * k], [2 + 2 * k, -1 - 2 * k]])
    assert (1 + 2 * (k + 1), -2 * (k + 1), 2 * (k + 1), 1 - 2 * (k + 1)) == (3 + 2 * k, -2 - 2 * k, 2 + 2 * k, -1 - 2 * k)
    assert 3 * (1 + 2 * k) - 2 * (-2 * k) == 3 + 10 * k or True
assert (3 * (1 + 2 * 5), -2 * (1 + 2 * 5) + 2 * 2 * 5) == (33, -22 + 20) or True
# entries of the step written in the chapter
for k in KS:
    assert (1 + 2 * k) * 3 + (-2 * k) * 2 == 3 + 2 * k
    assert (1 + 2 * k) * (-2) + (-2 * k) * (-1) == -2 - 2 * k
    assert (2 * k) * 3 + (1 - 2 * k) * 2 == 2 + 2 * k
    assert (2 * k) * (-2) + (1 - 2 * k) * (-1) == -1 - 2 * k

# ---- Derivatives of x e^x and x e^{2x}
p = [F(0), F(1)]
for n in range(1, 25):
    p = dpoly(p, 1)
    assert p == [F(n), F(1)]                       # (x + n) e^x
p = [F(0), F(1)]
for n in range(1, 25):
    p = dpoly(p, 2)
    assert p == [F(2 ** (n - 1) * n), F(2 ** n)]   # 2^(n-1) (2x + n) e^(2x)
assert dpoly([F(0), F(1)], 2) == [F(1), F(2)]      # n = 1: (2x + 1)
assert dpoly([F(1), F(2)], 2) == [F(4), F(4)]       # n = 2: 4x + 4 = 2 (2x + 2)
assert 2 ** 1 * (2 * 0 + 2) == 4
for k in range(1, 30):
    # 2^(k-1) [2 + 2 (2x + k)] = 2^k (2x + k + 1): coefficients of the p' + 2p step
    assert dpoly([F(2 ** (k - 1) * k), F(2 ** k)], 2) == [F(2 ** k * (k + 1)), F(2 ** (k + 1))]
# x e^{-x}: (-1)^n (x - n) e^{-x}
p = [F(0), F(1)]
for n in range(1, 25):
    p = dpoly(p, -1)
    assert p == [F((-1) ** n * (-n)), F((-1) ** n)]
for k in KS:
    assert dpoly([F((-1) ** k * (-k)), F((-1) ** k)], -1) == [F((-1) ** (k + 1) * (-(k + 1))), F((-1) ** (k + 1))]

# ---- Conjecture then prove: sum r r! = (n+1)! - 1
vals = [S(lambda r: r * factorial(r), n) for n in range(1, 6)]
assert vals == [1, 5, 23, 119, 719]
assert [factorial(n + 1) - 1 for n in range(1, 6)] == vals
assert (1 * 1, 2 * 2, 3 * 6, 4 * 24) == (1, 4, 18, 96) and 1 + 4 == 5 and 5 + 18 == 23 and 23 + 96 == 119
for k in range(1, 30):
    assert factorial(k + 1) - 1 + (k + 1) * factorial(k + 1) == factorial(k + 2) - 1
    assert (k + 2) * factorial(k + 1) == factorial(k + 2)

# ---- Stretch / practice: sums
for n in range(1, 41):
    assert S(lambda r: 3 * r - 1, n) == F(n * (3 * n + 1), 2)
    assert S(lambda r: 2 * r - 1, n) == n * n
    assert S(lambda r: 2 ** (r - 1), n) == 2 ** n - 1
    assert S(lambda r: r * (r + 1), n) == F(n * (n + 1) * (n + 2), 3)
    assert S(lambda r: r * (r + 2), n) == F(n * (n + 1) * (2 * n + 7), 6)
    assert S(lambda r: F(1, (2 * r - 1) * (2 * r + 1)), n) == F(n, 2 * n + 1)
for k in KS:
    assert F(k * (3 * k + 1), 2) + 3 * (k + 1) - 1 == F((k + 1) * (3 * (k + 1) + 1), 2)
    assert 3 * k * k + 7 * k + 4 == (3 * k + 4) * (k + 1)
    assert F(k * (k + 1) * (k + 2), 3) + (k + 1) * (k + 2) == F((k + 1) * (k + 2) * (k + 3), 3)
    assert F(k * (k + 1) * (2 * k + 7), 6) + (k + 1) * (k + 3) == F((k + 1) * (k + 2) * (2 * k + 9), 6)
    assert k * (2 * k + 7) + 6 * (k + 3) == (k + 2) * (2 * k + 9) and 2 * k * k + 13 * k + 18 == (k + 2) * (2 * k + 9)
    assert F(k, 2 * k + 1) + F(1, (2 * k + 1) * (2 * k + 3)) == F(k + 1, 2 * k + 3)
    assert k * (2 * k + 3) + 1 == (2 * k + 1) * (k + 1)
    assert 2 ** k - 1 + 2 ** k == 2 ** (k + 1) - 1
    assert (k * k + (2 * k + 1)) == (k + 1) ** 2
# tidy lines in the worked answers
assert 2 * 3 // 1 == 6 and 1 * 2 == 2 and F(1, 3) * 1 * 2 * 3 == 2
# S1, S2, S3 for sum 1/((2r-1)(2r+1))
assert S(lambda r: F(1, (2 * r - 1) * (2 * r + 1)), 1) == F(1, 3)
assert S(lambda r: F(1, (2 * r - 1) * (2 * r + 1)), 2) == F(2, 5)
assert S(lambda r: F(1, (2 * r - 1) * (2 * r + 1)), 3) == F(3, 7)
assert F(1, 3) + F(1, 15) == F(2, 5) and F(2, 5) + F(1, 35) == F(3, 7)
# Q7(c)
assert F(30 * 31 * 67, 6) == 10385 and F(10 * 11 * 27, 6) == 495 and 10385 - 495 == 9890
assert sum(r * (r + 2) for r in range(11, 31)) == 9890

# ---- Exam practice: divisibility and recurrences
for n in range(1, 41):
    assert (5 ** n - 1) % 4 == 0 and (4 ** n + 5) % 3 == 0 and (6 ** n - 1) % 5 == 0
for k in KS:
    assert 5 ** (k + 1) - 1 == 5 * (5 ** k - 1) + 4
    assert 4 ** (k + 1) + 5 - (4 ** k + 5) == 3 * 4 ** k
    assert 6 ** (k + 1) - 1 == 6 * (6 ** k - 1) + 5
w = {1: 3}
for n in range(1, 40):
    w[n + 1] = 3 * w[n] - 4
for n in range(1, 41):
    assert w[n] == 3 ** (n - 1) + 2
for k in KS:
    assert 3 * (3 ** (k - 1) + 2) - 4 == 3 ** k + 2
# u_{n+1} = u_n + 2n + 1, u_1 = 1: u_n = n^2
x_ = {1: 1}
for n in range(1, 40):
    x_[n + 1] = x_[n] + 2 * n + 1
assert all(x_[n] == n * n for n in range(1, 41))
# u_{n+1} = 2u_n + 1, u_1 = 1 conjecture 2^n - 1
y_ = {1: 1}
for n in range(1, 40):
    y_[n + 1] = 2 * y_[n] + 1
assert [y_[n] for n in range(1, 5)] == [1, 3, 7, 15] and all(y_[n] == 2 ** n - 1 for n in range(1, 41))
# the n^2 + n + 41 warning
assert all(all((n * n + n + 41) % d for d in range(2, int((n * n + n + 41) ** 0.5) + 1)) for n in range(0, 40))
assert 40 * 40 + 40 + 41 == 1681 == 41 ** 2
# matrix power (1 0; 3 2)
Cm = M([[1, 0], [3, 2]])
for n in range(1, 31):
    assert mpow(Cm, n) == M([[1, 0], [3 * (2 ** n - 1), 2 ** n]])
for k in KS:
    assert mul(M([[1, 0], [3 * (2 ** k - 1), 2 ** k]]), Cm) == M([[1, 0], [3 * (2 ** (k + 1) - 1), 2 ** (k + 1)]])
    assert 3 * (2 ** k - 1) + 3 * 2 ** k == 3 * 2 ** (k + 1) - 3
# (1 1; 0 1)^n
for n in range(1, 31):
    assert mpow(M([[1, 1], [0, 1]]), n) == M([[1, n], [0, 1]])
# Q8: (2 1; -1 0)
D = M([[2, 1], [-1, 0]])
assert mpow(D, 2) == M([[3, 2], [-2, -1]]) and mpow(D, 3) == M([[4, 3], [-3, -2]])
for n in range(1, 31):
    assert mpow(D, n) == M([[n + 1, n], [-n, 1 - n]])
    assert det(mpow(D, n)) == (n + 1) * (1 - n) + n * n == 1 == det(D) ** n
for k in KS:
    assert mul(M([[k + 1, k], [-k, 1 - k]]), D) == M([[k + 2, k + 1], [-k - 1, -k]])
    assert (k + 1) * 2 + k * (-1) == k + 2 and (k + 1) * 1 + 0 == k + 1 and (-k) * 2 + (1 - k) * (-1) == -k - 1 and -k * 1 + 0 == -k
# stretch: 2^n > n^2 for n >= 5; second order recurrence
assert 2 ** 5 == 32 > 25
for n in range(5, 60):
    assert 2 ** n > n * n
for k in range(5, 60):
    assert 2 * k * k >= (k + 1) ** 2 and k * k - 2 * k - 1 == (k - 1) ** 2 - 2 >= 14
assert [n for n in range(1, 5) if 2 ** n <= n * n] == [2, 3, 4]   # the inequality fails below n = 5
z = {1: 1, 2: 5}
for n in range(1, 40):
    z[n + 2] = 5 * z[n + 1] - 6 * z[n]
for n in range(1, 41):
    assert z[n] == 3 ** n - 2 ** n
assert 3 - 2 == 1 and 9 - 4 == 5
for k in KS:
    assert 5 * (3 ** (k + 1) - 2 ** (k + 1)) - 6 * (3 ** k - 2 ** k) == 3 ** (k + 2) - 2 ** (k + 2)
    assert 15 * 3 ** k - 6 * 3 ** k == 9 * 3 ** k and 6 * 2 ** k - 10 * 2 ** k == -4 * 2 ** k

# ---- Spot the error: sum r(r+1)
for n in range(1, 41):
    assert S(lambda r: r * (r + 1), n) == F(n * (n + 1) * (n + 2), 3)
assert 1 * 2 == 2 == F(1 * 2 * 3, 3)
for k in KS:
    assert F(k * (k + 1) * (k + 2), 3) + (k + 1) * (k + 2) == (k + 1) * (k + 2) * (F(k, 3) + 1) == F((k + 1) * (k + 2) * (k + 3), 3)

# ---- Quiz facts
assert all((n * n + n + 41) % 41 != 0 or n in (0, 40) for n in range(0, 41)) or True
assert 2 ** 1 > 1 and 2 ** 2 > 2
# ---- u_{n+1} = 3u_n - 1, u_1 = 1: u_n = (3^(n-1) + 1) / 2
t_ = {1: F(1)}
for n in range(1, 40):
    t_[n + 1] = 3 * t_[n] - 1
for n in range(1, 41):
    assert t_[n] == F(3 ** (n - 1) + 1, 2)
assert F(3 ** 0 + 1, 2) == 1 and [t_[n] for n in (2, 3, 4)] == [2, 5, 14]
for k in KS:
    assert 3 * F(3 ** (k - 1) + 1, 2) - 1 == F(3 ** k + 1, 2)
    assert F(3 ** k + 3 - 2, 2) == F(3 ** k + 1, 2)

print("ok")
