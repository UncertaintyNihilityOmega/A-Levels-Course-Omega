# data/fig_bio.classification.py: figures of chapters/bio.classification.md (three domains; the taxonomic hierarchy nesting).
# Run: py data/fig_bio.classification.py -> prints the <figure> lines (clearance report on stderr). py data/place_figs_p14.py bio.classification places them.
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p14 import Fig

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["DOM", "HIER"]

# ---------------------------------------------------------------- three domains
d = Fig("domains")
RX, N2X, TX = 100, 135, 165
ty = {"Bacteria": 30, "Archaea": 100, "Eukarya": 170}
n2 = (ty["Archaea"] + ty["Eukarya"]) / 2
root = (ty["Bacteria"] + n2) / 2
d.line([(70, root), (RX, root)], "ln sw2")
d.line([(RX, ty["Bacteria"]), (RX, n2)], "ln sw2")
d.line([(RX, ty["Bacteria"]), (TX, ty["Bacteria"])], "ln sw2")
d.line([(RX, n2), (N2X, n2)], "ln sw2")
d.line([(N2X, ty["Archaea"]), (N2X, ty["Eukarya"])], "ln sw2")
d.line([(N2X, ty["Archaea"]), (TX, ty["Archaea"])], "ln sw2")
d.line([(N2X, ty["Eukarya"]), (TX, ty["Eukarya"])], "ln sw2")
d.text(6, root - 2, "common", "tl")
d.text(6, root + 12, "ancestor", "tl")
info = {
    "Bacteria": ["peptidoglycan wall", "unbranched lipids,", "ester bonds"],
    "Archaea": ["no peptidoglycan", "branched lipids,", "ether bonds"],
    "Eukarya": ["nucleus and", "membrane-bound", "organelles"],
}
for k, y in ty.items():
    d.text(TX + 10, y + 4, k, "tl tb")
    for i, s in enumerate(info[k]):
        d.text(TX + 10, y + 20 + 14 * i, s, "tl")
dom = d.svg((340, 226),
    "A tree of the three domains. A common ancestor splits into Bacteria on one branch and a second branch that splits into Archaea and Eukarya. Bacteria: peptidoglycan wall, unbranched lipids with ester bonds. Archaea: no peptidoglycan, branched lipids with ether bonds. Eukarya: nucleus and membrane-bound organelles. Archaea and Eukarya share a more recent common ancestor than either does with Bacteria.",
    "The three domains. Archaea and Bacteria are prokaryotes; Eukarya have a nucleus. Ribosomal RNA sequences place Archaea closer to Eukarya than to Bacteria.",
    "fig small")

# ---------------------------------------------------------------- hierarchy funnel
h = Fig("hierarchy")
rows = [("Domain", "Eukarya"), ("Kingdom", "Animalia"), ("Phylum", "Chordata"), ("Class", "Mammalia"),
        ("Order", "Primates"), ("Family", "Hominidae"), ("Genus", "Homo"), ("Species", "Homo sapiens")]
CX, RH, GAP = 170, 28, 4
w0, dw = 320, 22
for i, (r, n) in enumerate(rows):
    w = w0 - i * dw
    y = 6 + i * (RH + GAP)
    h.rect(CX - w / 2, y, w, RH, "fm s-acc sw2", rx=4)
    h.text(CX, y + 19, f"{r}: {n}", "tl", "middle")
H = 6 + len(rows) * (RH + GAP) + 14
hier = h.svg((340, H),
    "A funnel of eight nested bars, each narrower than the one above. From the top: Domain Eukarya, Kingdom Animalia, Phylum Chordata, Class Mammalia, Order Primates, Family Hominidae, Genus Homo, Species Homo sapiens. Each rank is a smaller group inside the one above.",
    "The classification of a human. Each bar is a rank, drawn narrower than the one above because it holds fewer organisms, which share more features.",
    "fig small")
# REVIEW P16-P18: genus and species names are italic
hier = hier.replace(">Genus: Homo<", '>Genus: <tspan font-style="italic">Homo</tspan><').replace(
    ">Species: Homo sapiens<", '>Species: <tspan font-style="italic">Homo sapiens</tspan><')
print(dom)
print()
print(hier)
print("\n".join(d.check() + h.check()) or "clearance ok", file=sys.stderr)
