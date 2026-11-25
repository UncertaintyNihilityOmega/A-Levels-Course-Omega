# checks/math.fm.projectiles.py: recomputes every number in Projectiles (9231 Paper 3).
# Standard library only. g = 10 throughout. Each worked example is checked by simulating the motion
# (time stepping) or by solving the equations of motion a second way.
from math import sqrt, sin, cos, tan, atan, asin, radians, degrees, isclose, pi

g = 10.0


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def pos(V, th, t, h=0.0):
    return V * cos(th) * t, h + V * sin(th) * t - 0.5 * g * t * t


def vel(V, th, t):
    return V * cos(th), V * sin(th) - g * t


def traj(V, th, x):
    return x * tan(th) - g * x * x * (1 + tan(th) ** 2) / (2 * V * V)


# warm-up
eq("w1", 12 ** 2 / 20, 7.2)
eq("w2a", sf(20 * cos(radians(30)), 3), 17.3)
eq("w2b", 20 * sin(radians(30)), 10)
for th in (0.3, 1.0):
    eq("w3", 1 / cos(th) ** 2, 1 + tan(th) ** 2)

# eg 1: V = 25, tan = 3/4
th = atan(3 / 4)
eq("cos", cos(th), 0.8); eq("sin", sin(th), 0.6)
V = 25.0
eq("vx", V * cos(th), 20); eq("vy", V * sin(th), 15)
x, y = pos(V, th, 2)
eq("eg1 x", x, 40); eq("eg1 y", y, 10)
vx, vy = vel(V, th, 2)
eq("eg1 vy", vy, -5)
eq("eg1 speed", sf(sqrt(vx ** 2 + vy ** 2), 3), 20.6)
eq("eg1 angle", sf(degrees(atan(5 / 20)), 3), 14.0)
for t in (1, 2):
    eq(f"eg1 y at {t}", pos(V, th, t)[1], 10)
eq("eg1 roots", 15 * 1 - 5 * 1, 10)

# range derivation: R = V^2 sin 2 theta / g, checked by time stepping
def simulate_range(V, th, dt=1e-5):
    x, y, vx, vy = 0.0, 0.0, V * cos(th), V * sin(th)
    t = 0.0
    while True:
        x += vx * dt; y += vy * dt; vy -= g * dt; t += dt
        if y < 0:
            return x, t


Rn, Tn = simulate_range(30, radians(40), 1e-5)
eq("range sim", Rn, 30 ** 2 * sin(radians(80)) / g, 2e-3)
eq("T sim", Tn, 2 * 30 * sin(radians(40)) / g, 1e-3)
eq("max range", 30 ** 2 / g, 90)
s = 80 * g / 30 ** 2
eq("sin2t", sf(s, 4), 0.8889)
a1 = degrees(asin(s)); eq("2theta", sf(a1, 4), 62.73, 1e-2)
eq("theta1", sf(a1 / 2, 3), 31.4)
eq("theta2", sf(90 - a1 / 2, 3), 58.6)
eq("2theta 117", sf(180 - a1, 5), 117.27, 1e-2)
for th in (radians(31.4), radians(58.6)):
    eq("range 80", 900 * sin(2 * th) / g, 80, 0.05)
eq("complement", 31.4 + 58.6, 90)
eq("sin 30 vs 60 (plot)", sin(radians(60)), 0.8660254037844386)
eq("sin2 30", sf(sin(radians(60)), 3), 0.866)
# widget text: 60 deg climbs three times as high as 30 deg
eq("height ratio", sin(radians(60)) ** 2 / sin(radians(30)) ** 2, 3)
# v^2 = V^2 - 2 g y
for V_, th_, t_ in ((20, 0.6, 0.7), (35, 1.1, 2.5)):
    x_, y_ = pos(V_, th_, t_); vx_, vy_ = vel(V_, th_, t_)
    eq("v2 shortcut", vx_ ** 2 + vy_ ** 2, V_ ** 2 - 2 * g * y_, 1e-9)
    eq("vy2", vy_ ** 2, (V_ * sin(th_)) ** 2 - 2 * g * y_, 1e-9)

# cliff eg: V = 20, 30 degrees, from y = 0 to y = -40
V = 20.0; th = radians(30)
eq("cliff vx", sf(V * cos(th), 4), 17.32, 1e-2)
eq("cliff t", 5 * 4 ** 2 - 10 * 4, 40)       # 5t^2 - 10t - 40 = 0 at t = 4
eq("cliff y", pos(V, th, 4)[1], -40)
eq("cliff root -2", 5 * 4 + 20 - 40, 0)
eq("cliff x", sf(V * cos(th) * 4, 3), 69.3)
vx, vy = vel(V, th, 4)
eq("cliff vy", vy, -30)
eq("cliff v", sf(sqrt(vx ** 2 + vy ** 2), 3), 34.6)
eq("cliff v sq", vx ** 2 + vy ** 2, 1200)
eq("cliff angle", sf(degrees(atan(30 / vx)), 3), 60.0)
eq("cliff energy", V ** 2 + 2 * g * 40, 1200)

