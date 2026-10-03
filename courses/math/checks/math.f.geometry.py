# checks/math.f.geometry.py: recomputes every number in the Geometry and trigonometry basics chapter.
from math import isclose, sqrt, sin, cos, tan, asin, acos, atan, radians as rad, degrees as deg, pi

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def dp(x, n=1): return round(x, n)

# polygons
eq("15 sides", 360 / (180 - 156), 15); eq("hexagon", (6 - 2) * 180, 720)
eq("octagon ext", 360 / 8, 45); eq("octagon int", 180 - 45, 135)
eq("18 sides", 360 / 20, 18)

# Pythagoras
eq("isosceles h", sqrt(13**2 - 5**2), 12); eq("area", 0.5 * 10 * 12, 60)
assert 3**2 + 4**2 == 5**2 and 5**2 + 12**2 == 13**2 and 8**2 + 15**2 == 17**2 and 7**2 + 24**2 == 25**2
eq("41", sqrt(81 + 1600), 41); eq("15", sqrt(289 - 64), 15)

# SOHCAHTOA
eq("12 sin 35", sf(12 * sin(rad(35))), 6.88)
eq("atan 7/9", dp(deg(atan(7 / 9))), 37.9)
eq("tower", sf(40 * tan(rad(28))), 21.3)

# exact values
eq("sin30", sin(rad(30)), 1 / 2); eq("cos30", cos(rad(30)), sqrt(3) / 2); eq("tan30", tan(rad(30)), 1 / sqrt(3))
eq("sin45", sin(rad(45)), sqrt(2) / 2); eq("cos45", cos(rad(45)), sqrt(2) / 2); eq("tan45", tan(rad(45)), 1)
eq("sin60", sin(rad(60)), sqrt(3) / 2); eq("cos60", cos(rad(60)), 1 / 2); eq("tan60", tan(rad(60)), sqrt(3))
eq("1/sqrt3 = sqrt3/3", 1 / sqrt(3), sqrt(3) / 3)
eq("T5", sin(rad(45)) * cos(rad(45)) + tan(rad(60)) * tan(rad(30)), 1.5)

# sine and cosine rules
b = 8.5 * sin(rad(71)) / sin(rad(42)); eq("b", sf(b), 12.0); eq("b raw", round(b, 2), 12.01)
eq("C", 180 - 42 - 71, 67); eq("c", sf(8.5 * sin(rad(67)) / sin(rad(42))), 11.7)
a2 = 7**2 + 9**2 - 2 * 7 * 9 * cos(rad(62)); eq("a2", round(a2, 2), 70.85); eq("a", sf(sqrt(a2), 3), 8.42)
eq("130-126cos", 130 - 126 * cos(rad(62)), a2)
cC = (5**2 + 7**2 - 10**2) / (2 * 5 * 7); eq("cosC", round(cC, 4), -0.3714); eq("C", dp(deg(acos(cC))), 111.8)
# ambiguous
sB = 10 * sin(rad(40)) / 8; eq("sinB", round(sB, 4), 0.8035)
B1 = deg(asin(sB)); eq("B1", dp(B1), 53.5); eq("B2", dp(180 - B1), 126.5); assert 40 + 180 - B1 < 180

# exam: ABC
BC2 = 8**2 + 11**2 - 2 * 8 * 11 * cos(rad(58)); BC = sqrt(BC2)
eq("185-176", 185 - 176 * cos(rad(58)), BC2); eq("BC2", round(BC2, 2), 91.73); eq("BC", sf(BC), 9.58)
cB = (BC**2 + 8**2 - 11**2) / (2 * BC * 8); eq("cosB", round(cB, 4), 0.2267); eq("B", dp(deg(acos(cB))), 76.9)
eq("area", sf(0.5 * 8 * 11 * sin(rad(58))), 37.3)
sinB = 11 * sin(rad(58)) / BC; eq("sinB", round(sinB, 3), 0.974); eq("B asin", dp(deg(asin(sinB))), 76.9); eq("B obtuse", dp(180 - deg(asin(sinB))), 103.1)

# exam: tower with 30 and 45
x = 50 / (sqrt(3) - 1); eq("x", x, 25 * (sqrt(3) + 1)); eq("h", sf(x), 68.3)
eq("x/(x+50)", x / (x + 50), 1 / sqrt(3)); eq("rationalise", 50 * (sqrt(3) + 1) / (3 - 1), 25 * (sqrt(3) + 1))

# circles
eq("PT", sqrt(13**2 - 5**2), 12); eq("semicircle", 180 - 90 - 35, 55)

# arcs and solids
eq("arc", sf(75 / 360 * 2 * pi * 8), 10.5); eq("arc raw", round(75 / 360 * 2 * pi * 8, 2), 10.47)
eq("sector", sf(75 / 360 * pi * 64), 41.9); eq("sector raw", round(75 / 360 * pi * 64, 2), 41.89)
eq("slant", sqrt(36 + 64), 10); eq("CSA", sf(pi * 6 * 10), 188); eq("CSA 60pi", 60 * pi, pi * 6 * 10)
eq("V", sf(pi * 36 * 8 / 3), 302); eq("96pi", 96 * pi, pi * 36 * 8 / 3)

# try questions
eq("T3a", sf(15 * sin(rad(40))), 9.64); eq("T3b", dp(deg(asin(5 / 9))), 33.7)
eq("T4 angle", dp(deg(acos(1.5 / 5))), 72.5); eq("T4 h", sf(sqrt(25 - 2.25)), 4.77)
eq("T6", dp(deg(acos((36 + 64 - 121) / (2 * 6 * 8)))), 102.6); eq("T6 frac", (36 + 64 - 121) / 96, -21 / 96)
eq("T7", sf(0.5 * 7 * 9 * sin(rad(125))), 25.8)
eq("T8 PT", sqrt(625 - 49), 24); eq("T8 angle", dp(15 / (2 * pi * 12) * 360), 71.6)
sC = 12 * sin(rad(40)) / 9; eq("T9 sinC", round(sC, 3), 0.857); C1 = deg(asin(sC))
eq("T9 C1", dp(C1), 59.0); eq("T9 C2", dp(180 - C1), 121.0)
B = 180 - 40 - dp(C1); eq("T9 B", B, 81.0); eq("T9 area", sf(0.5 * 12 * 9 * sin(rad(B))), 53.3)

# quiz
eq("Q1", tan(rad(60)), sqrt(3))
eq("Q4 slant", sqrt(9 + 16), 5); eq("Q4 CSA", pi * 3 * 5, 15 * pi)
eq("Q5", 25 + 49 - 2 * 5 * 7 * 0.2, 60); eq("Q5 plus", 74 + 14, 88); eq("Q5 no 2", 74 - 35 * 0.2, 67); eq("Q5 wrong", 74 * 0.8, 59.2)
print("ok")
