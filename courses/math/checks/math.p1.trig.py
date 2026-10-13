# checks/math.p1.trig.py: recomputes every number in the Trigonometry chapter.
from math import isclose, sqrt, sin, cos, tan, asin, acos, atan, pi, radians as rad, degrees as deg

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def r1(x): return round(x, 1)

# exact values at related angles
eq("sin150", sin(rad(150)), 0.5); eq("cos240", cos(rad(240)), -0.5); eq("tan135", tan(rad(135)), -1)
eq("cos5pi/6", cos(5 * pi / 6), -sqrt(3) / 2)
for t, s_, c_, t_ in ((0, 0, 1, 0), (30, .5, sqrt(3)/2, sqrt(3)/3), (45, sqrt(2)/2, sqrt(2)/2, 1), (60, sqrt(3)/2, .5, sqrt(3))):
    eq(f"sin{t}", sin(rad(t)), s_); eq(f"cos{t}", cos(rad(t)), c_); eq(f"tan{t}", tan(rad(t)), t_)
eq("sin90", sin(pi/2), 1); eq("cos90", cos(pi/2), 0, 1e-12)
# signs by quadrant
for a in (45, 135, 225, 315):
    sg = (sin(rad(a)) > 0, cos(rad(a)) > 0, tan(rad(a)) > 0)
    assert sg == {45: (1, 1, 1), 135: (1, 0, 0), 225: (0, 0, 1), 315: (0, 1, 0)}[a]
# related angle identities
for th in (10, 25, 70):
    eq("sin(180-t)", sin(rad(180 - th)), sin(rad(th))); eq("cos(360-t)", cos(rad(360 - th)), cos(rad(th)))
    eq("tan(180+t)", tan(rad(180 + th)), tan(rad(th))); eq("sin(-t)", sin(rad(-th)), -sin(rad(th)))
    eq("cos(-t)", cos(rad(-th)), cos(rad(th))); eq("tan(-t)", tan(rad(-th)), -tan(rad(th)))
    eq("pyth", sin(rad(th))**2 + cos(rad(th))**2, 1)

# exam: f(x)=1-cos2x
for x in (45, 135, 225, 315): eq("f=1", 1 - cos(rad(2 * x)), 1)
vals = [1 - cos(rad(2 * x)) for x in range(0, 361)]; eq("min", min(vals), 0); eq("max", max(vals), 2)

# principal values
eq("asin-.5", deg(asin(-0.5)), -30); eq("acos-.5", deg(acos(-0.5)), 120); eq("atan1", deg(atan(1)), 45)

# solving
a = deg(asin(0.7)); eq("a1", r1(a), 44.4); eq("a2", r1(180 - a), 135.6)
a = deg(acos(-0.3)); eq("b1", r1(a), 107.5); eq("b2", r1(360 - a), 252.5)
a = deg(atan(-2)); eq("c0", r1(a), -63.4); eq("c1", r1(a + 180), 116.6); eq("c2", r1(a + 360), 296.6)
# sin2x = .5
xs = sorted(x for x in range(0, 361) if abs(sin(rad(2 * x)) - 0.5) < 1e-9); assert xs == [15, 75, 195, 255], xs
# cos 2x = .3
a = deg(acos(0.3)); eq("72.5", r1(a), 72.5)
u = [a, 360 - a, 360 + a, 720 - a]
eq("b", [r1(v / 2) for v in u][0], 36.3); eq("b", r1(u[1] / 2), 143.7); eq("b", r1(u[2] / 2), 216.3); eq("b", r1(u[3] / 2), 323.7)
eq("287.5", r1(360 - a), 287.5); eq("432.5", r1(360 + a), 432.5); eq("647.5", r1(720 - a), 647.5)
# sin(x-20)=.4
a = deg(asin(0.4)); eq("23.6", r1(a), 23.6); eq("156.4", r1(180 - a), 156.4); eq("x1", r1(a + 20), 43.6); eq("x2", r1(180 - a + 20), 176.4)
# radians
for x in (0, 2 * pi / 3, 2 * pi): eq("sin(x+pi/6)", sin(x + pi / 6), 0.5)

# equations with identities
for x in (120, 240): eq("2sin2+3cos", 2 * sin(rad(x))**2 + 3 * cos(rad(x)), 0)
eq("check 120", 2 * 0.75 + 3 * -0.5, 0)
for x in (0, 60, 180, 300, 360): eq("tan=2sin", tan(rad(x)), 2 * sin(rad(x)), 1e-9)
for x in (30, 150): eq("3tan=2cos", 3 * tan(rad(x)), 2 * cos(rad(x)))
assert abs(3 * tan(rad(90 - 1e-9))) > 1e6  # sanity
# exam identity: lhs = 2/sin
for th in (20, 100, 250, 330):
    t = rad(th); eq("id", sin(t) / (1 + cos(t)) + (1 + cos(t)) / sin(t), 2 / sin(t), 1e-9)
