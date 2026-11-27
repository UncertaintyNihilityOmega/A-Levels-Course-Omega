@chapter math.fm.mock.p3
@title Mock Paper 3: Further Mechanics
@level mock
@paper CAIE 9231 Paper 3
@time 1 h 30 min
@summary A complete original mock for 9231 Paper 3 (Further Mechanics): 7 questions, 50 marks, 1 hour 30 minutes, laid out like the real papers (marks 5, 7, 6, 7, 7, 9, 9) and covering variable force, projectiles, centres of mass and toppling, a horizontal circle with an elastic string, direct and oblique impact, a vertical circle and elastic energy. Full mark scheme with accepted alternatives; sit it in one go, mark yourself and see which chapters to revise.

:::why
Paper 3 is the Further Mechanics paper: 50 marks in 90 minutes, seven or so questions, and every one of them is a short chain of ideas from the chapters you have studied (a force law, a circle, a collision, an energy equation). The marks are won by choosing the right principle at once, writing the equation with every term in it, and keeping the signs and the units straight. This mock has the same number of questions, the same spread of marks and the same kinds of task as the real papers, but every question is new. Do it under exam conditions first, then use the mark scheme to see what the examiner is looking for line by line.
:::

:::exam Instructions
- Answer **all** questions. The total is **50 marks** and you have **1 hour 30 minutes**.
- You will need the list of formulae **MF19**. You should use a calculator where appropriate: only a scientific calculator, no graphical or symbolic algebra calculator.
- You must show all necessary working clearly; **no marks will be given for unsupported answers from a calculator**.
- Give non-exact numerical answers correct to **3 significant figures**, or **1 decimal place for angles in degrees**, unless the question says otherwise.
- Where a numerical value for the acceleration due to gravity (\(g\)) is needed, use \(10\ \mathrm{m\,s^{-2}}\).
- The number of marks for each question or part question is shown in brackets [ ]. Roughly one and three-quarter minutes per mark leaves a few minutes at the end.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::tip A time plan
At 1.8 minutes per mark the paper needs about 90 minutes, so aim for 1.5 minutes per mark on the early questions and keep the last ten minutes to go back to anything you left. A reasonable split is Question 1: 8 min, Question 2: 11 min, Question 3: 9 min, Question 4: 11 min, Question 5: 11 min, Question 6: 14 min, Question 7: 14 min, which leaves about 12 minutes. Draw a diagram for every question that has a collision, a string or a slope: almost every lost mark in Further Mechanics begins with a missing or wrong diagram.
:::

