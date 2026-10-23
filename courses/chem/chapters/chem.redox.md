@chapter chem.redox
@title Redox and oxidation numbers
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 4–6 hours
@summary Redox reactions are reactions in which electrons move from one species to another. You will learn oxidation numbers and how to work them out, how to name compounds with Roman numerals, how to write and combine half-equations, how to balance equations by oxidation-number change, and what oxidising agents, reducing agents and disproportionation are.

:::why
Rusting, burning, bleaching, the batteries in a phone, and the way your body gets energy from food are all redox reactions. Chemists use them to extract metals, to make bleach, and to measure the amount of iron in a tablet by titration. The same few ideas appear in every part of the course from here on: which species lose electrons, which gain them, and how to write the equation so that both the atoms and the charges balance.
:::

**Before you start**, you should know how ions form and how to write ionic formulas from [Chemistry from zero](#chem.f.basics), how to balance equations and do titration calculations from [Moles and stoichiometry](#chem.moles), and what electronegativity and bond polarity are from [Chemical bonding](#chem.bonding).

:::try Warm-up
Q: How many electrons does a magnesium atom lose to form \(\ce{Mg^2+}\)? (from [Atomic structure](#chem.atoms))
A: Two: the 3s² pair is lost, leaving 1s² 2s² 2p⁶.
Q: Balance \(\ce{H2 + O2 -> H2O}\). (from [Moles and stoichiometry](#chem.moles))
A: \(\ce{2H2 + O2 -> 2H2O}\).
Q: Which atom in H–Cl carries the partial negative charge, and why? (from [Chemical bonding](#chem.bonding))
A: Chlorine, because it is more electronegative than hydrogen and pulls the shared electrons towards itself: \(\ce{H^{\delta+}-Cl^{\delta-}}\).
:::

## Oxidation and reduction as electron transfer

When magnesium burns, each magnesium atom loses two electrons and each oxygen atom gains two. When zinc is put into copper(II) sulfate solution, a pink-brown coating of copper forms on the zinc, and the blue solution slowly fades. In both reactions electrons move from one species to another. That movement is what chemists mean by redox.

:::def Oxidation
Oxidation is the loss of electrons by a species. In terms of oxidation number, oxidation is an increase in oxidation number.
:::

:::def Reduction
Reduction is the gain of electrons by a species. In terms of oxidation number, reduction is a decrease in oxidation number.
:::

:::tip OIL RIG
**O**xidation **I**s **L**oss of electrons, **R**eduction **I**s **G**ain of electrons. Say it before every redox question until you stop needing to.
:::

Electrons cannot be left over, so oxidation and reduction always happen together in the same reaction. A reaction in which both occur is a **redox reaction** (reduction and oxidation). For zinc and copper(II) ions, the full reaction is

\[\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\]

Split it into two **half-equations**, one for each process, with the electrons written out:

\[\ce{Zn -> Zn^2+ + 2e-}\] (oxidation: zinc loses two electrons)
\[\ce{Cu^2+ + 2e- -> Cu}\] (reduction: copper(II) gains two electrons)

:::html
<figure class="fig small"><svg viewBox="0 18 330 140" role="img" aria-label="Half-equations for zinc reacting with copper(II) ions: zinc loses two electrons to form Zn2+ (oxidation), and a curved arrow carries the two electrons to Cu2+, which gains them to form copper (reduction)"><text class="tl" x="14" y="44">Zn</text><path class="ln" d="M40 40H82" marker-end="url(#ah)"/><text class="tl" x="92" y="44">Zn²⁺ + 2e⁻</text><text class="tl" x="210" y="36">oxidation:</text><text class="tl" x="210" y="54">electrons lost</text><text class="tl" x="14" y="134">Cu²⁺ + 2e⁻</text><path class="ln" d="M94 130H136" marker-end="url(#ah)"/><text class="tl" x="146" y="134">Cu</text><text class="tl" x="210" y="126">reduction:</text><text class="tl" x="210" y="144">electrons gained</text><path class="c2 sw2" d="M150 54Q140 96 80 112" marker-end="url(#ah)"/></svg><figcaption>Zinc is oxidised and copper(II) ions are reduced. The curved arrow shows the two electrons passing from the zinc to the copper(II) ion.</figcaption></figure>
:::

The electrons on the right of the first half-equation are the electrons on the left of the second, so they cancel when you add the half-equations. Adding gives the full equation above. Notice that the two half-equations must have the **same number of electrons** before you add them. Section "Half-equations" below turns this into a method.

Older books define oxidation as gaining oxygen or losing hydrogen, and reduction as the opposite. These are special cases: when magnesium gains oxygen to make \(\ce{MgO}\), it really loses electrons to oxygen. Electron transfer and oxidation number cover every case, including reactions with no oxygen or hydrogen at all, so use them.

## Oxidation numbers

In an ionic compound it is easy to see who has lost electrons: sodium chloride is \(\ce{Na+}\) and \(\ce{Cl-}\). In a covalent compound the electrons are shared, so no electrons are completely lost. Chemists still want to keep track of who has "gained" and who has "lost", so they use a bookkeeping number.

:::def Oxidation number
The oxidation number of an atom in a compound or ion is the charge it would have if all the bonding electrons were given to the more electronegative atom in each bond (and shared equally between identical atoms). It is written with its sign first: +2, −1.
:::

For a simple ion the oxidation number equals the charge: \(\ce{Na+}\) is +1, \(\ce{Cl-}\) is −1. For other species you work it out from a set of rules.

:::key Rules for oxidation numbers
Apply these in this order. The sum of oxidation numbers is **0** in a neutral compound and equals the **charge** in an ion.
1. An atom in an uncombined element has oxidation number **0** (\(\ce{Na}\), \(\ce{O2}\), \(\ce{P4}\), \(\ce{S8}\)).
2. A simple monatomic ion has an oxidation number equal to its charge (\(\ce{Fe^3+}\) is +3, \(\ce{O^2-}\) is −2).
3. Fluorine is always **−1** in compounds.
4. Group 1 metals are **+1** and Group 2 metals are **+2** in compounds. Aluminium is +3.
5. Hydrogen is **+1**, except in metal hydrides such as \(\ce{NaH}\) and \(\ce{CaH2}\), where it is −1.
6. Oxygen is **−2**, except in peroxides such as \(\ce{H2O2}\) (−1), and when combined with fluorine in \(\ce{OF2}\) (+2).
7. The atom of the more electronegative element in a bond takes the negative oxidation number (chlorine is −1 in \(\ce{CCl4}\)).
:::

:::warn Charge and oxidation number are written differently
A charge is written **number then sign**: \(\ce{Fe^3+}\), 3+. An oxidation number is written **sign then number**: +3. Writing "Fe has oxidation number 3+" loses a mark. In names, use Roman numerals with no sign: iron(III).
:::

:::eg Calculate the oxidation number of manganese in \(\ce{MnO4-}\), of chromium in \(\ce{Cr2O7^2-}\), of sulfur in \(\ce{SO4^2-}\) and \(\ce{S2O3^2-}\), of nitrogen in \(\ce{NH4+}\), and of oxygen in \(\ce{H2O2}\).
Let the unknown oxidation number be \(x\) and make the sum equal to the charge.

\(\ce{MnO4-}\): \(x + 4(-2) = -1\), so \(x = +7\).

\(\ce{Cr2O7^2-}\): \(2x + 7(-2) = -2\), so \(2x = +12\) and \(x = +6\).

\(\ce{SO4^2-}\): \(x + 4(-2) = -2\), so \(x = +6\).

\(\ce{S2O3^2-}\): \(2x + 3(-2) = -2\), so \(x = +2\). This is an average: the two sulfur atoms are not in identical positions, but the average is what the question asks for.

\(\ce{NH4+}\): \(x + 4(+1) = +1\), so \(x = -3\).

\(\ce{H2O2}\): \(2(+1) + 2x = 0\), so \(x = -1\). Oxygen is −1 here, which is why hydrogen peroxide is a peroxide and not an ordinary oxide.
:::

Oxidation numbers can also be used for organic compounds. Treat each carbon atom as the more electronegative partner of any hydrogen, and the less electronegative partner of oxygen:

| Compound | Formula | Oxidation number of carbon |
|---|---|---|
| methane | \(\ce{CH4}\) | −4 |
| methanol | \(\ce{CH3OH}\) | −2 |
| methanal | \(\ce{HCHO}\) | 0 |
| methanoic acid | \(\ce{HCOOH}\) | +2 |
| carbon dioxide | \(\ce{CO2}\) | +4 |

Going down the table, each step is an oxidation of the carbon atom. You will use the same idea for alcohols, aldehydes and carboxylic acids later in the course.

### Roman numerals in names

When an element can have more than one oxidation number, the name carries a Roman numeral in brackets to say which one is present. The numeral shows the **magnitude** of the oxidation number: no plus sign.

| Formula | Oxidation number | Name |
|---|---|---|
| \(\ce{FeCl2}\) | Fe +2 | iron(II) chloride |
| \(\ce{FeCl3}\) | Fe +3 | iron(III) chloride |
| \(\ce{CuO}\) | Cu +2 | copper(II) oxide |
| \(\ce{MnO4-}\) | Mn +7 | manganate(VII) |
| \(\ce{Cr2O7^2-}\) | Cr +6 | dichromate(VI) |
| \(\ce{ClO-}\) | Cl +1 | chlorate(I) |
| \(\ce{ClO3-}\) | Cl +5 | chlorate(V) |
| \(\ce{NO2-}\) | N +3 | nitrate(III) (nitrite) |
| \(\ce{NO3-}\) | N +5 | nitrate(V) (nitrate) |

The numeral goes with the element it names, not with the formula as a whole, so \(\ce{K2Cr2O7}\) is potassium dichromate(VI), where the (VI) is chromium's oxidation number. Compounds of elements with only one common oxidation number, such as sodium chloride or magnesium oxide, take no numeral.

:::eg Name \(\ce{Fe2O3}\) and \(\ce{KMnO4}\), and write the formula of copper(I) oxide.
In \(\ce{Fe2O3}\) the three oxide ions (−2 each) have a total of −6, so the two iron atoms share +6, and each is +3: iron(III) oxide.

In \(\ce{KMnO4}\) potassium is +1 and the four oxygens total −8, so Mn is +7: potassium manganate(VII).

Copper(I) means \(\ce{Cu+}\), and oxide is \(\ce{O^2-}\). Two \(\ce{Cu+}\) ions balance one \(\ce{O^2-}\): \(\ce{Cu2O}\).
:::

## Redox in terms of oxidation number

Electron transfer is easy to see in ionic reactions. For covalent reactions, work out the oxidation number of each element before and after.

:::key Redox by oxidation number
- **Oxidation**: the oxidation number of an element **increases**.
- **Reduction**: the oxidation number of an element **decreases**.
- If no element changes its oxidation number, the reaction is **not** redox (acid–base and precipitation reactions are not).
:::

:::eg Show, using oxidation numbers, whether each reaction is redox. If it is, name the species oxidised and reduced. (a) \(\ce{Mg + 2HCl -> MgCl2 + H2}\) (b) \(\ce{Cl2 + 2KBr -> 2KCl + Br2}\) (c) \(\ce{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}\)
(a) Mg goes from 0 to +2: oxidised. H goes from +1 (in HCl) to 0 (in \(\ce{H2}\)): reduced. Chlorine stays at −1. It is a redox reaction.

(b) Cl goes from 0 to −1: reduced. Br goes from −1 to 0: oxidised. Potassium stays at +1. Redox.

(c) Ca stays +2, C stays +4, O stays −2, H stays +1, Cl stays −1. Nothing changes, so it is not a redox reaction. It is an acid–carbonate reaction.
:::

### Redox you already know

Many familiar reactions are redox once you look at oxidation numbers.

- **Combustion.** In \(\ce{CH4 + 2O2 -> CO2 + 2H2O}\) carbon goes from −4 to +4 and oxygen from 0 to −2. Burning is oxidation of the fuel, and the oxygen is the oxidising agent.
- **Rusting.** Iron goes from 0 to +3 as it combines with oxygen and water, so rusting is oxidation of iron.
- **Metal displacement.** A more reactive metal reduces the ions of a less reactive one, as in \(\ce{Zn + Cu^2+ -> Zn^2+ + Cu}\). The more reactive metal is the better reducing agent.
- **Halogen displacement.** A more reactive halogen oxidises the halide ion of a less reactive one, as in \(\ce{Cl2 + 2Br- -> 2Cl- + Br2}\).
- **Extracting a metal.** In the blast furnace carbon monoxide reduces iron(III) oxide: \(\ce{Fe2O3 + 3CO -> 2Fe + 3CO2}\). Iron goes from +3 to 0 (reduced) and carbon from +2 to +4 (oxidised), so \(\ce{CO}\) is the reducing agent.

:::eg In \(\ce{Fe2O3 + 3CO -> 2Fe + 3CO2}\), show that the total increase in oxidation number equals the total decrease.
Iron: two atoms each go from +3 to 0, a total decrease of \(2 \times 3 = 6\).

Carbon: three atoms each go from +2 to +4, a total increase of \(3 \times 2 = 6\).

The increase and the decrease are equal (6 and 6), as they must be in a correct equation. Oxygen stays at −2 throughout.
:::

## Oxidising agents and reducing agents

:::def Oxidising agent
A species that oxidises another species by accepting electrons from it. The oxidising agent is itself **reduced**.
:::

:::def Reducing agent
A species that reduces another species by donating electrons to it. The reducing agent is itself **oxidised**.
:::

The agent and the thing it acts on are opposites, and the commonest slip in the topic is to mix them up. In \(\ce{Zn + Cu^2+ -> Zn^2+ + Cu}\), zinc is oxidised, so zinc is the **reducing agent**. Copper(II) is reduced, so \(\ce{Cu^2+}\) is the **oxidising agent**.

:::analogy
A reducing agent is like a generous friend who gives away electrons, and ends up with fewer. An oxidising agent is like someone who collects them. The giver is oxidised and the collector is reduced, but we name the agents by what they *do to the other species*.
:::

| Common oxidising agents (they gain electrons) | Common reducing agents (they lose electrons) |
|---|---|
| acidified \(\ce{MnO4-}\) (to \(\ce{Mn^2+}\)) | metals such as Mg, Zn, Fe |
| acidified \(\ce{Cr2O7^2-}\) (to \(\ce{Cr^3+}\)) | \(\ce{Fe^2+}\) (to \(\ce{Fe^3+}\)) |
| halogens \(\ce{Cl2}\), \(\ce{Br2}\) (to halide ions) | iodide ion \(\ce{I-}\) (to \(\ce{I2}\)) |
| \(\ce{H2O2}\) (to water), concentrated \(\ce{HNO3}\) | ethanedioate \(\ce{C2O4^2-}\) (to \(\ce{CO2}\)) |

Hydrogen peroxide is in an interesting position. Oxygen in \(\ce{H2O2}\) has oxidation number −1, between 0 (in \(\ce{O2}\)) and −2 (in water), so hydrogen peroxide can be reduced to water (acting as an oxidising agent) or oxidised to oxygen (acting as a reducing agent). Which one happens depends on what it meets.

:::eg Hydrogen peroxide reacts with acidified iron(II) ions: \(\ce{H2O2 + 2Fe^2+ + 2H+ -> 2H2O + 2Fe^3+}\). Identify what is oxidised and reduced, and the oxidising agent and reducing agent.
Iron: +2 → +3, an increase, so \(\ce{Fe^2+}\) is **oxidised**. It is the **reducing agent**.

Oxygen in \(\ce{H2O2}\): −1 → −2, a decrease, so \(\ce{H2O2}\) is **reduced**. It is the **oxidising agent**.

Hydrogen stays +1 throughout.
:::

## Half-equations

A half-equation shows one half of a redox reaction: the species gaining or losing electrons, with the electrons written in. In acid solution you can build any half-equation in five steps. The oxidation numbers are not needed in this method: the electrons are found from the charges.

:::steps
1. Write the species that changes and what it becomes (for example \(\ce{MnO4- -> Mn^2+}\)).
2. Balance the atoms other than O and H.
3. Balance oxygen by adding \(\ce{H2O}\) to the side that needs oxygen.
4. Balance hydrogen by adding \(\ce{H+}\) to the side that needs hydrogen.
5. Balance charge by adding electrons to the more positive side. Then check that atoms and charges balance.
:::

:::eg Write the half-equation for \(\ce{MnO4-}\) being reduced to \(\ce{Mn^2+}\) in acid.
Step 1: \(\ce{MnO4- -> Mn^2+}\). Step 2: one Mn on each side, so nothing to do.

Step 3: there are four oxygen atoms on the left, so add four \(\ce{H2O}\) on the right: \(\ce{MnO4- -> Mn^2+ + 4H2O}\).

Step 4: the four water molecules have eight hydrogen atoms, so add eight \(\ce{H+}\) on the left: \(\ce{MnO4- + 8H+ -> Mn^2+ + 4H2O}\).

Step 5: the left side has charge \(-1 + 8 = +7\) and the right side has \(+2\). Add five electrons to the left to make both sides +2:

\[\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\]

Check: Mn changes from +7 to +2, a gain of five electrons. ✓
:::

:::eg Write the half-equation for \(\ce{Cr2O7^2-}\) being reduced to \(\ce{Cr^3+}\) in acid.
Step 1: \(\ce{Cr2O7^2- -> Cr^3+}\). Step 2: two Cr on the left, so \(\ce{Cr2O7^2- -> 2Cr^3+}\).

Step 3: seven oxygens, so add \(\ce{7H2O}\) on the right. Step 4: fourteen hydrogens, so add \(\ce{14H+}\) on the left.

Step 5: left charge \(-2 + 14 = +12\), right charge \(2(+3) = +6\). Add six electrons to the left:

\[\ce{Cr2O7^2- + 14H+ + 6e- -> 2Cr^3+ + 7H2O}\]

Check: two chromium atoms each go from +6 to +3, a total gain of six electrons. ✓
:::

Many half-equations are simpler. For oxidations the electrons go on the right:

\[\ce{Fe^2+ -> Fe^3+ + e-}\]
\[\ce{C2O4^2- -> 2CO2 + 2e-}\]
\[\ce{2I- -> I2 + 2e-}\]
\[\ce{SO3^2- + H2O -> SO4^2- + 2H+ + 2e-}\]
\[\ce{H2O2 -> O2 + 2H+ + 2e-}\]

and for reductions they go on the left:

\[\ce{Cl2 + 2e- -> 2Cl-}\]
\[\ce{H2O2 + 2H+ + 2e- -> 2H2O}\]

Notice that the two hydrogen peroxide half-equations show it acting once as a reducing agent and once as an oxidising agent.

### Combining half-equations

To get the full equation, multiply each half-equation so that the electrons gained equal the electrons lost, then add the half-equations and cancel everything that appears on both sides (the electrons, and often some \(\ce{H+}\) and \(\ce{H2O}\)).

:::eg Combine the half-equations for \(\ce{Cr2O7^2-}\) and \(\ce{Fe^2+}\) to give the equation for the reaction in acid solution.
The dichromate half-equation takes six electrons: \(\ce{Cr2O7^2- + 14H+ + 6e- -> 2Cr^3+ + 7H2O}\).

The iron half-equation gives one electron per ion: \(\ce{Fe^2+ -> Fe^3+ + e-}\). Multiply it by 6 so that six electrons are released: \(\ce{6Fe^2+ -> 6Fe^3+ + 6e-}\).

Add, and cancel the 6 electrons:

\[\ce{Cr2O7^2- + 14H+ + 6Fe^2+ -> 2Cr^3+ + 7H2O + 6Fe^3+}\]

Check the charges: left \(-2 + 14 + 12 = +24\); right \(+6 + 0 + 18 = +24\). ✓
:::

:::eg Combine the half-equations for \(\ce{MnO4-}\) and \(\ce{H2O2}\) (acting as a reducing agent).
\(\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\) takes five electrons, and \(\ce{H2O2 -> O2 + 2H+ + 2e-}\) gives two. The lowest common multiple of 5 and 2 is 10, so multiply the first by 2 and the second by 5:

\[\ce{2MnO4- + 16H+ + 10e- -> 2Mn^2+ + 8H2O}\]
\[\ce{5H2O2 -> 5O2 + 10H+ + 10e-}\]

Adding, cancelling the 10 electrons, and removing 10 of the 16 \(\ce{H+}\) from both sides:

\[\ce{2MnO4- + 6H+ + 5H2O2 -> 2Mn^2+ + 8H2O + 5O2}\]

Check: oxygen 8 + 10 = 18 on each side; hydrogen 6 + 10 = 16 on each side; charge \(-2 + 6 = +4\) and \(2(+2) = +4\). ✓
:::

## Balancing equations with oxidation numbers

You can also balance an equation without writing half-equations. The rule is that the **total increase** in oxidation number must equal the **total decrease**.

:::steps
1. Write the unbalanced equation and find the oxidation numbers of the elements that change.
2. Find the change per atom, and the number of atoms of that element in each formula.
3. Choose coefficients so that total increase equals total decrease.
4. Balance the remaining atoms (O with \(\ce{H2O}\), H with \(\ce{H+}\) if the reaction is in acid) and check the charges.
:::

:::eg Balance \(\ce{MnO4- + Fe^2+ + H+ -> Mn^2+ + Fe^3+ + H2O}\).
Mn: +7 → +2, a decrease of 5 per Mn. Fe: +2 → +3, an increase of 1 per Fe.

For total increase to equal total decrease, 5 iron ions are needed for each manganese: ratio \(\ce{MnO4-} : \ce{Fe^2+} = 1 : 5\).

\[\ce{MnO4- + 5Fe^2+ + H+ -> Mn^2+ + 5Fe^3+ + H2O}\]

Four oxygens in \(\ce{MnO4-}\) need four \(\ce{H2O}\), which need eight \(\ce{H+}\):

\[\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}\]

Charge: left \(-1 + 10 + 8 = +17\); right \(+2 + 15 = +17\). ✓
:::

:::eg (Real context) Copper dissolves in concentrated nitric acid to give copper(II) nitrate, brown nitrogen dioxide and water. Balance \(\ce{Cu + HNO3 -> Cu(NO3)2 + NO2 + H2O}\) using oxidation numbers.
Cu: 0 → +2, an increase of 2. N in \(\ce{HNO3}\): +5, and in \(\ce{NO2}\): +4, a decrease of 1 per N that is reduced.

One Cu (increase 2) needs two N atoms reduced (decrease 2), so two \(\ce{NO2}\) are formed. The two nitrate ions in \(\ce{Cu(NO3)2}\) keep nitrogen at +5, so they are not reduced, but their nitrogen must also come from nitric acid. Total nitrogen: two in \(\ce{NO2}\) plus two in \(\ce{Cu(NO3)2}\) is four, so four \(\ce{HNO3}\) are needed:

\[\ce{Cu + 4HNO3 -> Cu(NO3)2 + 2NO2 + 2H2O}\]

Check: hydrogen 4 = 2 × 2; oxygen \(12 = 6 + 4 + 2\). ✓ Nitric acid does two jobs here: half of it is the oxidising agent (reduced to \(\ce{NO2}\)), and half stays as nitrate ions in the salt.
:::

## Disproportionation

Sometimes one element in one species is both oxidised and reduced in the same reaction.

:::def Disproportionation
The oxidation and reduction of the same element (in the same species) in the same reaction. Some of the atoms increase their oxidation number and some decrease it.
:::

The element must start at an oxidation number **between** two others that it can reach. Chlorine is the standard example. In cold, dilute sodium hydroxide:

\[\ce{Cl2 + 2NaOH -> NaCl + NaClO + H2O}\]

Chlorine goes from 0 to −1 in \(\ce{NaCl}\) (reduced) and from 0 to +1 in \(\ce{NaClO}\) (oxidised). The \(\ce{NaClO}\), sodium chlorate(I), is the active ingredient of household bleach. With hot concentrated sodium hydroxide the chlorine is oxidised further, to chlorate(V):

\[\ce{3Cl2 + 6NaOH -> 5NaCl + NaClO3 + 3H2O}\]

:::html
<figure class="fig small"><svg viewBox="0 4 340 200" role="img" aria-label="Number line of oxidation numbers for chlorine from minus 2 to plus 6, marking Cl minus (−1), Cl2 (0), ClO minus (+1) and ClO3 minus (+5). Chlorine at 0 forms Cl minus and ClO minus with cold sodium hydroxide, and Cl minus and ClO3 minus with hot sodium hydroxide"><text class="tl" x="14" y="20">oxidation number of chlorine</text><text class="tl" x="14" y="44">← reduction</text><text class="tl" x="326" y="44" text-anchor="end">oxidation →</text><path class="ax" d="M14 90H330" marker-end="url(#ahm)"/><path class="ln-m" d="M24 86V94"/><text class="ts tc" x="24" y="110">−2</text><path class="ln-m" d="M60 86V94"/><text class="ts tc" x="60" y="110">−1</text><path class="ln-m" d="M96 86V94"/><text class="ts tc" x="96" y="110">0</text><path class="ln-m" d="M132 86V94"/><text class="ts tc" x="132" y="110">+1</text><path class="ln-m" d="M168 86V94"/><text class="ts tc" x="168" y="110">+2</text><path class="ln-m" d="M204 86V94"/><text class="ts tc" x="204" y="110">+3</text><path class="ln-m" d="M240 86V94"/><text class="ts tc" x="240" y="110">+4</text><path class="ln-m" d="M276 86V94"/><text class="ts tc" x="276" y="110">+5</text><path class="ln-m" d="M312 86V94"/><text class="ts tc" x="312" y="110">+6</text><circle class="fa s-acc" cx="60" cy="90" r="4"/><text class="tl tc" x="60" y="76">Cl⁻</text><circle class="fa s-acc" cx="96" cy="90" r="4"/><text class="tl tc" x="96" y="76">Cl₂</text><circle class="fa s-acc" cx="132" cy="90" r="4"/><text class="tl tc" x="132" y="76">ClO⁻</text><circle class="fa s-acc" cx="276" cy="90" r="4"/><text class="tl tc" x="276" y="76">ClO₃⁻</text><path class="ln-m thin dash" d="M60 118V198"/><path class="ln-m thin dash" d="M96 118V198"/><path class="ln-m thin dash" d="M132 118V198"/><path class="ln-m thin dash" d="M276 118V198"/><text class="tl" x="146" y="138">cold NaOH(aq)</text><path class="ln" d="M92 150H64" marker-end="url(#ah)"/><path class="ln" d="M100 150H128" marker-end="url(#ah)"/><text class="tl" x="146" y="174">hot NaOH(aq)</text><path class="ln" d="M92 186H64" marker-end="url(#ah)"/><path class="ln" d="M100 186H272" marker-end="url(#ah)"/></svg><figcaption>Chlorine disproportionates in sodium hydroxide: some atoms move left on the line (reduction to chloride) and some move right (oxidation). With cold NaOH(aq) the product is chlorate(I), ClO⁻; with hot NaOH(aq) it is chlorate(V), ClO₃⁻.</figcaption></figure>
:::

Check the hot reaction by oxidation numbers: each Cl that becomes \(\ce{Cl-}\) gains 1 electron, and each Cl that becomes \(\ce{ClO3-}\) loses 5. Five \(\ce{Cl-}\) (a gain of 5) balance one \(\ce{ClO3-}\) (a loss of 5), so six chlorine atoms (three \(\ce{Cl2}\)) are needed, as the equation shows. The reaction of chlorine with water is also a disproportionation and is covered in [Group 17: the halogens](#chem.group17).

Hydrogen peroxide decomposes by disproportionation of its oxygen, from −1 to −2 and 0:

\[\ce{2H2O2 -> 2H2O + O2}\]

:::eg Show that \(\ce{2Cu+ -> Cu + Cu^2+}\) is a disproportionation.
Copper in \(\ce{Cu+}\) has oxidation number +1. In the products one copper is 0 (in \(\ce{Cu}\)): a decrease from +1, so reduction. The other is +2 (in \(\ce{Cu^2+}\)): an increase from +1, so oxidation.

The same species, \(\ce{Cu+}\), is both oxidised and reduced, so this is a disproportionation.
:::

## Redox titrations

Redox reactions are used for titration. The most common titrant is **acidified potassium manganate(VII)**. It is purple, and its reduction product \(\ce{Mn^2+}\) is almost colourless, so the mixture goes from purple to colourless as the manganate(VII) is added, and the **end-point** is the first permanent pale pink. No separate indicator is needed.

Three reactions are used in the practical course, and you should be able to write all three equations from half-equations:

\[\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}\]
\[\ce{2MnO4- + 5C2O4^2- + 16H+ -> 2Mn^2+ + 10CO2 + 8H2O}\]
\[\ce{2MnO4- + 5H2O2 + 6H+ -> 2Mn^2+ + 5O2 + 8H2O}\]

:::warn Use dilute sulfuric acid, not hydrochloric acid
Manganate(VII) must be acidified, and the acid used is **dilute sulfuric acid**. Hydrochloric acid cannot be used: manganate(VII) is a strong enough oxidising agent to oxidise chloride ions to chlorine, so some of it would be used up in this side-reaction and the titre would be too large.
:::

:::eg 25.0 cm³ of an iron(II) sulfate solution is titrated with 0.0200 mol dm⁻³ potassium manganate(VII) in the presence of excess dilute sulfuric acid. The mean titre is 22.40 cm³. Calculate the concentration of iron(II) ions.
The equation is \(\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}\): 1 mol of \(\ce{MnO4-}\) reacts with 5 mol of \(\ce{Fe^2+}\).

\[n(\ce{MnO4-}) = 0.0200 \times \frac{22.40}{1000} = 4.48 \times 10^{-4}\,\mathrm{mol}\] [M1]
\[n(\ce{Fe^2+}) = 5 \times 4.48 \times 10^{-4} = 2.24 \times 10^{-3}\,\mathrm{mol}\] [M1]
\[c(\ce{Fe^2+}) = \frac{2.24 \times 10^{-3}}{25.0/1000} = 0.0896\,\mathrm{mol\,dm^{-3}}\] [A1]
:::

:::eg (Real context) An iron supplement tablet of mass 1.50 g contains iron(II) sulfate, \(\ce{FeSO4}\), and an inert filler. The tablet is dissolved in dilute sulfuric acid and made up to 250 cm³ in a volumetric flask. A 25.0 cm³ portion needs 14.40 cm³ of 0.0100 mol dm⁻³ potassium manganate(VII). Calculate the percentage by mass of \(\ce{FeSO4}\) in the tablet.
\[n(\ce{MnO4-}) = 0.0100 \times \frac{14.40}{1000} = 1.440 \times 10^{-4}\,\mathrm{mol}\] [M1]
\[n(\ce{Fe^2+}) \text{ in } 25.0\ \mathrm{cm^3} = 5 \times 1.440 \times 10^{-4} = 7.20 \times 10^{-4}\,\mathrm{mol}\] [M1]
The portion is one tenth of the solution, so the whole tablet contained \(7.20 \times 10^{-3}\) mol. [M1]

\(M_r(\ce{FeSO4}) = 55.8 + 32.1 + 4(16.0) = 151.9\), so the mass is \(7.20 \times 10^{-3} \times 151.9 = 1.094\) g. [B1]

\[\text{percentage} = \frac{1.094}{1.50} \times 100 = 72.9\,\%\] [A1]
:::

:::eg 25.0 cm³ of 0.0500 mol dm⁻³ sodium ethanedioate, \(\ce{Na2C2O4}\), is warmed with excess dilute sulfuric acid and titrated with 0.0200 mol dm⁻³ potassium manganate(VII). What titre is expected?
From \(\ce{2MnO4- + 5C2O4^2- + 16H+ -> 2Mn^2+ + 10CO2 + 8H2O}\): 2 mol of \(\ce{MnO4-}\) react with 5 mol of \(\ce{C2O4^2-}\).

\(n(\ce{C2O4^2-}) = 0.0500 \times 0.0250 = 1.25 \times 10^{-3}\) mol.

\(n(\ce{MnO4-}) = 1.25 \times 10^{-3} \times \tfrac25 = 5.00 \times 10^{-4}\) mol.

\(V = 5.00 \times 10^{-4} / 0.0200 = 0.0250\) dm³ = 25.0 cm³.
:::

:::eg Spot the error: identify the oxidising agent and the reducing agent in \(\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}\), giving the oxidation-number change that shows each. [3 marks]
A student wrote this answer.

Line 1: Fe changes from +2 to +3, so Fe²⁺ is oxidised.
Line 2: Mn changes from +7 to +2, so MnO₄⁻ is reduced.
Line 3: Fe²⁺ is oxidised, so it is the oxidising agent, and MnO₄⁻ is reduced, so it is the reducing agent.

Line 1 is correct: the increase shows oxidation [B1]. Line 2 is correct: the decrease shows reduction [B1]. **Line 3 is wrong: the agent does the opposite of what happens to it. The species that is oxidised is the reducing agent, and the species that is reduced is the oxidising agent [B0].**

The student scores 2 out of 3. Correct line 3: \(\ce{Fe^2+}\) is oxidised, so it is the reducing agent; \(\ce{MnO4-}\) is reduced, so it is the oxidising agent. [B1]
:::

:::exam Redox answers that earn the marks
Always quote the oxidation-number change with its sign ("Mn from +7 to +2") and say what that change is called (reduction). Name the agent only after you have decided what was oxidised or reduced. In half-equations, check both atoms **and** charge before you write the final answer. In titration calculations, write the mole ratio from the balanced equation before using it.
:::

:::try Start easy, finish at exam standard
Q: Give the oxidation number of (a) S in \(\ce{H2S}\), (b) N in \(\ce{NO3-}\), (c) Cl in \(\ce{ClO4-}\), (d) C in \(\ce{CH3OH}\), (e) Mn in \(\ce{MnO2}\).
A: (a) \(2(+1) + x = 0\): −2. (b) \(x + 3(-2) = -1\): +5. (c) \(x + 4(-2) = -1\): +7. (d) \(x + 4(+1) + (-2) = 0\): −2. (e) \(x + 2(-2) = 0\): +4.
Q: Name \(\ce{CrCl3}\), \(\ce{Cu2O}\), \(\ce{Na2SO3}\) (sulfur is +4 in the sulfite ion), and \(\ce{KClO3}\).
A: Chromium(III) chloride; copper(I) oxide; sodium sulfate(IV) (sodium sulfite); potassium chlorate(V).
Q: In each reaction, state what is oxidised and what is reduced: (a) \(\ce{2Na + Cl2 -> 2NaCl}\), (b) \(\ce{Zn + 2H+ -> Zn^2+ + H2}\).
A: (a) Na 0 → +1 is oxidised; Cl 0 → −1 is reduced. (b) Zn 0 → +2 is oxidised; H +1 → 0 is reduced.
Q: In \(\ce{Cl2 + 2KI -> 2KCl + I2}\), name the oxidising agent and the reducing agent.
A: Cl goes from 0 to −1 (reduced), so \(\ce{Cl2}\) is the oxidising agent. I goes from −1 to 0 (oxidised), so \(\ce{I-}\) is the reducing agent.
Q: Write the half-equation for \(\ce{Fe^3+}\) being reduced to \(\ce{Fe^2+}\), and for \(\ce{Mg}\) being oxidised.
A: \(\ce{Fe^3+ + e- -> Fe^2+}\) and \(\ce{Mg -> Mg^2+ + 2e-}\).
Q: Use the half-equations \(\ce{Cl2 + 2e- -> 2Cl-}\) and \(\ce{Fe^2+ -> Fe^3+ + e-}\) to write the full equation.
A: Multiply the iron half-equation by 2 so the electrons match: \(\ce{Cl2 + 2Fe^2+ -> 2Cl- + 2Fe^3+}\). Charge: left +4, right −2 + 6 = +4. ✓
Q: Write the half-equation for \(\ce{SO3^2-}\) being oxidised to \(\ce{SO4^2-}\) in water.
A: \(\ce{SO3^2- + H2O -> SO4^2- + 2H+ + 2e-}\). Charge: left −2, right −2 + 2 − 2 = −2. ✓
Q: Show that \(\ce{3Cl2 + 6NaOH -> 5NaCl + NaClO3 + 3H2O}\) is a disproportionation.
A: Cl is 0 in \(\ce{Cl2}\). In \(\ce{NaCl}\) it is −1 (reduced) and in \(\ce{NaClO3}\) it is +5 (oxidised): one element, one reactant, both changes.
Q: 25.0 cm³ of 0.0500 mol dm⁻³ \(\ce{Fe^2+}\) is titrated with 0.0200 mol dm⁻³ \(\ce{MnO4-}\) in acid. What volume of manganate(VII) is needed?
A: \(n(\ce{Fe^2+}) = 0.0500 \times 0.0250 = 1.25 \times 10^{-3}\) mol; \(n(\ce{MnO4-}) = 1.25 \times 10^{-3} / 5 = 2.50 \times 10^{-4}\) mol; \(V = 2.50 \times 10^{-4} / 0.0200 = 0.0125\) dm³ = 12.5 cm³.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State what is meant by disproportionation, and give one example of a species that undergoes it.
A: The same element (in the same species) is both oxidised and reduced in the same reaction. [B1]
Example: \(\ce{Cl2}\) in cold aqueous sodium hydroxide, giving \(\ce{Cl-}\) and \(\ce{ClO-}\) (or \(\ce{H2O2}\) decomposing to water and oxygen). [B1]
Q: [3 marks] ★ Deduce the oxidation number of (a) manganese in \(\ce{MnO4^2-}\), (b) chlorine in \(\ce{ClO3-}\), (c) hydrogen in \(\ce{NaH}\).
A: (a) \(x + 4(-2) = -2\), so +6. [B1]
(b) \(x + 3(-2) = -1\), so +5. [B1]
(c) Hydrogen is −1 in a metal hydride (sodium is +1). [B1]
Q: [4 marks] ★★ In acid solution, \(\ce{MnO4-}\) is reduced to \(\ce{Mn^2+}\) and \(\ce{H2O2}\) is oxidised to \(\ce{O2}\). Write both half-equations and combine them into the overall ionic equation.
H: Multiply the half-equations so that both involve ten electrons.
A: \(\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\) [B1]
\(\ce{H2O2 -> O2 + 2H+ + 2e-}\) [B1]
Multiply the first by 2 and the second by 5 so that the electrons cancel. [M1]
\(\ce{2MnO4- + 6H+ + 5H2O2 -> 2Mn^2+ + 8H2O + 5O2}\) [A1]
Q: [4 marks] ★★ Chlorine reacts with hot concentrated aqueous sodium hydroxide to form sodium chloride and sodium chlorate(V). (a) Write the equation. (b) Use oxidation numbers to show that the reaction is a disproportionation.
A: (a) \(\ce{3Cl2 + 6NaOH -> 5NaCl + NaClO3 + 3H2O}\) [B1]
(b) Chlorine goes from 0 to −1 in \(\ce{NaCl}\): reduction. [B1]
Chlorine goes from 0 to +5 in \(\ce{NaClO3}\): oxidation. [B1]
The same element in the same species, \(\ce{Cl2}\), is both oxidised and reduced. [B1]
Q: [5 marks] ★★ A solution of hydrogen peroxide is analysed by titration. 25.0 cm³ of the solution, acidified with dilute sulfuric acid, needs 20.00 cm³ of 0.0200 mol dm⁻³ potassium manganate(VII) to reach the end-point. (a) State the colour change at the end-point. (b) Calculate the concentration of the hydrogen peroxide in mol dm⁻³ and in g dm⁻³.
H: Use the equation \(\ce{2MnO4- + 5H2O2 + 6H+ -> 2Mn^2+ + 5O2 + 8H2O}\) for the mole ratio.
A: (a) Colourless to (permanent) pale pink; the first drop of excess manganate(VII) is not decolourised. [B1]
(b) \(n(\ce{MnO4-}) = 0.0200 \times 0.02000 = 4.00 \times 10^{-4}\) mol [M1]
\(n(\ce{H2O2}) = 4.00 \times 10^{-4} \times \tfrac52 = 1.00 \times 10^{-3}\) mol [M1]
\(c = 1.00 \times 10^{-3} / 0.0250 = 0.0400\) mol dm⁻³ [A1]
\(M_r(\ce{H2O2}) = 34.0\), so \(0.0400 \times 34.0 = 1.36\) g dm⁻³ [A1]
Q: [5 marks] ★★ 1.50 g of a tablet containing iron(II) sulfate is dissolved in dilute sulfuric acid and made up to 250 cm³. 25.0 cm³ portions need a mean titre of 14.40 cm³ of 0.0100 mol dm⁻³ potassium manganate(VII). Calculate the percentage by mass of \(\ce{FeSO4}\) in the tablet.
H: The portion is one tenth of the whole solution.
A: \(n(\ce{MnO4-}) = 0.0100 \times 0.01440 = 1.44 \times 10^{-4}\) mol [M1]
\(n(\ce{Fe^2+})\) in the portion \(= 5 \times 1.44 \times 10^{-4} = 7.20 \times 10^{-4}\) mol [M1]
In 250 cm³: \(7.20 \times 10^{-3}\) mol [M1]
\(M_r(\ce{FeSO4}) = 151.9\), so the mass is 1.094 g [B1]
Percentage \(= 1.094 / 1.50 \times 100 = 72.9\,\%\) [A1]
Q: [6 marks] ★★★ Copper reacts with concentrated nitric acid: \(\ce{Cu + 4HNO3 -> Cu(NO3)2 + 2NO2 + 2H2O}\). (a) Use oxidation numbers to identify the oxidising agent and the element oxidised. (b) State the two roles of nitric acid in this reaction. (c) Calculate the volume of nitrogen dioxide formed, at room temperature and pressure, when 0.635 g of copper reacts.
H: In (b), count the nitrogen that is reduced and the nitrogen that is not.
A: (a) Cu goes from 0 to +2: copper is oxidised. [B1]
N goes from +5 to +4: it is reduced, so nitric acid is the oxidising agent. [B1]
(b) It is the oxidising agent (some of the nitrogen is reduced from +5 to +4), and it is also the source of the nitrate ions that remain in the salt. [B1]
(c) \(n(\mathrm{Cu}) = 0.635 / 63.5 = 0.0100\) mol [M1]
\(n(\ce{NO2}) = 2 \times 0.0100 = 0.0200\) mol, so \(V = 0.0200 \times 24.0 = 0.480\,\mathrm{dm^3}\) [M1] [A1]
Q: [6 marks] ★★★ Acidified potassium dichromate(VI) oxidises iron(II) ions to iron(III) ions. (a) Write the two half-equations. (b) Combine them into one ionic equation. (c) 25.0 cm³ of an iron(II) solution needs 20.00 cm³ of 0.0200 mol dm⁻³ potassium dichromate(VI). Calculate the concentration of the iron(II) solution.
H: Six electrons are involved in the dichromate(VI) half-equation.
A: (a) \(\ce{Cr2O7^2- + 14H+ + 6e- -> 2Cr^3+ + 7H2O}\) [B1] and \(\ce{Fe^2+ -> Fe^3+ + e-}\) [B1]
(b) \(\ce{Cr2O7^2- + 14H+ + 6Fe^2+ -> 2Cr^3+ + 7H2O + 6Fe^3+}\) [B1]
(c) \(n(\ce{Cr2O7^2-}) = 0.0200 \times 0.02000 = 4.00 \times 10^{-4}\) mol [M1]
\(n(\ce{Fe^2+}) = 6 \times 4.00 \times 10^{-4} = 2.40 \times 10^{-3}\) mol [M1]
\(c = 2.40 \times 10^{-3} / 0.0250 = 0.0960\) mol dm⁻³ [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Iodine oxidises thiosulfate ions, \(\ce{S2O3^2-}\), to tetrathionate ions, \(\ce{S4O6^2-}\), and is itself reduced to iodide ions. (a) Deduce the average oxidation number of sulfur in \(\ce{S4O6^2-}\). (b) Write the balanced ionic equation. (c) 25.0 cm³ of an iodine solution needs 20.0 cm³ of 0.100 mol dm⁻³ sodium thiosulfate to decolourise it. Calculate the concentration of the iodine.
H: Sulfur is +2 in \(\ce{S2O3^2-}\). How many electrons does \(\ce{I2}\) gain, and how many does each sulfur atom lose?
A: (a) \(4x + 6(-2) = -2\), so \(x = +2.5\). [B1]
(b) Each \(\ce{I2}\) gains 2 electrons. Four sulfur atoms (two \(\ce{S2O3^2-}\)) each go from +2 to +2.5 and lose 0.5, a total of 2 electrons. [M1]
\(\ce{2S2O3^2- + I2 -> S4O6^2- + 2I-}\) [A1]
(c) \(n(\ce{S2O3^2-}) = 0.100 \times 0.0200 = 2.00 \times 10^{-3}\) mol, so \(n(\ce{I2}) = 1.00 \times 10^{-3}\) mol [M1]; \(c(\ce{I2}) = 1.00 \times 10^{-3} / 0.0250 = 0.0400\) mol dm⁻³ [A1]
Q: [4 marks] ★★★ A student titrates iron(II) ions with potassium manganate(VII) but acidifies the solution with dilute hydrochloric acid instead of dilute sulfuric acid. (a) Write the half-equation for the reaction of chloride ions that causes an error. (b) Explain the effect on the titre and on the calculated concentration of iron(II).
H: Chloride ions are a reducing agent in this mixture. What does that do to the amount of manganate(VII) used?
A: (a) \(\ce{2Cl- -> Cl2 + 2e-}\) [B1]
(b) Chloride ions are oxidised by manganate(VII), so extra manganate(VII) is used up. [B1]
The titre is larger than the amount needed for iron(II) alone. [B1]
So the calculated concentration of iron(II) is too high. [B1]
:::

:::quiz
? In which species does chromium have the oxidation number +6?
- \(\ce{Cr^3+}\)
+ \(\ce{Cr2O7^2-}\)
- \(\ce{Cr2O3}\)
- \(\ce{Cr^2+}\)
> In \(\ce{Cr2O7^2-}\), \(2x + 7(-2) = -2\) gives \(x = +6\). \(\ce{Cr^3+}\) and \(\ce{Cr2O3}\) both contain chromium(III), and \(\ce{Cr^2+}\) is chromium(II).
? In \(\ce{2Fe^2+ + Cl2 -> 2Fe^3+ + 2Cl-}\), which statement is correct?
- \(\ce{Fe^2+}\) is the oxidising agent because it is oxidised.
- \(\ce{Cl2}\) is the reducing agent because it is reduced.
+ \(\ce{Fe^2+}\) is the reducing agent and \(\ce{Cl2}\) is the oxidising agent.
- Both are oxidised because both change oxidation number.
> Iron goes from +2 to +3 (oxidised), so it is the reducing agent. Chlorine goes from 0 to −1 (reduced), so it is the oxidising agent. The agent does the opposite of what happens to it.
? Which of these reactions is a disproportionation?
- \(\ce{Cl2 + 2KBr -> 2KCl + Br2}\)
- \(\ce{CaCO3 -> CaO + CO2}\)
+ \(\ce{2H2O2 -> 2H2O + O2}\)
- \(\ce{Mg + 2HCl -> MgCl2 + H2}\)
> In \(\ce{H2O2}\), oxygen is −1. In water it is −2 (reduced) and in \(\ce{O2}\) it is 0 (oxidised), so one element in one species both gains and loses. The other three are either simple displacements or not redox.
? What is the name of \(\ce{KClO3}\)?
- potassium chlorate(III)
- potassium chlorate(VII)
+ potassium chlorate(V)
- potassium chlorate(I)
> \(+1 + x + 3(-2) = 0\) gives \(x = +5\). The Roman numeral is the oxidation number of chlorine, written without a sign.
? 25.0 cm³ of 0.0500 mol dm⁻³ \(\ce{Fe^2+}\) is titrated with 0.0200 mol dm⁻³ \(\ce{MnO4-}\) in acid. What volume of manganate(VII) is needed?
- 62.5 cm³
- 25.0 cm³
- 2.50 cm³
+ 12.5 cm³
> \(n(\ce{Fe^2+}) = 1.25 \times 10^{-3}\) mol and 1 mol of \(\ce{MnO4-}\) reacts with 5 mol of \(\ce{Fe^2+}\), so \(n(\ce{MnO4-}) = 2.50 \times 10^{-4}\) mol and \(V = 2.50 \times 10^{-4}/0.0200 = 0.0125\) dm³. Ignoring the 1 : 5 ratio (treating the reaction as 1 : 1) gives 62.5 cm³.
? Which is the correct oxidation number of oxygen in \(\ce{H2O2}\)?
- −2, because oxygen is always −2
+ −1, because hydrogen is +1 and the molecule is neutral
- 0, because it is an element
- +1, because it is bonded to hydrogen
> \(2(+1) + 2x = 0\) gives \(x = -1\). Oxygen is −2 in most compounds, but peroxides are the exception.
:::

:::checklist What you can now do
- [ ] I can work out oxidation numbers of elements in compounds and ions, and write them as +n or −n.
- [ ] I can use changes in oxidation number to balance redox equations.
- [ ] I can define redox, oxidation, reduction and disproportionation in terms of electron transfer and oxidation number, and identify them in equations.
- [ ] I can identify oxidising agents and reducing agents.
- [ ] I can name compounds and ions with Roman numerals that show the oxidation number.
- [ ] I can write half-equations in acid and combine them into full ionic equations.
- [ ] I can calculate concentrations and amounts from redox titrations.
:::

:::recap
- Oxidation is loss of electrons (oxidation number increases); reduction is gain of electrons (oxidation number decreases). OIL RIG. They always happen together.
- Oxidation numbers: elements 0; simple ion = its charge; sum = 0 in a compound and = the charge in an ion; F −1, Group 1 +1, Group 2 +2, H +1 (−1 in metal hydrides), O −2 (−1 in peroxides). Written +2, not 2+.
- Roman numerals give the oxidation number: iron(III), manganate(VII), dichromate(VI), chlorate(I), chlorate(V).
- The oxidising agent is reduced; the reducing agent is oxidised.
- Half-equations in acid: balance atoms, then O with \(\ce{H2O}\), H with \(\ce{H+}\), then charge with electrons. Multiply to equalise electrons, add and cancel.
- Key half-equations: \(\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\); \(\ce{Cr2O7^2- + 14H+ + 6e- -> 2Cr^3+ + 7H2O}\); \(\ce{Fe^2+ -> Fe^3+ + e-}\).
- Balancing by oxidation numbers: total increase = total decrease. \(\ce{MnO4-} : \ce{Fe^2+} = 1 : 5\); \(\ce{Cr2O7^2-} : \ce{Fe^2+} = 1 : 6\).
- Disproportionation: one element, one species, oxidised and reduced together: \(\ce{Cl2}\) with cold NaOH gives \(\ce{Cl-}\) and \(\ce{ClO-}\), with hot NaOH gives \(\ce{Cl-}\) and \(\ce{ClO3-}\); \(\ce{2H2O2 -> 2H2O + O2}\).
- Manganate(VII) titrations use dilute sulfuric acid (never hydrochloric acid) and no indicator: colourless to the first permanent pale pink.
:::

:::links
- read: [Redox menu](https://www.chemguide.co.uk/inorganic/redoxmenu.html) · Chemguide · definitions of oxidation and reduction, writing half-equations and ionic equations, and working out oxidation states
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [Chemical equilibria](#chem.equilibria) shows what happens when a reaction can run in both directions.

