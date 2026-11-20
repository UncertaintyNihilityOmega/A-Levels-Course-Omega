# checks/math.fm.matrices2.py: recomputes every number in "Eigenvalues and eigenvectors".
# Standard library only; exact work with Fraction.
from fractions import Fraction as F
from math import sqrt, isclose


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mv(A, v):
    return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A))]


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def minor3(m, i, j):
    r = [row[:j] + row[j + 1:] for k, row in enumerate(m) if k != i]
    return det2(r)


def cof(m):
    return [[(-1) ** (i + j) * minor3(m, i, j) for j in range(3)] for i in range(3)]


def T(m):
    return [list(r) for r in zip(*m)]


def tr(m):
    return sum(m[i][i] for i in range(len(m)))


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sc(k, A):
    return [[k * x for x in r] for r in A]


def mpow(A, n):
    R = eye(len(A))
    for _ in range(n):
        R = mm(R, A)
    return R


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def isEig(A, lam, e):
    return mv(A, e) == [lam * x for x in e] and any(x != 0 for x in e)


def inv2(m):
    d = det2(m)
    return [[F(m[1][1], d), F(-m[0][1], d)], [F(-m[1][0], d), F(m[0][0], d)]]


def charpoly3(m):
    """(tr, c, det) so that the characteristic equation is x^3 - tr x^2 + c x - det = 0."""
    c = sum(minor3(m, i, i) for i in range(3))
    return tr(m), c, det3(m)


def diag3(d):
    return [[d[0], 0, 0], [0, d[1], 0], [0, 0, d[2]]]


# warm-up
A = [[3, 1], [2, 2]]
eq("w1", mv(A, [1, 1]), [4, 4])
eq("w2", (1 - 6 + 11 - 6, (-1) ** 0), (0, 1))
eq("w2 fac", [(l - 1) * (l - 2) * (l - 3) for l in (4, 5)], [l ** 3 - 6 * l ** 2 + 11 * l - 6 for l in (4, 5)])
eq("w3", det2([[1, 1], [2, 2]]), 0)

# intro
eq("intro e1", mv(A, [1, 0]), [3, 2])
eq("intro e2", mv(A, [1, 1]), [4, 4])
eq("intro e3", mv(A, [1, -2]), [1, -2])
eq("A char", [l * l - 5 * l + 4 for l in (1, 4)], [0, 0])
eq("A tr det", (tr(A), det2(A)), (5, 4))
eq("A eig 4", isEig(A, 4, [1, 1]), True)
eq("A eig 1", isEig(A, 1, [1, -2]), True)
eq("A-4I", [[3 - 4, 1], [2, 2 - 4]], [[-1, 1], [2, -2]])
eq("A-I", [[3 - 1, 1], [2, 2 - 1]], [[2, 1], [2, 1]])

# exam example 1: B
B = [[4, -2], [1, 1]]
eq("B char", [(4 - l) * (1 - l) + 2 - (l * l - 5 * l + 6) for l in range(-3, 6)], [0] * 9)
eq("B eig2", isEig(B, 2, [1, 1]), True)
eq("B eig3", isEig(B, 3, [2, 1]), True)
eq("B-2I", [[4 - 2, -2], [1, 1 - 2]], [[2, -2], [1, -1]])
eq("B-3I", [[4 - 3, -2], [1, 1 - 3]], [[1, -2], [1, -2]])
eq("B tr det", (tr(B), det2(B)), (5, 6))
eq("B*(2,1)", mv(B, [2, 1]), [6, 3])

# reflection
R = [[0, 1], [1, 0]]
eq("refl 1", isEig(R, 1, [1, 1]), True)
eq("refl -1", isEig(R, -1, [1, -1]), True)

# zero eigenvalue example
Z = [[2, 4], [1, 2]]
eq("Z tr det", (tr(Z), det2(Z)), (4, 0))
eq("Z eig0", isEig(Z, 0, [2, -1]), True)
eq("Z eig4", isEig(Z, 4, [2, 1]), True)
eq("Z-4I", [[2 - 4, 4], [1, 2 - 4]], [[-2, 4], [1, -2]])

