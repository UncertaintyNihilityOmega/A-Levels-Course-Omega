# checks/math.p3.logs.py: recomputes every number in the Logarithms and exponentials chapter.
from math import isclose, log, log2, log10, exp, e, sqrt
from fractions import Fraction as F

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")

# definitions
eq("log10 1000", log10(1000), 3); eq("log2 1/8", log2(1/8), -3); eq("9^1/2", 9**0.5, 3)
eq("log5 125", log(125, 5), 3); eq("log10 .01", log10(0.01), -2); eq("log4 2", log(2, 4), 0.5); assert 4**3 == 64
# laws
eq("a", log(9) + log(5) - log(15), log(3)); eq("b", log2(40) - log2(5), 3)
eq("tip", log10(10 + 90), 2); eq("tip2", log10(10) + log10(90), 2.954, 1e-3)
# equations
for x in (1,): eq("3a", log(x, 3) + log(x + 2, 3), 1)
assert (-3 + 3) * (-3 - 1) == 0 and 1 + 2 - 3 == 0
eq("3b", 2 * log(3), log(3 + 6)); assert 3**2 - 3 - 6 == 0 and (-2)**2 + 2 - 6 == 0
# e and graphs
eq("e", round(e, 5), 2.71828)
# a^x = b
eq("3^x", sf(log(20) / log(3)), 2.73); eq("3^2.727", round(3**2.727, 1), 20.0)
x = log(2) / log(2.5); eq("2^(x+1)=5^x", 2**(x + 1), 5**x); eq("x", sf(x), 0.756)
eq("e2x", sf(0.5 * log(7)), 0.973); eq("ln", sf((e**3 + 1) / 2), 10.5); eq("ln check", log(2 * ((e**3 + 1) / 2) - 1), 3)
# quadratics in e^x
for u in (2, 3): eq("quad", u * u - 5 * u + 6, 0)
eq("ln2", sf(log(2)), 0.693); eq("ln3", sf(log(3)), 1.10)
assert (9 - 9) * (9 + 5) == 0 and 81 - 36 - 45 == 0 and 3**2 == 9
# inequalities
eq("2^x>50", sf(log(50) / log(2), 3), 5.64); eq("0.5^x", sf(log(0.1) / log(0.5), 3), 3.32)
eq("n", sf(log(2) / log(1.05), 3), 14.2); assert 1.05**14 < 2 < 1.05**15
eq("1.05^14", round(1.05**14, 3), 1.980); eq("1.05^15", round(1.05**15, 3), 2.079)
# exam: population
eq("P10", sf(200 * exp(0.3)), 270); eq("t", sf(log(2.5) / 0.03), 30.5); eq("half", sf(log(2) / 0.1), 6.93)
# exam: logs
assert F(5, 7) + 5 == 8 * F(5, 7) and 2**3 == 8
eq("2b", log2(5/7 + 5) - log2(5/7), 3)
for u in (F(2, 3), 3): assert 3 * u * u - 11 * u + 6 == 0
assert (3 * F(2, 3) - 2) == 0
# linear form data
xs = [1, 2, 4, 9]; ys = [2 * x**1.5 for x in xs]
eq("y2", round(ys[1], 2), 5.66); eq("y9", ys[3], 54); eq("y4", ys[2], 16)
lx = [log(x) for x in xs]; ly = [log(y) for y in ys]
for a, b in zip(lx, [0, 0.693, 1.386, 2.197]): eq("lnx", a, b, 6e-4)
for a, b in zip(ly, [0.693, 1.733, 2.773, 3.989]): eq("lny", a, b, 6e-4)
eq("grad1", (1.733 - 0.693) / 0.693, 1.50, 1e-2); eq("grad2", (3.989 - 2.773) / (2.197 - 1.386), 1.50, 1e-2)
eq("k", round(exp(0.693)), 2)
eq("plot pt", 1.5 * 2.197 + 0.693, 3.989, 1e-3)
# exam: Ax^b
b = (7.1 - 2.1) / (2.5 - 0.5); eq("b", b, 2.5); lnA = 2.1 - b * 0.5; eq("lnA", lnA, 0.85); eq("A", sf(exp(0.85)), 2.34)
lna = (5.1 - 3.1) / (6 - 2); eq("lna", lna, 0.5); eq("a", sf(exp(0.5)), 1.65)
lnK = 3.1 - 0.5 * 2; eq("lnK", lnK, 2.1); eq("K", sf(exp(2.1)), 8.17)

