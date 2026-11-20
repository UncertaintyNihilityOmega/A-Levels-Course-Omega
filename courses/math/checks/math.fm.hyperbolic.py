# checks/math.fm.hyperbolic.py: recomputes every number in Hyperbolic functions.
# Standard library only.
from math import sinh, cosh, tanh, exp, log, sqrt, isclose, asinh, acosh, atanh


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def dp(x, n):
    return round(x, n)


# definitions and values
for x in (-2.0, -0.7, 0.3, 1.9):
    eq("def sinh", sinh(x), (exp(x) - exp(-x)) / 2)
    eq("def cosh", cosh(x), (exp(x) + exp(-x)) / 2)
    eq("def tanh", tanh(x), (exp(x) - exp(-x)) / (exp(x) + exp(-x)))
    eq("e^x", exp(x), cosh(x) + sinh(x))
    eq("e^-x", exp(-x), cosh(x) - sinh(x))
    eq("cosh-sinh", cosh(x) ** 2 - sinh(x) ** 2, 1)
    eq("1-tanh2", 1 - tanh(x) ** 2, 1 / cosh(x) ** 2)
    eq("coth2-1", 1 / tanh(x) ** 2 - 1, 1 / sinh(x) ** 2)
    eq("sinh2x", sinh(2 * x), 2 * sinh(x) * cosh(x))
    eq("cosh2x a", cosh(2 * x), cosh(x) ** 2 + sinh(x) ** 2)
    eq("cosh2x b", cosh(2 * x), 2 * cosh(x) ** 2 - 1)
    eq("cosh2x c", cosh(2 * x), 1 + 2 * sinh(x) ** 2)
    eq("tanh2x", tanh(2 * x), 2 * tanh(x) / (1 + tanh(x) ** 2))
    # table: parity
    eq("sinh odd", sinh(-x), -sinh(x))
    eq("cosh even", cosh(-x), cosh(x))
    eq("tanh odd", tanh(-x), -tanh(x))
    # tanh form dividing by e^x
    eq("tanh alt", tanh(x), (1 - exp(-2 * x)) / (1 + exp(-2 * x)))
eq("sinh0", sinh(0), 0); eq("cosh0", cosh(0), 1); eq("tanh0", tanh(0), 0)

# table
for x, s, c, t in [(-1, -1.175, 1.543, -0.7616), (1, 1.175, 1.543, 0.7616), (2, 3.627, 3.762, 0.9640)]:
    eq(f"tab sinh {x}", sf(sinh(x), 4), s, 1e-3)
    eq(f"tab cosh {x}", sf(cosh(x), 4), c, 1e-3)
    eq(f"tab tanh {x}", sf(tanh(x), 4), t, 1e-4)

# compound angle formulas
for A, B in [(0.4, 1.1), (-0.8, 0.5), (1.3, 0.2)]:
    eq("sinh(A+B)", sinh(A + B), sinh(A) * cosh(B) + cosh(A) * sinh(B))
    eq("sinh(A-B)", sinh(A - B), sinh(A) * cosh(B) - cosh(A) * sinh(B))
    eq("cosh(A+B)", cosh(A + B), cosh(A) * cosh(B) + sinh(A) * sinh(B))
    eq("cosh(A-B)", cosh(A - B), cosh(A) * cosh(B) - sinh(A) * sinh(B))
    eq("tanh(A+B)", tanh(A + B), (tanh(A) + tanh(B)) / (1 + tanh(A) * tanh(B)))
    eq("tanh(A-B)", tanh(A - B), (tanh(A) - tanh(B)) / (1 - tanh(A) * tanh(B)))
    # proof expansion
    e = exp
    lhs1 = (e(A) - e(-A)) * (e(B) + e(-B))
    lhs2 = (e(A) + e(-A)) * (e(B) - e(-B))
    eq("expand1", lhs1, e(A + B) + e(A - B) - e(-A + B) - e(-A - B))
    eq("expand2", lhs2, e(A + B) - e(A - B) + e(-A + B) - e(-A - B))
    eq("sum", lhs1 + lhs2, 2 * e(A + B) - 2 * e(-A - B))
    eq("sum/4", (lhs1 + lhs2) / 4, sinh(A + B))

