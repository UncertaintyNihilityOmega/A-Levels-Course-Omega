@chapter math.fm.projectiles
@title Projectiles
@level fm
@paper CAIE 9231 Paper 3 · Edexcel IAL Mechanics 2 · UK A Level Mechanics
@time 5–6 hours
@summary A projectile is a particle that moves under gravity alone, so its horizontal motion is steady and its vertical motion has constant acceleration. You will resolve the launch velocity, find the time of flight, range, greatest height, and the speed and direction at any moment, launch from a height onto a higher or lower level, derive and use the Cartesian equation of the path (including problems with an unknown speed or angle and two possible angles), deal with a plane that the particle strikes, and say what the model leaves out.

:::why
A thrown ball, a shot put, water from a fountain and a stone dropped off a cliff all follow the same simple rules once you ignore the air. Splitting one curved motion into two straight ones, one steady and one accelerating, is among the most useful moves in mechanics, and Further Mathematics asks you to push it further than the single-particle questions of 9709: paths through a given point, two angles that both work, and a launch speed you must find.
:::

**Before you start**, you need the constant-acceleration equations from [Kinematics: describing motion](#math.m.kinematics), the idea of resolving a vector from [Forces and equilibrium](#math.m.forces), and the identity \(1 + \tan^2\theta = \sec^2\theta\) from [Further trigonometry](#math.p3.trig). Throughout, **take \(g = 10\,\mathrm{m\,s^{-2}}\)**, as the 9231 paper instructs.

:::try Warm-up
Q: A ball is thrown straight up at \(12\,\mathrm{m\,s^{-1}}\). How high does it rise? Take \(g = 10\). (from [Kinematics: describing motion](#math.m.kinematics))
A: At the top \(v = 0\), so \(0 = 12^2 - 2 \times 10 \times s\), giving \(s = \dfrac{144}{20} = 7.2\) m.
Q: Resolve a velocity of \(20\,\mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal into horizontal and vertical components. (from [Forces and equilibrium](#math.m.forces))
A: Horizontal \(20\cos 30^\circ = 17.3\,\mathrm{m\,s^{-1}}\), vertical \(20\sin 30^\circ = 10\,\mathrm{m\,s^{-1}}\).
Q: Write \(\dfrac{1}{\cos^2\theta}\) in terms of \(\tan\theta\). (from [Further trigonometry](#math.p3.trig))
A: \(\dfrac{1}{\cos^2\theta} = \sec^2\theta = 1 + \tan^2\theta\).
:::

## The model: a particle under gravity alone

Throw a ball and watch it. Its path is a smooth curve that rises, flattens at the top and falls. The curve looks complicated, but it hides a simple fact: **the horizontal and vertical motions do not affect each other**. Once the ball has left your hand nothing pushes it sideways, so its horizontal velocity stays the same. Gravity pulls it downwards, so its vertical velocity changes at a steady rate.

:::def Projectile
A body launched into the air and then moving freely under gravity alone. In this chapter it is modelled as a particle (a point with mass) that moves in a vertical plane.
:::

The word "model" matters: the equations are only as true as the assumptions behind them.

:::key The projectile model
- The body is a **particle**: it has no size, no spin and no shape.
- The only force on it is its **weight**, so its acceleration is \(g\) downwards, the same everywhere along the path (take \(g = 10\)).
- There is **no air resistance** and no wind.
- The ground is a flat horizontal plane (the Earth's curvature is ignored).

The consequences are what you use: **horizontal acceleration \(= 0\)** and **vertical acceleration \(= -g\)** (upwards taken as positive).
:::

## Components of the launch velocity

A projectile is launched with **speed** \(V\) at an **angle of projection** \(\theta\) above the horizontal. Take the launch point \(O\) as the origin, \(x\) horizontal and \(y\) vertically upwards. The launch velocity splits into two components.

:::html
<figure class="fig"><svg viewBox="20 40 410 215" role="img" aria-label="A projectile launched from point O on level ground with speed V at angle theta above the horizontal. The launch velocity V is split into a horizontal component V cos theta and a vertical component V sin theta. The path is a curve that rises to a greatest height H above the ground, where the velocity is horizontal and equal to V cos theta, then lands a horizontal distance R, the range, from O.">
  <path class="ln-m" d="M20 200H430"/>
  <path class="c2" d="M80 200Q240 -60 400 200"/>
  <path class="ln-m thin dot" d="M132.4 114.9V200M132.4 114.9H80"/>
  <path class="ln-m thin dash" d="M240 70V200"/>
  <path class="ln thick" d="M80 200L132.4 114.9" marker-end="url(#ah)"/>
  <path class="c1" d="M80 200H132.4" marker-end="url(#ah-math)"/>
  <path class="c1" d="M80 200V114.9" marker-end="url(#ah-math)"/>
  <path class="ln" d="M240 70H290" marker-end="url(#ah)"/>
  <path class="ln-m thin" d="M110 200A30 30 0 0 0 95.7 174.5"/>
  <path class="ln-m thin dot" d="M80 200V236M400 200V236"/>
  <path class="ln-m" d="M240 232H84" marker-end="url(#ahm)"/>
  <path class="ln-m" d="M240 232H396" marker-end="url(#ahm)"/>
  <circle class="fi" cx="80" cy="200" r="3.5"/>
  <text class="tl halo" x="66" y="214" text-anchor="end">O</text>
  <text class="tl" x="138" y="108">V</text>
  <text class="tl halo" x="106" y="217" text-anchor="middle">V cos θ</text>
  <text class="tl halo" x="74" y="160" text-anchor="end">V sin θ</text>
  <text class="tl" x="114" y="191">θ</text>
  <text class="tl halo" x="247" y="140">H</text>
  <text class="tl" x="265" y="62" text-anchor="middle">V cos θ</text>
  <text class="tl" x="240" y="250" text-anchor="middle">range R</text>
</svg><figcaption>A projectile launched from O with speed V at angle θ. The launch velocity has components V cos θ (horizontal) and V sin θ (vertical). At the greatest height H the vertical component is zero and the velocity is horizontal, V cos θ. The range R is measured along level ground.</figcaption></figure>
:::

The horizontal component is steady for the whole flight; the vertical component starts at \(V\sin\theta\) and loses \(g\) every second. Apply the constant-acceleration equations to each direction separately.

:::key Equations of motion for a projectile (origin at the launch point)
\[\begin{aligned}
\text{horizontal:}\quad x &= V\cos\theta\,t & v_x &= V\cos\theta \\
\text{vertical:}\quad y &= V\sin\theta\,t - \tfrac12gt^2 & v_y &= V\sin\theta - gt
\end{aligned}\]
Also \(v_y^2 = V^2\sin^2\theta - 2gy\). The **speed** at any moment is \(v = \sqrt{v_x^2 + v_y^2}\), and its direction makes an angle \(\varphi\) with the horizontal where \(\tan\varphi = \dfrac{\lvert v_y\rvert}{v_x}\): above the horizontal if \(v_y > 0\), below if \(v_y < 0\).
:::

:::eg A particle is projected from \(O\) on level ground with speed \(25\,\mathrm{m\,s^{-1}}\) at an angle \(\theta\) where \(\tan\theta = \tfrac34\). Find (a) its position and (b) its velocity \(2\) s later, (c) the times at which it is \(10\) m above the ground.
\(\tan\theta = \tfrac34\) gives \(\cos\theta = \tfrac45\) and \(\sin\theta = \tfrac35\) (a 3-4-5 triangle). So \(V\cos\theta = 20\) and \(V\sin\theta = 15\).

(a) At \(t = 2\):
\[x = 20 \times 2 = 40, \qquad y = 15 \times 2 - 5 \times 2^2 = 10\]
The particle is at \((40, 10)\): 40 m along and 10 m up.

(b) \(v_x = 20\) and \(v_y = 15 - 10 \times 2 = -5\). The speed is \(\sqrt{20^2 + 5^2} = \sqrt{425} = 20.6\,\mathrm{m\,s^{-1}}\). The minus sign says it is falling: the direction is \(\tan^{-1}\dfrac{5}{20} = 14.0^\circ\) below the horizontal.

(c) Put \(y = 10\):
\[\begin{aligned}
15t - 5t^2 &= 10 \\
t^2 - 3t + 2 &= 0 \\
(t - 1)(t - 2) &= 0
\end{aligned}\]
So \(t = 1\) (on the way up) and \(t = 2\) (on the way down). A height below the maximum is reached twice.
:::

## Time of flight, greatest height and range

On level ground you can answer three standard questions from the equations above.

- **Greatest height.** At the top the vertical velocity is zero, so \(0 = V\sin\theta - gt\) gives the time to the top, \(t = \dfrac{V\sin\theta}{g}\). Then \(H = \dfrac{(V\sin\theta)^2}{2g}\).
- **Time of flight.** The particle returns to \(y = 0\) when \(V\sin\theta\,t - \tfrac12gt^2 = 0\), so \(t = 0\) (the launch) or \(t = \dfrac{2V\sin\theta}{g}\). This is twice the time to the top, because the path is symmetric.
- **Range.** The horizontal distance in that time is \(R = V\cos\theta \times \dfrac{2V\sin\theta}{g}\).

:::key Level ground: height, time and range
\[H = \frac{V^2\sin^2\theta}{2g} \qquad T = \frac{2V\sin\theta}{g} \qquad R = \frac{V^2\sin 2\theta}{g}\]
The range form uses \(2\sin\theta\cos\theta = \sin 2\theta\). **These three results are not on MF19**: learn them or, better, know how to derive them in a minute from the equations of motion.
:::

:::eg (Exam style) A particle is projected from a point \(O\) on horizontal ground with speed \(V\) at an angle \(\theta\) above the horizontal. Show that the range on the ground is \(\dfrac{V^2\sin 2\theta}{g}\). Hence find the greatest possible range for a speed of \(30\,\mathrm{m\,s^{-1}}\), and the angles of projection at which a target \(80\) m away is hit.
Vertical motion: \(y = V\sin\theta\,t - \tfrac12gt^2\). The particle is back on the ground when \(y = 0\):
\[t\left(V\sin\theta - \tfrac12gt\right) = 0\] [M1]
so \(t = \dfrac{2V\sin\theta}{g}\) (the other root \(t = 0\) is the launch). [A1]

Horizontal motion at constant speed \(V\cos\theta\):
\[R = V\cos\theta \times \frac{2V\sin\theta}{g}\] [M1]
\[= \frac{V^2 \times 2\sin\theta\cos\theta}{g} = \frac{V^2\sin 2\theta}{g}\] [A1]
The greatest value of \(\sin 2\theta\) is 1, at \(\theta = 45^\circ\), so \(R_{\max} = \dfrac{30^2}{10} = 90\) m. [B1]

For \(R = 80\): \(\sin 2\theta = \dfrac{80 \times 10}{900} = 0.8889\). [M1]
\[2\theta = 62.73^\circ \quad\text{or}\quad 2\theta = 180^\circ - 62.73^\circ = 117.27^\circ\]
\[\theta = 31.4^\circ \quad\text{or}\quad \theta = 58.6^\circ\] [A1]
**Check**: the two angles add to \(90^\circ\), as they must (see below).
:::

:::plot The range on level ground is proportional to sin 2θ. It is greatest at θ = 45°, and two angles that add up to 90° give the same range: the curve is symmetric about θ = 45°.
--f "sin(2*x)+0*sqrt(90-x)" --label "R ÷ (V²/g) = sin 2θ" --x 0 118 --y 0 1.3 --deg --xlabel "θ (degrees)" --pt "45,1,(45°, 1)@n" --pt "30,0.866,30°@nw" --pt "60,0.866,60°@ne" --legend tr
:::

The graph is symmetric about \(45^\circ\) because \(\sin 2\theta = \sin(180^\circ - 2\theta) = \sin 2(90^\circ - \theta)\). So **angles \(\theta\) and \(90^\circ - \theta\) give the same range**: the flatter shot takes less time, the steeper one more, and the product \(V\cos\theta \times T\) comes out the same. Try it:

:::html
<div class="widget" data-w="projectile" data-speed="20" data-angle="30" data-height="0"></div>
:::

Press Launch at \(30^\circ\) and note the range (keep \(g = 10\)). Then set the angle to \(60^\circ\) with the same speed and launch again: the range is the same, but the high shot stays up longer and climbs three times as high. Then try \(45^\circ\) for the longest range. (The widget starts on level ground; the sections below go beyond it.)

## Speed and direction at a point

A question may give a position, not a time. For the speed there is a shortcut. Eliminate \(\theta\) from \(v_x^2 + v_y^2\) using \(v_y^2 = V^2\sin^2\theta - 2gy\):
\[v^2 = V^2\cos^2\theta + V^2\sin^2\theta - 2gy = V^2 - 2gy\]
This is conservation of energy ([Work, energy and power](#math.m.energy)): the speed at a height depends only on the launch speed and the height, not on the angle.

:::key Speed at height \(y\) above the launch point
\[v^2 = V^2 - 2gy\]
Use it for speed only. For direction you still need \(v_x = V\cos\theta\) (unchanged) and \(v_y\) at that point from \(v_y^2 = V^2\sin^2\theta - 2gy\), taking the negative root if the particle is falling.
:::

## Launching from a height, landing at another level

When the launch and landing points are at different heights the symmetric results no longer apply, but the method is unchanged: write \(y\) at the landing point and solve the quadratic in \(t\).

- **Landing on lower ground** (a cliff or tower): \(y\) is negative at landing. The quadratic has one positive and one negative root: reject the negative time.
- **Landing on higher ground** (a roof, a platform): the quadratic can have two positive roots. They are the times on the way up and on the way down. If the roof is first reached after the top of the path, take the **later** time. Always check which root puts the particle over the roof.

:::eg (Exam style) A stone is thrown from the top of a vertical cliff, \(40\) m above the sea, with speed \(20\,\mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal. Find (a) the time taken to reach the sea, (b) the horizontal distance of the landing point from the foot of the cliff, (c) the speed and direction of the stone as it hits the sea.
Take \(O\) at the top of the cliff. \(V\cos 30^\circ = 17.32\) and \(V\sin 30^\circ = 10\). The sea is at \(y = -40\).

(a)
\[\begin{aligned}
-40 &= 10t - 5t^2 \\
5t^2 - 10t - 40 &= 0 \\
t^2 - 2t - 8 &= 0 \\
(t - 4)(t + 2) &= 0
\end{aligned}\] [M1 A1]
\(t = 4\) s; the root \(t = -2\) is rejected because the stone was not in the air before it was thrown. [A1]

(b) Horizontal distance:
\[x = 17.32 \times 4 = 69.3\ \text{m}\] [M1 A1]
(c) \(v_y = 10 - 10 \times 4 = -30\), and \(v_x = 17.32\). [B1]
\[v = \sqrt{17.32^2 + 30^2} = \sqrt{1200} = 34.6\,\mathrm{m\,s^{-1}}\] [M1 A1]
\[\tan\varphi = \frac{30}{17.32} \quad\Rightarrow\quad \varphi = 60.0^\circ \text{ below the horizontal}\] [A1]
**Check** with the energy shortcut: \(v^2 = V^2 - 2gy = 400 + 2 \times 10 \times 40 = 1200\). ✓.
:::

:::eg A ball is hit from the ground with speed \(25\,\mathrm{m\,s^{-1}}\) at an angle \(\theta\) with \(\tan\theta = \tfrac34\). A flat roof, \(10\) m above the ground, runs from a horizontal distance of \(30\) m to \(60\) m from the launch point. Does the ball land on the roof, and with what velocity?
From the first example of this chapter, \(V\cos\theta = 20\), \(V\sin\theta = 15\) and the ball is at height \(10\) m when \(t = 1\) and \(t = 2\).

At \(t = 1\): \(x = 20\) m, short of the roof (which starts at 30 m). At \(t = 2\): \(x = 40\) m, over the roof. So the ball lands on the roof at \(t = 2\), on its way down.

The velocity then is \(v_x = 20\) and \(v_y = 15 - 20 = -5\), so the speed is \(\sqrt{425} = 20.6\,\mathrm{m\,s^{-1}}\) at \(14.0^\circ\) below the horizontal.

The ball lands at 40 m along the roof, 10 m from the near edge. Had we taken \(t = 1\) the ball would be in mid-air in front of the building: the choice of root is the whole question.
:::

:::eg A ball rolls off the edge of a table \(0.8\) m high with horizontal speed \(3\,\mathrm{m\,s^{-1}}\). Find where it lands and its speed and direction just before landing.
Launched horizontally, so the angle of projection is \(0\): \(v_x = 3\) and the initial vertical velocity is zero. The floor is at \(y = -0.8\):
\[\begin{aligned}
-0.8 &= -5t^2 \\
t^2 &= 0.16 \\
t &= 0.4\ \text{s}
\end{aligned}\]
Horizontal distance: \(3 \times 0.4 = 1.2\) m from the table. Then \(v_y = -10 \times 0.4 = -4\), so
\[v = \sqrt{3^2 + 4^2} = 5\,\mathrm{m\,s^{-1}}, \qquad \tan\varphi = \tfrac43 \Rightarrow \varphi = 53.1^\circ \text{ below the horizontal}\]
:::

## The Cartesian equation of the trajectory

Often a question gives you the path through a point rather than a time. Eliminating \(t\) gives \(y\) as a function of \(x\), the **trajectory**.

:::eg (Exam style) A particle is projected from the origin with speed \(V\) at an angle \(\theta\) above the horizontal. Show that its path has equation \(y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}\).
Horizontal motion: \(x = V\cos\theta\,t\), so \(t = \dfrac{x}{V\cos\theta}\). [B1]

Vertical motion: \(y = V\sin\theta\,t - \tfrac12gt^2\). [M1]

Substitute for \(t\):
\[y = V\sin\theta \times \frac{x}{V\cos\theta} - \frac12g\left(\frac{x}{V\cos\theta}\right)^2\] [M1 A1]
\[y = x\tan\theta - \frac{gx^2}{2V^2\cos^2\theta}\] [A1]
:::

This equation **is on MF19**, so in a question that says "show that" you still write the derivation, but when you only need to *use* it you may quote it from the booklet. Replace \(\dfrac{1}{\cos^2\theta}\) by \(1 + \tan^2\theta\) and it becomes the form that is much easier to use when \(\theta\) is unknown:

:::key The trajectory, two forms
\[y = x\tan\theta - \frac{gx^2}{2V^2\cos^2\theta} \qquad\text{or}\qquad y = x\tan\theta - \frac{gx^2}{2V^2}\left(1 + \tan^2\theta\right)\]
Valid for a launch from the origin. The path is a parabola. The second form is a **quadratic in \(\tan\theta\)** when \(x\), \(y\) and \(V\) are known, which is why two angles often work.
:::

### Through a given point: two angles

For a target at \((x, y)\) with a given speed, put the numbers into the second form. You get a quadratic in \(\tan\theta\); each positive root gives an angle. **Two roots mean two possible paths**, one flatter (a "low" shot) and one steeper (a "lob").

:::eg (Exam style) A ball is projected from a point \(O\) on horizontal ground with speed \(25\,\mathrm{m\,s^{-1}}\). It just clears the top of a vertical wall, \(8\) m high, at a horizontal distance of \(30\) m from \(O\). (a) Show that \(\tan\theta\) satisfies \(18\tan^2\theta - 75\tan\theta + 38 = 0\). (b) Find the two possible angles of projection. (c) Find the range of values of \(\tan\theta\) for which the ball passes above the top of the wall (that is, its height at \(x = 30\) is at least \(8\) m).
**(a)** Use the second form with \(x = 30\), \(y = 8\), \(V = 25\):
\[8 = 30\tan\theta - \frac{10 \times 30^2}{2 \times 25^2}\left(1 + \tan^2\theta\right)\] [M1 A1]
The coefficient is \(\dfrac{9000}{1250} = 7.2\). Write \(T = \tan\theta\):
\[\begin{aligned}
8 &= 30T - 7.2\left(1 + T^2\right) \\
7.2T^2 - 30T + 15.2 &= 0
\end{aligned}\] [M1]
Multiply by 2.5 to clear the decimals:
\[18T^2 - 75T + 38 = 0\] [A1]
**(b)** The quadratic formula:
\[T = \frac{75 \pm \sqrt{75^2 - 4 \times 18 \times 38}}{36} = \frac{75 \pm \sqrt{2889}}{36}\] [M1]
\[T = 3.576 \quad\text{or}\quad T = 0.5903\] [A1]
\[\theta = 74.4^\circ \quad\text{or}\quad \theta = 30.6^\circ\] [A1]
**(c)** The ball is above \(y = 8\) at \(x = 30\) when \(30T - 7.2(1 + T^2) \ge 8\), that is \(18T^2 - 75T + 38 \le 0\). The parabola opens upwards, so this holds between the roots:
\[0.590 \le \tan\theta \le 3.58\] [B1]
:::

:::plot Two paths from the same point O with the same speed 25 m/s both pass through (30, 8), the top of the wall: a low shot at 30.6° and a steep lob at 74.4°. The lob has a much greater height and lands sooner.
--f "x*0.5903-0.008*(1+0.5903**2)*x**2" --f "x*3.5764-0.008*(1+3.5764**2)*x**2" --label "θ = 30.6°" --label "θ = 74.4°" --x 0 58 --y 0 36 --pt "30,8,(30, 8)@ne" --legend tr
:::

:::warn One angle is only half the answer
When the target can be reached, the quadratic in \(\tan\theta\) has two positive roots, and the question almost always wants both. After solving, ask "is the other root also in range?" Check it by substituting back: both angles must give the right height at the target. If the discriminant is negative the target is out of reach at that speed.
:::

### An unknown speed or angle

Sometimes the unknown is \(V\), or both \(V\) and \(\theta\). With **one point** on the path and the angle given, substitute and solve for \(V^2\). With **two points** on the path and nothing else, treat \(\tan\theta\) and \(\dfrac{g(1 + \tan^2\theta)}{2V^2}\) as two unknown constants, solve the two simultaneous equations, and then recover \(V\) and \(\theta\).

:::eg A projectile is launched from the origin and passes through the points \((20, 10)\) and \((40, 10)\). Find the angle of projection and the launch speed. Take \(g = 10\).
Write the second form as \(y = Tx - Kx^2\) with \(T = \tan\theta\) and \(K = \dfrac{g\left(1 + T^2\right)}{2V^2}\):
\[\begin{aligned}
10 &= 20T - 400K \\
10 &= 40T - 1600K
\end{aligned}\]
Double the first equation and subtract the second: \(10 = 800K\), so \(K = \tfrac{1}{80}\). Then \(20T = 10 + 5 = 15\), so \(T = \tfrac34\) and \(\theta = 36.9^\circ\).

Now \(K = \dfrac{10 \times \frac{25}{16}}{2V^2} = \dfrac{1}{80}\) gives \(V^2 = \dfrac{10 \times \frac{25}{16} \times 80}{2} = 625\), so \(V = 25\,\mathrm{m\,s^{-1}}\).

**Check**: these are the same numbers as the first example, where \(t = 1\) and \(t = 2\) gave \(x = 20\) and \(x = 40\) at height 10 m. The top of the path is midway, at \(x = 30\).
:::

:::eg A basketball player releases the ball \(2.0\) m above the floor at an angle of \(50^\circ\) above the horizontal. The hoop is \(4.2\) m away horizontally and \(3.05\) m above the floor. Find the release speed that sends the ball through the centre of the hoop, and the time the ball takes to get there.
Take the release point as the origin: the hoop is at \(x = 4.2\), \(y = 3.05 - 2.0 = 1.05\).
\[1.05 = 4.2\tan 50^\circ - \frac{10 \times 4.2^2}{2V^2\cos^2 50^\circ}\]
With \(4.2\tan 50^\circ = 5.005\) and \(2\cos^2 50^\circ = 0.8264\):
\[\frac{176.4}{0.8264V^2} = 5.005 - 1.05 = 3.955\]
\[V^2 = \frac{176.4}{0.8264 \times 3.955} = 53.97, \qquad V = 7.35\,\mathrm{m\,s^{-1}}\]
Time: \(t = \dfrac{x}{V\cos\theta} = \dfrac{4.2}{7.346 \times 0.6428} = 0.889\) s.
:::

## A projectile that meets a plane

So far the ground was horizontal. A particle can also land on a slope. The method is always the same: write the equation of the slope as a line through the launch point in the same axes, put the particle's coordinates into it to find the time, and then use the velocity components at that time.

If the particle **strikes the plane at right angles**, its velocity at that moment is perpendicular to the plane. The plane makes angle \(\alpha\) with the horizontal, so a line perpendicular to it makes \(90^\circ - \alpha\) with the horizontal (a perpendicular to a horizontal plane is vertical, \(90^\circ\); tilting the plane by \(\alpha\) tilts the perpendicular by \(\alpha\) away from the vertical). Since the particle is moving down and forward as it hits a rising plane, the velocity points \(90^\circ - \alpha\) below the horizontal. So the **velocity at impact makes angle \(90^\circ - \alpha\) with the horizontal**, and \(\tan\) of it is \(\dfrac{\lvert v_y\rvert}{v_x} = \tan(90^\circ - \alpha)\). For example, on a plane at \(30^\circ\) the velocity at impact is \(60^\circ\) below the horizontal.

A plane can also slope **downwards** from \(O\), at angle \(\alpha\) below the horizontal. Its equation in the same axes is \(y = -x\tan\alpha\), and the particle meets it when its height \(y\) equals \(-x\tan\alpha\). For example, a particle projected horizontally at \(8\,\mathrm{m\,s^{-1}}\) from \(O\) on a plane sloping down at \(45^\circ\) has \(x = 8t\) and \(y = -5t^2\) (with \(g = 10\)), and hits the plane when \(-5t^2 = -8t\), that is at \(t = 1.6\) s.

:::eg (Exam style) A plane is inclined at \(30^\circ\) to the horizontal. A particle is projected from a point \(O\) on the plane, with speed \(V\) at angle \(\theta\) above the horizontal, up the slope, in a vertical plane containing a line of greatest slope. It strikes the plane at right angles \(2\) s after projection. Find \(V\) and \(\theta\).
Axes: \(x\) horizontal, \(y\) vertically up, origin \(O\). The plane is the line \(y = x\tan 30^\circ = \dfrac{x}{\sqrt3}\). Let \(u = V\cos\theta\) and \(p = V\sin\theta\).

At \(t = 2\): \(x = 2u\) and \(y = 2p - 20\). [B1]

On the plane:
\[2p - 20 = \frac{2u}{\sqrt3}\] [M1]
At impact the velocity is at \(60^\circ\) below the horizontal, so \(v_y = -\sqrt3\,v_x\). Since \(v_y = p - 10 \times 2\) and \(v_x = u\),
\[p - 20 = -\sqrt3\,u\] [M1]
From the first equation, \(p = 10 + \dfrac{u}{\sqrt3}\). Substitute into the second:
\[10 + \frac{u}{\sqrt3} - 20 = -\sqrt3\,u \quad\Rightarrow\quad u\left(\frac{1}{\sqrt3} + \sqrt3\right) = 10 \quad\Rightarrow\quad \frac{4u}{\sqrt3} = 10\] [A1]
\[u = \frac{10\sqrt3}{4} = 4.33, \qquad p = 10 + \frac{4.33}{\sqrt3} = 12.5\]
\[V = \sqrt{u^2 + p^2} = \sqrt{175} = 13.2\,\mathrm{m\,s^{-1}}, \qquad \tan\theta = \frac{p}{u} = \frac{5}{\sqrt3}\ \Rightarrow\ \theta = 70.9^\circ\] [A1]
**Check**: at \(t = 2\), the particle is at \(x = 8.66\), \(y = 5\), and \(8.66 \tan 30^\circ = 5\). ✓ The velocity is \((4.33, -7.5)\), and \(\dfrac{7.5}{4.33} = 1.73 = \tan 60^\circ\). ✓
:::

## Modelling assumptions and their limits

Every number so far came from an idealised particle. A good answer says what that idealisation leaves out, and how the real motion differs.

:::key Assumptions, and what removing each one changes
| Assumption | What it ignores | Effect on the real flight |
|---|---|---|
| The body is a particle | its size, shape, spin | a spinning ball can swerve (the Magnus effect); a large body is not at a single height |
| No air resistance | drag force opposing the velocity | the range and greatest height are less; the path is steeper on the way down and not symmetric |
| \(g\) is constant | the weight changes slightly with height | negligible for a thrown ball; matters only for very long, very high paths |
| Flat horizontal ground | the Earth's curvature | negligible except for very long ranges |
| No wind | a sideways force or a headwind | the horizontal velocity is not constant |
:::

:::eg (Exam style) A golf ball is modelled as a particle moving under gravity alone. (a) State two further assumptions of this model. (b) Say how the real range would differ from the model's if air resistance were included, and give a reason.
**(a)** Any two of: there is no air resistance; the ball is a particle (its size and spin are ignored); \(g\) is constant; there is no wind; the ground is flat. [B1] [B1]

**(b)** The real range is smaller. [B1] Air resistance opposes the motion, so the ball loses horizontal speed throughout the flight and the vertical rise is reduced as well. [B1]
:::

:::exam What is given, and how to answer
MF19 gives the trajectory \(y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}\). It does **not** give the range, the time of flight or the greatest height; derive them from \(x\) and \(y\) in terms of \(t\). The paper says use \(g = 10\), so give 3 s.f. answers and angles to 1 d.p. (unless the answer is exact). A "show that" asks for every line, with the substitution made visible. Use "\(\sin 2\theta\)" only after you have shown where it comes from.
:::

:::board
Edexcel IAL Mechanics 2 and the UK A Level Mechanics papers also treat projectiles, using the same equations, and they take \(g = 9.8\) where 9231 takes \(g = 10\). The UK chapter [Projectiles and moments (UK boards)](#math.m.projectiles) covers the 9709-level ground for those boards.
:::

:::eg Spot the error: a ball is projected from level ground with speed \(20\,\mathrm{m\,s^{-1}}\). It must land on a target \(30\) m away on the same level. Find the possible angles of projection (4 marks).
A student wrote this answer.

Line 1: \(R = \dfrac{V^2\sin 2\theta}{g}\), so \(30 = \dfrac{400\sin 2\theta}{10}\) and \(\sin 2\theta = 0.75\)
Line 2: \(2\theta = 48.6^\circ\), so \(\theta = 24.3^\circ\)

Line 1 uses the range formula correctly. [M1] [A1] Line 2 solves for \(2\theta\) correctly as far as it goes. [M1]

**But line 2 gives only one angle.** [A0] \(\sin 2\theta = 0.75\) has a second solution \(2\theta = 180^\circ - 48.6^\circ = 131.4^\circ\), so \(\theta = 65.7^\circ\) works too. Because \(24.3^\circ + 65.7^\circ = 90^\circ\), the answer is a pair of complementary angles. The student scores 3 out of 4.

**Check**: \(\dfrac{400 \times \sin 131.4^\circ}{10} = 30.0\). ✓
:::

:::try Start easy, finish at exam standard
Q: A ball is kicked from level ground with speed \(26\,\mathrm{m\,s^{-1}}\) at \(\tan^{-1}\dfrac{5}{12}\) above the horizontal. Find the horizontal and vertical components of the launch velocity, and the time of flight.
A: \(\cos\theta = \tfrac{12}{13}\), \(\sin\theta = \tfrac{5}{13}\), so the components are \(24\) and \(10\) \(\mathrm{m\,s^{-1}}\). Time of flight \(\dfrac{2 \times 10}{10} = 2\) s.
Q: A stone is thrown with speed \(18\,\mathrm{m\,s^{-1}}\) at \(50^\circ\) above the horizontal from level ground. Find its greatest height and range.
A: \(H = \dfrac{(18\sin 50^\circ)^2}{20} = \dfrac{13.79^2}{20} = 9.51\) m. \(R = \dfrac{18^2\sin 100^\circ}{10} = 31.9\) m.
Q: A particle is projected horizontally at \(12\,\mathrm{m\,s^{-1}}\) from the top of a tower \(45\) m high. Find the time to reach the ground and how far from the foot it lands.
A: \(-45 = -5t^2\), so \(t = 3\) s. Distance \(12 \times 3 = 36\) m.
Q: For the particle in the previous question, find its speed on landing and the angle its path makes with the ground.
A: \(v_y = -30\), \(v_x = 12\). Speed \(\sqrt{144 + 900} = 32.3\,\mathrm{m\,s^{-1}}\). Angle \(\tan^{-1}\dfrac{30}{12} = 68.2^\circ\) below the horizontal.
Q: A ball is thrown up at \(15\,\mathrm{m\,s^{-1}}\) at \(40^\circ\) above the horizontal from a point \(2\) m above level ground. Find the speed with which it hits the ground.
A: Use \(v^2 = V^2 - 2gy\) with \(y = -2\): \(v^2 = 225 + 40 = 265\), so \(v = 16.3\,\mathrm{m\,s^{-1}}\). The angle does not matter.
Q: A projectile has \(V = 40\), \(\theta = 30^\circ\). How far has it travelled horizontally when it is at its greatest height?
A: Time to top \(= \dfrac{40 \times 0.5}{10} = 2\) s, \(x = 40\cos 30^\circ \times 2 = 69.3\) m (half the range).
Q: Find the angle of projection (the smaller one) that gives a range of \(40\) m with speed \(25\,\mathrm{m\,s^{-1}}\).
A: \(\sin 2\theta = \dfrac{400}{625} = 0.64\), \(2\theta = 39.8^\circ\), so \(\theta = 19.9^\circ\) (the other is \(70.1^\circ\)).
Q: A ball is projected from the origin at \(45^\circ\). It passes through \((10, 4)\). Find its speed of projection.
A: \(4 = 10 - \dfrac{10 \times 100}{2V^2 \times \frac12}\), so \(\dfrac{1000}{V^2} = 6\) and \(V^2 = 166.7\), \(V = 12.9\,\mathrm{m\,s^{-1}}\).
Q: A dart is thrown horizontally at \(8\,\mathrm{m\,s^{-1}}\) at a board \(2.4\) m away. How far below the throwing height does it hit?
A: \(t = \dfrac{2.4}{8} = 0.3\) s, drop \(= 5 \times 0.09 = 0.45\) m.
Q: A particle is launched at \(30^\circ\) above the horizontal with speed \(22\,\mathrm{m\,s^{-1}}\). Find its least speed during the flight and say where it occurs.
A: The horizontal component \(22\cos 30^\circ = 19.1\) never changes, and the vertical component is zero at the top, so the least speed is \(19.1\,\mathrm{m\,s^{-1}}\) at the greatest height.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Take \(g = 10\). A ball is projected from level ground with speed \(16\,\mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal. Find the greatest height reached and the total time of flight.
A: Vertical component \(16\sin 30^\circ = 8\). [B1]
At the top \(0 = 8^2 - 2 \times 10 \times H\) [M1], so \(H = 3.2\) m. [A1]
Time up \(= 0.8\) s, so total flight time \(= 1.6\) s. [B1]
Q: [5 marks] ★★ Take \(g = 10\). A particle is projected horizontally at \(15\,\mathrm{m\,s^{-1}}\) from the top of a vertical cliff \(80\) m above the sea. Find the time taken to reach the sea, and the speed of the particle as it enters the sea.
A: \(-80 = -5t^2\) [M1], so \(t = 4\) s. [A1]
\(v_y = -10 \times 4 = -40\) [B1], \(v_x = 15\), so \(v = \sqrt{15^2 + 40^2} = \sqrt{1825}\) [M1] \(= 42.7\,\mathrm{m\,s^{-1}}\). [A1]
Q: [4 marks] ★★ Take \(g = 10\). A ball is projected from the origin at \(45^\circ\) above the horizontal with speed \(V\). Given that it passes through the point \((12, 8)\), find \(V\).
A: \(y = x\tan\theta - \dfrac{gx^2}{2V^2\cos^2\theta}\) with \(\tan 45^\circ = 1\) and \(\cos^2 45^\circ = \tfrac12\):
\[8 = 12 - \frac{10 \times 144}{V^2}\] [M1 A1]
\(\dfrac{1440}{V^2} = 4\), so \(V^2 = 360\) [M1], \(V = 19.0\,\mathrm{m\,s^{-1}}\). [A1]
Q: [5 marks] ★★ Take \(g = 10\). A ball is projected from \(O\) on level ground with speed \(20\,\mathrm{m\,s^{-1}}\) and just clears the top of a vertical post, \(4\) m high, \(12\) m from \(O\). Find the two possible angles of projection.
A: \(4 = 12T - \dfrac{10 \times 144}{2 \times 400}\left(1 + T^2\right)\) [M1], so \(1.8T^2 - 12T + 5.8 = 0\). [A1]
\(T = \dfrac{12 \pm \sqrt{144 - 41.76}}{3.6}\) [M1] \(= 6.142\) or \(0.5246\). [A1]
Angles \(80.8^\circ\) and \(27.7^\circ\). [A1]
Q: [6 marks] ★★ Take \(g = 10\). A ball is hit from level ground and strikes a vertical wall \(24\) m away at the instant when it is moving horizontally, at a height of \(7.2\) m. Find the angle of projection and the speed of projection.
H: At the greatest height the ball is moving horizontally, so the wall is half the range away.
H: The range is \(48\) m and \(H = \dfrac{V^2\sin^2\theta}{2g}\), so \(\tan\theta = \dfrac{4H}{R}\).
A: The range is \(R = 48\) m [B1]. With \(R = \dfrac{V^2\sin 2\theta}{g}\) and \(H = \dfrac{V^2\sin^2\theta}{2g}\), dividing: \(\dfrac{H}{R} = \dfrac{\sin^2\theta}{4\sin\theta\cos\theta} = \dfrac{\tan\theta}{4}\) [M1].
\(\tan\theta = \dfrac{4 \times 7.2}{48} = 0.6\), so \(\theta = 31.0^\circ\). [A1]
\(\sin 2\theta = \dfrac{2 \times 0.6}{1 + 0.36} = 0.8824\) [M1], and \(V^2 = \dfrac{gR}{\sin 2\theta} = \dfrac{480}{0.8824} = 544\) [M1], \(V = 23.3\,\mathrm{m\,s^{-1}}\). [A1]
Q: [11 marks] (#math.p3.trig) ★★★ Take \(g = 10\). A golfer hits a ball from \(O\) on level ground with speed \(30\,\mathrm{m\,s^{-1}}\). The ball just clears the top of a tree, \(9\) m high, at a horizontal distance of \(45\) m from \(O\). (a) Show that \(\tan\theta\) satisfies \(5\tan^2\theta - 20\tan\theta + 9 = 0\). (b) Find the two possible angles of projection. (c) Find the range of the ball for each of the two angles. (d) Find the range of angles of projection for which the ball passes over the tree, and state which of the two angles in (b) gives the greater range.
H: Use the second form of the trajectory: \(\dfrac{gx^2}{2V^2} = \dfrac{10 \times 2025}{1800} = 11.25\).
H: For the range, use \(R = \dfrac{V^2\sin 2\theta}{g}\) and \(\sin 2\theta = \dfrac{2\tan\theta}{1 + \tan^2\theta}\).
H: For (d), the ball is above \(y = 9\) at \(x = 45\) for every \(\tan\theta\) between the roots.
A: (a) \(9 = 45T - 11.25(1 + T^2)\) [M1 A1], so \(11.25T^2 - 45T + 20.25 = 0\), and dividing by \(2.25\): \(5T^2 - 20T + 9 = 0\). [A1]
(b) \(T = \dfrac{20 \pm \sqrt{400 - 180}}{10} = \dfrac{20 \pm \sqrt{220}}{10}\) [M1], \(T = 3.483\) or \(0.5168\). [A1]
\(\theta = 74.0^\circ\) or \(27.3^\circ\). [A1]
(c) \(\sin 2\theta = \dfrac{2T}{1 + T^2}\): for \(T = 3.483\), \(\sin 2\theta = 0.5305\) and \(R = 90 \times 0.5305 = 47.7\) m; for \(T = 0.5168\), \(\sin 2\theta = 0.8157\) and \(R = 73.4\) m. [M1 A1 A1]
(d) At \(x = 45\) the height is \(y = 45T - 11.25\left(1 + T^2\right)\), which is at least 9 exactly when \(5T^2 - 20T + 9 \le 0\), that is between the roots, so any angle from \(27.3^\circ\) to \(74.0^\circ\) clears the tree. [B1] The lower angle gives the greater range, \(73.4\) m, because it is nearer \(45^\circ\). [B1]
Q: [8 marks] ★★★ Take \(g = 10\). A plane is inclined at \(45^\circ\) below the horizontal and passes through the point \(O\). A particle is projected horizontally from \(O\) with speed \(8\,\mathrm{m\,s^{-1}}\), in a vertical plane containing a line of greatest slope. (a) Find the time taken to hit the plane. (b) Find the distance from \(O\) to the point of impact, measured along the plane. (c) Find the speed of the particle at impact and the acute angle between its direction of motion and the plane.
H: Take axes with \(x\) horizontal, \(y\) up. The plane is the line \(y = -x\).
H: At impact \(x = 8t\) and \(y = -5t^2\); put \(y = -x\).
H: The velocity at impact points at \(\tan^{-1}\dfrac{\lvert v_y\rvert}{v_x}\) below the horizontal; the plane is at \(45^\circ\).
A: (a) \(x = 8t\), \(y = -5t^2\); on the plane \(y = -x\): \(5t^2 = 8t\) [M1], \(t = 1.6\) s. [A1]
(b) \(x = 12.8\), and along the slope the distance is \(\dfrac{12.8}{\cos 45^\circ}\) [M1] \(= 18.1\) m. [A1]
(c) \(v_y = -16\), \(v_x = 8\): speed \(\sqrt{64 + 256} = \sqrt{320}\) [M1] \(= 17.9\,\mathrm{m\,s^{-1}}\). [A1]
The velocity is \(\tan^{-1}2 = 63.4^\circ\) below the horizontal and the plane is at \(45^\circ\), so the angle between them is \(63.4^\circ - 45^\circ = 18.4^\circ\). [M1 A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A particle projected from level ground reaches greatest height \(H\) and has range \(R\). Show that \(\tan\theta = \dfrac{4H}{R}\), and hence find the angle of projection when the greatest height is equal to the range.
H: Write \(H\) and \(R\) in terms of \(V\), \(\theta\) and \(g\), and divide.
H: \(\sin 2\theta = 2\sin\theta\cos\theta\).
A: \(H = \dfrac{V^2\sin^2\theta}{2g}\) and \(R = \dfrac{V^2 \times 2\sin\theta\cos\theta}{g}\). [B1 B1]
\(\dfrac{H}{R} = \dfrac{\sin^2\theta}{4\sin\theta\cos\theta} = \dfrac{\tan\theta}{4}\) [M1 A1], so \(\tan\theta = \dfrac{4H}{R}\).
If \(H = R\): \(\tan\theta = 4\) [M1], \(\theta = 76.0^\circ\). [A1]
Q: [7 marks] ★★★ Take \(g = 10\). In tennis, a serve is hit horizontally from a point \(2.5\) m above the ground, with speed \(v\,\mathrm{m\,s^{-1}}\). The net is \(0.9\) m high and \(12\) m from the server horizontally. The ball must land no more than \(18.4\) m from the server. Treat the ball as a particle. Find the range of speeds \(v\) for which the serve clears the net and lands in.
H: To clear the net the ball must have fallen no more than \(2.5 - 0.9 = 1.6\) m when it has travelled \(12\) m horizontally.
H: To land in, the ball must reach the ground (fallen \(2.5\) m) after travelling at most \(18.4\) m horizontally.
A: Time to fall \(1.6\) m: \(1.6 = 5t^2\), \(t = \sqrt{0.32} = 0.5657\) s. [M1 A1]
The ball passes \(x = 12\) at \(t = \dfrac{12}{v}\), and must have fallen at most \(1.6\) m by then, so \(\dfrac{12}{v} \le 0.5657\) and \(v \ge 21.2\). [M1 A1]
Time to fall \(2.5\) m: \(t = \sqrt{0.5} = 0.7071\) s. [M1]
Landing in needs \(v \times 0.7071 \le 18.4\), so \(v \le 26.0\). [A1]
So \(21.2 \le v \le 26.0\,\mathrm{m\,s^{-1}}\). [A1]
:::

:::quiz
? A projectile is launched at \(V\) at angle \(\theta\) above the horizontal. Which gives the horizontal component of its velocity at any later time?
+ \(V\cos\theta\)
- \(V\sin\theta\)
- \(V\cos\theta - gt\)
- \(V\sin\theta - gt\)
> There is no horizontal force, so \(v_x = V\cos\theta\) for the whole flight. \(V\sin\theta\) is the initial vertical component, and \(V\sin\theta - gt\) is the vertical component at time \(t\).
? A ball is projected at \(20\,\mathrm{m\,s^{-1}}\) at \(30^\circ\) above the horizontal over level ground (\(g = 10\)). Which angle gives the same range?
+ \(60^\circ\)
- \(45^\circ\)
- \(150^\circ\)
- \(15^\circ\)
> \(R\) is proportional to \(\sin 2\theta\), and \(\sin 60^\circ = \sin 120^\circ\), so the angle \(90^\circ - 30^\circ = 60^\circ\) gives the same range. \(45^\circ\) gives the maximum range, which is longer.
? A stone is thrown from the top of a cliff and its time to hit the sea satisfies \(t^2 - 2t - 8 = 0\). What do you do with the root \(t = -2\)?
- Use it: it is the time when the stone passes the cliff top on its way up
+ Reject it: the stone was not in flight before \(t = 0\)
- Use it as the time of flight, since it is the root with the larger magnitude
- Take its modulus and add it to \(t = 4\)
> A negative time is before the launch, so it has no physical meaning here. For a launch from a height onto lower ground, one root of the landing equation is always negative; it is a number that fits the algebra, not the flight.
? Which statement about the speed of a projectile at height \(y\) above the launch point is correct?
+ It depends on \(V\) and \(y\) only: \(v^2 = V^2 - 2gy\)
- It also depends on the angle of projection \(\theta\)
- It is the same on the way up as on the way down, but only at the top
- It is always \(V\) at the same height as the launch, but not otherwise
> Energy is conserved, so the speed at a given height depends only on the launch speed and the height, whatever the angle. The speed is the same at a given height on the way up and on the way down, and it equals \(V\) whenever the height is zero.
? The equation \(a\tan^2\theta + b\tan\theta + c = 0\) for the path through a target has two distinct positive roots. What does this mean?
+ Two different angles of projection both hit the target
- The target is out of reach
- The ball must be launched at \(45^\circ\)
- Only the larger angle is physically possible
> Each positive root of \(\tan\theta\) is a valid angle of projection. A negative discriminant means that the target is out of reach, and the two roots coincide only for the single angle that is just able to reach the target.
? In the model of a projectile, which of these is NOT one of the assumptions?
- Air resistance is negligible
- The acceleration due to gravity is constant
- The body can be treated as a particle
+ The horizontal speed decreases at a steady rate
> The model has no horizontal force, so the horizontal speed is constant. The other three are the standard assumptions, and the first one is the one that most affects a real long flight.
:::

:::checklist What you can now do
- [ ] I can state the assumptions of the projectile model and say how air resistance, spin and wind change the real flight.
- [ ] I can resolve the launch velocity and write the horizontal and vertical equations of motion.
- [ ] I can find the time of flight, greatest height and range on level ground, and derive the range \(\dfrac{V^2\sin 2\theta}{g}\).
- [ ] I can find the speed and direction of a projectile at a given time or position.
- [ ] I can solve problems where a projectile is launched from, or lands at, a different level, choosing the correct root.
- [ ] I can derive the Cartesian equation of the trajectory and use it, including the form with \(1 + \tan^2\theta\).
- [ ] I can find an unknown speed or angle, and both angles that pass through a given point.
- [ ] I can solve a problem in which the projectile strikes an inclined plane, including at right angles.
:::

:::recap
- A projectile has horizontal acceleration \(0\) and vertical acceleration \(-g\) (\(g = 10\)); the two motions are independent.
- \(x = V\cos\theta\,t\), \(y = V\sin\theta\,t - \tfrac12gt^2\), \(v_x = V\cos\theta\), \(v_y = V\sin\theta - gt\).
- Level ground: \(H = \dfrac{V^2\sin^2\theta}{2g}\), \(T = \dfrac{2V\sin\theta}{g}\), \(R = \dfrac{V^2\sin 2\theta}{g}\) (not on MF19). Maximum range at \(45^\circ\); \(\theta\) and \(90^\circ - \theta\) give equal ranges.
- Speed at height \(y\): \(v^2 = V^2 - 2gy\). Direction: \(\tan\varphi = \dfrac{\lvert v_y\rvert}{v_x}\), below the horizontal if \(v_y < 0\).
- Different levels: put \(y\) at the landing point, solve the quadratic in \(t\), and choose the root that fits (the positive one, or the later one for a higher level).
- Trajectory (on MF19): \(y = x\tan\theta - \dfrac{gx^2}{2V^2}\left(1 + \tan^2\theta\right)\), a quadratic in \(\tan\theta\): two roots, two angles.
- For a plane, write its equation in the same axes; striking at right angles means the velocity is perpendicular to the plane.
- Limits: no air resistance, particle, constant \(g\), no wind: real ranges are shorter.
:::

:::links
- watch: [Projectiles playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NhfzR6dcRPAo139k4Q_YmP-) · ExamSolutions (YouTube) · worked projectile questions, from basic to exam level
- explore: [Projectile motion](https://phet.colorado.edu/en/simulations/projectile-motion) · PhET · change the speed, angle and air resistance and watch the path and range
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · graded projectile questions with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Further Mechanics questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Centres of mass](#math.fm.com) starts the second half of Further Mechanics: where the weight of a body acts, and how to find it for particles, laminas and solids.
