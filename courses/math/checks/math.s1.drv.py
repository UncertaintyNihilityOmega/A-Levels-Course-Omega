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
# ---- v2 additions (P13) ----
from math import log
# warm-up
eq("w1", log(50) / log(2), 5.6439, 1e-4); eq("w1 sf", sf(log(50) / log(2)), 5.64); eq("w2", comb(10, 3), 120); eq("w3", Fr(25, 216), (Fr(5, 6) ** 2) * Fr(1, 6)); eq("w3 sf", sf(Fr(25, 216)), 0.116)
# proofs: E(X)=np algebra, and numeric checks
for n_, p_ in ((2, 0.5), (7, 0.3), (12, 0.25)):
    eq("proof np", sum(r * b(n_, p_, r) for r in range(n_ + 1)), n_ * p_, 1e-9)
    eq("proof r C", sum(r * comb(n_, r) for r in range(1, n_ + 1)), sum(n_ * comb(n_ - 1, r - 1) for r in range(1, n_ + 1)))
eq("proof B(2,.5)", 0 * .25 + 1 * .5 + 2 * .25, 1)
for q_ in (0.3, 0.5, 0.9):
    S_ = sum((k + 1) * q_ ** k for k in range(4000)); eq("proof S", S_, 1 / (1 - q_) ** 2, 1e-4)
    eq("proof E geo", sum(r * q_ ** (r - 1) * (1 - q_) for r in range(1, 4000)), 1 / (1 - q_), 1e-4)
