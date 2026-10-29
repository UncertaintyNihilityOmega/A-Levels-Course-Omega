# checks/bio.inheritance.py: recomputes every ratio and probability in the monohybrid inheritance chapter.
from fractions import Fraction as Fr
from collections import Counter
from itertools import product
from math import isclose

n = 0


def eq(label, got, want, tol=0):
    global n
    n += 1
    if isinstance(want, float):
        assert isclose(float(got), want, rel_tol=0, abs_tol=tol or 1e-9), f"{label}: computed {got}, chapter says {want}"
    else:
        assert got == want, f"{label}: computed {got}, chapter says {want}"


def cross(p1, p2):
    """Offspring genotype Counter for two parents given as tuples of alleles (autosomal, one gene each).
    Alleles are strings; each parent's gametes are its two alleles. Result keys are sorted tuples."""
    c = Counter()
    for a, b in product(p1, p2):
        c[tuple(sorted((a, b)))] += 1
    return c


def prob(c, pred):
    tot = sum(c.values())
    return Fr(sum(v for k, v in c.items() if pred(k)), tot)


# --- eg1 peas: TT x tt -> Tt; Tt x Tt -> 1 TT : 2 Tt : 1 tt, 3 tall : 1 dwarf ----------------------------------
f1 = cross(("T", "T"), ("t", "t"))
eq("F1 all Tt", f1, Counter({("T", "t"): 4}))
f2 = cross(("T", "t"), ("T", "t"))
eq("F2 TT", f2[("T", "T")], 1)
eq("F2 Tt", f2[("T", "t")], 2)
eq("F2 tt", f2[("t", "t")], 1)
tall = prob(f2, lambda k: "T" in k)
eq("F2 tall", tall, Fr(3, 4))

# --- eg2 cattle: roan x roan -> 1 : 2 : 1; roan x white -> 1 : 1 -----------------------------------------------
c1 = cross(("R", "W"), ("R", "W"))
eq("cattle red", c1[("R", "R")], 1)
eq("cattle roan", c1[("R", "W")], 2)
eq("cattle white", c1[("W", "W")], 1)
c2 = cross(("R", "W"), ("W", "W"))
eq("roan x white: roan", c2[("R", "W")], 2)
eq("roan x white: white", c2[("W", "W")], 2)

# --- eg3 ABO: Ao x Bo -> AB, B, A, O 1:1:1:1; P(AB) = 1/4 -----------------------------------------------------
def group(k):
    s = set(k)
    if s == {"A", "B"}: return "AB"
    if "A" in s: return "A"
    if "B" in s: return "B"
    return "O"


abo = cross(("A", "o"), ("B", "o"))
eq("ABO groups", Counter(group(k) for k, v in abo.items() for _ in range(v)), Counter({"AB": 1, "B": 1, "A": 1, "O": 1}))
eq("P(AB)", prob(abo, lambda k: group(k) == "AB"), Fr(1, 4))
# practice: AB x O
abo2 = cross(("A", "B"), ("o", "o"))
eq("AB x O -> A", prob(abo2, lambda k: group(k) == "A"), Fr(1, 2))
eq("AB x O -> B", prob(abo2, lambda k: group(k) == "B"), Fr(1, 2))
eq("AB x O -> AB", prob(abo2, lambda k: group(k) == "AB"), Fr(0))
eq("AB x O -> O", prob(abo2, lambda k: group(k) == "O"), Fr(0))
# MN blood groups
mn = cross(("M", "N"), ("M", "N"))
eq("MN 1:2:1", (mn[("M", "M")], mn[("M", "N")], mn[("N", "N")]), (1, 2, 1))
eq("MN P(MN)", prob(mn, lambda k: k == ("M", "N")), Fr(1, 2))


# --- X-linked crosses ---------------------------------------------------------------------------------------
def xcross(mother, father):
    """mother: two X alleles; father: (X allele, 'Y'). Returns Counter of (sex, genotype)."""
    c = Counter()
    for a, b in product(mother, father):
        sex = "m" if b == "Y" else "f"
        c[(sex, tuple(sorted((a, b))))] += 1
    return c


