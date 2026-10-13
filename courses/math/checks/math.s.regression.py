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
tcrit = {4: 2.132, 5: 2.015, 6: 1.943, 7: 1.8946, 8: 1.8595, 9: 1.8331, 10: 1.8125}
want = {6: 0.7293, 7: 0.6694, 8: 0.6215, 9: 0.5822, 10: 0.5494, 11: 0.5214, 12: 0.4973}
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
assert 0.71 > 0.5822 and not (-0.45 < -0.4973)
eq("t10 Sxy", 1300 - 90 * 120 / 10, 220); eq("t10 Sxx", 1000 - 90 ** 2 / 10, 190); eq("t10 b", sf(220 / 190, 4), 1.158)
eq("t10 a", sf(12 - (220 / 190) * 9, 3), 1.58); eq("t10 b3", sf(220 / 190, 3), 1.16)

# ---- P14 additions ----
from math import sqrt as _s
# warm-up
eq("w1", 4 * 2 - 3, 5); eq("w2", 2516 - 140 ** 2 / 10, 556)
# proof check: x = 1,2,3  y = 2,3,7
_x = [1, 2, 3]; _y = [2, 3, 7]
_sxy = sum(a * b for a, b in zip(_x, _y)) - sum(_x) * sum(_y) / 3; _sxx = sum(a * a for a in _x) - sum(_x) ** 2 / 3
eq("p sxy", _sxy, 5); eq("p sxx", _sxx, 2); eq("p b", _sxy / _sxx, 2.5); eq("p a", 4 - 2.5 * 2, -1)
_res = [b - (-1 + 2.5 * a) for a, b in zip(_x, _y)]; assert _res == [0.5, -1.0, 0.5] and sum(_res) == 0
# brute-force check that (a, b) minimise the squared residuals
_ss = lambda a, b: sum((yy - a - b * xx) ** 2 for xx, yy in zip(_x, _y))
assert all(_ss(-1, 2.5) <= _ss(-1 + da, 2.5 + db) for da in (-.1, 0, .1) for db in (-.1, 0, .1))
# spot the error
eq("sp sxx", 55 - 15 ** 2 / 5, 10); eq("sp syy", 340 - 40 ** 2 / 5, 20); eq("sp sxy", 118 - 15 * 40 / 5, -2)
eq("sp wrong b", -2 / 20, -0.1); eq("sp wrong a", 8 + 0.1 * 3, 8.3); eq("sp b", -2 / 10, -0.2); eq("sp a", 8 + 0.2 * 3, 8.6)
eq("sp check", 8.6 - 0.2 * 3, 8); eq("sp prod", (-0.2) * (-0.1), 0.02); eq("sp r2", 4 / 200, 0.02)
# exam practice
X = [1, 2, 3, 4, 5, 6]; Y = [5, 7, 6, 9, 10, 12]
eq("e2 sx", sum(X), 21); eq("e2 sy", sum(Y), 49); eq("e2 sxx", sum(a * a for a in X), 91); eq("e2 syy", sum(a * a for a in Y), 435); eq("e2 sxy", sum(a * b for a, b in zip(X, Y)), 195)
Sxx = 91 - 21 ** 2 / 6; Syy = 435 - 49 ** 2 / 6; Sxy = 195 - 21 * 49 / 6
eq("e2 Sxx", Sxx, 17.5); eq("e2 Syy", round(Syy, 2), 34.83); eq("e2 Sxy", Sxy, 23.5); eq("e2 r", sf(Sxy / _s(Sxx * Syy)), 0.952)
b = Sxy / Sxx; a = 49 / 6 - b * 3.5
eq("e3 b", round(b, 3), 1.343); eq("e3 ybar", round(49 / 6, 3), 8.167); eq("e3 a", round(a, 3), 3.467)
eq("e3 p", sf(a + b * 4.5), 9.51); eq("e3 p2", sf(a + b * 10), 16.9)
assert 0.58 < 0.6319
eq("e5 40", 2.4 + 1.15 * 40, 48.4)
eq("e6 r", sf(-72 / _s(48 * 130)), -0.911); eq("e6 b", -72 / 48, -1.5); eq("e6 a", 40 + 1.5 * 6, 49)
# e7
eq("e7 b", round(3.391 / 60, 4), 0.0565); eq("e7 a", sf(39.76 + 5, 3), 44.8)
_sx, _sy, _sxx2, _syy2, _sxy2 = 56 + 10, 508 + 20, 484 + 100, 33406 + 400, 3868 + 200
eq("e7 sx", _sx, 66); eq("e7 sy", _sy, 528); eq("e7 sxx", _sxx2, 584); eq("e7 syy", _syy2, 33806); eq("e7 sxy", _sxy2, 4068)
Sxx9 = _sxx2 - _sx ** 2 / 9; Syy9 = _syy2 - _sy ** 2 / 9; Sxy9 = _sxy2 - _sx * _sy / 9
eq("e7 Sxx", Sxx9, 100); eq("e7 Syy", Syy9, 2830); eq("e7 Sxy", Sxy9, 196); eq("e7 r", sf(Sxy9 / _s(Sxx9 * Syy9)), 0.368)
# s1: revision data
_rx = [2, 3, 5, 6, 8, 9, 11, 12]; _ry = [48, 47, 60, 58, 66, 74, 71, 84]
eq("s1 b", sf(312 / 92, 4), 3.391); eq("s1 d", round(312 / 1148, 4), 0.2718)
eq("s1 bd", round((312 / 92) * (312 / 1148), 4), 0.9217); eq("s1 r2", round((312 / _s(92 * 1148)) ** 2, 4), 0.9217)
# s2: groups
_ax = [1, 2, 3]; _ay = [10, 11, 12]; _bx = [6, 7, 8]; _by = [2, 3, 4]
_gx = _ax + _bx; _gy = _ay + _by
_mx = sum(_gx) / 6; _my = sum(_gy) / 6; eq("s2 mx", _mx, 4.5); eq("s2 my", _my, 7)
_Sxx = sum((a - _mx) ** 2 for a in _gx); _Syy = sum((a - _my) ** 2 for a in _gy); _Sxy = sum((a - _mx) * (b - _my) for a, b in zip(_gx, _gy))
eq("s2 Sxx", _Sxx, 41.5); eq("s2 Syy", _Syy, 100); eq("s2 Sxy", _Sxy, -56); eq("s2 r", sf(_Sxy / _s(_Sxx * _Syy)), -0.869)
print("ok")
