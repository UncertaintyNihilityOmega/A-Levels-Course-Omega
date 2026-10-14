@chapter phys.dynamics
@title Dynamics and momentum
@level as
@paper CAIE P1 · P2 (AS)
@time 6–8 hours
@summary Why objects accelerate: mass, weight, Newton's three laws, momentum and force as its rate of change, friction and drag with terminal velocity, and the conservation of momentum in collisions and explosions in one and two dimensions.

:::why
Kinematics describes how things move; dynamics explains why. Every question about a car braking, a rocket launching, a skydiver falling or two snooker balls colliding comes down to the same few ideas: a resultant force changes momentum, and in a closed system momentum is never lost. Safety features such as crumple zones and airbags, and the design of every vehicle, are applications of exactly this chapter.
:::

**Before you start**, you need the suvat equations and velocity–time graphs from [Kinematics](#phys.kinematics), and resolving and adding vectors from [Physical quantities, units and uncertainty](#phys.units). The syllabus assumes you have met forces at IGCSE, so here is the two-sentence version. A **force** is a push or a pull, measured in newtons (N), and it has a size and a direction. The **resultant force** on an object is the single force that has the same effect as all the forces acting on it together.

:::try Warm-up
Q: A car speeds up from \(5.0\,\mathrm{m\,s^{-1}}\) to \(20\,\mathrm{m\,s^{-1}}\) in \(6.0\,\mathrm{s}\). Find its acceleration. (from [Kinematics](#phys.kinematics))
A: \(a = \dfrac{\Delta v}{\Delta t} = \dfrac{20 - 5.0}{6.0} = 2.5\,\mathrm{m\,s^{-2}}\). This is also the gradient of the velocity–time graph.
Q: A trolley starts from rest and accelerates uniformly at \(3.0\,\mathrm{m\,s^{-2}}\) for \(4.0\,\mathrm{s}\). How far does it travel? (from [Kinematics](#phys.kinematics))
A: \(s = ut + \tfrac12 at^2 = 0 + \tfrac12 \times 3.0 \times 4.0^2 = 24\,\mathrm{m}\).
Q: Two perpendicular forces of \(30\,\mathrm{N}\) and \(40\,\mathrm{N}\) act on an object at the same point. Find the size of the resultant. (from [Physical quantities, units and uncertainty](#phys.units))
A: \(\sqrt{30^2 + 40^2} = 50\,\mathrm{N}\), at \(\tan^{-1}(40/30) = 53.1^\circ\) to the \(30\,\mathrm{N}\) force.
:::

## Mass and weight

Pick up a bowling ball and a beach ball of the same size. The bowling ball is much harder to start moving, and much harder to stop. That reluctance to change its motion is a property of the object itself, and it is called mass.

:::def Mass
The property of an object that resists changes in its motion.
:::

Mass is measured in kilograms and has no direction. It does not change when you move the object to the Moon, or into space. Weight is a different quantity altogether.

:::def Weight
The force on a mass due to a gravitational field. Weight is a force, measured in newtons, and it acts towards the centre of the Earth (or whichever body is attracting the mass).
:::

Near the Earth's surface every kilogram of mass experiences a force of about \(9.81\,\mathrm{N}\). This number is the **gravitational field strength** \(g\), and it is also the **acceleration of free fall**: the two descriptions are the same quantity (\(1\,\mathrm{N\,kg^{-1}} = 1\,\mathrm{m\,s^{-2}}\)). We meet fields properly in [Gravitational fields](#phys.gravity).

:::formula Weight
\[W = mg\]
\(W\): weight (N) · \(m\): mass (kg) · \(g\): acceleration of free fall, \(9.81\,\mathrm{m\,s^{-2}}\) on the Earth (the data-sheet value).
:::

:::eg A 65 kg astronaut stands on the Earth, and later on the Moon where the gravitational field strength is \(1.62\,\mathrm{N\,kg^{-1}}\). Find the astronaut's mass and weight in each place.
The mass is \(65\,\mathrm{kg}\) in both places, because mass does not depend on the field.

On the Earth: \(W = mg = 65 \times 9.81 = 637.65\,\mathrm{N}\), which is \(638\,\mathrm{N}\) to 3 significant figures.

On the Moon: \(W = 65 \times 1.62 = 105.3\,\mathrm{N}\), which is \(105\,\mathrm{N}\).

The astronaut weighs about one sixth as much on the Moon, but is exactly as hard to push around. Carry full precision through a calculation and round only the final answer.
:::

:::warn Mass is not weight
In everyday speech "weight" means mass ("I weigh 65 kg"). In physics, never write kilograms for a weight or newtons for a mass. A balance compares masses and gives the same reading anywhere; a newton meter measures weight and would read differently on the Moon.
:::

## Newton's laws of motion

Isaac Newton gathered the whole subject into three statements. You need the exam wording of each, and you need to be able to apply it.

### The first law

:::def Newton's first law
A body remains at rest, or continues to move with constant velocity, unless acted on by a resultant force.
:::

Constant velocity means constant speed **and** constant direction. A hockey puck on ice keeps sliding because almost no force acts on it, and a spacecraft far from every planet needs no engine to keep moving. The idea that "a force is needed to keep something moving" is a misconception: a force is needed to **change** the motion. On Earth, things stop because friction and air resistance are forces. If the forces on a body are balanced, the resultant is zero, and the body either stays at rest or moves at constant velocity.

### The second law

:::def Newton's second law
The rate of change of momentum of a body is proportional to the resultant force acting on it and takes place in the direction of the force.
:::

We make this precise in the next section, once momentum has been defined. For an object of constant mass it gives the equation you have met before:

:::formula Newton's second law (constant mass)
\[F = ma\]
\(F\): **resultant** force (N) · \(m\): mass (kg) · \(a\): acceleration (\(\mathrm{m\,s^{-2}}\)). The acceleration is always in the same direction as the resultant force.
:::

This is how the newton is defined: one newton is the resultant force that gives a mass of \(1\,\mathrm{kg}\) an acceleration of \(1\,\mathrm{m\,s^{-2}}\), so \(1\,\mathrm{N} = 1\,\mathrm{kg\,m\,s^{-2}}\). The words "resultant" and "same direction" matter. If a skater is moving to the right and a force pushes to the left, the skater slows down: the acceleration points to the left, along with the force, even though the velocity points to the right.

### The third law

:::def Newton's third law
If body A exerts a force on body B, then body B exerts a force on body A that is equal in magnitude and opposite in direction. The two forces are of the same type.
:::

Forces always come in **pairs** like this. When you push on a wall, the wall pushes back on you with an equal force. When the Earth pulls an apple down, the apple pulls the Earth up with an equal force (the Earth's acceleration is far too small to notice, because its mass is so large). Every pair has three features that identify it:

- the two forces act on **different bodies**, A and B;
- they are the **same type** of force (both gravitational, or both contact, or both electric);
- they are **equal in magnitude** and **opposite in direction**, at every moment.

:::html
<figure class="fig"><svg viewBox="0 0 600 225" role="img" aria-label="Two free-body diagrams. Left: a book with an upward normal contact force N and a downward weight W of equal length. Right: a car with a long forward driving force, a shorter backward drag force, and equal upward normal contact force and downward weight."><rect class="f1 s-acc sw2" x="90" y="95" width="100" height="50"/><circle class="fi" cx="140" cy="120" r="3.5"/><path class="c1" d="M140 120V30" marker-end="url(#ah-phys)"/><path class="c1" d="M140 120V210" marker-end="url(#ah-phys)"/><text class="tl" x="150" y="46">N</text><text class="tl" x="150" y="204">W = mg</text><text class="tl tc" x="140" y="16">book on a table</text><rect class="f1 s-acc sw2" x="410" y="100" width="60" height="40" rx="6"/><circle class="fp s-ink sw2" cx="424" cy="146" r="9"/><circle class="fp s-ink sw2" cx="456" cy="146" r="9"/><circle class="fi" cx="440" cy="120" r="3.5"/><path class="c1" d="M440 120H570" marker-end="url(#ah-phys)"/><path class="c2" d="M440 120H392" marker-end="url(#ah2-phys)"/><path class="c1" d="M440 120V50" marker-end="url(#ah-phys)"/><path class="c1" d="M440 120V190" marker-end="url(#ah-phys)"/><text class="tl" x="478" y="108">driving force</text><text class="tl" x="478" y="140">3.0 kN</text><text class="tl tc ta2" x="372" y="108">drag</text><text class="tl tc ta2" x="372" y="140">1.2 kN</text><text class="tl" x="450" y="62">N</text><text class="tl" x="450" y="200">W</text><text class="tl tc" x="440" y="16">car on a level road</text></svg><figcaption>Free-body diagrams draw only the forces acting on one body, each from the point where it acts. The book is in equilibrium, so N and W are equal. The car has a resultant force of 1.8 kN forwards, so it accelerates forwards. The vertical forces on the car are drawn to a different scale from the horizontal ones.</figcaption></figure>
:::

:::warn The most common third-law mistake
The weight of a book on a table and the upward contact force of the table on the book are equal and opposite, but they are **not** a third-law pair. Both act on the same body (the book) and they are different types (gravitational and contact). The true pairs are: the Earth pulls the book down and the book pulls the Earth up (both gravitational); the table pushes the book up and the book pushes the table down (both contact). The reason the book does not accelerate is that the **first law** applies to the forces on it: they are balanced.
:::

:::eg A horse pulls a cart forwards. The cart pulls back on the horse with an equal force (third law). Explain how the horse and cart can accelerate.
The two forces of the third-law pair act on **different** bodies, so they never cancel each other. [B1]

Consider the cart: the forward pull of the horse is larger than the backward resistive forces on the cart, so the cart has a resultant force forwards and accelerates. [B1]

Consider the horse: the force of the ground pushing forwards on its hooves is larger than the backward pull of the cart, so the horse also has a resultant force forwards. [B1]

To analyse acceleration always choose **one body** and add up the forces on that body only.
:::

## Momentum and force

An object's tendency to keep going depends on its mass and also on its velocity. A cyclist and a lorry both travelling at \(10\,\mathrm{m\,s^{-1}}\) are very different to stop. Physicists combine the two quantities.

:::def Linear momentum
The product of mass and velocity.
:::

:::formula Momentum
\[p = mv\]
\(p\): momentum (\(\mathrm{kg\,m\,s^{-1}}\), which is the same as N s) · \(m\): mass (kg) · \(v\): velocity (\(\mathrm{m\,s^{-1}}\)). Momentum is a **vector**: it has the direction of the velocity, so its sign matters.
:::

A \(1200\,\mathrm{kg}\) car moving at \(25\,\mathrm{m\,s^{-1}}\) has momentum \(1200 \times 25 = 3.0 \times 10^{4}\,\mathrm{kg\,m\,s^{-1}}\). A change of velocity is a change of momentum, and it takes a force to do it.

:::def Force
The rate of change of momentum. (For a resultant force, the momentum changes in the direction of that force.)
:::

:::formula Force and momentum
\[F = \frac{\Delta p}{\Delta t} = \frac{\Delta (mv)}{\Delta t}\]
\(F\): resultant force (N) · \(\Delta p\): change of momentum (\(\mathrm{kg\,m\,s^{-1}}\)) · \(\Delta t\): time over which it changes (s).
:::

This is Newton's second law with the proportionality constant chosen to be 1 (that is what defining the newton as \(1\,\mathrm{kg\,m\,s^{-2}}\) does). It is more general than \(F = ma\), because it also works when the mass changes, as for a rocket burning fuel or sand falling onto a conveyor belt.

:::proof Why F = ma is the special case of constant mass
Start with \(F = \dfrac{\Delta(mv)}{\Delta t}\).
If the mass \(m\) is constant, it can be taken outside the change: \(\Delta(mv) = m\,\Delta v\).
So \(F = \dfrac{m\,\Delta v}{\Delta t} = m\,\dfrac{\Delta v}{\Delta t}\).
But \(\dfrac{\Delta v}{\Delta t}\) is the acceleration \(a\), so \(F = ma\).
The units agree: \(\mathrm{kg\,m\,s^{-1}}\) divided by \(\mathrm{s}\) is \(\mathrm{kg\,m\,s^{-2}} = \mathrm{N}\).
:::

### Impulse and the force–time graph

Rearranging \(F = \Delta p/\Delta t\) gives \(F\,\Delta t = \Delta p\). The product of force and the time for which it acts is called the **impulse**, and it equals the change of momentum. Cambridge only states force as rate of change of momentum, but impulse is a quick way to think. If the force changes during the contact, the impulse is the **area under the force–time graph**, and the average force is that area divided by the time.

:::html
<figure class="fig small"><svg viewBox="20 4 372 228" role="img" aria-label="Force against time graph for a football kick: the force rises in a straight line from zero to 1200 newtons at 7.5 milliseconds and falls back to zero at 15 milliseconds. The triangle under the graph is shaded."><path class="f1" d="M60 190L210 50L360 190Z"/><path class="ax" d="M60 25V190H380"/><path class="ln" d="M60 190L210 50L360 190"/><path class="gr dash thin" d="M60 50H210V190"/><text class="ts te" x="54" y="54">1200</text><text class="ts tc" x="210" y="206">7.5</text><text class="ts tc" x="360" y="206">15</text><text class="ts tc" x="60" y="206">0</text><text class="tl tc" x="220" y="222">t / ms</text><text class="tl" x="66" y="20">F / N</text><text class="tl tc" x="210" y="150">area = impulse = 9.0 N s</text></svg><figcaption>The force on a football during a kick. The shaded area is the impulse, which equals the change of momentum of the ball.</figcaption></figure>
:::

:::eg A 0.43 kg football is kicked from rest. The force from the boot rises steadily from zero to 1200 N in 7.5 ms and falls steadily back to zero in a further 7.5 ms, as in the graph. Find the speed of the ball as it leaves the boot.
The impulse is the area of the triangle: \(\tfrac12 \times \text{base} \times \text{height} = \tfrac12 \times 0.0150 \times 1200 = 9.0\,\mathrm{N\,s}\). [C1]

This equals the change of momentum, and the ball started from rest: \(mv = 9.0\). [M1]

\[v = \frac{9.0}{0.43} = 21\,\mathrm{m\,s^{-1}}\] [A1]
The area was found in seconds. Converting 15 ms to \(0.0150\,\mathrm{s}\) is the step that students forget.
:::

### Changing momentum safely

To bring a body to rest you must remove its momentum. The impulse needed is fixed by its mass and speed, so the only way to reduce the force is to **increase the time**.

:::eg A car of mass 1100 kg travelling at \(14\,\mathrm{m\,s^{-1}}\) hits a wall and stops. Find the average force on the car if it stops in 0.030 s (a rigid car), and in 0.15 s (with crumple zones).
The change of momentum has the same size in both cases: \(\Delta p = 1100 \times 14 = 1.54 \times 10^{4}\,\mathrm{kg\,m\,s^{-1}}\). [C1]

Rigid car: \(F = \dfrac{\Delta p}{\Delta t} = \dfrac{15400}{0.030} = 5.1 \times 10^{5}\,\mathrm{N}\). [A1]

With crumple zones: \(F = \dfrac{15400}{0.15} = 1.0 \times 10^{5}\,\mathrm{N}\). [A1]

Five times the stopping time gives one fifth of the force. This is why crumple zones collapse, airbags inflate and gymnasts bend their knees when they land: each makes the same change of momentum take longer.
:::

The same idea explains why a cricketer draws the hands back while catching a fast ball. A ball bouncing off a wall is a harder case, because the momentum reverses.

:::eg A 0.15 kg ball hits a wall at \(20\,\mathrm{m\,s^{-1}}\) and rebounds along the same line at \(15\,\mathrm{m\,s^{-1}}\). The contact lasts 0.010 s. Find the average force on the ball.
Choose a direction: take the direction **towards** the wall as positive. Then the initial velocity is \(+20\,\mathrm{m\,s^{-1}}\) and the final velocity is \(-15\,\mathrm{m\,s^{-1}}\). [B1]

\[\Delta p = m(v - u) = 0.15 \times (-15 - 20) = -5.25\,\mathrm{kg\,m\,s^{-1}}\] [C1]

\[F = \frac{\Delta p}{\Delta t} = \frac{-5.25}{0.010} = -525\,\mathrm{N}\] [A1]
The force on the ball is \(525\,\mathrm{N}\) **away from the wall**, because the negative sign points away from the wall. By the third law the ball pushes on the wall with \(525\,\mathrm{N}\) towards the wall.
:::

The size of the change of momentum is \(0.15 \times 20 + 0.15 \times 15\): the ball has to be stopped **and** sent back, so the two momenta add. Subtracting them (a change of \(0.75\,\mathrm{N\,s}\)) is the classic mistake, and one of the spot-the-error questions below.

### Mass flow

If a stream of fluid or grains is stopped, the momentum removed each second is the mass arriving each second multiplied by its velocity.

:::formula Force from a flow of mass
\[F = \frac{\Delta m}{\Delta t}\,v\]
\(\Delta m/\Delta t\): mass arriving per second (\(\mathrm{kg\,s^{-1}}\)) · \(v\): the change of velocity of that mass (\(\mathrm{m\,s^{-1}}\)), here from \(v\) to zero.
:::

:::eg Water leaves a hose at a steady \(2.0\,\mathrm{kg\,s^{-1}}\) with speed \(12\,\mathrm{m\,s^{-1}}\) and hits a wall, running down it with no sideways speed. Find the force of the water on the wall.
Each second \(2.0\,\mathrm{kg}\) of water loses its momentum of \(2.0 \times 12 = 24\,\mathrm{kg\,m\,s^{-1}}\). [C1]

The force on the water is \(24\,\mathrm{N}\), and by the third law the water pushes on the wall with \(24\,\mathrm{N}\). [A1]

A rocket works the same way in reverse. It throws exhaust backwards at a high speed, so the exhaust gains momentum backwards and the rocket gains momentum forwards: the thrust is the mass of exhaust expelled per second multiplied by its speed relative to the rocket.
:::

## Solving problems with F = ma

Almost every dynamics problem follows the same recipe.

:::steps
1. Draw a **free-body diagram** of the object: a dot or box with an arrow for every force that acts **on it** (weight, contact force, driving force, friction, drag, tension). Label each.
2. Choose a positive direction, normally the direction of the acceleration if you know it.
3. Add the forces in that direction to get the **resultant** force. Forces against the positive direction count as negative.
4. Apply \(F = ma\) (resultant force, not just one force) and solve for the unknown.
:::

:::eg A car of mass 1200 kg has a driving force of 3.0 kN and a total resistive force of 1.2 kN. Find its acceleration. What is its acceleration when the resistive force has risen to 3.0 kN?
The resultant force is \(3000 - 1200 = 1800\,\mathrm{N}\) forwards. [C1]

\[a = \frac{F}{m} = \frac{1800}{1200} = 1.5\,\mathrm{m\,s^{-2}}\] [A1]
When the resistive force reaches \(3.0\,\mathrm{kN}\), the resultant force is zero, so \(a = 0\): the car continues at a constant velocity (first law). [B1]
:::

### Connected bodies

When two objects are linked by a tow bar or string, they have the **same acceleration** (if the link does not stretch). Treat the pair as one body to find the acceleration, then treat one of them alone to find the force between them.

:::eg A car of mass 1000 kg tows a trailer of mass 300 kg along a level road. The driving force on the car is 3900 N. The resistive forces are 500 N on the car and 200 N on the trailer. Find the acceleration and the tension in the tow bar.
Treat the car and trailer together: mass \(1300\,\mathrm{kg}\), resultant force \(3900 - 500 - 200 = 3200\,\mathrm{N}\). [C1]
\[a = \frac{3200}{1300} = 2.46\,\mathrm{m\,s^{-2}}\] [A1]
Now the trailer alone. The tow bar pulls it forwards with tension \(T\), and the resistive force pulls back with \(200\,\mathrm{N}\):
\[T - 200 = 300 \times 2.46\ldots \quad\Rightarrow\quad T = 938\,\mathrm{N}\] [A1]
**Check** with the car alone: \(3900 - 500 - T = 1000 \times 2.46\ldots\) gives \(T = 938\,\mathrm{N}\) again.
:::

### Lifts and apparent weight

When you stand on scales, the reading shows the **normal contact force** \(R\) from the scales on you, not your weight. In a lift these two differ whenever the lift accelerates.

:::eg A 60 kg person stands on scales in a lift that accelerates upwards at \(1.5\,\mathrm{m\,s^{-2}}\). What do the scales read? What would they read if the lift accelerated downwards at the same rate?
Take upwards as positive. The scales push up with \(R\); the weight is \(mg = 60 \times 9.81\) downwards. The resultant force is \(R - mg\), and it equals \(ma\):
\[R - 60 \times 9.81 = 60 \times 1.5 \quad\Rightarrow\quad R = 60 \times (9.81 + 1.5) = 679\,\mathrm{N}\] [A1]
Accelerating downwards, the acceleration is \(-1.5\,\mathrm{m\,s^{-2}}\): \(R = 60 \times (9.81 - 1.5) = 499\,\mathrm{N}\). [A1]

The reading is larger than the true weight (\(589\,\mathrm{N}\)) when the lift accelerates **upwards** and smaller when it accelerates **downwards**. A lift moving at constant velocity, up or down, gives \(R = mg\) exactly. If the cable broke and the lift fell freely, \(R\) would be zero: the person would feel weightless.
:::

### Objects on slopes

On a slope the weight is not along the line of motion. Resolve it into a component **along** the slope and one **perpendicular** to it. For a slope at angle \(\theta\) to the horizontal, the weight \(mg\) has:

- a component \(mg\sin\theta\) acting **down the slope**;
- a component \(mg\cos\theta\) acting **into the slope**, balanced by the normal contact force: \(N = mg\cos\theta\).

:::html
<figure class="fig"><svg viewBox="0 0 600 240" role="img" aria-label="Left: a block on a slope at angle theta. Right: its free-body diagram with weight W vertically down, normal contact force N perpendicular to the slope, friction f up the slope, and the two components of the weight drawn dashed, mg sin theta down the slope and mg cos theta into the slope."><path class="fm" d="M30 215L330 215L330 42Z"/><path class="ln" d="M30 215L330 215L330 42Z"/><rect class="f1 s-acc sw2" x="143" y="96" width="50" height="36" transform="rotate(-30 168.2 114.4)"/><path class="ln thin" d="M64.6 195A40 40 0 0 0 70 215"/><text class="tl" x="78" y="211">θ</text><circle class="fi" cx="470" cy="110" r="3.5"/><path class="c1" d="M470 110V210" marker-end="url(#ah-phys)"/><path class="c1" d="M470 110L426.7 35" marker-end="url(#ah-phys)"/><path class="c3" d="M470 110L504.6 90" marker-end="url(#ahr)"/><path class="c2 dash" d="M470 110L426.7 135" marker-end="url(#ah2-phys)"/><path class="c2 dash" d="M470 110L513.3 185" marker-end="url(#ah2-phys)"/><text class="tl" x="476" y="206">W</text><text class="tl te" x="420" y="40">N</text><text class="tl" x="510" y="88">f</text><text class="tl te" x="420" y="146">mg sin θ</text><text class="tl" x="520" y="190">mg cos θ</text></svg><figcaption>A block on a rough slope (left) and its free-body diagram (right). The weight W is the sum of its two dashed components. Along the slope, the resultant force is mg sin θ − f.</figcaption></figure>
:::

:::eg A 5.0 kg block is released on a slope at \(30^\circ\) to the horizontal. A frictional force of 8.0 N acts up the slope. Find the acceleration down the slope and the normal contact force.
Component of the weight down the slope: \(mg\sin\theta = 5.0 \times 9.81 \times \sin 30^\circ = 24.5\,\mathrm{N}\). [C1]

Resultant force down the slope: \(24.5 - 8.0 = 16.5\,\mathrm{N}\), so \(a = \dfrac{16.5}{5.0} = 3.3\,\mathrm{m\,s^{-2}}\). [A1]

Perpendicular to the slope there is no acceleration, so \(N = mg\cos\theta = 5.0 \times 9.81 \times \cos 30^\circ = 42.5\,\mathrm{N}\). [A1]

Without friction the acceleration would be \(g\sin\theta = 4.9\,\mathrm{m\,s^{-2}}\), whatever the mass. The mass cancels, just as it does in free fall.
:::

## Resistive forces and terminal velocity

When one surface slides over another, **friction** acts on each surface in the direction that opposes the relative motion. Friction depends on the two surfaces and how hard they are pressed together (the syllabus does not ask for coefficients of friction). Friction can also act with no motion at all: a parked car on a hill is held by static friction. When an object moves through a fluid (a gas or a liquid), the fluid exerts a **drag** (or viscous) force on it, which opposes the motion. Air resistance is drag in air.

The simple model you need is that **drag increases as speed increases**. At zero speed there is no drag at all. Drag also depends on the shape of the object and on the fluid.

### A falling object with air resistance

Without air resistance, every object near the Earth falls with the same acceleration \(g\), whatever its mass. A heavier object does not fall faster in a vacuum: although its weight is bigger, so is its mass, and the ratio \(W/m = g\) stays the same. In air, the story changes:

:::html
<figure class="fig"><svg viewBox="0 0 600 220" role="img" aria-label="Three free-body diagrams of a skydiver. Just after leaving the aircraft only a long downward weight acts. Later a medium upward drag acts against the same weight. At terminal velocity the upward drag is as long as the weight."><circle class="f1 s-acc sw2" cx="100" cy="90" r="12"/><circle class="fi" cx="100" cy="90" r="3.5"/><path class="c1" d="M100 90V170" marker-end="url(#ah-phys)"/><text class="tl" x="110" y="164">W</text><text class="tl tc" x="100" y="22">just after jumping</text><text class="tl tc" x="100" y="200">a = g</text><circle class="f1 s-acc sw2" cx="300" cy="90" r="12"/><circle class="fi" cx="300" cy="90" r="3.5"/><path class="c1" d="M300 90V170" marker-end="url(#ah-phys)"/><path class="c2" d="M300 90V45" marker-end="url(#ah2-phys)"/><text class="tl" x="310" y="164">W</text><text class="tl" x="310" y="56">drag</text><text class="tl tc" x="300" y="22">speeding up</text><text class="tl tc" x="300" y="200">a smaller than g</text><circle class="f1 s-acc sw2" cx="500" cy="90" r="12"/><circle class="fi" cx="500" cy="90" r="3.5"/><path class="c1" d="M500 90V170" marker-end="url(#ah-phys)"/><path class="c2" d="M500 90V10" marker-end="url(#ah2-phys)"/><text class="tl" x="510" y="164">W</text><text class="tl" x="510" y="44">drag</text><text class="tl tc" x="500" y="200">terminal velocity, a = 0</text></svg><figcaption>As a skydiver speeds up, the upward drag grows while the weight stays the same. The resultant force shrinks until the two are equal.</figcaption></figure>
:::

:::steps
1. Just after leaving the aircraft the speed is almost zero, so the drag is almost zero. The resultant force is the weight, so \(a = g\).
2. As the speed increases, the drag increases. The resultant force \(W - \text{drag}\) decreases, so the acceleration decreases. The speed is still increasing, but more slowly.
3. At a certain speed the drag equals the weight. The resultant force is zero, so the acceleration is zero and the speed stops changing.
:::

:::def Terminal velocity
The constant velocity reached by an object moving against a resistive force, when the resistive force equals the driving force (for a falling object, its weight), so that the resultant force is zero.
:::

Terminal velocity is not "zero force" and it is not "zero acceleration because the object has stopped". Several forces still act: they are balanced. The same thing happens in other situations. A car at its top speed has a driving force from the engine equal to the total drag; a steel ball bearing dropped into a tall jar of oil quickly reaches a steady speed when the viscous drag plus the upthrust equal its weight.

:::eg An 80 kg skydiver falls from rest. Find the acceleration (a) at the moment of leaving the aircraft, (b) when the drag is 500 N, (c) when the drag equals the skydiver's weight. What is the drag then?
(a) The speed is zero, so there is no drag. \(a = g = 9.81\,\mathrm{m\,s^{-2}}\). [B1]

(b) Weight \(= 80 \times 9.81 = 784.8\,\mathrm{N}\). Resultant \(= 784.8 - 500 = 284.8\,\mathrm{N}\) downwards. [C1] \(a = 284.8/80 = 3.56\,\mathrm{m\,s^{-2}}\). [A1]

(c) The resultant force is zero, so \(a = 0\) and the velocity is terminal. The drag is \(785\,\mathrm{N}\). [A1]
:::

### The velocity–time graph of a skydiver

The velocity–time graph tells the whole story. The gradient is the acceleration, so it starts as steep as \(g\) and flattens.

:::html
<figure class="fig wide"><svg viewBox="0 0 600 290" role="img" aria-label="Velocity against time for a skydiver. The curve rises with gradient g at the start, flattens to a terminal velocity of 55 metres per second, drops sharply when the parachute opens at 30 seconds to a lower constant velocity of 5 metres per second, then falls to zero on landing."><path class="ax" d="M60 25V250H570"/><path class="gr dash thin" d="M60 250L106.7 48.3"/><path class="gr dash thin" d="M60 48.3H310"/><path class="gr dash thin" d="M310 48.3V250"/><path class="c1" d="M60 250L77 189L93 147L110 117L127 97L143 82L168 68L193 60L227 54L268 51L310 49"/><path class="c1" d="M310 49L314 121L318 165L322 191L327 207L335 223L343 228L352 230L518 232V250"/><text class="ts te" x="54" y="254">0</text><text class="ts te" x="54" y="52">55</text><text class="ts te" x="54" y="236">5</text><text class="ts tc" x="310" y="266">30</text><text class="ts tc" x="518" y="266">55</text><text class="tl tc" x="320" y="284">t / s</text><text class="tl" x="66" y="20">v / m s⁻¹</text><text class="tl" x="92" y="200">1: gradient = g</text><text class="tl tc" x="190" y="40">2: terminal velocity</text><text class="tl" x="322" y="110">3: parachute opens</text><text class="tl" x="360" y="212">4: new, lower terminal velocity</text><text class="tl te" x="566" y="244">5: lands</text></svg><figcaption>A skydiver's velocity–time graph (the numbers are typical, not exact). The dashed line shows the initial gradient g and where it meets the first terminal velocity. Opening the parachute suddenly increases the drag far above the weight.</figcaption></figure>
:::

:::exam Describing and explaining a v–t graph
Marks are given for linking each part of the graph to the forces. Use this pattern for each stage: **what the graph does**, **what the resultant force is**, **why**. For stage 3: the speed decreases rapidly because the drag suddenly increases and becomes **much larger than the weight**, so the resultant force is **upwards** and the acceleration is upwards (a deceleration). As the speed falls, the drag falls, until it again equals the weight at the new, lower terminal velocity.
:::

:::eg Explain the motion of the skydiver from the moment the parachute opens until she lands. The skydiver (with equipment) has mass 80 kg and was falling at the first terminal velocity.
Opening the parachute greatly increases the area exposed to the air, so the drag suddenly becomes much larger than the weight of 785 N. [B1] Suppose the drag is \(3000\,\mathrm{N}\) just after opening. The resultant force is \(3000 - 784.8 = 2215\,\mathrm{N}\) **upwards**, so \(a = 2215/80 = 27.7\,\mathrm{m\,s^{-2}}\) upwards. [A1]

The skydiver slows down, so the drag decreases. [B1] When the drag has fallen to equal the weight again (785 N), the resultant force is zero and the skydiver falls at a new, lower constant (terminal) velocity until landing. [B1]
:::

## Conservation of momentum

Newton's third law has a powerful consequence. When two bodies interact, each exerts an equal and opposite force on the other for the same time, so the momentum one gains is exactly the momentum the other loses (\(F\Delta t\) is the same size for both). The total never changes.

:::def Principle of conservation of momentum
The total momentum of a system of interacting bodies remains constant, provided no resultant external force acts on the system.
:::

A **system** is the set of bodies you choose to include. An **external** force is one from outside that system, such as friction with the floor. For a short collision, external forces are usually small compared with the large forces between the colliding bodies, so we treat momentum as conserved.

:::steps
1. Choose a positive direction (usually the direction of the first body's velocity). Any velocity in the opposite direction is negative.
2. Write the **total momentum before**: \(m_1u_1 + m_2u_2\).
3. Write the **total momentum after**: \(m_1v_1 + m_2v_2\) (or \((m_1 + m_2)v\) if they stick).
4. Set them equal and solve. Then check the sign of the answer to find the direction.
:::

:::formula Conservation of momentum (two bodies, one dimension)
\[m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2\]
\(m_1, m_2\): masses (kg) · \(u_1, u_2\): velocities before (\(\mathrm{m\,s^{-1}}\)) · \(v_1, v_2\): velocities after. Directions matter: use + and − signs.
:::

### Elastic and inelastic collisions

Momentum is conserved in **every** collision (and explosion) in an isolated system. Kinetic energy is a different story.

:::def Elastic collision
A collision in which the total kinetic energy is conserved. In an **inelastic** collision the total kinetic energy is not conserved: some of it is transferred to other forms, such as thermal energy, sound and deformation of the bodies.
:::

In a **perfectly inelastic** collision, the bodies stick together and move with a common velocity. This loses the largest possible amount of kinetic energy for the given momentum. For an elastic collision there is a second useful rule, which gives a second equation without any squares.

:::key Elastic collision in one dimension
Total kinetic energy before = total kinetic energy after, **and**

\[\text{relative speed of approach} = \text{relative speed of separation}\]
\[u_1 - u_2 = v_2 - v_1\]
Use momentum together with this relative-speed equation: two linear equations are much easier than momentum together with a quadratic kinetic-energy equation.
:::

:::proof Why the relative speeds are equal in an elastic collision
Let body 1 have mass \(m_1\) and body 2 have \(m_2\), moving in one line. Conservation of momentum: \(m_1(u_1 - v_1) = m_2(v_2 - u_2)\).   (1)
Conservation of kinetic energy: \(\tfrac12 m_1(u_1^2 - v_1^2) = \tfrac12 m_2(v_2^2 - u_2^2)\), so \(m_1(u_1 - v_1)(u_1 + v_1) = m_2(v_2 - u_2)(v_2 + u_2)\).   (2)
Divide (2) by (1). The common factors cancel (they are non-zero if there was a collision): \(u_1 + v_1 = v_2 + u_2\).
Rearrange: \(u_1 - u_2 = v_2 - v_1\), which is the speed of approach equal to the speed of separation.
:::

:::eg A 2.0 kg trolley moving at \(3.0\,\mathrm{m\,s^{-1}}\) to the right collides with a stationary 1.0 kg trolley. Find the velocities afterwards (a) if the trolleys stick together, (b) if the collision is elastic. In each case find the kinetic energy lost.
Kinetic energy before: \(\tfrac12 \times 2.0 \times 3.0^2 = 9.0\,\mathrm{J}\). Momentum before: \(2.0 \times 3.0 = 6.0\,\mathrm{kg\,m\,s^{-1}}\).

(a) Stick together: \((2.0 + 1.0)v = 6.0\), so \(v = 2.0\,\mathrm{m\,s^{-1}}\) to the right. [A1] Kinetic energy after: \(\tfrac12 \times 3.0 \times 2.0^2 = 6.0\,\mathrm{J}\), so \(3.0\,\mathrm{J}\) is lost, which is \(33\%\) of the original. [A1]

(b) Elastic: use momentum and relative speeds.
\[2.0v_1 + 1.0v_2 = 6.0 \qquad v_2 - v_1 = 3.0 - 0 = 3.0\] [M1]
Substitute \(v_2 = v_1 + 3.0\): \(2.0v_1 + v_1 + 3.0 = 6.0\), so \(v_1 = 1.0\,\mathrm{m\,s^{-1}}\) and \(v_2 = 4.0\,\mathrm{m\,s^{-1}}\), both to the right. [A1]

**Check** the kinetic energy: \(\tfrac12 \times 2.0 \times 1.0^2 + \tfrac12 \times 1.0 \times 4.0^2 = 1.0 + 8.0 = 9.0\,\mathrm{J}\). Nothing is lost. [A1]
:::

The lost energy in case (a) went into thermal energy, sound and bending the trolleys' bumpers: no momentum went anywhere. Try these two collisions in the widget below, and then change the masses. Notice what happens when the trolleys have equal masses in the elastic case, and what happens when a light trolley hits a heavy one.

:::html
<div class="widget" data-w="phys-collide" data-m1="2" data-m2="1" data-u1="3" data-u2="0" data-type="elastic"></div>
:::

:::eg A 3.0 kg trolley moving at \(2.0\,\mathrm{m\,s^{-1}}\) to the right meets a 1.0 kg trolley moving at \(4.0\,\mathrm{m\,s^{-1}}\) to the left. They stick together. Find their common velocity and the kinetic energy lost.
Take right as positive, so the second trolley's velocity is \(-4.0\,\mathrm{m\,s^{-1}}\). [B1]

\[3.0 \times 2.0 + 1.0 \times (-4.0) = (3.0 + 1.0)v\] [C1]
\(6.0 - 4.0 = 4.0v\), so \(v = +0.50\,\mathrm{m\,s^{-1}}\): they move slowly to the right. [A1]

Kinetic energy before: \(\tfrac12 \times 3.0 \times 2.0^2 + \tfrac12 \times 1.0 \times 4.0^2 = 6.0 + 8.0 = 14\,\mathrm{J}\). After: \(\tfrac12 \times 4.0 \times 0.50^2 = 0.50\,\mathrm{J}\). Lost: \(13.5\,\mathrm{J}\). [A1]

Almost all the kinetic energy has gone, because the two momenta nearly cancel.
:::

:::eg Two ice skaters of masses 60 kg and 40 kg stand together at rest and push each other apart. The 40 kg skater moves off at \(3.0\,\mathrm{m\,s^{-1}}\). Find the velocity of the other skater.
The total momentum before is zero. Take the 40 kg skater's direction as positive: [B1]
\[0 = 40 \times 3.0 + 60 \times v\] [C1]
so \(v = -2.0\,\mathrm{m\,s^{-1}}\): the 60 kg skater moves at \(2.0\,\mathrm{m\,s^{-1}}\) in the opposite direction. [A1]

The smaller mass gets the larger speed. Total momentum is still zero (+120 and −120), while the kinetic energy has increased from nothing: the skaters' muscles have supplied it.
:::

### Explosions and recoil

An explosion is a collision played backwards: one body breaks into two (or two bodies are pushed apart by a spring), and the initial momentum is often zero. Then the two parts must have **equal and opposite momenta**.

:::eg A rifle of mass 4.0 kg fires a bullet of mass 10 g at \(400\,\mathrm{m\,s^{-1}}\). Find the recoil speed of the rifle, and compare the kinetic energies.
Mass of bullet: \(10\,\mathrm{g} = 0.010\,\mathrm{kg}\). The rifle and bullet were at rest, so the total momentum is zero. [B1]
\[0 = 0.010 \times 400 + 4.0 \times v \quad\Rightarrow\quad v = -1.0\,\mathrm{m\,s^{-1}}\] [C1]
The rifle recoils at \(1.0\,\mathrm{m\,s^{-1}}\) in the opposite direction to the bullet. [A1]

Kinetic energy of the bullet: \(\tfrac12 \times 0.010 \times 400^2 = 800\,\mathrm{J}\). Kinetic energy of the rifle: \(\tfrac12 \times 4.0 \times 1.0^2 = 2.0\,\mathrm{J}\).

The same momentum gives very different energies: for a given momentum \(p\), the kinetic energy is \(p^2/2m\), so the light body takes almost all of it. This is why a recoiling gun is not dangerous, and a bullet is.
:::

### Collisions in two dimensions

Momentum is a vector, so it is conserved **in every direction separately**. For a collision in a plane, choose two perpendicular axes (usually along the original motion, and at right angles to it). Resolve every velocity into components with \(v\cos\theta\) and \(v\sin\theta\), and write one conservation equation for each axis. Alternatively, draw a **vector triangle** of the momenta: the momentum vectors before and after must form a closed triangle.

:::html
<figure class="fig"><svg viewBox="30 45 555 200" role="img" aria-label="Before: a ball moving right at 2.0 metres per second towards a stationary ball of equal mass. After: the first ball moves off at 30 degrees above the original line at 1.73 metres per second, and the second ball at 60 degrees below the line at 1.00 metre per second."><path class="ln-m dash thin" d="M40 130H480"/><path class="gr dash thin" d="M255 60V230"/><circle class="f1 s-acc sw2" cx="60" cy="130" r="14"/><path class="c1" d="M78 130H158" marker-end="url(#ah-phys)"/><text class="tl tc" x="118" y="118">u = 2.0 m s⁻¹</text><circle class="f2 s-acc2 sw2" cx="210" cy="130" r="14"/><text class="tl tc" x="135" y="178">before</text><path class="ln-m thin dash" d="M330 130L382 100M330 130L360 182"/><circle class="f1 s-acc sw2" cx="382" cy="100" r="14"/><circle class="f2 s-acc2 sw2" cx="360" cy="182" r="14"/><path class="c1" d="M394.1 93L454.7 58" marker-end="url(#ah-phys)"/><path class="c2" d="M367 194.1L387 228.7" marker-end="url(#ah2-phys)"/><text class="tl" x="460" y="62">v₁ = 1.73 m s⁻¹</text><text class="tl" x="394" y="230">v₂ = 1.00 m s⁻¹</text><path class="ln thin" d="M360 130A30 30 0 0 0 356 115"/><text class="tl" x="364" y="127">30°</text><path class="ln thin" d="M352 130A22 22 0 0 1 341 149.1"/><text class="tl" x="360" y="149">60°</text><text class="tl tc" x="300" y="215">after</text></svg><figcaption>A glancing collision between equal balls. Before: only the left ball moves. After: the two balls leave from the point of impact at 30° and 60° on opposite sides of the original line. Each axis gives its own conservation equation.</figcaption></figure>
:::

:::eg A 0.17 kg ball moving at \(2.0\,\mathrm{m\,s^{-1}}\) hits a stationary ball of equal mass. Afterwards the first ball moves at \(30^\circ\) above the original line and the second at \(60^\circ\) below it. Find both speeds, and show that the collision is elastic.
Take the original direction as \(x\) and upwards as \(y\). The mass \(m\) cancels in every equation.

Along \(y\) (momentum before is zero): \(0 = v_1\sin 30^\circ - v_2\sin 60^\circ\), so \(v_1 = 1.732\,v_2\). [M1]

Along \(x\): \(2.0 = v_1\cos 30^\circ + v_2\cos 60^\circ\). [M1] Substituting \(v_1 = 1.732v_2\):
\[2.0 = 1.732v_2 \times 0.866 + 0.5v_2 = 2.0\,v_2\]
so \(v_2 = 1.00\,\mathrm{m\,s^{-1}}\) and \(v_1 = 1.73\,\mathrm{m\,s^{-1}}\). [A1]

Kinetic energy before: \(\tfrac12 \times 0.17 \times 2.0^2 = 0.34\,\mathrm{J}\). After: \(\tfrac12 \times 0.17 \times (1.732^2 + 1.00^2) = \tfrac12 \times 0.17 \times 4.0 = 0.34\,\mathrm{J}\). They are equal, so the collision is elastic. [A1]

For equal-mass elastic glancing collisions the two balls always leave at 90° to each other. That is why a snooker player can predict where the cue ball goes after hitting an object ball.
:::

:::warn Momentum is conserved, kinetic energy often is not
Do not assume kinetic energy is conserved. Only a collision described as **elastic** (or one where the data prove it) conserves it. "Perfectly inelastic" means the bodies stick, but even then momentum is conserved. If you are not told, compute the kinetic energy before and after and compare.
:::

:::board
AQA and OCR use the term "impulse" explicitly (impulse = \(F\Delta t\) = change of momentum) and examine areas under force–time graphs; Cambridge states force as the rate of change of momentum, which gives the same physics. All boards: the same three Newton's laws and conservation of momentum, including collisions in two dimensions.
:::

:::eg Spot the error: a 0.15 kg ball hits a wall at \(20\,\mathrm{m\,s^{-1}}\) and rebounds at \(15\,\mathrm{m\,s^{-1}}\). The contact time is 0.010 s. Calculate the average force on the ball.
A student wrote this answer.

Line 1: \(\Delta p = mv - mu = 0.15 \times 15 - 0.15 \times 20 = -0.75\,\mathrm{N\,s}\)
Line 2: \(F = \Delta p/\Delta t = 0.75/0.010 = 75\,\mathrm{N}\)

Line 1 is the correct formula, but the student put both speeds in as positive numbers, although the ball reverses direction. **Line 1 is wrong: the rebound velocity should be \(-15\,\mathrm{m\,s^{-1}}\) if the incoming velocity is \(+20\,\mathrm{m\,s^{-1}}\).** The formula is right but the substitution is wrong, so the substitution mark and the answer mark are both lost. [C0 A0]

Correct working: \(\Delta p = 0.15 \times (-15) - 0.15 \times 20 = -5.25\,\mathrm{N\,s}\), so \(F = 5.25/0.010 = 525\,\mathrm{N}\). [A1]

Always ask: does the direction reverse? If so, the two momenta add. A ball that bounces back must be stopped and then sent away, so the force is much bigger than for a ball that is merely slowed down.
:::

:::try Start easy, finish at exam standard
Q: Calculate the weight of a football of mass \(0.45\,\mathrm{kg}\) on the Earth.
A: \(W = mg = 0.45 \times 9.81 = 4.41\,\mathrm{N}\), about \(4.4\,\mathrm{N}\).
Q: A resultant force of 1.8 kN acts on a 750 kg car. Find its acceleration.
A: \(a = F/m = 1800/750 = 2.4\,\mathrm{m\,s^{-2}}\), in the direction of the force.
Q: Find the momentum of a \(0.058\,\mathrm{kg}\) tennis ball moving at \(40\,\mathrm{m\,s^{-1}}\).
A: \(p = mv = 0.058 \times 40 = 2.32\,\mathrm{kg\,m\,s^{-1}}\), about \(2.3\,\mathrm{kg\,m\,s^{-1}}\).
Q: A jet of water of \(5.0\,\mathrm{kg\,s^{-1}}\) hits a wall at \(6.0\,\mathrm{m\,s^{-1}}\) and stops. Find the force on the wall.
A: \(F = \dfrac{\Delta m}{\Delta t}v = 5.0 \times 6.0 = 30\,\mathrm{N}\).
Q: A 0.50 kg trolley moving at \(2.0\,\mathrm{m\,s^{-1}}\) hits a stationary 1.5 kg trolley and they stick together. Find their speed.
A: \(0.50 \times 2.0 = (0.50 + 1.5)v\), so \(v = 1.0/2.0 = 0.50\,\mathrm{m\,s^{-1}}\).
Q: Explain why a hammer and a feather, released together in a vacuum, hit the ground at the same time.
A: The only force is the weight \(W = mg\). The acceleration is \(a = W/m = g\), which is the same for both whatever their mass, so they fall together.
Q: A 70 kg skydiver is falling at terminal velocity. What is the drag force on the skydiver? Explain.
A: At terminal velocity the resultant force is zero, so the drag equals the weight: \(70 \times 9.81 = 687\,\mathrm{N}\) upwards.
Q: A rocket engine expels \(250\,\mathrm{kg}\) of exhaust each second at \(2500\,\mathrm{m\,s^{-1}}\) relative to the rocket. The rocket has mass \(5.0 \times 10^{4}\,\mathrm{kg}\). Find the thrust and the initial acceleration just after take-off.
A: Thrust \(= \dfrac{\Delta m}{\Delta t}v = 250 \times 2500 = 6.25 \times 10^{5}\,\mathrm{N}\). The weight is \(5.0 \times 10^{4} \times 9.81 = 4.905 \times 10^{5}\,\mathrm{N}\). The resultant is \(1.345 \times 10^{5}\,\mathrm{N}\) upwards, so \(a = 1.345 \times 10^{5}/5.0 \times 10^{4} = 2.7\,\mathrm{m\,s^{-2}}\).
Q: A 4.0 kg bag of shopping hangs at rest from a spring balance in a lift that is accelerating downwards at \(2.0\,\mathrm{m\,s^{-2}}\). Find the balance reading.
A: Take downwards as positive: \(mg - T = ma\), so \(T = m(g - a) = 4.0 \times (9.81 - 2.0) = 31.2\,\mathrm{N}\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State Newton's third law of motion and give one example of a pair of forces.
A: If body A exerts a force on body B, body B exerts a force on A that is equal in magnitude and opposite in direction (and of the same type). [B1] Example: the Earth pulls a book down with gravity, and the book pulls the Earth up with an equal gravitational force. [B1]
Q: [3 marks] ★★ A tennis ball of mass \(0.058\,\mathrm{kg}\) hits a wall at \(30\,\mathrm{m\,s^{-1}}\) at right angles and rebounds at \(22\,\mathrm{m\,s^{-1}}\). The contact lasts 0.012 s. Calculate the average force on the ball.
A: Taking the initial direction as positive: \(\Delta p = 0.058 \times (-22 - 30)\) [C1] \(= -3.016\,\mathrm{N\,s}\). \(F = \dfrac{3.016}{0.012}\) [C1] \(= 251\,\mathrm{N}\), directed away from the wall. [A1]
Q: [4 marks] ★★ A skydiver jumps from a stationary balloon. Explain, in terms of the forces on the skydiver, why the skydiver's speed increases at first but then becomes constant.
A: At the start the only significant force is the weight, so the skydiver accelerates downwards. [B1] As the speed increases, the air resistance (drag) increases. [B1] The resultant force, weight minus drag, therefore decreases, so the acceleration decreases. [B1] When the drag equals the weight, the resultant force is zero, so there is no acceleration and the speed is constant (terminal velocity). [B1]
Q: [4 marks] ★★ A 3.0 kg block rests on a smooth horizontal table. It is joined by a light string over a smooth pulley to a 2.0 kg mass hanging freely. The system is released. Calculate the acceleration of the masses and the tension in the string.
H: Each mass has its own equation. The hanging mass has weight pulling down and tension pulling up; the block only has the tension.
A: Hanging mass: \(2.0 \times 9.81 - T = 2.0a\). Block: \(T = 3.0a\). [C1] Adding the equations: \(19.62 = 5.0a\) [C1] so \(a = 3.92\,\mathrm{m\,s^{-2}}\). [A1] \(T = 3.0 \times 3.924 = 11.8\,\mathrm{N}\). [A1]
Q: [5 marks] ★★ A trolley A of mass \(0.80\,\mathrm{kg}\) moves at \(1.5\,\mathrm{m\,s^{-1}}\) and catches up with trolley B of mass \(0.40\,\mathrm{kg}\) moving at \(0.50\,\mathrm{m\,s^{-1}}\) in the same direction. After the collision, B moves at \(1.3\,\mathrm{m\,s^{-1}}\). Calculate the velocity of A after the collision and decide whether the collision is elastic.
A: Momentum: \(0.80 \times 1.5 + 0.40 \times 0.50 = 0.80v_A + 0.40 \times 1.3\) [C1] so \(v_A = 1.10\,\mathrm{m\,s^{-1}}\). [A1] Kinetic energy before: \(\tfrac12 \times 0.80 \times 1.5^2 + \tfrac12 \times 0.40 \times 0.50^2 = 0.95\,\mathrm{J}\); after: \(\tfrac12 \times 0.80 \times 1.10^2 + \tfrac12 \times 0.40 \times 1.3^2 = 0.82\,\mathrm{J}\). [C1] The kinetic energy has decreased, [A1] so the collision is inelastic. [B1]
Q: [7 marks] ★★★ A ball of mass \(0.40\,\mathrm{kg}\) moving at \(5.0\,\mathrm{m\,s^{-1}}\) along the \(x\)-axis hits a stationary ball of mass \(0.60\,\mathrm{kg}\). After the collision the first ball moves at \(3.0\,\mathrm{m\,s^{-1}}\) at \(30^\circ\) above the \(x\)-axis. (a) Calculate the speed and direction of the second ball. (b) Show that the collision is inelastic.
H: Write one momentum equation along \(x\) and one along \(y\), each with the second ball's unknown component.
H: The speed comes from the two components by Pythagoras, and the angle from \(\tan\theta = v_y/v_x\).
A: (a) Along \(x\): \(0.40 \times 5.0 = 0.40 \times 3.0\cos 30^\circ + 0.60v_x\) [C1] so \(v_x = 1.60\,\mathrm{m\,s^{-1}}\). [A1] Along \(y\): \(0 = 0.40 \times 3.0\sin 30^\circ + 0.60v_y\) [C1] so \(v_y = -1.0\,\mathrm{m\,s^{-1}}\), that is \(1.0\,\mathrm{m\,s^{-1}}\) downwards. [A1] Speed \(= \sqrt{1.60^2 + 1.0^2} = 1.89\,\mathrm{m\,s^{-1}}\) at \(32^\circ\) below the \(x\)-axis. [A1] (b) Kinetic energy before: \(\tfrac12 \times 0.40 \times 5.0^2 = 5.0\,\mathrm{J}\). After: \(\tfrac12 \times 0.40 \times 3.0^2 + \tfrac12 \times 0.60 \times 1.89^2 = 1.8 + 1.07 = 2.87\,\mathrm{J}\). [C1] This is less than 5.0 J, so kinetic energy is not conserved and the collision is inelastic. [A1]
Q: [7 marks] (#phys.energy) ★★★ A bullet of mass \(0.010\,\mathrm{kg}\) is fired horizontally into a block of mass \(1.50\,\mathrm{kg}\) hanging from long strings (a ballistic pendulum). The bullet stays in the block, and the block swings up to a maximum height of \(0.20\,\mathrm{m}\) above its starting point. (a) Calculate the speed of the block just after the bullet has stopped inside it. (b) Calculate the speed of the bullet. (c) Calculate the percentage of the bullet's kinetic energy that is lost in the collision. (d) State why conservation of momentum cannot be used to link the speed just after the impact to the situation at the top of the swing.
H: After the impact, the kinetic energy of the block and bullet changes into gravitational potential energy: \(\tfrac12 (M + m)v^2 = (M + m)gh\).
H: Use conservation of momentum only for the collision itself, where the time is very short.
A: (a) \(\tfrac12 v^2 = gh\) so \(v = \sqrt{2 \times 9.81 \times 0.20}\) [C1] \(= 1.98\,\mathrm{m\,s^{-1}}\). [A1] (b) \(0.010u = (0.010 + 1.50) \times 1.981\) [C1] so \(u = 299\,\mathrm{m\,s^{-1}}\). [A1] (c) Kinetic energy before: \(\tfrac12 \times 0.010 \times 299^2 = 447\,\mathrm{J}\); after: \(\tfrac12 \times 1.51 \times 1.981^2 = 2.96\,\mathrm{J}\). [C1] Percentage lost \(= 99.3\%\). [A1] (d) While the block swings upwards, external forces (gravity and the tension in the strings) act on it, so the momentum is not conserved. [B1]
Q: [3 marks] ★★ A 70 kg person stands on scales in a lift that is moving upwards but slowing down, with a deceleration of \(2.0\,\mathrm{m\,s^{-2}}\). Calculate the reading on the scales.
H: Slowing down while moving upwards means the acceleration points downwards.
A: Take upwards as positive: the acceleration is \(-2.0\,\mathrm{m\,s^{-2}}\). \(R - mg = ma\) [C1] so \(R = 70 \times (9.81 - 2.0)\) [C1] \(= 547\,\mathrm{N}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Sand falls vertically from a hopper onto a horizontal conveyor belt at a steady rate of \(5.0\,\mathrm{kg\,s^{-1}}\). The belt moves at a constant speed of \(2.0\,\mathrm{m\,s^{-1}}\), and the sand is carried along without slipping. (a) Calculate the horizontal force that must be applied to the belt to keep it moving at constant speed. (b) Calculate the power needed to supply this force. (c) Calculate the rate at which the kinetic energy of the sand increases, and suggest what happens to the rest of the power.
H: Each second, \(5.0\,\mathrm{kg}\) of sand goes from zero horizontal velocity to \(2.0\,\mathrm{m\,s^{-1}}\). What momentum is that?
H: Power equals force multiplied by the speed at which the point of application moves.
A: (a) The momentum gained by the sand each second is \(5.0 \times 2.0 = 10\,\mathrm{kg\,m\,s^{-1}}\) [C1] so the horizontal force on the sand is \(10\,\mathrm{N}\), and the same force must be supplied to the belt. [A1] (b) \(P = Fv = 10 \times 2.0 = 20\,\mathrm{W}\). [A1] (c) The kinetic energy gained each second is \(\tfrac12 \times 5.0 \times 2.0^2 = 10\,\mathrm{W}\). [C1] This is half of the input power. [A1] The other 10 W is converted to thermal energy by friction as the sand speeds up while sliding on the belt. [B1]
Q: [6 marks] ★★★ A ball of mass \(M = 5.0\,\mathrm{kg}\) moving at \(4.0\,\mathrm{m\,s^{-1}}\) hits a stationary ball of mass \(m = 0.050\,\mathrm{kg}\) head-on in an elastic collision. (a) Use the relative-speed rule and conservation of momentum to find both velocities after the collision. (b) Show that a very light ball hit by a much heavier one leaves at close to twice the speed of the heavy ball, and explain how this relates to a ball bouncing off a moving surface.
H: Let the heavy ball leave at \(v_1\) and the light ball at \(v_2\). Relative speed: \(v_2 - v_1 = 4.0\).
H: When \(m \ll M\), the heavy ball is hardly slowed by the collision.
A: (a) Relative speeds: \(v_2 - v_1 = 4.0\). Momentum: \(5.0 \times 4.0 = 5.0v_1 + 0.050v_2\). [M1] Substitute \(v_2 = v_1 + 4.0\): \(20 = 5.05v_1 + 0.20\) [C1] so \(v_1 = 3.92\,\mathrm{m\,s^{-1}}\) and \(v_2 = 7.92\,\mathrm{m\,s^{-1}}\), both forwards. [A1] (b) The heavy ball loses very little speed (\(4.0 \to 3.92\)), so \(v_2 = v_1 + 4.0 \approx 4.0 + 4.0\): the light ball leaves at close to \(2 \times 4.0 = 8.0\,\mathrm{m\,s^{-1}}\). [M1] In the frame of the heavy ball, the light ball simply bounces back at the speed it arrived with; adding the heavy ball's own velocity doubles it. [A1] A ball that bounces off a surface moving towards it therefore leaves with its speed increased by twice the speed of the surface. [B1]
:::

:::quiz
? A book rests on a table. Which force forms a Newton's third law pair with the weight of the book (the pull of the Earth on the book)?
- The upward contact force of the table on the book
- The downward contact force of the book on the table
+ The pull of the book on the Earth
- The tension in the table
> A third-law pair acts on two different bodies and is the same type of force. The Earth pulls the book down, so the book pulls the Earth up, both by gravity. The table's contact force acts on the same body as the weight and is a different type of force.
? An object at terminal velocity falls through the air. Which statement is correct?
- There is no force acting on it.
- The weight is zero.
- The drag is greater than the weight.
+ The resultant force on it is zero.
> At terminal velocity the drag equals the weight, so the forces are balanced and the resultant is zero. Forces are certainly still acting, and the weight is unchanged.
? A 0.50 kg ball hits a floor at \(4.0\,\mathrm{m\,s^{-1}}\) and rebounds at \(3.0\,\mathrm{m\,s^{-1}}\). What is the size of its change of momentum?
- \(0.50\,\mathrm{kg\,m\,s^{-1}}\)
+ \(3.5\,\mathrm{kg\,m\,s^{-1}}\)
- \(7.0\,\mathrm{kg\,m\,s^{-1}}\)
- \(2.0\,\mathrm{kg\,m\,s^{-1}}\)
> The velocity reverses: \(\Delta v = 3.0 - (-4.0) = 7.0\,\mathrm{m\,s^{-1}}\), so \(\Delta p = 0.50 \times 7.0 = 3.5\). The value \(0.50\) comes from subtracting the speeds, \(7.0\) is the change of velocity with the mass forgotten, and \(2.0\) is only the momentum before the bounce.
? In an inelastic collision between two trolleys on a smooth track, which quantity is conserved?
- Kinetic energy only
- Neither momentum nor kinetic energy
+ Total momentum
- Velocity of each trolley
> Momentum is conserved in every collision when no resultant external force acts. Kinetic energy is not conserved in an inelastic collision, and the velocity of each trolley changes.
? A person stands on scales in a lift that is accelerating upwards. The scales read:
+ more than the person's weight
- less than the person's weight
- exactly the person's weight
- zero
> The scales show the contact force. For the resultant force to be upwards, the scale force must be greater than the weight. It is only zero in free fall.
? A heavy stone and a light stone are dropped together in a vacuum. Which statement is correct?
- The heavy stone hits the ground first because its weight is larger.
- The light stone hits the ground first because it has less inertia.
+ They hit the ground together because they have the same acceleration.
- The heavy stone accelerates faster because it has more momentum.
> The heavier stone has a larger weight but also a larger mass, so \(a = W/m = g\) for both. Mass and weight both grow in the same proportion.
? A skydiver at terminal velocity opens a parachute. Immediately afterwards the skydiver:
- continues at the same velocity
- speeds up, because the drag is smaller
+ slows down, because the drag now exceeds the weight
- stops instantly
> Opening the parachute raises the drag far above the weight, so the resultant force is upwards and the skydiver decelerates. The drag then falls as the speed falls until it balances the weight again.
? In an elastic collision in one dimension, the relative speed of approach is \(6.0\,\mathrm{m\,s^{-1}}\). What is the relative speed of separation?
- \(0\)
- \(3.0\,\mathrm{m\,s^{-1}}\)
+ \(6.0\,\mathrm{m\,s^{-1}}\)
- It depends on the masses.
> For an elastic collision the relative speeds of approach and separation are equal, whatever the masses. If the bodies stick, the relative speed of separation is zero, which is a perfectly inelastic collision.
:::

:::checklist What you can now do
- [ ] I can state that mass resists changes in motion, and use \(W = mg\) to find weight.
- [ ] I can use \(F = ma\) with the resultant force, including connected bodies, lifts and slopes, and give the direction of the acceleration.
- [ ] I can define linear momentum and force as the rate of change of momentum, and use them for rebounds, impacts and mass flow.
- [ ] I can state and apply each of Newton's three laws, and identify a third-law pair correctly.
- [ ] I can explain friction and drag, describe the motion of a falling object with air resistance, and explain terminal velocity.
- [ ] I can sketch and explain a skydiver's velocity–time graph.
- [ ] I can state and apply the conservation of momentum in one dimension, with correct signs, including explosions.
- [ ] I can solve collision problems in two dimensions by resolving momentum along two perpendicular axes.
- [ ] I can distinguish elastic from inelastic collisions, use the relative-speed rule, and say where the lost kinetic energy goes.
:::

:::recap
- Mass resists changes in motion (kg, no direction). Weight is the force of a gravitational field on a mass: \(W = mg\) (N).
- First law: no resultant force means constant velocity (or rest). Second law: \(F = \Delta p/\Delta t\), which gives \(F = ma\) for constant mass; \(a\) is in the direction of the resultant force. Third law: equal, opposite, same type, on different bodies.
- Momentum \(p = mv\) is a vector. Impulse \(F\Delta t = \Delta p\) is the area under a force–time graph. A longer stopping time means a smaller force. A rebound adds the two momenta.
- Solve \(F = ma\) problems from a free-body diagram: resultant force first. In a lift, scale reading \(R = m(g + a)\) for upward acceleration \(a\). On a slope, the component along the slope is \(mg\sin\theta\) and \(N = mg\cos\theta\).
- Drag increases with speed. A falling object has \(a = g\) at first, then \(a\) decreases to zero at terminal velocity, when drag equals weight (the resultant force is zero, not "no force").
- Conservation of momentum: total momentum is constant if no resultant external force acts. Use signs for direction; in two dimensions, conserve each perpendicular component.
- Elastic: kinetic energy conserved and relative speed of approach = relative speed of separation. Inelastic: some kinetic energy becomes other forms; momentum is still conserved. Sticking together loses the most.
:::

:::links
- explore: [Collision Lab](https://phet.colorado.edu/en/simulations/collision-lab) · PhET · set masses and speeds, and test elastic and inelastic collisions in one and two dimensions
- explore: [Forces and Motion: Basics](https://phet.colorado.edu/en/simulations/forces-and-motion-basics) · PhET · add forces and friction to see the resultant force and acceleration
- papers: [9702 Paper 2 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-physics/cie-paper-2/) · Physics & Maths Tutor · find the dynamics questions in real papers [unofficial]

Links checked 13 October 2026.
:::
Next: [Forces, density and pressure](#phys.forces)
