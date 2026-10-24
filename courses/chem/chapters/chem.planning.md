@chapter chem.planning
@title Planning, analysis and evaluation
@level a2
@paper CAIE 9701 Paper 5
@time 6–8 hours
@summary Paper 5 has no laboratory: you plan an experiment on paper, process a table of data, draw a conclusion and criticise the method. You will learn how to define variables, write a method with quantities that scores, choose precautions, process data into a straight-line graph, calculate percentage errors, and evaluate results.

:::why
A chemist who cannot design a fair test cannot trust any result, however neat the arithmetic. Paper 5 tests exactly that: can you decide what to change, what to measure and what to keep the same, and then say how far the numbers can be trusted? The same thinking decides whether a new medicine works or a water supply is safe, so the skill outlives the exam.
:::

**Before you start**, you should have met the practical techniques and uncertainties in [Practical skills and qualitative analysis](#chem.practical), the idea of rate in [Rate equations and catalysis](#chem.rates2), and mole calculations from [Moles and stoichiometry](#chem.moles).

:::try Warm-up
Q: A burette is read to the nearest 0.05 cm³. What is the maximum uncertainty in one reading, and in a titre? (from [Practical skills and qualitative analysis](#chem.practical))
A: Each reading is uncertain by ±0.05 cm³. A titre is the difference of two readings, so it is uncertain by ±0.10 cm³.
Q: A graph of rate against \([\ce{A}]\) is a straight line through the origin. What is the order with respect to A, and what does the gradient give? (from [Rate equations and catalysis](#chem.rates2))
A: First order, because rate is proportional to \([\ce{A}]\). The gradient is the rate constant \(k\).
Q: How many moles are in 25.0 cm³ of a 0.200 mol dm⁻³ solution? (from [Moles and stoichiometry](#chem.moles))
A: \(n = cV = 0.200 \times 0.0250 = 5.00 \times 10^{-3}\) mol.
:::

## What Paper 5 is

Paper 5 is a written paper about experiments. You never touch apparatus. You are given a context, which may be a reaction you have never studied, together with all the background you need, and you apply skills.

| | Paper 5 |
|---|---|
| Time | 1 h 15 min |
| Marks | 30 |
| Questions | two or more |
| Objective | AO3 only (experimental skills and investigations) |
| Laboratory | none |

The mark grid says the paper contains at least 12 marks for **planning** (defining the problem and writing the method), at least 12 marks for **analysis, conclusion and evaluation**, and 6 marks that vary from paper to paper. So roughly 40% of the marks reward a plan and 40% reward working with results.

:::tip Time per mark
75 minutes for 30 marks is 2.5 minutes a mark. A 4-mark part deserves about ten minutes, a 12-mark plan about thirty. If a plan feels short at five lines, you have probably left out quantities, a safety point or how the result is processed.
:::

Everything on the paper is one of three skills, and the chapter follows them in order.

1. **Plan**: name the variables, write a method with apparatus, quantities and a table, and say how you will process the results.
2. **Analyse**: turn raw data into processed values, a graph, a gradient and an uncertainty.
3. **Evaluate**: judge anomalies, reliability and accuracy, and say what to change.

:::exam Reading an unfamiliar context
If the chemistry looks strange, do not panic: the question supplies what you need. Underline the quantity you must measure, the quantity you must change, and any value given (volumes, concentrations, apparatus). Use only apparatus the question lists, plus ordinary school laboratory apparatus. Link the chemistry you do know (rates, moles, energetics) to the unfamiliar part.
:::

## Variables and predictions

Every investigation changes one thing and watches another. Keep the three roles apart.

:::def Independent variable
The variable that you deliberately change in the investigation. You choose its values.
:::

:::def Dependent variable
The variable that you measure as a result of changing the independent variable. You read its values.
:::

:::def Control variable
A variable that could affect the dependent variable, and is kept the same in every experiment so that the test is fair.
:::

:::def Hypothesis (prediction)
A statement of how the dependent variable will change when the independent variable is changed, with a scientific reason. A good one names the direction and the reason.
:::

Each variable needs three things: its **name**, its **unit** or how it is measured, and (for the independent variable) the **values** you will use and the number of them. At least five values spaced evenly across a sensible range are needed to draw a trustworthy graph.

:::eg Aim: investigate how the concentration of hydrochloric acid affects the time for a piece of magnesium ribbon to disappear. State the variables and how each control variable is kept constant.
**Independent variable**: concentration of hydrochloric acid / mol dm⁻³. I will use 0.400, 0.800, 1.20, 1.60 and 2.00 mol dm⁻³ (five values). [B1]

**Dependent variable**: time for the magnesium ribbon to disappear completely / s, measured with a stopwatch. [B1]

**Control variables** and how they are controlled:
- the mass (or length) of magnesium: cut every piece from one ribbon to the same length, 2.0 cm, and check on a balance reading to 0.01 g; [B1]
- the volume of acid: 50.0 cm³ each time, measured with the same burette; [B1]
- the temperature: stand the beaker in a water bath at 25 °C and check the acid with a thermometer before adding the magnesium; [B1]
- the surface of the metal: clean each piece with sandpaper to remove the oxide layer. [B1]

Note that the **volume** of acid is controlled, not the "amount" of acid: the amount in moles changes with the concentration.
:::

### Making a prediction

A prediction connects the variables with chemistry. Use the pattern *as [independent] increases, [dependent] increases/decreases, because …*.

:::eg Write a prediction for the magnesium and acid investigation, and sketch the expected graph.
As the concentration of hydrochloric acid increases, the time taken for the magnesium to disappear decreases. [B1] There are more hydrogen ions in each cm³, so more collisions per second between \(\ce{H+}\) ions and magnesium atoms on the surface, and so more successful collisions each second. The reaction is faster. [B1]

If the rate is proportional to the concentration, the time is inversely proportional to it, so the graph of time against concentration is a falling curve that flattens out (shown below). [B1]
:::

:::plot A sketch of the prediction: the time for the magnesium to disappear falls as the concentration of acid rises, steeply at first and then more slowly.
--f "24/x+0*sqrt(x-0.4)+0*sqrt(2.2-x)" --x 0 2.6 --y 0 80 --noticks --xlabel "concentration of HCl" --ylabel "time for Mg to disappear" --label "predicted curve" --legend tr
:::

:::warn Vague variables score nothing
"The amount of acid", "the speed" and "the temperature of the room" are not variables you can use. Write *volume of acid / cm³*, *time for the ribbon to disappear / s* and *temperature of the water bath / °C*, and say how each is controlled or measured.
:::

## Writing a method that scores

A good plan can be followed by someone who has never seen your experiment. It gives the apparatus, the quantities, the steps in order, how you vary the independent variable, how you measure the dependent variable, what you keep constant, a hazard and precaution, a table and how you process the results. The model plan below is built up step by step.

**Aim**: investigate how the rate of the reaction between calcium carbonate and hydrochloric acid depends on the concentration of the acid, by measuring the volume of carbon dioxide against time.

\[\ce{CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g)}\]

### Choosing quantities that work

Quantities cannot be guessed. Check them with a short calculation, as an examiner expects.

:::eg Show that 0.30 g of calcium carbonate with 50.0 cm³ of hydrochloric acid of concentration 0.400 mol dm⁻³ to 2.00 mol dm⁻³ is a sensible choice when the gas is collected in a 100 cm³ gas syringe.
\(M_r(\ce{CaCO3}) = 40.1 + 12.0 + 3(16.0) = 100.1\) [B1]

\(n(\ce{CaCO3}) = 0.30 / 100.1 = 2.997 \times 10^{-3}\) mol [M1]

Acid needed: \(2 \times 2.997 \times 10^{-3} = 5.99 \times 10^{-3}\) mol. The weakest acid contains \(0.400 \times 0.0500 = 0.0200\) mol, more than three times as much, so the acid is in excess in every experiment and the carbonate is always the limiting reactant. [M1]

Maximum gas: \(2.997 \times 10^{-3} \times 24.0 = 0.0719\) dm³ = 71.9 cm³ at room conditions, which fits in a 100 cm³ gas syringe. [A1]
:::

Because the acid is always in excess, the final gas volume is the same in every experiment (72 cm³). Only the speed changes, which makes the comparison fair.

### Varying the concentration: the dilution table

Stock solution: 2.00 mol dm⁻³ hydrochloric acid. Measure the volumes with a burette (to ±0.05 cm³ a reading), and make up each to 50.0 cm³ with distilled water. Since \(c_1V_1 = c_2V_2\), the volume of stock is \(V_1 = c_2 \times 50.0 / 2.00\).

| Required concentration / mol dm⁻³ | Volume of 2.00 mol dm⁻³ HCl / cm³ | Volume of distilled water / cm³ |
|---|---|---|
| 0.400 | 10.0 | 40.0 |
| 0.800 | 20.0 | 30.0 |
| 1.20 | 30.0 | 20.0 |
| 1.60 | 40.0 | 10.0 |
| 2.00 | 50.0 | 0.0 |

### Measuring: what apparatus and how precise?

Name the instrument and the precision. Reading the instrument tells you its uncertainty: **half the smallest division** is the maximum uncertainty of one reading.

| Quantity | Instrument | Reading to | Uncertainty of one reading |
|---|---|---|---|
| mass | balance | 0.01 g | ±0.005 g (two readings if weighed by difference: ±0.01 g) |
| volume of a titration | burette | 0.05 cm³ | ±0.05 cm³ (a titre has two readings: ±0.10 cm³) |
| volume of a liquid, approximate | measuring cylinder (1.0 cm³ divisions) | 0.5 cm³ | ±0.5 cm³ |
| volume of a gas | gas syringe (1 cm³ divisions) | 0.5 cm³ | ±0.5 cm³ |
| temperature | thermometer (1 °C divisions) | 0.5 °C | ±0.5 °C |
| fixed volume of solution | pipette | marked volume, e.g. 25.0 cm³ | the value stated in the question |
| time | stopwatch | 0.1 s | about ±0.2 s, from reaction time in starting and stopping |

:::html
<figure class="fig small"><svg viewBox="10 5 335 180" role="img" aria-label="Apparatus: a conical flask containing hydrochloric acid and calcium carbonate chips, closed with a bung, with a delivery tube leading to a horizontal gas syringe"><path class="ln" d="M60 60V90L25 170H115L80 90V60"/><path class="fa" d="M40.3 135H99.7L115 170H25Z"/><rect class="fm2" x="42" y="158" width="9" height="8"/><rect class="fm2" x="56" y="160" width="8" height="6"/><rect class="fm2" x="72" y="157" width="10" height="9"/><rect class="fm2" x="90" y="160" width="9" height="8"/><rect class="fm2" x="57" y="52" width="26" height="18"/><rect class="ln" x="57" y="52" width="26" height="18"/><path class="ln" d="M66 78V30H200M74 78V38H200"/><path class="ln" d="M200 18H300V50H200M200 18V30M200 38V50"/><path class="ln thin" d="M210 18V23M225 18V23M240 18V23M255 18V23M270 18V23M285 18V23"/><rect class="fm2" x="236" y="26" width="12" height="23"/><rect class="ln" x="236" y="26" width="12" height="23"/><path class="ln" d="M248 34H330M330 24V44"/><text class="tl" x="95" y="22">delivery tube</text><text class="tl" x="100" y="64">bung</text><path class="ln-m thin" d="M98 60H86"/><text class="tl tc" x="265" y="82">gas syringe</text><path class="ln-m thin" d="M265 69V53"/><text class="tl" x="128" y="140">hydrochloric acid</text><path class="ln-m thin" d="M126 136H95"/><text class="tl" x="128" y="172">calcium carbonate chips</text><path class="ln-m thin" d="M126 166H100"/></svg><figcaption>Gas collection. The carbon dioxide leaves through the delivery tube and pushes the plunger of the gas syringe along. Read the volume at fixed times. The bung must be fitted at once, or gas is lost.</figcaption></figure>
:::

### The complete model plan

:::eg Write a plan for the investigation above. Include the apparatus, quantities, procedure, controls, a hazard with a precaution, the table and how the results are processed.
**Prediction**: the greater the concentration of acid, the faster the reaction (and the greater the volume of gas after a fixed time) because there are more \(\ce{H+}\) ions per cm³, so more frequent successful collisions. [B1]

**Independent variable**: concentration of hydrochloric acid, five values 0.400 to 2.00 mol dm⁻³ made from 2.00 mol dm⁻³ stock using the dilution table. **Dependent variable**: volume of \(\ce{CO2}\) collected at 10 s intervals up to 120 s. [B1]

**Apparatus**: 100 cm³ conical flask, bung and delivery tube, 100 cm³ gas syringe, 50 cm³ burette, balance (0.01 g), stopwatch, calcium carbonate chips. [B1]

**Method**:
1. Use the burette to measure the volumes of stock acid and water for the first concentration into the conical flask, to make 50.0 cm³ in total. [B1]
2. Weigh 0.30 g of calcium carbonate chips of the same size and tip them in. Immediately fit the bung, connected to the gas syringe, and start the stopwatch. [B1]
3. Read the syringe every 10 s for 120 s and record the volume of gas. [B1]
4. Repeat for each of the other four concentrations with a fresh sample of chips, and repeat each concentration once more (replicate). [B1]

**Controls**: the same mass and size of chips (0.30 g), the same volume of acid (50.0 cm³), the same temperature (stand the flask in a water bath at 25 °C, checked by a thermometer). [B1]

**Hazard**: hydrochloric acid at this concentration can irritate the eyes and skin. **Precaution**: wear goggles and wash splashes from the skin with plenty of water. [B1]

**Processing**: plot volume of gas against time for each concentration, draw a tangent at \(t = 0\) and measure its gradient (the initial rate in cm³ s⁻¹). Plot initial rate against concentration. [B1]
:::

### Two ways to measure rate

The **initial rate** is the gradient of the volume–time graph at time zero. Alternatively, record the time \(t\) for a fixed volume of gas, say 30.0 cm³, to be collected. The average rate over that period is \(30.0 / t\), so with the same volume every time, the rate is proportional to \(1/t\). That is why \(1/t\) is plotted against concentration: the gradient is then proportional to the rate constant for a first-order reaction.

The results table is drawn before the experiment, with headings in the form *quantity / unit*, one table, and room for replicates and the processed value.

| concentration of HCl / mol dm⁻³ | time for 30.0 cm³, t₁ / s | t₂ / s | mean t / s | 1/t / s⁻¹ |
|---|---|---|---|---|
| 0.400 | … | … | … | … |
| 0.800 | … | … | … | … |
| 1.20 | … | … | … | … |
| 1.60 | … | … | … | … |
| 2.00 | … | … | … | … |

### Control experiments

A **control experiment** is a run in which the independent variable is removed or set to a known reference value, to show that the effect comes from the variable and not from something else. For the plan above, 50.0 cm³ of distilled water in place of acid with 0.30 g of chips should give no gas, which shows that the volume rise in the other runs is caused by the acid. Include one only when the question suggests that something else could produce the effect.

## Safety and risk

A hazard is something that can cause harm; a risk is the chance of harm; a precaution is what you do about it. "Wear goggles" alone scores little, because it does not name the hazard. Link each hazard to a specific precaution.

| Hazard | Precaution |
|---|---|
| toxic or irritating gas produced (chlorine, sulfur dioxide, nitrogen dioxide) | carry out the reaction in a fume cupboard |
| concentrated acid or alkali (corrosive) | goggles and chemically resistant gloves; add acid slowly to water; wash splashes with plenty of water |
| flammable solvent (ethanol, propanone, hexane) | no naked flames; heat in a water bath or with an electric heater |
| fine powder that can be breathed in | wear a face mask; avoid creating dust |
| toxic solutions (barium compounds, dichromate(VI), lead compounds) | wear gloves, avoid skin contact, put waste in a labelled container |
| hot crucible or glassware | handle with tongs, place on a heatproof mat and let it cool before weighing |
| closed system that is heated | never heat a closed container; leave one opening |

:::warn Write the hazard, then the precaution
"Wear a lab coat and goggles" is a general habit, not an answer. A mark needs a named hazard ("sulfur dioxide gas is toxic") and a precaution that deals with it ("do the experiment in a fume cupboard"). For one hazard and one precaution, give one of each, not a list of five precautions.
:::

## Standard procedures

Planning questions expect you to describe these correctly.

### Making a standard solution

A **standard solution** has an accurately known concentration.

:::steps
1. Weigh by difference: weigh the weighing bottle with the solid, tip the solid into a beaker, reweigh the bottle. The decrease in mass is the mass transferred, so no solid is left behind on the balance.
2. Dissolve the solid in distilled water in the beaker, using less than the final volume.
3. Pour the solution into a volumetric flask through a funnel, and rinse the beaker and funnel into the flask with distilled water.
4. Add distilled water until the bottom of the meniscus is on the mark, using a dropping pipette for the last few drops.
5. Stopper the flask and invert it several times to mix.
:::

:::eg Calculate the mass of anhydrous sodium carbonate needed to make 250.0 cm³ of a 0.0500 mol dm⁻³ standard solution.
\(M_r(\ce{Na2CO3}) = 2(23.0) + 12.0 + 3(16.0) = 106.0\) [B1]

\(n = cV = 0.0500 \times 0.2500 = 0.01250\) mol [M1]

\(m = 0.01250 \times 106.0 = 1.325\) g, weighed by difference on a balance reading to 0.01 g. [A1]
:::

### Other standard procedures

- **Heating to constant mass** (for example a hydrated salt in a crucible): heat strongly, cool in a desiccator so that the solid cannot take up moisture, weigh, then heat again and reweigh. Repeat until two consecutive masses agree (to within 0.01 g on this balance). That shows the reaction is complete.
- **Concordant titres**: a rough titration first, then accurate titrations until two titres are within 0.10 cm³ of each other; the mean uses only those.
- **Readings near an inflexion point**: when the pH or temperature changes rapidly, take readings much closer together (for example every 0.1 cm³ instead of every 1 cm³), so that the steep part of the curve is not missed.

:::eg Plan a gravimetric experiment to find the value of x in hydrated copper(II) sulfate, \(\ce{CuSO4.xH2O}\), and process these results: crucible and lid 24.68 g; with hydrated salt 27.18 g; after first heating 26.29 g; after second heating 26.28 g; after third heating 26.28 g.
*Plan*:
1. Weigh a clean, dry crucible with its lid. [B1]
2. Add about 2.5 g of the hydrated salt and reweigh, so that the mass of salt is found by difference. [B1]
3. Heat the crucible gently, then strongly, until the blue crystals turn white. Cool in a desiccator and reweigh. [B1]
4. Reheat, cool and reweigh until two consecutive masses are the same. [B1]
5. Precautions: tongs and a heatproof mat for the hot crucible; do not overheat, because black copper(II) oxide would be formed and the mass would fall too far. [B1]

*Results*: mass of hydrated salt \(= 27.18 - 24.68 = 2.50\) g; mass of anhydrous salt \(= 26.28 - 24.68 = 1.60\) g; mass of water lost \(= 27.18 - 26.28 = 0.90\) g (the last two masses agree, so heating is complete). [B1]

\(M_r(\ce{CuSO4}) = 63.5 + 32.1 + 4(16.0) = 159.6\), \(M_r(\ce{H2O}) = 18.0\) [B1]

\(n(\ce{CuSO4}) = 1.60 / 159.6 = 0.01003\) mol, \(n(\ce{H2O}) = 0.90 / 18.0 = 0.0500\) mol [M1]

\(x = 0.0500 / 0.01003 = 4.99\), so \(x = 5\). [A1]
:::

## Dealing with data

### Processed values

Raw readings are rarely the quantity you plot. Common processed values are:

- the **mean** of replicate readings (leaving out any anomalies);
- a **percentage change**, \(\dfrac{\text{final} - \text{initial}}{\text{initial}} \times 100\);
- \(1/t\) as a measure of rate, for the reason in the previous section;
- \(\ln y\) or \(\lg y\), when the question gives you the method, to turn a curve into a straight line.

Give calculated values to the same number of significant figures as (or one more than) the least precise data, and quote the unit in the column heading. Raw data keep the same number of decimal places throughout the column.

### Straight-line graphs

A relationship is easiest to test when the graph is a straight line, \(y = mx + c\). Choose the quantities plotted so that the theory predicts one.

:::key Drawing and using a graph
- Dependent variable (or processed value) on the y-axis, independent variable on the x-axis, each labelled with quantity / unit.
- Scale: 1, 2 or 5 units (or ×10, ÷10 of these) to a 20 mm square, with the points filling at least half the grid in both directions. The origin need not be shown.
- Plot each point as × or ⊙ and draw one straight line of best fit with about the same number of points above and below it.
- Mark any anomalous point and ignore it when drawing the line.
- Gradient: use two points on the line (not data points unless they are on it) more than half the length of the line apart, and show them on the graph. Gradient \(= \Delta y / \Delta x\), with its unit.
- y-intercept: the value of \(y\) where the line meets \(x = 0\); extend the line if the axis does not start at zero.
:::

:::eg A first-order reaction is followed by taking 10.0 cm³ samples of a mixture of hydrogen peroxide and acid at intervals, stopping the reaction and titrating with \(\ce{KMnO4}\). The titre is proportional to the concentration of hydrogen peroxide. The results are below. Use the graph of \(\ln(\text{titre})\) against time to find the rate constant.
| time / min | 0 | 10 | 20 | 30 | 40 | 50 |
|---|---|---|---|---|---|---|
| titre / cm³ | 24.00 | 17.80 | 13.15 | 9.75 | 7.25 | 5.35 |
| ln(titre) | 3.178 | 2.879 | 2.576 | 2.277 | 1.981 | 1.677 |

For a first-order reaction, \(\ln [\ce{H2O2}] = \ln [\ce{H2O2}]_0 - kt\). This is the integrated form of the first-order rate law (the half-life equation \(t_{\frac12} = \ln 2/k\) in [Rate equations and catalysis](#chem.rates2) comes from it); you are not asked to derive it. Taking ln (the natural-logarithm button on the calculator) of a first-order concentration turns the exponential curve into a straight line of gradient \(-k\). The titre is proportional to \([\ce{H2O2}]\), so \(\ln(\text{titre}) = \ln(\text{titre})_0 - kt\): a straight line with gradient \(-k\). [B1]

:::plot The graph of ln(titre) against time is a straight line. Two points on the line, far apart, give the gradient.
--f "3.178-0.0300*x" --x 0 56 --y 0 4.5 --pt "0,3.18,A (0, 3.18)@ne" --pt "50,1.68,B (50, 1.68)@ne" --xlabel "time / min" --ylabel "ln(titre)" --label "line of best fit" --legend tr
:::

Take points A (0, 3.18) and B (50, 1.68), both on the line. [M1]

Gradient \(= (1.68 - 3.18) / (50 - 0) = -0.0300\) min⁻¹ [M1]

\(k = 0.0300\) min⁻¹ (equal to \(5.00 \times 10^{-4}\) s⁻¹) [A1]

The y-intercept is 3.18. It has no unit, because it is the logarithm of the starting titre (24.0 cm³), and \(e^{3.18} = 24.0\). [B1]

Check with the half-life: \(t_{1/2} = 0.693 / k = 23.1\) min. The titre falls from 24.00 to about 12 cm³ in about 23 min, as the table shows (13.15 at 20 min, 9.75 at 30 min). [B1]
:::

The **unit of a gradient** is the unit of y divided by the unit of x. Here \(\ln\) has no unit, so the gradient is in min⁻¹. If the axes were *rate / mol dm⁻³ s⁻¹* and *concentration / mol dm⁻³*, the gradient would be in s⁻¹. The unit of the intercept is the unit of y.

### Percentage error

Each measuring instrument has a maximum uncertainty (the table above). The **percentage error** in a measurement is

\[\text{percentage error} = \frac{\text{uncertainty}}{\text{value measured}} \times 100\]

This is the same quantity that [Practical skills and qualitative analysis](#chem.practical) called percentage uncertainty; Paper 5 says percentage error.

If the quantity is found from two readings (a titre, a temperature change, weighing by difference), the uncertainties add. A small value measured with a coarse instrument has a large percentage error.

:::eg Calculate the percentage error in a titre of 23.45 cm³, and then in the concentration of hydrochloric acid found by titrating 25.0 cm³ of it (pipette uncertainty ±0.06 cm³) against 0.100 mol dm⁻³ sodium hydroxide.
Titre: two readings, each ±0.05 cm³, so ±0.10 cm³. \(0.10 / 23.45 \times 100 = 0.426\%\) [M1 A1]

Pipette: \(0.06 / 25.0 \times 100 = 0.24\%\) [B1]

The concentration comes from \(c = 0.100 \times 23.45 / 25.0 = 0.0938\) mol dm⁻³. The final result combines the errors by adding the percentages: \(0.426 + 0.24 = 0.67\%\) [M1]

Absolute uncertainty: \(0.0938 \times 0.67/100 = 6.3 \times 10^{-4}\), so the concentration is \((0.0938 \pm 0.0006)\) mol dm⁻³. [A1]
:::

:::eg The temperature of a solution rises from 21.5 °C to 35.5 °C. The thermometer is read to the nearest 0.5 °C. Calculate the percentage error in the temperature change.
\(\Delta T = 35.5 - 21.5 = 14.0\) °C [B1]

Two readings, each ±0.5 °C, so the uncertainty in \(\Delta T\) is ±1.0 °C. [M1]

\(1.0 / 14.0 \times 100 = 7.14\%\) [A1]
:::

:::warn Percentage error is not percentage difference
The percentage error comes from the instruments and describes how much you could be wrong. The percentage difference from a known value, \((\text{experimental} - \text{true}) / \text{true} \times 100\), describes how wrong the answer actually was. If the second is bigger than the first, there is another source of error, usually a method weakness such as heat loss.
:::

## Conclusions and evaluation

### Drawing a conclusion

A conclusion answers the aim, states whether the data support the hypothesis, and uses numbers with units from the results. Say what the graph shows: *"the graph of \(1/t\) against concentration is a straight line through the origin, so the rate is directly proportional to the concentration of acid: first order. The prediction is supported."* Then say how confident you are, which depends on the evaluation below.

### Anomalies

An **anomalous** result is one that does not fit the pattern of the others. To deal with one:

1. **Identify** it, quoting the value and where it lies away from the trend or the replicates.
2. **Explain** a likely cause, specific to the experiment (the stopwatch was stopped late, the bung was fitted late and gas escaped, not all of the solid reacted).
3. **Treat** it: leave it out of the mean and the line of best fit (never delete it from the table), repeat the experiment if possible, and say that you did.

:::eg In an experiment the time for 30.0 cm³ of gas at 1.20 mol dm⁻³ was recorded three times: 41.2 s, 40.6 s and 49.8 s. Identify the anomaly, suggest a cause and give the mean to use.
The result 49.8 s is anomalous: the other two agree within 0.6 s, and it is 8.9 s longer than the mean of those two. [B1]

A possible cause is that the bung was fitted late, or loosely, so that some gas escaped and the syringe reached 30.0 cm³ later. [B1]

Mean of the two consistent results: \((41.2 + 40.6) / 2 = 40.9\) s. [M1] Including the anomaly would give 43.9 s, three seconds too long. The anomaly stays in the table, marked, but is not used in the mean. [A1]
:::

### Reliability, accuracy and replicates

- **Accuracy**: how close a result is to the true value. A **systematic error** (a balance reading 0.05 g with nothing on it, a thermometer that reads 1 °C too high) shifts every result the same way, so it harms accuracy and repeating does not remove it.
- **Reliability** (precision): how closely repeated measurements agree. A **random error** (changes in room temperature, small differences in judging a colour change) scatters results about the true value.
- To be reliable, carry out **replicate** measurements, which means repeating an identical experiment, and take a mean. This reduces the effect of random errors. Never write "repeat to make it accurate".

"Human error" is not an acceptable answer. Say what the person did: "the stopwatch was started late", "the burette was read from above the meniscus".

### Evaluating a method

Give a **weakness**, say what **effect** it has on the results, and give a specific **improvement**. A good evaluation covers replication, the range of the independent variable, control of variables and the instruments.

| Weakness | Effect | Improvement |
|---|---|---|
| heat lost to the surroundings in a temperature-change experiment | measured temperature rise too small | insulate with a lid and lagging; plot a cooling curve and extrapolate |
| gas escapes before the bung is fitted | volume too small, time too long | fit the bung before adding the last reagent (for example tip the chips in from a small tube) |
| thermometer reads to 0.5 °C and the temperature change is small | large percentage error | use a thermometer reading to 0.1 °C, or a larger amount of reactants for a larger temperature change |
| each experiment done once | no way to spot anomalies; results less reliable | carry out each experiment at least twice and take the mean of consistent results |
| only three concentrations, close together | cannot show the shape of the relationship | use at least five values over a wider range |
| a gas is slightly soluble in water | volume of gas too small | collect the gas over a liquid in which it is less soluble, or use a gas syringe |
| colour change at the end point judged by eye | end-point times scattered | use a colorimeter or the same observer and background each time |

:::eg A student investigated how the mass of manganese(IV) oxide catalyst affects the time for 40 cm³ of oxygen to be collected from hydrogen peroxide. She used five masses between 0.10 g and 0.30 g, measured each once, and measured the volume of hydrogen peroxide with a 25 cm³ measuring cylinder. Evaluate the method and suggest two improvements.
*Weakness 1*: each experiment was done once, so an anomaly cannot be identified and the results are not shown to be reliable. [B1] *Improvement*: repeat each mass and calculate a mean of consistent results. [B1]

*Weakness 2*: the volume of hydrogen peroxide was measured to ±0.5 cm³ with a measuring cylinder, which for a 25.0 cm³ portion is a percentage error of 2.0%, so the concentration varies from experiment to experiment. [B1] *Improvement*: use a 25.0 cm³ pipette. [B1]

*Weakness 3*: the narrow range (0.10 to 0.30 g) may not show the overall trend. [B1] *Improvement*: use masses from 0.05 g to 0.50 g. [B1]
:::

### The effect of changing the conditions

Many questions ask what happens if a condition changes. Decide which quantity is affected, then state the effect on the measurement, with a reason.

:::eg In the calcium carbonate experiment, powdered calcium carbonate of the same mass replaces the chips. State and explain the effect on the volume–time graph and on the final volume of gas.
The surface area is much larger, so more particles of carbonate are exposed to acid at once and the rate is greater: the curve is steeper at the start. [B1]

The mass of calcium carbonate is the same, so the same number of moles of \(\ce{CO2}\) forms and the final volume is unchanged (72 cm³). [B1]
:::

:::eg Spot the error
A student writes the plan for the magnesium and acid experiment:

Line 1. Independent variable: the concentration of hydrochloric acid, 0.400 to 2.00 mol dm⁻³.
Line 2. Dependent variable: the time for the ribbon to disappear, in seconds.
Line 3. Control variable: keep the amount of acid the same each time.

Identify the error and say what mark is lost.

Lines 1 and 2 are correct [B1] [B1].

**Line 3 is wrong.** The "amount" of acid means moles, and the number of moles has to change when the concentration changes (at a fixed volume). What can be kept the same is the **volume** of acid, for example 50.0 cm³ measured with a burette. The control mark is lost [B0]. The student scores 2 out of 3.
:::

:::board AQA
AQA has no separate planning paper like Cambridge's Paper 5: its written A Level papers contain practical-skills and data-analysis questions instead, so the same skills are tested in a different layout.
:::

:::try Start easy, finish at exam standard
Q: Aim: investigate how temperature affects the mass of potassium nitrate that dissolves in 50.0 cm³ of water. State the independent, dependent and two control variables.
A: Independent: temperature of the water / °C. Dependent: the mass of potassium nitrate that dissolves / g. Controls: the volume of water (50.0 cm³), and the stirring (same speed and time before judging that the solid has dissolved).
Q: Calculate the volumes of 0.500 mol dm⁻³ sodium hydroxide and water needed to make 50.0 cm³ of each of 0.100, 0.200, 0.300 and 0.400 mol dm⁻³ solutions.
A: \(V = c \times 50.0 / 0.500\): 10.0, 20.0, 30.0 and 40.0 cm³ of sodium hydroxide, with 40.0, 30.0, 20.0 and 10.0 cm³ of water.
Q: Calculate the mass of ethanedioic acid dihydrate, \(\ce{H2C2O4.2H2O}\), needed to make 250.0 cm³ of a 0.0400 mol dm⁻³ solution.
A: \[M_r = 2(1.0) + 2(12.0) + 4(16.0) + 2(18.0) = 126.0\]
\(n = 0.0400 \times 0.2500 = 0.01000\) mol. \(m = 0.01000 \times 126.0 = 1.260\) g.
Q: Calculate the percentage error in a titre of 18.40 cm³ and in a temperature change of 8.5 °C measured with a thermometer reading to the nearest 0.5 °C. Which is larger?
A: Titre: \(0.10 / 18.40 \times 100 = 0.543\%\). Temperature change: \(1.0 / 8.5 \times 100 = 11.8\%\). The temperature change has the larger percentage error.
Q: The line of best fit on a graph of initial rate (mol dm⁻³ s⁻¹) against \([\ce{A}]\) (mol dm⁻³) passes through (0.050, \(1.10 \times 10^{-4}\)) and (0.250, \(5.50 \times 10^{-4}\)). Calculate the gradient with its unit, and state what the intercept shows.
A: Gradient:
\[\frac{5.50 \times 10^{-4} - 1.10 \times 10^{-4}}{0.250 - 0.050} = 2.20 \times 10^{-3}\ \text{s}^{-1}\]
Intercept at \([\ce{A}] = 0\): \(1.10 \times 10^{-4} - 2.20 \times 10^{-3} \times 0.050 = 0\): the line passes through the origin, so rate is proportional to \([\ce{A}]\) (first order) and \(k = 2.20 \times 10^{-3}\) s⁻¹.
Q: Powdered zinc is used in place of the same mass of zinc granules in a reaction with excess acid. State and explain the effect on the rate and on the total gas volume.
A: The rate increases because the surface area is greater, so there are more collisions per second. The total volume is unchanged because the amount of zinc is the same and the acid is in excess.
Q: Give a hazard and a precaution for (a) heating ethanol under reflux, (b) a reaction that produces sulfur dioxide.
A: (a) Ethanol is flammable, so heat with an electric heater or a hot-water bath and no naked flame. (b) Sulfur dioxide is a toxic gas, so carry out the reaction in a fume cupboard.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A student investigates how the mass of manganese(IV) oxide catalyst affects the rate of decomposition of hydrogen peroxide, measured by the volume of oxygen collected in 60 s. State the independent variable, the dependent variable and one control variable, with how it is controlled.
A: Independent variable: the mass of manganese(IV) oxide / g. [B1]
Dependent variable: the volume of oxygen collected in 60 s / cm³. [B1]
Control: the volume (and concentration) of hydrogen peroxide, e.g. 25.0 cm³ of the same solution, measured with a pipette. [B1]
Q: [2 marks] ★ A student records burette readings as 24.3 cm³ in one place and 24.30 cm³ in another. Explain what is wrong and how it should be written.
A: Readings should all be given to the same precision of the burette, two decimal places (to the nearest 0.05 cm³). [B1] So 24.3 should be 24.30 cm³. [B1]
Q: [4 marks] ★★ A student weighs a sample by difference and finds 1.62 g, using a balance that reads to 0.01 g (±0.005 g per reading). The titre is 21.35 cm³. Calculate the percentage error in each measurement and say which is larger.
H: A mass by difference has two readings. A titre has two readings of ±0.05 cm³.
A: Mass: two readings, so ±0.01 g; \(0.01 / 1.62 \times 100 = 0.617\%\). [M1 A1]
Titre: \(0.10 / 21.35 \times 100 = 0.468\%\). [M1]
The percentage error in the mass is larger. [A1]
Q: [5 marks] ★★ In a kinetics experiment the line of best fit for a graph of \(1/t\) (s⁻¹) against concentration (mol dm⁻³) passes through (0.200, 0.0160) and (0.800, 0.0640). (a) Calculate the gradient with its unit. (b) Calculate the y-intercept. (c) State what the intercept shows. (d) State the relationship between rate and concentration.
H: Use \(y = mx + c\) once you have \(m\).
A: (a) Gradient \(= (0.0640 - 0.0160) / (0.800 - 0.200) = 0.0800\) [M1] dm³ mol⁻¹ s⁻¹ [A1]
(b) \(c = 0.0160 - 0.0800 \times 0.200 = 0\) [B1]
(c) The line passes through the origin, so \(1/t\) (the rate) is directly proportional to concentration. [B1]
(d) rate \(\propto\) concentration: the reaction is first order in this reactant. [B1]
Q: [5 marks] ★★ In an experiment on the effect of temperature on a reaction rate, a student obtained times of 31.4 s, 30.8 s and 38.9 s for three identical runs at 40 °C. (a) Identify the anomaly and suggest a likely cause. (b) Calculate the mean to use. (c) Explain why repeating the experiment improves confidence in the result.
A: (a) 38.9 s is anomalous, because the other two agree within 0.6 s. [B1] The temperature of the mixture may have been lower, or the stopwatch stopped late. [B1]
(b) \((31.4 + 30.8) / 2 = 31.1\) s. [M1 A1]
(c) Replicates show whether the results agree, so random errors have less effect on the mean, which makes the results more reliable. [B1]
Q: [12 marks] ★★★ Plan an investigation of how the temperature affects the time for the cross to disappear when aqueous sodium thiosulfate reacts with dilute hydrochloric acid. The cloudiness is caused by a fine precipitate of sulfur.
\[\ce{S2O3^2-(aq) + 2H+(aq) -> S(s) + SO2(g) + H2O(l)}\]
You are provided with 0.100 mol dm⁻³ sodium thiosulfate, 1.00 mol dm⁻³ hydrochloric acid, a water bath, thermometer, stopwatch, conical flasks, measuring cylinders and a piece of paper with a cross.
A: Prediction: as the temperature increases the time for the cross to disappear decreases, because more particles have energy of at least the activation energy, so collisions are more often successful. [B1]
Independent variable: temperature of the mixture / °C; dependent variable: time for the cross to disappear / s. [B1]
Controls: volume and concentration of both solutions, the same flask and cross, the same observer. [B1]
Apparatus listed: conical flask, water bath, thermometer, stopwatch, measuring cylinders, paper with a cross. [B1]
Quantities: for example 50.0 cm³ of 0.100 mol dm⁻³ thiosulfate and 5.0 cm³ of 1.00 mol dm⁻³ acid each time. [B1]
Temperature control: warm the thiosulfate in the flask in a water bath until it is at the chosen temperature (checked with the thermometer); warm the acid in a test tube to the same temperature. [B1]
Measuring: add the acid, start the stopwatch, swirl, look down at the cross from above, and stop the stopwatch when the cross can no longer be seen; record the temperature again at the end. [B1]
Range and repeats: at least five temperatures, such as 20, 30, 40, 50 and 60 °C, and repeat each. [B1]
Hazard: sulfur dioxide is toxic (and the acid irritates the eyes). [B1]
Precaution: carry out the experiments in a fume cupboard or well-ventilated room, and wear goggles. [B1]
Results table: temperature / °C, time / s (two runs), mean time / s, 1/time / s⁻¹. [B1]
Processing: plot 1/t (a measure of rate) against temperature and describe the trend (or plot time against temperature and draw a smooth curve). [B1]
Q: [6 marks] ★★★ A student plots a graph of [A] / mol dm⁻³ against time / s for a reaction. The points (0, 2.00), (10, 1.60), (20, 1.20) and (30, 0.80) lie on a straight line. (a) Explain how the data show that the reaction is not first order. (b) State the order suggested by the data. (c) Calculate the rate constant from the graph.
H: Look at the half-life: the time for [A] to halve. Zero order has a constant gradient.
A: (a) For a first-order reaction the half-life is constant. Here, [A] falls from 2.00 to 1.00 in 25 s but from 1.00 to 0.50 in 12.5 s, so the half-life is not constant. [M1 A1]
(b) The concentration falls by the same amount (0.40 mol dm⁻³) every 10 s, so the rate is constant: zero order. [B1]
(c) For zero order, rate \(= k\) = the magnitude of the gradient \(= (2.00 - 0.80) / (30 - 0)\) [M1] \(= 0.0400\) [A1] mol dm⁻³ s⁻¹ [B1]
:::

:::try Stretch for A*
Q: [6 marks] A student wants to know which of two antacid tablets, X and Y, neutralises more acid. Tablets are insoluble in water, and the tablets contain carbonates. Using a back titration, plan how to find the moles of hydrochloric acid neutralised by one tablet. You are provided with 1.00 mol dm⁻³ hydrochloric acid, 0.200 mol dm⁻³ sodium hydroxide, a suitable indicator, a balance, and common laboratory apparatus.
H: Add an excess of acid first. Then ask what is left.
H: The unused acid is titrated with alkali. The acid used by the tablet is the difference.
H: The titration is strong acid with strong alkali, so methyl orange is suitable.
A: Weigh one tablet (by difference) and crush it, so that the reaction is fast. [B1]
Add it to a conical flask with a measured excess of hydrochloric acid, for example 50.0 cm³ of 1.00 mol dm⁻³ (from a burette or pipette), and warm gently or swirl until the effervescence stops. [B1]
Transfer to a 250.0 cm³ volumetric flask, rinsing the conical flask into it, and make up to the mark with distilled water; mix. [B1]
Titrate 25.0 cm³ samples (pipette) with 0.200 mol dm⁻³ sodium hydroxide, using methyl orange, until the first permanent colour change, repeating until two titres are within 0.10 cm³. [B1]
Calculate moles of acid left: \(n(\ce{HCl}) = n(\ce{NaOH}) \times 10\) (scaling 25.0 to 250.0 cm³). [B1]
Moles neutralised = moles added − moles left. Compare tablets X and Y, with the same procedure for each. [B1]
Q: [5 marks] The following data are from an experiment on the decomposition of a compound; samples are taken at intervals and the titre (proportional to concentration) is recorded.
| time / min | 0 | 10 | 30 | 70 |
|---|---|---|---|---|
| titre / cm³ | 20.0 | 10.0 | 5.0 | 2.5 |
Show that the reaction is not first order, and show that it is second order using a graph of 1/titre against time.
H: Compare successive half-lives.
H: The reciprocal of the titre should be linear with time if the order is two.
A: The titre halves from 20.0 to 10.0 in 10 min, from 10.0 to 5.0 in 20 min, and from 5.0 to 2.5 in 40 min. The half-life doubles each time, so it is not constant, and the reaction is not first order. [M1 A1]
1/titre: 0.0500, 0.100, 0.200, 0.400 cm⁻³. [M1]
Gradient between successive points: \(0.0500/10 = 0.00500\), \(0.100/20 = 0.00500\), \(0.200/40 = 0.00500\) cm⁻³ min⁻¹: constant, so 1/titre against time is a straight line. [M1]
A straight line for a plot of 1/[A] against time shows a second-order reaction. [A1]
:::

:::quiz
? A student writes: "I will keep the amount of acid the same". Which is a better control variable?
- the number of moles of acid
+ the volume of acid, measured with the same apparatus
- the colour of the acid
- the speed of the reaction
> Variables must be measurable and controllable. Moles of acid change when the concentration changes at a fixed volume, but the volume can be fixed.
? Why does a plot of 1/t against concentration help with rate?
- Because time is always inversely proportional to concentration
+ Because for the same change (for example the same volume of gas), the average rate is proportional to 1/t
- Because it removes the need for a stopwatch
- Because 1/t is always a straight line
> For a fixed amount of change in time \(t\), rate = change / \(t\), so rate is proportional to \(1/t\). Whether the graph is straight depends on the order.
? A student repeats an experiment three times "to make it accurate". What is wrong with that?
- Repeating does not change anything
+ Replicates improve reliability but do not remove a systematic error
- Repeating makes the experiment less accurate
- Three repeats are never enough
> A mean of replicates reduces random error (greater reliability). A systematic error such as a balance zero error affects every repeat the same way.
? The temperature rise in an experiment is 12.0 °C, measured from two readings on a thermometer with 1 °C divisions. What is the percentage error?
- 0.5 / 12.0 × 100 = 4.17%
+ 1.0 / 12.0 × 100 = 8.33%
- 0.1 / 12.0 × 100 = 0.833%
- 12.0 / 1.0 × 100 = 1200%
> Each reading is uncertain by ±0.5 °C and the change uses two readings: ±1.0 °C. The 4.17% option forgot the second reading.
? Which is an acceptable improvement for "the thermometer reads to only 0.5 °C and the temperature rise is small"?
- Be more careful
+ Use a thermometer reading to 0.1 °C or a larger quantity of reactants
- Reduce human error
- Do the experiment again
> A good improvement names a specific change that reduces the percentage error. "Be careful" and "human error" score nothing.
:::

:::checklist What you can now do
- [ ] I can identify the independent, dependent and control variables and state how each control is kept constant.
- [ ] I can write a prediction as a hypothesis with a scientific reason, or sketch the expected graph.
- [ ] I can write a full method with apparatus, quantities, procedure, replicates, control experiment, a hazard with a precaution, and a results table.
- [ ] I can describe how to make a standard solution, weigh by difference, heat to constant mass, obtain concordant titres and take extra readings near an inflexion point.
- [ ] I can calculate means, percentages and processed values such as 1/t, and plot a graph of y against x with suitable scales.
- [ ] I can find a gradient and an intercept from a graph and give their units.
- [ ] I can calculate the percentage error in a measurement and a final result.
- [ ] I can identify and deal with anomalies and say whether the data support a conclusion.
- [ ] I can evaluate a method (replication, range, control of variables, instrument precision) and suggest specific improvements, using reliability and accuracy correctly.
:::

:::recap
- Paper 5: 1 h 15 min, 30 marks, no laboratory, at least 12 marks for planning and 12 for analysis, conclusion and evaluation, 6 variable. About 2.5 minutes a mark.
- Independent variable is changed, dependent variable is measured, control variables are kept constant (name, unit, value, how). A prediction gives direction and a reason.
- A plan: aim, variables, apparatus, quantities (checked by calculation), ordered steps, controls, hazard with its own precaution, table with units, processing. Control experiment only if relevant.
- Uncertainty of one reading is half the smallest division (burette ±0.05 cm³, thermometer ±0.5 °C, balance ±0.005 g); two readings double it. Percentage error = uncertainty / value × 100; for a result, add the percentages.
- Rate ∝ 1/t for the same amount of change. Graph of y = mx + c: gradient = Δy / Δx with unit; use two points more than half the line apart.
- Anomalies are identified, explained and left out of means and lines (not deleted). Replicates improve reliability; systematic errors affect accuracy; never write "human error".
- A good evaluation: weakness, effect, specific improvement.
:::

:::links
- read: [Orders of reaction and rate equations](https://www.chemguide.co.uk/physical/basicrates/orders.html) · Chemguide · how rates and orders are found from graphs, useful for the data analysis questions
- read: [Chemguide: CIE A level chemistry support](https://www.chemguideforcie.co.uk/index.html) · Chemguide · notes written for the Cambridge syllabus, including calculation topics
- papers: [Cambridge International 9701 past papers](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-chemistry-9701/past-papers/) · Cambridge International · the board's own page for past papers and mark schemes; practise Paper 5 under timed conditions
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 24 October 2026.
:::

Next: [Paper 1 survival guide: multiple choice](#chem.exam.p1) begins the guides to each exam paper.
