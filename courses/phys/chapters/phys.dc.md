@chapter phys.dc
@title D.C. circuits
@level as
@paper CAIE P1 · P2 · P3 (AS)
@time 6–8 hours
@summary How real circuits behave: e.m.f. and internal resistance, Kirchhoff's two laws and the series and parallel formulae they give, potential dividers with sensors, and the potentiometer that measures an e.m.f. without drawing any current.

:::why
Every electrical device you own is a circuit of sources, resistors and sensors, and this chapter gives you the tools to predict exactly what each part of it does. Kirchhoff's laws are simply conservation of charge and conservation of energy written for circuits, so the same two ideas solve every circuit on Papers 1 and 2. Potential dividers are how thermostats, light-activated switches and most sensors turn a change in the world into a voltage a computer can read.
:::

**Before you start**, you need current, potential difference, resistance and power from [Electricity](#phys.electricity), and unit prefixes from [Physical quantities, units and uncertainty](#phys.units).

:::try Warm-up
Q: A steady current of 0.25 A flows for 2.0 minutes. How much charge passes? (from [Electricity](#phys.electricity))
A: \(Q = It = 0.25 \times 120 = 30\,\mathrm{C}\). Remember to change minutes into seconds first.
Q: A 12 V supply drives a current of 0.40 A through a resistor. Find its resistance and the power it dissipates. (from [Electricity](#phys.electricity))
A: \(R = V/I = 12/0.40 = 30\,\Omega\) and \(P = VI = 12 \times 0.40 = 4.8\,\mathrm{W}\).
Q: Write \(4.7\,\mathrm{k\Omega}\) and \(220\,\mathrm{mA}\) in base units, in standard form. (from [Physical quantities, units and uncertainty](#phys.units))
A: \(4.7 \times 10^{3}\,\Omega\) and \(2.20 \times 10^{-1}\,\mathrm{A}\) (that is, 0.220 A).
:::

## Circuit symbols and circuit diagrams

A circuit diagram is a map of where charge can flow. Examiners give you circuits as diagrams and expect you to draw them too, so you need to recognise every symbol in the Cambridge list instantly. Straight lines are connecting wires with negligible resistance, and a dot marks a **junction**, where wires join.

:::html
<figure class="fig"><svg viewBox="0 0 600 340" role="img" aria-label="Sixteen circuit symbols in a grid: cell, battery, switch, fixed resistor, variable resistor, potentiometer, thermistor, light-dependent resistor, lamp, diode, light-emitting diode, heater, ammeter, voltmeter, galvanometer and capacitor"><path class="ln" d="M30 40H70M80 40H120"/><path class="ln" d="M70 24V56"/><path class="ln thick" d="M80 32V48"/><text class="ts tc" x="62" y="22">+</text><text class="tl tc" x="75" y="76">cell</text><path class="ln" d="M180 40H210M218 40H232M240 40H270"/><path class="ln" d="M210 24V56M232 24V56"/><path class="ln thick" d="M218 32V48M240 32V48"/><text class="tl tc" x="225" y="76">battery of cells</text><path class="ln" d="M330 40H357M393 40H420"/><path class="ln" d="M357 40L389 26"/><circle class="fi" cx="357" cy="40" r="3"/><circle class="fi" cx="393" cy="40" r="3"/><text class="tl tc" x="375" y="76">switch (open)</text><path class="ln" d="M480 40H570"/><rect class="fp s-ink sw2" x="503" y="32" width="44" height="16"/><text class="tl tc" x="525" y="76">fixed resistor</text><path class="ln" d="M30 124H120"/><rect class="fp s-ink sw2" x="53" y="116" width="44" height="16"/><path class="ln" d="M53 142L95 108" marker-end="url(#ah)"/><text class="tl tc" x="75" y="160">variable resistor</text><path class="ln" d="M180 124H270"/><rect class="fp s-ink sw2" x="203" y="116" width="44" height="16"/><path class="ln" d="M225 94V112" marker-end="url(#ah)"/><text class="tl tc" x="225" y="160">potentiometer</text><path class="ln" d="M330 124H420"/><rect class="fp s-ink sw2" x="353" y="116" width="44" height="16"/><path class="ln" d="M345 142H353L397 106"/><text class="tl tc" x="375" y="160">thermistor</text><path class="ln" d="M480 124H570"/><rect class="fp s-ink sw2" x="503" y="116" width="44" height="16"/><path class="ln thin" d="M494 92L508 110M512 92L526 110" marker-end="url(#ah)"/><path class="ln thin" d="M494 92L508 110" marker-end="url(#ah)"/><text class="tl tc" x="525" y="160">light-dependent resistor</text><path class="ln" d="M30 208H120"/><circle class="fp s-ink sw2" cx="75" cy="208" r="13"/><path class="ln" d="M65.8 198.8L84.2 217.2M84.2 198.8L65.8 217.2"/><text class="tl tc" x="75" y="244">filament lamp</text><path class="ln" d="M180 208H270"/><path class="fp s-ink sw2" d="M215 197L235 208L215 219Z"/><path class="ln" d="M235 197V219"/><text class="tl tc" x="225" y="244">diode</text><path class="ln" d="M330 208H420"/><path class="fp s-ink sw2" d="M365 197L385 208L365 219Z"/><path class="ln" d="M385 197V219"/><path class="ln thin" d="M377 192L389 178M387 196L399 182" marker-end="url(#ah)"/><path class="ln thin" d="M377 192L389 178" marker-end="url(#ah)"/><text class="tl tc" x="375" y="244">light-emitting diode</text><path class="ln" d="M480 208H570"/><rect class="fp s-ink sw2" x="503" y="200" width="44" height="16"/><path class="ln thin" d="M514 200V216M525 200V216M536 200V216"/><text class="tl tc" x="525" y="244">heater</text><path class="ln" d="M30 292H120"/><circle class="fp s-ink sw2" cx="75" cy="292" r="13"/><text class="tb tc" x="75" y="297">A</text><text class="tl tc" x="75" y="328">ammeter</text><path class="ln" d="M180 292H270"/><circle class="fp s-ink sw2" cx="225" cy="292" r="13"/><text class="tb tc" x="225" y="297">V</text><text class="tl tc" x="225" y="328">voltmeter</text><path class="ln" d="M330 292H420"/><circle class="fp s-ink sw2" cx="375" cy="292" r="13"/><path class="ln thin" d="M369 301L380 282" marker-end="url(#ah)"/><text class="tl tc" x="375" y="328">galvanometer</text><path class="ln" d="M480 292H520M530 292H570"/><path class="ln" d="M520 276V308M530 276V308"/><text class="tl tc" x="525" y="328">capacitor</text></svg><figcaption>The circuit symbols you will use most in this chapter. In a cell the long thin plate is the positive terminal. The full list of symbols that can appear in Cambridge papers is in the syllabus.</figcaption></figure>
:::

Two meters measure what is happening in a circuit, and each must disturb it as little as possible.

- An **ammeter** measures current, so the current must pass through it: it goes **in series**. An ideal ammeter has **zero resistance**, so it takes no p.d. away from the rest of the circuit.
- A **voltmeter** measures the p.d. between two points, so it is connected **in parallel**, across the component. An ideal voltmeter has **infinite resistance**, so no current is diverted through it.

:::warn Meters in the wrong place
A voltmeter placed in series stops almost all the current, because its resistance is huge. An ammeter placed in parallel short-circuits the component and can draw a very large current. If a circuit you have drawn gives a strange answer, check where the meters are first.
:::

## E.m.f. and potential difference

Both e.m.f. and p.d. are measured in volts, and \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\). The difference between them is the **direction of the energy transfer**. In a source such as a battery, chemical energy (or some other form) is converted into electrical energy of the charges. In a resistor, a lamp or a motor, electrical energy is converted into other forms such as thermal energy and light.

:::def Electromotive force (e.m.f.)
The energy transferred (converted from other forms into electrical energy) per unit charge by a source in driving charge around a complete circuit.
:::

:::def Potential difference (p.d.)
The energy transferred (converted from electrical energy into other forms) per unit charge as charge passes between two points in a circuit.
:::

:::cols
:::col e.m.f., symbol \(E\)
Belongs to a **source**: cell, battery, generator, solar cell.

Other forms → electrical energy.

\(E = W/Q\), where \(W\) is the energy the source gives to charge \(Q\).
:::
:::col p.d., symbol \(V\)
Belongs to a **component** that the current passes through.

Electrical energy → other forms.

\(V = W/Q\), where \(W\) is the energy the charge \(Q\) gives to the component.
:::
:::

:::eg A 9.0 V battery drives 15 C of charge around a circuit. How much energy does the battery convert?
The e.m.f. is the energy converted per unit charge, so the energy is e.m.f. × charge:
\[W = QE = 15 \times 9.0 = 135\,\mathrm{J}\]
To 2 significant figures, like the data, that is 140 J. The battery converts this chemical energy into electrical energy. If the wires have negligible resistance, all of it is transferred to the components as the charge passes through them.
:::

## Internal resistance

A real battery gets warm when it delivers a large current. The energy that heats it comes from the charges themselves: they lose some energy *inside* the source before they ever reach the external circuit. We model this as a perfect source of e.m.f. \(E\) in series with a small resistance \(r\), the **internal resistance**, both hidden inside the battery case.

:::def Internal resistance
The resistance of the materials inside a source of e.m.f. It causes some of the e.m.f. to be "lost" inside the source as thermal energy whenever the source supplies a current.
:::

:::html
<figure class="fig"><svg viewBox="105 0 380 258" role="img" aria-label="A cell of e.m.f. E with internal resistance r inside a dashed box, connected to an external resistor R through an ammeter, with a voltmeter across the cell terminals"><rect class="fm" x="160" y="62" width="170" height="56" rx="6"/><rect class="fp s-mute sw1 dash" x="160" y="62" width="170" height="56" rx="6"/><path class="ln" d="M120 210V90H195M205 90H440V210H120"/><path class="ln" d="M205 70V110"/><path class="ln thick" d="M195 80V100"/><rect class="fp s-ink sw2" x="245" y="82" width="50" height="16"/><text class="tl ti tc" x="270" y="76">r</text><text class="tl ti te" x="187" y="96">E</text><circle class="fi" cx="150" cy="90" r="3.5"/><circle class="fi" cx="340" cy="90" r="3.5"/><path class="ln" d="M150 90V30H232M258 30H340V90"/><circle class="fp s-ink sw2" cx="245" cy="30" r="13"/><text class="tb tc" x="245" y="35">V</text><text class="tl" x="268" y="22">terminal p.d. V</text><rect class="fp s-ink sw2" x="432" y="125" width="16" height="50"/><text class="tl ti" x="458" y="155">R</text><circle class="fp s-ink sw2" cx="280" cy="210" r="13"/><text class="tb tc" x="280" y="215">A</text><path class="c1" d="M400 228H350" marker-end="url(#ah-phys)"/><text class="tl ti ta" x="376" y="246">I</text><text class="tl tc" x="245" y="138">the cell (inside the dashed box)</text></svg><figcaption>A real cell behaves like a perfect e.m.f. E in series with an internal resistance r. The voltmeter can only reach the terminals, so it reads the terminal p.d. V, not E.</figcaption></figure>
:::

Apply energy conservation to one coulomb going round this circuit. The source gives it \(E\) joules. It gives \(IR\) joules to the external resistor and \(Ir\) joules to the internal resistance. So

:::formula E.m.f. and internal resistance
\[E = I(R + r) \qquad\qquad V = E - Ir\]
\(E\): e.m.f. (V) · \(I\): current (A) · \(R\): external (load) resistance (Ω) · \(r\): internal resistance (Ω) · \(V = IR\): terminal p.d. (V). The term \(Ir\) is often called the **lost volts**.
:::

The second equation tells the whole story. When no current flows, \(V = E\): an ideal voltmeter across an isolated cell reads its e.m.f. As the current increases, more energy is wasted inside the source, so the terminal p.d. falls. The terminal p.d. of a source that is supplying current is always **less** than its e.m.f.

:::eg A cell of e.m.f. 1.50 V and internal resistance 0.50 Ω is connected to a 2.5 Ω resistor. Find the current, the terminal p.d. and the power wasted inside the cell.
The total resistance in the loop is \(R + r = 2.5 + 0.50 = 3.0\,\Omega\).
\[I = \frac{E}{R + r} = \frac{1.50}{3.0} = 0.50\,\mathrm{A}\]
Terminal p.d.: \(V = IR = 0.50 \times 2.5 = 1.25\,\mathrm{V}\). Check with the other form: \(E - Ir = 1.50 - 0.50 \times 0.50 = 1.25\,\mathrm{V}\). They agree.

Power wasted inside the cell: \(I^2 r = 0.50^2 \times 0.50 = 0.125\,\mathrm{W}\), while the resistor receives \(I^2 R = 0.625\,\mathrm{W}\). One sixth of the energy never leaves the cell.
:::

:::eg A car battery has e.m.f. 12.0 V and internal resistance 0.020 Ω. The starter motor draws 150 A. Explain why the headlights dim while the engine is being started.
Lost volts: \(Ir = 150 \times 0.020 = 3.0\,\mathrm{V}\). [C1]

Terminal p.d.: \(V = E - Ir = 12.0 - 3.0 = 9.0\,\mathrm{V}\). [A1]

The headlights are connected across the same terminals, so the p.d. across them falls from nearly 12 V to 9.0 V and they receive less power. [B1] The internal resistance of a car battery is made very small precisely so that it can deliver currents this large.
:::

:::tip Why some supplies have a large internal resistance on purpose
A school EHT supply (several thousand volts) contains a large resistance, often around \(50\,\mathrm{M\Omega}\). If you touch the terminals by mistake, \(E = I(R + r)\) with a huge \(r\) keeps the current tiny. A large internal resistance is a safety feature when you never need a large current.
:::

### Measuring E and r with a graph

Rearrange \(V = E - Ir\) into the form \(y = mx + c\):
\[V = -r\,I + E\]
So a graph of terminal p.d. \(V\) (on the \(y\)-axis) against current \(I\) (on the \(x\)-axis) is a straight line. Its **\(y\)-intercept is \(E\)** and its **gradient is \(-r\)**.

:::lab Finding the e.m.f. and internal resistance of a cell
:::steps
1. Connect the cell in series with an ammeter, a switch and a variable resistor. Connect a voltmeter across the cell's terminals.
2. Close the switch only while reading, so the cell does not warm up (its internal resistance changes with temperature).
3. Record \(V\) and \(I\) for at least six settings of the variable resistor, spread over the whole range.
4. Plot \(V\) against \(I\) and draw the line of best fit. Read \(E\) from the \(y\)-intercept; the internal resistance is minus the gradient.
:::
:::

:::plot Terminal p.d. against current for a cell. The y-intercept is the e.m.f., and the gradient is −r.
--f "1.55-0.8*x" --x 0 1.6 --y 0 1.8 --pt "0,1.55,E = 1.55 V@ne" --pt "1,0.75,(1.00, 0.75)@ne" --xlabel "I / A" --ylabel "V / V" --label "V = E − Ir"
:::

:::eg Use the graph above to find the e.m.f. and the internal resistance of the cell.
The \(y\)-intercept gives the e.m.f.: \(E = 1.55\,\mathrm{V}\). [B1]

Use two points far apart on the line, \((0, 1.55)\) and \((1.00, 0.75)\):
\[\text{gradient} = \frac{0.75 - 1.55}{1.00 - 0} = -0.80\,\mathrm{V\,A^{-1}}\] [C1]
The gradient is \(-r\), so \(r = 0.80\,\Omega\). [A1]
:::

:::eg A battery is connected to a 4.0 Ω resistor and the terminal p.d. is 2.4 V. With a 9.0 Ω resistor instead, the terminal p.d. is 2.7 V. Find the e.m.f. and the internal resistance.
Find each current from \(I = V/R\): \(I_1 = 2.4/4.0 = 0.60\,\mathrm{A}\) and \(I_2 = 2.7/9.0 = 0.30\,\mathrm{A}\). [C1]

Write \(E = V + Ir\) for both cases. The e.m.f. and \(r\) are the same in each:
\[E = 2.4 + 0.60r \qquad E = 2.7 + 0.30r\] [M1]
Subtract: \(0 = -0.3 + 0.30r\), so \(r = 1.0\,\Omega\). [A1]

Then \(E = 2.4 + 0.60 \times 1.0 = 3.0\,\mathrm{V}\). [A1]
:::

## Kirchhoff's laws

Kirchhoff's two laws are not new physics. They are the two great conservation laws, written in a form that fits circuits.

:::def Kirchhoff's first law
The sum of the currents entering any junction in a circuit is equal to the sum of the currents leaving that junction.
:::

Current is the rate of flow of charge. Charge cannot be created, destroyed or stored at a junction, so every coulomb that arrives each second must leave each second. Kirchhoff's first law is a consequence of the **conservation of charge**.

:::def Kirchhoff's second law
Around any closed loop in a circuit, the sum of the e.m.f.s is equal to the sum of the p.d.s.
:::

Follow one coulomb around a closed loop back to where it started. It gains energy \(E\) from each source and gives away energy \(V\) in each component. It ends where it began, with the same energy, so the total gained must equal the total given away. Kirchhoff's second law is a consequence of the **conservation of energy**.

:::analogy
Think of charge as walkers on a hill path. Sources are ski lifts that raise them (e.m.f.), and components are slopes they walk down (p.d.). A walker who goes round any closed route returns to the same height, so the total height gained on lifts equals the total height lost on slopes. And at a fork in the path, the number of walkers arriving each minute equals the number leaving.
:::

:::steps
1. Mark a current on every branch, with an arrow. Guess the direction if you do not know it: a negative answer just means the current flows the other way.
2. Use the first law at junctions so that you use as few unknown currents as possible.
3. Choose a loop and go round it in one direction. An e.m.f. counts as positive if your direction goes through the source from − to +. A p.d. \(IR\) counts as positive if your direction is the same as the current arrow.
4. Write one equation for each loop you need, and solve them simultaneously.
:::

:::html
<figure class="fig"><svg viewBox="0 18 520 236" role="img" aria-label="A two-loop circuit. Left branch: a 12 volt cell and a 2.0 ohm resistor carrying current I1 upwards. Middle branch: a 2.0 ohm resistor carrying current I1 plus I2 downwards. Right branch: a 9.0 volt cell and a 2.0 ohm resistor carrying current I2 upwards."><path class="ln" d="M80 165V40H420V165M80 175V220H420V175M250 40V220"/><path class="ln" d="M64 165H96M404 165H436"/><path class="ln thick" d="M72 175H88M412 175H428"/><rect class="fp s-ink sw2" x="72" y="70" width="16" height="40"/><rect class="fp s-ink sw2" x="242" y="110" width="16" height="40"/><rect class="fp s-ink sw2" x="412" y="70" width="16" height="40"/><circle class="fi" cx="250" cy="40" r="4"/><circle class="fi" cx="250" cy="220" r="4"/><text class="tl tc" x="250" y="32">P</text><text class="tl tc" x="250" y="240">Q</text><text class="tl te" x="62" y="95">R₁ = 2.0 Ω</text><text class="tl te" x="56" y="176">E₁ = 12 V</text><text class="tl" x="266" y="135">R₃ = 2.0 Ω</text><text class="tl" x="440" y="95">R₂ = 2.0 Ω</text><text class="tl" x="444" y="176">E₂ = 9.0 V</text><path class="c1" d="M106 150V120" marker-end="url(#ah-phys)"/><text class="tl ta" x="114" y="142">I₁</text><path class="c1" d="M394 150V120" marker-end="url(#ah-phys)"/><text class="tl ta te" x="386" y="142">I₂</text><path class="c1" d="M230 160V190" marker-end="url(#ah-phys)"/><text class="tl ta te" x="222" y="182">I₁ + I₂</text></svg><figcaption>Two cells, each with its positive terminal at the top, share the middle resistor. By the first law at junction P, the middle branch carries I₁ + I₂.</figcaption></figure>
:::

:::eg In the circuit above, the cells have negligible internal resistance. Find the currents \(I_1\) and \(I_2\) and the current in the middle resistor.
Kirchhoff's first law at P: the middle resistor carries \(I_1 + I_2\). [B1]

Left loop (clockwise, through \(E_1\) from − to +, down through \(R_3\)):
\[12 = 2.0 I_1 + 2.0(I_1 + I_2) \quad\Rightarrow\quad 4I_1 + 2I_2 = 12\] [M1]
Right loop (anticlockwise, through \(E_2\) from − to +, down through \(R_3\)):
\[9.0 = 2.0 I_2 + 2.0(I_1 + I_2) \quad\Rightarrow\quad 2I_1 + 4I_2 = 9\] [M1]
Double the second equation and subtract the first: \(6I_2 = 6\), so \(I_2 = 1.0\,\mathrm{A}\). Then \(4I_1 = 12 - 2.0\), so \(I_1 = 2.5\,\mathrm{A}\). [A1]

The middle resistor carries \(I_1 + I_2 = 3.5\,\mathrm{A}\). [A1]

**Check** with the outer loop (both cells, the middle branch left out): going clockwise, \(E_1 - E_2 = 12 - 9.0 = 3.0\,\mathrm{V}\), and \(2.0 \times 2.5 - 2.0 \times 1.0 = 3.0\,\mathrm{V}\). The outer loop also balances.
:::

:::warn Signs in loop equations
Most Kirchhoff marks are lost on signs, not physics. Decide your direction round the loop before writing anything, then apply the two sign rules in step 3 to every source and every resistor in that loop. If two cells in a loop face opposite ways, their e.m.f.s subtract.
:::

## Resistors in series and in parallel

The two formulae for combined resistance are both on the data sheet, but the syllabus asks you to **derive** them from Kirchhoff's laws. Both derivations are short, and both are examinable.

:::proof examinable Resistors in series
Resistors \(R_1, R_2, R_3, \dots\) are in series, so there are no junctions between them.
By Kirchhoff's first law, the same current \(I\) passes through each resistor.
By Kirchhoff's second law, the total p.d. \(V\) across the combination equals the sum of the p.d.s across the resistors:
\[V = V_1 + V_2 + V_3 + \dots\]
Use \(V = IR\) for each resistor, and for a single resistor \(R\) that could replace them all:
\[IR = IR_1 + IR_2 + IR_3 + \dots\]
The current \(I\) is the same in every term, so divide by \(I\):
\[R = R_1 + R_2 + R_3 + \dots\]
:::

:::proof examinable Resistors in parallel
Resistors \(R_1, R_2, R_3, \dots\) are in parallel between the same two junctions.
By Kirchhoff's second law (a loop through any one resistor and the supply), the p.d. \(V\) across each resistor is the same.
By Kirchhoff's first law, the total current \(I\) splits between the branches:
\[I = I_1 + I_2 + I_3 + \dots\]
Use \(I = V/R\) for each branch, and for a single resistor \(R\) that could replace them all:
\[\frac{V}{R} = \frac{V}{R_1} + \frac{V}{R_2} + \frac{V}{R_3} + \dots\]
The p.d. \(V\) is the same in every term, so divide by \(V\):
\[\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots\]
:::

:::formula Combined resistance
\[R = R_1 + R_2 + \dots \quad\text{(series)} \qquad\qquad \frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2} + \dots \quad\text{(parallel)}\]
For two resistors in parallel, \(R = \dfrac{R_1 R_2}{R_1 + R_2}\) ("product over sum"). For \(n\) identical resistors \(R\) in parallel, the total is \(R/n\).
:::

Two quick checks catch most mistakes. Adding a resistor in series always **increases** the total. Adding a resistor in parallel always **decreases** the total, because it opens a new path for the charge, so a parallel combination is always smaller than its smallest resistor.

:::eg A 12 V supply of negligible internal resistance is connected to a 6.0 Ω resistor in series with a parallel pair of 3.0 Ω and 6.0 Ω. Find the current in each resistor.
Parallel pair: \(\dfrac{3.0 \times 6.0}{3.0 + 6.0} = 2.0\,\Omega\). Total: \(6.0 + 2.0 = 8.0\,\Omega\). [C1]

Supply current: \(I = 12/8.0 = 1.5\,\mathrm{A}\), which passes through the 6.0 Ω series resistor. [A1]

The p.d. across the parallel pair is \(1.5 \times 2.0 = 3.0\,\mathrm{V}\). So the 3.0 Ω resistor carries \(3.0/3.0 = 1.0\,\mathrm{A}\) and the 6.0 Ω resistor carries \(3.0/6.0 = 0.50\,\mathrm{A}\). [A1]

**Check** with the first law: \(1.0 + 0.50 = 1.5\,\mathrm{A}\), the supply current.
:::

## Potential dividers

Two resistors in series across a supply share its p.d. between them, in the ratio of their resistances. This simple circuit, the **potential divider**, gives you any fraction of the supply p.d. you want.

:::formula The potential divider
\[V_\text{out} = \frac{R_2}{R_1 + R_2} \times V_\text{in} \qquad\qquad \frac{V_1}{V_2} = \frac{R_1}{R_2}\]
\(V_\text{in}\): p.d. across the whole divider · \(V_\text{out}\): p.d. across \(R_2\) · \(V_1, V_2\): p.d.s across \(R_1, R_2\). This assumes nothing connected to the output draws a significant current.
:::

:::proof Why the p.d. divides in the ratio of the resistances
The resistors are in series, so the same current \(I\) passes through both (first law).
The total resistance is \(R_1 + R_2\), so \(I = \dfrac{V_\text{in}}{R_1 + R_2}\).
The p.d. across \(R_2\) is \(V_\text{out} = IR_2 = \dfrac{R_2}{R_1 + R_2}\,V_\text{in}\).
Dividing \(V_1 = IR_1\) by \(V_2 = IR_2\), the current cancels: \(\dfrac{V_1}{V_2} = \dfrac{R_1}{R_2}\).
The larger resistor always takes the larger share of the p.d.
:::

:::eg A 9.0 V supply is connected across a 10 kΩ resistor in series with a 5.0 kΩ resistor. Find the p.d. across the 5.0 kΩ resistor.
\[V_\text{out} = \frac{5.0}{10 + 5.0} \times 9.0 = 3.0\,\mathrm{V}\]
The kilohms cancel in the fraction, so you do not need to convert them. The 10 kΩ resistor takes the other 6.0 V: twice the resistance, twice the p.d.
:::

### Sensors in potential dividers

Replace one resistor with a sensor and the output p.d. follows the world outside. From [Electricity](#phys.electricity): the resistance of a **thermistor** falls as its temperature rises, and the resistance of a **light-dependent resistor (LDR)** falls as the light intensity rises.

:::html
<figure class="fig"><svg viewBox="30 25 475 255" role="img" aria-label="Potential divider: a 6.0 volt battery across a thermistor on top and a 2.0 kilohm fixed resistor below. The output voltage is taken across the fixed resistor."><path class="ln" d="M100 145V40H300V260H100V155"/><path class="ln" d="M84 145H116"/><path class="ln thick" d="M92 155H108"/><text class="tl te" x="76" y="155">6.0 V</text><rect class="fp s-ink sw2" x="292" y="70" width="16" height="50"/><path class="ln" d="M278 128H286L316 62"/><text class="tl" x="322" y="100">thermistor</text><rect class="fp s-ink sw2" x="292" y="180" width="16" height="50"/><text class="tl" x="322" y="210">2.0 kΩ</text><circle class="fi" cx="300" cy="150" r="4"/><circle class="fi" cx="300" cy="260" r="4"/><path class="ln" d="M300 150H420M300 260H420"/><circle class="fp s-ink sw2" cx="424" cy="150" r="4"/><circle class="fp s-ink sw2" cx="424" cy="260" r="4"/><path class="c1" d="M450 205V160" marker-end="url(#ah-phys)"/><path class="c1" d="M450 205V250" marker-end="url(#ah-phys)"/><text class="tl ta" x="462" y="210">Vout</text></svg><figcaption>A temperature sensor. When the thermistor warms, its resistance falls, so it takes a smaller share of the 6.0 V and the output across the fixed resistor rises.</figcaption></figure>
:::

:::eg In the circuit above, the thermistor's resistance is 4.0 kΩ at 20 °C and 1.0 kΩ at 60 °C. Find \(V_\text{out}\) at each temperature.
At 20 °C: \(V_\text{out} = \dfrac{2.0}{4.0 + 2.0} \times 6.0 = 2.0\,\mathrm{V}\). [C1]

At 60 °C: \(V_\text{out} = \dfrac{2.0}{1.0 + 2.0} \times 6.0 = 4.0\,\mathrm{V}\). [A1]

The output rises with temperature, so this circuit could switch on a cooling fan when \(V_\text{out}\) passes a set value. Swap the thermistor and the fixed resistor and the output would *fall* as the temperature rises, which suits a heater.
:::

:::eg A street light should switch on when it gets dark. An LDR (100 kΩ in the dark, 1.0 kΩ in daylight) is in series with a 10 kΩ resistor across a 5.0 V supply. Where should the LDR go, and what are the two output p.d.s?
The control circuit needs a **high** output in the dark. In the dark the LDR has a high resistance, so it takes most of the p.d. Take \(V_\text{out}\) across the LDR: put the LDR at the bottom, in the \(R_2\) position. [B1]

Dark: \(V_\text{out} = \dfrac{100}{10 + 100} \times 5.0 = 4.5\,\mathrm{V}\). Daylight: \(V_\text{out} = \dfrac{1.0}{10 + 1.0} \times 5.0 = 0.45\,\mathrm{V}\). [A1]
:::

Try it yourself below. Put the sensor on top, then at the bottom, and watch which way \(V_\text{out}\) moves. Then change the fixed resistor: a value close to the sensor's resistance in the middle of its range makes the output change fastest there, which is how designers choose it.

:::html
<div class="widget" data-w="phys-divider" data-mode="thermistor" data-pos="top" data-vin="6" data-r="10"></div>
:::

:::exam Explaining a sensor circuit
"Explain what happens to the reading on the voltmeter as the temperature rises" is a common 3-mark question. Give the chain in order, one link per sentence: the thermistor's resistance **decreases**; so its share of the supply p.d. **decreases** (or the current increases); so the p.d. across the fixed resistor **increases**, because the two p.d.s add up to the supply p.d. A single sentence such as "the voltage goes up because it gets hotter" scores nothing.
:::

## The potentiometer and null methods

A voltmeter across a cell draws a small current, so it reads the terminal p.d., slightly less than the e.m.f. To measure an e.m.f. exactly you need a method that draws **no current at all** from the cell. The **potentiometer** does this.

A potentiometer is a long uniform resistance wire AB, often 1.00 m, with a steady **driver cell** across it. Because the wire is uniform, the p.d. between A and any point along it is proportional to the length from A. The wire is a ruler marked in volts.

:::html
<figure class="fig"><svg viewBox="46 0 506 274" role="img" aria-label="Potentiometer circuit: a driver cell across a uniform wire AB above a metre rule. A test cell and a galvanometer are connected from A to a sliding contact J on the wire, a balance length l from A."><path class="ln" d="M80 230V40H295M305 40H520V140"/><path class="ln" d="M295 24V56"/><path class="ln thick" d="M305 32V48"/><text class="tl tc" x="300" y="16">driver cell</text><path class="ln thick" d="M80 140H520"/><rect class="fm s-mute sw1" x="80" y="150" width="440" height="14"/><path class="ln-m thin" d="M124 150V158M168 150V158M212 150V158M256 150V158M300 150V158M344 150V158M388 150V158M432 150V158M476 150V158"/><circle class="fi" cx="80" cy="140" r="4"/><text class="tl te" x="70" y="145">A</text><text class="tl" x="528" y="145">B</text><path class="ln" d="M80 230H215M225 230H317M343 230H380V150"/><path class="ln" d="M215 214V246"/><path class="ln thick" d="M225 222V238"/><path class="ln" d="M380 160V147" marker-end="url(#ah)"/><circle class="fp s-ink sw2" cx="330" cy="230" r="13"/><path class="ln thin" d="M324 239L335 220" marker-end="url(#ah)"/><text class="tl" x="390" y="186">J (jockey)</text><path class="c1" d="M230 118H84" marker-end="url(#ah-phys)"/><path class="c1" d="M230 118H376" marker-end="url(#ah-phys)"/><text class="tl ti ta tc" x="230" y="110">l</text><text class="tl tc" x="220" y="264">test cell</text><text class="tl tc" x="330" y="264">galvanometer</text></svg><figcaption>Both cells have their positive terminals connected to A. The jockey J is slid along the wire until the galvanometer reads zero; the balance length l is then measured from A.</figcaption></figure>
:::

The test cell is connected, positive to positive, from A to a sliding contact (a **jockey**) through a **galvanometer**, a very sensitive centre-zero ammeter. Slide the jockey until the galvanometer shows **no deflection**. At this **balance point** the p.d. along length \(l\) of the wire exactly equals the test cell's e.m.f., so no current flows through the test cell in either direction.

:::def Null method
A measurement in which a quantity is found by adjusting a circuit until a detector, such as a galvanometer, reads zero. At balance no current flows in the detector branch.
:::

Because no current flows through the test cell at balance, there are no lost volts across its internal resistance: the potentiometer measures the true **e.m.f.**, not the terminal p.d. The galvanometer does not need to be calibrated either. It only has to show when the current is zero.

:::formula Comparing e.m.f.s with a potentiometer
\[\frac{E_1}{E_2} = \frac{l_1}{l_2}\]
\(E_1, E_2\): e.m.f.s of the two cells · \(l_1, l_2\): their balance lengths, measured from A on the same wire with the same driver current.
:::

:::eg A standard cell of e.m.f. 1.02 V balances at 51.0 cm on a potentiometer wire. A second cell balances at 74.0 cm. Find the e.m.f. of the second cell.
The p.d. along the wire is proportional to length, so the e.m.f.s are in the ratio of the balance lengths:
\[E_2 = E_1 \times \frac{l_2}{l_1} = 1.02 \times \frac{74.0}{51.0} = 1.48\,\mathrm{V}\]
The lengths are in the same units, so they cancel: no need to change centimetres into metres.
:::

:::warn When there is no balance point
If the galvanometer deflects the same way wherever the jockey touches, either the test cell is connected the wrong way round (negative to A), or its e.m.f. is larger than the p.d. across the whole wire. The driver cell must provide a larger p.d. across AB than the e.m.f. being measured.
:::

:::board
The slide-wire potentiometer and the galvanometer null method are part of the Cambridge 9702 syllabus (outcomes 10.3.2 and 10.3.3), so they can be examined: know how a balance length compares two p.d.s and why no current flows in the galvanometer at balance. Some textbooks write \(\varepsilon\) for e.m.f. instead of \(E\); the physics is the same.
:::

:::eg Spot the error: a battery of e.m.f. 6.0 V and internal resistance 0.50 Ω is connected to a 2.5 Ω resistor. Calculate the terminal p.d.
A student wrote this answer.

Line 1: \(I = \dfrac{E}{R + r} = \dfrac{6.0}{2.5 + 0.50} = 2.0\,\mathrm{A}\)
Line 2: lost volts \(= Ir = 2.0 \times 0.50 = 1.0\,\mathrm{V}\)
Line 3: terminal p.d. \(= E + Ir = 6.0 + 1.0 = 7.0\,\mathrm{V}\)

Lines 1 and 2 are correct. [C1] **Line 3 is wrong: the lost volts are subtracted from the e.m.f., not added, because energy is lost inside the battery. The answer mark is lost.** [A0]

Correct working: \(V = E - Ir = 6.0 - 1.0 = 5.0\,\mathrm{V}\). [A1]

Check: \(V = IR = 2.0 \times 2.5 = 5.0\,\mathrm{V}\). A source that is supplying current can never have a terminal p.d. bigger than its e.m.f., so 7.0 V should have looked wrong at once.
:::

:::try Start easy, finish at exam standard
Q: Currents of 2.5 A enter a junction along one wire. Two wires leave it: one carries 0.8 A. What does the other carry?
A: By Kirchhoff's first law, \(2.5 = 0.8 + I\), so \(I = 1.7\,\mathrm{A}\).
Q: Find the combined resistance of 47 Ω, 33 Ω and 20 Ω in series, and of three 12 Ω resistors in parallel.
A: Series: \(47 + 33 + 20 = 100\,\Omega\). Parallel: three identical resistors give \(12/3 = 4.0\,\Omega\).
Q: A cell of e.m.f. 1.5 V and internal resistance 0.30 Ω supplies a current of 0.50 A. Find the terminal p.d.
A: \(V = E - Ir = 1.5 - 0.50 \times 0.30 = 1.35\,\mathrm{V}\), about 1.4 V.
Q: Explain, in terms of energy, the difference between the e.m.f. of a battery and the p.d. across a lamp.
A: The e.m.f. is the energy converted from chemical to electrical energy per unit charge by the battery. The p.d. is the energy converted from electrical energy into other forms (thermal energy and light) per unit charge in the lamp.
Q: A potential divider is made from a 1.0 kΩ resistor and a 2.0 kΩ resistor in series across a 12 V supply. Find the p.d. across each resistor.
A: \(V_{2.0} = \dfrac{2.0}{1.0 + 2.0} \times 12 = 8.0\,\mathrm{V}\), and the 1.0 kΩ resistor takes \(12 - 8.0 = 4.0\,\mathrm{V}\).
Q: Why should a voltmeter have a very high resistance?
A: So that it draws almost no current. Then connecting it in parallel does not change the current or the p.d. it is trying to measure.
Q: Two 6.0 Ω resistors in parallel are connected in series with a 3.0 Ω resistor across a 12 V supply of negligible internal resistance. Find the supply current, the p.d. across the parallel pair and the current in each 6.0 Ω resistor.
A: The parallel pair is \(6.0/2 = 3.0\,\Omega\), so the total is \(6.0\,\Omega\) and \(I = 12/6.0 = 2.0\,\mathrm{A}\). The p.d. across the pair is \(2.0 \times 3.0 = 6.0\,\mathrm{V}\), and each 6.0 Ω resistor carries \(6.0/6.0 = 1.0\,\mathrm{A}\).
Q: A cell has e.m.f. 3.0 V. When it supplies 0.40 A, the terminal p.d. is 2.6 V. Find its internal resistance, and the current it would supply if its terminals were short-circuited with a thick wire.
A: Lost volts \(= 3.0 - 2.6 = 0.40\,\mathrm{V}\), so \(r = 0.40/0.40 = 1.0\,\Omega\). With \(R = 0\), \(I = E/r = 3.0/1.0 = 3.0\,\mathrm{A}\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the electromotive force (e.m.f.) of a source.
A: Energy transferred from other forms to electrical energy [B1] per unit charge, in driving charge round a complete circuit. [B1]
Q: [3 marks] ★ A 20 Ω resistor and a 30 Ω resistor are connected in parallel. This pair is connected in series with an 8.0 Ω resistor across a 6.0 V supply of negligible internal resistance. Calculate the current from the supply.
A: Parallel pair: \(\dfrac{20 \times 30}{20 + 30} = 12\,\Omega\) [C1] so the total is \(12 + 8.0 = 20\,\Omega\). [A1] \(I = 6.0/20 = 0.30\,\mathrm{A}\). [A1]
Q: [3 marks] ★★ The terminal p.d. of a battery of e.m.f. 12 V falls to 10.8 V when it supplies a current of 3.0 A. Calculate the internal resistance of the battery and the power dissipated inside it.
A: \(r = \dfrac{E - V}{I} = \dfrac{12 - 10.8}{3.0}\) [C1] \(= 0.40\,\Omega\). [A1] Power dissipated: \(I^2 r = 3.0^2 \times 0.40 = 3.6\,\mathrm{W}\). [A1]
Q: [4 marks] ★★ A thermistor is connected in series with a 1.5 kΩ fixed resistor across a 5.0 V supply. The output p.d. is taken across the fixed resistor. (a) At a certain temperature the thermistor's resistance is 3.5 kΩ. Calculate the output p.d. (b) The temperature now rises. State and explain the change in the output p.d.
A: (a) \(V_\text{out} = \dfrac{1.5}{3.5 + 1.5} \times 5.0\) [C1] \(= 1.5\,\mathrm{V}\). [A1] (b) The resistance of the thermistor decreases, so it takes a smaller share of the 5.0 V. [B1] The p.d. across the fixed resistor (the output) therefore increases. [B1]
Q: [3 marks] ★★ A cell of e.m.f. 9.0 V and a cell of e.m.f. 3.0 V, both of negligible internal resistance, are connected in a single loop with their positive terminals facing each other, in series with a 2.0 Ω resistor and a 4.0 Ω resistor. Calculate the current and state its direction through the 3.0 V cell.
H: The cells oppose each other, so their e.m.f.s subtract in the loop equation.
A: By Kirchhoff's second law, \(9.0 - 3.0 = I(2.0 + 4.0)\) [C1] so \(I = 1.0\,\mathrm{A}\). [A1] The larger e.m.f. wins: current passes through the 3.0 V cell from its positive terminal to its negative terminal, so that cell is being charged. [B1]
Q: [5 marks] ★★ A potentiometer wire AB is 1.00 m long. A driver cell maintains a p.d. of 2.0 V across AB. (a) Explain why, at the balance point, the potentiometer measures the e.m.f. of a test cell rather than its terminal p.d. (b) A test cell balances at 72.5 cm from A. Calculate its e.m.f. (c) State why a cell of e.m.f. 2.5 V could not be balanced on this wire.
A: (a) At balance the galvanometer reads zero, so no current flows through the test cell [B1] and there is no p.d. across its internal resistance (no lost volts). [B1] (b) The p.d. per unit length is \(2.0/1.00 = 2.0\,\mathrm{V\,m^{-1}}\), so \(E = 2.0 \times 0.725\) [C1] \(= 1.45\,\mathrm{V}\). [A1] (c) The p.d. across the whole wire is only 2.0 V, which is less than 2.5 V, so there is no point on the wire where the p.d. from A equals the e.m.f. [B1]
Q: [6 marks] (#phys.electricity) ★★★ A car battery has e.m.f. 12.0 V and internal resistance 0.025 Ω. While the engine is started, the starter motor draws a current of 160 A for 2.5 s. (a) Calculate the terminal p.d. of the battery during the start. (b) Calculate the power delivered to the starter motor. (c) Calculate the energy dissipated inside the battery during the start. (d) Suggest why the car's headlights dim while the engine is being started.
H: Lost volts first: \(Ir\).
H: The energy dissipated inside the battery is the power \(I^2 r\) multiplied by the time.
A: (a) \(V = E - Ir = 12.0 - 160 \times 0.025\) [C1] \(= 8.0\,\mathrm{V}\). [A1] (b) \(P = VI = 8.0 \times 160 = 1280\,\mathrm{W} \approx 1.3\,\mathrm{kW}\). [A1] (c) \(W = I^2 r t = 160^2 \times 0.025 \times 2.5\) [C1] \(= 1600\,\mathrm{J}\). [A1] (d) The headlights are connected across the battery terminals, and the terminal p.d. falls from 12.0 V to 8.0 V, so they receive less power. [B1]
Q: [7 marks] ★★★ A potentiometer wire is 1.00 m long and has resistance 5.0 Ω. It is connected in series with a driver cell of e.m.f. 4.0 V, negligible internal resistance, and a fixed resistor \(R\). A cell of e.m.f. 1.5 V is to balance at 75.0 cm from A. (a) Calculate the p.d. needed across the whole wire. (b) Calculate the current in the wire. (c) Calculate \(R\). (d) Explain why adding \(R\) makes the e.m.f. measurement more precise than connecting the 4.0 V cell directly across the wire.
H: At balance, the p.d. across 0.750 m of wire is 1.5 V. The p.d. is proportional to length.
H: The wire and \(R\) are in series with the driver cell, so they share its 4.0 V.
H: For (d), think about the percentage uncertainty in a balance length.
A: (a) \(V_{AB} = 1.5 \times \dfrac{1.00}{0.750}\) [C1] \(= 2.0\,\mathrm{V}\). [A1] (b) \(I = 2.0/5.0 = 0.40\,\mathrm{A}\). [A1] (c) The p.d. across \(R\) is \(4.0 - 2.0 = 2.0\,\mathrm{V}\), so \(R = 2.0/0.40\) [C1] \(= 5.0\,\Omega\). [A1] (d) Without \(R\) the p.d. across the wire would be 4.0 V and the cell would balance at only 37.5 cm. [B1] A longer balance length has a smaller percentage uncertainty for the same uncertainty in reading the rule. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A battery of e.m.f. 6.0 V and internal resistance 2.0 Ω is connected to a variable resistor \(R\). (a) Show that the power delivered to \(R\) is \(P = \dfrac{E^2 R}{(R + r)^2}\). (b) By writing \(P = \dfrac{E^2}{R + 2r + r^2/R}\), show that \(P\) is greatest when \(R = r\), and find the maximum power. (c) Find the efficiency of the battery when it delivers maximum power.
H: For (b), the power is greatest when the denominator \(R + r^2/R\) is smallest. Write \(R + \dfrac{r^2}{R} = \left(\sqrt{R} - \dfrac{r}{\sqrt{R}}\right)^2 + 2r\).
H: Efficiency is the useful power (in \(R\)) divided by the total power the source converts, \(EI\).
A: (a) \(I = \dfrac{E}{R + r}\) and \(P = I^2 R\), so \(P = \dfrac{E^2 R}{(R + r)^2}\). [B1] (b) Dividing top and bottom by \(R\) gives \(P = \dfrac{E^2}{R + 2r + r^2/R}\). [M1] Since \(R + \dfrac{r^2}{R} = \left(\sqrt{R} - \dfrac{r}{\sqrt{R}}\right)^2 + 2r \geq 2r\), the denominator is smallest when the square is zero, that is when \(R = r\). [M1] Then \(P_\text{max} = \dfrac{E^2}{4r} = \dfrac{6.0^2}{4 \times 2.0} = 4.5\,\mathrm{W}\). [A1] (c) With \(R = r\), half the e.m.f. is lost inside: the source converts \(EI = 6.0 \times 1.5 = 9.0\,\mathrm{W}\) [C1] and delivers 4.5 W, so the efficiency is 50%. [A1] Maximum power and maximum efficiency are not the same thing: a power station wants high efficiency, so its load resistance is far larger than its internal resistance.
Q: [6 marks] ★★★ Two 100 kΩ resistors form a potential divider across a 12.0 V supply. (a) A voltmeter of resistance 100 kΩ is connected across one resistor. Calculate its reading. (b) Calculate the minimum resistance a voltmeter must have if its reading is to be no more than 1% below the true value of 6.0 V.
H: The voltmeter is in parallel with the lower resistor, so it forms a new, smaller resistance with it.
H: For (b), find the parallel resistance \(R_p\) that gives 5.94 V, then use \(1/R_p = 1/(100\,\mathrm{k\Omega}) + 1/R_V\).
A: (a) The parallel pair is \(\dfrac{100 \times 100}{100 + 100} = 50\,\mathrm{k\Omega}\). [C1] Reading \(= \dfrac{50}{100 + 50} \times 12.0 = 4.0\,\mathrm{V}\), not 6.0 V. [A1] (b) A reading of \(0.99 \times 6.0 = 5.94\,\mathrm{V}\) needs \(\dfrac{R_p}{100 + R_p} \times 12.0 = 5.94\) [M1] so \(R_p = \dfrac{5.94 \times 100}{6.06} = 98.0\,\mathrm{k\Omega}\). [A1] Then \(\dfrac{1}{R_V} = \dfrac{1}{98.02} - \dfrac{1}{100}\) [M1] so \(R_V = 4.95 \times 10^{3}\,\mathrm{k\Omega} \approx 5.0\,\mathrm{M\Omega}\). [A1] This is why voltmeters used on high-resistance circuits must have resistances of megohms.
:::

:::quiz
? What is the resistance of an ideal ammeter?
+ Zero
- Infinite
- Equal to the resistance of the component it measures
- Very large, so that it draws little current
> The current must pass through an ammeter, so any resistance it has would take p.d. away from the circuit. "Very large" describes a voltmeter, which is connected in parallel.
? Kirchhoff's first law is a consequence of the conservation of which quantity?
+ Charge
- Energy
- Current
- Potential difference
> Charge cannot pile up at a junction, so the charge arriving per second equals the charge leaving per second. Conservation of energy gives the second law, and current is not itself a conserved quantity.
? A cell of e.m.f. 2.0 V and internal resistance 1.0 Ω is connected to a 3.0 Ω resistor. What is the terminal p.d.?
- 2.0 V
+ 1.5 V
- 0.50 V
- 6.0 V
> \(I = 2.0/(3.0 + 1.0) = 0.50\,\mathrm{A}\), so \(V = IR = 1.5\,\mathrm{V}\). 2.0 V ignores the internal resistance, 0.50 V is the lost volts, and 6.0 V comes from multiplying \(E\) by \(R\).
? Three identical resistors, each of resistance \(R\), are connected with two in parallel and the third in series with that pair. What is the total resistance?
+ \(1.5R\)
- \(3R\)
- \(R/3\)
- \(2R/3\)
> The parallel pair is \(R/2\); add the series resistor to get \(1.5R\). \(3R\) is all three in series, \(R/3\) is all three in parallel, and \(2R/3\) is one resistor in parallel with the other two in series.
? A thermistor and a fixed resistor form a potential divider across a constant supply. The temperature rises. What happens to the p.d. across the thermistor?
+ It decreases.
- It increases.
- It stays the same.
- It falls to zero.
> The thermistor's resistance falls, so its share of the fixed supply p.d. falls. It does not fall to zero, because its resistance is still more than zero.
? At the balance point of a potentiometer, what is the current in the galvanometer?
+ Zero
- The same as the current in the potentiometer wire
- A maximum
- The short-circuit current of the test cell
> Balance means the p.d. along the wire exactly matches the test cell's e.m.f., so nothing drives charge through the galvanometer branch.
? A second lamp is connected in parallel with a lamp across a battery that has significant internal resistance. What happens to the terminal p.d. of the battery?
+ It decreases.
- It stays the same.
- It increases.
- It doubles.
> Adding a parallel branch lowers the external resistance, so the current increases and the lost volts \(Ir\) increase. "Stays the same" would only be true for a source with no internal resistance.
:::

:::checklist What you can now do
- [ ] I can recognise and use the standard circuit symbols, and draw and interpret circuit diagrams with meters in the right places.
- [ ] I can define e.m.f. and explain the difference between e.m.f. and p.d. in terms of energy transfer.
- [ ] I can use \(E = I(R + r)\) and \(V = E - Ir\), and explain why the terminal p.d. falls as the current rises.
- [ ] I can find the e.m.f. and internal resistance of a source from a graph of \(V\) against \(I\).
- [ ] I can state Kirchhoff's two laws and link them to the conservation of charge and of energy.
- [ ] I can derive and use the formulae for resistors in series and in parallel.
- [ ] I can use Kirchhoff's laws to find the currents in a circuit with more than one loop.
- [ ] I can use a potential divider, including with a thermistor or an LDR, and explain how its output changes.
- [ ] I can explain how a potentiometer and a galvanometer null method compare e.m.f.s without drawing current.
:::

:::recap
- E.m.f.: energy converted from other forms to electrical energy per unit charge by a source. P.d.: electrical energy converted to other forms per unit charge in a component. Both in volts, \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\).
- A real source is an e.m.f. \(E\) in series with an internal resistance \(r\): \(E = I(R + r)\) and \(V = E - Ir\). The terminal p.d. falls as the current rises.
- A graph of \(V\) against \(I\) is a straight line: \(y\)-intercept \(E\), gradient \(-r\).
- Kirchhoff's first law (currents at a junction) comes from conservation of charge; the second (sum of e.m.f.s = sum of p.d.s round a loop) comes from conservation of energy.
- Series: \(R = R_1 + R_2 + \dots\) Parallel: \(1/R = 1/R_1 + 1/R_2 + \dots\) Both are derived from Kirchhoff's laws.
- Potential divider: \(V_\text{out} = \dfrac{R_2}{R_1 + R_2}V_\text{in}\). The larger resistance takes the larger share. Thermistors and LDRs make the output depend on temperature and light.
- A potentiometer compares e.m.f.s by balance lengths, \(E_1/E_2 = l_1/l_2\). At balance no current flows through the test cell, so it measures the true e.m.f.
- Ideal ammeter: zero resistance, in series. Ideal voltmeter: infinite resistance, in parallel.
:::

:::links
- explore: [Circuit Construction Kit: DC](https://phet.colorado.edu/en/simulations/circuit-construction-kit-dc) · PhET · build circuits with real meters and see the current flow
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the d.c. circuits questions in real papers [unofficial]
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Particle physics](#phys.particles)
