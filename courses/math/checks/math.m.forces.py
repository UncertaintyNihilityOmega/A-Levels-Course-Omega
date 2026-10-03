# checks/math.m.forces.py: recomputes every number in the Forces and equilibrium chapter (g = 10).
from math import isclose, sin, cos, tan, atan, atan2, radians, degrees, sqrt

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
print("ok")
