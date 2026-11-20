# checks/math.fm.vectors.py: recomputes every number in "Vectors: the vector product and planes".
# Standard library only; exact work with Fraction.
from fractions import Fraction as F
from math import sqrt, acos, asin, degrees, isclose, isqrt
from itertools import product


def eq(label, got, want, tol=1e-9):
    assert isclose(float(got), float(want), rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def same(label, got, want):
    assert tuple(got) == tuple(want), f"{label}: computed {tuple(got)}, chapter says {tuple(want)}"


def sf(x, n=3):
    return float(f"{float(x):.{n}g}")


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


def norm2(u):
    return dot(u, u)


def mag(u):
    return sqrt(norm2(u))


def parallel(u, v):
    return cross(u, v) == (0, 0, 0)


def plane_from(n, a):
    """returns (n, p) with r.n = p through a"""
    return n, dot(n, a)


# ---------- warm-up ----------
eq("w1 cos", dot((1, 2, 2), (2, -1, 2)) / (3 * 3), 4 / 9)
eq("w1 angle", sf(degrees(acos(4 / 9)), 3), 63.6)
same("w2 dir", sub((3, -1, 4), (1, 2, 0)), (2, -3, 4))
eq("w3 det", 2 * 4 - (-3) * 1, 11)

# ---------- first worked example and check ----------
a, b = (2, -1, 3), (1, 4, -2)
c = cross(a, b)
same("eg1 axb", c, (-10, 7, 9))
eq("eg1 a.c", dot(c, a), 0)
eq("eg1 b.c", dot(c, b), 0)
same("eg1 b x a", cross(b, a), (10, -7, -9))
eq("eg1 i comp", (-1) * (-2) - 3 * 4, -10)
eq("eg1 j comp", 3 * 1 - 2 * (-2), 7)
eq("eg1 k comp", 2 * 4 - (-1) * 1, 9)
eq("eg1 check 1", -20 - 7 + 27, 0)
eq("eg1 check 2", -10 + 28 - 18, 0)

# ---------- proofs: the algebra checked on random integer vectors ----------
import random
rnd = random.Random(7)
for _ in range(200):
    u = tuple(rnd.randint(-9, 9) for _ in range(3))
    v = tuple(rnd.randint(-9, 9) for _ in range(3))
    w = tuple(rnd.randint(-9, 9) for _ in range(3))
    x = cross(u, v)
    assert dot(u, x) == 0 and dot(v, x) == 0
    assert norm2(x) == norm2(u) * norm2(v) - dot(u, v) ** 2
    assert cross(v, u) == mul(-1, x)
    assert cross(u, add(v, w)) == add(cross(u, v), cross(u, w))
    assert cross(mul(3, u), v) == mul(3, x)
    # the nine-term expansion in the second proof
    a1, a2, a3 = u
    b1, b2, b3 = v
    expanded = (a2 ** 2 * b3 ** 2 + a3 ** 2 * b2 ** 2 + a3 ** 2 * b1 ** 2 + a1 ** 2 * b3 ** 2 + a1 ** 2 * b2 ** 2
                + a2 ** 2 * b1 ** 2 - 2 * a2 * a3 * b2 * b3 - 2 * a1 * a3 * b1 * b3 - 2 * a1 * a2 * b1 * b2)
    assert expanded == norm2(x)
    # six-term cancellation in the first proof
    six = (a1 * a2 * b3 - a1 * a3 * b2 + a2 * a3 * b1 - a1 * a2 * b3 + a1 * a3 * b2 - a2 * a3 * b1)
    assert six == 0
assert cross((1, 0, 0), (0, 1, 0)) == (0, 0, 1) and cross((0, 1, 0), (0, 0, 1)) == (1, 0, 0) and cross((0, 0, 1), (1, 0, 0)) == (0, 1, 0)

# ---------- unit perpendicular and the angle ----------
eq("eg2 |axb|^2", norm2(c), 230)
eq("eg2 |a|^2", norm2(a), 14)
eq("eg2 |b|^2", norm2(b), 21)
sin_t = sqrt(230) / (sqrt(14) * sqrt(21))
eq("eg2 sin", sf(sin_t, 4), 0.8845)
acute = degrees(asin(sin_t))
eq("eg2 acute", sf(acute, 3), 62.2)
eq("eg2 obtuse", sf(180 - acute, 4), 117.8)
eq("eg2 a.b", dot(a, b), -8)
eq("eg2 angle via cos", sf(degrees(acos(-8 / sqrt(14 * 21))), 4), 117.8)

# ---------- areas ----------
A, B, C = (1, 2, 0), (3, 0, 1), (3, 3, 4)
AB, AC = sub(B, A), sub(C, A)
same("eg3 AB", AB, (2, -2, 1))
same("eg3 AC", AC, (2, 1, 4))
x = cross(AB, AC)
same("eg3 cross", x, (-9, -6, 6))
eq("eg3 |x|^2", norm2(x), 153)
assert 153 == 9 * 17
eq("eg3 area", sf(0.5 * sqrt(153), 3), 6.18)
A, B, C = (0, 0, 2), (6, 0, 2), (2, 5, 4)
x = cross(sub(B, A), sub(C, A))
same("eg4 cross", x, (0, -12, 30))
eq("eg4 |x|^2", norm2(x), 1044)
assert 1044 == 36 * 29
eq("eg4 area", sf(0.5 * sqrt(1044), 3), 16.2)
eq("eg4 footprint", 0.5 * 6 * 5, 15)

# ---------- plane through a point with a normal ----------
n, p = plane_from((2, 3, -1), (1, -2, 4))
eq("eg5 p", p, -8)
eq("eg5 A in plane", 2 * 1 + 3 * (-2) - 4, -8)
eq("eg5 scaled", 4 * 1 + 6 * (-2) - 2 * 4, -16)
eq("eg6 P", 2 - 2 + 12, 12)
eq("eg6 Q", 2 + 2 + 4, 8)

# ---------- distance from the origin ----------
eq("eg7 |n|^2", norm2((2, 3, -1)), 14)
eq("eg7 dist", sf(8 / sqrt(14), 3), 2.14)
foot = tuple(F(-8, 14) * k for k in (2, 3, -1))
same("eg7 foot", foot, (F(-8, 7), F(-12, 7), F(4, 7)))
eq("eg7 foot in plane", 2 * foot[0] + 3 * foot[1] - foot[2], -8)

# ---------- parametric to Cartesian ----------
b_, c_ = (1, 2, 0), (0, 1, 3)
n = cross(b_, c_)
same("eg8 n", n, (6, -3, 1))
eq("eg8 p", dot(n, (1, 0, 2)), 8)
eq("eg8 b.n", dot(n, b_), 0)
eq("eg8 c.n", dot(n, c_), 0)
for lam, mu in [(0, 0), (1, 2), (-3, 4), (2, -1)]:
    pt = add(add((1, 0, 2), mul(lam, b_)), mul(mu, c_))
    assert dot(n, pt) == 8
eq("eg8 check b", 6 * 1 - 3 * 2 + 0, 0)
eq("eg8 check c", 6 * 0 - 3 * 1 + 3, 0)

# ---------- Cartesian to parametric ----------
n = (3, -2, 1)
eq("eg9 point", 3 * 2, 6)
bb, cc = (1, 0, -3), (0, 1, 2)
eq("eg9 b.n", dot(bb, n), 0)
eq("eg9 c.n", dot(cc, n), 0)
same("eg9 bxc", cross(bb, cc), (3, -2, 1))
assert not parallel(bb, cc)
b2, c2 = (2, 3, 0), (1, 0, -3)
eq("eg9 alt b", dot(b2, n), 0)
eq("eg9 alt c", dot(c2, n), 0)
eq("eg9 alt point", dot(n, (0, 0, 6)), 6)
assert not parallel(b2, c2)

# ---------- plane through three points (exam example) ----------
A, B, C = (2, 1, -1), (4, 0, 1), (3, 3, 2)
AB, AC = sub(B, A), sub(C, A)
same("eg10 AB", AB, (2, -1, 2))
same("eg10 AC", AC, (1, 2, 3))
n = cross(AB, AC)
same("eg10 n", n, (-7, -4, 5))
eq("eg10 p", dot(n, A), -23)
n2 = mul(-1, n)
eq("eg10 B", dot(n2, B), 23)
eq("eg10 C", dot(n2, C), 23)
eq("eg10 A", dot(n2, A), 23)
eq("eg10 arithmetic", -14 - 4 - 5, -23)
eq("eg10 checkB", 28 + 0 - 5, 23)
eq("eg10 checkC", 21 + 12 - 10, 23)

# ---------- line and point ----------
a0, d = (1, 2, 0), (2, 1, -1)
P = (3, -1, 4)
AP = sub(P, a0)
same("eg11 AP", AP, (2, -3, 4))
n = cross(d, AP)
same("eg11 n", n, (1, -10, -8))
eq("eg11 p", dot(n, a0), -19)
eq("eg11 P", dot(n, P), -19)
eq("eg11 t=1", dot(n, add(a0, d)), -19)
same("eg11 t=1 point", add(a0, d), (3, 3, -1))
eq("eg11 t=1 by hand", 3 - 30 + 8, -19)

# ---------- two intersecting lines ----------
s_, t_ = 1, 2
M_ = add((0, 1, 1), mul(s_, (1, 1, 0)))
same("eg11b M on l1", M_, (1, 2, 1))
same("eg11b M on l2", add((1, 0, -3), mul(t_, (0, 1, 2))), (1, 2, 1))
n = cross((1, 1, 0), (0, 1, 2))
same("eg11b n", n, (2, -2, 1))
eq("eg11b p", dot(n, M_), -1)
eq("eg11b l1 pt", dot(n, (0, 1, 1)), -1)
eq("eg11b l2 pt", dot(n, (1, 0, -3)), -1)
eq("eg11b parallel", dot(n, (1, 1, 1)), 1)

# ---------- perpendicular bisector ----------
A, B = (1, 2, 3), (5, 0, 7)
M = tuple(F(x + y, 2) for x, y in zip(A, B))
same("eg12 M", M, (3, 1, 5))
nn = (2, -1, 2)
assert parallel(sub(B, A), nn)
eq("eg12 AB", 0, 0)
same("eg12 AB vec", sub(B, A), (4, -2, 4))
eq("eg12 p", dot(nn, M), 15)
eq("eg12 A side", dot(nn, A), 6)
eq("eg12 B side", dot(nn, B), 24)
for _ in range(50):
    P = tuple(rnd.randint(-9, 9) for _ in range(3))
    # points of the plane are equidistant from A and B
    if dot(nn, P) == 15:
        assert norm2(sub(P, A)) == norm2(sub(P, B))
# construct plane points explicitly
for y, z in product(range(-3, 4), repeat=2):
    x = F(15 + y - 2 * z, 2)
    P = (x, y, z)
    assert norm2(sub(P, A)) == norm2(sub(P, B))

# ---------- the roof ----------
P_, Q_, R_ = (0, 0, 3), (6, 0, 3), (0, 4, 5)
PQ, PR = sub(Q_, P_), sub(R_, P_)
same("eg13 PQ", PQ, (6, 0, 0))
same("eg13 PR", PR, (0, 4, 2))
x = cross(PQ, PR)
same("eg13 cross", x, (0, -12, 24))
assert x == mul(12, (0, -1, 2))
eq("eg13 p", dot((0, -1, 2), P_), 6)
eq("eg13 Q", dot((0, -1, 2), Q_), 6)
eq("eg13 R", dot((0, -1, 2), R_), 6)
eq("eg13 height", 3 + 0.5 * 3, 4.5)

# ---------- spot the error ----------
a, b = (2, 1, -3), (4, -1, 2)
c = cross(a, b)
same("spot correct", c, (-1, -16, -6))
eq("spot i", 1 * 2 - (-3) * (-1), -1)
eq("spot student j", 2 * 2 - (-3) * 4, 16)
eq("spot correct j", (-3) * 4 - 2 * 2, -16)
eq("spot k", 2 * (-1) - 1 * 4, -6)
eq("spot wrong dot", dot(a, (-1, 16, -6)), 32)
eq("spot wrong dot hand", -2 + 16 + 18, 32)
eq("spot right dot", dot(a, c), 0)
eq("spot right dot hand", -2 - 16 + 18, 0)

# ---------- try: start easy ----------
same("t1", cross((3, -1, 2), (1, 4, -2)), (-6, 8, 13))
eq("t1 check", dot((3, -1, 2), (-6, 8, 13)), 0)
eq("t1 check hand", -18 - 8 + 26, 0)
same("t2", cross((2, -4, 6), (-1, 2, -3)), (0, 0, 0))
assert mul(-2, (-1, 2, -3)) == (2, -4, 6)
same("t3", cross((1, 0, 2), (3, -1, 1)), (2, 5, -1))
PQ, PR = (-3, 4, 0), (-3, 0, 2)
same("t4 PQ", sub((0, 4, 0), (3, 0, 0)), PQ)
same("t4 PR", sub((0, 0, 2), (3, 0, 0)), PR)
x = cross(PQ, PR)
same("t4 cross", x, (8, 6, 12))
assert x == mul(2, (4, 3, 6))
eq("t4 |.|^2", norm2((4, 3, 6)), 61)
eq("t4 area", sf(0.5 * mag(x), 3), 7.81)
eq("t5 p", dot((1, -2, 3), (2, 0, -1)), -1)
eq("t6 dist", sf(8 / sqrt(21), 3), 1.75)
eq("t7", 3 * 1 + 2 + 2, 7)
n = cross((1, 0, 2), (0, 3, 1))
same("t8 n", n, (-6, -1, 3))
eq("t8 p", dot(n, (1, 1, 0)), -7)
AB, AC = sub((2, 0, 3), (1, 1, 1)), sub((0, 2, 2), (1, 1, 1))
same("t9 AB", AB, (1, -1, 2))
same("t9 AC", AC, (-1, 1, 1))
n = cross(AB, AC)
same("t9 n", n, (-3, -3, 0))
for Pt in [(1, 1, 1), (2, 0, 3), (0, 2, 2)]:
    eq("t9 pt", Pt[0] + Pt[1], 2)
n = (1, 2, -1)
eq("t10 point", dot(n, (4, 0, 0)), 4)
eq("t10 b", dot(n, (-2, 1, 0)), 0)
eq("t10 c", dot(n, (1, 0, 1)), 0)
assert not parallel((-2, 1, 0), (1, 0, 1))

# ---------- exam practice ----------
same("e1", cross((4, -1, 2), (-1, 3, 1)), (-7, -6, 11))
eq("e1 check", dot((4, -1, 2), (-7, -6, 11)), 0)
A, B, C = (2, -1, 0), (3, 1, 2), (-1, 2, 1)
AB, AC = sub(B, A), sub(C, A)
same("e2 AB", AB, (1, 2, 2))
same("e2 AC", AC, (-3, 3, 1))
x = cross(AB, AC)
same("e2 cross", x, (-4, -7, 9))
eq("e2 |x|^2", norm2(x), 146)
eq("e2 area", sf(0.5 * sqrt(146), 3), 6.04)
A, B, C = (1, 0, -1), (2, 3, 1), (0, 1, 4)
AB, AC = sub(B, A), sub(C, A)
same("e3 AB", AB, (1, 3, 2))
same("e3 AC", AC, (-1, 1, 5))
n = cross(AB, AC)
same("e3 n", n, (13, -7, 4))
eq("e3 p", dot(n, A), 9)
eq("e3 B", dot(n, B), 9)
eq("e3 C", dot(n, C), 9)
b, c = (1, -2, 0), (3, 1, -1)
n = cross(b, c)
same("e4 n", n, (2, 1, 7))
eq("e4 p", dot(n, (2, -1, 3)), 24)
eq("e4 point", dot(n, (0, 3, 3)), 24)
A, B = (-1, 2, 3), (3, 0, -1)
M = tuple(F(x + y, 2) for x, y in zip(A, B))
same("e5 M", M, (1, 1, 1))
same("e5 AB", sub(B, A), (4, -2, -4))
nn = (2, -1, -2)
assert parallel(sub(B, A), nn)
eq("e5 p", dot(nn, M), -1)
eq("e5 |n|", mag(nn), 3)
eq("e5 dist", F(1, 3), 1 / 3)
for y, z in product(range(-3, 4), repeat=2):
    x = F(-1 + y + 2 * z, 2)
    Pt = (x, y, z)
    assert norm2(sub(Pt, A)) == norm2(sub(Pt, B))
# e6
l0, d = (0, 1, 3), (1, -1, 2)
P = (2, 2, -1)
eq("e6 a y at t=2", 1 - 2, -1)
AP = sub(P, l0)
same("e6 AP", AP, (2, 1, -4))
n = cross(d, AP)
same("e6 n", n, (2, 8, 3))
eq("e6 p", dot(n, l0), 17)
eq("e6 P", dot(n, P), 17)
eq("e6 line pt", dot(n, add(l0, mul(5, d))), 17)
AB = mul(2, d)
same("e6 AB", AB, (2, -2, 4))
x = cross(AB, AP)
same("e6 cross", x, (4, 16, 6))
assert x == mul(2, n)
eq("e6 |n|^2", norm2(n), 77)
eq("e6 area", sf(sqrt(77), 3), 8.77)
# e7
A, B, C = (1, 0, 0), (0, 2, 0), (0, 0, 3)
AB, AC = sub(B, A), sub(C, A)
same("e7 AB", AB, (-1, 2, 0))
same("e7 AC", AC, (-1, 0, 3))
n = cross(AB, AC)
same("e7 n", n, (6, 3, 2))
eq("e7 p", dot(n, A), 6)
eq("e7 B", dot(n, B), 6)
eq("e7 C", dot(n, C), 6)
eq("e7 |n|", mag(n), 7)
area = F(7, 2)
dist = F(6, 7)
vol = F(1, 3) * area * dist
eq("e7 volume", vol, 1)
eq("e7 triple", abs(dot(C, cross(A, B))) / 6, 1)

# ---------- stretch ----------
a, b, c = (4, 0, 0), (0, 6, 0), (2, 3, 3)
x = cross(a, b)
same("s1 axb", x, (0, 0, 24))
eq("s1 c.x", dot(c, x), 72)
eq("s1 volume", F(abs(dot(c, x)), 6), 12)
for h in range(1, 6):
    eq("s1 24h", dot((2, 3, h), x), 24 * h)
eq("s1 V=4h", F(24 * 3, 6), 12)
# random check of V = 1/6 |c.(a x b)| against base*height
for _ in range(50):
    a_ = tuple(rnd.randint(-5, 5) for _ in range(3))
    b_ = tuple(rnd.randint(-5, 5) for _ in range(3))
    c_ = tuple(rnd.randint(-5, 5) for _ in range(3))
    x = cross(a_, b_)
    if norm2(x) == 0:
        continue
    base = 0.5 * mag(x)
    height = abs(dot(c_, x)) / mag(x)
    eq("s1 general", base * height / 3, abs(dot(c_, x)) / 6)
p_, q_, r_ = 2, 3, 6
OAB, OBC, OCA = F(1, 2) * p_ * q_, F(1, 2) * q_ * r_, F(1, 2) * r_ * p_
same("s2 areas", (OAB, OBC, OCA), (3, 9, 6))
x = cross((-2, 3, 0), (-2, 0, 6))
same("s2 cross", x, (18, 12, 6))
eq("s2 |x|^2", norm2(x), 504)
assert 504 == 36 * 14
eq("s2 ABC^2", F(norm2(x), 4), 126)
eq("s2 sum", OAB ** 2 + OBC ** 2 + OCA ** 2, 126)
eq("s2 18^2+12^2+6^2", 324 + 144 + 36, 504)
for pt, qt, rt in [(1, 2, 3), (2, 3, 6), (4, 5, 7)]:
    xx = cross((-pt, qt, 0), (-pt, 0, rt))
    ABC2 = F(norm2(xx), 4)
    assert ABC2 == (F(pt * qt, 2)) ** 2 + (F(qt * rt, 2)) ** 2 + (F(rt * pt, 2)) ** 2

# ---------- quiz ----------
same("q1 j x i", cross((0, 1, 0), (1, 0, 0)), (0, 0, -1))
eq("q4 |n|", mag((2, -1, 2)), 3)
eq("q4 dist", 9 / 3, 3)
eq("q4 wrong sqrt", sf(9 / sqrt(5), 3), 4.02)
n = (3, -2, 1)
eq("q5 b", dot(n, (1, 0, -3)), 0)
eq("q5 c", dot(n, (0, 1, 2)), 0)
eq("q5 third point", dot(n, (1, 0, 0)), 3)
assert parallel((1, 0, -3), (2, 0, -6))

print("ok")
