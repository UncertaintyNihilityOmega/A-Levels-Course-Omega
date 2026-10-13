# checks/math.p3.numerical.py: recomputes every number in the Numerical solution of equations chapter.
from math import isclose, sqrt, sin, cos, tan, acos, exp, log, e, pi

def eq(label, got, want, tol=1e-4):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def cbrt(x): return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))
def iterate(F, x0, n):
    out = []; x = x0
    for _ in range(n): x = F(x); out.append(x)
    return out
def bis(f, a, b):
    for _ in range(80):
        m = (a + b) / 2
        if f(a) * f(m) <= 0: b = m
        else: a = m
    return a

# sign change
f = lambda x: x**3 + x - 5
assert f(1) == -3 and f(2) == 5
g = lambda x: exp(x) + x - 4
eq("g1", g(1), -0.282, 1e-3); eq("g1.5", g(1.5), 1.98, 1e-2)
# traps
assert (1 / -1) < 0 < (1 / 1) and (0 - 1)**2 == 1 and (2 - 1)**2 == 1 and (-3)**2 - 4 == 5 == 3**2 - 4
# ln x + x - 3
h = lambda x: log(x) + x - 3
eq("h2", h(2), -0.307, 1e-3); eq("h3", h(3), 1.099, 1e-3); eq("0.693", log(2), 0.693, 1e-3)
eq("h2.205", h(2.205), -0.0043, 1e-4); eq("h2.215", h(2.215), 0.0103, 1e-4)
eq("ln2.205", log(2.205), 0.7907, 1e-4); eq("ln2.215", log(2.215), 0.7953, 1e-4)
r = bis(h, 2, 3); eq("root", r, 2.2079, 1e-4); eq("plot pt y", 3 - r, 0.7921, 1e-4)
# x^3 - 2x - 5
k = lambda x: x**3 - 2 * x - 5; assert bis(k, 2, 3) > 2.0945
xs = iterate(lambda x: cbrt(2 * x + 5), 2, 5)
for a, b in zip(xs, (2.080084, 2.092351, 2.094217, 2.094501, 2.094544)): eq("it", a, b, 1e-6)
assert round(bis(k, 2, 3), 3) == 2.095
xs = iterate(lambda x: (x**3 - 5) / 2, 2, 5)
eq("d1", xs[0], 1.5); eq("d2", xs[1], -0.8125); eq("d3", xs[2], -2.768, 1e-3); eq("d4", xs[3], -13.1, 0.1); eq("d5", xs[4], -1128, 1)
eq("-0.536", (-0.8125)**3, -0.536, 1e-3); eq("-21.2", (-2.768)**3, -21.2, 0.05)
# e^x + 2x - 10
xs = iterate(lambda x: log(10 - 2 * x), 1.8, 6)
for a, b in zip(xs, (1.8563, 1.8385, 1.8442, 1.8424, 1.8430, 1.8428)): eq("e it", a, b, 1e-4)
eq("ln6.4", log(6.4), 1.8563, 1e-4); eq("6.2874", 10 - 2 * 1.8563, 6.2874, 1e-4); eq("6.3230", 10 - 2 * 1.8385, 6.323, 1e-4)
m = lambda x: exp(x) + 2 * x - 10; assert m(1.8) < 0 < m(1.9) and round(bis(m, 1.8, 1.9), 2) == 1.84
# sqrt(3 + x)
al = (1 + sqrt(13)) / 2; eq("alpha", al, 2.3028, 1e-3); eq("sqrt", sqrt(3 + al), al); assert round(al, 2) == 2.30
# tank
c = 6 / pi; eq("c", c, 1.9099, 1e-4)
t = lambda h: h**3 - 3 * h**2 + c
eq("f.9", t(0.9), 0.209, 1e-3); eq("f1", t(1), -0.090, 1e-3); eq("f.965", t(0.965), 0.0148, 1e-4); eq("f.975", t(0.975), -0.0152, 1e-4)
xs = iterate(lambda h: sqrt((h**3 + c) / 3), 0.9, 7)
for a, b in zip(xs, (0.9379, 0.9548, 0.9627, 0.9664, 0.9683, 0.9691, 0.9695)): eq("tank", a, b, 1e-4)
rt = bis(t, 0.9, 1); eq("tank root", rt, 0.97, 1e-3); eq("V", pi * rt**2 * (3 - rt) / 3, 2, 1e-9)
# exam x^3 - x - 3
kk = lambda x: x**3 - x - 3; assert kk(1) == -3 and kk(2) == 3
xs = iterate(lambda x: cbrt(x + 3), 1.5, 5)
for a, b in zip(xs, (1.6510, 1.6692, 1.6714, 1.6717, 1.6717)): eq("exam it", a, b, 1e-4)
eq("kk(1.6715)", kk(1.6715), -0.0015, 1e-4); eq("kk(1.6725)", kk(1.6725), 0.0059, 1e-4); assert round(bis(kk, 1, 2), 3) == 1.672

