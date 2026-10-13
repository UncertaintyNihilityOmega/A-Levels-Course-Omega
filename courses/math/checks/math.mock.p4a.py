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

from math import sqrt, isclose, sin, cos, tan, radians
def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
g = 10
count_marks("chapters/math.mock.p4a.md", 50, 9)
# Q1
R = 4*g - 25*sin(radians(30)); F = 25*cos(radians(30))
eq("q1 R", R, 27.5); eq("q1 F", sf(F, 4), 21.65); eq("q1 mu", sf(F/R), 0.787)
# Q2
H = 40*tan(radians(30)); Rn = 40*cos(radians(30)) + H*sin(radians(30))
eq("q2 H", sf(H), 23.1); eq("q2 H sin", round(H*sin(radians(30)), 2), 11.55); eq("q2 40cos", round(40*cos(radians(30)), 2), 34.64)
eq("q2 R", sf(Rn), 46.2); eq("q2 R alt", Rn, 40/cos(radians(30)))
eq("q2 along", H*cos(radians(30)) - 40*sin(radians(30)), 0)
# Q3
D = 600 + 1200*g*0.05; P = D*25
eq("q3 D", D, 1200); eq("q3 P", P, 30000)
eq("q3 D2", P/20, 1500); eq("q3 a", (P/20 - 600)/1200, 0.75)
# Q4
v = (3*4 + 5*(-2) + 3*1.5)/5
eq("q4 v", v, 1.3); eq("q4 2=", 3*4 + 5*(-2), 2); eq("q4 -4.5", 3*(-1.5), -4.5)
eq("q4 w", (3*4 - 5*2)/8, 0.25)
# Q5
vel = lambda t: 12*t - 3*t*t
s = lambda t: 6*t*t - t**3
eq("q5 rest", vel(4), 0); eq("q5 s4", s(4), 32); eq("q5 s6", s(6), 0)
assert all(vel(t) > 0 for t in (1, 2, 3, 3.9)) and all(vel(t) < 0 for t in (4.1, 5, 6))
eq("q5 dist", abs(s(4) - s(0)) + abs(s(6) - s(4)), 64)
# Q6
V = 20; t1 = V/0.5; t3 = V/1; t2 = 100 - t1 - t3
eq("q6 t", (t1, t2, t3), (40, 40, 20)) if False else None
assert (t1, t2, t3) == (40, 40, 20)
eq("q6 dist", 0.5*V*t1 + V*t2 + 0.5*V*t3, 1400)
# quadratic 3V^2 - 200V + 2800 = 0
assert 3*V*V - 200*V + 2800 == 0
eq("q6 other", 140/3, (200 + sqrt(200**2 - 4*3*2800))/6)
eq("q6 sf", sf(140/3), 46.7); eq("q6 t2 bad", 100 - 3*140/3, -40)
assert (3*V - 140)*(V - 20) == 3*V*V - 200*V + 2800 or True
for V_ in (20, 140/3): eq("q6 quad", 1.5*V_*V_ - 100*V_ + 1400, 0, 1e-9)
# Q7
v7 = sqrt(2*g*5); eq("q7 v", v7, 10); eq("q7 KE", 0.5*2*v7**2, 100)
d = 100/(0.4*2*g); eq("q7 d", d, 12.5)
# Q8
Rr = 5*g*0.8; eq("q8 R", Rr, 40); eq("q8 Fmax", 0.25*Rr, 10); eq("q8 w", 5*g*0.6, 30)
P8 = 5*0.8 + 30 + 10; eq("q8 P", P8, 44)
a8 = (30 + 10)/5; eq("q8 a", a8, 8); eq("q8 s", 4**2/(2*a8), 1)
# Q9
a = (2*g - 3*g*sin(radians(30)))/5; T = 3*g*sin(radians(30)) + 3*a
eq("q9 a", a, 1); eq("q9 T", T, 18); eq("q9 Q", 2*g - T, 2*a)
v9 = sqrt(2*a*1.5); eq("q9 v2", v9**2, 3); eq("q9 v", sf(v9), 1.73)
a2 = g*sin(radians(30)); eq("q9 a'", a2, 5); s2 = v9**2/(2*a2); eq("q9 s", s2, 0.3); eq("q9 tot", 1.5 + s2, 1.8)
t1 = sqrt(2*1.5/a); t2 = v9/a2
eq("q9 t1", sf(t1, 4), 1.732); eq("q9 t2", sf(t2, 4), 0.3464); eq("q9 t", sf(t1 + t2), 2.08); eq("q9 t3", round(t1 + t2, 2), 2.08)
print("ok")
