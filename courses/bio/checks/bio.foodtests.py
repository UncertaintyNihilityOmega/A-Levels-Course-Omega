# checks/bio.foodtests.py: recomputes every number in the Testing for biological molecules chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- Semi-quantitative worked example and :::plot: time = 120 / concentration -----------------------------
conc = [0.5, 1.0, 1.5, 2.0, 2.5]
time = [240, 120, 80, 60, 48]
for c, t in zip(conc, time):
    eq(f"t x c = 120 at {c}%", c * t, 120, 1e-9)
eq("curve value at 0.5%", 120 / 0.5, 240)
eq("time halves when concentration doubles 0.5 -> 1.0", time[0] / time[1], 2)
eq("rate 1/t at 1.0% (8.33e-3)", sf(1 / 120), 8.33e-3)
eq("rate at 2.0% (1.67e-2)", sf(1 / 60), 1.67e-2)
eq("rate proportional to concentration: rate(2.0)/rate(1.0)", (1 / 60) / (1 / 120), 2)
eq("unknown 100 s -> 1.2 %", 120 / 100, 1.2)
eq("plot point (1.2, 100)", 120 / 1.2, 100)
assert 120 / 0.45 < 340, "curve start stays inside the y range"
assert 120 / 2.9 > 30, "curve end is above the x-axis"

# --- Serial dilution worked example -----------------------------------------------------------------------
c = 2.0
steps = []
for _ in range(4):
    c = c * 5 / 10
    steps.append(c)
eq("first tube 1.0 %", steps[0], 1.0)
eq("second tube 0.50 %", steps[1], 0.50)
eq("third tube 0.25 %", steps[2], 0.25)
eq("fourth tube 0.125 %", steps[3], 0.125)
eq("c4 = 2.0 x (1/2)^4", 2.0 * 0.5 ** 4, 0.125)

# --- Practice -------------------------------------------------------------------------------------------
eq("try: 3.2 -> 0.20 takes 4 halvings", 3.2 * 0.5 ** 4, 0.20, 1e-12)
eq("try: chain 3.2 -> 1.6 -> 0.80 -> 0.40", 3.2 / 8, 0.40, 1e-12)
eq("exam Q4: 1/100", 1 / 100, 1.0e-2)
std_c = [0.3, 0.6, 0.9, 1.2]
std_t = [300, 150, 100, 75]
for cc, tt in zip(std_c, std_t):
    eq(f"exam Q4: t x c = 90 at {cc}%", cc * tt, 90, 1e-9)
eq("exam Q4: unknown 120 s -> 0.75 %", 90 / 120, 0.75)
assert 0.7 <= 90 / 120 <= 0.8
# colorimeter question: absorbance 0.80 at 0, falling 0.16 per 10 g/dm3
slope = 0.16 / 10
eq("exam Q6: slope 0.016", slope, 0.016, 1e-12)
eq("exam Q6: fall 0.80 - 0.37", 0.80 - 0.37, 0.43, 1e-12)
eq("exam Q6: concentration 26.875 -> 27", sf((0.80 - 0.37) / slope, 2), 27)
eq("exam Q6: calibration reaches 0.16 at 40 g/dm3", 0.80 - slope * 40, 0.16, 1e-12)
# stretch protease/biuret
eq("stretch Q2: (0.60 - 0.32) / 20", (0.60 - 0.32) / 20, 0.014, 1e-12)

print("ok")
