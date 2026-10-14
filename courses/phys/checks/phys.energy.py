# checks/phys.energy.py: recomputes every number in the Work, energy and power chapter.
from math import isclose, sqrt, cos, sin, radians, pi

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("warm v", sf(sqrt(2 * 2.5 * 40), 2), 14)
eq("warm v raw", sf(sqrt(200), 3), 14.1)
eq("warm a", 3000 / 1200, 2.5)
eq("warm comp", 50 * cos(radians(60)), 25, 1e-9)

# Crate
W = 120 * 8.0 * cos(radians(30))
eq("crate", sf(W, 3), 831)
eq("crate 2sf", sf(W, 2), 830)

# Trapezium under F = 20 + 10 s from 0 to 4
eq("F at 4", 20 + 10 * 4, 60)
eq("trap", 0.5 * (20 + 60) * 4.0, 160)

# Climber
eq("climber", sf(65 * g * 450, 3), 2.87e5, 1e3)
eq("climber 2sf", sf(65 * g * 450, 2), 2.9e5)

# Car KE
eq("car KE", 0.5 * 1400 * 30**2, 6.3e5)
eq("car KE x2", 0.5 * 1400 * 60**2, 2.52e6)

# Roller coaster
v = sqrt(2 * g * 35)
eq("rc v", sf(v, 3), 26.2); eq("rc v 2sf", sf(v, 2), 26)
v2 = sqrt(0.80 * 2 * g * 35)
eq("rc v2", sf(v2, 3), 23.4); eq("rc v2 2sf", sf(v2, 2), 23)

# Pendulum
eq("pendulum", sf(sqrt(2 * g * 0.20), 2), 2.0)

# Braking
EK = 0.5 * 1200 * 20**2
eq("brake KE", EK, 2.4e5)
eq("brake s", EK / 6000, 40)
eq("brake s x2", 0.5 * 1200 * 40**2 / 6000, 160)

# Slope with friction
h = 3.0 * sin(radians(30))
eq("slope h", h, 1.5)
eq("slope GPE", sf(2.0 * g * h, 3), 29.4)
eq("slope friction", 5.0 * 3.0, 15)
KE = 2.0 * g * h - 15
eq("slope KE", sf(KE, 4), 14.43)
eq("slope v", sf(sqrt(2 * KE / 2.0), 2), 3.8)

# Sankey
eq("sankey sum", 150 + 30 + 20, 200)
eq("sankey eff", 150 / 200, 0.75)

# Lift
Pout = 800 * g * 20 / 25
eq("lift out", sf(Pout, 2), 6300); eq("lift out raw", sf(Pout, 4), 6278)
eq("lift in", sf(Pout / 0.65, 2), 9700)

# Power
eq("stairs", sf(60 * g * 3.0 / 4.0, 2), 440); eq("stairs raw", sf(60 * g * 3.0 / 4.0, 3), 441)
eq("car F", 60e3 / 50, 1200)
eq("drag 25", 1200 / 2, 600)
eq("F at 25", 60e3 / 25, 2400)
eq("net", 2400 - 600, 1800)
eq("a", sf(1800 / 1100, 2), 1.6)

# Hydro
mdot = 1000 * 50
eq("mdot", mdot, 5.0e4)
Pin = mdot * g * 120
eq("hydro in", sf(Pin, 3), 5.89e7, 1e4)
eq("hydro out", sf(0.85 * Pin, 2), 5.0e7)

# kWh
eq("kWh J", 1000 * 3600, 3.6e6)
eq("heater kWh", 2.0 * 3.0, 6.0)
eq("heater J", 6.0 * 3.6e6, 2.16e7)

# Spot the error
eq("lawn wrong", 90 * 15, 1350)
eq("lawn right", sf(90 * 15 * cos(radians(40)), 2), 1000)

# Try easy
eq("t1", sf(15 * g * 2.0, 3), 294); eq("t1 2sf", sf(15 * g * 2.0, 2), 290)
eq("t3", sf(0.5 * 0.45 * 24**2, 2), 130)
eq("t4", sf(sqrt(2 * g * 1.8), 2), 5.9)
eq("t5", 3.5 / 5.0, 0.70)
eq("t6", 7500 / 30, 250)
eq("t7", sf(8000 * 22, 2), 1.8e5); eq("t7 raw", 8000 * 22, 176000)
eq("t8 kWh", 1.5 * 4.0 / 60, 0.10)
eq("t8 J", 0.10 * 3.6e6, 3.6e5)

