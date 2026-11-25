# checks/math.fm.vertical.py: recomputes every number in Circular motion: vertical circles.
# Standard library only. Slack points and leaving points are also confirmed by integrating the motion (RK4).
from math import isclose, sqrt, cos, sin, acos, degrees, radians

G = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def v2s(u, r, th):          # string, rod, inside: theta from the downward vertical
    return u * u - 2 * G * r * (1 - cos(th))


def Tst(m, u, r, th):
    return m * (v2s(u, r, th) / r + G * cos(th))


def v2o(u, r, th):          # outside: theta from the top
    return u * u + 2 * G * r * (1 - cos(th))


def Rout(m, u, r, th):
    return m * (G * cos(th) - v2o(u, r, th) / r)


def integrate_slack(u, r, outside=False, dt=1e-5, tmax=30):
    """RK4 of theta'' = -+(g/r) sin theta until the contact force is zero; returns (theta, speed)."""
    s = 1 if outside else -1
    th, om, t = 0.0, u / r, 0.0
    f = lambda a, b: (b, s * (G / r) * sin(a))
    while t < tmax:
        k1 = f(th, om); k2 = f(th + dt * k1[0] / 2, om + dt * k1[1] / 2)
        k3 = f(th + dt * k2[0] / 2, om + dt * k2[1] / 2); k4 = f(th + dt * k3[0], om + dt * k3[1])
        th += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        om += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        t += dt
        radial = (G * cos(th) - r * om * om) if outside else (r * om * om + G * cos(th))
        if radial <= 0:
            return th, abs(r * om)
    return None


# Warm-up
eq("w1", 0.5 * 4 / 0.4, 5); eq("w2", sqrt(2 * G * 1.8), 6); eq("w3", 2 * G / cos(radians(60)), 40)

# string, r 0.8, m 0.5, u 7
r, m, u = 0.8, 0.5, 7
eq("a h", r * (1 - cos(radians(60))), 0.4)
eq("a v2", v2s(u, r, radians(60)), 41); eq("a v", sf(sqrt(41)), 6.40)
eq("a T", Tst(m, u, r, radians(60)), 28.125); eq("a T 3sf", sf(Tst(m, u, r, radians(60))), 28.1)
eq("b v2", v2s(u, r, radians(180)), 17); eq("b T", Tst(m, u, r, radians(180)), 5.625); eq("b v", sf(sqrt(17)), 4.12)
eq("b T direct", m * (17 / r - G), 5.625)
eq("bottom", Tst(m, u, r, 0), 35.625); eq("diff 6mg", Tst(m, u, r, 0) - Tst(m, u, r, radians(180)), 6 * m * G)
# least speed r 1.5
eq("min u2", 5 * G * 1.5, 75); eq("min u", sf(sqrt(75)), 8.66)
eq("min top", 75 - 4 * G * 1.5, 15); eq("min top v", sf(sqrt(15)), 3.87); eq("gr", G * 1.5, 15)
# slack, r 1.2, u 7
r, u = 1.2, 7
eq("5gr", 5 * G * r, 60); eq("2gr", 2 * G * r, 24)
c = (2 * G * r - u * u) / (3 * G * r); eq("cos", c, -25 / 36)
eq("theta", sf(degrees(acos(c)), 4), 134.0, 1e-9 + 0.05)
eq("theta 3sf", sf(degrees(acos(c))), 134.0)
v2 = -G * r * c; eq("v2", sf(v2, 4), 8.333); eq("v", sf(sqrt(v2)), 2.89)
eq("energy form", 49 - 2 * G * r * (1 - c), 25 + 24 * c, 1e-9); eq("25 + 24c", 25 + 24 * c, -12 * c, 1e-9)
th, v = integrate_slack(u, r)
eq("sim theta", th, acos(c), 1e-3); eq("sim v", v, sqrt(v2), 2e-3)
sinphi = sqrt(1 - c * c); eq("sinphi", sf(sinphi, 4), 0.7195)
vy = sqrt(v2) * sinphi; eq("vy", sf(vy, 4), 2.077); rise = vy * vy / (2 * G); eq("rise", sf(rise, 4), 0.2157, 1e-3)
eq("2.887", sf(sqrt(v2), 4), 2.887)
h0 = r * (1 - c); eq("h0", sf(h0, 4), 2.033); eq("hmax", sf(h0 + rise), 2.25); assert h0 + rise < 2 * r
# swing back: u 4, r 1
eq("swing cos", 1 - 16 / (2 * G * 1), 0.2); eq("swing deg", sf(degrees(acos(0.2))), 78.5); assert 16 < 20
# wire bead r 0.6, m 0.2, u 5
eq("wire 4gr", 4 * G * 0.6, 24); assert 25 > 24
eq("wire v2", 25 - 4 * G * 0.6, 1); eq("wire T", 0.2 * 1 / 0.6 - 0.2 * G, -1.6667, 1e-3); eq("wire T 3sf", sf(0.2 / 0.6 - 2), -1.67)
# inside sphere r 0.5, u 3
eq("in 2gr", 2 * G * 0.5, 10); eq("in h", 9 / (2 * G), 0.45); eq("in cos", 1 - 0.45 / 0.5, 0.1)

