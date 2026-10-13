# checks/math.calc.py: recomputes every number in the chapter
from math import sqrt, sin, isclose, comb, exp
from statistics import NormalDist, mean, pstdev, stdev

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")

# mode example
eq("sin 30 deg", sin(30 * 3.141592653589793 / 180), 0.5)
eq("sin 30 rad", sf(sin(30)), -0.988)

# quadratic 3x^2 - 5x - 4
eq("disc", 25 + 48, 73)
eq("sqrt73", round(sqrt(73), 4), 8.5440)
eq("root +", sf((5 + sqrt(73)) / 6), 2.26)
eq("root -", sf((5 - sqrt(73)) / 6), -0.591)

# sign change table
f = lambda x: x**3 - 2 * x - 5
eq("f2", f(2), -1)
eq("f2.1", round(f(2.1), 3), 0.061)
eq("f2.2", round(f(2.2), 3), 1.248)

# iteration
x = 2.0
terms = []
for _ in range(5):
    x = (2 * x + 5) ** (1 / 3)
    terms.append(x)
for k,w in enumerate([2.0801,2.0924,2.0942,2.0945,2.0945]): eq(f"it{k+2}", round(terms[k],4), w)
eq("root 3sf", sf(terms[-1]), 2.09)

# trapezium
g = lambda t: 1 / (1 + t * t)
ys = [g(k * 0.25) for k in range(5)]
eq("y.25", round(ys[1], 4), 0.9412)
eq("y.5", ys[2], 0.8)
eq("y.75", ys[3], 0.64)
eq("bracket", round(ys[0] + ys[4] + 2 * (0.9412 + 0.8 + 0.64), 4), 6.2624)
T = 0.5 * 0.25 * (ys[0] + ys[4] + 2 * sum(ys[1:4]))
eq("trap", sf(T), 0.783)

# statistics
d = [4, 7, 7, 9, 13]
eq("sum", sum(d), 40)
eq("sumsq", sum(v * v for v in d), 364)
eq("mean", mean(d), 8)
eq("sigma", sf(pstdev(d)), 2.97)
eq("s", sf(stdev(d)), 3.32)
eq("sigma^2", 364 / 5 - 64, 8.8)
eq("s^2", (364 - 5 * 64) / 4, 11)

# regression
xs, ys2 = [1, 2, 3, 4], [2, 3, 5, 6]
n = 4
sxy = sum(a * b for a, b in zip(xs, ys2)) - sum(xs) * sum(ys2) / n
sxx = sum(a * a for a in xs) - sum(xs) ** 2 / n
eq("Sxy", sxy, 7)
eq("Sxx", sxx, 5)
b = sxy / sxx
a0 = mean(ys2) - b * mean(xs)
eq("b", b, 1.4)
eq("a", a0, 0.5)

# distributions
p = sum(comb(12, k) * 0.3**k * 0.7 ** (12 - k) for k in range(5))
eq("binom", sf(p), 0.724)
N = NormalDist(50, 6)
eq("normal tail", sf(1 - N.cdf(56)), 0.159)
eq("z", (56 - 50) / 6, 1)
eq("1-Phi(1) 4dp", round(1 - NormalDist().cdf(1), 4), 0.1587)
eq("inverse", sf(N.inv_cdf(0.9), 3), 57.7)
lam = 3.2
eq("poisson", sf(1 - exp(-lam) * (1 + lam)), 0.829)

# solver root
eq("solver", sf(terms[-1]), 2.09)
print("ok")
