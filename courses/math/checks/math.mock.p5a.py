# --- mark counting: every [M1]/[A1]/[B1] token in an answer must add up to the question's [n marks] ---
import re, pathlib, sys
def count_marks(path, total, expect_qs=None):
    text = pathlib.Path(path).read_text(encoding="utf8")
    blocks = re.split(r"(?m)^Q: ", text)[1:]
    grand = 0
    for i, b in enumerate(blocks, 1):
        b = b.split("\n:::")[0]
        m = re.match(r"\[(\d+) marks?\]", b)
        assert m, f"question {i}: no [n marks]"
        n = int(m.group(1))
        ans = b.split("\nA:", 1)[1]
        got = sum(int(d) for d in re.findall(r"\[(?:M|A|B|C|SC)(\d)(?:ft)?\]", ans))
        assert got == n, f"question {i}: [{n} marks] but the scheme shows {got}"
        grand += n
    assert grand == total, f"paper total {grand}, should be {total}"
    if expect_qs: assert len(blocks) == expect_qs, f"{len(blocks)} questions"

from math import sqrt, isclose, factorial, comb
from fractions import Fraction as F
from statistics import NormalDist
nd = NormalDist()
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
count_marks("chapters/math.mock.p5a.md", 50, 9)
# Q1
m = 20 + 15/12; v = 240/12 - (15/12)**2
eq("q1 m", m, 21.25); eq("q1 var", v, 18.4375); eq("q1 sd", sf(sqrt(v)), 4.29)
# Q2
assert factorial(10)//(6*6*2) == 50400 and factorial(10) % (6*6*2) == 0
assert factorial(9)//(6*6) == 10080
# brute-force check of (b) on a smaller scale is unnecessary; count STATISTICS arrangements by formula only
# Q3
assert comb(5,2)*comb(6,2) == 150 and comb(5,3)*comb(6,1) == 60 and comb(5,4) == 5
assert 150 + 60 + 5 == 215 == comb(11,4) - comb(6,4) - 5*comb(6,3)
assert (comb(11,4), comb(6,4), 5*comb(6,3)) == (330, 15, 100)
# Q4
pl = 0.3*0.2 + 0.7*0.05
eq("q4 late", pl, 0.095); eq("q4 b", sf(0.06/pl), 0.632); assert F(12, 19) == F(60, 95)
# Q5
f = [6, 14, 30, 24, 16]; mid = [5, 15, 25, 35, 50]
cf = [sum(f[:i+1]) for i in range(5)]; assert cf == [6, 20, 50, 74, 90]
med = 20 + (45 - 20)/30*10; q1 = 20 + 2.5/30*10; q3 = 30 + 17.5/24*10
eq("q5 med", sf(med), 28.3); eq("q5 q1", round(q1, 2), 20.83); eq("q5 q3", round(q3, 2), 37.29); eq("q5 iqr", sf(q3 - q1), 16.5)
sx = sum(a*b for a, b in zip(f, mid)); sxx = sum(a*b*b for a, b in zip(f, mid))
assert [a*b for a, b in zip(f, mid)] == [30, 210, 750, 840, 800] and sx == 2630
assert [a*b*b for a, b in zip(f, mid)] == [150, 3150, 18750, 29400, 40000] and sxx == 91450
mean = sx/90; eq("q5 mean", sf(mean), 29.2); eq("q5 sd", sf(sqrt(sxx/90 - round(mean, 2)**2)), 12.7); eq("q5 sd exact", sf(sqrt(sxx/90 - mean**2)), 12.7)
# Q6
k = 0.15; assert isclose(0.1 + 0.3 + 4*k, 1)
P = [0.1, 0.3, k, 3*k]; eq("q6 probs", 3*k, 0.45)
E = sum(x*p for x, p in zip((1,2,3,4), P)); E2 = sum(x*x*p for x, p in zip((1,2,3,4), P))
eq("q6 E", E, 2.95); eq("q6 E2", E2, 9.85); eq("q6 var", E2 - E*E, 1.1475); eq("q6 var sf", sf(E2 - E*E), 1.15)
eq("q6 terms", 0.1 + 0.6 + 0.45 + 1.8, 2.95); eq("q6 terms2", 0.1 + 1.2 + 1.35 + 7.2, 9.85)
# Q7
eq("q7a", sf(0.7**3*0.3), 0.103); eq("q7b", sf(1/0.3), 3.33); eq("q7c", sf(0.7**5), 0.168)
# Q8
tot = comb(9, 3); assert tot == 84
pr = [F(comb(5, 3), 84), F(4*comb(5, 2), 84), F(comb(4, 2)*5, 84), F(comb(4, 3), 84)]
assert pr == [F(5, 42), F(10, 21), F(5, 14), F(1, 21)] and sum(pr) == 1
assert [F(5, 42), F(20, 42), F(15, 42), F(2, 42)] == pr
Ex = sum(i*p for i, p in enumerate(pr)); Ex2 = sum(i*i*p for i, p in enumerate(pr))
assert Ex == F(4, 3) and Ex2 == F(7, 3) and Ex2 - Ex**2 == F(5, 9)
assert F(10, 21) + F(10, 14) + F(3, 21) == F(4, 3) and F(10, 21) + F(20, 14) + F(9, 21) == F(7, 3)
# Q9
p = 1 - nd.cdf(1.5); q = 1 - p
eq("q9a", round(p, 4), 0.0668); eq("q9 phi", round(nd.cdf(1.5), 4), 0.9332)
z = nd.inv_cdf(0.85); eq("q9 z", round(z, 3), 1.036); eq("q9 m", sf(160 + 20*z), 181); eq("q9 20z", round(20*z, 2), 20.73)
eq("q9 m tables", sf(160 + 20*1.04), 181)
for pp in (p, 0.0668):
    qq = 1 - pp
    eq("q9c", sf(1 - qq**10 - 10*pp*qq**9), 0.141)
mu = 200*p; var = 200*p*q
eq("q9 np", round(mu, 2), 13.36); eq("q9 npq", round(var, 2), 12.47); assert mu > 5 and 200*q > 5
zz = (20.5 - mu)/sqrt(var); eq("q9 z2", round(zz, 2), 2.02)
eq("q9 d", sf(1 - nd.cdf(zz), 3), 0.0216); eq("q9 d tables", round(1 - nd.cdf(2.02), 4), 0.0217)
print("ok")