eq("proof die", 1 / (1 / 6), 6)
# long exam 1
a_, b_ = 0.275, 0.225
eq("L1 sum", 0.15 + a_ + 0.35 + b_, 1); eq("L1 mean", a_ + 2 * 0.35 + 3 * b_, 1.65); eq("L1 a+b", a_ + b_, 0.5); eq("L1 a+3b", a_ + 3 * b_, 0.95); eq("L1 b", 0.45 / 2, 0.225)
Ex2 = a_ + 4 * 0.35 + 9 * b_; eq("L1 E2", Ex2, 3.7); eq("L1 parts", a_ + 1.4 + 2.025, 3.7); eq("L1 var", Ex2 - 1.65 ** 2, 0.9775); eq("L1 sq", 1.65 ** 2, 2.7225); eq("L1 var sf", sf(0.9775), 0.978)
P = {0: 0.15, 1: a_, 2: 0.35, 3: b_}
eq("L1 c", sum(P[i] * P[3 - i] for i in range(4) if 0 <= 3 - i <= 3), 0.26); eq("L1 c2", 2 * 0.15 * 0.225 + 2 * 0.275 * 0.35, 0.26); eq("L1 c parts", 0.0675 + 0.1925, 0.26)
eq("L1 c a", 2 * 0.15 * 0.225, 0.0675); eq("L1 c b", 2 * 0.275 * 0.35, 0.1925)
eq("L1 marks", 4 + 3 + 3, 10)
# long exam 2: bolts
p0 = 0.08
eq("L2 a", comb(15, 2) * p0 ** 2 * 0.92 ** 13, 0.2273, 1e-4); eq("L2 a sf", sf(b(15, p0, 2)), 0.227); eq("L2 105", comb(15, 2), 105)
eq("L2 .0064", p0 ** 2, 0.0064); eq("L2 .92^13", 0.92 ** 13, 0.33825, 1e-5)
eq("L2 b0", 0.92 ** 15, 0.2863, 1e-4); eq("L2 b1", 15 * p0 * 0.92 ** 14, 0.3734, 1e-4); eq("L2 b01", b(15, p0, 0) + b(15, p0, 1), 0.6597, 1e-4)
rej = 1 - b(15, p0, 0) - b(15, p0, 1); eq("L2 rej", sf(rej), 0.340)
eq("L2 c", 45 * 0.3403 ** 2 * 0.6597 ** 8, 0.187, 5e-4); eq("L2 c parts", 0.3403 ** 2, 0.11580, 1e-5); eq("L2 c parts2", 0.6597 ** 8, 0.035873, 1e-5)
eq("L2 c prod", 45 * 0.11580 * 0.035873, 0.187, 5e-4); eq("L2 c exact sf", sf(comb(10, 2) * rej ** 2 * (1 - rej) ** 8), 0.187); eq("L2 c 45", comb(10, 2), 45)
eq("L2 marks", 3 + 3 + 3 + 1, 10)
# spot the error
eq("se P2", sum(b(12, .25, r) for r in range(3)), 0.3907, 1e-4); eq("se P3", sum(b(12, .25, r) for r in range(4)), 0.6488, 1e-4)
eq("se wrong", 1 - 0.6488, 0.3512, 1e-4); eq("se wrong sf", sf(1 - 0.6488), 0.351); eq("se right", 1 - 0.3907, 0.6093, 1e-4); eq("se right sf", sf(1 - 0.3907), 0.609); eq("se mean", 12 * .25, 3)
# exam practice
eq("E1k", 1 - 0.2 - 0.4 - 0.1, 0.3); eq("E1 E", 1 * .2 + 2 * .4 + 3 * .3 + 4 * .1, 2.3)
eq("E2 p", comb(8, 3) * .4 ** 3 * .6 ** 5, 0.27869184, 1e-9); eq("E2 sf", sf(b(8, .4, 3)), 0.279); eq("E2 prod", 56 * 0.064 * 0.07776, 0.27869184, 1e-9); eq("E2 mean", 8 * .4, 3.2); eq("E2 var", 8 * .4 * .6, 1.92)
eq("E3 a", sf(g(.15, 4)), 0.0921); eq("E3 b", sf(.85 ** 6), 0.377); eq("E3 c", sf(1 / .15), 6.67)
eq("E4 p0", .85 ** 20, 0.0388, 5e-5); eq("E4 p1", 20 * .15 * .85 ** 19, 0.1368, 5e-5); eq("E4 p2", 190 * .15 ** 2 * .85 ** 18, 0.2293, 5e-5)
eq("E4 sum", .0388 + .1368 + .2293, 0.4049); eq("E4", sf(1 - sum(b(20, .15, r) for r in range(3))), 0.595); eq("E4 190", comb(20, 2), 190)
eq("E5 r", log(.05) / log(.7), 8.399, 1e-3); eq("E5 r sf", sf(log(.05) / log(.7)), 8.40)
eq("E5 check", min(r for r in range(1, 50) if 1 - .7 ** r > .95), 9); eq("E5 8", 1 - .7 ** 8 > .95, 0)
eq("E7 nets", [5 - 3, 4 - 3, 2 - 3, 0 - 3] == [2, 1, -1, -3], 1); eq("E7 ps", Fr(1, 2) + Fr(1, 4) + Fr(1, 8) + Fr(1, 8), 1)
xs7 = [2, 1, -1, -3]; ps7 = [Fr(1, 2), Fr(1, 4), Fr(1, 8), Fr(1, 8)]
e7, e72, v7 = stats(xs7, ps7); eq("E7 E", e7, 0.75); eq("E7 E2", e72, 3.5); eq("E7 var", v7, 2.9375); eq("E7 sd", sf(sqrt(float(v7))), 1.71)
eq("E7 parts", 1 + 0.25 - 0.125 - 0.375, 0.75); eq("E7 e2", 2 + .25 + .125 + 1.125, 3.5)
# E8: n, p
q8 = 4.2 / 6; eq("E8 q", q8, 0.7); eq("E8 n", 6 / 0.3, 20); eq("E8 pr", sf(b(20, .3, 6)), 0.192); eq("E8 C", comb(20, 6), 38760); eq("E8 .3^6", .3 ** 6, 0.000729); eq("E8 .7^14", .7 ** 14, 0.0067822, 1e-7)
eq("E8 prod", 38760 * 0.000729 * 0.0067822, 0.19164, 1e-4); eq("E8 m", log(.01) / log(.7), 12.911, 1e-3); eq("E8 m sf", sf(log(.01) / log(.7)), 12.9)
eq("E8 m min", min(m for m in range(1, 60) if 1 - .7 ** m > .99), 13); eq("E8 12", 1 - .7 ** 12 > .99, 0)
eq("E8 marks", 3 + 2 + 4, 9)
# stretch 1: Anil
pA = sum(Fr(5, 6) ** (2 * k) * Fr(1, 6) for k in range(0, 200)); eq("S1 pA", float(pA), 6 / 11, 1e-12); eq("S1 r", Fr(5, 6) ** 2, Fr(25, 36)); eq("S1 sum", Fr(1, 6) / (1 - Fr(25, 36)), Fr(6, 11)); eq("S1 B", 1 - Fr(6, 11), Fr(5, 11)); eq("S1 11/36", 1 - Fr(25, 36), Fr(11, 36))
eq("S1 t2", Fr(5, 6) ** 2 * Fr(1, 6), Fr(25, 216))
# stretch 2: memoryless
for a_, b_ in ((5, 3), (2, 7)):
    eq("S2 memoryless", (.8 ** (a_ + b_)) / (.8 ** a_), .8 ** b_, 1e-12)
eq("S2 b", .8 ** 3, 0.512)
print("ok")
