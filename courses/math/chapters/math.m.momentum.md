@chapter math.m.momentum
@title Momentum and collisions
@level as
@paper CAIE P4 · Edexcel IAL M1 · UK Mechanics
@time 4–6 hours
@summary Momentum is mass times velocity, and in a collision between two objects the total momentum does not change. You will learn the definition, how to use conservation of momentum for particles that bounce apart or join together, how to handle directions and unknown masses, and how to link momentum to kinetic energy lost.

:::why
When a lorry hits a car, or a billiard ball hits another, you could never follow the forces during the collision: they are huge and last a tiny fraction of a second. Conservation of momentum lets you skip the collision altogether and compare the motion just before with the motion just after. It explains rocket propulsion and recoil as well as crashes, and it is one of the shortest topics in Paper 4.
:::

**Before you start**, you need velocity and direction signs from [Kinematics](#math.m.kinematics) and Newton's third law from [Forces and equilibrium](#math.m.forces).

## Momentum

:::def Momentum
The momentum of a particle of mass \(m\) moving with velocity \(v\) is \(mv\). It is a **vector**: it has the direction of the velocity. The unit is \(\mathrm{kg\,m\,s^{-1}}\) (also written N s).
:::

A heavy lorry moving slowly and a light bullet moving fast can have similar momentum. In a straight line, choose a positive direction: momentum in the other direction is negative.

:::eg Find the momentum of (a) a 1200 kg car moving at \(15\ \mathrm{m\,s^{-1}}\) east, (b) a 0.02 kg bullet moving at \(400\ \mathrm{m\,s^{-1}}\) west. Take east as positive.
(a) \(1200 \times 15 = 18\,000\ \mathrm{kg\,m\,s^{-1}}\).
(b) \(0.02 \times (-400) = -8\ \mathrm{kg\,m\,s^{-1}}\), that is 8 in the westward direction.
The car has far more momentum, even though the bullet is much faster.
:::

## Conservation of momentum

When two particles collide, they exert forces on each other. By Newton's third law the forces are equal and opposite and last for exactly the same time, so each particle gains the momentum the other loses. The total does not change. This holds as long as no **external** force (such as friction from the ground) disturbs the motion during the collision.

:::key Conservation of linear momentum
In a direct collision (along a straight line) of two particles \(A\) and \(B\), with velocities measured in the same positive direction:
\[m_A u_A + m_B u_B = m_A v_A + m_B v_B\]
total momentum before = total momentum after, where \(u\) is the velocity before and \(v\) the velocity after.
- Momentum is a vector, so **signs matter**. A particle moving in the negative direction has a negative \(u\) or \(v\).
- If the particles **coalesce** (stick together), they move with a common velocity \(V\) afterwards and the mass of the combined body is \(m_A + m_B\): \(m_Au_A + m_Bu_B = (m_A + m_B)V\).
- Kinetic energy is generally **not** conserved in a collision, so do not use it as an equation here.
:::

:::steps
1. Draw a **before** and an **after** diagram. Label the masses and velocities, with arrows for the directions.
2. Choose a positive direction (usually the direction of motion of the first particle) and mark it.
3. Write the momentum equation, using signs for the velocities.
4. Solve for the unknown. If the result is negative, the velocity is in the negative direction.
:::

:::html
<figure class="fig"><svg viewBox="0 0 520 170" role="img" aria-label="Before: a 2 kg particle moves right at 6 metres per second towards a stationary 3 kg particle. After: they stick together as a 5 kg body moving right at 2.4 metres per second."><text class="tb" x="14" y="26">Before</text><rect class="f1 s-acc sw2" x="70" y="40" width="46" height="34"/><text class="tl" x="93" y="62" text-anchor="middle">2 kg</text><path class="c2" d="M122 57H180" marker-end="url(#ah)"/><text class="tl" x="151" y="48" text-anchor="middle">6</text><rect class="f2 s-acc sw2" x="260" y="40" width="58" height="34"/><text class="tl" x="289" y="62" text-anchor="middle">3 kg</text><text class="tl" x="289" y="90" text-anchor="middle">at rest</text><text class="tb" x="14" y="126">After</text><rect class="f1 s-acc sw2" x="200" y="140" width="46" height="26"/><rect class="f2 s-acc sw2" x="246" y="140" width="58" height="26"/><text class="tl" x="252" y="158" text-anchor="middle">5 kg</text><path class="c2" d="M312 153H390" marker-end="url(#ah)"/><text class="tl" x="351" y="144" text-anchor="middle">2.4</text></svg><figcaption>A 2 kg particle at \(6\ \mathrm{m\,s^{-1}}\) hits a stationary 3 kg particle and they coalesce. Velocities are in \(\mathrm{m\,s^{-1}}\).</figcaption></figure>
:::

:::eg A 2 kg particle moving at \(6\ \mathrm{m\,s^{-1}}\) collides with a stationary 3 kg particle on a smooth surface and they coalesce. Find the speed afterwards.
Take the direction of motion as positive.
\[2 \times 6 + 3 \times 0 = (2 + 3)V \quad\Rightarrow\quad 12 = 5V \quad\Rightarrow\quad V = 2.4\ \mathrm{m\,s^{-1}}\]
:::

:::eg A 3 kg ball moving at \(4\ \mathrm{m\,s^{-1}}\) hits a stationary 5 kg ball. The 3 kg ball rebounds at \(1\ \mathrm{m\,s^{-1}}\). Find the speed of the 5 kg ball afterwards.
Take the original direction as positive. The 3 kg ball now has velocity \(-1\):
\[3 \times 4 + 5 \times 0 = 3 \times (-1) + 5v \quad\Rightarrow\quad 12 = -3 + 5v \quad\Rightarrow\quad v = 3\ \mathrm{m\,s^{-1}}\]
Both balls end up moving apart, with the 5 kg ball going in the original direction.
:::

### Particles moving in opposite directions

:::eg A 4 kg particle moves east at \(5\ \mathrm{m\,s^{-1}}\) and a 2 kg particle moves west at \(8\ \mathrm{m\,s^{-1}}\). They collide head on. Find the common velocity if they coalesce. If instead the 4 kg particle continues east at \(1\ \mathrm{m\,s^{-1}}\), find the velocity of the 2 kg particle.
Take east as positive. Before: momentum \(= 4 \times 5 + 2 \times (-8) = 20 - 16 = 4\).

Coalescing: \(4 = 6V\), so \(V = \tfrac23 = 0.667\ \mathrm{m\,s^{-1}}\) east.

Second case: \(4 = 4 \times 1 + 2v\), so \(v = 0\). The 2 kg particle is brought to rest.
:::

### Separating and recoil

Momentum also works in reverse: two bodies at rest together have zero total momentum, so if they push apart (a gun firing a bullet), they move off with **equal and opposite** momentum.

:::eg A gun of mass 4 kg fires a bullet of mass 0.02 kg at \(400\ \mathrm{m\,s^{-1}}\). Find the recoil velocity of the gun. Take the bullet's direction as positive.
Initially everything is at rest, so the total momentum is 0.
\[0 = 0.02 \times 400 + 4V \quad\Rightarrow\quad 4V = -8 \quad\Rightarrow\quad V = -2\]
The gun recoils at \(2\ \mathrm{m\,s^{-1}}\) in the opposite direction to the bullet.
:::

### Unknown masses and speeds

:::eg Particle \(P\) of mass 2 kg moving at \(6\ \mathrm{m\,s^{-1}}\) collides with a stationary particle \(Q\) of mass \(m\) kg. After the collision \(P\) moves at \(1\ \mathrm{m\,s^{-1}}\) and \(Q\) at \(4\ \mathrm{m\,s^{-1}}\), in the same direction. Find \(m\).
\[2 \times 6 + 0 = 2 \times 1 + 4m \quad\Rightarrow\quad 12 = 2 + 4m \quad\Rightarrow\quad m = 2.5\]
:::

### Momentum and kinetic energy

Momentum is conserved in every collision, but energy is not: some turns into sound and heat. If you know the kinetic energy \(\tfrac12 mv^2\) (see [Work, energy and power](#math.m.energy)), the loss in a collision is the kinetic energy before minus after.

:::eg A railway truck of mass 12 000 kg moves at \(3\ \mathrm{m\,s^{-1}}\) and collides with a stationary truck of mass 8000 kg. They couple together. Find their speed and the kinetic energy lost.
\[12\,000 \times 3 = 20\,000V \quad\Rightarrow\quad V = 1.8\ \mathrm{m\,s^{-1}}\]
Kinetic energy before: \(\tfrac12 \times 12\,000 \times 3^2 = 54\,000\) J. After: \(\tfrac12 \times 20\,000 \times 1.8^2 = 32\,400\) J. The loss is \(54\,000 - 32\,400 = 21\,600\) J.
:::

:::warn Common slips
- Ignoring signs: a particle moving towards the other has a **negative** velocity if the positive direction is the other way.
- Writing \(m_Au_A - m_Bu_B\) in one place and a different sign convention elsewhere. Use plain signs in the equation, and put the negative sign inside the velocity.
- For coalescing, using \(m_A + m_B\) on the left side too. The left side has the separate masses, the right side the combined mass.
- Assuming kinetic energy is conserved to get a second equation. Only momentum is conserved (energy loss is not given unless the question tells you).
- Forgetting that a negative final velocity means motion in the opposite direction to your positive direction.
:::

## Exam-style questions

:::eg (Exam style) Particles \(A\) of mass 3 kg and \(B\) of mass \(m\) kg move towards each other along a straight line on a smooth horizontal surface, \(A\) at \(5\ \mathrm{m\,s^{-1}}\) and \(B\) at \(2\ \mathrm{m\,s^{-1}}\). After the collision \(A\) moves in the opposite direction to its original motion at \(1\ \mathrm{m\,s^{-1}}\), and \(B\) moves in the opposite direction to its original motion at \(3\ \mathrm{m\,s^{-1}}\). (a) Find \(m\). (b) \(A\) then collides with a stationary particle \(C\) of mass 2 kg and they coalesce. Find the speed of the combined particle. [7 marks]
(a) Take \(A\)'s original direction as positive. Before: \(A\) has velocity \(+5\), \(B\) has \(-2\). After: \(A\) has \(-1\), \(B\) has \(+3\). [B1]
\[3 \times 5 + m \times (-2) = 3 \times (-1) + m \times 3\] [M1 A1]
\[15 - 2m = -3 + 3m \quad\Rightarrow\quad 18 = 5m \quad\Rightarrow\quad m = 3.6\] [A1]

(b) \(A\) is moving at \(1\ \mathrm{m\,s^{-1}}\) in the negative direction, and \(C\) is at rest:
\[3 \times (-1) + 0 = (3 + 2)V \quad\Rightarrow\quad V = -0.6\] [M1 A1]
The speed of the combined particle is \(0.6\ \mathrm{m\,s^{-1}}\). [A1]
:::

:::eg (Exam style) A trolley of mass 5 kg moves at \(4\ \mathrm{m\,s^{-1}}\) along a smooth horizontal track. A sandbag of mass 3 kg is dropped vertically onto it and stays there. Find the new speed of the trolley, and explain why only the horizontal momentum is considered. [4 marks]
Horizontal momentum is conserved: the sandbag has no horizontal velocity, and nothing pushes the system horizontally. [B1]
\[5 \times 4 + 3 \times 0 = (5 + 3)V\] [M1] \(V = \dfrac{20}{8} = 2.5\ \mathrm{m\,s^{-1}}\). [A1]
The track exerts a vertical force when the sandbag lands, so vertical momentum is not conserved, but it has no effect on the horizontal motion. [B1]
:::

:::exam Technique
- Always draw before and after diagrams, with directions and a positive direction arrow.
- Put the momentum equation in words, "momentum before = momentum after", so a slip in signs can still earn the method mark.
- The phrase "smooth" means no friction: horizontal momentum is conserved in a horizontal collision.
- Cambridge Paper 4 covers direct impacts only. You will not need impulse or the coefficient of restitution.
:::

:::board
- **CAIE 9709 P4**: momentum is conserved in direct impact of two bodies, including coalescing. Impulse and the coefficient of restitution are not in the syllabus.
- **Edexcel IAL and UK A Level boards**: also examine **impulse**, the change in momentum, \(Ft = mv - mu\).
- The conservation equation is the same in every board.
:::

:::try Start easy, finish at exam standard
Q: Find the momentum of a 0.5 kg ball moving at \(12\ \mathrm{m\,s^{-1}}\) to the left. Take right as positive.
A: \(0.5 \times (-12) = -6\ \mathrm{kg\,m\,s^{-1}}\), that is 6 kg m s⁻¹ to the left.
Q: A 1.5 kg particle moving at \(4\ \mathrm{m\,s^{-1}}\) hits a stationary 2.5 kg particle and they coalesce. Find the speed afterwards.
A: \(1.5 \times 4 = 4V\), so \(V = 1.5\ \mathrm{m\,s^{-1}}\).
Q: A 2 kg particle at \(7\ \mathrm{m\,s^{-1}}\) hits a stationary 3 kg particle. The 2 kg particle stops dead. Find the velocity of the 3 kg particle.
A: \(14 = 0 + 3v\), so \(v = 4.67\ \mathrm{m\,s^{-1}}\) in the original direction.
Q: A 5 kg particle at \(3\ \mathrm{m\,s^{-1}}\) and a 3 kg particle at \(5\ \mathrm{m\,s^{-1}}\) move towards each other and coalesce. Find their velocity afterwards.
A: Taking the direction of the 5 kg particle as positive: \(15 - 15 = 8V\), so \(V = 0\). They stop.
Q: Two particles of mass 2 kg and 4 kg are moving in the same direction at \(9\ \mathrm{m\,s^{-1}}\) and \(3\ \mathrm{m\,s^{-1}}\), the lighter one behind. They collide and coalesce. Find the speed afterwards and the kinetic energy lost.
A: \(18 + 12 = 6V\), so \(V = 5\ \mathrm{m\,s^{-1}}\). KE before \(= \tfrac12 \times 2 \times 81 + \tfrac12 \times 4 \times 9 = 81 + 18 = 99\) J. After: \(\tfrac12 \times 6 \times 25 = 75\) J. Loss \(= 24\) J.
Q: A boy of mass 40 kg stands on a stationary trolley of mass 8 kg on smooth ground and jumps off horizontally at \(1.2\ \mathrm{m\,s^{-1}}\) relative to the ground. Find the velocity of the trolley.
A: \(0 = 40 \times 1.2 + 8V\), so \(V = -6\ \mathrm{m\,s^{-1}}\): the trolley moves at \(6\ \mathrm{m\,s^{-1}}\) in the opposite direction.
Q: Particle \(A\) of mass 0.4 kg moving at \(5\ \mathrm{m\,s^{-1}}\) collides with particle \(B\) of mass 0.6 kg moving in the opposite direction at \(3\ \mathrm{m\,s^{-1}}\). After the collision \(A\) moves at \(2\ \mathrm{m\,s^{-1}}\) in its original direction. Find the velocity of \(B\).
A: Take \(A\)'s original direction as positive. \(0.4 \times 5 + 0.6 \times (-3) = 0.4 \times 2 + 0.6v\), so \(2 - 1.8 = 0.8 + 0.6v\), \(0.2 - 0.8 = 0.6v\), \(v = -1\). \(B\) moves at \(1\ \mathrm{m\,s^{-1}}\) in the opposite direction to \(A\)'s original motion.
Q: Why is kinetic energy not used to find the speeds after a collision in which two particles coalesce?
A: Kinetic energy is lost (to sound, heat and deformation) when particles coalesce, and the amount is not known in advance. Momentum is conserved, so it is the momentum equation that gives the speed.
Q: (Exam style) Particles \(P\) (mass 0.5 kg) and \(Q\) (mass 0.3 kg) are moving in the same direction on a smooth horizontal plane with speeds \(4\ \mathrm{m\,s^{-1}}\) and \(2\ \mathrm{m\,s^{-1}}\), \(P\) behind \(Q\). They collide and \(P\) then moves with speed \(1.5\ \mathrm{m\,s^{-1}}\) in the same direction. (a) Find the speed of \(Q\) after the collision. (b) If instead they coalesce, find their common speed. [6 marks]
A: (a) \(0.5 \times 4 + 0.3 \times 2 = 0.5 \times 1.5 + 0.3v\) [M1 A1], so \(2.6 = 0.75 + 0.3v\) and \(v = 6.17\ \mathrm{m\,s^{-1}}\). [A1] (b) \(2.6 = 0.8V\) [M1 A1], so \(V = 3.25\ \mathrm{m\,s^{-1}}\). [A1]
Q: (Exam style) Two particles \(A\) (mass 2 kg) and \(B\) (mass 3 kg) are at rest on a smooth horizontal surface with a compressed light spring between them. The spring is released and \(A\) moves off at \(6\ \mathrm{m\,s^{-1}}\). Find the speed of \(B\) and the total kinetic energy given to the particles. [5 marks]
A: Total momentum is 0: \(0 = 2 \times 6 + 3v\) [M1 A1], so \(v = -4\), so \(B\) moves at \(4\ \mathrm{m\,s^{-1}}\) in the opposite direction. [A1] KE \(= \tfrac12 \times 2 \times 36 + \tfrac12 \times 3 \times 16 = 36 + 24\) [M1] \(= 60\) J. [A1]
:::

:::quiz Check your understanding
? A 3 kg particle moves at \(4\ \mathrm{m\,s^{-1}}\). What is its momentum?
- 7 kg m s⁻¹
- 1.33 kg m s⁻¹
+ 12 kg m s⁻¹
- 6 kg m s⁻¹
> Momentum is mass times velocity: \(3 \times 4 = 12\). Adding gives 7, and dividing gives 1.33.
? A 2 kg particle at \(3\ \mathrm{m\,s^{-1}}\) hits a stationary 4 kg particle and they coalesce. The speed afterwards is:
- 3
- 1.5
+ 1
- 2
> \(2 \times 3 = 6V\) with total mass 6, so \(V = 1\ \mathrm{m\,s^{-1}}\). Using only 4 kg gives 1.5.
? A 1 kg particle at \(5\ \mathrm{m\,s^{-1}}\) and a 1 kg particle at \(5\ \mathrm{m\,s^{-1}}\) in the opposite direction collide and coalesce. The velocity afterwards is:
- \(10\ \mathrm{m\,s^{-1}}\)
- \(5\ \mathrm{m\,s^{-1}}\)
+ 0
- \(2.5\ \mathrm{m\,s^{-1}}\)
> The momenta are \(+5\) and \(-5\), which cancel, so the total is 0 and the combined particle is at rest.
? In a collision between two particles on a smooth surface, which quantity is always conserved?
- kinetic energy
- speed of each particle
+ total momentum
- velocity of each particle
> Momentum is conserved. Kinetic energy is generally lost, and each particle's velocity changes.
? A gun and bullet are initially at rest. The bullet is fired forwards. The gun:
- stays at rest
+ recoils backwards with momentum equal in size to the bullet's
- moves forwards
- recoils with the same speed as the bullet
> Total momentum stays zero, so the gun's momentum is equal and opposite. Its speed is much smaller because its mass is much larger.
:::

:::recap
- Momentum \(= mv\), a vector, in \(\mathrm{kg\,m\,s^{-1}}\). Choose a positive direction and use signs.
- Conservation: \(m_Au_A + m_Bu_B = m_Av_A + m_Bv_B\) (momentum before = after) when no external force acts.
- Coalescing: \(m_Au_A + m_Bu_B = (m_A + m_B)V\).
- Bodies pushed apart from rest have zero total momentum, so move with equal and opposite momentum.
- Kinetic energy is generally not conserved. Loss \(= \) KE before \(-\) KE after.
- No impulse or coefficient of restitution in the Cambridge syllabus.
:::

:::note Learn more online
- **Practise:** [CAIE Mechanics momentum exam questions](https://www.savemyexams.com/a-level/maths/cie/20/mechanics/topic-questions/momentum/momentum-and-collisions/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Collision Lab](https://phet.colorado.edu/en/simulations/collision-lab) · PhET · collide two balls and check that momentum is conserved
- **Read:** [Physics archive](https://www.khanacademy.org/science/physics) · Khan Academy · the impacts and linear momentum unit
- **Read:** [University Physics Volume 1 (free textbook)](https://openstax.org/details/books/university-physics-volume-1) · OpenStax · the linear momentum and collisions chapter
- **Papers:** [9709 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-4) · Physics & Maths Tutor · papers with mark schemes *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Work, energy and power](#math.m.energy).
