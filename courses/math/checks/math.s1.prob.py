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
print("ok")
