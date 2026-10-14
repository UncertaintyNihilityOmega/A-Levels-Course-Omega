@chapter phys.kinematics
@title Kinematics
@level as
@paper CAIE P1 · P2 · P3 (AS)
@time 6–8 hours
@summary How to describe motion in a straight line and in two dimensions: displacement, velocity and acceleration, motion graphs, the four equations for constant acceleration (derived), free fall, an experiment to measure g, and projectiles.

:::why
Kinematics is the description of motion before you ask what causes it, and every later topic in mechanics, from forces to orbits and from oscillations to electrons in a field, builds on its ideas. The graphs and equations in this chapter let you predict where a car, a ball or a spacecraft will be and how fast it will be moving. Because the same few relationships solve most of the problems, a careful method and a firm sign convention matter more than clever tricks.
:::

**Before you start**, you need vectors and components from [Physical quantities, units and uncertainty](#phys.units), and straight-line graphs from [Graphs and straight lines](#math.f.graphs).

:::try Warm-up
Q: A velocity of \(20\,\mathrm{m\,s^{-1}}\) points 30° above the horizontal. Find its horizontal and vertical components. (from [Physical quantities, units and uncertainty](#phys.units))
A: Horizontal \(20\cos 30^\circ = 17.3\,\mathrm{m\,s^{-1}}\), vertical \(20\sin 30^\circ = 10.0\,\mathrm{m\,s^{-1}}\).
Q: Convert \(72\,\mathrm{km\,h^{-1}}\) to \(\mathrm{m\,s^{-1}}\). (from [Physical quantities, units and uncertainty](#phys.units))
A: \(72 \times 10^{3}\,\mathrm{m}/3600\,\mathrm{s} = 20\,\mathrm{m\,s^{-1}}\).
Q: Is a distance of 5 km a scalar or a vector? What extra information would make it a vector? (from [Physical quantities, units and uncertainty](#phys.units))
A: A scalar, because it has magnitude only. Adding a direction (5 km north) makes it a displacement, which is a vector.
:::

## Describing motion

To describe where something is, you need a starting point and a direction. In a straight line, you choose one direction to be **positive**, and everything pointing the other way is negative. Choose this first and keep to it for the whole problem. It is the single most useful habit in this chapter.

:::def Distance
The total length of the path travelled by an object, regardless of direction. It is a scalar.
:::

:::def Displacement
The distance in a specified direction from a fixed point (the straight-line distance from the start, with a direction). It is a vector.
:::

A runner who goes once around a 400 m track has travelled a distance of 400 m, but has a displacement of zero, because she finished where she started.

:::def Speed
The distance travelled per unit time. It is a scalar.
:::

:::def Velocity
The rate of change of displacement. It is a vector, so it has a direction, and in a straight line the sign shows the direction.
:::

:::def Acceleration
The rate of change of velocity. It is a vector, with unit \(\mathrm{m\,s^{-2}}\).
:::

In symbols, for an interval of time \(\Delta t\):
\[v = \frac{\Delta s}{\Delta t} \qquad\qquad a = \frac{\Delta v}{\Delta t} = \frac{v - u}{\Delta t}\]
where \(s\) is displacement, \(u\) is the initial velocity and \(v\) is the final velocity. These give **average** values over the interval. The **instantaneous** value is what you get as the interval shrinks to almost nothing, which is the reading on a speedometer at one moment.

Acceleration is the rate of change of *velocity*, not of speed. Because velocity is a vector, an object accelerates when its speed changes **or** when its direction changes. A car going round a bend at a steady \(20\,\mathrm{m\,s^{-1}}\) is accelerating, because its velocity vector is turning. This chapter looks at motion along a line (and one important case in a plane); circular motion comes later.

:::key Signs and "deceleration"
Acceleration is positive if it points in the positive direction, whatever the object is doing. An object **slows down** when its acceleration points *opposite* to its velocity. So a car moving in the positive direction while braking has a negative acceleration, and a car moving in the negative direction while braking has a positive one. "Deceleration" just means "acceleration opposite to the velocity". In calculations, write \(a = -5.0\,\mathrm{m\,s^{-2}}\) and not "a deceleration of 5.0".
:::

:::eg A runner completes one lap of a 400 m track in 50 s. Find her average speed and her average velocity for the lap.
Average speed \(= \dfrac{\text{distance}}{\text{time}} = \dfrac{400}{50} = 8.0\,\mathrm{m\,s^{-1}}\). [A1]

Average velocity \(= \dfrac{\text{displacement}}{\text{time}}\). She ends where she started, so the displacement is zero and the average velocity is \(0\,\mathrm{m\,s^{-1}}\). [A1]
Speed is a scalar and never negative. Velocity is a vector and averages to zero over a complete lap.
:::

:::eg A car accelerates uniformly from rest to \(100\,\mathrm{km\,h^{-1}}\) in 8.0 s. Calculate its acceleration.
Change to base units: \(100\,\mathrm{km\,h^{-1}} = \dfrac{100 \times 10^{3}}{3600} = 27.8\,\mathrm{m\,s^{-1}}\). [C1]

\[a = \frac{v - u}{t} = \frac{27.8 - 0}{8.0} = 3.5\,\mathrm{m\,s^{-2}}\] [A1]
Keep the unrounded speed in your calculator until the end: \(27.78/8.0 = 3.47\) unrounded. The answer is given to 2 significant figures, the same as the data.
:::

:::eg A ball hits a wall at \(8.0\,\mathrm{m\,s^{-1}}\) and rebounds at \(6.0\,\mathrm{m\,s^{-1}}\). The contact lasts 0.020 s. Find its average acceleration.
Take the direction towards the wall as positive, so \(u = +8.0\) and \(v = -6.0\,\mathrm{m\,s^{-1}}\). [B1]

\[a = \frac{v - u}{t} = \frac{-6.0 - 8.0}{0.020} = -700\,\mathrm{m\,s^{-2}}\] [C1]
The magnitude is \(7.0 \times 10^{2}\,\mathrm{m\,s^{-2}}\), directed away from the wall. [A1]
This is about 70 times the acceleration of free fall, which is why a hard ball hitting a wall can leave a dent.
:::

## Graphs of motion

Graphs show a whole journey at once, and they are the standard way physicists reason about motion. Three graphs matter, and each is connected to the next by a gradient or an area.

:::key Graphs of motion
| Graph | Gradient | Area under graph |
|---|---|---|
| displacement–time (\(s\)–\(t\)) | velocity | not used |
| velocity–time (\(v\)–\(t\)) | acceleration | displacement |
| acceleration–time (\(a\)–\(t\)) | not used | change in velocity |

Gradient = rise over run = (change in the \(y\) quantity) / (change in the \(x\) quantity). On a curve, use the gradient of the **tangent** at the point, which gives the instantaneous value.
:::

### Displacement–time graphs

On an \(s\)–\(t\) graph, a horizontal line means the object is at rest, and a straight sloping line means constant velocity. A steeper line means a larger speed. A line sloping downwards means the object is moving in the negative direction. A curve means the velocity is changing.

:::plot A car accelerating from rest has displacement \(s = 5t^{2}\). The gradient of the tangent at \(t = 2\,\mathrm{s}\) is its velocity at that moment.
--f "5*x**2" --f "20*x-20" --x 0 4 --y 0 100 --xstep 1 --pt "2,20,(2.0 s, 20 m)@nw" --pt "1,0,(1.0 s, 0)@se" --pt "3,40,(3.0 s, 40 m)@se" --xlabel "t / s" --ylabel "s / m" --label "s = 5t²" --label "tangent at t = 2 s" --legend tr
:::

:::eg Use the tangent in the graph above to find the velocity of the car at \(t = 2.0\,\mathrm{s}\).
The tangent touches the curve at \((2.0\,\mathrm{s}, 20\,\mathrm{m})\) and passes through \((1.0\,\mathrm{s}, 0)\) and \((3.0\,\mathrm{s}, 40\,\mathrm{m})\). Use two points far apart on the tangent. [B1]

\[v = \text{gradient} = \frac{40 - 0}{3.0 - 1.0} = 20\,\mathrm{m\,s^{-1}}\] [C1 A1]
The velocity is increasing: the gradient of the curve at \(t = 1\) is smaller, and at \(t = 3\) it is larger.
:::

:::warn Draw tangents, not chords
The gradient of the line joining two points on a curve is the *average* velocity between them. For the instantaneous velocity, the tangent must touch the curve at exactly one point, with the curve equally on both sides of the line near that point. Use a long tangent so that the gradient triangle is large.
:::

### Velocity–time graphs

The \(v\)–\(t\) graph is the most useful. Its **gradient** is the acceleration: a horizontal line is constant velocity (zero acceleration), and a straight sloping line is constant acceleration. Its **area** between the graph and the time axis is the displacement, because displacement = velocity × time, which is the area of a rectangle, and any shape can be built from rectangles and triangles. Area **above** the axis is displacement in the positive direction, and area **below** the axis is displacement in the negative direction.

:::html
<figure class="fig wide"><svg viewBox="0 0 520 235" role="img" aria-label="Velocity–time graph of a trolley. Velocity rises from 0 to 4 metres per second in 2 seconds, stays at 4 until 5 seconds, falls through zero at 7 seconds to minus 2 at 8 seconds and stays at minus 2 until 10 seconds. The areas above the axis are 4, 12 and 4 metres, and the areas below the axis are minus 1 and minus 4 metres."><path class="gr" d="M150 20V190M230 20V190M310 20V190M390 20V190M470 20V190"/><path class="gr" d="M70 30H480M70 80H480M70 180H480"/><path class="f1 s-acc sw1" d="M70 130L150 30V130Z"/><path class="f1 s-acc sw1" d="M150 30H270V130H150Z"/><path class="f1 s-acc sw1" d="M270 30L350 130H270Z"/><path class="f3 s-red sw1" d="M350 130L390 180V130Z"/><path class="f3 s-red sw1" d="M390 130H470V180H390Z"/><path class="ax" d="M70 130H485"/><path class="ax" d="M70 18V195"/><path class="c1" d="M70 130L150 30H270L390 180H470"/><text class="ts te" x="62" y="34">4</text><text class="ts te" x="62" y="84">2</text><text class="ts te" x="62" y="134">0</text><text class="ts te" x="62" y="184">−2</text><text class="ts tc" x="70" y="206">0</text><text class="ts tc" x="150" y="206">2</text><text class="ts tc" x="230" y="206">4</text><text class="ts tc" x="310" y="206">6</text><text class="ts tc" x="390" y="206">8</text><text class="ts tc" x="470" y="206">10</text><text class="tl tc" x="275" y="226">t / s</text><text class="tl" x="78" y="14">v / m s⁻¹</text><text class="tl tc" x="118" y="112">+4</text><text class="tl tc" x="210" y="88">+12</text><text class="tl tc" x="290" y="112">+4</text><text class="ts tc" x="379" y="150">−1</text><text class="tl tc" x="430" y="158">−4</text></svg><figcaption>A trolley moves forwards, slows, reverses and moves backwards. The numbers in the shaded areas are displacements in metres. The area above the axis counts as positive and the area below as negative. The acceleration is +2 m s⁻² for 0–2 s, zero for 2–5 s, and −2 m s⁻² for 5–8 s, then zero again.</figcaption></figure>
:::

:::eg Use the graph above to find (a) the acceleration between 5 s and 8 s, (b) the displacement of the trolley after 10 s, (c) the total distance it travels and (d) its average velocity and average speed over the 10 s.
(a) The gradient from \((5\,\mathrm{s}, 4\,\mathrm{m\,s^{-1}})\) to \((8\,\mathrm{s}, -2\,\mathrm{m\,s^{-1}})\) is
\[a = \frac{-2 - 4}{8 - 5} = -2.0\,\mathrm{m\,s^{-2}}\] [C1 A1]
(b) Add the areas, counting those below the axis as negative:
\[4 + 12 + 4 - 1 - 4 = 15\,\mathrm{m}\] [C1 A1]
(c) Distance is a scalar, so every area counts as positive: \(4 + 12 + 4 + 1 + 4 = 25\,\mathrm{m}\). [A1]

(d) Average velocity \(= 15/10 = 1.5\,\mathrm{m\,s^{-1}}\) and average speed \(= 25/10 = 2.5\,\mathrm{m\,s^{-1}}\). [A1]
The trolley turned round at 7 s, when its velocity passed through zero. A change in the sign of velocity is a change of direction.
:::

Explore the connection between a \(v\)–\(t\) graph, its gradient and its area:

:::html
<div class="widget" data-w="vt"></div>
:::

### Acceleration–time graphs

An \(a\)–\(t\) graph for the trolley above would be four horizontal segments: \(+2\), \(0\), \(-2\) and \(0\) in \(\mathrm{m\,s^{-2}}\). The area under it is the **change in velocity**. For 0 to 2 s the area is \(2 \times 2 = 4\,\mathrm{m\,s^{-1}}\), which is exactly how much the velocity rose.

### Converting between graphs

When you are given one graph and asked for another, work with gradients: the \(v\)–\(t\) graph is the gradient of the \(s\)–\(t\) graph, and the \(a\)–\(t\) graph is the gradient of the \(v\)–\(t\) graph. Going the other way, use areas. A useful check is that a horizontal \(s\)–\(t\) line gives \(v = 0\); a straight sloping \(s\)–\(t\) line gives a constant \(v\); and an \(s\)–\(t\) parabola gives a straight \(v\)–\(t\) line.

:::warn Distance–time or displacement–time?
A ball thrown straight up and caught at the same height has a displacement–time graph that rises, peaks and falls back to zero, a parabola. Its **distance**–time graph never falls: the distance travelled increases the whole time, up and then down. A distance–time graph can never have a negative gradient. If a question asks for "distance", the graph keeps rising.
:::

## Equations of uniformly accelerated motion

Many real motions have an acceleration that is constant, or close to it: a car pulling away steadily, a coin dropped in a vacuum, a ball in free fall. For constant acceleration there are four equations that link five quantities.

:::def Uniform acceleration
Acceleration that is constant in magnitude and direction.
:::

The five quantities are \(s\), \(u\), \(v\), \(a\) and \(t\). Each equation leaves one of them out, so you choose the equation by asking which quantity you neither know nor want.

:::formula Equations of uniformly accelerated motion
\[v = u + at \qquad s = \tfrac12(u + v)t \qquad s = ut + \tfrac12 at^{2} \qquad v^{2} = u^{2} + 2as\]
\(s\): displacement (m) · \(u\): initial velocity (\(\mathrm{m\,s^{-1}}\)) · \(v\): final velocity (\(\mathrm{m\,s^{-1}}\)) · \(a\): acceleration (\(\mathrm{m\,s^{-2}}\)) · \(t\): time (s). These apply **only** to motion in a straight line with **constant** acceleration. The data sheet gives \(s = ut + \tfrac12 at^{2}\) and \(v^{2} = u^{2} + 2as\); you must remember the other two, or derive them.
:::

The first equation is the definition of acceleration rearranged. To see where the others come from, look at a \(v\)–\(t\) graph for constant acceleration, which is a straight line.

:::html
<figure class="fig small"><svg viewBox="30 10 360 215" role="img" aria-label="A velocity–time graph with a straight line from velocity u at time 0 to velocity v at time t. A rectangle of height u below the line has area u times t, and a triangle on top has area one half of (v minus u) times t."><path class="f1 s-acc sw1" d="M60 130H300V190H60Z"/><path class="f2 s-acc2 sw1" d="M60 130H300V50Z"/><path class="ax" d="M60 190H340"/><path class="ax" d="M60 190V25"/><path class="c1" d="M60 130L300 50"/><path class="ln-m dash thin" d="M300 190V50"/><text class="tl ti te" x="52" y="134">u</text><text class="tl ti" x="310" y="54">v</text><text class="tl ti tc" x="300" y="208">t</text><text class="tl tc" x="60" y="208">0</text><text class="tl tc" x="180" y="168">area = ut</text><text class="tl tc" x="212" y="118">area = ½(v − u)t</text><text class="tl" x="68" y="22">v</text><text class="tl" x="346" y="194">t</text><text class="tl" x="78" y="82">gradient = a</text></svg><figcaption>For constant acceleration, the area under the line is a rectangle (u × t) plus a triangle (½ × (v − u) × t). The gradient of the line is a.</figcaption></figure>
:::

:::proof examinable Deriving the equations of uniformly accelerated motion
Start from the definition of acceleration, \(a = \dfrac{v - u}{t}\), where \(u\) is the initial velocity and \(v\) the velocity after time \(t\). Rearranging gives equation 1: \(v = u + at\).
The \(v\)–\(t\) graph is a straight line because \(a\) is constant, and the displacement \(s\) is the area under it.
The area is a trapezium of parallel sides \(u\) and \(v\) and width \(t\), so \(s = \tfrac12(u + v)t\). This is equation 2.
Alternatively, split the area into a rectangle and a triangle: \(s = ut + \tfrac12(v - u)t\).
From equation 1, \(v - u = at\), so \(s = ut + \tfrac12(at)t = ut + \tfrac12 at^{2}\). This is equation 3.
To remove \(t\), rearrange equation 1: \(t = \dfrac{v - u}{a}\).
Substitute into equation 2: \(s = \tfrac12(u + v)\dfrac{(v - u)}{a}\).
Multiply by \(2a\): \(2as = (u + v)(v - u) = v^{2} - u^{2}\).
Rearranging gives equation 4: \(v^{2} = u^{2} + 2as\).
Each step uses only the definition of acceleration and the fact that displacement is the area under a \(v\)–\(t\) graph.
:::

Use this procedure for every problem.

:::steps
1. **Choose a positive direction** and mark it on your sketch. Quantities pointing the other way are negative.
2. **List** \(s\), \(u\), \(v\), \(a\), \(t\) and write what you know, with signs. Write "?" for the one you want.
3. One of the five is neither known nor wanted. **Choose the equation that does not contain it.**
4. Substitute, solve, and check that the answer is sensible, with the sign and unit.
:::

:::eg A car accelerates from rest at \(2.5\,\mathrm{m\,s^{-2}}\) for 8.0 s. Find its final velocity and the distance it travels. It then brakes to rest over a distance of 40 m. Find the deceleration and the time to stop.
Take the direction of motion as positive. Stage 1: \(u = 0\), \(a = 2.5\,\mathrm{m\,s^{-2}}\), \(t = 8.0\,\mathrm{s}\). Wanted: \(v\) and \(s\).

\(v = u + at = 0 + 2.5 \times 8.0 = 20\,\mathrm{m\,s^{-1}}\). [C1 A1]

\(s = ut + \tfrac12 at^{2} = 0 + \tfrac12 \times 2.5 \times 8.0^{2} = 80\,\mathrm{m}\). [A1]

Stage 2: \(u = 20\,\mathrm{m\,s^{-1}}\), \(v = 0\), \(s = 40\,\mathrm{m}\). Wanted: \(a\), and \(t\) is not needed, so use \(v^{2} = u^{2} + 2as\). [B1]

\[0 = 20^{2} + 2a \times 40 \quad\Rightarrow\quad a = -\frac{400}{80} = -5.0\,\mathrm{m\,s^{-2}}\] [C1 A1]
The negative sign shows that the acceleration points opposite to the motion. To find the time: \(s = \tfrac12(u + v)t\) gives \(40 = \tfrac12 \times 20 \times t\), so \(t = 4.0\,\mathrm{s}\). [A1]
:::

### Stopping distances

A driver who sees danger needs time to react. During this **thinking time** the car keeps its speed, so the **thinking distance** is speed multiplied by reaction time. Then the brakes slow the car, over the **braking distance**.

:::eg A driver's reaction time is 0.70 s and the car can brake with a constant deceleration of \(5.0\,\mathrm{m\,s^{-2}}\). Find the stopping distance from (a) \(15\,\mathrm{m\,s^{-1}}\) and (b) \(30\,\mathrm{m\,s^{-1}}\).
(a) Thinking distance: \(15 \times 0.70 = 10.5\,\mathrm{m}\). [C1]

Braking distance, with \(u = 15\), \(v = 0\), \(a = -5.0\): \(s = \dfrac{v^{2} - u^{2}}{2a} = \dfrac{0 - 225}{-10} = 22.5\,\mathrm{m}\). [C1]

Stopping distance \(= 10.5 + 22.5 = 33\,\mathrm{m}\). [A1]

(b) At twice the speed: thinking distance \(30 \times 0.70 = 21\,\mathrm{m}\) (twice as long), braking distance \(\dfrac{900}{10} = 90\,\mathrm{m}\) (four times as long). Stopping distance \(= 111\,\mathrm{m}\). [A1]
Thinking distance is proportional to speed, because the car moves at constant speed. Braking distance is proportional to speed *squared*, because \(s = u^{2}/2|a|\). Doubling the speed more than doubles the stopping distance, which is why speed limits matter near schools.
:::

## Free fall

Near the Earth's surface, an object that is let go falls with an acceleration that does not depend on its mass, as long as air resistance is negligible. This is the **acceleration of free fall**, \(g = 9.81\,\mathrm{m\,s^{-2}}\), directed downwards. In 1971 an astronaut on the Moon dropped a hammer and a feather together. With no air to resist the feather, they hit the ground at the same time. On Earth, a feather falls slowly because of air resistance, not because it has less weight.

The four equations apply to free fall with \(a = \pm g\). **Choose up or down as positive and stay with it.** If up is positive, then \(a = -9.81\,\mathrm{m\,s^{-2}}\). If down is positive, then \(a = +9.81\,\mathrm{m\,s^{-2}}\), and an upward initial velocity must then be negative. This is where most marks are lost.

:::plot Velocity–time graph for a ball thrown upwards at 15 m s⁻¹ (up is positive). The gradient is −9.81 m s⁻² throughout, including at the top, where v = 0.
--f "15-9.81*x" --x 0 3.2 --y -20 20 --pt "1.53,0,top: v = 0 at 1.53 s@ne" --pt "0,15,15 m s⁻¹@ne" --xlabel "t / s" --ylabel "v / m s⁻¹" --label "v = 15 − 9.81t" --legend tr
:::

Two facts follow from the graph. First, at the highest point the velocity is zero **but the acceleration is not**: the line has the same slope there as everywhere else. Second, the ball returns to its starting level with the same speed it had when it left, but moving downwards, because the areas above and below the axis cancel when it is back at the start.

:::eg A ball is thrown vertically upwards at \(15\,\mathrm{m\,s^{-1}}\) from the top of a cliff 20 m above the sea. It misses the cliff on the way down. Find (a) the greatest height above the cliff top, (b) the time to reach the sea and (c) its speed on reaching the sea.
Take **up as positive**. Then \(u = +15\,\mathrm{m\,s^{-1}}\) and \(a = -9.81\,\mathrm{m\,s^{-2}}\).

(a) At the highest point \(v = 0\), and time is not needed, so \(v^{2} = u^{2} + 2as\) gives
\[0 = 15^{2} - 2 \times 9.81 \times s \quad\Rightarrow\quad s = \frac{225}{19.62} = 11.5\,\mathrm{m}\] [C1 A1]
(b) At the sea, the displacement from the cliff top is \(s = -20\,\mathrm{m}\). Using \(s = ut + \tfrac12 at^{2}\):
\[-20 = 15t - 4.905t^{2} \quad\Rightarrow\quad 4.905t^{2} - 15t - 20 = 0\] [M1]
By the quadratic formula,
\[t = \frac{15 \pm \sqrt{15^{2} + 4 \times 4.905 \times 20}}{2 \times 4.905} = \frac{15 \pm 24.85}{9.81}\]
so \(t = 4.06\,\mathrm{s}\) or \(t = -1.00\,\mathrm{s}\). [C1]

The negative root would be a time *before* the throw, so it has no physical meaning. The time is \(4.06\,\mathrm{s}\). [A1]

(c) \(v^{2} = u^{2} + 2as = 15^{2} + 2 \times (-9.81) \times (-20) = 617.4\), so the speed is \(24.8\,\mathrm{m\,s^{-1}}\). [A1]
As a check, \(v = u + at = 15 - 9.81 \times 4.06 = -24.8\,\mathrm{m\,s^{-1}}\): the negative sign means downwards. The speed at the sea is the same whether the ball was thrown up at 15 or thrown *down* at 15, because on the way down it passes the cliff top at \(15\,\mathrm{m\,s^{-1}}\) downwards.
:::

:::exam Rejecting a root
When a quadratic gives two times, decide which is physical and say why. A negative time is before the motion started. A time larger than the flight time means the object is already on the ground. Cambridge awards a mark for the reason, so write it in words.
:::

### Measuring the acceleration of free fall

You can measure \(g\) in the laboratory by timing something that falls. The usual method uses a small, dense **steel ball**, because air resistance is negligible for a compact object, and an electronic timer to avoid the errors of a stopwatch.

:::html
<figure class="fig small"><svg viewBox="60 12 400 270" role="img" aria-label="A steel ball held by an electromagnet at the top of a vertical stand. A trapdoor switch is a distance h below the ball. Wires from the electromagnet and the trapdoor switch lead to an electronic timer."><path class="ln thick" d="M90 24V272"/><path class="ln thick" d="M70 272H110"/><path class="ln" d="M90 41H170"/><rect class="fp s-ink sw2" x="170" y="30" width="40" height="22"/><circle class="fa s-ink sw1" cx="190" cy="61" r="9"/><rect class="fp s-ink sw2" x="165" y="232" width="50" height="10"/><path class="ln-m dash thin" d="M190 70H252M190 232H252"/><path class="c1" d="M246 151V73" marker-end="url(#ah-phys)"/><path class="c1" d="M246 151V229" marker-end="url(#ah-phys)"/><text class="tl ti ta" x="258" y="155">h</text><rect class="fp s-ink sw2" x="330" y="130" width="110" height="60"/><text class="tl tc" x="385" y="165">electronic timer</text><path class="ln" d="M210 41H385V130"/><path class="ln" d="M215 237H385V190"/><text class="tl" x="222" y="30">electromagnet</text><text class="tl te" x="174" y="86">steel ball</text><text class="tl tc" x="190" y="262">trapdoor switch</text></svg><figcaption>When the electromagnet current is switched off, the ball is released and the timer starts. When the ball hits the trapdoor switch, the timer stops. The ball falls the distance h, measured from the bottom of the ball to the switch.</figcaption></figure>
:::

:::lab Finding g using a falling ball
:::steps
1. Hold a steel ball on an electromagnet, a measured height \(h\) above a trapdoor switch. Measure \(h\) with a metre rule, from the bottom of the ball to the top of the switch.
2. Switch off the electromagnet: this releases the ball and starts the electronic timer. The timer stops when the ball opens the trapdoor. Record the time \(t\).
3. Repeat each height three times and take the mean time. Repeat for at least six different heights from about 0.2 m to 1.2 m.
4. The ball starts from rest, so \(h = \tfrac12 gt^{2}\). Plot \(h\) on the \(y\)-axis against \(t^{2}\). The graph is a straight line through the origin with **gradient \(= g/2\)**, so \(g = 2 \times \text{gradient}\).
5. Use a large triangle on the line of best fit to find the gradient.
:::
:::

Sources of error and improvements:

- **Release delay** (systematic): the magnet's field takes a moment to die away, so the ball is released slightly *after* the timer starts and every measured time is slightly too long. This puts a positive intercept on the time axis. See the analysis below for how to remove it.
- **Measuring \(h\)**: measure to the bottom of the ball, not the centre, and with the rule vertical. Use a set square to check.
- **Air resistance**: small for a dense ball over short distances, and it would make the measured \(g\) slightly too small. Use a small, heavy steel ball rather than a light one.
- **Alternative method**: let a card with equally spaced black bands (a "picket fence") fall through a light gate. The computer records the time for each band to pass and so finds the velocity at each position. A graph of \(v\) against \(t\) is a straight line with gradient \(g\).

If there is a release delay \(\delta\), the measured time is \(t = t_\mathrm{fall} + \delta\), where \(t_\mathrm{fall} = \sqrt{2h/g}\). Then \(t = \sqrt{2/g}\,\sqrt{h} + \delta\). A graph of \(t\) against \(\sqrt{h}\) is a straight line whose **gradient is \(\sqrt{2/g}\)** and whose **intercept on the \(t\)-axis is the delay \(\delta\)**. This graph is better than \(h\) against \(t^{2}\) because it measures the systematic error instead of being spoilt by it.

:::eg A ball is released with a delay. Times \(t\) for heights \(h\) are shown. A graph of \(t\) against \(\sqrt{h}\) gives the points \((0.447, 0.214)\) and \((1.095, 0.507)\) on its line of best fit, with \(\sqrt{h}\) in \(\mathrm{m^{1/2}}\) and \(t\) in s. Find \(g\) and the delay.

| \(h\,/\,\mathrm{m}\) | 0.20 | 0.40 | 0.60 | 0.80 | 1.00 | 1.20 |
|---|---|---|---|---|---|---|
| \(\sqrt{h}\,/\,\mathrm{m^{1/2}}\) | 0.447 | 0.632 | 0.775 | 0.894 | 1.000 | 1.095 |
| \(t\,/\,\mathrm{ms}\) | 214 | 298 | 362 | 416 | 464 | 507 |

Gradient \(= \dfrac{0.507 - 0.214}{1.095 - 0.447} = 0.452\,\mathrm{s\,m^{-1/2}}\). [C1]

The gradient is \(\sqrt{2/g}\). Keep the unrounded gradient (0.4522) in your calculator, so \(g = \dfrac{2}{0.4522^{2}} = 9.78\,\mathrm{m\,s^{-2}}\). [A1]

The intercept is \(c = 0.214 - 0.452 \times 0.447 = 0.012\,\mathrm{s}\), a delay of about 12 ms. [A1]
:::

## Projectiles

A **projectile** is an object that moves through the air under gravity alone. Its path is a curve, but the physics is simple if you split the motion into two perpendicular directions. Here we ignore air resistance, which for a real ball or a long-range shell has an effect that is not small; the effect of drag is treated qualitatively in [Dynamics and momentum](#phys.dynamics).

:::key The two independent motions
**Horizontal:** no force acts horizontally, so the horizontal velocity is **constant**. \(s_x = u_x t\).

**Vertical:** gravity gives a constant downward acceleration \(g\), so the vertical motion is free fall. Use the equations for constant acceleration with \(a = \pm 9.81\,\mathrm{m\,s^{-2}}\).

The two motions are **independent** and share only the time. Find the time from the direction where you know the most, then use it in the other.
:::

:::html
<figure class="fig wide"><svg viewBox="0 40 590 255" role="img" aria-label="A parabolic path from launch to landing on level ground, with arrows at five points. The horizontal velocity arrow has the same length at every point. The vertical velocity arrow points up and gets shorter, is zero at the top, then points down and grows again."><path class="ln-m dash thin" d="M40 230H580"/><path class="ln" d="M60 230Q280 -30 500 230"/><circle class="fi" cx="60" cy="230" r="4"/><circle class="fi" cx="170" cy="132.5" r="4"/><circle class="fi" cx="280" cy="100" r="4"/><circle class="fi" cx="390" cy="132.5" r="4"/><circle class="fi" cx="500" cy="230" r="4"/><path class="c1" d="M60 230H120" marker-end="url(#ah-phys)"/><path class="c2" d="M60 230V160" marker-end="url(#ah2-phys)"/><path class="c1" d="M170 132.5H230" marker-end="url(#ah-phys)"/><path class="c2" d="M170 132.5V97.5" marker-end="url(#ah2-phys)"/><path class="c1" d="M280 100H340" marker-end="url(#ah-phys)"/><path class="c1" d="M390 132.5H450" marker-end="url(#ah-phys)"/><path class="c2" d="M390 132.5V167.5" marker-end="url(#ah2-phys)"/><path class="c1" d="M500 230H560" marker-end="url(#ah-phys)"/><path class="c2" d="M500 230V280" marker-end="url(#ah2-phys)"/><text class="tl ta" x="66" y="248">u cos θ</text><text class="tl te ta2" x="52" y="196">u sin θ</text><text class="tl tc" x="280" y="86">highest point: vertical component is zero</text><text class="tl te" x="492" y="262">same vertical speed as at launch</text></svg><figcaption>The horizontal arrow is the same at every point because no horizontal force acts. The vertical arrow shrinks as the projectile rises, vanishes at the top and grows again as it falls. At the top the velocity is not zero: it is the horizontal component.</figcaption></figure>
:::

### Horizontal launch

An object projected horizontally has zero vertical velocity at the start.

:::eg A parcel is released from a plane flying horizontally at \(60\,\mathrm{m\,s^{-1}}\) at a height of 500 m. Ignore air resistance. Find (a) the time to reach the ground, (b) the horizontal distance travelled and (c) the speed and direction of the parcel when it hits the ground.
Take **down as positive**. Vertical: \(u_y = 0\), \(a = +9.81\,\mathrm{m\,s^{-2}}\), \(s_y = 500\,\mathrm{m}\). Horizontal velocity is constant at \(60\,\mathrm{m\,s^{-1}}\). [B1]

(a) \(s_y = u_y t + \tfrac12 at^{2}\) gives \(500 = \tfrac12 \times 9.81 \times t^{2}\), so
\[t = \sqrt{\frac{2 \times 500}{9.81}} = 10.1\,\mathrm{s}\] [C1 A1]
(b) \(s_x = u_x t = 60 \times 10.096 = 606\,\mathrm{m}\), about \(6.1 \times 10^{2}\,\mathrm{m}\). [A1]

(c) Vertical velocity on landing: \(v_y = u_y + at = 9.81 \times 10.096 = 99.0\,\mathrm{m\,s^{-1}}\). The horizontal component is still \(60\,\mathrm{m\,s^{-1}}\).
\[v = \sqrt{60^{2} + 99.0^{2}} = 116\,\mathrm{m\,s^{-1}}\] [C1 A1]
\[\theta = \tan^{-1}\frac{99.0}{60} = 58.8^\circ \text{ below the horizontal}\] [A1]
The parcel lands about 600 m *ahead of* the point where it was released. It stays directly below the plane (if the plane keeps its velocity) all the way down.
:::

### Launch at an angle

If the projectile is launched at speed \(u\) at angle \(\theta\) above the horizontal, the components are \(u_x = u\cos\theta\) and \(u_y = u\sin\theta\).

:::eg A footballer kicks a ball from the ground at \(25\,\mathrm{m\,s^{-1}}\) at 35° above the horizontal. Find the time of flight, the greatest height and the range on level ground.
Components: \(u_x = 25\cos 35^\circ = 20.5\,\mathrm{m\,s^{-1}}\) and \(u_y = 25\sin 35^\circ = 14.3\,\mathrm{m\,s^{-1}}\). [C1]

Take up as positive, so \(a = -9.81\,\mathrm{m\,s^{-2}}\). The ball returns to the ground when its displacement \(s_y\) is zero:
\[0 = 14.34\,t - 4.905\,t^{2} \quad\Rightarrow\quad t = \frac{14.34}{4.905} = 2.92\,\mathrm{s}\] [C1 A1]
(The other solution, \(t = 0\), is the launch.)

Greatest height: at the top \(v_y = 0\), so \(h = \dfrac{u_y^{2}}{2g} = \dfrac{14.34^{2}}{19.62} = 10.5\,\mathrm{m}\). [A1]

Range: \(x = u_x t = 20.48 \times 2.923 = 59.9\,\mathrm{m}\). [A1]
By symmetry the ball takes half of the flight time (1.46 s) to reach the top.
:::

:::warn The top of the path
The velocity at the highest point is not zero. Only the **vertical** component is zero. The ball is still moving horizontally at \(u\cos\theta\), so its speed at the top is \(u\cos\theta\), the smallest speed on the whole path. The acceleration at the top is still \(9.81\,\mathrm{m\,s^{-2}}\) downwards.
:::

Try the simulation: change the angle and the speed, and watch the horizontal and vertical components. Notice that two balls launched together, one horizontally and one dropped, land at the same time.

:::html
<div class="widget" data-w="projectile"></div>
:::

:::board
All boards teach the same kinematics. AQA and OCR use the same four equations, and some UK textbooks add a fifth, \(s = vt - \tfrac12 at^{2}\), which is the same as the third equation written from the final velocity.
:::

:::eg Spot the error: a stone is thrown vertically upwards at \(12\,\mathrm{m\,s^{-1}}\) from the edge of a cliff 30 m above the sea. Find the time it takes to reach the sea.
A student wrote this answer.

Line 1: take downwards as positive, so \(a = +9.81\,\mathrm{m\,s^{-2}}\) and \(s = +30\,\mathrm{m}\)
Line 2: \(u = +12\,\mathrm{m\,s^{-1}}\)
Line 3: \(30 = 12t + 4.905t^{2}\), so \(t = 1.54\,\mathrm{s}\)

Line 1 is correct. [C1] **Line 2 is wrong: the stone is thrown *upwards* and downwards was chosen as positive, so \(u = -12\,\mathrm{m\,s^{-1}}\). The signs have been mixed.** The final answer mark is lost. [A0]

Correct working: \(30 = -12t + 4.905t^{2}\), so \(4.905t^{2} - 12t - 30 = 0\), and \(t = \dfrac{12 + \sqrt{144 + 588.6}}{9.81} = 3.98\,\mathrm{s}\). [A1]

Check: the stone rises for \(12/9.81 = 1.2\,\mathrm{s}\) and needs another 1.2 s to fall back to the cliff top, 2.4 s in all, before it has even started to fall the 30 m. So 1.5 s was never possible.
:::

:::try Start easy, finish at exam standard
Q: A cyclist travels 90 m in 15 s. Find the average speed.
A: \(90/15 = 6.0\,\mathrm{m\,s^{-1}}\).
Q: A car's velocity changes from \(8.0\,\mathrm{m\,s^{-1}}\) to \(20\,\mathrm{m\,s^{-1}}\) in 6.0 s. Find its acceleration.
A: \(a = (20 - 8.0)/6.0 = 2.0\,\mathrm{m\,s^{-2}}\).
Q: A train travelling at \(30\,\mathrm{m\,s^{-1}}\) brakes uniformly to rest in 20 s. Find its acceleration and the distance it travels while braking.
A: \(a = (0 - 30)/20 = -1.5\,\mathrm{m\,s^{-2}}\). Distance: \(s = \tfrac12(u + v)t = \tfrac12 \times 30 \times 20 = 300\,\mathrm{m}\).
Q: A stone is dropped from rest from the top of a well and takes 2.4 s to hit the water. Find the depth of the well.
A: Take down as positive: \(s = \tfrac12 gt^{2} = \tfrac12 \times 9.81 \times 2.4^{2} = 28\,\mathrm{m}\).
Q: A velocity–time graph is a horizontal line at \(12\,\mathrm{m\,s^{-1}}\) from 0 to 5.0 s. What is the acceleration and the displacement?
A: The gradient is zero, so \(a = 0\). The displacement is the area of the rectangle: \(12 \times 5.0 = 60\,\mathrm{m}\).
Q: A ball is thrown vertically upwards at \(20\,\mathrm{m\,s^{-1}}\). How high does it rise?
A: Up is positive: \(0 = 20^{2} - 2 \times 9.81 \times s\), so \(s = 400/19.62 = 20.4\,\mathrm{m}\).
Q: A ball rolls off a table at \(1.5\,\mathrm{m\,s^{-1}}\) and falls for 0.40 s. How far from the table does it land, and what is its vertical velocity just before it lands?
A: Horizontal distance \(= 1.5 \times 0.40 = 0.60\,\mathrm{m}\). Vertical velocity \(= 9.81 \times 0.40 = 3.9\,\mathrm{m\,s^{-1}}\) downwards.
Q: The displacement–time graph of a cyclist is a straight line from \((0, 0)\) to \((20\,\mathrm{s}, 100\,\mathrm{m})\). Find the cyclist's velocity.
A: Gradient \(= 100/20 = 5.0\,\mathrm{m\,s^{-1}}\).
Q: Explain why a car's stopping distance more than doubles when its speed doubles.
A: The thinking distance doubles because the car travels at constant speed during the reaction time. The braking distance is four times as large, because \(s = u^{2}/2|a|\) depends on the speed squared. So the total is between two and four times as large.
Q: A projectile is launched at 30° above the horizontal at \(40\,\mathrm{m\,s^{-1}}\). What are its speed and the direction of its velocity at the highest point?
A: At the top only the horizontal component remains: \(40\cos 30^\circ = 34.6\,\mathrm{m\,s^{-1}}\), horizontal.
:::

:::try Exam practice ★ to ★★★
Q: [1 mark] ★ Define acceleration.
A: Acceleration is the rate of change of velocity. [B1]
Q: [3 marks] ★ A train's velocity increases uniformly from zero to \(30\,\mathrm{m\,s^{-1}}\) in 60 s. It then travels at this constant velocity for 120 s. Calculate the total distance travelled.
A: Distance while accelerating = area of triangle \(= \tfrac12 \times 60 \times 30 = 900\,\mathrm{m}\). [C1] Distance at constant velocity \(= 30 \times 120 = 3600\,\mathrm{m}\). [C1] Total \(= 4500\,\mathrm{m}\). [A1]
Q: [3 marks] ★ A car travelling at \(25\,\mathrm{m\,s^{-1}}\) brakes with a constant deceleration of \(6.0\,\mathrm{m\,s^{-2}}\). Calculate the distance it travels before stopping.
A: \(v^{2} = u^{2} + 2as\) with \(v = 0\), \(a = -6.0\) [C1] so \(0 = 25^{2} - 2 \times 6.0 \times s\) [C1] \(s = 625/12 = 52\,\mathrm{m}\). [A1]
Q: [4 marks] ★★ A ball is thrown vertically upwards from the ground at \(18\,\mathrm{m\,s^{-1}}\). (a) Calculate the maximum height. (b) Calculate the time for which the ball is in the air.
A: Take up as positive, \(a = -9.81\,\mathrm{m\,s^{-2}}\). (a) \(0 = 18^{2} - 2 \times 9.81 \times h\) [C1] \(h = 16.5\,\mathrm{m}\). [A1] (b) The ball returns to the ground when \(s = 0\): \(0 = 18t - 4.905t^{2}\) [C1] so \(t = 18/4.905 = 3.67\,\mathrm{s}\). [A1]
Q: [3 marks] ★★ A body moves in a straight line with uniform acceleration \(a\). Its velocity increases from \(u\) to \(v\) in time \(t\). Use a velocity–time graph to show that the displacement is \(s = ut + \tfrac12 at^{2}\).
A: The displacement is the area under the velocity–time graph. [B1] The area is a rectangle of height \(u\) and width \(t\), \(ut\), plus a triangle of height \(v - u\) and width \(t\), \(\tfrac12(v - u)t\). [M1] The gradient is \(a = (v - u)/t\), so \(v - u = at\), and \(s = ut + \tfrac12 at^{2}\). [A1]
Q: [5 marks] ★★ A ball rolls off the edge of a horizontal table of height 0.95 m with a horizontal velocity of \(1.8\,\mathrm{m\,s^{-1}}\). Air resistance is negligible. Calculate (a) the time taken to reach the floor, (b) the horizontal distance from the table's edge to where it lands, (c) the speed of the ball just before it hits the floor.
A: (a) \(0.95 = \tfrac12 \times 9.81 \times t^{2}\) [C1] \(t = 0.440\,\mathrm{s}\). [A1] (b) \(x = 1.8 \times 0.440 = 0.79\,\mathrm{m}\). [A1] (c) \(v_y = 9.81 \times 0.440 = 4.32\,\mathrm{m\,s^{-1}}\) [C1] so \(v = \sqrt{1.8^{2} + 4.32^{2}} = 4.7\,\mathrm{m\,s^{-1}}\). [A1]
Q: [7 marks] (#phys.units) ★★★ A ball is kicked from level ground at \(20\,\mathrm{m\,s^{-1}}\) at 40° above the horizontal. It lands on a flat platform 3.0 m above the ground. Air resistance is negligible. (a) Calculate the vertical component of the initial velocity. (b) Calculate the time at which the ball lands on the platform. (c) Calculate the horizontal distance from the kicker to the point where the ball lands. (d) Sketch a graph of the vertical component of velocity against time from the kick until the ball lands, marking the values at the start and the end.
H: Use \(s = ut + \tfrac12 at^{2}\) for the vertical motion with \(s = +3.0\,\mathrm{m}\) and solve a quadratic.
H: There are two positive roots: the ball passes the height of the platform on the way up and again on the way down.
H: Choose the root that corresponds to the ball landing on the platform, not passing over its height while still rising.
A: (a) \(u_y = 20\sin 40^\circ = 12.9\,\mathrm{m\,s^{-1}}\). [A1] (b) \(3.0 = 12.86t - 4.905t^{2}\), so \(4.905t^{2} - 12.86t + 3.0 = 0\). [C1] \(t = \dfrac{12.86 \pm \sqrt{12.86^{2} - 4 \times 4.905 \times 3.0}}{9.81}\) gives \(0.26\,\mathrm{s}\) or \(2.36\,\mathrm{s}\). [M1] At 0.26 s the ball is still rising through the height of the platform, so (assuming it clears the platform) it lands at the later time, \(2.36\,\mathrm{s}\). [A1] (c) \(x = 20\cos 40^\circ \times 2.362 = 15.3 \times 2.362 = 36\,\mathrm{m}\). [A1] (d) A straight line with negative gradient \(-9.81\,\mathrm{m\,s^{-2}}\), starting at \(+12.9\,\mathrm{m\,s^{-1}}\) [B1] crossing zero at 1.31 s and ending at about \(-10.3\,\mathrm{m\,s^{-1}}\) at 2.36 s. [B1]
Q: [6 marks] ★★★ In an experiment to find \(g\), a student drops a ball from heights \(h\) and records the time \(t\) for it to reach a trapdoor switch. Her graph of \(t\) against \(\sqrt{h}\) has the points \((0.447, 0.214)\) and \((1.095, 0.507)\) on the best-fit line, with \(\sqrt{h}\) in \(\mathrm{m^{1/2}}\) and \(t\) in seconds. (a) Show that the graph should be a straight line with gradient \(\sqrt{2/g}\). (b) Calculate \(g\). (c) The line does not pass through the origin. Calculate the intercept and suggest a cause.
H: Start from \(h = \tfrac12 gt^{2}\) and make \(t\) the subject.
H: A time that is always too long by the same amount is a systematic error.
A: (a) \(h = \tfrac12 gt^{2}\) so \(t = \sqrt{2/g}\,\sqrt{h}\), which has the form \(y = mx\) with gradient \(\sqrt{2/g}\). [B1] (b) Gradient \(= (0.507 - 0.214)/(1.095 - 0.447) = 0.452\) [C1] so \(g = 2/0.4522^{2}\) [C1] \(= 9.78\,\mathrm{m\,s^{-2}}\). [A1] (c) Intercept \(= 0.214 - 0.452 \times 0.447 = 0.012\,\mathrm{s}\). [B1] This could be a delay of about 12 ms between the timer starting and the ball being released (a systematic error in every time). [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Ball A is dropped from rest from the top of a vertical cliff 80 m high at the same instant as ball B is thrown vertically upwards from the foot of the cliff at \(25\,\mathrm{m\,s^{-1}}\). Neither is affected by air resistance. (a) Show that the balls meet after a time that does not depend on \(g\), and find this time. (b) Find the height above the ground at which they meet.
H: Both balls have the same acceleration. What is the acceleration of one *relative to* the other?
H: In the frame of ball A, ball B moves at a constant velocity towards it.
A: (a) Both balls accelerate downwards at \(g\), so the acceleration of B relative to A is zero. [B1] The balls therefore approach each other at a constant relative speed of \(25\,\mathrm{m\,s^{-1}}\), and must cover the 80 m separation: \(t = 80/25\) [M1] \(= 3.2\,\mathrm{s}\), independent of \(g\). [A1] (b) Ball A has fallen \(\tfrac12 \times 9.81 \times 3.2^{2}\) [C1] \(= 50.2\,\mathrm{m}\), so the height is \(80 - 50.2\) [C1] \(= 29.8\,\mathrm{m}\). [A1] (Check with ball B: \(25 \times 3.2 - 4.905 \times 3.2^{2} = 29.8\,\mathrm{m}\).)
Q: [6 marks] ★★★ A projectile is launched from level ground at speed \(u\) at angle \(\theta\) above the horizontal. (a) Show that the range on level ground is \(R = \dfrac{u^{2}\sin 2\theta}{g}\). (b) Hence show that, for a given \(u\), the range is greatest when \(\theta = 45^\circ\), and find this range for \(u = 25\,\mathrm{m\,s^{-1}}\). (c) Show that two launch angles \(\theta\) and \(90^\circ - \theta\) give the same range.
H: The time of flight is when the vertical displacement is zero again.
H: Use \(2\sin\theta\cos\theta = \sin 2\theta\).
A: (a) Vertical: \(0 = u\sin\theta\,t - \tfrac12 gt^{2}\), so \(t = \dfrac{2u\sin\theta}{g}\). [C1] Horizontal: \(R = u\cos\theta \times t = \dfrac{2u^{2}\sin\theta\cos\theta}{g}\) [M1] \(= \dfrac{u^{2}\sin 2\theta}{g}\). [A1] (b) For a given \(u\), \(R\) is greatest when \(\sin 2\theta = 1\), so \(2\theta = 90^\circ\), \(\theta = 45^\circ\). [B1] \(R_\mathrm{max} = \dfrac{25^{2}}{9.81} = 63.7\,\mathrm{m}\). [A1] (c) \(\sin 2(90^\circ - \theta) = \sin(180^\circ - 2\theta) = \sin 2\theta\), so the range is the same. [B1] In real games air resistance makes the best angle a little smaller than 45°.
:::

:::quiz
? What does the gradient of a displacement–time graph represent?
- acceleration
+ velocity
- distance travelled
- speed only, never velocity
> Gradient = change in displacement / change in time = velocity. It is a velocity (it can be negative); only the magnitude is the speed.
? A velocity–time graph has a straight line sloping down through the time axis. Which is true?
- The object has stopped for the whole time.
+ The area above the axis is displacement in one direction and the area below it is displacement in the opposite direction.
- The acceleration is increasing.
- The object is always slowing down.
> The velocity changes sign, so the object reverses. The constant negative gradient is a constant acceleration. The object slows until it passes through zero and then speeds up in the opposite direction.
? A ball is thrown straight up. At its highest point, which statement is correct?
- Its velocity and acceleration are both zero.
+ Its velocity is zero and its acceleration is \(9.81\,\mathrm{m\,s^{-2}}\) downwards.
- Its velocity is zero and its acceleration is zero because it is at rest.
- Its acceleration is upwards because it has stopped.
> The velocity is changing at the same rate throughout the flight, so the acceleration at the top is still \(g\) downwards. The ball is not "at rest": it is at rest only for an instant.
? One ball is dropped from a table. A second ball rolls off the same table horizontally at the same moment. Ignoring air resistance, which hits the floor first?
- The one that is dropped.
- The one that rolls off.
+ They land together.
- It depends on the mass of each ball.
> The vertical motion is the same for both: free fall from rest through the same height. The horizontal velocity does not affect it.
? Which of these motions can be solved with \(v = u + at\)?
- A ball on a spring.
- A car with a changing acceleration.
+ A trolley with a constant acceleration down a ramp.
- A satellite orbiting the Earth.
> The equations of uniformly accelerated motion need constant acceleration in a straight line. The other three have changing acceleration.
? A car travelling at \(10\,\mathrm{m\,s^{-1}}\) brakes with constant deceleration and stops in distance \(d\). If it had been travelling at \(20\,\mathrm{m\,s^{-1}}\) with the same deceleration, what would be the braking distance?
- \(2d\)
- \(3d\)
+ \(4d\)
- \(8d\)
> From \(v^{2} = u^{2} + 2as\), \(s \propto u^{2}\). Doubling the initial speed multiplies the braking distance by four.
? A runner completes one lap of a track. Which of these is zero for the lap?
- distance
- average speed
+ displacement
- time taken
> She finishes where she began, so her displacement is zero. The distance and the average speed are both positive.
? A ball is thrown at 30° above the horizontal at \(20\,\mathrm{m\,s^{-1}}\). What is its speed at the highest point?
- \(0\)
- \(10\,\mathrm{m\,s^{-1}}\)
+ \(17.3\,\mathrm{m\,s^{-1}}\)
- \(20\,\mathrm{m\,s^{-1}}\)
> Only the vertical component is zero at the top. The speed is the horizontal component, \(20\cos 30^\circ = 17.3\,\mathrm{m\,s^{-1}}\). The \(10\,\mathrm{m\,s^{-1}}\) is the *initial* vertical component.
:::

:::checklist What you can now do
- [ ] I can define and use distance, displacement, speed, velocity and acceleration, and say which are vectors.
- [ ] I can draw and interpret displacement–time, velocity–time and acceleration–time graphs.
- [ ] I can find displacement from the area under a velocity–time graph, and count area below the axis as negative.
- [ ] I can find velocity from the gradient of a displacement–time graph, using a tangent for a curve.
- [ ] I can find acceleration from the gradient of a velocity–time graph.
- [ ] I can derive the equations of uniformly accelerated motion from the definitions and the \(v\)–\(t\) graph.
- [ ] I can solve problems with those equations, choosing a positive direction and keeping to it, including falling bodies without air resistance.
- [ ] I can describe an experiment to measure the acceleration of free fall, with the graph, the sources of error and how to reduce them.
- [ ] I can analyse projectile motion as constant horizontal velocity and constant vertical acceleration, for horizontal and angled launches.
:::

:::recap
- Displacement and velocity are vectors; distance and speed are scalars. Velocity is the rate of change of displacement, and acceleration is the rate of change of velocity.
- \(s\)–\(t\): gradient = velocity. \(v\)–\(t\): gradient = acceleration, area = displacement. \(a\)–\(t\): area = change in velocity. Area below the axis is negative.
- Constant acceleration only: \(v = u + at\), \(s = \tfrac12(u + v)t\), \(s = ut + \tfrac12 at^{2}\), \(v^{2} = u^{2} + 2as\). Choose a positive direction and keep to it.
- Free fall: \(g = 9.81\,\mathrm{m\,s^{-2}}\) downwards, the same for every mass without air resistance, and also at the top of a throw.
- Stopping distance = thinking distance (proportional to \(v\)) + braking distance (proportional to \(v^{2}\)).
- Measuring \(g\): time a falling steel ball; plot \(h\) against \(t^{2}\) (gradient \(g/2\)); a release delay is a systematic error that gives an intercept on a \(t\) against \(\sqrt{h}\) graph.
- Projectiles: horizontal velocity constant, vertical motion is free fall, and the two motions share only the time. At the top of the path the velocity is the horizontal component.
:::

:::links
- explore: [Projectile Motion](https://phet.colorado.edu/en/simulations/projectile-motion) · PhET · launch objects and see the path, range and velocity components
- read: [CAIE Physics revision notes](https://www.physicsandmathstutor.com/physics-revision/a-level-cie/) · Physics & Maths Tutor · short notes and topic questions [unofficial]

Links checked 13 October 2026.
:::
Next: [Dynamics and momentum](#phys.dynamics)
