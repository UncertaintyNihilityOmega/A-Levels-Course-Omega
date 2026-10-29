@chapter bio.limiting
@title Limiting factors in photosynthesis
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 3–4 hours
@summary Light intensity, carbon dioxide concentration and temperature can each limit the rate of photosynthesis. You will learn how to read a limiting-factor graph and explain each part in terms of the two stages, how to calculate light intensity from a lamp distance, how to investigate the rate with a suspension of chloroplasts and DCPIP and with whole pondweed plants, and how a grower uses the idea in a glasshouse.

:::why
A plant in a field is almost never working at its best: some factor, often one you cannot see, is holding the rate down. Knowing which factor is limiting tells a grower what to change, and tells an examiner whether you understand the two stages of photosynthesis. Questions give you a graph or a table and ask you to name the limiting factor and explain it, to plan an investigation, or to analyse results from one.
:::

**Before you start**, you should know the light-dependent stage and the Calvin cycle from [Photosynthesis](#bio.photosynthesis), the effect of temperature on enzymes from [Enzymes](#bio.enzymes), and the redox indicators DCPIP and methylene blue from [Anaerobic respiration and investigating respiration](#bio.anaerobic).

:::try Warm-up
Q: Name the two products of the light-dependent stage that are used in the Calvin cycle. (from [Photosynthesis](#bio.photosynthesis))
A: ATP and reduced NADP.
Q: Which enzyme fixes carbon dioxide in the Calvin cycle, and which 5C compound does the carbon dioxide combine with? (from [Photosynthesis](#bio.photosynthesis))
A: Rubisco; ribulose bisphosphate (RuBP).
Q: Why does the rate of an enzyme reaction fall steeply above the optimum temperature? (from [Enzymes](#bio.enzymes))
A: Hydrogen bonds and ionic bonds in the enzyme break, so the shape of the active site changes and fewer enzyme–substrate complexes form: the enzyme is denatured.
:::

## What is a limiting factor?

A chain of events can go no faster than its slowest link. Photosynthesis is a chain of many steps, and several things must be present for it to run: light, carbon dioxide, water, suitable temperature, chlorophyll and minerals. At any moment one of them is in shortest supply, and that one sets the speed.

:::def Limiting factor
A variable that is in short supply, relative to what the plant could use, so that it limits the rate of a process. Increasing a limiting factor increases the rate; increasing any other factor does not.
:::

Three limiting factors are on the syllabus: **light intensity**, **carbon dioxide concentration** and **temperature**. Water, chlorophyll and minerals can also limit photosynthesis, but these three are the ones to learn.

:::key Reading a rate graph
1. Where the line is **rising**, the factor on the x-axis is the **limiting factor**.
2. Where the line is **flat**, the factor on the x-axis is **no longer limiting**. Something else is. Say what, and why.
3. Raising the right factor lifts the whole plateau; raising any other factor changes nothing.
:::

## Light intensity

Light supplies the energy for photoactivation in the light-dependent stage, so light intensity decides how much ATP and reduced NADP are made.

:::plot Rate of photosynthesis against light intensity at two carbon dioxide concentrations (25 °C). The curves coincide at low light intensity, then each levels off at its own maximum. Model curves, arbitrary units.
--f "(1.6*x+40-abs(1.6*x-40))/2" --f "(1.6*x+70-abs(1.6*x-70))/2" --label "0.04% CO₂" --label "0.12% CO₂" --x 0 100 --y 0 100 --xlabel "light intensity / arbitrary units" --ylabel "rate of photosynthesis / arbitrary units" --pt "12,19.2,light is limiting@se" --pt "80,40,CO₂ is limiting@s" --legend tr --alt "Two curves start together at the origin and rise in a straight line. The lower curve, at 0.04 percent carbon dioxide, levels off at a rate of 40 from a light intensity of 25. The upper curve, at 0.12 percent carbon dioxide, rises on the same line to a rate of 70 at a light intensity of about 44 and then levels off."
:::

- **At low light intensity** the rate rises steeply and in proportion to light intensity. Light is the limiting factor. More light means more photoactivation, so more ATP and reduced NADP are made, and the Calvin cycle can fix more carbon dioxide. At these low intensities, changing the carbon dioxide concentration makes no difference, so the two curves lie on top of each other.
- **At high light intensity** the curve levels off. More light does not raise the rate, because light is no longer limiting: the Calvin cycle cannot use ATP and reduced NADP any faster. Now **carbon dioxide concentration** (or temperature) is limiting, and a higher carbon dioxide concentration lifts the plateau.
- Notice that photosynthesis has not stopped at the plateau. It is running at its **maximum rate** for those conditions.

:::note The compensation point
A plant respires all the time, using oxygen and releasing carbon dioxide. In very dim light photosynthesis is slower than respiration, so there is a net release of carbon dioxide. The **compensation point** is the light intensity at which the rate of photosynthesis exactly equals the rate of respiration, so there is no net exchange of gases. Gas measurements, such as oxygen given off by pondweed, measure the **net** rate: net = gross photosynthesis − respiration.
:::

## Carbon dioxide concentration

Carbon dioxide is the substrate for rubisco. Air contains about 0.04% carbon dioxide, which is low enough that it often limits the rate.

:::plot Rate of photosynthesis against carbon dioxide concentration in bright light and in dim light (25 °C). In dim light the rate levels off at a low value, because light is limiting. Model curves, arbitrary units.
--f "112*x/(x+0.072)" --f "(24+112*x/(x+0.072)-abs(24-112*x/(x+0.072)))/2" --label "bright light" --label "dim light" --x 0 0.16 --y 0 110 --xlabel "carbon dioxide / %" --ylabel "rate of photosynthesis / arbitrary units" --pt "0.04,40,CO₂ is limiting@se" --pt "0.12,24,light is limiting@s" --legend tr --alt "Two curves start at the origin. The bright-light curve rises steeply and then more slowly to about 77 at 0.16 percent carbon dioxide. The dim-light curve follows the same line up to a rate of 24 at about 0.02 percent carbon dioxide and then stays flat at 24."
:::

- **In bright light**, the rate rises as carbon dioxide concentration rises. More carbon dioxide molecules collide with rubisco active sites, so more carbon dioxide is fixed, more GP is made and more of the ATP and reduced NADP is used. Carbon dioxide is the limiting factor. The curve flattens at high concentrations because rubisco is saturated or another factor takes over.
- **In dim light**, the rate levels off at a low value even though carbon dioxide is plentiful. Light is limiting: there is too little ATP and reduced NADP to use more carbon dioxide.

Carbon dioxide enters a leaf through open stomata (see [Plant tissues and water transport](#bio.planttransport)). On a hot dry day the stomata close to save water, and carbon dioxide can become the limiting factor even in bright light.

## Temperature

The light-dependent stage is affected little by temperature: absorbing a photon and raising an electron to a higher energy level does not need molecules to collide. The Calvin cycle, however, is a series of **enzyme-controlled reactions**, so temperature changes its rate.

:::plot Rate of photosynthesis against temperature in bright light and in dim light (carbon dioxide at 0.12%). In bright light the rate rises, peaks and falls; in dim light it is limited by light over a wide range of temperature. Model curves, arbitrary units.
--f "70*(2**(x/10)/(1+exp((x-35)/2.5)))/5.555+0*sqrt(42-x)" --f "(24+70*(2**(x/10)/(1+exp((x-35)/2.5)))/5.555-abs(24-70*(2**(x/10)/(1+exp((x-35)/2.5)))/5.555))/2+0*sqrt(42-x)" --label "bright light" --label "dim light" --x 0 50 --y 0 110 --xlabel "temperature / °C" --ylabel "rate of photosynthesis / arbitrary units" --pt "31,89.9,optimum near 31 °C@w" --legend tr --alt "In bright light the rate rises from about 18 at 5 degrees Celsius to a peak of about 90 near 31 degrees, then falls steeply to about 13 by 42 degrees, where the curve stops. In dim light the rate is flat at 24 from about 9 to 40 degrees and is lower only at the extremes."
:::

- **Below the optimum** (bright light), raising the temperature raises the rate. Enzyme and substrate molecules have more kinetic energy, so there are more collisions and more enzyme–substrate complexes, including rubisco with carbon dioxide and RuBP. The Calvin cycle runs faster and temperature is limiting.
- **Above the optimum**, the rate falls steeply. Hydrogen bonds and ionic bonds in the enzymes break, the active sites change shape, and the enzymes (including rubisco) are denatured. There are fewer enzyme–substrate complexes, so less carbon dioxide is fixed.
- **In dim light** the rate hardly changes with temperature, because light is limiting; temperature matters only at the extremes, where cold slows or heat denatures the enzymes enough to become the limiting factor.

:::warn Three tempting mistakes
1. **"Temperature affects the light-dependent stage most."** Absorbing light does not depend on temperature. Temperature matters through the *enzymes* of the Calvin cycle.
2. **"At the plateau photosynthesis has stopped."** It is at its maximum rate for those conditions; another factor is limiting.
3. **"More light always means a faster rate."** Only while light is the limiting factor. Beyond the plateau, extra light does not help.
:::

Try it: drag the marker along the light axis, then change the carbon dioxide concentration and the temperature. Watch the maximum rate move, and read which factor is limiting at the marker.

:::html
<div class="widget" data-w="bio-limiting" data-co2="0.04" data-temp="25"></div>
:::

## Finding the limiting factor from a graph

:::plot Rate of photosynthesis against light intensity at 15 °C and 25 °C, with carbon dioxide at 0.12% in both. Points A, B and C are marked. Model curves, arbitrary units.
--f "(1.6*x+36-abs(1.6*x-36))/2" --f "(1.6*x+70-abs(1.6*x-70))/2" --label "15 °C" --label "25 °C" --x 0 100 --y 0 100 --xlabel "light intensity / arbitrary units" --ylabel "rate of photosynthesis / arbitrary units" --pt "20,32,A@nw" --pt "70,36,B@s" --pt "70,70,C@n" --legend tr --alt "Two curves rise together in a straight line from the origin. The 15 degree curve levels off at a rate of 36 from a light intensity of about 22. The 25 degree curve rises to 70 at a light intensity of about 44 and then levels off. Point A is on the rising part of both curves at light intensity 20, point B is on the flat part of the 15 degree curve and point C is on the flat part of the 25 degree curve."
:::

:::eg The graph above shows the rate of photosynthesis at two temperatures. Name the factor that is limiting the rate at points A, B and C, and explain each.
Look first at where each point sits: on a rising part or on a flat part of the line.

At A the curve is rising, and both temperatures give the same rate, so light intensity is the limiting factor: more light would mean more photoactivation, ATP and reduced NADP. [B1]

At B the 15 °C curve is flat, so light is not limiting. The 25 °C curve is higher at the same light intensity, so temperature is the limiting factor: at 15 °C the enzymes of the Calvin cycle have less kinetic energy, so fewer enzyme–substrate complexes form. [B1]

At C the curve is flat, so light is not limiting. Carbon dioxide concentration (0.12% is below the level at which rubisco is saturated) or temperature (25 °C is still below the optimum) is limiting. [B1]

A weaker answer says "light is limiting at all three points because the graph is about light". It does not look at whether the line is rising or flat at each point, so it scores no more than one mark.
:::

### Which factor is limiting? A sequence of experiments

A grower can test which factor limits a crop by changing **one factor at a time** and watching the rate. If raising a factor raises the rate, it was limiting; if the rate does not change, it was not. Because factors interact, the same factor may be limiting in one set of conditions and not in another.

## Light intensity and the inverse square law

Light from a lamp spreads out in all directions. At twice the distance, the same light is spread over four times the area, so each square centimetre receives a quarter of the light.

:::formula Light intensity and distance
\[I \propto \frac{1}{d^2}\]
- \(I\) is the light intensity at the plant; \(d\) is the distance from the lamp to the plant.
- Doubling the distance gives \(\tfrac14\) of the intensity; tripling it gives \(\tfrac19\).
- To compare two distances: \(\dfrac{I_2}{I_1} = \left(\dfrac{d_1}{d_2}\right)^2\).
:::

:::eg A lamp 10 cm from a plant gives a light intensity of 100 arbitrary units. Calculate the light intensity at 20 cm and at 40 cm.
Use \(I_2 = I_1 \times (d_1 \div d_2)^2\).

\[\begin{aligned} I_{20} &= 100 \times \left(\frac{10}{20}\right)^2 \\ &= 100 \times 0.25 \\ &= 25 \end{aligned}\]

The method uses the inverse square law. [M1] The intensity at 20 cm is 25 arbitrary units. [A1]

\[\begin{aligned} I_{40} &= 100 \times \left(\frac{10}{40}\right)^2 \\ &= 6.25 \end{aligned}\]

The intensity at 40 cm is 6.25 arbitrary units. [A1]

The distance doubled from 20 cm to 40 cm and the intensity fell to a quarter (25 to 6.25), as the law predicts.
:::

:::warn Where the law fails
The law holds for a small bright lamp in a dark room. A lamp that is not a point source, light reflected from walls and windows, and a lamp that heats the water all spoil the result. Measure the intensity with a light meter if you can, and use a heat shield and a darkened room.
:::

## Investigating with a suspension of chloroplasts

Chloroplasts separated from leaf cells can still carry out the light-dependent stage (many are broken while the leaves are ground and lose the stroma enzymes of the Calvin cycle). We can still measure how fast the light-dependent stage runs if something takes the electrons in place of NADP. The redox indicator **DCPIP** does this.

DCPIP is **blue when oxidised and colourless when reduced**. When chloroplasts are lit, electrons are released from photoactivated chlorophyll, and DCPIP accepts them (and hydrogen) instead of NADP. The blue colour fades, and the faster the electrons are released, the faster it fades. Methylene blue can be used in the same way. (This is the same use of a redox indicator as in [Anaerobic respiration and investigating respiration](#bio.anaerobic), but here the electrons come from light, not from respiration.)

\[\text{rate of the light-dependent stage} \propto \frac{1}{\text{time for DCPIP to turn colourless}}\]

:::lab Effect of light intensity or light wavelength on the light-dependent stage, using chloroplasts and DCPIP
**Aim**: find how light intensity (or colour) affects the rate at which isolated chloroplasts reduce DCPIP.

:::steps
1. Grind fresh leaves (spinach) in **ice-cold isotonic buffer** in a chilled mortar, filter through muslin, and keep the chloroplast suspension on ice and in the dark.
2. Put a fixed volume of buffer, DCPIP solution and chloroplast suspension in a tube, mix, and stand it in a beaker of water (or a water tank) at a fixed distance from a lamp.
3. Start the stopwatch. Record the **time for the DCPIP to turn from blue to colourless**, or read the absorbance in a colorimeter (with a red filter) every minute and calculate the fall per minute.
4. **Light intensity**: repeat with the lamp at several distances (for example 10, 20, 30, 40, 50 cm) and work out the relative intensity as \(1/d^2\).
5. **Wavelength**: repeat at one distance with coloured filters (red, green, blue) between the lamp and the tube.
6. Repeat each condition three times and calculate the mean rate (\(1/t\) or absorbance change per minute).
:::

**Variables**: the independent variable is the light intensity (lamp distance) or the colour of the filter; the dependent variable is the time to decolourise (or the fall in absorbance). Standardise the volumes and concentrations of DCPIP and chloroplast suspension (the same batch), the temperature (a water tank as heat shield), the pH (buffer), and, for the wavelength investigation, the light intensity behind each filter.

**Controls**: (1) a tube wrapped in foil: no colour change shows that light is needed; (2) DCPIP and buffer without chloroplasts in the light: no change shows the chloroplasts are needed; (3) boiled chloroplasts: no change shows the reaction depends on intact, working chloroplasts. A tube of chloroplasts without DCPIP can be used to set the colorimeter to zero.

**Why the suspension is made as it is**: the buffer keeps the pH constant; it is **isotonic** (the same water potential as the chloroplasts) so they do not burst or shrink by osmosis; it is **ice-cold** to slow enzymes that would damage the chloroplasts and keep them working.

**Typical results**: the DCPIP fades faster close to the lamp, but not in proportion to the intensity at short distances. With filters, red and blue light are fast and green is slow, as in the action spectrum.

**Sources of error**: judging the end point by eye (use a colorimeter or a colour standard); filters transmit different amounts of light; the lamp warms the tube (use a heat shield); chloroplasts lose activity over time (use the suspension within an hour or so).

**Safety**: mains electricity near water (keep the socket and lamp dry); the lamp gets hot; DCPIP stains skin and clothes (wear gloves and eye protection).
:::

:::eg A chloroplast suspension was mixed with DCPIP and placed 10 cm or 30 cm from a lamp. Absorbance was read in a colorimeter with a red filter. Calculate the initial rate at each distance, and explain why the rate at 30 cm is not one-ninth of the rate at 10 cm.
Absorbance measures the blue colour of DCPIP, so a falling absorbance means DCPIP is being reduced.

| time / min | absorbance, lamp 10 cm | absorbance, lamp 30 cm |
|---|---|---|
| 0 | 0.82 | 0.82 |
| 1 | 0.66 | 0.77 |
| 2 | 0.51 | 0.72 |
| 3 | 0.38 | 0.68 |
| 4 | 0.30 | 0.63 |
| 5 | 0.24 | 0.59 |

**Initial rate** = fall in absorbance ÷ time, over the first 2 minutes, where the line is nearly straight. [M1]

\[\begin{aligned} \text{rate at 10 cm} &= \frac{0.82 - 0.51}{2} = 0.155\ \text{min}^{-1} \\ \text{rate at 30 cm} &= \frac{0.82 - 0.72}{2} = 0.050\ \text{min}^{-1} \end{aligned}\]

The rates are 0.155 and 0.050 absorbance units per minute. [A1]

**Explain.** The light intensity at 30 cm is \((10 \div 30)^2 = \tfrac19\) of that at 10 cm, but the rate is about one-third (0.050 ÷ 0.155 = 0.32) of the rate at 10 cm. [B1]

At 10 cm light is so intense that it is no longer the only limiting factor; another factor, such as the concentration of DCPIP or of chloroplasts, limits the rate. [B1]

At 30 cm there is less light, so fewer electrons are released from photoactivated chlorophyll and DCPIP is reduced more slowly. [B1]

A weaker answer says "the rate is lower because the light is weaker". It does not compare the rate ratio with the intensity ratio, so it never sees that the two are not proportional.
:::

## Investigating with whole plants

Aquatic plants such as pondweed (*Elodea* or *Cabomba*) are used because the gas they give off, mostly oxygen, appears as bubbles at the cut end of the stem.

<figure class="fig small"><svg viewBox="0 0 380 292" role="img" aria-label="Apparatus for investigating photosynthesis in pondweed. A lamp on a stand shines through a tank of water that acts as a heat shield onto a beaker of sodium hydrogencarbonate solution. In the beaker, pondweed lies under an inverted funnel whose stem leads into a test tube, where the gas given off collects. A thermometer is in the beaker. The distance d from the lamp to the beaker is the measured light variable."><circle class="fh s-mute sw2" cx="44" cy="120" r="16"/><path class="ln" d="M44 136L44 200"/><path class="ln" d="M28 200L60 200"/><text class="tl" x="44" y="92" text-anchor="middle">lamp</text><path class="c4 sw2 dash" d="M64 108L92 108" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M118 108L146 108" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M64 120L92 120" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M118 120L146 120" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M64 132L92 132" marker-end="url(#ah)"/><path class="c4 sw2 dash" d="M118 132L146 132" marker-end="url(#ah)"/><rect class="f2 s-acc2 sw2" x="96" y="76" width="16" height="130"/><text class="tl" x="104" y="226" text-anchor="middle">heat shield</text><text class="tl" x="104" y="242" text-anchor="middle">(water tank)</text><path class="ln" d="M150 66L150 96"/><path class="ln" d="M260 66L260 96"/><rect class="f2 s-acc2 sw2" x="150" y="96" width="110" height="110"/><rect class="fp ln" x="156" y="74" width="8" height="112"/><circle class="fa s-acc sw2" cx="160" cy="190" r="6"/><text class="tl" x="186" y="54" text-anchor="end">thermometer</text><path class="ln-m thin" d="M166 58L160 76"/><path class="fp ln" d="M172 196L238 196L215 140L215 120L195 120L195 140Z"/><path class="ln" d="M190 138L190 66L194 62L216 62L220 66L220 138"/><rect class="fp s-acc sw2" x="192" y="64" width="26" height="22"/><path class="c2 sw2" d="M190 194L186 172L192 160"/><path class="c2 sw2" d="M205 194L208 174L202 160"/><path class="c2 sw2" d="M221 194L226 174L219 162"/><circle class="fp s-acc sw2" cx="205" cy="150" r="2.5"/><circle class="fp s-acc sw2" cx="209" cy="140" r="2.5"/><circle class="fp s-acc sw2" cx="204" cy="130" r="2.5"/><text class="tl" x="272" y="46">gas collects</text><path class="ln-m thin" d="M268 50L218 72"/><text class="tl" x="272" y="112">inverted funnel</text><path class="ln-m thin" d="M268 118L228 168"/><text class="tl" x="272" y="196">pondweed</text><path class="ln-m thin" d="M268 192L224 184"/><text class="tl" x="160" y="262">sodium hydrogencarbonate</text><text class="tl" x="160" y="278">solution in a beaker</text><path class="c1 sw2" d="M86 262L44 262" marker-end="url(#ah)"/><path class="c1 sw2" d="M110 262L150 262" marker-end="url(#ah)"/><text class="tl tb" x="98" y="267" text-anchor="middle">d</text><path class="ln-m thin" d="M44 254L44 270"/><path class="ln-m thin" d="M150 254L150 270"/></svg><figcaption>Pondweed (Elodea) apparatus. The gas collected is mostly oxygen. The lamp distance d sets the light intensity, the sodium hydrogencarbonate sets the carbon dioxide available, and a water bath or the water tank keeps the temperature steady.</figcaption></figure>

:::lab The effect of light intensity, carbon dioxide concentration or temperature on the rate of photosynthesis of pondweed
**Aim**: measure the rate of oxygen production by pondweed while one factor is changed.

:::steps
1. Cut a piece of pondweed about 10 cm long and put it, cut end up, under an inverted funnel in a beaker of sodium hydrogencarbonate solution, as in the figure.
2. Put a test tube of the solution over the funnel stem, or attach a capillary tube or gas syringe, to collect the gas.
3. Set the factor you are investigating: **light intensity** (distance \(d\) from the lamp), **carbon dioxide concentration** (concentration of sodium hydrogencarbonate solution, which gives off carbon dioxide), or **temperature** (a water bath; check with a thermometer).
4. **Leave the plant for 5 minutes** after each change to adjust to the new conditions.
5. Count the **bubbles per minute**, or measure the **length of the gas bubble** collected in a capillary tube in 5 minutes.
6. Repeat three times for each value, calculate the mean rate, and plot rate against the factor.
:::

**Variables**: the independent variable is one of light intensity, carbon dioxide concentration or temperature; the dependent variable is the rate of gas production. Standardise the other two factors, and use the same piece of pondweed (length, mass and cut) and the same volume of solution.

- **Light**: lamp distance, with a **heat shield** (a tank of water) so that the lamp does not change the temperature; darken the room.
- **Carbon dioxide**: use a fresh sodium hydrogencarbonate solution of each concentration (for example 0, 0.02, 0.04, 0.06, 0.08 and 0.10 mol dm⁻³, made by diluting a stock solution) so that carbon dioxide is not used up.
- **Temperature**: a water bath with a thermometer, with light and carbon dioxide kept high enough that they do not limit the rate.

**Control**: boiled pondweed, or no pondweed, or the lamp switched off: no gas shows the gas comes from photosynthesis.

**Measuring more accurately**: bubble counting is only an estimate, because bubbles vary in size and some dissolve or stick to the plant. In a capillary tube of radius \(r\), a column of gas of length \(l\) has volume \(\pi r^2 l\), which is a better measure.

**Sources of error**: bubble size varies; the plant respires and uses some of the oxygen (the rate is *net*); the lamp warms the water; the plant has not adjusted to a new condition; carbon dioxide runs out of the solution.

**Safety**: mains electricity near water: keep the socket and lamp dry, wipe up spills, and switch off before moving anything. Risk: low if this is done.
:::

:::eg Plan an investigation to find the effect of carbon dioxide concentration on the rate of photosynthesis of pondweed.
A full-mark plan covers prediction, variables, method, repeats, control and safety, one point per mark.

Prediction: as the carbon dioxide concentration increases, the rate increases and then levels off, because carbon dioxide is the substrate of rubisco and is limiting at first. [B1]

Independent variable: concentration of sodium hydrogencarbonate solution, at least five concentrations (for example 0.00 to 0.10 mol dm⁻³), made by diluting a stock solution with distilled water. [B1]

Dependent variable: rate of photosynthesis, measured as the number of bubbles per minute (or the volume of gas collected in a capillary tube in 5 minutes). [B1]

Standardise light intensity: the same distance from the lamp, with a heat shield between them. [B1]

Standardise temperature: a water bath at a fixed temperature (for example 25 °C), checked with a thermometer. [B1]

Standardise the plant and volume: the same length and mass of pondweed (from the same plant) and the same volume of solution. [B1]

Leave the pondweed for 5 minutes in each new solution before counting; repeat at least three times at each concentration and calculate the mean. A control with boiled pondweed (or no pondweed) shows the gas comes from photosynthesis. [B1]

Safety: keep the lamp and mains sockets away from water. [B1]

A weaker plan says "put pondweed in water and count bubbles at different carbon dioxide". It gives no values, no standardised variables, no repeats and no way to vary carbon dioxide, so it scores at most two marks.
:::

:::exam Paper 5 and planning
In a planning question, name the independent variable and how you will change it, the dependent variable and how you will measure it, the key variables to keep the same and how, a control, repeats, and a risk. See [Planning investigations (Paper 5)](#bio.planning) for the full method, and write the measurements with units.
:::

## Limiting factors in the glasshouse

A glasshouse grower can control light, carbon dioxide and temperature, so can raise the rate of photosynthesis and the crop yield. But every change costs money, and there is a point at which another factor limits, so extra input adds almost nothing.

- **Light**: artificial lamps extend the day in winter; glass lets in light and whitewash reduces glare in summer.
- **Carbon dioxide**: burn gas or paraffin in the glasshouse, or add carbon dioxide from cylinders.
- **Temperature**: heating in winter; vents and shading in summer. Do not overheat: above the optimum, enzymes denature.

:::eg Real context, a tomato glasshouse: a grower tested four carbon dioxide concentrations. Use the data to decide the most economical concentration.
Each tonne of tomatoes sells for $500. The cost of the carbon dioxide is per hectare per year.

| CO₂ / % | yield / tonnes per hectare | cost of CO₂ / $ per hectare |
|---|---|---|
| 0.04 | 80 | 0 |
| 0.08 | 92 | 1500 |
| 0.12 | 98 | 3200 |
| 0.16 | 99 | 5000 |

For each step, compare the value of the extra yield with the extra cost. [M1]

From 0.04% to 0.08%: extra yield \(12 \times 500 = \$6000\); extra cost $1500; net gain $4500. [A1]

From 0.08% to 0.12%: extra yield \(6 \times 500 = \$3000\); extra cost \(3200 - 1500 = \$1700\); net gain $1300. [A1]

From 0.12% to 0.16%: extra yield \(1 \times 500 = \$500\); extra cost \(5000 - 3200 = \$1800\); net loss $1300. [A1]

The most economical concentration is 0.12%, because the next step costs more than the extra tomatoes are worth. [B1]

The gains get smaller because, as carbon dioxide rises, another factor (light, temperature, or rubisco itself being saturated) starts to limit the rate.
:::

:::eg Spot the error: explain why the rate of photosynthesis levels off as light intensity increases, with temperature and carbon dioxide concentration constant. [3]
A student wrote this answer.

Line 1: At low light intensity, light is the limiting factor, so the rate increases as light intensity increases.
Line 2: At the plateau, photosynthesis has stopped because all the chlorophyll is used up.
Line 3: Another factor, such as carbon dioxide concentration or temperature, is now limiting, so more light does not raise the rate.

Line 1 is correct [B1]. **Line 2 is wrong: at the plateau photosynthesis is going on at its maximum rate, and chlorophyll is not used up (it is not a reactant). The rate is level because the rest of the process, the Calvin cycle, cannot use ATP and reduced NADP any faster. That mark is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "At the plateau the rate is at its maximum for these conditions: the Calvin cycle cannot use the ATP and reduced NADP any faster." With that change the answer scores 3 marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State three limiting factors of photosynthesis.
A: Light intensity, carbon dioxide concentration and temperature.
Q: Explain why the rate of photosynthesis is proportional to light intensity at low light intensities.
A: Light is the limiting factor. More light means more photoactivation of chlorophyll, so more ATP and reduced NADP are made, and the Calvin cycle can fix carbon dioxide faster.
Q: On a curve of rate against light intensity at 0.04% carbon dioxide, the rate levels off. Name one factor that is limiting at the plateau and explain.
A: Carbon dioxide concentration. There is too little carbon dioxide for rubisco to fix, so the Calvin cycle cannot use more ATP and reduced NADP, and more light does not raise the rate. (Temperature is also acceptable.)
Q: A lamp 12 cm from a pond plant gives 100 arbitrary units of light. Calculate the intensity at 36 cm.
A: \(100 \times (12 \div 36)^2 = 100 \times \tfrac19 = 11\) arbitrary units (11.1).
Q: A tank of water is put between a lamp and a pondweed in a photosynthesis investigation. Explain why.
A: It absorbs the heat from the lamp, so the temperature of the pondweed does not change as the lamp is moved. Temperature is then a standardised variable and does not affect the rate.
Q: Explain why chloroplasts are kept in ice-cold isotonic buffer when they are isolated for a DCPIP investigation.
A: Isotonic: the same water potential as the chloroplasts, so they do not burst or shrink by osmosis. Ice-cold: slows enzymes that would damage them. Buffer: keeps the pH constant.
Q: In a capillary tube of radius 0.40 mm, pondweed gave a column of gas 18 mm long. Calculate the volume of gas.
A: \(\pi r^2 l = \pi \times 0.40^2 \times 18 = 9.0\ \mathrm{mm^3}\).
Q: In the DCPIP investigation, a tube is wrapped in foil. Explain the purpose of this tube.
A: It is a control. The chloroplasts get no light, so DCPIP should stay blue, which shows that light is needed to reduce DCPIP (not, for example, the chloroplasts or the buffer alone).
Q: Explain why counting bubbles is not an accurate measure of the rate of photosynthesis.
A: The bubbles vary in size, so the number is not proportional to the volume of oxygen. Some oxygen dissolves or sticks to the plant, and bubbles may be missed.
Q: A grower adds carbon dioxide to a glasshouse on a dark winter day and the rate of photosynthesis does not increase. Suggest why.
A: Light intensity (or temperature) is the limiting factor, so extra carbon dioxide cannot be used and the rate does not change.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State three ways in which a grower can increase the rate of photosynthesis of a crop in a glasshouse in winter.
A: Provide artificial lighting (to increase light intensity or day length). [B1]
Add carbon dioxide (increase its concentration). [B1]
Heat the glasshouse (raise the temperature, to near the optimum). [B1]
Q: [6 marks] ★★ The table shows the rate of photosynthesis of a plant at different temperatures in dim light and in bright light. (a) Describe the results. (b) Explain the results.

| temperature / °C | dim light / arbitrary units | bright light / arbitrary units |
|---|---|---|
| 10 | 10 | 14 |
| 20 | 12 | 33 |
| 30 | 12 | 62 |
| 40 | 12 | 41 |
| 50 | 4 | 5 |

H: Describe the shape of each column of figures, quoting peak values.
H: Which factor is limiting in dim light, and which in bright light below 30 °C?
A: (a) In bright light the rate increases from 14 at 10 °C to a maximum of 62 at 30 °C, then decreases to 5 at 50 °C. [B1]
In dim light the rate is almost constant at 10 to 12 units between 10 and 40 °C. [B1]
At 50 °C the rate falls to 4 in dim light and to 5 in bright light. [B1]
(b) In bright light below 30 °C temperature is limiting: more kinetic energy means more enzyme–substrate complexes in the Calvin cycle. [B1]
Above 30 °C the enzymes (such as rubisco) are denatured as bonds break and the active sites change shape. [B1]
In dim light, light is limiting, so changing the temperature has little effect (until denaturation at 50 °C). [B1]
Q: [4 marks] ★★ Pondweed was placed in a capillary tube apparatus. After 5 minutes the column of gas in the capillary tube, of radius 0.50 mm, was 12.0 mm long. (a) Calculate the volume of gas produced per minute. (b) Suggest why this is lower than the true rate of oxygen production by photosynthesis.
H: Volume \(= \pi r^2 l\). Divide by the time.
A: (a) Volume \(= \pi \times 0.50^2 \times 12.0\) [M1] \(= 9.4\ \mathrm{mm^3}\) [A1]
Rate \(= 9.4 \div 5 = 1.9\ \mathrm{mm^3\ min^{-1}}\) [A1]
(b) The plant respires, using some of the oxygen it produces, so the gas collected is the net amount. [B1]
(Also credit: some oxygen dissolves in the water.)
Q: [6 marks] ★★ A student measured the time for DCPIP to turn colourless with a suspension of chloroplasts, using coloured filters between the lamp and the tube.

| filter | time to turn colourless / s |
|---|---|
| none | 60 |
| red | 90 |
| blue | 75 |
| green | 420 |

(a) Calculate the rate of reaction with the green filter, as \(1/t\), in standard form. (b) Explain the differences between the filters. (c) Suggest why the rate with a red filter is lower than with no filter.
H: Rate \(= 1/t\) in \(\mathrm{s^{-1}}\).
H: Chlorophyll absorbs red and blue light much more than green.
A: (a) \(1 \div 420\) [M1] \(= 2.4 \times 10^{-3}\ \mathrm{s^{-1}}\) [A1]
(b) Chlorophyll absorbs red and blue light strongly, so there is more photoactivation and more electrons are released to reduce DCPIP; the rates are high. [B1]
Green light is mostly reflected or transmitted, so little energy is absorbed and the DCPIP is reduced slowly. [B1]
With no filter all wavelengths are available, including red and blue, so the time is shortest. [B1]
(c) The filter absorbs some of the light, so the light intensity reaching the chloroplasts is lower. [B1]
Q: [5 marks] ★★ The table shows the number of bubbles of gas released per minute by pondweed in solutions of different sodium hydrogencarbonate concentrations. (a) Describe the results. (b) Explain the results.

| sodium hydrogencarbonate / mol dm⁻³ | bubbles per minute |
|---|---|
| 0.00 | 2 |
| 0.02 | 12 |
| 0.04 | 21 |
| 0.06 | 29 |
| 0.08 | 30 |
| 0.10 | 30 |

A: (a) The rate increases from 2 bubbles per minute at 0.00 mol dm⁻³ to 29 at 0.06 mol dm⁻³. [B1]
Above 0.06 mol dm⁻³ the rate levels off at about 30 bubbles per minute. [B1]
(b) Sodium hydrogencarbonate supplies carbon dioxide, which is fixed by rubisco, so a higher concentration means more fixation and more oxygen produced. [B1]
At the plateau carbon dioxide is no longer limiting. [B1]
Another factor, such as light intensity or temperature, is now limiting the rate. [B1]
Q: [6 marks] (#bio.planning) ★★★ Plan an investigation, using a suspension of chloroplasts and DCPIP, to find the effect of light intensity on the rate of the light-dependent stage.
H: Say how you will change the light intensity and how you will calculate it.
H: Include a control, repeats and a risk.
A: Independent variable: light intensity, by placing the lamp at at least five distances (for example 10 to 50 cm), with relative intensity calculated as \(1/d^2\). [B1]
Dependent variable: time for DCPIP to turn from blue to colourless (or the fall in absorbance per minute in a colorimeter), converted to a rate as \(1/t\). [B1]
Standardise: the volumes and concentrations of DCPIP and chloroplast suspension (same batch), the temperature (a water tank as a heat shield), and the pH (buffer). [B1]
A control: a tube in the dark, wrapped in foil (or a tube without chloroplasts), to show that light and chloroplasts are needed. [B1]
Repeat each distance at least three times and calculate a mean rate; keep the chloroplasts ice-cold and isotonic between uses. [B1]
Risk: mains electricity near water, and a hot lamp; keep the socket dry, and use eye protection and gloves because DCPIP stains. [B1]
Q: [5 marks] (#bio.planttransport) ★★★ On a hot, dry, sunny day the rate of photosynthesis of a crop falls in the afternoon. Use your knowledge of stomata to suggest and explain a reason.
H: What do the guard cells do to save water, and what else cannot then enter the leaf?
A: The stomata close to reduce water loss by transpiration. [B1]
Carbon dioxide cannot diffuse into the leaf, so its concentration inside falls. [B1]
Carbon dioxide becomes the limiting factor, even though light is bright. [B1]
Less carbon dioxide is fixed by rubisco, so less GP and TP are made. [B1]
The ATP and reduced NADP from the light-dependent stage are not used up, so the light-dependent stage slows down. [B1]
Q: [5 marks] ★★★ The rate of photosynthesis of a crop was measured in bright light under four conditions.

| condition | rate / arbitrary units |
|---|---|
| A: 0.04% CO₂, 15 °C | 12 |
| B: 0.12% CO₂, 15 °C | 13 |
| C: 0.04% CO₂, 25 °C | 24 |
| D: 0.12% CO₂, 25 °C | 45 |

Deduce the limiting factor in conditions A and in C, and explain.
H: Compare A with B (change CO₂ only), and A with C (change temperature only).
H: Then compare C with D.
A: In A the limiting factor is temperature: raising the carbon dioxide concentration (A to B) hardly changes the rate (12 to 13). [B1]
Raising the temperature (A to C) doubles the rate (12 to 24), so temperature was limiting. [B1]
In C the limiting factor is carbon dioxide concentration: raising it (C to D) raises the rate from 24 to 45. [B1]
At 15 °C the enzymes of the Calvin cycle, including rubisco, have little kinetic energy, so fewer enzyme–substrate complexes form and extra carbon dioxide cannot be used. [B1]
At 25 °C rubisco is faster, so more carbon dioxide can be fixed and carbon dioxide becomes the limit. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A pondweed's net uptake of carbon dioxide was measured at different light intensities.

| light intensity / arbitrary units | net uptake of CO₂ / cm³ per hour |
|---|---|
| 0 | −2.0 |
| 10 | −1.0 |
| 20 | 0.0 |
| 30 | 1.0 |
| 40 | 2.0 |

(a) State the compensation point and explain what it means. (b) Explain why the net uptake is negative at 0. (c) Calculate the rate of photosynthesis (gross) at a light intensity of 40.
H: A negative net uptake means carbon dioxide is released.
H: Gross photosynthesis = net uptake + respiration.
A: (a) The compensation point is 20 arbitrary units. [B1]
At this light intensity the rate of photosynthesis equals the rate of respiration, so there is no net exchange of carbon dioxide. [B1]
(b) In the dark there is no photosynthesis, but the plant still respires and releases carbon dioxide. [B1]
(c) Respiration releases 2.0 cm³ per hour, so gross \(= 2.0 + 2.0\) [M1] \(= 4.0\ \mathrm{cm^3\ h^{-1}}\) [A1]
Q: [5 marks] ★★★ Unicellular algae are grown in a large, clear tank in bright light. The rate of photosynthesis per cell is higher when the tank is stirred and when sodium hydrogencarbonate is added. The rate per cell is lower when the algae are very dense. Suggest explanations for these three observations.
H: Think about which factor each change affects.
A: Stirring brings cells to the surface in turn and mixes carbon dioxide through the tank, so no cell is long in the dark or in a region short of carbon dioxide. [B1]
Sodium hydrogencarbonate supplies carbon dioxide, which is limiting; more carbon dioxide means more fixation by rubisco. [B1]
When the algae are dense they shade each other, so cells in the middle receive a lower light intensity. [B1]
Light is then the limiting factor for these cells, so less ATP and reduced NADP is made. [B1]
Dense cells may also use up the available carbon dioxide faster, so it becomes limiting. [B1]
:::

:::quiz
? Which statement describes a limiting factor?
+ the factor in shortest supply, which limits the rate until it is increased
- the factor that has the highest value at the optimum
- any factor that affects the rate of photosynthesis
- the factor that reaches its maximum first
> A limiting factor limits the rate: increasing it raises the rate, while increasing any other factor does not. A factor can affect the rate without limiting it at that moment.
? On the rising part of a curve of rate against light intensity, which factor is limiting?
+ light intensity
- carbon dioxide concentration
- temperature
- water
> On the rising part the factor on the x-axis is limiting: more light means more ATP and reduced NADP and a faster rate. The other factors take over at the plateau.
? What is happening to photosynthesis at the plateau of a light intensity curve?
+ it is at its maximum rate for those conditions, limited by another factor
- it has stopped because all the chlorophyll is used up
- it has stopped because the enzymes are denatured
- it continues to rise but too slowly to see
> The rate is constant at its maximum, because light is no longer limiting. Chlorophyll is not a reactant and is not used up.
? Why does temperature affect the rate of photosynthesis in bright light?
+ the enzymes of the Calvin cycle are affected by temperature
- light cannot be absorbed at low temperatures
- chlorophyll is destroyed at low temperatures
- water cannot enter the leaf at high temperatures
> The light-dependent absorption of light does not need collisions. The Calvin cycle is catalysed by enzymes, so its rate depends on kinetic energy and denaturation.
? A lamp is moved from 30 cm to 15 cm from a plant. What happens to the light intensity at the plant?
+ it rises to four times its value
- it doubles
- it falls to one quarter
- it rises to sixteen times its value
> Intensity is proportional to 1/d², and \((30 \div 15)^2 = 4\). Doubling would be a direct proportion with distance, one quarter has the ratio upside down, and sixteen squares the ratio twice.
? What is the purpose of DCPIP in an investigation with isolated chloroplasts?
+ it accepts electrons from the light-dependent stage and changes from blue to colourless
- it supplies carbon dioxide to the chloroplasts
- it absorbs the light so the chloroplasts are not damaged
- it is the substrate of rubisco
> DCPIP takes the electrons in place of NADP. The time it takes to become colourless shows the rate of the light-dependent stage. No carbon dioxide is supplied or measured in this investigation.
? Why is pondweed placed behind a tank of water when it is lit by a lamp?
+ the water absorbs heat, so temperature does not change as the lamp is moved
- the water provides carbon dioxide for the plant
- the water increases the light intensity
- the water filters out green light
> The tank is a heat shield. If the lamp warmed the pondweed, temperature would be a second variable and might affect the rate.
? Pondweed produces 2.0 mm³ min⁻¹ of oxygen measured by gas collection, but respires using 0.5 mm³ min⁻¹. What is the rate of photosynthesis (gross)?
+ 2.5 mm³ min⁻¹
- 1.5 mm³ min⁻¹
- 2.0 mm³ min⁻¹
- 4.0 mm³ min⁻¹
> The gas collected is the net amount: net = gross − respiration. So gross = 2.0 + 0.5 = 2.5 mm³ min⁻¹.
? In a glasshouse, a grower raises the carbon dioxide concentration but the yield does not increase. What is the most likely reason?
+ another factor, such as light intensity or temperature, is now limiting
- carbon dioxide is toxic to the plants at this concentration
- the Calvin cycle has stopped
- the rate of respiration has risen above the rate of photosynthesis
> Raising a factor that is not limiting changes nothing. The grower should find which factor is limiting and raise that.
:::

:::checklist What you can now do
- [ ] I can state that light intensity, carbon dioxide concentration and temperature are limiting factors of photosynthesis, and define a limiting factor.
- [ ] I can explain the effects of changes in light intensity, carbon dioxide concentration and temperature on the rate of photosynthesis, in terms of the two stages.
- [ ] I can read a rate graph, say which factor is limiting at each point, and explain why.
- [ ] I can calculate relative light intensity from the distance of a lamp, using the inverse square law.
- [ ] I can describe and carry out an investigation with DCPIP (or methylene blue) and a suspension of chloroplasts to find the effect of light intensity or wavelength.
- [ ] I can describe and carry out an investigation with whole plants, including aquatic plants, to find the effect of light intensity, carbon dioxide concentration or temperature.
- [ ] I can plan such an investigation, with variables, a control, repeats and a risk assessment.
- [ ] I can use limiting factors to decide how to improve the yield in a glasshouse, weighing cost against yield.
:::

:::recap
- A limiting factor is the factor in shortest supply: increasing it raises the rate. On a graph it is the x-axis factor where the line is rising; at a plateau another factor limits.
- Light intensity: supplies energy for ATP and reduced NADP; rate proportional to intensity at low light. Carbon dioxide: substrate for rubisco. Temperature: affects the enzymes of the Calvin cycle; denaturation above the optimum.
- At the plateau photosynthesis is at its maximum rate, not stopped. At low light intensity, temperature and carbon dioxide have little effect.
- Light intensity \(\propto 1/d^2\): doubling the distance gives one quarter.
- DCPIP: blue when oxidised, colourless when reduced; accepts electrons from the light-dependent stage. Chloroplasts: ice-cold, isotonic, buffered; controls with dark and with no chloroplasts.
- Whole plants (pondweed): count bubbles or measure gas in a capillary tube (\(\pi r^2 l\)); heat shield; sodium hydrogencarbonate for carbon dioxide; leave to adjust. The rate measured is net.
- In a glasshouse, raise the limiting factor until another limits or the cost exceeds the extra yield.
:::

:::links
- read: [CAIE A Level Biology: photosynthesis notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/photosynthesis/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Photosynthesis (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/13-photosynthesis/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of photosynthesis and its rate
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · planning and analysis questions on photosynthesis in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Homeostasis and the kidney](#bio.homeostasis) looks at how the body keeps its internal environment steady.
