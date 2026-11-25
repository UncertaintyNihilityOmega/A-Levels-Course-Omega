# data/fm-p29-fig.py: coordinates for the hand SVG figures of P29 (slope with string, conical pendulum, banked track, vertical circle)
from math import sin, cos, tan, radians, atan2, degrees, hypot
def pr(*a): print(*a)
# 1. slope with string: slope angle 30 degrees, rises to the right from (20,190)
th = radians(30)
u = (cos(th), -sin(th)); n = (-sin(th), -cos(th))
base = (20, 190)
top_x = 300
top = (top_x, 190 - (top_x - 20) * sin(th) / cos(th))
pr('slope top', top)
s = 150  # x of contact point
contact = (s, 190 - (s - 20) * sin(th) / cos(th))
C = (contact[0] + 9 * n[0], contact[1] + 9 * n[1])
pr('contact', contact, 'centre', C)
def pt(P, d, v): return (round(P[0] + d * v[0], 1), round(P[1] + d * v[1], 1))
pr('weight tip', pt(C, 48, (0, 1)))
pr('R tip', pt(C, 48, n))
pr('T tip', pt(C, 62, u))
t = (top_x - C[0]) / u[0]
pr('string end (O)', pt(C, t, u))
pr('F tip (down slope)', pt(C, 38, (-u[0], -u[1])))
pr('mg sin dashed tip', pt(C, 24, (-u[0], -u[1])))

# 2. conical pendulum (side view): O at (110,24); P at (190,150)
O = (110, 24); P = (190, 150)
L = hypot(P[0] - O[0], P[1] - O[1]); thp = atan2(P[0] - O[0], P[1] - O[1])
pr('\nconical: L', L, 'theta', degrees(thp))
uo = ((O[0] - P[0]) / L, (O[1] - P[1]) / L)
pr('T tip', pt(P, 60, uo), 'arc end', (round(O[0] + 40 * sin(thp), 1), round(O[1] + 40 * cos(thp), 1)))
# string x at y=84 and y=94
for y in (78, 84, 94, 96): pr('string x at y', y, round(O[0] + (y - O[1]) * tan(thp) if False else O[0] + (y - O[1]) * (P[0] - O[0]) / (P[1] - O[1]), 1))

# 3. banked track, 25 degrees (drawn, not to scale)
th = radians(25)
u = (cos(th), -sin(th)); n = (-sin(th), -cos(th))
base = (20, 170); top_x = 300
top = (top_x, 170 - (top_x - 20) * sin(th) / cos(th))
s = 200
contact = (s, 170 - (s - 20) * sin(th) / cos(th))
C = (contact[0] + 9 * n[0], contact[1] + 9 * n[1])
pr('\nbank top', top, 'contact', contact, 'C', C)
pr('mg tip', pt(C, 46, (0, 1)), 'R tip', pt(C, 54, n), 'F tip', pt(C, 38, (-u[0], -u[1])), 'centre arrow tip', (round(C[0] - 80, 1), round(C[1], 1)))
pr('arc end', (round(base[0] + 40 * cos(th), 1), round(base[1] - 40 * sin(th), 1)))
