# checks/math.fm.circular.py: recomputes every number in Circular motion: horizontal circles.
# Standard library only. Force balances are also confirmed by solving the equations directly.
from math import isclose, sqrt, sin, cos, tan, atan, acos, pi, radians, degrees, hypot

G = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def rpm(w):
    return w * 60 / (2 * pi)


def solve2(a, b, c, d, e, f):
    """Solve a x + b y = e, c x + d y = f."""
    det = a * d - b * c
    return (e * d - b * f) / det, (a * f - e * c) / det


# Warm-up
eq("w1", 5 * 0.8, 4); eq("w2", 0.4 * 2 * G, 8); eq("w3", 20 * 0.15 / 0.5, 6)

# Angular speed
w = 45 * 2 * pi / 60
eq("w 45rpm", w, 3 * pi / 2); eq("w 3sf", sf(w), 4.71)
eq("v 0.4", sf(0.4 * w), 1.88)
eq("rpm 12", sf(rpm(12), 4), 114.6)

# Proof: finite differences of r(cos wt, sin wt)
r, om, t, h = 0.7, 3.1, 0.37, 1e-4
pos = lambda t: (r * cos(om * t), r * sin(om * t))
acc = tuple((pos(t + h)[i] - 2 * pos(t)[i] + pos(t - h)[i]) / h ** 2 for i in range(2))
eq("proof ax", acc[0], -om ** 2 * pos(t)[0], 1e-4); eq("proof ay", acc[1], -om ** 2 * pos(t)[1], 1e-4)
vel = tuple((pos(t + h)[i] - pos(t - h)[i]) / (2 * h) for i in range(2))
eq("proof speed", hypot(*vel), r * om, 1e-6)
eq("proof perpendicular", vel[0] * pos(t)[0] + vel[1] * pos(t)[1], 0, 1e-6)

# smooth table
eq("T table", 0.4 * 9 / 0.5, 7.2); eq("w table", 3 / 0.5, 6); eq("T check", 0.4 * 0.5 * 36, 7.2)
# fairground
w = 2 * pi / 5
eq("fair w", sf(w, 4), 1.257); eq("fair v", sf(6 * w), 7.54); eq("fair a", sf(6 * w * w), 9.47)
eq("fair g", sf(6 * w * w / G), 0.947)

# disc
w2 = 0.6 * G / 0.12
eq("disc w2", w2, 50); eq("disc w", sf(sqrt(w2)), 7.07); eq("disc rpm", sf(rpm(sqrt(w2))), 67.5)

# conical pendulum, l 1.25, w 4
l, om, m = 1.25, 4, 0.4
c = G / (l * om ** 2); eq("cos", c, 0.5); th = acos(c); eq("theta", degrees(th), 60, 1e-9)
T = m * l * om ** 2; eq("T", T, 8); eq("T cos", T * c, 4)
rr = l * sin(th); eq("r", sf(rr, 5), 1.0825); eq("v", sf(rr * om), 4.33)
# l 0.8, 30 deg
th = radians(30); m = 0.5; rr = 0.8 * sin(th); eq("r30", rr, 0.4)
T = m * G / cos(th); eq("T30", sf(T, 4), 5.774)
v2 = T * sin(th) * rr / m; eq("v2", sf(v2, 4), 2.309); eq("v30", sf(sqrt(v2)), 1.52)
eq("1.25", m / rr, 1.25); eq("2.887", sf(T * sin(th), 4), 2.887)
eq("tan form", rr * G * tan(th), v2); eq("check tan", v2 / (rr * G), tan(th))
# elastic conical pendulum, l 0.5 lam 25 m 0.5 theta 60
m, l, lam, th = 0.5, 0.5, 25, radians(60)
T = m * G / cos(th); eq("T el", T, 10)
x = T * l / lam; eq("x el", x, 0.2); L = l + x; eq("L el", L, 0.7)
rr = L * sin(th); eq("r el", sf(rr, 4), 0.6062)
w2 = T * sin(th) / (m * rr); eq("w2 el", sf(w2, 4), 28.57); eq("w el", sf(sqrt(w2)), 5.35)
eq("v el", sf(rr * sqrt(w2)), 3.24); eq("8.660", sf(T * sin(th), 4), 8.660)

