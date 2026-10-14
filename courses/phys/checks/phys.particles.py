# checks/phys.particles.py: recomputes every number in the Particle physics chapter.
from math import isclose
from fractions import Fraction as F

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

e = 1.60e-19
u = 1.66e-27
mp = 1.67e-27
me = 9.11e-31
k = 8.99e9

# Warm-up
eq("warm electrons", 8.0e-19 / e, 5)
eq("warm nm", 0.1e-9, 1e-10, 1e-20)
eq("warm v", 2.0 * 3.0 / (2.0 + 1.0), 2.0)

# Sizes
eq("size ratio", 1e-10 / 1e-15, 1e5, 1)
eq("pea atom", 5e-3 * 1e5, 500)

# Particle table
eq("electron mass in u", sf(me / u, 2), 5.5e-4, 1e-9)
eq("proton mass in u", sf(mp / u, 3), 1.01)
eq("proton / electron", sf(mp / me, 2), 1800, 1e-6)

# Nuclide counts
eq("U neutrons", 235 - 92, 143)
eq("Fe neutrons", 56 - 26, 30)
eq("Fe3+ electrons", 26 - 3, 23)
eq("C-14 neutrons", 14 - 6, 8)
eq("C-13 neutrons", 13 - 6, 7)

# Alpha energy share
eq("energy ratio", 222 / 4, 55.5)
eq("fraction", sf(222 / (222 + 4), 2), 0.98)

# Decay equations (A and Z balance)
def balance(parent, products):
    A = sum(p[0] for p in products)
    Z = sum(p[1] for p in products)
    assert (parent[0], parent[1]) == (A, Z), f"unbalanced {parent} -> {products}"
balance((226, 88), [(222, 86), (4, 2)])
balance((14, 6), [(14, 7), (0, -1), (0, 0)])
balance((18, 9), [(18, 8), (0, 1), (0, 0)])
balance((238, 92), [(234, 90), (4, 2)])
balance((234, 90), [(234, 91), (0, -1), (0, 0)])
balance((19, 8), [(19, 9), (0, -1), (0, 0)])
balance((210, 84), [(206, 82), (4, 2)])
balance((239, 93), [(239, 94), (0, -1), (0, 0)])
balance((15, 8), [(15, 7), (0, 1), (0, 0)])
n += 9
# the faulty reaction: 238U -> 236Th + alpha
assert (238, 92) != (236 + 4, 90 + 2)
eq("faulty A", 236 + 4, 240)
eq("true daughter A", 238 - 4, 234)
eq("Po-210 daughter A", 210 - 4, 206)
eq("Po-210 daughter Z", 84 - 2, 82)

# Thorium-232 example
eq("Th A", 232 - 4, 228)
eq("Th Z after alpha", 90 - 2, 88)
eq("Th Z final", 90 - 2 + 2, 90)
eq("Th neutrons start", 232 - 90, 142)
eq("Th neutrons end", 228 - 90, 138)

# Mass of alpha
ma = 4.00 * u
eq("alpha mass", sf(ma, 3), 6.64e-27, 1e-32)
qa = 2 * e
eq("alpha q/m", sf(qa / ma, 2), 4.8e7, 1e4)
eq("proton q/m", sf(e / mp, 2), 9.6e7, 1e4)
eq("q/m ratio", sf((e / mp) / (qa / ma), 2), 2.0)
eq("C-12 mass", sf(12 * u, 3), 1.99e-26, 1e-30)

# Quarks
up, down = F(2, 3), F(-1, 3)
eq("proton charge", float(up + up + down), 1)
eq("neutron charge", float(up + down + down), 0)
eq("uds", float(up + down + down), 0)
eq("sss", float(3 * down), -1)
eq("anti-proton", float(-up - up - down), -1)
eq("u sbar", float(up - down), 1)
eq("pi- d ubar", float(down - up), -1)
eq("u dbar", float(up - down), 1)
eq("uus", float(up + up + down), 1)
eq("sbar", float(-down), 1 / 3, 1e-12)
# beta decays
eq("beta- d -> u e nu", float(up + (-1) + 0), float(down), 1e-12)
eq("beta+ u -> d e+ nu", float(down + 1 + 0), float(up), 1e-12)

# Decay chain
dA = 238 - 206
na = dA // 4
eq("alpha decays", na, 8)
eq("Z after alphas", 92 - 2 * na, 76)
nb = 82 - (92 - 2 * na)
eq("beta decays", nb, 6)
eq("A change", dA, 32)

# Closest approach
E = 5.0e6 * e
eq("5 MeV in J", E, 8.0e-13, 1e-19)
r = k * (2 * e) * (79 * e) / 8.0e-13
eq("closest approach", sf(r, 2), 4.5e-14, 1e-16)
eq("times nuclear radius", sf(4.5e-14 / 7e-15, 1), 6)

# Deflection paragraph (REVIEW P5-P6): specific charges and their ratio
eq("e/me", sf(e / me, 3), 1.76e11, 1e8)
eq("alpha Q/m", sf(2 * e / (4.00 * u), 2), 4.8e7, 1e5)
eq("ratio about 3600", round((e / me) / (2 * e / (4.00 * u)), -2), 3600, 1)

print("ok")
