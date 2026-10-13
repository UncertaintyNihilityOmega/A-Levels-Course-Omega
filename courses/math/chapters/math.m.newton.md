@chapter math.m.newton
@title Newton's laws and connected particles
@level as
@paper CAIE P4 · Edexcel IAL M1 · UK Mechanics
@time 8–10 hours
@summary Newton's second law links the resultant force on an object to its acceleration. You will learn to apply \(F = ma\) to objects on rough and smooth surfaces, lifts, slopes, particles joined by strings over pulleys, and a car towing a trailer, and to deal with a string that goes slack.

:::why
Kinematics describes motion; Newton's laws explain it. Every engineer who works out the force on a lift cable, the braking force of a train or the tension in a tow-bar is using the one equation in this chapter, \(F = ma\). It is also the heart of Paper 4: a typical question combines a force diagram, an equation of motion and a constant acceleration equation.
:::

**Before you start**, you need force diagrams, resolving and friction from [Forces and equilibrium](#math.m.forces), and the constant acceleration equations from [Kinematics](#math.m.kinematics).

:::try Warm-up
Q: A car accelerates uniformly from \(8\ \mathrm{m\,s^{-1}}\) to \(20\ \mathrm{m\,s^{-1}}\) over 84 m. Find its acceleration. (from [Kinematics](#math.m.kinematics))
A: \(v^2 = u^2 + 2as\), so \(400 = 64 + 168a\) and \(a = 2\ \mathrm{m\,s^{-2}}\).
Q: A block of mass 6 kg is on a smooth slope at \(30^\circ\) to the horizontal. Find the component of its weight down the slope and the normal reaction. Take \(g = 10\). (from [Forces and equilibrium](#math.m.forces))
A: Down the slope: \(60\sin 30^\circ = 30\) N. Normal reaction: \(R = 60\cos 30^\circ = 52.0\) N.
Q: Solve \(T - 12 = 3a\) and \(40 - T = 4a\) for \(a\) and \(T\). (from [Algebra from scratch](#math.f.algebra))
A: Add the equations: \(28 = 7a\), so \(a = 4\). Then \(T = 12 + 12 = 24\). Check: \(40 - 24 = 16 = 4 \times 4\).
:::

## Newton's laws of motion

:::key Newton's laws
1. **First law.** An object stays at rest, or moves in a straight line at constant speed, unless a resultant force acts on it.
2. **Second law.** The resultant force on an object equals its mass times its acceleration, in the direction of the resultant:
\[F = ma\]
3. **Third law.** If object A exerts a force on object B, then B exerts an equal and opposite force on A.
:::

:::def Newton and weight
One **newton** (N) is the force that gives a mass of 1 kg an acceleration of \(1\ \mathrm{m\,s^{-2}}\). The **weight** of an object is the force of gravity on it, \(W = mg\), acting vertically downwards.
:::

- \(F\) is the **resultant** (net) force in newtons (N), \(m\) is the mass in kilograms and \(a\) is the acceleration in \(\mathrm{m\,s^{-2}}\).
- Weight \(W = mg\), with \(g = 10\ \mathrm{m\,s^{-2}}\) in Cambridge questions that say so. A 5 kg mass has weight 50 N.
- The mass is **constant** in this course, and the force is constant unless the question says otherwise. Constant force gives constant acceleration, so the suvat equations apply.

:::steps
1. Draw a **separate force diagram** for each object, showing every force on it (weight, normal reaction, friction, tension, driving force, resistance).
2. Mark the direction of the acceleration, and choose a positive direction to match it.
3. Resolve forces along the line of motion (and, where needed, perpendicular to it).
4. Write \(F = ma\): **resultant force in the direction of motion = mass × acceleration**. Forces helping the motion are positive, forces against it are negative.
5. Solve, then use \(v = u + at\) and the other equations if time, speed or distance is wanted.
:::

:::eg A 4 kg block on a rough horizontal table is pulled by a horizontal force of 20 N. The friction force is 8 N. Find its acceleration, and its speed after 5 s from rest.
The resultant horizontal force is \(20 - 8 = 12\) N. Then \(F = ma\) gives
\[12 = 4a \quad\Rightarrow\quad a = 3\ \mathrm{m\,s^{-2}}\]
\(v = u + at = 0 + 3 \times 5 = 15\ \mathrm{m\,s^{-1}}\).
:::

:::warn Weight is not mass
Mass (kg) does not change from place to place. Weight (N) is the force of gravity. In \(F = ma\) use the mass, and use the weight \(mg\) only when gravity is one of the forces.
:::

## Lifts and vertical motion

For vertical motion the forces are the weight \(mg\) (down) and a support force upwards: the tension in a cable or the normal reaction \(R\) from a floor. If the object accelerates upwards, the upward force is **larger** than the weight.

:::eg A man of mass 70 kg stands in a lift that accelerates upwards at \(1.5\ \mathrm{m\,s^{-2}}\). Find the force of the floor on him. Take \(g = 10\).
Let \(R\) be the reaction from the floor. Take up as positive:
\[R - 70 \times 10 = 70 \times 1.5 \quad\Rightarrow\quad R = 700 + 105 = 805\ \text{N}\]
He feels heavier than usual, because \(R > mg\).
:::

:::eg A lift of mass 400 kg carries a person of mass 80 kg. It accelerates upwards at \(0.5\ \mathrm{m\,s^{-2}}\). Find the tension in the lift cable and the force between the person and the floor. Take \(g = 10\).
Whole system, mass 480 kg, with tension \(T\) upwards and weight \(4800\) N downwards:
\[T - 4800 = 480 \times 0.5 \quad\Rightarrow\quad T = 5040\ \text{N}\]
Person only: \(R - 800 = 80 \times 0.5\), so \(R = 840\) N.
:::

:::tip Lift going down
If a lift accelerates **downwards** at \(a\), the weight is larger than the support: \(mg - R = ma\), so \(R = m(g - a)\). In free fall (\(a = g\)) the floor force is 0, which is the feeling of weightlessness.
:::

## Motion on a slope

On a plane inclined at \(\theta\) to the horizontal, resolve **along** the slope and **perpendicular** to it. The weight has two components: \(mg\sin\theta\) down the slope and \(mg\cos\theta\) into it. The reaction is perpendicular to the plane, and there is no acceleration perpendicular to it, so \(R = mg\cos\theta\) (unless other forces help or press).

:::eg A particle of mass 2 kg slides from rest down a smooth plane inclined at \(30^\circ\) to the horizontal. Find the acceleration and the speed after it has travelled 4 m. Take \(g = 10\).
The only force along the slope is \(mg\sin 30^\circ\), down the slope:
\[2 \times 10 \times \tfrac12 = 2a \quad\Rightarrow\quad a = 5\ \mathrm{m\,s^{-2}}\]
\(v^2 = 0 + 2 \times 5 \times 4 = 40\), so \(v = 6.32\ \mathrm{m\,s^{-1}}\).
The mass cancels, so on a smooth slope every mass has \(a = g\sin\theta\).
:::

When the slope is **rough**, friction acts along the slope **against** the motion. Moving: \(F = \mu R\) with \(R = mg\cos\theta\). The acceleration is **different** up and down the slope, because friction reverses direction relative to gravity's component.

:::eg A box of mass 5 kg moves on a rough plane inclined at \(\theta\), where \(\sin\theta = \tfrac35\) and \(\cos\theta = \tfrac45\). The coefficient of friction is 0.5. Find the acceleration (a) when the box slides down, (b) when the box is moving up. Take \(g = 10\).
\(R = 5 \times 10 \times \tfrac45 = 40\) N, so the friction force is \(F = 0.5 \times 40 = 20\) N. The component of weight down the slope is \(5 \times 10 \times \tfrac35 = 30\) N.

(a) Sliding **down**: friction acts up the slope.
\[30 - 20 = 5a \quad\Rightarrow\quad a = 2\ \mathrm{m\,s^{-2}}\ \text{down the slope}\]

(b) Moving **up**: friction acts down the slope, with the weight component.
\[30 + 20 = 5a \quad\Rightarrow\quad a = 10\ \mathrm{m\,s^{-2}}\ \text{(deceleration) down the slope}\]
If projected up the slope at \(8\ \mathrm{m\,s^{-1}}\), it stops after \(0 = 64 - 2 \times 10 \times s\), so \(s = 3.2\) m.
:::

:::eg A force \(T\) of 20 N acts on a 4 kg block on a rough horizontal floor, at an angle \(\theta\) above the horizontal, where \(\sin\theta = \tfrac35\) and \(\cos\theta = \tfrac45\). The coefficient of friction is 0.3. Find the acceleration. Take \(g = 10\).
Vertically (no vertical acceleration): \(R + 20 \times \tfrac35 = 40\), so \(R = 28\) N. The pull reduces the force on the floor.
Friction: \(F = 0.3 \times 28 = 8.4\) N. Horizontally:
\[20 \times \tfrac45 - 8.4 = 4a \quad\Rightarrow\quad 16 - 8.4 = 4a \quad\Rightarrow\quad a = 1.9\ \mathrm{m\,s^{-2}}\]
:::

## Connected particles

Two particles joined by a string (or rod) usually move together with the same speed and acceleration. A string described as **light** has no mass and one described as **inextensible** does not stretch. A pulley that is **smooth** has no friction. Then:

:::key Connected particles
- The tension in a light string is the same throughout, including either side of a smooth pulley.
- The acceleration is the same size for both particles, because the string is inextensible: one goes up as the other comes down.
- Write \(F = ma\) **separately for each particle**, and solve the equations together. Alternatively, treat the particles as one system when the tension is not needed.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 400 200" role="img" aria-label="A light string passes over a smooth fixed pulley. A 5 kg particle hangs on the left and a 3 kg particle hangs on the right. Tension T acts upwards on each particle, and weights 5g and 3g act downwards."><path class="ln" d="M300 14V34"/><circle class="f2 s-acc sw2" cx="300" cy="50" r="16"/><path class="ln" d="M284 50V135M316 50V95"/><rect class="f1 s-acc sw2" x="264" y="135" width="40" height="36"/><rect class="f1 s-acc sw2" x="296" y="95" width="40" height="36"/><text class="tl" x="284" y="158" text-anchor="middle">5 kg</text><text class="tl" x="316" y="118" text-anchor="middle">3 kg</text><path class="c2" d="M232 90V125" marker-end="url(#ah)"/><text class="tl" x="222" y="112" text-anchor="end">a</text><path class="c2" d="M368 125V90" marker-end="url(#ah)"/><text class="tl" x="378" y="112">a</text><text class="tl" x="254" y="76" text-anchor="end">T</text><text class="tl" x="346" y="76">T</text></svg><figcaption>Particles of mass 5 kg and 3 kg over a smooth pulley: the heavier one goes down and the lighter one goes up, with the same acceleration \(a\) and the same tension \(T\).</figcaption></figure>
:::

:::eg Particles of mass 5 kg and 3 kg are joined by a light inextensible string over a smooth pulley and released from rest. Find the acceleration and the tension. Take \(g = 10\).
The 5 kg particle accelerates down, the 3 kg particle accelerates up, both at \(a\).
\[\text{5 kg (down):}\quad 50 - T = 5a\]
\[\text{3 kg (up):}\quad T - 30 = 3a\]
Add the equations to eliminate \(T\): \(20 = 8a\), so \(a = 2.5\ \mathrm{m\,s^{-2}}\). Then \(T = 30 + 3 \times 2.5 = 37.5\) N.
Check in the first equation: \(50 - 37.5 = 12.5 = 5 \times 2.5\). ✓
:::

:::proof Why a pulley system accelerates at \(\dfrac{(m_1 - m_2)g}{m_1 + m_2}\)
Let particle 1 (mass \(m_1\)) be the heavier one. The string is light and inextensible and the pulley is smooth, so the tension \(T\) is the same everywhere and both particles have acceleration \(a\): particle 1 downwards, particle 2 upwards.

Particle 1, resultant force downwards: \(m_1g - T = m_1a\).

Particle 2, resultant force upwards: \(T - m_2g = m_2a\).

Add the two equations. The tension cancels:
\[m_1g - m_2g = (m_1 + m_2)a \quad\Rightarrow\quad a = \frac{(m_1 - m_2)g}{m_1 + m_2}\]
Put this back into particle 2's equation:
\[T = m_2(g + a) = \frac{2m_1m_2g}{m_1 + m_2}\]
This shows two facts. If \(m_1 = m_2\) then \(a = 0\), which is balance. If \(m_2\) is tiny, \(a \to g\) and \(T \to 0\), which is free fall. For 5 kg and 3 kg with \(g = 10\): \(a = \dfrac{2 \times 10}{8} = 2.5\) and \(T = \dfrac{2 \times 15 \times 10}{8} = 37.5\) N, as in the example.
:::

:::eg A 4 kg block sits on a rough horizontal table (coefficient of friction 0.25) and is joined by a light string over a smooth pulley at the table edge to a 2 kg block hanging freely. The system is released from rest. Find the acceleration and the tension in the string. Take \(g = 10\).
Friction on the table block: \(F = 0.25 \times 40 = 10\) N (since \(R = 40\) N).
\[\text{4 kg (along the table):}\quad T - 10 = 4a\]
\[\text{2 kg (down):}\quad 20 - T = 2a\]
Adding: \(10 = 6a\), so \(a = \tfrac53 = 1.67\ \mathrm{m\,s^{-2}}\). Then \(T = 20 - 2 \times \tfrac53 = \tfrac{50}{3} = 16.7\) N.
:::

The widget below puts a 4 kg block on a rough slope at \(30^\circ\) (\(\mu = 0.25\)), joined over a pulley at the top to a hanging 3 kg mass. It shows the forces and says whether the block stays still or slides, with the acceleration (the start is from rest). Check its answer by hand: the hanging mass pulls the block up the slope with \(3 \times 10 = 30\) N and the block's weight pulls down with 20 N, so the net pull up the slope is 10 N, more than the greatest friction 8.66 N. Then change the angle or the hanging mass and predict the result before you read it.

:::html
<div class="widget" data-w="incline" data-angle="30" data-mu="0.25" data-mass="4" data-m2="3"></div>
:::

### When a particle hits the ground

A hanging particle that lands stops, and the string goes **slack**: the tension drops to zero. The other particle is no longer pulled, so it moves under the forces on it alone. It may decelerate (if gravity or friction opposes it), so you need a second stage with a new equation of motion.

:::eg In the 5 kg and 3 kg pulley system above, the 5 kg particle is released from rest 2 m above the floor. Find its speed on landing, and the greatest height the 3 kg particle reaches above its starting position. Take \(g = 10\). (Assume the pulley is high enough that the 3 kg particle never reaches it.)
Stage 1: \(a = 2.5\ \mathrm{m\,s^{-2}}\) for 2 m, so \(v^2 = 2 \times 2.5 \times 2 = 10\) and \(v = 3.16\ \mathrm{m\,s^{-1}}\). Both particles have this speed when the 5 kg particle lands.

Stage 2: the string goes slack. The 3 kg particle moves up freely with deceleration \(g = 10\): \(0 = 10 - 2 \times 10 \times s\), so \(s = 0.5\) m.
The 3 kg particle has risen \(2 + 0.5 = 2.5\) m above its starting position.
:::

:::eg (Exam style) Particle \(P\) of mass 4 kg is on a smooth plane inclined at \(30^\circ\) to the horizontal. A light inextensible string joins \(P\) to a particle \(Q\) of mass 2.5 kg, passing over a smooth pulley at the top of the plane so that \(Q\) hangs vertically. The system is released from rest with the string taut. (a) Find the acceleration of \(Q\) and the tension in the string. (b) \(Q\) hits the ground after falling 1.2 m. Find the speed of \(P\) at that moment and the further distance \(P\) moves up the plane before it first stops. Take \(g = 10\). [11 marks]
(a) For \(Q\) (down): \(25 - T = 2.5a\). [M1 A1] For \(P\) (up the slope): \(T - 4 \times 10 \times \sin 30^\circ = 4a\), that is \(T - 20 = 4a\). [M1 A1]
Adding: \(5 = 6.5a\), so \(a = \tfrac{10}{13} = 0.769\ \mathrm{m\,s^{-2}}\). [M1 A1] \(T = 20 + 4a = 23.1\) N. [A1]

(b) \(v^2 = 2 \times 0.7692 \times 1.2 = 1.846\), so \(v = 1.36\ \mathrm{m\,s^{-1}}\). [M1 A1]
After \(Q\) lands the string is slack, so \(P\) decelerates under its own weight component: \(a = -10\sin 30^\circ = -5\). Then \(0 = 1.846 - 2 \times 5 \times s\), so \(s = 0.185\) m. [M1 A1]
:::

## Cars, trailers and resistances

A car pulls a trailer with a light rope or a rigid tow-bar. The **driving force** acts on the car. Each vehicle also experiences a **resistance** (air and rolling friction) unless the question says there is none. The rope or bar exerts a force on each vehicle: a **tension** if it pulls, or a **thrust** if a rigid bar pushes.

:::eg A car of mass 800 kg tows a trailer of mass 400 kg along a straight horizontal road by a light tow-bar. The driving force is 2200 N. The resistances are 250 N on the car and 150 N on the trailer. Find the acceleration and the force in the tow-bar. Take \(g = 10\) where needed.
Whole system (1200 kg): \(2200 - 250 - 150 = 1200a\), so \(a = 1.5\ \mathrm{m\,s^{-2}}\).
Trailer only, with tension \(T\) pulling it forward: \(T - 150 = 400 \times 1.5\), so \(T = 750\) N.
Check on the car: \(2200 - 250 - 750 = 1200 = 800 \times 1.5\). ✓
:::

If the driving force is removed and the car brakes, the car may slow faster than the trailer would, so a **rigid** tow-bar is compressed and exerts a thrust on the trailer's front. A negative answer for \(T\) in a calculation means the bar is in thrust, not tension.

:::warn Frequent mistakes in connected-particle problems
- Using one equation for both particles with different signs for the same acceleration. Choose the direction of motion for each particle and write both equations with their own positive direction.
- Forgetting that friction appears on the rough-surface particle only and acts against the motion.
- Treating the tension as the weight of the hanging mass. It equals the weight only when there is no acceleration.
- After a particle lands, carrying on with the same acceleration. The string is slack, so the system changes.
- Resolving the weight on a slope the wrong way round: \(mg\sin\theta\) is **along** the slope.
:::

:::exam Technique
- Draw a separate force diagram for each particle, with the acceleration marked.
- Write each equation as "resultant force = mass × acceleration" so that the method mark is clear.
- "Light" and "smooth pulley" mean the tension is the same on both sides. "Inextensible" means the same acceleration.
- Use the value of \(g\) the question gives (10 in Cambridge papers), and keep the answers exact or to 3 s.f.
- If asked to "show that" the acceleration has a given value, use the given value to check your final answer.
:::

:::board
- **Edexcel IAL and UK boards**: \(g = 9.8\ \mathrm{m\,s^{-2}}\). Newton's laws and connected particles are in IAL M1 (and in UK Mechanics, with vector forces in \(\mathbf{i}\) and \(\mathbf{j}\) notation).
- **CAIE** does not use vector notation for forces in P4, and always tells you the value of \(g\) to use.
:::

:::eg Spot the error: friction on a slope
A student answered this question [6 marks]: "A box of mass 5 kg slides from rest down a rough plane inclined at \(30^\circ\) to the horizontal. The coefficient of friction is 0.2. Find the acceleration of the box. Take \(g = 10\)."

Line 1: \(R = 5 \times 10 = 50\) N.
Line 2: \(F = \mu R = 0.2 \times 50 = 10\) N.
Line 3: \(50\sin 30^\circ - 10 = 5a\), so \(25 - 10 = 5a\).
Line 4: \(a = 3\ \mathrm{m\,s^{-2}}\).

**Line 1 scores [M0 A0]**: on a slope the normal reaction balances only the component of weight into the slope, so \(R = mg\cos\theta\), not \(mg\). **Line 2 earns [M1]**: the method \(F = \mu R\) is right, and it is followed through from the student's own \(R\). **Line 3 earns [M1 A0]**: a correct three-term equation of motion, but the friction value in it is wrong. **Line 4 scores [A0]**. The student scores 2 out of 6.

Correct working: \(R = 50\cos 30^\circ = 43.30\) N. [M1 A1] \(F = 0.2 \times 43.30 = 8.660\) N. [M1] Along the slope: \(50\sin 30^\circ - 8.660 = 5a\). [M1 A1] \(a = \dfrac{16.34}{5} = 3.27\ \mathrm{m\,s^{-2}}\). [A1]

**Check:** a smooth slope would give \(a = 10\sin 30^\circ = 5\). Friction slows the box, so the answer must be below 5, and 3.27 is. The student's 3 is also below 5, so the check does not catch this slip: the friction value has to be checked on its own, since \(\mu mg\) is bigger than \(\mu mg\cos\theta\) on every slope.
:::

:::try Start easy, finish at exam standard
Q: A car of mass 1200 kg has a resultant force of 3000 N acting on it. Find its acceleration.
A: \(a = \dfrac{F}{m} = \dfrac{3000}{1200} = 2.5\ \mathrm{m\,s^{-2}}\).
Q: A 5 kg block is pulled across a rough horizontal floor by a horizontal force of 30 N. The friction force is 10 N. Find the acceleration and the speed after 6 s from rest.
A: \(30 - 10 = 5a\), so \(a = 4\ \mathrm{m\,s^{-2}}\). \(v = 4 \times 6 = 24\ \mathrm{m\,s^{-1}}\).
Q: A woman of mass 60 kg stands in a lift that accelerates downwards at \(2\ \mathrm{m\,s^{-2}}\). Find the force between her and the floor. Take \(g = 10\).
A: \(60 \times 10 - R = 60 \times 2\), so \(R = 600 - 120 = 480\) N.
Q: A 4 kg particle is on a rough plane inclined at \(30^\circ\) to the horizontal with coefficient of friction 0.2. Find its acceleration when it slides down. Take \(g = 10\).
A: \(R = 40\cos 30^\circ = 34.64\) N, \(F = 0.2 \times 34.64 = 6.93\) N. \(40\sin 30^\circ - 6.93 = 4a\), so \(20 - 6.93 = 4a\) and \(a = 3.27\ \mathrm{m\,s^{-2}}\).
Q: Particles of mass 4 kg and 6 kg are joined by a light string over a smooth pulley and released from rest. Find the acceleration and the tension. Take \(g = 10\).
A: \(60 - T = 6a\) and \(T - 40 = 4a\). Adding: \(20 = 10a\), so \(a = 2\ \mathrm{m\,s^{-2}}\). \(T = 40 + 8 = 48\) N.
Q: A 5 kg block is on a smooth horizontal table and is joined by a light string over a smooth pulley at the edge to a 3 kg block hanging freely. Find the acceleration and the tension. Take \(g = 10\).
A: Table block: \(T = 5a\). Hanging block: \(30 - T = 3a\). Adding: \(30 = 8a\), so \(a = 3.75\ \mathrm{m\,s^{-2}}\). \(T = 18.75\) N.
Q: A car of mass 900 kg pulls a trailer of mass 300 kg with a driving force of 3000 N. The resistances are 600 N on the car and 200 N on the trailer. Find the acceleration and the tension in the tow-bar.
A: \(3000 - 800 = 1200a\), so \(a = 1.83\ \mathrm{m\,s^{-2}}\). Trailer: \(T - 200 = 300 \times 1.8333\), so \(T = 750\) N.
Q: Explain why the tension in a light string passing over a smooth pulley is the same on both sides.
A: A light string has no mass, so the net force on any piece of it must be zero for it to have the acceleration it does. A smooth pulley exerts no friction along the string, so nothing changes the tension as the string passes over it.
Q: (Exam style) Particles \(A\) (mass 6 kg) and \(B\) (mass 2 kg) are joined by a light string over a smooth pulley. \(A\) is held at rest 1.6 m above the floor, with both parts of the string vertical, and then released. (a) Find the acceleration of \(A\) and the tension in the string. (b) Find the speed with which \(A\) hits the floor. (c) Find the greatest height of \(B\) above its starting position. Take \(g = 10\). [9 marks]
A: (a) \(A\): \(60 - T = 6a\). \(B\): \(T - 20 = 2a\). [M1 A1 A1] Adding: \(40 = 8a\), so \(a = 5\ \mathrm{m\,s^{-2}}\), and \(T = 20 + 10 = 30\) N. [A1] (b) \(v^2 = 2 \times 5 \times 1.6 = 16\), so \(v = 4\ \mathrm{m\,s^{-1}}\). [M1 A1] (c) After \(A\) lands the string is slack and \(B\) decelerates at 10: \(0 = 16 - 20s\), so \(s = 0.8\) m. [M1 A1] The greatest height above the start is \(1.6 + 0.8 = 2.4\) m. [A1]
Q: (Exam style) A 4 kg block is on a rough horizontal floor. A string at \(\theta\) above the horizontal, with \(\sin\theta = \tfrac35\), pulls it with tension \(T\). The coefficient of friction is 0.3. Find the least \(T\) for which the block is about to move. Take \(g = 10\). [6 marks]
A: Vertically: \(R = 40 - T\sin\theta = 40 - 0.6T\). [M1 A1] Limiting friction: \(F = 0.3R\). Horizontally: \(T\cos\theta = F\), so \(0.8T = 0.3(40 - 0.6T)\). [M1 A1] \(0.8T = 12 - 0.18T\), so \(0.98T = 12\) and \(T = 12.2\) N. [M1 A1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A woman of mass 60 kg stands on the floor of a lift. The lift accelerates downwards at \(1.2\ \mathrm{m\,s^{-2}}\). Find the force that the floor exerts on her. Take \(g = 10\).
A: Taking down as positive: \(600 - R = 60 \times 1.2\). [M1 A1] \(R = 528\) N. [A1]
Q: [5 marks] ★ A box of mass 8 kg is pulled from rest along rough horizontal ground by a horizontal force of 40 N. The coefficient of friction is 0.3. Find the acceleration of the box and the distance it travels in the first 3 seconds. Take \(g = 10\).
A: \(R = 80\) N, so \(F = 0.3 \times 80 = 24\) N. [B1] \(40 - 24 = 8a\), [M1] so \(a = 2\ \mathrm{m\,s^{-2}}\). [A1] \(s = \tfrac12 \times 2 \times 3^2\) [M1] \(= 9\) m. [A1]
Q: [3 marks] ★ A particle of mass 2 kg is released from rest on a smooth plane inclined at \(25^\circ\) to the horizontal. Find its speed after 3 seconds. Take \(g = 10\).
A: Down the slope: \(2 \times 10\sin 25^\circ = 2a\), [M1] so \(a = 10\sin 25^\circ = 4.226\ \mathrm{m\,s^{-2}}\). [A1] \(v = 4.226 \times 3 = 12.7\ \mathrm{m\,s^{-1}}\). [A1]
Q: [7 marks] ★★ Particles \(A\) of mass 6 kg and \(B\) of mass 2 kg are attached to the ends of a light inextensible string that passes over a smooth fixed pulley. Both particles hang freely and the string is taut. The system is released from rest. Find the acceleration of the particles and the tension in the string. Find also the speed of \(A\) after it has descended 1.5 m. Take \(g = 10\).
A: For \(A\) (down): \(60 - T = 6a\). [M1 A1] For \(B\) (up): \(T - 20 = 2a\). [M1 A1] Adding: \(40 = 8a\), so \(a = 5\ \mathrm{m\,s^{-2}}\) and \(T = 30\) N. [A1] \(v^2 = 2 \times 5 \times 1.5 = 15\), [M1] so \(v = 3.87\ \mathrm{m\,s^{-1}}\). [A1]
Q: [7 marks] ★★ A block \(P\) of mass 5 kg rests on a rough horizontal table. The coefficient of friction is 0.4. \(P\) is joined by a light inextensible string over a smooth pulley at the edge of the table to a particle \(Q\) of mass 3 kg, which hangs freely. The system is released from rest. Find the acceleration of \(P\) and the tension in the string. Take \(g = 10\).
A: \(R = 50\) N, so friction \(F = 0.4 \times 50 = 20\) N. [B1] For \(P\): \(T - 20 = 5a\). [M1 A1] For \(Q\): \(30 - T = 3a\). [M1 A1] Adding: \(10 = 8a\), so \(a = 1.25\ \mathrm{m\,s^{-2}}\). [A1] \(T = 20 + 5 \times 1.25 = 26.25\), so \(T = 26.3\) N. [A1]
Q: [5 marks] ★★ A block of mass 4 kg is pushed up a rough plane inclined at \(30^\circ\) to the horizontal by a force of 50 N acting parallel to a line of greatest slope. The coefficient of friction is 0.3. Find the acceleration of the block. Take \(g = 10\).
A: \(R = 40\cos 30^\circ = 34.64\) N. [B1] \(F = 0.3 \times 34.64 = 10.39\) N. [M1] Up the slope: \(50 - 40\sin 30^\circ - 10.39 = 4a\). [M1 A1] \(a = \dfrac{19.61}{4} = 4.90\ \mathrm{m\,s^{-2}}\). [A1]
Q: [9 marks] (#math.m.kinematics) ★★★ A car of mass 900 kg tows a trailer of mass 300 kg along a straight horizontal road, by a light rigid tow-bar. The driving force on the car is 3000 N. The resistances to motion are 400 N on the car and 200 N on the trailer. (a) Find the acceleration of the car and the tension in the tow-bar. (b) When the speed is \(20\ \mathrm{m\,s^{-1}}\) the tow-bar breaks. The resistance on the trailer is still 200 N. Find the distance the trailer travels before it stops.
H: Treat the car and trailer as one body for the acceleration, then look at the trailer alone for the tension.
H: After the bar breaks, the only horizontal force on the trailer is its resistance. Find the deceleration it causes.
H: Use \(v^2 = u^2 + 2as\) with \(v = 0\), \(u = 20\) and the deceleration you found.
A: (a) Whole system: \(3000 - 400 - 200 = 1200a\), [M1 A1] so \(a = 2\ \mathrm{m\,s^{-2}}\). [A1] Trailer: \(T - 200 = 300 \times 2\), [M1] so \(T = 800\) N. [A1] (b) The trailer's deceleration is \(\dfrac{200}{300} = \dfrac23\ \mathrm{m\,s^{-2}}\). [M1 A1] Then \(0 = 400 - 2 \times \dfrac23 s\), [M1] so \(s = 300\) m. [A1] Check on the car: \(3000 - 400 - 800 = 1800 = 900 \times 2\). ✓
Q: [11 marks] (#math.m.kinematics) ★★★ Particles \(A\) of mass 4 kg and \(B\) of mass \(m\) kg, with \(m < 4\), are attached to the ends of a light inextensible string that passes over a smooth fixed pulley. Both particles hang freely with the string taut, and \(A\) is 1.6 m above a horizontal floor. The system is released from rest and \(A\) reaches the floor 0.8 s later. (a) Find the acceleration of the particles, the tension in the string and the value of \(m\). (b) \(B\) does not reach the pulley. Find the greatest height above its starting position reached by \(B\). Take \(g = 10\).
H: Use the distance and time for \(A\) to find the acceleration with a constant acceleration equation, before you use Newton's law.
H: Write \(F = ma\) for \(A\) to find the tension, then for \(B\) to find \(m\).
H: When \(A\) hits the floor the string goes slack. What is \(B\)'s acceleration after that, and what is its speed at that moment?
A: (a) \(1.6 = \tfrac12 a(0.8)^2\), [M1] so \(a = 5\ \mathrm{m\,s^{-2}}\). [A1] For \(A\): \(40 - T = 4 \times 5\), [M1 A1] so \(T = 20\) N. For \(B\): \(T - 10m = 5m\), [M1 A1] so \(20 = 15m\) and \(m = \tfrac43 = 1.33\). [A1] (b) When \(A\) lands, the speed is \(5 \times 0.8 = 4\ \mathrm{m\,s^{-1}}\). [B1] The string goes slack and \(B\) moves freely upwards with deceleration 10, so it rises a further \(\dfrac{4^2}{2 \times 10} = 0.8\) m. [M1 A1] The greatest height is \(1.6 + 0.8 = 2.4\) m. [A1] Check: \(a = \dfrac{(4 - \frac43) \times 10}{4 + \frac43} = \dfrac{80/3}{16/3} = 5\). ✓
:::

:::try Stretch for A*
Q: [10 marks] ★★★ A block is projected with speed \(8\ \mathrm{m\,s^{-1}}\) up a line of greatest slope of a rough plane. The plane is inclined at angle \(\theta\) to the horizontal, where \(\sin\theta = 0.6\) and \(\cos\theta = 0.8\). The coefficient of friction is 0.5. (a) Show that the deceleration of the block while it moves up the plane is \(10\ \mathrm{m\,s^{-2}}\). (b) Find the greatest distance the block travels up the plane. (c) Show that the block slides back down, and find its speed when it returns to its starting point. Take \(g = 10\).
H: Call the mass \(m\): it cancels. Friction acts against the motion, so it acts down the plane while the block moves up, and up the plane while it slides down.
H: For (c), compare \(mg\sin\theta\) with the greatest friction \(\mu mg\cos\theta\) when the block is momentarily at rest at the top.
A: (a) \(R = 0.8mg = 8m\) and \(F = 0.5R = 4m\). [B1] Up the plane, both friction and the weight component act down the plane: \(-(6m + 4m) = ma\), [M1] so \(a = -10\): the deceleration is \(10\ \mathrm{m\,s^{-2}}\). [A1] (b) \(0 = 8^2 - 2 \times 10 \times s\), [M1] so \(s = 3.2\) m. [A1] (c) At the top the weight component \(6m\) is greater than the greatest friction \(4m\), so the block slides back. [B1] Down the plane, friction acts up the plane: \(6m - 4m = ma\), so \(a = 2\ \mathrm{m\,s^{-2}}\). [M1 A1] \(v^2 = 2 \times 2 \times 3.2 = 12.8\), [M1] so \(v = 3.58\ \mathrm{m\,s^{-1}}\). [A1] Check: it returns slower than the \(8\ \mathrm{m\,s^{-1}}\) it left with, as friction removed energy.
Q: [6 marks] ★★★ A particle \(P\) of mass 3 kg is on a rough plane inclined at \(30^\circ\) to the horizontal, with coefficient of friction 0.5. \(P\) is joined by a light inextensible string, passing over a smooth pulley at the top of the plane, to a particle \(Q\) of mass \(m\) kg which hangs freely. The system is at rest. Find the set of values of \(m\) for which \(P\) stays at rest. Take \(g = 10\).
H: Friction can act either way. Find the two limiting cases: \(P\) about to slide down, then \(P\) about to slide up.
H: At rest, the tension equals the weight of \(Q\), \(T = 10m\).
A: \(R = 30\cos 30^\circ = 25.98\) N, so the greatest friction is \(0.5 \times 25.98 = 12.99\) N. [B1] The weight component down the plane is \(30\sin 30^\circ = 15\) N. About to slide down (friction acts up the plane): \(T + 12.99 = 15\), [M1 A1] so \(10m = 2.01\) and \(m = 0.201\). [A1] About to slide up (friction acts down the plane): \(T = 15 + 12.99\), [M1] so \(10m = 27.99\) and \(m = 2.80\). [A1] \(P\) stays at rest for \(0.201 \le m \le 2.80\).
:::

:::quiz Check your understanding
? A 5 kg mass has an upward acceleration of \(2\ \mathrm{m\,s^{-2}}\) on a light cable. What is the tension? Take \(g = 10\).
- 40 N
- 50 N
+ 60 N
- 10 N
> \(T - 50 = 5 \times 2\), so \(T = 60\) N. The tension is larger than the weight because the mass is accelerating upwards.
? A particle slides down a smooth slope at \(30^\circ\). Its acceleration is:
- \(g\cos 30^\circ\)
+ \(g\sin 30^\circ\)
- \(g\)
- 0
> The only force along the slope is \(mg\sin\theta\), so \(a = g\sin\theta = 5\ \mathrm{m\,s^{-2}}\).
? Particles of 2 kg and 3 kg hang over a smooth pulley. The tension is:
- 20 N
- 30 N
+ between 20 N and 30 N
- 50 N
> The 3 kg mass accelerates down, so \(T < 30\). The 2 kg mass accelerates up, so \(T > 20\). Here \(T = 24\) N.
? A block on a rough slope is moving up. Compared with sliding down, its acceleration down the slope is:
- smaller
+ larger
- the same
- zero
> Moving up, friction and the weight component both act down the slope, so the deceleration is larger.
? A hanging particle lands and the string goes slack. The tension then is:
- the weight of the hanging particle
- unchanged
+ zero
- double
> A slack string cannot pull. The other particle then moves under its own forces only.
:::

:::checklist What you can now do
- [ ] I can write \(F = ma\) using the resultant force in the direction of the acceleration, with the right sign for each force.
- [ ] I can find the reaction on a person or object in a lift that is accelerating up or down.
- [ ] I can solve motion on a smooth or rough slope, and see why the acceleration is different up and down.
- [ ] I can write a separate equation of motion for each particle in a pulley system and solve for the acceleration and the tension.
- [ ] I can handle a car towing a trailer, with driving force, resistances, and a tow-bar in tension or thrust.
- [ ] I can tell when a string goes slack and start a second stage of motion.
- [ ] I can combine Newton's second law with the constant acceleration equations in one problem.
:::

:::recap
- \(F = ma\): resultant force (N) = mass (kg) × acceleration. Weight \(= mg\). Draw a force diagram for each object.
- Lifts: \(R - mg = ma\) going up, \(mg - R = ma\) accelerating down.
- Slopes: along the slope \(mg\sin\theta\); into the slope \(mg\cos\theta\) so \(R = mg\cos\theta\); friction \(F = \mu R\) opposes motion, so the acceleration differs up and down.
- Connected particles: same tension (light string, smooth pulley) and same acceleration (inextensible); write \(F = ma\) for each and solve.
- When a hanging particle lands, the string goes slack: start a second stage for the other particle.
- Car and trailer: whole system \(F - \text{resistances} = (m_1 + m_2)a\); trailer alone gives the tow-bar force; a rigid bar can be in thrust.
:::

:::links
- watch: [Connected particles on inclined planes](https://www.examsolutions.net/tutorials/connected-particles-on-inclined-planes/) · ExamSolutions · string over a pulley on a slope
- watch: [Exam questions: tow-bars](https://www.examsolutions.net/tutorials/exam-questions-tow-bars/) · ExamSolutions · car and trailer, tension and thrust
- practise: [CAIE Mechanics Newton's second law exam questions](https://www.savemyexams.com/a-level/maths/cie/20/mechanics/topic-questions/forces-and-equilibrium/newtons-second-law/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [The Ramp](https://phet.colorado.edu/en/simulations/the-ramp) · PhET · forces on a slope, with friction
- explore: [Forces and Motion: Basics](https://phet.colorado.edu/en/simulations/forces-and-motion-basics) · PhET · net force and acceleration
- papers: [9709 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-4) · Physics & Maths Tutor · papers with mark schemes [unofficial]

Links checked 3 October 2026.
:::
Next: [Momentum](#math.m.momentum).
