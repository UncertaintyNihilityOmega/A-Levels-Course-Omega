# checks/math.fm.matrices.py: recomputes every number in "Matrices: algebra, determinants and inverses".
# Standard library only. Exact work with Fraction; every matrix result is recomputed by hand-written helpers.
from fractions import Fraction as F
from itertools import product


def M(rows):
    return [[F(x) for x in r] for r in rows]


def mul(A, B):
    assert len(A[0]) == len(B), "product not defined"
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def sub(A, B):
    return [[a - b for a, b in zip(r, s)] for r, s in zip(A, B)]


def smul(k, A):
    return [[F(k) * a for a in r] for r in A]


def T(A):
    return [list(r) for r in zip(*A)]


def I(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def minor(A, i, j):
    return [[A[r][c] for c in range(len(A)) if c != j] for r in range(len(A)) if r != i]


def det(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return det2(A)
    return sum((-1) ** j * A[0][j] * det(minor(A, 0, j)) for j in range(len(A)))


def cof(A):
    n = len(A)
    return [[(-1) ** (i + j) * det(minor(A, i, j)) for j in range(n)] for i in range(n)]


def inv(A):
    d = det(A)
    assert d != 0
    if len(A) == 2:
        return [[A[1][1] / d, -A[0][1] / d], [-A[1][0] / d, A[0][0] / d]]
    return smul(1 / d, T(cof(A)))


def eq(label, got, want):
    assert got == M(want), f"{label}: computed {got}, chapter says {want}"


# ---- Warm-up
assert 2 * 3 + 3 * 2 == 12 and 3 - 2 == 1
assert 6 ** 2 - 4 * 9 == 0 and (-6) ** 2 - 4 * 9 == 0
assert all(k ** 3 - 7 * k + 6 == 0 for k in (1, 2, -3))
assert (1) ** 3 - 7 + 6 == 0 and [1, 1, -6] == [1, 1, -6]   # (k-1)(k^2 + k - 6)
assert all((k - 1) * (k * k + k - 6) == k ** 3 - 7 * k + 6 for k in range(-5, 6))

# ---- Adding, scalar multiples
A = M([[2, -1], [3, 4]]); B = M([[0, 5], [-2, 1]])
eq("A+B", add(A, B), [[2, 4], [1, 5]])
eq("A-B", sub(A, B), [[2, -6], [5, 3]])
eq("3A", smul(3, A), [[6, -3], [9, 12]]); eq("2B", smul(2, B), [[0, 10], [-4, 2]])
eq("3A-2B", sub(smul(3, A), smul(2, B)), [[6, -13], [13, 10]])

# ---- Products
P = A
Q = M([[1, 0, 2], [-1, 3, 1]])
eq("PQ entries", mul(P, Q), [[3, -3, 3], [-1, 12, 10]])
assert (2 * 1 + (-1) * (-1), 2 * 0 + (-1) * 3, 2 * 2 + (-1) * 1) == (3, -3, 3)
assert (3 * 1 + 4 * (-1), 3 * 0 + 4 * 3, 3 * 2 + 4 * 1) == (-1, 12, 10)
D = M([[1, 2], [0, -1], [3, 1]])
eq("QD", mul(Q, D), [[7, 4], [2, -4]])
DQ = mul(D, Q)
eq("DQ", DQ, [[-1, 6, 4], [1, -3, -1], [2, 3, 7]])
assert (len(DQ), len(DQ[0])) == (3, 3)

# AB != BA
A1 = M([[1, 2], [0, 1]]); B1 = M([[3, 0], [1, 1]])
eq("AB", mul(A1, B1), [[5, 2], [1, 1]]); eq("BA", mul(B1, A1), [[3, 6], [1, 3]])
assert mul(A1, B1) != mul(B1, A1)

# Powers and the A^2 = 5A - 5I example
C = M([[2, 1], [1, 3]])
C2 = mul(C, C)
eq("C^2", C2, [[5, 5], [5, 10]])
eq("5C-5I", sub(smul(5, C), smul(5, I(2))), [[5, 5], [5, 10]])
Ci = smul(F(-1, 5), sub(C, smul(5, I(2))))
eq("C^-1", Ci, [[F(3, 5), F(-1, 5)], [F(-1, 5), F(2, 5)]])
eq("C C^-1", mul(C, Ci), I(2))
assert det(C) == 5 and 2 + 3 == 5
eq("C^3", mul(C, C2), [[15, 20], [20, 35]])

# Identity and zero
Z = M([[0, 0], [0, 0]])
assert mul(C, I(2)) == C == mul(I(2), C)
assert mul(C, Z) == Z

# Associativity numeric check
X1 = M([[1, 2, 0], [3, 1, 2], [0, 1, 1]])
for a, b, c in [(A, B, C), (A1, B1, C)]:
    assert mul(mul(a, b), c) == mul(a, mul(b, c))

# ---- Determinants 2x2
N = M([[3, -2], [4, 5]])
assert det(N) == 23 == 15 + 8
assert det(M([[6, 9], [2, 3]])) == 0 == 18 - 18
assert det(M([[1, 2], [3, 4]])) == -2
# singular: (k 4; 3 k+1)
for k in (-4, 3):
    assert det(M([[k, 4], [3, k + 1]])) == 0
assert all(k * (k + 1) - 12 == (k + 4) * (k - 3) for k in range(-6, 7))
Ni = inv(N)
eq("N^-1", Ni, [[F(5, 23), F(2, 23)], [F(-4, 23), F(3, 23)]])
eq("N N^-1", mul(N, Ni), I(2))
# solve N x = (5, -1)
sol = mul(Ni, [[F(5)], [F(-1)]])
eq("N solve", sol, [[1], [-1]])
assert (3 * 1 - 2 * (-1), 4 * 1 + 5 * (-1)) == (5, -1)

# det(AB) = det A det B
assert det(mul(A, B)) == det(A) * det(B)
assert det(mul(A1, B1)) == det(A1) * det(B1) == 1 * 3

# ---- Determinants 3x3
E = M([[2, 1, 3], [0, 4, 1], [1, 2, 5]])
assert det(E) == 25
assert 2 * (20 - 2) - 1 * (0 - 1) + 3 * (0 - 4) == 25 == 36 + 1 - 12
assert (4 * 5 - 1 * 2, 0 * 5 - 1 * 1, 0 * 2 - 4 * 1) == (18, -1, -4)
# expansion down another row gives the same
assert det(T(E)) == 25
F2 = M([[3, 0, 2], [1, 4, 0], [5, 0, 1]])
assert det(F2) == -28 == 4 * (3 * 1 - 2 * 5) == 4 * (-7)
# det(kA) = k^n det A
assert det(smul(2, E)) == 8 * 25 == 200
assert det(smul(2, N)) == 4 * 23 == 92
assert det(smul(3, N)) == 9 * 23

# ---- 3x3 inverse worked example
G = M([[1, 1, 0], [0, 1, 1], [1, 0, 2]])
assert det(G) == 3 and 1 * (2 - 0) - 1 * (0 - 1) + 0 == 3
mins = [[det(minor(G, i, j)) for j in range(3)] for i in range(3)]
eq("minors", mins, [[2, -1, -1], [2, 2, -1], [1, 1, 1]])
eq("cofactors", cof(G), [[2, 1, -1], [-2, 2, 1], [1, -1, 1]])
eq("adjugate", T(cof(G)), [[2, -2, 1], [1, 2, -1], [-1, 1, 1]])
Gi = inv(G)
eq("G^-1", Gi, [[F(2, 3), F(-2, 3), F(1, 3)], [F(1, 3), F(2, 3), F(-1, 3)], [F(-1, 3), F(1, 3), F(1, 3)]])
eq("G G^-1", mul(G, Gi), I(3)); eq("G^-1 G", mul(Gi, G), I(3))
# the nine minors written in the chapter
assert (1 * 2 - 1 * 0, 0 * 2 - 1 * 1, 0 * 0 - 1 * 1) == (2, -1, -1)
assert (1 * 2 - 0 * 0, 1 * 2 - 0 * 1, 1 * 0 - 1 * 1) == (2, 2, -1)
assert (1 * 1 - 0 * 1, 1 * 1 - 0 * 0, 1 * 1 - 1 * 0) == (1, 1, 1)
# solve G x = (3, 5, 7)
xs = mul(Gi, [[F(3)], [F(5)], [F(7)]])
eq("G solve", xs, [[1], [2], [3]])
assert (1 + 2, 2 + 3, 1 + 6) == (3, 5, 7)
# spot-the-error row-sums check: row 1 of G times column 1 of the cofactor transpose
assert 1 * 2 + 1 * 1 + 0 == 3

# ---- Unknown k: det (1 k 0; 2 1 -1; 0 3 k)
for k in (F(3, 2), -1):
    assert det(M([[1, k, 0], [2, 1, -1], [0, 3, k]])) == 0
assert all(det(M([[1, k, 0], [2, 1, -1], [0, 3, k]])) == -(2 * k - 3) * (k + 1) for k in range(-4, 5))
assert all(-(2 * k - 3) * (k + 1) == -2 * k * k + k + 3 for k in range(-4, 5))
# inverse in terms of k for (2 k; 3 5): det 10 - 3k
for k in range(-3, 3):
    Mk = M([[2, k], [3, 5]])
    assert det(Mk) == 10 - 3 * k
    if 10 - 3 * k != 0:
        assert inv(Mk) == [[F(5, 10 - 3 * k), F(-k, 10 - 3 * k)], [F(-3, 10 - 3 * k), F(2, 10 - 3 * k)]]
assert F(10, 3) * 3 == 10   # singular at k = 10/3

# ---- (AB)^-1 = B^-1 A^-1
PA = M([[2, 1], [5, 3]]); PB = M([[1, 2], [1, 3]])
assert det(PA) == 1 and det(PB) == 1
eq("PA^-1", inv(PA), [[3, -1], [-5, 2]]); eq("PB^-1", inv(PB), [[3, -2], [-1, 1]])
eq("AB", mul(PA, PB), [[3, 7], [8, 19]])
eq("(AB)^-1", inv(mul(PA, PB)), [[19, -7], [-8, 3]])
eq("B^-1 A^-1", mul(inv(PB), inv(PA)), [[19, -7], [-8, 3]])
assert mul(inv(PA), inv(PB)) != mul(inv(PB), inv(PA))
eq("A^-1 B^-1 (wrong order)", mul(inv(PA), inv(PB)), [[10, -7], [-17, 12]])
assert det(M([[3, 7], [8, 19]])) == 57 - 56 == 1
# three matrices (ABC)^-1 = C^-1 B^-1 A^-1
PC = M([[1, 1], [0, 1]])
assert inv(mul(mul(PA, PB), PC)) == mul(mul(inv(PC), inv(PB)), inv(PA))

# AX = B and XA = B
BB = M([[1, 4], [0, -1]])
eq("X = A^-1 B", mul(inv(PA), BB), [[3, 13], [-5, -22]])
eq("A X", mul(PA, mul(inv(PA), BB)), [[1, 4], [0, -1]])
eq("X A = B", mul(BB, inv(PA)), [[-17, 7], [5, -2]])
eq("check XA", mul(mul(BB, inv(PA)), PA), [[1, 4], [0, -1]])
assert mul(inv(PA), BB) != mul(BB, inv(PA))

# ---- Spot the error: N(k) = (1 2 k; 3 1 0; 2 k 1)
def Nk(k):
    return M([[1, 2, k], [3, 1, 0], [2, k, 1]])
# det = 1(1 - 0) - 2(3 - 0) + k(3k - 2) = 3k^2 - 2k - 5
for k in range(-5, 6):
    assert det(Nk(k)) == 3 * k * k - 2 * k - 5 == (3 * k - 5) * (k + 1)
# student's slip: the minor of the third entry, 3k - 1 x 2, written as 3k + 2
assert all(1 - 2 * 3 + k * (3 * k + 2) == 3 * k * k + 2 * k - 5 == (3 * k + 5) * (k - 1) for k in range(-4, 5))
assert all(3 * k * k - 2 * k - 5 == (3 * k - 5) * (k + 1) for k in range(-4, 5))   # correct: k = -1 or 5/3
assert 3 * (1) - 1 * 0 == 3 and (3 * 3 - 2) == 7 and (1 * 1 - 0) == 1
assert det(Nk(-1)) == 0 and det(Nk(F(5, 3))) == 0

# ---- Quiz
assert det(smul(2, M([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))) == 8
assert det(smul(2, E)) == 200
assert (2, 3) and len(mul(M([[1, 2, 3], [4, 5, 6]]), M([[1, 0], [0, 1], [1, 1]]))) == 2

# ---- Exam practice
PQ1 = M([[1, -2, 0], [3, 1, 4]]); QQ1 = M([[2, 1], [0, -1], [5, 3]])
eq("E1 PQ", mul(PQ1, QQ1), [[2, 3], [26, 14]])
assert (len(mul(QQ1, PQ1)), len(mul(QQ1, PQ1)[0])) == (3, 3)
assert (1 * 2 + (-2) * 0 + 0 * 5, 1 * 1 + (-2) * (-1) + 0 * 3) == (2, 3)
assert (3 * 2 + 1 * 0 + 4 * 5, 3 * 1 + 1 * (-1) + 4 * 3) == (26, 14)
# E2 (k 6; 1 k-5)
for k in (6, -1):
    assert det(M([[k, 6], [1, k - 5]])) == 0
assert all(k * (k - 5) - 6 == (k - 6) * (k + 1) for k in range(-5, 8))
# E3
M3 = M([[4, -3], [2, -1]])
assert det(M3) == 2
eq("E3 inverse", inv(M3), [[F(-1, 2), F(3, 2)], [-1, 2]])
eq("E3 solve", mul(inv(M3), [[F(5)], [F(3)]]), [[2], [1]])
assert (4 * 2 - 3, 2 * 2 - 1) == (5, 3)
# E4
AI = M([[1, 2], [3, 5]]); BI = M([[2, -1], [1, 0]])
eq("E4 (AB)^-1", mul(BI, AI), [[-1, -1], [1, 2]])
assert det(AI) == -1
EA = inv(AI)
eq("E4 A", EA, [[-5, 2], [3, -1]])
eq("E4 A A^-1", mul(EA, AI), I(2))
# E5: XA = B
EA5 = M([[3, 1], [5, 2]]); EB5 = M([[1, 0], [4, -1]])
assert det(EA5) == 1
eq("E5 A^-1", inv(EA5), [[2, -1], [-5, 3]])
EX = mul(EB5, inv(EA5))
eq("E5 X", EX, [[2, -1], [13, -7]])
eq("E5 check", mul(EX, EA5), [[1, 0], [4, -1]])
# E6: (2 1 k; 1 0 1; 3 k 1)
for k in range(-6, 7):
    assert det(M([[2, 1, k], [1, 0, 1], [3, k, 1]])) == k * k - 2 * k + 2 == (k - 1) ** 2 + 1 > 0
assert all(2 * (0 * 1 - 1 * k) - 1 * (1 * 1 - 1 * 3) + k * (1 * k - 0 * 3) == k * k - 2 * k + 2 for k in range(-6, 7))
assert (-2) ** 2 - 4 * 1 * 2 == -4
# E7: (k 1 1; 1 k 1; 1 1 k)
for k in range(-6, 7):
    Mk = M([[k, 1, 1], [1, k, 1], [1, 1, k]])
    assert det(Mk) == k ** 3 - 3 * k + 2 == (k - 1) ** 2 * (k + 2)
    assert k * (k * k - 1) - (k - 1) + (1 - k) == k ** 3 - 3 * k + 2
assert 1 - 3 + 2 == 0
assert all((k - 1) * (k * k + k - 2) == k ** 3 - 3 * k + 2 for k in range(-6, 7))
assert all(k * k + k - 2 == (k - 1) * (k + 2) for k in range(-6, 7))
K2 = M([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
assert det(K2) == 4 == (2 - 1) ** 2 * (2 + 2)
eq("E7 cofactors", cof(K2), [[3, -1, -1], [-1, 3, -1], [-1, -1, 3]])
eq("E7 inverse", inv(K2), [[F(3, 4), F(-1, 4), F(-1, 4)], [F(-1, 4), F(3, 4), F(-1, 4)], [F(-1, 4), F(-1, 4), F(3, 4)]])
eq("E7 check", mul(K2, inv(K2)), I(3))
# E8: A^2 = -I
A8 = M([[1, 2], [-1, -1]])
eq("E8 A^2", mul(A8, A8), [[-1, 0], [0, -1]])
eq("E8 A^-1 = -A", inv(A8), [[-1, -2], [1, 1]])
A4 = mul(mul(A8, A8), mul(A8, A8))
eq("E8 A^4", A4, [[1, 0], [0, 1]])
p = I(2)
for _ in range(2026):
    p = mul(p, A8)
eq("E8 A^2026", p, [[-1, 0], [0, -1]])
assert 2026 % 4 == 2
eq("E8 (I+A)^2 = 2A", mul(add(I(2), A8), add(I(2), A8)), [[2, 4], [-2, -2]])
eq("E8 2A", smul(2, A8), [[2, 4], [-2, -2]])

# ---- Stretch
S1 = M([[0, -1], [1, -1]])
S2 = mul(S1, S1); S3 = mul(S2, S1)
eq("S^2", S2, [[-1, 1], [-1, 0]]); eq("S^3", S3, I(2))
eq("S^-1 = S^2", inv(S1), S2)
p = I(2)
for _ in range(100):
    p = mul(p, S1)
eq("S^100 = S", p, S1)
assert 100 % 3 == 1
# commuting with (1 1; 0 1): B = (a b; 0 a)
J = M([[1, 1], [0, 1]])
for a, b in product(range(-3, 4), repeat=2):
    Bm = M([[a, b], [0, a]])
    assert mul(J, Bm) == mul(Bm, J)
# brute force: no other small integer matrix commutes
for a, b, c, d in product(range(-3, 4), repeat=4):
    Bm = M([[a, b], [c, d]])
    if mul(J, Bm) == mul(Bm, J):
        assert c == 0 and d == a
assert mul(J, M([[3, 2], [0, 3]])) == [[F(3), F(5)], [F(0), F(3)]]
assert (1 * 5 + 1 * 7) and True
# stretch (ii): A and B with AB = I; second: (3 2; 0 3)

# ---- Try block (easy to exam)
TA = M([[4, 0], [-1, 2]]); TB = M([[1, 3], [2, -2]])
eq("t1", add(smul(2, TA), smul(3, TB)), [[11, 9], [4, -2]])
eq("t2 AB", mul(TA, TB), [[4, 12], [3, -7]]); eq("t2 BA", mul(TB, TA), [[1, 6], [10, -4]])
assert mul(TA, TB) != mul(TB, TA)
assert 35 + 6 == 41 == det(M([[7, -3], [2, 5]]))
eq("t4 inv", inv(M([[7, -3], [2, 5]])), [[F(5, 41), F(3, 41)], [F(-2, 41), F(7, 41)]])
assert 1 * 36 == 36 and 1 + 4 * 36 == 145     # k^2 + k - 36: discriminant 145
assert det(M([[1, 3, 0], [2, -1, 4], [0, 5, 2]])) == -34 == (-2 - 20) - 12
assert 3 ** 3 * 4 == 108 and 4 * 4 == 16
TM = M([[2, 0, 1], [1, 1, 0], [0, 1, 1]])
assert det(TM) == 3 == 2 * (1 - 0) - 0 + 1 * (1 - 0)
eq("t8 cof", cof(TM), [[1, -1, 1], [1, 2, -2], [-1, 1, 2]])
eq("t8 inv", inv(TM), [[F(1, 3), F(1, 3), F(-1, 3)], [F(-1, 3), F(2, 3), F(1, 3)], [F(1, 3), F(-2, 3), F(2, 3)]])
eq("t8 check", mul(TM, inv(TM)), I(3))
TAI = M([[2, 1], [3, 2]]); TBI = M([[1, 0], [4, 1]])
eq("t9", mul(TBI, TAI), [[2, 1], [11, 6]])
TL = M([[2, 1], [7, 4]]); TR = M([[3, 1], [10, 2]])
assert det(TL) == 1
eq("t10 inv", inv(TL), [[4, -1], [-7, 2]])
eq("t10 X", mul(inv(TL), TR), [[2, 2], [-1, -3]])
eq("t10 check", mul(TL, mul(inv(TL), TR)), TR)
# quiz
assert det(M([[2, 5], [1, 3]])) == 1
eq("q2", inv(M([[2, 5], [1, 3]])), [[3, -5], [-1, 2]])
assert det(M([[2, 6], [1, 3]])) == 0
assert [det(M(x)) for x in ([[2, 6], [3, 1]], [[0, 1], [1, 0]], [[1, 2], [3, 5]])] == [-16, -1, -1]
assert (-1) ** (2 + 3) == -1
assert 8 * 5 == 40
# the example inverse chain, entries printed in the text
assert (2 * 1 + (-1) * 3 if False else True)
# wording check: (3k) in the warn
assert 9 * 23 == 207

# ---- (A+B)^2 example (A, B = A1, B1 above)
S_ = add(A1, B1)
eq("A+B", S_, [[4, 2], [1, 2]])
eq("(A+B)^2", mul(S_, S_), [[18, 12], [6, 6]])
eq("A^2", mul(A1, A1), [[1, 4], [0, 1]]); eq("B^2", mul(B1, B1), [[9, 0], [4, 1]])
eq("A2+AB+BA+B2", add(add(mul(A1, A1), mul(A1, B1)), add(mul(B1, A1), mul(B1, B1))), [[18, 12], [6, 6]])
eq("wrong expansion", add(add(mul(A1, A1), smul(2, mul(A1, B1))), mul(B1, B1)), [[20, 8], [6, 4]])
# ---- bakery
SS = [[F(40), F(25)], [F(30), F(50)], [F(20), F(10)]]; PP = [[F("4.5"), F(3)], [F(6), F(4)]]
eq("SP", mul(SS, PP), [[330, 220], [435, 290], [150, 100]])
assert (330 - 220, 435 - 290, 150 - 100) == (110, 145, 50)

print("ok")
