# checks/chem.moles.py: recomputes every number in the Moles and stoichiometry chapter.
# Ar values come from data/elements.json (the 9701 Periodic Table, 1 d.p.).
import json
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

A = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
L = 6.022e23
def Mr(**d):
    return sum(A[k] * v for k, v in d.items())

# ---- Ar from isotopes
eq("Cl Ar", (75 * 35 + 25 * 37) / 100, 35.5)
eq("Mg sum", 24 * 79.0 + 25 * 10.0 + 26 * 11.0, 2432)
eq("Mg parts", 24 * 79.0 + 25 * 10.0 + 26 * 11.0, 1896 + 250 + 286)
eq("Mg Ar", sf(2432 / 100), 24.3)
eq("B abundance", 1100 - 1080, 20)
eq("B Ar from 20/80", (10 * 20 + 11 * 80) / 100, A['B'])
eq("Cu abundance", (6500 - 6350) / 2, 75)
eq("Cu Ar", (63 * 75 + 65 * 25) / 100, A['Cu'])
eq("Ga Ar", (69 * 60 + 71 * 40) / 100, 69.8)
eq("Ga quiz wrong 70.0", (69 + 71) / 2, 70.0)
eq("Ga quiz wrong 70.2", (69 * 40 + 71 * 60) / 100, 70.2)
eq("H2O", Mr(H=2, O=1), 18.0)
eq("Ca(OH)2", Mr(Ca=1, O=2, H=2), 74.1)
eq("Cl2 molar mass", 2 * A['Cl'], 71.0)

# ---- the mole
eq("water mol", 36.0 / 18.0, 2.00)
eq("water molecules", sf(2.00 * L), 1.20e24, 1e20)
eq("water atoms", sf(3 * 2.00 * L), 3.61e24, 1e21)
eq("1.2044e24", 2.00 * L, 1.2044e24, 1e19)
eq("Cl2 atoms per mol", sf(2 * L), 1.20e24, 1e21)
MrAS = 2 * A['Al'] + 3 * (A['S'] + 4 * A['O'])
eq("Al2(SO4)3", MrAS, 342.3, 1e-9)
nAS = 5.00 / MrAS
eq("Al2(SO4)3 mol", round(nAS, 6), 0.014607, 1e-9)
eq("sulfate mol", round(3 * nAS, 6), 0.043821, 1e-9)
eq("sulfate ions", sf(3 * nAS * L), 2.64e22, 1e18)

# ---- percentage by mass, empirical formulas
MrNH4 = 2 * (A['N'] + 4 * A['H']) + A['S'] + 4 * A['O']
eq("(NH4)2SO4", MrNH4, 132.1, 1e-9)
eq("N mass", 2 * A['N'], 28.0)
eq("%N", round(28.0 / MrNH4 * 100, 1), 21.2)
nC, nH, nO = 40.0 / A['C'], 6.7 / A['H'], 53.3 / A['O']
eq("glucose C", round(nC, 3), 3.333); eq("glucose H", round(nH, 3), 6.7); eq("glucose O", round(nO, 3), 3.331)
eq("glucose ratio C", round(nC / nO, 2), 1.00); eq("glucose ratio H", round(nH / nO, 2), 2.01); eq("glucose ratio O", 1.00, 1.00)
eq("CH2O mass", Mr(C=1, H=2, O=1), 30.0)
eq("glucose factor", 180 / 30.0, 6)
nFe, nOx = 69.9 / A['Fe'], 30.1 / A['O']
eq("Fe", round(nFe, 4), 1.2527); eq("O", round(nOx, 4), 1.8813); eq("O ratio", round(nOx / nFe, 3), 1.502)
eq("Mg burn n(Mg)", 2.43 / A['Mg'], 0.100); eq("O mass gained", round(4.03 - 2.43, 2), 1.60); eq("n(O)", 1.60 / A['O'], 0.100)
# combustion
eq("CO2 Mr", Mr(C=1, O=2), 44.0); eq("H2O Mr", Mr(H=2, O=1), 18.0)
nc = 1.10 / 44.0; nh = 2 * 0.450 / 18.0
eq("n CO2", nc, 0.02500); eq("n H2O", 0.450 / 18.0, 0.02500); eq("n H", nh, 0.05000)
eq("mass check", nc * A['C'] + nh * A['H'], 0.350, 1e-9)
eq("CH2 mass", Mr(C=1, H=2), 14.0); eq("C5H10 factor", 70.0 / 14.0, 5)
# hydrates
eq("CuSO4.5H2O", A['Cu'] + A['S'] + 4 * A['O'] + 5 * 18.0, 249.6)
MrMg = A['Mg'] + A['S'] + 4 * A['O']
eq("MgSO4", MrMg, 120.4)
eq("n MgSO4", round(1.20 / MrMg, 6), 0.009967, 1e-9)
eq("water lost", round(2.46 - 1.20, 2), 1.26)
eq("n H2O hydrate", 1.26 / 18.0, 0.0700)
eq("x MgSO4", round((1.26 / 18.0) / (1.20 / MrMg), 2), 7.02)
eq("MgSO4.7H2O", MrMg + 7 * 18.0, 246.4)
eq("%water CuSO4.5H2O", round(90.0 / 249.6 * 100, 1), 36.1)

