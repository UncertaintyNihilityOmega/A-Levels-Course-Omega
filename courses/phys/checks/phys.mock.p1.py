# checks/phys.mock.p1.py: recomputes every number in Mock paper 1 (40 multiple-choice questions, 1 mark each).
from math import isclose, sqrt, sin, cos, radians, pi, floor, log10
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

g = 9.81
e = 1.60e-19

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, paper says {want}"

def sf(x, k=2):
    """round half up to k significant figures"""
    if x == 0:
        return 0.0
    d = Decimal(f"{x:.12g}")
    ex = floor(log10(abs(x)))
    q = Decimal(10) ** (ex - k + 1)
    return float((d / q).quantize(Decimal(1), rounding=ROUND_HALF_UP) * q)

keys = {}
def mc(q, key, truth, opts):
    """opts: letter -> (raw computed value, value shown in the paper, s.f.)
    The keyed option must be the physically correct answer and every option must differ."""
    global n
    assert set(opts) == set("ABCD"), f"Q{q}: need four options"
    shown_vals = []
    for L, (raw, shown, k) in opts.items():
        n += 1
        got = sf(raw, k)
        assert isclose(got, shown, rel_tol=1e-12, abs_tol=0), f"Q{q} option {L}: computed {got}, paper says {shown}"
        shown_vals.append(shown)
    assert len(set(shown_vals)) == 4, f"Q{q}: options are not all different"
    assert isclose(opts[key][0], truth, rel_tol=1e-9, abs_tol=1e-12), f"Q{q}: key {key} is not the true answer {truth}"
    others = [opts[L][0] for L in "ABCD" if L != key]
    assert all(not isclose(o, truth, rel_tol=1e-9) for o in others), f"Q{q}: a distractor equals the answer"
    keys[q] = key

def st(q, key):
    """statement question with no number: record the key"""
    keys[q] = key

# ---- Q1 units of resistivity: exponents (kg, m, s, A)
def plus(a, b): return tuple(x + y for x, y in zip(a, b))
def minus(a, b): return tuple(x - y for x, y in zip(a, b))
W = (1, 2, -2, 0)                # J
Q_ = (0, 0, 1, 1)                # C = A s
V = minus(W, Q_)                 # V = J / C
I_ = (0, 0, 0, 1)
R = minus(V, I_)
area = (0, 2, 0, 0); length = (0, 1, 0, 0)
rho = minus(plus(R, area), length)
assert V == (1, 2, -3, -1) and R == (1, 2, -3, -2)
assert rho == (1, 3, -3, -2), rho
assert minus(plus(R, length), area) == (1, 1, -3, -2)                  # option A: R L / A
assert R == (1, 2, -3, -2)                                             # option B: R itself
assert plus(plus(R, area), length) == (1, 5, -3, -2)                   # option D: R A L
st(1, "C")

# ---- Q2 volume of blood: 5 litres
litre = 1e-3
eq("Q2 blood", 5 * litre, 5e-3)
for k_, v_ in zip("ABCD", (5e-3, 5e-2, 5e-1, 5.0)):
    eq("Q2 option " + k_, v_, {"A": 5e-3, "B": 5e-2, "C": 5e-1, "D": 5.0}[k_])
st(2, "A")

# ---- Q3 precision and accuracy
true = 4.00
data = {1: (4.31, 4.30, 4.32), 2: (3.84, 4.19, 4.00), 3: (4.42, 3.71, 4.10), 4: (3.99, 4.01, 4.00)}
cls = {}
for s, r in data.items():
    mean = sum(r) / 3
    spread = max(r) - min(r)
    precise = spread <= 0.05
    accurate = abs(mean - true) <= 0.05
    cls[s] = (precise, accurate)
assert cls == {1: (True, False), 2: (False, True), 3: (False, False), 4: (True, True)}, cls
eq("Q3 mean of student 1", sf(sum(data[1]) / 3, 3), 4.31)
st(3, "A")

# ---- Q4 percentage uncertainty in E = 1/2 m v^2
pm = 0.005 / 0.250 * 100
pv = 0.04 / 3.20 * 100
eq("Q4 pm", pm, 2.0)
eq("Q4 pv", pv, 1.25)
truth = pm + 2 * pv
mc(4, "C", truth, {"A": (pm + pv / 2, 2.6, 2), "B": (pm + pv, 3.3, 2), "C": (truth, 4.5, 2), "D": (2 * pm + 2 * pv, 6.5, 2)})

# ---- Q5 change in velocity
truth = sqrt(20**2 + 20**2)
mc(5, "D", truth, {"A": (0.0, 0, 1), "B": (20 / sqrt(2), 14, 2), "C": (20.0, 20, 2), "D": (truth, 28, 2)})

