# checks/math.fm.reduction.py: recomputes every number in Reduction formulae.
# Standard library only: exact values with Fraction, integrals with Simpson's rule.
from fractions import Fraction as F
from math import isclose, sqrt, sin, cos, tan, cosh, sinh, log, exp, pi, e, factorial


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


# ---- x^n e^{-x} on [0,1]: I_n = n I_{n-1} - 1/e
I = [1 - 1 / e]
for n in range(1, 6):
    I.append(n * I[n - 1] - 1 / e)
for n in range(6):
    eq(f"I{n} numeric", I[n], simp(lambda x: x ** n * exp(-x), 0, 1))
eq("I1", I[1], 1 - 2 / e)
eq("I2", I[2], 2 - 5 / e)
eq("I3", I[3], 6 - 16 / e)
eq("I3 value", sf(I[3], 4), 0.1139)
assert 0.25 / e < I[3] < 0.25 and round(0.25 / e, 3) == 0.092
eq("drug", sf(12 * I[3]), 1.37)
eq("drug exact", 72 - 192 / e, 12 * I[3])
# n = 0 misuse gives -1/e
eq("I0 misuse", 0 * 0 - 1 / e, -0.36787944117144233)
# spot the error: I_1
eq("spot I1", I[1], 1 - 2 / e)
eq("spot I1 value", sf(I[1]), 0.264)
eq("spot wrong", 2 / e - 1, -0.26424111765711533)

# ---- sin^n on [0, pi/2]
S = {0: pi / 2, 1: 1.0}
for n in range(2, 12):
    S[n] = (n - 1) / n * S[n - 2]
for n in range(0, 12):
    eq(f"sin^{n}", S[n], simp(lambda x: sin(x) ** n, 0, pi / 2))
    eq(f"cos^{n}", S[n], simp(lambda x: cos(x) ** n, 0, pi / 2))
eq("I5", S[5], 8 / 15)
eq("I2", S[2], pi / 4)
eq("I3", S[3], 2 / 3)
eq("I4", S[4], 3 * pi / 16)
eq("I6", S[6], 5 * pi / 32)
eq("I7", S[7], 16 / 35)
eq("I9", S[9], 128 / 315)
eq("I10/I8", S[10] / S[8], 9 / 10)
eq("I10", S[10], 63 * pi / 512)
eq("tip I2 direct", (pi / 4 - sin(pi) / 4) - 0, S[2])
assert F(5, 6) * F(3, 4) * F(1, 2) == F(15, 48) and F(15, 48) * pi / 2 == F(5, 16) * pi / 2
eq("15/48 pi/2", 15 / 48 * pi / 2, 5 * pi / 32)
# spindle volume
V = pi * S[6]
eq("V", V, 5 * pi ** 2 / 32)
eq("V numeric", V, simp(lambda x: pi * cos(x) ** 6, 0, pi / 2))
eq("V litres", sf(V), 1.54)
eq("cylinder", pi ** 2 / 2, 4.934802200544679)
assert V < pi ** 2 / 2
# I5 < I3
assert S[5] < S[3] and sf(S[3], 3) == 0.667 and sf(S[5], 3) == 0.533
# 6/7*4/5*2/3 and 8/9*6/7*4/5*2/3
assert F(6, 7) * F(4, 5) * F(2, 3) == F(16, 35) and F(48, 105) == F(16, 35)
assert F(8, 9) * F(6, 7) * F(4, 5) * F(2, 3) == F(128, 315) and F(384, 945) == F(128, 315)

# ---- tan^n on [0, pi/4]
T = {0: pi / 4, 1: 0.5 * log(2)}
for n in range(2, 8):
    T[n] = 1 / (n - 1) - T[n - 2]
for n in range(8):
    eq(f"T{n}", T[n], simp(lambda x: tan(x) ** n, 0, pi / 4))
