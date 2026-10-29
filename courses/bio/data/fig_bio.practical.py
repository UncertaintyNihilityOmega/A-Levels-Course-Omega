# data/fig_bio.practical.py: hand-drawn SVG for chapters/bio.practical.md (the water bath).
# Run: py data/fig_bio.practical.py  -> prints the clearance report. data/place_figs_p19.py pastes the figures in.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib_p19 import Fig, lead_check

sys.stdout.reconfigure(encoding="utf-8")


def figures():
    figs, problems = {}, []
    f = Fig("waterbath")
    LEAD = "ln-m thin"
    # water and beaker
    f.rect(105, 90, 140, 115, "fm s-acc sw2")
    f.line([(105, 44), (105, 90)], "ln")
    f.line([(245, 44), (245, 90)], "ln")
    # tube of milk suspension (left)
    tube = lambda x: [(x, 34), (x, 150), (x + 4, 158), (x + 18, 158), (x + 22, 150), (x + 22, 34)]
    f.line(tube(120), "fp ln", check=False)
    f.poly([(120, 110), (120, 150), (124, 158), (138, 158), (142, 150), (142, 110)], "f2 s-acc2 sw2", check=False)
    # tube of protease solution (right)
    f.line(tube(180), "fp ln", check=False)
    f.poly([(180, 122), (180, 150), (184, 158), (198, 158), (202, 150), (202, 122)], "f1 s-acc sw2", check=False)
    # thermometer
    f.rect(157, 28, 8, 140, "fp ln")
    f.line([(161, 70), (161, 166)], "c1 sw2", check=False)
    f.circle(161, 172, 6, "f1 s-acc sw2")
    # labels and leaders
    f.text(161, 16, "thermometer", "tl", "middle")
    f.line([(161, 20), (161, 27)], LEAD, check=False)
    f.text(96, 122, "tube of milk", "tl", "end")
    f.text(96, 136, "suspension", "tl", "end")
    f.line([(101, 129), (127, 133)], LEAD, check=False)
    problems += lead_check(f, (101, 129), (127, 133))
    f.text(257, 122, "tube of", "tl")
    f.text(257, 136, "protease", "tl")
    f.line([(251, 129), (197, 134)], LEAD, check=False)
    problems += lead_check(f, (251, 129), (197, 134))
    f.text(257, 186, "water bath", "tl")
    f.text(257, 200, "at 40 °C", "tl")
    f.line([(251, 183), (236, 181)], LEAD, check=False)
    problems += lead_check(f, (251, 183), (236, 181))
    label = ("A water bath: a beaker of water at 40 degrees Celsius holds a tube of milk suspension and a tube of protease "
             "solution, with a thermometer standing in the water between them.")
    cap = ("A water bath for a temperature investigation. The tube of milk suspension and the tube of protease solution "
           "stand in the water until the thermometer reads the chosen temperature, and only then are they mixed.")
    figs["waterbath"] = f.svg((340, 214), label, cap)
    problems += f.check()
    return figs, problems


if __name__ == "__main__":
    figs, problems = figures()
    print("\n".join(problems) or "clearance ok")
