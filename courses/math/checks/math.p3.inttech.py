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

# ---- v2 additions ----
# warm-up
chk("W1", lambda x: x * exp(2 * x), lambda x: (1 + 2 * x) * exp(2 * x))
for x in (0.3, 1.9, 4.0): eq("W2", 3 / ((x - 1) * (x + 2)), 1 / (x - 1) - 1 / (x + 2))
eq("W3", tan(pi / 4), 1, 1e-12)
# proofs: ln|f| derivative for f<0, product rule by parts check
chk("P1 f<0", lambda x: log(abs(x**2 - 9)), lambda x: 2 * x / (x**2 - 9), xs=(0.4, 1.1, 2.2))
# long example A
for x in (0.3, 1.1, 2.7): eq("A pf", (6 * x + 7) / ((x + 1) * (2 * x + 3)), 1 / (x + 1) + 4 / (2 * x + 3))
assert 6 * -1 + 7 == 1 and 6 * -1.5 + 7 == -2 == -0.5 * 4
fa = lambda x: (6 * x + 7) / ((x + 1) * (2 * x + 3))
eq("A area", simpson(fa, 0, 2), log(49 / 3), 1e-8); eq("A area exact", 2 * log(7) - log(3), log(49 / 3)); eq("A 3sf", sf(log(49 / 3)), 2.79)
eq("A y0", fa(0), 7 / 3, 1e-12); eq("A y0 dp", sf(fa(0), 3), 2.33); eq("A y2", sf(fa(2), 2), 0.90)
chk("A gradient", fa, lambda x: -1 / (x + 1)**2 - 8 / (2 * x + 3)**2)
# long example B
eq("B (a)", simpson(lambda x: exp(sqrt(x)), 0, 4, 20000), simpson(lambda u: 2 * u * exp(u), 0, 2), 1e-4)
eq("B (b)", simpson(lambda u: 2 * u * exp(u), 0, 2), 2 * e**2 + 2, 1e-8)
eq("B (c)", simpson(lambda x: 1 + exp(sqrt(x)), 0, 4, 20000), 2 * e**2 + 6, 1e-4)
eq("B 16.8", sf(2 * e**2 + 2), 16.8); eq("B avg", sf((2 * e**2 + 2) / 4, 2), 4.2); eq("B e2", sf(e**2, 3), 7.39)
# spot the error
eq("SE value", simpson(lambda x: x * sqrt(x * x + 1), 0, 2), (5 * sqrt(5) - 1) / 3, 1e-8); eq("SE 3sf", sf((5 * sqrt(5) - 1) / 3), 3.39)
eq("SE wrong", sf(2**1.5 / 3), 0.943); eq("SE x1", sf(sqrt(2)), 1.41); eq("SE x2", sf(2 * sqrt(5)), 4.47)
assert 1 + 1 + 1 == 3 and 1 + 1 + 1 + 1 + 1 == 5
# exam practice
eq("E1", simpson(lambda x: 3 * x * x / (x**3 + 1), 0, 2), log(9), 1e-8)
eq("E2", simpson(lambda x: x * exp(-2 * x), 0, 1), 0.25 - 0.75 * exp(-2), 1e-9)
eq("E3", simpson(lambda x: 1 / (1 + sqrt(x)), 0, 4), 4 - 2 * log(3), 1e-4); eq("E3 3sf", sf(4 - 2 * log(3)), 1.80)
for x in (0.5, 2.0, 7.0): eq("E4 pf", (5 * x + 7) / ((x + 1) * (x + 3)), 1 / (x + 1) + 4 / (x + 3))
eq("E4", simpson(lambda x: (5 * x + 7) / ((x + 1) * (x + 3)), 0, 2), log(625 / 27), 1e-8); eq("E4 alt", 4 * log(5) - 3 * log(3), log(625 / 27))
assert 5 * -1 + 7 == 2 and 5 * -3 + 7 == -8
eq("E5", simpson(lambda x: x**3 * log(x), 1, e), (3 * e**4 + 1) / 16, 1e-8)
chk("E6 dy", lambda x: x * exp(-x), lambda x: (1 - x) * exp(-x)); chk("E6 d2y", lambda x: (1 - x) * exp(-x), lambda x: (x - 2) * exp(-x))
eq("E6 area", simpson(lambda x: x * exp(-x), 0, 1), 1 - 2 / e, 1e-9)
eq("E7", simpson(lambda x: exp(x) / (exp(2 * x) + 3 * exp(x) + 2), 0, log(3)), log(6 / 5), 1e-9)
eq("E7 u", simpson(lambda u: 1 / ((u + 1) * (u + 2)), 1, 3), log(6 / 5), 1e-9); assert -1 + 2 == 1 and -2 + 1 == -1 and (u := 3) and (u**2 + 3 * u + 2) == (u + 1) * (u + 2)
eq("E7 comb", log(4 * 3 / (5 * 2)), log(6 / 5))
# stretch
In = lambda n: simpson(lambda x: x**n * exp(x), 0, 1)
eq("S1 I0", In(0), e - 1, 1e-9); eq("S1 I1", In(1), 1, 1e-9); eq("S1 I2", In(2), e - 2, 1e-9); eq("S1 I3", In(3), 6 - 2 * e, 1e-9)
for n in (1, 2, 3, 4): eq("S1 recurrence", In(n), e - n * In(n - 1), 1e-9)
eq("S2 I", simpson(lambda x: exp(x) * sin(x), 0, pi / 2), 0.5 * (exp(pi / 2) + 1), 1e-9)
eq("S2 J", simpson(lambda x: exp(x) * cos(x), 0, pi / 2), 0.5 * (exp(pi / 2) + 1) - 1, 1e-9)
print("ok")
