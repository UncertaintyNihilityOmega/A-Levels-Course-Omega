# checks/math.m.newton.py: recomputes every number in the Newton's laws chapter.
from math import isclose, sqrt, sin, cos, radians

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

g = 10
# block pulled
eq("a1", (20 - 8) / 4, 3); eq("v1", 3 * 5, 15)
# lift
eq("R", 70 * (g + 1.5), 805); eq("700+105", 700 + 105, 805)
eq("T", 480 * 10.5, 5040); eq("T form", 4800 + 480 * 0.5, 5040); eq("R2", 80 * 10.5, 840)
# smooth slope
eq("a slope", 2 * 10 * sin(radians(30)) / 2, 5); eq("v2", 2 * 5 * 4, 40); eq("v", sf(sqrt(40)), 6.32)
# rough slope 3-4-5
eq("R", 5 * 10 * 0.8, 40); eq("F", 0.5 * 40, 20); eq("W//", 5 * 10 * 0.6, 30)
eq("a down", (30 - 20) / 5, 2); eq("a up", (30 + 20) / 5, 10); eq("s", 64 / 20, 3.2)
# pulled block
eq("R pull", 40 - 20 * 0.6, 28); eq("F pull", 0.3 * 28, 8.4); eq("a pull", (16 - 8.4) / 4, 1.9)
# 5 kg 3 kg
a = (50 - 30) / 8; eq("a", a, 2.5); eq("T", 30 + 3 * a, 37.5); eq("chk", 50 - 37.5, 5 * a)
# table
a = (20 - 10) / 6; eq("a tab", sf(a), 1.67); eq("T tab", sf(20 - 2 * a), 16.7); eq("T exact", 50 / 3, 20 - 2 * a)
# landing
eq("v land", sf(sqrt(2 * 2.5 * 2)), 3.16); eq("v2", 2 * 2.5 * 2, 10); eq("s up", 10 / 20, 0.5); eq("rise", 2 + 0.5, 2.5)
# exam 1
a = (25 - 20) / 6.5; eq("a ex", sf(a), 0.769); eq("a frac", 10 / 13, a); eq("T ex", sf(20 + 4 * a), 23.1)
v2 = 2 * a * 1.2; eq("v2", sf(v2, 4), 1.846); eq("v", sf(sqrt(v2)), 1.36); eq("s", sf(v2 / 10, 3), 0.185)
eq("W//", 4 * 10 * sin(radians(30)), 20)
# car trailer
a = (2200 - 400) / 1200; eq("a car", a, 1.5); eq("T", 150 + 400 * a, 750); eq("chk", 2200 - 250 - 750, 800 * a)
# try
eq("t1", 3000 / 1200, 2.5); eq("t2a", (30 - 10) / 5, 4); eq("t2v", 24, 4 * 6); eq("t3", 600 - 120, 480)
R = 40 * cos(radians(30)); eq("t4 R", sf(R, 4), 34.64); eq("t4 F", sf(0.2 * R, 3), 6.93); eq("t4 a", sf((20 - 0.2 * R) / 4), 3.27)
a = (60 - 40) / 10; eq("t5 a", a, 2); eq("t5 T", 40 + 4 * a, 48)
a = 30 / 8; eq("t6 a", a, 3.75); eq("t6 T", 5 * a, 18.75)
a = (3000 - 800) / 1200; eq("t7 a", sf(a), 1.83); eq("t7 T", 200 + 300 * a, 750)
a = (60 - 20) / 8; eq("t9 a", a, 5); eq("t9 T", 20 + 2 * a, 30); eq("t9 v2", 2 * 5 * 1.6, 16); eq("t9 s", 16 / 20, 0.8); eq("t9 h", 1.6 + 0.8, 2.4)
T = 12 / 0.98; eq("t10 T", sf(T), 12.2); eq("t10 eq", 0.8 * T, 0.3 * (40 - 0.6 * T), 1e-9); eq("t10 coef", 0.8 + 0.18, 0.98)
# quiz
eq("q1", 50 + 5 * 2, 60); eq("q2", g * sin(radians(30)), 5)
a = (30 - 20) / 5; eq("q3 T", 2 * (10 + a), 24)
# ---- v2 additions ----
from math import asin
th = radians
# warm-up
eq("w1", (20 ** 2 - 8 ** 2) / (2 * 84), 2); eq("w2 down", 60 * sin(th(30)), 30); eq("w2 R", sf(60 * cos(th(30))), 52.0)
eq("w3 a", 28 / 7, 4); eq("w3 T", 12 + 3 * 4, 24); eq("w3 chk", 40 - 24, 4 * 4)
# proof formula
m1, m2 = 5, 3; eq("pr a", (m1 - m2) * 10 / (m1 + m2), 2.5); eq("pr T", 2 * m1 * m2 * 10 / (m1 + m2), 37.5)
for m1, m2 in ((7, 2), (4, 1.5), (3, 3)):
    a = (m1 - m2) * 10 / (m1 + m2); T = m2 * (10 + a); eq("pr sym", T, m1 * (10 - a))
