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

from math import sqrt, isclose, factorial, comb, exp, log, ceil
from fractions import Fraction as F
from statistics import NormalDist
nd = NormalDist()
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
po = lambda lam, k: exp(-lam)*lam**k/factorial(k)
b = lambda n, p, k: comb(n, k)*p**k*(1 - p)**(n - k)
Pc = lambda lam, k: sum(po(lam, j) for j in range(k + 1))   # P(X <= k)
count_marks("chapters/math.mixed.stats2.md", 127, 29)
def numint(f, a, b_, n=20000):
    h = (b_ - a)/n
    return sum((f(a + i*h) + 4*f(a + (i + 0.5)*h) + f(a + (i + 1)*h))*h/6 for i in range(n))
# 1-3
eq("1", sf(po(3, 2)), 0.224); eq("2", sf(1 - Pc(3, 1)), 0.801); eq("3", sf(exp(-1)), 0.368)
# 4-5
eq("4a", 3*4 + 2, 14); eq("4b", 9*5, 45); eq("5a", 10 - 7, 3); eq("5b", 4 + 9, 13)
# 6
eq("6 k", 1/8, 1/(0.5*16)); eq("6 area", numint(lambda x: x/8, 0, 4), 1, 1e-9); eq("6 p", numint(lambda x: x/8, 0, 2), 0.25, 1e-9)
# 7
eq("7", numint(lambda x: x*3*x*x, 0, 1), 0.75, 1e-9)
# 8
n = 5; sx = 45; sx2 = 445; eq("8 m", sx/n, 9); eq("8 s2", (sx2 - sx**2/n)/(n - 1), 10); assert sx**2/n == 405
xs8 = None
# 9
eq("9 z", (83 - 80)/sqrt(36/9), 1.5); eq("9 p", sf(1 - nd.cdf(1.5)), 0.0668)
# 10
eq("10 p", sf(sum(b(10, .5, k) for k in (9, 10))), 0.0107); eq("10 frac", 11/1024, sum(b(10, .5, k) for k in (9, 10))); assert 11/1024 < 0.05
# 11
eq("11", sf(1 - Pc(3, 2)), 0.577); eq("11 form", 1 - 8.5*exp(-3), 1 - Pc(3, 2))
# 12
assert 80 > 50 and 80*0.04 < 5; eq("12 lam", 80*0.04, 3.2); eq("12", sf(Pc(3.2, 2)), 0.380); eq("12 form", exp(-3.2)*(1 + 3.2 + 3.2**2/2), Pc(3.2, 2))
# 13
lam = log(5); eq("13a", sf(lam), 1.61); eq("13a4", round(lam, 3), 1.609); eq("13b", sf(1 - exp(-lam)*(1 + lam)), 0.478); eq("13b hand", sf(1 - 0.2*(1 + 1.609)), 0.478)
# 14
z = (19.5 - 25)/5; eq("14 z", z, -1.1); eq("14", sf(nd.cdf(z)), 0.136)
# 15
D = 40 - 25; V = 9 + 16; eq("15 m", D, 15); eq("15 v", V, 25); eq("15 p", sf(1 - nd.cdf((10 - 15)/5)), 0.841)
# 16
eq("16 ES", 4*12, 48); eq("16 VS", 4*4, 16); eq("16a", sf(1 - nd.cdf(0.5)), 0.309); eq("16 VT", 4**2*4, 64); eq("16 z", (50 - 48)/8, 0.25); eq("16b", sf(1 - nd.cdf(0.25)), 0.401)
# 17
k = 3/4
f17 = lambda x: k*x*(2 - x)
eq("17 area", numint(f17, 0, 2), 1, 1e-9); eq("17 form", 4 - 8/3, 4/3); eq("17 b", numint(f17, 1.5, 2), 5/32, 1e-9); eq("17 b sf", sf(5/32), 0.156)
eq("17 b form", 0.75*(4/3 - 1.125), 5/32); eq("17 E", numint(lambda x: x*f17(x), 0, 2), 1, 1e-9)
# 18
f18 = lambda x: 2/x**3
# E = int_1^inf 2/x^2 = 2 ; use substitution x = 1/u
eq("18 E", numint(lambda u: (1/u)*2*(1/u)**-3/u**2, 1e-9, 1, 40000), 2, 1e-3)
eq("18 m", sf(sqrt(2)), 1.41); eq("18 cdf", 1 - sqrt(2)**-2, 0.5)
# 19
eq("19 lo", sf(52.3 - 1.645), 50.7); eq("19 hi", sf(52.3 + 1.645), 53.9); eq("19 z", round(nd.inv_cdf(0.95), 3), 1.645); eq("19 se", 8/sqrt(64), 1)
# 20
se = sqrt(36/50); eq("20 se", round(se, 4), 0.8485); zz = (21.5 - 20)/se; eq("20 z", round(zz, 3), 1.768); eq("20 p", sf(1 - nd.cdf(zz)), 0.0385)
# 21
eq("21 p10", round(1 - Pc(6, 9), 4), 0.0839); eq("21 p11", round(1 - Pc(6, 10), 4), 0.0426); assert 1 - Pc(6, 9) > 0.05 >= 1 - Pc(6, 10)
# 22
eq("22 a", round(sum(b(20, .4, k) for k in range(5)), 4), 0.0510); eq("22 b3", round(sum(b(20, .4, k) for k in range(4)), 4), 0.0160)
assert sum(b(20, .4, k) for k in range(5)) > 0.05 > sum(b(20, .4, k) for k in range(4))
q = sum(b(20, .2, k) for k in range(4)); eq("22 c1", round(q, 4), 0.4114); eq("22 c", sf(1 - q), 0.589)
# 23
f23 = lambda x: x*(4 - x)/9
eq("23 area", numint(f23, 0, 3), 1, 1e-9); eq("23 form", 18 - 9, 9)
E = numint(lambda x: x*f23(x), 0, 3); E2 = numint(lambda x: x*x*f23(x), 0, 3)
eq("23 E", E, 7/4, 1e-9); eq("23 Ef", (36 - 20.25)/9, 1.75); eq("23 E2", E2, 3.6, 1e-9); eq("23 E2f", (81 - 48.6)/9, 3.6); eq("23 var", E2 - E*E, 0.5375, 1e-9); assert F(18, 5) - F(49, 16) == F(43, 80) and 0.5375 < 0.538 and 0.5375 > 0.5365
# 24
eq("24 z", round(nd.inv_cdf(0.995), 3), 2.576); eq("24 half", round(2.576*1.2, 2), 3.09); eq("24 lo", sf(410 - 2.576*1.2), 407); eq("24 hi", sf(410 + 2.576*1.2), 413); eq("24 lo4", sf(410 - 2.576*1.2, 4), 406.9)
assert not (406.9 <= 415 <= 413.1)
r = 2*2.576*12/4; eq("24 r", round(r, 2), 15.46); eq("24 n", round(r*r, 1), 238.9); assert ceil(r*r) == 239
assert 2*2.576*12/sqrt(239) < 4 < 2*2.576*12/sqrt(238)
# 25
assert 17 > 15; z = (21.5 - 17)/sqrt(17); eq("25 z", round(z, 3), 1.091); eq("25 p", sf(1 - nd.cdf(z)), 0.138); eq("25 tab", sf(1 - nd.cdf(1.09)), 0.138); assert 8 + 9 == 17
# 26
n = 100; sx = 5260; sx2 = 285000; s2 = (sx2 - sx**2/n)/(n - 1)
eq("26 m", sx/n, 52.6); eq("26 num", sx2 - sx**2/n, 8324); eq("26 s2", sf(s2), 84.1); eq("26 se2", round(s2/100, 4), 0.8408); eq("26 se", round(sqrt(s2/100), 4), 0.9170)
zt = (52.6 - 50)/sqrt(s2/100); eq("26 z", sf(zt), 2.84); assert zt > 1.96
# 27
eq("27 E", 4*150 + 6*60, 960); V = 4*400 + 6*100; eq("27 V", V, 2200); eq("27 parts", 1600 + 600, 2200)
z = (1000 - 960)/sqrt(V); eq("27 z", round(z, 3), 0.853); eq("27 p", sf(1 - nd.cdf(z)), 0.197)
mu = 150 - 2*60; var = 400 + 4*100; eq("27 mu", mu, 30); eq("27 var", var, 800); z2 = -30/sqrt(800); eq("27 z2", round(z2, 3), -1.061); eq("27 p2", sf(nd.cdf(z2)), 0.144)
# 28
z = (37.5 - 30)/sqrt(30); eq("28 z", round(z, 3), 1.369); eq("28 p", sf(1 - nd.cdf(z)), 0.0855); assert 1 - nd.cdf(z) > 0.05
# 29
eq("29 a1", round(Pc(2, 4), 4), 0.9473); eq("29 a", sf(1 - Pc(2, 4)), 0.0527)
eq("29 b", sf(Pc(4, 4)), 0.629); eq("29 b4", round(Pc(4, 4), 4), 0.6288)
eq("29 c1", sf(1 - Pc(2, 5)), 0.0166); eq("29 c0", round(Pc(2, 5), 4), 0.9834); eq("29 c2", sf(Pc(4, 5)), 0.785)
assert 1 - Pc(2, 5) < 1 - Pc(2, 4) and Pc(4, 5) > Pc(4, 4)
print("ok")
