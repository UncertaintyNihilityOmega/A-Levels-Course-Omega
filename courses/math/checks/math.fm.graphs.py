# checks/math.fm.graphs.py: recomputes every number in Graphs related to y = f(x).
# Standard library only: finite differences, brute-force sampling of solution sets.
from math import isclose, sqrt


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def grid(lo, hi, n=40001):
    return [lo + (hi - lo) * i / (n - 1) for i in range(n)]


def near(x, pts, tol=1e-3):
    return any(abs(x - p) < tol for p in pts)


# ---- warm-up
assert 2 * 3 - 1 == 5 and 2 * -2 - 1 == -5
g = lambda x: (x + 1) / (x - 2)
assert abs(g(1e6) - 1) < 1e-5

# ---- |f|: f = (x+2)(x-1)(x-3)
f = lambda x: (x + 2) * (x - 1) * (x - 3)
for x in [-3.0, 0.0, 1.7, 5.0]:
    eq("cubic expansion", f(x), x ** 3 - 2 * x ** 2 - 5 * x + 6, 1e-9)
eq("f(0)", f(0), 6)
x1, x2 = (2 - sqrt(19)) / 3, (2 + sqrt(19)) / 3
eq("f' root 1", 3 * x1 * x1 - 4 * x1 - 5, 0, 1e-9)
eq("f' root 2", 3 * x2 * x2 - 4 * x2 - 5, 0, 1e-9)
eq("x1", sf(x1), -0.786)
eq("x2", sf(x2), 2.12)
eq("f(x1)", sf(f(x1)), 8.21)
eq("f(x2)", sf(f(x2)), -4.06)
assert f(x1) > 0 > f(x2)
assert f(-3) < 0 and f(0) > 0 and f(2) < 0 and f(4) > 0
assert 16 + 60 == 76 and sqrt(76) / 6 * 3 - sqrt(19) == 0 or abs(sqrt(76) / 6 - sqrt(19) / 3) < 1e-12
# |f| maxima values are those of |f(x1)|, |f(x2)|
eq("|f(x2)|", sf(abs(f(x2)), 3), 4.06)

# ---- f(|x|): f = x^2-2x-3
h = lambda x: x * x - 2 * x - 3
fa = lambda x: h(abs(x))
eq("fa(3)", fa(3), 0)
eq("fa(-3)", fa(-3), 0)
eq("fa(0)", fa(0), -3)
eq("fa(1)", fa(1), -4)
eq("fa(-1)", fa(-1), -4)
assert abs(fa(2) - h(2)) < 1e-12 and fa(-2) == h(2)
eq("gradient right of 0", d(fa, 1e-3), -2, 1e-2)
eq("gradient left of 0", d(fa, -1e-3), 2, 1e-2)
assert min(fa(x) for x in grid(-6, 6)) == -4.0 or abs(min(fa(x) for x in grid(-6, 6)) + 4) < 1e-6
# f(|x|) vs |f| contrast, f = x-2
assert abs(0 - 2) == 2 and abs(2 - 2) == 0

# ---- 1/f: f = x^2-4
f4 = lambda x: x * x - 4
eq("1/f at 0", 1 / f4(0), -0.25)
eq("f(sqrt5)", f4(sqrt(5)), 1)
eq("f(sqrt3)", f4(sqrt(3)), -1)
assert f4(2.001) > 0 and f4(1.999) < 0
# max of 1/f on (-2,2) is -1/4
assert max(1 / f4(x) for x in grid(-1.99, 1.99)) <= -0.25 + 1e-9
# f = x^2-2x+5 >= 4, 1/f max 1/4 at x = 1
f5 = lambda x: x * x - 2 * x + 5
assert abs(f5(1) - 4) < 1e-12 and min(f5(x) for x in grid(-20, 20)) >= 4 - 1e-9
eq("1/f5 max", max(1 / f5(x) for x in grid(-20, 20)), 0.25, 1e-9)
# rational f = (x-1)/(x+2)
fr = lambda x: (x - 1) / (x + 2)
eq("1/fr(0)", 1 / fr(0), -2)
eq("fr(-1/2)", fr(-0.5), -1)
for x in grid(-10, 10, 2001):
    if not near(x, (-2, 1)):
        eq("recip", 1 / fr(x), (x + 2) / (x - 1), 1e-6)
assert abs(-0.5 - 1 + (-0.5 + 2)) < 1e-12   # x-1 = -(x+2) at x = -1/2

# ---- y^2 = f
for x in [-3.0, 3.0, 5.0]:
    assert x * x - 4 >= 0
assert 9 - 4 == 5
c3 = lambda x: (x + 1) * (x - 1) * (x - 3)
for x in [-2.0, -0.5, 0.0, 2.0, 4.0]:
    eq("c3 expansion", c3(x), x ** 3 - 3 * x ** 2 - x + 3)
