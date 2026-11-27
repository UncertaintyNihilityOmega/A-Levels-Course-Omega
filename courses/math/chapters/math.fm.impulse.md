@chapter math.fm.impulse
@title Direct impact and restitution
@level fm
@paper CAIE 9231 Paper 3
@time 5–6 hours
@summary In a collision the forces are huge and last for a moment, so we track the momentum before and after instead. You will use impulse and conservation of momentum, and Newton's experimental law with the coefficient of restitution \(e\), to find the velocities after a direct impact of two smooth spheres or of a sphere with a fixed wall, the kinetic energy lost, the heights of a bouncing ball, and the outcome of a sequence of collisions.

:::why
When two snooker balls meet, a ball hits a wall or a hammer strikes a nail, the contact lasts a few thousandths of a second and the force is far too large and too hard to measure to use \(F = ma\) directly. What you can measure is what goes in and what comes out. Two laws connect them: momentum is conserved, and the speed at which the two bodies separate is a fixed fraction of the speed at which they approached. With those two equations you can predict a whole collision, and a whole chain of collisions, from the numbers before it.
:::

**Before you start**, you need conservation of momentum from [Momentum and collisions](#math.m.momentum), kinetic energy from [Work, energy and power](#math.m.energy), and the sum to infinity of a geometric series from [Series: binomial expansion and progressions](#math.p1.series). Chapter [Linear motion under a variable force](#math.fm.variable) is useful for the impulse of a force that varies with time. In 9709 mechanics, impulse and the coefficient of restitution are not examined, so this chapter teaches both from the start.

:::try Warm-up
Q: A sphere of mass 3 kg moving at 4 m s⁻¹ hits a stationary sphere of mass 5 kg and they stick together. Find their common speed. (from [Momentum and collisions](#math.m.momentum))
A: Momentum is conserved: \(3 \times 4 = (3 + 5)v\), so \(v = \dfrac{12}{8} = 1.5\) m s⁻¹.
Q: Find the kinetic energy of a 0.2 kg ball moving at 10 m s⁻¹. (from [Work, energy and power](#math.m.energy))
A: \(\tfrac12 mv^2 = \tfrac12 \times 0.2 \times 100 = 10\) J.
Q: Find the sum to infinity of \(8 + 8(0.5) + 8(0.5)^2 + \cdots\). (from [Series: binomial expansion and progressions](#math.p1.series))
A: The first term is 8 and the common ratio is 0.5, so \(S_\infty = \dfrac{a}{1 - r} = \dfrac{8}{0.5} = 16\).
:::

## Impulse

When a bat hits a ball, the force changes second by second, rising from zero to a peak and back to zero in a few milliseconds. Newton's second law in the form \(F = \dfrac{d}{dt}(mv)\) says the force is the rate of change of momentum. Integrate that over the time of the contact and the awkward details of the force drop out.

:::def Impulse
The **impulse** of a force \(F\) acting for a time from \(t_1\) to \(t_2\) is \(I = \displaystyle\int_{t_1}^{t_2} F\,dt\). For a constant force this is \(Ft\). Impulse is a vector, measured in newton seconds (N s), and it equals the change of momentum.
:::

:::key Impulse–momentum principle
For a particle of mass \(m\) whose velocity changes from \(u\) to \(v\) in a straight line,
\[I = mv - mu\]
The impulse is the **final momentum minus the initial momentum**, with signs: take one direction as positive, and write a velocity in the other direction as negative.
:::

The sign is what catches students out: a ball that is hit back changes velocity by more than its speed.

:::eg A ball of mass 0.4 kg approaches a bat at 15 m s⁻¹ and leaves it in the opposite direction at 20 m s⁻¹. Find the magnitude of the impulse exerted by the bat on the ball, and the average force if the contact lasts 0.01 s.
Take the direction in which the ball leaves as positive. Then \(u = -15\) and \(v = +20\):
\[I = mv - mu = 0.4 \times 20 - 0.4 \times (-15) = 8 + 6 = 14\ \text{N s}\]
The average force is \(\dfrac{I}{t} = \dfrac{14}{0.01} = 1400\) N. That is about 350 times the ball's weight, which is why contact forces in impacts are so much larger than the ordinary forces around them.
:::

When the force is given as a function of time, integrate it.

:::eg A ball of mass 0.25 kg is at rest on a smooth floor and is struck. During the strike the force on it, in newtons, is \(F = 3 \times 10^7\,t\,(0.01 - t)\) for \(0 \le t \le 0.01\), where \(t\) is in seconds. Find the impulse, the greatest force and the speed with which the ball leaves.
\[I = \int_0^{0.01} 3 \times 10^7\,(0.01t - t^2)\,dt = 3 \times 10^7\left[\frac{0.01t^2}{2} - \frac{t^3}{3}\right]_0^{0.01}\]
The bracket is \(\dfrac{10^{-6}}{2} - \dfrac{10^{-6}}{3} = \dfrac{10^{-6}}{6}\), so \(I = 5\) N s.

The force is greatest at the midpoint, \(t = 0.005\): \(F = 3 \times 10^7 \times 0.005 \times 0.005 = 750\) N.

Impulse \(= mv - mu\) with \(u = 0\): \(5 = 0.25v\), so \(v = 20\) m s⁻¹.
:::

The area under a force–time graph is the impulse. This is useful when the graph is a triangle or a rectangle.

Newton's third law gives the key fact about collisions. When two bodies collide, each exerts a force on the other. The two forces are equal and opposite at every instant, so the two impulses are equal and opposite. The momentum gained by one equals the momentum lost by the other.

:::key Conservation of momentum in a collision
For two bodies of masses \(m_1\) and \(m_2\) colliding on a smooth surface (no other horizontal impulse),
\[m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\]
The total momentum in the line of the impact is unchanged. The **kinetic energy** is not conserved in general (see below).
:::

## Direct impact of two smooth spheres

:::def Direct impact
A collision of two smooth spheres in which the velocities of both spheres, just before the impact, are along the line joining their centres. The spheres are smooth, so the only force between them is along that line, and both keep moving along it.
:::

We model each sphere as a particle (it does not spin) of its given mass. The two unknown speeds after the impact need two equations. Conservation of momentum is one; the other is an experimental fact about how bouncy the materials are.

:::def Newton's experimental law and the coefficient of restitution
For two bodies colliding directly,
\[\text{speed of separation} = e \times \text{speed of approach}\]
The constant \(e\) depends only on the materials of the two bodies and is called the **coefficient of restitution**. It satisfies \(0 \le e \le 1\). If \(e = 1\) the collision is **perfectly elastic**: no kinetic energy is lost. If \(e = 0\) the collision is **inelastic**: the spheres do not separate and move on together.
:::

"Approach" and "separation" are speeds: the rate at which the gap closes before the impact, and the rate at which it opens afterwards. Take a positive direction and call the sphere behind \(A\) and the sphere in front \(B\), with velocities \(u_1, u_2\) before and \(v_1, v_2\) after, all measured in the positive direction.

:::key Direct impact: the two equations
\[\begin{aligned}
m_1u_1 + m_2u_2 &= m_1v_1 + m_2v_2 &\quad&\text{(momentum)} \\
v_2 - v_1 &= e\,(u_1 - u_2) &\quad&\text{(Newton's experimental law)}
\end{aligned}\]
In the second line, "behind" is \(A\) and "in front" is \(B\): separation is (velocity of the front sphere \(-\) velocity of the back sphere), approach is (back \(-\) front) before. Neither is on MF19: learn them.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 205" role="img" aria-label="Two rows of two spheres, before and after a direct impact. Before: sphere A of mass m1 has velocity u1 and sphere B of mass m2 has velocity u2, both to the right, with u1 greater than u2. After: A has velocity v1 and B has velocity v2, both measured to the right. A small arrow at the bottom right shows the positive direction."><text class="tl" x="10" y="18">Before</text><circle class="f1 s-acc sw2" cx="90" cy="60" r="22"/><circle class="f2 s-acc sw2" cx="210" cy="60" r="28"/><path class="c1 thick" d="M70 20H130" marker-end="url(#ah)"/><path class="c1 thick" d="M190 20H250" marker-end="url(#ah)"/><text class="tl" x="136" y="24">u₁</text><text class="tl" x="256" y="24">u₂</text><text class="tl" x="90" y="65" text-anchor="middle">m₁</text><text class="tl" x="210" y="65" text-anchor="middle">m₂</text><text class="tl" x="10" y="112">After</text><circle class="f1 s-acc sw2" cx="90" cy="160" r="22"/><circle class="f2 s-acc sw2" cx="210" cy="160" r="28"/><path class="c2 thick" d="M70 120H110" marker-end="url(#ah)"/><path class="c2 thick" d="M190 120H250" marker-end="url(#ah)"/><text class="tl" x="116" y="124">v₁</text><text class="tl" x="256" y="124">v₂</text><text class="tl" x="90" y="165" text-anchor="middle">m₁</text><text class="tl" x="210" y="165" text-anchor="middle">m₂</text><text class="tl" x="258" y="180">positive</text><path class="ln thin" d="M258 192H298" marker-end="url(#ah)"/></svg><figcaption>Before and after a direct impact. Both velocities of each row are measured in the positive direction, so a negative value means the sphere moves to the left. Velocities after the impact are unknown: draw them in the positive direction and let the algebra decide the sign. The picture is not to scale.</figcaption></figure>
:::

:::eg (Exam style) Two smooth spheres \(A\) and \(B\), of masses \(m_1\) and \(m_2\), lie at rest on a smooth horizontal table. \(A\) is projected directly towards \(B\) with speed \(u\), and the coefficient of restitution between the spheres is \(e\). Show that after the impact the speed of \(B\) is \(\dfrac{m_1(1 + e)u}{m_1 + m_2}\) and the velocity of \(A\) is \(\dfrac{(m_1 - em_2)u}{m_1 + m_2}\) in the direction of motion.
Let the velocities after impact be \(v_A\) and \(v_B\), in the direction of \(A\)'s motion.

Momentum:
\[m_1u = m_1v_A + m_2v_B\] [M1]
Newton's experimental law (\(B\) was at rest, so approach is \(u\)):
\[v_B - v_A = eu\] [M1]
Substitute \(v_A = v_B - eu\) into the momentum equation:
\[m_1u = m_1v_B - em_1u + m_2v_B\] [M1]
\[(m_1 + m_2)v_B = m_1u(1 + e) \quad\Rightarrow\quad v_B = \frac{m_1(1 + e)u}{m_1 + m_2}\] [A1]
Then
\[v_A = v_B - eu = \frac{m_1(1 + e)u - eu(m_1 + m_2)}{m_1 + m_2} = \frac{(m_1 - em_2)u}{m_1 + m_2}\] [A1]
:::

The result tells you at once what \(A\) does. If \(m_1 > em_2\), then \(v_A > 0\) and \(A\) goes on in the same direction. If \(m_1 < em_2\), \(v_A < 0\) and \(A\) rebounds. If \(m_1 = em_2\), \(A\) is brought to rest. Remember the structure of the result, but in an exam always solve the two equations with the numbers you are given, as in the next example.

:::eg A smooth sphere \(A\) of mass 2 kg moves at 5 m s⁻¹ along a smooth horizontal table and collides directly with a sphere \(B\) of mass 3 kg moving towards it at 1 m s⁻¹. The coefficient of restitution is 0.5. Find the velocities of \(A\) and \(B\) after the impact, and the kinetic energy lost.
Take the direction of \(A\)'s motion as positive, so \(u_1 = 5\) and \(u_2 = -1\).

Momentum:
\[2 \times 5 + 3 \times (-1) = 2v_1 + 3v_2 \quad\Rightarrow\quad 2v_1 + 3v_2 = 7\]
Newton's experimental law, with approach speed \(5 - (-1) = 6\):
\[v_2 - v_1 = 0.5 \times 6 = 3\]
Substitute \(v_2 = v_1 + 3\):
\[2v_1 + 3v_1 + 9 = 7 \quad\Rightarrow\quad 5v_1 = -2\]
So \(v_1 = -0.4\) and \(v_2 = 2.6\). \(A\) rebounds at 0.4 m s⁻¹ and \(B\) moves off at 2.6 m s⁻¹ in the original direction of \(A\).

Kinetic energy:
\[\begin{aligned}
\text{before} &= \tfrac12(2)(5)^2 + \tfrac12(3)(1)^2 = 26.5\ \text{J} \\
\text{after} &= \tfrac12(2)(0.4)^2 + \tfrac12(3)(2.6)^2 = 10.3\ \text{J}
\end{aligned}\]
The energy lost is \(26.5 - 10.3 = 16.2\) J.
:::

### The extreme cases

Putting \(e = 1\) and \(e = 0\) into the law shows what they mean.

- \(e = 1\): separation speed equals approach speed, and no energy is lost. For two spheres of **equal mass** the result is dramatic: they swap velocities, \(v_1 = u_2\) and \(v_2 = u_1\). A moving ball hitting an identical ball at rest stops dead, and the other moves off at the same speed (the idea behind Newton's cradle).
- \(e = 0\): separation speed is zero, so \(v_1 = v_2\): the two spheres move together after the impact, as if they had coalesced. Momentum alone gives that common speed, which is why 9709 "coalescing" problems are the case \(e = 0\).

:::warn Order of the speeds in Newton's experimental law
The law compares **separation** with **approach**. Write it as \(v_2 - v_1 = e(u_1 - u_2)\), with sphere 2 the one in front. Writing \(v_1 - v_2\) on the left gives a negative separation, which is impossible, and every number after it is wrong. After the impact you must always have \(v_2 \ge v_1\) when sphere 2 is in front, otherwise the spheres would pass through each other. If your answer fails this, you have used the law the wrong way round.
:::

:::warn Kinetic energy is lost unless \(e = 1\)
Momentum is conserved in every collision; kinetic energy is conserved only if \(e = 1\). Never write "energy before = energy after" for a collision unless the question says the impact is perfectly elastic. The lost energy goes into sound, heat and deformation.
:::

### Kinetic energy lost

The lost energy has a neat general formula, which you can use to check a calculation, and which gives a quick route when a question talks about a fraction of the energy lost.

:::proof The kinetic energy lost in a direct impact
Let the spheres have masses \(m_1, m_2\), velocities \(u_1, u_2\) before and \(v_1, v_2\) after. Write \(w = u_1 - u_2\) for the velocity of approach and \(M = m_1 + m_2\).
1. Define \(V = \dfrac{m_1u_1 + m_2u_2}{M}\), the mass-weighted average of the two velocities. (It is the velocity of the centre of mass, the point whose position you found in [Centres of mass](#math.fm.com) in the same way.) Momentum says \(m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\), so \(V = \dfrac{m_1v_1 + m_2v_2}{M}\) as well: \(V\) is the same before and after.
2. For any two velocities, \(\tfrac12m_1u_1^2 + \tfrac12m_2u_2^2 = \tfrac12MV^2 + \tfrac12m_1(u_1 - V)^2 + \tfrac12m_2(u_2 - V)^2\). (Expand the right side: the cross terms give \(-V(m_1u_1 + m_2u_2) = -MV^2\), which with \(+\tfrac12MV^2\) twice leaves exactly the left side.) The same holds after the impact with \(v_1, v_2\). So the kinetic energy is \(\tfrac12MV^2\) plus the energy "relative to \(V\)", and the first part is the same before and after.
3. Before the impact, \(u_1 - V = \dfrac{m_2w}{M}\) and \(u_2 - V = -\dfrac{m_1w}{M}\). The relative energy before is \(\tfrac12 m_1\dfrac{m_2^2w^2}{M^2} + \tfrac12 m_2\dfrac{m_1^2w^2}{M^2} = \tfrac12\dfrac{m_1m_2}{M}w^2\).
4. After the impact the velocity of separation is \(e\) times the velocity of approach, so \(v_1 - V = -\dfrac{em_2w}{M}\) and \(v_2 - V = \dfrac{em_1w}{M}\): every term of step 3 is multiplied by \(e\), so the relative energy is \(e^2\) times as large.
5. Energy lost \(= \tfrac12\dfrac{m_1m_2}{m_1 + m_2}(1 - e^2)(u_1 - u_2)^2\).
:::

:::key Kinetic energy lost
\[\text{KE lost} = \frac{m_1m_2}{2(m_1 + m_2)}\,(1 - e^2)\,(u_1 - u_2)^2\]
This is a result to know and check against, not a formula to quote without working, unless the question allows it. It is zero when \(e = 1\) or when the spheres have equal velocities.
:::

:::eg (Exam style) A smooth sphere \(A\) of mass \(m\) moving at speed \(u\) collides directly with a stationary smooth sphere \(B\) of mass \(3m\). The coefficient of restitution is \(e\). (a) Find, in terms of \(u\) and \(e\), the velocities of \(A\) and \(B\) after the impact. (b) The total kinetic energy after the impact is \(\tfrac{13}{25}\) of the kinetic energy before. Find \(e\). (c) Show that \(A\) reverses direction, and find the magnitude of the impulse of \(A\) on \(B\) in terms of \(m\) and \(u\).
**(a)** Take the direction of \(A\)'s motion as positive.
\[mu = mv_A + 3mv_B\] [M1]
\[v_B - v_A = eu\] [M1]
Substituting \(v_A = v_B - eu\): \(mu = mv_B - emu + 3mv_B\), so \(4v_B = u(1 + e)\). [M1]
\[v_B = \frac{(1 + e)u}{4} \qquad v_A = \frac{(1 + e)u}{4} - eu = \frac{(1 - 3e)u}{4}\] [A1]
**(b)** Kinetic energy before is \(\tfrac12mu^2\). After:
\[\tfrac12m\frac{(1 - 3e)^2u^2}{16} + \tfrac12(3m)\frac{(1 + e)^2u^2}{16} = \frac{mu^2}{32}\left[(1 - 3e)^2 + 3(1 + e)^2\right]\] [M1]
\[= \frac{mu^2}{32}\left(4 + 12e^2\right) = \frac{mu^2(1 + 3e^2)}{8}\] [A1]
This equals \(\tfrac{13}{25} \times \tfrac12mu^2\):
\[\frac{1 + 3e^2}{8} = \frac{13}{50} \quad\Rightarrow\quad 1 + 3e^2 = \frac{52}{25}\] [M1]
\[e^2 = \frac{9}{25}, \quad e = 0.6\] [A1]
**(c)** With \(e = 0.6\): \(v_A = \dfrac{(1 - 1.8)u}{4} = -0.2u\). It is negative, so \(A\) reverses direction. [B1]
The impulse of \(A\) on \(B\) equals the change of momentum of \(B\), \(3m(v_B - 0)\) with \(v_B = \dfrac{1.6u}{4} = 0.4u\):
\[I = 3m \times 0.4u = 1.2mu\] [A1]

**Check** with the loss formula: \(\dfrac{m \times 3m}{2 \times 4m}(1 - 0.36)u^2 = 0.24mu^2\), which is \(48\%\) of \(\tfrac12mu^2\), so \(52\%\) remains. \(\tfrac{13}{25} = 0.52\). Good.
:::

## A sphere and a fixed wall

A smooth wall is a very large mass that does not move: it is like \(m_2 \to \infty\) with \(u_2 = v_2 = 0\). Momentum is **not** conserved, because the wall (and the ground it is fixed to) takes some. But Newton's experimental law still holds, and it simplifies.

:::key Direct impact with a fixed surface
In this box \(u\) and \(v\) are **speeds** (both positive), not signed velocities. A sphere hits a fixed smooth surface directly with speed \(u\). After the impact it moves in the opposite direction with speed
\[v = eu\]
The impulse of the wall on the sphere is \(m(v + u) = m(1 + e)u\), along the normal and away from the wall. Kinetic energy lost is \(\tfrac12m(1 - e^2)u^2\).
:::

:::eg A ball of mass 0.16 kg hits a smooth vertical wall directly at 12 m s⁻¹ and rebounds at 9 m s⁻¹. Find (a) the coefficient of restitution, (b) the impulse of the wall on the ball, (c) the average force if the contact lasts 0.01 s, (d) the kinetic energy lost.
**(a)** \(v = eu\), so \(e = \dfrac{9}{12} = 0.75\).

**(b)** Take the direction away from the wall as positive: \(u = -12\), \(v = +9\).
\[I = m(v - u) = 0.16 \times (9 + 12) = 3.36\ \text{N s}\]
**(c)** \(F = \dfrac{3.36}{0.01} = 336\) N.

**(d)** \(\text{KE lost} = \tfrac12 \times 0.16 \times (12^2 - 9^2) = 0.08 \times 63 = 5.04\) J.
:::

### The bouncing ball

A ball dropped onto a horizontal floor hits it directly. If it is dropped from a height \(h\), it arrives with speed \(\sqrt{2gh}\) (constant acceleration, or energy). After the impact its speed is \(e\sqrt{2gh}\), so it rises to the height at which that speed has been used up:
\[h_1 = \frac{(e\sqrt{2gh})^2}{2g} = e^2h\]
Each bounce multiplies the speed by \(e\) and the height by \(e^2\). The heights \(h, e^2h, e^4h, \ldots\) form a geometric sequence with common ratio \(e^2 < 1\), so total distances and times are sums to infinity.

:::html
<figure class="fig small"><svg viewBox="0 0 320 205" role="img" aria-label="A vertical scale above a floor with three heights marked by dashed lines and dots: the drop height h equal to 2 metres at the top, the height after the first bounce e squared h equal to 0.72 metres, and the height after the second bounce e to the fourth h equal to 0.259 metres, for e equal to 0.6."><path class="ln" d="M20 180H300"/><path class="ln-m thin" d="M60 180V14"/><path class="ln-m thin dash" d="M60 20H190"/><path class="ln-m thin dash" d="M60 122.4H190"/><path class="ln-m thin dash" d="M60 159.3H190"/><circle class="f2 s-acc sw2" cx="60" cy="20" r="4"/><circle class="f2 s-acc sw2" cx="60" cy="122.4" r="4"/><circle class="f2 s-acc sw2" cx="60" cy="159.3" r="4"/><text class="tl" x="196" y="24">h = 2 m</text><text class="tl" x="196" y="126">e²h = 0.72 m</text><text class="tl" x="196" y="163">e⁴h = 0.259 m</text><text class="tl" x="230" y="198">floor</text></svg><figcaption>A ball dropped from \(h = 2\) m with \(e = 0.6\) rises to \(e^2h = 0.72\) m after the first impact and to \(e^4h = 0.2592\) m after the second: each height is \(e^2 = 0.36\) times the one before. The figure shows the heights only, not the path.</figcaption></figure>
:::

:::eg (Exam style) A small ball is dropped from rest at a height of 2 m above a horizontal floor and bounces repeatedly. The coefficient of restitution between the ball and the floor is 0.6. Take \(g = 10\). (a) Show that the height to which the ball rises after the \(n\)th bounce is \(2(0.36)^n\) m. (b) Find the total distance travelled by the ball before it comes to rest. (c) Find the total time taken for the bouncing to stop.
**(a)** Speed just before the first impact: \(v^2 = 2 \times 10 \times 2 = 40\), so \(v = \sqrt{40}\). [M1]
Each impact multiplies the speed by \(e = 0.6\), so after the first impact the speed is \(0.6\sqrt{40}\) and the ball rises to
\[h_1 = \frac{(0.6)^2 \times 40}{20} = 0.72 = 2(0.36)\] [M1]
By the same argument each height is \(e^2 = 0.36\) times the one before, so \(h_n = 2(0.36)^n\). [A1]
**(b)** The distance is 2 m down, then up and down for each later bounce:
\[D = 2 + 2\left(0.72 + 0.72(0.36) + \cdots\right)\] [M1]
The bracket is a geometric series with first term 0.72 and ratio 0.36:
\[D = 2 + \frac{2 \times 0.72}{1 - 0.36} = 2 + 2.25 = 4.25\ \text{m}\] [M1 A1]
**(c)** The first fall takes \(t_0 = \sqrt{\dfrac{2 \times 2}{10}} = \sqrt{0.4}\) s. [B1]
A ball thrown up with speed \(w\) takes \(\dfrac{w}{g}\) to stop rising (its speed falls by \(g\) each second) and the same time to fall back, so **up and back takes \(\dfrac{2w}{g}\)**. After the first impact the ball leaves with speed \(0.6\sqrt{40}\), so it takes \(\dfrac{2 \times 0.6\sqrt{40}}{10} = 1.2t_0\) s to go up and come down. Every later up-and-down takes 0.6 times as long as the one before, so the times form a geometric sequence with ratio 0.6:
\[T = t_0 + \frac{1.2t_0}{1 - 0.6}\] [M1]
\[T = t_0(1 + 3) = 4\sqrt{0.4} = 2.53\ \text{s}\] [A1]
:::

For a ball dropped from height \(h\) with restitution \(e\), the total distance is \(h\,\dfrac{1 + e^2}{1 - e^2}\) and the total time is \(\sqrt{\dfrac{2h}{g}}\,\dfrac{1 + e}{1 - e}\). In the example, \(2 \times \dfrac{1.36}{0.64} = 4.25\) and \(\sqrt{0.4} \times \dfrac{1.6}{0.4} = 2.53\), as found. The ball makes infinitely many bounces in a finite time and distance, because both series converge.

## Successive collisions

When there are several spheres, or a sphere and a wall as well, treat each impact in turn: the velocities after one impact are the velocities before the next. Then ask whether a later impact happens at all. Two bodies on a line collide again only if the one behind is faster than the one in front.

:::key When is there a further collision?
Two spheres moving along a line in the same direction collide again only if the back sphere has the greater velocity: \(v_{\text{back}} > v_{\text{front}}\). If a sphere moves towards a wall (or towards another sphere moving the opposite way), it hits it. A sphere that has been stopped by an impact has velocity 0 and meets any sphere that comes back.
:::

:::eg Three smooth spheres \(A\), \(B\) and \(C\), of masses 2 kg, 2 kg and 1 kg, lie in a straight line, in that order, on a smooth horizontal table, with \(B\) and \(C\) at rest. \(A\) moves towards \(B\) at 12 m s⁻¹. The coefficient of restitution between any two spheres is 0.5. Find the speeds of \(A\), \(B\) and \(C\) after \(B\) has hit \(C\), and say whether any further collision occurs.
**\(A\) hits \(B\).** Momentum: \(2 \times 12 = 2v_A + 2v_B\), so \(v_A + v_B = 12\). Newton's law: \(v_B - v_A = 0.5 \times 12 = 6\). Adding: \(2v_B = 18\), so \(v_B = 9\) and \(v_A = 3\).

**\(B\) hits \(C\).** Let their speeds after be \(w_B\) and \(w_C\). Momentum: \(2 \times 9 = 2w_B + w_C\). Law: \(w_C - w_B = 0.5 \times 9 = 4.5\). Substitute \(w_C = w_B + 4.5\):
\[18 = 2w_B + w_B + 4.5 \quad\Rightarrow\quad w_B = 4.5, \quad w_C = 9\]
**Further collisions.** \(A\) moves at 3 m s⁻¹ and \(B\) at 4.5 m s⁻¹ in the same direction, so \(B\) is moving away from \(A\) and they do not collide again. \(C\) moves at 9, faster than \(B\), so \(B\) does not catch \(C\). There are no further collisions.
:::

When the answer depends on a parameter, the condition for a second collision gives an inequality in \(e\). This is exactly how exam questions are built: the statement "show that there is no further collision if \(e > \ldots\)" means exactly this comparison.

:::eg (Exam style) Three smooth spheres \(A\), \(B\) and \(C\), of masses \(2m\), \(2m\) and \(m\), lie in a straight line in that order on a smooth horizontal table, with \(B\) and \(C\) at rest. \(A\) moves directly towards \(B\) with speed \(u\). The coefficient of restitution between any two spheres is \(e\). (a) Find, in terms of \(u\) and \(e\), the speeds of \(A\) and \(B\) after their impact. (b) \(B\) then collides with \(C\). Show that the speed of \(B\) after this second impact is \(\dfrac{(1 + e)(2 - e)u}{6}\). (c) Show that \(A\) and \(B\) collide a second time if and only if \(e < 2 - \sqrt3\).
**(a)** Momentum: \(2mu = 2mv_A + 2mv_B\), so \(v_A + v_B = u\). [M1]
Law: \(v_B - v_A = eu\). [M1]
\[v_B = \frac{(1 + e)u}{2} \qquad v_A = \frac{(1 - e)u}{2}\] [A1 A1]
**(b)** Let the speeds of \(B\) and \(C\) after their impact be \(w_B\) and \(w_C\). Momentum: \(2mv_B = 2mw_B + mw_C\). [M1]
Law: \(w_C - w_B = ev_B\). So \(2v_B = 2w_B + w_B + ev_B\), giving
\[w_B = \frac{(2 - e)v_B}{3} = \frac{(1 + e)(2 - e)u}{6}\] [A1]
(The speed of \(C\) is \(w_C = w_B + ev_B = \dfrac{(1 + e)^2u}{3}\), which is not needed here.)

**(c)** \(A\) catches \(B\) if and only if \(A\) is faster than \(B\) after \(B\)'s impact with \(C\):
\[v_A > w_B\] [M1]
\[\frac{(1 - e)u}{2} > \frac{(1 + e)(2 - e)u}{6}\] [A1]
Multiply by \(\dfrac{6}{u}\):
\[3(1 - e) > (1 + e)(2 - e) = 2 + e - e^2\]
\[e^2 - 4e + 1 > 0\] [A1]
The roots of \(e^2 - 4e + 1 = 0\) are \(e = 2 \pm \sqrt3\). Since \(2 + \sqrt3 > 1\), and \(0 \le e \le 1\), the inequality holds if and only if \(e < 2 - \sqrt3\). [A1]
:::

For \(e = 0.5\), above \(2 - \sqrt3 = 0.268\), the previous example found no second collision. For \(e = 0.2\) there is one: with \(u = 10\) the speeds are \(v_A = 4\) and \(w_B = 3.6\), so \(A\) catches \(B\). To follow the whole sequence you simply repeat the two equations for the new pair, using the new velocities as "before".

## Impulse in a collision

The impulse that one sphere exerts on the other during the impact is the change of momentum of either one. By Newton's third law the two impulses are equal and opposite.

:::key Impulse between two spheres
\[I = m_2(v_2 - u_2) = m_1(u_1 - v_1) = \frac{m_1m_2(1 + e)(u_1 - u_2)}{m_1 + m_2}\]
The third form comes from substituting the velocities after the impact. For a sphere hitting a fixed wall, \(I = m(1 + e)u\).
:::

For the spheres of mass 2 kg and 3 kg earlier (\(u_1 - u_2 = 6\), \(e = 0.5\)), the impulse on \(B\) is \(3(2.6 - (-1)) = 10.8\) N s, and the formula gives \(\dfrac{2 \times 3 \times 1.5 \times 6}{5} = 10.8\) N s. An impulse is a vector: say the direction (along the line of centres, from \(A\) towards \(B\)) as well as the size.

:::exam What to write and what is on MF19
Newton's experimental law and \(e\) are **not** on MF19: learn \(v_2 - v_1 = e(u_1 - u_2)\) and the meaning of \(e = 0\) and \(e = 1\). Start every collision question with a diagram: "before" and "after" rows, a positive direction, and unknown velocities drawn in the positive direction. State the two equations separately, labelled "momentum" and "NEL" (or "Newton's law"); each is a method mark. Use full calculator values and round only at the end. When a question says "show that", the given value must come out of your working, not be assumed. Check that, after the impact, the front sphere is not slower than the back one.
:::

:::board
Edexcel IAL and the UK A Levels use \(g = 9.8\) where 9231 uses \(g = 10\); this matters for the bouncing-ball heights and times. 9231 calls the law Newton's experimental law; many textbooks write Newton's law of restitution. The equations and the meaning of \(e\) are the same.
:::

:::eg Spot the error: a smooth sphere \(A\) of mass 3 kg moving at 6 m s⁻¹ collides directly with a smooth sphere \(B\) of mass 2 kg moving towards it at 2 m s⁻¹. The coefficient of restitution is 0.5. Find the speeds of \(A\) and \(B\) after the impact, for 6 marks.
A student wrote this answer.

Line 1: Momentum, \(A\) positive: \(3 \times 6 + 2 \times 2 = 3v_1 + 2v_2\), so \(3v_1 + 2v_2 = 22\)
Line 2: NEL: \(v_2 - v_1 = 0.5 \times (6 - 2) = 2\)
Line 3: \(v_2 = v_1 + 2\), so \(5v_1 + 4 = 22\) and \(v_1 = 3.6\), \(v_2 = 5.6\)

Line 1 uses a method of the right type: a momentum equation with the right masses and velocities. [M1] **But the student has used \(+2\) for the velocity of \(B\)**, which is moving towards \(A\), in the negative direction, so the equation should read \(18 - 4 = \ldots\). [A0] The same slip is in line 2: the approach speed is \(6 - (-2) = 8\), not 4. The law is written correctly, so the method mark is earned [M1] but the accuracy mark is lost. [A0] Line 3 solves the pair of equations correctly [DM1], so the method mark that depends on the two before it is earned, but the answers are wrong. [A0] The student scores 3 out of 6. A check with the law shows the slip: the correct separation speed is \(0.5 \times 8 = 4\), but the student's numbers separate at only \(5.6 - 3.6 = 2\).

Correct line 1: \(18 - 4 = 14 = 3v_1 + 2v_2\). Correct line 2: \(v_2 - v_1 = 0.5 \times 8 = 4\). Then \(5v_1 + 8 = 14\), so \(v_1 = 1.2\) and \(v_2 = 5.2\). [A1]
:::

:::try Start easy, finish at exam standard
Q: A ball of mass 0.5 kg moving at 8 m s⁻¹ is brought to rest by a wall in 0.02 s. Find the impulse and the average force.
A: Take the initial direction as positive: \(I = 0.5 \times 0 - 0.5 \times 8 = -4\) N s, so the wall exerts an impulse of magnitude 4 N s. The average force is \(\dfrac{4}{0.02} = 200\) N.
Q: A sphere of mass 2 kg moving at 6 m s⁻¹ hits a stationary sphere of mass 4 kg, and \(e = 0\). Find the common speed after, and the kinetic energy lost.
A: Momentum: \(12 = 6v\), so \(v = 2\) m s⁻¹. KE before \(= 36\) J, after \(= \tfrac12(6)(4) = 12\) J. Lost: 24 J. (Check: \(\dfrac{2 \times 4}{2 \times 6}(1 - 0)(36) = 24\).)
Q: Two equal spheres of mass \(m\) collide directly with \(e = 1\); \(A\) moves at 5 m s⁻¹ and \(B\) at 1 m s⁻¹ in the same direction. Find their velocities after.
A: Equal masses and \(e = 1\): the velocities are exchanged, so \(A\) moves at 1 m s⁻¹ and \(B\) at 5 m s⁻¹. (Momentum: \(6m\) before and after. Law: \(5 - 1 = 1 \times (5 - 1)\).)
Q: A ball is dropped from 5 m onto a floor and rebounds to 3.2 m. Find \(e\) (take \(g = 10\)).
A: Height scales as \(e^2\): \(e^2 = \dfrac{3.2}{5} = 0.64\), so \(e = 0.8\). (Impact speed 10 m s⁻¹, rebound speed 8.)
Q: A sphere of mass 1 kg moves at 4 m s⁻¹ and hits a stationary sphere of mass 3 kg. \(e = \tfrac13\). Find the velocities after the impact.
A: Momentum: \(4 = v_1 + 3v_2\). Law: \(v_2 - v_1 = \tfrac13 \times 4 = \tfrac43\). So \(v_1 = v_2 - \tfrac43\) and \(4v_2 - \tfrac43 = 4\), giving \(v_2 = \tfrac43\) and \(v_1 = 0\). The first sphere is brought to rest.
Q: A ball hits a smooth wall at 10 m s⁻¹ and loses \(36\%\) of its kinetic energy. Find \(e\).
A: Speed after \(= 10e\), KE after \(= e^2\) times KE before. \(e^2 = 0.64\), so \(e = 0.8\).
Q: Spheres \(A\) (mass 3 kg, velocity \(+4\)) and \(B\) (mass 1 kg, velocity \(-2\)) collide with \(e = 0.5\). Find the impulse exerted on \(B\).
A: \(I = \dfrac{m_1m_2(1 + e)(u_1 - u_2)}{m_1 + m_2} = \dfrac{3 \times 1 \times 1.5 \times 6}{4} = 6.75\) N s.
Q: Explain why momentum is conserved when two spheres collide on a smooth table but not when a sphere hits a fixed wall.
A: Between the two spheres the forces are an equal and opposite pair (Newton's third law), so the total momentum of the pair is unchanged. A fixed wall exerts an external impulse on the sphere, and the wall (with the ground it is fixed to) takes the momentum, so the sphere's momentum alone is not conserved.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A ball of mass 0.25 kg approaches a racket at 12 m s⁻¹ and leaves it in the opposite direction at 20 m s⁻¹. (a) Find the magnitude of the impulse of the racket on the ball. (b) Find the average force if the contact lasts 0.02 s.
A: (a) \(I = 0.25 \times 20 - 0.25 \times (-12)\) [M1] \(= 8\) N s. [A1]
(b) \(F = \dfrac{8}{0.02} = 400\) N. [A1]
Q: [4 marks] ★ A smooth sphere \(A\) of mass 0.5 kg moving at 6 m s⁻¹ collides directly with a stationary smooth sphere \(B\) of mass 0.3 kg. The coefficient of restitution is 0.4. Find the speeds of \(A\) and \(B\) after the impact.
A: Momentum: \(3 = 0.5v_A + 0.3v_B\). [M1] Law: \(v_B - v_A = 0.4 \times 6 = 2.4\). [M1] Substituting: \(3 = 0.5v_A + 0.3v_A + 0.72\), so \(v_A = 2.85\) m s⁻¹ [A1] and \(v_B = 5.25\) m s⁻¹. [A1]
Q: [6 marks] ★★ A ball of mass 0.2 kg hits a smooth vertical wall directly at 10 m s⁻¹. The coefficient of restitution is 0.7. Find (a) the speed of the ball after the impact, (b) the magnitude of the impulse of the wall on the ball, (c) the kinetic energy lost.
A: (a) \(v = eu = 7\) m s⁻¹. [M1 A1]
(b) \(I = 0.2(7 + 10)\) [M1] \(= 3.4\) N s. [A1]
(c) \(\tfrac12(0.2)(100 - 49)\) [M1] \(= 5.1\) J. [A1]
Q: [6 marks] ★★ A ball is dropped from rest at a height of 5 m above a horizontal floor. The coefficient of restitution is 0.8. Take \(g = 10\). (a) Find the speed of the ball just before it first hits the floor. (b) Find the height to which it rises after its second impact with the floor. (c) Find the total distance travelled by the ball before it comes to rest.
A: (a) \(v^2 = 2 \times 10 \times 5 = 100\), so \(v = 10\) m s⁻¹. [M1 A1]
(b) Each impact multiplies the height by \(e^2 = 0.64\), so after the second impact the height is \(5 \times 0.64^2\) [M1] \(= 2.048\) m (2.05 m to 3 s.f.). [A1]
(c) \(D = 5 + 2\left(\dfrac{3.2}{1 - 0.64}\right)\) [M1] \(= 5 + 17.78 = 22.8\) m. [A1]
Q: [7 marks] ★★ A smooth sphere \(A\) of mass 4 kg moving at 6 m s⁻¹ collides directly with a smooth sphere \(B\) of mass 2 kg moving towards it at 3 m s⁻¹. After the collision \(A\) is moving in its original direction at 2 m s⁻¹. (a) Find the speed of \(B\) after the collision. (b) Show that the coefficient of restitution is \(\tfrac13\). (c) Find the kinetic energy lost.
A: (a) Momentum: \(4 \times 6 - 2 \times 3 = 4 \times 2 + 2v_B\) [M1], so \(18 = 8 + 2v_B\) and \(v_B = 5\) m s⁻¹ in \(A\)'s original direction. [A1]
(b) Law: \(5 - 2 = e(6 - (-3))\) [M1], so \(3 = 9e\) [A1] and \(e = \tfrac13\). [A1]
(c) KE before \(= \tfrac12(4)(36) + \tfrac12(2)(9) = 81\) J; after \(= \tfrac12(4)(4) + \tfrac12(2)(25) = 33\) J [M1]. Lost: 48 J. [A1]
Q: [8 marks] ★★★ A smooth sphere \(A\) of mass \(m\) lies on a smooth horizontal table, with a second smooth sphere \(B\) of mass \(3m\) at rest on the same line, and a fixed smooth vertical wall perpendicular to the line, beyond \(B\). \(A\) is projected with speed \(u\) towards \(B\). The coefficient of restitution between any two bodies is \(e\), where \(e < \tfrac13\). (a) Find the velocities of \(A\) and \(B\) after their first impact. (b) \(B\) hits the wall and rebounds. Show that \(A\) and \(B\) collide again.
H: Use the result \(v_B = \dfrac{(1 + e)u}{4}\) from the working with masses \(m\) and \(3m\) (derive it again with the two equations).
H: With \(e < \tfrac13\), \(A\) keeps moving towards the wall. After the wall, \(B\) moves back towards \(A\).
H: When two spheres approach each other along a line they must collide, as long as there is no wall in between.
A: (a) Momentum: \(mu = mv_A + 3mv_B\). [M1] Law: \(v_B - v_A = eu\). [M1] So \(4v_B = (1 + e)u\), \(v_B = \dfrac{(1 + e)u}{4}\) [A1] and \(v_A = \dfrac{(1 - 3e)u}{4}\), which is positive as \(e < \tfrac13\). [A1]
(b) \(B\) hits the wall with speed \(\dfrac{(1 + e)u}{4}\) and rebounds with speed \(e\dfrac{(1 + e)u}{4}\) back towards \(A\). [M1 A1] \(A\) is still moving towards the wall, since \(v_A > 0\), so \(A\) and \(B\) are now moving towards each other. [B1] Two spheres approaching each other along a line must collide, so \(A\) and \(B\) collide again. [A1]
Q: [10 marks] ★★★ A smooth sphere \(A\) of mass \(2m\) moving at speed \(u\) collides directly with a stationary smooth sphere \(B\) of mass \(m\). The coefficient of restitution between the spheres is \(e\). (a) Show that the speeds of \(A\) and \(B\) after the collision are \(\dfrac{(2 - e)u}{3}\) and \(\dfrac{2(1 + e)u}{3}\). (b) The total kinetic energy after the collision is \(\tfrac34\) of the kinetic energy before. Find \(e\). (c) Find the magnitude of the impulse of \(A\) on \(B\).
H: Take the direction of \(A\) as positive and solve the two equations as in the general case.
H: Kinetic energy before is \(mu^2\). Add the two kinetic energies after, in terms of \(e\).
H: The impulse on \(B\) is its change of momentum.
A: (a) \(2mu = 2mv_A + mv_B\) [M1], \(v_B - v_A = eu\) [M1]. So \(2u = 2v_A + v_A + eu\), giving \(v_A = \dfrac{(2 - e)u}{3}\) [A1] and \(v_B = v_A + eu = \dfrac{(2 + 2e)u}{3}\). [A1]
(b) KE after \(= \tfrac12(2m)\dfrac{(2 - e)^2u^2}{9} + \tfrac12m\dfrac{4(1 + e)^2u^2}{9} = \dfrac{mu^2}{9}\left[(2 - e)^2 + 2(1 + e)^2\right]\) [M1]. The bracket is \(4 - 4e + e^2 + 2 + 4e + 2e^2 = 6 + 3e^2\), so KE after \(= \dfrac{mu^2(2 + e^2)}{3}\). [A1] Set equal to \(\tfrac34mu^2\): \(2 + e^2 = \tfrac94\) [M1], so \(e^2 = \tfrac14\) and \(e = 0.5\). [A1]
(c) \(I = m(v_B - 0) = \dfrac{2m(1.5)u}{3}\) [M1] \(= mu\). [A1]
Q: [9 marks] (#math.p1.series) ★★★ A ball is dropped from rest at a height of 1.8 m above a horizontal floor and bounces repeatedly. The coefficient of restitution is 0.5. Take \(g = 10\). (a) Find the speed of the ball just before and just after its first impact. (b) Find the time between the first and second impacts. (c) Show that the total time until the ball comes to rest is 1.8 s. (d) Find the total distance travelled.
H: Time of flight for a launch speed \(w\) straight up is \(\dfrac{2w}{g}\).
H: The times between impacts form a geometric sequence with ratio \(e\).
H: The heights form a geometric sequence with ratio \(e^2\).
A: (a) \(v^2 = 2 \times 10 \times 1.8 = 36\), so before: 6 m s⁻¹; after: \(0.5 \times 6 = 3\) m s⁻¹. [M1 A1]
(b) \(\dfrac{2 \times 3}{10} = 0.6\) s. [M1 A1]
(c) The first fall takes \(\dfrac{6}{10} = 0.6\) s. The later flights are \(0.6, 0.3, 0.15, \ldots\), with ratio 0.5. [M1] Total \(= 0.6 + \dfrac{0.6}{1 - 0.5}\) [M1] \(= 1.8\) s. [A1]
(d) The first fall is 1.8 m. The heights after the impacts are \(0.45, 0.1125, \ldots\) with ratio 0.25, each travelled twice: \(D = 1.8 + 2 \times \dfrac{0.45}{0.75}\) [M1] \(= 3\) m. [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A heavy ball of mass 0.6 kg lies directly beneath a light ball of mass 0.1 kg, touching it. They are dropped together from a height of 1.25 m above a horizontal floor. Model both as particles and every impact (ball and floor, ball and ball) as perfectly elastic, with the second impact taking place at floor level just after the first. Take \(g = 10\). (a) Find the speed of the heavy ball just after it hits the floor. (b) Find the speed of the light ball just after the two balls collide. (c) Find the greatest height above the floor reached by the light ball, and compare it with 1.25 m.
H: The heavy ball rises at 5 m s⁻¹ and the light ball is still moving down at 5 m s⁻¹ when they meet.
H: Take upwards as positive: the velocities before their collision are \(+5\) and \(-5\); use momentum and the law with \(e = 1\).
A: (a) Both balls fall at \(\sqrt{2 \times 10 \times 1.25} = 5\) m s⁻¹. [B1] The heavy ball rebounds at 5 m s⁻¹ upwards. [B1]
(b) Take upwards as positive. Momentum: \(0.6 \times 5 + 0.1 \times (-5) = 0.6V_1 + 0.1V_2\), so \(6V_1 + V_2 = 25\). [M1] Law: \(V_2 - V_1 = 5 - (-5) = 10\). [M1] Then \(7V_1 + 10 = 25\), \(V_1 = \tfrac{15}{7}\), and \(V_2 = \tfrac{85}{7} = 12.1\) m s⁻¹ upwards. [A1]
(c) The height is \(\dfrac{V_2^2}{2g} = \dfrac{(85/7)^2}{20} = 7.37\) m [M1], which is nearly six times the drop height of 1.25 m: the heavy ball has transferred energy to the light one. [A1]
Q: [6 marks] ★★★ A smooth sphere of mass \(m_1\) moving at speed \(u\) hits a stationary smooth sphere of mass \(m_2\), with coefficient of restitution \(e\). The first sphere is brought to rest by the impact. Show that \(m_1 = em_2\), and that the fraction of the original kinetic energy lost is \(1 - e\).
H: From the formula for \(v_A\), set it to 0.
H: The second sphere's speed is then \(\dfrac{m_1(1 + e)u}{m_1 + m_2}\); use \(m_1 = em_2\) to simplify it.
A: Momentum \(m_1u = m_1v_A + m_2v_B\) and law \(v_B - v_A = eu\) [M1]. With \(v_A = 0\): \(v_B = eu\) [A1] and \(m_1u = m_2eu\), so \(m_1 = em_2\). [A1]
KE after \(= \tfrac12m_2e^2u^2\). [M1] With \(m_2 = \dfrac{m_1}{e}\), this is \(\tfrac12m_1eu^2\), which is \(e\) times the original \(\tfrac12m_1u^2\). [A1] So the fraction lost is \(1 - e\). [A1]
:::

:::quiz
? Newton's experimental law for a direct collision says:
- the speed of each sphere after the impact is \(e\) times its speed before
+ the speed of separation is \(e\) times the speed of approach
- the total momentum after is \(e\) times the total before
- the kinetic energy after is \(e\) times the kinetic energy before
> The law compares how fast the spheres move apart with how fast they closed. Multiplying each speed by \(e\) works only for a sphere hitting a fixed wall, and it is the kinetic energy that is multiplied by \(e^2\) in that case. The total momentum of two spheres is conserved, not multiplied by \(e\).
? What does \(e = 0\) mean?
- the spheres stop dead
+ the spheres move on together after the impact
- the spheres exchange velocities
- no momentum is lost
> If \(e = 0\), the separation speed is zero, so both spheres have the same velocity: they stay together. Exchanging velocities is the case \(e = 1\) for equal masses, and momentum is conserved whatever \(e\) is, so "no momentum is lost" does not single out \(e = 0\).
? A ball is dropped from 4 m onto a floor, with \(e = 0.5\). To what height does it rise after the first impact?
- \(2\) m
+ \(1\) m
- \(0.5\) m
- \(3\) m
> The speed after is \(e\) times the speed before, and the height depends on the square of the speed, so it rises to \(e^2 \times 4 = 1\) m. The answer 2 forgets to square, 0.5 cubes \(e\), and 3 is the height lost.
? A ball hits a fixed wall. Which quantity is conserved?
- the ball's momentum
- the ball's kinetic energy
+ neither of these, unless \(e = 1\), when the energy is conserved
- both, as long as the wall is smooth
> The wall gives the ball an impulse, so its momentum changes (from \(mu\) to \(-emu\)). Kinetic energy changes unless \(e = 1\). Smoothness only means no friction.
? A sphere of mass 2 kg moving at 6 m s⁻¹ hits a stationary sphere of mass 1 kg, with \(e = 0\). What is their common speed after?
- \(6\) m s⁻¹
- \(3\) m s⁻¹
+ \(4\) m s⁻¹
- \(12\) m s⁻¹
> Momentum: \(12 = 3v\), so \(v = 4\). The answer 3 divides by 4, as if the masses added to 4, and 6 would mean the lighter sphere shared none of the momentum.
? The impulse that a force exerts on a particle over a time interval equals:
+ the change of momentum of the particle
- the change of kinetic energy of the particle
- the force multiplied by the distance
- the final momentum
> Impulse is \(\int F\,dt = mv - mu\). The change of kinetic energy is the work, \(\int F\,dx\); the final momentum alone ignores where the particle started.
:::

:::checklist What you can now do
- [ ] I can define impulse, find it as \(mv - mu\) or \(\int F\,dt\), and use the signs of the velocities correctly.
- [ ] I can state Newton's experimental law and the properties of the coefficient of restitution, including \(0 \le e \le 1\), perfectly elastic (\(e = 1\)) and inelastic (\(e = 0\)).
- [ ] I can use conservation of momentum and Newton's experimental law to find the velocities after a direct impact of two smooth spheres.
- [ ] I can find the kinetic energy lost, and use it to find \(e\).
- [ ] I can solve problems about a sphere hitting a fixed surface directly, including its impulse and the energy lost.
- [ ] I can find the heights, total distance and total time of a bouncing ball using a geometric series.
- [ ] I can follow successive impacts of three spheres, or spheres and a wall, and decide whether a further collision occurs, including a condition on \(e\).
:::

:::recap
- Impulse \(I = \int F\,dt = mv - mu\), in N s, a vector. Area under a force–time graph.
- Momentum is conserved for two spheres: \(m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\). It is not conserved when a sphere hits a fixed wall.
- Newton's experimental law: separation speed \(= e \times\) approach speed, \(v_2 - v_1 = e(u_1 - u_2)\). Not on MF19.
- \(0 \le e \le 1\): \(e = 1\) is perfectly elastic (kinetic energy conserved), \(e = 0\) is inelastic (spheres move together).
- Kinetic energy lost \(= \dfrac{m_1m_2}{2(m_1 + m_2)}(1 - e^2)(u_1 - u_2)^2\). Impulse between spheres \(= \dfrac{m_1m_2(1 + e)(u_1 - u_2)}{m_1 + m_2}\).
- Sphere and fixed wall: rebound speed \(eu\), impulse \(m(1 + e)u\), energy lost \(\tfrac12m(1 - e^2)u^2\).
- Bouncing ball dropped from \(h\): heights \(e^{2n}h\); total distance \(h\dfrac{1 + e^2}{1 - e^2}\); total time \(\sqrt{\dfrac{2h}{g}}\dfrac{1 + e}{1 - e}\).
- Successive collisions: repeat the two equations for each pair; a further collision needs the back sphere to be faster than the front one.
:::

:::links
- watch: [Newton's law of restitution playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NiPDYYt5yYtsPqnSbtedvrN) · ExamSolutions (YouTube) · direct impacts, walls and successive collisions worked step by step
- explore: [Collision lab](https://phet.colorado.edu/en/simulations/collision-lab) · PhET · set the elasticity and see the velocities after a collision
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · collision questions with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Paper 3 questions with mark schemes [unofficial]
- papers: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers sorted by year

Links checked 20 November 2026.
:::
Next: [Oblique impact](#math.fm.oblique) takes the same two laws to collisions where the spheres do not move along the line of centres, by splitting each velocity into two directions.