:::try
Q: [5 marks] (#math.fm.variable) A particle \(P\) of mass \(0.5\) kg moves in a straight line on a smooth horizontal surface. At time \(t\) seconds the displacement of \(P\) from a fixed point \(O\) on the line is \(x\) metres, and its velocity is \(v\ \mathrm{m\,s^{-1}}\). The only horizontal force acting on \(P\) has magnitude \(\dfrac{3}{(x + 1)^2}\) newtons and acts towards \(O\). When \(t = 0\), \(P\) is at \(O\) and is moving away from \(O\) with speed \(4\ \mathrm{m\,s^{-1}}\).

(a) Show that, for \(x \ge 0\), \(v^2 = 4 + \dfrac{12}{x + 1}\). [4]

(b) Explain why \(P\) never comes to rest. [1]
A: (a) The force is towards \(O\) while \(P\) moves away from \(O\), so Newton's second law, with \(a = v\dfrac{dv}{dx}\), gives
\[0.5\,v\frac{dv}{dx} = -\frac{3}{(x + 1)^2}\]
[B1]
Separate the variables and integrate:
\[\int v\,dv = -6\int (x + 1)^{-2}\,dx\]
[M1]
\[\tfrac12 v^2 = \frac{6}{x + 1} + C\]
[A1]
When \(x = 0\), \(v = 4\): \(8 = 6 + C\), so \(C = 2\). [A1]
\[v^2 = \frac{12}{x + 1} + 4\]
as required. (Check: at \(x = 0\), \(v^2 = 16\).)

(b) \(\dfrac{12}{x + 1} > 0\) for every \(x \ge 0\), so \(v^2 > 4\) and \(v\) never reaches 0 (the speed tends to \(2\ \mathrm{m\,s^{-1}}\) as \(x \to \infty\)). [B1]
:::

:::try
Q: [7 marks] (#math.fm.projectiles) A particle is projected from a point \(O\) on horizontal ground with speed \(25\ \mathrm{m\,s^{-1}}\) at an angle \(\theta\) above the horizontal. The particle passes through the point \(P\), which is \(30\) m horizontally from \(O\) and \(20\) m above the ground. Take \(g = 10\).

(a) Show that \(18\tan^2\theta - 75\tan\theta + 68 = 0\). [3]

(b) Find the two possible values of \(\theta\). [2]

(c) Find the speed of the particle at \(P\), and state whether this speed depends on which value of \(\theta\) is used. [2]
A: (a) Use the equation of the trajectory (MF19), with \(\dfrac{1}{\cos^2\theta} = 1 + \tan^2\theta\):
\[y = x\tan\theta - \frac{g\,x^2\left(1 + \tan^2\theta\right)}{2u^2}\]
[M1]
Substitute \(x = 30\), \(y = 20\), \(u = 25\), \(g = 10\):
\[20 = 30\tan\theta - \frac{10 \times 900\left(1 + \tan^2\theta\right)}{2 \times 625}\]
[A1]
\[20 = 30\tan\theta - 7.2 - 7.2\tan^2\theta\]
Multiply by \(2.5\) and rearrange:
\[18\tan^2\theta - 75\tan\theta + 68 = 0\]
[A1] (given result; the previous line must be shown)

(b) Factorise or use the formula:
\[(3\tan\theta - 4)(6\tan\theta - 17) = 0\]
[M1]
\(\tan\theta = \tfrac43\) or \(\tfrac{17}{6}\), so \(\theta = 53.1^\circ\) or \(70.6^\circ\). [A1] (both needed)

(c) By energy conservation (no force does work except gravity):
\[\tfrac12 v^2 = \tfrac12(25)^2 - 10 \times 20\]
[M1]
\(v^2 = 625 - 400 = 225\), so the speed is \(15\ \mathrm{m\,s^{-1}}\). It does not depend on \(\theta\): the speed depends only on the height of \(P\). [A1]
(Alternative: for \(\theta = 53.1^\circ\), the components are \(15\) and \(0\), because \(P\) is the highest point; for \(\theta = 70.6^\circ\) they are \(8.32\) and \(-12.5\) (to 3 s.f.), and again \(v = 15\).)
:::

:::try
Q: [6 marks] (#math.fm.com) A uniform solid \(S\) is made by joining the plane face of a uniform solid cone to one circular face of a uniform solid cylinder. The cone and the cylinder are made of the same material and both have base radius \(3a\). The cylinder has height \(2a\) and the cone has height \(4a\), and their axes lie on the same line.

(a) Find the distance of the centre of mass of \(S\) from the free circular face of the cylinder. [4]

The solid \(S\) is placed with the free circular face of the cylinder on a rough plane that is inclined at an angle \(\alpha\) to the horizontal. The plane is rough enough to prevent \(S\) from sliding, and \(S\) is on the point of toppling.

(b) Find \(\alpha\). [2]
A: (a) Volumes (the masses are proportional to them, since the material is the same):
\[\text{cylinder } \pi(3a)^2(2a) = 18\pi a^3 \qquad \text{cone } \tfrac13\pi(3a)^2(4a) = 12\pi a^3\]
[B1]
Distances of the centres of mass from the free face of the cylinder: \(a\) for the cylinder, and \(2a + \tfrac14(4a) = 3a\) for the cone (the centre of mass of a cone is \(\tfrac14\) of its height from the base, MF19). [B1]
Take moments about the free face:
\[(18 + 12)\,\bar x = 18(a) + 12(3a)\]
[M1]
\[30\bar x = 54a \quad\text{so}\quad \bar x = \tfrac95 a = 1.8a\]
[A1]

(b) When \(S\) is on the point of toppling, the vertical line through the centre of mass passes through the lowest point of the circular edge of the base. The centre of mass is on the axis, \(\tfrac95 a\) from the base, and the edge is \(3a\) from the axis, so
\[\tan\alpha = \frac{3a}{\tfrac95 a}\]
[M1]
\[\tan\alpha = \tfrac53 \quad\text{so}\quad \alpha = 59.0^\circ\]
[A1]
:::

:::try
Q: [7 marks] (#math.fm.circular) A particle \(P\) of mass \(0.5\) kg is attached to one end of a light elastic string of natural length \(0.5\) m and modulus of elasticity \(15\) N. The other end of the string is attached to a fixed point \(O\). The particle moves in a horizontal circle, below the level of \(O\), with constant angular speed \(\omega\ \mathrm{rad\,s^{-1}}\). The length of the string is \(0.75\) m, and the string makes an angle \(\theta\) with the downward vertical. Take \(g = 10\).

(a) Find the tension in the string. [1]

(b) Show that \(\cos\theta = \tfrac23\). [2]

(c) Find the value of \(\omega\). [3]

(d) Find the speed of \(P\). [1]
A: (a) The extension is \(0.75 - 0.5 = 0.25\) m, so by Hooke's law
\[T = \frac{\lambda x}{l} = \frac{15 \times 0.25}{0.5} = 7.5\ \text{N}\]
[B1]

(b) Resolve vertically (no vertical acceleration):
\[T\cos\theta = mg = 5\]
[M1]
\[\cos\theta = \frac{5}{7.5} = \frac23\]
[A1] (given result)

(c) The radius of the circle is \(r = 0.75\sin\theta\). [B1]
Resolve horizontally, towards the centre of the circle:
\[T\sin\theta = m r\omega^2 = 0.5\left(0.75\sin\theta\right)\omega^2\]
[M1]
Cancel \(\sin\theta\): \(7.5 = 0.375\,\omega^2\), so \(\omega^2 = 20\) and
\[\omega = 4.47\ \mathrm{rad\,s^{-1}}\]
[A1]
(This is the answer to 3 s.f.; the exact value is \(2\sqrt5\).)

(d) \(\sin\theta = \dfrac{\sqrt5}{3}\), so \(r = 0.75 \times \dfrac{\sqrt5}{3} = 0.559\) m and
\[v = r\omega = 0.559 \times 4.472 = 2.5\ \mathrm{m\,s^{-1}}\]
[B1]
:::

:::try
Q: [7 marks] (#math.fm.oblique) Two uniform smooth spheres \(A\) and \(B\), of equal radii and of masses \(m\) and \(2m\), lie on a smooth horizontal surface. Sphere \(A\) is moving with speed \(10\ \mathrm{m\,s^{-1}}\) when it collides with \(B\), which is at rest. At the instant of impact the direction of motion of \(A\) makes an angle \(\alpha\) with the line of centres, where \(\cos\alpha = \tfrac45\). The coefficient of restitution between the spheres is \(\tfrac12\).

(a) Show that, after the collision, \(A\) moves at right angles to the line of centres, and find the speed of \(B\). [4]

After the collision \(B\) strikes a smooth fixed vertical wall. Just before the impact \(B\) is moving at \(30^\circ\) to the wall. The coefficient of restitution between \(B\) and the wall is \(\tfrac12\).

(b) Find the speed of \(B\) immediately after it strikes the wall. [3]
A: (a) Along the line of centres \(A\) has component \(10\cos\alpha = 8\), and perpendicular to it \(10\sin\alpha = 6\). The perpendicular component of each sphere is unchanged by the impact. [B1]
Let \(v_A\) and \(v_B\) be the velocities along the line of centres after impact. Conservation of momentum along the line of centres:
\[m(8) = m v_A + 2m v_B\]
[M1]
Newton's law of restitution:
\[v_B - v_A = \tfrac12(8 - 0) = 4\]
[M1]
Substitute \(v_A = v_B - 4\): \(8 = 3v_B - 4\), so \(v_B = 4\) and \(v_A = 0\). [A1]
So \(A\) has no velocity along the line of centres and moves with speed \(6\ \mathrm{m\,s^{-1}}\) at right angles to it, and \(B\) moves along the line of centres with speed \(4\ \mathrm{m\,s^{-1}}\).

(b) The speed of \(B\) before it hits the wall is \(4\), at \(30^\circ\) to the wall. Components: along the wall \(4\cos30^\circ = 2\sqrt3\) (unchanged by the smooth wall), perpendicular to the wall \(4\sin30^\circ = 2\). [B1]
Restitution at the wall: the perpendicular component after impact is \(\tfrac12 \times 2 = 1\). [M1]
\[\text{speed} = \sqrt{\left(2\sqrt3\right)^2 + 1^2} = \sqrt{13} = 3.61\ \mathrm{m\,s^{-1}}\]
[A1]
:::

:::try
Q: [9 marks] (#math.fm.vertical) A smooth solid sphere of radius \(0.9\) m is fixed with its lowest point on horizontal ground. A particle \(P\) of mass \(0.2\) kg is projected horizontally with speed \(1.5\ \mathrm{m\,s^{-1}}\) from the highest point of the sphere and moves on the outer surface. While \(P\) remains in contact with the sphere, the radius to \(P\) makes an angle \(\theta\) with the upward vertical and the normal reaction on \(P\) is \(R\) newtons. Take \(g = 10\).

(a) Show that \(R = 6\cos\theta - 4.5\). [4]

(b) Find the value of \(\theta\) at which \(P\) leaves the surface of the sphere. [2]

(c) Find the speed of \(P\) at the instant it leaves the surface. [1]

(d) Find the speed with which \(P\) hits the ground. [2]
A: (a) \(P\) has fallen a vertical distance \(0.9(1 - \cos\theta)\). Energy conservation (the sphere is smooth):
\[\tfrac12(0.2)v^2 = \tfrac12(0.2)(1.5)^2 + 0.2 \times 10 \times 0.9(1 - \cos\theta)\]
[M1]
\[v^2 = 2.25 + 18(1 - \cos\theta) = 20.25 - 18\cos\theta\]
[A1]
Resolve towards the centre of the sphere (down the radius):
\[0.2 \times 10\cos\theta - R = \frac{0.2\,v^2}{0.9}\]
[M1]
\[R = 2\cos\theta - \frac{0.2\left(20.25 - 18\cos\theta\right)}{0.9} = 2\cos\theta - 4.5 + 4\cos\theta\]
\[R = 6\cos\theta - 4.5\]
[A1] (given result)

(b) \(P\) leaves the surface when \(R = 0\): \(\cos\theta = \dfrac{4.5}{6} = 0.75\). [M1]
\[\theta = 41.4^\circ\]
[A1]

(c) When \(R = 0\) the weight component provides all the acceleration: \(v^2 = 20.25 - 18(0.75) = 6.75\), so
\[v = 2.60\ \mathrm{m\,s^{-1}}\]
[B1]

(d) After leaving the surface only gravity acts, so energy is still conserved. The highest point is \(1.8\) m above the ground, so
\[\tfrac12 v^2 = \tfrac12(1.5)^2 + 10 \times 1.8\]
[M1]
\[v^2 = 2.25 + 36 = 38.25 \quad\text{so}\quad v = 6.18\ \mathrm{m\,s^{-1}}\]
[A1]
:::

:::try
Q: [9 marks] (#math.fm.elastic) A particle \(P\) of mass \(0.5\) kg is attached to one end of a light elastic string of natural length \(0.8\) m and modulus of elasticity \(20\) N. The other end of the string is attached to a fixed point \(O\), and \(P\) hangs in equilibrium vertically below \(O\). Take \(g = 10\).

(a) Find the extension of the string when \(P\) is in equilibrium. [2]

The particle is pulled vertically downwards to the point \(B\), where the extension of the string is \(0.6\) m, and is released from rest.

(b) Find the speed of \(P\) when the string first becomes slack. [4]

(c) Find the greatest height of \(P\) above \(B\) in the subsequent motion. [3]
A: (a) In equilibrium the tension equals the weight:
\[\frac{\lambda e}{l} = mg \quad\Rightarrow\quad \frac{20e}{0.8} = 5\]
[M1]
\[e = 0.2\ \text{m}\]
[A1]

(b) The string becomes slack when \(P\) is at the point where the string has its natural length, which is \(0.6\) m above \(B\). The elastic energy stored at \(B\) is
\[\frac{\lambda x^2}{2l} = \frac{20 \times 0.6^2}{2 \times 0.8} = 4.5\ \text{J}\]
[B1]
Energy conservation from \(B\) to the natural-length position (all the elastic energy has gone):
\[4.5 = \tfrac12(0.5)v^2 + 0.5 \times 10 \times 0.6\]
[M1 A1]
\[0.25v^2 = 1.5 \quad\text{so}\quad v^2 = 6 \quad\text{and}\quad v = 2.45\ \mathrm{m\,s^{-1}}\]
[A1]

(c) From the natural-length position \(P\) moves freely under gravity (the string is slack), so it rises a further distance \(h\) given by
\[0 = 6 - 2(10)h\]
[M1]
\[h = 0.3\ \text{m}\]
[A1]
The greatest height above \(B\) is \(0.6 + 0.3 = 0.9\) m. [A1]
:::

:::warn Where marks are usually lost on a paper like this
- **Leaving out a term in the energy equation** (Questions 6 and 7). Write the three kinds of energy on separate lines: kinetic, gravitational and elastic. Elastic energy is \(\dfrac{\lambda x^2}{2l}\) with \(x\) the extension, not the length.
- **Measuring the radius of a horizontal circle along the string** (Question 4). The radius is \(L\sin\theta\), not \(L\), and the tension has to be resolved: its horizontal part provides the force towards the centre, its vertical part balances the weight.
- **Treating the collision of two spheres in one direction only** (Question 5). Only the components along the line of centres are changed by the impact. The components perpendicular to it stay as they were, so you must resolve before you use momentum and restitution, and combine afterwards.
- **Skipping the given result** (Questions 1, 2, 4 and 6). In a "show that" question the last line is the printed answer: the mark is for the line before it, so show the substitution and the step that leads to the result, not only the result.
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 5 | Force depending on position, \(v\,dv/dx\) | [Linear motion under a variable force](#math.fm.variable) |
| 2 | 7 | Trajectory equation, two angles, speed at a point | [Projectiles](#math.fm.projectiles) |
| 3 | 6 | Centre of mass of a cone on a cylinder, toppling on a slope | [Centres of mass](#math.fm.com) (and [Equilibrium of a rigid body](#math.fm.rigid)) |
| 4 | 7 | Elastic string as a conical pendulum | [Circular motion: horizontal circles](#math.fm.circular) (and [Hooke's law and elastic energy](#math.fm.elastic)) |
| 5 | 7 | Oblique impact of two spheres, then impact with a wall | [Oblique impact](#math.fm.oblique) (and [Direct impact and restitution](#math.fm.impulse)) |
| 6 | 9 | Leaving the outside of a sphere, then free fall | [Circular motion: vertical circles](#math.fm.vertical) |
| 7 | 9 | Elastic string, equilibrium, energy, slack string | [Hooke's law and elastic energy](#math.fm.elastic) |

Next: [Mock Paper 4: Further Probability and Statistics](#math.fm.mock.p4)