eq("T3", T[3], 0.5 - 0.5 * log(2))
eq("T5", T[5], 0.5 * log(2) - 0.25)
eq("T5 value", sf(T[5]), 0.0966)
eq("T4", T[4], pi / 4 - 2 / 3)
eq("T6", T[6], 13 / 15 - pi / 4)
eq("T2", T[2], 1 - pi / 4)

# ---- sec^n on [0, pi/4]
def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


for n in (3, 4, 5, 6, 7):
    for x in (0.2, 0.5, 0.7):
        lhs = d(lambda t: tan(t) / cos(t) ** (n - 2), x)
        rhs = (n - 1) / cos(x) ** n - (n - 2) / cos(x) ** (n - 2)
        eq(f"sec deriv {n}", lhs, rhs, 1e-5)
J = {2: 1.0, 1: log(1 + sqrt(2)), 0: pi / 4}
for n in range(3, 8):
    J[n] = (2 ** ((n - 2) / 2) + (n - 2) * J[n - 2]) / (n - 1)
for n in range(8):
    eq(f"J{n}", J[n], simp(lambda x: 1 / cos(x) ** n, 0, pi / 4))
eq("J4", J[4], 4 / 3)
eq("J6", J[6], 28 / 15)
eq("J3 value", sf(J[3]), 1.15)
eq("J3", J[3], 0.5 * (sqrt(2) + log(1 + sqrt(2))))
eq("1.4142+0.8814", 0.5 * (1.4142 + 0.8814), 1.1478)
assert F(1, 3) * (2 + 2 * 1) == F(4, 3) and F(1, 5) * (4 + 4 * F(4, 3)) == F(28, 15)
eq("sec4 antiderivative", 1 + 1 / 3, 4 / 3)

# ---- (ln x)^n on [1, e]
L = [e - 1]
for n in range(1, 7):
    L.append(e - n * L[n - 1])
for n in range(7):
    eq(f"L{n}", L[n], simp(lambda x: log(x) ** n, 1, e))
eq("L1", L[1], 1)
eq("L2", L[2], e - 2)
eq("L3", L[3], 6 - 2 * e)
eq("L3 value", sf(L[3]), 0.563)
eq("L4", L[4], 9 * e - 24)
eq("L5", L[5], 120 - 44 * e)

# ---- x^n sqrt(1-x) on [0,1]
K = [F(2, 3)]
for n in range(1, 6):
    K.append(F(2 * n, 2 * n + 3) * K[n - 1])
for n in range(5):
    # substitute w = 1 - x: integral of (1-w)^n sqrt(w); smooth after w = t^2
    eq(f"K{n}", float(K[n]), simp(lambda t: (1 - t * t) ** n * t * 2 * t, 0, 1))
assert K[1] == F(4, 15) and K[2] == F(16, 105) and K[3] == F(32, 315) and K[4] == F(256, 3465)
assert F(2, 3) - F(2, 5) == F(4, 15)
assert F(6, 9) * F(16, 105) == F(32, 315) and F(8, 11) * F(32, 315) == F(256, 3465)

# ---- cosh^n on [0, ln 2]
a = log(2)
eq("cosh ln2", cosh(a), 5 / 4)
eq("sinh ln2", sinh(a), 3 / 4)
C = {0: a, 1: 0.75}
for n in range(2, 6):
    C[n] = (0.75 * 1.25 ** (n - 1) + (n - 1) * C[n - 2]) / n
for n in range(6):
    eq(f"C{n}", C[n], simp(lambda x: cosh(x) ** n, 0, a))
eq("C2", C[2], 0.5 * a + 15 / 32)
eq("C4", C[4], 735 / 1024 + 3 / 8 * a)
eq("C4 value", sf(C[4]), 0.978)
eq("(5/4)^4", 1.25 ** 4, 2.44140625)
eq("375/256", 0.75 * 1.25 ** 3, 375 / 256)
eq("C3", C[3], 57 / 64)
assert F(3, 4) * F(25, 16) + F(3, 2) == F(171, 64) and F(171, 64) / 3 == F(57, 64)
assert F(375, 256) + F(3, 2) * F(15, 16) == F(735, 256)
eq("C4 chain", (375 / 256 + 1.5 * (15 / 16 + a)) / 4, C[4])

