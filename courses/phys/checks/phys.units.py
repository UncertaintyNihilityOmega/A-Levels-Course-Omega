# checks/phys.units.py: recomputes every number in the Physical quantities, units and uncertainty chapter.
from math import isclose, sqrt, pi, cos, sin, atan, asin, radians, degrees

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

c = 3.00e8
g = 9.81

# Warm-up
eq("3.5 km", 3.5e3, 3500)
eq("hyp 6 8", sqrt(6.0**2 + 8.0**2), 10)

# Derived units as exponent vectors (kg, m, s, A)
def mul(*us): return tuple(sum(u[i] for u in us) for i in range(4))
def inv(u): return tuple(-x for x in u)
kg, m, s, A = (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
acc = mul(m, inv(s), inv(s))
N = mul(kg, acc)
eq("N", N == (1, 1, -2, 0), True)
Pa = mul(N, inv(m), inv(m))
eq("Pa", Pa == (1, -1, -2, 0), True)
J = mul(N, m)
eq("J", J == (1, 2, -2, 0), True)
W = mul(J, inv(s))
eq("W", W == (1, 2, -3, 0), True)
C = mul(A, s)
V = mul(J, inv(C))
eq("V", V == (1, 2, -3, -1), True)
Ohm = mul(V, inv(A))
eq("ohm", Ohm == (1, 2, -3, -2), True)
rho_u = mul(kg, inv(m), inv(m), inv(m))
eq("rho", rho_u == (1, -3, 0, 0), True)

# s = ut + 1/2 a t^2
v = mul(m, inv(s))
eq("ut", mul(v, s) == m, True)
eq("at2", mul(acc, s, s) == m, True)
# p = rho g h
eq("rho g h", mul(rho_u, acc, m) == Pa, True)
# pendulum
eq("l/g", mul(m, inv(acc)) == (0, 0, 2, 0), True)
# v^2 = u^2 + 2as
eq("v2", mul(v, v) == mul(acc, m), True)
# F = kAv^2
k_u = mul(N, inv(m), inv(m), inv(v), inv(v))
eq("k units", k_u == (1, -3, 0, 0), True)
# v = k T^x mu^y : kg: x+y=0, m: x-y=1, s: -2x=-1
x = 0.5; y = -0.5
eq("kg", x + y, 0); eq("m", x - y, 1); eq("s", -2 * x, -1)
# C in drag formula dimensionless
eq("C units", mul(N, inv(mul(rho_u, m, m, v, v))) == (0, 0, 0, 0), True)
# G units and Kepler
G_u = mul(N, m, m, inv(kg), inv(kg))
eq("G units", G_u == (-1, 3, -2, 0), True)
eq("Kepler", mul(m, m, m, inv(mul(G_u, kg))) == (0, 0, 2, 0), True)

# Prefix conversions
eq("0.35 mm2", 0.35e-6, 3.5e-7, 1e-20)
eq("2.4 cm3", 2.4e-6, 2.4e-6, 1e-20)
eq("rho Cu", 8.96e-3 / 1e-6, 8.96e3, 1e-9)
eq("72 km/h", 72e3 / 3600, 20)
lam = 650e-9
eq("lambda", lam, 6.50e-7, 1e-15)
f = c / lam
eq("f", sf(f, 3) / 1e14, 4.62)
# try: easy
eq("5 cm3", 5.0e-6, 5.0e-6, 1e-20)
eq("8.0+/-0.2 %", 0.2 / 8.0 * 100, 2.5)
eq("distance", 6.0 + 8.0, 14)
eq("disp", sqrt(6.0**2 + 8.0**2), 10)
eq("100N cos30", sf(100 * cos(radians(30))), 86.6)
eq("100N sin30", sf(100 * sin(radians(30))), 50.0)
A_sq = 50.0**2
eq("area", A_sq, 2500)
eq("area unc", 0.02 * A_sq, 50)

# Estimates
eq("KE sprinter", 0.5 * 70 * 10**2, 3500)
Vroom = 8 * 6 * 3
eq("room volume", Vroom, 144)
eq("air mass", sf(1.2 * Vroom, 3), 173)
eq("run upstairs P", sf(60 * g * 3.0 / 5.0, 3), 353)

# Micrometer zero error
r = [0.62, 0.63, 0.62, 0.61, 0.63]
mean = sum(r) / 5
eq("mean d", mean, 0.622)
eq("corrected d", sf(mean - 0.03, 2), 0.59)
eq("exam zero error", sf(0.62 - 0.04, 2), 0.58)

# Repeated timings
t = [2.31, 2.35, 2.28, 2.33, 2.30]
mt = sum(t) / 5
eq("mean t", mt, 2.314)
half = (max(t) - min(t)) / 2
eq("half range", half, 0.035)
eq("half range 1sf", sf(half, 1), 0.04)
eq("t percent", sf(0.04 / 2.31 * 100, 2), 1.7)

# Density of cylinder
mm, dm_ = 112.4, 0.1
d, dd = 15.00, 0.02
l, dl = 80.0, 0.1
Vmm3 = pi * d**2 * l / 4
eq("V mm3", round(Vmm3), 14137)
Vcm3 = Vmm3 / 1000
eq("V cm3", sf(Vcm3, 4), 14.14)
rho = mm / Vcm3
eq("rho", sf(rho, 3), 7.95)
pm, pd, pl = dm_ / mm * 100, dd / d * 100, dl / l * 100
eq("pm", sf(pm, 2), 0.089)
eq("pd", sf(pd, 3), 0.133)
eq("pl", sf(pl, 3), 0.125)
tot = pm + 2 * pd + pl
eq("total pc", sf(tot, 2), 0.48)
drho = tot / 100 * rho
eq("drho", sf(drho, 2), 0.038)
eq("drho 1sf", sf(drho, 1), 0.04)
# diameter dominates
eq("diameter share", 2 * pd / tot > 0.5, True)

# Pendulum period
eq("T", 31.2 / 20, 1.56)
eq("dT", 0.2 / 20, 0.01)
eq("one swing pc", sf(0.2 / 1.56 * 100, 2), 13)
eq("20 swing pc", sf(0.2 / 31.2 * 100, 2), 0.64)

# Bar
eq("bar x-y", sf(12.4 - 3.5, 3), 8.9)
eq("bar unc", 0.2 + 0.1, 0.3, 1e-12)
eq("bar pc", sf(0.3 / 8.9 * 100, 2), 3.4)
eq("bar x pc", sf(0.2 / 12.4 * 100, 2), 1.6)
eq("bar y pc", sf(0.1 / 3.5 * 100, 2), 2.9)

# Spot the error
eq("rods diff", 25.0 - 20.0, 5.0)
eq("rod pc 1", 0.5 / 25.0 * 100, 2.0)
eq("rod pc 2", 0.4 / 20.0 * 100, 2.0)
eq("wrong unc", 0.04 * 5.0, 0.2, 1e-12)
eq("right unc", 0.5 + 0.4, 0.9, 1e-12)
eq("right pc", 0.9 / 5.0 * 100, 18.0, 1e-9)
eq("ratio", 18 / 4, 4.5)

# Vectors
eq("R 90", sqrt(30**2 + 40**2), 50)
eq("theta 90", sf(degrees(atan(40 / 30)), 3), 53.1)
R2 = 30**2 + 40**2 - 2 * 30 * 40 * cos(radians(120))
eq("R2 60", round(R2), 3700)
R60 = sqrt(R2)
eq("R 60", sf(R60, 3), 60.8)
th = degrees(asin(sin(radians(120)) * 40 / R60))
eq("theta 60", sf(th, 3), 34.7)
cx, cy = 30 + 40 * cos(radians(60)), 40 * sin(radians(60))
eq("comp x", cx, 50)
eq("comp y", sf(cy, 3), 34.6)
eq("R comp", sf(sqrt(cx**2 + cy**2), 3), 60.8)
eq("theta comp", sf(degrees(atan(cy / cx)), 3), 34.7)
# figure geometry (scale 4 px per N)
eq("fig R 60", sqrt(200**2 + 138.6**2) / 4, 60.8, 0.05)
eq("fig b 60", sqrt(80**2 + 138.6**2), 160, 0.05)
eq("fig R 90", sqrt(120**2 + 160**2) / 4, 50)
# bounce
eq("bounce dv", -6.0 - 8.0, -14.0)
# components
eq("rope x", sf(250 * cos(radians(25)), 3), 227)
eq("rope y", sf(250 * sin(radians(25)), 3), 106)
eq("fig comp x", 200 * cos(radians(25)), 181.3, 0.1)
eq("fig comp y", 200 * sin(radians(25)), 84.5, 0.1)

# Exam practice
gg = 4 * pi**2 * 0.800 / 1.79**2
eq("g", sf(gg, 3), 9.86)
pl_, pt_ = 0.002 / 0.800 * 100, 0.02 / 1.79 * 100
eq("pl", sf(pl_, 3), 0.25)
eq("pt", sf(pt_, 3), 1.12)
eq("pg", sf(pl_ + 2 * pt_, 2), 2.5)
eq("dg", sf(gg * (pl_ + 2 * pt_) / 100, 1), 0.2)
# aircraft
eq("ground speed", sf(sqrt(220**2 + 40**2), 3), 224)
eq("bearing", sf(degrees(atan(40 / 220)), 3), 10.3)
# Young modulus
F_, L_, d_, x_ = 50.0, 2.000, 0.60e-3, 1.80e-3
E = 4 * F_ * L_ / (pi * d_**2 * x_)
eq("E", sf(E, 3) / 1e11, 1.96)
pF, pL, pd2, px = 0.5 / 50.0 * 100, 0.005 / 2.000 * 100, 0.01 / 0.60 * 100, 0.05 / 1.80 * 100
eq("pF", pF, 1.0)
eq("pL", pL, 0.25)
eq("pd", sf(pd2, 3), 1.67)
eq("px", sf(px, 3), 2.78)
ptot = pF + pL + 2 * pd2 + px
eq("E total", sf(ptot, 2), 7.4)
eq("dE", sf(E * ptot / 100, 2) / 1e10, 1.4)
# wall bounce 40 degrees
eq("perp comp", sf(15 * cos(radians(40)), 3), 11.5)
eq("dv wall", sf(2 * 15 * cos(radians(40)), 3), 23.0)

# Stretch: paper
eq("sheet t", 48.0 / 500, 0.096)
eq("sheet dt", 0.5 / 500, 0.001)
eq("stack diff", sf(48.0 - 47.9, 1), 0.1)
eq("diff unc", 0.5 + 0.5, 1.0)
eq("diff pc", 1.0 / 0.1 * 100, 1000)

# Quiz
eq("quiz 2mm2", 2.0e-6, 2.0e-6, 1e-20)
eq("sphere pc", 3 * 2, 6)
eq("max resultant", 3.0 + 4.0, 7.0)
eq("min resultant", 4.0 - 3.0, 1.0)
eq("5N at 90", sqrt(3.0**2 + 4.0**2), 5.0)

print("ok")
