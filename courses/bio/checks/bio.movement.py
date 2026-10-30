# checks/bio.movement.py: recomputes every number in the Movement into and out of cells chapter.
from math import pi, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- Warm-up --------------------------------------------------------------------------------------------------
eq("cube of side 3: V", 3 ** 3, 27)

# --- Cubes of side 1, 2, 3 (worked example) ---------------------------------------------------------------------
for L, sa, v, r in [(1, 6, 1, 6), (2, 24, 8, 3), (3, 54, 27, 2)]:
    eq(f"cube {L} SA", 6 * L ** 2, sa)
    eq(f"cube {L} V", L ** 3, v)
    eq(f"cube {L} SA:V", sa / v, r)
eq("double side: SA x4", 24 / 6, 4)
eq("double side: V x8", 8 / 1, 8)
eq("triple side: SA x9", 54 / 6, 9)
eq("triple side: V x27", 27 / 1, 27)

# --- Cuboid formula, cylinder worked example ---------------------------------------------------------------------
a, b, c = 4.0, 2.0, 1.0
eq("cuboid SA (practice)", 2 * (a * b + a * c + b * c), 28)
eq("cuboid V (practice)", a * b * c, 8)
eq("cuboid SA:V (3.5)", 28 / 8, 3.5)
r, h = 0.50, 4.0
sa = 2 * pi * r ** 2 + 2 * pi * r * h
v = pi * r ** 2 * h
eq("cylinder 2 pi r^2", round(2 * pi * r ** 2, 3), 1.571)
eq("cylinder curved", round(2 * pi * r * h, 3), 12.566)
eq("cylinder SA (14.1)", sf(sa), 14.1)
eq("cylinder V (3.14)", sf(v), 3.14)
eq("cylinder SA unrounded 14.137", round(sa, 3), 14.137)
eq("cylinder SA:V (4.5)", sf(sa / v, 2), 4.5)

# --- Agar cube worked example --------------------------------------------------------------------------------------
sides = [0.5, 1.0, 1.5, 2.0]
times = [160, 340, 600, 930]
for L, ratio in zip(sides, [12, 6, 4, 3]):
    eq(f"agar SA:V {L}", 6 / L, ratio)
rates = [1 / t for t in times]
for rt, want in zip(rates, [6.25e-3, 2.94e-3, 1.67e-3, 1.08e-3]):
    eq("agar rate", sf(rt, 3), want, 1e-12)
eq("time ratio 930/160 about 5.8", round(930 / 160, 1), 5.8)
assert all(t2 > t1 for t1, t2 in zip(times, times[1:])), "time rises as SA:V falls"

# --- Practice: cube of side 4 ---------------------------------------------------------------------------------------
eq("cube 4 SA", 6 * 4 ** 2, 96)
eq("cube 4 V", 4 ** 3, 64)
eq("cube 4 SA:V", 96 / 64, 1.5)

# --- Practice: sphere cells (stretch) --------------------------------------------------------------------------------
for R, want in [(5, 0.6), (50, 0.06)]:
    eq(f"sphere {R} SA:V = 3/r", (4 * pi * R ** 2) / (4 / 3 * pi * R ** 3), want, 1e-12)
eq("P is ten times Q", 0.6 / 0.06, 10, 1e-9)

# --- Practice: agar cubes with an acid front 0.30 cm in ---------------------------------------------------------------
front = 0.30
v1 = (1.0 - 2 * front) ** 3
v2 = (2.0 - 2 * front) ** 3
eq("1.0 cm unreached side 0.40", round(1.0 - 2 * front, 2), 0.40)
eq("1.0 cm unreached volume 0.064", round(v1, 3), 0.064)
eq("1.0 cm unreached 6.4%", round(v1 / 1.0 * 100, 1), 6.4)
eq("2.0 cm unreached side 1.4", round(2.0 - 2 * front, 2), 1.4)
eq("2.0 cm unreached volume 2.744", round(v2, 3), 2.744)
eq("2.0 cm unreached 34.3%", round(v2 / 8 * 100, 1), 34.3)
eq("SA:V 2 cm cube", 6 / 2.0, 3)
eq("SA:V 1 cm cube", 6 / 1.0, 6)

# --- :::plot 1: simple v facilitated diffusion -------------------------------------------------------------------------
simple = lambda x: 4 * x
facil = lambda x: 36 * x / (2 + x)
eq("plot point (10, 30)", facil(10), 30)
eq("simple at 12 is 48", simple(12), 48)
assert facil(12) < 36 and facil(12) > 30, "facilitated levels off below 36"
assert all(facil(x) > simple(x) for x in (0.5, 1, 2, 4)) and simple(12) > facil(12), "curves cross as stated in the plot"

