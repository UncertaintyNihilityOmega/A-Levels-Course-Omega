# checks/chem.mock.p5.py: recomputes every number in Mock paper 5.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, O 16.0.
from math import isclose

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

def fit(x, y):
    n = len(x); mx = sum(x) / n; my = sum(y) / n
    m = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return m, my - m * mx

H, C, O = 1.0, 12.0, 16.0

# Q1
q = 100 * 4.18 * 20.0
eq("q", q, 8360.0, 1e-9)
Mr_EtOH = 2 * C + 6 * H + O
eq("Mr ethanol", Mr_EtOH, 46.0)
n = 0.50 / Mr_EtOH
eq("n ethanol", sf(n, 3), 0.0109)
eq("dcH kJ", sf(q / n / 1000, 3), 769)

# Q2 data
c = [0.100, 0.200, 0.300, 0.400, 0.500, 0.600, 0.700, 0.800, 0.900]
t = [102.5, 49.6, 34.3, 25.0, 27.5, 16.2, 14.6, 12.6, 11.0]
want = [9.76, 20.2, 29.2, 40.0, 36.4, 61.7, 68.5, 79.4, 90.9]
inv = [1000 / x for x in t]
for i, (got, w) in enumerate(zip(inv, want)):
    eq(f"1/t row {i}", sf(got, 3), w, 1e-9)
# line fitted without the anomaly (row 4)
cc = [x for i, x in enumerate(c) if i != 4]
yy = [x for i, x in enumerate(inv) if i != 4]
m, b = fit(cc, yy)
eq("fit y(0.100)", round(b + m * 0.100, 2), 9.77, 0.011)  # stated point 9.80 is within 0.05 of the fit
assert abs((b + m * 0.100) - 9.80) < 0.1
assert abs((b + m * 0.900) - 90.1) < 0.1
grad = (90.1 - 9.80) / (0.900 - 0.100)
eq("gradient", round(grad, 1), 100.4)
eq("gradient 3sf", sf(grad, 3), 100.0, 0.5)
icpt = 9.80 - grad * 0.100
eq("intercept", round(icpt, 2), -0.24)
# anomaly: line value at 0.500 and the time it implies
y_line = b + m * 0.500
assert 49 < y_line < 51
eq("implied time", round(1000 / y_line, 0), 20.0, 0.5)
# doubling check
eq("ratio", round(40.0 / 20.2, 2), 1.98)
# percentage errors
eq("cyl pct", 0.5 / 10.0 * 100, 5.0)
eq("burette pct", 0.10 / 10.00 * 100, 1.0)
# marks
assert 2 + 3 + 4 + 2 + 3 == 14
assert 2 + 2 + 3 + 2 + 1 + 2 + 2 + 2 == 16
assert 14 + 16 == 30
print("ok")
