# checks/phys.planning.py: recomputes every number in the Planning, analysis and evaluation chapter.
import itertools
from math import isclose, sqrt, pi, log, log10, exp, sin, ceil

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def lsq(x, y):
    m_ = len(x); mx = sum(x) / m_; my = sum(y) / m_
    m = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return m, my - m * mx

def extremes(x, y, dy):
    """steepest and shallowest straight lines that pass through every error bar (vertices of the feasible region)"""
    cons = []
    for i in range(len(x)):
        cons.append((x[i], y[i] - dy[i])); cons.append((x[i], y[i] + dy[i]))
    pts = []
    for a, b in itertools.combinations(cons, 2):
        if a[0] == b[0]: continue
        m = (b[1] - a[1]) / (b[0] - a[0]); c = a[1] - m * a[0]
        if all(y[i] - dy[i] - 1e-9 <= c + m * x[i] <= y[i] + dy[i] + 1e-9 for i in range(len(x))): pts.append((m, c))
    return min(pts), max(pts)

# Warm-up
eq("warm gradient", (9.1 - 3.5) / (10.0 - 2.0), 0.70)
eq("warm lg", round(log10(76.5), 3), 1.884)

# Oscilloscope example: Y-gain 2.0 V/div, time-base 5.0 ms/div, amplitude 3.0 div, crests 4.0 div apart
eq("Vpeak", 3.0 * 2.0, 6.0); eq("Vpp", 6.0 * 2.0, 12)
eq("T", 4.0 * 5.0, 20); eq("f", 1 / 0.020, 50); eq("Ipeak", 6.0 / 120, 0.050)
# figure geometry: 40 px per division, centre line y = 180, crests at 100 and 260 px
eq("amp px", 180 - 3 * 40, 60)
eq("crest 1", 40 + 0.5 * 40 + 160 / 4, 100)
eq("crest spacing", 160 / 40, 4.0)
eq("sine crest y", round(180 - 120 * sin(2 * pi * (100 - 60) / 160)), 60)

# Light gates
eq("v1", 0.050 / 0.040, 1.25); eq("v2", 0.050 / 0.025, 2.00)
eq("a", (2.00 - 1.25) / 0.60, 1.25)

# Linearising
eq("g from gradient", sf(4 * pi**2 / 4.03, 3), 9.80)
eq("k lamp", sf(10**2.02, 3), 105)
mu = 1 / (4 * 0.600**2 * 12.5**2)
eq("mu", sf(mu, 3), 4.44e-3, 1e-9)
eq("lg e", round(log10(exp(1)), 3), 0.434)

# Log table
eq("lg 76.5", round(log10(76.5), 3), 1.884)
eq("lg 61.0", round(log10(61.0), 3), 1.785)
eq("lg 45.5", round(log10(45.5), 3), 1.658)
eq("lg 5.8", round(log10(5.8), 2), 0.76)
eq("lg 6.0 4dp", round(log10(6.0), 4), 0.7782)
eq("lg 5.8 4dp", round(log10(5.8), 4), 0.7634)
eq("dlg d", round(log10(6.0) - log10(5.8), 4), 0.0147)
eq("dlg d 1sf", sf(log10(6.0) - log10(5.8), 1), 0.01)
# spot the error gradient
eq("spot gradient", (1.40 - 0.40) / (0.60 - 0.10), 2.0)
# gradient uncertainty example
eq("dm", round(2.61 - 2.48, 2), 0.13)
eq("pct m", sf(0.13 / 2.48 * 100, 2), 5.2)

# Question 2: capacitor discharge
t = [10, 20, 30, 40, 50, 60]
V = [8.0, 5.4, 3.6, 2.4, 1.6, 1.1]
y = [log(v) for v in V]
dy = [log(v + 0.1) - log(v) for v in V]
for i, (a, b) in enumerate(zip([2.079, 1.686, 1.281, 0.875, 0.470, 0.095], [0.012, 0.018, 0.027, 0.041, 0.061, 0.087])):
    eq(f"ln V {i}", round(y[i], 3), a, 1e-9)
    eq(f"dln V {i}", round(dy[i], 3), b, 1e-9)
    assert abs((y[i] * 1000 % 1) - 0.5) > 0.03 and abs((dy[i] * 1000 % 1) - 0.5) > 0.03, ("rounding edge", i)
