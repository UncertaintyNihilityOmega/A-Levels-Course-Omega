# checks/math.fm.vectors2.py: recomputes every number in "Vectors: intersections, angles and distances".
# Standard library only; exact work with Fraction.
from fractions import Fraction as F
from math import sqrt, acos, asin, atan, degrees, isclose
from itertools import product
import random


def eq(label, got, want, tol=1e-9):
    assert isclose(float(got), float(want), rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def same(label, got, want):
    assert tuple(got) == tuple(want), f"{label}: computed {tuple(got)}, chapter says {tuple(want)}"


def sf(x, n=3):
    return float(f"{float(x):.{n}g}")


def d1(x):
    return round(float(x) + 0.0, 1)


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def mul(k, u):
    return tuple(k * a for a in u)


def n2(u):
    return dot(u, u)


def mag(u):
    return sqrt(n2(u))


def on_line(a, b, t):
    return add(a, mul(t, b))


def line_plane_t(a, b, n, d):
    """parameter t at which a + t b meets n.r = d (b.n != 0)"""
    return F(d - dot(n, a), dot(n, b))


def ang_line_plane(b, n):
    return degrees(asin(abs(dot(b, n)) / (mag(b) * mag(n))))


def ang_planes(n1, n2):
    return degrees(acos(abs(dot(n1, n2)) / (mag(n1) * mag(n2))))


def pt_plane(P, n, d):
    return abs(dot(n, P) - d) / mag(n)


def skew(a1, b1, a2, b2):
    c = cross(b1, b2)
    return abs(dot(sub(a2, a1), c)) / mag(c)


def pt_line(P, a, b):
    return mag(cross(sub(P, a), b)) / mag(b)


# ---------- warm-up ----------
same("w1", cross((1, 2, 3), (2, 0, 1)), (2, 5, -4))
eq("w2", 2 * 1 - 0 + 3 * 2, 8)
eq("w3 dot", dot((1, 2, 2), (2, 2, 3)), 12)
eq("w3 |b2|^2", n2((2, 2, 3)), 17)
eq("w3 cos", sf(12 / (3 * sqrt(17)), 3), 0.970)
eq("w3 angle", d1(degrees(acos(12 / (3 * sqrt(17))))), 14.0)

# ---------- line and plane ----------
a, b = (1, 0, 2), (2, 1, -1)
n, d = (3, 1, -2), 8
t = line_plane_t(a, b, n, d)
eq("eg1 t", t, 1)
same("eg1 pt", on_line(a, b, t), (3, 1, 1))
eq("eg1 expand", 3 + 1 - 4 + 0, 0)  # 9t - 1 = 8 : constant -1
eq("eg1 coeffs", 6 + 1 + 2, 9)
eq("eg1 const", 3 - 4, -1)
eq("eg1 check", 9 + 1 - 2, 8)
eq("eg1 b.n", dot(b, n), 9)
# parallel / in plane
n = (1, 1, 3)
eq("eg2 b.n", dot(b, n), 0)
eq("eg2 a.n", dot(n, a), 7)
for tt in range(-4, 5):
    assert dot(n, on_line(a, b, tt)) == 7
eq("eg2 (1+2t)+t+3(2-t) const", 1 + 6, 7)
# exam eg
a, b = (2, 0, -1), (1, 2, -1)
n, d = (1, -2, 3), 5
t = line_plane_t(a, b, n, d)
eq("ex1 t", t, -1)
same("ex1 pt", on_line(a, b, t), (1, -2, 0))
eq("ex1 const", 2 - 3, -1)
eq("ex1 t coeff", 1 - 4 - 3, -6)
eq("ex1 b.n", dot(b, n), -6)
eq("ex1 |b|^2", n2(b), 6)
eq("ex1 |n|^2", n2(n), 14)
eq("ex1 sin", sf(6 / (sqrt(6) * sqrt(14)), 4), 0.6547)
eq("ex1 angle", d1(ang_line_plane(b, n)), 40.9)

# ---------- derivation of the distance formula (random check) ----------
rnd = random.Random(11)
for _ in range(200):
    P = tuple(rnd.randint(-9, 9) for _ in range(3))
    nn = tuple(rnd.randint(-5, 5) for _ in range(3))
    if n2(nn) == 0:
        continue
    dd = rnd.randint(-20, 20)
    t = F(dd - dot(nn, P), n2(nn))
    Fp = tuple(p + t * q for p, q in zip(P, nn))
    assert dot(nn, Fp) == dd
    assert abs(float(abs(t)) * mag(nn) - abs(dot(nn, P) - dd) / mag(nn)) < 1e-9

# ---------- foot, distance, reflection ----------
P, n, d = (3, -1, 4), (2, 3, -1), -8
t = F(d - dot(n, P), n2(n))
eq("eg3 t", t, -0.5)
Fp = tuple(p + t * q for p, q in zip(P, n))
same("eg3 F", Fp, (2, F(-5, 2), F(9, 2)))
eq("eg3 expand const", 6 - 3 - 4, -1)
eq("eg3 coeff", 4 + 9 + 1, 14)
eq("eg3 dist", sf(0.5 * sqrt(14), 3), 1.87)
eq("eg3 formula num", 6 - 3 - 4 + 8, 7)
eq("eg3 formula", sf(7 / sqrt(14), 3), 1.87)
img = tuple(p + 2 * t * q for p, q in zip(P, n))
same("eg3 image", img, (1, -4, 5))
same("eg3 midpoint", tuple(F(x + y, 2) for x, y in zip(P, img)), Fp)
eq("eg3 pt_plane", pt_plane(P, n, d), 7 / sqrt(14))
# parallel planes
eq("eg3b parallel planes", sf(13 / sqrt(14), 3), 3.47)
# drone
D, n, d = (3, 3, 8), (0, -1, 2), 6
eq("eg4 n.D", dot(n, D), 13)
eq("eg4 dist", sf(7 / sqrt(5), 3), 3.13)
t = F(d - dot(n, D), n2(n))
eq("eg4 t", t, -F(7, 5))
Fp = tuple(p + t * q for p, q in zip(D, n))
same("eg4 foot", Fp, (3, F(22, 5), F(26, 5)))
eq("eg4 foot 4.4", Fp[1], 4.4)
eq("eg4 foot 5.2", Fp[2], 5.2)
eq("eg4 check", 2 * 5.2 - 4.4, 6)
eq("eg4 subst", -(3) + 16, 13)
# exam eg: foot of A
A, n, d = (-1, 3, -2), (2, -1, 2), 9
t = F(d - dot(n, A), n2(n))
eq("ex2 t", t, 2)
eq("ex2 expand", 2 * (-1) - 3 + 2 * (-2), -9)
Fp = tuple(p + t * q for p, q in zip(A, n))
same("ex2 F", Fp, (3, 1, 2))
eq("ex2 dist", abs(t) * mag(n), 6)
img = tuple(2 * f - p for f, p in zip(Fp, A))
same("ex2 image", img, (7, -1, 6))
eq("ex2 image in plane check A' dist", pt_plane(img, n, d), 6)

# ---------- angle line / plane ----------
b, n = (2, 1, -1), (3, 1, -2)
eq("eg5 b.n", dot(b, n), 9)
eq("eg5 sin", sf(9 / (sqrt(6) * sqrt(14)), 4), 0.9820)
eq("eg5 angle", d1(ang_line_plane(b, n)), 79.1)
eq("eg5 cos wrong", d1(degrees(acos(9 / (sqrt(6) * sqrt(14))))), 10.9)
eq("eg5 complement", d1(90 - ang_line_plane(b, n)), 10.9)
# the figure: theta + phi = 90
phi = 40
eq("fig theta", 90 - phi, 50)

# ---------- angle planes ----------
n1, n2_ = (2, 3, -1), (1, -1, 2)
eq("eg6 dot", dot(n1, n2_), -3)
eq("eg6 cos", sf(3 / sqrt(14 * 6), 4), 0.3273)
eq("eg6 angle", d1(ang_planes(n1, n2_)), 70.9)
eq("eg6 obtuse", d1(degrees(acos(-3 / sqrt(14 * 6)))), 109.1)
eq("eg7 cos", sf(2 / sqrt(5), 4), 0.8944)
eq("eg7 angle", d1(ang_planes((0, -1, 2), (0, 0, 1))), 26.6)
eq("eg7 atan", d1(degrees(atan(0.5))), 26.6)

# ---------- line of intersection ----------
n1, n2_ = (1, 2, -2), (2, -1, 1)
dirv = cross(n1, n2_)
same("eg8 dir", dirv, (0, -5, -5))
# point z=0
x, y = 3, 1
eq("eg8 p1", x + 2 * y, 5)
eq("eg8 p2", 2 * x - y, 5)
pt = (3, 1, 0)
for tt in range(-3, 4):
    q = add(pt, mul(tt, (0, 1, 1)))
    assert dot(n1, q) == 5 and dot(n2_, q) == 5
same("eg8 t=1", add(pt, (0, 1, 1)), (3, 2, 1))
eq("eg8 chk1", 3 + 4 - 2, 5)
eq("eg8 chk2", 6 - 2 + 1, 5)
# alternative z = t
for tt in range(-3, 4):
    xx = 3
    yy = 1 + tt
    assert xx + 2 * yy - 2 * tt == 5 and 2 * xx - yy + tt == 5
# closest point to origin for the widget note
tt = F(-1, 2)
q = add(pt, mul(tt, (0, 1, 1)))
same("eg8 closest", q, (3, F(1, 2), F(-1, 2)))
assert dot(q, (0, 1, 1)) == 0
eq("eg8 ang", d1(ang_planes(n1, n2_)), 74.2)
# warn example
n1, n2_ = (1, 2, 1), (2, 4, -1)
dv = cross(n1, n2_)
same("warn dir", dv, (-6, 3, 0))
assert cross(dv, (-2, 1, 0)) == (0, 0, 0)
# z = 0 clashes: x+2y=6 and 2x+4y=9
assert 2 * 6 != 9
y, z = F(5, 2), 1
eq("warn y", (6 + 9) / 6, 2.5)
eq("warn eq1", 2 * y + z, 6)
eq("warn eq2", 4 * y - z, 9)
pt = (0, y, z)
for tt in range(-3, 4):
    q = add(pt, mul(tt, (-2, 1, 0)))
    assert dot(n1, q) == 6 and dot(n2_, q) == 9
# exam eg
n1, n2_ = (2, 1, -1), (1, -1, 2)
eq("ex3 dot", dot(n1, n2_), -1)
eq("ex3 mags", n2(n1) * n2(n2_), 36)
eq("ex3 cos", 1 / 6, 1 / sqrt(6) / sqrt(6))
eq("ex3 angle", d1(ang_planes(n1, n2_)), 80.4)
dv = cross(n1, n2_)
same("ex3 dir", dv, (1, -5, -3))
eq("ex3 x", F(9, 3), 3)
eq("ex3 p1", 2 * 3 + (-2), 4)
eq("ex3 p2", 3 - (-2), 5)
for tt in range(-3, 4):
    q = add((3, -2, 0), mul(tt, dv))
    assert dot(n1, q) == 4 and dot(n2_, q) == 5
same("ex3 t=1", add((3, -2, 0), dv), (4, -7, -3))
eq("ex3 chk1", 8 - 7 + 3, 4)
eq("ex3 chk2", 4 + 7 - 6, 5)

# ---------- skew lines ----------
a1, b1, a2, b2 = (2, 0, 1), (1, 1, 2), (0, 3, 2), (2, -1, 0)
c = cross(b1, b2)
same("eg9 n", c, (2, 4, -3))
same("eg9 a2-a1", sub(a2, a1), (-2, 3, 1))
eq("eg9 dot", dot(sub(a2, a1), c), 5)
eq("eg9 |n|^2", n2(c), 29)
eq("eg9 d", sf(5 / sqrt(29), 3), 0.928)
# prove skew: no intersection
# s, t: 2+s=2t, s=3-t, 1+2s=2
s_ = F(1, 2)
tt = 3 - s_
assert 2 + s_ != 2 * tt
# common perpendicular example
a1, b1, a2, b2 = (0, 1, 2), (1, 2, 2), (1, 2, -1), (2, 2, 3)
c = cross(b1, b2)
same("eg10 n", c, (2, 1, -2))
eq("eg10 |n|", mag(c), 3)
same("eg10 a2-a1", sub(a2, a1), (1, 1, -3))
eq("eg10 dot", dot(sub(a2, a1), c), 9)
eq("eg10 d", skew(a1, b1, a2, b2), 3)
# PQ general
for s_, t_ in [(0, 0), (1, 1), (2, -1), (F(1, 3), F(5, 2))]:
    P = on_line(a1, b1, s_)
    Q = on_line(a2, b2, t_)
    PQ = sub(Q, P)
    same("eg10 PQ form", PQ, (1 + 2 * t_ - s_, 1 + 2 * t_ - 2 * s_, -3 + 3 * t_ - 2 * s_))
    eq("eg10 eq1", dot(PQ, b1), 12 * t_ - 9 * s_ - 3)
    eq("eg10 eq2", dot(PQ, b2), 17 * t_ - 12 * s_ - 5)
# solve 4t - 3s = 1, 17t - 12s = 5
s_ = F(3)
# 4t - 3s = 1 -> t = (1+3s)/4 ; 17(1+3s)/4 - 12 s = 5 -> 17 + 51 s - 48 s = 20 -> s = 1
s_ = F(1)
t_ = (1 + 3 * s_) / 4
assert 17 * t_ - 12 * s_ == 5 and t_ == 1
P = on_line(a1, b1, s_)
Q = on_line(a2, b2, t_)
same("eg10 P", P, (1, 3, 4))
same("eg10 Q", Q, (3, 4, 2))
same("eg10 PQ", sub(Q, P), (2, 1, -2))
eq("eg10 |PQ|", mag(sub(Q, P)), 3)

# ---------- point to line ----------
P, a, b = (4, 0, 5), (1, 0, 2), (1, 2, 2)
same("eg11 AP", sub(P, a), (3, 0, 3))
x = cross(sub(P, a), b)
same("eg11 cross", x, (-6, -3, 6))
eq("eg11 |x|", mag(x), 9)
eq("eg11 d", pt_line(P, a, b), 3)
# foot (2,2,4) from 9709 chapter
foot = (2, 2, 4)
assert dot(sub(foot, P), b) == 0 and foot == on_line(a, b, 1)
eq("eg11 foot dist", mag(sub(P, foot)), 3)
O, a, b = (0, 0, 0), (1, 0, 2), (2, 1, -1)
same("eg11 AO", sub(O, a), (-1, 0, -2))
x = cross(sub(O, a), b)
same("eg11 cross2", x, (2, -5, -1))
eq("eg11 |x|^2", n2(x), 30)
eq("eg11 d2", sf(pt_line(O, a, b), 3), 2.24)
eq("eg11 sqrt5", sqrt(30) / sqrt(6), sqrt(5))

# ---------- unknown k ----------
a1, b1 = (1, 0, 2), (1, 2, 2)
b2 = (2, 2, 3)
c = cross(b1, b2)
same("ex4 n", c, (2, 1, -2))
eq("ex4 |n|", mag(c), 3)
for k in range(-6, 15):
    a2 = (3, 1, k)
    same("ex4 diff", sub(a2, a1), (2, 1, k - 2))
    eq("ex4 dot", dot(sub(a2, a1), c), 9 - 2 * k)
    eq("ex4 dist", skew(a1, b1, a2, b2), abs(9 - 2 * k) / 3)
for k in (-3, 12):
    eq("ex4 k", skew(a1, b1, (3, 1, k), b2), 5)
eq("ex4 k=12", 9 - 24, -15)
eq("ex4 k=-3", 9 + 6, 15)
eq("ex4 meets", skew(a1, b1, (3, 1, F(9, 2)), b2), 0)

# ---------- spot the error ----------
b, n = (1, 2, 2), (2, -1, 2)
eq("spot b.n", dot(b, n), 4)
eq("spot mags", mag(b) * mag(n), 9)
eq("spot wrong", d1(degrees(acos(4 / 9))), 63.6)
eq("spot right", d1(ang_line_plane(b, n)), 26.4)
eq("spot sum", ang_line_plane(b, n) + degrees(acos(4 / 9)), 90)

# ---------- try ----------
a, b, n, d = (1, 1, 0), (1, -1, 2), (2, 1, -1), 6
t = line_plane_t(a, b, n, d)
eq("t1 t", t, -3)
same("t1 pt", on_line(a, b, t), (-2, 4, -6))
eq("t1 const", 2 + 1, 3)
eq("t1 check", -4 + 4 + 6, 6)
a, b, n = (0, 1, 2), (1, 2, -1), (3, -1, 1)
eq("t2 b.n", dot(b, n), 0)
eq("t2 a.n", dot(n, a), 1)
eq("t3 num", 2 - 2 - 6, -6)
eq("t3 d", sf(11 / 3, 3), 3.67)
eq("t3 pt_plane", pt_plane((2, -1, 3), (1, 2, -2), 5), 11 / 3)
P, n, d = (1, 2, 3), (1, 1, 1), 12
t = F(d - dot(n, P), n2(n))
eq("t4 t", t, 2)
same("t4 F", tuple(p + t * q for p, q in zip(P, n)), (3, 4, 5))
eq("t4 dist", sf(2 * sqrt(3), 3), 3.46)
P, n, d = (0, 0, 0), (2, -1, 2), 9
t = F(d - dot(n, P), n2(n))
eq("t5 t", t, 1)
same("t5 foot", tuple(p + t * q for p, q in zip(P, n)), (2, -1, 2))
same("t5 image", tuple(p + 2 * t * q for p, q in zip(P, n)), (4, -2, 4))
eq("t6 angle", d1(ang_line_plane((1, 1, 1), (0, 0, 1))), 35.3)
eq("t7 angle", d1(ang_planes((1, 1, 1), (0, 0, 1))), 54.7)
n1, n2_ = (1, 1, 1), (1, -1, 2)
same("t8 dir", cross(n1, n2_), (3, -1, -2))
pt = (3, 3, 0)
assert dot(n1, pt) == 6 and dot(n2_, pt) == 0
same("t8 t=1", add(pt, (3, -1, -2)), (6, 2, -2))
eq("t8 chk1", 6 + 2 - 2, 6)
eq("t8 chk2", 6 - 2 - 4, 0)
a1, b1, a2, b2 = (1, 2, 3), (1, 0, 1), (0, 1, 1), (1, 1, 0)
c = cross(b1, b2)
same("t9 n", c, (-1, 1, 1))
same("t9 a2-a1", sub(a2, a1), (-1, -1, -2))
eq("t9 dot", dot(sub(a2, a1), c), -2)
eq("t9 d", sf(2 / sqrt(3), 3), 1.15)
P, a, b = (1, 1, 1), (0, 0, 2), (1, 2, 2)
same("t10 AP", sub(P, a), (1, 1, -1))
x = cross(sub(P, a), b)
same("t10 cross", x, (4, -3, 1))
eq("t10 |x|^2", n2(x), 26)
eq("t10 d", sf(sqrt(26) / 3, 3), 1.70)

# ---------- exam practice ----------
a, b, n, d = (3, -1, 2), (-1, 2, 1), (2, 1, -1), 1
t = line_plane_t(a, b, n, d)
eq("e1 t", t, 2)
same("e1 pt", on_line(a, b, t), (1, 3, 4))
eq("e1 const", 6 - 1 - 2, 3)
eq("e1 check", 2 + 3 - 4, 1)
b, n = (1, -2, 2), (2, 3, 6)
eq("e2 b.n", dot(b, n), 8)
eq("e2 |b|,|n|", mag(b) * mag(n), 21)
eq("e2 angle", d1(ang_line_plane(b, n)), 22.4)
P, n, d = (4, -1, 2), (2, 1, 2), 2
t = F(d - dot(n, P), n2(n))
eq("e3 t", t, -1)
eq("e3 const", 8 - 1 + 4, 11)
same("e3 F", tuple(p + t * q for p, q in zip(P, n)), (2, -2, 0))
eq("e3 dist", abs(t) * mag(n), 3)
n1, n2_ = (1, 2, 2), (2, -3, 6)
eq("e4 dot", dot(n1, n2_), 8)
eq("e4 mags", mag(n1) * mag(n2_), 21)
eq("e4 angle", d1(ang_planes(n1, n2_)), 67.6)
assert dot(n1, (1, 1, 2)) == 7 and dot(n2_, (1, 1, 2)) == 11
same("e4 dir", cross(n1, n2_), (18, -2, -7))
for tt in range(-3, 4):
    q = add((1, 1, 2), mul(tt, (18, -2, -7)))
    assert dot(n1, q) == 7 and dot(n2_, q) == 11
a1, b1, a2, b2 = (1, 0, -2), (2, 1, -1), (0, 2, 2), (1, -1, 3)
c = cross(b1, b2)
same("e5 n", c, (2, -7, -3))
same("e5 a2-a1", sub(a2, a1), (-1, 2, 4))
eq("e5 dot", dot(sub(a2, a1), c), -28)
eq("e5 |n|^2", n2(c), 62)
eq("e5 d", sf(28 / sqrt(62), 3), 3.56)
eq("e5 d direct", sf(skew(a1, b1, a2, b2), 3), 3.56)
# e6
A, B, C = (1, 0, 2), (2, 1, 0), (0, 2, 1)
AB, AC = sub(B, A), sub(C, A)
same("e6 AB", AB, (1, 1, -2))
same("e6 AC", AC, (-1, 2, -1))
x = cross(AB, AC)
same("e6 cross", x, (3, 3, 3))
eq("e6 p", dot((1, 1, 1), A), 3)
for Pt in (A, B, C):
    assert sum(Pt) == 3
n1, n2_ = (1, 1, 1), (2, -1, 2)
eq("e6 dot", dot(n1, n2_), 3)
eq("e6 mags", mag(n1) * mag(n2_), 3 * sqrt(3))
eq("e6 cos", 3 / (3 * sqrt(3)), 1 / sqrt(3))
eq("e6 angle", d1(ang_planes(n1, n2_)), 54.7)
dv = cross(n1, n2_)
same("e6 dir", dv, (3, 0, -3))
assert (0, 0, 3) and sum((0, 0, 3)) == 3 and dot(n2_, (0, 0, 3)) == 6
for tt in range(-3, 4):
    q = add((0, 0, 3), mul(tt, (1, 0, -1)))
    assert dot(n1, q) == 3 and dot(n2_, q) == 6
PB = sub(B, (0, 0, 3))
same("e6 PB", PB, (2, 1, -3))
x = cross(PB, (1, 0, -1))
same("e6 PBxd", x, (-1, -1, -1))
eq("e6 d", sf(sqrt(3) / sqrt(2), 3), 1.22)
eq("e6 d direct", pt_line(B, (0, 0, 3), (1, 0, -1)), sqrt(1.5))
# e7
a, b = (1, -1, 2), (1, 2, 1)
eq("e7 a", 3 - 2 + (-1), 0)
n = (3, -1, -1)
eq("e7 b.n", dot(b, n), 0)
eq("e7 |n|^2", n2(n), 11)
eq("e7 n.A", dot(n, a), 2)
for bb in (13, -9):
    eq("e7 b", pt_plane(a, n, bb), sqrt(11))
P, d = a, 13
t = F(d - dot(n, P), n2(n))
eq("e7 t", t, 1)
eq("e7 expand", 3 + 1 - 2, 2)
same("e7 F", tuple(p + t * q for p, q in zip(P, n)), (4, -2, 1))

# ---------- stretch ----------
A, dv, n, d = (5, -3, 10), (-1, 2, -4), (2, -1, 2), 9
t = line_plane_t(A, dv, n, d)
eq("s1 t", t, 2)
eq("s1 expand", 10 + 3 + 20, 33)
eq("s1 coeff", -2 - 2 - 8, -12)
H = on_line(A, dv, t)
same("s1 H", H, (3, 1, 2))
eq("s1 d.n", dot(dv, n), -12)
eq("s1 |n|^2", n2(n), 9)
dp = tuple(F(x) - 2 * F(dot(dv, n), n2(n)) * y for x, y in zip(dv, n))
same("s1 d'", dp, (F(13, 3), F(-2, 3), F(4, 3)))
eq("s1 speed", sum(x * x for x in dp), 21)
eq("s1 |d|^2", n2(dv), 21)
eq("s1 169+4+16", 169 + 4 + 16, 189)
eq("s1 8/3", -2 * (-12) / 9, 8 / 3)
# reflected ray leaves the mirror on the same side, mirror image of A lies on its backward extension
Aim = tuple(F(p) - 2 * F(dot(n, A) - d, n2(n)) * q for p, q in zip(A, n))
assert cross(sub(H, Aim), (13, -2, 4)) == (0, 0, 0)
# s2
n1, d1_ = (1, 2, -2), 3
n2_ = (4, 0, -3)
eq("s2 |n1|", mag(n1), 3)
eq("s2 |n2|", mag(n2_), 5)
pa, pb = (-7, 10, -1), (17, 10, -19)
for _ in range(200):
    P = tuple(F(rnd.randint(-9, 9)) for _ in range(3))
    # plus-sign bisector 5(x+2y-2z-3) = 3(4x-3z): -7x + 10y - z = 15
    lhs = 5 * (P[0] + 2 * P[1] - 2 * P[2] - 3)
    ok_plus = (lhs == 3 * (4 * P[0] - 3 * P[2]))
    assert ok_plus == (dot(pa, P) == 15)
    ok_minus = (lhs == -3 * (4 * P[0] - 3 * P[2]))
    assert ok_minus == (dot(pb, P) == 15)
    if ok_plus or ok_minus:
        assert abs(dot(n1, P) - d1_) * 5 == abs(dot(n2_, P)) * 3
eq("s2 plus", 5 * 1 - 12, -7)
eq("s2 plus y", 5 * 2, 10)
eq("s2 plus z", -10 + 9, -1)
eq("s2 minus x", 5 + 12, 17)
eq("s2 minus z", -10 - 9, -19)
eq("s2 dot", 119 - 100 - 19, 0)
eq("s2 dot direct", dot((7, -10, 1), (17, 10, -19)), 0)
# the intersection point lies on both bisectors
Pt = (0, F(3, 2), 0)
assert dot(n1, Pt) == 3 and dot(n2_, Pt) == 0
assert dot(pa, Pt) == 15 and dot(pb, Pt) == 15

# ---------- quiz ----------
eq("q4 num", 2 - 2 + 6, 6)
eq("q4 d", abs(6 - 3) / 3, 1)
eq("q6 cos", d1(ang_planes((1, 0, 0), (1, 1, 1))), 54.7)
eq("q6 sin wrong", d1(degrees(asin(1 / sqrt(3)))), 35.3)

# ---------- figure geometry (numbers in the SVGs) ----------
from math import sin, cos, radians
phi = radians(40)
X = (170, 150)
top = (X[0] + 130 * cos(phi), X[1] - 130 * sin(phi))
low = (X[0] - 70 * cos(phi), X[1] + 70 * sin(phi))
eq("fig1 top x", top[0], 269.6, 0.05)
eq("fig1 top y", top[1], 66.4, 0.05)
eq("fig1 low x", low[0], 116.4, 0.05)
eq("fig1 low y", low[1], 195.0, 0.05)
eq("fig1 arc phi x", X[0] + 40 * cos(phi), 200.6, 0.05)
eq("fig1 arc phi y", X[1] - 40 * sin(phi), 124.3, 0.05)
th = radians(50)
eq("fig1 arc th x", X[0] + 55 * sin(th), 212.1, 0.05)
eq("fig1 arc th y", X[1] - 55 * cos(th), 114.6, 0.05)

print("ok")
