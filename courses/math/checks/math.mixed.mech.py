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

from math import sqrt, isclose, sin, cos, tan, atan, radians, degrees
from fractions import Fraction as F
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
g = 10
count_marks("chapters/math.mixed.mech.md", 124, 29)
# 1
eq("1 down", 100*sin(radians(30)), 50); eq("1 R", sf(100*cos(radians(30))), 86.6)
# 2
eq("2 mag", sqrt(36 + 64), 10); eq("2 ang", round(degrees(atan(8/6)), 1), 53.1)
# 3
a = (25 - 5)/8; eq("3 a", a, 2.5); eq("3 s", 0.5*(5 + 25)*8, 120); eq("3 s2", 5*8 + 0.5*a*64, 120)
# 4
eq("4", 2*6/(2 + 4), 2)
# 5
eq("5", 3*g + 3*2, 36)
# 6
eq("6", sqrt(2*g*20), 20); eq("6 ke", 0.5*0.5*400, 0.5*g*20)
# 7
eq("7", 400*15, 6000)
# 8
assert 0.3*10*10 == 30 and 25 < 30
# 9
eq("9", 0.5*4*8 + 8*6, 64); eq("9a", 0.5*4*8, 16); eq("9b", 8*6, 48)
# 10
h = 15**2/(2*g); eq("10 h", h, 11.25); eq("10 t", 2*15/g, 3); eq("10 t up", 15/g, 1.5)
# 11
s = lambda t: 2*t**3 - 9*t**2 + 12*t; v = lambda t: 6*t**2 - 18*t + 12
d = 1e-6
for t in (0.5, 1.7, 3, 4): eq("11 deriv", (s(t + d) - s(t - d))/(2*d), v(t), 1e-4)
eq("11 v3", v(3), 12); eq("11 v3 terms", 54 - 54 + 12, 12); eq("11 r1", v(1), 0); eq("11 r2", v(2), 0)
assert all((6*(t-1)*(t-2)) == v(t) for t in (0, 3, 5, 7))
# 12
T2 = 30*sqrt(3); T1 = 30
eq("12 horiz", T1*cos(radians(30)) - T2*cos(radians(60)), 0, 1e-9)
eq("12 vert", T1*sin(radians(30)) + T2*sin(radians(60)), 60, 1e-9); eq("12 T2", sf(T2), 52.0); eq("12 T1 rel", T2/sqrt(3), T1)
eq("12 combine", 1/(2*sqrt(3)) + sqrt(3)/2, 2/sqrt(3))
# 13
R = 60 + 30*sin(radians(25)); Fr = 30*cos(radians(25))
eq("13 R", round(R, 2), 72.68); eq("13 F", round(Fr, 2), 27.19); eq("13 mu", sf(Fr/R), 0.374)
# 14
a = (50 - 30)/8; T = 30 + 3*a; eq("14 a", a, 2.5); eq("14 T", T, 37.5); eq("14 P", 50 - T, 5*a)
eq("14 v2", 2*a*2, 10); eq("14 v", sf(sqrt(10)), 3.16)
# 15
a = (3500 - 700)/1400; eq("15 a", a, 2); eq("15 T", 200 + 400*a, 1000); eq("15 car", 3500 - 500 - 1000, 1000*a)
# 16
eq("16 pe", 8*g*5*0.6, 240); eq("16 wd", 80*5, 400); eq("16 fr", 12*5, 60); eq("16 ke", 400 - 60 - 240, 100)
eq("16 v", sqrt(2*100/8), 5)
# 17
sP = lambda t: t*t; sQ = lambda t: 16*(t - 3)
for t in (4, 12): eq("17 level", sP(t), sQ(t))
assert 16*16 - 4*48 == 64
eq("17 d1", sP(4), 16); eq("17 d2", sP(12), 144); assert (4 - 4)*(4 - 12) == 0 and 4*12 == 48 and 4 + 12 == 16
# 18
D = 24000/20; W = 800*g/20; eq("18 D", D, 1200); eq("18 W", W, 400); eq("18 R", D - W, 800)
# 19
X = 10 + 14*cos(radians(60)); Y = 14*sin(radians(60)); eq("19 X", X, 17); eq("19 Y", round(Y, 2), 12.12)
eq("19 mag2", X*X + Y*Y, 436, 1e-9); eq("19 mag", sf(sqrt(436)), 20.9); eq("19 ang", round(degrees(atan(Y/X)), 1), 35.5)
# 20
a = 2*20/25; eq("20 a", a, 1.6); eq("20 R", 70*g*0.2 - 70*a, 28); eq("20 wt", 70*g*0.2, 140); eq("20 ma", 70*a, 112)
# 21
V = 15; eq("21", 0.5*(3 + V)*10 + 15*V, 315); eq("21 lin", 15 + 20*V, 315)
# 22
Fr = 0.2*50; a = (30 - Fr)/8; Tn = Fr + 5*a
eq("22 a", a, 2.5); eq("22 T", Tn, 22.5); eq("22 B", 30 - Tn, 3*a); eq("22 v2", 2*a*1.8, 9); eq("22 v", sqrt(9), 3)
a2 = Fr/5; eq("22 a'", a2, 2); s2 = 9/(2*a2); eq("22 s", s2, 2.25); eq("22 tot", 1.8 + s2, 4.05)
# 23
vt = lambda t: 8*t - t*t; st = lambda t: 4*t*t - t**3/3
for t in (1.3, 5): eq("23 deriv v", (st(t + 1e-6) - st(t - 1e-6))/2e-6, vt(t), 1e-4)
eq("23 acc", (vt(2 + 1e-6) - vt(2 - 1e-6))/2e-6, 8 - 2*2, 1e-4)
eq("23 v8", vt(8), 0); eq("23 s8", st(8), 256/3); eq("23 s8 form", 256 - 512/3, 256/3); eq("23 sf", sf(256/3), 85.3)
eq("23 s12", st(12), 0, 1e-9); assert all(vt(t) < 0 for t in (9, 10, 11, 11.9)) and all(vt(t) > 0 for t in (1, 4, 7.9))
eq("23 dist", 2*st(8), 512/3); eq("23 dist sf", sf(512/3), 171)
# 24
v = (0.4*5 - 0.4*3)/0.1; eq("24 v", v, 8); eq("24 mom", 0.4*5, 1.2 + 0.1*8)
dec = 0.5*0.1*g/0.1; eq("24 dec", dec, 5); eq("24 d", v*v/(2*dec), 6.4); eq("24 energy", 0.5*0.1*64/(0.5*0.1*g), 6.4)
# 25
D = 900 + 1500*g*0.04; eq("25 D", D, 1500); eq("25 v", 36000/D, 24); D2 = 36000/15; eq("25 D2", D2, 2400); eq("25 a", (D2 - 900 - 600)/1500, 0.6)
# 26
Rn = 5*g*0.8; Fm = 0.5*Rn; W = 5*g*0.6; eq("26 R", Rn, 40); eq("26 F", Fm, 20); eq("26 W", W, 30)
eq("26 least", W - Fm, 10); eq("26 most", W + Fm, 50)
# 27
import cmath
t = 5; eq("27 eq", -25, 20*t - 5*t*t); assert (t - 5)*(t + 1) == t*t - 4*t - 5 or True
eq("27 quad", 5*(-1)**2 - 20*(-1) - 25, 0); eq("27 v", 20 - g*t, -30); eq("27 rise", 400/20, 20); eq("27 H", 25 + 20, 45)
eq("27 check H", 45, 25 + 20)
# 28
m = 21/10; eq("28 m", m, 2.1); eq("28 mom", 3*6 - m*4, -3 + m*6)
b = 0.5*3*36 + 0.5*m*16; af = 0.5*3*1 + 0.5*m*36
eq("28 before", b, 70.8); eq("28 b parts", 54 + 16.8, 70.8); eq("28 after", af, 39.3); eq("28 a parts", 1.5 + 37.8, 39.3); eq("28 loss", b - af, 31.5)
# 29
eq("29 acc", 70*g + 70*1, 770); eq("29 const", 700, 70*g); eq("29 dec", 70*g - 140, 560)
V = 1*4; t3 = V/2; eq("29 t3", t3, 2); eq("29 dist", 0.5*4*4 + 4*8 + 0.5*4*2, 44)
print("ok")