# Exam: cut-away sphere
r, m, u = 0.8, 0.3, 6
eq("A R", m * (u * u / r + G), 16.5)
eq("B height", r + 0.4, 1.2); v2B = u * u - 2 * G * 1.2; eq("B v2", v2B, 12)
cphi = 0.4 / r; eq("cos phi", cphi, 0.5)
RB = m * (v2B / r - G * cphi); eq("B R", RB, 3)
# general: R at angle theta from the bottom, B has cos theta = -0.5
eq("B R general", m * (u * u / r - 2 * G + 3 * G * (-cphi)), 3)
assert RB > 0
eq("vy2", v2B * sin(radians(60)) ** 2, 9); eq("rise", 9 / (2 * G), 0.45); eq("H", 1.2 + 0.45, 1.65)
# monotone R along the way
for i in range(0, 120):
    th = i * radians(1)
    if cos(th) >= -cphi:
        assert m * (u * u / r - 2 * G + 3 * G * cos(th)) >= RB - 1e-12

# Exam: string r 0.8 m 0.3 u 8
r, m, u = 0.8, 0.3, 8
eq("e1 T", m * (u * u / r + G), 27)
eq("e1 v2", v2s(u, r, radians(180)), 32); eq("e1 top", m * (32 / r - G), 9)
eq("e1 least", sf(sqrt(G * r + 4 * G * r)), 6.32); eq("e1 least u2", G * r + 4 * G * r, 40)
eq("e1 gr", G * r, 8); eq("e1 32", 4 * G * r, 32)

# Exam: hemisphere from rest, r 2
r, m = 2, 0.5
eq("h cos", 2 / 3, 2 / 3); eq("h v2", G * r * 2 / 3, 40 / 3, 1e-9); eq("h v", sf(sqrt(40 / 3)), 3.65)
eq("h ground", 2 * G * r, 40); eq("h ground v", sf(sqrt(40)), 6.32)
eq("h check R", Rout(m, 0, r, acos(2 / 3)), 0, 1e-9)
th, v = integrate_slack(1e-6, r, outside=True)
eq("sim out theta", th, acos(2 / 3), 2e-3); eq("sim out v", v, sqrt(40 / 3), 3e-3)
eq("deg", sf(degrees(acos(2 / 3)), 4), 48.19, 5e-3)
# outside example r 1.5 u 1.5
r, u = 1.5, 1.5
eq("o u2", u * u, 2.25); eq("o gr", G * r, 15)
c = (u * u + 2 * G * r) / (3 * G * r); eq("o cos", sf(c, 4), 0.7167); eq("o th", sf(degrees(acos(c))), 44.2)
eq("o v2", sf(G * r * c, 4), 10.75); eq("o v", sf(sqrt(G * r * c)), 3.28)
eq("o 32.25", u * u + 2 * G * r, 32.25); eq("o 45", 3 * G * r, 45)
th, v = integrate_slack(u, r, outside=True)
eq("o sim", th, acos(c), 2e-3)

# Spot the error
r, m, u = 0.5, 0.2, 6
eq("s wrong v2", u * u - 2 * G * r, 26); eq("s wrong T", m * (26 / r - G), 8.4)
eq("s v2", v2s(u, r, radians(180)), 16); eq("s T", Tst(m, u, r, radians(180)), 4.4); assert 36 >= 5 * G * r

# Try
eq("t1", sqrt(25 - 2 * G * 0.5), sqrt(15)); eq("t1 3sf", sf(sqrt(15)), 3.87)
eq("t2", 0.4 * (16 / 0.5 + G), 16.8)
eq("t3", sf(sqrt(5 * G * 0.9)), 6.71); eq("t4", sqrt(4 * G * 0.9), 6)
eq("t5 v2", 4.5 ** 2 - 2 * G * 0.4, 12.25); eq("t5 T", 0.2 * 12.25 / 0.4, 6.125)
eq("t6 2gr", 2 * G * 0.8, 16); eq("t6 cos", 1 - 12 / 16, 0.25)
eq("t7", 2 ** 2, 4); eq("t7 gr", G * 0.9, 9)
eq("t8", sf(sqrt(2 / 3 * G * 3)), 4.47); eq("t8 v2", 2 / 3 * G * 3, 20)
eq("t9", 50 - 5 * G * 1, 0)

