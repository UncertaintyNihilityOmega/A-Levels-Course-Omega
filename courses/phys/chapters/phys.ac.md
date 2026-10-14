@chapter phys.ac
@title Alternating currents
@level a2
@paper CAIE P4 (A Level)
@time 4–6 hours
@summary Alternating current and voltage, x = x₀ sin ωt, mean power and the r.m.s. value, half-wave and full-wave rectification with diodes, and how a capacitor smooths the rectified output.

:::why
The mains supply in your home is alternating current, but a phone, a laptop and a television all need direct current. Every plug-in charger therefore contains a transformer, a rectifier and a smoothing capacitor, which are the three ideas in this chapter and the last. You will learn how to describe an alternating supply with a single honest number, the r.m.s. value, and how to turn it into the steady voltage that electronics needs.
:::

**Before you start**, you need the induced e.m.f. of a rotating coil from [Electromagnetic induction](#phys.induction), the time constant of a capacitor discharging through a resistor from [Capacitance](#phys.capacitance), and power in a resistor and the diode from [Electricity](#phys.electricity).

:::try Warm-up
Q: A \(470\,\mu\mathrm{F}\) capacitor discharges through a \(2.0\,\mathrm{k\Omega}\) resistor. Find the time constant. (from [Capacitance](#phys.capacitance))
A: \(\tau = RC = 2.0 \times 10^{3} \times 470 \times 10^{-6} = 0.94\,\mathrm{s}\).
Q: A \(6.0\,\Omega\) resistor has a p.d. of 12 V across it. Find the power dissipated. (from [Electricity](#phys.electricity))
A: \(P = V^2/R = 12^2/6.0 = 24\,\mathrm{W}\).
Q: An oscillation has a frequency of 50 Hz. Find its angular frequency. (from [Oscillations](#phys.oscillations))
A: \(\omega = 2\pi f = 2\pi \times 50 = 314\,\mathrm{rad\,s^{-1}}\).
:::

## Alternating current and voltage

A **direct current** (d.c.) flows round a circuit in one direction. In an **alternating current** (a.c.) the charge carriers swing to and fro, so the current reverses direction again and again. The rotating coil in [Electromagnetic induction](#phys.induction) produces exactly this: an e.m.f. of the form \(E_0\sin\omega t\), which drives a current that follows it. Mains electricity comes from large generators of this kind, which is why it is a.c.

An alternating current or voltage is described by three numbers, which you read off a graph of it against time (or from an oscilloscope trace, as in [Waves](#phys.waves)).

:::def Period
The time taken for one complete cycle of the alternating current or voltage. Symbol \(T\), measured in seconds.
:::

:::def Frequency
The number of complete cycles per unit time: \(f = 1/T\). It is measured in hertz (Hz), \(1\,\mathrm{Hz} = 1\,\mathrm{s^{-1}}\).
:::

:::def Peak value
The maximum magnitude of the current or voltage, measured from zero (the amplitude). Symbols \(I_0\) and \(V_0\). The **peak-to-peak** value, from the lowest point to the highest, is twice as large.
:::

:::formula A sinusoidal alternating current or voltage
\[V = V_0\sin\omega t \qquad I = I_0\sin\omega t \qquad \omega = 2\pi f = \frac{2\pi}{T}\]
\(V, I\): the value at time \(t\) · \(V_0, I_0\): peak values · \(\omega\): angular frequency (\(\mathrm{rad\,s^{-1}}\)). The calculator must be in **radian** mode. For a current through a resistor, \(I = V/R\) at every instant, so the current is in phase with the voltage.
:::

:::html
<figure class="fig"><svg viewBox="10 0 600 265" role="img" aria-label="Graph of a sinusoidal voltage against time for two cycles. The curve peaks at 325 volts and bottoms out at minus 325 volts. A dashed line at 325 volts is the peak value and a dashed line at 230 volts is the r.m.s. value. A double-headed dimension above the first two crests shows the period T equal to 20 milliseconds."><path class="ax" d="M60 22V228M60 125H508"/><text class="tl ti te" x="54" y="26">V / V</text><path class="c1 sw2" d="M60 125L65.5 110.9L71 97.2L76.5 84.1L82 72.1L87.5 61.4L93 52.2L98.5 44.8L104 39.4L109.5 36.1L115 35L120.5 36.1L126 39.4L131.5 44.8L137 52.2L142.5 61.4L148 72.1L153.5 84.1L159 97.2L164.5 110.9L170 125L175.5 139.1L181 152.8L186.5 165.9L192 177.9L197.5 188.6L203 197.8L208.5 205.2L214 210.6L219.5 213.9L225 215L230.5 213.9L236 210.6L241.5 205.2L247 197.8L252.5 188.6L258 177.9L263.5 165.9L269 152.8L274.5 139.1L280 125L285.5 110.9L291 97.2L296.5 84.1L302 72.1L307.5 61.4L313 52.2L318.5 44.8L324 39.4L329.5 36.1L335 35L340.5 36.1L346 39.4L351.5 44.8L357 52.2L362.5 61.4L368 72.1L373.5 84.1L379 97.2L384.5 110.9L390 125L395.5 139.1L401 152.8L406.5 165.9L412 177.9L417.5 188.6L423 197.8L428.5 205.2L434 210.6L439.5 213.9L445 215L450.5 213.9L456 210.6L461.5 205.2L467 197.8L472.5 188.6L478 177.9L483.5 165.9L489 152.8L494.5 139.1L500 125"/><path class="ln-m thin dash" d="M60 35H500"/><text class="tl" x="508" y="39">325 V peak</text><path class="ln-m thin dash" d="M60 61.3H500"/><text class="tl" x="508" y="65.3">230 V r.m.s.</text><path class="ln-m thin dash" d="M60 215H500"/><text class="tl" x="508" y="219">−325 V</text><path class="ln-m thin dash" d="M115 12V35M335 12V35"/><path class="c1" d="M225 20H116" marker-end="url(#ah-phys)"/><path class="c1" d="M225 20H334" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="225" y="13">T = 20 ms</text><path class="ax" d="M60 240H508"/><path class="ax" d="M60 240V245"/><text class="ts tc" x="60" y="258">0</text><path class="ax" d="M170 240V245"/><text class="ts tc" x="170" y="258">10</text><path class="ax" d="M280 240V245"/><text class="ts tc" x="280" y="258">20</text><path class="ax" d="M390 240V245"/><text class="ts tc" x="390" y="258">30</text><path class="ax" d="M500 240V245"/><text class="ts tc" x="500" y="258">40</text><text class="tl" x="514" y="244">t / ms</text></svg><figcaption>The UK mains voltage \(V = 325\sin(100\pi t)\) plotted over two cycles. The peak value is 325 V and the period is 20 ms, so the frequency is 50 Hz. The lower dashed line marked 230 V is the r.m.s. value, which the next sections explain.</figcaption></figure>
:::

:::eg The mains voltage is \(V = 325\sin(100\pi t)\), with \(V\) in volts and \(t\) in seconds. Find the peak value, the frequency and the period. Find \(V\) at \(t = 2.5\,\mathrm{ms}\), and the first time at which \(V = 200\,\mathrm{V}\).
Compare with \(V = V_0\sin\omega t\): the peak value is \(V_0 = 325\,\mathrm{V}\) and \(\omega = 100\pi\,\mathrm{rad\,s^{-1}}\). [B1]

\[f = \frac{\omega}{2\pi} = \frac{100\pi}{2\pi} = 50\,\mathrm{Hz} \qquad T = \frac{1}{f} = 0.020\,\mathrm{s}\] [C1] [A1]

At \(t = 2.5 \times 10^{-3}\,\mathrm{s}\): \(\omega t = 100\pi \times 0.0025 = \pi/4\), so \(V = 325 \sin(\pi/4) = 325 \times 0.7071 = 230\,\mathrm{V}\). [A1]

For \(V = 200\,\mathrm{V}\): \(\sin\omega t = 200/325\), so \(\omega t = 0.6629\,\mathrm{rad}\) (calculator in radians, first solution), and \(t = 0.6629/(100\pi) = 2.1 \times 10^{-3}\,\mathrm{s}\), which is 2.1 ms. [A1]
:::

:::eg On an oscilloscope screen the trace of an alternating voltage is 6.0 divisions high from its lowest to its highest point, and one complete cycle is 4.0 divisions wide. The Y-gain is \(2.0\,\mathrm{V}\) per division and the time-base is \(5.0\,\mathrm{ms}\) per division. Find the peak voltage and the frequency.
Peak-to-peak voltage: \(6.0 \times 2.0 = 12\,\mathrm{V}\), so the peak value is half of this, \(V_0 = 6.0\,\mathrm{V}\). [C1] [A1]

Period: \(T = 4.0 \times 5.0 = 20\,\mathrm{ms}\), so \(f = 1/T = 1/0.020 = 50\,\mathrm{Hz}\). [C1] [A1]

The commonest slip is to call the whole screen height the peak. The peak is measured from the middle line.
:::

## Power in a resistor

Current through a resistor transfers energy whichever way it flows, because \(P = I^2R\) depends on \(I^2\), which is never negative. So an alternating current heats a resistor, even though its mean value over a cycle is zero.

At each instant, for \(I = I_0\sin\omega t\),
\[P = I^2R = I_0^2R\sin^2\omega t\]
The power is zero when the current is zero, and reaches its maximum \(P_0 = I_0^2R\) at each peak of the current, whether positive or negative. The power is never negative and it pulses at **twice** the frequency of the current.

:::plot The power in a resistor connected to a 50 Hz supply, as a fraction of the peak power. The horizontal line at 0.5 marks the mean power over a cycle.
--f "sin(pi*x/10)**2+0*sqrt(40-x)" --x 0 46 --y 0 1.3 --hline 0.5 --xlabel "t / ms" --ylabel "P / P₀" --pt "5,1,P₀@ne"
:::

The curve swings between 0 and \(P_0\), and it is symmetrical about the line at \(\tfrac12P_0\), so the mean is half the peak.

:::proof Why the mean of sin² is one half
We want the mean value of \(\sin^2\omega t\) over a whole number of cycles.
The identity \(\sin^2\theta + \cos^2\theta = 1\) holds at every instant, so \(\sin^2\) and \(\cos^2\) always add up to 1.
The cosine graph is the sine graph shifted by a quarter of a cycle, so over a whole cycle \(\cos^2\omega t\) takes exactly the same set of values as \(\sin^2\omega t\), and the two have the same mean.
Call this mean \(m\). Then \(m + m = 1\), so \(m = \tfrac12\).
Hence the mean power is \(\tfrac12 I_0^2R\), which is half the peak power \(I_0^2R\).
:::

:::formula Mean power in a resistive load
\[\langle P\rangle = \tfrac12 P_0 \qquad\text{where}\qquad P_0 = I_0^2R = \frac{V_0^2}{R} = I_0V_0\]
For a sinusoidal alternating current in a resistor, the mean power is **half** the maximum (peak) power. \(\langle P\rangle\) means "mean value of \(P\)".
:::

:::eg A heater of resistance \(25\,\Omega\) is connected to a sinusoidal supply with peak voltage 325 V. Find the peak power and the mean power.
Peak power: \(P_0 = \dfrac{V_0^2}{R} = \dfrac{325^2}{25} = 4225\,\mathrm{W}\), which is \(4.2\,\mathrm{kW}\) to 2 significant figures. [C1] [A1]

Mean power: \(\langle P\rangle = \tfrac12P_0 = 2112.5\,\mathrm{W}\) before rounding, so \(2.1\,\mathrm{kW}\). [A1]

This is the heating the owner pays for. The heater spends half its time near its peak and the rest below it, so the average is half the peak.
:::

## Root-mean-square values

Quoting the **mean** current would be useless, because over a whole cycle it is zero. Quoting the peak would overstate the heating. We want a single value that behaves like a steady current as far as heating is concerned. That value is the root-mean-square (r.m.s.) value.

:::def Root-mean-square current
The value of the steady direct current that would dissipate energy at the same average rate (the same mean power) in a resistor as the alternating current.
:::

The name is a recipe, read from the right: **square** the current, take the **mean** of the squares over a cycle, then take the square **root**. The same definition applies to the r.m.s. voltage.

:::proof Why the r.m.s. value is the peak divided by the square root of two
A direct current \(I_\text{r.m.s.}\) in a resistor \(R\) dissipates a steady power \(I_\text{r.m.s.}^2R\).
The alternating current \(I_0\sin\omega t\) dissipates a mean power \(\tfrac12I_0^2R\) (from the previous section).
By the definition of the r.m.s. value, these are equal: \(I_\text{r.m.s.}^2R = \tfrac12I_0^2R\).
Cancel \(R\): \(I_\text{r.m.s.}^2 = \tfrac12I_0^2\).
Take the square root: \(I_\text{r.m.s.} = \dfrac{I_0}{\sqrt2}\).
The same steps with \(P = V^2/R\) give \(V_\text{r.m.s.} = V_0/\sqrt2\).
:::

:::formula R.m.s. values and mean power
\[I_\text{r.m.s.} = \frac{I_0}{\sqrt2} \qquad V_\text{r.m.s.} = \frac{V_0}{\sqrt2} \qquad \langle P\rangle = I_\text{r.m.s.}V_\text{r.m.s.} = I_\text{r.m.s.}^2R = \frac{V_\text{r.m.s.}^2}{R}\]
\(1/\sqrt2 = 0.707\). These apply to a **sinusoidal** alternating current or voltage only. With r.m.s. values, all the d.c. power formulae work for the **mean** power.
:::

Mains voltages are always quoted as r.m.s. values. A UK supply of 230 V has a peak value \(230 \times \sqrt2 = 325\,\mathrm{V}\) and a frequency of 50 Hz, which is the graph at the start of the chapter. A voltmeter reading on an a.c. range is also an r.m.s. value.

:::eg A lamp is rated 60 W when connected to 230 V r.m.s. mains. Find the r.m.s. current, the peak current, the peak power and the resistance of the lamp.
The rating is the mean power, with r.m.s. values: \(I_\text{r.m.s.} = \dfrac{P}{V_\text{r.m.s.}} = \dfrac{60}{230} = 0.261\,\mathrm{A}\). [C1] [A1]

Peak current: \(I_0 = \sqrt2 \times 0.2609 = 0.37\,\mathrm{A}\). [A1]

Peak power: twice the mean, \(2 \times 60 = 120\,\mathrm{W}\). [A1]

Resistance (assuming it is steady at its working temperature): \(R = \dfrac{V_\text{r.m.s.}^2}{P} = \dfrac{230^2}{60} = 8.8 \times 10^{2}\,\Omega\). [A1]

**Check:** peak power \(= I_0V_0 = 0.3689 \times 325 = 120\,\mathrm{W}\). It agrees.
:::

:::warn Three confusions about r.m.s. values
1. The r.m.s. value is **not** the mean: the mean of a sine wave over a whole cycle is zero.
2. \(V_0/\sqrt2\) holds only for a sine wave. A square wave or a rectified wave has a different r.m.s. value, which you must find from the definition: square, mean, root.
3. Mean power is half the peak power, **not** the peak divided by \(\sqrt2\). The \(\sqrt2\) belongs to voltages and currents, because power goes with their squares.
:::

:::lab Checking \(V_\text{r.m.s.} = V_0/\sqrt2\)
:::steps
1. Connect a signal generator set to a sine wave (about 50 Hz) across an oscilloscope, and an a.c. voltmeter in parallel with it.
2. Adjust the Y-gain so that the trace fills most of the screen. Read the peak-to-peak height in divisions and multiply by the Y-gain to get the peak-to-peak voltage; half of it is \(V_0\).
3. Read the a.c. voltmeter, which shows \(V_\text{r.m.s.}\). Record both values for at least six settings of the generator amplitude.
4. Plot \(V_\text{r.m.s.}\) (y-axis) against \(V_0\) (x-axis). The graph is a straight line through the origin with gradient \(1/\sqrt2 = 0.707\).
5. Reading the screen height to the nearest tenth of a division is the main source of uncertainty, so use a large trace, and measure from the lowest to the highest point rather than from the centre line.
:::
:::

:::eg A sinusoidal alternating supply has a peak value of 9.0 V. What steady d.c. voltage would heat the same resistor at the same mean rate?
The d.c. voltage with the same mean power is the r.m.s. value of the a.c. supply. [B1]

\[V_\text{r.m.s.} = \frac{V_0}{\sqrt2} = \frac{9.0}{\sqrt2} = 6.4\,\mathrm{V}\] [C1] [A1]

A 9.0 V battery would heat the resistor twice as fast as this a.c. supply, because power goes with the square of the voltage and \((9.0/6.36)^2 = 2.0\).
:::

## Rectification

Most electronic circuits need current in one direction only. **Rectification** converts a.c. into d.c. using **diodes**, which conduct in one direction and block current in the other (see the diode characteristic in [Electricity](#phys.electricity)).

:::def Rectification
The conversion of alternating current into direct (one-direction) current.
:::

### Half-wave rectification with one diode

Put one diode in series with the load. During the half-cycles when the diode is forward-biased (the supply makes the end connected to its anode positive), current flows through the load. During the other half-cycles the diode is reverse-biased, so no current flows. The load sees pulses of current in one direction, with gaps in between.

:::html
<figure class="fig small"><svg viewBox="40 0 240 145" role="img" aria-label="A circuit with an a.c. supply, a diode and a load resistor R in series. An arrow marked I shows the current flowing from the supply through the diode to the resistor."><path class="ln" d="M60 67V35H110M150 35H250V62M250 108V135H60V93"/><circle class="fp s-ink sw2" cx="60" cy="80" r="13"/><path class="ln thin" d="M51 80C54 72 57 72 60 80C63 88 66 88 69 80"/><path class="ln" d="M110 35L121 35M139 35L150 35"/><path class="fp s-ink sw2" d="M121 45L139 35L121 25Z"/><path class="ln" d="M139 45L139 25"/><rect class="fp s-ink sw2" x="242" y="62" width="16" height="46"/><text class="tl" x="266" y="90">R</text><text class="tl tc" x="130" y="18">diode</text><path class="c1" d="M185 22H215" marker-end="url(#ah-phys)"/><text class="tl ta tc" x="200" y="14">I</text></svg><figcaption>A half-wave rectifier. The diode lets current flow in the direction of its arrow only, so the load R receives current in one half of each cycle.</figcaption></figure>
:::

### Full-wave rectification with a bridge

A half-wave rectifier throws away half of the supply. A **bridge rectifier** uses four diodes to make use of both half-cycles. The supply is connected across two opposite corners (A and B in the figure) and the load across the other two (P and Q).

:::html
<figure class="fig"><svg viewBox="5 10 485 293" role="img" aria-label="A bridge rectifier. An a.c. supply at the bottom connects to terminals A on the left and B on the right of a diamond of four diodes D1 to D4. A load resistor R is between the top corner P and the bottom corner Q. One set of arrows shows the path when A is positive, through D1, down through R and through D4. A second set shows the path when B is positive, through D2, down through R and through D3. In both cases the current in R points downwards."><path class="ln" d="M200 150L241.8 120.7M258.2 109.3L300 80"/><path class="fp s-ink sw2" d="M248.1 129.7L258.2 109.3L235.5 111.7Z"/><path class="ln" d="M264.5 118.3L251.9 100.3"/><path class="ln" d="M400 150L358.2 120.7M341.8 109.3L300 80"/><path class="fp s-ink sw2" d="M364.5 111.7L341.8 109.3L351.9 129.7Z"/><path class="ln" d="M348.1 100.3L335.5 118.3"/><path class="ln" d="M300 220L258.2 190.7M241.8 179.3L200 150"/><path class="fp s-ink sw2" d="M264.5 181.7L241.8 179.3L251.9 199.7Z"/><path class="ln" d="M248.1 170.3L235.5 188.3"/><path class="ln" d="M300 220L341.8 190.7M358.2 179.3L400 150"/><path class="fp s-ink sw2" d="M348.1 199.7L358.2 179.3L335.5 181.7Z"/><path class="ln" d="M364.5 188.3L351.9 170.3"/><path class="ln" d="M300 80V128M300 172V220"/><rect class="fp s-ink sw2" x="292" y="128" width="16" height="44"/><text class="tl te" x="284" y="154">R</text><circle class="fi" cx="200" cy="150" r="4"/><circle class="fi" cx="300" cy="80" r="4"/><circle class="fi" cx="400" cy="150" r="4"/><circle class="fi" cx="300" cy="220" r="4"/><path class="ln" d="M200 150H140V275H287M313 275H460V150H400"/><circle class="fp s-ink sw2" cx="300" cy="275" r="13"/><path class="ln thin" d="M291 275C294 267 297 267 300 275C303 283 306 283 309 275"/><text class="tl te" x="132" y="212">A</text><text class="tl" x="468" y="212">B</text><path class="c1" d="M211.2 115.3L263.6 78.6" marker-end="url(#ah-phys)"/><path class="c2" d="M388.8 115.3L336.4 78.6" marker-end="url(#ah2-phys)"/><path class="c2" d="M263.6 221.4L211.2 184.7" marker-end="url(#ah2-phys)"/><path class="c1" d="M336.4 221.4L388.8 184.7" marker-end="url(#ah-phys)"/><text class="tl ti tc" x="222.5" y="79.7">D₁</text><text class="tl ti tc" x="377.5" y="79.7">D₂</text><text class="tl ti tc" x="222.5" y="228.3">D₃</text><text class="tl ti tc" x="377.5" y="228.3">D₄</text><path class="c3" d="M326 134V170" marker-end="url(#ahr)"/><text class="tl ti" x="334" y="156">I</text><path class="c1" d="M20 28H70" marker-end="url(#ah-phys)"/><text class="tl" x="78" y="32">A positive</text><path class="c2" d="M20 52H70" marker-end="url(#ah2-phys)"/><text class="tl" x="78" y="56">B positive</text><text class="tl tc" x="300" y="68">P</text><text class="tl tc" x="300" y="246">Q</text></svg><figcaption>A bridge rectifier. When terminal A is positive, current flows A, D₁, P, down through R, Q, D₄ and back to B. When B is positive it flows B, D₂, P, down through R, Q, D₃ and back to A. In both half-cycles the current in R points from P to Q.</figcaption></figure>
:::

Follow the current in each half-cycle.

- **A positive.** Current leaves A and can only pass through D₁ (anode at A) to corner P. It flows down through the load to Q, and returns to B through D₄. D₂ and D₃ are reverse-biased and block.
- **B positive.** Current leaves B, passes through D₂ to P, down through the load to Q, and returns to A through D₃. D₁ and D₄ are blocked.

In both cases the current goes through the load from P to Q. The load sees current in the **same direction** in every half-cycle: the negative half-cycles have been flipped over.

:::html
<figure class="fig"><svg viewBox="30 0 570 385" role="img" aria-label="Three graphs of voltage against time on the same time scale from 0 to 40 milliseconds. Top: the sinusoidal input, with peak V0 and minus V0. Middle: the half-wave rectified output, which has the positive half-cycles of the input and is zero for the negative ones. Bottom: the full-wave rectified output, in which every half-cycle is positive, so it has twice as many humps."><path class="ax" d="M70 3V143M70 75H518"/><text class="tl te" x="64" y="19">V₀</text><text class="tl te" x="64" y="79">0</text><text class="tl" x="526" y="19">input</text><text class="tl te" x="64" y="139">−V₀</text><path class="ax" d="M70 153V233M70 225H518"/><text class="tl te" x="64" y="169">V₀</text><text class="tl te" x="64" y="229">0</text><text class="tl" x="526" y="169">half-wave</text><path class="ax" d="M70 273V353M70 345H518"/><text class="tl te" x="64" y="289">V₀</text><text class="tl te" x="64" y="349">0</text><text class="tl" x="526" y="289">full-wave</text><path class="c1 sw2" d="M70 75L75.5 65.6L81 56.5L86.5 47.8L92 39.7L97.5 32.6L103 26.5L108.5 21.5L114 17.9L119.5 15.7L125 15L130.5 15.7L136 17.9L141.5 21.5L147 26.5L152.5 32.6L158 39.7L163.5 47.8L169 56.5L174.5 65.6L180 75L185.5 84.4L191 93.5L196.5 102.2L202 110.3L207.5 117.4L213 123.5L218.5 128.5L224 132.1L229.5 134.3L235 135L240.5 134.3L246 132.1L251.5 128.5L257 123.5L262.5 117.4L268 110.3L273.5 102.2L279 93.5L284.5 84.4L290 75L295.5 65.6L301 56.5L306.5 47.8L312 39.7L317.5 32.6L323 26.5L328.5 21.5L334 17.9L339.5 15.7L345 15L350.5 15.7L356 17.9L361.5 21.5L367 26.5L372.5 32.6L378 39.7L383.5 47.8L389 56.5L394.5 65.6L400 75L405.5 84.4L411 93.5L416.5 102.2L422 110.3L427.5 117.4L433 123.5L438.5 128.5L444 132.1L449.5 134.3L455 135L460.5 134.3L466 132.1L471.5 128.5L477 123.5L482.5 117.4L488 110.3L493.5 102.2L499 93.5L504.5 84.4L510 75"/><path class="c1 sw2" d="M70 225L75.5 215.6L81 206.5L86.5 197.8L92 189.7L97.5 182.6L103 176.5L108.5 171.5L114 167.9L119.5 165.7L125 165L130.5 165.7L136 167.9L141.5 171.5L147 176.5L152.5 182.6L158 189.7L163.5 197.8L169 206.5L174.5 215.6L180 225L185.5 225L191 225L196.5 225L202 225L207.5 225L213 225L218.5 225L224 225L229.5 225L235 225L240.5 225L246 225L251.5 225L257 225L262.5 225L268 225L273.5 225L279 225L284.5 225L290 225L295.5 215.6L301 206.5L306.5 197.8L312 189.7L317.5 182.6L323 176.5L328.5 171.5L334 167.9L339.5 165.7L345 165L350.5 165.7L356 167.9L361.5 171.5L367 176.5L372.5 182.6L378 189.7L383.5 197.8L389 206.5L394.5 215.6L400 225L405.5 225L411 225L416.5 225L422 225L427.5 225L433 225L438.5 225L444 225L449.5 225L455 225L460.5 225L466 225L471.5 225L477 225L482.5 225L488 225L493.5 225L499 225L504.5 225L510 225"/><path class="c1 sw2" d="M70 345L75.5 335.6L81 326.5L86.5 317.8L92 309.7L97.5 302.6L103 296.5L108.5 291.5L114 287.9L119.5 285.7L125 285L130.5 285.7L136 287.9L141.5 291.5L147 296.5L152.5 302.6L158 309.7L163.5 317.8L169 326.5L174.5 335.6L180 345L185.5 335.6L191 326.5L196.5 317.8L202 309.7L207.5 302.6L213 296.5L218.5 291.5L224 287.9L229.5 285.7L235 285L240.5 285.7L246 287.9L251.5 291.5L257 296.5L262.5 302.6L268 309.7L273.5 317.8L279 326.5L284.5 335.6L290 345L295.5 335.6L301 326.5L306.5 317.8L312 309.7L317.5 302.6L323 296.5L328.5 291.5L334 287.9L339.5 285.7L345 285L350.5 285.7L356 287.9L361.5 291.5L367 296.5L372.5 302.6L378 309.7L383.5 317.8L389 326.5L394.5 335.6L400 345L405.5 335.6L411 326.5L416.5 317.8L422 309.7L427.5 302.6L433 296.5L438.5 291.5L444 287.9L449.5 285.7L455 285L460.5 285.7L466 287.9L471.5 291.5L477 296.5L482.5 302.6L488 309.7L493.5 317.8L499 326.5L504.5 335.6L510 345"/><path class="ax" d="M70 360H518"/><path class="ax" d="M70 360V365"/><text class="ts tc" x="70" y="378">0</text><path class="ax" d="M180 360V365"/><text class="ts tc" x="180" y="378">10</text><path class="ax" d="M290 360V365"/><text class="ts tc" x="290" y="378">20</text><path class="ax" d="M400 360V365"/><text class="ts tc" x="400" y="378">30</text><path class="ax" d="M510 360V365"/><text class="ts tc" x="510" y="378">40</text><text class="tl" x="524" y="364">t / ms</text></svg><figcaption>The same 50 Hz supply before and after rectification. Half-wave: one pulse per cycle, 50 per second. Full-wave: every half-cycle is used, so there are twice as many pulses, 100 per second, and the output is never negative.</figcaption></figure>
:::

:::eg A bridge rectifier is connected to a 50 Hz supply whose peak value is 12.0 V. Each conducting diode has a forward p.d. of 0.70 V. How many pulses of current pass through the load each second, and what is the peak p.d. across the load?
Full-wave rectification gives one pulse for every half-cycle, so there are \(2 \times 50 = 100\) pulses per second. [B1]

At the peak, the current passes through **two** diodes in series (one on the way to the load, one on the way back), so the p.d. across the load is reduced by \(2 \times 0.70 = 1.40\,\mathrm{V}\): \(V_\text{peak} = 12.0 - 1.4 = 10.6\,\mathrm{V}\). [C1] [A1]

A real diode needs about 0.6 to 0.7 V forward p.d. before it conducts, so the ideal peak is always slightly too high. Unless a question gives the diode p.d., treat the diodes as ideal.
:::

:::exam Explaining a bridge rectifier
A 4-mark answer follows the current. Name the diodes that conduct when one terminal is positive and give the path through the load; then do the same for the other half-cycle; then state that the current in the load is in the same direction both times. Say that the other two diodes are **reverse-biased**, and use the words "same direction through the load". A sentence such as "it changes a.c. into d.c." scores nothing without the current paths.
:::

## Smoothing with a capacitor

The output of a rectifier is **unidirectional** but far from steady: it rises from zero to the peak and falls back to zero, 50 or 100 times a second. An amplifier or a radio would hum. To smooth it, connect a capacitor of capacitance \(C\) in **parallel** with the load \(R\).

:::html
<figure class="fig"><svg viewBox="25 8 590 210" role="img" aria-label="On the left, a circuit with a capacitor C and a load resistor R connected in parallel across the output terminals of a rectifier. On the right, a graph of voltage against time for three humps of a full-wave rectified supply drawn as a dashed line, with the smoothed output drawn as a solid line that rises to the peak V0 at each hump and then decays more slowly before the next peak. The ripple, the difference between the highest and lowest values of the smoothed output, is marked delta V."><path class="ln" d="M40 60H160V92M160 138V170H40"/><path class="ln" d="M90 60V104M90 126V170"/><path class="ln" d="M72 104H108M72 126H108"/><circle class="fi" cx="90" cy="60" r="3.5"/><circle class="fi" cx="90" cy="170" r="3.5"/><circle class="fp s-ink sw2" cx="40" cy="60" r="4"/><circle class="fp s-ink sw2" cx="40" cy="170" r="4"/><rect class="fp s-ink sw2" x="152" y="92" width="16" height="46"/><text class="tl ti" x="116" y="120">C</text><text class="tl ti" x="176" y="120">R</text><text class="tl tc" x="100" y="204">rectifier output</text><path class="ax" d="M262 30V190M262 190H557"/><path class="ln-m thin dash" d="M262 190L266.8 166.5L271.5 143.6L276.3 121.9L281 101.8L285.8 83.9L290.5 68.6L295.3 56.3L300 47.3L304.8 41.8L309.5 40L314.3 41.8L319 47.3L323.8 56.3L328.5 68.6L333.3 83.9L338 101.8L342.8 121.9L347.5 143.6L352.3 166.5L357 190L361.8 166.5L366.5 143.6L371.3 121.9L376 101.8L380.8 83.9L385.5 68.6L390.3 56.3L395 47.3L399.8 41.8L404.5 40L409.3 41.8L414 47.3L418.8 56.3L423.5 68.6L428.3 83.9L433 101.8L437.8 121.9L442.5 143.6L447.3 166.5L452 190L456.8 166.5L461.5 143.6L466.3 121.9L471 101.8L475.8 83.9L480.5 68.6L485.3 56.3L490 47.3L494.8 41.8L499.5 40L504.3 41.8L509 47.3L513.8 56.3L518.5 68.6L523.3 83.9L528 101.8L532.8 121.9L537.5 143.6L542.3 166.5"/><path class="c1 sw2" d="M262 71.7L266.8 74.6L271.5 77.5L276.3 80.2L281 83L285.8 83.9L290.5 68.6L295.3 56.3L300 47.3L304.8 41.8L309.5 40L314.3 41.8L319 45.5L323.8 49.1L328.5 52.6L333.3 55.9L338 59.3L342.8 62.5L347.5 65.6L352.3 68.7L357 71.7L361.8 74.6L366.5 77.5L371.3 80.2L376 83L380.8 83.9L385.5 68.6L390.3 56.3L395 47.3L399.8 41.8L404.5 40L409.3 41.8L414 45.5L418.8 49.1L423.5 52.6L428.3 55.9L433 59.3L437.8 62.5L442.5 65.6L447.3 68.7L452 71.7L456.8 74.6L461.5 77.5L466.3 80.2L471 83L475.8 83.9L480.5 68.6L485.3 56.3L490 47.3L494.8 41.8L499.5 40L504.3 41.8L509 45.5L513.8 49.1L518.5 52.6L523.3 55.9L528 59.3L532.8 62.5L537.5 65.6L542.3 68.7"/><text class="tl te" x="256" y="44">V₀</text><text class="tl ti" x="270" y="26">V / V</text><path class="ln-m thin dash" d="M357 85.3H585M357 40H585"/><path class="c3" d="M577 62.6V41" marker-end="url(#ahr)"/><path class="c3" d="M577 62.6V84.3" marker-end="url(#ahr)"/><text class="tl ti" x="587" y="66.6">ΔV</text><path class="ax" d="M262 190V195"/><text class="ts tc" x="262" y="208">0</text><path class="ax" d="M357 190V195"/><text class="ts tc" x="357" y="208">10</text><path class="ax" d="M452 190V195"/><text class="ts tc" x="452" y="208">20</text><path class="ax" d="M547 190V195"/><text class="ts tc" x="547" y="208">30</text><text class="tl" x="563" y="194">t / ms</text></svg><figcaption>A capacitor in parallel with the load smooths a full-wave rectified supply. The dashed line is the rectified supply and the solid line is the p.d. across the load. It follows the supply up to each peak, then decays as the capacitor discharges through R, until the next peak tops it up. ΔV is the ripple. Here RC is only twice the time between peaks, so the ripple is large; a real design has a much smaller ripple.</figcaption></figure>
:::

The capacitor works in three stages.

1. While the rectified p.d. is rising, the capacitor charges through the conducting diode(s) and its p.d. follows the supply up to the **peak**, \(V_0\).
2. Just after the peak, the supply p.d. falls below the capacitor p.d. The diode(s) become **reverse-biased**, so the capacitor cannot discharge back into the supply. Its only way out is through the load, and the p.d. decays exponentially, \(V = V_0e^{-t/RC}\), with time constant \(RC\).
3. Before it has fallen far, the next peak arrives. The supply p.d. rises above the capacitor p.d. again, the diode(s) conduct, and the capacitor is topped up to \(V_0\).

The output therefore never falls to zero. It has a small remaining variation called **ripple**, a sawtooth of height \(\Delta V\) (the difference between the highest and lowest p.d.) at the frequency of the rectified pulses.

:::proof How big is the ripple?
Between peaks the capacitor discharges through the load for a time \(t\): \(t = T\) for half-wave rectification and \(t = T/2\) for full-wave.
From the exponential decay, the p.d. falls from \(V_0\) to \(V_0e^{-t/RC}\), so \(\Delta V = V_0\left(1 - e^{-t/RC}\right)\).
When the time constant is much longer than \(t\), the exponential is close to \(1 - t/RC\) (the first two terms of its series), so \(\Delta V \approx V_0\,\dfrac{t}{RC}\).
A second way to see it: the p.d. across the load is almost constant at \(V_0\), so the current in the load is almost constant at \(V_0/R\). In time \(t\) the capacitor loses charge \(\Delta Q = It = V_0t/R\), and \(\Delta V = \Delta Q/C = V_0t/RC\).
The same result comes from both routes.
:::

:::formula Ripple on a smoothed supply
\[\Delta V \approx \frac{V_0\,t}{RC} = \frac{It}{C} \qquad (t \ll RC)\]
\(\Delta V\): ripple (V) · \(V_0\): peak p.d. (V) · \(R\): load resistance (Ω) · \(C\): capacitance (F) · \(I\): load current (A) · \(t\): time between peaks, \(T\) for half-wave and \(T/2\) for full-wave (s). The ripple gets smaller as \(RC\) gets larger.
:::

Three things follow from the equation, and you should be able to explain each one in terms of charge.

- **Larger \(C\)** gives less ripple: the capacitor holds more charge for the same p.d., so the same load current removes a smaller fraction of it.
- **Larger \(R\)** gives less ripple: the load draws less current, so the capacitor loses charge more slowly. A **smaller** load resistance, which draws a larger current, gives **more** ripple.
- **Full-wave** rectification gives half the ripple of half-wave for the same \(R\) and \(C\): the peaks are twice as frequent, so \(t\) is halved, and the capacitor has half as long to discharge.

:::eg A full-wave rectifier gives a peak output of 12 V from a 50 Hz supply. A \(470\,\mu\mathrm{F}\) capacitor is connected across a \(2.0\,\mathrm{k\Omega}\) load. Estimate the ripple, as a percentage of the peak. How does it change if the rectifier is half-wave?
Time constant: \(RC = 2.0 \times 10^{3} \times 470 \times 10^{-6} = 0.94\,\mathrm{s}\). The time between peaks is \(T/2 = 0.010\,\mathrm{s}\), much shorter than \(RC\), so the approximation holds. [C1]

\[\Delta V \approx \frac{V_0\,t}{RC} = \frac{12 \times 0.010}{0.94} = 0.13\,\mathrm{V}\] [A1]

As a percentage of the peak: \(0.13/12 = 1.1\%\). The output is steady to about one per cent. [A1]

With half-wave rectification \(t = T = 0.020\,\mathrm{s}\), so the ripple doubles to \(0.26\,\mathrm{V}\), which is 2.1% of the peak. [A1]
:::

:::eg A half-wave rectified supply of 50 Hz powers a radio that draws a steady 0.040 A. The ripple must not exceed 0.30 V. What is the smallest smoothing capacitance? What would be needed for a full-wave rectifier?
For half-wave, \(t = T = 0.020\,\mathrm{s}\). The charge lost between peaks is \(\Delta Q = It = 0.040 \times 0.020 = 8.0 \times 10^{-4}\,\mathrm{C}\). [C1]

\[C = \frac{\Delta Q}{\Delta V} = \frac{8.0 \times 10^{-4}}{0.30} = 2.7 \times 10^{-3}\,\mathrm{F} = 2700\,\mu\mathrm{F}\] [A1]

With full-wave rectification \(t = 0.010\,\mathrm{s}\), so \(\Delta Q\) is halved and only \(1300\,\mu\mathrm{F}\) is needed. [A1]

This is why most power supplies use full-wave rectification: for the same smoothing, the capacitor can be half the size.
:::

:::warn Which way does the load resistance act?
Many students think that a **larger** resistor makes the output "worse". The opposite is true for smoothing. A larger \(R\) draws less current, so the capacitor discharges more slowly, and \(RC\) is larger. A small \(R\) (a heavy load) lets the capacitor drain quickly, and the ripple grows. If a power supply starts to hum when you plug in a bigger load, this is why.
:::

Now try it. Switch between the three tabs to see the unrectified supply, half-wave and full-wave output. Then set the capacitance to zero and increase it step by step, and watch the ripple \(\Delta V\) fall; change the load resistance and the supply frequency and see how the ripple responds.

:::html
<div class="widget" data-w="phys-ac" data-v0="10" data-f="50" data-mode="full" data-c="100" data-r="1"></div>
:::

:::lab Investigating the ripple on a smoothed supply
:::steps
1. Connect a low-voltage a.c. supply to a bridge rectifier, with a load resistor across the output. Connect an oscilloscope across the load.
2. With no capacitor, check that the trace shows the full-wave rectified humps, and measure the peak \(V_0\) using the Y-gain.
3. Connect a capacitor across the load. Switch the oscilloscope input to a.c. coupling, which removes the steady level, and increase the Y-gain until the ripple fills the screen. Measure the peak-to-peak height of the ripple, \(\Delta V\).
4. Repeat with at least five different capacitors, keeping \(R\) constant.
5. Plot \(\Delta V\) (y-axis) against \(1/C\) (x-axis). The graph is a straight line through the origin, because \(\Delta V = (V_0t/R)(1/C)\). The gradient is \(V_0t/R\), which allows \(t\) (and so the frequency of the pulses) or \(R\) to be checked.
6. Repeat with a half-wave rectifier: the gradient doubles.
:::
:::

:::board
Rectification with diodes and smoothing with a capacitor are listed in the Cambridge 9702 syllabus (topic 21.2). Check your own specification for whether you need them. The definitions of peak value, r.m.s. value, period and frequency are the same physics wherever you study.
:::

:::eg Spot the error: a resistor has a peak power of 80 W when connected to a sinusoidal supply. Calculate the mean power.
A student wrote this answer.

Line 1: mean power \(= \dfrac{P_0}{\sqrt2}\)
Line 2: \(= \dfrac{80}{\sqrt2} = 57\,\mathrm{W}\)

**Line 1 is wrong: the factor \(\sqrt2\) belongs to voltage and current, not power.** Power depends on the **square** of the current, so the \(\sqrt2\) squares to 2. Mean power is half the peak power. The formula mark and the answer mark are lost. [C0] [A0]

Correct working: \(\langle P\rangle = \tfrac12P_0 = \tfrac12 \times 80\) [C1] \(= 40\,\mathrm{W}\). [A1]

Check: the r.m.s. current is \(1/\sqrt2\) of the peak, so the mean power is \((1/\sqrt2)^2 = 1/2\) of the peak. A mean power of 57 W would need the current to be larger than \(1/\sqrt2\) of its peak.
:::

:::try Start easy, finish at exam standard
Q: An alternating voltage has a period of 25 ms. Find its frequency.
A: \(f = 1/T = 1/0.025 = 40\,\mathrm{Hz}\).
Q: A voltage is \(V = 12\sin(200\pi t)\). State the peak value, and find the frequency and the period.
A: Peak value 12 V. \(\omega = 200\pi\), so \(f = \omega/2\pi = 100\,\mathrm{Hz}\) and \(T = 1/f = 0.010\,\mathrm{s}\).
Q: An alternating supply has a peak voltage of 170 V. Find the r.m.s. voltage.
A: \(V_\text{r.m.s.} = 170/\sqrt2 = 120\,\mathrm{V}\).
Q: A peak current of 3.0 A flows through a \(10\,\Omega\) resistor. Find the mean power.
A: \(\langle P\rangle = \tfrac12I_0^2R = \tfrac12 \times 3.0^2 \times 10 = 45\,\mathrm{W}\).
Q: A heater is rated 2.0 kW on a 230 V r.m.s. supply. Find the r.m.s. current and the resistance.
A: \(I_\text{r.m.s.} = P/V_\text{r.m.s.} = 2000/230 = 8.7\,\mathrm{A}\) and \(R = V_\text{r.m.s.}^2/P = 230^2/2000 = 26\,\Omega\).
Q: Why is the mean value of an alternating current not used to describe the heating effect?
A: Over a whole cycle the mean value of a sinusoidal current is zero, because the positive and negative halves cancel, but the heating effect is not zero. The r.m.s. value is defined from the mean power, so it works.
Q: A bridge rectifier is supplied with a.c. of frequency 50 Hz. State the frequency of the pulses in the output, and the number of diodes that conduct at any instant.
A: The output pulses have frequency 100 Hz (one pulse per half-cycle), and two diodes conduct at any instant.
Q: A \(1000\,\mu\mathrm{F}\) capacitor is connected across a \(500\,\Omega\) load on a full-wave rectified 50 Hz supply with peak 10 V. Estimate the ripple.
A: \(RC = 500 \times 1000 \times 10^{-6} = 0.50\,\mathrm{s}\) and \(t = 0.010\,\mathrm{s}\), so \(\Delta V \approx V_0t/RC = 10 \times 0.010/0.50 = 0.20\,\mathrm{V}\).
Q: The a.c. input to a bridge rectifier has a peak value of 15.0 V. Find the peak output if each conducting diode has a forward p.d. of 0.70 V.
A: Two diodes conduct in series, so the loss is \(2 \times 0.70 = 1.4\,\mathrm{V}\) and the peak output is \(15.0 - 1.4 = 13.6\,\mathrm{V}\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the root-mean-square value of an alternating current.
A: The value of the steady direct current [B1] that would dissipate energy at the same (average) rate in a resistor as the alternating current. [B1]
Q: [4 marks] ★★ The trace on an oscilloscope screen of an alternating voltage is 5.6 cm high from its lowest to its highest point. One complete cycle is 5.0 cm wide. The Y-gain is \(5.0\,\mathrm{V\,cm^{-1}}\) and the time-base is \(2.0\,\mathrm{ms\,cm^{-1}}\). Calculate (a) the peak voltage, (b) the frequency, (c) the r.m.s. voltage.
A: (a) The peak-to-peak voltage is \(5.6 \times 5.0 = 28\,\mathrm{V}\) [C1] so the peak voltage is 14 V. [A1] (b) \(T = 5.0 \times 2.0 = 10\,\mathrm{ms}\), so \(f = 1/0.010 = 100\,\mathrm{Hz}\). [A1] (c) \(V_\text{r.m.s.} = 14/\sqrt2 = 9.9\,\mathrm{V}\). [A1]
Q: [3 marks] ★★ A sinusoidal alternating current of peak value 2.0 A is passed through a \(15\,\Omega\) resistor. Calculate (a) the peak power and (b) the mean power in the resistor.
A: (a) \(P_0 = I_0^2R = 2.0^2 \times 15 = 60\,\mathrm{W}\). [A1] (b) The mean power is half the peak power, \(\langle P\rangle = \tfrac12 \times 60\) [C1] \(= 30\,\mathrm{W}\). [A1]
Q: [2 marks] ★ A sinusoidal voltage of peak value \(V_0\) and period \(T\) is connected to a resistor through (a) a single diode and (b) a bridge of four diodes. Sketch, or describe, the graph of the p.d. across the resistor in each case.
A: (a) Positive half-cycles only, with zero between them, each lasting half a period \(T\), so the pulses repeat with period \(T\). [B1] (b) Every half-cycle is positive, so the p.d. is a series of humps of peak value \(V_0\) that repeat with period \(T/2\) (twice the frequency). [B1]
Q: [4 marks] ★★ A bridge rectifier has four diodes, D₁ to D₄. The a.c. supply is connected across two opposite corners and the load across the other two. Explain how current flows in the same direction through the load in both half-cycles of the supply.
A: In one half-cycle two diodes are forward-biased, and current passes through one of them, then through the load, then back through the second one to the supply. [B1] The other two diodes are reverse-biased and block. [B1] In the next half-cycle the supply polarity is reversed, and the other pair of diodes is forward-biased. [B1] Current passes through the load in the same direction as before, because the pair of diodes is arranged so that the same end of the load is connected to the positive supply terminal in both half-cycles. [B1]
Q: [4 marks] ★★ A full-wave rectified supply is smoothed by a capacitor \(C\) connected in parallel with a load \(R\). State and explain the effect on the ripple of (a) doubling the capacitance and (b) halving the resistance of the load.
A: (a) The ripple is halved. [B1] The time constant \(RC\) is doubled, so the capacitor discharges more slowly and its p.d. falls by less between peaks. [B1] (b) The ripple is doubled. [B1] The time constant is halved (the load takes twice the current), so the capacitor discharges faster. [B1]
Q: [5 marks] ★★★ A full-wave rectified 50 Hz supply has a peak output of 9.0 V and is smoothed with a capacitor connected across a \(150\,\Omega\) load. The ripple must be no more than 0.50 V. (a) State the time between successive peaks. (b) Calculate the smallest capacitance. (c) State whether a \(1000\,\mu\mathrm{F}\) capacitor would be suitable, giving a reason.
H: The load current is nearly constant at \(V_0/R\) for the time between peaks.
H: Use \(\Delta V = \Delta Q/C\) with \(\Delta Q = It\).
A: (a) The time between peaks is \(T/2 = 0.010\,\mathrm{s}\), because full-wave rectification gives 100 peaks per second. [B1] (b) \(I = V_0/R = 9.0/150 = 0.060\,\mathrm{A}\), so \(\Delta Q = It = 0.060 \times 0.010 = 6.0 \times 10^{-4}\,\mathrm{C}\). [C1] \(C = \dfrac{\Delta Q}{\Delta V} = \dfrac{6.0 \times 10^{-4}}{0.50}\) [C1] \(= 1.2 \times 10^{-3}\,\mathrm{F} = 1200\,\mu\mathrm{F}\). [A1] (c) No: \(1000\,\mu\mathrm{F}\) is smaller than the minimum, and would give a ripple of \(6.0 \times 10^{-4}/1.0 \times 10^{-3} = 0.60\,\mathrm{V}\), which is above the limit. [B1]
Q: [6 marks] ★★★ A heater of resistance \(8.0\,\Omega\) is connected to a 12 V d.c. supply. It is then connected to a sinusoidal 50 Hz a.c. supply and gives the same mean heating. (a) Calculate the power in the heater on the d.c. supply. (b) Calculate the peak voltage of the a.c. supply. (c) Calculate the peak power in the heater on the a.c. supply.
H: Same mean power in the same resistor means the a.c. supply has an r.m.s. value equal to the d.c. voltage.
H: The peak power is twice the mean power.
A: (a) \(P = V^2/R = 12^2/8.0\) [C1] \(= 18\,\mathrm{W}\). [A1] (b) The mean power is the same, so \(V_\text{r.m.s.} = 12\,\mathrm{V}\). [B1] \(V_0 = \sqrt2 \times 12\) [C1] \(= 17\,\mathrm{V}\). [A1] (c) The peak power is twice the mean power, \(2 \times 18 = 36\,\mathrm{W}\). [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A sinusoidal voltage of peak value \(V_0\) is half-wave rectified, so that the p.d. across a resistor is the positive half-cycles of the sine wave and zero for the rest of the time. (a) Show that the r.m.s. value of the rectified p.d. is \(V_0/2\). (b) The 230 V r.m.s. mains, of peak value 325 V, is half-wave rectified and applied to a \(100\,\Omega\) resistor. Calculate the mean power dissipated.
H: The mean of \(V^2\) is the mean over a whole cycle: half the time it follows \(V_0^2\sin^2\omega t\), and for the other half it is zero.
A: (a) For half of the cycle, the mean of \(V^2\) is \(\tfrac12V_0^2\); for the other half it is zero. So the mean over the whole cycle is \(\tfrac12 \times \tfrac12V_0^2\) [M1] \(= \tfrac14V_0^2\). [A1] The r.m.s. value is the square root of this mean square, \(V_0/2\). [A1] (b) \(V_\text{r.m.s.} = 325/2 = 162.5\,\mathrm{V}\), so \(\langle P\rangle = \dfrac{V_\text{r.m.s.}^2}{R} = \dfrac{162.5^2}{100}\) [C1] \(= 264\,\mathrm{W}\). [A1] This is exactly half of the \(230^2/100 = 529\,\mathrm{W}\) that the unrectified supply would dissipate, because the half-wave rectifier passes only half of the energy.
Q: [5 marks] ★★★ (a) Use the identity \(\sin^2\theta = \tfrac12(1 - \cos2\theta)\) to show that the mean value of \(\sin^2\omega t\) over a whole number of cycles is \(\tfrac12\). (b) A sinusoidal alternating p.d. of peak value 20 V and frequency 50 Hz is applied to a \(40\,\Omega\) resistor. Show that the mean power is 5.0 W.
H: What is the mean value of \(\cos2\omega t\) over a whole number of cycles of the sine wave?
A: (a) \(\sin^2\omega t = \tfrac12\left(1 - \cos2\omega t\right)\), so the mean is \(\tfrac12(1 - \text{mean of }\cos2\omega t)\). [M1] Over a whole number of cycles the cosine is positive as often as negative, and with the same size, so its mean is zero. [M1] The mean of \(\sin^2\omega t\) is therefore \(\tfrac12\). [A1] (b) \(P = V^2/R = V_0^2\sin^2\omega t/R\), so \(\langle P\rangle = \dfrac{V_0^2}{2R} = \dfrac{20^2}{2 \times 40}\) [C1] \(= 5.0\,\mathrm{W}\). [A1]
:::

:::quiz
? The r.m.s. voltage of the UK mains is 230 V. What is its peak value, to 3 significant figures?
+ 325 V
- 163 V
- 460 V
- 230 V
> The peak is \(\sqrt2 \times 230 = 325\,\mathrm{V}\). 163 V divides by \(\sqrt2\) instead of multiplying, and 460 V doubles the r.m.s. value; the peak-to-peak value is 650 V.
? A sinusoidal alternating current flows in a resistor. How does the mean power compare with the peak power?
+ It is half the peak power.
- It is \(1/\sqrt2\) of the peak power.
- It is equal to the peak power.
- It is zero, because the mean current is zero.
> Power goes with the square of the current, so the mean power is half of the peak. The \(1/\sqrt2\) belongs to the current and the voltage. The mean current is zero, but the mean power is not, because \(I^2\) is never negative.
? What is the mean value of a sinusoidal alternating current over one complete cycle?
+ Zero
- \(I_0/\sqrt2\)
- \(I_0/2\)
- \(I_0\)
> The positive and negative half-cycles are equal and opposite, so they cancel. \(I_0/\sqrt2\) is the r.m.s. value, which is defined in terms of power and not the mean current.
? A half-wave rectifier is connected to a 50 Hz supply. How many pulses of current pass through the load each second?
+ 50
- 100
- 25
- 0
> One pulse for each positive half-cycle, so 50 per second. A full-wave bridge would give 100.
? In a bridge rectifier, how many of the four diodes conduct at any instant?
+ Two
- One
- Three
- Four
> Current goes through one diode to the load and through a second back to the supply. The other two are reverse-biased.
? A smoothing capacitor is connected across the load of a rectifier. Which change reduces the ripple?
+ Increasing the capacitance
- Decreasing the load resistance
- Using half-wave rectification instead of full-wave
- Reducing the capacitance
> A larger capacitance gives a larger time constant \(RC\), so the p.d. falls less between peaks. A smaller load resistance and half-wave rectification both make the ripple larger.
? A capacitor smooths the output of a rectifier. The load resistance is reduced to half. What happens to the ripple?
+ It roughly doubles.
- It is roughly halved.
- It does not change.
- It falls to zero.
> A smaller \(R\) halves \(RC\) and draws twice the current, so the capacitor loses charge twice as fast. The ripple \(\Delta V \approx V_0t/RC\) doubles.
? Which definition of r.m.s. current is correct?
+ The steady current that would dissipate the same mean power in a resistor
- The mean value of the current over one cycle
- The peak current divided by two
- The current at the point where the power is a maximum
> The r.m.s. value is defined by its heating effect. The mean current is zero for a sine wave, and the factor is \(\sqrt2\), not 2.
:::

:::checklist What you can now do
- [ ] I can define and use period, frequency and peak value, and use \(x = x_0\sin\omega t\) for an alternating current or voltage.
- [ ] I can show and use that the mean power in a resistive load is half the maximum power for a sinusoidal current.
- [ ] I can define the r.m.s. value, and use \(I_\text{r.m.s.} = I_0/\sqrt2\) and \(V_\text{r.m.s.} = V_0/\sqrt2\), including with oscilloscope traces.
- [ ] I can distinguish half-wave and full-wave rectification graphically.
- [ ] I can explain half-wave rectification with a single diode.
- [ ] I can explain full-wave rectification with four diodes (a bridge), following the current in each half-cycle.
- [ ] I can analyse smoothing with a capacitor, including the effect of the capacitance and of the load resistance on the ripple.
:::

:::recap
- Period \(T\) (s), frequency \(f = 1/T\) (Hz), peak value \(V_0\) or \(I_0\); \(V = V_0\sin\omega t\) with \(\omega = 2\pi f\). Peak-to-peak is twice the peak.
- Power in a resistor \(P = I_0^2R\sin^2\omega t\). The mean of \(\sin^2\) over a cycle is \(\tfrac12\), so the mean power is **half** the peak power.
- R.m.s. value: the steady d.c. that gives the same mean power in a resistor. For a sinusoid \(I_\text{r.m.s.} = I_0/\sqrt2\) and \(V_\text{r.m.s.} = V_0/\sqrt2\). Mean power \(= I_\text{r.m.s.}V_\text{r.m.s.}\). Mains voltages are r.m.s. (UK: 230 V, peak 325 V, 50 Hz).
- Rectification converts a.c. into d.c. One diode gives half-wave (one pulse per cycle); a bridge of four diodes gives full-wave (two pulses per cycle, current in the load always in the same direction, two diodes conducting at a time).
- A capacitor in parallel with the load charges to the peak and discharges through the load between peaks, with time constant \(RC\). Ripple \(\Delta V \approx V_0t/RC\): less for larger \(C\), larger \(R\), and full-wave rectification (\(t = T/2\)).
:::

:::links
- explore: [Circuit Construction Kit: AC](https://phet.colorado.edu/en/simulations/circuit-construction-kit-ac) · PhET · build circuits with an a.c. source and see the voltage and current change with time
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the a.c. and rectification questions in real papers [unofficial]
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Quantum physics](#phys.quantum)
