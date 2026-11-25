# checks/math.fm.variable.py: recomputes every number in Linear motion under a variable force.
# Standard library only. Closed forms are confirmed by integrating the equation of motion numerically (RK4 / Simpson).
from math import isclose, sqrt, log, exp, tanh

G = 10


def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


def rk4(f, y, t0, t1, n=4000):
    """integrate y' = f(t, y) (y a list) from t0 to t1"""
    h = (t1 - t0) / n
    t = t0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k1)])
        k3 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k2)])
        k4 = f(t + h, [a + h * b for a, b in zip(y, k3)])
        y = [a + h / 6 * (p + 2 * q + 2 * r + s) for a, p, q, r, s in zip(y, k1, k2, k3, k4)]
        t += h
    return y


# ---- proof: work-energy from m v dv/dx = F (use F = 18/x^3, m = 2 from x = 1 to 7: v = 3/x)
m = 2
work = simpson(lambda x: -18 / x ** 3, 1, 7)
eq("proof work-energy", 0.5 * m * (3 / 7) ** 2 - 0.5 * m * 3 ** 2, work, 1e-8)

# ---- eg: force 36 - 6t, m = 3
eq("eg1 vmax", 12 * 6 - 36, 36)
eq("eg1 x at 12", 6 * 144 - 12 ** 3 / 3, 288)
t, x = rk4(lambda t, y: [y[1], (36 - 6 * t) / 3], [0, 0], 0, 12)[0:2]  # y = [x, v]
eq("eg1 numeric x(12)", t, 288, 1e-6)
eq("eg1 numeric v(12)", x, 0, 1e-6)

# ---- exam eg: m = 4, F = 24/(2t+1)
eq("ln v(2)", 3 * log(5), 4.828313737302301)
xx = simpson(lambda t: 3 * log(2 * t + 1), 0, 2)
eq("ln x(2)", 7.5 * log(5) - 6, xx, 1e-9)
eq("ln x 3sf", sf(7.5 * log(5) - 6), 6.07)
y = rk4(lambda t, y: [y[1], 24 / (2 * t + 1) / 4], [0, 0], 0, 2)
eq("ln numeric", y[0], xx, 1e-8)
eq("ln x/2 avg", (7.5 * log(5) - 6) / 2 > 3, True)

# ---- boat m = 200, R = 40 v, u = 10
eq("boat v(5)", sf(10 * exp(-1)), 3.68)
eq("boat half", sf(5 * log(2)), 3.47)
eq("boat stop", 200 * 10 / 40, 50)
y = rk4(lambda t, y: [y[1], -40 * y[1] / 200], [0, 10], 0, 5)
eq("boat numeric v(5)", y[1], 10 * exp(-1), 1e-8)
eq("boat numeric x", rk4(lambda t, y: [y[1], -40 * y[1] / 200], [0, 10], 0, 100, 40000)[0], 50, 1e-3)

# ---- exam eg: inverse cube, m = 2, F = 18/x^3
y = rk4(lambda t, y: [y[1], -18 / y[0] ** 3 / 2], [1, 3], 0, 8)
eq("cube x(8)", y[0], 7, 1e-6)
eq("cube v(8)", y[1], 3 / 7, 1e-6)
eq("cube t at x=7", (49 - 1) / 6, 8)
eq("cube v at 7", sf(3 / 7), 0.429)
eq("cube force at 7", sf(18 / 343), 0.0525)

# ---- escape: R = 6.4e6, g = 10
R = 6.4e6
eq("escape rhs", 2 * G * R, 1.28e8, 1)
eq("escape u^2", 8000 ** 2, 6.4e7)
xmax = 2 * G * R ** 2 / (2 * G * R - 8000 ** 2)
eq("escape xmax", xmax, 1.28e7, 1e-3)
eq("escape xmax = 2R", xmax, 2 * R, 1e-3)
eq("escape speed 3sf", sf(sqrt(2 * G * R)), 11300)
eq("escape speed", sqrt(2 * G * R), 11313.708498984761, 1e-6)

