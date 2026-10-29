# checks/bio.anaerobic.py: recomputes every number in the Anaerobic respiration chapter (chapters/bio.anaerobic.md).
from math import pi, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- warm-up and practice rates (rate = 1/t) -------------------------------------------------------------
eq("warm-up 1/200", 1 / 200, 5.0e-3)
eq("practice 1/320", sf(1 / 320, 3), 3.13e-3, 1e-12)
eq("quiz 1/150", sf(1 / 150, 3), 6.67e-3, 1e-12)

# --- sprinter (lactate and oxygen uptake) ------------------------------------------------------------------
lact = {0: 12.0, 5: 8.0, 10: 5.0, 20: 2.5, 30: 1.4}
eq("lactate fall 0-10", (lact[0] - lact[10]) / 10, 0.70)
eq("lactate fall 10-30", (lact[10] - lact[30]) / 20, 0.18)
assert 0.35 > 0.3 and 0.50 > 0.3          # uptake still above rest at 20 and 30 min
assert (lact[0] - lact[10]) / 10 > (lact[10] - lact[30]) / 20
eq("swimmer fall", (9.0 - 3.0) / 12, 0.50)

# --- methylene blue and temperature ------------------------------------------------------------------------
T = {20: 600, 30: 240, 40: 120, 50: 300}
rate = {k: 1 / v for k, v in T.items()}
eq("rate 20 C", sf(rate[20], 3), 1.67e-3, 1e-12)
eq("rate 30 C", sf(rate[30], 3), 4.17e-3, 1e-12)
eq("rate 40 C", sf(rate[40], 3), 8.33e-3, 1e-12)
eq("rate 50 C", sf(rate[50], 3), 3.33e-3, 1e-12)
eq("five times as fast 20 to 40", round(rate[40] / rate[20], 1), 5.0)
assert max(rate, key=rate.get) == 40
for t, r in [(20, 1.67), (30, 4.17), (40, 8.33), (50, 3.33)]:
    eq(f"plot point {t}", sf(1000 * rate[t], 3), r, 1e-9)

# --- glucose concentration ---------------------------------------------------------------------------------------
G = {2: 520, 4: 310, 6: 200, 8: 160, 10: 155}
eq("rate 4%", sf(1 / G[4], 3), 3.23e-3, 1e-12)
eq("rate 8%", sf(1 / G[8], 3), 6.25e-3, 1e-12)
eq("rate 10%", sf(1 / G[10], 3), 6.45e-3, 1e-12)
assert all(1 / G[k + 2] > 1 / G[k] for k in (2, 4, 6))   # rises until 8 %
assert (1 / G[10]) / (1 / G[8]) < 1.05            # levels off between 8 and 10 %

# --- respirometer and temperature -----------------------------------------------------------------------------
r = 0.50
d = {10: 6, 20: 14, 30: 28, 40: 46, 50: 23}
vol = {k: pi * r**2 * v / 5 for k, v in d.items()}
eq("rate 30 C mm3/min", sf(vol[30], 2), 4.4)
eq("rate 10 C mm3/min", sf(vol[10], 2), 0.94)
eq("rate 40 C mm3/min", sf(vol[40], 2), 7.2)
assert max(vol, key=vol.get) == 40 and vol[50] < vol[40]

# --- stretch: yeast ATP budget ---------------------------------------------------------------------------------
eq("aerobic glucose", 150 / 30, 5.0)
eq("anaerobic glucose", 150 / 2, 75)
eq("ethanol made", 75 * 2, 150)
eq("CO2 made", 75 * 2, 150)
eq("ratio of glucose", (150 / 2) / (150 / 30), 15)

print("ok")