# try
t1 = lambda x: x**3 - 4 * x + 1; assert t1(1) == -2 and t1(2) == 1
assert (1 / (1 - 2)) == -1 and (1 / (3 - 2)) == 1
t3 = lambda x: exp(-x) - x; eq("t3a", t3(0.5), 0.1065, 1e-4); eq("t3b", t3(0.6), -0.0512, 1e-4)
assert f(1.5) == -0.125; eq("f1.6", f(1.6), 0.696, 1e-3)
xs = iterate(lambda x: cbrt(5 - x), 1.5, 4)
for a, b in zip(xs, (1.5183, 1.5156, 1.5160, 1.5159)): eq("T4", a, b, 1e-4)
eq("T4 root", round(bis(f, 1, 2), 2), 1.52); eq("3.4817", 5 - 1.5183, 3.4817, 1e-4)
s = lambda x: 2 * log(x) + x - 6
xs = iterate(lambda x: 6 - 2 * log(x), 3, 6)
for a, b in zip(xs, (3.8028, 3.3285, 3.5949, 3.4410, 3.5285, 3.4783)): eq("T6", a, b, 1e-4)
eq("s3.495", s(3.495), -0.0023, 1e-4); eq("s3.505", s(3.505), 0.0134, 1e-4); assert round(bis(s, 3, 4), 2) == 3.50
# exam cos
q = lambda x: 2 * cos(x) - x
eq("q1", q(1), 0.081, 1e-3); eq("q1.5", q(1.5), -1.359, 1e-3)
xs = iterate(lambda x: acos(x / 2), 1, 7)
for a, b in zip(xs, (1.0472, 1.0197, 1.0358, 1.0264, 1.0319, 1.0287, 1.0306)): eq("acos it", a, b, 1e-4)
eq("q1.025", q(1.025), 0.0132, 1e-4); eq("q1.035", q(1.035), -0.0139, 1e-4); assert round(bis(q, 1, 1.5), 2) == 1.03
xs = iterate(lambda x: 2 * cos(x), 1, 6)
for a, b in zip(xs, (1.0806, 0.9416, 1.1770, 0.7674, 1.4395, 0.2619)): eq("2cos it", a, b, 1e-4)
# quiz
assert 0**3 - 6 * 0 + 2 == 2 and 1 - 6 + 2 == -3
eq("mid", (1.335 + 1.345) / 2, 1.34, 1e-12)
assert 3**2 - 3 - 6 == 0 and sqrt(3 + 6) == 3

