@chapter math.fm.oblique
@title Oblique impact
@level fm
@paper CAIE 9231 Paper 3
@time 5–6 hours
@summary Most collisions are not head-on. When a smooth sphere hits a wall at an angle, or two smooth spheres meet off-centre, the force acts along only one line, so only the velocity components along that line change. You will resolve each velocity along and perpendicular to the line of impact, apply momentum and Newton's experimental law along the line, keep the perpendicular components, and find the speeds, directions, impulses and energy lost afterwards, including rebounds from two walls and a direct impact followed by an oblique one.

:::why
A cue ball that clips another ball sends it off at an angle, a football bounces off a post, a squash ball rebounds from two walls in turn. In every case the contact is smooth, so the push is along one line and the sideways motion carries straight on. That one fact turns a two-dimensional collision into the one-dimensional collision you already know how to solve, plus a component that does not change. It also explains why billiard balls leave at right angles to each other after a perfectly elastic collision.
:::

**Before you start**, you need Newton's experimental law, momentum and the coefficient of restitution from [Direct impact and restitution](#math.fm.impulse), resolving a vector into components from [Forces and equilibrium](#math.m.forces), and the trigonometry of angles and \(\tan\) from [Trigonometry](#math.p1.trig). The stretch problem drops a ball onto a slope, using constant acceleration from [Kinematics: describing motion](#math.m.kinematics).

