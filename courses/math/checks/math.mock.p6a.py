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

from math import sqrt, isclose, factorial, exp, ceil
from statistics import NormalDist
nd = NormalDist()
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
po = lambda lam, k: exp(-lam)*lam**k/factorial(k)
count_marks("chapters/math.mock.p6a.md", 50, 9)
# Q1
eq("q1a", sf(po(4, 3)), 0.195); eq("q1b", sf(1 - po(2, 0) - po(2, 1)), 0.594); eq("q1b form", 1 - exp(-2)*3, 1 - po(2,0) - po(2,1))
# Q2
mu = 3*10 - 2*5; var = 9*4 + 4*9
eq("q2 mu", mu, 20); eq("q2 var", var, 72); eq("q2 var parts", 36 + 36, 72)
z = (25 - mu)/sqrt(var); eq("q2 z", sf(z), 0.589); eq("q2 p", sf(1 - nd.cdf(z)), 0.278); eq("q2 p tables", sf(1 - nd.cdf(0.59)), 0.278)
# Q3
eq("q3 lam", 3.2 + 1.8, 5); eq("q3", sf(po(2.5, 2)), 0.257)
# Q4
z4 = (25.5 - 20)/sqrt(20); eq("q4 z", round(z4, 2), 1.23); eq("q4 p", sf(1 - nd.cdf(z4)), 0.109); eq("q4 p tables", sf(1 - nd.cdf(1.23)), 0.109)
# exact is a little different but the approximation is the point
exact = 1 - sum(po(20, k) for k in range(26)); assert abs(exact - (1 - nd.cdf(z4))) < 0.01
# Q5: f = k/x^5 on [1, inf)
k = 4
# integral of k x^-5 from 1 to inf = k/4
eq("q5 area", k/4, 1)
eq("q5 E", 4/3, 4/3)
# numeric checks by Riemann sum on a transformed variable x = 1/u, dx = du/u^2, u in (0,1]
N = 200000
def integ(fn):
    h = 1.0/N
    return sum(fn((i + 0.5)*h)*h for i in range(N))
eq("q5 area num", integ(lambda u: 4*(1/u)**-5/u**2), 1, 1e-6)
eq("q5 E num", integ(lambda u: (1/u)*4*(1/u)**-5/u**2), 4/3, 1e-6)
m = 2**0.25; eq("q5 m", sf(m), 1.19); eq("q5 cdf", 1 - m**-4, 0.5)
# Q6
eq("q6 half", round(1.96*9/6, 2), 2.94); eq("q6 lo", sf(83.4 - 1.96*9/6), 80.5); eq("q6 hi", sf(83.4 + 1.96*9/6), 86.3)
eq("q6 z", round(nd.inv_cdf(0.975), 2), 1.96)
r = 2*1.96*9/4; eq("q6 sqrt n", round(r, 2), 8.82); eq("q6 n>", round(r*r, 1), 77.8); assert ceil(r*r) == 78
assert 2*1.96*9/sqrt(78) < 4 < 2*1.96*9/sqrt(77)
# Q7
eq("q7 mean", 300/12, 25); eq("q7 var", (8000 - 300**2/12)/11, 500/11); eq("q7 var sf", sf(500/11), 45.5); assert 300**2/12 == 7500
ph = 62/200; se = sqrt(ph*(1 - ph)/200); eq("q7 se", round(se, 4), 0.0327)
eq("q7 lo", sf(ph - 1.96*se), 0.246); eq("q7 hi", sf(ph + 1.96*se), 0.374)
# Q8
eq("q8 p", sf(po(4, 0) + po(4, 1)), 0.0916); eq("q8 form", exp(-4)*5, po(4, 0) + po(4, 1))
# the critical region for completeness: P(X<=0)=0.0183 < 0.05 < P(X<=1)
assert po(4, 0) < 0.05 < po(4, 0) + po(4, 1)
# Q9
se9 = 4/sqrt(25); eq("q9 se", se9, 0.8)
z9 = (498.9 - 500)/se9; eq("q9 z", z9, -1.375, 1e-9); assert z9 > -1.645
c = 500 + nd.inv_cdf(0.05)*se9; eq("q9 crit", round(c, 2), 498.68); eq("q9 z crit", round(nd.inv_cdf(0.05), 3), -1.645)
eq("q9 crit hand", round(500 - 1.645*0.8, 2), 498.68)
z2 = (c - 498)/se9; eq("q9 z2", round(z2, 3), 0.855); eq("q9 typeII", sf(1 - nd.cdf(z2)), 0.196)
eq("q9 typeII rounded crit", sf(1 - nd.cdf((498.68 - 498)/0.8)), 0.198)
print("ok")
