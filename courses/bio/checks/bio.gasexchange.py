# checks/bio.gasexchange.py: recomputes every number in chapters/bio.gasexchange.md
from math import isclose, pi

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- warm-up: magnification ---------------------------------------------------------------------------------
eq("warm-up M", 60 / 0.4, 150, 1e-9)

# --- :::plot rate = 100 / thickness and the worked example ----------------------------------------------------
rate = lambda d: 100 / d
eq("plot thickness 0.5", rate(0.5), 200)
eq("plot thickness 1", rate(1), 100)
eq("plot thickness 3 (labelled 33.3 and 33)", round(rate(3), 1), 33.3)
eq("plot label 33", round(rate(3)), 33)
eq("doubling thickness halves rate", rate(2), rate(1) / 2)
eq("eg: percentage fall 1 -> 3", sf((100 - round(rate(3), 1)) / 100 * 100, 2), 67)
assert 0 < rate(4.5) < 230 and rate(0.5) < 230, "curve stays inside the y range"

# --- worked example: plan diagram of the trachea ---------------------------------------------------------------
M = 25 / 0.5
eq("eg magnification", M, 50)
A = 36 / M
eq("eg actual thickness mm", A, 0.72, 1e-12)
eq("eg actual thickness um", A * 1000, 720, 1e-9)

# --- practice ---------------------------------------------------------------------------------------------------
eq("try: bronchiole diameter mm", 45 / 150, 0.30, 1e-12)
eq("try: bronchiole diameter um", 45 / 150 * 1000, 300, 1e-9)
pf = [240, 300, 380, 420, 430, 430]
eq("exam asthma: increase 0 -> 20 min", sf((430 - 240) / 240 * 100, 2), 79)
eq("exam asthma: plateau", pf[-1], pf[-2])
M2 = 62 / 0.50
eq("exam: M = 124", M2, 124)
eq("exam: scale bar", 0.10 * M2, 12.4, 1e-9)

r_big, r_small = 2.0, 0.5
V_big = 4 / 3 * pi * r_big ** 3
V_small = 64 * 4 / 3 * pi * r_small ** 3
eq("stretch: volumes equal", V_big, V_small, 1e-9)
eq("stretch: volume 33.5", round(V_big, 1), 33.5)
S_big = 4 * pi * r_big ** 2
S_small = 64 * 4 * pi * r_small ** 2
eq("stretch: SA large", sf(S_big), 50.3)
eq("stretch: SA small", sf(S_small), 201)
eq("stretch: ratio 4.0", sf(S_small / S_big, 2), 4.0)

print("ok")
