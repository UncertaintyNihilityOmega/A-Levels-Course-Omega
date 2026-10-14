# checks/phys.astro.py: recomputes every number in the Astronomy and cosmology chapter.
from math import isclose, sqrt, pi, exp

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# Data
c = 3.00e8
sigma = 5.67e-8
b = 2.9e-3
L_sun, r_sun, d_es = 3.83e26, 6.96e8, 1.50e11
ly = 9.46e15
H0 = 2.3e-18
year = 3.16e7

# Warm-up
eq("warm intensity", 3.0 / 0.50, 6.0)

# Solar constant
F_sun = L_sun / (4 * pi * d_es**2)
eq("solar constant", sf(F_sun, 3), 1.35e3, 1e-9)
# Mars
F_mars = L_sun / (4 * pi * (2.28e11)**2)
eq("mars flux", sf(F_mars, 3), 5.86e2, 1e-9)
eq("mars ratio", sf(2.28 / 1.50, 3), 1.52)
eq("solar 4sf", sf(F_sun, 4), 1.355e3, 1e-9)
eq("mars via ratio", sf(1.355e3 / 1.52**2, 2), 5.9e2, 1e-9)
eq("1.52 squared", sf(1.52**2, 3), 2.31)

# Cepheid
d_c = sqrt(3.0e30 / (4 * pi * 1.2e-12))
eq("cepheid d", sf(d_c, 2), 4.5e20, 1e16)
eq("cepheid d 3sf", sf(d_c, 3), 4.46e20, 1e17)
eq("cepheid ly", sf(d_c / ly, 2), 4.7e4, 1)

# Wien
eq("Wien sun", sf(b / 5.0e-7, 2), 5.8e3, 1e-6)
eq("3000 K peak", sf(b / 3000, 2), 9.7e-7, 1e-12)
eq("3000 K peak nm", sf(b / 3000 * 1e9, 2), 970, 1e-9)
# Planck figure peaks (Wien with 2.898e-3 gives the same to 3 s.f. with b=2.9e-3)
eq("peak 5000", sf(b / 5000 * 1e9, 3), 580)
eq("peak 6000", sf(b / 6000 * 1e9, 3), 483)
eq("peak 7000", sf(b / 7000 * 1e9, 3), 414)

# Kelvin note
eq("5800 K in C", sf(5800 - 273, 2), 5.5e3, 1e-6)

# Stefan-Boltzmann: Sun
L5800 = 4 * pi * sigma * r_sun**2 * 5800**4
eq("L sun from T", sf(L5800, 2), 3.9e26, 1e22)

# Radius example
T = b / 2.9e-7
eq("T 290 nm", T, 1.0e4, 1e-6)
r = sqrt(4.0e28 / (4 * pi * sigma * T**4))
eq("r", sf(r, 2), 2.4e9, 1e6)
eq("r 3sf", sf(r, 3), 2.37e9, 1e7)
eq("r / r_sun", sf(r / r_sun, 2), 3.4)

# Ratios
eq("16", 2**4, 16)
eq("4", 2**2, 4)

# Spot the error
r_half = 1.39e9 / 2
eq("half diameter", r_half, 6.95e8, 1e3)
L_ok = 4 * pi * sigma * r_half**2 * 5800**4
L_bad = 4 * pi * sigma * (1.39e9)**2 * 5800**4
eq("spot good", sf(L_ok, 2), 3.9e26, 1e22)
eq("spot bad", sf(L_bad, 2), 1.6e27, 1e23)
eq("spot factor 4", L_bad / L_ok, 4.0, 1e-9)

# Redshift
dl = 663.0 - 656.3
eq("delta lambda", dl, 6.7, 1e-9)
v = c * dl / 656.3
eq("v galaxy", sf(v, 2), 3.1e6, 1e3)
eq("v galaxy 3sf", sf(v, 3), 3.06e6, 1e3)
eq("v / c percent", sf(v / c * 100, 2), 1.0)
eq("v 0.020", 0.020 * c, 6.0e6, 1e-3)
# redshift strip figure: z = 0.030
for lam, obs in ((656.3, 676.0),):
    eq("strip Halpha", sf(lam * 1.030, 4), obs, 0.05)
