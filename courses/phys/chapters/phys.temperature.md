@chapter phys.temperature
@title Temperature
@level a2
@paper CAIE P4 (A Level) · P5
@time 3–5 hours
@summary What temperature really measures and how it differs from thermal energy, how thermometers work and why the thermodynamic scale starts at absolute zero, and how to calculate the energy needed to warm a substance (specific heat capacity) or to melt or boil it (specific latent heat), with the experiments that measure both.

:::why
A kettle, a fridge, a car engine and a human body all work because energy moves from where it is hot to where it is cold. To design or understand any of them you need two things: a scale that says how hot something is, and a way to calculate how much energy it takes to change that. This chapter gives you both, and the same ideas explain why a cup of tea cools in minutes while a swimming pool barely changes in a day.
:::

**Before you start**, you need power and energy from [Work, energy and power](#phys.energy), and resistance and the thermistor from [Electricity](#phys.electricity).

:::try Warm-up
Q: A 3.0 kW heater is switched on for 2.0 minutes. How much energy does it transfer? (from [Work, energy and power](#phys.energy))
A: \(E = Pt = 3000 \times 120 = 3.6 \times 10^{5}\,\mathrm{J}\). Change minutes into seconds first.
Q: A heater connected to a 12 V supply draws a current of 4.0 A. What is its power? (from [Electricity](#phys.electricity))
A: \(P = VI = 12 \times 4.0 = 48\,\mathrm{W}\).
Q: A mass of 450 g of water is used in an experiment. Write its mass in kilograms. (from [Physical quantities, units and uncertainty](#phys.units))
A: \(450\,\mathrm{g} = 0.450\,\mathrm{kg}\), because \(1\,\mathrm{kg} = 1000\,\mathrm{g}\).
:::

## Temperature and thermal energy

Everyday language mixes up two ideas that physics keeps apart.

- **Temperature** tells you how hot something is. It is a property of the object at one moment, and it does not depend on how much of the object there is. A drop of boiling water and a bucket of boiling water are at the same temperature.
- **Thermal energy** is the energy a body holds in the random motion and arrangement of its molecules. It does depend on how much there is. The bucket holds far more.

A bath of water at 40 °C holds much more thermal energy than a cup of tea at 80 °C, simply because it contains thousands of times more water. You will put numbers on this later in the chapter.

What decides which way energy flows is the temperature, not the amount of thermal energy.

:::key Direction of energy transfer
Thermal energy is transferred from a region of higher temperature to a region of lower temperature. Energy does not flow the other way by itself, however much more total energy the cooler body holds.
:::

Put a hot spoon in cold water. Energy flows from the spoon to the water. The spoon cools and the water warms. The transfer slows as the two temperatures get closer, and it stops when they are equal.

:::def Thermal equilibrium
A state in which there is no net transfer of thermal energy between two regions: they are at the same temperature.
:::

Thermal equilibrium is what makes a thermometer work. A thermometer cannot "sense" the temperature of an object at a distance. It must be in contact with the object for long enough to reach thermal equilibrium, and then the thermometer's own temperature, which it can show, is equal to the object's temperature. That is why a clinical thermometer is held under the tongue for a minute.

:::note
Many textbooks say "heat" for energy transferred because of a temperature difference. Cambridge writes "thermal energy" or "energy transferred by heating". Avoid the bare word "heat" in an answer when you can say precisely what you mean. Also, a thermometer measures its own temperature: always say it is in thermal equilibrium with the object.
:::

## Measuring temperature

Your senses are poor thermometers. A metal chair feels colder than a wooden one in the same room, because metal carries energy away from your hand faster, yet both are at the same temperature. To measure temperature you use a **physical property that changes with temperature** in a reliable way, and read the property instead.

:::key Thermometric properties
Any physical property that varies with temperature can be used to measure it. The syllabus names four: the **density** of a liquid (equivalently its volume, which is the length of the liquid in a narrow tube), the **volume of a gas at constant pressure**, the **resistance of a metal**, and the **e.m.f. of a thermocouple**. A thermistor, a semiconductor whose resistance changes sharply with temperature, works in the same way.
:::

A thermocouple is two wires of different metals joined at two junctions. If the junctions are at different temperatures, an e.m.f. appears between them, and it grows with the temperature difference. One junction is kept at a known temperature, such as that of melting ice. The other junction is the probe.

| Thermometer | Property that is read | Strengths | Limits |
|---|---|---|---|
| Liquid-in-glass | length of a column of liquid | cheap, direct reading, no power | narrow range, fragile, slow, cannot be read remotely |
| Constant-pressure gas | volume of a fixed mass of gas | very accurate, very wide range | bulky and slow: a laboratory standard |
| Platinum resistance | resistance of a metal wire | accurate, wide range, remote reading | slower than a thermocouple, wire can self-heat |
| Thermistor | resistance of a semiconductor | very sensitive, small, quick | narrow range, non-linear response |
| Thermocouple | e.m.f. of two metal junctions | tiny probe, very quick, very high temperatures | less accurate, needs a reference junction |

To turn a property into a scale you fix two reference temperatures, the **fixed points**, and share the property out evenly between them. On the Celsius scale the fixed points are the freezing point of pure water, 0 °C, and the boiling point of pure water at standard pressure, 100 °C. You note the property's value at each, and then you assume it changes in equal steps in between.

That assumption is where the trouble lies. No two properties change in exactly the same way with temperature. A resistance thermometer and a liquid-in-glass thermometer, each calibrated at 0 °C and 100 °C, agree at those two points and disagree a little in between.

:::plot Reading of thermometer B against the reading of thermometer A, where B's property rises faster at high temperatures. The two agree at the fixed points (0 and 100) and disagree between them.
--f "x" --f "100*(exp(0.004*x)-1)/(exp(0.4)-1)" --x 0 100 --y 0 110 --pt "50,50,A reads 50.0 °C@nw" --pt "50,45.0,B reads 45.0 °C@se" --xlabel "reading of A / °C" --ylabel "reading of B / °C" --xstep 20
:::

The straight line in the graph is the agreement you would have if both properties changed at the same rate. For the curve, B says 45.0 °C when A says 50.0 °C. Neither is "wrong": they are different scales. For this reason, a scale that depends on one substance is never fully satisfactory. The next section describes the scale that does not.

:::exam Choosing a thermometer
Questions ask you to choose a thermometer for a job and justify it. Give the property and the reason that matches the job. A furnace at 1200 °C needs a thermocouple (wide range, small probe, no glass to melt). A thermometer read by a computer needs a property that gives an electrical signal: a thermistor or a resistance thermometer. A sudden change needs a quick response: a small probe with small thermal capacity. A very small temperature change needs a very sensitive property: a thermistor.
:::

## The thermodynamic temperature scale

The thermodynamic scale is defined in a way that does not rely on the behaviour of any substance. That is its great advantage: scientists everywhere get the same value, whatever the material or instrument. It is the scale used in all of the equations of this topic. Its unit, the **kelvin** (K), is an SI base unit.

:::def Absolute zero
The lowest possible temperature, zero kelvin (0 K), at which a substance has minimum internal energy.
:::

In the molecular picture, cooling a substance takes energy out of the random motion of its molecules. At 0 K the energy cannot be reduced any further: nothing can be colder. In the next chapter, [Ideal gases](#phys.gases), you will see that the lines on a graph of gas pressure against Celsius temperature all point towards −273 °C at zero pressure, which is a strong sign that absolute zero is real.

The size of one kelvin equals the size of one degree Celsius, so the two scales only differ in where they start.

:::formula Converting between kelvin and degrees Celsius
\[T/\mathrm{K} = \theta/^\circ\mathrm{C} + 273.15\]
\(T\): thermodynamic temperature (K) · \(\theta\): Celsius temperature (\(^\circ\mathrm{C}\)). Zero kelvin is \(-273.15\,^\circ\mathrm{C}\). A temperature **change** is the same number in both units: \(\Delta T = \Delta\theta\). Never add 273 to a temperature change.
:::

This course uses 273.15 and gives the answer to the same number of significant figures as the data. If a question gives temperatures to the nearest degree, 273 is accepted.

:::eg Convert 37 °C to kelvin, 85 K to degrees Celsius, and the boiling point of nitrogen, −196 °C, to kelvin.
\(T = 37 + 273.15 = 310.15\,\mathrm{K}\), which is 310 K to 3 significant figures. [A1]
\(\theta = 85 - 273.15 = -188.15\), which is \(-188\,^\circ\mathrm{C}\). [A1]
\(T = -196 + 273.15 = 77.15\), which is 77 K. [A1]
:::

:::warn Temperature change is not temperature
Water is heated from 20 °C to 80 °C. The rise is \(\Delta\theta = 60\,^\circ\mathrm{C}\), and that is also \(\Delta T = 60\,\mathrm{K}\). Adding 273 to 60 is one of the most common mistakes in this topic. You only add 273.15 to a temperature written as a position on the scale, never to a difference.
:::

## Specific heat capacity

Heat a kilogram of water and a kilogram of copper with the same heater for the same time, and the copper gets much hotter. Different materials need different amounts of energy to warm up, and the quantity that describes this is the specific heat capacity.

:::def Specific heat capacity
The energy required per unit mass of a substance to raise its temperature by one degree (one kelvin), without a change of state: \(c = \dfrac{E}{m\Delta\theta}\).
:::

:::formula Energy to change the temperature
\[E = mc\,\Delta\theta\]
\(E\): energy transferred to the substance (J) · \(m\): mass (kg) · \(c\): specific heat capacity (\(\mathrm{J\,kg^{-1}\,K^{-1}}\)) · \(\Delta\theta\): rise in temperature (K or °C). For a falling temperature, \(\Delta\theta\) is negative and energy leaves the substance.
:::

Typical values, which an exam question gives you: water 4200, ice 2100, aluminium 900, copper 390, all in \(\mathrm{J\,kg^{-1}\,K^{-1}}\). Water's value is unusually large. That is why it makes a good coolant and why coastal climates are mild: the sea takes in or gives out a huge amount of energy for a small change of temperature.

:::eg A mass of 0.50 kg of water at 20 °C is heated to 100 °C in an electric kettle of power 2.0 kW. Calculate the energy needed and the time taken, ignoring all losses. The specific heat capacity of water is \(4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\).
\[E = mc\Delta\theta = 0.50 \times 4200 \times (100 - 20)\] [C1]
\[E = 1.68 \times 10^{5}\,\mathrm{J}\] [A1]
\[t = \frac{E}{P} = \frac{1.68 \times 10^{5}}{2000} = 84\,\mathrm{s}\] [A1]
A real kettle takes longer, because some energy warms the kettle itself and escapes to the room.
:::

:::eg Compare the thermal energy needed to warm the contents of a cup of tea (0.25 kg) from 20 °C to 80 °C with that needed to warm a bath (150 kg of water) from 20 °C to 40 °C. Use \(c = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\).
Tea: \(E = 0.25 \times 4200 \times 60 = 6.3 \times 10^{4}\,\mathrm{J}\). [C1]
Bath: \(E = 150 \times 4200 \times 20 = 1.26 \times 10^{7}\,\mathrm{J}\). [A1]
The bath needs 200 times as much energy, although its temperature rise is only a third as large. The tea is hotter, but the bath holds far more thermal energy.
:::

### Measuring the specific heat capacity of a solid

A block of the material has two holes: one holds an electric heater, the other a thermometer. The block is wrapped in insulation. The heater's power is found from a joulemeter, or from \(P = VI\) with an ammeter and a voltmeter.

:::html
<figure class="fig small"><svg viewBox="30 0 320 332" role="img" aria-label="Top: a metal block wrapped in insulation, with an electric heater and a thermometer in two holes in the block. Bottom: a circuit with a power supply, an ammeter in series, and a heater with a voltmeter connected across it."><rect class="fm s-mute sw1 dash" x="116" y="76" width="148" height="100"/><rect class="fm2 s-ink sw2" x="130" y="90" width="120" height="70"/><rect class="fp s-ink sw2" x="150" y="40" width="24" height="90"/><rect class="fp s-ink sw2" x="206" y="30" width="10" height="104"/><path class="ln" d="M156 40V16M168 40V16"/><circle class="fp s-ink sw2" cx="156" cy="12" r="4"/><circle class="fp s-ink sw2" cx="168" cy="12" r="4"/><text class="tl te" x="144" y="62">heater</text><text class="tl" x="224" y="44">thermometer</text><text class="tl tc" x="190" y="152">metal block</text><text class="tl te" x="108" y="130">insulation</text><path class="ln" d="M100 253V215H280V315H100V263"/><path class="ln" d="M86 253H114"/><path class="ln thick" d="M92 263H108"/><text class="tl te" x="78" y="262">supply</text><path class="ln" d="M230 215V315"/><circle class="fi" cx="230" cy="215" r="4"/><circle class="fi" cx="230" cy="315" r="4"/><circle class="fp s-ink sw2" cx="150" cy="215" r="13"/><text class="tb tc" x="150" y="220">A</text><circle class="fp s-ink sw2" cx="230" cy="265" r="13"/><text class="tb tc" x="230" y="270">V</text><rect class="fp s-ink sw2" x="272" y="240" width="16" height="50"/><text class="tl" x="296" y="270">heater</text></svg><figcaption>The block with its insulation (top) and the electrical circuit that supplies the heater (bottom). The ammeter is in series and the voltmeter is across the heater, so \(P = VI\).</figcaption></figure>
:::

:::lab Measuring the specific heat capacity of a metal block electrically
:::steps
1. Measure the mass \(m\) of the block with a balance. Put the heater and a thermometer into the holes (a drop of oil in the thermometer hole improves thermal contact) and wrap the block in thick insulation.
2. Record the starting temperature. Switch on the heater and start a stopwatch together. Read \(V\) and \(I\) (or the joulemeter) and keep them steady.
3. Record the temperature at regular intervals, for example every 30 s, for about 10 minutes. Switch off, and keep reading while the thermometer rises a little further, as energy spreads through the block.
4. Plot temperature \(\theta\) against time \(t\). The line is straight when the power is steady. Since \(E = Pt = mc\Delta\theta\), the gradient is \(\dfrac{\Delta\theta}{t} = \dfrac{P}{mc}\), so \(c = \dfrac{P}{m \times \text{gradient}}\).
:::
Using the gradient of a line averages out random errors, and a graph shows straight away if the power or the losses were not steady. The measured \(c\) is nearly always **too large**, because some of the electrical energy escapes to the surroundings and so the block warms less than it would. Reduce the error with thick insulation and a lid, and start a few degrees below room temperature and end the same number of degrees above it, so that the energy gained from the room in the first half balances the energy lost in the second half.
:::

:::plot Temperature of a 1.0 kg block heated by a 50 W heater. The gradient is \(P/(mc)\).
--f "20+0.050*x" --x 0 400 --y 0 45 --pt "0,20,θ = 20 °C at t = 0@se" --pt "300,35,(300 s, 35 °C)@se" --xlabel "t / s" --ylabel "θ / °C"
:::

:::eg In an experiment, a 50 W heater warms a 1.0 kg aluminium block. The graph of temperature against time is a straight line of gradient \(0.050\,\mathrm{K\,s^{-1}}\). Calculate the specific heat capacity, and say why the true value is lower than the result.
The gradient is \(\dfrac{P}{mc}\), so \(c = \dfrac{P}{m \times \text{gradient}} = \dfrac{50}{1.0 \times 0.050}\) [C1]
\[c = 1.0 \times 10^{3}\,\mathrm{J\,kg^{-1}\,K^{-1}}\] [A1]
Some of the energy supplied is lost to the surroundings, so the block gains less energy than \(Pt\). The block warms more slowly, the gradient is too small, and so the calculated \(c\) is too large. The accepted value for aluminium is about 900. [B1]
:::

### The method of mixtures

Drop a hot piece of metal into cool water inside an insulated cup. Energy flows from the metal to the water until they have the same temperature. If no energy escapes, then **energy lost by the hot object equals energy gained by the cold object**.

:::eg A copper block of mass 0.200 kg at 100 °C is dropped into 0.300 kg of water at 20.0 °C in an insulated container. Find the final temperature. (\(c_\text{Cu} = 390\,\mathrm{J\,kg^{-1}\,K^{-1}}\), \(c_\text{water} = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\)). Ignore the container.
Let the final temperature be \(\theta\). The copper cools from 100 °C to \(\theta\) and the water warms from 20.0 °C to \(\theta\).
Energy lost by copper = energy gained by water: [B1]
\[0.200 \times 390 \times (100 - \theta) = 0.300 \times 4200 \times (\theta - 20.0)\] [C1]
\[7800 - 78\theta = 1260\theta - 25\,200\] so \(\theta = \dfrac{33\,000}{1338}\) [M1]
\[\theta = 25\,^\circ\mathrm{C}\] [A1] (24.7 before rounding)
Water has a much larger \(mc\) than the copper, so the final temperature is close to the water's starting temperature.
:::

:::eg A metal sample of mass 0.150 kg is heated to 98 °C and dropped into 0.250 kg of water at 18.0 °C. The final temperature is 22.0 °C. Find the specific heat capacity of the metal.
\[0.150 \times c \times (98 - 22.0) = 0.250 \times 4200 \times (22.0 - 18.0)\] [C1]
\[11.4\,c = 4200\] [M1]
\[c = 3.7 \times 10^{2}\,\mathrm{J\,kg^{-1}\,K^{-1}}\] [A1] (368 before rounding, so the metal could be copper)
:::

## Specific latent heat

Heat a pan of ice with a steady heater and watch a thermometer. The ice warms to 0 °C. Then the temperature stops rising while the ice melts, even though the heater is still supplying energy. The temperature starts rising again only when all of the ice has become water. The same happens at 100 °C when water boils.

:::def Specific latent heat of fusion
The energy required per unit mass to change a substance from solid to liquid without any change in temperature.
:::

:::def Specific latent heat of vaporisation
The energy required per unit mass to change a substance from liquid to gas without any change in temperature.
:::

:::formula Energy for a change of state
\[E = mL\]
\(E\): energy transferred (J) · \(m\): mass that changes state (kg) · \(L\): specific latent heat (\(\mathrm{J\,kg^{-1}}\)), either \(L_\text{f}\) (fusion) or \(L_\text{v}\) (vaporisation). The same energy is given out when the change is reversed (freezing, condensing).
:::

Typical values for water: \(L_\text{f} = 3.34 \times 10^{5}\,\mathrm{J\,kg^{-1}}\) and \(L_\text{v} = 2.26 \times 10^{6}\,\mathrm{J\,kg^{-1}}\). Exam questions give them.

### Why the temperature stays constant

The temperature of a substance is linked to the average **kinetic** energy of its molecules. During a change of state, the energy supplied does not make the molecules move faster. Instead it increases their **potential energy**: the molecules are pulled apart against the forces between them. The mean kinetic energy stays the same, so the temperature stays the same. In the solid, the molecules vibrate about fixed positions and are held together. On melting they can slide past each other. On boiling they leave the liquid completely and move far apart.

Vaporisation needs much more energy than fusion, \(L_\text{v}/L_\text{f} = 6.77\) for water. There are two reasons. Boiling separates the molecules **completely**, so every attractive bond is broken, whereas melting only loosens them. And when a liquid boils into a gas it expands by a large factor and **pushes back the atmosphere**, so some of the energy does work on the surroundings.

:::html
<figure class="fig"><svg viewBox="20 44 520 228" role="img" aria-label="A heating curve for a substance heated at constant power. Temperature rises steeply as a solid, stays constant while the solid melts at 0 degrees, rises more slowly as a liquid up to 100 degrees, stays constant while it boils, and then rises steeply as a gas. The boiling plateau is much longer than the melting plateau."><path class="ax" d="M50 222V58M50 222H520"/><path class="ln thin dash" d="M50 90H350M50 190H90"/><path class="c1" d="M70 210L90 190H150L350 90H470L490 70"/><path class="ln-m thin" d="M90 222V228M150 222V228M350 222V228M470 222V228"/><text class="ts te" x="44" y="94">100</text><text class="ts te" x="44" y="194">0</text><text class="tl" x="58" y="64">θ / °C</text><text class="tl tc" x="74" y="244">solid</text><text class="tl tc" x="122" y="244">melting</text><text class="tl tc" x="250" y="244">liquid</text><text class="tl tc" x="410" y="244">boiling</text><text class="tl tc" x="480" y="244">gas</text><text class="tl tc" x="285" y="264">energy supplied at constant power (not to scale)</text></svg><figcaption>A heating curve. Where the line is level, the energy supplied goes into the potential energy of the molecules and the temperature stays constant. The line is steeper for the solid than for the liquid because the gradient is \(P/(mc)\) and the solid's \(c\) is smaller. The boiling plateau is drawn short: for water it is really about seven times as long as the melting plateau.</figcaption></figure>
:::

:::eg Calculate the energy needed to turn 0.20 kg of ice at −10 °C into water at 20 °C. \(c_\text{ice} = 2100\), \(c_\text{water} = 4200\) (both in \(\mathrm{J\,kg^{-1}\,K^{-1}}\)) and \(L_\text{f} = 3.34 \times 10^{5}\,\mathrm{J\,kg^{-1}}\).
Do it in three stages, one for each part of the heating curve:
Warm the ice to 0 °C: \(0.20 \times 2100 \times 10 = 4200\,\mathrm{J}\). [C1]
Melt it: \(0.20 \times 3.34 \times 10^{5} = 66\,800\,\mathrm{J}\). [C1]
Warm the water to 20 °C: \(0.20 \times 4200 \times 20 = 16\,800\,\mathrm{J}\). [C1]
Total \(= 4200 + 66\,800 + 16\,800 = 87\,800\,\mathrm{J} \approx 88\,\mathrm{kJ}\). [A1]
Melting takes more than three-quarters of the total: the biggest cost is not warming, but changing state.
:::

:::eg A burn from steam at 100 °C is worse than one from boiling water at 100 °C. Steam of mass 0.050 kg at 100 °C is passed into 0.40 kg of water at 20 °C in an insulated container. Find the final temperature. \(L_\text{v} = 2.26 \times 10^{6}\,\mathrm{J\,kg^{-1}}\), \(c = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\).
The steam first condenses, giving out \(0.050 \times 2.26 \times 10^{6} = 1.13 \times 10^{5}\,\mathrm{J}\). [C1]
The condensed water then cools from 100 °C to \(\theta\). Energy lost = energy gained:
\[1.13 \times 10^{5} + 0.050 \times 4200 \times (100 - \theta) = 0.40 \times 4200 \times (\theta - 20)\] [M1]
\[1.13 \times 10^{5} + 21\,000 - 210\theta = 1680\theta - 33\,600\] so \(\theta = \dfrac{167\,600}{1890}\)
\[\theta = 89\,^\circ\mathrm{C}\] [A1] (88.7 before rounding)
The condensing step released as much energy as it takes to warm the whole 0.40 kg of water by 67 K. That is why steam scalds so badly.
:::

### Measuring a specific latent heat

For ice, fill two funnels with crushed ice at 0 °C and place a beaker under each. In one funnel there is an electric heater, in the other there is not. Without the heater, ice still melts because the room warms it. The second funnel measures that.

:::lab Measuring the specific latent heat of fusion of ice
:::steps
1. Put an electric heater in crushed melting ice in a funnel (the **heater funnel**), above a beaker. Put the same amount of crushed ice in a second funnel without a heater (the **control funnel**) above another beaker.
2. Wait until the ice is melting steadily and water drips from both. Replace the beakers with empty ones of known mass, switch on the heater and start a stopwatch. Record \(V\) and \(I\).
3. After a measured time \(t\) (a few minutes), switch off the heater and collect the water. Find the masses of water \(m_1\) (heater funnel) and \(m_0\) (control funnel).
4. The energy from the heater melted the extra mass \(m_1 - m_0\), so \(VIt = (m_1 - m_0)L_\text{f}\) and \(L_\text{f} = \dfrac{VIt}{m_1 - m_0}\).
:::
The control funnel removes the effect of the room. Use crushed ice that is already melting (so it is at 0 °C and none of the heater's energy warms it) and let the water drain steadily before you start timing.
:::

:::eg In the experiment above, the heater is connected to a 12 V supply and draws 5.0 A. It is on for 300 s. The heater funnel collects 62.0 g of water and the control funnel collects 8.0 g. Calculate the specific latent heat of fusion of ice.
Energy supplied: \(E = VIt = 12 \times 5.0 \times 300 = 1.8 \times 10^{4}\,\mathrm{J}\). [C1]
Mass melted by the heater: \(m_1 - m_0 = 62.0 - 8.0 = 54.0\,\mathrm{g} = 0.0540\,\mathrm{kg}\). [C1]
\[L_\text{f} = \frac{E}{m_1 - m_0} = \frac{1.8 \times 10^{4}}{0.0540} = 3.3 \times 10^{5}\,\mathrm{J\,kg^{-1}}\] [A1]
This is close to the accepted value of \(3.34 \times 10^{5}\,\mathrm{J\,kg^{-1}}\).
:::

For the specific latent heat of vaporisation, an immersion heater boils water in a vessel standing on a balance. The balance reading falls as steam escapes. The same idea of a "control" is used here too: run the experiment twice with two different heater powers, and subtract. The energy lost to the surroundings is the same in both runs because the temperature is the same (100 °C), so it cancels.

:::proof examinable Latent heat of vaporisation by the two-power method
Run 1 uses a heater of power \(P_1\) and run 2 a heater of power \(P_2\). Both run for the same time \(t\) with the water boiling steadily at 100 °C, and the balance shows that masses \(m_1\) and \(m_2\) are boiled away.
The energy lost to the surroundings in time \(t\) is the same in each run, \(E_\text{loss}\), because the vessel is at the same temperature.
Run 1: the energy that vaporises the water is \(P_1 t - E_\text{loss} = m_1 L_\text{v}\).
Run 2: the energy that vaporises the water is \(P_2 t - E_\text{loss} = m_2 L_\text{v}\).
Subtract the second equation from the first: \(E_\text{loss}\) cancels, leaving \((P_1 - P_2)t = (m_1 - m_2)L_\text{v}\).
Therefore \(L_\text{v} = \dfrac{(P_1 - P_2)t}{m_1 - m_2}\).
:::

:::eg In a two-power experiment, a heater of 60 W boils away 14.3 g of water in 600 s. A heater of 40 W boils away 9.00 g in 600 s. Calculate the specific latent heat of vaporisation of water.
\[L_\text{v} = \frac{(P_1 - P_2)t}{m_1 - m_2} = \frac{(60 - 40) \times 600}{(14.3 - 9.00) \times 10^{-3}}\] [C1]
\[L_\text{v} = \frac{1.2 \times 10^{4}}{5.30 \times 10^{-3}} = 2.26 \times 10^{6}\,\mathrm{J\,kg^{-1}}\] [A1]
The difference \(m_1 - m_2\) is small, so a balance reading to 0.1 g matters: take a long enough time for the difference to be several grams.
:::

:::board
AQA and OCR include the same content: the same definitions, temperature scales, specific heat capacity and latent heat. AQA writes the specific heat capacity equation as \(Q = mc\Delta\theta\) and describes the continuous-flow method of measuring \(c\) for a liquid; that method is not on the Cambridge syllabus.
:::

:::eg Spot the error: a 2.0 kg block of water is heated through 15 °C. Calculate the energy needed. (\(c = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\))
A student wrote this answer.

Line 1: \(\Delta T = 15 + 273 = 288\,\mathrm{K}\)
Line 2: \(E = mc\Delta T = 2.0 \times 4200 \times 288 = 2.4 \times 10^{6}\,\mathrm{J}\)

**Line 1 is wrong: 15 °C is a temperature rise, not a point on the scale, so it is 15 K and you must not add 273.** Because the method was wrong, the formula mark is lost. [C0] The final answer is also wrong. [A0]

Correct working: \(E = 2.0 \times 4200 \times 15 = 1.3 \times 10^{5}\,\mathrm{J}\). [A1] (126 000 J before rounding)

A rise of 15 K is only about 5 % of 288 K, so an answer that is nearly 20 times too large should have rung a bell.
:::

:::try Start easy, finish at exam standard
Q: Convert −40 °C to kelvin and 500 K to degrees Celsius.
A: \(T = -40 + 273.15 = 233\,\mathrm{K}\) and \(\theta = 500 - 273.15 = 227\,^\circ\mathrm{C}\).
Q: What is the direction of the net energy transfer between a hot spoon and a cold cup of water in contact, and what is true when the transfer stops?
A: Energy goes from the spoon (higher temperature) to the water (lower temperature). It stops when the two are in thermal equilibrium, at the same temperature.
Q: Calculate the energy needed to raise the temperature of 2.0 kg of aluminium from 20 °C to 70 °C. (\(c = 900\,\mathrm{J\,kg^{-1}\,K^{-1}}\))
A: \(E = mc\Delta\theta = 2.0 \times 900 \times 50 = 9.0 \times 10^{4}\,\mathrm{J}\).
Q: A 1.5 kW heater melts a block of ice of mass 0.30 kg already at 0 °C. How long does it take, ignoring losses? (\(L_\text{f} = 3.34 \times 10^{5}\,\mathrm{J\,kg^{-1}}\))
A: \(E = mL = 0.30 \times 3.34 \times 10^{5} = 1.0 \times 10^{5}\,\mathrm{J}\) and \(t = E/P = 100\,200/1500 = 67\,\mathrm{s}\).
Q: How much energy is released when 0.40 kg of steam at 100 °C condenses to water at 100 °C? (\(L_\text{v} = 2.26 \times 10^{6}\,\mathrm{J\,kg^{-1}}\))
A: \(E = mL = 0.40 \times 2.26 \times 10^{6} = 9.0 \times 10^{5}\,\mathrm{J}\).
Q: The resistance of a platinum thermometer is 100.0 Ω at 0 °C and 138.5 Ω at 100 °C. Assuming resistance rises linearly with temperature, find the temperature when its resistance is 119.5 Ω.
A: The rise from 0 °C is \(\dfrac{119.5 - 100.0}{138.5 - 100.0} = \dfrac{19.5}{38.5}\) of the 100 °C range, so \(\theta = \dfrac{19.5}{38.5} \times 100 = 51\,^\circ\mathrm{C}\).
Q: A 100 W heater warms 0.25 kg of water for 3.0 minutes. Ignoring losses, find the rise in temperature. (\(c = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\))
A: \(E = Pt = 100 \times 180 = 1.8 \times 10^{4}\,\mathrm{J}\), so \(\Delta\theta = \dfrac{E}{mc} = \dfrac{18\,000}{0.25 \times 4200} = 17\,\mathrm{K}\).
Q: Explain why steam at 100 °C causes a worse scald than the same mass of water at 100 °C.
A: When the steam condenses on the skin it releases its latent heat of vaporisation, a large amount of energy per kilogram, before it cools further. The water at 100 °C releases only the much smaller energy of cooling.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Convert (a) 37 °C to kelvin and (b) 85 K to degrees Celsius.
A: (a) \(T = 37 + 273.15 = 310\,\mathrm{K}\) (or 310.15 K). [A1] (b) \(\theta = 85 - 273.15 = -188\,^\circ\mathrm{C}\). [A1]
Q: [2 marks] ★ Define the specific latent heat of vaporisation.
A: The energy required per unit mass [B1] to change a substance from liquid to gas without a change in temperature. [B1]
Q: [2 marks] ★★ A block of ice is melting at 0 °C while a heater supplies energy to it. Explain why its temperature does not change.
A: The energy supplied increases the potential energy of the molecules as they are separated, [B1] and not their mean kinetic energy, so the temperature stays constant. [B1]
Q: [4 marks] ★★ A piece of aluminium of mass 0.120 kg at 95 °C is dropped into 0.200 kg of water at 18 °C in an insulated container. Calculate the final temperature. (\(c_\text{Al} = 900\), \(c_\text{water} = 4200\), both in \(\mathrm{J\,kg^{-1}\,K^{-1}}\).)
A: Energy lost by aluminium = energy gained by water. [B1] \(0.120 \times 900 \times (95 - \theta) = 0.200 \times 4200 \times (\theta - 18)\) [C1] so \(10\,260 - 108\theta = 840\theta - 15\,120\) [M1] and \(\theta = \dfrac{25\,380}{948} = 27\,^\circ\mathrm{C}\). [A1]
Q: [4 marks] ★★ A 150 W heater is placed in water that is boiling at 100 °C in a flask standing on a balance. In 300 s the balance reading falls by 18.8 g. (a) Calculate the specific latent heat of vaporisation of water from these results. (b) The accepted value is lower than the result. Suggest why.
A: (a) \(E = Pt = 150 \times 300 = 4.5 \times 10^{4}\,\mathrm{J}\) [C1] \(L_\text{v} = \dfrac{E}{m} = \dfrac{4.5 \times 10^{4}}{0.0188}\) [C1] \(= 2.39 \times 10^{6}\,\mathrm{J\,kg^{-1}}\). [A1] (b) Some of the energy from the heater was lost to the surroundings and did not vaporise water, so the energy used on boiling is less than \(Pt\) and the calculated \(L_\text{v}\) is too large. [B1]
Q: [5 marks] ★★★ A solid of mass 0.50 kg is heated by a 500 W heater from 20 °C. It takes 90 s to reach its melting point of 80 °C. It then takes a further 300 s for all of the solid to melt, with the temperature constant. Assume all the energy goes into the solid. (a) Calculate the specific heat capacity of the solid. (b) Calculate the specific latent heat of fusion. (c) The same heater is used on 0.50 kg of the liquid. State and explain whether the liquid's temperature rises faster or more slowly than that of the solid if its specific heat capacity is larger.
H: Energy supplied is power times time, in both stages.
H: In (c), the rate of temperature rise is \(P/(mc)\).
A: (a) \(E = Pt = 500 \times 90 = 4.5 \times 10^{4}\,\mathrm{J}\) and \(c = \dfrac{E}{m\Delta\theta} = \dfrac{4.5 \times 10^{4}}{0.50 \times 60}\) [C1] \(= 1.5 \times 10^{3}\,\mathrm{J\,kg^{-1}\,K^{-1}}\). [A1] (b) \(E = 500 \times 300 = 1.5 \times 10^{5}\,\mathrm{J}\) and \(L = \dfrac{E}{m} = \dfrac{1.5 \times 10^{5}}{0.50}\) [C1] \(= 3.0 \times 10^{5}\,\mathrm{J\,kg^{-1}}\). [A1] (c) The rate of rise is \(P/(mc)\); with the same \(P\) and \(m\) and a larger \(c\), the temperature rises more slowly. [B1]
Q: [6 marks] ★★★ A student finds the specific latent heat of vaporisation of water with an immersion heater in boiling water on a balance. With a heater of power 60 W, 14.3 g of water is lost in 600 s. With a heater of power 40 W, 9.00 g is lost in 600 s. (a) Explain why the student uses two different powers. (b) Show that the energy supplied to the heater in the 60 W run is not all used to vaporise water, and calculate the rate at which energy is lost to the surroundings. (c) Calculate the specific latent heat of vaporisation.
H: In the 60 W run, the energy that vaporises water is \(mL\), where \(L\) is found from part (c).
H: Energy lost per second is the power minus the power that vaporises the water.
A: (a) Energy is lost to the surroundings, [B1] and the loss is the same in both runs because the temperature is the same, so it cancels when one equation is subtracted from the other. [B1] (c) \(L_\text{v} = \dfrac{(P_1 - P_2)t}{m_1 - m_2} = \dfrac{20 \times 600}{5.30 \times 10^{-3}}\) [C1] \(= 2.26 \times 10^{6}\,\mathrm{J\,kg^{-1}}\). [A1] (b) The energy that vaporises water is \(mL = 0.0143 \times 2.26 \times 10^{6} = 3.2 \times 10^{4}\,\mathrm{J}\), less than the 36 000 J supplied, [C1] so the loss is \((36\,000 - 32\,300)/600 \approx 6\,\mathrm{W}\). [A1]
Q: [4 marks] ★★★ A technician must measure the temperature of molten glass at about 1200 °C, and record it on a computer every second. Choose a suitable thermometer and justify your choice, and explain why a liquid-in-glass thermometer is unsuitable.
H: Use one reason for each requirement: temperature range, size of the sensor, electrical output.
A: A thermocouple. [B1] Its two metal wires withstand a very high temperature and its junction is small, so it responds quickly to changes. [B1] It produces an e.m.f., which is an electrical signal that a computer can record automatically. [B1] A liquid-in-glass thermometer would melt or the liquid would boil, it responds slowly, and it cannot be read by a computer. [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ An electric shower heats water from 10 °C to 38 °C. The water flows at 5.0 litres per minute (1 litre of water has a mass of 1.0 kg). (a) Calculate the minimum power of the heater. (b) The shower is actually rated at 10.5 kW. Calculate its efficiency, and suggest where the rest of the energy goes. (c) By what factor does the flow rate have to change for the water to leave at 48 °C instead, with the same rated power and the same efficiency? (\(c = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\))
H: Work with a mass flowing each second: energy per second is the power.
H: For (c), the rise in temperature is 38 K, not 48 K.
A: (a) The mass flow rate is \(5.0/60 = 0.0833\,\mathrm{kg\,s^{-1}}\). [C1] \(P = \dfrac{m}{t}c\Delta\theta = 0.0833 \times 4200 \times 28\) [C1] \(= 9.8 \times 10^{3}\,\mathrm{W}\). [A1] (b) Efficiency \(= 9.8/10.5 = 0.93\). [A1] The rest warms the casing and pipes and escapes to the surroundings. [B1] (c) The power transferred is the same, so \(\dfrac{m}{t}\Delta\theta\) is constant: the new rise is 38 K, so the flow rate must be multiplied by \(28/38 = 0.74\), about 3.7 litres per minute. [B1] [A1]
Q: [7 marks] ★★★ A cube of ice of mass 25 g at 0 °C is put into 0.250 kg of a drink at 22 °C in an insulated glass. Treat the drink as water and ignore the glass. (a) Show that the final temperature, when all of the ice has melted, is about 13 °C. (b) What is the largest mass of ice at 0 °C that could be added before the drink cools to 0 °C and some ice survives? (\(c = 4200\,\mathrm{J\,kg^{-1}\,K^{-1}}\), \(L_\text{f} = 3.34 \times 10^{5}\,\mathrm{J\,kg^{-1}}\))
H: Energy lost by the drink = energy to melt the ice + energy to warm the melted ice from 0 °C to \(\theta\).
H: In (b), the drink cools to 0 °C and gives out \(mc\Delta\theta\); that energy melts the ice.
A: (a) Energy to melt the ice: \(0.025 \times 3.34 \times 10^{5} = 8350\,\mathrm{J}\). [C1] Energy lost by the drink \(=\) energy to melt + energy to warm the meltwater: \(0.250 \times 4200 \times (22 - \theta) = 8350 + 0.025 \times 4200 \times \theta\) [M1] so \(23\,100 - 1050\theta = 8350 + 105\theta\) and \(\theta = \dfrac{14\,750}{1155} = 12.8\,^\circ\mathrm{C}\), about 13 °C. [A1] (b) When the drink has cooled from 22 °C to 0 °C it has given out \(0.250 \times 4200 \times 22 = 2.31 \times 10^{4}\,\mathrm{J}\). [C1] This melts at most \(m = \dfrac{2.31 \times 10^{4}}{3.34 \times 10^{5}} = 0.069\,\mathrm{kg}\) of ice. [A1] More than about 69 g of ice and some will survive. [B1] The final temperature of the drink is 0 °C in that case. [B1]
:::

:::quiz
? A bath of water at 40 °C and a cup of tea at 80 °C are brought into thermal contact through a thin metal wall. In which direction is the net transfer of thermal energy?
+ From the tea to the bath
- From the bath to the tea, because the bath holds more thermal energy
- There is no net transfer, because the energy stored is different
- It depends on the masses
> Energy flows from the higher temperature to the lower temperature. The bath contains more thermal energy overall, but the tea is hotter, so the energy goes from the tea to the bath.
? A temperature rises by 25 °C. What is the rise in kelvin?
+ 25 K
- 298 K
- 248 K
- 298.15 K
> The kelvin and the degree Celsius are the same size, so a change of 25 °C is a change of 25 K. Only a temperature on the scale needs 273.15 added.
? What is the thermodynamic temperature that corresponds to 0 °C?
- 0 K
- 273 °C
+ 273.15 K
- 100 K
> \(T = 0 + 273.15 = 273.15\,\mathrm{K}\). Zero kelvin is the lowest possible temperature, −273.15 °C.
? Which statement about the thermodynamic temperature scale is correct?
+ It does not depend on the property of any particular substance.
- It is defined by the expansion of mercury.
- It is the scale on which water boils at 0 K.
- It has the same zero as the Celsius scale.
> The thermodynamic scale is absolute and is not based on the behaviour of one substance. A scale built on mercury or on any other property would depend on that property, as the curve in the thermometer graph shows.
? The specific heat capacity of a substance is the energy
- needed to change 1 kg of it from solid to liquid at constant temperature
+ needed to raise the temperature of 1 kg of it by 1 K
- stored in 1 kg of it at 0 °C
- needed to raise the temperature of 1 m³ of it by 1 K
> Specific heat capacity is energy per kilogram per kelvin, \(c = E/(m\Delta\theta)\). The first option describes specific latent heat of fusion.
? Ice is melting steadily at 0 °C as a heater supplies energy. What happens to the energy?
+ It increases the potential energy of the molecules.
- It increases the mean kinetic energy of the molecules.
- It is stored as thermal energy in the heater.
- It is destroyed, because the temperature does not change.
> During a change of state, the molecules are pulled apart against attractive forces, so their potential energy rises. The mean kinetic energy, and so the temperature, is unchanged. Energy is never destroyed.
? A student measures the specific heat capacity of a block with an electric heater and does not insulate it. The result is
+ larger than the true value, because the block gains less energy than the electrical energy supplied
- smaller than the true value, because energy is lost
- correct, because losses cancel
- smaller than the true value, because the heater is not 100 % efficient
> Some energy escapes, so the temperature rise is smaller than it should be for the energy supplied. Since \(c = E/(m\Delta\theta)\), a smaller \(\Delta\theta\) with the same \(E\) gives a result that is too large.
:::

:::checklist What you can now do
- [ ] I can state that thermal energy is transferred from a region of higher to a region of lower temperature, and define thermal equilibrium.
- [ ] I can explain how a physical property that varies with temperature is used to measure it, and compare thermometers (liquid, gas, metal resistance, thermistor, thermocouple).
- [ ] I can explain why the thermodynamic scale does not depend on any substance and why absolute zero is the lowest possible temperature.
- [ ] I can convert between kelvin and degrees Celsius with \(T/\mathrm{K} = \theta/^\circ\mathrm{C} + 273.15\), and I never add 273 to a temperature change.
- [ ] I can define and use specific heat capacity with \(E = mc\Delta\theta\), including the method of mixtures.
- [ ] I can describe an electrical experiment to measure specific heat capacity, and explain why the result is too large.
- [ ] I can define specific latent heat of fusion and of vaporisation, use \(E = mL\), and explain why the temperature stays constant during a change of state.
- [ ] I can describe experiments to measure specific latent heat, including the two-power method that removes heat losses.
:::

:::recap
- Temperature decides the direction of energy flow (hot to cold); thermal energy depends on the amount of substance as well. Equal temperatures mean thermal equilibrium.
- Thermometers read a property that varies with temperature: liquid length, gas volume at constant pressure, resistance of a metal or thermistor, thermocouple e.m.f. Different properties agree only at the fixed points.
- The thermodynamic scale does not depend on any substance. \(T/\mathrm{K} = \theta/^\circ\mathrm{C} + 273.15\). Absolute zero, 0 K, is the lowest possible temperature (minimum internal energy). A change of 1 K equals a change of 1 °C.
- Specific heat capacity: \(E = mc\Delta\theta\), in \(\mathrm{J\,kg^{-1}\,K^{-1}}\). Electrical method: gradient of \(\theta\)–\(t\) is \(P/(mc)\); heat losses make \(c\) too large. Mixtures: energy lost = energy gained.
- Specific latent heat: \(E = mL\), in \(\mathrm{J\,kg^{-1}}\). Fusion (solid to liquid) and vaporisation (liquid to gas), at constant temperature.
- During a change of state, energy raises molecular potential energy, not kinetic energy. \(L_\text{v} \gg L_\text{f}\): molecules separate completely and push back the atmosphere.
- Two-power method: \(L_\text{v} = \dfrac{(P_1 - P_2)t}{m_1 - m_2}\) cancels the energy lost to the surroundings.
:::

:::links
- explore: [States of Matter](https://phet.colorado.edu/en/simulations/states-of-matter) · PhET · heat and cool a substance and watch the molecules change state
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the thermal physics questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Ideal gases](#phys.gases)