# ---- sinh^n on [0, ln 3]
b = log(3)
eq("cosh ln3", cosh(b), 5 / 3)
eq("sinh ln3", sinh(b), 4 / 3)
SH = {0: b}
SH[2] = ((5 / 3) * (4 / 3) - SH[0]) / 2
SH[4] = ((5 / 3) * (4 / 3) ** 3 - 3 * SH[2]) / 4
for n in (2, 4):
    eq(f"S{n}", SH[n], simp(lambda x: sinh(x) ** n, 0, b))
eq("S2", SH[2], 10 / 9 - 0.5 * b)

# ---- try questions: U_n = int x^n e^{3x}, E_n = int x^n e^{2x}, Q_n = int x^n cos x
U = [(exp(3) - 1) / 3]
for n in (1, 2):
    U.append(exp(3) / 3 - n / 3 * U[n - 1])
for n in range(3):
    eq(f"U{n}", U[n], simp(lambda x: x ** n * exp(3 * x), 0, 1))
eq("U1", U[1], (2 * exp(3) + 1) / 9)
eq("U2", U[2], (5 * exp(3) - 2) / 27)
E = [(exp(2) - 1) / 2]
for n in (1, 2):
    E.append(exp(2) / 2 - n / 2 * E[n - 1])
for n in range(3):
    eq(f"E{n}", E[n], simp(lambda x: x ** n * exp(2 * x), 0, 1))
eq("E1", E[1], (exp(2) + 1) / 4)
eq("E2", E[2], (exp(2) - 1) / 4)
Q = {0: 1.0, 1: pi / 2 - 1}
for n in range(2, 6):
    Q[n] = (pi / 2) ** n - n * (n - 1) * Q[n - 2]
for n in range(6):
    eq(f"Q{n}", Q[n], simp(lambda x: x ** n * cos(x), 0, pi / 2))
eq("Q2", Q[2], pi ** 2 / 4 - 2)
eq("warm-up", Q[1], pi / 2 - 1)
# warm-up recurrence
u = 3
for _ in range(3):
    u = 2 * u - 1
assert u == 17

# ---- (1 - x^2)^n
Ip = [1.0]
for n in range(1, 5):
    Ip.append(2 * n / (2 * n + 1) * Ip[n - 1])
for n in range(5):
    eq(f"(1-x^2)^{n}", Ip[n], simp(lambda x: (1 - x * x) ** n, 0, 1))
    eq(f"cos^(2n+1) {n}", Ip[n], S[2 * n + 1])
eq("I3 = 16/35", Ip[3], 16 / 35)

# ---- u_n induction formula
# ---- sin^n on [0, pi/3]
A = {0: pi / 3}
for n in range(1, 6):
    A[n] = ((n - 1) * (A[n - 2] if n >= 2 else 0) - 0.5 * (sqrt(3) / 2) ** (n - 1)) / n if n >= 2 else simp(sin, 0, pi / 3)
for n in range(6):
    eq(f"A{n}", A[n], simp(lambda x: sin(x) ** n, 0, pi / 3))
