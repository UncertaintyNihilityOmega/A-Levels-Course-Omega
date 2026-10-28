# checks/bio.f.basics.py: recomputes every number in Biology from zero (chapters/bio.f.basics.md).
from math import isclose, log10, exp

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- glucose formula ---------------------------------------------------------------------------------
eq("atoms in glucose", 6 + 12 + 6, 24)

# --- pH (log scale) ----------------------------------------------------------------------------------
eq("pH 3 vs pH 5", 10 ** (5 - 3), 100)
eq("pH 2 vs pH 4", 10 ** (4 - 2), 100)
eq("pH 2 vs pH 8", 10 ** (8 - 2), 1_000_000)

# --- unit conversions --------------------------------------------------------------------------------
eq("eg 0.025 mm in um", 0.025 * 1000, 25)
eq("eg 25 um in nm", 25 * 1000, 25000)
eq("eg virus 1.2e-7 m in nm", 1.2e-7 * 1e9, 120, 1e-6)
eq("eg virus in um", 120 / 1000, 0.12)
eq("try 3.2 mm in um", 3.2 * 1000, 3200)
eq("try 450 um in mm", 450 / 1000, 0.45)
eq("try 0.7 um in nm", 0.7 * 1000, 700)
eq("quiz 25 um in mm", 25 / 1000, 0.025)
eq("EP1 3 um in nm", 3 * 1000, 3000)
eq("EP1 40 um in nm", 40 * 1000, 40000)
eq("EP4 3.5 um in mm", 3.5 / 1000, 0.0035)
eq("EP4 0.062 mm in um", 0.062 * 1000, 62)
eq("EP4 62 um in m", 62e-6, 6.2e-5, 1e-12)
# size ordering example (nm)
sizes = {"atom": 0.1, "protein": 8, "virus": 100, "bacterium": 2 * 1000, "animal cell": 20 * 1000}
eq("eg order: bacterium nm", sizes["bacterium"], 2000)
eq("eg order: animal cell nm", sizes["animal cell"], 20000)
assert sorted(sizes, key=sizes.get) == ["atom", "protein", "virus", "bacterium", "animal cell"]
sizes2 = {"glucose": 1, "protein": 6, "virus": 90, "bacterium": 3000, "plant cell": 40000}
assert sorted(sizes2, key=sizes2.get) == ["glucose", "protein", "virus", "bacterium", "plant cell"]
n += 2

# --- size ladder figure (log positions used in data/fig_bio.f.basics.py) --------------------------------
eq("log10 5 nm", sf(log10(5) + 1, 4), 1.699)
eq("log10 20 nm", sf(log10(20) + 1, 4), 2.301)
eq("log10 300 nm", sf(log10(300) + 1, 4), 3.477)
eq("log10 5 um", sf(log10(5000) + 1, 4), 4.699)
eq("log10 30 um", sf(log10(30000) + 1, 4), 5.477)
eq("plant cell vs atom", 100 * 1000 / 0.1, 1_000_000)

# --- standard form and rounding -----------------------------------------------------------------------
eq("4 500 000", 4.5e6, 4500000)
eq("0.000 003", 3e-6, 0.000003, 1e-15)
eq("0.000 045 m", 4.5e-5, 0.000045, 1e-15)
eq("62 000", 6.2e4, 62000)
eq("0.00035", 3.5e-4, 0.00035, 1e-15)
eq("0.004071 to 2 sf", sf(0.004071, 2), 0.0041)
eq("7.396 to 3 sf", sf(7.396, 3), 7.40)
eq("15 960 to 3 sf", sf(15960, 3), 16000)
eq("25.0/12 to 2 sf", sf(25.0 / 12, 2), 2.1)
eq("25.0/12 to 3 sf", sf(25.0 / 12, 3), 2.08)

# --- percentages and means -------------------------------------------------------------------------------
eq("18 out of 60", 18 / 60 * 100, 30)
eq("mean 12.1 12.4 11.8", sf((12.1 + 12.4 + 11.8) / 3, 3), 12.1)
eq("try mean 8.4 8.9 8.6", sf((8.4 + 8.9 + 8.6) / 3, 2), 8.6)
eq("sum 8.4 8.9 8.6", 8.4 + 8.9 + 8.6, 25.9, 1e-9)

