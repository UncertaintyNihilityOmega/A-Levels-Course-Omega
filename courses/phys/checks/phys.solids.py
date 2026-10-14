# checks/phys.solids.py: recomputes every number in the Deformation of solids chapter.
from math import isclose, sqrt, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("warm W", 30 * 0.50, 15)
eq("warm p", 600 / 0.020, 3.0e4)
A = pi * (0.25e-3)**2
eq("warm A", sf(A, 2), 2.0e-7); eq("warm A raw", sf(A, 3), 1.96e-7, 1e-12)

# Spring example
F = 0.50 * g
eq("F", sf(F, 2), 4.9); eq("F raw", sf(F, 4), 4.905)
x = F / 40
eq("x", sf(x, 2), 0.12); eq("x raw", sf(x, 3), 0.123, 1e-9)
eq("compressed", 200 * 0.050, 10)

# Series/parallel
eq("par", 60 + 90, 150)
eq("ser", sf(60 * 90 / (60 + 90), 3), 36)

# Steel wire
A = pi * (0.20e-3)**2
eq("A steel", sf(A, 3), 1.26e-7, 1e-12)
sig = 25 / A
eq("sigma", sf(sig, 2), 2.0e8); eq("sigma raw", sf(sig, 3), 1.99e8, 1e5)
eps = 2.5e-3 / 2.5
eq("eps", eps, 1.0e-3)
E = sig / eps
eq("E steel", sf(E, 2), 2.0e11)

# Copper wire extension
A = pi * (0.25e-3)**2
xx = 15 * 3.0 / (1.96e-7 * 1.2e11)
eq("x copper", sf(xx, 2), 1.9e-3, 1e-12)
eq("strain", sf(xx / 3.0, 2), 6.4e-4, 1e-12)

# Copper experiment
E = 13e3 * 1.80 / 1.96e-7
eq("E copper", sf(E, 2), 1.2e11)
eq("E copper (full A)", sf(13e3 * 1.80 / A, 2), 1.2e11)

# Energy stored, spring
Fk = 0.50 * g; xk = Fk / 40
eq("E spring", sf(0.5 * Fk * xk, 2), 0.30)
eq("E spring kx2", sf(0.5 * 40 * xk**2, 2), 0.30)
eq("E doubled", sf(4 * 0.5 * Fk * xk, 2), 1.2)

# Rubber band trapezia
xs = [0, 2.0, 4.0, 6.0, 8.0, 10.0]; Fs = [0, 1.5, 2.5, 3.2, 4.0, 5.5]
terms = [0.5 * (Fs[i] + Fs[i + 1]) for i in range(5)]
eq("terms", sum(terms), 13.95, 1e-9)
eq("band", sf(0.020 * sum(terms), 2), 0.28)

# Spot the error
Aw = pi * (0.40e-3)**2
eq("spot wrong A", sf(Aw, 3), 5.03e-7, 1e-12)
eq("spot wrong sigma", sf(25 / Aw, 2), 5.0e7)
Ar = pi * (0.20e-3)**2
eq("spot right sigma", sf(25 / Ar, 2), 2.0e8)
eq("spot ratio", Aw / Ar, 4.0)

# Try easy
eq("t1", 3.0 / 0.060, 50)
eq("t2", 1.0e-3 / 2.0, 5.0e-4)
eq("t3", 80 / 4.0e-6, 2.0e7)
eq("t4", 0.5 * 100 * 0.10**2, 0.50); eq("t4 Fx", 100 * 0.10 * 0.10, 0.10 * 10)
eq("t5", 1 / (1 / 80 + 1 / 80), 40)
eq("t6", 2.0e11 * 1.5e-3, 3.0e8)

# Exam practice
eq("e2", sf(30 / (pi * (0.40e-3)**2), 2), 6.0e7)
eq("e3 k", 6.0 / 0.025, 240)
eq("e3 E", sf(0.5 * 240 * 0.040**2, 2), 0.19)
grad = 27 / 4.0e-3
eq("e4 grad", grad, 6750)
A = pi * (0.16e-3)**2
eq("e4 A", sf(A, 3), 8.04e-8, 1e-12)
eq("e4 E", sf(grad * 2.40 / A, 2), 2.0e11)
tr = [0.5 * (0 + 2.0), 0.5 * (2.0 + 3.5), 0.5 * (3.5 + 5.5), 0.5 * (5.5 + 9.5)]
eq("e6 sum", sum(tr), 15.75)
eq("e6 E", sf(0.010 * sum(tr), 2), 0.16)

