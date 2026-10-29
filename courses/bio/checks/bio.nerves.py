# checks/bio.nerves.py: recomputes every number in the Neurones and action potentials chapter (chapters/bio.nerves.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- resting potential, threshold, peak (FACTS and COURSE.md values) -------------------------------------------------
REST, THRESH, PEAK, UNDER = -70, -50, 35, -80
eq("depolarisation needed from rest to threshold", THRESH - REST, 20)

# --- the recorded trace in the worked example is the widget's model trace (control points) -----------------------------
PTS = [(0, -70), (0.5, -70), (0.75, -50), (1.0, 35), (1.5, -20), (2.0, -75), (3.0, -80), (4.0, -72), (5.0, -70)]
table = {0: -70, 0.5: -70, 0.75: -50, 1.0: 35, 1.5: -20, 2.0: -75, 3.0: -80, 4.0: -72, 5.0: -70}
for t, v in PTS:
    eq(f"table at {t} ms", v, table[t])
eq("peak of trace", max(v for _, v in PTS), PEAK)
eq("lowest point of trace", min(v for _, v in PTS), UNDER)

# --- refractory period and maximum frequency ---------------------------------------------------------------------------
eq("2 ms -> 500 per second", 1 / 0.002, 500, 1e-6)
eq("4 ms -> 250 per second", 1 / 0.004, 250, 1e-6)
eq("2.5 ms -> 400 per second", 1 / 0.0025, 400, 1e-6)
eq("5 ms -> 200 per second", 1 / 0.005, 200, 1e-6)
eq("quiz wrong option 20 (muddled digits)", 100 / 5, 20)
# the :::plot formula min(10x, 500) reaches 500 at x = 50
eq("plot: frequency saturates at stimulus 50", 500 / 10, 50)
eq("plot: formula at 70", (10 * 70 + 500 - abs(10 * 70 - 500)) / 2, 500)
eq("plot: formula at 30", (10 * 30 + 500 - abs(10 * 30 - 500)) / 2, 300)

# --- conduction speed ----------------------------------------------------------------------------------------------------
eq("myelinated: 0.12 m in 1.5 ms", 0.12 / 0.0015, 80, 1e-9)
eq("unmyelinated: 0.012 m in 12 ms", 0.012 / 0.012, 1.0)
eq("ratio of speeds", (0.12 / 0.0015) / (0.012 / 0.012), 80)
eq("easy set: 0.45 m in 6.0 ms", 0.45 / 0.0060, 75, 1e-9)
eq("exam practice: 1.0 m in 14 ms to 2 sf", sf(1.0 / 0.014, 2), 71)

# --- potassium table (resting potential rises towards threshold) --------------------------------------------------------
kout = {5: -78, 10: -68, 15: -60, 20: -54}
eq("K table: change in resting potential 5 -> 20", kout[20] - kout[5], 24)
eq("K table: gap to threshold at 20 mmol", abs(THRESH - kout[20]), 4)
eq("K table: gap to threshold at 5 mmol", abs(THRESH - kout[5]), 28)

# --- stretch receptor table ----------------------------------------------------------------------------------------------
dep = {0.5: 4, 1.0: 12, 1.5: 20, 2.0: 28, 2.5: 36}
imp = {0.5: 0, 1.0: 0, 1.5: 25, 2.0: 60, 2.5: 95}
eq("threshold depolarisation reached at 1.5 mm", dep[1.5], THRESH - REST)
assert dep[1.0] < THRESH - REST and dep[0.5] < THRESH - REST
assert imp[1.0] == 0 and imp[1.5] > 0
eq("impulses rise from 25 to 95", imp[2.5] - imp[1.5], 70)

# --- neurone table ---------------------------------------------------------------------------------------------------------
speed = {"A": 0.8, "B": 2.5, "C": 30, "D": 90}
eq("B (no myelin) vs C (myelin) same diameter 5 um: 12-fold", speed["C"] / speed["B"], 12)

# --- stretch: oscilloscope stimulus data ------------------------------------------------------------------------------------
counts = [4, 9, 22]
freqs = [c / 0.100 for c in counts]
for f_, w in zip(freqs, [40, 90, 220]):
    eq("impulses per second", f_, w, 1e-9)
assert max(freqs) < 500          # below the 2 ms ceiling, so the neurone is not yet saturated
eq("stimulus 2 is twice stimulus 1 and 5x for stimulus 3", 2 * 1, 2)

print("ok", n)
