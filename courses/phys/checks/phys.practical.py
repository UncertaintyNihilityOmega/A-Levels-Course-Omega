# checks/phys.practical.py: recomputes every number in the Practical skills chapter.
from math import isclose, sqrt, pi, ceil

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def pct(dx, x):
    return dx / x * 100

def pdiff(a, b):
    return abs(a - b) / ((a + b) / 2) * 100

# Warm-up
eq("warm pct", sf(pct(0.05, 2.40), 2), 2.1)
eq("warm gradient", (14.0 - 2.0) / 6.0, 2.0)
eq("warm R", 4.8 / 0.32, 15)

# Paper 3 marks
eq("Q1 marks", 7 + 6 + 4 + 3, 20)
eq("Q2 marks", 5 + 2 + 10 + 3, 20)
eq("paper", 20 + 20, 40)

# Micrometer: one turn 0.5 mm over 50 divisions
eq("thimble division", 0.5 / 50, 0.01)
eq("micro reading", 5.5 + 28 * 0.01, 5.78)
eq("micro corrected", sf(5.78 - 0.03, 3), 5.75)
# micrometer figure geometry: 40 px/mm, edge at 5.78 mm, half-mm line at 5.5 mm visible
mm, X0 = 40, 50
edge = X0 + mm * 5.78
eq("edge px", edge, 281.2, 1e-6)
assert X0 + mm * 5.5 < edge - 8, "5.5 mm line must be visible left of the thimble edge"
assert X0 + mm * 6.0 > edge, "6 mm line is hidden under the thimble"
eq("5.5 px", X0 + mm * 5.5, 270)
# thimble: 7 px per division, line 28 on datum y = 84, d=20..36 drawn from y=28 to y=140
eq("thimble top", 84 + (20 - 28) * 7, 28)
eq("thimble bottom", 84 + (36 - 28) * 7, 140)
eq("thimble 25", 84 + (25 - 28) * 7, 63)
eq("thimble 30", 84 + (30 - 28) * 7, 98)
eq("thimble 35", 84 + (35 - 28) * 7, 133)

# Vernier: ten divisions span 9 mm; zero at 23.4 mm
z = 23.4
aligned = [k for k in range(11) if abs((z + 0.9 * k) - round(z + 0.9 * k)) < 1e-9]
assert aligned == [4], aligned
eq("vernier 4th", z + 0.9 * 4, 27.0, 1e-9)
for k in range(11):
    if k != 4:
        off = abs((z + 0.9 * k) - round(z + 0.9 * k))
        assert off >= 0.09, (k, off)
eq("vernier reading", 23 + 4 * 0.1, 23.4)
eq("vernier corrected", 23.4 - 0.2, 23.2, 1e-9)
# vernier figure px: 28 px/mm from X0 = 40; zero at 135.2, 4th at 236 = 27 mm line
eq("vernier zero px", 40 + 28 * (z - 20), 135.2, 1e-9)
eq("vernier 4th px", 40 + 28 * (z - 20 + 0.9 * 4), 236, 1e-9)
eq("27 mm px", 40 + 28 * 7, 236)

# Timing eg
tm = (31.6 + 31.2) / 2
eq("mean 20", tm, 31.4, 1e-9)
T = tm / 20
eq("T", T, 1.57, 1e-9)
eq("half range", (31.6 - 31.2) / 2, 0.2, 1e-9)
eq("dT", 0.2 / 20, 0.01)
eq("pct T", sf(pct(0.01, 1.57), 2), 0.64)
eq("pct one swing", sf(pct(0.2, 1.57), 2), 13)