start = 2.50
potato = {0.0: 2.95, 0.2: 2.70, 0.4: 2.50, 0.6: 2.30, 0.8: 2.15}
want = {0.0: 18, 0.2: 8, 0.4: 0, 0.6: -8, 0.8: -14}
for c, m in potato.items():
    eq(f"eg potato % change at {c}", (m - start) / start * 100, want[c], 1e-9)
# Spot the error
eq("spot: change in mass", 3.40 - 4.00, -0.60, 1e-9)
eq("spot: wrong answer", sf(-0.60 / 3.40 * 100, 3), -17.6)
eq("spot: right answer", (3.40 - 4.00) / 4.00 * 100, -15, 1e-9)
# practice
eq("try leaf % change", (5.20 - 6.50) / 6.50 * 100, -20, 1e-9)
carrot = {0.0: 4.48, 0.1: 4.20, 0.2: 4.00, 0.3: 3.76, 0.4: 3.60}
cw = {0.0: 12, 0.1: 5, 0.2: 0, 0.3: -6, 0.4: -10}
for c, m in carrot.items():
    eq(f"EP carrot % change at {c}", (m - 4.00) / 4.00 * 100, cw[c], 1e-9)
quiz_pc = (15.0 - 20.0) / 20.0 * 100
eq("quiz % change", quiz_pc, -25, 1e-9)
eq("quiz wrong denominator", sf(-5.0 / 15.0 * 100, 2), -33)
# successive percentages
m1 = 8.00 * 1.25
m2 = m1 * 0.80
eq("stretch week 1", m1, 10.00)
eq("stretch week 2", m2, 8.00)
eq("stretch 25% of 8", 0.25 * 8.00, 2.00)
eq("stretch 20% of 10", 0.20 * 10.00, 2.00)
eq("stretch net change", (m2 - 8.00) / 8.00 * 100, 0, 1e-9)

# --- gradients and rates -------------------------------------------------------------------------------
eq("eg gradient", (30 - 12) / (50 - 20), 0.60)
eq("plot line at 60 s", 0.6 * 60, 36)
eq("plot line at 20 s", 0.6 * 20, 12)
eq("plot line at 50 s", 0.6 * 50, 30)
eq("tangent gradient 20/25", 20 / 25, 0.8)
eq("curve plateau", 20 * (1 - exp(-1e6)), 20, 1e-9)
eq("curve initial slope", 20 / 25, 0.8)
eq("tangent at 25 s", 0.8 * 25, 20)
eq("try oxygen rate", (25 - 5) / (50 - 10), 0.50)
gas = {0: 0, 20: 14, 40: 24, 60: 30, 80: 34, 100: 36}
eq("EP gas rate first 20 s", gas[20] / 20, 0.70)
eq("EP gas rate 60-100 s", (gas[100] - gas[60]) / (100 - 60), 0.15)

# --- surface area to volume --------------------------------------------------------------------------------
for L, sa, v, r in ((2, 24, 8, 3), (4, 96, 64, 1.5), (8, 384, 512, 0.75)):
    eq(f"cube {L} SA", 6 * L * L, sa)
    eq(f"cube {L} V", L ** 3, v)
    eq(f"cube {L} ratio", sa / v, r)
eq("try cube 3 SA", 6 * 3 * 3, 54)
eq("try cube 3 V", 3 ** 3, 27)
eq("try cube 3 ratio", 54 / 27, 2)
eq("EP 27 small cubes SA", 27 * 6 * 1 * 1, 162)
eq("EP small cube ratio", 162 / 27, 6)
eq("EP ratio rise", 6 / 2, 3)
# stretch: supply 1.0 per cm2, need 3.0 per cm3
for L, sup, need in ((1, 6, 3), (2, 24, 24), (3, 54, 81)):
    eq(f"stretch supply {L}", 6 * L * L * 1.0, sup)
    eq(f"stretch need {L}", L ** 3 * 3.0, need)
assert 6 * 2 * 2 >= 3 * 2 ** 3 and 6 * 3 * 3 < 3 * 3 ** 3
n += 1
print("ok")