# cable eg: y = 25 cosh(x/25) - 19
y = lambda x: 25 * cosh(x / 25) - 19
eq("cable low", y(0), 6)
eq("cosh 0.6", cosh(0.6), 1.18547, 1e-5)
eq("cable pole", sf(y(15), 4), 10.64, 1e-2)
eq("sag", sf(y(15) - 6, 3), 4.64, 1e-9)
c = 27 / 25
xx = 25 * acosh(c)
eq("cosh-1 1.08 formula", acosh(c), log(c + sqrt(c * c - 1)))
eq("0.3974", sf(acosh(c), 4), 0.3974, 1e-9)
# conversion eg
for x in (-0.6, 0.0, 1.4):
    eq("conv1", 5 * exp(x) - 3 * exp(-x), 2 * cosh(x) + 8 * sinh(x))
    eq("conv2", 6 * cosh(x) + 2 * sinh(x), 4 * exp(x) + 2 * exp(-x))
# sketch eg: y = 1 + 2 tanh x
eq("sk y0", 1 + 2 * tanh(0), 1)
xi = -atanh(0.5)
eq("sk xint", 1 + 2 * tanh(xi), 0)
eq("sk xint ln", xi, -0.5 * log(3))
eq("sk xint val", sf(xi, 3), -0.549)
eq("sk asym", 1 + 2 * tanh(30), 3)
# tanh(A+B) via division
for A, B in [(0.5, 0.9), (-1.0, 0.3)]:
    eq("tanhAB div", sinh(A + B) / cosh(A + B),
       (sinh(A) / cosh(A) + sinh(B) / cosh(B)) / (1 + sinh(A) * sinh(B) / (cosh(A) * cosh(B))))
for x in (0.3, -1.4, 2.1):
    eq("sinh2x/(1+cosh2x)", sinh(2 * x) / (1 + cosh(2 * x)), tanh(x))
# wave eg (g = 10)
g, lam = 10, 60
from math import pi
c2deep = g * lam / (2 * pi)
eq("wave deep c2", sf(c2deep, 4), 95.49, 1e-2)
eq("wave deep c", sf(sqrt(c2deep), 3), 9.77)
eq("wave arg", sf(2 * pi * 10 / lam, 5), 1.0472, 1e-4)
eq("wave tanh", sf(tanh(2 * pi * 10 / lam), 4), 0.7807, 1e-4)
eq("wave c2", sf(c2deep * tanh(2 * pi * 10 / lam), 4), 74.55, 1e-2)
eq("wave c", sf(sqrt(c2deep * tanh(2 * pi * 10 / lam)), 3), 8.63)
eq("0.95^2", 0.95 ** 2, 0.9025)
eq("wave atanh", sf(atanh(0.9025), 5), 1.4855, 1e-4)
eq("wave atanh log", 0.5 * log(1.9025 / 0.0975), atanh(0.9025))
dwave = lam * atanh(0.9025) / (2 * pi)
eq("wave d", sf(dwave, 3), 14.2)
eq("wave check", sqrt(c2deep * tanh(2 * pi * dwave / lam)), 0.95 * sqrt(c2deep))
eq("x=9.93", sf(xx, 3), 9.93, 1e-9)
eq("cable 8m", y(xx), 8)

# cosh x = 5/3 eg
s = sqrt(25 / 9 - 1)
eq("sinh 4/3", s, 4 / 3)
eq("tanh 4/5", s / (5 / 3), 4 / 5)
eq("sinh 2x 40/9", 2 * s * 5 / 3, 40 / 9)
eq("cosh2x 41/9", 25 / 9 + 16 / 9, 41 / 9)
eq("e^x=3", 5 / 3 + 4 / 3, 3)
eq("check 2x", (41 / 9) ** 2 - (40 / 9) ** 2, 1)
x0 = log(3)
eq("x from e^x", cosh(x0), 5 / 3)
eq("sinh2x num", sinh(2 * x0), 40 / 9)

# inverse functions
for v in (-2.5, 0.0, 0.7, 3.2):
    eq("sinh-1 log", asinh(v), log(v + sqrt(v * v + 1)))
