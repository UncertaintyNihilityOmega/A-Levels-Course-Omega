# checks/math.p3.diffeq.py: recomputes every number in the Differential equations chapter.
from math import isclose, sqrt, sin, cos, exp, log, e, pi

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
print("ok")
