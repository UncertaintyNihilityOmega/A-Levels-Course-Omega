# checks/math.fm.impulse.py: recomputes every number in Direct impact and restitution.
# Standard library only. Collisions are solved with a general routine and compared with the closed forms in the chapter.
from math import isclose, sqrt

G = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def hit(m1, u1, m2, u2, e):
    """direct impact: sphere 1 behind sphere 2; velocities along the positive direction. Returns (v1, v2)."""
    v1 = (m1 * u1 + m2 * u2 - m2 * e * (u1 - u2)) / (m1 + m2)
    v2 = (m1 * u1 + m2 * u2 + m1 * e * (u1 - u2)) / (m1 + m2)
    # self-test of both laws
    eq("momentum", m1 * v1 + m2 * v2, m1 * u1 + m2 * u2, 1e-9)
    eq("NEL", v2 - v1, e * (u1 - u2), 1e-9)
    return v1, v2


def ke(*pairs):
    return sum(0.5 * m * v * v for m, v in pairs)


def lost(m1, m2, e, w):
    return m1 * m2 / (2 * (m1 + m2)) * (1 - e * e) * w * w


# ---- impulse
eq("bat I", 0.4 * 20 + 0.4 * 15, 14)
eq("bat F", 14 / 0.01, 1400)
eq("bat weight multiple", 1400 / (0.4 * 10) > 300, True)
I = simpson(lambda t: 3e7 * t * (0.01 - t), 0, 0.01)
eq("pulse I", I, 5, 1e-9)
eq("pulse peak", 3e7 * 0.005 * 0.005, 750, 1e-9)
eq("pulse v", 5 / 0.25, 20)
eq("pulse bracket", 1e-6 / 2 - 1e-6 / 3, 1e-6 / 6, 1e-18)

# ---- proof of the loss formula, several cases (numeric check of the 7 lines)
for (m1, m2, u1, u2, e) in [(2, 3, 5, -1, 0.5), (1, 7, 3, 2, 0.2), (4, 2, 6, -3, 1 / 3), (5, 5, 1, -4, 1.0), (3, 1, 2, 2, 0.4)]:
    v1, v2 = hit(m1, u1, m2, u2, e)
    M = m1 + m2
    V = (m1 * u1 + m2 * u2) / M
    w = u1 - u2
    eq("proof step2a", u1 - V, m2 * w / M, 1e-9)
    eq("proof step2b", u2 - V, -m1 * w / M, 1e-9)
    eq("proof step3a", v1 - V, -e * m2 * w / M, 1e-9)
    eq("proof step3b", v2 - V, e * m1 * w / M, 1e-9)
    eq("proof step5", 0.5 * m1 * (m2 * w / M) ** 2 + 0.5 * m2 * (m1 * w / M) ** 2, 0.5 * m1 * m2 / M * w * w, 1e-9)
    eq("proof step7", ke((m1, u1), (m2, u2)) - ke((m1, v1), (m2, v2)), lost(m1, m2, e, w), 1e-9)

# ---- general speeds (exam eg 1)
m1, m2, u, e = 3.0, 5.0, 7.0, 0.35
v1, v2 = hit(m1, u, m2, 0, e)
eq("general vB", v2, m1 * (1 + e) * u / (m1 + m2))
eq("general vA", v1, (m1 - e * m2) * u / (m1 + m2))

# ---- numeric eg: 2 kg at 5, 3 kg at -1, e 0.5
v1, v2 = hit(2, 5, 3, -1, 0.5)
eq("n1 v1", v1, -0.4)
eq("n1 v2", v2, 2.6)
eq("n1 KE before", ke((2, 5), (3, -1)), 26.5)
eq("n1 KE after", ke((2, v1), (3, v2)), 10.3)
eq("n1 lost", 26.5 - 10.3, 16.2, 1e-9)
eq("n1 lost formula", lost(2, 3, 0.5, 6), 16.2, 1e-9)
eq("n1 impulse", 3 * (v2 - (-1)), 10.8, 1e-9)
eq("n1 impulse formula", 2 * 3 * 1.5 * 6 / 5, 10.8)