assert c3(-2) < 0 and c3(0) > 0 and c3(2) < 0 and c3(4) > 0
xm = 1 - 2 / sqrt(3)
eq("c3' zero", 3 * xm * xm - 6 * xm - 1, 0, 1e-12)
eq("xm", sf(xm), -0.155)
eq("c3(xm)", sf(c3(xm), 3), 3.08)
eq("c3(xm) 4sf", sf(c3(xm), 4), 3.079)
eq("sqrt", sf(sqrt(c3(xm)), 3), 1.75)
assert max(c3(x) for x in grid(-1, 1)) <= c3(xm) + 1e-9
width = 2 * sqrt(c3(xm))
eq("width units", sf(width, 3), 3.51)
eq("width m", sf(width * 10, 3), 35.1)
assert round(width * 10) == 35 and (1 - -1) * 10 == 20

# ---- |x^2-2x-3| < 2x+1
m = lambda x: abs(x * x - 2 * x - 3)
ln = lambda x: 2 * x + 1
r1, r2 = 2 + 2 * sqrt(2), 2 - 2 * sqrt(2)
for r in (r1, r2):
    eq("quad root", r * r - 4 * r - 4, 0, 1e-9)
eq("2+2sqrt2", sf(r1), 4.83)
eq("2-2sqrt2", sf(r2), -0.828, 1e-3)
assert r1 >= 3 and not (r2 <= -1 or r2 >= 3)
eq("sqrt2 meets", m(sqrt(2)), ln(sqrt(2)), 1e-9)
eq("-sqrt2 is false", sf(-sqrt(2), 3), -1.41)
assert m(-sqrt(2)) != ln(-sqrt(2))
eq("r1 meets", m(r1), ln(r1), 1e-9)
eq("(sqrt2) y", ln(sqrt(2)), 1 + 2 * sqrt(2))
eq("(r1) y", ln(r1), 5 + 4 * sqrt(2))
eq("bump at -1/2", m(-0.5), 1.75)
eq("bump height at 1", m(1), 4)
for x in grid(-6, 9, 60001):
    inside = sqrt(2) < x < 2 + 2 * sqrt(2)
    if near(x, (sqrt(2), 2 + 2 * sqrt(2))):
        continue
    assert (m(x) < ln(x)) == inside, x
eq("check x=3", m(3), 0)
assert m(3) < ln(3) and not (m(1) < ln(1)) and m(1) == 4 and ln(1) == 3

# ---- 1/(x^2-4) >= 1
for x in grid(-6, 6, 60001):
    if near(x, (-2, 2, sqrt(5), -sqrt(5))):
        continue
    holds = abs(x) > 2 and (1 / (x * x - 4) >= 1)
    mine = (2 < x <= sqrt(5)) or (-sqrt(5) <= x < -2)
    assert (abs(x) != 2 and 1 / (x * x - 4) >= 1) == mine or abs(x) == 2, x
    assert (4 < x * x <= 5) == mine

# ---- 2x/(x+3) > 1/(x-1)
a1, a2 = (3 - sqrt(33)) / 4, (3 + sqrt(33)) / 4
eq("a1 root", 2 * a1 * a1 - 3 * a1 - 3, 0, 1e-9)
eq("a2 root", 2 * a2 * a2 - 3 * a2 - 3, 0, 1e-9)
eq("a1", sf(a1), -0.686)
eq("a2", sf(a2), 2.19, 1e-2)
eq("a2 4sf", sf(a2, 4), 2.186)
assert 9 + 24 == 33
for x in grid(-8, 8, 80001):
    if near(x, (-3, 1, a1, a2)):
        continue
    lhs = 2 * x / (x + 3) > 1 / (x - 1)
    mine = x < -3 or a1 < x < 1 or x > a2
    assert lhs == mine, x
eq("2x(x-1)-(x+3)", 2 * 5 * 4 - 8, 2 * 25 - 15 - 3)
assert 0 > 1 / (0 - 1) and 1.5 / 4.5 < 1 / 0.5
eq("check 1.5", 2 * 1.5 / 4.5, 0.6667, 1e-4)
# sign table by leading behaviour
num = lambda x: 2 * x * x - 3 * x - 3
den = lambda x: (x + 3) * (x - 1)
for x, s in [(5, 1), (1.5, -1), (0, 1), (-1, -1), (-5, 1)]:
    assert (num(x) / den(x) > 0) == (s > 0), x

# ---- (x^2-4)/(x^2-1) > 2
q = lambda x: (x * x - 4) / (x * x - 1)
for x in grid(-6, 6, 60001):
    if near(x, (-1, 1)):
        continue
    assert (q(x) > 2) == (-1 < x < 1), x
for x in [-3.0, 0.0, 0.5, 3.0]:
    eq("rearr", q(x) - 2, -(x * x + 2) / (x * x - 1))
