# data/codon_table.py: the standard genetic code (mRNA codons) generated from the compact 64-letter string, checked by script.
# Used by: widgets/bio-codon.js (generated block, see `py data/codon_table.py js`), the chapter table (`md`) and checks/bio.synthesis.py.
# Run: py data/codon_table.py [js|md|check]
import sys
sys.stdout.reconfigure(encoding="utf-8")
BASES = "UCAG"
# Standard code in UCAG order (first base slowest, third base fastest), one-letter amino acid per codon, * = stop.
AA1 = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
NAMES = {"F": ("Phe", "phenylalanine"), "L": ("Leu", "leucine"), "S": ("Ser", "serine"), "Y": ("Tyr", "tyrosine"),
         "C": ("Cys", "cysteine"), "W": ("Trp", "tryptophan"), "P": ("Pro", "proline"), "H": ("His", "histidine"),
         "Q": ("Gln", "glutamine"), "R": ("Arg", "arginine"), "I": ("Ile", "isoleucine"), "M": ("Met", "methionine"),
         "T": ("Thr", "threonine"), "N": ("Asn", "asparagine"), "K": ("Lys", "lysine"), "V": ("Val", "valine"),
         "A": ("Ala", "alanine"), "D": ("Asp", "aspartic acid"), "E": ("Glu", "glutamic acid"), "G": ("Gly", "glycine")}
CODONS = [a + b + c for a in BASES for b in BASES for c in BASES]
CODE = {cod: ("STOP" if aa == "*" else NAMES[aa][0]) for cod, aa in zip(CODONS, AA1)}
FULL = {NAMES[a][0]: NAMES[a][1] for a in NAMES}
assert len(AA1) == 64 and len(CODE) == 64
assert sum(v == "STOP" for v in CODE.values()) == 3 and sum(v != "STOP" for v in CODE.values()) == 61
assert {k for k, v in CODE.items() if v == "STOP"} == {"UAA", "UAG", "UGA"}
assert CODE["AUG"] == "Met" and len(set(v for v in CODE.values() if v != "STOP")) == 20
# spot checks against well-known entries
for c, a in {"UUU": "Phe", "UUA": "Leu", "GCU": "Ala", "AAA": "Lys", "GGC": "Gly", "GAG": "Glu", "GUG": "Val", "UGG": "Trp",
             "AUA": "Ile", "CAU": "His", "GAU": "Asp", "UGU": "Cys", "AGA": "Arg", "UCU": "Ser", "CUC": "Leu"}.items():
    assert CODE[c] == a, (c, a, CODE[c])
assert len([c for c, a in CODE.items() if a == "Leu"]) == 6 and len([c for c, a in CODE.items() if a == "Met"]) == 1


def transcribe(template):
    """mRNA (written 5'->3') from a template strand written 3'->5' (as in the exam): complement, T->U."""
    return "".join({"A": "U", "T": "A", "C": "G", "G": "C"}[b] for b in template)


def translate(mrna):
    """amino acids from the first AUG to the first stop (list; ends with 'STOP' if a stop is reached)."""
    i = mrna.find("AUG")
    out = []
    while i >= 0 and i + 3 <= len(mrna):
        a = CODE[mrna[i:i + 3]]
        out.append(a)
        if a == "STOP":
            break
        i += 3
    return out


def md_table():
    rows = ["| amino acid | mRNA codons |", "|---|---|"]
    by = {}
    for c in CODONS:
        by.setdefault(CODE[c], []).append(c)
    order = sorted((a for a in by if a != "STOP"), key=lambda a: FULL[a])
    for a in order:
        extra = " (start)" if a == "Met" else ""
        rows.append(f"| {FULL[a]} ({a}){extra} | {' '.join(by[a])} |")
    rows.append(f"| stop | {' '.join(by['STOP'])} |")
    return "\n".join(rows)


def js_block():
    import json
    return "const CODE = " + json.dumps(CODE, separators=(",", ":")) + ";"


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    if mode == "md":
        print(md_table())
    elif mode == "js":
        print(js_block())
    else:
        print("codon table ok: 64 codons, 61 sense, 3 stop")
