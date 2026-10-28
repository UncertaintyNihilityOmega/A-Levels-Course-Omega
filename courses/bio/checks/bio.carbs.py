# checks/bio.carbs.py: recomputes every number in the Carbohydrates chapter (chapters/bio.carbs.md).
from math import exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


AR = {"C": 12, "H": 1, "O": 16}


def mr(c, h, o):
    return c * AR["C"] + h * AR["H"] + o * AR["O"]


# --- Monosaccharide formulae (CH2O)n -----------------------------------------------------------------------
for name, k, (c, h, o) in [("triose", 3, (3, 6, 3)), ("pentose", 5, (5, 10, 5)), ("hexose", 6, (6, 12, 6))]:
    eq(f"{name} C = n", c, k)
    eq(f"{name} H = 2n", h, 2 * k)
    eq(f"{name} O = n", o, k)

# --- Condensation: two glucose -> maltose + water -----------------------------------------------------------
glucose, water = mr(6, 12, 6), mr(0, 2, 1)
eq("glucose Mr", glucose, 180)
eq("water Mr", water, 18)
eq("maltose formula C", 6 + 6, 12)
eq("maltose formula H", 12 + 12 - 2, 22)
eq("maltose formula O", 6 + 6 - 1, 11)
eq("maltose Mr from formula", mr(12, 22, 11), 342)
eq("maltose Mr = 2 glucose - water", 2 * glucose - water, 342)
eq("practice: Mr maltose", 2 * 180 - 18, 342)


def chain(units):
    """(bonds, waters removed, Mr) of a glucose chain of the given length."""
    bonds = units - 1
    return bonds, bonds, units * glucose - bonds * water


b, w, m = chain(20)
eq("eg: bonds in a chain of 20", b, 19)
eq("eg: water removed", w, 19)
eq("eg: glucose mass 20 x 180", 20 * 180, 3600)
eq("eg: water mass 19 x 18", 19 * 18, 342)
eq("eg: Mr of chain of 20", m, 3258)
eq("practice: 250 units, bonds", chain(250)[0], 249)
b, w, m = chain(3000)
eq("exam: 3000 units, waters", w, 2999)
eq("exam: 3000 x 180", 3000 * 180, 540000)
eq("exam: 2999 x 18", 2999 * 18, 53982)
eq("exam: Mr cellulose", m, 486018)
eq("quiz: 5 units, waters", chain(5)[1], 4)

# --- Data question: graph of glucose released (:::plot) --------------------------------------------------------
gly = lambda t: 40 * (1 - exp(-t / 4))
amp = lambda t: 40 * (1 - exp(-t / 8))
eq("graph: glycogen at 4 min about 25", round(gly(4)), 25)
eq("graph: amylopectin at 4 min about 16", round(amp(4)), 16)
assert gly(30) > 39.9 and amp(30) > 39, "both curves level off near 40"
assert gly(20) > 39.7, "glycogen levelled off by 20 min"
assert amp(20) < 37, "amylopectin still rising at 20 min"
assert all(gly(t) > amp(t) for t in range(1, 31)), "glycogen above amylopectin throughout"

# --- Table in exam practice (amylose v amylopectin) ---------------------------------------------------------
t_ = [0, 2, 4, 6, 8]
amylose = [0, 4, 7, 9, 10]
amylopectin = [0, 11, 19, 25, 29]
assert all(b > a for a, b in zip(amylose[1:], amylopectin[1:])), "amylopectin higher at every time"
eq("table: amylopectin at 8 min", amylopectin[-1], 29)
eq("table: amylose at 8 min", amylose[-1], 10)
for series in (amylose, amylopectin):
    gaps = [b - a for a, b in zip(series, series[1:])]
    assert all(g2 <= g1 for g1, g2 in zip(gaps, gaps[1:])), "rate slows over time"

# --- Stretch: starch particles ---------------------------------------------------------------------------------
eq("stretch: 1.0e6 / 2000 starch molecules", 1.0e6 / 2000, 500)
eq("stretch: 2000 times as many particles as glucose", 1.0e6 / 500, 2000)

print("ok")
