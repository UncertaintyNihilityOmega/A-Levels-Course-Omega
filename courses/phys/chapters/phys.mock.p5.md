@chapter phys.mock.p5
@title Mock paper: Paper 5 planning, analysis and evaluation
@level mock
@paper CAIE 9702 Paper 5
@time 1 h 15 min
@summary An original Paper 5: plan an experiment in an unfamiliar context, then analyse supplied data with error bars, worst acceptable lines and uncertainties. 1 hour 15 minutes, 30 marks, like the real Paper 5.

:::exam Instructions
**1 hour 15 minutes · 30 marks · 2 questions of 15 marks each.** Spend about 35 minutes on each question and keep the rest for checking.
- Answer both questions on paper. Question 2 needs graph paper, a ruler and a pencil.
- The contexts may be unfamiliar. Everything you need is in the question, and no equipment is available: you plan and analyse only.
- Show every stage of your working, give units, and give the final uncertainty to 1 significant figure (2 at most).
- Press Finish to see the mark scheme. For the graph, compare your gradient and its uncertainty with the accepted ranges. Revise with [Planning, analysis and evaluation](#phys.planning).
:::

:::try
Q: [15 marks] (#phys.planning) A hacksaw blade is clamped horizontally at one end. A small mass is fixed to the free end. When the free end is pulled down and released, the blade oscillates vertically with frequency \(f\). It is suggested that \(f\) depends on the free length \(L\) of the blade (the length that sticks out of the clamp) as

\[f = kL^{n}\]

where \(k\) and \(n\) are constants.

:::html
<figure class="fig small"><svg viewBox="20 80 300 120" role="img" aria-label="A block on a bench holding one end of a thin horizontal blade. A small mass hangs from the free end of the blade."><rect class="fm s-mute sw1" x="30" y="170" width="280" height="14"/><rect class="fm s-ink sw2" x="40" y="100" width="70" height="70"/><rect class="fa" x="110" y="116" width="180" height="4"/><rect class="fi" x="280" y="120" width="22" height="24"/></svg><figcaption>The starting picture, not to scale: a blade held at one end, with a small mass fixed at the free end. It is not labelled and it is not a plan.</figcaption></figure>
:::

Plan a laboratory experiment to test the relationship between \(f\) and \(L\).

Draw a diagram showing the arrangement of your equipment. Explain how your results could be used to determine \(k\) and \(n\). (15 marks)
A: **Defining the problem**

- The independent variable is the free length \(L\) of the blade, measured from the edge of the clamp to the mass. [B1]
- The dependent variable is the frequency \(f\) of the vertical oscillations. [B1]
- Keep constant: the mass fixed at the end, the same blade (so the same width, thickness and material), and the pressure of the clamp. [B1]

**Methods of data collection**

- A labelled diagram showing the blade held in a clamp or vice at the edge of the bench, the mass at the free end, and a metre rule beside the blade. [B1]
- Change \(L\) by sliding the blade through the clamp and tightening it again. Measure \(L\) with the metre rule from the edge of the clamp to the mass, with the eye level with the scale to avoid parallax. [B1]
- Measure \(f\): pull the free end down and release it, time 20 oscillations with a stopwatch, then \(T = t/20\) and \(f = 1/T\). (A video of the blade next to a clock, or a motion sensor connected to a data-logger, is also accepted.) [B1]
- Use at least five (preferably six) values of \(L\), spread evenly over a stated range such as 0.08 m to 0.25 m. [B1]
- Start each oscillation with the same small displacement (for example 1 cm below the rest position, set against a rule), so the amplitude is small and the same each time. [B1]
- Check that the blade oscillates vertically without twisting, and that the clamp does not slip when it is tightened. Use a set square to check that the blade is horizontal at rest. [B1]

**Method of analysis**

- Take logarithms: \(\lg f = n\lg L + \lg k\). [B1]
- Plot \(\lg f\) on the \(y\)-axis against \(\lg L\) on the \(x\)-axis. If the relationship is valid, the graph is a straight line. [B1]
- The gradient is \(n\), and the \(y\)-intercept is \(\lg k\), so \(k = 10^{\text{intercept}}\). [B1]

**Additional detail, including safety**

- Safety: a hacksaw blade has sharp teeth and can snap when it is bent. Cover the teeth with tape, wear eye protection and keep the displacement small. [B1]
- Repeat each timing at least once and take the mean of the periods. [B1]
- One more detail, for example: put a small marker at the centre of the oscillation and count each time the mass passes it; do a trial run to choose masses and lengths that give a clear oscillation; avoid draughts. [B1]

Other creditable points that gain no extra mark: use a mass large enough that the mass of the blade can be neglected; use a larger number of oscillations for the shortest lengths if the frequency is high; check that \(f\) falls when \(L\) rises.
:::

:::try
Q: [15 marks] (#phys.planning) A ball rolls from rest down a ramp of length \(s\) that makes an angle \(\theta\) with the horizontal. The time \(t\) taken to reach the bottom is measured. It is suggested that

\[t^{2} = \frac{14s}{5g}\cdot\frac{1}{\sin\theta}\]

where \(g\) is the acceleration of free fall. The length of the ramp is \(s = 1.200 \pm 0.005\,\mathrm{m}\), and the angle \(\theta\) is changed for each measurement.

:::html
<figure class="fig small"><svg viewBox="20 30 320 160" role="img" aria-label="A ramp in the shape of a right-angled triangle, high on the left and low on the right, with a ball at the top. A dimension arrow parallel to the sloping surface marks its length s, and an arc at the bottom right corner marks the angle theta with the horizontal."><path class="fm s-ink sw2" d="M40 70L320 170H40Z"/><circle class="fa" cx="88" cy="77.6" r="9"/><path class="ln-m thin dash" d="M40 70L48.1 47.4M320 170L328.1 147.4"/><path class="c1" d="M188.1 97.4L52.5 49" marker-end="url(#ah-phys)"/><path class="c1" d="M188.1 97.4L323.7 145.8" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="192" y="86">s</text><path class="ln-m thin" d="M280 170A40 40 0 0 1 282.3 156.5"/><text class="tl ti" x="250" y="164">θ</text></svg><figcaption>A ball is released from rest at the top of the ramp. Its length is s and its angle with the horizontal is θ.</figcaption></figure>
:::

The results are shown in the table. The uncertainty in each time is \(\pm 0.05\,\mathrm{s}\).

| \(\theta\) / \(^\circ\) | \(t\) / s | \(1/\sin\theta\) | \(t^2\) / \(\mathrm{s^2}\) | absolute uncertainty in \(t^2\) / \(\mathrm{s^2}\) |
|---|---|---|---|---|
| 5.0 | 2.01 | | | |
| 10.0 | 1.39 | | | |
| 15.0 | 1.16 | | | |
| 20.0 | 0.98 | | | |
| 25.0 | 0.91 | | | |
| 30.0 | 0.84 | | | |

(a) A graph of \(t^2\) on the \(y\)-axis against \(1/\sin\theta\) on the \(x\)-axis is plotted. Express the gradient in terms of \(s\) and \(g\). (1 mark)

(b) Calculate and record in the table values of \(1/\sin\theta\), of \(t^2\), and of the absolute uncertainty in \(t^2\). (2 marks)

(c) (i) Plot a graph of \(t^2\) against \(1/\sin\theta\). Include error bars for \(t^2\). (2 marks)

(ii) Draw the line of best fit and a worst acceptable straight line. Label both lines. (2 marks)

(iii) Determine the gradient of the line of best fit, and the absolute uncertainty in the gradient. (2 marks)

(d) (i) Use your gradient to determine \(g\), with its unit. (2 marks)

(ii) Determine the percentage uncertainty in your value of \(g\). (2 marks)

(e) Use your gradient to predict the time taken for the ball to roll down the ramp when \(\theta = 12.0^\circ\), with its absolute uncertainty. Take the uncertainty in \(\theta\) to be negligible. (2 marks)
A: (a) gradient \(= \dfrac{14s}{5g}\) [B1]

(b) Values of \(1/\sin\theta\) and \(t^2\), to 2 decimal places, with the absolute uncertainty \(\Delta(t^2) = t^2 \times 2\dfrac{\Delta t}{t} = 2t\,\Delta t\): [B1] for the values, [B1] for the uncertainties (the uncertainty to 1 or 2 significant figures, with the same decimal places as \(t^2\)).

| \(\theta\) / \(^\circ\) | \(t\) / s | \(1/\sin\theta\) | \(t^2\) / \(\mathrm{s^2}\) | absolute uncertainty in \(t^2\) / \(\mathrm{s^2}\) |
|---|---|---|---|---|
| 5.0 | 2.01 | 11.47 | 4.04 | 0.20 |
| 10.0 | 1.39 | 5.76 | 1.93 | 0.14 |
| 15.0 | 1.16 | 3.86 | 1.35 | 0.12 |
| 20.0 | 0.98 | 2.92 | 0.96 | 0.10 |
| 25.0 | 0.91 | 2.37 | 0.83 | 0.09 |
| 30.0 | 0.84 | 2.00 | 0.71 | 0.08 |

(c)(i) All six points plotted to within half a small square, on sensible scales that use more than half of each axis, with labelled axes and units. [B1]

Error bars drawn in the \(y\)-direction on every point, each of total length twice the uncertainty in the table (\(\pm 0.20\) for the first point, down to \(\pm 0.08\) for the last). [B1]

(ii) The line of best fit, with the points balanced either side of it (it should pass close to the origin). [B1]

The worst acceptable line: the steepest (or the shallowest) straight line that passes through all six error bars. It must be labelled as such. [B1]

:::html
<figure class="fig"><svg viewBox="20 20 560 360" role="img" aria-label="Graph of t squared in seconds squared against 1 over sine theta. Six points with short vertical error bars lie close to a rising best-fit line through about the origin. A dashed, steeper worst acceptable line passes through all six error bars."><path class="gr" d="M150 330V60M230 330V60M310 330V60M390 330V60M470 330V60M550 330V60M70 270H550M70 210H550M70 150H550M70 90H550"/><path class="ax" d="M70 50V330H560"/><text class="ts tc" x="70" y="347">0</text><text class="ts tc" x="150" y="347">2</text><text class="ts tc" x="230" y="347">4</text><text class="ts tc" x="310" y="347">6</text><text class="ts tc" x="390" y="347">8</text><text class="ts tc" x="470" y="347">10</text><text class="ts tc" x="550" y="347">12</text><text class="ts te" x="64" y="334">0</text><text class="ts te" x="64" y="274">1</text><text class="ts te" x="64" y="214">2</text><text class="ts te" x="64" y="154">3</text><text class="ts te" x="64" y="94">4</text><text class="tl" x="40" y="38">t² / s²</text><text class="tl tc" x="310" y="372">1/sin θ</text><path class="c1" d="M90.0 321.5L550.0 78.0"/><path class="c2 dash" d="M110.0 315.6L550.0 63.5"/><path class="ln thin" d="M528.9 75.5V99.7M524.9 75.5H532.9M524.9 99.7H532.9M300.4 205.7V222.4M296.4 205.7H304.4M296.4 222.4H304.4M224.5 242.3V256.2M220.5 242.3H228.5M220.5 256.2H228.5M187.0 266.5V278.3M183.0 266.5H191.0M183.0 278.3H191.0M164.6 274.9V285.8M160.6 274.9H168.6M160.6 285.8H168.6M150.0 282.6V292.7M146.0 282.6H154.0M146.0 292.7H154.0"/><path class="c4" d="M523.9 87.6H533.9M528.9 82.6V92.6M295.4 214.1H305.4M300.4 209.1V219.1M219.5 249.3H229.5M224.5 244.3V254.3M182.0 272.4H192.0M187.0 267.4V277.4M159.6 280.3H169.6M164.6 275.3V285.3M145.0 287.7H155.0M150.0 282.7V292.7"/><path class="c1" d="M120 90H152"/><text class="tl" x="160" y="94">best-fit line</text><path class="c2 dash" d="M120 114H152"/><text class="tl" x="160" y="118">worst acceptable line</text><path class="ln thin" d="M136 128V144M132 128H140M132 144H140"/><text class="tl" x="160" y="142">error bar</text></svg><figcaption>A model graph: the best-fit line has gradient 0.353 and the steepest worst acceptable line 0.382. The error bars are short because the uncertainty in t² is small compared with the range of the data.</figcaption></figure>
:::

(iii) Gradient of the best-fit line from a large triangle (at least half the length of the line), for example using the points \((2.0,\ 0.67)\) and \((11.0,\ 3.85)\), read from the line (not from the table unless the points lie on the line):

\[m = \frac{3.85 - 0.67}{11.0 - 2.0} = 0.353\,\mathrm{s^2}\] [B1] (accept a best-fit gradient from 0.34 to 0.37)

Gradient of the steepest worst acceptable line: \(\dfrac{4.06 - 0.62}{11.0 - 2.0} = 0.382\) (accept 0.37 to 0.39); of the shallowest: \(\dfrac{3.69 - 0.76}{11.0 - 2.0} = 0.326\) (accept 0.31 to 0.34).

The uncertainty is the difference between the best-fit and worst acceptable gradients: \(\Delta m = |0.382 - 0.353| = 0.029\), so \(m = 0.353 \pm 0.029\,\mathrm{s^2}\) [B1] (accept an uncertainty from 0.02 to 0.04)

(d)(i) \(g = \dfrac{14s}{5m} = \dfrac{14 \times 1.200}{5 \times 0.353}\) [C1]

\(g = 9.5\,\mathrm{m\,s^{-2}}\) [A1] (accept 9.0 to 9.9)

(ii) The percentage uncertainties add: \(\dfrac{\Delta g}{g} = \dfrac{\Delta m}{m} + \dfrac{\Delta s}{s} = \dfrac{0.029}{0.353} + \dfrac{0.005}{1.200} = 8.2\% + 0.4\%\) [C1]

\(= 8.6\%\), so \(g = (9.5 \pm 0.8)\,\mathrm{m\,s^{-2}}\) [A1] (accept 6% to 12%)

(e) \(t^2 = \dfrac{m}{\sin 12.0^\circ} = \dfrac{0.353}{0.2079} = 1.70\,\mathrm{s^2}\), so \(t = \sqrt{1.70} = 1.30\,\mathrm{s}\) [C1]

\(t\) has half the fractional uncertainty of \(t^2\): \(\dfrac{\Delta t}{t} = \tfrac12 \times 8.2\% = 4.1\%\), so \(\Delta t = 0.05\,\mathrm{s}\) and \(t = 1.30 \pm 0.05\,\mathrm{s}\) [A1] (accept \(t\) from 1.27 s to 1.34 s)
:::

Next: [Physics: the course map](#phys.overview)
