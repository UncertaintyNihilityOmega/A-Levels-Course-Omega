# checks/math.fm.mock.p4.py: recomputes every number in Mock Paper 4 (Further Probability and Statistics).
# Standard library only: normal quantiles from NormalDist, t and chi-squared percentage points by Simpson
# integration of the density and bisection, Wilcoxon values by counting every sign pattern, Simpson for integrals.
import re
import pathlib
from fractions import Fraction as F
from math import isclose, sqrt, lgamma, exp, comb, pi, log, factorial
from statistics import NormalDist

N01 = NormalDist()


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    return sum((f(a + i * h) + 4 * f(a + (i + .5) * h) + f(a + (i + 1) * h)) * h / 6 for i in range(n))


# ---- mark counting: the tokens in every answer must add up to the question's [n marks] ----
TOKEN = re.compile(r"^(?:(?:DM|M|A|B)\d(?: FT)?\s*)+$")


def count_marks(path, total, expect_qs):
    text = pathlib.Path(path).read_text(encoding="utf8")
    blocks = re.split(r"(?m)^Q: ", text)[1:]
    grand, spread = 0, []
    for i, b in enumerate(blocks, 1):
        b = b.split("\n:::")[0]
        m = re.match(r"\[(\d+) marks?\]", b)
        assert m, f"question {i}: no [n marks]"
        n = int(m.group(1))
        ans = b.split("\nA:", 1)[1]
        got = 0
        for grp in re.findall(r"\[([^\]\n]*)\]", ans):
            if TOKEN.match(grp):
                got += sum(int(d) for d in re.findall(r"(?:DM|M|A|B)(\d)", grp))
        assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
        qpart = b.split("\nA:", 1)[0]
        parts = [int(x) for x in re.findall(r"(?<!\w)\[(\d+)\](?!\()", qpart)]
        if parts:
            assert sum(parts) == n, f"question {i}: part marks {parts} do not add to {n}"
        grand += n
        spread.append(n)
    assert grand == total, f"paper total {grand}, should be {total}"
    assert len(blocks) == expect_qs, f"{len(blocks)} questions"
    return spread


spread = count_marks("chapters/math.fm.mock.p4.md", 50, 6)
assert spread == [7, 10, 8, 7, 9, 9], spread


# ---- distribution helpers ----
def t_pdf(x, v):
    return exp(lgamma((v + 1) / 2) - lgamma(v / 2) - 0.5 * log(v * pi) - (v + 1) / 2 * log(1 + x * x / v))


def t_cdf(x, v, n=1000):
    h = x / n
    s = t_pdf(0, v) + t_pdf(x, v) + sum((4 if i % 2 else 2) * t_pdf(i * h, v) for i in range(1, n))
    return 0.5 + s * h / 3


def t_inv(p, v):
    lo, hi = 0.0, 70.0
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_cdf(mid, v) < p else (lo, mid)
    return lo


def chi2_cdf(x, v, n=2000):
    top = sqrt(x)
    c = 2 / (2 ** (v / 2) * exp(lgamma(v / 2)))
    g = lambda u: c * u ** (v - 1) * exp(-u * u / 2)
    h = top / n
    return (g(0) + g(top) + sum((4 if i % 2 else 2) * g(i * h) for i in range(1, n))) * h / 3


def chi2_inv(p, v):
    lo, hi = 0.0, 300.0
    for _ in range(70):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if chi2_cdf(mid, v) < p else (lo, mid)
    return (lo + hi) / 2


def signed_rank_crit(n, a):
    """largest T with P(T <= t) <= a under H0 (sum of the ranks of one sign, 2^n patterns)."""
    dist = [1]
    for k in range(1, n + 1):
        new = [0] * (len(dist) + k)
        for i, v in enumerate(dist):
            new[i] += v
            new[i + k] += v
        dist = new
    cum, best = 0, None
    for t, v in enumerate(dist):
        cum += v
        if F(cum, 2 ** n) <= a:
            best = t
        else:
            break
    return best


