# checks/bio.antibiotics.py: recomputes every number in chapters/bio.antibiotics.md
from math import isclose, exp, pi

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


area = lambda d: pi * (d / 2) ** 2

# --- doubling: 20 minutes, 10 hours --------------------------------------------------------------------------
divisions = 10 * 60 // 20
eq("30 divisions in 10 h", divisions, 30)
eq("2^30 about 1.1e9", sf(2 ** divisions / 1e9, 2), 1.1)

# --- :::plot resistant isolates (invented) and the worked example ---------------------------------------------
pct = lambda x: 5 + 55 / (1 + exp((6 - x) / 1.4))
eq("plot point year 4 label 16% (15.6)", round(pct(4), 1), 15.6)
eq("plot point year 8 label 49% (49.4)", round(pct(8), 1), 49.4)
eq("year 4 about 16", round(pct(4)), 16)
eq("year 8 about 49", round(pct(8)), 49)
eq("year 0 about 6", round(pct(0)), 6)
eq("year 12 about 59", round(pct(12)), 59)
eq("year 6 midpoint 32.5", pct(6), 32.5)
assert max(pct(x / 10) for x in range(0, 121)) < 60 and max(pct(x / 10) for x in range(0, 121)) < 80, "below the y axis top"
# fastest between years 4 and 8, slow before and after
d = lambda a, b: pct(b) - pct(a)
assert d(4, 8) > d(0, 4) and d(4, 8) > d(8, 12), "steepest between year 4 and year 8"
assert round(d(4, 8)) == 34 and round(d(0, 4)) == 10 and round(d(8, 12)) == 10

# --- worked example: disc diffusion (figure: A 22, B 12, C 6, D 18 mm; disc 6 mm) ------------------------------
eq("eg area A", sf(area(22)), 380)
eq("eg area B", sf(area(12)), 113)
eq("eg ratio A:B (unrounded)", sf(area(22) / area(12), 2), 3.4)
eq("eg ratio of diameters", sf(22 / 12, 2), 1.8)
eq("eg A minus disc", sf(area(22) - area(6)), 352)
eq("eg C zone equals disc", 6, 6)

# --- practice: try --------------------------------------------------------------------------------------------
eq("try S area", sf(area(28)), 616)
eq("try T area", sf(area(14)), 154)
eq("try ratio S:T", area(28) / area(14), 4.0, 1e-9)
eq("try 2^12", 2 ** (6 * 60 // 30), 4096)
eq("try resistant 3e9 x 1e-8", sf(3e9 * 1e-8), 30)

# --- practice: exam ------------------------------------------------------------------------------------------
eq("exam W area", sf(area(28)), 616)
use = [20, 40, 60, 80, 100, 120]
res = [8, 15, 24, 33, 41, 45]
steps = [b - a for a, b in zip(res, res[1:])]
eq("steps before the last", min(steps[:-1]), 7)
eq("steps before the last, max", max(steps[:-1]), 9)
eq("last step 100 to 120", steps[-1], 4)
eq("first and last res", res[-1], 45)
eq("TB both drugs", 1e-7 * 1e-8, 1e-15, 1e-30)
eq("TB drug A alone resistant", 1.0e9 * 1e-7, 100, 1e-6)
eq("TB both expected", 1.0e9 * 1e-15, 1e-6, 1e-18)
eq("country ratio", sf(62 / 18, 2), 3.4)

# --- quiz ------------------------------------------------------------------------------------------------------
eq("quiz area 20 mm", sf(area(20)), 314)
eq("quiz wrong 1257", sf(pi * 20 ** 2, 4), 1257)
eq("quiz wrong 62.8", sf(2 * pi * 10), 62.8)
eq("quiz wrong 31.4", sf(pi * 10), 31.4)

print("ok")
