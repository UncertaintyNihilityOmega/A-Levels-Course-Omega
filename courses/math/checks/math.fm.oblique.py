# checks/math.fm.oblique.py: recomputes every number in Oblique impact.
# Standard library only. Wall and sphere impacts are solved with vectors and compared with the chapter's formulas.
from math import isclose, sqrt, sin, cos, tan, atan, atan2, radians, degrees

G = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def wall(u, alpha_deg, e):
    """smooth wall along x; velocity makes alpha with the wall; returns (par, perp_before, perp_after, speed, beta_deg)"""
    a = radians(alpha_deg)
    par, perp = u * cos(a), u * sin(a)
    pa = e * perp
    return par, perp, pa, sqrt(par ** 2 + pa ** 2), degrees(atan2(pa, par))


def spheres(m1, m2, u1, th1, u2, th2, e):
    a = (u1 * cos(radians(th1)), u1 * sin(radians(th1)))
    b = (u2 * cos(radians(th2)), u2 * sin(radians(th2)))
    ap = a[0] - b[0]
    P = m1 * a[0] + m2 * b[0]
    v1x = (P - m2 * e * ap) / (m1 + m2)
    v2x = (P + m1 * e * ap) / (m1 + m2)
    # self-tests: momentum and Newton's law along the line, perpendicular unchanged
    eq("mom", m1 * v1x + m2 * v2x, P, 1e-9)
    eq("nel", v2x - v1x, e * ap, 1e-9)
    return (v1x, a[1]), (v2x, b[1]), a, b


def ke(m, v):
    return 0.5 * m * (v[0] ** 2 + v[1] ** 2)


# ---- derivation: tan beta = e tan alpha, speed
for (u, al, e) in [(7, 55, 0.35), (10, 20, 0.9), (3, 80, 0.0), (5, 40, 1.0)]:
    par, perp, pa, sp, beta = wall(u, al, e)
    eq("tan beta", tan(radians(beta)), e * tan(radians(al)), 1e-9)
    eq("speed", sp, u * sqrt(cos(radians(al)) ** 2 + e * e * sin(radians(al)) ** 2), 1e-9)
    eq("KE lost formula", 0.5 * u * u - 0.5 * sp * sp, 0.5 * u * u * (1 - e * e) * sin(radians(al)) ** 2, 1e-9)

# ---- widget figure numbers (alpha 40, e 0.6)
par, perp, pa, sp, beta = wall(5, 40, 0.6)
eq("fig beta", sf(beta, 3), 26.7)
eq("fig head y", 110 * 0.6 * sin(radians(40)), 42.4, 0.05)

# ---- plain eg: 0.5 kg, 20 m/s, 30 degrees, e 0.6
par, perp, pa, sp, beta = wall(20, 30, 0.6)
eq("e1 par", sf(par, 4), 17.32)
eq("e1 perp", perp, 10)
eq("e1 perp after", pa, 6)
eq("e1 speed sq", sp ** 2, 336, 1e-9)
eq("e1 speed", sf(sp), 18.3)
eq("e1 beta", round(beta, 1), 19.1)
eq("e1 impulse", 0.5 * (6 + 10), 8)
eq("e1 KE lost", 0.5 * 0.5 * (400 - 336), 16)
eq("e1 KE formula", 0.5 * 0.5 * 400 * (1 - 0.36) * 0.25, 16)

# ---- corner eg
ux, uy = 10 * cos(radians(30)), 10 * sin(radians(30))
eq("corner ux", sf(ux, 4), 8.660)
after1 = (ux, -0.8 * uy)
eq("corner after 1", after1[1], -4)
after2 = (-0.5 * after1[0], after1[1])
eq("corner x", sf(after2[0], 4), -4.330)
eq("corner speed sq", after2[0] ** 2 + after2[1] ** 2, 18.75 + 16, 1e-9)
eq("corner speed", sf(sqrt(after2[0] ** 2 + after2[1] ** 2)), 5.89)
# equal e: velocity reversed and multiplied by e
e = 0.7
v = (ux, uy)
a1 = (v[0], -e * v[1])
a2 = (-e * a1[0], a1[1])
eq("corner equal e x", a2[0], -e * v[0] * 1, 1e-12)
eq("corner equal e y", a2[1], -e * v[1], 1e-12)

