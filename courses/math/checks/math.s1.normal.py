# checks/math.s1.normal.py: recomputes every number in the Normal distribution chapter.
from statistics import NormalDist
from math import comb, sqrt

Z = NormalDist(); P = Z.cdf; inv = Z.inv_cdf
def eq(label, got, want, tol=1e-9): assert abs(float(got) - float(want)) <= tol, f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{float(x):.{n}g}")
def r4(x): return round(x, 4)

# plot caption and E1
eq("P(1.25)", r4(P(1.25)), 0.8944); eq("P(-1)", r4(P(-1)), 0.1587); eq("diff", r4(P(1.25)) - r4(P(-1)), 0.7357); eq("exact", r4(P(1.25) - P(-1)), 0.7357)
eq("a", r4(P(1)), 0.8413); eq("z b", (45 - 50) / 8, -0.625); eq("b", sf(P(0.625)), 0.734); eq("c", sf(P(1.25) - P(-1)), 0.736)
# flour
eq("z", round((490 - 500) / 6, 3), -1.667); eq("flour", sf(P(-10 / 6)), 0.0478); eq("z90", round(inv(.9), 4), 1.2816); eq("m", round(500 + inv(.9) * 6, 1), 507.7)
# tests and rods
eq("z1", (70 - 62) / 8, 1); eq("z2", (63 - 55) / 5, 1.6); eq("84.1", round(100 * P(1), 1), 84.1); eq("94.5", round(100 * P(1.6), 1), 94.5)
eq("lo", round((19.7 - 20) / 0.15, 6), -2); eq("hi", round((20.3 - 20) / 0.15, 6), 2); eq("acc", r4(P(2) - P(-2)), 0.9545); eq("0.9772", r4(P(2)), 0.9772); eq("0.0228", r4(P(-2)), 0.0228)
eq("rej", r4(1 - (P(2) - P(-2))), 0.0455); eq("500", round(500 * 0.0455, 2), 22.75)
# inverse
eq("95", round(inv(.95), 4), 1.6449); eq("975", round(inv(.975), 4), 1.96); eq("k", round(50 + inv(.9) * 8, 1), 60.3); eq("sigma", sf(10 / inv(.95)), 6.08)
# two unknowns
z1 = inv(.2); z2 = inv(.9); eq("z1", round(z1, 4), -0.8416); eq("z2", round(z2, 4), 1.2816); eq("sum", round(z2 - z1, 4), 2.1232)
s = 20 / (z2 - z1); m = 30 - z1 * s; eq("sigma", sf(s), 9.42); eq("mu", sf(m), 37.9)
eq("check", round((50 - 37.9) / 9.42, 2), 1.28); eq("12.1", round(50 - 37.9, 1), 12.1)
eq("mu eq", 30 - 0.8416 * 9.42, 30 - 0.8416 * 9.42)
# approximation
n, p = 40, .3; mu = n * p; v = n * p * (1 - p); sd = sqrt(v)
eq("mu", mu, 12); eq("v", v, 8.4); eq("sd", round(sd, 3), 2.898); eq("z", round((15.5 - mu) / sd, 3), 1.208); eq("a", sf(P((15.5 - mu) / sd)), 0.886)
ex = sum(comb(n, r) * p ** r * (1 - p) ** (n - r) for r in range(16)); eq("exact", sf(ex), 0.885)
za, zb = (9.5 - mu) / sd, (10.5 - mu) / sd; eq("za", round(za, 3), -0.863); eq("zb", round(zb, 3), -0.518); eq("b", sf(P(zb) - P(za)), 0.108)
eq("ex10", sf(comb(n, 10) * p ** 10 * (1 - p) ** 30), 0.113)
# drug
n, p = 80, .4; eq("np", n * p, 32); eq("nq", n * (1 - p), 48); eq("var", n * p * (1 - p), 19.2); sd = sqrt(19.2)
eq("sd", round(sd, 3), 4.382); eq("z", round(3.5 / sd, 3), 0.799); eq("p", sf(1 - P(3.5 / sd)), 0.212)
# try
eq("T1a", sf(1 - P(1.4)), 0.0808); eq("T1b", sf(P(-1)), 0.159); eq("T1c", sf(P(1.4) - P(-1)), 0.761); eq("0.9192", r4(P(1.4)), 0.9192)
eq("T2", sf(1 - P(1.5)), 0.0668); eq("T3 z", round(inv(.25), 4), -0.6745); eq("T3", sf(70 + inv(.25) * 12), 61.9)
eq("T4a", round(inv(.1), 4), -1.2816); eq("T4b", round(inv(.7), 4), 0.5244)
eq("T5", sf(40 + 1.5 * 6), 49.0); eq("T5 p", sf(P(-1.5)), 0.0668)
z1 = inv(.1); z2 = inv(.8); eq("T6 z2", round(z2, 4), 0.8416); s = 10 / (z2 - z1); eq("T6 sum", round(z2 - z1, 4), 2.1232); eq("T6 s", sf(s), 4.71); eq("T6 mu", sf(20 - z1 * s), 26.0)
eq("T7 mu", 20, 50 * .4); eq("T7 var", 12, 50 * .4 * .6); eq("T7 z", round(4.5 / sqrt(12), 3), 1.299); eq("T7", sf(P(4.5 / sqrt(12))), 0.903)
eq("T8 z", round(5.5 / sqrt(15), 3), 1.420); eq("T8", sf(1 - P(5.5 / sqrt(15))), 0.0778)
z = inv(.85); eq("T9 z", round(z, 4), 1.0364); s = 8 / z; eq("T9 s", sf(s), 7.72); eq("T9 z2", round(-7 / 7.72, 3), -0.907); eq("T9 p", sf(P(-7 / s)), 0.182)
# quiz
eq("Q1", sqrt(16), 4); eq("Q2", round(1 - 0.9332, 4), 0.0668); eq("Q3", round(inv(.2), 4), -0.8416)
# ---- v2 additions (P13) ----
from math import log
def b(n, p, r): return comb(n, r) * p ** r * (1 - p) ** (n - r)
# warm-up
eq("w1 mean", (2 + 4 + 6) / 3, 4); eq("w1 sq", 4 + 16 + 36, 56); eq("w1 var", 56 / 3 - 16, 2.6667, 1e-4); eq("w1 sd", sf(sqrt(56 / 3 - 16)), 1.63)
eq("w2", 10 * .3, 3); eq("w2 v", 10 * .3 * .7, 2.1); eq("w3 b", (13 - 7) / 2, 3); eq("w3 a", 7 - 2 * 3, 1)
# proofs
eq("proof phi", r4(P(-1)), 0.1587); eq("proof phi2", r4(1 - P(1)), 0.1587)
for z_ in (0.3, 1.7, 2.2): eq("proof sym", P(-z_), 1 - P(z_), 1e-12)
xs = [3.0, 5.5, 9.0, 12.0]; mu_, sd_ = sum(xs) / 4, sqrt(sum(x * x for x in xs) / 4 - (sum(xs) / 4) ** 2)
zs = [(x - mu_) / sd_ for x in xs]; eq("proof z mean", sum(zs) / 4, 0, 1e-12); eq("proof z sd", sqrt(sum(z * z for z in zs) / 4), 1, 1e-12)
# continuity correction rationale: normal area over bar vs binomial probability
Yn = NormalDist(20, sqrt(12)); eq("proof cc", Yn.cdf(20.5) - Yn.cdf(19.5), b(50, .4, 20), 3e-3)
# long exam 1: apples
eq("A za", (150 - 160) / 12, -0.8333, 1e-4); eq("A zb", (175 - 160) / 12, 1.25); eq("A P125", r4(P(1.25)), 0.8944); eq("A Pm", r4(P(-10 / 12)), 0.2023)
eq("A a", r4(P(1.25)) - r4(P(-10 / 12)), 0.6921); eq("A a sf", sf(P(1.25) - P(-10 / 12)), 0.692)
eq("A z", round(inv(.8), 4), 0.8416); eq("A m", 160 + inv(.8) * 12, 170.099, 1e-3); eq("A m r", round(160 + 0.8416 * 12, 1), 170.1)
eq("A c", 1 - .8 ** 6 - 6 * .2 * .8 ** 5, 0.34464, 1e-9); eq("A c1", round(.8 ** 6, 4), 0.2621); eq("A c2", round(6 * .2 * .8 ** 5, 4), 0.3932); eq("A c sf", sf(1 - .8 ** 6 - 6 * .2 * .8 ** 5), 0.345)
eq("A c sum", 1 - 0.2621 - 0.3932, 0.3447, 1e-9)
# long exam 2: guessing
eq("B np", 100 * .2, 20); eq("B nq", 100 * .8, 80); eq("B var", 100 * .2 * .8, 16); eq("B z", (24.5 - 20) / 4, 1.125); eq("B b", sf(1 - P(1.125)), 0.130)
eq("B z2", (14.5 - 20) / 4, -1.375); eq("B z3", (25.5 - 20) / 4, 1.375); eq("B P", r4(P(1.375)), 0.9154); eq("B c", 2 * r4(P(1.375)) - 1, 0.8308, 1e-9); eq("B c sf", sf(2 * P(1.375) - 1), 0.831)
exact = sum(b(100, .2, r) for r in range(25, 101)); eq("B exact check", exact, 0.1314, 5e-3)
eq("B exact c", sum(b(100, .2, r) for r in range(15, 26)), 0.8318, 5e-3)
# spot the error
eq("se np", 50 * .4, 20); eq("se npq", 50 * .4 * .6, 12); eq("se wrong z", 4.5 / sqrt(12), 1.299, 1e-3); eq("se wrong", sf(1 - P(4.5 / sqrt(12))), 0.0970)
eq("se z", 3.5 / sqrt(12), 1.010, 1e-3); eq("se right", sf(1 - P(3.5 / sqrt(12))), 0.156); eq("se z rounded", sf(1 - P(1.010)), 0.156)
eq("se exact", sum(b(50, .4, r) for r in range(24, 51)), 0.1573, 5e-3)
# exam practice
eq("E1 z", (120 - 100) / 15, 1.3333, 1e-4); eq("E1 P", r4(P(20 / 15)), 0.9088); eq("E1", sf(1 - P(20 / 15)), 0.0912)
eq("E2 z", (85 - 100) / 15, -1); eq("E2 z2", 10 / 15, 0.6667, 1e-4); eq("E2 P", r4(P(10 / 15)), 0.7475); eq("E2", sf(P(10 / 15) - P(-1)), 0.589)
eq("E3 z", round(inv(.95), 3), 1.645); eq("E3", sf(40 + 1.645 * 6), 49.9)
eq("E4 z", round(inv(.85), 4), 1.0364); eq("E4", sf(10 / inv(.85)), 9.65)
eq("E5 z", round(inv(.95), 4), 1.6449); eq("E5", sf(1.6449 * 10), 16.4)
eq("E6 z1", round(inv(.3), 4), -0.5244); eq("E6 z2", round(inv(.8), 4), 0.8416); eq("E6 sum", 0.8416 + 0.5244, 1.3660, 1e-9)
sg = 30 / (0.8416 + 0.5244); eq("E6 sigma", sf(sg), 22.0); eq("E6 sigma r", round(sg, 2), 21.96); eq("E6 mu", sf(35 + 0.5244 * 21.96), 46.5)
eq("E6 chk", (65 - 46.5) / sg, 0.8416, 5e-3)
eq("E7 np", 60 * .35, 21); eq("E7 npq", 60 * .35 * .65, 13.65); eq("E7 z", (18.5 - 21) / sqrt(13.65), -0.677, 1e-3); eq("E7", sf(P((18.5 - 21) / sqrt(13.65))), 0.249)
eq("E7 nq", 60 * .65, 39)
# E8 loaves
z1, z2 = inv(.04), inv(.92); eq("E8 z1", round(z1, 4), -1.7507); eq("E8 z2", round(z2, 4), 1.4051); eq("E8 sum", 1.7507 + 1.4051, 3.1558)
sg8 = 40 / 3.1558; eq("E8 sigma", sf(sg8), 12.7); eq("E8 sigma r", round(sg8, 3), 12.675); eq("E8 mu", sf(400 + 1.7507 * 12.675), 422)
eq("E8 chk", (440 - 422.19) / 12.675, 1.4051, 2e-3)
eq("E8 n", log(.5) / log(.96), 16.98, 1e-2); eq("E8 min", min(n for n in range(1, 80) if 1 - .96 ** n > .5), 17); eq("E8 16", 1 - .96 ** 16 > .5, 0)
# stretch 1
q = inv(.75); eq("S1 z", round(q, 4), 0.6745); eq("S1 iqr", sf(2 * 0.6745, 4), 1.349); eq("S1 k", 0.6745 + 1.5 * 1.349, 2.698, 1e-3); eq("S1 2.0235", 1.5 * 1.349, 2.0235, 1e-9)
eq("S1 p", 1 - P(2.698), 0.00349, 1e-5); eq("S1 tot", 2 * (1 - P(2.698)), 0.00698, 1e-4)
# stretch 2
za, zb = 4.5 / 7, 5.5 / 7; eq("S2 za", za, 0.6429, 1e-4); eq("S2 zb", zb, 0.7857, 1e-4); eq("S2 p1", r4(P(0.7857)), 0.7840); eq("S2 p2", r4(P(0.6429)), 0.7399)
eq("S2 p", r4(P(0.7857)) - r4(P(0.6429)), 0.0441); eq("S2 n", 400 * 0.0441, 17.64, 1e-9); eq("S2 n2", round(400 * 0.0441, 1), 17.6); eq("S2 exact", 400 * (P(zb) - P(za)), 17.66, 1e-2)
print("ok")
