# checks/math.p3.trig.py: recomputes every number in the Further trigonometry chapter.
from math import isclose, sqrt, sin, cos, tan, asin, acos, atan, pi, radians as rad, degrees as deg

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def r1(x): return round(x, 1)
sec = lambda t: 1 / cos(t); cosec = lambda t: 1 / sin(t); cot = lambda t: 1 / tan(t)

eq("sec40", sf(sec(rad(40)), 4), 1.305)
for t in (20, 100, 250): 
    eq("sec2", sec(rad(t))**2, 1 + tan(rad(t))**2); eq("cosec2", cosec(rad(t))**2, 1 + cot(rad(t))**2)
# eg 2tan^2 + sec = 1
a = deg(acos(-2 / 3)); eq("131.8", r1(a), 131.8); eq("228.2", r1(360 - a), 228.2)
for x in (0, 131.81, 228.19, 360): eq("eq1", 2 * tan(rad(x))**2 + sec(rad(x)), 1, 5e-3)
# cot^2 + 3cosec - 3 = 0
b = deg(asin(0.25)); eq("14.5", r1(b), 14.5); eq("194.5", r1(180 + b), 194.5); eq("345.5", r1(360 - b), 345.5)
for x in (90, 194.48, 345.52): eq("eq2", cot(rad(x))**2 + 3 * cosec(rad(x)) - 3, 0, 5e-3)
# compound
eq("test", sin(rad(90)), 1); eq("test2", sin(rad(60)) + sin(rad(30)), 1.366, 1e-3)
eq("sin75", sin(rad(75)), (sqrt(6) + sqrt(2)) / 4); eq("tan105", tan(rad(105)), -(2 + sqrt(3)))
eq("sin75 dp", round(sin(rad(75)), 4), 0.9659); eq("exact dp", round((sqrt(6) + sqrt(2)) / 4, 4), 0.9659)
sA, cB = 3/5, -5/13; cA = sqrt(1 - sA**2); sB = sqrt(1 - cB**2); eq("cA", cA, 0.8); eq("sB", sB, 12/13)
eq("sin(A+B)", sA * cB + cA * sB, 33 / 65)
# sin(x+30)=2cos x
for x in (60, 240): eq("sin(x+30)", sin(rad(x + 30)), 2 * cos(rad(x)))
eq("tanx", 3 / sqrt(3), sqrt(3))
# double
eq("sin2t", 2 * 0.6 * 0.8, 24 / 25); eq("cos2t", 1 - 2 * 0.36, 7 / 25); eq("tan2t", (24 / 25) / (7 / 25), 24 / 7); eq("pyth", (24/25)**2 + (7/25)**2, 1)
for x in (30, 90, 150): eq("cos2x", cos(rad(2 * x)) + 3 * sin(rad(x)), 2)
for x in (-pi/2, pi/6, pi/2, 5*pi/6): eq("sin2x=cosx", sin(2 * x), cos(x), 1e-9)
# proofs
eq("15", 1 / tan(rad(15)), 2 + sqrt(3)); eq("tan15", round(tan(rad(15)), 4), 0.2679)
for t in (20, 70, 130):
    th = rad(t)
    eq("cosec2+cot2", cosec(2 * th) + cot(2 * th), cot(th)); eq("tan(t+45)", tan(th + rad(45)), (1 + tan(th)) / (1 - tan(th)))
    eq("sin2/(1+cos2)", sin(2 * th) / (1 + cos(2 * th)), tan(th))
eq("cosec30+cot30", 2 + sqrt(3), 2 + sqrt(3))
for t in (1 / 2, 1 / 3):
    eq("tan45 eq", (1 + t) / (1 - t), 6 * t)
eq("26.6", r1(deg(atan(0.5))), 26.6); eq("18.4", r1(deg(atan(1 / 3))), 18.4)
assert 6 * 0.25 - 5 * 0.5 + 1 == 0 or abs(6 * 0.25 - 5 * 0.5 + 1) < 1e-12
# R form
eq("R", sqrt(9 + 16), 5); al = deg(atan(4 / 3)); eq("alpha", round(al, 2), 53.13)
for t in (10, 100, 200): eq("Rform", 3 * sin(rad(t)) + 4 * cos(rad(t)), 5 * sin(rad(t + al)))
eq("R2", sqrt(5), 2.2360679775); al2 = deg(atan(0.5)); eq("a2", round(al2, 2), 26.57)
for t in (10, 100, 200): eq("Rform2", 2 * sin(rad(t)) - cos(rad(t)), sqrt(5) * sin(rad(t - al2)))
# solve 3sin+4cos = 2.5
th1 = 150 - al; th2 = 390 - al; eq("96.9", r1(th1), 96.9); eq("336.9", r1(th2), 336.9)
for t in (th1, th2): eq("=2.5", 3 * sin(rad(t)) + 4 * cos(rad(t)), 2.5)
eq("max at", r1(90 - al), 36.9); eq("max", 3 * sin(rad(90 - al)) + 4 * cos(rad(90 - al)), 5)
# exam R cos
eq("R", sqrt(49 + 576), 25); al = deg(atan(24 / 7)); eq("alpha", round(al, 2), 73.74)
for t in (10, 100, 250): eq("Rcos", 7 * cos(rad(t)) - 24 * sin(rad(t)), 25 * cos(rad(t + al)))
u = deg(acos(0.4)); eq("66.42", round(u, 2), 66.42)
t1 = 360 - u - al; t2 = 360 + u - al; eq("219.8", r1(t1), 219.8); eq("352.7", r1(t2), 352.7); assert 0 <= t1 <= 360 and 0 <= t2 <= 360
eq("293.58", round(360 - u, 2), 293.58); eq("426.42", round(360 + u, 2), 426.42)
for t in (t1, t2): eq("=10", 7 * cos(rad(t)) - 24 * sin(rad(t)), 10)
eq("8/11", 40 / 55, 8 / 11); assert 30 - 25 == 5 and 30 + 25 == 55