# ---- exam eg: m and 3m
for e in (0.6,):
    v1, v2 = hit(1, 1, 3, 0, e)
    eq("ex2 vB", v2, (1 + e) / 4)
    eq("ex2 vA", v1, (1 - 3 * e) / 4)
    after = ke((1, v1), (3, v2))
    eq("ex2 ratio", after / 0.5, 13 / 25, 1e-12)
    eq("ex2 formula", (1 + 3 * e * e) / 8, 13 / 50, 1e-12)
    eq("ex2 vA -0.2", v1, -0.2)
    eq("ex2 vB 0.4", v2, 0.4)
    eq("ex2 impulse", 3 * v2, 1.2)
    eq("ex2 loss", lost(1, 3, e, 1), 0.24, 1e-12)
eq("ex2 e from ratio", sqrt((52 / 25 - 1) / 3), 0.6)
for e in (0.0, 0.3, 0.9):
    v1, v2 = hit(1, 1, 3, 0, e)
    eq("ex2 KE gen", ke((1, v1), (3, v2)), (1 + 3 * e * e) / 8, 1e-12)

# ---- wall
eq("wall e", 9 / 12, 0.75)
eq("wall I", 0.16 * (9 + 12), 3.36)
eq("wall F", 3.36 / 0.01, 336)
eq("wall KE", 0.5 * 0.16 * (144 - 81), 5.04)
eq("wall KE formula", 0.5 * 0.16 * (1 - 0.75 ** 2) * 144, 5.04)

# ---- bouncing ball
h, e = 2.0, 0.6
eq("ball v", 2 * G * h, 40)
eq("ball h1", (0.6 ** 2) * 40 / 20, 0.72)
eq("ball h1 form", 2 * 0.36, 0.72)
eq("ball h2", 2 * 0.36 ** 2, 0.2592)
D = h + 2 * 0.72 / (1 - 0.36)
eq("ball D", D, 4.25)
eq("ball D formula", h * (1 + e * e) / (1 - e * e), 4.25)
t0 = sqrt(2 * h / G)
eq("ball t0", t0, sqrt(0.4))
eq("ball first up-down", 2 * 0.6 * sqrt(40) / 10, 1.2 * t0)
T = t0 + 1.2 * t0 / (1 - 0.6)
eq("ball T", T, 4 * sqrt(0.4))
eq("ball T 3sf", sf(T), 2.53)
eq("ball T formula", t0 * (1 + e) / (1 - e), T)
# brute force simulation of the bounces
tt, dd, v, hh = t0, h, e * sqrt(2 * G * h), 0.0
for _ in range(200):
    tt += 2 * v / G
    dd += 2 * v * v / (2 * G)
    v *= e
eq("ball sim T", tt, T, 1e-9)
eq("ball sim D", dd, D, 1e-9)

# ---- three spheres, numbers: masses 2, 2, 1; e 0.5; u 12
vA, vB = hit(2, 12, 2, 0, 0.5)
eq("3s vA", vA, 3)
eq("3s vB", vB, 9)
wB, wC = hit(2, vB, 1, 0, 0.5)
eq("3s wB", wB, 4.5)
eq("3s wC", wC, 9)
eq("3s no collision", vA < wB, True)

# ---- exam eg three spheres, general e
for e in (0.0, 0.1, 0.2, 0.3, 0.5, 0.9, 1.0):
    vA, vB = hit(2, 1, 2, 0, e)
    eq("3g vA", vA, (1 - e) / 2)
    eq("3g vB", vB, (1 + e) / 2)
    wB, wC = hit(2, vB, 1, 0, e)
    eq("3g wB", wB, (1 + e) * (2 - e) / 6)
    eq("3g wC", wC, (1 + e) ** 2 / 3)
    catches = vA > wB + 1e-12
    eq("3g condition", catches, e < 2 - sqrt(3))
