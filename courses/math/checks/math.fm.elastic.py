# checks/math.fm.elastic.py: recomputes every number in Hooke's law and elastic energy.
# Standard library only. Energy answers are also confirmed by numerical integration of the motion.
from math import isclose, sqrt
from fractions import Fraction as F

G = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def T(lam, l, x):
    return lam * x / l if x > 0 else 0.0


def E(lam, l, x):
    return lam * x * x / (2 * l) if x > 0 else 0.0


def simulate(m, lam, l, force, s0, v0, tmax, dt=1e-5):
    """Particle on a line at position s with a string of natural length l from the origin (tension when s > l).
    force(s) is the other force along +s. Returns (greatest speed, least s, greatest s)."""
    s, v = s0, v0
    vmax = abs(v)
    smin = smax = s
    t = 0.0
    while t < tmax:
        a = (force(s) - T(lam, l, s - l)) / m
        v += a * dt
        s += v * dt
        vmax = max(vmax, abs(v))
        smin, smax = min(smin, s), max(smax, s)
        t += dt
    return vmax, smin, smax


# Warm-up
eq("w1", sqrt(2 * G * 1.5), sqrt(30)); eq("w1 3sf", round(sqrt(30), 2), 5.48)
eq("w2", (20 - 0.3 * 4 * G) / 4, 2)
eq("w3", 12 * 0.5, 6)

# Hooke's law examples
eq("eg1a", T(24, 0.8, 0.2), 6)
eq("eg1b", 15 * 0.8 / 24, 0.5)
eq("eg2 lam", 5 * 0.6 / 0.15, 20); eq("eg2 check", 20 * 0.15 / 0.6, 5)

# two strings on a table
k1, k2 = 12 / 0.6, 15 / 0.5
eq("k1", k1, 20); eq("k2", k2, 30)
y = F(9, 10) / F(5, 2)  # x = 1.5y and x + y = 0.9
x = F(3, 2) * y
eq("y", float(y), 0.36); eq("x", float(x), 0.54)
eq("T2s", k1 * float(x), 10.8); eq("T2s check", k2 * float(y), 10.8)
eq("AP", 0.6 + float(x), 1.14)

# spring compression
eq("spring x", 20 * 0.5 / 40, 0.25); eq("spring len", 0.5 - 0.25, 0.25)

# slope equilibrium range
R = 2 * G * 0.8; Fm = 0.5 * R; W = 2 * G * 0.6
eq("R", R, 16); eq("Fm", Fm, 8); eq("W", W, 12)
eq("Tmin", W - Fm, 4); eq("Tmax", W + Fm, 20)
eq("xmin", 4 / 30, 0.133, 1e-3); eq("xmax", 20 / 30, 0.667, 1e-3)

# EPE
eq("E1", E(45, 1.5, 0.4), 2.4)
eq("E2", E(45, 1.5, 0.9), 12.15)
eq("diff", E(45, 1.5, 0.9) - E(45, 1.5, 0.4), 9.75)
# plot: T = 40x for lam 20, l 0.5; area under to 0.3
eq("plot slope", 20 / 0.5, 40); eq("plot T", 40 * 0.3, 12)
eq("plot area", 0.5 * 0.3 * 12, 1.8); eq("plot E", E(20, 0.5, 0.3), 1.8)
# proof: integral of lam s / l = lam x^2/(2 l), Simpson
lam, l, xx, n = 45, 1.5, 0.4, 2000
h = xx / n
simpson = sum((1 if i in (0, n) else 4 if i % 2 else 2) * lam * (i * h) / l for i in range(n + 1)) * h / 3
eq("proof integral", simpson, E(lam, l, xx), 1e-9)

# horizontal smooth
e = E(20, 0.5, 0.3); eq("h E", e, 1.8); eq("h v2", e / (0.5 * 0.4), 9); eq("h v", sqrt(9), 3)
# two identical strings
eq("two start", E(10, 0.5, 0.8) + E(10, 0.5, 0.2), 6.8)
eq("two coef", 10 / (2 * 0.5), 10)
eq("two mid", 2 * E(10, 0.5, 0.5), 5)
eq("two v2", (6.8 - 5) / 0.2, 9)

# vertical release from O: m 0.5, l 1, lam 20
m, l, lam = 0.5, 1.0, 20
eq("greatest ext", m * G * (l + 1.0), E(lam, l, 1.0))
eq("other root", m * G * (l - 0.5) - lam * 0.5 * 0.5 / (2 * l), 0)
eq("quad", (2 * 1 + 1) * (1 - 1), 0)
xe = m * G * l / lam; eq("xe", xe, 0.25)
v2 = (m * G * (l + xe) - E(lam, l, xe)) / (0.5 * m)
eq("eg v2", v2, 22.5); eq("eg v", round(sqrt(v2), 2), 4.74)
eq("5.625", m * G * 1.25 - E(lam, l, xe), 5.625); eq("6.25", m * G * 1.25, 6.25); eq("0.625", E(lam, l, xe), 0.625)
vmax, smin, smax = simulate(m, lam, l, lambda s: m * G, 0.0, 0.0, 1.5)
eq("sim vmax", vmax, sqrt(v2), 1e-3); eq("sim greatest ext", smax - l, 1.0, 2e-3)

