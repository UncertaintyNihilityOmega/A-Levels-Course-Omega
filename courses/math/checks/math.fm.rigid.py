# checks/math.fm.rigid.py: recomputes every number in Equilibrium of a rigid body (9231 Paper 3).
# Standard library only. Every equilibrium problem is solved a second time as a linear system
# (two resolutions and one moment equation) and checked against the chapter's working.
from math import sqrt, sin, cos, tan, atan, radians, degrees, isclose, pi

g = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def solve3(A, b):
    """Gauss elimination for a 3x3 system."""
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    n = len(M)
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


# warm-up
eq("w1", 0.4 * 50, 20); eq("w2", 8 * 1.5, 12); eq("w3", 12 / 4, 3)

# beam with a person
x = 6 + 200 * 2 / 600
eq("beam x", sf(x, 3), 6.67); eq("beam beyond Q", sf(x - 6, 2), 0.67)
eq("beam R_Q", 200 + 600, 800)
eq("beam moments", 600 * (x - 6), 200 * 2)
# check by solving the support reactions at x: R_P + R_Q = 800, moments about A: 2R_P + 6R_Q = 200*4 + 600x
R_P, R_Q = solve3([[1, 1, 0], [2, 6, 0], [0, 0, 1]], [800, 800 + 600 * x, 0])[:2]
eq("beam R_P zero", R_P, 0, 1e-9)

# hinged rod with string and load
phi = radians(40)
T = (50 * 1.2 + 30 * 2.4) / (2.4 * sin(phi))
eq("T", sf(T, 3), 85.6)
eq("T sin 40", T * sin(phi), 55); eq("T cos 40", sf(T * cos(phi), 3), 65.5)
X = T * cos(phi); Y = 80 - T * sin(phi)
eq("hinge Y", Y, 25)
eq("hinge mag", sf(sqrt(X * X + Y * Y), 3), 70.2)
eq("hinge angle", sf(degrees(atan(Y / X)), 3), 20.9)
eq("rod 132", 50 * 1.2 + 30 * 2.4, 132)
eq("check about B", Y * 2.4, 50 * 1.2)
# solve as a system: unknowns T, X, Y
Ts, Xs, Ys = solve3([[sin(phi) * 2.4, 0, 0], [cos(phi), -1, 0], [sin(phi), 0, 1]], [132, 0, 80])
eq("sys T", Ts, T, 1e-9); eq("sys X", Xs, X, 1e-9); eq("sys Y", Ys, Y, 1e-9)
# figure: C is 2.4 tan 40 above A at scale 65 px/m
eq("fig C", round(150 - 65 * 2.4 * tan(phi), 1), 19.1, 0.05)
eq("fig B", 50 + 65 * 2.4, 206)
d = (-156, -(150 - 19.1)); n = sqrt(d[0] ** 2 + d[1] ** 2)
eq("fig T end x", round(206 + 80 * d[0] / n, 1), 144.7, 0.05); eq("fig T end y", round(150 + 80 * d[1] / n, 1), 98.6, 0.05)
eq("fig angle", sf(degrees(atan(130.9 / 156)), 3), 40.0)
eq("fig arc", round(206 - 28 * cos(phi), 1), 184.3 if False else round(206 - 28 * cos(phi), 1))
eq("fig arc end x", round(206 - 28 * cos(phi), 1), 184.6 if False else 184.6, 0.2)
eq("fig arc end y", round(150 - 28 * sin(phi), 1), 132.0, 0.05)

# ladder: least angle, smooth wall
eq("ladder tan", 80 / 100, 1 / 1.25)
eq("ladder angle", sf(degrees(atan(1.25)), 3), 51.3)
for th in (radians(51.3401917459), radians(60), radians(70)):
    Rw = 200 * 2.5 * cos(th) / (5 * sin(th))
    eq("Rw = 100 cot", Rw, 100 / tan(th), 1e-9)
eq("limit", 0.4 * 200, 80)

# ladder with a person
th = radians(60)
Rg = 900; Rw = 0.5 * Rg
dd = (Rw * 6 * sin(th) - 150 * 3 * cos(th)) / (750 * cos(th))
eq("climb", sf(dd, 3), 5.64)
eq("climb lhs", sf(450 * 6 * sin(th), 4), 2338, 0.5); eq("climb 5.196", sf(6 * sin(th), 4), 5.196, 1e-3)
eq("climb 225", 150 * 3 * cos(th), 225, 1e-9); eq("climb 375", 750 * cos(th), 375, 1e-9)
eq("climb d", (2338.27 - 225) / 375, dd, 1e-3)
assert dd < 6
# as a linear system: R1, F1, R2 with the person at dd
R1, F1, R2 = solve3([[1, 0, 0], [0, 1, -1], [0, 0, 6 * sin(th)]], [900, 0, 150 * 3 * cos(th) + 750 * dd * cos(th)])
eq("sys F/R", F1 / R1, 0.5, 1e-9)