# ---- exam eg: barrier 60 degrees, KE 7/16 remains
e = sqrt(((7 / 16) - 0.25) / 0.75)
eq("barrier e", e, 0.5)
eq("barrier algebra", 0.25 + 0.75 * 0.25, 7 / 16)
beta = degrees(atan(e * tan(radians(60))))
eq("barrier beta", sf(beta, 3), 40.9)
phi = 60 - beta
eq("barrier phi", sf(phi, 3), 19.1)
eq("barrier tan phi", tan(radians(phi)), sqrt(3) / 5, 1e-12)
eq("barrier cos2", cos(radians(phi)) ** 2, 25 / 28, 1e-12)
eq("barrier sin2", sin(radians(phi)) ** 2, 3 / 28, 1e-12)
v1sq = 7 / 16
v2sq = v1sq * (cos(radians(phi)) ** 2 + e * e * sin(radians(phi)) ** 2)
eq("barrier v2sq", v2sq, 103 / 256, 1e-12)
eq("barrier v2", sf(sqrt(v2sq)), 0.634)
eq("barrier v2 exact", sqrt(103) / 16, sqrt(v2sq), 1e-12)
eq("barrier 7/16 -> 9/16 lost", 1 - 7 / 16, 9 / 16)
eq("barrier (25+3/4)/28", (25 + 0.75) / 28 * 7 / 16, 103 / 256, 1e-12)
# geometry check of the figure: triangle OPQ, O=(250,170), P=(210,170), alpha 60, e 0.5
O, P = (250.0, 170.0), (210.0, 170.0)
dirq = (cos(radians(beta)), -sin(radians(beta)))
b2 = (0.5, -sqrt(3) / 2)
# P + s*dirq = O + t*b2
det = dirq[0] * (-b2[1]) - (-b2[0]) * dirq[1]
s = ((O[0] - P[0]) * (-b2[1]) - (-b2[0]) * (O[1] - P[1])) / det
Q = (P[0] + s * dirq[0], P[1] + s * dirq[1])
eq("fig Q x", Q[0], 290.0, 0.05)
eq("fig Q y", Q[1], 100.7, 0.1)
# angle between the path PQ and barrier 2 (directions) should be phi
cosang = abs(dirq[0] * b2[0] + dirq[1] * b2[1])
eq("fig angle at Q", degrees(atan2(sqrt(1 - cosang ** 2), cosang)), phi, 1e-6)
# simulate the two impacts with vectors
u = 1.0
v = (-u * cos(radians(60)), -u * sin(radians(60)))          # barrier 1 along x, ball moving down-right? direction of the incoming x is arbitrary
v = (u * cos(radians(60)), -u * sin(radians(60)))
v = (v[0], -e * v[1])
eq("sim v1 speed sq", v[0] ** 2 + v[1] ** 2, 7 / 16, 1e-12)
n2 = (-sin(radians(60)), cos(radians(60)))                  # barrier 2 at 120 degrees: direction (cos120, sin120)
d2 = (cos(radians(60)), sin(radians(60)))
nrm = (-d2[1], d2[0])
vt = v[0] * d2[0] + v[1] * d2[1]
vn = v[0] * nrm[0] + v[1] * nrm[1]
vv2 = vt ** 2 + (e * vn) ** 2
eq("sim v2sq", vv2, 103 / 256, 1e-12)

# ---- exam eg: two spheres, equal masses, e = 1, theta general
for th in (10, 30, 55, 80):
    v1, v2, a, b = spheres(1, 1, 1, th, 0, 0, 1)
    eq("90 deg v1", v1[0], 0, 1e-12)
    eq("90 deg v2", v2[0], cos(radians(th)), 1e-12)
    eq("90 deg dot", v1[0] * v2[0] + v1[1] * v2[1], 0, 1e-12)
    eq("90 deg v1 perp", v1[1], sin(radians(th)), 1e-12)

# ---- exam eg: find e (30 -> 60, e = 1/3)
v1, v2, a, b = spheres(1, 1, 1, 30, 0, 0, 1 / 3)
eq("find e angle", degrees(atan2(v1[1], v1[0])), 60, 1e-9)
eq("find e vA", v1[0], sqrt(3) / 4 * (1 - 1 / 3), 1e-12)
eq("find e algebra", 3 * (1 - 1 / 3), 2)
for e in (0.1, 0.5, 0.9):
    v1, v2, a, b = spheres(1, 1, 1, 30, 0, 0, e)
    eq("tan psi", v1[1] / v1[0], 2 * tan(radians(30)) / (1 - e), 1e-9)

