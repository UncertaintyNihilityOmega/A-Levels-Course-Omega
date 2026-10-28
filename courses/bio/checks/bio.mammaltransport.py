# checks/bio.mammaltransport.py: recomputes every number in chapters/bio.mammaltransport.md
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- worked example: wall thickness and lumen of plan diagrams -----------------------------------------
art_out, art_lum, vein_out, vein_lum = 46, 24, 40, 34
art_wall, vein_wall = (art_out - art_lum) / 2, (vein_out - vein_lum) / 2
eq("artery wall", art_wall, 11)
eq("vein wall", vein_wall, 3)
eq("artery ratio", sf(art_wall / art_lum, 2), 0.46)
eq("vein ratio", sf(vein_wall / vein_lum, 2), 0.088)
eq("ratio of ratios", sf((art_wall / art_lum) / (vein_wall / vein_lum), 2), 5.2)
eq("magnification of the artery drawing not used", 1, 1)

# --- worked example: differential count and magnification ------------------------------------------------
counts = {"neutrophils": 124, "lymphocytes": 56, "monocytes": 14, "other": 6}
assert sum(counts.values()) == 200
for k, pct in zip(counts, [62, 28, 7, 3]):
    eq(f"percentage {k}", counts[k] / 200 * 100, pct)
eq("percentages total", 62 + 28 + 7 + 3, 100)
eq("magnification of red cell drawing", 28 / (7 / 1000), 4000)

# --- practice (Start easy) ------------------------------------------------------------------------------
eq("try wall:lumen", 9 / 30, 0.30)
eq("try lymphocyte actual size in um", 36 / 3000 * 1000, 12)
eq("try monocyte percentage", 9 / 150 * 100, 6)

# --- exam practice: velocity table ----------------------------------------------------------------------
flow = 5.00 * 1000 / 60                                   # cm3 per s
eq("flow cm3 per s", sf(flow, 3), 83.3)
areas = {"aorta": 4.0, "arterioles": 400, "capillaries": 3000, "venules": 3500}
vel_mm = {k: flow / a * 10 for k, a in areas.items()}      # cm/s -> mm/s
eq("aorta velocity", sf(vel_mm["aorta"], 3), 208)
eq("arteriole velocity", sf(vel_mm["arterioles"], 3), 2.08)
eq("capillary velocity", sf(vel_mm["capillaries"], 3), 0.278)
eq("venule velocity", sf(vel_mm["venules"], 3), 0.238)
eq("aorta velocity in cm/s (working)", sf(flow / 4.0, 3), 20.8)

# --- exam practice: white cell table --------------------------------------------------------------------
healthy = [65, 25, 6, 4]
patient = [80, 14, 4, 2]
assert sum(healthy) == 100 and sum(patient) == 100
eq("percentage increase in neutrophils", sf((80 - 65) / 65 * 100, 2), 23)

# --- stretch: capillary pressures -------------------------------------------------------------------------
eq("arterial net", 4.0 - 3.0, 1.0)
eq("venous net", 1.5 - 3.0, -1.5)
eq("venous net with weak proteins", 1.5 - 1.2, 0.3, 1e-12)

print("ok")
