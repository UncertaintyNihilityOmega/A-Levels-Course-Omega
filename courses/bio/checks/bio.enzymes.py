# checks/bio.enzymes.py: recomputes every number in the Enzymes chapter (chapters/bio.enzymes.md).
from math import exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


def dp(x, k):
    return round(x + 0.0, k)


# --- Progress curve (:::plot) and the catalase worked example -------------------------------------------
V = lambda t: 48 * (1 - exp(-t / 40))           # model behind the plot and the table
times = [0, 10, 20, 30, 40, 60, 80, 100, 120]
table = [0, 11, 19, 25, 30, 37, 42, 44, 46]
for t, v in zip(times, table):
    eq(f"catalase table at {t} s", round(V(t)), v)
eq("initial rate = gradient of model at t = 0", 48 / 40, 1.2)
eq("tangent 1.2 t reaches 48 at 40 s", 1.2 * 40, 48)
eq("plateau of the curve", V(1e6), 48, 1e-6)
eq("mean rate first 30 s", sf(25 / 30, 2), 0.83)
eq("mean rate 60-120 s", (46 - 37) / 60, 0.15)

# --- Amylase end-point example -------------------------------------------------------------------------
conc = [0.2, 0.4, 0.6, 0.8, 1.0]
tend = [600, 300, 210, 150, 120]
rates = [1 / t for t in tend]
for r, w in zip(rates, [1.67e-3, 3.33e-3, 4.76e-3, 6.67e-3, 8.33e-3]):
    eq("amylase 1/t", sf(r), w)
eq("0.2% -> 0.4% doubles rate", rates[1] / rates[0], 2)
eq("1.0% gives five times the rate of 0.2%", rates[4] / rates[0], 5)
for t in tend:
    assert t % 30 == 0, "end-point times must be multiples of the 30 s sampling interval"
eq("uncertainty 30 s in 120 s", 30 / 120 * 100, 25)

# --- Colorimeter example ---------------------------------------------------------------------------------
cal_c = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
cal_a = [0.00, 0.16, 0.32, 0.48, 0.64, 0.80]
for c, a in zip(cal_c, cal_a):
    eq("calibration line absorbance = 0.80 c", 0.80 * c, a, 1e-12)
samp = {0: 0.80, 60: 0.56, 120: 0.36, 180: 0.22}
cs = {t: a / 0.80 for t, a in samp.items()}
eq("starch at 0 s", cs[0], 1.00, 1e-12)
eq("starch at 60 s", cs[60], 0.70, 1e-12)
eq("starch at 120 s", cs[120], 0.45, 1e-12)
eq("starch at 180 s (unrounded 0.275)", cs[180], 0.275, 1e-12)
from decimal import Decimal, ROUND_HALF_UP
eq("starch at 180 s to 2 s.f. (0.275 rounds half up)",
   float((Decimal(22) / Decimal(80)).quantize(Decimal("0.01"), ROUND_HALF_UP)), 0.28)
eq("rate first 60 s", (cs[0] - cs[60]) / 60, 0.0050, 1e-12)
eq("rate 120-180 s", sf((cs[120] - cs[180]) / 60, 2), 0.0029)

# --- Temperature :::plot (model curve) ------------------------------------------------------------------
T = lambda x: 7 * 2 ** (x / 10) / (1 + exp((x - 45) / 2.5))
peak = max((T(x / 100), x / 100) for x in range(0, 8001))
eq("optimum of the model near 41 °C", round(peak[1]), 41)
eq("peak rate about 100", round(peak[0]), 100)
eq("pt optimum (41, 100)", round(T(41)), 100)
eq("pt denaturation (50, 26.7)", round(T(50), 1), 26.7)
eq("curve cut at 64 °C is already below 0.5", round(T(64), 1), 0.3)
eq("rate at 0 °C about 7", round(T(0), 1), 7.0)
assert T(60) < 1.5, "almost zero by 60 °C"
eq("roughly doubles 10 -> 20 °C in the model", round(T(20) / T(10), 1), 2.0)

# --- Temperature worked example (salivary amylase table) ------------------------------------------------
temps = [10, 20, 30, 40, 50, 60, 70]
r = [12, 25, 47, 70, 38, 6, 0]
eq("optimum in the table at 40 °C", temps[r.index(max(r))], 40)
eq("maximum rate 70", max(r), 70)
eq("rate about doubles 10 -> 20 °C", round(r[1] / r[0]), 2)

# --- pH :::plot ----------------------------------------------------------------------------------------
pep = lambda x: 100 * exp(-((x - 2) / 1.3) ** 2)
amy = lambda x: 100 * exp(-((x - 7) / 1.3) ** 2)
eq("pepsin peak at pH 2", pep(2), 100)
eq("amylase peak at pH 7", amy(7), 100)
assert pep(5) < 1 and amy(4) < 1 and amy(10) < 1, "almost zero away from the optimum"

# --- Enzyme concentration :::plot ------------------------------------------------------------------------
lim = lambda x: (20 * x + 60 - abs(20 * x - 60)) / 2
eq("limited substrate plateau 60", lim(5), 60)
eq("plateau starts at 3", lim(3), 60)
eq("excess line at 5.5", 20 * 5.5, 110)
eq("lines identical below 3", lim(2), 40)

# --- Substrate concentration :::plot ---------------------------------------------------------------------
S = lambda x: 100 * x / (3 + x)
eq("pt (2, 40)", S(2), 40)
eq("pt (30, 90.9)", round(S(30), 1), 90.9)
assert S(40) < 100, "curve stays below Vmax = 100"

# --- Practice ------------------------------------------------------------------------------------------
eq("try: 18 cm3 in 45 s", 18 / 45, 0.40)
eq("try: 1/270", sf(1 / 270), 3.70e-3)
eq("try: % decrease 40.0 -> 16.0", (40.0 - 16.0) / 40.0 * 100, 60)
eq("exam Q2: 1/240", sf(1 / 240), 4.17e-3)
eq("exam Q2: 1/90", sf(1 / 90), 1.11e-2)
eq("exam Q3: 15/20", 15 / 20, 0.75)
lipase = dict(zip([5, 6, 7, 8, 9, 10, 11], [4, 11, 26, 42, 50, 31, 9]))
eq("exam Q4: optimum pH 9", max(lipase, key=lipase.get), 9)
c2 = (0.90 - 0.66) / 0.075
c6 = (0.90 - 0.39) / 0.075
eq("exam Q6: maltose at 2 min", c2, 3.2, 1e-9)
eq("exam Q6: maltose at 6 min", c6, 6.8, 1e-9)
eq("exam Q6: rate 2-6 min", (c6 - c2) / 4, 0.90, 1e-9)
q = [6.0, 12.6, 25.2, 37.8, 18.9]
eq("stretch Q10 10-20", q[1] / q[0], 2.1, 1e-9)
eq("stretch Q10 30-40", q[3] / q[2], 1.5, 1e-9)
eq("stretch Q10 40-50", q[4] / q[3], 0.5, 1e-9)

# --- Quiz ----------------------------------------------------------------------------------------------
eq("quiz: 1/250", 1 / 250, 4.0e-3)

print("ok")
