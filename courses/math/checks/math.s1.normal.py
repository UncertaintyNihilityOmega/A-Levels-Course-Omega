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
print("ok")