# ---- plain eg: 2 kg and 3 kg, 10 m/s at 30, e 0.5
v1, v2, a, b = spheres(2, 3, 10, 30, 0, 0, 0.5)
eq("p1 along A", sf(a[0], 4), 8.660)
eq("p1 v1x", sf(v1[0], 3), 0.866)
eq("p1 v2x", sf(v2[0], 3), 5.20)
eq("p1 A speed", sf(sqrt(v1[0] ** 2 + v1[1] ** 2)), 5.07)
eq("p1 A angle", round(degrees(atan2(v1[1], v1[0])), 1), 80.2)
eq("p1 KE before", ke(2, a), 100)
eq("p1 KE after", ke(2, v1) + ke(3, v2), 66.25, 1e-9)
eq("p1 KE A", ke(2, v1), 25.75, 1e-9)
eq("p1 KE B", ke(3, v2), 40.5, 1e-9)
eq("p1 lost", 100 - 66.25, 33.75, 1e-9)
eq("p1 lost formula", 2 * 3 * 0.75 / (2 * 5) * (10 * cos(radians(30))) ** 2, 33.75, 1e-9)
eq("p1 impulse", sf(3 * v2[0]), 15.6)

# ---- direct then oblique exam eg
m = 1.0
vA = (2 - 0.5) / 3
vB = 2 * (1.5) / 3
eq("d1 vA", vA, 0.5)
eq("d1 vB", vB, 1.0)
par, perp, pa, sp, beta = wall(1.0, 30, 0.8)
eq("d1 par", sf(par, 3), 0.866)
eq("d1 perp after", pa, 0.4)
eq("d1 speed sq", sp ** 2, 0.91, 1e-12)
eq("d1 speed", sf(sp), 0.954)
eq("d1 beta", round(beta, 1), 24.8)
eq("d1 fraction", 1 - sp ** 2 / 1.0, 0.09, 1e-12)

# ---- spot the error
par, perp, pa, sp, beta = wall(12, 30, 0.5)
eq("spot par", sf(par, 4), 10.39)
eq("spot perp after", pa, 3)
eq("spot speed", sf(sp), 10.8)
eq("spot student speed", sf(sqrt(6 ** 2 + (0.5 * 12 * cos(radians(30))) ** 2)), 7.94)
eq("spot student 5.196", sf(0.5 * 12 * cos(radians(30)), 4), 5.196)
eq("spot marks", 0 + 1 + 1 + 0, 2)

# ---- try block
par, perp, pa, sp, beta = wall(10, 45, 0.4)
eq("t1 par", sf(par, 3), 7.07)
eq("t1 perp", sf(pa, 3), 2.83)
eq("t2 e", sf(tan(radians(30)) / tan(radians(50))), 0.484)
eq("t3 I", sf(0.4 * 1.5 * 12 * sin(radians(60))), 6.24)
eq("t4 vB", 6, 6)
eq("t4 check", (8 - 4) / 2 + 4, 6)
eq("t5 e", sqrt((13 / 16 - 3 / 4) * 4), 0.5)
eq("t5 frac", 1 - 3 / 16, 13 / 16)
v1, v2, a, b = spheres(1, 1, 6, 60, 0, 0, 1)
eq("t6 A", sf(v1[1]), 5.20)
eq("t6 B", v2[0], 3, 1e-12)
eq("t7 speed", 8 * 0.5, 4)

