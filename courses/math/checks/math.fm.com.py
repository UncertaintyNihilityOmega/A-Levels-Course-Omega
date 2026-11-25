# checks/math.fm.com.py: recomputes every number in Centres of mass (9231 Paper 3).
# Standard library only. Exact values with Fraction; the MF19 results are confirmed by numerical integration.
from fractions import Fraction as F
from math import sqrt, sin, cos, tan, atan, atan2, radians, degrees, isclose, pi

g = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def cm(parts):
    """parts: list of (mass, x, y); returns (x, y) of the centre of mass."""
    M = sum(p[0] for p in parts)
    return sum(p[0] * p[1] for p in parts) / M, sum(p[0] * p[2] for p in parts) / M


# warm-up
eq("w1", sf(20 * sin(radians(60)), 3), 17.3)
eq("w2", 0.5 * 16 * 1.5, 12)
eq("w3", sf(degrees(atan(0.75)), 3), 36.9)

# MF19 results by integration (these back every "given" value quoted in the chapter)
# cone: thin discs, radius proportional to the distance from the vertex
for h in (9.0, 20.0):
    eq("cone 3h/4", simpson(lambda y: y ** 3, 0, h) / simpson(lambda y: y ** 2, 0, h), 0.75 * h, 1e-6)
eq("cone proof", (1 / 4) / (1 / 3), 3 / 4)
# solid hemisphere: discs radius sqrt(r^2 - y^2) at height y from the centre of the plane face
for r in (4.0, 8.0):
    eq("hemisphere 3r/8", simpson(lambda y: y * (r * r - y * y), 0, r) / simpson(lambda y: r * r - y * y, 0, r), 3 * r / 8, 1e-6)
# hemispherical shell: surface element proportional to dy
for r in (3.0, 5.0):
    eq("shell r/2", simpson(lambda y: y, 0, r) / simpson(lambda y: 1.0, 0, r), r / 2, 1e-6)
# arc, angle 2 alpha: mean of r cos t over [-alpha, alpha]
for r, al in ((9.0, pi / 3), (5.0, 0.9)):
    num = simpson(lambda t: r * cos(t), -al, al, 20000) / (2 * al)
    eq("arc r sin a / a", num, r * sin(al) / al, 1e-6)
# sector: mean of the distance (2/3) r cos t weighted by r^2 dt / 2
for r, al in ((6.0, pi / 2), (4.0, pi / 4)):
    num = simpson(lambda t: (2 / 3) * r * cos(t) * 0.5 * r * r, -al, al, 20000) / simpson(lambda t: 0.5 * r * r, -al, al, 20000)
    eq("sector 2 r sin a/(3a)", num, 2 * r * sin(al) / (3 * al), 1e-6)
# semicircle (sector alpha = pi/2): 4r/(3 pi); semicircular arc: 2r/pi
for r in (3.0, 6.0, 10.0):
    eq("semicircle", 2 * r * sin(pi / 2) / (3 * pi / 2), 4 * r / (3 * pi))
    eq("semi arc", r * sin(pi / 2) / (pi / 2), 2 * r / pi)
    # direct integration of the lamina
    eq("semi direct", simpson(lambda x: x * 2 * sqrt(r * r - x * x), 0, r, 200000) / (pi * r * r / 2), 4 * r / (3 * pi), 1e-4)
eq("semicircle 6", sf(8 / pi, 3), 2.55)
eq("semicircle 6 form", 2 * 6 * 1 / (3 * pi / 2), 8 / pi)

# moments eg
total = -10 * 1 + 6 * 3 + 12 * sin(radians(30)) * 4
eq("moments", total, 32)
eq("12 sin30", 12 * sin(radians(30)), 6)

# particles
x, y = cm([(2, 1, 0), (3, 4, 2), (5, -1, 3)])
eq("p x", x, 0.9); eq("p y", y, 2.1)
eq("rod", sf(42 / 11, 3), 3.82)
eq("rod table", 2 * 0 + 4 * 3 + 5 * 6, 42)
eq("rod total", 2 + 4 + 5, 11)