# Exam practice
r, m, u = 0.6, 0.4, 5
eq("p1 5gr", 5 * G * r, 30); assert 25 < 30
r, m, u = 0.4, 0.5, 6
eq("p2 a", m * (u * u / r + G), 50); eq("p2 v2", u * u - 2 * G * r, 28); eq("p2 b", m * 28 / r, 35)
r, m = 0.9, 0.6
eq("p3 4gr", 4 * G * r, 36); eq("p3 u", sqrt(36), 6); eq("p3 v2", 6.5 ** 2 - 36, 6.25); eq("p3 u2", 6.5 ** 2, 42.25)
eq("p3 T", sf(m * 6.25 / r - m * G, 3), -1.83)
r, m, u2 = 0.9, 0.4, 27
eq("p4 c", (2 * G * r - u2) / (3 * G * r), -1 / 3); eq("p4 9+18c", u2 - 2 * G * r, 9)
eq("p4 v2", G * r / 3, 3); eq("p4 v", sf(sqrt(3)), 1.73); assert 2 * G * r < u2 < 5 * G * r
th, v = integrate_slack(sqrt(u2), r); eq("p4 sim", th, acos(-1 / 3), 1e-3); eq("p4 sim v", v, sqrt(3), 2e-3)
r, m = 0.6, 0.3
eq("p5 a", sf(sqrt(4 * G * r)), 4.90); eq("p5 4gr", 4 * G * r, 24); eq("p5 v2", 49 - 4 * G * r, 25); eq("p5 R", m * 25 / r - m * G, 9.5)
eq("p5 c", m * (49 / r + G), 27.5); eq("p5 c2", m * 49 / r + 3, 27.5)
r, m, u = 1.2, 0.5, 1
c = (u * u + 2 * G * r) / (3 * G * r); eq("p6 cos", c, 25 / 36)
eq("p6 v2", G * r * c, 25 / 3, 1e-9); eq("p6 v", sf(sqrt(25 / 3)), 2.89); eq("p6 land", u * u + 2 * G * r, 25)
eq("p6 24", 2 * G * r, 24); eq("p6 eq", 12 * c, 25 - 24 * c, 1e-9)
r, m, u = 0.8, 0.4, 6
eq("p7 cos", (2 * G * r - u * u) / (3 * G * r), -5 / 6); eq("p7 20 + 16c", u * u - 2 * G * r, 20)
eq("p7 v2", G * r * 5 / 6, 6.6667, 1e-3); eq("p7 v", sf(sqrt(G * r * 5 / 6)), 2.58)
eq("p7 vy2", sf(G * r * 5 / 6 * 11 / 36, 4), 2.037); eq("p7 rise", sf(G * r * 5 / 6 * 11 / 36 / (2 * G), 4), 0.1019)
eq("p7 h0", sf(r * (1 + 5 / 6), 4), 1.467); eq("p7 H", sf(r * (1 + 5 / 6) + G * r * 5 / 6 * 11 / 36 / (2 * G)), 1.57); assert 1.5686 < 2 * r
th, v = integrate_slack(u, r); eq("p7 sim", th, acos(-5 / 6), 1e-3)

# Stretch: through the centre
s3 = sqrt(3); r = 1.0
sa = 1 / s3; eq("tan2", sa ** 2 / (1 - sa ** 2), 0.5); eq("u2", (2 + 3 * sa) * G * r, (2 + s3) * G * r); eq("u2 3sf", sf(2 + s3), 3.73)
ca = sqrt(1 - sa * sa); v = sqrt(G * r * sa)
x0, y0, vx, vy = r * ca, r * sa, -v * sa, v * ca
t = -x0 / vx; eq("through O", y0 + vy * t - 0.5 * G * t * t, 0, 1e-9)
# stretch: peg
l = 1.0; eq("peg d", 3 / 5 * l, 0.6); eq("peg ineq", 2 * l - 5 * (l - 0.6), 0)

# Quiz
eq("q3 top v2", 4.5 - 4, 0.5)

# Mark totals (also counted by the kit)
assert 2 + 5 + 2 == 9 and 2 + 5 + 3 == 10 and 5 + 2 + 2 == 9
print("ok")
