# checks/math.p3.diffeq.py: recomputes every number in the Differential equations chapter.
from math import isclose, sqrt, sin, cos, tan, exp, log, e, pi

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def d(f, x, h=1e-6): return (f(x + h) - f(x - h)) / (2 * h)
def ode(label, y, rhs, xs):
    """y(x) solves dy/dx = rhs(x, y) at each x."""
    for x in xs: eq(label, d(y, x), rhs(x, y(x)), 1e-5)

# worked: simple
ode("3y", lambda x: 5 * exp(3 * x), lambda x, y: 3 * y, (0.1, 0.5, 1.0)); eq("3y init", 5 * exp(0), 5)
ode("x/y", lambda x: sqrt(x * x + 4), lambda x, y: x / y, (0.3, 1.0, 2.5)); eq("x/y init", sqrt(4), 2)
ode("2xe-y", lambda x: log(x * x + 1), lambda x, y: 2 * x * exp(-y), (0.3, 1.0, 2.5)); eq("init", log(1), 0)

# insects
k = log(2) / 5; eq("k", sf(k), 0.139)
eq("N12", sf(2000 * 2**(12 / 5)), 10600); eq("N12 exp", 2000 * exp(12 * k), 2000 * 2**2.4)
t = 5 * log(5) / log(2); eq("t", sf(t), 11.6); eq("t check", 2000 * exp(k * t), 10000, 1e-6)
ode("N", lambda t: 2000 * exp(k * t), lambda t, N: k * N, (1.0, 4.0))

# cooling
kc = log(7 / 4) / 5; eq("kc", sf(kc), 0.112); eq("5k", 70 * exp(-5 * kc), 40, 1e-9)
th = lambda t: 20 + 70 * exp(-kc * t)
eq("th10", sf(th(10)), 42.9); eq("th10 frac", th(10), 20 + 70 * 16 / 49)
t40 = log(3.5) / kc; eq("t40", sf(t40), 11.2); eq("t40 check", th(t40), 40, 1e-9)
ode("cool", th, lambda t, v: -kc * (v - 20), (1.0, 6.0))
eq("e^-10k", exp(-10 * kc), 16 / 49)

# tank (exam)
hh = lambda t: ((20 - 0.4 * t) / 2)**2
eq("h0", hh(0), 100); eq("h10", hh(10), 64); eq("empty", hh(50), 0)
ode("tank", hh, lambda t, h: -0.4 * sqrt(h), (1.0, 10.0, 30.0))

# logistic
P = lambda t: 10 / (1 + 9 * exp(-0.5 * t))
eq("P0", P(0), 1); ode("P", P, lambda t, p: 0.05 * p * (10 - p), (0.5, 2.0, 5.0, 9.0))
tP = 2 * log(9); eq("tP", sf(tP), 4.39); eq("P(tP)", P(tP), 5, 1e-9)
eq("P form", 10 * exp(0.5 * 3) / (9 + exp(0.5 * 3)), P(3))
for p in (1.0, 3.0): eq("pf", 1 / (p * (10 - p)), 0.1 * (1 / p + 1 / (10 - p)))
eq("lim", P(60), 10, 1e-9); eq("plot pt", round(tP, 3), 4.394, 1e-9)

# exam: xy ln x
Y = lambda x: exp(0.5 * x * x * log(x) - 0.25 * x * x + 0.25)
eq("Y1", Y(1), 1); ode("xylnx", Y, lambda x, y: x * y * log(x), (1.3, 2.0, 2.7))
eq("lny", (e * e + 1) / 4, 0.5 * e * e - 0.25 * e * e + 0.25); eq("lny sf", round((e * e + 1) / 4, 3), 2.097)
eq("Y(e)", sf(Y(e)), 8.14)

# try
ode("T2", lambda x: 1 / (1 - 4 * x), lambda x, y: 4 * y * y, (0.05, 0.1, 0.2))
ode("T3", lambda x: log((exp(2 * x) + 1) / 2), lambda x, y: exp(2 * x - y), (0.2, 0.7, 1.5)); eq("T3 init", log(1), 0)
ode("T4", lambda x: exp(x * sin(x) + cos(x) - 1), lambda x, y: x * y * cos(x), (0.3, 1.0, 2.0)); eq("T4 init", exp(0 + 1 - 1), 1)
for x in (0.4, 1.1, 2.3): eq("T4 parts", d(lambda s: s * sin(s) + cos(s), x), x * cos(x), 1e-5)
eq("T5", sf(40 * 2**-2.5), 7.07); eq("T5 hl", 40 * exp(-log(2) / 8 * 8), 20)
eq("T6", sf(20 + 60 * exp(-0.6)), 52.9); ode("T6", lambda t: 20 + 60 * exp(-0.1 * t), lambda t, v: -0.1 * (v - 20), (1.0, 6.0))
h7 = lambda t: ((12 - 0.5 * t) / 2)**2
eq("T7 h0", h7(0), 36); eq("T7 h8", h7(8), 16); eq("T7 empty", h7(24), 0); ode("T7", h7, lambda t, h: -0.5 * sqrt(h), (1.0, 8.0))
ode("T8", lambda x: 4 * x / (x + 1), lambda x, y: y / (x * (x + 1)), (0.5, 1.0, 3.0)); eq("T8 init", 4 / 2, 2)
for x in (0.5, 2.0): eq("T8 pf", 1 / (x * (x + 1)), 1 / x - 1 / (x + 1))
eq("T8 c", log(2), log(0.5) + log(4))
# quiz
ode("Q3", lambda x: 7 * exp(2 * x), lambda x, y: 2 * y, (0.3, 1.0))