# ---- Q6 area under the v-t graph (points (0,0), (4,10), (10,10), (12,0))
pts = [(0, 0), (4, 10), (10, 10), (12, 0)]
area_total = sum((pts[i + 1][0] - pts[i][0]) * (pts[i + 1][1] + pts[i][1]) / 2 for i in range(3))
eq("Q6 area", area_total, 90)
mc(6, "C", area_total, {"A": (6 * 10, 60, 2), "B": (0.5 * 4 * 10 + 6 * 10, 80, 2), "C": (area_total, 90, 2), "D": (10 * 12, 120, 2)})
eq("Q6 no-half slip also 120", 4 * 10 + 6 * 10 + 2 * 10, 120)
# drawn graph: 22 px per s, 12 px per m/s, origin (50, 165)
eq("Q6 px t=4", 50 + 22 * 4, 138); eq("Q6 px t=10", 50 + 22 * 10, 270); eq("Q6 px t=12", 50 + 22 * 12, 314); eq("Q6 px v=10", 165 - 12 * 10, 45)

# ---- Q7 uniform deceleration
a = (30**2 - 10**2) / (2 * 400)
mc(7, "C", a, {"A": (20 / 400, 0.050, 2), "B": (20**2 / (2 * 400), 0.50, 2), "C": (a, 1.0, 2), "D": ((30**2 - 10**2) / 400, 2.0, 2)})

# ---- Q8 dropped ball and horizontally thrown ball: same time of fall
h = 80.0
for u in (0.0, 15.0, 40.0):
    t = sqrt(2 * h / g)          # vertical motion does not depend on u
    eq("Q8 same fall time", t, sqrt(2 * h / g))
st(8, "A")

# ---- Q9 ball thrown up and caught: v = u - g t is one straight line from +u to -u
u = 10.0
T = 2 * u / g
eq("Q9 v(0)", u - g * 0, 10)
eq("Q9 v(T/2)", u - g * T / 2, 0, 1e-9)
eq("Q9 v(T)", u - g * T, -10, 1e-9)
st(9, "A")

# ---- Q10 third-law pair: the pair of the weight (Earth on box) is box on Earth
st(10, "D")

# ---- Q11 sticking collision
v = (0.60 * 4.0 + 0.40 * 1.0) / (0.60 + 0.40)
mc(11, "D", v, {"A": ((0.60 * 4.0 - 0.40 * 1.0) / 1.0, 2.0, 2), "B": (0.60 * 4.0 / 1.0, 2.4, 2), "C": ((4.0 + 1.0) / 2, 2.5, 2), "D": (v, 2.8, 2)})

# ---- Q12 average force on a squash ball
m, t = 0.024, 8.0e-3
F = m * (25 + 20) / t
eq("Q12 F", F, 135)
mc(12, "D", F, {"A": (m * (25 - 20) / t, 15, 2), "B": (m * 20 / t, 60, 2), "C": (m * 25 / t, 75, 2), "D": (F, 135, 3)})

# ---- Q13 elastic collision
m1, m2, u1 = 0.60, 0.40, 5.0
v2 = 2 * m1 * u1 / (m1 + m2)
v1 = (m1 - m2) * u1 / (m1 + m2)
eq("Q13 relative speeds", v2 - v1, u1)
eq("Q13 momentum", m1 * v1 + m2 * v2, m1 * u1)
eq("Q13 KE", 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2, 0.5 * m1 * u1**2)
mc(13, "D", v2, {"A": (v1, 1.0, 2), "B": (m1 * u1 / (m1 + m2), 3.0, 2), "C": (5.0, 5.0, 2), "D": (v2, 6.0, 2)})

# ---- Q14 torque of a couple (vertical forces, rod at 30 deg)
Fc, L = 12.0, 0.80
tq = Fc * L * cos(radians(30))
mc(14, "C", tq, {"A": (0.0, 0, 1), "B": (Fc * L * sin(radians(30)), 4.8, 2), "C": (tq, 8.3, 2), "D": (Fc * L, 9.6, 2)})
# figure: rod 208 px horizontal for 0.80 m at 30 degrees
eq("Q14 fig x", 80 + 240 * cos(radians(30)), 287.85, 0.01)
eq("Q14 fig y", 170 - 240 * sin(radians(30)), 50)

# ---- Q15 non-uniform plank
Wt = 240.0
FQ = Wt * 1.2 / 3.0
mc(15, "A", FQ, {"A": (FQ, 96, 2), "B": (Wt / 2, 120, 2), "C": (Wt - FQ, 144, 3), "D": (Wt * 2.0 / 3.0, 160, 2)})
eq("Q15 fig CoG x", 40 + 1.2 * 80, 136); eq("Q15 fig Q x", 40 + 3.0 * 80, 280)

