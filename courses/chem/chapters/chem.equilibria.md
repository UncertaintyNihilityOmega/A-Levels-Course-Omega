@chapter chem.equilibria
@title Chemical equilibria
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 7–9 hours
@summary Many reactions can run in both directions and settle into a balance. You will learn what dynamic equilibrium is, how to predict the effect of changing concentration, pressure, temperature or a catalyst (Le Chatelier's principle), how to write and use Kc and Kp, and why the Haber and Contact processes use the conditions they do.

:::why
The ammonia made by the Haber process is the starting point for most of the nitrogen fertiliser on farms, and it is made from nitrogen and hydrogen by a reaction that stops part-way: the products turn back into reactants as fast as they form. Chemists who understand equilibrium can pick the pressure, temperature and catalyst that give the most product for the least cost. The same ideas explain why a fizzy drink goes flat, why acids are strong or weak, and why some reactions seem never to finish.
:::

**Before you start**, you should know how to calculate amounts and concentrations from [Moles and stoichiometry](#chem.moles), how gas pressure and volume are related from [States of matter](#chem.states), and what an exothermic and an endothermic reaction are from [Chemical energetics](#chem.energetics).

:::try Warm-up
Q: 0.200 mol of a solute is dissolved to make 500 cm³ of solution. What is its concentration in mol dm⁻³? (from [Moles and stoichiometry](#chem.moles))
A: \(c = n/V = 0.200 / 0.500 = 0.400\) mol dm⁻³.
Q: What happens to the pressure of a fixed amount of gas at constant temperature when its volume is halved? (from [States of matter](#chem.states))
A: The pressure doubles (\(p \propto 1/V\)), because the same number of molecules hit the walls more often.
Q: Is the sign of ΔH positive or negative for an exothermic reaction, and are the products higher or lower in energy than the reactants? (from [Chemical energetics](#chem.energetics))
A: ΔH is negative, and the products are lower in energy than the reactants.
:::

## Reversible reactions and dynamic equilibrium

Most reactions you have met so far "go to completion": magnesium burns until the magnesium or the oxygen runs out, and the product does not turn back into magnesium. Some reactions do not. Heat blue hydrated copper(II) sulfate and it loses its water and turns white. Add water to the white solid and it turns blue again. The same reaction can go either way.

:::def Reversible reaction
A reaction in which the products can react to re-form the reactants, so that the reaction can proceed in both the forward and the reverse direction. It is shown with the symbol \(\ce{<=>}\).
:::

\[\ce{CuSO4.5H2O(s) <=> CuSO4(s) + 5H2O(l)}\]

Now imagine a reversible reaction in a closed vessel, starting with only the reactants. At first the reactants are at their highest concentration, so the **forward** reaction is at its fastest. As products form, the **reverse** reaction begins and speeds up, while the falling concentration of the reactants slows the forward reaction. Eventually the two rates become equal. From then on, each reactant molecule used up in the forward reaction is replaced by one formed in the reverse reaction.

:::plot The concentrations of a reactant A and a product B in A ⇌ B, starting with only A. They change quickly at first, then level off at constant values (not equal to each other).
--f "1-0.6*(1-exp(-x))" --f "0.6*(1-exp(-x))" --label "[A]" --label "[B]" --x 0 6 --y 0 1.4 --xlabel "time" --ylabel "concentration" --legend tr
:::

:::plot The rates of the forward and reverse reactions in A ⇌ B. The forward rate falls and the reverse rate rises until they are equal; the two lines then stay together.
--f "1-0.6*(1-exp(-x))" --f "0.4*(1-exp(-x))" --label "forward rate" --label "reverse rate" --x 0 6 --y 0 1.4 --xlabel "time" --ylabel "rate" --legend tr
:::

:::def Dynamic equilibrium
The state of a reversible reaction in which the rate of the forward reaction equals the rate of the reverse reaction, so that the concentrations of reactants and products stay constant.
:::

The word **dynamic** matters. At equilibrium the reactions have not stopped: molecules are still reacting in both directions, but at the same rate, so nothing changes overall. This is like a moving escalator that carries people up as fast as they walk down: someone standing at the same height is still moving.

:::def Closed system
A system in which nothing can enter or leave: no reactants or products escape, so the amounts of all the species can only change through the reaction itself. A dynamic equilibrium can be reached only in a closed system.
:::

A reversible reaction in an open flask can still be reversible, but a gas that escapes is lost, and the reaction keeps going forwards until the reactant is gone. A sealed container is what lets the system settle.

The mixture at equilibrium contains **both** reactants and products. How much of each there is depends on the reaction and the conditions. When the equilibrium mixture is mostly products, we say the **position of equilibrium lies to the right** (towards the products). When it is mostly reactants, the position lies to the left.

:::warn Two common wrong ideas
- "At equilibrium the reaction has stopped." No: both reactions continue at equal rates.
- "At equilibrium the concentrations of reactants and products are equal." No: they are **constant**, and usually different. In the graph above, [A] and [B] level off at 0.4 and 0.6.
:::

## Le Chatelier's principle

If a system at equilibrium is disturbed, it adjusts itself and settles at a new equilibrium. The direction of the adjustment can be predicted from one rule.

:::def Le Chatelier's principle
If a change is made to a system at dynamic equilibrium, the position of equilibrium moves to minimise this change.
:::

"Minimise" means the system acts to oppose the change, never to cancel it completely. We shall use the Haber process as the example throughout:

\[\ce{N2(g) + 3H2(g) <=> 2NH3(g)} \qquad \Delta H \text{ is negative (the forward reaction is exothermic)}\]

Four moles of gas on the left (1 + 3) become two moles on the right.

### Changing the concentration

If you **add** more of a reactant, the position moves to the right: the extra reactant is used up (the change is minimised). If you **remove** a product, the position moves to the right again, making more product to replace it. Adding product, or removing reactant, moves the position to the left.

The reason is in the rates. If more \(\ce{N2}\) is added, the forward reaction suddenly speeds up because its reactant concentration is higher, while the reverse rate has not yet changed. The forward reaction now runs faster than the reverse, so there is a net conversion of reactants into products until the rates are equal again, at a new equilibrium with more \(\ce{NH3}\).

### Changing the pressure

Pressure only matters when gases take part, and when the number of gas molecules changes in the reaction. **Increasing** the pressure moves the position towards the side with **fewer moles of gas**, because this reduces the pressure. **Decreasing** the pressure moves it towards the side with more moles of gas.

For the Haber process, high pressure moves the position to the right (2 mol of gas instead of 4). For \(\ce{H2(g) + I2(g) <=> 2HI(g)}\) there are 2 mol of gas on each side, so changing the pressure moves nothing: the position is unchanged.

:::note Adding an unreactive gas
Adding an inert gas such as argon to a sealed vessel at constant volume raises the total pressure, but not the partial pressures of the reacting gases, so their concentrations do not change and the position does not move. What matters is the pressure of the reacting gases themselves.
:::

### Changing the temperature

Every reversible reaction is exothermic in one direction and endothermic in the other, with the same size of ΔH. **Increasing the temperature** moves the position in the **endothermic** direction, which absorbs heat (the change is minimised). **Decreasing the temperature** moves it in the **exothermic** direction, which releases heat.

For the Haber process the forward reaction is exothermic, so raising the temperature moves the position to the **left**, and the equilibrium mixture contains less ammonia. This is the only change that alters the value of the equilibrium constant (see below).

### Adding a catalyst

A catalyst speeds up the forward and the reverse reactions **by the same factor**. It makes the system reach equilibrium sooner, but it does **not** change the position of equilibrium or the amount of product at equilibrium.

:::key Le Chatelier's principle: the effects
| Change | Position of equilibrium moves | Value of K |
|---|---|---|
| increase the concentration of a reactant | right (towards products) | unchanged |
| increase the concentration of a product | left (towards reactants) | unchanged |
| increase the pressure (gases) | towards the side with fewer moles of gas | unchanged |
| increase the temperature | in the endothermic direction | changes |
| add a catalyst | no change (equilibrium reached faster) | unchanged |
:::

Try it with the widget. Choose a system and make a change: the shift, the value of K and the amounts at equilibrium respond.

:::html
<div class="widget" data-w="chem-equilibrium" data-system="haber"></div>
:::

:::eg (Exam style) The Haber process is \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\), ΔH negative. State and explain the effect on the position of equilibrium and on the equilibrium yield of ammonia of (a) increasing the pressure, (b) increasing the temperature, (c) removing ammonia as it forms, (d) adding a catalyst. [5 marks]
(a) The position moves to the right, because there are fewer moles of gas on the right (2 against 4), so the system minimises the increase in pressure. The yield of ammonia increases. [B1]

(b) The forward reaction is exothermic, so increasing the temperature moves the position to the left, in the endothermic direction, to absorb the added heat. The yield of ammonia decreases. [B1] [B1]

(c) Removing ammonia moves the position to the right, to replace the ammonia that was removed, so more ammonia is formed. [B1]

(d) A catalyst does not change the position or the equilibrium yield: it speeds up the forward and reverse reactions equally, so equilibrium is reached sooner. [B1]
:::

:::eg (Real context) A fizzy drink is bottled with carbon dioxide dissolved under pressure: \(\ce{CO2(g) <=> CO2(aq)}\). Explain why bubbles appear when the bottle is opened.
Opening the bottle lowers the pressure of the gas above the liquid. The position of equilibrium moves to the left, towards the side with more gas, so dissolved \(\ce{CO2}\) comes out of solution as bubbles. Warming the drink also makes it fizz more: dissolving a gas in a liquid releases heat (it is exothermic), so raising the temperature moves the position to the left as well.
:::

:::warn Position, rate and K are three different things
A higher temperature makes both reactions **faster** (rates), moves the **position** in the endothermic direction, and changes the value of **K** (only temperature does). A catalyst changes the rates only. Concentration and pressure change the position but not K. Never write "the equilibrium shifts to the right because the rate of the forward reaction is faster" as a full answer: say which direction is endothermic, or which side has fewer gas molecules.
:::

:::exam Writing a Le Chatelier answer
A complete answer has three parts: **the change** ("the temperature is raised"), **what the system does to oppose it** ("the position moves in the endothermic direction, absorbing heat; here that is to the left"), and **the consequence** ("so the yield of ammonia falls"). "The equilibrium shifts to the right" alone, with no reason, earns no marks.
:::

:::eg Spot the error: the Contact process is \(\ce{2SO2(g) + O2(g) <=> 2SO3(g)}\), and the forward reaction is exothermic. Explain the effect of increasing the temperature on the equilibrium yield of sulfur trioxide. [3 marks]
A student wrote this answer.

Line 1: Increasing the temperature makes the particles move faster, so the rate of the forward reaction increases.
Line 2: So the position of equilibrium moves to the right and more sulfur trioxide forms.
Line 3: The yield of sulfur trioxide therefore increases.

Line 1 is true but it is about the rate, not the position, so it earns no mark [B0]. **Line 2 is wrong: the forward reaction is exothermic, so increasing the temperature moves the position in the endothermic direction, to the left, to absorb heat [B0].** Line 3 follows from line 2 but is also wrong: the yield decreases [B0].

The student scores 0 out of 3 on the position and yield, and gains nothing for the true statement about rate. Correct lines: increasing the temperature moves the position in the endothermic direction, which is the reverse reaction, so it moves to the left [B1], absorbing the added heat [B1]. The equilibrium yield of \(\ce{SO3}\) therefore decreases. [B1]
:::

## The equilibrium constant, Kc

The position of equilibrium can be put into one number. For a reversible reaction in which \(a\) mol of A and \(b\) mol of B form \(c\) mol of C and \(d\) mol of D, the concentrations at equilibrium obey a fixed relationship at a given temperature.

:::formula Equilibrium constant Kc
\[\ce{aA + bB <=> cC + dD} \qquad K_c = \frac{[\mathrm{C}]^{c}\,[\mathrm{D}]^{d}}{[\mathrm{A}]^{a}\,[\mathrm{B}]^{b}}\]
[X] is the concentration of X in mol dm⁻³ **at equilibrium**. Products go on the top and reactants on the bottom, and each concentration is raised to the power of its coefficient in the balanced equation.
:::

:::def Equilibrium constant, Kc
The value of the expression for the concentrations of products over reactants (each to the power of its coefficient) at equilibrium, for a reversible reaction at a given temperature.
:::

For the Haber process:

\[K_c = \frac{[\ce{NH3}]^2}{[\ce{N2}]\,[\ce{H2}]^3}\]

The expression comes from the equation as written, so if you write the equation the other way round, the new constant is the **reciprocal**: for \(\ce{2NH3 <=> N2 + 3H2}\), the constant is \(1/K_c\).

:::eg Write the Kc expression for (a) \(\ce{2SO2(g) + O2(g) <=> 2SO3(g)}\), (b) \(\ce{H2(g) + I2(g) <=> 2HI(g)}\), (c) \(\ce{CH3COOH(l) + C2H5OH(l) <=> CH3COOC2H5(l) + H2O(l)}\).
(a) \(K_c = \dfrac{[\ce{SO3}]^2}{[\ce{SO2}]^2\,[\ce{O2}]}\)

(b) \(K_c = \dfrac{[\ce{HI}]^2}{[\ce{H2}]\,[\ce{I2}]}\)

(c) \(K_c = \dfrac{[\ce{CH3COOC2H5}]\,[\ce{H2O}]}{[\ce{CH3COOH}]\,[\ce{C2H5OH}]}\). The water is a product in an organic mixture, not a solvent in large excess, so it is included.
:::

### Heterogeneous equilibria

In a **homogeneous** equilibrium, all the species are in the same phase (all gases, or all in solution). In a **heterogeneous** equilibrium, some are in different phases, such as a solid and a gas. The concentration of a pure solid is constant, so solids are **left out** of the expression.

\[\ce{CaCO3(s) <=> CaO(s) + CO2(g)} \qquad K_c = [\ce{CO2}]\]

### Units of Kc

The units of Kc come from the expression. Replace each concentration by "mol dm⁻³", cancel, and give what is left. If everything cancels, Kc has no unit.

| Equilibrium | Expression | Unit of Kc |
|---|---|---|
| \(\ce{H2 + I2 <=> 2HI}\) | \([\ce{HI}]^2 / ([\ce{H2}][\ce{I2}])\) | none |
| \(\ce{N2O4 <=> 2NO2}\) | \([\ce{NO2}]^2 / [\ce{N2O4}]\) | mol dm⁻³ |
| \(\ce{2SO2 + O2 <=> 2SO3}\) | \([\ce{SO3}]^2 / ([\ce{SO2}]^2[\ce{O2}])\) | mol⁻¹ dm³ |
| \(\ce{N2 + 3H2 <=> 2NH3}\) | \([\ce{NH3}]^2 / ([\ce{N2}][\ce{H2}]^3)\) | mol⁻² dm⁶ |

The unit is \((\mathrm{mol\,dm^{-3}})^{\Delta n}\), where \(\Delta n\) is the number of moles of products minus the number of moles of reactants in the gaseous or dissolved species. For the Haber process \(\Delta n = 2 - 4 = -2\), which gives mol⁻² dm⁶.

### What the size of K tells you

A large \(K_c\) (much greater than 1) means the numerator is large compared with the denominator, so the equilibrium mixture is mostly products. A very small \(K_c\) (much less than 1) means mostly reactants. A \(K_c\) near 1 means there are significant amounts of both. The value tells you where the position lies, not how fast the equilibrium is reached.

### Calculating Kc from equilibrium amounts

When the amounts at equilibrium are given in moles, divide each by the volume of the vessel to get concentrations. When the reaction has the same number of moles of gas on each side (\(\Delta n = 0\)), the volumes cancel and you can use the moles directly.

:::eg 0.600 mol of ethanoic acid and 0.600 mol of ethanol are mixed with a little acid catalyst and left until equilibrium is reached: \(\ce{CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O}\). The equilibrium mixture contains 0.200 mol of ethanoic acid, 0.200 mol of ethanol, 0.400 mol of ethyl ethanoate and 0.400 mol of water. Calculate Kc.
The volume \(V\) is the same for every species, and there are two species on the top and two on the bottom, so \(V\) cancels:

\[K_c = \frac{\dfrac{0.400}{V} \times \dfrac{0.400}{V}}{\dfrac{0.200}{V} \times \dfrac{0.200}{V}} = \frac{0.400 \times 0.400}{0.200 \times 0.200} = 4.00\] [M1] [A1]

The volumes cancel, so Kc has no unit. [B1]
:::

:::eg 1.00 mol of hydrogen and 1.00 mol of iodine are heated in a sealed vessel until equilibrium is reached: \(\ce{H2(g) + I2(g) <=> 2HI(g)}\). The equilibrium mixture contains 1.50 mol of hydrogen iodide. Calculate Kc.
Use an ICE table (initial, change, equilibrium) in moles:

| | \(\ce{H2}\) | \(\ce{I2}\) | \(\ce{HI}\) |
|---|---|---|---|
| initial / mol | 1.00 | 1.00 | 0 |
| change / mol | −0.75 | −0.75 | +1.50 |
| equilibrium / mol | 0.25 | 0.25 | 1.50 |

The 1.50 mol of HI needs half as many moles of each reactant (the ratio is 1 : 1 : 2), so 0.75 mol of each is used up, leaving 0.25 mol. [M1]

\[K_c = \frac{(1.50)^2}{0.25 \times 0.25} = 36.0\] [M1] [A1]

There are 2 mol of gas on each side, so the volume cancels and there is no unit. [B1]
:::

:::eg 1.00 mol of dinitrogen tetroxide is placed in a 2.00 dm³ vessel and decomposes: \(\ce{N2O4(g) <=> 2NO2(g)}\). At equilibrium 0.600 mol of \(\ce{N2O4}\) remains. Calculate Kc, with its unit.
\(\ce{N2O4}\) used = 1.00 − 0.600 = 0.400 mol, which makes \(2 \times 0.400 = 0.800\) mol of \(\ce{NO2}\). [M1]

Concentrations: \([\ce{N2O4}] = 0.600 / 2.00 = 0.300\) mol dm⁻³ and \([\ce{NO2}] = 0.800 / 2.00 = 0.400\) mol dm⁻³. [M1]

\[K_c = \frac{[\ce{NO2}]^2}{[\ce{N2O4}]} = \frac{(0.400)^2}{0.300} = 0.533\,\mathrm{mol\,dm^{-3}}\] [A1]

Here \(\Delta n = 1\), so the volume does **not** cancel: you must convert to concentrations before substituting. [B1]
:::

:::eg 2.00 mol of sulfur dioxide and 1.00 mol of oxygen are sealed in a 5.00 dm³ vessel with a catalyst. At equilibrium the vessel holds 1.60 mol of sulfur trioxide: \(\ce{2SO2(g) + O2(g) <=> 2SO3(g)}\). Calculate Kc and give its unit.
\(\ce{SO3}\) formed = 1.60 mol, which uses 1.60 mol of \(\ce{SO2}\) and 0.80 mol of \(\ce{O2}\) (ratio 2 : 1 : 2). [M1]

At equilibrium: \(\ce{SO2}\) = 2.00 − 1.60 = 0.40 mol; \(\ce{O2}\) = 1.00 − 0.80 = 0.20 mol; \(\ce{SO3}\) = 1.60 mol.

Concentrations (divide by 5.00 dm³): \([\ce{SO2}] = 0.0800\), \([\ce{O2}] = 0.0400\), \([\ce{SO3}] = 0.320\) mol dm⁻³. [M1]

\[K_c = \frac{(0.320)^2}{(0.0800)^2 \times 0.0400} = 400\,\mathrm{mol^{-1}\,dm^{3}}\] [A1] [B1]
:::

The calculator below builds the ICE table from one equilibrium amount that you know and then works out Kc and its unit. It starts with the sulfur dioxide example above. Change the numbers or the coefficients and check your own working against it.

:::html
<div class="widget" data-w="chem-equilibrium" data-system="contact" data-tab="kc"></div>
:::

### Calculating an equilibrium amount from Kc

If you are given Kc and the starting amounts, you can find the equilibrium amounts. You are not asked to solve quadratic equations in this course, so the examples are designed so that taking a square root gives the answer.

:::eg The esterification \(\ce{CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O}\) has \(K_c = 4.00\) at a certain temperature. 1.00 mol of ethanoic acid is mixed with 1.00 mol of ethanol. Calculate the amount of ethyl ethanoate at equilibrium.
Let \(x\) mol of ester form. Then \(x\) mol of water form, and \(x\) mol each of acid and ethanol are used up:

| | acid | ethanol | ester | water |
|---|---|---|---|---|
| initial / mol | 1.00 | 1.00 | 0 | 0 |
| change / mol | −x | −x | +x | +x |
| equilibrium / mol | 1.00 − x | 1.00 − x | x | x |

The volume cancels (two species top and bottom): [M1]

\[K_c = \frac{x^2}{(1.00 - x)^2} = 4.00\]

Take the square root of both sides: \(\dfrac{x}{1.00 - x} = 2.00\) [M1]

So \(x = 2.00 - 2.00x\), giving \(3.00x = 2.00\) and \(x = 0.667\) mol of ester. [A1]
:::

### Reversing the equation

A final point, which is often asked as a short calculation: writing the reaction in the opposite direction inverts K. If \(K_c = 4.00\) for the esterification, then for the hydrolysis \(\ce{CH3COOC2H5 + H2O <=> CH3COOH + C2H5OH}\), \(K_c = 1/4.00 = 0.250\). The same equilibrium mixture is described, only with the labels reversed.

## Partial pressure and Kp

Gases are easier to measure by pressure than by concentration, so equilibria between gases are often described using **partial pressures**.

:::def Mole fraction
The mole fraction of a gas in a mixture is the number of moles of that gas divided by the total number of moles of gas in the mixture: \(x_{\mathrm{A}} = n_{\mathrm{A}} / n_{\mathrm{total}}\). The mole fractions of all the gases add up to 1.
:::

:::def Partial pressure
The partial pressure of a gas in a mixture is the pressure it would exert if it alone occupied the container. It equals its mole fraction multiplied by the total pressure, \(p_{\mathrm{A}} = x_{\mathrm{A}} \times p_{\mathrm{total}}\), and the partial pressures add up to the total pressure.
:::

:::eg A mixture contains 1.00 mol of nitrogen, 3.00 mol of hydrogen and 1.00 mol of ammonia at a total pressure of 200 atm. Calculate the mole fraction and partial pressure of each gas.
Total amount = 1.00 + 3.00 + 1.00 = 5.00 mol. [B1]

Mole fractions: \(\ce{N2}\) 1.00/5.00 = 0.200; \(\ce{H2}\) 3.00/5.00 = 0.600; \(\ce{NH3}\) 1.00/5.00 = 0.200. They add to 1.00. [M1]

Partial pressures: \(p(\ce{N2}) = 0.200 \times 200 = 40.0\) atm; \(p(\ce{H2}) = 0.600 \times 200 = 120\) atm; \(p(\ce{NH3}) = 0.200 \times 200 = 40.0\) atm. They add to 200 atm. [A1]
:::

The **equilibrium constant in terms of partial pressures**, \(K_p\), has the same form as \(K_c\), with partial pressures replacing concentrations. Only gases are included.

:::formula Equilibrium constant Kp
\[\ce{aA(g) + bB(g) <=> cC(g) + dD(g)} \qquad K_p = \frac{p_{\mathrm{C}}^{\,c}\,p_{\mathrm{D}}^{\,d}}{p_{\mathrm{A}}^{\,a}\,p_{\mathrm{B}}^{\,b}}\]
\(p_{\mathrm{X}}\) is the partial pressure of X at equilibrium. Its unit is the unit of pressure (Pa or atm) to the power \(\Delta n\), where \(\Delta n\) is moles of gaseous products minus moles of gaseous reactants.
:::

For the Haber process:

\[K_p = \frac{p(\ce{NH3})^2}{p(\ce{N2})\,\,p(\ce{H2})^3}\]

The unit is atm⁻² (or Pa⁻²), because \(\Delta n = -2\). For \(\ce{CaCO3(s) <=> CaO(s) + CO2(g)}\), \(K_p = p(\ce{CO2})\), with the solids left out.

:::eg The mixture of nitrogen, hydrogen and ammonia in the previous example is at equilibrium at 200 atm. Calculate Kp for \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\), with its unit.
\[K_p = \frac{p(\ce{NH3})^2}{p(\ce{N2})\,p(\ce{H2})^3} = \frac{(40.0)^2}{40.0 \times (120)^3}\] [M1]
\[= \frac{1600}{6.912 \times 10^{7}} = 2.31 \times 10^{-5}\,\mathrm{atm^{-2}}\] [A1] [B1]
:::

:::eg 1.00 mol of \(\ce{N2O4}\) is allowed to decompose, \(\ce{N2O4(g) <=> 2NO2(g)}\). At equilibrium there are 0.600 mol of \(\ce{N2O4}\) and 0.800 mol of \(\ce{NO2}\), at a total pressure of \(2.00 \times 10^{5}\) Pa. Calculate Kp, with its unit.
Total moles = 0.600 + 0.800 = 1.400. Mole fractions: \(\ce{N2O4}\) 0.600/1.400 = 0.4286; \(\ce{NO2}\) 0.800/1.400 = 0.5714. [M1]

Partial pressures: \(p(\ce{N2O4}) = 0.4286 \times 2.00 \times 10^{5} = 8.571 \times 10^{4}\) Pa; \(p(\ce{NO2}) = 0.5714 \times 2.00 \times 10^{5} = 1.143 \times 10^{5}\) Pa. [M1]

\[K_p = \frac{p(\ce{NO2})^2}{p(\ce{N2O4})} = \frac{(1.143 \times 10^{5})^2}{8.571 \times 10^{4}} = 1.52 \times 10^{5}\,\mathrm{Pa}\] [A1] [B1]
:::

:::eg 2.00 mol of phosphorus(V) chloride is heated in a sealed vessel and 25.0% of it decomposes: \(\ce{PCl5(g) <=> PCl3(g) + Cl2(g)}\). The total pressure at equilibrium is 3.00 atm. Calculate Kp.
\(\ce{PCl5}\) decomposed = 25.0% of 2.00 = 0.500 mol, giving 0.500 mol each of \(\ce{PCl3}\) and \(\ce{Cl2}\). At equilibrium: \(\ce{PCl5}\) 1.50 mol, \(\ce{PCl3}\) 0.500 mol, \(\ce{Cl2}\) 0.500 mol; total 2.50 mol. [M1]

Mole fractions: 0.600, 0.200, 0.200. Partial pressures: \(p(\ce{PCl5}) = 0.600 \times 3.00 = 1.80\) atm; \(p(\ce{PCl3}) = p(\ce{Cl2}) = 0.200 \times 3.00 = 0.600\) atm. [M1]

\[K_p = \frac{0.600 \times 0.600}{1.80} = 0.200\,\mathrm{atm}\] [A1]
:::

:::warn Use equilibrium amounts, and raise to the powers
Two slips cost the most marks in this topic. One is using the **initial** amounts in the expression instead of the equilibrium amounts. The other is forgetting that coefficients are **powers** (writing \([\ce{NH3}]\) instead of \([\ce{NH3}]^2\)). Also, never put a solid in Kc or Kp, and always state the unit or say there is none.
:::

:::eg Spot the error: at equilibrium in a 2.00 dm³ vessel there are 0.400 mol of \(\ce{N2}\), 1.20 mol of \(\ce{H2}\) and 0.400 mol of \(\ce{NH3}\). Calculate \(K_c\) for \(\ce{N2 + 3H2 <=> 2NH3}\), with its unit. [4 marks]
A student wrote this answer.

Line 1: \(K_c = \dfrac{[\ce{NH3}]}{[\ce{N2}][\ce{H2}]}\)
Line 2: \([\ce{N2}] = 0.200\), \([\ce{H2}] = 0.600\), \([\ce{NH3}] = 0.200\) mol dm⁻³
Line 3: \(K_c = 0.200 / (0.200 \times 0.600) = 1.67\) mol⁻¹ dm³

Line 2 is correct: the concentrations are the moles divided by 2.00 dm³ [M1]. **Line 1 is wrong: the coefficients must be powers, so the expression is \([\ce{NH3}]^2 / ([\ce{N2}][\ce{H2}]^3)\) [B0].** Line 3 uses the wrong expression, so the value and unit are wrong [A0] [B0].

The student scores 1 out of 4. Correct working: \(K_c = (0.200)^2 / (0.200 \times 0.600^3) = 0.0400 / 0.0432 = 0.926\) mol⁻² dm⁶. [B1] [A1] [B1] (for expression, value and unit)
:::

## What changes K, and what does not

The value of an equilibrium constant is fixed at a given temperature. This is why we can use one measured value to predict the result of many experiments.

:::key What changes the value of K
- **Only a change of temperature changes the value of K.**
- Changing the concentration of a species, the pressure or the volume changes the **position** of equilibrium, but the system settles at a new set of concentrations that give **the same K**.
- A catalyst changes neither the position nor K: it only shortens the time to reach equilibrium.
:::

Why does concentration not change K? Suppose you add extra ethanol to the esterification mixture. At that instant the ratio of concentrations in the expression is smaller than K, because the ethanol is in the denominator. The system is no longer at equilibrium, so the forward reaction runs faster than the reverse reaction until the ratio has climbed back to exactly the same K, at a new equilibrium with more ester.

Temperature is different because it changes the **rate constants** of the forward and reverse reactions by different amounts (the endothermic direction responds more). Equilibrium is reached when these rates are equal, and a different temperature means different concentrations at that point.

:::key Temperature and K
- Forward reaction **exothermic** (ΔH negative): increasing T **decreases** K, so the position moves to the left.
- Forward reaction **endothermic** (ΔH positive): increasing T **increases** K, so the position moves to the right.
:::

:::eg The reaction \(\ce{2NO2(g) <=> N2O4(g)}\) is exothermic. State and explain the effect of an increase in temperature on (a) the position of equilibrium, (b) the value of Kc. [3 marks]
(a) The forward reaction is exothermic, so raising the temperature moves the position in the endothermic direction, to the left, absorbing the added heat. [B1]

(b) The position moves to the left, so the concentration of \(\ce{N2O4}\) (in the numerator) falls and the concentrations of \(\ce{NO2}\) (in the denominator) rise. [B1]

So the value of \(K_c = [\ce{N2O4}]/[\ce{NO2}]^2\) decreases. [B1]
:::

:::eg Explain why a catalyst does not change the value of Kc. [2 marks]
A catalyst provides an alternative pathway with a lower activation energy for **both** the forward and the reverse reaction, by the same amount. [B1]

So both rates increase by the same factor and equilibrium is reached sooner, but the equilibrium concentrations (and therefore the ratio in Kc) are unchanged. [B1]
:::

## Equilibria in industry: the Haber and Contact processes

Industrial chemists want the highest yield at the lowest cost and in the shortest time. These aims often pull in opposite directions, and the result is a **compromise**.

### The Haber process

\[\ce{N2(g) + 3H2(g) <=> 2NH3(g)} \qquad \Delta H \text{ is negative}\]

Nitrogen comes from the air and hydrogen from natural gas and steam. Both Le Chatelier and rate arguments apply:

| Condition | Effect on yield | Effect on rate | What is used |
|---|---|---|---|
| high pressure | increases it (4 mol gas → 2 mol) | faster | about 200 atm (20 MPa): very high pressures need stronger vessels and more energy, which cost more |
| low temperature | increases it (forward reaction is exothermic) | too slow | about 400–450 °C: a compromise between yield and rate |
| iron catalyst | no change | much faster at the lower temperature | iron |

:::html
<figure class="fig"><svg viewBox="0 30 610 160" role="img" aria-label="Flow diagram of the Haber process: nitrogen and hydrogen are compressed to 200 atmospheres, pass over an iron catalyst at 450 degrees Celsius, then are cooled so that ammonia liquefies and is removed; unreacted nitrogen and hydrogen return to the compressor"><rect class="fm s-acc" x="110" y="42" width="104" height="62" rx="8"/><text class="tl tc" x="162.0" y="69.0">compressor</text><text class="tl tc" x="162.0" y="85.0">200 atm</text><rect class="fm s-acc" x="254" y="42" width="150" height="62" rx="8"/><text class="tl tc" x="329.0" y="61.0">reactor</text><text class="tl tc" x="329.0" y="77.0">iron catalyst</text><text class="tl tc" x="329.0" y="93.0">450 °C</text><rect class="fm s-acc" x="440" y="42" width="104" height="62" rx="8"/><text class="tl tc" x="492.0" y="69.0">cooler</text><text class="tl tc" x="492.0" y="85.0">NH₃ liquefies</text><text class="tl" x="10" y="58">N₂ + H₂</text><path class="ln" d="M66 73H106" marker-end="url(#ah)"/><path class="ln" d="M216 73H250" marker-end="url(#ah)"/><path class="ln" d="M406 73H436" marker-end="url(#ah)"/><path class="ln" d="M546 73H588" marker-end="url(#ah)"/><text class="tl tc" x="567" y="58">NH₃(l)</text><path class="ln" d="M492 106V176H162V110" marker-end="url(#ah)"/><text class="tl tc" x="327" y="168">unreacted N₂ and H₂ recycled</text></svg><figcaption>The Haber process (schematic). Ammonia is removed as a liquid and the unreacted gases go round again, so the reaction does not need to reach a high yield in a single pass.</figcaption></figure>
:::

At these conditions only part of the nitrogen and hydrogen is converted each time the gases pass through the reactor. The mixture is cooled, the ammonia liquefies and is removed, and the **unreacted nitrogen and hydrogen are recycled**. Removing ammonia also moves the position of equilibrium to the right, and recycling means that no reactant is wasted.

:::plot A sketch (not to scale) of the percentage of ammonia in the equilibrium mixture against temperature, at two pressures. The yield falls as the temperature rises, and is higher at the higher pressure.
--f "95/(1+exp(1.0*(x-6)))+0*sqrt(9-x)" --f "60/(1+exp(1.0*(x-4)))+0*sqrt(9-x)" --label "high pressure" --label "low pressure" --x 0 12 --y 0 130 --xlabel "temperature" --ylabel "% ammonia at equilibrium" --noticks --legend tr
:::

### The Contact process

\[\ce{2SO2(g) + O2(g) <=> 2SO3(g)} \qquad \Delta H \text{ is negative}\]

This is the key step in making sulfuric acid. As in the Haber process, the forward reaction is exothermic and 3 mol of gas become 2 mol, so low temperature and high pressure both favour the product.

| Condition | What is used | Why |
|---|---|---|
| catalyst | vanadium(V) oxide, \(\ce{V2O5}\) | speeds up the reaction without changing the yield |
| temperature | about 400–450 °C | a compromise: high enough for a fast rate with the catalyst, low enough for a good yield |
| pressure | about 1–2 atm | the yield at this pressure is already high, so the extra cost of high pressure is not worth it |

The sulfur trioxide is dissolved in concentrated sulfuric acid, not in water, because adding it directly to water produces a mist of acid that is hard to condense.

:::note Why do the two processes use different pressures?
Both reactions have fewer moles of gas on the right, so high pressure helps both. In the Haber process the yield at moderate pressure is low, so the cost of using 200 atm is repaid by a much higher yield. In the Contact process the yield is already high at about 1–2 atm, so extra pressure would add cost for very little gain.
:::

:::eg (Exam style) Explain why the Haber process is operated at about 450 °C rather than at a lower temperature, and why an iron catalyst is used. [4 marks]
The forward reaction is exothermic, so a lower temperature would move the position to the right and increase the equilibrium yield of ammonia. [B1]

But at a lower temperature the rate of reaction would be too slow to be economic. [B1]

450 °C is therefore a compromise between a reasonable yield and a fast enough rate. [B1]

The iron catalyst increases the rate of both forward and reverse reactions, so equilibrium is reached much more quickly at this temperature, without changing the equilibrium yield. [B1]
:::

## Putting it together

Equilibrium questions combine the pieces above. A reliable order is: write the equation; write the expression; draw an ICE table with the quantity you were given; convert to concentrations or partial pressures; substitute; state the unit.

:::eg (Exam style) 1.00 mol of nitrogen and 3.00 mol of hydrogen are sealed in a 2.00 dm³ vessel with an iron catalyst. At equilibrium the vessel contains 0.600 mol of ammonia. Calculate Kc for \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\), with its unit. [5 marks]
Expression: \(K_c = \dfrac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}\) [B1]

ICE table in moles. 0.600 mol of \(\ce{NH3}\) uses half as many moles of \(\ce{N2}\) and one and a half times as many of \(\ce{H2}\) (ratio 1 : 3 : 2):

| | \(\ce{N2}\) | \(\ce{H2}\) | \(\ce{NH3}\) |
|---|---|---|---|
| initial / mol | 1.00 | 3.00 | 0 |
| change / mol | −0.300 | −0.900 | +0.600 |
| equilibrium / mol | 0.700 | 2.10 | 0.600 |

[M1]

Concentrations (divide by 2.00 dm³): \([\ce{N2}] = 0.350\), \([\ce{H2}] = 1.05\), \([\ce{NH3}] = 0.300\) mol dm⁻³. [M1]

\[K_c = \frac{(0.300)^2}{0.350 \times (1.05)^3} = 0.222\] [A1]

The unit is mol⁻² dm⁶. [B1]
:::

:::try Start easy, finish at exam standard
Q: Write the Kc expression for \(\ce{2NO(g) + O2(g) <=> 2NO2(g)}\), and give its unit.
A: \(K_c = [\ce{NO2}]^2 / ([\ce{NO}]^2 [\ce{O2}])\). The unit is \((\mathrm{mol\,dm^{-3}})^{2-3} = \) mol⁻¹ dm³.
Q: Write the Kp expression for \(\ce{CaCO3(s) <=> CaO(s) + CO2(g)}\).
A: \(K_p = p(\ce{CO2})\); the solids are left out.
Q: A reaction mixture contains 0.50 mol of A, 1.50 mol of B and 2.00 mol of C, all gases. What is the mole fraction of each, and the partial pressure of C at a total pressure of 5.00 atm?
A: Total = 4.00 mol; \(x_{\mathrm{A}} = 0.125\), \(x_{\mathrm{B}} = 0.375\), \(x_{\mathrm{C}} = 0.500\). \(p_{\mathrm{C}} = 0.500 \times 5.00 = 2.50\) atm.
Q: The reaction \(\ce{H2(g) + I2(g) <=> 2HI(g)}\) is at equilibrium. State the effect on the position of equilibrium of doubling the pressure by compressing the vessel.
A: No effect on the position: there are 2 mol of gas on each side, so the system cannot reduce the pressure by shifting.
Q: For \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\), ΔH negative, state the effect on the position of lowering the temperature, and the effect on Kc.
A: The position moves to the right, in the exothermic direction, releasing heat. Kc increases.
Q: The equilibrium \(\ce{PCl5(g) <=> PCl3(g) + Cl2(g)}\) is endothermic in the forward direction. State the effect on the amount of chlorine of (a) increasing the temperature, (b) adding a catalyst.
A: (a) The position moves in the endothermic (forward) direction, so more chlorine forms. (b) No effect on the equilibrium amount: the catalyst only gets there sooner.
Q: For \(\ce{2NO2(g) <=> N2O4(g)}\), \(K_c = 0.250\) mol⁻¹ dm³ at a certain temperature. What is Kc for \(\ce{N2O4(g) <=> 2NO2(g)}\) at the same temperature?
A: The reaction is reversed, so \(K_c = 1/0.250 = 4.00\) mol dm⁻³.
Q: At equilibrium a 1.00 dm³ vessel holds 0.100 mol of \(\ce{H2}\), 0.100 mol of \(\ce{I2}\) and 0.500 mol of HI. Calculate Kc for \(\ce{H2 + I2 <=> 2HI}\).
A: \(K_c = (0.500)^2 / (0.100 \times 0.100) = 25.0\) (no unit).
Q: In the equilibrium \(\ce{A(g) + B(g) <=> 2C(g)}\) the partial pressures at equilibrium are \(p_{\mathrm{A}} = 2.0\) atm, \(p_{\mathrm{B}} = 2.0\) atm and \(p_{\mathrm{C}} = 4.0\) atm. Calculate Kp.
A: \(K_p = (4.0)^2 / (2.0 \times 2.0) = 4.0\). No unit, because \(\Delta n = 0\).
Q: Why is the Contact process operated at 1–2 atm and not at a much higher pressure?
A: The yield is already high at this pressure, so the extra cost of compressing and containing the gases at high pressure would not be repaid by a significant gain in yield.
Q: Ammonia is removed from the reactor as a liquid in the Haber process. How does this help?
A: Removing ammonia reduces its concentration, so the position moves to the right, making more ammonia. The unreacted nitrogen and hydrogen are recycled.
Q: Explain why increasing the concentration of one reactant does not change Kc.
A: The system moves to a new equilibrium at which the ratio of concentrations in the expression is the same value again. Only temperature changes K.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State what is meant by dynamic equilibrium.
A: The rate of the forward reaction equals the rate of the reverse reaction [B1], so the concentrations of reactants and products stay constant (while both reactions continue). [B1]
Q: [3 marks] ★ (a) Write the expression for Kc for \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\) and give its unit. (b) Write the expression for Kp for \(\ce{CaCO3(s) <=> CaO(s) + CO2(g)}\).
A: (a) \(K_c = [\ce{NH3}]^2 / ([\ce{N2}][\ce{H2}]^3)\) [B1], unit mol⁻² dm⁶ [B1]
(b) \(K_p = p(\ce{CO2})\) [B1]
Q: [4 marks] ★★ The Contact process is \(\ce{2SO2(g) + O2(g) <=> 2SO3(g)}\), and the forward reaction is exothermic. State and explain the effect of (a) increasing the pressure and (b) increasing the temperature on the position of equilibrium and on the value of Kc.
A: (a) The position moves to the right, because there are fewer moles of gas on the right (2 against 3), minimising the increase in pressure. [B1] Kc is unchanged. [B1]
(b) The position moves to the left, in the endothermic (reverse) direction, absorbing heat. [B1] Kc decreases. [B1]
Q: [4 marks] ★★ At equilibrium a mixture of 0.200 mol \(\ce{H2}\), 0.300 mol \(\ce{I2}\) and 1.20 mol HI is in a sealed vessel, \(\ce{H2(g) + I2(g) <=> 2HI(g)}\). Calculate Kc.
H: Does the volume of the vessel matter for this reaction?
A: \(K_c = \dfrac{[\ce{HI}]^2}{[\ce{H2}][\ce{I2}]}\) [B1]
There are 2 mol of gas on each side, so the volume cancels and moles can be used directly. [B1]
\(K_c = (1.20)^2 / (0.200 \times 0.300) = 1.44 / 0.0600 = 24.0\) [A1]
No unit. [B1]
Q: [5 marks] ★★ 2.00 mol of \(\ce{PCl5}\) is placed in a 4.00 dm³ vessel and heated: \(\ce{PCl5(g) <=> PCl3(g) + Cl2(g)}\). At equilibrium 0.500 mol of chlorine is present. Calculate Kc, with its unit.
H: Draw an ICE table. How much PCl₃ forms for each mole of Cl₂?
A: \(K_c = [\ce{PCl3}][\ce{Cl2}]/[\ce{PCl5}]\) [B1]
At equilibrium: \(\ce{PCl5}\) = 2.00 − 0.500 = 1.50 mol; \(\ce{PCl3}\) = 0.500 mol; \(\ce{Cl2}\) = 0.500 mol. [M1]
Concentrations: 0.375, 0.125 and 0.125 mol dm⁻³. [M1]
\(K_c = (0.125 \times 0.125) / 0.375 = 0.0417\) [A1]
Unit: mol dm⁻³. [B1]
Q: [5 marks] ★★ A mixture at equilibrium contains 2.00 mol of \(\ce{N2}\), 5.00 mol of \(\ce{H2}\) and 3.00 mol of \(\ce{NH3}\) at a total pressure of 100 atm. Calculate Kp for \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\), with its unit.
H: Find the mole fractions first, then the partial pressures.
A: Total = 10.0 mol; mole fractions 0.200, 0.500, 0.300. [B1]
Partial pressures: 20.0, 50.0 and 30.0 atm. [M1]
\(K_p = p(\ce{NH3})^2 / (p(\ce{N2})\,p(\ce{H2})^3)\) [B1]
\(K_p = (30.0)^2 / (20.0 \times 50.0^3) = 900 / 2.50 \times 10^{6}\) [M1]
\(= 3.60 \times 10^{-4}\) atm⁻² [A1]
Q: [6 marks] ★★★ In the Haber process, \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\) (ΔH negative), the conditions are an iron catalyst, about 450 °C and about 200 atm. (a) Explain why a lower temperature than 450 °C is not used. (b) Explain why a much higher pressure than 200 atm is not used. (c) Explain how the yield is increased by the removal of ammonia and the recycling of the reactants. (d) State the effect of the catalyst on the equilibrium yield.
A: (a) A lower temperature would give a higher equilibrium yield but the rate would be too slow. [B1] 450 °C is a compromise. [B1]
(b) Higher pressure raises the yield but needs stronger, more expensive vessels and more energy for compression, so the extra cost is not justified. [B1]
(c) Removing ammonia moves the position to the right, making more ammonia. [B1] Unreacted nitrogen and hydrogen are returned to the reactor, so none is wasted. [B1]
(d) The catalyst has no effect on the equilibrium yield, but it increases the rate so equilibrium is reached faster. [B1]
Q: [6 marks] ★★★ The esterification \(\ce{CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O}\) has \(K_c = 4.00\) at a certain temperature. 1.00 mol of ethanoic acid is mixed with 1.00 mol of ethanol. (a) Write the expression for Kc. (b) Calculate the amount of ethyl ethanoate at equilibrium. (c) Calculate the mass of ethyl ethanoate formed, given \(M_r = 88.0\).
H: Let \(x\) mol of ester form, and take the square root of both sides.
A: (a) \(K_c = \dfrac{[\ce{CH3COOC2H5}][\ce{H2O}]}{[\ce{CH3COOH}][\ce{C2H5OH}]}\) [B1]
(b) At equilibrium: ester = \(x\), water = \(x\), acid = ethanol = \(1.00 - x\). The volume cancels. [M1]
\(K_c = x^2/(1.00 - x)^2 = 4.00\), so \(x/(1.00 - x) = 2.00\) [M1]
\(x = 0.667\) mol [A1]
(c) Mass \(= 0.667 \times 88.0 = 58.7\) g [M1] [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ \(\ce{N2O4(g) <=> 2NO2(g)}\). 1.00 mol of \(\ce{N2O4}\) is heated at a total pressure of 2.00 atm. At equilibrium 20.0% of it has dissociated. (a) Calculate Kp. (b) The total pressure is doubled to 4.00 atm at the same temperature. Calculate the new fraction dissociated, and show that your answer agrees with Le Chatelier's principle.
H: If a fraction \(\alpha\) dissociates, the equilibrium amounts are \(1 - \alpha\) and \(2\alpha\), with a total of \(1 + \alpha\). Write the partial pressures in terms of \(\alpha\) and the total pressure \(p\).
A: (a) Equilibrium: \(\ce{N2O4}\) 0.800 mol, \(\ce{NO2}\) 0.400 mol, total 1.200 mol. Mole fractions 0.6667 and 0.3333. [M1]
Partial pressures: \(p(\ce{N2O4}) = 1.333\) atm; \(p(\ce{NO2}) = 0.6667\) atm. [M1]
\(K_p = (0.6667)^2 / 1.333 = 0.333\) atm [A1]
(b) In general \(K_p = \dfrac{4\alpha^2 p}{1 - \alpha^2}\). With \(K_p = 0.3333\) and \(p = 4.00\): \(16\alpha^2 = 0.3333(1 - \alpha^2)\), so \(\alpha^2 = 0.3333/16.333 = 0.02041\) and \(\alpha = 0.143\). [M1] [A1]
The fraction dissociated falls from 0.200 to 0.143: increasing the pressure moves the position towards the side with fewer moles of gas (\(\ce{N2O4}\)), as Le Chatelier's principle predicts. [B1]
Q: [5 marks] ★★★ Methanol is made from carbon monoxide and hydrogen: \(\ce{CO(g) + 2H2(g) <=> CH3OH(g)}\), ΔH negative. At equilibrium in a 1.00 dm³ vessel at one temperature, the amounts are 0.0500 mol of CO, 0.100 mol of \(\ce{H2}\) and 0.0150 mol of \(\ce{CH3OH}\). (a) Write the expression for Kc and calculate its value with its unit. (b) Suggest, with reasons, the effect of a high pressure and of a high temperature on the equilibrium yield of methanol.
H: Count the moles of gas on each side.
A: (a) \(K_c = [\ce{CH3OH}] / ([\ce{CO}][\ce{H2}]^2)\) [B1]
\(= 0.0150 / (0.0500 \times 0.100^2) = 30.0\) mol⁻² dm⁶ [M1] [A1]
(b) High pressure increases the yield: 3 mol of gas become 1 mol. [B1]
High temperature decreases the yield, because the forward reaction is exothermic. [B1]
:::

:::quiz
? For \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\), which is the correct Kc expression?
- \(\dfrac{[\ce{N2}][\ce{H2}]}{[\ce{NH3}]}\)
- \(\dfrac{[\ce{NH3}]}{[\ce{N2}][\ce{H2}]}\)
+ \(\dfrac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3}\)
- \(\dfrac{2[\ce{NH3}]}{[\ce{N2}] + 3[\ce{H2}]}\)
> Products go on top, reactants on the bottom, and each concentration is raised to the power of its coefficient: it is not multiplied by it, and concentrations are multiplied, not added.
? An equilibrium has the forward reaction exothermic. What happens to the position of equilibrium and to Kc when the temperature is raised?
- The position moves right and Kc increases.
- The position moves right and Kc is unchanged.
+ The position moves left and Kc decreases.
- The position moves left and Kc is unchanged.
> Raising the temperature favours the endothermic (reverse) direction, so the position moves left. This is the one change that alters K, and because the products are decreasing, K decreases.
? Which change alters the value of Kc for a reaction?
- adding a catalyst
- increasing the pressure
- adding more reactant
+ changing the temperature
> Only temperature changes K. The other three change either the rate or the position, but the system settles at concentrations that give the same Kc.
? In a closed vessel, the reaction \(\ce{A <=> B}\) is at equilibrium. Which statement is correct?
- The concentrations of A and B are equal.
- Both reactions have stopped.
+ The forward and reverse reactions continue at equal rates.
- The forward reaction is faster than the reverse reaction.
> "Dynamic" means that the reactions carry on. The concentrations are constant, not equal.
? 1.00 mol of \(\ce{N2O4}\) in a 2.00 dm³ vessel decomposes to give an equilibrium mixture containing 0.600 mol of \(\ce{N2O4}\) and 0.800 mol of \(\ce{NO2}\). What is Kc for \(\ce{N2O4 <=> 2NO2}\)?
- 1.07 mol dm⁻³
- 2.13 mol dm⁻³
+ 0.533 mol dm⁻³
- 0.267 mol dm⁻³
> The concentrations are 0.300 and 0.400 mol dm⁻³, so \(K_c = 0.400^2/0.300 = 0.533\). Using moles instead of concentrations gives 1.07, because for this reaction the volume does not cancel.
? Why is the Contact process run at only 1–2 atm?
- Because high pressure would move the position to the left.
- Because the reaction is endothermic.
+ Because the yield is already high, so extra pressure is not worth the cost.
- Because a catalyst makes pressure unnecessary.
> There are fewer moles of gas on the right, so high pressure would help, but the yield at 1–2 atm is already high and compressing the gases costs money. A catalyst does not remove the effect of pressure on the position.
:::

