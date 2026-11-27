@chapter math.fm.variable
@title Linear motion under a variable force
@level fm
@paper CAIE 9231 Paper 3
@time 5–6 hours
@summary When the force on a particle changes with time, position or speed, the acceleration is not constant and the equations of motion for constant acceleration fail. You will write Newton's second law as a differential equation, choose between \(\dfrac{dv}{dt}\) and \(v\dfrac{dv}{dx}\), solve it by separating the variables, and use the answer to find speeds, distances, times, terminal speeds and escape conditions.

:::why
A parachutist, a car braking against air resistance, a spacecraft leaving a planet and a boat gliding to a halt all feel forces that change as they move. The constant acceleration formulas cannot describe any of them. A differential equation can: Newton's second law says the acceleration is the force divided by the mass, and if you know how the force depends on time, position or speed, you can integrate your way to the motion. The same method gives the limit a body approaches (its terminal speed) and whether a rocket ever comes back.
:::

**Before you start**, you need Newton's second law from [Newton's laws of motion](#math.m.newton), the link between velocity and acceleration from [Kinematics: describing motion](#math.m.kinematics), power as force times speed from [Work, energy and power](#math.m.energy), and separable differential equations from [Differential equations](#math.p3.diffeq). The integrals use partial fractions ([Partial fractions](#math.p3.partial)) and integration by parts ([Integration techniques](#math.p3.inttech)). You may also use [Hyperbolic functions](#math.fm.hyperbolic) once, to name a result.

:::try Warm-up
Q: Solve \(\dfrac{dy}{dx} = 3y\), given that \(y = 2\) when \(x = 0\). (from [Differential equations](#math.p3.diffeq))
A: Separate: \(\displaystyle\int \frac{dy}{y} = \int 3\,dx\), so \(\ln y = 3x + c\). Then \(y = Ae^{3x}\), and \(y = 2\) at \(x = 0\) gives \(A = 2\): \(y = 2e^{3x}\).
Q: A 4 kg particle is acted on by a resultant force of 10 N in a straight line. Find its acceleration. (from [Newton's laws of motion](#math.m.newton))
A: \(F = ma\), so \(a = \dfrac{10}{4} = 2.5\,\mathrm{m\,s^{-2}}\).
Q: Express \(\dfrac{1}{9 - v^2}\) in partial fractions. (from [Partial fractions](#math.p3.partial))
A: \(9 - v^2 = (3 - v)(3 + v)\), and \(\dfrac{1}{9 - v^2} = \dfrac{1}{6}\left(\dfrac{1}{3 - v} + \dfrac{1}{3 + v}\right)\).
:::

## Newton's second law when the force varies

With constant forces you used \(F = ma\) and the four constant-acceleration equations ([Kinematics: describing motion](#math.m.kinematics)). Now the force depends on something that changes, so \(a\) changes too. The law \(F = ma\) still holds at every instant; what changes is that you can no longer solve it with algebra alone. You write \(a\) as a derivative and the law becomes a differential equation.

:::def Variable force
A force whose magnitude is not constant, because it depends on the time \(t\), on the particle's position \(x\), or on its speed \(v\). Examples: a force \(6t\) that grows as time passes, the gravitational pull \(\dfrac{k}{x^2}\) that weakens with distance, and air resistance \(kv^2\) that grows with speed.
:::

The particle moves in a straight line, so we measure its position \(x\) from a fixed point \(O\) and take one direction as positive. The velocity \(v\) and the acceleration \(a\) are then signed numbers, and a force pointing in the negative direction is negative.

There are three ways to write the acceleration. The first two are familiar; the third is the one that makes position problems solvable.

:::key Three forms of the acceleration
For motion in a straight line with position \(x\), velocity \(v\) and time \(t\),
\[a = \frac{dv}{dt} = \frac{d^2x}{dt^2} = v\,\frac{dv}{dx}\]
Newton's second law is then \(m\dfrac{dv}{dt} = F\) or \(mv\dfrac{dv}{dx} = F\), where \(F\) is the resultant force in the positive direction. Which form you use depends on what \(F\) is written in terms of (next section).
:::

The third form is not on MF19, so you must be able to derive it. It is a short chain-rule argument, and it is asked for as a "show that" in 9231.

:::eg (Exam style) A particle moves in a straight line with velocity \(v\) at position \(x\). Show that its acceleration is \(a = v\dfrac{dv}{dx}\).
By definition, acceleration is the rate of change of velocity, \(a = \dfrac{dv}{dt}\). Velocity is a function of position, and position is a function of time, so the chain rule gives
\[\frac{dv}{dt} = \frac{dv}{dx} \times \frac{dx}{dt}\] [M1]
Velocity is the rate of change of position, \(\dfrac{dx}{dt} = v\). [B1]
\[\text{So } a = \frac{dv}{dx} \times v = v\frac{dv}{dx}\] [A1]
:::

A second way to see it: \(\dfrac{d}{dx}\left(\tfrac12 v^2\right) = v\dfrac{dv}{dx}\), so \(v\dfrac{dv}{dx}\) is "the rate of change of kinetic energy per unit mass with distance". That is why integrating \(mv\dfrac{dv}{dx} = F\) with respect to \(x\) gives the work–energy equation.

:::proof Why \(mv\dfrac{dv}{dx} = F\) gives the work–energy equation
Start from Newton's second law in the \(x\) form:
\[mv\frac{dv}{dx} = F(x)\]
Integrate both sides with respect to \(x\) from \(x_1\) (speed \(u\)) to \(x_2\) (speed \(v\)).
\[\int_{x_1}^{x_2} mv\frac{dv}{dx}\,dx = \int_{x_1}^{x_2} F(x)\,dx\]
On the left, \(\dfrac{dv}{dx}\,dx = dv\), so the integral changes variable from \(x\) to \(v\):
\[\int_u^v mv\,dv = \left[\tfrac12 mv^2\right]_u^v = \tfrac12 mv^2 - \tfrac12 mu^2\]
The right side is the work done by the force, so the change in kinetic energy equals the work done: \(\tfrac12 mv^2 - \tfrac12 mu^2 = \int F\,dx\). When the force is constant this is the familiar \(F \times\) distance.
:::

So for a force that depends on \(x\) you may use either \(v\dfrac{dv}{dx}\) or the integral of the work. Examiners expect the differential equation, and it is the only method that carries on to the time \(t\).

## Choosing the form of the acceleration

The skill in this chapter is choosing the form that matches the variables in the question. The rule is: **write the acceleration so that the variable the force depends on is the one you integrate with respect to.**

| The force is given in terms of | Write \(a\) as | Separate to get | You then find |
|---|---|---|---|
| time \(t\) | \(\dfrac{dv}{dt}\) | \(\displaystyle\int dv = \int \frac{F}{m}\,dt\) | \(v\) in terms of \(t\); integrate again for \(x\) |
| position \(x\) | \(v\dfrac{dv}{dx}\) | \(\displaystyle\int v\,dv = \int \frac{F}{m}\,dx\) | \(v\) in terms of \(x\); then \(\dfrac{dx}{dt} = v\) for \(t\) |
| speed \(v\), asked for time | \(\dfrac{dv}{dt}\) | \(\displaystyle\int \frac{m}{F}\,dv = \int dt\) | \(t\) in terms of \(v\) |
| speed \(v\), asked for distance | \(v\dfrac{dv}{dx}\) | \(\displaystyle\int \frac{mv}{F}\,dv = \int dx\) | \(x\) in terms of \(v\) |

:::steps
1. Choose the positive direction, and draw the particle with the forces on it. Mark the velocity in the positive direction.
2. Write the resultant force in the positive direction, with signs: a resistance is negative when \(v > 0\), a force towards \(O\) is negative when \(x > 0\).
3. Write Newton's second law \(F = ma\) with the form of \(a\) from the table.
4. Separate the variables, and integrate both sides. Put the constant of integration on one side.
5. Use the initial conditions (usually "at \(x = x_0\), \(v = v_0\)" or "when \(t = 0\), \(v = 0\)") to find the constant, before you do anything else with the result.
6. Answer the question in context, with units, to three significant figures unless it is exact.
:::

:::warn Do not integrate \(v\dfrac{dv}{dx}\) as if it were \(\dfrac{dv}{dx}\)
The most common error is to write \(m\dfrac{dv}{dx} = F\). That drops the factor \(v\): \(\dfrac{dv}{dx}\) is not the acceleration. If the force depends on \(x\), write \(mv\dfrac{dv}{dx} = F\), integrate \(v\) with respect to \(v\) to get \(\tfrac12 v^2\), and remember the \(\tfrac12\). Also keep the mass: divide both sides by \(m\) only once, and divide every term.
:::

## Force depending on time

When the force is a function of \(t\), use \(a = \dfrac{dv}{dt}\). Integrate once for the velocity and again for the position. The two constants of integration come from the starting conditions.

:::eg A particle of mass 3 kg starts from rest at the point \(O\) on a smooth horizontal line. A force of \((36 - 6t)\) N acts on it in the positive direction, where \(t\) is the time in seconds. Find (a) the velocity at time \(t\), (b) the greatest speed, (c) the time at which it comes to rest again, and the distance it has then travelled.
Apply \(F = ma\) with \(a = \dfrac{dv}{dt}\):
\[3\frac{dv}{dt} = 36 - 6t, \quad\text{so}\quad \frac{dv}{dt} = 12 - 2t\]
**(a)** Integrate with respect to \(t\):
\[v = 12t - t^2 + c\]
At \(t = 0\), \(v = 0\), so \(c = 0\), and \(v = 12t - t^2\) m s⁻¹.

**(b)** The speed is greatest when \(a = 0\), that is when the force is zero, at \(t = 6\). Then \(v = 72 - 36 = 36\) m s⁻¹. After \(t = 6\) the force is negative, so the particle slows down, but it is still moving forward.

**(c)** The particle is at rest when \(v = t(12 - t) = 0\), so \(t = 12\) (the other root, \(t = 0\), is the start). Integrate again, using \(x = 0\) when \(t = 0\):
\[x = 6t^2 - \frac{t^3}{3}\]
At \(t = 12\):
\[x = 864 - 576 = 288\]
The particle comes to rest after 12 s, 288 m from \(O\), and never moved backwards.
:::

:::warn A force that changes sign does not make the particle reverse
In the example the force is negative for \(t > 6\), yet the velocity stays positive until \(t = 12\). A force changes the velocity, not the direction of motion directly. The direction reverses only when \(v\) itself changes sign. To find the distance travelled, check where \(v = 0\) before you integrate across a long interval.
:::

The next example has a force with a denominator, so the velocity involves a logarithm, and the position needs integration by parts. It is in the style of a "show that" followed by a harder second part.

:::eg (Exam style) A particle \(P\) of mass 4 kg is at rest at the origin \(O\) when \(t = 0\). It then moves along a straight line under the action of a force of magnitude \(\dfrac{24}{2t + 1}\) N in the direction of motion, where \(t\) is the time in seconds. (a) Show that the velocity of \(P\) at time \(t\) is \(3\ln(2t + 1)\) m s⁻¹. (b) Find the distance of \(P\) from \(O\) when \(t = 2\).
**(a)** Newton's second law, with \(a = \dfrac{dv}{dt}\):
\[4\frac{dv}{dt} = \frac{24}{2t + 1}\] [M1]
\[\frac{dv}{dt} = \frac{6}{2t + 1}\]
Integrate with respect to \(t\):
\[v = 3\ln(2t + 1) + c\] [M1 A1]
When \(t = 0\), \(v = 0\) and \(\ln 1 = 0\), so \(c = 0\) and \(v = 3\ln(2t + 1)\). [A1]

**(b)** The distance is \(x = \displaystyle\int_0^2 3\ln(2t + 1)\,dt\). Integrate by parts with \(u = \ln(2t + 1)\) and \(\dfrac{dw}{dt} = 1\):
\[\int \ln(2t + 1)\,dt = t\ln(2t + 1) - \int \frac{2t}{2t + 1}\,dt\] [M1]
Write \(\dfrac{2t}{2t + 1} = 1 - \dfrac{1}{2t + 1}\), so
\[\int \ln(2t + 1)\,dt = t\ln(2t + 1) - t + \tfrac12\ln(2t + 1)\] [A1]
Then, with limits 0 and 2:
\[\begin{aligned}
x &= 3\left[(t + \tfrac12)\ln(2t + 1) - t\right]_0^2 \\
&= 3\left(\tfrac52\ln 5 - 2\right) = 7.5\ln 5 - 6
\end{aligned}\] [M1]
The distance is \(6.07\) m (3 s.f.). [A1]

**Check**: the speed rises from 0 to \(3\ln 5 = 4.83\) m s⁻¹, so the average speed is a little over 3, and \(2 \times 3 = 6\). Good.
:::

:::plot A boat's speed \(v\) against the time \(t\) in seconds, under a resistance proportional to \(v\) (see the example below): \(v = 10e^{-t/5}\) falls to half its value after \(5\ln 2 = 3.47\) s but never reaches zero.
--f "10*exp(-x/5)" --label "v = 10 exp(−t/5)" --x 0 20 --y 0 13 --pt "3.466,5,half speed at t = 3.47@ne" --xlabel "t (s)" --ylabel "v (m/s)" --legend tr
:::

## Force depending on position: \(v\dfrac{dv}{dx}\)

When \(F\) is given as a function of \(x\), the time does not appear, so use \(a = v\dfrac{dv}{dx}\). Separate and integrate: \(m\int v\,dv = \int F(x)\,dx\). You get \(v^2\) in terms of \(x\), with the constant fixed by one known pair \((x, v)\).

This answers questions of the form "find the speed when the particle is at \(x = 5\)" without ever finding the time. If the question then asks for the time, replace \(v\) by \(\dfrac{dx}{dt}\) and separate again.

:::eg (Exam style) A particle \(P\) of mass 2 kg moves on the positive \(x\)-axis. When \(P\) is at distance \(x\) metres from the origin \(O\), the only horizontal force on it is a force of magnitude \(\dfrac{18}{x^3}\) N directed towards \(O\). When \(x = 1\), \(P\) is moving away from \(O\) with speed 3 m s⁻¹. (a) Show that \(v = \dfrac{3}{x}\). (b) Find \(x\) in terms of \(t\), where \(t = 0\) when \(x = 1\). (c) Find the time at which \(x = 7\).
**(a)** Take the positive direction away from \(O\). The force towards \(O\) is negative:
\[2v\frac{dv}{dx} = -\frac{18}{x^3}\] [M1 A1]
\[\int v\,dv = -9\int x^{-3}\,dx \quad\Rightarrow\quad \tfrac12 v^2 = \frac{9}{2x^2} + c\] [M1]
When \(x = 1\), \(v = 3\): \(\tfrac92 = \tfrac92 + c\), so \(c = 0\). Then \(v^2 = \dfrac{9}{x^2}\), and \(v > 0\) as \(P\) is moving away from \(O\), so \(v = \dfrac{3}{x}\). [A1]

**(b)** Now \(v = \dfrac{dx}{dt}\), so
\[\frac{dx}{dt} = \frac{3}{x} \quad\Rightarrow\quad \int x\,dx = \int 3\,dt\] [M1]
\[\tfrac12 x^2 = 3t + c\] [A1]
At \(t = 0\), \(x = 1\), so \(c = \tfrac12\), and \(x^2 = 6t + 1\). Since \(x > 0\),
\[x = \sqrt{6t + 1}\] [A1]
**(c)** \(7 = \sqrt{6t + 1}\) gives \(6t + 1 = 49\), so \(t = 8\) s. [B1]

**Check**: the speed at \(x = 7\) is \(\frac37\), about 0.43 m s⁻¹, and the force is \(\frac{18}{343}\) N, tiny: the particle has almost stopped feeling the pull and drifts slowly outward.
:::

The pull gets weaker with distance, yet the particle slows down for ever and still travels any distance given enough time. The speed \(v = \frac{3}{x}\) tends to 0 as \(x \to \infty\), so the particle only just "escapes". That is the idea of an escape speed, and the next example has the actual forces.

### Inverse-square forces and escape

Gravity at a distance \(x\) from the centre of a planet of radius \(R\) is \(\dfrac{k}{x^2}\) with \(k\) fixed. At the surface (\(x = R\)) the pull on mass \(m\) is \(mg\), so \(k = mgR^2\) and the force is \(\dfrac{mgR^2}{x^2}\). In 9231 the force law is given in the question; you do not need to know any gravitation theory.

:::eg A spacecraft of mass \(m\) is fired radially away from the surface of a planet of radius \(R = 6.4 \times 10^6\) m, where the surface gravity is \(g = 10\) m s⁻². At a distance \(x\) from the centre, the only force on it is a force of magnitude \(\dfrac{mgR^2}{x^2}\) towards the centre. It leaves the surface with speed \(u\). (a) Show that \(v^2 = u^2 - 2gR + \dfrac{2gR^2}{x}\). (b) For \(u = 8000\) m s⁻¹, find the greatest distance from the centre it reaches. (c) Find the least \(u\) for which the spacecraft never returns.
**(a)** Positive direction away from the centre:
\[mv\frac{dv}{dx} = -\frac{mgR^2}{x^2}\]
The mass cancels. Integrate:
\[\tfrac12 v^2 = \frac{gR^2}{x} + c\]
At \(x = R\), \(v = u\): \(\tfrac12 u^2 = gR + c\), so \(c = \tfrac12 u^2 - gR\). Then
\[v^2 = u^2 - 2gR + \frac{2gR^2}{x}\]

**(b)** At the greatest distance \(v = 0\):
\[0 = u^2 - 2gR + \frac{2gR^2}{x}\]
With \(u = 8000\): \(u^2 = 6.4 \times 10^7\) and \(2gR = 1.28 \times 10^8\), so
\[\frac{2gR^2}{x} = 1.28 \times 10^8 - 6.4 \times 10^7 = 6.4 \times 10^7\]
\[x = \frac{2gR^2}{6.4 \times 10^7} = \frac{2 \times 10 \times 4.096 \times 10^{13}}{6.4 \times 10^7} = 1.28 \times 10^7\ \text{m}\]
That is exactly \(2R\): the spacecraft rises 6400 km above the surface and falls back.

**(c)** It never returns if \(v\) never reaches 0, however large \(x\) is. As \(x \to \infty\), \(\dfrac{2gR^2}{x} \to 0\) from above, so \(v^2\) decreases towards \(u^2 - 2gR\). We need \(v^2 > 0\) for all \(x\), which holds when
\[u^2 \ge 2gR\]
The least speed is \(u = \sqrt{2gR} = \sqrt{1.28 \times 10^8} = 1.13 \times 10^4\) m s⁻¹ (3 s.f.), about 11.3 km s⁻¹. This is the **escape speed**; at exactly this speed the particle arrives "at infinity" with zero speed.
:::

## Force depending on speed: resistance

Air and water resist motion. A simple model says the resistance is proportional to the speed, \(kv\), or to its square, \(kv^2\), where \(k > 0\) is a constant. Both oppose the motion.

:::warn The sign of a resistance
If you take the direction of motion as positive, a resistance is \(-kv\) (or \(-kv^2\)). Write the minus sign in Newton's second law: \(m\dfrac{dv}{dt} = -kv\). A positive sign gives a particle that speeds up on its own, and every later answer is wrong. Choose the positive direction to be the way the particle moves, and write the sign of the resistance by looking at the diagram.
:::

When the force depends on \(v\), you can use either \(\dfrac{dv}{dt}\) or \(v\dfrac{dv}{dx}\). Look at what the question asks: **time → \(\dfrac{dv}{dt}\); distance → \(v\dfrac{dv}{dx}\)**. The first lets you separate to get \(t\) in terms of \(v\); the second gives \(x\) in terms of \(v\), and the extra \(v\) often cancels with the \(v\) in the force.

### Resistance proportional to the speed

:::eg A boat of mass 200 kg is moving at 10 m s⁻¹ when its engine is switched off. The water exerts a resistance of \(40v\) N when its speed is \(v\) m s⁻¹, and there are no other horizontal forces. Find (a) its speed 5 s after the engine is switched off, (b) the time taken to slow to 5 m s⁻¹, (c) the distance it travels before stopping.
Take the direction of motion as positive. The resistance is \(-40v\):
\[200\frac{dv}{dt} = -40v \quad\Rightarrow\quad \frac{dv}{dt} = -\frac{v}{5}\]
**(a)** Separate the variables and integrate:
\[\int \frac{dv}{v} = -\int \frac15\,dt \quad\Rightarrow\quad \ln v = -\frac{t}{5} + c\]
At \(t = 0\), \(v = 10\), so \(c = \ln 10\), and
\[\ln\frac{v}{10} = -\frac t5 \quad\Rightarrow\quad v = 10e^{-t/5}\]
At \(t = 5\), \(v = 10e^{-1} = 3.68\) m s⁻¹.

**(b)** Half speed: \(e^{-t/5} = \tfrac12\), so \(t = 5\ln 2 = 3.47\) s.

**(c)** The question asks for distance, so use \(a = v\dfrac{dv}{dx}\):
\[200v\frac{dv}{dx} = -40v \quad\Rightarrow\quad \frac{dv}{dx} = -\frac15\]
The \(v\) cancels, so \(v\) decreases at a constant rate with distance: \(v = 10 - \dfrac{x}{5}\). It stops when \(v = 0\), at \(x = 50\) m.
:::

Look at what happened. According to \(v = 10e^{-t/5}\) the boat never stops: \(v > 0\) for every \(t\). Yet the total distance is finite: the boat creeps ever closer to 50 m without passing it. Both are true: the boat slows more and more gently, and the total distance is a finite sum. For resistance \(kv\), the limiting distance is \(\dfrac{mu}{k}\) (here \(\dfrac{200 \times 10}{40} = 50\)). This is a result worth recognising, and the units check it: \(\dfrac{\text{kg} \times \text{m/s}}{\text{kg/s}}\) is metres.

### Resistance proportional to the square of the speed

:::eg (Exam style) A particle \(P\) of mass 0.5 kg moves in a straight line on a horizontal surface. The only horizontal force on \(P\) is a resistance of magnitude \(0.2v^2\) N, where \(v\) m s⁻¹ is its speed. Initially \(v = 8\). (a) Show that \(v = 8e^{-0.4x}\), where \(x\) is the distance moved. (b) Find the time taken for the speed to fall to 2 m s⁻¹. (c) Find the distance travelled in that time.
**(a)** Use \(a = v\dfrac{dv}{dx}\), with the resistance negative:
\[0.5v\frac{dv}{dx} = -0.2v^2\] [M1 A1]
Cancel \(v\) (as \(v > 0\)) and divide by 0.5:
\[\frac{dv}{dx} = -0.4v \quad\Rightarrow\quad \int\frac{dv}{v} = -0.4\int dx\] [M1]
\[\ln v = -0.4x + c\]
At \(x = 0\), \(v = 8\), so \(c = \ln 8\) and \(v = 8e^{-0.4x}\). [A1]

**(b)** For the time use \(a = \dfrac{dv}{dt}\):
\[0.5\frac{dv}{dt} = -0.2v^2 \quad\Rightarrow\quad \int \frac{dv}{v^2} = -0.4\int dt\] [M1]
\[-\frac1v = -0.4t + c\]
At \(t = 0\), \(v = 8\), so \(c = -\tfrac18\) and
\[\frac1v = 0.4t + \frac18\] [A1]
When \(v = 2\): \(\tfrac12 = 0.4t + \tfrac18\), so \(0.4t = \tfrac38\) and \(t = 0.9375\) s. [A1] (3 s.f.: 0.938 s)

**(c)** From part (a), \(2 = 8e^{-0.4x}\), so \(e^{-0.4x} = \tfrac14\) and
\[x = \frac{\ln 4}{0.4} = 3.47\ \text{m}\] [A1]
:::

Compare the two models. With resistance \(kv\) the distance travelled tends to the finite limit \(\dfrac{mu}{k}\), while \(v \to 0\) only as \(t \to \infty\). With \(kv^2\) the speed is \(ue^{-kx/m}\) and \(\dfrac{1}{v} = \dfrac{kt}{m} + \dfrac1u\): the speed tends to zero only as \(x \to \infty\) as well as \(t \to \infty\). So "find the distance to rest" has an answer in the first model and has none in the second. Whenever you reach a result like \(\ln 0\), stop and think about a limit.

### Driving forces and terminal speed

Add a constant driving force (an engine, or gravity on a falling body) to a resistance that grows with speed. At low speed the driving force wins and the particle accelerates. As \(v\) grows, the resistance grows, until the two balance and the acceleration is zero. The particle can then only travel at that speed.

:::def Terminal speed
The constant speed a particle approaches when the resistance balances the driving force, so the resultant force and the acceleration are zero: \(a = 0\). The speed tends to this value as \(t \to \infty\) but never exceeds it, if the particle starts below it.
:::

:::key Finding a terminal speed
Write the equation of motion \(m\dfrac{dv}{dt} = F_0 - R(v)\), with \(F_0\) the driving force. Put \(\dfrac{dv}{dt} = 0\) and solve \(R(V) = F_0\) for the terminal speed \(V\). For \(R = kv^2\), \(V = \sqrt{\dfrac{F_0}{k}}\). For \(R = kv\), \(V = \dfrac{F_0}{k}\).
:::

:::eg A particle of mass 2 kg is released from rest and falls vertically under gravity. The air resistance is \(0.2v^2\) N when its speed is \(v\) m s⁻¹. Take \(g = 10\). Find (a) the terminal speed, (b) \(x\) in terms of \(v\), where \(x\) is the distance fallen, (c) the time to reach 5 m s⁻¹.
Take downwards as positive. The weight is \(+20\) N and the resistance is \(-0.2v^2\) N:
\[2a = 20 - 0.2v^2 \quad\Rightarrow\quad a = 10 - 0.1v^2 = 0.1(100 - v^2)\]
**(a)** Terminal speed: \(a = 0\), so \(v^2 = 100\) and \(V = 10\) m s⁻¹.

**(b)** Use \(a = v\dfrac{dv}{dx}\), and integrate with \(x = 0\) when \(v = 0\):
\[\begin{aligned}
\int_0^x dx &= \int_0^v \frac{10v}{100 - v^2}\,dv \\
x &= \left[-5\ln(100 - v^2)\right]_0^v \\
&= 5\ln\frac{100}{100 - v^2}
\end{aligned}\]
**(c)** Use \(a = \dfrac{dv}{dt}\) and partial fractions, \(\dfrac{1}{100 - v^2} = \dfrac{1}{20}\left(\dfrac{1}{10 - v} + \dfrac{1}{10 + v}\right)\):
\[\begin{aligned}
t &= \int_0^v \frac{10\,dv}{100 - v^2} \\
&= \frac12\int_0^v \left(\frac{1}{10 - v} + \frac{1}{10 + v}\right)dv \\
&= \frac12\ln\frac{10 + v}{10 - v}
\end{aligned}\]
At \(v = 5\): \(t = \tfrac12\ln 3 = 0.549\) s.

Solving for \(v\): \(\dfrac{10 + v}{10 - v} = e^{2t}\), so \(v = 10\dfrac{e^{2t} - 1}{e^{2t} + 1} = 10\tanh t\) (see [Hyperbolic functions](#math.fm.hyperbolic)). It tends to 10 but never reaches it.
:::

:::plot The speed \(v = 10\tanh t\) of the falling particle approaches its terminal speed 10 m s⁻¹ from below: it is within 1% of it after about 3 s, but never reaches it.
--f "10*(exp(2*x)-1)/(exp(2*x)+1)" --label "v = 10 tanh t" --x 0 5 --y 0 13 --hline 10 --pt "0.549,5,v = 5 at t = 0.549@se" --xlabel "t (s)" --ylabel "v (m/s)" --legend tr
:::

The method is the same whether the driving force is gravity, an engine or a pull on a rope. Next, an example where a constant force and a \(v^2\) resistance both act. It is in the style of the real paper: use \(v\dfrac{dv}{dx}\) for the first part, then \(\dfrac{dv}{dt}\) for a time.

:::eg (Exam style) A particle \(P\) of mass 2 kg starts from rest at a point \(O\) and moves along a straight horizontal line. It is acted on by a constant driving force of 18 N and a resistance of magnitude \(2v^2\) N, where \(v\) m s⁻¹ is its speed. (a) Show that when \(P\) has travelled a distance \(x\) metres, \(x = \tfrac12\ln\left(\dfrac{9}{9 - v^2}\right)\). (b) Show that the time \(t\) taken to reach speed \(v\) is \(\dfrac{1}{6}\ln\left(\dfrac{3 + v}{3 - v}\right)\).
**(a)** With \(a = v\dfrac{dv}{dx}\):
\[2v\frac{dv}{dx} = 18 - 2v^2\] [M1 A1]
\[\int_0^x dx = \int_0^v \frac{v}{9 - v^2}\,dv\] [M1]
\[x = \left[-\tfrac12\ln(9 - v^2)\right]_0^v = -\tfrac12\ln(9 - v^2) + \tfrac12\ln 9\] [A1]
\[x = \tfrac12\ln\left(\frac{9}{9 - v^2}\right)\] [A1]

**(b)** With \(a = \dfrac{dv}{dt}\):
\[2\frac{dv}{dt} = 18 - 2v^2 \quad\Rightarrow\quad t = \int_0^v \frac{dv}{9 - v^2}\] [M1]
Partial fractions, \(\dfrac{1}{9 - v^2} = \dfrac16\left(\dfrac{1}{3 - v} + \dfrac{1}{3 + v}\right)\): [M1]
\[t = \frac16\Big[\ln(3 + v) - \ln(3 - v)\Big]_0^v\] [A1]
The lower limit gives \(\tfrac16(\ln 3 - \ln 3) = 0\), so
\[t = \frac16\ln\frac{3 + v}{3 - v}\] [A1]

**Check**: at \(x = 0.5\), \(v^2 = 9(1 - e^{-1}) = 5.69\), so \(v = 2.39\) m s⁻¹ and \(t = 0.362\) s. The terminal speed is \(\sqrt{18/2} = 3\) m s⁻¹, and both formulas blow up as \(v \to 3\), which confirms that \(P\) never reaches it.
:::

## Up and down: the direction matters

When a particle moves up and then down, the resistance changes direction and so does the sign in the equation. Treat the two stages as two separate problems, each with its own positive direction.

:::eg (Exam style) A ball of mass 0.4 kg is thrown vertically upwards with speed 20 m s⁻¹. Air resistance acts on it with magnitude \(0.04v^2\) N when the speed is \(v\) m s⁻¹. Take \(g = 10\). (a) Find the greatest height reached. (b) Find the speed with which the ball returns to the point of projection.
**(a)** Going up, take upwards as positive. Weight and resistance both act downwards:
\[0.4v\frac{dv}{dx} = -4 - 0.04v^2\] [M1 A1]
\[v\frac{dv}{dx} = -(10 + 0.1v^2)\]
Separate; \(x\) is the height above the starting point, and \(v\) falls from 20 to 0:
\[\int_0^H dx = -\int_{20}^0 \frac{v}{10 + 0.1v^2}\,dv = \int_0^{20}\frac{v}{10 + 0.1v^2}\,dv\] [M1]
\[H = \left[5\ln(10 + 0.1v^2)\right]_0^{20} = 5\ln 50 - 5\ln 10\] [A1]
\[H = 5\ln 5 = 8.05\ \text{m}\] [A1]
**(b)** Coming down, take downwards as positive. The weight is now positive, and the resistance (opposing the motion) is negative:
\[0.4v\frac{dv}{dx} = 4 - 0.04v^2\] [M1 A1]
\[\int_0^H dx = \int_0^V \frac{v}{10 - 0.1v^2}\,dv = \left[-5\ln(10 - 0.1v^2)\right]_0^V\] [M1]
\[5\ln 5 = 5\ln 10 - 5\ln(10 - 0.1V^2) \quad\Rightarrow\quad 10 - 0.1V^2 = 2\] [A1]
So \(V^2 = 80\) and \(V = 8.94\) m s⁻¹. [A1]

**Check**: the ball comes back more slowly than it left (8.94 against 20), because resistance took energy out on both journeys. Without resistance it would return at 20.
:::

## Interpreting the answer

Three kinds of limit appear in exam questions. Name each one in words, because the mark is often for the interpretation, not for the algebra.

:::key Limits and what they mean
- **\(v \to V\) as \(t \to \infty\)**: the particle approaches a terminal speed \(V\) and never exceeds it. Written \(V = \lim v\), it is also the value of \(v\) where \(a = 0\).
- **\(v\) never reaches 0**: a result of the form \(v = ue^{-kt}\) or \(v = \dfrac{u}{1 + kut}\) is positive for every \(t\), so the particle does not stop in finite time. A result like \(v = u - kx\) gives \(v = 0\) at \(x = \dfrac{u}{k}\): the distance travelled is finite, even if (as with resistance \(kv\)) that point is only reached in the limit \(t \to \infty\).
- **\(v^2 > 0\) for all \(x\)**: the particle goes to infinity and never returns (escape). The critical case, \(v^2 \to 0\) as \(x \to \infty\), is the escape speed.
:::

:::exam What to write and what is on MF19
Nothing for this chapter is on MF19 except the standard integrals from 9709 (such as \(\int \dfrac{1}{x}\,dx\) and \(\int e^{kx}\,dx\)). You must know \(a = \dfrac{dv}{dt} = v\dfrac{dv}{dx}\), and be ready to derive the last form. Write the equation of motion with the signs first: that line earns the M1 and the A1. Say which form you use ("using \(a = v\dfrac{dv}{dx}\)"). When the question says "show that", keep every step down to the given answer, including the constant of integration. Give a time or distance to 3 s.f. unless an exact form is asked for, and keep \(\ln\) answers exact if the question says "exact". Do not forget the units of the final answer.
:::

:::board
Edexcel IAL and the UK A Levels use \(g = 9.8\) where 9231 uses \(g = 10\). The difference appears only in questions with weight; the differential equations are the same, and the variable-force content in each specification is listed in its own syllabus, so use the 9231 list.
:::

:::eg Spot the error: a particle of mass 2 kg moves on a horizontal line against a resistance of \(0.6v^2\) N. Its initial speed is 5 m s⁻¹. Find \(v\) in terms of the distance \(x\) travelled, for 4 marks.
A student wrote this answer.

Line 1: \(2v\dfrac{dv}{dx} = 0.6v^2\)
Line 2: \(\dfrac{dv}{dx} = 0.3v\), so \(\displaystyle\int\dfrac{dv}{v} = \int 0.3\,dx\)
Line 3: \(\ln v = 0.3x + c\), and \(v = 5\) at \(x = 0\) gives \(c = \ln 5\)
Line 4: \(v = 5e^{0.3x}\)

Line 1 has the right form, \(mv\dfrac{dv}{dx}\), and all the forces, so the method mark is earned. [M1] **But the resistance has the wrong sign**: it opposes the motion, so the force is \(-0.6v^2\). [A0] Lines 2 to 4 follow correctly from line 1, so the second method mark is earned [M1], but the final answer is wrong and earns nothing. [A0] The student scores 2 out of 4. The clue was in the answer: a resisted particle cannot speed up, and \(5e^{0.3x}\) grows with \(x\).

Correct working: \(2v\dfrac{dv}{dx} = -0.6v^2\), so \(\dfrac{dv}{dx} = -0.3v\) and \(v = 5e^{-0.3x}\). [A1]
:::

:::try Start easy, finish at exam standard
Q: A particle of mass 4 kg starts from rest at \(O\), and a force of \(8t\) N acts on it along a straight line. Find its velocity and its distance from \(O\) when \(t = 3\).
A: \(4\dfrac{dv}{dt} = 8t\), so \(v = t^2\) (as \(v = 0\) at \(t = 0\)). At \(t = 3\), \(v = 9\) m s⁻¹. Then \(x = \dfrac{t^3}{3}\) (as \(x = 0\) at \(t = 0\)) gives \(x = 9\) m.
Q: A particle moves on the \(x\)-axis with \(v\dfrac{dv}{dx} = 6 - 2x\). It starts from \(x = 0\) at rest. Find \(v\) when \(x = 2\), and the value of \(x\) at which it next stops.
A: \(\tfrac12 v^2 = 6x - x^2 + c\), and \(c = 0\) from the start. So \(v^2 = 12x - 2x^2\). At \(x = 2\): \(v^2 = 24 - 8 = 16\), \(v = 4\) m s⁻¹. It stops again when \(12x - 2x^2 = 0\), at \(x = 6\).
Q: A particle of mass 2 kg moves on a horizontal line against a resistance of \(0.5v\) N. Its initial speed is 8 m s⁻¹. Find the time for the speed to fall to 2 m s⁻¹, and the distance it travels before stopping.
A: \(2\dfrac{dv}{dt} = -0.5v\), so \(\dfrac{dv}{dt} = -\dfrac v4\) and \(v = 8e^{-t/4}\). For \(v = 2\): \(e^{-t/4} = \tfrac14\), \(t = 4\ln 4 = 5.55\) s. For distance, \(v\dfrac{dv}{dx} = -\dfrac v4\), so \(v = 8 - \dfrac x4\), which is 0 at \(x = 32\) m.
Q: A particle moves in a line with acceleration \(-0.1v^2\) and initial speed 5 m s⁻¹. Find \(v\) in terms of the distance \(x\), and the speed after 10 m.
A: \(v\dfrac{dv}{dx} = -0.1v^2\), so \(\dfrac{dv}{dx} = -0.1v\) and \(v = 5e^{-0.1x}\). At \(x = 10\): \(v = 5e^{-1} = 1.84\) m s⁻¹.
Q: A particle falls from rest with acceleration \(a = 10 - 0.4v\). State its terminal speed and find the time to reach 15 m s⁻¹.
A: Terminal speed: \(10 - 0.4V = 0\), so \(V = 25\) m s⁻¹. Then \(\displaystyle t = \int_0^{15}\frac{dv}{10 - 0.4v} = \left[-2.5\ln(10 - 0.4v)\right]_0^{15} = 2.5\ln\frac{10}{4}\), so \(t = 2.29\) s.
Q: A particle falling from rest has acceleration \(12 - 0.03v^2\). Find the terminal speed.
A: \(12 - 0.03V^2 = 0\), so \(V^2 = 400\) and \(V = 20\) m s⁻¹ (not \(V = 400\); take the square root).
Q: A particle of mass 3 kg moves on the \(x\)-axis. It is attracted to \(O\) by a force of \(\dfrac{12}{x^2}\) N. It is at rest at \(x = 3\). Find its speed when \(x = 1\).
A: With the positive direction away from \(O\): \(3v\dfrac{dv}{dx} = -\dfrac{12}{x^2}\), so \(\tfrac12 v^2 = \dfrac4x + c\). At \(x = 3\), \(v = 0\): \(c = -\tfrac43\). At \(x = 1\): \(v^2 = 2\left(4 - \tfrac43\right) = \tfrac{16}{3}\), so the speed is \(2.31\) m s⁻¹ (towards \(O\)).
Q: Which form of the acceleration (\(\dfrac{dv}{dt}\) or \(v\dfrac{dv}{dx}\)) do you use to find (i) the speed at \(t = 3\) when \(F = 5 - 2t\), (ii) the speed at \(x = 2\) when \(F = 4x\), (iii) the time to halve the speed against a resistance \(0.3v\), (iv) the distance to halve the speed against a resistance \(0.3v^2\)?
A: (i) \(\dfrac{dv}{dt}\), as \(F\) is a function of \(t\). (ii) \(v\dfrac{dv}{dx}\), as \(F\) is a function of \(x\) and there is no time. (iii) \(\dfrac{dv}{dt}\), as a time is wanted. (iv) \(v\dfrac{dv}{dx}\), as a distance is wanted.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A particle of mass 5 kg is at rest at \(O\). A force of \(20t^2\) N acts on it along a straight line. Find its speed when \(t = 3\).
A: \(5\dfrac{dv}{dt} = 20t^2\), so \(\dfrac{dv}{dt} = 4t^2\). [M1] \(v = \dfrac{4t^3}{3}\), using \(v = 0\) at \(t = 0\). [M1] At \(t = 3\), \(v = 36\) m s⁻¹. [A1]
Q: [5 marks] ★ A particle of mass 1.2 kg moves on a horizontal line against a resistance of \(0.6v\) N. Its initial speed is 9 m s⁻¹. (a) Find the time taken for the speed to fall to 3 m s⁻¹. (b) Find the distance travelled before it stops.
A: (a) \(1.2\dfrac{dv}{dt} = -0.6v\), so \(\dfrac{dv}{dt} = -0.5v\). [M1] \(\ln\dfrac{v}{9} = -0.5t\) [M1], so \(t = 2\ln 3 = 2.20\) s. [A1]
(b) \(v\dfrac{dv}{dx} = -0.5v\), so \(\dfrac{dv}{dx} = -0.5\). [M1] \(v = 9 - 0.5x\), which is 0 at \(x = 18\) m. [A1]
Q: [6 marks] ★★ A particle \(P\) of mass 3 kg moves on the positive \(x\)-axis. The only horizontal force on it is a force of \(\dfrac{24}{x^2}\) N directed towards \(O\). When \(x = 2\), \(P\) is moving away from \(O\) with speed 4 m s⁻¹. (a) Show that \(v^2 = \dfrac{16}{x} + 8\). (b) Find the speed of \(P\) when \(x = 4\). (c) Explain why \(P\) never comes to rest.
A: (a) \(3v\dfrac{dv}{dx} = -\dfrac{24}{x^2}\) [M1 A1], so \(\tfrac12 v^2 = \dfrac8x + c\). [M1] At \(x = 2\), \(v = 4\): \(8 = 4 + c\), so \(c = 4\) and \(v^2 = \dfrac{16}{x} + 8\). [A1]
(b) At \(x = 4\): \(v^2 = 12\), so \(v = 3.46\) m s⁻¹. [A1]
(c) For all \(x > 0\), \(\dfrac{16}{x} > 0\), so \(v^2 > 8 > 0\) and \(P\) is never at rest. [B1]
Q: [5 marks] ★★ A particle of mass 0.4 kg moves on a horizontal surface against a resistance of \(0.1v^2\) N. Its initial speed is 12 m s⁻¹. (a) Show that \(v = 12e^{-0.25x}\), where \(x\) is the distance travelled. (b) Find the distance travelled when the speed has fallen to 4 m s⁻¹.
A: (a) \(0.4v\dfrac{dv}{dx} = -0.1v^2\), so \(\dfrac{dv}{dx} = -0.25v\). [M1] \(\ln v = -0.25x + c\) [M1], and \(c = \ln 12\), so \(v = 12e^{-0.25x}\). [A1]
(b) \(4 = 12e^{-0.25x}\), so \(e^{-0.25x} = \tfrac13\) [M1] and \(x = 4\ln 3 = 4.39\) m. [A1]
Q: [6 marks] ★★ A stone of mass 0.2 kg is thrown vertically upwards with speed 24 m s⁻¹. Air resistance has magnitude \(0.04v\) N. Take \(g = 10\). Find the greatest height reached.
A: Upwards positive: \(0.2v\dfrac{dv}{dx} = -2 - 0.04v\), so \(v\dfrac{dv}{dx} = -(10 + 0.2v)\). [M1 A1]
\(H = \displaystyle\int_0^{24}\frac{v}{10 + 0.2v}\,dv\) [M1]. Divide: \(\dfrac{v}{10 + 0.2v} = 5 - \dfrac{250}{50 + v}\), so \(H = \Big[5v - 250\ln(50 + v)\Big]_0^{24}\). [A1]
\(H = 120 - 250\ln\dfrac{74}{50}\) [M1] \(= 22.0\) m. [A1]
Q: [10 marks] ★★★ A particle \(P\) of mass 2 kg moves along the positive \(x\)-axis. When \(P\) is at distance \(x\) metres from the origin \(O\), a force of magnitude \(6x\) N acts on it directed away from \(O\). When \(x = 2\), the speed of \(P\) is \(2\sqrt3\) m s⁻¹, directed away from \(O\). (a) Show that \(v = \sqrt3\,x\). (b) Find \(x\) in terms of \(t\), where \(t = 0\) when \(x = 2\). (c) Find the time at which \(x = 20\).
H: Divide by the mass first: the acceleration is \(3x\). Use \(v\dfrac{dv}{dx}\).
H: In (b) write \(v = \dfrac{dx}{dt}\) and separate: the integral of \(\dfrac1x\) is \(\ln x\).
H: In (c) take the exponential of both sides, or substitute and use \(\ln\).
A: (a) \(2v\dfrac{dv}{dx} = 6x\) [M1], so \(\tfrac12 v^2 = \tfrac32x^2 + c\). [A1] At \(x = 2\), \(v^2 = 12\): \(6 = 6 + c\), so \(c = 0\). [M1] Then \(v^2 = 3x^2\) and \(v = \sqrt3\,x\) (moving away from \(O\)). [A1]
(b) \(\dfrac{dx}{dt} = \sqrt3\,x\), so \(\displaystyle\int\frac{dx}{x} = \sqrt3\int dt\) [M1]. \(\ln x = \sqrt3\,t + c\) [A1]. At \(t = 0\), \(x = 2\): \(c = \ln 2\). [M1] So \(x = 2e^{\sqrt3 t}\). [A1]
(c) \(20 = 2e^{\sqrt3 t}\), so \(\sqrt3\,t = \ln 10\) [M1], \(t = 1.33\) s. [A1]
Q: [9 marks] (#math.p3.diffeq) ★★★ A ball of mass 0.3 kg is released from rest and falls vertically through a liquid. The liquid exerts a resistance of \(0.6v\) N when the speed is \(v\) m s⁻¹. Take \(g = 10\). (a) Show that \(\dfrac{dv}{dt} = 10 - 2v\) and state the terminal speed. (b) Show that \(v = 5\left(1 - e^{-2t}\right)\). (c) Find the distance fallen in the first second.
H: Take downwards as positive: the weight is 3 N.
H: For (b) separate the variables; \(\displaystyle\int\frac{dv}{10 - 2v} = -\tfrac12\ln(10 - 2v)\).
H: For (c) integrate your answer to (b) with respect to \(t\), from 0 to 1.
A: (a) \(0.3\dfrac{dv}{dt} = 3 - 0.6v\), so \(\dfrac{dv}{dt} = 10 - 2v\). [M1 A1] Terminal speed: \(10 - 2V = 0\), so \(V = 5\) m s⁻¹. [B1]
(b) \(\displaystyle\int\frac{dv}{10 - 2v} = \int dt\), so \(-\tfrac12\ln(10 - 2v) = t + c\). [M1 A1] At \(t = 0\), \(v = 0\): \(c = -\tfrac12\ln 10\). So \(\ln\dfrac{10 - 2v}{10} = -2t\) [M1] and \(v = 5\left(1 - e^{-2t}\right)\). [A1]
(c) \(x = \displaystyle\int_0^1 5\left(1 - e^{-2t}\right)dt = \left[5t + \tfrac52e^{-2t}\right]_0^1\) [M1] \(= 5 + \tfrac52e^{-2} - \tfrac52 = 2.84\) m. [A1]
:::

:::try Stretch for A*
Q: [13 marks] ★★★ A car of mass 1000 kg travels along a straight horizontal road with its engine working at a constant power of 18 000 W. The resistance to motion is \(20v\) N when the speed is \(v\) m s⁻¹. (a) Find the maximum speed of the car. (b) Show that \(1000v\dfrac{dv}{dt} = 18\,000 - 20v^2\). (c) Find the time taken to accelerate from 10 m s⁻¹ to 20 m s⁻¹. (d) Find the distance travelled in that time.
H: The driving force is \(\dfrac{P}{v}\) (power divided by speed), so the force depends on \(v\).
H: In (c) the integral \(\displaystyle\int\frac{50v}{900 - v^2}\,dv\) is a logarithm; in (d) divide first: \(\dfrac{v^2}{900 - v^2} = -1 + \dfrac{900}{900 - v^2}\).
A: (a) At maximum speed the acceleration is zero, so the driving force equals the resistance: \(\dfrac{18\,000}{v} = 20v\). [M1] \(v^2 = 900\), so the maximum speed is 30 m s⁻¹. [A1]
(b) Driving force \(= \dfrac{P}{v} = \dfrac{18\,000}{v}\) [B1]. \(1000\dfrac{dv}{dt} = \dfrac{18\,000}{v} - 20v\); multiplying by \(v\) gives \(1000v\dfrac{dv}{dt} = 18\,000 - 20v^2\). [B1]
(c) \(\displaystyle t = \int_{10}^{20}\frac{50v}{900 - v^2}\,dv\) [M1] \(= \Big[-25\ln(900 - v^2)\Big]_{10}^{20}\) [A1] \(= 25\ln\dfrac{800}{500}\) [M1] \(= 11.8\) s. [A1]
(d) Use \(1000v\dfrac{dv}{dx} = \dfrac{18\,000 - 20v^2}{v}\), so \(x = \displaystyle\int_{10}^{20}\frac{50v^2}{900 - v^2}\,dv\). [M1] \(\dfrac{v^2}{900 - v^2} = -1 + \dfrac{900}{900 - v^2}\) [M1], and \(\displaystyle\int\frac{900}{900 - v^2}\,dv = 15\ln\frac{30 + v}{30 - v}\). [A1] So \(x = 50\left[-v + 15\ln\dfrac{30 + v}{30 - v}\right]_{10}^{20}\) [A1] \(= 50\left(-10 + 15\ln 2.5\right) = 187\) m. [A1]
Q: [6 marks] ★★★ A particle moves in a straight line with initial speed \(u\) against a resistance that gives it an acceleration \(-kv^2\), where \(k\) is a positive constant. (a) Show that \(v = \dfrac{u}{1 + kut}\) and that the distance travelled is \(x = \dfrac1k\ln(1 + kut)\). (b) Hence show that \(v = ue^{-kx}\), and explain why the particle never stops.
H: For the time form use \(\dfrac{dv}{dt} = -kv^2\), so \(\displaystyle\int\frac{dv}{v^2} = -k\int dt\).
H: For the distance, integrate \(v\) with respect to \(t\); the integral of \(\dfrac{1}{1 + kut}\) is \(\dfrac{1}{ku}\ln(1 + kut)\).
A: (a) \(\displaystyle\int\frac{dv}{v^2} = -k\int dt\) gives \(-\dfrac1v = -kt + c\). [M1] At \(t = 0\), \(v = u\): \(c = -\dfrac1u\), so \(\dfrac1v = kt + \dfrac1u = \dfrac{1 + kut}{u}\) and \(v = \dfrac{u}{1 + kut}\). [A1]
\(x = \displaystyle\int_0^t\frac{u}{1 + kut}\,dt\) [M1] \(= \left[\dfrac1k\ln(1 + kut)\right]_0^t = \dfrac1k\ln(1 + kut)\). [A1]
(b) From (a), \(1 + kut = e^{kx}\). Then \(v = \dfrac{u}{e^{kx}} = ue^{-kx}\). [M1] Since \(ue^{-kx} > 0\) for every \(x\), and \(\dfrac{u}{1 + kut} > 0\) for every \(t\), the speed never reaches zero: the particle never stops, though its speed tends to 0. [A1]
:::

:::quiz
? A particle's acceleration is to be found at a position \(x\), and the force is given as a function of \(x\) only. Which form of the acceleration do you use?
- \(\dfrac{dv}{dx}\)
+ \(v\dfrac{dv}{dx}\)
- \(\dfrac{dv}{dt}\) with \(F\) replaced by its average value
- \(\dfrac{d^2x}{dt^2}\) and then integrate \(F\) with respect to \(t\)
> \(v\dfrac{dv}{dx}\) lets you integrate with respect to \(x\), where the force is known. Using \(\dfrac{dv}{dx}\) drops a factor \(v\), and \(\dfrac{dv}{dt}\) with a force in \(x\) cannot be integrated without knowing \(x(t)\).
? A particle moves on a horizontal line against a resistance \(kv\). Which equation is correct, taking the direction of motion as positive?
- \(m\dfrac{dv}{dt} = kv\)
+ \(m\dfrac{dv}{dt} = -kv\)
- \(m\dfrac{dv}{dx} = -kv\)
- \(m\dfrac{dv}{dt} = -k\)
> The resistance opposes the motion, so the force is \(-kv\) and the acceleration \(\dfrac{dv}{dt}\) is negative. \(m\dfrac{dv}{dx}\) forgets the factor \(v\) in the acceleration, and \(-k\) forgets that the resistance depends on \(v\).
? A particle falls with acceleration \(20 - 0.8v^2\). What is its terminal speed?
- \(25\) m s⁻¹
+ \(5\) m s⁻¹
- \(0.04\) m s⁻¹
> At terminal speed \(20 - 0.8V^2 = 0\), so \(V^2 = 25\) and \(V = 5\). The answer 25 stops at \(V^2\) and forgets the square root; 0.04 inverts the ratio.
? A particle has \(v\dfrac{dv}{dx} = 6x\) and is at rest at \(x = 0\). What is \(v^2\) in terms of \(x\)?
- \(3x^2\)
+ \(6x^2\)
- \(12x^2\)
- \(6x\)
> \(\tfrac12 v^2 = 3x^2 + c\) and \(c = 0\), so \(v^2 = 6x^2\). The answer \(3x^2\) forgets that \(\int v\,dv = \tfrac12 v^2\), and \(12x^2\) integrates \(6x\) as \(6x^2\) before doubling.
? A boat slows against a resistance \(kv\). Which is true?
+ It never goes beyond a finite distance, but its speed is positive for every finite time.
- It stops after a finite time, but travels an infinite distance.
- It stops after a finite time and a finite distance.
- It never stops and travels an infinite distance.
> \(v = ue^{-kt/m}\) is positive for all \(t\), and \(v = u - \dfrac{k}{m}x\) shows the distance approaches the finite limit \(\dfrac{mu}{k}\) (where \(v\) would be 0) without ever reaching it. Do not confuse the two statements.
? A particle starts from rest with force \(6 - t\) N and mass 1 kg. What is true at \(t = 6\)?
+ Its speed is at a maximum, because the force is zero there.
- It is at rest, because the force is zero.
- It reverses direction, because the force changes sign.
- Its speed is 0, because \(6 - t = 0\).
> The speed grows while the force is positive and falls once it is negative, so \(v\) is greatest where \(a = 0\). The velocity is \(v = 6t - \tfrac12t^2\), which is 18 at \(t = 6\) and stays positive until \(t = 12\).
:::

:::checklist What you can now do
- [ ] I can write Newton's second law for a straight-line motion as a differential equation, using \(\dfrac{dv}{dt}\) or \(v\dfrac{dv}{dx}\), with every sign right.
- [ ] I can derive \(a = v\dfrac{dv}{dx}\) from the chain rule.
- [ ] I can choose between \(\dfrac{dv}{dt}\) and \(v\dfrac{dv}{dx}\) from the variable the force depends on and what the question asks.
- [ ] I can solve problems with a force depending on time, using the initial conditions to find each constant.
- [ ] I can solve problems with a force depending on position, finding \(v\) in terms of \(x\) and then \(x\) in terms of \(t\).
- [ ] I can solve problems with a resistance proportional to \(v\) or \(v^2\), finding time, distance and speed.
- [ ] I can find a terminal speed, and interpret limits such as "never stops" and "escapes".
- [ ] I can handle up-and-down motion with resistance, changing the sign of the forces at the turn.
:::

:::recap
- \(a = \dfrac{dv}{dt} = v\dfrac{dv}{dx} = \dfrac{d^2x}{dt^2}\); derive the middle form by the chain rule. Then \(F = ma\) is a differential equation.
- Force in terms of \(t\): use \(\dfrac{dv}{dt}\). Force in terms of \(x\): use \(v\dfrac{dv}{dx}\), giving \(\tfrac12 v^2\). Force in terms of \(v\): time uses \(\dfrac{dv}{dt}\), distance uses \(v\dfrac{dv}{dx}\).
- Take the direction of motion as positive. A resistance is \(-kv\) or \(-kv^2\); a force towards \(O\) is negative.
- Find constants of integration at once from the initial conditions. To find \(t\) from \(v(x)\), put \(v = \dfrac{dx}{dt}\) and separate again.
- Resistance \(kv\): stops after distance \(\dfrac{mu}{k}\) but never in finite time. Resistance \(kv^2\): \(v = ue^{-kx/m}\), no finite stopping distance.
- Terminal speed: put \(a = 0\). For \(F_0 - kv^2\), \(V = \sqrt{F_0/k}\); the speed tends to \(V\) as \(t \to \infty\).
- Inverse-square force \(\dfrac{mgR^2}{x^2}\): \(v^2 = u^2 - 2gR + \dfrac{2gR^2}{x}\); escape speed \(\sqrt{2gR}\).
- Up and down: the sign of the resistance changes with the direction of motion; treat each stage separately.
:::

:::links
- watch: [Projectiles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NhfzR6dcRPAo139k4Q_YmP-) · ExamSolutions (YouTube) · motion under gravity, useful before adding resistance
- watch: [Differential equations, a tourist's guide](https://www.3blue1brown.com/lessons/differential-equations) · 3Blue1Brown · why a rate of change that depends on the state gives a differential equation
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · variable force questions with answers
- practise: [Differential equations](https://www.khanacademy.org/math/differential-equations) · Khan Academy · separable equations, the maths behind every example here
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Paper 3 questions with mark schemes [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers sorted by year

Links checked 20 November 2026.
:::
Next: [Direct impact and restitution](#math.fm.impulse) moves from forces that act over time to collisions, where the force acts for a moment and momentum and Newton's experimental law decide what happens.
