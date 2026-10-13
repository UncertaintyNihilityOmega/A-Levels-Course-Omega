# checks/phys.dynamics.py: recomputes every number in the Dynamics and momentum chapter.
from math import isclose, sqrt, sin, cos, radians, atan2, degrees, tan

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

g = 9.81

# Warm-up
eq("warm a", (20 - 5.0) / 6.0, 2.5)
eq("warm s", 0.5 * 3.0 * 4.0**2, 24)
eq("warm resultant", sqrt(30**2 + 40**2), 50)
eq("warm angle", round(degrees(atan2(40, 30)), 1), 53.1)

# Mass and weight
eq("astronaut Earth", 65 * g, 637.65, 1e-9)
eq("astronaut Earth 3sf", sf(65 * g), 638)
eq("astronaut Moon", sf(65 * 1.62), 105)
eq("Moon fraction", 1.62 / g, 0.165, 0.001)

# Football impulse
area = 0.5 * 0.0150 * 1200
eq("impulse", area, 9.0)
eq("football speed", sf(area / 0.43, 2), 21)

# Crumple zones
dp = 1100 * 14
eq("car dp", dp, 15400)
eq("rigid", sf(dp / 0.030, 2), 5.1e5)
eq("crumple", sf(dp / 0.15, 2), 1.0e5)
eq("ratio", 0.15 / 0.030, 5)

# Ball and wall
dp = 0.15 * (-15 - 20)
eq("ball dp", dp, -5.25)
eq("ball F", dp / 0.010, -525)
eq("size of dp", 0.15 * 20 + 0.15 * 15, 5.25)
eq("wrong dp", 0.15 * 15 - 0.15 * 20, -0.75)
eq("wrong F", 0.75 / 0.010, 75)

# Hose
eq("hose", 2.0 * 12, 24)

# Car F = ma
eq("car resultant", 3000 - 1200, 1800)
eq("car a", 1800 / 1200, 1.5)

# Car and trailer
a = (3900 - 500 - 200) / 1300
eq("tow a", sf(a, 3), 2.46)
eq("tow T trailer", sf(200 + 300 * a, 3), 938)
eq("tow T car", sf(3900 - 500 - 1000 * a, 3), 938)

# Lift
eq("lift up", sf(60 * (g + 1.5), 3), 679)
eq("lift down", sf(60 * (g - 1.5), 3), 499)
eq("lift weight", sf(60 * g, 3), 589)

# Slope
w_par = 5.0 * g * sin(radians(30))
eq("slope component", round(w_par, 1), 24.5)
eq("slope resultant", round(w_par - 8.0, 1), 16.5)
eq("slope a", sf((w_par - 8.0) / 5.0, 2), 3.3)
eq("slope N", sf(5.0 * g * cos(radians(30)), 3), 42.5)
eq("slope no friction", sf(g * sin(radians(30)), 2), 4.9)

# Skydiver
W = 80 * g
eq("skydiver W", W, 784.8)
eq("skydiver W 3sf", sf(W, 3), 785)
eq("skydiver res b", W - 500, 284.8, 1e-9)
eq("skydiver a b", sf((W - 500) / 80, 3), 3.56)
eq("parachute res", sf(3000 - W, 4), 2215)
eq("parachute a", sf((3000 - W) / 80, 3), 27.7)

# Collision: 2.0 kg at 3.0 and 1.0 kg at rest
ke0 = 0.5 * 2.0 * 3.0**2
eq("ke0", ke0, 9.0)
eq("p0", 2.0 * 3.0, 6.0)
v = 6.0 / 3.0
eq("stick v", v, 2.0)
eq("stick ke", 0.5 * 3.0 * v**2, 6.0)
eq("stick lost", ke0 - 6.0, 3.0)
eq("stick percent", sf(100 * 3.0 / 9.0, 2), 33)
# elastic: v1 = ((m1-m2)u1+2 m2 u2)/(m1+m2)
v1 = ((2.0 - 1.0) * 3.0) / 3.0
v2 = (2 * 2.0 * 3.0) / 3.0
eq("elastic v1", v1, 1.0)
eq("elastic v2", v2, 4.0)
eq("elastic p", 2.0 * v1 + 1.0 * v2, 6.0)
eq("elastic rel", v2 - v1, 3.0)
eq("elastic ke", 0.5 * 2.0 * v1**2 + 0.5 * 1.0 * v2**2, 9.0)

# Head-on stick
v = (3.0 * 2.0 + 1.0 * (-4.0)) / 4.0
eq("head-on v", v, 0.50)
eq("head-on ke0", 0.5 * 3.0 * 2.0**2 + 0.5 * 1.0 * 4.0**2, 14)
eq("head-on ke1", 0.5 * 4.0 * v**2, 0.50)
eq("head-on lost", 14 - 0.5, 13.5)

# Skaters
eq("skater v", -(40 * 3.0) / 60, -2.0)

