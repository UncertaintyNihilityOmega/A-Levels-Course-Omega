# checks/chem.rates2.py: recomputes every number in "Rate equations and catalysis".
# Electrode potentials from FACTS.md: S2O8 2-/SO4 2- +2.01 V, Fe3+/Fe2+ +0.77 V, I2/I- +0.54 V.
# ln 2 is used as 0.693, as in the syllabus (k = 0.693 / t half).
from math import isclose, exp, log

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

LN2 = 0.693

# ---- effect of changing concentrations
eq("factor a", 3 ** 2 * 2, 18)
eq("factor b", (1 / 2) ** 2 * (1 / 2), 1 / 8)

# ---- plots: half-lives
# zero order, a0 = 1.00, k0 = 0.020: [A] = 1 - 0.02 t
t_half0 = 0.5 / 0.020
eq("zero order t1/2 (1.00 to 0.50)", t_half0, 25.0)
eq("zero second half-life", 0.25 / 0.020, 12.5)
eq("zero 0.25 at", 25.0 + 12.5, 37.5)
eq("zero reaches 0 at", 1.00 / 0.020, 50.0)
# first order: k = ln2/30
k1 = 0.693147 / 30
eq("plot k first order", sf(k1, 6), 0.0231049, 1e-7)
for t, a in [(30, 0.5), (60, 0.25), (90, 0.125)]:
    eq(f"first order at {t}", exp(-0.0231049 * t), a, 2e-4)
# second order: [A] = 1/(1 + k t), k = 1/30 for a0 = 1
for t, a in [(30, 0.5), (90, 0.25), (210, 0.125)]:
    eq(f"second order at {t}", 1 / (1 + t / 30), a, 1e-9)
eq("second order half-lives", (90 - 30) / 30, 2.0)
eq("second order half-lives 3", (210 - 90) / (90 - 30), 2.0)
# rate-concentration plots
eq("zero order rate", 0.02, 0.02)
eq("second order k", sf(1 / 30, 6), 0.0333333, 1e-7)

# ---- tangent example
rates = [0.0230, 0.0116, 0.00580]
concs = [1.00, 0.50, 0.25]
ks = [r / c for r, c in zip(rates, concs)]
eq("k1", sf(ks[0]), 0.0230)
eq("k2", sf(ks[1]), 0.0232)
eq("k3", sf(ks[2]), 0.0232)
eq("k mean", sf(sum(ks) / 3), 0.0231)

# ---- half-life examples
eq("eg k", sf(LN2 / 25), 2.77e-2)
# [A] data
a = [0.800, 0.400, 0.200, 0.100, 0.0500]
for i in range(1, 5):
    eq("halving", a[i] * 2, a[i - 1])
# second order data: half-lives 20, 40, 80
t = [0, 20, 60, 140]
hl = [t[i + 1] - t[i] for i in range(3)]
eq("hl1", hl[0], 20); eq("hl2", hl[1], 40); eq("hl3", hl[2], 80)
# drug
eq("drug 3 half-lives", 8.0 / 2 ** 3, 1.0)
eq("drug time", 3 * 6.0, 18)
eq("drug t1/2 s", 6.0 * 3600, 21600)
eq("drug k", sf(LN2 / 21600), 3.21e-5)

# ---- initial rates: NO + H2, rate = k[NO]^2 [H2], k = 200
k = 200.0
r1 = k * 0.0050 ** 2 * 0.0020
r2 = k * 0.0100 ** 2 * 0.0020
r3 = k * 0.0050 ** 2 * 0.0040
eq("r1", sf(r1), 1.0e-5)
eq("r2", sf(r2), 4.0e-5)
eq("r3", sf(r3), 2.0e-5)
eq("ratio 2/1", r2 / r1, 4.0)
eq("ratio 3/1", r3 / r1, 2.0)
eq("k from exp1", sf(1.0e-5 / (0.0050 ** 2 * 0.0020)), 2.0e2)
eq("k from exp2", sf(4.0e-5 / (0.0100 ** 2 * 0.0020)), 2.0e2)

# clock reaction: rate proportional to 1/t
eq("clock 1->2", (1 / 40) / (1 / 80), 2.0)
eq("clock 1->3", (1 / 40) / (1 / 80), 2.0)

# A + B -> C: rate = k[B]^2
k = 2.0e-2
eq("A+B r1", sf(k * 0.10 ** 2), 2.0e-4)
eq("A+B r2", sf(k * 0.10 ** 2), 2.0e-4)
eq("A+B r3", sf(k * 0.30 ** 2), 1.8e-3)
eq("A+B ratio", 1.8e-3 / 2.0e-4, 9.0)
eq("A+B k", sf(2.0e-4 / 0.10 ** 2), 2.0e-2)

# ---- Fe2+ catalysis
eq("uncatalysed Ecell", round(2.01 - 0.54, 2), 1.47)
eq("step 1 Ecell", round(2.01 - 0.77, 2), 1.24)
eq("step 2 Ecell", round(0.77 - 0.54, 2), 0.23)

# ---- try questions
eq("try3 k", sf(3.6e-4 / 0.30), 1.2e-3)
eq("try4 k", sf(LN2 / 40.0), 1.73e-2)
eq("try4 conc", 0.240 / 2 ** 3, 0.0300)
eq("try4 half-lives", 120 / 40.0, 3.0)
eq("try5 factor", 1.8e-2 / 2.0e-3, 9.0)
eq("try5 conc", 0.30 / 0.10, 3.0)
eq("try6 k", sf(4.5e-4 / (0.050 * 0.030)), 0.30)

# ---- exam practice
eq("ep1 factor", 3 * 2 ** 2, 12)
k = 1.3
eq("ep2 r1", sf(k * 0.010 * 0.10 * 0.10 ** 2), 1.3e-5)
eq("ep2 r2", sf(k * 0.020 * 0.10 * 0.10 ** 2), 2.6e-5)
eq("ep2 r3", sf(k * 0.010 * 0.20 * 0.10 ** 2), 2.6e-5)
eq("ep2 r4", sf(k * 0.010 * 0.10 * 0.20 ** 2), 5.2e-5)
eq("ep2 k", sf(1.3e-5 / (0.010 * 0.10 * 0.10 ** 2)), 1.3)
eq("ep3 t1/2 s", 25.0 * 60, 1500)
eq("ep3 k", sf(LN2 / 1500), 4.62e-4)
eq("ep3 half-lives", 75.0 / 25.0, 3.0)
eq("ep3 conc", sf(0.480 / 2 ** 3), 0.0600)
# ep8: second order, a0 = 0.800, t1/2 = 50 s, k = 1/(t1/2 a0)
k2 = 1 / (50 * 0.800)
eq("ep8 k", k2, 0.0250)
eq("ep8 initial rate", sf(k2 * 0.800 ** 2), 0.0160)
eq("ep8 k from rate", sf(0.0160 / 0.800 ** 2), 0.0250)
for t_, a_ in [(50, 0.400), (150, 0.200), (350, 0.100)]:
    eq(f"ep8 [A] at {t_}", 1 / (1 / 0.800 + k2 * t_), a_, 1e-9)
eq("ep8 hl1", 50, 50); eq("ep8 hl2", 150 - 50, 100); eq("ep8 hl3", 350 - 150, 200)

# ---- quiz
eq("quiz k", sf(LN2 / 40.0), 1.73e-2)
eq("quiz wrong 27.7", sf(0.693 * 40.0), 27.7)
eq("quiz wrong option", sf(40.0 / 0.693), 57.7)

print("ok")