mb, cb = lsq(t, y)
(mw, cw), (ms, cs) = extremes(t, y, dy)
assert mw < mb < ms          # steepest line has the more negative gradient
# the quoted read-off points lie on the lines (to the 2 d.p. read)
line = lambda m, c, x: c + m * x
eq("best y(10)", round(line(mb, cb, 10), 2), 2.08)
eq("best y(60)", round(line(mb, cb, 60), 2), 0.08)
eq("worst y(10)", round(line(mw, cw, 10), 2), 2.09)
eq("worst y(60)", round(line(mw, cw, 60), 2), 0.01)
eq("best intercept", round(cb, 2), 2.48)
eq("worst intercept", round(cw, 2), 2.51)
# the worst line passes through every bar; the best-fit line does too
for i in range(6):
    assert y[i] - dy[i] - 1e-9 <= line(mw, cw, t[i]) <= y[i] + dy[i] + 1e-9
    assert y[i] - dy[i] <= line(mb, cb, t[i]) <= y[i] + dy[i]
mbr = (0.08 - 2.08) / (60 - 10); mwr = (0.01 - 2.09) / (60 - 10)
eq("m best", mbr, -0.0400, 1e-12)
eq("m worst", sf(mwr, 3), -0.0416, 1e-12)
eq("dm", round(abs(mwr) - abs(mbr), 4), 0.0016, 1e-9)
eq("pct dm", sf(0.0016 / 0.0400 * 100, 2), 4.0)
RC = 1 / 0.0400
eq("RC", RC, 25.0)
C = RC / 50e3
eq("C", C, 5.0e-4, 1e-12)
eq("pct R", sf(1 / 50 * 100, 2), 2.0)
eq("pct C", 4.0 + 2.0, 6.0)
eq("dC", sf(0.060 * C, 1), 3e-5, 1e-12)
eq("V0", sf(exp(2.48), 3), 11.9)
eq("dV0", sf(0.03 * 11.9, 1), 0.4)
eq("dlnV0", round(2.51 - 2.48, 2), 0.03)
# the figure's best-fit line passes through (10, 2.08) and (60, 0.08): px coordinates
X = lambda tt: 70 + 6.6 * tt
Y = lambda v: 356 - 96 * (v + 0.5)
eq("fig best start", round(Y(cb), 1), 70.0, 0.2)
eq("fig best end", round(Y(cb + mb * 62), 1), 307.7, 0.2)
eq("fig worst start", round(Y(cw), 1), 67.2, 0.2)
eq("fig worst end", round(Y(cw + mw * 62), 1), 315.2, 0.2)
eq("fig tri A y", round(Y(2.08), 1), 108.3, 0.05)
eq("fig tri B y", round(Y(0.08), 1), 300.3, 0.05)
eq("fig tri B x", X(60), 466)
eq("fig X10", X(10), 136)
assert Y(3.0) == 20 and Y(-0.5) == 356

# Start easy
eq("easy lg 2.5", round(log10(2.5), 2), 0.40)
eq("easy dlg", sf(log10(2.6) - log10(2.5), 2), 0.017, 1e-9)
eq("easy dlg 1sf", sf(log10(2.6) - log10(2.5), 1), 0.02)
eq("easy T", 5.0 * 2.0, 10); eq("easy f", 1 / 0.010, 100)
eq("easy v", 0.050 / 0.020, 2.5)

