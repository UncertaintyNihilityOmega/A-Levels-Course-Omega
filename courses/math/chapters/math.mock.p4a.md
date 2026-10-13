@chapter math.mock.p4a
@title Mock paper: Mechanics (A)
@level mock
@paper CAIE 9709 Paper 4 · Edexcel IAL M1 · UK Mechanics Year 1
@time 1 h 15 min
@summary A complete original mock for Paper 4 (Mechanics): 9 questions, 50 marks, 1 hour 15 minutes, rising in difficulty, with a full mark scheme. Sit it in one go, then mark yourself and see which chapters to revise.

:::why
Paper 4 is where mechanics marks are won or lost on one habit: drawing the diagram and writing the equation of motion for each particle before you touch a number. This mock gives you 50 marks to practise that habit against the clock, at 1.5 minutes per mark.
:::

:::exam Instructions
- Answer **all** questions. The total is **50 marks** and you have **1 hour 15 minutes**.
- You may use a scientific calculator and the MF19 formula booklet. Graphical calculators and calculators with symbolic algebra, differentiation or integration are **not** allowed.
- Where a numerical value of \(g\) is needed, take \(g = 10\ \mathrm{m\,s^{-2}}\).
- Show every step. A correct answer with no working may score no marks.
- Give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**, unless the question says otherwise.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [3 marks] (#math.m.forces) A block of mass 4 kg is pulled along rough horizontal ground by a light rope. The rope is inclined at \(30^\circ\) above the horizontal and the tension in it is 25 N. The block moves with constant speed. Find the coefficient of friction between the block and the ground.
A: Resolve vertically: \(R + 25\sin 30^\circ = 40\), so \(R = 27.5\) N. [M1]
Resolve horizontally (constant speed, so no resultant force): \(F = 25\cos 30^\circ = 21.65\) N. [M1]
Friction is limiting, so
\[ \mu = \frac{F}{R} = \frac{21.65}{27.5} = 0.787 \]
[A1]
:::

:::try
Q: [4 marks] (#math.m.forces) A particle of weight 40 N rests in equilibrium on a smooth plane inclined at \(30^\circ\) to the horizontal. It is held by a horizontal force of magnitude \(H\) N, acting in the vertical plane that contains a line of greatest slope. Find \(H\) and the normal reaction \(R\) of the plane on the particle.
A: Resolve parallel to the plane (up the slope positive): \(H\cos 30^\circ - 40\sin 30^\circ = 0\). [M1]
\[ H = 40\tan 30^\circ = 23.1 \]
[A1] Resolve perpendicular to the plane: \(R = 40\cos 30^\circ + H\sin 30^\circ\). [M1]
\[ R = 34.64 + 11.55 = 46.2 \]
[A1]
:::

:::try
Q: [4 marks] (#math.m.energy) A car of mass 1200 kg travels at a constant speed of 25 m s⁻¹ up a straight road inclined at an angle \(\alpha\) to the horizontal, where \(\sin\alpha = 0.05\). The resistance to motion is 600 N.

(a) Find the power developed by the engine. [2]

The car now travels on a horizontal road against the same resistance of 600 N, with the engine working at the power found in part (a).

(b) Find the acceleration of the car when its speed is 20 m s⁻¹. [2]
A: (a) Constant speed, so the driving force balances resistance plus the weight component: \(D = 600 + 1200 \times 10 \times 0.05 = 1200\) N. [M1]
\[ P = Dv = 1200 \times 25 = 30\,000\ \text{W} = 30\ \text{kW} \]
[A1]

(b) At 20 m s⁻¹ the driving force is \(D = \dfrac{30\,000}{20} = 1500\) N. Newton's second law: \(1500 - 600 = 1200a\). [M1]
\(a = 0.75\ \mathrm{m\,s^{-2}}\). [A1]
:::

:::try
Q: [5 marks] (#math.m.momentum) Particle \(A\), of mass 3 kg, and particle \(B\), of mass 5 kg, move towards each other along a straight line on a smooth horizontal surface. \(A\) has speed 4 m s⁻¹ and \(B\) has speed 2 m s⁻¹. The particles collide directly. After the collision \(A\) moves in the opposite direction to its original motion, with speed 1.5 m s⁻¹.

(a) Find the speed of \(B\) after the collision and state its direction of motion. [3]

In a different collision the same two particles, moving as before, coalesce.

(b) Find the speed of the combined particle. [2]
A: (a) Take the original direction of \(A\)'s motion as positive. Conservation of momentum: [M1]
\[ 3(4) + 5(-2) = 3(-1.5) + 5v \]
[A1] \(2 = -4.5 + 5v\), so \(v = 1.3\). [A1] \(B\) moves at 1.3 m s⁻¹ in the original direction of motion of \(A\).

(b) Coalescing: \(12 - 10 = (3 + 5)w\). [M1] So \(w = 0.25\) m s⁻¹ in the original direction of \(A\). [A1]
:::

:::try
Q: [5 marks] (#math.m.kinematics) A particle moves in a straight line. Its velocity \(v\ \mathrm{m\,s^{-1}}\) at time \(t\) seconds is given by \(v = 12t - 3t^2\) for \(0 \le t \le 6\).

(a) Find the value of \(t\) at which the particle is instantaneously at rest, for \(t > 0\). [2]

(b) Find the total distance travelled by the particle in the first 6 seconds. [3]
A: (a) Put \(v = 0\): \(3t(4 - t) = 0\). [M1] So \(t = 4\) (rejecting \(t = 0\)). [A1]

(b) Integrate for the displacement from the start: \(s = 6t^2 - t^3\). [M1]
At \(t = 4\): \(s = 96 - 64 = 32\) m. [A1]
At \(t = 6\): \(s = 216 - 216 = 0\), so the particle has returned to its starting point and the velocity changed sign at \(t = 4\). The total distance is \(32 + 32 = 64\) m. [A1]
:::

:::try
Q: [6 marks] (#math.m.kinematics) A train starts from rest at station \(A\) and accelerates uniformly at 0.5 m s⁻² until it reaches a speed of \(V\) m s⁻¹. It then travels at this constant speed, and finally decelerates uniformly at 1 m s⁻² until it comes to rest at station \(B\). The total time for the journey is 100 s and the distance \(AB\) is 1400 m. Find the value of \(V\).
A: The time to reach speed \(V\) is \(t_1 = \dfrac{V}{0.5} = 2V\) and the time to stop is \(t_3 = \dfrac{V}{1} = V\). [B1]
So the time at constant speed is \(t_2 = 100 - 3V\). The distance is the area of the trapezium under the \(v\)–\(t\) graph: [M1]
\[ \tfrac12 V(2V) + V(100 - 3V) + \tfrac12 V(V) = 1400 \]
\[ V^2 + 100V - 3V^2 + 0.5V^2 = 1400 \quad\Rightarrow\quad 1.5V^2 - 100V + 1400 = 0 \]
[A1] Multiply by 2: \(3V^2 - 200V + 2800 = 0\), so \((3V - 140)(V - 20) = 0\). [M1]
\(V = 20\) or \(V = \dfrac{140}{3} = 46.7\). [A1]
If \(V = 46.7\) then \(t_2 = 100 - 140 < 0\), which is impossible, so \(V = 20\). [B1]
:::

:::try
Q: [4 marks] (#math.m.energy) A block of mass 2 kg is released from rest at a point 5 m above a horizontal floor, at the top of a smooth curved slide. It slides down to the bottom of the slide and then moves along the rough horizontal floor, where the coefficient of friction is 0.4, until it comes to rest.

(a) Find the speed of the block at the bottom of the slide. [2]

(b) Find the distance the block travels along the floor before it comes to rest. [2]
A: (a) The slide is smooth, so energy is conserved: \(\tfrac12(2)v^2 = 2 \times 10 \times 5\). [M1]
\(v^2 = 100\), so \(v = 10\ \mathrm{m\,s^{-1}}\). [A1]

(b) The normal reaction is \(R = 20\) N, so the friction force is \(0.4 \times 20 = 8\) N. All the kinetic energy (100 J) is lost to friction: \(8d = 100\). [M1]
\(d = 12.5\) m. [A1]
:::

:::try
Q: [8 marks] (#math.m.newton) A block of mass 5 kg lies on a rough plane inclined at an angle \(\alpha\) to the horizontal, where \(\sin\alpha = 0.6\) and \(\cos\alpha = 0.8\). The coefficient of friction between the block and the plane is 0.25. Take \(g = 10\).

(a) Show that the block will slide down the plane if it is released from rest. [3]

A force of magnitude \(P\) N, parallel to a line of greatest slope and directed up the plane, now acts on the block. The block moves up the plane with acceleration 0.8 m s⁻².

(b) Find the value of \(P\). [3]

When the block is moving up the plane at 4 m s⁻¹, the force \(P\) is removed.

(c) Find the distance the block moves up the plane after the force is removed. [2]
A: (a) Perpendicular to the plane: \(R = 5 \times 10 \times 0.8 = 40\) N. [B1]
The maximum friction is \(0.25 \times 40 = 10\) N, but the weight component down the slope is \(5 \times 10 \times 0.6 = 30\) N. [M1]
Since \(30 > 10\), friction cannot hold the block, so it slides down. [A1]

(b) The block moves up, so friction (10 N) acts down the plane. Newton's second law up the plane: [M1]
\[ P - 30 - 10 = 5 \times 0.8 \]
[A1] So \(P = 44\). [A1]

(c) With \(P\) removed the block moves up with both the weight component and friction acting down the plane: \(30 + 10 = 5a\), so \(a = 8\) (deceleration). [M1]
\(0 = 4^2 - 2(8)s\), so \(s = 1\) m. [A1]
:::

:::try
Q: [11 marks] (#math.m.newton) A particle \(P\) of mass 3 kg lies on a smooth plane inclined at \(30^\circ\) to the horizontal. A particle \(Q\) of mass 2 kg hangs vertically. The particles are connected by a light inextensible string that passes over a smooth pulley at the top edge of the plane. The string is taut, \(P\) is on the slope and \(Q\) is 1.5 m above the horizontal ground. The system is released from rest and \(P\) moves up the plane.

(a) Find the acceleration of the system and the tension in the string. [4]

Particle \(Q\) hits the ground and does not rebound. \(P\) does not reach the pulley.

(b) Find the speed of \(P\) when \(Q\) hits the ground. [2]

(c) Find the greatest distance \(P\) travels up the plane from its starting position. [3]

(d) Find the time from the release of the system until \(P\) first comes to instantaneous rest. [2]
A: (a) For \(P\), up the plane: \(T - 3 \times 10 \times \sin 30^\circ = 3a\), so \(T - 15 = 3a\). [M1]
For \(Q\), downwards: \(2 \times 10 - T = 2a\), so \(20 - T = 2a\). [M1]
Adding the equations: \(5 = 5a\), so \(a = 1\ \mathrm{m\,s^{-2}}\). [A1]
Then \(T = 15 + 3 = 18\) N. [A1]

(b) \(Q\) falls 1.5 m from rest: \(v^2 = 0 + 2(1)(1.5) = 3\). [M1]
\(v = \sqrt3 = 1.73\ \mathrm{m\,s^{-1}}\). [A1]

(c) Once \(Q\) lands the string goes slack, and \(P\) decelerates under the weight component alone: \(3a' = 3 \times 10 \times \sin 30^\circ\), so \(a' = 5\) (deceleration). [M1]
\(0 = 3 - 2(5)s\), so \(s = 0.3\) m after \(Q\) lands. [A1]
The greatest distance from the start is \(1.5 + 0.3 = 1.8\) m. [A1]

(d) \(Q\) falls for \(t_1\): \(1.5 = \tfrac12(1)t_1^2\), so \(t_1 = \sqrt3 = 1.732\) s. [M1]
Then \(P\) slows: \(0 = \sqrt3 - 5t_2\), so \(t_2 = 0.3464\) s, and the total time is \(1.732 + 0.346 = 2.08\) s. [A1]
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 3 | Rough horizontal ground, rope at an angle | [Forces and equilibrium](#math.m.forces) |
| 2 | 4 | Equilibrium on a smooth plane | [Forces and equilibrium](#math.m.forces) |
| 3 | 4 | Power, driving force on a hill | [Work, energy and power](#math.m.energy) |
| 4 | 5 | Collision and coalescence | [Momentum and collisions](#math.m.momentum) |
| 5 | 5 | Velocity as a function of time | [Kinematics: describing motion](#math.m.kinematics) |
| 6 | 6 | Train journey, \(v\)–\(t\) graph | [Kinematics: describing motion](#math.m.kinematics) |
| 7 | 4 | Smooth slide and rough floor | [Work, energy and power](#math.m.energy) |
| 8 | 8 | Rough inclined plane | [Newton's laws and connected particles](#math.m.newton) |
| 9 | 11 | Connected particles, plane and pulley | [Newton's laws and connected particles](#math.m.newton) |
