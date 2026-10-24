# checks/chem.mock.p3.py: recomputes every number in Mock paper 3 (written).
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, O 16.0, S 32.1, Fe 55.8.
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

H, O, S, Fe = 1.0, 16.0, 32.1, 55.8

# Q1 titration
rough = 25.90 - 0.00
t1 = 25.55 - 0.00
t2 = 26.10 - 1.00
t3 = 25.70 - 0.50
eq("rough", round(rough, 2), 25.90)
eq("t1", round(t1, 2), 25.55)
eq("t2", round(t2, 2), 25.10)
eq("t3", round(t3, 2), 25.20)
assert round(abs(t2 - t3), 2) <= 0.10
assert round(abs(t1 - t2), 2) > 0.10 and round(abs(t1 - t3), 2) > 0.10
mean = (t2 + t3) / 2
eq("mean", mean, 25.15)
n_mn = 0.0100 * mean / 1000
eq("n MnO4", n_mn, 2.515e-4, 1e-12)
n_fe = 5 * n_mn
eq("n Fe", n_fe, 1.2575e-3, 1e-12)
c_fe = n_fe / 0.0250
eq("c Fe", sf(c_fe, 3), 0.0503)
Mr_FeSO4 = Fe + S + 4 * O
eq("Mr FeSO4", Mr_FeSO4, 151.9)
Mr_hyd = 13.90 / sf(c_fe, 3)
eq("Mr hydrate", round(Mr_hyd, 1), 276.3)
x = (Mr_hyd - Mr_FeSO4) / (2 * H + O)
eq("x", round(x, 1), 6.9)
# x for FeSO4.7H2O and the given mass concentration
assert round(x) == 7
eq("pct unc", round(0.10 / mean * 100, 3), 0.398)
v_new = n_mn / 0.00600 * 1000
eq("new titre", round(v_new, 1), 41.9)
eq("new pct", round(0.10 / 41.9 * 100, 2), 0.24)
assert v_new < 50.0

# Q2 thermometric
slope = (29.0 - 31.0) / (5.5 - 3.5)
eq("cooling slope", slope, -1.0)
# all cooling points on one line
for t, T in [(3.0, 31.5), (3.5, 31.0), (4.0, 30.5), (4.5, 30.0), (5.0, 29.5), (5.5, 29.0)]:
    eq("on line", 31.0 + slope * (t - 3.5), T)
T_ext = 31.0 + slope * (2.0 - 3.5)
eq("extrapolated T", T_ext, 32.5)
dT = 32.5 - 21.5
eq("dT", dT, 11.0)
n_cu = 0.200 * 50.0 / 1000
eq("n Cu", n_cu, 0.0100)
q = 50.0 * 4.18 * dT
eq("q", round(q, 0), 2299, 1e-9)
dH = -q / n_cu
eq("dH J", round(dH, -1), -229900, 1e-9)
eq("dH kJ", sf(dH / 1000, 3), -230)
eq("pct dT", round(1.0 / dT * 100, 2), 9.09)
eq("cylinder pct", 0.5 / 50.0 * 100, 1.0)
eq("0.1 thermometer pct", round(0.10 / dT * 100, 2), 0.91)

# Q3 marks add up
assert 4 + 4 + 2 + 2 + 2 == 14
assert 4 + 2 + 3 + 3 + 2 + 2 == 16
assert 2 + 1 + 4 + 1 + 2 == 10
assert 16 + 10 + 14 == 40

print("ok")