# 3x3 example (exam style)
A3 = [[3, 2, 2], [1, 2, 0], [-1, -1, 1]]
for lam in range(-5, 8):
    # det(A - lam I) expanded along row 2 as in the chapter
    d = -1 * ((2 * (1 - lam)) - (2 * (-1))) + (2 - lam) * ((3 - lam) * (1 - lam) - 2 * (-1))
    eq(f"A3 expansion {lam}", d, det3([[3 - lam, 2, 2], [1, 2 - lam, 0], [-1, -1, 1 - lam]]))
    eq(f"A3 cubic {lam}", d, -lam ** 3 + 6 * lam ** 2 - 11 * lam + 6)
    eq(f"A3 mid {lam}", -(4 - 2 * lam) + (2 - lam) * (lam * lam - 4 * lam + 5), -lam ** 3 + 6 * lam ** 2 - 11 * lam + 6)
eq("A3 cp", charpoly3(A3), (6, 11, 6))
eq("A3 minors", [minor3(A3, i, i) for i in range(3)], [2, 5, 4])
eq("A3 roots", [l for l in range(-6, 7) if l ** 3 - 6 * l ** 2 + 11 * l - 6 == 0], [1, 2, 3])
eq("A3 factor", [(l - 1) * (l ** 2 - 5 * l + 6) for l in range(-3, 4)], [l ** 3 - 6 * l ** 2 + 11 * l - 6 for l in range(-3, 4)])
e1, e2, e3 = [1, -1, 0], [0, 1, -1], [1, 1, -1]
eq("A3 e1", isEig(A3, 1, e1), True)
eq("A3 e2", isEig(A3, 2, e2), True)
eq("A3 e3", isEig(A3, 3, e3), True)
eq("A3 *(1,1,-1)", mv(A3, e3), [3, 3, -3])
eq("A3-I", [[A3[i][j] - (1 if i == j else 0) for j in range(3)] for i in range(3)], [[2, 2, 2], [1, 1, 0], [-1, -1, 0]])
eq("A3-2I", [[A3[i][j] - (2 if i == j else 0) for j in range(3)] for i in range(3)], [[1, 2, 2], [1, 0, 0], [-1, -1, -1]])
eq("A3-3I", [[A3[i][j] - (3 if i == j else 0) for j in range(3)] for i in range(3)], [[0, 2, 2], [1, -1, 0], [-1, -1, -2]])
eq("A3 cross", cross([1, 2, 2], [1, 0, 0]), [0, 2, -2])

# properties (exam examples)
eq("A inv eig", [F(1, 2), F(1, -1), F(1, 4)], [F(1, 2), -1, F(1, 4)])
eq("A inv +3", [F(1, 2) + 3, -1 + 3, F(1, 4) + 3], [F(7, 2), 2, F(13, 4)])


def proves_power(A, lam, e, n):
    return mv(mpow(A, n), e) == [lam ** n * x for x in e]


for n in range(1, 7):
    assert proves_power(A3, 3, e3, n)
    assert proves_power(B, 3, [2, 1], n)

# diagonalisation: B
Q = [[1, 2], [1, 1]]
D = [[2, 0], [0, 3]]
eq("B detQ", det2(Q), -1)
Qi = [[-1, 2], [1, -1]]
eq("B Qinv", mm(Q, Qi), [[1, 0], [0, 1]])
eq("B QDQi", mm(mm(Q, D), Qi), B)
for n in range(0, 8):
    p2, p3 = 2 ** n, 3 ** n
    formula = [[2 * p3 - p2, 2 * p2 - 2 * p3], [p3 - p2, 2 * p2 - p3]]
    eq(f"B^{n}", mpow(B, n), formula)
eq("B^5", mpow(B, 5), [[454, -422], [211, -179]])
eq("B^5 numbers", (2 * 243 - 32, 64 - 486, 243 - 32, 64 - 243), (454, -422, 211, -179))
eq("B QDn step", mm(Q, [[2, 0], [0, 3]]), [[2, 6], [2, 3]])

# population example
M = [[F(8, 10), F(3, 10)], [F(2, 10), F(7, 10)]]
eq("pop tr det", (tr(M), det2(M)), (F(3, 2), F(1, 2)))
eq("pop det calc", F(56 - 6, 100), F(1, 2))
eq("pop e1", mv(M, [3, 2]), [3, 2])
eq("pop e.5", mv(M, [1, -1]), [F(1, 2), F(-1, 2)])
Qp = [[3, 1], [2, -1]]
eq("pop Qinv", mm(Qp, [[F(1, 5), F(1, 5)], [F(2, 5), F(-3, 5)]]), [[1, 0], [0, 1]])
v = [10000, 40000]
for n in range(0, 12):
    h = F(1, 2) ** n
    Mn = [[(3 + 2 * h) / 5, (3 - 3 * h) / 5], [(2 - 2 * h) / 5, (2 + 3 * h) / 5]]
    eq(f"pop M^{n}", Mn, mpow(M, n))
    a, b = mv(Mn, [10000, 40000])
    eq(f"pop a{n}", a, 30000 - 20000 * h)
    eq(f"pop b{n}", b, 20000 + 20000 * h)
