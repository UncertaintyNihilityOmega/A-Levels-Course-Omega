@chapter chem.energetics
@title Chemical energetics
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 7–9 hours
@summary How chemists measure and calculate the energy change of a reaction. You will learn exothermic and endothermic reactions and reaction pathway diagrams, the standard enthalpy changes, calorimetry with q = mcΔT, bond energy calculations and Hess's law with energy cycles.

:::why
Every reaction either gives out energy or takes it in. That energy heats homes and cooks food, drives a car engine, warms a hand-warmer, and in the body is the reason sugar is a useful fuel. Chemists need to predict how much energy a reaction releases, and to do so for reactions they cannot easily measure, such as burning carbon to carbon monoxide. This chapter gives you the tools: a calorimeter and one equation for measuring it, a list of bond energies for estimating it, and Hess's law for calculating it.
:::

**Before you start**, you should know how to calculate amounts in moles from [Moles and stoichiometry](#chem.moles) and what a covalent bond and its bond energy are from [Chemical bonding](#chem.bonding).

:::try Warm-up
Q: Calculate the amount of sodium hydroxide in 2.00 g of NaOH. (from [Moles and stoichiometry](#chem.moles))
A: \(M_r = 23.0 + 16.0 + 1.0 = 40.0\), so \(n = 2.00 / 40.0 = 0.0500\) mol.
Q: How many moles of HCl are in 50.0 cm³ of hydrochloric acid of concentration 1.00 mol dm⁻³? (from [Moles and stoichiometry](#chem.moles))
A: \(n = cV = 1.00 \times 50.0 / 1000 = 0.0500\) mol.
Q: Define bond energy. (from [Chemical bonding](#chem.bonding))
A: The energy required to break one mole of a particular covalent bond in the gaseous state.
:::

## Energy changes in reactions

### System, surroundings and enthalpy change

In a chemical reaction, bonds in the reactants break and new bonds form in the products. These two processes involve different amounts of energy, and the difference leaves the reacting chemicals (the **system**) as heat to the **surroundings** (the solution, the container, the air), or enters the system from them. You usually detect the change by a change in the temperature of the surroundings.

The heat change of a reaction at constant pressure has its own name and symbol.

:::def Enthalpy change, ΔH
The heat energy change of a reaction measured at constant pressure. \(\Delta H = H(\text{products}) - H(\text{reactants})\). It is given in kJ mol⁻¹ and carries a sign.
:::

The sign shows which way the energy goes, as seen by the chemicals.

| | Exothermic | Endothermic |
|---|---|---|
| Energy flow | released to the surroundings | taken in from the surroundings |
| Temperature of the surroundings | rises | falls |
| Enthalpy of the products compared with the reactants | lower | higher |
| Sign of \(\Delta H\) | **negative** | **positive** |
| Examples | combustion, neutralisation, respiration, rusting | thermal decomposition of calcium carbonate, photosynthesis, dissolving ammonium nitrate |

:::analogy
Think of the chemicals as a bank account and the sign of ΔH as the change in the balance. An exothermic reaction is a withdrawal from the account: the chemicals lose energy, so ΔH is negative, and the surroundings (the pocket) gain it and get warmer. An endothermic reaction is a deposit: the chemicals gain energy and ΔH is positive, and the surroundings lose energy and get colder.
:::

:::eg (Real context) Disposable hand-warmers contain iron powder that reacts slowly with oxygen from the air: \(\ce{4Fe + 3O2 -> 2Fe2O3}\). Instant cold packs contain ammonium nitrate that dissolves in water. Say which is exothermic and which is endothermic, and give the sign of ΔH for each.
The hand-warmer gets warm, so energy is released to the surroundings: the reaction is exothermic and ΔH is negative. [B1]
The cold pack gets cold as the ammonium nitrate dissolves, so energy is taken in from the surroundings: dissolving is endothermic and ΔH is positive. [B1]
:::

### Reaction pathway diagrams

A **reaction pathway diagram** plots the enthalpy of the chemicals against the progress of the reaction. Reactants do not turn into products straight away: bonds must start to break first, which needs energy, so the line climbs to a peak before falling to the products. The height of the peak above the reactants is the activation energy.

:::def Activation energy, Eₐ
The minimum energy that colliding particles must have for a reaction to occur. On a pathway diagram it is the energy difference between the reactants and the top of the peak (the transition state).
:::

:::cols
:::col Exothermic: ΔH negative
:::html
<figure class="fig small"><svg viewBox="0 8 300 228" role="img" aria-label="Reaction pathway diagram for an exothermic reaction: the products are lower than the reactants, the activation energy is marked from the reactants up to the peak and the enthalpy change is marked downwards from the reactants to the products"><path class="ax" d="M20 205V32" marker-end="url(#ahm)"/><path class="ax" d="M20 205H290" marker-end="url(#ahm)"/><text class="tl" x="28" y="24">enthalpy</text><text class="tl" x="290" y="227" text-anchor="end">progress of reaction</text><path class="ln thick" d="M60 105H115"/><path class="ln thick" d="M195 155H245"/><path class="c1 sw2" d="M115 105C137 105 133 48 155 48C177 48 173 155 195 155"/><path class="ln-m thin dash" d="M115 105H275"/><path class="ln-m thin dash" d="M245 155H275"/><path class="c2 sw2" d="M267 130V108" marker-end="url(#ah)"/><path class="c2 sw2" d="M267 130V152" marker-end="url(#ah)"/><text class="tl" x="276" y="134">ΔH</text><path class="ln-m thin dash" d="M42 48H151"/><path class="ln-m thin dash" d="M42 105H60"/><path class="c2 sw2" d="M42 77V51" marker-end="url(#ah)"/><path class="c2 sw2" d="M42 77V102" marker-end="url(#ah)"/><text class="tl tc" x="88" y="95">reactants</text><text class="tl tc" x="220" y="175">products</text><text class="tl" x="50" y="66">Eₐ</text></svg><figcaption>Exothermic: the products have lower enthalpy than the reactants, so ΔH is negative.</figcaption></figure>
:::
:::
:::col Endothermic: ΔH positive
:::html
<figure class="fig small"><svg viewBox="0 8 300 228" role="img" aria-label="Reaction pathway diagram for an endothermic reaction: the products are higher than the reactants, the activation energy is marked from the reactants up to the peak and the enthalpy change is marked upwards from the reactants to the products"><path class="ax" d="M20 205V32" marker-end="url(#ahm)"/><path class="ax" d="M20 205H290" marker-end="url(#ahm)"/><text class="tl" x="28" y="24">enthalpy</text><text class="tl" x="290" y="227" text-anchor="end">progress of reaction</text><path class="ln thick" d="M60 155H115"/><path class="ln thick" d="M195 105H245"/><path class="c1 sw2" d="M115 155C137 155 133 48 155 48C177 48 173 105 195 105"/><path class="ln-m thin dash" d="M115 155H275"/><path class="ln-m thin dash" d="M245 105H275"/><path class="c2 sw2" d="M267 130V152" marker-end="url(#ah)"/><path class="c2 sw2" d="M267 130V108" marker-end="url(#ah)"/><text class="tl" x="276" y="134">ΔH</text><path class="ln-m thin dash" d="M42 48H151"/><path class="ln-m thin dash" d="M42 155H60"/><path class="c2 sw2" d="M42 102V51" marker-end="url(#ah)"/><path class="c2 sw2" d="M42 102V152" marker-end="url(#ah)"/><text class="tl tc" x="88" y="175">reactants</text><text class="tl tc" x="220" y="95">products</text><text class="tl" x="50" y="106">Eₐ</text></svg><figcaption>Endothermic: the products have higher enthalpy than the reactants, so ΔH is positive.</figcaption></figure>
:::
:::
:::

In both diagrams Eₐ is measured from the reactants up to the peak, and ΔH from the reactants to the products.

Notice that Eₐ is the same kind of quantity in both diagrams (a climb from the reactants to the peak), while ΔH depends only on where the reactants and products stand. A reaction can be strongly exothermic and still need a big Eₐ: petrol burns with a large release of energy, but only after a spark. A catalyst gives the reaction an alternative route with a lower peak, as you will see in [Reaction kinetics](#chem.kinetics). It changes Eₐ but never ΔH.

Use the widget below to see how the diagram changes. Move ΔH to positive and negative values, change Eₐ, and tick the catalyst box.

:::html
<div class="widget" data-w="chem-profile" data-dh="-90" data-ea="120"></div>
:::

:::warn Two different energies
Do not confuse the two arrows. **ΔH** is the overall energy change between reactants and products (the sign matters). **Eₐ** is the energy barrier on the way (always positive). A reaction with a small Eₐ goes fast; a reaction with a large negative ΔH is very exothermic. The two are independent.
:::

## Standard enthalpy changes

Enthalpy changes depend on temperature, pressure and the physical state of every substance, so chemists compare them under agreed conditions.

:::def Standard conditions
A pressure of 101 kPa, a stated temperature, usually 298 K, and (for solutions) a concentration of 1.00 mol dm⁻³. The standard sign \(\ominus\) is added to the symbol, for example \(\Delta H^{\ominus}\). A **standard state** is the physical state of a substance under standard conditions: oxygen is \(\ce{O2(g)}\), mercury is Hg(l) and carbon is graphite.
:::

Four named enthalpy changes are defined in the syllabus. Each definition has the same parts: **one mole** of the named thing, and **standard conditions**.

:::def Standard enthalpy change of reaction, \(\Delta H^{\ominus}_{\mathrm{r}}\)
The enthalpy change when the amounts of reactants shown in the equation react to give products, all under standard conditions.
:::

:::def Standard enthalpy change of formation, \(\Delta H^{\ominus}_{\mathrm{f}}\)
The enthalpy change when one mole of a compound is formed from its elements in their standard states under standard conditions.
:::

:::def Standard enthalpy change of combustion, \(\Delta H^{\ominus}_{\mathrm{c}}\)
The enthalpy change when one mole of a substance is burnt completely in oxygen under standard conditions.
:::

:::def Standard enthalpy change of neutralisation, \(\Delta H^{\ominus}_{\mathrm{neut}}\)
The enthalpy change when one mole of water is formed by the reaction of an acid with an alkali under standard conditions.
:::

Each one has an equation that you must be able to write.

| Enthalpy change | Example equation | Notes |
|---|---|---|
| formation of methane | \(\ce{C(s) + 2H2(g) -> CH4(g)}\) | elements as reactants, standard states, 1 mol of product |
| formation of sodium chloride | \(\ce{Na(s) + 1/2Cl2(g) -> NaCl(s)}\) | half a mole of \(\ce{Cl2}\) is allowed so that exactly 1 mol of NaCl forms |
| combustion of ethanol | \(\ce{C2H5OH(l) + 3O2(g) -> 2CO2(g) + 3H2O(l)}\) | 1 mol burnt; products are \(\ce{CO2(g)}\) and \(\ce{H2O(l)}\) |
| neutralisation | \(\ce{H+(aq) + OH-(aq) -> H2O(l)}\) | exactly 1 mol of water forms |

The neutralisation of a strong acid by a strong alkali is close to \(-57\) kJ mol⁻¹ whichever acid and alkali you use, because the reaction is always \(\ce{H+ + OH- -> H2O}\). With a weak acid the value is different, because some energy is spent on ionising the acid.

:::warn Four traps in the definitions
(1) \(\Delta H^{\ominus}_{\mathrm{f}}\) of an **element** in its standard state is zero, because nothing is formed. (2) In a formation equation the reactants are only elements, in their standard states, with fractions if needed to give 1 mol of product. (3) In a combustion equation the water formed is liquid, \(\ce{H2O(l)}\); if the water is a gas the enthalpy change is not the standard enthalpy change of combustion. (4) \(\Delta H^{\ominus}_{\mathrm{r}}\) is for the equation **as written**: double the equation and the value doubles.
:::

## Measuring enthalpy changes: calorimetry

### The equation

You cannot measure enthalpy changes directly, but you can measure the temperature change of a known mass of water or solution, and work out the heat energy transferred to or from it.

:::formula Heat energy transferred
\[q = mc\Delta T\]
\(q\) = heat energy transferred in J, \(m\) = mass of water or solution being heated or cooled in g, \(c\) = specific heat capacity, 4.18 J g⁻¹ K⁻¹ for water and dilute solutions, \(\Delta T = T_{\text{final}} - T_{\text{initial}}\) in K.
:::

Then convert to the enthalpy change **per mole** of the reactant that is used up completely (the limiting reactant):

:::formula Enthalpy change from an experiment
\[\Delta H = -\frac{mc\Delta T}{n}\]
Divide by 1000 to give kJ mol⁻¹. \(n\) = amount in mol of the limiting reactant (or the substance in the definition, such as the water formed). The minus sign appears because the energy gained by the solution is lost by the reaction.
:::

The temperature **rise** of the solution (ΔT positive) means the reaction released energy, so ΔH is negative. A temperature fall (ΔT negative) gives a positive ΔH.

A change of 1 K equals a change of 1 °C, so you can use the temperature change in °C directly.

### Neutralisation and displacement in a cup

:::lab Enthalpy change of neutralisation in a polystyrene cup
Use a pipette or measuring cylinder to put 25.0 cm³ of 1.00 mol dm⁻³ hydrochloric acid in a polystyrene cup standing in a beaker (this insulates it). Record the temperature every 30 seconds for 3 minutes. At the fourth minute add 25.0 cm³ of 1.00 mol dm⁻³ sodium hydroxide solution, stir with the thermometer and carry on recording the temperature every 30 seconds for several minutes. Plot a graph of temperature against time. Wear eye protection: both solutions are corrosive.
:::

The temperature climbs quickly when you mix the solutions and then falls slowly as the cup loses heat to the room. If you read the highest temperature, you underestimate the rise, because some heat was already lost. The better method is to extend the cooling line backwards to the time of mixing.

:::html
<figure class="fig small"><svg viewBox="0 8 340 228" role="img" aria-label="Temperature against time for a reaction in a cup. A flat line of readings before mixing, a quick rise at the time of mixing, then a slow steady fall. The falling line is extended backwards as a dashed line to the time of mixing, and the temperature change is the vertical gap between the dashed line and the starting temperature"><path class="ax" d="M30 205V25" marker-end="url(#ahm)"/><path class="ax" d="M30 205H330" marker-end="url(#ahm)"/><text class="tl" x="38" y="22">temperature / °C</text><text class="tl" x="330" y="227" text-anchor="end">time / min</text><path class="c1 sw2" d="M40 170H120"/><circle class="fi" cx="40" cy="170" r="2.5"/><circle class="fi" cx="62" cy="170" r="2.5"/><circle class="fi" cx="84" cy="170" r="2.5"/><circle class="fi" cx="106" cy="170" r="2.5"/><path class="c1 sw2" d="M150 118Q154 70 168 70L325 112"/><circle class="fi" cx="190" cy="75.9" r="2.5"/><circle class="fi" cx="217" cy="83.1" r="2.5"/><circle class="fi" cx="244" cy="90.3" r="2.5"/><circle class="fi" cx="271" cy="97.6" r="2.5"/><circle class="fi" cx="298" cy="104.8" r="2.5"/><circle class="fi" cx="325" cy="112.0" r="2.5"/><path class="ln-m thin dash" d="M168 70L140 62.5"/><path class="ln-m thin dash" d="M120 170H140"/><path class="ln-m thin dash" d="M140 170V205"/><path class="c2 sw2" d="M140 116V65.5" marker-end="url(#ah)"/><path class="c2 sw2" d="M140 116V167" marker-end="url(#ah)"/><text class="tl" x="131" y="120" text-anchor="end">ΔT</text><text class="tl tc" x="140" y="227">time of mixing</text><text class="tl" x="36" y="160">before mixing</text><text class="tl" x="165" y="150">dashed: cooling line</text><text class="tl" x="165" y="167">extended back to mixing</text></svg><figcaption>A temperature–time graph for an exothermic reaction in a cup. The temperature change ΔT is read at the time of mixing, from the extended cooling line, so heat lost after mixing is allowed for.</figcaption></figure>
:::

:::eg 25.0 cm³ of 1.00 mol dm⁻³ hydrochloric acid and 25.0 cm³ of 1.00 mol dm⁻³ sodium hydroxide, both at the same starting temperature, are mixed in a polystyrene cup. The extrapolated temperature rise is 6.8 K. Calculate the enthalpy change of neutralisation. Assume that the density of the solution is 1.00 g cm⁻³ and its specific heat capacity is 4.18 J g⁻¹ K⁻¹.
The mass of solution is 50.0 g (25.0 + 25.0 cm³). Notice that it is the mass of **solution**, not the mass of NaOH or HCl.
\[q = mc\Delta T = 50.0 \times 4.18 \times 6.8 = 1421\,\mathrm{J}\] [M1]
Amount of water formed = amount of acid = \(1.00 \times 25.0/1000 = 0.0250\) mol. [B1]
\[\Delta H = -\frac{1421}{0.0250} = -56\,848\,\mathrm{J\,mol^{-1}} = -56.8\,\mathrm{kJ\,mol^{-1}}\] [M1] [A1]
The temperature rose, so the reaction is exothermic and the sign is negative.
:::

:::eg 25.0 cm³ of 0.200 mol dm⁻³ copper(II) sulfate solution is added to excess zinc powder in a polystyrene cup. The temperature rises by 10.4 K. Calculate the enthalpy change for \(\ce{Zn + CuSO4 -> ZnSO4 + Cu}\).
Zinc is in excess, so copper(II) sulfate is the limiting reactant: \(n = 0.200 \times 25.0/1000 = 0.00500\) mol. [B1]
The mass of solution is 25.0 g.
\[q = 25.0 \times 4.18 \times 10.4 = 1087\,\mathrm{J}\] [M1]
\[\Delta H = -\frac{1087}{0.00500} = -217\,000\,\mathrm{J\,mol^{-1}} = -217\,\mathrm{kJ\,mol^{-1}}\] [M1] [A1]
:::

:::eg (Endothermic) 4.00 g of ammonium nitrate, \(\ce{NH4NO3}\), is dissolved in 50.0 cm³ of water at 21.0 °C. The temperature falls by 6.1 K. Calculate the enthalpy change of solution, taking the mass heated or cooled as 50.0 g.
\(M_r = 2(14.0) + 4(1.0) + 3(16.0) = 80.0\), so \(n = 4.00/80.0 = 0.0500\) mol. [B1]
\[q = mc\Delta T = 50.0 \times 4.18 \times (-6.1) = -1275\,\mathrm{J}\] [M1]
\[\Delta H = -\frac{-1275}{0.0500} = +25\,500\,\mathrm{J\,mol^{-1}} = +25.5\,\mathrm{kJ\,mol^{-1}}\] [M1] [A1]
The sign is positive, as it should be for a process that makes the solution colder.
:::

:::warn Mass of what?
In \(q = mc\Delta T\) the mass \(m\) is the mass of the **water or solution** that changes temperature, not the mass of the solid you added. The amount \(n\) in \(\Delta H = -q/n\) is the amount of the **limiting reactant**. Many marks are lost by using the mass of the solid in \(q\), or the total amount of both reactants in \(n\).
:::

### Burning a fuel

:::lab Enthalpy change of combustion of ethanol
Fill a spirit burner with ethanol and weigh it. Put 200 g of water in a copper can, held above the burner, and record its temperature. Light the burner under the can and stir the water with the thermometer. After the temperature has risen by about 20 °C, put out the flame, record the highest temperature and weigh the burner again. The mass lost is the mass of ethanol burned. Keep draughts off the flame and use no other flames nearby, because ethanol is flammable.
:::

:::eg In an experiment like this, 0.78 g of ethanol, \(\ce{C2H5OH}\), burned and raised the temperature of 200 g of water by 20.0 K. Calculate the enthalpy change of combustion, and explain why the value is less exothermic than the data-book value of \(-1367\) kJ mol⁻¹.
\(M_r(\ce{C2H5OH}) = 2(12.0) + 6(1.0) + 16.0 = 46.0\), so \(n = 0.78/46.0 = 0.01696\) mol. [B1]
\[q = 200 \times 4.18 \times 20.0 = 16\,720\,\mathrm{J}\] [M1]
\[\Delta H_{\mathrm{c}} = -\frac{16\,720}{0.01696} = -986\,000\,\mathrm{J\,mol^{-1}} = -986\,\mathrm{kJ\,mol^{-1}}\] [M1] [A1]
The experiment captured only about 72% of the data-book energy. Most of the energy of the flame warms the air, the can and the apparatus rather than the water, so the value is less exothermic. Other causes: incomplete combustion (soot on the can), evaporation of ethanol from the wick, and the conditions are not standard.
:::

Heat loss is the main error of calorimetry. Ways to reduce it: use a lid on the cup, a draught shield around a burner, a copper can (a good conductor), a short distance between the flame and the can, and stirring so that the temperature is the same throughout the water. The extrapolation method corrects for the cooling in a cup but not for the heat that never reaches the water in a burner experiment.

## Bond energies

### Making and breaking bonds

Energy must be **put in** to break a bond, because the atoms are attracted to each other and have to be pulled apart. The same amount of energy is **released** when the bond forms again. So breaking bonds is endothermic and making bonds is exothermic.

:::def Bond energy
The energy required to break one mole of a particular covalent bond in the gaseous state. Bond energies are always positive.
:::

The enthalpy change of a reaction is the net result of the two: energy in to break the bonds in the reactants, and energy out as the bonds in the products form.

:::key Using bond energies
\[\Delta H = \sum(\text{bond energies of bonds broken}) - \sum(\text{bond energies of bonds formed})\]
Add up one side for **every** bond that breaks (each molecule's bonds, multiplied by the number of molecules in the equation), and subtract the total for **every** bond that forms. Reactants and products must all be gases for the result to be reliable.
:::

:::eg Calculate the enthalpy change of combustion of methane using these bond energies in kJ mol⁻¹: C–H 410, O=O 496, C=O (in \(\ce{CO2}\)) 805, O–H 460. The equation is \(\ce{CH4(g) + 2O2(g) -> CO2(g) + 2H2O(g)}\).
**Bonds broken:** 4 C–H in \(\ce{CH4}\) and 2 O=O in \(\ce{2O2}\).
\(4(410) + 2(496) = 1640 + 992 = 2632\) kJ [M1]
**Bonds formed:** 2 C=O in \(\ce{CO2}\) and 4 O–H in \(\ce{2H2O}\).
\(2(805) + 4(460) = 1610 + 1840 = 3450\) kJ [M1]
\[\Delta H = 2632 - 3450 = -818\,\mathrm{kJ\,mol^{-1}}\] [A1]
:::

The energy changes can be drawn as a level diagram. The gaseous atoms sit above both the reactants and the products, because bonds must break before they can form.

:::html
<figure class="fig small"><svg viewBox="0 14 340 234" role="img" aria-label="Energy level diagram for the combustion of methane from bond energies: reactants at the middle level, separate gaseous atoms at the top level, products at the lowest level. An upward arrow for bonds broken, plus 2632 kilojoules per mole, a downward arrow for bonds formed, minus 3450, and the overall enthalpy change of minus 818 between reactants and products"><path class="ln thick" d="M50 40H290"/><path class="ln thick" d="M10 150H140"/><path class="ln thick" d="M180 220H330"/><path class="ln-m thin dash" d="M140 150H330"/><path class="c2 sw2" d="M60 147V43" marker-end="url(#ah)"/><path class="c2 sw2" d="M190 43V217" marker-end="url(#ah)"/><path class="c2 sw2" d="M315 153V217" marker-end="url(#ah)"/><text class="tl tc" x="170" y="30">C(g) + 4H(g) + 4O(g)</text><text class="tl tc" x="75" y="170">CH₄(g) + 2O₂(g)</text><text class="tl tc" x="255" y="240">CO₂(g) + 2H₂O(g)</text><text class="tl" x="70" y="90">bonds broken</text><text class="tl" x="70" y="107">+2632 kJ mol⁻¹</text><text class="tl" x="200" y="90">bonds formed</text><text class="tl" x="200" y="107">−3450 kJ mol⁻¹</text><text class="tl" x="305" y="185" text-anchor="end">ΔH = −818</text><text class="tl" x="305" y="202" text-anchor="end">kJ mol⁻¹</text></svg><figcaption>Bond energies for burning methane. Breaking all the bonds in the reactants costs 2632 kJ; making all the bonds in the products releases 3450 kJ. The net change is −818 kJ per mole of methane.</figcaption></figure>
:::

### Exact and average bond energies

The Data section lists two kinds of bond energy. The bond energies of **diatomic** molecules such as H–H, O=O, N≡N, Cl–Cl and H–Cl are **exact**: there is only one bond of that kind. Bond energies for bonds such as C–H, C–C, C=O and O–H are **averages**: the C–H bond in methane needs a slightly different energy from the C–H bond in ethanol, so the table gives an average over many compounds.

Two consequences follow:

- A result from bond energies is only an **estimate**. Methane's calculated value of −818 kJ mol⁻¹ differs from the experimental \(\Delta H^{\ominus}_{\mathrm{c}}\) of about −890 kJ mol⁻¹, because average values are used, and because the calculation forms water as a **gas** while the standard enthalpy of combustion forms liquid water, which releases extra energy as the gas condenses.
- Bond energies apply to **gases**. Substances that are liquid or solid first need energy to vaporise, which the bond energy calculation does not include.

:::eg Calculate the enthalpy change for \(\ce{C2H4(g) + H2(g) -> C2H6(g)}\). Use C=C 610, H–H 436, C–C 350, C–H 410 kJ mol⁻¹.
Bonds broken: 1 C=C and 1 H–H: \(610 + 436 = 1046\) kJ. [M1]
Bonds formed: 1 C–C and 2 new C–H: \(350 + 2(410) = 1170\) kJ. [M1]
\[\Delta H = 1046 - 1170 = -124\,\mathrm{kJ\,mol^{-1}}\] [A1]
Only the bonds that actually change are counted: the four C–H bonds that were already in ethene stay the same, so they cancel.
:::

:::eg (Real context) The Haber process makes ammonia: \(\ce{N2(g) + 3H2(g) -> 2NH3(g)}\). Calculate the enthalpy change, using N≡N 944, H–H 436 and N–H 390 kJ mol⁻¹.
Bonds broken: 1 N≡N and 3 H–H: \(944 + 3(436) = 2252\) kJ. [M1]
Bonds formed: 6 N–H (three in each of the two \(\ce{NH3}\) molecules): \(6(390) = 2340\) kJ. [M1]
\[\Delta H = 2252 - 2340 = -88\,\mathrm{kJ\,mol^{-1}}\] [A1]
The reaction is exothermic, and the value is for the amounts in the equation (2 mol of ammonia).
:::

You can also run the calculation backwards to find an unknown bond energy.

:::eg The enthalpy change for \(\ce{2H2(g) + O2(g) -> 2H2O(g)}\) is −484 kJ mol⁻¹ (data for this question). Use H–H 436 and O=O 496 kJ mol⁻¹ to find the O–H bond energy.
Bonds broken: \(2(436) + 496 = 1368\) kJ. [M1]
Bonds formed: 4 O–H (two in each \(\ce{H2O}\)), each with energy \(E\): \(4E\). [B1]
\[-484 = 1368 - 4E \quad\Rightarrow\quad 4E = 1852 \quad\Rightarrow\quad E = 463\,\mathrm{kJ\,mol^{-1}}\] [M1] [A1]
This is close to the Data-section value of 460 kJ mol⁻¹, which is an average.
:::

:::warn "Making bonds needs energy"
This statement is wrong and appears in many wrong answers. **Breaking** bonds needs energy (endothermic). **Making** bonds releases it (exothermic). A reaction is exothermic overall when the bonds formed release more energy than the bonds broken cost.
:::

## Hess's law

### Why different routes give the same answer

Some enthalpy changes cannot be measured directly. If you burn carbon in a limited supply of oxygen, you get a mixture of carbon monoxide and carbon dioxide, never pure CO. Hess's law gets round this by using other changes that **can** be measured.

:::def Hess's law
The enthalpy change of a reaction is the same whatever route is taken from the reactants to the products, provided the initial and final conditions are the same.
:::

:::analogy
Climbing a mountain by the steep path or the long winding path takes different distances, but the change in height from the foot to the summit is the same. Enthalpy, like height, depends only on the start and the finish.
:::

:::proof Why Hess's law is true
1. Enthalpy \(H\) is a property of the chemicals in a given state, like height of a location.
2. Take two routes from the same reactants to the same products, with enthalpy changes \(\Delta H_1\) and \(\Delta H_2\).
3. Go forward by route 1 and back by route 2. You return to the reactants you started with, so the total enthalpy change round the loop is \(\Delta H_1 - \Delta H_2\).
4. If this were not zero, running round the loop would create or destroy energy each time.
5. Energy cannot be created or destroyed (the law of conservation of energy), so \(\Delta H_1 - \Delta H_2 = 0\), and \(\Delta H_1 = \Delta H_2\).
:::

An **energy cycle** shows the routes with arrows. The rule for reading it: follow the arrows of one route and add up its enthalpy changes; follow the other route and add up its enthalpy changes; the two totals are equal. When you go **against** an arrow, change the sign.

### Using enthalpies of formation

Any reaction can be done in your head by breaking the reactants down to their elements and building the products from the same elements. The elements are the common starting point, so they go at the bottom of the cycle.

:::html
<figure class="fig small"><svg viewBox="0 22 340 212" role="img" aria-label="Energy cycle for the reaction of iron(III) oxide with carbon monoxide. At the top an arrow from the reactants Fe2O3 plus 3CO to the products 2Fe plus 3CO2 is labelled delta H r equals question mark. Below, the elements 2Fe, 3C and 3O2 are joined to the reactants by an upward arrow (1) for the formation enthalpies of the reactants, minus 1157, and to the products by an upward arrow (2) for the formation enthalpies of the products, minus 1182"><rect class="fm s-acc" x="9.8" y="30" width="88" height="30" rx="8"/><text class="tl tc" x="53.8" y="50">Fe₂O₃ + 3CO</text><rect class="fm s-acc" x="248.9" y="30" width="81" height="30" rx="8"/><text class="tl tc" x="289.4" y="50">2Fe + 3CO₂</text><rect class="fm s-acc" x="116.5" y="150" width="107" height="30" rx="8"/><text class="tl tc" x="170" y="170">2Fe + 3C + 3O₂</text><path class="ln" d="M104 45L243 45" marker-end="url(#ah)"/><text class="tl tc halo" x="173" y="38">ΔHr = ?</text><path class="ln" d="M142 148L58 66" marker-end="url(#ah)"/><path class="ln" d="M198 148L285 66" marker-end="url(#ah)"/><text class="tl" x="86" y="110" text-anchor="end">(1) ΔHf</text><text class="tl" x="256" y="110">ΔHf (2)</text><text class="tl" x="15" y="207">(1) ΔHf of reactants: −824 + 3(−111) = −1157</text><text class="tl" x="15" y="227">(2) ΔHf of products: 3(−394) = −1182</text></svg><figcaption>A formation cycle for the reduction of iron(III) oxide by carbon monoxide in a blast furnace. The two upward arrows, (1) and (2), are formation enthalpies. Following the route round through the elements gives the same total as the direct arrow at the top.</figcaption></figure>
:::

Going from the reactants to the products by the route through the elements means going **against** the first arrow (reactants down to elements, so the sign changes) and **with** the second. In symbols:

:::key Hess's law with enthalpies of formation
\[\Delta H^{\ominus}_{\mathrm{r}} = \sum \Delta H^{\ominus}_{\mathrm{f}}(\text{products}) - \sum \Delta H^{\ominus}_{\mathrm{f}}(\text{reactants})\]
Multiply each \(\Delta H^{\ominus}_{\mathrm{f}}\) by the number of moles in the equation. Elements in their standard states have \(\Delta H^{\ominus}_{\mathrm{f}} = 0\).
:::

:::eg (Real context) In a blast furnace iron(III) oxide is reduced by carbon monoxide: \(\ce{Fe2O3(s) + 3CO(g) -> 2Fe(s) + 3CO2(g)}\). Use these data for this question, in kJ mol⁻¹: \(\Delta H_{\mathrm{f}}\) of \(\ce{Fe2O3}\) −824, of CO −111, of \(\ce{CO2}\) −394. Calculate \(\Delta H_{\mathrm{r}}\).
Fe is an element, so its \(\Delta H_{\mathrm{f}}\) is 0. [B1]
Products: \(3(-394) = -1182\) kJ. [M1]
Reactants: \(-824 + 3(-111) = -1157\) kJ. [M1]
\[\Delta H_{\mathrm{r}} = -1182 - (-1157) = -25\,\mathrm{kJ\,mol^{-1}}\] [A1]
:::

:::eg (Real context) The iron in a hand-warmer is oxidised: \(\ce{4Fe + 3O2 -> 2Fe2O3}\). Using \(\Delta H_{\mathrm{f}}(\ce{Fe2O3}) = -824\) kJ mol⁻¹, calculate the energy released by 10.0 g of iron.
Products: \(2(-824) = -1648\) kJ; both reactants are elements, so \(\Delta H_{\mathrm{r}} = -1648\) kJ for 4 mol of iron. [M1]
Energy per mole of iron \(= 1648/4 = 412\) kJ. [B1]
\(n(\ce{Fe}) = 10.0/55.8 = 0.1792\) mol. [B1]
Energy released \(= 0.1792 \times 412 = 73.8\) kJ. [A1]
:::

### Using enthalpies of combustion

Sometimes the data you have are enthalpies of combustion. Then the **products of combustion** (\(\ce{CO2}\) and \(\ce{H2O}\)) are the common point, and they go at the bottom of the cycle. Oxygen is supplied for every combustion, so it is not shown.

:::html
<figure class="fig small"><svg viewBox="0 22 340 212" role="img" aria-label="Energy cycle for the formation of ethanol from combustion data. At the top an arrow from 2C plus 3H2 plus half O2 to ethanol is labelled delta H f equals question mark. Below, a downward arrow (1) from the elements to the combustion products 2CO2 plus 3H2O is labelled with the combustion enthalpies of the elements, minus 1646, and a downward arrow (2) from ethanol to the same products with the combustion enthalpy of ethanol, minus 1367"><rect class="fm s-acc" x="9.9" y="30" width="166" height="30" rx="8"/><text class="tl tc" x="92.9" y="50">2C(s) + 3H₂(g) + ½O₂(g)</text><rect class="fm s-acc" x="255.2" y="30" width="75" height="30" rx="8"/><text class="tl tc" x="292.7" y="50">C₂H₅OH(l)</text><rect class="fm s-acc" x="106.5" y="150" width="127" height="30" rx="8"/><text class="tl tc" x="170" y="170">2CO₂(g) + 3H₂O(l)</text><path class="ln" d="M182 45L249 45" marker-end="url(#ah)"/><text class="tl tc halo" x="215.5" y="38">ΔHf = ?</text><path class="ln" d="M93 62L129 143" marker-end="url(#ah)"/><path class="ln" d="M293 62L213 144" marker-end="url(#ah)"/><text class="tl" x="100" y="110" text-anchor="end">(1) ΔHc</text><text class="tl" x="263" y="110">ΔHc (2)</text><text class="tl" x="15" y="207">(1) ΔHc: 2(−394) + 3(−286) = −1646</text><text class="tl" x="15" y="227">(2) ΔHc of ethanol: −1367</text></svg><figcaption>A combustion cycle for the formation of ethanol. Both downward arrows are combustion enthalpies: (1) burns the elements, (2) burns the ethanol, and both lead to the same products. The route down the left and up the right must equal the direct arrow at the top.</figcaption></figure>
:::

The route from the reactants to the products goes down the left arrow (with it) and up the right arrow (against it, so the sign changes):

:::key Hess's law with enthalpies of combustion
\[\Delta H^{\ominus}_{\mathrm{r}} = \sum \Delta H^{\ominus}_{\mathrm{c}}(\text{reactants}) - \sum \Delta H^{\ominus}_{\mathrm{c}}(\text{products})\]
Notice that the order is the reverse of the formation rule: **reactants minus products**.
:::

:::eg Calculate the enthalpy change of formation of ethanol, \(\ce{2C(s) + 3H2(g) + 1/2O2(g) -> C2H5OH(l)}\), from these standard enthalpies of combustion in kJ mol⁻¹: C(s) −394, \(\ce{H2(g)}\) −286, \(\ce{C2H5OH(l)}\) −1367.
Reactants: \(2(-394) + 3(-286) = -788 - 858 = -1646\) kJ. [M1]
(Oxygen has \(\Delta H_{\mathrm{c}} = 0\), as it does not burn.)
\[\Delta H_{\mathrm{f}} = \sum\Delta H_{\mathrm{c}}(\text{reactants}) - \sum\Delta H_{\mathrm{c}}(\text{products}) = -1646 - (-1367)\] [M1]
\[\Delta H_{\mathrm{f}} = -279\,\mathrm{kJ\,mol^{-1}}\] [A1]
:::

:::eg Calculate the standard enthalpy change of combustion of propane, \(\ce{C3H8(g)}\), using \(\Delta H_{\mathrm{f}}\) values (kJ mol⁻¹): \(\ce{C3H8}\) −105, \(\ce{CO2}\) −394, \(\ce{H2O(l)}\) −286.
The equation is \(\ce{C3H8(g) + 5O2(g) -> 3CO2(g) + 4H2O(l)}\). [B1]
Products: \(3(-394) + 4(-286) = -1182 - 1144 = -2326\) kJ. [M1]
Reactants: \(-105\) kJ (oxygen is an element, so 0).
\[\Delta H_{\mathrm{c}} = -2326 - (-105) = -2221\,\mathrm{kJ\,mol^{-1}}\] [M1] [A1]
:::

### A cycle with experimental data

Hess's law is also the way to find an enthalpy change that cannot be measured, using two that can. Calcium carbonate does not decompose at room temperature, and heating it in a calorimeter is hard. But both calcium carbonate and calcium oxide react readily with hydrochloric acid, and the temperature rises in a cup can be measured.

:::html
<figure class="fig small"><svg viewBox="0 22 340 212" role="img" aria-label="Energy cycle for the thermal decomposition of calcium carbonate. At the top an arrow from CaCO3 to CaO plus CO2 is labelled delta H equals question mark. Both are joined by downward arrows to CaCl2 solution plus water plus CO2: arrow (1), delta H 1 equals minus 15, for calcium carbonate with hydrochloric acid, and arrow (2), delta H 2 equals minus 194, for calcium oxide with hydrochloric acid"><rect class="fm s-acc" x="10" y="30" width="68" height="30" rx="8"/><text class="tl tc" x="44" y="50">CaCO₃(s)</text><rect class="fm s-acc" x="216.2" y="30" width="114" height="30" rx="8"/><text class="tl tc" x="273.2" y="50">CaO(s) + CO₂(g)</text><rect class="fm s-acc" x="74" y="150" width="192" height="30" rx="8"/><text class="tl tc" x="170" y="170">CaCl₂(aq) + H₂O(l) + CO₂(g)</text><path class="ln" d="M84 45L210 45" marker-end="url(#ah)"/><text class="tl tc halo" x="147" y="38">ΔH = ?</text><path class="ln" d="M44 62L96 143" marker-end="url(#ah)"/><path class="ln" d="M273 62L243 142" marker-end="url(#ah)"/><text class="tl" x="60" y="110" text-anchor="end">(1)</text><text class="tl" x="269" y="110">(2)</text><text class="tl" x="15" y="207">(1) + 2HCl(aq): ΔH₁ = −15</text><text class="tl" x="15" y="227">(2) + 2HCl(aq): ΔH₂ = −194</text></svg><figcaption>An energy cycle for the thermal decomposition of calcium carbonate. Both solids react with hydrochloric acid to give the same products, so the unknown enthalpy change is the difference between the two measured ones.</figcaption></figure>
:::

:::eg Calcium carbonate and calcium oxide each react with excess dilute hydrochloric acid. The measured enthalpy changes (data for this question) are: \(\ce{CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g)}\), \(\Delta H_1 = -15\) kJ mol⁻¹; \(\ce{CaO(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l)}\), \(\Delta H_2 = -194\) kJ mol⁻¹. Calculate the enthalpy change for \(\ce{CaCO3(s) -> CaO(s) + CO2(g)}\).
The direct route (top arrow) followed by \(\Delta H_2\) must equal route 1: \(\Delta H + \Delta H_2 = \Delta H_1\). [M1]
\[\Delta H = \Delta H_1 - \Delta H_2 = -15 - (-194)\] [M1]
\[\Delta H = +179\,\mathrm{kJ\,mol^{-1}}\] [A1]
The decomposition is endothermic, which is why limestone has to be heated strongly in a kiln to make quicklime.
:::

Hess's law needs only one more skill: finding a missing step, as for carbon monoxide.

:::eg Carbon cannot be burned to carbon monoxide alone. Calculate the enthalpy change of formation of CO from the standard enthalpies of combustion of carbon (−394 kJ mol⁻¹) and carbon monoxide (−283 kJ mol⁻¹).
Burning carbon straight to \(\ce{CO2}\) can be done in two steps: carbon to CO (\(\Delta H_{\mathrm{f}}\), unknown), then CO to \(\ce{CO2}\). [B1]
\[\ce{C + 1/2O2 -> CO} \;(\Delta H_{\mathrm{f}}) \qquad \ce{CO + 1/2O2 -> CO2} \;(-283) \qquad \ce{C + O2 -> CO2} \;(-394)\]
Both routes give \(\ce{CO2}\), so \(\Delta H_{\mathrm{f}} + (-283) = -394\). [M1]
\[\Delta H_{\mathrm{f}}(\ce{CO}) = -394 - (-283) = -111\,\mathrm{kJ\,mol^{-1}}\] [A1]
:::

:::eg (Real context) Compare hydrogen and octane (a component of petrol) as fuels per **gram**. Use \(\Delta H_{\mathrm{c}}\) (kJ mol⁻¹): \(\ce{H2}\) −286, \(\ce{C8H18}\) −5470.
\(M_r(\ce{H2}) = 2.0\): energy per gram \(= 286/2.0 = 143\) kJ g⁻¹. [M1]
\(M_r(\ce{C8H18}) = 8(12.0) + 18(1.0) = 114.0\): energy per gram \(= 5470/114.0 = 48.0\) kJ g⁻¹. [M1]
Hydrogen releases about three times as much energy per gram, but it is a gas, so a gram takes up a very large volume unless it is compressed. [B1]
:::

:::exam Hess's law method
Draw the cycle first. Write the three key lines: the reaction you want, the data you are given, and which of the two cycle types (formation: elements at the bottom; combustion: products of combustion at the bottom) fits the data. Multiply each value by its coefficient in the equation. Reverse an arrow, change the sign. State the final answer with its sign and the unit kJ mol⁻¹.
:::

:::eg Spot the error: 50.0 cm³ of 1.00 mol dm⁻³ hydrochloric acid and 50.0 cm³ of 1.00 mol dm⁻³ sodium hydroxide are mixed, and the temperature rises by 6.5 K. Calculate the enthalpy change of neutralisation (density 1.00 g cm⁻³, c = 4.18 J g⁻¹ K⁻¹). [4 marks]
A student wrote this answer.

Line 1: \(q = mc\Delta T = 100.0 \times 4.18 \times 6.5 = 2717\) J
Line 2: \(n(\ce{H2O}) = 1.00 \times 50.0/1000 = 0.0500\) mol
Line 3: \(\Delta H = 2.717 / 0.0500 = +54.3\) kJ mol⁻¹

Line 1 is correct [M1]. Line 2 is correct [M1]. Line 3 has the right size [M1]. **But the sign is wrong: the temperature rose, so the reaction is exothermic and ΔH must be negative. The accuracy mark is lost [A0].**

Correct line 3: \(\Delta H = -2.717/0.0500 = -54.3\) kJ mol⁻¹. [A1]

The student scores 3 out of 4. The formula \(\Delta H = -q/n\) has a minus sign built in: if you work out \(q\) from a temperature rise, the enthalpy change is negative. Finish every calorimetry answer by asking whether the sign matches what the thermometer did.
:::

:::try Start easy, finish at exam standard
Q: Say whether each is exothermic or endothermic: (a) ΔH = −92 kJ mol⁻¹, (b) a reaction that makes the test tube feel cold, (c) products higher than reactants on a pathway diagram, (d) bond making.
A: (a) exothermic. (b) endothermic: it takes energy from the surroundings. (c) endothermic: ΔH is positive. (d) exothermic: energy is released.
Q: Write the equation for the standard enthalpy change of formation of (a) \(\ce{CH4}\), (b) \(\ce{NaCl}\), (c) \(\ce{H2O(l)}\).
A: (a) \(\ce{C(s) + 2H2(g) -> CH4(g)}\). (b) \(\ce{Na(s) + 1/2Cl2(g) -> NaCl(s)}\). (c) \(\ce{H2(g) + 1/2O2(g) -> H2O(l)}\).
Q: How much heat energy is needed to warm 75.0 g of water by 8.0 K?
A: \(q = mc\Delta T = 75.0 \times 4.18 \times 8.0 = 2508\) J, which is 2.5 kJ.
Q: 0.0200 mol of a solid dissolves in 40.0 g of water and the temperature falls by 3.5 K. Calculate ΔH of solution.
A: \(q = 40.0 \times 4.18 \times (-3.5) = -585\) J. \(\Delta H = -(-585)/0.0200 = +29\,260\) J mol⁻¹ = +29.3 kJ mol⁻¹.
Q: Use bond energies (C–H 410, Cl–Cl 242, C–Cl 340, H–Cl 431 kJ mol⁻¹) to calculate ΔH for \(\ce{CH4 + Cl2 -> CH3Cl + HCl}\).
A: Broken: C–H and Cl–Cl, \(410 + 242 = 652\) kJ. Formed: C–Cl and H–Cl, \(340 + 431 = 771\) kJ. \(\Delta H = 652 - 771 = -119\) kJ mol⁻¹.
Q: Use these ΔHf values in kJ mol⁻¹ to calculate the enthalpy change for \(\ce{2H2O2(l) -> 2H2O(l) + O2(g)}\): \(\ce{H2O2(l)}\) −188, \(\ce{H2O(l)}\) −286.
A: Products: \(2(-286) = -572\) (\(\ce{O2}\) is an element, 0). Reactants: \(2(-188) = -376\). \(\Delta H = -572 - (-376) = -196\) kJ mol⁻¹.
Q: A reaction \(\ce{A -> B}\) has ΔH = +40 kJ mol⁻¹. State ΔH for (a) \(\ce{B -> A}\), (b) \(\ce{2A -> 2B}\).
A: (a) −40 kJ mol⁻¹: reversing the reaction changes the sign. (b) +80 kJ mol⁻¹: doubling the equation doubles ΔH.
Q: A student says the activation energy of a reaction is the same as its enthalpy change. Explain what is wrong.
A: Eₐ is the energy barrier from the reactants to the top of the peak and is always positive. ΔH is the energy difference between products and reactants and can be positive or negative. A catalyst lowers Eₐ but does not change ΔH.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Define the standard enthalpy change of formation of a compound.
A: The enthalpy change when one mole of the compound [B1] is formed from its elements [B1] in their standard states under standard conditions. [B1]
Q: [3 marks] ★ Sketch a reaction pathway diagram for an exothermic reaction. Label the reactants, the products, the activation energy and the enthalpy change.
A: The products are drawn lower than the reactants, with a curve rising to a peak between them. [B1]
Eₐ is labelled from the reactants level up to the top of the peak. [B1]
ΔH is labelled from the reactants level down to the products level, with an arrow pointing down. [B1]
Q: [4 marks] ★★ 50.0 cm³ of 2.00 mol dm⁻³ hydrochloric acid and 50.0 cm³ of 2.00 mol dm⁻³ sodium hydroxide solution are mixed in a polystyrene cup. The temperature rises by 13.5 K. Calculate the enthalpy change of neutralisation, in kJ mol⁻¹. Assume the density is 1.00 g cm⁻³ and \(c = 4.18\) J g⁻¹ K⁻¹.
H: What is the mass of the solution? What is the amount of water formed?
A: \(q = 100.0 \times 4.18 \times 13.5 = 5643\) J [M1]
\(n = 2.00 \times 50.0/1000 = 0.100\) mol [B1]
\(\Delta H = -5643 / 0.100 = -56\,430\) J mol⁻¹ [M1]
\(= -56.4\) kJ mol⁻¹ [A1]
Q: [4 marks] ★★ Use bond energies (C=C 610, C–C 350, C–H 410, H–Br 366, C–Br 280 kJ mol⁻¹) to calculate the enthalpy change for \(\ce{C2H4(g) + HBr(g) -> C2H5Br(g)}\).
H: List only the bonds that change: one C=C becomes C–C, and so on.
A: Bonds broken: C=C and H–Br. [B1]
\(610 + 366 = 976\) kJ [M1]
Bonds formed: C–C, C–H and C–Br: \(350 + 410 + 280 = 1040\) kJ [M1]
\(\Delta H = 976 - 1040 = -64\) kJ mol⁻¹ [A1]
Q: [3 marks] ★★ Burning carbon in a limited supply of oxygen does not give pure carbon monoxide, so its enthalpy change of formation cannot be measured directly. Use the enthalpies of combustion of carbon (−394 kJ mol⁻¹) and carbon monoxide (−283 kJ mol⁻¹) to calculate the enthalpy change of formation of carbon monoxide.
A: Route: \(\ce{C + 1/2O2 -> CO}\) then \(\ce{CO + 1/2O2 -> CO2}\), equal to \(\ce{C + O2 -> CO2}\). [M1]
\(\Delta H_{\mathrm{f}}(\ce{CO}) + (-283) = -394\) [M1]
\(\Delta H_{\mathrm{f}}(\ce{CO}) = -111\) kJ mol⁻¹ [A1]
Q: [6 marks] ★★ In an experiment, 0.64 g of methanol, \(\ce{CH3OH}\), was burned in a spirit burner and raised the temperature of 150 g of water by 18.0 K. (a) Calculate the enthalpy change of combustion of methanol. (b) The data-book value is −726 kJ mol⁻¹. Give two reasons why the experimental value is different.
H: Work out the amount of methanol from its mass first.
A: (a) \(M_r = 12.0 + 4(1.0) + 16.0 = 32.0\), so \(n = 0.64/32.0 = 0.0200\) mol. [B1]
\(q = 150 \times 4.18 \times 18.0 = 11\,286\) J [M1]
\(\Delta H = -11\,286/0.0200\) [M1] \(= -564\) kJ mol⁻¹ [A1]
(b) Heat is lost to the surroundings (the air, the can and the apparatus), so the temperature rise is too small. [B1]
Incomplete combustion releases less energy than complete combustion (or some methanol evaporates without burning). [B1]
Q: [6 marks] ★★★ (#chem.equilibria) Ammonia is made by \(\ce{N2(g) + 3H2(g) -> 2NH3(g)}\). (a) Use bond energies (N≡N 944, H–H 436, N–H 390 kJ mol⁻¹) to calculate the enthalpy change. (b) The enthalpy change of formation of ammonia is −46 kJ mol⁻¹. Use this to calculate the enthalpy change of the reaction. (c) Suggest one reason why the answers to (a) and (b) are different.
H: Part (b) is the formation rule: products minus reactants. Elements have zero formation enthalpy.
A: (a) Bonds broken: \(944 + 3(436) = 2252\) kJ [M1]; bonds formed: \(6(390) = 2340\) kJ [M1]; \(\Delta H = -88\) kJ mol⁻¹ [A1]
(b) \(\Delta H = 2(-46) - 0 = -92\) kJ mol⁻¹ [M1] [A1]
(c) The N–H bond energy in the Data section is an average over many compounds, not the exact value for ammonia. [B1]
Q: [7 marks] ★★★ (#chem.states) A car could run on hydrogen or on octane. \(\Delta H_{\mathrm{c}}\) (kJ mol⁻¹): \(\ce{H2}\) −286 and \(\ce{C8H18}\) −5470. (a) Calculate the energy released by burning 1.00 kg of each fuel. (b) Calculate the volume of 1.00 kg of hydrogen gas at 298 K and 101 kPa. (c) Comment on the practical consequence.
H: In (a), find the amount in mol of 1.00 kg of each. In (b), use \(pV = nRT\) with SI units.
A: (a) Hydrogen: \(n = 1000/2.0 = 500\) mol, energy \(= 500 \times 286 = 143\,000\) kJ (143 MJ). [M1] [A1]
Octane: \(M_r = 114.0\), \(n = 1000/114.0 = 8.772\) mol, energy \(= 8.772 \times 5470 = 47\,980\) kJ (48.0 MJ). [M1] [A1]
(b) \(V = nRT/p = 500 \times 8.31 \times 298 / 101\,000\) [M1] \(= 12.3\,\mathrm{m^3}\) (12 300 dm³). [A1]
(c) Hydrogen releases about three times as much energy per kilogram, but as a gas it occupies a very large volume, so it has to be compressed or liquefied and stored in strong tanks. [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ The enthalpy change of solution of anhydrous copper(II) sulfate, \(\ce{CuSO4(s)}\), is −66.1 kJ mol⁻¹ and that of hydrated copper(II) sulfate, \(\ce{CuSO4.5H2O(s)}\), is +11.7 kJ mol⁻¹ (data for this question). Draw an energy cycle and calculate the enthalpy change for \(\ce{CuSO4(s) + 5H2O(l) -> CuSO4.5H2O(s)}\).
H: Both solids dissolve to give the same solution.
A: Cycle: anhydrous \(\ce{CuSO4}\) + 5\(\ce{H2O}\) goes directly to the hydrate (ΔH unknown); both routes lead to \(\ce{CuSO4(aq)}\). [B1]
Route 1 (via the hydrate): \(\Delta H + 11.7\). Route 2 (dissolving the anhydrous solid directly): \(-66.1\). [B1]
\(\Delta H + 11.7 = -66.1\) [M1]
\(\Delta H = -77.8\) kJ mol⁻¹ [A1]
Q: [4 marks] ★★★ In the methane example the bond energy calculation gave −818 kJ mol⁻¹ with water as a gas, but the standard enthalpy change of combustion is about −890 kJ mol⁻¹. The enthalpy change for \(\ce{H2O(g) -> H2O(l)}\) is −44.0 kJ mol⁻¹ (data for this question). Correct the bond energy value for liquid water and say whether it now agrees with −890 kJ mol⁻¹.
H: The equation produces 2 mol of water.
A: Two moles of water condense, releasing \(2 \times 44.0 = 88.0\) kJ. [M1]
\(\Delta H = -818 - 88.0\) [M1] \(= -906\) kJ mol⁻¹. [A1]
This is closer to −890 kJ mol⁻¹, but it still differs by about 16 kJ mol⁻¹, because the bond energies for C–H, C=O and O–H are averages and not the exact values in these molecules. [B1]
:::

:::quiz
? Which statement is correct for an exothermic reaction?
- ΔH is positive and the surroundings get colder.
+ ΔH is negative and the surroundings get warmer.
- ΔH is negative and the surroundings get colder.
- ΔH is positive and the products have lower enthalpy than the reactants.
> In an exothermic reaction energy is released, the products have lower enthalpy than the reactants, ΔH is negative and the surroundings warm up.
? The temperature of 100 g of solution rises by 5.0 K when 0.0500 mol of a reactant reacts. What is ΔH? (c = 4.18 J g⁻¹ K⁻¹)
- +41.8 kJ mol⁻¹
- −41 800 kJ mol⁻¹
+ −41.8 kJ mol⁻¹
- −2.09 kJ mol⁻¹
> \(q = 100 \times 4.18 \times 5.0 = 2090\) J; \(2.09/0.0500 = 41.8\) kJ mol⁻¹, negative because the temperature rose. +41.8 has the wrong sign, −41 800 forgets to convert J to kJ, and −2.09 forgets to divide by the amount.
? Which equation represents the standard enthalpy change of formation of water?
- \(\ce{2H2(g) + O2(g) -> 2H2O(l)}\)
- \(\ce{H2(g) + 1/2O2(g) -> H2O(g)}\)
+ \(\ce{H2(g) + 1/2O2(g) -> H2O(l)}\)
- \(\ce{H2O(l) -> H2(g) + 1/2O2(g)}\)
> Formation means 1 mol of the compound from its elements in their standard states. Water is a liquid in its standard state, so \(\ce{H2O(l)}\) with one mole formed.
? How is ΔH calculated from bond energies?
- Σ(bonds formed) − Σ(bonds broken)
+ Σ(bonds broken) − Σ(bonds formed)
- Σ(bonds broken) + Σ(bonds formed)
- Σ(bonds formed) × Σ(bonds broken)
> Breaking bonds costs energy (a positive amount) and forming bonds releases it, so ΔH is the energy put in minus the energy released.
? Using Hess's law, which gives \(\Delta H_{\mathrm{r}}\) from standard enthalpies of combustion?
- Σ ΔHc(products) − Σ ΔHc(reactants)
+ Σ ΔHc(reactants) − Σ ΔHc(products)
- Σ ΔHc(reactants) + Σ ΔHc(products)
- Σ ΔHf(reactants) − Σ ΔHf(products)
> With combustion data the combustion products are the common point at the bottom of the cycle, so the rule is reactants minus products: the opposite of the formation rule.
? A student measures the enthalpy change of combustion of a fuel by heating water in a can. The result is less exothermic than the data-book value. Which is the most likely reason?
+ Heat is lost to the surroundings, so the water gains less than the fuel releases.
- The fuel burns at a lower temperature than normal.
- The water has a higher specific heat capacity than expected.
- The bonds in the fuel are stronger in the experiment.
> The main error in this experiment is heat loss to the air and to the apparatus, so the measured temperature rise, and so the enthalpy change, is too small.
? What does a catalyst change on a reaction pathway diagram?
- ΔH
+ Eₐ
- both Eₐ and ΔH
- the energy of the products
> A catalyst provides a route with a lower activation energy. The reactants and products are the same, so ΔH does not change.
:::

:::checklist What you can now do
- [ ] I can define exothermic and endothermic reactions and give the sign of ΔH for each.
- [ ] I can draw reaction pathway diagrams with ΔH and the activation energy labelled.
- [ ] I can state the standard conditions and define the standard enthalpy changes of reaction, formation, combustion and neutralisation.
- [ ] I can explain that breaking bonds is endothermic and making bonds is exothermic.
- [ ] I can use bond energies to calculate an enthalpy change of reaction, and explain why exact (diatomic) and average bond energies matter.
- [ ] I can calculate an enthalpy change from calorimetry data using \(q = mc\Delta T\) and \(\Delta H = -mc\Delta T/n\).
- [ ] I can construct an energy cycle and use Hess's law with enthalpies of formation, combustion and other measured data.
- [ ] I can calculate an enthalpy change that cannot be measured directly (such as the formation of CO), and one that uses bond energies in a cycle.
:::

:::recap
- Exothermic: energy released, temperature of surroundings rises, ΔH negative. Endothermic: energy absorbed, temperature falls, ΔH positive.
- Pathway diagram: Eₐ from the reactants up to the peak; ΔH from the reactants to the products. A catalyst lowers Eₐ, not ΔH.
- Standard conditions: 101 kPa, 298 K (1.00 mol dm⁻³ for solutions). ΔHf: 1 mol of compound from its elements in standard states; ΔHc: 1 mol burnt completely in oxygen; ΔHneut: 1 mol of water formed from an acid and an alkali; ΔHr: for the equation as written. ΔHf of an element = 0.
- Calorimetry: \(q = mc\Delta T\) with \(m\) the mass of water or solution and c = 4.18 J g⁻¹ K⁻¹; \(\Delta H = -q/n\) in kJ mol⁻¹ for the limiting reactant. Temperature rise means a negative ΔH. ΔT in K equals ΔT in °C.
- Extrapolate the cooling line back to the time of mixing. The main error in a combustion experiment is heat loss.
- Bond breaking is endothermic, bond making exothermic. ΔH = Σ(bonds broken) − Σ(bonds formed). Diatomic bond energies are exact, the others averages, so results are estimates.
- Hess's law: the enthalpy change is independent of the route. ΔHr = ΣΔHf(products) − ΣΔHf(reactants) and ΔHr = ΣΔHc(reactants) − ΣΔHc(products). Reversing the arrow changes the sign; multiply by the coefficients.
:::

:::links
- read: [Energetics menu](https://www.chemguide.co.uk/physical/energeticsmenu.html) · Chemguide · enthalpy changes, definitions, Hess's law and bond enthalpies in order
- read: [Hess's law and enthalpy cycles](https://www.chemguide.co.uk/physical/energetics/sums.html) · Chemguide · worked examples of energy cycles with formation and combustion data
- read: [Bond enthalpies](https://www.chemguide.co.uk/physical/energetics/bondenthalpies.html) · Chemguide · using average bond energies to estimate enthalpy changes
- practise: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [Redox and oxidation numbers](#chem.redox) shows how to follow the electrons in reactions.
