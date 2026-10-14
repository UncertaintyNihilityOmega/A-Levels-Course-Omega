@chapter phys.capacitance
@title Capacitance
@level a2
@paper CAIE P4 · P5 (A Level)
@time 5–7 hours
@summary How capacitors store charge and energy: the definition of capacitance, the series and parallel formulae, the energy stored from the area under a potential–charge graph, and discharge through a resistor with the time constant RC.

:::why
A capacitor is a rechargeable store of energy that can be emptied in a few milliseconds, which is why it powers camera flashes and defibrillators, keeps a computer's memory alive during a power cut and smooths the supply inside a phone charger. The discharge of a capacitor is also the cleanest example in A Level physics of an exponential decay, and the same mathematics returns in radioactive decay. Examiners love it because every part of it can be set as a calculation, a graph or an experiment.
:::

**Before you start**, you need the potential of a charged sphere from [Electric fields](#phys.efields), Kirchhoff's laws from [D.C. circuits](#phys.dc) and the exponential function from [Logarithms and exponentials](#math.p3.logs).

:::try Warm-up
Q: A metal sphere of radius 0.10 m carries a charge of 2.0 nC. Find its potential, taking the potential to be zero at infinity. (from [Electric fields](#phys.efields))
A: \(V = \dfrac{Q}{4\pi\varepsilon_0 r} = \dfrac{8.99 \times 10^{9} \times 2.0 \times 10^{-9}}{0.10} = 1.8 \times 10^{2}\,\mathrm{V}\).
Q: A 6.0 Ω resistor and a 3.0 Ω resistor are in parallel, and this pair is in series with a 4.0 Ω resistor. What is the total resistance? (from [D.C. circuits](#phys.dc))
A: The parallel pair is \(\dfrac{6.0 \times 3.0}{6.0 + 3.0} = 2.0\,\Omega\), so the total is \(2.0 + 4.0 = 6.0\,\Omega\).
Q: Solve \(e^{-x} = 0.25\). (from [Logarithms and exponentials](#math.p3.logs))
A: Take natural logs: \(-x = \ln 0.25\), so \(x = \ln 4 = 1.39\).
:::

## What a capacitor is

A **capacitor** is two conducting plates separated by an insulator. The insulator is called the **dielectric**. It might be air, a vacuum, plastic film or a thin layer of oxide. Because the dielectric is an insulator, no charge can cross from one plate to the other inside the capacitor.

:::html
<figure class="fig small"><svg viewBox="25 30 350 100" role="img" aria-label="Side view of a parallel plate capacitor: two horizontal metal plates, the upper marked plus and the lower marked minus, with an insulating dielectric layer between them. A double dimension arrow shows the separation d between the plates."><rect class="fm" x="60" y="48" width="140" height="62"/><rect class="fi" x="60" y="40" width="140" height="8"/><rect class="fi" x="60" y="110" width="140" height="8"/><text class="tl tc" x="80" y="62">+</text><text class="tl tc" x="113" y="62">+</text><text class="tl tc" x="147" y="62">+</text><text class="tl tc" x="180" y="62">+</text><text class="tl tc" x="80" y="106">−</text><text class="tl tc" x="113" y="106">−</text><text class="tl tc" x="147" y="106">−</text><text class="tl tc" x="180" y="106">−</text><path class="c1" d="M40 79V50" marker-end="url(#ah-phys)"/><path class="c1" d="M40 79V108" marker-end="url(#ah-phys)"/><text class="tl ti" x="48" y="83">d</text><text class="tl" x="212" y="50">metal plate, charge +Q</text><text class="tl" x="212" y="84">dielectric (insulator)</text><text class="tl" x="212" y="118">metal plate, charge −Q</text></svg><figcaption>A parallel plate capacitor. The plates carry equal and opposite charges and the insulating dielectric keeps them apart. The two charges attract each other across the gap.</figcaption></figure>
:::

To **charge** a capacitor you connect it to a source, such as a cell. The source does not add charge to the capacitor. It moves electrons from one plate, through the circuit, to the other. The plate that loses electrons becomes positive, with charge \(+Q\), and the plate that gains them becomes negative, with charge \(-Q\). So the **net charge on a capacitor is always zero**. When a question says "the charge on the capacitor", it means \(Q\), the magnitude of the charge on **one** plate.

:::html
<figure class="fig"><svg viewBox="36 16 470 214" role="img" aria-label="A circuit with a cell, a two-way switch, a resistor R and a capacitor C. With the switch at position 1 the cell is connected in series with the resistor and the capacitor, and a charging current arrow points right along the top wire. With the switch at position 2 the cell is bypassed, the capacitor discharges through the resistor alone, and the discharge current arrow points left along the top wire. The upper plate of the capacitor is marked plus Q and the lower plate minus Q."><path class="ln" d="M130 60H278M322 60H460V122M460 138V210H100V167M160 114V210M100 114V155"/><path class="ln" d="M444 122H476M444 138H476"/><path class="ln" d="M84 155H116"/><path class="ln thick" d="M92 167H108"/><rect class="fp s-ink sw2" x="278" y="52" width="44" height="16"/><path class="ln" d="M130 60L100 110"/><circle class="fi" cx="130" cy="60" r="4"/><circle class="fp s-ink sw2" cx="100" cy="110" r="4"/><circle class="fp s-ink sw2" cx="160" cy="110" r="4"/><circle class="fi" cx="160" cy="210" r="4"/><text class="tl te" x="90" y="114">1</text><text class="tl" x="170" y="114">2</text><text class="tl te" x="76" y="165">cell</text><text class="ts" x="122" y="149">+</text><text class="tl ti tc" x="300" y="44">R</text><text class="tl ti" x="486" y="134">C</text><text class="tl te" x="436" y="120">+Q</text><text class="tl te" x="436" y="148">−Q</text><path class="c1" d="M180 40H245" marker-end="url(#ah-phys)"/><text class="tl tc" x="212" y="30">charging</text><path class="c2" d="M245 80H180" marker-end="url(#ah2-phys)"/><text class="tl tc" x="212" y="96">discharging</text></svg><figcaption>A capacitor charging and discharging through a resistor. With the switch at 1 the cell charges the capacitor. Moved to 2, the capacitor discharges through R, and the current in R reverses.</figcaption></figure>
:::

The circuit symbol is two short parallel lines, as in the symbol chart in [D.C. circuits](#phys.dc). The resistor in the circuit matters. It limits the current, so the capacitor charges or discharges over a measurable time instead of instantly, and later in this chapter you will see exactly how that time depends on \(R\) and \(C\).

## Capacitance

If you double the charge on a given capacitor, the p.d. between its plates doubles too. The ratio of charge to p.d. stays the same, and it describes the capacitor, not the charge it holds at that moment. That ratio is the capacitance.

:::def Capacitance
The charge stored per unit potential difference: \(C = Q/V\). For a parallel plate capacitor, \(Q\) is the charge on one plate and \(V\) is the p.d. between the plates. For an isolated spherical conductor, \(V\) is the potential of the sphere (relative to infinity).
:::

:::def The farad
One farad is one coulomb per volt: \(1\,\mathrm{F} = 1\,\mathrm{C\,V^{-1}}\). A capacitor has a capacitance of 1 F if a p.d. of 1 V stores a charge of 1 C on one plate.
:::

:::formula Capacitance
\[C = \frac{Q}{V}\]
\(C\): capacitance (F) · \(Q\): charge on one plate (C) · \(V\): p.d. across the capacitor (V). Rearranged: \(Q = CV\) and \(V = Q/C\).
:::

The farad is a huge unit. Real capacitors are measured in microfarads (\(1\,\mu\mathrm{F} = 10^{-6}\,\mathrm{F}\)), nanofarads (\(10^{-9}\,\mathrm{F}\)) and picofarads (\(10^{-12}\,\mathrm{F}\)). Always convert to farads before you substitute.

:::eg A \(470\,\mu\mathrm{F}\) capacitor is connected across a 12 V supply. Find the charge on the positive plate.
\[Q = CV = 470 \times 10^{-6} \times 12\] [C1]
\[Q = 5.64 \times 10^{-3}\,\mathrm{C}\] [A1]
That is about 5.6 mC. The negative plate carries \(-5.64\,\mathrm{mC}\), so the capacitor as a whole is neutral.
:::

For a parallel plate capacitor, the capacitance depends on three things. It is **larger for a bigger plate area**, **larger for a smaller separation**, and **larger when the gap is filled with a suitable dielectric (such as plastic or ceramic) instead of air**. Charge on one plate attracts the opposite charge on the other, so plates that are large and close together can hold more charge for the same p.d. You are not asked for a formula here, only for this reasoning: it explains why practical capacitors are often long strips of metal foil rolled up with thin plastic between them.

### Capacitance of an isolated sphere

A single metal sphere is also a capacitor: the other "plate" is the rest of the universe, at zero potential at infinity. Outside a charged sphere the field is the same as that of a point charge at its centre, so the potential at the surface (radius \(r\)) is \(V = \dfrac{Q}{4\pi\varepsilon_0 r}\), from [Electric fields](#phys.efields).

:::proof Capacitance of an isolated sphere
The potential of the sphere is \(V = \dfrac{Q}{4\pi\varepsilon_0 r}\).
Capacitance is charge per unit potential: \(C = \dfrac{Q}{V}\).
Substitute for \(V\): \(C = \dfrac{Q}{\,Q/(4\pi\varepsilon_0 r)\,} = 4\pi\varepsilon_0 r\).
The charge cancels, so the capacitance depends only on the radius. A bigger sphere has a bigger capacitance.
:::

:::eg A metal sphere of radius 5.0 cm is charged to a potential of 1.0 kV. Find its capacitance and the charge on it.
\[C = 4\pi\varepsilon_0 r = \frac{r}{8.99 \times 10^{9}} = \frac{0.050}{8.99 \times 10^{9}}\] [C1]
\[C = 5.56 \times 10^{-12}\,\mathrm{F} \approx 5.6\,\mathrm{pF}\] [A1]
\[Q = CV = 5.56 \times 10^{-12} \times 1000 = 5.6 \times 10^{-9}\,\mathrm{C}\] [A1]
Even at 1 kV, the sphere holds only about 5.6 nC, far less than the 5.6 mC on the capacitor in the last example at only 12 V. This is why capacitors need plates close together: an isolated sphere is a very poor store of charge.
:::

:::eg Treat the Earth as an isolated conducting sphere of radius \(6.37 \times 10^{6}\,\mathrm{m}\). Find its capacitance.
\[C = 4\pi\varepsilon_0 R = \frac{6.37 \times 10^{6}}{8.99 \times 10^{9}}\] [C1]
\[C = 7.09 \times 10^{-4}\,\mathrm{F} \approx 0.71\,\mathrm{mF}\] [A1]
The whole planet has a capacitance only about six times that of the \(120\,\mu\mathrm{F}\) capacitor in a camera flash. A small capacitor with close plates is far better at storing charge than the Earth.
:::

## Capacitors in series and in parallel

Capacitors, like resistors, are often combined, and the syllabus asks you to **derive** both combination formulae from \(C = Q/V\). They are the other way round from resistors: capacitances **add** in parallel, and it is the **reciprocals** that add in series.

:::proof examinable Capacitors in parallel
Capacitors \(C_1, C_2, C_3, \dots\) are connected in parallel across a supply of p.d. \(V\).
They are connected between the same two points, so the p.d. across each capacitor is the same, \(V\).
Charge is conserved, so the total charge stored is the sum of the charges on the individual capacitors: \(Q = Q_1 + Q_2 + Q_3 + \dots\)
Use \(Q = CV\) for each, and for a single capacitor \(C\) that could replace them all: \(CV = C_1V + C_2V + C_3V + \dots\)
The p.d. \(V\) is the same in every term, so divide by \(V\):
\[C = C_1 + C_2 + C_3 + \dots\]
:::

:::proof examinable Capacitors in series
Capacitors \(C_1, C_2, C_3, \dots\) are connected in series across a supply of p.d. \(V\).
The charge that leaves the first plate of the chain is the charge that arrives at the last. The plates between are joined by wire, so their net charge stays zero, which means each capacitor holds the **same** charge \(Q\): \(+Q\) on one plate and \(-Q\) on the other.
By Kirchhoff's second law, the p.d.s add up to the supply p.d.: \(V = V_1 + V_2 + V_3 + \dots\)
Use \(V = Q/C\) for each, and for a single capacitor \(C\) that could replace them all: \(\dfrac{Q}{C} = \dfrac{Q}{C_1} + \dfrac{Q}{C_2} + \dfrac{Q}{C_3} + \dots\)
The charge \(Q\) is the same in every term, so divide by \(Q\):
\[\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots\]
:::

:::formula Combined capacitance
\[C = C_1 + C_2 + \dots \quad\text{(parallel)} \qquad\qquad \frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \dots \quad\text{(series)}\]
Both are on the data sheet. In parallel the **p.d. is shared by all**, and the charges add. In series the **charge is the same on all**, and the p.d.s add. For two capacitors in series, \(C = \dfrac{C_1 C_2}{C_1 + C_2}\). For \(n\) identical capacitors \(C\) in series, the total is \(C/n\).
:::

Two quick checks catch most errors. Capacitors in parallel give a total **larger** than any one of them, because you have effectively made bigger plates. Capacitors in series give a total **smaller** than the smallest one, because the gaps add up.

:::eg A \(2.0\,\mu\mathrm{F}\) and a \(3.0\,\mu\mathrm{F}\) capacitor are connected (a) in parallel and (b) in series. Find the combined capacitance each time. In (b), the combination is connected across a 10 V supply: find the p.d. across each capacitor.
(a) \(C = 2.0 + 3.0 = 5.0\,\mu\mathrm{F}\). [A1]
(b) \(\dfrac{1}{C} = \dfrac{1}{2.0} + \dfrac{1}{3.0} = 0.833\,\mu\mathrm{F}^{-1}\), so \(C = 1.2\,\mu\mathrm{F}\). [C1] [A1]
The charge is the same on both: \(Q = CV = 1.2 \times 10^{-6} \times 10 = 12\,\mu\mathrm{C}\). [C1]
\(V_{2.0} = Q/C = 12/2.0 = 6.0\,\mathrm{V}\) and \(V_{3.0} = 12/3.0 = 4.0\,\mathrm{V}\). The smaller capacitor takes the larger p.d., and \(6.0 + 4.0 = 10\,\mathrm{V}\). [A1]
:::

:::eg A \(6.0\,\mu\mathrm{F}\) capacitor is in series with a parallel pair of \(2.0\,\mu\mathrm{F}\) and \(4.0\,\mu\mathrm{F}\) capacitors, across a 12 V supply. Find the total capacitance and the charge on each capacitor.
Work from the inside out. The parallel pair is \(2.0 + 4.0 = 6.0\,\mu\mathrm{F}\). [C1]
That is in series with the \(6.0\,\mu\mathrm{F}\): \(\dfrac{6.0 \times 6.0}{6.0 + 6.0} = 3.0\,\mu\mathrm{F}\). [A1]
The charge from the supply: \(Q = CV = 3.0 \times 10^{-6} \times 12 = 36\,\mu\mathrm{C}\). This is the charge on the \(6.0\,\mu\mathrm{F}\) capacitor, and it is the charge that leaves the supply and shares between the pair. [C1]
The p.d. across the pair is \(36/6.0 = 6.0\,\mathrm{V}\). So the \(2.0\,\mu\mathrm{F}\) holds \(2.0 \times 6.0 = 12\,\mu\mathrm{C}\) and the \(4.0\,\mu\mathrm{F}\) holds \(4.0 \times 6.0 = 24\,\mu\mathrm{C}\). [A1]
**Check:** \(12 + 24 = 36\,\mu\mathrm{C}\), the charge that arrived at the pair.
:::

:::warn The rules are the other way round from resistors
For resistors, series resistances add. For capacitors it is the **parallel** capacitances that add. A common slip is to use the series formula for capacitors that are in parallel. Check with the size test: a parallel combination must be bigger than every capacitor in it, and a series combination smaller.
:::

## Energy stored in a capacitor

A charged capacitor stores energy. You can see where it comes from by charging one. The first small amount of charge moved from one plate to the other meets almost no opposing p.d. The more charge that is already there, the larger the p.d. that the next charge must be pushed against, so the p.d. rises steadily as the charge builds up. Plotting p.d. against charge gives a straight line through the origin, because \(V = Q/C\) has a constant \(C\).

:::plot The p.d. across a \(0.50\,\mathrm{mF}\) capacitor against the charge stored. The shaded area is the energy stored when the capacitor holds 6.0 mC at 12 V.
--f "2*x+0*sqrt(6-x)" --x 0 7 --y 0 14 --shade "0,0,6" --pt "6,12,(6.0 mC, 12 V)@nw" --xlabel "Q / mC" --ylabel "V / V"
:::

The gradient of this graph is \(V/Q = 1/C\). The **area under the graph** is the work done in charging the capacitor, and so the energy stored.

:::proof examinable Energy stored in a capacitor
Suppose the capacitor already holds charge \(q\), so the p.d. across it is \(v = q/C\).
Moving a further small charge \(\delta q\) from the negative plate to the positive plate needs work \(\delta W = v\,\delta q\), since p.d. is work per unit charge.
This is the area of a thin strip of height \(v\) and width \(\delta q\) on the V–Q graph.
Charging from zero to \(Q\) adds up all the strips, so the total work is the area under the graph from \(0\) to \(Q\).
The graph is a straight line through the origin, so this area is a triangle: \(W = \tfrac12 \times Q \times V\).
The work done is stored as electric potential energy in the capacitor.
:::

:::formula Energy stored in a capacitor
\[W = \tfrac12 QV = \tfrac12 CV^{2} = \frac{Q^{2}}{2C}\]
\(W\): energy stored (J) · \(Q\): charge (C) · \(V\): p.d. (V) · \(C\): capacitance (F). Use \(\tfrac12 CV^2\) when you know \(C\) and \(V\), and \(Q^2/2C\) when the charge is fixed.
:::

The factor \(\tfrac12\) is the average p.d. during charging: the p.d. rises from zero to \(V\), so on average the charge was moved against \(\tfrac12 V\). Do not use \(W = QV\), which would be the energy to move all the charge through the final p.d.

:::eg Find the energy stored in the \(470\,\mu\mathrm{F}\) capacitor charged to 12 V in the earlier example.
\[W = \tfrac12 CV^{2} = \tfrac12 \times 470 \times 10^{-6} \times 12^{2}\] [C1]
\[W = 3.38 \times 10^{-2}\,\mathrm{J}\] [A1]
Check with the other forms: with \(Q = 5.64 \times 10^{-3}\,\mathrm{C}\), \(\tfrac12 QV = \tfrac12 \times 5.64 \times 10^{-3} \times 12 = 3.38 \times 10^{-2}\,\mathrm{J}\) and \(Q^2/2C = (5.64 \times 10^{-3})^2 / (2 \times 470 \times 10^{-6}) = 3.38 \times 10^{-2}\,\mathrm{J}\). They agree.
:::

:::eg The flash unit of a camera uses a \(120\,\mu\mathrm{F}\) capacitor charged to 300 V. The energy is released in a flash lasting 1.0 ms. Find the energy stored and the mean power of the flash.
\[W = \tfrac12 CV^{2} = \tfrac12 \times 120 \times 10^{-6} \times 300^{2}\] [C1]
\[W = 5.4\,\mathrm{J}\] [A1]
\[P = \frac{W}{t} = \frac{5.4}{1.0 \times 10^{-3}} = 5.4 \times 10^{3}\,\mathrm{W}\] [A1]
A small battery takes several seconds to charge the capacitor, but the capacitor releases the same energy about a thousand times faster. That is the whole point of using one: it converts a slow, steady supply into a short, powerful burst.
:::

:::eg A \(2.0\,\mu\mathrm{F}\) capacitor is charged to 6.0 V and then disconnected from the supply. It is connected in parallel with an uncharged \(4.0\,\mu\mathrm{F}\) capacitor. Find the final p.d. and the energy lost.
The charge is conserved: \(Q = CV = 2.0 \times 6.0 = 12\,\mu\mathrm{C}\) shared between the two. [C1]
The capacitors are now in parallel, so \(C = 2.0 + 4.0 = 6.0\,\mu\mathrm{F}\) and \(V = Q/C = 12/6.0 = 2.0\,\mathrm{V}\). [A1]
Energy before: \(\tfrac12 \times 2.0 \times 10^{-6} \times 6.0^{2} = 36\,\mu\mathrm{J}\). Energy after: \(\tfrac12 \times 6.0 \times 10^{-6} \times 2.0^{2} = 12\,\mu\mathrm{J}\). [C1]
So \(24\,\mu\mathrm{J}\), two thirds of the energy, is lost. [A1] It is converted to thermal energy in the connecting wires (and some is radiated) as the charge flows from one capacitor to the other.
:::

:::key Half the energy is wasted when you charge through a resistor
When a supply of p.d. \(V\) charges a capacitor through a resistor, the supply transfers energy \(QV = CV^2\). The capacitor stores only \(\tfrac12 CV^2\). The other half is dissipated in the resistor as thermal energy, **whatever the value of \(R\)**. For the \(470\,\mu\mathrm{F}\) capacitor at 12 V: the supply transfers \(470 \times 10^{-6} \times 144 = 6.77 \times 10^{-2}\,\mathrm{J}\), the capacitor stores \(3.38 \times 10^{-2}\,\mathrm{J}\), and \(3.38 \times 10^{-2}\,\mathrm{J}\) heats the resistor and wires.
:::

Capacitors are used wherever a store of energy has to be filled slowly and emptied quickly or briefly: the flash in a camera, the defibrillator in an ambulance, the back-up supply that keeps a computer's memory alive for a few seconds when the power fails, and the many small capacitors that smooth the p.d. in a power supply (see [Alternating currents](#phys.ac)).

## Discharging a capacitor through a resistor

Connect a charged capacitor across a resistor, as with the switch at position 2 in the circuit above. Charge flows round the circuit from the positive plate through the resistor to the negative plate, and the capacitor loses charge. Here is the key idea. At any moment the p.d. across the resistor equals the p.d. across the capacitor, so the current is \(I = V/R\), which is proportional to the p.d. And the p.d. \(V = Q/C\) is itself proportional to the charge left. So the **current, which is the rate at which charge leaves, is proportional to the charge that remains**.

When the capacitor is full, charge leaves quickly. As it empties, the p.d. falls, the current falls, and charge leaves more and more slowly. This "rate proportional to what is left" is the signature of **exponential decay**.

:::proof Why the charge decays exponentially
The p.d. across the resistor equals the p.d. across the capacitor, so \(I = \dfrac{V}{R} = \dfrac{Q}{RC}\).
The current is the rate at which the charge on the capacitor falls: \(I = -\dfrac{dQ}{dt}\).
So \(\dfrac{dQ}{dt} = -\dfrac{Q}{RC}\). The rate of change of \(Q\) is proportional to \(Q\), with a negative constant.
The solution of this equation, with \(Q = Q_0\) at \(t = 0\), is \(Q = Q_0\,e^{-t/RC}\).
Since \(V = Q/C\) and \(I = V/R\) are both proportional to \(Q\), the p.d. and the current decay in the same way.
:::

:::formula Discharge of a capacitor
\[x = x_0\,e^{-t/RC}\]
\(x\) can be the charge \(Q\), the p.d. \(V\) across the capacitor or the current \(I\); \(x_0\) is its value at \(t = 0\); \(R\) is the resistance in the discharge circuit (Ω); \(C\) is the capacitance (F); \(t\) is the time since discharge began (s). The equation is on the data sheet.
:::

The combination \(RC\) has the dimension of time. In units, \(\Omega \times \mathrm{F} = (\mathrm{V\,A^{-1}}) \times (\mathrm{C\,V^{-1}}) = \mathrm{C\,A^{-1}} = \mathrm{s}\). It is so important that it has its own name.

:::def The time constant
The time constant \(\tau = RC\) is the time taken for the charge on the capacitor (or the p.d. across it, or the current) to fall to \(1/e\), about 37%, of its initial value during discharge.
:::

Put \(t = RC\) into the equation and you get \(x = x_0 e^{-1} = 0.37\,x_0\). That confirms the definition. Then \(e^{-t/\tau}\) tells you the fraction left after any number of time constants.

| Time | Fraction of initial value left |
|---|---|
| \(\tau\) | \(e^{-1} = 0.368\) (37%) |
| \(2\tau\) | \(e^{-2} = 0.135\) (14%) |
| \(3\tau\) | \(e^{-3} = 0.0498\) (5.0%) |
| \(5\tau\) | \(e^{-5} = 0.00674\) (under 1%) |

After about five time constants the capacitor is, for practical purposes, discharged. A larger \(R\) or a larger \(C\) makes the discharge slower, because a larger \(R\) cuts the current and a larger \(C\) holds more charge to get rid of.

:::plot Discharge of a capacitor: the charge, p.d. or current as a fraction of its initial value, against time in units of the time constant. After one time constant it has fallen to 37% of its starting value.
--f "exp(-x)+0*sqrt(5-x)" --x 0 5.8 --y 0 1.15 --pt "1,0.368,(τ, 0.37 V₀)@ne" --vline 1 --hline 0.368 --xlabel "t / τ" --ylabel "V / V₀"
:::

The curve has the same shape for \(Q\), \(V\) and \(I\). On a charge–time graph, the **gradient** at any instant is minus the current, \(I = -\mathrm{d}Q/\mathrm{d}t\), so the steep start of the curve is where the current is largest. The current starts at \(I_0 = V_0/R\), where \(V_0\) is the starting p.d., and decays by the same factor. The **area under the current–time graph** is the charge that flowed, so it equals the initial charge \(Q_0\). This gives a useful check: since \(I_0 = V_0/R\) and \(\tau = RC\), the area under an exponential curve from \(t=0\) to infinity is \(I_0\tau = (V_0/R) \times RC = CV_0 = Q_0\).

:::eg A \(100\,\mu\mathrm{F}\) capacitor charged to 9.0 V discharges through a \(50\,\mathrm{k\Omega}\) resistor. Find the time constant, the initial current and the p.d. after 3.0 s.
\[\tau = RC = 50 \times 10^{3} \times 100 \times 10^{-6} = 5.0\,\mathrm{s}\] [C1] [A1]
Initial current: \(I_0 = V_0/R = 9.0/(50 \times 10^{3}) = 1.8 \times 10^{-4}\,\mathrm{A}\) (180 µA). [A1]
After 3.0 s: \(V = V_0 e^{-t/RC} = 9.0\,e^{-3.0/5.0} = 9.0 \times 0.549\) [C1] \(= 4.9\,\mathrm{V}\). [A1]
The current after 3.0 s is also \(0.549\) of its initial value, \(98.8\,\mu\mathrm{A}\). You can check it with \(I = V/R = 4.94/(50 \times 10^{3})\).
:::

:::eg For the capacitor in the last example, find (a) the time for the p.d. to fall to 2.0 V and (b) the time for the p.d. to halve.
(a) Rearrange \(V = V_0 e^{-t/RC}\): \(\dfrac{V}{V_0} = e^{-t/RC}\), so \(t = RC \ln\dfrac{V_0}{V}\). [C1]
\[t = 5.0 \times \ln\frac{9.0}{2.0} = 5.0 \times 1.504 = 7.5\,\mathrm{s}\] [A1]
(b) Halving means \(V/V_0 = \tfrac12\): \(t = RC \ln 2 = 0.693 \times 5.0 = 3.5\,\mathrm{s}\). [A1]
This \(0.693\,RC\) is the **half-life** of the discharge, the time for any of \(Q\), \(V\) or \(I\) to halve. It is not the same as the time constant: \(t_{1/2} = 0.693\,RC\), while \(\tau = RC\).
:::

### Reading a discharge graph

The syllabus asks you to analyse graphs of \(V\), \(Q\) and \(I\) against time. You can find \(\tau\) from the curve in two ways: read off the time at which the value has fallen to 37% of its starting value, or read the time at which it has fallen to 50% (the half-life) and divide by 0.693.

:::plot The p.d. across a capacitor discharging through a \(100\,\mathrm{k\Omega}\) resistor.
--f "6*exp(-x/10)+0*sqrt(40-x)" --x 0 46 --y 0 8 --pt "0,6,(0, 6.0 V)@ne" --pt "10,2.207,(10 s, 2.2 V)@ne" --xlabel "t / s" --ylabel "V / V"
:::

:::eg Use the graph above to find the time constant of the discharge and the capacitance.
The initial p.d. is 6.0 V. One time constant is when the p.d. has fallen to \(6.0/e = 2.2\,\mathrm{V}\), and the graph shows this at \(t = 10\,\mathrm{s}\), so \(\tau = 10\,\mathrm{s}\). [B1]
As a check, the p.d. halves to 3.0 V at \(t = 6.9\,\mathrm{s}\), and \(\tau = t_{1/2}/0.693 = 6.9/0.693 = 10\,\mathrm{s}\). [C1]
\[C = \frac{\tau}{R} = \frac{10}{100 \times 10^{3}} = 1.0 \times 10^{-4}\,\mathrm{F} = 100\,\mu\mathrm{F}\] [A1]
:::

### A straight line from a curve: ln V against t

An exponential curve is hard to analyse by eye. Take natural logarithms of \(V = V_0 e^{-t/RC}\) and the equation becomes the equation of a straight line:
\[\ln V = \ln V_0 - \frac{1}{RC}\,t\]
Compare with \(y = mx + c\): a graph of \(\ln V\) (on the \(y\)-axis) against \(t\) (on the \(x\)-axis) is a straight line with **gradient \(-1/RC\)** and \(y\)-intercept \(\ln V_0\). Measure the gradient, and \(RC = -1/\text{gradient}\).

:::plot A graph of ln V against t for a capacitor discharging from 9.0 V with a time constant of 5.0 s. The gradient is −1/RC = −0.20 s⁻¹.
--f "log(9)-0.2*x+0*sqrt(10-x)" --x 0 13 --y 0 3 --pt "0,2.197,(0, 2.20)@ne" --pt "5,1.197,(5.0 s, 1.20)@ne" --xlabel "t / s" --ylabel "ln (V / V)"
:::

(The quantity inside a logarithm has no unit, so the axis is \(\ln(V/\mathrm{V})\): the log of the numerical value of the p.d. in volts.) A straight-line graph is a far better test of the exponential law than a curve is, because any systematic departure from a straight line is easy to see.

:::lab Measuring the time constant of an RC circuit
:::steps
1. Connect a capacitor (for example \(1000\,\mu\mathrm{F}\)), a resistor (for example \(47\,\mathrm{k\Omega}\), so that \(RC\) is about 47 s) and a switch. Charge the capacitor from a d.c. supply, then connect a voltmeter across the capacitor. Use a digital voltmeter whose resistance (typically \(10\,\mathrm{M\Omega}\)) is far larger than \(R\).
2. Move the switch so the capacitor discharges through the resistor, and start a stopwatch at the same moment. Record the voltmeter reading every 10 s for at least 8 readings, until the p.d. is a small fraction of its start. A data logger gives more points and removes the reaction-time error.
3. Calculate \(\ln V\) for each reading and plot \(\ln V\) against \(t\), with the line of best fit through the points.
4. Find the gradient with a large triangle. The time constant is \(RC = -1/\text{gradient}\), and \(C = \tau/R\). Compare with the marked values of \(R\) and \(C\) (capacitors often have a tolerance of 20%).
5. Repeat for a different \(R\), and check that the time constant is proportional to \(R\).
:::
Keep the voltmeter's resistance in mind. It is in parallel with the capacitor, so it provides a second path for discharge. If its resistance is not much larger than \(R\), the measured time constant will be too small. The method and its analysis are the sort of task examined in [Planning, analysis and evaluation](#phys.planning).
:::

Now experiment with the widget. Change \(R\) and \(C\) and watch the curve stretch, then switch to the **ln V** tab and watch the gradient.

:::html
<div class="widget" data-w="phys-rc" data-c="100" data-r="50" data-v="9"></div>
:::

:::exam Which quantity is which
The same equation \(x = x_0 e^{-t/RC}\) works for \(Q\), \(V\) and \(I\) on a **discharging** capacitor, so the time constant read from any of the three graphs is the same. Always convert to base units first: \(\mu\mathrm{F} \to 10^{-6}\,\mathrm{F}\), \(\mathrm{k\Omega} \to 10^{3}\,\Omega\). Then \(RC\) comes out in seconds and you can use \(t\) in seconds. In a question that asks for the energy, remember that energy is proportional to \(V^2\), so it falls by a factor of \(e^{-2}\) in one time constant, not \(e^{-1}\).
:::

For comparison only, when a capacitor **charges** through a resistor the p.d. across it rises the other way, starting at zero and approaching the supply p.d.

:::plot Charging a capacitor through a resistor: the p.d. across the capacitor as a fraction of the supply p.d. The curve is the mirror image of the discharge curve. You do not need the equation for this course.
--f "1-exp(-x)" --x 0 5 --y 0 1.15 --xlabel "t / τ" --ylabel "V / V₀"
:::

:::board
AQA also covers charging a capacitor through a resistor, with \(Q = Q_0(1 - e^{-t/RC})\). Cambridge asks only for discharge through a resistor, as above, and for the definitions and formulae in this chapter.
:::

:::eg Spot the error: A \(100\,\mu\mathrm{F}\) capacitor is charged to 12 V and discharged through a \(20\,\mathrm{k\Omega}\) resistor. Calculate the p.d. across the capacitor 3.0 ms after discharge begins.
A student wrote this answer.

Line 1: \(RC = 20 \times 10^{3} \times 100 \times 10^{-6} = 2.0\,\mathrm{s}\)
Line 2: \(V = 12\,e^{-3.0/2.0} = 12 \times 0.223\)
Line 3: \(V = 2.7\,\mathrm{V}\)

Line 1 is correct, and the formula in line 2 is the right one. [C1] **Line 2 is wrong: \(t\) must be in seconds, so \(t = 3.0 \times 10^{-3}\,\mathrm{s}\), not 3.0.** The answer mark is lost. [A0]

Correct working: \(V = 12\,e^{-0.0030/2.0} = 12 \times 0.9985 = 12\,\mathrm{V}\). [A1]

Check: 3.0 ms is a tiny fraction of a time constant of 2.0 s, so the capacitor has hardly begun to discharge. A fall from 12 V to 2.7 V in 3 ms should have looked wrong at once.
:::

:::try Start easy, finish at exam standard
Q: Find the charge on a \(220\,\mu\mathrm{F}\) capacitor when the p.d. across it is 9.0 V.
A: \(Q = CV = 220 \times 10^{-6} \times 9.0 = 1.98 \times 10^{-3}\,\mathrm{C}\), about 2.0 mC.
Q: A \(4.7\,\mu\mathrm{F}\) capacitor holds a charge of \(94\,\mu\mathrm{C}\). What is the p.d. across it?
A: \(V = Q/C = 94 \times 10^{-6} / (4.7 \times 10^{-6}) = 20\,\mathrm{V}\).
Q: Find the combined capacitance of \(6.0\,\mu\mathrm{F}\) and \(3.0\,\mu\mathrm{F}\) capacitors (a) in series and (b) in parallel.
A: (a) \(\dfrac{6.0 \times 3.0}{6.0 + 3.0} = 2.0\,\mu\mathrm{F}\). (b) \(6.0 + 3.0 = 9.0\,\mu\mathrm{F}\).
Q: Find the energy stored in a \(2200\,\mu\mathrm{F}\) capacitor charged to 16 V.
A: \(W = \tfrac12 CV^2 = \tfrac12 \times 2200 \times 10^{-6} \times 16^2 = 0.28\,\mathrm{J}\).
Q: Find the time constant of a \(4.7\,\mu\mathrm{F}\) capacitor discharging through a \(100\,\mathrm{k\Omega}\) resistor.
A: \(\tau = RC = 100 \times 10^{3} \times 4.7 \times 10^{-6} = 0.47\,\mathrm{s}\).
Q: What fraction of its initial charge is left on a discharging capacitor after two time constants?
A: \(e^{-2} = 0.135\), so about 14% remains.
Q: A \(220\,\mu\mathrm{F}\) capacitor charged to 6.0 V discharges through a \(10\,\mathrm{k\Omega}\) resistor. What is the p.d. after 2.2 s?
A: \(\tau = 10 \times 10^{3} \times 220 \times 10^{-6} = 2.2\,\mathrm{s}\), so after one time constant \(V = 6.0/e = 2.2\,\mathrm{V}\).
Q: A student says that "a charged capacitor has a charge of \(Q\) stored on it". Explain what is wrong with this statement.
A: The capacitor has \(+Q\) on one plate and \(-Q\) on the other, so its net charge is zero. What it stores is energy (and it stores charge \(Q\) separated on its plates).
Q: A \(10\,\mu\mathrm{F}\) capacitor is charged to 20 V, and then connected across an uncharged \(10\,\mu\mathrm{F}\) capacitor. Find the final p.d. and the fraction of the energy lost.
A: The charge \(200\,\mu\mathrm{C}\) is shared between \(20\,\mu\mathrm{F}\), so \(V = 200/20 = 10\,\mathrm{V}\). Energy before \(= \tfrac12 \times 10 \times 10^{-6} \times 400 = 2.0 \times 10^{-3}\,\mathrm{J}\). After: \(\tfrac12 \times 20 \times 10^{-6} \times 100 = 1.0 \times 10^{-3}\,\mathrm{J}\). Half the energy is lost.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define capacitance.
A: The charge stored (on one plate) per unit potential difference [B1] between the plates (or across the capacitor). [B1]
Q: [3 marks] ★ Derive the formula for the combined capacitance \(C\) of capacitors \(C_1\) and \(C_2\) connected in parallel.
A: The p.d. \(V\) is the same across each capacitor. [B1] The total charge is the sum: \(Q = Q_1 + Q_2\), so \(CV = C_1V + C_2V\). [B1] Dividing by \(V\): \(C = C_1 + C_2\). [B1]
Q: [3 marks] ★★ Sketch a graph of p.d. against charge for a capacitor and use it to show that the energy stored is \(\tfrac12 QV\).
A: The graph is a straight line through the origin (\(V \propto Q\)). [B1] The work done in moving a small charge \(\delta Q\) at p.d. \(V\) is \(V\,\delta Q\), the area of a strip, so the total energy stored is the area under the graph. [B1] The area is a triangle, \(\tfrac12 \times Q \times V\). [B1]
Q: [4 marks] ★★ A \(12\,\mu\mathrm{F}\) capacitor is in series with a parallel pair of \(4.0\,\mu\mathrm{F}\) and \(8.0\,\mu\mathrm{F}\) capacitors. The combination is connected across a 24 V supply. (a) Calculate the total capacitance. (b) Calculate the charge on the \(4.0\,\mu\mathrm{F}\) capacitor.
A: (a) The parallel pair is \(4.0 + 8.0 = 12\,\mu\mathrm{F}\). [C1] In series with \(12\,\mu\mathrm{F}\): \(\dfrac{12 \times 12}{12 + 12} = 6.0\,\mu\mathrm{F}\). [A1] (b) The total charge is \(6.0 \times 24 = 144\,\mu\mathrm{C}\), so the p.d. across the pair is \(144/12 = 12\,\mathrm{V}\). [C1] The charge on the \(4.0\,\mu\mathrm{F}\) is \(4.0 \times 12 = 48\,\mu\mathrm{C}\). [A1]
Q: [3 marks] ★★ A \(2000\,\mu\mathrm{F}\) capacitor discharges through a resistor. The p.d. across it falls from 8.0 V at \(t = 0\) to 2.9 V at \(t = 4.0\,\mathrm{s}\). (a) Show that the time constant is about 4.0 s. (b) Calculate the resistance.
A: (a) After one time constant the p.d. is \(8.0/e = 2.9\,\mathrm{V}\) [C1], which is reached at 4.0 s, so \(\tau \approx 4.0\,\mathrm{s}\). [B1] (b) \(R = \tau/C = 4.0/(2000 \times 10^{-6}) = 2.0 \times 10^{3}\,\Omega\). [A1]
Q: [4 marks] ★★ A capacitor discharges through a \(22\,\mathrm{k\Omega}\) resistor. The current falls from 0.50 mA at \(t = 0\) to 0.18 mA at \(t = 2.2\,\mathrm{s}\). (a) Show that the time constant is about 2.2 s. (b) Calculate the capacitance. (c) Calculate the initial charge on the capacitor, and state which area on the current–time graph it equals.
A: (a) After one time constant the current is \(0.50/e = 0.18\,\mathrm{mA}\), which is reached at 2.2 s, so \(\tau \approx 2.2\,\mathrm{s}\). [B1] (b) \(C = \tau/R = 2.2/(22 \times 10^{3})\) [C1] \(= 1.0 \times 10^{-4}\,\mathrm{F}\) (\(100\,\mu\mathrm{F}\)). [A1] (c) \(Q_0 = I_0\tau = 0.50 \times 10^{-3} \times 2.2 = 1.1 \times 10^{-3}\,\mathrm{C}\), which equals the whole area under the current–time curve (all the charge that flows off the capacitor). [B1]
Q: [3 marks] ★★ A \(470\,\mu\mathrm{F}\) capacitor charged to 12 V discharges through a \(47\,\mathrm{k\Omega}\) resistor. Calculate the p.d. across the capacitor 30 s after discharge begins.
A: \(\tau = RC = 47 \times 10^{3} \times 470 \times 10^{-6} = 22\,\mathrm{s}\). [C1] \(V = 12\,e^{-30/22.09}\) [C1] \(= 3.1\,\mathrm{V}\). [A1]
Q: [7 marks] ★★★ A defibrillator uses a \(40\,\mu\mathrm{F}\) capacitor charged to 4.0 kV. When used, the capacitor discharges through the patient, whose resistance is \(50\,\Omega\). (a) Calculate the energy stored. (b) Calculate the time constant, and the time taken for the stored energy to halve. (c) Calculate the mean power delivered during the time the energy takes to halve.
H: The stored energy is proportional to \(V^2\). When does \(V^2\) fall to half?
H: The p.d. must fall to \(V_0/\sqrt{2}\). Solve \(e^{-t/\tau} = 1/\sqrt{2}\).
A: (a) \(W = \tfrac12 CV^2 = \tfrac12 \times 40 \times 10^{-6} \times (4.0 \times 10^{3})^2\) [C1] \(= 320\,\mathrm{J}\). [A1] (b) \(\tau = RC = 50 \times 40 \times 10^{-6} = 2.0 \times 10^{-3}\,\mathrm{s}\) [C1]. The energy halves when the p.d. is \(V_0/\sqrt{2}\), so \(e^{-t/\tau} = 1/\sqrt{2}\) [M1], \(t = \tfrac12 \tau \ln 2 = 6.9 \times 10^{-4}\,\mathrm{s}\). [A1] (c) In this time 160 J is delivered, so \(P = 160/(6.93 \times 10^{-4})\) [C1] \(= 2.3 \times 10^{5}\,\mathrm{W}\). [A1]
Q: [7 marks] ★★★ A student discharges a capacitor through a resistor of resistance \(100 \pm 5\,\mathrm{k\Omega}\) and records the p.d. \(V\) across the capacitor at times \(t\). The readings are: 0 s, 10.0 V; 20 s, 6.7 V; 40 s, 4.5 V; 60 s, 3.0 V; 80 s, 2.0 V; 100 s, 1.35 V. (a) Show that a graph of \(\ln V\) against \(t\) should be a straight line, and state its gradient in terms of \(R\) and \(C\). (b) Use the first and last readings to find the gradient. (c) Calculate the capacitance, with its uncertainty from the uncertainty in \(R\).
H: Write \(V = V_0 e^{-t/RC}\) and take natural logarithms.
H: The percentage uncertainty in \(C\) comes from the percentage uncertainty in \(R\) (the gradient is taken as exact here).
A: (a) \(\ln V = \ln V_0 - \dfrac{1}{RC}\,t\), which is of the form \(y = mx + c\). [B1] The gradient is \(-\dfrac{1}{RC}\). [B1] (b) \(\ln 10.0 = 2.303\) and \(\ln 1.35 = 0.300\), so the gradient is \(\dfrac{0.300 - 2.303}{100 - 0}\) [C1] \(= -2.00 \times 10^{-2}\,\mathrm{s^{-1}}\). [A1] (c) \(C = \dfrac{1}{R \times |\text{gradient}|} = \dfrac{1}{1.00 \times 10^{5} \times 0.0200}\) [C1] \(= 5.0 \times 10^{-4}\,\mathrm{F}\). [A1] The percentage uncertainty in \(R\) is 5%, so \(C = (5.0 \pm 0.25) \times 10^{-4}\,\mathrm{F}\), that is \((500 \pm 25)\,\mu\mathrm{F}\). [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A \(4.0\,\mu\mathrm{F}\) capacitor is charged to 10 V and a \(6.0\,\mu\mathrm{F}\) capacitor is charged to 5.0 V. They are then connected together, positive plate to positive plate and negative to negative. (a) Find the final p.d. across each capacitor. (b) Find the energy lost. (c) Explain what happens to this energy. (d) Show that the time for the energy stored in a discharging capacitor to halve is half the time for its charge to halve.
H: The total charge is conserved, and the two capacitors end up in parallel.
H: For (d), the energy is proportional to \(Q^2\), so it halves when \(Q\) falls to \(Q_0/\sqrt{2}\).
A: (a) The charges are \(4.0 \times 10 = 40\,\mu\mathrm{C}\) and \(6.0 \times 5.0 = 30\,\mu\mathrm{C}\), so the total charge is \(70\,\mu\mathrm{C}\) (the like plates are joined, so the charges add). [C1] The capacitors are in parallel, so \(C = 10\,\mu\mathrm{F}\) and \(V = 70/10 = 7.0\,\mathrm{V}\). [A1] (b) With the capacitances in \(\mu\mathrm{F}\), the energies come out in \(\mu\mathrm{J}\). Before: \(\tfrac12 \times 4.0 \times 10^2 + \tfrac12 \times 6.0 \times 5.0^2 = 200 + 75 = 275\,\mu\mathrm{J}\). After: \(\tfrac12 \times 10 \times 7.0^2 = 245\,\mu\mathrm{J}\). [C1] Energy lost \(= 30\,\mu\mathrm{J}\). [A1] (c) It is dissipated as thermal energy in the connecting wires as the charge flows, and some may be radiated as electromagnetic waves. [B1] (d) The charge halves when \(e^{-t/\tau} = \tfrac12\), so \(t = \tau \ln 2\). [B1] The energy \(\tfrac12 Q^2/C\) halves when \(Q^2\) halves, that is \(Q = Q_0/\sqrt{2}\), so \(e^{-t/\tau} = 2^{-1/2}\) and \(t = \tfrac12 \tau \ln 2\), which is half the time for the charge to halve. [B1]
:::

:::quiz
? What is one farad equal to?
+ One coulomb per volt
- One volt per coulomb
- One joule per coulomb
- One coulomb per second
> Capacitance is charge per unit p.d., so \(1\,\mathrm{F} = 1\,\mathrm{C\,V^{-1}}\). One volt per coulomb is upside down, one joule per coulomb is a volt, and one coulomb per second is an ampere.
? A capacitor is connected to a 6.0 V battery and \(30\,\mu\mathrm{C}\) of charge is on its positive plate. What is the net charge on the capacitor?
+ Zero
- \(+30\,\mu\mathrm{C}\)
- \(+60\,\mu\mathrm{C}\)
- \(30\,\mu\mathrm{C}\) less than the battery supplied
> The negative plate carries \(-30\,\mu\mathrm{C}\), exactly cancelling the \(+30\,\mu\mathrm{C}\) on the other plate. The battery only moves charge from one plate to the other.
? Two identical capacitors, each of capacitance \(C\), are connected in series. What is their combined capacitance?
+ \(C/2\)
- \(2C\)
- \(C\)
- \(C^2\)
> In series, \(1/C_\text{total} = 1/C + 1/C = 2/C\), so \(C_\text{total} = C/2\). \(2C\) is the parallel answer.
? The p.d. across a capacitor is doubled. What happens to the energy stored?
+ It becomes four times larger.
- It doubles.
- It becomes half as large.
- It stays the same.
> \(W = \tfrac12 CV^2\) is proportional to \(V^2\), so doubling \(V\) multiplies the energy by four. The charge doubles, but the energy does not.
? A capacitor discharges through a resistor. About what fraction of the initial charge is left after three time constants?
+ 5%
- 37%
- 33%
- 10%
> After three time constants \(e^{-3} = 0.050\). 37% is the fraction left after one time constant. 33% divides 1 by 3 instead of calculating \(e^{-3}\), and 10% is a guess: always work out \(e^{-n}\) for \(n\) time constants.
? The resistance in a discharging circuit is doubled and the capacitance is unchanged. What happens to the time constant and to the initial current?
+ The time constant doubles and the initial current halves.
- The time constant doubles and the initial current doubles.
- The time constant halves and the initial current doubles.
- Both stay the same.
> \(\tau = RC\) doubles. The initial current \(I_0 = V_0/R\) halves, so the charge leaves more slowly, and the curve has the same shape stretched in time.
? A capacitor is charged by a supply through a resistor. How does the energy dissipated in the resistor compare with the energy stored?
+ They are equal, whatever the resistance.
- The resistor dissipates more energy if \(R\) is large.
- The resistor dissipates no energy once the capacitor is charged.
- The energy stored is twice the energy dissipated.
> The supply transfers \(CV^2\), the capacitor stores \(\tfrac12 CV^2\) and the rest, \(\tfrac12 CV^2\), is dissipated, independent of \(R\). A larger \(R\) only makes it happen more slowly.
? A graph of \(\ln V\) against \(t\) is plotted for a discharging capacitor. What does the gradient equal?
+ \(-1/RC\)
- \(RC\)
- \(-RC\)
- \(\ln V_0\)
> \(\ln V = \ln V_0 - t/RC\), so the gradient is \(-1/RC\) and the intercept is \(\ln V_0\). The time constant is minus the reciprocal of the gradient.
:::

:::checklist What you can now do
- [ ] I can define capacitance and the farad, describe how a capacitor charges, and explain why its net charge is zero.
- [ ] I can recall and use \(C = Q/V\), and derive and use the capacitance of an isolated sphere, \(4\pi\varepsilon_0 r\).
- [ ] I can derive and use the formulae for capacitors in series and in parallel, and find the charge and p.d. on each capacitor in a network.
- [ ] I can find the energy stored from the area under a potential–charge graph, and use \(W = \tfrac12 QV = \tfrac12 CV^2\).
- [ ] I can explain why charging through a resistor wastes half the energy, and calculate the energy lost when charge is shared between capacitors.
- [ ] I can analyse graphs of \(V\), \(Q\) and \(I\) against time for a capacitor discharging through a resistor.
- [ ] I can define and use the time constant \(\tau = RC\) and the half-life \(0.693\,RC\).
- [ ] I can use \(x = x_0e^{-t/RC}\) for the charge, p.d. and current, and use a graph of \(\ln V\) against \(t\) to find \(RC\).
:::

:::recap
- Capacitance \(C = Q/V\): the charge on one plate per unit p.d. The farad is one coulomb per volt. A charged capacitor has zero net charge: \(+Q\) on one plate and \(-Q\) on the other.
- Isolated sphere: \(C = 4\pi\varepsilon_0 r\). Parallel plates: larger area, smaller gap and a good dielectric all increase \(C\).
- Parallel: \(C = C_1 + C_2 + \dots\) (same p.d.). Series: \(1/C = 1/C_1 + 1/C_2 + \dots\) (same charge).
- Energy stored: the area under the V–Q graph, \(W = \tfrac12 QV = \tfrac12 CV^2 = Q^2/2C\). Charging through a resistor wastes half the energy supplied.
- Discharge through a resistor: \(Q\), \(V\) and \(I\) all follow \(x = x_0e^{-t/RC}\). The time constant \(\tau = RC\) is the time to fall to \(1/e\) (37%); the half-life is \(0.693\,RC\).
- A graph of \(\ln V\) against \(t\) is a straight line of gradient \(-1/RC\). The stored energy halves in half the time that the charge takes to halve.
:::

:::links
- explore: [Capacitor Lab: Basics](https://phet.colorado.edu/en/simulations/capacitor-lab-basics) · PhET · change plate area, separation and voltage and watch the charge and energy
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the capacitance questions in real papers [unofficial]
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Magnetic fields](#phys.magnetic)