eq("pop a1", 30000 - 20000 * F(1, 2), 20000)
eq("pop a1 direct", F(8, 10) * 10000 + F(3, 10) * 40000, 20000)

# 3x3 diagonalisation
Q3 = [[1, 0, 1], [-1, 1, 1], [0, -1, -1]]
eq("Q3 det", det3(Q3), 1)
eq("Q3 det expand", 1 * (-1 + 1) - 0 + 1 * (1 - 0), 1)
eq("Q3 cof", cof(Q3), [[0, -1, 1], [-1, -1, 1], [-1, -2, 1]])
Q3i = T(cof(Q3))
eq("Q3 inv", Q3i, [[0, -1, -1], [-1, -1, -2], [1, 1, 1]])
eq("Q3 Q Qi", mm(Q3, Q3i), eye(3))
eq("Q3 QDQi", mm(mm(Q3, diag3([1, 2, 3])), Q3i), A3)
eq("A4 QD4", mm(Q3, diag3([1, 16, 81])), [[1, 0, 81], [-1, 16, 81], [0, -16, -81]])
A4 = mm(mm(Q3, diag3([1, 16, 81])), Q3i)
eq("A4", A4, [[81, 80, 80], [65, 66, 50], [-65, -65, -49]])
eq("A4 direct", mpow(A3, 4), A4)
eq("A4 trace", (tr(A4), 1 + 16 + 81), (98, 98))
eq("Q3 check", (1 * 0 + 0 * -1 + 1 * 1, 1 * -1 + 0 * -1 + 1 * 1), (1, 0))
eq("cols of Q are e", T(Q3), [e1, e2, e3])

# spot the error
Qs = [[2, 1], [1, 1]]
Ds = [[2, 0], [0, 3]]
Qsi = [[1, -1], [-1, 2]]
eq("spot detQ", det2(Qs), 1)
eq("spot inv", mm(Qs, Qsi), eye(2))
eq("spot product", mm(mm(Qs, Ds), Qsi), [[1, 2], [-1, 4]])
Dgood = [[3, 0], [0, 2]]
eq("spot good", mm(mm(Qs, Dgood), Qsi), B)
eq("spot QD", mm(Qs, Dgood), [[6, 2], [3, 2]])

# Cayley-Hamilton 2x2
A2 = mm(A, A)
eq("CH A2", A2, add(sc(5, A), sc(-4, eye(2))))
Ainv = sc(F(1, 4), add(sc(5, eye(2)), sc(-1, A)))
eq("CH Ainv", Ainv, [[F(1, 2), F(-1, 4)], [F(-1, 2), F(3, 4)]])
eq("CH Ainv check", mm(A, Ainv), eye(2))
eq("CH Ainv text", sc(F(1, 4), [[2, -1], [-2, 3]]), Ainv)
eq("CH A3", mpow(A, 3), add(sc(21, A), sc(-20, eye(2))))
eq("CH A4", mpow(A, 4), add(sc(85, A), sc(-84, eye(2))))
eq("CH A4 val", mpow(A, 4), [[171, 85], [170, 86]])
eq("CH A4 tr", (tr(mpow(A, 4)), 1 + 4 ** 4), (257, 257))
eq("CH A4 coef", (5 * 5 - 4, 5 * 21 - 20 , 21 * 5 - 20 * 1, 21 * -4), (21, 85, 85, -84))

# exam example 7: CH 3x3
CA = [[1, 1, 0], [0, 2, 1], [1, 0, 3]]
eq("CA cp", charpoly3(CA), (6, 11, 7))
eq("CA minors", [minor3(CA, i, i) for i in range(3)], [6, 3, 2])
for lam in range(-4, 6):
    d = (1 - lam) * ((2 - lam) * (3 - lam)) - 1 * (0 - 1)
    eq(f"CA det {lam}", d, det3([[1 - lam, 1, 0], [0, 2 - lam, 1], [1, 0, 3 - lam]]))
    eq(f"CA cubic {lam}", d, -lam ** 3 + 6 * lam ** 2 - 11 * lam + 7)
