# checks/phys.mock.p5.py: recomputes every number in the Paper 5 mock and asserts the mark totals.
import itertools, os, re
from math import isclose, sqrt, sin, radians, log10

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, paper says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# ---- Question 2: the generator ------------------------------------------------
# t^2 = 14 s / (5 g sin(theta)); the times were made from g_true = 9.78 m s^-2 plus a small scatter
s = 1.200; ds = 0.005; g_true = 9.78
theta = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0]
scatter = [0.02, -0.02, 0.01, -0.02, 0.01, 0.01]       # added to the true time, in s
dt = 0.05
t_table = [2.01, 1.39, 1.16, 0.98, 0.91, 0.84]          # the times printed in the paper
for a, sc, tp in zip(theta, scatter, t_table):
    t_true = sqrt(14 * s / (5 * g_true * sin(radians(a))))
    eq(f"generator t at {a} deg", round(t_true + sc, 2), tp, 1e-9)
    assert abs(tp - t_true) <= dt          # every point lies within one uncertainty of the true line

# (b) table
x_tab = [2.0 * 0 + 1 / sin(radians(a)) for a in theta]
y_tab = [t * t for t in t_table]
ey_tab = [2 * t * dt for t in t_table]               # absolute uncertainty in t^2 = t^2 x 2 (dt/t)
for (xs, want) in zip(x_tab, [11.47, 5.76, 3.86, 2.92, 2.37, 2.00]):
    eq("1/sin", round(xs, 2), want, 1e-9)
for (ys, want) in zip(y_tab, [4.04, 1.93, 1.35, 0.96, 0.83, 0.71]):
    eq("t^2", round(ys, 2), want, 1e-9)
for (es, want) in zip(ey_tab, [0.20, 0.14, 0.12, 0.10, 0.09, 0.08]):
    eq("d(t^2)", round(es, 2), want, 1e-9)
for t, e1 in zip(t_table, ey_tab):
    eq("percentage rule: 2 x %dt", (e1 / (t * t)) * 100, 2 * dt / t * 100, 1e-9)

# (c)(iii) least-squares gradient and the steepest / shallowest lines through every error bar
N = len(x_tab)
sx, sy = sum(x_tab), sum(y_tab)
sxx = sum(a * a for a in x_tab); sxy = sum(a * b for a, b in zip(x_tab, y_tab))
m_ls = (N * sxy - sx * sy) / (N * sxx - sx * sx)
c_ls = (sy - m_ls * sx) / N
eq("LS gradient", sf(m_ls), 0.353, 5e-4)
eq("LS intercept", sf(c_ls, 2), -0.034, 5e-4)
pts = []
for a, b, e1 in zip(x_tab, y_tab, ey_tab):
    pts += [(a, b + e1), (a, b - e1)]
lines = []
for p, q in itertools.combinations(pts, 2):
    if abs(p[0] - q[0]) < 1e-9:
        continue
    mm = (q[1] - p[1]) / (q[0] - p[0]); cc = p[1] - mm * p[0]
    if all(b - e1 - 1e-9 <= mm * a + cc <= b + e1 + 1e-9 for a, b, e1 in zip(x_tab, y_tab, ey_tab)):
        lines.append((mm, cc))
assert lines, "no line passes through all the error bars"
m_steep, c_steep = max(lines)
m_shallow, c_shallow = min(lines)
eq("steepest worst line", sf(m_steep), 0.382, 5e-4)
eq("shallowest worst line", sf(m_shallow), 0.325, 5e-4)
assert m_shallow < m_ls < m_steep
# the best-fit line itself passes through (or very near) every bar
for a, b, e1 in zip(x_tab, y_tab, ey_tab):
    assert abs(m_ls * a + c_ls - b) <= e1, "best-fit line misses a bar"
# the read-off points quoted in the answer
eq("LS line at x = 2.0", sf(m_ls * 2.0 + c_ls, 2), 0.67, 5e-3)
eq("LS line at x = 11.0", sf(m_ls * 11.0 + c_ls), 3.85, 5e-3)
m_read = (3.85 - 0.67) / (11.0 - 2.0)
eq("gradient from the read-off points", sf(m_read), 0.353, 5e-4)
eq("steepest at x = 2.0", sf(m_steep * 2.0 + c_steep, 2), 0.62, 5e-3)
eq("steepest at x = 11.0", sf(m_steep * 11.0 + c_steep, 3), 4.06, 5e-3)
eq("steepest gradient from read-off", sf((4.06 - 0.62) / 9.0), 0.382, 5e-4)
eq("shallowest at x = 2.0", sf(m_shallow * 2.0 + c_shallow, 2), 0.76, 5e-3)
eq("shallowest at x = 11.0", sf(m_shallow * 11.0 + c_shallow, 3), 3.69, 5e-3)
eq("shallowest gradient from read-off", sf((3.69 - 0.76) / 9.0), 0.326, 5e-4)
dm = sf(m_steep - m_ls, 2)
eq("delta m", dm, 0.029, 5e-4)
dm_shallow = m_ls - m_shallow
assert 0.02 <= dm <= 0.04 and 0.02 <= dm_shallow <= 0.04      # accepted range for the uncertainty
# accepted ranges quoted in the answer
assert 0.34 <= m_ls <= 0.37
assert 0.37 <= m_steep <= 0.39 and 0.31 <= m_shallow <= 0.34

