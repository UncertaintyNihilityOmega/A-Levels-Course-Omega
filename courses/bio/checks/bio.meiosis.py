# checks/bio.meiosis.py: recomputes every number in the meiosis chapter (chapters/bio.meiosis.md).
from math import exp, isclose

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- haploid numbers and the table of organisms -------------------------------------------------------------
for name, d, h in (("human", 46, 23), ("fruit fly", 8, 4), ("pea", 14, 7), ("maize", 20, 10), ("dog", 78, 39)):
    eq(f"{name} haploid", d / 2, h)
eq("practice 2n = 18 -> n", 18 / 2, 9)

# --- chromosome number doubling if gametes were diploid ----------------------------------------------------
eq("zygote if gametes diploid", 46 + 46, 92)
eq("next generation", 92 + 92, 184)


# --- counting table: human cell, 2n = 46, and the 2n = 12 worked example -------------------------------------
def counts(c):
    """(chromosomes, chromatids, DNA molecules) per cell."""
    return {
        "G1": (c, 0, c),
        "metaphase I": (c, 2 * c, 2 * c),
        "after meiosis I": (c // 2, c, c),          # per cell
        "metaphase II": (c // 2, c, c),
        "anaphase II": (c, 0, c),                   # per cell
        "after meiosis II": (c // 2, 0, c // 2),    # per cell
    }


h = counts(46)
eq("human G1 chromosomes", h["G1"][0], 46)
eq("human prophase I chromatids", h["metaphase I"][1], 92)
eq("human prophase I DNA", h["metaphase I"][2], 92)
eq("human after I chromosomes", h["after meiosis I"][0], 23)
eq("human after I chromatids", h["after meiosis I"][1], 46)
eq("human after I DNA", h["after meiosis I"][2], 46)
eq("human anaphase II chromosomes", h["anaphase II"][0], 46)
eq("human after II chromosomes", h["after meiosis II"][0], 23)
eq("human after II DNA", h["after meiosis II"][2], 23)
t = counts(12)
for label, key, want in (("G1", "G1", (12, 0, 12)), ("metaphase I", "metaphase I", (12, 24, 24)),
                         ("after I", "after meiosis I", (6, 12, 12)), ("anaphase II", "anaphase II", (12, 0, 12)),
                         ("after II", "after meiosis II", (6, 0, 6))):
    for i in range(3):
        eq(f"eg 2n=12 {label} col {i}", t[key][i], want[i])

# --- DNA content plot ---------------------------------------------------------------------------------------
def dna(x):
    s = lambda c: 1 / (1 + exp(0 - (x - c) * 3))
    return 2 + 2 * s(6) - 2 * s(16) - 1 * s(24)


eq("DNA at 0", dna(0), 2, 1e-3)
eq("DNA at 11 (S phase done)", dna(11), 4, 1e-3)
eq("DNA at 20 (meiosis I over)", dna(20), 2, 1e-3)
eq("DNA at 28 (meiosis II over)", dna(28), 1, 1e-3)
eq("DNA at 6 (halfway through S)", dna(6), 3, 1e-2)
eq("S phase doubles DNA", dna(11) / dna(0), 2, 1e-3)

# --- combinations ------------------------------------------------------------------------------------------
eq("eg 2n=6 haploid", 6 / 2, 3)
eq("eg gametes 2^3", 2 ** 3, 8)
eq("eg zygotes 8x8", 8 * 8, 64)
eq("2^23", 2 ** 23, 8388608)
eq("2^23 in millions (8.4)", sf(2 ** 23 / 1e6, 2), 8.4)
eq("2^46 = 2^23 x 2^23", 2 ** 23 * 2 ** 23, 2 ** 46)
eq("2^46 mantissa (7.0e13)", sf(2 ** 46 / 1e13, 2), 7.0)
eq("2^2 orientations pairs", 2 ** 2, 4)
eq("quiz 2^7", 2 ** (14 // 2), 128)
eq("quiz distractor 7^2", 7 ** 2, 49)
eq("try 2^5 (2n=10)", 2 ** (10 // 2), 32)

# --- practice: mouse 2n = 40 ---------------------------------------------------------------------------------
eq("mouse n", 40 // 2, 20)
eq("mouse gametes 2^20", 2 ** 20, 1048576)
eq("mouse zygotes 2^40 mantissa", sf(2 ** 40 / 1e12, 2), 1.1)
eq("mouse zygotes", 2 ** 20 * 2 ** 20, 2 ** 40)

# --- practice: cell 2n = 8 -----------------------------------------------------------------------------------
eq("2n=8 metaphase II chromosomes", 8 // 2, 4)
eq("2n=8 metaphase II chromatids", 2 * (8 // 2), 8)
eq("2n=8 mitosis anaphase chromatids per pole", 8, 8)
eq("2n=8 anaphase II chromatids per pole", 8 // 2, 4)

# --- practice: DNA of a body cell 5.4 pg ----------------------------------------------------------------------
eq("metaphase I DNA", 2 * 5.4, 10.8)
eq("after telophase I DNA", 2 * 5.4 / 2, 5.4)
eq("sperm DNA", 5.4 / 2, 2.7)
eq("zygote DNA", 2.7 + 2.7, 5.4)

# --- stretch: Down syndrome and the mule ------------------------------------------------------------------------
eq("normal gamete", 46 // 2, 23)
eq("gamete with extra chromosome", 23 + 1, 24)
eq("gamete missing a chromosome", 23 - 1, 22)
eq("trisomy zygote", 24 + 23, 47)
eq("horse gamete", 64 / 2, 32)
eq("donkey gamete", 62 / 2, 31)
eq("mule", 32 + 31, 63)

# --- anther squash: lily 2n = 24 -------------------------------------------------------------------------------
eq("lily bivalents", 24 / 2, 12)

# --- eg 4 cells from 2n = 6 plant -----------------------------------------------------------------------------------
eq("anaphase I poles (2n=6)", 6 / 2, 3)
eq("telophase II n (2n=6)", 6 / 2, 3)

print(f"ok ({n} checks)")