CA2 = mm(CA, CA)
eq("CA A2", CA2, [[1, 3, 1], [1, 4, 5], [4, 1, 9]])
CA3 = mpow(CA, 3)
eq("CH3 holds", add(add(CA3, sc(-6, CA2)), add(sc(11, CA), sc(-7, eye(3)))), [[0] * 3] * 3)
inv = sc(F(1, 7), add(add(CA2, sc(-6, CA)), sc(11, eye(3))))
eq("CA inv", inv, [[F(x, 7) for x in r] for r in [[6, -3, 1], [1, 3, -1], [-2, 1, 2]]])
eq("CA inv check", mm(CA, inv), eye(3))
eq("CA inv cofactor", [[F(x, 7) for x in r] for r in T(cof(CA))], inv)
eq("CA A4", mpow(CA, 4), add(add(sc(25, CA2), sc(-59, CA)), sc(42, eye(3))))
eq("CA A4 coef", (6 * 6 - 11, 6 * -11 + 7, 6 * 7), (25, -59, 42))

# try block
T1 = [[5, 4], [1, 2]]
eq("t1 tr det", (tr(T1), det2(T1)), (7, 6))
eq("t1 e1", isEig(T1, 1, [1, -1]), True)
eq("t1 e6", isEig(T1, 6, [4, 1]), True)
T2 = [[4, 3], [1, 2]]
eq("t2", mv(T2, [3, 1]), [15, 5])
# t3: [[2,k],[3,1]] eigenvalue 4
eq("t3 k", [k for k in range(-9, 10) if (2 - 4) * (1 - 4) - 3 * k == 0], [2])
eq("t3 other", (3 - 4, 2 * 1 - 2 * 3, 4 * -1), (-1, -4, -4))
T4 = [[2, 1, 0], [0, 3, 0], [1, 3, 1]]
for lam in range(-3, 6):
    eq(f"t4 det {lam}", det3([[2 - lam, 1, 0], [0, 3 - lam, 0], [1, 3, 1 - lam]]), (3 - lam) * (2 - lam) * (1 - lam))
eq("t4 e3", isEig(T4, 3, [1, 1, 2]), True)
eq("t5", [l * l - 2 * l + 3 for l in (2, -3)], [3, 18])
T6 = [[2, 1], [1, 2]]
eq("t6 eig", (isEig(T6, 1, [1, -1]), isEig(T6, 3, [1, 1])), (True, True))
T6i = inv2(T6)
eq("t6 inv", T6i, [[F(2, 3), F(-1, 3)], [F(-1, 3), F(2, 3)]])
eq("t6 tr", (tr(T6i), 1 + F(1, 3)), (F(4, 3), F(4, 3)))
Qt = [[4, 1], [1, -1]]
Qti = [[F(1, 5), F(1, 5)], [F(1, 5), F(-4, 5)]]
eq("t7 Qinv", mm(Qt, Qti), eye(2))
eq("t7 QDQi", mm(mm(Qt, [[6, 0], [0, 1]]), Qti), T1)
eq("t7 cube", mm(mm(Qt, [[216, 0], [0, 1]]), Qti), mpow(T1, 3))
eq("t7 cube val", mpow(T1, 3), [[173, 172], [43, 44]])
eq("t7 numbers", (4 * 216 + 1, 4 * 216 - 4, 216 - 1, 216 + 4), (865, 860, 215, 220))
eq("t7 detQ", det2(Qt), -5)
T8 = [[1, 2], [3, 4]]
eq("t8 A2", mm(T8, T8), [[7, 10], [15, 22]])
eq("t8 CH", mm(T8, T8), add(sc(5, T8), sc(2, eye(2))))
eq("t8 inv", sc(F(1, 2), add(T8, sc(-5, eye(2)))), [[-2, 1], [F(3, 2), F(-1, 2)]])
eq("t8 inv check", mm(T8, [[-2, 1], [F(3, 2), F(-1, 2)]]), eye(2))
eq("t8 A3", mpow(T8, 3), add(sc(27, T8), sc(10, eye(2))))
eq("t8 A3 val", mpow(T8, 3), [[37, 54], [81, 118]])
T9 = [[2, 7, 1], [0, 3, 4], [0, 0, -1]]
for lam in range(-3, 6):
    eq(f"t9 {lam}", det3([[2 - lam, 7, 1], [0, 3 - lam, 4], [0, 0, -1 - lam]]), (2 - lam) * (3 - lam) * (-1 - lam))
