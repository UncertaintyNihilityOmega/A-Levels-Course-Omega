# checks/math.s2.poisson.py: recomputes every number in the Poisson distribution chapter.
from math import isclose, exp, factorial, comb, log, sqrt
from statistics import NormalDist

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

def po(l, r):
    return exp(-l) * l ** r / factorial(r)

def cdf(l, r):
    return sum(po(l, k) for k in range(r + 1))

Z = NormalDist()

# Recurrence tip, lambda = 4
eq("P0", round(exp(-4), 4), 0.0183); eq("P1", round(po(4, 1), 4), 0.0733); eq("P2", round(po(4, 2), 4), 0.1465)

# Emails Po(4)
eq("a", sf(po(4, 3)), 0.195); eq("a exact form", po(4, 3), 32 / 3 * exp(-4))
eq("b", sf(cdf(4, 2)), 0.238); eq("b form", cdf(4, 2), 13 * exp(-4))
terms = [1, 4, 8, 32 / 3, 32 / 3, 128 / 15]
for k, t in enumerate(terms):
    eq(f"term {k}", 4 ** k / factorial(k), t)
eq("c inner", round(cdf(4, 5), 4), 0.7851); eq("c", sf(1 - cdf(4, 5)), 0.215)

# Scaling warning
eq("e^-0.8", round(exp(-0.8), 3), 0.449); eq("e^-1.6", round(exp(-1.6), 3), 0.202)
eq("0.449^2", round(0.449 ** 2, 3), 0.202)

# Cable
eq("25 m mean", 0.8 * 2.5, 2.0); eq("e^-2", sf(exp(-2)), 0.135)
eq("5 m mean", 0.8 * 0.5, 0.4); eq("inner", round(exp(-0.4) * 1.4, 4), 0.9384)
eq("P(Y>=2)", sf(1 - cdf(0.4, 1)), 0.0616)

# Bulbs B(150, 0.02)
eq("np", 150 * 0.02, 3)
approx = cdf(3, 2); eq("8.5e^-3", approx, 8.5 * exp(-3)); eq("approx", sf(approx), 0.423)
exact = sum(comb(150, k) * 0.02 ** k * 0.98 ** (150 - k) for k in range(3))
eq("exact", sf(exact), 0.421); eq("difference", round(sf(approx) - sf(exact), 3), 0.002)

# Normal approx Po(24)
eq("sigma", round(sqrt(24), 3), 4.899)
z = (29.5 - 24) / sqrt(24); eq("z", round(z, 3), 1.123); eq("normal", sf(1 - Z.cdf(z)), 0.131)
eq("exact Po(24)", sf(1 - cdf(24, 29)), 0.132)

# Cars
eq("b", sf(po(3.2, 2)), 0.209)
eq("c", sf(cdf(1.6, 2)), 0.783)
eq("5 min mean", 3.2 * 5, 16)
z = (20.5 - 16) / 4; eq("z", z, 1.125); eq("d", sf(1 - Z.cdf(z)), 0.130)

# Try it yourself
eq("t1a", sf(po(1.5, 2)), 0.251); eq("t1b", sf(1 - exp(-1.5)), 0.777)
eq("t3a", sf(exp(-2)), 0.135); eq("t3b", sf(1 - exp(-6)), 0.998); eq("t3c", sf(po(4, 4)), 0.195)
lam = log(5); eq("ln5", round(lam, 3), 1.609); eq("P(X=1)", sf(lam * 0.2), 0.322); eq("check", exp(-lam), 0.2)
eq("ratio", po(6, 3) / po(6, 2), 2)
eq("115 terms", sum(6 ** k / factorial(k) for k in range(5)), 115); eq("t5", sf(cdf(6, 4)), 0.285)
eq("np 80", 80 * 0.03, 2.4); eq("inner", round(cdf(2.4, 2), 4), 0.5697); eq("t6", sf(1 - cdf(2.4, 2)), 0.430)
z = (14.5 - 20) / sqrt(20); eq("z", round(z, 3), -1.230); eq("t7", sf(Z.cdf(z)), 0.109)
eq("P(X<=7)", round(cdf(4, 7), 4), 0.9489); p = 1 - cdf(4, 7); eq("t8a", sf(p), 0.0511)
eq("P(X<=8)", round(cdf(4, 8), 4), 0.9786); eq("P(X<=9)", round(cdf(4, 9), 4), 0.9919)
eq("t8c", sf(comb(5, 2) * 0.0511 ** 2 * 0.9489 ** 3), 0.0223)

# Quiz
eq("20 s mean", 6 / 3, 2); eq("np 200", 200 * 0.01, 2)
print("ok")