# ---- reacting masses
MrCaCO3 = A['Ca'] + A['C'] + 3 * A['O']; MrCaO = A['Ca'] + A['O']
eq("CaCO3", MrCaCO3, 100.1); eq("CaO", MrCaO, 56.1)
eq("n CaCO3 25 g", round(25.0 / MrCaCO3, 4), 0.2498)
eq("m CaO", sf(25.0 / MrCaCO3 * MrCaO), 14.0)
MrOct = 8 * A['C'] + 18 * A['H']
eq("octane", MrOct, 114.0)
eq("n octane", round(1000 / MrOct, 3), 8.772)
eq("n CO2 octane", round(8 * 1000 / MrOct, 2), 70.18)
eq("m CO2 octane g", round(8 * 1000 / MrOct * 44.0), 3088)
eq("m CO2 kg", sf(8 * 1000 / MrOct * 44.0 / 1000), 3.09)
MrSal = 7 * A['C'] + 6 * A['H'] + 3 * A['O']; MrAsp = 9 * A['C'] + 8 * A['H'] + 4 * A['O']
eq("salicylic", MrSal, 138.0); eq("aspirin", MrAsp, 180.0)
eq("n salicylic", round(2.00 / MrSal, 5), 0.01449)
eq("theoretical aspirin", round(2.00 / MrSal * MrAsp, 3), 2.609)
eq("yield aspirin", round(2.30 / (2.00 / MrSal * MrAsp) * 100, 1), 88.2)

# ---- gas volumes
eq("Mg H2 n", 2.43 / A['Mg'], 0.100)
eq("Mg H2 V", sf(2.43 / A['Mg'] * 24.0), 2.40); eq("Mg H2 cm3", sf(2.43 / A['Mg'] * 24000), 2400, 1e-9)
nc2 = 2.00 / MrCaCO3
eq("CaCO3 mol", round(nc2, 5), 0.01998)
eq("CO2 dm3", round(nc2 * 24.0, 4), 0.4795)
eq("CO2 cm3", sf(nc2 * 24000), 480, 1e-9)
# hydrocarbon (worked example): 10 cm3 + 60 O2 -> 40 after cooling, 10 after NaOH
co2 = 40 - 10; o2_used = 60 - 10
eq("eg CO2", co2, 30); eq("eg C atoms", co2 / 10, 3); eq("eg O2 used", o2_used, 50)
eq("eg O atoms", 2 * o2_used, 100); eq("eg O in CO2", 2 * co2, 60); eq("eg water vol", 2 * o2_used - 2 * co2, 40)
eq("eg H atoms per molecule", 2 * 40 / 10, 8)
# C3H8 + 5 O2 -> 3 CO2 + 4 H2O for 10 cm3
eq("C3H8 O2", 10 * 5, 50); eq("C3H8 CO2", 10 * 3, 30)
# exam Q hydrocarbon: 10 cm3 + 80 O2 -> 60 -> 20
co2q = 60 - 20; o2uq = 80 - 20
eq("q CO2", co2q, 40); eq("q C", co2q / 10, 4); eq("q O2 used", o2uq, 60); eq("q O atoms", 2 * o2uq, 120)
eq("q O in CO2", 2 * co2q, 80); eq("q water", 2 * o2uq - 2 * co2q, 40); eq("q H", 2 * 40 / 10, 8)
eq("C4H8 final volume", 40 + 20, 60)
eq("C3H8 final volume", 30 + 10, 40)

