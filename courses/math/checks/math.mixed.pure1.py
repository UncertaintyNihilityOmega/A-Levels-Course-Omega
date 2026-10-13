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

count_marks("chapters/math.mixed.pure1.md", 106, 29)
# 1
for x in (7, -2): assert x*x - 5*x - 14 == 0
# 2
assert 7 + 9*4 == 43
# 3
m = F(-3 - 5, 6 - 2); assert m == -2
assert all(-2*x + 9 == y for x, y in ((2, 5), (6, -3)))
# 4: numerical derivative
f4 = lambda x: 3*x**4 - 2/x**2 + 5*sqrt(x)
d4 = lambda x: 12*x**3 + 4*x**-3 + 2.5*x**-0.5
for x in (0.7, 2.3): eq("q4", (f4(x + 1e-6) - f4(x - 1e-6))/2e-6, d4(x), 1e-5)
# 5
F5 = lambda x: 2*x**3 + 4/x
for x in (1.3, 2.1): eq("q5", (F5(x + 1e-6) - F5(x - 1e-6))/2e-6, 6*x*x - 4/x**2, 1e-5)
# 6
eq("q6", radians(150), 5*pi/6)
# 7
th = atan(3/4); eq("q7 s", sin(th), 3/5); eq("q7 c", cos(th), 4/5)
# 8
for x in (-5, 0, 2.5): eq("q8", x*x + 6*x + 2, (x + 3)**2 - 7)
# 9
fq = lambda x: 2*x + 3; gq = lambda x: x*x
for x in (-3 + sqrt(6), -3 - sqrt(6)): eq("q9", fq(gq(x)), gq(fq(x)), 1e-9)
assert 36 - 12 == 24 and 4 - 2 == 2
# 10
from math import comb
assert (2**5, comb(5, 1)*2**4*3, comb(5, 2)*2**3*9) == (32, 240, 720)
# 11
a = degrees(atan(2)); eq("q11a", round(a, 1), 63.4)
x1, x2 = a + 20, a + 200
eq("q11b", round(x1, 1), 83.4); eq("q11c", round(x2, 1), 263.4)
for x in (x1, x2): eq("q11", tan(radians(x - 20)), 2, 1e-9)
# 12
assert 3**2 + 4**2 == 25
# 13
assert 2**3 - 4*2 == 0 and 3*4 - 4 == 8
assert F(-1, 8) == -1/F(8)
# 14
eq("q14", 3*36 - 6**3/3, 36); eq("q14 num", simpson(lambda x: 6*x - x*x, 0, 6), 36)
# 15
assert 16 - 4*5 < 0 and 16 - 4*3 > 0 and 16 - 4*4 == 0
# 16
eq("q16 arc", 5*0.8, 4); eq("q16 per", 10 + 4, 14); eq("q16 area", .5*25*.8, 10)
# 17: translation by (2,3) then reflection
t17 = lambda x: -(((x - 2)**2 - 4*(x - 2)) + 3)
for x in (-1, 0, 2, 5): eq("q17", t17(x), -x*x + 8*x - 15)
for x in (-1, 0, 3): eq("q17 mid", (x - 2)**2 - 4*(x - 2) + 3, x*x - 8*x + 15)
# 18
fi = lambda x: (x - 1)/(x + 2); fii = lambda x: (1 + 2*x)/(1 - x)
for x in (0, 3, 10, -5): eq("q18", fii(fi(x)), x, 1e-9)
# 19
eq("q19a", 3*(2**8 - 1), 765); eq("q19b", 12/(1 - 2/3), 36); eq("q19 r", 8/12, 2/3)
eq("q19 r2", (16/3)/8, 2/3)
# 20
assert F(8 - 2, 5 - 1) == F(3, 2)
assert 2*3 + 3*5 - 21 == 0 and (1 - 3)**2 + (2 - 5)**2 == (5 - 3)**2 + (8 - 5)**2
# 21
for th in (0.4, 1.0): eq("q21", tan(th) + 1/tan(th), 1/(sin(th)*cos(th)))
# 22
eq("q22", sf(2*pi*5*0.2), 6.28)
# 23
for x in (F(1, 4), 9): assert 2*x - 7*sqrt(x) + 3 == 0
# 24
for k in (1, -7): assert (3 + k)**2 - 16 == 0
# 25
y25 = lambda x: x + 4/x
assert y25(2) == 4 and y25(-2) == -4
# 26
eq("q26", 16 - 16/3 - (-16 + 16/3), 64/3); eq("q26 num", simpson(lambda x: 8 - 2*x*x, -2, 2), 64/3)
# 27
a, d = 5, 3; assert a + 4*d == 17 and sum(a + i*d for i in range(10)) == 185
# 28
r = 5; th = (20 - 2*r)/r
eq("q28", th, 2); eq("q28 A", .5*r*r*th, 25)
assert max(10*r_ - r_*r_ for r_ in [i/100 for i in range(1, 1000)]) <= 25 + 1e-9
# 29
s = asin(1/3); eq("q29 ref", round(degrees(s), 1), 19.5)
sols = [30, 150, 180 + degrees(s), 360 - degrees(s)]
for x in sols: eq("q29", 6*cos(radians(x))**2 + sin(radians(x)) - 5, 0, 1e-9)
eq("q29 a", round(sols[2], 1), 199.5); eq("q29 b", round(sols[3], 1), 340.5)
print("ok")