# Table section: pendulum data (shared with the walk-through)
l = [0.300, 0.400, 0.500, 0.600, 0.700, 0.800]
t1 = [22.06, 25.31, 28.45, 31.02, 33.50, 36.01]
t2 = [21.94, 25.45, 28.27, 31.22, 33.66, 35.87]
mean = [(a + b) / 2 for a, b in zip(t1, t2)]
Ts = [m / 20 for m in mean]
T2 = [x * x for x in Ts]
for i, (want_m, want_T, want_T2) in enumerate(zip(
        [22.00, 25.38, 28.36, 31.12, 33.58, 35.94],
        [1.100, 1.269, 1.418, 1.556, 1.679, 1.797],
        [1.210, 1.610, 2.011, 2.421, 2.819, 3.229])):
    eq(f"mean {i}", round(mean[i], 2), want_m, 1e-9)
    eq(f"T {i}", sf(Ts[i], 4), want_T, 1e-9)
    eq(f"T2 {i}", sf(T2[i], 4), want_T2, 1e-9)
    # no rounding-edge ambiguity: the digit after the 4th s.f. must not be near 5
    assert abs(((Ts[i] * 1000) % 1) - 0.5) > 0.05, ("T rounding edge", i, Ts[i])
    assert abs(((T2[i] * 1000) % 1) - 0.5) > 0.05, ("T2 rounding edge", i, T2[i])
# half-range of each pair (the readings agree to about 0.1 s)
assert all(abs(a - b) / 2 < 0.11 for a, b in zip(t1, t2))
# faulty table checks: row 1 and 2 values
eq("faulty T row3", sf(((28.45 + 28.27) / 2) / 20, 4), 1.418)
eq("faulty T2 sf", sf(T2[0], 2), 1.2)
eq("faulty T2 sf2", sf(T2[1], 2), 1.6)
eq("faulty T2 sf3", sf(T2[2], 2), 2.0)

# Scale example
eq("l range", sf(0.78 - 0.32, 2), 0.46)
eq("l 0.1 fills", sf(0.46 / 1.0 * 100, 2), 46)
eq("l 0.05 span", 10 * 0.05, 0.50, 1e-12)
eq("l 0.05 fills", sf(0.46 / 0.50 * 100, 2), 92)
eq("T2 range", 3.15 - 1.30, 1.85, 1e-12)
eq("T2 0.1 span", 14 * 0.1, 1.4, 1e-12)
eq("T2 0.5 span", 14 * 0.5, 7.0)
eq("T2 0.5 fills", sf(1.85 / 7.0 * 100, 2), 26)
eq("T2 0.2 span", 14 * 0.2, 2.8, 1e-12)
eq("T2 0.2 fills", sf(1.85 / 2.8 * 100, 2), 66)
assert 1.2 + 14 * 0.2 >= 3.15 and 0.30 + 10 * 0.05 >= 0.78 - 1e-12
# physical consistency of the quoted data: T^2 = (4 pi^2/g) l
assert abs(4 * pi**2 / 9.81 * 0.32 - 1.30) < 0.02 and abs(4 * pi**2 / 9.81 * 0.78 - 3.15) < 0.05

# Spring graph
F = [1, 2, 3, 4, 5, 6]
L = [13.3, 14.2, 14.8, 16.5, 16.6, 17.2]
line = lambda f: 12.5 + 0.8 * f
res = [round(a - line(f), 10) for f, a in zip(F, L)]
assert abs(res[3]) > 0.5 and all(abs(r) <= 0.1 + 1e-9 for i, r in enumerate(res) if i != 3), res
eq("balanced residuals", sum(r for i, r in enumerate(res) if i != 3), 0.0, 1e-9)
eq("line at 1", line(1.0), 13.3)
eq("line at 6", line(6.0), 17.3)
grad = (17.3 - 13.3) / (6.0 - 1.0)
eq("gradient", grad, 0.80)
eq("intercept", 13.3 - 0.80 * 1.0, 12.5, 1e-12)
eq("k per cm", 1 / 0.80, 1.25)
eq("k per m", 1.25 * 100, 125)
assert 6.0 - 1.0 > 0.5 * (6.4 - 0.7), "triangle spans more than half the drawn line"
# spring figure geometry: 68 px/N, 64 px/cm, origin (70, 340) at l = 13.0
X = lambda f: 70 + 68 * f
Y = lambda v: 340 - 64 * (v - 13.0)
eq("fig X1", X(1), 138); eq("fig Y 13.3", round(Y(13.3), 1), 320.8)
eq("fig X6", X(6), 478); eq("fig Y 17.3", round(Y(17.3), 1), 64.8)
eq("fig anomalous y", round(Y(16.5), 1), 116.0)
eq("fig line start", round(Y(line(0.7)), 1), 336.2); eq("fig line end", round(Y(line(6.4)), 1), 44.3)
eq("fig line start x", X(0.7), 117.6, 1e-9); eq("fig line end x", X(6.4), 505.2, 1e-9)
assert Y(13.0) - Y(18.0) == 320
# spot the error
eq("spot gradient", (16.5 - 14.8) / (4.0 - 3.0), 1.7)
eq("spot k", sf(1 / 1.7, 2), 0.59)

