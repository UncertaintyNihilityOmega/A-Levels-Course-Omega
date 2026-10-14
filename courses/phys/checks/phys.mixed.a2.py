# checks/phys.mixed.a2.py: recomputes every number in the A Level mixed practice chapter.
from math import isclose, sqrt, pi, exp, log, asin, degrees

g = 9.81
e = 1.60e-19
u = 1.66e-27
G = 6.67e-11
h = 6.63e-34
c = 3.00e8
k = 1.38e-23
R = 8.31
NA = 6.02e23
me = 9.11e-31
mp = 1.67e-27
sigma = 5.67e-8


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


# ---- Set A
# A1 car on a bend
m, r, v = 1100, 45, 12
eq("A1 omega", sf(v / r, 2), 0.27)
eq("A1 F", sf(m * v**2 / r, 2), 3.5e3)
eq("A1 vmax", sf(sqrt(0.60 * g * r), 2), 16)

# A2 satellite
M, Re, ms = 5.97e24, 6.37e6, 850
r1 = Re + 4.0e5
eq("A2 r", r1, 6.77e6)
v1 = sqrt(G * M / r1)
eq("A2 v", sf(v1, 2), 7.7e3)
eq("A2 v 3", sf(v1, 3), 7.67e3)
T1 = 2 * pi * r1 / v1
eq("A2 T", sf(T1, 2), 5.5e3)
eq("A2 T min", round(T1 / 60), 92)
EK = 0.5 * ms * v1**2
EP = -G * M * ms / r1
eq("A2 EK", sf(EK, 2), 2.5e10)
eq("A2 EP", sf(EP, 2), -5.0e10)
eq("A2 EP=-2EK", EP, -2 * EK, 1e-3 * abs(EP))
r2 = 4.22e7
E2 = -G * M * ms / (2 * r2)
eq("A2 E2", sf(E2, 2), -4.0e9)
E1 = EK + EP
eq("A2 E1", sf(E1, 2), -2.5e10)
eq("A2 dE", sf(E2 - E1, 2), 2.1e10)

# A3 mass on a spring
mm, kk, x0 = 0.40, 64, 0.050
T = 2 * pi * sqrt(mm / kk)
eq("A3 T 3", sf(T, 3), 0.497)
eq("A3 T 2", sf(T, 2), 0.50)
om = sqrt(kk / mm)
eq("A3 omega", sf(om, 3), 12.6)
eq("A3 v0", sf(om * x0, 2), 0.63)
E = 0.5 * mm * om**2 * x0**2
eq("A3 E", sf(E, 2), 0.080)
eq("A3 E=kx2/2", E, 0.5 * kk * x0**2)
eq("A3 f", sf(1 / T, 2), 2.0)

# ---- Set B
# B1 kettle
Q = 1.5 * 4200 * 80
eq("B1 Q", sf(Q, 2), 5.0e5)
Pu = 0.90 * 2200
eq("B1 Pu", Pu, 1980)
eq("B1 t", sf(Q / Pu, 2), 2.5e2)
Eb = Pu * 120
eq("B1 Eb", sf(Eb, 3), 2.38e5)
eq("B1 mass", sf(Eb / 2.26e6, 2), 0.11)

# B2 helium
p, V, Tg = 1.5e5, 2.4e-3, 300
n = p * V / (R * Tg)
eq("B2 n", sf(n, 2), 0.14)
eq("B2 n 4", sf(n, 4), 0.1444)
N = n * NA
eq("B2 N", sf(N, 2), 8.7e22)
EKa = 1.5 * k * Tg
eq("B2 EK", sf(EKa, 2), 6.2e-21)
crms = sqrt(3 * k * Tg / (4.0 * u))
eq("B2 crms", sf(crms, 2), 1.4e3)

# B3 first law
p3, V1, V2, T1g = 1.0e5, 2.0e-3, 3.0e-3, 300
W = p3 * (V2 - V1)
eq("B3 W", W, 100)
dU = 250 - W
eq("B3 dU", dU, 150)
T2g = T1g * V2 / V1
eq("B3 T2", T2g, 450)
n3 = p3 * V1 / (R * T1g)
eq("B3 n", sf(n3, 3), 0.0802)
dU2 = 1.5 * n3 * R * (T2g - T1g)
eq("B3 dU2", dU2, 150, 1e-6)

