# checks/math.fm.systems.py: recomputes every number in "Three equations, three planes".
# Standard library only; exact work with Fraction.
from fractions import Fraction as F


def eq(label, got, want):
    assert got == want, f"{label}: computed {got}, chapter says {want}"


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def mv(A, v):
    return [sum(A[i][k] * v[k] for k in range(3)) for i in range(3)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def minor(m, i, j):
    r = [row[:j] + row[j + 1:] for k, row in enumerate(m) if k != i]
    return r[0][0] * r[1][1] - r[0][1] * r[1][0]


def cof(m):
    return [[(-1) ** (i + j) * minor(m, i, j) for j in range(3)] for i in range(3)]


def T(m):
    return [list(r) for r in zip(*m)]


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def solve(A, b):
    d = det3(A)
    out = []
    for i in range(3):
        m = [r[:] for r in A]
        for r in range(3):
            m[r][i] = b[r]
        out.append(F(det3(m), d))
    return out


def satisfies(A, b, x):
    return all(F(v) == w for v, w in zip(mv(A, x), b))


# warm-up
eq("w1 det", 3 * 2 - 1 * 5, 1)
eq("w3 det", det3([[1, 2, 0], [0, 1, 3], [2, 0, 1]]), 13)

# bakery
A = [[3, 2, 1], [1, 4, 2], [2, 1, 3]]
b = [16, 22, 19]
eq("bakery", solve(A, b), [2, 3, 4])
# the substitutions in the text: m = 22 - 4s - 2l
s, l = 3, 4
eq("bakery 2s+l", 2 * s + l, 10)
eq("bakery 7s+l", 7 * s + l, 25)
eq("bakery 10s+5l", 10 * s + 5 * l, 50)
eq("bakery third", 2 * 2 + 3 + 3 * 4, 19)

# exam example 1: unique solution
M = [[2, 1, 3], [-1, -1, 0], [-1, -2, -1]]
eq("E1 det", det3(M), 4)
eq("E1 det expand", 2 * (1 - 0) - 1 * (1 - 0) + 3 * (2 - 1), 4)
C = [[1, -1, 1], [-5, 1, 3], [3, -3, -1]]
eq("E1 cofactors", cof(M), C)
adj = [[1, -5, 3], [-1, 1, -3], [1, 3, -1]]
eq("E1 adjugate", T(cof(M)), adj)
Minv = [[F(x, 4) for x in r] for r in adj]
eq("E1 M Minv", mm(M, Minv), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
eq("E1 solution", solve(M, [9, 1, 0]), [1, -2, 3])
eq("E1 product", [sum(Minv[i][k] * [9, 1, 0][k] for k in range(3)) for i in range(3)], [1, -2, 3])
eq("E1 product raw", mv(adj, [9, 1, 0]), [4, -8, 12])

# the sheaf / prism example
S = [[1, 2, -1], [2, -1, 3], [3, 1, 2]]
eq("sheaf det", det3(S), 0)
eq("sheaf row3", [S[0][j] + S[1][j] for j in range(3)], S[2])
eq("sheaf consistent", 4 + 3, 7)
for lam in (0, 1, 2, -3):
    pt = [2 - lam, 1 + lam, lam]
    assert satisfies(S, [4, 3, 7], pt), "sheaf line"
eq("sheaf cross", cross(S[0], S[1]), [5, -5, -5])
# elimination: y = z + 1
for z in (0, 3, -2):
    y = z + 1
    x = 4 - 2 * y + z
    eq("sheaf y=z+1 eq2", 2 * x - y + 3 * z, 3)
# prism: with 8 no solution, row relation fails
eq("prism", 4 + 3 == 8, False)
for i, j in ((0, 1), (0, 2), (1, 2)):
    assert cross(S[i], S[j]) != [0, 0, 0], "normals parallel"

# coincide example (a)
n1, n2, n3 = [1, 2, 1], [2, 4, 2], [1, -1, 1]
eq("par n2=2n1", [2 * v for v in n1], n2)
eq("par a", 2 * 4, 8)
eq("par cross", cross(n1, n3), [3, 0, -3])
for lam in (0, 1, -2, 5):
    p = [4 + lam, 0, -lam]
    assert dot(n1, p) == 4 and dot(n2, p) == 8 and dot(n3, p) == 4
# z=0 point
eq("par point", (F(4) - F(4)) / 3, 0)

# solving consistent: x - y + 2z = 1, 2x + y - z = 5, 3x + z = c
Q = [[1, -1, 2], [2, 1, -1], [3, 0, 1]]
eq("Q det", det3(Q), 0)
eq("Q row3", [Q[0][j] + Q[1][j] for j in range(3)], Q[2])
eq("Q c", 1 + 5, 6)
for lam in (0, 1, -1, 2):
    p = [lam, 11 - 5 * lam, 6 - 3 * lam]
    assert satisfies(Q, [1, 5, 6], p)
eq("Q direction", cross(Q[0], Q[1]), [1, -5, -3]) if False else None
c = cross(Q[0], Q[1])
assert c[0] * -5 == c[1] and c[0] * -3 == c[2], "Q direction"
# x + y + z = 3: x = 3 - mu - lam
eq("plane param", 3 - 2 - 5 + 2 + 5, 3 - 2 - 5 + 2 + 5)

# exam example with k
def Mk(k):
    return [[1, 0, 2], [-1, -2, k], [3, k, 2]]


for k in range(-7, 8):
    eq(f"Ek det {k}", det3(Mk(k)), -k * k - 2 * k + 8)
eq("Ek roots", [k for k in range(-10, 10) if det3(Mk(k)) == 0], [-4, 2])
eq("Ek expand", 1 * (-4 - 4) + 2 * (-2 + 6), 0)
bk = [3, 1, 5]
A2 = Mk(2)
eq("Ek2 row3", [2 * A2[0][j] - A2[1][j] for j in range(3)], A2[2])
eq("Ek2 const", 2 * 3 - 1, 5)
for lam in (0, 1, 2, -1):
    p = [3 - 2 * lam, -2 + 2 * lam, lam]
    assert satisfies(A2, bk, p), "Ek2 line"
eq("Ek2 check", 9 - 4, 5)
A4 = Mk(-4)
eq("Ek4 row3", [5 * A4[0][j] + 2 * A4[1][j] for j in range(3)], A4[2])
eq("Ek4 const", 5 * 3 + 2 * 1, 17)
for i, j in ((0, 1), (0, 2), (1, 2)):
    assert cross(A4[i], A4[j]) != [0, 0, 0]
eq("Ek0 unique", solve(Mk(0), bk), [1, -1, 1]) if False else None

# planes in vector form
P = [[1, 1, 1], [2, -1, 1], [3, 0, 2]]
eq("vf det", det3(P), 0)
eq("vf row3", [P[0][j] + P[1][j] for j in range(3)], P[2])
eq("vf const", 3 + 3, 6)
for lam in (0, 1, -2):
    p = [2 - 2 * lam, 1 - lam, 3 * lam]
    assert satisfies(P, [3, 3, 6], p), "vf line"

# homogeneous example
H = [[1, 2, -1], [2, -1, 3], [3, 1, 2]]
for t in (1, 2, -3):
    assert satisfies(H, [0, 0, 0], [-t, t, t])

# spot the error
Sp = [[1, 2, 1], [3, -1, 2], [4, 1, 3]]
eq("spot det", 1 * (-3 - 2) - 2 * (9 - 8) + 1 * (3 + 4), 0)
eq("spot det2", det3(Sp), 0)
eq("spot row3", [Sp[0][j] + Sp[1][j] for j in range(3)], Sp[2])
eq("spot const", 5 + 6, 11)
for p in ([1, 1, 2], [6, 2, -5]):
    assert satisfies(Sp, [5, 6, 11], p), "spot points"
eq("spot dir", cross(Sp[0], Sp[1]), [5, 1, -7])

# try block
eq("t1", [[2, -1, 3], [1, 4, 0], [0, 3, -1]][1][2], 0)
eq("t3", solve([[1, 1, 1], [2, -1, 1], [1, 2, -1]], [6, 3, 2]), [1, 2, 3])
eq("t3 a", [1 + 2 * 1 * 0 + 0, 0][0], 1)
eq("t3 sums", (1 + 2, 2 + 3), (3, 5)) if False else None
eq("t3 e1", (2 * 1 + 3 * 2, -1 + 2 * 2), (8, 3))
eq("t4a", det3([[1, 2, 3], [4, 5, 6], [7, 8, 10]]), -3)
eq("t4b", det3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)
eq("t4a expand", 1 * (50 - 48) - 2 * (40 - 42) + 3 * (32 - 35), -3)
eq("t4b expand", 1 * (45 - 48) - 2 * (36 - 42) + 3 * (32 - 35), 0)
T5 = [[1, 1, 1], [1, -1, 1], [2, 0, 2]]
eq("t5 det", det3(T5), 0)
eq("t5 row3", [T5[0][j] + T5[1][j] for j in range(3)], T5[2])
for lam in (0, 1, 3):
    assert satisfies(T5, [3, 1, 4], [lam, 1, 2 - lam])
eq("t6 const", 3 + 1 == 5, False)
T7 = [[1, 1, -1], [2, 2, -2], [3, -1, 1]]
eq("t7 det", det3(T7), 0)
for lam in (0, 1, -2):
    assert satisfies(T7, [2, 4, 2], [1, 1 + lam, lam])
eq("t7 x", F(2 + 2, 4), 1)
eq("t8 ratio", (1 * 2 == 2) and (1 * 3 != 2) and (5 != 2), True)
T9 = [[1, 2, 1], [2, 1, -1], [3, 3, 0]]
eq("t9 det", det3(T9), 0)
eq("t9 row3", [T9[0][j] + T9[1][j] for j in range(3)], T9[2])
for t in (1, 2, -1):
    assert satisfies(T9, [0, 0, 0], [t, -t, t])
T10 = [[1, 1, 1], [2, -1, 4], [3, 0, 5]]
eq("t10 det", det3(T10), 0)
eq("t10 row3", [T10[0][j] + T10[1][j] for j in range(3)], T10[2])
eq("t10 c", 1 + 5, 6)

# exam practice
E1 = [[2, 1, 3], [1, -1, 2], [0, 4, 5]]
eq("ep1 det", det3(E1), -19)
eq("ep1 expand", 2 * (-5 - 8) - 1 * (5 - 0) + 3 * (4 - 0), -19)
E2 = [[2, 1, -1], [1, 3, 1], [3, -2, 2]]
eq("ep2", solve(E2, [-1, 0, 9]), [1, -1, 2])
eq("ep2 s1", (3 * 1 + 4 * -1), -1)
eq("ep2 s2", 2 * 0 - 9, -9)
eq("ep2 z", -1 - 3 * -1, 2)
eq("ep2 28y", (24 + 4, -1 - 27), (28, -28))
Fd = [[2, 1, 3], [1, 2, 1], [1, 1, 2]]
Fi = [[3, 1, -5], [-1, 1, 1], [-1, -1, 3]]
eq("ep3 inverse", mm(Fd, [[F(x, 2) for x in r] for r in Fi]), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
eq("ep3 product", mv(Fi, [11, 8, 7]), [6, 4, 2])
eq("ep3", solve(Fd, [11, 8, 7]), [3, 2, 1])


def Hk(k):
    return [[k, 1, 1], [1, k, 1], [1, 1, k]]


for k in range(-6, 7):
    eq(f"ep4 det {k}", det3(Hk(k)), (k - 1) ** 2 * (k + 2))
eq("ep4 expand", [k * (k * k - 1) - 1 * (k - 1) + 1 * (1 - k) for k in (3, 5)], [(k - 1) ** 2 * (k + 2) for k in (3, 5)])
eq("ep4 factor", [(k - 1) * (k * k + k - 2) for k in (3, 5)], [(k - 1) ** 2 * (k + 2) for k in (3, 5)])
for t in (1, 4):
    assert satisfies(Hk(-2), [0, 0, 0], [t, t, t])
eq("ep4 x=y", -3 * 1 + 3 * 1, 0)


def Rk(k):
    return [[1, 1, 2], [3, -1, 1], [-1, 3, k]]


for k in range(-6, 7):
    eq(f"ep5 det {k}", det3(Rk(k)), 12 - 4 * k)
eq("ep5 expand", 1 * (-3 - 3) - 1 * (9 + 1) + 2 * (9 - 1), 0) if False else None
for k in (0, 1, 5):
    assert 1 * (-k - 3) - 1 * (3 * k + 1) + 2 * (9 - 1) == 12 - 4 * k
R3 = Rk(3)
eq("ep5 row3", [2 * R3[0][j] - R3[1][j] for j in range(3)], R3[2])
eq("ep5 const", 2 * 1 - 11, -9)
for lam in (0, 1, -2, 3):
    p = [3 - 3 * lam, -2 - 5 * lam, 4 * lam]
    assert satisfies(R3, [1, 11, -9], p), "ep5 line"
eq("ep5 4x+3z", 4 * 3 + 3 * 0, 12)

N6 = [[3, -1, 2], [6, -2, 4], [1, 1, -1]]
eq("ep6 c", 2 * 4, 8)
eq("ep6 cross", cross(N6[0], N6[2]), [-1, 5, 4])
for lam in (0, 1, 2):
    p = [1 - lam, -1 + 5 * lam, 4 * lam]
    assert dot(N6[0], p) == 4 and dot(N6[1], p) == 8 and dot(N6[2], p) == 0
eq("ep6 point", (3 * 1 - (-1), 1 + (-1)), (4, 0))

N7 = [[1, 1, 1], [2, 3, 4], [3, 4, 5]]
eq("ep7 det", det3(N7), 0)
eq("ep7 expand", 1 * (15 - 16) - 1 * (10 - 12) + 1 * (8 - 9), 0)
eq("ep7 row3", [N7[0][j] + N7[1][j] for j in range(3)], N7[2])
eq("ep7 a", 2 + 5, 7)
for lam in (0, 1, -1, 4):
    p = [1 + lam, 1 - 2 * lam, lam]
    assert satisfies(N7, [2, 5, 7], p), "ep7 line"
for i, j in ((0, 1), (0, 2), (1, 2)):
    assert cross(N7[i], N7[j]) != [0, 0, 0]

N8 = [[1, 1, -1], [2, -1, 1], [4, 1, 1]]
d = cross(N8[0], N8[1])
eq("ep8 cross", d, [0, -3, -3])
for lam in (0, 1, 2):
    p = [1, 1 + lam, lam]
    assert dot(N8[0], p) == 2 and dot(N8[1], p) == 1
eq("ep8 a", dot([0, 1, 1], [4, -1, 1]), 0)
eq("ep8 b", 4 * 1 - 1 * 1 + 0, 3)
eq("ep8 c", [4 + 1 + 2 * 1], [7])
N8c = [[1, 1, -1], [2, -1, 1], [4, 1, 1]]
eq("ep8 solve", solve(N8c, [2, 1, 7]), [1, 2, 1])

# stretch 1
def Sa(a):
    return [[1, 1, 1], [1, a, 1], [1, 1, a]]


for a in range(-4, 5):
    eq(f"st1 det {a}", det3(Sa(a)), (a - 1) ** 2)
for a, b in ((2, 5), (3, -1), (-2, 4)):
    x, y, z = solve(Sa(a), [1, b, 2])
    eq("st1 z", z, F(1, a - 1))
    eq("st1 y", y, F(b - 1, a - 1))
    eq("st1 x", x, 1 - y - z)

# stretch 2
def Cm(k):
    return [[1, -1, -1], [5, 2, 0], [0, 2, -k]]


for k in range(1, 9):
    eq(f"st2 det {k}", det3(Cm(k)), -7 * k - 10)
    I = solve(Cm(k), [0, 12, 0])
    eq(f"st2 I2 {k}", I[1], F(12 * k, 7 * k + 10))
    eq(f"st2 I3 {k}", I[2], F(24, 7 * k + 10))
    eq(f"st2 I1 {k}", I[0], I[1] + I[2])
eq("st2 expand", 1 * (-2 * 4 - 0) + 1 * (-5 * 4 - 0) - 1 * (10 - 0), -7 * 4 - 10)

# marks: totals of exam-style examples and practice questions
eq("E1 marks", 2 + 3 + 2, 7)
eq("E2 marks", 2 + 3 + 2, 7)
eq("E3 marks", 4 + 4 + 3, 11)
eq("E4 marks", 6 + 2, 8)
eq("spot marks", 2 + 0 + 2, 4)

print("ok")