# Uncertainty eg: g from the pendulum
g = 4 * pi**2 * 0.610 / 1.57**2
eq("g", round(g, 3), 9.770)
pl, pt = pct(0.001, 0.610), pct(0.01, 1.57)
eq("pct l", sf(pl, 2), 0.16)
eq("pct T", sf(pt, 2), 0.64)
tot = pl + 2 * pt
eq("pct g", sf(tot, 2), 1.4)
eq("dg", sf(0.014 * 9.770, 2), 0.14)
eq("dg exact", sf(tot / 100 * g, 1), 0.1)
eq("g 2 sf", sf(g, 2), 9.8)
eq("T share", sf(2 * pt, 2), 1.3)

# Testing a relationship
R1, R2 = 1.0 / 0.205, 4.0 / 0.790
eq("R1", sf(R1, 3), 4.88); eq("R2", sf(R2, 3), 5.06)
eq("R mean", round((R1 + R2) / 2, 3), 4.971)
eq("R diff", round(R2 - R1, 3), 0.185)
eq("R pdiff", sf(pdiff(R1, R2), 2), 3.7)
L1, L2 = 1.0 / 0.100, 6.0 / 0.250
eq("lamp R1", L1, 10); eq("lamp R2", L2, 24)
eq("lamp pdiff", sf(pdiff(L1, L2), 2), 82)
eq("pendulum intercept", round(1.21 - 4.04 * 0.300, 3), -0.002)

# Question 2 evaluation
tb = (0.52 + 0.58 + 0.55) / 3
eq("mean fall", sf(tb, 2), 0.55)
eq("half range fall", (0.58 - 0.52) / 2, 0.03, 1e-12)
g2 = 2 * 1.500 / 0.55**2
eq("g2", sf(g2, 2), 9.9)
eq("pct h", sf(pct(0.002, 1.500), 2), 0.13)
eq("pct t", sf(pct(0.03, 0.55), 2), 5.5)
tot2 = pct(0.002, 1.500) + 2 * pct(0.03, 0.55)
eq("pct g2", sf(tot2, 2), 11)
eq("dg2", sf(tot2 / 100 * g2, 2), 1.1)

# Walk-through: gradient and g
eq("walk gradient", (3.23 - 1.21) / (0.800 - 0.300), 4.04, 1e-9)
eq("walk g", sf(4 * pi**2 / 4.04, 3), 9.77)
# least-squares line agrees with the two read points to 0.01
mx, my = sum(l) / 6, sum(T2) / 6
sl = sum((x - mx) * (y - my) for x, y in zip(l, T2)) / sum((x - mx) ** 2 for x in l)
ic = my - sl * mx
assert abs(sl - 4.04) < 0.01, sl
eq("line at 0.300", round(ic + sl * 0.300, 2), 1.21, 1e-9)
eq("line at 0.800", round(ic + sl * 0.800, 2), 3.23, 1e-9)
assert abs(ic) < 0.01
# scatter of T^2 about the line is about 0.01 s^2 or less
assert max(abs(y - (ic + sl * x)) for x, y in zip(l, T2)) < 0.012