# ---- Q1: two-sample normal test ----
nP, sP, SP = 45, 1962, 1584
nQ, sQ, SQ = 60, 2472, 2891
xb, yb = sP / nP, sQ / nQ
eq("q1 xbar", xb, 43.6); eq("q1 ybar", yb, 41.2)
vP, vQ = SP / (nP - 1), SQ / (nQ - 1)
eq("q1 sP2", vP, 36); eq("q1 sQ2", vQ, 49)
eq("q1 terms", vP / nP, 0.8); eq("q1 terms", round(vQ / nQ, 4), 0.8167, 1e-12)
se = sqrt(vP / nP + vQ / nQ)
eq("q1 se", round(se, 4), 1.2715, 1e-12)
z = (xb - yb) / se
eq("q1 z", round(z, 2), 1.89, 1e-12)
crit = N01.inv_cdf(0.95)
eq("q1 crit", round(crit, 3), 1.645, 1e-12)
assert z > crit
eq("q1 p", round(1 - N01.cdf(z), 4), 0.0295, 1e-12)
assert round(1 - N01.cdf(z), 4) < 0.05

# ---- Q2: piecewise PDF ----
f = lambda x, k: k * x if 0 <= x <= 1 else (k / 3) * (4 - x) if 1 < x <= 4 else 0
area = lambda k: simpson(lambda x: f(x, k), 0, 1) + simpson(lambda x: f(x, k), 1, 4)
eq("q2a area", area(0.5), 1)
assert F(1, 2) / 1 == F(1, 2) and F(1, 2) + F(3, 2) == 2
def Fcdf(x):
    return simpson(lambda t: f(t, 0.5), 0, x) if x <= 1 else simpson(lambda t: f(t, 0.5), 0, 1) + simpson(lambda t: f(t, 0.5), 1, x)
for x in (1, 1.5, 2.5, 3.9, 4):
    eq("q2b F", Fcdf(x), (-x * x + 8 * x - 4) / 12, 1e-9)
eq("q2b F(1)", Fcdf(1), 0.25); eq("q2b F(4)", Fcdf(4), 1)
m = 4 - sqrt(6)
eq("q2c median", Fcdf(m), 0.5, 1e-9)
eq("q2c m", round(m, 2), 1.55, 1e-12)
assert 1 < m < 4 and 4 + sqrt(6) > 4
assert F(1) * (m * m - 8 * m + 10) < 1e-12
# Y = X^2: G(y) = F(sqrt y); g(y) = G'(y)
G = lambda y: Fcdf(sqrt(y))
for y in (1.5, 4, 9, 14):
    gnum = (G(y + 1e-4) - G(y - 1e-4)) / 2e-4
    eq("q2d g", gnum, (4 - sqrt(y)) / (12 * sqrt(y)), 1e-5)
    eq("q2d g via f", gnum, f(sqrt(y), 0.5) / (2 * sqrt(y)), 1e-5)
    eq("q2d G", G(y), (-y + 8 * sqrt(y) - 4) / 12, 1e-8)
eq("q2d check y=4", (4 - 2) / (12 * 2), 1 / 12)
eq("q2d total", simpson(lambda y: (4 - sqrt(y)) / (12 * sqrt(y)), 1, 16) + 0.25, 1, 1e-7)   # g integrates to 3/4 on (1,16)

# ---- Q3: chi-squared goodness of fit ----
E = [150 * comb(4, r) * 0.3 ** r * 0.7 ** (4 - r) for r in range(5)]
for got, want in zip(E[:3], (36.015, 61.74, 39.69)):
    eq("q3 table", got, want, 1e-9)
eq("q3a E3", E[3], 11.34); eq("q3a E4", E[4], 1.215)
eq("q3 sum", sum(E), 150, 1e-9)
assert E[4] < 5 <= E[3]
eq("q3 check sum", 150 - 36.015 - 61.74 - 39.69, 12.555, 1e-9)
O = [24, 58, 46, 19, 3]
assert sum(O) == 150
Oc = O[:3] + [O[3] + O[4]]; Ec = E[:3] + [E[3] + E[4]]
contrib = [(o - e) ** 2 / e for o, e in zip(Oc, Ec)]
for got, want in zip(contrib, (4.008, 0.227, 1.003, 7.105)):
    eq("q3 contributions", round(got, 3), want, 1e-12)
X2 = sum(contrib)
eq("q3 X2", round(X2, 1), 12.3, 1e-12)
cv = chi2_inv(0.95, 3)
eq("q3 crit", round(cv, 3), 7.815, 1e-3)
assert X2 > cv
assert X2 > chi2_inv(0.99, 3)    # significant even at 1%