for v in (1.0, 1.5, 4.0):
    eq("cosh-1 log", acosh(v), log(v + sqrt(v * v - 1)))
    other = v - sqrt(v * v - 1)
    eq("product 1", (v + sqrt(v * v - 1)) * other, 1)
    eq("other root is -cosh-1", log(other), -acosh(v))
for v in (-0.8, 0.0, 0.5):
    eq("tanh-1 log", atanh(v), 0.5 * log((1 + v) / (1 - v)))
    eq("tanh via e^2y", tanh(atanh(v)), (exp(2 * atanh(v)) - 1) / (exp(2 * atanh(v)) + 1))
# exact values
eq("sinh-1 3/4", asinh(0.75), log(2))
eq("sqrt 3/4", sqrt(9 / 16 + 1), 5 / 4)
eq("cosh-1 2", acosh(2), log(2 + sqrt(3)))
eq("tanh-1 1/2", atanh(0.5), 0.5 * log(3))
eq("sinh ln2", sinh(log(2)), 3 / 4)
eq("cosh y=2 pm", cosh(-log(2 + sqrt(3))), 2)

# equations
# 4 sinh x + 3 cosh x = 4
t = (4 + sqrt(23)) / 7
xs = log(t)
eq("eq1 root", 4 * sinh(xs) + 3 * cosh(xs), 4)
eq("eq1 value", sf(xs, 3), 0.228)
eq("eq1 check sinh", sf(sinh(xs), 4), 0.2304, 1e-4)
eq("eq1 check cosh", sf(cosh(xs), 4), 1.0261, 1e-4)
assert (4 - sqrt(23)) / 7 < 0
eq("92", 64 + 28, 92)
eq("sqrt92", sqrt(92), 2 * sqrt(23))
# cosh 2x = 3 sinh x + 1
x1 = asinh(1.5)
eq("eq2 x=0", cosh(0), 3 * sinh(0) + 1)
eq("eq2 root", cosh(2 * x1), 3 * sinh(x1) + 1)
eq("eq2 log", x1, log((3 + sqrt(13)) / 2))
eq("eq2 val", sf(x1, 3), 1.19)
eq("sqrt9/4+1", sqrt(9 / 4 + 1), sqrt(13) / 2)
# 3 cosh x = 2 + 4 sinh^2 x
cc = (3 + sqrt(41)) / 8
xc = acosh(cc)
eq("eq3 root", 3 * cosh(xc), 2 + 4 * sinh(xc) ** 2)
eq("eq3 -root", 3 * cosh(-xc), 2 + 4 * sinh(-xc) ** 2)
eq("eq3 c", sf(cc, 4), 1.175, 1e-3)
eq("eq3 x", sf(xc, 4), 0.5839, 1e-4)
assert (3 - sqrt(41)) / 8 < 0
eq("disc 41", 9 + 32, 41)
# skydiver
v = lambda t: 40 * tanh(0.25 * t)
tt = 2 * log(7)
eq("skydiver t", v(tt), 30)
eq("tanh-1 3/4", atanh(0.75), 0.5 * log(7))
eq("t=3.89", sf(tt, 3), 3.89)
# spot the error
eq("sp cosh", sqrt(1 + 9 / 16), 5 / 4)
eq("sp 17/8", 25 / 16 + 9 / 16, 17 / 8)
eq("sp wrong", 25 / 16 - 9 / 16, 1)
eq("sp check", cosh(2 * log(2)), 17 / 8)
eq("sp x", asinh(0.75), log(2))

