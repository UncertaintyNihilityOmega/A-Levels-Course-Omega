# checks/math.s1.prob.py: recomputes every number in the Probability chapter.
from fractions import Fraction as Fr
from itertools import product, combinations
from math import comb, isclose

def eq(label, got, want, tol=1e-9): assert abs(float(got) - float(want)) <= tol, f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{float(x):.{n}g}")

# dice
S = list(product(range(1, 7), repeat=2)); eq("36", len(S), 36)
eq("a", Fr(sum(1 for a, b in S if a + b == 7), 36), Fr(1, 6)); eq("b", Fr(sum(1 for a, b in S if a + b >= 10), 36), Fr(1, 6))
eq("c", Fr(sum(1 for a, b in S if 6 in (a, b)), 36), Fr(11, 36)); eq("c2", 1 - Fr(25, 36), Fr(11, 36))
# venn
eq("T only", 25 - 8, 17); eq("C only", 18 - 8, 10); eq("either", 17 + 8 + 10, 35); eq("neither", 40 - 35, 5)
eq("union", Fr(35, 40), Fr(7, 8)); eq("T|C", Fr(8, 18), Fr(4, 9)); eq("PT", 25 / 40, 0.625); eq("PC", 18 / 40, 0.45); eq("prod", 0.625 * 0.45, 0.28125); eq("both", 8 / 40, 0.2)
# independent / exclusive
eq("ind", 0.4 + 0.5 - 0.4 * 0.5, 0.7); eq("excl", 0.4 + 0.5, 0.9)
eq("3 coins", 1 - Fr(1, 2) ** 3, Fr(7, 8)); eq("third throw", Fr(5, 6) ** 2 * Fr(1, 6), Fr(25, 216)); eq("0.116", sf(Fr(25, 216)), 0.116)
# tree: bag
eq("RR", Fr(5, 8) * Fr(4, 7), Fr(5, 14)); eq("20/56", Fr(20, 56), Fr(5, 14)); eq("RB", Fr(5, 8) * Fr(3, 7) + Fr(3, 8) * Fr(5, 7), Fr(15, 28)); eq("30/56", Fr(30, 56), Fr(15, 28))
eq("BB", Fr(3, 8) * Fr(2, 7), Fr(3, 28)); eq("sum", Fr(10, 28) + Fr(15, 28) + Fr(3, 28), 1)
# factory
eq("A&D", 0.6 * 0.03, 0.018); eq("B&D", 0.4 * 0.05, 0.020); eq("PD", 0.018 + 0.020, 0.038); eq("A&G", 0.6 * 0.97, 0.582); eq("B&G", 0.4 * 0.95, 0.380)
eq("sum", 0.018 + 0.582 + 0.020 + 0.380, 1); eq("B|D", sf(0.020 / 0.038), 0.526)
# rain
eq("RL", 0.3 * 0.4, 0.12); eq("R'L", 0.7 * 0.1, 0.07); eq("L", 0.19, 0.12 + 0.07); eq("R|L", sf(0.12 / 0.19), 0.632)
# committee
eq("9C4", comb(9, 4), 126); eq("2w", Fr(comb(4, 2) * comb(5, 2), 126), Fr(10, 21)); eq("0.476", sf(Fr(10, 21)), 0.476)
eq("no w", comb(5, 4), 5); eq("1-", 1 - Fr(5, 126), Fr(121, 126)); eq("0.960", sf(Fr(121, 126)), 0.960)
# try
eq("T1", Fr(sum(1 for a, b in S if a * b == 12), 36), Fr(1, 9))
eq("T2 u", 0.5 + 0.3 - 0.1, 0.7); eq("T2 c", 0.1 / 0.3, 1 / 3); eq("T2 prod", 0.5 * 0.3, 0.15)
b = 0.2 / 0.4; eq("T3", b, 0.5); eq("T3 check", 0.6 + b - 0.6 * b, 0.8)
eq("T4 GG", Fr(6, 10) * Fr(5, 9), Fr(1, 3)); eq("T4 diff", Fr(4, 10) * Fr(6, 9) + Fr(6, 10) * Fr(4, 9), Fr(8, 15)); eq("48/90", Fr(48, 90), Fr(8, 15))
eq("T5", Fr(5, 6) ** 3 * Fr(1, 6), Fr(125, 1296)); eq("T5 sf", sf(Fr(125, 1296)), 0.0965)
eq("T6 x", 35 + 28 - 50, 13); eq("T6 p", sf(Fr(13, 28)), 0.464)
eq("T7 C", 0.2 * 0.7 + 0.8 * 0.1, 0.22); eq("T7", sf(0.14 / 0.22), 0.636)
eq("T8", Fr(comb(5, 3), comb(12, 3)), Fr(1, 22)); eq("T8 sf", sf(Fr(1, 22)), 0.0455); eq("T8b", 1 - Fr(1, 22), Fr(21, 22)); eq("T8c", sf(Fr(21, 22)), 0.955); eq("220", comb(12, 3), 220)
r = Fr(6, 10) * Fr(5, 9) * Fr(4, 8); bl = Fr(4, 10) * Fr(3, 9) * Fr(2, 8)
eq("T9 r", r, Fr(120, 720)); eq("T9 b", bl, Fr(24, 720)); eq("T9 same", r + bl, Fr(1, 5)); eq("T9 cond", r / (r + bl), Fr(5, 6)); eq("0.833", sf(Fr(5, 6)), 0.833)
# quiz
eq("Q1", 0.3 + 0.4, 0.7); eq("Q1 prod", 0.3 * 0.4, 0.12); eq("Q5", Fr(3, 5) * Fr(2, 4), Fr(3, 10)); eq("Q5b", Fr(3, 5) * Fr(3, 5), Fr(9, 25)); eq("Q5c", Fr(3, 5) * Fr(2, 5), Fr(6, 25))
# ---- v2 additions (P13) ----
from math import factorial as fa, perm
from itertools import permutations
# warm-up
eq("w1", Fr(3, 8) * Fr(4, 7), Fr(3, 14)); eq("w2", Fr(12, 56), Fr(3, 14)); eq("w2 b", (0.8 - 0.6) / (1 - 0.6), 0.5); eq("w3", comb(8, 3), 56)
# proof: counting version
N = 1000; nA = N * 0.4; nAB = nA * 0.5; eq("proof", nAB / N, 0.4 * 0.5)
# long exam 1: Maya
pL, pML, pMn = 0.25, 0.6, 0.1
eq("L1 a1", pL * pML, 0.15); eq("L1 a2", (1 - pL) * pMn, 0.075); pM = pL * pML + (1 - pL) * pMn; eq("L1 a", pM, 0.225)
eq("L1 b", Fr(15, 100) / Fr(225, 1000), Fr(2, 3)); eq("L1 b sf", sf(Fr(2, 3)), 0.667)
eq("L1 c", 2 * 0.225 * 0.775, 0.34875); eq("L1 c sf", sf(2 * 0.225 * 0.775), 0.349); eq("L1 0.775", 1 - 0.225, 0.775)
eq("L1 d", 0.25 * 0.225, 0.05625); assert abs(0.25 * 0.225 - 0.15) > 1e-3; eq("L1 d2", 0.6, 0.6); assert 0.6 != 0.225
eq("L1 marks", 3 + 3 + 3 + 2, 11)
# long exam 2: counters
eq("L2 tot", comb(12, 3), 220); eq("L2 a", comb(5, 3) + comb(4, 3) + comb(3, 3), 15); eq("L2 a p", Fr(15, 220), Fr(3, 44)); eq("L2 a sf", sf(Fr(3, 44)), 0.0682)
eq("L2 b", comb(5, 2) * comb(7, 1), 70); eq("L2 b p", Fr(70, 220), Fr(7, 22)); eq("L2 b sf", sf(Fr(7, 22)), 0.318)
eq("L2 c no red", comb(7, 3), 35); eq("L2 c", 1 - Fr(35, 220), Fr(37, 44)); eq("L2 c ans", Fr(7, 22) / Fr(37, 44), Fr(14, 37)); eq("L2 c sf", sf(Fr(14, 37)), 0.378); eq("L2 c alt", Fr(70, 185), Fr(14, 37))
eq("L2 185", 220 - 35, 185)
# brute force on L2 via enumeration
cs = ["R"] * 5 + ["B"] * 4 + ["G"] * 3
sel = list(combinations(range(12), 3))
eq("L2 brute a", sum(1 for t in sel if len({cs[i] for i in t}) == 1), 15)
eq("L2 brute b", sum(1 for t in sel if sum(cs[i] == "R" for i in t) == 2), 70)
eq("L2 brute c", Fr(sum(1 for t in sel if sum(cs[i] == "R" for i in t) == 2), sum(1 for t in sel if sum(cs[i] == "R" for i in t) >= 1)), Fr(14, 37))
eq("L2 marks", 1 + 3 + 3 + 3, 10)
# spot the error
eq("se x", Fr(15, 40) * Fr(4, 100), Fr(15, 1000)); eq("se x dec", 15 / 40 * 0.04, 0.015); eq("se P(X)", 15 / 40, 0.375); eq("se wrong", 0.015 / 0.375, 0.04)
eq("se y", 25 / 40 * 0.02, 0.0125); eq("se F", 0.015 + 0.0125, 0.0275); eq("se ans", 0.015 / 0.0275, 6 / 11); eq("se ans sf", sf(0.015 / 0.0275), 0.545)
# exam practice
eq("E1a", 0.35 + 0.45 - 0.15, 0.65); eq("E1b", Fr(15, 45), Fr(1, 3))
eq("E2", sum(1 for a, b in S if abs(a - b) == 2), 8); eq("E2 p", Fr(8, 36), Fr(2, 9))
eq("E3 either", 60 - 9, 51); eq("E3 both", 32 + 24 - 51, 5); eq("E3 p", Fr(5, 24), Fr(5, 24)); eq("E3 sf", sf(Fr(5, 24)), 0.208)
eq("E4 WB", Fr(7, 10) * Fr(3, 9), Fr(21, 90)); eq("E4 BW", Fr(3, 10) * Fr(7, 9), Fr(21, 90)); eq("E4 a", Fr(42, 90), Fr(7, 15))
eq("E4 b", Fr(7, 10) * Fr(6, 9) + Fr(3, 10) * Fr(7, 9), Fr(7, 10)); eq("E4 42", Fr(7, 10) * Fr(6, 9), Fr(42, 90)); eq("E4 63", Fr(42, 90) + Fr(21, 90), Fr(63, 90))
b_ = (0.65 - 0.3) / 0.7; eq("E5 b", b_, 0.5); eq("E5 eq", 0.3 + 0.5 - 0.3 * 0.5, 0.65); eq("E5 neither", 1 - 0.65, 0.35); eq("E5 prod", 0.7 * 0.5, 0.35)
eq("E6 pos1", 0.02 * 0.95, 0.019); eq("E6 pos2", 0.98 * 0.08, 0.0784); eq("E6 pos", 0.019 + 0.0784, 0.0974); eq("E6 b", 0.019 / 0.0974, 0.195071868); eq("E6 sf", sf(0.019 / 0.0974), 0.195)
eq("E7 arr", fa(6) // (fa(3) * fa(2)), 60); eq("E7 block", fa(5) // fa(3), 20); eq("E7 p", Fr(20, 60), Fr(1, 3))
arr = set(permutations("BANANA")); eq("E7 brute", sum(1 for p in arr if "NN" in "".join(p)), 20); eq("E7 brute tot", len(arr), 60)
# E8: 4 red, n blue
sol = [n for n in range(1, 40) if Fr(4, 4 + n) * Fr(3, 3 + n) == Fr(1, 6)]; eq("E8 n", sol[0], 5); eq("E8 len", len(sol), 1)
eq("E8 expand", (5 + 4) * (5 + 3), 72); eq("E8 quad", 25 + 35 - 60, 0); eq("E8 factor", (5 + 12) * (5 - 5), 0); eq("E8 rr", Fr(4, 9) * Fr(3, 8), Fr(1, 6)); eq("E8 12/72", Fr(12, 72), Fr(1, 6))
eq("E8 RB", Fr(4, 9) * Fr(5, 8), Fr(20, 72)); eq("E8 BR", Fr(5, 9) * Fr(4, 8), Fr(20, 72)); eq("E8 b", Fr(40, 72), Fr(5, 9)); eq("E8 c", Fr(20, 72) / Fr(40, 72), Fr(1, 2))
eq("E8 marks", 5 + 2 + 2, 9)
# stretch: Monty Hall (simulate exactly)
pC = Fr(1, 3); pH = {1: Fr(1, 2), 2: Fr(1), 3: Fr(0)}
pH3 = sum(pC * pH[i] for i in (1, 2, 3)); eq("S1 H3", pH3, Fr(1, 2)); eq("S1 post", pC * pH[2] / pH3, Fr(2, 3)); eq("S1 post1", pC * pH[1] / pH3, Fr(1, 3))
import random
random.seed(1); w = 0; t = 0
for _ in range(200000):
    car = random.randint(1, 3)
    opts = [d for d in (2, 3) if d != car]
    op = random.choice(opts)
    if op == 3:
        t += 1; w += (car == 2)
eq("S1 sim", w / t, 2 / 3, 0.01)
# birthdays
pd = 1
for k in range(5): pd *= Fr(365 - k, 365)
eq("S2 a", float(pd), 0.9728644263, 1e-9); eq("S2 a sf", sf(float(pd)), 0.973); eq("S2 b", 1 - float(pd), 0.0271355737, 1e-9); eq("S2 b sf", sf(1 - float(pd)), 0.0271)
print("ok")
