# checks/bio.energy.py: recomputes every number in the Energy, ATP and RQ chapter (chapters/bio.energy.md).
from math import pi, isclose
from fractions import Fraction

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=2):
    return float(f"{x:.{k}g}")


def o2_needed(x, y, z):
    """O2 molecules for complete oxidation of CxHyOz."""
    return x + Fraction(y, 4) - Fraction(z, 2)


def rq(x, y, z):
    return float(Fraction(x) / o2_needed(x, y, z))


def atoms_ok(x, y, z):
    """atom balance of the equation CxHyOz + O2 -> xCO2 + (y/2)H2O."""
    o = o2_needed(x, y, z)
    return z + 2 * o == 2 * x + Fraction(y, 2)


# --- hydrogen and mass --------------------------------------------------------------------------------
M_glucose = 6 * 12 + 12 * 1 + 6 * 16
M_tripalm = 51 * 12 + 98 * 1 + 6 * 16
eq("M glucose", M_glucose, 180)
eq("M tripalmitin", M_tripalm, 806)
eq("H% glucose", round(12 / M_glucose * 100, 1), 6.7)
eq("H% tripalmitin", sf(98 / M_tripalm * 100, 2), 12)
o2_g = float(o2_needed(6, 12, 6)) / M_glucose
o2_t = float(o2_needed(51, 98, 6)) / M_tripalm
eq("tripalmitin O2 per g vs glucose", round(o2_t / o2_g, 1), 2.7)
eq("tripalmitin O2 coefficient", float(o2_needed(51, 98, 6)), 72.5)
eq("energy value ratio lipid/carb (about 2.4)", round(39 / 16, 1), 2.4)

# --- energy example -----------------------------------------------------------------------------------
eq("20 g carbohydrate", 20 * 16, 320)
eq("20 g lipid", 20 * 39, 780)
eq("ratio 780/320", round(780 / 320, 1), 2.4)
eq("nuts", 9.0 * 39 + 2.0 * 17 + 2.5 * 16, 425)

# --- RQ from equations ---------------------------------------------------------------------------------
eq("glucose O2", float(o2_needed(6, 12, 6)), 6)
eq("glucose RQ", rq(6, 12, 6), 1.0)
assert atoms_ok(6, 12, 6)
eq("oleic O2", float(o2_needed(18, 34, 2)), 25.5)
assert atoms_ok(18, 34, 2)
eq("oleic H2O", 34 / 2, 17)
eq("oleic O atoms left 2+51", 2 + 2 * 25.5, 53)
eq("oleic O atoms right 36+17", 2 * 18 + 17, 53)
eq("oleic RQ", sf(rq(18, 34, 2), 2), 0.71)
eq("lauric O2", float(o2_needed(12, 24, 2)), 17)
assert atoms_ok(12, 24, 2)
eq("lauric RQ", sf(rq(12, 24, 2), 2), 0.71)
eq("lauric wrong inverted 1.4", sf(17 / 12, 2), 1.4)
eq("palmitic O2", float(o2_needed(16, 32, 2)), 23)
eq("palmitic RQ", sf(rq(16, 32, 2), 2), 0.70)
eq("sucrose O2", float(o2_needed(12, 22, 11)), 12)
eq("sucrose RQ", rq(12, 22, 11), 1.0)
eq("malic O2", float(o2_needed(4, 6, 5)), 3)
assert atoms_ok(4, 6, 5)
eq("malic RQ", sf(rq(4, 6, 5), 2), 1.3)
eq("glycerol O2", float(o2_needed(3, 8, 3)), 3.5)
eq("glycerol RQ", sf(rq(3, 8, 3), 2), 0.86)
eq("glycerol CO2/H2O wrong", 3 / 4, 0.75)
eq("glycerol inverted", sf(3.5 / 3, 3), 1.17)

# --- respirometer worked example ------------------------------------------------------------------------
r, d1, d2 = 0.50, 42, 12
vo2 = pi * r**2 * d1
vnet = pi * r**2 * d2
vco2 = pi * r**2 * (d1 - d2)
eq("eg O2 volume", sf(vo2, 2), 33)
eq("eg net volume", sf(vnet, 2), 9.4)
eq("eg CO2 volume", sf(vco2, 2), 24)
eq("eg O2 - net = CO2", vo2 - vnet, vco2, 1e-9)
eq("eg RQ", sf(vco2 / vo2, 2), 0.71)
eq("eg RQ from distances", sf((d1 - d2) / d1, 2), 0.71)
eq("eg wrong 12/42", sf(12 / 42, 2), 0.29)

# --- germination data ----------------------------------------------------------------------------------
for day, o2, co2, want in [(2, 40, 28, 0.70), (4, 55, 44, 0.80), (6, 70, 63, 0.90), (8, 84, 84, 1.0)]:
    eq(f"germination day {day} RQ", co2 / o2, want)
    eq(f"plot line at day {day}", 0.6 + 0.05 * day, want)

# --- practice ----------------------------------------------------------------------------------------------
eq("try respirometer O2", sf(pi * 0.40**2 * 35, 2), 18)
eq("try respirometer RQ", (35 - 7.0) / 35, 0.80)
eq("blowfly O2", sf(pi * 0.35**2 * 30, 2), 12)
eq("blowfly RQ", (30 - 6.0) / 30, 0.80)
eq("bacteria X", 52 / 52, 1.0)
eq("bacteria Y", sf(43 / 60, 2), 0.72)
f = (0.88 - 0.70) / (1.0 - 0.70)
eq("mixture fraction carbohydrate", f, 0.60, 1e-9)
eq("weighted average", 1.0 * 0.6 + 0.70 * 0.4, 0.88)
eq("quiz (25-3)/25", sf((25 - 3) / 25, 2), 0.88)
eq("quiz inverted 25/22", sf(25 / 22, 3), 1.14)
eq("quiz 22/28", sf(22 / 28, 2), 0.79)
eq("quiz 3/25", sf(3 / 25, 2), 0.12)

print("ok")
