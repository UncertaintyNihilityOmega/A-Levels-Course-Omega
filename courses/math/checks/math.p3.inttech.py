# checks/math.p3.inttech.py: recomputes every number in the Integration techniques chapter.
from math import isclose, sqrt, sin, cos, tan, exp, log, atan, e, pi

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def d(f, x, h=1e-6): return (f(x + h) - f(x - h)) / (2 * h)
def chk(label, F, f, xs=(0.4, 0.9, 1.7, 2.6)):
    for x in xs: eq(label, d(F, x), f(x), 1e-5)
def simpson(f, a, b, n=4000):
    h = (b - a) / n; s = f(a) + f(b)
    for i in range(1, n): s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

# f'/f
chk("a", lambda x: 0.5 * log(x * x + 4), lambda x: x / (x * x + 4))
chk("b", lambda x: -log(abs(cos(x))), lambda x: tan(x), xs=(0.3, 0.8, 1.2))
eq("c", sf(log(13)), 2.56); eq("c num", simpson(lambda x: (3 * x * x + 2) / (x**3 + 2 * x + 1), 0, 2), log(13), 1e-8)
chk("1/(x2+4)", lambda x: 0.5 * atan(x / 2), lambda x: 1 / (x * x + 4))

# partial fractions
f1 = lambda x: (5 * x + 1) / ((x - 1) * (x + 2))
for x in (3.0, 5.0): eq("pf1", 2 / (x - 1) + 3 / (x + 2), f1(x))
eq("pf1 int", 2 * log(3) + 3 * log(1.5), simpson(f1, 2, 4), 1e-8); eq("pf1 sf", sf(2 * log(3) + 3 * log(1.5)), 3.41)
g = lambda x: (x * x + 3) / (x * x - 1)
for x in (2.0, 3.5): eq("pf2", 1 + 2 / (x - 1) - 2 / (x + 1), g(x))
eq("pf2 int", 1 + 2 * log(1.5), simpson(g, 2, 3), 1e-8); eq("pf2 alg", 1 - 2 * log(2) + 2 * log(3), 1 + 2 * log(1.5))
h3 = lambda x: (3 * x + 1) / ((x - 1) * (x + 2)**2)
for x in (2.0, 3.0, 5.0): eq("pf3", (4 / 9) / (x - 1) - (4 / 9) / (x + 2) + (5 / 3) / (x + 2)**2, h3(x))
eq("pf3 int", 4 / 9 * log(2) + 5 / 36, simpson(h3, 2, 4), 1e-8)
eq("pf3 step", (4 / 9) * log(0.5) - 5 / 18 - ((4 / 9) * log(0.25) - 5 / 12), 4 / 9 * log(2) + 5 / 36)
eq("5/12-5/18", 5 / 12 - 5 / 18, 5 / 36)

# parts
chk("x sin2x", lambda x: -0.5 * x * cos(2 * x) + 0.25 * sin(2 * x), lambda x: x * sin(2 * x))
eq("xsin2x def", pi / 4, simpson(lambda x: x * sin(2 * x), 0, pi / 2), 1e-8)
chk("ln", lambda x: x * log(x) - x, lambda x: log(x))
eq("xlnx", (e * e + 1) / 4, simpson(lambda x: x * log(x), 1, e), 1e-8); eq("xlnx sf", sf((e * e + 1) / 4), 2.10)
eq("e2/2-e2/4+1/4", e * e / 2 - e * e / 4 + 0.25, (e * e + 1) / 4)
chk("x2e-x", lambda x: -exp(-x) * (x * x + 2 * x + 2), lambda x: x * x * exp(-x))
eq("x2e-x def", 2 - 5 / e, simpson(lambda x: x * x * exp(-x), 0, 1), 1e-8); eq("x2e sf", sf(2 - 5 / e), 0.161)
eq("xatan", pi / 4 - 0.5, simpson(lambda x: x * atan(x), 0, 1), 1e-8); eq("xatan alg", pi / 8 - 0.5 * (1 - pi / 4), pi / 4 - 0.5)
chk("x-atan", lambda x: x - atan(x), lambda x: x * x / (1 + x * x))
V = simpson(lambda t: t * exp(-t / 2), 0, 4)
eq("tank", 4 - 12 * exp(-2), V, 1e-8); eq("tank sf", sf(V), 2.38); eq("tank alg", -8 * exp(-2) - 4 * exp(-2) + 4, V, 1e-12)
chk("-2te", lambda t: -2 * t * exp(-t / 2) - 4 * exp(-t / 2), lambda t: t * exp(-t / 2))

