# checks/math.s1.perms.py: recomputes every number in the permutations chapter.
from math import isclose, factorial as f, comb, perm
from itertools import permutations, combinations

def eq(label, got, want): assert got == want, f"{label}: computed {got}, chapter says {want}"
def rep(n, *ks):
    d = f(n)
    for k in ks: d //= f(k)
    return d

eq("meal", 4 * 6 * 3, 72); eq("skip", 6 * 3 + 4 * 6, 42)
eq("5!", f(5), 120); eq("10P3", perm(10, 3), 720); eq("10x9x8", 10 * 9 * 8, 720); eq("7C4", comb(7, 4), 35); eq("6C3", comb(6, 3), 20)
eq("nPr", perm(7, 3), f(3) * comb(7, 3))
eq("banana", rep(6, 3, 2), 60); eq("mississippi", rep(11, 4, 4, 2), 34650); eq("11!", f(11), 39916800); eq("1152", 24 * 24 * 2, 1152)
eq("stat", rep(8, 3, 2), 3360); eq("8!", f(8), 40320)
# brute force check of STATISTICS S's together
w = "STATISTICS"; eq("len", len(w), 10); eq("S3", w.count("S"), 3); eq("T3", w.count("T"), 3); eq("I2", w.count("I"), 2)
# method check by brute force on a smaller word: SSSTTII
small = set(permutations("SSSTTII"))
eq("small total", len(small), rep(7, 3, 2, 2)); eq("small together", sum(1 for s in small if "SSS" in "".join(s)), rep(5, 2, 2))
eq("small ends T", sum(1 for s in small if s[0] == "T" and s[-1] == "T"), rep(5, 3, 2))
# 8 people
eq("8!", f(8), 40320); eq("together", 2 * f(7), 10080); eq("apart", f(8) - 10080, 30240); eq("ends", 2 * f(6), 1440)
nums = [p for p in permutations(range(1, 8), 4)]
eq("total", len(nums), 840); eq("even", sum(1 for p in nums if p[-1] % 2 == 0), 360); eq("odd", sum(1 for p in nums if p[-1] % 2), 480)
eq("gt5000", sum(1 for p in nums if p[0] >= 5), 360); eq("360", 3 * 6 * 5 * 4, 360)
eq("4 digit", 9 * 9 * 8 * 7, 4536)
# team
eq("10C5", comb(10, 5), 252); eq("2g", comb(4, 2) * comb(6, 3), 120); eq("no girl", comb(6, 5), 6); eq("ge1", 252 - 6, 246); eq("zara", comb(9, 4), 126)
# committee
eq("11C5", comb(11, 5), 462); eq("0w", comb(7, 5), 21); eq("1w", comb(4, 1) * comb(7, 4), 140); eq("ge2", 462 - 21 - 140, 301)
eq("2w", comb(4, 2) * comb(7, 3), 210); eq("3w", comb(4, 3) * comb(7, 2), 84); eq("4w", comb(4, 4) * comb(7, 1), 7); eq("sum", 210 + 84 + 7, 301)
# rows
eq("rows", f(8), 40320); eq("AB front", perm(4, 2) * f(6), 8640); eq("12x720", 12 * 720, 8640)
# code
eq("letters", perm(8, 3), 336); eq("digits", perm(9, 2), 72); eq("codes", 336 * 72, 24192); eq("with A", 3 * perm(7, 2), 126); eq("with A codes", 126 * 72, 9072)
eq("alt A", perm(8, 3) - perm(7, 3), 126)
# try
eq("6!/4!", f(6) // f(4), 30); eq("9C4", comb(9, 4), 126); eq("letter", rep(6, 2, 2), 180)
eq("T4", sum(1 for p in permutations(range(1, 10), 3) if p[-1] % 2 == 0), 224); eq("T4b", 4 * 8 * 7, 224)
eq("T5", 2 * f(4), 48); eq("T6", comb(8, 3), 56); eq("T6b", perm(8, 3), 336)
# T8 no two girls adjacent
cnt = 0
for arr in set(permutations("BBBBBGGG")):
    if "GG" not in "".join(arr): cnt += 1
eq("T8 arrangements of types", cnt, comb(6, 3)); eq("T8", f(5) * f(3) * comb(6, 3), 14400); eq("T8b", f(5) * perm(6, 3), 14400); eq("120x120", 120 * 120, 14400)
# T9
eq("T9 together", rep(8, 3, 2), 3360); eq("T9 ends", rep(8, 3, 2), 3360)
# quiz
eq("Q1", comb(10, 3), 120); eq("Q2", rep(5, 2, 2), 30); eq("Q3", 2 * f(3), 12); eq("Q4", comb(6, 5), 6)
# ---- v2 additions (P13) ----
# warm-up
eq("w1", 2 ** 3 * 3 ** 2, 72); eq("w2", comb(5, 2), 10); eq("w3", 7 * 6 * 5 * 4 // (4 * 3 * 2 * 1), 35); eq("w3b", 210 // 6, 35)
# proofs
for n_, r_ in ((10, 3), (7, 4), (9, 5)):
    eq("perm formula", perm(n_, r_), f(n_) // f(n_ - r_)); eq("comb=P/r!", comb(n_, r_), perm(n_, r_) // f(r_))
eq("proof P10_3", 10 * 9 * 8, 720); eq("proof 10!/7!", f(10) // f(7), 720); eq("proof P74", perm(7, 4), 840); eq("proof 840/24", 840 // f(4), 35)
eq("proof banana", f(6) // (f(3) * f(2)), 60)
# brute force: labelled arrangements divide by p!q!
from collections import Counter
eq("banana brute", len(set(permutations("BANANA"))), 60)
# spot the error COMMITTEE
eq("se letters", len("COMMITTEE"), 9); eq("se counts", sorted(Counter("COMMITTEE").values()), [1, 1, 1, 2, 2, 2])
eq("se wrong den", 2 + 2 + 2, 6); eq("se wrong", f(9) // 6, 60480); eq("se 9!", f(9), 362880)
eq("se right", f(9) // (2 * 2 * 2), 45360); eq("se right2", rep(9, 2, 2, 2), 45360)
# long exam 1: digits 1..8, 5-digit
D = range(1, 9)
tot = list(permutations(D, 5)); eq("L1a", len(tot), 6720); eq("L1a f", perm(8, 5), 6720)
ev = [p for p in tot if p[-1] % 2 == 0]; eq("L1b", len(ev), 3360); eq("L1b f", 4 * 7 * 6 * 5 * 4, 3360); eq("L1b 840", 7 * 6 * 5 * 4, 840)
def num(p): return int("".join(map(str, p)))
big = [p for p in ev if num(p) > 60000]; eq("L1c", len(big), 1200)
eq("L1c 68", len([p for p in ev if p[0] in (6, 8)]), 720); eq("L1c 6", len([p for p in ev if p[0] == 6]), 360); eq("L1c 7", len([p for p in ev if p[0] == 7]), 480)
eq("L1c 360", 3 * 6 * 5 * 4, 360); eq("L1c 480", 4 * 6 * 5 * 4, 480); eq("L1c sum", 720 + 480, 1200)
both = [p for p in tot if 1 in p and 2 in p]; eq("L1d", len(both), 2400); eq("L1d f", perm(5, 2) * perm(6, 3), 2400); eq("L1d a", perm(5, 2), 20); eq("L1d b", perm(6, 3), 120)
eq("L1 marks", 1 + 2 + 4 + 3, 10)
# long exam 2: council
eq("L2a", comb(13, 6), 1716); eq("L2b", comb(5, 2) * comb(8, 4), 700); eq("L2b parts", comb(5, 2), 10); eq("L2b parts2", comb(8, 4), 70)
eq("L2c0", comb(8, 6), 28); eq("L2c1", comb(5, 1) * comb(8, 5), 280); eq("L2c55", comb(8, 5), 56); eq("L2c", 1716 - 28 - 280, 1408)
alt = sum(comb(5, t) * comb(8, 6 - t) for t in range(2, 6)); eq("L2c alt", alt, 1408)
eq("L2d", comb(11, 4), 330); eq("L2d", 1716 - 330, 1386)
from fractions import Fraction
eq("L2e", Fraction(700, 1716), Fraction(175, 429)); eq("L2e dec", float(f"{700 / 1716:.3g}"), 0.408)
eq("L2 marks", 1 + 2 + 4 + 2 + 2, 11)
# exam practice
eq("E1a", perm(9, 2), 72); eq("E1b", comb(9, 3), 84)
eq("E2a", rep(6, 2), 360); eq("E2a brute", len(set(permutations("STATIC"))), 360); eq("E2b", rep(5, 2), 60)
eq("E2b brute", len([p for p in set(permutations("STATIC")) if p[0] == "S"]), 60)
nums = [p for p in permutations(range(10), 4) if p[0] != 0 and p[-1] % 2 == 0]
eq("E3", len(nums), 2296); eq("E3 a", 9 * 8 * 7, 504); eq("E3 b", 4 * 8 * 8 * 7, 1792); eq("E3 sum", 504 + 1792, 2296)
eq("E3 last0", len([p for p in nums if p[-1] == 0]), 504)
eq("E4 tot", comb(11, 4), 330); eq("E4 j", comb(6, 4), 15); eq("E4 s", comb(5, 4), 5); eq("E4", 330 - 15 - 5, 310)
eq("E4 alt", sum(comb(6, j) * comb(5, 4 - j) for j in range(1, 4)), 310)
cnt = 0
for p in permutations(range(7)):
    # 0 = Dev, 1 = Eva, 2 = Fay
    i0 = p.index(0)
    if i0 not in (0, 6): continue
    if abs(p.index(1) - p.index(2)) == 1: cnt += 1
eq("E5 brute", cnt, 480); eq("E5", 2 * f(5) * 2, 480); eq("E5 half", f(5) * 2, 240)
eq("E6 tot", comb(8, 4), 70); eq("E6 fav", comb(3, 2) * comb(5, 2), 30); eq("E6", Fraction(30, 70), Fraction(3, 7))
# E7: n = 10
sol = [n for n in range(2, 60) if perm(n, 2) - comb(n, 2) == 45]; eq("E7 n", sol, [10])
eq("E7 diff", 10 * 9 - 45, 45); eq("E7 half", 10 * 9 // 2, 45); eq("E7 quad", (10 - 10) * (10 + 9), 0); eq("E7 expand", -10 + 9, -1); eq("E7 prod", -10 * 9, -90)
eq("E7b", comb(10, 3), 120); eq("E7b0", comb(6, 3), 20); eq("E7b", 120 - 20, 100)
eq("E7b alt", sum(comb(4, j) * comb(6, 3 - j) for j in range(1, 4)), 100)
# E8: BOOKKEEPER
W = "BOOKKEEPER"; eq("E8 len", len(W), 10); eq("E8 counts", sorted(Counter(W).values()), [1, 1, 1, 2, 2, 3])
eq("E8a", rep(10, 2, 2, 3), 151200); eq("E8a den", f(2) * f(2) * f(3), 24); eq("E8a num", f(10), 3628800)
eq("E8b", rep(8, 2, 2), 10080)
others = "BOOKKPR"; eq("E8c others", rep(7, 2, 2), 1260); eq("E8c gaps", comb(8, 3), 56)
eq("E8c", 1260 * 56, 70560)
Epos = [c for c in combinations(range(10), 3) if all(c[i + 1] - c[i] > 1 for i in range(2))]
eq("E8c pos", len(Epos), 56); eq("E8c total", len(Epos) * len(set(permutations(others))), 70560)
eq("E8b brute", len([c for c in combinations(range(10), 3) if c[2] - c[0] == 2]) * 1260, 8 * 7 // 1 * 1260 // 1 if False else 10080)
# stretch 1: polygon
eq("S1a", comb(12, 2) - 12, 54); eq("S1a pairs", comb(12, 2), 66); eq("S1b", comb(12, 3), 220)
n_ = 12
def sides(tri):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if (tri[j] - tri[i]) % n_ in (1, n_ - 1))
tris = list(combinations(range(n_), 3))
eq("S1 two", len([t for t in tris if sides(t) == 2]), 12); eq("S1 one", len([t for t in tris if sides(t) == 1]), 96)
eq("S1 one f", 12 * (12 - 4), 96); eq("S1 none", len([t for t in tris if sides(t) == 0]), 112); eq("S1c", 220 - 108, 112); eq("S1 formula", 12 * 8 * 7 // 6, 112)
# stretch 2: grid
eq("S2a", comb(10, 4), 210)
from itertools import product
routes = [r for r in set(permutations("RRRRRRUUUU"))]
eq("S2a brute", len(routes), 210)
def thru(r):
    x = y = 0
    for s_ in r:
        if s_ == "R": x += 1
        else: y += 1
        if (x, y) == (3, 2): return True
    return False
eq("S2b", len([r for r in routes if thru(r)]), 100); eq("S2b f", comb(5, 2) * comb(5, 2), 100); eq("S2c", 210 - 100, 110)
print("ok")
