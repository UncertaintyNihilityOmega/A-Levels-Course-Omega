# checks/math.s.regression.py: recomputes every number in the correlation and regression chapter.
from math import isclose, sqrt

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, n=3):
    return float(f"{x:.{n}g}")

def sums(x, y):
    n = len(x)
    return (n, sum(x), sum(y), sum(a * a for a in x), sum(b * b for b in y), sum(a * b for a, b in zip(x, y)))

# Revision data
x = [2, 3, 5, 6, 8, 9, 11, 12]; y = [48, 47, 60, 58, 66, 74, 71, 84]
n, sx, sy, sxx_, syy_, sxy_ = sums(x, y)
eq("sx", sx, 56); eq("sy", sy, 508); eq("sxx", sxx_, 484); eq("syy", syy_, 33406); eq("sxy", sxy_, 3868)
Sxx = sxx_ - sx ** 2 / n; Syy = syy_ - sy ** 2 / n; Sxy = sxy_ - sx * sy / n
eq("Sxx", Sxx, 92); eq("Syy", Syy, 1148); eq("Sxy", Sxy, 312)
r = Sxy / sqrt(Sxx * Syy)
eq("sqrt", sf(sqrt(92 * 1148), 5), 324.99); eq("r", sf(r), 0.960)
b = Sxy / Sxx; a = sy / n - b * sx / n
eq("b", sf(b, 4), 3.391); eq("xbar", sx / n, 7); eq("ybar", sy / n, 63.5); eq("a", round(a, 2), 39.76); eq("a 3sf", sf(a), 39.8); eq("b 3sf", sf(b), 3.39)
eq("pred10", sf(a + b * 10), 73.7); eq("pred20", sf(a + b * 20, 4), 107.6)
eq("pred9", sf(a + b * 9), 70.3); eq("res9", sf(74 - (a + b * 9), 2), 3.7)
eq("res sum", sum(yy - (a + b * xx) for xx, yy in zip(x, y)), 0, 1e-9)
eq("1 hr", sf(b, 2), 3.4)
# Critical values from t values
tcrit = {4: 2.132, 5: 2.015, 6: 1.943, 7: 1.895, 8: 1.860, 9: 1.833, 10: 1.812}
want = {6: 0.7293, 7: 0.6694, 8: 0.6215, 9: 0.5823, 10: 0.5494, 11: 0.5214, 12: 0.4972}
for df, t in tcrit.items():
    eq(f"cv n={df + 2}", round(t / sqrt(t * t + df), 4), want[df + 2], 1e-4)
for df, t, w in [(6, 2.447, 0.7067), (8, 2.306, 0.6319)]:
    eq(f"cv2 n={df + 2}", round(t / sqrt(t * t + df), 4), w, 1e-4)
# Gas example
x2 = [2, 5, 8, 10, 13, 15, 18, 20, 23, 26]; y2 = [88, 76, 74, 63, 60, 50, 49, 38, 36, 28]
n, sx, sy, sxx_, syy_, sxy_ = sums(x2, y2)
eq("g sx", sx, 140); eq("g sy", sy, 562); eq("g sxx", sxx_, 2516); eq("g syy", syy_, 34990); eq("g sxy", sxy_, 6506)
Sxx = sxx_ - sx ** 2 / n; Syy = syy_ - sy ** 2 / n; Sxy = sxy_ - sx * sy / n
eq("g Sxx", Sxx, 556); eq("g Syy", Syy, 3405.6); eq("g Sxy", Sxy, -1362)
r = Sxy / sqrt(Sxx * Syy); eq("g r", sf(r), -0.990)
b = Sxy / Sxx; a = sy / n - b * sx / n
eq("g b", sf(b), -2.45); eq("g b4", round(b, 4), -2.4496); eq("g a", sf(a), 90.5); eq("g a2", round(a, 3), 90.495)
eq("g 12", sf(a + b * 12), 61.1); eq("g 30", sf(a + b * 30), 17.0); eq("g ybar", sy / n, 56.2)
assert abs(r) > 0.6319 and min(x2) == 2 and max(x2) == 26
# Try
eq("t2 r", -54 / sqrt(40 * 90), -0.9); eq("t2 b", -54 / 40, -1.35)
eq("t3 Sxx", 200 - 30 ** 2 / 6, 50); eq("t3 Syy", 330 - 42 ** 2 / 6, 36); eq("t3 Sxy", 250 - 30 * 42 / 6, 40)
eq("t3 r", sf(40 / sqrt(1800)), 0.943); eq("t3 b", 40 / 50, 0.8); eq("t3 a", 7 - 0.8 * 5, 3)
eq("t4a", 2.7 * 100, 270); eq("t4b", 12.4 * 100, 1240)
eq("t5 6", 12.4 + 2.7 * 6, 28.6); eq("t5 14", sf(12.4 + 2.7 * 14, 3), 50.2); eq("t5 6 money", 28.6 * 100, 2860); eq("t5 14 money", 50.2 * 100, 5020)
xs = [-2, -1, 0, 1, 2]; ys = [4, 1, 0, 1, 4]
eq("t6 sx", sum(xs), 0); eq("t6 sxy", sum(a_ * b_ for a_, b_ in zip(xs, ys)), 0); eq("t6 terms", -8 - 1 + 0 + 1 + 8, 0)
assert 0.71 > 0.5823 and not (-0.45 < -0.4972)
eq("t10 Sxy", 1300 - 90 * 120 / 10, 220); eq("t10 Sxx", 1000 - 90 ** 2 / 10, 190); eq("t10 b", sf(220 / 190, 4), 1.158)
eq("t10 a", sf(12 - (220 / 190) * 9, 3), 1.58); eq("t10 b3", sf(220 / 190, 3), 1.16)
print("ok")
