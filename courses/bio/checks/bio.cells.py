# checks/bio.cells.py: recomputes every number in the Eukaryotic cells and organelles chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


UM_PER_MM, NM_PER_UM = 1000, 1000

# warm-up
eq("warm-up 1.4 um in nm", 1.4 * NM_PER_UM, 1400)

# worked example: mitochondria per 100 um^2 (x5000, micrograph 90 mm x 70 mm)
M = 5000
w = 90 / M * UM_PER_MM
h = 70 / M * UM_PER_MM
eq("width mm", 90 / M, 0.018, 1e-12)
eq("width um", w, 18)
eq("height mm", 70 / M, 0.014, 1e-12)
eq("height um", h, 14)
area = w * h
eq("area", area, 252)
heart = 36 / area * 100
skin = 6 / area * 100
eq("heart per 100 um2", round(heart, 1), 14.3)
eq("skin per 100 um2", round(skin, 2), 2.38)
eq("skin 1 dp", round(skin, 1), 2.4)
eq("about six times", round(heart / skin), 6)

# try set
eq("try mitochondrion mm", 54 / 18000, 0.003, 1e-12)
eq("try mitochondrion um", 54 / 18000 * UM_PER_MM, 3.0)

# exam practice
eq("chloroplast mm", 48 / 12000, 0.004, 1e-12)
eq("chloroplast um", 48 / 12000 * UM_PER_MM, 4.0)
eq("microvillus mm", 3.2 / 4000, 0.0008, 1e-12)
eq("microvillus um", 3.2 / 4000 * UM_PER_MM, 0.80)
mito = {"W": 1800, "X": 300, "Y": 400, "Z": 120}
rer = {"W": 12, "X": 95, "Y": 10, "Z": 8}
lys = {"W": 20, "X": 15, "Y": 160, "Z": 4}
assert max(rer, key=rer.get) == "X" and rer["X"] == 95
assert max(lys, key=lys.get) == "Y" and lys["Y"] == 160
assert max(mito, key=mito.get) == "W" and mito["W"] == 1800
assert min(mito, key=mito.get) == "Z" and mito["Z"] == 120
assert (mito["X"], mito["Y"]) == (300, 400)

print("ok")