# (d) g and its uncertainty
m = 0.353                                              # the value used in the answer
g = 14 * s / (5 * m)
eq("(d)(i) g", sf(g, 2), 9.5, 1e-9)
eq("(d)(i) g from the unrounded gradient", sf(14 * s / (5 * m_ls), 2), 9.5, 1e-9)
assert 9.0 <= g <= 9.9
assert 9.0 <= 14 * s / (5 * 0.37) and 14 * s / (5 * 0.34) <= 9.9   # range from the accepted gradients
pm = dm / m * 100
eq("(d)(ii) percentage m", sf(pm, 2), 8.2, 1e-9)
ps = ds / s * 100
eq("(d)(ii) percentage s", sf(ps, 2), 0.42, 1e-9)
pg = pm + ps
eq("(d)(ii) percentage g", sf(pg, 2), 8.6, 1e-9)
eq("(d)(ii) percentage g, unrounded gradients", sf((m_steep - m_ls) / m_ls * 100 + ps, 2), 8.7, 1e-9)
eq("(d)(ii) absolute dg", sf(g * pg / 100, 1), 0.8, 1e-9)
assert 6 <= pg <= 12
assert 6 <= (0.02 / m * 100 + ps) and (0.04 / m * 100 + ps) <= 12.5    # range from the accepted uncertainties
assert abs(g_true - g) <= g * pg / 100 + 0.3               # the result is consistent with the generating value

# (e) prediction at 12.0 degrees
sin12 = sin(radians(12.0))
eq("(e) sin 12", sf(sin12, 4), 0.2079, 5e-5)
t2 = m / sin12
eq("(e) t^2", sf(t2, 3), 1.70, 5e-3)
t_pred = sqrt(t2)
eq("(e) t", sf(t_pred, 3), 1.30, 5e-3)
pt = pm / 2
eq("(e) percentage in t", sf(pt, 2), 4.1, 1e-9)
eq("(e) absolute dt", sf(t_pred * pt / 100, 1), 0.05, 1e-9)
assert 1.27 <= t_pred <= 1.34
assert 1.27 <= sqrt(0.34 / sin12) and sqrt(0.37 / sin12) <= 1.34     # accepted t from the accepted gradients
t_true12 = sqrt(14 * s / (5 * g_true * sin12))
assert abs(t_true12 - t_pred) <= t_pred * pt / 100 + 0.02

# figure: ramp (the picture is schematic, but the numbers must be self-consistent)
from math import atan2, degrees, hypot
ux, uy = 280, 100
L = hypot(ux, uy)
eq("ramp fig: surface direction x", ux / L, 0.9418, 1e-3)
eq("ramp fig: surface direction y", uy / L, 0.3364, 1e-3)
eq("ramp fig: arc end x", 320 - 40 * ux / L, 282.3, 0.1)
eq("ramp fig: arc end y", 170 - 40 * uy / L, 156.5, 0.1)
eq("ramp fig: ball centre x", 85 + 9 * uy / L, 88.0, 0.1)
eq("ramp fig: ball centre y", 70 + 45 * uy / ux - 9 * ux / L, 77.6, 0.1)

# ---- Question 1: the mark scheme has the right number of marks in each section -----
here = os.path.dirname(os.path.abspath(__file__))
text = open(os.path.join(here, "..", "chapters", "phys.mock.p5.md"), encoding="utf-8").read()
q1 = text.split(":::try")[1]
q1_answer = q1.split("\nA:")[1]
sections = re.split(r"\n\*\*(.+?)\*\*\n", "\n" + q1_answer.lstrip())
counts = {}
for i in range(1, len(sections), 2):
    counts[sections[i]] = sections[i + 1].count("[B1]")
want_q1 = {"Defining the problem": 3, "Methods of data collection": 6,
           "Method of analysis": 3, "Additional detail, including safety": 3}
assert counts == want_q1, counts
# the log relationship used in the analysis
f_test = [log10(2.0 * L0 ** -1.5) for L0 in (0.08, 0.12, 0.16, 0.20, 0.25)]
grad = (f_test[-1] - f_test[0]) / (log10(0.25) - log10(0.08))
eq("Q1 log-log gradient for f = k L^n with n = -1.5", grad, -1.5, 1e-9)

marks = {1: {"defining the problem": 3, "methods of data collection": 6, "method of analysis": 3, "additional detail": 3},
         2: {"a": 1, "b": 2, "c(i)": 2, "c(ii)": 2, "c(iii)": 2, "d(i)": 2, "d(ii)": 2, "e": 2}}
for q, parts in marks.items():
    assert sum(parts.values()) == 15, f"Q{q} parts sum to {sum(parts.values())}"
assert sum(sum(p.values()) for p in marks.values()) == 30
print("ok")
