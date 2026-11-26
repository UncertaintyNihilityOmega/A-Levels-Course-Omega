@chapter math.fm.mixed.applied
@title Mixed practice: Further Mechanics and Statistics
@level guide
@paper CAIE 9231 Papers 3 and 4
@time 5–7 hours
@summary Thirty-two short questions that mix every topic of Further Mechanics (Paper 3) and Further Probability and Statistics (Paper 4): projectiles, centres of mass, rigid bodies, elastic strings, horizontal and vertical circles, variable force, direct and oblique impact, then continuous random variables, t and normal tests, chi-squared tests, sign and Wilcoxon tests and probability generating functions. Each half goes from one star to three, and a final mixed set alternates mechanics and statistics. Each answer is a mark scheme, and each question names the chapter to revise.

:::why
In the exam you are not told which chapter a question comes from, and on these two papers the first step is nearly always the whole battle: is this a vertical circle or a projectile, a paired test or a two-sample test, a goodness-of-fit table or a contingency table? Practising one topic at a time trains the method but not that first decision. This page is mixed on purpose. No two neighbouring questions come from the same chapter, so each one starts with the real task: working out which tool to pick up. Mechanics comes first, statistics second, and the last four questions alternate between the two papers.
:::

:::tip How to use this page
Do the questions in order, a few at a time, on paper, and mark yourself with the scheme. Questions 1 to 14 are Further Mechanics (Paper 3), questions 15 to 28 are Further Probability and Statistics (Paper 4), and questions 29 to 32 alternate between the two. In each half the stars rise: ★ questions are one idea (3 to 5 marks), ★★ questions are one part of an exam question, ★★★ questions need two or more ideas in one answer and are the size of a real question (8 to 10 marks). When you lose a mark, follow the chapter link in brackets and redo one worked example there before moving on. MF19 is available for every question: it gives the trajectory equation, \(T = \lambda x/l\) and the elastic energy \(\lambda x^2/(2l)\), the acceleration \(r\omega^2\) or \(v^2/r\), the centres of mass of the standard solids, the pooled variance, the mean and variance from a probability generating function, and the normal, \(t\), \(\chi^2\) and Wilcoxon tables. It does not give \(v = r\omega\), the law of restitution, \(\sum (O - E)^2/E\), the \(t\)-test statistic or the sign-test rules, which you must know. Take \(g = 10\) in mechanics, and give non-exact answers to 3 significant figures and angles in degrees to 1 decimal place.
:::

