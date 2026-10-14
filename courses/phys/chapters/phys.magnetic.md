@chapter phys.magnetic
@title Magnetic fields
@level a2
@paper CAIE P4 (A Level)
@time 6–8 hours
@summary Magnetic fields from magnets and currents, the force on a current-carrying wire and on a moving charge, circular paths and velocity selection, the Hall effect and Hall probe, and the forces between parallel currents.

:::why
Magnetic fields turn electric current into motion: they spin every electric motor, steer the electron beams in old televisions and the particle beams at CERN, and sort atoms by mass in a mass spectrometer. The Hall probe, which uses the sideways push on moving charges, is the sensor in phone compasses and in the wheel-speed sensors of cars. The rules are few and follow one pattern, force at right angles to both the field and the motion, so a clear picture and a careful choice of direction win most of the marks.
:::

**Before you start**, you need forces on charges in [Electric fields](#phys.efields), circular motion from [Motion in a circle](#phys.circular) and the drift of charge carriers from [Electricity](#phys.electricity).

:::try Warm-up
Q: An electron is accelerated from rest through a p.d. of 500 V. Find its speed. (from [Electric fields](#phys.efields))
A: The electric potential energy lost becomes kinetic energy, \(eV = \tfrac12 mv^2\), so \(v = \sqrt{\dfrac{2eV}{m}} = \sqrt{\dfrac{2 \times 1.60 \times 10^{-19} \times 500}{9.11 \times 10^{-31}}} = 1.3 \times 10^{7}\,\mathrm{m\,s^{-1}}\).
Q: A 0.50 kg mass moves in a horizontal circle of radius 0.80 m on a string at \(4.0\,\mathrm{m\,s^{-1}}\). Find the tension. (from [Motion in a circle](#phys.circular))
A: The tension provides the centripetal force: \(F = \dfrac{mv^2}{r} = \dfrac{0.50 \times 4.0^2}{0.80} = 10\,\mathrm{N}\).
Q: A copper wire of cross-sectional area \(1.0\,\mathrm{mm^2}\) carries 2.0 A. The electron density is \(8.5 \times 10^{28}\,\mathrm{m^{-3}}\). Find the drift speed. (from [Electricity](#phys.electricity))
A: \(An = 1.0 \times 10^{-6} \times 8.5 \times 10^{28} = 8.5 \times 10^{22}\) and \(Anq = 1.36 \times 10^{4}\), so \(v = I/Anq = 2.0/(1.36 \times 10^{4}) = 1.5 \times 10^{-4}\,\mathrm{m\,s^{-1}}\).
:::

## Magnetic fields and field lines

Two kinds of source make a magnetic field. A **permanent magnet** has one, and so does **any moving charge**, which means any electric current. The two are really one: the field of a permanent magnet comes from the motion of electrons inside its atoms, which line up in a magnet and cancel in other materials. A magnetic field acts only on things that are moving charges, on magnetic poles, and on conductors carrying current. A charge that is at rest feels no magnetic force at all.

:::def Magnetic field
A region of space in which a moving charge, a current-carrying conductor or a magnetic pole experiences a force. It is produced by moving charges or by permanent magnets.
:::

You draw a magnetic field with **field lines**. The rules are the same as for electric field lines in [Electric fields](#phys.efields), with one important difference.

- The **direction** of a line at any point is the direction of the force on a (hypothetical) north pole placed there. Outside a magnet, lines run from the north pole to the south pole.
- The lines are drawn closer together where the field is **stronger**, and parallel and equally spaced where the field is uniform.
- Lines **never cross**, because the field has one direction at each point.
- Magnetic field lines are **closed loops**. Electric field lines start and end on charges, but there are no isolated magnetic poles: cut a magnet in two and each half has both a north and a south pole. Inside a magnet the lines run from south to north, completing the loop.

:::html
<figure class="fig small"><svg viewBox="50 -10 300 260" role="img" aria-label="Field lines of a bar magnet, north pole on the left. Lines leave the north pole, curve round outside the magnet, and enter the south pole. They are closest together near the poles."><rect class="f1 s-ink sw2" x="130" y="95" width="70" height="50"/><rect class="f2 s-ink sw2" x="200" y="95" width="70" height="50"/><text class="tb tc" x="165" y="125">N</text><text class="tb tc" x="235" y="125">S</text><path class="c1" d="M130 97C90 47 310 47 270 97"/><path class="c1" d="M194 59.5L206 59.5" marker-end="url(#ah-phys)"/><path class="c1" d="M130 143C90 193 310 193 270 143"/><path class="c1" d="M194 180.5L206 180.5" marker-end="url(#ah-phys)"/><path class="c1" d="M130 104C55 9 345 9 270 104"/><path class="c1" d="M194 32.8L206 32.8" marker-end="url(#ah-phys)"/><path class="c1" d="M130 136C55 231 345 231 270 136"/><path class="c1" d="M194 207.2L206 207.2" marker-end="url(#ah-phys)"/><path class="c1" d="M130 111C20 -29 380 -29 270 111"/><path class="c1" d="M194 6L206 6" marker-end="url(#ah-phys)"/><path class="c1" d="M130 129C20 269 380 269 270 129"/><path class="c1" d="M194 234L206 234" marker-end="url(#ah-phys)"/><path class="c1" d="M124 120L66 120" marker-end="url(#ah-phys)"/><path class="c1" d="M334 120L276 120" marker-end="url(#ah-phys)"/></svg><figcaption>The field of a bar magnet. Lines leave the north pole and enter the south pole, are closest together near the poles where the field is strongest, and never cross. Inside the magnet they continue from S to N, so every line is a closed loop.</figcaption></figure>
:::

When a field points at right angles to the page, you need a way to draw it on paper. A **dot in a circle** (⊙) means a field, or a current, pointing **out of the page**, towards you: it is the tip of an arrow coming at you. A **cross in a circle** (⊗) means **into the page**, away from you: it is the feathers of an arrow going away. A uniform field into the page is drawn as a grid of crosses.

## Fields due to currents

An electric current produces a magnetic field around it. The shapes you must be able to sketch are those of a long straight wire, a flat circular coil and a long solenoid.

**A long straight wire.** The field lines are concentric circles in planes at right angles to the wire, centred on it. The direction is given by the **right-hand grip rule**: point the thumb of your right hand along the conventional current, and your fingers curl in the direction of the field. For a current out of the page, the lines run anticlockwise. The field is strongest near the wire, so the lines are closer there and spread further apart as you move away.

**A flat circular coil.** Near each part of the wire the field loops round it as for a straight wire. Through the middle of the coil all the contributions point the same way, so the field is a bundle of lines passing straight through the coil along its axis, which loop round outside and return. The pattern looks like that of a short bar magnet: one face is a north pole and the other a south pole.

:::html
<figure class="fig"><svg viewBox="10 15 605 280" role="img" aria-label="Two field patterns. Panel a: end view of a long straight wire with current out of the page, a dot in a circle, surrounded by three concentric circular field lines with arrows pointing anticlockwise, further apart at larger radius. Panel b: side view of a flat circular coil, with the wire cutting the page at an upper point where the current is out of the page and a lower point where it is into the page. Field lines pass through the coil from left to right along the axis and loop back round outside it."><circle class="fp s-ink sw2" cx="125" cy="140" r="6"/><circle class="fi" cx="125" cy="140" r="2"/><path class="c1" d="M100 140A25 25 0 1 0 150 140A25 25 0 1 0 100 140"/><path class="c1" d="M132 115L118 115" marker-end="url(#ah-phys)"/><path class="c1" d="M118 165L132 165" marker-end="url(#ah-phys)"/><path class="c1" d="M75 140A50 50 0 1 0 175 140A50 50 0 1 0 75 140"/><path class="c1" d="M132 90L118 90" marker-end="url(#ah-phys)"/><path class="c1" d="M118 190L132 190" marker-end="url(#ah-phys)"/><path class="c1" d="M25 140A100 100 0 1 0 225 140A100 100 0 1 0 25 140"/><path class="c1" d="M132 40L118 40" marker-end="url(#ah-phys)"/><path class="c1" d="M118 240L132 240" marker-end="url(#ah-phys)"/><text class="tl tc" x="125" y="275">(a) straight wire</text><path class="ln-m thin dash" d="M450 93L450 187"/><path class="c1" d="M300 140L600 140"/><path class="c1" d="M560 140L574 140" marker-end="url(#ah-phys)"/><path class="c1" d="M375 76.8A75 19.2 0 1 0 525 76.8A75 19.2 0 1 0 375 76.8"/><path class="c1" d="M457 57.5L443 57.5" marker-end="url(#ah-phys)"/><path class="c1" d="M375 203.2A75 19.2 0 1 0 525 203.2A75 19.2 0 1 0 375 203.2"/><path class="c1" d="M457 222.5L443 222.5" marker-end="url(#ah-phys)"/><path class="c1" d="M330 74A120 44 0 1 0 570 74A120 44 0 1 0 330 74"/><path class="c1" d="M457 30L443 30" marker-end="url(#ah-phys)"/><path class="c1" d="M330 206A120 44 0 1 0 570 206A120 44 0 1 0 330 206"/><path class="c1" d="M457 250L443 250" marker-end="url(#ah-phys)"/><circle class="fp s-ink sw2" cx="450" cy="85" r="6"/><circle class="fi" cx="450" cy="85" r="2"/><circle class="fp s-ink sw2" cx="450" cy="195" r="6"/><path class="ln thin" d="M446.4 191.4L453.6 198.6M446.4 198.6L453.6 191.4"/><text class="tl tc" x="450" y="275">(b) flat coil, side view</text></svg><figcaption>(a) A long straight wire with the current out of the page: the field lines are concentric circles running anticlockwise, further apart where the field is weaker. (b) A flat circular coil in side view: the lines pass through the coil one way and loop back round outside, like the field of a short bar magnet, so the face they leave (right) is a north pole.</figcaption></figure>
:::

To find which face of a coil or solenoid is the north pole, look at that face end-on. If the current goes **anticlockwise**, that face is a **north** pole. If the current goes clockwise, it is a south pole. This is the grip rule again, with your fingers curling along the current and your thumb pointing to the north pole.

**A long solenoid.** A solenoid is a long coil of many turns. Each turn contributes, and inside the solenoid the contributions add to give a strong, **uniform** field along the axis: straight, parallel, equally spaced lines. Outside, the field is weak and the pattern is that of a bar magnet, with lines leaving from the north end and returning to the south end.

:::html
<figure class="fig"><svg viewBox="5 0 430 260" role="img" aria-label="Side view of a long solenoid of six turns. Current comes out of the page at the top wires and goes into the page at the bottom wires. Inside, four straight parallel field lines run left to right, equally spaced. Outside, each line loops round from the right end back to the left end, like the field of a bar magnet. The right-hand end is the north pole."><path class="c1" d="M95 103.3L345 103.3"/><path class="c1" d="M212 103.3L226 103.3" marker-end="url(#ah-phys)"/><path class="c1" d="M95 116.7L345 116.7"/><path class="c1" d="M212 116.7L226 116.7" marker-end="url(#ah-phys)"/><path class="c1" d="M95 143.3L345 143.3"/><path class="c1" d="M212 143.3L226 143.3" marker-end="url(#ah-phys)"/><path class="c1" d="M95 156.7L345 156.7"/><path class="c1" d="M212 156.7L226 156.7" marker-end="url(#ah-phys)"/><path class="c1" d="M345 103.3C415 103.3 415 55 220 55C25 55 25 103.3 95 103.3"/><path class="c1" d="M227 55L213 55" marker-end="url(#ah-phys)"/><path class="c1" d="M345 116.7C455 116.7 455 15 220 15C-15 15 -15 116.7 95 116.7"/><path class="c1" d="M227 15L213 15" marker-end="url(#ah-phys)"/><path class="c1" d="M345 156.7C415 156.7 415 205 220 205C25 205 25 156.7 95 156.7"/><path class="c1" d="M227 205L213 205" marker-end="url(#ah-phys)"/><path class="c1" d="M345 143.3C455 143.3 455 245 220 245C-15 245 -15 143.3 95 143.3"/><path class="c1" d="M227 245L213 245" marker-end="url(#ah-phys)"/><circle class="fp s-ink sw2" cx="120" cy="90" r="6"/><circle class="fi" cx="120" cy="90" r="2"/><circle class="fp s-ink sw2" cx="120" cy="170" r="6"/><path class="ln thin" d="M116.4 166.4L123.6 173.6M116.4 173.6L123.6 166.4"/><circle class="fp s-ink sw2" cx="160" cy="90" r="6"/><circle class="fi" cx="160" cy="90" r="2"/><circle class="fp s-ink sw2" cx="160" cy="170" r="6"/><path class="ln thin" d="M156.4 166.4L163.6 173.6M156.4 173.6L163.6 166.4"/><circle class="fp s-ink sw2" cx="200" cy="90" r="6"/><circle class="fi" cx="200" cy="90" r="2"/><circle class="fp s-ink sw2" cx="200" cy="170" r="6"/><path class="ln thin" d="M196.4 166.4L203.6 173.6M196.4 173.6L203.6 166.4"/><circle class="fp s-ink sw2" cx="240" cy="90" r="6"/><circle class="fi" cx="240" cy="90" r="2"/><circle class="fp s-ink sw2" cx="240" cy="170" r="6"/><path class="ln thin" d="M236.4 166.4L243.6 173.6M236.4 173.6L243.6 166.4"/><circle class="fp s-ink sw2" cx="280" cy="90" r="6"/><circle class="fi" cx="280" cy="90" r="2"/><circle class="fp s-ink sw2" cx="280" cy="170" r="6"/><path class="ln thin" d="M276.4 166.4L283.6 173.6M276.4 173.6L283.6 166.4"/><circle class="fp s-ink sw2" cx="320" cy="90" r="6"/><circle class="fi" cx="320" cy="90" r="2"/><circle class="fp s-ink sw2" cx="320" cy="170" r="6"/><path class="ln thin" d="M316.4 166.4L323.6 173.6M316.4 173.6L323.6 166.4"/><text class="tb tc" x="361" y="135">N</text><text class="tb tc" x="79" y="135">S</text></svg><figcaption>Field of a solenoid. Inside, the lines are straight, parallel and evenly spaced, so the field is uniform and strong. Outside, the pattern is that of a bar magnet, and the right-hand end (where the lines emerge) is a north pole.</figcaption></figure>
:::

A stronger current, or more turns in the same length, gives a stronger field. You are not asked for formulae for the size of the field near a wire or inside a solenoid, only for these patterns and the reasoning behind them.

:::tip A ferrous core makes an electromagnet
Put a core of soft iron inside a solenoid and the field becomes much stronger. The field of the current magnetises the iron, turning each of its tiny magnetic regions in the same direction, and the iron then adds its own field to that of the coil. Soft iron is used because it magnetises and demagnetises easily, so switching the current off removes the field. Steel would stay magnetised. This is how electromagnets lift scrap metal and how a relay uses a small current to close the contacts of a circuit carrying a large one.
:::

## Force on a current-carrying conductor

A wire carrying a current is surrounded by its own field. Put it in another magnetic field and the two fields interact, which pushes the wire sideways. This is the **motor effect**. The force is largest when the wire is at right angles to the field, and zero when the wire is parallel to the field. In between it depends on the angle \(\theta\) between the wire and the field.

:::formula Force on a current-carrying conductor
\[F = BIL\sin\theta\]
\(F\): force (N) · \(B\): magnetic flux density (T) · \(I\): current (A) · \(L\): length of wire in the field (m) · \(\theta\): angle between the wire and the field direction. For a wire at right angles to the field, \(F = BIL\).
:::

The quantity \(B\) is called the **magnetic flux density**. It is the measure of how strong the field is, and this equation defines it.

:::def Magnetic flux density
The force acting per unit current per unit length on a wire placed at right angles to the magnetic field: \(B = \dfrac{F}{IL}\).
:::

:::def The tesla
One tesla is the magnetic flux density when a wire carrying a current of 1 A, at right angles to the field, experiences a force of 1 N per metre of its length: \(1\,\mathrm{T} = 1\,\mathrm{N\,A^{-1}\,m^{-1}}\).
:::

The \(\sin\theta\) is there because only the component of the field **at right angles to the wire**, \(B\sin\theta\), pushes the wire. The component along the wire has no effect. Take care: \(\theta\) is the angle between the wire and the **field**, not the angle to a normal or to a plane. A wire parallel to the field has \(\theta = 0\), so \(F = 0\).

:::eg A straight wire 0.050 m long carries a current of 3.0 A in a uniform field of flux density 0.20 T. Find the force on the wire when it is (a) at right angles to the field and (b) at 30° to the field.
(a) \(F = BIL = 0.20 \times 3.0 \times 0.050\) [C1] \(= 0.030\,\mathrm{N}\). [A1]
(b) \(F = BIL\sin\theta = 0.20 \times 3.0 \times 0.050 \times \sin 30^\circ\) [C1] \(= 0.015\,\mathrm{N}\). [A1]
At 30° the force is half as large, because \(\sin 30^\circ = 0.5\).
:::

### The direction of the force: Fleming's left-hand rule

The force is at right angles to **both** the wire and the field, so it needs a rule. Hold your **left** hand with the thumb, first finger and second finger at right angles to each other. Point the **first** finger along the **field**, the **se**cond finger along the (conventional) **current**, and the thumb then shows the direction of the **force** (the **th**rust, or motion).

:::html
<figure class="fig"><svg viewBox="-10 5 490 290" role="img" aria-label="Three mutually perpendicular arrows from one point, labelled as in Fleming's left-hand rule. The field B points to the right, the current I points out of the page towards the viewer, drawn down and to the left, and the force F points straight up."><path class="c1" d="M200 170L360 170" marker-end="url(#ah-phys)"/><path class="c2" d="M200 170L120 250" marker-end="url(#ah2-phys)"/><path class="c3" d="M200 170L200 40" marker-end="url(#ahr)"/><text class="tl" x="366" y="174">B: field</text><text class="tl" x="366" y="190">(first finger)</text><text class="tl te" x="114" y="260">I: current</text><text class="tl te" x="114" y="276">(second finger)</text><text class="tl tc" x="200" y="32">F: force or motion (thumb)</text><circle class="fi" cx="200" cy="170" r="3"/></svg><figcaption>Fleming's left-hand rule: the first finger points along the field, the second finger along the conventional current, and the thumb shows the direction of the force. The three directions are at right angles. Here the current points out of the page.</figcaption></figure>
:::

Use the **conventional** current, from positive to negative, and the left hand. Many students lose a mark by using the right hand, which is for the direction of a field around a wire.

:::eg A straight wire carries a current to the right through a uniform magnetic field directed into the page. Give the direction of the force on the wire.
Point the first finger into the page (the field) and the second finger to the right (the current). [C1]
The thumb points up the page, so the force on the wire is **upwards**. [A1]
If either the field or the current were reversed, the force would reverse. If both were reversed, it would stay the same.
:::

### Measuring B with a current balance

The wire experiences a force, and by Newton's third law the magnets feel an equal and opposite force on them. If the magnets stand on a top-pan balance, this force changes the reading, and you can find \(B\).

:::html
<figure class="fig small"><svg viewBox="45 25 350 225" role="img" aria-label="A current balance. Two magnet poles, north on the left and south on the right, stand on the pan of a top-pan balance with a uniform field between them pointing from north to south. A straight wire passes through the gap at right angles to the field, shown end-on with the current out of the page. The force on the wire is upwards, so the magnets feel an equal downward force and the balance reading increases."><rect class="fp s-ink sw2" x="60" y="195" width="320" height="36"/><rect class="fm s-mute sw1" x="250" y="203" width="100" height="20"/><text class="tl tc" x="300" y="218">0.00 g</text><rect class="fm s-ink sw2" x="80" y="185" width="280" height="10"/><rect class="f1 s-ink sw2" x="130" y="95" width="50" height="90"/><rect class="f2 s-ink sw2" x="260" y="95" width="50" height="90"/><text class="tb tc" x="155" y="145">N</text><text class="tb tc" x="285" y="145">S</text><path class="c1" d="M188 155L252 155" marker-end="url(#ah-phys)"/><text class="tl tc" x="220" y="172">B</text><circle class="fp s-ink sw2" cx="220" cy="120" r="6"/><circle class="fi" cx="220" cy="120" r="2"/><text class="tl tc" x="220" y="142">wire</text><path class="c3" d="M220 111L220 72" marker-end="url(#ahr)"/><text class="tl" x="230" y="90">F</text><path class="c2" d="M155 62L155 92" marker-end="url(#ah2-phys)"/><path class="c2" d="M285 62L285 92" marker-end="url(#ah2-phys)"/><text class="tl tc" x="220" y="50">equal and opposite forces on the magnets</text></svg><figcaption>A current balance. The wire is held still by a clamp (not shown) and carries a current through the field between the poles. The force on the wire is upwards, so by Newton's third law the force on the magnets is downwards, and the reading rises by \(\Delta m\) where \(\Delta m\,g = BIL\).</figcaption></figure>
:::

:::lab Measuring a magnetic flux density with a current balance
:::steps
1. Stand a pair of magnets (north and south poles facing each other, on a steel yoke) on a top-pan balance, so the field between the poles is horizontal. Clamp a stiff wire so that a length \(L\) lies between the poles, at right angles to the field, and measure \(L\) with a rule.
2. Connect the wire in series with a power supply, a variable resistor and an ammeter. With no current, tare the balance so that it reads zero.
3. Switch on and record the current \(I\) and the change \(\Delta m\) in the balance reading. Repeat for at least six values of \(I\) (reverse the current to check that \(\Delta m\) changes sign).
4. Plot \(\Delta m\) against \(I\). The force on the magnets is \(\Delta m\,g = BIL\), so the graph is a straight line through the origin with gradient \(BL/g\). Then \(B = g \times \text{gradient}/L\).
5. To reduce uncertainty, use a large current, a long length \(L\) in the field, and a line of best fit instead of one reading.
:::
Only the part of the wire between the poles is in the field. Wires leading to it are in a much weaker field, so they add little to the force.
:::

:::eg In a current balance the wire has \(L = 0.040\,\mathrm{m}\) in the field. A graph of the change in balance reading \(\Delta m\) against current \(I\) is a straight line through the origin, passing through \(\Delta m = 0.40\,\mathrm{g}\) at \(I = 2.0\,\mathrm{A}\). Find the magnetic flux density.
The gradient is \(0.40\,\mathrm{g}/2.0\,\mathrm{A} = 0.20\,\mathrm{g\,A^{-1}} = 2.0 \times 10^{-4}\,\mathrm{kg\,A^{-1}}\). [C1]
The force is \(F = \Delta m\,g = BIL\), so \(B = \dfrac{g \times \text{gradient}}{L}\). [C1]
\[B = \frac{9.81 \times 2.0 \times 10^{-4}}{0.040} = 4.9 \times 10^{-2}\,\mathrm{T}\] [A1]
That is about 49 mT, typical of a pair of small bar magnets.
:::

The motor effect also explains how an electric motor turns. In a rectangular coil in a field, the currents in the two sides that cut across the field flow in opposite directions, so the forces on them are opposite. This pair of equal and opposite forces is a **couple** (see [Forces, density and pressure](#phys.forces)), and it turns the coil.

## Force on a moving charge

A current is a flow of moving charges, so the force on a wire is the sum of the forces on its moving charge carriers. The same field therefore acts on a single moving charge \(Q\) with speed \(v\).

:::formula Force on a moving charge
\[F = BQv\sin\theta\]
\(F\): force (N) · \(B\): magnetic flux density (T) · \(Q\): charge (C) · \(v\): speed (\(\mathrm{m\,s^{-1}}\)) · \(\theta\): angle between the velocity and the field. For a charge moving at right angles to the field, \(F = BQv\).
:::

:::proof Force on a single moving charge, from the force on a wire
Take a length \(L\) of a wire at right angles to a field \(B\), carrying a current \(I = nAvQ\) (\(n\) carriers per unit volume, cross-sectional area \(A\), drift speed \(v\), charge \(Q\) on each).
The force on the wire is \(F = BIL = B(nAvQ)L\).
The number of carriers in the length \(L\) is \(N = nAL\).
The force on one carrier is \(F/N = \dfrac{BnAvQL}{nAL} = BQv\).
So a charge \(Q\) moving at speed \(v\) at right angles to the field feels a force \(BQv\). For other angles, only the component of the velocity at right angles to the field counts, giving \(BQv\sin\theta\).
:::

### Direction of the force

Use Fleming's left-hand rule again, with the second finger along the **conventional current**. For a **positive** charge the current is in the direction of the velocity. For a **negative** charge, such as an electron, the conventional current is **opposite** to the velocity, so point your second finger against the electron's motion. The force on an electron is opposite to the force on a proton moving in the same direction in the same field.

Two features of this force are essential.

- It is at right angles to both the field and the velocity.
- Because it is always at right angles to the velocity, it does **no work** on the charge: the speed and the kinetic energy do not change. The force changes only the direction of travel.

:::eg An electron moves at \(2.0 \times 10^{7}\,\mathrm{m\,s^{-1}}\) at right angles to a uniform magnetic field of flux density 5.0 mT. Find the force on it.
\[F = BQv = 5.0 \times 10^{-3} \times 1.60 \times 10^{-19} \times 2.0 \times 10^{7}\] [C1]
\[F = 1.6 \times 10^{-14}\,\mathrm{N}\] [A1]
This is tiny, but the electron's mass is tiny too, so the acceleration is enormous: \(a = F/m = 1.6 \times 10^{-14}/9.11 \times 10^{-31} = 1.8 \times 10^{16}\,\mathrm{m\,s^{-2}}\).
:::

:::eg A proton moves at \(4.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\) at 30° to a field of 0.40 T. Find the force on it.
\[F = BQv\sin\theta = 0.40 \times 1.60 \times 10^{-19} \times 4.0 \times 10^{6} \times \sin 30^\circ\] [C1]
\[F = 1.3 \times 10^{-13}\,\mathrm{N}\] [A1]
Only the component of the velocity at right angles to the field, \(v\sin 30^\circ\), is deflected. The component along the field is unaffected.
:::

## A charged particle in a uniform field

Fire a charged particle into a uniform magnetic field at right angles to the field. The force is at right angles to the velocity, so the speed stays the same but the direction turns. As the velocity turns, the force turns with it and stays at right angles. A force of constant size that is always at right angles to the velocity is exactly what is needed for circular motion, as in [Motion in a circle](#phys.circular).

:::html
<figure class="fig"><svg viewBox="25 30 425 220" role="img" aria-label="A uniform magnetic field directed into the page, shown by a grid of crosses. An electron enters from the left moving right and is bent downwards into a circular path of radius r, travelling clockwise. At the right-hand side of the circle the force F points towards the centre, at right angles to the velocity."><path class="ln-m thin" d="M67 47l6 6m0 -6l-6 6M67 107l6 6m0 -6l-6 6M67 167l6 6m0 -6l-6 6M67 227l6 6m0 -6l-6 6M127 47l6 6m0 -6l-6 6M127 107l6 6m0 -6l-6 6M127 167l6 6m0 -6l-6 6M127 227l6 6m0 -6l-6 6M187 47l6 6m0 -6l-6 6M187 107l6 6m0 -6l-6 6M187 227l6 6m0 -6l-6 6M247 47l6 6m0 -6l-6 6M247 107l6 6m0 -6l-6 6M307 47l6 6m0 -6l-6 6M307 227l6 6m0 -6l-6 6M367 47l6 6m0 -6l-6 6M367 107l6 6m0 -6l-6 6M367 167l6 6m0 -6l-6 6M367 227l6 6m0 -6l-6 6M427 47l6 6m0 -6l-6 6M427 107l6 6m0 -6l-6 6M427 167l6 6m0 -6l-6 6M427 227l6 6m0 -6l-6 6"/><path class="c1" d="M40 90L150 90" marker-end="url(#ah-phys)"/><path class="c1" d="M150 90L260 90"/><path class="c1" d="M190 160A70 70 0 1 0 330 160A70 70 0 1 0 190 160"/><path class="c1" d="M330 153L330 167" marker-end="url(#ah-phys)"/><path class="c1" d="M190 167L190 153" marker-end="url(#ah-phys)"/><path class="c3" d="M330 160L290 160" marker-end="url(#ahr)"/><path class="ln-m thin dash" d="M260 160L210.5 209.5"/><circle class="fi" cx="260" cy="160" r="2.5"/><text class="tl halo" x="224" y="188">r</text><text class="tl" x="50" y="78">electron, velocity v</text><text class="tl halo tc" x="310" y="152">F</text></svg><figcaption>An electron entering a uniform field directed into the page (crosses). The force is always at right angles to the velocity and towards the centre, so the electron moves on a circle of radius \(r\) at constant speed.</figcaption></figure>
:::

:::proof Radius of the circular path
The magnetic force provides the centripetal force: \(BQv = \dfrac{mv^2}{r}\).
Cancel one factor of \(v\): \(BQ = \dfrac{mv}{r}\).
Rearrange for the radius: \(r = \dfrac{mv}{BQ}\).
The time for one circle is \(T = \dfrac{2\pi r}{v} = \dfrac{2\pi m}{BQ}\): the speed has cancelled.
:::

:::key Charged particle moving at right angles to a uniform magnetic field
\[r = \frac{mv}{BQ} \qquad\qquad T = \frac{2\pi m}{BQ}\]
The path is a **circle** at constant speed. A faster particle moves on a **larger circle** but takes the **same time** to go round, and a heavier particle moves on a larger circle than a lighter one at the same speed. Compare with a charge entering an electric field, which follows a parabola and gains speed.
:::

:::eg Find the radius of the path of the electron in the earlier example (\(2.0 \times 10^{7}\,\mathrm{m\,s^{-1}}\) in a field of 5.0 mT), and the time taken for one circuit.
\[r = \frac{mv}{BQ} = \frac{9.11 \times 10^{-31} \times 2.0 \times 10^{7}}{5.0 \times 10^{-3} \times 1.60 \times 10^{-19}}\] [C1]
\[r = 2.3 \times 10^{-2}\,\mathrm{m} = 2.3\,\mathrm{cm}\] [A1]
\[T = \frac{2\pi r}{v} = \frac{2\pi \times 0.02278}{2.0 \times 10^{7}} = 7.2 \times 10^{-9}\,\mathrm{s}\] [A1]
**Check** with the other form: \(T = 2\pi m/BQ\) gives \(7.2 \times 10^{-9}\,\mathrm{s}\) as well. The electron goes round more than a hundred million times a second.
:::

:::eg A proton is accelerated from rest through a p.d. of 2.0 kV and then enters a region of uniform field of flux density 0.10 T at right angles to its velocity. Find the radius of its path.
The proton gains kinetic energy \(\tfrac12 mv^2 = eV\), so \(v = \sqrt{\dfrac{2eV}{m}} = \sqrt{\dfrac{2 \times 1.60 \times 10^{-19} \times 2000}{1.67 \times 10^{-27}}}\) [C1] \(= 6.2 \times 10^{5}\,\mathrm{m\,s^{-1}}\). [A1]
\[r = \frac{mv}{BQ} = \frac{1.67 \times 10^{-27} \times 6.19 \times 10^{5}}{0.10 \times 1.60 \times 10^{-19}}\] [C1]
\[r = 6.5 \times 10^{-2}\,\mathrm{m}\] [A1]
Do not round the speed before using it in the second step. Using the full value of \(v\) gives \(r = 6.46\,\mathrm{cm}\), which rounds to 6.5 cm.
:::

Circular paths in magnetic fields have important uses. In a **bubble chamber** the tracks of charged particles show up as curved lines: the radius tells you the particle's momentum (\(p = BQr\)), the direction of the curve tells you the sign of its charge, and a track that spirals inwards shows a particle losing energy as it moves. In a **mass spectrometer**, ions of the same charge and speed enter a magnetic field and are bent into semicircles whose radius \(r = mv/BQ\) is larger for heavier ions, so the detector separates the isotopes. Ions that all have the same speed come from the velocity selector described next.

## Velocity selection with crossed fields

A beam of charged particles usually contains particles with a range of speeds. To pick out a single speed, pass the beam through a region where an **electric field** and a **magnetic field** are at right angles to each other and to the beam, and arrange for the two forces to point in opposite directions.

:::html
<figure class="fig"><svg viewBox="25 45 440 180" role="img" aria-label="A velocity selector. Positive ions enter through a slit on the left between two horizontal plates, the upper plate positive, so the electric field points downwards. A magnetic field points into the page, shown by crosses. Ions of the right speed travel straight through the exit slit. Ions that are too fast curve upwards and ions that are too slow curve downwards."><rect class="fi" x="120" y="60" width="270" height="8"/><rect class="fi" x="120" y="170" width="270" height="8"/><text class="ts tc" x="104" y="70">+</text><text class="ts tc" x="104" y="180">−</text><path class="ln thick" d="M114 68L114 112M114 128L114 170M396 68L396 112M396 128L396 170"/><path class="ln-m thin" d="M147 89l6 6m0 -6l-6 6M147 145l6 6m0 -6l-6 6M192 89l6 6m0 -6l-6 6M192 145l6 6m0 -6l-6 6M237 89l6 6m0 -6l-6 6M237 145l6 6m0 -6l-6 6M282 89l6 6m0 -6l-6 6M282 145l6 6m0 -6l-6 6M357 100l6 6m0 -6l-6 6M357 134l6 6m0 -6l-6 6"/><path class="c1" d="M40 120L108 120" marker-end="url(#ah-phys)"/><text class="tl" x="40" y="108">ions</text><path class="c1" d="M120 120L396 120"/><path class="c1" d="M396 120L450 120" marker-end="url(#ah-phys)"/><path class="c2" d="M120 120C175 120 230 120 330 84" marker-end="url(#ah2-phys)"/><path class="c3" d="M120 120C175 120 230 120 330 156" marker-end="url(#ahr)"/><text class="tl" x="338" y="88">too fast</text><text class="tl" x="338" y="160">too slow</text><text class="tl halo" x="126" y="138">v = E/B</text><path class="c1" d="M425 78L425 112" marker-end="url(#ah-phys)"/><text class="tl" x="435" y="98">E</text><text class="tl tc" x="255" y="205">B into the page, E downwards</text></svg><figcaption>A velocity selector. The electric force on a positive ion is downwards and the magnetic force is upwards. Only ions for which the two forces are equal, with \(v = E/B\), pass undeflected through the exit slit; faster ions curve up, slower ions curve down.</figcaption></figure>
:::

For a positive ion moving to the right with the magnetic field into the page, Fleming's left-hand rule gives an **upward** magnetic force, so the electric field must point **down** to give a downward electric force. The ion goes straight through only if the two forces balance:
\[QE = BQv \quad\Rightarrow\quad v = \frac{E}{B}\]
The charge \(Q\) cancels, and so does the mass: **any** particle with this speed passes straight through, whatever its charge or mass. A faster particle has a larger magnetic force (\(\propto v\)) and bends towards the magnetic force, and a slower one bends towards the electric force. Only particles close to \(v = E/B\) get through the exit slit.

:::eg A velocity selector has plates 2.0 cm apart with a p.d. of 600 V between them, and a magnetic field of 0.15 T. Find the speed of the ions that pass straight through.
The electric field between the plates is \(E = \dfrac{V}{d} = \dfrac{600}{0.020} = 3.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\). [C1]
\[v = \frac{E}{B} = \frac{3.0 \times 10^{4}}{0.15} = 2.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\] [A1]
Ions of any mass and charge with this speed emerge undeflected. Changing \(E\) or \(B\) selects another speed.
:::

## The Hall effect

Put a thin slab of conductor in a magnetic field at right angles to its broad face, and pass a current along it. The moving charge carriers feel the magnetic force and are pushed sideways, towards one edge of the slab. They pile up there, leaving the opposite edge short of charge, so one edge becomes negative and the other positive. This **Hall effect** produces a measurable p.d. across the slab.

:::def Hall voltage
The potential difference produced across a conductor carrying a current in a magnetic field, at right angles to both the current and the field.
:::

:::html
<figure class="fig"><svg viewBox="35 25 555 235" role="img" aria-label="A rectangular slab seen in perspective, with the current I entering from the left, the magnetic field out of the page through the front face (dots) and electrons drifting to the left. Electrons are pushed to the bottom edge, which becomes negative, leaving the top edge positive. A voltmeter connected between the top and bottom edges reads the Hall voltage. The width d is the distance between the connected edges and the thickness t is the dimension along the field."><path class="fm s-ink sw1" d="M120 100L360 100L400 70L160 70Z"/><path class="fm2 s-ink sw1" d="M360 100L400 70L400 170L360 200Z"/><rect class="fp s-ink sw2" x="120" y="100" width="240" height="100"/><circle class="fp s-ink sw2" cx="170" cy="162" r="5"/><circle class="fi" cx="170" cy="162" r="2"/><circle class="fp s-ink sw2" cx="240" cy="162" r="5"/><circle class="fi" cx="240" cy="162" r="2"/><circle class="fp s-ink sw2" cx="310" cy="162" r="5"/><circle class="fi" cx="310" cy="162" r="2"/><text class="tl tc" x="150" y="116">+</text><text class="tl tc" x="150" y="192">−</text><text class="tl tc" x="200" y="116">+</text><text class="tl tc" x="200" y="192">−</text><text class="tl tc" x="250" y="116">+</text><text class="tl tc" x="250" y="192">−</text><text class="tl tc" x="300" y="116">+</text><text class="tl tc" x="300" y="192">−</text><path class="c2" d="M330 138L240 138" marker-end="url(#ah2-phys)"/><text class="tl" x="338" y="142">v</text><path class="c1" d="M50 160L118 160" marker-end="url(#ah-phys)"/><text class="tl tc" x="80" y="150">I</text><text class="tl" x="408" y="124">d</text><text class="tl" x="388" y="200">t</text><text class="tl tc" x="240" y="222">B out of the page</text><path class="ln" d="M340 100L340 40L470 40L470 127"/><path class="ln" d="M340 200L340 245L470 245L470 153"/><circle class="fp s-ink sw2" cx="470" cy="140" r="13"/><text class="tb tc" x="470" y="145">V</text><text class="tl" x="490" y="144">Hall voltage</text></svg><figcaption>The Hall effect in a slab. Current flows to the right, so electrons drift to the left. The field (out of the page) pushes them to the bottom edge, which becomes negative, and a Hall voltage \(V_\mathrm{H}\) appears between the top and bottom edges. The width is \(d\) and the thickness \(t\) is measured along the field.</figcaption></figure>
:::

The charge does not keep piling up. The separated charges produce an electric field across the slab, the **Hall field**, which pushes the carriers back. A steady state is reached when the electric force on a carrier balances the magnetic force on it, so the carriers then flow straight along the slab again, with a constant p.d. \(V_\mathrm{H}\) across it.

:::proof examinable The Hall voltage
A slab has width \(d\) (between the edges the voltmeter is connected to) and thickness \(t\) (measured **along the field**, so \(B\) is perpendicular to the \(d \times\) length face). It carries a current \(I\) of carriers of charge \(q\), \(n\) per unit volume, with drift speed \(v\).
The current is \(I = nAvq\) with cross-sectional area \(A = td\), so \(I = ntdvq\). (Step 1)
In the steady state the Hall field \(E_\mathrm{H}\) balances the magnetic force: \(qE_\mathrm{H} = Bqv\), so \(E_\mathrm{H} = Bv\). (Step 2)
The Hall field is uniform across the width \(d\), so \(V_\mathrm{H} = E_\mathrm{H}d = Bvd\). (Step 3)
From step 1, \(v = \dfrac{I}{ntdq}\). Substitute: \(V_\mathrm{H} = Bd \times \dfrac{I}{ntdq}\).
The width \(d\) cancels:
\[V_\mathrm{H} = \frac{BI}{ntq}\]
:::

:::formula The Hall voltage
\[V_\mathrm{H} = \frac{BI}{ntq}\]
\(V_\mathrm{H}\): Hall voltage (V) · \(B\): flux density (T) · \(I\): current (A) · \(n\): number density of charge carriers (\(\mathrm{m^{-3}}\)) · \(t\): thickness of the slab, measured along the field (m) · \(q\): charge on each carrier (C).
:::

The formula has two consequences. First, \(V_\mathrm{H}\) is proportional to \(B\), which is why the effect measures a magnetic field. Second, \(V_\mathrm{H}\) is inversely proportional to \(n\). In a metal \(n\) is huge (around \(10^{29}\,\mathrm{m^{-3}}\)), so the Hall voltage is far too small to use. In a **semiconductor**, \(n\) is many orders of magnitude smaller, so \(V_\mathrm{H}\) is large enough to measure.

:::eg A slab of semiconductor of thickness 0.50 mm carries a current of 20 mA in a field of 0.10 T at right angles to the slab. The charge carriers have number density \(1.0 \times 10^{22}\,\mathrm{m^{-3}}\) and charge \(e\). Find the Hall voltage, and compare it with the value for a copper slab of the same size under the same conditions (\(n = 8.5 \times 10^{28}\,\mathrm{m^{-3}}\)).
\[V_\mathrm{H} = \frac{BI}{ntq} = \frac{0.10 \times 20 \times 10^{-3}}{1.0 \times 10^{22} \times 0.50 \times 10^{-3} \times 1.60 \times 10^{-19}}\] [C1]
\[V_\mathrm{H} = 2.5 \times 10^{-3}\,\mathrm{V}\] [A1]
For copper only \(n\) changes. \(V_\mathrm{H}\) is inversely proportional to \(n\), so it falls by the factor \(8.5 \times 10^{28}/1.0 \times 10^{22} = 8.5 \times 10^{6}\): \(V_\mathrm{H} = 2.9 \times 10^{-10}\,\mathrm{V}\). [A1]
The semiconductor gives a few millivolts, easy to measure. Copper gives under a nanovolt, buried in noise.
:::

### The Hall probe

A **Hall probe** is a small slice of semiconductor with a constant current through it and a voltmeter across its edges. Since \(V_\mathrm{H} \propto B\) for a constant current, the reading shows the flux density. To use it, hold the probe so that the field is **at right angles to the face** of the slice, since only the component of \(B\) in that direction counts. Then rotate the probe a little and read the **maximum** voltage: this gives the field at that point. The probe is calibrated first in a field of known flux density, such as the inside of a long solenoid, and a thin slice (small \(t\)) makes it more sensitive. The sign of \(V_\mathrm{H}\) also shows whether the carriers are positive or negative.

## Forces between currents

Every current produces a field, and every current in a field feels a force. Two parallel wires carrying currents therefore push or pull on each other. Take two wires with current out of the page, as in the figure. Use the grip rule: the field of wire 2 at the position of wire 1 points **down**. Now use the left-hand rule on wire 1: the field is down and its current is out of the page, so the force on wire 1 points **towards** wire 2. By the same reasoning, wire 2 is pushed towards wire 1.

:::html
<figure class="fig small"><svg viewBox="110 45 260 130" role="img" aria-label="End view of two long parallel wires, both with current out of the page. The field of wire 2 at wire 1 points downwards and the field of wire 1 at wire 2 points upwards. The force on each wire points towards the other, so the wires attract."><circle class="fp s-ink sw2" cx="150" cy="110" r="6"/><circle class="fi" cx="150" cy="110" r="2"/><circle class="fp s-ink sw2" cx="330" cy="110" r="6"/><circle class="fi" cx="330" cy="110" r="2"/><text class="tl tc" x="150" y="90">wire 1</text><text class="tl tc" x="330" y="138">wire 2</text><path class="c1" d="M160 110L215 110" marker-end="url(#ah-phys)"/><path class="c1" d="M320 110L265 110" marker-end="url(#ah-phys)"/><text class="tl tc" x="188" y="100">F</text><text class="tl tc" x="292" y="100">F</text><path class="c3" d="M150 122L150 160" marker-end="url(#ahr)"/><text class="tl" x="158" y="150">B₂</text><path class="c3" d="M330 98L330 60" marker-end="url(#ahr)"/><text class="tl" x="338" y="80">B₁</text><text class="tl tc" x="240" y="150">the wires attract</text></svg><figcaption>Two parallel wires with currents in the same direction (both out of the page). Each wire is in the field of the other, \(B_2\) at wire 1 and \(B_1\) at wire 2, so each feels a force towards the other: the wires attract, and the two forces are equal and opposite.</figcaption></figure>
:::

:::key Forces between parallel currents
Currents in the **same direction** attract. Currents in **opposite directions** repel. The force on each wire is equal in size and opposite in direction to the force on the other, **even if the currents are different**, because the two forces are an interaction pair under Newton's third law. Each wire sits in the field of the other.
:::

To find the force between two currents, always follow the same two steps: find the direction of the field of one wire at the position of the other (grip rule), then find the force on the second wire (left-hand rule). Reverse one current and the force reverses, so the wires repel.

:::warn Directions: the three classic slips
Use the **left** hand for forces (and the right-hand grip rule only for the field around a wire). For an **electron**, the conventional current points opposite to the velocity, so the force is opposite to that on a positive charge moving the same way. And the magnetic force does **no work**: it can change the direction of a particle but never its speed or kinetic energy.
:::

:::board
The Cambridge syllabus asks for sketches of the field of a wire, a coil and a solenoid, but not for formulae for their size. It does require you to derive the Hall voltage \(V_\mathrm{H} = BI/(ntq)\), where \(t\) is the thickness along the field. Check your own specification for other boards' requirements.
:::

:::eg Spot the error: An electron moves to the right through a uniform magnetic field directed out of the page. State the direction of the force on it.
A student wrote this answer.

Line 1: The force is at right angles to both the velocity and the field, so it is up or down the page.
Line 2: Left-hand rule: first finger out of the page (field), second finger to the right (the electron's motion).
Line 3: The thumb points down, so the force is down.

Line 1 is correct. [B1] **Line 2 is wrong: the electron is negative, so the conventional current is opposite to its motion. The second finger must point to the left.** The direction mark is lost. [B0]

Correct working: first finger out of the page, second finger to the left, so the thumb points **up**. The force on the electron is upwards. [B1]

Check: a positive charge moving to the right in the same field would be pushed down, and an electron must be pushed the opposite way.
:::

:::try Start easy, finish at exam standard
Q: A wire of length 0.25 m carries a current of 6.0 A at right angles to a field of 0.080 T. Find the force on it.
A: \(F = BIL = 0.080 \times 6.0 \times 0.25 = 0.12\,\mathrm{N}\).
Q: What is the force on a wire that carries a current along the direction of a uniform magnetic field? Explain.
A: Zero. The angle \(\theta\) between the wire and the field is zero, so \(F = BIL\sin\theta = 0\): there is no component of the field at right angles to the wire.
Q: A wire carries a current to the right in a field directed down the page. Give the direction of the force.
A: First finger down the page, second finger to the right: the thumb points **into** the page.
Q: An electron moves at \(3.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\) at right angles to a field of 0.040 T. Find the force on it.
A: \(F = BQv = 0.040 \times 1.60 \times 10^{-19} \times 3.0 \times 10^{6} = 1.9 \times 10^{-14}\,\mathrm{N}\).
Q: A proton moves at \(5.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\) at right angles to a field of 0.20 T. Find the radius of its path.
A: \(r = \dfrac{mv}{BQ} = \dfrac{1.67 \times 10^{-27} \times 5.0 \times 10^{5}}{0.20 \times 1.60 \times 10^{-19}} = 2.6 \times 10^{-2}\,\mathrm{m}\).
Q: A velocity selector has \(E = 5.0 \times 10^{3}\,\mathrm{V\,m^{-1}}\) and \(B = 0.025\,\mathrm{T}\). What speed passes straight through?
A: \(v = E/B = 5.0 \times 10^{3}/0.025 = 2.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\).
Q: Explain why the Hall voltage is much larger in a semiconductor than in a copper strip of the same size.
A: \(V_\mathrm{H} = BI/(ntq)\), so for the same \(B\), \(I\) and \(t\), \(V_\mathrm{H}\) is inversely proportional to the number density \(n\) of carriers. A semiconductor has far fewer carriers per unit volume than a metal, so it gives a much larger \(V_\mathrm{H}\).
Q: Explain why a magnetic field can change the direction of a moving charged particle but cannot change its kinetic energy.
A: The magnetic force is always at right angles to the velocity, so it does no work on the particle (no displacement in the direction of the force). With no work done, the kinetic energy and speed are constant.
Q: A current flows out of the page along a straight wire. What is the direction of the field lines around it?
A: Anticlockwise, as seen from the front: the right-hand grip rule gives circles round the wire, with the thumb out of the page.
Q: Why is a core of soft iron placed inside the solenoid of an electromagnet?
A: The iron is magnetised by the field of the current, and adds its own field to that of the coil, making the total field much stronger. Soft iron loses its magnetism when the current is switched off.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define the tesla.
A: The magnetic flux density when a wire carrying a current of 1 A, at right angles to the field, [B1] experiences a force of 1 N per metre of its length. [B1]
Q: [2 marks] ★ A straight wire of length 0.15 m carries a current of 4.0 A in a uniform magnetic field of flux density 0.30 T. The wire makes an angle of 40° with the field. Calculate the force on the wire.
A: \(F = BIL\sin\theta = 0.30 \times 4.0 \times 0.15 \times \sin 40^\circ\) [C1] \(= 0.12\,\mathrm{N}\). [A1]
Q: [3 marks] ★ An electron moving to the right enters a uniform magnetic field directed into the page. (a) State the direction of the force on it as it enters the field. (b) Describe its path in the field and explain why its speed does not change.
A: (a) Down the page: the electron is negative, so the conventional current is to the left, and Fleming's left-hand rule gives a downward force. [B1] (b) An arc of a circle, turning clockwise. [B1] The force is always at right angles to the velocity, so it does no work on the electron and its kinetic energy, and so its speed, stay the same. [B1]
Q: [2 marks] ★★ Sketch the magnetic field pattern inside and outside a long solenoid, showing the direction of the field.
A: Inside the solenoid, straight parallel equally spaced lines along the axis, [B1] and outside, lines looping from one end back to the other like a bar magnet's, with arrows on all lines pointing out of the north end and into the south end. [B1]
Q: [4 marks] ★★ Explain the origin of the Hall voltage across a slab of conductor that carries a current in a magnetic field.
A: The charge carriers move at right angles to the field, so they experience a magnetic force at right angles to both. [B1] They are pushed to one side of the slab, making one edge negative and the other positive, [B1] which creates an electric field across the slab. [B1] The charge builds up until the electric force on a carrier equals the magnetic force on it, and the p.d. between the edges is then constant: the Hall voltage. [B1]
Q: [4 marks] ★★ A proton moves at \(3.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\) at right angles to a uniform magnetic field of flux density 0.50 T. (a) Calculate the radius of its circular path. (b) Calculate the time for one complete circle.
A: (a) \(r = \dfrac{mv}{BQ} = \dfrac{1.67 \times 10^{-27} \times 3.0 \times 10^{6}}{0.50 \times 1.60 \times 10^{-19}}\) [C1] \(= 6.3 \times 10^{-2}\,\mathrm{m}\). [A1] (b) \(T = \dfrac{2\pi r}{v} = \dfrac{2\pi \times 0.0626}{3.0 \times 10^{6}}\) [C1] \(= 1.3 \times 10^{-7}\,\mathrm{s}\). [A1]
Q: [3 marks] ★★ A Hall probe uses a slice of semiconductor of thickness 0.20 mm, with \(5.0 \times 10^{21}\) charge carriers per \(\mathrm{m^{3}}\), each of charge \(e\). With a current of 15 mA, the Hall voltage is 3.0 mV. (a) Calculate the magnetic flux density. (b) State why a semiconductor is used rather than a metal.
A: (a) \(B = \dfrac{V_\mathrm{H}\,ntq}{I}\) [C1]. First \(V_\mathrm{H}n = 3.0 \times 10^{-3} \times 5.0 \times 10^{21} = 1.5 \times 10^{19}\), then \(V_\mathrm{H}nt = 3.0 \times 10^{15}\), and \(B = \dfrac{3.0 \times 10^{15} \times 1.60 \times 10^{-19}}{15 \times 10^{-3}} = 3.2 \times 10^{-2}\,\mathrm{T}\). [A1] (b) A semiconductor has far fewer charge carriers per unit volume, so the Hall voltage is much larger and easier to measure. [B1]
Q: [7 marks] ★★★ Singly charged ions of neon-20 and neon-22 (masses 20 u and 22 u) pass through a velocity selector with an electric field of \(2.0 \times 10^{4}\,\mathrm{V\,m^{-1}}\) and a magnetic field of 0.20 T. They then enter a second region with a uniform field of 0.20 T at right angles to their velocity, and move in semicircles to a detector. (a) Show that the speed of the ions leaving the selector is \(1.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\). (b) Calculate the radius of the path of each ion. (c) Calculate the separation of the points where the two ions reach the detector.
H: In the selector, the electric and magnetic forces balance.
H: Use \(r = mv/BQ\) with the mass in kilograms. The ions land at the far end of a diameter.
H: The separation is the difference in diameters.
A: (a) The forces balance, \(QE = BQv\) [B1], so \(v = E/B = \dfrac{2.0 \times 10^{4}}{0.20} = 1.0 \times 10^{5}\,\mathrm{m\,s^{-1}}\). [A1] (b) \(r = \dfrac{mv}{BQ}\), so for neon-20: \(r = \dfrac{20 \times 1.66 \times 10^{-27} \times 1.0 \times 10^{5}}{0.20 \times 1.60 \times 10^{-19}}\) [C1] \(= 0.104\,\mathrm{m}\). [A1] Neon-22: \(r = 0.104 \times \dfrac{22}{20} = 0.114\,\mathrm{m}\). [A1] (c) After a semicircle each ion is a diameter from the entry point, so the separation is \(2(r_{22} - r_{20}) = 2 \times (0.1141 - 0.1038)\) [C1] \(= 2.1 \times 10^{-2}\,\mathrm{m}\). [A1]
Q: [3 marks] ★★★ Two long straight parallel wires carry currents of 5.0 A and 2.0 A in opposite directions. (a) State whether the force between them is attractive or repulsive. (b) Compare the magnitudes of the force on one wire and the force on the other, and explain your answer.
H: Each wire is in the field of the other.
A: (a) Repulsive: currents in opposite directions repel. [B1] (b) The forces are equal in magnitude (and opposite in direction), [B1] because the force on each wire is due to the field of the other, and the two forces are an interaction pair under Newton's third law, so the different sizes of the currents do not matter. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A proton moves in a circle in a uniform magnetic field of 1.2 T. (a) Show that the time for a half-circle is \(\pi m/BQ\), independent of the speed of the proton. (b) Calculate this time. (c) Calculate the radius of the path for protons moving at \(1.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\) and at \(2.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\), and comment on how this fact is used to accelerate particles in a cyclotron.
H: A half-circle has length \(\pi r\).
H: In a cyclotron the particles are given a small push by an alternating electric field each time they cross a gap.
A: (a) \(t = \dfrac{\pi r}{v} = \dfrac{\pi}{v} \times \dfrac{mv}{BQ} = \dfrac{\pi m}{BQ}\), and \(v\) has cancelled. [B1] (b) \(t = \dfrac{\pi \times 1.67 \times 10^{-27}}{1.2 \times 1.60 \times 10^{-19}}\) [C1] \(= 2.7 \times 10^{-8}\,\mathrm{s}\). [A1] (c) \(r = \dfrac{mv}{BQ} = 8.7 \times 10^{-3}\,\mathrm{m}\) for \(1.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\) [C1] and \(1.7 \times 10^{-2}\,\mathrm{m}\) for \(2.0 \times 10^{6}\,\mathrm{m\,s^{-1}}\). [A1] The faster proton moves on a circle twice as large but takes the same time for each half-circle, so a voltage alternating at a fixed frequency can give the protons a push every half-circle as they spiral outwards. [B1]
Q: [5 marks] ★★★ In a current balance, a wire with \(0.060\,\mathrm{m}\) of its length in a horizontal field is at right angles to the field. When the current is varied, the line of best fit of the change in balance reading \(\Delta m\) against current \(I\) passes through \((1.0\,\mathrm{A}, 0.37\,\mathrm{g})\) and \((5.0\,\mathrm{A}, 1.80\,\mathrm{g})\). (a) Explain why the balance reading changes. (b) Calculate the magnetic flux density.
H: Treat the force on the magnets as \(\Delta m\,g\), and find the gradient.
A: (a) The wire carries a current in the field, so it experiences a force. [B1] By Newton's third law the magnets feel an equal and opposite force, which changes the balance reading. [B1] (b) The gradient is \(\dfrac{(1.80 - 0.37) \times 10^{-3}}{5.0 - 1.0} = 3.575 \times 10^{-4}\,\mathrm{kg\,A^{-1}}\) [C1]. Since \(\Delta m\,g = BIL\), \(B = \dfrac{g \times \text{gradient}}{L} = \dfrac{9.81 \times 3.575 \times 10^{-4}}{0.060}\) [C1] \(= 5.8 \times 10^{-2}\,\mathrm{T}\). [A1]
:::

:::quiz
? Which of these experiences no magnetic force from a uniform magnetic field?
+ A proton at rest in the field
- An electron moving at right angles to the field
- A wire carrying a current at right angles to the field
- A proton moving at 45° to the field
> The magnetic force on a charge is \(BQv\sin\theta\), which is zero when \(v = 0\). A stationary charge feels no magnetic force. The other three all have a non-zero \(v\sin\theta\) or \(I\sin\theta\).
? A straight wire carrying a current is placed in a uniform magnetic field. For which angle between the wire and the field is the force largest?
+ 90°
- 0°
- 45°
- 180°
> \(F = BIL\sin\theta\) is largest when \(\sin\theta = 1\), at 90°. At 0° and 180° the wire is parallel to the field and \(F = 0\).
? A charged particle moves at right angles to a uniform magnetic field. What happens to its kinetic energy?
+ It stays the same.
- It increases.
- It decreases.
- It alternates between larger and smaller values.
> The force is always at right angles to the velocity, so it does no work. The speed and kinetic energy are constant, and only the direction changes.
? An electron enters a uniform magnetic field at right angles to the field. What is the shape of its path?
+ A circle
- A parabola
- A straight line
- A spiral that gets smaller and smaller
> The force has constant size and is always at right angles to the velocity: circular motion. A parabola is the path in a uniform *electric* field. A spiral would need the electron to lose energy.
? A proton moving at constant speed passes undeflected through crossed electric and magnetic fields. What happens to an alpha particle with the same speed?
+ It also passes undeflected.
- It is deflected towards the magnetic force.
- It is deflected towards the electric force.
- It stops.
> The condition \(QE = BQv\) gives \(v = E/B\), independent of \(Q\) and \(m\). Every particle with that speed goes straight through.
? A Hall probe uses a semiconductor rather than a copper slice because:
+ the semiconductor has far fewer charge carriers per unit volume, giving a larger Hall voltage.
- the semiconductor has a higher resistivity, so it gets hotter.
- copper is not affected by a magnetic field.
- the Hall voltage is larger in a metal.
> \(V_\mathrm{H} = BI/(ntq)\) is inversely proportional to \(n\). Copper is affected by the field just as much, but its huge \(n\) gives a minute \(V_\mathrm{H}\).
? Two long parallel wires carry currents in the same direction. What is the force between them?
+ Attractive, and equal in size on both wires.
- Repulsive, and equal in size on both wires.
- Attractive, and larger on the wire with the larger current.
- Repulsive, and larger on the wire with the smaller current.
> Parallel currents attract. The forces on the two wires are an interaction pair, so they are equal in size and opposite in direction, whatever the currents.
? A charged particle moves in a circle in a uniform magnetic field. The speed of the particle is doubled. What happens to the radius and the time for one circle?
+ The radius doubles and the period is unchanged.
- The radius doubles and the period doubles.
- The radius is unchanged and the period halves.
- The radius quadruples and the period is unchanged.
> \(r = mv/BQ\) is proportional to \(v\), so it doubles. The period \(T = 2\pi m/BQ\) does not depend on the speed: a faster particle goes on a larger circle at a higher speed, taking the same time.
:::

:::checklist What you can now do
- [ ] I can explain that a magnetic field is produced by moving charges or permanent magnets, and represent it with field lines, using the dot and cross notation.
- [ ] I can sketch the fields of a long straight wire, a flat circular coil and a long solenoid, and explain the effect of a ferrous core.
- [ ] I can recall and use \(F = BIL\sin\theta\), find the direction with Fleming's left-hand rule, and define the magnetic flux density and the tesla.
- [ ] I can describe how to measure a magnetic flux density with a current balance.
- [ ] I can recall and use \(F = BQv\sin\theta\), and find the direction of the force on positive and negative charges.
- [ ] I can describe and explain the circular path of a charged particle in a uniform field, and use \(r = mv/BQ\).
- [ ] I can explain how crossed electric and magnetic fields select a velocity, \(v = E/B\).
- [ ] I can explain the Hall voltage, derive and use \(V_\mathrm{H} = BI/(ntq)\), and describe how a Hall probe measures a flux density.
- [ ] I can explain the forces between current-carrying conductors and find their directions.
:::

:::recap
- A magnetic field is produced by moving charges (currents) or permanent magnets. Field lines are closed loops, closer together where the field is stronger. ⊙ is out of the page, ⊗ is into the page.
- Straight wire: concentric circles (right-hand grip rule). Flat coil: like a short bar magnet. Solenoid: uniform inside, like a bar magnet outside; a soft iron core strengthens it.
- \(F = BIL\sin\theta\), direction by Fleming's left-hand rule (first finger field, second finger conventional current, thumb force). The tesla is \(1\,\mathrm{N\,A^{-1}\,m^{-1}}\); the force is zero when the wire is parallel to the field.
- \(F = BQv\sin\theta\), at right angles to \(v\), so it does no work. For an electron, the conventional current is opposite to the velocity.
- In a uniform field at right angles to the velocity, the path is a circle with \(r = mv/BQ\) and period \(T = 2\pi m/BQ\), independent of speed.
- Velocity selector: \(QE = BQv\), so \(v = E/B\), whatever the charge or mass.
- Hall voltage \(V_\mathrm{H} = BI/(ntq)\): the carriers are pushed sideways until the electric force balances the magnetic force. Large in semiconductors (small \(n\)), tiny in metals. A Hall probe measures \(B\) with its face at right angles to the field.
- Parallel currents in the same direction attract and opposite currents repel, with equal and opposite forces on the two wires.
:::

:::links
- explore: [Magnet and Compass](https://phet.colorado.edu/en/simulations/magnet-and-compass) · PhET · move a compass around a bar magnet and see the field direction
- explore: [Faraday's Electromagnetic Lab](https://phet.colorado.edu/en/simulations/faradays-electromagnetic-lab) · PhET · explore the field of a magnet, a coil and an electromagnet
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the magnetic fields questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Electromagnetic induction](#phys.induction)