# triangle lamina by mean of vertices and by integration
V = [(0, 0), (9, 0), (3, 6)]
eq("tri x", sum(v[0] for v in V) / 3, 4); eq("tri y", sum(v[1] for v in V) / 3, 2)
eq("tri third of height", 6 / 3, 2)
# numerical check of the centroid by horizontal strips
def tri_centroid(V, n=4000):
    ys = [v[1] for v in V]
    y0, y1 = min(ys), max(ys)
    A = X = Y = 0.0
    for i in range(n):
        yy = y0 + (i + 0.5) * (y1 - y0) / n
        xs = []
        for a in range(3):
            p, q = V[a], V[(a + 1) % 3]
            if (p[1] - yy) * (q[1] - yy) < 0:
                xs.append(p[0] + (yy - p[1]) * (q[0] - p[0]) / (q[1] - p[1]))
        w = (max(xs) - min(xs)); d = (y1 - y0) / n
        A += w * d; X += w * d * (max(xs) + min(xs)) / 2; Y += w * d * yy
    return X / A, Y / A
cx, cy = tri_centroid(V)
eq("tri numeric", cx, 4, 1e-3); eq("tri numeric y", cy, 2, 1e-3)

# L with equal arms
x, y = cm([(12, 3, 1), (8, 1, 4)])
eq("L eq x", x, 2.2); eq("L eq y", y, 2.2)
eq("L eq 44", 12 * 3 + 8 * 1, 44); eq("L eq 44 y", 12 * 1 + 8 * 4, 44)

# L (exam style)
x, y = cm([(F(24), F(4), F(3, 2)), (F(12), F(3, 2), F(5))])
eq("L x", float(x), 19 / 6); eq("L y", float(y), 8 / 3)
eq("L x 3sf", sf(float(x), 3), 3.17); eq("L y 3sf", sf(float(y), 3), 2.67)
eq("L x num", 24 * 4 + 12 * 1.5, 114); eq("L y num", 24 * 1.5 + 12 * 5, 96)
eq("L areas", 8 * 3, 24); eq("L areas 2", 3 * 4, 12)
# G on the line G1 G2: (4,1.5), (1.5,5)
cross = (1.5 - 4) * (float(y) - 1.5) - (5 - 1.5) * (float(x) - 4)
eq("G on G1G2", cross, 0, 1e-9)
# figure coordinates (scale 22, origin 40, 200)
eq("fig G x", round(40 + 22 * float(x), 1), 109.7, 0.05); eq("fig G y", round(200 - 22 * float(y), 1), 141.3, 0.05)

# square with a circular hole
xb = (500 - 12 * pi) / (100 - 4 * pi)
eq("hole x", sf(xb, 3), 5.29)
eq("hole nums", sf(500 - 12 * pi, 4), 462.3, 0.05); eq("hole den", sf(100 - 4 * pi, 4), 87.43, 0.01)
x, y = cm([(100, 5, 5), (-4 * pi, 3, 3)])
eq("hole cm", x, xb); eq("hole sym", y, x)
# numerical check by sampling the lamina
def sample_cm(inside, xs, ys, n=1000):
    sx = sy = c = 0
    for i in range(n):
        for j in range(n):
            px = xs[0] + (i + 0.5) * (xs[1] - xs[0]) / n; py = ys[0] + (j + 0.5) * (ys[1] - ys[0]) / n
            if inside(px, py):
                sx += px; sy += py; c += 1
    return sx / c, sy / c
sx, sy = sample_cm(lambda a, b: (a - 3) ** 2 + (b - 3) ** 2 > 4, (0, 10), (0, 10), 800)
eq("hole sample", sx, xb, 0.02)

# semicircle + rectangle
sem = 4.5 * pi
cen = 4 / pi
xx = (30 * -2.5 + sem * cen) / (30 + sem)
eq("semi+rect", sf(xx, 3), -1.29)
eq("semi area", sf(sem, 4), 14.14, 0.01); eq("semi centre", sf(cen, 4), 1.273, 1e-3)
eq("semi 18", sem * cen, 18); eq("semi den", sf(30 + sem, 4), 44.14, 0.01)