# --- Practice: table of A and B ---------------------------------------------------------------------------------------
grad = [2, 4, 6, 8, 10, 12]
A = [8, 16, 24, 32, 40, 48]
B = [14, 24, 30, 33, 34, 34]
for g, a_ in zip(grad, A):
    eq(f"A = 4 x gradient {g}", 4 * g, a_)
assert all(y2 >= y1 for y1, y2 in zip(B, B[1:])), "B never falls"
assert B[4] == B[5] == 34 and B[0] == 14, "B levels off at 34 from gradient 10"
assert B[3] < 34, "B not yet level at gradient 8"

# --- Worked example: potato in sucrose --------------------------------------------------------------------------------
m0 = 2.50
conc = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
final = [2.95, 2.76, 2.59, 2.40, 2.23, 2.05]
pct = [(f - m0) / m0 * 100 for f in final]
for p, want in zip(pct, [18.0, 10.4, 3.6, -4.0, -10.8, -18.0]):
    eq("potato % change", round(p, 1), want)
eq("plot line 18 - 72x at 0", 18 - 72 * 0, 18)
eq("plot line at 0.5", 18 - 72 * 0.5, -18)
eq("plot line crosses at 0.25", 18 - 72 * 0.25, 0)
x_int = 0.2 + 0.1 * pct[2] / (pct[2] - pct[3])
assert abs(x_int - 0.25) < 0.005, f"data intercept {x_int} should be about 0.25"
eq("midpoint of -540 and -820 is -680", (-540 + -820) / 2, -680)
eq("dilution 2 cm3 stock + 8 cm3 water, 1.0 stock", 1.0 * 2 / 10, 0.2)

# --- Practice: carrot ------------------------------------------------------------------------------------------------
c0 = 3.00
cfinal = [3.29, 3.20, 3.10, 3.01, 2.92, 2.83]
cpct = [(f - c0) / c0 * 100 for f in cfinal]
eq("carrot 0.2 -> +3.3%", round(cpct[2], 1), 3.3)
eq("carrot 0.3 -> +0.3%", round(cpct[3], 1), 0.3)
eq("carrot 0.4 -> -2.7%", round(cpct[4], 1), -2.7)
cx = 0.3 + 0.1 * cpct[3] / (cpct[3] - cpct[4])
eq("carrot zero change at about 0.31", round(cx, 2), 0.31)
assert cpct[0] > 0 and cpct[-1] < 0 and cpct[3] > 0 > cpct[4], "sign change between 0.3 and 0.4"

# --- Practice: cell water potentials and the sucrose strips -----------------------------------------------------------
assert -300 > -700, "solution (-300) has the higher water potential than the cell (-700): water enters"
assert -400 > -650, "Y (-400) has the higher water potential than X (-650): water moves Y to X"
assert -900 < -650, "-900 solution is lower than cell X: water leaves"
assert -500 > -900, "plasmolysis example: cell -500 higher than solution -900: water leaves"
assert -1200 < -300 < -50 < 0, "quiz: -1200 is the lowest water potential"

# --- Practice: ion uptake -------------------------------------------------------------------------------------------
air, n2, cn = 8.4, 1.2, 0.9
assert air > n2 > cn, "uptake highest in air, lowest with cyanide"

# --- Practice: onion plasmolysis table ----------------------------------------------------------------------------------
oc = [0.20, 0.25, 0.30, 0.35, 0.40]
op = [0, 12, 48, 86, 100]
x50 = 0.30 + 0.05 * (50 - 48) / (86 - 48)
assert abs(x50 - 0.30) < 0.01, "50% plasmolysed at about 0.30"
assert all(y2 > y1 for y1, y2 in zip(op, op[1:])), "percentage rises with concentration"

# --- Quiz and recap --------------------------------------------------------------------------------------------------------
eq("6/L halves when L doubles", (6 / 4) / (6 / 2), 0.5)
eq("sodium-potassium pump 3 Na+ out", 3, 3)
eq("sodium-potassium pump 2 K+ in", 2, 2)

wp_table = [(0.1, -270), (0.2, -540), (0.3, -820), (0.4, -1100)]
assert all(b[1] < a[1] for a, b in zip(wp_table, wp_table[1:])), "water potential table falls as sucrose rises"
assert -820 < (-540 + -820) / 2 < -540, "potato water potential -680 lies between the two table values"

print("ok")
