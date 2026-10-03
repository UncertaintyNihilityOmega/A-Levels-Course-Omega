# checks/math.p3.integ.py: recomputes every number in the Further integration chapter.
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
def trap(f, a, b, n):
    h = (b - a) / n; ys = [f(a + i * h) for i in range(n + 1)]
    return 0.5 * h * (ys[0] + ys[-1] + 2 * sum(ys[1:-1]))
sec = lambda x: 1 / cos(x)

# antiderivatives
chk("a", lambda x: 1.5 * exp(2 * x) + 4 * x, lambda x: 3 * exp(2 * x) + 4)
chk("b", lambda x: 3 * log(abs(2 * x + 1)), lambda x: 6 / (2 * x + 1))
chk("c", lambda x: -0.25 * cos(4 * x) - 10 * sin(x / 2), lambda x: sin(4 * x) - 5 * cos(x / 2))
chk("d", lambda x: 2 * tan(x / 2), lambda x: sec(x / 2)**2, xs=(0.3, 0.9, 1.4))
chk("(1+e^x)^2", lambda x: x + 2 * exp(x) + 0.5 * exp(2 * x), lambda x: (1 + exp(x))**2)
chk("x2+1 / x", lambda x: 0.5 * x * x + log(x), lambda x: (x * x + 1) / x)
# definite
eq("a", 0.5 * (exp(2 * log(2)) - 1), 1.5); eq("ln3", log(3), simpson(lambda x: 1 / x, 1, 3), 1e-8)
eq("sec2", tan(pi / 4) - tan(0), 1); eq("sin2x", simpson(lambda x: sin(2 * x), 0, pi / 2), 1, 1e-8)
eq("e2ln2", exp(2 * log(2)), 4)
# identities
for x in (0.3, 1.1, 2.0):
    eq("sin2", sin(x)**2, 0.5 * (1 - cos(2 * x))); eq("cos2", cos(x)**2, 0.5 * (1 + cos(2 * x))); eq("tan2", tan(x)**2, sec(x)**2 - 1)
    eq("sc", sin(x) * cos(x), 0.5 * sin(2 * x)); eq("cos22x", cos(2 * x)**2, 0.5 * (1 + cos(4 * x)))
chk("int sin2", lambda x: x / 2 - sin(2 * x) / 4, lambda x: sin(x)**2)
chk("int cos22x", lambda x: x / 2 + sin(4 * x) / 8, lambda x: cos(2 * x)**2)
chk("int tan2", lambda x: tan(x) - x, lambda x: tan(x)**2, xs=(0.2, 0.6, 1.0))
eq("d", pi / 8 - 0.25, simpson(lambda x: sin(x)**2, 0, pi / 4)); eq("d val", round(pi / 8 - 0.25, 4), 0.1427)
# area, volume
eq("area", sf(0.5 * log(5)), 0.805); eq("area num", simpson(lambda x: 1 / (2 * x + 1), 0, 2), 0.5 * log(5), 1e-8)
eq("vol", sf(pi * pi / 2), 4.93); eq("vol num", pi * simpson(lambda x: sin(x)**2, 0, pi), pi * pi / 2, 1e-8)
# users
N = lambda t: 25000 * exp(0.2 * t) - 5000
eq("N0", N(0), 20000); eq("N5", round(N(5)), 62957); eq("N5 3sf", sf(N(5)), 63000); chk("N'", N, lambda t: 5000 * exp(0.2 * t), xs=(1.0, 3.0))
# exam
eq("area R", simpson(lambda x: 3 / (2 * x + 1), 0, 2), 1.5 * log(5), 1e-8)
eq("vol R", pi * simpson(lambda x: 9 / (2 * x + 1)**2, 0, 2), 18 * pi / 5, 1e-8); eq("0.4", -1 / 10 + 1 / 2, 0.4); eq("9*.4", 9 * 0.4, 3.6)
# trapezium
f = lambda x: exp(x * x)
eq("trap e^x2", round(trap(f, 0, 1, 4), 4), 1.4907, 1e-4); eq("trap sf", sf(trap(f, 0, 1, 4), 4), 1.491, 1e-3)
for x, y in zip((0, .25, .5, .75, 1), (1, 1.064494, 1.284025, 1.755055, 2.718282)): eq("ord", f(x), y, 1e-6)
eq("11.92543", 1 + 2.718282 + 2 * (1.064494 + 1.284025 + 1.755055), 11.925430, 1e-5); eq("*.125", 0.125 * 11.92543, 1.4907, 1e-4)
eq("true", simpson(f, 0, 1), 1.463, 1e-3)
assert all((2 + 4 * x * x) * exp(x * x) > 0 for x in (0, .5, 1))
eq("trap ln", sf(trap(log, 1, 3, 4), 4), 1.282, 1e-3); eq("5.1284", 1.098612 + 2 * (0.405465 + 0.693147 + 0.916291), 5.128418, 1e-5)
eq("true ln", 3 * log(3) - 2, 1.296, 1e-3); assert trap(log, 1, 3, 4) < 3 * log(3) - 2
ys = [0, sqrt(2) / 2, 1, sqrt(2) / 2, 0]; eq("sin trap", sf(trap(sin, 0, pi, 4)), 1.90); eq("4.8284", 2 * (sqrt(2) + 1), 4.8284, 1e-4); assert trap(sin, 0, pi, 4) < 2
# 1/(x^2+a^2)
eq("atan1", atan(1), pi / 4)
chk("4+x2", lambda x: 0.5 * atan(x / 2), lambda x: 1 / (4 + x * x))
chk("3+2x2", lambda x: atan(sqrt(2 / 3) * x) / sqrt(6), lambda x: 1 / (3 + 2 * x * x))