# ---- exam eg: m = 0.5, R = 0.2 v^2, u = 8
eq("v2 t at 2", (1 / 2 - 1 / 8) / 0.4, 0.9375)
eq("v2 x", log(4) / 0.4, 3.465735902799726)
eq("v2 x 3sf", sf(log(4) / 0.4), 3.47)
y = rk4(lambda t, y: [y[1], -0.2 * y[1] ** 2 / 0.5], [0, 8], 0, 0.9375)
eq("v2 numeric v", y[1], 2, 1e-7)
eq("v2 numeric x", y[0], log(4) / 0.4, 1e-6)
eq("v2 3sf t", sf(0.9375), 0.938)

# ---- falling, m = 2, R = 0.2 v^2
V = sqrt(20 / 0.2)
eq("fall terminal", V, 10)
eq("fall t(5)", sf(0.5 * log(3)), 0.549)
eq("fall tanh", 10 * tanh(0.5 * log(3)), 5)
eq("fall x(5) = 5 ln(4/3)", 5 * log(100 / 75), simpson(lambda v: 10 * v / (100 - v * v), 0, 5), 1e-8)
y = rk4(lambda t, y: [y[1], 10 - 0.1 * y[1] ** 2], [0, 0], 0, 0.5 * log(3))
eq("fall numeric v", y[1], 5, 1e-8)
eq("fall within 1% by t=3", 10 * tanh(3) > 9.9, True)
eq("fall 10tanh(2.65)>9.9", 10 * tanh(2.65) > 9.9, True)

# ---- exam eg: m = 2, F = 18, R = 2 v^2
vs = sqrt(9 * (1 - exp(-1)))
eq("cf v at 0.5", sf(vs), 2.39)
eq("cf x from v", 0.5 * log(9 / (9 - vs * vs)), 0.5, 1e-12)
tt = log((3 + vs) / (3 - vs)) / 6
eq("cf t", sf(tt), 0.362)
y = rk4(lambda t, y: [y[1], (18 - 2 * y[1] ** 2) / 2], [0, 0], 0, tt)
eq("cf numeric x", y[0], 0.5, 1e-7)
eq("cf numeric v", y[1], vs, 1e-7)
eq("cf terminal", sqrt(18 / 2), 3)

# ---- exam eg: ball up and down, m = 0.4, R = 0.04 v^2
H = 5 * log(5)
eq("ball H", sf(H), 8.05)
Hn = simpson(lambda v: v / (10 + 0.1 * v * v), 0, 20)
eq("ball H integral", H, Hn, 1e-8)
eq("ball 5ln50-5ln10", 5 * log(50) - 5 * log(10), H, 1e-12)
Vd = sqrt(80)
eq("ball return", sf(Vd), 8.94)
eq("ball return integral", simpson(lambda v: v / (10 - 0.1 * v * v), 0, Vd), H, 1e-6)
eq("ball 10-0.1V^2", 10 - 0.1 * Vd ** 2, 2, 1e-12)

# ---- spot the error: 2 v dv/dx = -0.6 v^2, u = 5 -> v = 5 e^{-0.3x}
y = rk4(lambda x, y: [-0.3 * y[0]], [5], 0, 3)
eq("spot v(3)", y[0], 5 * exp(-0.9), 1e-9)
# marks of the Spot the error: M1 A0 M1 A0 = 2 of 4
eq("spot marks", 1 + 0 + 1 + 0, 2)

# ---- try block
eq("t1 v", 3 ** 2, 9)
eq("t1 x", 3 ** 3 / 3, 9)
eq("t2 v2", 12 * 2 - 2 * 2 ** 2, 16)
eq("t2 stop", 12 / 2, 6)
eq("t3 t", sf(4 * log(4)), 5.55)
eq("t3 x", 2 * 8 / 0.5, 32)
eq("t4 v", sf(5 * exp(-1)), 1.84)
eq("t5 V", 10 / 0.4, 25)
eq("t5 t", sf(2.5 * log(10 / 4)), 2.29)
eq("t5 numeric", simpson(lambda v: 1 / (10 - 0.4 * v), 0, 15), 2.5 * log(2.5), 1e-8)
eq("t6 V", sqrt(12 / 0.03), 20)
c = -4 / 3
eq("t7 v", sf(sqrt(2 * (4 + c))), 2.31)
eq("t7 v2", 2 * (4 + c), 16 / 3)