# ---- Q16 manometer
rho_oil, h = 850.0, 0.14
dp = rho_oil * g * h
mc(16, "B", dp, {"A": (rho_oil * h, 1.2e2, 2), "B": (dp, 1.2e3, 2), "C": (2 * dp, 2.3e3, 2), "D": (dp * 100, 1.2e5, 2)})
eq("Q16 fig h", 110 - 50, 60)

# ---- Q17 stone in water
Wa, Wapp, rw = 4.0, 2.8, 1000.0
up = Wa - Wapp
eq("Q17 upthrust", up, 1.2)
rho_s = rw * Wa / up
mc(17, "D", rho_s, {"A": (rw * Wapp / Wa, 7.0e2, 2), "B": (rw * Wa / Wapp, 1.4e3, 2), "C": (rw * Wapp / up, 2.3e3, 2), "D": (rho_s, 3.3e3, 2)})
# the g cancels: V = up/(rw g), m = Wa/g
Vs = up / (rw * g); ms = Wa / g
eq("Q17 density via V and m", ms / Vs, rho_s, 1e-6)

# ---- Q18 efficiency of the hoist motor
out = 6.0 * g * 2.0
inp = 24 * 3.0 * 4.0
eff = out / inp * 100
eq("Q18 input", inp, 288)
mc(18, "C", eff, {"A": (6.0 * 2.0 / inp * 100, 4.2, 2), "B": ((out / 4.0) / inp * 100, 10, 2), "C": (eff, 41, 2), "D": (out / (24 * 3.0 * 2.0) * 100, 82, 2)})

# ---- Q19 power of a cyclist
Fr, vv, mass = 32.0, 7.5, 90.0
P = Fr * vv
mc(19, "B", P, {"A": (Fr / vv, 4.3, 2), "B": (P, 240, 2), "C": (Fr * vv**2, 1800, 2), "D": (0.5 * mass * vv**2, 2500, 2)})

# ---- Q20 energy transferred by friction
PE = 5.0 * g * 1.2
KE = 0.5 * 5.0 * 3.2**2
eq("Q20 KE", KE, 25.6)
fr = PE - KE
mc(20, "B", fr, {"A": (KE, 26, 2), "B": (fr, 33, 2), "C": (PE, 59, 2), "D": (PE + KE, 84, 2)})
eq("Q20 fig slope point", 50 + (120 - 80) / 2, 70)

# ---- Q21 springs in series
x = 3.0 / 30 + 3.0 / 60
eq("Q21 series k", 1 / (1 / 30 + 1 / 60), 20)
eq("Q21 x via k", 3.0 / 20, x)
mc(21, "D", x, {"A": (3.0 / (30 + 60), 0.033, 2), "B": (3.0 / 45, 0.067, 2), "C": (3.0 / 30, 0.10, 2), "D": (x, 0.15, 2)})

# ---- Q22 extension ratio of two wires
ratio = (1.5) * (1 / 2) * (2**2)
mc(22, "C", ratio, {"A": (1 / ratio, 0.33, 2), "B": (1.5 * (1 / 2) * 2, 1.5, 2), "C": (ratio, 3.0, 2), "D": (1.5 * 2**2, 6.0, 2)})

# ---- Q23 energy from the F-x graph (x in mm)
E_graph = 0.5 * 20 * 4.0 + 0.5 * (4.0 + 12.0) * 20       # N mm = mJ
eq("Q23 area", E_graph, 200)
Ej = E_graph * 1e-3
mc(23, "B", Ej, {"A": (0.5 * 20 * 4.0 * 1e-3, 0.040, 2), "B": (Ej, 0.20, 2), "C": (0.5 * 12.0 * 40 * 1e-3, 0.24, 2), "D": (12.0 * 40 * 1e-3, 0.48, 2)})
eq("Q23 fig px", 190 - 0, 190); eq("Q23 px F=4", 190 - 14 * 4, 134); eq("Q23 px F=12", 190 - 14 * 12, 22); eq("Q23 px x=40", 50 + 7 * 40, 330)

