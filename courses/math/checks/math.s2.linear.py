# checks/math.s2.linear.py: recomputes every number in the linear combinations chapter.
from math import isclose, exp, factorial, sqrt
from statistics import NormalDist

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

Z = NormalDist()
Phi = Z.cdf

# Temperature
eq("E F", 1.8 * 18 + 32, 64.4); eq("Var F", 1.8 ** 2 * 4, 12.96); eq("sd F", sqrt(12.96), 3.6)
# Postage
eq("E P", 4 + 1.5 * 2.6, 7.9); eq("Var P", 1.5 ** 2 * 1.04, 2.34); eq("sd P", sf(sqrt(2.34)), 1.53)
# Discrete table
p = {1: 0.2, 2: 0.5, 3: 0.3}
EX = sum(k * q for k, q in p.items()); EX2 = sum(k * k * q for k, q in p.items())
eq("EX", EX, 2.1); eq("EX2", EX2, 4.9); eq("VarX", EX2 - EX ** 2, 0.49)
eq("E3X-2", 3 * EX - 2, 4.3); eq("Var3X-2", 9 * (EX2 - EX ** 2), 4.41)
Y = {3 * k - 2: q for k, q in p.items()}
eq("Y mean", sum(k * q for k, q in Y.items()), 4.3); eq("Y sq", sum(k * k * q for k, q in Y.items()), 22.9)
eq("Y var", 22.9 - 4.3 ** 2, 4.41); eq("wrong 3Var", 3 * 0.49, 1.47)
# 2X - 3Y + 1
eq("E comb", 2 * 5 - 3 * 2 + 1, 5); eq("Var comb", 4 * 4 + 9 * 9, 97)
# Bottles
eq("Var 2X", 4 * 16, 64); eq("Var X1+X2", 16 + 16, 32)
eq("tail sum z", sf(10 / sqrt(32), 4), 1.768); eq("tail sum", sf(1 - Phi(10 / sqrt(32)), 3), 0.0385)
eq("tail 2X", sf(1 - Phi(10 / 8)), 0.106)
# Lift
eq("lift var", 4 * 64, 256); eq("lift", sf(1 - Phi(1.25)), 0.106); eq("Phi1.25", round(Phi(1.25), 4), 0.8944)
eq("lift k", sf(300 + Z.inv_cdf(0.95) * 16), 326); eq("1.645", round(Z.inv_cdf(0.95), 3), 1.645)
# Bus bike
eq("bus", sf(Phi(0.6)), 0.726)
# Croissants
v = 25 + 25 + 36
eq("box var", v, 86); eq("box sd", sf(sqrt(v), 4), 9.274)
eq("box z", sf(15 / sqrt(v), 4), 1.617); eq("box Phi", round(Phi(1.617), 4), 0.9471); eq("box", sf(1 - Phi(15 / sqrt(v))), 0.0529)
# Poisson sum
po = lambda l, r: exp(-l) * l ** r / factorial(r)
eq("a", sf(po(5, 6)), 0.146); eq("b", sf(1 - sum(po(5, k) for k in range(3))), 0.875); eq("b form", 1 - 18.5 * exp(-5), 1 - sum(po(5, k) for k in range(3)))
eq("Po2 2X var", 2 ** 2 * 2, 8)
# Try
eq("t1a", 4 * 10 - 1, 39); eq("t1b", 16 * 3, 48); eq("t1c", 4 * 3, 12)
eq("t2a", 18 - 9, 9); eq("t2b", 9 * 2 + 5, 23)
eq("t3a", 36, 3 * 12); eq("t3b", 27, 3 * 9); eq("t3c", 81, 9 * 9)
eq("t4 var", 36 + 64, 100); eq("t4", sf(1 - Phi(1)), 0.159)
eq("t5", sf(Phi(0.5)), 0.691)
eq("t6 var", 6 * 400, 2400); eq("t6 sd", sf(sqrt(2400), 4), 48.99); eq("t6 z", sf(100 / sqrt(2400), 4), 2.041); eq("t6", sf(1 - Phi(100 / sqrt(2400)), 3), 0.0206)
eq("t7", sf(po(4, 2)), 0.147); eq("t7 form", 8 * exp(-4), po(4, 2))
eq("t8 E", 12 * 250 + 80, 3080); eq("t8 var", 12 * 9 + 4, 112); eq("t8 z", sf(-10 / sqrt(112), 3), -0.945); eq("t8", sf(Phi(-10 / sqrt(112))), 0.172)
eq("t9 var", 6.25 + 9, 15.25); eq("t9 sd", sf(sqrt(15.25), 4), 3.905); eq("t9a z", sf(-1 / sqrt(15.25), 3), -0.256); eq("t9a", sf(Phi(-1 / sqrt(15.25))), 0.399)
eq("t9b z", sf(-3 / sqrt(15.25), 3), -0.768); eq("t9b", sf(Phi(-3 / sqrt(15.25))), 0.221)
eq("t10 E", 4 * 1010, 4040); eq("t10 var", 4 * 144, 576); eq("t10 sd", sqrt(576), 24); eq("t10 wrong", 4 * 12, 48)
# Quiz
eq("q1", 9 * 5, 45); eq("q2", 4 + 1, 5); eq("q3", 4 + 4, 8); eq("q3b", 4 * 4, 16)
eq("q4 var2X", 4 * 3, 12); eq("q5", sqrt(9 + 16), 5)