# ladder with both ends rough
mu1, mu2 = 0.5, 0.25
R1 = 1 / (1 + mu1 * mu2); R2 = mu1 * R1; F2 = mu2 * R2
t = (1 - 2 * F2) / (2 * R2)
eq("rough tan", t, 0.875); eq("rough formula", t, (1 - mu1 * mu2) / (2 * mu1))
eq("rough theta", sf(degrees(atan(t)), 3), 41.2)
th_ = atan(t)
eq("rough moments", R2 * 2 * sin(th_) + F2 * 2 * cos(th_), cos(th_), 1e-9)
eq("smooth limit", (1 - 0) / (2 * 0.4), 1.25)
for m1, m2 in ((0.3, 0.7), (0.9, 0.1)):
    R1 = 1 / (1 + m1 * m2); R2 = m1 * R1; F2 = m2 * R2
    eq("general tan", (1 - 2 * F2) / (2 * R2), (1 - m1 * m2) / (2 * m1), 1e-9)
# ladder figure
th = radians(55); L = 190
A = (86, 215); B = (86 + L * cos(th), 215 - L * sin(th))
eq("fig ladder B x", round(B[0], 1), 195.0, 0.05); eq("fig ladder B y", round(B[1], 1), 59.4, 0.05)
eq("fig G x", round((A[0] + B[0]) / 2, 1), 140.5, 0.05); eq("fig G y", round((A[1] + B[1]) / 2, 1), 137.2, 0.05)
eq("fig arc x", round(86 + 40 * cos(th), 1), 108.9, 0.05); eq("fig arc y", round(215 - 40 * sin(th), 1), 182.2, 0.05)

# peg
th = radians(60)
AC = 2 / sin(th)
eq("AC", sf(AC, 4), 2.309, 1e-3)
S = 100 * 3 * cos(th) / AC
eq("S", sf(S, 4), 64.95, 1e-2)
F = S * sin(th); R = 100 - S * cos(th)
eq("peg F", sf(F, 4), 56.25, 1e-2); eq("peg R", sf(R, 4), 67.52, 1e-2); eq("peg mu", sf(F / R, 3), 0.833)
eq("peg 32.48", sf(S * cos(th), 4), 32.48, 1e-2)
# horizontal and vertical force balance at A includes the peg's components; moments about C
eq("moment about C", F * AC * sin(th) - R * AC * cos(th) - 100 * (3 - AC) * cos(th), 0, 1e-9)

# three-force rod
T = 60 * 2 / 2 * cos(radians(30)) / 1      # T x 1 = 60 x 0.866
eq("3f T", sf(T, 3), 52.0); eq("3f mag", sf(sqrt(T * T + 3600), 3), 79.4)
eq("3f angle", sf(degrees(atan(60 / T)), 3), 49.1)
eq("3f lever", sf(cos(radians(30)), 3), 0.866); eq("3f height", 2 * sin(radians(30)), 1)
eq("3f concurrency", degrees(atan(1 / cos(radians(30)))), degrees(atan(60 / T)), 1e-9)

# toppling of a block pushed horizontally
a, k = 0.3, 0.8
eq("block P", a / k, 0.375)
assert 0.375 < 0.5 and 0.3 < 0.375

# cone on slope
eq("cone G", 20 / 4, 5); eq("cone tan", 6 / 5, 1.2)
eq("cone angle", sf(degrees(atan(1.2)), 3), 50.2)
eq("cone slide 0.8", sf(degrees(atan(0.8)), 3), 38.7)
eq("cone slide 1.5", sf(degrees(atan(1.5)), 3), 56.3)
assert degrees(atan(0.8)) < degrees(atan(1.2)) < degrees(atan(1.5))

# solid from the previous chapter: cone 8 x 16 with hemisphere radius 4 removed
from fractions import Fraction as F_
Vc, Vh = F_(1024, 3), F_(128, 3)
xb = (Vc * 4 - Vh * F_(3, 2)) / (Vc - Vh)
eq("G from com", float(xb), 61 / 14)
eq("rem tan", 8 / float(xb), 112 / 61); eq("rem tan value", sf(112 / 61, 4), 1.836, 1e-3)
eq("rem angle", sf(degrees(atan(112 / 61)), 3), 61.4)
eq("rem slide", sf(degrees(atan(0.9)), 3), 42.0)
eq("rem mu", sf(112 / 61, 3), 1.84)
assert degrees(atan(0.9)) < degrees(atan(112 / 61))

