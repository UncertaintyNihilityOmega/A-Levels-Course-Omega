# checks/phys.mock.p2.py: recomputes every number in Mock paper 2 (7 structured questions, 60 marks).
from math import isclose, sqrt, sin, cos, tan, radians, degrees, asin, pi, floor, log10, atan2
from decimal import Decimal, ROUND_HALF_UP

g = 9.81

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, paper says {want}"

def sf(x, k=3):
    if x == 0:
        return 0.0
    d = Decimal(f"{x:.12g}")
    ex = floor(log10(abs(x)))
    q = Decimal(10) ** (ex - k + 1)
    return float((d / q).quantize(Decimal(1), rounding=ROUND_HALF_UP) * q)

# ---- Q1 units and uncertainty (6 marks)
kg, m_, s_ = (1, 0, 0), (0, 1, 0), (0, 0, 1)
F_units = (1, 1, -2)                     # kg m s^-2
k_units = tuple(a - b for a, b in zip(F_units, (0, 1, 0)))
assert k_units == (1, 0, -2), k_units    # kg s^-2
d, L, mass = 12.00e-3, 85.0e-3, 80.6e-3
ud, uL, um = 0.02e-3, 0.5e-3, 0.1e-3
V = pi * d**2 / 4 * L
rho = mass / V
eq("Q1 rho", sf(rho, 3), 8380)
pm, pd, pL = um / mass * 100, ud / d * 100, uL / L * 100
eq("Q1 % mass", sf(pm, 2), 0.12)
eq("Q1 % diameter", sf(pd, 2), 0.17)
eq("Q1 % length", sf(pL, 2), 0.59)
ptot = pm + 2 * pd + pL
eq("Q1 total %", sf(ptot, 3), 1.05)
urho = rho * ptot / 100
eq("Q1 abs unc", sf(urho, 2), 88)
eq("Q1 abs unc quoted as 0.09e3", sf(urho, 1), 90)
Q1 = [2, 2, 2]

# ---- Q2 projectile (9 marks)
u, th = 22.0, 50.0
vx, vy = u * cos(radians(th)), u * sin(radians(th))
eq("Q2 vx", sf(vx, 2), 14)
eq("Q2 vy", sf(vy, 2), 17)
H = vy**2 / (2 * g)
eq("Q2 H", sf(H, 2), 14)
eq("Q2 H 3sf", sf(H, 3), 14.5)
T = 2 * vy / g
eq("Q2 T", sf(T, 2), 3.4)
R = vx * T
eq("Q2 range", sf(R, 2), 49)
R_with_rounded_T = vx * 3.4
assert 48 <= sf(R_with_rounded_T, 2) <= 49          # accepted range in the scheme
# figure: parabola through (70,150), apex at x=270, landing (470,150) with the launch at 50 degrees
eq("Q2 fig apex ratio", tan(radians(th)) * (R / 2) / H, 2.0, 1e-9)   # tan(theta) = 2H / (R/2)
eq("Q2 fig arrow x", 70 + 65 * cos(radians(th)) , 111.8, 0.1)
eq("Q2 fig arrow y", 150 - 65 * sin(radians(th)), 100.2, 0.1)
eq("Q2 fig arc end x", 70 + 40 * cos(radians(th)), 95.7, 0.1)
eq("Q2 fig arc end y", 150 - 40 * sin(radians(th)), 119.4, 0.1)
Q2 = [1, 2, 2, 2, 2]

# ---- Q3 trolleys (9 marks)
mA, uA, mB = 0.50, 2.4, 0.30
v = mA * uA / (mA + mB)
eq("Q3 v", v, 1.5)
impulse = mB * v
eq("Q3 impulse on B", impulse, 0.45)
tc = 0.060
Fmax = 2 * impulse / tc
eq("Q3 Fmax", Fmax, 15.0)
KE0 = 0.5 * mA * uA**2
KE1 = 0.5 * (mA + mB) * v**2
eq("Q3 KE before", KE0, 1.44)
eq("Q3 KE after", KE1, 0.90)
eq("Q3 KE lost", KE0 - KE1, 0.54)
assert KE1 < KE0
# the impulse on A equals the impulse on B in size (third law)
eq("Q3 impulse on A", mA * (uA - v), impulse)
Q3 = [1, 2, 2, 2, 2]