# Exam: elastic conical pendulum m 0.4 l 0.6 lam 24 w 5
m, l, lam, om = 0.4, 0.6, 24, 5
# T = m L w^2 = 10 L ; T = lam (L - l)/l = 40 (L - 0.6)
eq("10", m * om ** 2, 10); eq("40", lam / l, 40); eq("24", 40 * 0.6, 24)
L = 24 / 30; eq("L", L, 0.8)
T = 10 * L; eq("T", T, 8)
c = m * G / T; eq("cos", c, 0.5); th = acos(c); eq("theta", degrees(th), 60)
rr = L * sin(th); eq("r", sf(rr, 4), 0.6928); eq("v", sf(rr * om), 3.46)

# Cone, semi-vertical 30, m 0.3, h 0.45
m, a, h = 0.3, radians(30), 0.45
R = m * G / sin(a); eq("R cone", R, 6)
rr = h * tan(a); eq("r cone", sf(rr, 4), 0.2598)
eq("5.196", sf(R * cos(a), 4), 5.196)
v2 = R * cos(a) * rr / m; eq("v2 cone", v2, 4.5); eq("v cone", sf(sqrt(v2)), 2.12); eq("gh", G * h, 4.5)
eq("quiz gh 45", sf(sqrt(G * 0.8)), 2.83)

# Banked: no friction
eq("bank tan", 625 / (250 * G), 0.25); eq("bank deg", sf(degrees(atan(0.25)), 3), 14.0)
# Cyclist: tan 3/4, mu 0.5, r 20
sn, cs, mu, r = 0.6, 0.8, 0.5, 20
eq("(a) v2", r * G * 0.75, 150); eq("(a) v", sf(sqrt(150)), 12.2)
# greatest: friction down slope.  R cs - mu R sn = mg ; R sn + mu R cs = m v^2 / r  (m = 1)
Rg = G / (cs - mu * sn); eq("R max", Rg, 20)  # 2 mg with m = 1
v2 = r * Rg * (sn + mu * cs) / 1; eq("v2 max", v2, 400); eq("v max", sqrt(v2), 20)
eq("0.5R", cs - mu * sn, 0.5); eq("0.3", mu * sn, 0.3); eq("0.4", mu * cs, 0.4); eq("0.6+0.4", sn + mu * cs, 1.0)
Rl = G / (cs + mu * sn); eq("R min", Rl, G / 1.1)
v2 = r * Rl * (sn - mu * cs); eq("v2 min", sf(v2, 4), 36.36); eq("v min", sf(sqrt(v2)), 6.03)
eq("0.2", sn - mu * cs, 0.2)
# general formulas
t = 0.75
eq("formula max", r * G * (t + mu) / (1 - mu * t), 400); eq("formula min", r * G * (t - mu) / (1 + mu * t), v2, 1e-9)
# verify by solving the two linear equations numerically
R_, F_ = solve2(cs, -sn, sn, cs, G, 400 / r)  # R cs - F sn = g ; R sn + F cos = v^2/r
eq("solve F/R", F_ / R_, mu, 1e-9)
R_, F_ = solve2(cs, sn, sn, -cs, G, v2 / r)
eq("solve F/R min", F_ / R_, mu, 1e-9)

# Two strings, A 0.3 above, B 0.3 below, strings 0.5, m 0.6
m, L, d = 0.6, 0.5, 0.3
rr = sqrt(L ** 2 - d ** 2); eq("r rod", rr, 0.4)
ca, sa = d / L, rr / L; eq("cos a", ca, 0.6); eq("sin a", sa, 0.8)
om = 10
TA, TB = solve2(ca, -ca, sa, sa, m * G, m * rr * om ** 2)
eq("TA", TA, 20); eq("TB", TB, 10)
eq("dif", m * G / ca / 1 * 0 + (TA - TB), 10); eq("sum", TA + TB, 30)
eq("w crit2", (0.8 * 10) / (m * rr), 33.333333333333336, 1e-6); eq("w crit", sf(sqrt(8 / (m * rr))), 5.77)

# Spot the error
m = 0.5
eq("spot T", sf(m * G / cos(radians(30)), 4), 5.774)
eq("spot 0.625", m / 0.8, 0.625)
eq("spot v2 wrong", sf(2.887 / 0.625, 4), 4.619); eq("spot v wrong", sf(sqrt(2.887 / 0.625)), 2.15)
eq("spot v2", sf(0.5 * G / cos(radians(30)) * 0.5 / 1.25, 4), 2.309); eq("spot v", sf(sqrt(2.309)), 1.52); eq("spot tan", 2.309 / 4, tan(radians(30)), 1e-3)

