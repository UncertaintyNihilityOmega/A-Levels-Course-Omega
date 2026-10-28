# data/fig_bio.translocation.py: builds the hand-drawn SVG figures of chapters/bio.translocation.md and checks label clearance.
# Run: py data/fig_bio.translocation.py -> prints each <figure> (blank line between) in the order of NAMES; clearance report on stderr.
# data/place_figs_p6.py bio.translocation replaces the @@FIG_<NAME> placeholder lines of the chapter (put each inside :::html ... :::).
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_p6 import Fig, ellipse

sys.stdout.reconfigure(encoding="utf-8")
NAMES = ["LOAD", "MASSFLOW", "RING"]
figs, problems = [], []
XY = "f2 s-acc2 sw2"
PH = "f1 s-acc sw2"

# ---------- 1. loading of sucrose into a sieve tube element by a companion cell ----------
f = Fig("loading")
f.rect(150, 16, 150, 54, "f2 ln")                                         # cell wall space (apoplast)
f.rect(150, 70, 150, 80, "f1 s-acc sw2")                                  # companion cell
f.rect(150, 150, 150, 80, "fm s-acc sw2")                                 # sieve tube element
f.rect(256, 62, 28, 16, "f2 s-acc2 sw2")                                  # proton pump
f.rect(176, 62, 30, 16, "fm s-acc sw2")                                   # cotransporter
ellipse(f, 270, 124, 16, 9, "fok s-acc sw2", check=False)                 # mitochondrion
f.line([(270, 60), (270, 28)], "c2 sw2", arrow="ah")                      # H+ out
f.line([(184, 54), (184, 104)], "c2 sw2", arrow="ah")                     # H+ in
f.line([(198, 54), (198, 104)], "c1 sw2", arrow="ah")                     # sucrose in with H+
f.line([(270, 112), (270, 82)], "c3 sw2", arrow="ah")                     # ATP to the pump
f.line([(220, 146), (220, 154)], "c3 sw3", check=False)                   # plasmodesmata
f.line([(244, 146), (244, 154)], "c3 sw3", check=False)
f.line([(232, 112), (232, 200)], "c1 sw2", arrow="ah")                    # sucrose through plasmodesmata
f.text(278, 44, "H⁺")
f.text(160, 52, "H⁺")
f.text(203, 38, "sucrose")
f.text(265, 100, "ATP", anchor="end")
f.text(232, 218, "sucrose")
LX, RX = 138, 312
f.text(LX, 30, "cell wall space:", anchor="end"); f.text(LX, 44, "high in H⁺", anchor="end"); f.leader((LX + 4, 36), (150, 36))
f.text(LX, 88, "cotransporter", anchor="end"); f.leader((LX + 4, 85), (174, 71))
f.text(LX, 118, "companion cell", anchor="end"); f.leader((LX + 4, 115), (158, 115))
f.text(LX, 160, "plasmodesmata", anchor="end"); f.leader((LX + 4, 157), (214, 150))
f.text(LX, 200, "sieve tube", anchor="end"); f.text(LX, 214, "element", anchor="end"); f.leader((LX + 4, 207), (158, 207))
f.text(RX, 84, "proton pump"); f.leader((RX - 4, 81), (286, 71))
f.text(RX, 130, "mito-"); f.text(RX, 144, "chondrion"); f.leader((RX - 4, 127), (288, 124))
figs.append(f.svg((400, 246),
    "Loading of sucrose into a sieve tube. A companion cell lies above a sieve tube element, with a cell wall space above it. In the companion cell surface membrane a proton pump, supplied with ATP by a mitochondrion, moves H+ out into the cell wall space. "
    "H+ then flows back into the companion cell through a cotransporter protein, carrying sucrose with it. The sucrose then passes through plasmodesmata from the companion cell into the sieve tube element.",
    "Sucrose loading. The proton pump uses ATP to build up a high concentration of H⁺ outside the companion cell. H⁺ diffusing back in through the cotransporter brings sucrose in with it, and the sucrose passes into the sieve tube element through plasmodesmata."))
problems += f.check()

