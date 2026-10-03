@chapter math.m.forces
@title Forces and equilibrium
@level as
@paper CAIE P4 · Edexcel IAL M1 · UK Mechanics
@time 5–7 hours
@summary Mechanics begins with forces. You will learn to name the forces on an object, draw a force diagram, resolve forces into components, find a resultant, and use equilibrium, friction and Newton's third law on flat surfaces and slopes.

:::why
Every bridge, crane, climbing rope and roof is designed so that the forces on it balance. If they do not, something moves, usually in the wrong direction. Mechanics is the mathematics of forces and motion. It is a short, high-scoring paper (Cambridge Paper 4) once you can draw a good force diagram, and this chapter teaches the skills that every later mechanics chapter uses: spotting forces, splitting them into components and writing equations.
:::

**Before you start**, you need right-angled triangle trigonometry from [Geometry and trigonometry basics](#math.f.geometry) and confident algebra from [Algebra from scratch](#math.f.algebra). Slopes use \(\sin\) and \(\cos\) of angles, as in [Trigonometry](#math.p1.trig).

## Forces and the mechanics model

A **force** is a push or a pull. Forces are measured in **newtons** (N). They have both a size and a direction, so they are vectors: a force of 10 N means nothing until you say which way it acts.

:::def Force
A push or a pull on an object. It is a vector quantity, measured in newtons (N). A resultant force on an object changes its velocity.
:::

:::def Resultant force
The single force that has the same effect as all the forces on an object together. It is the vector sum of the forces.
:::

Real objects are complicated, so mechanics replaces them with simple **models**. The words in an exam question tell you what to ignore.

| Word in the question | What it means for your model |
|---|---|
| particle | All the mass is at one point. Ignore size, shape and spin. |
| light (string, rod, pulley) | The mass is zero. A light string has the same tension at both ends. |
| inextensible string | It does not stretch, so connected objects move together. |
| smooth | No friction. The contact force is perpendicular to the surface. |
| rough | Friction may act. |
| uniform (rod, plank) | The mass is spread evenly, so the weight acts at the midpoint. |
| smooth pulley or peg | A string slides over it freely, so the tension is the same on both sides. |

A model is a simplification, and Cambridge can ask about its limits. No real surface is perfectly smooth, so a "smooth" model predicts that an object starts to slide under the smallest push and never slows down by itself. It works well for ice or a polished, greased surface, but it overestimates speeds and underestimates the force needed to hold an object still on anything rougher.

## The forces you will meet

| Force | Usual symbol | Direction | Where it comes from |
|---|---|---|---|
| Weight | \(W = mg\) | Vertically down | Gravity pulling on mass \(m\) |
| Normal reaction | \(R\) | Perpendicular to the surface, away from it | A surface pushing back |
| Friction | \(F\) | Along the surface, against sliding | A rough surface |
| Tension | \(T\) | Along the string, pulling the object | A taut string or rope |
| Thrust | \(T\) | Along a rod, pushing the object | A compressed rod |
| Driving force | \(D\) | In the direction of motion | An engine, or a person pushing |
| Resistance | \(F\) or a number | Against the motion | Air, water, friction in the machinery |

**Mass** \(m\) (in kg) measures how much matter an object has. **Weight** is the force of gravity on it, \(W = mg\). Cambridge tells you to "take \(g = 10\)", so a 5 kg mass has weight \(5 \times 10 = 50\) N. Edexcel and the UK boards use \(g = 9.8\), so the same mass weighs 49 N. Use whichever value the paper gives.

:::def Normal reaction
The component of the contact force between two surfaces that acts at right angles ("normal") to the surfaces, pushing the object away from the surface.
:::

## Force diagrams

A **force diagram** shows every force on one object. Nearly every mechanics mark depends on drawing it carefully, so do it first, every time.

:::html
<figure class="fig"><svg viewBox="40 90 520 235" role="img" aria-label="A crate on rough ground pulled by a rope at angle theta above the horizontal. Weight acts down, the normal reaction up, friction to the left and tension along the rope, with the tension split into horizontal and vertical components.">
  <path class="ln thick" d="M50 218H550"/>
  <text class="tl" x="52" y="240">rough horizontal floor</text>
  <rect class="f1 s-acc sw2" x="245" y="162" width="110" height="56" rx="4"/>
  <path class="ln-m dash" d="M300 190H360.6V155.4"/>
  <path class="ln" d="M300 190V287" marker-end="url(#ah)"/>
  <path class="ln" d="M300 190V127" marker-end="url(#ah)"/>
  <path class="ln" d="M300 190H240.5" marker-end="url(#ah)"/>
  <path class="c1" d="M300 190L360 155.4" marker-end="url(#ah-math)"/>
  <circle class="fi" cx="300" cy="190" r="3.5"/>
  <path class="ln-m thin" d="M338 190A38 38 0 0 0 332.9 171"/>
  <text class="tl halo" x="345" y="185">θ</text>
  <text class="halo tb" x="308" y="152">R</text>
  <text class="halo tb" x="308" y="284">W = mg</text>
  <text class="halo tb ta" x="366" y="150">T</text>
  <text class="halo tb" x="233" y="195" text-anchor="end">F</text>
  <text class="tl halo" x="366" y="207">T cos θ</text>
  <text class="tl halo" x="368" y="178">T sin θ</text>
  <path class="ln-m" d="M430 262H520" marker-end="url(#ahm)"/>
  <text class="tl" x="430" y="282">direction of motion</text>
</svg><figcaption>A crate pulled along rough ground by a rope at angle θ. Every force is drawn from the centre of the crate (the particle model). The tension T is split into T cos θ along the ground and T sin θ upwards. The upward part carries some of the weight, so R is smaller than W.</figcaption></figure>
:::

:::steps
1. Draw the object as a box or a dot. For a particle, draw every force starting at the same point.
2. Draw the weight \(W = mg\) straight down.
3. Look at everything touching the object. For each surface draw a normal reaction \(R\), and a friction force \(F\) if the surface is rough. For each string draw a tension \(T\) pulling away from the object along the string.
4. Add any given forces (a push, a pull, a driving force) and any resistance.
5. Label every force with its size or a letter, and mark the direction you will take as positive.
:::

:::warn Do not invent forces
There is no "force of motion" and no "force of the throw" once a ball has left your hand. An object needs a force to change its velocity, not to keep moving. Every force on your diagram must come from something you can name: gravity, a surface, a string, an engine.
:::

## Resolving forces

A force at an angle can be replaced by two perpendicular forces, called its **components**, which together have exactly the same effect. Finding them is called **resolving**.

:::key Resolving a force
A force \(F\) at angle \(\theta\) to a given direction has components
- \(F\cos\theta\) **along** that direction, and
- \(F\sin\theta\) **perpendicular** to it.

The angle must be measured from the direction you are resolving along. If you are given the angle to the other direction, swap \(\cos\) and \(\sin\).
:::

:::eg A force of 20 N acts at \(30^\circ\) above the horizontal. Find its horizontal and vertical components.
Horizontal: \(20\cos 30^\circ = 17.3\) N.

Vertical: \(20\sin 30^\circ = 10.0\) N.

**Check:** \(\sqrt{17.3^2 + 10^2} = 20\), as it should be.
:::

:::tip Choose your two directions wisely
You can resolve in any two perpendicular directions. Choose them so that as many unknown forces as possible lie along one of them. On a slope, resolve along and perpendicular to the slope. With strings, use horizontal and vertical.
:::

## Resultant of several forces

To find the resultant: choose \(x\) and \(y\) directions, add up all the \(x\)-components, add up all the \(y\)-components, then combine the two totals with Pythagoras and \(\tan\).

:::eg Two forces act on a particle at \(O\). \(P = 12\) N acts along the positive \(x\)-axis. \(Q = 10\) N acts at \(60^\circ\) above the negative \(x\)-axis. Find the magnitude and direction of the resultant.
Components of \(Q\): \(x\)-component \(-10\cos 60^\circ = -5\), and \(y\)-component \(10\sin 60^\circ = 8.66\).

Totals: \(X = 12 - 5 = 7\) N and \(Y = 8.66\) N.

\[\text{magnitude} = \sqrt{7^2 + 8.66^2} = \sqrt{124} = 11.1 \text{ N}\]
\[\tan\alpha = \frac{8.66}{7} \quad\Rightarrow\quad \alpha = 51.1^\circ\]

The resultant is 11.1 N, at \(51.1^\circ\) above the positive \(x\)-axis.
:::

The widget below holds this example: 12 N at \(0^\circ\) and 10 N at \(120^\circ\) (the angle of \(Q\) measured from the positive \(x\)-axis). Add a third force, change an angle, and watch \(\Sigma X\) and \(\Sigma Y\) change. Tick the box to draw the balancing force: it has the same size as the resultant and points the opposite way, which is what equilibrium needs.

:::html
<div class="widget" data-w="resultant" data-forces="12@0; 10@120"></div>
:::

## Equilibrium

:::def Equilibrium
A particle is in equilibrium when the resultant force on it is zero. It is then either at rest or moving in a straight line at constant speed (Newton's first law).
:::

Equilibrium gives two equations, one for each of two perpendicular directions: the components in each direction add to zero. In words: forces up = forces down, and forces left = forces right.

:::eg A particle of mass 5 kg hangs in equilibrium from two light strings. One string makes \(30^\circ\) with the horizontal and the other makes \(60^\circ\) with the horizontal, on opposite sides. Find the tension in each string. Take \(g = 10\).
The weight is \(5 \times 10 = 50\) N. Let \(T_1\) be the tension in the \(30^\circ\) string and \(T_2\) the tension in the \(60^\circ\) string.

Horizontally, left equals right:
\[T_1\cos 30^\circ = T_2\cos 60^\circ \quad\Rightarrow\quad T_2 = \sqrt{3}\,T_1\]
Vertically, up equals down:
\[T_1\sin 30^\circ + T_2\sin 60^\circ = 50\]
Substitute \(T_2 = \sqrt3\,T_1\):
\[\tfrac12 T_1 + \sqrt3\cdot\tfrac{\sqrt3}{2}T_1 = \tfrac12 T_1 + \tfrac32 T_1 = 2T_1 = 50\]
So \(T_1 = 25\) N and \(T_2 = 25\sqrt3 = 43.3\) N.

**Sense check:** the steeper string carries more of the weight, so its tension is larger.
:::

## Friction

When two rough surfaces are pushed together, a **friction** force acts along the surfaces and resists sliding.

:::def Friction
A contact force that acts along the surfaces, opposing sliding (or the tendency to slide). It is zero for a smooth contact.
:::

Friction can only be as big as the situation needs, up to a maximum that depends on how hard the surfaces are pressed together:

:::key The friction law
\[F \leq \mu R\]
where \(R\) is the normal reaction and \(\mu\) is the **coefficient of friction** between the two surfaces. When the object is **about to slip** (limiting equilibrium) or is **sliding**, \(F = \mu R\), and friction acts against the motion (or the direction it would move).
:::

:::def Limiting friction
The maximum value of friction, \(\mu R\), reached when an object is on the point of slipping.
:::

The **contact force** between two surfaces is the resultant of \(R\) and \(F\). Its magnitude is \(\sqrt{R^2 + F^2}\).

:::warn Friction is not always \(\mu R\)
Take a 10 kg box on a floor with \(\mu = 0.4\) (so \(R = 100\) N and the maximum friction is 40 N). If you push it with only 30 N, nothing moves, and the friction is **30 N**, not 40 N. Friction matches the push until the push exceeds \(\mu R\). Write \(F = \mu R\) only when the question says "limiting equilibrium", "about to slip" or "sliding".
:::

:::eg A crate of mass 10 kg lies on rough horizontal ground with coefficient of friction 0.4. A rope at \(30^\circ\) above the horizontal pulls it. Find the tension in the rope when the crate is about to slide. Take \(g = 10\).
The rope lifts the crate slightly, so \(R\) is less than the weight.

Vertically: \(R + T\sin 30^\circ = 100\), so \(R = 100 - 0.5T\).

Horizontally: \(T\cos 30^\circ = F\). The crate is about to slide, so \(F = 0.4R\).
\[T\cos 30^\circ = 0.4(100 - 0.5T) \quad\Rightarrow\quad T(\cos 30^\circ + 0.2) = 40\]
\[T = \frac{40}{1.0660} = 37.5 \text{ N}\]
Then \(R = 100 - 0.5(37.5) = 81.2\) N.
:::

## Inclined planes

On a slope, resolve **along** the slope and **perpendicular** to it. Gravity does not point along either direction, so the weight must be split.

:::html
<figure class="fig"><svg viewBox="30 20 450 275" role="img" aria-label="A block on a slope inclined at angle theta. Weight acts straight down and is split into mg sin theta down the slope and mg cos theta into the slope. The normal reaction acts perpendicular to the slope and friction acts up the slope.">
  <polygon class="fm s-mute sw1" points="70,260 433.7,50 433.7,260"/>
  <path class="ln thick" d="M40 260H470"/>
  <path class="ln thick" d="M70 260L433.7 50"/>
  <polygon class="f1 s-acc sw2" points="234.5,165 300.4,127 277.4,87.2 211.5,125.2"/>
  <path class="ln-m dot" d="M208.4 153.6L256 236.1M303.6 208.6L256 236.1"/>
  <path class="c1" d="M256 126.1L208.4 153.6" marker-end="url(#ah-math)"/>
  <path class="c1" d="M256 126.1L303.6 208.6" marker-end="url(#ah-math)"/>
  <path class="ln" d="M256 126.1V234" marker-end="url(#ah)"/>
  <path class="ln" d="M256 126.1L208.4 43.6" marker-end="url(#ah)"/>
  <path class="ln" d="M256 126.1L303.6 98.6" marker-end="url(#ah)"/>
  <circle class="fi" cx="256" cy="126.1" r="3.5"/>
  <path class="ln-m thin" d="M130 260A60 60 0 0 0 122 230"/>
  <text class="tl" x="136" y="253">θ</text>
  <path class="ln-m thin" d="M256 166.1A40 40 0 0 0 276 160.7"/>
  <text class="tl halo" x="263" y="180">θ</text>
  <text class="halo tb" x="200" y="55" text-anchor="end">R</text>
  <text class="halo tb" x="310" y="97">F</text>
  <text class="halo tb" x="264" y="250">W = mg</text>
  <text class="tl ta halo" x="202" y="168" text-anchor="end">mg sin θ</text>
  <text class="tl ta halo" x="310" y="216">mg cos θ</text>
</svg><figcaption>A block on a slope at angle θ. The weight mg is split into mg sin θ down the slope and mg cos θ into the slope. The normal reaction R balances mg cos θ. Friction F acts up the slope because the block tends to slide down.</figcaption></figure>
:::

:::key Weight on a slope inclined at angle \(\theta\)
- Component of weight **down** the slope: \(mg\sin\theta\)
- Component of weight **into** the slope: \(mg\cos\theta\)
- With no other forces perpendicular to the slope, \(R = mg\cos\theta\).
- A block just about to slide down a rough slope, with no other forces, has \(\mu = \tan\theta\).
:::

:::eg (Exam style) A block of mass 5 kg rests on a rough plane inclined at angle \(\theta\) to the horizontal, where \(\sin\theta = 0.6\) and \(\cos\theta = 0.8\). The coefficient of friction between the block and the plane is 0.5. A force of magnitude \(P\) N acts on the block up the plane, parallel to a line of greatest slope. Find the set of values of \(P\) for which the block stays in equilibrium. Take \(g = 10\).
Perpendicular to the plane: \(R = 50\cos\theta = 50 \times 0.8 = 40\) N. [M1 A1]

Maximum friction: \(F_{\max} = 0.5 \times 40 = 20\) N. [B1]

The weight component down the plane is \(50\sin\theta = 30\) N. [B1]

**Least \(P\):** the block is about to slide down, so friction acts up the plane. Resolving along the plane: \(P + 20 = 30\), so \(P = 10\). [M1 A1]

**Greatest \(P\):** the block is about to slide up, so friction acts down the plane. Resolving along the plane: \(P = 30 + 20 = 50\). [M1 A1]

The block is in equilibrium for \(10 \leq P \leq 50\). [A1]
:::

## Newton's third law

:::def Newton's third law
If object A exerts a force on object B, then B exerts an equal and opposite force on A. The two forces are the same type of force and act on **different** objects.
:::

Think of two ice-skaters who push off from each other: each feels the same size of force, in opposite directions. A common error concerns a book on a table. The weight of the book and the normal reaction on the book are equal and opposite, but they are **not** a third-law pair, because both act on the book. The partner of the book's weight is the book's pull on the Earth. The partner of the table's push on the book is the book's push on the table.

In problems, the law tells you that a string pulling two particles has the same tension on both, and that two blocks in contact push on each other with equal and opposite forces.

:::board
Cambridge 9709 Paper 4 and Edexcel IAL Mechanics 1 treat this topic in the same way and use the same model words. The differences are small. Cambridge says "take \(g = 10\)" and expects 3 significant figures. Edexcel IAL and the UK boards use \(g = 9.8\) and expect 2 or 3 significant figures. Edexcel IAL also gives forces as vectors in \(\mathbf{i}\) and \(\mathbf{j}\) notation, such as \((3\mathbf{i} - 2\mathbf{j})\) N, which you add component by component. In the UK A Level Mathematics specifications (Edexcel, AQA, OCR), friction and \(F \leq \mu R\) are second-year content.
:::

:::exam Forces questions: where the marks are
Draw the force diagram before writing any equation, and mark the positive direction. Examiners give a method mark for each correct resolving equation, so write one equation for each direction. Give the full working for \(R\) before using \(F = \mu R\). State "limiting equilibrium" when you use \(F = \mu R\), and give answers to 3 significant figures.
:::

:::try Start easy, finish at exam standard
Q: A force of 50 N acts at \(40^\circ\) above the horizontal. Find its horizontal and vertical components.
A: Horizontal: \(50\cos 40^\circ = 38.3\) N. Vertical: \(50\sin 40^\circ = 32.1\) N.
Q: A particle of mass 2.5 kg hangs at rest from a light vertical string. Find the tension. Take \(g = 10\).
A: Equilibrium: the tension balances the weight, \(T = 2.5 \times 10 = 25\) N.
Q: A box of mass 8 kg rests on a rough horizontal floor with coefficient of friction 0.25. A horizontal force of 15 N is applied to the box. Take \(g = 10\). (a) Show that the box does not move. (b) Find the friction force. (c) Find the magnitude of the contact force between the box and the floor.
A: (a) \(R = 80\) N, so the maximum friction is \(0.25 \times 80 = 20\) N. The push of 15 N is less than 20 N, so the box does not move.
(b) The box is in equilibrium, so \(F = 15\) N (not 20 N).
(c) Contact force \(= \sqrt{R^2 + F^2} = \sqrt{80^2 + 15^2} = 81.4\) N.
Q: A particle of mass 6 kg rests on a smooth plane inclined at \(30^\circ\) to the horizontal. It is held by a light string parallel to the plane. Find the tension in the string and the normal reaction. Take \(g = 10\).
A: Along the plane: \(T = 60\sin 30^\circ = 30\) N. Perpendicular to the plane: \(R = 60\cos 30^\circ = 52.0\) N.
Q: A block rests in limiting equilibrium on a rough plane inclined at \(20^\circ\) to the horizontal. No other force acts on it. Find the coefficient of friction.
A: Along the plane: \(F = mg\sin 20^\circ\). Perpendicular: \(R = mg\cos 20^\circ\). Limiting: \(F = \mu R\), so \(\mu = \tan 20^\circ = 0.364\).
Q: Forces of 6 N and 8 N act on a particle at right angles to each other. A third force \(F\) keeps the particle in equilibrium. Find the magnitude of \(F\) and the angle between \(F\) and the 8 N force.
A: The resultant of the 6 N and 8 N forces is \(\sqrt{36 + 64} = 10\) N, at \(\tan^{-1}(6/8) = 36.9^\circ\) to the 8 N force. \(F\) must be equal and opposite, so \(F = 10\) N, and the angle between \(F\) and the 8 N force is \(180^\circ - 36.9^\circ = 143.1^\circ\).
Q: (Exam style) A block of mass 4 kg is held in equilibrium on a smooth plane inclined at \(30^\circ\) to the horizontal by a horizontal force of magnitude \(P\) N. Find \(P\) and the normal reaction \(R\). Take \(g = 10\).
A: Resolve along the plane: \(P\cos 30^\circ = 40\sin 30^\circ\). [M1]
\(P = 40\tan 30^\circ = 23.1\) N. [A1]
Resolve perpendicular to the plane: \(R = 40\cos 30^\circ + P\sin 30^\circ\). [M1]
\(R = 34.64 + 11.55 = 46.2\) N. [A1]
Q: (Exam style) A block of mass 3 kg is on a rough plane inclined at \(30^\circ\) to the horizontal, with coefficient of friction 0.2. A horizontal force \(P\) N pushes the block up the plane and the block is about to slide up. Find \(P\). Take \(g = 10\).
A: Perpendicular to the plane: \(R = 30\cos 30^\circ + P\sin 30^\circ\). [M1 A1]
Along the plane (friction acts down the plane): \(P\cos 30^\circ = 30\sin 30^\circ + 0.2R\). [M1 A1]
Substitute: \(P\cos 30^\circ = 15 + 0.2(25.98 + 0.5P)\), so \(P(0.8660 - 0.1) = 15 + 5.196\). [M1]
\(P = \dfrac{20.196}{0.7660} = 26.4\) N. [A1]
:::

:::quiz
? A 6 kg box rests on a rough horizontal floor with \(\mu = 0.5\). A horizontal force of 20 N is applied and the box does not move. Take \(g = 10\). What is the friction force?
- 30 N
+ 20 N
- 10 N
- 0 N
> The maximum friction is \(0.5 \times 60 = 30\) N, but friction is only as large as needed. The box is in equilibrium, so friction equals the 20 N push.
? A block of mass \(m\) is on a smooth slope inclined at \(\theta\) to the horizontal. What is the component of its weight down the slope?
- \(mg\cos\theta\)
+ \(mg\sin\theta\)
- \(mg\tan\theta\)
- \(mg\)
> The component along the slope uses \(\sin\theta\), and the component into the slope uses \(\cos\theta\). Check with \(\theta = 0^\circ\): a flat surface has no component down it, and \(\sin 0^\circ = 0\).
? A book rests on a table. Which pair of forces is a Newton's third law pair?
- The weight of the book and the table's push on the book
+ The Earth's pull on the book and the book's pull on the Earth
- The weight of the book and the book's push on the table
> A third-law pair acts on two different objects and is the same type of force. The first option is two forces on the book that balance. The third option mixes gravity with a contact force.
? A particle is in equilibrium under three forces. Which statement must be true?
+ The resultant force is zero.
- The particle is at rest.
- The three forces have equal magnitudes.
- Each force is perpendicular to the other two.
> Equilibrium means zero resultant force. The particle could be at rest or moving at constant velocity, and the forces can have any magnitudes that balance.
:::

:::recap
- A force is a vector, measured in newtons. Weight is \(W = mg\); take \(g = 10\) (Cambridge) or \(g = 9.8\) (Edexcel and UK boards).
- Always draw a force diagram: weight, then a normal reaction and friction at each surface, then tensions and any given forces.
- A force \(F\) at angle \(\theta\) to a direction has components \(F\cos\theta\) along it and \(F\sin\theta\) perpendicular to it.
- The resultant comes from adding components in two perpendicular directions, then using Pythagoras and \(\tan\).
- Equilibrium means the resultant is zero: the components add to zero in each of two perpendicular directions.
- Friction obeys \(F \leq \mu R\), with \(F = \mu R\) only when the object is about to slip or is sliding.
- On a slope, the weight splits into \(mg\sin\theta\) down the slope and \(mg\cos\theta\) into it.
- Newton's third law: the two forces of a pair are equal, opposite, of the same type, and act on different objects.
:::

:::links
- watch: [Resolving forces](https://www.examsolutions.net/tutorials/resolving-forces/) · ExamSolutions · components in two directions
- watch: [Friction and limiting equilibrium](https://www.examsolutions.net/tutorials/friction-limiting-equilibrium-coefficient-friction/) · ExamSolutions · F = μR and "about to slip"
- practise: [CAIE Mechanics: resolving, slopes and friction exam questions](https://www.savemyexams.com/a-level/maths/cie/20/mechanics/topic-questions/forces-and-equilibrium/resolving-forces-inclined-planes-and-friction/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Forces and Motion: Basics](https://phet.colorado.edu/en/simulations/forces-and-motion-basics) · PhET · push, friction and net force
- explore: [Vector Addition](https://phet.colorado.edu/en/simulations/vector-addition) · PhET · add forces as vectors and read the components
- papers: [9709 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-4) · Physics & Maths Tutor · papers with mark schemes [unofficial]

Links checked 3 October 2026.
:::
Next: [Kinematics: describing motion](#math.m.kinematics) describes how an object moves, and [Newton's laws and connected particles](#math.m.newton) links forces to that motion.
