@chapter math.fm.circular
@title Circular motion: horizontal circles
@level fm
@paper CAIE 9231 Paper 3
@time 5–6 hours
@summary A particle moving in a circle at constant speed accelerates towards the centre, and the resultant force on it must point that way. You will learn angular speed and the relation \(v = r\omega\), the acceleration \(r\omega^2 = \dfrac{v^2}{r}\), and how to use them for particles on discs, conical pendulums (with inextensible and elastic strings), cones and bowls, banked tracks and two strings on a rod.

:::why
A car on a bend, a ride at a fairground, a satellite and a drying machine all move in circles. The speed can be steady and yet the particle is accelerating, because its direction keeps changing. Mechanics then asks one question: what force points towards the centre? Answering it for strings, friction and slopes is a large part of Further Mechanics.
:::

**Before you start**, you need Newton's second law, friction and resolving forces from [Newton's laws and connected particles](#math.m.newton) and [Forces and equilibrium](#math.m.forces), radians and arc length from [Circular measure](#math.p1.circular), and Hooke's law from [Hooke's law and elastic energy](#math.fm.elastic).

:::try Warm-up
Q: An arc of a circle of radius 5 cm subtends an angle of 0.8 radians at the centre. Find the arc length. (from [Circular measure](#math.p1.circular))
A: \(s = r\theta = 5 \times 0.8 = 4\) cm.
Q: A particle of mass 2 kg lies on a rough horizontal surface with \(\mu = 0.4\). Find the greatest friction force available. Take \(g = 10\). (from [Newton's laws and connected particles](#math.m.newton))
A: \(R = 20\) N, so \(F_{\max} = 0.4 \times 20 = 8\) N.
Q: A string of natural length 0.5 m and modulus 20 N is stretched to a length of 0.65 m. Find the tension. (from [Hooke's law and elastic energy](#math.fm.elastic))
A: \(x = 0.15\) m, so \(T = \dfrac{20 \times 0.15}{0.5} = 6\) N.
:::

## Angular speed

A particle moving round a circle of radius \(r\) covers an angle at a certain rate. That rate has its own name.

:::def Angular speed
The rate at which the line from the centre to a particle turns, measured in radians per second. For a particle in a circle it is written \(\omega\) (the Greek letter omega). If it is constant, the particle turns through \(\omega t\) radians in time \(t\).
:::

One full turn is \(2\pi\) radians. So the **period** (the time for one revolution) is \(\dfrac{2\pi}{\omega}\), and the number of revolutions per second is \(\dfrac{\omega}{2\pi}\). Everyday speeds use revolutions per minute (rpm). One revolution per minute is \(\dfrac{2\pi}{60}\) rad s⁻¹.

In time \(t\) the particle moves a distance \(r \times \omega t\) round the arc (arc length \(= r\theta\)), so its **speed** is \(r\omega\).

:::key Angular speed and speed
\[v = r\omega \qquad T = \frac{2\pi}{\omega} \qquad \omega\ (\mathrm{rad\,s^{-1}}) = \frac{2\pi \times \mathrm{rpm}}{60}\]
\(v\) is the speed along the circle in m s⁻¹, \(r\) the radius in m, \(\omega\) the angular speed in rad s⁻¹ and \(T\) the period in seconds. \(v = r\omega\) is **not** on MF19: learn it.
:::

:::eg A turntable rotates at 45 revolutions per minute. (a) Find its angular speed. (b) Find the speed of a point 0.4 m from the centre. (c) Find the angular speed of a wheel turning at 12 rad s⁻¹, in rpm.
(a)
\[\omega = \frac{45 \times 2\pi}{60} = \frac{3\pi}{2} = 4.71\ \mathrm{rad\,s^{-1}}\]
(b)
\[v = r\omega = 0.4 \times \frac{3\pi}{2} = 1.88\ \mathrm{m\,s^{-1}}\]
(c) Reverse the conversion: \(\dfrac{12 \times 60}{2\pi} = 114.6\) rpm, about 115 revolutions per minute.
:::

## The acceleration towards the centre

A particle moving at **constant speed** in a circle has constant speed but changing velocity: the direction turns all the time. Changing velocity means acceleration. The acceleration is towards the centre of the circle, and is found from the speed and the radius.

:::key Acceleration in a circle
A particle moving in a circle of radius \(r\) at constant speed \(v\) and angular speed \(\omega\) has acceleration towards the centre of magnitude
\[a = r\omega^2 = \frac{v^2}{r}\]
These are on MF19. They are the same thing: \(v = r\omega\) gives \(\dfrac{v^2}{r} = \dfrac{r^2\omega^2}{r}\).
:::

:::proof Why the acceleration is \(r\omega^2\) towards the centre (not examined)
Take the centre as the origin and start at \((r, 0)\) at time 0.
1. After time \(t\) the particle has turned through \(\omega t\), so its position is \(\mathbf{r} = (r\cos\omega t,\ r\sin\omega t)\).
2. Differentiate for the velocity: \(\mathbf{v} = (-r\omega\sin\omega t,\ r\omega\cos\omega t)\).
3. Its magnitude is \(r\omega\sqrt{\sin^2\omega t + \cos^2\omega t} = r\omega\), the constant speed. The velocity is at right angles to \(\mathbf{r}\) (their scalar product is 0): it is tangent to the circle.
4. Differentiate again: \(\mathbf{a} = (-r\omega^2\cos\omega t,\ -r\omega^2\sin\omega t)\).
5. That is \(\mathbf{a} = -\omega^2\mathbf{r}\): the acceleration points opposite to the position vector, towards the origin.
6. Its magnitude is \(r\omega^2\), and with \(\omega = \dfrac{v}{r}\) this is \(\dfrac{v^2}{r}\).
:::

By Newton's second law the resultant force on the particle is mass times acceleration, so it too points towards the centre:

:::key The force towards the centre
Resultant force towards the centre \(= \dfrac{mv^2}{r} = mr\omega^2\).
This is not a new force. It is the **resultant** of the real forces (tension, friction, a component of the normal reaction, weight) added up towards the centre. Never draw a force called "centripetal force" on your diagram.
:::

:::warn No centrifugal force
A passenger in a turning car feels pushed outwards, but that is the car seat pushing inwards on someone whose body "wants" to carry straight on. In the exam model there are only real forces, and the resultant points inward. If you draw an outward "centrifugal force" on a diagram you will write a wrong equation and lose the marks.
:::

:::steps
1. Draw the particle and every real force on it. Mark the centre of the circle and the radius \(r\). The radius is the distance of the particle from the **vertical axis** of the motion.
2. **Vertically** the particle is not accelerating (it stays on a horizontal circle): resolve and put the forces equal.
3. **Horizontally, towards the centre**, the resultant force equals \(\dfrac{mv^2}{r}\) or \(mr\omega^2\): write the equation using whichever of \(v\) and \(\omega\) the question gives.
4. Solve the two equations together. Work with exact fractions or full calculator values.
:::

:::eg A particle of mass 0.4 kg moves in a horizontal circle of radius 0.5 m on a smooth horizontal table. It is attached to the centre of the circle by a light inextensible string, and moves at 3 m s⁻¹. Find the tension in the string and the angular speed.
The tension is the only horizontal force, and it points towards the centre. Vertically the weight and the normal reaction cancel.
\[T = \frac{mv^2}{r} = \frac{0.4 \times 9}{0.5} = 7.2\ \mathrm{N}\]
The angular speed is \(\omega = \dfrac{v}{r} = \dfrac{3}{0.5} = 6\) rad s⁻¹.

**Check**: \(mr\omega^2 = 0.4 \times 0.5 \times 36 = 7.2\) N. ✓
:::

:::eg A fairground ride carries riders in a horizontal circle of radius 6 m, one revolution taking 5 s. Find the speed of a rider and the size of the acceleration, as a multiple of \(g\). Take \(g = 10\).
\[\omega = \frac{2\pi}{5} = 1.257\ \mathrm{rad\,s^{-1}}, \qquad v = r\omega = 6 \times 1.257 = 7.54\ \mathrm{m\,s^{-1}}\]
\[a = r\omega^2 = 6 \times 1.257^2 = 9.47\ \mathrm{m\,s^{-2}}\]
That is \(0.947g\), nearly \(g\): the resultant force on a rider is nearly equal to their weight, and acts horizontally.
:::

## A particle on a rotating disc

Place a coin on a record player. If the turntable spins slowly the coin goes round with it; faster and it slides off. The only horizontal force on the coin is friction, so friction provides all the force towards the centre. The coin stays at rest **relative to the disc** while friction is no more than its limiting value \(\mu R\).

:::eg A coin rests on a rough horizontal turntable at 0.12 m from the centre. The coefficient of friction is 0.6. The turntable rotates with constant angular speed. Find the greatest angular speed for which the coin does not slip, and give it in revolutions per minute. Take \(g = 10\).
Vertically \(R = mg\). Horizontally, friction towards the centre is at most \(\mu R = 0.6\,mg\). At the greatest angular speed it is limiting:
\[\mu mg = mr\omega^2\]
\[\omega^2 = \frac{\mu g}{r} = \frac{0.6 \times 10}{0.12} = 50\]
\[\omega = 7.07\ \mathrm{rad\,s^{-1}} = \frac{7.071 \times 60}{2\pi} = 67.5\ \mathrm{rpm}\]
The mass cancels: a heavier coin would slip at exactly the same speed. A coin further out (larger \(r\)) slips at a smaller \(\omega\).
:::

## The conical pendulum

Hang a ball on a string and set it moving in a horizontal circle: the string sweeps out a cone. This is the **conical pendulum**. The picture shows it from the side.

:::html
<figure class="fig small"><svg viewBox="0 0 320 210" role="img" aria-label="A conical pendulum seen from the side. A string of length l runs from a fixed point O at the top to a particle P, which moves in a horizontal circle of radius r about the vertical line through O. The angle between the string and the vertical is theta. The tension T acts along the string towards O and the weight mg acts vertically downwards."><path class="ln-m thin dash" d="M110 24V190"/><path class="ln-m thin dash" d="M30 150H190"/><path class="c3" d="M110 24L190 150"/><circle class="f1 s-acc sw2" cx="190" cy="150" r="9"/><rect class="f2 s-acc sw2" x="106" y="20" width="8" height="8"/><path class="c1 thick" d="M190 150L157.8 99.3" marker-end="url(#ah)"/><path class="c2 thick" d="M190 150V196" marker-end="url(#ah)"/><path class="ln thin" d="M110 64A40 40 0 0 0 131.4 57.8"/><text class="tl" x="118" y="78">θ</text><text class="tl" x="164" y="94">T</text><text class="tl" x="206" y="192">mg</text><text class="tl" x="144" y="144" text-anchor="middle">r</text><text class="tl" x="96" y="30" text-anchor="end">O</text><text class="tl" x="134" y="116">l</text></svg><figcaption>The string has length \(l\) but the circle has radius \(r = l\sin\theta\). The two forces on \(P\) are \(T\) and \(mg\). Their resultant is horizontal and points to the centre of the circle, the point on the dashed vertical line level with \(P\).</figcaption></figure>
:::

Resolve in two directions. There is no vertical acceleration, and the horizontal resultant provides the force towards the centre:
\[\begin{aligned}
T\cos\theta &= mg \\
T\sin\theta &= \frac{mv^2}{r} = mr\omega^2
\end{aligned}\]
With \(r = l\sin\theta\), the second equation gives \(T = ml\omega^2\), and dividing the two equations gives \(\tan\theta = \dfrac{v^2}{rg}\).

:::key Conical pendulum (inextensible string of length \(l\), angle \(\theta\) to the vertical)
\[\begin{aligned}
r &= l\sin\theta \\
T\cos\theta &= mg \\
T\sin\theta &= mr\omega^2 \quad\Rightarrow\quad T = ml\omega^2,\ \ \cos\theta = \frac{g}{l\omega^2}
\end{aligned}\]
The string can only keep the particle in a horizontal circle (\(\cos\theta < 1\)) if \(l\omega^2 > g\): too slow, and the particle just hangs.
:::

:::warn The radius is not the string length
The radius of the circle is \(l\sin\theta\), the horizontal distance from the vertical axis, not \(l\). Using \(l\) in \(\dfrac{mv^2}{r}\) is the most common error in this topic. Mark \(r\) on your diagram before you write any equation.
:::

:::eg A particle of mass 0.4 kg is attached to one end of a light inextensible string of length 1.25 m. The other end is fixed, and the particle moves in a horizontal circle with constant angular speed 4 rad s⁻¹. Find (a) the angle of the string to the vertical, (b) the tension, (c) the speed of the particle. Take \(g = 10\).
(a) Use \(\cos\theta = \dfrac{g}{l\omega^2}\):
\[\cos\theta = \frac{10}{1.25 \times 16} = \frac12 \quad\Rightarrow\quad \theta = 60^\circ\]
(b) \(T = ml\omega^2 = 0.4 \times 1.25 \times 16 = 8\) N.

**Check**: \(T\cos 60^\circ = 4 = mg\). ✓

(c) The radius is \(1.25\sin 60^\circ = 1.0825\) m, so \(v = r\omega = 1.0825 \times 4 = 4.33\) m s⁻¹.
:::

:::eg A particle \(P\) of mass 0.5 kg is attached to a fixed point by a light inextensible string of length 0.8 m. It moves in a horizontal circle with the string at \(30^\circ\) to the vertical. Find the tension and the speed. Take \(g = 10\).
The radius is \(0.8\sin 30^\circ = 0.4\) m.
\[T\cos 30^\circ = 0.5 \times 10 \quad\Rightarrow\quad T = 5.77\ \mathrm{N}\]
Horizontally:
\[\begin{aligned}
T\sin 30^\circ &= \frac{0.5v^2}{0.4} \\
2.887 &= 1.25v^2 \\
v^2 &= 2.309
\end{aligned}\]
So \(v = 1.52\) m s⁻¹. Alternatively \(\tan\theta = \dfrac{v^2}{rg}\) gives \(v^2 = 0.4 \times 10 \times \tan 30^\circ = 2.309\), the same answer.
:::

### With an elastic string

If the string is elastic its length is **not known** in advance: it is the natural length plus the extension, and the extension comes from the tension by Hooke's law (see [Hooke's law and elastic energy](#math.fm.elastic)). You then have one more unknown (the length \(L\)) and one more equation. The method: write the two Newton equations with \(L\) for the length, use \(T = \dfrac{\lambda(L - l)}{l}\) to link \(T\) to \(L\), and solve.

:::eg A particle of mass 0.5 kg is attached to one end of a light elastic string of natural length 0.5 m and modulus 25 N. The other end is fixed to a point \(O\). The particle moves in a horizontal circle with the string at \(60^\circ\) to the vertical. Find the length of the string, the angular speed and the speed of the particle. Take \(g = 10\).
Vertically, \(T\cos 60^\circ = mg = 5\), so \(T = 10\) N.

Hooke's law gives the extension:
\[x = \frac{Tl}{\lambda} = \frac{10 \times 0.5}{25} = 0.2\ \mathrm{m}\]
The length is \(L = 0.5 + 0.2 = 0.7\) m, and the radius is \(0.7\sin 60^\circ = 0.6062\) m.

Horizontally:
\[\begin{aligned}
T\sin 60^\circ &= mr\omega^2 \\
8.660 &= 0.5 \times 0.6062 \times \omega^2 \\
\omega^2 &= 28.57
\end{aligned}\]
So \(\omega = 5.35\) rad s⁻¹, and \(v = r\omega = 0.6062 \times 5.345 = 3.24\) m s⁻¹.
:::

:::eg (Exam style) A particle \(P\) of mass 0.4 kg is attached to one end of a light elastic string of natural length 0.6 m and modulus of elasticity 24 N. The other end of the string is fixed to a point \(O\). \(P\) moves in a horizontal circle with constant angular speed 5 rad s⁻¹, with the string making an angle \(\theta\) with the downward vertical through \(O\). The length of the string is \(L\) m. Take \(g = 10\). (a) Show that \(L = 0.8\). (b) Find \(\theta\). (c) Find the speed of \(P\).
**(a)** Horizontally, the radius is \(L\sin\theta\):
\[T\sin\theta = 0.4 \times L\sin\theta \times 25\] [M1 A1]
So \(T = 10L\). By Hooke's law \(T = \dfrac{24(L - 0.6)}{0.6} = 40(L - 0.6)\). [M1]
\[\begin{aligned}
10L &= 40L - 24 \\
L &= 0.8
\end{aligned}\] [A1]
**(b)** \(T = 8\) N. Vertically, \(T\cos\theta = 0.4 \times 10 = 4\), [M1] so \(\cos\theta = \tfrac12\) and \(\theta = 60^\circ\). [A1]
**(c)** The radius is \(0.8\sin 60^\circ = 0.6928\) m, and
\[v = r\omega = 0.6928 \times 5\] [M1]
\[v = 3.46\ \mathrm{m\,s^{-1}}\] [A1]
:::

## A particle inside a smooth cone or bowl

Now the surface pushes on the particle. A smooth surface pushes at right angles to itself, so the normal reaction has a vertical component that holds the particle up and a horizontal one that provides the force towards the axis. Everything else is the same.

:::eg A smooth hollow cone has its axis vertical and its vertex downwards, with semi-vertical angle \(30^\circ\) (the surface makes \(30^\circ\) with the axis). A particle of mass 0.3 kg moves in a horizontal circle on the inside surface, at a height 0.45 m above the vertex. Find the normal reaction and the speed of the particle. Take \(g = 10\).
The surface makes \(30^\circ\) with the vertical, so the normal reaction \(R\) makes \(30^\circ\) with the horizontal. Its vertical component is \(R\sin 30^\circ\) and its horizontal component, towards the axis, is \(R\cos 30^\circ\).
\[\begin{aligned}
R\sin 30^\circ &= mg = 3 \quad\Rightarrow\quad R = 6\ \mathrm{N} \\
R\cos 30^\circ &= \frac{mv^2}{r}
\end{aligned}\]
The radius is \(r = 0.45\tan 30^\circ = 0.2598\) m. So
\[\begin{aligned}
5.196 &= \frac{0.3v^2}{0.2598} \\
v^2 &= 4.5
\end{aligned}\]
and \(v = 2.12\) m s⁻¹. Notice \(v^2 = 4.5 = g \times 0.45\): for any cone, \(v^2 = gh\), where \(h\) is the height above the vertex.
:::

## Banked tracks

On a flat bend, only friction can turn a car. A **banked** track tilts towards the centre, so that part of the normal reaction points inward. At one speed no friction is needed at all.

:::html
<figure class="fig small"><svg viewBox="0 0 340 190" role="img" aria-label="Cross-section of a banked track rising to the right at angle theta to the horizontal, with a car on it. The centre of the circle lies to the left, level with the car, shown by a dashed arrow. Forces on the car: the weight mg downwards, the normal reaction R perpendicular to the track, and friction F down the slope."><path class="ax" d="M20 170H300"/><path class="ln thick" d="M20 170L300 39.4"/><path class="ln-m thin dash" d="M300 170V39.4"/><circle class="f1 s-acc sw2" cx="196.2" cy="77.9" r="9"/><path class="ln-m thin dash" d="M196.2 77.9H116.2" marker-end="url(#ah)"/><path class="c2 thick" d="M196.2 77.9V123.9" marker-end="url(#ah)"/><path class="c4 thick" d="M196.2 77.9L173.4 29" marker-end="url(#ah)"/><path class="c3 dash thick" d="M196.2 77.9L161.8 94" marker-end="url(#ah)"/><path class="ln thin" d="M60 170A40 40 0 0 0 56.3 153.1"/><text class="tl" x="70" y="166">θ</text><text class="tl" x="210" y="134">mg</text><text class="tl" x="160" y="32">R</text><text class="tl" x="144" y="102">F</text><text class="tl" x="150" y="68" text-anchor="end">to the centre</text></svg><figcaption>A car on a track banked at \(\theta\) to the horizontal. The normal reaction \(R\) is perpendicular to the surface, so it tilts towards the centre. Friction \(F\) is shown acting down the slope, for the car about to slide up the bank.</figcaption></figure>
:::

Without friction, the two forces are \(R\) and \(mg\):
\[\begin{aligned}
R\cos\theta &= mg \\
R\sin\theta &= \frac{mv^2}{r}
\end{aligned}\]
Dividing, \(\tan\theta = \dfrac{v^2}{rg}\). That is the speed at which the car needs no help from friction. Faster, and the car tends to slide up the bank (friction acts down the slope); slower, and it tends to slide down (friction acts up the slope). Resolve **horizontally** and **vertically**, not along and across the slope: the acceleration is horizontal, towards the centre.

:::key Banked track
With no friction needed: \(\tan\theta = \dfrac{v^2}{rg}\).

With friction \(F = \mu R\) at the limit, resolve vertically (no acceleration) and horizontally towards the centre. Friction **down** the slope (car about to slide up, the greatest speed):
\[\begin{aligned}
R\cos\theta - F\sin\theta &= mg \\
R\sin\theta + F\cos\theta &= \frac{mv^2}{r}
\end{aligned}\]
Friction **up** the slope (car about to slide down, the least speed):
\[\begin{aligned}
R\cos\theta + F\sin\theta &= mg \\
R\sin\theta - F\cos\theta &= \frac{mv^2}{r}
\end{aligned}\]
:::

:::eg A road bend is a circular arc of radius 250 m. It is to be banked so that a car travelling at 25 m s⁻¹ needs no friction. Find the angle of the bank. Take \(g = 10\).
\[\tan\theta = \frac{v^2}{rg} = \frac{625}{250 \times 10} = 0.25\]
\(\theta = 14.0^\circ\). The mass of the car is not needed.
:::

:::eg (Exam style) A cyclist rides round a circular track of radius 20 m banked at \(\theta\) to the horizontal, where \(\tan\theta = \tfrac34\). The coefficient of friction between the tyres and the track is 0.5. Model the cyclist and bicycle as a particle of mass \(m\). Take \(g = 10\). (a) Find the speed at which no friction is needed. (b) Find the greatest speed at which the cyclist can ride without slipping. (c) Find the least speed.
Here \(\sin\theta = 0.6\) and \(\cos\theta = 0.8\).
**(a)**
\[\tan\theta = \frac{v^2}{rg} \quad\Rightarrow\quad v^2 = 20 \times 10 \times 0.75 = 150\] [M1]
\[v = 12.2\ \mathrm{m\,s^{-1}}\] [A1]
**(b)** The cyclist is about to slide **up** the bank, so friction is limiting and acts down the slope, \(F = 0.5R\). [B1]
\[\begin{aligned}
R\cos\theta - F\sin\theta &= mg \\
0.8R - 0.3R &= mg \quad\Rightarrow\quad R = 2mg
\end{aligned}\] [M1 A1]
\[\begin{aligned}
R\sin\theta + F\cos\theta &= \frac{mv^2}{20} \\
0.6R + 0.4R &= \frac{mv^2}{20} \\
2mg &= \frac{mv^2}{20}
\end{aligned}\] [M1 A1]
\[v^2 = 400 \quad\Rightarrow\quad v = 20\ \mathrm{m\,s^{-1}}\] [A1]
**(c)** About to slide **down**: friction acts up the slope.
\[\begin{aligned}
0.8R + 0.3R &= mg \quad\Rightarrow\quad R = \frac{mg}{1.1} \\
0.6R - 0.4R &= \frac{mv^2}{20}
\end{aligned}\] [M1 A1]
\[\begin{aligned}
v^2 &= \frac{20 \times 0.2 \times 10}{1.1} = 36.36 \\
v &= 6.03\ \mathrm{m\,s^{-1}}
\end{aligned}\] [A1]
:::

:::exam Which way does friction act?
Decide first whether the vehicle is about to slide up the bank (too fast: friction down the slope) or down the bank (too slow: friction up the slope). Write that in words on your diagram. A range of speeds always comes from two cases. If a question asks for the "greatest speed" it is the first case.
:::

## Two strings and a vertical rod

A particle can also be tied to two points on a vertical axis. One string alone would swing out like a conical pendulum; the second string adds a force. Both strings are taut only for a range of speeds. The tension in a string is zero at the point where it just goes slack, and that is how you find the limit.

:::eg (Exam style) A smooth vertical rod has two points \(A\) and \(B\) on it, with \(A\) 0.3 m above the level of a particle \(P\) and \(B\) 0.3 m below that level. \(P\) has mass 0.6 kg and is joined to \(A\) and \(B\) by light inextensible strings each of length 0.5 m. \(P\) moves in a horizontal circle about the rod with both strings taut, with angular speed \(\omega\). Take \(g = 10\). (a) Find the tensions \(T_A\) and \(T_B\) when \(\omega = 10\). (b) Find the least \(\omega\) for which both strings are taut. [7 marks]
The radius is \(\sqrt{0.5^2 - 0.3^2} = 0.4\) m. [B1] Each string makes an angle \(\alpha\) with the vertical where \(\cos\alpha = 0.6\) and \(\sin\alpha = 0.8\).

**(a)** \(T_A\) pulls \(P\) up and inwards; \(T_B\) pulls \(P\) down and inwards. Vertically:
\[0.6T_A - 0.6T_B = 0.6 \times 10\quad\Rightarrow\quad T_A - T_B = 10\] [M1]
Horizontally, towards the rod:
\[0.8T_A + 0.8T_B = 0.6 \times 0.4 \times 100\] [M1 A1]
\[T_A + T_B = 30\]
Add and subtract: \(T_A = 20\) N and \(T_B = 10\) N. [A1]

**(b)** \(B\) goes slack when \(T_B = 0\). [M1] Then \(T_A = 10\) from the vertical equation, and the horizontal equation gives
\[0.8 \times 10 = 0.6 \times 0.4 \times \omega^2 \quad\Rightarrow\quad \omega^2 = 33.3\]
So \(\omega \ge 5.77\) rad s⁻¹ for both strings to be taut. [A1] For smaller values only \(AP\) is taut and the particle drops to a conical pendulum.
:::

:::board
Edexcel IAL and the UK A Levels use \(g = 9.8\) where 9231 uses \(g = 10\). Circular motion is part of Further Mathematics (Further Mechanics) in the UK boards, with the same formulas \(v = r\omega\) and \(a = r\omega^2 = \dfrac{v^2}{r}\).
:::

:::exam What MF19 gives you
MF19 gives the acceleration \(r\omega^2\) or \(\dfrac{v^2}{r}\) towards the centre. It does not give \(v = r\omega\), the period \(\dfrac{2\pi}{\omega}\) or the rpm conversion, so learn those. Say "towards the centre" in your equation, and give the angle \(\theta\) or the speed to 3 significant figures, as the paper's front page requires.
:::

:::eg Spot the error: a particle of mass 0.5 kg is attached by a light inextensible string of length 0.8 m to a fixed point. It moves in a horizontal circle with the string at \(30^\circ\) to the vertical. Find the speed. Take \(g = 10\). [4 marks]
A student wrote this answer.

Line 1: \(T\cos 30^\circ = 0.5 \times 10\), so \(T = 5.774\) N
Line 2: \(T\sin 30^\circ = \dfrac{0.5v^2}{0.8}\)
Line 3: \(2.887 = 0.625v^2\), so \(v^2 = 4.619\) and \(v = 2.15\) m s⁻¹

Line 1 is correct. [B1]

**The slip is the radius in line 2.** The student used the length of the string, but the radius is \(0.8\sin 30^\circ = 0.4\) m. The equation has the right form, so the method mark is earned. [M1] The accuracy mark is lost because the radius is wrong. [A0] The answer 2.15 follows from the wrong equation, so it earns no mark. [A0] The student scores 2 out of 4.

Correct line 2: \(2.887 = \dfrac{0.5v^2}{0.4} = 1.25v^2\) [A1], so \(v^2 = 2.309\) and \(v = 1.52\) m s⁻¹ [A1].

**Check** with \(\tan\theta = \dfrac{v^2}{rg}\): \(\dfrac{2.309}{0.4 \times 10} = 0.577 = \tan 30^\circ\). ✓
:::

:::try Start easy, finish at exam standard
Q: A particle moves in a circle of radius 0.5 m with angular speed 8 rad s⁻¹. Find its speed and its acceleration.
A: \(v = r\omega = 4\) m s⁻¹ and \(a = r\omega^2 = 0.5 \times 64 = 32\) m s⁻², directed towards the centre.
Q: A wheel turns at 300 revolutions per minute. Find its angular speed and its period.
A: \(\omega = \dfrac{300 \times 2\pi}{60} = 10\pi = 31.4\) rad s⁻¹. Period \(= \dfrac{2\pi}{\omega} = 0.2\) s.
Q: A car of mass 1000 kg travels round a flat circular bend of radius 50 m at 10 m s⁻¹. Find the friction force needed.
A: \(F = \dfrac{mv^2}{r} = \dfrac{1000 \times 100}{50} = 2000\) N.
Q: A particle of mass 0.2 kg on a smooth horizontal table moves in a circle of radius 0.4 m on a light string with period 2 s. Find the tension.
A: \(\omega = \pi\) rad s⁻¹, so \(T = mr\omega^2 = 0.2 \times 0.4 \times \pi^2 = 0.790\) N.
Q: A coin lies 0.2 m from the centre of a rough horizontal turntable (\(\mu = 0.5\)). Find the greatest angular speed without slipping. Take \(g = 10\).
A: \(\omega^2 = \dfrac{\mu g}{r} = \dfrac{5}{0.2} = 25\), so \(\omega = 5\) rad s⁻¹.
Q: A particle hangs on a string of length 1 m moving as a conical pendulum with angular speed 5 rad s⁻¹. Find the angle of the string to the vertical. Take \(g = 10\).
A: \(\cos\theta = \dfrac{g}{l\omega^2} = \dfrac{10}{25} = 0.4\), so \(\theta = 66.4^\circ\).
Q: A bend of radius 100 m is banked at \(\theta\) with \(\tan\theta = 0.2\). Find the speed at which no friction is needed. Take \(g = 10\).
A: \(v^2 = rg\tan\theta = 100 \times 10 \times 0.2 = 200\), so \(v = 14.1\) m s⁻¹.
Q: A particle moves in a horizontal circle on the inside of a smooth cone, with its axis vertical and vertex downwards, at a height of 0.8 m above the vertex. The semi-vertical angle of the cone is \(45^\circ\). Find the speed of the particle. Take \(g = 10\).
A: For a cone, \(v^2 = gh = 8\), so \(v = 2.83\) m s⁻¹.
Q: A particle of mass 0.3 kg is joined to a fixed point by an inextensible string of length 0.5 m, and moves in a horizontal circle with the string taut at \(60^\circ\) to the vertical. Find the tension. Take \(g = 10\).
A: \(T\cos 60^\circ = 3\), so \(T = 6\) N. Check: \(T = ml\omega^2\) gives \(\omega^2 = 40\), which is greater than \(\dfrac{g}{l} = 20\) as it must be.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A particle moves in a horizontal circle of radius 0.8 m with constant angular speed 6 rad s⁻¹. Find its speed and the magnitude of its acceleration.
A: \(v = r\omega = 0.8 \times 6\) [M1] \(= 4.8\) m s⁻¹. [A1]
\(a = r\omega^2 = 0.8 \times 36 = 28.8\) m s⁻². [A1]
Q: [4 marks] ★ A particle of mass 0.3 kg moves in a horizontal circle on a smooth table, on a light inextensible string of length 0.6 m, with speed 4 m s⁻¹. Find the tension in the string and the time for one revolution.
A: \(T = \dfrac{mv^2}{r} = \dfrac{0.3 \times 16}{0.6}\) [M1] \(= 8\) N. [A1]
\(\omega = \dfrac{4}{0.6} = 6.667\), so the period is \(\dfrac{2\pi}{\omega}\) [M1] \(= 0.942\) s. [A1]
Q: [5 marks] ★★ A coin of mass \(m\) lies on a rough horizontal turntable, 0.15 m from its centre. The coefficient of friction is 0.4. The turntable is made to rotate faster and faster. Find the angular speed at which the coin begins to slip, in rad s⁻¹ and in revolutions per minute. Take \(g = 10\).
A: \(R = mg\), so the greatest friction is \(0.4mg\). [B1]
\(0.4mg = m \times 0.15\,\omega^2\) [M1 A1]
\(\omega^2 = \dfrac{4}{0.15} = 26.67\), so \(\omega = 5.16\) rad s⁻¹. [A1]
\(\dfrac{5.164 \times 60}{2\pi} = 49.3\) rpm. [A1]
Q: [6 marks] ★★ A particle of mass 0.2 kg is attached to a fixed point by a light inextensible string of length 1.0 m. It moves in a horizontal circle with constant angular speed 6 rad s⁻¹. Find the tension in the string and the angle the string makes with the vertical. Take \(g = 10\).
A: Horizontally: \(T\sin\theta = 0.2 \times (1.0\sin\theta) \times 36\) [M1 A1], so \(T = 7.2\) N. [A1]
Vertically: \(T\cos\theta = 0.2 \times 10 = 2\) [M1], so \(\cos\theta = \dfrac{2}{7.2} = 0.2778\) [A1] and \(\theta = 73.9^\circ\). [A1]
Q: [5 marks] ★★ A car travels round a bend of radius 80 m at 20 m s⁻¹. The bend is banked at \(\theta\) to the horizontal so that no sideways friction is needed. Find \(\theta\). Take \(g = 10\).
A: \(R\cos\theta = mg\) [M1], \(R\sin\theta = \dfrac{mv^2}{r}\) [M1 A1]
\(\tan\theta = \dfrac{400}{80 \times 10} = 0.5\) [A1], so \(\theta = 26.6^\circ\). [A1]
Q: [9 marks] (#math.fm.elastic) ★★★ A particle \(P\) of mass 0.5 kg is attached to one end of a light elastic string of natural length 0.4 m and modulus of elasticity 10 N. The other end is attached to a fixed point \(O\) on a smooth horizontal table. \(P\) moves on the table in a circle with centre \(O\) and radius 0.6 m. (a) Find the tension. (b) Find the speed of \(P\). (c) The speed is increased so that the circle has radius 0.9 m. Find the new speed. (d) Find the increase in the total of the kinetic energy of \(P\) and the elastic energy in the string.
H: The extension is the radius minus the natural length, because the string lies along the radius.
H: The tension is the only horizontal force: \(T = \dfrac{mv^2}{r}\).
H: For (d) find the kinetic energy and the elastic energy at each radius and subtract.
A: (a) \(x = 0.6 - 0.4 = 0.2\) m, \(T = \dfrac{10 \times 0.2}{0.4}\) [M1] \(= 5\) N. [A1]
(b) \(5 = \dfrac{0.5v^2}{0.6}\) [M1], so \(v^2 = 6\) and \(v = 2.45\) m s⁻¹. [A1]
(c) \(x = 0.5\) m, so \(T = \dfrac{10 \times 0.5}{0.4} = 12.5\) N, and \(12.5 = \dfrac{0.5v^2}{0.9}\) [M1], so \(v^2 = 22.5\) and \(v = 4.74\) m s⁻¹. [A1]
(d) First radius: \(\tfrac12 \times 0.5 \times 6 = 1.5\) J of KE and \(\dfrac{10 \times 0.2^2}{0.8} = 0.5\) J of EPE, total 2 J. [M1]
Second radius: \(\tfrac12 \times 0.5 \times 22.5 = 5.625\) J and \(\dfrac{10 \times 0.5^2}{0.8} = 3.125\) J, total 8.75 J. [M1]
Increase: \(8.75 - 2 = 6.75\) J. [A1]
Q: [9 marks] (#math.m.forces) ★★★ A particle \(P\) of mass 0.5 kg is attached by two light inextensible strings to points \(A\) and \(B\) on a fixed vertical rod, with \(A\) above \(B\) and \(AB = 0.8\) m. \(AP = 1.0\) m and \(BP = 0.6\) m. \(P\) moves in a horizontal circle with both strings taut and constant angular speed \(\omega\). Take \(g = 10\). (a) Show that the tension in \(AP\) is 6.25 N and that \(BP\) is horizontal. (b) Find the tension in \(BP\) when \(\omega = 5\). (c) Find the least \(\omega\) for which both strings are taut.
H: Use the triangle \(ABP\): are the lengths 0.6, 0.8, 1.0 a familiar triple?
H: If \(BP\) is horizontal, only \(AP\) has a vertical component.
H: \(BP\) goes slack when its tension is zero.
A: (a) \(0.6^2 + 0.8^2 = 1.0^2\), so the angle at \(B\) is a right angle and \(BP\) is horizontal. [B1] \(AP\) makes angle \(\alpha\) with the vertical, \(\cos\alpha = \dfrac{0.8}{1.0}\). Vertically \(T_A\cos\alpha = mg = 5\) [M1], so \(T_A = 6.25\) N. [A1]
(b) The radius is 0.6 m. Horizontally, towards the rod: \(T_A\sin\alpha + T_B = mr\omega^2\) [M1 A1]
\(3.75 + T_B = 0.5 \times 0.6 \times 25 = 7.5\), so \(T_B = 3.75\) N. [A1]
(c) \(T_B = 0\) gives \(3.75 = 0.5 \times 0.6 \times \omega^2\) [M1], so \(\omega^2 = 12.5\) [A1] and \(\omega = 3.54\) rad s⁻¹. [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A particle \(P\) of mass 0.3 kg lies on a smooth horizontal table and is joined by a light inextensible string through a small smooth hole \(O\) in the table to a particle \(Q\) of mass 0.9 kg hanging below the table. \(P\) moves in a horizontal circle with centre \(O\), while \(Q\) hangs at rest. Take \(g = 10\). (a) Find the angular speed of \(P\) when the radius of its circle is 0.4 m. (b) Find the angular speed when the radius is 0.25 m. (c) Show that the time for one revolution is proportional to the square root of the radius.
H: \(Q\) is at rest, so the tension equals its weight. The same string passes through the hole, so the tension in \(P\)'s part is the same.
H: The tension is the only horizontal force on \(P\).
A: The tension is \(T = 0.9 \times 10 = 9\) N for \(Q\) at rest. [B1]
(a) \(9 = 0.3 \times 0.4 \times \omega^2\) [M1], so \(\omega^2 = 75\) and \(\omega = 8.66\) rad s⁻¹. [A1]
(b) \(9 = 0.3 \times 0.25 \times \omega^2\), so \(\omega^2 = 120\) and \(\omega = 11.0\) rad s⁻¹. [M1 A1]
(c) \(\omega^2 = \dfrac{T}{mr}\), so the period is \(\dfrac{2\pi}{\omega} = 2\pi\sqrt{\dfrac{mr}{T}}\) [M1] with \(m\) and \(T\) constant, so the period is proportional to \(\sqrt r\). [A1]
Q: [8 marks] ★★★ A particle \(P\) of mass \(m\) moves in a horizontal circle on the smooth inner surface of a hemispherical bowl of radius \(a\), with centre \(O\). The radius \(OP\) makes an angle \(\alpha\) with the downward vertical, and \(P\) moves with constant angular speed \(\omega\). (a) Show that \(\cos\alpha = \dfrac{g}{a\omega^2}\). (b) Deduce that \(P\) can only move in a horizontal circle above the lowest point if \(\omega^2 > \dfrac{g}{a}\). (c) Find \(\omega\) and the speed of \(P\) when \(a = 0.8\) m and \(\alpha = 45^\circ\). Take \(g = 10\).
H: The normal reaction \(R\) acts along \(PO\), towards the centre of the bowl, so it makes angle \(\alpha\) with the vertical.
H: The radius of the circle is \(a\sin\alpha\).
A: (a) Vertically: \(R\cos\alpha = mg\). Horizontally: \(R\sin\alpha = m(a\sin\alpha)\omega^2\). [M1 M1]
The second gives \(R = ma\omega^2\) [A1], and substituting in the first, \(ma\omega^2\cos\alpha = mg\), so \(\cos\alpha = \dfrac{g}{a\omega^2}\). [A1]
(b) \(\cos\alpha < 1\) for \(\alpha > 0\), so \(\dfrac{g}{a\omega^2} < 1\), that is \(\omega^2 > \dfrac{g}{a}\). [B1]
(c) \(\omega^2 = \dfrac{10}{0.8\cos 45^\circ} = 17.68\) [M1], so \(\omega = 4.20\) rad s⁻¹. [A1]
The radius is \(0.8\sin 45^\circ = 0.5657\) m, and \(v = r\omega = 2.38\) m s⁻¹. [A1]
:::

:::quiz
? A particle moves in a circle at constant speed. Which statement about its acceleration is correct?
+ It is directed towards the centre, with magnitude \(\dfrac{v^2}{r}\)
- It is zero, because the speed is constant
- It is directed along the tangent, in the direction of motion
- It is directed away from the centre, with magnitude \(\dfrac{v^2}{r}\)
> The velocity changes direction, so there is an acceleration, and it points towards the centre. A zero acceleration confuses constant speed with constant velocity. An outward acceleration is the "centrifugal" slip.
? A particle moves in a circle of radius 2 m at 6 m s⁻¹. What is its angular speed?
+ \(3\) rad s⁻¹
- \(12\) rad s⁻¹
- \(18\) rad s⁻¹
- \(\dfrac13\) rad s⁻¹
> \(\omega = \dfrac{v}{r} = 3\). The answer 12 multiplies instead of dividing, and \(\dfrac13\) inverts the formula.
? A coin on a rotating turntable just slips at angular speed \(\omega\). The coin is moved to twice the distance from the centre. At what angular speed does it now just slip?
- \(2\omega\)
- \(\omega\)
+ \(\dfrac{\omega}{\sqrt2}\)
- \(\dfrac{\omega}{2}\)
> \(\omega^2 = \dfrac{\mu g}{r}\), so doubling \(r\) divides \(\omega^2\) by 2 and \(\omega\) by \(\sqrt2\). The mass makes no difference, and halving \(\omega\) would need four times the radius.
? In a conical pendulum the string has length \(l\) and makes angle \(\theta\) with the vertical. What is the radius of the circle?
- \(l\)
- \(l\cos\theta\)
+ \(l\sin\theta\)
- \(l\tan\theta\)
> The radius is the horizontal distance from the vertical axis: \(l\sin\theta\). Using \(l\) is the commonest slip, and \(l\cos\theta\) is the depth of the particle below the fixed point.
? A car goes round a banked bend (no friction) at the design speed. Which pair of equations is correct?
+ \(R\cos\theta = mg\) and \(R\sin\theta = \dfrac{mv^2}{r}\)
- \(R = mg\) and \(R\sin\theta = \dfrac{mv^2}{r}\)
- \(R\sin\theta = mg\) and \(R\cos\theta = \dfrac{mv^2}{r}\)
- \(R\cos\theta = \dfrac{mv^2}{r}\) and \(R\sin\theta = mg\)
> The normal reaction is perpendicular to the track, at \(\theta\) to the vertical. Its vertical component balances the weight and its horizontal component provides the force towards the centre. The other pairs swap or drop a component.
? A particle is held in a horizontal circle by two strings to a vertical rod. As the angular speed is reduced from a large value, what happens to the tension in the lower string?
+ It falls to zero, and the string goes slack at a critical angular speed
- It increases
- It stays the same
- It becomes negative, so the string pushes
> The horizontal equation needs less force towards the rod as \(\omega\) falls, and the lower tension is the one that goes first. Strings can never push, so it stops at zero and the string goes slack.
:::

:::checklist What you can now do
- [ ] I can use angular speed \(\omega\), the relation \(v = r\omega\), the period and revolutions per minute.
- [ ] I can state and use the acceleration \(r\omega^2 = \dfrac{v^2}{r}\) towards the centre.
- [ ] I can find the resultant force towards the centre by resolving, and know there is no centrifugal force.
- [ ] I can solve problems on a rotating disc with friction, including the limiting angular speed.
- [ ] I can solve conical pendulum problems with an inextensible string and with an elastic string.
- [ ] I can solve problems of a particle moving in a horizontal circle inside a smooth cone or bowl.
- [ ] I can solve banked-track problems with and without friction, and find a range of speeds.
- [ ] I can solve problems with two strings to a vertical rod and find when one goes slack.
:::

:::recap
- \(v = r\omega\); period \(\dfrac{2\pi}{\omega}\); 1 rpm \(= \dfrac{2\pi}{60}\) rad s⁻¹.
- Constant speed in a circle: acceleration \(r\omega^2 = \dfrac{v^2}{r}\) towards the centre (MF19); the resultant force is \(mr\omega^2\). No centrifugal force.
- Resolve vertically (zero) and horizontally towards the centre (\(mr\omega^2\)).
- Radius is the distance from the vertical axis: \(l\sin\theta\) for a string of length \(l\).
- Conical pendulum: \(T\cos\theta = mg\), \(T = ml\omega^2\), \(\cos\theta = \dfrac{g}{l\omega^2}\). With an elastic string, the length is \(l + \dfrac{Tl}{\lambda}\).
- Rotating disc: friction at the limit, \(\mu g = r\omega^2\); the mass cancels.
- Smooth cone: \(v^2 = gh\). Banked track with no friction: \(\tan\theta = \dfrac{v^2}{rg}\); with friction, resolve horizontally and vertically, friction up or down the slope.
- A string goes slack when its tension reaches zero; that gives the limits of the angular speed.
:::

:::links
- watch: [Horizontal circles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NjtPvBrbfB1Ge-Tk6pCf4xQ) · ExamSolutions (YouTube) · worked examples of conical pendulums, discs and banked tracks
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · circular motion questions with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Paper 3 questions with mark schemes [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers sorted by year

Links checked 20 November 2026.
:::
Next: [Circular motion: vertical circles](#math.fm.vertical) is the case where the speed changes: energy and the radial equation together decide whether a particle completes its circle.