# Exam practice
eq("e2", sf(80 * 12 * cos(radians(35)), 2), 790)
Pu = 3.0 * g * 1.2 / 4.0
eq("e4 useful", sf(Pu, 3), 8.83); eq("e4 in", 12 * 2.5, 30)
eq("e4 eff", sf(Pu / 30, 2), 0.29)
Eg = 85 * g * 24; Ek = 0.5 * 85 * 15**2
eq("e5 GPE", sf(Eg, 2), 2.0e4); eq("e5 GPE raw", sf(Eg, 5), 20012)
eq("e5 KE", sf(Ek, 2), 9.6e3); eq("e5 KE raw", Ek, 9562, 1)
eq("e5 diss", sf(Eg - Ek, 2), 1.0e4)
w = 1200 * g * sin(radians(5.0))
eq("e6 w", sf(w, 3), 1030, 1)
eq("e6 w raw", sf(w, 4), 1026)
F = 450 + 1026
eq("e6 F", sf(w + 450, 3), 1480, 1)
P = (w + 450) * 20.0
eq("e6 P", sf(P, 2), 3.0e4); eq("e6 P raw", sf(P, 4), 29520, 1)
eq("e6 in", sf(P / 0.25, 2), 1.2e5)
vb = 0.010 * 350 / 2.00
eq("e7 v", vb, 1.75); eq("e7 v 2sf", sf(vb, 2), 1.8)
K0 = 0.5 * 0.010 * 350**2; K1 = 0.5 * 2.00 * vb**2
eq("e7 K0", K0, 612.5); eq("e7 K1", sf(K1, 3), 3.06)
eq("e7 lost", sf(K0 - K1, 3), 609); eq("e7 lost 2sf", sf(K0 - K1, 2), 610)

# Stretch: bungee
m, L, k = 70, 25, 150
eq("b v", sf(sqrt(2 * g * 25), 2), 22)
eq("b mg", sf(m * g, 4), 686.7); eq("b mgL", sf(m * g * L, 5), 17168, 1)
eq("b half k", 0.5 * k, 75)
eq("b 687", sf(m * g, 3), 687); eq("b 1.72e4", sf(m * g * L, 3), 1.72e4)
a_, b_, c_ = 75, -m * g, -m * g * L
x = (-b_ + sqrt(b_**2 - 4 * a_ * c_)) / (2 * a_)
eq("b x", sf(x, 3), 20.4); eq("b x 2sf", sf(x, 2), 20)
xr = (687 + sqrt(687**2 + 4 * 75 * 17200)) / 150
eq("b x rounded coeffs", sf(xr, 3), 20.4)
T = k * x
eq("b T", sf(T, 4), 3058, 1)
eq("b res", sf(T - m * g, 4), 2371, 1)
eq("b a", sf((T - m * g) / m, 2), 34)
eq("b a/g", sf((T - m * g) / m / g, 2), 3.5)

# Stretch: wind turbine
A = pi * 40**2
eq("A", sf(A, 4), 5027)
Pw = 0.5 * 1.2 * A * 10**3
eq("wind P", sf(Pw, 2), 3.0e6)
eq("wind x8", 2**3, 8)
eq("wind elec", sf(0.40 * 3.0e6, 2), 1.2e6)

# Review additions: kinetic energy from momentum
p_ = 6.0e2
eq("pKE car", p_**2 / (2 * 1200), 150)
eq("pKE cyc", p_**2 / (2 * 60), 3.0e3)
eq("v car", p_ / 1200, 0.50); eq("v cyc", p_ / 60, 10)
eq("ratio", (p_**2 / 120) / (p_**2 / 2400), 20)
eq("alpha KE", sf((1.0e-19)**2 / (2 * 6.64e-27), 2), 7.5e-13, 1e-20)
# Energy on graphs: 0.50 kg from 20 m
eq("mg", 0.50 * g, 4.905)
eq("total", sf(0.50 * g * 20, 3), 98.1)

# Review fix: motor-efficiency lab sample readings
mgh = 0.50 * g * 1.20
eq("motor mgh", sf(mgh, 2), 5.9, 1e-9); eq("motor mgh raw", sf(mgh, 4), 5.886, 1e-9)
eq("motor eff", sf(mgh / 11.8, 2), 0.50)

print("ok")