for th in (30, 150): t = rad(th); eq("=4", sin(t) / (1 + cos(t)) + (1 + cos(t)) / sin(t), 4)
# simplifications
for th in (20, 100, 250):
    t = rad(th)
    eq("simp a", sin(t) * cos(t) / tan(t), cos(t)**2); eq("simp b", sin(t)**2 / (1 - cos(t)**2), 1)
    eq("sin4-cos4", sin(t)**4 - cos(t)**4, sin(t)**2 - cos(t)**2)
    eq("prove tan", tan(t) + 1 / tan(t), 1 / (sin(t) * cos(t)))
    eq("cos2/(1-sin)", cos(t)**2 / (1 - sin(t)), 1 + sin(t))

# try questions
eq("T1a", sin(rad(300)), -sqrt(3) / 2); eq("T1b", cos(2 * pi / 3), -0.5); eq("T1c", tan(rad(210)), sqrt(3) / 3)
eq("T2b", 360 / 3, 120)
eq("T3a", 180 + 30, 210); eq("T3b", r1(deg(acos(0.6))), 53.1); eq("T3b2", r1(360 - deg(acos(0.6))), 306.9)
a = deg(atan(1.5)); eq("T4", r1(a), 56.3)
eq("T4 x1", r1(a / 3), 18.8); eq("T4 x2", r1((a + 180) / 3), 78.8); eq("T4 x3", r1((a + 360) / 3), 138.8)
for x in (pi / 6, pi / 2): eq("T5", cos(x - pi / 3), sqrt(3) / 2)
a = deg(asin(-1 / 3)); eq("T7 s", r1(180 - a), 199.5); eq("T7 s2", r1(360 + a), 340.5)
for x in (199.47, 340.53, 30, 150): eq("T7 eq", 6 * cos(rad(x))**2 + sin(rad(x)), 5, 5e-3)
c = (1 - sqrt(2)) / 2; eq("T9 c", round(c, 4), -0.2071); eq("T9 cp", round((1 + sqrt(2)) / 2, 3), 1.207)
eq("T9 th", r1(deg(acos(c))), 102.0); eq("T9 th2", r1(360 - deg(acos(c))), 258.0)
for th in (102.0, 258.0): eq("T9 eq", 4 * sin(rad(th))**2, 3 - 4 * cos(rad(th)), 5e-3)
eq("T9 formula", sqrt(32), 4 * sqrt(2))

# quiz
eq("Q1", sin(rad(150)), 0.5); eq("Q2", r1(deg(asin(0.3))), 17.5); eq("Q2b", r1(180 - deg(asin(0.3))), 162.5)
eq("Q3", 360 / 3, 120); eq("Q3 w", 360 * 3, 1080)
# FIX additions: negative intervals
a = deg(asin(-2 / 3)); eq("neg1", r1(a), -41.8); eq("neg2", r1(-180 - a), -138.2)
for x in (-41.8, -138.2): eq("3sin=-2", 3 * sin(rad(x)), -2, 0.01)
xs = [pi / 6, -pi / 6, 5 * pi / 6, -5 * pi / 6]
for x in xs: eq("2cos2x=1", 2 * cos(2 * x), 1)
assert len([x for x in range(-180, 181) if abs(sin(rad(x)) + 2 / 3) < 0.01]) >= 2
# v2: warm-up
eq("w1", 10 * sin(rad(30)), 5); eq("w2", 120 * pi / 180, 2 * pi / 3)

# v2: proofs. exact values from the triangles, and the two identities at random angles
eq("45 hyp", sqrt(1 + 1), sqrt(2)); eq("sin45", sin(rad(45)), 1 / sqrt(2)); eq("tan45", tan(rad(45)), 1)
eq("30 height", sqrt(4 - 1), sqrt(3)); eq("sin30", sin(rad(30)), 0.5); eq("cos30", cos(rad(30)), sqrt(3) / 2); eq("tan30", tan(rad(30)), 1 / sqrt(3))
eq("sin60", sin(rad(60)), sqrt(3) / 2); eq("cos60", cos(rad(60)), 0.5); eq("tan60", tan(rad(60)), sqrt(3))
for t in (-200, -45, 10, 130, 250, 333, 500):
    eq("pyth", sin(rad(t)) ** 2 + cos(rad(t)) ** 2, 1); eq("tan id", sin(rad(t)) / cos(rad(t)), tan(rad(t)), 1e-9)

