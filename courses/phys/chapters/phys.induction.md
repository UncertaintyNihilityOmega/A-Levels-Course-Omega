@chapter phys.induction
@title Electromagnetic induction
@level a2
@paper CAIE P4 (A Level)
@time 5–7 hours
@summary Magnetic flux and flux linkage, the experiments that show a changing flux induces an e.m.f., Faraday's and Lenz's laws, the e.m.f. of a moving rod, flux–time and e.m.f.–time graphs, and how generators, transformers and eddy currents all follow from the same two laws.

:::why
A current in a wire makes a magnetic field. Induction is the reverse: a changing magnetic field makes an e.m.f. in a conductor. That one idea powers the generators in every power station, the transformers that carry the electricity to your home, the induction hob in a kitchen and the brakes on some trains. Faraday's and Lenz's laws are also conservation of energy at work, so the same reasoning lets you predict the size and the direction of every induced current in this chapter.
:::

**Before you start**, you need magnetic flux density, field patterns and the force \(F = BIL\) from [Magnetic fields](#phys.magnetic), and e.m.f. from [D.C. circuits](#phys.dc).

:::try Warm-up
Q: Define the tesla. (from [Magnetic fields](#phys.magnetic))
A: One tesla is the magnetic flux density of a uniform field in which a straight wire carrying a current of 1 A at right angles to the field experiences a force of 1 N per metre of its length. This comes from \(F = BIL\), so \(B = F/IL\).
Q: Define electromotive force (e.m.f.). (from [D.C. circuits](#phys.dc))
A: The energy transferred from other forms into electrical energy per unit charge by a source in driving charge around a complete circuit. It is measured in volts, \(1\,\mathrm{V} = 1\,\mathrm{J\,C^{-1}}\).
Q: A person pulls a trolley at a steady speed of \(0.50\,\mathrm{m\,s^{-1}}\) with a force of 12 N. At what rate do they transfer energy to it? (from [Work, energy and power](#phys.energy))
A: \(P = Fv = 12 \times 0.50 = 6.0\,\mathrm{W}\).
:::

## Magnetic flux

You already know that a magnetic field is drawn as field lines, and that the lines are closer together where the field is stronger. **Magnetic flux** counts how much of the field passes through a surface, like counting the lines that go through a hoop. A strong field through a large hoop gives a large flux. Tilt the hoop so that it faces away from the field and fewer lines pass through it, even though the field and the hoop are unchanged.

The magnetic flux density \(B\) is the flux per unit area at right angles to the field, which is where its other name, "flux density", comes from. Rearranging gives the flux itself.

:::def Magnetic flux
The product of the magnetic flux density and the cross-sectional area perpendicular to the direction of the magnetic flux density.
:::

:::def Weber (Wb)
The magnetic flux through an area of \(1\,\mathrm{m^2}\) that is perpendicular to a uniform magnetic flux density of \(1\,\mathrm{T}\). So \(1\,\mathrm{Wb} = 1\,\mathrm{T\,m^2}\).
:::

:::formula Magnetic flux
\[\Phi = BA \qquad\qquad \Phi = BA\cos\theta\]
\(\Phi\): magnetic flux (Wb) · \(B\): magnetic flux density (T) · \(A\): area of the surface (\(\mathrm{m^2}\)) · \(\theta\): angle between the field and the **normal** (the line at right angles) to the surface.
\(\Phi = BA\) holds when the surface is at right angles to the field (\(\theta = 0\)). The second form is the general one: only the part of the area at right angles to \(B\), which is \(A\cos\theta\), counts.
:::

:::html
<figure class="fig"><svg viewBox="25 25 445 195" role="img" aria-label="Horizontal field lines pointing right pass through a loop drawn side-on and tilted. A normal arrow n leaves the loop at an angle theta above the horizontal dashed line that shows the direction of the field."><path class="c1" d="M40 40H440" marker-end="url(#ah-phys)"/><path class="c1" d="M40 75H440" marker-end="url(#ah-phys)"/><path class="c1" d="M40 145H440" marker-end="url(#ah-phys)"/><path class="c1" d="M40 180H440" marker-end="url(#ah-phys)"/><path class="ln thick" d="M199.8 52.7L280.2 167.3"/><path class="ln-m thin dash" d="M240 110H330"/><path class="c2" d="M240 110L297.3 69.8" marker-end="url(#ah2-phys)"/><path class="ln thin" d="M285 110A45 45 0 0 0 276.9 84.2"/><text class="tl ti" x="302.9" y="94.2">θ</text><text class="tl ti tc" x="307.3" y="67.8">n</text><text class="tl ti" x="448" y="79">B</text><text class="tl" x="296" y="205">loop, side-on (area A)</text></svg><figcaption>A loop seen edge-on in a uniform field. The angle θ is between the field and the normal n to the loop. Tilting the loop reduces the number of field lines that pass through it, so the flux is \(BA\cos\theta\), and it falls to zero when the loop lies along the field.</figcaption></figure>
:::

:::eg A square coil of side 2.0 cm lies at right angles to a uniform field of flux density 0.25 T. Find the flux through it. What is the flux if the coil is turned so that its normal makes 60° with the field?
Area: \(A = 0.020^2 = 4.0 \times 10^{-4}\,\mathrm{m^2}\).
Facing the field: \(\Phi = BA = 0.25 \times 4.0 \times 10^{-4} = 1.0 \times 10^{-4}\,\mathrm{Wb}\). [C1] [A1]

Turned through 60°: \(\Phi = BA\cos 60^\circ = 1.0 \times 10^{-4} \times 0.50 = 5.0 \times 10^{-5}\,\mathrm{Wb}\). [A1]

Half the flux passes through, because \(\cos 60^\circ = 0.50\).
:::

:::warn Flux and flux density are different quantities
\(B\) (in T) says how strong the field is at a point. \(\Phi\) (in Wb) says how much field passes through a whole surface. A weak field through a huge area can have more flux than a strong field through a tiny one. Always check that the area in \(\Phi = BA\) is the one **at right angles** to the field.
:::

### Flux linkage

A coil with \(N\) turns is \(N\) loops in series, and the same flux \(\Phi\) passes through each loop. Each loop gets its own e.m.f., and because the loops are in series these e.m.f.s add. So what matters for a coil is not \(\Phi\) alone but \(N\Phi\).

:::def Magnetic flux linkage
The product of the magnetic flux through a coil and the number of turns of the coil: flux linkage \(= N\Phi\) (measured in Wb, sometimes written Wb-turns).
:::

:::eg A coil has 200 turns and each turn has area \(4.0 \times 10^{-4}\,\mathrm{m^2}\). It lies at right angles to a field of 0.25 T. Find the flux linkage.
\(\Phi = BA = 0.25 \times 4.0 \times 10^{-4} = 1.0 \times 10^{-4}\,\mathrm{Wb}\). [C1]

\(N\Phi = 200 \times 1.0 \times 10^{-4} = 2.0 \times 10^{-2}\,\mathrm{Wb}\). [A1]
:::

:::eg A rectangular coil of 50 turns measures 6.0 cm by 4.0 cm. It is in a field of 0.12 T whose direction makes an angle of 30° with the plane of the coil. Find the flux linkage.
The angle in \(\Phi = BA\cos\theta\) is between the field and the **normal**. The field is 30° from the plane, so it is \(90^\circ - 30^\circ = 60^\circ\) from the normal. [B1]

\(A = 0.060 \times 0.040 = 2.4 \times 10^{-3}\,\mathrm{m^2}\), so \(\Phi = 0.12 \times 2.4 \times 10^{-3} \times \cos 60^\circ = 1.44 \times 10^{-4}\,\mathrm{Wb}\). [C1]

\(N\Phi = 50 \times 1.44 \times 10^{-4} = 7.2 \times 10^{-3}\,\mathrm{Wb}\). [A1]

A common slip is to use the angle to the plane directly, which gives \(\cos 30^\circ\) and a flux that is too large.
:::

## Experiments that show induction

Faraday found that a steady magnetic field does nothing to a coil, however strong it is. An e.m.f. appears only while the magnetic flux linkage is **changing**. These three experiments show that, and show what controls the size and the direction of the e.m.f.

:::html
<figure class="fig small"><svg viewBox="25 20 315 210" role="img" aria-label="A bar magnet with its north pole facing a coil of five turns and moving towards it with velocity v. The coil is connected to a centre-zero meter below it."><rect class="f1 s-ink sw2" x="40" y="70" width="55" height="40"/><rect class="f2 s-ink sw2" x="95" y="70" width="55" height="40"/><text class="tb tc" x="67" y="95">N</text><text class="tb tc" x="122" y="95">S</text><path class="c1" d="M60 50H140" marker-end="url(#ah-phys)"/><text class="tl ta tc" x="100" y="42">v</text><path class="ln" d="M230 58A9 32 0 1 0 230 122A9 32 0 1 0 230 58"/><path class="ln" d="M250 58A9 32 0 1 0 250 122A9 32 0 1 0 250 58"/><path class="ln" d="M270 58A9 32 0 1 0 270 122A9 32 0 1 0 270 58"/><path class="ln" d="M290 58A9 32 0 1 0 290 122A9 32 0 1 0 290 58"/><path class="ln" d="M310 58A9 32 0 1 0 310 122A9 32 0 1 0 310 58"/><text class="tl tc" x="270" y="38">coil, N turns</text><path class="ln" d="M230 122V175H257M310 122V175H283"/><circle class="fp s-ink sw2" cx="270" cy="175" r="13"/><path class="ln thin" d="M270 185V166" marker-end="url(#ah)"/><text class="tl tc" x="270" y="212">centre-zero meter</text></svg><figcaption>Experiment 1. The meter deflects only while the magnet is moving, and the deflection reverses when the magnet is withdrawn.</figcaption></figure>
:::

:::lab Experiment 1: a magnet moving in and out of a coil
:::steps
1. Connect a coil of many turns to a sensitive **centre-zero** meter (a galvanometer, with zero in the middle of its scale so that it shows which way the current flows). There is no battery in the circuit.
2. Push the north pole of a bar magnet into the coil and hold it still. The meter deflects while the magnet moves, then returns to zero when the magnet stops, even though the magnet is still inside the coil.
3. Pull the magnet out. The meter deflects the **opposite** way, then returns to zero.
4. Repeat the push faster. The deflection is larger, but lasts for a shorter time.
5. Repeat with a coil with more turns, then with a stronger magnet. Each gives a larger deflection for the same speed.
6. Push in the south pole instead. The deflection reverses compared with step 2.
:::
:::

:::lab Experiment 2: a straight wire cutting field lines
:::steps
1. Place two magnets with opposite poles facing across a gap, so that the field between them is roughly uniform. Connect a short length of wire to a sensitive centre-zero meter with long flexible leads.
2. Move the wire **across** the gap, at right angles to the field lines (this is called cutting the field lines). The meter deflects while the wire moves.
3. Move the wire **along** the field lines, or hold it still. There is no deflection.
4. Move the wire across faster, or use stronger magnets, or a longer length of wire in the field. The deflection is larger each time.
5. Move the wire back the other way. The deflection reverses.
:::
:::

:::lab Experiment 3: two coils with no movement at all
:::steps
1. Wind two coils on the same iron core (or on a ring of iron). Connect the first coil to a battery through a switch, and the second coil to a centre-zero meter.
2. Close the switch. The meter gives a brief kick in one direction and returns to zero, although the current in the first coil is now steady.
3. Open the switch. The meter gives a brief kick in the **opposite** direction.
4. Replace the battery with a variable resistor and change the current steadily. A steady deflection appears for as long as the current is changing. With an alternating supply the meter would flicker continuously.
:::
:::

:::key What the experiments show
1. An e.m.f. is induced in a circuit only while the **magnetic flux linkage is changing**. A steady flux, however large, induces nothing. In experiment 3 nothing moves: the changing current changes the field, and so the flux through the second coil.
2. The e.m.f. is induced whether the flux changes because the magnet moves, the coil moves, the field changes strength, or the coil turns.
3. The **direction** of the e.m.f. reverses when the change reverses (pushing in against pulling out, switching on against switching off).
4. The **size** of the e.m.f. increases when the flux changes faster, when there are more turns, and when the field is stronger or the area larger.
:::

The iron core in experiment 3 carries the field of the first coil through the whole of the second coil, so that almost all of the flux links both coils. Without it the effect is much weaker, because the field spreads out into the air. This is also why a transformer has an iron core.

## Faraday's law and Lenz's law

The experiments say that the e.m.f. depends on how **fast** the flux linkage changes. Faraday's law makes that exact.

:::def Faraday's law of electromagnetic induction
The magnitude of the induced e.m.f. is equal (proportional) to the rate of change of magnetic flux linkage.
:::

The experiments also show that the direction reverses with the change. Lenz's law says which way it points.

:::def Lenz's law
The direction of the induced e.m.f. (and of any current it drives) is such as to oppose the change in flux that produces it.
:::

:::formula Faraday's and Lenz's laws combined
\[E = -\frac{\Delta(N\Phi)}{\Delta t} \qquad\text{or}\qquad E = -\frac{\mathrm{d}(N\Phi)}{\mathrm{d}t}\]
\(E\): induced e.m.f. (V) · \(N\Phi\): flux linkage (Wb) · \(t\): time (s). The size is \(|E| = \Delta(N\Phi)/\Delta t\), which is the **gradient** of a graph of flux linkage against time. The minus sign is Lenz's law: the induced e.m.f. opposes the change.
For constant \(N\), \(E = -N\,\Delta\Phi/\Delta t\). If the flux linkage changes at a steady rate, \(\Delta(N\Phi)/\Delta t\) is the e.m.f. itself; if the rate varies, it gives the **average** e.m.f. over the interval.
:::

:::eg A coil of 200 turns has area \(4.0 \times 10^{-4}\,\mathrm{m^2}\) and lies at right angles to a field. The flux density rises uniformly from 0 to 0.25 T in 0.050 s. Find the induced e.m.f.
Final flux linkage: \(N\Phi = N B A = 200 \times 0.25 \times 4.0 \times 10^{-4} = 2.0 \times 10^{-2}\,\mathrm{Wb}\). The initial flux linkage is zero. [C1]

\[E = \frac{\Delta(N\Phi)}{\Delta t} = \frac{2.0 \times 10^{-2}}{0.050} = 0.40\,\mathrm{V}\] [A1]

The e.m.f. is steady for as long as the field rises at a steady rate, and drops to zero the moment the field stops changing.
:::

:::eg A coil of 100 turns is in a magnetic field. The flux through each turn falls uniformly from \(5.0 \times 10^{-3}\,\mathrm{Wb}\) to \(1.0 \times 10^{-3}\,\mathrm{Wb}\) in 0.20 s. Calculate the e.m.f. induced in the coil.
The flux linkage falls from \(100 \times 5.0 \times 10^{-3} = 0.50\,\mathrm{Wb}\) to \(100 \times 1.0 \times 10^{-3} = 0.10\,\mathrm{Wb}\), a change of 0.40 Wb. [C1]

\[E = \frac{0.40}{0.20} = 2.0\,\mathrm{V}\] [A1]
:::

### Lenz's law is conservation of energy

Suppose the induced current went the **other** way. Push the north pole of a magnet towards a coil, and suppose the coil's nearer face became a south pole. It would pull the magnet in. The magnet would speed up, so the flux would change faster, so the current would be bigger, so the pull would be stronger. The magnet would accelerate with no one doing any work, while the current heated the wires: energy created from nothing. That cannot happen.

What really happens is that the nearer face of the coil becomes a **north** pole and **repels** the approaching magnet. You must do work pushing against that repulsion, and that work is the energy that appears as the electrical energy of the induced current. Pull the magnet away and the coil's face becomes a south pole that pulls it back, so again you do work. Every induced current takes its energy from whatever causes the change.

To find the direction of an induced current, work through these steps.

:::steps
1. Decide how the flux through the circuit is **changing**: increasing or decreasing, and in which direction it points.
2. The induced current must produce a field that **opposes the change**. If the flux is increasing, the induced field points the opposite way to the existing field. If the flux is decreasing, the induced field points the same way, to try to keep it up.
3. Use the right-hand grip rule on the loop (or the end-pole rule below) to find which way the current must flow to produce that field.
:::

The end-pole rule is quicker for a coil. Looking at one end of a coil, a current that flows **anticlockwise** makes that end a **north pole**, and a clockwise current makes it a south pole.

:::eg The north pole of a bar magnet is pulled away from one end of a coil. State the pole produced at that end of the coil, and the direction of the induced current as seen from the magnet's side.
The flux from the north pole through the coil is decreasing as the magnet moves away. The coil must oppose this by attracting the magnet back. [B1]

The end of the coil facing the magnet therefore becomes a **south** pole. [B1]

A south pole at the end that faces you means a **clockwise** current as seen from the magnet's side. [A1]

For comparison, pushing the north pole **towards** the coil makes the near end a north pole to repel it, so the current is anticlockwise as seen from the magnet.
:::

:::warn Lenz's law opposes the change, not the field
The induced field does not always point against the original field. If the flux is **decreasing**, the induced field points the **same** way as the original, because that opposes the decrease. Always ask "what is changing?" first.
:::

## A rod moving through a field

The simplest induced e.m.f. to calculate is in a straight conductor of length \(L\) moved at right angles to a uniform field \(B\) with speed \(v\). This is experiment 2 with numbers.

:::proof The e.m.f. of a moving rod: E = BLv
The rod moves a distance \(v\,\Delta t\) in a time \(\Delta t\), at right angles to \(B\) and along the rails that complete the circuit.
In this time it sweeps out an area \(\Delta A = L \times v\,\Delta t\), and the area enclosed by the circuit grows by this amount.
The change in flux through the circuit is \(\Delta\Phi = B\,\Delta A = BLv\,\Delta t\).
There is a single loop, so \(N = 1\) and Faraday's law gives \(E = \Delta\Phi/\Delta t\).
Hence \(E = BLv\).
Another view: each free electron in the rod moves with it at speed \(v\) across the field, and feels a magnetic force \(Bev\) along the rod. Doing work \(Bev \times L\) on each electron means an energy per unit charge of \(BLv\), which is the e.m.f.
:::

:::formula E.m.f. of a rod moving through a uniform field
\[E = BLv\]
\(E\): induced e.m.f. (V) · \(B\): flux density (T) · \(L\): length of rod in the field (m) · \(v\): speed (\(\mathrm{m\,s^{-1}}\)), with \(B\), \(L\) and \(v\) all at right angles to each other. If the rod is in a closed circuit of resistance \(R\), the current is \(I = E/R = BLv/R\).
:::

Notice how many things the induced current does. It flows round the circuit and heats the resistor. But a wire carrying a current in a magnetic field feels a force \(BIL\). Lenz's law says that this force must **oppose** the motion that caused the current. So to keep the rod moving at constant speed you must push it with a force equal to \(BIL\), and your push does work.

:::html
<figure class="fig"><svg viewBox="85 10 410 255" role="img" aria-label="Two horizontal rails joined at the left by a resistor R, with a vertical rod laid across them. A uniform field points into the page everywhere, shown by circles with crosses. The rod moves right with velocity v. An arrow F equal to BIL points left from the rod. The induced current I flows up the rod, left along the top rail, down through the resistor and right along the bottom rail."><path class="ln" d="M120 55H480M120 215H480"/><path class="ln" d="M120 55V92M120 138V215"/><rect class="fp s-ink sw2" x="112" y="92" width="16" height="46"/><text class="tl te" x="102" y="120">R</text><path class="ln thick" d="M320 55V215"/><circle class="fp s-ink sw1" cx="170" cy="88" r="8"/><path class="ln thin" d="M165.5 83.5L174.5 92.5M165.5 92.5L174.5 83.5"/><circle class="fp s-ink sw1" cx="220" cy="88" r="8"/><path class="ln thin" d="M215.5 83.5L224.5 92.5M215.5 92.5L224.5 83.5"/><circle class="fp s-ink sw1" cx="270" cy="88" r="8"/><path class="ln thin" d="M265.5 83.5L274.5 92.5M265.5 92.5L274.5 83.5"/><circle class="fp s-ink sw1" cx="370" cy="88" r="8"/><path class="ln thin" d="M365.5 83.5L374.5 92.5M365.5 92.5L374.5 83.5"/><circle class="fp s-ink sw1" cx="420" cy="88" r="8"/><path class="ln thin" d="M415.5 83.5L424.5 92.5M415.5 92.5L424.5 83.5"/><circle class="fp s-ink sw1" cx="460" cy="88" r="8"/><path class="ln thin" d="M455.5 83.5L464.5 92.5M455.5 92.5L464.5 83.5"/><circle class="fp s-ink sw1" cx="170" cy="178" r="8"/><path class="ln thin" d="M165.5 173.5L174.5 182.5M165.5 182.5L174.5 173.5"/><circle class="fp s-ink sw1" cx="220" cy="178" r="8"/><path class="ln thin" d="M215.5 173.5L224.5 182.5M215.5 182.5L224.5 173.5"/><circle class="fp s-ink sw1" cx="270" cy="178" r="8"/><path class="ln thin" d="M265.5 173.5L274.5 182.5M265.5 182.5L274.5 173.5"/><circle class="fp s-ink sw1" cx="370" cy="178" r="8"/><path class="ln thin" d="M365.5 173.5L374.5 182.5M365.5 182.5L374.5 173.5"/><circle class="fp s-ink sw1" cx="420" cy="178" r="8"/><path class="ln thin" d="M415.5 173.5L424.5 182.5M415.5 182.5L424.5 173.5"/><circle class="fp s-ink sw1" cx="460" cy="178" r="8"/><path class="ln thin" d="M455.5 173.5L464.5 182.5M455.5 182.5L464.5 173.5"/><path class="c1" d="M326 133H410" marker-end="url(#ah-phys)"/><text class="tl ta tc" x="368" y="125">v</text><path class="c2" d="M314 133H240" marker-end="url(#ah2-phys)"/><text class="tl ta2 tc" x="277" y="125">F = BIL</text><path class="c3" d="M250 37H190" marker-end="url(#ahr)"/><text class="tl tc" x="220" y="29">I</text><path class="c3" d="M190 233H250" marker-end="url(#ahr)"/><text class="tl tc" x="220" y="251">I</text></svg><figcaption>A rod of length L moves right at speed v through a uniform field pointing into the page (each circle with a cross). The flux through the circuit grows, so by Lenz's law the induced current flows anticlockwise, to make a field out of the page. The force BIL on the rod then points left, against the motion.</figcaption></figure>
:::

:::eg A metal rod 0.40 m long slides at \(3.0\,\mathrm{m\,s^{-1}}\) along two rails, at right angles to a uniform field of 0.50 T. The rails are joined by a \(2.0\,\Omega\) resistor, and the resistance of everything else is negligible. Find the e.m.f., the current, the force needed to keep the rod moving at constant speed, and the power you supply.
\(E = BLv = 0.50 \times 0.40 \times 3.0 = 0.60\,\mathrm{V}\). [C1] [A1]

\(I = E/R = 0.60/2.0 = 0.30\,\mathrm{A}\). [A1]

The force the field exerts on the rod is \(F = BIL = 0.50 \times 0.30 \times 0.40 = 0.060\,\mathrm{N}\), against the motion. You must supply an equal and opposite force of 0.060 N to keep the speed constant. [A1]

The power you supply is \(Fv = 0.060 \times 3.0 = 0.18\,\mathrm{W}\). [A1]

**Check:** the electrical power in the resistor is \(EI = 0.60 \times 0.30 = 0.18\,\mathrm{W}\), and \(I^2R = 0.30^2 \times 2.0 = 0.18\,\mathrm{W}\). Mechanical power in equals electrical power out.
:::

This is no coincidence. The mechanical power is \(Fv = (BIL)v = (BLv)I = EI\), the electrical power. The induced e.m.f. and the opposing force are two sides of the same energy transfer, and Lenz's law is what keeps the books balanced.

:::eg An aircraft with a wingspan of 30 m flies at \(250\,\mathrm{m\,s^{-1}}\) in a region where the vertical component of the Earth's field is \(4.0 \times 10^{-5}\,\mathrm{T}\). Find the e.m.f. between the wing tips. Why can you not light a lamp with it?
The wings cut the vertical field as they move horizontally, so \(E = BLv = 4.0 \times 10^{-5} \times 30 \times 250 = 0.30\,\mathrm{V}\). [C1] [A1]

A current needs a complete circuit. The e.m.f. appears across the wings, but there is no loop for it to drive a current round: connecting a wire from one wing tip to the other with a lamp would put that wire in the same field and moving with the aircraft, so it would have an equal e.m.f. of its own, and the two would cancel. [B1]
:::

:::warn Which rule for which job?
Two different things get muddled. To find the direction of the **force** on a current in a field (the motor effect, using the left-hand rule from [Magnetic fields](#phys.magnetic)) you start from a known current. To find the direction of an **induced** current you start from the change or the motion and use **Lenz's law**: ask what the induced current would do to the motion or to the flux, and make it oppose that. Then, if you need the force on that induced current, it is again the motor effect, and it must come out opposing the motion.
:::

## Flux linkage and e.m.f. graphs

Because \(E = -\Delta(N\Phi)/\Delta t\), the e.m.f. is minus the **gradient** of a flux-linkage–time graph. Whenever you see a graph of flux linkage, read the gradient. Where the line is flat, the e.m.f. is zero. Where it rises, the e.m.f. is negative (it opposes the rise); where it falls, positive.

A rectangular coil of 50 turns, 4.0 cm wide and 5.0 cm tall, is pulled at \(0.20\,\mathrm{m\,s^{-1}}\) through a region of uniform field \(0.30\,\mathrm{T}\) that is 12 cm wide and larger than the coil. The coil enters the field in 0.20 s, is completely inside it for 0.40 s, and takes 0.20 s to leave.

:::html
<figure class="fig"><svg viewBox="25 8 540 336" role="img" aria-label="Two stacked graphs sharing a time axis from 0 to 1.0 seconds. Top: flux linkage in webers rises in a straight line from 0 to 0.030 at 0.2 seconds, stays constant until 0.6 seconds, falls in a straight line to 0 at 0.8 seconds and then stays at zero. Bottom: e.m.f. in volts is minus 0.15 from 0 to 0.2 seconds, zero from 0.2 to 0.6 seconds, plus 0.15 from 0.6 to 0.8 seconds and zero afterwards."><path class="ax" d="M80 130H510M80 130V28"/><path class="c1 sw2" d="M80 130L164 40L332 40L416 130L500 130"/><text class="tl te" x="74" y="44">0.030</text><text class="tl te" x="74" y="134">0</text><text class="tl ti" x="88" y="22">NΦ / Wb</text><path class="ln-m thin dash" d="M164 40V130M332 40V130"/><path class="ax" d="M80 255H510M80 200V310"/><path class="c2 sw2" d="M80 300L164 300L164 255L332 255L332 210L416 210L416 255L500 255"/><text class="tl te" x="74" y="214">+0.15</text><text class="tl te" x="74" y="259">0</text><text class="tl te" x="74" y="304">−0.15</text><text class="tl ti" x="88" y="196">E / V</text><path class="ln-m thin dash" d="M164 135V300M332 135V300M416 135V300"/><text class="tl tc" x="122" y="291">entering</text><text class="tl tc" x="248" y="247">fully inside</text><text class="tl tc" x="374" y="231">leaving</text><path class="ax" d="M80 318H510"/><path class="ax" d="M80 318V323"/><text class="ts tc" x="80" y="336">0</text><path class="ax" d="M164 318V323"/><text class="ts tc" x="164" y="336">0.2</text><path class="ax" d="M248 318V323"/><text class="ts tc" x="248" y="336">0.4</text><path class="ax" d="M332 318V323"/><text class="ts tc" x="332" y="336">0.6</text><path class="ax" d="M416 318V323"/><text class="ts tc" x="416" y="336">0.8</text><path class="ax" d="M500 318V323"/><text class="ts tc" x="500" y="336">1.0</text><text class="tl" x="516" y="322">t / s</text></svg><figcaption>A coil crossing a region of uniform field at constant speed. The e.m.f. (lower graph) is minus the gradient of the flux linkage (upper graph): steady and negative while the flux linkage rises, zero while it is constant, steady and positive while it falls.</figcaption></figure>
:::

:::eg Use the graphs to find the e.m.f. while the coil enters the field, and check it using \(E = NBhv\), where \(h\) is the height of the coil.
While entering, the flux linkage rises from 0 to 0.030 Wb in 0.20 s: \(0.030 = 50 \times 0.30 \times (0.040 \times 0.050)\), the full flux linkage when the whole coil is inside. [C1]

\[|E| = \frac{0.030}{0.20} = 0.15\,\mathrm{V}\] [A1]

The sign is negative because the flux linkage is rising. [B1]

Check with the rod formula: only the leading edge of height \(h = 0.050\,\mathrm{m}\) is cutting the field. Each of the 50 turns gives \(BLv\), so \(E = N B h v = 50 \times 0.30 \times 0.050 \times 0.20 = 0.15\,\mathrm{V}\). The two methods agree.

While the coil is completely inside, both sides of the coil cut field lines, but the two e.m.f.s cancel round the loop, and the flux linkage is constant, so \(E = 0\). The e.m.f. is positive on leaving, since the flux linkage is falling.
:::

:::key The area under an e.m.f.–time graph
Since \(E\,\Delta t = -\Delta(N\Phi)\), the **area** under an e.m.f.–time graph is minus the **change in flux linkage**, so it does not depend on how fast the change happens. In the graph above, each pulse has an area of \(0.15 \times 0.20 = 0.030\,\mathrm{V\,s}\), which is the whole flux linkage of the coil. (Note that \(1\,\mathrm{V\,s} = 1\,\mathrm{Wb}\).)
:::

### A magnet falling through a coil

Drop a bar magnet vertically through a coil. As it approaches, the flux linkage rises, reaches a maximum when the magnet is at the middle of the coil, and falls again as the magnet leaves. The e.m.f. is minus the gradient: first one sign, zero at the middle, then the other sign.

:::plot The e.m.f. induced as a magnet falls through a coil. The two pulses have opposite signs. The second is taller and narrower, because the magnet is moving faster by then; the areas are equal.
--f "0-50*exp(0-((x-0.30)/0.08)**2)+80*exp(0-((x-0.62)/0.05)**2)+0*sqrt(0.95-x)" --x 0 1.1 --y -75 110 --xlabel "t / s" --ylabel "E / mV" --pt "0.30,-50,first pulse@s" --pt "0.62,80,second pulse@w"
:::

Read the graph in order. The first pulse is negative because the flux linkage is **increasing** as the magnet enters. Between the pulses, when the magnet is at the middle of the coil, the flux linkage is at its maximum and not changing, so the e.m.f. passes through zero. The second pulse has the opposite sign because the flux linkage is **decreasing**. The magnet is accelerating, so it passes through the second half of the coil faster than the first: the pulse is taller and shorter. The two areas are equal, because each equals the same change in flux linkage (from zero to its maximum, and back again).

:::eg A magnet is dropped through a coil. Describe and explain the e.m.f.–time graph.
Flux linkage increases as the magnet enters, so an e.m.f. is induced; by Faraday's law its size is the rate of change of flux linkage. [B1]

The e.m.f. is zero when the magnet is at the centre of the coil, because the flux linkage is at a maximum and not changing. [B1]

The second pulse is of opposite sign, because the flux linkage is now decreasing. [B1]

The second pulse is larger in peak value and shorter, because the magnet is travelling faster (it has accelerated under gravity). [B1]

The areas under the two pulses are equal, because both equal the same change in flux linkage. [B1]
:::

## Generators, transformers and eddy currents

### The generator

An alternating current generator turns a coil in a magnetic field. As the coil rotates, the angle between its normal and the field changes, so the flux through it changes, and an e.m.f. is induced.

:::proof The e.m.f. of a rotating coil
A flat coil of \(N\) turns and area \(A\) rotates at constant angular speed \(\omega\) in a uniform field \(B\). Take \(t = 0\) when its normal points along the field.
At time \(t\) the normal has turned through \(\theta = \omega t\), so the flux through each turn is \(\Phi = BA\cos\omega t\).
The flux linkage is \(N\Phi = NBA\cos\omega t\).
By Faraday's and Lenz's laws, \(E = -\dfrac{\mathrm{d}(N\Phi)}{\mathrm{d}t}\) and the derivative of \(\cos\omega t\) is \(-\omega\sin\omega t\).
So \(E = NBA\omega\sin\omega t\).
The peak value is \(E_0 = BAN\omega\), and the e.m.f. alternates sinusoidally with frequency \(f = \omega/2\pi\).
:::

:::plot The flux linkage and the e.m.f. of a coil turning at 50 Hz, each divided by its maximum. The e.m.f. is largest when the flux linkage passes through zero, where the flux changes most rapidly.
--f "cos(2*pi*x/20)+0*sqrt(20-x)" --f "sin(2*pi*x/20)+0*sqrt(20-x)" --x 0 23 --y -1.4 2.4 --xlabel "t / ms" --ylabel "value / maximum" --label "flux linkage NΦ" --label "e.m.f. E" --legend tr
:::

The e.m.f. is a maximum when the coil is **parallel** to the field. In that position no flux passes through it (\(\Phi = 0\)), but the flux is changing fastest, because the coil edges are cutting straight across the field lines. When the coil is at right angles to the field the flux is at its maximum and the e.m.f. is zero. This sin and cos pairing is what you saw in the graph above.

:::eg A coil of 200 turns and area \(0.020\,\mathrm{m^2}\) rotates at 50 Hz in a uniform field of 0.15 T. Find the peak e.m.f.
\(\omega = 2\pi f = 2\pi \times 50 = 314\,\mathrm{rad\,s^{-1}}\). [C1]

\(E_0 = BAN\omega = 0.15 \times 0.020 \times 200 \times 314.16 = 188.5\,\mathrm{V}\) (using the unrounded \(\omega\)), which is \(1.9 \times 10^{2}\,\mathrm{V}\) to 2 significant figures. [A1]

The e.m.f. alternates between \(+1.9 \times 10^2\,\mathrm{V}\) and \(-1.9 \times 10^2\,\mathrm{V}\). You can raise it by spinning faster, using a stronger field or more turns, or making the coil larger. [Alternating currents](#phys.ac) shows how to describe this e.m.f. and its power.
:::

### Transformers

A transformer is experiment 3 turned into a machine. A primary coil and a secondary coil are wound on a closed iron core. An **alternating** current in the primary makes a flux in the core that is constantly changing, and the iron guides almost all of this flux through the secondary. By Faraday's law, an alternating e.m.f. is induced in the secondary. If the secondary has more turns than the primary, it gives a larger e.m.f.; fewer turns, a smaller one.

A steady direct current would not work: with steady current the flux is constant, and no e.m.f. is induced. This is why transformers need alternating current, and why electricity is distributed as alternating current. Power stations use transformers to raise the voltage so that the current in the long cables is small, and the \(I^2R\) heating in the cables is small too; transformers near your home lower it again. The turns-ratio rule \(V_s/V_p = N_s/N_p\) from IGCSE follows from the same flux passing through every turn of both coils. The learning outcomes for 9702 do not list it, so be ready to **explain** a transformer in terms of flux, rather than to quote it.

### Eddy currents

Flux change does not need a wire. Any lump of conductor in a changing field has e.m.f.s induced in it, and because the metal is a solid block of low resistance, they drive large circulating currents called **eddy currents**. By Lenz's law, the eddy currents oppose the change that produces them, and they heat the metal.

- **Laminated cores.** The iron cores of transformers are made of thin sheets, insulated from each other, so that eddy currents are confined to small loops and cannot waste much energy as heat.
- **Induction hobs.** A coil under the hob carries a high-frequency alternating current. The changing field induces eddy currents in the base of the iron or steel pan, and these heat the pan. The hob itself stays cool, and no heat is produced if the pan is lifted away.
- **Magnetic braking.** A conducting plate moving between the poles of magnets has eddy currents induced in it. The force on these currents opposes the motion, and the plate slows without any contact, converting kinetic energy into thermal energy. The faster it moves, the larger the force.

:::lab A magnet falling through a pipe
:::steps
1. Hold a copper pipe vertically. Drop a small cylindrical magnet down it and time the fall with a stopwatch. Repeat with a plastic pipe of the same size, and with a non-magnetic object of the same size and mass as a control.
2. The magnet takes noticeably longer to fall through the copper pipe. In the plastic pipe, and for the control, it falls in about the time expected for free fall.
3. Repeat with a copper pipe that has a slit cut down its length: the slit breaks the eddy-current loops, and the magnet falls much faster.
4. Explanation: as the magnet falls, the flux through each section of the pipe wall changes, so e.m.f.s are induced in the copper and drive eddy currents round the pipe. By Lenz's law, the current's field opposes the motion of the magnet, so there is an upward force. The force grows with speed, so the magnet reaches a steady terminal speed when it equals the weight.
:::
:::

:::board
Other boards teach these laws in the same way, and AQA and OCR also use the e.m.f. of a rotating coil and the transformer equation, \(N_s/N_p = V_s/V_p\). Cambridge's learning outcomes for this topic are the flux, flux linkage, experiments, Faraday's law and Lenz's law covered here. Some UK specifications write the combined law as \(\varepsilon = -N\,\mathrm{d}\Phi/\mathrm{d}t\); it is the same law with a different symbol for e.m.f.
:::

:::eg Spot the error: the flux through each turn of a 100-turn coil falls uniformly from 5.0 × 10⁻³ Wb to 1.0 × 10⁻³ Wb in 0.20 s. Calculate the induced e.m.f.
A student wrote this answer.

Line 1: change in flux \(= 5.0 \times 10^{-3} - 1.0 \times 10^{-3} = 4.0 \times 10^{-3}\,\mathrm{Wb}\)
Line 2: \(E = \dfrac{\Delta\Phi}{\Delta t} = \dfrac{4.0 \times 10^{-3}}{0.20}\)
Line 3: \(E = 0.020\,\mathrm{V}\)

Line 1 is correct. **Line 2 is wrong: it uses the flux through one turn and forgets that the coil has 100 turns.** Faraday's law needs the flux **linkage**, \(N\Phi\). The substitution mark is lost, and so is the answer mark. [C0] [A0]

Correct working: \(E = \dfrac{N\,\Delta\Phi}{\Delta t} = \dfrac{100 \times 4.0 \times 10^{-3}}{0.20}\) [C1] \(= 2.0\,\mathrm{V}\). [A1]

Check: an e.m.f. of only 0.020 V from a 100-turn coil is 100 times too small, which is what you get when you ignore \(N\).
:::

:::try Start easy, finish at exam standard
Q: A square coil of side 5.0 cm lies at right angles to a uniform field of 0.40 T. Find the flux through it.
A: \(A = 0.050^2 = 2.5 \times 10^{-3}\,\mathrm{m^2}\), so \(\Phi = BA = 0.40 \times 2.5 \times 10^{-3} = 1.0 \times 10^{-3}\,\mathrm{Wb}\).
Q: A coil of 120 turns has a flux of \(3.5 \times 10^{-4}\,\mathrm{Wb}\) through each turn. What is the flux linkage?
A: \(N\Phi = 120 \times 3.5 \times 10^{-4} = 4.2 \times 10^{-2}\,\mathrm{Wb}\).
Q: The flux linkage of a coil rises uniformly from 0 to 0.060 Wb in 0.40 s. Find the induced e.m.f.
A: \(E = \Delta(N\Phi)/\Delta t = 0.060/0.40 = 0.15\,\mathrm{V}\).
Q: A coil of one turn and area \(3.0 \times 10^{-3}\,\mathrm{m^2}\) is in a field of 0.20 T. The normal to the coil makes 30° with the field. Find the flux through it.
A: \(\Phi = BA\cos\theta = 0.20 \times 3.0 \times 10^{-3} \times \cos 30^\circ = 5.2 \times 10^{-4}\,\mathrm{Wb}\).
Q: A magnet is held still inside a coil connected to a sensitive meter. Why does the meter read zero?
A: The magnetic flux linkage is not changing, and an e.m.f. is only induced while the flux linkage changes.
Q: A wire 0.15 m long moves at \(4.0\,\mathrm{m\,s^{-1}}\) at right angles to a uniform field of 0.30 T, and at right angles to its own length. Find the e.m.f. between its ends.
A: \(E = BLv = 0.30 \times 0.15 \times 4.0 = 0.18\,\mathrm{V}\).
Q: The south pole of a bar magnet is pushed towards one end of a coil. State the direction of the induced current as seen from the magnet's side.
A: The coil opposes the approach of the south pole by making the nearer end a south pole. A south pole means a clockwise current as seen from that end, so the current is **clockwise** as seen from the magnet.
Q: Explain why the direction of an induced current must follow Lenz's law if energy is conserved.
A: If the induced current helped the change instead of opposing it (for example by pulling a magnet into a coil), the change would speed up, the current would grow and so on, so energy would be produced with no work done. Opposing the change means that work must be done against the induced force, and this work is the source of the electrical energy.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Define magnetic flux and magnetic flux linkage.
A: Magnetic flux is the product of the magnetic flux density and the cross-sectional area perpendicular to the direction of the field. [B1] Flux linkage is the product of the flux through a coil and the number of turns of the coil. [B1]
Q: [2 marks] ★ State Faraday's law of electromagnetic induction.
A: The induced e.m.f. is directly proportional to (equal to) [B1] the rate of change of magnetic flux linkage. [B1]
Q: [3 marks] ★★ The north pole of a bar magnet is pushed towards one end of a coil that is connected to a sensitive meter. State the polarity produced at that end of the coil and the direction of the induced current as seen from the magnet. Use the idea of energy to explain why this is the direction.
A: The end of the coil becomes a north pole. [B1] The current is anticlockwise as seen from the magnet. [B1] The induced pole repels the magnet, so work has to be done in pushing it in; this work is transferred into the electrical energy of the current. If the pole attracted the magnet instead, energy would be created from nothing. [B1]
Q: [3 marks] ★★ The flux linkage of a coil falls uniformly from 0.048 Wb to 0.012 Wb in 0.15 s, and then stays constant. Calculate the e.m.f. induced during the fall, and state the e.m.f. after it.
A: \(E = \dfrac{\Delta(N\Phi)}{\Delta t} = \dfrac{0.048 - 0.012}{0.15}\) [C1] \(= 0.24\,\mathrm{V}\). [A1] After the fall the flux linkage is not changing, so the e.m.f. is zero. [B1]
Q: [6 marks] ★★ A metal rod of length 0.25 m slides at a steady speed of \(2.4\,\mathrm{m\,s^{-1}}\) along horizontal rails, at right angles to a vertical uniform field of 0.40 T. The rails and rod form a circuit of total resistance \(1.5\,\Omega\). (a) Calculate the induced e.m.f. (b) Calculate the current. (c) Calculate the force needed to keep the rod moving at constant speed. (d) Calculate the power needed to do this.
A: (a) \(E = BLv = 0.40 \times 0.25 \times 2.4\) [C1] \(= 0.24\,\mathrm{V}\). [A1] (b) \(I = E/R = 0.24/1.5 = 0.16\,\mathrm{A}\). [A1] (c) \(F = BIL = 0.40 \times 0.16 \times 0.25\) [C1] \(= 0.016\,\mathrm{N}\). [A1] (d) \(P = Fv = 0.016 \times 2.4 = 0.038\,\mathrm{W}\) (equal to \(I^2R\)). [A1]
Q: [5 marks] ★★★ A bar magnet is released from rest above a coil and falls vertically through the coil, which is connected to a data logger. Sketch the graph of induced e.m.f. against time, and explain its shape, including the relative sizes of any peaks.
H: Think of the flux linkage first: where is it increasing, constant and decreasing?
H: The magnet accelerates under gravity as it falls. What does that do to the two peaks?
A: There are two pulses, of opposite sign (one positive, one negative). [B1] The e.m.f. is zero when the magnet is at the centre of the coil, where the flux linkage is at its maximum and not changing. [B1] The pulses have opposite signs because the flux linkage first increases and then decreases. [B1] The second pulse has a larger peak and is shorter, because the magnet is moving faster. [B1] The areas under the two pulses are equal, because each equals the same change in flux linkage. [B1]
Q: [6 marks] (#phys.magnetic) ★★★ A rectangular coil of 120 turns, 5.0 cm by 8.0 cm, rotates at 25 revolutions per second in a uniform field of flux density 0.20 T. (a) Calculate the angular speed of the coil. (b) Calculate the maximum e.m.f. induced. (c) State the position of the coil, relative to the field, at which the e.m.f. is a maximum, and explain why it is a maximum there.
H: The maximum e.m.f. is \(E_0 = BAN\omega\), from the proof in the chapter.
H: At the maximum e.m.f. the flux through the coil is not at a maximum.
A: (a) \(\omega = 2\pi f = 2\pi \times 25\) [C1] \(= 157\,\mathrm{rad\,s^{-1}}\). [A1] (b) \(A = 0.050 \times 0.080 = 4.0 \times 10^{-3}\,\mathrm{m^2}\), so \(E_0 = BAN\omega = 0.20 \times 4.0 \times 10^{-3} \times 120 \times 157\) [C1] \(= 15\,\mathrm{V}\). [A1] (c) The plane of the coil is parallel to the field. [B1] The flux through it is zero there, but is changing at its greatest rate (the sides cut straight across the field lines), and the e.m.f. is the rate of change of flux linkage. [B1]
Q: [5 marks] ★★★ A small magnet falls through a vertical copper pipe much more slowly than through a plastic pipe of the same size. Explain why, and explain why the magnet reaches a constant speed in the copper pipe.
H: Copper conducts. What can the changing flux do to the wall of the pipe?
A: The flux through the wall of the pipe changes as the magnet falls past. [B1] This induces an e.m.f., which drives circulating (eddy) currents in the copper. [B1] By Lenz's law the field of these currents opposes the motion of the magnet, so there is an upward force on it. [B1] The faster the magnet moves, the larger the e.m.f., current and upward force, so it reaches a speed at which this force equals its weight and the resultant force is zero (terminal speed). [B1] The energy that the magnet loses is transferred as thermal energy in the pipe. [B1]
:::

:::try Stretch for A*
Q: [9 marks] ★★★ A square loop of side 0.10 m and resistance \(0.50\,\Omega\) is pulled at constant speed \(2.0\,\mathrm{m\,s^{-1}}\) in the plane of the page, so that it enters a region of uniform field 0.40 T that is 0.30 m wide and acts into the page. The loop starts just outside the field, with its leading edge at the edge of the region at \(t = 0\). (a) Calculate the e.m.f. while the loop is entering the field. (b) Calculate the current and the force that must be applied to the loop during this time. (c) Calculate the energy dissipated as the loop enters the field, and show that it equals the work done by the applied force. (d) Describe the graphs of e.m.f. and of applied force against time from \(t = 0\) to \(t = 0.20\,\mathrm{s}\).
H: Only the leading edge is in the field while the loop enters; use \(E = BLv\) with \(L = 0.10\,\mathrm{m}\).
H: How long does the leading edge take to cross the 0.30 m region, and when does the trailing edge leave?
A: (a) \(E = BLv = 0.40 \times 0.10 \times 2.0\) [C1] \(= 0.080\,\mathrm{V}\). [A1] (b) \(I = E/R = 0.080/0.50 = 0.16\,\mathrm{A}\). [A1] \(F = BIL = 0.40 \times 0.16 \times 0.10\) [C1] \(= 6.4 \times 10^{-3}\,\mathrm{N}\). [A1] (c) The loop takes \(0.10/2.0 = 0.050\,\mathrm{s}\) to enter. Energy dissipated \(= I^2Rt = 0.16^2 \times 0.50 \times 0.050\) [C1] \(= 6.4 \times 10^{-4}\,\mathrm{J}\). [A1] The work done by the force is \(F \times d = 6.4 \times 10^{-3} \times 0.10 = 6.4 \times 10^{-4}\,\mathrm{J}\), the same. (d) For \(0 < t < 0.05\,\mathrm{s}\) the e.m.f. is constant at 0.080 V and the force is constant at 6.4 mN. For \(0.05 < t < 0.15\,\mathrm{s}\) the whole loop is in the field, the flux is constant, and both are zero. For \(0.15 < t < 0.20\,\mathrm{s}\) the loop is leaving: the e.m.f. is 0.080 V in the **opposite** direction, but the force is again 6.4 mN **against the motion**, because the force always opposes the movement. [B1] [B1] The total energy dissipated is \(2 \times 6.4 \times 10^{-4} = 1.3 \times 10^{-3}\,\mathrm{J}\).
Q: [6 marks] ★★★ A metal rod of mass 0.020 kg and length 0.30 m falls under gravity, with its ends in contact with two long vertical rails joined at the bottom, so that the rod and rails form a circuit of resistance \(0.10\,\Omega\). A horizontal uniform field of 0.50 T is at right angles to the plane of the rails. Friction is negligible. (a) Explain why the rod reaches a terminal speed. (b) Calculate the current when it is falling at terminal speed. (c) Calculate the terminal speed. (d) Show that the rate of loss of gravitational potential energy equals the power dissipated in the circuit.
H: At terminal speed the magnetic force \(BIL\) equals the weight.
H: Once you have the current, find the e.m.f. from \(E = IR\), then use \(E = BLv\).
A: (a) As the rod speeds up the induced e.m.f. and current increase, so the upward force \(BIL\) increases until it equals the weight; the resultant force is then zero. [B1] (b) \(mg = BIL\), so \(I = \dfrac{0.020 \times 9.81}{0.50 \times 0.30}\) [C1] \(= 1.3\,\mathrm{A}\). [A1] (c) \(E = IR = 1.308 \times 0.10 = 0.131\,\mathrm{V}\), and \(v = \dfrac{E}{BL} = \dfrac{0.131}{0.50 \times 0.30}\) [C1] \(= 0.87\,\mathrm{m\,s^{-1}}\). [A1] (d) \(mgv = 0.020 \times 9.81 \times 0.872 = 0.171\,\mathrm{W}\) and \(I^2R = 1.308^2 \times 0.10 = 0.171\,\mathrm{W}\). [B1]
:::

:::quiz
? What is the unit of magnetic flux, the weber, in terms of other units?
+ \(\mathrm{T\,m^2}\)
- \(\mathrm{T\,m^{-2}}\)
- \(\mathrm{T\,m}\)
- \(\mathrm{N\,A^{-1}\,m^{-1}}\)
> Flux is \(BA\), so its unit is \(\mathrm{T\,m^2}\). \(\mathrm{T\,m^{-2}}\) mixes the two up, and \(\mathrm{N\,A^{-1}\,m^{-1}}\) is the unit of \(B\) itself (the tesla), not of flux.
? A coil has \(N\) turns, each of area \(A\), at right angles to a uniform field \(B\). What is its flux linkage?
+ \(NBA\)
- \(BA\)
- \(BA/N\)
- \(NB/A\)
> Flux linkage is the number of turns times the flux through each turn, and the flux is \(BA\). The expression \(BA\) forgets the turns, which is the commonest mistake in induction questions.
? Which situation induces an e.m.f. in a coil?
- A strong magnet held still inside the coil
- A steady direct current in a nearby coil
- The coil at rest in a strong uniform field
+ A magnet moving into the coil
> An e.m.f. is induced only while the flux linkage is changing. A strong or steady field does nothing; a moving magnet changes the flux through the coil.
? The north pole of a magnet approaches one end of a coil. What pole does that end of the coil become?
+ A north pole
- A south pole
- No pole at all
- A south pole first, then a north pole
> The coil opposes the approach, so it repels the north pole with its own north pole. A south pole would attract the magnet and speed up the change, which breaks conservation of energy.
? A rod moves through a uniform field at speed \(v\). The speed is doubled and the field is halved. What happens to the e.m.f. \(E = BLv\)?
+ It stays the same.
- It doubles.
- It halves.
- It becomes four times larger.
> The two changes cancel: \(B \to B/2\) and \(v \to 2v\) leave \(BLv\) unchanged.
? A rod carrying an induced current is moving through a magnetic field. The magnetic force on the current in the rod is
+ opposite to the rod's velocity.
- in the same direction as the rod's velocity.
- zero, because the e.m.f. is induced.
- at right angles to the rod's velocity.
> By Lenz's law the force opposes the motion, otherwise the rod would speed up for free and the energy of the current would come from nowhere. The force lies along the line of motion, not across it.
? A coil rotates at constant speed in a uniform field. When is the induced e.m.f. a maximum?
+ When the plane of the coil is parallel to the field
- When the plane of the coil is at right angles to the field
- When the flux through the coil is a maximum
- It is the same at all times
> The e.m.f. is the rate of change of flux linkage, and this is greatest when the flux passes through zero, with the coil parallel to the field. When the flux is at its maximum its rate of change is zero.
? A magnet falls much more slowly through a copper pipe than through a plastic pipe. What is the reason?
+ Eddy currents in the copper produce a force that opposes the motion.
- Copper is magnetic and attracts the magnet upwards.
- The copper pipe has a smaller diameter, so there is more air resistance.
- The pipe shields the magnet from gravity.
> The falling magnet induces e.m.f.s in the copper, which drive eddy currents. By Lenz's law, these oppose the motion. Plastic is an insulator, so no current flows and nothing slows the magnet.
:::

:::checklist What you can now do
- [ ] I can define magnetic flux and the weber, and use \(\Phi = BA\) (and \(BA\cos\theta\) for a tilted surface).
- [ ] I can define and use magnetic flux linkage \(N\Phi\).
- [ ] I can describe experiments that show a changing flux induces an e.m.f., that it opposes the change, and what affects its size.
- [ ] I can state and use Faraday's law and Lenz's law, \(E = -\Delta(N\Phi)/\Delta t\), including finding the direction of an induced current.
- [ ] I can use \(E = BLv\) for a moving rod and explain the force that opposes the motion in terms of energy.
- [ ] I can interpret flux-linkage–time and e.m.f.–time graphs, including the area and gradient.
- [ ] I can explain qualitatively how a generator, a transformer and eddy currents work.
:::

:::recap
- Magnetic flux \(\Phi = BA\) (area at right angles to \(B\); \(BA\cos\theta\) for a tilted surface), in webers (\(1\,\mathrm{Wb} = 1\,\mathrm{T\,m^2}\)). Flux linkage is \(N\Phi\).
- An e.m.f. is induced only while the flux linkage **changes**. It is larger for a faster change, more turns and a stronger field, and it reverses when the change reverses.
- Faraday: the magnitude of the induced e.m.f. equals the rate of change of flux linkage, \(E = \Delta(N\Phi)/\Delta t\), the gradient of the flux-linkage graph. Lenz: the induced e.m.f. opposes the change producing it (the minus sign), which is conservation of energy.
- A rod moving at right angles to a field has \(E = BLv\); the induced current gives a force \(BIL\) against the motion, and mechanical power \(Fv\) equals electrical power \(EI\).
- The area under an e.m.f.–time graph is minus the change in flux linkage. A magnet falling through a coil gives two pulses of opposite sign and equal area, the second taller and shorter.
- A coil rotating in a field has \(E = BAN\omega\sin\omega t\), a maximum when the coil is parallel to the field. Transformers work only with changing flux, so they need alternating current; eddy currents oppose changes in flux and heat conductors.
:::

:::links
- explore: [Faraday's Law](https://phet.colorado.edu/en/simulations/faradays-law) · PhET · move a magnet through a coil and see the e.m.f. and the lamp respond
- explore: [Faraday's Electromagnetic Lab](https://phet.colorado.edu/en/simulations/faradays-electromagnetic-lab) · PhET · build a generator and a transformer
- papers: [9702 Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-4/) · Physics & Maths Tutor · find the induction questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Alternating currents](#phys.ac)
