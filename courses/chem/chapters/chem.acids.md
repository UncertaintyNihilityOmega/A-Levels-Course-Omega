@chapter chem.acids
@title Acids and bases
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 5–7 hours
@summary What acids and bases are and how strong and weak ones differ. You will learn the Brønsted–Lowry theory, the pH scale, how to compare a strong and a weak acid by experiment, neutralisation and salts, the shape of the four pH titration curves, and how to choose an indicator from its colour-change range.

:::why
Acids and bases are everywhere. Stomach acid digests your lunch, and an indigestion tablet is a base that neutralises the excess. Vinegar, fizzy drinks, batteries, soap, fertilisers and swimming pools are all controlled by pH. Chemists measure how much acid is in a sample by titration, and a good exam answer depends on knowing why a weak acid behaves differently from a strong one and why the choice of indicator matters. This chapter gives you the ideas and the exam wording.
:::

**Before you start**, you should be comfortable with moles and concentration from [Moles and stoichiometry](#chem.moles), including ionic equations and titration calculations, and with dynamic equilibrium and the position of equilibrium from [Chemical equilibria](#chem.equilibria). This chapter stays at AS level: calculating pH, Ka, buffers and conjugate pairs come later in [pH, buffers, solubility product and partition](#chem.acids2).

:::try Warm-up
Q: Calculate the amount of HCl in 25.0 cm³ of hydrochloric acid of concentration 0.100 mol dm⁻³. (from [Moles and stoichiometry](#chem.moles))
A: \(n = cV = 0.100 \times 25.0 / 1000 = 0.00250\) mol.
Q: In \(\ce{N2O4(g) <=> 2NO2(g)}\), what does the double arrow tell you about the reaction, and what does it mean if the position of equilibrium lies far to the left? (from [Chemical equilibria](#chem.equilibria))
A: The reaction is reversible: the forward and reverse reactions both happen. If the position lies far to the left, most of the substance is present as the reactant at equilibrium.
Q: Write the ionic equation for \(\ce{HCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)}\), leaving out the spectator ions. (from [Moles and stoichiometry](#chem.moles))
A: \(\ce{H+(aq) + OH-(aq) -> H2O(l)}\). The ions \(\ce{Na+}\) and \(\ce{Cl-}\) are the same on both sides.
:::

## The acids and alkalis you must know

You already know that acids taste sour and turn indicators red, but chemists define acids by what they do to other particles. First meet the substances. Learn the formulas, because exam questions assume them.

| Acid | Formula | Where you meet it | Strength |
|---|---|---|---|
| hydrochloric acid | \(\ce{HCl}\) | stomach acid, cleaning metals | strong |
| sulfuric acid | \(\ce{H2SO4}\) | car batteries, making fertilisers | strong |
| nitric acid | \(\ce{HNO3}\) | making fertilisers and explosives | strong |
| ethanoic acid | \(\ce{CH3COOH}\) | vinegar | weak |

| Alkali | Formula | Where you meet it | Strength |
|---|---|---|---|
| sodium hydroxide | \(\ce{NaOH}\) | soap making, drain cleaner | strong |
| potassium hydroxide | \(\ce{KOH}\) | liquid soaps, alkaline batteries | strong |
| ammonia solution | \(\ce{NH3}\) | household cleaners, fertilisers | weak |

Hydrochloric and nitric acids each release one \(\ce{H+}\) per molecule, so they are **monoprotic**. Sulfuric acid can release two, so it is **diprotic**. Ethanoic acid has four hydrogen atoms but is monoprotic: only the hydrogen of the \(\ce{-COOH}\) group comes off as \(\ce{H+}\). You will see why in [Carboxylic acids, esters and nitriles](#chem.org.acids).

An **alkali** is a base that dissolves in water. Every alkali is a base, but not every base is an alkali: copper(II) oxide is a base that does not dissolve.

## The pH scale

Acids differ in how acidic their solutions are, and chemists need one number to compare them. That number is the **pH**.

:::def pH
A measure of the acidity of a solution, defined by \(\mathrm{pH} = -\lg[\ce{H+}]\), where \([\ce{H+}]\) is the concentration of hydrogen ions in mol dm⁻³.
:::

You do not calculate pH at AS level (that is in [pH, buffers, solubility product and partition](#chem.acids2)), but two ideas are needed now. First, a **lower pH means more \(\ce{H+}\)**: each step down the scale means ten times more \(\ce{H+}\) ions. Second, pure water contains equal, tiny amounts of \(\ce{H+}\) and \(\ce{OH-}\) ions, \(1.00 \times 10^{-7}\) mol dm⁻³ of each at 298 K, so its pH is 7.

:::key The pH scale
Pure water and neutral solutions: pH 7. Acidic solutions: pH below 7 (the lower the number, the more acidic). Alkaline solutions: pH above 7. The scale usually runs from 0 to 14.
:::

Typical values for solutions at 0.100 mol dm⁻³ are pH 1 for hydrochloric acid and pH 13 for sodium hydroxide. You can measure pH in two ways:

- **Universal indicator** is a mixture of dyes that gives a different colour at each pH: red or orange for strong acids, green near pH 7, blue or purple for strong alkalis. It is quick and cheap but only gives an approximate pH.
- A **pH meter** has a probe that you dip into the solution. It is calibrated with solutions of known pH first and then gives the pH as a number. Use it when you need an accurate value or a pH curve.

## Brønsted–Lowry acids and bases

Acids need not always be in water. The **Brønsted–Lowry theory** works in any solvent and is based on one particle, the proton. A proton is a hydrogen ion \(\ce{H+}\): a hydrogen atom has one proton and one electron, so \(\ce{H+}\) is just a proton.

:::def Brønsted–Lowry acid and base
An acid is a proton donor. A base is a proton acceptor.
:::

When hydrogen chloride dissolves in water, an \(\ce{HCl}\) molecule gives its proton to a water molecule:

\[\ce{HCl + H2O -> H3O+ + Cl-}\]

\(\ce{HCl}\) is the acid, because it donates a proton. \(\ce{H2O}\) is the base, because it accepts one. The ion \(\ce{H3O+}\) is the **oxonium ion** (also called the hydronium ion). Chemists often write \(\ce{H+(aq)}\) as a shorthand for it, and so does the syllabus.

Ammonia is a base because its lone pair on nitrogen accepts a proton. In water:

\[\ce{NH3 + H2O <=> NH4+ + OH-}\]

Now water has given a proton away, so water is the **acid** here, and \(\ce{NH3}\) is the base. A substance that can behave as an acid in one reaction and as a base in another, as water does, is **amphoteric**. The \(\ce{OH-}\) ions explain why a solution of ammonia is alkaline.

:::analogy
Imagine a proton as a ball. The acid is the player who throws it and the base is the player who catches it. Water can play either position. With \(\ce{HCl}\) it catches; with \(\ce{NH3}\) it throws.
:::

:::warn Say "donor" and "acceptor"
The examiner's words are "proton donor" and "proton acceptor". "A base neutralises acids" describes what a base does, not what it is, so it does not score as a definition. An acid donates a hydrogen **ion**, \(\ce{H+}\), not a hydrogen atom.
:::

:::eg In each equation, identify the Brønsted–Lowry acid and the Brønsted–Lowry base on the left-hand side. (a) \(\ce{HNO3 + H2O -> H3O+ + NO3-}\) (b) \(\ce{NH3 + HCl -> NH4+ + Cl-}\) (c) \(\ce{CH3COOH + OH- -> CH3COO- + H2O}\)
Look for the particle that loses a proton (the acid) and the one that gains it (the base).

(a) \(\ce{HNO3}\) loses \(\ce{H+}\) to become \(\ce{NO3-}\): it is the acid. \(\ce{H2O}\) gains \(\ce{H+}\) to become \(\ce{H3O+}\): it is the base. [B1]

(b) \(\ce{HCl}\) loses \(\ce{H+}\) to become \(\ce{Cl-}\): acid. \(\ce{NH3}\) gains \(\ce{H+}\) to become \(\ce{NH4+}\): base. [B1]

(c) \(\ce{CH3COOH}\) loses \(\ce{H+}\) to become \(\ce{CH3COO-}\): acid. \(\ce{OH-}\) gains \(\ce{H+}\) to become \(\ce{H2O}\): base. [B1]
:::

Neutralisation of an acid by an alkali is the same idea in its simplest form. The base is \(\ce{OH-}\), the acid is \(\ce{H+}\), and one proton moves:

\[\ce{H+(aq) + OH-(aq) -> H2O(l)}\]

## Strong and weak: how much of the acid splits up

A solution of an acid in water contains acid molecules and the ions made when they give protons to water. The difference between **strong** and **weak** is how many of the molecules do this.

:::def Strong acid
An acid that is fully (completely) dissociated into ions in aqueous solution.
:::

:::def Weak acid
An acid that is only partially dissociated into ions in aqueous solution.
:::

The same two definitions apply to bases: a **strong base** is fully dissociated or ionised in aqueous solution and a **weak base** is only partially so. The equations show the difference. A strong acid uses a one-way arrow, a weak acid the equilibrium arrow:

\[\ce{HCl(aq) -> H+(aq) + Cl-(aq)}\]
\[\ce{CH3COOH(aq) <=> CH3COO-(aq) + H+(aq)}\]

In ethanoic acid at 0.100 mol dm⁻³ only about one molecule in a hundred has split. The rest stay as molecules. The position of equilibrium lies far to the **left**. Add more ethanoic acid and a new equilibrium is set up; the proportion that splits stays small.

:::html
<figure class="fig small"><svg viewBox="0 4 330 168" role="img" aria-label="Two boxes of particles: in the strong acid box every HA has split into an H plus ion and an A minus ion; in the weak acid box most particles are whole HA molecules with only one H plus ion and one A minus ion"><path class="ln" d="M15 12H145a10 10 0 0 1 10 10V116a10 10 0 0 1-10 10H15a10 10 0 0 1-10-10V22a10 10 0 0 1 10-10Z"/><text class="tl tc ta" x="24" y="38">H⁺</text><text class="tl tc ta" x="52" y="38">A⁻</text><text class="tl tc ta" x="80" y="38">H⁺</text><text class="tl tc ta" x="108" y="38">A⁻</text><text class="tl tc ta" x="136" y="38">H⁺</text><text class="tl tc ta" x="24" y="64">A⁻</text><text class="tl tc ta" x="52" y="64">H⁺</text><text class="tl tc ta" x="80" y="64">A⁻</text><text class="tl tc ta" x="108" y="64">H⁺</text><text class="tl tc ta" x="136" y="64">A⁻</text><text class="tl tc ta" x="24" y="90">H⁺</text><text class="tl tc ta" x="52" y="90">A⁻</text><text class="tl tc ta" x="80" y="90">H⁺</text><text class="tl tc ta" x="108" y="90">A⁻</text><text class="tl tc ta" x="136" y="90">H⁺</text><text class="tl tc ta" x="24" y="116">A⁻</text><text class="tl tc ta" x="52" y="116">H⁺</text><text class="tl tc ta" x="80" y="116">A⁻</text><text class="tl tc ta" x="108" y="116">H⁺</text><text class="tl tc ta" x="136" y="116">A⁻</text><text class="tl tc" x="80" y="146">strong acid:</text><text class="tl tc" x="80" y="163">all HA split</text><path class="ln" d="M185 12H315a10 10 0 0 1 10 10V116a10 10 0 0 1-10 10H185a10 10 0 0 1-10-10V22a10 10 0 0 1 10-10Z"/><text class="tl tc" x="194" y="38">HA</text><text class="tl tc" x="222" y="38">HA</text><text class="tl tc" x="250" y="38">HA</text><text class="tl tc" x="306" y="38">HA</text><text class="tl tc" x="222" y="64">HA</text><text class="tl tc" x="278" y="64">HA</text><text class="tl tc ta" x="306" y="64">H⁺</text><text class="tl tc" x="194" y="90">HA</text><text class="tl tc" x="250" y="90">HA</text><text class="tl tc" x="306" y="90">HA</text><text class="tl tc ta" x="194" y="116">A⁻</text><text class="tl tc" x="250" y="146">weak acid:</text><text class="tl tc" x="250" y="163">most HA stay whole</text></svg><figcaption>The same ten units of acid HA in water, drawn as a picture. In the strong acid every HA has given its proton away. In the weak acid most HA are still whole molecules, and only a few have split into H⁺ and A⁻. The picture exaggerates the weak acid: for 0.100 mol dm⁻³ ethanoic acid only about 1 molecule in 100 splits.</figcaption></figure>
:::

Strong and weak describe the **degree of dissociation**. They say nothing about how much acid is dissolved. That is a different idea, concentration.

:::warn Strong is not the same as concentrated
**Strong** and **weak** describe how far an acid dissociates. **Concentrated** and **dilute** describe how much acid is dissolved in the solution. You can have a dilute solution of a strong acid (0.001 mol dm⁻³ \(\ce{HCl}\)) and a concentrated solution of a weak acid (a very concentrated ethanoic acid). Never write "weak acid = dilute acid".
:::

:::key Strong and weak at a glance
Strong acids: \(\ce{HCl}\), \(\ce{HNO3}\), \(\ce{H2SO4}\). Weak acid: \(\ce{CH3COOH}\). Strong bases: \(\ce{NaOH}\), \(\ce{KOH}\). Weak base: \(\ce{NH3}\). At AS treat sulfuric acid as a strong, diprotic acid: each molecule can supply two \(\ce{H+}\) ions in a reaction.
:::

## Comparing strong and weak acids by experiment

You can tell a strong acid from a weak one with solutions of the **same concentration** (and the same volume and temperature). The weak acid has far fewer \(\ce{H+}\) ions, which affects everything that depends on them. Take 0.100 mol dm⁻³ hydrochloric acid and 0.100 mol dm⁻³ ethanoic acid:

| Test | Strong acid (\(\ce{HCl}\)) | Weak acid (\(\ce{CH3COOH}\)) | Why |
|---|---|---|---|
| pH (pH meter or universal indicator) | about 1.0 | about 2.9 | fewer \(\ce{H+}\) ions in the weak acid, so the pH is higher |
| Electrical conductivity | high | low | fewer ions to carry the current |
| Reaction with magnesium ribbon | vigorous fizzing, fast | slow fizzing | the rate depends on the concentration of \(\ce{H+}\) |
| Volume of \(\ce{H2}\) from excess magnesium | the same for both | the same for both | both contain the same amount of acid |

The last row surprises students. Both samples hold the same number of moles of acid, and a weak acid still has all of its hydrogen to give. As the \(\ce{H+}\) ions are used up by the magnesium, the equilibrium \(\ce{CH3COOH <=> CH3COO- + H+}\) shifts to the right to replace them (Le Chatelier's principle), until all the acid has reacted. The weak acid takes longer, but it gives the same final volume.

:::plot Hydrogen from excess magnesium and equal amounts of acid: a typical result. The weak acid is slower but reaches the same final volume.
--f "30*(1-exp(-x/20))" --f "30*(1-exp(-x/60))" --label "strong acid" --label "weak acid" --x 0 240 --y 0 45 --hline 30 --xlabel "time / s" --ylabel "volume of H₂ / cm³" --legend tr
:::

:::eg (Exam style) 25.0 cm³ of 0.100 mol dm⁻³ hydrochloric acid and 25.0 cm³ of 0.100 mol dm⁻³ ethanoic acid are each added to excess magnesium. (a) Compare the pH values of the two acids and explain the difference. (b) Compare the initial rates of reaction. (c) Calculate the volume of hydrogen produced by each acid, at room conditions.
(a) The hydrochloric acid has the lower pH. [B1] \(\ce{HCl}\) is fully dissociated, so the \(\ce{H+}\) concentration is higher, while ethanoic acid is only partially dissociated. [B1]

(b) The hydrochloric acid reacts faster at the start, because its higher \(\ce{H+}\) concentration means more frequent collisions between \(\ce{H+}\) ions and the magnesium. [B1]

(c) \(\ce{Mg + 2H+ -> Mg^2+ + H2}\), so \(n(\ce{H2}) = \tfrac12 n(\text{acid})\).
\[n(\text{acid}) = 0.100 \times \frac{25.0}{1000} = 0.00250\,\mathrm{mol}\] [M1]
\[V(\ce{H2}) = \tfrac12 \times 0.00250 \times 24.0 = 0.0300\,\mathrm{dm^3} = 30.0\,\mathrm{cm^3}\] [A1]
Both acids give 30.0 cm³, because each contains the same amount of acid and all of it reacts in the end.
:::

:::lab Fair test for a strong and a weak acid
Use the same volume and concentration of each acid, the same temperature, and a piece of magnesium ribbon of the same length (or the same mass of powder) each time. Start timing as the metal goes in and collect the gas in a gas syringe. Magnesium and hydrogen are the hazards: wear eye protection and keep flames away.
:::

## Neutralisation and salts

When an acid reacts with a base, the acid's hydrogen ions are replaced by metal or ammonium ions, and a **salt** forms.

:::def Salt
A compound formed when the hydrogen ions of an acid have been replaced by metal ions or by ammonium ions.
:::

The name of the salt has two parts. The first is the cation from the base (sodium, copper(II), ammonium). The second comes from the acid.

| Acid | Salt it forms | Example |
|---|---|---|
| hydrochloric | chloride | sodium chloride, \(\ce{NaCl}\) |
| sulfuric | sulfate | copper(II) sulfate, \(\ce{CuSO4}\) |
| nitric | nitrate | potassium nitrate, \(\ce{KNO3}\) |
| ethanoic | ethanoate | sodium ethanoate, \(\ce{CH3COONa}\) |

Learn the four ways of making a salt from an acid, because each one is a standard equation to write:

| Reaction | Example | Products |
|---|---|---|
| acid + alkali | \(\ce{HCl + NaOH -> NaCl + H2O}\) | salt + water |
| acid + metal oxide or hydroxide | \(\ce{CuO + H2SO4 -> CuSO4 + H2O}\) | salt + water |
| acid + carbonate | \(\ce{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}\) | salt + water + carbon dioxide |
| acid + reactive metal | \(\ce{Mg + 2HCl -> MgCl2 + H2}\) | salt + hydrogen |

Ammonia is a special case. It is a base but contains no \(\ce{OH-}\) to form water. It simply accepts a proton:

\[\ce{NH3(aq) + HCl(aq) -> NH4Cl(aq)}\]

Only a salt forms, ammonium chloride. This is how ammonium fertilisers such as ammonium nitrate and ammonium sulfate are made: \(\ce{NH3 + HNO3 -> NH4NO3}\) and \(\ce{2NH3 + H2SO4 -> (NH4)2SO4}\).

For a diprotic acid the equation needs two moles of base per mole of acid when both protons are removed:

\[\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}\]

:::eg (Real context) An indigestion tablet contains 0.500 g of magnesium hydroxide, \(\ce{Mg(OH)2}\). Stomach acid is hydrochloric acid. What volume of 0.100 mol dm⁻³ hydrochloric acid can the tablet neutralise?
Write the equation: \(\ce{Mg(OH)2 + 2HCl -> MgCl2 + 2H2O}\). [B1]

\(M_r(\ce{Mg(OH)2}) = 24.3 + 2(16.0 + 1.0) = 58.3\), so \(n(\ce{Mg(OH)2}) = 0.500 / 58.3 = 0.008576\) mol. [M1]

From the equation, \(n(\ce{HCl}) = 2 \times 0.008576 = 0.01715\) mol. [M1]

\[V = \frac{n}{c} = \frac{0.01715}{0.100} = 0.1715\,\mathrm{dm^3} = 172\,\mathrm{cm^3}\] [A1]
:::

## pH titration curves

A **titration curve** (a pH curve) plots the pH of the flask against the volume of base added from the burette. A pH meter, or a data logger with a pH probe, records it. Everything you learnt about titration technique in [Moles and stoichiometry](#chem.moles) still applies: the curve just shows the pH at every point.

Two terms are easy to confuse.

:::def Equivalence point
The point in a titration at which the amount of base added exactly reacts with the amount of acid in the flask, in the ratio shown by the equation.
:::

:::def End point
The point at which the indicator changes colour. If the indicator is well chosen it is at (very nearly) the equivalence point.
:::

Take 25.0 cm³ of an acid of concentration 0.100 mol dm⁻³ in the flask and add a base of the same concentration. The equivalence point is at 25.0 cm³ for a monoprotic acid with a monobasic base, whether the acid is strong or weak: **strength does not change how much base is needed, only the pH.** The amounts in moles decide the equivalence volume.

You need the shape of the four curves. They differ in four places: the pH at the start, the height and position of the steep (vertical) section, the pH at the equivalence point, and the pH at the end.

:::html
<figure class="fig small"><svg viewBox="-5 -4 290 907" role="img" aria-label="Four titration curve sketches of pH against volume of base added, 0 to 50 cubic centimetres: strong acid with strong base, weak acid with strong base, strong acid with weak base and weak acid with weak base. Each has a dashed line at pH 7 and a dot at the equivalence point at 25 cubic centimetres"><path class="ax" d="M41 175V26" marker-end="url(#ahm)"/><path class="ax" d="M41 175H253" marker-end="url(#ahm)"/><text class="tl tc" x="145" y="8">strong acid + strong base</text><text class="tl" x="49" y="32">pH</text><text class="ts" x="31" y="179" text-anchor="end">0</text><text class="ts" x="31" y="106" text-anchor="end">7</text><text class="ts" x="31" y="34" text-anchor="end">14</text><text class="ts tc" x="41" y="189">0</text><text class="ts tc" x="143" y="189">25</text><text class="ts tc" x="245" y="189">50</text><text class="tl tc" x="145" y="205">volume of base added / cm³</text><path class="ln-m thin dash" d="M41 102H245"/><path class="c1 sw2" d="M41 165L49 164L57 163L65 163L72 162L80 161L88 160L96 159L104 158L112 157L119 155L127 153L135 150L137 149L140 146L142 141L143 103L144 64L146 59L149 56L151 55L159 52L167 51L174 49L182 49L190 48L198 47L206 47L214 46L221 46L229 46L237 46L245 45"/><circle class="fi" cx="143" cy="103" r="3.5"/><text class="tl" x="163" y="131">steep part:</text><text class="tl" x="163" y="149">pH 3 to 11</text><g transform="translate(-305 230)"><path class="ax" d="M346 175V26" marker-end="url(#ahm)"/><path class="ax" d="M346 175H558" marker-end="url(#ahm)"/><text class="tl tc" x="450" y="8">weak acid + strong base</text><text class="tl" x="354" y="32">pH</text><text class="ts" x="336" y="179" text-anchor="end">0</text><text class="ts" x="336" y="106" text-anchor="end">7</text><text class="ts" x="336" y="34" text-anchor="end">14</text><text class="ts tc" x="346" y="189">0</text><text class="ts tc" x="448" y="189">25</text><text class="ts tc" x="550" y="189">50</text><text class="tl tc" x="450" y="205">volume of base added / cm³</text><path class="ln-m thin dash" d="M346 102H550"/><path class="c1 sw2" d="M346 145L354 137L362 133L370 131L377 129L385 128L393 126L401 125L409 124L417 122L424 120L432 118L440 115L442 113L445 110L447 105L448 85L449 64L451 59L454 56L456 55L464 52L472 51L479 49L487 49L495 48L503 47L511 47L519 46L526 46L534 46L542 46L550 45"/><circle class="fi" cx="448" cy="85" r="3.5"/><text class="tl" x="468" y="131">steep part:</text><text class="tl" x="468" y="149">pH 6.5 to 11</text></g><g transform="translate(0 220)"><path class="ax" d="M41 415V266" marker-end="url(#ahm)"/><path class="ax" d="M41 415H253" marker-end="url(#ahm)"/><text class="tl tc" x="145" y="248">strong acid + weak base</text><text class="tl" x="49" y="272">pH</text><text class="ts" x="31" y="419" text-anchor="end">0</text><text class="ts" x="31" y="346" text-anchor="end">7</text><text class="ts" x="31" y="274" text-anchor="end">14</text><text class="ts tc" x="41" y="429">0</text><text class="ts tc" x="143" y="429">25</text><text class="ts tc" x="245" y="429">50</text><text class="tl tc" x="145" y="445">volume of base added / cm³</text><path class="ln-m thin dash" d="M41 342H245"/><path class="c1 sw2" d="M41 405L49 404L57 403L65 403L72 402L80 401L88 400L96 399L104 398L112 397L119 395L127 393L135 390L137 389L140 386L142 381L143 360L144 340L146 335L149 332L151 331L159 328L167 326L174 325L182 323L190 323L198 322L206 321L214 321L221 320L229 320L237 320L245 319"/><circle class="fi" cx="143" cy="360" r="3.5"/><text class="tl" x="163" y="371">steep part:</text><text class="tl" x="163" y="389">pH 3 to 7.5</text></g><g transform="translate(-305 450)"><path class="ax" d="M346 415V266" marker-end="url(#ahm)"/><path class="ax" d="M346 415H558" marker-end="url(#ahm)"/><text class="tl tc" x="450" y="248">weak acid + weak base</text><text class="tl" x="354" y="272">pH</text><text class="ts" x="336" y="419" text-anchor="end">0</text><text class="ts" x="336" y="346" text-anchor="end">7</text><text class="ts" x="336" y="274" text-anchor="end">14</text><text class="ts tc" x="346" y="429">0</text><text class="ts tc" x="448" y="429">25</text><text class="ts tc" x="550" y="429">50</text><text class="tl tc" x="450" y="445">volume of base added / cm³</text><path class="ln-m thin dash" d="M346 342H550"/><path class="c1 sw2" d="M346 385L354 377L362 373L370 371L377 369L385 368L393 366L401 365L409 364L417 362L424 360L432 358L440 355L442 353L445 350L447 346L448 342L449 339L451 335L454 332L456 331L464 328L472 326L479 324L487 323L495 323L503 322L511 321L519 321L526 320L534 320L542 320L550 319"/><circle class="fi" cx="448" cy="342" r="3.5"/><text class="tl" x="468" y="371">no steep part:</text><text class="tl" x="468" y="389">pH 6.4 to 7.6</text></g></svg><figcaption>The four pH curves for 25.0 cm³ of 0.100 mol dm⁻³ acid and a base of the same concentration. The dot marks the equivalence point, and the dashed line is pH 7. The steep part is the pH range covered within 0.5 cm³ either side of the equivalence point.</figcaption></figure>
:::

:::key What to say about each curve
| Combination | Starts at | Steep part | pH at equivalence | Suitable indicator |
|---|---|---|---|---|
| strong acid + strong base | low (about 1) | long, pH 3 to 11 | exactly 7 | any in the list: methyl orange, bromophenol blue, thymol blue, thymolphthalein |
| weak acid + strong base | higher (about 3) | pH 6.5 to 11 | above 7 (about 8.7) | thymol blue, thymolphthalein |
| strong acid + weak base | low (about 1) | pH 3 to 7.5 | below 7 (about 5.3) | methyl orange, bromophenol blue |
| weak acid + weak base | higher (about 3) | none: gradual rise | about 7 | none: use a pH meter |
:::

A few more features are worth describing in an answer. The curve for a **weak acid** begins at a higher pH than the strong acid, and then rises gently before the steep part. The curve for a **weak base** ends at a lower pH than the strong base, because the base itself is weaker. After the steep section the pH levels off close to the pH of the base added. For a titration the other way round (acid added to base) the curve is the mirror image: it starts high and falls.

### Why the equivalence point is not always at pH 7

At the equivalence point the flask holds only a salt and water, so it seems that it should be neutral. It is neutral only when both the acid and the base are strong. The salt can react with water:

- Sodium ethanoate (weak acid + strong base) contains the ethanoate ion, \(\ce{CH3COO-}\). This ion is a base: it accepts protons from water and leaves \(\ce{OH-}\) ions in the solution. The pH is **above 7**.
- Ammonium chloride (strong acid + weak base) contains the ammonium ion, \(\ce{NH4+}\). This ion is an acid: it donates protons to water. The pH is **below 7**.
- Sodium chloride (strong acid + strong base) has ions that do neither: pH 7.

You do not need to calculate these pH values at AS level. You do need to state that the equivalence point is above 7, below 7 or at 7, and to choose the indicator accordingly.

Use the widget to draw all four curves. Start with strong acid and strong base, then make the acid weak, then the base weak. Check where the equivalence point and the steep section move, and try each indicator to see whether its band lies inside the steep section.

:::html
<div class="widget" data-w="chem-titration" data-acid="strong" data-base="strong"></div>
:::

:::warn Typical errors with curves
Do not say that the equivalence point of every acid–base titration is pH 7. It is only pH 7 for a strong acid and a strong base. Do not draw the equivalence point at a different volume for a weak acid: with the same concentrations and volumes it is at the same volume. And a weak acid does not start at pH 1: draw the start higher than for the strong acid.
:::

:::eg Sketch the pH curve when 0.100 mol dm⁻³ sodium hydroxide is added from a burette to 25.0 cm³ of 0.100 mol dm⁻³ ethanoic acid, and label the main features.
Axes: pH (0 to 14) on the vertical axis and volume of NaOH added (cm³) on the horizontal axis. [B1]

The curve starts at about pH 3, which is higher than for hydrochloric acid because ethanoic acid is only partially dissociated. [B1]

It rises gently, then steeply: a vertical section from about pH 6.5 to pH 11 at 25.0 cm³. [B1]

The equivalence point is at 25.0 cm³ (\(n(\ce{NaOH}) = n(\ce{CH3COOH})\) at \(0.100 \times 25.0/1000 = 0.00250\) mol each), at a pH above 7. [B1]

After the vertical section the curve levels off at about pH 12 to 13, the pH of the sodium hydroxide solution. [B1]
:::

## Indicators

An **indicator** is a substance whose colour depends on the pH. Indicators are themselves weak acids or weak bases, with the particles in one form (say \(\ce{HIn}\)) having a different colour from the other form (\(\ce{In-}\)). Each changes colour gradually over a **range of about two pH units**, not at a single pH. These are the four indicators in the Cambridge practical list (the colour change is from the acid side to the alkaline side):

| Indicator | pH range | Colour change |
|---|---|---|
| methyl orange | 2.9–4.6 | red to yellow |
| bromophenol blue | 3.0–4.5 | yellow to blue |
| thymol blue | 8.0–9.6 | yellow to blue |
| thymolphthalein | 9.3–10.5 | colourless to blue |

The reason it matters is the steep section. A drop of base can change the pH of the flask by several units near the equivalence point. If the indicator's range lies in that steep section, the colour changes with one drop and the end point is the equivalence point to within a drop. If its range lies outside, the colour changes slowly and early or late over a large volume, and the result is wrong.

:::key Choosing an indicator
The indicator's pH range must lie **within the steep (vertical) section** of the titration curve. The end point is then very close to the equivalence point.
:::

The figure compares the four ranges with the steep sections of the curves you met. Read across: an indicator is suitable if its bar lies inside the bar of the titration.

:::html
<figure class="fig small"><svg viewBox="0 0 340 404" role="img" aria-label="Bars on a pH scale from 0 to 14. Indicator ranges: methyl orange 2.9 to 4.6, bromophenol blue 3.0 to 4.5, thymol blue 8.0 to 9.6, thymolphthalein 9.3 to 10.5. Steep parts of the titration curves: strong acid with strong base 3 to 11, weak acid with strong base 6.5 to 11, strong acid with weak base 3 to 7.5"><path class="ln" d="M20 352V358"/><text class="ts tc" x="20" y="372">0</text><path class="ln" d="M63 352V358"/><text class="ts tc" x="63" y="372">2</text><path class="ln" d="M106 352V358"/><text class="ts tc" x="106" y="372">4</text><path class="ln" d="M149 352V358"/><text class="ts tc" x="149" y="372">6</text><path class="ln" d="M191 352V358"/><text class="ts tc" x="191" y="372">8</text><path class="ln" d="M234 352V358"/><text class="ts tc" x="234" y="372">10</text><path class="ln" d="M277 352V358"/><text class="ts tc" x="277" y="372">12</text><path class="ln" d="M320 352V358"/><text class="ts tc" x="320" y="372">14</text><path class="ax" d="M20 352H336" marker-end="url(#ahm)"/><text class="tl tc" x="170" y="396">pH</text><text class="tl" x="10" y="16">indicator ranges</text><text class="tl" x="20" y="40">methyl orange</text><rect class="fa" x="82" y="46" width="36" height="16" rx="3"/><text class="tl" x="127" y="59">2.9–4.6</text><text class="tl" x="20" y="80">bromophenol blue</text><rect class="fa" x="84" y="86" width="32" height="16" rx="3"/><text class="tl" x="124" y="99">3.0–4.5</text><text class="tl" x="20" y="120">thymol blue</text><rect class="fa" x="191" y="126" width="34" height="16" rx="3"/><text class="tl" x="234" y="139">8.0–9.6</text><text class="tl" x="20" y="160">thymolphthalein</text><rect class="fa" x="219" y="166" width="26" height="16" rx="3"/><text class="tl" x="253" y="179">9.3–10.5</text><text class="tl" x="10" y="210">steep part of the curve</text><text class="tl" x="20" y="234">strong acid + strong base</text><rect class="fm s-acc" x="84" y="240" width="171" height="16" rx="3"/><text class="tl" x="264" y="253">3–11</text><text class="tl" x="20" y="274">weak acid + strong base</text><rect class="fm s-acc" x="159" y="280" width="96" height="16" rx="3"/><text class="tl" x="264" y="293">6.5–11</text><text class="tl" x="20" y="314">strong acid + weak base</text><rect class="fm s-acc" x="84" y="320" width="96" height="16" rx="3"/><text class="tl" x="189" y="333">3–7.5</text></svg><figcaption>Indicator ranges (upper four bars) against the steep parts of the titration curves (lower three bars) on the same pH scale. An indicator is suitable when its bar lies within (or, for methyl orange with a strong acid and strong base, almost within) the bar for the titration. The weak acid with weak base curve has no steep part, so no bar is drawn for it.</figcaption></figure>
:::

From the figure: methyl orange and bromophenol blue lie within the strong acid–weak base titration (pH 3 to 7.5) and the strong–strong one, but they change colour long before the weak acid–strong base steep section starts at pH 6.5. Thymol blue and thymolphthalein lie in the weak acid–strong base titration (pH 6.5 to 11) and in the strong–strong one, but not in the strong acid–weak base one, where they would change colour only well after the equivalence point (long after the pH has stopped changing steeply). For a weak acid with a weak base there is no steep section at all, so no indicator gives a sharp end point. The titration is followed with a pH meter instead.

:::exam Choosing an indicator for full marks
(1) Say which type of titration it is. (2) State the steep section from the graph (read it off the vertical part). (3) Give the indicator whose range lies **within** it. (4) Say why the others are unsuitable: "methyl orange changes colour at pH 2.9 to 4.6, which is before the steep section, so the colour change is gradual and well before the equivalence point". Quote the pH range numbers; "it changes colour at the right pH" earns nothing.
:::

:::eg Sodium hydroxide solution is added to ethanoic acid. Which of methyl orange (2.9–4.6) and thymolphthalein (9.3–10.5) is suitable, and why?
Ethanoic acid is a weak acid and sodium hydroxide a strong base, so the pH at the equivalence point is above 7 and the vertical section is at high pH, from about pH 6.5 to 11. [B1]

Thymolphthalein changes colour between pH 9.3 and 10.5, which lies within the vertical section, so it changes colour sharply at the equivalence point. [B1]

Methyl orange changes colour between pH 2.9 and 4.6, well below the vertical section. The colour would change gradually early in the titration, long before the equivalence point. [B1]
:::

Use only a few drops of indicator. The indicator is itself a weak acid or base, so a large amount would react with the solutions and change the result.

:::eg Spot the error: Ethanoic acid is titrated with sodium hydroxide. A student states that thymolphthalein is a suitable indicator. Explain this choice. [3 marks]
A student wrote this answer.

Line 1: Thymolphthalein is suitable.
Line 2: Ethanoic acid is a weak acid, so the pH at the equivalence point is 7.
Line 3: Thymolphthalein changes colour at pH 9.3 to 10.5, which lies within the vertical section of the titration curve.

Line 1 is correct [B1]. **Line 2 is wrong: the equivalence point is only at pH 7 for a strong acid with a strong base. Ethanoate ions are bases, so the equivalence point of a weak acid with a strong base is above 7 (about 8.7). The mark is lost [B0].** Line 3 is correct and uses the numbers [B1].

Correct line 2: the vertical section is at high pH, about 6.5 to 11, and the equivalence point is above 7. [B1]

The student scores 2 out of 3. The error matters: if the equivalence point really were at pH 7, neither thymolphthalein (9.3–10.5) nor methyl orange (2.9–4.6) would change colour there, so line 2 gives no reason to choose thymolphthalein.
:::

## Titration calculations

The calculation of concentration from a titre uses the steps of [Moles and stoichiometry](#chem.moles): moles of the known solution, ratio from the balanced equation, moles of the unknown, then concentration. The only new point is that the ratio depends on how many protons the acid can donate.

:::steps
1. Write the balanced equation (\(\ce{HCl + NaOH -> NaCl + H2O}\) 1 : 1, but \(\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}\) 1 : 2).
2. Work out the amount of the solution you know: \(n = c \times V\), with V in dm³.
3. Use the equation ratio to find the amount of the other solution.
4. Divide by its volume (in dm³) to get its concentration. Multiply by \(M_r\) if you need g dm⁻³.
:::

Take the mean of the **concordant** titres (within 0.10 cm³) and give your answer to 3 s.f.

:::eg (Real context) Vinegar is a solution of ethanoic acid. 25.0 cm³ of vinegar was diluted to 250 cm³ in a volumetric flask. A 25.0 cm³ sample of the diluted solution needed 21.30 cm³ of 0.100 mol dm⁻³ sodium hydroxide for neutralisation. Calculate the concentration of ethanoic acid in the vinegar, in mol dm⁻³ and in g dm⁻³.
The equation is \(\ce{CH3COOH + NaOH -> CH3COONa + H2O}\), a 1 : 1 ratio. [B1]
\[n(\ce{NaOH}) = 0.100 \times \frac{21.30}{1000} = 0.002130\,\mathrm{mol}\] [M1]
So \(n(\ce{CH3COOH})\) in the 25.0 cm³ sample is also 0.002130 mol.
\[c(\text{diluted}) = \frac{0.002130}{25.0/1000} = 0.0852\,\mathrm{mol\,dm^{-3}}\] [M1]
The solution was diluted ten times (25.0 cm³ to 250 cm³), so the vinegar is ten times as concentrated: \(c = 0.852\) mol dm⁻³. [A1]

\(M_r(\ce{CH3COOH}) = 2(12.0) + 4(1.0) + 2(16.0) = 60.0\). The mass concentration is \(0.852 \times 60.0 = 51.1\) g dm⁻³. [A1]
:::

:::eg (Exam style) In a titration, 25.0 cm³ of sulfuric acid was neutralised by sodium hydroxide of concentration 0.200 mol dm⁻³. The titres were 23.00 (rough), 22.45, 22.40 and 22.40 cm³. Calculate the concentration of the sulfuric acid.
The rough titre is ignored. The three accurate titres are within 0.10 cm³ of each other, so all three are concordant. [M1]
\[\text{mean titre} = \frac{22.45 + 22.40 + 22.40}{3} = 22.42\,\mathrm{cm^3}\]
The equation is \(\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}\). [B1]
\[n(\ce{NaOH}) = 0.200 \times \frac{22.42}{1000} = 0.004483\,\mathrm{mol}\] [M1]
The acid is diprotic, so \(n(\ce{H2SO4}) = \tfrac12 \times 0.004483 = 0.002242\) mol. [M1]
\[c(\ce{H2SO4}) = \frac{0.002242}{25.0/1000} = 0.0897\,\mathrm{mol\,dm^{-3}}\] [A1]
:::

:::try Start easy, finish at exam standard
Q: Define a Brønsted–Lowry base and give one example of a substance that acts as a base in water.
A: A base is a proton acceptor. Example: \(\ce{NH3}\), which accepts \(\ce{H+}\) from water to form \(\ce{NH4+}\) (hydroxide ion is also correct).
Q: Which is the stronger acid, 0.0010 mol dm⁻³ \(\ce{HCl}\) or 2.0 mol dm⁻³ \(\ce{CH3COOH}\)? Explain.
A: Hydrochloric acid is the stronger acid: it is fully dissociated, while ethanoic acid is only partially dissociated. Strength depends on the degree of dissociation, not on the concentration, even though the ethanoic acid solution is far more concentrated.
Q: Write the equation for the reaction between dilute nitric acid and calcium carbonate.
A: \[\ce{CaCO3 + 2HNO3 -> Ca(NO3)2 + H2O + CO2}\]
Q: Two acids of the same concentration are tested: acid X has pH 1.0 and conductivity 'high', acid Y has pH 2.9 and conductivity 'low'. Which is the weak acid? Explain.
A: Y is the weak acid. It has a higher pH, so fewer \(\ce{H+}\) ions, and a lower conductivity, so fewer ions, because it is only partially dissociated.
Q: How many cm³ of 0.100 mol dm⁻³ NaOH are needed to neutralise 20.0 cm³ of 0.100 mol dm⁻³ \(\ce{H2SO4}\)?
A: \(n(\ce{H2SO4}) = 0.100 \times 20.0/1000 = 0.00200\) mol; \(n(\ce{NaOH}) = 2 \times 0.00200 = 0.00400\) mol; \(V = 0.00400 / 0.100 = 0.0400\) dm³ = 40.0 cm³.
Q: Methyl orange and thymolphthalein are available. Which would you use for hydrochloric acid titrated with ammonia solution, and why?
A: Methyl orange. Strong acid with weak base has its vertical section at about pH 3 to 7.5, and methyl orange (pH 2.9–4.6) changes colour within it. Thymolphthalein (9.3–10.5) changes colour above the vertical section.
Q: Explain why the pH at the equivalence point is above 7 when ethanoic acid is titrated with sodium hydroxide.
A: The salt formed is sodium ethanoate. The ethanoate ion is a base: it accepts protons from water, forming \(\ce{OH-}\) ions, so the solution is alkaline.
Q: A student says "a weak acid needs less sodium hydroxide to neutralise it than a strong acid of the same concentration, because it is weaker". Correct this.
A: The same volume is needed. Equal volumes of acids of the same concentration contain the same amount of acid in moles, and each mole needs one mole of NaOH. Strength changes the pH, not the amount of alkali needed.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define (a) a Brønsted–Lowry acid, (b) a strong base.
A: (a) A proton donor. [B1]
(b) A base that is fully dissociated (ionised) in aqueous solution. [B1]
Q: [3 marks] ★ Ammonia reacts with water. (a) Write an equation for the reaction. (b) State the role of water in this reaction.
A: (a) \(\ce{NH3 + H2O <=> NH4+ + OH-}\) [B1] with the equilibrium arrow because ammonia is a weak base, only partially reacting. [B1]
(b) Water acts as a Brønsted–Lowry acid because it donates a proton to ammonia. [B1]
Q: [4 marks] ★★ Hydrochloric acid and ethanoic acid are both 0.100 mol dm⁻³. Describe four differences, or similarities, in the way the two acids behave. Give your answer for pH, conductivity, rate of reaction with magnesium, and the volume of hydrogen from excess magnesium.
H: Use the amount of acid in each sample for the last part.
A: pH: hydrochloric acid has the lower pH (about 1, compared with about 3). [B1]
Conductivity: hydrochloric acid is higher, as it has more ions. [B1]
Rate with magnesium: hydrochloric acid reacts faster because its concentration of \(\ce{H+}\) is greater. [B1]
Volume of hydrogen: the same, because both contain the same amount of acid and all of it eventually reacts. [B1]
Q: [4 marks] ★★ (#chem.moles) An antacid tablet contains 0.500 g of calcium carbonate. Calculate the volume of 0.100 mol dm⁻³ hydrochloric acid that the tablet can neutralise.
H: Write the equation first. The ratio of \(\ce{CaCO3}\) to \(\ce{HCl}\) is not 1 : 1.
A: \(M_r(\ce{CaCO3}) = 40.1 + 12.0 + 3(16.0) = 100.1\) [B1]
\(n(\ce{CaCO3}) = 0.500/100.1 = 0.004995\) mol [M1]
\(\ce{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}\), so \(n(\ce{HCl}) = 2 \times 0.004995 = 0.009990\) mol [M1]
\(V = 0.009990/0.100 = 0.0999\,\mathrm{dm^3} = 99.9\,\mathrm{cm^3}\) [A1]
Q: [5 marks] ★★ (#chem.moles) 25.0 cm³ of sodium hydroxide of concentration 0.150 mol dm⁻³ was neutralised by 18.60 cm³ of sulfuric acid. (a) Write the equation. (b) Calculate the concentration of the sulfuric acid in mol dm⁻³.
A: (a) \(\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}\) [B1]
(b) \(n(\ce{NaOH}) = 0.150 \times 25.0/1000 = 0.003750\) mol [M1]
\(n(\ce{H2SO4}) = \tfrac12 \times 0.003750 = 0.001875\) mol [M1]
\(c = 0.001875 / (18.60/1000) = 0.1008\) mol dm⁻³ [M1]
Concentration \(= 0.101\) mol dm⁻³ (3 s.f.) [A1]
Q: [4 marks] ★★ The pH curve for the titration of a weak acid with a strong base has a vertical section from pH 6.5 to pH 11. Methyl orange (2.9–4.6), bromophenol blue (3.0–4.5), thymol blue (8.0–9.6) and thymolphthalein (9.3–10.5) are available. (a) Which indicators are suitable? (b) Explain why the others are not.
A: (a) Thymol blue [B1] and thymolphthalein [B1], because their colour-change ranges lie within the vertical section.
(b) Methyl orange and bromophenol blue change colour at pH 2.9–4.6, below the vertical section, [B1] so the colour change is gradual and well before the equivalence point. [B1]
Q: [5 marks] ★★ Sketch the pH curve when 0.100 mol dm⁻³ hydrochloric acid is added to 25.0 cm³ of 0.100 mol dm⁻³ ammonia solution, labelling the axes. Mark the equivalence point and say whether its pH is above or below 7.
H: The acid is added to the base, so the curve falls. Where does it start, and what is the salt formed?
A: Axes labelled pH and volume of acid added / cm³. [B1]
Starts at a high pH (about 11) because ammonia is a weak base. [B1]
Vertical section at 25.0 cm³, falling from about pH 7.5 to about pH 3. [B1]
Equivalence point at 25.0 cm³, below pH 7 [B1] because the ammonium ion formed is an acid (it donates protons to water). [B1]
Q: [6 marks] ★★★ Ethanoic acid is a weak acid. (a) Write an equation for its dissociation in water. (b) Explain, using equilibrium ideas, why 25.0 cm³ of 0.100 mol dm⁻³ ethanoic acid needs exactly the same volume of 0.100 mol dm⁻³ sodium hydroxide for neutralisation as 25.0 cm³ of 0.100 mol dm⁻³ hydrochloric acid. (c) State why the pH of the two solutions differs at the start.
H: As \(\ce{OH-}\) removes \(\ce{H+}\), what happens to the position of the equilibrium?
A: (a) \(\ce{CH3COOH <=> CH3COO- + H+}\) [B1]
(b) Both samples contain the same amount of acid (0.00250 mol), and each mole needs one mole of NaOH. [B1] The \(\ce{OH-}\) removes \(\ce{H+}\), so the equilibrium moves to the right, [B1] and more molecules dissociate, until all the ethanoic acid has reacted. [B1]
(c) Ethanoic acid is only partially dissociated, so its \(\ce{H+}\) concentration is lower [B1] and its pH is higher than that of hydrochloric acid, which is fully dissociated. [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ 25.0 cm³ of 0.100 mol dm⁻³ sulfuric acid is titrated with 0.100 mol dm⁻³ sodium hydroxide. At what volume of sodium hydroxide is the equivalence point, and how does it compare with the equivalence point for 25.0 cm³ of 0.100 mol dm⁻³ hydrochloric acid and the same sodium hydroxide? Sketch the shape you expect.
H: How many protons does each acid molecule supply?
A: \(n(\ce{H2SO4}) = 0.100 \times 25.0/1000 = 0.00250\) mol; \(n(\ce{NaOH})\) needed \(= 2 \times 0.00250 = 0.00500\) mol. [M1]
\(V = 0.00500 / 0.100 = 0.0500\) dm³ = 50.0 cm³. [A1]
Hydrochloric acid needs 25.0 cm³, so sulfuric acid needs twice as much, because it is diprotic. [B1]
The curve is the same shape as for a strong acid with a strong base, with the vertical section at 50.0 cm³. [B1]
Q: [5 marks] ★★★ (#chem.moles) A sample of hydrated ethanedioic acid, \(\ce{H2C2O4.xH2O}\), of mass 1.26 g was dissolved in water and made up to 250 cm³. A 25.0 cm³ portion required 20.00 cm³ of 0.100 mol dm⁻³ sodium hydroxide for complete neutralisation (the acid is diprotic). Find x.
H: Find the moles of acid in the 25.0 cm³ portion, then scale up to 250 cm³.
A: \(n(\ce{NaOH}) = 0.100 \times 20.00/1000 = 0.002000\) mol [M1]
\(n(\text{acid}) = \tfrac12 \times 0.002000 = 0.001000\) mol in 25.0 cm³ [M1]
So there is 0.01000 mol in 250 cm³. [M1]
\(M_r = 1.26/0.01000 = 126.0\) [A1]
\(M_r(\ce{H2C2O4}) = 2(1.0) + 2(12.0) + 4(16.0) = 90.0\), so \(18.0x = 36.0\) and \(x = 2\). [A1]
:::

:::quiz
? Which statement defines a Brønsted–Lowry acid?
- A substance that produces hydroxide ions in water
- A substance that accepts a pair of electrons
+ A substance that donates a proton
- A substance with a pH below 7
> A Brønsted–Lowry acid is a proton donor. Producing \(\ce{OH-}\) describes an alkali. A pH below 7 describes a solution, and accepting an electron pair is a different (Lewis) definition.
? In the reaction \(\ce{NH3 + H2O <=> NH4+ + OH-}\) (forward direction), which species is the Brønsted–Lowry acid?
- \(\ce{NH3}\)
+ \(\ce{H2O}\)
- \(\ce{NH4+}\)
- \(\ce{OH-}\)
> Water donates a proton to ammonia, so water is the acid and ammonia the base in the forward reaction.
? Which solution has the highest pH? All have a concentration of 0.100 mol dm⁻³.
- hydrochloric acid
- ethanoic acid
- ammonia solution
+ sodium hydroxide solution
> Acids have a pH below 7. Of the two alkalis, sodium hydroxide is fully dissociated and gives more \(\ce{OH-}\) ions than the partly dissociated ammonia, so its pH is higher.
? A student says that 2.0 mol dm⁻³ ethanoic acid is a strong acid because it is concentrated. What is wrong?
- Ethanoic acid is not an acid
- Concentrated acids are always weak
+ Strength depends on the degree of dissociation, not concentration
- Ethanoic acid is only an acid at low concentration
> Strong and weak describe how much of the acid dissociates. Concentration says how much is dissolved. Ethanoic acid is weak at every concentration.
? Equal volumes of 0.100 mol dm⁻³ hydrochloric acid and 0.100 mol dm⁻³ ethanoic acid are added to excess magnesium. Which statement about the volume of hydrogen at the end is correct?
- Hydrochloric acid gives more hydrogen
- Ethanoic acid gives more hydrogen
+ Both give the same volume
- Ethanoic acid gives none
> Both samples contain the same amount of acid, and the weak acid dissociates further as \(\ce{H+}\) is used up. The rate differs but the final volume does not.
? 20.0 cm³ of 0.100 mol dm⁻³ sulfuric acid is neutralised by 0.100 mol dm⁻³ sodium hydroxide. What volume of sodium hydroxide is needed?
- 10.0 cm³
- 20.0 cm³
+ 40.0 cm³
- 80.0 cm³
> \(\ce{H2SO4}\) needs two moles of NaOH per mole: \(n(\ce{H2SO4}) = 0.00200\) mol, \(n(\ce{NaOH}) = 0.00400\) mol, \(V = 0.00400/0.100 = 0.0400\,\mathrm{dm^3} = 40.0\,\mathrm{cm^3}\).
? Ethanoic acid is titrated with sodium hydroxide. What is true of the pH at the equivalence point?
- It is exactly 7
- It is below 7
+ It is above 7
- It cannot be found
> The salt, sodium ethanoate, contains the ethanoate ion, which is a base, so the solution is alkaline at the equivalence point.
? Which indicator is suitable for titrating hydrochloric acid with ammonia solution?
- thymolphthalein
- thymol blue
+ methyl orange
- none of them
> A strong acid with a weak base has its vertical section at about pH 3 to 7.5. Methyl orange (2.9–4.6) changes colour inside it. Thymol blue and thymolphthalein change colour above it.
? What is the product of the reaction between ammonia and hydrochloric acid?
- ammonium chloride and water
+ ammonium chloride only
- ammonium hydroxide
- nitrogen and hydrogen chloride
> Ammonia accepts a proton: \(\ce{NH3 + HCl -> NH4Cl}\). No water forms, because ammonia has no hydroxide ion to combine with the proton.
:::

:::checklist What you can now do
- [ ] I can recall the common acids (HCl, H₂SO₄, HNO₃, CH₃COOH) and alkalis (NaOH, KOH, NH₃) and say which are strong and weak.
- [ ] I can define Brønsted–Lowry acids and bases and identify the acid and the base in an equation, including water acting as an acid or a base.
- [ ] I can explain what strong and weak mean for acids and bases, with equations, and why strong does not mean concentrated.
- [ ] I can state the pH of water, acids and alkalis and name two ways of measuring pH.
- [ ] I can compare a strong and a weak acid at the same concentration by pH, conductivity, reaction with magnesium and volume of hydrogen formed.
- [ ] I can write the equation for neutralisation, \(\ce{H+(aq) + OH-(aq) -> H2O(l)}\), and for the formation of salts from acids with alkalis, carbonates, oxides and metals.
- [ ] I can sketch the pH curves for strong or weak acid with strong or weak base, and label the equivalence point and the vertical section.
- [ ] I can say whether the pH at equivalence is above, below or at 7 and explain why.
- [ ] I can choose a suitable indicator from its pH range and the steep part of the curve, and explain why others are unsuitable.
- [ ] I can calculate a concentration from a titration, including a diprotic acid.
:::

:::recap
- Brønsted–Lowry acid = proton donor; base = proton acceptor. Alkali = a base that dissolves in water. Water is amphoteric.
- Strong acid or base: fully dissociated (→). Weak: partly dissociated (⇌, far to the left for a weak acid). Strong is not the same as concentrated.
- Common acids: HCl, H₂SO₄, HNO₃ (strong), CH₃COOH (weak). Alkalis: NaOH, KOH (strong), NH₃ (weak).
- pH 7 for water, below 7 acidic, above 7 alkaline. Measured with universal indicator or a pH meter.
- At the same concentration, a weak acid has a higher pH, lower conductivity and slower reaction with magnesium, but gives the same final volume of H₂ from excess magnesium.
- Neutralisation: \(\ce{H+(aq) + OH-(aq) -> H2O(l)}\). Salts from acid + alkali, oxide, carbonate or metal; \(\ce{NH3 + HCl -> NH4Cl}\) forms only a salt.
- Four curves: strong–strong pH 7 at equivalence; weak acid–strong base above 7; strong acid–weak base below 7; weak–weak no sharp end point. Equivalence volume depends on moles, not strength.
- Indicator range must lie within the steep section: methyl orange 2.9–4.6 and bromophenol blue 3.0–4.5 (strong acid–weak base); thymol blue 8.0–9.6 and thymolphthalein 9.3–10.5 (weak acid–strong base); any of the four for strong–strong.
- Titration calculations: n = cV, use the equation ratio (H₂SO₄ : NaOH = 1 : 2), mean of concordant titres.
:::

:::links
- read: [Strong and weak acids](https://www.chemguide.co.uk/physical/acidbaseeqia/acids.html) · Chemguide · what "strong" and "weak" mean, with the equations (the pH and equilibrium-constant parts are A Level)
- read: [pH (titration) curves](https://www.chemguide.co.uk/physical/acidbaseeqia/phcurves.html) · Chemguide · the four curves, equivalence point and end point explained step by step
- read: [Acid-base indicators](https://www.chemguide.co.uk/physical/acidbaseeqia/indicators.html) · Chemguide · how indicators work and how to choose one (assumes the curves above)
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [Reaction kinetics](#chem.kinetics) looks at how fast reactions go, and what you can do to speed them up.
