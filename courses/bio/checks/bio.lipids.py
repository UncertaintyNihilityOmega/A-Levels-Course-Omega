# checks/bio.lipids.py: recomputes every number in the Lipids and water chapter (chapters/bio.lipids.md).
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


AR = {"C": 12, "H": 1, "O": 16}


def mr(c, h, o):
    return c * AR["C"] + h * AR["H"] + o * AR["O"]


# --- Heating experiment (:::plot): oil 20 + 6x, water 20 + 3x -----------------------------------------------
oil = lambda t: 20 + 6 * t
wat = lambda t: 20 + 3 * t
eq("plot: oil at 5 min", oil(5), 50)
eq("plot: water at 5 min", wat(5), 35)
eq("oil rises twice as fast", 6 / 3, 2)
eq("alt: oil at 8 min", oil(8), 68)
eq("alt: water at 8 min", wat(8), 44)

# --- Sweat: runner (eg) and practice ----------------------------------------------------------------------------
eq("eg: 0.50 dm3 -> 500 g", 0.50 * 1000 * 1.0, 500)
eq("eg: energy 500 g x 2.4 kJ/g", 500 * 2.4, 1200)
eq("try: 0.20 dm3 -> 200 g", 0.20 * 1000, 200)
eq("try: 200 x 2.4", 200 * 2.4, 480)
eq("exam: leaf 12 x 2.4", 12 * 2.4, 28.8, 1e-9)

# --- Tripalmitin ------------------------------------------------------------------------------------------------
glycerol, palmitic = (3, 8, 3), (16, 32, 2)
C = glycerol[0] + 3 * palmitic[0]
H = glycerol[1] + 3 * palmitic[1]
O = glycerol[2] + 3 * palmitic[2]
eq("tripalmitin C before", C, 51)
eq("tripalmitin H before", H, 104)
eq("tripalmitin O before", O, 9)
eq("tripalmitin H after 3 H2O", H - 6, 98)
eq("tripalmitin O after 3 H2O", O - 3, 6)
eq("tripalmitin Mr", mr(51, 98, 6), 806)
eq("sum: 51 x 12", 51 * 12, 612)
eq("Mr glycerol", mr(*glycerol), 92)
eq("Mr palmitic acid", mr(*palmitic), 256)
eq("Mr by other route", 92 + 3 * 256 - 3 * 18, 806)

# --- Energy values -------------------------------------------------------------------------------------------------
LIP, CARB = 39, 16
eq("eg sleep: mass of fat 2000/39", round(2000 / LIP), 51)
eq("eg sleep: mass of carbohydrate 2000/16", 2000 / CARB, 125)
eq("eg sleep: about 2.4 times the mass", round(125 / (2000 / LIP), 1), 2.4)
assert LIP / CARB > 2, "lipid gives more than twice the energy per gram"
eq("try: 25 g fat", 25 * LIP, 975)
eq("try: carbohydrate for 975 kJ", round(975 / CARB), 61)
eq("exam stretch: fat 780/39", 780 / LIP, 20)
eq("exam stretch: carbohydrate 780/16", 780 / CARB, 48.75)

# --- Hibernation table ---------------------------------------------------------------------------------------
lost = 60.0 - 38.4
eq("bear: fat lost over 120 days", lost, 21.6, 1e-9)
eq("bear: g per day", lost * 1000 / 120, 180, 1e-9)
eq("bear: kJ per day", 180 * 39, 7020)

# --- Melting points (real values, rounded) ---------------------------------------------------------------------
mp = {0: 69, 1: 13, 2: -5}
vals = [mp[k] for k in sorted(mp)]
assert vals == sorted(vals, reverse=True), "melting point falls as C=C bonds increase"

print("ok")
