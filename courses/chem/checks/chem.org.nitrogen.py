# checks/chem.org.nitrogen.py: recomputes every number in the Amines, amides and amino acids chapter.
# Ar values from the 9701 Periodic Table (data/elements.json): H 1.0, C 12.0, N 14.0, O 16.0, Br 79.9.
# Isoelectric points (gly 5.97, ala 6.00, lys 9.74, asp 2.77, glu 3.22) are standard table values quoted in the text and given as data in the questions.
from math import isclose
from itertools import product, permutations

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sp(charge=0, **atoms):
    return (atoms, charge)

def balanced(label, lhs, rhs):
    global n
    n += 1
    def tot(side):
        atoms, q = {}, 0
        for c, (a, ch) in side:
            for k, v in a.items():
                atoms[k] = atoms.get(k, 0) + c * v
            q += c * ch
        return atoms, q
    la, lq = tot(lhs); ra, rq = tot(rhs)
    assert la == ra and lq == rq, f"{label}: not balanced: {la} {lq} vs {ra} {rq}"

H, C, N, O, Br = 1.0, 12.0, 14.0, 16.0, 79.9
H2 = sp(H=2)

# equations
balanced("EtBr + 2NH3", [(1, sp(C=2, H=5, Br=1)), (2, sp(N=1, H=3))], [(1, sp(C=2, H=7, N=1)), (1, sp(N=1, H=4, Br=1))])
balanced("nitrile + 4[H]", [(1, sp(C=3, H=5, N=1)), (4, sp(H=1))], [(1, sp(C=3, H=9, N=1))])
balanced("amide + 4[H]", [(1, sp(C=2, H=5, N=1, O=1)), (4, sp(H=1))], [(1, sp(C=2, H=7, N=1)), (1, H2 and sp(H=2, O=1))])
balanced("N-Me amide + 4[H]", [(1, sp(C=3, H=7, N=1, O=1)), (4, sp(H=1))], [(1, sp(C=3, H=9, N=1)), (1, sp(H=2, O=1))])
balanced("nitrobenzene reduction", [(1, sp(C=6, H=5, N=1, O=2)), (6, sp(H=1)), (1, sp(1, H=1))], [(1, sp(1, C=6, H=8, N=1)), (2, sp(H=2, O=1))])
balanced("phenylammonium + OH-", [(1, sp(1, C=6, H=8, N=1)), (1, sp(-1, O=1, H=1))], [(1, sp(C=6, H=7, N=1)), (1, sp(H=2, O=1))])
balanced("phenylamine + 3Br2", [(1, sp(C=6, H=7, N=1)), (3, sp(Br=2))], [(1, sp(C=6, H=4, N=1, Br=3)), (3, sp(H=1, Br=1))])
balanced("diazotisation", [(1, sp(C=6, H=7, N=1)), (1, sp(H=1, N=1, O=2)), (1, sp(H=1, Cl=1))], [(1, sp(1, C=6, H=5, N=2)), (1, sp(-1, Cl=1)), (2, sp(H=2, O=1))])
balanced("diazonium + water", [(1, sp(1, C=6, H=5, N=2)), (1, sp(H=2, O=1))], [(1, sp(C=6, H=6, O=1)), (1, sp(N=2)), (1, sp(1, H=1))])
balanced("coupling", [(1, sp(C=6, H=5, N=2, Cl=1)), (1, sp(C=6, H=6, O=1)), (1, sp(Na=1, O=1, H=1))],
         [(1, sp(C=12, H=10, N=2, O=1)), (1, sp(Na=1, Cl=1)), (1, sp(H=2, O=1))])
balanced("amide hydrolysis acid", [(1, sp(C=2, H=5, N=1, O=1)), (1, sp(1, H=1)), (1, sp(H=2, O=1))], [(1, sp(C=2, H=4, O=2)), (1, sp(1, N=1, H=4))])
balanced("amide hydrolysis alkali", [(1, sp(C=2, H=5, N=1, O=1)), (1, sp(-1, O=1, H=1))], [(1, sp(-1, C=2, H=3, O=2)), (1, sp(N=1, H=3))])
balanced("N-Me amide acid", [(1, sp(C=3, H=7, N=1, O=1)), (1, sp(1, H=1)), (1, sp(H=2, O=1))], [(1, sp(C=2, H=4, O=2)), (1, sp(1, C=1, H=6, N=1))])
balanced("N-Me amide alkali", [(1, sp(C=3, H=7, N=1, O=1)), (1, sp(-1, O=1, H=1))], [(1, sp(-1, C=2, H=3, O=2)), (1, sp(C=1, H=5, N=1))])
balanced("EtBr + 2MeNH2", [(1, sp(C=2, H=5, Br=1)), (2, sp(C=1, H=5, N=1))], [(1, sp(C=3, H=9, N=1)), (1, sp(1, C=1, H=6, N=1)), (1, sp(-1, Br=1))])
balanced("dipeptide formation", [(1, sp(C=2, H=5, N=1, O=2)), (1, sp(C=3, H=7, N=1, O=2))], [(1, sp(C=5, H=10, N=2, O=3)), (1, sp(H=2, O=1))])
balanced("amino acid zwitterion", [(1, sp(C=2, H=5, N=1, O=2))], [(1, sp(C=2, H=5, N=1, O=2))])
balanced("zwitterion + OH-", [(1, sp(0, C=2, H=5, N=1, O=2)), (1, sp(-1, O=1, H=1))], [(1, sp(-1, C=2, H=4, N=1, O=2)), (1, sp(H=2, O=1))])
balanced("acyl chloride + SOCl2 route", [(1, sp(C=3, H=6, O=2)), (1, sp(S=1, O=1, Cl=2))], [(1, sp(C=3, H=5, O=1, Cl=1)), (1, sp(S=1, O=2)), (1, sp(H=1, Cl=1))])
balanced("propanoyl chloride + NH3", [(1, sp(C=3, H=5, O=1, Cl=1)), (2, sp(N=1, H=3))], [(1, sp(C=3, H=7, N=1, O=1)), (1, sp(N=1, H=4, Cl=1))])
balanced("propanamide + 4[H]", [(1, sp(C=3, H=7, N=1, O=1)), (4, sp(H=1))], [(1, sp(C=3, H=9, N=1)), (1, sp(H=2, O=1))])

