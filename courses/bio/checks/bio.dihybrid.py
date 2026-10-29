# checks/bio.dihybrid.py: recomputes every ratio, expected value and chi-squared value in the dihybrid chapter.
import os, sys
from fractions import Fraction as Fr
from collections import Counter
from itertools import product
from math import isclose

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'data'))
from crit import chi2_crit

n = 0


def eq(label, got, want, tol=0):
    global n
    n += 1
    if isinstance(want, float):
        assert isclose(float(got), want, rel_tol=0, abs_tol=tol or 1e-9), f"{label}: computed {got}, chapter says {want}"
    else:
        assert got == want, f"{label}: computed {got}, chapter says {want}"


def chi2(obs, exp):
    return sum((o - e) ** 2 / e for o, e in zip(obs, exp))


def expected(total, ratio):
    s = sum(ratio)
    return [total * r / s for r in ratio]


# --- critical values printed in the chapter -----------------------------------------------------------------------
for df, want in zip(range(1, 6), (3.84, 5.99, 7.81, 9.49, 11.07)):
    eq(f"critical df {df}", round(chi2_crit(df), 2), want)

# --- eg1 pea RrYy x RrYy: 9 genotypes (1,2,2,4,1,2,1,2,1), phenotypes 9:3:3:1 ---------------------------------------
g = [a + b for a in "Rr" for b in "Yy"]
off = Counter()
for x, y in product(g, g):
    geno = ("".join(sorted((x[0], y[0]), key=lambda c: (c.islower(), c))) +
            "".join(sorted((x[1], y[1]), key=lambda c: (c.islower(), c))))
    off[geno] += 1
eq("16 boxes", sum(off.values()), 16)
eq("9 genotypes", len(off), 9)
eq("genotype counts", sorted(off.values()), [1, 1, 1, 1, 2, 2, 2, 2, 4])
eq("RrYy count", off["RrYy"], 4)
ph = Counter()
for geno, c in off.items():
    ph[("round" if "R" in geno else "wrinkled", "yellow" if "Y" in geno else "green")] += c
eq("9:3:3:1", (ph[("round", "yellow")], ph[("round", "green")], ph[("wrinkled", "yellow")], ph[("wrinkled", "green")]), (9, 3, 3, 1))
eq("P round yellow", Fr(3, 4) * Fr(3, 4), Fr(9, 16))
eq("P round green", Fr(3, 4) * Fr(1, 4), Fr(3, 16))
eq("P wrinkled yellow", Fr(1, 4) * Fr(3, 4), Fr(3, 16))
eq("P wrinkled green", Fr(1, 4) * Fr(1, 4), Fr(1, 16))

# --- eg2 test cross counts ----------------------------------------------------------------------------------------
eq("eg2 total", 24 + 26 + 25 + 25, 100)

# --- eg3 fruit fly, Ll XR Xr x Ll XR Y -----------------------------------------------------------------------------
fem = [(w, x) for w in "Ll" for x in ("R", "r")]
mal = [(w, x) for w in "Ll" for x in ("R", "Y")]
res = Counter()
for (w1, x1), (w2, x2) in product(fem, mal):
    sex = "m" if x2 == "Y" else "f"
    wing = "long" if "L" in (w1, w2) else "vestigial"
    eye = "red" if (x1 == "R" or x2 == "R") else "white"
    res[(sex, wing, eye)] += 1
eq("fly f long red", res[("f", "long", "red")], 6)
eq("fly f vestigial red", res[("f", "vestigial", "red")], 2)
eq("fly f white", sum(v for k, v in res.items() if k[0] == "f" and k[2] == "white"), 0)
eq("fly m long red", res[("m", "long", "red")], 3)
eq("fly m long white", res[("m", "long", "white")], 3)
eq("fly m vestigial red", res[("m", "vestigial", "red")], 1)
eq("fly m vestigial white", res[("m", "vestigial", "white")], 1)
eq("3/8 long red females", Fr(3, 4) * Fr(1, 2), Fr(3, 8))
eq("1/8 vestigial red females", Fr(1, 4) * Fr(1, 2), Fr(1, 8))
eq("3/16 male long red", Fr(3, 4) * Fr(1, 2) * Fr(1, 2), Fr(3, 16))
eq("1/16 male vestigial", Fr(1, 4) * Fr(1, 2) * Fr(1, 2), Fr(1, 16))

# --- linkage example: 84, 78, 22, 16 of 200 --------------------------------------------------------------------------
eq("link total", 84 + 78 + 22 + 16, 200)
eq("link expected each", 200 / 4, 50)
eq("link recombinants", 22 + 16, 38)
eq("link recombinant %", 38 / 200 * 100, 19.0)
x2 = chi2([84, 78, 22, 16], [50] * 4)
for o, w in zip((84, 78, 22, 16), (23.12, 15.68, 15.68, 23.12)):
    eq("link term", round((o - 50) ** 2 / 50, 2), w)
eq("link squares", [(o - 50) ** 2 for o in (84, 78, 22, 16)], [1156, 784, 784, 1156])
eq("link chi2", x2, 77.6, 1e-9)
assert x2 > chi2_crit(3)

# --- epistasis Labrador: B_E_ 9, bbE_ 3, ee 4 ---------------------------------------------------------------------
lab = Counter()
for (b1, e1), (b2, e2) in product(list(product("Bb", "Ee")), repeat=2):
    ee = e1 == "e" and e2 == "e"
    black = ("B" in (b1, b2))
    lab["yellow" if ee else ("black" if black else "chocolate")] += 1
eq("lab", (lab["black"], lab["chocolate"], lab["yellow"]), (9, 3, 4))
eq("P ee", Fr(1, 4), Fr(4, 16))
eq("P black", Fr(3, 4) * Fr(3, 4), Fr(9, 16))
eq("P chocolate", Fr(1, 4) * Fr(3, 4), Fr(3, 16))

