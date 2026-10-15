# checks/phys.mock.p3.py: recomputes every number in Mock paper 3 (two practical questions of 20 marks).
from math import isclose, sqrt, sin, cos, radians, degrees, pi, floor, log10, atan2
from decimal import Decimal, ROUND_HALF_UP

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

# ======================= Question 1: current in a resistance wire =======================
# generator (the readings below were chosen near these ideal values, with scatter of about 1 to 4 per cent):
E = 3.00            # V, e.m.f. of the cell
Rfix = 2.10         # ohm, fixed resistor plus internal resistance
rho_true = 4.9e-7   # ohm m (constantan)
d_true = 0.40e-3    # m
A_true = pi * d_true**2 / 4
r_per_m = rho_true / A_true
eq("Q1 wire resistance per metre", r_per_m, 3.899, 0.001)
lengths = [0.200, 0.300, 0.400, 0.500, 0.600, 0.700]
ideal = [E / (Rfix + r_per_m * L) for L in lengths]
raw = [(1.03, 1.05), (0.91, 0.93), (0.82, 0.82), (0.78, 0.74), (0.68, 0.68), (0.61, 0.63)]
for (a, b), i0, L in zip(raw, ideal, lengths):
    assert abs((a + b) / 2 - i0) / i0 < 0.04, (L, a, b, i0)       # readings are within 4% of the ideal
    assert round(a * 100) == a * 100 or abs(a * 100 - round(a * 100)) < 1e-9   # recorded to 0.01 A
eq("Q1 ideal I at 0.2", sf(ideal[0], 3), 1.04)
eq("Q1 ideal I at 0.7", sf(ideal[5], 3), 0.621)
# the odd pair is at L = 0.500 m and differs most
diffs = [abs(a - b) for a, b in raw]
assert max(diffs) == diffs[3] and diffs[3] > 2 * sorted(diffs)[-2] - 1e-9 or diffs[3] == max(diffs)
eq("Q1 odd pair difference", round(diffs[3], 2), 0.04)
# (a)(i) ammeter drawing: pointer at 0.68 A, scale 0 to 1.2 A mapped to 150 deg .. 30 deg
ang = 150 - 0.68 / 1.2 * 120
eq("Q1 pointer angle", ang, 82.0)
cx, cy, Rr = 160, 178, 125
tipx, tipy = cx + (Rr - 10) * cos(radians(ang)), cy - (Rr - 10) * sin(radians(ang))
eq("Q1 pointer tip x", tipx, 176.0, 0.1)
eq("Q1 pointer tip y", tipy, 64.1, 0.1)
eq("Q1 first reading at 0.600 m is 0.68", raw[4][0], 0.68)
# minor division 0.02 A; half a division 0.01 A
eq("Q1 minor division", 1.2 / 60, 0.02)
# (a)(ii) micrometer: sleeve 0 mm, thimble line 40 at the datum: 40 x 0.01 mm
eq("Q1 micrometer", 0 + 40 * 0.01, 0.40)
eq("Q1 thimble line 40 y", 84 + 7 * (40 - 40), 84)
eq("Q1 thimble line 35 y", 84 + 7 * (35 - 40), 49)
eq("Q1 thimble line 45 y", 84 + 7 * (45 - 40), 119)
eq("Q1 thimble edge x for 0.40 mm", 50 + 40 * 0.40, 66)      # 40 px per mm, zero line at x = 50
# (b) table
means = [(a + b) / 2 for a, b in raw]
for m_, want in zip(means, [1.04, 0.92, 0.82, 0.76, 0.68, 0.62]):
    eq("Q1 mean I", round(m_, 2), want)
recips = [1 / m_ for m_ in means]
for r_, want3 in zip(recips, [0.962, 1.09, 1.22, 1.32, 1.47, 1.61]):
    eq("Q1 1/I (3 s.f.)", sf(r_, 3), want3)
for r_, want4 in zip(recips, [0.9615, 1.087, 1.220, 1.316, 1.471, 1.613]):
    eq("Q1 1/I (4 s.f.)", sf(r_, 4), want4)
# (c) least squares and accepted ranges
mx = sum(lengths) / 6
my = sum(recips) / 6
P = sum((x - mx) * (y - my) for x, y in zip(lengths, recips)) / sum((x - mx) ** 2 for x in lengths)
Q = my - P * mx
eq("Q1 least-squares P", sf(P, 3), 1.29, 0.0051)
eq("Q1 least-squares Q", sf(Q, 3), 0.70, 0.0051)
P_end = (recips[5] - recips[0]) / (lengths[5] - lengths[0])
eq("Q1 end-points gradient", sf(P_end, 2), 1.3)
Q_end = recips[0] - P_end * lengths[0]
eq("Q1 end-points intercept", sf(Q_end, 2), 0.70)
assert 1.22 <= P_end <= 1.35 and abs(1.22 - P) / P < 0.055 and abs(1.35 - P) / P < 0.055    # +-5% of least squares
assert 0.65 <= Q <= 0.75 and 0.65 <= Q_end <= 0.75
# ideal values for comparison: P = r/E and Q = Rfix/E
eq("Q1 theory P", r_per_m / E, 1.30, 0.005)
eq("Q1 theory Q", Rfix / E, 0.70, 0.005)
# (d)
Ameas = pi * (0.40e-3) ** 2 / 4
eq("Q1 area", sf(Ameas, 3), 1.26e-7, 1e-10)
rho_meas = P * E * Ameas
eq("Q1 rho from least squares P", sf(rho_meas, 2), 4.9e-7, 5e-9)
for Pt in (1.22, 1.35):
    assert 4.5e-7 <= Pt * E * Ameas <= 5.1e-7, Pt            # accepted range for rho