# Exam practice
eq("ex3 lg 45.5", round(log10(45.5), 3), 1.658)
eq("ex3 lg 6.0", round(log10(6.0), 2), 0.78); eq("ex3 lg 6.0 3dp", round(log10(6.0), 3), 0.778)
eq("ex4 lg", round(log10(5.8), 2), 0.76)
eq("ex4 d", sf(log10(6.0) - log10(5.8), 1), 0.01)
eq("ex5 best", (9.1 - 3.5) / (10.0 - 2.0), 0.70)
eq("ex5 worst", (9.0 - 3.8) / (10.0 - 2.0), 0.65)
eq("ex5 d", round(0.70 - 0.65, 2), 0.05)
eq("ex5 pct", sf(0.05 / 0.70 * 100, 2), 7.1)
g6 = 4 * pi**2 / 4.02
eq("ex6 g", sf(g6, 3), 9.82)
eq("ex6 pct", sf(0.12 / 4.02 * 100, 2), 3.0)
eq("ex6 dg", sf(0.030 * g6, 1), 0.3)
# Q8 lamp
Vl = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
Il = [105, 158, 198, 238, 268, 297]
xl = [log10(v) for v in Vl]; yl = [log10(i) for i in Il]; dl = [log10(i + 3) - log10(i) for i in Il]
for i, (a, b, c) in enumerate(zip([0.000, 0.301, 0.477, 0.602, 0.699, 0.778], [2.021, 2.199, 2.297, 2.377, 2.428, 2.473], [0.012, 0.008, 0.007, 0.005, 0.005, 0.004])):
    eq(f"lamp lgV {i}", round(xl[i], 3), a, 1e-9)
    eq(f"lamp lgI {i}", round(yl[i], 3), b, 1e-9)
    eq(f"lamp dlgI {i}", round(dl[i], 3), c, 1e-9)
    assert abs((xl[i] * 1000 % 1) - 0.5) > 0.01 and abs((yl[i] * 1000 % 1) - 0.5) > 0.03 and abs((dl[i] * 1000 % 1) - 0.5) > 0.03, ("lamp rounding edge", i)
mlb, clb = lsq(xl, yl)
(mlw, clw), (mls, cls_) = extremes(xl, yl, dl)
eq("lamp best y(0.1)", round(line(mlb, clb, 0.100), 3), 2.080)
eq("lamp best y(0.7)", round(line(mlb, clb, 0.700), 3), 2.429)
assert mls > mlb  # the steeper line (positive gradient, larger) is the worst
eq("lamp worst y(0.1)", round(line(mls, cls_, 0.100), 3), 2.070)
eq("lamp worst y(0.7)", round(line(mls, cls_, 0.700), 3), 2.430)
for i in range(6):
    assert yl[i] - dl[i] - 1e-9 <= line(mls, cls_, xl[i]) <= yl[i] + dl[i] + 1e-9
    assert yl[i] - dl[i] <= line(mlb, clb, xl[i]) <= yl[i] + dl[i]
gb = (2.429 - 2.080) / (0.700 - 0.100); gw = (2.430 - 2.070) / (0.700 - 0.100)
eq("lamp gb", round(gb, 3), 0.582)
eq("lamp gw", round(gw, 3), 0.600)
eq("lamp dn", sf(gw - gb, 1), 0.02)
eq("lamp n", sf(gb, 2), 0.58)
cb_l = 2.080 - gb * 0.100
eq("lamp c", round(cb_l, 3), 2.022)
eq("lamp k", sf(10**cb_l, 3), 105)

# Stretch 1: cell with false origin
eq("st1 r", -(1.02 - 1.34) / (0.60 - 0.20), 0.80, 1e-12)
eq("st1 E", 1.34 + 0.80 * 0.20, 1.50, 1e-12)
eq("st1 worst r", -(0.98 - 1.36) / (0.60 - 0.20), 0.95, 1e-12)
eq("st1 dr", round(0.95 - 0.80, 2), 0.15)
eq("st1 worst E", 1.36 + 0.95 * 0.20, 1.55, 1e-12)
eq("st1 dE", round(1.55 - 1.50, 2), 0.05)
# Stretch 2: distinguishing exponents
e = log10(1.10)
eq("st2 e", sf(e, 2), 0.041)
eq("st2 lgx", sf(2 * e / 0.25, 3), 0.331)
eq("st2 ratio", sf(10**(2 * e / 0.25), 3), 2.14)
eq("st2 dm at factor 10", sf(2 * e / 1.0, 2), 0.083 if False else 0.083, 1e-9)

# Quiz
eq("quiz RC", 1 / 0.040, 25)
eq("quiz Vpeak", 2.4 * 5.0, 12)
eq("quiz dm", round(2.61 - 2.48, 2), 0.13)

print("ok")
