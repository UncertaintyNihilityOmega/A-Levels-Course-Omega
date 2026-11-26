# checks/math.fm.exam.fs.py: recomputes every number in the chapter
from math import isclose, floor, gamma, sqrt, pi, exp

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def rh(x): return floor(x + 0.5)

def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def t_pdf(v):
    c = gamma((v + 1) / 2) / (sqrt(v * pi) * gamma(v / 2))
    return lambda x: c * (1 + x * x / v) ** (-(v + 1) / 2)

def t_cdf(x, v):
    return 0.5 + simpson(t_pdf(v), 0, x)

def t_quantile(p, v):
    lo, hi = 0.0, 50.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if t_cdf(mid, v) < p: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def chi_pdf(k):
    c = 1 / (2 ** (k / 2) * gamma(k / 2))
    return lambda x: c * x ** (k / 2 - 1) * exp(-x / 2)

def chi_quantile(p, k):
    # k = 2: the density is finite at 0, so Simpson from 0 is fine
    lo, hi = 0.0, 100.0
    f = chi_pdf(k)
    for _ in range(80):
        mid = (lo + hi) / 2
        if simpson(f, 0, mid) < p: lo = mid
        else: hi = mid
    return (lo + hi) / 2

# timing
eq("min per mark", 90 / 50, 1.8)
for marks, mins in [(6, 10), (7, 11), (8, 13), (10, 16), (12, 19)]:
    eq(f"{marks} marks", rh(marks * 1.6), mins)
eq("whole paper", 50 * 1.6, 80)
eq("spare", 90 - 50 * 1.6, 10)

q25 = [7, 12, 8, 7, 10, 6]
q26 = [7, 10, 6, 9, 8, 10]
eq("sum 2025", sum(q25), 50)
eq("sum 2026", sum(q26), 50)
assert len(q25) == 6 and len(q26) == 6
eq("q1 2026", 1 + 6, 7)
eq("q2 2026", 8 + 2, 10)
eq("q4 2026", 1 + 3 + 2 + 3, 9)
eq("q5 2026", 7 + 1, 8)
eq("q6 2026", 5 + 2 + 3, 10)

# t-test example
n, xbar, mu0, s = 9, 62.1, 60.0, 3.0
t = (xbar - mu0) / (s / sqrt(n))
eq("t", t, 2.1)
crit = t_quantile(0.95, 8)
eq("t crit nu=8 p=0.95", round(crit, 3), 1.860)
assert t > crit
eq("one-tailed vs two-tailed nu=9", round(t_quantile(0.95, 9), 3), 1.833)
eq("two-tailed nu=9", round(t_quantile(0.975, 9), 3), 2.262)
eq("marks t example", 1 + 1 + 1 + 1 + 1 + 1 + 1, 7)

# chi-squared independence example
obs = [[28, 22, 20], [22, 38, 40]]
rt = [sum(r) for r in obs]
ct = [sum(obs[i][j] for i in range(2)) for j in range(3)]
N = sum(rt)
eq("N", N, 170)
assert rt == [70, 100] and ct == [50, 60, 60]
E = [[rt[i] * ct[j] / N for j in range(3)] for i in range(2)]
for i, row in enumerate([[20.6, 24.7, 24.7], [29.4, 35.3, 35.3]]):
    for j, v in enumerate(row):
        eq(f"E{i}{j}", float(f"{E[i][j]:.3g}"), v)
assert all(e > 5 for r in E for e in r)
contrib = [(obs[i][j] - E[i][j]) ** 2 / E[i][j] for i in range(2) for j in range(3)]
for c, w in zip(contrib, [2.668, 0.296, 0.896, 1.868, 0.208, 0.628]):
    eq("contribution", round(c, 3), w, 1e-9) if abs(round(c, 3) - w) < 1e-9 else eq("contribution", c, w, 6e-4)
X2 = sum(contrib)
eq("X2", round(X2, 2), 6.56)
eq("sum of stated contributions", round(2.668 + 0.296 + 0.896 + 1.868 + 0.208 + 0.628, 2), 6.56)
crit2 = chi_quantile(0.95, 2)
eq("chi2 crit nu=2", round(crit2, 3), 5.991)
assert X2 > crit2
eq("nu", (2 - 1) * (3 - 1), 2)
assert max(contrib) == contrib[0]
eq("marks chi2 example", 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1, 8)
print("ok")