# ---- solutions
eq("NaOH M", A['Na'] + A['O'] + A['H'], 40.0)
eq("NaOH n", 4.00 / 40.0, 0.100); eq("NaOH c", 0.100 / 0.250, 0.400); eq("NaOH g/dm3", 0.400 * 40.0, 16.0); eq("g/dm3 direct", 4.00 / 0.250, 16.0)
eq("titr n HCl", 0.100 * 21.40 / 1000, 0.002140, 1e-12); eq("titr c NaOH", sf(0.002140 / 0.0250), 0.0856, 1e-12)
eq("H2SO4 n", 0.200 * 0.0250, 0.00500); eq("NaOH needed", 2 * 0.00500, 0.0100); eq("V NaOH cm3", 0.0100 / 0.500 * 1000, 20.0)
# back titration
nHCl = 0.200 * 0.0250; nex = 0.100 * 0.01240; nreact = nHCl - nex; nCa = nreact / 2
eq("tablet HCl", nHCl, 0.00500); eq("tablet NaOH", nex, 0.001240, 1e-12); eq("tablet reacted", nreact, 0.003760, 1e-12)
eq("tablet CaCO3 mol", nCa, 0.001880, 1e-12); eq("tablet mass", round(nCa * MrCaCO3, 4), 0.1882)
eq("tablet %", round(nCa * MrCaCO3 / 0.500 * 100, 1), 37.6)

# ---- limiting reagent
eq("Mg 6.00 mol", round(6.00 / A['Mg'], 4), 0.2469)
eq("HCl mol", 2.00 * 0.0600, 0.120)
eq("Mg/1", round(6.00 / A['Mg'] / 1, 4), 0.2469); eq("HCl/2", 0.120 / 2, 0.0600)
eq("H2 mol", 0.120 / 2, 0.0600); eq("H2 V", 0.0600 * 24.0, 1.44)
eq("Mg reacted g", round(0.0600 * A['Mg'], 3), 1.458); eq("Mg left", sf(6.00 - 0.0600 * A['Mg']), 4.54)

# ---- stoichiometry from data
eq("acid n", 0.100 * 0.0250, 0.00250); eq("OH n", 0.100 * 0.0500, 0.00500); eq("acid ratio", 0.00500 / 0.00250, 2)
eq("gas ratio", 20 / 10, 2)

# ---- spot the error
eq("spot n Na2CO3", 0.100 * 0.0250, 0.00250); eq("spot wrong c", 0.00250 / 0.0200, 0.125)
eq("spot right n HCl", 2 * 0.00250, 0.00500); eq("spot right c", 0.00500 / 0.0200, 0.250)

# ---- try questions
eq("try Mr CaCO3", MrCaCO3, 100.1); eq("try Mr (NH4)2SO4", MrNH4, 132.1); eq("try MgSO4.7H2O", MrMg + 7 * 18.0, 246.4)
eq("try NaOH 8 g", 8.00 / 40.0, 0.200); eq("try Cu 0.250 g", sf(0.250 / A['Cu']), 0.00394, 1e-9)
eq("try CH2 C", round(85.7 / A['C'], 3), 7.142); eq("try CH2 H", 14.3 / A['H'], 14.3); eq("try C6H12", 84.0 / 14.0, 6)
eq("try Zn n", 0.654 / A['Zn'], 0.0100); eq("try Zn cm3", 0.0100 * 24.0 * 1000, 240)
eq("try NaCl M", A['Na'] + A['Cl'], 58.5); eq("try NaCl n", 5.85 / 58.5, 0.100); eq("try NaCl c", 0.100 / 0.500, 0.200)
eq("try C burn n", 6.00 / A['C'], 0.500); eq("try O2 mass", 0.500 * 32.0, 16.0)
eq("try Al", 0.200 / 2, 0.100); eq("try Cl2", 0.240 / 3, 0.0800)