# ---- v2 additions ----
def rk4(f, x0, y0, x1, n=4000):
    h = (x1 - x0) / n; x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y); k2 = f(x + h / 2, y + h * k1 / 2); k3 = f(x + h / 2, y + h * k2 / 2); k4 = f(x + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; x += h
    return y
# warm-up
eq("W1", sf(log(2) / 3), 0.231); ode("W2", lambda y: 0.5 * log(abs(2 * y + 1)), lambda y, _: 1 / (2 * y + 1), (0.5, 2.0))
for y in (0.7, 2.5, 3.9): eq("W3", 1 / (y * (4 - y)), 0.25 * (1 / y + 1 / (4 - y)))
# slope-field example hyperbola and logistic (as described in the text)
ode("hyperbola", lambda x: sqrt(x * x + 4), lambda x, y: x / y, (0.5, 1.5, 3.0))
# long example A (tank)
V = lambda t: 40 * (1 - exp(-0.15 * t))
ode("A DE", V, lambda t, v: 6 - 0.15 * v, (0.5, 2.0, 7.0)); eq("A V0", V(0), 0); eq("A k", 6 - 40 * 0.15, 0)
eq("A t", sf(log(4) / 0.15), 9.24); eq("A V30", V(log(4) / 0.15), 30, 1e-9); eq("A limit", V(1e6), 40, 1e-9)
eq("A rk4", rk4(lambda t, v: 6 - 0.15 * v, 0, 0, 5), V(5), 1e-6)
# long example B
yB = lambda x: sqrt(3 - 2 * (x + 1) * exp(-x))
ode("B DE", yB, lambda x, y: x * exp(-x) / y, (0.3, 1.0, 2.0, 4.0)); eq("B y0", yB(0), 1)
eq("B y2 sq", sf(3 - 6 * exp(-2), 4), 2.188); eq("B y2", sf(yB(2)), 1.48); eq("B limit", yB(60), sqrt(3), 1e-9)
eq("B rk4", rk4(lambda x, y: x * exp(-x) / y, 0, 1, 2), yB(2), 1e-8)
for x in (0.5, 1.7): eq("B deriv", d(lambda s: -2 * (s + 1) * exp(-s), x), 2 * x * exp(-x), 1e-6)
# spot the error
eq("SE y(0) wrong", 89 + 1, 90); eq("SE c", 70 - 1, 69)
th = lambda t: 20 + 70 * exp(-0.2 * t); ode("SE good", th, lambda t, y: -0.2 * (y - 20), (0.5, 3.0)); eq("SE good 0", th(0), 90)
bad = lambda t: 89 + exp(-0.2 * t); assert abs(d(bad, 1.0) - (-0.2 * (bad(1.0) - 20))) > 1
# exam practice
assert 10 == 50 * 0.2
ode("E2", lambda x: sqrt(2 * x**3 + 4), lambda x, y: 3 * x * x / y, (0.4, 1.3)); eq("E2 y0", 2, sqrt(4))
ode("E3", lambda x: 1 / (2 - exp(x)), lambda x, y: y * y * exp(x), (-1.0, 0.3, 0.6)); eq("E3 y0", 1 / (2 - 1), 1); assert 2 - exp(log(2)) == 0
ode("E4", lambda x: 3 / cos(x), lambda x, y: y * sin(x) / cos(x), (0.3, 1.0)); eq("E4 x", 1 / cos(pi / 3), 2); eq("E4 y", 3 / cos(pi / 3), 6)
k = log(4 / 3) / 3; eq("E5 k", sf(k), 0.0959); eq("E5 C6", sf(8 * exp(-6 * k)), 4.50); eq("E5 C6 exact", 8 * (3 / 4)**2, 4.5)
eq("E5 t", sf(log(4) / k), 14.5); eq("E5 C3", 8 * exp(-3 * k), 6, 1e-12)
for x in (0.2, 1.1, 5.0): eq("E6 pf", 4 / ((x + 1) * (x + 3)), 2 / (x + 1) - 2 / (x + 3))
ode("E6", lambda x: 16 * ((x + 1) / (x + 3))**2, lambda x, y: 4 * y / ((x + 1) * (x + 3)), (1.0, 2.3, 6.0)); eq("E6 y1", 16 * (2 / 4)**2, 4)
xs = lambda t: 20 * (exp(0.06 * t) - 1) / (5 * exp(0.06 * t) - 2)
ode("E7 DE", xs, lambda t, x: 0.01 * (10 - x) * (4 - x), (1.0, 5.0, 10.0, 30.0)); eq("E7 x0", xs(0), 0)
for x in (0.5, 2.0, 3.3): eq("E7 pf", 1 / ((10 - x) * (4 - x)), (1 / (4 - x) - 1 / (10 - x)) / 6)
eq("E7 x10", sf(xs(10)), 2.31); eq("E7 limit", xs(1e4 / 6), 4, 1e-9); eq("E7 rk4", rk4(lambda t, x: 0.01 * (10 - x) * (4 - x), 0, 0, 10), xs(10), 1e-8)
eq("E7 form", (10 - xs(7)) / (4 - xs(7)), 2.5 * exp(0.42), 1e-9)
# stretch
kk = log(14 / 11) / 30; eq("S1 k", sf(kk, 3), 0.00804); eq("S1 e30", exp(-30 * kk), 11 / 14); eq("S1 t", -log(29 / 14) / kk, -90.59, 1e-2)
eq("S1 mins", 540 - 90.6, 449.4, 1e-9); assert 7 * 60 + 29 == 449 and 9 * 60 - 91 == 449
yS = lambda x: tan(sin(x)); ode("S2", yS, lambda x, y: (1 + y * y) * cos(x), (0.3, 1.0, 2.0)); eq("S2 max", sf(tan(1)), 1.56); assert 1 < pi / 2
print("ok")
