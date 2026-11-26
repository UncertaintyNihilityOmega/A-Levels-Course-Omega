# checks/math.fm.transform.py: recomputes every number in "Matrices as transformations".
# Standard library only. Exact work with Fraction where possible; trig values with math and a tolerance.
from fractions import Fraction as F
from itertools import product
from math import cos, sin, tan, radians, sqrt, isclose, atan2, degrees, pi


def M(rows):
    return [[F(x) for x in r] for r in rows]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):
    d = det(A)
    return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]


def img(A, p):
    return (A[0][0] * p[0] + A[0][1] * p[1], A[1][0] * p[0] + A[1][1] * p[1])


def area(pts):
    n = len(pts)
    return abs(sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))) / 2


def eq(label, got, want):
    assert got == M(want), f"{label}: computed {got}, chapter says {want}"


def near(label, got, want, tol=1e-9):
    assert isclose(got, want, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def mnear(label, got, want, tol=1e-9):
    for r, s in zip(got, want):
        for a, b in zip(r, s):
            assert isclose(float(a), b, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def rot(deg):
    t = radians(deg)
    return [[cos(t), -sin(t)], [sin(t), cos(t)]]


def refl(deg):
    t = radians(2 * deg)
    return [[cos(t), sin(t)], [sin(t), -cos(t)]]


def fmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


# ---- Warm-up
near("cos30", cos(radians(30)), sqrt(3) / 2); near("sin30", sin(radians(30)), 0.5)
assert all(2 * m * m + m - 1 == 0 for m in (F(1, 2), -1))
eq("warm-up product", mul(M([[1, 2], [0, 1]]), M([[3], [4]])), [[11], [4]])

# ---- Columns are the images of i and j
assert img(M([[2, 3], [1, 4]]), (1, 0)) == (2, 1) and img(M([[2, 3], [1, 4]]), (0, 1)) == (3, 4)
# any point: M(x,y) = x * (first column) + y * (second column)
Mx = M([[2, 3], [1, 4]])
for p in product(range(-3, 4), repeat=2):
    assert img(Mx, p) == (p[0] * 2 + p[1] * 3, p[0] * 1 + p[1] * 4)
# the matrix from images: i -> (3, 1), j -> (-2, 2) gives (3 -2; 1 2)
S = M([[3, -2], [1, 2]]); assert img(S, (1, 0)) == (3, 1) and img(S, (0, 1)) == (-2, 2)
# shear figure: (1 2; 0 1): O, A(1,0), B(1,1), C(0,1) -> O, A, B'(3,1), C'(2,1)
Sh = M([[1, 2], [0, 1]])
assert [img(Sh, p) for p in ((0, 0), (1, 0), (1, 1), (0, 1))] == [(0, 0), (1, 0), (3, 1), (2, 1)]
assert det(Sh) == 1 and area([(0, 0), (1, 0), (3, 1), (2, 1)]) == 1

# ---- Standard matrices
mnear("rot 90", rot(90), [[0, -1], [1, 0]])
mnear("rot 180", rot(180), [[-1, 0], [0, -1]])
mnear("rot -90", rot(-90), [[0, 1], [-1, 0]])
mnear("rot 60", rot(60), [[0.5, -sqrt(3) / 2], [sqrt(3) / 2, 0.5]])
mnear("rot 45", rot(45), [[1 / sqrt(2), -1 / sqrt(2)], [1 / sqrt(2), 1 / sqrt(2)]])
mnear("rot 30", rot(30), [[sqrt(3) / 2, -0.5], [0.5, sqrt(3) / 2]])
mnear("refl x-axis", refl(0), [[1, 0], [0, -1]])
mnear("refl y-axis", refl(90), [[-1, 0], [0, 1]])
mnear("refl y=x", refl(45), [[0, 1], [1, 0]])
mnear("refl y=-x", refl(135), [[0, -1], [-1, 0]])
# reflection in y = x sqrt3: angle 60 deg
assert isclose(tan(radians(60)), sqrt(3))
mnear("refl y=sqrt3 x", refl(60), [[-0.5, sqrt(3) / 2], [sqrt(3) / 2, 0.5]])
# derivation: image of j in the mirror at angle t is at angle 2t - 90 deg
for t in (10, 35, 60, 100):
    a = radians(2 * t - 90)
    near("refl j", cos(a), sin(radians(2 * t))); near("refl j2", sin(a), -cos(radians(2 * t)))
# determinants
near("det rot", sum(1 for _ in [0]) * (rot(37)[0][0] * rot(37)[1][1] - rot(37)[0][1] * rot(37)[1][0]), 1)
near("det refl", refl(37)[0][0] * refl(37)[1][1] - refl(37)[0][1] * refl(37)[1][0], -1)
# rotation and reflection matrices are orthogonal: R^T R = I; inverse of rot(t) is rot(-t)
mnear("rot inverse", fmul(rot(40), rot(-40)), [[1, 0], [0, 1]])
mnear("refl^2 = I", fmul(refl(25), refl(25)), [[1, 0], [0, 1]])

# Stretch, enlargement, shear facts
E3 = M([[3, 0], [0, 3]]); St = M([[2, 0], [0, 1]]); Shk = M([[1, 3], [0, 1]])
assert img(E3, (2, -1)) == (6, -3) and img(St, (2, -1)) == (4, -1)
assert img(Shk, (1, 1)) == (4, 1) and img(Shk, (0, 1)) == (3, 1) and img(Shk, (5, 0)) == (5, 0)
assert det(E3) == 9 and det(St) == 2 and det(Shk) == 1
eq("inverse of shear", inv(Shk), [[1, -3], [0, 1]])
eq("inverse of enlargement", inv(E3), [[F(1, 3), 0], [0, F(1, 3)]])
eq("inverse of stretch", inv(St), [[F(1, 2), 0], [0, 1]])

# ---- Naming from a matrix
assert img(M([[0, -1], [1, 0]]), (1, 0)) == (0, 1)
assert img(M([[1, 3], [0, 1]]), (0, 1)) == (3, 1)

# ---- Composition: AB means B first
Rot90 = M([[0, -1], [1, 0]]); Ry = M([[0, 1], [1, 0]])   # reflection in y = x
AB = mul(Rot90, Ry)       # reflect in y=x, then rotate 90
BA = mul(Ry, Rot90)
eq("rot after refl(y=x)", AB, [[-1, 0], [0, 1]])
eq("refl after rot", BA, [[1, 0], [0, -1]])
assert img(Ry, (1, 0)) == (0, 1) and img(Rot90, (0, 1)) == (-1, 0) and img(AB, (1, 0)) == (-1, 0)
assert img(BA, (1, 0)) == (1, 0) and img(BA, (0, 1)) == (0, -1)
# inverse of "B then A" is "A^-1 then B^-1": (AB)^-1 = B^-1 A^-1
assert inv(AB) == mul(inv(Ry), inv(Rot90))

# decomposition of (0 -2; 1 0) = (stretch x SF 2) after (rotation 90)
Mq = M([[0, -2], [1, 0]])
assert mul(St, Rot90) == Mq
eq("M R^-1", mul(Mq, inv(Rot90)), [[2, 0], [0, 1]])
assert img(Mq, (1, 0)) == (0, 1) and img(Mq, (0, 1)) == (-2, 0)
assert det(Mq) == 2

# ---- Determinant and area
assert det(S) == 8 and area([(0, 0), (3, 1), (1, 3 + 1 - 2 + 1)]) >= 0
Tm = M([[2, 1], [3, 4]]); tri = [(1, 1), (4, 1), (1, 3)]
assert area(tri) == 3 and det(Tm) == 5
tri2 = [img(Tm, p) for p in tri]
assert tri2 == [(3, 7), (9, 16), (5, 15)] and area(tri2) == 15
assert 3 * (16 - 15) + 9 * (15 - 7) + 5 * (7 - 16) == 30
# area of the image of the unit square = |ad - bc| (proof check on random matrices)
for a, b, c, d in product(range(-3, 4), repeat=4):
    Q = M([[a, b], [c, d]])
    sq = [img(Q, p) for p in ((0, 0), (1, 0), (1, 1), (0, 1))]
    assert area(sq) == abs(a * d - b * c)
# the composite sign rule: det(AB) = det A det B
assert det(AB) == det(Rot90) * det(Ry) == -1
# singular matrix collapses the plane
Sg = M([[1, 2], [2, 4]]); assert det(Sg) == 0
for p in product(range(-3, 4), repeat=2):
    x, y = img(Sg, p)
    assert y == 2 * x
assert img(Sg, (3, 1)) == (5, 10)
# logo: stretch x SF 3, reflect in x-axis, shear (1 2; 0 1)
Lst = M([[3, 0], [0, 1]]); Lre = M([[1, 0], [0, -1]]); Lsh = M([[1, 2], [0, 1]])
LM = mul(Lsh, mul(Lre, Lst))
eq("logo matrix", LM, [[3, -2], [0, -1]])
eq("logo step 1", mul(Lre, Lst), [[3, 0], [0, -1]])
assert det(LM) == -3 == 3 * -1 * 1 and 18 * 3 == 54

# ---- Invariant points
Ma = M([[3, -2], [1, 0]])
for t in range(-4, 5):
    assert img(Ma, (t, t)) == (t, t)                  # line y = x of invariant points
assert (3 - 1, -2, 1, 0 - 1) == (2, -2, 1, -1)         # (M - I) = (2 -2; 1 -1): both rows give x = y
assert det(Ma) == 2
# rotation has only the origin: det(M - I) != 0
for deg in (30, 90, 135, 270):
    R = rot(deg)
    assert (R[0][0] - 1) * (R[1][1] - 1) - R[0][1] * R[1][0] > 1e-9
# shear: invariant points are the x-axis
assert all(img(Shk, (t, 0)) == (t, 0) for t in range(-3, 4))
# (M - I) for (5 -2; 4 -1) is (4 -2; 4 -2)
Mb = M([[5, -2], [4, -1]])
assert all(img(Mb, (t, 2 * t)) == (t, 2 * t) for t in range(-4, 5))
assert det(Mb) == 3

# ---- Invariant lines through O: (3 1; 2 2)
Mc = M([[3, 1], [2, 2]])
assert det(Mc) == 4
for m in (1, -2):
    assert 1 * m * m + (3 - 2) * m - 2 == 0
assert all(1 * m * m + m - 2 != 0 for m in (0, 2, -1))
assert all(img(Mc, (t, t)) == (4 * t, 4 * t) for t in range(-3, 4))             # y = x scaled by 4
assert all(img(Mc, (t, -2 * t)) == (t, -2 * t) for t in range(-3, 4))          # y = -2x fixed pointwise
assert img(Mc, (0, 1)) == (1, 2)                                                   # y-axis is not invariant
# general fact: y = mx invariant iff b m^2 + (a - d) m - c = 0 (random integer matrices, brute force over m)
for a, b, c, d in product(range(-2, 3), repeat=4):
    for m in (F(-3), F(-2), F(-1), F(-1, 2), F(0), F(1, 2), F(1), F(2), F(3)):
        Q = M([[a, b], [c, d]])
        inv_line = all(img(Q, (t, m * t))[1] == m * img(Q, (t, m * t))[0] for t in (1, 2, 3))
        assert inv_line == (b * m * m + (a - d) * m - c == 0)
# y-axis invariant iff b = 0
for a, b, c, d in product(range(-2, 3), repeat=4):
    Q = M([[a, b], [c, d]])
    assert (img(Q, (0, 1))[0] == 0) == (b == 0)
# shear (1 k; 0 1): only the x-axis (m = 0) through O
for k in (1, 3):
    assert [m for m in range(-4, 5) if k * m * m == 0] == [0]
# rotation: no real m (b m^2 + (a-d) m - c = -sin(m^2 + 1))
assert all(-1 * m * m - 1 < 0 for m in range(-5, 6))

# every line of gradient 1 is invariant under (2 -1; 1 0)
Mg = M([[2, -1], [1, 0]])
for c in range(-3, 4):
    for t in range(-3, 4):
        x, y = img(Mg, (t, t + c))
        assert y == x + c and (x, y) == (t - c, t)

# Lines not through O under (3 -2; 1 0)
assert all(-2 * m * m + 3 * m - 1 == 0 for m in (1, F(1, 2)))
for c in range(-3, 4):
    for t in range(-3, 4):
        x, y = img(Ma, (t, F(t, 2) + c))
        assert y == F(x, 2) + c                      # y = x/2 + c invariant
        x, y = img(Ma, (t, t + c))
        assert (y == x + c) == (c == 0)              # y = x + c only for c = 0
        assert y == x + 2 * c if True else 0
# check (x, x/2 + c) -> (2x - 2c, x)
assert img(Ma, (4, 2 + 1)) == (2 * 4 - 2 * 1, 4)

# ---- Spot the error
Ra = M([[1, 0], [0, -1]]); Rb = M([[0, -1], [1, 0]])
eq("spot BA", mul(Rb, Ra), [[0, 1], [1, 0]])
eq("spot AB (student)", mul(Ra, Rb), [[0, -1], [-1, 0]])
assert img(mul(Rb, Ra), (2, 1)) == (1, 2)
assert img(mul(Ra, Rb), (2, 1)) == (-1, -2)
assert img(Ra, (2, 1)) == (2, -1) and img(Rb, (2, -1)) == (1, 2)

# ---- Try block
near("t rot 60 exact", sqrt(3) / 2, cos(radians(30)))
assert img(M([[0, 1], [-1, 0]]), (3, 2)) == (2, -3)          # rotation 90 clockwise
eq("t2 stretch y", M([[1, 0], [0, 5]]), [[1, 0], [0, 5]])
eq("t3 refl x then ... ", mul(M([[0, 1], [1, 0]]), M([[1, 0], [0, -1]])), [[0, -1], [1, 0]])
assert img(M([[0, -1], [1, 0]]), (3, 2)) == (-2, 3)
assert det(M([[2, 3], [1, 4]])) == 5 and 5 * 6 == 30
assert det(M([[4, 2], [2, 1]])) == 0
# t6: inverse of (1 2; 0 1) is (1 -2; 0 1); inverse of rotation 90 anticlockwise
eq("t inverse shear", inv(M([[1, 2], [0, 1]])), [[1, -2], [0, 1]])
eq("t inverse rot", inv(M([[0, -1], [1, 0]])), [[0, 1], [-1, 0]])
# t7 invariant points (2 1; 2 3)? M - I = (1 1; 2 2): x + y = 0
Mt = M([[2, 1], [2, 3]]); assert all(img(Mt, (t, -t)) == (t, -t) for t in range(-3, 4))
# t8 invariant lines of (1 2; 3 2): 2m^2 - m - 3 = 0
Mu = M([[1, 2], [3, 2]])
assert all(2 * m * m - m - 3 == 0 for m in (F(3, 2), -1))
assert img(Mu, (2, 3)) == (8, 12) and img(Mu, (1, -1)) == (-1, 1)

# ---- Exam practice
# Q1 rotation 60
mnear("E1", rot(60), [[0.5, -sqrt(3) / 2], [sqrt(3) / 2, 0.5]])
near("E1 image of (4,0)", rot(60)[0][0] * 4, 2); near("E1 image y", rot(60)[1][0] * 4, 2 * sqrt(3))
# Q2
assert img(M([[0, -1], [-1, 0]]), (1, 0)) == (0, -1) and img(M([[0, -1], [-1, 0]]), (1, -1)) == (1, -1)   # y = -x fixed
# Q3 reflection in y = x then enlargement SF 3
E3m = M([[3, 0], [0, 3]])
Q3 = mul(E3m, Ry)
eq("E3 matrix", Q3, [[0, 3], [3, 0]])
assert det(Q3) == -9 and 4 * 9 == 36
# Q4 invariant points (5 -2; 4 -1): y = 2x
# Q5 invariant lines of (1 2; 3 2)
assert 2 * F(3, 2) ** 2 - F(3, 2) - 3 == 0 and 2 * 1 - (-1) - 3 == 0
assert img(Mu, (2, 3)) == (8, 12) and 12 * 1 == F(3, 2) * 8
# Q6 area scale: (k 1; 2 3) det 3k - 2 = +-11
for k, d in ((F(13, 3), 11), (-3, -11)):
    assert det(M([[k, 1], [2, 3]])) == d and abs(d) * 5 == 55
# Q7
c45 = 1 / sqrt(2)
T7 = fmul([[1, 0], [0, -1]], rot(45))
mnear("E7 T", T7, [[c45, -c45], [-c45, -c45]])
near("E7 2 alpha", atan2(-c45, c45), -pi / 4)      # sin 2a = -1/sqrt2, cos 2a = 1/sqrt2
near("E7 alpha", degrees(-pi / 8), -22.5)
near("E7 tan 22.5", tan(radians(22.5)), sqrt(2) - 1)
mnear("E7 T^2 = I", fmul(T7, T7), [[1, 0], [0, 1]])
mnear("E7 refl(-22.5)", refl(-22.5), T7)
# Q8
Mq8 = M([[1, 1], [-2, 4]])
assert det(Mq8) == 6
assert all(1 * m * m - 3 * m + 2 == 0 for m in (1, 2))
assert img(Mq8, (1, 1)) == (2, 2) and img(Mq8, (1, 2)) == (3, 6)
assert area([(0, 0), (2, 2), (3, 6)]) == 3 == area([(0, 0), (1, 1), (1, 2)]) * 6
eq("E8 inverse", inv(Mq8), [[F(2, 3), F(-1, 6)], [F(1, 3), F(1, 6)]])
eq("E8 check", mul(Mq8, inv(Mq8)), [[1, 0], [0, 1]])
assert mul(Mq8, M([[4, -1], [2, 1]])) == M([[6, 0], [0, 6]])
assert [(0, 0), (1, 1), (1, 2)] and (-3) ** 2 - 4 * 2 == 1
# Q8 (a) the second invariant-line check by direct images: (t, 2t) -> (3t, 6t)
assert all(img(Mq8, (t, 2 * t)) == (3 * t, 6 * t) for t in range(-3, 4))

# ---- Stretch
# (i) M = (cos t, sin t; sin t, -cos t): invariant points y = x tan(t/2)
for t in (30, 70, 110, 200):
    Mt_ = refl(t / 2)
    mnear("stretch refl", Mt_, [[cos(radians(t)), sin(radians(t))], [sin(radians(t)), -cos(radians(t))]])
    m = tan(radians(t / 2))
    x = 1.7
    px, py = x, m * x
    qx = Mt_[0][0] * px + Mt_[0][1] * py; qy = Mt_[1][0] * px + Mt_[1][1] * py
    near("fixed x", qx, px); near("fixed y", qy, py)
    near("half-angle", (1 - cos(radians(t))) / sin(radians(t)), tan(radians(t / 2)))
# (ii) two reflections make a rotation of twice the angle between the mirrors
for a_, b_ in ((10, 55), (20, 80), (-15, 40)):
    R = fmul(refl(b_), refl(a_))
    mnear("two reflections", R, rot(2 * (b_ - a_)))

# ---- Quiz
assert det(M([[0, -1], [1, 0]])) == 1
assert det(M([[1, 0], [0, -1]])) == -1
assert det(M([[2, 0], [0, 3]])) == 6
assert img(M([[0, 1], [1, 0]]), (3, 5)) == (5, 3)
assert img(M([[1, 0], [0, 2]]), (3, 5)) == (3, 10)
# Reader FIX: bounding rectangle (a+b)(c+d) minus corners = ad - bc; triangle check from image vertex (3, 7)
for a, b, c, d in product(range(1, 6), repeat=4):
    if a * d > b * c:
        assert (a + b) * (c + d) - (a * c + b * d + 2 * b * c) == a * d - b * c
assert F(1, 2) * abs(6 * 8 - 2 * 9) == 15
print("ok")
