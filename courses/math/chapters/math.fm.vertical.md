@chapter math.fm.vertical
@title Circular motion: vertical circles
@level fm
@paper CAIE 9231 Paper 3
@time 5–6 hours
@summary In a vertical circle gravity speeds a particle up on the way down and slows it on the way up, so its speed changes and a force towards the centre is needed at every moment. You will combine an energy equation with the radial equation to find the speed, the tension or reaction at any angle, where a string goes slack or a particle leaves a surface, and the conditions for a complete circle for a string, a rod, a tube and the inside or outside of a sphere.
:::why
A roller coaster loop, a stone swung on a string, a bucket whirled overhead and a skier going over the crest of a snowy dome are all vertical circles. The same question comes up every time: will the string stay taut, will the car stay on the track, will the particle stay on the surface? The answer is a simple condition on one force, and finding it takes two equations you already know.
:::

**Before you start**, you need the acceleration \(\dfrac{v^2}{r}\) towards the centre from [Circular motion: horizontal circles](#math.fm.circular), conservation of energy from [Work, energy and power](#math.m.energy), and resolving forces from [Forces and equilibrium](#math.m.forces). After the string goes slack the motion is that of [Projectiles](#math.fm.projectiles).

:::try Warm-up
Q: A particle of mass 0.5 kg moves in a horizontal circle of radius 0.4 m at 2 m s⁻¹. Find the resultant force on it. (from [Circular motion: horizontal circles](#math.fm.circular))
A: \(F = \dfrac{mv^2}{r} = \dfrac{0.5 \times 4}{0.4} = 5\) N, towards the centre.
Q: A smooth track descends 1.8 m from rest. Find the speed at the bottom. Take \(g = 10\). (from [Work, energy and power](#math.m.energy))
A: \(\tfrac12 v^2 = 10 \times 1.8\), so \(v^2 = 36\) and \(v = 6\) m s⁻¹.
Q: A particle of mass 2 kg hangs from a string making \(60^\circ\) with the vertical, held by a horizontal force. Find the tension. Take \(g = 10\). (from [Forces and equilibrium](#math.m.forces))
A: \(T\cos 60^\circ = 20\), so \(T = 40\) N.
:::

## Speed changes: the energy equation

On a horizontal circle the speed is constant. On a vertical circle it is not: the particle gains speed as it falls and loses speed as it rises. We assume no energy is lost, so mechanical energy is conserved ([Work, energy and power](#math.m.energy)), provided that the only forces that do work are gravity (the tension or reaction is at right angles to the motion and does no work).

To use the equations you need one angle convention. We measure the angle \(\theta\) at the centre \(O\) from the **downward** vertical, so the lowest point is \(\theta = 0\) and the highest is \(\theta = 180^\circ\).

:::html
<figure class="fig small"><svg viewBox="0 0 320 220" role="img" aria-label="A vertical circle with centre O of radius r and the lowest point A directly below O. A particle P is at angle theta from the downward vertical OA. At P: the tension T acts along PO towards the centre, the weight mg acts downwards with its component mg cos theta shown dashed along OP produced, and the velocity v is along the tangent. The height of P above A is marked h, equal to r minus r cos theta."><path class="ln-m thin dash" d="M80 110A80 80 0 1 0 240 110A80 80 0 1 0 80 110Z"/><path class="ln-m thin dash" d="M160 110V190"/><path class="ln-m thin dash" d="M221.3 161.4H70"/><path class="ln-m thin dash" d="M160 190H70"/><path class="c3" d="M160 110L221.3 161.4"/><circle class="f1 s-acc sw2" cx="221.3" cy="161.4" r="9"/><path class="c1 thick" d="M221.3 161.4L193.7 138.3" marker-end="url(#ah)"/><path class="c2 thick" d="M221.3 161.4V201.4" marker-end="url(#ah)"/><path class="c2 dash thick" d="M221.3 161.4L245.8 182" marker-end="url(#ah)"/><path class="c4 thick" d="M221.3 161.4L247 130.8" marker-end="url(#ah)"/><path class="ln thin" d="M160 132A22 22 0 0 0 176.9 124.1"/><path class="ln thin" d="M76 163V188" marker-end="url(#ah)"/><path class="ln thin" d="M76 188V163" marker-end="url(#ah)"/><circle class="f2 s-acc sw2" cx="160" cy="110" r="3"/><text class="tl" x="152" y="106" text-anchor="end">O</text><text class="tl" x="166" y="150">θ</text><text class="tl" x="200" y="132">T</text><text class="tl" x="208" y="196" text-anchor="end">mg</text><text class="tl" x="252" y="190">mg cosθ</text><text class="tl" x="252" y="128">v</text><text class="tl" x="66" y="180" text-anchor="end">h</text><text class="tl" x="190" y="212" text-anchor="end">A (lowest point)</text></svg><figcaption>The angle \(\theta\) is measured at \(O\) from the downward vertical \(OA\). The height of \(P\) above the lowest point is \(h = r - r\cos\theta = r(1 - \cos\theta)\). The component of the weight along \(PO\) produced is \(mg\cos\theta\), directed away from the centre.</figcaption></figure>
:::

The particle starts at \(A\) with speed \(u\) and rises \(h = r(1 - \cos\theta)\). Energy conservation gives the speed at angle \(\theta\):
\[\tfrac12 mv^2 + mgr(1 - \cos\theta) = \tfrac12 mu^2\]

:::key The energy equation (string, rod, inside a sphere)
\[v^2 = u^2 - 2gr(1 - \cos\theta)\]
At the top (\(\theta = 180^\circ\)), \(h = 2r\) and \(v^2 = u^2 - 4gr\). For motion **on the outside** of a sphere, measure \(\theta\) from the top instead, and the particle goes down: \(v^2 = u^2 + 2gr(1 - \cos\theta)\).
:::

## The radial equation

Now resolve along the line to the centre. The acceleration towards \(O\) is \(\dfrac{v^2}{r}\). For a particle on a string the tension \(T\) acts towards \(O\), and the component of the weight along \(PO\) is \(mg\cos\theta\), away from \(O\) when \(P\) is below the centre level (\(\theta < 90^\circ\)). So

\[T - mg\cos\theta = \frac{mv^2}{r}\]

The same equation holds for \(\theta > 90^\circ\) with \(\cos\theta\) negative: above the centre the weight has a component towards \(O\).

:::key The radial equation (towards the centre)
\[T - mg\cos\theta = \frac{mv^2}{r}\]
With the energy equation, eliminate \(v^2\):
\[T = m\left(\frac{u^2}{r} - 2g + 3g\cos\theta\right)\]
At the lowest point (\(\cos\theta = 1\)): \(T = m\left(\dfrac{u^2}{r} + g\right)\). At the highest point (\(\cos\theta = -1\)): \(T = m\left(\dfrac{u^2}{r} - 5g\right)\). For a particle on the inside of a sphere or tube, write \(R\) for \(T\): the same equations hold.
:::

:::steps
1. Draw the circle, the particle, and the angle \(\theta\) from the **downward** vertical at the centre.
2. Energy: write \(v^2 = u^2 - 2g \times (\text{height gained})\), with height gained \(= r(1 - \cos\theta)\) (or \(2r\) at the top).
3. Radial: forces towards the centre minus forces away \(= \dfrac{mv^2}{r}\). Include the weight component \(mg\cos\theta\) with the right sign.
4. Substitute \(v^2\), and solve for the unknown. For a "just" condition, set the force to 0 and solve.
:::

:::warn The two common slips
**Wrong height.** The height gained is \(r(1 - \cos\theta)\) from the lowest point, **not** \(r\cos\theta\) and not \(r\sin\theta\); at the top it is \(2r\), not \(r\). **Wrong vertical.** If your angle is measured from the upward vertical instead, \(\cos\theta\) changes sign in both equations. Fix one convention in your diagram and use it throughout.
:::

:::def Complete circular motion
Motion in which the particle goes all the way round the vertical circle, staying on its string, surface or wire throughout. For a string or the inside of a sphere that means the tension or reaction is never negative.
:::

:::def Thrust
A push along a rod (or spring) when it is compressed; it counts as a negative tension. A string can never provide one.
:::

## A particle on a string

A string can pull but never push. So the tension must satisfy \(T \ge 0\) all the way round. The tension is smallest at the top, so that is where the string goes slack first.

:::eg A particle of mass 0.5 kg is attached to one end of a light inextensible string of length 0.8 m. The other end is fixed at \(O\). The particle is held at rest at the lowest point and projected horizontally with speed 7 m s⁻¹. Find the speed and the tension (a) when the string makes \(60^\circ\) with the downward vertical, (b) at the highest point. Take \(g = 10\).
(a) The height gained is \(0.8(1 - \cos 60^\circ) = 0.4\) m.
\[v^2 = 49 - 2 \times 10 \times 0.4 = 41\]
So \(v = 6.40\) m s⁻¹. The radial equation:
\[T = m\left(\frac{v^2}{r} + g\cos\theta\right) = 0.5\left(\frac{41}{0.8} + 5\right) = 28.1\ \mathrm{N}\]
(b) At the top the height gained is \(2r = 1.6\) m:
\[v^2 = 49 - 32 = 17\]
At the top the weight acts towards the centre, so \(T + mg = \dfrac{mv^2}{r}\):
\[T = 0.5\left(\frac{17}{0.8} - 10\right) = 5.625\ \mathrm{N}\]
The speed is \(\sqrt{17} = 4.12\) m s⁻¹. The tension is positive, so the string is taut at the top. As \(T\) is least there, the string stays taut all the way round and the particle completes the circle.
:::

### The condition to complete the circle

The tension at the top is \(m\left(\dfrac{u^2}{r} - 5g\right)\). For it to be at least 0:

:::key Complete circle: string (or inside a sphere)
\[T_{\text{top}} \ge 0 \quad\Longleftrightarrow\quad u^2 \ge 5gr\]
At the top the speed then satisfies \(v^2 \ge gr\). With the limiting value \(u^2 = 5gr\), \(T_{\text{top}} = 0\) and \(v_{\text{top}}^2 = gr\). While the string stays taut, the tension at the bottom exceeds the tension at the top by \(6mg\), whatever \(u\) is: subtract \(m\left(\dfrac{u^2}{r} - 5g\right)\) from \(m\left(\dfrac{u^2}{r} + g\right)\).
:::

:::eg A particle on a light inextensible string of length 1.5 m moves in a vertical circle. Find the least speed at the lowest point for the particle to complete the circle, and the speed at the top in that case. Take \(g = 10\).
The least value has \(u^2 = 5gr = 5 \times 10 \times 1.5 = 75\), so \(u = 8.66\) m s⁻¹.
At the top, \(v^2 = u^2 - 4gr = 75 - 60 = 15 = gr\), so \(v = 3.87\) m s⁻¹.
Both are independent of the mass.
:::

### When the string goes slack

If \(u^2 < 5gr\) the string goes slack somewhere. The speed at the bottom then falls into one of three cases:

| Bottom speed | What happens |
|---|---|
| \(u^2 \ge 5gr\) | the particle completes the circle |
| \(2gr < u^2 < 5gr\) | the string goes slack above the level of \(O\) and the particle leaves the circle |
| \(u^2 \le 2gr\) | the particle rises no higher than \(O\) and swings back, with the string always taut |

For the middle case find the angle by setting \(T = 0\) in the formula:
\[0 = \frac{u^2}{r} - 2g + 3g\cos\theta \quad\Rightarrow\quad \cos\theta = \frac{2gr - u^2}{3gr}\]
At that point \(v^2 = -gr\cos\theta\) (from \(T = 0\) in the radial equation). The cosine is negative, so \(\theta > 90^\circ\). The swing-back case, \(u^2 \le 2gr\): the speed falls to zero at the angle with \(\cos\theta = 1 - \dfrac{u^2}{2gr}\), where the tension \(mg\cos\theta\) is still positive.

:::eg A particle of mass 0.4 kg is attached to a light inextensible string of length 1.2 m, and projected horizontally from the lowest point with speed 7 m s⁻¹. Show that the string goes slack, and find the angle with the downward vertical at which this happens, and the speed then. Take \(g = 10\).
The limit for a complete circle is \(u^2 = 5gr = 60\), but \(u^2 = 49 < 60\), and \(49 > 2gr = 24\), so the string goes slack above the level of \(O\).

At the slack point \(T = 0\): from the radial equation \(-mg\cos\theta = \dfrac{mv^2}{r}\), so \(v^2 = -gr\cos\theta = -12\cos\theta\).

Energy: \(v^2 = 49 - 2 \times 10 \times 1.2(1 - \cos\theta) = 25 + 24\cos\theta\).

Equate:
\[\begin{aligned}
-12\cos\theta &= 25 + 24\cos\theta \\
-36\cos\theta &= 25 \\
\cos\theta &= -\tfrac{25}{36}
\end{aligned}\]
So \(\theta = 134.0^\circ\) (3 s.f.), and \(v^2 = 12 \times \tfrac{25}{36} = 8.33\), so \(v = 2.89\) m s⁻¹.
:::

After the string goes slack, the only force is gravity, so the particle is a projectile with the velocity it had at the slack point, directed along the tangent to the circle. This is the link with [Projectiles](#math.fm.projectiles).

:::eg Continue the previous example. Find the greatest height above the lowest point that the particle reaches. Does it reach the top of the circle?
At the slack point the radius makes an angle \(\varphi\) with the **upward** vertical, where \(\cos\varphi = \tfrac{25}{36}\), so \(\sin\varphi = \sqrt{1 - \tfrac{625}{1296}} = 0.7195\). The tangent makes the same angle \(\varphi\) with the horizontal, so the vertical component of the velocity is
\[v\sin\varphi = 2.887 \times 0.7195 = 2.077\ \mathrm{m\,s^{-1}}\]
The further rise is \(\dfrac{2.077^2}{2 \times 10} = 0.2157\) m. The height of the slack point above the lowest point is \(1.2(1 - \cos\theta) = 1.2\left(1 + \tfrac{25}{36}\right) = 2.033\) m.

Greatest height \(= 2.033 + 0.216 = 2.25\) m. The top of the circle is at \(2r = 2.4\) m, so the particle does not reach it.
:::

:::eg (Exam style) A particle \(P\) of mass \(m\) is attached to one end of a light inextensible string of length \(a\). The other end is attached to a fixed point \(O\). \(P\) hangs at rest at the point \(A\) vertically below \(O\), and is projected horizontally with speed \(\sqrt{3ag}\). (a) When the string makes an angle \(\theta\) with the downward vertical, and is still taut, show that the tension is \(mg(1 + 3\cos\theta)\). (b) The string goes slack. Find the greatest height of \(P\) above \(A\) in the subsequent motion. [9 marks]
**(a)** \(P\) has risen \(a(1 - \cos\theta)\). Energy:
\[\tfrac12 mv^2 = \tfrac12 m(3ag) - mga(1 - \cos\theta)\] [M1]
\[v^2 = ag(1 + 2\cos\theta)\] [A1]
The component of the weight along the string, away from \(O\), is \(mg\cos\theta\). Towards \(O\):
\[T - mg\cos\theta = \frac{mv^2}{a}\] [B1]
\[T = mg\cos\theta + mg(1 + 2\cos\theta) = mg(1 + 3\cos\theta)\] [A1]

**(b)** The string goes slack when \(T = 0\):
\[1 + 3\cos\theta = 0 \quad\Rightarrow\quad \cos\theta = -\tfrac13\] [M1]
Then \(v^2 = ag\left(1 - \tfrac23\right) = \tfrac13 ag\). [A1]
The radius \(OP\) makes an angle \(\varphi\) with the **upward** vertical, where \(\cos\varphi = \tfrac13\) and \(\sin^2\varphi = \tfrac89\). The velocity is along the tangent, at \(\varphi\) to the horizontal, so the vertical component of the velocity satisfies
\[(v\sin\varphi)^2 = \frac{ag}{3} \times \frac89 = \frac{8ag}{27}\] [M1]
P then moves freely, and rises a further
\[\frac{(v\sin\varphi)^2}{2g} = \frac{4a}{27}\] [M1]
The slack point is \(a(1 - \cos\theta) = \tfrac43 a\) above \(A\), so the greatest height above \(A\) is
\[\frac{4a}{3} + \frac{4a}{27} = \frac{40a}{27}\] [A1]
:::

The widget lets you see all three cases. Slide \(u\) in String mode: the solid arc is the motion on the string, the dashed curve is the flight after the string goes slack. At \(u^2 = 5gr\) the tension at the top reaches zero, and above that the path closes up into a full circle.

:::html
<div class="widget" data-w="fm-vcircle" data-mode="string" data-u="6" data-r="1" data-m="0.5"></div>
:::

:::eg A particle on a light string of length 1 m has speed 4 m s⁻¹ at the lowest point. Find the greatest angle the string makes with the downward vertical. Take \(g = 10\).
\(u^2 = 16\), which is less than \(2gr = 20\), so the particle swings. It is at rest when \(\cos\theta = 1 - \dfrac{u^2}{2gr} = 1 - 0.8 = 0.2\), so \(\theta = 78.5^\circ\). The tension there is \(mg\cos\theta > 0\), so the string stays taut.
:::

## A particle on a rod, a bead on a ring, a particle in a tube

A **rod** (or a smooth tube, or a smooth circular wire with a bead on it) can push as well as pull. So the force in a rod, written as a tension \(T\) in the same equations, may be negative: a **thrust**. The radial equation \(T - mg\cos\theta = \dfrac{mv^2}{r}\) is the same, but now \(T\) is allowed to be negative.

The condition to complete the circle is only that the particle reaches the top, which needs \(v \ge 0\) there:
\[u^2 - 4gr \ge 0 \quad\Longleftrightarrow\quad u^2 \ge 4gr\]
With exactly \(u^2 = 4gr\) the particle just reaches the top with speed zero (and a thrust \(mg\) in the rod holding it up). If \(u^2 < 4gr\) the particle comes to rest at \(\cos\theta = 1 - \dfrac{u^2}{2gr}\) and swings back; unlike a string, a rod cannot go slack, so there is no free flight.

:::key String against rod
- **String**: needs \(T \ge 0\) at the top, so \(u^2 \ge 5gr\) and \(v_{\text{top}}^2 \ge gr\). Otherwise it goes slack above the centre.
- **Rod, tube, wire**: needs only \(v \ge 0\) at the top, so \(u^2 \ge 4gr\). The force can be a thrust.
- A particle on the **inside** of a sphere or ring behaves like a string (the surface can only push inwards); a bead or a particle in a **tube** behaves like a rod.
:::

:::eg A smooth circular wire of radius 0.6 m is fixed in a vertical plane. A bead of mass 0.2 kg is threaded on the wire and projected from the lowest point with speed 5 m s⁻¹. Find the speed at the top and the force the wire exerts there. Take \(g = 10\).
The bead reaches the top if \(u^2 \ge 4gr = 24\); \(u^2 = 25\), so it does.
\[v^2 = 25 - 4 \times 10 \times 0.6 = 1\]
At the top the weight acts towards the centre: \(T + mg = \dfrac{mv^2}{r}\), where \(T\) is the force on the bead towards the centre (down).
\[T = 0.2 \times \frac{1}{0.6} - 2 = -1.67\ \mathrm{N}\]
The negative sign means the wire pushes the bead **upwards**, away from the centre, with a force of 1.67 N. The speed at the top is 1 m s⁻¹.
:::

## Inside a smooth sphere or bowl

A particle moving on the **inside** of a smooth sphere is like a particle on a string: the surface can only push, so the reaction \(R \ge 0\) (acting towards the centre). It leaves the surface where \(R = 0\), and the conditions are the same as for a string: it completes the circle if \(u^2 \ge 5gr\), leaves the surface above the centre if \(2gr < u^2 < 5gr\), and slides back if \(u^2 \le 2gr\).

:::eg A particle is projected from the lowest point of the inside of a smooth hollow sphere of radius 0.5 m with speed 3 m s⁻¹. Show that it does not leave the surface, and find how high above the lowest point it rises. Take \(g = 10\).
\(u^2 = 9\) and \(2gr = 10\). Since \(u^2 < 2gr\) the particle comes to rest below the level of the centre, where the reaction is still positive, so it does not leave the surface. It rises \(h\) with
\[\tfrac12 \times 9 = 10h \quad\Rightarrow\quad h = 0.45\ \mathrm{m}\]
At that point \(\cos\theta = 1 - \dfrac{0.45}{0.5} = 0.1\), so the reaction is \(mg\cos\theta > 0\). Then it slides back down.
:::

:::eg (Exam style) A particle \(P\) of mass 0.3 kg is projected along the inside surface of a smooth hollow sphere with centre \(O\) and radius 0.8 m, starting from the lowest point \(A\) with speed 6 m s⁻¹. The sphere is fixed, and the part of the sphere above a horizontal plane 0.4 m above \(O\) is cut away, leaving a circular rim at \(B\). Take \(g = 10\). (a) Find the reaction at \(A\). (b) Show that \(P\) reaches \(B\) without leaving the surface, and find the reaction there. (c) After leaving the sphere at \(B\), \(P\) moves freely. Find the greatest height above \(A\) that \(P\) reaches.
**(a)** At \(A\) the reaction \(R\) is upwards and the weight downwards:
\[R - mg = \frac{mu^2}{r}\] [M1]
\[R = 0.3\left(\frac{36}{0.8} + 10\right) = 16.5\ \mathrm{N}\] [A1]
**(b)** \(B\) is \(0.8 + 0.4 = 1.2\) m above \(A\). Energy:
\[v^2 = 36 - 2 \times 10 \times 1.2\] [M1]
\[v^2 = 12\] [A1]
\(OB\) makes an angle \(\varphi\) with the upward vertical, where \(\cos\varphi = \dfrac{0.4}{0.8} = 0.5\). At \(B\), above the centre, the weight has a component \(mg\cos\varphi\) towards \(O\):
\[R + mg\cos\varphi = \frac{mv^2}{r}\] [M1]
\[R = 0.3\left(\frac{12}{0.8} - 5\right) = 3\ \mathrm{N}\] [A1]
The reaction decreases as \(P\) rises, and it is still positive at \(B\), so \(P\) stays on the surface all the way. [B1]
**(c)** At \(B\) the radius makes \(60^\circ\) with the vertical, so the tangent (the direction of motion) makes \(60^\circ\) with the horizontal. The vertical component of the velocity is
\[v\sin 60^\circ,\quad\text{so}\quad (v\sin 60^\circ)^2 = 12 \times \tfrac34 = 9\] [M1]
The further rise is \(\dfrac{9}{2 \times 10} = 0.45\) m. [M1]
Greatest height above \(A\): \(1.2 + 0.45 = 1.65\) m. [A1]
:::

:::eg (Exam style) A particle \(P\) of mass 0.3 kg is attached to one end of a light inextensible string of length 0.8 m. The other end is fixed at \(O\). \(P\) is projected horizontally from the lowest point with speed 8 m s⁻¹. Take \(g = 10\). (a) Find the tension in the string when \(P\) is at the lowest point, just after projection. (b) Show that the string remains taut when \(P\) is at the highest point, and find the tension there. (c) Find the least speed of projection for which \(P\) completes a vertical circle.
**(a)**
\[T - mg = \frac{mu^2}{r}\] [M1]
\[T = 0.3\left(\frac{64}{0.8} + 10\right) = 27\ \mathrm{N}\] [A1]
**(b)** At the top \(P\) has risen \(2r = 1.6\) m:
\[v^2 = 64 - 2 \times 10 \times 1.6\] [M1]
\[v^2 = 32\] [A1]
At the top the weight and the tension both act towards \(O\):
\[T + mg = \frac{mv^2}{r}\] [M1]
\[T = 0.3\left(\frac{32}{0.8} - 10\right) = 9\ \mathrm{N}\] [A1]
The tension is positive, so the string is taut at the top, and as it is least there, it is taut throughout. [B1]
**(c)** The string is just taut at the top when \(T = 0\), so \(v^2 = gr = 8\) there. [M1]
\[u^2 = 8 + 4gr = 8 + 32 = 40 \quad\Rightarrow\quad u = 6.32\ \mathrm{m\,s^{-1}}\] [A1]
:::

## On the outside of a sphere

Now the particle is on the **outside** of a smooth fixed sphere or dome, starting at the top. Gravity pulls it down the surface and so it speeds up, and the surface can only push it **away** from the centre. When the speed gets large enough the surface can no longer curve it round, and it leaves.

Measure \(\theta\) from the **upward** vertical (from the top). The particle has fallen \(r(1 - \cos\theta)\). If it starts at the top with speed \(u\):
\[v^2 = u^2 + 2gr(1 - \cos\theta)\]
Now the weight component \(mg\cos\theta\) points towards the centre and the reaction \(R\) away from it, so
\[mg\cos\theta - R = \frac{mv^2}{r}\]

:::key Leaving the outside of a sphere
\[R = m\left(3g\cos\theta - 2g - \frac{u^2}{r}\right)\]
The particle leaves the surface when \(R = 0\):
\[\cos\theta = \frac{u^2 + 2gr}{3gr}\]
Starting from rest at the top (or very nearly), \(\cos\theta = \tfrac23\) and the speed on leaving is \(v^2 = gr\cos\theta = \tfrac23 gr\). If the speed at the top satisfies \(u^2 \ge gr\), the formula gives \(\cos\theta \ge 1\): the particle leaves **at once**, at the top.
:::

:::eg A particle is placed at the top of a smooth fixed sphere of radius 1.5 m and projected horizontally with speed 1.5 m s⁻¹. Find the angle from the top at which it leaves the surface and its speed then. Take \(g = 10\).
\(u^2 = 2.25\) and \(gr = 15\), so \(u^2 < gr\) and the particle stays on the surface at first.
\[\cos\theta = \frac{2.25 + 30}{45} = 0.7167\]
So \(\theta = 44.2^\circ\). At that point \(R = 0\), so \(mg\cos\theta = \dfrac{mv^2}{r}\) and
\[v^2 = gr\cos\theta = 15 \times 0.7167 = 10.75\]
The speed on leaving is 3.28 m s⁻¹.
:::

:::html
<div class="widget" data-w="fm-vcircle" data-mode="outside" data-u="0.5" data-r="2" data-m="1"></div>
:::

The second widget shows a particle starting almost at rest at the top of a dome (radius 2 m). Slide the angle to see \(R\) fall to zero at 48.2°, and then press Play: the particle leaves the surface and follows a parabola to the ground.

:::eg (Exam style) A smooth solid hemisphere of radius 2 m is fixed with its plane face on horizontal ground. A particle \(P\) of mass 0.5 kg is placed at the highest point and slightly displaced, so that it moves from rest. Take \(g = 10\). (a) Show that \(P\) leaves the surface when \(\cos\theta = \tfrac23\), where \(\theta\) is the angle from the upward vertical. (b) Find its speed at that point. (c) Find the speed with which \(P\) hits the ground.
**(a)** Energy, starting from rest at the top:
\[v^2 = 2gr(1 - \cos\theta)\] [M1 A1]
At the point of leaving, \(R = 0\):
\[mg\cos\theta = \frac{mv^2}{r}\quad\Rightarrow\quad v^2 = gr\cos\theta\] [M1 A1]
\[\begin{aligned}
gr\cos\theta &= 2gr(1 - \cos\theta) \\
3\cos\theta &= 2
\end{aligned}\]
so \(\cos\theta = \tfrac23\). [A1]
**(b)** \(v^2 = gr\cos\theta = 10 \times 2 \times \tfrac23 = 13.3\), so \(v = 3.65\) m s⁻¹. [M1 A1]
**(c)** After leaving, only gravity acts, so energy is conserved from the top (a height 2 m above the ground) to the ground:
\[\tfrac12 \times 0.5 \times v^2 = 0.5 \times 10 \times 2\] [M1]
\[v^2 = 40 \quad\Rightarrow\quad v = 6.32\ \mathrm{m\,s^{-1}}\] [A1]
:::

:::board
Edexcel IAL and the UK A Levels use \(g = 9.8\) where 9231 uses \(g = 10\). Vertical circular motion is part of Further Mathematics (Further Mechanics) in the UK specifications; the condition \(u^2 \ge 5gr\) for a string and the energy and radial equations are the same.
:::

:::exam What to write
No formula for vertical circles is on MF19, but the acceleration \(\dfrac{v^2}{r}\) is. So the pattern is always the same: an energy equation (state the heights), then a radial equation with the weight component, then solve. A "show that" with a given answer needs both equations written out. For "just completes" set \(T = 0\) at the top (string) or \(v = 0\) at the top (rod). Give angles to 1 d.p. and speeds to 3 s.f.
:::

:::eg Spot the error: a particle of mass 0.2 kg is attached to a light inextensible string of length 0.5 m, and projected horizontally from the lowest point with speed 6 m s⁻¹. Find the tension in the string at the highest point. Take \(g = 10\). [4 marks]
A student wrote this answer.

Line 1: \(v^2 = 36 - 2 \times 10 \times 0.5 = 26\)
Line 2: \(T + mg = \dfrac{mv^2}{r}\), so \(T = 0.2\left(\dfrac{26}{0.5} - 10\right) = 8.4\) N

Line 1 is an energy equation of the right form, so the method mark is earned. [M1] **The slip is the height.** At the highest point the particle has risen \(2r = 1\) m, not \(r\). So \(v^2\) is wrong. [A0]

Line 2 is the correct radial equation for the top, and the student has used it properly with their own \(v^2\). [M1] The answer 8.4 N is wrong, because \(v^2\) was wrong. [A0] The student scores 2 out of 4.

Correct: \(v^2 = 36 - 20 = 16\) [A1], so \(T = 0.2\left(\dfrac{16}{0.5} - 10\right) = 4.4\) N [A1].

**Check** with the condition \(u^2 = 36 \ge 5gr = 25\): the string stays taut, and the tension is positive. ✓
:::

:::try Start easy, finish at exam standard
Q: A particle on a string of length 0.5 m is at the lowest point with speed 5 m s⁻¹. Find the speed when the string is horizontal. Take \(g = 10\).
A: Height gained \(= 0.5\) m, so \(v^2 = 25 - 10 = 15\) and \(v = 3.87\) m s⁻¹.
Q: A particle of mass 0.4 kg is at the lowest point of a circle of radius 0.5 m with speed 4 m s⁻¹, on a string. Find the tension. Take \(g = 10\).
A: \(T = m\left(\dfrac{u^2}{r} + g\right) = 0.4(32 + 10) = 16.8\) N.
Q: Find the least speed at the lowest point for a particle on a string of length 0.9 m to complete a vertical circle. Take \(g = 10\).
A: \(u^2 = 5gr = 45\), so \(u = 6.71\) m s⁻¹.
Q: Find the least speed at the lowest point for a bead on a smooth circular wire of radius 0.9 m to reach the top. Take \(g = 10\).
A: \(u^2 = 4gr = 36\), so \(u = 6\) m s⁻¹.
Q: A particle of mass 0.2 kg on a string of length 0.4 m is at the lowest point with speed 4.5 m s⁻¹. Find the tension when the string is horizontal. Take \(g = 10\).
A: \(v^2 = 20.25 - 8 = 12.25\), and at the horizontal \(\cos\theta = 0\), so \(T = \dfrac{mv^2}{r} = \dfrac{0.2 \times 12.25}{0.4} = 6.125\) N.
Q: A particle is at the lowest point of a string of length 0.8 m with speed \(\sqrt{12}\) m s⁻¹. Does it swing or does the string go slack? Take \(g = 10\).
A: \(u^2 = 12\) and \(2gr = 16\). Since \(u^2 < 2gr\) it swings, rising to \(\cos\theta = 1 - \dfrac{12}{16} = 0.25\), below the level of the centre.
Q: A particle at the top of a smooth fixed sphere of radius 0.9 m is given speed 2 m s⁻¹. Does it leave at once? Take \(g = 10\).
A: \(u^2 = 4\) and \(gr = 9\), so \(u^2 < gr\): it stays on the surface at first.
Q: A particle slides from rest at the top of a smooth sphere of radius 3 m. Find the speed when it leaves. Take \(g = 10\).
A: \(v^2 = \tfrac23 gr = 20\), so \(v = 4.47\) m s⁻¹.
Q: A smooth sphere of radius 1 m. A particle inside at the lowest point has speed \(\sqrt{50}\) m s⁻¹. Does it complete the circle? Take \(g = 10\).
A: \(u^2 = 50 = 5gr\). The reaction at the top is exactly zero, so it just completes the circle.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A particle of mass 0.4 kg is attached to one end of a light inextensible string of length 0.6 m, the other end fixed. It is projected from the lowest point with speed 5 m s⁻¹. Show that it cannot move in a complete vertical circle. Take \(g = 10\).
A: For a complete circle the tension at the top must be at least zero: \(T_{\text{top}} = m\left(\dfrac{u^2}{r} - 5g\right) \ge 0\). [M1]
This needs \(u^2 \ge 5gr = 30\). [A1]
\(u^2 = 25 < 30\), so the string goes slack before the top and the particle cannot complete the circle. [B1]
Q: [5 marks] ★ A particle of mass 0.5 kg is attached to a light inextensible string of length 0.4 m. It is projected horizontally from the lowest point with speed 6 m s⁻¹. Find (a) the tension at the lowest point, (b) the tension when the string is horizontal. Take \(g = 10\).
A: (a) \(T - mg = \dfrac{mu^2}{r}\) [M1], so \(T = 0.5(90 + 10) = 50\) N. [A1]
(b) \(v^2 = 36 - 2 \times 10 \times 0.4 = 28\) [M1 A1]. Horizontal string: \(T = \dfrac{mv^2}{r} = \dfrac{0.5 \times 28}{0.4} = 35\) N. [A1]
Q: [6 marks] ★★ A particle of mass 0.6 kg is attached to one end of a light rod of length 0.9 m, the other end of which is fixed. The particle is projected from the lowest point with speed \(u\). Take \(g = 10\). (a) Find the least value of \(u\) for the particle to reach the highest point. (b) When \(u = 6.5\), find the force in the rod at the highest point, stating whether it is a tension or a thrust.
A: (a) At the top \(v \ge 0\): \(u^2 \ge 4gr = 36\) [M1], so \(u \ge 6\) m s⁻¹. [A1]
(b) \(v^2 = 42.25 - 36 = 6.25\). [M1 A1]
\(T + mg = \dfrac{mv^2}{r}\) [M1], so \(T = \dfrac{0.6 \times 6.25}{0.9} - 6 = -1.83\): a thrust of 1.83 N. [A1]
Q: [7 marks] ★★ A particle of mass 0.4 kg is attached to a light inextensible string of length 0.9 m. It is projected from the lowest point with speed \(\sqrt{27}\) m s⁻¹. Show that the string becomes slack when the angle \(\theta\) between the string and the downward vertical satisfies \(\cos\theta = -\tfrac13\), and find the speed of the particle at that instant. Take \(g = 10\).
A: Energy: \(v^2 = 27 - 2 \times 10 \times 0.9(1 - \cos\theta) = 9 + 18\cos\theta\). [M1 A1]
When slack, \(T = 0\): \(-mg\cos\theta = \dfrac{mv^2}{r}\), so \(v^2 = -9\cos\theta\). [M1 A1]
\(9 + 18\cos\theta = -9\cos\theta\), so \(27\cos\theta = -9\) and \(\cos\theta = -\tfrac13\). [A1]
\(v^2 = 3\), so \(v = 1.73\) m s⁻¹. [M1 A1]
Q: [9 marks] (#math.m.energy) ★★★ A smooth circular tube of radius 0.6 m is fixed in a vertical plane. A particle \(P\) of mass 0.3 kg moves inside the tube. At the lowest point it has speed \(u\). Take \(g = 10\). (a) Find the least \(u\) for \(P\) to reach the highest point. (b) When \(u = 7\), find the speed of \(P\) at the highest point and the force exerted by the tube there, stating its direction. (c) Find the force exerted by the tube at the lowest point when \(u = 7\).
H: A tube can push both ways, so the condition at the top is only that the speed is not negative.
H: At the top, the force from the tube and the weight both point towards the centre when the tube pushes down.
H: At the bottom, the reaction is up and the weight is down.
A: (a) \(u^2 - 4gr \ge 0\), so \(u^2 \ge 24\) [M1], \(u \ge 4.90\) m s⁻¹. [A1]
(b) \(v^2 = 49 - 24 = 25\), so \(v = 5\) m s⁻¹. [M1 A1]
\(R + mg = \dfrac{mv^2}{r}\) [M1], so \(R = \dfrac{0.3 \times 25}{0.6} - 3 = 9.5\) N, directed downwards (towards the centre): the outer wall pushes the particle down. [A1] [B1]
(c) \(R - mg = \dfrac{mu^2}{r}\) [M1], so \(R = \dfrac{0.3 \times 49}{0.6} + 3 = 27.5\) N. [A1]
Q: [9 marks] (#math.m.energy) ★★★ A smooth solid hemisphere of radius 1.2 m is fixed with its plane face on horizontal ground. A particle \(P\) of mass 0.5 kg is projected horizontally from the highest point with speed 1 m s⁻¹. Take \(g = 10\). (a) Show that \(P\) leaves the surface when the angle \(\theta\) from the upward vertical satisfies \(\cos\theta = \tfrac{25}{36}\). (b) Find the speed of \(P\) when it leaves the surface. (c) Find the speed with which \(P\) hits the ground.
H: Energy from the top: \(v^2 = u^2 + 2gr(1 - \cos\theta)\).
H: The surface can only push away from the centre: it leaves when \(R = 0\).
H: After leaving only gravity acts, so use energy from the top to the ground.
A: (a) \(v^2 = 1 + 24(1 - \cos\theta)\) [M1 A1]. At the point of leaving \(R = 0\): \(mg\cos\theta = \dfrac{mv^2}{r}\), so \(v^2 = 12\cos\theta\). [M1 A1]
\(12\cos\theta = 25 - 24\cos\theta\), so \(\cos\theta = \tfrac{25}{36}\). [A1]
(b) \(v^2 = 12 \times \tfrac{25}{36} = 8.33\) [M1], so \(v = 2.89\) m s⁻¹. [A1]
(c) Energy from the top: \(v^2 = 1 + 2 \times 10 \times 1.2 = 25\) [M1], so \(v = 5\) m s⁻¹. [A1]
Q: [9 marks] (#math.fm.projectiles) ★★★ A particle of mass 0.4 kg is attached to a light inextensible string of length 0.8 m and projected horizontally from the lowest point with speed 6 m s⁻¹. Take \(g = 10\). (a) Show that the string goes slack when \(\cos\theta = -\tfrac56\), where \(\theta\) is the angle from the downward vertical. (b) Find the speed of the particle then. (c) Find the greatest height above the lowest point that the particle reaches.
H: Use \(T = 0\) in the radial equation, and the energy equation, as in the worked example.
H: The tangent at the slack point makes an angle with the horizontal equal to the angle of the radius with the vertical.
H: After the string goes slack the vertical motion is under gravity alone.
A: (a) Energy: \(v^2 = 36 - 16(1 - \cos\theta) = 20 + 16\cos\theta\) [M1 A1]. \(T = 0\): \(v^2 = -gr\cos\theta = -8\cos\theta\). [M1]
\(20 + 16\cos\theta = -8\cos\theta\), so \(\cos\theta = -\tfrac{20}{24} = -\tfrac56\). [A1]
(b) \(v^2 = 8 \times \tfrac56 = 6.67\) [M1], so \(v = 2.58\) m s⁻¹. [A1]
(c) The radius makes an angle \(\varphi\) with the upward vertical with \(\cos\varphi = \tfrac56\), so \(\sin^2\varphi = \tfrac{11}{36}\), and the vertical velocity component squared is \(6.667 \times \tfrac{11}{36} = 2.037\). [M1]
The further rise is \(\dfrac{2.037}{20} = 0.1019\) m. [M1]
The slack point is at height \(0.8\left(1 + \tfrac56\right) = 1.467\) m, so the greatest height is \(1.57\) m. [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A particle of mass \(m\) is attached to a light inextensible string of length \(r\) and projected from the lowest point with speed \(u\) so that the string goes slack when the radius makes an angle \(\alpha\) above the horizontal. The particle then moves freely and passes through the centre \(O\) of the circle. (a) Show that \(\sin\alpha\) satisfies \(u^2 = gr(2 + 3\sin\alpha)\). (b) Show that \(\tan^2\alpha = \tfrac12\). (c) Deduce the value of \(u^2\) in terms of \(gr\).
H: At the slack point, the radial equation gives \(v^2 = gr\sin\alpha\) (the component of the weight towards the centre is \(mg\sin\alpha\)).
H: The velocity is tangential: it makes angle \(\alpha\) with the vertical. Write the coordinates \((x, y)\) of the particle after time \(t\), taking \(O\) as the origin.
H: Use \(x = 0\) to find \(t\), then substitute into \(y = 0\).
A: (a) At the slack point the height above the lowest point is \(r + r\sin\alpha\). Energy: \(u^2 = v^2 + 2gr(1 + \sin\alpha)\). [M1] \(T = 0\): \(\dfrac{mv^2}{r} = mg\sin\alpha\), so \(v^2 = gr\sin\alpha\). [M1 A1] Then \(u^2 = gr\sin\alpha + 2gr + 2gr\sin\alpha = gr(2 + 3\sin\alpha)\). [A1]
(b) Take \(O\) as origin. The particle leaves at \((r\cos\alpha,\ r\sin\alpha)\) with velocity components \((-v\sin\alpha,\ v\cos\alpha)\). [B1] It reaches the vertical through \(O\) when \(r\cos\alpha - vt\sin\alpha = 0\), so \(t = \dfrac{r\cos\alpha}{v\sin\alpha}\). [M1]
At that time \(y = 0\): \(r\sin\alpha + vt\cos\alpha - \tfrac12 gt^2 = 0\). Substitute \(t\) and \(v^2 = gr\sin\alpha\):
\[r\sin\alpha + \frac{r\cos^2\alpha}{\sin\alpha} = \frac{r\cos^2\alpha}{2\sin^3\alpha}\]
Multiply by \(\dfrac{\sin^3\alpha}{r}\): \(\sin^4\alpha + \sin^2\alpha\cos^2\alpha = \tfrac12\cos^2\alpha\), so \(\sin^2\alpha = \tfrac12\cos^2\alpha\) and \(\tan^2\alpha = \tfrac12\). [A1]
(c) \(\sin^2\alpha = \dfrac{\tan^2\alpha}{1 + \tan^2\alpha} = \tfrac13\), so \(\sin\alpha = \dfrac{1}{\sqrt3}\), and \(u^2 = gr(2 + \sqrt3) = 3.73\,gr\). [A1]
Q: [7 marks] ★★★ A particle on a light inextensible string of length \(l\) is released from rest with the string horizontal. When the string is vertical it meets a smooth peg at a point a distance \(d\) vertically below the fixed point \(O\), and the particle then moves in a vertical circle about the peg. (a) Find the speed of the particle when the string is vertical. (b) Show that the string stays taut for the whole of the circle about the peg if \(d \ge \tfrac35 l\). (c) For \(l = 1\) m find the least \(d\) in metres.
H: After meeting the peg the radius of the circle is \(l - d\), and the particle is at the lowest point of that smaller circle.
H: Use the condition \(u^2 \ge 5gr\) with the new radius.
A: (a) The particle falls a height \(l\): \(v^2 = 2gl\). [M1 A1]
(b) The new radius is \(l - d\), and the particle is at the lowest point of the new circle with \(u^2 = 2gl\). [B1] It completes the circle if \(u^2 \ge 5g(l - d)\) [M1], so \(2l \ge 5(l - d)\) [A1] and \(5d \ge 3l\), that is \(d \ge \tfrac35 l\). [A1]
(c) \(d = 0.6\) m. [A1]
:::

:::quiz
? A particle on a string is at the lowest point of a vertical circle with speed \(u\). Which condition lets it complete the circle?
+ \(u^2 \ge 5gr\)
- \(u^2 \ge 4gr\)
- \(u^2 \ge 2gr\)
- \(u^2 \ge gr\)
> The tension at the top must be at least zero, which needs \(u^2 \ge 5gr\). The condition \(u^2 \ge 4gr\) is for a rod, which can push. \(u^2 \ge 2gr\) is where the particle gets above the centre, and \(u^2 \ge gr\) is the speed condition at the top, not at the bottom.
? What is the height gained by a particle on a circle of radius \(r\) when it reaches the highest point from the lowest?
- \(r\)
+ \(2r\)
- \(\pi r\)
- \(4r\)
> The highest point is a diameter above the lowest, so \(2r\). Using \(r\) is the commonest error in energy equations for vertical circles.
? A particle on a light rod is projected from the lowest point with \(u^2 = 4.5\,gr\). What happens?
+ It completes the circle, with the rod in thrust at the top
- The rod goes slack above the centre
- It swings back without reaching the top
- It completes the circle, with the rod in tension at the top
> \(u^2 > 4gr\) completes the circle for a rod. At the top \(v^2 = 0.5\,gr\), which is less than \(gr\), so the rod must push the particle outwards: a thrust. A string would go slack here (\(4.5\,gr < 5\,gr\)), but a rod cannot.
? A particle is released from rest at the top of a smooth fixed sphere. It leaves the surface when
- \(\cos\theta = \tfrac12\)
+ \(\cos\theta = \tfrac23\)
- \(\cos\theta = \tfrac13\)
- \(\theta = 90^\circ\)
> Energy gives \(v^2 = 2gr(1 - \cos\theta)\) and \(R = 0\) gives \(v^2 = gr\cos\theta\), so \(\cos\theta = \tfrac23\) (about 48.2°). The particle leaves well before reaching the horizontal.
? A particle on a string has speed \(v\) at a point where the string makes angle \(\theta\) with the **downward** vertical. Which radial equation is right?
+ \(T - mg\cos\theta = \dfrac{mv^2}{r}\)
- \(T + mg\cos\theta = \dfrac{mv^2}{r}\)
- \(T = mg\cos\theta\)
- \(T - mg\sin\theta = \dfrac{mv^2}{r}\)
> Measured from the downward vertical the weight component along the string is \(mg\cos\theta\) away from the centre, so it is subtracted from \(T\). The plus sign is for the angle measured from the upward vertical, and \(T = mg\cos\theta\) forgets the acceleration.
? A string of length \(r\) carries a particle with \(2gr < u^2 < 5gr\) at the lowest point. Which statement is true?
+ The string goes slack above the level of the centre and the particle then moves as a projectile
- The particle swings back below the level of the centre
- The particle completes the circle but with the string slack at the top
- The particle stops at the top
> In this range the particle rises above the centre but cannot reach the top; the tension falls to zero first, and the particle then moves freely under gravity. Swinging back is the case \(u^2 \le 2gr\).
:::

:::checklist What you can now do
- [ ] I can use energy conservation to find the speed of a particle at any point of a vertical circle, with the height \(r(1 - \cos\theta)\).
- [ ] I can write the radial equation \(T - mg\cos\theta = \dfrac{mv^2}{r}\) and find the tension or reaction at any angle.
- [ ] I can state and use the conditions for a complete circle: \(u^2 \ge 5gr\) for a string or the inside of a sphere, \(u^2 \ge 4gr\) for a rod or a tube.
- [ ] I can find where a string goes slack or a particle leaves a surface (the force is zero) and the speed there.
- [ ] I can follow a particle after it leaves the circle as a projectile.
- [ ] I can solve problems about a particle on the outside of a sphere, finding where it leaves.
- [ ] I can interpret a negative tension as a thrust, and compare reactions at different points.
:::

:::recap
- Energy (no losses): \(v^2 = u^2 - 2gr(1 - \cos\theta)\), with \(\theta\) from the downward vertical; the top is \(2r\) above the bottom.
- Radial: \(T - mg\cos\theta = \dfrac{mv^2}{r}\), so \(T = m\left(\dfrac{u^2}{r} - 2g + 3g\cos\theta\right)\); at the top \(T = m\left(\dfrac{u^2}{r} - 5g\right)\).
- String or inside of a sphere: complete circle if \(u^2 \ge 5gr\) (\(v_{\text{top}}^2 \ge gr\)); slack above the centre if \(2gr < u^2 < 5gr\), at \(\cos\theta = \dfrac{2gr - u^2}{3gr}\), with \(v^2 = -gr\cos\theta\); swings back if \(u^2 \le 2gr\).
- Rod, tube, wire: reaches the top if \(u^2 \ge 4gr\); the force can be a thrust (negative \(T\)).
- Outside of a sphere (from the top): \(v^2 = u^2 + 2gr(1 - \cos\theta)\); leaves at \(\cos\theta = \dfrac{u^2 + 2gr}{3gr}\); from rest \(\cos\theta = \tfrac23\); leaves at once if \(u^2 \ge gr\).
- After leaving, the particle is a projectile with the tangent velocity at the point of leaving.
:::

:::links
- watch: [Vertical circles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiWB2Brk-zazRkg-RvE_cJk) · ExamSolutions (YouTube) · string, rod and sphere cases worked step by step
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · vertical circle questions with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Paper 3 questions with mark schemes [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers sorted by year

Links checked 20 November 2026.
:::
Next: [Linear motion under a variable force](#math.fm.variable) moves on to forces that change with position, time or speed, solved with differential equations.
