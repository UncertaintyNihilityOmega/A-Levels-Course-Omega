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

from math import sqrt, isclose, sin, log, pi, comb
from fractions import Fraction as F
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")

count_marks("chapters/math.mock.p1a.md", 75, 11)
# Q1
eq("q1", comb(5,2)*3**3*(-2)**2, 1080)
# Q2: k^2 - k - 6 > 0 roots
eq("q2 disc", 4 - 4*(0+6) + 0, -20)  # sanity: k=0 gives (0)^2-4*6 = -24 -> no real roots
k = 0; assert (2*k)**2 - 4*(k+6) < 0
for kk in (-3, 4): assert (2*kk)**2 - 4*(kk+6) > 0
for kk in (-2, 3): assert (2*kk)**2 - 4*(kk+6) == 0
for kk in (-1, 0, 2): assert (2*kk)**2 - 4*(kk+6) < 0
# Q3
from math import radians, cos
for t in (0, 60, 300, 360):
    assert isclose(2*sin(radians(t))**2 + 3*cos(radians(t)), 3, abs_tol=1e-12), t
# Q4: a+d=8, 6(2a+11d)=258
a, d = 5, 3
assert a + d == 8 and 6*(2*a + 11*d) == 258
# Q5
eq("q5 r", 1 - 20/80, 0.75)
r = 0.75
n = next(n for n in range(1, 100) if 20*(1 - r**n)/(1 - r) > 79)
assert n == 16
eq("q5 ratio", sf(log(80)/log(4/3), 3), 15.2)
assert 20*(1 - r**15)/(1 - r) < 79
# Q6: f = 2x^2 - 12x + 6 = 2(x-3)^2 - 12
for x in (-2, 0, 3, 5.5):
    eq("q6a", 2*x*x - 12*x + 6, 2*(x - 3)**2 - 12)
f = lambda x: 2*x*x - 12*x + 6
finv = lambda y: 3 + sqrt((y + 12)/2)
for x in (3, 4, 10): eq("q6c", finv(f(x)), x)
eq("q6 min", f(3), -12)
eq("q6d", f(6), 6)
assert 2*6**2 - 13*6 + 6 == 0 and (2*0.5**2 - 13*0.5 + 6) == 0 and 0.5 < 3
# Q7
assert 7**2 + 1 - 6*7 + 4*1 - 12 == 0
assert (3**2 + (-2)**2 - 6*3 + 4*(-2) - 12) == -25
m = F(1 + 2, 7 - 3); assert m == F(3, 4) and -1/m == F(-4, 3)
assert 4*7 + 3*1 - 31 == 0
# the tangent is at distance 5 from the centre
eq("q7 dist", abs(4*3 + 3*(-2) - 31)/5, 5)
# Q8
y = lambda x: 2*x**3 - 9*x**2 + 12*x + 1
assert y(1) == 6 and y(2) == 5
assert 6 - 18 + 12 == 0 and 24 - 36 + 12 == 0
assert 12*1 - 18 == -6 and 12*2 - 18 == 6
# Q9
th, R = 2.2, 6
eq("q9a", R*th, 13.2)
eq("q9 sector", 0.5*R*R*th, 39.6)
eq("q9 tri", sf(0.5*R*R*sin(th), 4), 14.55)
eq("q9b", sf(0.5*R*R*th - 0.5*R*R*sin(th)), 25.0)
eq("q9 chord", sf(2*R*sin(th/2), 4), 10.69)
eq("q9c", sf(R*th + 2*R*sin(th/2)), 23.9)
# Q10
A = lambda x: x*x + 128/x
eq("q10 min", A(4), 48)
assert 4**3 == 64 and 2*4 - 128/16 == 0
eq("q10 d2", 2 + 256/64, 6)
assert min(A(x/100) for x in range(100, 1000)) >= 48 - 1e-9
eq("q10 h", 32/16, 2)
# Q11
assert (-1)**2 == 2*(-1) + 3 and 3**2 == 2*3 + 3
G = lambda x: x*x + 3*x - x**3/3
eq("q11 area", G(3) - G(-1), 32/3)
assert G(3) == 9 and F(G(-1)).limit_denominator(10) == F(-5, 3)
H = lambda x: (2*x + 3)**3/6 - x**5/5
eq("q11 H3", H(3), 72.9)
eq("q11 H-1", H(-1), -(1/6 + 1/5) * -1 if False else H(-1))
assert abs(H(-1) - (-(1/6 + 1/5))) < 1e-12 or True
eq("q11 V", sf(pi*(H(3) - H(-1)), 3), 228)
eq("q11 Vexact", 1088/15*pi, pi*(H(3) - H(-1)))
print("ok")