# roof eg
V = 25.0; th = atan(3 / 4)
eq("roof t1 x", pos(V, th, 1)[0], 20)
eq("roof t2 x", pos(V, th, 2)[0], 40)
assert 20 < 30 <= 40 <= 60
eq("roof edge", 40 - 30, 10)

# table eg
eq("table t", sqrt(0.8 / 5), 0.4)
eq("table x", 3 * 0.4, 1.2)
eq("table v", sqrt(9 + 16), 5)
eq("table angle", sf(degrees(atan(4 / 3)), 3), 53.1)

# trajectory derivation numerically
for V_, th_, t_ in ((20, 0.5, 1.2), (30, 1.0, 2.0)):
    x_, y_ = pos(V_, th_, t_)
    eq("traj", traj(V_, th_, x_), y_, 1e-9)
    eq("traj cos form", x_ * tan(th_) - g * x_ ** 2 / (2 * V_ ** 2 * cos(th_) ** 2), y_, 1e-9)

# wall eg
V = 25.0
a = g * 30 ** 2 / (2 * V ** 2)
eq("wall coefficient", a, 7.2)
eq("wall coefficient frac", 9000 / 1250, 7.2)
eq("wall quad", 7.2 * 2.5, 18); eq("wall quad b", 30 * 2.5, 75); eq("wall quad c", 15.2 * 2.5, 38)
disc = 75 ** 2 - 4 * 18 * 38
eq("wall disc", disc, 2889)
T1 = (75 + sqrt(disc)) / 36; T2 = (75 - sqrt(disc)) / 36
eq("wall T1", sf(T1, 4), 3.576, 1e-3); eq("wall T2", sf(T2, 4), 0.5903, 1e-4)
eq("wall th1", sf(degrees(atan(T1)), 3), 74.4); eq("wall th2", sf(degrees(atan(T2)), 3), 30.6)
for T in (T1, T2):
    eq("wall passes", traj(V, atan(T), 30), 8, 1e-9)
eq("wall range lo", sf(T2, 3), 0.590); eq("wall range hi", sf(T1, 3), 3.58)
mid = (T1 + T2) / 2
assert traj(V, atan(mid), 30) > 8 and traj(V, atan(0.3), 30) < 8 and traj(V, atan(5.0), 30) < 8
# plot: path equations through (30, 8); the plot strings use 0.5903 and 3.5764
for T in (0.5903, 3.5764):
    eq("plot passes", T * 30 - 0.008 * (1 + T * T) * 900, 8, 2e-3)
eq("plot coefficient", g / (2 * V * V), 0.008)
# maximum heights for the plot window y 0-36
for T in (T1, T2):
    th_ = atan(T)
    assert (V * sin(th_)) ** 2 / (2 * g) < 36
eq("lob height", sf((V * sin(atan(T1))) ** 2 / (2 * g), 3), 29.0, 0.05)
eq("lob range", sf(V * V * sin(2 * atan(T1)) / g, 3), 32.4, 0.05)

# unknown V and theta eg
K = 1 / 80; T = 3 / 4
eq("2 pts a", 20 * T - 400 * K, 10); eq("2 pts b", 40 * T - 1600 * K, 10)
eq("K", g * (1 + T * T) / (2 * 625), K)
eq("V2", 10 * 25 / 16 * 80 / 2, 625)
eq("theta", sf(degrees(atan(T)), 3), 36.9)
eq("2 pts 2x eq1 minus eq2", 20 - 10, 800 * K)
eq("2 pts T", 20 * T, 10 + 5)

# basketball
th = radians(50)
eq("bb tan", sf(4.2 * tan(th), 4), 5.005, 1e-3)
eq("bb 2cos2", sf(2 * cos(th) ** 2, 4), 0.8264, 1e-4)
eq("bb 176.4", 10 * 4.2 ** 2, 176.4)
V2 = 176.4 / (2 * cos(th) ** 2 * (4.2 * tan(th) - 1.05))
eq("bb V2", sf(V2, 4), 53.97, 1e-2)
eq("bb V", sf(sqrt(V2), 3), 7.35)
eq("bb through hoop", traj(sqrt(V2), th, 4.2), 1.05, 1e-9)
eq("bb 3.955", sf(4.2 * tan(th) - 1.05, 4), 3.955, 1e-3)
eq("bb t", sf(4.2 / (sqrt(V2) * cos(th)), 3), 0.889)