# try
eq("sinh1.5", sf(sinh(1.5), 4), 2.129, 1e-3)
eq("cosh1.5", sf(cosh(1.5), 4), 2.352, 1e-3)
eq("tanh1.5", sf(tanh(1.5), 4), 0.9051, 1e-4)
eq("5.534", sf(cosh(1.5) ** 2, 4), 5.534, 1e-3)
eq("4.534", sf(sinh(1.5) ** 2, 4), 4.534, 1e-3)
eq("sinh=12/5", cosh(asinh(12 / 5)), 13 / 5)
eq("tanh 12/13", tanh(asinh(12 / 5)), 12 / 13)
eq("x=ln5", asinh(12 / 5), log(5))
for x in (0.4, -1.1, 2.0):
    eq("sinh3x", sinh(3 * x), 4 * sinh(x) ** 3 + 3 * sinh(x))
    eq("cosh3x", cosh(3 * x), 4 * cosh(x) ** 3 - 3 * cosh(x))
    eq("(c+s)^n", (cosh(x) + sinh(x)) ** 5, cosh(5 * x) + sinh(5 * x))
    eq("sinh 3x expansion", 2 * sinh(x) * (1 + sinh(x) ** 2) + sinh(x) + 2 * sinh(x) ** 3, sinh(3 * x))
eq("sinh-1 5/12", asinh(5 / 12), log(3 / 2))
eq("sqrt 25/144+1", sqrt(25 / 144 + 1), 13 / 12)
eq("cosh-1 17/8", acosh(17 / 8), log(4))
eq("sqrt 289/64 -1", sqrt(289 / 64 - 1), 15 / 8)
eq("tanh x=3/5", atanh(3 / 5), log(2))
eq("e^x=5", log(5), asinh(12 / 5))
for x in (0, log(4)):
    eq("5c-3s=5", 5 * cosh(x) - 3 * sinh(x), 5)
eq("2sinh2-3cosh", 2 * sinh(log(2 + sqrt(3))) ** 2 - 3 * cosh(log(2 + sqrt(3))), 2 * 3 - 6)  # sinh^2 = 3, cosh 2
eq("2c2-3c-2", (2 * 2 + 1) * (2 - 2), 0)
eq("3 sub", 2 * (2 * 2 - 1) - 3 * 2 - 0, 0)  # 2(cosh^2 -1) -3cosh at cosh=2 -> 6-6

# exam practice
eq("q1 cosh", sqrt(1 + 25 / 144), 13 / 12)
eq("q1 tanh", (5 / 12) / (13 / 12), 5 / 13)
eq("q1 e^x", 13 / 12 + 5 / 12, 3 / 2)
for x in (0.3, 1.7):
    eq("q2", 2 * sinh(x) * cosh(x), (exp(2 * x) - exp(-2 * x)) / 2)
# q3: 7 cosh x - 3 sinh x = 8
for sign in (1, -1):
    t3 = 2 + sign * sqrt(6) / 2
    assert t3 > 0
    x3 = log(t3)
    eq("q3", 7 * cosh(x3) - 3 * sinh(x3), 8)
eq("q3 quad", (8 + sqrt(24)) / 4, 2 + sqrt(6) / 2)
eq("q3 reduce", 7 / 2 - 3 / 2, 2)
eq("q3 reduce2", 7 / 2 + 3 / 2, 5)
# q4: cosh 2x - 5 sinh x = 7
xs4 = []
for sg in (1, -1):
    s4 = (5 + sg * sqrt(73)) / 4
    x4 = asinh(s4)
    eq("q4", cosh(2 * x4) - 5 * sinh(x4), 7)
    xs4.append(x4)
eq("q4 x1", sf(xs4[0], 3), 1.93)
eq("q4 x2", sf(xs4[1], 3), -0.798)
eq("q4 disc", 25 + 48, 73)
# q5
eq("q5a", asinh(8 / 15), log(5 / 3))
eq("q5a sqrt", sqrt(64 / 225 + 1), 17 / 15)
eq("q5b", acosh(13 / 5), log(5))
eq("q5b sqrt", sqrt(169 / 25 - 1), 12 / 5)
# q6
t6 = log(19) / 0.6
eq("q6", 30 * tanh(0.3 * t6), 27)
eq("q6 t", sf(t6, 3), 4.91)
eq("q6 tanh-1", atanh(0.9), 0.5 * log(19))
# q7
eq("q7b", cosh(3 * acosh(sqrt(3.5))), 11 * sqrt(3.5))
eq("q7 form", log(sqrt(3.5) + sqrt(2.5)), acosh(sqrt(3.5)))
eq("q7 sqrt", sqrt(3.5) ** 2 - 1, 2.5)
eq("q7 4C2", 4 * 3.5 - 3, 11)
# q8
for r in (1, 2, 5):
    eq("q8a", 2 * sinh(0.5) * cosh(r), sinh(r + 0.5) - sinh(r - 0.5))