# try
eq("T1a", log(81, 3), 4, 1e-9); eq("T1b", log10(0.001), -3); eq("T1c", log(2, 8), 1/3); eq("T1d", log(e**5), 5)
eq("T2", log10(8) + log10(5) - log10(4), 1)
eq("T4a", sf(log(12) / log(5)), 1.54); eq("T4b", sf((1 + log(10)) / 3), 1.10); eq("T4c", sf(e**2 - 4), 3.39)
for u in (3, 4): assert u * u - 7 * u + 12 == 0
eq("T5", sf(log(4)), 1.39)
assert (4 - 4) * (4 + 1) == 0 and 4**2 - 3 * 4 - 4 == 0 and 2**2 == 4
eq("T7a", sf(log(7) / log(3)), 1.77); eq("T7b", sf(log(0.3) / log(0.8)), 5.40); eq("T7c", sf(log(100) / log(1.2), 4), 25.26)
assert 1.2**25 < 100 < 1.2**26
eq("T8", sf(log(0.25) / log(0.88), 4), 10.84); assert 0.88**10 * 20000 > 5000 > 0.88**11 * 20000
ys = [5 * 1.5**k for k in range(4)]; assert ys == [5, 7.5, 11.25, 16.875]
for a, b_ in zip([log(y) for y in ys], [1.609, 2.015, 2.420, 2.826]): eq("T10 ln", a, b_, 6e-4)
eq("T10 g", log(1.5), 0.405, 6e-4); eq("T10 a", sf(exp(0.405)), 1.5, 1e-2); eq("T10 k", exp(log(5)), 5)
# quiz
eq("Q1", log2(8) + log2(4), 5); eq("Q2", log(12) - log(4), log(3)); eq("Q3", sf(log(9) / log(2)), 3.17); eq("Q3w", sf(log(9) - log(2)), 1.50)

assert (5 - 1) * (5 + 3) == 32
# ---- v2 additions: warm-up, proof, spot the error, exam practice, stretch ----
import random
from math import log, exp
eq("warm-up 16^(3/4) x 2^-5", 16 ** 0.75 * 2 ** -5, 0.25)
assert (3 - 3) * (3 - 4) == 0 and 3 * 4 == 12 and 3 + 4 == 7
f_inv = lambda x: (x + 1) / 3
for x in (-2, 0.5, 7):
    eq("warm-up inverse", 3 * f_inv(x) - 1, x)
for _ in range(10):                                                   # proof: the three laws
    a = random.uniform(1.5, 6); x, y, k = random.uniform(0.5, 9), random.uniform(0.5, 9), random.uniform(-3, 3)
    la = lambda t: log(t) / log(a)
    eq("product law", la(x * y), la(x) + la(y)); eq("quotient law", la(x / y), la(x) - la(y)); eq("power law", la(x ** k), k * la(x))
eq("spot: correct x", log(2) / (log(5) - log(2)), 0.756, 0.0005)       # spot the error
eq("spot: wrong x", log(2, 10) / (log(5, 10) - 1), -1.0)
assert 2 ** 0 == 1 and 5 ** -1 == 0.2
eq("spot check LHS", 2 ** (0.756 + 1), 3.38, 0.005); eq("spot check RHS", 5 ** 0.756, 3.38, 0.005)
eq("Q1", log(30) / log(5), 2.11, 0.005)                               # exam practice
eq("Q2", 2 * log(6, 3) - log(4, 3), 2)
for x in (2, 3):
    eq("Q3", 2 * log(x), log(5 * x - 6))
assert [(x - 2) * (x - 3) for x in (2, 3)] == [0, 0]
for x in (log(2), log(5)):
    eq("Q4", exp(2 * x) - 7 * exp(x) + 10, 0)
eq("Q5a", 80 * exp(-0.5), 48.5, 0.05); eq("Q5b", log(4) / 0.05, 27.7, 0.05); eq("Q5c", log(2) / 0.05, 13.9, 0.05)
eq("Q5b check", 80 * exp(-0.05 * log(4) / 0.05), 20); eq("Q5c check", 80 * exp(-0.05 * log(2) / 0.05), 40)
m = (7.3 - 2.5) / 3; eq("Q6 grad", m, 1.6); eq("Q6 b", exp(m), 4.95, 0.005); eq("Q6 c", 2.5 - m, 0.9); eq("Q6 A", exp(0.9), 2.46, 0.005)
assert abs(2 ** 3 - 6) == 2 and abs(2 ** 2 - 6) == 2                  # Q7
for x in (-3, 0, 1, 2.5):
    eq("Q8a", 2 ** (2 * x + 1), 2 * (2 ** x) ** 2)
for x in (-1, 2):
    u = 2 ** x; eq("Q8b", 2 * u * u - 9 * u + 4, 0)
for x in (-3, -1.5, 0, 1, 1.9, 2.5, 4):                               # Q8c sign of the expression
    assert (2 ** (2 * x + 1) - 9 * 2 ** x + 4 < 0) == (-1 < x < 2)
x = log(15) / log(25 / 6)                                             # stretch 1
eq("S1", x, 1.90, 0.005); eq("S1 check", 2 ** x * 3 ** (x + 1), 5 ** (2 * x - 1), 1e-9)
r = (5 + 17 ** 0.5) / 2                                               # stretch 2
eq("S2 lhs", log(r - 2) + log(r + 1), log(4 * r - 4))
r2 = (5 - 17 ** 0.5) / 2
assert r2 - 2 < 0 and 25 - 8 == 17
print("ok")
