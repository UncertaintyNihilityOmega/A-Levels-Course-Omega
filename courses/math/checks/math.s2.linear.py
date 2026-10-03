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
print("ok")