# Exam: slope string
m, lam, l = 0.8, 12, 0.5
Wc = m * G * 0.6; eq("Wc", Wc, 4.8)
xe = Wc * l / lam; eq("xe slope", xe, 0.2)
ke = Wc * xe - E(lam, l, xe); eq("ke", ke, 0.48)
v = sqrt(ke / (0.5 * m)); eq("v slope", v, 1.0954, 1e-4); eq("v 3sf", round(v, 2), 1.10)
eq("0.96", Wc * xe, 0.96); eq("0.48", E(lam, l, xe), 0.48)
xmax = 2 * l * Wc / lam; eq("x greatest slope", xmax, 0.4)
eq("x greatest check", Wc * xmax, E(lam, l, xmax))
vmax, smin, smax = simulate(m, lam, l, lambda s: Wc, l, 0.0, 3.0)
eq("sim slope vmax", vmax, v, 1e-3); eq("sim slope ext", smax - l, 0.4, 2e-3)

# Exam: spring with a particle on top
m, lam, l = 0.6, 30, 0.5
eq("spring eq", m * G * l / lam, 0.1)
e0 = E(lam, l, 0.3); eq("spring E0", e0, 2.7)
eq("spring v2", (e0 - m * G * 0.3) / (0.5 * m), 3)
eq("spring vmax", sqrt((e0 - m * G * 0.2 - E(lam, l, 0.1)) / (0.5 * m)), 2)
eq("1.2 and 0.3", E(lam, l, 0.1), 0.3); eq("6x0.2", m * G * 0.2, 1.2)
ee = 0.1
eq("spring top", m * G * (0.3 + ee) + E(lam, l, ee), e0)
eq("quad factor", (10 * ee - 1) * (10 * ee + 3), 0); eq("quad expand", 100 * ee ** 2 + 20 * ee - 3, 0)
eq("30e2+6e-0.9", 30 * ee ** 2 + 6 * ee - 0.9, 0)
eq("top length", l + ee, 0.6)
s, vv, t, dt = 0.2, 0.0, 0.0, 1e-5   # s = length of the spring = height of P above the floor
vm, smx, smn = 0, s, s
while t < 3:
    a = (-m * G + lam * (l - s) / l) / m
    vv += a * dt; s += vv * dt; vm = max(vm, abs(vv)); smx = max(smx, s); smn = min(smn, s); t += dt
eq("sim spring vmax", vm, 2, 1e-3); eq("sim top", smx, 0.6, 2e-3); eq("sim symmetric low", smn, 0.2, 2e-3)

# Exam: friction on a table
m, lam, l, mu = 2, 40, 1, 0.3
fr = mu * m * G; eq("fr", fr, 6)
eq("fr E", E(lam, l, 0.5), 5); eq("fr work", fr * 0.5, 3)
v = sqrt(5 - 3); eq("fr v", v, sqrt(2)); eq("fr v 3sf", round(v, 2), 1.41)
eq("fr ke", 0.5 * m * v * v, 2); d = 2 / fr; eq("fr d", d, 1 / 3); eq("fr dist", 1 - d, 2 / 3)

# Spot the error
m, lam, l = 0.5, 20, 1
eq("student eq", 5 * 0.5 - 10 * 0.5 ** 2, 0)
eq("correct", 5 * (1 + 1) - 10 * 1, 0)
eq("spot T", T(lam, l, 1), 20)

# Try
eq("t1 T", T(30, 0.4, 0.3), 22.5); eq("t1 E", E(30, 0.4, 0.3), 3.375); eq("t1 half", 0.5 * 22.5 * 0.3, 3.375)
eq("t2", 9 * 1 / (36 * 0.25), 1)
eq("t3 thrust", 32 * 0.2 / 0.8, 8); eq("t3 E", E(32, 0.8, 0.2), 0.8)
eq("t4", 15 * 0.9 / 45, 0.3); eq("t4 len", 0.9 + 0.3, 1.2)
eq("t5 x", 5 * 2 / 50, 0.2); eq("t5 E", E(50, 2, 0.2), 0.5); eq("t5 half", 0.5 * 5 * 0.2, 0.5)
eq("t6 coef", 18 / 1.2, 15); eq("t6 W", E(18, 0.6, 0.4) - E(18, 0.6, 0.2), 1.8)
eq("t7 E", E(6, 0.4, 0.2), 0.3); eq("t7 v2", 0.3 / 0.15, 2); eq("t7 v", round(sqrt(2), 2), 1.41)
eq("t8", 3 * 0.6 / 15, 0.12)
eq("t9", T(15, 0.5, 0.3), 9)