:::try Further Mechanics warm-up ★
Q: [4 marks] (#math.fm.projectiles) ★ A particle is projected from a point on horizontal ground with speed \(20\ \mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal. Take \(g = 10\).

(a) Find the greatest height of the particle above the ground. [2]

(b) Find the horizontal distance from the point of projection to the point where the particle lands. [2]
A: (a) The vertical component of the initial velocity is \(20\sin30^\circ = 10\). At the greatest height the vertical velocity is zero, so
\[0 = 10^2 - 2(10)H\]
[M1]
\[H = 5\ \text{m}\]
[A1]

(b) The particle lands when it returns to the ground: \(0 = 10t - 5t^2\), so \(t = 2\) s. [M1]
The horizontal component is \(20\cos30^\circ\), so the range is
\[20\cos30^\circ \times 2 = 34.6\ \text{m}\]
[A1]
Q: [3 marks] (#math.fm.com) ★ A uniform lamina is L-shaped. It is made of a rectangle measuring 6 cm by 2 cm (the base) and a second rectangle 2 cm wide and 5 cm high standing on the base at its left-hand end, with the left edges in line. Find the distances of the centre of mass of the lamina from the left-hand edge and from the bottom edge.
A: Take the bottom left corner as the origin. The base has area \(12\) and its centre of mass is at \((3, 1)\); the upright part has area \(10\) and its centre of mass is at \((1, 4.5)\). The mass is proportional to the area. [M1]
\[22\bar x = 12(3) + 10(1) = 46 \quad\text{so}\quad \bar x = \frac{23}{11} = 2.09\ \text{cm}\]
[A1]
\[22\bar y = 12(1) + 10(4.5) = 57 \quad\text{so}\quad \bar y = \frac{57}{22} = 2.59\ \text{cm}\]
[A1]
Q: [3 marks] (#math.fm.variable) ★ A particle moves in a straight line. At time \(t\) seconds its velocity is \(v\ \mathrm{m\,s^{-1}}\) and its acceleration is \(-2v\). When \(t = 0\), \(v = 10\). Find \(v\) in terms of \(t\).
A: The acceleration is \(\dfrac{dv}{dt}\), so \(\dfrac{dv}{dt} = -2v\). Separate the variables:
\[\int \frac{1}{v}\,dv = \int -2\,dt\]
[M1]
\[\ln v = -2t + C\]
[A1]
When \(t = 0\), \(v = 10\), so \(C = \ln 10\), and
\[v = 10e^{-2t}\]
[A1]
Q: [3 marks] (#math.fm.elastic) ★ A light elastic string has natural length \(0.6\) m and modulus of elasticity \(18\) N. It is stretched to a length of \(0.9\) m. Find the tension in the string and the elastic energy stored in it.
A: The extension is \(0.9 - 0.6 = 0.3\) m, so
\[T = \frac{\lambda x}{l} = \frac{18 \times 0.3}{0.6} = 9\ \text{N}\]
[B1]
\[E = \frac{\lambda x^2}{2l} = \frac{18 \times 0.3^2}{2 \times 0.6}\]
[M1]
\[E = 1.35\ \text{J}\]
[A1]
Q: [3 marks] (#math.fm.circular) ★ A particle of mass \(0.4\) kg moves on a smooth horizontal table in a circle of radius \(0.5\) m, held by a light inextensible string fixed at the centre of the circle. The speed of the particle is \(3\ \mathrm{m\,s^{-1}}\). Find the angular speed and the tension in the string.
A: Angular speed \(\omega = \dfrac{v}{r} = \dfrac{3}{0.5} = 6\ \mathrm{rad\,s^{-1}}\). [B1]
The tension provides the force towards the centre:
\[T = \frac{mv^2}{r} = \frac{0.4 \times 9}{0.5}\]
[M1]
\[T = 7.2\ \text{N}\]
[A1]
:::

:::try Further Mechanics exam standard ★★
Q: [5 marks] (#math.fm.rigid) ★★ A uniform ladder \(AB\), of length \(5\) m and mass \(20\) kg, rests with its end \(A\) on rough horizontal ground and its end \(B\) against a smooth vertical wall. The foot \(A\) is \(3\) m from the wall, and \(B\) is \(4\) m above the ground. The ladder is in limiting equilibrium. Take \(g = 10\). Find the coefficient of friction between the ladder and the ground.
A: The forces are the weight \(200\) N at the midpoint, the reaction \(S\) of the wall (horizontal, since the wall is smooth), and the normal reaction \(R\) and friction \(F\) at \(A\). Take moments about \(A\). The weight acts \(1.5\) m horizontally from \(A\) and \(S\) acts at height \(4\) m:
\[4S = 200 \times 1.5\]
[M1]
\[S = 75\ \text{N}\]
[A1]
Resolve vertically and horizontally: \(R = 200\) and \(F = S = 75\). [B1]
In limiting equilibrium \(F = \mu R\): [M1]
\[\mu = \frac{75}{200} = 0.375\]
[A1]
Q: [4 marks] (#math.fm.vertical) ★★ A particle of mass \(0.5\) kg is attached to one end of a light inextensible string of length \(0.8\) m. The other end is attached to a fixed point \(O\). The particle is held with the string taut and horizontal and released from rest. Find the speed of the particle and the tension in the string when the particle is vertically below \(O\). Take \(g = 10\).
A: Energy conservation as the particle falls \(0.8\) m:
\[\tfrac12 v^2 = 10 \times 0.8\]
[M1]
\[v^2 = 16 \quad\text{so}\quad v = 4\ \mathrm{m\,s^{-1}}\]
[A1]
At the lowest point the resultant force towards \(O\) (upwards) provides the circular motion:
\[T - 0.5 \times 10 = \frac{0.5 \times 16}{0.8}\]
[M1]
\[T = 5 + 10 = 15\ \text{N}\]
[A1]
Q: [6 marks] (#math.fm.impulse) ★★ Two small smooth spheres \(A\) and \(B\), of masses \(2\) kg and \(3\) kg, lie on a smooth horizontal table. Sphere \(A\) is moving with speed \(6\ \mathrm{m\,s^{-1}}\) directly towards \(B\), which is at rest. The coefficient of restitution between the spheres is \(\tfrac12\).

(a) Find the speeds of \(A\) and \(B\) after the collision. [4]

(b) Find the loss in kinetic energy. [2]
A: (a) Let \(v_A\) and \(v_B\) be the velocities after impact, in the original direction of motion of \(A\). Conservation of momentum:
\[2(6) = 2v_A + 3v_B\]
[M1]
Newton's law of restitution:
\[v_B - v_A = \tfrac12 \times 6 = 3\]
[M1]
Substitute \(v_B = v_A + 3\): \(12 = 5v_A + 9\), so \(v_A = 0.6\) and \(v_B = 3.6\). [A1 A1]
Both spheres move in the original direction, with speeds \(0.6\) and \(3.6\ \mathrm{m\,s^{-1}}\).

(b) The kinetic energy before is \(\tfrac12(2)(36) = 36\) J and after is \(\tfrac12(2)(0.36) + \tfrac12(3)(12.96)\). [M1]
\[\text{loss} = 36 - 19.8 = 16.2\ \text{J}\]
[A1]
Q: [4 marks] (#math.fm.oblique) ★★ A small smooth ball moves on a smooth horizontal surface and strikes a fixed smooth vertical wall. Its speed just before the impact is \(10\ \mathrm{m\,s^{-1}}\) and its direction makes an angle of \(30^\circ\) with the wall. The coefficient of restitution between the ball and the wall is \(0.6\). Find the speed of the ball after the impact and the angle its path then makes with the wall.
A: Components before: along the wall \(10\cos30^\circ = 8.66\), perpendicular to the wall \(10\sin30^\circ = 5\). [B1]
The component along the wall is unchanged. The component perpendicular to the wall becomes \(0.6 \times 5 = 3\). [M1]
\[\text{speed} = \sqrt{8.66^2 + 3^2} = \sqrt{84} = 9.17\ \mathrm{m\,s^{-1}}\]
[A1]
\[\tan\phi = \frac{3}{8.66} \quad\text{so}\quad \phi = 19.1^\circ\]
[A1]
Q: [4 marks] (#math.fm.elastic) ★★ A particle of mass \(0.6\) kg lies on a smooth horizontal table and is attached to one end of a light elastic string of natural length \(0.5\) m and modulus of elasticity \(15\) N. The other end of the string is fixed to a point \(O\) on the table. The particle is held at a distance \(0.7\) m from \(O\), with the string taut, and released. Find the speed of the particle when the string becomes slack.
A: The extension at the start is \(0.2\) m, so the elastic energy is
\[\frac{\lambda x^2}{2l} = \frac{15 \times 0.2^2}{2 \times 0.5} = 0.6\ \text{J}\]
[B1]
When the string reaches its natural length all this energy has become kinetic energy:
\[\tfrac12(0.6)v^2 = 0.6\]
[M1 A1]
\[v^2 = 2 \quad\text{so}\quad v = 1.41\ \mathrm{m\,s^{-1}}\]
[A1]
:::

:::try Further Mechanics stretch ★★★
Q: [8 marks] (#math.fm.projectiles) ★★★ A particle is projected from a point \(P\) at the top of a vertical cliff, \(20\) m above the level sea, with speed \(25\ \mathrm{m\,s^{-1}}\) at an angle \(\theta\) above the horizontal, where \(\tan\theta = \tfrac34\). The particle moves freely under gravity in a vertical plane perpendicular to the cliff face and enters the sea at the point \(Q\). Take \(g = 10\).

(a) Find the time taken for the particle to reach the sea. [3]

(b) Find the horizontal distance of \(Q\) from the cliff. [1]

(c) Find the speed of the particle when it reaches \(Q\), and the angle its path makes with the horizontal. [4]
A: (a) \(\sin\theta = \tfrac35\) and \(\cos\theta = \tfrac45\), so the initial velocity has components \(20\) horizontally and \(15\) upwards. Vertical displacement \(-20\):
\[-20 = 15t - 5t^2\]
[M1]
\[t^2 - 3t - 4 = 0 \quad\text{so}\quad (t - 4)(t + 1) = 0\]
[A1]
\(t = 4\) s (the negative root is rejected). [A1]

(b) \(20 \times 4 = 80\) m. [B1]

(c) The vertical component at \(Q\) is \(15 - 10 \times 4 = -25\) (downwards). [B1]
\[\text{speed} = \sqrt{20^2 + 25^2} = \sqrt{1025}\]
[M1]
\[= 32.0\ \mathrm{m\,s^{-1}}\]
[A1]
\[\tan\phi = \frac{25}{20} \quad\text{so the path is}\quad 51.3^\circ\ \text{below the horizontal}\]
[A1]
Q: [8 marks] (#math.fm.com) ★★★ A uniform solid is made by joining a solid hemisphere of radius \(r\) to a solid cone of base radius \(r\) and height \(h\), so that their plane faces coincide. The hemisphere and the cone are made of the same material.

(a) Show that the distance of the centre of mass of the solid from the common plane face, measured into the cone, is \(\dfrac{h^2 - 3r^2}{4(2r + h)}\). [4]

The solid is placed with its curved hemispherical surface on a horizontal table. It rests in stable equilibrium whenever its centre of mass is below the centre of the common plane face.

(b) Find the greatest value of \(h\) for which this is so. [2]

(c) When \(h = r\), find the distance of the centre of mass from the vertex of the cone. [2]
A: (a) The volumes are proportional to the masses: hemisphere \(\tfrac23\pi r^3\), cone \(\tfrac13\pi r^2h\). [B1]
The centre of mass of the hemisphere is \(\tfrac38 r\) from the plane face on the side away from the cone, and that of the cone is \(\tfrac14 h\) from its base (MF19). [B1]
Take moments about the common plane face, measuring positive into the cone:
\[\left(\tfrac23 r^3 + \tfrac13 r^2h\right)\bar x = \tfrac13 r^2h \times \tfrac14 h - \tfrac23 r^3 \times \tfrac38 r\]
[M1]
\[\frac{r^2(2r + h)}{3}\,\bar x = \frac{r^2\left(h^2 - 3r^2\right)}{12} \quad\text{so}\quad \bar x = \frac{h^2 - 3r^2}{4(2r + h)}\]
[A1] (given result)

(b) The centre of mass is on the hemisphere's side of the plane face (or on it) when \(\bar x \le 0\). [M1]
\[h^2 \le 3r^2 \quad\text{so}\quad h \le \sqrt3\,r\]
The greatest value is \(h = \sqrt3\,r\). [A1]

(c) With \(h = r\): \(\bar x = \dfrac{r^2 - 3r^2}{4(3r)} = -\dfrac{r}{6}\), so the centre of mass is \(\tfrac16 r\) from the plane face, inside the hemisphere. [M1]
The vertex of the cone is a distance \(h = r\) from the plane face on the other side, so the distance from the vertex is
\[r + \tfrac16 r = \tfrac76 r\]
[A1]
Q: [9 marks] (#math.fm.circular) ★★★ A smooth hemispherical bowl of radius \(0.8\) m is fixed with its rim horizontal and uppermost. A particle \(P\) of mass \(0.3\) kg moves in a horizontal circle on the smooth inner surface of the bowl with constant angular speed \(\omega\ \mathrm{rad\,s^{-1}}\). The line joining \(P\) to the centre \(O\) of the bowl makes an angle \(\theta\) with the downward vertical. The normal reaction on \(P\) is \(R\). Take \(g = 10\).

(a) Show that \(R = m a\omega^2\), where \(m\) is the mass of \(P\) and \(a\) is the radius of the bowl. [3]

(b) Given that \(\omega = 5\), find \(\theta\). [2]

(c) Find the speed of \(P\). [2]

(d) Show that a horizontal circular motion of this kind is possible only if \(\omega\) is greater than a certain value, and find that value. [2]
A: (a) The reaction acts along \(PO\). Vertically, there is no acceleration:
\[R\cos\theta = mg\]
[M1]
The radius of the circle is \(a\sin\theta\), so horizontally
\[R\sin\theta = m\left(a\sin\theta\right)\omega^2\]
[M1]
Cancel \(\sin\theta\): \(R = ma\omega^2\). [A1] (given result)

(b) \(R = 0.3 \times 0.8 \times 25 = 6\) N, and \(\cos\theta = \dfrac{mg}{R} = \dfrac{3}{6}\). [M1]
\[\theta = 60.0^\circ\]
[A1]

(c) The radius of the circle is \(0.8\sin60^\circ = 0.693\) m. [M1]
\[v = r\omega = 0.693 \times 5 = 3.46\ \mathrm{m\,s^{-1}}\]
[A1]

(d) From (a), \(\cos\theta = \dfrac{mg}{ma\omega^2} = \dfrac{g}{a\omega^2}\). Since \(\cos\theta \le 1\), [M1]
\[\omega^2 \ge \frac{g}{a} = 12.5 \quad\text{so}\quad \omega \ge 3.54\ \mathrm{rad\,s^{-1}}\]
[A1] (at \(\omega^2 = g/a\) the particle is at the bottom of the bowl, \(\theta = 0\))
Q: [8 marks] (#math.fm.variable) ★★★ A boat of mass \(200\) kg is driven by an engine that exerts a constant force of \(400\) N. The resistance to the motion of the boat has magnitude \(20v\) newtons, where \(v\ \mathrm{m\,s^{-1}}\) is the speed of the boat. The boat starts from rest at \(t = 0\).

(a) Show that \(v = 20\left(1 - e^{-0.1t}\right)\). [4]

(b) State the speed that the boat approaches as \(t\) becomes large. [1]

(c) Find the distance the boat travels in the first \(10\) seconds. [3]
A: (a) Newton's second law:
\[200\frac{dv}{dt} = 400 - 20v \quad\text{so}\quad \frac{dv}{dt} = 0.1(20 - v)\]
[B1]
Separate the variables and integrate:
\[\int \frac{1}{20 - v}\,dv = \int 0.1\,dt\]
[M1]
\[-\ln(20 - v) = 0.1t + C\]
[A1]
When \(t = 0\), \(v = 0\), so \(C = -\ln 20\), and \(\ln\dfrac{20}{20 - v} = 0.1t\). Rearranging,
\[v = 20\left(1 - e^{-0.1t}\right)\]
[A1] (given result)

(b) As \(t \to \infty\), \(e^{-0.1t} \to 0\), so \(v \to 20\ \mathrm{m\,s^{-1}}\). [B1]

(c) Distance \(= \displaystyle\int_0^{10} 20\left(1 - e^{-0.1t}\right)dt\). [M1]
\[= \Big[20t + 200e^{-0.1t}\Big]_0^{10}\]
[A1]
\[= \left(200 + 200e^{-1}\right) - 200 = 200e^{-1} = 73.6\ \text{m}\]
[A1]
:::

:::try Further Statistics warm-up ★
Q: [4 marks] (#math.fm.crv) ★ The continuous random variable \(X\) has probability density function \(f(x) = kx^2\) for \(0 \le x \le 3\), and \(f(x) = 0\) otherwise.

(a) Find the value of \(k\). [2]

(b) Find \(\mathrm{E}(X)\). [2]
A: (a) The total probability is 1:
\[\int_0^3 kx^2\,dx = k\left[\frac{x^3}{3}\right]_0^3 = 9k = 1\]
[M1]
\[k = \tfrac19\]
[A1]

(b) \(\mathrm{E}(X) = \displaystyle\int_0^3 x \times \frac{x^2}{9}\,dx\). [M1]
\[= \frac19\left[\frac{x^4}{4}\right]_0^3 = \frac{81}{36} = \frac94\]
[A1]
Q: [5 marks] (#math.fm.inference) ★ A machine is supposed to fill bags with a mean mass of \(12.0\) kg of compost. The masses, in kg, of a random sample of six bags are \(12.1,\ 11.8,\ 12.6,\ 12.3,\ 11.9,\ 12.5\). Assuming that the masses are normally distributed, test at the 5% significance level whether the mean mass is greater than \(12.0\) kg.
A: Let \(\mu\) be the population mean mass in kg. \(H_0: \mu = 12.0\) and \(H_1: \mu > 12.0\). [B1]
The sample mean is \(\bar x = 12.2\) and \(\sum(x - \bar x)^2 = 0.52\), so
\[s^2 = \frac{0.52}{5} = 0.104 \qquad s = 0.3225\]
[M1]
\[t = \frac{12.2 - 12.0}{0.3225/\sqrt6} = 1.52\]
[A1]
For \(\nu = 5\), one-tailed at 5%, the critical value is \(2.015\). [B1]
\(1.52 < 2.015\), so do not reject \(H_0\). There is insufficient evidence, at the 5% level, that the mean mass of compost per bag is greater than \(12.0\) kg. [A1]
Q: [4 marks] (#math.fm.chisq) ★ A die is rolled 120 times and the numbers of 1, 2, 3, 4, 5 and 6 are \(15, 22, 18, 25, 17, 23\) respectively. Test, at the 5% significance level, whether the die is fair.
A: \(H_0\): the die is fair. \(H_1\): the die is not fair. The expected frequency for each score is \(120 \times \tfrac16 = 20\). [B1]
\[X^2 = \frac{(-5)^2 + 2^2 + (-2)^2 + 5^2 + (-3)^2 + 3^2}{20}\]
[M1]
\[X^2 = \frac{76}{20} = 3.8\]
[A1]
\(\nu = 6 - 1 = 5\) and the 5% critical value is \(11.070\). \(3.8 < 11.070\), so do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the die is biased. [A1]
Q: [4 marks] (#math.fm.nonpar) ★ A shopkeeper claims that the median daily takings are at least \(\pounds 400\). In a random sample of 10 days, 8 days had takings below \(\pounds 400\) and 2 days had takings above \(\pounds 400\). Carry out a sign test, at the 5% significance level, of the claim.
A: Let \(m\) be the population median daily takings. \(H_0: m = 400\) and \(H_1: m < 400\). [B1]
Under \(H_0\) the number of days below \(\pounds 400\) is \(S \sim \mathrm{B}(10, \tfrac12)\), and we observed \(S = 8\). [M1]
\[\mathrm{P}(S \ge 8) = \frac{45 + 10 + 1}{1024} = 0.0547\]
[A1]
\(0.0547 > 0.05\), so do not reject \(H_0\). There is insufficient evidence, at the 5% level, that the median daily takings are below \(\pounds 400\). [A1]
Q: [3 marks] (#math.fm.pgf) ★ The independent random variables \(X\) and \(Y\) have Poisson distributions with means \(2\) and \(3\). Use probability generating functions to show that \(X + Y\) has a Poisson distribution and find \(\mathrm{P}(X + Y = 2)\).
A: The generating functions are \(\mathrm{G}_X(t) = e^{2(t - 1)}\) and \(\mathrm{G}_Y(t) = e^{3(t - 1)}\), and for independent variables the generating function of the sum is the product: [M1]
\[\mathrm{G}_{X+Y}(t) = e^{2(t - 1)}e^{3(t - 1)} = e^{5(t - 1)}\]
[A1]
This is the generating function of \(\mathrm{Po}(5)\), so \(X + Y \sim \mathrm{Po}(5)\) and
\[\mathrm{P}(X + Y = 2) = e^{-5}\frac{5^2}{2!} = 0.0842\]
[A1]
:::

:::try Further Statistics exam standard ★★
Q: [6 marks] (#math.fm.twosample) ★★ Eight athletes each run a timed sprint before and after a training course. The reductions in time, in seconds (time before minus time after), are \(2.1,\ 3.4,\ -0.5,\ 1.8,\ 2.9,\ 0.7,\ 3.3,\ 1.5\). Assuming that the reductions are a random sample from a normal distribution, test at the 5% significance level whether the course reduces the mean time.
A: Let \(\mu_d\) be the population mean reduction in time, in seconds. \(H_0: \mu_d = 0\) and \(H_1: \mu_d > 0\). [B1]
\(\sum d = 15.2\) and \(\sum d^2 = 41.5\), so
\[\bar d = 1.9 \qquad s^2 = \frac{41.5 - 15.2^2/8}{7} = 1.803\]
[M1]
\[t = \frac{\bar d}{s/\sqrt n} = \frac{1.9}{1.3427/\sqrt8}\]
[M1]
\[t = 4.00\]
[A1]
For \(\nu = 7\), one-tailed at 5%, the critical value is \(1.895\). [B1]
\(4.00 > 1.895\), so reject \(H_0\). There is sufficient evidence, at the 5% level, that the course reduces the mean sprint time. [A1]
Q: [5 marks] (#math.fm.contingency) ★★ A survey asks 100 men and 100 women which of three brands, \(A\), \(B\) and \(C\), they prefer. The numbers are given below.

| | \(A\) | \(B\) | \(C\) |
|---|---|---|---|
| Men | 30 | 45 | 25 |
| Women | 50 | 30 | 20 |

Test, at the 5% significance level, whether brand preference is independent of gender.
A: \(H_0\): brand preference is independent of gender. \(H_1\): brand preference and gender are associated. [B1]
Expected frequency \(=\dfrac{\text{row total} \times \text{column total}}{200}\). The column totals are \(80, 75, 45\) and both rows total \(100\), so the expected frequencies are \(40, 37.5, 22.5\) in each row, all at least 5. [M1]
\[X^2 = 2\left[\frac{10^2}{40} + \frac{7.5^2}{37.5} + \frac{2.5^2}{22.5}\right]\]
[M1]
\[X^2 = 2(2.5 + 1.5 + 0.2778) = 8.56\]
[A1]
\(\nu = (2 - 1)(3 - 1) = 2\) and the 5% critical value is \(5.991\). \(8.56 > 5.991\), so reject \(H_0\). There is sufficient evidence, at the 5% level, of an association between brand preference and gender. [A1]
Q: [5 marks] (#math.fm.wilcoxon) ★★ The times, in seconds, taken by two machines to produce a component are recorded. Machine \(X\) (5 components): \(12, 15, 9, 18, 11\). Machine \(Y\) (6 components): \(20, 17, 22, 14, 25, 19\). Use a Wilcoxon rank-sum test, at the 5% significance level, to test whether the median times differ.
A: \(H_0\): the two populations of times are identical. \(H_1\): they are not (the medians differ). [B1]
Rank all 11 times together (9 is rank 1, 11 is rank 2, 12 is rank 3, 14 is rank 4, 15 is rank 5, and so on). The ranks of machine \(X\), the smaller sample (\(m = 5\), \(n = 6\)), are \(1, 2, 3, 5, 7\). [M1]
\(R_m = 18\), and \(m(m + n + 1) - R_m = 60 - 18 = 42\), so \(W = \min(18, 42) = 18\). [A1]
For \(m = 5\), \(n = 6\), two-tailed at 5%, MF19 gives \(18\). [B1]
\(18 \le 18\), so reject \(H_0\). There is sufficient evidence, at the 5% level, that the median times of the two machines differ. [A1]
Q: [5 marks] (#math.fm.crv) ★★ The continuous random variable \(X\) has cumulative distribution function \(\mathrm{F}(x) = \dfrac{x^3 + x}{10}\) for \(0 \le x \le 2\), with \(\mathrm{F}(x) = 0\) for \(x < 0\) and \(\mathrm{F}(x) = 1\) for \(x > 2\).

(a) Find the probability density function of \(X\). [2]

(b) Find \(\mathrm{P}(X > 1.5)\). [2]

(c) Verify that \(\mathrm{F}\) is a valid cumulative distribution function on \([0, 2]\). [1]
A: (a) Differentiate: \(f(x) = \mathrm{F}'(x)\) [M1]
\[f(x) = \frac{3x^2 + 1}{10}\quad\text{for } 0 \le x \le 2\text{, and 0 otherwise}\]
[A1]

(b) \(\mathrm{P}(X > 1.5) = 1 - \mathrm{F}(1.5)\) [M1]
\[= 1 - \frac{3.375 + 1.5}{10} = 0.5125\]
[A1]

(c) \(\mathrm{F}(0) = 0\), \(\mathrm{F}(2) = \tfrac{8 + 2}{10} = 1\), and \(f(x) > 0\) throughout, so \(\mathrm{F}\) increases from 0 to 1. [B1]
Q: [5 marks] (#math.fm.inference) ★★ A random sample of 9 observations from a normal population has mean \(52.4\) and unbiased estimate of the population standard deviation \(s = 3.6\). Find a 95% confidence interval for the population mean, and state an assumption you have made.
A: There are \(\nu = 8\) degrees of freedom, and the 97.5% point of the \(t\)-distribution is \(2.306\). [B1]
The standard error is \(\dfrac{s}{\sqrt n} = \dfrac{3.6}{3} = 1.2\). [M1]
\[52.4 \pm 2.306 \times 1.2 = 52.4 \pm 2.767\]
[A1]
The interval is \((49.6,\ 55.2)\). [A1]
The population is assumed to be normally distributed. [B1]
:::

:::try Further Statistics stretch ★★★
Q: [9 marks] (#math.fm.pgf) ★★★ The discrete random variable \(X\) has probability generating function \(\mathrm{G}(t) = \dfrac{1 + t}{4 - 2t}\), for \(|t| < 2\).

(a) Find \(\mathrm{E}(X)\). [3]

(b) Find \(\mathrm{Var}(X)\). [4]

(c) Expand \(\mathrm{G}(t)\) in ascending powers of \(t\) as far as \(t^2\), and write down \(\mathrm{P}(X = 0)\) and \(\mathrm{P}(X = 2)\). [2]
A: (a) By the quotient rule
\[\mathrm{G}'(t) = \frac{(4 - 2t) + 2(1 + t)}{(4 - 2t)^2}\]
[M1]
\[\mathrm{G}'(t) = \frac{6}{(4 - 2t)^2}\]
[A1]
\[\mathrm{E}(X) = \mathrm{G}'(1) = \frac64 = \frac32\]
[A1]

(b) Differentiate again:
\[\mathrm{G}''(t) = \frac{24}{(4 - 2t)^3}\]
[M1]
\[\mathrm{G}''(1) = \frac{24}{8} = 3\]
[A1]
\[\mathrm{Var}(X) = \mathrm{G}''(1) + \mathrm{G}'(1) - \left[\mathrm{G}'(1)\right]^2\]
[M1]
\[= 3 + \frac32 - \frac94 = \frac94\]
[A1]

(c) \(\mathrm{G}(t) = \dfrac14(1 + t)\left(1 - \dfrac t2\right)^{-1} = \dfrac14(1 + t)\left(1 + \dfrac t2 + \dfrac{t^2}{4} + \cdots\right)\). [M1]
\[\mathrm{G}(t) = \frac14\left(1 + \frac32 t + \frac34 t^2 + \cdots\right)\]
so \(\mathrm{P}(X = 0) = \tfrac14\) and \(\mathrm{P}(X = 2) = \tfrac{3}{16}\). [A1]
Q: [8 marks] (#math.fm.chisq) ★★★ The numbers of faults in 80 lengths of cable, each 100 m long, are summarised in the table. The mean number of faults per length in the sample is \(1.7\), and it is suggested that the number of faults per length has a Poisson distribution with this mean.

| Faults | 0 | 1 | 2 | 3 | 4 or more |
|---|---|---|---|---|---|
| Observed frequency | 12 | 26 | 24 | 12 | 6 |
| Expected frequency | 14.61 | 24.84 | | | |

(a) Calculate the expected frequencies for 2, 3 and 4 or more faults. [3]

(b) Carry out a goodness-of-fit test, at the 5% significance level, of the suggestion. [5]
A: (a) For \(\mathrm{Po}(1.7)\): \(80\,\mathrm{P}(X = 2) = 80 \times e^{-1.7}\dfrac{1.7^2}{2!} = 21.12\). [M1]
\(80\,\mathrm{P}(X = 3) = 80 \times e^{-1.7}\dfrac{1.7^3}{3!} = 11.97\). [A1]
The expected frequency for 4 or more is the remainder: \(80 - 14.61 - 24.84 - 21.12 - 11.97 = 7.46\). [A1] (7.45 or 7.46 allowed, from the rounding)

(b) \(H_0\): the number of faults per length has a Poisson distribution with mean \(1.7\). \(H_1\): it does not. [B1]
Every expected frequency is at least 5, so no classes need combining:
\[X^2 = \frac{(12 - 14.61)^2}{14.61} + \frac{(26 - 24.84)^2}{24.84} + \cdots + \frac{(6 - 7.46)^2}{7.46}\]
[M1]
\[X^2 = 0.468 + 0.054 + 0.393 + 0.000 + 0.284 = 1.20\]
[A1]
There are 5 classes. The mean was estimated from the data, so \(\nu = 5 - 1 - 1 = 3\), and the 5% critical value is \(7.815\). [B1]
\(1.20 < 7.815\), so do not reject \(H_0\). There is insufficient evidence, at the 5% level, that a Poisson distribution with mean \(1.7\) is not a suitable model for the number of faults per length. [A1]
Q: [9 marks] (#math.fm.inference) ★★★ The masses, in grams, of a random sample of 10 apples from an orchard are summarised by \(\sum x = 520\) and \(\sum x^2 = 27148\). The masses are assumed to be normally distributed. The grower claims that the mean mass is \(50\) g.

(a) Calculate the sample mean and an unbiased estimate of the population variance. [2]

(b) Test the grower's claim at the 5% significance level, against the alternative that the mean mass is different from \(50\) g. [5]

(c) Find a 95% confidence interval for the population mean mass, and explain how it agrees with your conclusion in (b). [2]
A: (a) \(\bar x = 52\) and \(\sum(x - \bar x)^2 = 27148 - \dfrac{520^2}{10} = 108\). [M1]
\[s^2 = \frac{108}{9} = 12\]
[A1]

(b) Let \(\mu\) be the population mean mass in grams. \(H_0: \mu = 50\) and \(H_1: \mu \ne 50\). [B1]
\[t = \frac{52 - 50}{\sqrt{12}/\sqrt{10}}\]
[M1]
\[t = 1.83\]
[A1]
For \(\nu = 9\), two-tailed at 5%, the critical value is \(\pm2.262\). [B1]
\(1.83 < 2.262\), so do not reject \(H_0\). There is insufficient evidence, at the 5% level, that the mean mass differs from \(50\) g. [A1]

(c) \(52 \pm 2.262 \times \dfrac{\sqrt{12}}{\sqrt{10}} = 52 \pm 2.478\). [M1]
The interval is \((49.5,\ 54.5)\). It contains 50, which agrees with not rejecting \(H_0\) in a two-tailed 5% test. [A1]
Q: [9 marks] (#math.fm.wilcoxon) ★★★ A researcher measures the resting heart rate of 30 volunteers before and after a month of regular exercise. The differences (before minus after) are all non-zero, and are assumed to come from a symmetrical distribution. The ranks of the absolute differences are found. The sum of the ranks of the positive differences is \(140\), and the sum of the ranks of the negative differences is \(325\).

(a) State the mean and the variance of the sum of the ranks of the positive differences when there is no change in the population median. [3]

(b) Use a normal approximation to test, at the 5% significance level, whether the exercise changes the median resting heart rate. [5]

(c) State the assumption about the differences that must hold for this Wilcoxon test to be valid. [1]
A: (a) With \(n = 30\), the sum of the ranks of the positive differences has mean and variance
\[\frac{n(n + 1)}{4} \quad\text{and}\quad \frac{n(n + 1)(2n + 1)}{24}\]
[M1]
\[\text{mean} = \frac{30 \times 31}{4} = 232.5\]
[A1]
\[\text{variance} = \frac{30 \times 31 \times 61}{24} = 2363.75\]
[A1]

(b) Let \(m\) be the population median of the differences. \(H_0: m = 0\) and \(H_1: m \ne 0\). [B1]
\(T = \min(140, 325) = 140\), in the lower tail. Use a continuity correction, because the ranks are whole numbers:
\[z = \frac{140.5 - 232.5}{\sqrt{2363.75}}\]
[M1]
\[z = \frac{-92}{48.62} = -1.89\]
[A1]
The test is two-tailed at 5%, so the critical values are \(\pm1.960\). [M1]
\(-1.89 > -1.960\), so do not reject \(H_0\). There is insufficient evidence, at the 5% level, that the exercise changes the median resting heart rate. [A1]

(c) The population of differences must be symmetrical about its median. [B1] (the sign test needs no such assumption, but it ignores the sizes of the differences)
:::

:::try Mixed set: mechanics and statistics together ★★★
Q: [9 marks] (#math.fm.elastic) ★★★ A particle \(P\) of mass \(0.8\) kg lies on a smooth plane inclined at \(30^\circ\) to the horizontal. It is attached to one end of a light elastic string of natural length \(1\) m and modulus of elasticity \(24\) N. The other end of the string is attached to a fixed point \(O\) at the top of the plane, and the string lies along a line of greatest slope. The particle is released from rest at \(O\) and slides down the plane. Take \(g = 10\).

(a) Find the speed of \(P\) when the string first becomes taut. [2]

(b) Find the greatest extension of the string. [4]

(c) Find the greatest speed of \(P\). [3]
A: (a) Until the string is taut \(P\) falls freely down the slope, a distance \(1\) m. The component of the weight down the slope is \(0.8 \times 10 \times \sin30^\circ = 4\) N, so
\[\tfrac12(0.8)v^2 = 4 \times 1\]
[M1]
\[v^2 = 10 \quad\text{so}\quad v = 3.16\ \mathrm{m\,s^{-1}}\]
[A1]

(b) At the greatest extension \(x\), \(P\) is instantaneously at rest and has moved \(1 + x\) down the slope. The elastic energy is \(\dfrac{24x^2}{2 \times 1} = 12x^2\). [B1]
Energy conservation from \(O\):
\[4(1 + x) = 12x^2\]
[M1 A1]
\[3x^2 - x - 1 = 0 \quad\text{so}\quad x = \frac{1 + \sqrt{13}}{6}\]
[A1] (the positive root; \(x = 0.768\) m)

(c) The speed is greatest when the acceleration is zero: tension \(=\) component of weight, \(\dfrac{24e}{1} = 4\), so \(e = \tfrac16\) m. [M1]
Energy conservation from \(O\) to this position:
\[4\left(1 + \tfrac16\right) = \tfrac12(0.8)v^2 + 12\left(\tfrac16\right)^2\]
[M1]
\[0.4v^2 = 4.667 - 0.333 \quad\text{so}\quad v^2 = 10.83 \quad\text{and}\quad v = 3.29\ \mathrm{m\,s^{-1}}\]
[A1]
Q: [8 marks] (#math.fm.contingency) ★★★ A survey asks 128 people from towns and villages how they usually travel to work. The results are shown below.

| | Rail | Bus | Cycle |
|---|---|---|---|
| Town | 50 | 24 | 4 |
| Village | 20 | 28 | 2 |

(a) Carry out a test, at the 5% significance level, of whether the method of travel is independent of where the person lives. [7]

(b) Which cell of your final table contributes most to the test statistic, and what does it show? [1]
A: (a) \(H_0\): the method of travel is independent of where the person lives. \(H_1\): the method of travel and the place of residence are associated. [B1]
The row totals are \(78\) and \(50\), and the column totals are \(70, 52, 6\). Expected frequency \(= \dfrac{\text{row} \times \text{column}}{128}\): the cycle column gives \(3.66\) and \(2.34\), both less than 5. [M1]
Combine the bus and cycle columns (they are similar kinds of travel, and each expected frequency is then at least 5). [B1]

| | Rail | Bus or cycle |
|---|---|---|
| Town: observed, expected | 50, 42.66 | 28, 35.34 |
| Village: observed, expected | 20, 27.34 | 30, 22.66 |

\[X^2 = 1.264 + 1.526 + 1.972 + 2.380\]
[M1]
\[X^2 = 7.14\]
[A1]
There are now 2 rows and 2 columns, so \(\nu = (2 - 1)(2 - 1) = 1\), and the 5% critical value is \(3.841\). [B1]
\(7.14 > 3.841\), so reject \(H_0\). There is sufficient evidence, at the 5% level, of an association between the method of travel to work and where the person lives. [A1]

(b) The village people using a bus or a bicycle contribute \(2.380\), the largest: more village workers use a bus or cycle (30) than the 22.66 expected if the method of travel were independent of where they live. [B1]
Q: [10 marks] (#math.fm.vertical) ★★★ A particle \(P\) of mass \(m\) moves on the smooth inner surface of a fixed hollow sphere of centre \(O\) and radius \(a\). It is projected horizontally from the lowest point \(A\) with speed \(\sqrt{3ag}\). When \(OP\) makes an angle \(\theta\) with the downward vertical, the normal reaction on \(P\) is \(R\).

(a) Show that \(R = mg\left(1 + 3\cos\theta\right)\). [4]

(b) Show that \(P\) leaves the surface where \(\cos\theta = -\tfrac13\), and find the speed of \(P\) there. [3]

(c) Find the greatest height above \(A\) reached by \(P\) in the subsequent motion. [3]
A: (a) The height of \(P\) above \(A\) is \(a(1 - \cos\theta)\). Energy conservation:
\[\tfrac12 mv^2 = \tfrac12 m(3ag) - mga(1 - \cos\theta)\]
[M1]
\[v^2 = 3ag - 2ag(1 - \cos\theta) = ag(1 + 2\cos\theta)\]
[A1]
Resolve towards \(O\) (the component of the weight towards \(O\) is \(-mg\cos\theta\)):
\[R - mg\cos\theta = \frac{mv^2}{a}\]
[M1]
\[R = mg\cos\theta + mg(1 + 2\cos\theta) = mg(1 + 3\cos\theta)\]
[A1] (given result)

(b) \(P\) leaves the surface when \(R = 0\): \(1 + 3\cos\theta = 0\), so [M1]
\[\cos\theta = -\tfrac13\]
[A1] (this is above the level of \(O\), where \(P\) can leave the surface)
\[v^2 = ag\left(1 - \tfrac23\right) = \tfrac13 ag \quad\text{so}\quad v = \sqrt{\tfrac{ag}{3}}\]
[A1]

(c) \(P\) leaves with velocity along the tangent, perpendicular to \(OP\). Here \(\sin\theta = \tfrac{2\sqrt2}{3}\), and the tangent makes an angle with the horizontal whose sine is \(\tfrac{2\sqrt2}{3}\) (the same angle as \(OP\) makes with the vertical), so the upward component of the velocity is
\[v_y = v \times \frac{2\sqrt2}{3} \quad\text{and}\quad v_y^2 = \frac{ag}{3} \times \frac89 = \frac{8ag}{27}\]
[B1]
After leaving, \(P\) rises a further distance
\[\frac{v_y^2}{2g} = \frac{4a}{27}\]
[M1]
The height of the leaving point above \(A\) is \(a(1 - \cos\theta) = \tfrac43 a\), so the greatest height above \(A\) is
\[\frac43 a + \frac{4a}{27} = \frac{40a}{27}\]
[A1]
Q: [9 marks] (#math.fm.crv) ★★★ The continuous random variable \(X\) has probability density function \(f(x) = \dfrac{k}{x^2}\) for \(1 \le x \le 4\), and \(f(x) = 0\) otherwise.

(a) Show that \(k = \tfrac43\). [2]

(b) Find the cumulative distribution function of \(X\). [2]

(c) Find the median of \(X\). [2]

The random variable \(Y\) is defined by \(Y = \ln X\).

(d) Find the cumulative distribution function and the probability density function of \(Y\). [3]
A: (a) \(\displaystyle\int_1^4 \frac{k}{x^2}\,dx = k\left[-\frac1x\right]_1^4 = \frac{3k}{4}\). [M1]
This equals 1, so \(k = \tfrac43\). [A1]

(b) For \(1 \le x \le 4\):
\[\mathrm{F}(x) = \int_1^x \frac{4}{3t^2}\,dt = \frac43\left(1 - \frac1x\right)\]
[M1]
with \(\mathrm{F}(x) = 0\) for \(x < 1\) and \(\mathrm{F}(x) = 1\) for \(x > 4\). [A1]

(c) \(\mathrm{F}(m) = \tfrac12\): \(1 - \dfrac1m = \dfrac38\). [M1]
\[m = \frac85 = 1.6\]
[A1]

(d) For \(0 \le y \le \ln4\): \(\mathrm{G}(y) = \mathrm{P}(\ln X \le y) = \mathrm{P}\left(X \le e^y\right) = \mathrm{F}\left(e^y\right)\). [M1]
\[\mathrm{G}(y) = \frac43\left(1 - e^{-y}\right)\]
[A1]
\[g(y) = \mathrm{G}'(y) = \frac43 e^{-y} \quad\text{for } 0 \le y \le \ln4\]
[A1]
:::

## Where the questions come from

| Chapter | Questions |
|---|---|
| [Projectiles](#math.fm.projectiles) | 1, 11 |
| [Centres of mass](#math.fm.com) | 2, 12 |
| [Equilibrium of a rigid body](#math.fm.rigid) | 6 |
| [Hooke's law and elastic energy](#math.fm.elastic) | 4, 10, 29 |
| [Circular motion: horizontal circles](#math.fm.circular) | 5, 13 |
| [Circular motion: vertical circles](#math.fm.vertical) | 7, 31 |
| [Linear motion under a variable force](#math.fm.variable) | 3, 14 |
| [Direct impact and restitution](#math.fm.impulse) | 8 |
| [Oblique impact](#math.fm.oblique) | 9 |
| [Continuous random variables](#math.fm.crv) | 15, 23, 32 |
| [The t-distribution: one-sample tests and intervals](#math.fm.inference) | 16, 24, 27 |
| [Comparing two means](#math.fm.twosample) | 20 |
| [Chi-squared goodness of fit](#math.fm.chisq) | 17, 26 |
| [Chi-squared tests for independence](#math.fm.contingency) | 21, 30 |
| [Non-parametric tests: the sign test](#math.fm.nonpar) | 18 |
| [Wilcoxon tests](#math.fm.wilcoxon) | 22, 28 |
| [Probability generating functions](#math.fm.pgf) | 19, 25 |

:::recap
- Mixed practice trains the first step: read the question, name the chapter, then choose the method. Do a few questions at a time and keep a list of the chapters you had to look up.
- In mechanics, decide the principle before the algebra: energy (a change in height or extension, no time asked), Newton's second law (a force, a tension or a reaction asked), momentum and restitution (a collision), or calculus (a force that depends on speed or position).
- In statistics, decide the test before the numbers: one sample, paired, two independent samples, a table of counts, or a median; then write the hypotheses, the statistic, the critical value and a conclusion in context.
- Every lost mark has a name: a method mark you did not show, an accuracy mark lost in the arithmetic, or a given result you did not reach honestly. Write the name next to the question and fix that habit first.
- When the questions feel easy, sit [Mock Paper 3](#math.fm.mock.p3) and [Mock Paper 4](#math.fm.mock.p4) under exam conditions.
:::

Next: [Mock Paper 1: Further Pure Mathematics 1](#math.fm.mock.p1)