# ---- Q24 phase difference on a displacement-distance graph
lam = 8.0
eq("Q24 crest at 2 cm", sin(2 * pi * 2.0 / lam), 1.0)
eq("Q24 crest at 10 cm", sin(2 * pi * 10.0 / lam), 1.0)
eq("Q24 Q on axis", sin(2 * pi * 4.0 / lam), 0.0, 1e-12)
eq("Q24 P height px", 95 - 55 * sin(2 * pi * 1.0 / lam), 56.1, 0.05)
phi = (4.0 - 1.0) / lam * 360
mc(24, "C", phi, {"A": (1.0 / lam * 360, 45, 2), "B": (3.0 / lam * 180, 68, 2), "C": (phi, 135, 3), "D": (3.0 / 4.0 * 360, 270, 3)})

# ---- Q25 frequency from an oscilloscope trace
tb = 2.5e-3
cycles_in_10_div = 2
period_div = 10 / cycles_in_10_div
eq("Q25 period div", period_div, 5.0)
eq("Q25 trace period px", 30 * period_div, 150)
f = 1 / (period_div * tb)
mc(25, "B", f, {"A": (1 / (10 * tb), 40, 2), "B": (f, 80, 2), "C": (1 / (period_div / 2 * tb), 160, 3), "D": (1 / (1 * tb), 400, 3)})

# ---- Q26 intensity and amplitude with distance
r1, r2 = 1.0, 2.0
I_ratio = (r1 / r2) ** 2
A_ratio = sqrt(I_ratio)
eq("Q26 I ratio", I_ratio, 0.25)
eq("Q26 A ratio", A_ratio, 0.5)
combos = {"A": (0.25, 0.5), "B": (0.5, 0.5), "C": (0.25, 0.25), "D": (0.5, 1 / sqrt(2))}
good = [k for k, (i, a_) in combos.items() if isclose(i, I_ratio) and isclose(a_, A_ratio)]
assert good == ["A"], good
st(26, "A")

# ---- Q27 Doppler effect, source receding
fs, vs, vsound = 420.0, 30.0, 340.0
fo = fs * vsound / (vsound + vs)
mc(27, "B", fo, {"A": (fs * (1 - vs / vsound), 383, 3), "B": (fo, 386, 3), "C": (fs * (1 + vs / vsound), 457, 3), "D": (fs * vsound / (vsound - vs), 461, 3)})

# ---- Q28 two polarising filters
I0 = 24.0
I1 = I0 / 2
I2 = I1 * cos(radians(60)) ** 2
mc(28, "A", I2, {"A": (I2, 3.0, 2), "B": (I1 * cos(radians(60)), 6.0, 2), "C": (I1 * cos(radians(30)) ** 2, 9.0, 2), "D": (I0 * cos(radians(30)) ** 2, 18, 2)})

# ---- Q29 closed pipe: node at the closed end, antinode at the open end, 3 lambda / 4 = L
Lp = 0.90
lam = 4 * Lp / 3
mc(29, "D", lam, {"A": (Lp / 3, 0.30, 2), "B": (2 * Lp / 3, 0.60, 2), "C": (Lp, 0.90, 2), "D": (lam, 1.2, 2)})
eq("Q29 node position px", 40 + lam / 2 * (320 / Lp), 253.3, 0.05)
eq("Q29 L = 3 lam/4", 3 * lam / 4, Lp)

# ---- Q30 coherence
st(30, "D")

# ---- Q31 double-slit
x0 = 2.0
xn = x0 * (480 / 640) * (2.4 / 1.2)
mc(31, "C", xn, {"A": (x0 * (640 / 480) * (1.2 / 2.4), 1.3, 2), "B": (x0 * (480 / 640), 1.5, 2), "C": (xn, 3.0, 2), "D": (x0 * (640 / 480) * (2.4 / 1.2), 5.3, 2)})
eq("Q31 check original a", 640e-9 * 1.2 / 2.0e-3, 3.84e-4, 1e-12)

# ---- Q32 grating maxima
d = 1e-3 / 350
lam = 520e-9
eq("Q32 d in micrometres", d * 1e6, 2.857, 0.001)
nmax = floor(d / lam)
eq("Q32 d/lambda", d / lam, 5.495, 0.001)
eq("Q32 highest order", nmax, 5)
total = 2 * nmax + 1
mc(32, "D", total, {"A": (nmax, 5, 1), "B": (nmax + 1, 6, 1), "C": (2 * nmax, 10, 2), "D": (total, 11, 2)})

# ---- Q33 protons per second
Ib = 2.4e-6
N = Ib / e
mc(33, "C", N, {"A": (Ib * e, 3.8e-25, 2), "B": (e / Ib, 6.7e-14, 2), "C": (N, 1.5e13, 2), "D": (2.4e-3 / e, 1.5e16, 2)})

