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
print("ok")
