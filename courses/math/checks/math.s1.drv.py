# checks/math.s1.drv.py: recomputes every number in the Discrete random variables chapter.
from math import comb, sqrt, log, ceil
from fractions import Fraction as Fr

def eq(label, got, want, tol=1e-9): assert abs(float(got) - float(want)) <= tol, f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{float(x):.{n}g}")
def b(n, p, r): return comb(n, r) * p ** r * (1 - p) ** (n - r)
def g(p, r): return (1 - p) ** (r - 1) * p
def stats(xs, ps):
    e = sum(x * p for x, p in zip(xs, ps)); e2 = sum(x * x * p for x, p in zip(xs, ps)); return e, e2, e2 - e * e

# tables
k = 1 / 10; ps = [k * x for x in (1, 2, 3, 4)]; eq("sum", sum(ps), 1); e, e2, v = stats((1, 2, 3, 4), ps)
eq("E", e, 3); eq("E2", e2, 10); eq("Var", v, 1)
a = b_ = 0.25; eq("a+b", a + b_, 0.5); eq("mean", a + 2 * 0.3 + 3 * b_, 1.6); eq("a+3b", a + 3 * b_, 1)
e, e2, v = stats((0, 1, 2, 3), (0.2, 0.25, 0.3, 0.25)); eq("E", e, 1.6); eq("E2", e2, 3.7); eq("Var", v, 1.14); eq("sum", 0.2 + 0.25 + 0.3 + 0.25, 1)
# game
e, e2, v = stats((-2, -1, 3), (1 / 2, 1 / 3, 1 / 6)); eq("G sum", 1 / 2 + 1 / 3 + 1 / 6, 1); eq("G E", e, -5 / 6); eq("G E sf", sf(e), -0.833)
eq("G E2", e2, 3.8333333333, 1e-6); eq("G var", v, 3.8333333333 - 25 / 36, 1e-6); eq("G var sf", sf(v), 3.14); eq("G sd", sf(sqrt(v)), 1.77); eq("var 3dp", round(v, 3), 3.139)
# binomial 10, .3
eq("P3", b(10, .3, 3), 0.267, 5e-4); eq("120x", 120 * 0.027 * 0.0823543, b(10, .3, 3), 1e-6); eq("0.7^7", 0.7 ** 7, 0.0823543, 1e-9)
eq("P0", b(10, .3, 0), 0.0282, 5e-5); eq("P1", b(10, .3, 1), 0.1211, 5e-5); eq("P2", b(10, .3, 2), 0.2335, 5e-5)
eq("P<=2", sum(b(10, .3, r) for r in range(3)), 0.383, 5e-4); eq("P<=3", sum(b(10, .3, r) for r in range(4)), 0.3828 + 0.2668, 1e-4)
eq("P>=4", 1 - sum(b(10, .3, r) for r in range(4)), 0.350, 5e-4); eq("mean", 10 * 0.3, 3); eq("var", 10 * .3 * .7, 2.1)
# bulbs
eq("P0", .96 ** 20, 0.442, 5e-4); eq("P1", b(20, .04, 1), 0.3683, 5e-5); eq("P2", b(20, .04, 2), 0.1458, 5e-5); eq("P<=2", sum(b(20, .04, r) for r in range(3)), 0.956, 5e-4)
eq("0.4420", .96 ** 20, 0.4420, 5e-5)
n = log(0.1) / log(0.96); eq("n", round(n, 1), 56.4); eq("n", ceil(n), 57); eq("0.96^56", .96 ** 56, 0.1017, 5e-5); eq("0.96^57", .96 ** 57, 0.0976, 5e-5)
assert .96 ** 56 > 0.1 > .96 ** 57
# geometric
eq("g4", g(1 / 6, 4), 0.0965, 5e-5); eq("gt4", (5 / 6) ** 4, 0.482, 5e-4); eq("le3", 1 - (5 / 6) ** 3, 0.421, 5e-4); eq("E", 1 / (1 / 6), 6)
eq("ft", 0.3 ** 2 * 0.7, 0.063); eq("1/0.7", sf(1 / 0.7), 1.43)
eq("P(X>r)", sum(g(0.25, r) for r in range(4, 4000)), 0.75 ** 3, 1e-9)
eq("E geo", sum(r * g(0.25, r) for r in range(1, 4000)), 4, 1e-6)
# exam 8, .35
eq("P3", b(8, .35, 3), 0.279, 5e-4); eq("56x", 56 * 0.042875 * 0.116029, b(8, .35, 3), 1e-5); eq("P>=5", sum(b(8, .35, r) for r in range(5, 9)), 0.106, 5e-4)
eq("mean", 8 * .35, 2.8); eq("var", 8 * .35 * .65, 1.82); eq("geo3", .65 ** 2 * .35, 0.148, 5e-4)
# try
ps = [k_ * 0.1 for k_ in (4, 3, 2, 1)]; eq("T1 sum", sum(ps), 1); e, e2, v = stats((1, 2, 3, 4), ps); eq("T1 E", e, 2); eq("T1 E2", e2, 5); eq("T1 v", v, 1)
e, e2, v = stats((2, 4, 6, 8), (.1, .4, .3, .2)); eq("T2 E", e, 5.2); eq("T2 E2", e2, 30.4); eq("T2 v", v, 3.36); eq("T2 sd", sf(sqrt(v)), 1.83)
eq("T3", Fr(15, 64), b(6, .5, 2)); eq("T3 sf", sf(b(6, .5, 2)), 0.234); eq("T3b", sum(b(6, .5, r) for r in (5, 6)), 7 / 64); eq("T3c", sf(7 / 64), 0.109)
eq("T4", sum(b(15, .4, r) for r in range(7)), 0.610, 5e-4); eq("T4b", b(15, .4, 6), 0.207, 5e-4); eq("T4 mean", 15 * .4, 6); eq("T4 var", 15 * .4 * .6, 3.6)
eq("T5", 1 - (5 / 6) ** 5, 0.598, 5e-4)
eq("T6a", .8 ** 4 * .2, 0.0819, 5e-5); eq("T6b", .8 ** 5, 0.328, 5e-4); eq("T6c", 1 / .2, 5)
n8 = log(0.05) / log(0.96); eq("T8", round(n8, 1), 73.4); eq("T8 n", ceil(n8), 74); assert 1 - .96 ** 73 < .95 < 1 - .96 ** 74
eq("T9", b(12, .25, 4), 0.194, 5e-4); eq("495", comb(12, 4), 495); eq("T9b", 1 - .75 ** 12, 0.968, 5e-4); eq("0.0317", .75 ** 12, 0.0317, 5e-5); eq("0.100113", .75 ** 8, 0.100113, 5e-7)
# quiz
eq("Q2", 20 * .3, 6); eq("Q2 var", 20 * .3 * .7, 4.2); eq("Q3", .8 ** 3, 0.512); eq("Q4", 12 - 9, 3)
print("ok")