eq("3g root", (2 - sqrt(3)) ** 2 - 4 * (2 - sqrt(3)) + 1, 0, 1e-12)
eq("3g other root>1", 2 + sqrt(3) > 1, True)
eq("3g 2-sqrt3", sf(2 - sqrt(3)), 0.268)
vA, vB = hit(2, 10, 2, 0, 0.2)
wB, _ = hit(2, vB, 1, 0, 0.2)
eq("3g e=0.2 vA", vA, 4)
eq("3g e=0.2 wB", wB, 3.6)

# ---- spot the error
vA, vB = hit(3, 6, 2, -2, 0.5)
eq("spot v1", vA, 1.2)
eq("spot v2", vB, 5.2)
eq("spot momentum", 3 * 6 + 2 * (-2), 14)
eq("spot student v1", (22 - 4) / 5, 3.6)
eq("spot student v2", 3.6 + 2, 5.6)
eq("spot student separation", 5.6 - 3.6, 2, 1e-12)
eq("spot marks", 1 + 0 + 1 + 0 + 1 + 0, 3)

# ---- try block
eq("t1 I", 0.5 * 0 - 0.5 * 8, -4)
eq("t1 F", 4 / 0.02, 200)
v1, v2 = hit(2, 6, 4, 0, 0)
eq("t2 v", v1, 2)
eq("t2 v2", v2, 2)
eq("t2 KE lost", ke((2, 6)) - ke((6, 2)), 24)
eq("t2 formula", lost(2, 4, 0, 6), 24)
v1, v2 = hit(1, 5, 1, 1, 1)
eq("t3 swap", (v1, v2), (1, 5)) if False else None
eq("t3 v1", v1, 1)
eq("t3 v2", v2, 5)
eq("t4 e", sqrt(3.2 / 5), 0.8)
v1, v2 = hit(1, 4, 3, 0, 1 / 3)
eq("t5 v1", v1, 0, 1e-12)
eq("t5 v2", v2, 4 / 3, 1e-12)
eq("t6 e", sqrt(0.64), 0.8)
eq("t7 I", 3 * 1 * 1.5 * 6 / 4, 6.75)
v1, v2 = hit(3, 4, 1, -2, 0.5)
eq("t7 I direct", 1 * (v2 - (-2)), 6.75)

# ---- exam practice
eq("ep1 I", 0.25 * 20 + 0.25 * 12, 8)
eq("ep1 F", 8 / 0.02, 400)
v1, v2 = hit(0.5, 6, 0.3, 0, 0.4)
eq("ep2 vA", v1, 2.85)
eq("ep2 vB", v2, 5.25)
eq("ep3 v", 0.7 * 10, 7)
eq("ep3 I", 0.2 * 17, 3.4)
eq("ep3 KE", 0.5 * 0.2 * (100 - 49), 5.1)
eq("ep4 v", sqrt(2 * G * 5), 10)
eq("ep4 h2", 5 * 0.64 ** 2, 2.048)
eq("ep4 D", 5 + 2 * 3.2 / (1 - 0.64), 22.77777777777778)
eq("ep4 D 3sf", sf(5 + 2 * 3.2 / (1 - 0.64)), 22.8)
eq("ep4 D formula", 5 * (1 + 0.64) / (1 - 0.64), 5 + 2 * 3.2 / 0.36, 1e-9)
# ep5: A 4 kg 6, B 2 kg -3, A after 2
vB5 = (4 * 6 - 2 * 3 - 4 * 2) / 2
eq("ep5 vB", vB5, 5)
eq("ep5 e", (vB5 - 2) / 9, 1 / 3)
v1, v2 = hit(4, 6, 2, -3, 1 / 3)
eq("ep5 hit v1", v1, 2)
eq("ep5 hit v2", v2, 5)
eq("ep5 KE before", ke((4, 6), (2, -3)), 81)
eq("ep5 KE after", ke((4, 2), (2, 5)), 33)
eq("ep5 lost", 81 - 33, 48)
eq("ep5 formula", lost(4, 2, 1 / 3, 9), 48, 1e-9)
# ep6: m, 3m, wall
for e in (0.0, 0.1, 0.2, 0.33):
    vA, vB = hit(1, 1, 3, 0, e)
    eq("ep6 vA>0", vA > 0, True)
    eq("ep6 vB", vB, (1 + e) / 4)
    back = e * vB
    eq("ep6 approach", back + vA > 0, True)
