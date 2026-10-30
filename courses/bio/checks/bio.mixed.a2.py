# checks/bio.mixed.a2.py: recomputes every number in chapters/bio.mixed.a2.md (A Level mixed practice)
import os, sys, math
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(here), "data"))
from crit import chi2_crit, t_crit, r_crit
n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert math.isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def r2(x, d=2): return round(x + 1e-12, d)


# Section 1
eq("Q1 RQ", r2(18 / 26), 0.69)
eq("Q2 Rf", r2(4.2 / 9.0), 0.47)
chi = (58 - 50) ** 2 / 50 + (42 - 50) ** 2 / 50
eq("Q3 chi", chi, 2.56, 1e-9)
eq("Q3 crit df1", r2(chi2_crit(1)), 3.84); eq("Q3 crit df2", r2(chi2_crit(2)), 5.99); eq("Q3 crit df3", r2(chi2_crit(3)), 7.81)
q = math.sqrt(40 / 25000)
eq("Q4 q2", 40 / 25000, 0.0016); eq("Q4 q", q, 0.04); eq("Q4 2pq", 2 * (1 - q) * q, 0.0768); eq("Q4 carriers", 2 * (1 - q) * q * 25000, 1920, 1e-6)
eq("Q5 Lincoln", 72 * 54 / 18, 216)
ss = (28 / 50) ** 2 + (12 / 50) ** 2 + (6 / 50) ** 2 + (4 / 50) ** 2
eq("Q6 sum", ss, 0.392); eq("Q6 D", r2(1 - ss), 0.61)
eq("Q7 copies", 5 * 2 ** 12, 20480)
eq("Q8 speed", 1.8 / 0.015, 120, 1e-9)
eq("Q9 I relaxed", 2.4 - 1.6, 0.8); eq("Q9 I contracted", 2.0 - 1.6, 0.4)
eq("Q10 length", 36 / 12000 * 1000, 3.0)
# Section 2
eq("D1 day1", 35 / 50, 0.70); eq("D1 day5", 76 / 80, 0.95); eq("D1 pct", (80 - 50) / 50 * 100, 60)
f = lambda x: 15 + 75 * math.exp(-((x - 440) / 30) ** 2) + 85 * math.exp(-((x - 675) / 25) ** 2)
eq("D2 440", round(f(440)), 90); eq("D2 675", round(f(675)), 100); eq("D2 550", round(f(550)), 15)
eq("D3 pct", r2((7.9 - 4.8) / 4.8 * 100, 0), 65)
eq("D4 time ms", 1.2 / 96 * 1000, 12.5)
eq("D5 pct", (80 - 23) / 23 * 100, 247.826087, 1e-5)
eq("D7 pct", (400 - 12) / 400 * 100, 97)
surv = {2: 52, 3: 74, 4: 88, 5: 70, 6: 55, 7: 31}
eq("D6 max", max(surv.values()), 88); eq("D6 argmax", max(surv, key=surv.get), 4)
eq("D8 sum", 800 + 300, 1100)
# Section 4
O = [171, 68, 57, 24]; E = [180, 60, 60, 20]
eq("S1 expected total", sum(E), 320); eq("S1 obs total", sum(O), 320)
c1 = sum((o - e) ** 2 / e for o, e in zip(O, E))
eq("S1 chi", r2(c1), 2.47); eq("S1 crit4", r2(chi2_crit(4)), 9.49)
eq("S1 terms", r2((171 - 180) ** 2 / 180), 0.45); eq("S1 t2", r2(8 ** 2 / 60), 1.07); eq("S1 t3", r2(9 / 60), 0.15); eq("S1 t4", r2(16 / 20), 0.80)
a, b = 4.1 ** 2 / 12, 3.6 ** 2 / 12
t = 4.6 / math.sqrt(a + b)
eq("S2 a", round(a, 3), 1.401); eq("S2 b", round(b, 3), 1.080); eq("S2 t", r2(t), 2.92)
for df, v in [(20, 2.09), (21, 2.08), (22, 2.07), (23, 2.07), (24, 2.06)]:
    eq(f"S2 crit {df}", r2(t_crit(df)), v)
x = [23, 41, 15, 36, 52, 28, 47, 33]; y = [14, 52, 20, 33, 68, 24, 57, 41]
rk = lambda v: [sorted(v, reverse=True).index(a) + 1 for a in v]
rx, ry = rk(x), rk(y)
assert rx == [7, 3, 8, 4, 1, 6, 2, 5] and ry == [8, 3, 7, 5, 1, 6, 2, 4]
D = [a - b for a, b in zip(rx, ry)]
assert D == [-1, 0, 1, -1, 0, 0, 0, 1]
eq("S3 sumD2", sum(d * d for d in D), 4); eq("S3 denom", 8 ** 3 - 8, 504); eq("S3 rs", r2(1 - 6 * 4 / 504), 0.95)
xs = [12, 15, 18, 21, 24, 27, 30, 33]; ys = [3.1, 3.9, 4.0, 5.2, 5.0, 6.3, 6.6, 7.4]
eq("S4 mx", sum(xs) / 8, 22.5); eq("S4 my", sum(ys) / 8, 5.1875)
eq("S4 sxy", sum(p * q_ for p, q_ in zip(xs, ys)), 1009.2, 1e-9)
sx = math.sqrt(sum((p - 22.5) ** 2 for p in xs) / 7); sy = math.sqrt(sum((p - 5.1875) ** 2 for p in ys) / 7)
eq("S4 sx", r2(sx), 7.35); eq("S4 sy", r2(sy), 1.49)
eq("S4 num", 1009.2 - 8 * 22.5 * 5.1875, 75.45); eq("S4 den", 7 * 7.35 * 1.49, 76.6605, 1e-4)
eq("S4 r", r2(75.45 / (7 * 7.35 * 1.49)), 0.98); eq("S4 crit", round(r_crit(8), 3), 0.707)
eq("S5 SE", 2.6 / 5, 0.52); eq("S5 CI lo", r2(18.4 - 1.04, 1), 17.4); eq("S5 CI hi", r2(18.4 + 1.04, 1), 19.4)
eq("S5 B lo", round(16.9 - 0.88, 1), 16.0); eq("S5 B hi", round(16.9 + 0.88, 1), 17.8)
print("ok", n)
