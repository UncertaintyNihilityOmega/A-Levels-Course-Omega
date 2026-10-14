@chapter phys.practical
@title Practical skills: measurement, tables, graphs and uncertainty
@level as
@paper CAIE P3 (AS) · P5
@time 6–8 hours
@summary How to collect, record, plot and judge experimental data: reading instruments and correcting zero errors, timing oscillations, laying out tables and graphs to the marking conventions, estimating uncertainties, testing whether a quantity is constant, and evaluating a method.

:::why
Paper 3 is a laboratory exam: you are given apparatus and two hours, and every mark comes from what you do, record and conclude. It is 23% of the AS and 11.5% of the A Level, and no theory beyond the question's own instructions is needed, so a student who has practised the skills in this chapter can score well in it. The same skills (tables, graphs, uncertainties, evaluation) carry straight into Paper 5, which the next chapter covers.
:::

**Before you start**, you need the rules for uncertainty from [Physical quantities, units and uncertainty](#phys.units) and the idea of a straight-line graph from [Graphs and straight lines](#math.f.graphs).

:::try Warm-up
Q: A length is measured as \(2.40 \pm 0.05\,\mathrm{cm}\). What is the percentage uncertainty? (from [Physical quantities, units and uncertainty](#phys.units))
A: \(\dfrac{0.05}{2.40} \times 100\% = 2.1\%\).
Q: A velocity–time graph is a straight line from \(2.0\,\mathrm{m\,s^{-1}}\) at \(t = 0\) to \(14.0\,\mathrm{m\,s^{-1}}\) at \(t = 6.0\,\mathrm{s}\). What is the acceleration? (from [Kinematics](#phys.kinematics))
A: The acceleration is the gradient: \(\dfrac{14.0 - 2.0}{6.0} = 2.0\,\mathrm{m\,s^{-2}}\).
Q: A resistor carries \(0.32\,\mathrm{A}\) when the p.d. across it is \(4.8\,\mathrm{V}\). What is its resistance? (from [Electricity](#phys.electricity))
A: \(R = V/I = 4.8/0.32 = 15\,\Omega\).
:::

## What Paper 3 tests

Paper 3 (Advanced Practical Skills) lasts 2 hours and carries 40 marks. It has two questions, each worth 20 marks and each set for 1 hour, in **different areas of physics**. You need no prior knowledge of the theory: the question tells you what to do, and gives any equation you need.

| | Question 1 | Question 2 |
|---|---|---|
| What you do | collect data, plot a graph, draw conclusions | collect data and draw conclusions; a graph may or may not be needed |
| The method | works well if you follow it | deliberately inaccurate: you evaluate it and suggest improvements |
| Handling the apparatus | at least 7 marks (manipulation, measurement, observation) | at least 5 marks (collecting data) |
| Recording | at least 6 marks for presentation | at least 2 marks for recording |
| Thinking about the results | at least 4 marks for analysis | at least 10 marks for analysis, conclusions and evaluation |
| Spread across these | 3 more marks | 3 more marks |

The marks are for skills, not for getting the textbook value. An honest, well-presented set of readings with a sensible conclusion scores well even when the apparatus is poor.

:::steps
1. **Read the whole question first**, including the last part. It tells you what the graph or table is for, and how many sets of readings are wanted.
2. **Set up from the instructions and diagram.** Check each instrument for a zero error before you use it.
3. **Draw the results table before you measure**, with headings and units, so that you can write each reading as you take it.
4. **Take a first reading to see the range**, then spread your readings over the largest range the apparatus allows. For a graph, six sets of values is a sensible minimum, and you should follow any number the question gives.
5. **Repeat readings where that helps** (above all for timings) and record every reading, not only the mean.
6. **Watch the clock**: each question is one hour. A table and graph finished early are worth more than a perfect experiment with no analysis.
:::

## Instruments, resolution and zero error

Every instrument has a limit to what it can show. You choose the instrument by the size of the quantity: a micrometer for the thickness of a wire, a metre rule for a pendulum length.

:::def Resolution
The smallest change in a quantity that an instrument can show: the smallest division on an analogue scale, or the last digit on a digital display.
:::

:::def Zero error
A systematic error in which an instrument does not read zero when the quantity it measures is zero. A positive zero error makes every reading too large, so you subtract it from every reading. A negative zero error makes every reading too small, so you add it back.
:::

| Instrument | Resolution | Notes |
|---|---|---|
| millimetre rule | 1 mm | a length needs two readings, one at each end |
| vernier calipers | 0.1 mm (many read to 0.02 mm) | outside and inside diameters, depths |
| digital calipers | 0.01 mm | press zero with the jaws closed |
| micrometer screw gauge | 0.01 mm | use the ratchet; for wire diameters and small thicknesses |
| protractor | 1° | angles |
| digital stopwatch | 0.01 s | a hand timing is limited by reaction time, about 0.1 s to 0.2 s |
| top-pan balance | 0.1 g or 0.01 g | press tare with the empty container on |
| newton meter | its smallest division | check it reads zero before the load is hung |
| thermometer | 1 °C | read at eye level, with the bulb in the liquid |
| measuring cylinder | its smallest division | read the bottom of the meniscus |
| analogue meter | its smallest division | check the pointer rests on zero |
| digital meter | the last digit | the reading may drift: note the value you take |

Record every raw reading to the resolution of the instrument and no further: \(4\,\mathrm{cm}\) and \(4.000\,\mathrm{cm}\) are both wrong for a reading from a millimetre rule, which gives \(4.0\,\mathrm{cm}\).

### Reading a micrometer

A micrometer has two scales. The **sleeve** is a fixed scale in millimetres, with the whole-millimetre lines above the datum line and the half-millimetre lines below it. The **thimble** turns, and has 50 divisions around its edge. One full turn moves the spindle by 0.5 mm, so each thimble division is \(0.5/50 = 0.01\,\mathrm{mm}\).

:::html
<figure class="fig"><svg viewBox="20 8 510 180" role="img" aria-label="A micrometer scale. On the sleeve the millimetre lines above the datum line are numbered 0 to 5, and the half-millimetre line after 5 is visible just before the thimble edge. On the thimble, line 28 is level with the datum line. The reading is 5.5 millimetres plus 0.28 millimetres, which is 5.78 millimetres."><rect class="fm s-mute sw1" x="30" y="44" width="311.2" height="80"/><rect class="f1 s-acc sw2" x="281.2" y="18" width="230" height="132"/><path class="ln" d="M30 84H281.2"/><path class="ln thin" d="M50 84V68M90 84V68M130 84V68M170 84V68M210 84V68M250 84V68M70 84V96M110 84V96M150 84V96M190 84V96M230 84V96M270 84V96"/><text class="ts tc" x="50" y="61">0</text><text class="ts tc" x="90" y="61">1</text><text class="ts tc" x="130" y="61">2</text><text class="ts tc" x="170" y="61">3</text><text class="ts tc" x="210" y="61">4</text><text class="ts tc" x="250" y="61">5</text><path class="ln thin" d="M281.2 28H293.2M281.2 35H293.2M281.2 42H293.2M281.2 49H293.2M281.2 56H293.2M281.2 70H293.2M281.2 77H293.2M281.2 91H293.2M281.2 105H293.2M281.2 112H293.2M281.2 119H293.2M281.2 126H293.2M281.2 140H293.2M281.2 28H303.2M281.2 63H303.2M281.2 98H303.2M281.2 133H303.2"/><path class="c3" d="M281.2 84H315.2"/><text class="ts" x="308.2" y="32">20</text><text class="ts" x="308.2" y="67">25</text><text class="ts" x="308.2" y="102">30</text><text class="ts" x="308.2" y="137">35</text><text class="tl tc" x="150" y="140">sleeve: 5.5 mm</text><text class="tl" x="331.2" y="80">28 divisions</text><text class="tl" x="331.2" y="98">= 0.28 mm</text><text class="tl tc" x="200" y="176">reading = 5.5 mm + 0.28 mm = 5.78 mm</text></svg><figcaption>The sleeve shows 5.5 mm (the half-millimetre line after 5 is just visible). The thimble line level with the datum line is 28, which is 0.28 mm. The thimble edge sits a little past the 5.5 mm line, as it should for a reading of 5.78 mm.</figcaption></figure>
:::

:::steps
1. Close the jaws with the ratchet and read the **zero error**, with its sign. Check it again at the end.
2. Grip the object with the ratchet only. Never force the thimble.
3. Read the sleeve: the whole millimetres, plus 0.5 mm if the half-millimetre line is visible beyond the last whole line.
4. Read the thimble line that is level with the datum line, and multiply by 0.01 mm.
5. Add the two readings, then correct for the zero error.
:::

:::eg A wire is gripped in a micrometer. The sleeve and thimble show the reading in the figure above. With the jaws closed, the micrometer reads \(+0.03\,\mathrm{mm}\). Find the diameter of the wire.
Sleeve: \(5.5\,\mathrm{mm}\). Thimble: \(28 \times 0.01 = 0.28\,\mathrm{mm}\). The reading is \(5.5 + 0.28 = 5.78\,\mathrm{mm}\). [B1]

The zero error is positive, so every reading is too large by \(0.03\,\mathrm{mm}\). Subtract it: [C1]
\[d = 5.78 - 0.03 = 5.75\,\mathrm{mm}\] [A1]
:::

### Reading vernier calipers

A vernier scale lets you read between the lines of the main scale. On the common type, ten vernier divisions together span 9 mm, so each is 0.9 mm long, and each is 0.1 mm shorter than a main-scale division. Slide the jaws open, and the vernier line that lines up exactly with a main-scale line tells you the extra tenths of a millimetre.

:::html
<figure class="fig"><svg viewBox="20 30 580 170" role="img" aria-label="A vernier scale. The upper main scale is marked in millimetres from 20 to 33. The vernier zero lies between the 23 and 24 millimetre lines. The fourth vernier line is lined up with the 27 millimetre line, so the reading is 23 millimetres plus 0.4 millimetres, which is 23.4 millimetres."><rect class="fm s-mute sw1" x="30" y="36" width="394" height="48"/><rect class="f1 s-acc sw1" x="123.2" y="84" width="276" height="54"/><path class="ln thin" d="M40 84V62M68 84V70M96 84V70M124 84V70M152 84V70M180 84V62M208 84V70M236 84V70M264 84V70M292 84V70M320 84V62M348 84V70M376 84V70M404 84V70"/><text class="ts tc" x="40" y="54">20</text><text class="ts tc" x="180" y="54">25</text><text class="ts tc" x="320" y="54">30</text><path class="ln thin" d="M135.2 84V106M160.4 84V98M185.6 84V98M210.8 84V98M236 84V98M261.2 84V106M286.4 84V98M311.6 84V98M336.8 84V98M362 84V98M387.2 84V106"/><text class="ts tc" x="135.2" y="120">0</text><text class="ts tc" x="261.2" y="120">5</text><text class="ts tc" x="387.2" y="120">10</text><path class="c3" d="M236 62V106"/><text class="tl" x="436" y="60">main scale: 23 mm</text><text class="tl" x="436" y="88">4th line aligned</text><text class="tl" x="436" y="106">= 4 × 0.1 mm = 0.4 mm</text><text class="tl tc" x="230" y="184">reading = 23 mm + 0.4 mm = 23.4 mm</text></svg><figcaption>The upper scale is the main scale (in millimetres) and the lower scale is the vernier. The vernier zero is just past the 23 mm line, and the fourth vernier line is the one that lines up with a main-scale line (27 mm). Every other vernier line is out of line by a visible amount.</figcaption></figure>
:::

:::steps
1. Close the jaws and read the zero error, as for the micrometer.
2. Read the main scale at the vernier zero: the last whole millimetre **before** the zero line.
3. Find the vernier line that lines up best with any main-scale line, and multiply its number by the resolution (0.1 mm here).
4. Add the two, and correct for the zero error.
:::

Calipers that read to 0.02 mm work in exactly the same way, with fifty finer vernier lines and each one worth 0.02 mm.

:::eg The calipers in the figure read \(23.4\,\mathrm{mm}\) across a metal rod. With the jaws closed they read \(0.2\,\mathrm{mm}\). Find the diameter of the rod.
The reading is \(23 + 4 \times 0.1 = 23.4\,\mathrm{mm}\). The zero error is \(+0.2\,\mathrm{mm}\), so every reading is too large by that amount. [C1]
\[d = 23.4 - 0.2 = 23.2\,\mathrm{mm}\] [A1]
:::

### Meters, parallax and the meniscus

- **Analogue meters**: read the pointer with your eye directly in front of it. Many meters have a mirror strip behind the pointer: when the pointer hides its own reflection, your eye is in the right place.
- **Parallax** is the apparent shift of an object against a scale when your eye is not directly in front of it. It makes a rule read too high or too low. Put the eye at right angles to the scale, and bring the scale as close to the object as you can.
- A liquid in a narrow tube curves at its edge (the **meniscus**). Read the bottom of the curve with your eye level with it.
- **Digital meters** show the value to the last digit. If the last digit flickers, record the central value.
- Zero errors affect meters too. A reading of \(0.02\,\mathrm{A}\) with nothing connected is a zero error of \(+0.02\,\mathrm{A}\) in every later reading.

## Timing oscillations

A stopwatch can show \(0.01\,\mathrm{s}\), but you start and stop it by hand, with a reaction time of about \(0.1\,\mathrm{s}\) to \(0.2\,\mathrm{s}\) each time. That is the real uncertainty in a hand timing. For one swing of a pendulum, with a period near \(1.6\,\mathrm{s}\), it is an enormous percentage. The cure is to **time many oscillations** and divide: the reaction-time uncertainty is spread over all the oscillations.

:::lab Timing a pendulum accurately
:::steps
1. Clamp the string between two wooden blocks, so the length is fixed at the same point on every swing. Measure the length \(l\) from the lower edge of the clamp to the centre of the bob, with a rule fixed vertically beside the string.
2. Put a **fiducial marker** (a pin or a vertical strip of tape) behind the string at the centre of the swing. The bob moves fastest there, so the moment it crosses the marker is much easier to judge than the end of a swing, where the bob is almost still.
3. Displace the bob by a small angle (about \(5^\circ\)) and release it with no sideways push.
4. Start the stopwatch as the bob crosses the marker, counting this crossing as 0. Count the following crossings in the same direction, and stop the watch at 20.
5. Repeat the timing of 20 oscillations, and take the mean of the two times. Divide by 20 to get the period \(T\).
:::
:::

:::eg Two timings of 20 oscillations of a pendulum are \(31.6\,\mathrm{s}\) and \(31.2\,\mathrm{s}\). Find the period with its absolute and percentage uncertainty.
The mean time for 20 oscillations is \(\dfrac{31.6 + 31.2}{2} = 31.4\,\mathrm{s}\), so \(T = \dfrac{31.4}{20} = 1.57\,\mathrm{s}\). [C1]

For repeated readings, the uncertainty is **half the range**: \(\dfrac{31.6 - 31.2}{2} = 0.2\,\mathrm{s}\) in the time for 20 oscillations. [B1]

The 20 is a counted number with no uncertainty, so \(\Delta T = \dfrac{0.2}{20} = 0.01\,\mathrm{s}\), and \(T = (1.57 \pm 0.01)\,\mathrm{s}\). [A1]

Percentage uncertainty: \(\dfrac{0.01}{1.57} \times 100\% = 0.64\%\). [A1]

If one swing were timed by hand with the same \(0.2\,\mathrm{s}\) uncertainty, the percentage uncertainty would be \(\dfrac{0.2}{1.57} \times 100\% = 13\%\): twenty times larger.
:::

Choose the number of oscillations so that the whole timing lasts long enough to make the reaction time small, but not so long that the swing dies away or you lose count. Ten or twenty is usual.

## Tables of results

A table is marked on a short list of rules, and each is easy to satisfy.

:::key The rules for a table of results
- **One table** for the readings, with raw and calculated columns in the order you take or work them out.
- **Every heading is quantity / unit**: \(I\) / mA. The forms "\(I\) (mA)" and "\(I\) in mA" are also accepted. "\(I\) mA" and "mA" alone are not. A column with no unit (a ratio, or a log) needs no unit, but the heading still names the quantity.
- **Raw readings are recorded to the resolution of the instrument**, and every value in a column has the same number of decimal places. A millimetre rule gives \(0.300\,\mathrm{m}\), not \(0.3\,\mathrm{m}\) and not \(0.30000\,\mathrm{m}\).
- **Calculated values are given to \(n\) or \(n + 1\) significant figures**, where \(n\) is the smallest number of significant figures in the raw data used in that calculation. If \(V\) has 2 s.f. and \(I\) has 4 s.f., then \(R\) is given to 2 or 3 s.f.
- **Repeat readings are shown**: both timings, then the mean.
:::

:::eg Find the five errors in this table of pendulum results. The length was measured with a millimetre rule, and the times are for 20 oscillations.
| \(l\) / m | \(t_1\) s | \(t_2\) / s | \(T\) | \(T^2\) / s² |
|---|---|---|---|---|
| 0.3 | 22.06 | 21.94 | 1.100 | 1.2 |
| 0.4 | 25.31 | 25.45 | 1.269 | 1.6 |
| 0.5 | 28.45 | 28.3 | 1.418 | 2.0 |

1. The heading \(t_1\) s has no slash: it must be \(t_1\) / s. [B1]
2. The heading \(T\) has no unit: it must be \(T\) / s. [B1]
3. The lengths \(0.3\), \(0.4\), \(0.5\) are given to 0.1 m, but a millimetre rule reads to 0.001 m: they should be \(0.300\), \(0.400\), \(0.500\). [B1]
4. In the \(t_2\) column, \(28.3\) has one decimal place while the others have two: it should be \(28.27\) (the reading as taken). [B1]
5. The \(T^2\) values have 2 significant figures, but the times have 3 or 4, so \(T^2\) should be given to 3 or 4 significant figures: \(1.210\), \(1.610\), \(2.011\). [B1]
:::

The corrected table:

| \(l\) / m | \(t_1\) / s | \(t_2\) / s | \(T\) / s | \(T^2\) / s² |
|---|---|---|---|---|
| 0.300 | 22.06 | 21.94 | 1.100 | 1.210 |
| 0.400 | 25.31 | 25.45 | 1.269 | 1.610 |
| 0.500 | 28.45 | 28.27 | 1.418 | 2.011 |

Every number in the \(T\) and \(T^2\) columns is worked out from the unrounded mean time, not from a rounded \(T\).

:::tip Make the table do the work
Put the column you plot on the graph in the table, and calculate it for **every** row before you start plotting. A missing value in a calculated column is a lost presentation mark and, usually, a missing point on the graph.
:::

## Graphs

A graph is how you turn a set of readings into one reliable number. The marking rules are a checklist, and every item is within your control.

:::key The rules for a graph
- **Axes labelled quantity / unit** (\(T^2\) / s², \(l\) / m). The independent variable (the one you changed) goes on the horizontal axis, unless the question says otherwise.
- **Scales** of 1, 2 or 5 units per large square (or 10, 20, 50 or 0.1, 0.2, 0.5 and so on). Never 3, 4, 6, 7, 8 or 9. Number the axes at least every two large squares.
- **The points fill at least half the grid in both directions.** If they do not, use a **false origin**: start an axis at a value other than zero.
- **Plot every point to better than half a small square** as a small cross (\(\times\)) or dot with a diameter below 1 mm. Never a large blob.
- **A line of best fit**: a single thin straight line (or smooth curve) with points **balanced either side along its whole length**. Use a transparent ruler, and do not force it through the origin or through the first and last points.
- **One anomalous point** may be ignored in drawing the line, if you circle it and label it.
:::

:::def False origin
A graph axis that starts at a value other than zero, used so that the data fill the grid. The origin of the grid is then not the point (0, 0), so the line cannot be read off at \(x = 0\).
:::

### Choosing scales

:::eg A student has values of \(l\) from \(0.32\,\mathrm{m}\) to \(0.78\,\mathrm{m}\) and values of \(T^2\) from \(1.30\,\mathrm{s^2}\) to \(3.15\,\mathrm{s^2}\). The grid is 10 large squares wide (for \(l\)) and 14 large squares tall (for \(T^2\)). Choose scales.
For \(l\): the data range is \(0.78 - 0.32 = 0.46\,\mathrm{m}\). A scale of \(0.1\,\mathrm{m}\) per square covers 1.0 m of axis, so the data fill only 46% of the width. That fails the half-grid rule. A scale of \(0.05\,\mathrm{m}\) per square covers \(10 \times 0.05 = 0.50\,\mathrm{m}\): start the axis at \(0.30\,\mathrm{m}\) (a false origin) and it runs from 0.30 to 0.80, with the data filling \(0.46/0.50 = 92\%\). [B1]

For \(T^2\): a scale of \(0.1\,\mathrm{s^2}\) per square covers only \(1.4\,\mathrm{s^2}\), too little for the data. A scale of \(0.5\,\mathrm{s^2}\) per square covers \(7.0\,\mathrm{s^2}\), so the data fill only 26%. A scale of \(0.2\,\mathrm{s^2}\) per square covers \(14 \times 0.2 = 2.8\,\mathrm{s^2}\): start at \(1.2\,\mathrm{s^2}\), so the axis runs from 1.2 to 4.0 and the data fill \(1.85/2.8 = 66\%\). [B1]

A scale of \(0.04\,\mathrm{m}\) per square would also fit, but it is not allowed: scales are 1, 2 or 5 (times a power of ten). [B1]
:::

### Plotting and drawing the line

Mark each point with a small neat cross. Use the table, not your memory, and plot from the axes, not by eye. When all the points are plotted, look at the pattern before you draw anything. Does it look like a straight line? A curve? Is one point obviously out of line?

Draw the line of best fit with a sharp pencil and a transparent ruler, so that you can see the points on both sides. Balance the points: roughly as many above the line as below, and with the distances of the points above about equal to the distances below, along the whole line. The line need not pass through any point.

A point that is far off the trend is an **anomalous result**, probably from a misread instrument or a slip in the experiment. Circle it, label it "anomalous", and draw the line without it. Do not circle a point just because it is a little off the line: real data have scatter.

:::def Anomalous result
A reading that does not fit the pattern of the other readings, well beyond the scatter that random errors would produce. It is circled and labelled on a graph, and left out when the line of best fit is drawn.
:::

### The gradient and the intercept

For a straight line \(y = mx + c\), the gradient \(m\) is the change in \(y\) divided by the change in \(x\). The intercept \(c\) is the value of \(y\) at \(x = 0\).

:::steps
1. Choose two points **on the line** (not data points), far apart: more than half the length of the line.
2. Read their coordinates to better than half a small square and draw the gradient triangle with the line as its hypotenuse.
3. Gradient \(= \Delta y / \Delta x\), with units that match the axes (the unit of \(y\) divided by the unit of \(x\)).
4. Find the intercept. If the line reaches \(x = 0\) on the grid, read it. If the axis has a false origin, **substitute** one point from the line and the gradient into \(y = mx + c\) and solve for \(c\).
:::

:::html
<figure class="fig"><svg viewBox="25 -15 536 410" role="img" aria-label="Graph of spring length l in centimetres against load F in newtons, with a vertical axis starting at 13.0 centimetres. Six points are plotted as crosses along a rising straight line; the point at 4.0 newtons is circled and labelled anomalous. The best-fit line passes through (1.0, 13.3) and (6.0, 17.3), and a dashed gradient triangle has horizontal side 5.0 newtons and vertical side 4.0 centimetres."><path class="gr" d="M70 20V340M138 20V340M206 20V340M274 20V340M342 20V340M410 20V340M478 20V340M546 20V340M70 340H546M70 308H546M70 276H546M70 244H546M70 212H546M70 180H546M70 148H546M70 116H546M70 84H546M70 52H546M70 20H546"/><path class="ax" d="M70 20V340H546"/><text class="ts tc" x="70" y="357">0</text><text class="ts tc" x="138" y="357">1</text><text class="ts tc" x="206" y="357">2</text><text class="ts tc" x="274" y="357">3</text><text class="ts tc" x="342" y="357">4</text><text class="ts tc" x="410" y="357">5</text><text class="ts tc" x="478" y="357">6</text><text class="ts tc" x="546" y="357">7</text><text class="ts te" x="64" y="344">13.0</text><text class="ts te" x="64" y="312">13.5</text><text class="ts te" x="64" y="280">14.0</text><text class="ts te" x="64" y="248">14.5</text><text class="ts te" x="64" y="216">15.0</text><text class="ts te" x="64" y="184">15.5</text><text class="ts te" x="64" y="152">16.0</text><text class="ts te" x="64" y="120">16.5</text><text class="ts te" x="64" y="88">17.0</text><text class="ts te" x="64" y="56">17.5</text><text class="ts te" x="64" y="24">18.0</text><text class="tl" x="40" y="4">l / cm</text><text class="tl tc" x="308" y="384">F / N</text><path class="c2" d="M117.6 336.2L505.2 44.3"/><path class="c1" d="M133 320.8H143M138 315.8V325.8M201 263.2H211M206 258.2V268.2M269 224.8H279M274 219.8V229.8M337 116H347M342 111V121M405 109.6H415M410 104.6V114.6M473 71.2H483M478 66.2V76.2"/><circle class="c3" cx="342" cy="116" r="10"/><text class="tl te halo" x="326" y="108">anomalous point</text><path class="ln-m thin dash" d="M138 320.8H478V64.8"/><text class="tl tc halo" x="308" y="312.8">ΔF = 5.0 N</text><text class="tl te halo" x="470" y="196.8">Δl = 4.0 cm</text></svg><figcaption>Length of a spring against the load hung from it. The vertical axis starts at 13.0 cm (a false origin), so the line cannot be read at F = 0. The gradient triangle uses two points on the line, far apart, not data points. The circled point is anomalous and was left out when the line was drawn.</figcaption></figure>
:::

:::eg Use the graph above to find the gradient and the intercept, and explain what they mean. The spring obeys \(l = l_0 + F/k\), where \(l_0\) is its natural length and \(k\) its spring constant.
The line passes through \((1.0\,\mathrm{N},\ 13.3\,\mathrm{cm})\) and \((6.0\,\mathrm{N},\ 17.3\,\mathrm{cm})\), which are more than half the line apart. [B1]
\[\text{gradient} = \frac{17.3 - 13.3}{6.0 - 1.0} = 0.80\,\mathrm{cm\,N^{-1}}\] [C1] [A1]
The vertical axis starts at 13.0 cm, so the line does not reach \(F = 0\) on the grid. Substitute a point from the line, \((1.0, 13.3)\), into \(l = mF + c\): [M1]
\[13.3 = 0.80 \times 1.0 + c \quad\Rightarrow\quad c = 12.5\,\mathrm{cm}\] [A1]
The intercept \(l_0 = 12.5\,\mathrm{cm}\) is the natural length of the spring. The gradient is \(1/k\), the extension for each newton, so \(k = 1/0.80 = 1.25\,\mathrm{N\,cm^{-1}} = 125\,\mathrm{N\,m^{-1}}\). [A1]
:::

:::warn Graph marks lost every year
A tiny gradient triangle (the uncertainty in \(\Delta y/\Delta x\) is then huge). Gradient points taken from the table, not the line. A line forced through the origin when the data do not go there. A scale of 3 units per square. Plotted points that are blobs. A missing unit on an axis label. All of these are easy to avoid, and every one costs a mark.
:::

## Uncertainties

Every measurement has an uncertainty, and every result you calculate inherits uncertainty from the numbers it came from. The rules from [Physical quantities, units and uncertainty](#phys.units) are all that Paper 3 needs.

:::key Estimating and combining uncertainties
- **One reading, digital**: at least \(\pm 1\) in the last digit shown. **One reading, analogue**: about half the smallest division at each reading. A length on a millimetre rule needs two readings, so \(\pm 1\,\mathrm{mm}\).
- **Repeated readings**: half the range, \(\tfrac12(x_\text{max} - x_\text{min})\), or the resolution if that is larger.
- **Absolute** \(\Delta x\) (same unit as \(x\)); **fractional** \(\Delta x/x\); **percentage** \(\dfrac{\Delta x}{x} \times 100\%\).
- **Product or quotient**: add the percentage uncertainties. **Power** \(x^n\): multiply the percentage uncertainty by \(n\). **Sum or difference**: add the absolute uncertainties.
- Give the uncertainty to 1 s.f. (2 at most) and the value to the same number of decimal places.
:::

:::eg A student finds the acceleration of free fall from a pendulum, using \(g = \dfrac{4\pi^2 l}{T^2}\). The length is \(l = 0.610 \pm 0.001\,\mathrm{m}\). The period is found from the two timings of 20 oscillations in the earlier example, so \(T = 1.57 \pm 0.01\,\mathrm{s}\). Find \(g\) with its uncertainty.
Value: \(g = \dfrac{4\pi^2 \times 0.610}{1.57^2} = 9.770\,\mathrm{m\,s^{-2}}\). [C1]

Percentage uncertainties: \(l\): \(\dfrac{0.001}{0.610} = 0.16\%\). \(T\): \(\dfrac{0.01}{1.57} = 0.64\%\). [C1]

\(T\) is squared, so its percentage is doubled, and the percentages add:
\[\frac{\Delta g}{g} = 0.16\% + 2 \times 0.64\% = 1.4\%\] [M1]
\[\Delta g = 0.014 \times 9.770 = 0.14\,\mathrm{m\,s^{-2}}\] [A1]
To 1 s.f. the uncertainty is \(0.1\), so \(g = (9.8 \pm 0.1)\,\mathrm{m\,s^{-2}}\). [A1]

The timing contributes \(2 \times 0.64 = 1.3\%\) of the 1.4%, so the period is the dominant uncertainty. To reduce it, time more oscillations: the half-range uncertainty of \(0.2\,\mathrm{s}\) is then a smaller fraction of a longer time.
:::

:::exam "Most significant source of uncertainty"
Evaluation questions ask which measurement contributes most. Work out the percentage uncertainty of **each** measured quantity (squared quantities count twice). The biggest percentage wins. Then say which quantity it is and give the reason, for example "timing 20 oscillations, uncertainty \(\pm 0.2\,\mathrm{s}\) is 0.64% of the time, doubled because \(T\) is squared".
:::

## Testing a relationship

Paper 3 often says "it is suggested that \(k\) is constant" and asks whether the data support this. With two readings, you test it by comparing two values of \(k\).

:::def Percentage difference
The difference between two values of a quantity, divided by their mean, as a percentage: \(\dfrac{k_1 - k_2}{\tfrac12(k_1 + k_2)} \times 100\%\). It is used to compare the two values of a constant with the percentage uncertainty in it.
:::

:::steps
1. Calculate \(k\) for each set of readings. Keep the unrounded values.
2. Find the percentage difference between the two values of \(k\).
3. Compare it with the percentage uncertainty (the question gives one, or you estimate it from the uncertainties in the readings).
4. **If the percentage difference is less than the percentage uncertainty, the data support the suggestion** that \(k\) is constant, within the uncertainty. If it is greater, they do not.
:::

:::eg A student suggests that the resistance \(R = V/I\) of a metal wire is constant. She measures \(V = 1.0\,\mathrm{V}\) and \(I = 0.205\,\mathrm{A}\), then \(V = 4.0\,\mathrm{V}\) and \(I = 0.790\,\mathrm{A}\). She estimates the percentage uncertainty in \(R\) as 5%. Do the data support her suggestion?
\(R_1 = \dfrac{1.0}{0.205} = 4.88\,\Omega\) and \(R_2 = \dfrac{4.0}{0.790} = 5.06\,\Omega\). [C1]

Mean: \(\tfrac12(4.878 + 5.063) = 4.971\,\Omega\). Difference: \(5.063 - 4.878 = 0.185\,\Omega\).
\[\text{percentage difference} = \frac{0.185}{4.971} \times 100\% = 3.7\%\] [A1]
This is less than the 5% uncertainty, so the data support the suggestion that \(R\) is constant, within the uncertainty. [B1]

Agreement within the uncertainty does not **prove** that \(R\) is constant. It shows that these two readings cannot tell the difference. Taking more readings is how you tighten the conclusion.
:::

:::eg A student makes the same suggestion for a filament lamp. At \(V = 1.0\,\mathrm{V}\) the current is \(0.100\,\mathrm{A}\), and at \(V = 6.0\,\mathrm{V}\) it is \(0.250\,\mathrm{A}\). The percentage uncertainty in \(R\) is 5%. Do the data support the suggestion?
\(R_1 = \dfrac{1.0}{0.100} = 10\,\Omega\) and \(R_2 = \dfrac{6.0}{0.250} = 24\,\Omega\). [C1]
\[\text{percentage difference} = \frac{24 - 10}{\tfrac12(10 + 24)} \times 100\% = 82\%\] [A1]
This is far greater than 5%, so the data do **not** support the suggestion: the resistance of the lamp is not constant. [B1] (The filament is hotter at the higher p.d.)
:::

**Proportionality from a graph** works the same way. If \(y\) is proportional to \(x\), a graph of \(y\) against \(x\) is a straight line **through the origin**. Draw the best-fit line and decide whether it passes through the origin within the scatter of the points. In the pendulum data later in this chapter, the line of \(T^2\) against \(l\) has an intercept of about \(-0.002\,\mathrm{s^2}\), tiny compared with the \(0.01\,\mathrm{s^2}\) scatter, so \(T^2 \propto l\) is supported.

## Evaluation: limitations and improvements

In Question 2 the method is deliberately poor, and you must find the faults and mend them. Each answer needs three parts: **the quantity** involved, **why** it is a problem (usually a size or a comparison), and **a specific improvement**. The improvement must use other apparatus or a changed procedure: not a different experiment.

| Limitation (with the reason) | Improvement |
|---|---|
| Only two readings: a valid conclusion about a relationship needs more | Take at least six sets of readings across the whole range and plot a graph |
| The ball falls for only 0.5 s, so the reaction time of 0.2 s is a large percentage of the time | Video the fall next to a clock, or use light gates connected to an electronic timer |
| Hard to judge the instant the ball is released or lands | Release it with an electromagnet and stop the timer with a switch or microphone at the floor |
| Parallax when reading the position of the pointer on a rule | Fix the rule vertically beside the object; use a set square or a mirror strip to line the eye up |
| The wire is kinked, so the length between the clamps is not the length that stretches | Hang a small load on the wire first to straighten it |
| The resistor warms as the current flows, so its resistance changes | Switch off between readings, and keep the current small |
| Draughts move the paper (or flame, or pendulum) | Use a draught shield or repeat in a closed room |
| It is hard to judge the end of a swing, where the bob is almost at rest | Time from a fiducial marker at the centre of the swing |
| Large amplitude, so the period is not constant as the swing decays | Release from a small angle, measured with a protractor, and time only the first few swings |
| Hot water loses energy to the room, so the temperature rise is too small | Put the beaker in lagging, with a lid |
| A zero error on the instrument was not checked | Measure the zero error with nothing to measure, and subtract it from every reading |
| The diameter was measured once, but the wire may not be uniform | Measure at three places along the wire, at two angles at each, and take the mean |

:::warn Answers that score nothing
"Human error", "be more careful", "use more accurate equipment" (which?), "repeat the readings" (for what quantity, and what is done with them?), "the experiment was not fair" and "parallax" alone (parallax in which reading?). An examiner needs the quantity, the problem, and the fix. "Repeat the timing and take the mean, to reduce the effect of random error in the time" does score.
:::

## A full Question 1, and a Question 2 evaluation

:::eg A Question 1 for the pendulum. It is suggested that \(T^2 = kl\), where \(k\) is constant. Collect data, plot a graph, find \(k\), and use it to find \(g\), given \(T = 2\pi\sqrt{l/g}\).
**Setting up and measuring.**
- Clamp the pendulum between two wooden blocks, with a rule fixed vertically beside it. Check the stopwatch and rule read zero and are in good order. [B1]
- Measure \(l\) from the bottom of the clamp to the centre of the bob, to the nearest millimetre. [B1]
- Use six lengths from \(0.300\,\mathrm{m}\) to \(0.800\,\mathrm{m}\), a range of well over a factor of two. [B1]
- Time 20 oscillations from a fiducial marker at the centre of the swing, from a small angle, and repeat the timing for each length. [B1]

**The table** (raw times to 0.01 s, \(T\) and \(T^2\) to 4 s.f., the same as the least number in the times):

| \(l\) / m | \(t_1\) / s | \(t_2\) / s | \(\langle t\rangle\) / s | \(T\) / s | \(T^2\) / s² |
|---|---|---|---|---|---|
| 0.300 | 22.06 | 21.94 | 22.00 | 1.100 | 1.210 |
| 0.400 | 25.31 | 25.45 | 25.38 | 1.269 | 1.610 |
| 0.500 | 28.45 | 28.27 | 28.36 | 1.418 | 2.011 |
| 0.600 | 31.02 | 31.22 | 31.12 | 1.556 | 2.421 |
| 0.700 | 33.50 | 33.66 | 33.58 | 1.679 | 2.819 |
| 0.800 | 36.01 | 35.87 | 35.94 | 1.797 | 3.229 |

Headings are quantity / unit, all raw values keep two decimal places, and the calculated values have 4 s.f. [B1] [B1] [B1]

**The graph**: \(T^2\) / s² on the \(y\)-axis against \(l\) / m on the \(x\)-axis, scales of \(0.1\,\mathrm{m}\) and \(0.5\,\mathrm{s^2}\) per large square from zero, so the points fill more than half the grid. Six crosses, and a thin best-fit line with the points balanced about it. [B1] [B1] [B1]

:::plot The pendulum data. The line passes close to the origin, so \(T^2\) is proportional to \(l\).
--f "4.04*x+0*sqrt(0.84-x)+0*sqrt(x-0.27)" --x 0 1 --y 0 4 --pt "0.3,1.21" --pt "0.4,1.61" --pt "0.5,2.011" --pt "0.6,2.421" --pt "0.7,2.819" --pt "0.8,3.229" --xlabel "l / m" --ylabel "T² / s²" --xstep 0.1
:::

**The gradient.** The line passes through \((0.300,\ 1.21)\) and \((0.800,\ 3.23)\), which are the ends of the data, the full length of the line. [B1]
\[k = \text{gradient} = \frac{3.23 - 1.21}{0.800 - 0.300} = 4.04\,\mathrm{s^2\,m^{-1}}\] [C1] [A1]
**The conclusion.** The line is straight and passes through the origin (substituting \((0.300, 1.21)\) gives \(c = 1.21 - 4.04 \times 0.300 = -0.002\,\mathrm{s^2}\), about zero), so the data support \(T^2 = kl\). [B1]

Since \(T^2 = \dfrac{4\pi^2}{g}\,l\), the gradient is \(4\pi^2/g\), so
\[g = \frac{4\pi^2}{k} = \frac{4\pi^2}{4.04} = 9.77\,\mathrm{m\,s^{-2}}\] [C1] [A1]
:::

:::eg A Question 2 evaluation. A student drops a small table-tennis ball from a height \(h = 1.500 \pm 0.002\,\mathrm{m}\) measured with a tape, and times the fall three times with a stopwatch: \(0.52\,\mathrm{s}\), \(0.58\,\mathrm{s}\), \(0.55\,\mathrm{s}\). She uses \(g = 2h/t^2\). Find \(g\) and its uncertainty, then evaluate the method.
Mean time: \(\dfrac{0.52 + 0.58 + 0.55}{3} = 0.55\,\mathrm{s}\), with uncertainty half the range, \(\dfrac{0.58 - 0.52}{2} = 0.03\,\mathrm{s}\). [B1]

\(g = \dfrac{2 \times 1.500}{0.55^2} = 9.9\,\mathrm{m\,s^{-2}}\). [C1]

Percentage uncertainties: \(h\): \(\dfrac{0.002}{1.500} = 0.13\%\); \(t\): \(\dfrac{0.03}{0.55} = 5.5\%\), doubled because \(t\) is squared. [C1]
\[\frac{\Delta g}{g} = 0.13\% + 2 \times 5.5\% = 11\% \quad\Rightarrow\quad \Delta g = 0.11 \times 9.9 = 1.1\,\mathrm{m\,s^{-2}}\] [M1]
\[g = (9.9 \pm 1.1)\,\mathrm{m\,s^{-2}}\] [A1]

**Evaluation** (each limitation with the reason, then the improvement):
- The time of fall, 0.55 s, is short, and the stopwatch is started and stopped by hand: the reaction time of about 0.2 s is a large fraction of it. Use light gates connected to an electronic timer. [B1]
- The release and the landing are hard to judge by eye. Release the ball with an electromagnet, and stop the timer with a microphone or switch at the floor. [B1]
- Only one height was used, so the data cannot show that \(h = \tfrac12 g t^2\) holds. Use at least six heights from \(0.50\,\mathrm{m}\) to \(1.50\,\mathrm{m}\), and plot \(h\) against \(t^2\), whose gradient is \(g/2\). [B1]
- A light ball is slowed by air resistance, so \(t\) is too long and \(g\) too small. Use a small dense steel ball. [B1]
:::

:::board
AQA, OCR and Edexcel (UK) assess practical skills partly through a separate practical endorsement in the laboratory, and partly through written questions on methods, data and uncertainty. Edexcel IAL has written practical papers. The skills in this chapter (resolution, zero error, tables, graphs, uncertainties, evaluation) are the same everywhere; what differs is how they are assessed.
:::

:::eg Spot the error: the gradient of the spring graph. The graph of spring length \(l\) against load \(F\) (earlier in this chapter) has a best-fit line of gradient \(0.80\,\mathrm{cm\,N^{-1}}\). A student wrote this answer.
Line 1: "I take two points from the table: \((3.0\,\mathrm{N},\ 14.8\,\mathrm{cm})\) and \((4.0\,\mathrm{N},\ 16.5\,\mathrm{cm})\)."
Line 2: gradient \(= \dfrac{16.5 - 14.8}{4.0 - 3.0} = 1.7\,\mathrm{cm\,N^{-1}}\)
Line 3: "The spring has \(k = 1/1.7 = 0.59\,\mathrm{N\,cm^{-1}}\)."

The substitution in line 2 is correct, so the method mark stays. [C1] **Line 1 is wrong: the points must lie on the line of best fit, not be data points. Here they are also close together (only 1.0 N apart), and the second is the anomalous point, which was circled and left out when the line was drawn.** The answer is wrong by a factor of more than two, and the mark is lost. [A0]

Correct working: use two points on the line, far apart, such as \((1.0, 13.3)\) and \((6.0, 17.3)\): gradient \(= 4.0/5.0 = 0.80\,\mathrm{cm\,N^{-1}}\), so \(k = 1.25\,\mathrm{N\,cm^{-1}}\). [A1]
:::

:::try Start easy, finish at exam standard
Q: Give the resolution of a millimetre rule, a micrometer, and a digital stopwatch.
A: Millimetre rule: \(1\,\mathrm{mm}\). Micrometer: \(0.01\,\mathrm{mm}\). Digital stopwatch: \(0.01\,\mathrm{s}\) (but a hand timing is uncertain by about the reaction time, \(0.1\)–\(0.2\,\mathrm{s}\)).
Q: With its jaws closed, a micrometer reads \(-0.04\,\mathrm{mm}\). A wire is gripped and the reading is \(0.87\,\mathrm{mm}\). What is the diameter?
A: A negative zero error makes every reading too small, so add it back: \(0.87 - (-0.04) = 0.91\,\mathrm{mm}\).
Q: Vernier calipers (resolution \(0.1\,\mathrm{mm}\)) have a main-scale reading of \(41\,\mathrm{mm}\) before the vernier zero, and the 7th vernier line is lined up. There is no zero error. Give the reading.
A: \(41 + 7 \times 0.1 = 41.7\,\mathrm{mm}\).
Q: Which of these headings are accepted: \(I\) / mA, \(I\) (mA), \(I\) mA, mA?
A: \(I\) / mA and \(I\) (mA) are accepted. \(I\) mA and mA alone are not (the quantity must be named and the unit separated).
Q: A length of \(0.500\,\mathrm{m}\) is measured with a metre rule, with an uncertainty of \(\pm 1\,\mathrm{mm}\) (two readings). What is the percentage uncertainty?
A: \(\dfrac{0.001}{0.500} \times 100\% = 0.2\%\).
Q: \(V = 2.4\,\mathrm{V}\) (2 s.f.) and \(I = 0.153\,\mathrm{A}\) (3 s.f.). How many s.f. may \(R = V/I\) have, and what is a suitable value?
A: The least number of s.f. in the data is 2, so \(R\) has 2 or 3 s.f.: \(R = 15.69\ldots\,\Omega\), given as \(16\,\Omega\) or \(15.7\,\Omega\).
Q: Values from \(0\) to \(7.3\,\mathrm{N}\) are plotted on an axis of 10 large squares. Which scale should be used: 0.5, 1, or 3 N per square?
A: \(0.5\,\mathrm{N}\) per square covers only \(5\,\mathrm{N}\), too little. \(3\,\mathrm{N}\) per square is not allowed (scales are 1, 2 or 5). \(1\,\mathrm{N}\) per square covers \(10\,\mathrm{N}\), and the data fill 73% of it.
Q: A timing of 10 oscillations is \(14.8\,\mathrm{s}\), with an uncertainty of \(0.2\,\mathrm{s}\). Find the period, its absolute uncertainty, and its percentage uncertainty.
A: \(T = 14.8/10 = 1.48\,\mathrm{s}\), \(\Delta T = 0.2/10 = 0.02\,\mathrm{s}\), and the percentage uncertainty is \(\dfrac{0.2}{14.8} \times 100\% = 1.4\%\).
Q: Two values of a constant are \(2.5\) and \(2.7\). What is the percentage difference?
A: \(\dfrac{2.7 - 2.5}{\tfrac12(2.5 + 2.7)} \times 100\% = \dfrac{0.2}{2.6} \times 100\% = 7.7\%\).
Q: A student writes a temperature as \(25.0\,^\circ\mathrm{C}\), read from a thermometer marked in steps of \(1\,^\circ\mathrm{C}\). What is wrong with this?
A: The thermometer cannot show \(0.1\,^\circ\mathrm{C}\), so the reading is recorded to the resolution of the instrument, \(25\,^\circ\mathrm{C}\). Writing \(25.0\,^\circ\mathrm{C}\) claims a precision the thermometer does not have.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ A student heads the columns of a results table "Current mA", "p.d. V" and "R (Ω)". Write the headings in the form required, changing only those that need it.
A: Current: \(I\) / mA. [B1] p.d.: \(V\) / V. [B1] The heading \(R\) (Ω) is already acceptable.
Q: [1 mark] ★ A p.d. \(V = 4.5\,\mathrm{V}\) and a current \(I = 0.0312\,\mathrm{A}\) are measured. Give the resistance with a suitable number of significant figures.
A: \(R = 4.5/0.0312 = 144.2\,\Omega\). The least number of s.f. in the data is 2, so \(R\) is given to 2 or 3 s.f.: \(140\,\Omega\) or \(144\,\Omega\). [A1]
Q: [2 marks] ★ A p.d. varies from \(0.45\,\mathrm{V}\) to \(2.85\,\mathrm{V}\). The vertical axis of the grid has 14 large squares. Choose a scale and say where the axis starts.
A: \(0.2\,\mathrm{V}\) per large square (the axis then covers \(14 \times 0.2 = 2.8\,\mathrm{V}\)), starting at \(0.2\,\mathrm{V}\) or \(0.4\,\mathrm{V}\) (a false origin). [B1] The data then fill \(2.40/2.8 = 86\%\) of the axis, more than half, and \(0.1\) per square is too little, \(0.5\) per square too much. [B1]
Q: [3 marks] ★★ A graph of temperature \(\theta\) against time \(t\) has a false origin, so the axes start at \(t = 1.0\,\mathrm{min}\) and \(\theta = 20.0\,^\circ\mathrm{C}\). The best-fit line passes through \((2.0\,\mathrm{min},\ 28.0\,^\circ\mathrm{C})\) and \((10.0\,\mathrm{min},\ 52.0\,^\circ\mathrm{C})\). (a) Find the gradient. (b) Find the value of \(\theta\) at \(t = 0\).
A: (a) gradient \(= \dfrac{52.0 - 28.0}{10.0 - 2.0}\) [C1] \(= 3.0\,^\circ\mathrm{C\,min^{-1}}\). [A1] (b) \(28.0 = 3.0 \times 2.0 + c\), so \(c = 22.0\,^\circ\mathrm{C}\). [A1]
Q: [2 marks] (#phys.units) ★ A student times 20 oscillations of a mass on a spring and records \(27.4\,\mathrm{s}\), with an uncertainty of \(\pm 0.2\,\mathrm{s}\). Find the period with its absolute uncertainty, and the percentage uncertainty in the period.
A: \(T = 27.4/20 = 1.37\,\mathrm{s}\) and \(\Delta T = 0.2/20 = 0.01\,\mathrm{s}\), so \(T = (1.37 \pm 0.01)\,\mathrm{s}\). [B1] Percentage uncertainty \(= \dfrac{0.2}{27.4} \times 100\% = 0.73\%\). [A1]
Q: [3 marks] ★★ A student suggests that the spring constant \(k = F/x\) of a spring is constant. A load of \(1.0\,\mathrm{N}\) gives an extension of \(2.10\,\mathrm{cm}\), and \(4.0\,\mathrm{N}\) gives \(9.00\,\mathrm{cm}\). The percentage uncertainty in \(k\) is 5%. Do the results support the suggestion?
A: \(k_1 = 1.0/0.0210 = 47.6\,\mathrm{N\,m^{-1}}\) and \(k_2 = 4.0/0.0900 = 44.4\,\mathrm{N\,m^{-1}}\). [C1] Percentage difference \(= \dfrac{47.62 - 44.44}{\tfrac12(47.62 + 44.44)} \times 100\% = 6.9\%\). [A1] This is greater than the 5% uncertainty, so the results do not support the suggestion that \(k\) is constant. [B1]
Q: [8 marks] ★★★ A student determines the resistivity of a metal wire. She measures the diameter once, with a millimetre rule, and records \(1\,\mathrm{mm}\). She connects a \(1.00\,\mathrm{m}\) length of the wire to a cell, an ammeter and a voltmeter, switches on, and records one pair of readings of \(V\) and \(I\) while writing up her notes. She then does the same for a second length. Identify four limitations of this method and suggest an improvement for each.
H: Think about the size of the diameter measurement compared with the resolution of the rule.
H: What happens to a wire that carries a current for a long time?
A: Limitation 1: a millimetre rule has a resolution of \(1\,\mathrm{mm}\), as large as the diameter itself, so the percentage uncertainty in the diameter, and twice that in the cross-sectional area, is very large. [B1] Improvement: use a micrometer and measure the diameter at several places, at two angles at each, and take the mean. [B1]
Limitation 2: the current flows for a long time, so the wire heats up and its resistance increases. [B1] Improvement: switch off between readings, and use a small current. [B1]
Limitation 3: only two lengths, so she cannot show that the resistance is proportional to the length. [B1] Improvement: take at least six lengths over the largest range and plot \(R\) against \(l\), whose gradient is \(\rho/A\). [B1]
Limitation 4: the wire is not straight or taut along the rule, so the measured length is not the length that carries the current. [B1] Improvement: tape the wire straight and tight along a rule, and use a sliding contact at the marked length. [B1]
Q: [6 marks] ★★★ A ball rolls from rest down a ramp, and the time \(t\) taken to roll a distance \(s\) is measured. For constant acceleration \(a\), \(s = \tfrac12 a t^2\). A graph of \(s\) against \(t^2\) is plotted. (a) Calculate \(t^2\) for \(t = 3.20\,\mathrm{s}\), to a suitable number of significant figures. (b) The best-fit line passes through \((2.00\,\mathrm{s^2},\ 0.62\,\mathrm{m})\) and \((10.00\,\mathrm{s^2},\ 3.10\,\mathrm{m})\). Find its gradient. (c) Use the gradient to find \(a\). (d) Show that the line passes through the origin, and say why this is expected.
H: The gradient of \(s\) against \(t^2\) is not \(a\). Compare \(s = \tfrac12 a t^2\) with \(y = mx\).
A: (a) \(t^2 = 3.20^2 = 10.24 \approx 10.2\,\mathrm{s^2}\) (3 s.f., like \(t\)). [A1] (b) gradient \(= \dfrac{3.10 - 0.62}{10.00 - 2.00}\) [C1] \(= 0.310\,\mathrm{m\,s^{-2}}\). [A1] (c) \(s = \tfrac12 a t^2\), so the gradient is \(a/2\). [C1] Then \(a = 2 \times 0.310 = 0.62\,\mathrm{m\,s^{-2}}\). [A1] (d) Substitute \((2.00, 0.62)\) into \(s = mt^2 + c\): \(c = 0.62 - 0.310 \times 2.00 = 0.00\,\mathrm{m}\). The line passes through the origin, as expected because the ball starts at \(s = 0\) when \(t = 0\) and \(s = \tfrac12 a t^2\) has no constant term. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A student suggests that the resistance \(R = V/I\) of a resistor is constant. She measures \(R\) at five p.d.s, \(V = 1.0, 2.0, 3.0, 4.0, 5.0\,\mathrm{V}\), and finds \(R = 4.86, 4.92, 4.98, 5.04, 5.10\,\Omega\). She estimates the percentage uncertainty in each \(R\) as 5%. (a) Compare the first and last values, and say what she concludes. (b) Comment on all five values, and explain why more readings give a better test than two. (c) Say what graph would test the suggestion.
H: Look at the difference between each value of \(R\) and the next.
A: (a) Percentage difference \(= \dfrac{5.10 - 4.86}{\tfrac12(5.10 + 4.86)} \times 100\%\) [C1] \(= 4.8\%\). [A1] This is less than 5%, so with two readings she would conclude that \(R\) is constant within the uncertainty. [B1] (b) \(R\) rises by exactly \(0.06\,\Omega\) at every step: a steady trend, not random scatter. [B1] Two readings cannot tell a trend from scatter, but five in order show that \(R\) increases with \(V\) (the resistor is probably warming), so the suggestion is not well supported even though 4.8% is below 5%. [B1] (c) Plot \(R\) against \(V\). If \(R\) were constant the line would be horizontal (gradient zero within the uncertainty); here the gradient is \(0.06\,\Omega\,\mathrm{V^{-1}}\), clearly not zero. [B1]
Q: [6 marks] ★★★ A pendulum has \(T = 1.57\,\mathrm{s}\) and is timed by hand, with an uncertainty of \(\pm 0.2\,\mathrm{s}\) in any timing. (a) Find the percentage uncertainty in \(T\) if one oscillation is timed. (b) Show that timing \(N\) oscillations gives a percentage uncertainty in \(T\) that is \(1/N\) of that value. (c) How many oscillations must be timed to bring the percentage uncertainty in \(T\) below \(0.30\%\)? Why is it not sensible to time many more than this?
H: The time for \(N\) oscillations is \(NT\), and the same \(0.2\,\mathrm{s}\) applies to it.
A: (a) \(\dfrac{0.2}{1.57} \times 100\% = 12.7\%\). [A1] (b) The time for \(N\) oscillations is \(NT\), with uncertainty \(0.2\,\mathrm{s}\), so the percentage uncertainty in \(T\) is \(\dfrac{0.2}{NT} \times 100\%\) [M1] \(= \dfrac{1}{N} \times \dfrac{0.2}{T} \times 100\%\), which is \(1/N\) of the single-oscillation value. [A1] (c) \(\dfrac{0.2}{N \times 1.57} < 0.0030\) [C1] gives \(N > 42.5\), so at least 43 oscillations. [A1] A long timing lets the amplitude die away (the period is no longer the same) and makes it easy to lose count, so a moderate number of oscillations is used. [B1]
:::

:::quiz
? Which heading for a column of currents in milliamperes is accepted?
- \(I\) mA
- mA
- \(I\) milliamperes
+ \(I\) / mA
> The heading must name the quantity and give the unit separated from it, as in \(I\) / mA (\(I\) (mA) and \(I\) in mA are also accepted). "\(I\) mA" and "mA" alone are not.
? With its jaws closed, a micrometer reads \(+0.02\,\mathrm{mm}\). A wire gives a reading of \(3.45\,\mathrm{mm}\). What is the diameter?
- 3.47 mm
+ 3.43 mm
- 3.45 mm
- 3.65 mm
> A positive zero error makes every reading too large, so it is subtracted: \(3.45 - 0.02 = 3.43\,\mathrm{mm}\). Adding it (3.47 mm) is the usual slip.
? Why is the time for 20 oscillations measured rather than for one?
+ The reaction-time uncertainty is spread over all the oscillations, so the percentage uncertainty in the period is much smaller.
- The stopwatch is only accurate for times longer than 30 s.
- It removes systematic errors from the experiment.
- The pendulum swings with a different period when it is timed for longer.
> The absolute uncertainty in the total time is the same, whether it is for one swing or twenty, so it is a smaller fraction of the longer time. It does not remove systematic errors, and the period does not change.
? Which choice of two points gives the best gradient from a straight-line graph?
- Two data points that are next to each other
- The first and last data points, even if they are off the line
+ Two points on the best-fit line, far apart (more than half the line)
- Two points close to the origin
> The points must lie on the line, not be data points, and far apart so that \(\Delta y\) and \(\Delta x\) are large compared with the reading error.
? Two values of a constant are \(10.0\) and \(10.5\), and the percentage uncertainty in the constant is 3.0%. Do the data support the suggestion that the constant is the same?
+ No: the percentage difference is 4.9%, which is greater than 3.0%.
- Yes: the difference of 0.5 is less than 3.0.
- Yes: both values are 10 to 2 significant figures.
- No: any difference at all means the constant is not the same.
> The percentage difference is \(\dfrac{0.5}{10.25} \times 100\% = 4.9\%\), and it is compared with the percentage uncertainty. Comparing 0.5 with 3.0 mixes an absolute value with a percentage, and the test allows for the uncertainty: a small difference is not enough to reject the suggestion, but this one is too big.
? A graph has one point far from the others. What should be done?
- Include it, because every reading must be used
- Delete it and say nothing
+ Circle it and label it as anomalous, then draw the line without it
- Draw a line through it and the first point
> An obvious outlier is ignored in drawing the line, but must be shown and labelled. A point only slightly off the line is normal scatter and is not anomalous.
? Which is a valid improvement for "the reaction time is large compared with the 0.4 s fall"?
- Be more careful with the stopwatch
- Repeat the readings
+ Use a light gate connected to an electronic timer
- Use a more accurate stopwatch
> It must be a specific change of apparatus that removes the cause (hand timing). "Be more careful" and "repeat" do not address a reaction time, and a stopwatch with finer resolution does not either, because reaction time is the problem.
:::

:::checklist What you can now do
- [ ] I can read a micrometer and vernier calipers, find the zero error and correct for it, and give raw readings to the right resolution.
- [ ] I can time oscillations accurately with a fiducial marker and find the period with its uncertainty.
- [ ] I can lay out a table of results with correct headings, consistent decimal places and the right number of significant figures.
- [ ] I can choose scales (including a false origin), plot points, draw a line of best fit and circle an anomalous point.
- [ ] I can find the gradient and the intercept of a line, and say what they mean, including when the axis has a false origin.
- [ ] I can estimate absolute and percentage uncertainties, use half the range, and combine them by simple addition.
- [ ] I can decide whether data support a constant by comparing a percentage difference with the percentage uncertainty.
- [ ] I can find the limitations of a method, name the most significant source of uncertainty, and suggest specific improvements.
:::

:::recap
- Paper 3: 2 hours, 40 marks, two 20-mark questions in different areas of physics, no prior knowledge of the theory needed. Question 1 collects data and plots a graph; Question 2 evaluates a deliberately inaccurate method.
- Resolution is the smallest reading an instrument shows. Subtract a positive zero error from every reading (add back a negative one). Micrometer: sleeve + thimble \(\times\,0.01\,\mathrm{mm}\). Vernier: main scale + aligned line \(\times\) resolution.
- Time 20 oscillations from a fiducial marker at the centre of the swing, repeat, and divide: this cuts the percentage uncertainty in the period by a factor of 20 compared with timing one.
- Tables: headings quantity / unit; raw readings to the instrument's resolution with the same decimal places; calculated values to \(n\) or \(n + 1\) s.f.
- Graphs: labelled axes; scales of 1, 2 or 5; data fill more than half the grid (false origin if needed); small crosses; balanced best-fit line; circle one anomalous point; gradient from two points on the line, more than half the line apart; with a false origin find the intercept by substituting a point.
- Uncertainty: half the range for repeats; percentage = \(\Delta x/x \times 100\%\); add percentages for products and quotients, multiply by the power for powers, add absolute values for sums and differences.
- A constant is supported if the percentage difference between two values is less than the percentage uncertainty. Proportional: a straight line through the origin.
- Evaluation: name the quantity, give the reason, and suggest a specific improvement (other apparatus or procedure, not a different experiment). "Human error" and "repeat the readings" score nothing.
:::

:::links
- explore: [Curve Fitting](https://phet.colorado.edu/en/simulations/curve-fitting) · PhET · fit lines and curves to data and see how well they match
- papers: [9702 Paper 3 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-3/) · Physics & Maths Tutor · practise whole practical questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Planning, analysis and evaluation](#phys.planning)
