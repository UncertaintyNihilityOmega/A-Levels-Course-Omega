# checks/chem.kinetics.py: recomputes every number in the Reaction kinetics chapter.
import json
from math import isclose, exp, sqrt, pi, erfc

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
R = 8.31

# ---- warm-up
eq("CO2 n", 0.120 / 24.0, 0.00500)

# ---- clock reaction table
times = [188, 95, 62, 47, 38]
rates = [1000 / t for t in times]
for r, want in zip(rates, [5.32, 10.5, 16.1, 21.3, 26.3]):
    eq("relative rate", sf(r, 3), want, 1e-9)
assert 1.9 < rates[1] / rates[0] < 2.1, "doubling concentration should double the relative rate"

# ---- volume-time curve V = 60(1 - exp(-t/40)): table, average rates, tangents
V = lambda t: 60 * (1 - exp(-t / 40))
for t, want in zip([0, 20, 40, 60, 80, 100], [0, 24, 38, 47, 52, 55]):
    eq(f"V({t}) rounds to table", round(V(t)), want)
vols = [0, 24, 38, 47, 52, 55]
av = [(vols[i + 1] - vols[i]) / 20 for i in range(5)]
for got, want in zip(av, [1.2, 0.70, 0.45, 0.25, 0.15]):
    eq("average rate", got, want, 1e-9)
assert all(av[i] > av[i + 1] for i in range(4))
# tangent at 40 s: V(40) = 60(1 - 1/e) = 37.93, gradient = (60/40) exp(-1) = 0.5518
eq("V(40)", sf(V(40), 4), 37.93, 1e-9)
slope40 = 1.5 * exp(-1)
eq("gradient at 40 s", sf(slope40, 4), 0.5518, 1e-9)
y0 = V(40) - slope40 * 40
y100 = V(40) + slope40 * 60
eq("tangent passes (0, 16)", y0, 16, 0.2)
eq("tangent passes (100, 71)", y100, 71, 0.2)
eq("tangent gradient read from graph", (71 - 16) / (100 - 0), 0.55)
eq("initial rate", 60 / 40, 1.5)
eq("initial / rate at 40 s", sf(1.5 / 0.55, 2), 2.7)
# the tangent line in the plot stays inside the y range up to x = 110
assert V(40) + slope40 * (110 - 40) < 80

# ---- simple rate calculations in the practice questions
eq("syringe rate", (42 - 18) / (30 - 10), 1.2)
eq("conc rate", (0.200 - 0.120) / 100, 8.0e-4, 1e-12)
eq("tangent mass rate", (0.80 - 0.20) / (70 - 10), 0.010)
eq("cross rate factor", 40 / 20, 2)

# ---- exam practice: concentration-time
c = [0.400, 0.300, 0.220, 0.160]
eq("rate first 100 s", (c[0] - c[1]) / 100, 1.00e-3, 1e-12)
eq("rate last 100 s", (c[2] - c[3]) / 100, 6.0e-4, 1e-12)

# ---- exam practice: thiosulfate
eq("1000/80", 1000 / 80, 12.5)
eq("1000/40", 1000 / 40, 25)

# ---- exam practice: calcium carbonate on a balance
Mr = A['Ca'] + A['C'] + 3 * A['O']
eq("CaCO3 Mr", Mr, 100.1)
n = 2.73 / Mr
eq("CaCO3 n", sf(n, 4), 0.02727, 1e-9)
Mr_co2 = A['C'] + 2 * A['O']
eq("CO2 Mr", Mr_co2, 44.0)
eq("CO2 mass", sf(n * Mr_co2, 3), 1.20)
eq("mass rate", 0.54 / 30, 0.018)
# the 0.54 g in 30 s matches the curve 1.20(1 - exp(-t/50))
eq("mass lost at 30 s", round(1.20 * (1 - exp(-30 / 50)), 2), 0.54)

# ---- quiz: tangent gradient
eq("quiz gradient", (65 - 5) / (50 - 0), 1.2)

# ---- Boltzmann tail areas: fraction of molecules with E >= Ea for f(E) ~ sqrt(E) exp(-E/RT)
def tail(Ea_kJ, T):
    x = Ea_kJ * 1000 / (R * T)
    return erfc(sqrt(x)) + 2 * sqrt(x / pi) * exp(-x)

eq("collision frequency rise for 300 to 310 K (about 2%)", sf((sqrt(310 / 300) - 1) * 100, 2), 1.7, 0.1)
ratio = tail(50, 310) / tail(50, 300)
eq("fraction ratio 300 to 310 K, Ea 50 (about 1.9)", sf(ratio, 2), 1.9, 1e-9)
eq("catalyst: Ea 50 to 30 at 300 K (about 2400)", sf(tail(30, 300) / tail(50, 300), 2), 2400, 1e-9)
assert 0.85 < ratio - 1 < 0.95, "about 90% increase"
# the sketch with theta = 1 and 1.5, Ea at x = 3: the shaded tail, and the curves are normalised to the same area
def tailx(x): return erfc(sqrt(x)) + 2 * sqrt(x / pi) * exp(-x)
assert tailx(2) > tailx(3), "higher temperature has the larger tail beyond the same Ea"
f1 = lambda x: 2 / sqrt(pi) * sqrt(x) * exp(-x)
f2 = lambda x: 2 / sqrt(pi) / 1.5 ** 1.5 * sqrt(x) * exp(-x / 1.5)
def area(f, a, b, n=200000):
    h = (b - a) / n
    return sum(f(a + (i + 0.5) * h) for i in range(n)) * h
eq("area under T1 curve", area(f1, 0, 40), 1.0, 1e-3)
eq("area under T2 curve", area(f2, 0, 60), 1.0, 1e-3)
assert max(f2(x / 100) for x in range(1, 700)) < max(f1(x / 100) for x in range(1, 700)), "T2 peak lower"
assert f1(6.6) < 0.01 and f2(6.6) < 0.05, "curves stop near the axis"

print("ok")