# even for e > 1/3, still a collision (not asked): (e-1)^2 > 0
for e in (0.4, 0.7, 0.95):
    vA, vB = hit(1, 1, 3, 0, e)
    eq("ep6 beyond", e * vB > -vA if vA < 0 else True, True)
    eq("ep6 identity", e * (1 + e) - (3 * e - 1), (e - 1) ** 2, 1e-12)
# ep7: 2m and m
for e in (0.5,):
    vA, vB = hit(2, 1, 1, 0, e)
    eq("ep7 vA", vA, (2 - e) / 3)
    eq("ep7 vB", vB, 2 * (1 + e) / 3)
    eq("ep7 ratio", ke((2, vA), (1, vB)) / ke((2, 1)), 0.75, 1e-12)
    eq("ep7 impulse", 1 * vB, 1.0, 1e-12)
for e in (0.0, 0.4, 1.0):
    vA, vB = hit(2, 1, 1, 0, e)
    eq("ep7 KE gen", ke((2, vA), (1, vB)), (2 + e * e) / 3, 1e-12)
eq("ep7 bracket", (2 - 0.3) ** 2 + 2 * (1 + 0.3) ** 2, 6 + 3 * 0.09, 1e-12)
eq("ep7 e", sqrt(9 / 4 - 2), 0.5)
# ep8
h, e = 1.8, 0.5
v = sqrt(2 * G * h)
eq("ep8 v", v, 6)
eq("ep8 after", e * v, 3)
eq("ep8 flight", 2 * e * v / G, 0.6)
T8 = v / G + 2 * e * v / G / (1 - e)
eq("ep8 T", T8, 1.8)
D8 = h + 2 * (e * e * h) / (1 - e * e)
eq("ep8 D", D8, 3)
eq("ep8 h1", e * e * h, 0.45)
eq("ep8 h2", e ** 4 * h, 0.1125)
tt, dd, v = v / G, h, e * v
for _ in range(200):
    tt += 2 * v / G
    dd += v * v / G
    v *= e
eq("ep8 sim T", tt, 1.8, 1e-9)
eq("ep8 sim D", dd, 3.0, 1e-9)

# ---- stretch
v = sqrt(2 * G * 1.25)
eq("s1 v", v, 5)
M, m = 0.6, 0.1
V1, V2 = hit(M, v, m, -v, 1)
eq("s1 V1", V1, 15 / 7, 1e-12)
eq("s1 V2", V2, 85 / 7, 1e-12)
eq("s1 V2 3sf", sf(V2), 12.1)
eq("s1 height", V2 ** 2 / (2 * G), 7.372448979591836, 1e-9)
eq("s1 height 3sf", sf(V2 ** 2 / 20), 7.37)
eq("s1 ratio", V2 ** 2 / 20 / 1.25 > 5, True)
eq("s1 momentum eq", 6 * V1 + V2, 25, 1e-12)
for (m1, m2) in [(1, 4), (3, 7), (2, 5)]:
    e = m1 / m2
    vA, vB = hit(m1, 1, m2, 0, e)
    eq("s2 stop", vA, 0, 1e-12)
    eq("s2 fraction", 1 - ke((m2, vB)) / ke((m1, 1)), 1 - e, 1e-12)

# ---- quiz
v1, v2 = hit(2, 6, 1, 0, 0)
eq("q5", v1, 4)
eq("q3", 4 * 0.25, 1)
print("ok")
