@chapter chem.kinetics
@title Reaction kinetics
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 5–7 hours
@summary How fast reactions go and what controls their speed. You will learn how to measure a rate and find it from a graph, collision theory, the effect of concentration, pressure and surface area, the Boltzmann distribution and the effect of temperature, and how a catalyst works.

:::why
Some reactions are far too slow to be useful, and others are too fast to be safe. Drug manufacturers must know how long a medicine lasts on the shelf. Food keeps longer in a fridge because the reactions that spoil it slow down. A car's catalytic converter turns poisonous carbon monoxide into carbon dioxide in the second or so that the exhaust gases spend in it. Kinetics is the study of rates, and it explains all of these. This chapter builds one simple picture, particles colliding, and uses it to explain every factor that changes a rate.
:::

**Before you start**, you should know what activation energy and a reaction pathway diagram are from [Chemical energetics](#chem.energetics), what dynamic equilibrium is from [Chemical equilibria](#chem.equilibria), and how to turn gas volumes and masses into moles from [Moles and stoichiometry](#chem.moles).

:::try Warm-up
Q: On a reaction pathway diagram, what does the activation energy measure? (from [Chemical energetics](#chem.energetics))
A: The energy difference between the reactants and the top of the peak (the transition state): the energy barrier that must be crossed.
Q: What is true about the rates of the forward and the reverse reactions in a system at dynamic equilibrium? (from [Chemical equilibria](#chem.equilibria))
A: They are equal, so the concentrations stay constant even though both reactions are still happening.
Q: How many moles of carbon dioxide are in 120 cm³ of the gas at room conditions (molar volume 24.0 dm³ mol⁻¹)? (from [Moles and stoichiometry](#chem.moles))
A: \(n = 0.120 / 24.0 = 0.00500\) mol.
:::

## What is the rate of a reaction?

A reaction starts fast and slows down as the reactants are used up. Think of a car journey that is quick on a motorway and slow in town: you can talk about its speed at one moment, or its average speed over the whole trip. In the same way, the **rate of reaction** tells you how quickly reactants are being used up or products made.

:::def Rate of reaction
The change in concentration of a reactant or a product per unit time.
:::

\[\text{rate} = \frac{\text{change in concentration}}{\text{time taken}}\]

The usual unit is **mol dm⁻³ s⁻¹**. When it is easier to measure the amount of a gas or a mass, the rate can be given as cm³ s⁻¹ or g s⁻¹ instead, as long as you say what was measured. The rate of a reaction is largest at the start, when the reactants are most concentrated, and falls to zero when the reactant that is not in excess has all been used. The rate **at the very start** is the **initial rate**.

## Measuring rates

To follow a reaction you measure some property that changes steadily as it goes, at regular times. Pick the method that suits the reaction.

| What changes | How to follow it | Suitable example |
|---|---|---|
| a gas is made | collect it and read its volume at regular times in a gas syringe | magnesium with hydrochloric acid (hydrogen); hydrogen peroxide with manganese(IV) oxide (oxygen) |
| a gas escapes | stand the flask on a balance (reading to 0.01 g) and note the loss in mass | calcium carbonate with hydrochloric acid (carbon dioxide leaves) |
| a coloured species is used up or made | measure how much light it absorbs with a colorimeter, or compare colours | bromine reacting with an alkene (orange fades); iodine (brown) |
| the amount of an acid or alkali changes | take samples, stop the reaction (quench) and titrate, or follow the pH | ester hydrolysis by acid or alkali |
| a precipitate forms | time how long it takes to hide a mark | sodium thiosulfate with acid (see below) |

:::html
<figure class="fig"><svg viewBox="20 0 520 175" role="img" aria-label="Apparatus for collecting a gas: a conical flask containing metal and acid with a bung and delivery tube leading to a gas syringe whose plunger moves out as the gas collects"><path class="ln" d="M90 60V100L55 160H145L110 100V60"/><path class="fa" d="M65.0 142H135.0L145 160H55Z"/><path class="fm2" d="M86 48H114L112 64H88Z"/><path class="ln thick" d="M100 52V26H262"/><path class="ln" d="M262 10H452M262 42H452M262 10V42"/><path class="fa2" d="M264 12H330V40H264Z"/><path class="ln thick" d="M330 12V40"/><path class="ln thick" d="M330 26H500"/><path class="ln thick" d="M500 14V38"/><path class="ln thin" d="M280 10V16"/><path class="ln thin" d="M300 10V16"/><path class="ln thin" d="M320 10V16"/><path class="ln thin" d="M340 10V16"/><path class="ln thin" d="M360 10V16"/><path class="ln thin" d="M380 10V16"/><path class="ln thin" d="M400 10V16"/><path class="ln thin" d="M420 10V16"/><path class="ln thin" d="M440 10V16"/><text class="tl tc" x="300" y="70">gas syringe</text><path class="ln-m thin" d="M300 56V45"/><text class="tl" x="160" y="100">delivery tube</text><path class="ln-m thin" d="M158 96L112 40"/><path class="ln-m thin" d="M118 152L172 152"/><text class="tl" x="178" y="156">metal and acid</text><text class="tl" x="500" y="62" text-anchor="end">plunger moves out as</text><text class="tl" x="500" y="79" text-anchor="end">gas collects</text></svg><figcaption>Measuring the rate of a reaction that gives off a gas. The syringe reading is taken at regular times, and the volume is plotted against time. The bung must be pushed in firmly or gas escapes.</figcaption></figure>
:::

### A clock reaction: the cross experiment

Sodium thiosulfate reacts with an acid to give a pale yellow precipitate of sulfur:

\[\ce{S2O3^2-(aq) + 2H+(aq) -> S(s) + SO2(g) + H2O(l)}\]

The flask is stood on a piece of paper with a cross drawn on it, and the solution is viewed from above. The sulfur slowly makes the liquid cloudy, and the time for the cross to disappear is noted. That time is the same amount of reaction (the same amount of sulfur) every time, so the **rate is proportional to 1/time**.

:::lab Thiosulfate and acid: rate against concentration
Measure 50 cm³ of thiosulfate solution (made up from a stock solution and water in a measuring cylinder, so that the total volume stays 50 cm³ each time) into a conical flask on the cross. Add 5.0 cm³ of dilute hydrochloric acid, start the clock and swirl once. Stop the clock when the cross can no longer be seen. Repeat with different concentrations of thiosulfate, keeping the temperature and the volume of acid the same. The reaction gives off sulfur dioxide, which is toxic and can set off asthma: work in a ventilated room or fume cupboard, keep the volumes small, and wear eye protection.
:::

:::eg (Exam style) A student repeated the cross experiment with 50 cm³ of thiosulfate solution at five concentrations, shown as the volume of stock solution used. The times were 188 s (10 cm³ of stock), 95 s (20 cm³), 62 s (30 cm³), 47 s (40 cm³) and 38 s (50 cm³). Calculate the relative rate (1000/time) for each, and state what the results show.
Rate is proportional to 1/time, so the relative rate is 1000/time. [B1]

| Volume of stock / cm³ | 10 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|
| time / s | 188 | 95 | 62 | 47 | 38 |
| relative rate = 1000/time | 5.32 | 10.5 | 16.1 | 21.3 | 26.3 |

Doubling the volume of stock from 10 to 20 cm³ (so doubling the concentration) roughly doubles the relative rate (5.32 to 10.5), and a graph of relative rate against concentration would be a straight line through the origin. [B1]

So in this reaction the rate is proportional to the concentration of thiosulfate. [B1]
:::

## Finding the rate from a graph

A graph of volume of gas (or mass lost, or concentration) against time is the usual way to turn raw readings into a rate. The shape is a curve, steep at first and then flattening as the reactant is used up.

:::plot Volume of gas against time for a reaction (the volumes of the table below), with the tangent drawn at 40 s. The gradient of the tangent is the rate at that moment.
--f "60*(1-exp(-x/40))" --f "37.93+0.5518*(x-40)+0*sqrt(110-x)" --label "volume of gas" --label "tangent at 40 s" --x 0 130 --y 0 80 --pt "40,37.93,t = 40 s@se" --xlabel "time / s" --ylabel "volume of gas / cm³" --legend tr
:::

There are two ways to get a number from the curve.

- **Average rate** between two times: divide the change in the measured quantity by the time between them. It is the gradient of the straight line joining two points of the curve.
- **Rate at one moment**: draw a **tangent** to the curve at that point. A tangent is a straight line that touches the curve at that point and has the same slope as the curve there. The rate is the gradient of the tangent, from a large right-angled triangle drawn on it (more than half the length of the line). The rate at \(t = 0\) is the **initial rate**.

For a graph of the concentration of a reactant, the curve falls, so the tangent has a negative gradient. The rate is the size of the gradient, written as a positive number: the rate of use of a reactant is \(-\) (gradient).

:::eg (Exam style) The volume of hydrogen made when magnesium reacts with excess hydrochloric acid was measured at 20 s intervals: 0, 24, 38, 47, 52 and 55 cm³ at 0, 20, 40, 60, 80 and 100 s. Calculate the average rate for each 20 s interval and say how the rate changes.
\[\text{average rate} = \frac{\text{change in volume}}{\text{time}}\]
0–20 s: \(24/20 = 1.2\) cm³ s⁻¹. 20–40 s: \((38 - 24)/20 = 0.70\) cm³ s⁻¹. 40–60 s: \((47 - 38)/20 = 0.45\) cm³ s⁻¹. 60–80 s: \((52 - 47)/20 = 0.25\) cm³ s⁻¹. 80–100 s: \((55 - 52)/20 = 0.15\) cm³ s⁻¹. [M1 A1]

The rate decreases throughout. [B1] As the acid is used up its concentration falls, so there are fewer collisions between particles each second. [B1]
:::

:::eg (Exam style) On the plot above, the tangent at 40 s passes through (0, 16) and (100, 71). Find the rate at 40 s. The tangent at t = 0 rises 60 cm³ in 40 s. Find the initial rate and compare it with the rate at 40 s.
The gradient of the tangent at 40 s is \(\dfrac{71 - 16}{100 - 0} = 0.55\) cm³ s⁻¹. [M1 A1]

The tangent at \(t = 0\) has gradient \(\dfrac{60}{40} = 1.5\) cm³ s⁻¹: the initial rate. [M1 A1]

The initial rate is nearly three times the rate at 40 s (1.5/0.55 = 2.7), because the reactant is more concentrated at the start. [B1]
:::

:::warn Reading a graph
Draw the tangent with a ruler, so that it touches the curve at one point without cutting it, and choose two points on the tangent far apart (more than half its length). Use the **tangent's** points, not points on the curve. Write the units of the gradient: volume per time, for example cm³ s⁻¹. For a clock reaction you use 1/time instead, with no units on a relative rate.
:::

## Collision theory

Particles react only if they meet, so reactions start with a collision. But most collisions do not lead to a reaction. Two things must be true for a collision to be **effective**.

:::def Effective collision
A collision between particles that results in a reaction. It needs the colliding particles to have at least the activation energy and to meet in the correct orientation.
:::

:::def Activation energy, Eₐ
The minimum energy that colliding particles must have for a collision to be effective (to result in a reaction).
:::

The energy is needed to break old bonds as new ones begin to form. Particles that collide with less than Eₐ simply bounce apart. The orientation matters because a reaction usually occurs at one part of a molecule: a collision on the wrong side does not reach it. Collisions that are not effective are **non-effective collisions**.

:::html
<figure class="fig"><svg viewBox="10 25 600 130" role="img" aria-label="Three collisions between a molecule X-Y and an atom Z. In the first, Z approaches the Y end slowly, shown by a short arrow, and bounces off. In the second, Z approaches the X end quickly, the wrong end, and bounces off. In the third, Z approaches the Y end quickly and a reaction occurs"><path class="ln-m thin dash" d="M232 30V150"/><path class="ln-m thin dash" d="M432 30V150"/><circle class="fm s-acc" cx="93" cy="70" r="15"/><text class="tl tc" x="93" y="75">X</text><circle class="fm2 s-acc" cx="127" cy="70" r="15"/><text class="tl tc" x="127" y="75">Y</text><circle class="fa s-acc" cx="190" cy="70" r="15"/><text class="tl tc tp" x="190" y="75">Z</text><path class="ln" d="M200 40H178" marker-end="url(#ah)"/><text class="tl tc" x="110" y="120">too slow:</text><text class="tl tc" x="110" y="138">not enough energy</text><circle class="fm s-acc" cx="328" cy="70" r="15"/><text class="tl tc" x="328" y="75">X</text><circle class="fm2 s-acc" cx="362" cy="70" r="15"/><text class="tl tc" x="362" y="75">Y</text><circle class="fa s-acc" cx="265" cy="70" r="15"/><text class="tl tc tp" x="265" y="75">Z</text><path class="ln" d="M255 40H311" marker-end="url(#ah)"/><text class="tl tc" x="345" y="120">wrong end:</text><text class="tl tc" x="345" y="138">wrong orientation</text><circle class="fm s-acc" cx="483" cy="70" r="15"/><text class="tl tc" x="483" y="75">X</text><circle class="fm2 s-acc" cx="517" cy="70" r="15"/><text class="tl tc" x="517" y="75">Y</text><circle class="fa s-acc" cx="580" cy="70" r="15"/><text class="tl tc tp" x="580" y="75">Z</text><path class="ln" d="M590 40H534" marker-end="url(#ah)"/><text class="tl tc" x="500" y="120">fast, right end:</text><text class="tl tc" x="500" y="138">reaction occurs</text></svg><figcaption>Z can only bond to the Y end of the molecule X–Y. A longer arrow means a faster particle. In the first two collisions the particles bounce apart: one is too slow, and one is the wrong way round. In the third both conditions are met.</figcaption></figure>
:::

:::analogy
Think of a golf ball and a hole. The ball must be moving fast enough to get over the lip of the hole (the activation energy), and it must also head for the hole itself, not the rim (the orientation). Most shots miss for one reason or the other. Only a few go in.
:::

So the rate of a reaction depends on how often particles collide **effectively**. That is the **frequency of effective collisions**. A factor speeds up a reaction either by making collisions more frequent, or by making a larger share of them effective. The rest of the chapter goes through each factor with this in mind.

## Concentration and pressure

At a higher concentration there are more particles in the same volume, so they are closer together and collide more often. If the concentration of one reactant is doubled, the number of collisions per second involving that reactant roughly doubles. The proportion of collisions that are effective stays the same, because Eₐ and the temperature are unchanged, so the **frequency of effective collisions rises** and so does the rate.

:::key Concentration and pressure
Increasing the concentration of a reactant in solution, or the pressure of a gas, increases the number of particles in a given volume. They collide more frequently, so the frequency of effective collisions increases and the rate increases. The activation energy is the same.
:::

For gases, pressure plays the part of concentration. Squeezing the same gas into half the volume at the same temperature doubles the number of molecules in each cm³, which doubles the concentration. Pressure has no effect on the rate of a reaction between solids and liquids.

:::eg Explain why the rate of reaction between magnesium and hydrochloric acid decreases as the reaction proceeds, and what a student could do to measure the rate at the very start.
As the reaction proceeds, the \(\ce{H+}\) ions are used up, so the concentration of the acid falls. [B1]

There are fewer \(\ce{H+}\) ions in a given volume, so collisions between \(\ce{H+}\) ions and magnesium atoms at the surface are less frequent, [B1] and so the frequency of effective collisions falls. [B1]

The rate at the very start (initial rate) is the gradient of the tangent to the volume–time curve at \(t = 0\). [B1]
:::

## Surface area

When one reactant is a solid, a reaction can only happen where the solid meets the other reactant: at the surface. A lump has most of its particles buried inside, out of reach. Crushing it to a powder exposes many more particles at the surface.

:::key Surface area
The same mass of a solid with a larger surface area (a powder instead of lumps) has more of its particles exposed, so there are more collisions per second between them and the other reactant, and the rate increases. Eₐ and the energy of the particles are unchanged.
:::

:::eg (Real context) A student reacts 2.0 g of marble chips (calcium carbonate) with excess dilute hydrochloric acid, and then repeats with 2.0 g of powdered marble. Predict how the volume of gas against time graph for the powder differs, and explain.
The powder gives a steeper curve (the initial rate is greater) and reaches its plateau sooner. [B1]

The powder has a larger surface area than the chips, so more calcium carbonate is exposed to the acid. [B1] Collisions between acid particles and calcium carbonate are therefore more frequent. [B1]

The final volume of carbon dioxide is the same, because the amount of marble (2.0 g) is the same. [B1]
:::

## Temperature and the Boltzmann distribution

Reactions go faster when the temperature is raised, but the reason is more subtle than "particles collide more often".

In a gas or a liquid, the particles do not all have the same energy. They constantly exchange energy by colliding, so a few particles have very little, many have a middling amount and a few have a lot. A graph that shows how many particles have each energy is the **Boltzmann distribution** (the Maxwell–Boltzmann distribution).

:::def Boltzmann distribution
The distribution of the energies of the molecules in a sample at a given temperature: it shows the number of molecules with each energy.
:::

:::html
<div class="widget" data-w="chem-boltzmann" data-t1="300" data-t2="310" data-ea="50"></div>
:::

The curve has a characteristic shape. Learn its features, since they are asked in almost every exam answer on this topic.

:::key Features of the Boltzmann distribution
- The curve starts at the **origin**: no molecules have zero energy.
- It rises to a **peak** (the most likely energy) and then falls gradually.
- It **never touches the horizontal axis** at high energy: there is no maximum energy, since a very few molecules can have a very high energy.
- The **area under the curve** is the total number of molecules. It stays the same if the amount of gas and its volume are fixed.
- The activation energy Eₐ is marked on the energy axis. The **area to the right of Eₐ** is the number of molecules with energy of at least Eₐ, the ones that can react on collision.
:::

### Raising the temperature

The molecules at a higher temperature have more energy on average, so the whole curve moves to the right. The peak is lower and shifts to a higher energy, the curve is flatter, and the tail on the right is higher. The area under the two curves is the same because the number of molecules is the same.

:::plot Boltzmann distributions at two temperatures. The activation energy is the same for both, and the area to the right of it, for the curve with the lower temperature, is shaded.
--f "2/sqrt(pi)*sqrt(x)*exp(-x)+0*sqrt(6.6-x)" --f "2/sqrt(pi)/1.5**1.5*sqrt(x)*exp(-x/1.5)+0*sqrt(6.6-x)" --label "lower temperature T₁" --label "higher temperature T₂" --x 0 7.5 --y 0 0.75 --shade "0,3,6.6" --vline 3 --xlabel "energy" --ylabel "number of molecules" --noticks --legend tr
:::

The vertical line is Eₐ. Compare the area to its right under the two curves. At the higher temperature a **much larger share** of the molecules has energy of at least Eₐ, so a much larger share of collisions is effective. There are two effects of a higher temperature:

1. The particles move faster, so they collide more often. This effect is small: for example, a 10 K rise from 300 K increases the number of collisions per second by only about 2%.
2. A larger fraction of the particles has energy of at least Eₐ. This effect is large. For Eₐ = 50 kJ mol⁻¹, a 10 K rise from 300 K to 310 K nearly doubles that fraction (it increases by a factor of about 1.9).

:::key Why temperature has such a large effect
The main reason is that, at a higher temperature, a greater proportion of molecules has energy greater than or equal to Eₐ, so the frequency of effective collisions increases sharply. The extra collision frequency is a minor contribution. Eₐ does not change.
:::

This is why a small rise in temperature often has a large effect. A rise of 10 °C often roughly doubles the rate of a reaction, but this is only an observation for many reactions, not a rule: the size of the effect depends on Eₐ.

:::warn Common mistakes with the Boltzmann curve
Do not draw the curve touching the horizontal axis at high energy, or starting somewhere other than the origin. Do not draw the high-temperature curve with a larger area. Do not move Eₐ when you change the temperature: the activation energy of a reaction is fixed. And do not say that heating "gives the molecules more activation energy" or that "all the molecules now have enough energy".
:::

:::eg Sketch the Boltzmann distribution curves at two temperatures, T₁ and a higher temperature T₂, mark Eₐ, and use the curves to explain why the rate is greater at T₂. [5 marks]
Axes labelled: vertical axis number of molecules, horizontal axis energy. [B1]

Both curves start at the origin and do not touch the horizontal axis at high energy. [B1]

The T₂ curve has a lower peak at higher energy, and the same total area as the T₁ curve. [B1]

A vertical line for Eₐ is drawn to the right of both peaks. [B1]

At T₂ a larger area (a greater proportion of molecules) lies to the right of Eₐ, so more collisions are effective and the rate is higher. [B1]
:::

:::eg (Exam style) Explain why the rate of a reaction is often roughly doubled by a 10 °C rise in temperature, although the number of collisions per second rises by only a few per cent. [3 marks]
At the higher temperature the molecules have more energy and the whole distribution shifts to higher energy. [B1]

A much larger proportion of molecules has energy of at least Eₐ (about 1.9 times more, if Eₐ is 50 kJ mol⁻¹). [B1]

So the frequency of effective collisions rises by much more than the frequency of all collisions. [B1]
:::

:::eg Spot the error: Explain why increasing the temperature increases the rate of a reaction. [3 marks]
A student wrote this answer.

Line 1: At a higher temperature the particles have more kinetic energy and move faster.
Line 2: This lowers the activation energy, so more collisions are effective.
Line 3: So the frequency of effective collisions increases and the rate increases.

Line 1 is correct [B1]. **Line 2 is wrong: temperature does not change Eₐ. What changes is the proportion of molecules with energy of at least Eₐ. The mark is lost [B0].** Line 3 is correct [B1].

Correct line 2: a greater proportion of the molecules have energy greater than or equal to Eₐ. [B1]

The student scores 2 out of 3. Lowering Eₐ is what a catalyst does, and the two effects must not be mixed up.
:::

## Catalysts

A catalyst speeds up a reaction without being used up. Chemists use catalysts everywhere: iron in the Haber process, vanadium(V) oxide in the Contact process, and platinum, palladium and rhodium in a car's catalytic converter.

:::def Catalyst
A substance that increases the rate of a reaction by providing a different reaction pathway (mechanism) with a lower activation energy, and that is not used up in the reaction.
:::

A catalyst does take part: the reactants may stick to its surface or form an intermediate with it. But it is regenerated, so it is there, unchanged in amount, when the reaction is over. The reactants find another route to the same products, and that route has a **lower activation energy**.

:::html
<figure class="fig small"><svg viewBox="0 8 330 232" role="img" aria-label="Reaction pathway diagram for an exothermic reaction with and without a catalyst: the solid curve has a high peak and the dashed curve a lower peak; both go from the same reactants to the same products, so the enthalpy change is the same. The activation energy is marked for each"><path class="ax" d="M20 205V30" marker-end="url(#ahm)"/><path class="ax" d="M20 205H290" marker-end="url(#ahm)"/><text class="tl" x="28" y="24">enthalpy</text><text class="tl" x="290" y="227" text-anchor="end">progress of reaction</text><path class="ln thick" d="M60 118H115"/><path class="ln thick" d="M195 168H245"/><path class="c1 sw2" d="M115 118C137 118 133.0 52 155.0 52C177.0 52 173 168 195 168"/><path class="c1 sw2 dash" d="M115 118C137 118 133.0 86 155.0 86C177.0 86 173 168 195 168"/><text class="tl tc" x="87.5" y="138">reactants</text><text class="tl tc" x="220.0" y="188">products</text><path class="ln-m thin dash" d="M32 52H151.0"/><path class="ln-m thin dash" d="M60 86H151.0"/><path class="ln-m thin dash" d="M32 118H60"/><path class="c2 sw2" d="M38 85.0V55" marker-end="url(#ah)"/><path class="c2 sw2" d="M38 85.0V115" marker-end="url(#ah)"/><path class="c2 sw2" d="M66 102.0V89" marker-end="url(#ah)"/><path class="c2 sw2" d="M66 102.0V115" marker-end="url(#ah)"/><text class="tl" x="45" y="76">Eₐ</text><text class="tl" x="74" y="106.0">Eₐ′</text><path class="ln-m thin dash" d="M115 118H283"/><path class="ln-m thin dash" d="M245 168H283"/><path class="c2 sw2" d="M275 143.0V121" marker-end="url(#ah)"/><path class="c2 sw2" d="M275 143.0V165" marker-end="url(#ah)"/><text class="tl" x="266" y="147.0" text-anchor="end">ΔH</text><path class="c1 sw2" d="M200 40H224"/><text class="tl" x="230" y="44">no catalyst</text><path class="c1 sw2 dash" d="M200 62H224"/><text class="tl" x="230" y="66">with catalyst</text></svg><figcaption>Pathway diagram with and without a catalyst. Eₐ is the activation energy without the catalyst and Eₐ′ the lower activation energy with it. The reactants, the products and ΔH are the same for both routes.</figcaption></figure>
:::

The effect on the Boltzmann distribution is that **the distribution does not change** (the temperature is the same), but the activation energy moves to the left. A larger area now lies to the right of it. A much larger proportion of the molecules has enough energy to react, so the frequency of effective collisions rises.

:::plot The same Boltzmann distribution with two activation energies. The catalyst lowers Eₐ, so the area to the right of the line marked Eₐ (catalyst) is much larger than the area to the right of the line marked Eₐ.
--f "2/sqrt(pi)*sqrt(x)*exp(-x)+0*sqrt(6.6-x)" --x 0 7.5 --y 0 0.6 --vline 3 --vline 1.8 --pt "1.8,0.4,Eₐ (catalyst)@w" --pt "3,0.25,Eₐ@e" --xlabel "energy" --ylabel "number of molecules" --noticks
:::

The numbers are striking. At 300 K, lowering Eₐ from 50 to 30 kJ mol⁻¹ increases the fraction of molecules that can react by a factor of about 2400.

Try the widget below, which draws the pathway diagram. Tick the catalyst box and see what changes (Eₐ) and what does not (ΔH, and the starting and finishing levels).

:::html
<div class="widget" data-w="chem-profile" data-dh="-90" data-ea="120" data-cat="1"></div>
:::

:::key What a catalyst does and does not do
A catalyst provides a different mechanism with a lower Eₐ, so a greater proportion of collisions are effective and the rate increases. It does **not** change ΔH, the products, the position of equilibrium or the amount of product formed. In a reversible reaction it speeds up the forward and reverse reactions equally, so equilibrium is reached sooner but at the same position.
:::

:::warn Catalyst mistakes
Do not write that a catalyst "gives the molecules more energy" (it lowers the barrier instead) or that it "is not involved in the reaction" (it takes part and is regenerated). "A catalyst is not used up" is true but never enough for full marks: always mention the alternative pathway with a lower activation energy.
:::

There are two kinds of catalyst. In a **heterogeneous** catalyst, the catalyst is in a different phase from the reactants (the solid metals in the Haber process and in a catalytic converter). In a **homogeneous** catalyst, it is in the same phase. Both are treated in [Rate equations and catalysis](#chem.rates2); at AS you only need the idea of a lower-Eₐ route.

:::eg (Real context) Car exhaust gases contain carbon monoxide and nitrogen monoxide, which react very slowly: \(\ce{2CO + 2NO -> 2CO2 + N2}\). A catalytic converter contains platinum and rhodium on a honeycomb. Explain how the catalyst makes the reaction fast enough to clear the gases. [4 marks]
The catalyst provides an alternative reaction pathway (mechanism) with a lower activation energy. [B1]

The Boltzmann distribution is unchanged, but Eₐ moves to the left, [B1] so a greater proportion of molecules has energy of at least the new Eₐ. [B1]

The frequency of effective collisions on the metal surface increases, and so the rate increases. [B1]
:::

## Putting the factors together

Every change you can make to a reaction either changes the number of collisions or changes the proportion that are effective.

| Change | Frequency of collisions | Proportion of particles with E ≥ Eₐ | Eₐ itself |
|---|---|---|---|
| higher concentration (or gas pressure) | up | same | same |
| larger surface area of a solid | up | same | same |
| higher temperature | up slightly | up a lot | same |
| catalyst | same | up a lot | **lowered** |

:::exam Explaining a change in rate
Write the chain in three links: (1) what changes (concentration, temperature …); (2) what that does to the particles (more particles in a given volume; a greater proportion with E ≥ Eₐ); (3) the effect on the **frequency of effective collisions** and the rate. For temperature and catalysts the second link must mention Eₐ. Write "rate", not "speed", and "particles with energy ≥ Eₐ", not "particles that are hot".
:::

:::try Start easy, finish at exam standard
Q: Define the rate of a reaction and give a suitable unit.
A: The change in concentration of a reactant or a product per unit time. Unit: mol dm⁻³ s⁻¹.
Q: A gas syringe reading rises from 18 cm³ at 10 s to 42 cm³ at 30 s. Calculate the average rate.
A: \((42 - 18)/(30 - 10) = 24/20 = 1.2\) cm³ s⁻¹.
Q: The concentration of a reactant falls from 0.200 mol dm⁻³ to 0.120 mol dm⁻³ in 100 s. Calculate the average rate of use of the reactant.
A: \(0.080/100 = 8.0 \times 10^{-4}\) mol dm⁻³ s⁻¹.
Q: A tangent to a mass–time graph passes through (10 s, 0.20 g) and (70 s, 0.80 g). What is the rate at the point of contact?
A: \((0.80 - 0.20)/(70 - 10) = 0.60/60 = 0.010\) g s⁻¹.
Q: Explain, in terms of collisions, why increasing the pressure of a gaseous reaction mixture increases the rate.
A: A higher pressure packs more molecules into the same volume (higher concentration), so they collide more often, and the frequency of effective collisions increases.
Q: Why does powdered zinc react faster with acid than a lump of zinc of the same mass?
A: The powder has a larger surface area, so more zinc is exposed to the acid and there are more frequent collisions at the surface.
Q: What is meant by a non-effective collision?
A: A collision between particles that does not result in a reaction: they bounce apart, because they have less than Eₐ or are in the wrong orientation.
Q: In the cross experiment, the time for the cross to disappear is 40 s at 20 °C and 20 s at 30 °C. By what factor does the rate change?
A: Rate is proportional to 1/time, so the rate is \(40/20 = 2\) times greater at 30 °C.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define (a) activation energy, (b) an effective collision.
A: (a) The minimum energy that colliding particles must have for a collision to be effective (to result in a reaction). [B1]
(b) A collision that results in a reaction, because the particles have at least the activation energy and the correct orientation. [B1]
Q: [3 marks] ★ Explain, in terms of collisions, why the rate of a reaction in solution increases when the concentration of a reactant is increased.
A: There are more particles per unit volume. [B1] They collide more frequently. [B1] So the frequency of effective collisions increases, and the rate increases. [B1]
Q: [4 marks] ★★ The concentration of a reactant was measured during a reaction: 0.400 mol dm⁻³ at 0 s, 0.300 at 100 s, 0.220 at 200 s and 0.160 at 300 s. (a) Calculate the average rate over the first 100 s and over the last 100 s. (b) Explain why they differ.
H: Rate = (change in concentration)/(time), as a positive number.
A: (a) First 100 s: \(0.100/100 = 1.00 \times 10^{-3}\) mol dm⁻³ s⁻¹. [B1]
Last 100 s: \(0.060/100 = 6.0 \times 10^{-4}\) mol dm⁻³ s⁻¹. [B1]
(b) The reactant is used up, so its concentration falls. [B1] Collisions are less frequent, so the rate falls. [B1]
Q: [4 marks] ★★ Sketch the Boltzmann distribution for a gas at a temperature T. On the same axes sketch the distribution at a higher temperature. Mark the activation energy and state how the areas to the right of it compare.
A: Axes labelled number of molecules and energy; curve for T starting at the origin and not touching the axis at high energy. [B1]
Higher temperature curve has a lower peak at higher energy and the same total area. [B1]
Eₐ drawn as a vertical line to the right of both peaks. [B1]
The area to the right of Eₐ is greater at the higher temperature. [B1]
Q: [5 marks] ★★ Explain, with the aid of a reaction pathway diagram, how a catalyst increases the rate of a reaction.
H: Your diagram needs two routes between the same reactants and products.
A: Pathway diagram showing reactants and products at the same levels, [B1] a high peak without catalyst and a lower peak with catalyst. [B1]
The catalyst provides an alternative reaction pathway (different mechanism). [B1]
This has a lower activation energy. [B1]
A greater proportion of the molecules has energy of at least the activation energy, so the frequency of effective collisions increases. [B1]
Q: [4 marks] ★★ In a cross experiment, 50 cm³ of thiosulfate solution gave times of 80 s at 0.050 mol dm⁻³ and 40 s at 0.100 mol dm⁻³ (the acid was in excess each time). (a) Calculate the relative rate (1000/time) for each. (b) State the effect of doubling the concentration, and explain.
A: (a) 1000/80 = 12.5 [B1] and 1000/40 = 25. [B1]
(b) Doubling the concentration doubles the rate. [B1] There are twice as many thiosulfate ions in a given volume, so they collide twice as often with the acid, and the frequency of effective collisions doubles. [B1]
Q: [6 marks] ★★★ (#chem.moles) A flask containing excess hydrochloric acid stood on a balance. 2.73 g of calcium carbonate was added. The mass of the flask fell by 0.54 g in the first 30 s, and by 1.20 g in total at the end of the reaction. (a) Show that the total loss in mass fits the amount of calcium carbonate. (b) Calculate the average rate of loss of mass over the first 30 s. (c) Explain why the rate of loss decreases during the reaction.
H: The mass lost is carbon dioxide. Write the equation first.
A: (a) \(\ce{CaCO3 + 2HCl -> CaCl2 + H2O + CO2}\); \(M_r(\ce{CaCO3}) = 100.1\), so \(n = 2.73/100.1 = 0.02727\) mol [B1]
\(n(\ce{CO2}) = 0.02727\) mol, mass \(= 0.02727 \times 44.0 = 1.20\) g [M1] [A1]
(b) \(0.54/30 = 0.018\) g s⁻¹ [B1]
(c) The acid is used up, so its concentration falls, [B1] and collisions between \(\ce{H+}\) ions and calcium carbonate are less frequent. [B1]
Q: [6 marks] ★★★ Ammonia is made by \(\ce{N2(g) + 3H2(g) <=> 2NH3(g)}\) with an iron catalyst. (a) Explain how the iron catalyst affects the rate. (b) State and explain the effect of the catalyst on the position of equilibrium and the yield. (c) The forward reaction is exothermic. Why is a compromise temperature used?
H: Think about what happens to both the forward and the reverse reactions.
A: (a) Iron provides a different pathway with a lower activation energy, [B1] so a greater proportion of collisions are effective and the rate increases. [B1]
(b) The catalyst has no effect on the position of equilibrium or the yield, [B1] because it speeds up the forward and reverse reactions equally. [B1] The equilibrium is reached sooner. [B1]
(c) A low temperature favours a high yield (exothermic) but gives a slow rate; a high temperature gives a fast rate but a low yield, so a compromise is used. [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ A student says: "Heating from 300 K to 310 K doubles the rate because the particles collide twice as often." The number of collisions per second increases by about 2% for this rise, but the fraction of molecules with energy of at least Eₐ increases by about 90% for Eₐ = 50 kJ mol⁻¹. Use the figures to criticise the student's statement.
H: Compare the sizes of the two effects.
A: The student is wrong that collisions become twice as frequent: they rise by only about 2%. [B1]
The rate does roughly double, because the fraction of molecules with E ≥ Eₐ increases by about 90%. [B1]
So the frequency of effective collisions (collision frequency × the fraction with E ≥ Eₐ) is nearly doubled. [B1]
The main reason is the change in the proportion of molecules with enough energy, shown by the Boltzmann distribution, not the collision frequency. [B1]
Q: [5 marks] ★★★ The catalyst in a catalytic converter is spread as a thin layer on a ceramic honeycomb, and it works only when the exhaust is hot. Explain (a) why a honeycomb is used, (b) why a catalyst does not make the reaction work at room temperature.
H: (a) Think surface area. (b) A catalyst lowers Eₐ, but does it reduce it to zero?
A: (a) The honeycomb gives the catalyst a very large surface area in a small volume. [B1] More gas molecules meet the catalyst surface each second, [B1] so the frequency of effective collisions is greater. [B1]
(b) The catalytic route still has an activation energy greater than zero, [B1] so at room temperature too few molecules have enough energy; heating increases the proportion that do. [B1]
:::

:::quiz
? Which is a correct unit for the rate of a reaction?
- mol dm⁻³
+ mol dm⁻³ s⁻¹
- s mol⁻¹ dm³
- kJ mol⁻¹
> Rate = change in concentration ÷ time, so the unit is mol dm⁻³ per second. kJ mol⁻¹ is the unit of enthalpy change or activation energy.
? A tangent to a gas volume–time graph passes through (0 s, 5 cm³) and (50 s, 65 cm³). What is the rate at the point of contact?
- 0.083 cm³ s⁻¹
+ 1.2 cm³ s⁻¹
- 60 cm³ s⁻¹
- 70 cm³ s⁻¹
> Gradient = (65 − 5)/(50 − 0) = 60/50 = 1.2 cm³ s⁻¹. 0.083 is time ÷ volume, upside down.
? What is the activation energy?
- the energy released in a reaction
- the average energy of the molecules
+ the minimum energy colliding particles need for a collision to be effective
- the energy needed to start a flame
> Eₐ is the minimum energy that colliding particles must have to react. The energy released is the enthalpy change.
? Why does doubling the concentration of a reactant in solution increase the rate?
- Eₐ is halved
- the particles have more energy
+ the particles collide more frequently
- more particles have energy above Eₐ
> More particles in each cm³ means more frequent collisions. The proportion of particles with E ≥ Eₐ depends on the temperature, which has not changed.
? What is the main reason that a 10 °C rise in temperature increases the rate of a reaction so much?
- the particles collide twice as often
- the activation energy is lowered
+ a much larger proportion of particles has energy at least equal to Eₐ
- the particles are more concentrated
> The collision rate rises by only a few per cent. The main effect is the larger share of particles in the tail of the Boltzmann distribution beyond Eₐ.
? Which statement about the Boltzmann distribution is correct?
- The curve touches the energy axis at high energy
- The higher-temperature curve has the larger area
+ The area under the curve is the total number of molecules
- The peak moves to lower energy as temperature rises
> The area is the number of molecules, so it is the same at both temperatures. The curve approaches the axis but never touches it, and the peak moves to higher energy with a rise in temperature.
? What does a catalyst do to a reaction?
- It increases ΔH
- It increases the proportion of reactants converted at equilibrium
+ It provides a different pathway with a lower activation energy
- It gives the molecules more energy
> A catalyst lowers Eₐ. ΔH, the equilibrium yield and the energy of the molecules are unchanged.
? 2.0 g of calcium carbonate lumps and 2.0 g of calcium carbonate powder are each added to excess acid. What is the same for both?
- the initial rate
- the time to finish
+ the final volume of gas
- the surface area
> The same mass gives the same amount of carbon dioxide at the end. The powder has a larger surface area, a faster initial rate and finishes sooner.
:::

:::checklist What you can now do
- [ ] I can define rate of reaction, and explain the terms frequency of collisions, effective collision and non-effective collision.
- [ ] I can explain the effect of concentration and pressure on rate in terms of the frequency of effective collisions.
- [ ] I can calculate rates from experimental data, using average rates, the gradient of a tangent, and 1/time for a clock reaction.
- [ ] I can describe how to follow a reaction by gas volume, mass loss or colour change.
- [ ] I can define activation energy as the minimum energy colliding particles need for an effective collision.
- [ ] I can sketch the Boltzmann distribution, mark Eₐ, and sketch the curve at a higher temperature.
- [ ] I can explain the effect of temperature using the Boltzmann distribution and the frequency of effective collisions.
- [ ] I can explain how a catalyst works, with a pathway diagram and a Boltzmann distribution.
:::

:::recap
- Rate = change in concentration ÷ time (mol dm⁻³ s⁻¹). It is largest at the start and falls as reactants are used up. Initial rate = gradient at t = 0.
- Rate from a graph: average rate = change ÷ time; rate at a point = gradient of a tangent; clock reactions: rate ∝ 1/time.
- Reaction needs effective collisions: energy ≥ Eₐ and the correct orientation. Eₐ = the minimum energy colliding particles need for an effective collision.
- Higher concentration, pressure (gases) or surface area (solids) means more frequent collisions, so more frequent effective collisions. Eₐ and the proportion with E ≥ Eₐ are unchanged.
- Boltzmann distribution: starts at the origin, has a peak, never touches the axis, area = number of molecules. At a higher T the peak is lower and further right; the area is the same.
- Temperature: a larger proportion of molecules with E ≥ Eₐ is the main reason; the small rise in collision frequency is minor. Eₐ is unchanged.
- Catalyst: a different pathway with a lower Eₐ, so more molecules have E ≥ Eₐ. Not used up. No change to ΔH, products or the position of equilibrium; reaches equilibrium sooner.
:::

:::links
- read: [An introduction to collision theory](https://www.chemguide.co.uk/physical/basicrates/introduction.html) · Chemguide · activation energy and collisions, step by step
- read: [The effect of temperature on rates of reaction](https://www.chemguide.co.uk/physical/basicrates/temperature.html) · Chemguide · the Maxwell–Boltzmann distribution and why a small rise in temperature has a big effect
- read: [The effect of catalysts on rates of reaction](https://www.chemguide.co.uk/physical/basicrates/catalyst.html) · Chemguide · lower activation energy shown on a distribution and an energy profile
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 16 October 2026.
:::

Next: [Periodicity: Period 3](#chem.periodicity) turns to the elements of Period 3 and how their properties change across the period.