# ---- Set C
# C1 proton in a magnetic field
V = 1500
vp = sqrt(2 * e * V / mp)
eq("C1 v", sf(vp, 2), 5.4e5)
eq("C1 v 3", sf(vp, 3), 5.36e5)
B = 0.080
rp = mp * vp / (B * e)
eq("C1 r", sf(rp, 2), 7.0e-2)
Tp = 2 * pi * mp / (B * e)
eq("C1 T", sf(Tp, 2), 8.2e-7)
eq("C1 T=2pi r/v", Tp, 2 * pi * rp / vp, 1e-12)
eq("C1 ratio", sf(sqrt(me / mp), 2), 0.023)
re_ = me * sqrt(2 * e * V / me) / (B * e)
eq("C1 r electron / r proton", re_ / rp, sqrt(me / mp), 1e-9)

# C3 supercapacitor
C, V0, Rc = 1.0, 12, 10
Es = 0.5 * C * V0**2
eq("C3 E", Es, 72)
dT = Es / (0.025 * 4200)
eq("C3 dT", sf(dT, 2), 0.69)
tau = Rc * C
eq("C3 tau", tau, 10)
eq("C3 I0", V0 / Rc, 1.2)
t = tau * log(V0 / 3.0)
eq("C3 t", sf(t, 2), 14)

# C4 Hall probe
B4, I4, t4, n4, w4 = 0.15, 5.0e-3, 2.0e-4, 2.0e22, 4.0e-3
VH = B4 * I4 / (n4 * t4 * e)
eq("C4 VH", sf(VH, 2), 1.2e-3)
eq("C4 VH 3", sf(VH, 3), 1.17e-3)
VHcu = B4 * I4 / (8.5e28 * t4 * e)
eq("C4 VH Cu", sf(VHcu, 2), 2.8e-10)
A4 = w4 * t4
eq("C4 A", A4, 8.0e-7)
vd = I4 / (n4 * A4 * e)
eq("C4 vd", sf(vd, 2), 2.0)
eq("C4 vd 3", sf(vd, 3), 1.95)
Fm = B4 * e * vd
Fe = e * VH / w4
eq("C4 Fm", sf(Fm, 2), 4.7e-20)
eq("C4 Fe", sf(Fe, 2), 4.7e-20)
eq("C4 equal", Fm, Fe, 1e-24)

# C5 generator
N5, B5, A5, f5, R5 = 250, 0.20, 4.0e-3, 25, 15
eq("C5 flux linkage", N5 * B5 * A5, 0.20)
om5 = 2 * pi * f5
eq("C5 omega", sf(om5, 3), 157)
E0 = N5 * B5 * A5 * om5
eq("C5 E0", sf(E0, 2), 31)
eq("C5 E0 3", sf(E0, 3), 31.4)
Erms = E0 / sqrt(2)
eq("C5 Erms", sf(Erms, 2), 22)
eq("C5 Erms 3", sf(Erms, 3), 22.2)
P5 = Erms**2 / R5
eq("C5 P", sf(P5, 2), 33)
eq("C5 half E0", sf(E0 / 2, 2), 16)
eq("C5 quarter P", sf(P5 / 4, 2), 8.2)

# C6 transformer and smoothing
Ns = 920 * 12 / 230
eq("C6 Ns", Ns, 48, 1e-9)
V06 = sqrt(2) * 12
eq("C6 V0", sf(V06, 2), 17)
eq("C6 V0 3", sf(V06, 3), 17.0)
RC = 24 * 2200e-6
eq("C6 RC", RC, 0.0528)
Vend = V06 * exp(-0.010 / RC)
eq("C6 Vend", sf(Vend, 3), 14.0)
eq("C6 ripple", sf(V06 - Vend, 2), 2.9)

# ---- Set D
# D1 photoelectric effect
lam = 250e-9
Eph = h * c / lam
eq("D1 E", sf(Eph, 2), 8.0e-19)
eq("D1 E 4", sf(Eph, 4), 7.956e-19)
Phi = 4.2 * e
eq("D1 Phi", Phi, 6.72e-19, 1e-24)
K = Eph - Phi
eq("D1 K", sf(K, 2), 1.2e-19)
eq("D1 K 4", sf(K, 4), 1.236e-19)
eq("D1 Vs", sf(K / e, 2), 0.77)
lam0 = h * c / Phi
eq("D1 lam0", sf(lam0, 2), 3.0e-7)

