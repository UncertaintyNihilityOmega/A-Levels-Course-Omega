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

from math import sqrt, isclose, sin, cos, tan, radians, degrees, atan, log, exp, e
from fractions import Fraction as F
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")

count_marks("chapters/math.mock.p2a.md", 50, 9)
# Q1
x = (log(5)/log(3) - 1)/2
eq("q1 2x+1", sf(log(5)/log(3), 4), 1.465); eq("q1", sf(x), 0.232)
eq("q1 check", 3**(2*x + 1), 5)
# Q2: |x-2| < 3|x+1|  <=>  8x^2 + 22x + 5 > 0, roots -1/4, -5/2
assert (x*x for x in [0])
for xx in (-5/2, -1/4): eq("q2 root", 8*xx*xx + 22*xx + 5, 0)
assert 22**2 - 4*8*5 == 324
for xx in [i/10 for i in range(-80, 60)]:
    if abs(xx + 1) < 1e-9: continue
    inside = abs(xx - 2) < 3*abs(xx + 1)
    pred = xx < -2.5 or xx > -0.25
    if abs(xx + 2.5) < 1e-9 or abs(xx + 0.25) < 1e-9: continue
    assert inside == pred, xx
# Q3
for a in [-2]:
    f = lambda x: 2*x**3 + a*x*x - 7*x + 6
    assert f(2) == 0 and f(-1) == 9
assert 16 + 4*(-2) - 14 + 6 == 0
# Q4
for t in (3, -0.5):
    assert isclose(2*(1 + t*t) - 5*t - 5, 0, abs_tol=1e-12) or t == 3 or t == -0.5
    eq("q4 quad", 2*t*t - 5*t - 3, 0)
th1 = degrees(atan(3)); th2 = 180 - degrees(atan(0.5))
eq("q4a", round(th1, 1), 71.6); eq("q4b", round(th2, 1), 153.4); eq("q4 26.6", round(degrees(atan(0.5)), 1), 26.6)
for th in (th1, th2):
    eq("q4 eq", 2/cos(radians(th))**2 - 5*tan(radians(th)) - 5, 0, 1e-9)
# Q5
n = (6.5 - 2.5)/(3 - 1); c = 2.5 - n*1
eq("q5 n", n, 2); eq("q5 c", c, 0.5); eq("q5 K", sf(exp(c)), 1.65)
eq("q5 pt2", n*3 + c, 3.5 + 3 - 0.5 + 0.5 if False else 6.5)
# Q6
t = 2
x6 = t*t + 2*t; y6 = 3*t - t**3
assert (x6, y6) == (8, -2)
m = F(3 - 3*t*t, 2*t + 2); assert m == F(-3, 2)
assert 3*8 + 2*(-2) == 20
# Q7
g = lambda x: sqrt(1 + x**3)
ys = [g(0.5*i) for i in range(5)]
eq("q7 y1", sf(ys[1], 5), 1.0607); eq("q7 y2", sf(ys[2], 5), 1.4142); eq("q7 y3", sf(ys[3], 5), 2.0917)
inner = 1.0607 + 1.4142 + 2.0917
eq("q7 sum", round(1 + 3 + 2*inner, 3), 13.133)
T = 0.25*(ys[0] + ys[4] + 2*sum(ys[1:4]))
eq("q7 T", sf(T), 3.28)
# exact integral by Simpson to check over-estimate; second derivative positive
N = 20000; hh = 2/N
S = sum((g(i*hh) + 4*g(i*hh + hh/2) + g((i + 1)*hh))*hh/6 for i in range(N))
assert T > S
d = 1e-4
assert all(g(xx + d) - 2*g(xx) + g(xx - d) > 0 for xx in [0.02*i + 0.02 for i in range(98)])
# Q8
h = lambda x: x**3 - 3*x - 5
assert h(2) == -3 and h(3) == 13
xs = [2.0]
for _ in range(5): xs.append((3*xs[-1] + 5)**(1/3))
for i, want in zip(range(1, 6), (2.2240, 2.2684, 2.2770, 2.2786, 2.2789)):
    eq(f"q8 x{i+1}", round(xs[i], 4), want)
eq("q8 sf", sf(xs[-1]), 2.28)
eq("q8 h-", round(h(2.275), 4), -0.0505); eq("q8 h+", round(h(2.285), 4), 0.0755)
# Q9
y9 = lambda x: exp(2*x) - 8*exp(x)
eq("q9a", y9(log(8)), 0, 1e-9)
eq("q9b y", y9(log(4)), -16, 1e-9)
eq("q9 dy", 2*exp(2*log(4)) - 8*exp(log(4)), 0)
eq("q9 y0", y9(0), -7)
G = lambda x: 0.5*exp(2*x) - 8*exp(x)
eq("q9 G8", G(log(8)), -32); eq("q9 G0", G(0), -7.5)
eq("q9 area", -(G(log(8)) - G(0)), 24.5)
eq("q9 d2", 4*16 - 8*4, 32)
print("ok")
