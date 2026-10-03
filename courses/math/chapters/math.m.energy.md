@chapter math.m.energy
@title Work, energy and power
@level as
@paper CAIE P4 · Edexcel IAL M1 and M2 · UK Mechanics
@time 7–9 hours
@summary Energy is the currency of mechanics: forces do work, work changes energy, and power is the rate of doing work. You will learn the work done by a force, kinetic and gravitational potential energy, the work–energy principle and conservation of energy (including curved paths), and power, driving force and maximum speed for vehicles on flat roads and hills.

:::why
Forces and acceleration become hard when the motion is complicated, such as a roller-coaster on a curved track. Energy methods skip the details of the path and compare only the start and the end. They also answer practical questions: how big an engine does a car need to climb a hill at a given speed, and how much energy is lost to friction on the way?
:::

**Before you start**, you need Newton's second law and friction from [Newton's laws and connected particles](#math.m.newton), and the constant acceleration equations from [Kinematics](#math.m.kinematics). Resolving forces is in [Forces and equilibrium](#math.m.forces).

## Work done by a force

:::def Work done
The work done by a constant force is the force multiplied by the distance moved **in the direction of the force**. It is measured in joules (J): 1 J is the work done by a force of 1 N moving its point of application 1 m in the direction of the force.
:::

If the force \(F\) acts along the direction of motion, the work is \(Fd\). If the force acts at an angle \(\theta\) to the direction of motion, only the component \(F\cos\theta\) does work.

:::key Work done
\[W = Fd\cos\theta\]
- \(F\) is the size of the force (N), \(d\) the distance moved (m) and \(\theta\) the angle between the force and the direction of motion.
- If \(\theta = 0^\circ\), \(W = Fd\). If \(\theta = 90^\circ\), \(W = 0\): a force at right angles to the motion (the normal reaction, or the weight on a horizontal floor) does no work.
- Work done **against** a force such as friction or a resistance is \(Fd\) (positive energy lost). The work done **by** the friction force on the object is negative.
- This formula is not on MF19: learn it.
:::

:::html
<figure class="fig"><svg viewBox="0 0 400 150" role="img" aria-label="A block moves to the right a distance d along the floor. A force F acts on it at angle theta above the horizontal. The horizontal component F cos theta is shown as a dashed arrow."><rect class="f1 s-acc sw2" x="120" y="80" width="64" height="36"/><path class="ax" d="M20 116H380"/><path class="c1 thick" d="M152 98L262 38" marker-end="url(#ah)"/><path class="c2 dash" d="M152 98H262" marker-end="url(#ah)"/><path class="dash thin ln" d="M262 38V98"/><path class="c3" d="M120 136H300" marker-end="url(#ah)"/><text class="tl" x="212" y="144" text-anchor="middle">d</text><text class="tl" x="268" y="36">F</text><text class="tl" x="210" y="114" text-anchor="middle">F cos θ</text><text class="tl" x="192" y="90">θ</text></svg><figcaption>Only the component \(F\cos\theta\) along the motion does work.</figcaption></figure>
:::

:::eg A force of 50 N pulls a sledge a distance of 10 m. The force is at \(60^\circ\) to the direction of motion. Find the work done by the force.
\[W = Fd\cos\theta = 50 \times 10 \times \cos 60^\circ = 250\ \text{J}\]
:::

:::eg A 40 N force at \(30^\circ\) above the horizontal drags a crate 5 m along a rough floor. The friction force is 12 N. Find the work done by the force, the work done against friction and the net work done on the crate.
Work by the pull: \(40 \times 5 \times \cos 30^\circ = 173\) J (3 s.f.).
Work against friction: \(12 \times 5 = 60\) J.
Net work \(= 173.2 - 60 = 113\) J (3 s.f.). This net work becomes the crate's kinetic energy gain.
:::

## Kinetic and gravitational potential energy

:::def Kinetic energy and gravitational potential energy
The **kinetic energy** (KE) of a particle of mass \(m\) moving at speed \(v\) is \(\tfrac12 mv^2\). The **gravitational potential energy** (GPE) of a particle of mass \(m\) at height \(h\) above a chosen reference level is \(mgh\). The change in GPE when the height changes by \(h\) is \(mgh\). Both are in joules.
:::

- Energy is a **scalar**: no direction. KE is never negative; GPE is positive above the reference level and negative below it.
- Only **changes** in GPE matter, so you may choose any reference level, such as the starting point or the ground.
- These two formulae are not on MF19: learn them.

:::eg Find the kinetic energy of a 800 kg car at \(25\ \mathrm{m\,s^{-1}}\), and the potential energy gained by a 60 kg climber who climbs 30 m. Take \(g = 10\).
\(\text{KE} = \tfrac12 \times 800 \times 25^2 = 250\,000\) J.
\(\text{GPE gained} = 60 \times 10 \times 30 = 18\,000\) J.
:::

## The work–energy principle

:::key Work–energy principle
The total work done on a particle equals the change in its kinetic energy. Including the change in potential energy, for motion with driving forces and resistances:
\[\begin{aligned}&\text{work done by driving forces} - \text{work done against resistances}\\ &\qquad = \Delta\text{KE} + \Delta\text{GPE}\end{aligned}\]
that is, energy put in, less energy lost to resistances, equals the energy gained.
- With **no** driving force and **no** resistance (smooth surface, no friction or air resistance), energy is **conserved**: \(\text{KE} + \text{GPE}\) stays constant.
- It is the same principle whether the path is straight or curved, because only the change in height matters for GPE.
:::

:::steps
1. Choose the start and the end positions, and a level for \(h = 0\).
2. Write the energy at the start and at the end: KE, GPE.
3. List the work done by each force that is not gravity (driving force, friction, resistance, pull). Give it the correct sign: positive if it helps the motion, negative if it opposes.
4. Write the energy equation in words: energy at the start, plus work done by driving forces, minus work done against resistances, equals energy at the end (KE + GPE each time).
5. Solve for the unknown.
:::

:::eg A 4 kg box on a rough horizontal floor starts from rest and is pushed 6 m by a horizontal force of 30 N. The friction force is 10 N. Find its final speed.
Work by the push: \(30 \times 6 = 180\) J. Work against friction: \(10 \times 6 = 60\) J. Net work \(= 120\) J, which equals the change in KE:
\[\tfrac12 \times 4 \times v^2 = 120 \quad\Rightarrow\quad v^2 = 60 \quad\Rightarrow\quad v = 7.75\ \mathrm{m\,s^{-1}}\]
Check with \(F = ma\): \(a = \dfrac{20}{4} = 5\), and \(v^2 = 2 \times 5 \times 6 = 60\). ✓
:::

### Conservation of energy and curved paths

For a smooth track the normal reaction is perpendicular to the motion, so it does no work. Only gravity does work, and energy is conserved whatever the shape of the track.

:::eg A particle is released from rest at the top of a smooth curved slide, 5 m above the bottom. Find its speed at the bottom. Take \(g = 10\).
Take the bottom as \(h = 0\). Energy conservation:
\[mg(5) + 0 = 0 + \tfrac12 mv^2 \quad\Rightarrow\quad v^2 = 2 \times 10 \times 5 = 100 \quad\Rightarrow\quad v = 10\ \mathrm{m\,s^{-1}}\]
The mass cancels and the shape of the slide does not matter. This is the same as \(v^2 = 2gh\) for free fall through the same height.
:::

:::eg A ball is thrown vertically upwards at \(15\ \mathrm{m\,s^{-1}}\) from a point 2 m above the ground. Find the greatest height above the ground and the speed at which it hits the ground. Take \(g = 10\).
Take the ground as \(h = 0\) and let \(H\) be the greatest height. Start: KE \(= \tfrac12 m(225)\), GPE \(= m(10)(2)\). At the top the speed is 0:
\[\tfrac12 m(225) + 20m = 10mH \quad\Rightarrow\quad 112.5 + 20 = 10H \quad\Rightarrow\quad H = 13.25\ \text{m}\]
Landing: \(\tfrac12 mv^2 = \tfrac12 m(225) + 20m\), so \(v^2 = 225 + 40 = 265\) and \(v = 16.3\ \mathrm{m\,s^{-1}}\).
:::

:::eg A 5 kg block slides from rest down a rough slope inclined at \(\theta\) with \(\sin\theta = 0.6\) and \(\cos\theta = 0.8\), with coefficient of friction 0.5. Find its speed after it has slid 4 m down the slope. Take \(g = 10\).
Height lost: \(4 \times 0.6 = 2.4\) m, so GPE lost \(= 5 \times 10 \times 2.4 = 120\) J. Friction: \(R = 5 \times 10 \times 0.8 = 40\) N, \(F = 0.5 \times 40 = 20\) N, so the work done against friction is \(20 \times 4 = 80\) J.
\[120 - 80 = \tfrac12 \times 5 \times v^2 \quad\Rightarrow\quad v^2 = 16 \quad\Rightarrow\quad v = 4\ \mathrm{m\,s^{-1}}\]
This agrees with the same slope in [Newton's laws and connected particles](#math.m.newton), where the acceleration was \(2\ \mathrm{m\,s^{-2}}\), so \(v^2 = 2 \times 2 \times 4 = 16\). ✓
:::

:::warn Energy slips
- Mixing up the signs: work done **against** friction takes energy away. It should be subtracted on the energy-in side.
- Using the **vertical** height for GPE but the **slope** distance for friction work. On a slope of length \(s\), the height is \(s\sin\theta\), and friction work is \(F \times s\).
- Forgetting that the normal reaction does no work (it is perpendicular to the motion).
- Using \(F = ma\) and \(\text{KE}\) in the same equation. Use one method per equation.
- Writing \(mgh\) when the object ends below the reference level; \(h\) is then negative.
:::

## Power

:::def Power
Power is the rate of doing work: how much work is done per second. Its unit is the watt (W): 1 W is 1 J s⁻¹. Average power \(=\dfrac{\text{work done}}{\text{time taken}}\).
:::

If a constant force \(F\) acts on an object moving at speed \(v\) in the direction of the force, the work done per second is \(F\) times the distance moved per second, so:

:::key Power, force and speed
\[P = Fv\]
- \(P\) is the power in watts, \(F\) is the **driving force** in newtons and \(v\) is the speed in \(\mathrm{m\,s^{-1}}\). 1 kW \(= 1000\) W.
- For a vehicle, \(F\) is the driving force of the engine. It is not the resultant force: the resultant force is \(F\) minus resistances (and minus the weight component on a slope).
- Use \(F = ma\) with the resultant force to find acceleration: \(\dfrac{P}{v} - R_{\text{resistance}} - mg\sin\theta = ma\).
- At the **maximum speed**, the acceleration is 0, so the driving force equals the total resistance (plus the weight component on a hill).
:::

:::eg A crane lifts a 500 kg load vertically at a constant speed of \(0.8\ \mathrm{m\,s^{-1}}\). Find the power needed. Take \(g = 10\).
Constant speed means the lifting force equals the weight: \(F = 500 \times 10 = 5000\) N.
\[P = Fv = 5000 \times 0.8 = 4000\ \text{W} = 4\ \text{kW}\]
In 30 s the crane does \(4000 \times 30 = 120\,000\) J of work.
:::

:::eg A car of mass 1200 kg has an engine of power 60 kW. On a horizontal road the resistance to motion is constant at 1500 N. Find (a) the maximum speed, (b) the acceleration when the speed is \(30\ \mathrm{m\,s^{-1}}\).
(a) At maximum speed \(a = 0\), so the driving force equals the resistance: \(F = 1500\) N.
\[60\,000 = 1500v \quad\Rightarrow\quad v = 40\ \mathrm{m\,s^{-1}}\]
(b) At \(30\ \mathrm{m\,s^{-1}}\): \(F = \dfrac{60\,000}{30} = 2000\) N. Then
\[2000 - 1500 = 1200a \quad\Rightarrow\quad a = 0.417\ \mathrm{m\,s^{-2}}\]
The acceleration falls to 0 as the speed approaches \(40\ \mathrm{m\,s^{-1}}\).
:::

:::eg The same car (1200 kg, power 60 kW, resistance 1500 N) drives up a hill inclined at \(\theta\) to the horizontal, where \(\sin\theta = \dfrac{1}{20}\). Find the maximum speed, and the acceleration at \(20\ \mathrm{m\,s^{-1}}\). Take \(g = 10\).
The weight component down the slope is \(1200 \times 10 \times \tfrac{1}{20} = 600\) N.
Maximum speed: \(F = 1500 + 600 = 2100\) N, so \(v = \dfrac{60\,000}{2100} = 28.6\ \mathrm{m\,s^{-1}}\).
At \(20\ \mathrm{m\,s^{-1}}\): \(F = \dfrac{60\,000}{20} = 3000\) N.
\[3000 - 1500 - 600 = 1200a \quad\Rightarrow\quad a = 0.75\ \mathrm{m\,s^{-2}}\]
:::

:::tip Choosing between \(P = Fv\) and \(P = \text{work}/\text{time}\)
If a question gives a speed, use \(P = Fv\) to find the force or power at that moment. If it gives the work done and the time, use \(P = W/t\) (average power). The work done by the engine in time \(t\) at constant power is \(Pt\).
:::

## Exam-style questions

:::eg (Exam style) A particle \(P\) of mass 0.5 kg is released from rest at the point \(A\) on a smooth curved track. \(A\) is 2.5 m above the horizontal level of the point \(B\) at the foot of the track. The particle then moves along a rough horizontal surface with coefficient of friction 0.4 until it comes to rest at \(C\). Take \(g = 10\). (a) Find the speed of \(P\) at \(B\). (b) Find the distance \(BC\). [7 marks]
(a) The track is smooth, so energy is conserved. Take \(B\) as the reference level:
\[0.5 \times 10 \times 2.5 = \tfrac12 \times 0.5 \times v^2\] [M1 A1]
\[v^2 = 50 \quad\Rightarrow\quad v = 7.07\ \mathrm{m\,s^{-1}}\] [A1]

(b) On the horizontal surface \(R = 0.5 \times 10 = 5\) N, so \(F = 0.4 \times 5 = 2\) N. [B1]
The work done against friction equals the kinetic energy lost:
\[2 \times BC = \tfrac12 \times 0.5 \times 50 = 12.5\] [M1 A1]
\[BC = 6.25\ \text{m}\] [A1]
:::

:::eg (Exam style) A car of mass 1500 kg is driven up a straight hill inclined at \(\theta\) to the horizontal, where \(\sin\theta = \tfrac1{30}\). The engine works at a constant rate of 45 kW and the resistance to motion is 900 N. Take \(g = 10\). (a) Show that the maximum speed up the hill is about \(32.1\ \mathrm{m\,s^{-1}}\). (b) Find the acceleration when the speed is \(15\ \mathrm{m\,s^{-1}}\). (c) The car reaches the top of the hill and moves on level ground with the same power and resistance. State its acceleration at \(15\ \mathrm{m\,s^{-1}}\) and its maximum speed. [8 marks]
(a) At maximum speed, \(a = 0\) so the driving force is \(F = 900 + 1500 \times 10 \times \tfrac1{30} = 1400\) N. [M1 A1] \(v = \dfrac{P}{F} = \dfrac{45\,000}{1400} = 32.1\ \mathrm{m\,s^{-1}}\). [A1]

(b) \(F = \dfrac{45\,000}{15} = 3000\) N. [B1] \(3000 - 900 - 500 = 1500a\), so \(a = 1.07\ \mathrm{m\,s^{-2}}\). [M1 A1]

(c) On the level: \(3000 - 900 = 1500a\), so \(a = 1.4\ \mathrm{m\,s^{-2}}\). [M1 A1] Maximum speed \(= \dfrac{45\,000}{900} = 50\ \mathrm{m\,s^{-1}}\). [A1]
:::

:::exam Technique
- Say which principle you are using: "work–energy principle" or "conservation of energy".
- Write energy equations in words first (KE gained = work done by driving force − work done against resistance − GPE gained), then substitute.
- Show the force \(F = P/v\) separately, then the \(F = ma\) equation. Mark schemes award method marks for each.
- A "constant rate" of working means constant \(P\): the driving force changes as the speed changes.
- Give final answers to 3 s.f., with units (J, W, kW, \(\mathrm{m\,s^{-1}}\)).
:::

:::board
- **Edexcel IAL and UK boards** use \(g = 9.8\). Work, energy and power are in IAL M2 and in UK A Level Mechanics.
- Cambridge P4 uses \(Fd\cos\theta\) and does not use the scalar product.
:::

:::try Start easy, finish at exam standard
Q: A force of 40 N acts at \(30^\circ\) to the direction of motion and moves an object 5 m. Find the work done.
A: \(40 \times 5 \times \cos 30^\circ = 173\) J.
Q: Find the kinetic energy of a 70 kg cyclist moving at \(8\ \mathrm{m\,s^{-1}}\), and the potential energy gained if she rides up a hill rising 12 m. Take \(g = 10\).
A: KE \(= \tfrac12 \times 70 \times 64 = 2240\) J. GPE \(= 70 \times 10 \times 12 = 8400\) J.
Q: A 2 kg ball is dropped from 20 m above the ground. Find its speed on landing. Take \(g = 10\).
A: \(2 \times 10 \times 20 = \tfrac12 \times 2 \times v^2\), so \(v^2 = 400\) and \(v = 20\ \mathrm{m\,s^{-1}}\).
Q: A 3 kg particle is projected up a smooth slope inclined at \(30^\circ\) at \(8\ \mathrm{m\,s^{-1}}\). Find how far up the slope it travels before stopping. Take \(g = 10\).
A: KE lost \(= \tfrac12 \times 3 \times 64 = 96\) J. GPE gained \(= 3 \times 10 \times s\sin 30^\circ = 15s\). So \(15s = 96\) and \(s = 6.4\) m.
Q: A 2 kg particle moving at \(6\ \mathrm{m\,s^{-1}}\) on a rough horizontal surface comes to rest after 9 m. Find the friction force and the coefficient of friction. Take \(g = 10\).
A: Work against friction \(= \tfrac12 \times 2 \times 36 = 36\) J \(= F \times 9\), so \(F = 4\) N. \(R = 20\) N, so \(\mu = \dfrac{4}{20} = 0.2\).
Q: A crane lifts a 250 kg load at a constant speed of \(1.2\ \mathrm{m\,s^{-1}}\). Find the power. Take \(g = 10\).
A: \(F = 2500\) N and \(P = 2500 \times 1.2 = 3000\) W.
Q: A car of mass 1000 kg has an engine of power 50 kW and a constant resistance of 1250 N. Find its maximum speed on a level road and its acceleration at \(20\ \mathrm{m\,s^{-1}}\).
A: Maximum speed: \(\dfrac{50\,000}{1250} = 40\ \mathrm{m\,s^{-1}}\). At 20: \(F = 2500\) N, so \(2500 - 1250 = 1000a\) and \(a = 1.25\ \mathrm{m\,s^{-2}}\).
Q: A cyclist and bicycle of total mass 80 kg climb a slope at a steady \(5\ \mathrm{m\,s^{-1}}\) with power 200 W against a constant resistance of 15 N. Find the angle of the slope. Take \(g = 10\).
A: \(F = \dfrac{200}{5} = 40\) N. Constant speed: \(40 = 15 + 800\sin\theta\), so \(\sin\theta = \dfrac{25}{800} = 0.03125\) and \(\theta = 1.79^\circ\).
Q: (Exam style) A lorry of mass 2000 kg goes up a straight road 100 m long, rising 5 m, and its speed increases from \(10\ \mathrm{m\,s^{-1}}\) to \(15\ \mathrm{m\,s^{-1}}\). The resistance to motion is 800 N throughout. Find the constant driving force. Take \(g = 10\). [5 marks]
A: Work by the driving force \(= 100D\). Work against resistance \(= 800 \times 100 = 80\,000\) J. GPE gained \(= 2000 \times 10 \times 5 = 100\,000\) J. KE gained \(= \tfrac12 \times 2000 \times (225 - 100) = 125\,000\) J. [B1 B1 B1] \(100D - 80\,000 = 100\,000 + 125\,000\) [M1], so \(D = 3050\) N. [A1]
Q: (Exam style) A car of mass 1500 kg has a maximum speed of \(50\ \mathrm{m\,s^{-1}}\) on a level road with resistance 1200 N. Find the power of the engine, and the acceleration at \(30\ \mathrm{m\,s^{-1}}\). [5 marks]
A: At maximum speed \(F = 1200\) N, so \(P = 1200 \times 50 = 60\,000\) W = 60 kW. [M1 A1] At \(30\ \mathrm{m\,s^{-1}}\): \(F = \dfrac{60\,000}{30} = 2000\) N. [B1] \(2000 - 1200 = 1500a\), so \(a = 0.533\ \mathrm{m\,s^{-2}}\). [M1 A1]
:::

:::quiz Check your understanding
? A force of 10 N acts at \(90^\circ\) to the direction of motion over 5 m. The work done by the force is:
- 50 J
- 25 J
+ 0 J
- 5 J
> \(W = Fd\cos 90^\circ = 0\). A force at right angles to the motion does no work, like the normal reaction on a flat surface.
? Which of these is the kinetic energy of a 4 kg particle moving at \(3\ \mathrm{m\,s^{-1}}\)?
- 12 J
- 36 J
+ 18 J
- 6 J
> KE \(= \tfrac12 mv^2 = \tfrac12 \times 4 \times 9 = 18\) J. Forgetting the half gives 36, and using \(mv\) gives 12.
? A car's engine produces a driving force of 2000 N at a speed of \(20\ \mathrm{m\,s^{-1}}\). The power is:
- 100 W
+ 40 kW
- 400 W
- 40 W
> \(P = Fv = 2000 \times 20 = 40\,000\) W \(= 40\) kW.
? A car moving at constant maximum speed on a level road has driving force 1800 N. The resistance is:
- 0 N
- more than 1800 N
+ 1800 N
- less than 1800 N
> At constant speed the acceleration is zero, so the driving force equals the resistance.
? A particle slides down a smooth curved slide from rest through a height of 3.2 m. Its speed at the bottom is (\(g = 10\)):
- 3.2
+ 8
- 64
- 32
> \(v^2 = 2gh = 2 \times 10 \times 3.2 = 64\), so \(v = 8\). Stopping at \(v^2 = 64\) without taking the square root is the usual slip.
:::

:::recap
- Work \(W = Fd\cos\theta\) (joules). A force at \(90^\circ\) to the motion does no work.
- \(\text{KE} = \tfrac12 mv^2\). \(\text{GPE} = mgh\). Both are scalars.
- Work–energy: work by driving forces − work against resistances = change in KE + change in GPE. On a smooth track energy is conserved, whatever the shape.
- Power \(P = Fv\) (watts), average power \(= \dfrac{\text{work}}{\text{time}}\). The driving force is \(P/v\).
- Maximum speed: acceleration zero, so driving force = resistance (+ \(mg\sin\theta\) on a hill).
- Acceleration of a vehicle: \(\dfrac{P}{v} - \text{resistance} - mg\sin\theta = ma\).
:::

:::note Learn more online
- **Watch:** [The work–energy principle](https://www.examsolutions.net/tutorials/conservation-of-energy-work-energy-principle/) · ExamSolutions · energy in, energy out, work against resistance
- **Watch:** [Car accelerating on a hill](https://www.examsolutions.net/tutorials/car-accelerating-along-horizontal-hill/) · ExamSolutions · P = Fv and F = ma together
- **Practise:** [CAIE Mechanics work and energy exam questions](https://www.savemyexams.com/a-level/maths/cie/20/mechanics/topic-questions/energy-work-and-power/work-and-energy/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Energy Skate Park](https://phet.colorado.edu/en/simulations/energy-skate-park) · PhET · KE and GPE trade places on a curved track
- **Explore:** [The Ramp](https://phet.colorado.edu/en/simulations/the-ramp) · PhET · work done against friction on a slope
- **Papers:** [9709 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-4) · Physics & Maths Tutor · papers with mark schemes *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Projectiles and moments](#math.m.projectiles).
