# checks/bio.evolution.py: recomputes every number in the Evolution and speciation chapter.
from math import isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def diffs(a, b):
    assert len(a) == len(b)
    return sum(1 for x, y in zip(a, b) if x != y)


# --- sequence comparison example (10 bases) ---------------------------------------------------------
s1, s2 = "ATGCCATTGA", "ATGCTATTCA"
eq("eg seq differences", diffs(s1, s2), 2)
eq("eg seq percent", diffs(s1, s2) / len(s1) * 100, 20)

# --- beetle tree ----------------------------------------------------------------------------------------
M = {("W", "X"): 6, ("Y", "Z"): 14, ("W", "Y"): 30, ("W", "Z"): 30, ("X", "Y"): 30, ("X", "Z"): 30}
eq("tree WX", M[("W", "X")], 6)
eq("tree WX half", M[("W", "X")] / 2, 3)
eq("tree YZ half", M[("Y", "Z")] / 2, 7)
eq("tree root half", M[("W", "Y")] / 2, 15)
eq("tree ratio 6/14", round(6 / 14, 2), 0.43)
eq("tree percentages of 100 bases", 14 / 100 * 100, 14)
# the matrix is ultrametric: every cross-pair is 30, so the tree is consistent
eq("tree cross pairs equal", len({M[k] for k in M if k not in (("W", "X"), ("Y", "Z"))}), 1)

# --- molecular clock (voles) --------------------------------------------------------------------------------
rate = 36 / 9
eq("clock rate", rate, 4)
eq("clock A and C time", 20 / rate, 5)
eq("clock plot point A,B", rate * 9, 36)
eq("clock plot point A,C", rate * 5, 20)

# --- practice: lizards -----------------------------------------------------------------------------------------
l1, l2, l3 = "GATTACCGTAAC", "GATTGCCGTAAC", "GCTTGCCGTCAC"
eq("lizards L1 L2", diffs(l1, l2), 1)
eq("lizards L2 L3", diffs(l2, l3), 2)
eq("lizards L1 L3", diffs(l1, l3), 3)
eq("lizards L1 L2 position", [i + 1 for i in range(12) if l1[i] != l2[i]][0], 5)
eq("lizards L2 L3 positions", sum([i + 1 for i in range(12) if l2[i] != l3[i]]), 2 + 10)
# --- practice: frogs
eq("frogs percent", 30 / 1200 * 100, 2.5)
eq("frogs time", 30 / 5, 6)

# --- exam practice -----------------------------------------------------------------------------------------------
eq("geckos percent", 22 / 200 * 100, 11)
# amino acid table is consistent: M,N pair 2; P,Q pair 4; cross 8; R 14
T = {"MN": 2, "PQ": 4, "MP": 8, "MQ": 8, "NP": 8, "NQ": 8, "MR": 14, "NR": 14, "PR": 14, "QR": 14}
eq("aa table R is the most different", min(T[k] for k in T if "R" in k), 14)
eq("aa table cross pairs", len({T[k] for k in ("MP", "MQ", "NP", "NQ")}), 1)
# fruit flies
m = [[38, 12], [10, 41]]
tot = sum(map(sum, m))
same = m[0][0] + m[1][1]
eq("flies total", tot, 101)
eq("flies same-cage", same, 79)
eq("flies same-cage percent", round(same / tot * 100), 78)
eq("flies different-cage", tot - same, 22)
eq("flies different-cage percent", round((tot - same) / tot * 100), 22)
# polyploid plant
eq("hybrid chromosomes", 14 / 2 + 18 / 2, 16)
eq("doubled hybrid", 16 * 2, 32)
# fish E, F, G
r = 45 / 5
eq("fish rate", r, 9)
eq("fish time E and G", 90 / r, 10)
# saturation table
t = [2, 4, 8, 16, 32]
d = [4, 8, 15, 25, 33]
eq("saturation early rate", d[0] / t[0], 2)
eq("saturation early rate 4", d[1] / t[1], 2)
eq("saturation late rate", (d[4] - d[3]) / (t[4] - t[3]), 0.5)
print("ok", n)