# ---------- 2. mass flow from source to sink ----------
f = Fig("massflow")
f.rect(90, 20, 120, 50, PH)                                               # source cell
f.rect(130, 70, 40, 160, "fm s-acc sw2")                                  # sieve tube
f.rect(90, 230, 120, 50, PH)                                              # sink cell
f.rect(320, 20, 24, 260, XY)                                              # xylem
f.line([(150, 52), (150, 100)], "c2 sw2", arrow="ah")                     # sucrose in
f.line([(318, 114), (176, 114)], "c1 sw2", arrow="ah")                    # water in
f.line([(150, 124), (150, 186)], "c3 sw3", arrow="ah")                    # mass flow
f.line([(176, 196), (318, 196)], "c1 sw2", arrow="ah")                    # water out
f.line([(150, 202), (150, 246)], "c2 sw2", arrow="ah")                    # sucrose out
f.text(150, 40, "source (leaf)", anchor="middle")
f.text(150, 270, "sink (root)", anchor="middle")
f.text(186, 90, "water enters"); f.text(186, 104, "by osmosis")
f.text(186, 172, "water leaves"); f.text(186, 186, "by osmosis")
f.text(122, 96, "high", anchor="end"); f.text(122, 110, "hydrostatic", anchor="end"); f.text(122, 124, "pressure", anchor="end")
f.text(122, 150, "mass flow", anchor="end")
f.text(122, 184, "low", anchor="end"); f.text(122, 198, "hydrostatic", anchor="end"); f.text(122, 212, "pressure", anchor="end")
f.text(332, 298, "xylem", anchor="middle")
figs.append(f.svg((380, 306),
    "Mass flow in a sieve tube from a source to a sink. At the source at the top sucrose is loaded into the sieve tube and water enters it from the xylem by osmosis, giving a high hydrostatic pressure. "
    "At the sink at the bottom sucrose is removed and water leaves the sieve tube by osmosis, giving a low hydrostatic pressure. The sap flows down the sieve tube from high to low pressure.",
    "Mass flow. Loading at the source lowers the water potential in the sieve tube, so water enters and the pressure rises; unloading at the sink raises the water potential, so water leaves and the pressure falls. The sap flows down the pressure gradient."))
problems += f.check()

# ---------- 3. ringing experiment ----------
f = Fig("ringing")
poly = [(130, 20), (130, 70), (122, 100), (122, 112), (154, 114), (154, 138), (130, 140), (130, 240),
        (210, 240), (210, 140), (186, 138), (186, 114), (218, 112), (218, 100), (210, 70), (210, 20)]
f.poly(poly, PH, check=False)                                             # stem: bark with phloem
f.rect(154, 20, 32, 220, XY)                                              # xylem core
f.line([(140, 32), (140, 96)], "c2 sw2", arrow="ah")                      # sucrose moving down
RX = 236
f.text(RX, 34, "bark with phloem"); f.leader((RX - 4, 31), (212, 34))
f.text(RX, 66, "xylem"); f.leader((RX - 4, 63), (188, 66))
f.text(RX, 98, "swelling: sucrose"); f.text(RX, 112, "builds up above"); f.text(RX, 126, "the ring"); f.leader((RX - 4, 95), (220, 98))
f.text(RX, 160, "ring: bark and"); f.text(RX, 174, "phloem removed"); f.leader((RX - 4, 157), (188, 130))
f.text(RX, 216, "roots (sink)"); f.leader((RX - 4, 213), (212, 213))
f.text(122, 14, "leaves (source) above", anchor="start") if False else None
figs.append(f.svg((380, 252),
    "A stem with a ring of bark and phloem removed. Above the ring the stem is swollen and an arrow shows sucrose moving down the phloem and stopping at the ring. At the ring only the xylem remains. Below the ring the stem is normal.",
    "A ringing experiment. Removing a ring of bark, which includes the phloem, stops sucrose passing down the stem. The xylem is left, so water can still move up."))
problems += f.check()

print("\n\n".join(figs))
print("\n".join(problems) or "clearance ok", file=sys.stderr)
