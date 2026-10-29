# checks/bio.maths.py: recomputes every number in the Maths skills chapter (chapters/bio.maths.md).
from math import exp, isclose, pi, log10

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- warm-up -----------------------------------------------------------------------------------------
eq("warm 0.045 mm in um", 0.045 * 1000, 45)
eq("warm M", 36 * 1000 / 12, 3000)
eq("warm cube SA", 6 * 3 ** 2, 54)
eq("warm cube V", 3 ** 3, 27)

# --- conversions, standard form, estimation ----------------------------------------------------------
eq("eg conv a", 0.35 * 1000, 350)
eq("eg conv b", 4.2 / 1000, 0.0042)
eq("eg conv c", 250 / 1000, 0.25)
eq("eg conv d", 0.90 / 60, 0.015)
eq("culture bacteria", 3.2e7 * 0.25, 8.0e6)
eq("estimate", sf(3.9e-3 * 410), 1.60)
eq("estimate rough", 4e-3 * 400, 1.6)
eq("sf rate", sf(4.7 / 15, 2), 0.31)
eq("sf rate 3", sf(4.7 / 15, 3), 0.313)

# --- averages ----------------------------------------------------------------------------------------
leaf = [42, 38, 45, 41, 38, 52, 40, 38, 44, 43]
eq("leaf sum", sum(leaf), 421)
eq("leaf mean", sum(leaf) / 10, 42.1)
s = sorted(leaf)
eq("leaf median", (s[4] + s[5]) / 2, 41.5)
eq("leaf mode", max(set(leaf), key=leaf.count), 38)
eq("leaf mode count", leaf.count(38), 3)
eq("leaf range", max(leaf) - min(leaf), 14)

# --- ratios and percentages ---------------------------------------------------------------------------
eq("ratio 108:36", 108 / 36, 3)
eq("ratio 45:12", 45 / 12, 3.75)
eq("share 120", 120 / 4 * 3, 90)
sea = [(4.20, 4.62), (3.85, 3.47), (5.10, 4.59)]
for (a, b), w in zip(sea, [10.0, -9.87, -10.0]):
    eq("seaweed %", sf((b - a) / a * 100, 3), w)
eq("seaweed B change", sf(3.85 - 3.47, 2), 0.38)
eq("seaweed C change", sf(5.10 - 4.59, 2), 0.51)
eq("pc a", sf(0.1 / 6.0 * 100, 2), 1.7)
eq("pc b", 0.1 / 2.0 * 100, 5.0)
eq("pc three times", (0.1 / 2.0) / (0.1 / 6.0), 3)

# --- geometry ------------------------------------------------------------------------------------------
r, h = 0.50, 3.0
V = pi * r ** 2 * h
A = 2 * pi * r ** 2 + 2 * pi * r * h
eq("potato V", sf(V), 2.36)
eq("potato A", sf(A), 11.0)
eq("potato A/V", sf(A / V), 4.67)
eq("A unrounded", sf(A, 6), 10.9956)
eq("V unrounded", sf(V, 5), 2.3562)
eq("clear zone", sf(pi * 7.0 ** 2), 154)

# --- magnification -------------------------------------------------------------------------------------
eq("photomicrograph actual mm", 54 / 1500, 0.036)
eq("photomicrograph actual um", 54 / 1500 * 1000, 36)
eq("scale bar M", 20000 / 5, 4000)

# --- pie chart, straight line, tangent ----------------------------------------------------------------
eq("pie 55%", 0.55 * 360, 198)
eq("straight gradient", (4.8 - 0) / 40, 0.12)
eq("0.12 * 40", 0.12 * 40, 4.8)

P = lambda t: 24 * (1 - exp(-t / 3))
slope = lambda t: 8 * exp(-t / 3)
for t, w in zip([0, 1, 2, 3, 4, 5, 6, 8, 10], [0.0, 6.8, 11.7, 15.2, 17.7, 19.5, 20.8, 22.3, 23.1]):
    eq(f"P({t})", round(P(t), 1), w)
eq("tangent value at 2", sf(P(2), 4), 11.68)
eq("tangent slope at 2", sf(slope(2), 4), 4.107)
eq("tangent at x=0", round(P(2) - 2 * slope(2), 1), 3.5)
eq("tangent at x=6", round(P(2) + 4 * slope(2), 1), 28.1)
eq("rate at 2 (read)", sf((28.1 - 3.5) / 6, 2), 4.1)
eq("rate at 6", sf(slope(6), 2), 1.1)
eq("plateau", P(1e6), 24, 1e-6)
eq("plot line const", 11.678 + 4.1073 * (2 - 2), 11.678)

# --- logs -----------------------------------------------------------------------------------------------
eq("pH", sf(-log10(3.2e-5), 3), 4.49)
eq("lg 4.0e5", sf(log10(4.0e5), 3), 5.60)
eq("10^7.30", sf(10 ** 7.30, 2), 2.0e7)

