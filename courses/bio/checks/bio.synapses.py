# checks/bio.synapses.py: recomputes every number in the Synapses and muscle contraction chapter (chapters/bio.synapses.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- model filament lengths (also in widgets/bio-sarcomere.js): thin 1.0 um from each Z line, thick 1.6 um centred on the M line
THIN, THICK = 1.0, 1.6


def bands(L):
    return {"A": THICK, "I": L - THICK, "H": max(0.0, L - 2 * THIN), "overlap": 2 * max(0.0, min(THIN, L / 2 + THICK / 2) - max(0.0, L / 2 - THICK / 2))}


# --- worked example: electron micrograph at x20 000 (relaxed 50 mm, A 32 mm, H 10 mm; contracted 40 mm, A 32 mm, H 0) ------
MAG = 20000
um = lambda mm, mag: mm / mag * 1000            # image mm -> actual um
eq("relaxed sarcomere 50 mm at x20000 = 2.5 um", um(50, MAG), 2.5, 1e-9)
eq("A band 32 mm = 1.6 um", um(32, MAG), 1.6, 1e-9)
eq("contracted sarcomere 40 mm = 2.0 um", um(40, MAG), 2.0, 1e-9)
eq("H zone relaxed 10 mm = 0.5 um", um(10, MAG), 0.5, 1e-9)
b = bands(2.5)
eq("model I band at 2.5 um = 0.9 um = 18 mm", b["I"] * MAG / 1000, 18, 1e-9)
eq("model H zone at 2.5 um = 10 mm", b["H"] * MAG / 1000, 10, 1e-9)
eq("model A band 32 mm", b["A"] * MAG / 1000, 32, 1e-9)
b = bands(2.0)
eq("model I band at 2.0 um = 8 mm", b["I"] * MAG / 1000, 8, 1e-9)
eq("model H zone at 2.0 um = 0", b["H"], 0)
eq("I band by subtraction, relaxed", 50 - 32, 18)
eq("I band by subtraction, contracted", 40 - 32, 8)
eq("percentage decrease in length", (50 - 40) / 50 * 100, 20)

# --- easy set and exam practice -------------------------------------------------------------------------------------------
eq("2.6 -> 2.1 um percentage decrease", sf((2.6 - 2.1) / 2.6 * 100, 3), 19.2)
eq("x30000: 66 mm -> 2.2 um", um(66, 30000), 2.2, 1e-9)
eq("x30000: 48 mm -> 1.6 um", um(48, 30000), 1.6, 1e-9)
eq("I band = 2.2 - 1.6", 2.2 - 1.6, 0.6, 1e-9)
eq("quiz: 65 mm at x25000", um(65, 25000), 2.6, 1e-9)
eq("quiz wrong option: multiplied by the magnification", 65 * 25000 / 1000, 1625)
eq("H zone vanishes at 2.0 um (model)", bands(2.0)["H"], 0)
# table of three sarcomeres: A band 1.6 constant, H zone = L - 2.0 (model), I band at 2.4
for L, A, H in ((3.0, 1.6, 1.0), (2.4, 1.6, 0.4), (2.2, 1.6, 0.2)):
    eq(f"table A band at {L}", bands(L)["A"], A)
    eq(f"table H zone at {L}", bands(L)["H"], H, 1e-9)
eq("I band at 2.4 um", 2.4 - 1.6, 0.8, 1e-9)

# --- calcium table: depolarisation values only compared ----------------------------------------------------------------------
ca = {0.0: 0, 0.5: 3, 1.0: 7, 2.0: 12, 4.0: 14}
assert all(ca[a] < ca[b2] for a, b2 in zip(sorted(ca), sorted(ca)[1:]))
eq("increase 2.0 -> 4.0 is small (2 mV)", ca[4.0] - ca[2.0], 2)
assert ca[4.0] - ca[2.0] < ca[2.0] - ca[1.0]

# --- receptor blocker table: threshold needs 20 mV (-70 -> -50) ------------------------------------------------------------------
dep = {0: 25, 1: 21, 2: 16, 4: 9, 8: 4}
need = -50 - (-70)
eq("depolarisation needed", need, 20)
responds = [c for c, d in dep.items() if d >= need]
assert responds == [0, 1], responds
assert all(dep[a] > dep[b2] for a, b2 in zip(sorted(dep), sorted(dep)[1:]))

# --- synaptic cleft size (course value): about 20 nm = 0.02 um ----------------------------------------------------------------
eq("20 nm in um", 20 / 1000, 0.02)
print("ok", n)
