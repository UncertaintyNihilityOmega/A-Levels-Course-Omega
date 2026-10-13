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
b = lambda n, p, k: comb(n, k)*p**k*(1 - p)**(n - k)
count_marks("chapters/math.mixed.stats1.md", 123, 29)
# 1
xs = [3, 7, 7, 9, 12, 15, 16, 21]; eq("1 mean", sum(xs)/8, 11.25); eq("1 med", (xs[3] + xs[4])/2, 10.5); assert sum(xs) == 90
# 2
eq("2 var", 800/5 - 12**2, 16)
# 3
eq("3", 50 + (-12)/8, 48.5)
# 4
assert factorial(5) == 120 and comb(8, 3) == 56
# 5
assert factorial(5)//(2*2) == 30 or factorial(5)/4 == 30
# 6
eq("6 and", 0.4*0.5, 0.2); eq("6 or", 0.4 + 0.5 - 0.2, 0.7)
# 7
assert sum(1 for i in range(1, 7) for j in range(1, 7) if i + j == 8) == 5
# 8
eq("8", sf(b(10, 0.3, 4)), 0.200)
# 9
P = [0.4, 0.3, 0.2, 0.1]; E = sum(i*p for i, p in enumerate(P)); E2 = sum(i*i*p for i, p in enumerate(P))
eq("9 E", E, 1); eq("9 E2", E2, 2); eq("9 var", E2 - E*E, 1)
# 10
eq("10", sf(1 - nd.cdf(1.5)), 0.0668)
# 11
area = 2*6; eq("11 area", area, 12); eq("11 per", area/24, 0.5); eq("11 area2", 30*0.5, 15); eq("11 h", 15/4, 3.75)
# 12
f = [5, 15, 40, 30, 10]; cf = [sum(f[:i+1]) for i in range(5)]; assert cf == [5, 20, 60, 90, 100]
eq("12 med", 20 + (50 - 20)/40*20, 35); eq("12 p80", sf(40 + (80 - 60)/30*40), 66.7)
# 13
S = 10*12 + 15*16; eq("13 S", S, 360); eq("13 mean", S/25, 14.4)
A2 = 10*(4 + 144); B2 = 15*(9 + 256); assert (A2, B2) == (1480, 3975)
var = (A2 + B2)/25 - 14.4**2; eq("13 var", var, 10.84); eq("13 parts", (A2 + B2)/25, 218.2); eq("13 sq", 14.4**2, 207.36); eq("13 sd", sf(sqrt(var)), 3.29)
# 14
assert factorial(5)*factorial(4) == 2880 and 5 + 4 == 9
# 15
assert 9*8*7*6 == 3024 and 4*8*7*6 == 1344
import itertools
nums = [p for p in itertools.permutations(range(1, 10), 4)]
assert len(nums) == 3024 and sum(1 for p in nums if p[-1] % 2 == 0) == 1344
# 16
pab = 0.5 + 0.4 - 0.7; eq("16 pab", pab, 0.2); eq("16 cond", pab/0.4, 0.5); eq("16 prod", 0.5*0.4, pab)
# 17
eq("17", sf(F(13, 28)), 0.464) if False else None
assert F(5, 8)*F(4, 7) + F(3, 8)*F(2, 7) == F(13, 28) and F(20, 56) + F(6, 56) == F(13, 28); eq("17 dec", sf(13/28), 0.464)
# 18
eq("18a", sf(sum(b(15, 0.2, k) for k in range(3))), 0.398); eq("18 mean", 15*0.2, 3); eq("18 var", 15*0.2*0.8, 2.4)
# 19
eq("19a", sf(0.75**4*0.25), 0.0791); eq("19b", sf(1 - 0.75**3), 0.578)
# 20
z1 = nd.inv_cdf(0.2); z2 = nd.inv_cdf(0.9); sig = 20/(z2 - z1); mu = 30 - z1*sig
eq("20 z1", round(z1, 4), -0.8416); eq("20 z2", round(z2, 4), 1.2816); eq("20 diff", round(z2 - z1, 4), 2.1232)
eq("20 sig", sf(sig), 9.42); eq("20 mu", sf(mu), 37.9)
eq("20 mu hand", sf(30 + 0.8416*9.42), 37.9)
# 21
assert 100*0.4 > 5 and 100*0.6 > 5; eq("21 var", 100*0.4*0.6, 24)
z = 4.5/sqrt(24); eq("21 z", round(z, 3), 0.919); eq("21 p", sf(1 - nd.cdf(z)), 0.179); assert abs(sum(b(100, 0.4, k) for k in range(45, 101)) - 0.179) < 0.001
# 22
m = 1020/40; v = 26500/40 - m*m
eq("22 m", m, 25.5); eq("22 var", v, 12.25); eq("22 parts", 662.5 - 650.25, 12.25); eq("22 sd", sqrt(v), 3.5)
z = (20 - m)/3.5; eq("22 z", round(z, 3), -1.571); eq("22 p", sf(nd.cdf(z)), 0.058); eq("22 p4", round(1 - 0.9419, 4), 0.0581); eq("22 tables", sf(nd.cdf(-1.57)), 0.0582); eq("22 phi", round(nd.cdf(1.571), 4), 0.9419)
m2 = 1051/41; v2 = 27461/41 - m2**2
eq("22 m2", sf(m2), 25.6); eq("22 m2 4", round(m2, 3), 25.634); eq("22 var2", round(v2, 2), 12.67); eq("22 sd2", sf(sqrt(v2)), 3.56); assert 26500 + 31**2 == 27461
# 23
assert factorial(7) == 5040 and 2*factorial(6) == 1440 and 5040 - 1440 == 3600
assert factorial(5)*factorial(3) == 720 and 2*factorial(5) == 240; assert F(240, 5040) == F(1, 21); eq("23c", sf(1/21), 0.0476)
# brute force for (a)
cnt = sum(1 for p in itertools.permutations(range(7)) if abs(p.index(0) - p.index(1)) != 1); assert cnt == 3600
# 24
pp = 0.02*0.95 + 0.98*0.04; eq("24 a", pp, 0.0582); eq("24 parts", 0.02*0.95, 0.019); eq("24 parts2", 0.98*0.04, 0.0392)
eq("24 b", sf(0.019/pp), 0.326)
n1 = 0.02*0.95**2; n2 = 0.98*0.04**2; eq("24 n1", n1, 0.01805); eq("24 n2", n2, 0.001568); eq("24 c", sf(n1/(n1 + n2)), 0.920)
# 25
k = F(1, 30); assert sum(k*x*x for x in range(1, 5)) == 1 and 1 + 4 + 9 + 16 == 30
E = sum(k*x**3 for x in range(1, 5)); E2 = sum(k*x**4 for x in range(1, 5))
assert E == F(10, 3) and E2 == F(354, 30) and 1 + 8 + 27 + 64 == 100 and 1 + 16 + 81 + 256 == 354
eq("25 E2", float(E2), 11.8); eq("25 var", sf(float(E2 - E*E)), 0.689)
pr = {x: k*x*x for x in range(1, 5)}
pair = sum(pr[a]*pr[5 - a] for a in range(1, 5) if 5 - a in pr); assert pair == F(2*52, 900)
eq("25 d", sf(float(pair)), 0.116)
# 26
p = sum(b(10, 0.8, r) for r in (8, 9, 10)); eq("26 a", sf(p), 0.678)
eq("26 b", sf(comb(5, 3)*0.6778**3*0.3222**2), 0.323); eq("26 b exact", sf(comb(5, 3)*p**3*(1-p)**2), 0.323); eq("26 c", sf(1/0.6778), 1.48)
# 27
z = nd.inv_cdf(0.04); eq("27 z", round(z, 3), -1.751); mu = 49.5 - z*0.8; eq("27 mu", sf(mu), 50.9)
mu9 = 50.9; zz = (52 - mu9)/0.8; eq("27 z2", round(zz, 3), 1.375); pq = 1 - nd.cdf(zz); eq("27 b", sf(pq), 0.0846)
eq("27 c", sf((1 - pq)**20 + 20*pq*(1 - pq)**19), 0.486); eq("27 c 4dp", sf(0.9154**20 + 20*0.0846*0.9154**19), 0.486)
# 28
assert 50*0.5 > 5; eq("28 var", 50*0.5*0.5, 12.5)
zl = (19.5 - 25)/sqrt(12.5); zu = (28.5 - 25)/sqrt(12.5)
eq("28 zl", round(zl, 3), -1.556); eq("28 zu", round(zu, 3), 0.990); eq("28 p", sf(nd.cdf(zu) - nd.cdf(zl)), 0.779)
eq("28 tables", round(nd.cdf(0.99), 4), 0.8389); eq("28 tables2", round(nd.cdf(-1.556), 4), 0.0599)
# 29
pr = [F(comb(4, r)*comb(6, 3 - r), 120) for r in range(4)]
assert pr == [F(1, 6), F(1, 2), F(3, 10), F(1, 30)] and sum(pr) == 1 and comb(10, 3) == 120
E = sum(r*p for r, p in enumerate(pr)); assert E == F(6, 5); assert F(1, 2) + F(6, 10) + F(3, 30) == F(6, 5)
eq("29 c", sf(b(8, 0.3, 2)), 0.296)
print("ok")