# eg4 haemophilia: XH Xh x XH Y
h = xcross(("H", "h"), ("H", "Y"))
sons = {k: v for k, v in h.items() if k[0] == "m"}
daughters = {k: v for k, v in h.items() if k[0] == "f"}
eq("haemophilia: affected sons / sons", Fr(sons[("m", ("Y", "h"))], sum(sons.values())), Fr(1, 2))
eq("haemophilia: affected daughters", sum(v for k, v in daughters.items() if k[1] == ("h", "h")), 0)
eq("haemophilia: carrier daughters / daughters", Fr(daughters[("f", ("H", "h"))], sum(daughters.values())), Fr(1, 2))
eq("haemophilia: any child affected", Fr(h[("m", ("Y", "h"))], sum(h.values())), Fr(1, 4))
eq("four classes 1:1:1:1", sorted(h.values()), [1, 1, 1, 1])
# practice: colour blind man x homozygous normal woman -> daughters carriers, sons normal
cb = xcross(("B", "B"), ("Y", "b"))
eq("cb: daughters all XB Xb", cb[("f", ("B", "b"))], 2)
eq("cb: sons all XB Y", cb[("m", ("B", "Y"))], 2)
# then carrier daughter x normal man: colour-blind boy 1/4
cb2 = xcross(("B", "b"), ("B", "Y"))
eq("cb2: colour-blind boy", Fr(cb2[("m", ("Y", "b"))], sum(cb2.values())), Fr(1, 4))
# colour-blind woman x normal man: sons all colour blind
cb3 = xcross(("b", "b"), ("B", "Y"))
eq("cb3: sons all Xb Y", cb3[("m", ("Y", "b"))], 2)
# PED2: II-3 XH Xh x II-4 XH Y -> affected boy 1/4
eq("ped2 affected boy", Fr(h[("m", ("Y", "h"))], sum(h.values())), Fr(1, 4))
# cats: XB XO x XO Y -> 1:1:1:1, black male 1/4
cat = xcross(("B", "O"), ("O", "Y"))
eq("cats classes", sorted(cat.values()), [1, 1, 1, 1])
eq("cats black male", Fr(cat[("m", ("B", "Y"))], sum(cat.values())), Fr(1, 4))

# --- test cross: Ll x ll -> 1:1; observed 53 : 49 -----------------------------------------------------------------
tc = cross(("L", "l"), ("l", "l"))
eq("test cross Ll", tc[("L", "l")], 2)
eq("test cross ll", tc[("l", "l")], 2)
eq("fruit fly total", 53 + 49, 102)
eq("rabbit Bb x bb 1:1", cross(("B", "b"), ("b", "b"))[("B", "b")], 2)
eq("rabbit brown prob", prob(cross(("B", "b"), ("b", "b")), lambda k: k == ("b", "b")), Fr(1, 2))

# --- pedigree 1: Hh x Hh; III-1 unaffected -> P(carrier) = 2/3 ----------------------------------------------------
ph = cross(("H", "h"), ("H", "h"))
eq("III-1 carrier given unaffected", Fr(ph[("H", "h")], ph[("H", "H")] + ph[("H", "h")]), Fr(2, 3))

# --- probabilities with two carriers (CF) -------------------------------------------------------------------------
a = Fr(1, 4)
eq("P affected", prob(ph, lambda k: k == ("h", "h")), Fr(1, 4))
eq("P unaffected carrier", prob(ph, lambda k: k == ("H", "h")), Fr(1, 2))
eq("two affected", a * a, Fr(1, 16))
eq("27/64", (1 - a) ** 3, Fr(27, 64))
eq("at least one of three", 1 - (1 - a) ** 3, Fr(37, 64))
eq("37/64 approx 0.58", float(Fr(37, 64)), 0.58, 0.005)
# quiz: both unaffected
eq("quiz both unaffected", (1 - a) ** 2, Fr(9, 16))

# --- guinea pigs: Bb x Bb -> white 1/4 ---------------------------------------------------------------------------
eq("guinea pig white", prob(cross(("B", "b"), ("B", "b")), lambda k: k == ("b", "b")), Fr(1, 4))

# --- tomato data: 146 : 54 against 3 : 1 in 200 -------------------------------------------------------------------
eq("tomato total", 146 + 54, 200)
eq("expected red", Fr(3, 4) * 200, 150)
eq("expected yellow", Fr(1, 4) * 200, 50)
eq("ratio red:yellow", round(146 / 54, 1), 2.7)

# --- Huntington: Hh x hh -> 1 : 1; two unaffected children 1/4 ------------------------------------------------------
hd = cross(("H", "h"), ("h", "h"))
eq("HD affected prob", prob(hd, lambda k: "H" in k), Fr(1, 2))
eq("HD two unaffected", Fr(1, 2) * Fr(1, 2), Fr(1, 4))

# --- Manx cats: Mm x Mm, MM dies -> 2 Manx : 1 normal; P(Manx) = 2/3 ----------------------------------------------
mx = cross(("M", "m"), ("M", "m"))
live = {k: v for k, v in mx.items() if k != ("M", "M")}
eq("Manx live 2:1", (live[("m", "M")] if ("m", "M") in live else live[("M", "m")], live[("m", "m")]), (2, 1))
eq("Manx P(tailless | live)", Fr(live[("M", "m")], sum(live.values())), Fr(2, 3))

# --- quiz: Aa x Aa genotypes 1 : 2 : 1 ---------------------------------------------------------------------------
aa = cross(("A", "a"), ("A", "a"))
eq("quiz 1:2:1", (aa[("A", "A")], aa[("A", "a")], aa[("a", "a")]), (1, 2, 1))
eq("quiz Aa carrier prob", prob(aa, lambda k: k == ("A", "a")), Fr(1, 2))

print(f"ok ({n} checks)")
