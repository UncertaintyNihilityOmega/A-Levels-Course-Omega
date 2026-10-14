@chapter phys.planning
@title Planning, analysis and evaluation
@level a2
@paper CAIE P5 (A Level)
@time 6–8 hours
@summary How to plan an experiment in full (variables, apparatus, analysis, safety), choose what to plot so that a relationship becomes a straight line, tabulate logarithms and uncertainties correctly, draw error bars and a worst acceptable line, and turn a gradient and its uncertainty into a constant with its uncertainty.

:::why
Paper 5 asks you to think like an experimenter without a laboratory in front of you: plan an investigation of a situation you may never have seen, then analyse someone else's data to find a constant and say how well it is known. These are the skills that real physicists use every day, and they follow a pattern that you can learn and rehearse. Because the contexts may be outside the syllabus, the method matters more than the topic.
:::

**Before you start**, you need the table, graph and uncertainty rules from [Practical skills: measurement, tables, graphs and uncertainty](#phys.practical) and the logarithm rules from [Logarithms and exponentials](#math.p3.logs).

:::try Warm-up
Q: A straight line passes through \((2.0\,\mathrm{s},\ 3.5\,\mathrm{m})\) and \((10.0\,\mathrm{s},\ 9.1\,\mathrm{m})\). What is its gradient, with its unit? (from [Practical skills](#phys.practical))
A: \(\dfrac{9.1 - 3.5}{10.0 - 2.0} = 0.70\,\mathrm{m\,s^{-1}}\).
Q: Evaluate \(\lg 76.5\) to three decimal places, and simplify \(\ln\left(e^{3x}\right)\). (from [Logarithms and exponentials](#math.p3.logs))
A: \(\lg 76.5 = 1.884\), and \(\ln\left(e^{3x}\right) = 3x\).
Q: The number of undecayed nuclei is \(N = N_0 e^{-\lambda t}\). Take natural logarithms of both sides. What straight-line graph results? (from [Nuclear physics](#phys.nuclear))
A: \(\ln N = \ln N_0 - \lambda t\). A graph of \(\ln N\) against \(t\) is a straight line with gradient \(-\lambda\) and intercept \(\ln N_0\).
:::

## What Paper 5 tests

Paper 5 (Planning, Analysis and Evaluation) lasts 1 hour 15 minutes and carries 30 marks, in two compulsory 15-mark questions. It is 11.5% of the A Level. The contexts may be outside the syllabus, and any information you need is given in the question.

| | Question 1: planning | Question 2: analysis, conclusions and evaluation |
|---|---|---|
| Marks | 15 | 15 |
| What it covers | defining the problem; methods of data collection; method of analysis; additional detail including safety | data analysis; table of results; graph; conclusion; treatment of uncertainties |
| What you do | write a plan, with a labelled diagram and extended writing | given an equation and data, find a constant and estimate its uncertainty |

### The planning checklist

A good plan covers the same four headings every time. Learn them as a checklist and run down it for every planning question.

:::key Planning checklist
1. **Define the problem.** Name the **independent variable** (what you change), the **dependent variable** (what you measure as a result), and the **control variables** (what you keep the same).
2. **Methods of data collection.** A **labelled diagram** of a workable arrangement. How you change the independent variable (and over what range, with at least six values). The **instrument** for each measured quantity, named and suited to its size. How each control variable is kept constant.
3. **Method of analysis.** What equation to expect, how to rearrange it into \(y = mx + c\), **what to plot**, what the gradient and intercept equal, and what result would show the relationship is valid.
4. **Additional detail.** A **specific** safety risk and its precaution; repeated readings and means; a trial run; a way to reduce a named source of error.
:::

:::def Independent variable
The quantity that the experimenter deliberately changes in an investigation.
:::

:::def Dependent variable
The quantity that is measured as a result, and that is expected to change when the independent variable changes.
:::

:::def Control variable
A quantity that could affect the dependent variable, and that is kept constant so that it cannot confuse the result.
:::

:::exam The diagram earns marks
Draw the diagram with a ruler, label every item of apparatus, and show where each measurement is made (a rule beside the oil, a micrometer on the sphere). Draw it so that someone could build the experiment from it. A circle labelled "device" or a vague "timer" loses marks.
:::

## Instruments for planning

Name the instrument, and say what it is measuring. These are the instruments the syllabus expects you to be able to describe.

- **Oscilloscope (including a storage oscilloscope).** The **Y-gain** (volts per division) sets the vertical scale, and the **time-base** (seconds per division) sets the horizontal scale. A voltage is the number of divisions \(\times\) the Y-gain, measured from the centre line for a peak voltage, or crest to trough for the peak-to-peak voltage. A time (and so a period) is the number of horizontal divisions \(\times\) the time-base, and the **frequency is \(f = 1/T\)**. To see a **current**, pass it through a resistor of known value and observe the p.d. across it: \(I = V/R\). A storage oscilloscope keeps a single trace on the screen, so you can measure a fast pulse or a decay at leisure.
- **Light gate and data logger.** A light gate records the time for which a beam is blocked. With one gate and a card of known width \(d\), the speed is \(d/t\). With two gates, the logger also records the time between them, and the **acceleration** is the change in speed divided by that time.
- **Motion sensor.** An ultrasonic sensor with a data logger records position against time, from which the logger gives velocity (the gradient) and acceleration.
- **Other sensors and a data logger**: a temperature probe for temperature against time, a Hall probe for magnetic flux density, a Geiger–Müller tube and counter for count rate (subtract the background count).
- **Calipers, micrometer, rule, balance, stopwatch** as in [Practical skills](#phys.practical): choose by the size of the quantity.

A data logger takes many readings in a short time, removes reaction time, and records at regular intervals. These are the reasons to suggest one for a fast change.

:::html
<figure class="fig"><svg viewBox="20 6 516 385" role="img" aria-label="An oscilloscope screen with a grid of 10 horizontal by 8 vertical divisions. A sine wave of amplitude 3.0 divisions crosses the centre line with its crests 4.0 divisions apart. The Y-gain is 2.0 volts per division and the time-base is 5.0 milliseconds per division."><rect class="fm s-mute sw1" x="40" y="20" width="400" height="320"/><path class="gr" d="M80 20V340M120 20V340M160 20V340M200 20V340M240 20V340M280 20V340M320 20V340M360 20V340M400 20V340M40 60H440M40 100H440M40 140H440M40 220H440M40 260H440M40 300H440"/><path class="ax" d="M40 180H440"/><path class="c1" d="M40 265L44 251L48 234L52 217L56 199L60 180L64 161L68 143L72 126L76 109L80 95L84 83L88 73L92 66L96 61L100 60L104 61L108 66L112 73L116 83L120 95L124 109L128 126L132 143L136 161L140 180L144 199L148 217L152 234L156 251L160 265L164 277L168 287L172 294L176 299L180 300L184 299L188 294L192 287L196 277L200 265L204 251L208 234L212 217L216 199L220 180L224 161L228 143L232 126L236 109L240 95L244 83L248 73L252 66L256 61L260 60L264 61L268 66L272 73L276 83L280 95L284 109L288 126L292 143L296 161L300 180L304 199L308 217L312 234L316 251L320 265L324 277L328 287L332 294L336 299L340 300L344 299L348 294L352 287L356 277L360 265L364 251L368 234L372 217L376 199L380 180L384 161L388 143L392 126L396 109L400 95L404 83L408 73L412 66L416 61L420 60L424 61L428 66L432 73L436 83L440 95"/><path class="c2" d="M180 46H102" marker-end="url(#ah2-phys)"/><path class="c2" d="M180 46H258" marker-end="url(#ah2-phys)"/><path class="ln-m thin dash" d="M100 38V56M260 38V56"/><text class="tl tc" x="180" y="38">4.0 div</text><path class="ln-m thin dash" d="M440 60H468M440 180H468"/><path class="c2" d="M462 120V62" marker-end="url(#ah2-phys)"/><path class="c2" d="M462 120V178" marker-end="url(#ah2-phys)"/><text class="tl" x="472" y="124">3.0 div</text><text class="tl tc" x="130" y="368">Y-gain: 2.0 V / div</text><text class="tl tc" x="350" y="368">time-base: 5.0 ms / div</text></svg><figcaption>An oscilloscope trace. The amplitude is measured from the centre line to a crest, and the period between two crests in the same direction.</figcaption></figure>
:::

:::eg The trace above is the p.d. across a \(120\,\Omega\) resistor. Find the peak p.d., the peak-to-peak p.d., the period, the frequency and the peak current.
Peak p.d.: \(3.0 \times 2.0 = 6.0\,\mathrm{V}\). Peak-to-peak: \(6.0 \times 2.0 = 12\,\mathrm{V}\) (6.0 divisions from trough to crest). [A1]

Period: \(4.0 \times 5.0\,\mathrm{ms} = 20\,\mathrm{ms}\), so \(f = \dfrac{1}{T} = \dfrac{1}{0.020} = 50\,\mathrm{Hz}\). [A1]

Peak current: \(I = \dfrac{V}{R} = \dfrac{6.0}{120} = 0.050\,\mathrm{A}\). [C1] [A1]
:::

:::html
<figure class="fig"><svg viewBox="20 40 560 220" role="img" aria-label="Plan view of a track with a trolley carrying a card of width d. Two light gates, each with a light source on one side of the track and a receiver on the other, are placed along the track. Both are connected to a data logger below."><rect class="fm s-mute sw1" x="30" y="100" width="540" height="60"/><rect class="f1 s-acc sw2" x="70" y="108" width="130" height="44"/><rect class="f2 s-acc2 sw2" x="135" y="127" width="22" height="6"/><text class="tl tc" x="104" y="148">trolley</text><rect class="fp s-ink sw2" x="291" y="66" width="18" height="22"/><rect class="fp s-ink sw2" x="291" y="172" width="18" height="22"/><path class="ln-m thin dash" d="M300 88V172"/><text class="tl tc" x="300" y="56">light gate 1</text><rect class="fp s-ink sw2" x="431" y="66" width="18" height="22"/><rect class="fp s-ink sw2" x="431" y="172" width="18" height="22"/><path class="ln-m thin dash" d="M440 88V172"/><text class="tl tc" x="440" y="56">light gate 2</text><path class="c1" d="M100 84H172" marker-end="url(#ah-phys)"/><text class="tl ti ta" x="182" y="88">v</text><rect class="fm s-ink sw2" x="280" y="214" width="180" height="34"/><text class="tl tc" x="370" y="235">data logger</text><path class="ln-m thin" d="M300 194V214M440 194V214"/><text class="tl" x="452" y="128">light beam</text><path class="ln-m thin" d="M146 172V134"/><text class="tl tc" x="146" y="190">card, width d</text></svg><figcaption>Seen from above. The card breaks the beam of each gate for as long as it takes to pass, so the speed at each gate is the width of the card divided by the time it blocks the beam.</figcaption></figure>
:::

:::eg A trolley carries a card of width \(d = 0.050\,\mathrm{m}\). It blocks light gate 1 for \(0.040\,\mathrm{s}\) and light gate 2 for \(0.025\,\mathrm{s}\). The logger records \(0.60\,\mathrm{s}\) between the card first blocking gate 1 and first blocking gate 2. Find the acceleration.
Speed at gate 1: \(v_1 = \dfrac{0.050}{0.040} = 1.25\,\mathrm{m\,s^{-1}}\). Speed at gate 2: \(v_2 = \dfrac{0.050}{0.025} = 2.00\,\mathrm{m\,s^{-1}}\). [C1]

Acceleration \(a = \dfrac{v_2 - v_1}{t} = \dfrac{2.00 - 1.25}{0.60} = 1.25\,\mathrm{m\,s^{-2}}\). [A1]

(The speeds are really the mean speeds while the card passes, so a narrower card gives speeds closer to those at the gates.)
:::

## Writing a full plan

The best way to learn planning is to see a complete answer built mark point by mark point. The diagram comes first, because an examiner reads it first.

:::html
<figure class="fig small"><svg viewBox="25 5 305 420" role="img" aria-label="A tall transparent measuring cylinder filled with oil to a surface near the top. A steel sphere is falling below the surface with an arrow marking its speed v. Two elastic bands, marked A and B, encircle the cylinder at a distance s apart, well below the surface. A metre rule stands beside the cylinder and the cylinder stands on a tray."><rect class="fm s-ink sw2" x="110" y="30" width="80" height="360"/><rect class="f2" x="112" y="60" width="76" height="328"/><path class="ln thin" d="M112 60H188"/><rect class="fm s-mute sw1" x="70" y="396" width="150" height="16"/><rect class="fm s-mute sw1" x="50" y="30" width="20" height="360"/><path class="ln-m thin" d="M60 30H70M64 40H70M64 50H70M64 60H70M64 70H70M60 80H70M64 90H70M64 100H70M64 110H70M64 120H70M60 130H70M64 140H70M64 150H70M64 160H70M64 170H70M60 180H70M64 190H70M64 200H70M64 210H70M64 220H70M60 230H70M64 240H70M64 250H70M64 260H70M64 270H70M60 280H70M64 290H70M64 300H70M64 310H70M64 320H70M60 330H70M64 340H70M64 350H70M64 360H70M64 370H70M60 380H70M64 390H70"/><text class="tl tc" x="60" y="22">metre rule</text><circle class="fi" cx="150" cy="105" r="7"/><path class="c1" d="M150 118V152" marker-end="url(#ah-phys)"/><text class="tl ti ta" x="160" y="140">v</text><path class="ln thick" d="M108 170H192M108 330H192"/><text class="tl te" x="104" y="174">A</text><text class="tl te" x="104" y="334">B</text><path class="ln-m thin dash" d="M192 170H238M192 330H238"/><path class="c1" d="M228 250V172" marker-end="url(#ah-phys)"/><path class="c1" d="M228 250V328" marker-end="url(#ah-phys)"/><text class="tl ti" x="238" y="254">s</text><text class="tl tc" x="150" y="250">oil</text><path class="ln-m thin" d="M160 100H204"/><text class="tl" x="208" y="104">steel sphere</text><text class="tl" x="226" y="408">tray</text><path class="ln-m thin" d="M196 60H250"/><text class="tl" x="254" y="64">oil surface</text></svg><figcaption>A sphere is released at the surface and reaches terminal speed before mark A. Its speed is the distance s between the marks divided by the time it takes to fall from A to B.</figcaption></figure>
:::

:::eg It is suggested that the terminal speed \(v\) of a small steel sphere falling through oil depends on the radius \(r\) of the sphere as \(v = kr^n\), where \(k\) and \(n\) are constants. Plan an investigation to find \(n\) and \(k\), using steel spheres of different radii, a tall cylinder of oil, and any other apparatus you need. (15 marks.)
**Defining the problem**
- The independent variable is the radius \(r\) of the sphere. [B1]
- The dependent variable is the terminal speed \(v\). [B1]
- Keep constant: the oil and its temperature (the viscosity changes with temperature), the material of the spheres (the same density), and the cylinder. [B1]

**Methods of data collection**
- Use the arrangement in the diagram: a tall cylinder of oil, two marks A and B a distance \(s\) apart low in the oil, and a rule beside it. [B1]
- Use at least six spheres, with radii from about \(1.0\,\mathrm{mm}\) to \(4.0\,\mathrm{mm}\). Measure each diameter with a micrometer at several places and in two directions, take the mean, and halve it to get \(r\). [B1]
- Release each sphere at the centre of the surface, away from the walls of the cylinder, and place mark A far enough below the surface that the sphere has reached terminal speed before it passes A. [B1]
- Measure the time \(t\) from A to B. A stopwatch has a reaction-time uncertainty of about \(0.2\,\mathrm{s}\), so use a video camera filming the rule and a timer, or two light gates linked to a logger. [B1]
- Measure the distance \(s\) between the marks with the metre rule, with the eye level with each mark to avoid parallax, and find \(v = s/t\). [B1]
- Keep the oil at a constant temperature: leave it in the room until it is at room temperature, and check with a thermometer at the start and at the end. [B1]

**Method of analysis**
- Taking logarithms of \(v = kr^n\) gives \(\lg v = n \lg r + \lg k\). [B1]
- Plot \(\lg v\) on the \(y\)-axis against \(\lg r\) on the \(x\)-axis. If the relationship is valid, the graph is a straight line. [B1]
- The gradient is \(n\), and the intercept on the \(y\)-axis is \(\lg k\), so \(k = 10^{\text{intercept}}\). [B1]

**Additional detail**
- Safety: spilt oil makes the floor slippery, so stand the cylinder in a tray, and wipe up spills at once. Wear eye protection. Take the spheres out with a magnet, not with fingers. [B1]
- Do a trial run to check that the marks are low enough: the times for two equal distances must be the same, which shows that the speed is constant. [B1]
- Repeat the timing for each sphere, and use the mean. [B1]
:::

Two things make this a model answer. Every mark point is **specific**: it names an instrument, a number, or a reason. And the analysis states **what** is plotted, **what** the gradient equals, and **how** to find the constant from it.

## Linearising an equation

Analysis begins with turning the equation you are given into the straight-line form \(y = mx + c\). Then a straight line supports the relationship, and the gradient and intercept hand you the constants.

:::key Three standard forms
| Equation | Rearranged | Plot (y against x) | Gradient | Intercept |
|---|---|---|---|---|
| \(y = mx + c\) | already straight | \(y\) against \(x\) | \(m\) | \(c\) |
| \(y = ax^n\) | \(\lg y = n\lg x + \lg a\) | \(\lg y\) against \(\lg x\) | \(n\) | \(\lg a\) |
| \(y = ae^{kx}\) | \(\ln y = kx + \ln a\) | \(\ln y\) against \(x\) | \(k\) | \(\ln a\) |
:::

For a power law, \(\ln\) works just as well as \(\lg\): \(\ln y = n \ln x + \ln a\), with the same gradient \(n\). For an exponential, \(\lg y\) against \(x\) is also straight, but the gradient is then \(k \lg e = 0.434k\), which is a trap if you forget it.

:::proof Why a power law is a straight line on log axes
Start from the power law \(y = ax^n\).
Take logarithms of both sides, using \(\lg(AB) = \lg A + \lg B\): \(\lg y = \lg a + \lg(x^n)\).
Use \(\lg(x^n) = n\lg x\): \(\lg y = n\lg x + \lg a\).
This is \(Y = mX + c\) with \(Y = \lg y\), \(X = \lg x\), \(m = n\) and \(c = \lg a\).
So a graph of \(\lg y\) against \(\lg x\) is a straight line, and its gradient is the power \(n\).
:::

:::eg A pendulum has \(T = 2\pi\sqrt{l/g}\). What should be plotted to find \(g\)?
Square both sides: \(T^2 = \dfrac{4\pi^2}{g}\,l\). [M1]

Plot \(T^2\) on the \(y\)-axis against \(l\) on the \(x\)-axis. [A1]

The line is straight and passes through the origin, and its gradient is \(\dfrac{4\pi^2}{g}\), so \(g = \dfrac{4\pi^2}{\text{gradient}}\). [A1] For a gradient of \(4.03\,\mathrm{s^2\,m^{-1}}\), \(g = \dfrac{4\pi^2}{4.03} = 9.80\,\mathrm{m\,s^{-2}}\). [C1] [A1]
:::

:::eg A capacitor discharges through a resistor \(R\): \(V = V_0 e^{-t/RC}\). What should be plotted to find \(C\)?
Take natural logarithms: \(\ln V = \ln V_0 - \dfrac{t}{RC}\). [M1]

Plot \(\ln V\) against \(t\). [A1] The gradient is \(-\dfrac{1}{RC}\) and the intercept is \(\ln V_0\). [A1]

So \(C = -\dfrac{1}{R \times \text{gradient}}\). [A1]
:::

:::eg A lamp obeys \(I = kV^n\), and a student plots \(\lg I\) against \(\lg V\). The gradient is \(0.58\), and \(\lg(I/\mathrm{mA}) = 2.02\) where \(\lg(V/\mathrm{V}) = 0\). Find \(n\) and \(k\).
\(\lg I = n\lg V + \lg k\), so the gradient is \(n = 0.58\). [B1]

The intercept is \(\lg k = 2.02\), so \(k = 10^{2.02} = 105\,\mathrm{mA\,V^{-0.58}}\). [C1] [A1]

The unit of \(k\) is whatever makes \(I = kV^n\) true: milliamperes per volt to the power 0.58.
:::

:::eg A stretched string of length \(L\) vibrating in its fundamental mode has frequency \(f = \dfrac{1}{2L}\sqrt{\dfrac{T}{\mu}}\), where \(T\) is the tension and \(\mu\) the mass per unit length. A graph of \(f\) against \(\sqrt{T}\) has gradient \(12.5\,\mathrm{Hz\,N^{-1/2}}\) for a string of length \(L = 0.600\,\mathrm{m}\). Find \(\mu\).
\(f = \dfrac{1}{2L\sqrt{\mu}}\,\sqrt{T}\), so a graph of \(f\) against \(\sqrt{T}\) is a straight line through the origin with gradient \(\dfrac{1}{2L\sqrt{\mu}}\). [M1]

\(\sqrt{\mu} = \dfrac{1}{2L \times \text{gradient}}\), so \(\mu = \dfrac{1}{4L^2 \times \text{gradient}^2}\). [C1]
\[\mu = \frac{1}{4 \times 0.600^2 \times 12.5^2} = 4.44 \times 10^{-3}\,\mathrm{kg\,m^{-1}}\] [A1]
:::

:::eg The power from a turbine is \(P = kv^3\), where \(v\) is the wind speed. Give two ways to find \(k\) by a straight-line graph.
Either plot \(P\) against \(v^3\): a straight line through the origin with gradient \(k\). [B1]

Or plot \(\lg P\) against \(\lg v\): \(\lg P = 3\lg v + \lg k\), a straight line with gradient 3 and intercept \(\lg k\). [B1] The second method also tests the power: a gradient that is not close to 3 means the power law is wrong.
:::

## Tables with logarithms

When a column holds logarithms, three rules apply (the first two are the ones students miss).

:::key Logarithm columns
- **The unit goes inside the logarithm.** Write the heading as \(\lg(L/\mathrm{cm})\) or \(\ln(V/\mathrm{V})\). The logarithm itself has no unit, because you can only take the logarithm of a number, and \(L/\mathrm{cm}\) is a pure number.
- **The number of decimal places in a logarithm equals the number of significant figures in the quantity.** One more decimal place is also accepted. So \(L = 76.5\,\mathrm{cm}\) (3 s.f.) gives \(\lg(L/\mathrm{cm}) = 1.884\) (or \(1.8837\)).
- **An uncertainty goes beside every value**, in its own column, in the same unit as the value (so in a log column, no unit).
:::

:::eg Complete the logarithm column for \(L / \mathrm{cm} = 76.5,\ 61.0,\ 45.5\), and explain how many decimal places are used.
Each length has 3 significant figures, so each logarithm has 3 decimal places. [B1]

| \(L\) / cm | \(\lg(L/\mathrm{cm})\) |
|---|---|
| 76.5 | 1.884 |
| 61.0 | 1.785 |
| 45.5 | 1.658 |

Values: \(\lg 76.5 = 1.884\), \(\lg 61.0 = 1.785\), \(\lg 45.5 = 1.658\). [A1]
:::

**Uncertainty in a logarithm.** If \(x\) has an absolute uncertainty \(\Delta x\), the uncertainty in \(\lg x\) is the largest value minus the value:
\[\Delta(\lg x) = \lg(x + \Delta x) - \lg x\]
For \(\ln\), the same pattern holds, \(\Delta(\ln x) = \ln(x + \Delta x) - \ln x\), and for small uncertainties this is close to the fractional uncertainty \(\Delta x/x\).

:::eg A diameter is \(d = 5.8 \pm 0.2\,\mathrm{cm}\). Find \(\lg(d/\mathrm{cm})\) with its uncertainty.
\(d\) has 2 significant figures, so give the logarithm to 2 decimal places: \(\lg 5.8 = 0.76\). [A1]

\(\Delta(\lg d) = \lg(6.0) - \lg(5.8) = 0.7782 - 0.7634 = 0.0147\), which is \(0.01\) to 1 significant figure and 2 decimal places. [C1] [A1]

So \(\lg(d/\mathrm{cm}) = 0.76 \pm 0.01\).
:::

:::eg Spot the error: a student plots \(\lg v\) against \(\lg r\) for the sphere in oil, with \(v\) in \(\mathrm{cm\,s^{-1}}\) and \(r\) in \(\mathrm{mm}\). The line passes through \((0.10,\ 0.40)\) and \((0.60,\ 1.40)\).
A student wrote this answer.

Line 1: heading "\(\lg v\) / cm s\(^{-1}\)" and "\(\lg r\) / mm"
Line 2: gradient \(= \dfrac{1.40 - 0.40}{0.60 - 0.10} = 2.0\,\mathrm{cm\,s^{-1}\,mm^{-1}}\)
Line 3: so \(n = 2.0\)

The gradient arithmetic is correct. [C1] **Line 1 is wrong: a logarithm has no unit, so the unit goes inside the logarithm, \(\lg(v/\mathrm{cm\,s^{-1}})\). That is also why line 2 is wrong: the gradient of a log-log graph is a pure number, the power \(n\), with no unit.** [A0]

Correct working: gradient \(= \dfrac{1.00}{0.50} = 2.0\), with no unit, so \(n = 2.0\). [A1]
:::

## Error bars and the worst acceptable line

Every value has an uncertainty, and a graph should show it. An **error bar** is a short line through a plotted point, as long as the uncertainty in that value, on each side. Draw it in the \(y\)-direction (from \(y - \Delta y\) to \(y + \Delta y\)) and, where the \(x\)-value is also uncertain, in the \(x\)-direction.

:::def Error bar
A line drawn through a plotted point, extending from the value minus its absolute uncertainty to the value plus its absolute uncertainty, to show the range in which the true value is expected to lie.
:::

You draw two lines. The **best-fit line** is the ordinary line, with the points balanced either side. The **worst acceptable line** is the steepest or the shallowest straight line that still **passes through all the error bars**. The difference between the two gradients is the uncertainty in the gradient.

:::def Worst acceptable line
The steepest (or the shallowest) straight line that still passes through every error bar on the graph. It shows the greatest (or least) gradient that the data allow, and so how uncertain the gradient is.
:::

:::formula Uncertainties from the two lines
\[\Delta(\text{gradient}) = |m_\text{best} - m_\text{worst}| \qquad\qquad \Delta(\text{intercept}) = |c_\text{best} - c_\text{worst}|\]
\(m\): gradient · \(c\): \(y\)-intercept. Draw the worst acceptable line dashed (or label it). If the graph has a false origin, find each intercept by substituting a point from that line and its gradient into \(y = mx + c\).
:::

:::steps
1. Draw the error bars on **every** point, in both directions where both quantities are uncertain.
2. Draw the best-fit line and read its gradient from two points far apart.
3. Draw the worst acceptable line: pivot it about the middle of the data until it is as steep (or as shallow) as it can be while still crossing every bar. Check **every** bar, including the middle ones.
4. Read its gradient. The uncertainty in the gradient is \(|m_\text{best} - m_\text{worst}|\).
5. Convert to a percentage if you need to: \(\dfrac{\Delta m}{m_\text{best}} \times 100\%\).
:::

:::eg A best-fit line has gradient \(2.48\) and the worst acceptable line has gradient \(2.61\). Give the gradient with its uncertainty and its percentage uncertainty.
\(\Delta m = |2.61 - 2.48| = 0.13\). [A1]

The gradient is \(2.48 \pm 0.13\). [A1]

The percentage uncertainty is \(\dfrac{0.13}{2.48} \times 100\% = 5.2\%\). [A1]
:::

The widget below does this for a real data set. Switch between the three graphs to see how the same data look when linearised in different ways, and edit a value to see how the worst acceptable line (dashed) and the gradient uncertainty react. If no line can pass through all the error bars, it says so: either the error bars are too small, or the relationship is not a straight line. The widget computes its best-fit line by least squares and finds the steepest line exactly, so for these data it gives gradients of \(-0.0399\) and \(-0.0417\,\mathrm{s^{-1}}\), where the lines drawn by hand in the next section give \(-0.0400\) and \(-0.0416\,\mathrm{s^{-1}}\). A difference in the third significant figure is normal: two careful students never draw exactly the same line by eye.

:::html
<div class="widget" data-w="phys-bestfit" data-preset="discharge"></div>
:::

## A full Question 2

:::html
<figure class="fig"><svg viewBox="15 -5 540 420" role="img" aria-label="Graph of the natural logarithm of V against t for a discharging capacitor, with t from 0 to 70 seconds and the vertical axis from minus 0.5 to 3.0. Six points have error bars that grow with t. A solid best-fit line falls from 2.48 at t = 0 to about 0.08 at t = 60. A dashed worst acceptable line is slightly steeper and passes through all six error bars. A dashed gradient triangle on the best-fit line has a horizontal side of 50 seconds and a vertical side of minus 2.00."><path class="gr" d="M70 20V356M136 20V356M202 20V356M268 20V356M334 20V356M400 20V356M466 20V356M532 20V356M70 356H532M70 308H532M70 260H532M70 212H532M70 164H532M70 116H532M70 68H532M70 20H532"/><path class="ax" d="M70 20V356H532"/><text class="ts tc" x="70" y="373">0</text><text class="ts tc" x="136" y="373">10</text><text class="ts tc" x="202" y="373">20</text><text class="ts tc" x="268" y="373">30</text><text class="ts tc" x="334" y="373">40</text><text class="ts tc" x="400" y="373">50</text><text class="ts tc" x="466" y="373">60</text><text class="ts tc" x="532" y="373">70</text><text class="ts te" x="64" y="360">−0.5</text><text class="ts te" x="64" y="312">0.0</text><text class="ts te" x="64" y="264">0.5</text><text class="ts te" x="64" y="216">1.0</text><text class="ts te" x="64" y="168">1.5</text><text class="ts te" x="64" y="120">2.0</text><text class="ts te" x="64" y="72">2.5</text><text class="ts te" x="64" y="24">3.0</text><text class="tl" x="36" y="6">ln (V / V)</text><text class="tl tc" x="301" y="400">t / s</text><path class="c1" d="M70 70L479.2 307.7"/><path class="c2 dash" d="M70 67.2L479.2 315.2"/><path class="ln thin" d="M136 107.2V109.6M132 107.2H140M132 109.6H140M202 144.3V147.9M198 144.3H206M198 147.9H206M268 182.4V187.7M264 182.4H272M264 187.7H272M334 220V227.9M330 220H338M330 227.9H338M400 257.1V268.7M396 257.1H404M396 268.7H404M466 290.5V307.2M462 290.5H470M462 307.2H470"/><path class="c4" d="M131 108.4H141M136 103.4V113.4M197 146.1H207M202 141.1V151.1M263 185H273M268 180V190M329 224H339M334 219V229M395 262.9H405M400 257.9V267.9M461 298.9H471M466 293.9V303.9"/><path class="ln-m thin dash" d="M136 108.3V300.3H466"/><text class="tl halo" x="146" y="196.8">Δy = −2.00</text><text class="tl tc halo" x="301" y="318.3">Δt = 50 s</text><path class="c1" d="M340 50H372"/><text class="tl" x="380" y="54">best-fit line</text><path class="c2 dash" d="M340 74H372"/><text class="tl" x="380" y="78">worst acceptable line</text><path class="ln thin" d="M356 88V104M352 88H360M352 104H360"/><text class="tl" x="380" y="102">error bar</text></svg><figcaption>ln (V / V) against t. The error bars lengthen as V falls, because a fixed uncertainty of 0.1 V is a larger fraction of a smaller voltage. The dashed worst acceptable line is the steepest line that still passes through every bar.</figcaption></figure>
:::

:::eg A capacitor of capacitance \(C\) discharges through a resistor \(R = 50 \pm 1\,\mathrm{k\Omega}\). The p.d. is \(V = V_0 e^{-t/RC}\). The table gives \(V\) at times \(t\), each with an uncertainty \(\Delta V = 0.1\,\mathrm{V}\). The graph above shows \(\ln(V/\mathrm{V})\) against \(t\) with error bars. Determine \(C\) and its uncertainty.

| \(t\) / s | \(V\) / V | \(\Delta V\) / V |
|---|---|---|
| 10 | 8.0 | 0.1 |
| 20 | 5.4 | 0.1 |
| 30 | 3.6 | 0.1 |
| 40 | 2.4 | 0.1 |
| 50 | 1.6 | 0.1 |
| 60 | 1.1 | 0.1 |

**The table.** \(V\) has 2 significant figures, so \(\ln(V/\mathrm{V})\) needs 2 decimal places, and one more is allowed: [B1]
\(\Delta \ln V = \ln(V + \Delta V) - \ln V\). [C1]

| \(t\) / s | \(\ln(V/\mathrm{V})\) | \(\Delta\ln(V/\mathrm{V})\) |
|---|---|---|
| 10 | 2.079 | 0.012 |
| 20 | 1.686 | 0.018 |
| 30 | 1.281 | 0.027 |
| 40 | 0.875 | 0.041 |
| 50 | 0.470 | 0.061 |
| 60 | 0.095 | 0.087 |

The values and their uncertainties are as shown. [A1]

**The graph.** Plot \(\ln(V/\mathrm{V})\) against \(t\), with error bars of length \(\pm\Delta \ln V\) on every point. [B1] Draw the best-fit line, with the points balanced about it. [B1] Draw the worst acceptable line: the steepest line that passes through all six error bars. [B1]

**The gradient.** Best-fit line through \((10,\ 2.08)\) and \((60,\ 0.08)\): [C1]
\[m_\text{best} = \frac{0.08 - 2.08}{60 - 10} = -0.0400\,\mathrm{s^{-1}}\] [A1]
Worst acceptable line through \((10,\ 2.09)\) and \((60,\ 0.01)\):
\[m_\text{worst} = \frac{0.01 - 2.09}{60 - 10} = -0.0416\,\mathrm{s^{-1}}\] [A1]
\[\Delta m = |-0.0416 - (-0.0400)| = 0.0016\,\mathrm{s^{-1}}, \quad \text{a fractional uncertainty of } \frac{0.0016}{0.0400} = 4.0\%\] [A1]

**The capacitance.** \(\ln V = \ln V_0 - \dfrac{t}{RC}\), so the gradient is \(-\dfrac{1}{RC}\) and \(RC = \dfrac{1}{0.0400} = 25.0\,\mathrm{s}\). [C1]
\[C = \frac{25.0}{50 \times 10^{3}} = 5.0 \times 10^{-4}\,\mathrm{F}\] [A1]
Percentage uncertainty in \(C\): the gradient (4.0%) and \(R\) (\(1/50 = 2.0\%\)) add: \(4.0\% + 2.0\% = 6.0\%\). [M1]
\[\Delta C = 0.060 \times 5.0 \times 10^{-4} = 0.3 \times 10^{-4}\,\mathrm{F} \qquad C = (5.0 \pm 0.3) \times 10^{-4}\,\mathrm{F}\] [A1]

The unit of the gradient is \(\mathrm{s^{-1}}\), because \(\ln V\) has no unit. [B1]

**The intercept** gives the starting p.d. The best-fit line meets the vertical axis at \(\ln V_0 = 2.48\) and the worst acceptable line at \(2.51\), so \(\Delta(\ln V_0) = 0.03\). Then \(V_0 = e^{2.48} = 11.9\,\mathrm{V}\), and since \(\Delta(\ln V_0) = \Delta V_0/V_0\), \(\Delta V_0 = 0.03 \times 11.9 = 0.4\,\mathrm{V}\). So \(V_0 = (11.9 \pm 0.4)\,\mathrm{V}\). (Not marked above.)
:::

:::exam Reading a Question 2
Do the parts in the order the question sets them, and show each stage on its own line: the log values, the uncertainties, the plot, the two gradients, the constant, its percentage uncertainty, the final value with unit. Examiners follow your working. State the **unit** of every gradient and constant, and give the final uncertainty to 1 significant figure (2 at most), with the value to the same number of decimal places.
:::

:::board
AQA (7408) has no separate planning paper like Paper 5: it tests planning, data analysis and uncertainty through written questions inside its exam papers. The skills in this chapter carry over; the question style does not.
:::

:::try Start easy, finish at exam standard
Q: A student investigates how the period of a pendulum depends on its length. State the independent variable, the dependent variable, and one variable to be kept constant.
A: Independent: the length \(l\). Dependent: the period \(T\). Control: the mass of the bob (or the amplitude of the swing).
Q: The power from a wind turbine is \(P = kv^3\). A graph of \(\lg P\) against \(\lg v\) is plotted. What are the gradient and the intercept?
A: \(\lg P = 3\lg v + \lg k\). The gradient is 3 and the intercept is \(\lg k\).
Q: The activity of a sample is \(A = A_0 e^{-\lambda t}\). What should be plotted to find the decay constant, and what is the gradient?
A: Plot \(\ln A\) against \(t\). \(\ln A = \ln A_0 - \lambda t\), so the gradient is \(-\lambda\).
Q: A frequency \(f\) is related to a tension \(T\) by \(f = \dfrac{1}{2L}\sqrt{\dfrac{T}{\mu}}\). What graph is a straight line through the origin?
A: \(f\) against \(\sqrt{T}\), with gradient \(\dfrac{1}{2L\sqrt{\mu}}\).
Q: A length is \(76.5\,\mathrm{cm}\). A student writes \(\lg 76.5 = 1.88\). What is wrong, and what should be written in the column?
A: \(76.5\,\mathrm{cm}\) has 3 significant figures, so its logarithm needs 3 decimal places: \(1.884\). The heading should be \(\lg(L/\mathrm{cm})\), with the unit inside.
Q: A value is \(x = 2.5 \pm 0.1\) (2 s.f.). Find \(\lg x\) with its uncertainty.
A: \(\lg 2.5 = 0.40\), and \(\Delta(\lg x) = \lg 2.6 - \lg 2.5 = 0.0170 \approx 0.02\). So \(\lg x = 0.40 \pm 0.02\).
Q: The best-fit gradient is \(2.48\) and the worst acceptable gradient is \(2.61\). Find the uncertainty in the gradient and its percentage.
A: \(2.61 - 2.48 = 0.13\), and \(\dfrac{0.13}{2.48} \times 100\% = 5.2\%\).
Q: On an oscilloscope the time-base is \(2.0\,\mathrm{ms}\) per division, and one complete cycle covers \(5.0\) divisions. Find the frequency.
A: \(T = 5.0 \times 2.0 = 10\,\mathrm{ms}\), so \(f = 1/0.010 = 100\,\mathrm{Hz}\).
Q: A card \(0.050\,\mathrm{m}\) wide blocks a light gate for \(0.020\,\mathrm{s}\). What is its speed?
A: \(v = \dfrac{0.050}{0.020} = 2.5\,\mathrm{m\,s^{-1}}\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A student plans to find how the height \(h\) to which a ball bounces depends on the height \(H\) from which it is dropped. State the independent variable, the dependent variable, and one variable to be kept constant.
A: Independent variable: the drop height \(H\). [B1] Dependent variable: the bounce height \(h\). [B1] Control: the same ball and the same surface (or the same temperature of the ball). [B1]
Q: [2 marks] ★ The flow rate \(Q\) of water through a pipe depends on the radius \(r\) of the pipe as \(Q = kr^n\). State what to plot to find \(n\), and what the gradient and intercept are.
A: Plot \(\lg Q\) against \(\lg r\), because \(\lg Q = n\lg r + \lg k\). [B1] The gradient is \(n\) and the intercept is \(\lg k\). [B1]
Q: [2 marks] ★ Give \(\lg(L/\mathrm{cm})\) for \(L = 45.5\,\mathrm{cm}\), and \(\lg(V/\mathrm{V})\) for \(V = 6.0\,\mathrm{V}\), each to a suitable number of decimal places.
A: \(\lg 45.5 = 1.658\) (3 s.f. so 3 decimal places). [B1] \(\lg 6.0 = 0.78\) (2 s.f. so 2 decimal places; 0.778 is also accepted). [B1]
Q: [2 marks] ★★ A diameter is \(5.8 \pm 0.2\,\mathrm{cm}\). Find \(\lg(d/\mathrm{cm})\) and its absolute uncertainty.
A: \(\lg 5.8 = 0.76\). [A1] \(\Delta(\lg d) = \lg 6.0 - \lg 5.8 = 0.0147 \approx 0.01\). [A1]
Q: [4 marks] ★★ A graph of \(x\) against \(t\) has a best-fit line through \((2.0\,\mathrm{s},\ 3.5\,\mathrm{m})\) and \((10.0\,\mathrm{s},\ 9.1\,\mathrm{m})\), and a worst acceptable line through \((2.0\,\mathrm{s},\ 3.8\,\mathrm{m})\) and \((10.0\,\mathrm{s},\ 9.0\,\mathrm{m})\). Find the gradient with its uncertainty, and the percentage uncertainty.
A: Best gradient: \(\dfrac{9.1 - 3.5}{10.0 - 2.0} = 0.70\,\mathrm{m\,s^{-1}}\). [A1] Worst gradient: \(\dfrac{9.0 - 3.8}{10.0 - 2.0} = 0.65\,\mathrm{m\,s^{-1}}\). [A1] Uncertainty: \(0.70 - 0.65 = 0.05\,\mathrm{m\,s^{-1}}\), so the gradient is \((0.70 \pm 0.05)\,\mathrm{m\,s^{-1}}\). [A1] Percentage: \(\dfrac{0.05}{0.70} \times 100\% = 7.1\%\). [A1]
Q: [4 marks] (#phys.oscillations) ★★ A graph of \(T^2\) against \(l\) for a pendulum has gradient \((4.02 \pm 0.12)\,\mathrm{s^2\,m^{-1}}\). Use \(T^2 = \dfrac{4\pi^2}{g}\,l\) to find \(g\) with its percentage and absolute uncertainty.
A: \(g = \dfrac{4\pi^2}{\text{gradient}} = \dfrac{4\pi^2}{4.02}\) [C1] \(= 9.82\,\mathrm{m\,s^{-2}}\). [A1] The percentage uncertainty in the gradient is \(\dfrac{0.12}{4.02} \times 100\% = 3.0\%\), which is also the percentage uncertainty in \(g\). [C1] \(\Delta g = 0.030 \times 9.82 = 0.3\,\mathrm{m\,s^{-2}}\), so \(g = (9.8 \pm 0.3)\,\mathrm{m\,s^{-2}}\). [A1]
Q: [15 marks] ★★★ A strip of conducting putty has a rectangular cross-section. It is suggested that its resistance \(R\) is proportional to its length \(l\). Plan an investigation to test this and to find the resistivity of the putty. You have a power supply, a variable resistor, meters, a ruler, calipers and connecting wires, and any other common apparatus.
H: Name the independent variable, the dependent variable and two control variables. For the cross-section, think how a strip of constant width and thickness can be made.
H: The analysis should say what is plotted, what the gradient is, and how the resistivity follows from it.
A: Defining the problem: the independent variable is the length \(l\) of the putty between the contacts. [B1] The dependent variable is the resistance \(R\). [B1] Keep constant: the cross-section (width and thickness) of the strip, and the temperature. [B1]
Methods: press the putty into a rectangular trough or channel, so that it has a constant cross-section, and put two metal contacts into it. [B1] Draw the circuit: a power supply and variable resistor in series with an ammeter and the putty, and a voltmeter across the putty between the contacts. [B1] Vary \(l\) by moving one contact along the putty to at least six values, measured with a ruler beside the strip from contact to contact. [B1] Find \(R = V/I\) for each length. [B1] Measure the width and thickness of the strip with calipers at several places, and take the means. [B1] Use a low p.d. and a small current, so the putty does not heat. [B1]
Analysis: \(R = \dfrac{\rho l}{A}\), where \(A\) is the cross-sectional area. [B1] Plot \(R\) against \(l\): if \(R\) is proportional to \(l\), the graph is a straight line through the origin. [B1] The gradient is \(\rho/A\), so \(\rho = \text{gradient} \times A\), with \(A\) = mean width \(\times\) mean thickness. [B1]
Additional detail: safety: the putty can irritate the skin, so wear gloves when shaping it (or wash your hands afterwards). [B1] Repeat each reading and take the mean, and check the meters for zero errors before use. [B1] The contacts add a small resistance of their own, so the line may miss the origin slightly: a straight line with a small intercept still gives \(\rho\) from the gradient. [B1]
Q: [15 marks] ★★★ The current \(I\) through a filament lamp depends on the p.d. \(V\) across it as \(I = kV^n\), where \(k\) and \(n\) are constants. The table gives \(V\) (with negligible uncertainty) and \(I\), each \(I\) with an uncertainty \(\Delta I = 3\,\mathrm{mA}\).

| \(V\) / V | 1.0 | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|---|---|
| \(I\) / mA | 105 | 158 | 198 | 238 | 268 | 297 |

(a) Show that a graph of \(\lg I\) against \(\lg V\) is a straight line, and say what its gradient and intercept are. (b) Complete a table of \(\lg(V/\mathrm{V})\) and \(\lg(I/\mathrm{mA})\) to suitable decimal places. (c) Find \(\Delta(\lg I)\) for each point. (d) Plot the graph with error bars, a best-fit line and a worst acceptable line. (e) The best-fit line passes through \((0.100,\ 2.080)\) and \((0.700,\ 2.429)\), and the worst acceptable line through \((0.100,\ 2.070)\) and \((0.700,\ 2.430)\). Find \(n\) with its uncertainty. (f) Find \(k\), with its unit and its absolute uncertainty.
H: Only \(I\) has an uncertainty, so the error bars are vertical.
H: In (f), the intercept on the \(\lg I\) axis is where \(\lg V = 0\). Use the best-fit line through \((0.100,\ 2.080)\) with its gradient.
A: (a) \(\lg I = n\lg V + \lg k\) [B1] is of the form \(y = mx + c\), so the graph is a straight line, with gradient \(n\) and intercept \(\lg k\). [B1] (b) Headings \(\lg(V/\mathrm{V})\) and \(\lg(I/\mathrm{mA})\) with the units inside. [B1] \(\lg(V/\mathrm{V})\): 0.000, 0.301, 0.477, 0.602, 0.699, 0.778. [B1] \(\lg(I/\mathrm{mA})\): 2.021, 2.199, 2.297, 2.377, 2.428, 2.473. [B1] (c) \(\Delta(\lg I) = \lg(I + 3) - \lg I\) \(= 0.012,\ 0.008,\ 0.007,\) \(0.005,\ 0.005,\ 0.004\). [A1] (d) Points plotted correctly. [B1] Error bars of \(\pm\Delta(\lg I)\), which are longest at the smallest \(V\). [B1] A best-fit line with points balanced. [B1] A worst acceptable line through all the bars. [B1] (e) Best gradient \(= \dfrac{2.429 - 2.080}{0.700 - 0.100} = 0.582\). [A1] Worst gradient \(= \dfrac{2.430 - 2.070}{0.600} = 0.600\). [A1] \(\Delta n = 0.600 - 0.582 = 0.018 \approx 0.02\), so \(n = 0.58 \pm 0.02\). [A1] (f) Best-fit intercept: \(2.080 - 0.582 \times 0.100 = 2.022\), so \(k = 10^{2.022} = 105\,\mathrm{mA\,V^{-0.58}}\). [A1] Worst-line intercept: \(2.070 - 0.600 \times 0.100 = 2.010\), so \(10^{2.010} = 102\), and \(\Delta k = 105 - 102 = 3\): \(k = (105 \pm 3)\,\mathrm{mA\,V^{-0.58}}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A cell is connected to a variable resistor, and the p.d. \(V\) across the cell is plotted against the current \(I\) with \(V = E - Ir\). The axes of the graph start at \(I = 0.20\,\mathrm{A}\) and \(V = 0.90\,\mathrm{V}\) (a false origin). The best-fit line passes through \((0.20\,\mathrm{A},\ 1.34\,\mathrm{V})\) and \((0.60\,\mathrm{A},\ 1.02\,\mathrm{V})\), and the worst acceptable line through \((0.20\,\mathrm{A},\ 1.36\,\mathrm{V})\) and \((0.60\,\mathrm{A},\ 0.98\,\mathrm{V})\). Find the e.m.f. \(E\) and the internal resistance \(r\), each with its uncertainty.
H: The line does not reach \(I = 0\) on the grid. Substitute a point and the gradient into \(V = mI + c\) to find the intercept.
A: Best gradient: \(\dfrac{1.02 - 1.34}{0.60 - 0.20} = -0.80\,\Omega\), so \(r = 0.80\,\Omega\). [A1] Best intercept: \(1.34 = -0.80 \times 0.20 + c\) [M1] so \(E = c = 1.50\,\mathrm{V}\). [A1] Worst gradient: \(\dfrac{0.98 - 1.36}{0.40} = -0.95\,\Omega\), so \(\Delta r = 0.95 - 0.80 = 0.15\,\Omega\). [A1] Worst intercept: \(1.36 + 0.95 \times 0.20 = 1.55\,\mathrm{V}\), so \(\Delta E = 0.05\,\mathrm{V}\). [A1] \(E = (1.50 \pm 0.05)\,\mathrm{V}\) and \(r = (0.80 \pm 0.15)\,\Omega\). [A1]
Q: [6 marks] ★★★ A student wants to find out whether \(y = ax^2\) or \(y = ax^{1.5}\) describes a set of data, using a graph of \(\lg y\) against \(\lg x\). Each \(y\) has an uncertainty of 10%. (a) Show that the uncertainty in each \(\lg y\) is 0.041. (b) The line is drawn with the first and last error bars as its extreme points. Show that the uncertainty in the gradient is about \(\dfrac{2 \times 0.041}{\lg(x_\text{max}/x_\text{min})}\). (c) The two exponents are 0.5 apart. For the data to tell them apart, the uncertainty in the gradient must be less than half that: \(0.25\). Find the smallest ratio \(x_\text{max}/x_\text{min}\). (d) Comment on the range of \(x\) that you would choose.
H: For a rising line, the steepest line goes from the bottom of the first bar to the top of the last bar, and the shallowest does the reverse.
A: (a) \(\Delta(\lg y) = \lg 1.10 = 0.0414 \approx 0.041\). [A1] (b) The best-fit line goes through the middle of the first and last bars. The steepest line goes from the top of one end bar to the bottom of the other, so its gradient differs from the best by \(\dfrac{2 \times 0.041}{\Delta(\lg x)}\), where \(\Delta(\lg x) = \lg(x_\text{max}/x_\text{min})\). [M1] [A1] (c) \(\dfrac{2 \times 0.0414}{\lg(x_\text{max}/x_\text{min})} < 0.25\) [C1] gives \(\lg(x_\text{max}/x_\text{min}) > 0.331\), so the ratio is more than \(2.14\). [A1] (d) Use a range of a factor of 10 or more, so that the gradient uncertainty is about \(0.08\), comfortably smaller than the 0.25 needed. [B1]
:::

:::quiz
? For \(y = ae^{kx}\), which graph is a straight line with gradient \(k\)?
- \(y\) against \(x\)
- \(\lg y\) against \(\lg x\)
+ \(\ln y\) against \(x\)
- \(\ln y\) against \(\ln x\)
> Taking natural logarithms gives \(\ln y = kx + \ln a\), which is a straight line when \(\ln y\) is plotted against \(x\). Plotting \(\lg y\) against \(\lg x\) is the test for a power law, \(y = ax^n\).
? A length is \(76.5\,\mathrm{cm}\). Which entry for \(\lg\) of it, in a column headed \(\lg(L/\mathrm{cm})\), is correct?
- 1.88
+ 1.884
- 1.884 cm
- 1.9
> The length has 3 significant figures, so its logarithm has 3 decimal places (one more is also accepted). A logarithm has no unit, so "cm" is wrong, and 1.88 or 1.9 have too few decimal places.
? What is the worst acceptable line?
- The line through the first and last data points
- The line with the largest scatter of points either side
+ The steepest or shallowest line that still passes through every error bar
- The line that misses the most error bars
> It is the extreme line that the data still allow. Comparing its gradient with the best-fit gradient gives the uncertainty in the gradient.
? A graph of \(\ln V\) against \(t\) for a discharging capacitor has gradient \(-0.040\,\mathrm{s^{-1}}\). What is \(RC\)?
- 0.040 s
+ 25 s
- \(-25\) s
- 0.69 s
> The gradient is \(-1/(RC)\), so \(RC = 1/0.040 = 25\,\mathrm{s}\). A negative time constant is meaningless, and 0.69 mixes in \(\ln 2\).
? An oscilloscope has a Y-gain of \(5.0\,\mathrm{V}\) per division. A trace has a crest \(2.4\) divisions above the centre line. What is the peak p.d.?
- 2.4 V
- 0.48 V
+ 12 V
- 24 V
> The peak voltage is the number of divisions times the Y-gain: \(2.4 \times 5.0 = 12\,\mathrm{V}\). The peak-to-peak value would be twice this, 24 V.
? Which is a control variable in an investigation of how the extension of a wire depends on the load?
- The load
- The extension
+ The temperature and the material and diameter of the wire
- The number of readings taken
> The load is the independent variable and the extension is the dependent variable. A control variable is something that could affect the extension (the wire itself, the temperature), and so is kept the same.
? The best-fit gradient is \(2.48\) and the worst acceptable gradient is \(2.61\). What is the uncertainty in the gradient?
- 5.09
+ 0.13
- 1.05
- 2.48
> The uncertainty is the difference of the two gradients, \(2.61 - 2.48 = 0.13\). Adding them or dividing one by the other is not the method.
? Which is the best safety statement in a plan about oil in a measuring cylinder?
- Be careful with the oil.
+ Stand the cylinder in a tray and wipe up any spilt oil, because oil on the floor is a slipping hazard.
- Wear a lab coat.
- Do not drop the spheres.
> A safety mark needs a specific risk and a specific precaution that goes with it. "Be careful" and general statements score nothing.
:::

:::checklist What you can now do
- [ ] I can identify the independent, dependent and control variables, and describe how to change, measure and control each.
- [ ] I can draw a labelled diagram of a workable arrangement and name suitable instruments, including an oscilloscope, light gates, a motion sensor and a data logger.
- [ ] I can write a method of analysis: what to plot, what the gradient and intercept mean, and what shows the relationship is valid.
- [ ] I can add specific safety precautions, trials, repeats and a way to reduce a named error.
- [ ] I can rearrange equations of the forms \(y = mx + c\), \(y = ax^n\) and \(y = ae^{kx}\) so that a straight-line graph gives the constants.
- [ ] I can write logarithm columns with the unit inside the log and the right number of decimal places, and find the uncertainty in a logarithm.
- [ ] I can draw error bars, a best-fit line and a worst acceptable line, and find the gradient and intercept with their uncertainties.
- [ ] I can find a constant with its percentage and absolute uncertainty, and give the result to a sensible number of significant figures with its unit.
:::

:::recap
- Paper 5: 1 hour 15 minutes, 30 marks, two 15-mark questions. Question 1 is planning (defining the problem, methods of data collection, method of analysis, additional detail including safety). Question 2 is analysis, conclusions and evaluation, with an equation, data, and uncertainties.
- Plan checklist: variables; labelled diagram; how to change the independent variable and measure and control; what to plot and what the gradient is; specific safety; repeats and a trial.
- Oscilloscope: voltage = divisions \(\times\) Y-gain; time = divisions \(\times\) time-base; \(f = 1/T\); current from the p.d. across a known resistor. Light gate: \(v = d/t\); two gates give \(a = \Delta v/\Delta t\).
- \(y = ax^n\): plot \(\lg y\) against \(\lg x\), gradient \(n\), intercept \(\lg a\). \(y = ae^{kx}\): plot \(\ln y\) against \(x\), gradient \(k\), intercept \(\ln a\).
- Log columns: unit inside the log, \(\lg(L/\mathrm{cm})\); decimal places of the log = significant figures of the quantity; \(\Delta(\lg x) = \lg(x + \Delta x) - \lg x\).
- Error bars show the uncertainty in each point. Worst acceptable line: the steepest or shallowest line through all the bars. \(\Delta m = |m_\text{best} - m_\text{worst}|\), and the same for the intercept (using substitution when there is a false origin).
- A constant found from a gradient has the percentage uncertainty of the gradient plus those of any other quantities used (add percentages). Give the result as value \(\pm\) uncertainty with a unit.
:::

:::links
- explore: [Least-Squares Regression](https://phet.colorado.edu/en/simulations/least-squares-regression) · PhET · drag points and see the best-fit line and its residuals change
- explore: [Curve Fitting](https://phet.colorado.edu/en/simulations/curve-fitting) · PhET · fit lines and curves to data and see how well they match
- papers: [9702 Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-5/) · Physics & Maths Tutor · practise whole planning and analysis questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Paper 1 survival guide: multiple choice](#phys.exam.p1)