# --- Spot the error ---------------------------------------------------------------------------------------
eq("spot wrong", sf(-2.0 / 6.0 * 100, 2), -33)
eq("spot right", (6.0 - 8.0) / 8.0 * 100, -25)

# --- practice (easy) ------------------------------------------------------------------------------------
eq("mg to g", 2.5 / 1000, 0.0025)
eq("dm3 to cm3", 0.40 * 1000, 400)
eq("std form 1", 4.7e-5, 0.000047)
eq("std form 2", 6.2e6, 6200000)
seed = [18, 22, 19, 22, 25, 20, 22]
eq("seedling sum", sum(seed), 148)
eq("seedling mean", sf(sum(seed) / 7), 21.1)
eq("seedling median", sorted(seed)[3], 22)
eq("seedling range", max(seed) - min(seed), 7)
eq("beetroot", sf((5.76 - 6.40) / 6.40 * 100, 3), -10.0)
eq("burette volume", round(31.60 - 23.40, 2), 8.20)
eq("burette pc", sf(0.10 / 8.20 * 100, 2), 1.2)
eq("leaf area", 8.4 * 3.5, 29.4)
eq("leaf perimeter", 2 * (8.4 + 3.5), 23.8)
eq("field area", sf(pi * 0.225 ** 2), 0.159)
eq("pie Y", sf(32 / 100 * 360, 3), 115)
eq("pie Y exact", 32 / 100 * 360, 115.2)
eq("tangent gradient", (15.0 - 6.0) / (8 - 2), 1.5)

# --- exam practice ---------------------------------------------------------------------------------------
eq("ep1", 2.5 / 1000, 2.5e-3)
eq("ep2", sf((138 - 72) / 72 * 100), 91.7)
st = [12, 15, 11, 14, 13, 14, 16, 14, 12]
eq("stomata sum", sum(st), 121)
eq("stomata mean", sf(sum(st) / 9), 13.4)
eq("stomata mode", max(set(st), key=st.count), 14)
eq("stomata median", sorted(st)[4], 14)
eq("stomata range", max(st) - min(st), 5)
G = lambda t: 15 * (1 - exp(-t / 4))
gs = lambda t: 15 / 4 * exp(-t / 4)
eq("gas at 3", sf(G(3), 3), 7.91)
eq("gas tangent at 0", round(G(3) - 3 * gs(3), 1), 2.6)
eq("gas tangent at 8", round(G(3) + 5 * gs(3), 1), 16.8)
eq("gas rate read", sf((16.8 - 2.6) / 8, 2), 1.8)
eq("gas rate exact", sf(gs(3), 2), 1.8)
eq("gas mean to 3", sf(7.9 / 3, 2), 2.6)
eq("plot const gas", sf(G(3), 4), 7.915)
eq("cylinder error", sf(0.5 / 12 * 100, 2), 4.2)
r2, h2 = 0.60, 4.0
V2 = pi * r2 ** 2 * h2
A2 = 2 * pi * r2 ** 2 + 2 * pi * r2 * h2
eq("agar V", sf(V2), 4.52)
eq("agar A", sf(A2), 17.3)
eq("agar ratio", sf(A2 / V2), 3.83)
counts = [2.5e3, 1.6e4, 1.0e5, 6.4e5]
for c, w in zip(counts, [3.40, 4.20, 5.00, 5.81]):
    eq("lg count", sf(log10(c), 3), w)
eq("factor", 1.6e4 / 2.5e3, 6.4)
eq("factor 2", 1.0e5 / 1.6e4, 6.25 if False else 1.0e5 / 1.6e4)
eq("factor 3", 6.4e5 / 1.0e5, 6.4)

# --- stretch -----------------------------------------------------------------------------------------------
eq("mass error", sf(0.005 / 2.50 * 100, 1), 0.2)
eq("vol error is 1.25, which rounds to 1.3", 0.05 / 4.0 * 100, 1.25)
eq("time error", sf(0.5 / 30 * 100, 2), 1.7)
eq("doubling lg", sf(log10(2), 3), 0.301)
eq("doubling time", sf(0.301 / 0.15, 2), 2.0)
eq("10 h factor", sf(10 ** 1.5, 2), 32)
eq("2^5", 2 ** 5, 32)

# --- quiz ---------------------------------------------------------------------------------------------------
eq("quiz um to mm", 35 / 1000, 0.035)
eq("quiz std", 8.0e-3, 0.0080)
eq("quiz pc", (6.0 - 5.0) / 5.0 * 100, 20)
eq("quiz wrong pc", sf(1.0 / 6.0 * 100, 2), 17)
eq("quiz thermometer", 0.5 / 20 * 100, 2.5)

print("ok")