# v2: spot the error: cos 2x = -0.6 on [0, 360]
a = deg(acos(-0.6))
eq("spot a", round(a, 1), 126.9); eq("spot b", round(360 - a, 1), 233.1)
vals = [a, 360 - a, a + 360, 360 - a + 360]
xs = [round(v / 2, 1) for v in vals]
assert xs == [63.4, 116.6, 243.4, 296.6], xs
for x in xs: eq("spot root", cos(rad(2 * x)), -0.6, 5e-3)
# four crossings of y = -0.6 by cos 2x on [0, 360]
cnt = sum(1 for i in range(0, 3600) if (cos(rad(2 * i / 10)) + 0.6) * (cos(rad(2 * (i + 1) / 10)) + 0.6) < 0)
eq("spot crossings", cnt, 4)

# v2: exam practice
eq("x1a", sin(rad(135)), sqrt(2) / 2); eq("x1b", cos(rad(240)), -0.5); eq("x1c", tan(rad(330)), -1 / sqrt(3)); eq("x1c2", -1 / sqrt(3), -sqrt(3) / 3)
eq("x2", round(deg(acos(-0.75)), 1), 138.6); eq("x2b", round(360 - deg(acos(-0.75)), 1), 221.4)
t0 = deg(atan(1.5)); eq("x3 a", round(t0, 1), 56.3); eq("x3 b", round(t0 + 180, 1), 236.3)
eq("x3 x1", round((t0 + 30) / 2, 1), 43.2); eq("x3 x2", round((t0 + 180 + 30) / 2, 1), 133.2)
for x in (43.155, 133.155): eq("x3 check", tan(rad(2 * x - 30)), 1.5, 1e-3)
for th, ok in ((90, True), (210, True), (330, True)): eq("x4", 2 * cos(rad(th)) ** 2 + sin(rad(th)), 1, 1e-9)
for s in (-2, 0.3, 1): eq("x4 poly", 2 - 2 * s * s + s - 1, -(2 * s * s - s - 1))
eq("x4 fact", (2 * -0.5 + 1) * (-0.5 - 1), 0)
for t in (10, 100, 250): eq("x5", tan(rad(t)) + 1 / tan(rad(t)), 1 / (sin(rad(t)) * cos(rad(t))), 1e-9)
f6 = lambda x: 3 - 2 * cos(rad(2 * x))
eq("x6 max", max(f6(i) for i in range(0, 361)), 5); eq("x6 min", min(f6(i) for i in range(0, 361)), 1)
for x in (60, 120, 240, 300): eq("x6 f=4", f6(x), 4, 1e-9)
cnt = sum(1 for i in range(0, 3600) if (f6(i / 10) - 4) * (f6((i + 1) / 10) - 4) < 0); eq("x6 count", cnt, 4)
for x in (-pi, -pi / 3, pi / 3, pi): eq("x7", 2 * sin(x) ** 2, 1 + cos(x), 1e-9)
for c in (-0.9, 0.2, 1.4): eq("x7 poly", 2 * (1 - c * c) - (1 + c), -(2 * c * c + c - 1))
for t in (30, 150, 199.47122, 340.52878):
    eq("x8", 6 * cos(rad(t)) ** 2 + sin(rad(t)), 5, 1e-6)
eq("x8 199.5", round(180 + deg(asin(1 / 3)), 1), 199.5); eq("x8 340.5", round(360 - deg(asin(1 / 3)), 1), 340.5)
for s in (-1, 0.4, 2): eq("x8 poly", 6 * (1 - s * s) + s - 5, -(6 * s * s - s - 1)); eq("x8 fact", (3 * s + 1) * (2 * s - 1), 6 * s * s - s - 1)
# stretch 1
good = [x for x in (0, 90, 180, 270, 360) if abs(sin(rad(x)) + cos(rad(x)) - 1) < 1e-9]
assert good == [0, 90, 360], good
eq("s1 identity", (sin(rad(33)) + cos(rad(33))) ** 2, 1 + sin(rad(66)))
# stretch 2
for x in (26.565051, 45):
    eq("s2", 2 * sin(rad(x)) ** 2 - 3 * sin(rad(x)) * cos(rad(x)) + cos(rad(x)) ** 2, 0, 1e-8)
eq("s2 a", round(deg(atan(0.5)), 1), 26.6); eq("s2 cos0", 2 * 1 - 0 + 0, 2)
print("ok")