# ---- exam practice
eq("Q3 C", 52.2 / A['C'], 4.35); eq("Q3 H", 13.0 / A['H'], 13.0); eq("Q3 O", 34.8 / A['O'], 2.175)
eq("Q3 ratio C", sf(4.35 / 2.175), 2.0); eq("Q3 ratio H", sf(13.0 / 2.175, 3), 5.98)
MrNa2CO3 = 2 * A['Na'] + A['C'] + 3 * A['O']
eq("Q4 Mr", MrNa2CO3, 106.0); eq("Q4 n", 1.06 / 106.0, 0.0100); eq("Q4 water", round(2.86 - 1.06, 2), 1.80)
eq("Q4 n water", 1.80 / 18.0, 0.100); eq("Q4 x", 0.100 / 0.0100, 10)
eq("Q5 n NaOH", 0.100 * 0.03120, 0.003120, 1e-12); eq("Q5 n H2SO4", 0.003120 / 2, 0.001560, 1e-12)
eq("Q5 c", sf(0.001560 / 0.0250), 0.0624, 1e-12)
MrH2SO4 = 2 * A['H'] + A['S'] + 4 * A['O']
eq("Q5 M", MrH2SO4, 98.1); eq("Q5 g/dm3", sf(0.0624 * 98.1), 6.12)
MrEtOH = 2 * A['C'] + 6 * A['H'] + A['O']; MrEster = 4 * A['C'] + 8 * A['H'] + 2 * A['O']
eq("Q6 Mr ethanol", MrEtOH, 46.0); eq("Q6 Mr ester", MrEster, 88.0)
eq("Q6 n", round(4.00 / 46.0, 5), 0.08696); eq("Q6 theo", round(4.00 / 46.0 * 88.0, 3), 7.652)
eq("Q6 yield", round(5.10 / (4.00 / 46.0 * 88.0) * 100, 1), 66.6)
eq("Q8 n Mg", round(0.486 / A['Mg'], 4), 0.0200); eq("Q8 n HCl", 0.500 * 0.0400, 0.0200)
eq("Q8 Mg needs HCl", 2 * 0.0200, 0.0400); eq("Q8 n H2", 0.0200 / 2, 0.0100)
eq("Q8 V", 0.0100 * 24.0 * 1000, 240); eq("Q8 Mg left", sf(0.0100 * A['Mg']), 0.243)

# ---- stretch
eq("S1 n N2", 60.0 / 24.0, 2.50); eq("S1 n NaN3", round(2.50 * 2 / 3, 3), 1.667)
MrNaN3 = A['Na'] + 3 * A['N']
eq("S1 Mr", MrNaN3, 65.0); eq("S1 mass", sf(2.50 * 2 / 3 * 65.0), 108)
MrAgCl = A['Ag'] + A['Cl']
eq("S2 Mr AgCl", round(MrAgCl, 1), 143.4); eq("S2 n AgCl", round(2.87 / MrAgCl, 5), 0.02001)
eq("S2 x", round(2.87 / MrAgCl / 0.0100), 2)
eq("S2 Mr MCl2", 1.11 / 0.0100, 111); eq("S2 Ar M", 111 - 2 * A['Cl'], 40.0)

# ---- stretch: C, H, O by difference (REVIEW fix)
mC = 2.200 * A['C'] / (A['C'] + 2 * A['O']); mH = 0.900 * 2 * A['H'] / (2 * A['H'] + A['O'])
eq("S3 mass C", round(mC, 3), 0.600); eq("S3 mass H", round(mH, 3), 0.100)
mO = round(1.50 - mC - mH, 3)
eq("S3 mass O", mO, 0.800)
eq("S3 n C", round(mC / A['C'], 4), 0.0500); eq("S3 n H", round(mH / A['H'], 4), 0.100); eq("S3 n O", round(mO / A['O'], 4), 0.0500)
eq("S3 emp mass", A['C'] + 2 * A['H'] + A['O'], 30.0); eq("S3 multiple", 180 / 30.0, 6)

# ---- quiz
eq("quiz NaOH 2.00 g n", 2.00 / 40.0, 0.0500); eq("quiz c", 0.0500 / 0.500, 0.100); eq("quiz wrong 1e-4", 0.0500 / 500, 1.00e-4, 1e-12)
eq("quiz CO2", 0.0500 * 24.0, 1.20); eq("quiz CO2 stp wrong", 0.0500 * 22.4, 1.12)
eq("quiz 8 g wrong mult", 8.00 * 40.0, 320)
print("ok")
