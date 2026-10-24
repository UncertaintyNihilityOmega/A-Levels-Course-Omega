# checks/chem.practical.py: recomputes every number in "Practical skills and qualitative analysis".
# Ar from the 9701 table (data/elements.json): H 1.0, C 12.0, O 16.0, Na 23.0, Mg 24.3, S 32.1, Cl 35.5, Ca 40.1, Fe 55.8, Ba 137.3.
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

H, C, O, Na, Mg, S, Cl, Ca, Fe, Ba = 1.0, 12.0, 16.0, 23.0, 24.3, 32.1, 35.5, 40.1, 55.8, 137.3

# warm-up
eq("wu c NaOH", 0.100 * 0.0200 / 0.0250, 0.0800)
eq("wu q", 50.0 * 4.18 * 6.0, 1254.0, 1e-6)

# mean titre example
tit = {"1": 23.90 - 0.50, "2": 23.65 - 0.00, "3": 23.50 - 0.00}
eq("t1", tit["1"], 23.40, 1e-9); eq("t2", tit["2"], 23.65, 1e-9); eq("t3", tit["3"], 23.50, 1e-9)
assert abs(tit["3"] - tit["1"] - 0.10) < 1e-9 and tit["2"] - tit["3"] > 0.10 + 1e-9
eq("mean titre", (tit["1"] + tit["3"]) / 2, 23.45, 1e-9)

# standard solution
Mr_Na2CO3 = 2 * Na + C + 3 * O
eq("Mr Na2CO3", Mr_Na2CO3, 106.0)
eq("n Na2CO3", 0.0500 * 0.2500, 0.01250)
eq("mass Na2CO3", round(0.01250 * Mr_Na2CO3, 3), 1.325)
m_tr = round(25.62 - 24.28, 2)
eq("mass transferred", m_tr, 1.34)
n_tr = m_tr / Mr_Na2CO3
eq("n transferred", round(n_tr, 5), 0.01264)
eq("conc", sf(n_tr / 0.2500, 3), 0.0506)

# KMnO4 / iron(II) sulfate purity
t = (21.10 + 21.00 + 21.05) / 3
eq("mean 21.05", t, 21.05, 1e-9)
assert max(21.10, 21.00, 21.05) - min(21.10, 21.00, 21.05) <= 0.10 + 1e-9
nMn = 0.0200 * t / 1000
eq("n MnO4", nMn, 4.210e-4, 1e-12)
nFe25 = 5 * nMn
eq("n Fe 25", nFe25, 2.105e-3, 1e-12)
nFe = nFe25 * 10
eq("n Fe 250", nFe, 0.02105, 1e-12)
Mr_FeSO4_7 = Fe + S + 4 * O + 7 * 18.0
eq("Mr FeSO4.7H2O", Mr_FeSO4_7, 277.9, 1e-9)
mFe = nFe * Mr_FeSO4_7
eq("mass", round(mFe, 3), 5.850)
eq("pct", round(mFe / 6.50 * 100, 1), 90.0)

# gravimetric BaCl2.xH2O
Mr_BaCl2 = Ba + 2 * Cl
eq("Mr BaCl2", Mr_BaCl2, 208.3, 1e-9)
anh = round(16.60 - 14.52, 2); wat = round(16.96 - 16.60, 2)
eq("anhydrous", anh, 2.08); eq("water", wat, 0.36); eq("hydrate", round(16.96 - 14.52, 2), 2.44)
eq("n BaCl2", round(anh / Mr_BaCl2, 6), 0.009986)
eq("n H2O", round(wat / 18.0, 5), 0.02000)
eq("x", round((wat / 18.0) / (anh / Mr_BaCl2), 3), 2.003)
# under-heated version (evaluating example)
anh2 = round(16.70 - 14.52, 2); wat2 = round(16.96 - 16.70, 2)
eq("anh2", anh2, 2.18); eq("wat2", wat2, 0.26)
eq("n BaCl2 2", round(anh2 / Mr_BaCl2, 5), 0.01047)
eq("n H2O 2", round(wat2 / 18.0, 5), 0.01444)
eq("x low", round((wat2 / 18.0) / (anh2 / Mr_BaCl2), 2), 1.38)

# MgSO4.xH2O exam question
Mr_MgSO4 = Mg + S + 4 * O
eq("Mr MgSO4", round(Mr_MgSO4, 1), 120.4)
w3 = round(2.46 - 1.20, 2)
eq("water", w3, 1.26)
eq("n MgSO4", round(1.20 / Mr_MgSO4, 6), 0.009967)
eq("n H2O", round(w3 / 18.0, 4), 0.0700)
eq("x MgSO4", round((w3 / 18.0) / (1.20 / Mr_MgSO4), 2), 7.02)

