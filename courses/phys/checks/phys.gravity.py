# checks/phys.gravity.py: recomputes every number in the Gravitational fields chapter.
from math import isclose, sqrt, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

G = 6.67e-11
M_E, R_E = 5.97e24, 6.37e6
M_M, R_M, D_EM = 7.35e22, 1.74e6, 3.84e8
GM = G * M_E
day = 86400.0

# GM displayed
eq("GM", sf(GM, 3), 3.98e14)

# Warm-up
eq("warm w", sf(2 * pi / (90 * 60), 2), 1.2e-3)
eq("warm Ep", sf(80 * 9.81 * 500, 2), 3.9e5)
eq("warm W", sf(65 * 9.81, 2), 640)

# Newton's law
eq("F EM", sf(G * M_E * M_M / D_EM**2, 3), 1.98e20)
eq("F people", sf(G * 70 * 70 / 1.0**2, 2), 3.3e-7)
eq("weight 70", sf(70 * 9.81, 2), 690)
ratio = 70 * 9.81 / (G * 70 * 70)
assert 1.9e9 < ratio < 2.3e9, ratio          # "about two billion"
eq("sat 3R", sf(8.0 / 9, 2), 0.89)

# g = GM/r^2
eq("g surface", sf(GM / R_E**2, 3), 9.81)
r_iss = R_E + 4.08e5
eq("r ISS", sf(r_iss, 4), 6.778e6)
g_iss = GM / r_iss**2
eq("g ISS", sf(g_iss, 3), 8.67)
eq("g ISS pct", round(g_iss / (GM / R_E**2) * 100), 88)

# near the surface
d1 = (R_E + 1000) / R_E - 1
eq("r change 1 km", sf(d1 * 100, 2), 0.016)
eq("g change 1 km", sf((1 - (R_E / (R_E + 1000))**2) * 100, 2), 0.031)
eq("g change Everest", sf((1 - (R_E / (R_E + 8800))**2) * 100, 2), 0.28)

# plot points
eq("plot k", sf(GM / 1e12, 4), 398.2)
eq("plot surface", sf(398.2 / 6.37**2, 3), 9.81)
eq("plot 2R", sf(398.2 / 12.74**2, 3), 2.45)
eq("plot geo", sf(398.2 / 42.2**2, 2), 0.22)
eq("plot phi surface", sf(-398.2 / 6.37, 3), -62.5)
eq("plot phi geo", sf(-398.2 / 42.2, 2), -9.4)

# orbits: ISS
v_iss = sqrt(GM / r_iss)
eq("v ISS", sf(v_iss, 3), 7.66e3)
T_iss = 2 * pi * r_iss / v_iss
eq("T ISS", sf(T_iss, 3), 5.56e3)
eq("T ISS min", sf(T_iss / 60, 3), 92.6)
eq("orbits per day", sf(day / T_iss, 2), 16)
eq("kepler T ISS", sf(2 * pi * sqrt(r_iss**3 / GM), 3), 5.56e3)

# Jupiter from Io
T_io = 1.77 * day
eq("T Io", sf(T_io, 4), 1.529e5)
eq("M Jupiter", sf(4 * pi**2 * (4.22e8)**3 / (G * T_io**2), 3), 1.90e27)

# Moon period
T_moon = 2 * pi * sqrt(D_EM**3 / GM)
eq("T Moon", sf(T_moon, 3), 2.37e6)
eq("T Moon days", sf(T_moon / day, 3), 27.4)

# Geostationary
T_g = 24 * 3600.0
eq("T geo", T_g, 8.64e4)
r3 = GM * T_g**2 / (4 * pi**2)
eq("r3 geo", sf(r3, 3), 7.53e22)
r_g = r3 ** (1 / 3)
eq("r geo", sf(r_g, 3), 4.22e7)
eq("h geo", sf(r_g - R_E, 3), 3.59e7)
eq("h geo km", sf((r_g - R_E) / 1000, 2), 3.6e4)
eq("v geo", sf(2 * pi * r_g / T_g, 3), 3.07e3)
eq("g geo", sf(GM / r_g**2, 2), 0.22)
eq("signal time", sf(2 * (r_g - R_E) / 3.00e8, 2), 0.24)
eq("geo scale", sf(r_g / R_E, 2), 6.6)

# potential
eq("phi surface", sf(-GM / R_E, 3), -6.25e7)
eq("phi geo (r given as 4.22e7)", sf(-GM / 4.22e7, 3), -9.44e6)

# potential energy change to ISS height
dE = GM * 1000 * (1 / R_E - 1 / r_iss)
eq("dEp ISS", sf(dE, 3), 3.76e9)
eq("mgh ISS", sf(1000 * 9.81 * 4.08e5, 3), 4.00e9)
eq("mgh excess pct", round((1000 * 9.81 * 4.08e5 / dE - 1) * 100), 6)

