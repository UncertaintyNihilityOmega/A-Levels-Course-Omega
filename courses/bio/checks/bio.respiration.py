# checks/bio.respiration.py: recomputes every number in the Aerobic respiration chapter (chapters/bio.respiration.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=2):
    return float(f"{x:.{k}g}")


# --- per-glucose tally ---------------------------------------------------------------------------------------
GLY = dict(co2=0, nadh=2, fadh=0, atp=4 - 2)           # glycolysis: 4 made, 2 used
LINK = dict(co2=1, nadh=1, fadh=0, atp=0)              # per pyruvate
KREBS = dict(co2=2, nadh=3, fadh=1, atp=1)             # per turn
pyr = 2                                                # pyruvate per glucose = acetyl CoA = turns of the cycle
tot = {k: GLY[k] + pyr * LINK[k] + pyr * KREBS[k] for k in GLY}
eq("CO2 total", tot["co2"], 6)
eq("reduced NAD total", tot["nadh"], 10)
eq("reduced FAD total", tot["fadh"], 2)
eq("ATP made directly total", tot["atp"], 4)
eq("link CO2 per glucose", pyr * LINK["co2"], 2)
eq("link reduced NAD per glucose", pyr * LINK["nadh"], 2)
eq("Krebs CO2 per glucose", pyr * KREBS["co2"], 4)
eq("Krebs reduced NAD per glucose", pyr * KREBS["nadh"], 6)
eq("Krebs reduced FAD per glucose", pyr * KREBS["fadh"], 2)
eq("Krebs ATP per glucose", pyr * KREBS["atp"], 2)
eq("carbon atoms accounted for by CO2", tot["co2"], 6)
# carbon numbers in the cycle: 4C + 2C -> 6C -> 5C (CO2) -> 4C (CO2)
eq("citrate carbons", 4 + 2, 6)
eq("after two decarboxylations", 6 - 1 - 1, 4)
eq("pyruvate carbons after link", 3 - 1, 2)

# --- magnification ---------------------------------------------------------------------------------------------
A_mm = 62 / 20000
eq("eg actual length mm", A_mm, 0.0031, 1e-12)
eq("eg actual length µm", A_mm * 1000, 3.1, 1e-9)
M = 18 / 0.002
eq("scale bar magnification", M, 9000)
L = 33 / M
eq("practice length mm", sf(L, 3), 0.00367)
eq("practice length µm", sf(L * 1000, 2), 3.7)

eq("practice magnification", 63 / (4.2 / 1000), 15000, 1e-6)

# --- poison data ---------------------------------------------------------------------------------------------------
eq("ATP decrease %", (10.0 - 1.5) / 10.0 * 100, 85)
eq("O2 increase %", (5.0 - 4.0) / 4.0 * 100, 25)

# --- isolated mitochondria with ADP --------------------------------------------------------------------------
t = [0, 60, 120, 150, 180, 210, 240, 300]
o2 = [250, 247, 244, 214, 184, 154, 152, 149]
d = dict(zip(t, o2))
eq("rate before ADP", (d[0] - d[120]) / 120, 0.050, 1e-9)
eq("rate 0-60 equals rate 60-120", (d[0] - d[60]) / 60, (d[60] - d[120]) / 60)
eq("rate with ADP 120-210", (d[120] - d[210]) / 90, 1.0)
eq("rate 120-150", (d[120] - d[150]) / 30, 1.0)
eq("rate 150-180", (d[150] - d[180]) / 30, 1.0)
eq("rate 180-210", (d[180] - d[210]) / 30, 1.0)
eq("rate after 210 s (slow)", sf((d[210] - d[300]) / 90, 2), 0.056)
assert (d[210] - d[300]) / 90 < 0.1

print("ok")