# ---- P14 additions ----
from math import comb
def po(l, r): return exp(-l) * l ** r / factorial(r)
def cdf(l, r): return sum(po(l, k) for k in range(r + 1))
# warm-up
w = {1: 0.5, 2: 0.3, 4: 0.2}
m = sum(k * q for k, q in w.items()); m2 = sum(k * k * q for k, q in w.items())
eq("w1 E", m, 1.9); eq("w1 E2", m2, 4.9); eq("w1 Var", m2 - m * m, 1.29)
eq("w2", sf(Phi(2) - Phi(-1)), 0.819); eq("w3 coef", 1 + 3.5 + 3.5 ** 2 / 2, 10.625); eq("w3", sf(cdf(3.5, 2)), 0.321)
# proofs: aX+b and variance formula on the table 1,2,3 / 0.2,0.5,0.3
eq("proof 3X-2 values", sum((3 * k - 2) * q for k, q in p.items()), 4.3)
eq("proof mu^2", 2.1 ** 2, 4.41)
# variance of sum with independence: brute force over a joint table
import itertools
px = {1: 0.2, 2: 0.5, 3: 0.3}; py = {0: 0.4, 5: 0.6}
mx = sum(k * q for k, q in px.items()); my = sum(k * q for k, q in py.items())
vs = sum(((a + b) - (mx + my)) ** 2 * qa * qb for (a, qa), (b, qb) in itertools.product(px.items(), py.items()))
vx = sum((a - mx) ** 2 * q for a, q in px.items()); vy = sum((b - my) ** 2 * q for b, q in py.items())
eq("indep var adds", vs, vx + vy)
# spot the error
eq("sp E", 3 * 150, 450); eq("sp wrong var", 9 * 400, 3600); eq("sp wrong p", sf(1 - Phi(0.5)), 0.309)
eq("sp z", round(30 / sqrt(1200), 3), 0.866); eq("sp good", sf(1 - Phi(30 / sqrt(1200))), 0.193)
# exam practice
eq("e1 E", 3 * 8 - 4, 20); eq("e1 V", 9 * 5, 45); eq("e1 sd", sf(sqrt(4 * 5)), 4.47)
eq("e2 E", 2 * 12 - 3 * 7, 3); eq("e2 V", 4 * 3 + 9 * 2, 30)
eq("e3", sf(po(5.5, 4)), 0.156)
eq("e4 E", 4 * 1008, 4032); eq("e4 V", 4 * 25, 100); eq("e4", sf(Phi(-1.2)), 0.115)
eq("e5 E", 60 - 56, 4); eq("e5 V", 16 + 4 * 9, 52); eq("e5 z", round(4 / sqrt(52), 3), 0.555); eq("e5", sf(Phi(4 / sqrt(52))), 0.710)
eq("e6 cdf", round(cdf(10, 11), 4), 0.6968); eq("e6", sf(1 - cdf(10, 11)), 0.303)
eq("e6b m", 2 * 4, 8); eq("e6b v", 4 * 4, 16)
eq("e7 E", 4 * 72, 288); eq("e7 V", 4 * 81, 324); eq("e7 z", round(32 / 18, 3), 1.778); eq("e7a", sf(1 - Phi(32 / 18)), 0.0377)
zz = Z.inv_cdf(0.99); eq("e7 zz", round(zz, 3), 2.326); eq("e7 coef", round(9 * zz, 2), 20.94)
a, b, c = 72, 9 * zz, -500
s = (-b + sqrt(b * b - 4 * a * c)) / (2 * a); eq("e7 sqrt n", round(s, 3), 2.494); eq("e7 n", round(s * s, 2), 6.22)
n6 = (500 - 72 * 6) / (9 * sqrt(6)); eq("e7 n6 sd", round(9 * sqrt(6), 2), 22.05); eq("e7 n6 z", round(n6, 2), 3.08)
eq("e7 n6 p", sf(1 - Phi(n6)), 0.00102); assert 72 * 7 > 500
n5 = (500 - 72 * 7) / (9 * sqrt(7)); assert 1 - Phi(n5) > 0.5
# stretch
eq("s1 z", round(Z.inv_cdf(0.975), 2), 1.96); eq("s1 n", round((1.96 * 4) ** 2, 2), 61.47)
assert (1.96 * 4) ** 2 > 61 and 62 >= (1.96 * 4) ** 2
sx = {1: .25, 2: .5, 3: .25}; ex = sum(k * q for k, q in sx.items()); ex2 = sum(k * k * q for k, q in sx.items())
eq("s2 E", ex, 2); eq("s2 E2", ex2, 4.5); eq("s2 Var", ex2 - ex * ex, 0.5)
assert all(4 - x + x == 4 for x in sx)
print("ok")