# worked example: tribromophenylamine yield
Mr_pa = 6 * C + 7 * H + N
Mr_tb = 6 * C + 4 * H + 3 * Br + N
eq("Mr phenylamine", Mr_pa, 93.0)
eq("Mr tribromophenylamine", round(Mr_tb, 1), 329.7)
npa = 1.86 / Mr_pa
eq("tb moles", round(npa, 4), 0.0200)
mmax = npa * Mr_tb
eq("tb max", round(mmax, 3), 6.594)
eq("tb yield", round(5.43 / mmax * 100, 1), 82.3)

# ethanamide hydrolysis: NH3 volume at rtp
Mr_am = 2 * C + 5 * H + N + O
eq("Mr ethanamide", Mr_am, 59.0)
nam = 2.95 / Mr_am
eq("ethanamide moles", round(nam, 4), 0.0500)
eq("NH3 volume", round(nam * 24.0, 2), 1.20)

# peptides
Mr_gly = 2 * C + 5 * H + N + 2 * O
Mr_ala = 3 * C + 7 * H + N + 2 * O
eq("Mr gly", Mr_gly, 75.0)
eq("Mr ala", Mr_ala, 89.0)
Mr_water = 2 * H + O
eq("Mr water", Mr_water, 18.0)
eq("Mr Gly-Ala", Mr_gly + Mr_ala - Mr_water, 146.0)
eq("Mr Gly-Ala from formula C5H10N2O3", 5 * C + 10 * H + 2 * N + 3 * O, 146.0)
eq("Mr GlyGlyGly", 3 * Mr_gly - 2 * Mr_water, 189.0)
eq("dipeptides from 2 amino acids", len(list(product("GA", repeat=2))), 4)
eq("quiz dipeptides", 2 ** 2, 4)

# exam practice: nitrobenzene -> phenylamine
Mr_nb = 6 * C + 5 * H + N + 2 * O
eq("Mr nitrobenzene", Mr_nb, 123.0)
nn = 9.84 / Mr_nb
eq("nb moles", round(nn, 4), 0.0800)
mm = nn * Mr_pa
eq("pa max", round(mm, 2), 7.44)
eq("pa yield", round(5.58 / mm * 100, 1), 75.0)

# charges of amino acids (net charge = sum of group charges)
def charge(nh3, coo):
    return nh3 - coo
eq("Lys pH1", charge(2, 0), 2)
eq("Asp pH12", charge(0, 2), -2)
eq("Gly-Lys pH7", 1 - 1 + 1, 1)
eq("Gly-Asp pH7", 1 - 1 - 1, -1)
eq("Lys pH6", charge(2, 1), 1)
eq("Glu pH6", charge(1, 2), -1)

# pI sense: compare pH with pI
pI = {"gly": 5.97, "ala": 6.00, "lys": 9.74, "asp": 2.77, "glu": 3.22}
def sign(aa, ph, tol=0.005):
    if abs(ph - pI[aa]) <= tol: return 0
    return 1 if ph < pI[aa] else -1
eq("ala pH6.00", sign("ala", 6.00), 0)
eq("lys pH6.00", sign("lys", 6.00), 1)
eq("glu pH6.00", sign("glu", 6.00), -1)
eq("asp pH8", sign("asp", 8), -1)
eq("gly pH8", sign("gly", 8), -1)
eq("lys pH8", sign("lys", 8), 1)
eq("quiz pI6 pH9", sign("ala", 9), -1)

# quiz: methylamine + HCl
nMe = 0.0250 * 0.100
eq("quiz HCl volume cm3", round(nMe / 0.200 * 1000, 2), 12.5)

# dipeptide count with tripeptide note (not in text beyond the formula 2 x 2)
eq("permutations of 3", len(list(permutations("GAL"))), 6)

print("ok")
