# checks/bio.glucose.py: recomputes every number in the Blood glucose chapter (chapters/bio.glucose.md).
from math import exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- :::plot blood glucose after a meal: g(x) = 5 + 11.9 x exp(-x/0.8) -----------------------------------------------
g = lambda x: 5 + 11.9 * x * exp(-x / 0.8)
eq("starts at 5.0", g(0), 5.0)
peak_x = max((k / 1000 for k in range(0, 5001)), key=g)
eq("peak at 0.8 h", round(peak_x, 3), 0.8)
eq("peak value 8.5", round(g(0.8), 1), 8.5)
assert g(3) < 6 and g(3) > 5, "back in the normal range (below 6) by 3 h"
n += 1
eq("alt text: about 5.8 at 3 h", round(g(3), 1), 5.8)

# --- worked example: amplification (invented numbers) ----------------------------------------------------------------------
g_prot = 1 * 10
ac = g_prot * 1
camp = ac * 100
pka = camp * 1
e1 = pka * 10
e_final = e1 * 10
eq("G-proteins", g_prot, 10)
eq("adenylyl cyclase", ac, 10)
eq("cAMP", camp, 1000)
eq("protein kinase A", pka, 1000)
eq("first enzyme", e1, 10000)
eq("final enzyme", e_final, 100000)
eq("glucose units per second", e_final * 20, 2.0e6)

# --- worked example: biosensor calibration (0.30 + 0.60 c) ---------------------------------------------------------------
conc = [0, 2, 4, 6, 8, 10]
cur = [0.30, 1.50, 2.70, 3.90, 5.10, 6.30]
for c, i in zip(conc, cur):
    eq(f"calibration at {c}", round(0.30 + 0.60 * c, 2), i)
eq("gradient", (cur[1] - cur[0]) / (conc[1] - conc[0]), 0.60)
eq("sample 3.30 µA", (3.30 - 0.30) / 0.60, 5.0)
assert 4 <= 5.0 <= 6
n += 1

# --- try (easy): proportional biosensor ----------------------------------------------------------------------------------------
eq("2.25 / 4.50 x 9.0", 2.25 / 4.50 * 9.0, 4.5)

# --- exam practice: second calibration (0.50 + 0.50 c) ---------------------------------------------------------------------
conc2 = [0, 3, 6, 9, 12]
cur2 = [0.50, 2.00, 3.50, 5.00, 6.50]
for c, i in zip(conc2, cur2):
    eq(f"calibration 2 at {c}", 0.50 + 0.50 * c, i)
eq("gradient 2", (cur2[1] - cur2[0]) / (conc2[1] - conc2[0]), 0.50)
eq("sample 4.25 µA", (4.25 - 0.50) / 0.50, 7.5)

# --- exam practice: type 1 diabetes table (invented) -----------------------------------------------------------------------
no_ins = [9, 15, 18, 19, 19]
with_ins = [7, 11, 9, 7, 6]
eq("no insulin rises to 19", max(no_ins), 19)
eq("no insulin starts at 9", no_ins[0], 9)
eq("with insulin peaks at 11 at 1 h", with_ins.index(max(with_ins)), 1)
eq("with insulin peak value", max(with_ins), 11)
eq("with insulin falls to 6", with_ins[-1], 6)

print(f"ok ({n} checks)")
