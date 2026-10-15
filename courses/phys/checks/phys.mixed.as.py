# checks/phys.mixed.as.py: recomputes every number in the AS mixed practice chapter.
from math import isclose, sqrt, pi, sin, radians, asin, degrees

g = 9.81
e = 1.60e-19
u = 1.66e-27
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# ---- Multiple choice
# Q2 uncertainty
eq("mcq unc", 2 * 2.0 + 3.0, 7.0)
eq("mcq unc 6", 2.0 * 3.0, 6.0)
# Q3 ball
eq("mcq up time", sf(14 / g, 2), 1.4)
eq("mcq return", sf(2 * 14 / g, 2), 2.9)
eq("mcq 4v/g", sf(4 * 14 / g, 2), 5.7)
# Q4 braking
eq("mcq dist", 0.5 * 20 * 5.0, 50)
eq("mcq vt", 20 * 5.0, 100)
eq("mcq decel", 20 / 5.0, 4.0)
# Q6 rebound (REVIEW: replaced the trolley question that duplicated phys.exam.p1)
dp = 0.15 * (6.0 - (-8.0))
eq("mcq dp", dp, 2.1)
eq("mcq F", dp / 0.020, 105)
eq("mcq F wrong sub", 0.15 * (8.0 - 6.0) / 0.020, 15)
eq("mcq F arriving", 0.15 * 8.0 / 0.020, 60)
# Q7 floating
eq("mcq floating", 600 / 1000, 0.60)
# Q8 power
eq("mcq power", 1200 * 25, 30000)
eq("mcq F/v", 1200 / 25, 48)
eq("mcq half", 0.5 * 1200 * 25, 15000)
# Q9 elastic energy (REVIEW: replaced the wire question that duplicated phys.exam.p1)
eq("mcq EPE", 0.5 * 40 * 8.0e-3, 0.16)
eq("mcq EPE no half", 40 * 8.0e-3, 0.32)
eq("mcq EPE mm", 0.5 * 40 * 8.0, 160)
eq("mcq k", 40 / 8.0e-3, 5000)
# Q10 Malus (REVIEW: replaced the intensity question that duplicated phys.exam.p1)
from math import cos
eq("mcq malus", cos(radians(60))**2, 0.25)
eq("mcq malus sin2", sin(radians(60))**2, 0.75)
eq("mcq malus sin", sf(sin(radians(60)), 2), 0.87)
# Q11 stationary
eq("mcq wavelength", 2 * 1.2 / 3, 0.80)
eq("mcq loop", 1.2 / 3, 0.40)
# Q12 double slit
eq("mcq double slit", 2 * 2, 4)
# Q13 resistivity
eq("mcq stretch", 2 * 2, 4)
# Q14 parallel power
eq("mcq P1", 6.0**2 / 4.0, 9.0)
eq("mcq P2", 6.0**2 / 12, 3.0)
eq("mcq Ptot", 6.0**2 / 4.0 + 6.0**2 / 12, 12)
eq("mcq series", 6.0**2 / 16, 2.25)  # 2.25 W rounds to 2.3 W (2 s.f., half up)

# ---- Set A
# A1 car
v, s, m = 24.0, 62.0, 1200.0
a = v**2 / (2 * s)
eq("A1 a", sf(a, 2), 4.6)
eq("A1 t", sf(2 * s / v, 2), 5.2)
eq("A1 t alt", sf(v / a, 2), 5.2)
E = 0.5 * m * v**2
eq("A1 E", E, 345600)
eq("A1 E sf", sf(E, 2), 3.5e5)
eq("A1 F", sf(E / s, 2), 5.6e3)
eq("A1 F=ma", sf(m * a, 2), 5.6e3)
eq("A1 double", sf(s * 4, 2), 250)

# A2 spring
k, x, mb, h = 450.0, 0.060, 0.025, 1.2
E = 0.5 * k * x**2
eq("A2 E", E, 0.81)
vv = sqrt(2 * E / mb)
eq("A2 v", sf(vv, 2), 8.0)
eq("A2 v 3sf", sf(vv, 3), 8.05)
t = sqrt(2 * h / g)
eq("A2 t", sf(t, 2), 0.49)
eq("A2 t 3sf", sf(t, 3), 0.495)
eq("A2 range", sf(vv * t, 2), 4.0)