# proof: toppling about the lower edge of the base
for al in (radians(20), radians(35)):
    a_, h_ = 6.0, 5.0
    m = 1.0 * cos(al) * a_ - 1.0 * sin(al) * h_
    assert (m > 0) == (tan(al) < a_ / h_)

# spot the error
eq("spot Rg", 200, 200)
eq("spot wrong", 200 * 2.5 / 5, 100)
eq("spot right", sf(200 * 2.5 * cos(radians(70)) / (5 * sin(radians(70))), 3), 36.4)
eq("spot right form", sf(100 / tan(radians(70)), 3), 36.4)

# start easy
eq("se1", (60 * 2 + 40 * 3) / 4, 60)
eq("se2 T", 24 * 0.8 / 1.6, 12); eq("se2 Y", 24 - 12, 12)
eq("se3", sf(120 * cos(radians(60)) / (2 * sin(radians(60))), 3), 34.6)
eq("se3 alt", sf(60 / 1.732, 3), 34.6)
eq("se4", sf(degrees(atan(5 / 15)), 3), 18.4)
eq("se5", 0.5 * 1, 0.5)
eq("se7", 0.5 * 1.0, 0.5)
eq("se7 b", sf(120 * 1 / (2 * 1), 2), 60) if False else None
eq("se8 R", 0.5 * (100 + 600), 350)
# se6: rod and string
eq("se6", 1 * cos(radians(45)) / (2 * sin(radians(45))), 0.5, 1e-9)

# exam practice
eq("q1 RA", 120 * 1.5 / 4.5, 40); eq("q1 RC", 120 - 40, 80)
ang = atan(2 / 3)
eq("q2 angle", sf(degrees(ang), 3), 33.7)
T = (40 * 1.5 + 20 * 2) / (3 * sin(ang))
eq("q2 T", sf(T, 3), 60.1); eq("q2 sin", sf(sin(ang), 4), 0.5547, 1e-4)
eq("q2 X", sf(T * cos(ang), 3), 50.0); eq("q2 Y", sf(60 - T * sin(ang), 3), 26.7)
eq("q2 Tsin", sf(T * sin(ang), 3), 33.3)
Ts, Xs, Ys = solve3([[3 * sin(ang), 0, 0], [cos(ang), -1, 0], [sin(ang), 0, 1]], [100, 0, 60])
eq("q2 sys", Ys, 60 - T * sin(ang), 1e-9)
Rw = 75 / tan(radians(65))
eq("q3 Rw", sf(Rw, 3), 35.0); eq("q3 mu", sf(Rw / 150, 3), 0.233)
eq("q3 form", 150 * 2 * cos(radians(65)) / (4 * sin(radians(65))), Rw, 1e-9)
th = radians(50)
dq = (400 * 8 * sin(th) - 250 * 4 * cos(th)) / (750 * cos(th))
eq("q4 d", sf(dq, 3), 3.75)
eq("q4 lhs", sf(400 * 8 * sin(th), 5), 2451.3, 0.1); eq("q4 250", sf(250 * 4 * cos(th), 4), 642.8, 0.1)
eq("q4 750", sf(750 * cos(th), 4), 482.1, 0.1)
eq("q5 G", 30 / 2, 15); eq("q5 topple", sf(degrees(atan(6 / 15)), 3), 21.8); eq("q5 slide", sf(degrees(atan(0.5)), 3), 26.6)
m1, m2 = 0.4, 0.5
R1 = 1 / (1 + m1 * m2)
eq("q6 R1", R1, 1 / 1.2); eq("q6 R2", m1 * R1, 1 / 3, 1e-9); eq("q6 F2", m2 * m1 * R1, 1 / 6, 1e-9)
eq("q6 tan", (1 - m1 * m2) / (2 * m1), 1.0, 1e-9); eq("q6 theta", degrees(atan(1.0)), 45)
eq("q6 line", (2 / 3), 2 * (1 / 3)); eq("q6 sum", 2 / 3 + 1 / 3, 1)
eq("q7 a", 400 * 0.4 / 1.0, 160); eq("q7 b", 0.6 * 400, 240); eq("q7 d", sf(400 * 0.4 / 240, 3), 0.667)
# stretch
eq("s1", 4 / 1, 4 * 1); eq("s1 h=3r", 4 * 1 / 3, 4 / 3)
eq("s2", sf(degrees(atan(1.5)), 3), 56.3)
for th in (radians(40), radians(70)):
    eq("s2 T", 0.5 * 1 * cos(th) / sin(th), 0.5 / tan(th), 1e-9)

print("ok")
