# checks/bio.homeostasis.py: recomputes every number in the Homeostasis and the kidney chapter (chapters/bio.homeostasis.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- worked example: plasma, filtrate and urine (glucose, protein, urea) ---------------------------------------
plasma = {"glucose": 1.0, "protein": 70, "urea": 0.3}
filtrate = {"glucose": 1.0, "protein": 0.0, "urea": 0.3}
urine = {"glucose": 0.0, "protein": 0.0, "urea": 20}
eq("filtrate glucose = plasma glucose", filtrate["glucose"], plasma["glucose"])
eq("filtrate urea = plasma urea", filtrate["urea"], plasma["urea"])
eq("urea in urine / urea in filtrate (about 67 times)", round(urine["urea"] / filtrate["urea"]), 67)

# --- practice: percentage of the filtrate reabsorbed (150 dm3 filtrate, 2.5 dm3 urine) ---------------------------
eq("percentage reabsorbed", sf((150 - 2.5) / 150 * 100, 3), 98.3)

# --- text: 180 dm3 of filtrate, 1.5 dm3 of urine -> over 99% reabsorbed ------------------------------------------------
assert (180 - 1.5) / 180 > 0.99, "text says over 99% of the water is reabsorbed"
n += 1

# --- exam practice: PCT glucose table falls from 5.0 to 0.0 over 12 mm ----------------------------------------
glc = [5.0, 3.5, 1.8, 0.4, 0.0]
assert all(a > b for a, b in zip(glc, glc[1:])), "glucose must fall along the PCT"
n += 1

# --- exam practice: volunteer table (urine flow and ADH) ------------------------------------------------------------
flow = [1, 3, 12, 10, 4]
adh = [9, 5, 2, 3, 7]
eq("maximum urine flow is at 60 min", flow.index(max(flow)), 2)
eq("minimum ADH is at 60 min", adh.index(min(adh)), 2)
eq("flow at 60 min / flow at 0 min", flow[2] / flow[0], 12)

# --- exam practice: relative molecular masses in order ---------------------------------------------------------------------
rmm = [18, 60, 180, 69000]
assert rmm == sorted(rmm)
n += 1

# --- stretch: set point 37 -> 39 °C, a rise of 2 °C ------------------------------------------------------------------------------
eq("fever set point rise", 39 - 37, 2)

print(f"ok ({n} checks)")
