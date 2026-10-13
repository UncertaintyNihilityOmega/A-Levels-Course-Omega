# checks/math.p1.circular.py: recomputes every number in the Circular measure chapter.
from math import isclose, sqrt, sin, cos, tan, atan, acos, pi, radians, degrees

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")

# figure: 1 radian and arc endpoint
eq("1 rad deg", sf(degrees(1), 3), 57.3)
eq("x", 120 + 150 * cos(1), 201.05, 0.01); eq("y", 200 - 150 * sin(1), 73.78, 0.01)
eq("sin1 rad", sf(sin(1)), 0.841); eq("sin1 deg", sf(sin(radians(1)), 3), 0.0175)

# conversions
eq("72", 72 * pi / 180, 2 * pi / 5); eq("72 sf", sf(2 * pi / 5), 1.26)
eq("135", 135 * pi / 180, 3 * pi / 4); eq("135 sf", sf(3 * pi / 4), 2.36)
eq("2.5", round(2.5 * 180 / pi, 1), 143.2); eq("7pi/6", 7 * 180 / 6, 210)

# sectors
eq("s", 6 * 1.2, 7.2); eq("perim", 2 * 6 + 7.2, 19.2); eq("A", 0.5 * 36 * 1.2, 21.6)
eq("theta", 10 / 8, 1.25); eq("r2", 45 / 0.45, 100); eq("r", sqrt(100), 10)
eq("arc c", 30 - 16, 14); eq("theta c", 14 / 8, 1.75); eq("A c", 0.5 * 64 * 1.75, 56)

# segments
eq("seg1", sf(50 * (0.8 - sin(0.8))), 4.13); eq("sin .8", round(sin(0.8), 4), 0.7174)
eq("chord", sf(16 * sin(0.7)), 10.3); eq("sin .7", round(sin(0.7), 4), 0.6442)
eq("cos rule", sf(sqrt(128 - 128 * cos(1.4))), 10.3); eq("128cos", round(128 * cos(1.4), 1), 21.8); eq("128-21.8", round(128 - 21.8, 1), 106.2)

# exam: r=6 theta 2.1
eq("arc", 6 * 2.1, 12.6); eq("chord", round(12 * sin(1.05), 2), 10.41); eq("perim", sf(12.6 + 12 * sin(1.05)), 23.0)
eq("seg", sf(18 * (2.1 - sin(2.1))), 22.3); eq("sin 2.1", round(sin(2.1), 4), 0.8632)
eq("sector", 18 * 2.1, 37.8); eq("tri", round(18 * sin(2.1), 2), 15.54); eq("diff", round(37.8 - 18 * sin(2.1), 2), 22.26)

# exam: ABC
A = atan(8 / 6)  # careful: angle BAC has tan = BC/AB = 8/6
eq("A", round(A, 4), 0.9273)
eq("sector", round(0.5 * 36 * A, 2), 16.69); eq("region", sf(24 - 0.5 * 36 * A), 7.31)
eq("AC", sqrt(36 + 64), 10); eq("arc", round(6 * A, 3), 5.564); eq("perimeter", sf(8 + 4 + 6 * A), 17.6)

# exam: perimeter 24 area 32
for r, th in ((4, 4), (8, 1)):
    eq("perim", 2 * r + r * th, 24); eq("area", 0.5 * r * r * th, 32)
assert (r := 4) and 4**2 - 12 * 4 + 32 == 0 and 8**2 - 12 * 8 + 32 == 0
eq("theta r4", (24 - 8) / 4, 4); eq("theta r8", (24 - 16) / 8, 1)

# try
eq("T1a", 150 / 180, 5 / 6); eq("T1b", round(0.8 * 180 / pi, 1), 45.8); eq("T1c", 5 * 180 / 12, 75)
eq("T2 arc", 12 * pi / 3, 4 * pi); eq("T2 A", 0.5 * 144 * pi / 3, 24 * pi)
eq("T3 r", 15 / 1.2, 12.5); eq("T3 A", 0.5 * 12.5**2 * 1.2, 93.75)
eq("T4", (16 - 10) / 5, 1.2); eq("T4 A", 0.5 * 25 * 1.2, 15)
eq("T5", sf(32 * (1.5 - sin(1.5))), 16.1); eq("sin1.5", round(sin(1.5), 4), 0.9975)
eq("T7 dist", 9 * 2 * pi / 3, 6 * pi); eq("T7 dist sf", sf(6 * pi), 18.8); eq("T7 A", 0.5 * 81 * 2 * pi / 3, 27 * pi); eq("T7 A sf", sf(27 * pi), 84.8)
eq("T8", sf(50 * (0.9 - sin(0.9))), 5.83); eq("sin .9", round(sin(0.9), 4), 0.7833)
eq("T9 theta", 12.6 / 9, 1.4); eq("T9 sector", 0.5 * 81 * 1.4, 56.7); eq("T9 tri", sf(40.5 * sin(1.4)), 39.9)
eq("T9 sin", round(sin(1.4), 5), 0.98545); eq("T9 seg", sf(56.7 - 40.5 * sin(1.4)), 16.8)