# inclined plane eg: slope 30 degrees up, strikes at right angles after 2 s
u = 10 * sqrt(3) / 4; p = 10 + u / sqrt(3)
eq("plane u", sf(u, 3), 4.33); eq("plane p", p, 12.5)
eq("plane V", sqrt(u * u + p * p), sqrt(175), 1e-9)
eq("plane V 3sf", sf(sqrt(175), 3), 13.2)
eq("plane theta", sf(degrees(atan(p / u)), 3), 70.9)
eq("plane tan", p / u, 5 / sqrt(3))
x2, y2 = 2 * u, 2 * p - 20
eq("plane x", sf(x2, 3), 8.66); eq("plane y", y2, 5)
eq("plane on slope", x2 * tan(radians(30)), y2, 1e-9)
vx2, vy2 = u, p - 20
eq("plane vy", vy2, -7.5)
eq("plane perpendicular", vy2 / vx2, -tan(radians(60)), 1e-9)
eq("plane 1/sqrt3 + sqrt3", 1 / sqrt(3) + sqrt(3), 4 / sqrt(3))
eq("plane dot product", vx2 * cos(radians(30)) + vy2 * sin(radians(30)), 0, 1e-9)

# spot the error
eq("spot sin2t", 30 * g / 400, 0.75)
eq("spot 2theta", sf(degrees(asin(0.75)), 3), 48.6)
eq("spot theta1", sf(degrees(asin(0.75)) / 2, 3), 24.3)
eq("spot 2theta 2", sf(180 - degrees(asin(0.75)), 4), 131.4)
eq("spot theta2", sf((180 - degrees(asin(0.75))) / 2, 3), 65.7)
eq("spot sum", 24.3 + 65.7, 90)
eq("spot check", 400 * sin(radians(131.4)) / g, 30.0, 0.05)

# start easy
th = atan(5 / 12)
eq("se1 cos", cos(th) * 26, 24); eq("se1 sin", sin(th) * 26, 10); eq("se1 T", 2 * 10 / g, 2)
eq("se2 vy", sf(18 * sin(radians(50)), 4), 13.79, 1e-2)
eq("se2 H", sf((18 * sin(radians(50))) ** 2 / 20, 3), 9.51)
eq("se2 R", sf(324 * sin(radians(100)) / g, 3), 31.9)
eq("se3 t", sqrt(45 / 5), 3); eq("se3 x", 12 * 3, 36)
eq("se4 v", sf(sqrt(144 + 900), 3), 32.3); eq("se4 angle", sf(degrees(atan(30 / 12)), 3), 68.2)
eq("se5 v2", 225 + 40, 265); eq("se5 v", sf(sqrt(265), 3), 16.3)
eq("se6 t", 40 * 0.5 / 10, 2); eq("se6 x", sf(40 * cos(radians(30)) * 2, 3), 69.3)
eq("se6 half range", 40 ** 2 * sin(radians(60)) / g / 2, 40 * cos(radians(30)) * 2, 1e-9)
eq("se7 sin2t", 400 / 625, 0.64)
eq("se7 2t", sf(degrees(asin(0.64)), 3), 39.8); eq("se7 t", sf(degrees(asin(0.64)) / 2, 3), 19.9)
eq("se7 t2", sf(90 - degrees(asin(0.64)) / 2, 3), 70.1)
eq("se8", 1000 / 6, 1000 / 6); eq("se8 V", sf(sqrt(1000 / 6), 3), 12.9)
eq("se8 check", 10 * 1 - 10 * 100 / (2 * (1000 / 6) * 0.5), 4, 1e-9)
eq("se9 t", 2.4 / 8, 0.3); eq("se9 drop", 5 * 0.3 ** 2, 0.45)
eq("se10 vx", sf(22 * cos(radians(30)), 3), 19.1)

# exam practice
eq("q1 vy", 16 * sin(radians(30)), 8); eq("q1 H", 64 / 20, 3.2); eq("q1 T", 2 * 8 / g, 1.6)
eq("q2 t", sqrt(80 / 5), 4); eq("q2 vy", 10 * 4, 40); eq("q2 v2", 15 ** 2 + 40 ** 2, 1825)
eq("q2 v", sf(sqrt(1825), 3), 42.7)
V2 = 12 * 1440 / 4 - 0  # placeholder to keep names unique
eq("q3 V2", 1440 / 4, 360); eq("q3 V", sf(sqrt(360), 3), 19.0)
eq("q3 passes", traj(sqrt(360), radians(45), 12), 8, 1e-9)
a = g * 144 / (2 * 400)
eq("q4 a", a, 1.8); eq("q4 b", 12, 12); eq("q4 c", 4 + a, 5.8)
D = 144 - 4 * 1.8 * 5.8
eq("q4 disc", D, 102.24, 1e-9)
Ta = (12 + sqrt(D)) / 3.6; Tb = (12 - sqrt(D)) / 3.6
eq("q4 Ta", sf(Ta, 4), 6.142, 1e-3); eq("q4 Tb", sf(Tb, 4), 0.5246, 1e-4)
eq("q4 th a", sf(degrees(atan(Ta)), 3), 80.8); eq("q4 th b", sf(degrees(atan(Tb)), 3), 27.7)
for T in (Ta, Tb):
    eq("q4 passes", traj(20, atan(T), 12), 4, 1e-9)