# substitution
eq("sub1", 8 / 3, simpson(lambda x: x / sqrt(x + 1), 0, 3), 1e-8); eq("sub1 alg", (16 / 3 - 4) - (2 / 3 - 2), 8 / 3)
eq("sub2", 8 / 15, simpson(lambda x: sin(2 * x)**2 * cos(x), 0, pi / 2), 1e-8); eq("sub2 alg", 4 / 3 - 4 / 5, 8 / 15)
for x in (0.3, 1.0): eq("sin2 cos", sin(2 * x)**2 * cos(x), 4 * sin(x)**2 * (1 - sin(x)**2) * cos(x))
eq("sub3", 2 * log(1.5), simpson(lambda x: 1 / (x + sqrt(x)), 1, 4), 1e-8)
for u in (1.2, 1.7): eq("sub3 u", 2 * u / (u * u + u), 2 / (u + 1))

# try
chk("T1", lambda x: log(x * x + 5), lambda x: 2 * x / (x * x + 5))
eq("T2", sf(log(1.5)), 0.405); eq("T2 num", simpson(lambda x: exp(x) / (1 + exp(x)), 0, log(2)), log(1.5), 1e-8)
t3 = lambda x: (x + 5) / ((x + 1) * (x + 2))
for x in (1.0, 2.0): eq("T3 pf", 4 / (x + 1) - 3 / (x + 2), t3(x))
eq("T3", sf(4 * log(1.5) - 3 * log(4 / 3)), 0.759); eq("T3 num", simpson(t3, 1, 2), 4 * log(1.5) - 3 * log(4 / 3), 1e-8)
eq("T4", pi / 2 - 1, simpson(lambda x: x * cos(x), 0, pi / 2), 1e-8)
eq("T5", (2 * e**3 + 1) / 9, simpson(lambda x: x * exp(3 * x), 0, 1), 1e-7); eq("T5 sf", sf((2 * e**3 + 1) / 9), 4.57)
eq("T5 alg", e**3 / 3 - (e**3 - 1) / 9, (2 * e**3 + 1) / 9)
eq("T6", 0.5 - log(2) / 2, simpson(lambda x: log(x) / x**2, 1, 2), 1e-8); eq("T6 sf", sf(0.5 - log(2) / 2), 0.153)
chk("T7", lambda x: -x * x * cos(x) + 2 * x * sin(x) + 2 * cos(x), lambda x: x * x * sin(x))
eq("T8", 1 / 8, simpson(lambda x: x / (1 + x)**3, 0, 1), 1e-8); eq("T8 alg", (-0.5 + 0.125) - (-1 + 0.5), 1 / 8)
eq("T9", 2 / 3, simpson(lambda x: sin(x)**3, 0, pi / 2), 1e-8)
# quiz
chk("Q1", lambda x: 0.5 * log(x * x + 1), lambda x: x / (x * x + 1)); chk("Q4", lambda x: x * log(x) - x, lambda x: log(x))
eq("Q3", 1 / 3, simpson(lambda x: sin(x)**2 * cos(x), 0, pi / 2), 1e-8)
for x in (1.5, 4.0): eq("Q5", (x * x + 3) / (x * x - 1), 1 + 4 / (x * x - 1))
print("ok")
