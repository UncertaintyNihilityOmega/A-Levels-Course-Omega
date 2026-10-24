# checks/chem.planning.py: recomputes every number in "Planning, analysis and evaluation".
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0, Na 23.0, S 32.1, Ca 40.1, Cu 63.5.
from math import isclose, log, exp

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def fit(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n
    m = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return m, my - m * mx

H, C, O, Na, S, Ca, Cu = 1.0, 12.0, 16.0, 23.0, 32.1, 40.1, 63.5

# warm-up
eq("warm-up moles", 0.200 * 0.0250, 5.00e-3)

# quantities for CaCO3 + HCl
Mr_CaCO3 = Ca + C + 3 * O
eq("Mr CaCO3", Mr_CaCO3, 100.1)
n_CaCO3 = 0.30 / Mr_CaCO3
eq("n CaCO3", sf(n_CaCO3, 4), 2.997e-3, 1e-9)
eq("acid needed", sf(2 * n_CaCO3, 3), 5.99e-3, 1e-9)
eq("acid in weakest", 0.400 * 0.0500, 0.0200)
assert 0.0200 / (2 * n_CaCO3) > 3
eq("gas volume dm3", sf(n_CaCO3 * 24.0, 3), 0.0719, 1e-9)
eq("gas volume cm3", sf(n_CaCO3 * 24.0 * 1000, 3), 71.9, 1e-9)

# dilution table
for c, v, w in [(0.400, 10.0, 40.0), (0.800, 20.0, 30.0), (1.20, 30.0, 20.0), (1.60, 40.0, 10.0), (2.00, 50.0, 0.0)]:
    eq(f"dilution {c}", c * 50.0 / 2.00, v)
    eq(f"water {c}", 50.0 - v, w)

# standard solution
Mr_Na2CO3 = 2 * Na + C + 3 * O
eq("Mr Na2CO3", Mr_Na2CO3, 106.0)
eq("n std", 0.0500 * 0.2500, 0.01250)
eq("m Na2CO3", 0.0500 * 0.2500 * Mr_Na2CO3, 1.325, 1e-9)

# gravimetric CuSO4.xH2O
eq("m hydrate", round(27.18 - 24.68, 2), 2.50)
eq("m anhydrous", round(26.28 - 24.68, 2), 1.60)
eq("m water", round(27.18 - 26.28, 2), 0.90)
Mr_CuSO4 = Cu + S + 4 * O
eq("Mr CuSO4", Mr_CuSO4, 159.6)
n_cu = 1.60 / Mr_CuSO4
n_w = 0.90 / 18.0
eq("n CuSO4", sf(n_cu, 4), 0.01003, 1e-9)
eq("n H2O", n_w, 0.0500)
eq("x", sf(n_w / n_cu, 3), 4.99, 1e-9)

# first-order graph
k = 0.0300
ts = [0, 10, 20, 30, 40, 50]
v = [round(24.00 * exp(-k * t) / 0.05) * 0.05 for t in ts]
for got, want in zip(v, [24.00, 17.80, 13.15, 9.75, 7.25, 5.35]):
    eq("titre", round(got, 2), want, 1e-9)
lv = [log(x) for x in v]
for got, want in zip(lv, [3.178, 2.879, 2.576, 2.277, 1.981, 1.677]):
    eq("ln titre", round(got, 3), want, 1e-9)
m, c0 = fit(ts, lv)
eq("fit gradient", round(m, 4), -0.0300)
eq("point A", round(c0, 2), 3.18)
eq("point B", round(c0 + m * 50, 2), 1.68)
eq("gradient from points", (1.68 - 3.18) / 50, -0.0300)
eq("k in s-1", 0.0300 / 60, 5.00e-4, 1e-12)
eq("exp intercept", round(exp(3.18), 1), 24.0)
eq("half-life", round(0.693 / 0.0300, 1), 23.1)

# percentage errors
eq("titre %", round(0.10 / 23.45 * 100, 3), 0.426)
eq("pipette %", 0.06 / 25.0 * 100, 0.24)
conc = 0.100 * 23.45 / 25.0
eq("c HCl", round(conc, 4), 0.0938)
tot = 0.10 / 23.45 * 100 + 0.06 / 25.0 * 100
eq("total %", round(tot, 2), 0.67)
eq("abs unc", sf(conc * 0.67 / 100, 2), 6.3e-4, 1e-9)
eq("dT", 35.5 - 21.5, 14.0)
eq("dT %", round(1.0 / 14.0 * 100, 2), 7.14)

# anomaly
eq("agree", round(41.2 - 40.6, 1), 0.6)
eq("mean consistent", (41.2 + 40.6) / 2, 40.9)
eq("mean with anomaly", round((41.2 + 40.6 + 49.8) / 3, 1), 43.9)
eq("anomaly excess", round(49.8 - (41.2 + 40.6) / 2, 1), 8.9)
eq("shift", round(43.9 - 40.9, 1), 3.0)
eq("measuring cylinder %", 0.5 / 25.0 * 100, 2.0)

# try questions
for cc, vv in [(0.100, 10.0), (0.200, 20.0), (0.300, 30.0), (0.400, 40.0)]:
    eq("try dil", cc * 50.0 / 0.500, vv)
Mr_ox = 2 * H + 2 * C + 4 * O + 2 * 18.0
eq("Mr ethanedioic dihydrate", Mr_ox, 126.0)
eq("mass ox", 0.0400 * 0.2500 * Mr_ox, 1.260, 1e-9)
eq("titre 18.40 %", round(0.10 / 18.40 * 100, 3), 0.543)
eq("dT 8.5 %", round(1.0 / 8.5 * 100, 1), 11.8)
g = (5.50e-4 - 1.10e-4) / (0.250 - 0.050)
eq("try gradient", g, 2.20e-3, 1e-12)
eq("try intercept", 1.10e-4 - g * 0.050, 0.0, 1e-12)

# exam practice
eq("mass %", round(0.01 / 1.62 * 100, 3), 0.617)
eq("titre 21.35 %", round(0.10 / 21.35 * 100, 3), 0.468)
g2 = (0.0640 - 0.0160) / (0.800 - 0.200)
eq("ep gradient", g2, 0.0800, 1e-12)
eq("ep intercept", 0.0160 - g2 * 0.200, 0.0, 1e-12)
eq("ep mean", (31.4 + 30.8) / 2, 31.1)
eq("ep agree", round(31.4 - 30.8, 1), 0.6)

# zero order
A = [2.00 - 0.040 * t for t in (0, 10, 20, 30)]
for got, want in zip(A, [2.00, 1.60, 1.20, 0.80]):
    eq("zero order [A]", got, want, 1e-9)
eq("half-life 1", 1.00 and (2.00 - 1.00) / 0.040, 25.0)
eq("half-life 2", (1.00 - 0.50) / 0.040, 12.5)
eq("k zero", (2.00 - 1.60) / 10, 0.040)

# stretch 2
tt = [0, 10, 30, 70]; tit = [20.0, 10.0, 5.0, 2.5]
inv = [1 / x for x in tit]
for got, want in zip(inv, [0.0500, 0.100, 0.200, 0.400]):
    eq("1/titre", got, want, 1e-9)
for i in range(3):
    eq("1/titre gradient", (inv[i + 1] - inv[i]) / (tt[i + 1] - tt[i]), 0.00500, 1e-12)
eq("half-lives", (30 - 10) / 2, 10.0)

print("ok")