# D2 fluorine-18
t12 = 110 * 60
lm = 0.693 / t12
eq("D2 lambda", sf(lm, 3), 1.05e-4)
A0 = 3.7e8
N0 = A0 / lm
eq("D2 N", sf(N0, 2), 3.5e12)
tt = 3.0 * 3600
eq("D2 t", tt, 10800)
At = A0 * exp(-lm * tt)
eq("D2 A", sf(At, 2), 1.2e8)
Em = me * c**2
eq("D2 E", sf(Em, 2), 8.2e-14)
eq("D2 E MeV", sf(Em / e / 1e6, 2), 0.51)

# D3 fission power
Ef = 200e6 * e
eq("D3 Ef", Ef, 3.2e-11, 1e-20)
rate = 3.0e9 / Ef
eq("D3 rate", sf(rate, 2), 9.4e19)
eq("D3 rate 4", sf(rate, 4), 9.375e19)
mday = rate * 86400 * 235 * u
eq("D3 mass", sf(mday, 2), 3.2)
dm = Ef / c**2
eq("D3 dm", sf(dm, 2), 3.6e-28)
eq("D3 dm u", sf(dm / u, 2), 0.21)
eq("D3 Pe", 0.40 * 3.0e9, 1.2e9)

# D4 X-ray attenuation and ultrasound
mt, mb = 0.18, 0.60
Ia = exp(-mt * 6.0)
eq("D4 a", sf(Ia, 2), 0.34)
eq("D4 a 4", sf(Ia, 4), 0.3396)
Ib = exp(-(mb * 2.0 + mt * 4.0))
eq("D4 exponent", mb * 2.0 + mt * 4.0, 1.92)
eq("D4 b", sf(Ib, 2), 0.15)
eq("D4 b 4", sf(Ib, 4), 0.1466)
eq("D4 ratio", sf(Ib / Ia, 2), 0.43)
eq("D4 half", sf(log(2) / mt, 2), 3.9)
refl = (7.8 - 1.6) ** 2 / (7.8 + 1.6) ** 2
eq("D4 refl", sf(refl, 2), 0.44)

# D5 star
Tstar = 2.898e-3 / 460e-9
eq("D5 T", sf(Tstar, 2), 6.3e3)
L, F = 1.9e27, 2.0e-9
d = sqrt(L / (4 * pi * F))
eq("D5 d", sf(d, 2), 2.7e17)
eq("D5 ly", sf(d / 9.46e15, 2), 29)
rs = sqrt(L / (4 * pi * sigma * Tstar**4))
eq("D5 r", sf(rs, 2), 1.3e9)
eq("D5 r/Rsun", sf(rs / 6.96e8, 2), 1.9)
eq("D5 r 3", sf(rs, 3), 1.30e9)

# ---- Set E
# E1 oil drop
rho, rd, dgap, Vp = 900, 1.0e-6, 12e-3, 925
md = rho * 4 / 3 * pi * rd**3
eq("E1 m", sf(md, 2), 3.8e-15)
Wd = md * g
eq("E1 W", sf(Wd, 2), 3.7e-14)
Ef1 = Vp / dgap
eq("E1 field", sf(Ef1, 2), 7.7e4)
eq("E1 field 4", sf(Ef1, 4), 7.708e4)
q = Wd / Ef1
eq("E1 q", sf(q, 2), 4.8e-19)
eq("E1 n", sf(q / e, 2), 3.0)

# E2 electron diffraction
Ve = 120
pe = sqrt(2 * me * e * Ve)
eq("E2 p", sf(pe, 2), 5.9e-24)
eq("E2 p 4", sf(pe, 4), 5.915e-24, 1e-27)
lame = h / pe
eq("E2 lambda", sf(lame, 2), 1.1e-10)
eq("E2 lambda 4", sf(lame, 4), 1.121e-10)
theta = degrees(asin(lame / 2.5e-10))
eq("E2 theta", sf(theta, 2), 27)
Eph2 = h * c / lame
eq("E2 Eph", sf(Eph2, 2), 1.8e-15)
eq("E2 Eph keV", sf(Eph2 / e / 1e3, 2), 11)
eq("E2 ratio", sf(Eph2 / (e * Ve), 1), 90)

# E3 redshift
z = (680 - 656) / 656
eq("E3 z", sf(z, 3), 0.0366)
v3 = c * z
eq("E3 v", sf(v3, 2), 1.1e7)
eq("E3 v 4", sf(v3, 4), 1.098e7, 1e3)
H0 = 2.2e-18
d3 = v3 / H0
eq("E3 d", sf(d3, 2), 5.0e24)
age = 1 / H0
eq("E3 age s", sf(age, 2), 4.5e17)
eq("E3 age yr", sf(age / 3.16e7, 2), 1.4e10)

print("ok")
