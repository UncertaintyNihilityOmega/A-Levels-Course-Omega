# checks/bio.synthesis.py: recomputes every sequence and number in the protein synthesis chapter (chapters/bio.synthesis.md).
# The genetic code comes from data/codon_table.py (generated and asserted: 64 codons, 61 sense, 3 stop), never typed by hand.
import os, sys
from math import isclose

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data"))
from codon_table import CODE, FULL, transcribe, translate  # noqa: E402

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def same(label, got, want):
    global n
    n += 1
    assert got == want, f"{label}: computed {got!r}, chapter says {want!r}"


PAIR = {"A": "T", "T": "A", "C": "G", "G": "C"}


def rna_comp(m):
    """anticodon (or complement) of an RNA sequence, base by base (A-U, C-G)."""
    return "".join({"A": "U", "U": "A", "C": "G", "G": "C"}[b] for b in m)


def codons(m):
    return [m[i:i + 3] for i in range(0, len(m) - len(m) % 3, 3)]


def aa(m, upto=None):
    return "-".join(CODE[c] for c in codons(m)[:upto])


# --- the code itself ---------------------------------------------------------------------------------------------
eq("possible codons", 4 ** 3, 64)
eq("two bases give only", 4 * 4, 16)
eq("sense codons", sum(v != "STOP" for v in CODE.values()), 61)
eq("stop codons", sum(v == "STOP" for v in CODE.values()), 3)
same("start codon", CODE["AUG"], "Met")
same("stop codons are UAA UAG UGA", sorted(c for c, v in CODE.items() if v == "STOP"), ["UAA", "UAG", "UGA"])
for c, a in {"CCA": "Pro", "CCG": "Pro", "GAA": "Glu", "GAG": "Glu", "GAC": "Asp", "UUU": "Phe", "GGG": "Gly", "UCC": "Ser",
             "AGA": "Arg", "AUU": "Ile", "UGG": "Trp", "GUA": "Val", "CAG": "Gln", "AAU": "Asn", "UUG": "Leu", "GGU": "Gly",
             "UAC": "Tyr", "GUG": "Val", "UGA": "STOP", "UAG": "STOP", "UAA": "STOP"}.items():
    same(f"code {c}", CODE[c], a)
same("glutamic acid", FULL["Glu"], "glutamic acid")
same("aspartic acid", FULL["Asp"], "aspartic acid")
same("valine", FULL["Val"], "valine")

# --- worked example: transcribe and translate ---------------------------------------------------------------------------
T1 = "TACGGTCTTAAACCCATC"
M1 = transcribe(T1)
same("eg mRNA", " ".join(codons(M1)), "AUG CCA GAA UUU GGG UAG")
same("eg third anticodon", rna_comp(codons(M1)[2]), "CUU")
same("eg polypeptide", "-".join(translate(M1)[:-1]), "Met-Pro-Glu-Phe-Gly")
same("eg last codon stop", translate(M1)[-1], "STOP")
same("key box: TAC -> AUG -> UAC -> Met", (transcribe("TAC"), rna_comp(transcribe("TAC")), CODE[transcribe("TAC")]), ("AUG", "UAC", "Met"))

# --- widget default (bio-codon) -----------------------------------------------------------------------------------------
WD = "TACCGAAAGTTTCCGATT"
same("widget default mRNA", " ".join(codons(transcribe(WD))), "AUG GCU UUC AAA GGC UAA")
same("widget default polypeptide", "-".join(translate(transcribe(WD))), "Met-Ala-Phe-Lys-Gly-STOP")

# --- table of changes to M1 ---------------------------------------------------------------------------------------------
def mutate_sub(m, pos, base):
    return m[:pos] + base + m[pos + 1:]


def poly(m):
    return "–".join(a for a in translate(m) if a != "STOP")


m = M1
same("sub CCA->CCG mRNA", " ".join(codons(mutate_sub(m, 5, "G"))), "AUG CCG GAA UUU GGG UAG")
same("sub CCA->CCG poly", poly(mutate_sub(m, 5, "G")), "Met–Pro–Glu–Phe–Gly")
same("sub GAA->GAC mRNA", " ".join(codons(mutate_sub(m, 8, "C"))), "AUG CCA GAC UUU GGG UAG")
same("sub GAA->GAC poly", poly(mutate_sub(m, 8, "C")), "Met–Pro–Asp–Phe–Gly")
same("sub GAA->UAA mRNA", " ".join(codons(mutate_sub(m, 6, "U"))), "AUG CCA UAA UUU GGG UAG")
same("sub GAA->UAA poly", poly(mutate_sub(m, 6, "U")), "Met–Pro")
ins = m[:3] + "U" + m[3:]
same("insertion mRNA", " ".join(codons(ins)) + " " + ins[len(ins) - len(ins) % 3:], "AUG UCC AGA AUU UGG GUA G")
same("insertion poly (reads past the old stop)", "–".join(CODE[c] for c in codons(ins)), "Met–Ser–Arg–Ile–Trp–Val")
dele = m[:3] + m[6:]
same("3-base deletion mRNA", " ".join(codons(dele)), "AUG GAA UUU GGG UAG")
same("3-base deletion poly", poly(dele), "Met–Glu–Phe–Gly")

