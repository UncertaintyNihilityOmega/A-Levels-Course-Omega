# data/fm-chisq-design.py: scratch calculations used to choose the data of math.fm.chisq (kept so the choices can be re-derived).
from math import comb, exp, factorial, erf, sqrt, lgamma
from statistics import NormalDist

N01 = NormalDist()


def chi2_cdf(x, v, n=4000):
    if x <= 0:
        return 0.0
    if v == 1:
        return erf(sqrt(x / 2))
    if v == 2:
        return 1 - exp(-x / 2)
    f = lambda t: t ** (v / 2 - 1) * exp(-t / 2) / (2 ** (v / 2) * exp(lgamma(v / 2)))
    h = x / n
    s = f(0) + f(x) + sum((4 if i % 2 else 2) * f(i * h) for i in range(1, n))
    return s * h / 3


def chi2_inv(p, v):
    lo, hi = 0.0, 400.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if chi2_cdf(mid, v) < p else (lo, mid)
    return (lo + hi) / 2


def x2(o, e):
    return sum((a - b) ** 2 / b for a, b in zip(o, e))


def show(name, o, e, v, alpha_p=0.95):
    print(name, "N", sum(o), "sumE", round(sum(e), 6), "E", [round(a, 3) for a in e], "X2", round(x2(o, e), 4),
          "v", v, "crit", round(chi2_inv(alpha_p, v), 3), "p", round(1 - chi2_cdf(x2(o, e), v), 4))


# binomial p given
pm = [comb(5, k) * 0.2 ** k * 0.8 ** (5 - k) for k in range(6)]
e = [200 * p for p in pm]
print([round(a, 3) for a in e])
e2 = e[:3] + [sum(e[3:])]
show("bin p given", [60, 88, 40, 12], e2, 3)

# Poisson lambda estimated
obs = [12, 27, 28, 18, 9, 4, 2]
lam = sum(i * f for i, f in enumerate(obs)) / sum(obs)
pp = [exp(-lam) * lam ** k / factorial(k) for k in range(6)]
pp.append(1 - sum(pp))
e = [100 * p for p in pp]
print("lam", lam, [round(a, 3) for a in e])
e2 = e[:5] + [e[5] + e[6]]
o2 = obs[:5] + [obs[5] + obs[6]]
show("poisson", o2, e2, 4)

# geometric p estimated
mean = 2.6
p = 1 / mean
q = 1 - p
e = [100 * q ** (r - 1) * p for r in range(1, 6)] + [100 * q ** 5]
show("geo", [41, 22, 14, 11, 5, 7], e, 4)

# normal given
bounds = [250 - 6, 250 - 2, 250 + 2, 250 + 6]
cdf = [N01.cdf((b - 250) / 4) for b in bounds]
pr = [cdf[0], cdf[1] - cdf[0], cdf[2] - cdf[1], cdf[3] - cdf[2], 1 - cdf[3]]
e = [200 * a for a in pr]
show("normal", [18, 45, 70, 52, 15], e, 4)

# pdf x/8
e = [160 * a for a in [1 / 16, 3 / 16, 5 / 16, 7 / 16]]
show("pdf", [14, 26, 55, 65], e, 3)

# June 2025 shape: binomial B(6, p) p estimated
obs = [48, 78, 49, 18, 5, 2, 0]
n = sum(obs)
mean = sum(i * f for i, f in enumerate(obs)) / n
ph = mean / 6
print("mean", mean, "p", ph)
e = [n * comb(6, k) * ph ** k * (1 - ph) ** (6 - k) for k in range(7)]
print([round(a, 3) for a in e])