I_1m = 1 / (P + Q)
eq("Q1 I at 1.000 m", sf(I_1m, 2), 0.50)
assert 0.49 <= I_1m <= 0.52
I_1m_end = 1 / (P_end + Q_end)
assert 0.49 <= I_1m_end <= 0.52
Q1_marks = [7, 6, 4, 3]
Q1_tokens = {"(a)": 7, "(b)": 6, "(c)": 4, "(d)": 3}

# ======================= Question 2: falling paper cone =======================
t1 = [0.52, 0.47, 0.55]        # h = 0.400 m
t2 = [1.06, 1.00, 1.13]        # h = 0.800 m (first reading in Fig. 2.2)
h1, h2 = 0.400, 0.800
# (a)(i) stopwatch display
eq("Q2 stopwatch", 0 * 60 + 1 + 6 / 100, 1.06)
eq("Q2 first reading in Table 2.1", t2[0], 1.06)
# (a)(ii) vernier: main scale 78 mm, 7th vernier line aligned
mm_per_px = 1 / 28
x_zero = 40 + 28 * (78.7 - 75)
eq("Q2 vernier zero x", x_zero, 143.6, 0.05)
for k in range(11):
    pos = x_zero + 25.2 * k
    want = [143.6, 168.8, 194.0, 219.2, 244.4, 269.6, 294.8, 320.0, 345.2, 370.4, 395.6][k]
    eq(f"Q2 vernier line {k}", pos, want, 0.05)
# line 7 is on the main-scale line for 85 mm (x = 40 + 28 x 10 = 320) and no other line is on a main line
main_x = [40 + 28 * j for j in range(14)]
aligned = [k for k in range(11) if any(abs(x_zero + 25.2 * k - mx_) < 0.5 for mx_ in main_x)]
assert aligned == [7], aligned
eq("Q2 diameter", 78 + 7 * 0.1, 78.7)
eq("Q2 vernier division", 28 * 0.9, 25.2)
# (a)(iii) means
m1, m2 = sum(t1) / 3, sum(t2) / 3
eq("Q2 mean 1", sf(m1, 3), 0.513)
eq("Q2 mean 2", sf(m2, 3), 1.06, 0.0051)
eq("Q2 mean 2 unrounded", m2, 1.06333333, 1e-6)
# (a)(iv) half range and per cent
hr1 = (max(t1) - min(t1)) / 2
hr2 = (max(t2) - min(t2)) / 2
eq("Q2 half range 1", hr1, 0.04, 1e-12)
eq("Q2 half range 2", hr2, 0.065, 1e-12)
p1 = hr1 / m1 * 100
p2 = hr2 / m2 * 100
eq("Q2 percent t at 0.400", sf(p1, 2), 7.8)
eq("Q2 percent t at 0.800", sf(p2, 2), 6.1)
# (a)(v) uncertainty in h
dh = 0.005
ph1, ph2 = dh / h1 * 100, dh / h2 * 100
eq("Q2 percent h at 0.400", sf(ph1, 2), 1.3)
eq("Q2 percent h at 0.800", sf(ph2, 2), 0.63)
# (b) recording: the means to 0.01 s
eq("Q2 recorded mean 1", round(m1, 2), 0.51)
eq("Q2 recorded mean 2", round(m2, 2), 1.06)
# (c)
k1, k2 = m1 / h1, m2 / h2
eq("Q2 k1", sf(k1, 3), 1.28)
eq("Q2 k2", sf(k2, 3), 1.33)
pdiff = abs(k2 - k1) / ((k1 + k2) / 2) * 100
eq("Q2 percentage difference", sf(pdiff, 2), 3.5)
pdiff_rounded = abs(1.33 - 1.28) / ((1.33 + 1.28) / 2) * 100
assert 3.0 <= pdiff_rounded <= 4.0
punc = p1 + ph1
eq("Q2 percent uncertainty in k", sf(punc, 2), 9.0)
eq("Q2 about 9 per cent (7.8 + 1.3 added as rounded)", 7.8 + 1.3, 9.1)
assert pdiff < punc and pdiff < (p2 + ph2)                 # supports t = kh whichever uncertainty is used
eq("Q2 k mean", sf((k1 + k2) / 2, 4), 1.306)
# (d)
assert p1 > ph1 * 5                                         # time dominates the uncertainty
Q2_marks = [5, 2, 10, 3]
Q2_tokens = {"(a)": 5, "(b)": 2, "(c)": 1 + 1 + 4 + 4, "(d)": 3}

# ======================= the paper =======================
assert sum(Q1_marks) == 20 and sum(Q1_tokens.values()) == 20
assert sum(Q2_marks) == 20 and sum(Q2_tokens.values()) == 20
assert Q1_marks == [7, 6, 4, 3] and Q2_marks == [5, 2, 10, 3]
assert sum(Q1_marks) + sum(Q2_marks) == 40
print("ok", n, "checks; total marks", sum(Q1_marks) + sum(Q2_marks))