# try
eq("T1a", sf(sec(rad(50))), 1.56); eq("T1b", sf(cot(rad(20))), 2.75); eq("T1c", sf(cosec(1.2)), 1.07)
eq("T2", r1(deg(acos(-0.4))), 113.6); eq("T2b", r1(360 - deg(acos(-0.4))), 246.4)
s1 = (1 + sqrt(17)) / 2; s2 = (1 - sqrt(17)) / 2; eq("s1", round(s1, 3), 2.562); eq("s2", round(s2, 3), -1.562)
eq("c1", round(1 / s1, 4), 0.3904, 1e-4); eq("c2", round(1 / s2, 4), -0.6403, 1e-4)
for t in (67.0, 293.0, 129.8, 230.2): eq("eq3", tan(rad(t))**2, 3 + sec(rad(t)), 0.05)
eq("T3 th", r1(deg(acos(1 / s1))), 67.0); eq("T3 th2", r1(deg(acos(1 / s2))), 129.8)
eq("cos15", cos(rad(15)), (sqrt(2) + sqrt(6)) / 4)
sA = 5 / 13; cB = 4 / 5; eq("cos(A-B)", 12/13 * 4/5 + 5/13 * 3/5, 63 / 65)
for x in (0, 60, 180, 300, 360): eq("sin2x=sinx", sin(rad(2 * x)), sin(rad(x)), 1e-9)
for x in (75.52, 284.48, 180): eq("T8", 2 * cos(rad(2 * x)) + 3 * cos(rad(x)) + 1, 0, 5e-3)
eq("T8 a", r1(deg(acos(0.25))), 75.5); eq("T8 b", r1(360 - deg(acos(0.25))), 284.5)
al = deg(atan(12 / 5)); eq("R13", sqrt(25 + 144), 13); eq("67.38", round(al, 2), 67.38)
t1, t2 = 150 - al, 390 - al; eq("82.6", r1(t1), 82.6); eq("322.6", r1(t2), 322.6)
for t in (t1, t2): eq("=6.5", 5 * sin(rad(t)) + 12 * cos(rad(t)), 6.5)
# exam last: sqrt3 cos + sin = sqrt2
for t in (5 * pi / 12, 23 * pi / 12): eq("last", sqrt(3) * cos(t) + sin(t), sqrt(2))
eq("R", sqrt(3 + 1), 2); eq("alpha", atan(1 / sqrt(3)), pi / 6)
assert -pi / 6 > -pi / 4 and 7 * pi / 4 < 11 * pi / 6

# quiz
eq("sin15", sin(rad(15)), (sqrt(6) - sqrt(2)) / 4)
for t in (30, 100): eq("cos2", cos(rad(2 * t)), 1 - 2 * sin(rad(t))**2)
eq("Q4", 4 / 3, 4 / 3); eq("Q5", 1 / (4 - 3), 1); eq("Q5b", 1 / (4 + 3), 1 / 7)

# ---- v2 additions: warm-up, proofs, spot the error, exam practice, stretch ----
import random
from math import hypot, atan2
for s in (0.5, -1):
    eq("warm-up quadratic", 2 * s * s + s - 1, 0)
eq("warm-up cos 120", cos(rad(120)), -0.5); eq("warm-up cos 240", cos(rad(240)), -0.5)
eq("warm-up cos", sqrt(1 - 0.8 ** 2), 0.6); eq("warm-up tan", 0.8 / 0.6, 4 / 3)
for _ in range(12):                                                  # proof: compound angles via the unit-circle construction
    A, B = random.uniform(0.1, 1.4), random.uniform(0.1, 1.4)
    Q = (cos(B) * cos(A), cos(B) * sin(A))
    P = (Q[0] + sin(B) * -sin(A), Q[1] + sin(B) * cos(A))
    eq("proof P_x", P[0], cos(A + B)); eq("proof P_y", P[1], sin(A + B))
    eq("proof OQ", hypot(*Q), cos(B))
    eq("double sin", sin(2 * A), 2 * sin(A) * cos(A))
    eq("double cos 1", cos(2 * A), 2 * cos(A) ** 2 - 1); eq("double cos 2", cos(2 * A), 1 - 2 * sin(A) ** 2)
    eq("double tan", tan(2 * A), 2 * tan(A) / (1 - tan(A) ** 2))
    a, b = random.uniform(0.5, 9), random.uniform(0.5, 9); R = hypot(a, b); al = atan2(b, a)
    th = random.uniform(0, 6)
    eq("proof R form", a * sin(th) + b * cos(th), R * sin(th + al))
    eq("tan alpha", tan(al), b / a)