# q5: wall at 24 m, horizontal at 7.2 m
T = 4 * 7.2 / 48
eq("q5 tan", T, 0.6)
th = atan(T)
eq("q5 th", sf(degrees(th), 3), 31.0)
eq("q5 sin2t", sf(2 * T / (1 + T * T), 4), 0.8824, 1e-4)
V = sqrt(g * 48 / sin(2 * th))
eq("q5 V2", sf(V * V, 3), 544); eq("q5 V", sf(V, 3), 23.3)
eq("q5 H", (V * sin(th)) ** 2 / (2 * g), 7.2, 1e-9)
eq("q5 half range", V * cos(th) * V * sin(th) / g, 24, 1e-9)
eq("q5 ratio", T, 4 * ((V * sin(th)) ** 2 / (2 * g)) / (V * V * sin(2 * th) / g), 1e-9)
# q6 golfer: V = 30, tree 9 m high at 45 m
a = g * 45 ** 2 / (2 * 30 ** 2)
eq("q6 a", a, 11.25)
eq("q6 quad", 11.25 / 2.25, 5); eq("q6 quad b", 45 / 2.25, 20); eq("q6 quad c", 20.25 / 2.25, 9)
eq("q6 c", 9 + a, 20.25)
T1 = (20 + sqrt(220)) / 10; T2 = (20 - sqrt(220)) / 10
eq("q6 disc", 400 - 4 * 5 * 9, 220)
eq("q6 sum", T1 + T2, 4); eq("q6 prod", T1 * T2, 9 / 5)
eq("q6 T1", sf(T1, 4), 3.483, 1e-3); eq("q6 T2", sf(T2, 4), 0.5168, 1e-4)
eq("q6 th1", sf(degrees(atan(T1)), 3), 74.0); eq("q6 th2", sf(degrees(atan(T2)), 3), 27.3)
for T in (T1, T2):
    eq("q6 passes", traj(30, atan(T), 45), 9, 1e-9)
eq("q6 R1 sin", sf(2 * T1 / (1 + T1 ** 2), 4), 0.5305, 1e-4)
eq("q6 R2 sin", sf(2 * T2 / (1 + T2 ** 2), 4), 0.8157, 1e-4)
eq("q6 R1", sf(90 * 2 * T1 / (1 + T1 ** 2), 3), 47.7)
eq("q6 R2", sf(90 * 2 * T2 / (1 + T2 ** 2), 3), 73.4)
eq("q6 R1 direct", sf(30 ** 2 * sin(2 * atan(T1)) / g, 3), 47.7)
assert 45 < 90 * 2 * T1 / (1 + T1 ** 2)
assert traj(30, atan(1.0), 45) > 9 and traj(30, atan(0.3), 45) < 9 and traj(30, atan(4.0), 45) < 9
eq("q6 eq", 5 * T1 ** 2 - 20 * T1 + 9, 0, 1e-9)
# q7: plane 45 below horizontal
t = 8 / 5
eq("q7 t", t, 1.6); eq("q7 x", 8 * t, 12.8)
eq("q7 on plane", -5 * t * t, -8 * t, 1e-9)
eq("q7 dist", sf(12.8 / cos(radians(45)), 3), 18.1)
eq("q7 v", sf(sqrt(320), 3), 17.9); eq("q7 vy", -10 * t, -16)
eq("q7 angle", sf(degrees(atan(2)), 3), 63.4); eq("q7 between", sf(degrees(atan(2)) - 45, 3), 18.4)

# stretch
for V_, th_ in ((30, 0.8), (17, 1.2)):
    H = (V_ * sin(th_)) ** 2 / (2 * g); R = V_ * V_ * sin(2 * th_) / g
    eq("tan = 4H/R", tan(th_), 4 * H / R, 1e-9)
eq("s1 angle", sf(degrees(atan(4)), 3), 76.0)
eq("s2 t net", sqrt(1.6 / 5), 0.5657, 1e-4); eq("s2 vmin", sf(12 / sqrt(0.32), 3), 21.2)
eq("s2 t land", sqrt(2.5 / 5), 0.7071, 1e-4); eq("s2 vmax", sf(18.4 / sqrt(0.5), 3), 26.0)
eq("s2 drop", 2.5 - 0.9, 1.6)

# quiz
eq("quiz complement", 90 - 30, 60)
eq("quiz sin", sin(radians(60)), sin(radians(120)))

print("ok")