:::try Warm-up
Q: A velocity of 12 m s⁻¹ makes an angle of 30° with the horizontal. Find its horizontal and vertical components. (from [Forces and equilibrium](#math.m.forces))
A: Horizontal: \(12\cos 30° = 10.4\) m s⁻¹. Vertical: \(12\sin 30° = 6\) m s⁻¹.
Q: A ball hits a wall directly at 8 m s⁻¹ with \(e = 0.5\). Find its speed after the impact. (from [Direct impact and restitution](#math.fm.impulse))
A: The speed after is \(eu = 0.5 \times 8 = 4\) m s⁻¹, away from the wall.
Q: A sphere of mass 2 kg at 6 m s⁻¹ hits a stationary sphere of mass 1 kg directly, with \(e = 1\). Find the velocity of the 1 kg sphere afterwards. (from [Direct impact and restitution](#math.fm.impulse))
A: \(v_B = \dfrac{m_1(1 + e)u}{m_1 + m_2} = \dfrac{2 \times 2 \times 6}{3} = 8\) m s⁻¹.
:::

## Oblique impact with a fixed surface

:::def Oblique impact
A collision in which the velocity of at least one of the bodies is not along the line of impact. The **line of impact** is the common normal at the point of contact: for a sphere and a plane wall it is the perpendicular to the wall; for two spheres it is the line of centres.
:::

In a direct impact the whole motion is along the line of impact. In an oblique impact each velocity has a component along that line and a component perpendicular to it. Because the surfaces are **smooth**, the contact force has no component perpendicular to the line of impact. So the two components behave differently.

:::key Smooth sphere hitting a fixed smooth wall
Resolve the velocity into a component **parallel to the wall** and a component **perpendicular to the wall** (along the normal).
- The parallel component is **unchanged**: there is no force along the wall.
- The perpendicular component is treated like a direct impact on the wall: it is **multiplied by \(e\) and reversed**.
\[v_{\parallel} = u_{\parallel} \qquad v_{\perp} = e\,u_{\perp}\]
The speed after is \(\sqrt{v_{\parallel}^2 + v_{\perp}^2}\), and the direction is found from the two components.
:::

If the sphere hits the wall at speed \(u\), making an angle \(\alpha\) with the wall, then \(u_\parallel = u\cos\alpha\) and \(u_\perp = u\sin\alpha\). After the impact it makes an angle \(\beta\) with the wall.

:::html
<figure class="fig small"><svg viewBox="0 0 340 190" role="img" aria-label="A smooth horizontal wall with a sphere hitting it at a point P. The incoming velocity u comes from upper left at angle alpha to the wall, and the outgoing velocity v leaves towards the upper right at a smaller angle beta. A dashed normal rises vertically from P. Dashed vertical lines mark the perpendicular components u sin alpha before and e u sin alpha after. Two dashed arrows under the wall show the parallel component u cos alpha, the same before and after."><path class="ln thick" d="M20 150H320"/><path class="ln-m thin" d="M30 150l-8 8M44 150l-8 8M58 150l-8 8M72 150l-8 8M86 150l-8 8M100 150l-8 8M114 150l-8 8M128 150l-8 8M142 150l-8 8M156 150l-8 8M170 150l-8 8M184 150l-8 8M198 150l-8 8M212 150l-8 8M226 150l-8 8M240 150l-8 8M254 150l-8 8M268 150l-8 8M282 150l-8 8M296 150l-8 8M310 150l-8 8"/><path class="ln-m thin dash" d="M170 150V40"/><path class="ln-m thin dash" d="M85.7 79.3V150"/><path class="ln-m thin dash" d="M254.3 107.6V150"/><path class="c1 thick" d="M85.7 79.3L170 150" marker-end="url(#ah)"/><path class="c2 thick" d="M170 150L254.3 107.6" marker-end="url(#ah)"/><path class="ln thin" d="M134 150A36 36 0 0 1 142.4 126.9"/><path class="ln thin" d="M209.3 130.2A44 44 0 0 1 214 150"/><path class="ln-m thin" d="M85.7 164H168" marker-end="url(#ahm)"/><path class="ln-m thin" d="M172 164H254" marker-end="url(#ahm)"/><text class="tl" x="136" y="104">u</text><text class="tl" x="200" y="114">v</text><text class="tl" x="116" y="142">α</text><text class="tl" x="221" y="142">β</text><text class="tl" x="80" y="118" text-anchor="end">u sin α</text><text class="tl" x="260" y="132">e u sin α</text><text class="tl" x="176" y="50">normal</text><text class="tl" x="128" y="180" text-anchor="middle">u cos α</text><text class="tl" x="212" y="180" text-anchor="middle">u cos α</text></svg><figcaption>A smooth sphere hits a fixed wall at speed \(u\), at angle \(\alpha\) to the wall, and leaves at speed \(v\) and angle \(\beta\). The component along the wall, \(u\cos\alpha\), is the same before and after. The component along the normal changes from \(u\sin\alpha\) to \(eu\sin\alpha\) and reverses. The picture is not to scale.</figcaption></figure>
:::

:::eg (Exam style) A smooth sphere hits a fixed smooth plane wall with speed \(u\) at an angle \(\alpha\) to the wall. The coefficient of restitution is \(e\). Show that the sphere rebounds at an angle \(\beta\) to the wall with \(\tan\beta = e\tan\alpha\), and with speed \(u\sqrt{\cos^2\alpha + e^2\sin^2\alpha}\).
The wall is smooth, so there is no impulse parallel to it, and the component of velocity parallel to the wall is unchanged: \(u\cos\alpha\). [B1]
Newton's experimental law for the component perpendicular to the wall (the approach speed is \(u\sin\alpha\)):
\[v_\perp = eu\sin\alpha\] [M1]
The angle \(\beta\) is found from the two components after the impact:
\[\tan\beta = \frac{v_\perp}{v_\parallel} = \frac{eu\sin\alpha}{u\cos\alpha}\] [M1]
\[\tan\beta = e\tan\alpha\] [A1]
Speed:
\[v = \sqrt{u^2\cos^2\alpha + e^2u^2\sin^2\alpha} = u\sqrt{\cos^2\alpha + e^2\sin^2\alpha}\] [A1]
:::

The result \(\tan\beta = e\tan\alpha\) shows at once how the angle changes. Since \(e \le 1\), \(\tan\beta \le \tan\alpha\), so \(\beta \le \alpha\): the sphere leaves **closer to the wall** than it arrived, unless \(e = 1\), when \(\beta = \alpha\) (the familiar mirror reflection). If \(e = 0\), \(\beta = 0\): the sphere slides along the wall.

:::key Rebound from a fixed wall
For speed \(u\) at angle \(\alpha\) to the wall, with coefficient of restitution \(e\):
\[\tan\beta = e\tan\alpha \qquad v = u\sqrt{\cos^2\alpha + e^2\sin^2\alpha}\]
Impulse of the wall on the sphere: \(m(1 + e)u\sin\alpha\), perpendicular to the wall. Kinetic energy lost: \(\tfrac12mu^2(1 - e^2)\sin^2\alpha\).
:::

:::warn Angle with the wall, or with the normal?
Check which angle the question gives. If it says "at an angle \(\alpha\) to the wall", the parallel component is \(u\cos\alpha\) and the perpendicular one is \(u\sin\alpha\). If it says "at an angle \(\theta\) to the normal" the two swap: parallel is \(u\sin\theta\), perpendicular is \(u\cos\theta\). A neat sketch with the components marked prevents the swap, and \(\tan\beta = e\tan\alpha\) only holds for angles measured from the wall.
:::

:::eg A smooth sphere of mass 0.5 kg hits a fixed smooth wall at 20 m s⁻¹, at 30° to the wall. The coefficient of restitution is 0.6. Find (a) the speed of the sphere after the impact, (b) the angle at which it leaves the wall, (c) the impulse of the wall on the sphere, (d) the kinetic energy lost.
Parallel to the wall: \(20\cos 30° = 17.32\) m s⁻¹, unchanged. Perpendicular before: \(20\sin 30° = 10\) m s⁻¹. After: \(0.6 \times 10 = 6\) m s⁻¹, away from the wall.

**(a)** Speed \(= \sqrt{17.32^2 + 6^2} = \sqrt{300 + 36} = \sqrt{336} = 18.3\) m s⁻¹ (3 s.f.).

**(b)** \(\tan\beta = \dfrac{6}{17.32}\), so \(\beta = 19.1°\) to the wall.

**(c)** The impulse is perpendicular to the wall, with magnitude \(m(v_\perp + u_\perp) = 0.5 \times (6 + 10) = 8\) N s.

**(d)** \(\text{KE lost} = \tfrac12 \times 0.5 \times (20^2 - 336) = 0.25 \times 64 = 16\) J.

Check with the formula: \(\tfrac12(0.5)(400)(1 - 0.36)(0.25) = 16\) J.
:::

Try the widget in "Sphere and wall" mode. Slide \(e\) from 0 to 1 and watch the outgoing arrow lean from "along the wall" to "mirror image"; the dashed horizontal component never changes.

:::html
<div class="widget" data-w="fm-impact" data-mode="wall" data-u="5" data-angle="40" data-e="0.6" data-m="1" data-components="on"></div>
:::

:::proof Why the perpendicular component is multiplied by \(e\)
Newton's experimental law was stated for a direct impact. For a smooth sphere the contact force acts along the normal only, so, with axes along and perpendicular to the wall:
1. In the direction along the wall, no force acts, so by \(F = ma\) the velocity component along the wall does not change during the impact.
2. In the direction of the normal, the sphere's motion is exactly that of a direct impact with a wall, because nothing else acts along that line.
3. For a direct impact the law says (speed of separation) \(= e \times\) (speed of approach).
4. So the component along the normal after the impact is \(e\) times the component before, reversed.
5. The two components then combine to give the new velocity: it is not \(e\) times the old velocity, because only one component is scaled.
The law for oblique impact is therefore a statement about the **component along the normal**, and the syllabus uses it in exactly that form.
:::

:::warn Do not apply \(e\) to the whole velocity
\(v = eu\) is true only when the sphere hits the wall **directly** (\(\alpha = 90°\)). In an oblique impact only the perpendicular component is multiplied by \(e\). Writing "speed after \(= e \times\) speed before" scores nothing: the speed after is \(u\sqrt{\cos^2\alpha + e^2\sin^2\alpha}\), always greater than \(eu\) unless the impact is direct.
:::

### Two walls: a particle in a corner

When a particle hits one barrier and then another, treat the impacts one after the other. The velocity after the first impact is the velocity before the second, and the angle with the second barrier depends on how the barriers are placed. The simplest case is two walls at right angles.

:::eg A smooth ball moves on a smooth horizontal floor in a corner formed by two vertical walls at right angles. It hits the first wall at 10 m s⁻¹, its path making an angle of 30° with that wall. It then hits the second wall. The coefficients of restitution with the first and second walls are 0.8 and 0.5. Find the speed of the ball after the second impact.
Take axes along the first wall (\(x\)) and perpendicular to it (\(y\)). Before the first impact the velocity components are \(u_x = 10\cos 30° = 8.660\) (along the wall) and \(u_y = 10\sin 30° = 5\) (towards the wall).

First wall: the component along the wall is unchanged; the component towards the wall becomes \(-0.8 \times 5 = -4\). So the velocity is \((8.660, -4)\).

The second wall is perpendicular to the first, so its normal is along \(x\). The component along \(x\) is perpendicular to the second wall and becomes \(-0.5 \times 8.660 = -4.330\). The component along \(y\) is parallel to the second wall and is unchanged: \(-4\).

The velocity after the second impact is \((-4.330, -4)\), a speed of
\[\sqrt{4.330^2 + 4^2} = \sqrt{18.75 + 16} = 5.89\ \text{m s}^{-1}\]
Notice what happened to the direction: the ball is now moving backwards (\(x\) reversed) and still away from the wall it first hit (\(y\) reversed). If the two coefficients had been equal, both components would have been multiplied by \(-e\), and the ball would leave **parallel to its original path**, in the opposite direction, at speed \(eu\).
:::

For walls that are not perpendicular the angles need a sketch. The next example is in the style of a real question: a barrier, a given loss of energy, and then a second barrier at 120° to the first.

:::html
<figure class="fig small"><svg viewBox="0 0 340 195" role="img" aria-label="Two smooth barriers meeting at O with an angle of 120 degrees between them. Barrier 1 runs horizontally to the left of O; barrier 2 runs from O up and to the right. A particle moves down and to the right, hits barrier 1 at P at angle alpha, rebounds up and to the right and hits barrier 2 at Q. The angle OPQ is the angle beta between the rebound path and barrier 1."><path class="ln thick" d="M30 170H250"/><path class="ln thick" d="M250 170L325 40.1"/><path class="c1 thick" d="M165 92.1L210 170" marker-end="url(#ah)"/><path class="c2 thick" d="M210 170L290 100.7" marker-end="url(#ah)"/><path class="ln thin" d="M182 170A28 28 0 0 1 196 145.8"/><path class="ln thin" d="M222 170A28 28 0 0 1 264 145.8"/><circle class="f2 s-acc sw2" cx="210" cy="170" r="3"/><circle class="f2 s-acc sw2" cx="290" cy="100.7" r="3"/><text class="tl" x="166" y="162">α</text><text class="tl" x="227" y="128" text-anchor="middle">120°</text><text class="tl" x="256" y="186">O</text><text class="tl" x="204" y="186">P</text><text class="tl" x="298" y="106">Q</text><text class="tl" x="40" y="186">barrier 1</text><text class="tl" x="304" y="44" text-anchor="end">barrier 2</text><text class="tl" x="160" y="86" text-anchor="end">u</text></svg><figcaption>A particle hits barrier 1 at \(P\), at angle \(\alpha\) to the barrier, rebounds and hits barrier 2 at \(Q\). The barriers meet at \(O\) at 120°. The angle \(OPQ\) is the rebound angle \(\beta\), so in triangle \(OPQ\) the angle at \(Q\), between the path and barrier 2, is \(180° - 120° - \beta = 60° - \beta\). The picture is not to scale.</figcaption></figure>
:::

:::eg (Exam style) A particle \(P\) moves on a smooth horizontal table and strikes a fixed smooth vertical barrier 1 at speed \(u\), at an angle of 60° to the barrier. The coefficient of restitution between \(P\) and any barrier is \(e\), and \(P\) loses \(\tfrac{9}{16}\) of its kinetic energy in this impact. (a) Find the value of \(e\). \(P\) then travels to a second smooth vertical barrier 2, which meets barrier 1 at an angle of 120° as in the figure. (b) Find the angle that the path of \(P\) makes with barrier 2 just before it hits it. (c) Find the speed of \(P\) after the impact with barrier 2, in terms of \(u\).
**(a)** Before the impact the components are \(u\cos 60° = \tfrac12u\) (parallel) and \(u\sin 60° = \tfrac{\sqrt3}{2}u\) (perpendicular). After the impact, the perpendicular one is multiplied by \(e\):
\[v^2 = \tfrac14u^2 + e^2\left(\tfrac34u^2\right)\] [M1 A1]
The energy after is \(\tfrac{7}{16}\) of the energy before, so \(v^2 = \tfrac{7}{16}u^2\):
\[\frac14 + \frac34e^2 = \frac{7}{16}\] [M1]
\[e^2 = \frac14, \qquad e = \frac12\] [A1]
**(b)** The rebound angle is given by \(\tan\beta = e\tan 60° = \tfrac{\sqrt3}{2}\), so \(\beta = 40.9°\). [M1 A1]
In triangle \(OPQ\) the angle at \(O\) is 120° and the angle at \(P\) is \(\beta\), so the angle at \(Q\) is \(180° - 120° - 40.9° = 19.1°\). [A1]
**(c)** The speed before the second impact is \(v_1 = \tfrac{\sqrt7}{4}u\) from (a). The path makes the angle \(\varphi = 19.1°\) with barrier 2, where \(\tan\varphi = \dfrac{\sqrt3}{5}\), so \(\cos^2\varphi = \dfrac{25}{28}\) and \(\sin^2\varphi = \dfrac{3}{28}\). The component parallel to barrier 2 is unchanged and the perpendicular one is multiplied by \(\tfrac12\):
\[v_2^2 = v_1^2\left(\cos^2\varphi + \tfrac14\sin^2\varphi\right)\] [M1]
\[v_2^2 = \frac{7}{16}u^2 \times \frac{25 + \frac34}{28} = \frac{103}{256}u^2\] [M1]
\[v_2 = \frac{\sqrt{103}}{16}u = 0.634u\] [A1]
:::

## Oblique impact of two smooth spheres

Two smooth spheres touch at one point, and the contact force acts along the line joining their centres, the **line of centres**. Take that line as one axis, from the centre of \(A\) towards the centre of \(B\), and the common tangent at the point of contact (perpendicular to it) as the other.

:::html
<figure class="fig small"><svg viewBox="0 0 290 185" role="img" aria-label="Two touching spheres A and B on a horizontal line of centres, with a vertical common tangent at the point of contact. Sphere A moves up and to the right with velocity u at angle theta to the line of centres. Its components are shown dashed: u cos theta along the line of centres and u sin theta perpendicular to it. Sphere B is at rest."><path class="ln-m thin dash" d="M14 100H270"/><path class="ln-m thin dash" d="M174 56V128"/><circle class="f1 s-acc sw2" cx="150" cy="100" r="24"/><circle class="f2 s-acc sw2" cx="198" cy="100" r="24"/><path class="c1 thick" d="M63.4 150L150 100" marker-end="url(#ah)"/><path class="ln-m thin dash" d="M63.4 150H148" marker-end="url(#ahm)"/><path class="ln-m thin dash" d="M150 148V114" marker-end="url(#ahm)"/><path class="ln thin" d="M103.4 150A40 40 0 0 0 98 130"/><text class="tl" x="134" y="93" text-anchor="middle">A</text><text class="tl" x="206" y="104" text-anchor="middle">B</text><text class="tl" x="100" y="115" text-anchor="end">u</text><text class="tl" x="108" y="140">θ</text><text class="tl" x="106" y="166" text-anchor="middle">u cos θ</text><text class="tl" x="157" y="147">u sin θ</text><text class="tl" x="14" y="94">line of centres</text><text class="tl" x="180" y="60">common tangent</text></svg><figcaption>At the moment of impact, \(A\) arrives with speed \(u\) at angle \(\theta\) to the line of centres, and \(B\) is at rest. Along the line of centres the collision is direct, with approach speed \(u\cos\theta\). Perpendicular to it nothing acts, so \(u\sin\theta\) is unchanged for \(A\), and \(B\) has no perpendicular component. The picture is not to scale.</figcaption></figure>
:::

:::key Oblique impact of two smooth spheres
Resolve both velocities along the line of centres (from \(A\) to \(B\)) and perpendicular to it.
- **Perpendicular to the line of centres**: each sphere's component is unchanged.
- **Along the line of centres**: the collision is direct. Use conservation of momentum and Newton's experimental law with the components along the line:
\[\begin{aligned}
m_1u_1 + m_2u_2 &= m_1v_1 + m_2v_2 \\
v_2 - v_1 &= e(u_1 - u_2)
\end{aligned}\]
Here \(u_1, u_2, v_1, v_2\) are the components along the line of centres, not the speeds.
- Combine the two components of each sphere to find its speed and direction after the impact. The impulse acts along the line of centres.
:::

:::steps
1. Sketch the spheres at the moment of impact, with the line of centres and the common tangent. Mark the velocity of each sphere before the impact.
2. Resolve every velocity into a component along the line of centres and a component perpendicular to it. Check the angles: are they measured from the line of centres or from the tangent?
3. Write the momentum equation and the Newton's law equation for the components along the line, and solve for \(v_1\) and \(v_2\).
4. Write down the perpendicular components, which have not changed.
5. Find each speed with Pythagoras and each direction with \(\tan^{-1}\) of (perpendicular \(\div\) along). Give angles to 1 d.p.
6. Use the components along the line only for the impulse and for the kinetic energy lost: \(\dfrac{m_1m_2(1 - e^2)}{2(m_1 + m_2)}(u_1 - u_2)^2\).
:::

:::warn Momentum is conserved along the line of centres, not along the original direction
The momentum of the pair is conserved in every direction, but perpendicular to the line of centres each sphere simply keeps its own component, so there is nothing to solve there. Use the momentum equation for the components along the line of centres, and apply Newton's experimental law to those components, never to the speeds.
:::

:::eg A smooth sphere \(A\) of mass 2 kg moves at 10 m s⁻¹ and collides with a stationary smooth sphere \(B\) of mass 3 kg. At the instant of impact the velocity of \(A\) makes an angle of 30° with the line of centres. The coefficient of restitution is 0.5. Find (a) the speeds and directions of \(A\) and \(B\) after the impact, (b) the kinetic energy lost, (c) the impulse of \(A\) on \(B\).
Components of \(A\) before the impact: along the line of centres \(10\cos 30° = 8.660\); perpendicular \(10\sin 30° = 5\). \(B\) is at rest.

**(a)** Along the line of centres:
\[\begin{aligned}
2 \times 8.660 &= 2v_1 + 3v_2 \\
v_2 - v_1 &= 0.5 \times 8.660 = 4.330
\end{aligned}\]
Substitute \(v_2 = v_1 + 4.330\): \(17.32 = 5v_1 + 12.99\), so \(v_1 = 0.866\) and \(v_2 = 5.196\).

\(B\) has no perpendicular component, so it moves along the line of centres at **5.20 m s⁻¹**.

\(A\) keeps its perpendicular component, 5 m s⁻¹. Its speed is \(\sqrt{0.866^2 + 5^2} = 5.07\) m s⁻¹, at an angle \(\tan^{-1}\dfrac{5}{0.866} = 80.2°\) to the line of centres.

**(b)** Before: \(\tfrac12(2)(100) = 100\) J. After: \(\tfrac12(2)(0.75 + 25) + \tfrac12(3)(27) = 25.75 + 40.5 = 66.25\) J. Lost: **33.75 J**. Check: \(\dfrac{2 \times 3 \times 0.75}{2 \times 5}(8.660)^2 = 33.75\) J.

**(c)** The impulse is the change of momentum of \(B\), along the line of centres: \(3 \times 5.196 = 15.6\) N s.
:::

Try the widget in "Two spheres" mode: it starts with this example. Change the direction of \(A\) and see that \(B\) always leaves along the line of centres, while the perpendicular components of both spheres stay the same.

:::html
<div class="widget" data-w="fm-impact" data-mode="spheres" data-m1="2" data-m2="3" data-u1="10" data-angle1="30" data-u2="0" data-angle2="0" data-e="0.5"></div>
:::

:::eg (Exam style) Two identical smooth spheres \(A\) and \(B\) lie on a smooth horizontal table, with \(B\) at rest. \(A\) moves with speed \(u\) and collides with \(B\). At the instant of impact the velocity of \(A\) makes an angle \(\theta\) with the line of centres. The collision is perfectly elastic. Show that after the collision the spheres move in directions that are at right angles to each other, and find their speeds.
Let the mass of each sphere be \(m\). The components along the line of centres before the impact are \(u\cos\theta\) for \(A\) and 0 for \(B\). The perpendicular components are \(u\sin\theta\) for \(A\) and 0 for \(B\), and they do not change. [B1]

Along the line of centres:
\[mu\cos\theta = mv_A + mv_B\] [M1]
\[v_B - v_A = 1 \times u\cos\theta\] [M1]
Adding the two equations gives \(2v_B = 2u\cos\theta\), so \(v_B = u\cos\theta\) and \(v_A = 0\). [A1]
So \(B\) moves along the line of centres with speed \(u\cos\theta\), and \(A\) has no component along the line, only its perpendicular component, so it moves perpendicular to the line of centres with speed \(u\sin\theta\). The directions are at right angles. [A1]
:::

The result is the reason that billiard balls leave at right angles when a cue ball clips another of equal mass. It fails when \(e < 1\) or when the masses differ.

:::eg (Exam style) Two identical smooth spheres \(A\) and \(B\) of equal mass are on a smooth horizontal table, with \(B\) at rest. \(A\) moves with speed \(u\) and at the instant of impact its velocity makes an angle of 30° with the line of centres. After the impact the direction of motion of \(A\) makes an angle of 60° with the line of centres. Show that the coefficient of restitution is \(\tfrac13\).
The perpendicular component of \(A\) is unchanged: \(u\sin 30° = \tfrac12u\). [B1]

Along the line of centres, with \(u\cos 30° = \tfrac{\sqrt3}{2}u\):
\[\tfrac{\sqrt3}{2}u = v_A + v_B\] [M1]
\[v_B - v_A = e\tfrac{\sqrt3}{2}u\] [M1]
Subtracting the second equation from the first gives \(2v_A = \tfrac{\sqrt3}{2}u(1 - e)\), so
\[v_A = \frac{\sqrt3}{4}(1 - e)u\] [A1]
The direction of \(A\) after the impact is given by the ratio of the perpendicular to the along-the-line component:
\[\tan 60° = \frac{\tfrac12u}{\tfrac{\sqrt3}{4}(1 - e)u} = \frac{2}{\sqrt3(1 - e)}\] [M1]
Since \(\tan 60° = \sqrt3\), \(3(1 - e) = 2\), so \(e = \tfrac13\). [A1]
:::

### A direct impact followed by an oblique one

Many questions put two stages together: a direct impact between two spheres, which gives a speed, then an oblique impact of one of them with a wall. The speed from the first stage is the speed before the second.

:::eg (Exam style) Two smooth spheres \(A\) and \(B\), of masses 2\(m\) and \(m\), lie on a smooth horizontal table. \(B\) is at rest and \(A\) moves directly towards it with speed \(u\). The coefficient of restitution between the spheres is \(\tfrac12\). (a) Find the speeds of \(A\) and \(B\) after the collision. After the collision \(B\) moves towards a fixed smooth vertical wall and hits it with its path at 30° to the wall. The coefficient of restitution between \(B\) and the wall is 0.8. (b) Find the speed of \(B\) after it hits the wall, and the angle between its path and the wall. (c) Find the fraction of the kinetic energy of \(B\) that is lost in the impact with the wall.
**(a)** Momentum: \(2mu = 2mv_A + mv_B\). [M1] Law: \(v_B - v_A = \tfrac12u\). [M1] So \(2u = 2v_A + v_A + \tfrac12u\), giving \(v_A = \tfrac12u\) and \(v_B = u\). [A1]
**(b)** Parallel to the wall: \(u\cos 30° = \tfrac{\sqrt3}{2}u = 0.866u\), unchanged. [B1]
Perpendicular: \(u\sin 30° = 0.5u\) before, and \(0.8 \times 0.5u = 0.4u\) after. [M1]
\[v = \sqrt{0.75u^2 + 0.16u^2} = \sqrt{0.91}\,u = 0.954u\] [M1 A1]
\[\tan\beta = \frac{0.4}{0.866} \quad\Rightarrow\quad \beta = 24.8°\] [A1]
**(c)** The kinetic energy of \(B\) after is \(0.91\) of its kinetic energy before (both are \(\tfrac12m \times\) speed squared). [M1]
The fraction lost is \(1 - 0.91 = 0.09\). [A1]
:::

:::exam What to write and what is on MF19
Nothing for oblique impact is on MF19: learn that the perpendicular component is unchanged, and Newton's experimental law for the component along the normal or the line of centres. Always draw the diagram, mark the line of impact, and say in words which line you are using ("resolving along the line of centres"). Each component and each equation earns its own mark, so show them. The directions are angles to a named line; give them to 1 d.p., speeds to 3 s.f., and say which side (rebound, or the same way). Keep exact values in surds where they are given.
:::

:::board
Edexcel IAL and the UK A Levels use \(g = 9.8\) where 9231 uses \(g = 10\), which matters only when a ball is dropped or thrown before the impact. The laws of oblique impact (perpendicular component unchanged, Newton's law along the line of centres) and the meaning of \(e\) are the same.
:::

:::eg Spot the error: a smooth ball hits a fixed smooth wall at 12 m s⁻¹, at an angle of 30° to the wall. The coefficient of restitution is 0.5. Find the speed of the ball after the impact, for 4 marks.
A student wrote this answer.

Line 1: Parallel to the wall: \(12\sin 30° = 6\), unchanged.
Line 2: Perpendicular to the wall: \(12\cos 30° = 10.39\), and after the impact \(0.5 \times 10.39 = 5.196\).
Line 3: Speed \(= \sqrt{6^2 + 5.196^2} = 7.94\) m s⁻¹.

The scheme gives one mark each for the correct parallel component, for Newton's law applied to the perpendicular component, for combining the two components into a speed, and for the correct speed.

**Line 1 swaps the components.** The angle is measured from the wall, so the component along the wall is \(12\cos 30° = 10.39\), not \(12\sin 30°\). [B0] Line 2 uses a correct method (the law applied to the component perpendicular to the wall), only with the wrong value, so the method mark is kept. [M1] Line 3 combines two components correctly. [M1] The speed is wrong. [A0] The student scores 2 out of 4. The slip is the one in the warning above: \(\sin\) goes with the angle to the wall for the **perpendicular** part.

Correct working: parallel \(12\cos 30° = 10.39\); perpendicular before \(12\sin 30° = 6\), after \(3\); speed \(= \sqrt{10.39^2 + 9} = 10.8\) m s⁻¹. [A1]
:::

:::try Start easy, finish at exam standard
Q: A smooth ball hits a fixed smooth wall at 10 m s⁻¹, at 45° to the wall. \(e = 0.4\). Find the components of its velocity parallel and perpendicular to the wall after the impact.
A: Before: both components are \(10\sin 45° = 10\cos 45° = 7.071\). Parallel unchanged: 7.07 m s⁻¹. Perpendicular after: \(0.4 \times 7.071 = 2.83\) m s⁻¹, away from the wall.
Q: A ball hits a wall at an angle of 50° to the wall and rebounds at 30° to the wall. Find \(e\).
A: \(\tan\beta = e\tan\alpha\), so \(e = \dfrac{\tan 30°}{\tan 50°} = 0.484\).
Q: A smooth ball of mass 0.4 kg hits a fixed wall at 12 m s⁻¹, at 60° to the wall, with \(e = 0.5\). Find the impulse of the wall on the ball.
A: The perpendicular component is \(12\sin 60° = 10.39\). \(I = m(1 + e)u_\perp = 0.4 \times 1.5 \times 10.39 = 6.24\) N s, perpendicular to the wall.
Q: Two smooth equal spheres: \(A\) at 8 m s⁻¹ along the line of centres hits \(B\) at rest, \(e = 0.5\). Find the speeds after.
A: Direct impact: \(v_B - v_A = 4\) and \(v_A + v_B = 8\), so \(v_B = 6\) and \(v_A = 2\) m s⁻¹.
Q: A smooth ball hits a wall and loses \(\tfrac{3}{16}\) of its kinetic energy. It hits at 30° to the wall. Find \(e\).
A: The fraction remaining is \(\cos^2 30° + e^2\sin^2 30° = \tfrac34 + \tfrac14e^2 = \tfrac{13}{16}\), so \(e^2 = \tfrac14\) and \(e = \tfrac12\).
Q: A smooth sphere \(A\) of mass 1 kg moving at 6 m s⁻¹, at 60° to the line of centres, hits a stationary sphere \(B\) of mass 1 kg. \(e = 1\). Find the speeds and directions after.
A: Along the line: \(6\cos 60° = 3\); perpendicular \(6\sin 60° = 5.196\). Equal masses and \(e = 1\): \(A\) keeps only the perpendicular part, 5.20 m s⁻¹ along the tangent; \(B\) moves along the line of centres at 3 m s⁻¹. The paths are at 90° to each other.
Q: A ball bounces off two perpendicular smooth walls in turn, with \(e = 0.5\) at both. It hits the first at 8 m s⁻¹ at 40° to the wall. Find its speed after the second impact, and the angle between its final and its original direction of motion.
A: With equal \(e\) both components are reversed and multiplied by 0.5, so the velocity after is \(-0.5\) times the velocity before. Speed \(= 4\) m s⁻¹, and the direction is exactly opposite: the angle between the directions is 180°.
Q: Explain why the impulse on a smooth sphere hitting a wall has no component parallel to the wall.
A: The wall is smooth, so the only contact force is along the normal. An impulse is the integral of the force, so it also has only a normal component.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A smooth ball hits a fixed smooth wall at 10 m s⁻¹, at an angle of 45° to the wall. The coefficient of restitution is 0.4. Find the speed of the ball after the impact.
A: Parallel component: \(10\cos 45° = 7.071\), unchanged. [M1] Perpendicular after: \(0.4 \times 10\sin 45° = 2.828\). [M1] Speed \(= \sqrt{50 + 8} = 7.62\) m s⁻¹. [A1]
Q: [5 marks] ★ A smooth ball hits a fixed smooth wall at an angle of 50° to the wall and rebounds at an angle of 30° to the wall. (a) Find the coefficient of restitution. (b) Find the percentage of the kinetic energy lost in the impact.
A: (a) \(\tan 30° = e\tan 50°\) [M1], so \(e = 0.484\). [A1]
(b) Fraction remaining \(= \cos^2 50° + e^2\sin^2 50°\) [M1] \(= 0.4132 + 0.2347 \times 0.5868 = 0.5509\). Lost: \(44.9\%\). [A1] [A1]
Q: [5 marks] ★★ A smooth ball of mass 0.4 kg hits a fixed smooth wall at 12 m s⁻¹, at an angle of 60° to the wall. The coefficient of restitution is 0.5. Find (a) the magnitude of the impulse of the wall on the ball, (b) the kinetic energy lost.
A: (a) Perpendicular component before: \(12\sin 60° = 10.39\). [B1] \(I = 0.4(10.39 + 0.5 \times 10.39)\) [M1] \(= 6.24\) N s. [A1]
(b) Lost \(= \tfrac12(0.4)(12^2)(1 - 0.25)\sin^2 60°\) [M1] \(= 16.2\) J. [A1]
Q: [7 marks] ★★ A smooth sphere \(A\) of mass 0.5 kg moves at 8 m s⁻¹ and collides with a stationary smooth sphere \(B\) of mass 0.25 kg. At the instant of impact the velocity of \(A\) makes an angle of 60° with the line of centres. The coefficient of restitution is 0.6. Find the speed of \(B\) after the impact, and the speed and direction of \(A\) after the impact.
A: Along the line of centres, \(A\) has component \(8\cos 60° = 4\) and the perpendicular component is \(8\sin 60° = 6.928\). Momentum: \(0.5 \times 4 = 0.5v_A + 0.25v_B\). [M1] Law: \(v_B - v_A = 0.6 \times 4 = 2.4\). [M1] Solving: \(v_A = 1.867\) [A1] and \(v_B = 4.27\) m s⁻¹ along the line of centres. [A1]
Speed of \(A\) \(= \sqrt{1.867^2 + 6.928^2}\) [M1] \(= 7.18\) m s⁻¹. [A1] Its direction makes an angle \(\tan^{-1}\dfrac{6.928}{1.867} = 74.9°\) with the line of centres. [A1]
Q: [6 marks] ★★ Two identical smooth spheres \(A\) and \(B\) are on a smooth horizontal table, with \(B\) at rest. \(A\) moves at 12 m s⁻¹ and at the instant of impact its velocity makes an angle of 40° with the line of centres. The collision is perfectly elastic. Show that the directions of motion after the collision are at right angles, and find the speeds of \(A\) and \(B\) after it.
A: Perpendicular components are unchanged: \(A\) has \(12\sin 40°\), \(B\) has 0. [B1] Along the line with \(e = 1\) and equal masses: \(v_A + v_B = 12\cos 40°\) [M1] and \(v_B - v_A = 12\cos 40°\) [M1], so \(v_A = 0\) and \(v_B = 12\cos 40° = 9.19\) m s⁻¹. [A1] \(A\) moves perpendicular to the line of centres at \(12\sin 40° = 7.71\) m s⁻¹, so the directions are at right angles. [A1 A1]
Q: [9 marks] ★★★ A smooth ball moves on a smooth horizontal floor and hits a smooth vertical wall at an angle of 45° to the wall. The ball loses \(\tfrac{8}{25}\) of its kinetic energy in the impact. (a) Show that the coefficient of restitution between the ball and the wall is 0.6. The ball then hits a second smooth vertical wall, perpendicular to the first, with the same coefficient of restitution. (b) Show that the ball leaves the second wall moving parallel to its original direction, and find its final speed as a fraction of its original speed.
H: The kinetic energy after the first impact is \(\cos^2 45° + e^2\sin^2 45°\) times the original.
H: After the first wall the component along the first wall is unchanged and the component towards it is multiplied by \(-e\). The second wall is perpendicular to the first.
H: Compare the final velocity with the original velocity as a vector.
A: (a) Fraction remaining \(= \tfrac12 + \tfrac12e^2\) [M1 A1] \(= \tfrac{17}{25}\) [M1], so \(e^2 = \tfrac{9}{25}\) and \(e = 0.6\). [A1]
(b) Take \(x\) along the first wall and \(y\) towards it, with original components \((c, s)\) where \(c = s = \dfrac{u}{\sqrt2}\). After the first wall: \((c, -0.6s)\). [M1 A1] The second wall's normal is along \(x\), so the \(x\)-component is reversed and multiplied by 0.6: \((-0.6c, -0.6s)\). [M1] This is \(-0.6\) times the original velocity, so the new direction is parallel to the original and opposite to it. [A1] The speed is 0.6 of the original speed. [A1]
Q: [10 marks] ★★★ A smooth sphere \(A\) of mass \(3m\) moves with speed \(u\) and collides with a stationary smooth sphere \(B\) of mass \(2m\). At the instant of impact the velocity of \(A\) makes an angle \(\alpha\) with the line of centres, where \(\tan\alpha = \tfrac34\). The coefficient of restitution is \(\tfrac12\). (a) Find the components of the velocities of \(A\) and \(B\) along the line of centres after the impact. (b) Find the speed of \(A\) after the impact and the angle its path makes with the line of centres. (c) Find the kinetic energy lost.
H: \(\tan\alpha = \tfrac34\) gives \(\cos\alpha = 0.8\) and \(\sin\alpha = 0.6\) (a 3, 4, 5 triangle).
H: The perpendicular component of \(A\) is \(0.6u\) before and after.
H: In (c) add the kinetic energies after, or use the formula with the component \(0.8u\).
A: (a) The perpendicular component of \(A\), \(0.6u\), is unchanged. [B1] Along the line before: \(A\) has \(0.8u\). Momentum: \(3m(0.8u) = 3mv_A + 2mv_B\) [M1]; law: \(v_B - v_A = 0.5(0.8u) = 0.4u\) [M1]. So \(2.4u = 3v_A + 2v_A + 0.8u\), giving \(v_A = 0.32u\) [A1] and \(v_B = 0.72u\). [A1]
(b) Speed of \(A\) \(= u\sqrt{0.32^2 + 0.6^2}\) [M1] \(= 0.680u\). [A1] Angle with the line of centres: \(\tan^{-1}\dfrac{0.6}{0.32} = 61.9°\). [A1]
(c) Before: \(\tfrac12(3m)u^2 = 1.5mu^2\). After:
\[\begin{aligned}
&\tfrac12(3m)(0.4624u^2) + \tfrac12(2m)(0.5184u^2) \\
&= 0.6936mu^2 + 0.5184mu^2
\end{aligned}\] [M1]
Lost \(= 1.5mu^2 - 1.212mu^2 = 0.288mu^2\). [A1]
Q: [10 marks] (#math.fm.impulse) ★★★ A smooth sphere \(A\) of mass \(3m\) moves with speed \(u\) along a smooth horizontal table and collides directly with a stationary smooth sphere \(B\) of mass \(m\). The coefficient of restitution between the spheres is 0.6. (a) Find the speed of \(B\) after the collision. Immediately after the collision, \(B\) moves towards a fixed smooth vertical wall and hits it with its path at 45° to the wall. The coefficient of restitution between \(B\) and the wall is 0.5. (b) Find the speed of \(B\) after it hits the wall and the angle its path makes with the wall. (c) Find the fraction of the kinetic energy of \(B\) lost in the impact with the wall.
H: In (a) use \(v_B = \dfrac{m_1(1 + e)u}{m_1 + m_2}\), or solve the two equations again.
H: In (b) the parallel component is unchanged and the perpendicular component is multiplied by \(e\).
A: (a) \(3mu = 3mv_A + mv_B\) [M1], \(v_B - v_A = 0.6u\) [M1], so \(v_B = 1.2u\) and \(v_A = 0.6u\). [A1]
(b) Components of \(B\)'s velocity: parallel \(1.2u\cos 45° = 0.8485u\), unchanged [B1]; perpendicular before \(0.8485u\), after \(0.5 \times 0.8485u = 0.4243u\). [M1] Speed \(= u\sqrt{0.8485^2 + 0.4243^2}\) [M1] \(= 0.949u\). [A1] The angle with the wall: \(\tan^{-1}\dfrac{0.4243}{0.8485} = 26.6°\). [A1]
(c) Kinetic energy after \(\div\) before \(= \left(\dfrac{0.949}{1.2}\right)^2 = 0.625\) [M1], so the fraction lost is \(\tfrac38\). [A1]
:::

:::try Stretch for A*
Q: [10 marks] ★★★ A small smooth ball is dropped from rest at a point 1.25 m vertically above a smooth plane inclined at 30° to the horizontal. The coefficient of restitution between the ball and the plane is \(\tfrac12\). Take \(g = 10\). (a) Find the components of the velocity of the ball just before it hits the plane, parallel and perpendicular to the plane. (b) Find the time between the first and second impacts with the plane. (c) Show that the distance along the plane between the first and second impacts is \(4e(1 + e)h\sin\alpha\), where \(h\) is the height from which the ball was dropped and \(\alpha\) is the angle of the plane, and find its value.
H: Resolve the acceleration \(g\) parallel and perpendicular to the plane.
H: After the first impact the motion perpendicular to the plane is that of a ball thrown up and back to the same level.
H: Along the plane, the ball has the speed it had before the first impact and an acceleration \(g\sin\alpha\).
A: (a) Speed just before the impact: \(v = \sqrt{2 \times 10 \times 1.25} = 5\) m s⁻¹, vertically downwards. Parallel to the plane (down the slope): \(5\sin 30° = 2.5\) m s⁻¹; perpendicular to the plane (towards it): \(5\cos 30° = 4.33\) m s⁻¹. [B1 B1]
(b) After the impact the parallel component is unchanged and the perpendicular component is \(e \times 4.33 = 2.165\), away from the plane. [M1] Perpendicular to the plane the acceleration is \(-g\cos 30°\), and the ball returns to the plane when \(2.165T - \tfrac12(10\cos 30°)T^2 = 0\) [M1], so \(T = \dfrac{2 \times 2.165}{10\cos 30°} = 0.5\) s. [A1]
(c) Along the plane the ball starts with 2.5 m s⁻¹ and has acceleration \(g\sin\alpha = 5\) m s⁻²: distance \(= 2.5T + \tfrac12(5)T^2\). [M1 A1] In general the speed is \(v = \sqrt{2gh}\), \(T = \dfrac{2ev}{g}\), and distance \(= v\sin\alpha\,T + \tfrac12g\sin\alpha\,T^2 = \dfrac{2ev^2\sin\alpha}{g}(1 + e)\). With \(v^2 = 2gh\) this is \(4e(1 + e)h\sin\alpha\). [M1 A1] The value: \(4 \times 0.5 \times 1.5 \times 1.25 \times 0.5 = 1.875\) m. [A1]
Q: [6 marks] ★★★ Two identical smooth spheres collide, with \(B\) at rest and \(A\) moving at an angle \(\theta\) (acute) to the line of centres at the instant of impact. The coefficient of restitution is \(e\), with \(e < 1\). Show that the angle \(\psi\) between the paths of \(A\) and \(B\) after the impact satisfies \(\tan\psi = \dfrac{2\tan\theta}{1 - e}\), and deduce that \(\psi\) is acute and tends to 90° as \(e \to 1\).
H: \(B\) moves along the line of centres after the impact, so the angle between the paths is the angle that the path of \(A\) makes with the line of centres.
H: Find \(v_A\) along the line as in the worked examples, with general \(\theta\) and \(e\).
A: The perpendicular component of \(A\), \(u\sin\theta\), is unchanged. [B1] Along the line: \(u\cos\theta = v_A + v_B\) and \(v_B - v_A = eu\cos\theta\). [M1 M1] So \(v_A = \tfrac12(1 - e)u\cos\theta\). [A1] \(B\) moves along the line of centres, so \(\psi\) is the angle between the path of \(A\) and that line: \(\tan\psi = \dfrac{u\sin\theta}{\tfrac12(1 - e)u\cos\theta} = \dfrac{2\tan\theta}{1 - e}\). [A1] For \(e < 1\) the along-line component is positive and \(\tan\psi\) is positive and finite, so \(\psi\) is acute; as \(e \to 1\), \(\tan\psi \to \infty\) and \(\psi \to 90°\). [A1]
:::

:::quiz
? A smooth sphere hits a fixed smooth wall obliquely. Which component of its velocity is unchanged by the impact?
+ the component parallel to the wall
- the component perpendicular to the wall
- the component along the original direction of motion
- none: both components are multiplied by \(e\)
> The wall is smooth, so it exerts no force along itself, and the parallel component stays the same. Only the component along the normal is multiplied by \(e\) and reversed. Multiplying both by \(e\) is the mistake in the first warning.
? A ball hits a smooth wall at an angle \(\alpha\) to the wall and rebounds at \(\beta\) to the wall. Which relation holds?
- \(\beta = e\alpha\)
+ \(\tan\beta = e\tan\alpha\)
- \(\sin\beta = e\sin\alpha\)
- \(\tan\beta = \dfrac{\tan\alpha}{e}\)
> The parallel component is unchanged and the perpendicular component is multiplied by \(e\), so the ratio of perpendicular to parallel, \(\tan\) of the angle with the wall, is multiplied by \(e\). The angle itself is not.
? For an oblique impact of two smooth spheres, Newton's experimental law is applied to
- the speeds of the spheres
+ the components of velocity along the line of centres
- the components of velocity perpendicular to the line of centres
- the components along the original direction of \(A\)
> The impulse acts along the line of centres, so the collision along that line is a direct impact. The perpendicular components do not change, so there is nothing for the law to say about them.
? Two identical smooth spheres collide with \(e = 1\); one is at rest. After the impact the angle between their paths is
- \(30°\)
- \(60°\)
- \(45°\)
+ \(90°\)
> The moving sphere keeps only its perpendicular component and the struck sphere moves along the line of centres, so the paths are at right angles. This is true for any angle of approach (other than head-on, when the first sphere stops).
? A ball hits a smooth wall at 30° to the wall, with \(e = \tfrac12\). What fraction of its kinetic energy remains?
- \(\tfrac14\)
- \(\tfrac12\)
+ \(\tfrac{13}{16}\)
- \(\tfrac{3}{4}\)
> The fraction remaining is \(\cos^2 30° + e^2\sin^2 30° = \tfrac34 + \tfrac14 \times \tfrac14 = \tfrac{13}{16}\). The answer \(\tfrac14\) is \(e^2\), which is the direct-impact fraction, and \(\tfrac34\) forgets the perpendicular part that survives.
? In an oblique impact between two smooth spheres, the impulse on \(B\) acts
+ along the line of centres
- along the direction of motion of \(A\) before the impact
- perpendicular to the line of centres
- along the common tangent
> The spheres are smooth, so the contact force is along the normal to the surfaces at the contact point, which is the line of centres. The direction of motion of \(A\) has no special role.
:::

:::checklist What you can now do
- [ ] I can resolve a velocity along and perpendicular to the line of impact, and say which component changes in an oblique impact with smooth surfaces.
- [ ] I can find the speed and direction after a smooth sphere hits a fixed surface, using the unchanged parallel component and \(e\) on the perpendicular component.
- [ ] I can use \(\tan\beta = e\tan\alpha\), find \(e\) from the angles or from the kinetic energy, and find the impulse and the kinetic energy lost.
- [ ] I can follow a particle through two successive impacts with walls, including walls at right angles and at other angles.
- [ ] I can solve the oblique impact of two smooth spheres using momentum and Newton's experimental law along the line of centres, and the unchanged perpendicular components.
- [ ] I can find the speeds, directions, impulse and kinetic energy lost after an oblique impact of two spheres.
- [ ] I can show that equal smooth spheres, one at rest, with \(e = 1\) leave at right angles.
- [ ] I can combine a direct impact of two spheres with an oblique impact of one of them with a wall.
:::

:::recap
- Smooth surfaces: the impulse acts along the line of impact only (the normal to a wall, the line of centres for spheres). The component perpendicular to it is unchanged.
- Sphere and fixed wall at angle \(\alpha\) to the wall: parallel component \(u\cos\alpha\) unchanged; perpendicular component \(u\sin\alpha\) becomes \(eu\sin\alpha\), reversed. \(\tan\beta = e\tan\alpha\). Speed after \(= u\sqrt{\cos^2\alpha + e^2\sin^2\alpha}\). Impulse \(m(1 + e)u\sin\alpha\).
- Two spheres: resolve along the line of centres; use momentum and \(v_2 - v_1 = e(u_1 - u_2)\) for those components; keep each sphere's perpendicular component.
- Kinetic energy lost \(= \dfrac{m_1m_2(1 - e^2)}{2(m_1 + m_2)}(u_1 - u_2)^2\), with \(u_1 - u_2\) the along-the-line approach speed.
- Equal masses, \(e = 1\), one at rest: the spheres leave at 90°.
- Two perpendicular walls with the same \(e\): the final velocity is \(-e\) times the original.
- Angle given to the wall or to the normal? Check before resolving.
- Do not apply \(e\) to the whole velocity or to the speeds of two spheres in an oblique impact.
:::

:::links
- watch: [Newton's law of restitution playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiPDYYt5yYtsPqnSbtedvrN) · ExamSolutions (YouTube) · includes oblique impact with walls and spheres
- explore: [Collision lab](https://phet.colorado.edu/en/simulations/collision-lab) · PhET · two-dimensional collisions with adjustable elasticity
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · oblique impact questions with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Paper 3 questions with mark schemes [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers sorted by year

Links checked 20 November 2026.
:::
Next: [Continuous random variables](#math.fm.crv) leaves Further Mechanics for Further Probability and Statistics, starting with probability density and cumulative distribution functions.
