# checks/chem.lattice.py: recomputes every number in "Lattice energy, entropy and Gibbs free energy".
# All enthalpy, electron affinity, hydration, ionic radius and S values are "data for this question"
# (standard data-book values); IE values and bond energies agree with FACTS.md (Mg 736 1450, Na 494, K 418, Ca 590 1150,
# Ba 502 966; F-F 158, Cl-Cl 242).
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

# --- definitions
eq("half Cl-Cl", 242 / 2, 121)
eq("half F-F", 158 / 2, 79)

# --- NaCl Born-Haber (worked example, widget default, table)
nacl = -411 - (107 + 122 + 494 - 349)
eq("NaCl latt", nacl, -785)
eq("NaCl sum steps", 107 + 122 + 494 - 349, 374)

# --- MgO
mgo_sum = 148 + 249 + 736 + 1450 - 141 + 798
eq("MgO sum", mgo_sum, 3240)
eq("MgO latt", -602 - mgo_sum, -3842)

# --- MgCl2 formation
eq("MgCl2 Hf", 148 + 736 + 1450 + 2 * 122 + 2 * -349 + -2521, -641)
eq("MgCl2 latt from Hf", -641 - (148 + 736 + 1450 + 2 * 122 + 2 * -349), -2521)

# --- EA of Cl from KCl
eq("EA Cl from KCl", -437 - 89 - 122 - 418 + 717, -349)
eq("KCl latt", -437 - (89 + 418 + 122 - 349), -717)

# --- NaF
eq("NaF latt", -574 - (107 + 494 + 79 - 328), -926)
eq("NaF sum", 107 + 494 + 79 - 328, 352)

# --- ratios in text
eq("MgO/NaCl", round(3842 / 785, 1), 4.9)
eq("Mg/Na hyd ratio", round(1920 / 406, 1), 4.7)

# --- dissolving NaCl
eq("NaCl sol", 785 - 406 - 364, 15)
eq("NaCl hyd sum", 406 + 364, 770)
# MgCl2
eq("MgCl2 sol", 2521 - 1920 - 2 * 364, -127)
eq("MgCl2 sol wrong (one Cl)", 2521 - 1920 - 364, 237)
eq("MgCl2 sol wrong (sign)", -2521 - 1920 - 2 * 364, -5169)
eq("MgCl2 sol sign flipped", 127, 127)
# KBr
eq("KBr sol", 679 - 322 - 335, 22)

# --- CaO formation
eq("CaO Hf", 178 + 590 + 1150 + 249 - 141 + 798 - 3459, -635)
eq("CaO sum", 178 + 590 + 1150 + 249 - 141 + 798, 2824)
eq("CaO latt", -635 - 2824, -3459)

# --- BaO
eq("BaO sum", 180 + 502 + 966 + 249 - 141 + 798, 2554)
eq("BaO Hf", 2554 - 3102, -548)

# --- KF
eq("KF sum", 89 + 79 + 418 - 328, 258)
eq("KF latt", -568 - 258, -826)

# --- Na2O
na2o = 2 * 107 + 2 * 494 + 249 - 141 + 798
eq("Na2O sum", na2o, 2108)
eq("Na2O latt", -414 - na2o, -2522)

# --- MgCl stretch
mgcl = 148 + 736 + 122 - 349 - 753
eq("MgCl Hf", mgcl, -96)
eq("disproportionation", -641 - 2 * mgcl, -449)

# --- entropy
dS_haber = 2 * 192.8 - (191.6 + 3 * 130.7)
eq("dS haber", round(dS_haber, 1), -198.1)
eq("2NH3", 2 * 192.8, 385.6)
eq("N2+3H2", 191.6 + 3 * 130.7, 583.7)
dS_caco3 = (39.7 + 213.8) - 92.9
eq("dS CaCO3", round(dS_caco3, 1), 160.6)
dS_ch4 = (213.8 + 2 * 69.9) - (186.3 + 2 * 205.0)
eq("dS CH4 comb", round(dS_ch4, 1), -242.7)
eq("CH4 prods", 213.8 + 2 * 69.9, 353.6)
eq("CH4 reacts", 186.3 + 2 * 205.0, 596.3)
dS_mg = (26.9 + 213.8) - 65.7
eq("dS MgCO3", round(dS_mg, 1), 175.0)

# --- Gibbs
dG_haber = -92.2 - 298 * (dS_haber / 1000)
eq("dG haber", round(dG_haber, 1), -33.2)
eq("298 x 0.1981", round(298 * 0.1981, 2), 59.03)
T_caco3 = 178000 / dS_caco3
eq("T CaCO3", round(T_caco3), 1108)
eq("dG CaCO3 298", round(178 - 298 * dS_caco3 / 1000), 130)
eq("dG CaCO3 298 (plot)", round(178 - 298 * 0.1606, 1), 130.1)
eq("plot zero", round(178 / 0.1606), 1108)
eq("cold pack", round(26 - 298 * 108 / 1000, 1), -6.2)
eq("cold pack TdS", round(298 * 0.108, 2), 32.18)
eq("spot error dG", round(178 - 1500 * 0.161, 1), -63.5)
eq("spot error wrong", 178 - 1500 * 161, -241322)
T_mg = 117000 / dS_mg
eq("T MgCO3", round(T_mg), 669)
eq("try T", -120000 / -250, 480)
eq("NH4Cl T", round(176000 / 285), 618)

print("ok")
