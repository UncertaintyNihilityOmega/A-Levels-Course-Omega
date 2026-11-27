@chapter math.fm.rigid
@title Equilibrium of a rigid body
@level fm
@paper CAIE 9231 Paper 3 · Edexcel IAL Mechanics 2 · UK A Level Mechanics
@time 6–7 hours
@summary A rigid body is in equilibrium when the forces on it have no resultant and no turning effect. You will solve problems on beams, rods hinged to walls, ladders on rough or smooth surfaces and rods resting on pegs, by resolving twice and taking moments once at a well-chosen point. You will use the three-force rule, and decide whether a block or solid on a plane, or pushed by a force, slides or topples first.

:::why
Ladders, beams, doors and cranes are all rigid bodies held still by forces that are not at one point. Knowing whether a ladder will slip, whether a wall will hold a bracket, or whether a cabinet will tip before it slides is what separates a safe structure from an accident. The method is short: two resolving equations, one moments equation, and a good choice of the point to take moments about.
:::

**Before you start**, you need moments and centres of mass from [Centres of mass](#math.fm.com), resolving forces and the friction law \(F \le \mu R\) from [Forces and equilibrium](#math.m.forces), and \(\tan\theta\) from [Trigonometry](#math.p1.trig). Take **\(g = 10\,\mathrm{m\,s^{-2}}\)**.

:::try Warm-up
Q: A block of weight \(50\) N rests on rough horizontal ground, \(\mu = 0.4\). What is the greatest friction the ground can provide? (from [Forces and equilibrium](#math.m.forces))
A: \(R = 50\) N, so \(F_{\max} = \mu R = 0.4 \times 50 = 20\) N.
Q: A force of \(8\) N acts perpendicular to a rod at a point \(1.5\) m from a pivot. Find its moment about the pivot. (from [Centres of mass](#math.fm.com))
A: \(8 \times 1.5 = 12\) N m.
Q: A uniform solid cone has height \(12\) cm. How far is its centre of mass from its base? (from [Centres of mass](#math.fm.com))
A: \(\tfrac14 \times 12 = 3\) cm from the base.
:::

## The conditions for equilibrium

A particle is in equilibrium when the forces on it have no resultant. A body of some size needs one more condition, because forces that cancel in total can still turn it: two equal and opposite forces along different lines make a **couple**, and the body spins.

:::def Rigid body
A body whose shape does not change under the forces on it: its particles stay the same distance apart. All the bodies in this chapter (rods, ladders, blocks, laminas) are modelled as rigid.
:::

:::key Equilibrium of a rigid body under coplanar forces (all in one plane)
A rigid body acted on by coplanar forces (forces all in one plane) is in equilibrium if and only if
1. the **vector sum of the forces is zero**: resolve in two perpendicular directions and the sum in each is \(0\);
2. the **sum of the moments of the forces about any point is zero**.
The converse is true too: if both conditions hold, the body stays at rest (or moves with constant velocity). There are three independent equations, so a problem can have **three unknowns**. The moment condition holds about *every* point, so you may choose the most convenient one.
:::

Each type of contact has its own force. Learn what each can do, because a missing or extra force is the commonest source of error.

:::key What each contact can provide
| Contact | Force on the body |
|---|---|
| Weight | acts at the centre of mass \(G\), vertically downwards |
| Smooth surface, smooth peg, smooth edge | one reaction, **perpendicular** to the surface (or perpendicular to the rod at a peg) |
| Rough surface | normal reaction \(R\) perpendicular to the surface, **and** friction \(F\) along it; \(F \le \mu R\), and \(F = \mu R\) in **limiting equilibrium** (about to slip) |
| Smooth hinge | one force of unknown size and direction at the hinge: use two components (horizontal \(X\), vertical \(Y\)) |
| Light string | tension along the string, pulling the body towards the string |
:::

:::def Limiting equilibrium
Equilibrium in which friction has reached its greatest value, \(F = \mu R\), so the body is on the point of slipping. Friction acts in the direction opposing the slipping that would occur.
:::

:::steps
1. Draw a clear diagram and mark **every** force, with its line of action: weights at the centre of mass, reactions as the table says, friction opposing the slipping.
2. Choose the point for moments where as many unknown forces as possible pass through it. Their moments are then zero.
3. Take moments, resolve in two directions, and solve.
4. Check: take moments about a second point and see that the sum is zero.
:::

## Beams and rods on supports

When a beam rests on two supports, each support gives a vertical reaction. Taking moments about one support removes its reaction, leaving the other.

:::eg A uniform beam \(AB\) of length \(8\) m and weight \(200\) N rests on supports at \(P\) and \(Q\), where \(AP = 2\) m and \(AQ = 6\) m. A person of weight \(600\) N walks along the beam from \(A\). How far from \(A\) is the person when the beam is about to tilt, and what are the reactions then?
When the beam is about to tilt about \(Q\), the support \(P\) is no longer pushing: \(R_P = 0\). The person is beyond \(Q\), at distance \(x\) from \(A\). Take moments about \(Q\) (the unknown \(R_Q\) has no moment):
- the person's weight turns the beam one way: \(600(x - 6)\);
- the beam's weight acts at \(4\) m from \(A\), which is \(2\) m from \(Q\), and turns it the other way: \(200 \times 2\).
\[\begin{aligned}
600(x - 6) &= 200 \times 2 \\
x - 6 &= \tfrac23 \\
x &= 6.67\ \text{m}
\end{aligned}\]
The person can go \(6.67\) m from \(A\) (\(0.67\) m beyond \(Q\)). Vertically, \(R_Q = 200 + 600 = 800\) N and \(R_P = 0\).
:::

## A rod hinged to a wall

A rod fixed at a hinge can turn about it, so the hinge reaction passes through the hinge and has no moment about it. Taking moments about the hinge therefore finds the tension in a string without involving the hinge force at all.

:::html
<figure class="fig small"><svg viewBox="20 5 240 215" role="img" aria-label="A uniform rod AB hinged at A to a vertical wall and held horizontal by a light string from B to a point C on the wall above A. The angle between the string and the rod at B is 40 degrees. The rod's weight of 50 newtons acts at its midpoint and a load of 30 newtons hangs at B. The tension T acts along BC. The hinge reaction at A has a horizontal component X away from the wall and a vertical component Y upwards.">
  <path class="ln thick" d="M50 12V190"/>
  <path class="ln thin" d="M206 150L50 19.1"/>
  <rect class="fm s-acc sw2" x="50" y="146" width="156" height="8"/>
  <path class="ln" d="M206 150L144.7 98.6" marker-end="url(#ah)"/>
  <path class="c1" d="M50 150H94" marker-end="url(#ah-math)"/>
  <path class="c1" d="M50 150V104" marker-end="url(#ah-math)"/>
  <path class="ln" d="M128 154V200" marker-end="url(#ah)"/>
  <path class="ln" d="M206 154V200" marker-end="url(#ah)"/>
  <path class="ln-m thin" d="M178 150A28 28 0 0 1 184.6 132"/>
  <circle class="fi" cx="50" cy="150" r="3.5"/>
  <text class="tl halo" x="132" y="112">T</text>
  <text class="tl halo" x="84" y="141">X</text>
  <text class="tl halo" x="44" y="112" text-anchor="end">Y</text>
  <text class="tl" x="140" y="196">50 N</text>
  <text class="tl" x="216" y="196">30 N</text>
  <text class="tl" x="146" y="142">40°</text>
  <text class="tl" x="40" y="168" text-anchor="end">A</text>
  <text class="tl" x="214" y="146">B</text>
  <text class="tl" x="40" y="23" text-anchor="end">C</text>
</svg><figcaption>The rod AB, hinged at A, held horizontal by the string BC. The tension T acts along BC. The hinge reaction at A is shown by its components X and Y, and the 50 N weight acts at the midpoint of the rod.</figcaption></figure>
:::

:::eg (Exam style) A uniform rod \(AB\) of length \(2.4\) m and weight \(50\) N is hinged at \(A\) to a vertical wall. It is held horizontal by a light string \(BC\), where \(C\) is a point on the wall above \(A\), and the angle \(ABC = 40^\circ\). A load of weight \(30\) N is attached to the rod at \(B\). Find (a) the tension in the string, (b) the magnitude and direction of the force exerted on the rod by the hinge.
**(a)** Take moments about \(A\), so the hinge force has no moment. The component of \(T\) perpendicular to the rod is \(T\sin 40^\circ\), acting at \(2.4\) m from \(A\):
\[T\sin 40^\circ \times 2.4 = 50 \times 1.2 + 30 \times 2.4\] [M1 A1]
\[T = \frac{132}{2.4\sin 40^\circ} = 85.6\ \text{N}\] [A1]
**(b)** Let the hinge force have components \(X\) (horizontal, away from the wall) and \(Y\) (upwards).

Horizontally: \(X = T\cos 40^\circ = 65.5\) N. [M1 A1]

Vertically: \(Y + T\sin 40^\circ = 50 + 30\), and \(T\sin 40^\circ = 55\), so \(Y = 25\) N. [A1]

Magnitude \(\sqrt{65.5^2 + 25^2} = 70.2\) N, at \(\tan^{-1}\dfrac{25}{65.5} = 20.9^\circ\) above the horizontal, pointing away from the wall. [M1 A1]
**Check**: moments about \(B\): \(Y \times 2.4 = 50 \times 1.2\), that is \(25 \times 2.4 = 60 = 60\). ✓ (the weight of the load has no moment about \(B\), and neither has \(T\)).
:::

## Ladders

A ladder leans against a wall with its foot on the ground. The wall and the ground can each be smooth or rough. If the wall is **smooth**, it can only push perpendicular to itself: a horizontal force \(R_2\). The ground gives a vertical reaction \(R_1\) and, if rough, a friction \(F_1\) along it. The friction at the foot always acts **towards the wall**, because the wall's push tends to drive the foot away from it.

:::html
<figure class="fig small"><svg viewBox="30 5 215 245" role="img" aria-label="A uniform ladder AB leaning against a vertical wall on its right, at angle theta to the rough horizontal ground. The weight W acts downwards at the midpoint G. At the foot A there is a normal reaction R1 upwards and a friction force F1 horizontally towards the wall. At the top B the wall gives a horizontal reaction R2 away from the wall and, if the wall is rough, a friction force F2 upwards. If the wall is smooth, F2 is zero.">
  <path class="ln-m" d="M30 215H230"/>
  <path class="ln thick" d="M195 215V10"/>
  <path class="ln thick" d="M86 215L195 59.4"/>
  <path class="c1" d="M86 215V165" marker-end="url(#ah-math)"/>
  <path class="c1" d="M86 215H136" marker-end="url(#ah-math)"/>
  <path class="ln" d="M195 59.4H145" marker-end="url(#ah)"/>
  <path class="ln" d="M195 59.4V22" marker-end="url(#ah)"/>
  <path class="ln" d="M140.5 137.2V190" marker-end="url(#ah)"/>
  <path class="ln-m thin" d="M126 215A40 40 0 0 0 108.9 182.2"/>
  <circle class="fi" cx="140.5" cy="137.2" r="3.5"/>
  <text class="tl halo" x="78" y="172" text-anchor="end">R₁</text>
  <text class="tl" x="116" y="231">F₁</text>
  <text class="tl halo" x="168" y="52">R₂</text>
  <text class="tl" x="202" y="40">F₂</text>
  <text class="tl halo" x="152" y="180">W</text>
  <text class="tl halo" x="132" y="133" text-anchor="end">G</text>
  <text class="tl" x="114" y="203">θ</text>
  <text class="tl" x="74" y="231" text-anchor="end">A</text>
  <text class="tl" x="202" y="64">B</text>
</svg><figcaption>A uniform ladder AB against a wall. The ground gives R₁ and friction F₁ (towards the wall); the wall gives R₂ (horizontal, away from the wall) and, if rough, friction F₂ (upwards). W acts at the midpoint G. For a smooth wall F₂ = 0.</figcaption></figure>
:::

For a ladder of length \(2a\) at angle \(\theta\) to the horizontal, resolving gives \(R_1 = W\) and \(F_1 = R_2\) (smooth wall), and moments about the foot \(A\) give the wall reaction. Here is the key: the **perpendicular distances** are the horizontal distance \(a\cos\theta\) from \(A\) to the weight, and the height \(2a\sin\theta\) of \(B\) above \(A\).

:::eg A uniform ladder of weight \(200\) N and length \(5\) m rests with its top against a smooth vertical wall and its foot on rough horizontal ground, where \(\mu = 0.4\). Find the least angle the ladder can make with the ground without slipping.
Let the angle with the ground be \(\theta\). Resolve vertically: \(R_1 = 200\). Horizontally: \(F_1 = R_2\).

Moments about \(A\): the weight acts \(2.5\cos\theta\) from \(A\) horizontally, the wall reaction at height \(5\sin\theta\):
\[R_2 \times 5\sin\theta = 200 \times 2.5\cos\theta\]
\[R_2 = 100\cot\theta\]
So \(F_1 = 100\cot\theta\). Friction is limited: \(F_1 \le \mu R_1 = 0.4 \times 200 = 80\).
\[100\cot\theta \le 80 \quad\Rightarrow\quad \tan\theta \ge 1.25 \quad\Rightarrow\quad \theta \ge 51.3^\circ\]
The ladder will not slip if it is at least \(51.3^\circ\) to the ground. A flatter ladder needs more friction than the ground can give.
:::

:::eg (Exam style) A uniform ladder \(AB\) of length \(6\) m and weight \(150\) N rests with \(A\) on rough horizontal ground (\(\mu = 0.5\)) and \(B\) against a smooth vertical wall. The ladder makes an angle of \(60^\circ\) with the ground. A person of weight \(750\) N climbs the ladder. How far along the ladder from \(A\) can the person climb before the ladder slips?
Let the person be at distance \(d\) from \(A\) along the ladder, and let \(R_2\) be the wall reaction (horizontal) with \(R_1\) and \(F_1\) at \(A\).

Vertically: \(R_1 = 150 + 750 = 900\). [B1]

The ladder is about to slip when friction is limiting: \(F_1 = 0.5 \times 900 = 450\). Horizontally, \(R_2 = F_1 = 450\). [B1]

Moments about \(A\):
\[R_2 \times 6\sin 60^\circ = 150 \times 3\cos 60^\circ + 750 \times d\cos 60^\circ\] [M1 A1]
\[450 \times 5.196 = 225 + 375d\]
\[2338 = 225 + 375d\] [M1]
\[d = 5.64\ \text{m}\] [A1]
The person can climb \(5.64\) m along the ladder (the ladder is \(6\) m long). A person who goes beyond that makes the ladder slip.
:::

:::warn Perpendicular distances on a ladder
The horizontal distance from the foot of the ladder to a point at distance \(d\) along it is \(d\cos\theta\), and the vertical height is \(d\sin\theta\). The wall reaction is horizontal, so its perpendicular distance from \(A\) is the **height** \(6\sin\theta\), not the length of the ladder. The weight and the person are vertical, so their distances are **horizontal**: \(d\cos\theta\). Writing the length of the ladder for a perpendicular distance is the most common error.
:::

:::eg (Exam style) A uniform ladder of length \(2a\) and weight \(W\) rests at angle \(\theta\) to the horizontal with its foot on rough ground (coefficient of friction \(\mu_1\)) and its top against a rough vertical wall (coefficient \(\mu_2\)). The ladder is in limiting equilibrium at both contacts. Show that \(\tan\theta = \dfrac{1 - \mu_1\mu_2}{2\mu_1}\), and find \(\theta\) when \(\mu_1 = 0.5\) and \(\mu_2 = 0.25\).
Let the ground give \(R_1\) (up) and \(F_1\) (towards the wall) and the wall give \(R_2\) (away from the wall) and \(F_2\) (up).

Limiting friction at both ends: \(F_1 = \mu_1R_1\) and \(F_2 = \mu_2R_2\). [B1]

Horizontally: \(R_2 = F_1 = \mu_1R_1\). Vertically: \(R_1 + F_2 = W\). [M1]
\[R_1 + \mu_2\mu_1R_1 = W \quad\Rightarrow\quad R_1 = \frac{W}{1 + \mu_1\mu_2}\] [A1]
so \(R_2 = \dfrac{\mu_1W}{1 + \mu_1\mu_2}\) and \(F_2 = \dfrac{\mu_1\mu_2W}{1 + \mu_1\mu_2}\).

Moments about \(A\): \(R_2\) at height \(2a\sin\theta\), \(F_2\) at horizontal distance \(2a\cos\theta\), and \(W\) at horizontal distance \(a\cos\theta\):
\[R_2 \times 2a\sin\theta + F_2 \times 2a\cos\theta = W \times a\cos\theta\] [M1 A1]
Divide by \(a\cos\theta\) and substitute:
\[2R_2\tan\theta + 2F_2 = W \quad\Rightarrow\quad \tan\theta = \frac{W - 2F_2}{2R_2}\]
\[\tan\theta = \frac{1 + \mu_1\mu_2 - 2\mu_1\mu_2}{2\mu_1} = \frac{1 - \mu_1\mu_2}{2\mu_1}\] [M1 A1]
With \(\mu_1 = 0.5\), \(\mu_2 = 0.25\): \(\tan\theta = \dfrac{1 - 0.125}{1} = 0.875\), so \(\theta = 41.2^\circ\). [A1]
**Check**: \(\mu_2 = 0\) gives \(\tan\theta = \dfrac{1}{2\mu_1}\), which is the smooth-wall result \(\tan\theta \ge \dfrac{1}{2\mu}\) of the earlier example (\(\dfrac{1}{0.8} = 1.25\)). ✓
:::

## Rods resting on pegs and edges

When a rod rests on a smooth peg or edge, or against a smooth surface, the reaction is **perpendicular to the rod** at the point of contact (the rod's side is the surface it touches). This is the same rule as for any smooth contact, but a student who draws the reaction vertically instead of perpendicular to the rod loses everything after it.

:::html
<figure class="fig small"><svg viewBox="20 10 240 240" role="img" aria-label="A uniform rod AB rises to the right at 60 degrees from rough horizontal ground, with its lower end A on the ground. A smooth peg C touches the underside of the rod. At A the ground gives a normal reaction R upwards and a friction force F horizontally to the right. At C the peg gives a reaction S perpendicular to the rod, pointing up and to the left. The weight 100 N acts downwards at the midpoint G.">
  <path class="ln thick" d="M30 225H250"/>
  <path class="ln thick" d="M60 225L168 37.9"/>
  <circle class="f1 s-acc sw2" cx="105" cy="155" r="4"/>
  <path class="c1" d="M60 225V185" marker-end="url(#ah-math)"/>
  <path class="c1" d="M60 225H94" marker-end="url(#ah-math)"/>
  <path class="c1" d="M101.6 153L66.9 133" marker-end="url(#ah-math)"/>
  <path class="ln" d="M114 131.5V185.5" marker-end="url(#ah)"/>
  <circle class="fi" cx="114" cy="131.5" r="3.5"/>
  <path class="ln-m thin" d="M88 225A28 28 0 0 0 74 200.8"/>
  <text class="tl halo" x="54" y="181" text-anchor="end">R</text>
  <text class="tl" x="94" y="241">F</text>
  <text class="tl halo" x="62.9" y="133" text-anchor="end">S</text>
  <text class="tl" x="128" y="181.5">100 N</text>
  <text class="tl" x="96" y="215">60°</text>
  <text class="tl" x="54" y="241" text-anchor="end">A</text>
  <text class="tl" x="176" y="41.9">B</text>
  <text class="tl" x="86" y="166" text-anchor="end">C</text>
  <text class="tl" x="124" y="125.5">G</text>
</svg><figcaption>The rod \(AB\) rests with \(A\) on rough ground and touches the smooth peg \(C\) from below. The peg's reaction \(S\) is perpendicular to the rod, up and to the left. The ground gives \(R\) upwards and friction \(F\) to the right. The weight acts at the midpoint \(G\). Not to scale.</figcaption></figure>
:::

:::eg A uniform rod \(AB\) of length \(6\) m and weight \(100\) N rests with \(A\) on rough horizontal ground and touches a smooth horizontal peg \(C\), \(2\) m above the ground. The rod makes \(60^\circ\) with the horizontal. Find the least coefficient of friction between the rod and the ground for the rod to stay at rest.
The peg is smooth, so the reaction \(S\) at \(C\) is perpendicular to the rod. The distance \(AC = \dfrac{2}{\sin 60^\circ} = 2.309\) m.

Moments about \(A\) (the unknown ground forces have no moment):
\[S \times 2.309 = 100 \times 3\cos 60^\circ\]
\[S = 64.95\ \text{N}\]
The rod slopes up to the right, so \(S\) pushes **up and to the left**, perpendicular to the rod (see the figure). It is at \(60^\circ\) to the vertical, so it has horizontal component \(S\sin 60^\circ\) (to the left) and vertical component \(S\cos 60^\circ\) (upwards). The leftward push would drive the foot \(A\) to the left, so friction \(F\) at \(A\) acts **to the right**, and the ground reaction \(R\) acts upwards.

Horizontally, \(F\) balances the leftward part of \(S\): \(F = S\sin 60^\circ = 56.25\) N. Vertically: \(R + S\cos 60^\circ = 100\), so \(R = 100 - 32.48 = 67.52\) N.
\[\mu \ge \frac{F}{R} = \frac{56.25}{67.52} = 0.833\]
The least coefficient of friction is \(0.833\).
:::

## Three forces: the lines of action meet

A rod or lamina in equilibrium under **three non-parallel** forces has a special property that often saves a whole calculation.

:::key Three-force rule
If a rigid body is in equilibrium under three coplanar forces that are not parallel, their **lines of action pass through one point**. Conversely, if two of the forces meet at a point, the third passes through it too. Reason: take moments about the point where two lines meet; those two forces have no moment, so the third must have none, and its line of action must pass through the point.
:::

:::eg (Exam style) A uniform rod \(AB\) of length \(2\) m and weight \(60\) N is hinged to a vertical wall at \(A\). It rests at \(30^\circ\) above the horizontal, held by a horizontal light string from \(B\) to the wall. Find the tension in the string and the magnitude and direction of the hinge reaction.
The rod has three forces: the weight \(60\) N (vertical at the midpoint, \(1\) m from \(A\) along the rod), the tension \(T\) (horizontal at \(B\)), and the hinge reaction. [B1]

Moments about \(A\): the weight is at horizontal distance \(1\cos 30^\circ = 0.866\) m; \(T\) at vertical distance \(2\sin 30^\circ = 1\) m.
\[T \times 1 = 60 \times 0.866\] [M1 A1]
\[T = 52.0\ \text{N}\] [A1]
Resolve: horizontally the hinge force \(X = T = 52.0\) N (away from the wall), vertically \(Y = 60\) N (up). [M1]
\[\text{magnitude} = \sqrt{52.0^2 + 60^2} = 79.4\ \text{N}, \qquad \tan\varphi = \frac{60}{52.0} \Rightarrow \varphi = 49.1^\circ\] [A1]
**Three-force check**: the weight (vertical line through the midpoint, \(0.866\) m from the wall) and the tension (horizontal line through \(B\), at height \(1\) m) meet at the point \((0.866, 1)\). The hinge reaction must pass through that point and through \(A = (0, 0)\), so it makes \(\tan^{-1}\dfrac{1}{0.866} = 49.1^\circ\) with the horizontal. ✓
:::

The check shows the power of the rule: the direction of the hinge force came for free from a picture, with no resolving.

## Toppling and sliding

A solid resting on a plane can fail in two ways under a push or a tilt: it can **slide** (the friction runs out) or **topple** (tip over an edge).

- It **slides** when the friction needed exceeds the greatest friction available: \(F > \mu R\).
- It **topples** when the line of action of the weight falls outside the base, or, for a pushed body, when the push turns it about an edge of the base before it slides. At the point of toppling the whole reaction acts at that edge (the **pivot**); the base is just touching the plane only along that edge.

Which happens first depends on the shape and on \(\mu\). **Compare the two conditions** and say which one is reached first.

### A block pushed by a horizontal force

A uniform block of weight \(W\) has a base of width \(2a\) and its centre of mass is at height \(h\). A horizontal force \(P\) acts on it at height \(k\) above the base, pushing towards the right. As \(P\) increases:

- it **slides** when \(P = \mu W\) (friction \(F = P\) reaches \(\mu R\), with \(R = W\));
- it **topples** about the lower-right edge when the moment of \(P\) about that edge equals the moment of the weight: \(P \times k = W \times a\), so \(P = \dfrac{Wa}{k}\).

The smaller of these values of \(P\) is the one at which the block moves.

:::eg A uniform rectangular block of weight \(W\), with base width \(0.6\) m and height \(1.0\) m, stands on rough horizontal ground. A horizontal force \(P\) is applied to a vertical face at height \(0.8\) m above the base. Find the value of \(P\) at which the block topples, and decide whether the block slides or topples first as \(P\) increases when (a) \(\mu = 0.5\), (b) \(\mu = 0.3\).
The half-width of the base is \(a = 0.3\) m, and the weight acts through the centre, \(0.3\) m from each side. At the instant of toppling the reaction \(R\) and friction \(F\) act at the edge; take moments about that edge:
\[P \times 0.8 = W \times 0.3 \quad\Rightarrow\quad P = 0.375W\]
Sliding would need \(P = \mu W\) (since \(R = W\)).

(a) \(\mu = 0.5\): sliding needs \(P = 0.5W\), which is larger than \(0.375W\). The block **topples first**. Check that it does not slide at that instant: the friction needed is \(F = P = 0.375W\), and the greatest friction is \(0.5W\), so friction holds. ✓

(b) \(\mu = 0.3\): sliding needs \(P = 0.3W\), smaller than \(0.375W\). The block **slides first**, at \(P = 0.3W\), long before the moment of \(P\) can tip it.
:::

### A solid on an inclined plane

Place a solid on a rough plane inclined at angle \(\alpha\) and increase \(\alpha\) slowly. The solid slides when \(\tan\alpha > \mu\). It topples when the vertical line through the centre of mass \(G\) passes outside the base, that is when \(\tan\alpha\) exceeds the ratio of the half-width of the base to the height of \(G\) above the base.

:::key Toppling and sliding on a slope of angle \(\alpha\)
- **Slides** when \(\tan\alpha > \mu\).
- **Topples** when \(\tan\alpha > \dfrac{a}{h}\), where \(a\) is the distance, measured along the slope, from the lower edge of the base to the point of the base directly beneath \(G\) (for a symmetric base, its half-width or radius), and \(h\) is the height of \(G\) above the base.
- As \(\alpha\) increases from \(0\), the **smaller** critical angle is reached first and decides what happens. Always compare \(\tan^{-1}\mu\) with \(\tan^{-1}\dfrac{a}{h}\).
:::

:::html
<figure class="fig small"><svg viewBox="20 15 250 290" role="img" aria-label="A solid on a plane that rises to the right at angle alpha to the horizontal. O is the lower left edge of its base. G is the centre of mass, at distance a up the slope from O along the base and at height h above the base, measured perpendicular to the plane. At the point of toppling the vertical line through G, along which the weight W acts, passes through O.">
  <path class="ln thick" d="M60 290.4L260 175"/>
  <polygon class="fm s-acc sw2" points="130,250 223.5,196 130,34 36.5,88"/>
  <path class="ln-m thin dash" d="M130 142V250"/>
  <path class="ln-m thin dash" d="M176.8 223L130 142"/>
  <path class="ln-m thin dash" d="M130 250H90"/>
  <path class="ln-m thin" d="M134 257L180.8 230"/>
  <path class="ln" d="M130 142V190" marker-end="url(#ah)"/>
  <path class="ln-m thin" d="M100 250A30 30 0 0 0 104 265"/>
  <circle class="fi" cx="130" cy="142" r="3.5"/>
  <circle class="fi" cx="130" cy="250" r="3"/>
  <text class="tl" x="138" y="136">G</text>
  <text class="tl halo" x="124" y="172" text-anchor="end">W</text>
  <text class="tl" x="162" y="184">h</text>
  <text class="tl" x="162" y="252">a</text>
  <text class="tl" x="136" y="270">O</text>
  <text class="tl" x="84" y="266">α</text>
</svg><figcaption>A solid on a plane at angle \(\alpha\). \(O\) is the lower edge of the base, \(G\) is \(a\) from \(O\) along the slope and \(h\) above the plane. At the point of toppling the weight, which acts vertically through \(G\), passes through \(O\). Not to scale.</figcaption></figure>
:::

:::proof Why the critical angle for toppling is \(\tan^{-1}(a/h)\) (not examined)
At the point of toppling the plane exerts its whole reaction (normal \(R\) and friction \(F\)) at the lower edge of the base, so these forces have no moment about that edge. The only other force is the weight \(W\) at \(G\), so its moment about the edge must also be zero: its line of action passes through the edge.

The plane rises to the right in the figure, so \(O\) is the lower edge of the base, on the left. The centre of mass \(G\) is at distance \(a\) from \(O\) measured up the slope and at height \(h\) above the plane (\(h\) is measured perpendicular to the plane). Split the weight \(W\) into a component \(W\cos\alpha\) into the plane and a component \(W\sin\alpha\) down the slope.

The component into the plane acts at distance \(a\) along the slope from \(O\), so it turns the solid back against the plane, with moment \(W\cos\alpha \times a\). The component down the slope acts at height \(h\) above the plane, so it turns the solid over the edge \(O\), with moment \(W\sin\alpha \times h\). The solid is about to topple when the two are equal:
\[W\cos\alpha \times a = W\sin\alpha \times h \quad\Rightarrow\quad \tan\alpha = \frac ah\]
For a larger angle the turning moment over the edge wins, so it topples.
:::

:::eg A uniform solid cone has base radius \(6\) cm and height \(20\) cm. It stands with its base on a rough plane, with coefficient of friction \(\mu\), and the plane is slowly tilted. Find the angle at which it topples, and say whether it slides or topples first when (a) \(\mu = 0.8\), (b) \(\mu = 1.5\).
The centre of mass is on the axis, \(\tfrac14 \times 20 = 5\) cm above the base. The half-width of the base is its radius, \(6\) cm.
\[\tan\alpha_{\text{topple}} = \frac{6}{5} = 1.2 \quad\Rightarrow\quad \alpha = 50.2^\circ\]
(a) Sliding occurs when \(\tan\alpha = \mu = 0.8\), that is \(\alpha = 38.7^\circ\). That is smaller than \(50.2^\circ\), so the cone **slides first**; it never topples, because it has slid away before the tilt reaches \(50.2^\circ\).

(b) \(\mu = 1.5\) gives \(\alpha = 56.3^\circ\) for sliding, which is more than \(50.2^\circ\), so the cone **topples first**, at \(50.2^\circ\).
:::

:::eg (Exam style) A uniform solid is formed from a cone of base radius \(8\) cm and height \(16\) cm by removing a hemisphere of radius \(4\) cm from its base, as in [Centres of mass](#math.fm.com) (the centre of the hemisphere is the centre of the base). The centre of mass is on the axis, \(\tfrac{61}{14}\) cm from the base. The solid stands with its base on a rough plane inclined at angle \(\alpha\) to the horizontal. (a) Find the greatest angle \(\alpha\) at which the solid does not topple. (b) The coefficient of friction between the solid and the plane is \(0.9\). Show that the solid slides before it topples as \(\alpha\) increases. (c) Find the least value of \(\mu\) for which toppling occurs before sliding.
**(a)** The solid is about to topple when the vertical through \(G\) passes through the lower edge of the base. The base has radius \(8\) cm and \(G\) is \(\tfrac{61}{14}\) cm above it:
\[\tan\alpha = \frac{8}{61/14} = \frac{112}{61}\] [M1 A1]
\[\alpha = 61.4^\circ\] [A1]
**(b)** Sliding occurs when \(\tan\alpha = 0.9\), that is \(\alpha = 42.0^\circ\). [M1] Since \(42.0^\circ < 61.4^\circ\), the solid slides before the plane is steep enough to topple it. [A1]

**(c)** Toppling comes first if the sliding angle is larger: \(\tan\alpha_s = \mu \ge \dfrac{112}{61}\), so \(\mu \ge 1.84\). [B1]
**Check** with part (b): \(\mu = 0.9 < 1.84\), so it slides first. ✓
:::

:::warn Check both before you claim one
"The block topples" is only true if the friction needed at that instant is no more than \(\mu R\); "the block slides" is only true if it has not already toppled. Compare the two critical values (the force, or the angle) and state which is smaller. A solution that finds one critical value and stops loses the final mark.
:::

Now see it for yourself. The widget below puts a solid on a plane that you tilt. The vertical dashed line through \(G\) shows whether the weight falls inside the base; the readouts give both critical angles. Start with the cone from the example, base radius 6 and height 20, and \(\mu = 0.8\).

:::html
<div class="widget" data-w="fm-topple" data-shape="cone" data-width="6" data-height="20" data-mu="0.8" data-alpha="30"></div>
:::

Raise the angle and watch it slide at \(38.7^\circ\) while \(G\) is still above the base. Then set \(\mu\) to \(1.5\) and raise the angle again: now the dashed line leaves the base at \(50.2^\circ\) and the cone topples. Switch to the cuboid and the cylinder to compare how a tall, thin solid behaves against a short, wide one.

:::exam What is given, and the form of the answer
There is nothing on MF19 for equilibrium itself: learn "resolve twice, moments once" and the friction law \(F \le \mu R\). The centre of mass results from [Centres of mass](#math.fm.com) are on MF19. Say where you are taking moments ("moments about \(A\)"), give each perpendicular distance as a product of length and \(\sin\) or \(\cos\), state when friction is limiting, and write a final sentence in words ("the ladder slips when the person is more than \(5.64\) m from \(A\)"). For toppling, compare both critical values.
:::

:::board
Moments and the equilibrium of rods and ladders also appear in Edexcel IAL and UK A Level Mechanics, which take \(g = 9.8\) where 9231 takes \(g = 10\); [Projectiles and moments (UK boards)](#math.m.projectiles) covers the moments and tipping of rods for those boards.
:::

:::eg Spot the error: a uniform ladder \(AB\), of length \(5\) m and weight \(200\) N, rests with \(A\) on rough horizontal ground and \(B\) against a smooth vertical wall, at \(70^\circ\) to the horizontal. Find the reaction of the wall (4 marks).
A student wrote this answer.

Line 1: Vertically, \(R_1 = 200\) N
Line 2: Moments about \(A\): \(R_2 \times 5 = 200 \times 2.5\)
Line 3: \(R_2 = 100\) N

Line 1 is correct. [B1] The student takes moments about the right point, with the wall reaction and the weight on opposite sides. [M1]

**But the distances in line 2 are wrong.** [A0] The wall reaction is horizontal, so its perpendicular distance from \(A\) is the height \(5\sin 70^\circ\). The weight is vertical, so its distance is the horizontal \(2.5\cos 70^\circ\). The lengths \(5\) and \(2.5\) lie along the ladder, which is not perpendicular to either force. Line 3 follows from line 2 but has the wrong value. [A0] The student scores 2 out of 4.

Correct line 2: \(R_2 \times 5\sin 70^\circ = 200 \times 2.5\cos 70^\circ\), so \(R_2 = \dfrac{100}{\tan 70^\circ} = 36.4\) N.

**Check**: this ladder is steep, so the wall only needs to push gently: \(36.4\) N is far less than the \(100\) N the student found. ✓
:::

:::try Start easy, finish at exam standard
Q: A uniform beam of length \(4\) m and weight \(60\) N rests on supports at its ends. A \(40\) N weight hangs from a point \(1\) m from one end, \(A\). Find the reaction at \(A\).
A: Moments about the other end \(B\): \(R_A \times 4 = 60 \times 2 + 40 \times 3\), so \(R_A = 60\) N.
Q: A uniform rod \(AB\) of length \(1.6\) m and weight \(24\) N is hinged at \(A\) and held horizontal by a vertical string at \(B\). Find the tension and the hinge reaction.
A: Moments about \(A\): \(T \times 1.6 = 24 \times 0.8\), so \(T = 12\) N. Vertically, \(Y + 12 = 24\), so \(Y = 12\) N upwards; there is no horizontal force.
Q: A uniform ladder of weight \(120\) N leans against a smooth wall at \(60^\circ\) to the ground. Find the horizontal force at the foot.
A: Moments about the foot (length \(2a\)): \(R_2 \times 2a\sin 60^\circ = 120 \times a\cos 60^\circ\), so \(R_2 = \dfrac{120\cos 60^\circ}{2\sin 60^\circ} = \dfrac{60}{1.732} = 34.6\) N. The friction at the foot equals this.
Q: A uniform solid cylinder of radius \(5\) cm and height \(30\) cm stands on a rough plane tilted at \(\alpha\). Find the angle at which it topples.
A: \(G\) is \(15\) cm above the base, half-width \(5\) cm: \(\tan\alpha = \dfrac{5}{15} = \dfrac13\), so \(\alpha = 18.4^\circ\).
Q: A cube of weight \(W\) stands on rough horizontal ground. A horizontal force acts at the top edge. Show that, for a cube of side \(l\), the cube topples at \(P = \tfrac12W\), if the friction is large enough.
A: Moments about the lower edge: \(P \times l = W \times \tfrac12l\), so \(P = \tfrac12W\).
Q: In the previous question, what is the least \(\mu\) for the cube to topple rather than slide?
A: Sliding needs \(P = \mu W\); toppling occurs first when \(\tfrac12W < \mu W\), so \(\mu > 0.5\).
Q: A uniform rod \(AB\) of length \(2a\) rests with end \(A\) on smooth horizontal ground and end \(B\) against a smooth wall, held by a horizontal string from \(A\) to the foot of the wall. The rod makes \(45^\circ\) with the ground and has weight \(W\). Find the tension.
A: Moments about \(A\): \(R_2 \times 2a\sin 45^\circ = W \times a\cos 45^\circ\), so \(R_2 = \tfrac12W\). The string balances \(R_2\): \(T = \tfrac12W\).
Q: A person stands at the midpoint of a uniform plank \(6\) m long, mass \(10\) kg, supported at its ends. The person has mass \(60\) kg. Find the reaction at each end (take \(g = 10\)).
A: By symmetry the reactions are equal: \(R = \tfrac12(100 + 600) = 350\) N each.
Q: A rod \(AB\) of weight \(40\) N rests in equilibrium with its end \(A\) on rough ground and its midpoint against a smooth peg. Which direction does the peg's reaction have?
A: The reaction is perpendicular to the rod at the point of contact, not vertical.
Q: A uniform ladder is in limiting equilibrium against a smooth wall. State in which direction the friction acts at the foot.
A: Towards the wall, to oppose the tendency of the foot to slide away from it.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Take \(g = 10\). A uniform beam \(AB\) of length \(6\) m and weight \(120\) N rests on a support at \(A\) and on a support at \(C\), where \(BC = 1.5\) m. Find the reaction at each support.
A: Moments about \(C\): \(R_A \times 4.5 = 120 \times 1.5\) [M1], so \(R_A = 40\) N. [A1]
Resolve vertically: \(R_C = 120 - 40\) [M1] \(= 80\) N. [A1]
Q: [6 marks] ★★ A uniform rod \(AB\) of length \(3\) m and weight \(40\) N is hinged at \(A\) to a vertical wall and held horizontal by a light string \(BC\), where \(C\) is on the wall \(2\) m above \(A\). A load of weight \(20\) N is attached to the rod at a point \(2\) m from \(A\). Find the tension in the string and the horizontal and vertical components of the force of the hinge on the rod.
A: \(\angle ABC = \tan^{-1}\tfrac23 = 33.7^\circ\). Moments about \(A\): \(T\sin 33.7^\circ \times 3 = 40 \times 1.5 + 20 \times 2\) [M1 A1], so \(T = \dfrac{100}{3 \times 0.5547} = 60.1\) N. [A1]
Horizontally, \(X = T\cos 33.7^\circ = 50.0\) N away from the wall. [M1 A1]
Vertically, \(Y = 60 - T\sin 33.7^\circ = 60 - 33.3 = 26.7\) N upwards. [A1]
Q: [5 marks] ★★ A uniform ladder of length \(4\) m and weight \(150\) N rests at \(65^\circ\) to the horizontal with its top against a smooth vertical wall and its foot on rough horizontal ground. The ladder is in equilibrium. Find the least possible value of the coefficient of friction.
A: Vertically \(R_1 = 150\). [B1]
Moments about the foot: \(R_2 \times 4\sin 65^\circ = 150 \times 2\cos 65^\circ\) [M1], so \(R_2 = \dfrac{75}{\tan 65^\circ} = 35.0\) N. [A1]
Horizontally \(F = R_2 = 35.0\) [M1], and \(\mu \ge \dfrac{35.0}{150} = 0.233\). [A1]
Q: [6 marks] ★★ A uniform ladder of length \(8\) m and weight \(250\) N rests against a smooth vertical wall, with its foot on rough ground (\(\mu = 0.4\)), at \(50^\circ\) to the horizontal. A person of weight \(750\) N stands on the ladder. How far along the ladder from its foot can the person stand before the ladder begins to slip?
A: Vertically, \(R_1 = 1000\). [B1] Limiting: \(R_2 = F = 0.4 \times 1000 = 400\). [B1]
Moments about the foot, with the person at distance \(d\): \(400 \times 8\sin 50^\circ = 250 \times 4\cos 50^\circ + 750 \times d\cos 50^\circ\) [M1 A1]
Evaluating: \(2451.3 = 642.8 + 482.1d\) [M1], so \(d = 3.75\) m. [A1]
Q: [5 marks] ★★ A uniform solid cylinder of radius \(6\) cm and height \(30\) cm rests with its flat base on a rough plane inclined at angle \(\alpha\), where the coefficient of friction is \(0.5\). The angle \(\alpha\) is gradually increased. Show whether the cylinder slides or topples first, giving the angle at which it happens.
A: The centre of mass is \(15\) cm above the base. [B1]
It topples when \(\tan\alpha = \dfrac{6}{15} = 0.4\) [M1], \(\alpha = 21.8^\circ\). [A1]
It slides when \(\tan\alpha = 0.5\) [M1], \(\alpha = 26.6^\circ\). [A1]
Since \(21.8^\circ < 26.6^\circ\), the cylinder topples first, at \(21.8^\circ\).
Q: [10 marks] (#math.p1.trig) ★★★ A uniform ladder of length \(2a\) and weight \(W\) rests at angle \(\theta\) to the horizontal with its foot on rough ground (coefficient of friction \(0.4\)) and its top against a rough vertical wall (coefficient of friction \(0.5\)). The ladder is in limiting equilibrium at both contacts. (a) Show that the normal reaction at the ground is \(\dfrac{W}{1.2}\). (b) Find the reaction and the friction at the wall. (c) Find \(\theta\).
H: Both contacts are limiting: \(F_1 = 0.4R_1\) and \(F_2 = 0.5R_2\). Horizontally \(R_2 = F_1\); vertically \(R_1 + F_2 = W\).
H: Moments about the foot: \(R_2\) acts at height \(2a\sin\theta\), \(F_2\) at horizontal distance \(2a\cos\theta\) and \(W\) at \(a\cos\theta\).
A: (a) \(F_1 = 0.4R_1\), \(R_2 = F_1 = 0.4R_1\), \(F_2 = 0.5R_2 = 0.2R_1\). [B1]
Vertically \(R_1 + 0.2R_1 = W\) [M1], so \(R_1 = \dfrac{W}{1.2}\). [A1]
(b) \(R_2 = 0.4R_1 = \dfrac{W}{3}\) [B1], \(F_2 = \dfrac{W}{6}\). [B1]
(c) \(\dfrac W3 \times 2a\sin\theta + \dfrac W6 \times 2a\cos\theta = W \times a\cos\theta\) [M1 A1]
Divide by \(Wa\cos\theta\): \(\dfrac23\tan\theta + \dfrac13 = 1\) [M1], so \(\tan\theta = 1\) [A1] and \(\theta = 45^\circ\). [A1]
Q: [8 marks] ★★★ A uniform rectangular block of weight \(400\) N has a base of width \(0.8\) m and a height of \(1.2\) m. It rests on rough horizontal ground, with coefficient of friction \(0.6\). A horizontal force \(P\) is applied to a vertical face at height \(1.0\) m above the ground. (a) Find the value of \(P\) at which the block is about to topple. (b) Find the value of \(P\) at which the block is about to slide. (c) State which happens first as \(P\) increases. (d) For what height \(k\) of the point of application do the two happen at the same value of \(P\)?
H: At the point of toppling the reaction is at the edge: take moments about that edge.
H: At the point of sliding \(F = P = \mu R\) with \(R = W\).
A: (a) \(P \times 1.0 = 400 \times 0.4\) [M1 A1], \(P = 160\) N. [A1]
(b) \(P = 0.6 \times 400\) [M1] \(= 240\) N. [A1]
(c) \(160 < 240\), so the block topples first. [B1]
(d) Equal values: \(\dfrac{400 \times 0.4}{k} = 240\) [M1], \(k = 0.667\) m. [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A uniform solid cone has base radius \(r\) and height \(h\), and stands with its base on a rough plane of coefficient of friction \(\mu\), inclined at angle \(\alpha\). Show that, as \(\alpha\) increases, the cone topples before it slides if and only if \(\mu > \dfrac{4r}{h}\). Find the least value of \(\mu\) for which this happens when \(h = 3r\).
H: The centre of mass is \(\tfrac14h\) above the base. Compare the two critical values of \(\tan\alpha\).
H: Toppling: \(\tan\alpha = \dfrac{r}{h/4}\). Sliding: \(\tan\alpha = \mu\).
A: The centre of mass is \(\tfrac14h\) above the base, and the half-width is \(r\). [B1]
It topples when \(\tan\alpha_t = \dfrac{r}{h/4} = \dfrac{4r}{h}\). [M1 A1]
It slides when \(\tan\alpha_s = \mu\). [B1]
Toppling comes first when \(\tan\alpha_t < \tan\alpha_s\), that is \(\dfrac{4r}{h} < \mu\), which is the stated condition. [A1]
For \(h = 3r\), \(\mu > \dfrac43\). [B1]
Q: [6 marks] ★★★ A uniform rod \(AB\) of length \(2a\) and weight \(W\) has its end \(A\) on a smooth horizontal floor and its end \(B\) against a smooth vertical wall. It is held at angle \(\theta\) to the floor by a light horizontal string joining \(A\) to the foot of the wall. (a) Show that the tension in the string is \(\tfrac12W\cot\theta\). (b) The string can bear a tension of at most \(\tfrac13W\). Find the least angle \(\theta\).
H: The floor and wall are smooth, so the reactions are vertical (at \(A\)) and horizontal (at \(B\)).
H: Take moments about \(A\).
A: (a) The floor reaction at \(A\) is vertical and equals \(W\); the wall reaction \(R\) at \(B\) is horizontal, balancing the tension: \(T = R\). [B1]
Moments about \(A\): \(R \times 2a\sin\theta = W \times a\cos\theta\) [M1 A1], so \(R = \tfrac12W\cot\theta\) and \(T = \tfrac12W\cot\theta\). [A1]
(b) \(\tfrac12\cot\theta \le \tfrac13\) gives \(\tan\theta \ge \tfrac32\) [M1], so \(\theta \ge 56.3^\circ\). [A1]
:::

:::quiz
? A uniform ladder rests against a smooth vertical wall. What is the direction of the wall's force on the ladder?
+ Horizontal, perpendicular to the wall
- Along the ladder
- Vertically upwards
- Perpendicular to the ladder
> A smooth surface gives a reaction perpendicular to itself, and the wall is vertical, so the reaction is horizontal. A reaction perpendicular to the ladder is what a smooth peg or edge gives, not a wall.
? Which point is the best to take moments about for a ladder with unknown reactions at both ends?
+ The foot of the ladder, where the ground reaction and friction both act
- The centre of the ladder
- The top of the ladder, where the wall reaction acts
- The point on the ground directly below the centre of the ladder
> The moment equation is true about every point, but the foot removes two unknowns (the ground reaction and the friction). The top would remove only one, and the centre removes none. The answer is the same, but the work differs.
? A block is about to topple about its lower edge. Which statement is true at that instant?
+ The whole normal reaction acts at that edge
- The friction at the base is zero
- The block has started to slide
- The weight acts at the edge
> At toppling the base touches the surface only along the edge, so \(R\) and \(F\) act there. The weight still acts at \(G\); its line of action passes through the edge. Friction need not be zero, and the block has not slid.
? A cone on a slope has critical angles \(50.2^\circ\) for toppling and \(38.7^\circ\) for sliding. What happens as the slope is raised?
+ It slides first, at \(38.7^\circ\)
- It topples first, at \(38.7^\circ\)
- It topples first, at \(50.2^\circ\)
- It slides and topples at the same time
> The smaller critical angle is reached first. Here that is \(38.7^\circ\), for sliding, and the cone has moved before the slope reaches the toppling angle.
? Three forces keep a rod in equilibrium and two of them meet at a point. What follows?
+ The third force's line of action passes through that point
- The third force is zero
- The three forces are parallel
- The rod is at the point of toppling
> If two lines meet at a point, the moments of those forces about it are zero, so the third force must have zero moment about it too, which means its line passes through the point.
? A rod rests against a smooth peg. Which of these is the direction of the peg's reaction on the rod?
+ Perpendicular to the rod
- Vertically upwards
- Along the rod
- Horizontal
> A smooth contact gives a force perpendicular to the surfaces in contact: at a peg or edge that is perpendicular to the rod. Drawing it vertical is a common slip.
:::

:::checklist What you can now do
- [ ] I can state the two conditions for a rigid body in equilibrium under coplanar forces, and the converse.
- [ ] I can draw all the forces on a rod or ladder, including friction and the reaction at a hinge, a peg or a smooth wall.
- [ ] I can solve problems on beams, rods hinged to walls and rods held by strings, by resolving and taking moments at a well-chosen point.
- [ ] I can solve ladder problems with a smooth or a rough wall, including limiting equilibrium and a person climbing.
- [ ] I can use the three-force rule: the lines of action of three non-parallel forces in equilibrium are concurrent.
- [ ] I can decide whether a block pushed by a force, or a solid on a rough plane, topples or slides first, and find the critical force or angle.
:::

:::recap
- A rigid body is in equilibrium if and only if the vector sum of the forces is zero and the sum of moments about any point is zero.
- Smooth contact: one reaction, perpendicular to the surface (perpendicular to the rod at a peg). Rough contact: \(R\) and \(F\), \(F \le \mu R\), with \(F = \mu R\) at limiting equilibrium. Hinge: two components.
- Resolve twice, take moments once about the point where most unknowns act; use perpendicular distances (horizontal for vertical forces, vertical for horizontal forces).
- Ladder at angle \(\theta\), smooth wall: \(R_2 = \tfrac12W\cot\theta\) for a uniform ladder, and friction at the foot is \(R_2\).
- Three non-parallel forces in equilibrium: lines of action concurrent.
- Slides when \(F\) exceeds \(\mu R\) (on a slope, \(\tan\alpha > \mu\)); topples when the weight's line passes outside the base (\(\tan\alpha > a/h\)). The smaller critical value is the one that happens first.
:::

:::links
- watch: [Toppling playlist](https://www.youtube.com/playlist?list=PL5pdglZEO3NgTf2HUkNHheRbMCrt00iyD) · ExamSolutions (YouTube) · toppling and sliding questions, worked step by step
- practise: [Mechanics booklets](https://madasmaths.com/archive_maths_booklets_mechanics.html) · MadAsMaths · moments, ladders and equilibrium questions with answers
- papers: [9231 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fm/) · Physics & Maths Tutor · real Further Mechanics questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Hooke's law and elastic energy](#math.fm.elastic) turns to strings and springs: the force in a stretched string, and the energy stored in it.
