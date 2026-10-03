# checks/math.p3.vectors.py: recomputes every number in the Vectors chapter.
from math import isclose, sqrt, acos, degrees

def eq(label, got, want, tol=1e-9):
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"
def sf(x, n=3): return float(f"{x:.{n}g}")
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def mul(k, a): return tuple(k * x for x in a)
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def mag(a): return sqrt(dot(a, a))
def ang(a, b): return degrees(acos(dot(a, b) / (mag(a) * mag(b))))
def acute(a, b): return degrees(acos(abs(dot(a, b)) / (mag(a) * mag(b))))
def same(label, a, b):
    for x, y in zip(a, b): eq(label, x, y, 1e-9)

# components
a = (2, -3, 6); eq("|a|", mag(a), 7); same("par", mul(-2, a), (-4, 6, -12))
# AB
A, B = (1, 2, 3), (4, -2, 5)
same("AB", sub(B, A), (3, -4, 2)); eq("AB", sf(mag(sub(B, A))), 5.39); eq("sqrt29", mag((3, -4, 2)), sqrt(29))
same("mid", mul(0.5, add(A, B)), (2.5, 0, 4))
same("B'", add(A, (1, 3, 2)), (2, 5, 5))
# line through A(1,2,-1), B(3,5,1)
P1, Q1 = (1, 2, -1), (3, 5, 1); dd = sub(Q1, P1); same("dir", dd, (2, 3, 2))
same("P on", add(P1, mul(2, dd)), (5, 8, 3))
q = add(P1, mul(1.5, dd)); assert q != (4, 7, 2) and q[0] == 4 and q[1] == 6.5
# drone
d = (6, 8, -2); eq("speed", sf(mag(d)), 10.2); eq("mag104", mag(d), sqrt(104))
t = 40 / 2; same("land", add((0, 0, 40), mul(t, d)), (120, 160, 0)); eq("dist", sf(t * mag(d)), 204)
# intersect l1, l2
l1 = lambda s: add((1, 2, 3), mul(s, (1, -1, 2))); l2 = lambda t: add((1, -1, 8), mul(t, (2, 1, -1)))
same("meet", l1(2), l2(1)); same("pt", l1(2), (3, 0, 7))
d1, d2 = (1, -1, 2), (2, 1, -1)
eq("dot12", dot(d1, d2), -1); eq("mag", mag(d1), sqrt(6)); eq("acute", round(acute(d1, d2), 1), 80.4); eq("obtuse", round(ang(d1, d2), 1), 99.6)
eq("cos", dot(d1, d2) / 6, -1 / 6)
# skew l3
l3 = lambda u: add((1, -1, 0), mul(u, (2, 1, -1)))
same("l3 xy", l1(2)[:2], l3(1)[:2]); assert l1(2)[2] != l3(1)[2]; eq("z3", l3(1)[2], -1)
# scalar product
a2, b2 = (2, -1, 2), (1, 2, -2)
eq("dot", dot(a2, b2), -4); eq("ang", round(ang(a2, b2), 1), 116.4); eq("|a|", mag(a2), 3); eq("|b|", mag(b2), 3)
A3, B3, C3 = (1, 0, 2), (3, 1, 0), (2, 3, 1)
BA, BC = sub(A3, B3), sub(C3, B3); same("BA", BA, (-2, -1, 2)); same("BC", BC, (-1, 2, 1))
eq("dotB", dot(BA, BC), 2); eq("cosB", dot(BA, BC) / (mag(BA) * mag(BC)), 0.2722, 1e-4); eq("angB", round(ang(BA, BC), 1), 74.2)
# foot
Aa, dl, Pp = (1, 0, 2), (1, 2, 2), (4, 0, 5)
X = lambda t: add(Aa, mul(t, dl))
same("PX", sub(X(1), Pp), (-2, 2, -1)); eq("perp", dot(sub(X(1), Pp), dl), 0); eq("dist", mag(sub(X(1), Pp)), 3); same("foot", X(1), (2, 2, 4))
for t in (0.0, 2.0): eq("9t-9", dot(sub(X(t), Pp), dl), 9 * t - 9)
# cuboid
O, Ac, Bc, Cc = (0, 0, 0), (6, 0, 0), (6, 4, 0), (0, 4, 0); D, E, F, G = (0, 0, 3), (6, 0, 3), (6, 4, 3), (0, 4, 3)
eq("OF", mag(F), sqrt(61)); eq("OF sf", sf(mag(F)), 7.81)
eq("OE.OG", dot(E, G), 9); eq("OE", mag(E), sqrt(45)); eq("OG", mag(G), 5); eq("cosEOG", 9 / (5 * sqrt(45)), 0.2683, 1e-4); eq("EOG", round(ang(E, G), 1), 74.4)
AG = sub(G, Ac); same("AG", AG, (-6, 4, 3)); eq("OF.AG", dot(F, AG), -11); eq("|AG|", mag(AG), sqrt(61)); eq("acute", round(acute(F, AG), 1), 79.6)
BD = sub(D, Bc); same("BD", BD, (-6, -4, 3)); eq("OF.BD", dot(F, BD), -43); eq("OF BD", round(acute(F, BD), 1), 45.2)

# try
eq("T1", mag((3, -4, 12)), 13)
A5, B5 = (2, -1, 3), (-1, 3, 5); same("T2", sub(B5, A5), (-3, 4, 2)); eq("T2", sf(mag(sub(B5, A5))), 5.39); same("T2 mid", mul(0.5, add(A5, B5)), (0.5, 1, 4))
d6 = sub((3, -2, 1), (1, 0, -2)); same("T3 dir", d6, (2, -2, 3)); same("T3", add((1, 0, -2), mul(3, d6)), (7, -6, 7))
eq("T4 dot", dot((1, 2, 2), (2, -3, 6)), 8); eq("T4", round(ang((1, 2, 2), (2, -3, 6)), 1), 67.6); eq("|b|", mag((2, -3, 6)), 7)
eq("T5", dot((2, 2, -1), (3, -1, 4)), 0)
m1 = lambda s: add((1, 3, 2), mul(s, (2, -1, 1))); m2 = lambda t: add((-1, 0, 1), mul(t, (2, 1, 1)))
same("T6", m1(1), m2(2)); same("T6 pt", m1(1), (3, 2, 3)); eq("T6 dot", dot((2, -1, 1), (2, 1, 1)), 4); eq("T6", round(acute((2, -1, 1), (2, 1, 1)), 1), 48.2)
# T7 skew
k1 = lambda s: add((1, 0, 0), mul(s, (0, 1, 1))); k2 = lambda t: add((0, 1, 0), mul(t, (1, 0, 2)))
same("T7 xy", k1(1)[:2], k2(1)[:2]); assert k1(1)[2] != k2(1)[2]
# T8
X8 = lambda t: add((0, 1, 2), mul(t, (1, 1, 1))); P8 = (3, 1, 5)
eq("T8 dot", dot(sub(X8(2), P8), (1, 1, 1)), 0); same("T8 foot", X8(2), (2, 3, 4)); eq("T8", sf(mag(sub(X8(2), P8))), 2.45)
for t in (0.0, 5.0): eq("3t-6", dot(sub(X8(t), P8), (1, 1, 1)), 3 * t - 6)
# quiz
same("Q1", sub((3, 1, 4), (1, 4, -2)), (2, -3, 6))
q1 = lambda t: add((1, 2, 3), mul(t, (1, 1, 2))); same("Q5", q1(1), (2, 3, 5))
assert q1(1) != (2, 3, 4)
print("ok")
