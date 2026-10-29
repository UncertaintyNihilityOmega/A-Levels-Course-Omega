# checks/bio.limiting.py: recomputes every number in the Limiting factors chapter (chapters/bio.limiting.md).
from math import isclose, exp, pi, sqrt

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- the model behind the :::plot curves and the widget -------------------------------------------------------
SLOPE, A, KC = 1.6, 112, 0.072
f = lambda T: 2 ** (T / 10) / (1 + exp((T - 35) / 2.5))
F25 = f(25)
eq("f(25) written as 5.555 in the plot", sf(F25, 4), 5.555)
pmaxC = lambda C: A * C / (C + KC)
blackman = lambda a, b: (a + b - abs(a - b)) / 2          # = min(a, b), as written in the :::plot formulas
# plot 1
eq("plateau 0.04% CO2", pmaxC(0.04), 40, 1e-9)
eq("plateau 0.12% CO2", pmaxC(0.12), 70, 1e-9)
eq("light-limited corner for 40", 40 / SLOPE, 25)
eq("light-limited corner for 70", 70 / SLOPE, 43.75)
eq("point A on the rising line", SLOPE * 12, 19.2, 1e-9)
eq("blackman = min", blackman(SLOPE * 12, 40), 19.2, 1e-9)
# plot 3: CO2 curves
eq("bright light at 0.16", sf(pmaxC(0.16), 3), 77.2)
eq("dim light reached at (about 0.02)", sf(24 * KC / (A - 24), 2), 0.02)
eq("point bright 0.04", pmaxC(0.04), 40, 1e-9)
# plot 4: temperature curves
P = lambda T: 70 * f(T) / 5.555
Tpk = max((t / 10 for t in range(0, 600)), key=f)
assert 30.5 <= Tpk <= 31.5, Tpk
eq("peak rate in bright light", sf(P(Tpk), 3), 90.0, 0.2)
eq("point on plot 4", 89.9, round(P(31), 1), 0.0)
eq("rate at 5 C in bright light", round(P(5)), 18)
eq("rate at 42 C (curve stops here)", round(P(42)), 13)
eq("plot 2 plateau at 15 C", round(pmaxC(0.12) * f(15) / F25), 36)
eq("dim light flat at 24 in the range 9 to 40 C", min(blackman(24, P(t)) for t in (10, 20, 30, 40)), 24, 0.1)
assert P(8) < 24 < P(10)                                # dim curve leaves the 24 line between 8 and 10 C
# plot 2 points
eq("A on both curves", SLOPE * 20, 32)
eq("B", 36, 36)
eq("C", 70, 70)

# --- inverse square law worked example ------------------------------------------------------------------------
eq("I at 20 cm", 100 * (10 / 20) ** 2, 25)
eq("I at 40 cm", 100 * (10 / 40) ** 2, 6.25)
eq("I at 20 -> 40 is quarter", 6.25 / 25, 0.25)
eq("practice I at 36 cm", sf(100 * (12 / 36) ** 2, 3), 11.1)
eq("quiz 30 -> 15 cm is four times", (30 / 15) ** 2, 4)

# --- DCPIP worked example -----------------------------------------------------------------------------------
a10 = [0.82, 0.66, 0.51, 0.38, 0.30, 0.24]
a30 = [0.82, 0.77, 0.72, 0.68, 0.63, 0.59]
r10, r30 = (a10[0] - a10[2]) / 2, (a30[0] - a30[2]) / 2
eq("rate at 10 cm", r10, 0.155, 1e-9)
eq("rate at 30 cm", r30, 0.050, 1e-9)
eq("rate ratio", sf(r30 / r10, 2), 0.32)
eq("intensity ratio", (10 / 30) ** 2, 1 / 9)
assert r30 / r10 > 2 * (10 / 30) ** 2                      # rate falls far less than the intensity
assert all(b < a for a, b in zip(a10, a10[1:])) and all(b < a for a, b in zip(a30, a30[1:]))

# --- glasshouse economics example ----------------------------------------------------------------------------
co2 = [0.04, 0.08, 0.12, 0.16]
yld = [80, 92, 98, 99]
cost = [0, 1500, 3200, 5000]
price = 500
nets = []
for i in range(1, 4):
    gain = (yld[i] - yld[i - 1]) * price
    extra = cost[i] - cost[i - 1]
    nets.append(gain - extra)
eq("step 1 extra income", (92 - 80) * price, 6000)
eq("step 1 net", nets[0], 4500)
eq("step 2 extra income", (98 - 92) * price, 3000)
eq("step 2 extra cost", 3200 - 1500, 1700)
eq("step 2 net", nets[1], 1300)
eq("step 3 extra income", (99 - 98) * price, 500)
eq("step 3 extra cost", 5000 - 3200, 1800)
eq("step 3 net", nets[2], -1300)
assert co2[2] == 0.12 and nets[1] > 0 > nets[2]

# --- practice numbers ----------------------------------------------------------------------------------------
eq("capillary volume practice", sf(pi * 0.40 ** 2 * 18, 2), 9.0)
V = pi * 0.50 ** 2 * 12.0
eq("exam practice volume", sf(V, 2), 9.4)
eq("exam practice rate", sf(V / 5, 2), 1.9)
eq("rate green filter", sf(1 / 420, 2), 0.0024)
t = {"none": 60, "red": 90, "blue": 75, "green": 420}
assert t["none"] == min(t.values()) and t["green"] == max(t.values())
# temperature table
dim = [10, 12, 12, 12, 4]
bright = [14, 33, 62, 41, 5]
temps = [10, 20, 30, 40, 50]
eq("bright peak at 30", temps[bright.index(max(bright))], 30)
eq("bright peak value", max(bright), 62)
eq("bright at 10", bright[0], 14)
eq("bright at 50", bright[4], 5)
assert all(10 <= d <= 12 for d in dim[:4])
# NaHCO3 table
bub = [2, 12, 21, 29, 30, 30]
assert all(b2 >= b1 for b1, b2 in zip(bub, bub[1:]))
eq("rise to 0.06", bub[3], 29)
eq("plateau", bub[4], bub[5])
# factorial table
cond = {"A": 12, "B": 13, "C": 24, "D": 45}
eq("C is double A", cond["C"] / cond["A"], 2)
assert cond["B"] - cond["A"] == 1 and cond["D"] > cond["C"]
# compensation point
light = [0, 10, 20, 30, 40]
net = [-2.0, -1.0, 0.0, 1.0, 2.0]
eq("compensation point", light[net.index(0.0)], 20)
eq("respiration", -net[0], 2.0)
eq("gross at 40", net[4] + 2.0, 4.0)
# quiz gross rate
eq("quiz gross", 2.0 + 0.5, 2.5)
# the widget's model reproduces the plateaus at defaults (25 C): see data/test_bio-limiting.js

print("ok")