# Try
eq("t1 v", 0.5 * 8, 4); eq("t1 a", 0.5 * 64, 32)
eq("t2 w", sf(300 * 2 * pi / 60), 31.4); eq("t2 T", 2 * pi / (10 * pi), 0.2)
eq("t3", 1000 * 100 / 50, 2000)
eq("t4", sf(0.2 * 0.4 * pi ** 2), 0.790)
eq("t5", 0.5 * G / 0.2, 25)
eq("t6", sf(degrees(acos(G / 25))), 66.4)
eq("t7", sf(sqrt(100 * G * 0.2)), 14.1)
eq("t9 T", 3 / cos(radians(60)), 6); eq("t9 w2", 6 / (0.3 * 0.5), 40); assert 40 > G / 0.5

# Exam practice
eq("p1", 0.8 * 6, 4.8); eq("p1 a", 0.8 * 36, 28.8)
eq("p2 T", 0.3 * 16 / 0.6, 8); eq("p2 T period", sf(2 * pi / (4 / 0.6)), 0.942)
w2 = 4 / 0.15; eq("p3 w2", sf(w2, 4), 26.67); eq("p3 w", sf(sqrt(w2)), 5.16); eq("p3 rpm", sf(rpm(sqrt(w2))), 49.3)
T = 0.2 * 1.0 * 36; eq("p4 T", T, 7.2); c = 2 / T; eq("p4 cos", sf(c, 4), 0.2778); eq("p4 th", sf(degrees(acos(c))), 73.9)
eq("p5 tan", 400 / (80 * G), 0.5); eq("p5 deg", sf(degrees(atan(0.5))), 26.6)
eq("p6 T", 10 * 0.2 / 0.4, 5); eq("p6 v2", 5 * 0.6 / 0.5, 6); eq("p6 v", sf(sqrt(6)), 2.45)
T2 = 10 * 0.5 / 0.4; eq("p6 T2", T2, 12.5); v22 = T2 * 0.9 / 0.5; eq("p6 v2b", v22, 22.5); eq("p6 vb", sf(sqrt(v22)), 4.74)
E1 = 0.5 * 0.5 * 6 + 10 * 0.2 ** 2 / 0.8; E2 = 0.5 * 0.5 * v22 + 10 * 0.5 ** 2 / 0.8
eq("p6 E1", E1, 2); eq("p6 E2", E2, 8.75); eq("p6 dE", E2 - E1, 6.75)
eq("p6 KE1", 0.25 * 6, 1.5); eq("p6 KE2", 0.25 * v22, 5.625); eq("p6 EPE1", 10 * 0.04 / 0.8, 0.5); eq("p6 EPE2", 10 * 0.25 / 0.8, 3.125)
eq("p7 triple", 0.6 ** 2 + 0.8 ** 2, 1.0); TA = 0.5 * G / 0.8; eq("p7 TA", TA, 6.25)
eq("p7 3.75", TA * 0.6, 3.75); eq("p7 7.5", 0.5 * 0.6 * 25, 7.5); eq("p7 TB", 7.5 - 3.75, 3.75)
w2 = 3.75 / (0.5 * 0.6); eq("p7 w2", w2, 12.5); eq("p7 w", sf(sqrt(w2)), 3.54)

# Stretch
Tn = 0.9 * G; eq("s1 T", Tn, 9)
eq("s1 w2a", Tn / (0.3 * 0.4), 75); eq("s1 wa", sf(sqrt(75)), 8.66)
eq("s1 w2b", Tn / (0.3 * 0.25), 120); eq("s1 wb", sf(sqrt(120)), 11.0)
# bowl: cos a = g/(a w^2), a 0.8, alpha 45
w2 = G / (0.8 * cos(radians(45))); eq("s2 w2", sf(w2, 4), 17.68); eq("s2 w", sf(sqrt(w2)), 4.20)
rr = 0.8 * sin(radians(45)); eq("s2 r", sf(rr, 4), 0.5657); eq("s2 v", sf(rr * sqrt(w2)), 2.38)

# Quiz
eq("q2", 6 / 2, 3); eq("q3", sqrt(2) ** 2, 2)

# Mark totals (also counted by the kit)
assert 4 + 2 + 2 == 8       # elastic conical pendulum example
assert 2 + 6 + 3 == 11      # cyclist example
print("ok")
