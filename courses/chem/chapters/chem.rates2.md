@chapter chem.rates2
@title Rate equations and catalysis
@level a2
@paper CAIE 9701 Paper 4
@time 8–10 hours
@summary How to write the speed of a reaction as an equation. You will learn orders of reaction and the rate constant, how to find the order from initial rates, half-lives and graphs, how to calculate k and its units, how a rate equation reveals the rate-determining step and the mechanism, why temperature changes k, and how heterogeneous and homogeneous catalysts work.

:::why
A medicine company must know how long a drug stays in the body, a chemical plant must know how a change in concentration changes the output, and an engineer designing a car's exhaust system needs a catalyst that works in about a second. All three depend on a rate equation, a short expression that says how fast a reaction goes and what it depends on. A rate equation is also the best clue to *how* a reaction happens, step by step. In [Reaction kinetics](#chem.kinetics) you learnt why reactions speed up; here you measure by how much.
:::

**Before you start**, you should know collision theory, rate measured from a tangent and the effect of catalysts from [Reaction kinetics](#chem.kinetics), and the SN1 and SN2 mechanisms from [Halogenoalkanes](#chem.org.halogen).

:::try Warm-up
Q: A graph of concentration of a reactant against time is a curve. How do you find the rate at one moment? (from [Reaction kinetics](#chem.kinetics))
A: Draw a tangent to the curve at that time. The rate is the size of its gradient (concentration change divided by time change).
Q: Why does the rate of most reactions fall as the reaction proceeds? (from [Reaction kinetics](#chem.kinetics))
A: The reactants are used up, so their concentrations fall, there are fewer collisions per second and fewer effective collisions.
Q: Which species take part in the slow step of the SN1 hydrolysis of 2-bromo-2-methylpropane, and which in the SN2 reaction of bromoethane with hydroxide ions? (from [Halogenoalkanes](#chem.org.halogen))
A: SN1: only the halogenoalkane (it breaks into a carbocation and \(\ce{Br-}\)). SN2: the halogenoalkane and the nucleophile together, in a single step.
:::

## The words you need

:::def Rate of reaction
The change in concentration of a reactant or product per unit time. Its unit is mol dm⁻³ s⁻¹.
:::

:::def Rate equation
An equation that links the rate of a reaction to the concentrations of the reactants, found by experiment. For a reaction of A and B, \(\text{rate} = k[\ce{A}]^m[\ce{B}]^n\).
:::

:::def Order of reaction
The power to which the concentration of a reactant is raised in the rate equation. A reaction is first order with respect to A if \(m = 1\). The **overall order** is the sum of the individual orders, \(m + n\).
:::

:::def Rate constant, k
The proportionality constant in the rate equation. It is the rate when all the concentrations are 1 mol dm⁻³ (when every concentration term equals 1). It has a fixed value at a given temperature and its units depend on the overall order.
:::

:::def Half-life, t½
The time taken for the concentration of a reactant to fall to half of its initial value.
:::

:::def Rate-determining step
The slowest step in the mechanism of a multi-step reaction. It sets the overall rate.
:::

:::def Intermediate
A species formed in one step of a multi-step reaction and used up in a later step. It does not appear in the overall equation.
:::

## The rate equation and orders

Suppose you measure the rate of a reaction between A and B with different starting concentrations. You find that the rate depends on the concentrations of the reactants in a simple way. For example, doubling the concentration of A doubles the rate, and doubling the concentration of B makes no difference. You would write

\[\text{rate} = k[\ce{A}]\]

with B left out. "Zero order in B" means the rate is unchanged by \([\ce{B}]\): the term is \([\ce{B}]^0 = 1\). In the 9701 syllabus the orders are 0, 1 or 2.

| Order with respect to X | Effect of doubling [X] on the rate | Effect of tripling [X] |
|---|---|---|
| 0 | no change (× 1) | no change (× 1) |
| 1 | doubles (× 2) | × 3 |
| 2 | × 4 | × 9 |

Overall order is the sum. \(\text{rate} = k[\ce{A}]^2[\ce{B}]\) is second order in A, first order in B and **third order overall**.

:::key The rate equation comes from experiment
The orders **cannot be read from the balanced equation**. The reaction \(\ce{2NO(g) + 2H2(g) -> N2(g) + 2H2O(g)}\) has a rate equation \(\text{rate} = k[\ce{NO}]^2[\ce{H2}]\): second order in NO but first order in \(\ce{H2}\), even though the equation shows two of each. Only experiments (or a known mechanism) give the order. The coefficients in the equation tell you how much of each substance reacts, not how the rate depends on it.
:::

The halogenoalkane chapter already gave two examples. For bromoethane with hydroxide ions (SN2), \(\text{rate} = k[\ce{CH3CH2Br}][\ce{OH-}]\); for 2-bromo-2-methylpropane (SN1), \(\text{rate} = k[\ce{(CH3)3CBr}]\), zero order in hydroxide ions, which is why the nucleophile can change without affecting the rate.

### The rate constant and its units

\(k\) is constant for a given reaction at a given temperature. A large \(k\) means a fast reaction. To find its units, rearrange the rate equation to make \(k\) the subject and put in units. The rate has units mol dm⁻³ s⁻¹ and each concentration mol dm⁻³.

| Overall order | Rate equation | \(k = \dfrac{\text{rate}}{\text{concentrations}}\) | Units of \(k\) |
|---|---|---|---|
| 0 | rate = k | mol dm⁻³ s⁻¹ | mol dm⁻³ s⁻¹ |
| 1 | rate = k[A] | (mol dm⁻³ s⁻¹) / (mol dm⁻³) | s⁻¹ |
| 2 | rate = k[A][B] or k[A]² | (mol dm⁻³ s⁻¹) / (mol dm⁻³)² | mol⁻¹ dm³ s⁻¹ |
| 3 | rate = k[A]²[B] | (mol dm⁻³ s⁻¹) / (mol dm⁻³)³ | mol⁻² dm⁶ s⁻¹ |

Do not memorise the table: derive the units each time, because the order may not be what you expect.

:::eg Write the rate equation and the units of \(k\) when the rate is first order in P, second order in Q and zero order in R.
\(\text{rate} = k[\ce{P}][\ce{Q}]^2\) (R does not appear, as its order is zero). [B1]
Overall order \(= 1 + 2 = 3\). [B1]
\[k = \frac{\text{rate}}{[\ce{P}][\ce{Q}]^2}\quad\text{so units} = \frac{\text{mol dm}^{-3}\,\text{s}^{-1}}{(\text{mol dm}^{-3})^3} = \text{mol}^{-2}\,\text{dm}^6\,\text{s}^{-1}\] [B1]
:::

:::eg Rate equation \(\text{rate} = k[\ce{A}]^2[\ce{B}]\). Find the factor by which the rate changes when (a) [A] is tripled and [B] doubled, (b) both are halved by adding an equal volume of water.
(a) The factor is \(3^2 \times 2 = 18\). [B1]
(b) Both concentrations are multiplied by ½: \((\tfrac12)^2 \times \tfrac12 = \tfrac18\). The rate falls to one eighth. [B1]
Adding water changes the concentrations of everything, so the effect combines the orders of all the reactants.
:::

## What the graphs look like

The shape of a graph tells you the order at a glance. There are two kinds: concentration against time, and rate against concentration.

### Concentration–time graphs

These come straight from an experiment. Follow the concentration of the reactant A over time, and read the **half-lives** off the graph. A half-life is the time for the concentration to halve, starting from any point. Each plot below starts at 1.00 mol dm⁻³.

:::plot Zero order: [A] falls in a straight line, because the rate does not depend on [A]. The half-lives get shorter: 25 s to go from 1.00 to 0.50, then 12.5 s from 0.50 to 0.25.
--f "1-0.02*x+0*sqrt(50-x)" --x 0 58 --y 0 1.3 --pt "25,0.5,0.50 at 25 s@ne" --pt "37.5,0.25,0.25 at 37.5 s@ne" --xlabel "time / s" --ylabel "[A] / mol dm⁻³"
:::

:::plot First order: [A] falls in a curve of constant proportion. Every half-life is the same, here 30 s: the concentration is 0.50 at 30 s, 0.25 at 60 s and 0.125 at 90 s.
--f "exp(-0.0231049*x)+0*sqrt(120-x)" --x 0 140 --y 0 1.3 --pt "30,0.5,0.50 at 30 s@ne" --pt "60,0.25,0.25 at 60 s@ne" --pt "90,0.125,0.125 at 90 s@ne" --xlabel "time / s" --ylabel "[A] / mol dm⁻³"
:::

:::plot Second order: the curve falls steeply at first and then very slowly. Each half-life is double the last: 30 s, then 60 s (0.25 at 90 s), then 120 s (0.125 at 210 s).
--f "1/(1+x/30)+0*sqrt(240-x)" --x 0 280 --y 0 1.3 --pt "30,0.5,0.50 at 30 s@ne" --pt "90,0.25,0.25 at 90 s@ne" --pt "210,0.125,0.125 at 210 s@ne" --xlabel "time / s" --ylabel "[A] / mol dm⁻³"
:::

:::key Recognising the order from a concentration–time graph
- **Zero order**: a straight line with constant negative gradient; successive half-lives get *shorter* (each half the last).
- **First order**: an exponential curve; every half-life is the *same*.
- **Second order**: a curve that flattens more slowly; successive half-lives get *longer* (each double the last).
:::

### Rate–concentration graphs

The rate at any moment is the gradient of the tangent to the concentration–time curve. Draw tangents at several concentrations, then plot the gradients (rates) against the concentrations. This graph shows the order directly, because \(\text{rate} = k[\ce{A}]^m\).

:::plot Zero order: the rate is constant, whatever [A]. First order: the rate is directly proportional to [A], a straight line through the origin whose gradient is k.
--f "0.02+0*x" --f "0.0231049*x" --label "zero order" --label "first order" --x 0 1.2 --y 0 0.04 --xlabel "[A] / mol dm⁻³" --ylabel "rate / mol dm⁻³ s⁻¹" --legend tr
:::

:::plot Second order: the rate is proportional to [A]², a curve that gets steeper as [A] rises. The straight line is the first-order graph for comparison.
--f "0.0231049*x" --f "0.0333333*x**2" --label "first order" --label "second order" --x 0 1.2 --y 0 0.06 --xlabel "[A] / mol dm⁻³" --ylabel "rate / mol dm⁻³ s⁻¹" --legend tr
:::

Try the widget. It draws both graphs for the order you choose, with the half-lives marked.

:::html
<div class="widget" data-w="chem-order" data-order="1"></div>
:::

Change [A]₀ with the first-order setting selected: the half-life does not change. Do the same with second order and the half-life shortens as the starting concentration rises.

:::eg (Exam style) The rate of decomposition of a compound was found from tangents to a concentration–time graph: 0.0230 mol dm⁻³ s⁻¹ at [A] = 1.00 mol dm⁻³, 0.0116 at 0.50 mol dm⁻³ and 0.00580 at 0.25 mol dm⁻³. State the order and calculate \(k\). [4 marks]
Halving the concentration halves the rate each time (0.0230, 0.0116, 0.00580), so rate is proportional to [A]. [M1]
The reaction is first order and \(\text{rate} = k[\ce{A}]\). [A1]
\(k\) is the rate divided by the concentration: 0.0230/1.00 = 0.0230, 0.0116/0.50 = 0.0232, 0.00580/0.25 = 0.0232. [M1]
The mean is \(k = 0.0231\ \text{s}^{-1}\). [A1]
:::

## Finding the order: half-life method

For a **first-order** reaction the half-life does not depend on the concentration. Read the concentration at the start, find the time to reach half, then the time to go from that value to a quarter, and so on. If these times are equal, the reaction is first order.

:::formula First-order half-life and rate constant
\[t_{\frac12} = \frac{\ln 2}{k} = \frac{0.693}{k}\qquad\text{so}\qquad k = \frac{0.693}{t_{\frac12}}\]
\(k\) is in s⁻¹ if \(t_{\frac12}\) is in seconds. Convert minutes or hours to seconds first. This applies to first-order reactions only. (ln 2 is just the number 0.693; you do not need the ln button.)
:::

Why is it constant? In a first-order reaction the rate is proportional to [A], so when the concentration has halved the rate has halved too, and exactly the same time is needed to lose the next half. In second order the rate is proportional to [A]², so when [A] has halved the rate is only a quarter, and the next half-life takes longer.

:::eg (Exam style) The concentration of a reactant A changed as follows. Deduce the order with respect to A and calculate \(k\). [4 marks]

| time / s | 0 | 25 | 50 | 75 | 100 |
|---|---|---|---|---|---|
| [A] / mol dm⁻³ | 0.800 | 0.400 | 0.200 | 0.100 | 0.0500 |

The concentration halves every 25 s (0.800 to 0.400 to 0.200 to 0.100 to 0.0500). [M1]
The half-life is constant, so the reaction is **first order** with respect to A. [A1]
\[k = \frac{0.693}{t_{\frac12}} = \frac{0.693}{25} = 2.77 \times 10^{-2}\ \text{s}^{-1}\] [M1 A1]
:::

:::eg A second reaction gave [A] = 1.00, 0.50, 0.25 and 0.125 mol dm⁻³ at 0, 20, 60 and 140 s. What is the order?
The first half-life, 1.00 to 0.50, takes 20 s. The second, 0.50 to 0.25, takes 60 − 20 = 40 s. The third, 0.25 to 0.125, takes 140 − 60 = 80 s. [B1]
The half-lives double each time, so the reaction is **second order** in A. [B1]
:::

:::eg (Real context) A drug is removed from the blood by a first-order process with a half-life of 6.0 hours. The concentration in the blood of one patient is 8.0 mg dm⁻³ just after a dose. (a) How long does it take to fall below 1.0 mg dm⁻³? (b) Calculate the rate constant in s⁻¹. [4 marks]
(a) Each half-life halves the concentration: 8.0 to 4.0 to 2.0 to 1.0 mg dm⁻³ takes three half-lives. [M1]
Time \(= 3 \times 6.0 = 18\) hours. [A1]
(b) \(t_{\frac12} = 6.0 \times 3600 = 21\,600\) s. [M1]
\[k = \frac{0.693}{21\,600} = 3.21 \times 10^{-5}\ \text{s}^{-1}\] [A1]
:::

:::warn Half-lives: three traps
(1) A constant half-life proves first order only if you check at least **two** half-lives, starting at different concentrations. (2) \(k = 0.693/t_{\frac12}\) works for first order only. (3) Convert the half-life to seconds before using it, unless the question asks for k in min⁻¹ or h⁻¹.
:::

## Finding the order: initial rates method

Another way is to measure the **initial rate**, the rate right at the start, for several different starting concentrations. At the start you know every concentration exactly (you made the mixture), and nothing has built up that could slow the reaction down. The initial rate comes from the gradient of the tangent at \(t = 0\) on a concentration–time graph, or from a clock reaction.

The method:

:::steps
1. Run a set of experiments, changing the concentration of **one** reactant at a time and keeping the others the same.
2. For each reactant, compare two experiments in which only that concentration changes. By what factor did the concentration change, and by what factor did the rate change?
3. Match: rate × 1 for a concentration change of × 2 means order 0; × 2 means order 1; × 4 means order 2.
4. Write the rate equation, then put one experiment's numbers in to find \(k\) and its units.
:::

:::eg (Exam style) The initial rate of \(\ce{2NO(g) + 2H2(g) -> N2(g) + 2H2O(g)}\) was measured at one temperature. [6 marks]

| Experiment | [NO] / mol dm⁻³ | [H₂] / mol dm⁻³ | initial rate / mol dm⁻³ s⁻¹ |
|---|---|---|---|
| 1 | 0.0050 | 0.0020 | \(1.0 \times 10^{-5}\) |
| 2 | 0.0100 | 0.0020 | \(4.0 \times 10^{-5}\) |
| 3 | 0.0050 | 0.0040 | \(2.0 \times 10^{-5}\) |

Experiments 1 and 2: [H₂] is the same and [NO] doubles; the rate rises by a factor of 4. So the reaction is second order with respect to NO. [M1 A1]
Experiments 1 and 3: [NO] is the same and [H₂] doubles; the rate doubles. So it is first order with respect to \(\ce{H2}\). [M1 A1]
\[\text{rate} = k[\ce{NO}]^2[\ce{H2}]\] [A1]
Using experiment 1: \(k = \dfrac{1.0 \times 10^{-5}}{(0.0050)^2(0.0020)} = 2.0 \times 10^{2}\ \text{mol}^{-2}\,\text{dm}^6\,\text{s}^{-1}\) [A1]
:::

Check by using experiment 2: \(4.0 \times 10^{-5}/((0.0100)^2 \times 0.0020) = 2.0 \times 10^{2}\), the same, as it must be if the equation is right. Always check \(k\) with a second experiment.

### Clock reactions

In a clock reaction you measure the **time** for a small fixed amount of reaction to happen (a colour appears). The amount is made fixed like this: a small, fixed amount of sodium thiosulfate is added at the start; it removes the first iodine formed, so the starch turns blue only when that fixed amount of iodine has been made. The amount is the same in each run, so the rate is proportional to 1/time.

:::eg (Exam style) In the reaction \(\ce{S2O8^2-(aq) + 2I-(aq) -> 2SO4^2-(aq) + I2(aq)}\), the time for a fixed amount of iodine to form (a blue colour appearing with starch) was measured. [4 marks]

| Experiment | [S₂O₈²⁻] / mol dm⁻³ | [I⁻] / mol dm⁻³ | time / s |
|---|---|---|---|
| 1 | 0.040 | 0.080 | 80 |
| 2 | 0.080 | 0.080 | 40 |
| 3 | 0.040 | 0.160 | 40 |

The rate is proportional to 1/t, so halving the time doubles the rate. [B1]
Experiments 1 and 2: [S₂O₈²⁻] doubles and the rate doubles, so first order in \(\ce{S2O8^2-}\). [B1]
Experiments 1 and 3: [I⁻] doubles and the rate doubles, so first order in \(\ce{I-}\). [B1]
\(\text{rate} = k[\ce{S2O8^2-}][\ce{I-}]\), second order overall. [B1]
:::

:::tip A bigger table
In an exam table, more than one concentration may change at once. Choose the pairs where only one changes first. If none exist, work out what the change in the first reactant's concentration should do to the rate (using the order you have found), and see what is left for the second.

For example, if [A] × 2 and [B] × 3 together make the rate × 18, and A is already known to be first order:
- [A] × 2 accounts for a rate × 2.
- What is left is 18 ÷ 2 = 9, and it must come from [B] × 3.
- 3² = 9, so B is second order.
:::

:::eg (Exam style) The reaction \(\ce{A + B -> C}\) gave these initial rates. Find the rate equation and \(k\). [5 marks]

| Experiment | [A] / mol dm⁻³ | [B] / mol dm⁻³ | rate / mol dm⁻³ s⁻¹ |
|---|---|---|---|
| 1 | 0.10 | 0.10 | \(2.0 \times 10^{-4}\) |
| 2 | 0.20 | 0.10 | \(2.0 \times 10^{-4}\) |
| 3 | 0.10 | 0.30 | \(1.8 \times 10^{-3}\) |

Experiments 1 and 2: [A] doubles, rate unchanged, so zero order in A. [M1 A1]
Experiments 1 and 3: [B] × 3 and the rate × 9, so second order in B. [M1 A1]
\(\text{rate} = k[\ce{B}]^2\), and \(k = \dfrac{2.0 \times 10^{-4}}{(0.10)^2} = 2.0 \times 10^{-2}\ \text{mol}^{-1}\,\text{dm}^3\,\text{s}^{-1}\). [A1]
:::

## Temperature and the rate constant

Raising the temperature makes almost every reaction faster. The rate equation shows how: the concentrations are the same, so it must be \(k\) that changes. **\(k\) increases as temperature increases.**

The reason is the one from [Reaction kinetics](#chem.kinetics). At a higher temperature a larger proportion of the molecules has energy of at least the activation energy, so a larger proportion of collisions is successful, and \(k\) goes up. Try the widget from that chapter again and compare the shaded areas at two temperatures.

:::html
<div class="widget" data-w="chem-boltzmann" data-t1="300" data-t2="310" data-ea="50"></div>
:::

A catalyst also changes \(k\) (it lowers \(E_a\)) but changing a concentration does not.

:::key What changes \(k\)?
\(k\) changes with **temperature** and with a **catalyst**. It does *not* change when the concentrations change. A reaction can go faster because the concentration is higher (the rate equation) or because \(k\) is larger (temperature, catalyst): do not mix the two up.
:::

:::board
AQA also teaches the Arrhenius equation, \(k = Ae^{-E_a/RT}\), and the use of a graph of \(\ln k\) against \(1/T\) to find the activation energy. The Cambridge 9701 syllabus treats the effect of temperature on \(k\) only qualitatively.
:::

## Mechanisms and the rate-determining step

Most reactions happen in more than one step. The balanced equation gives the overall change, but the mechanism says what happens at the level of particles. Each step involves one or two particles colliding.

:::html
<figure class="fig small"><svg viewBox="0 8 330 232" role="img" aria-label="Reaction pathway diagram for a two-step reaction: the first peak, transition state TS1, is higher than the second peak, TS2, with a valley between them that is the intermediate"><path class="ax" d="M20 205V30" marker-end="url(#ahm)"/><path class="ax" d="M20 205H290" marker-end="url(#ahm)"/><text class="tl" x="28" y="24">enthalpy</text><text class="tl" x="290" y="227" text-anchor="end">progress of reaction</text><path class="ln thick" d="M50 140H90"/><path class="ln thick" d="M250 160H282"/><path class="c1 sw2" d="M90 140C108 140 112 60 130 60C148 60 152 110 170 110C188 110 192 85 210 85C228 85 232 160 250 160"/><text class="tl tc" x="70" y="158">reactants</text><text class="tl tc" x="266" y="180">products</text><text class="tl tc" x="170" y="128">intermediate</text><text class="tl tc" x="130" y="50">TS₁ (slow step)</text><text class="tl tc" x="210" y="75">TS₂ (fast step)</text><path class="ln-m thin dash" d="M32 60H126"/><path class="ln-m thin dash" d="M32 140H50"/><path class="c2 sw2" d="M38 100V63" marker-end="url(#ah)"/><path class="c2 sw2" d="M38 100V137" marker-end="url(#ah)"/><text class="tl" x="45" y="104">Eₐ</text></svg><figcaption>Pathway of a two-step reaction. Each step has its own peak, a transition state (TS). The valley between the peaks is an intermediate, a real species that can in principle be detected. The step with the higher activation energy (the first) is the slow, rate-determining step.</figcaption></figure>
:::

:::key Intermediate or transition state?
An **intermediate** sits in a valley of the pathway diagram: it is a real species with a measurable life. A **transition state** sits at a peak: it is the arrangement of atoms at the point of no return, not a species you can isolate. A mechanism with *n* steps has *n* transition states and *n* − 1 intermediates.
:::

### Reading a mechanism from a rate equation

The reasoning is the same in both directions.

:::key The rule for the rate-determining step
The rate equation contains the species that take part in the rate-determining step (and any steps before it). Species that only react **after** the slow step do not appear in the rate equation, however much of them is needed overall. The power of each species in the rate equation is the number of its particles in that step.
:::

Why "and any steps before it"? A slow step can only use particles that have already been made. If an earlier (fast) step makes an intermediate that the slow step then uses, the amount of that intermediate depends on the reactants of the earlier step, so those reactants count too. Example: \(\ce{2NO + O2 -> 2NO2}\) goes in two steps. Step 1 (fast): \(\ce{NO + NO -> N2O2}\). Step 2 (slow): \(\ce{N2O2 + O2 -> 2NO2}\). The slow step uses \(\ce{N2O2}\) and \(\ce{O2}\), and the more NO there is, the more \(\ce{N2O2}\) is made, so the rate depends on both \([\ce{NO}]\) and \([\ce{O2}]\). Here the slow step is the second one, and the NO still appears in the rate equation. (You will not be asked to derive the exact powers for a case like this at AS; just recognise why the earlier reactants appear.)

A mechanism must (1) add up to the overall equation, with intermediates cancelling, and (2) have a slow step that matches the rate equation.

:::eg Deduce the rate equation for each: (a) \(\ce{CH3CH2Br + OH- -> CH3CH2OH + Br-}\) by SN2 (one step), (b) \(\ce{(CH3)3CBr + OH- -> (CH3)3COH + Br-}\) by SN1 (two steps, the first slow).
(a) The rate-determining step is the only step, and it involves one molecule of bromoethane and one hydroxide ion: \(\text{rate} = k[\ce{CH3CH2Br}][\ce{OH-}]\). [B1]
(b) The slow step is \(\ce{(CH3)3CBr -> (CH3)3C+ + Br-}\), which involves only the halogenoalkane: \(\text{rate} = k[\ce{(CH3)3CBr}]\). The hydroxide ion reacts in the fast second step, so it does not appear. [B1]
:::

:::eg (Exam style) The reaction \(\ce{2NO2 + F2 -> 2NO2F}\) has the rate equation \(\text{rate} = k[\ce{NO2}][\ce{F2}]\). Suggest a two-step mechanism, state which step is rate-determining and identify the intermediate. [4 marks]
The rate equation shows one \(\ce{NO2}\) and one \(\ce{F2}\) in the slow step: [M1]
Step 1 (slow): \(\ce{NO2 + F2 -> NO2F + F}\) [A1]
Step 2 (fast): \(\ce{NO2 + F -> NO2F}\) [A1]
Adding: \(\ce{2NO2 + F2 + F -> 2NO2F + F}\) and cancelling the \(\ce{F}\) on both sides gives the overall equation. The intermediate is the fluorine atom, \(\ce{F}\). [A1]
:::

:::eg (Exam style) The reaction \(\ce{2A + B -> C}\) has the rate equation \(\text{rate} = k[\ce{A}]^2\). Which mechanism fits? [3 marks]
Mechanism 1: Step 1 (slow) \(\ce{A + A -> X}\); Step 2 (fast) \(\ce{X + B -> C}\).
Mechanism 2: Step 1 (slow) \(\ce{A + B -> Y}\); Step 2 (fast) \(\ce{Y + A -> C}\).
Both add up to \(\ce{2A + B -> C}\) (the intermediates X or Y cancel). [B1]
Mechanism 1 has two \(\ce{A}\) in the slow step and no B, so rate = \(k[\ce{A}]^2\): this is consistent. [B1]
Mechanism 2 has A and B in the slow step, so rate = \(k[\ce{A}][\ce{B}]\): it does not match. [B1]
B is zero order, because it reacts only after the slow step. In mechanism 1 the intermediate is X.
:::

:::warn "Zero order" does not mean "not involved"
\(\text{rate} = k[\ce{A}]^2\) in the example above does not mean that B takes no part: B is in the overall equation and is a reactant. Zero order means B is **not in the rate-determining step or any step before it**: it reacts in a fast step afterwards, so changing its concentration does not change the rate. The same is true for hydroxide ions in SN1.
:::

:::eg (Real context) Propanone reacts with iodine in aqueous acid: \(\ce{CH3COCH3 + I2 -> CH3COCH2I + HI}\). The rate equation is \(\text{rate} = k[\ce{CH3COCH3}][\ce{H+}]\). (a) State the order with respect to iodine and what it shows. (b) What is the role of \(\ce{H+}\)? [4 marks]
(a) Zero order with respect to \(\ce{I2}\). [B1] Iodine is not in the rate-determining step; it reacts in a fast step after it. [B1]
(b) \(\ce{H+}\) appears in the rate equation but not in the overall equation, so it is used in the slow step and regenerated later: it is a catalyst. [B1] The slow step involves propanone and \(\ce{H+}\) forming the enol, \(\ce{CH3C(OH)=CH2}\) (an enol is a compound with an OH group on a carbon of a C=C double bond; it is an isomer of the carbonyl compound); the iodine reacts with the enol in the fast step. [B1]
:::

:::eg Spot the error: The hydrolysis of 2-bromo-2-methylpropane by aqueous sodium hydroxide has the rate equation \(\text{rate} = k[\ce{(CH3)3CBr}]\). Deduce the order with respect to hydroxide ions and explain what this tells you about the mechanism. [3 marks]
A student wrote this answer.

Line 1: The reaction is zero order with respect to hydroxide ions.
Line 2: Zero order means hydroxide ions do not take part in the reaction.
Line 3: The rate-determining step involves only the halogenoalkane.

Line 1 is correct [B1]. **Line 2 is wrong: hydroxide ions are a reactant and are used up (the product is an alcohol, which contains the OH group). Zero order means only that they are not in the rate-determining step or before it, so the rate does not depend on their concentration. [B0]** Line 3 is correct [B1].

Correct line 2: hydroxide ions react in a fast step after the rate-determining step. [B1]

The student scores 2 out of 3. The distinction between "not involved" and "not in the slow step" is exactly what examiners test.
:::

### Steps for working with a mechanism

:::steps
1. **Overall equation from a mechanism**: add the steps and cancel anything that appears on both sides. What cancels is an intermediate or a catalyst.
2. **Rate equation from a mechanism**: find the slowest step and write a concentration term for each species in it (squared for two identical particles).
3. **Mechanism from a rate equation**: put the species of the rate equation into the slow step, then add fast steps to complete the overall equation.
4. **Intermediate or catalyst?** Both appear in the mechanism but not in the overall equation. An intermediate is made first and used later; a catalyst is used first and regenerated later.
5. **Rate-determining step**: the step whose reactants match the rate equation; on a pathway diagram, the step with the highest activation energy.
:::

## Catalysts and how they work

A **catalyst** (see [Reaction kinetics](#chem.kinetics)) speeds up a reaction by providing an alternative pathway with a lower activation energy, and is not used up. It changes \(k\). Catalysts fall into two groups, according to their physical state compared with the reactants.

:::def Heterogeneous catalyst
A catalyst that is in a different physical state (phase) from the reactants. Typically it is a solid, with reactants that are gases or in solution.
:::

:::def Homogeneous catalyst
A catalyst that is in the same physical state (phase) as the reactants.
:::

### Heterogeneous catalysis: reactions on a surface

The reaction takes place on the surface of the solid, so a big surface area makes the catalyst work better: the metals are used as fine powders or coatings. There are three stages.

:::steps
1. **Adsorption.** Reactant molecules are held on the surface by weak bonds to the atoms there (they are adsorbed). They are brought close together on the same surface.
2. **Bond weakening and reaction.** Bonding to the surface weakens (or breaks) bonds within the reactant molecules, which lowers the activation energy, and the adsorbed atoms and molecules react.
3. **Desorption.** The product molecules leave the surface, which frees the sites for more reactant.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 460" role="img" aria-label="Three panels of the Haber process on an iron surface: nitrogen and hydrogen molecules arrive and stick to the surface (adsorption); their bonds break and hydrogen atoms join nitrogen atoms; ammonia molecules leave the surface (desorption)"><text class="tl ta" x="8" y="14">1 Adsorption onto the surface</text><circle class="fa" cx="90" cy="52" r="10"/><text class="tl tc tp" x="90" y="56.7">N</text><circle class="fa" cx="110" cy="52" r="10"/><text class="tl tc tp" x="110" y="56.7">N</text><circle class="fa2" cx="212" cy="52" r="8"/><text class="tl tc tp" x="212" y="56.7">H</text><circle class="fa2" cx="228" cy="52" r="8"/><text class="tl tc tp" x="228" y="56.7">H</text><path class="ln" d="M100 68V96" marker-end="url(#ah)"/><path class="ln" d="M220 66V96" marker-end="url(#ah)"/><circle class="fm2" cx="30" cy="118" r="11"/><circle class="fm2" cx="65" cy="118" r="11"/><circle class="fm2" cx="100" cy="118" r="11"/><circle class="fm2" cx="135" cy="118" r="11"/><circle class="fm2" cx="170" cy="118" r="11"/><circle class="fm2" cx="205" cy="118" r="11"/><circle class="fm2" cx="240" cy="118" r="11"/><circle class="fm2" cx="275" cy="118" r="11"/><circle class="fm2" cx="310" cy="118" r="11"/><text class="tl tc" x="170" y="146">iron surface</text><path class="ln-m thin dash" d="M8 156H332"/><text class="tl ta" x="8" y="174">2 Bonds break, new bonds form</text><circle class="fa" cx="70" cy="256" r="10"/><text class="tl tc tp" x="70" y="260.7">N</text><circle class="fa2" cx="112" cy="258" r="8"/><text class="tl tc tp" x="112" y="262.7">H</text><path class="ln dash" d="M82 256H102"/><circle class="fa2" cx="150" cy="258" r="8"/><text class="tl tc tp" x="150" y="262.7">H</text><circle class="fa" cx="190" cy="256" r="10"/><text class="tl tc tp" x="190" y="260.7">N</text><circle class="fa2" cx="232" cy="258" r="8"/><text class="tl tc tp" x="232" y="262.7">H</text><path class="ln dash" d="M202 256H222"/><circle class="fa2" cx="272" cy="258" r="8"/><text class="tl tc tp" x="272" y="262.7">H</text><circle class="fm2" cx="30" cy="278" r="11"/><circle class="fm2" cx="65" cy="278" r="11"/><circle class="fm2" cx="100" cy="278" r="11"/><circle class="fm2" cx="135" cy="278" r="11"/><circle class="fm2" cx="170" cy="278" r="11"/><circle class="fm2" cx="205" cy="278" r="11"/><circle class="fm2" cx="240" cy="278" r="11"/><circle class="fm2" cx="275" cy="278" r="11"/><circle class="fm2" cx="310" cy="278" r="11"/><path class="ln-m thin dash" d="M8 316H332"/><text class="tl ta" x="8" y="334">3 Desorption: ammonia leaves</text><circle class="fa2" cx="90.4" cy="388.8" r="6"/><circle class="fa2" cx="109.6" cy="388.8" r="6"/><circle class="fa2" cx="100" cy="360" r="6"/><circle class="fa" cx="100" cy="376" r="10"/><text class="tl tc tp" x="100" y="380.7">N</text><text class="tl" x="122" y="380">NH₃</text><circle class="fa2" cx="210.4" cy="388.8" r="6"/><circle class="fa2" cx="229.6" cy="388.8" r="6"/><circle class="fa2" cx="220" cy="360" r="6"/><circle class="fa" cx="220" cy="376" r="10"/><text class="tl tc tp" x="220" y="380.7">N</text><text class="tl" x="242" y="380">NH₃</text><path class="ln" d="M68 414V382" marker-end="url(#ah)"/><path class="ln" d="M188 414V382" marker-end="url(#ah)"/><circle class="fm2" cx="30" cy="438" r="11"/><circle class="fm2" cx="65" cy="438" r="11"/><circle class="fm2" cx="100" cy="438" r="11"/><circle class="fm2" cx="135" cy="438" r="11"/><circle class="fm2" cx="170" cy="438" r="11"/><circle class="fm2" cx="205" cy="438" r="11"/><circle class="fm2" cx="240" cy="438" r="11"/><circle class="fm2" cx="275" cy="438" r="11"/><circle class="fm2" cx="310" cy="438" r="11"/></svg><figcaption>A heterogeneous catalyst in three stages. The larger circles marked N are nitrogen atoms, the smaller circles marked H are hydrogen atoms, and the row of large circles at the foot of each panel is the iron surface. In panel 2 the dashed lines are N–H bonds forming as the bonds inside the N₂ and H₂ molecules break. In panel 3 the small unlabelled circles are the hydrogen atoms of each NH₃ molecule.</figcaption></figure>
:::

The best-known examples:

- **Iron in the Haber process.** \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\) is made at about 450 °C with an iron catalyst. Both gases are adsorbed on the iron. The strong \(\ce{N#N}\) bond is weakened and broken on the surface, the atoms combine to give ammonia, and \(\ce{NH3}\) is desorbed. (Conditions and equilibrium: [Chemical equilibria](#chem.equilibria).)
- **Palladium, platinum and rhodium in catalytic converters** (see [Nitrogen and sulfur](#chem.nitrogen)). Carbon monoxide and nitrogen monoxide are adsorbed on a thin layer of the metals spread over a ceramic honeycomb. The N–O and C–O bonds weaken, and the atoms react to form carbon dioxide and nitrogen, which desorb: \(\ce{2CO + 2NO -> 2CO2 + N2}\).

:::eg (Exam style) Explain how rhodium in a catalytic converter increases the rate of \(\ce{2CO(g) + 2NO(g) -> 2CO2(g) + N2(g)}\). [4 marks]
The gases are adsorbed onto the surface of the metal, which holds the molecules close together. [B1]
Bonding to the metal weakens the bonds in CO and NO (the N–O bond in particular), [B1] providing a route with a lower activation energy. [B1]
The products \(\ce{CO2}\) and \(\ce{N2}\) are desorbed, leaving the surface free for more reactants. [B1]
:::

Because a surface has a limited number of sites, a heterogeneous catalyst can behave in unexpected ways. If the surface is crowded with reactant, doubling the concentration adds no extra molecules to it, and the rate stays the same: **zero order**. This is observed, for example, in the decomposition of ammonia on a hot tungsten surface. At a very low concentration the surface is mostly empty and the rate is proportional to the concentration.

:::warn Poisoning
A catalyst can be **poisoned** when a substance sticks permanently to the active sites and blocks them. Lead in petrol coated the surface of catalytic converters, which is why cars with converters must use unleaded petrol. Poisoned catalysts are why industrial feed gases are purified first.
:::

### Homogeneous catalysis: a cycle in solution or gas

A homogeneous catalyst is used in one step and regenerated in a later one. It often does this by changing its oxidation state (a transition metal ion, or a species such as NO).

:::html
<figure class="fig small"><svg viewBox="0 8 330 232" role="img" aria-label="Pathway diagram for the reaction of persulfate ions with iodide ions: one high peak without a catalyst, and two lower peaks joined by a valley with an iron catalyst"><path class="ax" d="M20 205V30" marker-end="url(#ahm)"/><path class="ax" d="M20 205H290" marker-end="url(#ahm)"/><text class="tl" x="28" y="24">enthalpy</text><text class="tl" x="290" y="227" text-anchor="end">progress of reaction</text><path class="ln thick" d="M50 90H90"/><path class="ln thick" d="M250 170H282"/><path class="c1 sw2" d="M90 90C106 90 112 24 150 24C212 24 226 170 250 170"/><path class="c1 sw2 dash" d="M90 90C104 90 108 70 122 70C136 70 142 112 160 112C178 112 184 92 198 92C210 92 218 170 250 170"/><text class="tl tc" x="70" y="108">reactants</text><text class="tl tc" x="266" y="190">products</text><text class="tl tc" x="160" y="132">Fe³⁺ stage</text><path class="c1 sw2" d="M50 158H74"/><text class="tl" x="80" y="162">no catalyst</text><path class="c1 sw2 dash" d="M50 180H74"/><text class="tl" x="80" y="184">with Fe²⁺ catalyst</text></svg><figcaption>The reaction of S₂O₈²⁻ with I⁻ with and without iron ions. The catalysed route has two lower peaks, and the valley between them is the stage when the iron is present as Fe³⁺. Both routes start and end at the same levels, so ΔH is unchanged.</figcaption></figure>
:::

**Oxides of nitrogen and sulfur dioxide.** In the atmosphere, nitrogen dioxide oxidises sulfur dioxide, and is itself reduced to nitrogen monoxide, which air then oxidises back (see [Nitrogen and sulfur](#chem.nitrogen)):

\[\ce{SO2 + NO2 -> SO3 + NO}\]
\[\ce{NO + 1/2 O2 -> NO2}\]

Adding the equations and cancelling gives \(\ce{SO2 + 1/2 O2 -> SO3}\). The \(\ce{NO2}\) is used in step 1 and regenerated in step 2: it is a homogeneous catalyst (all gases). The sulfur trioxide then dissolves in water droplets to make sulfuric acid in acid rain.

**Iron ions, persulfate ions and iodide ions.** The reaction

\[\ce{S2O8^2-(aq) + 2I-(aq) -> 2SO4^2-(aq) + I2(aq)}\]

is thermodynamically feasible (\(E^{\ominus}_{\text{cell}} = 2.01 - 0.54 = +1.47\) V) but slow, because both reactants are **negative ions** that repel each other, so collisions are rarely energetic enough. Iron(II) or iron(III) ions provide a route with two steps, each a collision between oppositely charged ions:

\[\ce{S2O8^2- + 2Fe^2+ -> 2SO4^2- + 2Fe^3+}\]
\[\ce{2Fe^3+ + 2I- -> 2Fe^2+ + I2}\]

The overall change is the same, and the iron is regenerated.

:::eg (Exam style) Explain, using the electrode potentials \(E^{\ominus}(\ce{S2O8^2-}/\ce{SO4^2-}) = +2.01\) V, \(E^{\ominus}(\ce{Fe^3+}/\ce{Fe^2+}) = +0.77\) V and \(E^{\ominus}(\ce{I2}/\ce{I-}) = +0.54\) V, how \(\ce{Fe^2+}\) catalyses the reaction between \(\ce{S2O8^2-}\) and \(\ce{I-}\). [6 marks]
The uncatalysed reaction is slow because \(\ce{S2O8^2-}\) and \(\ce{I-}\) are both negative ions, which repel each other, so the activation energy is high. [B1]
Step 1: \(\ce{S2O8^2- + 2Fe^2+ -> 2SO4^2- + 2Fe^3+}\) is feasible: \(E^{\ominus}_{\text{cell}} = 2.01 - 0.77 = +1.24\) V. [B1]
Step 2: \(\ce{2Fe^3+ + 2I- -> 2Fe^2+ + I2}\) is feasible: \(E^{\ominus}_{\text{cell}} = 0.77 - 0.54 = +0.23\) V. [B1]
Both steps are collisions between oppositely charged ions, which attract, so each step has a lower activation energy. [B1]
\(\ce{Fe^2+}\) is used in step 1 and regenerated in step 2: it is a catalyst. [B1]
The iron(II) and iron(III) ions are in the same aqueous phase as the reactants, so this is homogeneous catalysis. [B1]
:::

Iron(III) ions work as well, by the same two steps in the other order: \(\ce{2Fe^3+ + 2I- -> 2Fe^2+ + I2}\) first, which makes \(\ce{Fe^2+}\) for the persulfate step. The feasibility argument is why transition metals suit this role: they have two stable oxidation states with potentials between those of the two reagents (see [Transition elements](#chem.transition)).

:::cols
:::col Heterogeneous catalyst
Different phase from the reactants (usually a solid). Reaction on the surface: adsorption, bond weakening, reaction, desorption. Easy to separate and reuse. Examples: Fe in the Haber process; Pd, Pt and Rh in converters.
:::
:::col Homogeneous catalyst
Same phase as the reactants. Used in one step and regenerated in a later step, often by changing oxidation state. Examples: \(\ce{NO2}\) with \(\ce{SO2}\); \(\ce{Fe^2+}\)/\(\ce{Fe^3+}\) with \(\ce{S2O8^2-}\) and \(\ce{I-}\); \(\ce{H+}\) with propanone and iodine.
:::
:::

:::eg (Exam style) A student writes: "The catalyst is not involved in the reaction because it is not in the equation." Correct this statement, with an example. [3 marks]
A catalyst **does** take part: it reacts in one step and is regenerated in a later step, so it does not appear in the overall equation. [B1]
Example: \(\ce{Fe^2+}\) reacts with \(\ce{S2O8^2-}\) to form \(\ce{Fe^3+}\), and \(\ce{Fe^3+}\) reacts with \(\ce{I-}\) to reform \(\ce{Fe^2+}\). [B1]
It increases the rate by providing a route with a lower activation energy; it is unchanged in amount at the end. [B1]
:::

:::eg A mechanism has these steps. Step 1 (slow): \(\ce{A + C -> X}\). Step 2 (fast): \(\ce{X + B -> D + C}\). Give the overall equation, the rate equation, the intermediate and the catalyst. [4 marks]
Overall: add the steps and cancel X and C: \(\ce{A + B -> D}\). [B1]
Rate equation: the slow step has A and C: \(\text{rate} = k[\ce{A}][\ce{C}]\). [B1]
The intermediate is X (made in step 1, used in step 2). [B1]
C is the catalyst: used in step 1 and regenerated in step 2, and it appears in the rate equation but not in the overall equation. [B1]
:::

:::try Start easy, finish at exam standard
Q: The rate equation for a reaction is \(\text{rate} = k[\ce{P}]^2[\ce{Q}]\). State the order with respect to each reactant, the overall order and the units of \(k\).
A: Second order in P, first order in Q, third order overall. Units of \(k\): mol⁻² dm⁶ s⁻¹.
Q: A reaction is first order in X and zero order in Y. What happens to the rate when [X] is doubled and [Y] is tripled?
A: It doubles (the zero-order term does not matter).
Q: The rate of a reaction is \(3.6 \times 10^{-4}\) mol dm⁻³ s⁻¹ when \([\ce{A}] = 0.30\) mol dm⁻³ and the rate equation is rate = k[A]. Calculate \(k\).
A: \(k = 3.6 \times 10^{-4}/0.30 = 1.2 \times 10^{-3}\) s⁻¹.
Q: A first-order reaction has a half-life of 40.0 s. Calculate \(k\) and the concentration remaining after 120 s from a start of 0.240 mol dm⁻³.
A: \(k = 0.693/40.0 = 1.73 \times 10^{-2}\) s⁻¹. 120 s is 3 half-lives: \(0.240 \to 0.120 \to 0.0600 \to 0.0300\) mol dm⁻³.
Q: The initial rate of a reaction was \(2.0 \times 10^{-3}\) mol dm⁻³ s⁻¹ when [A] = 0.10 mol dm⁻³ and \(1.8 \times 10^{-2}\) when [A] = 0.30 mol dm⁻³, with [B] constant. What is the order in A?
A: [A] × 3 and rate × 9, so second order in A.
Q: A reaction has rate equation rate = k[X][Y]. The rate is \(4.5 \times 10^{-4}\) mol dm⁻³ s⁻¹ when [X] = 0.050 and [Y] = 0.030 mol dm⁻³. Calculate \(k\) with its units.
A: \(k = 4.5 \times 10^{-4}/(0.050 \times 0.030) = 0.30\) mol⁻¹ dm³ s⁻¹.
Q: A mechanism has slow step 1: \(\ce{2A -> B}\) and fast step 2: \(\ce{B + C -> D}\). Write the rate equation and the overall equation.
A: Rate = \(k[\ce{A}]^2\) (two A in the slow step; C is not). Overall: \(\ce{2A + C -> D}\) (B is the intermediate and cancels).
Q: State the difference between an intermediate and a transition state.
A: An intermediate is a real species in a valley of the pathway diagram, made in one step and used in the next. A transition state is the arrangement of atoms at the peak of a step and cannot be isolated.
Q: Give the three stages of heterogeneous catalysis and say which stage lowers the activation energy.
A: Adsorption, bond weakening and reaction on the surface, desorption. The weakening of the reactants' bonds on the surface gives the lower activation energy.
Q: Why does the temperature affect the rate constant but a change of concentration does not?
A: At a higher temperature more molecules have energy of at least \(E_a\), so more collisions are successful and \(k\) is larger. Concentration changes the rate through the concentration terms, not through \(k\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A reaction has the rate equation \(\text{rate} = k[\ce{P}][\ce{Q}]^2\). (a) State the effect on the rate of tripling [P] and doubling [Q]. (b) Give the units of \(k\).
A: (a) The rate rises by a factor of \(3 \times 2^2 = 12\). [B1]
(b) Overall order 3: \(k = \text{rate}/([\ce{P}][\ce{Q}]^2)\) [B1] with units mol⁻² dm⁶ s⁻¹. [B1]
Q: [5 marks] ★★ The initial rates of \(\ce{BrO3^- + 5Br- + 6H+ -> 3Br2 + 3H2O}\) were measured. Deduce the order with respect to each reactant, write the rate equation and calculate \(k\) with its units.

| Experiment | [BrO₃⁻] / mol dm⁻³ | [Br⁻] / mol dm⁻³ | [H⁺] / mol dm⁻³ | rate / mol dm⁻³ s⁻¹ |
|---|---|---|---|---|
| 1 | 0.010 | 0.10 | 0.10 | \(1.3 \times 10^{-5}\) |
| 2 | 0.020 | 0.10 | 0.10 | \(2.6 \times 10^{-5}\) |
| 3 | 0.010 | 0.20 | 0.10 | \(2.6 \times 10^{-5}\) |
| 4 | 0.010 | 0.10 | 0.20 | \(5.2 \times 10^{-5}\) |

H: In each pair of experiments only one concentration changes. Compare the factor for the concentration with the factor for the rate.
A: Experiments 1 and 2: [BrO₃⁻] × 2, rate × 2: first order in \(\ce{BrO3^-}\). [B1]
Experiments 1 and 3: [Br⁻] × 2, rate × 2: first order in \(\ce{Br-}\). [B1]
Experiments 1 and 4: [H⁺] × 2, rate × 4: second order in \(\ce{H+}\). [B1]
\(\text{rate} = k[\ce{BrO3^-}][\ce{Br-}][\ce{H+}]^2\); \(k = \dfrac{1.3 \times 10^{-5}}{0.010 \times 0.10 \times (0.10)^2}\) [M1]
\(= 1.3\ \text{mol}^{-3}\,\text{dm}^9\,\text{s}^{-1}\) [A1]
Q: [4 marks] ★★ A first-order reaction has a half-life of 25.0 minutes. (a) Calculate the rate constant in s⁻¹. (b) A solution has a concentration of 0.480 mol dm⁻³. What is the concentration 75.0 minutes later?
A: (a) \(t_{\frac12} = 25.0 \times 60 = 1500\) s [M1]; \(k = 0.693/1500 = 4.62 \times 10^{-4}\) s⁻¹ [A1]
(b) 75.0 min = 3 half-lives [M1]; \(0.480 \to 0.240 \to 0.120 \to 0.0600\) mol dm⁻³ [A1]
Q: [4 marks] ★★ The reaction \(\ce{2A + B -> C}\) has the rate equation \(\text{rate} = k[\ce{A}][\ce{B}]\). A two-step mechanism is proposed: step 1 (slow) \(\ce{A + B -> X}\); step 2 (fast) \(\ce{X + A -> C}\). (a) Show the mechanism agrees with the overall equation and the rate equation. (b) Identify the intermediate. (c) Why would a one-step mechanism of \(\ce{A + A + B}\) not give this rate equation?
A: (a) Adding the steps and cancelling X gives \(\ce{2A + B -> C}\). [B1] The slow step has one A and one B, so rate = \(k[\ce{A}][\ce{B}]\). [B1]
(b) The intermediate is X. [B1]
(c) A one-step mechanism would involve two A and one B in the single (slow) step, giving \(\text{rate} = k[\ce{A}]^2[\ce{B}]\), which does not match. [B1]
Q: [5 marks] ★★ Describe, in three stages, how a platinum catalyst in a catalytic converter removes carbon monoxide and nitrogen monoxide from exhaust gas. Give an equation, and state why a larger surface area makes the catalyst more effective.
A: Adsorption: CO and NO molecules are held on the metal surface. [B1]
Bond weakening: bonds in the adsorbed molecules weaken, so the activation energy of the reaction is lowered. [B1]
Reaction and desorption: the products leave the surface. [B1]
\(\ce{2CO + 2NO -> 2CO2 + N2}\) [B1]
A larger surface has more active sites for adsorption, so more reaction can happen at the same time. [B1]
Q: [5 marks] ★★ Nitrogen dioxide catalyses the oxidation of sulfur dioxide in the atmosphere. The first step is \(\ce{SO2 + NO2 -> SO3 + NO}\). (a) Write the second step. (b) Explain why \(\ce{NO2}\) is a catalyst. (c) State whether the catalysis is homogeneous or heterogeneous, and give a reason.
A: (a) \(\ce{NO + 1/2 O2 -> NO2}\) [B1]
(b) Adding the steps gives \(\ce{SO2 + 1/2 O2 -> SO3}\) with \(\ce{NO2}\) cancelling. [B1] \(\ce{NO2}\) is used in step 1 and reformed in step 2, so it is not used up. [B1]
(c) Homogeneous [B1] because \(\ce{NO2}\) is a gas in the same phase as the reactants. [B1]
Q: [6 marks] ★★★ Iron(II) ions catalyse the reaction between peroxodisulfate and iodide ions. Using \(E^{\ominus}(\ce{S2O8^2-}/\ce{SO4^2-}) = +2.01\) V, \(E^{\ominus}(\ce{Fe^3+}/\ce{Fe^2+}) = +0.77\) V, \(E^{\ominus}(\ce{I2}/\ce{I-}) = +0.54\) V, (a) write the two steps, (b) show with calculations that both are feasible, and (c) explain why the catalysed route is faster.
A: (a) \(\ce{S2O8^2- + 2Fe^2+ -> 2SO4^2- + 2Fe^3+}\) and \(\ce{2Fe^3+ + 2I- -> 2Fe^2+ + I2}\) [B1 B1]
(b) \(E^{\ominus}_{\text{cell}} = 2.01 - 0.77 = +1.24\) V for step 1 [B1]; \(0.77 - 0.54 = +0.23\) V for step 2. Both are positive, so both are feasible. [B1]
(c) The uncatalysed reaction is between two negative ions, which repel. [B1] Each catalysed step is between oppositely charged ions, so the activation energies are lower. [B1]
Q: [6 marks] ★★★ The concentration of A was followed over time. Deduce the order, write the rate equation and calculate \(k\), given that the initial rate (the gradient of the tangent at \(t = 0\)) is \(0.0160\) mol dm⁻³ s⁻¹.

| time / s | 0 | 50 | 150 | 350 |
|---|---|---|---|---|
| [A] / mol dm⁻³ | 0.800 | 0.400 | 0.200 | 0.100 |

H: Find the time taken for each halving of the concentration.
A: The half-lives are 50 s (0.800 to 0.400), 100 s (0.400 to 0.200) and 200 s (0.200 to 0.100). [B1]
The half-life doubles each time. [B1]
The reaction is second order in A. [B1]
\(\text{rate} = k[\ce{A}]^2\) [B1]
\(k = \dfrac{0.0160}{(0.800)^2}\) [M1] \(= 0.0250\ \text{mol}^{-1}\,\text{dm}^3\,\text{s}^{-1}\) [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The reaction \(\ce{H2O2 + 2I- + 2H+ -> I2 + 2H2O}\) has the rate equation \(\text{rate} = k[\ce{H2O2}][\ce{I-}]\). (a) State the order with respect to each reactant and the units of \(k\). (b) The mechanism has three steps. Step 1: \(\ce{H2O2 + I- -> IO- + H2O}\). Step 2: \(\ce{IO- + H+ -> HOI}\). Step 3: \(\ce{HOI + I- + H+ -> I2 + H2O}\). Show that the steps add up to the overall equation, and identify the rate-determining step and the two intermediates. (c) Explain why \(\ce{H+}\) does not appear in the rate equation.
H: Add the three steps and cancel what appears on both sides.
H: Which step contains exactly the species in the rate equation?
A: (a) First order in \(\ce{H2O2}\), first order in \(\ce{I-}\), zero order in \(\ce{H+}\); overall order 2, so \(k\) has units mol⁻¹ dm³ s⁻¹. [B1 B1]
(b) Adding: \(\ce{H2O2 + 2I- + 2H+ + IO- + HOI -> IO- + HOI + I2 + 2H2O}\); cancelling \(\ce{IO-}\) and \(\ce{HOI}\) gives the overall equation. [B1]
Step 1 is the rate-determining step because it contains \(\ce{H2O2}\) and \(\ce{I-}\), the species in the rate equation. [B1]
The intermediates are \(\ce{IO-}\) and \(\ce{HOI}\). [B1]
(c) \(\ce{H+}\) reacts only in the fast steps after the rate-determining step, so changing its concentration does not change the rate. [B1]
Q: [5 marks] ★★★ Ammonia decomposes on a hot tungsten surface, \(\ce{2NH3 -> N2 + 3H2}\), and the reaction is zero order in ammonia over a wide range of concentration. (a) Describe the shape of a graph of [NH₃] against time. (b) Explain why the reaction is zero order. (c) What would you expect if the pressure of ammonia were reduced to a very low value?
H: Think about the number of places on the surface where molecules can sit.
A: (a) A straight line with a negative gradient. [B1]
(b) The surface sites are all occupied by ammonia, so the rate is limited by the number of sites, not by the concentration of ammonia in the gas. [B1] Increasing the concentration adds no more molecules to the surface. [B1]
(c) At very low pressure many sites are empty, so the rate would depend on the concentration of ammonia. [B1] The reaction would show first order (rate proportional to [NH₃]). [B1]
:::

:::quiz
? Which method can give the order of reaction with respect to a reactant?
- Reading the coefficients from the balanced equation
+ Comparing initial rates when only that concentration is changed
- Measuring the colour of the products
- Calculating it from the activation energy
> Orders come from experiments. The coefficients in the equation show the amounts that react, and may not match the orders.
? The rate equation is \(\text{rate} = k[\ce{A}][\ce{B}]\). What are the units of \(k\)?
- s⁻¹
- mol dm⁻³ s⁻¹
+ mol⁻¹ dm³ s⁻¹
- mol⁻² dm⁶ s⁻¹
> The reaction is second order overall: \((\text{mol dm}^{-3}\,\text{s}^{-1})/(\text{mol dm}^{-3})^2 = \text{mol}^{-1}\,\text{dm}^3\,\text{s}^{-1}\).
? Doubling [A] makes the rate go up four times and doubling [B] has no effect. What is the rate equation?
- rate = k[A][B]
- rate = k[A]
+ rate = k[A]²
- rate = k[A]²[B]²
> Factor 4 for doubling gives second order in A. [B] does not change the rate, so it is zero order and left out.
? For a first-order reaction, which statement is true?
- The half-life doubles each time.
+ The half-life is constant.
- The rate is constant.
- The half-life is proportional to the starting concentration.
> The rate is proportional to [A], so the concentration falls by half in the same time wherever it starts. A doubling half-life is second order; a constant rate is zero order.
? The half-life of a first-order reaction is 40.0 s. What is k?
- 27.7 s⁻¹
+ \(1.73 \times 10^{-2}\) s⁻¹
- 57.7 s⁻¹
- 40.0 s⁻¹
> \(k = 0.693/t_{\frac12} = 0.693/40.0 = 1.73 \times 10^{-2}\) s⁻¹. Multiplying 0.693 by 40.0 gives 27.7, and dividing 40.0 by 0.693 gives 57.7: both turn the formula upside down.
? What is the shape of a graph of rate against concentration for a first-order reaction?
- a horizontal line
+ a straight line through the origin
- a curve that gets steeper
- a curve that levels off
> \(\text{rate} = k[\ce{A}]\) is proportional to [A], so the graph is a straight line through the origin with gradient \(k\). A horizontal line is zero order and an upward curve is second order.
? The rate equation is \(\text{rate} = k[\ce{X}][\ce{Y}]\) for the overall reaction \(\ce{2X + Y -> Z}\). Which is true of the rate-determining step?
- It contains two molecules of X.
+ It contains one molecule of X and one of Y.
- It contains only Y.
- It cannot be identified.
> The species in the rate equation, with the powers shown, are the species in the slow step.
? What distinguishes a catalyst from an intermediate in a mechanism?
+ A catalyst is used in one step and regenerated in a later step; an intermediate is made in one step and used in a later one.
- A catalyst appears in the overall equation; an intermediate does not.
- A catalyst changes ΔH; an intermediate does not.
- A catalyst is always a solid; an intermediate is always a gas.
> Both are missing from the overall equation. The order in which they are made and used tells them apart, and a catalyst may be in any phase. Neither changes ΔH.
? Why does raising the temperature increase the rate constant?
- It increases the activation energy.
- It increases the concentrations of the reactants.
+ A larger proportion of the molecules has energy of at least the activation energy.
- It provides an alternative reaction pathway.
> The Boltzmann distribution shifts to higher energy, so more collisions are successful. Temperature does not change \(E_a\); an alternative pathway is what a catalyst offers.
:::

:::checklist What you can now do
- [ ] I can define rate equation, order, overall order, rate constant, half-life, rate-determining step and intermediate.
- [ ] I can write a rate equation of the form rate = k[A]^m[B]^n and explain why it cannot be deduced from the balanced equation.
- [ ] I can recognise zero-, first- and second-order reactions from concentration–time and rate–concentration graphs.
- [ ] I can find an initial rate from a tangent at t = 0 and use initial rates to deduce orders and construct a rate equation.
- [ ] I can use constant and changing half-lives to find the order, and use \(t_{\frac12} = 0.693/k\) for first-order reactions.
- [ ] I can calculate k and give its units for orders 0, 1, 2 and 3.
- [ ] I can predict the rate equation from a mechanism, and suggest a mechanism consistent with a rate equation and an overall equation.
- [ ] I can identify intermediates, catalysts and the rate-determining step in a mechanism.
- [ ] I can state that a higher temperature increases k.
- [ ] I can describe heterogeneous catalysis (adsorption, bond weakening, desorption) with Fe in the Haber process and Pd, Pt and Rh in converters.
- [ ] I can describe homogeneous catalysis with oxides of nitrogen and SO₂, and with Fe²⁺ or Fe³⁺ in the S₂O₈²⁻/I⁻ reaction.
:::

:::recap
- Rate = k[A]^m[B]^n. Orders (0, 1, 2) come from experiment, not from the balanced equation. Overall order = sum. Doubling a concentration: × 1, × 2, × 4 for order 0, 1, 2.
- Units of k: derive from the rate equation. Order 0: mol dm⁻³ s⁻¹; 1: s⁻¹; 2: mol⁻¹ dm³ s⁻¹; 3: mol⁻² dm⁶ s⁻¹.
- Graphs: [A]–t: zero order a straight line, first order an exponential curve, second order a flatter curve. Rate–[A]: horizontal line, straight line through the origin, upward curve. Initial rate is the gradient of the tangent at t = 0.
- First-order half-life is constant; \(k = 0.693/t_{\frac12}\). Zero order: successive half-lives halve; second order: they double.
- Initial rates: change one concentration at a time and compare ratios. A clock reaction gives rate ∝ 1/time.
- k depends on temperature (higher T gives larger k, since more molecules have E ≥ Eₐ) and on a catalyst, not on concentration.
- Mechanism: the slow step sets the rate; the rate equation holds the species in the slow step (and before it). Intermediates and catalysts cancel in the overall equation. Zero order means "not in or before the rate-determining step".
- Heterogeneous catalyst (different phase): adsorption, bond weakening, desorption (Fe in the Haber process; Pd, Pt, Rh in converters). Homogeneous catalyst (same phase): used in one step, regenerated in another (NO₂/SO₂; Fe²⁺/Fe³⁺ with S₂O₈²⁻ and I⁻, each step between oppositely charged ions).
:::

:::links
- read: [Orders of reaction and rate equations](https://www.chemguide.co.uk/physical/basicrates/orders.html) · Chemguide · orders, rate constants and how to find them from data
- read: [Orders of reaction and mechanisms](https://www.chemguide.co.uk/physical/basicrates/ordermech.html) · Chemguide · how the rate equation points to the rate-determining step
- read: [Types of catalysis](https://www.chemguide.co.uk/physical/catalysis/introduction.html) · Chemguide · heterogeneous and homogeneous catalysts, with the persulfate and iodide example
- read: [Catalysts in inorganic industrial processes](https://www.chemguide.co.uk/physical/catalysis/inorganic.html) · Chemguide · catalysts in the Haber and Contact processes
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Transition elements](#chem.transition) shows why the d-block metals make such good catalysts.
