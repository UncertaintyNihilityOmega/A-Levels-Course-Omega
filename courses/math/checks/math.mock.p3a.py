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

from math import sqrt, isclose, sin, cos, tan, radians, degrees, atan, asin, acos, log, exp, e, pi
from fractions import Fraction as F
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def simpson(f, a, b, N=20000):
    hh = (b - a)/N
    return sum((f(a + i*hh) + 4*f(a + (i + .5)*hh) + f(a + (i + 1)*hh))*hh/6 for i in range(N))

count_marks("chapters/math.mock.p3a.md", 75, 11)
# Q1
x = 1/(e - 2); eq("q1", sf(x), 1.39); eq("q1 check", log(2*x + 1) - log(x), 1)
# Q2: (2-x)^-2 = 1/4 + x/4 + 3x^2/16
t = 0.01
eq("q2", (2 - t)**-2, 1/4 + t/4 + 3*t*t/16, 1e-6)
assert F(1, 4)*F(3, 4) == F(3, 16)
# Q3
assert 1 + 2 + 4 == 7
assert F(-(2*1 + 2), 1 + 2*2) == F(-4, 5)
def yb(x): return (-x + sqrt(x*x - 4*(x*x - 7)))/2
eq("q3", (yb(1 + 1e-6) - yb(1 - 1e-6))/2e-6, -0.8, 1e-6); eq("q3 pt", yb(1), 2)
# Q4
R = sqrt(3**2 + 4**2); al = degrees(atan(4/3))
eq("q4 R", R, 5); eq("q4 alpha", round(al, 1), 53.1)
eq("q4 asin", round(degrees(asin(0.4)), 2), 23.58); eq("q4 156", round(180 - degrees(asin(0.4)), 2), 156.42)
t1 = 180 - degrees(asin(0.4)) - al; t2 = 360 + degrees(asin(0.4)) - al
eq("q4 t1", round(t1, 1), 103.3); eq("q4 t2", round(t2, 1), 330.4)
eq("q4 383", round(360 + degrees(asin(0.4)), 2), 383.58)
for t in (t1, t2): eq("q4 eq", 3*sin(radians(t)) + 4*cos(radians(t)), 2, 1e-12)
# Q5
eq("q5", (2*e**3 + 1)/9, simpson(lambda x: x*x*log(x), 1, e), 1e-9)
eq("q5 alt", 2/9*e**3 + 1/9, (2*e**3 + 1)/9)
# Q6
k = 0.4
h = lambda t: (3 - k*t/2)**2
eq("q6 h0", h(0), 9); eq("q6 h5", h(5), 4); eq("q6 empty", h(15), 0)
eq("q6 k", 2/5, 0.4)
# Q7
eq("q7", 4 - 2*log(3), simpson(lambda x: 1/(1 + sqrt(x)), 0, 4, 200000), 1e-6)
# Q8
c = lambda z: z**3 - 3*z**2 + 4*z - 2
for r in (1 + 1j, 1 - 1j, 1): eq("q8 root", abs(c(r)), 0)
# (z^2 - 2z + 2)(z - 1) expanded: z^3 - z^2 - 2z^2 + 2z + 2z - 2
for z in (0.3, -2, 1 + 2j): eq("q8 factor", abs((z*z - 2*z + 2)*(z - 1) - c(z)), 0)
eq("q8 r", abs(1 + 1j), sqrt(2)); eq("q8 arg", atan(1), pi/4)
eq("q8c", abs((1 + 1j)**8 - 16), 0, 1e-9)
assert sum([1 + 1j, 1 - 1j, 1]) == 3
# Q9
l1 = lambda lam: (1 + 2*lam, 2 + lam, -1 + 3*lam)
l2 = lambda mu: (2 + mu, 4 - mu, 1 + mu)
assert l1(1) == l2(1) == (3, 3, 2)
d1, d2 = (2, 1, 3), (1, -1, 1)
dot = sum(a*b for a, b in zip(d1, d2)); assert dot == 4
eq("q9", round(degrees(acos(4/sqrt(14*3))), 1), 51.9)
# no other lambda,mu pair works
assert not any(l1(lam) == l2(mu) for lam in range(-5, 6) for mu in range(-5, 6) if (lam, mu) != (1, 1))
# Q10
f = lambda x: (7*x + 4)/((x + 2)*(1 - 2*x))
pf = lambda x: -2/(x + 2) + 3/(1 - 2*x)
for x in (0, 0.1, -0.3, 0.2): eq("q10a", f(x), pf(x), 1e-12)
assert 7*(-2) + 4 == -10 and 7*0.5 + 4 == 7.5 and F(15, 2)/F(5, 2) == 3
for x in (0.001, -0.001):
    eq("q10b", f(x), 2 + 13/2*x + 47/4*x*x, 1e-6)
assert F(-1, 4) + 12 == F(47, 4)
eq("q10c", 15/2*log(2) - 4*log(3), simpson(f, 0, 0.25), 1e-9)
Fq = lambda x: -2*log(x + 2) - 1.5*log(1 - 2*x)
eq("q10 F(1/4)", Fq(.25), -4*log(3) + 5.5*log(2)); eq("q10 F0", Fq(0), -2*log(2))
# Q11
g = lambda x: 2*atan(x) - x
eq("q11a y", 2*atan(1) - 1, pi/2 - 1); eq("q11a dy", 2/(1 + 1) - 1, 0)
eq("q11b g2", round(g(2), 3), 0.214); eq("q11b g3", round(g(3), 3), -0.502)
xs = [2.3]
for _ in range(5): xs.append(2*atan(xs[-1]))
for i, want in zip(range(1, 6), (2.3213, 2.3281, 2.3302, 2.3308, 2.3310)):
    eq(f"q11c x{i+1}", round(xs[i], 4), want)
root = 2.3311; assert abs(g(root)) < 1e-4; eq("q11c sf", sf(root), 2.33)
eq("q11d", 3*pi/4, simpson(lambda x: 6/(4 + x*x), 0, 2))
print("ok")
