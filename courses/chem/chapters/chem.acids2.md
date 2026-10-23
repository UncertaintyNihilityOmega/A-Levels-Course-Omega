@chapter chem.acids2
@title pH, buffers, solubility product and partition
@level a2
@paper CAIE 9701 Paper 4
@time 8–10 hours
@summary How to put numbers on acids and bases. You will learn conjugate acid–base pairs, how to calculate the pH of strong acids, strong alkalis and weak acids, how a buffer resists changes in pH and how to find its pH, how to read a weak-acid titration curve with pKa, how the solubility product Ksp predicts solubility and precipitation (including the common ion effect), and how a solute shares itself between two solvents (the partition coefficient).

:::why
Almost every living cell, every swimming pool and every medicine depends on a pH that must stay in a narrow range. Your blood stays at about pH 7.4 because it is buffered, a barium meal is safe to swallow because barium sulfate hardly dissolves at all, and a chemist can pull a product out of a reaction mixture because it prefers one solvent to another. In [Acids and bases](#chem.acids) you met these ideas in words. Here you turn them into numbers, and the numbers are what Paper 4 asks for.
:::

**Before you start**, you should know strong and weak acids and the Brønsted–Lowry theory from [Acids and bases](#chem.acids), the equilibrium constant \(K_c\) and Le Chatelier's principle from [Chemical equilibria](#chem.equilibria), and amount of substance and concentration from [Moles and stoichiometry](#chem.moles). You will also use logarithms: if you want a refresher, see [Logarithms and exponentials](#math.p3.logs) and [Indices, surds and standard form](#math.f.powers).

:::try Warm-up
Q: What is a weak acid? Give an example. (from [Acids and bases](#chem.acids))
A: An acid that is only partially dissociated in aqueous solution, for example ethanoic acid, \(\ce{CH3COOH}\).
Q: Write the \(K_c\) expression for \(\ce{2SO2(g) + O2(g) <=> 2SO3(g)}\) and give its units. (from [Chemical equilibria](#chem.equilibria))
A: \(K_c = \dfrac{[\ce{SO3}]^2}{[\ce{SO2}]^2[\ce{O2}]}\). The units are \(\dfrac{(\text{mol dm}^{-3})^2}{(\text{mol dm}^{-3})^3} = \text{mol}^{-1}\,\text{dm}^3\).
Q: How many moles of \(\ce{NaOH}\) are in 25.0 cm³ of a 0.100 mol dm⁻³ solution? (from [Moles and stoichiometry](#chem.moles))
A: \(n = cV = 0.100 \times 25.0/1000 = 0.00250\) mol.
:::

## Conjugate acid–base pairs

In [Acids and bases](#chem.acids) an acid was a proton donor and a base a proton acceptor. Now look at what is left after the proton has moved. Take ethanoic acid dissolving in water:

\[\ce{CH3COOH + H2O <=> CH3COO- + H3O+}\]

Going left to right, \(\ce{CH3COOH}\) gives a proton away and becomes \(\ce{CH3COO-}\). That ion could take the proton back, so it is a base. Going right to left, \(\ce{H3O+}\) gives a proton to \(\ce{CH3COO-}\) and becomes \(\ce{H2O}\). Every acid–base reaction has **two** such pairs, one on each side.

:::def Conjugate acid and conjugate base
A conjugate base is the species left when an acid has donated a proton; a conjugate acid is the species formed when a base has accepted a proton. An acid and its conjugate base (or a base and its conjugate acid) differ by one \(\ce{H+}\) and form a conjugate acid–base pair.
:::

:::html
<figure class="fig small"><svg viewBox="0 4 340 140" role="img" aria-label="The equilibrium CH3COOH + H2O gives CH3COO- + H3O+, with the pairs marked: CH3COOH (acid 1) and CH3COO- (base 1) form conjugate pair 1, and H2O (base 2) and H3O+ (acid 2) form conjugate pair 2"><path class="ln" d="M45 46V26H215V46"/><text class="tl tc" x="130" y="18">conjugate pair 1</text><text class="tl tc" x="45" y="66">CH₃COOH</text><text class="tl tc" x="93" y="66">+</text><text class="tl tc" x="125" y="66">H₂O</text><path class="ln" d="M150 61H174" marker-end="url(#ah)"/><path class="ln" d="M174 71H150" marker-end="url(#ah)"/><text class="tl tc" x="215" y="66">CH₃COO⁻</text><text class="tl tc" x="263" y="66">+</text><text class="tl tc" x="296" y="66">H₃O⁺</text><text class="tl tc ta" x="45" y="86">acid 1</text><text class="tl tc ta" x="125" y="86">base 2</text><text class="tl tc ta" x="215" y="86">base 1</text><text class="tl tc ta" x="296" y="86">acid 2</text><path class="ln" d="M125 96V116H296V96"/><text class="tl tc" x="210" y="134">conjugate pair 2</text></svg><figcaption>Two conjugate pairs in one equilibrium. Acid 1 and base 1 differ by one H⁺, and so do base 2 and acid 2. The number after "acid" or "base" only says which pair it belongs to.</figcaption></figure>
:::

| Acid | Conjugate base |
|---|---|
| \(\ce{HCl}\) | \(\ce{Cl-}\) |
| \(\ce{CH3COOH}\) | \(\ce{CH3COO-}\) |
| \(\ce{H3O+}\) | \(\ce{H2O}\) |
| \(\ce{NH4+}\) | \(\ce{NH3}\) |
| \(\ce{H2O}\) | \(\ce{OH-}\) |
| \(\ce{H2CO3}\) | \(\ce{HCO3-}\) |
| \(\ce{HCO3-}\) | \(\ce{CO3^2-}\) |

Read the table downwards for a pattern. A **strong acid has a very weak conjugate base**: \(\ce{Cl-}\) has almost no tendency to take a proton back, so \(\ce{HCl}\) is fully dissociated. A **weak acid has a conjugate base that is a base in its own right**: \(\ce{CH3COO-}\) does take protons from water, which is why sodium ethanoate solution is slightly alkaline (see [Acids and bases](#chem.acids)).

:::eg In each equilibrium, label the two conjugate pairs. (a) \(\ce{NH3 + H2O <=> NH4+ + OH-}\) (b) \(\ce{HNO3 + CH3COOH <=> CH3COOH2+ + NO3-}\) (c) \(\ce{HCO3- + H2O <=> CO3^2- + H3O+}\)
In each case find the species that loses \(\ce{H+}\) (acid) and the one it becomes (conjugate base); then the species that gains \(\ce{H+}\) (base) and what it becomes (conjugate acid).

(a) \(\ce{H2O}\) gives \(\ce{H+}\) to \(\ce{NH3}\). Pair 1: \(\ce{NH3}\) (base) and \(\ce{NH4+}\) (its conjugate acid). Pair 2: \(\ce{H2O}\) (acid) and \(\ce{OH-}\) (its conjugate base). [B1]

(b) \(\ce{HNO3}\) is the stronger acid and gives \(\ce{H+}\) to \(\ce{CH3COOH}\), so ethanoic acid acts as a base here. Pair 1: \(\ce{HNO3}\) (acid) and \(\ce{NO3-}\). Pair 2: \(\ce{CH3COOH}\) (base) and \(\ce{CH3COOH2+}\) (its conjugate acid). [B1]

(c) \(\ce{HCO3-}\) loses \(\ce{H+}\). Pair 1: \(\ce{HCO3-}\) (acid) and \(\ce{CO3^2-}\). Pair 2: \(\ce{H2O}\) (base) and \(\ce{H3O+}\). [B1]
:::

:::warn Water and hydrogencarbonate play both roles
Water is the conjugate base of \(\ce{H3O+}\) and the conjugate acid of \(\ce{OH-}\). \(\ce{HCO3-}\) is the conjugate base of \(\ce{H2CO3}\) and the conjugate acid of \(\ce{CO3^2-}\). Such species are amphoteric, so always decide which role they play **in the equation you are given**. A conjugate pair always differs by exactly one proton: \(\ce{NH3}\) and \(\ce{NH4+}\) are a pair, \(\ce{NH3}\) and \(\ce{NH2-}\) would be a different one.
:::

## The pH scale in numbers

At AS level you used the pH scale in words. Now you define it exactly.

:::def pH
\(\mathrm{pH} = -\lg[\ce{H+}]\), where \([\ce{H+}]\) is the hydrogen ion concentration in mol dm⁻³ and \(\lg\) is the logarithm to base 10 (the \(\log_{10}\) button on your calculator).
:::

To go back from pH to concentration, \([\ce{H+}] = 10^{-\mathrm{pH}}\). Two things to see at once. Each step of 1 in pH is a factor of **10** in \([\ce{H+}]\), so pH 3 is ten times more acidic than pH 4. And a *lower* pH means a *higher* \([\ce{H+}]\).

Give pH to **2 decimal places**: the digits after the point in a pH count as the significant figures of \([\ce{H+}]\), so a concentration given to 3 significant figures gives a pH with 2 decimal places.

### Water: \(K_w\)

Pure water ionises very slightly, and this is a dynamic equilibrium:

\[\ce{H2O(l) <=> H+(aq) + OH-(aq)}\]

Its equilibrium expression has no term for water itself, because water is in such large excess that its concentration does not change. What is left is the **ionic product of water**.

:::def Ionic product of water, Kw
\(K_w = [\ce{H+}][\ce{OH-}]\). At 298 K, \(K_w = 1.00 \times 10^{-14}\ \mathrm{mol^2\,dm^{-6}}\).
:::

In pure water each \(\ce{H2O}\) that ionises gives one \(\ce{H+}\) and one \(\ce{OH-}\), so \([\ce{H+}] = [\ce{OH-}]\). Then \([\ce{H+}]^2 = 1.00 \times 10^{-14}\), \([\ce{H+}] = 1.00 \times 10^{-7}\) mol dm⁻³ and the pH is 7.00. That is why 7 is neutral at 298 K. Adding an acid raises \([\ce{H+}]\), and the equilibrium moves left, so \([\ce{OH-}]\) falls; adding an alkali does the opposite. Both ions are always present, and their product stays at \(K_w\).

:::note Neutral is not always pH 7
The ionisation of water is endothermic, so \(K_w\) is larger at higher temperatures. Pure water at 50 °C has \([\ce{H+}] = [\ce{OH-}]\), so it is still neutral, but its pH is below 7. "Neutral means pH 7" is true only at 298 K.
:::

### Strong acids

A strong acid is fully dissociated, so for a monoprotic acid (one \(\ce{H+}\) per molecule) \([\ce{H+}]\) equals the acid concentration: \(\ce{HCl}\), \(\ce{HNO3}\).

:::eg Calculate the pH of 0.0500 mol dm⁻³ hydrochloric acid.
\(\ce{HCl}\) is a strong monoprotic acid, so it is fully dissociated: \([\ce{H+}] = 0.0500\) mol dm⁻³. [B1]
\[\mathrm{pH} = -\lg(0.0500) = 1.30\] [A1]
:::

:::eg Calculate the pH of the solution made by diluting 10.0 cm³ of 0.100 mol dm⁻³ hydrochloric acid to 1.00 dm³ with water.
Amount of \(\ce{HCl}\): \(n = 0.100 \times 10.0/1000 = 1.00 \times 10^{-3}\) mol. [M1]
\[[\ce{H+}] = \frac{1.00 \times 10^{-3}}{1.00} = 1.00 \times 10^{-3}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = 3.00\] [A1]
The solution was diluted 100 times and the pH rose by 2. A strong acid diluted ten times rises by 1.
:::

For sulfuric acid, a question will tell you what to assume. If both protons are treated as fully released, 0.0500 mol dm⁻³ \(\ce{H2SO4}\) gives \([\ce{H+}] = 0.100\) mol dm⁻³ and pH 1.00. (Only the first dissociation of sulfuric acid is complete; the second is not.)

### Strong alkalis

A strong alkali is fully dissociated into \(\ce{OH-}\) ions. You are given \([\ce{OH-}]\), but pH needs \([\ce{H+}]\), and \(K_w\) links them:

\[[\ce{H+}] = \frac{K_w}{[\ce{OH-}]}\]

:::eg Calculate the pH of 0.0200 mol dm⁻³ sodium hydroxide at 298 K.
\(\ce{NaOH}\) is a strong base: \([\ce{OH-}] = 0.0200\) mol dm⁻³. [B1]
\[[\ce{H+}] = \frac{1.00 \times 10^{-14}}{0.0200} = 5.00 \times 10^{-13}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = -\lg(5.00 \times 10^{-13}) = 12.30\] [A1]
:::

At 298 K there is a shortcut that gives the same answer: \(\mathrm{pH} = 14 + \lg[\ce{OH-}]\). (Taking \(-\lg\) of \(K_w/[\ce{OH-}]\) gives \(-\lg K_w + \lg[\ce{OH-}] = 14 + \lg[\ce{OH-}]\).) For \(0.0200\) mol dm⁻³ this is \(14 - 1.70 = 12.30\). Learn the method with \(K_w\) first, because it also works when a question gives \(K_w\) at another temperature.

:::warn Count the hydroxide ions
\(\ce{Ba(OH)2}\) gives **two** \(\ce{OH-}\) per formula unit, so 0.0250 mol dm⁻³ \(\ce{Ba(OH)2}\) has \([\ce{OH-}] = 0.0500\) mol dm⁻³. And never write "pH = −lg[OH⁻]": that gives a number that is not the pH. \(\ce{NaOH}\) of concentration 0.0200 mol dm⁻³ has pH 12.30, not 1.70.
:::

### Mixing an acid and an alkali

When you mix a strong acid and a strong alkali, they react in the ratio 1 : 1, \(\ce{H+ + OH- -> H2O}\). Work in **amounts**, find which is in excess, and divide by the **total** volume.

:::eg (Exam style) 25.0 cm³ of 0.100 mol dm⁻³ hydrochloric acid is mixed with 15.0 cm³ of 0.100 mol dm⁻³ sodium hydroxide. Calculate the pH of the mixture. [4 marks]
\(n(\ce{H+}) = 0.100 \times 25.0/1000 = 2.50 \times 10^{-3}\) mol and \(n(\ce{OH-}) = 0.100 \times 15.0/1000 = 1.50 \times 10^{-3}\) mol. [M1]
Acid is in excess: \(2.50 \times 10^{-3} - 1.50 \times 10^{-3} = 1.00 \times 10^{-3}\) mol of \(\ce{H+}\) left. [M1]
\[[\ce{H+}] = \frac{1.00 \times 10^{-3}}{40.0/1000} = 0.0250\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = 1.60\] [A1]
:::

## Weak acids: \(K_a\) and \(\mathrm{p}K_a\)

A weak acid \(\ce{HA}\) is only partly dissociated, so its \([\ce{H+}]\) is *not* the acid concentration. You must use the equilibrium:

\[\ce{HA(aq) <=> H+(aq) + A-(aq)}\]

:::def Acid dissociation constant, Ka
For the dissociation \(\ce{HA <=> H+ + A-}\), \(K_a = \dfrac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}\) at equilibrium, in mol dm⁻³. The larger \(K_a\) is, the further the acid is dissociated and the stronger it is.
:::

:::def pKa
\(\mathrm{p}K_a = -\lg K_a\), so \(K_a = 10^{-\mathrm{p}K_a}\).
:::

\(K_a\) values are small and awkward (1.74 × 10⁻⁵), so chemists often quote \(\mathrm{p}K_a\) (4.76). Because of the minus sign, **a smaller \(\mathrm{p}K_a\) means a stronger acid**, and one unit of \(\mathrm{p}K_a\) is a factor of 10 in \(K_a\). Exam questions give \(K_a\) or \(\mathrm{p}K_a\) as data. The values below are the ones used in this chapter.

| Acid | \(K_a\) / mol dm⁻³ | \(\mathrm{p}K_a\) |
|---|---|---|
| chloroethanoic acid, \(\ce{CH2ClCOOH}\) | \(1.38 \times 10^{-3}\) | 2.86 |
| methanoic acid, \(\ce{HCOOH}\) | \(1.78 \times 10^{-4}\) | 3.75 |
| ethanoic acid, \(\ce{CH3COOH}\) | \(1.74 \times 10^{-5}\) | 4.76 |
| propanoic acid, \(\ce{CH3CH2COOH}\) | \(1.35 \times 10^{-5}\) | 4.87 |

Chloroethanoic acid is the strongest of the four because the electronegative chlorine atom pulls electron density away from the carboxylate group, which stabilises the \(\ce{CH2ClCOO-}\) ion and makes the acid release \(\ce{H+}\) more readily (see [Carboxylic acids, esters and nitriles](#chem.org.acids)).

### The pH of a weak acid

Two assumptions turn the awkward expression into a simple one. Take a solution of \(\ce{HA}\) of concentration \(c\).

:::steps
1. The only significant source of \(\ce{H+}\) is the acid, and each \(\ce{HA}\) that dissociates gives one \(\ce{H+}\) and one \(\ce{A-}\). So \([\ce{H+}] = [\ce{A-}]\). (The \(\ce{H+}\) from the ionisation of water is negligible.)
2. The acid is weak, so very little dissociates and the equilibrium \([\ce{HA}]\) is almost the original concentration: \([\ce{HA}] \approx c\).
3. Put both into \(K_a\): \(K_a = \dfrac{[\ce{H+}]^2}{c}\).
:::

:::formula pH of a weak acid
\[[\ce{H+}] = \sqrt{K_a \times c}\]
\(K_a\) is the acid dissociation constant (mol dm⁻³) and \(c\) the concentration of the acid (mol dm⁻³). Then \(\mathrm{pH} = -\lg[\ce{H+}]\).
:::

:::eg (Exam style) Calculate the pH of 0.100 mol dm⁻³ ethanoic acid, \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³. [3 marks]
\(\ce{CH3COOH <=> H+ + CH3COO-}\), with \([\ce{H+}] = [\ce{CH3COO-}]\) and \([\ce{CH3COOH}] \approx 0.100\) mol dm⁻³. [B1]
\[[\ce{H+}] = \sqrt{1.74 \times 10^{-5} \times 0.100} = 1.319 \times 10^{-3}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = -\lg(1.319 \times 10^{-3}) = 2.88\] [A1]
Check the assumption: \(1.319 \times 10^{-3}/0.100 = 1.3\,\%\) of the acid has dissociated, so \([\ce{HA}] \approx c\) is justified. In [Acids and bases](#chem.acids) the same acid had a pH "about 2.9" at this concentration: now you can calculate it.
:::

:::key When the approximations hold
The weak-acid formula needs (1) \([\ce{H+}] = [\ce{A-}]\), which fails if the acid is so dilute that the \(\ce{H+}\) from water matters, and (2) \([\ce{HA}] \approx c\), which fails if a large fraction (more than a few per cent) of the acid has dissociated. In 9701 questions the approximations are allowed unless the question says otherwise: state them in your answer.
:::

Compare equal concentrations, 0.100 mol dm⁻³: hydrochloric acid has pH 1.00, ethanoic acid pH 2.88. The weak acid's \([\ce{H+}]\) is only 1.3 % of the strong acid's.

### Finding \(K_a\) from a measured pH

Run the formula backwards. A pH meter gives \([\ce{H+}] = 10^{-\mathrm{pH}}\); the stoichiometry gives \([\ce{A-}] = [\ce{H+}]\); and \([\ce{HA}] \approx c\).

:::eg (Exam style) A 0.250 mol dm⁻³ solution of a weak acid HX has a pH of 2.60. Calculate \(K_a\) for HX. [4 marks]
\([\ce{H+}] = 10^{-2.60} = 2.512 \times 10^{-3}\) mol dm⁻³. [M1]
\([\ce{X-}] = [\ce{H+}]\) and \([\ce{HX}] \approx 0.250\) mol dm⁻³ (very little has dissociated). [B1]
\[K_a = \frac{[\ce{H+}]^2}{[\ce{HX}]} = \frac{(2.512 \times 10^{-3})^2}{0.250} = 2.52 \times 10^{-5}\ \mathrm{mol\,dm^{-3}}\] [M1 A1]
If the question also asks for \(\mathrm{p}K_a\): \(-\lg(2.524 \times 10^{-5}) = 4.60\). Use the unrounded \(K_a\), not 2.52 × 10⁻⁵.
:::

### What happens when you dilute

Dilution changes a strong acid and a weak acid by different amounts. For a weak acid \([\ce{H+}] = \sqrt{K_a c}\), so diluting 10 times divides \([\ce{H+}]\) by \(\sqrt{10} = 3.16\), not by 10. The pH rises by only **0.50**.

:::eg Calculate the pH of 0.0100 mol dm⁻³ ethanoic acid, and compare the change from 0.100 mol dm⁻³ with the change for hydrochloric acid on the same dilution.
\([\ce{H+}] = \sqrt{1.74 \times 10^{-5} \times 0.0100} = 4.171 \times 10^{-4}\) mol dm⁻³, so pH = 3.38. [M1 A1]
Ethanoic acid: 2.88 to 3.38, a rise of 0.50. Hydrochloric acid: 1.00 to 2.00, a rise of 1.00. [B1]
A weak acid dissociates *more* when it is diluted (the equilibrium moves to the side with more particles), so its \(\ce{H+}\) concentration falls less than the dilution factor. [B1]
:::

:::eg Spot the error: Calculate the pH of 0.0100 mol dm⁻³ ethanoic acid, \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³. [3 marks]
A student wrote this answer.

Line 1: Ethanoic acid is a weak acid, so it is only partially dissociated.
Line 2: \([\ce{H+}] = 0.0100\) mol dm⁻³, so \(\mathrm{pH} = -\lg 0.0100 = 2.00\).

Line 1 is correct [B1]. **Line 2 is wrong: \([\ce{H+}] = c\) is true only for a strong acid. For a weak acid the student must use \(K_a\), so the method mark is lost [M0] and so is the accuracy mark [A0].** The question supplied \(K_a\), which is the clue that the weak-acid method is needed.

Correct line 2: \([\ce{H+}] = \sqrt{K_a c} = \sqrt{1.74 \times 10^{-5} \times 0.0100} = 4.17 \times 10^{-4}\) mol dm⁻³ [M1], so pH = 3.38 [A1].

The student scores 1 out of 3. If the question gives you \(K_a\) and the word "weak", the answer is never the strong-acid pH.
:::

## Buffer solutions

Some systems must hold their pH steady. Blood must stay between about pH 7.35 and 7.45; an enzyme in a cell, a shampoo and an injected medicine all need the pH to stay near a set value even when small amounts of acid or alkali get in. A **buffer solution** does this.

:::def Buffer solution
A solution that minimises changes in pH when small amounts of acid or alkali are added (or when it is diluted).
:::

A buffer does not hold the pH *exactly* constant, and it does not work for large additions. It **minimises** the change.

### How a buffer is made

A buffer needs two things in the same solution: a particle that can **remove added \(\ce{H+}\)** and one that can **remove added \(\ce{OH-}\)**. A weak acid and its conjugate base do exactly this. There are two ways to make one.

- **A weak acid plus a salt of that acid**: for example ethanoic acid and sodium ethanoate, \(\ce{CH3COOH + CH3COONa}\). The salt is fully dissociated, so it supplies plenty of \(\ce{CH3COO-}\); the acid supplies \(\ce{CH3COOH}\).
- **A weak acid partly neutralised by a strong alkali**: add sodium hydroxide to *excess* ethanoic acid. Some of the acid is converted to ethanoate ions, \(\ce{CH3COOH + OH- -> CH3COO- + H2O}\), and the rest of the acid is left. (If you add enough alkali to neutralise *all* the acid, there is no weak acid left and it is no longer a buffer.)

Either way the mixture contains a large amount of \(\ce{CH3COOH}\) **and** a large amount of \(\ce{CH3COO-}\). The acid is only slightly dissociated, and the ethanoate ions from the salt push the equilibrium \(\ce{CH3COOH <=> H+ + CH3COO-}\) further to the left. So almost all of the acid is present as undissociated \(\ce{CH3COOH}\), and almost all of the ethanoate comes from the salt.

### How a buffer works

:::html
<figure class="fig small"><svg viewBox="0 6 340 250" role="img" aria-label="A buffer holds two reservoirs. When acid, H+, is added it is removed by the conjugate base CH3COO-, forming CH3COOH. When alkali, OH-, is added it is removed by CH3COOH, forming CH3COO- and water"><text class="tl tc" x="170" y="22">small amount of acid added (H⁺)</text><path class="ln" d="M170 30V54" marker-end="url(#ah)"/><rect class="fm" x="70" y="60" width="200" height="38" rx="8"/><text class="tl tc" x="170" y="84">CH₃COO⁻ (conjugate base)</text><text class="tl tc" x="170" y="118">CH₃COO⁻ + H⁺ → CH₃COOH</text><text class="tl tc" x="170" y="156">small amount of alkali added (OH⁻)</text><path class="ln" d="M170 164V188" marker-end="url(#ah)"/><rect class="fm" x="70" y="194" width="200" height="38" rx="8"/><text class="tl tc" x="170" y="218">CH₃COOH (weak acid)</text><text class="tl tc" x="170" y="252">CH₃COOH + OH⁻ → CH₃COO⁻ + H₂O</text></svg><figcaption>The two reservoirs of an ethanoic acid and ethanoate buffer. Added H⁺ is removed by the ethanoate ions; added OH⁻ is removed by the ethanoic acid. Each box holds far more than is added, so the ratio between them hardly changes.</figcaption></figure>
:::

The key equations for a buffer of ethanoic acid and sodium ethanoate:

\[\ce{CH3COO-(aq) + H+(aq) -> CH3COOH(aq)}\quad\text{(added acid is removed)}\]
\[\ce{CH3COOH(aq) + OH-(aq) -> CH3COO-(aq) + H2O(l)}\quad\text{(added alkali is removed)}\]

:::steps
1. **Acid added.** The extra \(\ce{H+}\) combines with the ethanoate ions: the equilibrium \(\ce{CH3COOH <=> H+ + CH3COO-}\) shifts to the left. A small amount of \(\ce{CH3COO-}\) is used up and a small amount of \(\ce{CH3COOH}\) made.
2. **Alkali added.** The extra \(\ce{OH-}\) reacts with \(\ce{H+}\) (to form water) and with the ethanoic acid. The acid dissociates a little more to replace the \(\ce{H+}\): the equilibrium shifts to the right.
3. In both cases the amounts of acid and ethanoate each change by a **small fraction** of what is there, so their ratio, and so \([\ce{H+}]\), hardly changes.
:::

### The pH of a buffer

The weak-acid expression still holds. Rearrange \(K_a = \dfrac{[\ce{H+}][\ce{A-}]}{[\ce{HA}]}\) to make \([\ce{H+}]\) the subject:

:::formula pH of a buffer
\[[\ce{H+}] = K_a \times \frac{[\ce{HA}]}{[\ce{A-}]}\]
\([\ce{HA}]\) is the concentration of the weak acid and \([\ce{A-}]\) that of its conjugate base. Then \(\mathrm{pH} = -\lg[\ce{H+}]\).
:::

Here \([\ce{HA}]\) is almost the amount of acid you put in, and \([\ce{A-}]\) almost the amount of salt (or of ions made by adding alkali), because the equilibrium has so little effect on either. The two share the **same volume**, so the volume cancels in the ratio and you may use *amounts* (moles) directly. This also explains why adding water to a buffer does not change its pH.

Two special cases tell you what a buffer is doing. If \([\ce{HA}] = [\ce{A-}]\), the ratio is 1 and \([\ce{H+}] = K_a\), so **the pH of the buffer equals the \(\mathrm{p}K_a\) of the acid**. A buffer is most effective when the two concentrations are not too different, so a good buffer for a given pH uses an acid whose \(\mathrm{p}K_a\) is close to it.

:::note The logarithm form
Taking \(-\lg\) of the buffer expression gives \(\mathrm{pH} = \mathrm{p}K_a + \lg\dfrac{[\ce{A-}]}{[\ce{HA}]}\). It is the same result and some textbooks quote it. The 9701 syllabus gives the \([\ce{H+}]\) form, and both are accepted.
:::

:::eg (Exam style) A buffer is made by mixing 50.0 cm³ of 0.200 mol dm⁻³ ethanoic acid with 50.0 cm³ of 0.100 mol dm⁻³ sodium ethanoate. Calculate its pH. \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³. [3 marks]
After mixing, the total volume is 100.0 cm³, so both concentrations halve: \([\ce{CH3COOH}] = 0.100\) mol dm⁻³ and \([\ce{CH3COO-}] = 0.0500\) mol dm⁻³. (Using amounts gives the same ratio: 0.0100 mol and 0.00500 mol.) [B1]
\[[\ce{H+}] = K_a \times \frac{[\ce{HA}]}{[\ce{A-}]} = 1.74 \times 10^{-5} \times \frac{0.100}{0.0500} = 3.48 \times 10^{-5}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = 4.46\] [A1]
:::

:::eg (Exam style) Calculate the pH of the buffer made by adding 40.0 cm³ of 0.500 mol dm⁻³ sodium hydroxide to 100 cm³ of 0.500 mol dm⁻³ ethanoic acid. \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³. [4 marks]
\(n(\ce{CH3COOH})\) at the start \(= 0.500 \times 100/1000 = 0.0500\) mol; \(n(\ce{NaOH}) = 0.500 \times 40.0/1000 = 0.0200\) mol. [B1]
The alkali reacts 1 : 1 with the acid, \(\ce{CH3COOH + OH- -> CH3COO- + H2O}\), so \(n(\ce{CH3COO-}) = 0.0200\) mol and \(n(\ce{CH3COOH})\) left \(= 0.0500 - 0.0200 = 0.0300\) mol. [M1]
\[[\ce{H+}] = 1.74 \times 10^{-5} \times \frac{0.0300}{0.0200} = 2.61 \times 10^{-5}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = 4.58\] [A1]
The acid is in excess, so this is a buffer. Both amounts are in the same 140 cm³, which is why the volume cancels.
:::

:::eg (Exam style) How much sodium ethanoate must be dissolved in 250 cm³ of 0.200 mol dm⁻³ ethanoic acid to make a buffer of pH 5.00? \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³. Ignore any change in volume. [4 marks]
\([\ce{H+}] = 10^{-5.00} = 1.00 \times 10^{-5}\) mol dm⁻³. [M1]
Rearrange: \(\dfrac{[\ce{A-}]}{[\ce{HA}]} = \dfrac{K_a}{[\ce{H+}]} = \dfrac{1.74 \times 10^{-5}}{1.00 \times 10^{-5}} = 1.74\). [M1]
\(n(\ce{CH3COOH}) = 0.200 \times 250/1000 = 0.0500\) mol, so \(n(\ce{CH3COO-}) = 1.74 \times 0.0500 = 0.0870\) mol. [M1]
\(M_r(\ce{CH3COONa}) = 2(12.0) + 3(1.0) + 2(16.0) + 23.0 = 82.0\), so the mass is \(0.0870 \times 82.0 = 7.13\) g. [A1]
:::

### What a small addition does

The best way to see buffer action is to compare a buffer with plain water, in numbers.

:::eg (Exam style) A buffer, 1.00 dm³, contains 0.500 mol of ethanoic acid and 0.500 mol of sodium ethanoate. (a) Find its pH. (b) 0.0100 mol of hydrogen chloride is added. Find the new pH, ignoring any change in volume. (c) Compare this with adding the same amount of hydrogen chloride to 1.00 dm³ of pure water. [6 marks]
(a) The ratio is 1, so \([\ce{H+}] = K_a = 1.74 \times 10^{-5}\) mol dm⁻³ and \(\mathrm{pH} = \mathrm{p}K_a = 4.76\). [A1]
(b) The added \(\ce{H+}\) reacts with the ethanoate: \(n(\ce{CH3COO-}) = 0.500 - 0.0100 = 0.490\) mol and \(n(\ce{CH3COOH}) = 0.500 + 0.0100 = 0.510\) mol. [M1 A1]
\[[\ce{H+}] = 1.74 \times 10^{-5} \times \frac{0.510}{0.490} = 1.811 \times 10^{-5}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = 4.74\] [A1]
The pH has fallen by only 0.02.
(c) In pure water, \([\ce{H+}] = 0.0100\) mol dm⁻³, so pH = 2.00. The pH falls from 7.00 to 2.00, a change of 5.00. [B1]
:::

Do the same with 0.0100 mol of added sodium hydroxide: \(n(\ce{CH3COO-}) = 0.510\) mol, \(n(\ce{CH3COOH}) = 0.490\) mol, \([\ce{H+}] = 1.74 \times 10^{-5} \times 0.490/0.510 = 1.672 \times 10^{-5}\) and the pH rises to 4.78. Again the change is 0.02, in the opposite direction.

:::warn Buffer mistakes
A buffer does **not** "keep the pH constant" or "stop the pH changing": it *minimises* the change, and only for *small* additions. It does not "neutralise" the added acid either: the conjugate base *removes* \(\ce{H+}\) and the weak acid removes \(\ce{OH-}\). In an explanation, always name **both** species, give **both** equations, and say that the *ratio* \([\ce{HA}]/[\ce{A-}]\) hardly changes, so \([\ce{H+}]\) hardly changes. A mixture of a weak acid and a *strong* alkali is a buffer only if the acid is in excess; if the alkali neutralises all of the acid, the buffer is gone.
:::

### Buffers in the body: blood

Blood is buffered by dissolved carbon dioxide, which acts as the weak acid \(\ce{H2CO3}\), and by hydrogencarbonate ions, \(\ce{HCO3-}\). The system is a pair of linked equilibria:

\[\ce{H+(aq) + HCO3-(aq) <=> H2CO3(aq) <=> H2O(l) + CO2(g)}\]

:::steps
1. If acid enters the blood (from exercise, for example), the \(\ce{HCO3-}\) removes the extra \(\ce{H+}\), pushing the equilibrium to the right: \(\ce{H+ + HCO3- -> H2CO3}\). The \(\ce{H2CO3}\) breaks down to water and \(\ce{CO2}\), and the lungs breathe the carbon dioxide out.
2. If alkali enters, the \(\ce{H2CO3}\) provides \(\ce{H+}\) to remove it: \(\ce{H2CO3 + OH- -> HCO3- + H2O}\), and more \(\ce{CO2}\) dissolves to replace the acid.
:::

Blood contains about twenty times more \(\ce{HCO3-}\) than dissolved \(\ce{CO2}\) at pH 7.4, so it has far more capacity to remove acid than alkali, which suits a body that makes acids as it burns food. Other uses: buffers of known pH are used to **calibrate pH meters** (see [Acids and bases](#chem.acids)); they keep the pH right for enzymes in biological washing powders and in the fermentation of foods and drinks; they keep injected medicines and eye drops at a pH the body tolerates; and they are added to shampoos and some foods to control acidity.

## Titration curves, revisited with pKa

In [Acids and bases](#chem.acids) you drew the curve for ethanoic acid and sodium hydroxide and noticed that it rises gently before the steep part. That gentle section is a **buffer region**: after some alkali has been added, the flask holds both unreacted ethanoic acid and ethanoate ions. Now you can say exactly what the pH is at each point.

:::html
<div class="widget" data-w="chem-titration" data-acid="weak" data-base="strong" data-pka="4.76"></div>
:::

The \(\mathrm{p}K_a\) slider is set to 4.76, the value for ethanoic acid. Move the "Volume of base added" slider to half the equivalence volume and read the pH, then change the \(\mathrm{p}K_a\) slider and watch the half-equivalence point follow it.

:::key The half-equivalence point
Half the acid has been neutralised when the volume of alkali added is **half the equivalence volume**. Then \([\ce{HA}] = [\ce{A-}]\), the ratio is 1, \([\ce{H+}] = K_a\), and
\[\mathrm{pH} = \mathrm{p}K_a\]
So the \(\mathrm{p}K_a\) of a weak acid is the pH read from the titration curve at half the volume needed to reach the equivalence point.
:::

Here is the full set of calculations for 25.0 cm³ of 0.100 mol dm⁻³ ethanoic acid titrated with 0.100 mol dm⁻³ sodium hydroxide. The acid amount is \(0.100 \times 25.0/1000 = 2.50 \times 10^{-3}\) mol, so the equivalence volume is 25.0 cm³.

| Volume of NaOH / cm³ | What is in the flask | How to calculate | pH |
|---|---|---|---|
| 0 | weak acid only | \(\sqrt{K_a c}\) | 2.88 |
| 10.0 | acid in excess, ethanoate: buffer | ratio \(0.00150/0.00100\) | 4.58 |
| 12.5 | half-equivalence: equal \([\ce{HA}]\), \([\ce{A-}]\) | \(\mathrm{pH} = \mathrm{p}K_a\) | 4.76 |
| 20.0 | mostly ethanoate: buffer | ratio \(0.000500/0.00200\) | 5.36 |
| 25.0 | only ethanoate ions | equivalence point: above 7 | about 8.7 |
| 30.0 | excess strong alkali | \([\ce{OH-}] = 5.00 \times 10^{-4}\,\text{mol}/55.0\,\text{cm}^3\) | 11.96 |

The widget calculates with a fuller model, so its readings agree with this table to about 0.1; at the equivalence point and beyond the pH rises very quickly with each drop. Notice where the table's methods change. Before the equivalence point you are in a weak acid or buffer calculation. After it, the pH comes from the excess **strong** alkali, and the weak acid no longer matters.

:::eg (Exam style) 25.0 cm³ of a weak acid HA is titrated with 0.100 mol dm⁻³ sodium hydroxide. The equivalence point is reached after 20.0 cm³, and the pH of the flask after 10.0 cm³ of alkali has been added is 4.20. Calculate the concentration of the acid, and \(K_a\). [4 marks]
\(n(\ce{NaOH}) = 0.100 \times 20.0/1000 = 2.00 \times 10^{-3}\) mol = \(n(\ce{HA})\) (1 : 1). [M1]
\[c(\ce{HA}) = \frac{2.00 \times 10^{-3}}{25.0/1000} = 0.0800\ \mathrm{mol\,dm^{-3}}\] [A1]
10.0 cm³ is **half** the equivalence volume, so this is the half-equivalence point and \(\mathrm{pH} = \mathrm{p}K_a = 4.20\). [M1]
\[K_a = 10^{-4.20} = 6.31 \times 10^{-5}\ \mathrm{mol\,dm^{-3}}\] [A1]
:::

:::tip Choosing a buffer or an indicator
For a buffer you want the acid's \(\mathrm{p}K_a\) close to the pH you need, so that a roughly 1 : 1 mixture can be used. For an indicator in a titration you want its colour change to lie inside the steep part of the curve (see [Acids and bases](#chem.acids)). Different jobs, same curve.
:::

:::key Which pH method?
Decide what is in the flask first, then choose the method.

| What is in the solution | Method | Example in this chapter |
|---|---|---|
| strong monoprotic acid | \([\ce{H+}] = c\) | 0.0500 mol dm⁻³ HCl: pH 1.30 |
| strong alkali | \([\ce{OH-}] = c\) (times the number of \(\ce{OH-}\) per formula unit), then \([\ce{H+}] = K_w/[\ce{OH-}]\) | 0.0200 mol dm⁻³ NaOH: pH 12.30 |
| weak acid alone | \([\ce{H+}] = \sqrt{K_a c}\) | 0.100 mol dm⁻³ ethanoic acid: pH 2.88 |
| weak acid with its salt, or part-neutralised by alkali | \([\ce{H+}] = K_a[\ce{HA}]/[\ce{A-}]\) with amounts | ethanoic acid + ethanoate: pH 4.46 |
| strong acid and strong alkali mixed | amounts, find the excess, divide by the **total** volume | pH 1.60 |
| weak acid with alkali beyond the equivalence point | excess strong alkali decides the pH | 30.0 cm³ of alkali: pH 11.96 |
:::

## Solubility product, Ksp

Salts called "insoluble" do dissolve a very little. When solid silver chloride is shaken with water, a tiny amount dissolves until the solution is **saturated**. Then a dynamic equilibrium exists between the solid and its ions:

\[\ce{AgCl(s) <=> Ag+(aq) + Cl-(aq)}\]

The equilibrium constant, with the solid left out because its concentration is fixed, is the solubility product.

:::def Solubility product, Ksp
The product of the concentrations of the ions of a sparingly soluble salt in its saturated solution at a stated temperature, each raised to the power of its coefficient in the equilibrium equation. For \(\ce{AgCl}\): \(K_{sp} = [\ce{Ag+}][\ce{Cl-}]\).
:::

Write \(K_{sp}\) from the equation for the equilibrium, with the solid on the left:

| Salt | Equilibrium | \(K_{sp}\) | Units of \(K_{sp}\) |
|---|---|---|---|
| silver chloride | \(\ce{AgCl(s) <=> Ag+ + Cl-}\) | \([\ce{Ag+}][\ce{Cl-}]\) | mol² dm⁻⁶ |
| lead(II) iodide | \(\ce{PbI2(s) <=> Pb^2+ + 2I-}\) | \([\ce{Pb^2+}][\ce{I-}]^2\) | mol³ dm⁻⁹ |
| calcium hydroxide | \(\ce{Ca(OH)2(s) <=> Ca^2+ + 2OH-}\) | \([\ce{Ca^2+}][\ce{OH-}]^2\) | mol³ dm⁻⁹ |
| silver chromate(VI) | \(\ce{Ag2CrO4(s) <=> 2Ag+ + CrO4^2-}\) | \([\ce{Ag+}]^2[\ce{CrO4^2-}]\) | mol³ dm⁻⁹ |
| iron(III) hydroxide | \(\ce{Fe(OH)3(s) <=> Fe^3+ + 3OH-}\) | \([\ce{Fe^3+}][\ce{OH-}]^3\) | mol⁴ dm⁻¹² |

A coefficient in the equation becomes a **power** in the expression, not a multiplier. The units come from the expression, exactly as for \(K_c\): replace each concentration by "mol dm⁻³" and cancel.

### Ksp from solubility, and back

The **solubility** of a salt is the concentration of it that dissolves in a saturated solution (mol dm⁻³, or g dm⁻³). Call it \(s\). It links to the ion concentrations through the formula of the salt.

:::cols
:::col Salts like AgCl or BaSO₄ (1 : 1)
\([\ce{Ag+}] = [\ce{Cl-}] = s\), so \(K_{sp} = s^2\) and \(s = \sqrt{K_{sp}}\).
:::
:::col Salts like Ca(OH)₂ or PbI₂ (1 : 2)
\([\ce{Ca^2+}] = s\) and \([\ce{OH-}] = 2s\), so \(K_{sp} = s \times (2s)^2 = 4s^3\) and \(s = \sqrt[3]{K_{sp}/4}\).
:::
:::

:::eg (Exam style) The solubility of silver chloride at 298 K is \(1.34 \times 10^{-5}\) mol dm⁻³. Calculate \(K_{sp}\) and give its units. [3 marks]
\(\ce{AgCl(s) <=> Ag+ + Cl-}\): each mole that dissolves gives 1 mol of each ion, so \([\ce{Ag+}] = [\ce{Cl-}] = 1.34 \times 10^{-5}\) mol dm⁻³. [B1]
\[K_{sp} = [\ce{Ag+}][\ce{Cl-}] = (1.34 \times 10^{-5})^2 = 1.80 \times 10^{-10}\] [M1]
Units: mol dm⁻³ × mol dm⁻³ = mol² dm⁻⁶. [A1]
In mass terms, \(M_r(\ce{AgCl}) = 107.9 + 35.5 = 143.4\), so about \(1.34 \times 10^{-5} \times 143.4 = 1.92 \times 10^{-3}\) g dissolves in each dm³.
:::

:::eg (Real context) Limewater is a saturated solution of calcium hydroxide, used to test for carbon dioxide. A saturated solution contains \([\ce{Ca^2+}] = 1.10 \times 10^{-2}\) mol dm⁻³. Calculate \(K_{sp}\) for \(\ce{Ca(OH)2}\) and give its units. [3 marks]
\(\ce{Ca(OH)2(s) <=> Ca^2+ + 2OH-}\), so \([\ce{OH-}] = 2 \times 1.10 \times 10^{-2} = 2.20 \times 10^{-2}\) mol dm⁻³. [B1]
\[K_{sp} = [\ce{Ca^2+}][\ce{OH-}]^2 = (1.10 \times 10^{-2})(2.20 \times 10^{-2})^2 = 5.32 \times 10^{-6}\] [M1]
Units: mol dm⁻³ × (mol dm⁻³)² = mol³ dm⁻⁹. [A1]
:::

:::eg (Real context) A barium meal, a suspension of barium sulfate, is swallowed so that the digestive tract shows up on an X-ray. Barium ions are poisonous, so the sulfate must be very insoluble. For \(\ce{BaSO4}\), \(K_{sp} = 1.1 \times 10^{-10}\) mol² dm⁻⁶. Calculate the solubility in mol dm⁻³ and in g dm⁻³. [4 marks]
\(\ce{BaSO4(s) <=> Ba^2+ + SO4^2-}\), so \(K_{sp} = s^2\). [B1]
\[s = \sqrt{1.1 \times 10^{-10}} = 1.05 \times 10^{-5}\ \mathrm{mol\,dm^{-3}}\] [M1 A1]
\(M_r(\ce{BaSO4}) = 137.3 + 32.1 + 4(16.0) = 233.4\), so the mass is \(1.049 \times 10^{-5} \times 233.4 = 2.45 \times 10^{-3}\) g dm⁻³. [A1]
Only about 2 mg of barium sulfate dissolves per dm³, which is too little to harm the patient.
:::

:::eg (Exam style) Magnesium hydroxide, the active ingredient of milk of magnesia (an antacid), has \(K_{sp} = 5.6 \times 10^{-12}\) mol³ dm⁻⁹. Calculate the solubility of \(\ce{Mg(OH)2}\) and the pH of its saturated solution at 298 K. [6 marks]
\(\ce{Mg(OH)2(s) <=> Mg^2+ + 2OH-}\): \([\ce{Mg^2+}] = s\), \([\ce{OH-}] = 2s\). [B1]
\[K_{sp} = s(2s)^2 = 4s^3\quad\text{so}\quad s = \sqrt[3]{\frac{5.6 \times 10^{-12}}{4}}\] [M1]
\[s = 1.12 \times 10^{-4}\ \mathrm{mol\,dm^{-3}}\] [A1]
\([\ce{OH-}] = 2s = 2.237 \times 10^{-4}\) mol dm⁻³. [B1]
\[[\ce{H+}] = \frac{K_w}{[\ce{OH-}]} = \frac{1.00 \times 10^{-14}}{2.237 \times 10^{-4}} = 4.47 \times 10^{-11}\ \mathrm{mol\,dm^{-3}}\] [M1]
\[\mathrm{pH} = 10.35\] [A1]
The solution is alkaline enough to neutralise stomach acid but nowhere near as alkaline as sodium hydroxide, because \(\ce{Mg(OH)2}\) is so sparingly soluble.
:::

:::warn Ksp traps
(1) The power comes from the **coefficient**, and the 2 also multiplies the concentration: for \(\ce{Ca(OH)2}\), \(K_{sp} = s(2s)^2 = 4s^3\), not \(s^3\) and not \(s^2\). (2) When you find the ion concentration in a 1 : 2 salt, **double** the \(\ce{OH-}\) (or \(\ce{I-}\)), and then square it. (3) \(K_{sp}\) has units that depend on the salt, so work them out. (4) \(K_{sp}\) is a constant only at one temperature. It describes a *saturated* solution only.
:::

### Will a precipitate form?

\(K_{sp}\) is a property of a *saturated* solution. For any solution, calculate the **ionic product**: the same expression as \(K_{sp}\) but with the concentrations you actually have. Compare it with \(K_{sp}\).

:::key Predicting precipitation
- Ionic product < \(K_{sp}\): the solution is unsaturated; no precipitate forms.
- Ionic product = \(K_{sp}\): exactly saturated.
- Ionic product > \(K_{sp}\): too many ions; a **precipitate forms** until the ionic product falls back to \(K_{sp}\).
:::

When you *mix* two solutions, each solution dilutes the other, so find the concentrations **after mixing** before you compare. This is the commonest slip.

:::eg (Exam style) Equal volumes of 1.0 × 10⁻⁴ mol dm⁻³ silver nitrate and 1.0 × 10⁻⁴ mol dm⁻³ sodium chloride are mixed. Does silver chloride precipitate? What if both solutions are 1.0 × 10⁻⁵ mol dm⁻³? \(K_{sp}(\ce{AgCl}) = 1.8 \times 10^{-10}\) mol² dm⁻⁶. [4 marks]
Equal volumes: after mixing each concentration is halved, so \([\ce{Ag+}] = [\ce{Cl-}] = 5.0 \times 10^{-5}\) mol dm⁻³. [M1]
Ionic product \(= (5.0 \times 10^{-5})^2 = 2.5 \times 10^{-9}\), which is greater than \(1.8 \times 10^{-10}\): a precipitate forms. [M1 A1]
With 1.0 × 10⁻⁵ mol dm⁻³ solutions, the concentrations after mixing are \(5.0 \times 10^{-6}\) mol dm⁻³ and the ionic product is \(2.5 \times 10^{-11}\), which is less than \(K_{sp}\): no precipitate. [A1]
:::

### The common ion effect

A salt is less soluble in a solution that already contains one of its ions. This is Le Chatelier's principle at work. In a saturated solution of silver chloride, \(\ce{AgCl(s) <=> Ag+ + Cl-}\); add sodium chloride and the extra \(\ce{Cl-}\) pushes the equilibrium to the left, so some \(\ce{AgCl}\) precipitates and fewer silver ions remain in solution.

:::def Common ion effect
The solubility of a sparingly soluble ionic compound is decreased by the presence of a second compound that provides an ion in common with it.
:::

The calculation changes in one way. The common ion now has *two* sources, but the one from the salt is tiny next to the one you added, so it is ignored. The solubility is the concentration of the *other* ion.

:::eg (Exam style) Calculate the solubility of silver chloride in 0.100 mol dm⁻³ sodium chloride, and compare it with the solubility in pure water. \(K_{sp} = 1.80 \times 10^{-10}\) mol² dm⁻⁶. [5 marks]
In 0.100 mol dm⁻³ NaCl, \([\ce{Cl-}] = 0.100\) mol dm⁻³ from the sodium chloride. The chloride from the silver chloride that dissolves (about \(10^{-9}\) mol dm⁻³) is negligible. [B1]
\[[\ce{Ag+}] = \frac{K_{sp}}{[\ce{Cl-}]} = \frac{1.80 \times 10^{-10}}{0.100} = 1.80 \times 10^{-9}\ \mathrm{mol\,dm^{-3}}\] [M1 A1]
Each \(\ce{Ag+}\) comes from one dissolved \(\ce{AgCl}\), so the solubility is \(1.80 \times 10^{-9}\) mol dm⁻³. [B1]
In pure water the solubility is \(\sqrt{1.80 \times 10^{-10}} = 1.34 \times 10^{-5}\) mol dm⁻³, about 7450 times larger. [B1]
:::

For a 1 : 2 salt the common-ion concentration is squared. For \(\ce{Mg(OH)2}\) in 0.0100 mol dm⁻³ sodium hydroxide: \([\ce{OH-}] = 0.0100\) mol dm⁻³, so \([\ce{Mg^2+}] = K_{sp}/[\ce{OH-}]^2 = 5.6 \times 10^{-12}/(0.0100)^2 = 5.6 \times 10^{-8}\) mol dm⁻³. This is the solubility, about 2000 times smaller than in pure water (\(1.12 \times 10^{-4}\) mol dm⁻³).

:::tip Using this idea
To remove an ion from solution almost completely, add an excess of the ion that precipitates it. The common ion keeps the concentration of the ion you want to remove very small.
:::

## Partition coefficients

Shake iodine solution in water with hexane in a separating funnel and the two solvents separate into layers (they do not mix). The brown colour moves almost entirely into the hexane. The iodine is not stuck in either layer: it passes between them until a dynamic equilibrium is reached, with a fixed ratio of concentrations.

:::html
<figure class="fig small"><svg viewBox="0 8 340 270" role="img" aria-label="A separating funnel with an upper organic layer and a lower aqueous layer, a stopper at the top and a tap at the bottom"><path class="fa2" d="M119.9,112 116.4,119 113.9,126 112.5,133 112,140 112,147 112,150 228,150 228,147 228,140 227.5,133 226.1,126 223.6,119 220.1,112Z"/><path class="fa" d="M112,150 112.5,157 114,164 116.5,171 119.9,178 124.4,185 129.7,192 135.8,199 142.5,206 149.3,213 155.9,220 161,227 163,232 177,232 179,227 184.1,220 190.7,213 197.5,206 204.2,199 210.3,192 215.6,185 220.1,178 223.5,171 226,164 227.5,157 228,150Z"/><rect class="fa" x="163" y="232" width="14" height="12"/><path class="ln" d="M157 30V62C157 80 112 100 112 140V150C112 190 160 215 163 232V262"/><path class="ln" d="M183 30V62C183 80 228 100 228 140V150C228 190 180 215 177 232V262"/><path class="ln" d="M151 24H189V30H151Z"/><path class="ln thick" d="M150 244H190"/><path class="ln" d="M190 244H204"/><text class="tl" x="196" y="20">stopper</text><text class="tl" x="212" y="248">tap</text><text class="tl" x="98" y="134" text-anchor="end">organic layer</text><path class="ln-m thin" d="M102 130H138"/><text class="tl" x="244" y="200">aqueous layer</text><path class="ln-m thin" d="M240 196H196"/></svg><figcaption>A separating funnel. The less dense layer floats on top (here an organic solvent such as hexane over water). Shake, let the layers settle, then run the lower layer out through the tap.</figcaption></figure>
:::

:::def Partition coefficient, Kpc
For a solute X that dissolves in two immiscible solvents, \(K_{pc} = \dfrac{[\ce{X}]_{\text{solvent 1}}}{[\ce{X}]_{\text{solvent 2}}}\) at equilibrium, at a stated temperature. The solvent that is on top of the fraction must be stated.
:::

A few conditions apply. \(K_{pc}\) is constant at constant temperature. The solute must be in the **same state** in both solvents: it must not dissociate or associate in one of them, or the ratio changes with concentration. And there is no unit if the concentrations are in the same units (a ratio). If asked, state which solvent is on top of the fraction: \(K_{pc}\) for water-over-hexane is the reciprocal of hexane-over-water.

### Why a solute prefers one solvent

The answer is the rule from [Chemical bonding](#chem.bonding): like dissolves like. A **non-polar** solute such as iodine, \(\ce{I2}\), can form only instantaneous dipole–induced dipole forces. These are easily matched by non-polar hexane, but water is held together by strong hydrogen bonds that the iodine cannot replace, so iodine is far more soluble in hexane. **Polar or ionic** solutes (and those that form hydrogen bonds) have strong attractions to water and are more soluble in the polar solvent. A solute that can hydrogen-bond only weakly with water prefers the organic layer more strongly as its non-polar part gets bigger.

:::eg (Exam style) A solution of iodine in water was shaken with hexane. At equilibrium the concentration of iodine in hexane was 0.0850 mol dm⁻³ and in water 1.00 × 10⁻³ mol dm⁻³. Calculate \(K_{pc}\) for iodine between hexane and water, and explain why it is large. [3 marks]
\[K_{pc} = \frac{[\ce{I2}]_{\text{hexane}}}{[\ce{I2}]_{\text{water}}} = \frac{0.0850}{1.00 \times 10^{-3}} = 85.0\] [M1 A1]
Iodine is a non-polar molecule, so it is held in hexane by id–id forces that are matched by hexane's own, while in water it cannot form hydrogen bonds or compete with the hydrogen bonding between water molecules. [B1]
:::

### Extracting a solute: one big portion or several small ones?

Chemists use partition to take a product out of an aqueous mixture into an organic solvent (a **solvent extraction**). Because the ratio is fixed, how much you extract depends on how you use the solvent.

:::eg (Exam style) 100 cm³ of an aqueous solution contains 1.00 g of an organic compound X. The partition coefficient is \(K_{pc} = [\ce{X}]_{\text{ether}}/[\ce{X}]_{\text{water}} = 4.00\). Calculate the mass of X extracted (a) by shaking once with 100 cm³ of ether and (b) by shaking twice, each time with 50.0 cm³ of fresh ether. [6 marks]
(a) Let \(m\) g move into the ether. Then 1.00 − \(m\) g stays in 100 cm³ of water. [B1]
\[4.00 = \frac{m/100}{(1.00 - m)/100}\quad\Rightarrow\quad m = 4.00(1.00 - m) = 4.00 - 4.00m\quad\Rightarrow\quad m = 0.800\ \mathrm{g}\] [M1 A1]
(b) First extraction with 50.0 cm³: \(4.00 = \dfrac{m_1/50.0}{(1.00 - m_1)/100}\), so \(m_1/(1.00 - m_1) = 2.00\) and \(m_1 = 0.667\) g. 0.333 g remains in the water. [M1]
Second extraction, with the 0.333 g: \(m_2/(0.333 - m_2) = 2.00\), so \(m_2 = 0.222\) g. [M1]
Total extracted \(= 0.667 + 0.222 = 0.889\) g, more than 0.800 g with the same total volume of ether. [A1]
:::

There is a short cut. A fraction \(\dfrac{V_w}{V_w + K_{pc}V_o}\) of the solute remains in the aqueous layer after each extraction (\(V_w\) the volume of water and \(V_o\) the volume of organic solvent). For (a) that is \(100/(100 + 4.00 \times 100) = 0.200\); for (b) it is \(100/(100 + 4.00 \times 50.0) = 0.333\) after one extraction, and \(0.333^2 = 0.111\) after two. So several small portions of solvent always extract more than one large portion of the same total volume.

:::key Extraction
A fixed volume of solvent removes more solute if it is used in several small portions than in one large portion. For a solute that prefers the organic solvent, shake with a fresh portion each time and combine the organic layers.
:::

:::lab Using a separating funnel
Pour the mixture into the funnel with the tap closed and put in the stopper. Invert the funnel, open the tap to release the pressure (point the stem away from everyone), close it, shake, then let the layers settle and run the lower layer into a flask. Check which layer is which by adding a drop of water: it joins the aqueous layer. Dry the organic layer with a drying agent such as anhydrous magnesium sulfate and distil off the solvent. (See [Organic synthesis (AS)](#chem.org.synthesis).)
:::

:::try Start easy, finish at exam standard
Q: Write the formula of (a) the conjugate base of \(\ce{HNO3}\) and of \(\ce{NH4+}\), (b) the conjugate acid of \(\ce{OH-}\) and of \(\ce{CH3COO-}\).
A: (a) \(\ce{NO3-}\) and \(\ce{NH3}\). (b) \(\ce{H2O}\) and \(\ce{CH3COOH}\). Each differs from the original by one \(\ce{H+}\).
Q: Calculate the pH of (a) 0.0250 mol dm⁻³ nitric acid and (b) 0.00400 mol dm⁻³ potassium hydroxide at 298 K.
A: (a) Strong monoprotic: \([\ce{H+}] = 0.0250\), pH = 1.60. (b) \([\ce{OH-}] = 0.00400\), \([\ce{H+}] = 1.00 \times 10^{-14}/0.00400 = 2.50 \times 10^{-12}\), pH = 11.60.
Q: A solution has pH 3.40. Calculate \([\ce{H+}]\).
A: \([\ce{H+}] = 10^{-3.40} = 3.98 \times 10^{-4}\) mol dm⁻³.
Q: Calculate the pH of 0.250 mol dm⁻³ propanoic acid, \(K_a = 1.35 \times 10^{-5}\) mol dm⁻³.
A: \([\ce{H+}] = \sqrt{1.35 \times 10^{-5} \times 0.250} = 1.837 \times 10^{-3}\) mol dm⁻³; pH = 2.74.
Q: A weak acid has \(\mathrm{p}K_a = 3.75\). Calculate \(K_a\), and say which is the stronger acid, this one or ethanoic acid (\(\mathrm{p}K_a = 4.76\)).
A: \(K_a = 10^{-3.75} = 1.78 \times 10^{-4}\) mol dm⁻³. It has the smaller \(\mathrm{p}K_a\), so it is the stronger acid (about ten times, since the \(\mathrm{p}K_a\) values differ by one unit).
Q: A 0.0800 mol dm⁻³ solution of a weak acid has pH 3.10. Calculate \(K_a\).
A: \([\ce{H+}] = 10^{-3.10} = 7.943 \times 10^{-4}\); \(K_a = (7.943 \times 10^{-4})^2/0.0800 = 7.89 \times 10^{-6}\) mol dm⁻³.
Q: A buffer contains 0.200 mol of propanoic acid and 0.150 mol of sodium propanoate in 1.00 dm³. Find its pH. \(K_a = 1.35 \times 10^{-5}\) mol dm⁻³.
A: \([\ce{H+}] = 1.35 \times 10^{-5} \times 0.200/0.150 = 1.80 \times 10^{-5}\) mol dm⁻³; pH = 4.74.
Q: Write the \(K_{sp}\) expression and units for (a) \(\ce{Fe(OH)3}\) and (b) \(\ce{Ag2CO3}\).
A: (a) \(K_{sp} = [\ce{Fe^3+}][\ce{OH-}]^3\), mol⁴ dm⁻¹². (b) \(K_{sp} = [\ce{Ag+}]^2[\ce{CO3^2-}]\), mol³ dm⁻⁹.
Q: The solubility of calcium fluoride, \(\ce{CaF2}\), is \(2.14 \times 10^{-4}\) mol dm⁻³. Calculate \(K_{sp}\).
A: \([\ce{Ca^2+}] = s\), \([\ce{F-}] = 2s\). \(K_{sp} = 4s^3 = 4(2.14 \times 10^{-4})^3 = 3.92 \times 10^{-11}\) mol³ dm⁻⁹.
Q: 20.0 cm³ of 2.0 × 10⁻⁴ mol dm⁻³ silver nitrate is added to 30.0 cm³ of 1.0 × 10⁻³ mol dm⁻³ sodium chloride. Does silver chloride precipitate? \(K_{sp} = 1.8 \times 10^{-10}\) mol² dm⁻⁶.
A: Total volume 50.0 cm³. \([\ce{Ag+}] = 2.0 \times 10^{-4} \times 20.0/50.0 = 8.0 \times 10^{-5}\); \([\ce{Cl-}] = 1.0 \times 10^{-3} \times 30.0/50.0 = 6.0 \times 10^{-4}\). Ionic product \(= 4.8 \times 10^{-8}\), which is greater than \(K_{sp}\), so a precipitate forms.
Q: The partition coefficient of a compound between ether and water, \(K_{pc} = [\ce{X}]_{\text{ether}}/[\ce{X}]_{\text{water}}\), is 7.5. At equilibrium the aqueous layer holds 0.020 mol dm⁻³. Find the concentration in the ether.
A: \([\ce{X}]_{\text{ether}} = 7.5 \times 0.020 = 0.15\) mol dm⁻³.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Calculate the pH of 0.0250 mol dm⁻³ barium hydroxide, \(\ce{Ba(OH)2}\), at 298 K.
A: \([\ce{OH-}] = 2 \times 0.0250 = 0.0500\) mol dm⁻³, so \([\ce{H+}] = 1.00 \times 10^{-14}/0.0500 = 2.00 \times 10^{-13}\) mol dm⁻³. [M1]
pH = 12.70 [A1]
Q: [3 marks] ★ Calculate the pH of 0.0500 mol dm⁻³ methanoic acid, \(\ce{HCOOH}\), \(K_a = 1.78 \times 10^{-4}\) mol dm⁻³.
A: \([\ce{H+}] = \sqrt{K_a c}\) [M1] \(= \sqrt{1.78 \times 10^{-4} \times 0.0500} = 2.983 \times 10^{-3}\) mol dm⁻³ [M1]
pH = 2.53 [A1]
Q: [4 marks] ★★ A 0.150 mol dm⁻³ solution of a weak acid HX has a pH of 2.85. Calculate \(K_a\) and \(\mathrm{p}K_a\) of HX.
H: Find \([\ce{H+}]\) from the pH; assume \([\ce{X-}] = [\ce{H+}]\).
A: \([\ce{H+}] = 10^{-2.85} = 1.413 \times 10^{-3}\) mol dm⁻³ [M1]
\(K_a = [\ce{H+}]^2/[\ce{HX}] = (1.413 \times 10^{-3})^2/0.150\) [M1]
\(= 1.33 \times 10^{-5}\) mol dm⁻³ [A1]
\(\mathrm{p}K_a = 4.88\) [A1]
Q: [4 marks] ★★ A buffer of pH 4.30 is to be made by dissolving sodium ethanoate (\(M_r = 82.0\)) in 250 cm³ of 0.400 mol dm⁻³ ethanoic acid. Calculate the mass of sodium ethanoate needed. \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³.
H: Find \([\ce{H+}]\), then the ratio \([\ce{A-}]/[\ce{HA}] = K_a/[\ce{H+}]\).
A: \([\ce{H+}] = 10^{-4.30} = 5.012 \times 10^{-5}\) mol dm⁻³ [M1]
\([\ce{A-}]/[\ce{HA}] = 1.74 \times 10^{-5}/5.012 \times 10^{-5} = 0.3472\) [M1]
\(n(\ce{HA}) = 0.400 \times 250/1000 = 0.100\) mol, so \(n(\ce{A-}) = 0.03472\) mol [M1]
Mass \(= 0.03472 \times 82.0 = 2.85\) g [A1]
Q: [5 marks] ★★ A buffer contains ethanoic acid and sodium ethanoate. Explain how it resists a change in pH when (a) a small amount of hydrochloric acid is added and (b) a small amount of sodium hydroxide is added. Include equations.
A: The buffer contains a large amount of \(\ce{CH3COOH}\) (weak acid) and of \(\ce{CH3COO-}\) (its conjugate base, from the salt). [B1]
(a) \(\ce{CH3COO- + H+ -> CH3COOH}\): the base removes the added \(\ce{H+}\). [B1]
(b) \(\ce{CH3COOH + OH- -> CH3COO- + H2O}\): the acid removes the added \(\ce{OH-}\). [B1]
Only small amounts of \(\ce{CH3COOH}\) and \(\ce{CH3COO-}\) are used up, so the ratio \([\ce{CH3COOH}]/[\ce{CH3COO-}]\) hardly changes [B1] and so \([\ce{H+}] = K_a \times [\ce{HA}]/[\ce{A-}]\) and the pH hardly change. [B1]
Q: [5 marks] ★★ The solubility of lead(II) iodide, \(\ce{PbI2}\), is \(1.35 \times 10^{-3}\) mol dm⁻³ at 298 K. (a) Write the \(K_{sp}\) expression and calculate \(K_{sp}\), with units. (b) Calculate the solubility of \(\ce{PbI2}\) in 0.0100 mol dm⁻³ lead(II) nitrate.
H: In (b) the common ion is \(\ce{Pb^2+}\): its concentration is 0.0100 mol dm⁻³, so find \([\ce{I-}]\) and halve it.
A: (a) \(K_{sp} = [\ce{Pb^2+}][\ce{I-}]^2\) [B1]; \([\ce{I-}] = 2.70 \times 10^{-3}\), \(K_{sp} = (1.35 \times 10^{-3})(2.70 \times 10^{-3})^2 = 9.84 \times 10^{-9}\) mol³ dm⁻⁹ [M1 A1]
(b) \([\ce{I-}]^2 = K_{sp}/[\ce{Pb^2+}] = 9.84 \times 10^{-9}/0.0100\), so \([\ce{I-}] = 9.92 \times 10^{-4}\) mol dm⁻³ [M1]
Solubility \(= [\ce{I-}]/2 = 4.96 \times 10^{-4}\) mol dm⁻³ [A1]
Q: [5 marks] ★★★ A solution contains 0.0200 mol dm⁻³ magnesium ions. Dilute sodium hydroxide is added slowly. Calculate the pH at which magnesium hydroxide first starts to precipitate. \(K_{sp}(\ce{Mg(OH)2}) = 5.6 \times 10^{-12}\) mol³ dm⁻⁹; \(K_w = 1.00 \times 10^{-14}\) mol² dm⁻⁶.
H: A precipitate starts when the ionic product just equals \(K_{sp}\).
H: Find \([\ce{OH-}]\) first, then \([\ce{H+}]\) using \(K_w\).
A: Precipitation begins when \([\ce{Mg^2+}][\ce{OH-}]^2 = K_{sp}\). [M1]
\([\ce{OH-}]^2 = 5.6 \times 10^{-12}/0.0200 = 2.8 \times 10^{-10}\) [M1]
\([\ce{OH-}] = 1.67 \times 10^{-5}\) mol dm⁻³ [A1]
\([\ce{H+}] = 1.00 \times 10^{-14}/1.673 \times 10^{-5} = 5.98 \times 10^{-10}\) mol dm⁻³ [M1]
pH = 9.22 [A1]
Q: [7 marks] ★★ The partition coefficient of compound X is \(K_{pc} = [\ce{X}]_{\text{organic}}/[\ce{X}]_{\text{water}} = 6.00\). 100 cm³ of an aqueous solution holds 0.600 g of X. (a) Calculate the mass extracted by one shaking with 50.0 cm³ of the organic solvent. (b) Calculate the total mass extracted by two shakings with 25.0 cm³ of fresh solvent each time, and say which method is better.
H: Let the mass extracted be \(m\) and write the concentration in each layer as mass divided by volume.
A: (a) \(6.00 = \dfrac{m/50.0}{(0.600 - m)/100}\) [M1] so \(2m = 6.00(0.600 - m)\) and \(m = 0.450\) g [M1 A1]
(b) After each shaking, the fraction left in water is \(100/(100 + 6.00 \times 25.0) = 0.400\). [M1]
After two shakings, \(0.600 \times 0.400^2 = 0.0960\) g remains [M1], so \(0.600 - 0.0960 = 0.504\) g has been extracted. [A1]
The two smaller portions extract more (0.504 g against 0.450 g). [B1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ 25.0 cm³ of 0.200 mol dm⁻³ ethanoic acid is titrated with 0.100 mol dm⁻³ sodium hydroxide. \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³. Calculate (a) the volume needed to reach the equivalence point, (b) the pH at the start, (c) the pH after 25.0 cm³ of alkali, (d) the pH after 40.0 cm³ and (e) the pH after 60.0 cm³.
H: Which kind of solution is in the flask at each volume: weak acid, buffer, or excess strong alkali?
H: At 25.0 cm³ how much of the acid has been neutralised?
H: For (e), the volume of the mixture is 85.0 cm³.
A: (a) \(n(\ce{HA}) = 0.200 \times 25.0/1000 = 5.00 \times 10^{-3}\) mol; volume \(= 5.00 \times 10^{-3}/0.100 = 0.0500\) dm³ = 50.0 cm³. [B1]
(b) \([\ce{H+}] = \sqrt{1.74 \times 10^{-5} \times 0.200} = 1.865 \times 10^{-3}\); pH = 2.73. [M1 A1]
(c) 25.0 cm³ is half of 50.0 cm³: half-equivalence, \(\mathrm{pH} = \mathrm{p}K_a = 4.76\). [A1]
(d) \(n(\ce{OH-}) = 4.00 \times 10^{-3}\) mol, so \(n(\ce{A-}) = 4.00 \times 10^{-3}\) and \(n(\ce{HA}) = 1.00 \times 10^{-3}\) mol. \([\ce{H+}] = 1.74 \times 10^{-5} \times 1.00/4.00 = 4.35 \times 10^{-6}\); pH = 5.36. [M1 A1]
(e) \(n(\ce{OH-})\) added \(= 6.00 \times 10^{-3}\) mol; excess \(= 1.00 \times 10^{-3}\) mol in 85.0 cm³: \([\ce{OH-}] = 0.01176\), \([\ce{H+}] = 8.50 \times 10^{-13}\), pH = 12.07. [M1 A1]
Q: [5 marks] ★★★ A solution contains 0.0100 mol dm⁻³ chloride ions and 0.0100 mol dm⁻³ iodide ions. Solid silver nitrate is added slowly (ignore any change in volume). \(K_{sp}(\ce{AgCl}) = 1.8 \times 10^{-10}\) and \(K_{sp}(\ce{AgI}) = 8.5 \times 10^{-17}\) mol² dm⁻⁶. (a) Which silver halide precipitates first? (b) Calculate \([\ce{Ag+}]\) when the second begins to precipitate, and the concentration of the first halide ion still in solution at that point. Comment.
H: A precipitate starts when \([\ce{Ag+}]\) reaches \(K_{sp}/[\text{halide}]\).
A: (a) \(\ce{AgI}\) needs \([\ce{Ag+}] = 8.5 \times 10^{-17}/0.0100 = 8.5 \times 10^{-15}\) mol dm⁻³; \(\ce{AgCl}\) needs \(1.8 \times 10^{-8}\) mol dm⁻³. AgI needs far less silver, so it precipitates first. [B1 M1]
(b) AgCl begins at \([\ce{Ag+}] = 1.8 \times 10^{-10}/0.0100 = 1.8 \times 10^{-8}\) mol dm⁻³. [A1]
Then \([\ce{I-}] = 8.5 \times 10^{-17}/1.8 \times 10^{-8} = 4.7 \times 10^{-9}\) mol dm⁻³. [M1]
This is only \(4.7 \times 10^{-7}\) of the original iodide (0.000047 %), so the two halides can be separated almost completely. [B1]
:::

:::quiz
? In the equilibrium \(\ce{NH3 + H2O <=> NH4+ + OH-}\), which species is the conjugate acid of \(\ce{NH3}\)?
- \(\ce{H2O}\)
- \(\ce{OH-}\)
+ \(\ce{NH4+}\)
- \(\ce{NH2-}\)
> The conjugate acid is the base plus one proton: \(\ce{NH3 + H+ -> NH4+}\). \(\ce{H2O}\) is the acid on the left, and \(\ce{OH-}\) is its conjugate base.
? What is the pH of 0.0100 mol dm⁻³ sodium hydroxide at 298 K?
- 2.00
+ 12.00
- 11.00
- 13.00
> \([\ce{OH-}] = 0.0100\), so \([\ce{H+}] = 1.00 \times 10^{-14}/0.0100 = 1.00 \times 10^{-12}\) and pH = 12.00. A pH of 2.00 comes from forgetting \(K_w\) and using \(-\lg[\ce{OH-}]\).
? What is the pH of 0.0100 mol dm⁻³ ethanoic acid, \(K_a = 1.74 \times 10^{-5}\) mol dm⁻³?
- 2.00
- 4.76
- 2.38
+ 3.38
> \([\ce{H+}] = \sqrt{1.74 \times 10^{-5} \times 0.0100} = 4.17 \times 10^{-4}\) mol dm⁻³, so pH = 3.38. A pH of 2.00 treats the weak acid as strong, and 4.76 is the \(\mathrm{p}K_a\).
? Which of these mixtures is a buffer solution?
- 50 cm³ of 0.10 mol dm⁻³ ethanoic acid + 50 cm³ of 0.10 mol dm⁻³ sodium hydroxide
+ 50 cm³ of 0.10 mol dm⁻³ ethanoic acid + 25 cm³ of 0.10 mol dm⁻³ sodium hydroxide
- 50 cm³ of 0.10 mol dm⁻³ hydrochloric acid + 25 cm³ of 0.10 mol dm⁻³ sodium hydroxide
- 50 cm³ of 0.10 mol dm⁻³ hydrochloric acid + 50 cm³ of 0.10 mol dm⁻³ sodium chloride
> The second mixture leaves half of the weak acid unreacted and makes an equal amount of ethanoate: a weak acid and its conjugate base. The first leaves only sodium ethanoate (no acid), and the others involve a strong acid with no conjugate base of a weak acid.
? What does a buffer solution do?
+ It minimises the change in pH when small amounts of acid or alkali are added.
- It keeps the pH exactly constant when any amount of acid or alkali is added.
- It neutralises any acid or alkali that is added, giving pH 7.
- It prevents the dissociation of the weak acid.
> A buffer resists a change in pH but does not stop it, and only for small additions. It works because a weak acid and its conjugate base are both present, not because the pH is moved to 7.
? What is the \(K_{sp}\) expression for silver chromate(VI), \(\ce{Ag2CrO4}\)?
- \([\ce{Ag+}][\ce{CrO4^2-}]\)
+ \([\ce{Ag+}]^2[\ce{CrO4^2-}]\)
- \(2[\ce{Ag+}][\ce{CrO4^2-}]\)
- \(\dfrac{[\ce{Ag+}]^2[\ce{CrO4^2-}]}{[\ce{Ag2CrO4}]}\)
> The coefficient 2 of \(\ce{Ag+}\) in the equation becomes a power, and the solid is left out of the expression.
? Solid sodium chloride is added to a saturated solution of silver chloride. What happens?
- More silver chloride dissolves.
- \(K_{sp}\) decreases.
+ Some silver chloride precipitates and \(K_{sp}\) is unchanged.
- Nothing, because sodium chloride and silver chloride are different salts.
> The extra \(\ce{Cl-}\) shifts \(\ce{AgCl(s) <=> Ag+ + Cl-}\) to the left (the common ion effect). \(K_{sp}\) depends only on temperature.
? The solubility of magnesium hydroxide is \(1.0 \times 10^{-4}\) mol dm⁻³. What is its \(K_{sp}\)?
- \(1.0 \times 10^{-12}\)
- \(1.0 \times 10^{-8}\)
+ \(4.0 \times 10^{-12}\)
- \(2.0 \times 10^{-12}\)
> \([\ce{Mg^2+}] = 1.0 \times 10^{-4}\) and \([\ce{OH-}] = 2.0 \times 10^{-4}\), so \(K_{sp} = (1.0 \times 10^{-4})(2.0 \times 10^{-4})^2 = 4.0 \times 10^{-12}\). Using \(s^3\) gives \(1.0 \times 10^{-12}\).
? Iodine is much more soluble in hexane than in water. Which explanation is correct?
- Iodine is ionic and hexane is polar.
+ Iodine and hexane are both non-polar, so they form id–id forces, while water has strong hydrogen bonds that iodine cannot match.
- Hexane is denser than water.
- Iodine reacts with hexane.
> Like dissolves like. Iodine is non-polar and mixes with a non-polar solvent without having to break hydrogen bonds between water molecules.
:::

:::checklist What you can now do
- [ ] I can identify the conjugate acid and conjugate base in an equation and label conjugate acid–base pairs.
- [ ] I can define pH, \(K_a\), \(\mathrm{p}K_a\) and \(K_w\), and use them, giving pH to 2 decimal places.
- [ ] I can calculate the pH of strong acids, strong alkalis (using \(K_w\)) and mixtures of them.
- [ ] I can calculate \([\ce{H+}]\) and the pH of a weak acid with \([\ce{H+}] = \sqrt{K_a c}\), state the assumptions, and find \(K_a\) from a pH.
- [ ] I can define a buffer, say how one is made, and explain with equations how it controls pH, including \(\ce{HCO3-}\) in blood.
- [ ] I can calculate the pH of a buffer from \([\ce{H+}] = K_a[\ce{HA}]/[\ce{A-}]\), including one made by adding alkali to excess weak acid.
- [ ] I can use the half-equivalence point of a weak acid titration to find \(\mathrm{p}K_a\).
- [ ] I can write \(K_{sp}\) expressions and calculate \(K_{sp}\) from solubility and solubility from \(K_{sp}\), with units.
- [ ] I can predict precipitation by comparing the ionic product with \(K_{sp}\) and do common ion calculations.
- [ ] I can define \(K_{pc}\), calculate with it (including one or two extractions) and explain it using polarity.
:::

:::recap
- A conjugate pair differs by one \(\ce{H+}\). Strong acid: very weak conjugate base. Every acid–base reaction has two pairs.
- \(\mathrm{pH} = -\lg[\ce{H+}]\); \(K_w = [\ce{H+}][\ce{OH-}] = 1.00 \times 10^{-14}\) mol² dm⁻⁶ at 298 K. Strong acid: \([\ce{H+}] = c\). Strong alkali: \([\ce{H+}] = K_w/[\ce{OH-}]\).
- \(K_a = [\ce{H+}][\ce{A-}]/[\ce{HA}]\), \(\mathrm{p}K_a = -\lg K_a\). Weak acid: \([\ce{H+}] = \sqrt{K_a c}\) (assumes \([\ce{H+}] = [\ce{A-}]\), \([\ce{HA}] \approx c\)). Diluting 10 times raises a weak acid's pH by 0.50.
- Buffer: minimises changes in pH on adding small amounts of acid or alkali. Weak acid + its salt, or weak acid + less strong alkali. \(\ce{A- + H+ -> HA}\); \(\ce{HA + OH- -> A- + H2O}\). \([\ce{H+}] = K_a[\ce{HA}]/[\ce{A-}]\); pH = pKa when equal amounts.
- Blood: \(\ce{H+ + HCO3- <=> H2CO3 <=> H2O + CO2}\).
- Half-equivalence of a weak acid titration: pH = pKa.
- \(K_{sp}\) = product of the ion concentrations in a saturated solution, each to the power of its coefficient. 1:1: \(K_{sp} = s^2\); 1:2: \(K_{sp} = 4s^3\). Ionic product > \(K_{sp}\): precipitate. Mixing dilutes both solutions.
- Common ion effect: a salt is less soluble in a solution containing one of its ions; \(K_{sp}\) is unchanged.
- \(K_{pc} = [\text{X}]_{\text{solvent 1}}/[\text{X}]_{\text{solvent 2}}\); state which solvent is on top; same state in both. Like dissolves like. Several small extractions beat one large one.
:::

:::links
- read: [Buffer solutions](https://www.chemguide.co.uk/physical/acidbaseeqia/buffers.html) · Chemguide · how a buffer works, with the calculations, from the acid-base equilibria menu
- read: [Strong and weak acids](https://www.chemguide.co.uk/physical/acidbaseeqia/acids.html) · Chemguide · pH, Ka and the weak-acid calculation
- read: [The ionic product for water: Kw](https://www.chemguide.co.uk/physical/acidbaseeqia/kw.html) · Chemguide · pH of strong alkalis step by step
- read: [Solubility products menu](https://www.chemguide.co.uk/physical/kspmenu.html) · Chemguide · introduction, calculations and the common ion effect
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Rate equations and catalysis](#chem.rates2) turns to the speed of reactions, and writes the rate as an equation.
