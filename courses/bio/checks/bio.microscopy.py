# checks/bio.microscopy.py: recomputes every number in the Microscopy and magnification chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


UM_PER_MM = 1000
NM_PER_UM = 1000

# --- units ---------------------------------------------------------------------------------------------
eq("warm-up 0.025 mm", 0.025 * UM_PER_MM, 25)
eq("table 0.035 mm", 0.035 * UM_PER_MM, 35)
eq("table 7 um", 7 * NM_PER_UM, 7000)
eq("table 450 nm", 450 / NM_PER_UM, 0.45)
eq("table 6.5 um", 6.5 / UM_PER_MM, 0.0065)
eq("eg units 0.0065 mm -> um", 0.0065 * UM_PER_MM, 6.5)
eq("eg units 6.5 um -> nm", 6.5 * NM_PER_UM, 6500)
eq("standard form 6.5e-3", 6.5e-3, 0.0065)
eq("total magnification x40", 10 * 40, 400)
eq("total magnification x10", 10 * 10, 100)

# --- magnification -------------------------------------------------------------------------------------
eq("eg mitochondrion mm", 42 / 30000, 0.0014, 1e-12)
eq("eg mitochondrion um", 42 / 30000 * UM_PER_MM, 1.4, 1e-9)
eq("eg drawing", 90 * UM_PER_MM / 45, 2000)
eq("scale bar eg bar in um", 25 * UM_PER_MM, 25000)
eq("scale bar eg M", 25 * UM_PER_MM / 2, 12500)
eq("scale bar eg nucleus", 68 * UM_PER_MM / 12500, 5.44, 1e-9)
eq("scale bar eg nucleus ratio", 68 / 25 * 2, 5.44, 1e-9)
eq("scale bar eg 2 sf", sf(5.44, 2), 5.4)
eq("figure mitochondrion 3 bars", 3 * 0.5, 1.5)
eq("spot error 36 mm", 36 * UM_PER_MM, 36000)
eq("spot error M", 36 * UM_PER_MM / 12, 3000)
eq("malaria parasite mm", 2.5 / 1000, 0.0025, 1e-12)
eq("malaria parasite um", 2.5 / 1000 * UM_PER_MM, 2.5)
eq("malaria RBC um", 7.0 / 1000 * UM_PER_MM, 7.0)

# --- graticule -----------------------------------------------------------------------------------------
eq("graticule eg divisions", 6 * 10, 60)
eq("graticule eg unit", 60 / 25, 2.4)
eq("graticule eg cell", 18 * 2.4, 43.2, 1e-9)
eq("graticule eg 2 sf", sf(43.2, 2), 43)
eq("x10 cell units", 18 / 4, 4.5)
eq("x10 unit", 4 * 2.4, 9.6)
eq("x10 length", 4.5 * 9.6, 43.2, 1e-9)
eq("wrong calibration at x10", 4.5 * 2.4, 10.8, 1e-9)
# figure geometry: 25 units = 6 divisions, 10 px per unit
eq("figure division px", 25 * 10.0 / 6, 41.6666667, 1e-6)
eq("figure: 6 divisions end at 25 units", 6 * (25 * 10.0 / 6), 250)
eq("reading uncertainty 5 units", 0.5 / 5 * 100, 10)
eq("reading uncertainty 25 units", 0.5 / 25 * 100, 2)

# --- resolution ----------------------------------------------------------------------------------------
eq("0.15 um in nm", 0.15 * NM_PER_UM, 150)
assert 150 < 200
assert 150 > 0.5

# --- practice: try set ---------------------------------------------------------------------------------
eq("try 0.35 mm", 0.35 * UM_PER_MM, 350)
eq("try 850 nm", 850 / NM_PER_UM, 0.85)
eq("try total magnification", 10 * 40, 400)
eq("try drawing 12 cm", 12 * 10 * UM_PER_MM / 60, 2000)
eq("try photomicrograph mm", 27 / 600, 0.045, 1e-12)
eq("try photomicrograph um", 27 / 600 * UM_PER_MM, 45)
eq("try vesicle um", 6.0 / 20000 * UM_PER_MM, 0.3, 1e-12)
eq("try vesicle nm", 6.0 / 20000 * UM_PER_MM * NM_PER_UM, 300, 1e-9)
eq("try image length", 150 * 80 / UM_PER_MM, 12)
eq("try scale bar", 45 / 18 * 10, 25)

# --- practice: exam set --------------------------------------------------------------------------------
eq("exam pollen", 54 * UM_PER_MM / 30, 1800)
eq("exam calibration x10 stage", 20 * 10, 200)
eq("exam calibration x10 unit", 20 * 10 / 40, 5.0)
eq("exam calibration x40 stage", 5 * 10, 50)
eq("exam calibration x40 unit", 5 * 10 / 40, 1.25)
eq("exam cell at x40", 14 * 1.25, 17.5)
widths = [7, 8, 9, 8, 7, 9, 8, 8]
eq("cheek unit stage", 15 * 10, 150)
eq("cheek unit", 15 * 10 / 20, 7.5)
eq("cheek sum", sum(widths), 64)
eq("cheek mean units", sum(widths) / len(widths), 8.0)
eq("cheek mean um", sum(widths) / len(widths) * 7.5, 60)
eq("cheek min um", min(widths) * 7.5, 52.5)
eq("cheek max um", max(widths) * 7.5, 67.5)
assert widths.count(8) == 4
eq("yeast bar um", 30 * UM_PER_MM, 30000)
eq("yeast M", 30 * UM_PER_MM / 2, 15000)
eq("yeast diameter", 105 * UM_PER_MM / 15000, 7.0)
eq("drawing cell length", 16 * 2.5, 40)
eq("drawing M", 72 * UM_PER_MM / 40, 1800)
eq("0.1 um in nm", 0.1 * NM_PER_UM, 100)
# stretch
eq("photocopy M", 400 * 1.2, 480)
true_um = 30 / 480 * UM_PER_MM
used_um = 30 / 400 * UM_PER_MM
eq("photocopy true mm", 30 / 480, 0.0625, 1e-12)
eq("photocopy true um", true_um, 62.5)
eq("photocopy used um", used_um, 75)
eq("photocopy error %", (used_um - true_um) / true_um * 100, 20)
eq("field x400", 1.8 / 4, 0.45)
eq("field um", 0.45 * UM_PER_MM, 450)
eq("cells across field", 450 / 60, 7.5)

# --- quiz ----------------------------------------------------------------------------------------------
eq("quiz drawing", 40 * UM_PER_MM / 20, 2000)
eq("quiz graticule unit", 6 * 10 / 25, 2.4)
eq("quiz 0.0065 mm", 0.0065 * UM_PER_MM, 6.5)
eq("quiz recalibration factor", 40 / 10, 4)

print("ok")
