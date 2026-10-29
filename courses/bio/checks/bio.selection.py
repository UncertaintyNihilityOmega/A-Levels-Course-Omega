# checks/bio.selection.py: recomputes every number in the Natural and artificial selection chapter.
from math import isclose, sqrt
from fractions import Fraction

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def hw(q2):
    q = sqrt(q2)
    p = 1 - q
    return p, q, p * p, 2 * p * q, q * q


# --- Warm-up -----------------------------------------------------------------------------------------------
eq("Aa x Aa gives aa 1/4", Fraction(1, 4) * 1.0, 0.25)

# --- Beetles (worked example) -----------------------------------------------------------------------------
gen = [0, 2, 4, 6, 8, 10]
dark = [8, 14, 26, 44, 63, 78]
eq("beetles 4 to 8: 26 to 63", dark[4] - dark[2], 37)
eq("beetles about 9 points per generation", round((63 - 26) / 4), 9)
eq("beetles biggest rise is gens 4 to 8", int(max(range(len(dark) - 2), key=lambda i: dark[i + 2] - dark[i])), 2)

# --- Lizards ---------------------------------------------------------------------------------------------------
before = [10, 20, 40, 20, 10]
after = [2, 18, 60, 18, 2]
eq("lizards before total 100", sum(before), 100)
eq("lizards after total 100", sum(after), 100)

# --- Founder effect -----------------------------------------------------------------------------------------
qi = 3 / 16
eq("founder q", round(qi, 2), 0.19)
eq("founder q^2 on the island", round(qi ** 2, 3), 0.035)
eq("founder mainland q^2", 0.02 ** 2, 0.0004)
eq("founder about 88 times", round(qi ** 2 / 0.02 ** 2), 88)
eq("founder island 3.5 %", round(qi ** 2 * 100, 1), 3.5)

# --- Hardy-Weinberg: 1 in 2500 --------------------------------------------------------------------------------
p, q, p2, h, q2 = hw(1 / 2500)
eq("cf q^2", 1 / 2500, 0.0004)
eq("cf q", q, 0.02)
eq("cf p", p, 0.98)
eq("cf 2pq", h, 0.0392)
eq("cf p^2", p2, 0.9604, 1e-12)
eq("cf carriers in a million", round(h * 1_000_000), 39200)
eq("cf about 1 in 26 (1/0.0392 = 25.5)", round(1 / h), 26)
eq("cf genotypes sum to 1", p2 + h + q2, 1, 1e-12)

# --- Purple and white plants ------------------------------------------------------------------------------------
p, q, p2, h, q2 = hw(0.09)
eq("plants q", q, 0.30)
eq("plants p", p, 0.70)
eq("plants 2pq", h, 0.42)
eq("plants p^2", p2, 0.49)
eq("plants sum", p2 + h + q2, 1, 1e-12)
eq("plants about 46 % of purple are Aa", round(42 / 91 * 100), 46)
eq("plants dominant phenotype 91 %", p2 + h, 0.91)

# --- Mice genotype counts ---------------------------------------------------------------------------------------
AA, Aa, aa = 280, 140, 80
eq("mice total", AA + Aa + aa, 500)
eq("mice copies of A", 2 * AA + Aa, 700)
eq("mice p", (2 * AA + Aa) / 1000, 0.70)
eq("mice expected AA", 0.49 * 500, 245)
eq("mice expected Aa", 0.42 * 500, 210)
eq("mice expected aa", 0.09 * 500, 45, 1e-9)

# --- Rabbits ------------------------------------------------------------------------------------------------------
eq("rabbits q 1990", sqrt(0.09), 0.30)
eq("rabbits q 2020", sqrt(0.2025), 0.45)

# --- Practice -----------------------------------------------------------------------------------------------------
p, q, p2, h, q2 = hw(1 / 10000)
eq("try q", q, 0.01)
eq("try 2pq", h, 0.0198)
eq("try AA", 0.8 ** 2, 0.64)
eq("try Aa", 2 * 0.8 * 0.2, 0.32)
eq("try aa", 0.2 ** 2, 0.04)
rats_y = [0, 3, 6, 9, 12]
rats = [2, 6, 19, 48, 74]
eq("rats fastest 6 to 9", rats[3] - rats[2], 29)
assert rats[3] - rats[2] > rats[4] - rats[3] > rats[1] - rats[0]
p, q, p2, h, q2 = hw(0.16)
eq("snails q", q, 0.4)
eq("snails p", p, 0.6)
eq("snails 2pq", h, 0.48)
eq("snails 240 in 500", round(h * 500), 240)
eq("ladybirds copies of B", 2 * 144 + 192, 480)
eq("ladybirds total", 144 + 192 + 64, 400)
eq("ladybirds p", 480 / 800, 0.6)
eq("ladybirds observed equal expected", 144 - 0.36 * 400 + 192 - 0.48 * 400 + 64 - 0.16 * 400, 0, 1e-9)
eq("milk: best over worst", round((6450 - 5600) / 5600 * 100, 1), 15.2)
eq("quiz: 2pq at q = 0.25", 2 * 0.75 * 0.25, 0.375)
eq("quiz: q^2 at q = 0.25", 0.25 ** 2, 0.0625)
eq("quiz: p^2 at q = 0.25", 0.75 ** 2, 0.5625)
eq("quiz: pq at q = 0.25", 0.75 * 0.25, 0.1875)
eq("beetles exp BB", 0.36 * 400, 144, 1e-9)
eq("beetles exp Bb", 0.48 * 400, 192, 1e-9)
eq("beetles exp bb", 0.16 * 400, 64, 1e-9)
p, q, p2, h, q2 = hw(0.01)
eq("sickle q", q, 0.1)
eq("sickle 2pq", h, 0.18)
bulls = {1: 5900, 2: 6450, 3: 6150, 4: 5600}
eq("best bull is 2", max(bulls, key=bulls.get), 2)

# --- Stretch: lethal recessive -------------------------------------------------------------------------------------
q0 = 0.20
eq("lethal AA", (1 - q0) ** 2, 0.64)
eq("lethal Aa", 2 * q0 * (1 - q0), 0.32)
eq("lethal aa", q0 ** 2, 0.04)
surv = 1 - q0 ** 2
eq("lethal survivors", surv, 0.96)
eq("lethal Aa among survivors 1/3", round(0.32 / surv, 3), 0.333)
qn = 0.5 * (0.32 / surv)
eq("lethal q after one generation", round(qn, 3), 0.167)
eq("lethal q formula q/(1+q)", q0 / (1 + q0), qn, 1e-12)
# --- Stretch: bottleneck ------------------------------------------------------------------------------------------------
eq("bottleneck P(no X)", round(0.9 ** 12, 2), 0.28)
eq("bottleneck expected copies", 12 * 0.1, 1.2)

print("ok")