# widget example
R = 40 * cos(th(30)); Fm = 0.25 * R; eq("wg Fm", round(Fm, 2), 8.66); eq("wg net", 3 * 10 - 4 * 10 * sin(th(30)), 10); assert 10 > Fm
# spot the error
R = 50 * cos(th(30)); eq("se R", round(R, 2), 43.30); F = 0.2 * R; eq("se F", round(F, 3), 8.660)
a = (50 * sin(th(30)) - F) / 5; eq("se a", sf(a), 3.27); eq("se top", round(50 * sin(th(30)) - F, 2), 16.34)
eq("se wrong", (25 - 10) / 5, 3); eq("se smooth", 10 * sin(th(30)), 5)
# exam practice
eq("q1", 600 - 60 * 1.2, 528)
eq("q2 F", 0.3 * 80, 24); eq("q2 a", (40 - 24) / 8, 2); eq("q2 s", 0.5 * 2 * 9, 9)
a = 10 * sin(th(25)); eq("q3 a", round(a, 3), 4.226); eq("q3 v", sf(3 * a), 12.7)
a = (60 - 20) / 8; eq("q4 a", a, 5); eq("q4 T", 20 + 2 * a, 30); eq("q4 chk", 60 - 30, 6 * a); eq("q4 v2", 2 * 5 * 1.5, 15); eq("q4 v", sf(sqrt(15)), 3.87)
F = 0.4 * 50; eq("q5 F", F, 20); a = (30 - 20) / 8; eq("q5 a", a, 1.25); T = 20 + 5 * a; eq("q5 T", T, 26.25); eq("q5 chk", 30 - T, 3 * a)
R = 40 * cos(th(30)); eq("q6 R", round(R, 2), 34.64); F = 0.3 * R; eq("q6 F", round(F, 2), 10.39)
a = (50 - 40 * sin(th(30)) - F) / 4; eq("q6 a", sf(a), 4.90); eq("q6 top", round(50 - 20 - F, 2), 19.61)
a = (3000 - 400 - 200) / 1200; eq("q7 a", a, 2); T = 200 + 300 * a; eq("q7 T", T, 800); eq("q7 car", 3000 - 400 - T, 900 * a)
dec = 200 / 300; eq("q7 dec", dec, 2 / 3); eq("q7 s", 20 ** 2 / (2 * dec), 300)
a = 2 * 1.6 / 0.8 ** 2; eq("q8 a", a, 5); T = 4 * 10 - 4 * a; eq("q8 T", T, 20); m = T / (10 + a); eq("q8 m", round(m, 2), 1.33); eq("q8 m exact", m, 4 / 3)
eq("q8 chk", (4 - 4 / 3) * 10 / (4 + 4 / 3), 5); v = a * 0.8; eq("q8 v", v, 4); eq("q8 rise", v ** 2 / 20, 0.8); eq("q8 tot", 1.6 + v ** 2 / 20, 2.4)
# stretch
st, ct, mu = 0.6, 0.8, 0.5
eq("s1 R", ct * 10, 8); eq("s1 F", mu * 8, 4); eq("s1 up", 10 * st + mu * 10 * ct, 10); eq("s1 s", 64 / 20, 3.2)
assert 6 > 4; adn = 10 * st - mu * 10 * ct; eq("s1 down", adn, 2); eq("s1 v2", 2 * adn * 3.2, 12.8); eq("s1 v", sf(sqrt(12.8)), 3.58); assert sqrt(12.8) < 8
R = 30 * cos(th(30)); eq("s2 R", round(R, 2), 25.98); Fm = 0.5 * R; eq("s2 Fm", round(Fm, 2), 12.99); eq("s2 w", 30 * sin(th(30)), 15)
eq("s2 m1", sf((15 - Fm) / 10), 0.201); eq("s2 10m", round(15 - Fm, 2), 2.01); eq("s2 m2", sf((15 + Fm) / 10), 2.80); eq("s2 27.99", round(15 + Fm, 2), 27.99)

print("ok")