# Start easy
eq("easy pct rule", sf(pct(0.001, 0.500), 1), 0.2)
eq("easy neg zero", round(0.87 - (-0.04), 2), 0.91)
eq("easy vernier", 41 + 7 * 0.1, 41.7, 1e-9)
eq("easy R", sf(2.4 / 0.153, 3), 15.7)
eq("easy R 2sf", sf(2.4 / 0.153, 2), 16)
eq("easy scale", 7.3 / 10 * 100, 73, 1e-9)
eq("easy T", 14.8 / 10, 1.48); eq("easy dT", 0.2 / 10, 0.02)
eq("easy pct T", sf(pct(0.2, 14.8), 2), 1.4)
eq("easy pdiff", sf(pdiff(2.5, 2.7), 2), 7.7)

# Exam practice
eq("ex2 R", sf(4.5 / 0.0312, 4), 144.2)
eq("ex2 R 2sf", sf(4.5 / 0.0312, 2), 140)
eq("ex2 R 3sf", sf(4.5 / 0.0312, 3), 144)
eq("ex3 span", 14 * 0.2, 2.8, 1e-12)
eq("ex3 fill", sf((2.85 - 0.45) / 2.8 * 100, 2), 86)
assert 0.2 + 2.8 >= 2.85 and 0.4 + 2.8 >= 2.85
eq("ex4 gradient", (52.0 - 28.0) / (10.0 - 2.0), 3.0)
eq("ex4 intercept", 28.0 - 3.0 * 2.0, 22.0)
eq("ex5 T", sf(27.4 / 20, 3), 1.37)
eq("ex5 dT", 0.2 / 20, 0.01)
eq("ex5 pct", sf(pct(0.2, 27.4), 2), 0.73)
k1, k2 = 1.0 / 0.0210, 4.0 / 0.0900
eq("ex6 k1", sf(k1, 3), 47.6); eq("ex6 k2", sf(k2, 3), 44.4)
eq("ex6 pdiff", sf(pdiff(k1, k2), 2), 6.9)
assert pdiff(k1, k2) > 5
eq("ex8 t2", sf(3.20**2, 4), 10.24)
eq("ex8 t2 3sf", sf(3.20**2, 3), 10.2)
eq("ex8 gradient", round((3.10 - 0.62) / (10.00 - 2.00), 3), 0.310)
eq("ex8 a", sf(2 * 0.310, 2), 0.62)
eq("ex8 intercept", round(0.62 - 0.310 * 2.00, 3), 0.0, 1e-12)

# Stretch
Rs = [4.86, 4.92, 4.98, 5.04, 5.10]
eq("st1 pdiff", sf(pdiff(Rs[0], Rs[-1]), 2), 4.8)
for a, b in zip(Rs, Rs[1:]):
    eq("st1 step", round(b - a, 10), 0.06, 1e-9)
eq("st1 gradient", (5.10 - 4.86) / (5.0 - 1.0), 0.06, 1e-12)
eq("st2 a", sf(pct(0.2, 1.57), 3), 12.7)
Nmin = 0.2 / (1.57 * 0.0030)
eq("st2 N", ceil(Nmin), 43)
assert 0.2 / (43 * 1.57) * 100 < 0.30 < 0.2 / (42 * 1.57) * 100
eq("st2 Nmin", sf(Nmin, 3), 42.5)
eq("st2 factor", pct(0.2, 1.57) / pct(0.2, 20 * 1.57), 20, 1e-9)

# Quiz
eq("quiz micro", round(3.45 - 0.02, 2), 3.43)
eq("quiz pdiff", sf(pdiff(10.0, 10.5), 2), 4.9)
eq("quiz pdiff den", 0.5 / 10.25 * 100, 4.878, 1e-3)


# Review additions: tangent example and the 0.06 m scale in "Choosing scales"
eq("tangent gradient", (14.0 - 2.0) / (7.0 - 1.0), 2.0)
eq("tangent span", 7.0 - 1.0, 6.0)
eq("scale 0.06 covers", round(10 * 0.06, 2), 0.60)
assert 10 * 0.06 >= 0.78 - 0.32
print("ok")