# --- sickle cell ----------------------------------------------------------------------------------------------------------
same("CTC -> GAG -> Glu", (transcribe("CTC"), CODE[transcribe("CTC")]), ("GAG", "Glu"))
same("CAC -> GUG -> Val", (transcribe("CAC"), CODE[transcribe("CAC")]), ("GUG", "Val"))

# --- intron / exon worked example and exam question -----------------------------------------------------------------
ex = [150, 210, 330, 210]
intr = [420, 800, 560]
eq("exons", sum(ex), 900)
eq("introns", sum(intr), 1780)
eq("primary transcript", sum(ex) + sum(intr), 2680)
eq("codons", sum(ex) / 3, 300)
eq("amino acids", sum(ex) / 3 - 1, 299)
ex2, in2 = [114, 180, 150], [340, 610]
eq("exam: exons", sum(ex2), 444)
eq("exam: primary transcript", sum(ex2) + sum(in2), 1394)
eq("exam: codons", sum(ex2) / 3, 148)
eq("exam: amino acids", sum(ex2) / 3 - 1, 147)
eq("try: introns", 2500 - 1200, 1300)

# --- practice -------------------------------------------------------------------------------------------------------------
t = "TACGGCTTTATT"
mt = transcribe(t)
same("try mRNA", " ".join(codons(mt)), "AUG CCG AAA UAA")
same("try second anticodon", rna_comp(codons(mt)[1]), "GGC")
same("try translate", "–".join(a for a in translate("AUGUGGCAUUAA") if a != "STOP"), "Met–Trp–His")
same("try UAA stop", CODE["UAA"], "STOP")
eq("try: 120 amino acids", (120 + 1) * 3, 363)

t2 = "TACAAGGGCGAAACT"
m2 = transcribe(t2)
same("exam mRNA", " ".join(codons(m2)), "AUG UUC CCG CUU UGA")
same("exam second anticodon", rna_comp(codons(m2)[1]), "AAG")
same("exam polypeptide", "–".join(translate(m2)[:-1]), "Met–Phe–Pro–Leu")
same("exam stop", translate(m2)[-1], "STOP")

# mutants 1-3 of the exam question
base = "AUGGAACUUAAAUUUGGCUGA"
same("mutant base polypeptide", poly(base), "Met–Glu–Leu–Lys–Phe–Gly")
m_1 = mutate_sub(base, 8, "G")  # GAA -> GAG is codon 2, third base index 5
m_1 = base[:5] + "G" + base[6:]
same("mutant 1 codon", codons(m_1)[1], "GAG")
same("mutant 1 poly", poly(m_1), "Met–Glu–Leu–Lys–Phe–Gly")
m_2 = base[:9] + "U" + base[10:]
same("mutant 2 codon", codons(m_2)[3], "UAA")
same("mutant 2 poly", poly(m_2), "Met–Glu–Leu")
m_3 = base[:12] + base[13:]  # delete first U of UUU (codon 5, index 12)
same("mutant 3 mRNA codons", " ".join(codons(m_3)), "AUG GAA CUU AAA UUG GCU GA".rsplit(" ", 1)[0])
same("mutant 3 poly", "–".join(CODE[c] for c in codons(m_3)), "Met–Glu–Leu–Lys–Leu–Ala")

# stretch 1: insertion then deletion
orig = "AUGACCGGAUUCCAUGAAUUUCAGUAG"
same("stretch (a)", poly(orig), "Met–Thr–Gly–Phe–His–Glu–Phe–Gln")
ins2 = orig[:3] + "A" + orig[3:]
same("stretch (b) codons", " ".join(codons(ins2)), "AUG AAC CGG AUU CCA UGA AUU UCA GUA")
same("stretch (b) poly", poly(ins2), "Met–Asn–Arg–Ile–Pro")
i = ins2.index("GGA")  # the G of GGA that is deleted: second G (frame shift fixed by removing one G)
dbl = ins2[:i] + ins2[i + 1:]
same("stretch (c) codons", " ".join(codons(dbl)), "AUG AAC CGA UUC CAU GAA UUU CAG UAG")
same("stretch (c) poly", poly(dbl), "Met–Asn–Arg–Phe–His–Glu–Phe–Gln")
diff = [k for k, (a, b) in enumerate(zip(translate(orig), translate(dbl))) if a != b]
same("stretch (c) amino acids that differ", diff, [1, 2])
same("stretch (c) original codons 2, 3", (CODE["ACC"], CODE["GGA"]), ("Thr", "Gly"))
same("stretch (c) new codons 2, 3", (CODE["AAC"], CODE["CGA"]), ("Asn", "Arg"))

# stretch 2: repeating copolymers
same("UUU", CODE["UUU"], "Phe")
cu = "CUCUCUCUCU"
same("CU repeat codons", codons(cu), ["CUC", "UCU", "CUC"])
same("CU repeat amino acids", [CODE[c] for c in codons(cu)], ["Leu", "Ser", "Leu"])

# exam: mutant lengths
eq("exam: stop at codon 80 leaves", 80 - 1, 79)
eq("exam: 3-base deletion shortens by one", 250 - 1, 249)

# quiz
same("quiz TAC", (transcribe("TAC"), rna_comp(transcribe("TAC"))), ("AUG", "UAC"))
same("quiz UAC UAG", (CODE["UAC"], CODE["UAG"]), ("Tyr", "STOP"))
eq("quiz: 4 x 4 x 4", 4 * 4 * 4, 64)

print("ok")