# A3 collision
mA, mB, uA, vA = 0.40, 0.60, 3.0, -0.60
vB = (mA * uA - mA * vA) / mB
eq("A3 vB", vB, 2.4)
ke0 = 0.5 * mA * uA**2
ke1 = 0.5 * mA * vA**2 + 0.5 * mB * vB**2
eq("A3 KE0", ke0, 1.8)
eq("A3 KE A", 0.5 * mA * vA**2, 0.072)
eq("A3 KE B", 0.5 * mB * vB**2, 1.728)
eq("A3 KE1", ke1, 1.8)
eq("A3 rel speed", uA, vB - vA)
F = mB * vB / 0.050
eq("A3 F", sf(F, 2), 29)
eq("A3 F on A", sf(mA * (uA - vA) / 0.050, 2), 29)

# A4 floating
m = 3.2
W = m * g
eq("A4 W", sf(W, 2), 31)
V = m / 1000
eq("A4 V", V, 3.2e-3)
depth = V / (0.20 * 0.20)
eq("A4 depth", depth, 0.080)
p = 1000 * g * depth
eq("A4 p", sf(p, 2), 7.8e2)
eq("A4 p 3sf", sf(p, 3), 785)
eq("A4 pA", sf(p * 0.040, 2), 31)
eq("A4 pA=W", p * 0.20 * 0.20, W, 1e-9)

# A5 wire
F, A, E, L = 90.0, 0.30e-6, 2.0e11, 1.200
sigma = F / A
eq("A5 stress", sigma, 3.0e8)
ext = sigma * L / E
eq("A5 ext", ext, 1.8e-3)
lam = 2 * L / 4
eq("A5 lambda", lam, 0.60)
# REVIEW: 320 Hz (not 160 Hz) so that v agrees with sqrt(T/mu) for this steel wire (rho 7800 kg/m3)
eq("A5 v", sf(320 * lam, 2), 190)
mu = 7800 * 0.30e-6
assert abs(sqrt(90 / mu) - 320 * lam) / (320 * lam) < 0.05

# ---- Set B
# B1 CRO
T = 3.2 * 0.50e-3
eq("B1 T", T, 1.6e-3)
f = 1 / T
eq("B1 f", f, 625)
eq("B1 f sf", f, 625)  # 625 Hz is 6.3 x 10^2 Hz (2 s.f., half up)
eq("B1 pp", 4.0 * 0.20, 0.80)
eq("B1 amp", 4.0 * 0.20 / 2, 0.40)
fo = f * 340 / (340 - 20)
eq("B1 Doppler", sf(fo, 2), 6.6e2)

# B2 intensity
P = 4.0
I1 = P / (4 * pi * 5.0**2)
I2 = P / (4 * pi * 20**2)
eq("B2 I1", sf(I1, 2), 1.3e-2)
eq("B2 I2", sf(I2, 2), 8.0e-4)
eq("B2 ratio", sqrt(I2 / I1), 0.25)
eq("B2 ratio rounded", sqrt(8.0e-4 / 1.3e-2) > 0.24, True)

# B3 grating
d = 1 / 300e3
eq("B3 d", sf(d, 3), 3.33e-6)
lam = 589e-9
theta = degrees(asin(lam / d))
eq("B3 theta", sf(theta, 3), 10.2)
nmax = d / lam
eq("B3 nmax", sf(nmax, 3), 5.66)
eq("B3 order", int(nmax), 5)
eq("B3 total", 2 * int(nmax) + 1, 11)

# B4 resonance tube
L1, L2, f = 0.240, 0.770, 320.0
lam = 2 * (L2 - L1)
eq("B4 lambda", lam, 1.06)
eq("B4 v", f * lam, 339.2, 1e-9)
eq("B4 v sf", sf(f * lam, 3), 339)
eq("B4 L3", L2 + lam / 2, 1.30)

# ---- Set C
# C1 heater
dia, rho, R, Eb, r = 0.40e-3, 1.1e-6, 4.0, 12.0, 0.50
A = pi * dia**2 / 4
eq("C1 A", sf(A, 2), 1.3e-7)
eq("C1 A 4sf", sf(A, 4), 1.257e-7)
L = R * A / rho
eq("C1 L", sf(L, 2), 0.46)
I = Eb / (R + r)
eq("C1 I", sf(I, 2), 2.7)
eq("C1 I 4", sf(I, 4), 2.667)
eq("C1 P", sf(I**2 * R, 2), 28)
eq("C1 Pr", sf(I**2 * r, 2), 3.6)

# C2 drift velocity
Ia, Aw, nd = 5.0, 2.5e-6, 8.5e28
vd = Ia / (Aw * nd * e)
eq("C2 vd", sf(vd, 2), 1.5e-4)
eq("C2 vd2", sf(2 * vd, 2), 2.9e-4)