eq("A2", A[2], pi / 6 - sqrt(3) / 8)
eq("A4", A[4], pi / 8 - 9 * sqrt(3) / 64)
eq("A4 antiderivative", pi / 8 - sqrt(3) / 8 - sqrt(3) / 64, A[4])
eq("2A2", 2 * A[2], pi / 3 - sqrt(3) / 4)
eq("4A4", 4 * A[4], pi / 2 - 3 * sqrt(3) / 8 - 3 * sqrt(3) / 16)
eq("3sqrt3/8", (sqrt(3) / 2) ** 3, 3 * sqrt(3) / 8)
eq("I8", S[8], 35 * pi / 256)
eq("x^5 sqrt", simp(lambda x: x ** 5 * sqrt(1 - x * x), 0, 1, 40000), 8 / 105, 1e-6)
eq("theta form", simp(lambda t: sin(t) ** 5 * cos(t) ** 2, 0, pi / 2), 8 / 105)
eq("I5-I7", S[5] - S[7], 8 / 105)
assert F(8, 15) - F(16, 35) == F(8, 105) and F(56, 105) - F(48, 105) == F(8, 105)
eq("peak", max(x ** 5 * sqrt(1 - x * x) for x in [i / 1000 for i in range(1001)]), 0.2588, 1e-3)
eq("8/105", sf(8 / 105), 0.0762)
assert F(7, 8) * F(5, 6) * F(3, 4) * F(1, 2) == F(35, 128)

for n in range(0, 6):
    eq(f"u{n}", S[2 * n], factorial(2 * n) * pi / (2 ** (2 * n + 1) * factorial(n) ** 2))
for k in range(0, 8):
    lhs = (2 * k + 1) / (2 * k + 2) * factorial(2 * k) * pi / (2 ** (2 * k + 1) * factorial(k) ** 2)
    rhs = factorial(2 * k + 2) * pi / (2 ** (2 * k + 3) * factorial(k + 1) ** 2)
    eq(f"induction step {k}", lhs, rhs)
    assert (2 * k + 2) ** 2 * factorial(k) ** 2 == 4 * factorial(k + 1) ** 2
eq("u5", factorial(10) * pi / (2 ** 11 * factorial(5) ** 2), 63 * pi / 512)

# ---- cosec^n on [pi/6, pi/2]
def cosec(x):
    return 1 / sin(x)


def cot(x):
    return cos(x) / sin(x)


for n in (3, 4, 5):
    for x in (0.7, 1.0, 1.3):
        lhs = d(lambda t: cot(t) * cosec(t) ** (n - 2), x)
        rhs = (n - 2) * cosec(x) ** (n - 2) - (n - 1) * cosec(x) ** n
        eq(f"cosec deriv {n}", lhs, rhs, 1e-5)
eq("cot pi/6", cot(pi / 6), sqrt(3))
eq("cosec pi/6", cosec(pi / 6), 2)
Vc = {2: sqrt(3)}
Vc[4] = (4 * sqrt(3) + 2 * Vc[2]) / 3
eq("V2", Vc[2], simp(lambda x: cosec(x) ** 2, pi / 6, pi / 2))
eq("V4", Vc[4], simp(lambda x: cosec(x) ** 4, pi / 6, pi / 2))
eq("V4 exact", Vc[4], 2 * sqrt(3))
eq("vol", pi * Vc[4], simp(lambda x: pi * cosec(x) ** 4, pi / 6, pi / 2))

# ---- stretch: Wallis-type bounds
for n in range(1, 11):
    eq(f"n I_n I_(n-1) {n}", n * S[n] * S[n - 1], pi / 2)
    assert sqrt(pi / (2 * (n + 1))) <= S[n] <= sqrt(pi / (2 * n)) + 1e-12
eq("lower n=10", sf(sqrt(pi / 22), 4), 0.3779)
eq("upper n=10", sf(sqrt(pi / 20), 4), 0.3963)
eq("I10", sf(S[10], 4), 0.3866)
# V_{m,n}
def beta(m, n):
    return F(factorial(m) * factorial(n), factorial(m + n + 1))


assert beta(4, 3) == F(1, 280) and F(3, 5) * F(2, 6) * F(1, 7) * F(1, 8) == F(1, 280) and F(6, 210) * F(1, 8) == F(1, 280) * 1
for m in range(0, 5):
    for n in range(1, 5):
        assert beta(m, n) == F(n, m + 1) * beta(m + 1, n - 1)
eq("beta numeric", float(beta(4, 3)), simp(lambda x: x ** 4 * (1 - x) ** 3, 0, 1))

print("ok")