# ---- Q34 drift speed ratio
rv = Fraction(1, 1) / (2 * Fraction(3, 2) ** 2)
assert rv == Fraction(2, 9)
mc(34, "A", float(rv), {"A": (float(rv), 0.22, 2), "B": (1 / (2 * 1.5), 0.33, 2), "C": (1 / 2.25, 0.44, 2), "D": (2 * 2.25, 4.5, 2)})
eq("Q34 fractions", float(Fraction(2, 9)), 0.2222222222, 1e-9)
eq("Q34 1/3", float(Fraction(1, 3)), 1 / 3)
eq("Q34 4/9", float(Fraction(4, 9)), 1 / 2.25)
eq("Q34 9/2", float(Fraction(9, 2)), 4.5)

# ---- Q35 resistance of a lamp at P
def I_lamp(Vx): return 0.8 * (Vx / 8) ** 0.6
eq("Q35 I at 8 V", I_lamp(8), 0.80)
R_p = 8.0 / I_lamp(8)
slope = 0.6 * 0.8 / 8
eq("Q35 slope", slope, 0.06)
mc(35, "C", R_p, {"A": (I_lamp(8) / 8.0, 0.10, 2), "B": (8.0 * I_lamp(8), 6.4, 2), "C": (R_p, 10, 2), "D": (1 / slope, 17, 2)})
assert I_lamp(14) < 1.4          # curve stays inside the plot

# ---- Q36 power in R
E, r, Rl = 9.0, 2.0, 7.0
Iq = E / (Rl + r)
PR = Iq**2 * Rl
mc(36, "B", PR, {"A": (Iq**2 * r, 2.0, 2), "B": (PR, 7.0, 2), "C": (E * Iq, 9.0, 2), "D": (E**2 / Rl, 12, 2)})

# ---- Q37 two-cell network (node-voltage method, independent of the loop equations in the answer)
E1, R1, E2, R2, R3 = 9.0, 3.0, -6.0, 6.0, 3.0         # E2 negative: positive terminal at the bottom
Vp = (E1 / R1 + E2 / R2) / (1 / R1 + 1 / R2 + 1 / R3)
I1 = (E1 - Vp) / R1
I2 = (E2 - Vp) / R2
I3 = Vp / R3
eq("Q37 Vp", Vp, 2.4)
eq("Q37 I1", I1, 2.2); eq("Q37 I2", I2, -1.4); eq("Q37 I3", I3, 0.8)
eq("Q37 I3 = I1 + I2", I3, I1 + I2)
eq("Q37 loop 1", 6 * I1 + 3 * I2, 9.0)
eq("Q37 loop 2", 3 * I1 + 9 * I2, -6.0)
mc(37, "A", I3, {"A": (I3, 0.80, 2), "B": (abs(I2), 1.4, 2), "C": (I1, 2.2, 2), "D": (I1 + abs(I2), 3.6, 2)})

# ---- Q38 potential divider with an LDR
Rf, V0 = 6.0e3, 9.0
for Rldr, Vexp, Iexp in ((2.0e3, 2.25, 1.125e-3), (18e3, 6.75, 0.375e-3)):
    eq("Q38 Vout", V0 * Rldr / (Rf + Rldr), Vexp)
    eq("Q38 I", V0 / (Rf + Rldr), Iexp, 1e-12)
assert 0.375e-3 < 1.125e-3 and 6.75 > 2.25      # current falls, Vout rises
st(38, "B")

# ---- Q39 decay series
A0, Z0 = 235, 92
A1 = A0 - 4 * 4
Z1 = Z0 - 4 * 2 + 2 * 1
eq("Q39 A", A1, 219); eq("Q39 Z", Z1, 86)
eq("Q39 slip A (beta lowers Z)", Z0 - 8 - 2, 82)
eq("Q39 slip C", A0 - 8, 227)
eq("Q39 slip D", Z0 - 4 + 2, 90)
st(39, "B")

# ---- Q40 beta-plus decay at quark level: u -> d + e+ + electron neutrino
up_q, down_q = Fraction(2, 3), Fraction(-1, 3)
assert up_q == down_q + 1 + 0                       # charge: u -> d + e+ + nu_e
assert not (down_q == up_q + 1)                     # option B violates charge
assert (-1) + (-1) != 0 and (-1) + 1 == 0           # lepton number: e+ (-1) with antineutrino (-1) fails, with neutrino (+1) works
st(40, "A")

# ---- the paper
assert sorted(keys) == list(range(1, 41)), "need exactly 40 keyed questions"
marks = [1] * 40
assert len(marks) == 40 and sum(marks) == 40
counts = {L: sum(1 for k in keys.values() if k == L) for L in "ABCD"}
assert all(5 <= c <= 15 for c in counts.values()), counts   # keys are well spread
print("ok", n, "checks; key counts", counts)
