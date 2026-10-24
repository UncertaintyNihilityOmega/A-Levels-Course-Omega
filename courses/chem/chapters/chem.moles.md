@chapter chem.moles
@title Moles and stoichiometry
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 8–10 hours
@summary How chemists count atoms by weighing. You will use relative masses and the mole, write formulas and balanced and ionic equations, find empirical and molecular formulas, and calculate reacting masses, percentage yield, gas volumes, solution concentrations, titrations and limiting reagents.

:::why
Chemists cannot count atoms, so they weigh them, and the mole is the bridge between the mass you can weigh and the number of particles that react. Every quantitative question in chemistry, from the dose in a tablet to the carbon dioxide from a car engine, rests on this chapter. It is also the chapter that the whole of Paper 2 and Paper 4 calculations are built on, so time spent here repays itself many times.
:::

**Before you start**, you should know isotopes and the structure of the atom from [Atomic structure](#chem.atoms), and the basics of formulas and word equations from [Chemistry from zero](#chem.f.basics).

:::try Warm-up
Q: Define isotopes. (from [Atomic structure](#chem.atoms))
A: Atoms of the same element, with the same number of protons, but different numbers of neutrons.
Q: How many neutrons are in an atom of \({}^{37}\mathrm{Cl}\)? (from [Atomic structure](#chem.atoms))
A: Chlorine has 17 protons, so 37 − 17 = 20 neutrons.
Q: Balance \(\ce{H2 + O2 -> H2O}\). (from [Chemistry from zero](#chem.f.basics))
A: \(\ce{2H2 + O2 -> 2H2O}\)
:::

## Relative masses

An atom is far too light to weigh directly. Instead we compare the mass of each atom with a standard. The standard is the carbon-12 atom, and the unit of comparison is one twelfth of it.

:::def Unified atomic mass unit (u)
One twelfth of the mass of an atom of carbon-12.
:::

:::def Relative isotopic mass
The mass of an atom of an isotope compared with one twelfth of the mass of an atom of carbon-12.
:::

:::def Relative atomic mass, \(A_r\)
The weighted average mass of an atom of an element, taking account of the abundance of its isotopes, compared with one twelfth of the mass of an atom of carbon-12.
:::

:::def Relative molecular mass, \(M_r\)
The weighted average mass of a molecule compared with one twelfth of the mass of an atom of carbon-12. It is the sum of the \(A_r\) values of all the atoms in the molecular formula. For an ionic compound, which has no molecules, the same sum gives the **relative formula mass**, also written \(M_r\).
:::

All of these are *relative* quantities: they are ratios, so they have **no unit**. The \(A_r\) values you use come from the Periodic Table: \(A_r(\mathrm{H}) = 1.0\), \(A_r(\mathrm{C}) = 12.0\), \(A_r(\mathrm{O}) = 16.0\), \(A_r(\mathrm{Cl}) = 35.5\), and so on.

### Relative atomic mass from isotopes

Most elements are a mixture of isotopes. The relative atomic mass is the **weighted** mean of their isotopic masses: each isotopic mass counts in proportion to its abundance.

:::formula Relative atomic mass from isotopic abundances
\[A_r = \frac{\sum (\text{isotopic mass} \times \text{percentage abundance})}{100}\]
Add up (isotopic mass × abundance) for every isotope, then divide by 100 if the abundances are percentages (or by the sum of the abundances).
:::

:::eg Chlorine is 75% \({}^{35}\mathrm{Cl}\) and 25% \({}^{37}\mathrm{Cl}\). Calculate its relative atomic mass.
In 100 atoms, 75 have mass 35 and 25 have mass 37.
\[A_r = \frac{(75 \times 35) + (25 \times 37)}{100} = \frac{2625 + 925}{100} = 35.5\]
The answer lies between 35 and 37, and is closer to 35 because the lighter isotope is more abundant. That is a quick sense check.
:::

:::eg (Exam style) A sample of magnesium contains 79.0% \({}^{24}\mathrm{Mg}\), 10.0% \({}^{25}\mathrm{Mg}\) and 11.0% \({}^{26}\mathrm{Mg}\). Calculate the relative atomic mass of magnesium to 3 significant figures. [3 marks]
\[\sum(\text{mass} \times \text{abundance}) = (24 \times 79.0) + (25 \times 10.0) + (26 \times 11.0)\] [M1]
\[= 1896 + 250 + 286 = 2432\] [M1]
\[A_r = \frac{2432}{100} = 24.3\] [A1]
:::

:::eg Boron has two isotopes, \({}^{10}\mathrm{B}\) and \({}^{11}\mathrm{B}\), and \(A_r = 10.8\). Find the percentage abundance of \({}^{10}\mathrm{B}\).
Let the abundance of \({}^{10}\mathrm{B}\) be \(x\) per cent, so that of \({}^{11}\mathrm{B}\) is \(100 - x\).
\[\frac{10x + 11(100 - x)}{100} = 10.8 \quad\Rightarrow\quad 10x + 11(100 - x) = 1080\]
\[10x + 1100 - 11x = 1080 \quad\Rightarrow\quad 1100 - x = 1080 \quad\Rightarrow\quad x = 20\]
(The \(x\) terms combine: \(10x - 11x = -x\).)
Boron is 20% \({}^{10}\mathrm{B}\) and 80% \({}^{11}\mathrm{B}\).
:::

To find \(M_r\), add up the \(A_r\) values for every atom in the formula. Water, \(\ce{H2O}\): \(2(1.0) + 16.0 = 18.0\). Calcium hydroxide, \(\ce{Ca(OH)2}\): the bracket multiplies everything inside, so \(40.1 + 2(16.0 + 1.0) = 74.1\).

:::warn \(M_r\) has no unit, but molar mass does
\(M_r\) is a ratio, so it has no unit: "\(M_r\) of water is 18.0". The mass of one **mole** is the **molar mass**, \(M\), with the unit g mol⁻¹: "the molar mass of water is 18.0 g mol⁻¹". The numbers are the same, and the unit tells you which one you mean.
:::

## The mole

A glass of water contains about \(10^{25}\) molecules, a number too large to use as a unit. So chemists count in a large bundle called the **mole**.

:::def Mole
The amount of substance that contains \(6.022 \times 10^{23}\) particles. This number of particles per mole is the Avogadro constant, \(L = 6.022 \times 10^{23}\,\mathrm{mol^{-1}}\). The particles can be atoms, molecules, ions or electrons.
:::

The number was chosen so that 12 g of carbon-12 contains one mole of atoms, and that connects the two scales. The mass of one mole of a substance, in grams, is numerically equal to its relative mass: 12.0 g of carbon (\(A_r = 12.0\)), 18.0 g of water (\(M_r = 18.0\)), 58.5 g of sodium chloride (\(M_r = 58.5\)). So a mole is a known mass and a known number of particles at once.

:::formula The mole equations
\[n = \frac{m}{M} \qquad\qquad N = nL\]
\(n\) is the amount in mol, \(m\) the mass in g, \(M\) the molar mass in g mol⁻¹, and \(N\) the number of particles. Rearranged: \(m = nM\) and \(M = m/n\).
:::

:::warn Say which particles you mean
"One mole of chlorine" is ambiguous. One mole of chlorine **molecules**, \(\ce{Cl2}\), has a mass of 71.0 g and contains \(6.022 \times 10^{23}\) molecules, which is \(1.204 \times 10^{24}\) atoms. One mole of chlorine **atoms**, Cl, has a mass of 35.5 g. Always say "molecules" or "atoms" (or give the formula) in a calculation.
:::

:::eg How many molecules, and how many atoms, are in 36.0 g of water?
\(M_r(\ce{H2O}) = 18.0\), so \(M = 18.0\,\mathrm{g\,mol^{-1}}\).
\[n = \frac{36.0}{18.0} = 2.00\,\mathrm{mol}\]
\[N(\text{molecules}) = 2.00 \times 6.022 \times 10^{23} = 1.20 \times 10^{24}\]
Each molecule has three atoms (two H, one O), so \(N(\text{atoms}) = 3 \times 1.2044 \times 10^{24} = 3.61 \times 10^{24}\).
:::

:::eg (Exam style) Calculate the number of sulfate ions in 5.00 g of aluminium sulfate, \(\ce{Al2(SO4)3}\). [4 marks]
\[M_r(\ce{Al2(SO4)3}) = 2(27.0) + 3(32.1 + 4 \times 16.0) = 342.3\] [B1]
\[n = \frac{5.00}{342.3} = 0.014607\,\mathrm{mol}\] [M1]
Each formula unit contains 3 sulfate ions, so \(n(\ce{SO4^2-}) = 3 \times 0.014607 = 0.043821\) mol. [M1]
\[N = 0.043821 \times 6.022 \times 10^{23} = 2.64 \times 10^{22}\] [A1]
:::

## Formulas and equations

### Ionic formulas

An ionic compound has no overall charge, so the charges of its ions must add up to zero. You can predict the charge of the simple ions from the Periodic Table.

| Group | 1 | 2 | 13 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|
| Ion formed | \(1+\) | \(2+\) | \(3+\) | \(3-\) | \(2-\) | \(1-\) |
| Example | \(\ce{Na+}\) | \(\ce{Mg^2+}\) | \(\ce{Al^3+}\) | \(\ce{N^3-}\) | \(\ce{O^2-}\) | \(\ce{Cl-}\) |

Transition elements form ions of more than one charge, so the charge is written in the name as a **Roman numeral**: iron(II) is \(\ce{Fe^2+}\) and iron(III) is \(\ce{Fe^3+}\). (The numeral is the oxidation number, which [Redox](#chem.redox) explains.) You must also **recall** these ions:

| Name | Formula | Name | Formula |
|---|---|---|---|
| nitrate | \(\ce{NO3-}\) | hydroxide | \(\ce{OH-}\) |
| carbonate | \(\ce{CO3^2-}\) | ammonium | \(\ce{NH4+}\) |
| sulfate | \(\ce{SO4^2-}\) | zinc | \(\ce{Zn^2+}\) |
| hydrogencarbonate | \(\ce{HCO3-}\) | silver | \(\ce{Ag+}\) |
| phosphate | \(\ce{PO4^3-}\) | | |

To write the formula, balance the charges with the smallest numbers of each ion, and put brackets round a polyatomic ion if you need more than one.

:::steps
1. Write each ion with its charge: \(\ce{Al^3+}\) and \(\ce{SO4^2-}\).
2. Find the smallest numbers that make the total charge zero: 2 aluminium ions give 6+, and 3 sulfate ions give 6−.
3. Write the formula with brackets round the polyatomic ion: \(\ce{Al2(SO4)3}\).
:::

Other examples: iron(III) oxide is \(\ce{Fe^3+}\) and \(\ce{O^2-}\), so 2 and 3 ions make 6+ and 6−: \(\ce{Fe2O3}\). Ammonium phosphate is \(\ce{(NH4)3PO4}\), calcium hydroxide is \(\ce{Ca(OH)2}\), zinc nitrate is \(\ce{Zn(NO3)2}\), and silver carbonate is \(\ce{Ag2CO3}\).

### Balanced and ionic equations

A balanced equation has the same number of each kind of atom on both sides (and the same total charge, if ions are present). Balance by changing the **coefficients** in front of the formulas, never the formulas themselves. **State symbols** show the physical state: (s), (l), (g), and (aq) for dissolved in water.

\[\ce{Fe2O3(s) + 3CO(g) -> 2Fe(s) + 3CO2(g)}\]

In water, ionic compounds that dissolve split into ions. An **ionic equation** shows only the ions or molecules that actually change. The ions that are the same on both sides are **spectator ions**, which take no part in the reaction and are left out.

:::steps
1. Write the balanced equation with state symbols.
2. Write every soluble ionic compound, and strong acid (one that splits completely into ions in water; Acids and bases explains this), as separate ions, with (aq). Leave solids, liquids, gases and water as formulas.
3. Cancel the ions that appear unchanged on both sides (the spectators).
4. Check that the atoms and the charges balance.
:::

A question normally gives the state symbols; if it does not, use these rules. All nitrates, and all sodium, potassium and ammonium salts, dissolve. The insoluble precipitates met here are the silver halides (AgCl, AgBr, AgI) and barium sulfate, BaSO₄.

:::eg Write the ionic equation for the reaction of aqueous barium chloride with aqueous sodium sulfate.
Full equation: \(\ce{BaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2NaCl(aq)}\)

In ions: \(\ce{Ba^2+(aq) + 2Cl-(aq) + 2Na+(aq) + SO4^2-(aq) -> BaSO4(s) + 2Na+(aq) + 2Cl-(aq)}\)

The sodium ions and chloride ions are the same on both sides, so they are spectators. Remove them:
\[\ce{Ba^2+(aq) + SO4^2-(aq) -> BaSO4(s)}\]
Atoms balance, and the charges balance (2+ and 2− on the left give 0, and BaSO₄ has no charge).
:::

Three ionic equations occur all through the course:

\[\ce{Ag+(aq) + Cl-(aq) -> AgCl(s)}\]
\[\ce{H+(aq) + OH-(aq) -> H2O(l)}\]
\[\ce{Mg(s) + 2H+(aq) -> Mg^2+(aq) + H2(g)}\]

The first is the test for chloride ions, the second is neutralisation (any strong acid with any strong alkali), and the third is a metal reacting with an acid. In the third equation the spectator ion is the anion of the acid, for example chloride in hydrochloric acid.

:::warn Spectators, charge and state symbols
Leave solids, liquids and gases whole: writing \(\ce{BaSO4(s)}\) as \(\ce{Ba^2+ + SO4^2-}\) cancels the whole reaction. And the total charge must balance as well as the atoms: \(\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\) is balanced, but \(\ce{Zn + Cu^2+ -> Zn^+ + Cu}\) is not.
:::

## Empirical and molecular formulas

:::def Empirical formula
The simplest whole-number ratio of the atoms of each element in a compound.
:::

:::def Molecular formula
The actual number of atoms of each element in one molecule of the compound.
:::

Glucose has the molecular formula \(\ce{C6H12O6}\) and the empirical formula \(\ce{CH2O}\). For ionic compounds the empirical formula is the formula, for example \(\ce{NaCl}\).

### Percentage by mass

The percentage of an element in a compound is the mass of that element in one mole divided by the molar mass of the compound, times 100.

:::eg (Real context) Ammonium sulfate, \(\ce{(NH4)2SO4}\), is a fertiliser. Calculate the percentage of nitrogen by mass.
\(M_r(\ce{(NH4)2SO4}) = 2(14.0 + 4 \times 1.0) + 32.1 + 4 \times 16.0 = 132.1\) [B1]

One mole contains 2 mol of N atoms, with mass \(2 \times 14.0 = 28.0\) g.
\[\%\,\mathrm{N} = \frac{28.0}{132.1} \times 100 = 21.2\,\%\] [M1] [A1]
:::

### From percentages (or masses) to the formula

:::steps
1. Write the mass (or percentage) of each element.
2. Divide each by its \(A_r\) to get the amount in mol (or, for a percentage, per 100 g).
3. Divide all the amounts by the smallest one.
4. If the ratio is not whole numbers, multiply all by the smallest factor that makes them whole (×2 for a .5, ×3 for a .33 or .67).
5. For the molecular formula, divide the given \(M_r\) by the empirical formula mass and multiply the formula by the answer.
:::

:::eg A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% oxygen by mass, and its \(M_r\) is 180. Find its empirical formula and molecular formula.
Take 100 g, so the masses are 40.0 g, 6.7 g and 53.3 g.

| | C | H | O |
|---|---|---|---|
| mass / g | 40.0 | 6.7 | 53.3 |
| amount / mol (÷ \(A_r\)) | 3.333 | 6.7 | 3.331 |
| ratio (÷ 3.331) | 1.00 | 2.01 | 1.00 |

The ratio is C : H : O = 1 : 2 : 1, so the empirical formula is \(\ce{CH2O}\).

Empirical formula mass = 12.0 + 2(1.0) + 16.0 = 30.0. \(180 / 30.0 = 6\), so the molecular formula is \(\ce{C6H12O6}\).
:::

:::eg 69.9% iron and 30.1% oxygen by mass: find the empirical formula of the iron oxide.
\(n(\mathrm{Fe}) = 69.9 / 55.8 = 1.2527\) and \(n(\mathrm{O}) = 30.1 / 16.0 = 1.8813\) (per 100 g).

Dividing by the smaller: Fe = 1.00 and O = 1.502. This is not a whole-number ratio, but it is 1 : 1.5, so multiply by 2: Fe : O = 2 : 3.

The empirical formula is \(\ce{Fe2O3}\). (Never round 1.5 to 1 or 2.)
:::

When the data are masses from an experiment, the same method works. When 2.43 g of magnesium burns in oxygen, the product weighs 4.03 g, so the mass of oxygen gained is 4.03 − 2.43 = 1.60 g. Then \(n(\mathrm{Mg}) = 2.43 / 24.3 = 0.100\) and \(n(\mathrm{O}) = 1.60 / 16.0 = 0.100\): a 1 : 1 ratio, and the empirical formula is MgO.

**Combustion data.** A compound containing only carbon and hydrogen is burned completely, so all its carbon goes to \(\ce{CO2}\) and all its hydrogen goes to \(\ce{H2O}\). From the masses of these, you can find the moles of C and H.

:::eg (Exam style) 0.350 g of a hydrocarbon burns completely to give 1.10 g of carbon dioxide and 0.450 g of water. Its \(M_r\) is 70.0. Find its molecular formula. [5 marks]
\(M_r(\ce{CO2}) = 44.0\) and \(M_r(\ce{H2O}) = 18.0\). [B1]
\[n(\ce{CO2}) = \frac{1.10}{44.0} = 0.02500\,\mathrm{mol} \quad\Rightarrow\quad n(\mathrm{C}) = 0.02500\,\mathrm{mol}\] [M1]
\[n(\ce{H2O}) = \frac{0.450}{18.0} = 0.02500\,\mathrm{mol} \quad\Rightarrow\quad n(\mathrm{H}) = 2 \times 0.02500 = 0.05000\,\mathrm{mol}\] [M1]
The ratio C : H = 0.02500 : 0.05000 = 1 : 2, so the empirical formula is \(\ce{CH2}\) (mass 14.0). [A1]

\(70.0 / 14.0 = 5\), so the molecular formula is \(\ce{C5H10}\). [A1]
:::

### Water of crystallisation

Many salts crystallise from water with water molecules built into the crystal in a fixed ratio.

:::def Water of crystallisation
Water molecules that are part of the crystal structure of a compound, in a fixed ratio to the other ions. A compound that has them is **hydrated**; one without them is **anhydrous**.
:::

Copper(II) sulfate crystals are \(\ce{CuSO4.5H2O}\) (blue and hydrated), and heating drives the water off to give white anhydrous \(\ce{CuSO4}\). The dot in the formula means "combined with", and the 5 multiplies only the \(\ce{H2O}\). So \(M_r(\ce{CuSO4.5H2O}) = 63.5 + 32.1 + 4(16.0) + 5(18.0) = 249.6\).

Try the calculator below with \(\ce{CuSO4.5H2O}\) to see each atom's contribution to the mass, and then with other formulas.

:::html
<div class="widget" data-w="molar" data-formula="CuSO4.5H2O"></div>
:::

:::lab Finding the water of crystallisation by heating
Weigh a clean, dry crucible. Add 2–3 g of the hydrated salt and weigh again to find its mass (balance reading to 0.01 g). Heat the crucible gently, then strongly, on a pipe-clay triangle. Let it cool, then weigh. **Heat again and reweigh until two readings agree: this is "heating to constant mass"**, and it shows that all the water has gone. The mass lost is the mass of water. Wear eye protection, and do not touch the hot crucible.
:::

:::html
<figure class="fig small"><svg viewBox="0 20 350 170" role="img" aria-label="Heating a hydrated salt: a crucible holding the salt rests in a pipe-clay triangle with heat below"><path class="ln" d="M102 50L115 104H165L178 50"/><path class="fm2" d="M110.2 84L115 104H165L169.8 84Z"/><path class="ln thick" d="M80 72H200"/><path class="c2 sw2" d="M140 175V125" marker-end="url(#ah)"/><text class="tl" x="152" y="160">heat</text><path class="ln-m thin" d="M181 54L206 46"/><text class="tl" x="211" y="48">crucible</text><path class="ln-m thin" d="M203 72L208 72"/><text class="tl" x="212" y="76">pipe-clay triangle</text><path class="ln-m thin" d="M138 94H100"/><text class="tl" x="94" y="98" text-anchor="end">hydrated salt</text></svg><figcaption>Heating a hydrated salt in a crucible. The crucible sits in a pipe-clay triangle. Heating, cooling and weighing are repeated until the mass stops changing.</figcaption></figure>
:::

:::eg (Exam style) 2.46 g of hydrated magnesium sulfate, \(\ce{MgSO4.xH2O}\), is heated until all the water has gone. 1.20 g of anhydrous \(\ce{MgSO4}\) remains. Find \(x\). [4 marks]
\(M_r(\ce{MgSO4}) = 24.3 + 32.1 + 4(16.0) = 120.4\) [B1]
\[n(\ce{MgSO4}) = \frac{1.20}{120.4} = 0.009967\,\mathrm{mol}\] [M1]
Mass of water lost = 2.46 − 1.20 = 1.26 g.
\[n(\ce{H2O}) = \frac{1.26}{18.0} = 0.0700\,\mathrm{mol}\] [M1]
\[x = \frac{0.0700}{0.009967} = 7.02 \approx 7\] [A1]
The formula is \(\ce{MgSO4.7H2O}\).
:::

## Reacting masses and percentage yield

A balanced equation tells you the **ratio in moles** in which substances react. This is the central idea of the chapter. The coefficients are mole ratios, not mass ratios.

:::key The method for every reacting-mass question
1. Write the balanced equation.
2. Convert the given mass to moles: \(n = m / M\).
3. Use the equation ratio to find the moles of the substance you want.
4. Convert to mass (or volume, or concentration) as asked.
:::

The **mole map** below shows every conversion in the chapter. The amount in moles is always in the middle: to get from one quantity to another, go in to the moles and then out again. The balanced equation is what connects the moles of one substance to the moles of another.

:::html
<figure class="fig"><svg viewBox="0 0 600 255" role="img" aria-label="Mole map: amount in moles at the centre, with mass, number of particles, gas volume and concentration around it, and the operation on each arrow"><rect class="f1 s-acc sw2" x="240" y="100" width="120" height="50" rx="8"/><text class="tl tc" x="300" y="129">amount, n / mol</text><rect class="fm" x="20" y="100" width="125" height="50" rx="8"/><text class="tl tc" x="82.5" y="129">mass, m / g</text><rect class="fm" x="455" y="100" width="125" height="50" rx="8"/><text class="tl tc" x="517.5" y="129">gas volume / dm³</text><rect class="fm" x="225" y="5" width="150" height="40" rx="8"/><text class="tl tc" x="300" y="29">number of particles</text><rect class="fm" x="205" y="205" width="190" height="40" rx="8"/><text class="tl tc" x="300" y="229">concentration / mol dm⁻³</text><path class="ln" d="M155 113H230" marker-end="url(#ah)"/><text class="tl tc" x="192" y="107">÷ M</text><path class="ln" d="M230 137H155" marker-end="url(#ah)"/><text class="tl tc" x="192" y="156">× M</text><path class="ln" d="M370 113H445" marker-end="url(#ah)"/><text class="tl tc" x="407" y="107">× 24.0</text><path class="ln" d="M445 137H370" marker-end="url(#ah)"/><text class="tl tc" x="407" y="156">÷ 24.0</text><path class="ln" d="M280 90V55" marker-end="url(#ah)"/><text class="tl" x="272" y="76" text-anchor="end">× L</text><path class="ln" d="M320 55V90" marker-end="url(#ah)"/><text class="tl" x="328" y="76">÷ L</text><path class="ln" d="M280 160V195" marker-end="url(#ah)"/><text class="tl" x="272" y="182" text-anchor="end">÷ V</text><path class="ln" d="M320 195V160" marker-end="url(#ah)"/><text class="tl" x="328" y="182">× V</text></svg><figcaption>The mole map. \(M\) is the molar mass, \(L\) the Avogadro constant, 24.0 dm³ mol⁻¹ the molar gas volume at room conditions, and \(V\) the volume of solution in dm³. Going down from the moles divides by \(V\) to give the concentration; coming up multiplies by \(V\).</figcaption></figure>
:::

:::eg (Real context) Limestone (calcium carbonate) is heated in a lime kiln: \(\ce{CaCO3 -> CaO + CO2}\). What mass of calcium oxide forms from 25.0 g of calcium carbonate?
\(M_r(\ce{CaCO3}) = 40.1 + 12.0 + 3(16.0) = 100.1\) and \(M_r(\ce{CaO}) = 40.1 + 16.0 = 56.1\). [B1]
\[n(\ce{CaCO3}) = \frac{25.0}{100.1} = 0.2498\,\mathrm{mol}\] [M1]
The ratio is 1 : 1, so \(n(\ce{CaO}) = 0.2498\) mol.
\[m(\ce{CaO}) = 0.2498 \times 56.1 = 14.0\,\mathrm{g}\] [M1] [A1]
:::

:::eg (Real context) Petrol is mainly octane, \(\ce{C8H18}\): \(\ce{2C8H18 + 25O2 -> 16CO2 + 18H2O}\). What mass of carbon dioxide is released by burning 1.00 kg of octane?
\(M_r(\ce{C8H18}) = 8(12.0) + 18(1.0) = 114.0\), and \(M_r(\ce{CO2}) = 44.0\).
\[n(\ce{C8H18}) = \frac{1000}{114.0} = 8.772\,\mathrm{mol}\]
From the equation, 2 mol of octane give 16 mol of \(\ce{CO2}\): the ratio is 1 : 8, so \(n(\ce{CO2}) = 8 \times 8.772 = 70.18\) mol.
\[m(\ce{CO2}) = 70.18 \times 44.0 = 3088\,\mathrm{g} = 3.09\,\mathrm{kg}\]
One kilogram of petrol releases more than three kilograms of carbon dioxide, because each carbon atom joins with two oxygen atoms from the air.
:::

### Percentage yield

The **theoretical yield** is the mass of product the equation says you should get. The **actual yield** is what you collect. It is usually less, because some product is lost in transfers and filtering, some reactions do not go to completion, and side reactions occur.

:::formula Percentage yield
\[\text{percentage yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100\]
Both yields must be in the same unit (grams, or moles).
:::

:::eg (Real context) Aspirin is made from salicylic acid: \(\ce{C7H6O3 + (CH3CO)2O -> C9H8O4 + CH3COOH}\). 2.00 g of salicylic acid gave 2.30 g of aspirin. Calculate the percentage yield.
\(M_r(\ce{C7H6O3}) = 138.0\) and \(M_r(\ce{C9H8O4}) = 180.0\). [B1]
\[n(\ce{C7H6O3}) = \frac{2.00}{138.0} = 0.01449\,\mathrm{mol}\] [M1]
The ratio is 1 : 1, so the theoretical yield is \(0.01449 \times 180.0 = 2.609\) g. [M1]
\[\text{percentage yield} = \frac{2.30}{2.609} \times 100 = 88.2\,\%\] [A1]
:::

:::board
AQA also asks for percentage atom economy calculations, which compare the mass of the useful product with the total mass of all the products. Atom economy is not in the Cambridge 9701 learning outcomes.
:::

## Gas volumes

Avogadro realised that equal volumes of different gases, at the same temperature and pressure, contain the same number of molecules. So the volume of a gas depends on the amount in moles, not on what the gas is. At **room temperature and pressure** one mole of any gas occupies **24.0 dm³**, and at standard temperature and pressure (s.t.p., 273 K and 101 kPa) one mole occupies 22.4 dm³. Use 24.0 unless the question says s.t.p.

:::formula Gas volume
\[V = n \times 24.0\,\mathrm{dm^3} \quad\text{(room conditions)}\]
\(V\) is in dm³. To get cm³, multiply by 1000. Gases measured at the same temperature and pressure react in the ratio of their mole coefficients, so a volume ratio equals a mole ratio.
:::

:::eg 2.43 g of magnesium reacts with excess hydrochloric acid. Calculate the volume of hydrogen formed at room temperature and pressure.
\(\ce{Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)}\)

\(n(\mathrm{Mg}) = 2.43 / 24.3 = 0.100\) mol. The ratio is 1 : 1, so \(n(\ce{H2}) = 0.100\) mol.
\[V = 0.100 \times 24.0 = 2.40\,\mathrm{dm^3} = 2400\,\mathrm{cm^3}\]
:::

:::eg 2.00 g of calcium carbonate reacts with excess acid and the carbon dioxide is collected in a gas syringe. What volume does it fill?
\(\ce{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}\)

\(n(\ce{CaCO3}) = 2.00 / 100.1 = 0.01998\) mol, which equals \(n(\ce{CO2})\).
\[V = 0.01998 \times 24.0 = 0.4795\,\mathrm{dm^3} = 480\,\mathrm{cm^3}\]
A gas syringe of volume 100 cm³ is too small for this: use a larger one or less carbonate.
:::

For the conditions in which gases are not at room temperature and pressure, you use \(pV = nRT\), covered in [States of matter](#chem.states).

### Burning hydrocarbons

Because volume ratios are mole ratios, the volumes of gases in a combustion experiment give the formula directly. Water formed in the experiment condenses to a liquid when the gases cool to room temperature, so only the remaining gases count. Carbon dioxide is absorbed by sodium hydroxide solution, so the volume it removes is the volume of \(\ce{CO2}\).

:::eg (Exam style) 10 cm³ of a gaseous hydrocarbon \(\ce{C_xH_y}\) is mixed with 60 cm³ of oxygen, which is in excess, and burned. After cooling to room temperature the gas volume is 40 cm³. Shaking with aqueous sodium hydroxide reduces it to 10 cm³. Deduce the formula of the hydrocarbon. [5 marks]
The volume absorbed by sodium hydroxide is the carbon dioxide: 40 − 10 = 30 cm³. [B1]
10 cm³ of hydrocarbon gives 30 cm³ of \(\ce{CO2}\), so each molecule has 3 carbon atoms: \(x = 3\). [M1]
The 10 cm³ left is unused oxygen, so oxygen used = 60 − 10 = 50 cm³. [B1]
Count the oxygen atoms: 50 volumes of \(\ce{O2}\) is 100 volumes of O atoms. 30 volumes of \(\ce{CO2}\) use 60 of them, so the other 40 are in water: 40 volumes of \(\ce{H2O}\). [M1]
40 volumes of \(\ce{H2O}\) contain 80 volumes of H atoms, which came from 10 volumes of hydrocarbon, so \(y = 8\): \(\ce{C3H8}\). [A1]

Check with the equation \(\ce{C3H8 + 5O2 -> 3CO2 + 4H2O}\): for 10 cm³ of \(\ce{C3H8}\), 50 cm³ of \(\ce{O2}\) is used and 30 cm³ of \(\ce{CO2}\) is formed. ✓
:::

## Solutions and titrations

Many reactions take place in solution. The **concentration** of a solution is the amount of solute in a given volume.

:::formula Concentration
\[c = \frac{n}{V}\qquad n = cV\qquad c\,(\mathrm{g\,dm^{-3}}) = c\,(\mathrm{mol\,dm^{-3}}) \times M\]
\(c\) is in mol dm⁻³, \(n\) in mol and \(V\) in **dm³**. Convert cm³ to dm³ by dividing by 1000.
:::

:::eg 4.00 g of sodium hydroxide is dissolved in water and made up to 250 cm³. What is the concentration in (a) mol dm⁻³ and (b) g dm⁻³?
\(M(\mathrm{NaOH}) = 23.0 + 16.0 + 1.0 = 40.0\,\mathrm{g\,mol^{-1}}\).

(a) \(n = 4.00 / 40.0 = 0.100\) mol and \(V = 250 / 1000 = 0.250\) dm³.
\[c = \frac{0.100}{0.250} = 0.400\,\mathrm{mol\,dm^{-3}}\]
(b) \(0.400 \times 40.0 = 16.0\,\mathrm{g\,dm^{-3}}\), or directly: 4.00 g in 0.250 dm³ is 4.00 / 0.250 = 16.0 g dm⁻³.
:::

### Titration

A **titration** measures the volume of one solution needed to react exactly with a known volume of another. The solution in the burette is added to the one in the flask until an **indicator** changes colour at the **end-point**, where the amounts are in the ratio of the equation.

:::html
<figure class="fig small"><svg viewBox="0 6 330 290" role="img" aria-label="Titration apparatus: a burette with a tap above a conical flask containing alkali and indicator"><path class="fa" d="M150 70H166V150H150Z"/><path class="ln" d="M150 20V150M166 20V150"/><path class="ln" d="M142 150H174"/><path class="ln" d="M156 150V176M160 150V176"/><path class="ln" d="M146 205V225L112 270H204L170 225V205"/><path class="fa" d="M127.1 250H188.9L204 270H112Z"/><path class="ln-m thin" d="M170 100H205"/><text class="tl" x="210" y="104">burette</text><path class="ln-m thin" d="M178 150H205"/><text class="tl" x="210" y="154">tap</text><path class="ln-m thin" d="M124 258H104"/><text class="tl" x="98" y="250" text-anchor="end">alkali and</text><text class="tl" x="98" y="266" text-anchor="end">indicator</text><path class="ln-m thin" d="M146 215H104"/><text class="tl" x="98" y="219" text-anchor="end">conical flask</text></svg><figcaption>A titration. The burette delivers one solution to the flask a little at a time. A pipette puts an exact volume of the other solution, with a few drops of indicator, into the flask.</figcaption></figure>
:::

:::lab Carrying out a titration
Use a **pipette** to transfer 25.0 cm³ of one solution into a conical flask and add a few drops of indicator. Fill the burette with the other solution and read the starting volume. Do a rough titration to find the approximate end-point. Then repeat, adding the last few cm³ drop by drop, and record the burette reading to 0.05 cm³. The **titre** is the volume added. Repeat until two or more titres are **concordant** (within 0.10 cm³ of one another) and take the mean of those. Wear eye protection.
:::

:::eg (Exam style) 25.0 cm³ of sodium hydroxide solution is neutralised by 21.40 cm³ of 0.100 mol dm⁻³ hydrochloric acid. Calculate the concentration of the sodium hydroxide. [3 marks]
\(\ce{NaOH + HCl -> NaCl + H2O}\)
\[n(\mathrm{HCl}) = 0.100 \times \frac{21.40}{1000} = 0.002140\,\mathrm{mol}\] [M1]
The ratio is 1 : 1, so \(n(\mathrm{NaOH}) = 0.002140\) mol. [M1]
\[c(\mathrm{NaOH}) = \frac{0.002140}{0.0250} = 0.0856\,\mathrm{mol\,dm^{-3}}\] [A1]
:::

When the ratio is not 1 : 1, the ratio step matters.

:::eg 25.0 cm³ of 0.200 mol dm⁻³ sulfuric acid is neutralised by 0.500 mol dm⁻³ sodium hydroxide. What volume of sodium hydroxide is needed?
\(\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}\)

\(n(\ce{H2SO4}) = 0.200 \times 0.0250 = 0.00500\) mol.

The ratio is 1 : 2, so \(n(\mathrm{NaOH}) = 2 \times 0.00500 = 0.0100\) mol.
\[V = \frac{n}{c} = \frac{0.0100}{0.500} = 0.0200\,\mathrm{dm^3} = 20.0\,\mathrm{cm^3}\]
:::

### Back titration

Sometimes the substance does not dissolve or reacts too slowly to titrate directly, such as the calcium carbonate in an antacid tablet. In a **back titration** you add a measured **excess** of a reagent, let it react, and then titrate what is left over.

:::eg (Exam style, ★★★) A 0.500 g antacid tablet containing calcium carbonate is crushed and added to 25.0 cm³ of 0.200 mol dm⁻³ hydrochloric acid, which is in excess. The excess acid needs 12.40 cm³ of 0.100 mol dm⁻³ sodium hydroxide for neutralisation. Calculate the percentage by mass of \(\ce{CaCO3}\) in the tablet. [6 marks]
\(n(\mathrm{HCl\ added}) = 0.200 \times 0.0250 = 0.00500\) mol [B1]
\(n(\mathrm{NaOH}) = 0.100 \times 0.01240 = 0.001240\) mol, and the ratio with HCl is 1 : 1, so the excess HCl is 0.001240 mol. [M1]
\(n(\mathrm{HCl\ reacted\ with\ CaCO_3}) = 0.00500 - 0.001240 = 0.003760\) mol [M1]
\(\ce{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}\): 2 mol of HCl react with 1 mol of \(\ce{CaCO3}\). So \(n(\ce{CaCO3}) = 0.003760 / 2 = 0.001880\) mol. [M1]
\[m(\ce{CaCO3}) = 0.001880 \times 100.1 = 0.1882\,\mathrm{g}\] [M1]
\[\%\ \ce{CaCO3} = \frac{0.1882}{0.500} \times 100 = 37.6\,\%\] [A1]
:::

## Limiting and excess reagents

When two reactants are mixed, one may run out first. That one is the **limiting reagent**: it decides how much product forms. The other is in **excess**, and some of it is left over.

:::steps
1. Convert the mass or volume of each reactant to moles.
2. Divide each amount by its coefficient in the balanced equation.
3. The reactant with the smaller value is the limiting reagent.
4. Do the rest of the calculation (product amount, product mass or volume) from the limiting reagent. The excess left over is its starting amount minus the amount that reacted.
:::

:::eg 6.00 g of magnesium is added to 60.0 cm³ of 2.00 mol dm⁻³ hydrochloric acid. (a) Which reagent is limiting? (b) What volume of hydrogen forms at room temperature and pressure? (c) What mass of magnesium is left?
\(\ce{Mg + 2HCl -> MgCl2 + H2}\)

(a) \(n(\mathrm{Mg}) = 6.00 / 24.3 = 0.2469\) mol and \(n(\mathrm{HCl}) = 2.00 \times 0.0600 = 0.120\) mol.

Dividing by the coefficients: Mg \(0.2469 / 1 = 0.2469\); HCl \(0.120 / 2 = 0.0600\). The smaller is HCl, so **hydrochloric acid is limiting**.

(b) \(n(\ce{H2}) = \tfrac12 \times 0.120 = 0.0600\) mol, and \(V = 0.0600 \times 24.0 = 1.44\,\mathrm{dm^3}\).

(c) Magnesium reacted = 0.0600 mol \(= 0.0600 \times 24.3 = 1.458\) g, so magnesium left = 6.00 − 1.458 = 4.54 g.
:::

## Stoichiometry from experimental data

**Stoichiometry** means the amounts of substances in a reaction, as shown by the coefficients of the balanced equation. You can also work backwards: find the ratio from experimental amounts, and from the ratio find the equation or the formula.

:::eg 25.0 cm³ of 0.100 mol dm⁻³ of an acid, \(\ce{H_xA}\), is neutralised by 50.0 cm³ of 0.100 mol dm⁻³ sodium hydroxide. How many hydrogen ions does each molecule release?
\(n(\ce{H_xA}) = 0.100 \times 0.0250 = 0.00250\) mol. \(n(\ce{OH-}) = 0.100 \times 0.0500 = 0.00500\) mol.

Ratio acid : hydroxide = 0.00250 : 0.00500 = 1 : 2. Each \(\ce{OH-}\) removes one \(\ce{H+}\), so each acid molecule gives 2 \(\ce{H+}\): the acid is \(\ce{H2A}\), a dibasic acid (each molecule can release two \(\ce{H+}\)).
:::

:::eg 20 cm³ of a gas X reacts with 10 cm³ of oxygen to give 20 cm³ of a gaseous product, all volumes at the same temperature and pressure. Deduce the ratio X : O₂ : product.
Volume ratios are mole ratios: 20 : 10 : 20 = 2 : 1 : 2. So the equation has the form \(\ce{2X + O2 -> 2Y}\), where Y is the product. An example with this ratio is \(\ce{2NO + O2 -> 2NO2}\), in which X is nitrogen monoxide.
:::

:::exam Calculation technique for full marks
Write the balanced equation first, and the unit and the \(M_r\) at each step. Keep four or more significant figures through the working and round only the final answer, to the number of significant figures of the data (usually 3). Put the unit in the final answer. Convert cm³ to dm³ before you divide. Examiners award the method mark even if an earlier slip carries through, so show every step.
:::

:::eg Spot the error: 25.0 cm³ of 0.100 mol dm⁻³ sodium carbonate is titrated against hydrochloric acid, and 20.0 cm³ of acid is needed. Calculate the concentration of the acid. [4 marks]
A student wrote this answer.

Line 1: \(\ce{Na2CO3 + 2HCl -> 2NaCl + H2O + CO2}\)
Line 2: \(n(\ce{Na2CO3}) = 0.100 \times 0.0250 = 0.00250\) mol
Line 3: \(n(\mathrm{HCl}) = 0.00250\) mol
Line 4: \(c(\mathrm{HCl}) = 0.00250 / 0.0200 = 0.125\,\mathrm{mol\,dm^{-3}}\)

Line 1 is correct [B1]. Line 2 is correct, with the volume converted to dm³ [M1]. **Line 3 is wrong: the equation shows 2 mol of HCl for every 1 mol of \(\ce{Na2CO3}\), so \(n(\mathrm{HCl}) = 2 \times 0.00250 = 0.00500\) mol. The ratio step is missing [M0].** Line 4 divides by the right volume in dm³, but the wrong amount gives a wrong answer [A0].

Correct lines: \(n(\mathrm{HCl}) = 0.00500\) mol, so \(c = 0.00500 / 0.0200 = 0.250\) mol dm⁻³. [M1] [A1]

The student scores 2 out of 4. Every titration answer should have a line that shows the ratio from the equation.
:::

:::try Start easy, finish at exam standard
Q: Calculate \(M_r\) for (a) \(\ce{CaCO3}\), (b) \(\ce{(NH4)2SO4}\), (c) \(\ce{MgSO4.7H2O}\).
A: (a) 40.1 + 12.0 + 48.0 = 100.1. (b) 2(14.0 + 4.0) + 32.1 + 64.0 = 132.1. (c) 24.3 + 32.1 + 64.0 + 7(18.0) = 246.4.
Q: Calculate the amount in mol in (a) 8.00 g of sodium hydroxide, (b) 0.250 g of copper.
A: (a) \(M = 40.0\), so \(n = 8.00 / 40.0 = 0.200\) mol. (b) \(n = 0.250 / 63.5 = 0.00394\) mol.
Q: Copper has two isotopes, \({}^{63}\mathrm{Cu}\) and \({}^{65}\mathrm{Cu}\), and \(A_r = 63.5\). What is the percentage of \({}^{63}\mathrm{Cu}\)?
A: Let \(x\) be the percentage of \({}^{63}\mathrm{Cu}\): \(63x + 65(100 - x) = 6350\), so \(6500 - 2x = 6350\) and \(x = 75\%\).
Q: Write the formulas of (a) iron(II) sulfate, (b) iron(III) sulfate, (c) ammonium carbonate, (d) silver nitrate.
A: (a) \(\ce{FeSO4}\). (b) \(\ce{Fe2(SO4)3}\). (c) \(\ce{(NH4)2CO3}\). (d) \(\ce{AgNO3}\).
Q: Write the ionic equation for aqueous silver nitrate with aqueous sodium bromide.
A: \(\ce{Ag+(aq) + Br-(aq) -> AgBr(s)}\); the nitrate and sodium ions are spectators.
Q: A compound contains 85.7% carbon and 14.3% hydrogen by mass and has \(M_r = 84.0\). Find its molecular formula.
A: C: 85.7 / 12.0 = 7.142; H: 14.3 / 1.0 = 14.3; ratio 1 : 2, empirical formula \(\ce{CH2}\) (mass 14.0). 84.0 / 14.0 = 6, so \(\ce{C6H12}\).
Q: 0.654 g of zinc reacts with excess dilute sulfuric acid. What volume of hydrogen forms at room temperature and pressure? Give the answer in cm³.
A: \(\ce{Zn + H2SO4 -> ZnSO4 + H2}\). \(n(\mathrm{Zn}) = 0.654 / 65.4 = 0.0100\) mol, so \(n(\ce{H2}) = 0.0100\) mol and \(V = 0.0100 \times 24.0 = 0.240\) dm³ = 240 cm³.
Q: Calculate the concentration, in mol dm⁻³, of a solution containing 5.85 g of sodium chloride in 500 cm³.
A: \(M = 23.0 + 35.5 = 58.5\); \(n = 5.85 / 58.5 = 0.100\) mol; \(c = 0.100 / 0.500 = 0.200\) mol dm⁻³.
Q: Find the mass of oxygen needed to burn 6.00 g of carbon completely to carbon dioxide.
A: \(\ce{C + O2 -> CO2}\). \(n(\mathrm{C}) = 6.00 / 12.0 = 0.500\) mol, so \(n(\ce{O2}) = 0.500\) mol, and the mass is \(0.500 \times 32.0 = 16.0\) g.
Q: 0.200 mol of aluminium reacts with 0.240 mol of chlorine: \(\ce{2Al + 3Cl2 -> 2AlCl3}\). Which is limiting?
A: Al: 0.200 / 2 = 0.100. \(\ce{Cl2}\): 0.240 / 3 = 0.0800. The smaller is chlorine, so chlorine is limiting.
Q: What is the percentage by mass of water in \(\ce{CuSO4.5H2O}\)?
A: \(5 \times 18.0 = 90.0\); \(M_r = 249.6\); \(90.0 / 249.6 \times 100 = 36.1\%\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the term relative atomic mass.
A: The weighted average mass of an atom of an element (taking account of its isotopes and their abundances) [B1] compared with one twelfth of the mass of an atom of carbon-12. [B1]
Q: [3 marks] ★ A compound contains 52.2% carbon, 13.0% hydrogen and 34.8% oxygen by mass. Calculate its empirical formula.
A: C: 52.2 / 12.0 = 4.35; H: 13.0 / 1.0 = 13.0; O: 34.8 / 16.0 = 2.175. [M1]
Divide by the smallest (2.175): C 2.0, H 5.98, O 1.0, so the ratio is 2 : 6 : 1. [M1]
Empirical formula \(\ce{C2H6O}\). [A1]
Q: [4 marks] ★★ 2.86 g of hydrated sodium carbonate, \(\ce{Na2CO3.xH2O}\), is heated to constant mass and leaves 1.06 g of anhydrous sodium carbonate. Find \(x\).
H: What mass of water was lost, and how many moles of it is that?
A: \(M_r(\ce{Na2CO3}) = 2(23.0) + 12.0 + 3(16.0) = 106.0\) [B1]
\(n(\ce{Na2CO3}) = 1.06 / 106.0 = 0.0100\) mol [M1]
Water lost = 2.86 − 1.06 = 1.80 g, so \(n(\ce{H2O}) = 1.80 / 18.0 = 0.100\) mol [M1]
\(x = 0.100 / 0.0100 = 10\) [A1]
Q: [5 marks] ★★ 25.0 cm³ of sulfuric acid is titrated with 0.100 mol dm⁻³ sodium hydroxide. The mean titre is 31.20 cm³. (a) Write the equation for the reaction. (b) Calculate the concentration of the acid in mol dm⁻³. (c) Convert this to g dm⁻³.
H: Work out the moles of sodium hydroxide first, then use the 1 : 2 ratio.
A: (a) \(\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}\) [B1]
(b) \(n(\mathrm{NaOH}) = 0.100 \times 0.03120 = 0.003120\) mol [M1]
\(n(\ce{H2SO4}) = 0.003120 / 2 = 0.001560\) mol, and \(c = 0.001560 / 0.0250 = 0.0624\) mol dm⁻³ [M1] [A1]
(c) \(M(\ce{H2SO4}) = 98.1\), so \(0.0624 \times 98.1 = 6.12\) g dm⁻³ [A1]
Q: [4 marks] ★★ 4.00 g of ethanol, \(\ce{C2H5OH}\), is heated with excess ethanoic acid and a catalyst of concentrated sulfuric acid to make ethyl ethanoate, \(\ce{CH3COOC2H5}\), and water. 5.10 g of ethyl ethanoate is obtained. Calculate the percentage yield.
H: One mole of ethanol makes one mole of ester.
A: \(M_r(\ce{C2H5OH}) = 46.0\) and \(M_r(\ce{CH3COOC2H5}) = 88.0\) [B1]
\(n(\mathrm{ethanol}) = 4.00 / 46.0 = 0.08696\) mol [M1]
Theoretical mass of ester = \(0.08696 \times 88.0 = 7.652\) g [M1]
Percentage yield = \(5.10 / 7.652 \times 100 = 66.6\,\%\) [A1]
Q: [5 marks] ★★★ 10 cm³ of a gaseous hydrocarbon is burned in 80 cm³ of oxygen (an excess). After the mixture has cooled to room temperature the volume is 60 cm³. Shaking with sodium hydroxide solution reduces it to 20 cm³. Deduce the molecular formula of the hydrocarbon.
H: What does the sodium hydroxide absorb, and what is the gas that remains?
H: Count the oxygen atoms used and share them between \(\ce{CO2}\) and \(\ce{H2O}\).
A: \(\ce{CO2}\) = 60 − 20 = 40 cm³, so carbon atoms per molecule = 40 / 10 = 4. [B1] [M1]
Oxygen left = 20 cm³, so oxygen used = 80 − 20 = 60 cm³, which is 120 cm³ of O atoms. [B1]
The \(\ce{CO2}\) contains 80 cm³ of O atoms, so the water contains 40 cm³ of O atoms, which is 40 cm³ of \(\ce{H2O}\), and so 80 cm³ of H atoms, or 8 per molecule of hydrocarbon. [M1]
The formula is \(\ce{C4H8}\). [A1]
Q: [6 marks] ★★★ 0.486 g of magnesium ribbon is added to 40.0 cm³ of 0.500 mol dm⁻³ hydrochloric acid. (a) Show that the acid is the limiting reagent. (b) Calculate the volume of hydrogen formed at room temperature and pressure, in cm³. (c) Calculate the mass of magnesium left.
H: Use \(\ce{Mg + 2HCl -> MgCl2 + H2}\) and divide each amount by its coefficient.
A: (a) \(n(\mathrm{Mg}) = 0.486 / 24.3 = 0.0200\) mol and \(n(\mathrm{HCl}) = 0.500 \times 0.0400 = 0.0200\) mol. [B1] [B1]
Magnesium needs 0.0400 mol of HCl to react completely, but only 0.0200 mol is present, so HCl is limiting. [M1]
(b) \(n(\ce{H2}) = 0.0200 / 2 = 0.0100\) mol [M1], and \(V = 0.0100 \times 24.0 = 0.240\,\mathrm{dm^3} = 240\,\mathrm{cm^3}\) [A1]
(c) Magnesium reacted = 0.0100 mol, so 0.0100 mol is left: \(0.0100 \times 24.3 = 0.243\) g. [A1]
Q: [6 marks] ★★★ 1.50 g of a compound containing only carbon, hydrogen and oxygen is burned completely in excess oxygen. The only products are 2.200 g of carbon dioxide and 0.900 g of water. The relative molecular mass of the compound is 180. Deduce its molecular formula.
H: Find the mass of carbon in the carbon dioxide and the mass of hydrogen in the water. Oxygen is not measured directly: how can you find its mass?
A: Mass of C = \(2.200 \times 12.0 / 44.0 = 0.600\) g, and mass of H = \(0.900 \times 2.0 / 18.0 = 0.100\) g [M1] [M1]
Mass of O = 1.50 − 0.600 − 0.100 = 0.800 g (by difference: most of the oxygen in the products came from the air, so it cannot be read from them) [M1]
Moles: C = 0.600 / 12.0 = 0.0500; H = 0.100 / 1.0 = 0.100; O = 0.800 / 16.0 = 0.0500 [M1]
Ratio C : H : O = 1 : 2 : 1, so the empirical formula is \(\ce{CH2O}\) [A1]
Empirical mass = 30.0 and 180 / 30.0 = 6, so the molecular formula is \(\ce{C6H12O6}\). [A1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ A car air bag is inflated by the decomposition of sodium azide, \(\ce{2NaN3(s) -> 2Na(s) + 3N2(g)}\). What mass of sodium azide is needed to produce 60.0 dm³ of nitrogen at room temperature and pressure?
H: Find the moles of nitrogen first. What is the ratio of \(\ce{NaN3}\) to \(\ce{N2}\)?
H: \(M_r(\ce{NaN3}) = 23.0 + 3(14.0)\).
A: \(n(\ce{N2}) = 60.0 / 24.0 = 2.50\) mol [M1]
\(n(\ce{NaN3}) = 2.50 \times \tfrac23 = 1.667\) mol [M1]
\(M_r(\ce{NaN3}) = 65.0\) [B1]
Mass = \(1.667 \times 65.0 = 108\) g [A1]
Q: [5 marks] ★★★ 0.0100 mol of a metal chloride, \(\ce{MCl_x}\), is dissolved in water and treated with excess aqueous silver nitrate. 2.87 g of silver chloride is precipitated. The mass of the metal chloride is 1.11 g. (a) Find \(x\). (b) Calculate \(A_r\) of M and suggest what M is.
H: Each chloride ion gives one mole of AgCl.
A: \(M_r(\mathrm{AgCl}) = 107.9 + 35.5 = 143.4\) [B1]
\(n(\mathrm{AgCl}) = 2.87 / 143.4 = 0.02001\) mol, which is 0.0200 mol of chloride ions [M1]
(a) \(x = 0.0200 / 0.0100 = 2\) [A1]
(b) \(M_r(\ce{MCl2}) = 1.11 / 0.0100 = 111\), so \(A_r(\mathrm{M}) = 111 - 2(35.5) = 40.0\) [M1], which is calcium. [A1]
:::

:::quiz
? Gallium has two isotopes, \({}^{69}\mathrm{Ga}\) (60%) and \({}^{71}\mathrm{Ga}\) (40%). What is its relative atomic mass?
- 70.0
- 70.2
- 140.0
+ 69.8
> The weighted mean is \((69 \times 60 + 71 \times 40) / 100 = 69.8\). 70.0 is the simple mean, which ignores the abundances. 70.2 swaps the abundances. 140.0 adds the two masses.
? How many moles are in 8.00 g of sodium hydroxide?
- 0.125
+ 0.200
- 5.00
- 320
> \(n = m / M = 8.00 / 40.0 = 0.200\). 5.00 inverts the formula (\(M/m\)), 0.125 is \(1/8.00\) with the molar mass left out, and 320 multiplies mass by molar mass.
? 2.00 g of sodium hydroxide is dissolved in water and made up to 500 cm³. What is the concentration?
- 0.0250 mol dm⁻³
- 1.00 × 10⁻⁴ mol dm⁻³
+ 0.100 mol dm⁻³
- 10.0 mol dm⁻³
> \(n = 2.00 / 40.0 = 0.0500\) mol and \(V = 0.500\) dm³, so \(c = 0.100\) mol dm⁻³. Using 500 instead of 0.500 gives 1.00 × 10⁻⁴.
? What volume of carbon dioxide at room temperature and pressure forms when 0.0500 mol of calcium carbonate is heated: \(\ce{CaCO3 -> CaO + CO2}\)?
- 0.0500 dm³
- 1.12 dm³
+ 1.20 dm³
- 2.40 dm³
> The ratio is 1 : 1, so \(n(\ce{CO2}) = 0.0500\) mol and \(V = 0.0500 \times 24.0 = 1.20\) dm³. 1.12 uses 22.4, which is the value at s.t.p., not room conditions.
? A hydrocarbon has \(M_r = 84.0\) and contains 85.7% carbon. What is its molecular formula?
- \(\ce{CH2}\)
- \(\ce{C3H6}\)
+ \(\ce{C6H12}\)
- \(\ce{C7H12}\)
> The empirical formula is \(\ce{CH2}\) (mass 14.0), and \(84.0 / 14.0 = 6\), so the molecular formula is \(\ce{C6H12}\). \(\ce{CH2}\) is the empirical formula, which is a different thing.
? 0.200 mol of aluminium and 0.240 mol of chlorine react: \(\ce{2Al + 3Cl2 -> 2AlCl3}\). Which statement is correct?
- Aluminium is limiting.
+ Chlorine is limiting.
- Both are used up exactly.
- Neither can be limiting.
> Al: 0.200 / 2 = 0.100 and \(\ce{Cl2}\): 0.240 / 3 = 0.0800. The smaller value is chlorine, so chlorine runs out first and some aluminium is left.
? Which is the correct ionic equation for aqueous silver nitrate with aqueous potassium chloride?
- \(\ce{AgNO3(aq) + KCl(aq) -> AgCl(s) + KNO3(aq)}\)
+ \(\ce{Ag+(aq) + Cl-(aq) -> AgCl(s)}\)
- \(\ce{Ag+(aq) + Cl-(aq) + K+(aq) -> AgCl(s) + K+(aq)}\)
- \(\ce{Ag+(aq) + Cl-(aq) -> Ag+Cl-(aq)}\)
> An ionic equation leaves out spectator ions (here \(\ce{K+}\) and \(\ce{NO3-}\)) and shows the solid precipitate. The first option is the full equation, and the third still contains a spectator.
? What is the formula of iron(III) sulfate?
- \(\ce{FeSO4}\)
- \(\ce{Fe3(SO4)2}\)
+ \(\ce{Fe2(SO4)3}\)
- \(\ce{Fe(SO4)3}\)
> \(\ce{Fe^3+}\) and \(\ce{SO4^2-}\): two Fe³⁺ give 6+ and three sulfate ions give 6−, so \(\ce{Fe2(SO4)3}\). \(\ce{FeSO4}\) is iron(II) sulfate.
:::

:::checklist What you can now do
- [ ] I can state the unified atomic mass unit and define relative isotopic mass, relative atomic mass, relative molecular mass and relative formula mass.
- [ ] I can calculate relative atomic mass from isotopic abundances, and abundances from relative atomic mass.
- [ ] I can define the mole and the Avogadro constant and convert between mass, amount in moles and number of particles.
- [ ] I can write the formulas of ionic compounds from ionic charges and Roman numerals, and recall the formulas of nitrate, carbonate, sulfate, hydroxide, ammonium, zinc, silver, hydrogencarbonate and phosphate ions.
- [ ] I can write balanced equations with state symbols, and ionic equations leaving out spectator ions.
- [ ] I can define empirical and molecular formula and calculate them from percentage composition, masses or combustion data.
- [ ] I can explain anhydrous, hydrated and water of crystallisation, and find the formula of a hydrated salt from heating data.
- [ ] I can calculate reacting masses and percentage yield.
- [ ] I can calculate gas volumes at room temperature and pressure, and deduce formulas from gas-volume data for burning hydrocarbons.
- [ ] I can calculate concentrations in mol dm⁻³ and g dm⁻³, and do titration and back-titration calculations.
- [ ] I can identify limiting and excess reagents and calculate the product and the excess left over.
- [ ] I can deduce stoichiometric relationships and equations from experimental data.
:::

:::recap
- \(A_r\) is the weighted mean mass of an atom of an element compared with one twelfth of a carbon-12 atom: \(A_r = \sum(\text{mass} \times \text{abundance})/100\). Relative masses have no unit.
- Mole: \(L = 6.022 \times 10^{23}\) particles. \(n = m/M\) and \(N = nL\). Say whether you mean atoms or molecules.
- Ionic formulas balance the charges to zero: brackets for more than one polyatomic ion. The Roman numeral is the charge of the metal ion. Ionic equations leave out spectator ions and keep solids, liquids and gases whole.
- Empirical formula: divide the mass or percentage by \(A_r\), divide by the smallest, multiply to make whole numbers. Molecular formula = empirical formula × \(M_r\) / empirical mass.
- Hydrated salts have water of crystallisation: heat to constant mass, and the mass lost is water.
- Reacting masses: equation, moles, ratio, mass. Percentage yield = actual / theoretical × 100.
- Gas volume = \(n \times 24.0\) dm³ at room conditions (22.4 dm³ at s.t.p.). Volume ratios equal mole ratios for gases at the same temperature and pressure.
- \(c = n/V\) with \(V\) in dm³; g dm⁻³ = mol dm⁻³ × \(M\). In a titration use the ratio from the equation; in a back titration, subtract the excess from the amount added.
- The limiting reagent is the one with the smallest amount ÷ coefficient. Work from it.
:::

:::links
- read: [Chemguide: CIE A level chemistry support](https://www.chemguideforcie.co.uk/index.html) · Chemguide · notes written for the Cambridge syllabus, including the calculation topics
- read: [Chemguide: atomic structure and bonding](https://www.chemguide.co.uk/atommenu.html) · Chemguide · background on relative atomic mass and isotopes
- practise: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic, including mole calculations [unofficial]

Links checked 15 October 2026.
:::

Next: [Chemical bonding](#chem.bonding) uses the electron configurations from this topic and the previous one to explain how atoms join.