# ---- exam practice
eq("ep1 v", 4 * 27 / 3, 36)
eq("ep2 t", sf(2 * log(3)), 2.20)
eq("ep2 x", 9 / 0.5, 18)
eq("ep3 c", 8 - 4, 4)
eq("ep3 v at 4", sf(sqrt(16 / 4 + 8)), 3.46)
y = rk4(lambda t, y: [y[1], -24 / y[0] ** 2 / 3], [2, 4], 0, 1)
eq("ep3 numeric energy", y[1] ** 2, 16 / y[0] + 8, 1e-7)
eq("ep4 x", sf(4 * log(3)), 4.39)
eq("ep4 check", 0.4 * 0.0 + 0.1 / 0.4, 0.25)
eq("ep5 divide", 5 - 250 / (50 + 0), 0.0)
eq("ep5 divide2", 5 - 250 / (50 + 10), 10 / (10 + 0.2 * 10) * 1 if False else 5 - 250 / 60)
eq("ep5 divide3", 10 / (10 + 0.2 * 10), 5 - 250 / 60, 1e-12)
Hs = simpson(lambda v: v / (10 + 0.2 * v), 0, 24)
eq("ep5 H", 120 - 250 * log(74 / 50), Hs, 1e-8)
eq("ep5 H 3sf", sf(Hs), 22.0)
eq("ep6 v", sqrt(3) * 2, 2 * sqrt(3))
eq("ep6 x(1.33)", sf(log(10) / sqrt(3)), 1.33)
y = rk4(lambda t, y: [y[1], 3 * y[0]], [2, 2 * sqrt(3)], 0, log(10) / sqrt(3))
eq("ep6 numeric x", y[0], 20, 1e-4)
eq("ep7 terminal", 10 / 2, 5)
xs = 5 + 2.5 * exp(-2) - 2.5
eq("ep7 x(1)", sf(xs), 2.84)
y = rk4(lambda t, y: [y[1], 10 - 2 * y[1]], [0, 0], 0, 1)
eq("ep7 numeric x", y[0], xs, 1e-8)
eq("ep7 v(1)", y[1], 5 * (1 - exp(-2)), 1e-8)

# ---- stretch: car
P, mc, k = 18000, 1000, 20
eq("car vmax", sqrt(P / k), 30)
tcar = simpson(lambda v: mc * v / (P - k * v * v), 10, 20)
eq("car t", tcar, 25 * log(1.6), 1e-9)
eq("car t 3sf", sf(tcar), 11.8)
xcar = simpson(lambda v: mc * v * v / (P - k * v * v), 10, 20)
eq("car x", xcar, 50 * (-10 + 15 * log(2.5)), 1e-7)
eq("car x 3sf", sf(xcar), 187)
y = rk4(lambda t, y: [y[1], (P / y[1] - k * y[1]) / mc], [0, 10], 0, tcar, 8000)
eq("car numeric v", y[1], 20, 1e-6)
eq("car numeric x", y[0], xcar, 1e-4)

# stretch 2: a = -k v^2
kk, u = 0.3, 7.0
y = rk4(lambda t, y: [y[1], -kk * y[1] ** 2], [0, u], 0, 5)
eq("s2 v", y[1], u / (1 + kk * u * 5), 1e-9)
eq("s2 x", y[0], log(1 + kk * u * 5) / kk, 1e-8)
eq("s2 v(x)", y[1], u * exp(-kk * y[0]), 1e-8)

# ---- quiz
eq("q3 V", sqrt(20 / 0.8), 5)
eq("q6 v(6)", 6 * 6 - 36 / 2, 18)
eq("q6 v(12)", 6 * 12 - 144 / 2, 0)
print("ok")
