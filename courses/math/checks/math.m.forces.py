# checks/math.m.forces.py: recomputes every number in the Forces and equilibrium chapter (g = 10).
from math import isclose, sin, cos, tan, atan, atan2, asin, radians, degrees, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

d = radians
g = 10

eq("5 kg weight", 5 * g, 50); eq("5 kg with 9.8", 5 * 9.8, 49)

# Resolving 20 N at 30 degrees
eq("horizontal", sf(20 * cos(d(30))), 17.3); eq("vertical", 20 * sin(d(30)), 10.0)
eq("check", round(sqrt(17.3 ** 2 + 10 ** 2), 1), 20.0, 0.05)

# Resultant of P = 12 and Q = 10 at 60 degrees above negative x-axis
qx, qy = -10 * cos(d(60)), 10 * sin(d(60))
eq("qx", qx, -5); eq("qy", round(qy, 2), 8.66)
X, Y = 12 + qx, qy
eq("X", X, 7); eq("|R|^2", round(X * X + Y * Y), 124); eq("|R|", sf(sqrt(X * X + Y * Y)), 11.1)
eq("alpha", round(degrees(atan2(Y, X)), 1), 51.1)

# Two strings, 5 kg
# solve directly: T1 cos30 = T2 cos60, T1 sin30 + T2 sin60 = 50
T1 = 50 / (sin(d(30)) + cos(d(30)) / cos(d(60)) * sin(d(60)))
T2 = T1 * cos(d(30)) / cos(d(60))
eq("T1", T1, 25); eq("T2/T1", T2 / T1, sqrt(3)); eq("T2", sf(T2), 43.3)

# Friction warning: 10 kg, mu 0.4
eq("R", 10 * g, 100); eq("max friction", 0.4 * 100, 40)

# Crate pulled at 30 degrees, about to slide
T = 40 / (cos(d(30)) + 0.2)
eq("denominator", round(cos(d(30)) + 0.2, 4), 1.0660); eq("T", sf(T), 37.5)
R = 100 - 0.5 * T; eq("R", sf(R), 81.2)
eq("limiting check", T * cos(d(30)), 0.4 * R, 1e-9)

# Exam-style slope: sin = 0.6, cos = 0.8, mu = 0.5, m = 5
R = 50 * 0.8; Fmax = 0.5 * R; down = 50 * 0.6
eq("R", R, 40); eq("Fmax", Fmax, 20); eq("down", down, 30)
eq("least P", down - Fmax, 10); eq("greatest P", down + Fmax, 50)

# Try it yourself
eq("t1 h", sf(50 * cos(d(40))), 38.3); eq("t1 v", sf(50 * sin(d(40))), 32.1)
eq("t2", 2.5 * g, 25)
eq("t3 R", 8 * g, 80); eq("t3 max", 0.25 * 80, 20); eq("t3 contact", sf(sqrt(80 ** 2 + 15 ** 2)), 81.4)
eq("t4 T", 60 * sin(d(30)), 30); eq("t4 R", sf(60 * cos(d(30))), 52.0)
eq("t5 mu", sf(tan(d(20))), 0.364)
eq("t6 F", sqrt(36 + 64), 10); a = degrees(atan(6 / 8)); eq("t6 angle", round(a, 1), 36.9)
eq("t6 opposite", round(180 - round(a, 1), 1), 143.1)
P = 40 * tan(d(30)); eq("t7 P", sf(P), 23.1)
eq("t7 parts", round(40 * cos(d(30)), 2), 34.64); eq("t7 parts b", round(P * sin(d(30)), 2), 11.55)
eq("t7 R", sf(40 * cos(d(30)) + P * sin(d(30))), 46.2)
# t8: P cos30 = 30 sin30 + 0.2 (30 cos30 + P sin30)
P = (30 * sin(d(30)) + 0.2 * 30 * cos(d(30))) / (cos(d(30)) - 0.2 * sin(d(30)))
eq("t8 30cos30", round(30 * cos(d(30)), 2), 25.98); eq("t8 0.2*25.98", round(0.2 * 30 * cos(d(30)), 3), 5.196)
eq("t8 coeff", round(cos(d(30)) - 0.1, 4), 0.7660); eq("t8 P", sf(P), 26.4)

