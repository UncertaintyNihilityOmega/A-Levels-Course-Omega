@chapter phys.energy
@title Work, energy and power
@level as
@paper CAIE P1 · P2 (AS)
@time 5–7 hours
@summary Work done by a force, the conservation of energy, gravitational potential energy and kinetic energy (with both formulae derived), efficiency, and power including P = Fv, with worked problems on falling objects, slopes, braking cars and power stations.

:::why
Energy is the single most useful idea in physics because it is conserved: whatever happens to a system, the total never changes, so you can often solve a problem without knowing the details of the motion. Work, efficiency and power then tell you what a real machine achieves, from a phone charger to a hydroelectric dam. Every later topic, from gases to quantum physics, uses the energy ideas in this chapter.
:::

**Before you start**, you need the equations of motion from [Kinematics](#phys.kinematics) and \(F = ma\) from [Dynamics and momentum](#phys.dynamics).

:::try Warm-up
Q: A car accelerates from rest at \(2.5\,\mathrm{m\,s^{-2}}\) over a distance of 40 m. Find its final speed. (from [Kinematics](#phys.kinematics))
A: \(v^2 = u^2 + 2as = 0 + 2 \times 2.5 \times 40 = 200\), so \(v = 14\,\mathrm{m\,s^{-1}}\) (14.1 before rounding to 2 significant figures).
Q: A resultant force of 3000 N acts on a car of mass 1200 kg. Find its acceleration. (from [Dynamics and momentum](#phys.dynamics))
A: \(a = F/m = 3000/1200 = 2.5\,\mathrm{m\,s^{-2}}\).
Q: A force of 50 N acts at 60° above the horizontal. Find its horizontal component. (from [Forces, density and pressure](#phys.forces))
A: \(F\cos 60^\circ = 50 \times 0.5 = 25\,\mathrm{N}\).
:::

## Energy: the big idea

**Energy** is a number that tells you how much change a system can cause. It comes in several stores, and the total in a closed system never changes. You met the stores at IGCSE, and you will need all of them:

| Store | What it is | Example |
|---|---|---|
| Kinetic | energy of motion | a moving car |
| Gravitational potential | energy of position in a gravitational field | water behind a dam |
| Elastic potential | energy in a stretched or compressed object | a drawn bow |
| Thermal (internal) | random motion and interactions of particles | a hot kettle |
| Chemical | energy in bonds, released by reactions | petrol, food, batteries |
| Nuclear | energy in the nucleus, released by fission or fusion | a power reactor |
| Electrical | energy carried by charges moving in a circuit | the current in a lamp |
| Radiation | energy carried by electromagnetic waves | sunlight |

Energy moves from one store to another in a few ways: by a force doing **work**, by an electric current, by heating, and by waves. The next section defines work, because it is the way mechanical energy changes. The unit of energy is the joule, defined with work below.

## Work done

If you push a shopping trolley, you transfer energy to it. The size of the transfer depends on how hard you push and how far the trolley moves. That product is called work.

:::def Work done
The product of the force and the displacement in the direction of the force.
:::

:::def The joule
The work done when a force of 1 N moves its point of application 1 m in the direction of the force. So \(1\,\mathrm{J} = 1\,\mathrm{N\,m}\).
:::

When the force and the displacement are in the same direction, \(W = Fs\). Often they are not. Only the part of the force **along the displacement** does work, so you must resolve the force, as in [Forces, density and pressure](#phys.forces).

:::formula Work done
\[W = Fs\cos\theta\]
\(W\): work done (J) · \(F\): force (N) · \(s\): displacement (m) · \(\theta\): angle between the force and the displacement. \(F\cos\theta\) is the component of the force along the displacement.
:::

:::html
<figure class="fig"><svg viewBox="15 35 540 200" role="img" aria-label="A crate on the floor pulled by a rope at 30 degrees above the horizontal. The force F of 120 newtons is shown with dashed horizontal component F cos theta and vertical component F sin theta, and the displacement s of 8.0 metres is drawn below the floor."><path class="ln" d="M30 170H540"/><rect class="f1 s-acc sw2" x="200" y="110" width="100" height="60"/><text class="tl tc" x="250" y="145">crate</text><circle class="fi" cx="300" cy="140" r="4"/><path class="c1" d="M300 140L429.9 65" marker-end="url(#ah-phys)"/><path class="c3 dash thin" d="M300 140H430M430 140V65"/><path class="ln thin" d="M340 140A40 40 0 0 0 334.6 120"/><text class="tl" x="346" y="132">θ = 30°</text><text class="tl" x="444" y="60">F = 120 N</text><text class="tl" x="440" y="112">F sin θ</text><text class="tl tc" x="365" y="162">F cos θ</text><path class="c2" d="M170 202H500" marker-end="url(#ah2-phys)"/><text class="tl tc" x="335" y="222">displacement s = 8.0 m</text></svg><figcaption>Only the component F cos θ along the displacement does work. The vertical component F sin θ is perpendicular to the displacement, so it does no work.</figcaption></figure>
:::

:::eg A crate of mass 25 kg is pulled 8.0 m along a level floor by a rope. The rope pulls with a force of 120 N at 30° above the horizontal. Calculate the work done by the rope.
Only the horizontal component of the force acts along the displacement:
\[W = Fs\cos\theta = 120 \times 8.0 \times \cos 30^\circ\] [C1]
\[W = 831\,\mathrm{J}\]
To 2 significant figures, as the data are given, the work done is \(8.3 \times 10^{2}\,\mathrm{J}\). [A1]

The mass of the crate does not appear. The work done by this particular force depends only on the force, the distance and the angle.
:::

Three consequences of \(W = Fs\cos\theta\) appear again and again.

- **\(\theta = 0^\circ\)**: force along the motion, \(\cos 0^\circ = 1\), so \(W = Fs\). This is the largest work for a given force.
- **\(\theta = 90^\circ\)**: force perpendicular to the motion, \(\cos 90^\circ = 0\), so **no work is done**. A bag carried at constant height has a vertical supporting force and a horizontal displacement, so the force does no work. A satellite in a circular orbit has a gravitational force that is always at 90° to its velocity, so gravity does no work on it and its speed stays constant.
- **\(\theta = 180^\circ\)**: force opposite to the motion, \(\cos 180^\circ = -1\), so the work is **negative**. Friction and drag do negative work on a moving object. They transfer energy away from it, usually as thermal energy.

When the force changes during the motion, you cannot just multiply. The work done is the **area under the force–displacement graph**, a fact that returns in [Deformation of solids](#phys.solids) for stretched springs and wires.

:::plot A box is pushed with a force that rises steadily from 20 N to 60 N over 4.0 m (F = 20 + 10s). The shaded area is the work done.
--f "20+10*x" --x 0 5 --y 0 80 --shade "0,0,4" --pt "4,60,(4.0 m, 60 N)@se" --xlabel "s / m" --ylabel "F / N"
:::

:::eg Find the work done on the box by the force shown in the graph above.
The work is the area under the graph. The shape from \(s = 0\) to \(s = 4.0\,\mathrm{m}\) is a trapezium:
\[W = \tfrac12 (20 + 60) \times 4.0\] [C1]
\[W = 160\,\mathrm{J}\] [A1]
:::

## Conservation of energy

:::def Principle of conservation of energy
Energy cannot be created or destroyed; it can only be transferred from one form to another. The total energy of a closed system is constant.
:::

This principle is the most reliable tool in physics. The word "lost" in everyday speech ("energy is lost as heat") is misleading. Energy that is **dissipated** has not disappeared. It has been transferred into thermal energy of the surroundings (and sometimes sound), spread out among so many particles that you cannot get it back usefully.

To use the principle, write the total energy at the start and at the end. For a moving object there are two ways its energy can change:

- a force does **work** on it (or it does work against a force such as friction), or
- energy moves between its stores, for example gravitational potential to kinetic.

When all the energy transferred to an object ends up as kinetic energy, then **work done = change in kinetic energy**. The next two sections prove the formulae for the energy of position and the energy of motion.

## Gravitational potential energy

:::def Gravitational potential energy
The energy a mass has because of its position in a gravitational field.
:::

Lift a book from the floor to a shelf and you do work against its weight. That work is stored as gravitational potential energy (GPE) of the book, ready to be released if it falls.

:::proof examinable Change in gravitational potential energy
A mass \(m\) is raised through a vertical height \(\Delta h\) at constant speed, in a uniform gravitational field of strength \(g\).
At constant speed there is no acceleration, so the resultant force is zero (Newton's first law).
The lifting force \(F\) therefore equals the weight: \(F = mg\).
The force and the displacement are both vertical, so the work done is \(W = F\Delta h\).
Substituting \(F = mg\) gives \(W = mg\Delta h\).
This work is the energy transferred to the mass. Its kinetic energy has not changed, so it is stored as gravitational potential energy.
Therefore \(\Delta E_\mathrm{P} = mg\Delta h\).
:::

:::formula Change in gravitational potential energy
\[\Delta E_\mathrm{P} = mg\Delta h\]
\(\Delta E_\mathrm{P}\): change in GPE (J) · \(m\): mass (kg) · \(g\): acceleration of free fall, \(9.81\,\mathrm{m\,s^{-2}}\) · \(\Delta h\): change in **vertical** height (m). Valid only where \(g\) is uniform, which is true near the Earth's surface. For large changes in height, see [Gravitational fields](#phys.gravity).
:::

Notice three things. The formula uses the **vertical** height gained, not the distance travelled along a slope. Only the change matters, so you may choose any reference level to call \(h = 0\). And a fall transfers energy in the same way: \(\Delta h\) negative means the GPE decreases.

:::eg A climber of mass 65 kg walks up a path that is 2.4 km long and rises 450 m vertically. Calculate the increase in her gravitational potential energy.
Use the vertical height, not the length of the path:
\[\Delta E_\mathrm{P} = mg\Delta h = 65 \times 9.81 \times 450\] [C1]
\[\Delta E_\mathrm{P} = 2.87 \times 10^{5}\,\mathrm{J}\]
To 2 significant figures, this is \(2.9 \times 10^{5}\,\mathrm{J}\). [A1]
:::

## Kinetic energy

:::def Kinetic energy
The energy an object has because of its motion.
:::

:::proof examinable Kinetic energy
A constant resultant force \(F\) acts on a mass \(m\), initially at rest, along a straight line, and moves it through a displacement \(s\) while it reaches speed \(v\).
By Newton's second law, \(F = ma\).
The work done by the resultant force is \(W = Fs = mas\).
For constant acceleration from rest, \(v^2 = u^2 + 2as = 2as\), so \(as = \tfrac12 v^2\).
Substituting, \(W = m \times \tfrac12 v^2 = \tfrac12 mv^2\).
This work is the energy transferred to the mass, and no other store has changed, so it is the kinetic energy.
Therefore \(E_\mathrm{K} = \tfrac12 mv^2\).
:::

:::formula Kinetic energy
\[E_\mathrm{K} = \tfrac12 mv^2\]
\(E_\mathrm{K}\): kinetic energy (J) · \(m\): mass (kg) · \(v\): speed (\(\mathrm{m\,s^{-1}}\)). Energy is a scalar, so it has no direction.
:::

The speed is **squared**. Doubling the speed of a car makes its kinetic energy four times as large, which is why a car at \(60\,\mathrm{km\,h^{-1}}\) is far more dangerous than one at \(30\,\mathrm{km\,h^{-1}}\).

:::eg A car of mass 1400 kg travels at 30 m s⁻¹. Calculate its kinetic energy, and the kinetic energy at twice that speed.
\[E_\mathrm{K} = \tfrac12 mv^2 = \tfrac12 \times 1400 \times 30^2\] [C1]
\[E_\mathrm{K} = 6.3 \times 10^{5}\,\mathrm{J}\] [A1]
At \(60\,\mathrm{m\,s^{-1}}\), the kinetic energy is \(\tfrac12 \times 1400 \times 60^2 = 2.52 \times 10^{6}\,\mathrm{J}\): four times larger, because \(v\) is squared.
:::

### Kinetic energy and momentum

Collision questions often give you the momentum \(p = mv\) from [Dynamics and momentum](#phys.dynamics) and ask for the kinetic energy. Substitute \(v = p/m\) into \(\tfrac12 mv^2\):

:::formula Kinetic energy from momentum
\[E_\mathrm{K} = \frac12 m\left(\frac{p}{m}\right)^2 = \frac{p^2}{2m}\]
\(p\): momentum (\(\mathrm{kg\,m\,s^{-1}}\)) · \(m\): mass (kg). For the same momentum, the **lighter** object has the **larger** kinetic energy.
:::

:::eg A car of mass 1200 kg and a cyclist and bicycle of total mass 60 kg each have a momentum of \(6.0 \times 10^{2}\,\mathrm{kg\,m\,s^{-1}}\). Calculate the kinetic energy of each.
Car: \(E_\mathrm{K} = \dfrac{p^2}{2m} = \dfrac{(6.0 \times 10^{2})^2}{2 \times 1200}\) [C1] \(= 150\,\mathrm{J}\). [A1]
Cyclist: \(E_\mathrm{K} = \dfrac{(6.0 \times 10^{2})^2}{2 \times 60} = 3.0 \times 10^{3}\,\mathrm{J}\). [A1]
The car is crawling at \(0.50\,\mathrm{m\,s^{-1}}\) and the cyclist is moving at \(10\,\mathrm{m\,s^{-1}}\): equal momenta, but twenty times the kinetic energy for the object with one-twentieth of the mass.
:::

## Solving energy problems

For nearly every problem, follow the same plan.

:::steps
1. Choose two instants: the start and the end.
2. List the stores of energy at each instant (kinetic, gravitational, elastic, thermal).
3. Add work done against friction or drag as energy transferred to thermal energy.
4. Write: energy at start = energy at end + energy dissipated. Solve for the unknown.
:::

When the only force doing work is gravity, **kinetic energy gained = gravitational potential energy lost**. Then the mass cancels:
\[\tfrac12 mv^2 = mg\Delta h \quad\Rightarrow\quad v = \sqrt{2g\Delta h}\]
That is why a feather and a hammer fall at the same rate in a vacuum, and why the speed at the bottom of a pendulum swing does not depend on the mass of the bob.

:::html
<figure class="fig"><svg viewBox="0 0 600 340" role="img" aria-label="A roller coaster track descending from A at the top, through B halfway down, to C at the bottom, with a bar chart of gravitational and kinetic energy at each point. The two bars always add to the same total."><path class="ln dash thin" d="M30 150H570"/><path class="ln-m" d="M30 40H90C150 40 170 150 260 150C340 150 380 70 470 70H570"/><path class="c3 dash thin" d="M70 46V144" marker-end="url(#ahr)"/><circle class="fa" cx="70" cy="40" r="6"/><circle class="fa" cx="163.75" cy="95" r="6"/><circle class="fa" cx="260" cy="150" r="6"/><text class="tl tc" x="70" y="28">A</text><text class="tl" x="176" y="86">B</text><text class="tl tc" x="260" y="172">C</text><text class="tl" x="78" y="100">h = 35 m</text><path class="ln dash thin" d="M40 210H560"/><text class="tl tc" x="100" y="198">at A</text><rect class="f1 s-acc sw2" x="70" y="210" width="26" height="90"/><text class="tl tc" x="83" y="322">GPE</text><text class="tl tc" x="117" y="322">KE</text><text class="tl tc" x="300" y="198">at B</text><rect class="f1 s-acc sw2" x="270" y="255" width="26" height="45"/><rect class="f2 s-acc sw2" x="304" y="255" width="26" height="45"/><text class="tl tc" x="283" y="322">GPE</text><text class="tl tc" x="317" y="322">KE</text><text class="tl tc" x="500" y="198">at C</text><rect class="f2 s-acc sw2" x="504" y="210" width="26" height="90"/><text class="tl tc" x="483" y="322">GPE</text><text class="tl tc" x="517" y="322">KE</text><text class="tl" x="34" y="205">total</text><path class="ln" d="M40 300H560"/></svg><figcaption>With no friction, the heights of the two bars at A, at B and at C always add up to the same total, the height of the dashed line. At A, all the energy is gravitational. At B, half has become kinetic. At C, all of it is kinetic.</figcaption></figure>
:::

:::eg A roller-coaster car starts from rest at the top of a track 35 m above the lowest point. Ignore friction. (a) Calculate its speed at the bottom. (b) In a second run, 20% of the energy it starts with is dissipated by friction and air resistance before the bottom. Calculate its speed at the bottom.
(a) Gravitational energy lost = kinetic energy gained:
\[\tfrac12 mv^2 = mgh \quad\Rightarrow\quad v = \sqrt{2gh} = \sqrt{2 \times 9.81 \times 35}\] [C1]
\[v = 26\,\mathrm{m\,s^{-1}}\] [A1] (26.2 before rounding to 2 significant figures)
(b) Only 80% of the gravitational energy becomes kinetic energy:
\[\tfrac12 mv^2 = 0.80\,mgh \quad\Rightarrow\quad v = \sqrt{0.80 \times 2 \times 9.81 \times 35}\] [C1]
\[v = 23\,\mathrm{m\,s^{-1}}\] [A1] (23.4 before rounding)
The mass of the car is not needed in either part, because it cancels.
:::

:::eg A pendulum bob is released from rest at a point 0.20 m higher than the lowest point of its swing. Find its speed at the lowest point.
Only gravity does work on the bob (the tension is always perpendicular to the motion, so it does none), so \(\tfrac12 mv^2 = mg\Delta h\):
\[v = \sqrt{2g\Delta h} = \sqrt{2 \times 9.81 \times 0.20} = 2.0\,\mathrm{m\,s^{-1}}\]
The result does not depend on the mass of the bob, or on the length of the string. Only the height matters.
:::

### Energy on graphs

Exam questions often ask you to sketch how the energies change during a fall. Take a ball of mass 0.50 kg dropped from rest from a height of 20 m, with no air resistance. Its gravitational potential energy is \(mgh\), which is proportional to its height \(h\) above the ground, and the total is always \(mg \times 20 = 98.1\,\mathrm{J}\), so its kinetic energy is \(98.1 - mgh\).

:::plot Energy against height for a 0.50 kg ball falling from 20 m with no air resistance. Read the graph from right to left as the ball falls: the gravitational potential energy line goes down and the kinetic energy line goes up, and at every height the two add up to 98.1 J.
--f "4.905*x" --f "4.905*(20-x)" --x 0 20 --y 0 140 --xstep 5 --xlabel "h / m" --ylabel "E / J" --label "gravitational potential energy" --label "kinetic energy" --legend tr
:::

Both graphs against **height** are straight lines with gradients \(+mg\) and \(-mg\). Against **time** they are curves: the speed grows in proportion to time, so the kinetic energy \(\tfrac12 mv^2\) grows in proportion to \(t^2\) (a parabola starting flat at \(t = 0\)). With air resistance, the kinetic energy at each height is less than the line shows: the total falls below \(98.1\,\mathrm{J}\), and the shortfall is the work done against air resistance so far. At terminal velocity the kinetic energy stops changing, and all of the gravitational potential energy lost is dissipated as thermal energy, at the rate \(mgv\).

:::eg A car of mass 1200 kg travelling at 20 m s⁻¹ brakes to rest. The total resistive force (brakes plus air resistance) is a constant 6000 N. Calculate the stopping distance.
Kinetic energy at the start:
\[E_\mathrm{K} = \tfrac12 \times 1200 \times 20^2 = 2.4 \times 10^{5}\,\mathrm{J}\] [C1]
All of it is removed by the work done by the resistive force, which acts opposite to the motion:
\[Fs = E_\mathrm{K} \quad\Rightarrow\quad s = \frac{2.4 \times 10^{5}}{6000} = 40\,\mathrm{m}\] [A1]
At \(40\,\mathrm{m\,s^{-1}}\) the energy is four times larger, so for the same braking force the stopping distance is four times larger, 160 m. This is why stopping distances grow so fast with speed.
:::

:::eg A block of mass 2.0 kg is released from rest at the top of a rough slope. The slope is 3.0 m long and makes an angle of 30° with the horizontal. A constant frictional force of 5.0 N acts up the slope while the block slides down. Calculate the speed of the block at the bottom.
The height of the top above the bottom is \(3.0 \sin 30^\circ = 1.5\,\mathrm{m}\). [B1]

Gravitational energy lost: \(mg\Delta h = 2.0 \times 9.81 \times 1.5 = 29.4\,\mathrm{J}\).
Work done against friction (dissipated as thermal energy): \(Fs = 5.0 \times 3.0 = 15\,\mathrm{J}\). [C1]
The rest is kinetic energy:
\[\tfrac12 mv^2 = 29.43 - 15 = 14.43\,\mathrm{J}\]
\[v = \sqrt{\frac{2 \times 14.43}{2.0}} = 3.8\,\mathrm{m\,s^{-1}}\] [A1]
:::

## Efficiency

No machine converts all the energy it receives into the form you want. Some is always dissipated, as thermal energy in the wires of a motor or as sound in the gears.

:::def Efficiency
The ratio of the useful energy output from a system to the total energy input. Equivalently, the ratio of the useful power output to the total power input.
:::

:::formula Efficiency
\[\text{efficiency} = \frac{\text{useful energy output}}{\text{total energy input}} = \frac{\text{useful power output}}{\text{total power input}}\]
Give it as a ratio (0 to 1) or multiply by 100 for a percentage. It has no unit.
:::

Efficiency can never be above 1 (100%), because that would mean a machine produces more energy than it receives, which breaks the conservation of energy. Useful output plus dissipated energy always equals the input.

:::html
<figure class="fig"><svg viewBox="15 45 565 188" role="img" aria-label="A Sankey diagram for an electric motor: 200 joules of electrical energy in, 150 joules useful output lifting a load, 30 joules thermal in the windings and 20 joules thermal and sound elsewhere. The band widths are proportional to the energy."><path class="fm s-mute sw1" d="M30 60H130V160H30Z"/><text class="tl tc" x="80" y="115">200 J in</text><path class="fok s-mute sw1" d="M130 60H440V135H130Z"/><path class="fr s-mute sw1" d="M130 135C250 135 260 170 400 170V185C260 185 250 150 130 150Z"/><path class="fr s-mute sw1" d="M130 150C260 150 260 205 400 205V215C260 215 260 160 130 160Z"/><text class="tl" x="450" y="102">150 J useful (lifting)</text><text class="tl" x="410" y="182">30 J thermal (windings)</text><text class="tl" x="410" y="214">20 J thermal and sound</text><text class="tl tc" x="285" y="97">useful output</text></svg><figcaption>A Sankey diagram draws energy as bands whose widths are proportional to the energy. Here the efficiency is 150/200 = 0.75, or 75%.</figcaption></figure>
:::

:::eg A lift motor raises a load of mass 800 kg through a height of 20 m in 25 s. The motor is 65% efficient. Calculate the electrical power it needs.
Useful power output = rate of gain of GPE:
\[P_\text{out} = \frac{mg\Delta h}{t} = \frac{800 \times 9.81 \times 20}{25} = 6.3 \times 10^{3}\,\mathrm{W}\] [C1]
\[P_\text{in} = \frac{P_\text{out}}{\text{efficiency}} = \frac{6278}{0.65} = 9.7 \times 10^{3}\,\mathrm{W}\] [A1]
Always divide the useful output by the efficiency to find the input. Multiplying instead gives an input smaller than the output, which is impossible.
:::

## Power

Two engines can do the same work, but the one that does it faster is more powerful.

:::def Power
The work done (or energy transferred) per unit time.
:::

:::formula Power
\[P = \frac{W}{t} = \frac{\Delta E}{t}\]
\(P\): power (W) · \(W\): work done or energy transferred (J) · \(t\): time (s). One **watt** is one joule per second: \(1\,\mathrm{W} = 1\,\mathrm{J\,s^{-1}}\).
:::

:::eg A student of mass 60 kg climbs a flight of stairs, a vertical height of 3.0 m, in 4.0 s. Calculate her useful power output.
\[P = \frac{mg\Delta h}{t} = \frac{60 \times 9.81 \times 3.0}{4.0}\] [C1]
\[P = 4.4 \times 10^{2}\,\mathrm{W}\] [A1] (441 W before rounding)
:::

### Power and velocity

Cars, lifts and cyclists all move against a steady force. For a force acting along the motion, power can be written using the velocity.

:::proof examinable Power and velocity: \(P = Fv\)
A constant force \(F\) acts on an object and moves it a distance \(s\) in the direction of the force in time \(t\).
The work done is \(W = Fs\).
The power is \(P = \dfrac{W}{t} = \dfrac{Fs}{t}\).
The force is constant and \(F\) is not changed by the division, so \(P = F \times \dfrac{s}{t}\).
But \(\dfrac{s}{t} = v\), the velocity of the object along the force.
Therefore \(P = Fv\).
:::

:::formula Power and velocity
\[P = Fv\]
\(P\): power (W) · \(F\): force in the direction of motion (N) · \(v\): speed (\(\mathrm{m\,s^{-1}}\)). At a changing speed, \(Fv\) gives the power at that instant.
:::

When a car, cyclist or boat moves at **constant velocity**, the resultant force is zero, so the driving force equals the resistive force. The power the engine delivers is then \(P = F_\text{drag} \times v\). Because drag usually rises with speed, a car's top speed is where the engine's maximum power just balances the drag.

:::eg A car of mass 1100 kg has a maximum engine power of 60 kW. Its top speed is 50 m s⁻¹. (a) Calculate the drag force at top speed. (b) Assume that the drag is proportional to the speed. Calculate the greatest acceleration the car can have at 25 m s⁻¹ on a level road, with the engine at full power.
(a) At constant top speed, the driving force equals the drag:
\[F = \frac{P}{v} = \frac{60 \times 10^{3}}{50}\] [C1]
\[F = 1.2 \times 10^{3}\,\mathrm{N}\] [A1]
(b) The drag at 25 m s⁻¹ is half of 1200 N, that is 600 N. [B1]

The driving force at full power and 25 m s⁻¹ is \(P/v = 60\,000/25 = 2400\,\mathrm{N}\).
The resultant force is \(2400 - 600 = 1800\,\mathrm{N}\), so
\[a = \frac{F_\text{res}}{m} = \frac{1800}{1100} = 1.6\,\mathrm{m\,s^{-2}}\] [A1]
The acceleration falls to zero as the car approaches 50 m s⁻¹, where the driving force has fallen to equal the drag.
:::

:::eg A hydroelectric power station takes water from a lake that is 120 m above its turbines. The water flows at \(50\,\mathrm{m^3\,s^{-1}}\) (density \(1000\,\mathrm{kg\,m^{-3}}\)). The overall efficiency is 85%. Calculate the electrical power produced.
Mass of water per second: \(1000 \times 50 = 5.0 \times 10^{4}\,\mathrm{kg\,s^{-1}}\). [B1]

Power input from the falling water:
\[P_\text{in} = \frac{mg\Delta h}{t} = 5.0 \times 10^{4} \times 9.81 \times 120 = 5.89 \times 10^{7}\,\mathrm{W}\] [C1]
\[P_\text{out} = 0.85 \times 5.89 \times 10^{7} = 5.0 \times 10^{7}\,\mathrm{W}\] [A1]
That is 50 MW, enough for tens of thousands of homes.
:::

### The kilowatt-hour

Electricity companies sell energy in **kilowatt-hours** (kW h). One kilowatt-hour is the energy transferred by a 1 kW device in 1 hour:
\[1\,\mathrm{kW\,h} = 1000\,\mathrm{W} \times 3600\,\mathrm{s} = 3.6 \times 10^{6}\,\mathrm{J}\]
A 2.0 kW heater left on for 3.0 hours uses \(2.0 \times 3.0 = 6.0\,\mathrm{kW\,h}\), which is \(6.0 \times 3.6 \times 10^{6} = 2.16 \times 10^{7}\,\mathrm{J}\). The electrical formula for power, \(P = VI\), is in [Electricity](#phys.electricity).

:::warn Common mistakes in energy and power
- **Work is zero for a force perpendicular to the motion.** Do not multiply by a distance when the force acts at 90° to it.
- **Energy is not "used up".** It is transferred, and the total never changes. Write "dissipated as thermal energy", not "lost".
- **Never give an efficiency above 100%.** If you do, you have divided the wrong way round.
- **Square the speed** in \(\tfrac12 mv^2\), and convert grams to kilograms before you substitute.
- **Use the data-sheet value** \(g = 9.81\,\mathrm{m\,s^{-2}}\), not 10, and keep kW and W straight: \(60\,\mathrm{kW} = 6.0 \times 10^{4}\,\mathrm{W}\).
:::

:::exam Showing energy conservation clearly
In "calculate the speed" questions, write the energy equation in words first: "loss of gravitational potential energy = gain in kinetic energy + work done against friction". The examiner gives the method mark for the right equation, even if your arithmetic later slips. For a derivation (\(P = Fv\), \(E_\mathrm{K}\), \(\Delta E_\mathrm{P}\)), name each step: the starting definition, the substitution, and the final result.
:::

:::board
All the specifications cover the same content. Some UK specifications write the work done as \(W = Fs\cos\theta\) explicitly and give efficiency and power in the same forms; the Cambridge syllabus asks you to derive \(P = Fv\), \(\Delta E_\mathrm{P} = mg\Delta h\) and \(E_\mathrm{K} = \tfrac12 mv^2\).
:::

:::eg Spot the error: a lawnmower is pushed 15 m across a lawn by a force of 90 N directed 40° below the horizontal. Calculate the work done by the person.
A student wrote this answer.

Line 1: \(W = Fs\)
Line 2: \(W = 90 \times 15 = 1350\,\mathrm{J}\)

**Line 1 is wrong: the full force is used, but only its horizontal component \(F\cos\theta\) acts along the displacement. The formula mark and the answer mark are both lost.** [C0] [A0]

Correct working: \(W = Fs\cos\theta = 90 \times 15 \times \cos 40^\circ\) [C1] \(= 1.0 \times 10^{3}\,\mathrm{J}\). [A1]

Check: the true work must be smaller than \(Fs\), because \(\cos\theta < 1\) for any angle other than zero. The answer 1350 J was the largest it could possibly be.
:::

:::try Start easy, finish at exam standard
Q: A builder lifts a 15 kg box through a vertical height of 2.0 m at constant speed. How much work does she do?
A: \(W = mg\Delta h = 15 \times 9.81 \times 2.0 = 294\,\mathrm{J}\), so \(2.9 \times 10^{2}\,\mathrm{J}\) to 2 significant figures.
Q: A waiter carries a tray horizontally at constant speed across a room. How much work does the force of his hand do on the tray?
A: Zero. The supporting force is vertical and the displacement is horizontal, so \(\theta = 90^\circ\) and \(\cos 90^\circ = 0\).
Q: A football of mass 0.45 kg is kicked at \(24\,\mathrm{m\,s^{-1}}\). Calculate its kinetic energy.
A: \(E_\mathrm{K} = \tfrac12 \times 0.45 \times 24^2 = 130\,\mathrm{J}\).
Q: A ball is dropped from rest from a height of 1.8 m. Ignoring air resistance, calculate its speed just before it hits the ground.
A: \(\tfrac12 mv^2 = mgh\), so \(v = \sqrt{2 \times 9.81 \times 1.8} = 5.9\,\mathrm{m\,s^{-1}}\).
Q: A pump takes 5.0 kW of electrical power and delivers 3.5 kW to the water. Calculate its efficiency.
A: Efficiency \(= 3.5/5.0 = 0.70\), that is 70%.
Q: A machine transfers 7500 J in 30 s. Calculate the power.
A: \(P = W/t = 7500/30 = 250\,\mathrm{W}\).
Q: A lorry travels at a constant \(22\,\mathrm{m\,s^{-1}}\) against a drag force of 8.0 kN. Calculate the power of its engine, ignoring other losses.
A: At constant speed, the driving force equals the drag, so \(P = Fv = 8000 \times 22 = 1.8 \times 10^{5}\,\mathrm{W}\) (176 kW before rounding).
Q: A 1.5 kW kettle is on for 4.0 minutes. Calculate the energy transferred in kW h and in joules.
A: \(4.0\,\mathrm{min} = 4.0/60\,\mathrm{h}\), so the energy is \(1.5 \times 4.0/60 = 0.10\,\mathrm{kW\,h}\), which is \(0.10 \times 3.6 \times 10^{6} = 3.6 \times 10^{5}\,\mathrm{J}\).
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define power.
A: The work done (or energy transferred) per unit time. [B1]
Q: [2 marks] ★ A child pulls a sledge a distance of 12 m across level snow with a rope. The rope pulls with a force of 80 N at 35° to the horizontal. Calculate the work done by the child.
A: \(W = Fs\cos\theta = 80 \times 12 \times \cos 35^\circ\) [C1] \(= 7.9 \times 10^{2}\,\mathrm{J}\). [A1]
Q: [3 marks] ★★ A constant force \(F\) moves an object through a displacement \(s\) in time \(t\), along the direction of the force. Derive the equation \(P = Fv\) for the power \(P\), where \(v\) is the velocity of the object.
A: Power \(P = W/t\), where \(W\) is the work done. [B1] The work done is \(W = Fs\), so \(P = Fs/t\). [B1] Since \(s/t = v\), \(P = Fv\). [B1]
Q: [3 marks] ★★ (a) Show that the kinetic energy of an object of mass \(m\) and momentum \(p\) is \(p^2/2m\). (b) An alpha particle of mass \(6.64 \times 10^{-27}\,\mathrm{kg}\) has a momentum of \(1.0 \times 10^{-19}\,\mathrm{kg\,m\,s^{-1}}\). Calculate its kinetic energy.
A: (a) \(v = p/m\), so \(E_\mathrm{K} = \tfrac12 m(p/m)^2 = p^2/2m\). [M1] (b) \(E_\mathrm{K} = \dfrac{(1.0 \times 10^{-19})^2}{2 \times 6.64 \times 10^{-27}}\) [C1] \(= 7.5 \times 10^{-13}\,\mathrm{J}\). [A1]
Q: [3 marks] ★★ An electric motor is supplied with a p.d. of 12 V and a current of 2.5 A. It lifts a load of mass 3.0 kg through 1.2 m in 4.0 s. Calculate the efficiency of the motor.
A: Useful power \(= mg\Delta h/t = 3.0 \times 9.81 \times 1.2/4.0 = 8.83\,\mathrm{W}\). [C1] Input power \(= VI = 12 \times 2.5 = 30\,\mathrm{W}\). [C1] Efficiency \(= 8.83/30 = 0.29\) (29%). [A1]
Q: [6 marks] ★★ A cyclist and bicycle have a total mass of 85 kg. They freewheel from rest down a hill and reach a speed of \(15\,\mathrm{m\,s^{-1}}\) at the bottom, which is 24 m lower than the start. (a) Calculate the loss of gravitational potential energy. (b) Calculate the gain in kinetic energy. (c) Calculate the energy dissipated. (d) State the main form into which this energy is transferred.
H: The energy dissipated is the energy lost from the gravitational store that did not appear as kinetic energy.
A: (a) \(\Delta E_\mathrm{P} = mg\Delta h = 85 \times 9.81 \times 24\) [C1] \(= 2.0 \times 10^{4}\,\mathrm{J}\). [A1] (b) \(E_\mathrm{K} = \tfrac12 \times 85 \times 15^2\) [C1] \(= 9.6 \times 10^{3}\,\mathrm{J}\). [A1] (c) \(20\,012 - 9\,562 = 1.0 \times 10^{4}\,\mathrm{J}\). [A1] (d) Thermal energy of the road, tyres, brakes and air (by work done against friction and air resistance). [B1]
Q: [7 marks] ★★★ A car of mass 1200 kg climbs a straight road at a constant speed of \(20.0\,\mathrm{m\,s^{-1}}\). The road makes an angle of 5.0° with the horizontal. The total resistive force from air and the road is a constant 450 N. (a) Calculate the component of the car's weight along the slope. (b) Calculate the driving force from the engine. (c) Calculate the power delivered by the engine to the wheels. (d) The engine is 25% efficient. Calculate the rate at which energy must be supplied to the engine by the fuel.
H: At constant speed the resultant force along the slope is zero.
H: The driving force balances the resistive force plus the component of the weight down the slope.
A: (a) Component \(= mg\sin\theta = 1200 \times 9.81 \times \sin 5.0^\circ\) [C1] \(= 1.03 \times 10^{3}\,\mathrm{N}\). [A1] (b) Driving force \(= 450 + 1026 = 1.48 \times 10^{3}\,\mathrm{N}\). [C1] [A1] (c) \(P = Fv = 1476 \times 20.0\) [C1] \(= 3.0 \times 10^{4}\,\mathrm{W}\). [A1] (d) Power input \(= 29\,520/0.25 = 1.2 \times 10^{5}\,\mathrm{W}\). [A1]
Q: [6 marks] ★★★ A bullet of mass 10 g is fired at \(350\,\mathrm{m\,s^{-1}}\) into a stationary block of wood of mass 1.99 kg on a smooth surface. The bullet embeds in the block, and they move off together. (a) Use the conservation of momentum to find the speed of the block and bullet. (b) Calculate the kinetic energy lost. (c) State where the energy has gone.
H: Momentum is conserved in the collision, but kinetic energy is not.
A: (a) Momentum before = momentum after: \(0.010 \times 350 = (0.010 + 1.99)v\) [C1] \(v = 1.75\,\mathrm{m\,s^{-1}}\), so \(1.8\,\mathrm{m\,s^{-1}}\). [A1] (b) Initial \(E_\mathrm{K} = \tfrac12 \times 0.010 \times 350^2 = 612.5\,\mathrm{J}\); final \(E_\mathrm{K} = \tfrac12 \times 2.00 \times 1.75^2 = 3.06\,\mathrm{J}\). [C1] [C1] Energy lost \(= 609\,\mathrm{J} \approx 6.1 \times 10^{2}\,\mathrm{J}\). [A1] (c) It is transferred to thermal energy of the bullet and the wood (and some sound), by the work done against the forces that stop the bullet. [B1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A bungee jumper of mass 70 kg steps off a platform. The unstretched rope is 25 m long, and when it stretches by \(x\) it obeys \(F = kx\) with \(k = 150\,\mathrm{N\,m^{-1}}\) (so the energy stored in it is \(\tfrac12 kx^2\), see [Deformation of solids](#phys.solids)). Ignore the mass of the rope and air resistance. (a) Calculate the jumper's speed when the rope first becomes taut. (b) Show that, at the lowest point, \(75x^2 - 687x - 1.72 \times 10^{4} = 0\). (c) Find the maximum extension \(x\) of the rope. (d) Calculate the greatest acceleration of the jumper.
H: At the lowest point the jumper is momentarily at rest, so all the lost gravitational potential energy is stored in the rope.
H: The jumper falls a total distance \(25 + x\).
H: At the lowest point the tension is \(kx\) upwards and the weight is \(mg\) downwards.
A: (a) Falling 25 m: \(v = \sqrt{2gh} = \sqrt{2 \times 9.81 \times 25}\) [C1] \(= 22\,\mathrm{m\,s^{-1}}\). [A1] (b) Energy lost by the jumper equals the energy stored in the rope: \(mg(25 + x) = \tfrac12 kx^2\). [M1] Then \(686.7(25 + x) = 75x^2\), so \(75x^2 - 686.7x - 17\,168 = 0\), which rounds to the given equation. [A1] (c) \(x = \dfrac{687 + \sqrt{687^2 + 4 \times 75 \times 17\,200}}{2 \times 75}\) [C1] \(= 20\,\mathrm{m}\) (20.4 m before rounding). [A1] (d) At the lowest point the tension is \(kx = 150 \times 20.4 = 3058\,\mathrm{N}\), so the resultant force is \(3058 - 687 = 2371\,\mathrm{N}\) upwards. [C1] Then \(a = 2371/70 = 34\,\mathrm{m\,s^{-2}}\) upwards, about \(3.5g\). [A1]
Q: [7 marks] ★★★ A wind turbine has blades of length 40 m, so the blades sweep out a circle of radius 40 m. Wind of density \(1.2\,\mathrm{kg\,m^{-3}}\) blows at \(10\,\mathrm{m\,s^{-1}}\) perpendicular to the circle. (a) Show that the kinetic energy of the air that passes through the circle each second is \(\tfrac12 \rho A v^3\), and calculate its value. (b) The wind speed doubles. By what factor does this power increase? (c) The turbine converts 40% of this power to electrical power. Calculate the electrical output. (d) Explain why a turbine cannot extract all of the kinetic energy of the wind.
H: In one second, the air that passes is a cylinder of cross-sectional area \(A\) and length \(v\).
H: Mass per second is density times volume per second.
A: (a) The volume of air per second is \(Av\), so the mass per second is \(\rho Av\). [C1] The kinetic energy per second is \(\tfrac12 (\rho Av)v^2 = \tfrac12 \rho Av^3\). [C1] With \(A = \pi \times 40^2 = 5027\,\mathrm{m^2}\): \(P = 0.5 \times 1.2 \times 5027 \times 10^3 = 3.0 \times 10^{6}\,\mathrm{W}\). [A1] (b) \(P \propto v^3\), so doubling \(v\) increases \(P\) by \(2^3 = 8\). [M1] [A1] (c) \(0.40 \times 3.0 \times 10^{6} = 1.2 \times 10^{6}\,\mathrm{W}\). [A1] (d) The air must keep moving to leave the turbine and make way for more air, so it keeps some kinetic energy. [B1]
:::

:::quiz
? A force acts on an object that moves at 90° to the force. How much work does the force do?
+ Zero
- Force × distance
- Force × distance × sin 90°, which is the maximum
- A negative amount
> \(W = Fs\cos 90^\circ = 0\). Only the component of the force along the displacement does work. Negative work needs the force to oppose the motion.
? A car doubles its speed. What happens to its kinetic energy?
- It doubles.
+ It becomes four times larger.
- It becomes eight times larger.
- It increases by 50%.
> \(E_\mathrm{K} = \tfrac12 mv^2\) depends on \(v^2\), so doubling \(v\) multiplies the energy by \(2^2 = 4\).
? Two balls of different mass are dropped from the same height and fall freely. Just before they hit the ground, which statement is correct?
+ They have the same speed.
- The heavier ball is faster.
- The lighter ball is faster.
- They have the same kinetic energy.
> \(\tfrac12 mv^2 = mgh\), so \(m\) cancels and \(v = \sqrt{2gh}\) for both. They have different kinetic energies, because their masses differ.
? Which of these efficiencies is impossible for any machine?
- 0.05
- 0.35
- 0.99
+ 1.2
> An efficiency above 1 (120%) would mean the machine gives out more useful energy than it takes in, which breaks the conservation of energy. Low values such as 0.05 are common, for example for a filament lamp.
? A car travels at a constant top speed on a level road. How does the driving force compare with the resistive force?
+ They are equal.
- The driving force is larger.
- The driving force is smaller.
- The driving force is zero.
> The speed is constant, so the resultant force is zero. The engine still has to push forward to cancel the drag, so the driving force is not zero, and \(P = F_\text{drag} v\).
? Which is a unit of energy?
- kW
+ kW h
- N m s⁻¹
- J s⁻¹
> A kilowatt-hour is power multiplied by time, which is energy. kW and \(\mathrm{J\,s^{-1}}\) are units of power, and \(\mathrm{N\,m\,s^{-1}}\) is the same as watts.
? A box slides down a rough slope at constant speed. What happens to its gravitational potential energy?
- It becomes kinetic energy.
- It is destroyed.
+ It is transferred to thermal energy.
- It stays the same.
> The speed is constant, so the kinetic energy does not change. The energy lost from the gravitational store is dissipated by friction as thermal energy of the box and the slope.
:::

:::checklist What you can now do
- [ ] I can define work done and the joule, and use \(W = Fs\cos\theta\) for a force at an angle to the displacement.
- [ ] I can state the principle of conservation of energy and use it to solve problems with friction, slopes and falling objects.
- [ ] I can derive and use \(\Delta E_\mathrm{P} = mg\Delta h\) and \(E_\mathrm{K} = \tfrac12 mv^2\), use \(E_\mathrm{K} = p^2/2m\), and sketch how the energies change during a fall.
- [ ] I can define efficiency and use it to find input or output energy and power.
- [ ] I can define power and use \(P = W/t\), and derive and use \(P = Fv\).
- [ ] I can use the area under a force–displacement graph as work done.
- [ ] I can convert between kW h and joules.
:::

:::recap
- Work done = force × displacement in the direction of the force: \(W = Fs\cos\theta\). Perpendicular force: zero work. Opposing force: negative work. Area under a force–displacement graph = work done. 1 J = 1 N m.
- Energy is conserved: it is transferred between stores, never created or destroyed. "Lost" energy is dissipated as thermal energy.
- \(\Delta E_\mathrm{P} = mg\Delta h\) (vertical height, uniform field) and \(E_\mathrm{K} = \tfrac12 mv^2\), both derived from \(W = Fs\).
- Falling with no friction: \(v = \sqrt{2gh}\), independent of mass. Kinetic energy from momentum: \(E_\mathrm{K} = p^2/2m\).
- Efficiency = useful output / total input (energy or power), never above 1.
- Power \(P = W/t\) (1 W = 1 J s⁻¹) and \(P = Fv\). At constant velocity, driving force = resistive force.
- 1 kW h = \(3.6 \times 10^{6}\) J.
:::

:::links
- explore: [Energy Skate Park: Basics](https://phet.colorado.edu/en/simulations/energy-skate-park-basics) · PhET · drag a skater around a track and watch kinetic, potential and thermal energy trade places
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the work, energy and power questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Deformation of solids](#phys.solids)
