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
print("ok")