# thermometric: Zn + CuSO4
dT = 46.5 - 21.0
eq("dT", dT, 25.5)
q = 50.0 * 4.18 * dT
eq("q J", round(q), 5330)
eq("q kJ", round(q / 1000, 2), 5.33)
nCu = 0.500 * 0.0500
eq("n Cu", nCu, 0.0250)
eq("dH", sf(-q / 1000 / nCu), -213)
eq("pct unc dT", round(2 * 0.5 / dT * 100, 2), 3.92)
# extrapolation: cooling points 5..10 min fall 0.5 degC per minute from 46.0
pts = [(5, 46.0), (6, 45.5), (7, 45.0), (8, 44.5), (9, 44.0), (10, 43.5)]
mx = sum(a for a, _ in pts) / 6; my = sum(b for _, b in pts) / 6
slope = sum((a - mx) * (b - my) for a, b in pts) / sum((a - mx) ** 2 for a, _ in pts)
inter = my - slope * mx
eq("slope", slope, -0.5, 1e-9)
eq("extrapolated T at 4 min", inter + slope * 4, 46.5, 1e-9)
# figure geometry (temperature graph: 20 C at y 200, 160/30 px per degree; 26 px per min from x 50)
sy = 160 / 30
eq("fig y 46.5", round(200 - sy * (46.5 - 20), 1), 58.7)
eq("fig y 21", round(200 - sy * 1, 1), 194.7)

# gas collection
n_co2 = 84.0 / 24000
eq("n CO2", n_co2, 0.00350, 1e-12)
Mr_CaCO3 = Ca + C + 3 * O
eq("Mr CaCO3", round(Mr_CaCO3, 1), 100.1)
eq("mass CaCO3", n_co2 * Mr_CaCO3, 0.35035, 1e-9)
eq("pct CaCO3", round(n_co2 * Mr_CaCO3 / 0.500 * 100, 1), 70.1)

# uncertainties
eq("FACTS 14.0 rise", round(2 * 0.5 / 14.0 * 100, 2), 7.14)
eq("titre 23.45", round(2 * 0.05 / 23.45 * 100, 2), 0.43)
eq("mass diff 1.34", round(0.01 / 1.34 * 100, 2), 0.75)
eq("titre readings", round(26.85 - 3.40, 2), 23.45)
eq("17.75 unc", round(0.10 / 17.75 * 100, 3), 0.563)
eq("8.0 rise", 2 * 0.5 / 8.0 * 100, 12.5)
eq("10.0 rise", 2 * 0.5 / 10.0 * 100, 10.0)
eq("6.5 rise", round(2 * 0.5 / 6.5 * 100, 1), 15.4)
eq("rise 6.5", 28.0 - 21.5, 6.5)

# exam: concordant titres
eq("mean 17.75", (17.70 + 17.80) / 2, 17.75, 1e-9)
assert abs(17.95 - 17.80 - 0.15) < 1e-9

# thiosulfate / copper(II)
nS = 0.100 * 0.02240
eq("n S2O3", nS, 2.240e-3, 1e-12)
eq("c Cu", sf(nS / 0.0250, 3), 0.0896)

# rate data
V = [10, 20, 30, 40, 50]
T = [130, 65, 43, 33, 26]
inv = [1000 / x for x in T]
for v, x, want in zip(V, inv, [7.7, 15.4, 23.3, 30.3, 38.5]):
    eq(f"1000/t {v}", round(x, 1), want)
mx = sum(V) / 5; my = sum(inv) / 5
m = sum((a - mx) * (b - my) for a, b in zip(V, inv)) / sum((a - mx) ** 2 for a in V)
c = my - m * mx
eq("best-fit m", round(m, 4), 0.7646)
eq("best-fit c", round(c, 4), 0.0824)
y10, y50 = m * 10 + c, m * 50 + c
eq("y10", round(y10, 1), 7.7); eq("y50", round(y50, 1), 38.3)
eq("dy", round(38.3 - 7.7, 1), 30.6)
eq("gradient", round(30.6 / 40, 3), 0.765)
eq("fig y(10) px", round(210 - 3.8 * y10, 1), 180.6)
assert 40 > 0.5 * (54 - 5)      # triangle base more than half the plotted line

print("ok", n)