assert min(q(x) for x in grid(-0.99, 0.99)) >= 4 - 1e-9

# ---- exam example: f = (x-2)^2/(x+1)
fe = lambda x: (x - 2) ** 2 / (x + 1)
re = lambda x: (x + 1) / (x - 2) ** 2
for x in [-6.0, -0.3, 0.0, 3.0, 7.0]:
    eq("recip exam", re(x), 1 / fe(x), 1e-12)
eq("min of 1/f", sf(1 / fe(-4), 3), -0.0833, 1e-4)
eq("1/f(-4)", 1 / fe(-4), -1 / 12)
eq("1/f(0)", re(0), 0.25)
eq("1/f(-1)", re(-1), 0)
assert fe(-4) == -12
# derivative of 1/f is (-x-4)/(x-2)^3
for x in [-6.0, -2.0, 0.0, 3.0, 5.0]:
    eq("deriv 1/f", d(re, x), (-x - 4) / (x - 2) ** 3, 1e-5)
assert re(-10) < 0 and re(10) > 0 and abs(re(1e6)) < 1e-5
# f(|x|)
fb = lambda x: fe(abs(x))
eq("f(|x|) at 0", fb(0), 4)
eq("f(|x|) at 2", fb(2), 0)
eq("f(|x|) at -2", fb(-2), 0)
eq("grad right", d(fb, 1e-3), -8, 0.1)
eq("grad left", d(fb, -1e-3), 8, 0.1)
assert abs(fb(40) - (40 - 5)) < 0.3 and abs(fb(-40) - (40 - 5)) < 0.3
# |f| < 2
for x in grid(-30, 30, 120001):
    if near(x, (-1, 3 - sqrt(7), 3 + sqrt(7)), 1e-3):
        continue
    assert (abs(fe(x)) < 2) == (3 - sqrt(7) < x < 3 + sqrt(7)), x
eq("x^2-6x+2 root", (3 - sqrt(7)) ** 2 - 6 * (3 - sqrt(7)) + 2, 0, 1e-9)
assert 4 - 24 < 0 and fe(1) == 0.5
assert max(fe(x) for x in grid(-30, -1.001, 20001)) <= -12 + 1e-6

# ---- spot the error |x-4| < 2x-5
for x in grid(-5, 12, 17001):
    if near(x, (3,)):
        continue
    assert (abs(x - 4) < 2 * x - 5) == (x > 3), x
assert 2 * 1 - 5 == -3 and abs(1 - 4) == 3 and abs(3 - 4) == 1 == 2 * 3 - 5
assert abs(5 - 4) == 1 < 5 and not (abs(2 - 4) < 2 * 2 - 5)
assert 2 * 3 - 5 == 1 and 9 == 3 * 3

# ---- try
assert abs(0 - 3) == 3
assert 2 * 2 == 4 and (2 ** 2 - 4) == 0
for x in [-1, 1, 5, -5]:
    assert x * x - 6 * abs(x) + 5 == 0 if abs(x) in (1, 5) else False
assert 9 - 9 == 0
for x, v in [(3, 7), (-0.5, 3.5)]:
    eq("try |3x-2|", abs(3 * x - 2), x + 4)
for x in grid(-6, 6, 60001):
    if near(x, (1, 1.5)):
        continue
    assert (1 / (x - 1) > 2) == (1 < x < 1.5), x
k = lambda x: abs(x * x - 4)


def count(kv):
    n = 0
    for sgn in (1, -1):
        # x^2 - 4 = sgn*kv  -> x^2 = 4 + sgn*kv
        r = 4 + sgn * kv
        if r > 0:
            n += 2
        elif r == 0:
            n += 1
    return n if kv >= 0 else 0


# k=0 would double count x^2-4=0 twice; handle separately
assert count(2) == 4 and count(6) == 2
assert count(4) == 2 + 1  # x^2=8 (two), x^2=0 (one)
assert k(0) == 4 and k(2) == 0
# k = 0: x = +-2; for 0<k<4: four; k>4: two
assert count(0.5) == 4 and count(5) == 2

# ---- exam practice
# Q1: |x^2-4x|
assert 4 - 8 == -4 and 2 * 2 - 4 * 2 == -4
# Q2: x^2-4x-5 -> f(|x|): roots +-5, min -9 at +-2
fq = lambda x: x * x - 4 * x - 5
eq("q2 root", fq(5), 0)
eq("q2 min", fq(2), -9)
eq("q2 y-int", fq(0), -5)
# Q3: f = x^2-5x+4
f3 = lambda x: x * x - 5 * x + 4
eq("q3 min", f3(2.5), -9 / 4)
eq("q3 recip", 1 / f3(2.5), -4 / 9)
eq("q3 y int", 1 / f3(0), 0.25)
# Q4: y^2 = (x-1)(x-5) = (x-3)^2 - 4
for x in [-2.0, 0.0, 6.0, 9.0]:
    eq("q4", (x - 1) * (x - 5), (x - 3) ** 2 - 4)