:::checklist What you can now do
- [ ] I can define reversible reaction, dynamic equilibrium and closed system.
- [ ] I can state Le Chatelier's principle and use it to predict the effect of changing concentration, pressure, temperature or adding a catalyst.
- [ ] I can write Kc expressions, including heterogeneous equilibria, and work out their units.
- [ ] I can define mole fraction and partial pressure and calculate them for a gas mixture.
- [ ] I can write Kp expressions and work out their units.
- [ ] I can calculate Kc and Kp from equilibrium amounts or from initial amounts and one equilibrium amount.
- [ ] I can calculate an equilibrium amount from a given Kc (no quadratics).
- [ ] I can state that only temperature changes the value of K, and that a catalyst changes the rate but not the position or K.
- [ ] I can explain the conditions used in the Haber and Contact processes in terms of yield, rate and cost.
:::

:::recap
- Dynamic equilibrium: rates of forward and reverse reactions are equal, concentrations are constant, and the system is closed.
- Le Chatelier: if a change is made to a system at dynamic equilibrium, the position of equilibrium moves to minimise this change.
- More reactant or less product: position moves right. More gas moles on one side: higher pressure favours the side with fewer moles. Higher T favours the endothermic direction. A catalyst changes only the rate.
- \(K_c = [\mathrm{C}]^c[\mathrm{D}]^d / ([\mathrm{A}]^a[\mathrm{B}]^b)\), with equilibrium concentrations, coefficients as powers, solids left out. Its unit is \((\mathrm{mol\,dm^{-3}})^{\Delta n}\).
- Mole fraction \(x = n/n_{\mathrm{total}}\); partial pressure \(p = x \times p_{\mathrm{total}}\). Kp has the same form as Kc, in partial pressures.
- Only temperature changes K. Exothermic forward reaction: K falls as T rises. A catalyst does not change K or the position.
- ICE tables: initial, change, equilibrium. Convert moles to concentrations unless the volume cancels.
- Haber: iron catalyst, about 400–450 °C, about 200 atm (20 MPa), ΔH negative, ammonia removed as a liquid, nitrogen and hydrogen recycled. Contact: \(\ce{V2O5}\), about 400–450 °C, about 1–2 atm, because the yield is already high.
:::

:::links
- read: [Le Chatelier's principle](https://www.chemguide.co.uk/physical/equilibria/lechatelier.html) · Chemguide · concentration, pressure, temperature and catalysts, with the reasoning for each
- read: [Equilibrium constants, Kc](https://www.chemguide.co.uk/physical/equilibria/kc.html) · Chemguide · writing Kc expressions and calculating with them
- read: [Equilibrium constants, Kp](https://www.chemguide.co.uk/physical/equilibria/kp.html) · Chemguide · mole fraction, partial pressure and Kp calculations
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [Acids and bases](#chem.acids) uses equilibrium to explain why some acids are strong and others weak.
