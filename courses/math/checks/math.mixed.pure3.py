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
def deriv(f, x, h=1e-6): return (f(x + h) - f(x - h))/(2*h)

count_marks("chapters/math.mixed.pure3.md", 105, 29)
# 1
eq("q1", 2*log(6, 3) - log(4, 3), 2)
# 2
f2 = lambda x: exp(3*x) + log(2*x); 
for x in (0.5, 1.7): eq("q2", deriv(f2, x), 3*exp(3*x) + 1/x, 1e-4)
# 3
F3 = lambda x: .5*exp(2*x) + log(3*x + 1)/3
for x in (0.4, 2.0): eq("q3", deriv(F3, x), exp(2*x) + 1/(3*x + 1), 1e-6)
# 4
for x in (3, -2): assert abs(2*x - 1) == 5
# 5
eq("q5 mod", sqrt(9 + 16), 5); eq("q5 arg", round(atan(4/3), 3), 0.927)
# 6
assert 4 + 9 + 36 == 49
# 7
eq("q7", sin(radians(75)), (sqrt(6) + sqrt(2))/4)
# 8
g8 = lambda x: x**3 + x - 3; assert g8(1) == -1 and g8(2) == 7
# 9
assert 27 - 18 + 3*(-1) + 6 == 12 and 15 + 3*(-1) == 12
# 10
for x in (2, 3, -2): eq("q10", 5/((x - 1)*(x + 4)), 1/(x - 1) - 1/(x + 4), 1e-12)
# 11
for x in (0.001, -0.002): eq("q11", (1 + 2*x)**-0.5, 1 - x + 1.5*x*x, 1e-7)
assert F(3, 8)*4 == F(3, 2)
# 12
y12 = lambda x: x*x*exp(-x)
for x in (0, 2): eq("q12", deriv(y12, x), 0, 1e-5)
# 13
y13 = lambda x: (x*x + 1)/(x - 2)
eq("q13", deriv(y13, 3), -4, 1e-5)
# 14
for th in (90, 194.5, 345.5):
    eq("q14", 2*cos(radians(2*th)) + 3*sin(radians(th)), 1, 0.02)
s = asin(0.25); eq("q14 a", round(180 + degrees(s), 1), 194.5); eq("q14 b", round(360 - degrees(s), 1), 345.5)
eq("q14 90", 2*cos(radians(180)) + 3, 1)
# 15
eq("q15", pi/4, simpson(lambda x: sin(x)**2, 0, pi/2))
# 16
x = log(5)/(2*log(3) - log(5)); eq("q16", sf(x), 2.74); eq("q16 chk", 5**(x + 1), 3**(2*x), 1e-9)
# 17
eq("q17 b", (2.8 - 1.2)/2, 0.8); eq("q17 A", sf(exp(1.2)), 3.32)
# 18
z = (2 + 3j)/(1 - 1j); eq("q18 re", z.real, -0.5); eq("q18 im", z.imag, 2.5)
# 19
BA = (-2, 2, -1); BC = (-1, 4, 1)
dot = sum(a*b for a, b in zip(BA, BC)); assert dot == 9
eq("q19", degrees(acos(dot/(3*sqrt(18)))), 45)
assert tuple(a - b for a, b in zip((2, 1, -1), (4, -1, 0))) == BA and tuple(a - b for a, b in zip((3, 3, 1), (4, -1, 0))) == BC
# 20
for x in (0, 0.5, 1.3): eq("q20", deriv(lambda t: 3*exp(t*t), x), 2*x*3*exp(x*x), 1e-4)
# 21
xs = [1.5]
for _ in range(5): xs.append((7 - xs[-1])**(1/3))
for i, want in zip(range(1, 4), (1.7652, 1.7363, 1.7395)): eq(f"q21 x{i+1}", round(xs[i], 4), want)
eq("q21 x5", round(xs[4], 4), 1.7392); eq("q21", sf(xs[-1]), 1.74)
# 22
eq("q22", .5*log(2), simpson(lambda x: x/(x*x + 1), 0, 1))
# 23
eq("q23", (exp(2) + 1)/4, simpson(lambda x: x*exp(2*x), 0, 1))
# 24
eq("q24", 116/15, simpson(lambda x: x*sqrt(x + 1), 0, 3))
eq("q24 parts", (64/5 - 16/3) - (2/5 - 2/3), 116/15)
# 25
for z in (3 - 2j, -3 + 2j): eq("q25", abs(z*z - (5 - 12j)), 0)
assert (9 - 9) == 0 and (-4) * 1 == -4 and 9 * 4 == 36
# 26
th = lambda t: 20 + 80*exp(-log(2)/10*t)
eq("q26 t0", th(0), 100); eq("q26 t10", th(10), 60); eq("q26", th(20), 40)
# 27
t = 2; assert (t*t, t**3 - 3*t) == (4, 2)
m = F(3*t*t - 3, 2*t); assert m == F(9, 4)
eq("q27", 2 - 9/4*4, -7)
# 28
P = (1, 5, 2); d = (1, 2, -1)
tt = F(3, 2)
Fp = (tt, 1 + 2*tt, 2 - tt); assert Fp == (F(3, 2), 4, F(1, 2))
PF = tuple(a - b for a, b in zip(Fp, P)); assert sum(a*b for a, b in zip(PF, d)) == 0
eq("q28", sf(sqrt(float(sum(a*a for a in PF)))), 1.87); eq("q28 sq", float(sum(a*a for a in PF)), 3.5)
# 29
R = sqrt(25 + 144); al = degrees(atan(12/5))
eq("q29 R", R, 13); eq("q29 a", round(al, 1), 67.4)
vals = [1/(14 + 5*cos(radians(t/10)) - 12*sin(radians(t/10))) for t in range(0, 3600)]
eq("q29 max", max(vals), 1, 1e-4); eq("q29 min", min(vals), 1/27, 1e-6)
for t in (10, 100, 250): eq("q29 form", 5*cos(radians(t)) - 12*sin(radians(t)), 13*cos(radians(t + al)), 1e-9)
print("ok")