# ---- v2 additions: warm-up, proofs, spot the error, exam practice, stretch ----
T = 5e-5                                                                    # 4 d.p. tolerance
def sf(x, n=3): return float(f"{x:.{n}g}")
for x in (1.5, 2.7): eq("warm-up", cbrt(2 * x + 5) ** 3, 2 * x + 5, 1e-9)
eq("warm-up e^1.5", exp(1.5), 4.48, 5e-3); eq("warm-up grad", log(e) + 1, 2)
f = lambda x: x ** 3 - x - 3                                               # spot the error
eq("spot f(1.67)", f(1.67), -0.0125, 5e-5); eq("spot f(1.68)", f(1.68), 0.0616, 5e-5)
eq("spot f(1.665)", f(1.665), -0.0492, 5e-5); eq("spot f(1.675)", f(1.675), 0.0244, 5e-5)
assert f(1.665) < 0 < f(1.675) and round(1.676, 2) == 1.68 and round(1.6717, 2) == 1.67
eq("spot root", bis(f, 1, 2), 1.6717, 5e-5)
g = lambda x: x ** 3 + 2 * x - 7; assert g(1) == -4 and g(2) == 5            # exam practice Q1
xs = iterate(lambda x: sqrt(3 * x + 4), 3, 3)                              # Q2
eq("Q2 x1", sf(xs[0], 4), 3.606, 5e-4); eq("Q2 x2", sf(xs[1], 4), 3.849, 5e-4); eq("Q2 x3", sf(xs[2], 4), 3.943, 5e-4)
h = lambda x: exp(x) + x - 4                                               # Q3
eq("Q3 f(1)", h(1), -0.282, 5e-4); eq("Q3 f(1.5)", h(1.5), 1.98, 5e-3); assert h(1) < 0 < h(1.5)
k = lambda x: 2 * x ** 3 - 3 * x - 4                                       # Q4
r4 = bis(k, 1, 2); eq("Q4 fixed point", cbrt((3 * r4 + 4) / 2), r4, 1e-9)
xs = iterate(lambda x: cbrt((3 * x + 4) / 2), 1.5, 3)
for i, w in enumerate((1.6198, 1.6423, 1.6465)): eq(f"Q4 x{i+1}", xs[i], w, T)
eq("Q4 g(1.645)", k(1.645), -0.0322, 5e-5); eq("Q4 g(1.655)", k(1.655), 0.1012, 5e-5); assert k(1.645) < 0 < k(1.655)
m = lambda x: log(x) + 2 * x - 5                                           # Q5
eq("Q5 f(2)", m(2), -0.307, 5e-4); eq("Q5 f(2.5)", m(2.5), 0.916, 5e-4)
xs = iterate(lambda x: (5 - log(x)) / 2, 2, 3)
for i, w in enumerate((2.1534, 2.1165, 2.1251)): eq(f"Q5 x{i+1}", xs[i], w, T)
eq("Q5 f(2.115)", m(2.115), -0.0209, 5e-5); eq("Q5 f(2.125)", m(2.125), 0.0038, 5e-5); assert m(2.115) < 0 < m(2.125)
p = lambda x: 2 ** x - 5 * x                                               # Q6
assert p(4) == -4 and p(5) == 7
xs = iterate(lambda x: log(5 * x) / log(2), 4.5, 3)
for i, w in enumerate((4.4919, 4.4892, 4.4884)): eq(f"Q6 x{i+1}", xs[i], w, T)
eq("Q6 f(4.485)", p(4.485), -0.0316, 5e-5); eq("Q6 f(4.495)", p(4.495), 0.0741, 5e-5); assert p(4.485) < 0 < p(4.495)
for x in (3.3, 4.8): eq("Q6 rearrange", log(2 ** x) / log(2), x)
q = lambda x: x ** 3 - 3 * x - 1                                           # stretch 1
assert [q(t) for t in (-2, -1, 0, 1, 2)] == [-3, 1, -1, -3, 1]
xs = iterate(lambda x: (x ** 3 - 1) / 3, 0, 4)
for i, w in enumerate((-0.3333, -0.3457, -0.3471, -0.3473)): eq(f"S1 x{i+1}", xs[i], w, T)
eq("S1 root", bis(q, -1, 0), -0.3473, 5e-5)
xs = iterate(lambda x: (x ** 3 - 1) / 3, 2, 3)
eq("S1 d1", xs[0], 2.333, 5e-4); eq("S1 d2", xs[1], 3.901, 5e-4); eq("S1 d3", xs[2], 19.46, 5e-3); assert xs[2] > xs[1] > xs[0] > 2
a = 3; assert a ** 2 - 2 * a - 3 == 0 and 2 + 3 / a == a                    # stretch 2
xs = iterate(lambda x: 2 + 3 / x, 1, 40); assert all(x > 0 for x in xs); eq("S2 limit", xs[-1], 3, 1e-6)
print("ok")