# Two wires
As = pi * (0.30e-3)**2; Ac = pi * (0.15e-3)**2
ratio = (1.0 / 2.0) * (As / Ac) * (2.0e11 / 1.2e11)
eq("e7 ratio", sf(ratio, 2), 3.3)
eq("e7 ratio parts", (0.50 * 4.0 * 1.67), 3.34, 1e-9)
xs_ = 60 * 2.0 / (As * 2.0e11); xc_ = 60 * 1.0 / (Ac * 1.2e11)
eq("e7 xs", sf(xs_ * 1e3, 2), 2.1); eq("e7 xc", sf(xc_ * 1e3, 2), 7.1)
eq("e7 total", sf((xs_ + xc_) * 1e3, 2), 9.2)

# Mass onto spring
m, h, k = 0.50, 0.30, 120
eq("e8 v", sf(sqrt(2 * g * h), 2), 2.4)
eq("e8 half k", 0.5 * k, 60)
eq("e8 b", sf(m * g, 2), 4.9); eq("e8 c", sf(m * g * h, 2), 1.5)
xr = (4.9 + sqrt(4.9**2 + 4 * 60 * 1.5)) / (2 * 60)
eq("e8 x", sf(xr, 2), 0.20)
xe = (m * g + sqrt((m * g)**2 + 4 * 60 * m * g * h)) / 120
eq("e8 x exact", sf(xe, 2), 0.20)

# Stretch 1: uncertainty
L, d, Fl, ext = 2.500, 0.400e-3, 25.0, 2.50e-3
E = 4 * Fl * L / (pi * d**2 * ext)
eq("s1 E", sf(E, 3), 1.99e11, 1e8)
pF, pL, pd, px = 0.2 / 25.0, 0.005 / 2.5, 0.005 / 0.400, 0.05 / 2.50
eq("s1 pF", pF * 100, 0.8); eq("s1 pL", pL * 100, 0.2); eq("s1 pd", pd * 100, 1.25); eq("s1 px", px * 100, 2.0)
tot = (pF + pL + 2 * pd + px) * 100
eq("s1 total", tot, 5.5)
eq("s1 abs", sf(E * tot / 100, 2), 1.1e10)

# Stretch 2: springs
kp = 60 + 90
kt = kp * 100 / (kp + 100)
eq("s2 k", kt, 60)
eq("s2 x", 12 / kt, 0.20)
eq("s2 pair", 12 / kp, 0.080); eq("s2 third", 12 / 100, 0.12)
eq("s2 sum", 12 / kp + 12 / 100, 0.20)
eq("s2 E", 0.5 * 12 * 0.20, 1.2)

# Quiz
eq("quiz E", 0.5 * 100 * 0.10**2, 0.50)
eq("quiz 4", 2**2, 4)

# Review additions: stress-strain graph, energy on unloading
eq("ss steel", 1.0e8 / 0.50e-3, 2.0e11, 1)
eq("ss copper", 1.2 * 0.50, 0.60)
eq("ss copper E", 0.60e8 / 0.50e-3, 1.2e11, 1)
eq("try ss", sf(1.8e8 / 1.5e-3, 2), 1.2e11, 1)
Er = 0.5 * 60 * (6.0 - 3.6) * 1e-3
eq("unload rec", Er, 0.072)
eq("unload diss 2sf", sf(0.25 - Er, 2), 0.18)
assert Er / 0.25 < 1 / 3

# Review fix: femur in compression
sig = 700 / 3.0e-4
eq("femur sigma", sf(sig, 2), 2.3e6, 1e3); eq("femur sigma raw", sf(sig, 3), 2.33e6, 1e3)
eps = sig / 1.8e10
eq("femur eps", sf(eps, 2), 1.3e-4, 1e-9); eq("femur eps raw", sf(eps, 3), 1.30e-4, 1e-9)
eq("femur x", sf(eps * 0.45, 2), 5.8e-5, 1e-9); eq("femur x mm", sf(eps * 0.45 * 1e3, 2), 0.058, 1e-6)
assert 1e-4 * 1 == 1e-4

print("ok")
