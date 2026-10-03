# checks/math.s1.data.py: recomputes every number in the data chapter.
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def med(a):
    a = sorted(a); n = len(a); return a[n // 2] if n % 2 else (a[n // 2 - 1] + a[n // 2]) / 2
def quart(a):
    a = sorted(a); n = len(a); h = n // 2
    return med(a[:h]), med(a), med(a[h + 1:] if n % 2 else a[h:])
def mean(a): return sum(a) / len(a)
def sd(a): return sqrt(sum(x * x for x in a) / len(a) - mean(a) ** 2)

A = [23, 31, 28, 35, 42, 27, 31, 38, 45, 29, 33, 36, 31, 24, 40]
B = [26, 30, 32, 34, 35, 35, 37, 38, 39, 41, 44]
eq("nA", len(A), 15); q1, m, q3 = quart(A)
eq("q1", q1, 28); eq("med", m, 31); eq("q3", q3, 38); eq("iqr", q3 - q1, 10); eq("range", max(A) - min(A), 22)
assert sorted(A).count(31) == 3; eq("sumA", sum(A), 493); eq("meanA", sf(mean(A)), 32.9)
b1, bm, b3 = quart(B); eq("b1", b1, 32); eq("bm", bm, 35); eq("b3", b3, 39); eq("biqr", b3 - b1, 7); eq("nB", len(B), 11)
eq("fenceA", q3 + 1.5 * 10, 53); eq("fenceA lo", q1 - 15, 13)
# stem and leaf rows
assert [x % 10 for x in sorted(A) if x // 10 == 2] == [3, 4, 7, 8, 9]; assert [x % 10 for x in sorted(A) if x // 10 == 3] == [1, 1, 1, 3, 5, 6, 8]
assert [x % 10 for x in sorted(A) if x // 10 == 4] == [0, 2, 5]
assert [x % 10 for x in sorted(B) if x // 10 == 3] == [0, 2, 4, 5, 5, 7, 8, 9]
# means
eq("sd5", sd([4, 6, 8, 10, 12]), sqrt(8)); eq("sd5 sf", sf(sd([4, 6, 8, 10, 12])), 2.83); eq("ssq", sum(x * x for x in [4, 6, 8, 10, 12]), 360)
# goals table
xs = [1, 2, 3, 4, 5]; fs = [3, 7, 10, 6, 4]; n = sum(fs)
sfx = sum(x * f for x, f in zip(xs, fs)); sfx2 = sum(x * x * f for x, f in zip(xs, fs))
eq("n", n, 30); eq("sfx", sfx, 91); eq("sfx2", sfx2, 317); eq("mean", sf(sfx / n), 3.03)
var = sfx2 / n - (sfx / n) ** 2; eq("var", round(var, 3), 1.366); eq("sd", sf(sqrt(var)), 1.17)
data = [x for x, f in zip(xs, fs) for _ in range(f)]; eq("med", med(data), 3)
# coded
eq("coded mean", 60 + 24 / 10, 62.4); eq("var", 410 / 10 - 2.4 ** 2, 35.24); eq("sd", sf(sqrt(35.24)), 5.94)
# combine
eq("mean", (12 * 15 + 8 * 20) / 20, 17); s1 = 12 * (4 + 225); s2 = 8 * (9 + 400); eq("s1", s1, 2748); eq("s2", s2, 3272)
eq("var", (s1 + s2) / 20 - 289, 12); eq("sd", sf(sqrt(12)), 3.46)
# exam: runners
eq("mean", 600 / 25, 24); eq("var", 14700 / 25 - 576, 12); eq("sd", sf(sqrt(12)), 3.46)
eq("n2", 25 + 1, 26); eq("sum2", 14700 + 30 ** 2, 15600); eq("mean2", sf(630 / 26), 24.2)
v2 = 15600 / 26 - (630 / 26) ** 2; eq("var2", round(v2, 2), 12.87); eq("sd2", sf(sqrt(v2)), 3.59); eq("sq", round((630 / 26) ** 2, 2), 587.13)
# histogram
cls = [(0, 10, 12), (10, 20, 30), (20, 40, 24), (40, 60, 14)]
fd = [f / (b - a) for a, b, f in cls]; eq("fd", fd[0], 1.2); eq("fd", fd[1], 3); eq("fd", fd[2], 1.2); eq("fd", fd[3], 0.7); eq("N", sum(c[2] for c in cls), 80)
mid = [(a + b) / 2 for a, b, f in cls]; eq("mids", mid[2], 30)
fx = sum(m * c[2] for m, c in zip(mid, cls)); fx2 = sum(m * m * c[2] for m, c in zip(mid, cls))
eq("sfx", fx, 1930); eq("sfx2", fx2, 63650); eq("mean", fx / 80, 24.125); eq("mean sf", sf(fx / 80), 24.1)
v = fx2 / 80 - 24.125 ** 2; eq("var", round(v, 1), 213.6); eq("sd", sf(sqrt(v)), 14.6)
# ogive
eq("med", 10 + (40 - 12) / 30 * 10, 19 + 1 / 3); eq("q1", 10 + (20 - 12) / 30 * 10, 12 + 2 / 3); eq("q3", 20 + (60 - 42) / 24 * 20, 35)
eq("iqr", round(35 - (12 + 2 / 3), 1), 22.3); eq("cf30", 42 + 10 / 20 * 24, 54); eq("more", 80 - 54, 26)
eq("90", round(40 + (72 - 66) / 14 * 20, 1), 48.6); eq("med r", round(19 + 1 / 3, 1), 19.3); eq("q1 r", round(12 + 2 / 3, 1), 12.7)
# try
T1 = [7, 3, 9, 3, 12, 8, 3, 15]; a, b, c = quart(T1); eq("T1", b, 7.5); eq("q1", a, 3); eq("q3", c, 10.5); eq("iqr", c - a, 7.5)
eq("T4a", 18 / 5, 3.6); eq("T4b", round(24 / 15, 1), 1.6)
eq("T5", 19, 20 + -15 / 15); eq("T5 var", 135 / 15 - 1, 8); eq("T5 sd", sf(sqrt(8)), 2.83)
eq("T6", (15 * 8 + 10 * 13) / 25, 10)
T8 = [12, 14, 15, 15, 16, 17, 18, 19, 40]; a, b, c = quart(T8)
eq("T8 q1", a, 14.5); eq("T8 q3", c, 18.5); eq("T8 med", b, 16); eq("fence", c + 1.5 * (c - a), 24.5); assert 40 > 24.5
# quiz
eq("Q1 a", 20 / 10, 2); eq("Q1 b", 20 / 20, 1)
print("ok")