T10 = [[2, -1], [-6, 3]]
eq("t10", (det2(T10), tr(T10)), (0, 5))
eq("t10 e0", isEig(T10, 0, [1, 2]), True)
eq("t10 e5", isEig(T10, 5, [1, -3]), True)

# exam practice
M1 = [[1, 4], [2, 3]]
eq("ep1 cp", (tr(M1), det2(M1)), (4, -5))
eq("ep1 expand", (1 - 5) * (3 - 5) - 8, 0)
eq("ep1 e5", isEig(M1, 5, [1, 1]), True)
eq("ep1 e-1", isEig(M1, -1, [2, -1]), True)
eq("ep2", (1 + 2 + 5, 1 * 2 * 5, [l * l - l for l in (1, 2, 5)]), (8, 10, [0, 2, 20]))
M3 = [[3, 2], [2, 0]]
eq("ep3 cp", (tr(M3), det2(M3)), (3, -4))
eq("ep3 roots", [l for l in range(-6, 7) if l * l - 3 * l - 4 == 0], [-1, 4])
eq("ep3 vals", [l * l - 4 * l for l in (4, -1)], [0, 5])
M3s = add(mm(M3, M3), sc(-4, M3))
eq("ep3 A2-4A", M3s, [[1, -2], [-2, 4]])
eq("ep3 A2-4A eig", (tr(M3s), det2(M3s)), (5, 0))
P = [[1, 2, 2], [-3, 1, 3], [3, 2, 0]]
for lam in range(-5, 7):
    d = (1 - lam) * ((1 - lam) * (-lam) - 6) - 2 * (3 * lam - 9) + 2 * (-6 - 3 * (1 - lam))
    eq(f"ep4 det {lam}", d, det3([[1 - lam, 2, 2], [-3, 1 - lam, 3], [3, 2, -lam]]))
    eq(f"ep4 cubic {lam}", d, -lam ** 3 + 2 * lam ** 2 + 5 * lam - 6)
    eq(f"ep4 factor {lam}", (1 - lam) * (lam * lam - lam - 6), -lam ** 3 + 2 * lam ** 2 + 5 * lam - 6)
    eq(f"ep4 cancel {lam}", (-2) * (3 * lam - 9) + 2 * (-6 - 3 * (1 - lam)), 0)
eq("ep4 cp", charpoly3(P), (2, -5, -6))
eq("ep4 roots", [l for l in range(-6, 7) if l ** 3 - 2 * l ** 2 - 5 * l + 6 == 0], [-2, 1, 3])
eq("ep4 e3", isEig(P, 3, [1, 0, 1]), True)
eq("ep4 e1", isEig(P, 1, [1, -1, 1]), True)
eq("ep4 e-2", isEig(P, -2, [0, 1, -1]), True)
eq("ep4 cross", cross([-2, 2, 2], [-3, -2, 3]), [10, 0, 10])
eq("ep4 A-3I", [[P[i][j] - (3 if i == j else 0) for j in range(3)] for i in range(3)], [[-2, 2, 2], [-3, -2, 3], [3, 2, -3]])
# sequence
M5 = [[5, -6], [1, 0]]
a = [0, 1]
for n in range(2, 15):
    a.append(5 * a[-1] - 6 * a[-2])
eq("ep5 formula", a, [3 ** n - 2 ** n for n in range(15)])
eq("ep5 e2", isEig(M5, 2, [2, 1]), True)
eq("ep5 e3", isEig(M5, 3, [3, 1]), True)
Q5 = [[3, 2], [1, 1]]
eq("ep5 Qinv", mm(Q5, [[1, -2], [-1, 3]]), eye(2))
eq("ep5 QDQi", mm(mm(Q5, [[3, 0], [0, 2]]), [[1, -2], [-1, 3]]), M5)
for n in range(0, 9):
    col = mv(mpow(M5, n), [1, 0])
    eq(f"ep5 col {n}", col, [3 ** (n + 1) - 2 ** (n + 1), 3 ** n - 2 ** n])
