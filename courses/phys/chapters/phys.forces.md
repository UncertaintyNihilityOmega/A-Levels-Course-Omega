@chapter phys.forces
@title Forces, density and pressure
@level as
@paper CAIE P1 · P2 (AS)
@time 5–7 hours
@summary How forces turn things and balance: centre of gravity, moments, couples and torque, equilibrium and the vector triangle for three forces, then density, pressure, hydrostatic pressure \(\Delta p = \rho g \Delta h\) and the upthrust on an object in a fluid.

:::why
A bridge stands, a crane lifts, a ship floats and a diver feels the water press on every side, all for the same reason: the forces balance. This chapter teaches you how to tell whether a structure will stay put or tip over, how to find the force in a cable or at a hinge, and how a fluid pushes on anything immersed in it. Engineers use these ideas to design everything from a seesaw to a submarine.
:::

**Before you start**, you need Newton's laws and weight from [Dynamics and momentum](#phys.dynamics), and resolving a force into components from [Physical quantities, units and uncertainty](#phys.units).

:::try Warm-up
Q: What is the weight of a \(2.5\,\mathrm{kg}\) mass on the Earth? (from [Dynamics and momentum](#phys.dynamics))
A: \(W = mg = 2.5 \times 9.81 = 24.5\,\mathrm{N}\) (to 3 significant figures), acting downwards.
Q: A \(50\,\mathrm{N}\) force acts at \(30^\circ\) above the horizontal. Find its horizontal and vertical components. (from [Physical quantities, units and uncertainty](#phys.units))
A: Horizontal: \(50\cos 30^\circ = 43.3\,\mathrm{N}\). Vertical: \(50\sin 30^\circ = 25.0\,\mathrm{N}\).
Q: A resultant force of \(12\,\mathrm{N}\) acts on a \(3.0\,\mathrm{kg}\) trolley. What is its acceleration? (from [Dynamics and momentum](#phys.dynamics))
A: \(a = F/m = 12/3.0 = 4.0\,\mathrm{m\,s^{-2}}\), in the direction of the force.
:::

## Centre of gravity

Every particle of an object is pulled down by the Earth. Adding up all these tiny forces would be tedious, so we replace them with one force, the weight, acting at one point.

:::def Centre of gravity
The point at which the whole weight of an object may be considered to act.
:::

For a symmetrical object of uniform density, such as a ruler, a sphere or a rectangular block, the centre of gravity is at the geometric centre. For an irregular object you can find it by experiment. An object hanging freely from a point always comes to rest with its centre of gravity vertically **below** the point of suspension, because only then is there no turning effect from the weight.

:::lab Finding the centre of gravity of an irregular lamina
:::steps
1. Make three small holes near the edge of a flat piece of card (the lamina), well apart from each other.
2. Hang the lamina freely from a pin through one hole, held in a clamp. Let it come to rest.
3. Hang a plumb line (a small weight on a string) from the same pin so that the string hangs in front of the lamina. Draw a line on the lamina along the string.
4. Repeat with the other two holes.
5. The lines cross at one point. That point is the centre of gravity. Two lines are enough, and the third line checks the accuracy (the three should meet).
:::
:::

The plumb line shows the true vertical, because the string hangs freely. Using a long string makes the line easier to draw accurately.

### Stability

Whether an object tips over depends on where the line of action of its weight falls relative to its base. Tilt a tall block about one bottom edge. As long as the vertical line through the centre of gravity falls **inside** the base, the weight gives a turning effect that rolls the block back. When the line falls **outside** the base, the weight turns the block further and it topples.

:::html
<figure class="fig"><svg viewBox="0 0 600 230" role="img" aria-label="Three tall blocks on a table. Upright: the weight acts through the centre of the base. Tilted a little about a bottom corner: the line of the weight is still inside the corner and the block would roll back. Tilted a lot: the line of the weight is beyond the corner and the block topples."><path class="ln" d="M20 200H580"/><rect class="f1 s-acc sw2" x="60" y="100" width="60" height="100"/><circle class="fi" cx="90" cy="150" r="3.5"/><path class="c1" d="M90 150V210" marker-end="url(#ah-phys)"/><text class="tl" x="98" y="176">W</text><text class="tl tc" x="90" y="40">upright: stable</text><rect class="f1 s-acc sw2" x="250" y="100" width="60" height="100" transform="rotate(15 310 200)"/><circle class="fi" cx="294" cy="143.9" r="3.5"/><path class="c1" d="M294 143.9V210" marker-end="url(#ah-phys)"/><text class="tl" x="272" y="176">W</text><text class="tl tc" x="300" y="40">tilted a little:</text><text class="tl tc" x="300" y="60">rolls back</text><rect class="f1 s-acc sw2" x="450" y="100" width="60" height="100" transform="rotate(40 510 200)"/><circle class="fi" cx="519.2" cy="142.4" r="3.5"/><path class="c1" d="M519.2 142.4V210" marker-end="url(#ah-phys)"/><text class="tl" x="527" y="216">W</text><text class="tl tc" x="510" y="40">tilted a lot:</text><text class="tl tc" x="510" y="60">topples</text></svg><figcaption>The dot is the centre of gravity. The block tips over only when the vertical line through the centre of gravity passes beyond the edge it is turning about. A wide, low base makes that much harder, which is why racing cars are low and wide.</figcaption></figure>
:::

## Moment of a force

A force can turn an object as well as push it. You can open a door by pushing near the handle far more easily than near the hinge, and you use a long spanner on a tight nut. The turning effect is called the moment.

:::def Moment of a force
The product of the force and the perpendicular distance of its line of action from the pivot.
:::

:::formula Moment of a force
\[\text{moment} = F \times d_\perp\]
\(F\): force (N) · \(d_\perp\): perpendicular distance from the pivot to the line of action of the force (m). The unit of moment is the newton metre (N m). A moment is clockwise or anticlockwise.
:::

The key words are **perpendicular distance** and **line of action**. The line of action is the straight line along the direction of the force. Push a door straight at its hinge and the perpendicular distance is zero, so there is no moment at all, however big the force.

:::html
<figure class="fig"><svg viewBox="15 88 370 192" role="img" aria-label="A spanner of length d pivoting at the left end. A force F acts at the other end at 60 degrees to the spanner. A dashed line extends the line of action of the force backwards, and the perpendicular distance from the pivot to this line is marked d perpendicular."><rect class="fm s-mute sw1" x="70" y="183" width="200" height="14"/><circle class="fi" cx="70" cy="190" r="6"/><path class="ln-m dash thin" d="M270 190L220 103.4"/><path class="ln-m thin" d="M211.3 108.4L216.3 117.1L225 112.1"/><path class="ln thin" d="M70 190L220 103.4"/><path class="c1" d="M270 190L315 268" marker-end="url(#ah-phys)"/><path class="ln thin" d="M310 190A40 40 0 0 1 290 224.6"/><text class="tl" x="318" y="212">θ = 60°</text><text class="tl" x="322" y="266">F</text><text class="tl tc" x="170" y="218">d</text><text class="tl te" x="146" y="132">d⊥</text><text class="tl te" x="62" y="176">pivot</text></svg><figcaption>The moment of F about the pivot is F × d⊥, where d⊥ = d sin θ is the perpendicular distance from the pivot to the line of action. A force along the spanner would have no moment.</figcaption></figure>
:::

When a force makes an angle \(\theta\) with the line from the pivot to the point where it acts, the perpendicular distance is \(d\sin\theta\). The moment is \(F d\sin\theta\). There is an equivalent way to think of it: resolve the force into a part along the spanner (no moment) and a part \(F\sin\theta\) perpendicular to it, and multiply that part by \(d\).

:::eg A force of 80 N is applied at right angles to the end of a spanner 0.25 m long. Find the moment about the nut. Find the moment when the same force is applied at \(60^\circ\) to the spanner.
At right angles: \(\text{moment} = F d = 80 \times 0.25 = 20\,\mathrm{N\,m}\). [C1]

At \(60^\circ\) to the spanner, the perpendicular distance is \(d\sin 60^\circ\):
\[\text{moment} = 80 \times 0.25 \times \sin 60^\circ = 17.3\,\mathrm{N\,m}\] [A1]
Equivalently, only the component \(80\sin 60^\circ = 69.3\,\mathrm{N}\) of the force is perpendicular to the spanner. The turning effect is smaller because part of the force is wasted pushing along the spanner.
:::

## Couples and torque

Wring out a wet cloth, turn a steering wheel or twist a tap with finger and thumb: in each case two forces act, equal and opposite, on opposite sides of the turning axis.

:::def Couple
A pair of equal and opposite forces whose lines of action are parallel but do not coincide. It produces rotation only.
:::

The resultant force of a couple is **zero**, because the two forces cancel. So a couple does not make an object accelerate in any direction, but it does make it turn. If it were not for the turning effect, the object would remain in equilibrium.

:::def Torque of a couple
The product of one of the forces and the perpendicular distance between the lines of action of the two forces.
:::

:::formula Torque of a couple
\[\text{torque} = F \times d\]
\(F\): size of **one** of the two forces (N) · \(d\): perpendicular distance between their lines of action (m). The unit is N m.
:::

:::html
<figure class="fig small"><svg viewBox="60 38 280 222" role="img" aria-label="A steering wheel seen from above with two equal and opposite forces F acting at the left and right of the rim, one downwards and one upwards, a perpendicular distance d apart, shown with dimension arrows below."><circle class="fm s-ink sw2" cx="200" cy="130" r="80"/><circle class="fp s-ink sw2" cx="200" cy="130" r="12"/><path class="ln thin" d="M200 142V210M200 118V50" /><path class="c1" d="M120 130V190" marker-end="url(#ah-phys)"/><path class="c1" d="M280 130V70" marker-end="url(#ah-phys)"/><text class="tl te" x="112" y="170">F</text><text class="tl" x="288" y="100">F</text><path class="c1" d="M200 222H124" marker-end="url(#ah-phys)"/><path class="c1" d="M200 222H276" marker-end="url(#ah-phys)"/><text class="tl tc" x="200" y="244">d</text></svg><figcaption>Two equal and opposite forces F, a distance d apart, turn the wheel without pushing it in any direction. The torque is F × d, wherever on the wheel you apply them.</figcaption></figure>
:::

:::eg A driver turns a steering wheel of diameter 0.36 m by pushing with a force of 12 N with one hand and pulling with 12 N with the other, at opposite ends of a diameter. Find the torque of the couple. Show that the same answer comes from adding the moments of the two forces about the centre.
The forces are parallel, \(0.36\,\mathrm{m}\) apart:
\[\text{torque} = F \times d = 12 \times 0.36 = 4.32\,\mathrm{N\,m}\] [C1] [A1]
About the centre, each force is \(0.18\,\mathrm{m}\) from the axis, and both turn the wheel the same way. The moments add: \(12 \times 0.18 + 12 \times 0.18 = 4.32\,\mathrm{N\,m}\). The two views agree: "two forces, each at distance \(d/2\)" is the same as "one force, at distance \(d\)".
:::

:::proof Why the torque of a couple does not depend on the pivot
Let two forces of size \(F\) act on opposite sides, a perpendicular distance \(d\) apart, turning the same way.
Choose any point P, a perpendicular distance \(x\) from the line of one force and so \(d - x\) from the line of the other (P lies between them).
The two moments about P are \(Fx\) and \(F(d - x)\), and both are in the same direction.
Their sum is \(Fx + F(d - x) = Fd\), and \(x\) has cancelled.
If P lies outside the two lines, the moments are opposite and the difference is again \(F d\).
So a couple has the same turning effect about **every** point: it is a pure torque.
:::

## The principle of moments and equilibrium

If an object is not turning, the turning effects must balance. A uniform seesaw with two children on it shows this: a heavier child sits closer to the middle to balance a lighter child far from it.

:::def Principle of moments
For a body in equilibrium, the sum of the clockwise moments about any point equals the sum of the anticlockwise moments about the same point.
:::

:::def Equilibrium
A body is in equilibrium when there is no resultant force on it and no resultant torque on it. It then has no acceleration and no angular acceleration, so it is at rest or moving at constant velocity without turning.
:::

Two conditions are needed, and they do different jobs. **No resultant force** stops the object accelerating in a straight line. **No resultant torque** stops it from starting to rotate. A couple satisfies the first and not the second, so a couple alone is never equilibrium.

The pivot you choose is up to you, which is a tool, not a problem: take moments about the point where the **most unknown forces act**. An unknown force at the pivot has zero perpendicular distance, so it vanishes from the equation.

:::steps
1. Draw the object and every force on it: weights (at the centre of gravity for a uniform object), loads, supports, cables, with their positions.
2. Choose a pivot where an unknown force acts, so that force drops out.
3. Write: total clockwise moment = total anticlockwise moment, using the perpendicular distance for each force.
4. Resolve forces vertically and horizontally (no resultant force) to find the rest.
:::

:::html
<figure class="fig"><svg viewBox="30 20 460 245" role="img" aria-label="A uniform beam 4.0 metres long on two supports at its ends A and B. A 500 newton person stands 1.0 metre from A and the 200 newton weight of the beam acts at its centre. Upward support forces act at A and B. A scale along the bottom shows 1.0, 1.0 and 2.0 metres."><rect class="f1 s-acc sw2" x="60" y="100" width="400" height="12"/><path class="fm2 s-ink sw2" d="M60 112L48 134H72Z"/><path class="fm2 s-ink sw2" d="M460 112L448 134H472Z"/><path class="c1" d="M160 40V98" marker-end="url(#ah-phys)"/><path class="c1" d="M260 76V98" marker-end="url(#ah-phys)"/><path class="c1" d="M60 195V138" marker-end="url(#ah-phys)"/><path class="c1" d="M460 168V138" marker-end="url(#ah-phys)"/><text class="tl tc" x="160" y="34">500 N</text><text class="tl tc" x="260" y="68">200 N (beam)</text><text class="tl tc" x="60" y="214">force at A</text><text class="tl tc" x="460" y="187">force at B</text><text class="tl te" x="46" y="106">A</text><text class="tl" x="474" y="106">B</text><path class="ln thin" d="M60 245H460M60 240V250M160 240V250M260 240V250M460 240V250"/><text class="tl tc" x="110" y="236">1.0 m</text><text class="tl tc" x="210" y="236">1.0 m</text><text class="tl tc" x="360" y="236">2.0 m</text></svg><figcaption>A uniform beam on two supports. Its weight acts at the centre. Take moments about A to find the force at B (the force at A then has no moment), and about B to find the force at A.</figcaption></figure>
:::

:::eg A uniform beam of length 4.0 m and weight 200 N rests on supports at its two ends, A and B. A person of weight 500 N stands 1.0 m from A. Find the support forces \(R_A\) and \(R_B\).
Take moments about A. Then \(R_A\) has zero moment. The anticlockwise moment is \(R_B\) (upwards at B, 4.0 m from A) and the clockwise moments are the beam weight (2.0 m from A) and the person (1.0 m from A):
\[R_B \times 4.0 = 200 \times 2.0 + 500 \times 1.0 = 900\] [C1]
\[R_B = 225\,\mathrm{N}\] [A1]
There is no resultant force: \(R_A + R_B = 200 + 500 = 700\,\mathrm{N}\), so \(R_A = 700 - 225 = 475\,\mathrm{N}\). [A1]

**Check** by taking moments about B: \(R_A \times 4.0 = 200 \times 2.0 + 500 \times 3.0 = 1900\), so \(R_A = 475\,\mathrm{N}\). The person stands nearer to A, so A carries the larger share, as it should.
:::

A harder case is a **hinged beam**: a uniform horizontal beam of length 2.0 m and weight 100 N is hinged to a wall at one end. A lamp of weight 60 N hangs from the other end, B. A cable joins B to the wall above the hinge, making \(30^\circ\) with the beam. The question is to find the tension in the cable and the hinge force.

:::html
<figure class="fig"><svg viewBox="20 10 340 230" role="img" aria-label="A horizontal beam hinged to a vertical wall at the left. A cable runs from the free end up and to the left to the wall at 30 degrees to the beam. A 60 newton lamp hangs from the free end and the 100 newton weight of the beam acts at its centre. The hinge force is shown as an arrow from the hinge pointing up and to the right."><rect class="fm" x="40" y="20" width="20" height="200"/><path class="ln" d="M60 20V220"/><rect class="f1 s-acc sw2" x="60" y="144" width="200" height="12"/><circle class="fi" cx="60" cy="150" r="4"/><path class="ln" d="M260 150L60 34.5"/><path class="c1" d="M260 150L164.7 95" marker-end="url(#ah-phys)"/><path class="c1" d="M160 156V206" marker-end="url(#ah-phys)"/><path class="c1" d="M260 156V186" marker-end="url(#ah-phys)"/><path class="c3" d="M60 150L155.3 125" marker-end="url(#ahr)"/><path class="ln thin" d="M220 150A40 40 0 0 1 225.4 130"/><text class="tl" x="188" y="142">30°</text><text class="tl" x="188" y="82">T</text><text class="tl" x="170" y="204">100 N</text><text class="tl" x="268" y="182">60 N</text><text class="tl" x="70" y="112">hinge force</text><text class="tl tc" x="260" y="136">B</text></svg><figcaption>The cable pulls up and towards the wall. The hinge force is whatever is needed to make the forces balance; take moments about the hinge so that it drops out.</figcaption></figure>
:::

The hinge force is unknown in size and direction, so take moments **about the hinge**: it has no moment there. The cable acts at B, 2.0 m from the hinge, at \(30^\circ\) to the beam, so its perpendicular distance from the hinge is \(2.0\sin 30^\circ = 1.0\,\mathrm{m}\). The beam's weight acts at its centre, 1.0 m from the hinge.

:::eg Find the cable tension \(T\) for the hinged beam above, and the horizontal and vertical components of the hinge force.
Moments about the hinge: the cable gives an anticlockwise moment, and the beam weight and the lamp give clockwise ones.
\[T \times 2.0\sin 30^\circ = 100 \times 1.0 + 60 \times 2.0 = 220\] [C1]
\[T = \frac{220}{1.0} = 220\,\mathrm{N}\] [A1]
Resolve the cable force: horizontal \(T\cos 30^\circ = 190.5\,\mathrm{N}\) towards the wall, and vertical \(T\sin 30^\circ = 110\,\mathrm{N}\) upwards.

Horizontally the beam has no resultant force, so the hinge pushes **away from the wall** with \(H = 190.5 \approx 191\,\mathrm{N}\). [A1]

Vertically: \(V + 110 = 100 + 60\), so \(V = 50\,\mathrm{N}\) upwards. [A1]

The hinge force has size \(\sqrt{190.5^2 + 50^2} = 197\,\mathrm{N}\), directed \(14.7^\circ\) above the horizontal, away from the wall.
:::

The muscle in your forearm works like the cable: it is attached very close to the elbow, so it must pull far harder than the weight it lifts.

:::eg The forearm is held horizontal, and the hand holds a 5.0 kg mass 0.35 m from the elbow. The biceps muscle pulls vertically upwards and is attached 0.040 m from the elbow. Ignoring the weight of the forearm, find the force in the muscle.
The load is \(5.0 \times 9.81 = 49.05\,\mathrm{N}\). Take moments about the elbow joint:
\[F \times 0.040 = 49.05 \times 0.35\] [C1]
\[F = \frac{17.17}{0.040} = 429\,\mathrm{N}\] [A1]
The muscle force is nearly nine times the load. A short lever arm for the muscle means a large force, but the hand moves a long way for a small contraction.
:::

## Three forces in equilibrium: the vector triangle

Forces are vectors, so if the resultant force is zero, the vectors added head to tail return to their starting point. Three forces in equilibrium therefore form a **closed triangle**.

:::key Three coplanar forces in equilibrium
Draw the three force vectors head to tail, each to scale and in the correct direction. If the forces are in equilibrium, the triangle closes. You can then find unknown sides and angles by scale drawing, or by the sine rule and cosine rule, or by simple trigonometry if the triangle is right-angled.

Three non-parallel forces in equilibrium also have lines of action that **meet at one point**. If they did not, the forces would have a resultant moment.
:::

:::html
<figure class="fig wide"><svg viewBox="0 0 560 210" role="img" aria-label="Left: a picture hung from a knot with two strings each at 40 degrees to the horizontal. The weight of 12 newtons acts down from the knot, and each string tension acts up and outwards. Right: the closed vector triangle of the three forces, with the 12 newton weight drawn downwards, then T2 up and to the right, then T1 up and to the left back to the start."><path class="ln" d="M20 30H220"/><path class="ln" d="M24.7 30L120 110L215.3 30"/><circle class="fi" cx="120" cy="110" r="4"/><path class="c1" d="M120 110V170" marker-end="url(#ah-phys)"/><path class="c1" d="M120 110L84.2 80" marker-end="url(#ah-phys)"/><path class="c1" d="M120 110L155.8 80" marker-end="url(#ah-phys)"/><text class="tl" x="128" y="150">W = 12 N</text><text class="tl te" x="78" y="76">T₁</text><text class="tl" x="162" y="76">T₂</text><text class="tl tc" x="120" y="196">forces on the knot</text><path class="c1" d="M400 40V160" marker-end="url(#ah-phys)"/><path class="c2" d="M400 160L471.5 100" marker-end="url(#ah2-phys)"/><path class="c3" d="M471.5 100L400 40" marker-end="url(#ahr)"/><text class="tl te" x="392" y="104">W</text><text class="tl" x="446" y="148">T₂</text><text class="tl" x="446" y="62">T₁</text><text class="tl tc" x="430" y="196">the closed triangle of forces</text></svg><figcaption>The two strings are symmetrical, so the force triangle is isosceles: T₁ = T₂. Each string must supply half of the vertical force, which is why 2T sin 40° = 12 N.</figcaption></figure>
:::

:::eg A picture of weight 12 N hangs from a knot supported by two strings, each at \(40^\circ\) above the horizontal. Find the tension in each string (a) by resolving, (b) from the triangle.
(a) By symmetry the two tensions are equal, \(T\). Resolving vertically: the vertical components support the weight.
\[2T\sin 40^\circ = 12\] [C1]
\[T = \frac{12}{2\sin 40^\circ} = 9.33\,\mathrm{N}\] [A1]
The horizontal components \(T\cos 40^\circ\) are equal and opposite, so they cancel.

(b) The closed triangle has a vertical side of 12 N (the weight) and two equal sides \(T\), each at \(40^\circ\) to the horizontal. Splitting the isosceles triangle into two right-angled triangles gives \(T\sin 40^\circ = 6.0\), the same equation, and the same \(T = 9.33\,\mathrm{N}\). [A1]

The tension in each string is more than half the weight, and it gets larger as the strings become flatter. A wire pulled tight horizontally between two posts needs an enormous tension to support even a light load.
:::

:::eg A ball of weight 8.0 N rests on a smooth slope at \(30^\circ\) to the horizontal, held by a string parallel to the slope. Find the tension in the string and the contact force from the slope.
Three forces act on the ball: the weight (vertical), the contact force from the slope (perpendicular to the slope, because the slope is smooth), and the tension (up the slope). The triangle is right-angled, with the weight as the hypotenuse. [B1]

\[T = W\sin 30^\circ = 8.0 \times 0.50 = 4.0\,\mathrm{N}\] [C1]
\[N = W\cos 30^\circ = 8.0 \times 0.866 = 6.9\,\mathrm{N}\] [A1]
:::

## Density and pressure

Both ideas compare a quantity with a size. Density compares mass with volume. Pressure compares force with area.

:::def Density
Mass per unit volume.
:::

:::formula Density
\[\rho = \frac{m}{V}\]
\(\rho\): density (\(\mathrm{kg\,m^{-3}}\)) · \(m\): mass (kg) · \(V\): volume (\(\mathrm{m^3}\)).
:::

Densities are often quoted in \(\mathrm{g\,cm^{-3}}\). Because \(1\,\mathrm{g} = 10^{-3}\,\mathrm{kg}\) and \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\), \(1\,\mathrm{g\,cm^{-3}} = 1000\,\mathrm{kg\,m^{-3}}\). Water is \(1000\,\mathrm{kg\,m^{-3}}\) (\(1.00\,\mathrm{g\,cm^{-3}}\)), steel about \(7800\,\mathrm{kg\,m^{-3}}\), air about \(1.2\,\mathrm{kg\,m^{-3}}\). The great trap is volume: \(1\,\mathrm{cm^3}\) is \(10^{-6}\,\mathrm{m^3}\), **not** \(10^{-2}\,\mathrm{m^3}\), because the conversion applies to each of three lengths.

:::def Pressure
The normal force per unit area. (The force acts at right angles to the surface.)
:::

:::formula Pressure
\[p = \frac{F}{A}\]
\(p\): pressure (pascal, \(1\,\mathrm{Pa} = 1\,\mathrm{N\,m^{-2}}\)) · \(F\): force **normal** to the surface (N) · \(A\): area (\(\mathrm{m^2}\)).
:::

The same force gives a big pressure on a small area and a small pressure on a large area. That is why a knife is sharp, why snowshoes stop you sinking, and why a stiletto heel damages a wooden floor.

:::eg A woman of mass 60 kg stands on one stiletto heel of area \(1.0\,\mathrm{cm^2}\). Compare the pressure under the heel with the pressure when the same weight is carried on a flat shoe of area \(150\,\mathrm{cm^2}\).
Her weight is \(60 \times 9.81 = 588.6\,\mathrm{N}\). [C1]

Heel: \(A = 1.0\,\mathrm{cm^2} = 1.0 \times 10^{-4}\,\mathrm{m^2}\), so \(p = \dfrac{588.6}{1.0 \times 10^{-4}} = 5.9 \times 10^{6}\,\mathrm{Pa}\). [A1]

Flat shoe: \(A = 0.015\,\mathrm{m^2}\), so \(p = \dfrac{588.6}{0.015} = 3.9 \times 10^{4}\,\mathrm{Pa}\). [A1]

The heel's pressure is 150 times larger, because its area is 150 times smaller. Be careful with the area: \(1\,\mathrm{cm^2} = 10^{-4}\,\mathrm{m^2}\), and this is where most errors occur.
:::

## Pressure in a fluid

Dive into a swimming pool and your ears feel the pressure increase the deeper you go. A fluid (a liquid or a gas) exerts a pressure at every point, in every direction, and in a liquid at rest the pressure depends on the depth. Take a column of liquid and ask what holds up the liquid below.

:::proof examinable Hydrostatic pressure: Δp = ρgΔh
Consider a vertical column of liquid of cross-sectional area \(A\) and height \(\Delta h\), in a liquid of density \(\rho\).
Its volume is \(V = A\Delta h\), so its mass is \(m = \rho V = \rho A\Delta h\) (from the definition of density).
Its weight is \(W = mg = \rho A\Delta h\,g\).
This weight is a force acting downwards on the liquid beneath the column, spread over the area \(A\) of the base.
The pressure increase from the top to the bottom of the column is \(\Delta p = \dfrac{F}{A}\) (from the definition of pressure).
Substitute: \(\Delta p = \dfrac{\rho A\Delta h\,g}{A} = \rho g\Delta h\).
:::

:::formula Hydrostatic pressure
\[\Delta p = \rho g \Delta h\]
\(\Delta p\): increase of pressure with depth (Pa) · \(\rho\): density of the **fluid** (\(\mathrm{kg\,m^{-3}}\)) · \(g\): \(9.81\,\mathrm{m\,s^{-2}}\) · \(\Delta h\): the vertical depth difference (m).
:::

Three consequences matter. The pressure depends on the **vertical** depth and the density only, not on the shape or width of the container: a narrow tube and a wide lake have the same pressure at the same depth. At the same depth in the same liquid, the pressure is the same in every direction. And the **total** pressure at a depth \(h\) beneath the surface of a liquid open to the air is the pressure of the atmosphere plus the pressure from the liquid:

\[p = p_\text{atm} + \rho g h\]

This is why dams are thicker at the bottom, where the pressure is greatest, and why a submarine hull must be strong. Your blood pressure is measured in the same way, as the height of a column of mercury it can support.

:::eg Sea water has a density of \(1030\,\mathrm{kg\,m^{-3}}\). The atmospheric pressure is \(1.01 \times 10^{5}\,\mathrm{Pa}\). A diver is 30 m below the surface. Find (a) the pressure due to the water, (b) the total pressure, (c) the force on a window of area \(0.20\,\mathrm{m^2}\) in a submersible at this depth.
(a) \(\Delta p = \rho g h = 1030 \times 9.81 \times 30 = 3.03 \times 10^{5}\,\mathrm{Pa}\). [C1] [A1]

(b) \(p = p_\text{atm} + \rho g h = 1.01 \times 10^{5} + 3.03 \times 10^{5} = 4.04 \times 10^{5}\,\mathrm{Pa}\). [A1]

(c) The force on the window is \(F = pA = 4.04 \times 10^{5} \times 0.20 = 8.08 \times 10^{4}\,\mathrm{N}\) (about 81 kN). [A1] This is the force of the water (and the air above it) on the outside of the window. If the inside of the submersible is at atmospheric pressure, the air inside pushes back, and the **net** force is \((p - p_\text{atm})A = 3.03 \times 10^{5} \times 0.20 = 6.06 \times 10^{4}\,\mathrm{N}\).

Read the question: if it asks for "the pressure due to the water", leave out the atmosphere. If it asks for "the pressure at that depth", add it.
:::

A **manometer** is a U-tube of liquid used to measure pressure differences. The pressure is the same at two points at the same level in the same connected liquid, so a difference in the heights of the two surfaces shows the pressure difference \(\rho g\Delta h\).

## Upthrust

Hold a ball under water and it pushes up on your hands. This upward force on an object in a fluid is called upthrust, and it comes from the pressure of the fluid itself.

:::def Upthrust
The upward force on an object in a fluid, caused by the difference in hydrostatic pressure between its lower and upper surfaces.
:::

:::html
<figure class="fig wide"><svg viewBox="0 0 600 260" role="img" aria-label="Left: a block fully under water. Short arrows push down on its top face and longer arrows push up on its bottom face, because the pressure is greater at the greater depth. Right: a block floating, with its weight acting down and an equal upthrust acting up."><rect class="fm" x="40" y="40" width="240" height="190"/><path class="ln" d="M40 40H280"/><rect class="f1 s-acc sw2" x="130" y="100" width="60" height="60"/><path class="c1" d="M140 76V98" marker-end="url(#ah-phys)"/><path class="c1" d="M160 76V98" marker-end="url(#ah-phys)"/><path class="c1" d="M180 76V98" marker-end="url(#ah-phys)"/><path class="c1" d="M140 206V162" marker-end="url(#ah-phys)"/><path class="c1" d="M160 206V162" marker-end="url(#ah-phys)"/><path class="c1" d="M180 206V162" marker-end="url(#ah-phys)"/><path class="ln-m thin" d="M210 70V42" marker-end="url(#ahm)"/><path class="ln-m thin" d="M210 70V98" marker-end="url(#ahm)"/><path class="ln-m thin" d="M240 100V42" marker-end="url(#ahm)"/><path class="ln-m thin" d="M240 100V158" marker-end="url(#ahm)"/><text class="tl te" x="124" y="90">p at top: ρgh₁</text><text class="tl te" x="124" y="196">p at bottom: ρgh₂</text><text class="tl" x="214" y="75">h₁</text><text class="tl" x="244" y="105">h₂</text><text class="tl tc" x="160" y="250">fully submerged</text><rect class="fm" x="320" y="94" width="240" height="136"/><path class="ln" d="M320 94H560"/><rect class="f1 s-acc sw2" x="400" y="70" width="80" height="80"/><circle class="fi" cx="440" cy="110" r="3.5"/><path class="c1" d="M440 110V170" marker-end="url(#ah-phys)"/><path class="c2" d="M440 110V50" marker-end="url(#ah2-phys)"/><text class="tl" x="450" y="164">W</text><text class="tl" x="450" y="60">upthrust</text><text class="tl tc" x="440" y="250">floating: upthrust = weight</text></svg><figcaption>Left: pressure grows with depth, so the upward forces on the bottom face are bigger than the downward forces on the top face. The sideways forces cancel in pairs. Right: a floating block, where the upthrust balances the weight.</figcaption></figure>
:::

Take a block with top and bottom faces of area \(A\), a vertical distance \(\Delta h\) apart. The pressure on the bottom face is greater than on the top face by \(\rho g\Delta h\). The net upward force from the fluid is the pressure difference multiplied by the area:

\[F = (p_\text{bottom} - p_\text{top})A = \rho g\Delta h \times A = \rho g V\]

where \(V = A\Delta h\) is the volume of the block. The forces on the vertical sides are equal and opposite, so they cancel. This is Archimedes' principle: the upthrust equals the weight of fluid the object displaces (\(\rho V\) is the mass of that fluid).

:::formula Upthrust (Archimedes' principle)
\[F = \rho g V\]
\(F\): upthrust (N) · \(\rho\): density of the **fluid** (\(\mathrm{kg\,m^{-3}}\)) · \(V\): volume of fluid displaced, which is the **submerged** volume of the object (\(\mathrm{m^3}\)).
:::

Note that the upthrust does not depend on how deep a fully submerged object is, because the pressure difference between its top and bottom faces depends only on its height. It also uses the density of the **fluid**, never of the object.

### Floating

An object floats when the upthrust equals its weight. A floating object sinks until the weight of the fluid displaced equals its own weight. With the object's density \(\rho_o\), the fluid's \(\rho_f\), total volume \(V\) and submerged volume \(V_s\):

\[\rho_f g V_s = \rho_o g V \quad\Rightarrow\quad \frac{V_s}{V} = \frac{\rho_o}{\rho_f}\]

so the fraction submerged is the ratio of the densities. An object less dense than the fluid floats; an object denser than the fluid sinks. A steel ship floats because its hollow shape displaces a large volume of water, so its **average** density is less than that of water. A hot-air balloon floats in the same way in air: the hot air inside is less dense than the surrounding air, so the upthrust of the cold air exceeds the total weight. A hydrometer floats lower in a less dense liquid, so its scale reads the density directly.

:::eg A wooden cube of side 0.10 m and density \(700\,\mathrm{kg\,m^{-3}}\) floats in water of density \(1000\,\mathrm{kg\,m^{-3}}\). Find the depth of the cube below the surface.
The weight of the cube is \(700 \times (0.10)^3 \times 9.81 = 6.87\,\mathrm{N}\). [C1]

For floating, the upthrust equals the weight: \(1000 \times 9.81 \times V_s = 6.87\), so \(V_s = 7.0 \times 10^{-4}\,\mathrm{m^3}\). [C1]

The depth is \(V_s/\text{area} = 7.0 \times 10^{-4}/(0.10)^2 = 0.070\,\mathrm{m}\). [A1]

**Check** with the density ratio: the fraction submerged is \(700/1000 = 0.70\) of the 0.10 m height, which is \(0.070\,\mathrm{m}\).
:::

:::eg A solid steel block of mass 2.0 kg (density \(7800\,\mathrm{kg\,m^{-3}}\)) hangs from a newton meter and is lowered completely into water. Find the upthrust and the reading on the newton meter.
Volume of the block: \(V = m/\rho = 2.0/7800 = 2.56 \times 10^{-4}\,\mathrm{m^3}\). [C1]

Upthrust: \(F = \rho g V = 1000 \times 9.81 \times 2.56 \times 10^{-4} = 2.52\,\mathrm{N}\). [A1]

Weight in air: \(2.0 \times 9.81 = 19.6\,\mathrm{N}\). The newton meter reads the weight minus the upthrust: \(19.6 - 2.52 = 17.1\,\mathrm{N}\). [A1]

The reading, called the apparent weight, is smaller than the true weight. Note that the density used for the upthrust is that of the water, not of the steel.
:::

:::warn Common mistakes
Using the density of the **object** in \(\rho g V\) for the upthrust (it needs the fluid's density). Using the whole volume when only part is submerged. Forgetting the atmosphere when a question asks for the total pressure, or adding it when the question asks for the pressure due to the liquid only. Taking moments with the distance **along** a slanted force instead of the perpendicular distance. Forgetting one force (often the weight of the beam itself) in a moments equation. Converting \(\mathrm{cm^3}\) to \(\mathrm{m^3}\) by \(10^{-2}\) instead of \(10^{-6}\).
:::

:::exam Moments questions
Name your pivot, draw the forces, and write one clear equation: "clockwise moments = anticlockwise moments about A". For a force at an angle, say how you found the perpendicular distance or the perpendicular component. When the question says "uniform", the weight acts at the centre. When a hinge is involved, take moments about the hinge, then use force balance for the hinge force. Marks usually go to the moments equation, to the substitution and to the answer.
:::

:::board
AQA and OCR use "moment" and "couple" in the same way. Hydrostatic pressure and upthrust are in the Edexcel IAL and OCR specifications and appear less on AQA, so check yours. The equations are the same on every board.
:::

:::eg Spot the error: a spanner is used with a force of 50 N applied at a point 0.30 m from the nut, at \(40^\circ\) to the spanner. Calculate the moment of the force about the nut.
A student wrote this answer.

Line 1: moment \(= F \times d\)
Line 2: \(= 50 \times 0.30 = 15\,\mathrm{N\,m}\)

**Line 2 is wrong: the distance 0.30 m is along the spanner, but the moment needs the perpendicular distance from the nut to the line of action of the force.** The force is not at right angles to the spanner, so the formula as used gives the wrong answer. The substitution mark and the answer mark are both lost. [C0] [A0]

Correct working: \(\text{moment} = F \times d\sin\theta = 50 \times 0.30 \times \sin 40^\circ\) [C1] \(= 9.6\,\mathrm{N\,m}\). [A1]

Check: the moment must be smaller than \(15\,\mathrm{N\,m}\), the largest possible moment for this force and distance, which would occur at \(90^\circ\).
:::

:::try Start easy, finish at exam standard
Q: A force of 20 N acts at a perpendicular distance of 0.35 m from a pivot. Find its moment.
A: \(\text{moment} = Fd = 20 \times 0.35 = 7.0\,\mathrm{N\,m}\).
Q: A 30 kg child sits 1.8 m from the pivot of a uniform seesaw. Where must a 45 kg child sit on the other side to balance it?
A: The weights are proportional to the masses, so \(30 \times 1.8 = 45 \times d\), giving \(d = 54/45 = 1.2\,\mathrm{m}\) from the pivot.
Q: Two forces of 15 N form a couple with their lines of action 0.30 m apart. Find the torque.
A: \(\text{torque} = Fd = 15 \times 0.30 = 4.5\,\mathrm{N\,m}\).
Q: A uniform metre rule of weight 1.0 N is balanced on a pivot at the 30 cm mark by a weight hung at the 0 cm end. Find the hanging weight.
A: The rule's weight acts at 50 cm, which is 0.20 m from the pivot. The hanging weight \(W\) is 0.30 m from the pivot on the other side. \(W \times 0.30 = 1.0 \times 0.20\), so \(W = 0.67\,\mathrm{N}\).
Q: A steel block measuring 5.0 cm by 4.0 cm by 3.0 cm has a mass of 468 g. Find its density in \(\mathrm{kg\,m^{-3}}\).
A: \(V = 5.0 \times 4.0 \times 3.0 = 60\,\mathrm{cm^3}\), so \(\rho = 468/60 = 7.8\,\mathrm{g\,cm^{-3}} = 7800\,\mathrm{kg\,m^{-3}}\).
Q: An 80 kg person stands on boots with a total area of \(0.040\,\mathrm{m^2}\), then on snowshoes with a total area of \(0.50\,\mathrm{m^2}\). Find the pressure on the snow in each case.
A: The weight is \(80 \times 9.81 = 784.8\,\mathrm{N}\). Boots: \(784.8/0.040 = 2.0 \times 10^{4}\,\mathrm{Pa}\). Snowshoes: \(784.8/0.50 = 1.6 \times 10^{3}\,\mathrm{Pa}\).
Q: Find the pressure due to the water at the bottom of a lake 12 m deep (\(\rho = 1000\,\mathrm{kg\,m^{-3}}\)), and the total pressure if the atmospheric pressure is \(1.01 \times 10^{5}\,\mathrm{Pa}\).
A: \(\rho gh = 1000 \times 9.81 \times 12 = 1.18 \times 10^{5}\,\mathrm{Pa}\). Total: \(1.18 \times 10^{5} + 1.01 \times 10^{5} = 2.19 \times 10^{5}\,\mathrm{Pa}\).
Q: The two columns of mercury (\(\rho = 13\,600\,\mathrm{kg\,m^{-3}}\)) in a manometer differ in height by 12 cm. Find the pressure difference.
A: \(\Delta p = \rho g\Delta h = 13600 \times 9.81 \times 0.12 = 1.60 \times 10^{4}\,\mathrm{Pa}\).
Q: Find the upthrust on a wooden log that is fully submerged in water and has a volume of \(0.0030\,\mathrm{m^3}\).
A: \(F = \rho g V = 1000 \times 9.81 \times 0.0030 = 29.4\,\mathrm{N}\).
Q: A ball of weight 8.0 N is held on a smooth \(30^\circ\) slope by a string parallel to the slope. Find the tension.
A: The three forces form a right-angled triangle, with the weight as hypotenuse: \(T = 8.0\sin 30^\circ = 4.0\,\mathrm{N}\).
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define the moment of a force about a point.
A: The product of the force and the perpendicular distance of its line of action from the point. [B1]
Q: [2 marks] ★ Define the torque of a couple.
A: The product of one of the forces [B1] and the perpendicular distance between the lines of action of the two forces. [B1]
Q: [4 marks] ★★ A uniform horizontal bridge deck of length 6.0 m and weight 300 N rests on supports at its two ends. A cart of weight 750 N is 2.0 m from the left-hand end. Calculate the force exerted by each support.
H: Take moments about one support so that its force drops out.
A: Moments about the right-hand end: \(R_\text{L} \times 6.0 = 300 \times 3.0 + 750 \times 4.0\) [C1] so \(R_\text{L} = 650\,\mathrm{N}\). [A1] No resultant force: \(R_\text{L} + R_\text{R} = 300 + 750 = 1050\,\mathrm{N}\) [C1] so \(R_\text{R} = 400\,\mathrm{N}\). [A1]
Q: [4 marks] ★★ A traffic light of weight 80 N hangs from two cables. One cable makes \(30^\circ\) with the horizontal and the other \(45^\circ\), on opposite sides. Draw the triangle of forces in words and calculate the tension in each cable.
H: The three forces form a closed triangle. The sides are 80 N, \(T_1\) and \(T_2\), and the angles opposite them are \(75^\circ\), \(45^\circ\) and \(60^\circ\).
H: Use the sine rule: each side divided by the sine of the opposite angle is the same.
A: The weight and the two tensions, drawn head to tail, form a closed triangle with angles \(75^\circ\) (opposite the weight), \(45^\circ\) (opposite \(T_1\)) and \(60^\circ\) (opposite \(T_2\)). [B1] Sine rule: \(\dfrac{80}{\sin 75^\circ} = \dfrac{T_1}{\sin 45^\circ} = \dfrac{T_2}{\sin 60^\circ}\). [C1] \(T_1 = 58.6\,\mathrm{N}\) (the cable at \(30^\circ\)). [A1] \(T_2 = 71.7\,\mathrm{N}\) (the cable at \(45^\circ\)). [A1]
Q: [3 marks] ★★ Derive the equation \(\Delta p = \rho g\Delta h\) for the increase of pressure with depth in a liquid of density \(\rho\).
A: Consider a column of liquid of cross-sectional area \(A\) and height \(\Delta h\). Its weight is \(mg = \rho A\Delta h\,g\) (mass = density × volume). [B1] The pressure at the bottom of the column exceeds the pressure at the top by the weight divided by area, \(\Delta p = F/A\). [B1] So \(\Delta p = \rho A\Delta h\,g/A = \rho g\Delta h\). [B1]
Q: [4 marks] ★★ A uniform cylinder floats upright in water with 60% of its volume below the surface. (a) Calculate the density of the cylinder. (b) The cylinder is moved into a liquid of density \(800\,\mathrm{kg\,m^{-3}}\). Calculate the fraction of its volume that is submerged.
A: (a) The upthrust equals the weight, so \(\rho_\text{water} \times 0.60V = \rho_\text{cyl}V\). [B1] \(\rho_\text{cyl} = 0.60 \times 1000 = 600\,\mathrm{kg\,m^{-3}}\). [A1] (b) \(\text{fraction} = \dfrac{\rho_\text{cyl}}{\rho_\text{liquid}} = \dfrac{600}{800}\) [C1] \(= 0.75\). [A1]
Q: [7 marks] ★★★ A uniform horizontal beam of length 3.0 m and weight 90 N is hinged to a vertical wall at its left end A. A cable joins the right end B to the wall, making an angle of \(35^\circ\) with the beam. A load of 120 N hangs from the beam 2.0 m from A. (a) Calculate the tension in the cable. (b) Calculate the horizontal and vertical components of the force exerted by the hinge on the beam.
H: Take moments about A. The perpendicular distance for the cable is \(3.0\sin 35^\circ\).
H: The vertical forces: the hinge force and the cable's vertical component support the beam and the load.
A: (a) Moments about A: \(T \times 3.0\sin 35^\circ = 90 \times 1.5 + 120 \times 2.0\). [C1] The right-hand side is \(375\,\mathrm{N\,m}\). [C1] \(T = \dfrac{375}{3.0\sin 35^\circ} = 218\,\mathrm{N}\). [A1] (b) Horizontal: the hinge force balances the horizontal component of the cable force, \(H = T\cos 35^\circ\) [C1] \(= 179\,\mathrm{N}\) away from the wall. [A1] Vertical: \(V + T\sin 35^\circ = 90 + 120\) [C1] so \(V = 210 - 125 = 85.0\,\mathrm{N}\) upwards. [A1]
Q: [6 marks] (#phys.dynamics) ★★★ A solid metal cube of side \(0.050\,\mathrm{m}\) and density \(7800\,\mathrm{kg\,m^{-3}}\) hangs from a newton meter. It is lowered, with its top face horizontal, until it is completely submerged in water of density \(1000\,\mathrm{kg\,m^{-3}}\). (a) Calculate the difference between the pressure on its bottom face and on its top face. (b) Use this to calculate the upthrust. (c) Calculate the reading on the newton meter. (d) State and explain what happens to the reading if the cube is lowered further.
H: The vertical distance between the two faces is the side of the cube.
H: The newton meter reads weight minus upthrust.
A: (a) \(\Delta p = \rho g\Delta h = 1000 \times 9.81 \times 0.050\) [C1] \(= 4.9 \times 10^{2}\,\mathrm{Pa}\). [A1] (b) The faces have area \(0.050^2 = 2.5 \times 10^{-3}\,\mathrm{m^2}\), so \(F = \Delta p \times A = 490.5 \times 2.5 \times 10^{-3}\) [C1] \(= 1.23\,\mathrm{N}\). [A1] (c) Weight \(= 7800 \times 0.050^3 \times 9.81 = 9.56\,\mathrm{N}\), so the reading is \(9.56 - 1.23 = 8.34\,\mathrm{N}\). [A1] (d) The reading does not change, because the pressure difference between the top and bottom faces depends only on the height of the cube, not on its depth, so the upthrust stays the same. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A uniform ladder of length 5.0 m and weight 200 N rests on rough horizontal ground and leans against a smooth vertical wall. It makes an angle of \(60^\circ\) with the ground. (a) Calculate the friction force at the foot of the ladder. (b) A person of weight 700 N climbs three quarters of the way up the ladder. Calculate the friction force now, and explain why a ladder is more likely to slip when someone is high up.
H: The wall is smooth, so its force on the ladder is horizontal. Take moments about the foot of the ladder, where the ground's unknown force acts.
H: The horizontal forces on the ladder are the wall's force and the friction. They must balance.
A: (a) Moments about the foot, with the wall force \(S\) at height \(L\sin 60^\circ\) and the weight at a horizontal distance \(\tfrac12 L\cos 60^\circ\): \(S \times L\sin 60^\circ = 200 \times \tfrac12 L\cos 60^\circ\). [C1] So \(S = \dfrac{200}{2\tan 60^\circ} = 57.7\,\mathrm{N}\). [A1] The horizontal forces balance, so the friction force is \(57.7\,\mathrm{N}\) away from the wall. [B1] (b) \(S \times L\sin 60^\circ = (200 \times 0.5 + 700 \times 0.75)L\cos 60^\circ\) [C1] so \(S = \dfrac{625}{\tan 60^\circ} = 361\,\mathrm{N}\), and the friction force is \(361\,\mathrm{N}\). [A1] The turning effect of the extra weight about the foot increases as the person climbs, so the wall must push back harder, and friction must supply an equal force; if the ground cannot provide that much friction, the ladder slips. [B1]
Q: [4 marks] ★★★ A U-shaped tube contains water. Oil that does not mix with the water is poured into one arm until the oil column is 22.5 cm high. The water in the other arm then stands 18.0 cm above the level of the boundary between the oil and water. (a) Explain why the pressure is the same in both arms at the level of the boundary. (b) Calculate the density of the oil. (c) State why the oil column is the taller one.
H: Compare \(\rho g h\) in the two arms, measured from the boundary level.
A: (a) The water below the boundary is one connected liquid at rest, so the pressure is the same at all points at the same level in it. [B1] (b) \(\rho_\text{oil}g(0.225) = \rho_\text{water}g(0.180)\), and \(g\) cancels. [C1] \(\rho_\text{oil} = 1000 \times \dfrac{18.0}{22.5} = 800\,\mathrm{kg\,m^{-3}}\). [A1] (c) The oil is less dense, so a taller column is needed to give the same pressure. [B1]
:::

:::quiz
? Two forces of 10 N each form a couple, with their lines of action 0.40 m apart. What is the torque of the couple?
+ \(4.0\,\mathrm{N\,m}\)
- \(8.0\,\mathrm{N\,m}\)
- \(0\,\mathrm{N\,m}\)
- \(2.0\,\mathrm{N\,m}\)
> Torque \(= Fd = 10 \times 0.40 = 4.0\,\mathrm{N\,m}\), using one force. \(8.0\) comes from adding both forces, \(0\) from confusing the zero resultant force with zero torque, and \(2.0\) from using half the distance.
? Which statement describes an object in equilibrium?
- The resultant force is zero but there may be a resultant torque.
- The resultant torque is zero but there may be a resultant force.
+ The resultant force and the resultant torque are both zero.
- The clockwise moments are larger than the anticlockwise moments.
> Both conditions are needed: no resultant force prevents acceleration, and no resultant torque prevents rotation. A couple has no resultant force but still turns.
? A rock has a density of \(2.7\,\mathrm{g\,cm^{-3}}\). What is this in \(\mathrm{kg\,m^{-3}}\)?
- 2.7
- 27
+ 2700
- 0.0027
> \(1\,\mathrm{g\,cm^{-3}} = 1000\,\mathrm{kg\,m^{-3}}\), so \(2.7\,\mathrm{g\,cm^{-3}} = 2700\,\mathrm{kg\,m^{-3}}\). The other values come from using the wrong conversion factor.
? A tall tank and a wide tank hold water to the same depth. Compared with the wide tank, the pressure at the bottom of the tall tank is:
- greater, because there is more water
- smaller, because the area is smaller
+ the same
- zero
> \(\Delta p = \rho g\Delta h\) depends on the density and the depth only. The amount of water and the shape of the container do not matter.
? A fully submerged steel ball is lowered deeper into water. What happens to the upthrust on it?
- It increases, because the pressure is higher.
- It decreases, because the ball is heavier at depth.
+ It stays the same.
- It becomes zero.
> The upthrust is \(\rho g V\) with the volume of the ball. The pressure on both the top and bottom faces increases by the same amount, so the difference, and hence the upthrust, does not change.
? A block floats in fresh water. It is then put in sea water, which is denser. What happens?
- The upthrust increases and the block rises out of the water.
+ The upthrust is unchanged and less of the block is submerged.
- The upthrust decreases and the block sinks further.
- The block sinks to the bottom.
> A floating block always has an upthrust equal to its weight. In the denser liquid, a smaller submerged volume gives the same weight of liquid displaced, so the block floats higher.
? Three forces keep a body in equilibrium. How are they drawn in the vector triangle?
- All three arrows point towards one corner.
+ Head to tail, so the arrows go round the triangle in the same sense.
- All three arrows start from one corner.
- They cannot form a triangle.
> The vectors add to zero, so drawn head to tail they return to the start and form a closed triangle with the arrows following each other round it.
? A tall block is tilted about one edge of its base. At which point will it topple?
- When the tilt reaches \(45^\circ\)
+ When the vertical line through the centre of gravity passes outside that edge
- When its weight becomes larger than the contact force
- As soon as it is tilted at all
> The weight gives a turning effect about the edge. While the line of the weight passes inside the edge it rolls the block back; once it passes outside, it turns the block further.
:::

:::checklist What you can now do
- [ ] I can state that the weight of an object acts at its centre of gravity, find the centre of gravity of a lamina, and decide whether an object will topple.
- [ ] I can define and calculate the moment of a force, using the perpendicular distance.
- [ ] I can define a couple and the torque of a couple, and calculate it.
- [ ] I can state and apply the principle of moments, including a beam on two supports and a hinged beam with a cable.
- [ ] I can state the two conditions for equilibrium and use them to find unknown forces.
- [ ] I can use a vector triangle for three coplanar forces in equilibrium.
- [ ] I can define and use density and pressure, with correct unit conversions.
- [ ] I can derive and use \(\Delta p = \rho g\Delta h\), including total pressure at a depth.
- [ ] I can explain upthrust as a pressure difference, calculate it with \(F = \rho g V\) and solve floating problems.
:::

:::recap
- The weight of an object acts at its centre of gravity. An object topples when the vertical line through its centre of gravity falls outside its base.
- Moment of a force \(= F d_\perp\) (N m), with \(d_\perp\) the perpendicular distance from the pivot to the line of action. Torque of a couple \(= F d\), with \(d\) the distance between the lines of action; a couple has zero resultant force.
- Principle of moments: for equilibrium, clockwise moments = anticlockwise moments about any point. Equilibrium needs no resultant force **and** no resultant torque. Take moments about the point where the most unknown forces act.
- Three coplanar forces in equilibrium form a closed vector triangle (head to tail); their lines of action meet at a point.
- Density \(\rho = m/V\): \(1\,\mathrm{g\,cm^{-3}} = 1000\,\mathrm{kg\,m^{-3}}\); \(1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}\). Pressure \(p = F/A\) in pascals.
- Hydrostatic pressure \(\Delta p = \rho g\Delta h\) (from weight of a column over its area). Total pressure at depth \(h\): \(p_\text{atm} + \rho g h\). Independent of container shape.
- Upthrust comes from the pressure difference between the lower and upper faces: \(F = \rho g V\), with the density of the **fluid** and the **submerged** volume. A floating object has upthrust equal to its weight, and the fraction submerged is \(\rho_\text{object}/\rho_\text{fluid}\).
:::

:::links
- explore: [Balancing Act](https://phet.colorado.edu/en/simulations/balancing-act) · PhET · balance masses on a plank and see the moments
- explore: [Density](https://phet.colorado.edu/en/simulations/density) · PhET · compare the densities of materials by floating and sinking blocks
- explore: [Buoyancy](https://phet.colorado.edu/en/simulations/buoyancy) · PhET · change a block's density and the fluid and watch the upthrust
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the moments, equilibrium and pressure questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Work, energy and power](#phys.energy)