# Rifle
eq("rifle v", -(0.010 * 400) / 4.0, -1.0)
eq("bullet ke", 0.5 * 0.010 * 400**2, 800)
eq("rifle ke", 0.5 * 4.0 * 1.0**2, 2.0)

# 2D equal balls
v2 = 2.0 / (sqrt(3) * cos(radians(30)) + cos(radians(60)))
v1 = sqrt(3) * v2
eq("2D v2", v2, 1.00, 1e-9)
eq("2D v1", sf(v1, 3), 1.73)
eq("2D ratio", sin(radians(60)) / sin(radians(30)), 1.732, 1e-3)
eq("2D ke0", 0.5 * 0.17 * 2.0**2, 0.34)
eq("2D ke1", 0.5 * 0.17 * (v1**2 + v2**2), 0.34)
eq("2D coefficient", 1.732 * 0.866 + 0.5, 2.0, 1e-3)

# Try: start easy
eq("t1", sf(0.45 * g, 3), 4.41)
eq("t2", 1800 / 750, 2.4)
eq("t3", 0.058 * 40, 2.32)
eq("t4", 5.0 * 6.0, 30)
eq("t5", 0.50 * 2.0 / (0.50 + 1.5), 0.50)
eq("t7", sf(70 * g, 3), 687)
thrust = 250 * 2500
eq("rocket thrust", thrust, 6.25e5)
eq("rocket weight", 5.0e4 * g, 4.905e5)
eq("rocket res", thrust - 5.0e4 * g, 1.345e5, 1e-4)
eq("rocket a", sf((thrust - 5.0e4 * g) / 5.0e4, 2), 2.7)
eq("bag", sf(4.0 * (g - 2.0), 3), 31.2)

# Exam practice
dp = 0.058 * (-22 - 30)
eq("ex2 dp", dp, -3.016)
eq("ex2 F", sf(-dp / 0.012, 3), 251)
a = 2.0 * g / 5.0
eq("ex4 a", sf(a, 3), 3.92)
eq("ex4 T", sf(3.0 * a, 3), 11.8)
vA = (0.80 * 1.5 + 0.40 * 0.50 - 0.40 * 1.3) / 0.80
eq("ex5 vA", vA, 1.10)
ke0 = 0.5 * 0.80 * 1.5**2 + 0.5 * 0.40 * 0.50**2
ke1 = 0.5 * 0.80 * vA**2 + 0.5 * 0.40 * 1.3**2
eq("ex5 ke0", ke0, 0.95)
eq("ex5 ke1", sf(ke1, 2), 0.82)
# 2D exam
vx = (0.40 * 5.0 - 0.40 * 3.0 * cos(radians(30))) / 0.60
vy = -(0.40 * 3.0 * sin(radians(30))) / 0.60
eq("ex6 vx", sf(vx, 3), 1.60)
eq("ex6 vy", vy, -1.0)
speed = sqrt(vx**2 + vy**2)
eq("ex6 speed", sf(speed, 3), 1.89)
eq("ex6 angle", sf(degrees(atan2(-vy, vx)), 2), 32)
ke0 = 0.5 * 0.40 * 5.0**2
ke1 = 0.5 * 0.40 * 3.0**2 + 0.5 * 0.60 * speed**2
eq("ex6 ke0", ke0, 5.0)
eq("ex6 ke1", sf(ke1, 3), 2.87)
eq("ex6 parts", 0.5 * 0.40 * 3.0**2, 1.8)
eq("ex6 part2", sf(0.5 * 0.60 * speed**2, 3), 1.07)
# ballistic pendulum
v = sqrt(2 * g * 0.20)
eq("ex7 v", sf(v, 3), 1.98)
u = (0.010 + 1.50) * v / 0.010
eq("ex7 u", sf(u, 3), 299)
keb = 0.5 * 0.010 * sf(u, 3)**2
kea = 0.5 * 1.51 * v**2
eq("ex7 keb", sf(keb, 3), 447)
eq("ex7 kea", sf(kea, 3), 2.96)
eq("ex7 pct", sf(100 * (1 - kea / keb), 3), 99.3)
# lift decelerating
eq("ex8", sf(70 * (g - 2.0), 3), 547)

# Stretch: conveyor
eq("belt F", 5.0 * 2.0, 10)
eq("belt P", 10 * 2.0, 20)
eq("belt ke", 0.5 * 5.0 * 2.0**2, 10)
# stretch: heavy ball
v1 = (5.0 * 4.0 - 0.050 * 4.0) / (5.0 + 0.050)
v2 = v1 + 4.0
eq("heavy v1", sf(v1, 3), 3.92)
eq("heavy v2", sf(v2, 3), 7.92)
eq("heavy momentum", 5.0 * v1 + 0.050 * v2, 20.0)
eq("heavy 5.05", 5.0 + 0.05, 5.05)
eq("heavy 20-0.2", 20 - 0.050 * 4.0, 19.8)

# Quiz
eq("quiz dp", 0.50 * (3.0 + 4.0), 3.5)

print("ok")
