@chapter phys.electricity
@title Electricity
@level as
@paper CAIE P1 · P2 · P3 (AS)
@time 6–8 hours
@summary Current as a flow of quantised charge and the drift-speed equation I = Anvq, potential difference and power, resistance and Ohm's law, the I–V characteristics of a wire, a filament lamp and a diode, resistivity, and the LDR and thermistor.

:::why
Every phone, car and power station is built on one idea: moving charge carries energy from where it is made to where it is used. This chapter gives you the quantities that describe that process (current, p.d., resistance, power) and the graphs that show how real components behave. [D.C. circuits](#phys.dc) then combines them, so everything you learn here is used on almost every Paper 1, 2 and 3 question about electricity.
:::

**Before you start**, you need the idea of power as energy per unit time from [Work, energy and power](#phys.energy), and unit prefixes and standard form from [Physical quantities, units and uncertainty](#phys.units).

:::try Warm-up
Q: A heater transfers 360 kJ of energy in 3.0 minutes. What is its power? (from [Work, energy and power](#phys.energy))
A: \(P = W/t = 360\,000/180 = 2.0 \times 10^{3}\,\mathrm{W}\), that is 2.0 kW. Change minutes into seconds before dividing.
Q: Write \(25\,\mathrm{mA}\) and \(4.7\,\mathrm{k\Omega}\) in base units, in standard form. (from [Physical quantities, units and uncertainty](#phys.units))
A: \(2.5 \times 10^{-2}\,\mathrm{A}\) and \(4.7 \times 10^{3}\,\Omega\).
Q: A wire has a diameter of \(0.50\,\mathrm{mm}\). Find the area of its circular cross-section in \(\mathrm{m^2}\). (from [Physical quantities, units and uncertainty](#phys.units))
A: The radius is \(0.25\,\mathrm{mm} = 2.5 \times 10^{-4}\,\mathrm{m}\), so \(A = \pi r^{2} = \pi \times (2.5 \times 10^{-4})^{2} = 1.96 \times 10^{-7}\,\mathrm{m^{2}}\).
:::

## Current: a flow of charge carriers

In a metal, each atom gives up one or more of its outer electrons. The atoms become fixed positive **ions** that sit in a regular lattice, and the electrons wander freely between them. These **free electrons** are the **charge carriers**. With no p.d. across the metal they move at random in all directions, so there is no net flow of charge. A p.d. across the wire adds a small, steady drift along the wire on top of the random motion, and that drift is the current.

Other substances have other carriers. In a salt solution, both positive and negative **ions** move, in opposite directions. In a spark or a flame, ions and free electrons carry the charge through the gas. In every case the idea is the same: an electric current is charge carriers moving.

:::def Electric current
The rate of flow of charge: \(I = \Delta Q/\Delta t\). It is measured in amperes (A).
:::

The direction you draw on a circuit diagram is the **conventional current**: the direction in which positive charge would move, from the positive terminal of a source round to the negative. This convention was chosen before electrons were discovered. In a metal the carriers are electrons, which are negative, so they actually move the other way. Both pictures give the same results, and in an exam you draw conventional current unless the question says otherwise.

:::warn Current is not used up
Charge is conserved, so the current that leaves a lamp is exactly the same as the current that enters it. What the lamp uses up is **energy**, which the charges carry in and leave behind as light and heat. If a question says "the current is used up in the lamp", it is wrong, and a mark scheme will say so.
:::

## Charge, the coulomb and quantisation

Rearranging \(I = \Delta Q/\Delta t\) for a steady current gives the charge that has passed.

:::def The coulomb
The coulomb (C) is the charge that passes a point when a current of 1 ampere flows for 1 second. So \(1\,\mathrm{C} = 1\,\mathrm{A\,s}\).
:::

:::formula Charge and current
\[Q = It\]
\(Q\): charge (C) · \(I\): current (A) · \(t\): time (s). Convert minutes and hours to seconds, and mA and µA to A, before you substitute.
:::

:::eg A steady current of 3.0 A flows through a heater for 5.0 minutes. Find the charge that passes, and the number of electrons.
Time in seconds: \(5.0 \times 60 = 300\,\mathrm{s}\). Then
\[Q = It = 3.0 \times 300 = 900\,\mathrm{C}\] [C1] [A1]
Each electron carries a charge of magnitude \(e = 1.60 \times 10^{-19}\,\mathrm{C}\), so the number of electrons is
\[N = \frac{Q}{e} = \frac{900}{1.60 \times 10^{-19}} = 5.6 \times 10^{21}\] [C1] [A1]
The unrounded value is \(5.625 \times 10^{21}\); the answer is given to 2 significant figures, like the data. An enormous number of electrons passes in a few minutes, which is why a current looks smooth even though charge comes in tiny lumps.
:::

:::eg In a lightning flash, 15 C of charge is transferred in 0.20 ms. Find the average current.
\[I = \frac{Q}{t} = \frac{15}{0.20 \times 10^{-3}} = 7.5 \times 10^{4}\,\mathrm{A}\]
That is 75 kA. The current is huge because the time is tiny. Always convert milliseconds to seconds before dividing.
:::

When the current changes, \(Q = It\) still holds for each short interval, so the charge is the **area under the current–time graph**. For a steady current the area is a rectangle, \(I \times t\); for a changing current, add up the areas of the simple shapes (or count squares).

:::plot The current in a motor as it starts: it rises steadily to 4.0 A in 10 s, then stays at 4.0 A. The charge that has passed is the area under the line.
--f "(0.4*x + 4 - abs(0.4*x - 4))/2" --x 0 16 --y 0 5.5 --pt "10,4,(10 s, 4.0 A)@n" --xlabel "t / s" --ylabel "I / A"
:::

:::eg Use the graph above to find the charge that passes in the first 15 s.
The area is a triangle for the first 10 s and a rectangle for the next 5 s:
\[Q = \tfrac12 \times 10 \times 4.0 + 5.0 \times 4.0\] [C1] \(= 20 + 20 = 40\,\mathrm{C}\). [A1]
The average current over the 15 s is \(40/15 = 2.7\,\mathrm{A}\), not the 4.0 A at the end: when the current varies, \(Q = It\) needs the average current.
:::

Charge comes in lumps. The smallest charge you can isolate is the charge of one electron or one proton, the **elementary charge** \(e = 1.60 \times 10^{-19}\,\mathrm{C}\). Every charge you can measure is a whole-number multiple of it. We say charge is **quantised**.

:::key Quantisation of charge
\[Q = ne \qquad (n = 0, \pm 1, \pm 2, \dots)\]
Any charge you can isolate is a whole number of times \(e\). (Quarks carry \(\pm\tfrac13 e\) and \(\pm\tfrac23 e\), but they are never found on their own: see [Particle physics](#phys.particles).)
:::

:::eg Which of these could be the charge on a tiny oil droplet: \(4.8 \times 10^{-19}\,\mathrm{C}\), \(6.4 \times 10^{-19}\,\mathrm{C}\) or \(2.4 \times 10^{-19}\,\mathrm{C}\)?
Divide each by \(e = 1.60 \times 10^{-19}\,\mathrm{C}\) and look for a whole number.
\[\frac{4.8}{1.60} = 3 \qquad \frac{6.4}{1.60} = 4 \qquad \frac{2.4}{1.60} = 1.5\]
The first two are 3 and 4 electron charges, so they are possible. The third would need one and a half electrons, so it is impossible. A calculation that gives a fraction of an electron has gone wrong.
:::

## Drift speed and I = Anvq

How fast do the carriers move? Their random thermal speeds in a metal are huge, around \(10^{5}\,\mathrm{m\,s^{-1}}\), but because they move in all directions they carry no net charge anywhere. The current comes from the tiny extra **drift velocity** \(v\) along the wire. We can link \(I\) to \(v\) by counting the charge in a short length of wire.

:::html
<figure class="fig"><svg viewBox="100 30 420 160" role="img" aria-label="A section of wire drawn as a cylinder of length l equal to v times t and cross-sectional area A. Eighteen dots inside represent charge carriers, which drift to the right at speed v. A dimension arrow below the cylinder shows its length."><rect class="fm s-mute sw1" x="120" y="70" width="320" height="70"/><path class="ln thin" d="M120 70A14 35 0 0 0 120 140"/><ellipse class="fp s-mute sw1" cx="440" cy="105" rx="14" ry="35"/><circle class="fi" cx="148" cy="88" r="3.5"/><circle class="fi" cx="196" cy="88" r="3.5"/><circle class="fi" cx="244" cy="88" r="3.5"/><circle class="fi" cx="292" cy="88" r="3.5"/><circle class="fi" cx="340" cy="88" r="3.5"/><circle class="fi" cx="388" cy="88" r="3.5"/><circle class="fi" cx="148" cy="105" r="3.5"/><circle class="fi" cx="196" cy="105" r="3.5"/><circle class="fi" cx="244" cy="105" r="3.5"/><circle class="fi" cx="292" cy="105" r="3.5"/><circle class="fi" cx="340" cy="105" r="3.5"/><circle class="fi" cx="388" cy="105" r="3.5"/><circle class="fi" cx="148" cy="122" r="3.5"/><circle class="fi" cx="196" cy="122" r="3.5"/><circle class="fi" cx="244" cy="122" r="3.5"/><circle class="fi" cx="292" cy="122" r="3.5"/><circle class="fi" cx="340" cy="122" r="3.5"/><circle class="fi" cx="388" cy="122" r="3.5"/><path class="c1" d="M180 52H280" marker-end="url(#ah-phys)"/><text class="tl ti ta" x="292" y="56">v</text><text class="tl" x="462" y="110">area A</text><path class="c1" d="M280 172H124" marker-end="url(#ah-phys)"/><path class="c1" d="M280 172H436" marker-end="url(#ah-phys)"/><text class="tl ti ta tc" x="280" y="162">l = vt</text></svg><figcaption>Every carrier inside the length l = vt reaches the right-hand face (area A) within time t. Each dot stands for a carrier of charge q, and there are n of them in every cubic metre.</figcaption></figure>
:::

:::proof Why I = Anvq
Let a wire have cross-sectional area \(A\) and \(n\) charge carriers per unit volume (the **number density**, in \(\mathrm{m^{-3}}\)), each with charge \(q\), drifting with speed \(v\).
In a time \(t\), every carrier within a distance \(vt\) of a cross-section reaches it and passes through.
Those carriers fill a volume \(Avt\).
The number of carriers in that volume is \(nAvt\).
The charge passing the cross-section is \(Q = nAvt \times q\).
The current is the charge per unit time: \(I = Q/t = nAvq\).
:::

:::formula Current and drift speed
\[I = Anvq\]
\(I\): current (A) · \(A\): cross-sectional area (\(\mathrm{m^2}\)) · \(n\): number density of charge carriers (\(\mathrm{m^{-3}}\)) · \(v\): mean drift speed (\(\mathrm{m\,s^{-1}}\)) · \(q\): charge on each carrier (C). For electrons, \(q = e = 1.60 \times 10^{-19}\,\mathrm{C}\).
:::

:::eg A copper wire of diameter 1.0 mm carries a current of 2.0 A. Copper has \(8.5 \times 10^{28}\) free electrons per cubic metre. Find the drift speed of the electrons.
Area: \(A = \pi r^{2} = \pi \times (0.50 \times 10^{-3})^{2} = 7.85 \times 10^{-7}\,\mathrm{m^{2}}\). [C1]
Rearrange \(I = Anvq\):
\[v = \frac{I}{Anq} = \frac{2.0}{7.85 \times 10^{-7} \times 8.5 \times 10^{28} \times 1.60 \times 10^{-19}} = 1.9 \times 10^{-4}\,\mathrm{m\,s^{-1}}\] [C1] [A1]
The electrons drift at under two tenths of a millimetre per second, slower than a snail. Keep the unrounded area in your calculator, and remember to use metres, not millimetres.
:::

If the drift is so slow, why does a lamp light the instant you press the switch? The electric field that pushes the electrons spreads along the circuit at close to the speed of light, and every free electron in the wire, including those already inside the filament, starts to drift at once.

:::analogy
A pipe full of water behaves in the same way. When you open the tap, water leaves the far end immediately, even though each drop travels slowly. The pipe was already full, and the push travels through the water almost instantly. A wire is already full of free electrons.
:::

:::eg Two wires of the same copper are joined in series. One has diameter 1.0 mm and the other 0.50 mm. Compare the drift speeds of the electrons in them.
The wires are in series, so the current is the same in both. [B1] The carriers are the same, so \(n\) and \(q\) are the same, and \(I = Anvq\) gives \(v \propto 1/A\).
The area is proportional to diameter squared. The thin wire has half the diameter, so a quarter of the area, and the electrons drift **4 times faster** in it. [A1]
Check with numbers: for 2.0 A the thick wire gives \(1.9 \times 10^{-4}\,\mathrm{m\,s^{-1}}\) (above) and the thin wire gives \(7.5 \times 10^{-4}\,\mathrm{m\,s^{-1}}\). The ratio is 4.
:::

:::tip Metals and semiconductors
A metal has a very large \(n\) (about \(10^{29}\,\mathrm{m^{-3}}\)). A semiconductor has far fewer free carriers, perhaps \(10^{22}\,\mathrm{m^{-3}}\) or less. For the same current in a wire of the same area, \(v \propto 1/n\), so each carrier in a semiconductor has to drift much faster. An insulator has almost no free carriers, so even a large p.d. produces almost no current.
:::

## Potential difference and energy

Carriers need energy to move through a component, and the p.d. tells you how much each coulomb gives up. The definition below is the one examiners expect, word for word.

:::def Potential difference (p.d.)
The potential difference across a component is the energy transferred per unit charge as charge passes through it, from electrical energy to other forms (thermal energy, light, kinetic energy, ...).
:::

:::def The volt
The volt (V) is one joule per coulomb: \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\). There is a p.d. of 1 V between two points if 1 J of energy is transferred when 1 C of charge passes between them.
:::

:::formula Potential difference and energy
\[V = \frac{W}{Q} \qquad\text{so}\qquad W = QV\]
\(V\): p.d. (V) · \(W\): energy transferred (J) · \(Q\): charge (C). The source that provides the energy has an **e.m.f.**, which is defined in [D.C. circuits](#phys.dc).
:::

:::eg An electron is accelerated from rest through a p.d. of 2.5 kV in a vacuum tube. Find the kinetic energy it gains and its final speed. Use \(m_e = 9.11 \times 10^{-31}\,\mathrm{kg}\).
The charge is \(e\) and the p.d. is 2500 V, so
\[W = QV = 1.60 \times 10^{-19} \times 2500 = 4.0 \times 10^{-16}\,\mathrm{J}\] [C1] [A1]
All of this becomes kinetic energy, \(\tfrac12 m v^{2} = W\):
\[v = \sqrt{\frac{2W}{m}} = \sqrt{\frac{2 \times 4.0 \times 10^{-16}}{9.11 \times 10^{-31}}} = 3.0 \times 10^{7}\,\mathrm{m\,s^{-1}}\] [C1] [A1]
This is one tenth of the speed of light, so the non-relativistic formula is a fair approximation.
:::

## Electrical power and energy

A source or component transfers energy at a rate given by the power. Combine \(P = W/t\) with \(W = QV\) and \(Q = It\):

:::proof Three forms of the power equation
\(P = W/t\), and \(W = QV\), so \(P = QV/t\).
Charge per unit time is the current, \(Q/t = I\), so \(P = VI\).
For a resistor, \(V = IR\). Substituting for \(V\) gives \(P = (IR) \times I = I^{2}R\).
Substituting for \(I = V/R\) instead gives \(P = V \times V/R = V^{2}/R\).
:::

:::formula Electrical power
\[P = VI = I^{2}R = \frac{V^{2}}{R}\]
\(P\): power (W) · \(V\): p.d. **across the component** (V) · \(I\): current in it (A) · \(R\): its resistance (\(\Omega\)). Use \(I^{2}R\) when the current is known (series circuits) and \(V^{2}/R\) when the p.d. is known (parallel circuits and mains).
:::

:::eg A kettle is rated 2.0 kW on a 230 V supply. Find (a) its current, (b) its resistance, (c) the energy it transfers in 3.0 minutes.
(a) \(I = \dfrac{P}{V} = \dfrac{2000}{230} = 8.7\,\mathrm{A}\) [C1] [A1]
(b) \(R = \dfrac{V}{I} = \dfrac{230}{8.696} = 26\,\Omega\) [A1]. Check with \(V^{2}/P = 230^{2}/2000 = 26.45\,\Omega\).
(c) \(W = Pt = 2000 \times 180 = 3.6 \times 10^{5}\,\mathrm{J}\) [A1]
In (b), use the unrounded current, not 8.7 A, so that both methods agree.
:::

:::eg A lamp is marked "12 V, 36 W". Find the current and the resistance at normal brightness. Why would its resistance be much lower if you measured it cold?
\[I = \frac{P}{V} = \frac{36}{12} = 3.0\,\mathrm{A} \qquad R = \frac{V}{I} = \frac{12}{3.0} = 4.0\,\Omega\]
The glowing filament is at about 2500 °C or more. The resistance of a metal rises with temperature, so a cold filament has a much smaller resistance. Suppose it were 0.40 Ω when cold: at switch-on the current would be \(12/0.40 = 30\,\mathrm{A}\), ten times the normal 3.0 A. This surge is why lamps usually fail at the moment they are switched on.
:::

Electricity companies sell **energy**, not power, and measure it in kilowatt-hours.

:::def The kilowatt-hour (kW h)
The energy transferred by a device of power 1 kW in a time of 1 hour: \(1\,\mathrm{kW\,h} = 1000 \times 3600 = 3.6 \times 10^{6}\,\mathrm{J}\).
:::

:::eg A 3.0 kW heater is on for 5.0 hours. Electricity costs 30 p per kW h. Find the energy used in kW h and in joules, and the cost.
Energy in kW h: \(3.0 \times 5.0 = 15\,\mathrm{kW\,h}\).
Cost: \(15 \times 30 = 450\,\mathrm{p} = £4.50\).
In joules: \(15 \times 3.6 \times 10^{6} = 5.4 \times 10^{7}\,\mathrm{J}\).
When the power is in kW and the time in hours, the energy comes out directly in kW h. Do not convert to joules unless asked.
:::

:::warn Which V goes in P = V²/R?
The V in \(V^{2}/R\) is the p.d. across that resistor, not the supply p.d. In a series circuit the supply p.d. is shared, so using it for one resistor over-estimates the power. Also remember that at constant resistance, doubling the p.d. makes the power four times bigger.
:::

## Resistance and Ohm's law

For the same p.d., a thin wire passes less current than a thick one. We measure how hard a component makes it for current to flow with its **resistance**.

:::def Resistance
The resistance of a component is the ratio of the potential difference across it to the current in it: \(R = V/I\).
:::

:::def The ohm
The ohm (\(\Omega\)) is one volt per ampere: \(1\,\Omega = 1\,\mathrm{V\,A^{-1}}\).
:::

:::formula Resistance
\[R = \frac{V}{I} \qquad\text{so}\qquad V = IR\]
\(R\): resistance (\(\Omega\)) · \(V\): p.d. across the component (V) · \(I\): current in it (A).
:::

:::eg The p.d. across a component is 6.0 V when the current in it is 0.24 A. Find its resistance. What current flows if the p.d. is changed to 4.5 V and the component stays ohmic?
\[R = \frac{V}{I} = \frac{6.0}{0.24} = 25\,\Omega\]
For an ohmic component \(R\) stays the same, so \(I = V/R = 4.5/25 = 0.18\,\mathrm{A}\). Equivalently, the current is proportional to the p.d., and \(4.5/6.0 = 0.75\) of \(0.24\,\mathrm{A}\) is \(0.18\,\mathrm{A}\).
:::

Some components keep the same resistance whatever the p.d.; others do not. Ohm's law describes the simplest case.

:::def Ohm's law
The current in a metallic conductor is directly proportional to the potential difference across it, provided its temperature (and other physical conditions) remain constant.
:::

A component that obeys Ohm's law is called **ohmic**. Its \(I\)–\(V\) graph is a straight line through the origin, and its resistance is the same at every p.d. A filament lamp and a diode are **non-ohmic**, but \(R = V/I\) is still true for them, point by point.

:::warn Resistance is V/I, not the gradient
For a non-ohmic component, the resistance at a point on the \(I\)–\(V\) graph is the \(V\) value divided by the \(I\) value **at that point**. It is not \(1/\)gradient of the curve there. On an \(I\)–\(V\) graph a steeper line means a **smaller** resistance, so the resistance is the reciprocal of the gradient of the line from the origin to the point, never of the tangent. The widget in the next section shows the difference.
:::

## I–V characteristics

An \(I\)–\(V\) **characteristic** is a graph of current against p.d. for a component, including negative values (the supply reversed). Its shape shows how the component's resistance changes.

:::html
<figure class="fig wide"><svg viewBox="10 14 640 200" role="img" aria-label="Three I-V graphs with axes through the origin. Left: a metal wire at constant temperature gives a straight line through the origin. Middle: a filament lamp gives a symmetrical S-shaped curve whose gradient decreases as the p.d. increases in either direction. Right: a semiconductor diode gives almost no current for negative p.d. and for small positive p.d., then the current rises very steeply above about 0.6 volts."><path class="ax" d="M22 100H190M106 22V178"/><path class="c1" d="M36 160L176 40"/><text class="tl" x="114" y="32">I</text><text class="tl" x="196" y="104">V</text><text class="tl tc" x="106" y="198">Metal wire</text><path class="ax" d="M242 100H410M326 22V178"/><path class="c1" d="M256 162L262.8 158.3L269.3 154.6L275.4 151L281.2 147.4L286.6 143.9L291.7 140.4L296.4 137L300.8 133.6L304.8 130.3L308.5 127L311.8 123.8L314.8 120.6L317.4 117.6L319.7 114.6L321.6 111.7L323.2 109L324.4 106.4L325.3 103.9L325.8 101.7L326 100L326.2 98.3L326.7 96.1L327.6 93.6L328.8 91L330.4 88.3L332.3 85.4L334.6 82.4L337.2 79.4L340.2 76.2L343.5 73L347.2 69.7L351.2 66.4L355.6 63L360.3 59.6L365.4 56.1L370.8 52.6L376.6 49L382.7 45.4L389.2 41.7L396 38"/><text class="tl" x="334" y="32">I</text><text class="tl" x="416" y="104">V</text><text class="tl tc" x="326" y="198">Filament lamp</text><path class="ax" d="M462 100H630M546 22V178"/><path class="c1" d="M476 103L546 100L551 100L556 100L561 100L566 100L571 99.8L576 99.5L581 99L586 98L591 96.4L596 93.5L601 88.5L606 79.8L611 64.5L616 38"/><text class="tl" x="554" y="32">I</text><text class="tl" x="636" y="104">V</text><text class="tl tc" x="506" y="128">reverse</text><text class="tl tc" x="586" y="128">forward</text><text class="tl tc" x="546" y="198">Semiconductor diode</text></svg><figcaption>I–V characteristics. The metal wire is at constant temperature. The lamp's line flattens as it gets hotter, and the diode conducts in one direction only, once the forward p.d. is above about 0.6 V.</figcaption></figure>
:::

### A metal conductor at constant temperature

The graph is a straight line through the origin, and the line is the same in the negative quadrant. Current is directly proportional to p.d., so \(R = V/I\) is constant: this is Ohm's law. If the wire is allowed to warm up, its resistance rises and the line curves, which is why the statement of the law needs "constant temperature".

### A filament lamp

The graph is an S-shape: steep near the origin, flattening as the p.d. increases in either direction. The gradient decreases, so the **resistance \(V/I\) increases with current**. The explanation is about temperature:

:::steps
1. A larger current means more energy is transferred to the filament each second, so its temperature rises (to over 2000 °C in normal use).
2. The positive ions of the metal lattice vibrate with a larger amplitude.
3. The free electrons collide with the ions more often, so they drift more slowly for the same p.d.
4. The current is smaller than Ohm's law would predict, so the resistance \(V/I\) is larger.
:::

The number of carriers hardly changes in a metal. It is the collision rate that does. The graph is symmetrical because the filament heats in the same way whichever way the current flows.

### A semiconductor diode

A diode lets current pass in one direction only. In the **forward** direction, almost no current flows until the p.d. reaches about 0.6 V (for a silicon diode), and above that the current rises steeply, so the resistance becomes very small. In the **reverse** direction, the current is almost zero for any p.d., so the resistance is extremely large. For this reason, a diode is used in the rectification of alternating current.

:::eg Estimate the resistance of a filament lamp from the readings 2.0 V, 0.13 A and 6.0 V, 0.25 A. Comment on the change.
At 2.0 V: \(R = V/I = 2.0/0.13 = 15\,\Omega\). [C1] [A1]
At 6.0 V: \(R = 6.0/0.25 = 24\,\Omega\). [A1]
The resistance rises by about 60% as the current almost doubles, because the filament becomes hotter. [B1]
:::

:::eg A diode in forward bias has a current of 2.0 mA at 0.60 V and 40 mA at 0.75 V. In reverse bias, at 5.0 V, the current is 0.10 µA. Find the resistance in each case.
Forward at 0.60 V: \(R = \dfrac{0.60}{2.0 \times 10^{-3}} = 300\,\Omega\).
Forward at 0.75 V: \(R = \dfrac{0.75}{40 \times 10^{-3}} = 19\,\Omega\) (unrounded 18.75).
Reverse at 5.0 V: \(R = \dfrac{5.0}{0.10 \times 10^{-6}} = 5.0 \times 10^{7}\,\Omega\).
The resistance of the diode ranges over a factor of a million. The forward resistance falls as the p.d. rises, and the reverse resistance is enormous. Convert mA and µA into A first.
:::

Try the widget. Slide the p.d. and read \(R = V/I\) at each point. Switch on the dashed line from the origin (its gradient is \(1/R\)) and then the tangent. For the lamp the two lines differ, so the tangent does **not** give \(1/R\).

:::html
<div class="widget" data-w="phys-iv" data-c="lamp"></div>
:::

:::lab Measuring an I–V characteristic
The supply must be able to reach 0 V, so a **potential divider** is used rather than a single variable resistor. The ammeter is in series with the component and the voltmeter is in parallel with it.

:::html
<figure class="fig"><svg viewBox="85 28 450 210" role="img" aria-label="Circuit for measuring an I-V characteristic. A cell is connected across the two ends of a variable resistor. A sliding contact on the resistor and one end of it feed a series branch containing an ammeter and the component under test, with a voltmeter connected across the component."><path class="ln" d="M200 60H100V210H300M310 210H520V60H420"/><path class="ln" d="M300 194V226"/><path class="ln thick" d="M310 202V218"/><text class="ts tc" x="290" y="190">+</text><rect class="fp s-ink sw2" x="200" y="52" width="220" height="16"/><path class="ln" d="M310 112V72" marker-end="url(#ah)"/><text class="tl te" x="300" y="96">slider</text><text class="tl tc" x="310" y="44">variable resistor</text><path class="ln" d="M310 112H337M363 112H420M464 112H480V170H100"/><circle class="fi" cx="100" cy="170" r="4"/><circle class="fp s-ink sw2" cx="350" cy="112" r="13"/><text class="tb tc" x="350" y="117">A</text><rect class="fp s-ink sw2" x="420" y="104" width="44" height="16"/><text class="tl tc" x="442" y="140">component</text><circle class="fi" cx="390" cy="112" r="4"/><circle class="fi" cx="480" cy="112" r="4"/><path class="ln" d="M390 112V84H429M455 84H480V112"/><circle class="fp s-ink sw2" cx="442" cy="84" r="13"/><text class="tb tc" x="442" y="89">V</text></svg><figcaption>Moving the slider changes the p.d. across the component from 0 V up to the cell's e.m.f. Reversing the cell (or the connections to the component) gives the negative half of the characteristic.</figcaption></figure>
:::

:::steps
1. Connect the circuit as shown. For a diode, add a **protective resistor** in series (for example \(100\,\Omega\)), so the forward current cannot burn it out.
2. Set the slider so the p.d. is 0 V. Increase it in equal steps and record \(V\) and \(I\) at each step. Take at least 10 readings over the whole range, with more where the graph bends.
3. Switch the circuit off between readings for a metal wire, so it stays at constant temperature. A lamp is meant to warm up, so wait a few seconds at each setting.
4. Reverse the connections to the cell and repeat to get the negative values.
5. Plot \(I\) against \(V\) and join the points with a smooth curve (a straight line for the wire). Find \(R = V/I\) at chosen points.
:::
:::

## Resistivity

Resistance depends on the size of the sample as well as on the material. A longer wire gives the carriers more ions to collide with, so \(R\) is proportional to the length \(L\). A thicker wire gives them more room, so \(R\) is inversely proportional to the cross-sectional area \(A\). Combining the two:

:::formula Resistivity
\[R = \frac{\rho L}{A} \qquad\text{so}\qquad \rho = \frac{RA}{L}\]
\(R\): resistance (\(\Omega\)) · \(\rho\): resistivity (\(\Omega\,\mathrm{m}\)) · \(L\): length (m) · \(A\): cross-sectional area (\(\mathrm{m^{2}}\)). For a round wire, \(A = \pi d^{2}/4\).
:::

:::def Resistivity
The resistivity \(\rho\) of a material is a property of the material, equal to the resistance of a sample of unit length and unit cross-sectional area: \(\rho = RA/L\). Its unit is the ohm metre (\(\Omega\,\mathrm{m}\)).
:::

Resistivity depends on the material and its temperature, **not** on the shape or size of the sample. A fat, short copper rod and a long, thin copper wire have the same \(\rho\) but very different \(R\). Typical values at room temperature (not for recall, and they will be given in a question) are in the table.

| Material | Typical resistivity / Ω m | Type |
|---|---|---|
| Copper | \(1.7 \times 10^{-8}\) | good conductor |
| Nichrome | \(1.1 \times 10^{-6}\) | alloy used in heaters |
| Pure silicon | about \(2 \times 10^{3}\) | semiconductor |
| Glass | about \(10^{11}\) | insulator |

:::eg A nichrome wire is 1.5 m long and has a diameter of 0.30 mm. Its resistivity is \(1.1 \times 10^{-6}\,\Omega\,\mathrm{m}\). Find its resistance. What would the resistance be if the same volume of wire were drawn out to twice the length?
Area: \(A = \pi \times (0.15 \times 10^{-3})^{2} = 7.07 \times 10^{-8}\,\mathrm{m^{2}}\). [C1]
\[R = \frac{\rho L}{A} = \frac{1.1 \times 10^{-6} \times 1.5}{7.07 \times 10^{-8}} = 23\,\Omega\] [C1] [A1]
The volume \(AL\) is fixed. Doubling \(L\) halves \(A\). Then \(R \propto L/A\) becomes \(2 \div \tfrac12 = 4\) times bigger: about \(93\,\Omega\). [B1]
:::

:::warn Converting areas
A diameter in millimetres must be changed into metres **before** it is squared: \(0.30\,\mathrm{mm} = 3.0 \times 10^{-4}\,\mathrm{m}\). The radius is half the diameter. Writing \(A = \pi d^{2}\) instead of \(\pi d^{2}/4\) makes the area four times too large and \(R\) four times too small.
:::

:::lab Measuring the resistivity of a wire
:::steps
1. Stretch a straight, uniform wire along a metre rule and fix it at both ends. Measure its diameter \(d\) with a **micrometer** at several places along the wire and in two perpendicular directions, then take the mean. Avoid squeezing the wire.
2. Connect the wire to a low-voltage supply with an ammeter in series and a voltmeter across the length you are using. Attach one connection at the zero of the rule and a second contact at a measured length \(L\).
3. Use a small current and switch off between readings, so the wire does not warm up and change its resistivity. Record \(V\) and \(I\) and calculate \(R = V/I\).
4. Repeat for at least 5 lengths, for example 0.200 m to 1.000 m.
5. Plot \(R\) against \(L\). The points should lie on a straight line through the origin, because \(R = (\rho/A)L\). The gradient is \(\rho/A\), so \(\rho = \text{gradient} \times A\).
:::
:::

:::plot The best-fit line of resistance against length for a nichrome wire. Its gradient is \(\rho/A\).
--f "17.75*x+0.05" --x 0 1.1 --y 0 22 --pt "0.2,3.6,(0.200, 3.6)@se" --pt "1,17.8,(1.000, 17.8)@nw" --xlabel "L / m" --ylabel "R / Ω"
:::

:::eg The graph above was drawn for a wire of diameter 0.28 mm. Use the two marked points to find the resistivity of the wire.
\[\text{gradient} = \frac{17.8 - 3.6}{1.000 - 0.200} = 17.75\,\Omega\,\mathrm{m^{-1}}\] [C1]
The area is \(A = \pi \times (0.14 \times 10^{-3})^{2} = 6.16 \times 10^{-8}\,\mathrm{m^{2}}\).
\[\rho = \text{gradient} \times A = 17.75 \times 6.16 \times 10^{-8} = 1.1 \times 10^{-6}\,\Omega\,\mathrm{m}\] [A1]
This agrees with the value for nichrome. Using two points far apart on the line gives a more reliable gradient than using two close together.
:::

## Sensors: the LDR and the thermistor

The resistance of some components changes with their surroundings, and this lets circuits measure the world. In both the components below, the change comes from the number density of free carriers: more energy in the material frees more carriers, so \(n\) in \(I = Anvq\) goes up and the resistance goes down.

A **light-dependent resistor (LDR)** is a semiconductor whose resistance **decreases as the light intensity increases**. In the dark its resistance may be about \(100\,\mathrm{k\Omega}\) or more, and in bright light only a few hundred ohms or kilohms.

A **thermistor** in this syllabus is a negative temperature coefficient (NTC) thermistor, a semiconductor whose resistance **decreases as its temperature increases**. Warming the material releases more carriers.

:::plot Resistance of a typical NTC thermistor against temperature. The resistance falls steeply when the thermistor is cold, then more slowly.
--f "10*exp(3950*(1/(x+273.15)-1/298.15))" --x 0 60 --y 0 36 --pt "25,10,10 kΩ at 25 °C@ne" --pt "50,3.59,3.6 kΩ at 50 °C@ne" --xlabel "θ / °C" --ylabel "R / kΩ" --label "NTC thermistor"
:::

:::plot Resistance of a typical LDR against light intensity. The resistance is large in dim light and small in bright light.
--f "100*(10/x)**0.8" --x 5 100 --y 0 200 --pt "10,100,100 kΩ at 10 lux@ne" --pt "50,27.6,28 kΩ at 50 lux@ne" --xlabel "light intensity / lux" --ylabel "R / kΩ" --label "LDR"
:::

:::eg A thermistor of resistance \(10\,\mathrm{k\Omega}\) at 25 °C is connected across a 5.0 V supply. Its resistance at 100 °C is \(0.70\,\mathrm{k\Omega}\). Find the current at each temperature.
At 25 °C: \(I = \dfrac{V}{R} = \dfrac{5.0}{10 \times 10^{3}} = 0.50\,\mathrm{mA}\). [C1] [A1]
At 100 °C: \(I = \dfrac{5.0}{0.70 \times 10^{3}} = 7.1\,\mathrm{mA}\). [A1]
The current is 14 times larger at 100 °C, because the resistance has fallen to a fourteenth. [B1]
:::

:::exam Explaining a sensor
A common question says "explain why the resistance of a thermistor decreases when the temperature increases". Write: the temperature rises, so more charge carriers are released (the number density \(n\) increases); with more carriers available, the same p.d. gives a larger current, so the resistance falls. For a **metal** wire, say the opposite: the lattice ions vibrate more, collide more often with the electrons, and the resistance rises.
:::

Both sensors become really useful in a **potential divider**, which turns a change in resistance into a change in p.d. That is the topic of [D.C. circuits](#phys.dc).

:::board
AQA also teaches superconductivity (a material whose resistivity becomes zero below its critical temperature); Cambridge does not. OCR A writes the drift-speed equation as \(I = Anev\), with the carriers taken to be electrons. The physics is the same.
:::

:::eg Spot the error: the I–V graph of a filament lamp is a curve. At the point V = 6.0 V, I = 0.25 A, the tangent has gradient 0.025 A V⁻¹. Calculate the resistance of the lamp at this point.
A student wrote this answer.

Line 1: at the point, \(V = 6.0\,\mathrm{V}\) and \(I = 0.25\,\mathrm{A}\)
Line 2: \(R = 1/\text{gradient of the tangent} = 1/0.025 = 40\,\Omega\)

Line 1 is correct. [B1] **Line 2 is wrong: resistance is defined as \(V/I\) at the point, not the reciprocal of the gradient of the tangent. The method mark and the answer mark are lost.** [M0] [A0]

Correct working: \(R = V/I = 6.0/0.25 = 24\,\Omega\). [A1]

Check: the tangent is flatter than the line from the origin to the point (the lamp curve flattens as it goes up), so \(1/\text{gradient}\) gives a larger value than \(V/I\). The two agree only for an ohmic component.
:::

:::try Start easy, finish at exam standard
Q: A current of 4.0 mA flows for 5.0 s. How much charge passes?
A: \(I = 4.0 \times 10^{-3}\,\mathrm{A}\), so \(Q = It = 4.0 \times 10^{-3} \times 5.0 = 2.0 \times 10^{-2}\,\mathrm{C}\).
Q: How many electrons pass a point each second in a current of 0.50 A?
A: Charge per second is 0.50 C, so \(N = 0.50/(1.60 \times 10^{-19}) = 3.1 \times 10^{18}\).
Q: A \(330\,\Omega\) resistor is connected across a 12 V supply. Find the current and the power dissipated.
A: \(I = 12/330 = 0.0364\,\mathrm{A} = 36\,\mathrm{mA}\). \(P = VI = 12 \times 0.0364 = 0.44\,\mathrm{W}\).
Q: A current of 2.5 A flows for 10 minutes through a component with a p.d. of 6.0 V across it. How much energy is transferred?
A: \(Q = It = 2.5 \times 600 = 1500\,\mathrm{C}\), so \(W = QV = 1500 \times 6.0 = 9.0 \times 10^{3}\,\mathrm{J}\), that is 9.0 kJ.
Q: A wire of resistance \(4.0\,\Omega\) is 2.0 m long. What is the resistance of a 3.0 m length of the same wire?
A: \(R \propto L\) for the same material and area, so \(R = 4.0 \times 3.0/2.0 = 6.0\,\Omega\).
Q: A lamp is marked "230 V, 60 W". Find its operating resistance and current.
A: \(R = V^{2}/P = 230^{2}/60 = 880\,\Omega\) and \(I = P/V = 60/230 = 0.26\,\mathrm{A}\).
Q: Find the resistance of a copper wire of length 2.0 m and diameter 0.60 mm. Take \(\rho = 1.7 \times 10^{-8}\,\Omega\,\mathrm{m}\).
A: \(A = \pi \times (0.30 \times 10^{-3})^{2} = 2.83 \times 10^{-7}\,\mathrm{m^{2}}\). \(R = \dfrac{\rho L}{A} = \dfrac{1.7 \times 10^{-8} \times 2.0}{2.83 \times 10^{-7}} = 0.12\,\Omega\).
Q: Convert \(3.6 \times 10^{6}\,\mathrm{J}\) into kW h.
A: \(1\,\mathrm{kW\,h} = 3.6 \times 10^{6}\,\mathrm{J}\), so the energy is exactly 1.0 kW h.
Q: Electrons drift very slowly along a wire. Explain why a lamp still lights almost at once when a switch is closed.
A: The wire and the filament already contain free electrons. The electric field travels along the circuit at close to the speed of light, so all the electrons start drifting at about the same moment.
Q: State what happens to the resistance of an LDR when the light gets brighter, and of an NTC thermistor when it is heated.
A: Both decrease.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the potential difference across a component.
A: The energy transferred [B1] per unit charge passing through the component (from electrical to other forms of energy). [B1]
Q: [2 marks] ★ State Ohm's law.
A: The current in a metallic conductor is directly proportional to the potential difference across it [B1] provided the temperature (and other physical conditions) is constant. [B1]
Q: [3 marks] ★ A current of 0.80 A flows in a wire for 2.0 minutes. Calculate (a) the charge that passes a point in the wire and (b) the number of electrons that pass.
A: (a) \(Q = It = 0.80 \times 120\) [C1] \(= 96\,\mathrm{C}\). [A1] (b) \(N = 96/(1.60 \times 10^{-19}) = 6.0 \times 10^{20}\). [A1]
Q: [4 marks] ★★ (a) Describe the shape of the I–V characteristic of a filament lamp for both positive and negative p.d.s. (b) Explain why the resistance of the lamp increases as the current increases.
A: (a) The graph passes through the origin and is symmetrical about it. [B1] The line curves so that its gradient decreases as the magnitude of the p.d. increases. [B1] (b) A larger current raises the temperature of the filament. [B1] The lattice ions vibrate with greater amplitude, so the electrons collide with them more often and the resistance is larger. [B1]
Q: [3 marks] ★★ A semiconductor diode carries a current of 12 mA when the forward p.d. is 0.70 V. When the p.d. is reversed to 4.0 V, the current is 0.20 µA. Calculate the resistance of the diode in each case.
A: Forward: \(R = 0.70/(12 \times 10^{-3})\) [C1] \(= 58\,\Omega\). [A1] Reverse: \(R = 4.0/(0.20 \times 10^{-6}) = 2.0 \times 10^{7}\,\Omega\). [A1]
Q: [4 marks] ★★ Two copper wires are connected in series. Wire X has diameter 1.2 mm and wire Y has diameter 0.60 mm. The current is 3.0 A. (a) State and explain how the drift speed in Y compares with that in X. (b) Calculate the drift speed in Y. The number density of free electrons in copper is \(8.5 \times 10^{28}\,\mathrm{m^{-3}}\).
A: (a) The current is the same in both wires (series). The area of Y is a quarter of the area of X, so \(v \propto 1/A\) makes the drift speed in Y four times bigger. [B1] [B1] (b) \(A = \pi \times (0.30 \times 10^{-3})^{2} = 2.83 \times 10^{-7}\,\mathrm{m^{2}}\), and \(v = \dfrac{I}{Anq} = \dfrac{3.0}{2.83 \times 10^{-7} \times 8.5 \times 10^{28} \times 1.60 \times 10^{-19}}\) [C1] \(= 7.8 \times 10^{-4}\,\mathrm{m\,s^{-1}}\). [A1]
Q: [7 marks] ★★★ A student measures the resistance \(R\) of different lengths \(L\) of a wire of diameter \(0.28 \pm 0.01\,\mathrm{mm}\) and plots \(R\) against \(L\). The points are:

| L / m | 0.200 | 0.400 | 0.600 | 0.800 | 1.000 |
|---|---|---|---|---|---|
| R / Ω | 3.6 | 7.2 | 10.7 | 14.3 | 17.8 |

(a) State what the graph should look like if \(R\) is proportional to \(L\). (b) The best-fit line passes through (0.200, 3.6) and (1.000, 17.8). Find its gradient. (c) Calculate the resistivity of the wire. (d) Estimate the percentage uncertainty in the resistivity that comes from the diameter.
H: The gradient of the graph is \(\rho/A\).
H: The area depends on \(d^{2}\), so a percentage uncertainty in \(d\) counts twice.
H: Percentage uncertainty in \(d\) is \(\tfrac{0.01}{0.28} \times 100\%\).
A: (a) A straight line [B1] through the origin. (b) Gradient \(= \dfrac{17.8 - 3.6}{1.000 - 0.200}\) [C1] \(= 17.8\,\Omega\,\mathrm{m^{-1}}\). [A1] (c) \(A = \pi \times (0.14 \times 10^{-3})^{2} = 6.16 \times 10^{-8}\,\mathrm{m^{2}}\), so \(\rho = \text{gradient} \times A = 17.75 \times 6.16 \times 10^{-8}\) [C1] \(= 1.1 \times 10^{-6}\,\Omega\,\mathrm{m}\). [A1] (d) The percentage uncertainty in \(d\) is \(0.01/0.28 = 3.6\%\). [C1] Since \(\rho \propto d^{2}\), the percentage uncertainty in \(\rho\) is twice this, about 7%. [A1]
Q: [6 marks] ★★★ A heater element is made of nichrome wire of diameter 0.40 mm and is designed to transfer 1.5 kW from the 230 V mains. The resistivity of nichrome is \(1.1 \times 10^{-6}\,\Omega\,\mathrm{m}\). (a) Calculate the current in the element. (b) Calculate the resistance of the element. (c) Calculate the length of wire needed.
H: Use \(P = VI\) for the current, then \(R = V/I\) (or \(V^{2}/P\)).
H: Rearrange \(R = \rho L/A\) to make \(L\) the subject, using the area of a 0.40 mm diameter wire.
A: (a) \(I = P/V = 1500/230\) [C1] \(= 6.5\,\mathrm{A}\). [A1] (b) \(R = V^{2}/P = 230^{2}/1500\) [C1] \(= 35\,\Omega\). [A1] (c) \(A = \pi \times (0.20 \times 10^{-3})^{2} = 1.26 \times 10^{-7}\,\mathrm{m^{2}}\), and \(L = \dfrac{RA}{\rho} = \dfrac{35.3 \times 1.26 \times 10^{-7}}{1.1 \times 10^{-6}}\) [C1] \(= 4.0\,\mathrm{m}\). [A1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ A uniform wire is stretched to 1.1 times its original length. Its volume stays constant and its resistivity is unchanged. (a) Show that its resistance increases by a factor of \(1.1^{2}\). (b) Find the percentage increase in resistance.
H: Volume \(= AL\) is constant, so if \(L\) becomes \(1.1L\), what happens to \(A\)?
A: (a) The new area is \(A' = A/1.1\) because \(A'L' = AL\). [B1] Then \(R' = \dfrac{\rho L'}{A'} = \dfrac{\rho \times 1.1L}{A/1.1} = 1.1^{2}\,\dfrac{\rho L}{A} = 1.1^{2}R\). [M1] (b) \(R'/R = 1.1^{2} = 1.21\) [C1], so the resistance increases by 21%. [A1]
Q: [6 marks] ★★★ A copper wire and a rod of a semiconductor, both of cross-sectional area \(2.0\,\mathrm{mm^{2}}\), each carry a current of 1.0 mA. Copper has \(n = 8.5 \times 10^{28}\,\mathrm{m^{-3}}\) and the semiconductor \(n = 2.0 \times 10^{22}\,\mathrm{m^{-3}}\); in both the carriers are electrons. (a) Calculate the drift speed of the carriers in each. (b) Calculate the ratio of the semiconductor speed to the copper speed. (c) Explain, using \(I = Anvq\), why the ratio is so large. (d) The carriers in the semiconductor move far faster, yet the rod needs a much larger p.d. than the copper wire to carry the same current. Explain why.
H: \(2.0\,\mathrm{mm^{2}} = 2.0 \times 10^{-6}\,\mathrm{m^{2}}\).
A: (a) Copper: \(v = \dfrac{I}{Anq} = \dfrac{1.0 \times 10^{-3}}{2.0 \times 10^{-6} \times 8.5 \times 10^{28} \times 1.60 \times 10^{-19}}\) [C1] \(= 3.7 \times 10^{-8}\,\mathrm{m\,s^{-1}}\). [A1] Semiconductor: the same working with \(n = 2.0 \times 10^{22}\) gives \(0.16\,\mathrm{m\,s^{-1}}\). [A1] (b) Using the unrounded speeds, the ratio is \(\dfrac{v_\text{semi}}{v_\text{Cu}} = \dfrac{8.5 \times 10^{28}}{2.0 \times 10^{22}} = 4.3 \times 10^{6}\) (2 s.f., like the data). [A1] (c) For the same \(I\), \(A\) and \(q\), \(v \propto 1/n\). The semiconductor has about \(4 \times 10^{6}\) times fewer carriers per unit volume, so each carrier must drift that much faster to carry the same current. [B1] (d) The p.d. depends on the resistance, not on the drift speed. With so few carriers, the semiconductor's resistivity is many orders of magnitude larger than copper's, so \(R = \rho L/A\) is far larger for the same shape and \(V = IR\) is far larger for the same current. [B1]
:::

:::quiz
? Which of these charges could exist on an isolated object?
- \(2.4 \times 10^{-19}\,\mathrm{C}\)
+ \(3.2 \times 10^{-19}\,\mathrm{C}\)
- \(1.0 \times 10^{-19}\,\mathrm{C}\)
- \(4.0 \times 10^{-19}\,\mathrm{C}\)
> Charge must be a whole number of times \(1.60 \times 10^{-19}\,\mathrm{C}\). Only \(3.2 \times 10^{-19}\,\mathrm{C}\) is exactly 2e; the others are 1.5e, 0.625e and 2.5e.
? A copper wire of diameter 2.0 mm is joined in series to a wire of the same copper of diameter 1.0 mm. How does the drift speed in the thin wire compare with that in the thick wire?
+ 4 times greater
- 2 times greater
- The same
- 4 times smaller
> The current is the same and \(v \propto 1/A\). Halving the diameter makes the area a quarter, so the speed is four times greater. "2 times" forgets that the area depends on diameter squared.
? What is the unit of potential difference in base units?
+ \(\mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}\)
- \(\mathrm{kg\,m^{2}\,s^{-2}\,A^{-1}}\)
- \(\mathrm{kg\,m\,s^{-2}\,A^{-1}}\)
- \(\mathrm{kg\,m^{2}\,s^{-3}\,A}\)
> \(V = P/I\), and the watt is \(\mathrm{kg\,m^{2}\,s^{-3}}\), so the volt is \(\mathrm{kg\,m^{2}\,s^{-3}\,A^{-1}}\). The second option is a joule per ampere and the fourth multiplies by the current instead of dividing.
? The p.d. across a resistor is halved. What happens to the power dissipated in it, if its resistance is unchanged?
- It is halved.
- It stays the same.
+ It falls to a quarter.
- It is doubled.
> \(P = V^{2}/R\), so halving \(V\) divides \(P\) by 4. Halving would be right only if the current were fixed and the resistance changed.
? Which statement about the I–V characteristic of a filament lamp is correct?
- It is a straight line through the origin because the lamp is ohmic.
+ Its resistance \(V/I\) increases as the current increases, because the filament gets hotter.
- Its resistance decreases as the current increases because more carriers are freed.
- It conducts in one direction only.
> The lamp's graph is S-shaped and symmetrical. The rising temperature makes the lattice ions vibrate more, so collisions are more frequent and the resistance is larger. Freeing more carriers is the explanation for a thermistor.
? A diode is connected the wrong way round (reverse bias) in a circuit. What is the effect?
+ Almost no current flows because its resistance is very large.
- A very large current flows because its resistance is zero.
- It acts as an ohmic resistor of about \(0.6\,\Omega\).
- Its resistance is the same as in forward bias.
> A diode has a very high resistance in the reverse direction, so the current is almost zero. A short circuit would be a forward-biased diode well above 0.6 V.
? A wire has resistance \(R\). A second wire of the same material has twice the length and twice the cross-sectional area. What is the resistance of the second wire?
+ \(R\)
- \(2R\)
- \(4R\)
- \(R/2\)
> \(R = \rho L/A\). Doubling both \(L\) and \(A\) cancels, so the resistance is unchanged.
? What happens to the resistance of an NTC thermistor as its temperature rises?
+ It decreases because more charge carriers are released.
- It increases because the ions vibrate more.
- It stays constant.
- It decreases because the lattice ions vibrate less.
> A thermistor is a semiconductor, so heating it frees more carriers and its resistance falls. Increased lattice vibration is the explanation for a metal's rising resistance.
:::

:::checklist What you can now do
- [ ] I can explain that current is a flow of charge carriers, define it as rate of flow of charge, and use \(Q = It\) and the coulomb.
- [ ] I can explain that charge is quantised and use \(Q = ne\) to count electrons.
- [ ] I can derive and use \(I = Anvq\) and compare drift speeds in different wires.
- [ ] I can define p.d. and the volt, and use \(V = W/Q\).
- [ ] I can use \(P = VI\), \(P = I^{2}R\) and \(P = V^{2}/R\), and calculate the cost of electricity in kW h.
- [ ] I can define resistance and the ohm, use \(V = IR\), and state Ohm's law.
- [ ] I can sketch and explain the I–V characteristics of a metal wire, a filament lamp and a diode, and describe how to measure them.
- [ ] I can define resistivity, use \(R = \rho L/A\) and describe how to measure resistivity with a graph.
- [ ] I can describe how the resistance of an LDR and an NTC thermistor changes with light and temperature.
:::

:::recap
- Current is the rate of flow of charge, \(I = \Delta Q/\Delta t\); \(Q = It\), and \(1\,\mathrm{C} = 1\,\mathrm{A\,s}\). Charge is quantised: \(Q = ne\), with \(e = 1.60 \times 10^{-19}\,\mathrm{C}\).
- \(I = Anvq\): for the same current, the drift speed is inversely proportional to the area and to the number density.
- P.d. is energy transferred per unit charge, \(V = W/Q\); \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\).
- Power: \(P = VI = I^{2}R = V^{2}/R\). \(1\,\mathrm{kW\,h} = 3.6 \times 10^{6}\,\mathrm{J}\).
- Resistance \(R = V/I\) at a point (not a gradient); ohm = V A⁻¹. Ohm's law holds for a metal at constant temperature.
- Wire: straight line through the origin. Filament lamp: resistance rises with current because the filament is hotter. Diode: conducts only above about 0.6 V forward and has a very high resistance in reverse.
- Resistivity \(\rho = RA/L\) (unit \(\Omega\,\mathrm{m}\)) depends on the material and temperature only. \(R = \rho L/A\).
- LDR: resistance falls as light intensity rises. NTC thermistor: resistance falls as temperature rises.
:::

:::links
- explore: [Ohm's Law](https://phet.colorado.edu/en/simulations/ohms-law) · PhET · change the p.d. and resistance and watch the current
- explore: [Resistance in a Wire](https://phet.colorado.edu/en/simulations/resistance-in-a-wire) · PhET · see how resistivity, length and area change the resistance
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the electricity questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [D.C. circuits](#phys.dc)
