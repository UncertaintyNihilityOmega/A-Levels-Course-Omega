# checks/bio.membranes.py: recomputes every number in the Membrane structure and cell signalling chapter.
from math import exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# --- Warm-up and practice: units -------------------------------------------------------------------------
eq("7 nm in um", 7 / 1000, 0.007)
eq("bilayers in 1 um (143)", round(1000 / 7), 143)
assert 1000 / 7 > 142.5, "rounds up to 143"

# --- Beetroot worked example, table and :::plot ------------------------------------------------------------
A = lambda x: 0.04 + 0.86 / (1 + exp((58 - x) / 5))
temps = [20, 30, 40, 50, 60, 70, 80]
tab = [0.04, 0.05, 0.07, 0.20, 0.56, 0.83, 0.88]
for t, a in zip(temps, tab):
    assert abs(A(t) - a) <= 0.03, f"table value at {t} deviates from the model curve ({A(t):.3f} v {a})"
eq("plot point (40, 0.063)", round(A(40), 3), 0.063)
eq("plot point (60, 0.555)", round(A(60), 3), 0.555)
eq("plot point (80, 0.89)", round(A(80), 2), 0.89)
eq("curve start at 10 C", round(A(10), 2), 0.04)
assert A(90) < 1.2 and max(tab) < 1.2, "y range 0-1.2 holds the curve"
eq("rise 40 -> 50 (0.13)", round(tab[3] - tab[2], 2), 0.13)
eq("rise 50 -> 60 (0.36)", round(tab[4] - tab[3], 2), 0.36)
assert all(b > a for a, b in zip(tab, tab[1:])), "absorbance rises with temperature"
assert tab[6] - tab[5] < 0.1, "levels off by 80 C"
assert (tab[2] - tab[0]) < 0.05, "small rise 20-40 C (0.04 to 0.07)"

# --- Exam practice: ethanol table ----------------------------------------------------------------------------
eth = [0, 10, 20, 30, 40, 50]
ab = [0.03, 0.05, 0.18, 0.47, 0.71, 0.74]
steps = [round(b - a, 2) for a, b in zip(ab, ab[1:])]
eq("steepest rise 20-40% ethanol (0.13, 0.29, 0.24)", max(steps), 0.29)
assert steps.index(max(steps)) in (2, 3), "steepest between 20% and 40%"
assert steps[-1] < 0.05, "levels off above 40%"
eq("0.74 at 50%", ab[-1], 0.74)

# --- Hormone binding table ------------------------------------------------------------------------------------
assert 5200 > 380 and 410 < 5200, "liver > kidney; protease reduces binding"
assert 410 < 5200 / 10, "protease reduces binding to under a tenth"

# --- Membrane mixing table -------------------------------------------------------------------------------------
temp = [5, 15, 25, 37]
mix = [0, 8, 62, 100]
d = [b - a for a, b in zip(mix, mix[1:])]
assert d.index(max(d)) == 1, "biggest rise 15 -> 25 C"
eq("8% to 62% is the biggest increase", max(d), 54)

print("ok")