# cone + hemisphere
Vc = F(1, 3) * 36 * 9; Vh = F(2, 3) * 216
eq("cone vol", float(Vc), 108); eq("hemi vol", float(Vh), 144)
x = (Vc * F(9, 4) + Vh * (-F(9, 4))) / (Vc + Vh)
eq("cone+hemi", float(x), -9 / 28 + 0.0, 1e-12) if False else None
eq("cone+hemi x", sf(float(x), 3), -0.321)
eq("cone+hemi 2.25", 9 / 4, 2.25); eq("hemi dist", 3 * 6 / 8, 2.25)
# general: G in the plane iff h = sqrt(3) r
for r in (2.0, 6.0):
    h = sqrt(3) * r
    eq("h sqrt3", (h ** 2 / 12) - r ** 2 / 4, 0, 1e-9)
    eq("h moments", (pi * r * r * h / 3) * (h / 4) - (2 * pi * r ** 3 / 3) * (3 * r / 8), 0, 1e-9)
eq("r=6 h", sf(sqrt(3) * 6, 3), 10.4)
# cone with hemisphere removed
Vc = F(1024, 3); Vh = F(128, 3)
eq("cone V", float(Vc), 1024 / 3); eq("hemi V", float(Vh), 128 / 3)
eq("rem V", float(Vc - Vh), 896 / 3)
x = (Vc * 4 - Vh * F(3, 2)) / (Vc - Vh)
eq("removed x", float(x), 61 / 14); eq("removed x frac", float((4096 - 192) / F(896)), 61 / 14)
eq("removed 3sf", sf(float(x), 3), 4.36)
eq("3904/896", 3904 / 896, 61 / 14)
eq("hemi dist 1.5", 3 * 4 / 8, 1.5)
# numerical check: solid of revolution, cone radius 8 height 16, hemisphere radius 4 removed at the base
def cone_r(z): return 8 * (1 - z / 16)
def hole_r2(z): return 16 - z * z if z < 4 else 0
num = simpson(lambda z: z * pi * (cone_r(z) ** 2 - hole_r2(z)), 0, 16, 200000)
den = simpson(lambda z: pi * (cone_r(z) ** 2 - hole_r2(z)), 0, 16, 200000)
eq("removed numeric", num / den, 61 / 14, 1e-4)

# cylinder + hemisphere
def cylhemi(r, h):
    Vc, Vh = r * r * h, F(2, 3) * r ** 3
    return (Vc * F(h, 2) + Vh * (h + F(3, 8) * r)) / (Vc + Vh)
for r, h in ((5, 8), (3, 7), (10, 4)):
    eq("cyl+hemi formula", float(cylhemi(F(r), F(h))), float(F(6 * h * h + 8 * r * h + 3 * r * r, 4 * (3 * h + 2 * r))), 1e-12)
eq("cyl+hemi 779/136", 6 * 64 + 8 * 40 + 3 * 25, 779); eq("136", 4 * (24 + 10), 136)
eq("cyl+hemi x", sf(779 / 136, 4), 5.728, 1e-3)
eq("cyl+hemi theta", sf(degrees(atan(5 / (779 / 136))), 3), 41.1)
eq("cyl+hemi tan", sf(5 / (779 / 136), 4), 0.8729, 1e-4)
assert 4 < 779 / 136 < 9.875
eq("hemi centre", 8 + 3 * 5 / 8, 9.875)
# numeric check of the solid
num = simpson(lambda z: z * pi * 25, 0, 8) + simpson(lambda z: z * pi * (25 - (z - 8) ** 2), 8, 13)
den = simpson(lambda z: pi * 25, 0, 8) + simpson(lambda z: pi * (25 - (z - 8) ** 2), 8, 13)
eq("cyl+hemi numeric", num / den, 779 / 136, 1e-4)

