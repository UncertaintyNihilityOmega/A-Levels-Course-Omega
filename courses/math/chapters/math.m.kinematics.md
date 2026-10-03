@chapter math.m.kinematics
@title Kinematics: describing motion
@level as
@paper CAIE P4 · Edexcel IAL M1 and M2 · UK Mechanics
@time 7–9 hours
@summary Kinematics describes how an object moves, without asking what causes the motion. You will learn the difference between distance and displacement and between speed and velocity, how to read distance–time and velocity–time graphs, the constant acceleration equations, vertical motion under gravity, problems with two moving objects, and motion with variable acceleration using calculus.

:::why
Before you can explain why things move, you need a precise way to say how they move: where an object is, how fast it is going, and how quickly its speed is changing. The same few ideas describe a car braking, a ball thrown into the air and a train pulling out of a station. This chapter also puts your calculus to work: velocity is the derivative of position, and acceleration is the derivative of velocity.
:::

**Before you start**, you need rearranging formulae and solving quadratics from [Quadratics](#math.p1.quadratics), and differentiation and integration of powers of \(x\) from [Differentiation](#math.p1.diff) and [Integration](#math.p1.integ). Force diagrams and resolving are in [Forces and equilibrium](#math.m.forces).

## Distance, displacement, speed, velocity, acceleration

Mechanics treats an object as a **particle**: a point with mass but no size. This chapter is about motion in a straight line, so every vector quantity has a direction that is simply "positive" or "negative". Choose which direction is positive and keep to it.

:::def Scalar and vector quantities
A **scalar** has size only. A **vector** has size and direction. In straight-line motion a vector's direction is shown by its sign.
:::

| Quantity | Scalar or vector | Meaning | Unit |
|---|---|---|---|
| Distance | scalar | total length of path travelled | m |
| Displacement \(s\) | vector | position relative to the start, in a given direction | m |
| Speed | scalar | rate of change of distance, never negative | m s⁻¹ |
| Velocity \(v\) | vector | rate of change of displacement | m s⁻¹ |
| Acceleration \(a\) | vector | rate of change of velocity | m s⁻² |

**Deceleration** is a word for slowing down: the speed decreases. If the object moves in the positive direction and slows, its acceleration is negative. If it moves in the negative direction and slows, its acceleration is positive.

:::eg A walker goes 3 km east and then 4 km north, taking 1 hour in total. Find the distance, the displacement, the average speed and the size of the average velocity.
Distance \(= 3 + 4 = 7\) km. The displacement is the straight line from the start: \(\sqrt{3^2 + 4^2} = 5\) km.
Average speed \(= \dfrac{\text{distance}}{\text{time}} = 7\) km h⁻¹. The size of the average velocity is \(\dfrac{\text{displacement}}{\text{time}} = 5\) km h⁻¹.
The two differ because distance counts every step, while displacement counts only where you finish compared with where you started.
:::

## Graphs of motion

A **displacement–time** (\(s\)–\(t\)) graph shows position against time. Its **gradient** is the velocity. A horizontal line means the object is at rest.

A **velocity–time** (\(v\)–\(t\)) graph shows velocity against time.

:::key Reading a velocity–time graph
- The **gradient** is the acceleration.
- The **area under the graph** is the displacement. Area **above** the \(t\)-axis counts as positive and area **below** as negative.
- Distance travelled is the total of all the areas taken as positive.
- A horizontal line means constant velocity (zero acceleration). A straight sloping line means constant acceleration.
:::

For a shape made of straight lines, split the area into triangles, rectangles and trapeziums.

:::html
<figure class="fig"><svg viewBox="0 0 560 235" role="img" aria-label="Velocity–time graph: velocity rises uniformly from 0 at t = 0 to 20 metres per second at t = 8 seconds, stays at 20 until t = 38 seconds, then falls uniformly to 0 at t = 50 seconds."><path class="gr thin" d="M50 190H510M50 190V30"/><path class="fm" d="M50 190L122 50L392 50L500 190Z" opacity="0.25"/><path class="c1 thick" d="M50 190L122 50L392 50L500 190"/><path class="dash thin ln" d="M122 50V190M392 50V190M50 50H122"/><path class="ax" d="M50 190H520" marker-end="url(#ahm)"/><path class="ax" d="M50 190V25" marker-end="url(#ahm)"/><text class="ts" x="50" y="208" text-anchor="middle">0</text><text class="ts" x="122" y="208" text-anchor="middle">8</text><text class="ts" x="392" y="208" text-anchor="middle">38</text><text class="ts" x="500" y="208" text-anchor="middle">50</text><text class="ts" x="42" y="54" text-anchor="end">20</text><text class="tl" x="520" y="224" text-anchor="end">t (s)</text><text class="tl" x="58" y="22">v (m s⁻¹)</text><text class="tl" x="86" y="112" text-anchor="middle">A</text><text class="tl" x="257" y="130" text-anchor="middle">B</text><text class="tl" x="446" y="112" text-anchor="middle">C</text></svg><figcaption>The areas A, B and C are a triangle, a rectangle and a triangle.</figcaption></figure>
:::

:::eg A car accelerates uniformly from rest to \(20\ \mathrm{m\,s^{-1}}\) in 8 s, travels at constant speed for 30 s, then decelerates uniformly to rest in 12 s, as in the graph. Find the acceleration, the deceleration and the total distance.
Acceleration \(= \dfrac{20 - 0}{8} = 2.5\ \mathrm{m\,s^{-2}}\).
Deceleration \(= \dfrac{20}{12} = 1.67\ \mathrm{m\,s^{-2}}\) (the gradient is \(-\tfrac53\)).
Total distance is the area under the graph, in three parts:
\[A = \tfrac12 \times 8 \times 20 = 80 \qquad B = 30 \times 20 = 600 \qquad C = \tfrac12 \times 12 \times 20 = 120\]
\[\text{distance} = 80 + 600 + 120 = 800\ \text{m}\]
The total time is \(8 + 30 + 12 = 50\) s, so the average speed is \(\dfrac{800}{50} = 16\ \mathrm{m\,s^{-1}}\).
:::

## The constant acceleration equations

When the acceleration is **constant**, five quantities describe the motion: \(s\), \(u\), \(v\), \(a\) and \(t\).

- \(s\) is the displacement from the start,
- \(u\) is the initial velocity,
- \(v\) is the final velocity,
- \(a\) is the (constant) acceleration,
- \(t\) is the time.

:::key The constant acceleration equations
\[v = u + at\]
\[s = \tfrac12(u + v)t\]
\[s = ut + \tfrac12 at^2\]
\[v^2 = u^2 + 2as\]
- Use them only when \(a\) is **constant**, in a straight line.
- All four are on MF19, but you must know when to choose each one.
- Each equation leaves out one of the five quantities. Pick the one that has the three you know and the one you want.
:::

These come from the \(v\)–\(t\) graph of a straight line from \(u\) to \(v\): the gradient is \(a = \dfrac{v - u}{t}\), which gives the first equation, and the area of the trapezium is \(s = \tfrac12(u + v)t\).

:::steps
1. Draw a sketch, mark the positive direction and write down the values you know with their signs.
2. Write \(s, u, v, a, t\) as a list. Mark the one you want and the one that is missing from the problem.
3. Choose the equation that contains the quantities you have and the one you need, and does not contain the unknown you do not care about.
4. Solve, and check that the answer is reasonable and has a unit.
:::

:::eg A car is travelling at \(25\ \mathrm{m\,s^{-1}}\) and brakes with constant deceleration \(5\ \mathrm{m\,s^{-2}}\) until it stops. Find the stopping distance and the time taken.
Take the direction of motion as positive: \(u = 25\), \(v = 0\), \(a = -5\). The missing quantity is \(t\), so use \(v^2 = u^2 + 2as\):
\[0 = 625 - 10s \quad\Rightarrow\quad s = 62.5\ \text{m}\]
For the time use \(v = u + at\): \(0 = 25 - 5t\), so \(t = 5\) s.
:::

:::eg A train passes a signal at \(12\ \mathrm{m\,s^{-1}}\) and accelerates uniformly. After 540 m its speed is \(30\ \mathrm{m\,s^{-1}}\). Find the acceleration and the time taken.
\(u = 12\), \(v = 30\), \(s = 540\), and \(t\) is not wanted yet, so use \(v^2 = u^2 + 2as\):
\[900 = 144 + 1080a \quad\Rightarrow\quad a = \frac{756}{1080} = 0.7\ \mathrm{m\,s^{-2}}\]
Then \(v = u + at\) gives \(30 = 12 + 0.7t\), so \(t = \dfrac{18}{0.7} = 25.7\) s.
Check with \(s = \tfrac12(u + v)t = \tfrac12 \times 42 \times 25.71 = 540\). ✓
:::

:::warn Direction and sign slips
- Mixing directions: if up is positive, then a ball thrown up has \(u > 0\) but \(a = -10\) (gravity pulls down).
- Using a negative \(s\) as a distance. \(s\) is displacement and can be negative; distance cannot.
- "Decelerates at 5" means \(a = -5\) when the motion is in the positive direction. Do not use \(+5\).
- Using the equations when the acceleration changes. Split the motion into stages with constant acceleration instead.
:::

## Vertical motion under gravity

An object moving freely under gravity, with air resistance ignored, has constant acceleration \(g = 10\ \mathrm{m\,s^{-2}}\) downwards. Take \(g = 10\) in every question that does not say otherwise. Choose up as positive, so \(a = -10\) throughout, whether the object is moving up or down.

:::eg A ball is thrown vertically upwards at \(18\ \mathrm{m\,s^{-1}}\) from the ground. Find the greatest height, the time to reach it and the total time in the air. Take \(g = 10\).
Up is positive, \(u = 18\), \(a = -10\). At the highest point \(v = 0\).
\[0 = 18^2 - 20s \quad\Rightarrow\quad s = \frac{324}{20} = 16.2\ \text{m}\]
\[0 = 18 - 10t \quad\Rightarrow\quad t = 1.8\ \text{s}\]
The ball returns to the ground when \(s = 0\): \(0 = 18t - 5t^2 = t(18 - 5t)\), so \(t = 0\) or \(t = 3.6\) s. The total time is 3.6 s, twice the time to the top. It lands at the same speed, \(18\ \mathrm{m\,s^{-1}}\), that it left with.
:::

:::eg A stone is thrown vertically upwards at \(12\ \mathrm{m\,s^{-1}}\) from a point 32 m above the ground. Find the time taken to reach the ground, and the speed on landing. Take \(g = 10\).
Up is positive. The displacement on landing is \(s = -32\), with \(u = 12\) and \(a = -10\):
\[-32 = 12t - 5t^2 \quad\Rightarrow\quad 5t^2 - 12t - 32 = 0\]
\[(5t + 8)(t - 4) = 0 \quad\Rightarrow\quad t = 4\ \text{s} \quad(\text{the root } t = -1.6 \text{ is rejected})\]
\(v = u + at = 12 - 40 = -28\), so the speed on landing is \(28\ \mathrm{m\,s^{-1}}\) (the minus sign shows it is moving downwards).
:::

:::eg A ball is thrown upwards at \(25\ \mathrm{m\,s^{-1}}\) from the ground. For how long is it more than 20 m above the ground? Take \(g = 10\).
\(s = 25t - 5t^2 = 20\), so \(5t^2 - 25t + 20 = 0\), which is \(t^2 - 5t + 4 = 0\) and \((t - 1)(t - 4) = 0\). The ball is at 20 m when \(t = 1\) (going up) and \(t = 4\) (coming down). It is above 20 m for \(4 - 1 = 3\) s.
:::

## Two-particle problems

Two objects can start together or at different times, from the same place or from different places. Write an expression for each object's displacement from the same origin, **measured from the same moment**, then put the two equal when they meet (or use the condition given).

:::eg A cyclist rides at a constant \(6\ \mathrm{m\,s^{-1}}\) past a point \(O\). Four seconds later a motorcyclist leaves \(O\) from rest in the same direction with constant acceleration \(1.5\ \mathrm{m\,s^{-2}}\). When does the motorcyclist catch the cyclist, and how far from \(O\) is that?
Let \(t\) be the time in seconds after the cyclist passes \(O\). The cyclist has travelled \(6t\) metres. The motorcyclist has been moving for \(t - 4\) seconds, so travels \(\tfrac12(1.5)(t - 4)^2 = 0.75(t - 4)^2\) metres.
They meet when
\[6t = 0.75(t - 4)^2 \quad\Rightarrow\quad 0.75t^2 - 12t + 12 = 0 \quad\Rightarrow\quad t^2 - 16t + 16 = 0\]
\[t = 8 \pm \sqrt{48} = 14.93\ \text{or}\ 1.07\]
The motorcyclist starts at \(t = 4\), so \(t = 1.07\) is rejected. They meet at \(t = 14.9\) s, a distance of \(6 \times 14.93 = 89.6\) m from \(O\).
:::

:::eg Ball A is dropped from rest from the top of a 60 m tower. At the same moment ball B is thrown upwards from the ground at \(20\ \mathrm{m\,s^{-1}}\). When and where do they meet? Take \(g = 10\).
Measure height above the ground. A is at \(60 - 5t^2\) and B is at \(20t - 5t^2\). Equal heights:
\[60 - 5t^2 = 20t - 5t^2 \quad\Rightarrow\quad t = 3\ \text{s}\]
The height is \(20 \times 3 - 5 \times 9 = 15\) m. They meet after 3 s, 15 m above the ground. The \(t^2\) terms cancel because both balls have the same acceleration.
:::

## Variable acceleration and calculus

If the acceleration is not constant, the equations above do not apply. Use calculus instead, with displacement \(s\), velocity \(v\) and acceleration \(a\) all functions of time \(t\).

:::key Calculus in kinematics
\[v = \frac{ds}{dt} \qquad a = \frac{dv}{dt} = \frac{d^2s}{dt^2}\]
\[v = \int a\,dt \qquad s = \int v\,dt\]
- Each integration needs a constant, found from a given value such as "\(s = 0\) when \(t = 0\)" or "\(v = 5\) when \(t = 0\)".
- The object is **at rest** when \(v = 0\). It is at its greatest speed or turns round where \(a = 0\) or \(v = 0\) respectively, so solve \(v = 0\) or \(a = 0\) as the question needs.
- Displacement between two times: \(\displaystyle\int_{t_1}^{t_2} v\,dt\). **Distance** travelled needs the integral split wherever \(v\) changes sign.
:::

:::eg A particle moves along a line with displacement \(s = t^3 - 6t^2 + 9t\) metres from \(O\) at time \(t\) seconds, \(t \ge 0\). Find the velocity and acceleration, the times it is at rest, and the distance travelled in the first 4 seconds.
\[v = \frac{ds}{dt} = 3t^2 - 12t + 9 = 3(t - 1)(t - 3) \qquad a = \frac{dv}{dt} = 6t - 12\]
At rest when \(v = 0\): \(t = 1\) and \(t = 3\).
Positions: \(s(0) = 0\), \(s(1) = 1 - 6 + 9 = 4\), \(s(3) = 27 - 54 + 27 = 0\), \(s(4) = 64 - 96 + 36 = 4\).
The particle moves from 0 to 4 (\(t = 0\) to 1), back from 4 to 0 (\(t = 1\) to 3) and then from 0 to 4 again (\(t = 3\) to 4). The **distance travelled** is \(4 + 4 + 4 = 12\) m, while the displacement after 4 s is \(+4\) m.
:::

:::eg A particle starts from rest at \(O\) with acceleration \(a = 4 - 2t\ \mathrm{m\,s^{-2}}\). Find the velocity and displacement at time \(t\), the maximum velocity, and when and where the particle first comes to rest again.
\[v = \int (4 - 2t)\,dt = 4t - t^2 + c\]
\(v = 0\) when \(t = 0\), so \(c = 0\) and \(v = 4t - t^2\).
\[s = \int (4t - t^2)\,dt = 2t^2 - \frac{t^3}{3} + k\]
\(s = 0\) when \(t = 0\), so \(k = 0\).
The velocity is greatest when \(a = 0\), that is \(4 - 2t = 0\), \(t = 2\): \(v = 8 - 4 = 4\ \mathrm{m\,s^{-1}}\).
It is at rest again when \(4t - t^2 = t(4 - t) = 0\), \(t = 4\) s. Then \(s = 32 - \dfrac{64}{3} = \dfrac{32}{3} = 10.7\) m from \(O\).
:::

:::tip Choosing the method
Is the acceleration a number? Use the constant acceleration equations. Is it a function of \(t\)? Use calculus. A question that gives a velocity–time graph made of straight lines should be answered with gradients and areas.
:::

## Exam-style questions

:::eg (Exam style) A car moves along a straight road. It accelerates uniformly from rest for 10 s, travels at constant speed \(V\ \mathrm{m\,s^{-1}}\) for 40 s, then decelerates uniformly to rest in 15 s. The total distance is 1050 m. (a) Sketch the \(v\)–\(t\) graph. (b) Find \(V\). (c) Find the acceleration in the first stage. (d) Find the time at which the car's speed first falls to \(16\ \mathrm{m\,s^{-1}}\) during the deceleration. [8 marks]
(a) A trapezium: a line from \((0, 0)\) to \((10, V)\), a horizontal line to \((50, V)\), then a line down to \((65, 0)\). [B1]

(b) The area is
\[\tfrac12 \times 10 \times V + 40V + \tfrac12 \times 15 \times V = 52.5V = 1050\] [M1 A1]
so \(V = 20\). [A1]

(c) \(a = \dfrac{20}{10} = 2\ \mathrm{m\,s^{-2}}\). [B1]

(d) The deceleration is \(\dfrac{20}{15} = \dfrac43\ \mathrm{m\,s^{-2}}\). [M1] Speed \(= 16\) when \(20 - \dfrac43\tau = 16\), so \(\tau = 3\) s after the deceleration starts, that is at \(t = 50 + 3 = 53\) s. [M1 A1]
:::

:::eg (Exam style) A particle moves on a straight line. At time \(t\) seconds, \(t \ge 0\), its velocity is \(v = t^2 - 6t + 8\ \mathrm{m\,s^{-1}}\). (a) Find the times at which the particle is at rest. (b) Find the acceleration when \(t = 0\). (c) Find the displacement of the particle from its starting position when \(t = 4\), and the distance it travels in the first 4 seconds. [9 marks]
(a) \(v = (t - 2)(t - 4) = 0\), so \(t = 2\) and \(t = 4\). [M1 A1]

(b) \(a = \dfrac{dv}{dt} = 2t - 6\), so at \(t = 0\), \(a = -6\ \mathrm{m\,s^{-2}}\). [M1 A1]

(c) \(s = \displaystyle\int (t^2 - 6t + 8)\,dt = \frac{t^3}{3} - 3t^2 + 8t\) (taking \(s = 0\) at \(t = 0\)). [M1 A1]
\[s(2) = \frac83 - 12 + 16 = \frac{20}{3} \qquad s(4) = \frac{64}{3} - 48 + 32 = \frac{16}{3}\]
The displacement at \(t = 4\) is \(\dfrac{16}{3} = 5.33\) m. [A1]
The velocity is positive for \(0 < t < 2\) and negative for \(2 < t < 4\), so the particle goes out to \(\tfrac{20}{3}\) m and returns \(\tfrac{20}{3} - \tfrac{16}{3} = \tfrac43\) m. [M1] The distance is \(\tfrac{20}{3} + \tfrac43 = 8\) m. [A1]
:::

:::exam Technique
- Always state your positive direction, and keep it for every quantity.
- Write down \(s, u, v, a, t\) with their values and signs before choosing an equation.
- "Show that" questions need the working that leads to the given value, with the exact answer before any rounding.
- For a "distance" question about calculus, check where \(v\) changes sign; for "displacement" simply integrate.
- Give units in final answers, and 3 s.f. unless the answer is exact.
:::

:::board
- **Edexcel IAL and UK boards** use \(g = 9.8\ \mathrm{m\,s^{-2}}\) where this chapter uses 10. Cambridge always says "take \(g = 10\)" when it matters.
- **Edexcel IAL**: kinematics with constant acceleration is in M1, and calculus-based motion is in M2.
- **UK A Level (AQA, Edexcel 9MA0, OCR)**: kinematics is part of the Mechanics content, with \(g = 9.8\) and vector notation (\(\mathbf{i}\), \(\mathbf{j}\)) in two-dimensional motion. Cambridge 9709 has no vector notation in P4, and this chapter is one-dimensional.
:::

:::try Start easy, finish at exam standard
Q: A runner completes one lap of a 400 m track in 80 s, finishing where she started. Find her average speed and average velocity.
A: Average speed \(= \dfrac{400}{80} = 5\ \mathrm{m\,s^{-1}}\). Her displacement is 0, so her average velocity is 0.
Q: A car accelerates uniformly from rest to \(12\ \mathrm{m\,s^{-1}}\) in 6 s, travels at that speed for 10 s, then decelerates uniformly to rest in 4 s. Find the total distance and the average speed.
A: Distance \(= \tfrac12 \times 6 \times 12 + 10 \times 12 + \tfrac12 \times 4 \times 12 = 36 + 120 + 24 = 180\) m. Time \(= 20\) s, so the average speed is \(9\ \mathrm{m\,s^{-1}}\).
Q: A particle has \(u = 5\ \mathrm{m\,s^{-1}}\), constant acceleration \(2\ \mathrm{m\,s^{-2}}\) and moves for 8 s. Find its displacement and final velocity.
A: \(s = 5 \times 8 + \tfrac12 \times 2 \times 64 = 40 + 64 = 104\) m. \(v = 5 + 2 \times 8 = 21\ \mathrm{m\,s^{-1}}\).
Q: A motorbike accelerates uniformly from rest to \(30\ \mathrm{m\,s^{-1}}\) over 225 m. Find the acceleration and the time taken.
A: \(900 = 0 + 2a(225)\), so \(a = 2\ \mathrm{m\,s^{-2}}\). \(t = \dfrac{30}{2} = 15\) s.
Q: A car travelling at \(20\ \mathrm{m\,s^{-1}}\) brakes uniformly and stops in 50 m. Find the deceleration and the time taken.
A: \(0 = 400 + 2a(50)\), so \(a = -4\), a deceleration of \(4\ \mathrm{m\,s^{-2}}\). \(0 = 20 - 4t\), so \(t = 5\) s. Check: \(s = \tfrac12(20 + 0) \times 5 = 50\). ✓
Q: A stone is dropped from rest from a height of 45 m. Find the time to reach the ground and the speed when it lands. Take \(g = 10\).
A: \(45 = 5t^2\), so \(t = 3\) s. \(v = 10 \times 3 = 30\ \mathrm{m\,s^{-1}}\).
Q: A particle has displacement \(s = 2t^3 - 15t^2 + 36t\) metres. Find the times at which it is at rest, the displacement at those times, and the acceleration at the first of them.
A: \(v = 6t^2 - 30t + 36 = 6(t - 2)(t - 3)\), so at rest at \(t = 2\) and \(t = 3\). \(s(2) = 16 - 60 + 72 = 28\), \(s(3) = 54 - 135 + 108 = 27\). \(a = 12t - 30\), so at \(t = 2\), \(a = -6\ \mathrm{m\,s^{-2}}\).
Q: The velocity of a particle is \(v = 6t - t^2\) for \(0 \le t \le 6\). Find the greatest velocity and the displacement from \(t = 0\) to \(t = 6\).
A: \(a = 6 - 2t = 0\) at \(t = 3\), so the greatest velocity is \(18 - 9 = 9\ \mathrm{m\,s^{-1}}\). \(s = \left[3t^2 - \dfrac{t^3}{3}\right]_0^6 = 108 - 72 = 36\) m.
Q: (Exam style) Particle A passes a point \(O\) with constant speed \(5\ \mathrm{m\,s^{-1}}\). At the same moment particle B is at rest 60 m ahead of \(O\) on the same line and moves back towards \(O\) with constant acceleration \(1.5\ \mathrm{m\,s^{-2}}\). Find the time at which they meet. [5 marks]
A: A is at \(5t\) from \(O\). B is at \(60 - \tfrac12(1.5)t^2 = 60 - 0.75t^2\). [M1 A1] They meet when \(5t = 60 - 0.75t^2\), so \(3t^2 + 20t - 240 = 0\). [M1] \(t = \dfrac{-20 + \sqrt{400 + 2880}}{6} = 6.21\) s (the negative root is rejected). [M1 A1]
Q: (Exam style) A ball is thrown vertically upwards from a point 15 m above the ground with speed \(10\ \mathrm{m\,s^{-1}}\). Find the time it takes to reach the ground and its speed on impact. Take \(g = 10\). [5 marks]
A: Up positive: \(-15 = 10t - 5t^2\), so \(t^2 - 2t - 3 = 0\). [M1 A1] \((t - 3)(t + 1) = 0\), so \(t = 3\) s. [A1] \(v = 10 - 30 = -20\), so the speed is \(20\ \mathrm{m\,s^{-1}}\). [M1 A1]
:::

:::quiz Check your understanding
? A car goes round a circular track and finishes at its starting point. Which is zero?
- distance
- average speed
+ displacement
- time
> Displacement compares the finish with the start, so it is zero. Distance and average speed count the whole path.
? On a velocity–time graph, the area under the graph between two times represents:
- acceleration
+ displacement
- speed
- force
> Area under a \(v\)–\(t\) graph is displacement. The gradient gives acceleration.
? A ball is thrown upwards. At its highest point:
- \(v = 0\) and \(a = 0\)
+ \(v = 0\) and \(a = -10\ \mathrm{m\,s^{-2}}\)
- \(v = 10\) and \(a = 0\)
- \(v = 0\) and \(a = +10\ \mathrm{m\,s^{-2}}\)
> The velocity is momentarily zero but gravity still acts, so the acceleration is \(-10\) when up is positive.
? A particle starts at rest and accelerates at \(3\ \mathrm{m\,s^{-2}}\) for 4 s. How far does it travel?
- 12 m
- 48 m
+ 24 m
- 6 m
> \(s = \tfrac12 at^2 = \tfrac12 \times 3 \times 16 = 24\). Using \(at^2\) gives 48, and \(at\) gives 12 (the final speed).
? \(v = 3t^2 - 4\). What is the acceleration at \(t = 2\)?
- 8
+ 12
- 0
- 4
> \(a = \dfrac{dv}{dt} = 6t = 12\) when \(t = 2\). Substituting into \(v\) gives 8, the velocity.
:::

:::recap
- Distance and speed are scalars. Displacement, velocity and acceleration are vectors: choose a positive direction and use signs.
- \(v\)–\(t\) graph: gradient = acceleration, area = displacement. Distance counts areas below the axis as positive.
- Constant acceleration: \(v = u + at\), \(s = \tfrac12(u + v)t\), \(s = ut + \tfrac12 at^2\), \(v^2 = u^2 + 2as\).
- Free fall: \(a = -10\) with up positive, whether rising or falling. The time up equals the time down to the same level.
- Two particles: write each displacement from a common origin and a common start time, then equate.
- Variable acceleration: \(v = \dfrac{ds}{dt}\), \(a = \dfrac{dv}{dt}\); integrate with constants from the given conditions. Split the integral where \(v\) changes sign to find distance.
:::

:::note Learn more online
- **Watch:** [Constant acceleration (suvat)](https://www.examsolutions.net/tutorials/motion-straight-line-constant-acceleration-suvat/) · ExamSolutions · choosing the right equation
- **Watch:** [Exam questions: velocity–time graphs](https://www.examsolutions.net/tutorials/velocity-time-graphs-exam-questions/) · ExamSolutions · areas and gradients in exam style
- **Practise:** [CAIE Mechanics kinematics graphs exam questions](https://www.savemyexams.com/a-level/maths/cie/20/mechanics/topic-questions/kinematics-straight-line-motion/kinematics-graphs/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Practise:** [Isaac Science](https://isaacscience.org/) · Isaac Science · free problem-solving practice, including kinematics (free account)
- **Read:** [University Physics Volume 1 (free textbook)](https://openstax.org/details/books/university-physics-volume-1) · OpenStax · the chapter on motion along a straight line

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Newton's laws and connected particles](#math.m.newton).
