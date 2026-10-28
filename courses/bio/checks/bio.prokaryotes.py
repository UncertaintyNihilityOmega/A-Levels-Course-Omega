# checks/bio.prokaryotes.py: recomputes every number in the Prokaryotes and viruses chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


UM_PER_MM, NM_PER_UM, NM_PER_MM = 1000, 1000, 1_000_000

# warm-up
eq("warm-up 2 um in nm", 2 * NM_PER_UM, 2000)

# bacterium range
eq("1 um in nm", 1 * NM_PER_UM, 1000)
eq("5 um in nm", 5 * NM_PER_UM, 5000)

# worked example: TEM, bar 20 mm = 0.5 um, bacterium 72 mm x 26 mm
bar_um = 20 * UM_PER_MM
eq("bar in um", bar_um, 20000)
eq("M", bar_um / 0.5, 40000)
eq("length ratio method", 72 / 20 * 0.5, 1.8)
eq("length magnification method", 72 * UM_PER_MM / 40000, 1.8)
eq("width ratio method", 26 / 20 * 0.5, 0.65)
eq("width magnification method", 26 * UM_PER_MM / 40000, 0.65)

# worked example: virus particle
eq("2 um in nm", 2 * NM_PER_UM, 2000)
eq("bacterium vs virus", 2000 / 100, 20)
eq("virus image nm", 100 * 200000, 20_000_000)
eq("virus image mm", 100 * 200000 / NM_PER_MM, 20)

# try set
eq("try drawing mm to um", 15 * UM_PER_MM, 15000)
eq("try M", 15 * UM_PER_MM / 3, 5000)
eq("try virus image nm", 80 * 150000, 12_000_000)
eq("try virus image mm", 80 * 150000 / NM_PER_MM, 12)
assert 100 < 200 < 2 * NM_PER_UM

# exam practice
eq("bar um", 30 * UM_PER_MM, 30000)
eq("M", 30 * UM_PER_MM / 1, 30000)
eq("bacterium length", 66 / 30 * 1, 2.2)
eq("2.0 um in nm", 2.0 * NM_PER_UM, 2000)
eq("ratio", 2000 / 100, 20)
eq("RBC image um", 35 * UM_PER_MM, 35000)
eq("RBC M", 35 * UM_PER_MM / 7.0, 5000)
sizes = {"virus": 100e-3, "mito": 1.5, "bacterium": 2.0, "rbc": 7.0}     # in um
assert sorted(sizes, key=sizes.get) == ["virus", "mito", "bacterium", "rbc"]
assert [k for k, v in sizes.items() if v < 0.2] == ["virus"]

# stretch
eq("6 mm in nm", 6 * NM_PER_MM, 6_000_000)
eq("M needed", 6 * NM_PER_MM / 120, 50000)
eq("image at x1500 nm", 120 * 1500, 180000)
eq("image at x1500 mm", 120 * 1500 / NM_PER_MM, 0.18)

# quiz
eq("quiz actual", 40 / 20000 * UM_PER_MM, 2.0)

print("ok")
