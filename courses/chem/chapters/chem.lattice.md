@chapter chem.lattice
@title Lattice energy, entropy and Gibbs free energy
@level a2
@paper CAIE 9701 Paper 4
@time 8–10 hours
@summary Why ionic compounds are stable and why reactions go the way they do. You will build Born–Haber cycles to find lattice energies, link lattice energy and hydration to the enthalpy change of solution, then learn entropy and the Gibbs free energy equation to decide whether a reaction is feasible and at which temperature.

:::why
Enthalpy change alone does not tell you whether a reaction happens. Ice melts at room temperature although melting takes in energy, and salt dissolves in water although its lattice is very strong. This chapter adds the two missing ideas: the energy stored in an ionic lattice, which explains why ionic compounds form and dissolve as they do, and entropy, which explains why some endothermic changes still go. Together they give you ΔG, the quantity chemists use to decide whether a reaction is feasible.
:::

**Before you start**, you should know Hess's law and enthalpy of formation from [Chemical energetics](#chem.energetics), ionisation energy from [Atomic structure](#chem.atoms) and ionic bonding from [Chemical bonding](#chem.bonding).

:::try Warm-up
Q: Write the equation, with state symbols, for the standard enthalpy change of formation of sodium chloride. (from [Chemical energetics](#chem.energetics))
A: \(\ce{Na(s) + 1/2Cl2(g) -> NaCl(s)}\). The elements are in their standard states and exactly 1 mol of product forms.
Q: Write the equation for the second ionisation energy of magnesium. (from [Atomic structure](#chem.atoms))
A: \(\ce{Mg+(g) -> Mg^2+(g) + e-}\). It removes an electron from a gaseous 1+ ion.
Q: A sodium ion and a magnesium ion both have the electron configuration 1s² 2s² 2p⁶. Which is smaller, and why? (from [Atomic structure](#chem.atoms))
A: \(\ce{Mg^2+}\). It has the same 10 electrons but 12 protons instead of 11, so the nuclear attraction is stronger and pulls the electrons in closer.
:::

## Why ionic compounds are stable

Sodium and chlorine react violently to give sodium chloride. That seems natural, but look at the energy bookkeeping for one pair of atoms. Taking an electron from a sodium atom costs energy (the ionisation energy). Giving that electron to a chlorine atom releases only a little energy back. Turning atoms into ions is therefore **endothermic overall**. Sodium chloride still forms because of a third step: the gaseous ions, oppositely charged, fall together into a lattice, and that releases a very large amount of energy. The ionic compound is stable because the lattice more than pays for the cost of making the ions.

That third step cannot be measured directly, because nobody can collect a mole of gaseous \(\ce{Na+}\) and a mole of gaseous \(\ce{Cl-}\) and let them crystallise. So chemists calculate it from a Hess's law cycle that uses numbers they can measure. That cycle is the **Born–Haber cycle**, and building it is the main skill of the first half of this chapter. First you need four definitions.

## The definitions

All the enthalpy changes in this chapter are standard enthalpy changes: they are measured under standard conditions (298 K, 101 kPa, solutions at 1.00 mol dm⁻³), and each definition is for **one mole** of the named thing.

:::def Enthalpy change of atomisation, \(\Delta H^{\ominus}_{\mathrm{at}}\)
The enthalpy change when one mole of gaseous atoms is formed from the element in its standard state.
:::

Atomisation is always endothermic, because bonds or attractions between the particles must be broken. Note the words "one mole of gaseous **atoms**". For chlorine, which is \(\ce{Cl2}\) in its standard state, only half a mole of molecules is needed:

\[\ce{Na(s) -> Na(g)}\qquad \Delta H^{\ominus}_{\mathrm{at}} = +107\ \mathrm{kJ\,mol^{-1}}\]
\[\ce{1/2Cl2(g) -> Cl(g)}\qquad \Delta H^{\ominus}_{\mathrm{at}} = +122\ \mathrm{kJ\,mol^{-1}}\]

(The second value is close to half the Cl–Cl bond energy, ½ × 242 = 121 kJ mol⁻¹; tables of atomisation enthalpies use more precise bond energies than the rounded Data section value.)

The ionisation energies are the ones you met in [Atomic structure](#chem.atoms): the first removes one electron from each atom in a mole of gaseous atoms, and the second removes a further electron from each gaseous 1+ ion. Use the values in the Data section of the exam paper.

:::def First electron affinity, EA₁
The enthalpy change when one electron is added to each atom in one mole of gaseous atoms to form one mole of gaseous 1− ions.
:::

\[\ce{Cl(g) + e- -> Cl-(g)}\qquad \mathrm{EA}_1 = -349\ \mathrm{kJ\,mol^{-1}}\]

The first electron affinity of most non-metals is exothermic: the incoming electron is attracted by the nucleus. Adding a second electron is a different matter. The ion \(\ce{O-}\) is already negative and repels the new electron, so the **second electron affinity** is endothermic:

\[\ce{O(g) + e- -> O-(g)}\qquad \mathrm{EA}_1 = -141\ \mathrm{kJ\,mol^{-1}}\]
\[\ce{O-(g) + e- -> O^2-(g)}\qquad \mathrm{EA}_2 = +798\ \mathrm{kJ\,mol^{-1}}\]

:::def Lattice energy, \(\Delta H^{\ominus}_{\mathrm{latt}}\)
The enthalpy change when one mole of an ionic compound is formed from its gaseous ions under standard conditions.
:::

\[\ce{Na+(g) + Cl-(g) -> NaCl(s)}\qquad \Delta H^{\ominus}_{\mathrm{latt}} = -785\ \mathrm{kJ\,mol^{-1}}\]

:::warn The direction of the lattice-energy definition
In this syllabus the lattice energy is for **gaseous ions forming the solid**, so it is always **exothermic** (negative). Many books and websites define the opposite process, breaking the solid into gaseous ions, which is endothermic and has the same size but the opposite sign. If an exam question gives a positive number for a "lattice energy", read the definition it uses. Write your equation with the gaseous ions on the left, as above.
:::

### Factors that affect electron affinity

Electron affinity measures how strongly a nucleus attracts an extra electron into the outer shell. The same three factors as for ionisation energy decide it:

- **Nuclear charge.** More protons attract the incoming electron more strongly, so the electron affinity is more exothermic.
- **Atomic radius.** The further the outer shell is from the nucleus, the weaker the attraction.
- **Shielding.** Inner shells repel the incoming electron and cancel part of the nuclear charge.

Across a period the nuclear charge rises and the radius falls, so the first electron affinity becomes more exothermic from Group 16 to Group 17. Down a group the radius and the shielding increase, so the attraction falls and the first electron affinity becomes **less exothermic**.

| Group 17 atom | EA₁ / kJ mol⁻¹ | Group 16 atom | EA₁ / kJ mol⁻¹ |
|---|---|---|---|
| F | −328 | O | −141 |
| Cl | −349 | S | −200 |
| Br | −325 | Se | −195 |
| I | −295 | Te | −190 |

Values from a standard data book; use them as data for this chapter's questions.

Look at the first row. The trend "less exothermic down the group" holds from chlorine to iodine and from sulfur to tellurium, but **fluorine and oxygen are exceptions**. Their atoms are so small that the 2p sub-shell is crowded: the electrons already there repel an incoming electron strongly, which cancels some of the attraction. So the first electron affinity of chlorine is more exothermic than that of fluorine, and that of sulfur is more exothermic than that of oxygen. The second electron affinity of any Group 16 element is endothermic, because a negative ion is gaining another electron.

## The Born–Haber cycle for sodium chloride

A Born–Haber cycle is a Hess's law cycle (see [Chemical energetics](#chem.energetics)) for the formation of an ionic compound. There are two routes from the elements to the solid compound:

- **Route 1, direct:** the enthalpy change of formation, \(\Delta H^{\ominus}_{\mathrm{f}}\), which can be measured.
- **Route 2, in steps:** turn the elements into gaseous atoms, then into gaseous ions, then let the ions form the lattice.

By Hess's law both routes have the same total enthalpy change. The cycle is drawn as a **level diagram**: each species is a horizontal level, higher up means more enthalpy, and each step is an arrow, up for an endothermic step and down for an exothermic one.

:::html
<figure class="fig small"><svg viewBox="0 0 345 382" role="img" aria-label="Born–Haber cycle for sodium chloride drawn as a level diagram: from sodium solid and half a mole of chlorine gas, steps 1 and 2 go up to gaseous atoms, step 3 goes up to a gaseous sodium ion and an electron, step 4 goes down to the gaseous sodium and chloride ions, and step 5 goes down to solid sodium chloride, which is also reached directly by the enthalpy change of formation"><path class="ln thick" d="M150 240.9H188"/><path class="ln thick" d="M150 208.8H210"/><path class="ln thick" d="M150 172.2H232"/><path class="ln thick" d="M150 24.0H254"/><path class="ln thick" d="M242 128.7H276"/><path class="ln thick" d="M150 364.2H276"/><text class="tl" x="144" y="244.9" text-anchor="end">Na(s) + ½Cl₂(g)</text><text class="tl" x="144" y="212.8" text-anchor="end">Na(g) + ½Cl₂(g)</text><text class="tl" x="144" y="176.2" text-anchor="end">Na(g) + Cl(g)</text><text class="tl" x="144" y="28.0" text-anchor="end">Na⁺(g) + e⁻ + Cl(g)</text><text class="tl" x="144" y="368.2" text-anchor="end">NaCl(s)</text><text class="tl" x="282" y="132.7">Na⁺(g) +</text><text class="tl" x="282" y="148.7">Cl⁻(g)</text><path class="ln" d="M160 240.9V364.2" marker-end="url(#ah)"/><path class="ln" d="M182 240.9V208.8" marker-end="url(#ah)"/><path class="ln" d="M204 208.8V172.2" marker-end="url(#ah)"/><path class="ln" d="M226 172.2V24.0" marker-end="url(#ah)"/><path class="ln" d="M248 24.0V128.7" marker-end="url(#ah)"/><path class="c2 sw2" d="M270 128.7V364.2" marker-end="url(#ah)"/><text class="tl" x="154" y="306.6" text-anchor="end">ΔHf</text><text class="tl" x="188" y="228.9">1</text><text class="tl" x="210" y="194.5">2</text><text class="tl" x="220" y="102.1" text-anchor="end">3</text><text class="tl" x="254" y="80.3">4</text><text class="tl" x="276" y="310.4">5</text></svg><figcaption>The Born–Haber cycle for sodium chloride, drawn to scale. The levels rise for endothermic steps (1 to 3) and fall for exothermic steps (4, 5 and the formation enthalpy). The thicker arrow, step 5, is the lattice energy.</figcaption></figure>
:::

The numbered steps are, with the data used in this chapter:

| Step | Process | Name | Value / kJ mol⁻¹ |
|---|---|---|---|
| 1 | \(\ce{Na(s) -> Na(g)}\) | atomisation of sodium | +107 |
| 2 | \(\ce{1/2Cl2(g) -> Cl(g)}\) | atomisation of chlorine | +122 |
| 3 | \(\ce{Na(g) -> Na+(g) + e-}\) | first ionisation energy of sodium | +494 |
| 4 | \(\ce{Cl(g) + e- -> Cl-(g)}\) | first electron affinity of chlorine | −349 |
| 5 | \(\ce{Na+(g) + Cl-(g) -> NaCl(s)}\) | lattice energy | to find |
| direct | \(\ce{Na(s) + 1/2Cl2(g) -> NaCl(s)}\) | enthalpy change of formation | −411 |

Going round route 2 must give the same total as route 1:

\[\Delta H^{\ominus}_{\mathrm{f}} = \Delta H^{\ominus}_{\mathrm{at}}(\ce{Na}) + \Delta H^{\ominus}_{\mathrm{at}}(\ce{Cl}) + \mathrm{IE}_1(\ce{Na}) + \mathrm{EA}_1(\ce{Cl}) + \Delta H^{\ominus}_{\mathrm{latt}}\]

:::key Born–Haber equation
\(\Delta H^{\ominus}_{\mathrm{f}}\) = (sum of the atomisation enthalpies) + (sum of the ionisation energies) + (sum of the electron affinities) + \(\Delta H^{\ominus}_{\mathrm{latt}}\). Rearrange it to find whichever term is missing. Every term is for the amount of substance in the formation equation of **one mole of the compound**.
:::

:::eg (Exam style) Calculate the lattice energy of sodium chloride from these data (data for this question). ΔHf(NaCl) = −411, ΔHat(Na) = +107, ΔHat(Cl) = +122, IE₁(Na) = +494, EA₁(Cl) = −349, all in kJ mol⁻¹.
Write the Born–Haber equation for the compound: [M1]
\[\Delta H^{\ominus}_{\mathrm{f}} = \Delta H^{\ominus}_{\mathrm{at}}(\ce{Na}) + \Delta H^{\ominus}_{\mathrm{at}}(\ce{Cl}) + \mathrm{IE}_1 + \mathrm{EA}_1 + \Delta H^{\ominus}_{\mathrm{latt}}\]
Rearrange for the lattice energy and substitute:
\[\Delta H^{\ominus}_{\mathrm{latt}} = -411 - (107 + 122 + 494 - 349) = -411 - 374\] [M1]
\[\Delta H^{\ominus}_{\mathrm{latt}} = -785\ \mathrm{kJ\,mol^{-1}}\] [A1]
The value is large and negative, as expected for ions of opposite charge coming together. The sign and the unit both score.
:::

The widget builds the same cycle to scale. Change any value and watch the levels move, then choose a different unknown term and let it calculate that instead.

:::html
<div class="widget" data-w="chem-bornhaber" data-compound="NaCl"></div>
:::

### Steps for any Born–Haber cycle

:::steps
1. Write the formation equation for **one mole** of the compound. This sets how many atoms and ions of each element appear. For \(\ce{MgCl2}\) there is one Mg and two Cl.
2. Atomise each element: one \(\Delta H_{\mathrm{at}}\) per mole of metal atoms, and one per **mole of non-metal atoms**, multiplied by the number of atoms in the formula (2 for \(\ce{MgCl2}\)).
3. Form the cation: first ionisation energy, then the second (and third) if the charge is 2+ (or 3+). Use every ionisation energy of that atom up to the charge.
4. Form the anion: the first electron affinity for each non-metal atom, plus the second if the charge is 2−.
5. Put the gaseous ions into the lattice: the lattice energy.
6. Check the direction of every arrow: a negative value goes down, a positive value up.
:::

### Compounds with 2+ ions and 2− ions: magnesium oxide

Magnesium oxide, \(\ce{MgO}\), is built from \(\ce{Mg^2+}\) and \(\ce{O^2-}\), so two extra steps appear: the second ionisation energy of magnesium and the second electron affinity of oxygen. Oxygen's atomisation is per mole of O atoms, \(\ce{1/2O2(g) -> O(g)}\).

:::eg (Exam style) Calculate the lattice energy of magnesium oxide from these data (data for this question), in kJ mol⁻¹: ΔHf(MgO) = −602; ΔHat(Mg) = +148; IE₁(Mg) = +736; IE₂(Mg) = +1450; ΔHat(O) = +249; EA₁(O) = −141; EA₂(O) = +798. The ionisation energies agree with the Data section.
The oxide ion needs two electrons, so both electron affinities appear, and the magnesium ion needs both ionisation energies. [M1]
\[\Delta H^{\ominus}_{\mathrm{latt}} = \Delta H^{\ominus}_{\mathrm{f}} - \left(\Delta H^{\ominus}_{\mathrm{at}}(\ce{Mg}) + \Delta H^{\ominus}_{\mathrm{at}}(\ce{O}) + \mathrm{IE}_1 + \mathrm{IE}_2 + \mathrm{EA}_1 + \mathrm{EA}_2\right)\]
\[\Delta H^{\ominus}_{\mathrm{latt}} = -602 - (148 + 249 + 736 + 1450 - 141 + 798) = -602 - 3240\] [M1]
\[\Delta H^{\ominus}_{\mathrm{latt}} = -3842\ \mathrm{kJ\,mol^{-1}}\] [A1]
The endothermic second electron affinity (+798) adds to the energy that must be recovered, and the lattice energy still easily pays for it.
:::

:::eg (Exam style) Calculate the enthalpy change of formation of magnesium chloride, \(\ce{MgCl2}\), from these data (data for this question), in kJ mol⁻¹: ΔHat(Mg) = +148; ΔHat(Cl) = +122; IE₁(Mg) = +736; IE₂(Mg) = +1450; EA₁(Cl) = −349; ΔHlatt(MgCl₂) = −2521.
There are **two** chlorine atoms and two chloride ions in the formula, so the chlorine terms are doubled. The ionisation energies of magnesium are not doubled, because there is one magnesium ion. [B1]
\[\Delta H^{\ominus}_{\mathrm{f}} = 148 + 736 + 1450 + 2(122) + 2(-349) + (-2521)\] [M1]
\[\Delta H^{\ominus}_{\mathrm{f}} = 148 + 736 + 1450 + 244 - 698 - 2521 = -641\ \mathrm{kJ\,mol^{-1}}\] [A1]
:::

:::eg Calculate the first electron affinity of chlorine from these data (data for this question), in kJ mol⁻¹: ΔHf(KCl) = −437; ΔHat(K) = +89; IE₁(K) = +418; ΔHat(Cl) = +122; ΔHlatt(KCl) = −717.
Here the unknown is the electron affinity, so rearrange the Born–Haber equation for it. [M1]
\[\mathrm{EA}_1(\ce{Cl}) = \Delta H^{\ominus}_{\mathrm{f}} - \Delta H^{\ominus}_{\mathrm{at}}(\ce{K}) - \Delta H^{\ominus}_{\mathrm{at}}(\ce{Cl}) - \mathrm{IE}_1(\ce{K}) - \Delta H^{\ominus}_{\mathrm{latt}}\]
\[\mathrm{EA}_1(\ce{Cl}) = -437 - 89 - 122 - 418 + 717\] [M1]
\[\mathrm{EA}_1(\ce{Cl}) = -349\ \mathrm{kJ\,mol^{-1}}\] [A1]
This is the value in the data table above. In reality, electron affinities are the measured quantity and lattice energies are found from the cycle, as in the earlier example. The arithmetic is the same either way.
:::

:::warn Five slips that cost marks
(1) Using only the first ionisation energy for \(\ce{Mg^2+}\). (2) Forgetting that the second electron affinity of oxygen is **positive** (endothermic). (3) Using \(\Delta H_{\mathrm{at}}\) of a molecule instead of per mole of atoms (the chlorine value is per mole of Cl, so do not halve it again). (4) Not doubling the chlorine terms for \(\ce{MgCl2}\) (or doubling the magnesium ones). (5) Giving the lattice energy a positive sign: with the gas-to-solid definition it is negative.
:::

## What decides the size of the lattice energy

The lattice energy is released by the attraction between oppositely charged ions. Coulomb's law says the force between two charges is larger when the charges are larger and the distance between them is smaller. The result is the rule you need:

:::key Lattice energy: charge and radius
The lattice energy is more exothermic (a larger negative number) when the ions have **higher charges** and when the ions are **smaller**, so that the distance between their centres is shorter. Charge has by far the bigger effect.
:::

| Compound | Ions | Ionic radii / nm (cation, anion) | ΔHlatt / kJ mol⁻¹ |
|---|---|---|---|
| KCl | \(\ce{K+}\), \(\ce{Cl-}\) | 0.133, 0.181 | −717 |
| NaCl | \(\ce{Na+}\), \(\ce{Cl-}\) | 0.095, 0.181 | −785 |
| NaF | \(\ce{Na+}\), \(\ce{F-}\) | 0.095, 0.136 | −926 |
| MgO | \(\ce{Mg^2+}\), \(\ce{O^2-}\) | 0.065, 0.140 | −3842 |

Lattice energies calculated from Born–Haber cycles with the data in this chapter. Ionic radii are data for this chapter.

Read the table as three comparisons. From KCl to NaCl the charges are the same, but the sodium ion is smaller than the potassium ion, so the ions get closer and the lattice energy becomes more exothermic. From NaCl to NaF the anion is smaller, with the same effect. From NaCl to MgO both ions carry twice the charge (2+ and 2− instead of 1+ and 1−), and the magnesium ion is smaller than the sodium ion: the lattice energy is almost five times larger.

:::eg Explain why the lattice energy of magnesium oxide, −3842 kJ mol⁻¹, is much more exothermic than that of sodium chloride, −785 kJ mol⁻¹.
\(\ce{MgO}\) contains \(\ce{Mg^2+}\) and \(\ce{O^2-}\); \(\ce{NaCl}\) contains \(\ce{Na+}\) and \(\ce{Cl-}\). The ions in MgO have twice the charge, so the electrostatic attraction between oppositely charged ions is much stronger. [B1]
\(\ce{Mg^2+}\) is smaller than \(\ce{Na+}\) (more protons for the same number of electrons) and \(\ce{O^2-}\) is smaller than \(\ce{Cl-}\) (one fewer shell of electrons), so the distance between the ion centres is smaller. [B1]
Both the higher charges and the smaller distance increase the attraction, so more energy is released when the lattice forms. [B1]
:::

This also explains physical properties: the very exothermic lattice energy of MgO is why it melts at a far higher temperature than NaCl and is used to line furnaces.

## Hydration, solution and the energy of dissolving

An ionic solid dissolves when the water–ion attractions are strong enough to pay for breaking the lattice. Two definitions describe the two parts:

:::def Enthalpy change of hydration, \(\Delta H^{\ominus}_{\mathrm{hyd}}\)
The enthalpy change when one mole of gaseous ions dissolves in water to form an infinitely dilute solution.
:::

:::def Enthalpy change of solution, \(\Delta H^{\ominus}_{\mathrm{sol}}\)
The enthalpy change when one mole of an ionic solid dissolves in water to form an infinitely dilute solution.
:::

\[\ce{Na+(g) -> Na+(aq)}\qquad \Delta H^{\ominus}_{\mathrm{hyd}} = -406\ \mathrm{kJ\,mol^{-1}}\]
\[\ce{NaCl(s) -> Na+(aq) + Cl-(aq)}\qquad \Delta H^{\ominus}_{\mathrm{sol}}\]

"Infinitely dilute" means so much water that adding more changes nothing. Hydration is always exothermic, because water molecules are attracted to the ions: the \(\delta-\) oxygen atoms point at cations, and the \(\delta+\) hydrogen atoms point at anions.

Dissolving can be done in two imaginary steps that lead to the same final state. First, take the lattice apart into gaseous ions. This is the reverse of the lattice-energy process, so it costs \(-\Delta H^{\ominus}_{\mathrm{latt}}\). Second, put the gaseous ions into water, which releases the hydration enthalpies of all the ions.

:::html
<figure class="fig small"><svg viewBox="0 0 345 200" role="img" aria-label="Energy cycle: solid sodium chloride goes up to gaseous ions with enthalpy change minus the lattice energy, the gaseous ions go down to aqueous ions with the enthalpy change of hydration, and the solid goes directly to aqueous ions with the enthalpy change of solution"><text class="tl tc" x="172" y="24">Na⁺(g) + Cl⁻(g)</text><text class="tl tc" x="50" y="176">NaCl(s)</text><text class="tl tc" x="282" y="176">Na⁺(aq) + Cl⁻(aq)</text><path class="ln" d="M56 156L128 44" marker-end="url(#ah)"/><text class="tl" x="78" y="108" text-anchor="end">−ΔHlatt</text><path class="ln" d="M214 44L276 152" marker-end="url(#ah)"/><text class="tl" x="258" y="100">ΔHhyd</text><path class="ln" d="M90 172H212" marker-end="url(#ah)"/><text class="tl tc" x="152" y="164">ΔHsol</text></svg><figcaption>The energy cycle for dissolving sodium chloride. The route through gaseous ions (up, then down) has the same enthalpy change as the direct route (along the bottom).</figcaption></figure>
:::

By Hess's law:

:::key Enthalpy change of solution
\[\Delta H^{\ominus}_{\mathrm{sol}} = -\Delta H^{\ominus}_{\mathrm{latt}} + \sum \Delta H^{\ominus}_{\mathrm{hyd}}\]
\(\sum \Delta H_{\mathrm{hyd}}\) is the hydration enthalpy of **every ion in the formula**: for \(\ce{MgCl2}\) it is one \(\ce{Mg^2+}\) and two \(\ce{Cl-}\). The lattice energy is negative, so \(-\Delta H_{\mathrm{latt}}\) is positive.
:::

:::eg (Exam style) Calculate the enthalpy change of solution of sodium chloride from these data (data for this question), in kJ mol⁻¹: ΔHlatt(NaCl) = −785; ΔHhyd(Na⁺) = −406; ΔHhyd(Cl⁻) = −364.
\[\Delta H^{\ominus}_{\mathrm{sol}} = -\Delta H^{\ominus}_{\mathrm{latt}} + \Delta H^{\ominus}_{\mathrm{hyd}}(\ce{Na+}) + \Delta H^{\ominus}_{\mathrm{hyd}}(\ce{Cl-})\] [M1]
\[\Delta H^{\ominus}_{\mathrm{sol}} = +785 - 406 - 364\] [M1]
\[\Delta H^{\ominus}_{\mathrm{sol}} = +15\ \mathrm{kJ\,mol^{-1}}\] [A1]
The answer is slightly endothermic. The measured value for sodium chloride is also a small positive number: it is the difference between two very large numbers (785 and 770), so a 1% error in either one produces a large change in the answer.
:::

### What decides the hydration enthalpy

The hydration enthalpy is larger (more exothermic) for ions with a **higher charge** and a **smaller radius**: the ratio of charge to size, the **charge density**, controls how strongly water molecules are attracted.

| Ion | Radius / nm | ΔHhyd / kJ mol⁻¹ |
|---|---|---|
| \(\ce{K+}\) | 0.133 | −322 |
| \(\ce{Na+}\) | 0.095 | −406 |
| \(\ce{Ca^2+}\) | 0.099 | −1650 |
| \(\ce{Mg^2+}\) | 0.065 | −1920 |
| \(\ce{Br-}\) | 0.195 | −335 |
| \(\ce{Cl-}\) | 0.181 | −364 |

Data for this chapter. Comparing \(\ce{Na+}\) and \(\ce{Mg^2+}\): the magnesium ion has twice the charge and a smaller radius, so water molecules are held much more strongly and the hydration enthalpy is about five times larger. Comparing \(\ce{Mg^2+}\) and \(\ce{Ca^2+}\): the same charge, but the smaller ion wins.

:::eg Explain why the hydration enthalpy of \(\ce{Mg^2+}\) is much more exothermic than that of \(\ce{Na+}\).
\(\ce{Mg^2+}\) has a charge of 2+ and \(\ce{Na+}\) has 1+. [B1]
\(\ce{Mg^2+}\) is also smaller, so it has a much higher charge density. [B1]
It attracts the \(\delta-\) oxygen atoms of water molecules more strongly, so more energy is released when the ion is hydrated. [B1]
:::

Whether a salt dissolves depends on how its lattice energy and hydration enthalpies change together. Down Group 2 this balance explains why the hydroxides become more soluble and the sulfates less soluble (see [Group 2](#chem.group2)). The enthalpy change of solution is only half of the story, though: some salts dissolve with a positive ΔHsol. For that you need entropy.

## Entropy

You know that a tidy room becomes untidy by itself but never the other way round. There are many more untidy arrangements than tidy ones, so untidiness is overwhelmingly more probable. Chemists give a name to this "number of ways":

:::def Entropy, S
A measure of the number of possible arrangements of the particles and their energy in a given system. The more ways the particles and their energy can be arranged, the higher the entropy.
:::

Entropy has units of J K⁻¹ mol⁻¹. Take care that this is **joules**, not kilojoules, per kelvin per mole. Standard entropies, \(S^{\ominus}\), are measured for one mole at 298 K and 101 kPa.

:::html
<figure class="fig small"><svg viewBox="0 0 345 152" role="img" aria-label="Particles in a solid, a liquid and a gas: a regular grid in the solid, a close random arrangement in the liquid and a few widely spaced particles in the gas"><path class="ln-m thin" d="M8 10H108V90H8Z"/><path class="ln-m thin" d="M123 10H223V90H123Z"/><path class="ln-m thin" d="M238 10H338V90H238Z"/><circle class="fa" cx="26" cy="24" r="5"/><circle class="fa" cx="26" cy="41" r="5"/><circle class="fa" cx="26" cy="58" r="5"/><circle class="fa" cx="26" cy="75" r="5"/><circle class="fa" cx="42" cy="24" r="5"/><circle class="fa" cx="42" cy="41" r="5"/><circle class="fa" cx="42" cy="58" r="5"/><circle class="fa" cx="42" cy="75" r="5"/><circle class="fa" cx="58" cy="24" r="5"/><circle class="fa" cx="58" cy="41" r="5"/><circle class="fa" cx="58" cy="58" r="5"/><circle class="fa" cx="58" cy="75" r="5"/><circle class="fa" cx="74" cy="24" r="5"/><circle class="fa" cx="74" cy="41" r="5"/><circle class="fa" cx="74" cy="58" r="5"/><circle class="fa" cx="74" cy="75" r="5"/><circle class="fa" cx="90" cy="24" r="5"/><circle class="fa" cx="90" cy="41" r="5"/><circle class="fa" cx="90" cy="58" r="5"/><circle class="fa" cx="90" cy="75" r="5"/><circle class="fa" cx="150" cy="53" r="5"/><circle class="fa" cx="162" cy="57" r="5"/><circle class="fa" cx="184" cy="21" r="5"/><circle class="fa" cx="131" cy="72" r="5"/><circle class="fa" cx="152" cy="32" r="5"/><circle class="fa" cx="216" cy="48" r="5"/><circle class="fa" cx="202" cy="48" r="5"/><circle class="fa" cx="185" cy="74" r="5"/><circle class="fa" cx="175" cy="66" r="5"/><circle class="fa" cx="156" cy="19" r="5"/><circle class="fa" cx="164" cy="70" r="5"/><circle class="fa" cx="206" cy="23" r="5"/><circle class="fa" cx="184" cy="37" r="5"/><circle class="fa" cx="174" cy="42" r="5"/><circle class="fa" cx="204" cy="82" r="5"/><circle class="fa" cx="165" cy="27" r="5"/><circle class="fa" cx="173" cy="83" r="5"/><circle class="fa" cx="157" cy="80" r="5"/><circle class="fa" cx="185" cy="56" r="5"/><circle class="fa" cx="132" cy="58" r="5"/><circle class="fa" cx="284" cy="54" r="5"/><circle class="fa" cx="324" cy="48" r="5"/><circle class="fa" cx="254" cy="37" r="5"/><circle class="fa" cx="254" cy="70" r="5"/><circle class="fa" cx="304" cy="21" r="5"/><circle class="fa" cx="329" cy="80" r="5"/><text class="tl tc" x="58" y="108">solid</text><text class="tl tc" x="173" y="108">liquid</text><text class="tl tc" x="288" y="108">gas</text><path class="ln" d="M24 124H322" marker-end="url(#ah)"/><text class="tl tc" x="172" y="144">more arrangements, so higher entropy</text></svg><figcaption>The same number of particles as a solid, a liquid and a gas. In the solid each particle has one fixed position, so there are very few arrangements. In the gas the particles can be almost anywhere and move freely, so there are very many.</figcaption></figure>
:::

### Predicting the sign of ΔS

The change in entropy is \(\Delta S = S_{\text{final}} - S_{\text{initial}}\). It is positive when the system gets more disordered. You can usually predict the sign without any numbers:

| Change | Sign of ΔS | Why |
|---|---|---|
| melting, boiling, sublimation | positive | particles gain freedom to move (a gas has far more arrangements than a liquid) |
| freezing, condensation | negative | the reverse: the particles become more ordered |
| dissolving a solid in a liquid | usually positive | the lattice breaks up and the ions move freely in the solution |
| raising the temperature | positive | more energy is available, and it can be shared among the particles in more ways |
| a reaction that makes more moles of gas | positive | gas particles have by far the most arrangements |
| a reaction that makes fewer moles of gas | negative | |

A change with the same number of gas moles on each side has a small ΔS, and the sign is harder to predict.

:::warn Entropy of elements, and dissolving
The enthalpy of formation of an element in its standard state is zero, but **the standard entropy of an element is not zero**: \(\ce{N2(g)}\) has \(S^{\ominus} = 191.6\ \mathrm{J\,K^{-1}\,mol^{-1}}\). Also, dissolving is "usually" positive: when the ions are small and highly charged they hold the water molecules around them in a rigid arrangement, so ΔS for such a dissolving can be negative. Dissolving a **gas** in a liquid always has a negative ΔS.
:::

:::eg Predict the sign of ΔS for each change, with a reason. (a) \(\ce{H2O(l) -> H2O(g)}\) (b) \(\ce{N2O4(g) -> 2NO2(g)}\) (c) \(\ce{2H2(g) + O2(g) -> 2H2O(l)}\) (d) \(\ce{NaCl(s) -> Na+(aq) + Cl-(aq)}\)
(a) Positive. A gas has far more arrangements than a liquid. [B1]
(b) Positive. One mole of gas becomes two moles of gas, so the number of gas particles doubles. [B1]
(c) Negative. Three moles of gas become liquid water. [B1]
(d) Positive. The ordered lattice breaks up and the ions are free to move in the solution. [B1]
:::

### Calculating ΔS for a reaction

Standard entropies are tabulated, and the entropy change is calculated in the same way as the enthalpy change of reaction from formation enthalpies, with the products first:

:::formula Entropy change of a reaction
\[\Delta S^{\ominus} = \sum S^{\ominus}(\text{products}) - \sum S^{\ominus}(\text{reactants})\]
Multiply each \(S^{\ominus}\) by its coefficient in the balanced equation. The unit is J K⁻¹ mol⁻¹.
:::

:::eg (Exam style) Calculate \(\Delta S^{\ominus}\) for the Haber process, \(\ce{N2(g) + 3H2(g) -> 2NH3(g)}\), using \(S^{\ominus}\) values (data for this question) in J K⁻¹ mol⁻¹: \(\ce{N2(g)}\) 191.6, \(\ce{H2(g)}\) 130.7, \(\ce{NH3(g)}\) 192.8. Comment on the sign.
\[\Delta S^{\ominus} = 2(192.8) - \left[191.6 + 3(130.7)\right]\] [M1]
\[\Delta S^{\ominus} = 385.6 - 583.7\] [M1]
\[\Delta S^{\ominus} = -198.1\ \mathrm{J\,K^{-1}\,mol^{-1}}\] [A1]
The sign is negative, as predicted: four moles of gas become two moles of gas, so the system becomes more ordered. [B1]
:::

## Gibbs free energy and feasibility

A reaction tends to happen if it releases energy (negative ΔH) **and** if it increases disorder (positive ΔS). These two tendencies can pull in opposite directions, and the Gibbs free energy change combines them in one number.

:::formula Gibbs free energy equation
\[\Delta G^{\ominus} = \Delta H^{\ominus} - T\,\Delta S^{\ominus}\]
\(\Delta G^{\ominus}\) is in kJ mol⁻¹, \(\Delta H^{\ominus}\) in kJ mol⁻¹, \(T\) is the temperature in **kelvin**, and \(\Delta S^{\ominus}\) must be in **kJ K⁻¹ mol⁻¹**: divide the value in J K⁻¹ mol⁻¹ by 1000.
:::

:::key Feasibility
A reaction is **feasible** (it can happen) when \(\Delta G\) is negative. When \(\Delta G\) is zero the reaction is just on the point of becoming feasible, and when \(\Delta G\) is positive it is not feasible at that temperature.
:::

:::eg (Exam style) Calculate \(\Delta G^{\ominus}\) at 298 K for \(\ce{N2(g) + 3H2(g) -> 2NH3(g)}\) given \(\Delta H^{\ominus} = -92.2\) kJ mol⁻¹ and \(\Delta S^{\ominus} = -198.1\) J K⁻¹ mol⁻¹. Is the reaction feasible?
Convert the entropy change to kJ: \(-198.1 / 1000 = -0.1981\) kJ K⁻¹ mol⁻¹. [M1]
\[\Delta G^{\ominus} = -92.2 - (298)(-0.1981)\] [M1]
\[\Delta G^{\ominus} = -92.2 + 59.03 = -33.2\ \mathrm{kJ\,mol^{-1}}\] [A1]
\(\Delta G^{\ominus}\) is negative, so the reaction is feasible at 298 K. [B1]
:::

### The effect of temperature

In \(\Delta H - T\Delta S\) the temperature multiplies only the entropy term, so the effect of temperature depends on the signs of \(\Delta H\) and \(\Delta S\):

| ΔH | ΔS | −TΔS | ΔG | Feasible? |
|---|---|---|---|---|
| negative | positive | negative | always negative | at **all** temperatures |
| negative | negative | positive, grows with T | negative only at low T | at **low** temperatures |
| positive | positive | negative, grows with T | negative only at high T | at **high** temperatures |
| positive | negative | positive | always positive | at **no** temperature |

The temperature at which the sign changes is where \(\Delta G = 0\), so \(\Delta H = T\Delta S\):

\[T = \frac{\Delta H}{\Delta S}\]

Use this for the minimum temperature of a reaction with positive ΔH and positive ΔS (or the maximum for negative ΔH and negative ΔS). Take care with the units: \(\Delta H\) in J mol⁻¹ and \(\Delta S\) in J K⁻¹ mol⁻¹, or both in kJ.

The graph of \(\Delta G\) against \(T\) is a straight line, because \(\Delta G = \Delta H - T\Delta S\) has the form \(y = c + mx\): the intercept (at \(T = 0\)) is \(\Delta H\) and the gradient is \(-\Delta S\). Thermal decomposition of calcium carbonate, \(\ce{CaCO3(s) -> CaO(s) + CO2(g)}\), with \(\Delta H^{\ominus} = +178\) kJ mol⁻¹ and \(\Delta S^{\ominus} = +160.6\) J K⁻¹ mol⁻¹ (worked out in the next example), shows the case with both positive.

:::plot Gibbs free energy change for the decomposition of calcium carbonate against temperature. The line crosses ΔG = 0 at 1108 K: below that temperature the reaction is not feasible, above it the reaction is feasible.
--f "178-0.1606*x" --label "ΔG = ΔH − TΔS" --x 0 1700 --y -120 260 --pt "1108,0,T = 1108 K@ne" --pt "298,130.1,ΔG = +130 kJ mol⁻¹ at 298 K@ne" --xlabel "T / K" --ylabel "ΔG / kJ mol⁻¹" --legend tr --xstep 500
:::

:::eg (Exam style) For \(\ce{CaCO3(s) -> CaO(s) + CO2(g)}\), \(\Delta H^{\ominus} = +178\) kJ mol⁻¹. Use \(S^{\ominus}\) values (data for this question) in J K⁻¹ mol⁻¹: \(\ce{CaCO3}\) 92.9, \(\ce{CaO}\) 39.7, \(\ce{CO2}\) 213.8. Calculate the minimum temperature at which the decomposition is feasible, and say why it is not feasible at room temperature.
\[\Delta S^{\ominus} = (39.7 + 213.8) - 92.9 = +160.6\ \mathrm{J\,K^{-1}\,mol^{-1}}\] [M1]
At the minimum temperature \(\Delta G = 0\), so \(T = \Delta H / \Delta S\) with both in joules: [M1]
\[T = \frac{178\,000}{160.6} = 1108\ \mathrm{K}\] [A1]
At 298 K, \(\Delta G = 178 - 298(0.1606) = +130\) kJ mol⁻¹. It is positive: the entropy increase is too small, at this temperature, to outweigh the large positive \(\Delta H\). [B1]
:::

:::eg (Real context) Instant cold packs contain solid ammonium nitrate and a bag of water. When the bag is broken, the nitrate dissolves, and the pack becomes cold. For \(\ce{NH4NO3}\), \(\Delta H_{\mathrm{sol}} = +26\) kJ mol⁻¹ and \(\Delta S = +108\) J K⁻¹ mol⁻¹ (data for this question). Show that dissolving is feasible at 298 K.
Dissolving takes in heat from the surroundings (\(\Delta H\) positive), which is why the pack feels cold. [B1]
\[\Delta G = +26 - 298\left(\tfrac{108}{1000}\right) = 26 - 32.18\] [M1]
\[\Delta G = -6.2\ \mathrm{kJ\,mol^{-1}}\] [A1]
\(\Delta G\) is negative, so dissolving is feasible, even though it is endothermic, because the entropy gain when the solid lattice breaks up is large enough. [B1]
:::

### Feasible does not mean fast

A negative \(\Delta G\) tells you that a reaction **can** happen. It tells you nothing about how fast. A mixture of hydrogen and oxygen at room temperature has a large negative \(\Delta G\) for forming water, yet it can sit for years: the activation energy is so high that almost no collisions have enough energy. A spark, or a platinum catalyst, starts the reaction at once. Likewise diamond is, strictly, less stable than graphite at room temperature, but it never changes in your lifetime, because breaking its bonds has a huge activation energy. A reaction that is feasible but extremely slow is called **kinetically stable**.

:::warn Two opposite mistakes
"\(\Delta G\) is negative, so the reaction is fast" is wrong: \(\Delta G\) says nothing about the rate. "The reaction does not happen, so it is not feasible" is also wrong: it may simply be too slow. Also, calculations of \(\Delta G\) assume that \(\Delta H\) and \(\Delta S\) stay the same at different temperatures, which is a good approximation for the exam but not exact in reality.
:::

:::eg Spot the error: Calculate \(\Delta G^{\ominus}\) at 1500 K for \(\ce{CaCO3(s) -> CaO(s) + CO2(g)}\) (\(\Delta H^{\ominus} = +178\) kJ mol⁻¹, \(\Delta S^{\ominus} = +161\) J K⁻¹ mol⁻¹) and say whether it is feasible. [4 marks]
A student wrote this answer.

Line 1: \(\Delta G = \Delta H - T\Delta S\)
Line 2: \(\Delta G = 178 - (1500 \times 161) = -241\,322\) kJ mol⁻¹
Line 3: \(\Delta G\) is negative so the reaction is feasible.

Line 1 is correct [B1]. **Line 2 is wrong: \(\Delta S\) is in J K⁻¹ mol⁻¹ but \(\Delta H\) is in kJ mol⁻¹. The entropy must be divided by 1000 before it is used, and the working and the answer both lose the mark [M0] [A0].** Line 3 reaches the right conclusion from the sign [B1], but only by luck, because the wrong number is still negative.

Correct line 2: \(\Delta G = 178 - 1500 \times 0.161 = -63.5\) kJ mol⁻¹. [M1] [A1]

The student scores 2 out of 4. Always convert J to kJ (or kJ to J) before combining \(\Delta H\) and \(T\Delta S\); a feasibility check at a temperature where the answer is positive would have exposed the mistake.
:::

:::try Start easy, finish at exam standard
Q: Write the equation, with state symbols, for (a) the first electron affinity of bromine and (b) the lattice energy of calcium oxide.
A: (a) \(\ce{Br(g) + e- -> Br-(g)}\) (b) \(\ce{Ca^2+(g) + O^2-(g) -> CaO(s)}\)
Q: Explain why the first electron affinity of sulfur is more exothermic than that of oxygen, although oxygen has the smaller radius.
A: The oxygen atom is so small that the electrons already in its 2p sub-shell repel an incoming electron strongly, which cancels some of the attraction of the nucleus. In the larger sulfur atom, the 3p sub-shell is bigger and the repulsion is weaker, so more energy is released.
Q: Calculate the lattice energy of sodium fluoride from these data (data for this question), in kJ mol⁻¹: ΔHf(NaF) = −574; ΔHat(Na) = +107; IE₁(Na) = +494; ΔHat(F) = +79; EA₁(F) = −328.
A: \(\Delta H_{\mathrm{latt}} = -574 - (107 + 494 + 79 - 328) = -574 - 352 = -926\) kJ mol⁻¹.
Q: Calculate the enthalpy change of formation of calcium oxide from these data (data for this question), in kJ mol⁻¹: ΔHat(Ca) = +178; IE₁(Ca) = +590; IE₂(Ca) = +1150; ΔHat(O) = +249; EA₁(O) = −141; EA₂(O) = +798; ΔHlatt(CaO) = −3459.
A: \[\Delta H_{\mathrm{f}} = 178 + 590 + 1150 + 249 - 141 + 798 - 3459 = -635\ \mathrm{kJ\,mol^{-1}}\]
Q: Calculate the enthalpy change of solution of magnesium chloride from these data, in kJ mol⁻¹: ΔHlatt(MgCl₂) = −2521; ΔHhyd(Mg²⁺) = −1920; ΔHhyd(Cl⁻) = −364.
A: \(\Delta H_{\mathrm{sol}} = +2521 - 1920 + 2(-364) = -127\) kJ mol⁻¹. There are two chloride ions in the formula.
Q: Predict the sign of ΔS for (a) \(\ce{CaCO3(s) -> CaO(s) + CO2(g)}\), (b) \(\ce{CO2(g) -> CO2(s)}\) and (c) the temperature of a block of copper rising from 300 K to 400 K.
A: (a) positive: a gas forms from solids. (b) negative: a gas becomes a solid. (c) positive: more energy states are available, so more arrangements.
Q: A reaction has ΔH = −120 kJ mol⁻¹ and ΔS = −250 J K⁻¹ mol⁻¹. Calculate the temperature above which it stops being feasible.
A: \(T = \Delta H / \Delta S = -120\,000 / -250 = 480\) K. Below 480 K, ΔG is negative; above it, ΔG is positive.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Write equations, with state symbols, for the first and second electron affinities of oxygen, and explain why the second is endothermic.
A: \(\ce{O(g) + e- -> O-(g)}\) [B1] \(\ce{O-(g) + e- -> O^2-(g)}\) [B1]
The second electron is added to an ion that is already negative, so electrostatic repulsion has to be overcome. [B1]
Q: [4 marks] ★★ Calculate the lattice energy of potassium fluoride from these data (data for this question), in kJ mol⁻¹: ΔHf(KF) = −568; ΔHat(K) = +89; IE₁(K) = +418; EA₁(F) = −328. The bond energy of F–F is 158 kJ mol⁻¹ (Data section).
H: Atomisation of fluorine is per mole of F atoms, so use half the bond energy.
A: \(\Delta H_{\mathrm{at}}(\ce{F}) = \tfrac12 \times 158 = +79\) kJ mol⁻¹. [B1]
\[\Delta H_{\mathrm{latt}} = \Delta H_{\mathrm{f}} - \left(\Delta H_{\mathrm{at}}(\ce{K}) + \Delta H_{\mathrm{at}}(\ce{F}) + \mathrm{IE}_1 + \mathrm{EA}_1\right)\] [M1]
\(= -568 - (89 + 79 + 418 - 328) = -568 - 258\) [M1]
\(= -826\) kJ mol⁻¹ [A1]
Q: [4 marks] ★★ Calculate the enthalpy change of formation of barium oxide, using these data (data for this question), in kJ mol⁻¹: ΔHat(Ba) = +180; IE₁(Ba) = +502 and IE₂(Ba) = +966 (both from the Data section); ΔHat(O) = +249; EA₁(O) = −141; EA₂(O) = +798; ΔHlatt(BaO) = −3102.
H: Use both ionisation energies of barium and both electron affinities of oxygen.
A: Both IEs of Ba and both EAs of O included. [M1]
\[\Delta H_{\mathrm{f}} = 180 + 502 + 966 + 249 - 141 + 798 - 3102\] [M1]
\(= 2554 - 3102\) [M1]
\(= -548\) kJ mol⁻¹ [A1]
Q: [3 marks] ★★ Explain why the lattice energy of magnesium oxide (−3842 kJ mol⁻¹) is more exothermic than that of calcium oxide (−3459 kJ mol⁻¹).
A: The ions have the same charges (2+ and 2−) in both compounds. [B1]
\(\ce{Mg^2+}\) is smaller than \(\ce{Ca^2+}\), because it has one fewer electron shell, so the distance between the ion centres is smaller in MgO. [B1]
The electrostatic attraction between the ions is therefore stronger and more energy is released when the lattice forms. [B1]
Q: [4 marks] ★★ The lattice energy of potassium bromide is −679 kJ mol⁻¹, and the hydration enthalpies are −322 kJ mol⁻¹ for \(\ce{K+}\) and −335 kJ mol⁻¹ for \(\ce{Br-}\). (a) Calculate the enthalpy change of solution of potassium bromide. (b) Explain why potassium bromide dissolves in water although the process is endothermic.
A: (a) \(\Delta H_{\mathrm{sol}} = -\Delta H_{\mathrm{latt}} + \Delta H_{\mathrm{hyd}}(\ce{K+}) + \Delta H_{\mathrm{hyd}}(\ce{Br-})\) [M1]
\(= +679 - 322 - 335 = +22\) kJ mol⁻¹ [M1] [A1]
(b) The entropy increases when the solid lattice breaks up and the ions move freely in solution, so \(T\Delta S\) is larger than \(\Delta H\) and \(\Delta G\) is negative. [B1]
Q: [4 marks] ★★ Calculate \(\Delta S^{\ominus}\) for \(\ce{CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)}\) using \(S^{\ominus}\) values (data for this question) in J K⁻¹ mol⁻¹: \(\ce{CH4(g)}\) 186.3; \(\ce{O2(g)}\) 205.0; \(\ce{CO2(g)}\) 213.8; \(\ce{H2O(l)}\) 69.9. Explain the sign of your answer.
A: \[\Delta S^{\ominus} = \left[213.8 + 2(69.9)\right] - \left[186.3 + 2(205.0)\right]\] [M1]
\(= 353.6 - 596.3\) [M1]
\(= -242.7\) J K⁻¹ mol⁻¹ [A1]
Negative: three moles of gas become one mole of gas and two moles of liquid, so the number of arrangements falls. [B1]
Q: [6 marks] ★★★ Magnesium carbonate decomposes: \(\ce{MgCO3(s) -> MgO(s) + CO2(g)}\), \(\Delta H^{\ominus} = +117\) kJ mol⁻¹. \(S^{\ominus}\) values (data for this question) in J K⁻¹ mol⁻¹: \(\ce{MgCO3}\) 65.7, \(\ce{MgO}\) 26.9, \(\ce{CO2}\) 213.8. (a) Calculate \(\Delta S^{\ominus}\). (b) Calculate the minimum temperature at which the decomposition is feasible. (c) Explain why the decomposition is feasible only above this temperature.
H: At the minimum temperature, \(\Delta G = 0\).
H: Convert \(\Delta H\) to joules before dividing.
A: (a) \(\Delta S^{\ominus} = (26.9 + 213.8) - 65.7\) [M1] \(= +175.0\) J K⁻¹ mol⁻¹ [A1]
(b) \(\Delta G = 0\), so \(T = \Delta H / \Delta S\). [M1] Converting: \(T = 117\,000 / 175.0\) [M1] \(= 669\) K [A1]
(c) \(\Delta S\) is positive (a gas is formed), so \(-T\Delta S\) becomes more negative as \(T\) rises; above 669 K it outweighs the positive \(\Delta H\) and \(\Delta G\) is negative. [B1]
Q: [6 marks] ★★★ Sodium oxide, \(\ce{Na2O}\), contains \(\ce{Na+}\) and \(\ce{O^2-}\) ions. (a) Calculate the lattice energy of \(\ce{Na2O}\) from these data (data for this question), in kJ mol⁻¹: ΔHf(Na₂O) = −414; ΔHat(Na) = +107; IE₁(Na) = +494; ΔHat(O) = +249; EA₁(O) = −141; EA₂(O) = +798. (b) Explain why the lattice energy of \(\ce{Na2O}\) is much more exothermic than that of \(\ce{NaCl}\) (−785 kJ mol⁻¹).
H: The formula has two sodium atoms and one oxygen atom.
A: (a) Two sodium atoms are atomised and two are ionised: the sodium terms are doubled. [M1]
Both electron affinities of oxygen are used, with EA₂ positive. [M1]
\[\Delta H_{\mathrm{latt}} = -414 - \left[2(107) + 2(494) + 249 - 141 + 798\right] = -414 - 2108\] [M1]
\(= -2522\) kJ mol⁻¹ [A1]
(b) The oxide ion has a charge of 2− and the chloride ion has 1−, so the attraction to the sodium ions is stronger. [B1]
The oxide ion is also smaller than the chloride ion (one fewer shell), so the ions are closer together. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A student asks why magnesium forms \(\ce{MgCl2}\) and not \(\ce{MgCl}\). Use these data (data for this question), in kJ mol⁻¹: ΔHat(Mg) = +148; IE₁(Mg) = +736; ΔHat(Cl) = +122; EA₁(Cl) = −349; ΔHlatt(MgCl) = −753 (a hypothetical lattice with one \(\ce{Mg+}\) and one \(\ce{Cl-}\)); ΔHf(MgCl₂) = −641. (a) Calculate ΔHf of the hypothetical \(\ce{MgCl}\). (b) Calculate the enthalpy change of the reaction \(\ce{2MgCl(s) -> Mg(s) + MgCl2(s)}\). (c) What does your answer show?
H: A formation enthalpy for 2 mol of MgCl is twice the value for 1 mol.
H: Write the reaction as products minus reactants, using formation enthalpies. Elements have ΔHf = 0.
A: (a) \(\Delta H_{\mathrm{f}}(\ce{MgCl}) = 148 + 736 + 122 - 349 - 753\) [M1] \(= -96\) kJ mol⁻¹ [A1]
So \(\ce{MgCl}\) would be exothermic to form from its elements. (b) \(\Delta H = \Delta H_{\mathrm{f}}(\ce{MgCl2}) - 2\Delta H_{\mathrm{f}}(\ce{MgCl})\) [M1] \(= -641 - 2(-96) = -449\) kJ mol⁻¹ [A1]
(c) The disproportionation of \(\ce{MgCl}\) is strongly exothermic, so MgCl would break down to Mg and \(\ce{MgCl2}\). [B1]
The extra energy needed for the second ionisation energy of magnesium (+1450) is more than repaid by the much larger lattice energy of \(\ce{MgCl2}\) (−2521), which has \(\ce{Mg^2+}\) ions. [B1]
Q: [4 marks] ★★★ Ammonium chloride decomposes on heating: \(\ce{NH4Cl(s) -> NH3(g) + HCl(g)}\), \(\Delta H^{\ominus} = +176\) kJ mol⁻¹ and \(\Delta S^{\ominus} = +285\) J K⁻¹ mol⁻¹ (data for this question). (a) Calculate the temperature above which the decomposition is feasible. (b) A student heats ammonium chloride in a test tube and sees a white solid forming on the cooler glass near the top. Explain this.
H: For the reverse reaction, ΔH and ΔS both change sign.
A: (a) \(T = 176\,000 / 285\) [M1] \(= 618\) K [A1]
(b) The gases ammonia and hydrogen chloride leave the hot region, where the decomposition is feasible. [B1] Near the top the glass is below 618 K, where the reverse reaction has a negative ΔG, so the two gases combine and form white solid ammonium chloride again. [B1]
:::

:::quiz
? Which equation represents the lattice energy of sodium chloride in this syllabus?
- \(\ce{NaCl(s) -> Na+(g) + Cl-(g)}\)
+ \(\ce{Na+(g) + Cl-(g) -> NaCl(s)}\)
- \(\ce{Na(s) + 1/2Cl2(g) -> NaCl(s)}\)
- \(\ce{Na+(g) + Cl-(aq) -> NaCl(s)}\)
> The lattice energy is for one mole of the compound formed from its gaseous ions, so it is exothermic. The first option is the reverse process; the third is the enthalpy of formation.
? Why is the second electron affinity of oxygen endothermic?
- Oxygen has a high electronegativity.
+ The \(\ce{O-}\) ion repels the incoming electron.
- The \(\ce{O^2-}\) ion is larger than the \(\ce{O-}\) ion.
- The electron enters a new shell.
> Adding an electron to a negative ion needs energy to overcome repulsion. The energy is later repaid by the lattice energy.
? For which compound is the lattice energy most exothermic?
- NaCl
- KBr
- NaF
+ MgO
> MgO has the highest charges (2+ and 2−) and small ions. The charge matters far more than the size, so even the small ions of NaF give a much less exothermic lattice energy.
? Calculate the enthalpy change of solution of MgCl₂ when ΔHlatt = −2521, ΔHhyd(Mg²⁺) = −1920 and ΔHhyd(Cl⁻) = −364 (all kJ mol⁻¹).
- +237
- +127
- −5169
+ −127
> There are two chloride ions per formula unit: +2521 − 1920 − 2(364) = −127 kJ mol⁻¹. Forgetting the factor 2 gives +237, and using the lattice energy with the wrong sign gives −5169.
? A reaction has ΔH positive and ΔS positive. When is it feasible?
- never
- at all temperatures
- only at low temperatures
+ only at high temperatures
> ΔG = ΔH − TΔS. The negative term −TΔS grows with temperature, and once it outweighs ΔH the value of ΔG becomes negative.
? What is the error in "ΔG is very negative, so this reaction is fast"?
- None: ΔG measures the rate.
+ ΔG says only whether the reaction is feasible; the rate depends on the activation energy.
- A negative ΔG means the reaction is endothermic.
- ΔG applies only to gases.
> A feasible reaction can be very slow (kinetically stable) if its activation energy is high.
:::

:::checklist What you can now do
- [ ] I can define enthalpy change of atomisation, first electron affinity and lattice energy, with equations and state symbols.
- [ ] I can explain the factors affecting electron affinity and the trend and exceptions in Groups 16 and 17.
- [ ] I can construct a Born–Haber cycle for a compound with 1+ or 2+ cations and 1− or 2− anions.
- [ ] I can use a Born–Haber cycle to calculate a lattice energy or any other unknown term.
- [ ] I can explain how ionic charge and radius affect the size of the lattice energy.
- [ ] I can define enthalpy change of hydration and of solution, and calculate ΔHsol from ΔHlatt and ΔHhyd.
- [ ] I can explain the effect of ionic charge and radius on the hydration enthalpy.
- [ ] I can define entropy and predict the sign of ΔS for changes of state, dissolving, temperature changes and reactions that change the number of moles of gas.
- [ ] I can calculate ΔS⦵ from standard entropies and ΔG⦵ from ΔH⦵ and ΔS⦵, converting units correctly.
- [ ] I can decide whether a reaction is feasible and find the temperature at which feasibility changes.
:::

:::recap
- Ionic compounds are stable because the lattice energy (very exothermic) repays the energy cost of making the ions. Lattice energy is for gaseous ions forming the solid: negative.
- \(\Delta H_{\mathrm{at}}\) is per mole of gaseous atoms formed (half the bond energy for diatomic elements). EA₁ is exothermic for most non-metals, less so down a group (F and O are exceptions); EA₂ of oxygen is endothermic.
- Born–Haber: \(\Delta H_{\mathrm{f}} = \sum\Delta H_{\mathrm{at}} + \sum\mathrm{IE} + \sum\mathrm{EA} + \Delta H_{\mathrm{latt}}\), for one mole of compound. Count the atoms and use every IE and EA.
- Lattice energy is larger for higher ionic charges and smaller ions: MgO ≫ NaCl.
- \(\Delta H_{\mathrm{sol}} = -\Delta H_{\mathrm{latt}} + \sum\Delta H_{\mathrm{hyd}}\). Hydration is more exothermic for ions with higher charge and smaller radius.
- Entropy S counts the arrangements of the particles and their energy. ΔS is positive for melting, boiling, dissolving a solid, a temperature rise and a reaction that makes more gas.
- \(\Delta S^{\ominus} = \sum S(\text{products}) - \sum S(\text{reactants})\) in J K⁻¹ mol⁻¹. Elements have non-zero S.
- \(\Delta G = \Delta H - T\Delta S\) (divide ΔS by 1000). Feasible if ΔG is negative. The crossover temperature is \(T = \Delta H / \Delta S\). Feasible does not mean fast.
:::

:::links
- read: [Lattice enthalpy (lattice energy)](https://www.chemguide.co.uk/physical/energetics/lattice.html) · Chemguide · Born–Haber cycles and the effect of ion size and charge, step by step
- read: [Enthalpies of solution and hydration](https://www.chemguide.co.uk/physical/energetics/solution.html) · Chemguide · the energy cycle for dissolving and how ion size and charge change the numbers
- read: [Entropy and free energy menu](https://www.chemguide.co.uk/physical/entropymenu.html) · Chemguide · entropy changes, ΔG and feasibility from first principles
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Electrochemistry: electrolysis and electrode potentials](#chem.electrochem) uses ΔG in a new way: the energy that a cell can deliver as electrical work.
