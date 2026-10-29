# checks/bio.practical.py: recomputes every number in the Practical skills: investigations chapter.
from math import exp, isclose, pi

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- warm-up ---------------------------------------------------------------------------------------------
eq("warm rate", sf(1 / 125, 2), 8.0e-3)
eq("warm uncertainty", 1 / 2, 0.5)

# --- paper facts (FACTS.md) --------------------------------------------------------------------------------
eq("minutes per mark", 120 / 40, 3)
eq("june 2024 marks", 21 + 19, 40)

# --- dilutions ----------------------------------------------------------------------------------------------
for c2, v1, w in [(0.10, 2.5, 17.5), (0.20, 5.0, 15.0), (0.30, 7.5, 12.5), (0.40, 10.0, 10.0), (0.50, 12.5, 7.5)]:
    eq(f"stock for {c2}", c2 * 20 / 0.80, v1)
    eq(f"water for {c2}", 20 - v1, w)
c = 2.0
for want in [0.20, 0.020, 0.0020]:
    c /= 10
    eq("tenfold", c, want)

# --- running investigation ------------------------------------------------------------------------------------
reps = {20: [396, 404, 400], 30: [197, 203, 200], 40: [102, 104, 106], 50: [158, 164], 60: []}
means = {T: (sum(v) / len(v) if v else None) for T, v in reps.items()}
for T, m in [(20, 400), (30, 200), (40, 104), (50, 161)]:
    eq(f"mean {T}", means[T], m)
for T, r in [(20, 2.50), (30, 5.00), (40, 9.62), (50, 6.21)]:
    eq(f"rate {T}", sf(1000 / means[T], 3), r)
eq("anomaly differs", 245 - 164, 81)
eq("agreement 158/164", 164 - 158, 6)
eq("mean 104", sf((102 + 104 + 106) / 3, 3), 104)
eq("rate 40 unrounded", sf(1000 / 104, 3), 9.62)
eq("rate 20 std form", sf(1 / 400 * 1000, 3), 2.50)

# --- the curve in the plot passes near the points -------------------------------------------------------------
R = lambda T: 2.5 * 2 ** ((T - 20) / 10) / (1 + exp((T - 48) / 2.5))
for T, v in [(20, 2.50), (30, 5.00), (40, 9.62), (50, 6.21), (60, 0.0)]:
    assert abs(R(T) - v) < 0.4, f"curve at {T}: {R(T)} vs {v}"
    n += 1
eq("curve 35", sf(R(35), 2), 7.0)
eq("prediction 140 s", round(1000 / 7.0, -1), 140)
assert R(45) > R(40) > R(30) and R(45) > R(50), "peak between 40 and 50"
n += 1

# --- calibration -----------------------------------------------------------------------------------------------
conc = [0.2, 0.4, 0.6, 0.8, 1.0]
vol = [5.1, 2.5, 1.7, 1.2, 1.0]
for c_, v in zip(conc, vol):
    assert abs(1 / c_ - v) < 0.2, (c_, v)
    n += 1
eq("unknown", 1 / 2.0, 0.50)

# --- errors ---------------------------------------------------------------------------------------------------
eq("syringe 10%", 0.1 / 1.0 * 100, 10)
eq("fine syringe 0.5%", 0.005 / 1.0 * 100, 0.5)
eq("0.5/40", 0.5 / 40 * 100, 1.25)

# --- practice ------------------------------------------------------------------------------------------------
eq("stock 25 cm3", 0.40 * 25 / 1.0, 10)
eq("water 25", 25 - 10, 15)
four = [12.1, 11.8, 12.3, 12.2]
eq("four total", round(sum(four), 1), 48.4)
eq("four mean", sf(sum(four) / 4, 3), 12.1)

# --- exam practice -----------------------------------------------------------------------------------------------
eq("ep dilution", 0.20 * 30 / 0.60, 10)
eq("ep water", 30 - 10, 20)
eq("ep calibration slope", 0.12 * 4, 0.48)
eq("unknown absorbance", 0.30 / 0.12, 2.5)
assert 0.66 > 0.48
n += 1
eq("0.66 would be", sf(0.66 / 0.12, 2), 5.5)
eq("pollen mean 15%", (28 + 27) / 2, 27.5)
eq("pollen mean 10%", (35 + 33 + 34) / 3, 34)
eq("pollen pc", 34 / 50 * 100, 68)

# --- stretch ----------------------------------------------------------------------------------------------------
A = [49, 52, 55]
B = [52, 56, 60]
eq("A mean", sum(A) / 3, 52)
eq("B mean", sum(B) / 3, 56)
eq("pc diff", sf((56 - 52) / 52 * 100, 2), 7.7)
eq("diff vs unc", 56 - 52, 4)
vol = pi * 0.50 ** 2 * 18
eq("resp volume", sf(vol, 3), 14.1)
eq("resp rate", sf(vol / 10 / 2.50, 2), 0.57)

# --- root length data ----------------------------------------------------------------------------------------
roots = {10: 4.2, 15: 9.8, 20: 17.5, 25: 24.1, 30: 19.6, 35: 6.3}
assert max(roots, key=roots.get) == 25
n += 1

# --- quiz ----------------------------------------------------------------------------------------------------
eq("quiz stock", 0.30 * 50 / 2.0, 7.5)
eq("quiz wrong conc", sf(7.5 * 2.0 / 57.5, 2), 0.26)

print("ok")