# ---- exam practice
par, perp, pa, sp, beta = wall(10, 45, 0.4)
eq("ep1", sf(sp), 7.62)
eq("ep1 sq", 50 + 8, sp ** 2, 1e-9)
e = tan(radians(30)) / tan(radians(50))
eq("ep2 e", sf(e), 0.484)
rem = cos(radians(50)) ** 2 + e * e * sin(radians(50)) ** 2
eq("ep2 remaining", round(rem, 4), 0.5509)
eq("ep2 lost %", sf(100 * (1 - rem)), 44.9)
eq("ep2 cos2", round(cos(radians(50)) ** 2, 4), 0.4132)
eq("ep2 e2 sin2", round(e * e * sin(radians(50)) ** 2, 4), 0.1377)
eq("ep2 e2", round(e * e, 4), 0.2347)
eq("ep2 sin2", round(sin(radians(50)) ** 2, 4), 0.5868)
par, perp, pa, sp, beta = wall(12, 60, 0.5)
eq("ep3 perp", sf(perp, 4), 10.39)
eq("ep3 I", sf(0.4 * (perp + pa)), 6.24)
eq("ep3 KE", 0.5 * 0.4 * 144 * 0.75 * 0.75, 16.2, 1e-9)
eq("ep3 KE direct", 0.5 * 0.4 * (144 - sp ** 2), 16.2, 1e-9)
v1, v2, a, b = spheres(0.5, 0.25, 8, 60, 0, 0, 0.6)
eq("ep4 along", a[0], 4, 1e-12)
eq("ep4 perp", sf(a[1], 4), 6.928)
eq("ep4 vA", sf(v1[0], 4), 1.867)
eq("ep4 vB", sf(v2[0], 3), 4.27)
eq("ep4 speed A", sf(sqrt(v1[0] ** 2 + v1[1] ** 2)), 7.18)
eq("ep4 angle A", round(degrees(atan2(v1[1], v1[0])), 1), 74.9)
v1, v2, a, b = spheres(1, 1, 12, 40, 0, 0, 1)
eq("ep5 vB", sf(v2[0]), 9.19)
eq("ep5 A", sf(v1[1]), 7.71)
eq("ep5 A along", v1[0], 0, 1e-9)
eq("ep6 fraction", 0.5 + 0.5 * 0.36, 17 / 25, 1e-12)
eq("ep6 e", sqrt(2 * 17 / 25 - 1), 0.6)
eq("ep6 lost", 1 - 17 / 25, 8 / 25, 1e-12)
c = s_ = 1 / sqrt(2)
a1 = (c, -0.6 * s_)
a2 = (-0.6 * a1[0], a1[1])
eq("ep6 x", a2[0], -0.6 * c, 1e-12)
eq("ep6 y", a2[1], -0.6 * s_, 1e-12)
eq("ep6 speed", sqrt(a2[0] ** 2 + a2[1] ** 2), 0.6, 1e-12)
v1, v2, a, b = spheres(3, 2, 1, degrees(atan(3 / 4)), 0, 0, 0.5)
eq("ep7 vA", v1[0], 0.32, 1e-12)
eq("ep7 vB", v2[0], 0.72, 1e-12)
eq("ep7 perp", v1[1], 0.6, 1e-12)
eq("ep7 speed", sf(sqrt(v1[0] ** 2 + v1[1] ** 2)), 0.680)
eq("ep7 angle", round(degrees(atan2(0.6, 0.32)), 1), 61.9)
eq("ep7 KE before", ke(3, a), 1.5, 1e-12)
eq("ep7 KE after A", ke(3, v1), 0.6936, 1e-12)
eq("ep7 KE after B", ke(2, v2), 0.5184, 1e-12)
eq("ep7 lost", 1.5 - ke(3, v1) - ke(2, v2), 0.288, 1e-12)
eq("ep7 0.4624", 0.32 ** 2 + 0.6 ** 2, 0.4624, 1e-12)
eq("ep7 2.4u eq", 3 * 0.8, 2.4)
vB8 = 3 * 1.6 / 4
eq("ep8 vB", vB8, 1.2, 1e-12)
par, perp, pa, sp, beta = wall(vB8, 45, 0.5)
eq("ep8 par", sf(par, 4), 0.8485)
eq("ep8 perp after", sf(pa, 4), 0.4243)
eq("ep8 speed", sf(sp / 1.0, 3), 0.949)
eq("ep8 angle", round(beta, 1), 26.6)
eq("ep8 frac", 1 - (sp / vB8) ** 2, 3 / 8, 1e-12)
eq("ep8 ratio", sf(sp ** 2 / vB8 ** 2, 3), 0.625)
v1, v2, a, b = spheres(3, 1, 1, 0, 0, 0, 0.6)
eq("ep8 vA", v1[0], 0.6, 1e-12)

# ---- stretch: inclined plane
h, al, e = 1.25, radians(30), 0.5
v = sqrt(2 * G * h)
eq("s1 v", v, 5)
eq("s1 par", sf(v * sin(al), 3), 2.50)
eq("s1 perp", sf(v * cos(al), 3), 4.33)
eq("s1 perp after", sf(e * v * cos(al), 4), 2.165)
T = 2 * e * v * cos(al) / (G * cos(al))
eq("s1 T", T, 0.5)
eq("s1 T formula", 2 * e * v / G, 0.5)
dist = v * sin(al) * T + 0.5 * G * sin(al) * T ** 2
eq("s1 dist", dist, 4 * e * (1 + e) * h * sin(al), 1e-12)
eq("s1 value", dist, 1.875, 1e-12)
eq("s1 2.5T+2.5T^2", 2.5 * T + 0.5 * 5 * T * T, 1.875, 1e-12)
eq("s1 accel along", G * sin(al), 5, 1e-12)
# s1 simulation by stepping
x, y, vx, vy = 0.0, 0.0, v * sin(al), e * v * cos(al)
dt = 1e-5
t = 0.0
while True:
    vx += G * sin(al) * dt
    vy -= G * cos(al) * dt
    x += vx * dt
    y += vy * dt
    t += dt
    if y <= 0:
        break
eq("s1 sim T", t, 0.5, 1e-3)
eq("s1 sim dist", x, 1.875, 1e-2)

# ---- quiz
eq("q5", cos(radians(30)) ** 2 + 0.25 * sin(radians(30)) ** 2, 13 / 16, 1e-12)
print("ok")
