# checks/bio.oxygen.py: recomputes every number in chapters/bio.oxygen.md
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sat(p, p50, nn=2.7):
    """Model curve behind the :::plot lines and the widget: Hill function."""
    return 100 * p**nn / (p50**nn + p**nn)


def sf(x, k=3):
    return float(f"{x:.{k}g}")


P50_LOW = 3.4
P50_HIGH = 3.4 + 0.25 * (10 - 5.3)          # the widget's rule at pCO2 10 kPa
eq("P50 at 10 kPa", P50_HIGH, 4.575, 1e-12)

# --- model curve readings quoted in the text and plot ----------------------------------------------------
eq("lungs 13 kPa", round(sat(13, P50_LOW)), 97)
eq("lungs 13 kPa to 1 d.p. (plot point)", round(sat(13, P50_LOW), 1), 97.4)
eq("resting tissue 4 kPa", round(sat(4, P50_LOW)), 61)
eq("resting tissue 4 kPa to 1 d.p. (plot point)", round(sat(4, P50_LOW), 1), 60.8)
eq("tissue 5 kPa", round(sat(5, P50_LOW)), 74)
eq("altitude 8 kPa", round(sat(8, P50_LOW)), 91)
eq("high pCO2, 4 kPa", round(sat(4, P50_HIGH)), 41)
eq("high pCO2, 4 kPa to 1 d.p. (plot point)", round(sat(4, P50_HIGH), 1), 41.0)
eq("Bohr shift at 4 kPa (percentage points, text says 20)", round(sat(4, P50_LOW) - sat(4, P50_HIGH)), 20)
assert sat(2, P50_LOW) < sat(6, P50_LOW) < sat(13, P50_LOW) < 100
# steepest between 2 and 6 kPa
slopes = {a: sat(a + 1, P50_LOW) - sat(a, P50_LOW) for a in range(0, 13)}
assert max(slopes, key=slopes.get) in (2, 3, 4), slopes

# --- worked example: oxygen unloaded --------------------------------------------------------------------
unloaded = 97 - 74
eq("unloaded points", unloaded, 23)
eq("volume unloaded", sf(unloaded / 100 * 20, 2), 4.6)
eq("O2 carried at 97%", 0.97 * 20, 19.4, 1e-12)
eq("share of O2 given up", round(4.6 / 19.4 * 100), 24)
eq("O2 still carried at 74%", 0.74 * 20, 14.8, 1e-12)

# --- worked example: altitude -----------------------------------------------------------------------------
eq("fall in pO2 as %", round((13 - 8) / 13 * 100), 38)
eq("fall in saturation (points)", 97 - 91, 6)

# --- practice: Start easy ---------------------------------------------------------------------------------
eq("try 80% of 15", 80 / 100 * 15, 12)
eq("percentages of CO2", 85 + 10 + 5, 100)

# --- exam practice: large and small mammal table ----------------------------------------------------------
large = {2: 29, 4: 72, 6: 89, 9: 96, 13: 98}
small = {2: 7, 4: 32, 6: 58, 9: 81, 13: 92}
for p in large:
    eq(f"large mammal at {p} kPa", round(sat(p, 2.8)), large[p])
    eq(f"small mammal at {p} kPa", round(sat(p, 5.3)), small[p])
    assert large[p] > small[p]
eq("small mammal unloaded", small[13] - small[4], 60)
eq("small mammal volume", sf((small[13] - small[4]) / 100 * 15, 2), 9.0)

# --- exam practice: Bohr data (invented, must show a right shift that is smaller at high pO2) -----------------
low = {3: 45, 6: 85, 10: 96}
high = {3: 25, 6: 68, 10: 90}
for p in low:
    assert high[p] < low[p]
assert (low[3] - high[3]) > (low[10] - high[10])

# --- stretch: anaemia -------------------------------------------------------------------------------------
eq("normal blood unloads (points)", 98 - 42, 56)
eq("normal blood volume", sf(0.56 * 16, 2), 9.0, 1e-12)
eq("anaemic blood volume", sf(0.56 * 8, 2), 4.5, 1e-12)

# --- worked example: extra oxygen released by the Bohr shift at 4 kPa (97% leaving the lungs, 18 cm3 capacity) ------------
eq("Bohr eg: saturation at 4 kPa, normal pCO2", round(sat(4, P50_LOW)), 61)
eq("Bohr eg: saturation at 4 kPa, raised pCO2", round(sat(4, P50_HIGH)), 41)
eq("Bohr eg: unloaded, normal", 97 - 61, 36)
eq("Bohr eg: unloaded, raised", 97 - 41, 56)
eq("Bohr eg: extra points", (97 - 41) - (97 - 61), 20)
eq("Bohr eg: extra volume", sf(20 / 100 * 18, 2), 3.6, 1e-12)
eq("Bohr eg: volume normal", 0.36 * 18, 6.48, 1e-12)
eq("Bohr eg: volume raised", 0.56 * 18, 10.08, 1e-12)
eq("Bohr eg: ratio", sf(10.08 / 6.48, 2), 1.6, 1e-12)

print("ok")