# --- chi-squared tomato example: 275, 98, 79, 28 of 480 vs 9:3:3:1 ---------------------------------------------------------
obs = [275, 98, 79, 28]
exp_ = expected(480, [9, 3, 3, 1])
eq("tomato total", sum(obs), 480)
eq("tomato expected", exp_, [270.0, 90.0, 90.0, 30.0])
terms = [(o - e) ** 2 / e for o, e in zip(obs, exp_)]
eq("tomato O-E", [o - e for o, e in zip(obs, exp_)], [5, 8, -11, -2])
eq("tomato squares", [(o - e) ** 2 for o, e in zip(obs, exp_)], [25, 64, 121, 4])
for t, w in zip(terms, (0.093, 0.711, 1.344, 0.133)):
    eq("tomato term", round(t, 3), w)
eq("tomato chi2", sum(terms), 2.28, 0.005)
eq("tomato rounded", round(sum(terms), 2), 2.28)
assert sum(terms) < chi2_crit(3)

# --- Spot the error: maize 170, 80, 50, 20 of 320 --------------------------------------------------------------------------
obs = [170, 80, 50, 20]
exp_ = expected(320, [9, 3, 3, 1])
eq("spot expected", exp_, [180.0, 60.0, 60.0, 20.0])
terms = [(o - e) ** 2 / e for o, e in zip(obs, exp_)]
for t, w in zip(terms, (0.556, 6.667, 1.667, 0.0)):
    eq("spot term", round(t, 3), w)
eq("spot chi2", sum(terms), 8.89, 0.005)
assert sum(terms) > chi2_crit(3) and sum(terms) < chi2_crit(4)

# --- practice -------------------------------------------------------------------------------------------------------------------
eq("try expected 160", expected(160, [9, 3, 3, 1]), [90.0, 30.0, 30.0, 10.0])
eq("try 3:1 expected", expected(200, [3, 1]), [150.0, 50.0])
t = chi2([148, 52], [150, 50])
eq("try 3:1 chi2", round(t, 2), 0.11)
eq("try 3:1 terms", (round(4 / 150, 3), round(4 / 50, 3)), (0.027, 0.08))
assert t < chi2_crit(1)
eq("try product aabb", Fr(1, 4) * Fr(1, 4), Fr(1, 16))
eq("try genotypes AaBb x AaBb", len(set(product(["AA", "Aa", "aa"], ["BB", "Bb", "bb"]))), 9)
# E2: white petals long stamens among 800
eq("E2 white long of 800", Fr(3, 16) * 800, 150)
eq("E2 white short", Fr(1, 4) * Fr(1, 4), Fr(1, 16))
# E3: ABO x colour blindness
eq("E3 group O", Fr(1, 2), Fr(1, 2))
eq("E3 colour-blind boy", Fr(1, 4), Fr(1, 4))
eq("E3 both", Fr(1, 2) * Fr(1, 4), Fr(1, 8))
eq("E3 gametes", len(list(product(["A", "o"], ["XB", "Xb"]))), 4)
# E4: linkage table
eq("E4 total", 403 + 389 + 98 + 110, 1000)
eq("E4 recombinants %", (98 + 110) / 1000 * 100, 20.8)
# E5: moth
obs = [188, 57, 52, 23]
exp_ = expected(320, [9, 3, 3, 1])
eq("E5 total", sum(obs), 320)
eq("E5 expected", exp_, [180.0, 60.0, 60.0, 20.0])
terms = [(o - e) ** 2 / e for o, e in zip(obs, exp_)]
for t_, w in zip(terms, (0.356, 0.150, 1.067, 0.450)):
    eq("E5 term", round(t_, 3), w)
eq("E5 chi2", round(sum(terms), 2), 2.02)
assert sum(terms) < chi2_crit(3)
# E6: mouse 90, 28, 42
eq("E6 total", 90 + 28 + 42, 160)
eq("E6 expected 9:3:4", expected(160, [9, 3, 4]), [90.0, 30.0, 40.0])
mouse = Counter()
for (a1, c1), (a2, c2) in product(list(product("Aa", "Cc")), repeat=2):
    cc = c1 == "c" and c2 == "c"
    mouse["albino" if cc else ("agouti" if "A" in (a1, a2) else "black")] += 1
eq("E6 mouse 9:3:4", (mouse["agouti"], mouse["black"], mouse["albino"]), (9, 3, 4))
# E7: beetle 66, 58, 61, 55
obs = [66, 58, 61, 55]
eq("E7 total", sum(obs), 240)
eq("E7 squares sum", sum((o - 60) ** 2 for o in obs), 66)
eq("E7 chi2", sum((o - 60) ** 2 for o in obs) / 60, 1.1, 1e-9)
assert chi2(obs, [60] * 4) < chi2_crit(3)
# Stretch 1: sweet pea 9 purple : 7 white
sp = Counter()
for (c1, p1), (c2, p2) in product(list(product("Cc", "Pp")), repeat=2):
    purple = ("C" in (c1, c2)) and ("P" in (p1, p2))
    sp["purple" if purple else "white"] += 1
eq("sweet pea 9:7", (sp["purple"], sp["white"]), (9, 7))
# Stretch 2: linkage arrangement
eq("S2 total", 12 + 10 + 88 + 90, 200)
eq("S2 recombinant %", (12 + 10) / 200 * 100, 11.0)
# quiz
eq("quiz expected 240/4", 240 / 4, 60.0)
eq("quiz df 5 classes", 5 - 1, 4)
assert 6.2 < chi2_crit(3)

print(f"ok ({n} checks)")
