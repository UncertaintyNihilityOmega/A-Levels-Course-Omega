# checks/math.fm.rectangles.py: recomputes every number in Sums, rectangles and bounds.
# Standard library only.
from fractions import Fraction as F
from math import isclose, sqrt, log, exp, pi, e, factorial, atan


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simp(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


H = lambda n: sum(1 / r for r in range(1, n + 1))

# warm-up
eq("ln5", simp(lambda x: 1 / x, 1, 5), log(5))
assert 10 * 11 * 21 // 6 == 385 == sum(r * r for r in range(1, 11))

# eg 1: integral of 1/x on [1,3], four strips
h = 0.5
left = h * sum(1 / (1 + i * h) for i in range(4))
right = h * sum(1 / (1 + (i + 1) * h) for i in range(4))
eq("left", sf(left, 4), 1.283)
eq("right", sf(right, 3), 0.950)
eq("ln3", sf(log(3), 5), 1.0986)
eq("gap", left - right, h * (1 - 1 / 3))
eq("gap value", sf(left - right, 3), 0.333)
assert right < log(3) < left
# widget numbers: 1/x on [1,6], 5 strips
eq("left5", sum(1 / r for r in range(1, 6)), 2.2833333333333, 1e-9)
eq("right5", sum(1 / r for r in range(2, 7)), 1.45)
eq("ln6", log(6), 1.791759469228055)
eq("gap5", (2.2833333333333332 - 1.45), 1 - 1 / 6, 1e-9)

# harmonic bounds
for n in range(1, 200):
    assert log(n + 1) < H(n) < 1 + log(n) or n == 1
    if n >= 2:
        assert sum(1 / r for r in range(2, n + 1)) < log(n)
eq("ln101", sf(log(101), 5), 4.6151)
eq("1+ln100", sf(1 + log(100), 5), 5.6052)
eq("H100", sf(H(100), 4), 5.187)
assert 4.61 < log(101) and 1 + log(100) < 5.61 and 4.61 < H(100) < 5.61
# thresholds for 10
eq("e^10", sf(exp(10), 6), 22026.5)
eq("e^9", sf(exp(9), 5), 8103.1)
assert log(22027) >= 10 and log(22026) < 10      # n+1 = 22027 first with ln >= 10
nmin = 0
s = 0.0
while s <= 10:
    nmin += 1
    s += 1 / nmin
assert nmin == 12367 and 8104 <= nmin <= 22026
# threshold for 5
nm5 = 0
s = 0.0
while s <= 5:
    nm5 += 1
    s += 1 / nm5
assert nm5 == 83 and 55 <= nm5 <= 148
eq("e^4", sf(exp(4), 3), 54.6)
eq("e^5", sf(exp(5), 4), 148.4)
assert exp(4) < 55 and 54 < exp(4) and log(148) < 5 <= log(149) and exp(5) < 148.5
assert log(148) < 5  # n = 147 not guaranteed (n+1 = 148)
assert log(148 + 1) > 5  # n = 148 guaranteed

# sqrt sums
S100 = sum(sqrt(r) for r in range(1, 101))
for n in range(1, 120):
    s = sum(sqrt(r) for r in range(1, n + 1))
    assert 2 / 3 * n ** 1.5 < s < 2 / 3 * n ** 1.5 + sqrt(n)
eq("sqrt100 low", 2 * 1000 / 3, 666.6666666667, 1e-6)
eq("sqrt100 high", 2030 / 3, 676.6666666667, 1e-6)
eq("S100", sf(S100, 4), 671.5)
assert F(2000, 3) + 10 == F(2030, 3)
assert abs(sqrt(100) - 10) < 1e-12 and 100 ** 1.5 == 1000
# figure data
for r in range(1, 5):
    assert 1 / r > 1 / (r + 1)

# 1/r^2 bounds
for N in (1, 5, 10):
    for n in (N + 1, N + 7, 200):
        s = sum(1 / r ** 2 for r in range(N + 1, n + 1))
        assert 1 / (N + 1) - 1 / (n + 1) < s < 1 / N - 1 / n
s10 = sum(1 / r ** 2 for r in range(1, 11))
eq("s10", sf(s10, 7), 1.549768, 1e-6)
eq("1.549768+1/11", 1.549768 + 1 / 11, 1.640677, 1e-6)
eq("+0.1", 1.549768 + 0.1, 1.649768, 1e-6)
assert 1.64 < 1.549768 + 1 / 11 and 1.549768 + 0.1 < 1.65
eq("pi^2/6", sf(pi ** 2 / 6, 5), 1.6449)
eq("1/11", sf(1 / 11, 5), 0.090909)
assert 1 / (31 * 32) > 0.001 > 1 / (32 * 33)
for n in range(2, 100):
    assert sum(1 / r ** 2 for r in range(1, n + 1)) < 2 - 1 / n
    assert sum(1 / r ** 3 for r in range(2, n + 1)) < 0.5 - 1 / (2 * n * n)

# e^{-r} sum
s5 = sum(exp(-r) for r in range(1, 6))
eq("e up", 1 - exp(-5), 0.993, 5e-4)
eq("e low", exp(-1) - exp(-6), 0.365, 5e-4)
eq("e exact", (1 - exp(-5)) / (e - 1), s5)
eq("e exact value", sf(s5), 0.578)
assert exp(-1) - exp(-6) < s5 < 1 - exp(-5)
eq("simp e", simp(lambda x: exp(-x), 0, 5), 1 - exp(-5))

# limits
def R(f, n):
    return sum(f(r / n) for r in range(1, n + 1)) / n


def L(f, n):
    return sum(f(r / n) for r in range(0, n)) / n


eq("R10", R(lambda x: x * x, 10), 0.385)
eq("L10", L(lambda x: x * x, 10), 0.285)
eq("diff", R(lambda x: x * x, 10) - L(lambda x: x * x, 10), 0.1)
for n in (3, 10, 50):
    eq("R-L", R(lambda x: x * x, n) - L(lambda x: x * x, n), (1 - 0) / n)
    assert L(lambda x: x * x, n) < 1 / 3 < R(lambda x: x * x, n)
eq("sum r^2 / n^3", sum(r * r for r in range(1, 1001)) / 1000 ** 3, 1 / 3, 1e-3)
for n in (5, 12):
    assert F(n * (n + 1) * (2 * n + 1), 6) == sum(r * r for r in range(1, n + 1))
    eq("formula limit form", sum(r * r for r in range(1, n + 1)) / n ** 3, (n + 1) * (2 * n + 1) / (6 * n * n))
sa = sum(1 / (100 + r) for r in range(1, 101))
sb = sum(100 / (100 ** 2 + r * r) for r in range(1, 101))
eq("n=100 (a)", sf(sa, 4), 0.6907)
eq("n=100 (b)", sf(sb, 4), 0.7829)
eq("ln2", sf(log(2), 4), 0.6931)
eq("pi/4", sf(pi / 4, 4), 0.7854)
eq("limit a", simp(lambda x: 1 / (1 + x), 0, 1), log(2))
eq("limit b", simp(lambda x: 1 / (1 + x * x), 0, 1), atan(1))
eq("H2n-Hn", H(2000) - H(1000), log(2), 1e-3)
eq("half err a", (1 - 0.5) / (2 * 100), 0.0025)
eq("err a", log(2) - sa, 0.0025, 1e-4)
eq("err b", pi / 4 - sb, 0.0025, 1e-4)
for n in (10, 1000):
    s = sum(r / n for r in range(1, 2 * n + 1)) / n
    eq("2n sum", s, 2 + 1 / n)
eq("sqrt limit", simp(lambda x: x ** 0.5, 0, 1), 2 / 3, 1e-6)
for n in (10, 100):
    s = sum(sqrt(r) for r in range(1, n + 1)) / n ** 1.5
    assert 2 / 3 < s < 2 / 3 + 1 / n

# try questions
low = 0.5 * sum(exp(-(i + 1) * 0.5) for i in range(4))
up = 0.5 * sum(exp(-i * 0.5) for i in range(4))
eq("e^-x up", sf(up, 5), 1.0988, 1e-4)
eq("e^-x low", sf(low, 4), 0.6664, 1e-4)
eq("e^-x exact", 1 - exp(-2), 0.8646647167633873)
eq("0.6065 sum", 0.5 * (0.6065 + 0.3679 + 0.2231 + 0.1353), 0.6664, 1e-9)
eq("int 1/x^2 1..10", 1 - 1 / 10, 0.9)
assert sum(1 / r ** 2 for r in range(1, 10)) > 0.9
eq("ln720", sf(log(720), 3), 6.58)
eq("6ln6-5", sf(6 * log(6) - 5, 3), 5.75)
eq("1+ln1000", sf(1 + log(1000), 4), 7.908)
assert H(1000) < 8
eq("lim x^3", simp(lambda x: x ** 3, 0, 1), 0.25)
eq("1/(1+x)^2", simp(lambda x: 1 / (1 + x) ** 2, 0, 1), 0.5)

# exam practice
eq("q1 low", 0.5 * sum((i * 0.5) ** 2 for i in range(4)), 1.75)
eq("q1 high", 0.5 * sum(((i + 1) * 0.5) ** 2 for i in range(4)), 3.75)
for n in range(1, 150):
    s = sum(1 / sqrt(r) for r in range(1, n + 1))
    assert 2 * sqrt(n + 1) - 2 < s < 2 * sqrt(n) - 1 or n == 1
eq("q2 n=1", 1.0, 2 * sqrt(1) - 1)       # equality at n = 1 (strict from n >= 2)
for n in range(2, 12):
    lg = sum(log(r) for r in range(1, n + 1))
    assert n * log(n) - n + 1 < lg < (n + 1) * log(n) - n + 1
eq("int ln", simp(log, 1, 7), 7 * log(7) - 7 + 1)
eq("ln10!", sf(sum(log(r) for r in range(1, 11)), 5), 15.104)
eq("q4", simp(lambda x: sqrt(1 + 3 * x), 0, 1), 14 / 9)
eq("q4 sum", sum(sqrt(1 + 3 * r / 5000) for r in range(1, 5001)) / 5000, 14 / 9, 1e-3)
eq("q5", simp(lambda x: 1 / (1 + 2 * x), 0, 1), 0.5 * log(3))
eq("q5 sum", sum(1 / (5000 + 2 * r) for r in range(1, 5001)), 0.5 * log(3), 1e-3)
# q6
for n in range(1, 60):
    s = sum(r * r for r in range(1, n + 1))
    assert n ** 3 / 3 < s < n ** 3 / 3 + n * n
    assert F(n * (n + 1) * (2 * n + 1), 6) == F(n ** 3, 3) + F(n * n, 2) + F(n, 6)
    assert F(n * n, 2) + F(n, 6) < n * n
# q7
for n in range(2, 120):
    s = sum(1 / (2 * r + 1) for r in range(1, n + 1))
    assert 0.5 * log((2 * n + 3) / 3) < s < 1 / 3 + 0.5 * log((2 * n + 1) / 3)
s40 = sum(1 / (2 * r + 1) for r in range(1, 41))
eq("q7 low", sf(0.5 * log(83 / 3), 3), 1.66)
eq("q7 high", sf(1 / 3 + 0.5 * log(81 / 3), 3), 1.98)
eq("q7 true", sf(s40, 3), 1.84)
eq("e^6", sf(exp(6), 5), 403.43)
eq("2n+3", sf(3 * exp(6), 5), 1210.3)
nn = 1
while 0.5 * log((2 * nn + 3) / 3) <= 3:
    nn += 1
assert nn == 604 and (3 * exp(6) - 3) / 2 > 603.6

# stretch
d = lambda n: H(n) - log(n)
for n in range(1, 300):
    assert d(n) - d(n + 1) > 0 and d(n) > 0 and isclose(d(n) - d(n + 1), log((n + 1) / n) - 1 / (n + 1), abs_tol=1e-12)
eq("d1", d(1), 1.0)
eq("euler", sf(d(100000), 4), 0.5772, 2e-5)
for n in range(1, 60):
    assert log(n + 1) < H(n)

# review fix: bounds for the integral of 1 + x^2 with n rectangles
for n in (1, 2, 5, 10, 37):
    Un = sum(F(1, n) * (1 + F(r * r, n * n)) for r in range(1, n + 1))
    Ln = sum(F(1, n) * (1 + F((r - 1) ** 2, n * n)) for r in range(1, n + 1))
    assert Un == 1 + F((n + 1) * (2 * n + 1), 6 * n * n), n
    assert Ln == 1 + F((n - 1) * (2 * n - 1), 6 * n * n), n
    assert Un - Ln == F(1, n), n
    assert Ln < F(4, 3) < Un
    assert (n + 1) * (2 * n + 1) - (n - 1) * (2 * n - 1) == 6 * n
eq("U10", sf(float(1 + F(11 * 21, 600)), 4), 1.385, 1e-9)
eq("L10", sf(float(1 + F(9 * 19, 600)), 4), 1.285, 1e-9)
eq("43", sf(4 / 3, 4), 1.333, 1e-9)
eq("int", simp(lambda x: 1 + x * x, 0, 1), 4 / 3, 1e-9)
assert sum(s * s for s in range(0, 10)) == 9 * 10 * 19 // 6

print("ok")