# Exam practice
eq("p1 T", T(30, 0.75, 0.15), 6); eq("p1 E", E(30, 0.75, 0.15), 0.45)
eq("p2", 3 * 0.4 / 0.06, 20)
k1, k2 = 8 / 0.4, 18 / 0.6
eq("p3 k", k1, 20); eq("p3 k2", k2, 30)
x, y = 0.48, 0.32
eq("p3 sum", x + y, 0.8); eq("p3 ratio", k1 * x, k2 * y); eq("p3 T", k1 * x, 9.6); eq("p3 AP", 0.4 + x, 0.88)
eq("p4 E", E(15, 0.6, 0.4), 2); eq("p4 fr", 0.2 * 1.5 * G, 3); eq("p4 w", 3 * 0.4, 1.2)
v2 = (2 - 1.2) / (0.5 * 1.5); eq("p4 v2", v2, 1.0667, 1e-4); eq("p4 v", round(sqrt(v2), 2), 1.03)
Wc = 0.45 * G * 0.8; eq("p5 W", Wc, 3.6)
xe = Wc * 0.9 / 18; eq("p5 x", xe, 0.18)
eq("p5 gain", Wc * xe, 0.648); eq("p5 epe", E(18, 0.9, xe), 0.324)
v2 = (0.648 - 0.324) / 0.225; eq("p5 v2", v2, 1.44); eq("p5 v", sqrt(v2), 1.2)
eq("p6 a", 5 * 0.8 / 20, 0.2)
xs = 0.2 + 0.5; eq("p6 start ext", xs, 0.7); eq("p6 E", E(20, 0.8, xs), 6.125); eq("p6 GPE", 5 * 0.7, 3.5)
v2 = (6.125 - 3.5) / 0.25; eq("p6 v2", v2, 10.5); eq("p6 v", round(sqrt(v2), 2), 3.24); eq("p6 h", v2 / (2 * G), 0.525)
R = 1 * G * 0.8; Fm = 0.2 * R; Wd = G * 0.6
eq("p7 R", R, 8); eq("p7 F", Fm, 1.6); eq("p7 Tmin", Wd - Fm, 4.4); eq("p7 Tmax", Wd + Fm, 7.6)
eq("p7 xmin", 4.4 / 40, 0.11); eq("p7 xmax", 7.6 / 40, 0.19)
xs = 4.4 / 20; eq("p7 stop", xs, 0.22); eq("p7 T", 40 * xs, 8.8)
eq("p7 energy", (Wd - Fm) * xs, E(20, 0.5, xs))
assert 8.8 > 7.6

# Stretch
lam = 60 * G * 40 / (400 / 40); eq("bungee lam", lam, 2400)
eq("bungee energy", 60 * G * (20 + 20), E(lam, 20, 20))
Tb = lam * 20 / 20; eq("bungee T", Tb, 2400); eq("bungee a", (Tb - 600) / 60, 30)
eq("series", 0.6 / 30 + 0.4 / 20, 0.04); eq("series lam", 1.0 / 0.04, 25)

# Quiz
eq("q1", T(40, 2, 0.5), 10); eq("q1 bad", 40 * 2.5 / 2, 50); eq("q1 bad2", 40 * 0.5, 20)
eq("q6", 20 * 0.2 / 0.5, 8)

# Exam-style: released from O, l = 2, lambda = 24, m = 1.2
for x in (0.4, 1.0, 2.5):
    v2 = (1.2 * 10 * (2 + x) - 24 * x * x / (2 * 2)) / 0.6
    assert abs(v2 - (-10 * (x * x - 2 * x - 4))) < 1e-9, x
E_ = 1 + 5 ** 0.5; assert abs(E_ * E_ - 2 * E_ - 4) < 1e-9 and round(E_, 2) == 3.24
assert abs(24 * 1 / 2 - 1.2 * 10) < 1e-12
assert abs((-10 * (1 - 2 - 4)) - 50) < 1e-12 and round(50 ** 0.5, 2) == 7.07

# Mark totals of the exam-style answers (also counted by the kit)
assert 2 + 4 + 3 == 9              # slope example
assert 2 + 3 + 4 + 4 == 13         # spring example
assert 1 + 1 + 1 + 1 + 1 + 1 + 1 == 7   # friction example
assert 3 + 1 + 2 == 6             # hanging-vertically release-from-O example
print("ok")
