# checks/bio.hormones.py: recomputes every number in the Control and coordination in plants chapter (chapters/bio.hormones.md).
from math import cos, pi, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- :::plot stomatal aperture: 4.5 - 3.5 cos(2 pi x / 24) ----------------------------------------------------------------
a = lambda x: 4.5 - 3.5 * cos(2 * pi * x / 24)
for x in (0, 24, 48, 72, 96):
    eq(f"minimum 1 µm at {x} h", a(x), 1.0, 1e-9)
for x in (12, 36, 60, 84):
    eq(f"maximum 8 µm at {x} h", a(x), 8.0, 1e-9)

# --- try (easy): percentage decrease of aperture 6.0 -> 1.5 µm ----------------------------------------------------------
eq("75% decrease", (6.0 - 1.5) / 6.0 * 100, 75.0)

# --- exam practice: aperture, CO2 uptake and water loss -----------------------------------------------------------------------
ap = [0, 2, 4, 6, 8]
co2 = [0, 5, 8, 9, 9.5]
water = [0, 4, 8, 12, 16]
eq("CO2 / water at 2 µm", co2[1] / water[1], 1.25)
eq("CO2 / water at 8 µm to 2 d.p.", round(co2[4] / water[4], 2), 0.59)
assert co2[4] - co2[2] < water[4] - water[2], "CO2 uptake rises less than water loss"
n += 1
eq("water loss at 4 and 8 µm", water[2], 8)
eq("water loss at 8 µm", water[4], 16)
eq("CO2 uptake at 4 µm", co2[2], 8)

# --- exam practice: ABA table ---------------------------------------------------------------------------------------------------
abc = [0, 1, 10, 100, 1000]
apr = [9.0, 7.5, 4.0, 1.5, 1.0]
eq("percentage decrease 0 -> 100 µmol dm-3", sf((apr[0] - apr[3]) / apr[0] * 100, 2), 83)
assert all(x > y for x, y in zip(apr, apr[1:])), "aperture decreases with ABA"
n += 1

# --- worked example: barley amylase table ---------------------------------------------------------------------------------------
t = [0, 12, 24, 36, 48]
ga = [0, 4, 18, 40, 62]
water_c = [0, 1, 2, 3, 3]
eq("mean rate with gibberellin 12-36 h", (ga[3] - ga[1]) / (t[3] - t[1]), 1.5)
eq("change in activity", ga[3] - ga[1], 36)
eq("change in time", t[3] - t[1], 24)
eq("activity with gibberellin at 48 h", ga[4], 62)
eq("activity in water at 48 h", water_c[4], 3)

print(f"ok ({n} checks)")