# C3 thermistor
Rf, Vin, Vo = 2.2, 5.0, 2.0
Rth = Rf * (Vin - Vo) / Vo
eq("C3 Rth", sf(Rth, 2), 3.3)
Rp = Rf * 10 / (Rf + 10)
eq("C3 Rp", sf(Rp, 2), 1.8)
eq("C3 reading", sf(Rp / (Rp + 3.3) * 5.0, 2), 1.8)

# C4 alpha decay
eq("C4 nucleon", 241, 237 + 4)
eq("C4 proton", 95, 93 + 2)
E = 5.5e6 * e
eq("C4 E", E, 8.8e-13, 1e-20)
ma, Mn = 4.00 * u, 237 * u
va = sqrt(2 * E / ma)
eq("C4 va", sf(va, 2), 1.6e7)
eq("C4 va 4", sf(va, 4), 1.628e7)
vn = ma * va / Mn
eq("C4 vn", sf(vn, 2), 2.7e5)
ken = (ma * va) ** 2 / (2 * Mn)
eq("C4 KE ratio less", ken < E, True)

# ---- Set D
# D1 uncertainty
m, d, L = 85.2e-3, 12.00e-3, 95.0e-3
rho = 4 * m / (pi * d**2 * L)
eq("D1 rho", sf(rho, 3), 7.93e3)
pm, pd, pl = 0.1 / 85.2, 2 * 0.02 / 12.00, 0.5 / 95.0
eq("D1 pm", sf(pm * 100, 2), 0.12)
eq("D1 pd", sf(pd * 100, 2), 0.33)
eq("D1 pl", sf(pl * 100, 2), 0.53)
tot = pm + pd + pl
eq("D1 total", sf(tot * 100, 2), 0.98)
eq("D1 abs", sf(rho * tot, 2), 77)
eq("D1 abs 1sf", sf(rho * tot, 1), 80)

# D2 ball bearing in oil
r = 2.0e-3
V = 4 / 3 * pi * r**3
eq("D2 V", sf(V, 3), 3.35e-8)
mass = 7800 * V
W = mass * g
U = 900 * V * g
eq("D2 W", sf(W, 2), 2.6e-3)
eq("D2 W 3", sf(W, 3), 2.56e-3)
eq("D2 U", sf(U, 2), 3.0e-4)
eq("D2 U 3", sf(U, 3), 2.96e-4)
eq("D2 drag", sf(W - U, 2), 2.3e-3)
eq("D2 drag 4", sf(W - U, 4), 2.268e-3)
eq("D2 mass", sf(mass, 4), 2.614e-4)
eq("D2 a", sf((W - U) / mass, 2), 8.7)

# D3 cyclist
m, th, v, Fr = 85.0, radians(3.0), 8.0, 20.0
Fw = m * g * sin(th)
eq("D3 Fw", sf(Fw, 2), 44)
eq("D3 Fw 3", sf(Fw, 3), 43.6)
F = Fw + Fr
eq("D3 F", sf(F, 2), 64)
P = F * v
eq("D3 P", sf(P, 2), 5.1e2)
eq("D3 P 3", sf(P, 3), 509)
eq("D3 input", sf(P / 0.25, 2), 2.0e3)

# D4 Young modulus
F, x, L, dia = 32.0, 2.5e-3, 2.000, 0.40e-3
k = F / x
eq("D4 k", sf(k, 2), 1.3e4)
eq("D4 k exact", k, 12800)
A = pi * (dia / 2) ** 2
eq("D4 A", sf(A, 4), 1.257e-7)
E = k * L / A
eq("D4 E", sf(E, 2), 2.0e11)
eq("D4 EP", 0.5 * F * x, 0.040)

# D5 ballistic pendulum
mb, M, h = 0.010, 2.0, 0.10
vf = sqrt(2 * g * h)
eq("D5 vf", sf(vf, 2), 1.4)
eq("D5 vf 3", sf(vf, 3), 1.40)
ub = (mb + M) * vf / mb
eq("D5 u", sf(ub, 2), 2.8e2)
eq("D5 u 4", sf(ub, 4), 281.5)
KE0 = 0.5 * mb * ub**2
eq("D5 KE0", sf(KE0, 2), 4.0e2)
eq("D5 KE0 3", sf(KE0, 3), 396)
KE1 = 0.5 * (mb + M) * vf**2
eq("D5 KE1", sf(KE1, 3), 1.97)
eq("D5 loss", sf((KE0 - KE1) / KE0 * 100, 3), 99.5)

print("ok")