for n in (3, 10):
    s_direct = sum(cosh(r) for r in range(1, n + 1))
    eq("q8b", s_direct, (sinh(n + 0.5) - sinh(0.5)) / (2 * sinh(0.5)), 1e-6)
s10 = sum(cosh(r) for r in range(1, 11))
eq("q8c", sf(s10, 3), 17400, 1e-9)

# stretch 1: 5 cosh x - 4 sinh x
alpha = log(3)
eq("tanh alpha", tanh(alpha), 4 / 5)
eq("atanh 4/5", atanh(0.8), 0.5 * log(9 / 5 / (1 / 5)))
eq("R", sqrt(25 - 16), 3)
for x in (-1.0, 0.5, 2.2):
    eq("R cosh form", 5 * cosh(x) - 4 * sinh(x), 3 * cosh(x - alpha))
for x in (0, 2 * log(3)):
    eq("stretch1 root", 5 * cosh(x) - 4 * sinh(x), 5)
eq("cosh(ln3)", cosh(log(3)), 5 / 3)
eq("ln(5/3+4/3)", log(5 / 3 + 4 / 3), log(3))
eq("sinh alpha", sinh(alpha), 4 / 3)
eq("R coshalpha", 3 * cosh(alpha), 5)
eq("R sinh alpha", 3 * sinh(alpha), 4)
# stretch 2: t = tanh(x/2)
for x in (-1.2, 0.4, 2.0):
    t_ = tanh(x / 2)
    eq("s2 sinh", sinh(x), 2 * t_ / (1 - t_ * t_))
    eq("s2 cosh", cosh(x), (1 + t_ * t_) / (1 - t_ * t_))
tr = (-5 + sqrt(41)) / 8
assert abs(tr) < 1 and abs((-5 - sqrt(41)) / 8) > 1
xr = log((1 + tr) / (1 - tr))
eq("s2 root", 3 * cosh(xr) + 5 * sinh(xr), 5)
eq("s2 closed", xr, log((5 + sqrt(41)) / 8))
eq("s2 val", sf(xr, 3), 0.354)
eq("s2 quad", 3 + 5, 8)

# reciprocal eg: tanh x = 5/13
xr5 = atanh(5 / 13)
eq("sech", 1 / cosh(xr5), 12 / 13)
eq("coth", 1 / tanh(xr5), 13 / 5)
eq("cosech", 1 / sinh(xr5), 12 / 5)
eq("sech2", 1 - 25 / 169, 144 / 169)
eq("sinh 5/12", sinh(xr5), 5 / 12)
eq("coth2-1", 169 / 25 - 1, 144 / 25)
# tanh 2x = 4/5
x25 = 0.5 * log(3)
eq("t2x", tanh(2 * x25), 4 / 5)
eq("t2x atanh", atanh(4 / 5), log(3))
eq("t2x 1/2", tanh(x25), 1 / 2)
eq("t2x quad", 2 * 0.5 ** 2 - 5 * 0.5 + 2, 0)
eq("t2x quad2", 2 * 2 ** 2 - 5 * 2 + 2, 0)
eq("t2x formula", 2 * 0.5 / (1 + 0.25), 4 / 5)

# extra exam practice
for x_, y_ in [(0.3, 0.5), (-0.6, 0.2)]:
    eq("tanh-1 sum", atanh(x_) + atanh(y_), atanh((x_ + y_) / (1 + x_ * y_)))
for sg in (1, -1):
    t_ = 3 + sg * sqrt(6)
    assert t_ > 0
    x_ = log(t_)
    eq("q intersect", 2 * cosh(x_), 3 + sinh(x_))
    eq("q intersect t", t_ ** 2 - 6 * t_ + 3, 0)
eq("q y1", sf(2 * cosh(log(3 + sqrt(6))), 3), 5.63)
eq("q y2", sf(2 * cosh(log(3 - sqrt(6))), 3), 2.37)
eq("q half", 1 / 2, 0.5)

print("ok")
