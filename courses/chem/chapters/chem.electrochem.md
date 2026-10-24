@chapter chem.electrochem
@title Electrochemistry: electrolysis and electrode potentials
@level a2
@paper CAIE 9701 Paper 4
@time 8–10 hours
@summary How electricity and chemistry work together. You will predict the products of electrolysis, calculate masses and gas volumes from a current and a time, measure standard electrode potentials against the standard hydrogen electrode, and use them to find cell voltages, predict whether reactions happen, allow for concentration with the Nernst equation and link voltage to Gibbs free energy.

:::why
A battery, a copper-plated pipe, the aluminium in an aeroplane and the chlorine in drinking water all depend on electrons moving between chemicals. Electrochemistry tells you how much product a current can make, and it gives you a table of electrode potentials that predicts which redox reactions will happen, without doing the experiment. That table is the one tool you will use again in transition-metal chemistry and in every redox titration.
:::

**Before you start**, you should know oxidation, reduction and half-equations from [Redox and oxidation numbers](#chem.redox), moles and gas volumes from [Moles and stoichiometry](#chem.moles), and feasibility from the Gibbs section of [Lattice energy, entropy and Gibbs free energy](#chem.lattice).

:::try Warm-up
Q: Write the half-equation for zinc metal becoming zinc ions, and say whether it is oxidation or reduction. (from [Redox and oxidation numbers](#chem.redox))
A: \(\ce{Zn -> Zn^2+ + 2e-}\). Electrons are lost, so it is oxidation.
Q: How many moles of copper are in 3.175 g of copper? (\(A_r\) of Cu = 63.5.) (from [Moles and stoichiometry](#chem.moles))
A: \(3.175 / 63.5 = 0.0500\) mol.
Q: What does it mean if ΔG for a reaction is negative? (from [Lattice energy, entropy and Gibbs free energy](#chem.lattice))
A: The reaction is feasible (it can happen), although it may be too slow to see.
:::

## Electrolysis

In a spontaneous redox reaction, such as zinc displacing copper, electrons pass from one substance to another by themselves. **Electrolysis** forces the opposite: an external power supply pushes electrons round a circuit and makes a non-spontaneous redox reaction happen.

:::def Electrolysis
The decomposition of an ionic compound, molten or in solution, by passing an electric current through it. Electrical energy drives a redox reaction that would not otherwise happen.
:::

The solid or liquid that carries the current in and out is an **electrode**. The positive electrode (connected to the positive terminal of the supply) is the **anode**, the negative electrode is the **cathode**. The ions of the electrolyte are free to move, so positive ions (cations) move to the cathode and negative ions (anions) to the anode.

:::key Naming the electrodes
**Anode**: oxidation happens here (ions lose electrons); in electrolysis it is positive. **Cathode**: reduction happens here (ions gain electrons); in electrolysis it is negative. Remember "An Ox, Red Cat". The names follow the process, not the sign: in the next half of the chapter the cathode of a working cell will turn out to be the positive electrode.
:::

### Predicting the products

**A molten compound** contains only two kinds of ions, so there is no choice. Molten lead(II) bromide gives lead at the cathode and bromine at the anode:

\[\ce{Pb^2+ + 2e- -> Pb}\qquad\qquad \ce{2Br- -> Br2 + 2e-}\]

**An aqueous solution** contains two kinds of cation (the metal ion and \(\ce{H+}\) from water) and two kinds of anion (the negative ion and \(\ce{OH-}\) from water). Now there is a competition at each electrode, and the standard electrode potentials in the table later in this chapter decide it.

E⦵ (electrode potential, defined later in this chapter) is a number in volts: the more positive it is, the more easily that ion or molecule gains electrons. Use it now as a ranking. "Discharged" means turned into the neutral element at the electrode.

- **At the cathode, the species with the more positive E⦵ is reduced first.** The metal ion is reduced to metal if its E⦵ is more positive than that of water, \(\ce{2H2O + 2e- <=> H2 + 2OH-}\) (E⦵ = −0.83 V). Copper (+0.34 V) and silver (+0.80 V) are deposited. Sodium (−2.71 V), potassium and magnesium (−2.38 V) are not: hydrogen gas forms instead, and the solution becomes alkaline. In an acid solution the \(\ce{H+}\) ions themselves are reduced: \(\ce{2H+ + 2e- -> H2}\).
- **At the anode, the species with the more negative E⦵ is oxidised first** (it loses electrons more easily). The half-equation for oxygen is \(\ce{O2 + 4H+ + 4e- <=> 2H2O}\) (E⦵ = +1.23 V), so bromide (+1.07 V) and iodide (+0.54 V) are oxidised before water and give bromine and iodine. Sulfate and nitrate ions are not discharged: their elements are already in their highest oxidation states. Water is oxidised instead: \(\ce{2H2O -> O2 + 4H+ + 4e-}\).
- **Concentration** matters for chloride. On E⦵ alone water (+1.23 V) should be oxidised before chloride (+1.36 V). In a **concentrated** solution of chloride ions, the high concentration makes chloride much easier to oxidise, and the formation of oxygen is a slow process, so chlorine is the main product. In a **dilute** solution, mainly oxygen forms.
- **The electrode material** also matters. Graphite and platinum are **inert**: they only carry electrons. A copper anode is **active**: copper (+0.34 V) is oxidised more easily than water or any anion, so the anode dissolves, \(\ce{Cu -> Cu^2+ + 2e-}\).

| Electrolyte | Electrodes | Cathode (−) | Anode (+) |
|---|---|---|---|
| molten \(\ce{PbBr2}\) | inert | Pb | \(\ce{Br2}\) |
| molten \(\ce{NaCl}\) | inert | Na | \(\ce{Cl2}\) |
| concentrated \(\ce{NaCl(aq)}\) | inert | \(\ce{H2}\) (and \(\ce{OH-}\) forms) | \(\ce{Cl2}\) |
| dilute \(\ce{NaCl(aq)}\) | inert | \(\ce{H2}\) | mainly \(\ce{O2}\) |
| \(\ce{CuSO4(aq)}\) | inert | Cu | \(\ce{O2}\) |
| \(\ce{CuSO4(aq)}\) | copper | Cu is deposited | Cu dissolves |
| dilute \(\ce{H2SO4}\) | inert | \(\ce{H2}\) | \(\ce{O2}\) |

The last row shows that electrolysing dilute sulfuric acid, or any dilute solution of a reactive metal's salt, is really the electrolysis of water: hydrogen and oxygen come off in a 2 : 1 volume ratio.

:::eg (Exam style) State the products at the cathode and the anode, with half-equations, when each is electrolysed with inert electrodes: (a) molten lead(II) bromide, (b) concentrated aqueous sodium chloride, (c) aqueous copper(II) sulfate.
(a) Cathode: lead, \(\ce{Pb^2+ + 2e- -> Pb}\). [B1] Anode: bromine, \(\ce{2Br- -> Br2 + 2e-}\). [B1]
(b) Cathode: hydrogen. Sodium (E⦵ = −2.71 V) is less easily reduced than water (−0.83 V), so water is reduced, \(\ce{2H2O + 2e- -> H2 + 2OH-}\). [B1] Anode: chlorine, \(\ce{2Cl- -> Cl2 + 2e-}\), because the concentration of chloride ions is high. [B1]
(c) Cathode: copper, \(\ce{Cu^2+ + 2e- -> Cu}\), because E⦵ = +0.34 V is more positive than that of water. [B1] Anode: oxygen, \(\ce{2H2O -> O2 + 4H+ + 4e-}\), because sulfate ions are not oxidised. [B1]
:::

:::html
<figure class="fig small"><svg viewBox="30 8 270 262" role="img" aria-label="Electrolysis of copper(II) sulfate solution with two copper electrodes: copper is deposited on the cathode connected to the negative terminal and dissolves from the anode connected to the positive terminal"><path class="ln" d="M55 110L55 220L275 220L275 110"/><path class="fa" d="M56 130H274V219H56Z"/><path class="fm2" d="M96 74H104V196H96Z"/><path class="fm2" d="M226 74H234V196H226Z"/><path class="ln" d="M100 74L100 44L116 44"/><circle class="f1 s-acc sw2" cx="130" cy="44" r="14"/><text class="tl tc" x="130" y="49">A</text><path class="ln" d="M144 44L172 44"/><path class="ln thick" d="M172 36L172 52"/><path class="ln" d="M184 30L184 58"/><path class="ln" d="M184 44L230 44L230 74"/><text class="tl tc" x="172" y="22">−</text><text class="tl tc" x="184" y="22">+</text><path class="c2 sw2" d="M224 34H198" marker-end="url(#ah)"/><text class="tl tc" x="211" y="26">e⁻</text><path class="ln" d="M205 144H125" marker-end="url(#ah)"/><text class="tl tc" x="165" y="122">Cu²⁺</text><text class="tl tc" x="100" y="240">cathode (−)</text><text class="tl tc" x="100" y="257">Cu²⁺ + 2e⁻ → Cu</text><text class="tl tc" x="230" y="240">anode (+)</text><text class="tl tc" x="230" y="257">Cu → Cu²⁺ + 2e⁻</text></svg><figcaption>Electrolysis of copper(II) sulfate solution with copper electrodes. The electrons are pushed from the anode, round the circuit, to the cathode; copper ions in the solution move to the cathode and copper atoms leave the anode as ions. The cell is joined to a d.c. supply (the long line of its symbol is the positive terminal) with an ammeter in series.</figcaption></figure>
:::

With copper electrodes the mass lost by the anode equals the mass gained by the cathode, and the blue colour of the solution does not change: for every \(\ce{Cu^2+}\) ion removed at the cathode, one is made at the anode. This is how copper is purified and how objects are electroplated, with the object as the cathode.

## Quantitative electrolysis

A current is a flow of charge. The amount of substance made at an electrode is proportional to the charge that has flowed, which is the idea behind Faraday's laws.

:::formula Charge and current
\[Q = I\,t\]
\(Q\) = charge in coulombs (C), \(I\) = current in amperes (A), \(t\) = time in **seconds**.
:::

The charge of one electron is \(e = 1.60 \times 10^{-19}\) C. One mole of electrons contains \(L\) electrons, where \(L\) is the Avogadro constant, so the charge of one mole of electrons is the **Faraday constant**:

:::def Faraday constant, F
The charge carried by one mole of electrons: \(F = Le\). Its value is \(9.65 \times 10^4\ \mathrm{C\,mol^{-1}}\) (in the Data section).
:::

Check the product: \(6.022 \times 10^{23} \times 1.60 \times 10^{-19} = 9.64 \times 10^{4}\ \mathrm{C\,mol^{-1}}\). The Data section gives \(9.65 \times 10^4\), because the electron charge is known to more than 3 significant figures; the two agree to the precision of \(e\). Use the Data section value in calculations.

:::steps
1. Charge: \(Q = It\) with the time converted to seconds.
2. Moles of electrons: \(n(\mathrm{e^-}) = Q / F\).
3. Use the half-equation for the electrode to turn moles of electrons into moles of product (for example \(\ce{Cu^2+ + 2e- -> Cu}\): 2 mol of electrons per mole of copper).
4. Convert to mass (\(\times A_r\)) or to gas volume (\(\times 24.0\ \mathrm{dm^3\,mol^{-1}}\) at room conditions).
:::

:::eg (Exam style) A current of 0.500 A passes through copper(II) sulfate solution for 30.0 minutes with inert electrodes. Calculate the mass of copper deposited at the cathode.
\[Q = It = 0.500 \times (30.0 \times 60) = 900\ \mathrm{C}\] [M1]
\[n(\mathrm{e^-}) = \frac{900}{9.65 \times 10^{4}} = 9.326 \times 10^{-3}\ \mathrm{mol}\] [M1]
\(\ce{Cu^2+ + 2e- -> Cu}\): \(n(\ce{Cu}) = 9.326 \times 10^{-3} / 2 = 4.663 \times 10^{-3}\) mol, so
\[m(\ce{Cu}) = 4.663 \times 10^{-3} \times 63.5 = 0.296\ \mathrm{g}\] [A1]
:::

:::eg (Exam style) Dilute sulfuric acid is electrolysed with inert electrodes using a current of 2.00 A for 20.0 minutes. Calculate the volume of oxygen formed at the anode at room conditions.
\[Q = 2.00 \times (20.0 \times 60) = 2400\ \mathrm{C}\] [M1]
\[n(\mathrm{e^-}) = \frac{2400}{9.65 \times 10^{4}} = 0.02487\ \mathrm{mol}\] [M1]
The anode reaction is \(\ce{2H2O -> O2 + 4H+ + 4e-}\): 4 mol of electrons per mole of \(\ce{O2}\), so \(n(\ce{O2}) = 0.02487 / 4 = 6.218 \times 10^{-3}\) mol. [M1]
\[V(\ce{O2}) = 6.218 \times 10^{-3} \times 24.0 = 0.149\ \mathrm{dm^3} = 149\ \mathrm{cm^3}\] [A1]
:::

:::eg (Real context) A spoon is electroplated with silver by making it the cathode in a solution of silver nitrate. A current of 1.50 A flows for 20.0 minutes. Calculate the mass of silver deposited.
\[Q = 1.50 \times (20.0 \times 60) = 1800\ \mathrm{C}\] [M1]
\[n(\mathrm{e^-}) = \frac{1800}{9.65 \times 10^{4}} = 0.01865\ \mathrm{mol}\] [M1]
\(\ce{Ag+ + e- -> Ag}\): one electron per atom of silver, so \(n(\ce{Ag}) = 0.01865\) mol. [B1]
\[m(\ce{Ag}) = 0.01865 \times 107.9 = 2.01\ \mathrm{g}\] [A1]
The object to be plated is made the cathode so that the metal ions are reduced onto it.
:::

:::eg Aluminium is made by electrolysing aluminium oxide dissolved in molten cryolite, which lowers the temperature needed. A cell carries a current of \(1.00 \times 10^{5}\) A for 1.00 hour. Calculate the mass of aluminium formed.
The cathode reaction is \(\ce{Al^3+ + 3e- -> Al}\): 3 mol of electrons per mole of aluminium. [B1]
\[Q = 1.00 \times 10^{5} \times 3600 = 3.60 \times 10^{8}\ \mathrm{C}\] [M1]
\[n(\mathrm{e^-}) = \frac{3.60 \times 10^{8}}{9.65 \times 10^{4}} = 3731\ \mathrm{mol}, \qquad n(\ce{Al}) = \frac{3731}{3} = 1244\ \mathrm{mol}\] [M1]
\[m(\ce{Al}) = 1244 \times 27.0 = 3.36 \times 10^{4}\ \mathrm{g} = 33.6\ \mathrm{kg}\] [A1]
A table of E⦵ values shows why this has to be done by electrolysis of the molten oxide: \(\ce{Al^3+}\) (−1.66 V) is less easily reduced than water, so electrolysing an aqueous solution would give hydrogen.
:::

### Finding the charge on an ion

Rearranging the same steps lets you find the charge of an ion, or the number of electrons in a half-equation: divide the moles of electrons by the moles of metal formed.

:::eg 0.274 g of nickel (\(A_r\) = 58.7) is deposited by a current of 1.50 A flowing for 10.0 minutes. Find the charge on the nickel ion.
\(Q = 1.50 \times 600 = 900\) C, so \(n(\mathrm{e^-}) = 900 / 9.65 \times 10^{4} = 9.326 \times 10^{-3}\) mol. [M1]
\(n(\ce{Ni}) = 0.274 / 58.7 = 4.668 \times 10^{-3}\) mol. [M1]
Electrons per nickel atom \(= 9.326 \times 10^{-3} / 4.668 \times 10^{-3} = 2.00\), so the ion is \(\ce{Ni^2+}\). [A1]
:::

### Determining the Avogadro constant by electrolysis

You can turn the calculation round: measure the charge and the amount of copper deposited, and calculate \(L\). The charge of one electron \(e = 1.60 \times 10^{-19}\) C is taken as known.

:::lab Measuring L with copper electrodes
Clean two copper plates with fine sandpaper, wash them with water and propanone and dry them. Weigh the one that will be the cathode (balance reading to 0.01 g, or better). Connect both plates to a d.c. supply with an ammeter and a variable resistor in series, with the cathode joined to the negative terminal, and immerse them in copper(II) sulfate solution. Switch on, start a stopwatch and adjust the resistor to hold the current steady (about 0.3 A), noting the current every few minutes. After about 45 minutes, switch off, lift out the cathode, rinse it gently with water and then with propanone, dry it in warm air and weigh it again.
Safety: copper(II) sulfate is harmful to eyes and aquatic life; propanone is flammable, so keep it away from the power supply when the circuit is on.
:::

The calculation: \(Q = It\) (using the mean current), moles of copper \(= \Delta m / A_r\), moles of electrons \(= 2 \times\) moles of copper, number of electrons \(= Q / e\). Then \(L = \dfrac{Q/e}{n(\mathrm{e^-})} = \dfrac{Q}{n(\mathrm{e^-})\,e}\).

:::eg (Exam style) In an experiment with copper electrodes, a current of 0.350 A flowed for 45.0 minutes and the cathode gained 0.312 g. Calculate a value for the Avogadro constant, \(L\), given \(e = 1.60 \times 10^{-19}\) C.
\[Q = 0.350 \times (45.0 \times 60) = 945\ \mathrm{C}\] [M1]
\(n(\ce{Cu}) = 0.312 / 63.5 = 4.913 \times 10^{-3}\) mol, so \(n(\mathrm{e^-}) = 2 \times 4.913 \times 10^{-3} = 9.827 \times 10^{-3}\) mol. [M1]
\[L = \frac{Q}{n(\mathrm{e^-})\,e} = \frac{945}{9.827 \times 10^{-3} \times 1.60 \times 10^{-19}} = 6.01 \times 10^{23}\ \mathrm{mol^{-1}}\] [A1]
This is within 1% of the accepted value, \(6.022 \times 10^{23}\). The main errors are the mass difference (with a balance reading to 0.01 g, a gain of about 0.31 g is uncertain by about 3%) and the current drifting; a longer run gives a larger mass change and a smaller percentage error.
:::

## Electrode potentials

Electrolysis uses electrical energy to drive a reaction. Now reverse the idea: a **cell** uses a spontaneous redox reaction to produce electrical energy. Put a strip of zinc in a solution of copper(II) ions and the zinc dissolves while copper is deposited, and heat is released. Separate the two half-reactions into two beakers, joined by a wire, and the electrons are forced to take the long way round through the wire, doing work.

### Half-cells

A **half-cell** is a metal (or other conductor) dipping into a solution of its ions. A zinc strip in zinc sulfate solution is a half-cell, and the equilibrium at the surface is

\[\ce{Zn^2+(aq) + 2e- <=> Zn(s)}\]

Zinc atoms tend to leave the metal as \(\ce{Zn^2+}\) ions, leaving electrons on the strip, so the zinc builds up a negative charge. Copper is much less keen to lose electrons, so the equilibrium \(\ce{Cu^2+(aq) + 2e- <=> Cu(s)}\) lies further to the right and the strip is less negative. Each half-cell has its own **electrode potential**, which measures how strongly the equilibrium lies towards the reduced or the oxidised form. You cannot measure the potential of one half-cell by itself. A voltmeter always compares two. So all half-cells are compared with one agreed reference.

### The standard hydrogen electrode

:::def Standard hydrogen electrode
A platinum electrode, coated with finely divided platinum (platinum black), in a solution of \(\ce{H+}\) ions of concentration 1.00 mol dm⁻³, with hydrogen gas at a pressure of 101 kPa bubbled over it, at 298 K. The half-equation is \(\ce{2H+(aq) + 2e- <=> H2(g)}\). Its electrode potential is defined as exactly 0.00 V.
:::

Platinum is used because it is inert and because platinum black, with its huge surface area, catalyses the equilibrium between hydrogen gas and hydrogen ions so that it is set up quickly.

:::def Standard electrode (reduction) potential, E⦵
The voltage measured when a half-cell is connected to a standard hydrogen electrode, under standard conditions: 298 K, ions at a concentration of 1.00 mol dm⁻³ and gases at a pressure of 101 kPa. It is written for the half-equation as a reduction (electrons on the left).
:::

:::html
<figure class="fig small"><svg viewBox="4 0 345 270" role="img" aria-label="A standard hydrogen electrode on the left joined by a salt bridge and a voltmeter to a copper electrode in copper(II) sulfate solution on the right"><path class="ln" d="M20 114L20 214L125 214L125 114"/><path class="ln" d="M225 114L225 214L330 214L330 114"/><path class="fa" d="M21 134H124V213H21Z"/><path class="fa" d="M226 134H329V213H226Z"/><path class="fm2" d="M72 76H78V196H72Z"/><path class="fm2" d="M284 76H290V196H284Z"/><path class="ln" d="M36 80L36 200"/><circle class="fa2" cx="31" cy="192" r="2.5"/><circle class="fa2" cx="41" cy="184" r="2.5"/><circle class="fa2" cx="33" cy="174" r="2.5"/><path class="ln" d="M100 179L100 92L106 84L244 84L250 92L250 179"/><path class="ln" d="M112 179L112 102L238 102L238 179"/><circle class="f1 s-acc sw2" cx="175" cy="40" r="17"/><text class="tl tc" x="175" y="45">V</text><path class="ln" d="M75 76L75 40L158 40"/><path class="ln" d="M287 76L287 40L192 40"/><path class="c2 sw2" d="M96 26H132" marker-end="url(#ah)"/><text class="tl tc" x="114" y="20">e⁻</text><text class="tl tc" x="36" y="50">H₂(g)</text><text class="tl tc" x="36" y="67">101 kPa</text><text class="tl tc" x="175" y="72">salt bridge</text><text class="tl" x="50" y="122">Pt</text><text class="tl" x="296" y="122">Cu</text><text class="tl tc" x="72" y="236">H⁺(aq)</text><text class="tl tc" x="72" y="253">1.00 mol dm⁻³</text><text class="tl tc" x="278" y="236">Cu²⁺(aq)</text><text class="tl tc" x="278" y="253">1.00 mol dm⁻³</text></svg><figcaption>A cell for measuring the standard electrode potential of copper. The left half-cell is the standard hydrogen electrode (platinum black electrode, hydrogen at 101 kPa, 1.00 mol dm⁻³ H⁺). The right half-cell is copper in 1.00 mol dm⁻³ copper(II) ions. A high-resistance voltmeter reads the cell voltage, and the salt bridge completes the circuit. The arrow shows the direction of electron flow in the wire.</figcaption></figure>
:::

Four parts of the apparatus need a reason:

- The **high-resistance voltmeter** draws almost no current, so the reading is the full potential difference of the cell, with no reaction taking place to change the concentrations.
- The **salt bridge** (a strip of filter paper soaked in potassium nitrate solution, or a gel) completes the circuit by letting ions move between the beakers. **It carries ions, not electrons.** The salt must not react with either solution: potassium nitrate is used because all nitrates are soluble and neither ion forms a precipitate or a complex.
- **Standard conditions** (298 K, 1.00 mol dm⁻³, 101 kPa) are needed because the potential depends on concentration, pressure and temperature.
- The **platinum** electrode is also used for any half-cell that has no metal to dip in the solution.

### Three kinds of half-cell

| Half-cell | What the electrode is | Example half-equation |
|---|---|---|
| a metal in contact with its ions | the metal itself, in 1.00 mol dm⁻³ of its ions | \(\ce{Zn^2+ + 2e- <=> Zn}\) |
| a non-metal and its ions | platinum, in 1.00 mol dm⁻³ of the ions, with the gas at 101 kPa bubbled over it | \(\ce{Cl2 + 2e- <=> 2Cl-}\) |
| ions of the same element in different oxidation states | platinum, in a solution with **both** ions at 1.00 mol dm⁻³ | \(\ce{Fe^3+ + e- <=> Fe^2+}\) |

When the half-cell is joined to the standard hydrogen electrode, the voltage reading is its E⦵. The sign comes from the direction in which the electrons flow. If electrons flow from the hydrogen electrode to the half-cell (so the half-cell is the positive terminal), its E⦵ is positive (copper, +0.34 V); if they flow to the hydrogen electrode, its E⦵ is negative (zinc, −0.76 V).

## The table of standard electrode potentials

The Data section lists many E⦵ values. This table has the ones used most often in this chapter, ordered from the most negative to the most positive.

| Half-equation | E⦵ / V |
|---|---|
| \(\ce{Li+ + e- <=> Li}\) | −3.04 |
| \(\ce{K+ + e- <=> K}\) | −2.92 |
| \(\ce{Ca^2+ + 2e- <=> Ca}\) | −2.87 |
| \(\ce{Na+ + e- <=> Na}\) | −2.71 |
| \(\ce{Mg^2+ + 2e- <=> Mg}\) | −2.38 |
| \(\ce{Al^3+ + 3e- <=> Al}\) | −1.66 |
| \(\ce{Zn^2+ + 2e- <=> Zn}\) | −0.76 |
| \(\ce{Fe^2+ + 2e- <=> Fe}\) | −0.44 |
| \(\ce{Pb^2+ + 2e- <=> Pb}\) | −0.13 |
| \(\ce{2H+ + 2e- <=> H2}\) | 0.00 |
| \(\ce{Cu^2+ + 2e- <=> Cu}\) | +0.34 |
| \(\ce{I2 + 2e- <=> 2I-}\) | +0.54 |
| \(\ce{Fe^3+ + e- <=> Fe^2+}\) | +0.77 |
| \(\ce{Ag+ + e- <=> Ag}\) | +0.80 |
| \(\ce{Br2 + 2e- <=> 2Br-}\) | +1.07 |
| \(\ce{O2 + 4H+ + 4e- <=> 2H2O}\) | +1.23 |
| \(\ce{Cr2O7^2- + 14H+ + 6e- <=> 2Cr^3+ + 7H2O}\) | +1.33 |
| \(\ce{Cl2 + 2e- <=> 2Cl-}\) | +1.36 |
| \(\ce{MnO4- + 8H+ + 5e- <=> Mn^2+ + 4H2O}\) | +1.52 |
| \(\ce{F2 + 2e- <=> 2F-}\) | +2.87 |

How to read it. Each line is a competition for electrons between the oxidised form on the left and the reduced form on the right.

- A **more positive** E⦵ means the oxidised form (on the left) is a **stronger oxidising agent**: it takes electrons more readily. Fluorine, at the bottom, is the strongest oxidising agent in the table; permanganate and dichromate are strong oxidising agents too.
- A **more negative** E⦵ means the reduced form (on the right) is a **stronger reducing agent**: it gives up electrons more readily. Lithium metal is the strongest reducing agent in the table, which is one reason lithium is useful in cells: it is very reactive and light. In a lithium-ion cell the lithium ions move through the electrolyte between the electrodes as the cell is charged and discharged.
- Metals above hydrogen in the table (negative E⦵) react with dilute acids to give hydrogen; those below it (copper, silver) do not.

:::warn E⦵ is not multiplied
Multiplying a half-equation by a number changes the amount of electrons transferred but **not** the potential. \(\ce{2Ag+ + 2e- <=> 2Ag}\) still has E⦵ = +0.80 V. Potential measures the tendency per electron, not per mole of reaction. Adding or doubling an E⦵ is one of the most common slips in this topic.
:::

## Cell potentials

When two half-cells are joined, the one with the **more positive** E⦵ gains electrons (reduction) and becomes the **positive** electrode. The one with the **more negative** E⦵ loses electrons (oxidation) and becomes the **negative** electrode. Electrons flow in the external wire **from the negative electrode to the positive one**.

:::def Standard cell potential, E⦵cell
The potential difference between two half-cells under standard conditions: the E⦵ of the positive electrode minus the E⦵ of the negative electrode.
:::

:::formula Cell potential
\[E^{\ominus}_{\mathrm{cell}} = E^{\ominus}(\text{positive}) - E^{\ominus}(\text{negative})\]
The positive electrode is the one with the more positive E⦵, so E⦵cell is a positive number for a working cell. Use the values exactly as in the table; never multiply them.
:::

:::eg (Exam style) A cell is made from a zinc half-cell and a copper half-cell, both at standard conditions. Identify the positive and negative electrodes, state the direction of electron flow, calculate E⦵cell and write the overall equation.
\(E^{\ominus}(\ce{Cu^2+/Cu}) = +0.34\) V is more positive than \(E^{\ominus}(\ce{Zn^2+/Zn}) = -0.76\) V. So copper is the positive electrode and zinc the negative electrode. [B1]
Electrons flow in the wire from the zinc electrode to the copper electrode. [B1]
\[E^{\ominus}_{\mathrm{cell}} = +0.34 - (-0.76) = +1.10\ \mathrm{V}\] [M1] [A1]
At the zinc electrode: \(\ce{Zn -> Zn^2+ + 2e-}\) (oxidation); at the copper electrode: \(\ce{Cu^2+ + 2e- -> Cu}\) (reduction). Adding gives
\[\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\] [B1]
:::

The widget builds any cell from the half-cells in the table, marks the polarity and the direction of the electrons, and gives E⦵cell, the overall equation and ΔG⦵. Try zinc and copper, then swap them over, then pick two half-cells of your own.

:::html
<div class="widget" data-w="chem-cell" data-left="Zn" data-right="Cu"></div>
:::

### Writing the overall equation

1. Write both half-equations as reductions, as in the table.
2. Reverse the half-equation with the **more negative** E⦵ (it is the one that goes as an oxidation).
3. Multiply the half-equations so that the number of electrons is the same in both. Do not change any E⦵.
4. Add them; the electrons cancel. Cancel any \(\ce{H+}\) or \(\ce{H2O}\) that appear on both sides.

:::eg Write the overall equation, and calculate E⦵cell, for the reaction between acidified permanganate ions and iron(II) ions.
Reduction: \(\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\), E⦵ = +1.52 V. Oxidation (reverse of \(\ce{Fe^3+ + e- <=> Fe^2+}\), E⦵ = +0.77 V): \(\ce{Fe^2+ -> Fe^3+ + e-}\). [B1]
Five electrons are needed, so multiply the iron half-equation by 5: \(\ce{5Fe^2+ -> 5Fe^3+ + 5e-}\). [M1]
Adding and cancelling the electrons:
\[\ce{MnO4- + 8H+ + 5Fe^2+ -> Mn^2+ + 4H2O + 5Fe^3+}\] [A1]
\[E^{\ominus}_{\mathrm{cell}} = +1.52 - (+0.77) = +0.75\ \mathrm{V}\] [A1]
The multiplying by 5 does not change either E⦵.
:::

:::eg Calculate E⦵cell for a cell made of two platinum electrodes dipping in \(\ce{Fe^3+/Fe^2+}\) (each at 1.00 mol dm⁻³) and in \(\ce{I2/I-}\), and write the overall equation.
\(\ce{Fe^3+/Fe^2+}\) (+0.77 V) is more positive than \(\ce{I2/I-}\) (+0.54 V), so the iron half-cell is positive and the iodine half-cell is negative. [B1]
\[E^{\ominus}_{\mathrm{cell}} = +0.77 - (+0.54) = +0.23\ \mathrm{V}\] [M1]
Reverse the iodine half-equation and double the iron one so that two electrons are exchanged:
\[\ce{2Fe^3+ + 2I- -> 2Fe^2+ + I2}\] [A1]
:::

### Predicting whether a reaction is feasible

A reaction is feasible when its E⦵cell is positive, since that is when the overall reaction would drive a positive current in a cell. To test a proposed reaction, identify the oxidising agent and the reducing agent, look up both E⦵ values and calculate E⦵(oxidising agent) − E⦵(reducing agent).

:::key Feasibility from E⦵
A reaction is feasible under standard conditions if E⦵cell is positive, where E⦵cell = E⦵(the half-equation being reduced) − E⦵(the half-equation being oxidised). The oxidising agent is on the left of the more positive half-equation.
:::

:::eg (Exam style) Use E⦵(Fe³⁺/Fe²⁺) = +0.77 V, E⦵(I₂/I⁻) = +0.54 V, E⦵(Cl₂/Cl⁻) = +1.36 V, E⦵(Br₂/Br⁻) = +1.07 V, E⦵(2H⁺/H₂) = 0.00 V and E⦵(Cu²⁺/Cu) = +0.34 V to decide whether (a) \(\ce{Fe^3+}\) ions oxidise iodide ions, (b) chlorine oxidises bromide ions, (c) copper reacts with dilute hydrochloric acid.
(a) The reduction is \(\ce{Fe^3+ -> Fe^2+}\) (+0.77 V) and the oxidation is \(\ce{2I- -> I2}\) (+0.54 V): \(E^{\ominus}_{\mathrm{cell}} = 0.77 - 0.54 = +0.23\) V. Positive, so feasible. [B1]
(b) \(\ce{Cl2 -> 2Cl-}\) (+1.36 V) is reduced and \(\ce{2Br- -> Br2}\) (+1.07 V) is oxidised: \(E^{\ominus}_{\mathrm{cell}} = 1.36 - 1.07 = +0.29\) V. Feasible. [B1]
(c) The reduction would be \(\ce{2H+ -> H2}\) (0.00 V) and the oxidation \(\ce{Cu -> Cu^2+}\) (+0.34 V): \(E^{\ominus}_{\mathrm{cell}} = 0.00 - 0.34 = -0.34\) V. Negative, so not feasible. [B1]
:::

:::eg Copper does react with concentrated nitric acid. Use E⦵ values to explain this, given \(\ce{NO3- + 2H+ + e- <=> NO2 + H2O}\), E⦵ = +0.81 V.
In (c) above the oxidising agent was \(\ce{H+}\), which is too weak (0.00 V against +0.34 V). In nitric acid the oxidising agent is the nitrate ion. [B1]
\(E^{\ominus}_{\mathrm{cell}} = +0.81 - (+0.34) = +0.47\) V, which is positive, so copper is oxidised by nitrate in acid, giving brown nitrogen dioxide. [B1]
:::

### What a positive E⦵cell does not tell you

E⦵ values predict only what is **feasible** under **standard conditions**. Two cautions follow, as with ΔG in [Lattice energy, entropy and Gibbs free energy](#chem.lattice):

- **The rate.** A positive E⦵cell says nothing about speed. A mixture of hydrogen and oxygen has E⦵cell = 1.23 − 0.00 = +1.23 V for forming water, yet it can sit unchanged at room temperature until a spark or a catalyst starts the reaction.
- **The concentration.** E⦵ values apply to 1.00 mol dm⁻³ solutions. In other concentrations the actual potential changes (next section), and a reaction with a small E⦵cell may go the other way. For instance, manganese(IV) oxide does not oxidise chloride ions under standard conditions (E⦵cell = 1.23 − 1.36 = −0.13 V), yet chlorine is made in the laboratory by heating the oxide with *concentrated* hydrochloric acid, because the high concentrations of \(\ce{H+}\) and \(\ce{Cl-}\) shift both potentials in the right direction.

A very small value of E⦵cell, such as +0.03 V, is only just feasible, and a slight change in concentration can reverse it.

:::eg (Stretch) \(\ce{Cu+}\) is formed when copper(II) ions react with copper metal. Use these data to show that \(\ce{Cu+}\) ions disproportionate in water: \(\ce{Cu+ + e- <=> Cu}\), E⦵ = +0.52 V; \(\ce{Cu^2+ + e- <=> Cu+}\), E⦵ = +0.15 V.
A disproportionation is a reaction in which a species is both oxidised and reduced. \(\ce{Cu+}\) can be reduced to Cu (+0.52 V) and oxidised to \(\ce{Cu^2+}\) (the reverse of the +0.15 V half-equation). [B1]
\[\ce{2Cu+ -> Cu^2+ + Cu}\] [B1]
\[E^{\ominus}_{\mathrm{cell}} = +0.52 - (+0.15) = +0.37\ \mathrm{V}\] [M1]
This is positive, so the disproportionation is feasible: copper(I) ions are unstable in water. [A1]
:::

## Concentration and the Nernst equation

E⦵ is for 1.00 mol dm⁻³. Change the concentration and the position of the equilibrium \(\ce{Cu^2+ + 2e- <=> Cu}\) shifts. Using Le Chatelier's principle: a **higher** concentration of \(\ce{Cu^2+}\) pushes the equilibrium to the right, making the electrode **more positive**; a **lower** concentration makes the electrode **less positive**. For a cell, this changes E. For a half-cell of the form oxidised form + electrons ⇌ reduced form:

:::formula Nernst equation (298 K)
\[E = E^{\ominus} + \frac{0.059}{z}\,\log_{10}\frac{[\text{oxidised}]}{[\text{reduced}]}\]
\(z\) is the number of electrons in the half-equation. Concentrations are in mol dm⁻³. A solid metal counts as 1, so for \(\ce{Cu^2+/Cu}\) the equation is \(E = E^{\ominus} + \dfrac{0.059}{2}\log_{10}[\ce{Cu^2+}]\).
:::

At 1.00 mol dm⁻³ the logarithm is zero and \(E = E^{\ominus}\), as it should be. Each tenfold change of the concentration changes E by \(0.059/z\) V.

:::eg (Exam style) Calculate the electrode potential of a copper half-cell in which the concentration of \(\ce{Cu^2+}\) is 0.0100 mol dm⁻³.
\(z = 2\) and the reduced form is a solid (taken as 1). [B1]
\[E = 0.34 + \frac{0.059}{2}\log_{10}(0.0100) = 0.34 + 0.0295 \times (-2)\] [M1]
\[E = +0.28\ \mathrm{V}\] [A1]
The potential is less positive than E⦵, as predicted by Le Chatelier's principle: fewer \(\ce{Cu^2+}\) ions mean less tendency to be reduced.
:::

:::eg (Exam style) A platinum electrode is dipped in a solution containing \(\ce{Fe^3+}\) and \(\ce{Fe^2+}\) in the ratio 10 : 1. Calculate its electrode potential.
For \(\ce{Fe^3+ + e- <=> Fe^2+}\), \(z = 1\) and E⦵ = +0.77 V. [B1]
\[E = 0.77 + \frac{0.059}{1}\log_{10}\frac{10}{1} = 0.77 + 0.059\] [M1]
\[E = +0.83\ \mathrm{V}\] [A1]
Only the **ratio** matters here, because the concentrations appear as a ratio in the same half-cell.
:::

:::eg Calculate E for a cell of zinc in 0.100 mol dm⁻³ zinc ions joined by a salt bridge to copper in 1.00 mol dm⁻³ copper(II) ions.
The copper half-cell is standard: +0.34 V. [B1]
For zinc, \(z = 2\): \(E = -0.76 + 0.0295 \times \log_{10}(0.100) = -0.76 - 0.0295 = -0.7895\) V. [M1]
\[E_{\mathrm{cell}} = 0.34 - (-0.7895) = +1.13\ \mathrm{V}\] [A1]
Diluting the \(\ce{Zn^2+}\) makes zinc a stronger reducing agent, and the cell voltage rises above the standard 1.10 V.
:::

A graph of E against \(\log_{10}[\ce{Cu^2+}]\) is a straight line with a gradient of 0.0295 V per tenfold change, passing through +0.34 V at 1.00 mol dm⁻³.

:::plot Electrode potential of the Cu²⁺/Cu half-cell against log₁₀[Cu²⁺]. The line rises by 0.0295 V for each tenfold increase in concentration and passes through E⦵ = +0.34 V at 1.00 mol dm⁻³, where the logarithm is 0.
--f "0.34+0.0295*x" --label "E = 0.34 + 0.0295 log[Cu²⁺]" --x -4 1 --y 0.2 0.4 --pt "0,0.34,E⦵@se" --pt "-2,0.281,+0.28 V at 0.0100 mol dm⁻³@se" --xlabel "log₁₀[Cu²⁺]" --ylabel "E / V" --legend tl --xstep 1 --ystep 0.05
:::

The widget's second tab draws the same line for any half-cell: choose a half-cell, set the concentrations on a logarithmic slider and read E.

:::html
<div class="widget" data-w="chem-cell" data-tab="nernst" data-left="Cu" data-right="Ag"></div>
:::

## Cell potential and free energy

The electrical work done by a cell is the charge that passes multiplied by the voltage. If \(n\) moles of electrons are transferred in the overall equation, the charge is \(nF\), and the maximum work is \(nFE^{\ominus}_{\mathrm{cell}}\). The system does the work, so its Gibbs free energy falls:

:::formula Free energy and cell potential
\[\Delta G^{\ominus} = -\,n\,F\,E^{\ominus}_{\mathrm{cell}}\]
\(n\) = number of moles of electrons transferred in the equation as written, \(F = 9.65 \times 10^4\ \mathrm{C\,mol^{-1}}\), E⦵cell in volts. This gives \(\Delta G^{\ominus}\) in **J mol⁻¹**; divide by 1000 for kJ mol⁻¹.
:::

A positive E⦵cell therefore gives a negative ΔG⦵, which is the same condition for feasibility that you met in [Lattice energy, entropy and Gibbs free energy](#chem.lattice).

:::eg (Exam style) Calculate ΔG⦵ for \(\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\), for which E⦵cell = +1.10 V.
Two electrons are transferred (\(\ce{Zn -> Zn^2+ + 2e-}\)), so \(n = 2\). [B1]
\[\Delta G^{\ominus} = -2 \times 9.65 \times 10^{4} \times 1.10\] [M1]
\[\Delta G^{\ominus} = -2.12 \times 10^{5}\ \mathrm{J\,mol^{-1}} = -212\ \mathrm{kJ\,mol^{-1}}\] [A1]
:::

:::eg Calculate ΔG⦵ for the permanganate and iron(II) reaction \(\ce{MnO4- + 8H+ + 5Fe^2+ -> Mn^2+ + 4H2O + 5Fe^3+}\), with E⦵cell = +0.75 V.
Five electrons are transferred in the equation as written, so \(n = 5\). [B1]
\[\Delta G^{\ominus} = -5 \times 9.65 \times 10^{4} \times 0.75 = -3.62 \times 10^{5}\ \mathrm{J\,mol^{-1}} = -362\ \mathrm{kJ\,mol^{-1}}\] [M1] [A1]
:::

:::warn Which "n"?
Use the number of electrons in the **balanced equation as written**. If you double the equation, \(n\) and ΔG⦵ both double, but E⦵cell does not change.
:::

:::board
AQA also covers electrochemical cells that are used as commercial energy sources, including fuel cells such as the hydrogen–oxygen fuel cell. These applications are not in the Cambridge 9701 syllabus.
:::

:::eg Spot the error: Calculate E⦵cell for a standard cell of magnesium in \(\ce{Mg^2+}\)(aq) and silver in \(\ce{Ag+}\)(aq), using \(E^{\ominus}(\ce{Mg^2+/Mg}) = -2.38\) V and \(E^{\ominus}(\ce{Ag+/Ag}) = +0.80\) V, and state the direction of electron flow. [4 marks]
A student wrote this answer.

Line 1: Silver is the positive electrode and magnesium the negative electrode.
Line 2: The silver half-equation is doubled, so \(E^{\ominus}_{\mathrm{cell}} = 2(+0.80) - (-2.38) = +3.98\) V.
Line 3: Electrons flow from the magnesium to the silver.

Line 1 is correct [B1]. **Line 2 is wrong: doubling a half-equation does not double E⦵. The value of +0.80 V is used as it is, so the method and the answer are lost [M0] [A0].** Line 3 is correct [B1].

Correct line 2: \(E^{\ominus}_{\mathrm{cell}} = +0.80 - (-2.38) = +3.18\) V. [M1] [A1]

The student scores 2 out of 4. E⦵ is a property of the half-equation per electron, so it is never multiplied by the coefficients.
:::

:::try Start easy, finish at exam standard
Q: At which electrode does reduction happen in electrolysis, and what is its sign?
A: At the cathode, which is the negative electrode in electrolysis.
Q: State the products at each electrode when molten sodium bromide is electrolysed.
A: Sodium at the cathode and bromine at the anode.
Q: Calculate the charge, in coulombs, that passes when a current of 2.50 A flows for 40.0 minutes.
A: \(Q = It = 2.50 \times (40.0 \times 60) = 6000\) C.
Q: Calculate the mass of zinc deposited at the cathode when a current of 3.00 A passes through zinc sulfate solution for 1.00 hour. (\(A_r\) of Zn = 65.4)
A: \(Q = 3.00 \times 3600 = 10\,800\) C; \(n(\mathrm{e^-}) = 10\,800 / 9.65 \times 10^{4} = 0.1119\) mol; \(\ce{Zn^2+ + 2e- -> Zn}\) gives \(n(\ce{Zn}) = 0.05596\) mol; \(m = 0.05596 \times 65.4 = 3.66\) g.
Q: Calculate E⦵cell for a cell made from lead and copper half-cells (E⦵(Pb²⁺/Pb) = −0.13 V, E⦵(Cu²⁺/Cu) = +0.34 V) and say which metal is the negative electrode.
A: \(E^{\ominus}_{\mathrm{cell}} = +0.34 - (-0.13) = +0.47\) V. Lead is the negative electrode (E⦵ is more negative).
Q: Will bromine oxidise iron(II) ions to iron(III) ions? Show your working. (E⦵(Br₂/Br⁻) = +1.07 V, E⦵(Fe³⁺/Fe²⁺) = +0.77 V.)
A: \(E^{\ominus}_{\mathrm{cell}} = +1.07 - (+0.77) = +0.30\) V. Positive, so yes, under standard conditions.
Q: List the conditions that define a standard hydrogen electrode.
A: A platinum (platinum black) electrode, hydrogen gas at 101 kPa, \(\ce{H+}\) at 1.00 mol dm⁻³, at 298 K.
Q: Calculate ΔG⦵, in kJ mol⁻¹, for a reaction with n = 2 and E⦵cell = +0.47 V.
A: \(\Delta G^{\ominus} = -2 \times 9.65 \times 10^{4} \times 0.47 = -9.07 \times 10^{4}\) J mol⁻¹ \(= -90.7\) kJ mol⁻¹.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ State the products at the cathode and at the anode when (a) molten zinc chloride and (b) concentrated aqueous sodium chloride are electrolysed using inert electrodes.
A: (a) Cathode: zinc. [B1] Anode: chlorine. [B1]
(b) Cathode: hydrogen (water is reduced in preference to sodium ions). [B1] Anode: chlorine. [B1]
Q: [3 marks] ★ A current of 0.800 A flows for 25.0 minutes through silver nitrate solution. Calculate the mass of silver deposited at the cathode.
A: \(Q = 0.800 \times 1500 = 1200\) C [M1]
\(n(\mathrm{e^-}) = 1200 / 9.65 \times 10^{4} = 0.01244\) mol, and \(n(\ce{Ag}) = n(\mathrm{e^-})\) [M1]
\(m = 0.01244 \times 107.9 = 1.34\) g [A1]
Q: [5 marks] ★★ Dilute sulfuric acid is electrolysed with inert electrodes. A current of 1.50 A flows for 30.0 minutes. Calculate the volume of (a) hydrogen and (b) oxygen formed, at room conditions.
H: Write the half-equation at each electrode to find the moles of electrons per mole of gas.
A: \(Q = 1.50 \times 1800 = 2700\) C, \(n(\mathrm{e^-}) = 2700 / 9.65 \times 10^{4} = 0.02798\) mol [M1]
(a) \(\ce{2H+ + 2e- -> H2}\): \(n(\ce{H2}) = 0.02798 / 2 = 0.01399\) mol [M1]; \(V = 0.01399 \times 24.0 = 0.336\ \mathrm{dm^3} = 336\ \mathrm{cm^3}\) [A1]
(b) \(\ce{2H2O -> O2 + 4H+ + 4e-}\): \(n(\ce{O2}) = 0.02798 / 4 = 6.995 \times 10^{-3}\) mol [M1]; \(V = 168\ \mathrm{cm^3}\) [A1]
Q: [4 marks] ★★ In an experiment to find the Avogadro constant, a current of 0.250 A flowed for 60.0 minutes through copper(II) sulfate solution with copper electrodes. The cathode gained 0.294 g. Use \(e = 1.60 \times 10^{-19}\) C to calculate L.
A: \(Q = 0.250 \times 3600 = 900\) C [M1]
\(n(\ce{Cu}) = 0.294 / 63.5 = 4.630 \times 10^{-3}\) mol, \(n(\mathrm{e^-}) = 9.260 \times 10^{-3}\) mol [M1]
\(L = Q / (n(\mathrm{e^-})\,e)\) [M1]
\(= 900 / (9.260 \times 10^{-3} \times 1.60 \times 10^{-19}) = 6.07 \times 10^{23}\ \mathrm{mol^{-1}}\) [A1]
Q: [4 marks] ★★ A cell is made from a platinum electrode in a solution of \(\ce{V^3+}\) and \(\ce{V^2+}\) and a platinum electrode in a solution of \(\ce{Sn^4+}\) and \(\ce{Sn^2+}\), all at 1.00 mol dm⁻³. Use \(\ce{V^3+ + e- <=> V^2+}\), E⦵ = −0.26 V and \(\ce{Sn^4+ + 2e- <=> Sn^2+}\), E⦵ = +0.15 V to state the positive electrode, calculate E⦵cell, give the direction of electron flow, and write the overall equation.
H: Reverse the vanadium half-equation, then make the electrons equal.
A: The tin half-cell is positive because its E⦵ is more positive. [B1]
\(E^{\ominus}_{\mathrm{cell}} = +0.15 - (-0.26) = +0.41\) V [B1]
Electrons flow in the wire from the vanadium half-cell to the tin half-cell. [B1]
\(\ce{Sn^4+ + 2V^2+ -> Sn^2+ + 2V^3+}\) [B1]
Q: [5 marks] ★★ Acidified potassium manganate(VII) is used in titrations. (a) Use E⦵(MnO₄⁻/Mn²⁺) = +1.52 V, E⦵(Br₂/Br⁻) = +1.07 V and E⦵(Cl₂/Cl⁻) = +1.36 V to show that acidified \(\ce{MnO4-}\) can oxidise both bromide ions and chloride ions. (b) Explain why hydrochloric acid cannot be used to acidify a manganate(VII) titration of iron(II).
A: (a) With bromide: \(E^{\ominus}_{\mathrm{cell}} = +1.52 - (+1.07) = +0.45\) V, positive. [B1] With chloride: \(+1.52 - (+1.36) = +0.16\) V, positive. [B1] (Both reactions are feasible.)
(b) \(\ce{MnO4-}\) would also oxidise \(\ce{Cl-}\) from the hydrochloric acid, which is feasible. [B1]
This uses up some of the manganate(VII), so the titre would be too large and the iron(II) result too high. [B1] Dilute sulfuric acid is used, because sulfate is not oxidised. [B1]
Q: [4 marks] ★★ (a) Given E⦵(Ag⁺/Ag) = +0.80 V, calculate the electrode potential of a silver half-cell in which the concentration of \(\ce{Ag+}\) is 0.0500 mol dm⁻³. (b) State and explain how E changes if the concentration of silver ions is increased.
A: (a) \(z = 1\) [B1]; \(E = 0.80 + 0.059 \log_{10}(0.0500)\) [M1] \(= +0.72\) V [A1]
(b) E increases (becomes more positive), because a higher concentration of \(\ce{Ag+}\) moves the equilibrium \(\ce{Ag+ + e- <=> Ag}\) to the right. [B1]
Q: [6 marks] ★★★ A cell is made from a zinc half-cell and a silver half-cell, both at standard conditions (E⦵(Zn²⁺/Zn) = −0.76 V, E⦵(Ag⁺/Ag) = +0.80 V; F = 9.65 × 10⁴ C mol⁻¹). (a) Calculate E⦵cell. (b) Calculate ΔG⦵ for \(\ce{Zn(s) + 2Ag+(aq) -> Zn^2+(aq) + 2Ag(s)}\). (c) The concentration of \(\ce{Ag+}\) is changed to 0.0100 mol dm⁻³. Calculate the new cell potential.
H: In (b), how many electrons are transferred in the equation as written?
H: In (c), only the silver half-cell changes.
A: (a) \(E^{\ominus}_{\mathrm{cell}} = +0.80 - (-0.76) = +1.56\) V [B1]
(b) \(n = 2\); \(\Delta G^{\ominus} = -2 \times 9.65 \times 10^{4} \times 1.56\) [M1] \(= -3.01 \times 10^{5}\) J mol⁻¹ \(= -301\) kJ mol⁻¹ [A1]
(c) \(E(\ce{Ag+/Ag}) = 0.80 + 0.059 \log_{10}(0.0100) = 0.80 - 0.118 = 0.682\) V [M1]
\(E_{\mathrm{cell}} = 0.682 - (-0.76)\) [M1] \(= +1.44\) V [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Use these data to show that copper(I) ions disproportionate: \(\ce{Cu+ + e- <=> Cu}\), E⦵ = +0.52 V; \(\ce{Cu^2+ + e- <=> Cu+}\), E⦵ = +0.15 V. Then calculate ΔG⦵ for \(\ce{2Cu+ -> Cu^2+ + Cu}\).
H: ΔG⦵ uses the number of electrons in the equation as written. How many are transferred when two \(\ce{Cu+}\) ions react?
A: \(\ce{Cu+}\) is reduced to Cu (+0.52 V) and oxidised to \(\ce{Cu^2+}\) (+0.15 V). [B1]
\(E^{\ominus}_{\mathrm{cell}} = +0.52 - (+0.15) = +0.37\) V, positive, so the reaction is feasible. [M1] [A1]
\(n = 1\): one electron is passed from one \(\ce{Cu+}\) to the other. \(\Delta G^{\ominus} = -1 \times 9.65 \times 10^{4} \times 0.37\) [M1] \(= -35.7\) kJ mol⁻¹. [A1]
Q: [6 marks] ★★★ Aluminium is extracted by electrolysing aluminium oxide dissolved in molten cryolite using carbon anodes. A cell runs at \(1.00 \times 10^{5}\) A for 1.00 hour. (a) Write the half-equation at the cathode and calculate the mass of aluminium formed. (b) At the anode the oxide ions are oxidised, \(\ce{2O^2- -> O2 + 4e-}\), and the oxygen reacts with the carbon to form carbon dioxide. Calculate the mass of carbon used up. (c) Suggest why the anodes have to be replaced regularly.
H: Use the moles of electrons from part (a).
A: (a) \(\ce{Al^3+ + 3e- -> Al}\) [B1]; \(Q = 3.60 \times 10^{8}\) C, \(n(\mathrm{e^-}) = 3731\) mol, \(n(\ce{Al}) = 1244\) mol [M1]; \(m = 1244 \times 27.0 = 33.6\) kg [A1]
(b) \(n(\ce{O2}) = 3730.6 / 4 = 932.6\) mol, and \(\ce{C + O2 -> CO2}\) uses one carbon per \(\ce{O2}\). [M1] \(m(\ce{C}) = 932.6 \times 12.0 = 11.2\) kg [A1]
(c) The carbon anodes are burned away as carbon dioxide forms. [B1]
:::

:::quiz
? Which statement about electrolysis is correct?
- Oxidation happens at the cathode.
+ The anode is the positive electrode and oxidation happens there.
- The cathode is the positive electrode.
- Reduction happens at the anode.
> "An Ox, Red Cat": oxidation at the anode, reduction at the cathode. In electrolysis the anode is joined to the positive terminal of the supply.
? What is formed at the cathode when aqueous sodium chloride is electrolysed?
- sodium
+ hydrogen
- chlorine
- oxygen
> Sodium (E⦵ = −2.71 V) is less easily reduced than water (−0.83 V), so water is reduced to hydrogen. Chlorine would be at the anode.
? A current of 2.00 A flows for 965 s. How many moles of electrons pass? (F = 9.65 × 10⁴ C mol⁻¹)
- 0.0100
+ 0.0200
- 0.0400
- 2.00
> Q = It = 2.00 × 965 = 1930 C and n = 1930 / 96 500 = 0.0200 mol. Dividing by 2 or forgetting to multiply by the time gives the wrong options.
? Why is a high-resistance voltmeter used to measure E⦵cell?
- To make the reaction in the cell faster.
- To carry electrons through the salt bridge.
+ So that almost no current flows and the full potential difference is read.
- To keep the temperature at 298 K.
> A large current would change the concentrations and drop the voltage. The salt bridge carries ions, and the voltmeter does not control the rate or temperature.
? E⦵ for Zn²⁺/Zn is −0.76 V and for Ag⁺/Ag is +0.80 V. What is E⦵cell for a cell of these two half-cells?
- +0.04 V
- −1.56 V
+ +1.56 V
- +2.36 V
> The positive electrode is silver: 0.80 − (−0.76) = +1.56 V. Adding the numbers with the wrong sign gives +0.04 V, subtracting the wrong way round gives −1.56 V, and doubling the silver half-equation gives the wrong value 0.80 × 2 + 0.76 = +2.36 V, because E⦵ is never multiplied.
? Which statement about the Nernst equation is correct for Cu²⁺ + 2e⁻ ⇌ Cu?
- E increases when [Cu²⁺] decreases.
+ E decreases when [Cu²⁺] decreases.
- E is unchanged by concentration.
- E = E⦵ whenever [Cu²⁺] is 0.1 mol dm⁻³.
> Lower [Cu²⁺] moves the equilibrium to the left (less reduction), so the electrode becomes less positive. E equals E⦵ only at 1.00 mol dm⁻³.
? The salt bridge in a cell contains potassium nitrate. What does it do?
- It carries electrons from one half-cell to the other.
+ It completes the circuit by allowing ions to move between the half-cells.
- It supplies the metal ions for each electrode.
- It increases E⦵cell.
> Electrons travel only in the wire. Ions in the salt bridge move so that charge does not build up in the beakers.
:::

:::checklist What you can now do
- [ ] I can predict the products of electrolysis of molten and aqueous electrolytes from E⦵ values and concentration, and write the half-equations.
- [ ] I can use F = Le and Q = It, and calculate the mass or volume of a substance liberated in electrolysis.
- [ ] I can describe and calculate a determination of the Avogadro constant by electrolysis.
- [ ] I can define standard electrode potential and standard cell potential, and describe the standard hydrogen electrode.
- [ ] I can describe how to measure E⦵ for a metal in contact with its ions and for ions of the same element in different oxidation states.
- [ ] I can calculate E⦵cell, identify the positive and negative electrodes and give the direction of electron flow.
- [ ] I can use E⦵ values to judge relative strengths of oxidising and reducing agents and to predict whether a reaction is feasible, and I know the limits of such predictions.
- [ ] I can write a full redox equation by combining two half-equations.
- [ ] I can state and use the effect of concentration on E, and use the Nernst equation for \(\ce{Cu^2+/Cu}\) and \(\ce{Fe^3+/Fe^2+}\).
- [ ] I can calculate ΔG⦵ from E⦵cell using ΔG⦵ = −nFE⦵cell.
:::

:::recap
- Electrolysis: anode is positive (oxidation), cathode is negative (reduction). In aqueous solution the more positive E⦵ is reduced at the cathode and the more negative E⦵ is oxidised at the anode; concentrated chloride gives chlorine; sulfate and nitrate are not discharged; a copper anode dissolves.
- \(Q = It\) (seconds), \(F = Le = 9.65 \times 10^4\) C mol⁻¹, \(n(\mathrm{e^-}) = Q/F\); then use the half-equation ratio. L can be found by weighing the cathode: \(L = Q/(n(\mathrm{e^-})\,e)\).
- E⦵ is measured against the standard hydrogen electrode (Pt black, 101 kPa \(\ce{H2}\), 1.00 mol dm⁻³ \(\ce{H+}\), 298 K), with a high-resistance voltmeter and a salt bridge; gases and ions of one element use a platinum electrode.
- More positive E⦵: stronger oxidising agent. More negative E⦵: stronger reducing agent. Never multiply E⦵.
- \(E^{\ominus}_{\mathrm{cell}} = E^{\ominus}(\text{positive}) - E^{\ominus}(\text{negative})\). Electrons flow from the negative to the positive electrode. Positive E⦵cell: feasible, but it may be slow or non-standard.
- Nernst: \(E = E^{\ominus} + (0.059/z)\log_{10}([\text{ox}]/[\text{red}])\). Higher [oxidised] gives a more positive E.
- \(\Delta G^{\ominus} = -nFE^{\ominus}_{\mathrm{cell}}\) (J mol⁻¹; divide by 1000 for kJ).
:::

:::links
- read: [Redox equilibria menu](https://www.chemguide.co.uk/physical/redoxeqiamenu.html) · Chemguide · electrode potentials, the electrochemical series and using E⦵ to predict reactions
- read: [An introduction to redox equilibria and electrode potentials](https://www.chemguide.co.uk/physical/redoxeqia/introduction.html) · Chemguide · half-cells, the standard hydrogen electrode and how cell voltages arise
- read: [Making predictions using redox (electrode) potentials](https://www.chemguide.co.uk/physical/redoxeqia/predict.html) · Chemguide · using E⦵ to decide whether a reaction happens, and its limits
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [pH, buffers, solubility product and partition](#chem.acids2) uses the equilibrium ideas of this chapter in solutions of acids and bases.
