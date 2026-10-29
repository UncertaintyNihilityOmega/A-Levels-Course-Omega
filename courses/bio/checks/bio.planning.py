# checks/bio.planning.py: recomputes every number in the Planning investigations chapter (chapters/bio.planning.md).
from math import isclose


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


# --- percentage uncertainty ---
eq("cylinder u", 1 / 2, 0.5)
eq("cylinder %", 0.5 / 20 * 100, 2.5)
eq("syringe u", 0.2 / 2, 0.1)
eq("syringe %", 0.1 / 20 * 100, 0.5)
eq("ratio", 2.5 / 0.5, 5)

# --- % (w/v) and mol dm-3 ---
eq("4% of 250", 4.0 * 250 / 100, 10)
eq("4.0 x 2.5", 4.0 * 2.5, 10)
mol = 0.20 * 100 / 1000
eq("glucose moles", mol, 0.020)
eq("glucose mass", mol * 180, 3.6)

# --- proportional dilution table: 20 cm3 from 1.0 stock ---
for cf, vs, vw in [(0.2, 4, 16), (0.4, 8, 12), (0.6, 12, 8), (0.8, 16, 4)]:
    eq(f"stock {cf}", cf * 20 / 1.0, vs)
    eq(f"water {cf}", 20 - vs, vw)

# --- serial dilution (figure): tenfold from 0.10 ---
c = 0.10
for want in [0.010, 0.0010, 0.00010]:
    c = c * 1 / (1 + 9)
    eq("serial", c, want, 1e-12)
eq("1 + 9", 1 + 9, 10)
# plan 1 concentrations: 0.10 .. 0.000010 by tenfold steps
c = 0.10
series = [c]
for _ in range(4):
    c /= 10
    series.append(c)
for got, want in zip(series, [0.10, 0.010, 0.0010, 0.00010, 0.000010]):
    eq("plan1 series", got, want, 1e-12)
eq("plan 1 dishes", 6 * 3, 18)

# --- easy practice ---
eq("NaOH 5% 200", 5.0 * 200 / 100, 10)
sucrose = 0.40 * 0.250
eq("sucrose moles", sucrose, 0.100)
eq("sucrose mass", sucrose * 342, 34.2)
eq("stock 0.30", 0.30 * 25 / 1.5, 5)
eq("water 0.30", 25 - 5, 20)
eq("serial practice 1", 1.0 / 10, 0.10)
eq("serial practice 2", 0.10 / 10, 0.010)
eq("serial practice 3", 0.010 / 10, 0.0010, 1e-12)
eq("balance mean", round((5.2 + 5.2 + 5.3) / 3, 2), 5.23)
assert abs(5.23 - 5.00) > 0.1 and max(5.2, 5.2, 5.3) - min(5.2, 5.2, 5.3) <= 0.1

# --- exam practice ---
mol = 0.25 * 0.500
eq("NaCl moles", mol, 0.125)
eq("NaCl mass", round(mol * 58.5, 1), 7.3)
eq("NaCl mass exact", mol * 58.5, 7.3125)
eq("NaCl %", round(7.3125 / 500 * 100, 1), 1.5)
for cf, vs, vw in [(0.4, 2, 8), (0.8, 4, 6), (1.2, 6, 4), (1.6, 8, 2)]:
    eq(f"glucose stock {cf}", cf * 10 / 2.0, vs)
    eq(f"glucose water {cf}", 10 - vs, vw)

# --- stretch ---
eq("cyl 12", round(0.5 / 12 * 100, 1), 4.2)
eq("syr 12", round(0.1 / 12 * 100, 2), 0.83)
eq("time", 0.5 / 20 * 100, 2.5)
assert 2.5 > 0.83

# --- quiz ---
eq("quiz stock", 0.30 * 10 / 1.0, 3.0)
eq("quiz water", 10 - 3.0, 7.0)
eq("quiz 500 cm3 2%", 2.0 * 500 / 100, 10)
eq("quiz serial", 0.50 / 10, 0.050)
print("ok")
