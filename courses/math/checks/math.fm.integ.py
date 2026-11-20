# checks/math.fm.integ.py: recomputes every number in Further integration: hyperbolic and inverse forms.
# Standard library only: Simpson's rule and finite differences confirm each antiderivative and value.
from math import (sinh, cosh, tanh, exp, log, sqrt, sin, cos, tan, atan, asin, asinh, acosh, atanh, pi,
                  isclose)


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def D(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


sech = lambda x: 1 / cosh(x)
cosech = lambda x: 1 / sinh(x)
coth = lambda x: 1 / tanh(x)
I = lambda f, a, b, n=4000: simpson(f, a, b, n)
S = 1e-7  # tolerance for Simpson checks

# warm-up
eq("w1", D(lambda x: log(x * x + 3), 1.3), 2 * 1.3 / (1.3 ** 2 + 3), 1e-6)
eq("w2", D(lambda x: 0.5 * atan(x / 2), 0.9), 1 / (0.9 ** 2 + 4), 1e-6)
for x in (0.4, 1.5):
    eq("w3", cosh(x) ** 2, 0.5 * (1 + cosh(2 * x)))

# integrals of hyperbolic functions: derivative checks
for x in (0.3, 1.2):
    eq("antiderivs sech2", D(tanh, x), sech(x) ** 2, 1e-6)
    eq("antideriv cosech2", D(lambda u: -coth(u), x), cosech(x) ** 2, 1e-6)
    eq("antideriv tanh", D(lambda u: log(cosh(u)), x), tanh(x), 1e-6)
    eq("antideriv coth", D(lambda u: log(abs(sinh(u))), x), coth(x), 1e-6)
    eq("eg a", D(lambda u: 1.5 * sinh(2 * u) - 2 * cosh(u / 2), x), 3 * cosh(2 * x) - sinh(x / 2), 1e-6)
# eg b, c
eq("eg b", I(lambda x: sinh(2 * x), 0, 1), 0.5 * (cosh(2) - 1), S)
eq("eg b val", sf(0.5 * (cosh(2) - 1), 3), 1.38)
eq("cosh ln3", cosh(log(3)), 5 / 3)
eq("eg c", I(tanh, 0, log(3)), log(5 / 3), S)
# cosh^2
v = 0.5 * log(2) + 15 / 32
eq("cosh2 int", I(lambda x: cosh(x) ** 2, 0, log(2)), v, S)
eq("sinh 2ln2", sinh(2 * log(2)), 15 / 8)
eq("cosh2 val", sf(v, 4), 0.8153, 1e-4)
eq("cosh2 bound", cosh(log(2)) ** 2, 1.5625)
assert 0.69 < v < 1.08
eq("bound lo", sf(log(2), 2), 0.69)
eq("bound hi", sf(1.5625 * log(2), 3), 1.08)
# sinh^3
for x in (0.5, 1.4):
    eq("sinh3", D(lambda u: cosh(u) ** 3 / 3 - cosh(u), x), sinh(x) ** 3, 1e-6)
# x cosh x
eq("xcosh", I(lambda x: x * cosh(x), 0, 1), 1 - exp(-1), S)
eq("xcosh d", D(lambda x: x * sinh(x) - cosh(x), 0.7), 0.7 * cosh(0.7), 1e-6)
eq("sinh1-cosh1", sinh(1) - cosh(1), -exp(-1))
eq("xcosh val", sf(1 - exp(-1), 3), 0.632)
# cable area
area = I(lambda x: 25 * cosh(x / 25) - 19, -15, 15)
eq("area", area, 1250 * sinh(0.6) - 570, 1e-6)
eq("area 4sf", sf(area, 4), 225.8)
eq("area 2x", 2 * (625 * sinh(0.6) - 285), area)

# standard forms
for x in (0.3, 1.1):
    a = 2.5
    eq("sin-1 form", D(lambda u: asin(u / a), x * 0.9), 1 / sqrt(a * a - (x * 0.9) ** 2), 1e-6)
    eq("sinh-1 form", D(lambda u: asinh(u / a), x), 1 / sqrt(x * x + a * a), 1e-6)
    eq("sinh-1 log form", asinh(x / a), log((x + sqrt(x * x + a * a)) / a))
for x in (3.0, 4.5):
    a = 2.5
    eq("cosh-1 form", D(lambda u: acosh(u / a), x), 1 / sqrt(x * x - a * a), 1e-6)
    eq("cosh-1 log form", acosh(x / a), log((x + sqrt(x * x - a * a)) / a))
# eg a,b,c
for x in (0.3, 0.7):
    eq("9-4x2", D(lambda u: 0.5 * asin(2 * u / 3), x), 1 / sqrt(9 - 4 * x * x), 1e-6)
eq("eg b int", I(lambda x: 1 / sqrt(x * x + 9), 0, 2), asinh(2 / 3), S)
eq("eg b log", asinh(2 / 3), log((2 + sqrt(13)) / 3))
eq("eg b val", sf(asinh(2 / 3), 3), 0.625)
eq("eg c int", I(lambda x: 1 / sqrt(x * x - 4), 3, 5), acosh(5 / 2) - acosh(3 / 2), 1e-7)
eq("cosh-1 5/2", acosh(2.5), log(2.5 + sqrt(21) / 2))
eq("cosh-1 3/2", acosh(1.5), log(1.5 + sqrt(5) / 2))
eq("eg c log", acosh(2.5) - acosh(1.5), log((5 + sqrt(21)) / (3 + sqrt(5))))
cval = log((5 + sqrt(21)) / (3 + sqrt(5)))
eq("eg c val", sf(cval, 3), 0.604)
# sinh sub proof
for u in (0.3, 1.6):
    a = 1.7
    eq("sqrt root", sqrt((a * sinh(u)) ** 2 + a * a), a * cosh(u))
# tanh-1 two ways
eq("1/(1-x2)", I(lambda x: 1 / (1 - x * x), 0, 0.5), 0.5 * log(3), 1e-7)
eq("atanh half", atanh(0.5), 0.5 * log(3))
# partial fractions
for x in (0.2, 0.6):
    eq("pf", 1 / (1 - x * x), 0.5 * (1 / (1 - x) + 1 / (1 + x)))

# completing the square
for x in (1.5, 3.0):
    eq("x2+2x", x * x + 2 * x, (x + 1) ** 2 - 1)
    eq("cosh-1(x+1)", D(lambda u: acosh(u + 1), x), 1 / sqrt(x * x + 2 * x), 1e-6)
    eq("log form", acosh(x + 1), log(x + 1 + sqrt(x * x + 2 * x)))
for x in (-1.0, 0.3, 1.0):
    eq("5-4x-x2", 5 - 4 * x - x * x, 9 - (x + 2) ** 2)
    eq("x2-2x+5", x * x - 2 * x + 5, (x - 1) ** 2 + 4)
eq("pi/2 exact", asin(1) - asin(0), pi / 2)
eq("sq b", I(lambda x: 1 / sqrt(x * x - 2 * x + 5), 1, 3), log(1 + sqrt(2)), S)
eq("asinh 1", asinh(1), log(1 + sqrt(2)))
# linear numerator
for x in (0.2, 1.4):
    eq("split", x + 3, 0.5 * (2 * x + 2) + 2)
    F = lambda u: sqrt(u * u + 2 * u + 5) + 2 * asinh((u + 1) / 2)
    eq("split antideriv", D(F, x), (x + 3) / sqrt(x * x + 2 * x + 5), 1e-6)
    eq("split parts", (x + 1) / sqrt(x * x + 2 * x + 5) + 2 / sqrt(x * x + 2 * x + 5), (x + 3) / sqrt(x * x + 2 * x + 5))
    eq("split 2nd", D(lambda u: 2 * asinh((u + 1) / 2), x), 2 / sqrt(x * x + 2 * x + 5), 1e-6)

# sqrt integrals
for x in (0.4, 1.0):
    a = 1.8
    G1 = lambda u: 0.5 * (u * sqrt(a * a - u * u) + a * a * asin(u / a))
    G2 = lambda u: 0.5 * (u * sqrt(u * u + a * a) + a * a * asinh(u / a))
    eq("int sqrt a2-x2", D(G1, x), sqrt(a * a - x * x), 1e-6)
    eq("int sqrt x2+a2", D(G2, x), sqrt(x * x + a * a), 1e-6)
    eq("proof sum", sqrt(a * a - x * x) - x * x / sqrt(a * a - x * x) + a * a / sqrt(a * a - x * x), 2 * sqrt(a * a - x * x))
for x in (2.5, 4.0):
    a = 1.8
    G3 = lambda u: 0.5 * (u * sqrt(u * u - a * a) - a * a * acosh(u / a))
    eq("int sqrt x2-a2", D(G3, x), sqrt(x * x - a * a), 1e-6)
# x = 2 sinh u eg
val = 2 * asinh(0.5) + sqrt(5) / 2
eq("sqrt int", I(lambda x: sqrt(x * x + 4), 0, 1), val, S)
eq("u1", asinh(0.5), log((1 + sqrt(5)) / 2))
eq("cosh u1", sqrt(1 + 0.25), sqrt(5) / 2)
eq("sinh2u1", 2 * 0.5 * sqrt(5) / 2, sqrt(5) / 2)
eq("val 3sf", sf(val, 3), 2.08)
eq("sqrt5", sqrt(5), 2.24, 5e-3)
# window
yv = lambda y: 2 * sqrt(2.25 - y * y)
Aw = I(yv, 0.9, 1.5, 200000)
eq("window num", Aw, 2.25 * (pi / 2 - asin(0.6)) - 1.08, 1e-4)
eq("window top", sf(2.25 * pi / 2, 4), 3.534)
eq("window bottom", sf(0.9 * 1.2 + 2.25 * asin(0.6), 4), 2.528, 1e-3)
eq("window 1.448", sf(2.25 * asin(0.6), 4), 1.448, 1e-3)
eq("window area", sf(Aw, 3), 1.01)
eq("window whole", sf(pi * 1.5 ** 2, 3), 7.07)
eq("sqrt(2.25-.81)", sqrt(2.25 - 0.81), 1.2)
# tower
At = I(lambda y: 2 * sqrt(100 + 4 * y * y), 0, 15)
eq("tower formula", At, 2 * (15 * sqrt(250) + 25 * asinh(3)), 1e-5)
eq("tower 565", sf(At, 3), 565)
eq("sqrt250", sf(sqrt(250), 4), 15.81, 1e-2)
eq("asinh3", sf(asinh(3), 4), 1.818, 1e-3)
eq("asinh3 log", asinh(3), log(3 + sqrt(10)))
eq("237.2", sf(15 * sqrt(250), 4), 237.2, 1e-1)
eq("45.46", sf(25 * asinh(3), 4), 45.46, 1e-2)
eq("width 63.2", sf(2 * sqrt(1000), 3), 63.2)
eq("avg width", sf(At / 15, 2), 38)
# x^2/sqrt(x^2+1)
v2 = 0.5 * sqrt(2) - 0.5 * log(1 + sqrt(2))
eq("x2/sqrt", I(lambda x: x * x / sqrt(x * x + 1), 0, 1), v2, S)
eq("x2/sqrt 3sf", sf(v2, 3), 0.266)
for u in (0.4, 1.1):
    eq("sinh2u identity", 0.25 * sinh(2 * u) - 0.5 * u, 0.5 * sinh(u) * cosh(u) - 0.5 * u)
    eq("D", D(lambda w: 0.25 * sinh(2 * w) - 0.5 * w, u), sinh(u) ** 2, 1e-6)

# parts twice
for x in (0.3, 1.2):
    eq("exp sin antideriv", D(lambda u: 0.5 * exp(u) * (sin(u) - cos(u)), x), exp(x) * sin(x), 1e-6)
eq("exp sin 0..pi", I(lambda x: exp(x) * sin(x), 0, pi), 0.5 * (exp(pi) + 1), 1e-6)
eq("exp sin val", sf(0.5 * (exp(pi) + 1), 3), 12.1)
# sinh-1 by parts
v3 = log(1 + sqrt(2)) + 1 - sqrt(2)
eq("asinh parts", I(asinh, 0, 1), v3, S)
eq("asinh parts val", sf(v3, 3), 0.467)
for x in (0.4, 1.3):
    eq("asinh anti", D(lambda u: u * asinh(u) - sqrt(u * u + 1), x), asinh(x), 1e-6)
# t = tan x/2
v4 = pi / (3 * sqrt(3))
eq("t sub", I(lambda x: 1 / (2 + cos(x)), 0, pi / 2), v4, S)
eq("t sub int", I(lambda t: 2 / (3 + t * t), 0, 1), v4, S)
for x in (0.3, 1.0):
    t = tan(x / 2)
    eq("cos in t", cos(x), (1 - t * t) / (1 + t * t))
    eq("dt/dx", 0.5 * (1 + t * t), 1 / (2 / (1 + t * t)))
    eq("2+cos", 2 + cos(x), (3 + t * t) / (1 + t * t))
eq("tan pi/4", tan(pi / 4), 1)
eq("t eg val", 2 / sqrt(3) * (pi / 6), v4)

# spot the error
eq("sinh4", sf(4 + sinh(4), 3), 31.3)
good = 2 * log(1 + sqrt(2)) + 2 * sqrt(2)
eq("good", I(lambda x: sqrt(x * x + 4), 0, 2), good, S)
eq("good 3sf", sf(good, 3), 4.59)
eq("sinh2u", 2 * 1 * sqrt(2), 2 * sqrt(2))
eq("standard", 0.5 * (2 * sqrt(8) + 4 * asinh(1)), good)

# try
for x in (0.4, 1.0):
    eq("t1a", D(lambda u: 2 / 3 * cosh(3 * u) + 2 * sinh(u / 2), x), 2 * sinh(3 * x) + cosh(x / 2), 1e-6)
    eq("t1b", D(lambda u: 0.25 * tanh(4 * u), x), sech(4 * x) ** 2, 1e-6)
eq("t2", I(lambda x: sinh(x) ** 2, 0, log(2)), 15 / 32 - 0.5 * log(2), S)
eq("acosh2", acosh(2), log(2 + sqrt(3)))
for x in (0.3, 1.1):
    eq("t5", D(lambda u: 0.5 * asinh(2 * u / 3), x), 1 / sqrt(4 * x * x + 9), 1e-6)
    eq("t6", D(lambda u: asinh((u - 3) / 2), x + 3), 1 / sqrt((x + 3) ** 2 - 6 * (x + 3) + 13), 1e-6)
    eq("t6 sq", (x + 3) ** 2 - 6 * (x + 3) + 13, x * x + 4)
eq("t7", I(lambda x: 1 / (x * x - 1), 2, 3), 0.5 * log(1.5), S)
eq("t7 pf", 0.5 * (log(1 / 2) - log(1 / 3)), 0.5 * log(1.5))
eq("t8", I(lambda x: x / sqrt(x * x + 9), 0, 4), sqrt(25) - 3, S)
eq("t9", I(lambda x: sqrt(9 - x * x), 0, 3, 100000), 9 * pi / 4, 1e-4)
eq("t10 sub", D(lambda u: 0.5 * (u * sqrt(u * u - 9) - 9 * acosh(u / 3)), 4.5), sqrt(4.5 ** 2 - 9), 1e-6)
for u in (0.4, 1.2):
    eq("t10 mid", 9 * (0.25 * sinh(2 * u) - 0.5 * u), 4.5 * (sinh(u) * cosh(u) - u))

# exam practice
eq("q1b", sinh(log(3)), 4 / 3)
eq("q1b int", I(cosh, 0, log(3)), 4 / 3, S)
eq("q1a", D(lambda u: 3 * cosh(2 * u), 0.5), 6 * sinh(1.0), 1e-6)
for x in (0.3, 0.9):
    eq("q2a", D(lambda u: 0.5 * asin(2 * u / 5), x), 1 / sqrt(25 - 4 * x * x), 1e-6)
    eq("q2b", D(lambda u: asinh(3 * u / 4) / 3, x), 1 / sqrt(9 * x * x + 16), 1e-6)
q3 = acosh(4) - acosh(2)
eq("q3", I(lambda x: 1 / sqrt(x * x - 6 * x + 8), 5, 7), q3, 1e-7)
eq("q3 log", q3, log((4 + sqrt(15)) / (2 + sqrt(3))))
eq("q3 val", sf(q3, 3), 0.746)
for x in (4.0, 6.0):
    eq("q3 sq", x * x - 6 * x + 8, (x - 3) ** 2 - 1)
q4 = 10 / 9 - 0.5 * log(3)
eq("q4", I(lambda x: sinh(x) ** 2, 0, log(3)), q4, S)
eq("q4 sinh", sinh(2 * log(3)), 40 / 9)
q5 = pi / 12 + sqrt(3) / 2 - 1
eq("q5", I(asin, 0, 0.5), q5, S)
for x in (0.2, 0.6):
    eq("q5 anti", D(lambda u: u * asin(u) + sqrt(1 - u * u), x), asin(x), 1e-6)
q6 = sqrt(2) - sqrt(5) / 2
eq("q6", I(lambda x: 1 / (x * x * sqrt(x * x + 1)), 1, 2), q6, S)
eq("q6 coth", 1 / (sinh(asinh(2)) / cosh(asinh(2))), sqrt(5) / 2)
eq("q6 coth1", cosh(asinh(1)) / sinh(asinh(1)), sqrt(2))
for x in (1.2, 2.4):
    eq("q6 anti", D(lambda u: -sqrt(u * u + 1) / u, x), 1 / (x * x * sqrt(x * x + 1)), 1e-6)
q7a = 0.5 * atan(0.5)
eq("q7a", I(lambda x: 1 / (5 + 3 * cos(x)), 0, pi / 2), q7a, S)
eq("q7a t", I(lambda t: 1 / (4 + t * t), 0, 1), q7a, S)
for x in (0.3, 1.0):
    t = tan(x / 2)
    eq("q7a denom", 5 + 3 * cos(x), (8 + 2 * t * t) / (1 + t * t))
q7b = 0.5 * (exp(pi / 2) - 1)
eq("q7b", I(lambda x: exp(x) * cos(x), 0, pi / 2), q7b, S)
for x in (0.3, 1.0):
    eq("q7b anti", D(lambda u: 0.5 * exp(u) * (sin(u) + cos(u)), x), exp(x) * cos(x), 1e-6)
eq("q8a", I(lambda x: 1 / sqrt(x * x + 9), 0, 4), log(3), S)
eq("q8a asinh", asinh(4 / 3), log(3))
eq("q8a sqrt", sqrt(16 / 9 + 1), 5 / 3)
q8b = pi / 3 * atan(4 / 3)
eq("q8b", pi * I(lambda x: 1 / (x * x + 9), 0, 4), q8b, S)
eq("q8b val", sf(q8b, 3), 0.971)

# stretch 1: ellipse
s1 = 15 * (pi / 2 - asin(0.6) - 0.5 * (24 / 25))
eq("ellipse area", 2 * I(lambda x: 0.6 * sqrt(25 - x * x), 3, 5, 200000), s1, 1e-4)
eq("ellipse 3sf", sf(s1, 3), 6.71)
eq("sin 2t0", 2 * 0.6 * 0.8, 24 / 25)
eq("theta0", sf(asin(0.6), 4), 0.6435, 1e-4)
eq("1.5708-0.6435-0.48", sf(1.5708 - 0.6435 - 0.48, 4), 0.4473, 1e-4)
eq("15*", sf(15 * (1.5708 - 0.6435 - 0.48), 3), 6.71)
eq("coef", 6 / 5 * 25 * 0.5, 15)
# stretch 2: sech
for x in (0.4, 1.3):
    eq("sech anti", D(lambda u: atan(sinh(u)), x), sech(x), 1e-6)
    eq("sech form", sech(x), cosh(x) / (1 + sinh(x) ** 2))
eq("sech int", I(sech, 0, log(3)), atan(4 / 3), S)
eq("sinh ln3", sinh(log(3)), 4 / 3)
eq("sech val", sf(atan(4 / 3), 3), 0.927)

# quiz
for x in (0.4, 1.0):
    eq("quiz 9-4x2", D(lambda u: 0.5 * asin(2 * u / 3), x * 0.5), 0.5 * (2 / 3) / sqrt(1 - 4 * (x * 0.5) ** 2 / 9), 1e-6)
eq("quiz limit", sinh(asinh(1)), 1)

# added examples
for a_ in (0.3, 1.2):
    eq("diff sin-1 proof", D(lambda u: asin(u / 2.5), a_), 1 / sqrt(1 - a_ * a_ / 6.25) / 2.5, 1e-6)
    eq("a sqrt", 2.5 * sqrt(1 - a_ * a_ / 6.25), sqrt(6.25 - a_ * a_))
w1 = log((2 + sqrt(5)) / (1 + sqrt(2)))
eq("sq2", I(lambda x: 1 / sqrt(x * x + 2 * x + 2), 0, 1), w1, S)
eq("sq2 val", sf(w1, 3), 0.562)
eq("asinh2", asinh(2), log(2 + sqrt(5)))
w2 = log(8 / (1 + sqrt(17)))
eq("u sub", I(lambda x: exp(x) / sqrt(exp(2 * x) + 16), 0, log(3)), w2, S)
eq("u sub val", sf(w2, 3), 0.446)
eq("asinh 1/4", asinh(0.25), log((1 + sqrt(17)) / 4))
eq("asinh 3/4", asinh(0.75), log(2))
eq("u sub combine", log(2) - log((1 + sqrt(17)) / 4), w2)
for x in (0.5, 1.5):
    eq("12+4x-x2", 12 + 4 * x - x * x, 16 - (x - 2) ** 2)
    eq("choose b", D(lambda u: 2 * sqrt(u * u + 4) - asinh(u / 2), x), (2 * x - 1) / sqrt(x * x + 4), 1e-6)
    eq("choose e", cosh(3 * x) ** 2, 0.5 * (1 + cosh(6 * x)))
eq("quarter circle", I(lambda x: sqrt(9 - x * x), 0, 3, 200000), 9 * pi / 4, 1e-3)

# more worked examples
V = pi / 2 + pi / 4 * sinh(2)
eq("vase", pi * I(lambda x: cosh(x) ** 2, 0, 1), V, S)
eq("vase 3sf", sf(V, 3), 4.42)
eq("vase bounds", sf(pi * 1.54 ** 2, 2), 7.5)
eq("cosh1", sf(cosh(1), 3), 1.54)
for x in (0.4, 1.3):
    d_ = D(lambda u: u * sqrt(u * u + 1), x)
    eq("hence a", d_, 2 * sqrt(x * x + 1) - 1 / sqrt(x * x + 1), 1e-6)
    eq("hence b", D(lambda u: 0.5 * (u * sqrt(u * u + 1) + asinh(u)), x), sqrt(x * x + 1), 1e-6)
    eq("hence split", sqrt(x * x + 1) + x * x / sqrt(x * x + 1), sqrt(x * x + 1) + (x * x + 1) / sqrt(x * x + 1) - 1 / sqrt(x * x + 1))
v5 = pi / 12 - sqrt(3) / 8
eq("sin sub", I(lambda x: x * x / sqrt(1 - x * x), 0, 0.5), v5, S)
eq("sin sub val", sf(v5, 3), 0.0453)
eq("asin half", asin(0.5), pi / 6)
eq("sin sub inner", 0.5 * (pi / 6 - 0.5 * sqrt(3) / 2), v5)
eq("mean height", sf(area / 30, 3), 7.53)

print("ok")