# ---- Q4: pooled variance and t interval ----
n1, s1, q1 = 8, 196, 4830
n2, s2, q2 = 10, 229, 5291
S1 = q1 - s1 ** 2 / n1; S2 = q2 - s2 ** 2 / n2
eq("q4 S1", S1, 28); eq("q4 S2", S2, 46.9, 1e-9)
sp2 = (S1 + S2) / (n1 + n2 - 2)
eq("q4 sp2", sp2, 4.68125, 1e-9); eq("q4 sp2 3sf", float(f"{sp2:.3g}"), 4.68, 1e-12)
eq("q4 means", s1 / n1, 24.5); eq("q4 means", s2 / n2, 22.9)
dm = s1 / n1 - s2 / n2
eq("q4 diff", dm, 1.6, 1e-12)
tcrit = t_inv(0.975, 16)
eq("q4 t", round(tcrit, 3), 2.120, 1e-3)
sdiff = sqrt(sp2 * (1 / n1 + 1 / n2))
eq("q4 se", round(sdiff, 4), 1.0263, 1e-12)
lo, hi = dm - 2.120 * sdiff, dm + 2.120 * sdiff
eq("q4 lo", round(lo, 3), -0.576, 1e-12); eq("q4 hi", round(hi, 2), 3.78, 1e-12)
assert lo < 0 < hi

# ---- Q5: Wilcoxon matched pairs and the sign test ----
before = [52, 61, 48, 70, 55, 66, 43, 58, 64]
after = [61, 75, 45, 81, 61, 61, 56, 65, 79]
d = [a - b for a, b in zip(after, before)]
assert d == [9, 14, -3, 11, 6, -5, 13, 7, 15]
order = sorted(abs(x) for x in d)
assert len(set(order)) == 9 and 0 not in d
rank = [order.index(abs(x)) + 1 for x in d]
assert rank == [5, 8, 1, 6, 3, 2, 7, 4, 9]
neg = sum(r for r, x in zip(rank, d) if x < 0); pos = sum(r for r, x in zip(rank, d) if x > 0)
assert neg == 3 and pos == 42 and neg + pos == 45
eq("q5 crit one-tailed 5%", signed_rank_crit(9, F(5, 100)), 8)
assert neg <= 8
assert signed_rank_crit(9, F(1, 100)) == 3 and neg <= 3     # also significant at 1% (one-tailed): not quoted
S = sum(1 for x in d if x > 0)
assert S == 7
p = sum(comb(9, k) for k in range(7, 10)) / 2 ** 9
eq("q5b p", round(p, 4), 0.0898, 1e-12)
assert comb(9, 7) + comb(9, 8) + comb(9, 9) == 36 + 9 + 1
assert p > 0.05

# ---- Q6: probability generating function ----
k = F(1, 8)
G = lambda t: k * (1 + t) * (3 + t)
assert G(1) == 1
coef = [F(3, 8), F(4, 8), F(1, 8)]
assert coef == [k * 3, k * 4, k * 1]
mean = sum(i * c for i, c in enumerate(coef)); ex2 = sum(i * i * c for i, c in enumerate(coef))
assert mean == F(3, 4) and ex2 - mean ** 2 == F(7, 16)
assert (2 * 1 + 4) * k == F(3, 4) and 2 * k == F(1, 4)      # G'(1), G''(t)
assert F(1, 4) + F(3, 4) - F(9, 16) == F(7, 16)
# W = X + Y, Y ~ Po(2)
py = lambda r: exp(-2) * 2 ** r / factorial(r)
pw1 = float(coef[0]) * py(1) + float(coef[1]) * py(0)
eq("q6d P(W=1)", pw1, 1.25 * exp(-2), 1e-12)
eq("q6d value", round(pw1, 3), 0.169, 1e-12)
# G_W'(0) by finite differences
GW = lambda t: float(G(F(t))) * exp(2 * (t - 1)) if False else (1 + t) * (3 + t) / 8 * exp(2 * (t - 1))
eq("q6d G_W'(0)", (GW(1e-6) - GW(-1e-6)) / 2e-6, 1.25 * exp(-2), 1e-6)
eq("q6c G_W(1)", GW(1), 1)
print("ok")