# wire frameworks
x, y = cm([(3, 0, F(3, 2)), (4, 2, 0), (5, 2, F(3, 2))])
eq("wire x", float(x), 1.5); eq("wire y", float(y), 1.0)
eq("lamina tri", (0 + 4 + 0) / 3, 4 / 3)
yw = 20 / (pi + 2)
eq("arc+diam", sf(yw, 3), 3.89)
eq("arc+diam form", (10 * pi * 20 / pi) / (10 * pi + 20), yw)
eq("arc numeric", simpson(lambda t: 10 * sin(t) * 10, 0, pi) / (10 * pi) , 20 / pi, 1e-6)

# suspended L
th = atan(F(19, 6) / F(8, 3) if False else (19 / 6) / (8 / 3))
eq("susp tan", (19 / 6) / (8 / 3), 19 / 16)
eq("susp theta", sf(degrees(th), 3), 49.9)
# figure: rotate so that AG is vertical, check the plotted vertices
G = (19 / 6, 8 / 3)
ang = atan2(G[1], G[0]); rot = -pi / 2 - ang
def Q(x, y):
    u = x * cos(rot) - y * sin(rot); v = x * sin(rot) + y * cos(rot)
    return round(150 + 22 * u, 1), round(40 - 22 * v, 1)
for name, p, want in (("B", (8, 0), (36.6, 174.6)), ("C", (8, 3), (87.1, 217.1)), ("D", (3, 3), (158.0, 133.0)), ("E", (3, 7), (225.3, 189.7)), ("F", (0, 7), (267.8, 139.2)), ("G", G, (150.0, 131.1))):
    q = Q(*p)
    eq("fig " + name + " x", q[0], want[0], 0.05); eq("fig " + name + " y", q[1], want[1], 0.05)
# the angle between AF and the vertical in the figure is theta
dx, dy = 267.8 - 150, 139.2 - 40
eq("fig theta", sf(degrees(atan(dx / dy)), 3), 49.9)
# arc end point of the theta mark: radius 40 from A in the direction of AF
n = sqrt(dx * dx + dy * dy)
eq("fig arc x", round(150 + 40 * dx / n, 1), 180.6, 0.05); eq("fig arc y", round(40 + 40 * dy / n, 1), 65.8, 0.05)

# spot the error
eq("spot cone", F(1, 3) * 16 * 12, 64); eq("spot cyl", 16 * 6, 96)
eq("spot wrong", (64 * 9 - 96 * 3) / 160, 1.8); eq("spot wrong num", 576 - 288, 288)
eq("spot right", (64 * 3 - 96 * 3) / 160, -0.6); eq("spot right num", 64 * 3 - 96 * 3, -96)
eq("spot quarter", 12 / 4, 3)

# start easy
eq("se1", (0 + 8 + 35) / 10, 4.3)
eq("se2", sf(15 * sin(radians(40)) * 2, 3), 19.3)
V = [(1, 2), (7, 2), (4, 8)]
eq("se3 x", sum(v[0] for v in V) / 3, 4); eq("se3 y", sum(v[1] for v in V) / 3, 4)
eq("se4", 3 * 8 / 8, 3)
eq("se5 vertex", 0.75 * 20, 15); eq("se5 base", 0.25 * 20, 5)
al = pi / 3
eq("se6", sf(9 * sin(al) / al, 3), 7.44); eq("se6 2a", 2 * al, 2 * pi / 3)
x, y = cm([(24, 3, 2), (-4, 5, 3)])
eq("se7 x", x, 2.6); eq("se7 y", y, 1.8)
x, y = cm([(24, 0, 2), (9, 0, 5)])
eq("se8", sf(y, 3), 2.82); eq("se8 num", 48 + 45, 93)
eq("se9", 3 * 12 / 4, 9)
eq("se10", 1 / (2 * sqrt(3)), sqrt(3) / 6)
assert isclose((sqrt(3) / 2) / 3, sqrt(3) / 6)