eq("strip v", 0.030 * c, 9.0e6, 1e-3)

# Hubble
d_g = v / H0
eq("d galaxy", sf(d_g, 2), 1.3e24, 1e20)
eq("d galaxy ly", sf(d_g / ly, 2), 1.4e8, 1e5)
# Hubble figure: gradient
eq("fig gradient", 2.3e-18 * 1e24 / 1e6, 2.3)
eq("fig line end", 250 - 2.3 * 4 * 22, 47.6, 1e-9)
# age
t = 1 / H0
eq("age s", sf(t, 2), 4.3e17, 1e14)
eq("age yr", sf(t / year, 2), 1.4e10, 1e7)
eq("age 3sf s", sf(t, 3), 4.35e17, 1e14)

# Start easy
eq("e1 F", sf(2.0e27 / (4 * pi * (1.0e17)**2), 2), 1.6e-8, 1e-12)
eq("e2 T", sf(b / 7.25e-7, 2), 4.0e3, 1e-6)
eq("e3 sigma T4", sf(sigma * 6000**4, 2), 7.3e7, 1e3)
eq("e4 L", sf(4 * pi * sigma * (1.4e9)**2 * 5000**4, 2), 8.7e26, 1e22)
eq("e5 v", 0.0050 * c, 1.5e6, 1e-3)
eq("e6 v", H0 * 2.0e24, 4.6e6, 1e-3)
eq("e7 ratio", (4 / 2**2), 1.0)
d_sn = sqrt(1.0e36 / (4 * pi * 2.0e-15))
eq("e9 d", sf(d_sn, 2), 6.3e24, 1e21)
eq("e9 ly", sf(d_sn / ly, 2), 6.7e8, 1e5)

# Exam practice
eq("x3 F", sf(4.0e-9 / 9, 2), 4.4e-10, 1e-13)
eq("x4 T", sf(b / 2.4e-7, 2), 1.2e4, 1e-6)
eq("x5 ratio", (6000 / 3000)**2, 4.0)
dl2 = 491.9 - 486.1
eq("x6 delta", dl2, 5.8, 1e-9)
eq("x6 v", sf(c * dl2 / 486.1, 2), 3.6e6, 1e3)
# Q8
T8 = b / 4.6e-7
eq("x8 T", sf(T8, 2), 6.3e3, 1e-6)
L8 = 4 * pi * (2.5e17)**2 * 1.4e-9
eq("x8 L", sf(L8, 2), 1.1e27, 1e23)
eq("x8 L 5sf", sf(L8, 5), 1.0996e27, 1e22)
r8 = sqrt(L8 / (4 * pi * sigma * T8**4))
eq("x8 r", sf(r8, 2), 9.9e8, 1e6)
eq("x8 r/rsun", sf(r8 / r_sun, 2), 1.4)
eq("x8 T 4sf", sf(T8, 4), 6304, 1e-6)

# Stretch
eq("s1 T ratio", 580 / 290, 2.0)
eq("s1 flux ratio", 2.0**4, 16)
eq("s1 r ratio", 2.0**2, 4.0)
eq("s2 z", (486.4 - 121.6) / 121.6, 3.0, 1e-9)
eq("s2 v", 3.0 * c, 9.0e8, 1e-3)

# Quiz
eq("quiz 2d", 1 / 2**2, 0.25)
eq("quiz T x2", 2**4, 16)

# Exam: redshift, Hubble distance, age
vq = c * (670.1 - 656.3) / 656.3
eq("xh dl", sf(670.1 - 656.3, 3), 13.8, 1e-9)
eq("xh v", sf(vq, 2), 6.3e6, 1e3)
eq("xh d", sf(vq / H0, 2), 2.7e24, 1e22)
eq("xh t s", sf(1 / H0, 3), 4.35e17, 1e14)
eq("xh t yr", sf(1 / H0 / 3.16e7, 2), 1.4e10, 1e7)

print("ok")