# Quiz
eq("quiz max friction", 0.5 * 60, 30)
# ---- v2 additions ----
# warm-up
eq("w sin30", sin(d(30)), 0.5); eq("w cos30", cos(d(30)), sqrt(3) / 2); eq("w tan60", tan(d(60)), sqrt(3))
eq("w sim y", 2, 2); assert 2 * 3 + 3 * 2 == 12 and 3 - 2 == 1
eq("w tri", sqrt(13 ** 2 - 5 ** 2), 12); eq("w ang", round(degrees(asin(5 / 13)), 1), 22.6)
# proof: components, 3-4-5, check at 0 and 90
eq("proof 30", 50 * 0.6, 30); eq("proof 40", 50 * 0.8, 40); eq("proof pyth", 30 ** 2 + 40 ** 2, 50 ** 2)
for th in (13, 37, 61):
    eq("proof sin", cos(d(90 - th)), sin(d(th)))
# spot the error
R = 60 * cos(d(30)); eq("se R", sf(R), 52.0); eq("se R2", round(R, 2), 51.96)
eq("se Fwrong", round(0.6 * round(R, 1), 1), 31.2); eq("se Fmax", round(0.6 * R, 2), 31.18)
eq("se down", 60 * sin(d(30)), 30); assert 0.6 * R > 30; eq("se tan30", sf(tan(d(30))), 0.577)
# exam practice
eq("q1 R", 12 * g, 120); eq("q1 Fmax", 0.35 * 120, 42); assert 36 < 42
eq("q2 res", sqrt(7 ** 2 + 24 ** 2), 25); eq("q2 ang", round(degrees(atan(7 / 24)), 1), 16.3)
eq("q3 mu", sf(tan(d(35))), 0.700); eq("q3 tan30", sf(tan(d(30))), 0.577); assert tan(d(30)) < tan(d(35))
T = 40 / cos(d(30)); eq("q4 T", sf(T), 46.2); eq("q4 P", sf(T * sin(d(30))), 23.1)
P = 50 * sin(d(40)) / cos(d(20)); eq("q5 lhs", round(50 * sin(d(40)), 2), 32.14); eq("q5 cos20", round(cos(d(20)), 4), 0.9397)
eq("q5 P", sf(P), 34.2); eq("q5 50cos40", round(50 * cos(d(40)), 2), 38.30); eq("q5 Psin", round(P * sin(d(20)), 2), 11.70)
eq("q5 R", sf(50 * cos(d(40)) - P * sin(d(20))), 26.6)
den = cos(d(20)) + 0.3 * sin(d(20)); T = 45 / den; eq("q6 den", round(den, 4), 1.0423)
eq("q6 T", sf(T), 43.2); eq("q6 Tsin", round(T * sin(d(20)), 2), 14.77); eq("q6 R", sf(150 - T * sin(d(20))), 135)
eq("q6 check", T * cos(d(20)), 0.3 * (150 - T * sin(d(20))), 1e-9)
X = 8 + 6 * cos(d(120)); Y = 6 * sin(d(120)); eq("q7 X", X, 5); eq("q7 Y", round(Y, 3), 5.196)
eq("q7 mag", sf(sqrt(X ** 2 + Y ** 2)), 7.21); eq("q7 ang", round(degrees(atan(Y / X)), 1), 46.1)
th = atan(1 / 3); eq("q8 th", round(degrees(th), 1), 18.4)
Pq = 40; eq("q8 eq", Pq * (cos(th) - 0.5 * sin(th)), 40 * sin(th) + 20 * cos(th))
Rq = 40 * cos(th) + Pq * sin(th); eq("q8 R", sf(Rq, 3), 50.6)
eq("q8 along", round(40 * cos(th), 1), 37.9); eq("q8 sum", round(40 * sin(th), 1) + round(0.5 * Rq, 1), 37.9)
eq("q8 12.6", round(40 * sin(th), 1), 12.6); eq("q8 25.3", round(0.5 * Rq, 1), 25.3)
# stretch
mu = 0.4; Tmin = 0.4 * 200 / sqrt(1 + mu ** 2); eq("s1 sqrt", round(sqrt(1.16), 4), 1.0770)
eq("s1 alpha", round(degrees(atan(mu)), 1), 21.8); eq("s1 Tmin", sf(80 / sqrt(1.16)), 74.3)
eq("s1 T0", 80 / (cos(0) + mu * sin(0)), 80); eq("s1 T30", sf(80 / (cos(d(30)) + mu * sin(d(30))), 3), 75.0)
assert all(80 / (cos(d(t)) + mu * sin(d(t))) > 80 / sqrt(1.16) - 1e-9 for t in range(0, 90))
# quiz
eq("quiz slope", round(50 * sin(d(20)), 1), 17.1)

print("ok")