eq("ep5 -auxiliary", [l * l - 5 * l + 6 for l in (2, 3)], [0, 0])
# roots cubic
roots = [l for l in range(-5, 6) if l ** 3 - 3 * l ** 2 + l + 2 == 0]
eq("ep6 root 2", roots, [2])
# eigenvalues: 2 and roots of l^2 - l - 1 = 0
ph, ps = (1 + sqrt(5)) / 2, (1 - sqrt(5)) / 2
ev = [2.0, ph, ps]
assert all(abs(l ** 3 - 3 * l ** 2 + l + 2) < 1e-9 for l in ev)
eq("ep6 tr", round(sum(ev), 9), 3.0)
eq("ep6 det", round(ev[0] * ev[1] * ev[2], 9), -2.0)
sq = [l * l for l in ev]
assert all(abs(y ** 3 - 7 * y ** 2 + 13 * y - 4) < 1e-9 for y in sq)
eq("ep6 sum", round(sum(sq), 9), 7.0)
eq("ep6 prod", round(sq[0] * sq[1] * sq[2], 9), 4.0)
for y in range(-3, 6):
    eq(f"ep6 expand {y}", y * (y + 1) ** 2 - (3 * y - 2) ** 2, y ** 3 - 7 * y ** 2 + 13 * y - 4)
# N
N = [[1, 2, 0], [0, 1, 1], [1, 0, 2]]
eq("ep7 cp", charpoly3(N), (4, 5, 4))
for lam in range(-4, 6):
    d = (1 - lam) ** 2 * (2 - lam) + 2
    eq(f"ep7 det {lam}", d, det3([[1 - lam, 2, 0], [0, 1 - lam, 1], [1, 0, 2 - lam]]))
    eq(f"ep7 cubic {lam}", d, -lam ** 3 + 4 * lam ** 2 - 5 * lam + 4)
N2 = mm(N, N)
eq("ep7 N2", N2, [[1, 4, 2], [1, 1, 3], [3, 2, 4]])
Ninv = sc(F(1, 4), add(add(N2, sc(-4, N)), sc(5, eye(3))))
eq("ep7 inv", Ninv, [[F(x, 4) for x in r] for r in [[2, -4, 2], [1, 2, -1], [-1, 2, 1]]])
eq("ep7 inv check", mm(N, Ninv), eye(3))
eq("ep7 N4", mpow(N, 4), add(add(sc(11, N2), sc(-16, N)), sc(16, eye(3))))
eq("ep7 coef", (4 * 4 - 5, 4 * -5 + 4, 4 * 4), (11, -16, 16))
# tanks
Mt = [[F(7, 10), F(1, 10)], [F(3, 10), F(9, 10)]]
eq("ep8 tr det", (tr(Mt), det2(Mt)), (F(8, 5), F(3, 5)))
eq("ep8 det calc", F(63, 100) - F(3, 100), F(3, 5))
eq("ep8 e1", mv(Mt, [1, 3]), [1, 3])
eq("ep8 e.6", mv(Mt, [1, -1]), [F(3, 5), F(-3, 5)])
Qt2 = [[1, 1], [3, -1]]
eq("ep8 Qinv", mm(Qt2, [[F(1, 4), F(1, 4)], [F(3, 4), F(-1, 4)]]), eye(2))
for n in range(0, 10):
    h = F(3, 5) ** n
    Mn = [[(1 + 3 * h) / 4, (1 - h) / 4], [(3 - 3 * h) / 4, (3 + h) / 4]]
    eq(f"ep8 M^{n}", Mn, mpow(Mt, n))
    a_, b_ = mv(Mn, [80, 0])
    eq(f"ep8 a{n}", a_, 20 + 60 * h)
    eq(f"ep8 b{n}", b_, 60 - 60 * h)
# stretch: Fibonacci
fib = [0, 1]
for n in range(2, 40):
    fib.append(fib[-1] + fib[-2])
for n in range(0, 30):
    assert isclose((ph ** n - ps ** n) / sqrt(5), fib[n], abs_tol=1e-6)
assert abs(ph * ph - ph - 1) < 1e-12 and abs(ps * ps - ps - 1) < 1e-12
assert isclose(ph - ps, sqrt(5))

# marks
eq("X1", 5, 3 + 2)
eq("X2", 3 + 2 + 4, 9)
eq("X3", 2 + 5, 7)
eq("X4", 3 + 2, 5)
eq("X5", 4 + 3 + 1, 8)
eq("X6", 2 + 2 + 2, 6)
eq("X7", 3 + 4 + 2, 9)
eq("spot", 1 + 0 + 2, 3)

print("ok")