# quiz
eq("Q1", 4 * 180 / 3, 240); eq("Q1 wrong", 2 * 180 / 3, 120)
eq("Q2", 5 * 0.8, 4); eq("Q2 area", 0.5 * 25 * 0.8, 10); eq("Q2 r/theta", 5 / 0.8, 6.25)
eq("Q4 deg", sf(sin(radians(1.2)), 3), 0.0209); eq("Q4 rad", sf(sin(1.2)), 0.932)
# FIX additions: cosine rule then sector and segment
th = acos(-2 / 98)
eq("cos", -2 / 98, (49 + 49 - 100) / (2 * 49)); eq("th", round(th, 3), 1.591); assert th > pi / 2 and round(pi / 2, 3) == 1.571
eq("arc", sf(7 * round(th, 3)), 11.1); eq("sector", sf(0.5 * 49 * round(th, 3)), 39.0)
eq("sin", round(sin(round(th, 3)), 4), 0.9998); eq("tri", sf(0.5 * 49 * sin(th)), 24.5)
eq("seg", sf(39.0 - 24.5), 14.5); eq("seg full", round(0.5 * 49 * (th - sin(th)), 2), 14.49)
# v2: warm-up
eq("w1", sf(60 / 360 * 2 * pi * 6), 6.28); eq("w1 exact", 2 * pi, 6.283185307179586); eq("w2", 0.5 * 7 * 10 * sin(radians(30)), 17.5); eq("w3", 4 * 4 + 2 * 4 - 24, 0)

# v2: proofs: sector area as a fraction of the circle, A = 1/2 r s, chord = 2 r sin(theta/2)
for r, t in ((6, 1.1), (3, 2.5), (10, 0.4), (2, 5.0)):
    eq("proof A", t / (2 * pi) * pi * r * r, 0.5 * r * r * t, 1e-9)
    eq("proof A=rs/2", 0.5 * r * (r * t), 0.5 * r * r * t)
for r, t in ((7, 1.2), (5, 2.0), (3, 0.5)):
    # chord from the cosine rule
    eq("proof chord", sqrt(r * r + r * r - 2 * r * r * cos(t)), 2 * r * sin(t / 2), 1e-9)

# v2: spot the error
r, t = 6, 1.1
eq("spot sector", 0.5 * r * r * t, 19.8); eq("spot triangle", 0.5 * r * r * sin(t), 16.04, 5e-3); eq("spot sin", sf(sin(t), 4), 0.8912)
eq("spot wrong sin", sf(sin(radians(1.1)), 3), 0.0192)
eq("spot student", sf(18 * (1.1 - sin(radians(1.1))), 3), 19.5)
eq("spot right", sf(18 * (1.1 - sin(1.1))), 3.76); eq("spot diff", sf(1.1 - sin(1.1), 4), 0.2088)
eq("spot student triangle", 19.8 - 19.5, 0.3); eq("spot tri 0.8912", 0.5 * 36 * 0.8912, 16.04, 1e-2)

# v2: exam practice
eq("x1a", 150 * pi / 180, 5 * pi / 6); eq("x1b", round(1.8 * 180 / pi, 1), 103.1)
eq("x2 arc", 9 * 0.8, 7.2); eq("x2 per", 18 + 7.2, 25.2); eq("x2 area", sf(0.5 * 81 * 0.8), 32.4)
eq("x3 theta", 40 * 2 / 64, 1.25); eq("x3 arc", 8 * 1.25, 10); eq("x3 per", 16 + 10, 26)
eq("x4 r", 36 * 2 / 12, 6); eq("x4 theta", 12 / 6, 2)
eq("x5 seg", sf(0.5 * 49 * (1.2 - sin(1.2))), 6.57); eq("x5 diff", sf(1.2 - sin(1.2), 4), 0.2680)
eq("x5 arc", 7 * 1.2, 8.4); eq("x5 chord", sf(14 * sin(0.6), 4), 7.905); eq("x5 chord cosine", sqrt(98 - 98 * cos(1.2)), 14 * sin(0.6), 1e-9)
eq("x5 per", sf(8.4 + 14 * sin(0.6)), 16.3)
for r in (1, 3, 5, 8): eq("x6 A", 0.5 * r * (20 - 2 * r), 10 * r - r * r); eq("x6 square", 10 * r - r * r, 25 - (r - 5) ** 2)
eq("x6 max", 25 - 0, 25); eq("x6 s", 20 - 2 * 5, 10); eq("x6 theta", 10 / 5, 2)
assert max(10 * (i / 100) - (i / 100) ** 2 for i in range(0, 1001)) == 25
eq("x7 TA", sqrt(13 ** 2 - 5 ** 2), 12); a = acos(5 / 13)
eq("x7 AOT", sf(a, 4), 1.176); eq("x7 AOB", sf(2 * a), 2.35); eq("x7 sector", sf(0.5 * 25 * 2 * a, 3), 29.4)
eq("x7 kite", 2 * 0.5 * 5 * 12, 60); eq("x7 region", sf(60 - 0.5 * 25 * 2 * a), 30.6)
# stretch 1: cone from a sector
R, th = 12, 4 * pi / 3
eq("s1 arc", R * th, 16 * pi); eq("s1 r", R * th / (2 * pi), 8); eq("s1 h", sf(sqrt(144 - 64)), 8.94); eq("s1 csa", 0.5 * R * R * th, 96 * pi); eq("s1 csa pi r l", pi * 8 * 12, 96 * pi)
eq("s1 csa sf", sf(96 * pi), 302)
# stretch 2
for r in (1, 2.5, 4):
    eq("s2 seg", 0.5 * r * r * (pi / 2 - sin(pi / 2)), r * r * (pi - 2) / 4); eq("s2 chord", 2 * r * sin(pi / 4), r * sqrt(2), 1e-9)
    eq("s2 pct", sf(100 * ((pi - 2) / 4) / pi), 9.08); eq("s2 frac", (r * r * (pi - 2) / 4) / (pi * r * r), (pi - 2) / (4 * pi))
eq("quiz arc", 36 - 20, 16); eq("quiz area", 0.5 * 16 * pi / 2, 4 * pi); eq("quiz arc2", 4 * pi / 2, 2 * pi)
print("ok")
