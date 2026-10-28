# checks/bio.heart.py: recomputes every number in chapters/bio.heart.md
import os, sys
from math import isclose

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data"))
from fig_cardiac import LA, LV, AO, events, KEY

n = 0


def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"


def sf(x, k=3):
    return float(f"{x:.{k}g}")


# --- the model behind the static pressure graph and the widget ---------------------------------------------
ev = events()
assert [s for _, s in ev] == ["AV valve closes", "semilunar valve opens", "semilunar valve closes", "AV valve opens"], ev
t1, t2, t3, t4 = (round(t, 2) for t, _ in ev)
eq("event 1: AV valve closes about 0.10 s", t1, 0.10, 0.006)
eq("event 2: semilunar valve opens about 0.17 s", t2, 0.17, 0.006)
eq("event 3: semilunar valve closes about 0.38 s", t3, 0.38, 0.006)
eq("event 4: AV valve opens about 0.45 s", t4, 0.45, 0.006)
peak_lv = max(LV(k / 1000) for k in range(801))
peak_ao = max(AO(k / 1000) for k in range(801))
min_ao = min(AO(k / 1000) for k in range(801))
peak_la = max(LA(k / 1000) for k in range(801))
eq("LV peak about 16 kPa", peak_lv, 16, 0.3)
eq("aortic peak about 16 kPa", peak_ao, 16, 0.3)
eq("aortic minimum 10.5 kPa", min_ao, 10.5, 0.01)
eq("left atrium peak about 1.5 kPa", peak_la, 1.5, 0.1)
assert max(LV(k / 1000) for k in range(460, 801)) < 1.0, "diastolic ventricle pressure below 1 kPa"
assert 14 < AO(0.45) < 15 and AO(0.8) < 11
eq("AV valve, 0.8 s cycle: 60/0.8", 60 / 0.8, 75)
eq("semilunar open time (rounded events)", round(t3 - t2, 2), 0.21, 1e-9)
eq("phases 0.1 + 0.3 + 0.4 = 0.8", 0.1 + 0.3 + 0.4, 0.8)

# --- practice (Start easy) --------------------------------------------------------------------------------
eq("try 60/0.60", 60 / 0.60, 100)
eq("try cycle time 15/18", sf(15 / 18, 2), 0.83)
eq("try heart rate 18 in 15 s", 18 * 60 / 15, 72)
eq("try wall ratio", sf(11 / 3.5, 2), 3.1)
eq("warm-up magnification", 40 / 0.2, 200)

# --- exam practice: the child's pressure table -------------------------------------------------------------------
tab = {  # time: (LA, LV, AO)
    0.00: (0.9, 0.5, 10.0), 0.05: (1.3, 0.8, 9.9), 0.10: (0.9, 3.0, 9.9), 0.15: (0.9, 9.0, 9.8), 0.20: (1.0, 13.0, 11.5),
    0.25: (1.0, 14.0, 13.8), 0.30: (1.1, 12.0, 13.2), 0.35: (1.1, 2.0, 12.5), 0.40: (0.9, 0.7, 11.8), 0.45: (0.7, 0.4, 11.0),
    0.50: (0.6, 0.4, 10.4), 0.55: (0.7, 0.5, 10.1)}
ts = sorted(tab)
av_open = [tab[t][0] > tab[t][1] for t in ts]
sl_open = [tab[t][1] > tab[t][2] for t in ts]
# AV valve: open at 0.00 and 0.05, shut from 0.10 to 0.35, open again from 0.40
assert av_open == [True, True, False, False, False, False, False, False, True, True, True, True], av_open
assert sl_open == [False, False, False, False, True, True, False, False, False, False, False, False], sl_open
eq("AV closes between 0.05 and 0.10", ts[av_open.index(False)], 0.10)
eq("semilunar opens between 0.15 and 0.20", ts[sl_open.index(True)], 0.20)
assert tab[0.15][1] == 9.0 and tab[0.15][2] == 9.8 and tab[0.20][1] == 13.0 and tab[0.20][2] == 11.5
eq("child heart rate", 60 / 0.60, 100)
assert min(v[2] for v in tab.values()) == 9.8

# --- exam practice: pulse of 70 ---------------------------------------------------------------------------------
cyc = 60 / 70
eq("cycle time at 70", sf(cyc, 2), 0.86)
eq("diastole at 70", sf(cyc - 0.10 - 0.30, 2), 0.46)

# --- stretch: exercise ------------------------------------------------------------------------------------------
eq("cycle at 150", 60 / 150, 0.40, 1e-12)
eq("cycle at rest 60 bpm", 60 / 60, 1.0)
d_rest, d_ex = 1.0 - 0.4, 0.40 - 0.30
eq("diastole at rest", d_rest, 0.6, 1e-12)
eq("diastole at 150", d_ex, 0.10, 1e-12)
eq("diastole falls by", round((d_rest - d_ex) / d_rest * 100), 83)
eq("systole falls by", round((0.4 - 0.3) / 0.4 * 100), 25)

print("ok")