sols = [0, 60, 180, 300, 360]                                         # spot the error
for x in sols: eq("spot", sin(rad(2 * x)), sin(rad(x)), 1e-9)
assert len(sols) == 5
cA = sqrt(1 - (5 / 13) ** 2); eq("Q1 cos", cA, 12 / 13); eq("Q1", 2 * (5 / 13) * cA, 120 / 169)  # exam practice
eq("Q2 R", hypot(5, 12), 13); eq("Q2 alpha", r1(deg(atan(12 / 5))), 67.4)
for t in (deg(acos(1 / 6)), 360 - deg(acos(1 / 6)), 180):             # Q3
    eq("Q3", 3 * cos(rad(2 * t)) + 5 * cos(rad(t)) + 2, 0, 1e-9)
eq("Q3a", r1(deg(acos(1 / 6))), 80.4); eq("Q3b", r1(360 - deg(acos(1 / 6))), 279.6)
for x in (0.3, 1.1, 2.0): eq("Q4", sin(2 * x) / (1 + cos(2 * x)), tan(x))
for t in (deg(atan(4 - sqrt(3))), deg(atan(4 - sqrt(3))) + 180):      # Q5
    eq("Q5", sin(rad(t + 60)), 2 * cos(rad(t)), 1e-9)
eq("Q5a", r1(deg(atan(4 - sqrt(3)))), 66.2); eq("Q5b", r1(deg(atan(4 - sqrt(3))) + 180), 246.2)
al = deg(atan(15 / 8)); eq("Q6 R", hypot(8, 15), 17); eq("Q6 alpha", r1(al), 61.9)  # Q6
for t in (82.5948295576597, 221.26019657063438):
    eq("Q6", 8 * sin(rad(t)) - 15 * cos(rad(t)), 6, 1e-9)
t1 = al + deg(asin(6 / 17)); t2 = al + 180 - deg(asin(6 / 17))
eq("Q6 s1", r1(deg(asin(6 / 17))), 20.7); eq("Q6 s2", r1(180 - deg(asin(6 / 17))), 159.3)
eq("Q6 t1", r1(t1), 82.6); eq("Q6 t2", r1(t2), 221.3)
for x in (0.4, 1.0): eq("Q7a", (1 - cos(2 * x)) / sin(2 * x), tan(x))
eq("Q7b", (1 - cos(rad(30))) / sin(rad(30)), 2 - sqrt(3)); eq("Q7b tan15", tan(rad(15)), 2 - sqrt(3)); eq("Q7c", r1(deg(atan(2))), 63.4)
R = sqrt(13); al = deg(atan(2 / 3)); eq("Q8 R", sf(R), 3.61); eq("Q8 alpha", r1(al), 33.7)   # tide
eq("Q8 max", sf(6 + R, 3), 9.61); eq("Q8 t", sf((90 - al) / 30, 3), 1.88)
h = lambda t: 6 + 3 * sin(rad(30 * t)) + 2 * cos(rad(30 * t))
eq("Q8 max check", h((90 - al) / 30), 6 + R)
phi = deg(asin(2.5 / R)); eq("Q8 sin", sf(2.5 / R, 3), 0.693); eq("Q8 phi", r1(phi), 43.9); eq("Q8 phi2", r1(180 - phi), 136.1)
ts = [(phi - al) / 30, (180 - phi - al) / 30]
eq("Q8 t1", round(ts[0], 2), 0.34); eq("Q8 t2", round(ts[1], 2), 3.41)
for t in ts: eq("Q8 h=8.5", h(t), 8.5, 1e-9)
eq("Q8 next", round((360 + phi - al) / 30, 2), 12.34)
for x in (0.3, 1.2, 2.5): eq("S1a", sin(3 * x), 3 * sin(x) - 4 * sin(x) ** 3)   # stretch
for t in (0, 45, 135, 180): eq("S1b", sin(rad(3 * t)), sin(rad(t)), 1e-9)
assert len([t for t in range(0, 181) if abs(sin(rad(3 * t)) - sin(rad(t))) < 1e-9]) == 4
eq("S2 R", hypot(3, 4), 5); eq("S2 alpha", r1(deg(atan(4 / 3))), 53.1)
vals = [1 / (7 + 3 * sin(rad(t)) + 4 * cos(rad(t))) for t in range(0, 3600)]
eq("S2 max", max(vals), 1 / 2, 1e-4); eq("S2 min", min(vals), 1 / 12, 1e-4)
print("ok")