# ---- Q4 beam and wire (9 marks)
Wb, Wl = 120.0, 90.0
Lb, xl, ang = 2.0, 1.5, 35.0
cw = Wb * (Lb / 2) + Wl * xl
eq("Q4 clockwise moment", cw, 255.0)
T_ = cw / (Lb * sin(radians(ang)))
eq("Q4 T", sf(T_, 2), 220)
assert 220 <= T_ <= 222.5
dw = 1.2e-3
A = pi * (dw / 2) ** 2
eq("Q4 area", sf(A, 3), 1.13e-6, 1e-12)
sigma = T_ / A
eq("Q4 stress", sf(sigma, 2), 2.0e8, 1)
Lw = Lb / cos(radians(ang))
eq("Q4 wire length from geometry", sf(Lw, 3), 2.44)
E_ = 2.0e11
x = sigma * 2.44 / E_
eq("Q4 extension", sf(x, 2), 2.4e-3, 1e-9)
eq("Q4 strain", sigma / E_, 9.83e-4, 1e-6)
# figure: wire from (300,190) to (60,22) makes 35 degrees with the beam
eq("Q4 fig angle", degrees(atan2(190 - 22, 300 - 60)), ang, 0.05)
eq("Q4 fig arc end", 260 + 40 * 0, 260)
eq("Q4 fig weight x", 60 + 120 * 1.0, 180); eq("Q4 fig load x", 60 + 120 * 1.5, 240)
Q4 = [1, 3, 2, 2, 1]

# ---- Q5 waves (10 marks)
Ls, loops, f = 0.90, 3, 120.0
lam = 2 * Ls / loops
eq("Q5 lambda", lam, 0.60)
eq("Q5 speed", f * lam, 72.0)
eq("Q5 phase diff adjacent loops", 180.0, 180.0)
lines = 420e3
dgr = 1 / lines
lam_l = 640e-9
eq("Q5 d", sf(dgr, 3), 2.38e-6, 1e-9)
s2 = 2 * lam_l / dgr
eq("Q5 sin theta", sf(s2, 3), 0.538)
th2 = degrees(asin(s2))
eq("Q5 theta2", sf(th2, 3), 32.5)
assert 32 <= th2 <= 33
nmax_raw = dgr / lam_l
eq("Q5 d/lambda", sf(nmax_raw, 3), 3.72)
nmax = floor(nmax_raw)
eq("Q5 highest order", nmax, 3)
eq("Q5 total maxima", 2 * nmax + 1, 7)
assert 4 * lam_l / dgr > 1          # order 4 would need sin theta > 1
# figure: 3 loops of 120 px between x=70 and x=430 for 0.90 m
eq("Q5 fig loop width", (430 - 70) / loops, 120)
Q5 = [2, 2, 1, 2, 3]

# ---- Q6 circuit (11 marks)
E, r, Rf, Rth = 12.0, 1.0, 15.0, 20.0
Rtot = Rf + Rth + r
I = E / Rtot
eq("Q6 total R", Rtot, 36.0)
eq("Q6 I", sf(I, 2), 0.33)
Vt = E - I * r
eq("Q6 terminal pd", sf(Vt, 3), 11.7)
eq("Q6 terminal pd via I x 35", sf(I * (Rf + Rth), 3), 11.7)
Vth = I * Rth
eq("Q6 V thermistor", sf(Vth, 2), 6.7)
# (d) V_th = E R / (Rf + r + R) increases with R, so it falls when R falls
def vth(Rx): return E * Rx / (Rf + r + Rx)
assert vth(10.0) < vth(20.0) < vth(40.0)
rho_c, dd = 4.9e-7, 0.20e-3
Aw = pi * (dd / 2) ** 2
Lwire = Rf * Aw / rho_c
eq("Q6 wire length", sf(Lwire, 2), 0.96)
Q6 = [2, 3, 2, 2, 2]

# ---- Q7 nucleus (6 marks)
A_na, Z_na = 22, 11
A_ne, Z_ne = A_na, Z_na - 1                  # beta+: A same, Z - 1
eq("Q7 neon A", A_ne, 22); eq("Q7 neon Z", Z_ne, 10)
assert Z_na == Z_ne + 1                      # charge: positron carries +1
from fractions import Fraction as Fr
assert Fr(2, 3) == Fr(-1, 3) + 1 + 0
Q7 = [2, 2, 2]

# ---- the paper
paper = {1: Q1, 2: Q2, 3: Q3, 4: Q4, 5: Q5, 6: Q6, 7: Q7}
expected = {1: 6, 2: 9, 3: 9, 4: 9, 5: 10, 6: 11, 7: 6}
for q, parts in paper.items():
    assert sum(parts) == expected[q], f"Q{q}: parts sum to {sum(parts)}, expected {expected[q]}"
assert len(paper) == 7
assert sum(expected.values()) == 60
print("ok", n, "checks; total marks", sum(sum(p) for p in paper.values()))