# Q5: 3/(x-1) < x+1
for x in grid(-6, 6, 60001):
    if near(x, (-2, 1, 2)):
        continue
    assert (3 / (x - 1) < x + 1) == (-2 < x < 1 or x > 2), x
for x, v in [(0, -4), (3, -2.5), (1.5, 3.5), (-3, 1.25)]:
    eq("q5 sign", (4 - x * x) / (x - 1), v)
# Q6: |x^2-4| = 3x
for x in (4, -1, 1, -4):
    isroot = abs(x * x - 4) == 3 * x
    assert isroot == (x in (4, 1)), x
for x in grid(-3, 8, 22001):
    if near(x, (1, 4)):
        continue
    assert (abs(x * x - 4) < 3 * x) == (1 < x < 4), x
# Q7: f = x^2/(x-2)
f7 = lambda x: x * x / (x - 2)
for x in [-3.0, 0.5, 3.0, 6.0]:
    eq("q7 split", f7(x), x + 2 + 4 / (x - 2))
eq("f7(4)", f7(4), 8)
eq("f7(0)", f7(0), 0)
eq("1/f(4)", 1 / f7(4), 1 / 8)
for x in grid(-8, 10, 36001):
    if near(x, (0, 2, 3)):
        continue
    assert (f7(x) < 3 * x) == (0 < x < 2 or x > 3), x
for x in [-2.0, 1.0, 3.5, 6.0]:
    eq("q7 combined", f7(x) - 3 * x, -2 * x * (x - 3) / (x - 2))
for x in [-5.0, -1.0, 1.0, 5.0]:
    eq("q7 recip", 1 / f7(x), (x - 2) / (x * x), 1e-12)
assert 1 / f7(1) < 0 and 1 / f7(-1) < 0
# Q8: (x^2+3)/(x+1)
f8 = lambda x: (x * x + 3) / (x + 1)
eq("f8(1)", f8(1), 2)
eq("f8(-3)", f8(-3), -6)
for x in [-5.0, 0.0, 2.0, 7.0]:
    eq("f8 split", f8(x), x - 1 + 4 / (x + 1))
eq("f8 d at 1", d(f8, 1.0), 0, 1e-6)
eq("f8 d at -3", d(f8, -3.0), 0, 1e-6)
for x in grid(-8, 8, 80001):
    if near(x, (-1, 0, 3)):
        continue
    assert (f8(x) > 3) == (-1 < x < 0 or x > 3), x
for x in [-3.0, 0.5, 4.0]:
    eq("f8 minus 3", f8(x) - 3, x * (x - 3) / (x + 1))
eq("|f8(-3)|", abs(f8(-3)), 6)

# ---- stretch 1
assert abs(k(0) - 4) == 0 and abs(k(2)) == 0
# for f(|x|) = k with f = x^2-4
assert (4 + (-4)) == 0 and 4 + 0 == 4
# stretch 2: y^2 = (x-1)^2 (x+2)
s2 = lambda x: (x - 1) ** 2 * (x + 2)
for x in [-1.5, 0.0, 2.0, 5.0]:
    eq("s2 expansion", s2(x), x ** 3 - 3 * x + 2)
yp = lambda x: (x - 1) * sqrt(x + 2)
eq("slope at 1", d(yp, 1.0 + 1e-9, 1e-6), sqrt(3), 1e-4)
eq("sqrt3", sf(sqrt(3)), 1.73)
g2 = lambda x: (1 - x) ** 2 * (x + 2)
for x in [-1.7, 0.2, 0.9]:
    eq("g' factor", d(g2, x), (1 - x) * (-3 - 3 * x), 1e-5)
eq("g(-1)", g2(-1), 4)
assert max(g2(x) for x in grid(-2, 1)) <= 4 + 1e-9
eq("ymax", sqrt(g2(-1)), 2)

# ---- marks totals
assert 4 + 3 + 5 == 12 and 3 + 5 + 4 == 12 and 5 + 5 == 10 and 2 + 2 + 4 == 8 and 1 + 4 + 1 == 6
assert 3 + 3 + 5 + 4 + 6 + 6 == 27

# exact-form inequality example: 1 + 1 + 1 + 1 + 1 = 5 marks; numerator 2x^2 - 3x - 3
assert 1 + 1 + 1 + 1 + 1 == 5
for xx in [-2.0, 0.5, 3.0]:
    assert abs((2 * xx / (xx + 3) - 1 / (xx - 1)) - (2 * xx * xx - 3 * xx - 3) / ((xx + 3) * (xx - 1))) < 1e-12

print("ok")
