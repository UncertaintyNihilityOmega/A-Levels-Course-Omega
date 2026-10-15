# checks/phys.exam.p1.py: recomputes every number in the Paper 1 guide.
from math import isclose, sqrt, atan2, degrees

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# The paper in numbers
eq("min per q", 75 / 40, 1.875)
eq("1 min 53 s", 0.875 * 60, 52.5)
eq("first pass", 40 * 1.5, 60)
eq("review time", 75 - 60, 15)
eq("checkpoint 10", 10 * 1.5, 15)
eq("checkpoint 20", 20 * 1.5, 30)
eq("checkpoint 30", 30 * 1.5, 45)

# T1 units of viscosity: exponents (kg, m, s)
F = (1, 1, -2)
rv = (0, 2, -1)
eta = tuple(a - b for a, b in zip(F, rv))
eq("eta kg", eta[0], 1)
eq("eta m", eta[1], -1)
eq("eta s", eta[2], -1)
pressure = (1, -1, -2)   # F / area
assert pressure == (1, -1, -2) and pressure != eta

# T2 estimation
eq("KE jog", 0.5 * 60 * 5**2, 750)
eq("B speed", sqrt(2 * 75 / 60), 1.58, 0.01)
eq("D speed", sqrt(2 * 7500 / 60), 15.8, 0.1)
eq("jog time", 1000 / 5, 200)

# T3 ratio
eq("wire", 2 / (1 / 2)**2, 8)
eq("wire area halved", 2 * 2, 4)
eq("wire squared both", 4 * 4, 16)
eq("inverse square 2r", (1 / 2)**2, 0.25)
eq("inverse square 3r", (1 / 3)**2, 1 / 9)

# T4 v-t graph
a1 = 0.5 * 4.0 * 8.0
a2 = 6.0 * 8.0
a3 = 0.5 * 4.0 * 8.0
eq("tri", a1, 16)
eq("rect", a2, 48)
eq("total", a1 + a2 + a3, 80)
eq("trapezium", 0.5 * (6.0 + 14) * 8.0, 80)
eq("B triangle", 0.5 * 14 * 8.0, 56)
eq("D rectangle", 14 * 8.0, 112)
eq("t total", 4.0 + 6.0 + 4.0, 14)

# T5 vectors
eq("resultant", sqrt(6.0**2 + 8.0**2), 10)
eq("angle", round(degrees(atan2(8.0, 6.0))), 53)
eq("swap angle", round(degrees(atan2(6.0, 8.0))), 37)
eq("sum of sizes", 6.0 + 8.0, 14)

# T7 uncertainty
R = 8.0 / 0.50
eq("R", R, 16)
pv = 0.2 / 8.0
pi_ = 0.01 / 0.50
eq("%V", pv, 0.025)
eq("%I", pi_, 0.02)
eq("sum %", pv + pi_, 0.045)
eq("dR", sf(R * (pv + pi_), 2), 0.72, 1e-9)
eq("dR 1sf", sf(R * (pv + pi_), 1), 0.7)
eq("A diff", sf(R * (pv - pi_), 1), 0.08)
eq("B abs", 0.2 + 0.01, 0.21, 1e-9)
eq("D 4.5", 4.5, 4.5)

# T8 bridge
eq("P", 12 * 200 / 400, 6.0)
eq("Q", 12 * 300 / 400, 9.0)
eq("meter", 12 * 300 / 400 - 12 * 200 / 400, 3.0)

# T9 wave graphs
T = 2 * 0.010
eq("T", T, 0.020)
eq("v", 0.80 / T, 40, 1e-9)
eq("A lambda*T", sf(0.80 * T, 2), 0.016)
eq("B T/lambda", sf(T / 0.80, 2), 0.025)
eq("D half period", 0.80 / 0.010, 80, 1e-9)

# T10 quarks
eq("meson", 2 / 3 + 1 / 3, 1.0)
eq("wrong meson", sf(2 / 3 - 1 / 3, 2), 0.33)
eq("proton", 2 / 3 + 2 / 3 - 1 / 3, 1.0)
eq("meson baryon number", 1 / 3 - 1 / 3, 0.0)

# Quiz
eq("q1 s", sf(0.5 * g * 3.0**2, 2), 44)
eq("q1 gt", sf(g * 3.0, 2), 29)
eq("q1 no half", sf(g * 3.0**2, 2), 88)
eq("q1 half gt", sf(0.5 * g * 3.0, 2), 15)
v = 6.0 / 3.0
eq("q2 v", v, 2.0)
eq("q2 KE i", 0.5 * 2.0 * 3.0**2, 9.0)
eq("q2 KE f", 0.5 * 3.0 * v**2, 6.0)
eq("q2 loss", 0.5 * 2.0 * 3.0**2 - 0.5 * 3.0 * v**2, 3.0)
eq("q3 W", 1.2 * 0.20 / 0.30, 0.80)
eq("q3 swap", 1.2 * 0.30 / 0.20, 1.8, 1e-9)
eq("q3 no div", 1.2 * 0.30, 0.36)
eq("q3 centre dist", 0.50 - 0.30, 0.20)
P = 400 * g * 0.50
eq("q4 P", P, 1962)
eq("q4 2sf", sf(P, 2), 2.0e3)
eq("q4 3sf", sf(P, 3), 1.96e3)
eq("q4 no g", 400 * 0.50, 200)
eq("q4 divide", sf(400 * g / 0.50, 2), 7.8e3)
eq("q5 ratio", 2 / 2**2, 0.5)
eq("q6 ratio", 3**2, 9)
eq("q6 cube", 3**3, 27)
eq("q7 f1", 150 / 3, 50)
eq("q7 overtone", 150 / 4, 37.5)
eq("q7 mult", 150 * 3, 450)
eq("q8 area", 2**2, 4)
I = 6.0 / (5.0 + 1.0)
eq("q9 I", I, 1.0)
eq("q9 V", I * 5.0, 5.0)
eq("q9 lost", I * 1.0, 1.0)
# REVIEW: fourth options added to the crane and cell questions
eq("q4 KE option", 0.5 * 400 * 0.50**2, 50)
eq("q9 E/R slip", 6.0 - (6.0 / 5.0) * 1.0, 4.8)

print("ok")