# satellite to geostationary
dEp = GM * 500 * (1 / R_E - 1 / r_g)
eq("dEp geo", sf(dEp, 3), 2.65e10)
Ek = GM * 500 / (2 * r_g)
eq("Ek geo", sf(Ek, 3), 2.36e9)
eq("total", sf(dEp + Ek, 3), 2.89e10)
eq("sum display", sf(2.65e10 + 2.36e9, 3), 2.89e10)
v_eq = R_E * 2 * pi / T_g
Ek_surf = 0.5 * 500 * v_eq**2
eq("Ek surface", sf(Ek_surf, 1), 5e7)
eq("Ek surface pct", sf(Ek_surf / (dEp + Ek) * 100, 1), 0.2)

# escape speed
eq("escape", sf(sqrt(2 * GM / R_E), 3), 1.12e4)

# Spot the error
r_s = R_E + 6.0e5
eq("spot wrong", sf(GM * 1000 / 6.0e5**2, 2), 1.1e6)
eq("spot r", sf(r_s, 3), 6.97e6)
eq("spot right", sf(GM * 1000 / r_s**2, 2), 8.2e3)
eq("spot weight", sf(1000 * 9.81, 2), 9.8e3)

# Start easy
eq("e3 Moon g", sf(G * M_M / R_M**2, 3), 1.62)
eq("e4 Jupiter g", sf(G * 1.90e27 / (6.99e7)**2, 3), 25.9)
eq("e4 ratio", sf(25.9 / 9.81, 2), 2.6)
eq("e5 v", sf(sqrt(GM / 7.2e6), 2), 7.4e3)
T_y = 365.25 * day
eq("e6 T", sf(T_y, 4), 3.156e7)
eq("e6 M Sun", sf(4 * pi**2 * (1.50e11)**3 / (G * T_y**2), 3), 2.01e30)
eq("e3 ratio", round(1 / (1.62 / 9.81)), 6)

# Exam practice
r4 = R_E + 3.50e5
eq("Q4 r", r4, 6.72e6)
eq("Q4 g", sf(GM / r4**2, 3), 8.82)
GM_Mars = G * 6.42e23
T_ph = 2 * pi * sqrt((9.38e6)**3 / GM_Mars)
eq("Q5 T", sf(T_ph, 3), 2.76e4)
eq("Q5 hours", sf(T_ph / 3600, 3), 7.66)
eq("Q6 r3", sf(3.98e14 * T_g**2 / (4 * pi**2), 3), 7.53e22)
eq("Q6 r", sf((3.98e14 * T_g**2 / (4 * pi**2)) ** (1 / 3), 2), 4.2e7)
m7 = 1200
E1 = -GM * m7 / (2 * 7.0e6)
E2 = -GM * m7 / (2 * 1.40e7)
eq("Q7 E1", sf(E1, 3), -3.41e10)
eq("Q7 E2", sf(E2, 3), -1.71e10)
eq("Q7 dE", sf(E2 - E1, 3), 1.71e10)
eq("Q7 Ek1", sf(-E1, 3), 3.41e10)
eq("Q7 Ek2", sf(-E2, 3), 1.71e10)
q = sqrt(M_M / M_E)
eq("Q8 ratio", sf(q, 3), 0.111)
x = D_EM / (1 + q)
eq("Q8 x", sf(x, 3), 3.46e8)
eq("Q8 1+q", sf(1 + q, 4), 1.111)
# field zero check
assert isclose(M_E / x**2, M_M / (D_EM - x)**2, rel_tol=1e-9)

# Stretch 1: drag
m = 800; r1 = 6.70e6
E1 = -GM * m / (2 * r1)
eq("S1 E1", sf(E1, 3), -2.38e10)
E2 = E1 - 5.0e8
eq("S1 E2", sf(E2, 3), -2.43e10)
r2 = -GM * m / (2 * E2)
eq("S1 r2", sf(r2, 3), 6.56e6)
eq("S1 drop km", round((r1 - r2) / 1000), 138)
v1, v2 = sqrt(GM / r1), sqrt(GM / r2)
eq("S1 v1", sf(v1, 3), 7.71e3)
eq("S1 v2", sf(v2, 3), 7.79e3)
eq("S1 dv", round(v2 - v1), 81)

# Stretch 2: binary stars
M = 1.99e30; d = 3.0e11
v = sqrt(G * M / (2 * d))
eq("S2 v", sf(v, 3), 1.49e4)
Tb = pi * d / v
eq("S2 T", sf(Tb, 2), 6.3e7)
eq("S2 years", sf(Tb / 3.156e7, 2), 2.0)

# Quiz
eq("quiz 1/4", (1 / 2)**2, 0.25)
eq("quiz 2R", 1 / (2**2), 0.25)
eq("quiz Ep", 1 / 2, 0.5)

print("ok")
