@chapter math.m.projectiles
@title Projectiles and moments (UK boards)
@level ext
@paper Edexcel IAL M1 and M2 · AQA 7357 / Edexcel 9MA0 / OCR H240 Mechanics · not in CAIE 9709 P4
@time 7–9 hours
@summary A projectile moves under gravity alone, so its horizontal and vertical motions can be treated separately. You will learn to resolve the launch velocity, find the time of flight, range and greatest height, use the equation of the trajectory, and then the second topic of this chapter: the moment of a force and the equilibrium of a rod or beam.

:::why
A footballer's free kick, a water jet, and the arc of a thrown javelin all follow the same curve, and you can predict it with two ideas you already know: constant velocity in one direction and constant acceleration in the other. Moments are the other half of statics: forces can balance and still make an object turn, which is why a see-saw works and a plank can tip. This chapter is **not in the CAIE 9709 Paper 4 syllabus**; it is for students on Edexcel IAL or UK A Level courses and a good extension for everyone else.
:::

**Before you start**, you need the constant acceleration equations from [Kinematics](#math.m.kinematics), resolving forces from [Forces and equilibrium](#math.m.forces) and trigonometry from [Trigonometry](#math.p1.trig). Quadratics are in [Quadratics](#math.p1.quadratics).

## Projectile motion

:::def Projectile
An object that moves through the air under the force of gravity alone, with air resistance ignored. Its acceleration is \(g\) downwards, and there is no force, and so no acceleration, horizontally.
:::

A projectile is launched with speed \(u\) at angle \(\alpha\) above the horizontal. Resolve the velocity into components, and treat the two directions separately:

| | Horizontal | Vertical (up positive) |
|---|---|---|
| Initial velocity | \(u\cos\alpha\) | \(u\sin\alpha\) |
| Acceleration | 0 | \(-g\) |
| Velocity at time \(t\) | \(u\cos\alpha\) (constant) | \(u\sin\alpha - gt\) |
| Displacement at time \(t\) | \(x = ut\cos\alpha\) | \(y = ut\sin\alpha - \tfrac12 gt^2\) |

:::key Projectile results (launched from ground level)
- Time of flight (back to the launch height): \(T = \dfrac{2u\sin\alpha}{g}\)
- Greatest height: \(H = \dfrac{u^2\sin^2\alpha}{2g}\), reached at \(t = \dfrac{u\sin\alpha}{g}\)
- Range: \(R = \dfrac{u^2\sin 2\alpha}{g}\), which is greatest when \(\alpha = 45^\circ\)
- Trajectory: \(y = x\tan\alpha - \dfrac{gx^2}{2u^2\cos^2\alpha}\), a parabola
- Speed at time \(t\): \(\sqrt{(u\cos\alpha)^2 + (u\sin\alpha - gt)^2}\); direction \(\tan\theta = \dfrac{u\sin\alpha - gt}{u\cos\alpha}\)
Do not memorise these without understanding them: in exams, it is safer to build each result from the table.
:::

:::steps
1. Resolve the initial velocity into horizontal and vertical components.
2. Use the vertical motion (\(a = -g\)) to find the time (to the top, to the ground, or to a given height).
3. Use the horizontal motion (constant velocity) with that time to find the horizontal distance.
4. To find the velocity at a time \(t\), combine the horizontal and vertical components with Pythagoras and \(\tan\).
:::

:::plot A projectile launched at \(20\ \mathrm{m\,s^{-1}}\) at \(45^\circ\), with \(g = 10\), has \(y = x - \dfrac{x^2}{40}\). The range is 40 m and the greatest height is 10 m.
--f "x-x**2/40" --label "y = x − x²/40" --x 0 52 --y 0 14 --pt "20,10,greatest height 10 m@n" --pt "40,0,range 40 m@ne" --legend tr --xlabel "x (m)" --ylabel "y (m)"
:::

Try the launcher below. Press Launch with a few different angles and compare the faint earlier paths. Which angle gives the longest range? Add a launch height and see what happens to it.

:::html
<div class="widget" data-w="projectile" data-speed="20" data-angle="45" data-height="0"></div>
:::

:::eg A ball is projected from level ground at \(20\ \mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal. Find the time of flight, the greatest height and the range. Take \(g = 10\).
Components: \(u\cos 30^\circ = 17.32\) and \(u\sin 30^\circ = 10\).
Vertically: back at ground when \(0 = 10t - 5t^2 = 5t(2 - t)\), so \(T = 2\) s.
Greatest height: \(0 = 10^2 - 2 \times 10 \times H\), so \(H = 5\) m.
Range: \(17.32 \times 2 = 34.6\) m.
:::

:::eg A ball is thrown horizontally at \(12\ \mathrm{m\,s^{-1}}\) from the top of a cliff 45 m high. Find the time to reach the sea, the horizontal distance from the cliff, and the speed and direction when it lands. Take \(g = 10\).
Vertically (down positive): \(u_y = 0\), \(s = 45\): \(45 = 5t^2\), so \(t = 3\) s.
Horizontal distance: \(12 \times 3 = 36\) m.
On landing: horizontal velocity \(12\), vertical velocity \(10 \times 3 = 30\) downwards.
\[\text{speed} = \sqrt{12^2 + 30^2} = \sqrt{1044} = 32.3\ \mathrm{m\,s^{-1}}\]
\[\theta = \tan^{-1}\frac{30}{12} = 68.2^\circ \text{ below the horizontal}\]
:::

:::eg A ball is projected from the top of a tower 30 m high at \(20\ \mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal. Find the time to hit the ground, the horizontal distance, and the speed at impact. Take \(g = 10\).
Up is positive: \(u_y = 10\), displacement \(= -30\):
\[-30 = 10t - 5t^2 \quad\Rightarrow\quad t^2 - 2t - 6 = 0 \quad\Rightarrow\quad t = 1 + \sqrt7 = 3.65\ \text{s}\]
Horizontal distance: \(17.32 \times 3.646 = 63.1\) m.
Speed: \(v_y = 10 - 10 \times 3.646 = -26.46\), so \(v = \sqrt{17.32^2 + 26.46^2} = 31.6\ \mathrm{m\,s^{-1}}\).
Energy check: \(v^2 = 20^2 + 2 \times 10 \times 30 = 1000\), so \(v = 31.6\). ✓
:::

:::eg A ball is hit from the ground at \(25\ \mathrm{m\,s^{-1}}\) at an angle \(\alpha\) with \(\tan\alpha = \tfrac34\). A wall 4 m high stands 20 m away. Does the ball clear the wall? Take \(g = 10\).
\(\sin\alpha = 0.6\), \(\cos\alpha = 0.8\), so the components are \(u\cos\alpha = 20\) and \(u\sin\alpha = 15\).
At the wall \(x = 20\), so \(t = 1\) s. Then
\[y = 15(1) - 5(1)^2 = 10\ \text{m}\]
Using the trajectory equation: \(y = 20 \times 0.75 - \dfrac{10 \times 400}{2 \times 25^2 \times 0.64} = 15 - 5 = 10\) m. ✓
At the wall the ball is 10 m high, which is above 4 m, so the ball clears the wall.
:::

:::warn Projectile slips
- Using the same signs for \(g\) in two different directions. Choose one positive direction for the vertical motion and keep it.
- Using the speed instead of the components: always resolve into \(u\cos\alpha\) and \(u\sin\alpha\).
- Adding the vertical and horizontal speeds. The speed is \(\sqrt{v_x^2 + v_y^2}\).
- Forgetting that the time is the link: find \(t\) from the vertical motion, then use it for the horizontal.
- Using the range formula when the launch and landing heights differ. It only works for level ground.
:::

## Moments and equilibrium of rigid bodies

So far a "particle" had no size, so forces could not make it turn. A **rigid body** (a rod, beam or plank) has size, and a force can turn it about a point or **pivot**.

:::def Moment of a force
The moment of a force about a point is the size of the force multiplied by the **perpendicular** distance from the point to the line of action of the force. It is measured in N m. A moment is **clockwise** or **anticlockwise**.
:::

:::key Equilibrium of a rigid body
A body is in equilibrium when:
1. the resultant force is zero (forces balance in two perpendicular directions), and
2. the total moment about **any** point is zero: clockwise moments = anticlockwise moments (the **principle of moments**).
- The weight of a **uniform** rod acts at its centre.
- A force acting at the pivot has no moment about that pivot: choose the pivot where an unknown force acts to remove it from the equation.
- If a force makes an angle with the rod, use the perpendicular component (or perpendicular distance).
:::

:::eg A uniform see-saw is balanced on a central pivot. A child of mass 30 kg sits 2 m from the pivot. Where must a 40 kg child sit on the other side? Take \(g = 10\).
Moments about the pivot: \(300 \times 2 = 400 \times d\), so \(d = 1.5\) m. (The see-saw's own weight passes through the pivot and has no moment.)
:::

:::html
<figure class="fig"><svg viewBox="0 0 520 170" role="img" aria-label="A horizontal beam AB, 6 metres long, rests on a support at A and a support at C, 4 metres from A. Its weight of 200 newtons acts at the centre, and a 50 newton load hangs at B. Upward reactions R_A at A and R_C at C are shown."><rect class="f1 s-acc sw2" x="60" y="70" width="400" height="14"/><path class="f2 s-acc sw2" d="M60 84L50 112H70Z"/><path class="f2 s-acc sw2" d="M327 84L317 112H337Z"/><path class="c1 thick" d="M260 22V66" marker-end="url(#ah)"/><path class="c1 thick" d="M460 22V66" marker-end="url(#ah)"/><path class="c2 thick" d="M60 150V118" marker-end="url(#ah)"/><path class="c2 thick" d="M327 150V118" marker-end="url(#ah)"/><text class="tl" x="268" y="36">200 N</text><text class="tl" x="466" y="36">50 N</text><text class="tl" x="68" y="146">R_A</text><text class="tl" x="335" y="146">R_C</text><text class="tl" x="60" y="62" text-anchor="middle">A</text><text class="tl" x="327" y="62" text-anchor="middle">C</text><text class="tl" x="460" y="100" text-anchor="middle">B</text></svg><figcaption>A uniform beam \(AB\) of weight 200 N, length 6 m, on supports at \(A\) and \(C\) with \(AC = 4\) m, carrying a 50 N load at \(B\).</figcaption></figure>
:::

:::eg A uniform beam \(AB\) of length 6 m and mass 20 kg rests on supports at \(A\) and at \(C\), where \(AC = 4\) m. A mass of 5 kg is placed at \(B\). Find the reactions at the supports. Take \(g = 10\).
The beam's weight is 200 N, acting 3 m from \(A\). The load is 50 N at \(B\), 6 m from \(A\).
Moments about \(A\) (this removes \(R_A\)):
\[R_C \times 4 = 200 \times 3 + 50 \times 6 = 900 \quad\Rightarrow\quad R_C = 225\ \text{N}\]
Resolving vertically: \(R_A + R_C = 250\), so \(R_A = 25\) N.
Check by taking moments about \(C\): \(R_A \times 4 + 50 \times 2 = 200 \times 1\), that is \(100 + 100 = 200\). ✓
:::

:::eg A uniform rod \(AB\) of length 2 m and mass 6 kg is hinged to a wall at \(A\) and held horizontal by a light string from \(B\) to a point on the wall above \(A\). The string makes \(30^\circ\) with the rod. Find the tension, and the size of the force at the hinge. Take \(g = 10\).
Weight \(= 60\) N at the centre, 1 m from \(A\). Take moments about \(A\) (the hinge force has no moment). The vertical component of the tension is \(T\sin 30^\circ\), at 2 m from \(A\):
\[T\sin 30^\circ \times 2 = 60 \times 1 \quad\Rightarrow\quad T = 60\ \text{N}\]
Resolve: horizontal component of the hinge force \(X = T\cos 30^\circ = 52.0\) N, directed away from the wall (the string pulls \(B\) towards the wall). Vertical: \(Y + T\sin 30^\circ = 60\), so \(Y = 30\) N upwards.
Hinge force \(= \sqrt{52.0^2 + 30^2} = 60\) N, at \(30^\circ\) to the horizontal.
:::

### Tipping

A plank on two supports is about to tip about one support when the reaction at the other support becomes zero.

:::eg A uniform plank \(AB\) of length 5 m and mass 20 kg rests horizontally on supports at \(C\) and \(D\), where \(AC = 1\) m and \(DB = 1\) m. A man of mass 40 kg walks along the plank towards \(B\). How far beyond \(D\) can he go before the plank tips? Take \(g = 10\).
The plank is about to tip about \(D\) when \(R_C = 0\). Let the man be \(x\) m beyond \(D\). Moments about \(D\): the man (400 N) at distance \(x\) is clockwise; the plank's weight (200 N), acting at the centre \(2.5\) m from \(A\), which is \(1.5\) m to the left of \(D\), is anticlockwise:
\[400x = 200 \times 1.5 \quad\Rightarrow\quad x = 0.75\ \text{m}\]
He can walk 0.75 m beyond \(D\), that is to within 0.25 m of \(B\), before the plank tips.
:::

## Exam-style questions

:::eg (Exam style) A particle is projected from a point \(O\) on level ground with speed \(26\ \mathrm{m\,s^{-1}}\) at an angle \(\alpha\) above the horizontal, where \(\tan\alpha = \tfrac{5}{12}\). Take \(g = 10\). (a) Show that the greatest height is 5 m and find the range. (b) Find the speed and direction of motion after 1.5 s. [8 marks]
\(\sin\alpha = \tfrac5{13}\), \(\cos\alpha = \tfrac{12}{13}\). Components: horizontal \(24\), vertical \(10\). [B1]

(a) Greatest height: \(0 = 10^2 - 2 \times 10 \times H\), so \(H = 5\) m. [M1 A1]
Time of flight: \(0 = 10t - 5t^2\), so \(T = 2\) s. [M1] Range \(= 24 \times 2 = 48\) m. [A1]

(b) At \(t = 1.5\): \(v_x = 24\), \(v_y = 10 - 15 = -5\). [M1] Speed \(= \sqrt{24^2 + 5^2} = 24.5\ \mathrm{m\,s^{-1}}\). [A1] Direction: \(\tan^{-1}\dfrac{5}{24} = 11.8^\circ\) below the horizontal. [A1]
:::

:::eg (Exam style) A uniform plank \(AB\) of mass 12 kg and length 4 m rests on a support at \(A\) and a support at \(C\), where \(AC = 3\) m. A load of mass 8 kg is placed at \(B\). Find the reactions at \(A\) and \(C\). The load is replaced by a heavier one at \(B\). Find the greatest mass of the load that can be placed at \(B\) without the plank tipping about \(C\). Take \(g = 10\). [7 marks]
Plank weight 120 N at 2 m from \(A\). Load 80 N at \(B\), 4 m from \(A\).
Moments about \(A\): \(R_C \times 3 = 120 \times 2 + 80 \times 4 = 560\) [M1 A1], so \(R_C = 186.7\) N. [A1]
\(R_A = 200 - 186.7 = 13.3\) N. [B1]
About to tip about \(C\): \(R_A = 0\). Moments about \(C\): the load \(W\) at \(1\) m from \(C\) is clockwise, the plank's weight at 1 m on the other side is anticlockwise: \(W \times 1 = 120 \times 1\). [M1 A1] The greatest load has weight 120 N, mass 12 kg. [A1]
:::

:::exam Technique
- In projectile questions, say "horizontally, constant velocity" and "vertically, \(a = -g\)". The mark scheme rewards a clear separation.
- Define the positive direction in each question and the point you take moments about.
- For moments, choose the pivot where unknown forces act to eliminate them.
- Quote \(g = 9.8\) for IAL and UK papers (check the question). This chapter uses 10 for tidy numbers.
:::

:::board
- **Edexcel IAL**: moments are in IAL M1, and projectiles in IAL M2. IAL and UK boards use \(g = 9.8\).
- **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: projectiles and moments are in the mechanics content (moments with ladders, beams and friction), and the trajectory equation is used.
- **CAIE 9709**: neither topic is in Paper 4.
:::

:::try Start easy, finish at exam standard
Q: A ball is launched at \(40\ \mathrm{m\,s^{-1}}\) at \(60^\circ\) above the horizontal. Find the horizontal and vertical components of the velocity.
A: Horizontal \(40\cos 60^\circ = 20\ \mathrm{m\,s^{-1}}\). Vertical \(40\sin 60^\circ = 34.6\ \mathrm{m\,s^{-1}}\).
Q: A ball is projected from the ground at \(30\ \mathrm{m\,s^{-1}}\) at \(30^\circ\). Find the time of flight, the greatest height and the range. Take \(g = 10\).
A: Vertical component 15, horizontal \(25.98\). \(T = \dfrac{2 \times 15}{10} = 3\) s. \(H = \dfrac{15^2}{20} = 11.25\) m. \(R = 25.98 \times 3 = 77.9\) m.
Q: A stone is thrown horizontally at \(15\ \mathrm{m\,s^{-1}}\) from a bridge 20 m above the water. Find the time to hit the water and the horizontal distance travelled. Take \(g = 10\).
A: \(20 = 5t^2\), so \(t = 2\) s. Distance \(= 15 \times 2 = 30\) m.
Q: A projectile has speed \(20\ \mathrm{m\,s^{-1}}\). Find the greatest possible range on level ground, and the angle that gives it. Take \(g = 10\).
A: \(R = \dfrac{u^2\sin 2\alpha}{g}\) is greatest when \(\sin 2\alpha = 1\): \(R = \dfrac{400}{10} = 40\) m at \(\alpha = 45^\circ\).
Q: A ball is projected at \(20\ \mathrm{m\,s^{-1}}\) at \(45^\circ\) from the ground. Use the trajectory \(y = x - \dfrac{x^2}{40}\) to find its height when \(x = 30\) m.
A: \(y = 30 - \dfrac{900}{40} = 30 - 22.5 = 7.5\) m.
Q: A projectile is launched at \(20\ \mathrm{m\,s^{-1}}\) and lands on level ground 30 m away. Find the two possible angles of projection. Take \(g = 10\).
A: \(30 = \dfrac{400\sin 2\alpha}{10}\), so \(\sin 2\alpha = 0.75\). \(2\alpha = 48.6^\circ\) or \(131.4^\circ\), so \(\alpha = 24.3^\circ\) or \(65.7^\circ\).
Q: A child of mass 25 kg sits 1.8 m from the pivot of a balanced see-saw. Where must a child of mass 30 kg sit on the other side? Take \(g = 10\).
A: \(250 \times 1.8 = 300 \times d\), so \(d = 1.5\) m.
Q: A uniform rod of length 3 m and mass 4 kg is hinged at one end \(A\) and held horizontal by a vertical string at a point \(C\), 2 m from \(A\). Find the tension in the string and the vertical force at the hinge. Take \(g = 10\).
A: Moments about \(A\): \(T \times 2 = 40 \times 1.5\), so \(T = 30\) N. Vertically \(Y + 30 = 40\), so \(Y = 10\) N upwards.
Q: (Exam style) A ball is projected from the top of a cliff 20 m high at \(15\ \mathrm{m\,s^{-1}}\) at an angle \(\alpha\) above the horizontal, with \(\tan\alpha = \tfrac43\). Find the time to hit the ground, the horizontal distance from the cliff and the speed on landing. Take \(g = 10\). [7 marks]
A: Components: horizontal 9, vertical 12. [B1] \(-20 = 12t - 5t^2\), so \(5t^2 - 12t - 20 = 0\). [M1 A1] \(t = \dfrac{12 + \sqrt{544}}{10} = 3.53\) s. [A1] Horizontal distance \(= 9 \times 3.532 = 31.8\) m. [A1] Speed: \(v^2 = 15^2 + 2 \times 10 \times 20 = 625\), so \(v = 25\ \mathrm{m\,s^{-1}}\). [M1 A1]
Q: (Exam style) A uniform plank \(AB\) of length 4 m and mass 12 kg rests on supports at \(A\) and \(C\) with \(AC = 3\) m. A load of mass 8 kg is at \(B\). Find the reaction at \(C\). [4 marks]
A: Weight of plank 120 N at 2 m, load 80 N at 4 m. [B1] Moments about \(A\): \(3R_C = 120 \times 2 + 80 \times 4 = 560\). [M1 A1] \(R_C = 187\) N. [A1]
:::

:::quiz Check your understanding
? At the top of its path a projectile has:
- zero velocity
+ horizontal velocity only, \(u\cos\alpha\)
- vertical velocity only
- zero acceleration
> The vertical velocity is zero at the top, but the horizontal velocity is unchanged, and the acceleration is still \(g\) downwards.
? A projectile on level ground has the greatest range when the angle of projection is:
- \(30^\circ\)
- \(60^\circ\)
+ \(45^\circ\)
- \(90^\circ\)
> \(R = \dfrac{u^2\sin 2\alpha}{g}\) is greatest when \(\sin 2\alpha = 1\), that is \(\alpha = 45^\circ\). Angles \(\alpha\) and \(90^\circ - \alpha\) give the same range.
? A ball is thrown horizontally from a cliff. Compared with a ball dropped from rest at the same moment, it lands:
- later
- earlier
+ at the same time
- depends on the speed
> The vertical motion is the same for both (\(u_y = 0\), \(a = g\)), so they land together. The horizontal motion does not affect the time.
? The moment of a 20 N force acting at a perpendicular distance of 0.5 m from a pivot is:
- 40 N m
+ 10 N m
- 10.5 N m
- 20 N m
> Moment \(=\) force \(\times\) perpendicular distance \(= 20 \times 0.5 = 10\) N m.
? A uniform rod is balanced on a pivot at its centre. A 3 N weight is hung 2 m to the left. A weight of 4 N must be hung to the right at:
- 1 m
+ 1.5 m
- 2.5 m
- 2 m
> \(3 \times 2 = 4 \times d\), so \(d = 1.5\) m. The rod's own weight is at the pivot and has no moment.
:::

:::recap
- Projectile: horizontal constant velocity \(u\cos\alpha\); vertical acceleration \(-g\) with initial velocity \(u\sin\alpha\). Time links the two.
- Level ground: \(T = \dfrac{2u\sin\alpha}{g}\), \(H = \dfrac{u^2\sin^2\alpha}{2g}\), \(R = \dfrac{u^2\sin 2\alpha}{g}\) (greatest at \(45^\circ\)). Trajectory \(y = x\tan\alpha - \dfrac{gx^2}{2u^2\cos^2\alpha}\).
- Speed \(= \sqrt{v_x^2 + v_y^2}\); angle from \(\tan\theta = \dfrac{v_y}{v_x}\).
- Moment \(=\) force \(\times\) perpendicular distance. Equilibrium: forces balance and moments balance about any point.
- Uniform rod: weight at the centre. About to tip: the reaction at the other support is zero.
:::

:::links
- watch: [Projectiles](https://www.examsolutions.net/tutorials/projectiles/) · ExamSolutions · horizontal and vertical motion separately
- watch: [Equation of the trajectory](https://www.examsolutions.net/tutorials/equation-of-the-trajectory-of-a-projectile/) · ExamSolutions · why the path is a parabola
- watch: [Horizontal beams in equilibrium](https://www.examsolutions.net/tutorials/moments-horizontal-beams/) · ExamSolutions · taking moments about a point
- practise: [Isaac Science](https://isaacscience.org/) · Isaac Science · free problem-solving practice (free account)
- explore: [Projectile Motion](https://phet.colorado.edu/en/simulations/projectile-motion) · PhET · change angle and speed and compare paths

Links checked 3 October 2026.
:::
Next: [Further Mathematics: a guided tour](#math.further).