# try
chk("T1a", lambda x: -2 * exp(-2 * x), lambda x: 4 * exp(-2 * x)); chk("T1b", lambda x: 5 / 3 * log(abs(3 * x - 1)), lambda x: 5 / (3 * x - 1), xs=(0.9, 1.7))
chk("T1c", lambda x: 1.5 * sin(2 * x + 1), lambda x: 3 * cos(2 * x + 1)); chk("T1d", lambda x: tan(3 * x) / 3 + 2 * x, lambda x: sec(3 * x)**2 + 2, xs=(0.1, 0.3, 0.4))
chk("T2a", lambda x: 0.5 * exp(2 * x) + 2 * exp(x) + x, lambda x: (exp(x) + 1)**2); chk("T2b", lambda x: x * x - 3 * log(x), lambda x: (2 * x * x - 3) / x)
eq("T3a", (exp(3) - 1) / 3, simpson(lambda x: exp(3 * x), 0, 1), 1e-7); eq("T3b", 3 * log(5 / 2), simpson(lambda x: 3 / x, 2, 5), 1e-8); eq("T3c", 0.5, simpson(sin, 0, pi / 3), 1e-9)
chk("T4a", lambda x: x / 2 + sin(2 * x) / 4, lambda x: cos(x)**2); eq("T4b", pi / 4, simpson(lambda x: sin(3 * x)**2, 0, pi / 2), 1e-8)
eq("T5b", 4 - pi, simpson(lambda x: 4 * tan(x)**2, 0, pi / 4), 1e-8)
eq("T6", sf(trap(lambda x: 1 / x, 1, 2, 4), 3), 0.697); eq("T6 sum", 1.5 + 2 * (0.8 + 0.666667 + 0.571429), 5.576190, 1e-5); eq("T6 val", 0.125 * 5.576190, 0.69702, 1e-5)
assert trap(lambda x: 1 / x, 1, 2, 4) > log(2)
eq("T7", pi * simpson(lambda x: exp(x), 0, 2), pi * (e * e - 1), 1e-7)
V = lambda t: 16000 * exp(-0.25 * t) + 4000; eq("V0", V(0), 20000); eq("V4", round(V(4), 2), 9886.07); eq("V4 sf", sf(V(4)), 9890); chk("V'", V, lambda t: -4000 * exp(-0.25 * t), xs=(1.0, 2.0))
chk("T9a", lambda x: 2 * atan(x / 3), lambda x: 6 / (9 + x * x)); eq("T9b", pi / (4 * sqrt(3)), simpson(lambda x: 1 / (3 + x * x), 0, sqrt(3)), 1e-8)
g = lambda x: sqrt(1 + x * x)
eq("T10", sf(trap(g, 0, 2, 4)), 2.98); eq("T10 sum", 1 + 2.236068 + 2 * (1.118034 + 1.414214 + 1.802776), 11.906116, 1e-5); eq("T10 val", 0.25 * 11.906116, 2.9765, 1e-4)
assert all((1 + x * x)**-1.5 > 0 for x in (0, 1, 2))
# quiz
chk("Q1", lambda x: exp(4 * x) / 4, lambda x: exp(4 * x), xs=(0.2, 0.5)); chk("Q2", lambda x: -cos(3 * x) / 3, lambda x: sin(3 * x))
eq("Q5", pi / 4, simpson(lambda x: 1 / (1 + x * x), 0, 1), 1e-9)
print("ok")
