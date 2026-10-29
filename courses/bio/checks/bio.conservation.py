# checks/bio.conservation.py: recomputes every number in the Conservation chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- fragmentation worked example: 4 km square, 16 patches of 1 km, edge zone 0.25 km
side, edge, patch = 4.0, 0.25, 1.0
core_before = (side - 2 * edge) ** 2
eq("core before", core_before, 12.25)
eq("core before %", sf(core_before / side**2 * 100), 76.6)
core_patch = (patch - 2 * edge) ** 2
eq("core of one patch", core_patch, 0.25)
core_after = 16 * core_patch
eq("core after", core_after, 4.0)
eq("core after %", core_after / side**2 * 100, 25.0)
eq("core lost %", sf((core_before - core_after) / core_before * 100), 67.3)
eq("edge before", 4 * side, 16)
eq("edge after", 16 * 4 * patch, 64)
eq("figure: edge zone px", edge * 25, 6.25)
eq("figure: core px before", (side - 2 * edge) * 25, 87.5)
eq("figure: core px patch", (patch - 2 * edge) * 25, 12.5)

# --- antelope reserve
yrs = [0, 5, 10, 15, 20]
pop = [24, 38, 61, 97, 150]
eq("increase", pop[-1] - pop[0], 126)
eq("percentage increase", (pop[-1] - pop[0]) / pop[0] * 100, 525)
eq("mean per year", 126 / 20, 6.3)
eq("first 5 y gain", pop[1] - pop[0], 14)
eq("last 5 y gain", pop[4] - pop[3], 53)
eq("first 5 y %", round((pop[1] / pop[0] - 1) * 100), 58)
eq("last 5 y %", round((pop[4] / pop[3] - 1) * 100), 55)

# --- practice
eq("perimeter before", 4 * 2, 8)
eq("perimeter after", 4 * 4, 16)
eq("seed viability", 170 / 200 * 100, 85)
seeds = [97, 95, 92, 84, 61]
eq("seed fall", seeds[0] - seeds[-1], 36)
eq("seed fall last 20 y", seeds[2] - seeds[4], 31)
eq("first below 85 at index 3 (30 y)", [i for i, v in enumerate(seeds) if v < 85][0], 3)
eq("early fall", seeds[0] - seeds[2], 5)

# --- stretch A: two plans, 36 km2
coreA = (6 - 2 * 0.5) ** 2
eq("plan A core", coreA, 25)
eq("plan A pairs", coreA // 2, 12)
coreB1 = (2 - 2 * 0.5) ** 2
eq("plan B core one block", coreB1, 1)
eq("plan B total core", 9 * coreB1, 9)
eq("plan B pairs", 0 if coreB1 < 2 else 9 * (coreB1 // 2), 0)
eq("plan B naive", 9 / 2, 4.5)

# --- stretch B: projects
eq("project 1 cost", 40 * 500, 20000)
eq("project 1 survivors", 40 / 2, 20)
eq("project 1 cost per frog", 20000 / 20, 1000)
eq("project 2 gain", 600 * 0.05, 30)

print("ok")