# exam practice
x, y = cm([(1, 0, 0), (2, 4, 3), (5, -2, 5)])
eq("q1 x", x, -0.25); eq("q1 y", y, 3.875)
eq("q2", sf(15 * sin(radians(40)) * 2.4, 3), 23.1)
x, y = cm([(36, 4.5, 2), (-6, 7.5, 3)])
eq("q3 x", x, 3.9); eq("q3 y", y, 1.8); eq("q3 xnum", 36 * 4.5 - 6 * 7.5, 117); eq("q3 ynum", 72 - 18, 54)
sx, sy = sample_cm(lambda a, b: not (a > 6 and b > 2), (0, 9), (0, 4), 1000)
eq("q3 sample", sx, 3.9, 0.02); eq("q3 sample y", sy, 1.8, 0.02)
eq("q4 xbar", (36 * 2 + 18 * 5.5) / 54, 171 / 54); eq("q4 3sf", sf(171 / 54, 3), 3.17); eq("q4 cone", 4 + 6 / 4, 5.5)
eq("q4 vols", 9 * 4, 36); eq("q4 cone vol", 9 * 6 / 3, 18)
# q5 semicircle on rectangle
d = 16 / (3 * pi)
eq("q5 d", sf(d, 4), 1.698, 1e-3)
yy = (40 * 2.5 + 8 * pi * (5 + d)) / (40 + 8 * pi)
eq("q5", sf(yy, 3), 4.12)
eq("q5 num", sf(40 * 2.5 + 8 * pi * (5 + d), 4), 268.3, 0.05); eq("q5 den", sf(40 + 8 * pi, 4), 65.13, 0.01)
eq("q5 6.698", sf(5 + d, 4), 6.698, 1e-3); eq("q5 168.3", sf(8 * pi * (5 + d), 4), 168.3, 0.05)
# q6 square + triangle
eq("q6 y", (36 * 3 + 12 * (6 + 4 / 3)) / 48, 49 / 12); eq("q6 y 3sf", sf(49 / 12, 3), 4.08)
eq("q6 196", 36 * 3 + 12 * (22 / 3), 196)
eq("q6 tan", 3 / (49 / 12), 36 / 49); eq("q6 th", sf(degrees(atan(36 / 49)), 3), 36.3)
sx, sy = sample_cm(lambda a, b: (b <= 6 and 0 <= a <= 6) or (b > 6 and b <= 10 and abs(a - 3) <= 3 * (10 - b) / 4), (0, 6), (0, 10), 1000)
eq("q6 sample", sy, 49 / 12, 0.02)
# q7 wire hanging from A
yb = 30 / (pi + 2)
eq("q7 y", sf(yb, 3), 5.83); eq("q7 form", 450 / (15 * pi + 30), yb)
eq("q7 arc", sf(30 / pi, 4), 9.549, 1e-3)
eq("q7 phi", sf(degrees(atan(yb / 15)), 3), 21.3); eq("q7 tan", sf(yb / 15, 4), 0.3889, 1e-4)
eq("q7 length", 15 * pi + 30, 15 * pi + 30)

# stretch
r = 10.0; h = r / sqrt(2)
eq("s1 h", sf(h, 3), 7.07)
eq("s1 moments", pi * r * r * h * h / 2 - (2 / 3) * pi * r ** 3 * 3 * r / 8, 0, 1e-9)
eq("s1 h2", h * h, r * r / 2)
a = 1.0
xbar = (4 * pi * a * a * 0 - pi * a * a * a) / (3 * pi * a * a)
eq("s2 x", xbar, -a / 3)
eq("s2 tan", (a / 3) / (2 * a), 1 / 6); eq("s2 theta", sf(degrees(atan(1 / 6)), 3), 9.46)
sx, sy = sample_cm(lambda p, q: p * p + q * q <= 4 and (p - 1) ** 2 + q * q > 1, (-2, 2), (-2, 2), 1000)
eq("s2 sample", sx, -1 / 3, 0.02)

print("ok")
