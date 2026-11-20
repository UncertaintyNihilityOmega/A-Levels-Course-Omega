@chapter math.fm.polar
@title Polar coordinates
@level fm
@paper CAIE 9231 Paper 1 · Edexcel Further Maths Core Pure
@time 6–8 hours
@summary Polar coordinates describe a point by its distance r from a fixed point and the angle θ of the direction to it. You will convert between polar and Cartesian coordinates and equations, sketch curves such as circles, cardioids, roses and spirals, find greatest distances with calculus, and find areas with ½∫r² dθ.

:::why
Some curves that are awkward in x and y become one short equation in r and θ: a circle through the origin, a spiral, the pickup pattern of a microphone, the coverage of a radar antenna. Polar coordinates match how these things work, with a distance and a direction. They also give a new and neat way to find areas, by adding up thin sectors instead of thin strips.
:::

**Before you start**, you need radians, arcs and sectors from [Circular measure](#math.p1.circular), the double-angle identities from [Further trigonometry](#math.p3.trig) and integration by parts from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech).

:::try Warm-up
Q: A sector has radius 6 cm and angle 0.5 radians. Find its area. (from [Circular measure](#math.p1.circular))
A: Area \(= \tfrac12 r^2\theta = \tfrac12 \times 36 \times 0.5 = 9\,\mathrm{cm^2}\).
Q: Write \(\cos^2\theta\) in terms of \(\cos 2\theta\). (from [Further trigonometry](#math.p3.trig))
A: \(\cos 2\theta = 2\cos^2\theta - 1\), so \(\cos^2\theta = \tfrac12(1 + \cos 2\theta)\).
Q: Find \(\displaystyle\int \theta\,\mathrm{e}^{2\theta}\,d\theta\). (from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech))
A: By parts with \(u = \theta\) and \(\dfrac{dv}{d\theta} = \mathrm{e}^{2\theta}\): \(\tfrac12\theta\mathrm{e}^{2\theta} - \tfrac14\mathrm{e}^{2\theta} + c\).
:::

## Polar coordinates

On a map you can give a place two ways: "3 km east and 4 km north" (Cartesian) or "5 km away in the direction north-east of north" (polar). Polar coordinates use the second way.

:::def Polar coordinates
Fix a point \(O\), the **pole**, and a half-line from it, the **initial line** (drawn along the positive \(x\)-axis). A point \(P\) has polar coordinates \((r, \theta)\), where \(r\) is the distance \(OP\) and \(\theta\) is the angle from the initial line to \(OP\), measured **anticlockwise** and in **radians**. The pole itself has \(r = 0\) and no definite angle.
:::

In 9231 the convention \(r \geq 0\) is used: a distance is never negative. Angles are given in either \(0 \leq \theta < 2\pi\) or \(-\pi < \theta \leq \pi\), and adding \(2\pi\) to \(\theta\) gives the same point.

:::html
<figure class="fig small"><svg viewBox="0 0 320 250" role="img" aria-label="A point P at distance r from the pole O along a ray making angle theta with the initial line. The perpendicular from P to the initial line shows x equals r cos theta along the initial line and y equals r sin theta up to P.">
<line class="ln" x1="40" y1="210" x2="300" y2="210" marker-end="url(#ah)"/>
<line class="c1 sw2" x1="40" y1="210" x2="142.8" y2="87.4"/>
<line class="ln-m thin dash" x1="142.8" y1="87.4" x2="142.8" y2="210"/>
<path class="ln-m" d="M76 210 A36 36 0 0 0 63.1 182.4" fill="none"/>
<circle class="fi" cx="142.8" cy="87.4" r="3.5"/>
<circle class="fi" cx="40" cy="210" r="3"/>
<text class="tl" x="24" y="228">O</text>
<text class="tl" x="150" y="84">P (r, θ)</text>
<text class="tl" x="74" y="146">r</text>
<text class="tl" x="84" y="204">θ</text>
<text class="tl" x="52" y="228">x = r cos θ</text>
<text class="tl" x="150" y="152">y = r sin θ</text>
<text class="tl" x="222" y="200">initial line</text>
</svg><figcaption>The point \(P\) with polar coordinates \((r, \theta)\). Its Cartesian coordinates are \(x = r\cos\theta\) and \(y = r\sin\theta\).</figcaption></figure>
:::

### From Cartesian to polar and back

The right-angled triangle in the figure gives every link between the two systems.

:::key Cartesian and polar
\[x = r\cos\theta \qquad y = r\sin\theta\]
\[r^2 = x^2 + y^2 \qquad \tan\theta = \frac{y}{x}\]
\(r = \sqrt{x^2 + y^2} \geq 0\). To find \(\theta\), use \(\tan\theta = \dfrac{y}{x}\) **and the quadrant** of the point. Find the acute angle \(\tan^{-1}\left|\dfrac yx\right|\) and place it in the right quadrant.
:::

:::eg (a) Convert \((-1, \sqrt3)\) to polar coordinates with \(-\pi < \theta \leq \pi\). (b) Convert \((-2, -2)\). (c) Convert the polar point \(\left(4, \dfrac\pi3\right)\) to Cartesian coordinates.
(a) \(r = \sqrt{1 + 3} = 2\). The point is in the second quadrant, and the acute angle is \(\tan^{-1}\sqrt3 = \dfrac\pi3\). So \(\theta = \pi - \dfrac\pi3 = \dfrac{2\pi}{3}\). The point is \(\left(2, \dfrac{2\pi}{3}\right)\).

(b) \(r = \sqrt{4 + 4} = 2\sqrt2\). The point is in the third quadrant, with acute angle \(\tan^{-1}1 = \dfrac\pi4\). In the range \(-\pi < \theta \leq \pi\), \(\theta = -\pi + \dfrac\pi4 = -\dfrac{3\pi}{4}\). The point is \(\left(2\sqrt2, -\dfrac{3\pi}{4}\right)\), or \(\left(2\sqrt2, \dfrac{5\pi}{4}\right)\) in the range \(0 \leq \theta < 2\pi\).

(c) \(x = 4\cos\dfrac\pi3 = 2\) and \(y = 4\sin\dfrac\pi3 = 2\sqrt3\). The point is \((2, 2\sqrt3)\).
:::

:::warn The calculator gives the wrong quadrant
\(\tan^{-1}\left(\dfrac{y}{x}\right)\) on a calculator always lies between \(-\dfrac\pi2\) and \(\dfrac\pi2\). For \((-1, \sqrt3)\) it gives \(-\dfrac\pi3\), which points into the fourth quadrant. Sketch the point, then add or subtract \(\pi\) as needed.
:::

## Converting equations

A curve given by a Cartesian equation can be written in polar form by substituting \(x = r\cos\theta\) and \(y = r\sin\theta\), and the other way round.

:::steps
1. **Cartesian to polar:** replace \(x\) by \(r\cos\theta\), \(y\) by \(r\sin\theta\), and \(x^2 + y^2\) by \(r^2\). Simplify, and divide through by \(r\) if you can (check that the pole is not lost).
2. **Polar to Cartesian:** multiply both sides by \(r\) (or \(r^2\)) so that you can see \(r\cos\theta = x\), \(r\sin\theta = y\) and \(r^2 = x^2 + y^2\). Replace \(r\) by \(\sqrt{x^2 + y^2}\) only if you must, then square to remove the root.
:::

:::eg Write in polar form: (a) \(x^2 + y^2 = 4x\), (b) \(y = 3\), (c) \(y^2 = 4x\).
(a) Replace \(x^2 + y^2\) by \(r^2\) and \(x\) by \(r\cos\theta\):
\[r^2 = 4r\cos\theta\]
Divide by \(r\): \(r = 4\cos\theta\). (The pole is still on this curve, at \(\theta = \dfrac\pi2\), so nothing is lost.) This is a circle through the pole.

(b) \(r\sin\theta = 3\), so \(r = 3\csc\theta\) (that is, \(\dfrac{3}{\sin\theta}\)). It is a horizontal line.

(c) \(r^2\sin^2\theta = 4r\cos\theta\), so \(r = \dfrac{4\cos\theta}{\sin^2\theta}\).
:::

:::eg Find the Cartesian equation of (a) \(r = 2a\cos\theta\), (b) \(r = \dfrac{4}{1 + \cos\theta}\), (c) \(r = a\sec\theta\).
(a) Multiply by \(r\): \(r^2 = 2ar\cos\theta\), so \(x^2 + y^2 = 2ax\). Complete the square:
\[(x - a)^2 + y^2 = a^2\]
A circle, centre \((a, 0)\) and radius \(a\).

(b) Multiply out: \(r + r\cos\theta = 4\), so \(r = 4 - x\). Replace \(r\) by \(\sqrt{x^2 + y^2}\) and square:
\[x^2 + y^2 = 16 - 8x + x^2\]
so \(y^2 = 16 - 8x\), a parabola.

(c) \(r\cos\theta = a\), so \(x = a\): a vertical line.
:::

Even a simple polar equation can be a mess in Cartesian form. The cardioid \(r = 1 + \cos\theta\) becomes \((x^2 + y^2 - x)^2 = x^2 + y^2\) (multiply by \(r\) to get \(r^2 = r + r\cos\theta\), isolate \(r\) and square). That is the reason for working in polar form.

## Sketching polar curves

To sketch \(r = f(\theta)\), let \(\theta\) turn and watch the point sweep out the curve. Instead of calculating many points, answer a few questions that reveal the shape. The syllabus asks your sketch to show **symmetry, the points where the curve meets the initial line, the form of the curve at the pole and the least and greatest values of \(r\)**.

:::steps
1. **Where does the curve exist?** Because \(r \geq 0\), keep only the \(\theta\) where \(f(\theta) \geq 0\). For \(r = \cos 2\theta\) that is where \(\cos 2\theta \geq 0\), and no point is drawn elsewhere.
2. **Symmetry.** If \(f(-\theta) = f(\theta)\) the curve is symmetric about the initial line. If \(f(\pi - \theta) = f(\theta)\) it is symmetric about the line \(\theta = \dfrac\pi2\) (the \(y\)-axis).
3. **Greatest and least \(r\).** Use the range of the trigonometric function, or solve \(\dfrac{dr}{d\theta} = 0\).
4. **The pole.** Where \(r = 0\), the curve goes through the pole **tangent to the line** \(\theta = \) that value. Say so in the sketch.
5. **Intersections with the initial line** and its extension: \(\theta = 0\) and \(\theta = \pi\) (and with \(\theta = \dfrac\pi2\) if useful).
6. A short **table of values** (every \(\dfrac\pi6\) or \(\dfrac\pi4\)), then join the points smoothly in the order of increasing \(\theta\).
:::

:::key Standard polar curves (\(a > 0\))
| Equation | Curve |
|---|---|
| \(r = a\) | circle, centre the pole, radius \(a\) |
| \(\theta = \alpha\) | half-line through the pole |
| \(r = a\sec\theta\), \(r = a\csc\theta\) | the lines \(x = a\) and \(y = a\) |
| \(r = 2a\cos\theta\), \(r = 2a\sin\theta\) | circles through the pole, diameter \(2a\) along the initial line or along \(\theta = \dfrac\pi2\) |
| \(r = a(1 + \cos\theta)\) | **cardioid**: heart shape with a cusp at the pole |
| \(r = a + b\cos\theta\) | **limaçon**: no loop if \(a > b > 0\) |
| \(r = a\cos n\theta\) or \(a\sin n\theta\) | **rose** with petals |
| \(r = a\theta\) | **spiral** (Archimedean), \(\theta \geq 0\) |
| \(r = a\mathrm{e}^{k\theta}\) | **equiangular spiral**: \(r\) multiplies by a fixed factor each turn |
| \(r^2 = a^2\cos 2\theta\) | **lemniscate**: figure of eight |
:::

The widget below draws any of these. Choose a curve, drag \(\theta\) or press Play to watch the point move along the curve, and watch what the readout says when \(r\) would be negative. Then type your own equation, such as \(2\sin(3t)\), into the box.

:::html
<div class="widget" data-w="fm-polar" data-r="1+cos(t)" data-range="0,2*pi" data-presets="cardioid,circle,rose,spiral,limacon,lemniscate"></div>
:::

:::eg Sketch the cardioid \(r = a(1 + \cos\theta)\), \(0 \leq \theta < 2\pi\), where \(a > 0\).
**Existence.** \(1 + \cos\theta \geq 0\) for every \(\theta\), so \(r \geq 0\) throughout and the whole range is used.

**Symmetry.** \(\cos(-\theta) = \cos\theta\), so the curve is symmetric about the initial line.

**Greatest and least \(r\).** \(r\) is greatest, \(2a\), at \(\theta = 0\), and least, 0, at \(\theta = \pi\).

**Pole.** \(r = 0\) at \(\theta = \pi\), so the curve reaches the pole tangent to the line \(\theta = \pi\) (the \(x\)-axis): a cusp at the pole, pointing left.

**Axes.** It meets the initial line at \((2a, 0)\) and the pole. At \(\theta = \dfrac\pi2\), \(r = a\), giving \((0, a)\), and at \(\theta = \dfrac{3\pi}{2}\), \((0, -a)\).

**Table.**

| \(\theta\) | \(0\) | \(\dfrac\pi3\) | \(\dfrac\pi2\) | \(\dfrac{2\pi}{3}\) | \(\pi\) |
|---|---|---|---|---|---|
| \(r\) | \(2a\) | \(1.5a\) | \(a\) | \(0.5a\) | \(0\) |

Join the points for \(0 \leq \theta \leq \pi\) to form the upper half, a smooth curve from \((2a, 0)\) up to the left and in to the pole, then reflect it in the initial line to get the lower half.
:::

:::eg A cardioid microphone is most sensitive to sound arriving from the front and not at all to sound from directly behind. Its sensitivity to sound from a direction at angle \(\theta\) to the front is \(r = 1 + \cos\theta\), taking the greatest value as 2. For which directions is the sensitivity at least half its greatest value?
The curve \(r = 1 + \cos\theta\) is the cardioid above with \(a = 1\): its greatest value is 2 in the direction \(\theta = 0\) (the front) and it is 0 at \(\theta = \pi\) (the back).

Half the greatest value is 1. Solve \(1 + \cos\theta \geq 1\), so \(\cos\theta \geq 0\), which gives \(-\dfrac\pi2 \leq \theta \leq \dfrac\pi2\).

So the microphone has at least half its maximum sensitivity for sound from the front half-plane, within \(90^\circ\) either side of straight ahead. The cusp at the pole shows that it ignores sound from straight behind.
:::

:::eg Sketch (a) \(r = 2 + \cos\theta\) and (b) \(r = 1 + 2\cos\theta\), using the convention \(r \geq 0\).
**(a)** \(2 + \cos\theta\) is between 1 and 3, so \(r > 0\) throughout and the curve never reaches the pole. It is symmetric about the initial line, with the greatest \(r = 3\) at \(\theta = 0\), \((3, 0)\), and the least \(r = 1\) at \(\theta = \pi\), \((1, \pi)\). At \(\theta = \dfrac\pi2\), \(r = 2\). It is a smooth, egg-shaped loop (a limaçon with no inner loop and no cusp).

**(b)** \(1 + 2\cos\theta \geq 0\) needs \(\cos\theta \geq -\dfrac12\), that is \(-\dfrac{2\pi}{3} \leq \theta \leq \dfrac{2\pi}{3}\). For \(\dfrac{2\pi}{3} < \theta < \dfrac{4\pi}{3}\), \(r\) would be negative, so **nothing is drawn** there: under the convention \(r \geq 0\), the small inner loop that appears when negative \(r\) is allowed is not part of the curve. The greatest \(r = 3\) is at \(\theta = 0\). At \(\theta = \pm\dfrac{2\pi}{3}\), \(r = 0\), so the curve reaches the pole tangent to the lines \(\theta = \dfrac{2\pi}{3}\) and \(\theta = -\dfrac{2\pi}{3}\). At \(\theta = \dfrac\pi2\), \(r = 1\), giving \((0, 1)\).
:::

:::eg Sketch the curve \(r = a\cos2\theta\), \(0 \leq \theta < 2\pi\), where \(a > 0\), using the convention \(r \geq 0\).
**Existence.** \(\cos2\theta \geq 0\) when \(2\theta\) is in \(\left[-\dfrac\pi2, \dfrac\pi2\right]\) or \(\left[\dfrac{3\pi}{2}, \dfrac{5\pi}{2}\right]\), so for \(\theta\) in \(\left[0, \dfrac\pi4\right]\), \(\left[\dfrac{3\pi}{4}, \dfrac{5\pi}{4}\right]\) and \(\left[\dfrac{7\pi}{4}, 2\pi\right)\). For \(\dfrac\pi4 < \theta < \dfrac{3\pi}{4}\) and \(\dfrac{5\pi}{4} < \theta < \dfrac{7\pi}{4}\), \(r\) would be negative: no points.

**Symmetry.** \(\cos(-2\theta) = \cos2\theta\), so the curve is symmetric about the initial line; also \(\cos(2(\pi - \theta)) = \cos2\theta\), so it is symmetric about the line \(\theta = \dfrac\pi2\).

**Greatest \(r\).** \(r = a\) at \(\theta = 0\) and \(\theta = \pi\).

**Pole.** \(r = 0\) at \(\theta = \dfrac\pi4\) and \(\dfrac{3\pi}{4}\), \(\dfrac{5\pi}{4}\), \(\dfrac{7\pi}{4}\): the petals reach the pole tangent to the lines \(\theta = \pm\dfrac\pi4\).

So there are **two petals** along the initial line (the \(x\)-axis): one on the right, from \(\theta = -\dfrac\pi4\) to \(\dfrac\pi4\), reaching \((a, 0)\), and one on the left, from \(\theta = \dfrac{3\pi}{4}\) to \(\dfrac{5\pi}{4}\), reaching \((a, \pi)\). If a question restricts \(\theta\) to \(-\dfrac\pi4 \leq \theta \leq \dfrac\pi4\), only the right-hand petal is drawn.
:::

:::eg Sketch the spirals (a) \(r = a\theta\) for \(\theta \geq 0\), and (b) \(r = \mathrm{e}^{\theta/\pi}\) for \(0 \leq \theta \leq 2\pi\).
**(a)** \(r = 0\) at \(\theta = 0\), so the spiral starts at the pole, tangent to the initial line, and \(r\) grows steadily with \(\theta\): after one full turn it has reached \(r = 2\pi a\) on the initial line, after two turns \(4\pi a\), and so on. The gap between successive turns, measured along any ray, is a constant \(2\pi a\).

**(b)** \(r = \mathrm{e}^{\theta/\pi}\) never reaches 0. At \(\theta = 0\), \(r = 1\); at \(\theta = \pi\), \(r = \mathrm{e} = 2.72\); at \(\theta = 2\pi\), \(r = \mathrm{e}^2 = 7.39\). Each half-turn multiplies \(r\) by \(\mathrm{e}\) (about 2.72). The curve starts at \((1, 0)\) and winds outward with the gap between turns growing quickly.
:::

### Greatest distances, by calculus

The distance of a point from the initial line is \(y = r\sin\theta\), and its distance from the line \(\theta = \dfrac\pi2\) is \(x = r\cos\theta\). Writing \(y\) as a function of \(\theta\) and differentiating finds greatest distances.

:::key Greatest distances for \(r = f(\theta)\)
- Greatest distance from the initial line: maximise \(y = r\sin\theta = f(\theta)\sin\theta\), so solve \(\dfrac{dy}{d\theta} = 0\).
- Furthest left or right: maximise or minimise \(x = f(\theta)\cos\theta\).
- The tangent is **parallel to the initial line** where \(\dfrac{dy}{d\theta} = 0\), and **perpendicular** to it (parallel to \(\theta = \dfrac\pi2\)) where \(\dfrac{dx}{d\theta} = 0\).
- Greatest and least \(r\): solve \(\dfrac{dr}{d\theta} = 0\) (or use the range of the trigonometric function).
:::

:::eg Find the greatest distance of the cardioid \(r = a(1 + \cos\theta)\) from the initial line, and the coordinates of the point where it occurs.
\[y = r\sin\theta = a(1 + \cos\theta)\sin\theta\]
Differentiate:
\[\begin{aligned}
\frac{dy}{d\theta} &= a\left(-\sin^2\theta + (1 + \cos\theta)\cos\theta\right) \\
&= a\left(\cos\theta + \cos^2\theta - \sin^2\theta\right) \\
&= a\left(2\cos^2\theta + \cos\theta - 1\right) \\
&= a(2\cos\theta - 1)(\cos\theta + 1)
\end{aligned}\]
This is zero when \(\cos\theta = \dfrac12\) (so \(\theta = \dfrac\pi3\)) or \(\cos\theta = -1\) (the pole, where \(y = 0\)). At \(\theta = \dfrac\pi3\), \(r = \dfrac{3a}{2}\) and
\[y = \frac{3a}{2} \times \frac{\sqrt3}{2} = \frac{3\sqrt3}{4}a\]
This is a maximum, because \(y = 0\) at both ends. So the greatest distance from the initial line is \(\dfrac{3\sqrt3}{4}a\), at the point with polar coordinates \(\left(\dfrac{3a}{2}, \dfrac\pi3\right)\). By symmetry the same distance is reached below the line.
:::

## The area of a sector: \(\tfrac12\int r^2\,d\theta\)

In [Circular measure](#math.p1.circular) the area of a sector of radius \(r\) and angle \(\theta\) is \(\tfrac12r^2\theta\). For a curve whose radius changes with the angle, split the region into many thin sectors and add them up.

:::proof Why the area formula is \(\tfrac12\int r^2\,d\theta\)
Let the curve be \(r = f(\theta)\), and let \(A\) be the area swept by the radius from \(\theta = \alpha\) to \(\theta = \beta\).
1. Cut the angle into thin slices of width \(\delta\theta\).
2. A slice at angle \(\theta\) is almost a sector of radius \(r\) and angle \(\delta\theta\), so its area is about \(\tfrac12r^2\,\delta\theta\) (the sector formula).
3. Adding all the slices gives \(A \approx \sum \tfrac12 r^2\,\delta\theta\).
4. As \(\delta\theta \to 0\) the error vanishes and the sum becomes an integral.
5. So \(A = \displaystyle\int_\alpha^\beta \tfrac12 r^2\,d\theta\).
:::

:::key Area in polar coordinates
The area of the region bounded by the curve \(r = f(\theta)\) and the half-lines \(\theta = \alpha\) and \(\theta = \beta\) (\(\alpha < \beta\)), with \(r \geq 0\), is
\[A = \frac12\int_\alpha^\beta r^2\,d\theta\]
- \(\theta\) is in **radians**.
- Substitute \(r^2\) **before** integrating. Square the whole expression (\((1 + \cos\theta)^2\), not \(1 + \cos^2\theta\)).
- For the region between two curves with the same limits, \(A = \dfrac12\int_\alpha^\beta \left(r_1^2 - r_2^2\right)d\theta\), where \(r_1 \geq r_2\).
:::

Two identities do most of the work: \(\cos^2\theta = \tfrac12(1 + \cos2\theta)\) and \(\sin^2\theta = \tfrac12(1 - \cos2\theta)\), which are in MF19. A spiral usually needs integration by parts.

:::eg Find the area enclosed by the cardioid \(r = a(1 + \cos\theta)\).
The whole curve is traced for \(0 \leq \theta \leq 2\pi\), and \(r \geq 0\) throughout.
\[\begin{aligned}
A &= \frac12\int_0^{2\pi} a^2(1 + \cos\theta)^2\,d\theta \\
&= \frac{a^2}{2}\int_0^{2\pi}\left(1 + 2\cos\theta + \cos^2\theta\right)d\theta \\
&= \frac{a^2}{2}\int_0^{2\pi}\left(\tfrac32 + 2\cos\theta + \tfrac12\cos2\theta\right)d\theta
\end{aligned}\]
using \(\cos^2\theta = \tfrac12 + \tfrac12\cos2\theta\). Integrate:
\[\begin{aligned}
A &= \frac{a^2}{2}\left[\tfrac32\theta + 2\sin\theta + \tfrac14\sin2\theta\right]_0^{2\pi} \\
&= \frac{a^2}{2}\times 3\pi = \frac{3\pi a^2}{2}
\end{aligned}\]
**Check** with \(a = 1\): \(\dfrac{3\pi}{2} = 4.71\). The widget gives this value when you tick "Shade the area" and let \(\theta\) run to \(2\pi\) (see below). It is bigger than the circle of radius 1 (\(\pi\)) and smaller than the circle of radius 2 (\(4\pi\)), as it should be.
:::

Use the widget again, this time ticking "Shade the area": the shaded sector is the region swept out from \(\theta = 0\) up to the current \(\theta\), and the readout shows \(\tfrac12\int r^2\,d\theta\) for it. Run \(\theta\) to \(2\pi\) on the cardioid and check the value \(\dfrac{3\pi}{2}\); then pick the circle and check \(\pi\).

:::html
<div class="widget" data-w="fm-polar" data-r="1+cos(t)" data-range="0,2*pi" data-area="0,pi/2" data-presets="cardioid,circle,rose,spiral"></div>
:::

:::eg Find the area of one petal of \(r = a\cos2\theta\), the petal that lies along the initial line.
The petal on the right runs from \(\theta = -\dfrac\pi4\) to \(\theta = \dfrac\pi4\), where \(r\) goes from 0 to \(a\) and back to 0. By symmetry about the initial line the area is twice the area from \(0\) to \(\dfrac\pi4\):
\[\begin{aligned}
A &= 2 \times \frac12\int_0^{\pi/4} a^2\cos^22\theta\,d\theta \\
&= a^2\int_0^{\pi/4}\tfrac12(1 + \cos4\theta)\,d\theta \\
&= \frac{a^2}{2}\left[\theta + \tfrac14\sin4\theta\right]_0^{\pi/4} \\
&= \frac{a^2}{2}\times\frac\pi4 = \frac{\pi a^2}{8}
\end{aligned}\]
:::

:::eg A radar antenna detects aircraft within the region enclosed by the petal \(r = 30\cos2\theta\) kilometres, \(-\dfrac\pi4 \leq \theta \leq \dfrac\pi4\), where the antenna is at the pole and the initial line points due east. Find (a) the area of the detection region, and (b) the greatest distance north of the initial line that it reaches.
(a) From the previous example with \(a = 30\): \(A = \dfrac{\pi a^2}{8} = \dfrac{900\pi}{8} = 112.5\pi = 353\,\mathrm{km^2}\) (3 s.f.).

(b) The distance north is \(y = r\sin\theta = 30\cos2\theta\sin\theta\). Write \(\cos2\theta = 1 - 2\sin^2\theta\) and put \(s = \sin\theta\):
\[y = 30(1 - 2s^2)s = 30s - 60s^3\]
\[\frac{dy}{ds} = 30 - 180s^2 = 0 \quad\Rightarrow\quad s^2 = \tfrac16, \; s = \frac{1}{\sqrt6}\]
Then \(y = 30s(1 - 2s^2) = \dfrac{30}{\sqrt6} \times \dfrac23 = \dfrac{20}{\sqrt6} = 8.16\) km. The region reaches 8.16 km north (and 8.16 km south) of the line through the antenna: it is 16.3 km wide at its widest, and 30 km long.
:::

:::eg Find the area of the region bounded by the spiral \(r = a\theta\), \(0 \leq \theta \leq \pi\), and the initial line.
\[\begin{aligned}
A &= \frac12\int_0^\pi a^2\theta^2\,d\theta \\
&= \frac{a^2}{2}\left[\frac{\theta^3}{3}\right]_0^\pi = \frac{\pi^3a^2}{6}
\end{aligned}\]
:::

### Areas between curves, and with lines

For a region between two curves, first find where the curves meet (equate the two values of \(r\)); then work out which curve is farther from the pole between those angles; then integrate \(\tfrac12\left(r_{\text{outer}}^2 - r_{\text{inner}}^2\right)\). A sketch with both curves is essential.

:::eg The circle \(r = 3\cos\theta\) and the cardioid \(r = 1 + \cos\theta\) are drawn for \(-\dfrac\pi2 \leq \theta \leq \dfrac\pi2\). Find the exact area of the region inside the circle and outside the cardioid.
**Intersections.** \(3\cos\theta = 1 + \cos\theta\), so \(\cos\theta = \dfrac12\) and \(\theta = \pm\dfrac\pi3\). At these points \(r = \dfrac32\).

**Which is outside?** At \(\theta = 0\) the circle has \(r = 3\) and the cardioid \(r = 2\). So for \(-\dfrac\pi3 \leq \theta \leq \dfrac\pi3\) the circle is outside, and the required region lies between the two curves there. Both curves are symmetric about the initial line, so the area is twice the area for \(0 \leq \theta \leq \dfrac\pi3\):
\[\begin{aligned}
A &= 2 \times \frac12\int_0^{\pi/3}\left(9\cos^2\theta - (1 + \cos\theta)^2\right)d\theta \\
&= \int_0^{\pi/3}\left(8\cos^2\theta - 1 - 2\cos\theta\right)d\theta \\
&= \int_0^{\pi/3}\left(3 + 4\cos2\theta - 2\cos\theta\right)d\theta
\end{aligned}\]
using \(8\cos^2\theta = 4 + 4\cos2\theta\). Integrate:
\[\begin{aligned}
A &= \Big[3\theta + 2\sin2\theta - 2\sin\theta\Big]_0^{\pi/3} \\
&= \pi + 2 \times \frac{\sqrt3}{2} - 2 \times \frac{\sqrt3}{2} = \pi
\end{aligned}\]
The area is exactly \(\pi\). The surds cancel, which is a good sign.
:::

:::eg Find the area of the region inside the circle \(r = 2\) and to the right of the line \(r = \sec\theta\).
The line \(r = \sec\theta\) is \(x = 1\). It meets the circle where \(\sec\theta = 2\), so \(\cos\theta = \dfrac12\) and \(\theta = \pm\dfrac\pi3\).

For \(-\dfrac\pi3 \leq \theta \leq \dfrac\pi3\) a ray from the pole leaves the region at the circle (\(r = 2\)) and enters it at the line (\(r = \sec\theta\)). So the region lies between the line (inner) and the circle (outer):
\[\begin{aligned}
A &= \frac12\int_{-\pi/3}^{\pi/3}\left(4 - \sec^2\theta\right)d\theta = \int_0^{\pi/3}\left(4 - \sec^2\theta\right)d\theta \\
&= \Big[4\theta - \tan\theta\Big]_0^{\pi/3} = \frac{4\pi}{3} - \sqrt3
\end{aligned}\]
**Check** by geometry: the region is a circular segment cut off by the chord \(x = 1\) at distance 1 from the centre of a circle of radius 2. The segment has angle \(\dfrac{2\pi}{3}\) at the centre, so its area is \(\tfrac12 \times 4\left(\dfrac{2\pi}{3} - \sin\dfrac{2\pi}{3}\right) = \dfrac{4\pi}{3} - \sqrt3\). It agrees.
:::

:::warn The three lost marks in polar areas
**Radians.** The formula \(\tfrac12\int r^2\,d\theta\) needs \(\theta\) in radians: limits such as \(60^\circ\) must be \(\dfrac\pi3\). **Counting twice.** Limits must cover only the part of the curve that exists with \(r \geq 0\): for \(r = 3\cos\theta\) the whole circle is drawn for \(-\dfrac\pi2 \leq \theta \leq \dfrac\pi2\); integrating over \(0\) to \(2\pi\) doubles the area. When you double an area found by symmetry, check that the region really is symmetric. **The \(\tfrac12\) and the square.** Forgetting the \(\tfrac12\), or integrating \(r\) instead of \(r^2\), loses the method mark.
:::

## Exam-style examples

:::eg (Exam style) The curve \(C\) has polar equation \(r = 3 + 2\cos\theta\), \(0 \leq \theta < 2\pi\). (a) Sketch \(C\), stating the greatest and least values of \(r\). (b) Find the area enclosed by \(C\). (c) Find the greatest distance of \(C\) from the initial line, giving your answer to 3 significant figures.
**(a)** \(3 + 2\cos\theta\) lies between 1 and 5, so \(r > 0\): a smooth closed curve that does not pass through the pole. [B1]

It is symmetric about the initial line. The greatest \(r\) is 5, at \(\theta = 0\). [B1]

The least \(r\) is 1, at \(\theta = \pi\). [B1]

**(b)**
\[A = \frac12\int_0^{2\pi}(3 + 2\cos\theta)^2\,d\theta\] [M1]
Expand and use \(\cos^2\theta = \tfrac12(1 + \cos2\theta)\):
\[\begin{aligned}
A &= \frac12\int_0^{2\pi}\left(9 + 12\cos\theta + 2 + 2\cos2\theta\right)d\theta \\
&= \frac12\int_0^{2\pi}\left(11 + 12\cos\theta + 2\cos2\theta\right)d\theta
\end{aligned}\] [M1]
\[A = \frac12\Big[11\theta + 12\sin\theta + \sin2\theta\Big]_0^{2\pi}\] [A1]
\[A = \frac12 \times 22\pi = 11\pi\] [A1]
**(c)** The distance from the initial line is
\[y = (3 + 2\cos\theta)\sin\theta = 3\sin\theta + 2\sin\theta\cos\theta\] [M1]
\[\frac{dy}{d\theta} = 3\cos\theta + 2\cos2\theta\] [M1]
Put \(\dfrac{dy}{d\theta} = 0\) with \(\cos2\theta = 2\cos^2\theta - 1\):
\[4\cos^2\theta + 3\cos\theta - 2 = 0\] [A1]
\[\cos\theta = \frac{-3 + \sqrt{41}}{8} = 0.4254\] [M1]
(the other root, \(-1.175\), is impossible). Then \(\sin\theta = 0.9050\) and \(y = (3 + 2\cos\theta)\sin\theta = 3.485\) to 4 s.f. [A1]
The greatest distance from the initial line is 3.48 (3 s.f.).
:::

:::eg (Exam style) The curve \(C\) has polar equation \(r = \sqrt\theta\,\mathrm{e}^\theta\), \(0 \leq \theta \leq 1\). (a) Sketch \(C\). (b) Find, in exact form, the area of the region bounded by \(C\), the initial line and the half-line \(\theta = 1\).
**(a)** \(C\) starts at the pole when \(\theta = 0\) and \(r\) increases steadily with \(\theta\) as a curve spiralling outwards anticlockwise. [B1]

At \(\theta = 1\), \(r = \mathrm{e} = 2.72\), and at \(\theta = \dfrac12\), \(r = 0.707 \times 1.65 = 1.17\); the end point is marked at \((\mathrm{e}, 1)\). [B1]

**(b)**
\[A = \frac12\int_0^1 r^2\,d\theta = \frac12\int_0^1\theta\mathrm{e}^{2\theta}\,d\theta\] [M1 A1]
Integrate by parts with \(u = \theta\) and \(\dfrac{dv}{d\theta} = \mathrm{e}^{2\theta}\):
\[\int\theta\mathrm{e}^{2\theta}\,d\theta = \tfrac12\theta\mathrm{e}^{2\theta} - \tfrac12\int\mathrm{e}^{2\theta}\,d\theta\] [M1]
\[= \tfrac12\theta\mathrm{e}^{2\theta} - \tfrac14\mathrm{e}^{2\theta}\] [A1]
\[A = \frac12\left[\tfrac12\theta\mathrm{e}^{2\theta} - \tfrac14\mathrm{e}^{2\theta}\right]_0^1 = \frac12\left(\tfrac12\mathrm{e}^2 - \tfrac14\mathrm{e}^2 + \tfrac14\right)\] [M1]
\[A = \frac{\mathrm{e}^2 + 1}{8}\] [A1]
:::

:::eg (Exam style) The circle \(C_1\) has polar equation \(r = 4\cos\theta\), \(-\dfrac\pi2 \leq \theta \leq \dfrac\pi2\), and the line \(l\) has polar equation \(r = 3\sec\theta\). (a) Find the polar coordinates of the points where \(l\) meets \(C_1\). (b) Find, in exact form, the area of the smaller region bounded by \(C_1\) and \(l\).
**(a)** At an intersection \(4\cos\theta = 3\sec\theta\). [M1]
\[\cos^2\theta = \tfrac34, \quad \cos\theta = \frac{\sqrt3}{2}\] [A1]
(taking \(\cos\theta > 0\) on this range). So \(\theta = \pm\dfrac\pi6\) and \(r = 4\cos\dfrac\pi6 = 2\sqrt3\). [A1]

The points are \(\left(2\sqrt3, \dfrac\pi6\right)\) and \(\left(2\sqrt3, -\dfrac\pi6\right)\).

**(b)** \(l\) is the line \(x = 3\), which cuts off the small region of the circle (centre \((2, 0)\), radius 2) to its right. For \(-\dfrac\pi6 \leq \theta \leq \dfrac\pi6\), the line is the inner boundary and the circle the outer. By symmetry,
\[A = 2 \times \frac12\int_0^{\pi/6}\left(16\cos^2\theta - 9\sec^2\theta\right)d\theta\] [M1]
\[= \int_0^{\pi/6}\left(8 + 8\cos2\theta - 9\sec^2\theta\right)d\theta\] [M1]
\[= \Big[8\theta + 4\sin2\theta - 9\tan\theta\Big]_0^{\pi/6}\] [A1]
\[= \frac{4\pi}{3} + 2\sqrt3 - 3\sqrt3\] [M1]
\[A = \frac{4\pi}{3} - \sqrt3\] [A1]
**Check**: the segment is cut off at distance 1 from the centre of a circle of radius 2, so its area is \(\tfrac12 \times 4\left(\dfrac{2\pi}{3} - \dfrac{\sqrt3}{2}\right) = \dfrac{4\pi}{3} - \sqrt3\).
:::

:::board
Polar coordinates are also part of the Edexcel Further Maths Core Pure content (9FM0): converting between polar and Cartesian forms, sketching curves \(r = f(\theta)\), and the area \(\tfrac12\int r^2\,d\theta\). The notation and the formula are the same as here.
:::

:::exam What MF19 gives you
The area formula \(\tfrac12\int r^2\,d\theta\) is **not** in MF19: learn it, along with \(x = r\cos\theta\) and \(y = r\sin\theta\). The double-angle identities and the rules for integration by parts are in MF19. In "find the exact area" questions leave \(\pi\) and surds in your answer. When a question says "sketch", label the coordinates of where the curve meets the initial line and the form at the pole, and write the least and greatest values of \(r\). Say the range of \(\theta\) you used for each integral.
:::

:::eg Spot the error: the curve \(C\) has equation \(r = 3\cos\theta\), where \(r \geq 0\). Find the area enclosed by \(C\), for 5 marks.
A student wrote this answer.

Line 1: \(A = \tfrac12\int_0^{2\pi} 9\cos^2\theta\,d\theta\)
Line 2: \(= \tfrac92\int_0^{2\pi}\tfrac12(1 + \cos2\theta)\,d\theta\)
Line 3: \(= \tfrac94\left[\theta + \tfrac12\sin2\theta\right]_0^{2\pi} = \tfrac{9\pi}{2}\)

Line 1 uses the area formula with \(r^2 = 9\cos^2\theta\). [M1] Line 2 uses the double-angle identity correctly. [M1] Line 3 integrates correctly. [A1]

**The limits are wrong.** [M0] [A0] For \(\theta\) between \(\dfrac\pi2\) and \(\dfrac{3\pi}{2}\), \(\cos\theta < 0\) so \(r < 0\), and under the convention \(r \geq 0\) there are no points. The circle is traced once for \(-\dfrac\pi2 \leq \theta \leq \dfrac\pi2\), and integrating over \(0\) to \(2\pi\) counts it twice. The student scores 3 out of 5.

Correct line 3: the limits are \(-\dfrac\pi2\) to \(\dfrac\pi2\), so \(A = \tfrac94\left[\theta + \tfrac12\sin2\theta\right]_{-\pi/2}^{\pi/2} = \tfrac94\pi\). [M1] [A1]

**Check**: \(C\) is the circle with diameter 3, so its area is \(\pi\left(\tfrac32\right)^2 = \tfrac{9\pi}{4}\).
:::

:::try Start easy, finish at exam standard
Q: Convert \((-3, 3)\) to polar coordinates with \(-\pi < \theta \leq \pi\).
A: \(r = \sqrt{18} = 3\sqrt2\). The point is in the second quadrant with acute angle \(\dfrac\pi4\), so \(\theta = \pi - \dfrac\pi4 = \dfrac{3\pi}{4}\). The point is \(\left(3\sqrt2, \dfrac{3\pi}{4}\right)\).
Q: Find the Cartesian coordinates of the point \(\left(6, \dfrac{5\pi}{6}\right)\).
A: \(x = 6\cos\dfrac{5\pi}{6} = -3\sqrt3\) and \(y = 6\sin\dfrac{5\pi}{6} = 3\). The point is \((-3\sqrt3, 3)\).
Q: Write \(x^2 + y^2 = 6y\) in polar form.
A: \(r^2 = 6r\sin\theta\), so \(r = 6\sin\theta\).
Q: Find the Cartesian equation of \(r = 5\csc\theta\).
A: \(r\sin\theta = 5\), so \(y = 5\).
Q: State the least and greatest values of \(r\) on \(r = 4 + 3\cos\theta\), and where they occur.
A: Greatest \(r = 7\) at \(\theta = 0\); least \(r = 1\) at \(\theta = \pi\).
Q: Over which values of \(\theta\) in \(0 \leq \theta < 2\pi\) does \(r = 2\sin3\theta\) give points (with \(r \geq 0\))?
A: \(\sin3\theta \geq 0\) when \(3\theta\) is in \([0, \pi]\), \([2\pi, 3\pi]\) or \([4\pi, 5\pi]\), so \(\theta\) is in \(\left[0, \dfrac\pi3\right]\), \(\left[\dfrac{2\pi}{3}, \pi\right]\) or \(\left[\dfrac{4\pi}{3}, \dfrac{5\pi}{3}\right]\): three petals.
Q: Find the area enclosed by the circle \(r = 5\) using \(\tfrac12\int r^2\,d\theta\), and check it.
A: \(\tfrac12\int_0^{2\pi}25\,d\theta = 25\pi\), which is \(\pi r^2\) for \(r = 5\).
Q: Find the area of the region bounded by \(r = \theta\), \(0 \leq \theta \leq 2\), and the initial line and the half-line \(\theta = 2\).
A: \(\tfrac12\int_0^2\theta^2\,d\theta = \tfrac12 \times \dfrac83 = \dfrac43\).
Q: The curve \(r = 2\sin\theta\), \(0 \leq \theta \leq \pi\), is a circle. Find the area it encloses.
A: \(\tfrac12\int_0^\pi4\sin^2\theta\,d\theta = \int_0^\pi(1 - \cos2\theta)\,d\theta = \pi\), the area of a circle of radius 1.
Q: Find the greatest value of \(r\) on the curve \(r = 2 + \sin2\theta\) and one value of \(\theta\) where it occurs.
A: \(\sin2\theta = 1\) gives \(2\theta = \dfrac\pi2\), \(\theta = \dfrac\pi4\), and \(r = 3\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ (a) Convert the point \((-3, 3)\) to polar coordinates \((r, \theta)\) with \(r > 0\) and \(0 \leq \theta < 2\pi\). (b) Find the Cartesian equation of the curve \(r = 5\sec\theta\).
A: (a) \(r = 3\sqrt2\) [B1], \(\theta = \dfrac{3\pi}{4}\) [B1].
(b) \(r\cos\theta = 5\) [M1], so \(x = 5\). [A1]
Q: [4 marks] ★★ Find the Cartesian equation of the curve with polar equation \(r = \dfrac{4}{1 + \cos\theta}\).
A: \(r + r\cos\theta = 4\), so \(r = 4 - x\). [M1 A1]
\(x^2 + y^2 = (4 - x)^2\) [M1], so \(y^2 = 16 - 8x\). [A1]
Q: [4 marks] ★★ Sketch the curve \(r = 4\sin2\theta\), \(0 \leq \theta \leq \dfrac\pi2\), stating the greatest value of \(r\) and the direction of the tangents at the pole.
A: A single petal in the first quadrant, symmetric about \(\theta = \dfrac\pi4\). [B1]
Greatest \(r = 4\) at \(\theta = \dfrac\pi4\). [B1]
\(r = 0\) at \(\theta = 0\) and \(\theta = \dfrac\pi2\) [B1], so the tangents at the pole are the initial line and the line \(\theta = \dfrac\pi2\). [B1]
Q: [5 marks] ★★ Find the area enclosed by the curve \(r = 3 + \cos\theta\), \(0 \leq \theta < 2\pi\).
A: \(A = \dfrac12\int_0^{2\pi}(3 + \cos\theta)^2\,d\theta\) [M1]
\(= \dfrac12\int_0^{2\pi}\left(9 + 6\cos\theta + \tfrac12 + \tfrac12\cos2\theta\right)d\theta\) [M1 M1]
\(= \dfrac12\left[\tfrac{19}{2}\theta + 6\sin\theta + \tfrac14\sin2\theta\right]_0^{2\pi}\) [A1]
\(= \dfrac{19\pi}{2}\). [A1]
Q: [5 marks] ★★ The curve \(C\) has polar equation \(r = \theta^2\), \(0 \leq \theta \leq \dfrac\pi2\). Sketch \(C\) and find the area of the region bounded by \(C\) and the half-line \(\theta = \dfrac\pi2\).
A: The curve starts at the pole and spirals outward anticlockwise, ending at \(\left(\dfrac{\pi^2}{4}, \dfrac\pi2\right)\). [B1 B1]
\(A = \dfrac12\int_0^{\pi/2}\theta^4\,d\theta\) [M1] \(= \dfrac12\left[\dfrac{\theta^5}{5}\right]_0^{\pi/2}\) [A1] \(= \dfrac{\pi^5}{320}\). [A1]
Q: [6 marks] ★★ A radio mast covers the region enclosed by the three petals of \(r = 8\sin3\theta\) (in km, with \(r \geq 0\)), \(0 \leq \theta < 2\pi\). (a) State the range of \(\theta\) for the petal that lies along the line \(\theta = \dfrac\pi6\). (b) Find the area of one petal. (c) Find the total area covered.
A: (a) \(0 \leq \theta \leq \dfrac\pi3\). [B1]
(b) \(\dfrac12\int_0^{\pi/3}64\sin^23\theta\,d\theta\) [M1] \(= 32\int_0^{\pi/3}\tfrac12(1 - \cos6\theta)\,d\theta\) [M1]
\(= 16\left[\theta - \tfrac16\sin6\theta\right]_0^{\pi/3}\) [A1] \(= \dfrac{16\pi}{3}\,\mathrm{km^2}\). [A1]
(c) Three identical petals: \(16\pi = 50.3\,\mathrm{km^2}\). [B1]
Q: [11 marks] (#math.p3.trig) ★★★ The circle \(C_1\) has polar equation \(r = 2\sin\theta\), \(0 \leq \theta \leq \pi\), and the circle \(C_2\) has polar equation \(r = 1\). (a) Sketch \(C_1\) and \(C_2\) on one diagram. (b) Find the polar coordinates of the points where they meet. (c) Find, in exact form, the area of the region inside \(C_1\) and outside \(C_2\).
H: \(C_1\) is a circle of radius 1 through the pole, with its diameter along \(\theta = \dfrac\pi2\).
H: In (c), the region is symmetric about \(\theta = \dfrac\pi2\); integrate from \(\dfrac\pi6\) to \(\dfrac\pi2\) and double.
H: \(4\sin^2\theta - 1 = 1 - 2\cos2\theta\).
A: (a) \(C_2\) is a circle of radius 1 centred on the pole [B1]; \(C_1\) is a circle through the pole with diameter 2 along \(\theta = \dfrac\pi2\), reaching \(\left(2, \dfrac\pi2\right)\) [B1]; both curves on one diagram with the intersections marked. [B1]
(b) \(2\sin\theta = 1\) [M1], so \(\theta = \dfrac\pi6\) or \(\dfrac{5\pi}{6}\) [A1], with \(r = 1\) at both: \(\left(1, \dfrac\pi6\right)\) and \(\left(1, \dfrac{5\pi}{6}\right)\). [A1]
(c) For \(\dfrac\pi6 \leq \theta \leq \dfrac{5\pi}{6}\), \(C_1\) is outside \(C_2\). [M1]
\(A = 2 \times \dfrac12\int_{\pi/6}^{\pi/2}\left(4\sin^2\theta - 1\right)d\theta\) [M1]
\(= \int_{\pi/6}^{\pi/2}\left(1 - 2\cos2\theta\right)d\theta\) [A1]
\(= \Big[\theta - \sin2\theta\Big]_{\pi/6}^{\pi/2}\) [M1]
\(= \dfrac\pi2 - 0 - \left(\dfrac\pi6 - \dfrac{\sqrt3}{2}\right) = \dfrac\pi3 + \dfrac{\sqrt3}{2}\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ The curve \(L\) has equation \(r^2 = a^2\cos2\theta\), where \(a > 0\) and \(r \geq 0\), for \(0 \leq \theta < 2\pi\). (a) Find the values of \(\theta\) for which the curve exists, and sketch it. (b) Find the total area enclosed by \(L\). (c) Find the greatest distance of \(L\) from the initial line.
H: \(\cos2\theta \geq 0\) gives two ranges of \(\theta\), one around the initial line and one around \(\theta = \pi\).
H: Area of one loop: \(\tfrac12\int_{-\pi/4}^{\pi/4}a^2\cos2\theta\,d\theta\), then double.
H: \(y^2 = r^2\sin^2\theta = a^2\cos2\theta\sin^2\theta\). Let \(s = \sin^2\theta\), so \(\cos2\theta = 1 - 2s\).
A: (a) \(\cos2\theta \geq 0\) for \(-\dfrac\pi4 \leq \theta \leq \dfrac\pi4\) and \(\dfrac{3\pi}{4} \leq \theta \leq \dfrac{5\pi}{4}\). [B1] The curve is a figure of eight: one loop on each side of the pole, symmetric about both axes, passing through the pole with tangents \(\theta = \pm\dfrac\pi4\), and reaching \((a, 0)\) and \((a, \pi)\). [B1]
(b) One loop: \(\tfrac12\int_{-\pi/4}^{\pi/4}a^2\cos2\theta\,d\theta = \dfrac{a^2}{2}\left[\tfrac12\sin2\theta\right]_{-\pi/4}^{\pi/4}\) [M1] \(= \dfrac{a^2}{2}\). [A1]
Total area \(= a^2\). [A1]
(c) \(y^2 = r^2\sin^2\theta = a^2(1 - 2s)s\) with \(s = \sin^2\theta\). [M1]
\(\dfrac{d(y^2)}{ds} = a^2(1 - 4s) = 0\) gives \(s = \tfrac14\). [M1]
\(y^2 = a^2 \times \tfrac12 \times \tfrac14 = \dfrac{a^2}{8}\), so the greatest distance is \(\dfrac{a}{2\sqrt2}\). [A1]
Q: [8 marks] ★★★ The spiral \(S\) has polar equation \(r = a\theta\) for \(\theta \geq 0\). Let \(R_1\) be the region bounded by the first turn of \(S\) (\(0 \leq \theta \leq 2\pi\)) and the initial line. (a) Find the area of \(R_1\). (b) Show that the area of \(R_1\) is one third of the area of the circle with centre the pole and radius \(2\pi a\). (c) Let \(R_2\) be the region between the first turn and the second turn, bounded by the curve for \(0 \leq \theta \leq 2\pi\) and by the curve for \(2\pi \leq \theta \leq 4\pi\), and the initial line. Show that the area of \(R_2\) is six times the area of \(R_1\).
H: For (c), along the direction \(\varphi\) (with \(0 \leq \varphi \leq 2\pi\)), the inner radius is \(a\varphi\) and the outer radius is \(a(\varphi + 2\pi)\).
H: Expand \((\varphi + 2\pi)^2 - \varphi^2 = 4\pi\varphi + 4\pi^2\).
A: (a) \(A_1 = \tfrac12\int_0^{2\pi}a^2\theta^2\,d\theta\) [M1] \(= \dfrac{a^2}{2} \times \dfrac{8\pi^3}{3} = \dfrac{4\pi^3a^2}{3}\). [A1]
(b) The circle has area \(\pi(2\pi a)^2 = 4\pi^3a^2\) [B1], and \(\dfrac{4\pi^3a^2}{3} = \tfrac13 \times 4\pi^3a^2\). [A1]
(c) \(A_2 = \tfrac12\int_0^{2\pi}a^2\left[(\varphi + 2\pi)^2 - \varphi^2\right]d\varphi = \tfrac12a^2\int_0^{2\pi}\left(4\pi\varphi + 4\pi^2\right)d\varphi\) [M1]
\(= \tfrac12a^2\Big[2\pi\varphi^2 + 4\pi^2\varphi\Big]_0^{2\pi} = \tfrac12a^2\left(8\pi^3 + 8\pi^3\right)\) [M1] \(= 8\pi^3a^2\) [A1]
\(= 6 \times \dfrac{4\pi^3a^2}{3}\), six times \(A_1\). [A1]
:::

:::quiz
? What are the polar coordinates of the point \((-2, 0)\) with \(r > 0\) and \(-\pi < \theta \leq \pi\)?
- \((2, 0)\)
+ \((2, \pi)\)
- \((-2, 0)\)
- \(\left(2, \dfrac\pi2\right)\)
> The point is on the negative \(x\)-axis, 2 units from the pole, so \(r = 2\) and \(\theta = \pi\). A negative \(r\) is not used under the convention \(r \geq 0\). The option \((2, 0)\) is the point on the positive \(x\)-axis, on the initial line.
? Which is the polar form of \(x^2 + y^2 = 6x\)?
- \(r = 6\)
- \(r = 6\sin\theta\)
+ \(r = 6\cos\theta\)
- \(r = \dfrac{6}{\cos\theta}\)
> \(r^2 = 6r\cos\theta\), so \(r = 6\cos\theta\). The equation \(r = 6\sin\theta\) is the circle with its diameter on \(\theta = \dfrac\pi2\), and \(r = 6\sec\theta\) is the line \(x = 6\).
? The curve \(r = \cos2\theta\) is drawn for \(0 \leq \theta < 2\pi\) using the convention \(r \geq 0\). How many petals are drawn?
- 4
+ 2
- 1
- 8
> Points exist only where \(\cos2\theta \geq 0\), which is two of the four quarter-turns: the petals along the initial line to the right and to the left. The four-petal rose appears only if negative \(r\) is allowed.
? Which is the area of the region enclosed by \(r = 2\cos\theta\), \(-\dfrac\pi2 \leq \theta \leq \dfrac\pi2\)?
- \(2\pi\)
+ \(\pi\)
- \(4\pi\)
- \(\dfrac\pi2\)
> \(\tfrac12\int_{-\pi/2}^{\pi/2}4\cos^2\theta\,d\theta = \int_{-\pi/2}^{\pi/2}(1 + \cos2\theta)\,d\theta = \pi\), the area of a circle of radius 1. The answer \(2\pi\) comes from integrating \(r^2\) without the \(\tfrac12\); \(4\pi\) from using \(0\) to \(2\pi\) and no \(\tfrac12\).
? A student finds the area enclosed by \(r = 1 + \cos\theta\) as \(\tfrac12\int_0^{2\pi}\left(1 + \cos^2\theta\right)d\theta\). What is wrong?
- Nothing
+ The square is wrong: \(r^2 = (1 + \cos\theta)^2 = 1 + 2\cos\theta + \cos^2\theta\)
- The limits should be \(0\) to \(\pi\)
- The \(\tfrac12\) should be missing
> Squaring \(1 + \cos\theta\) gives three terms, including the cross term \(2\cos\theta\). Squaring each term separately is the algebra slip.
? At the pole, the curve \(r = 3\sin2\theta\) has \(r = 0\) at \(\theta = \dfrac\pi2\). What does this tell you?
- The curve stops there
+ The curve passes through the pole and is tangent to the line \(\theta = \dfrac\pi2\) there
- The curve has a vertical asymptote
- The curve is at its greatest distance from the pole
> A zero of \(r\) means the curve is at the pole, and the direction in which it arrives is the line \(\theta = \) that value.
:::

:::checklist What you can now do
- [ ] I can convert points and equations between Cartesian and polar form, taking care over the quadrant and the convention \(r \geq 0\).
- [ ] I can sketch simple polar curves (circles, cardioids, limaçons, roses, spirals), showing symmetry, intersections with the initial line, the form at the pole and the least and greatest \(r\).
- [ ] I can find the range of \(\theta\) for which a curve exists with \(r \geq 0\).
- [ ] I can find the greatest distance of a curve from the initial line, and where the tangent is parallel or perpendicular to it.
- [ ] I can recall and use \(\tfrac12\int r^2\,d\theta\) to find the area of a sector-shaped region.
- [ ] I can use symmetry and double-angle identities to find the area of a loop or petal.
- [ ] I can find the area between two curves, or between a curve and a line, after finding the intersections.
- [ ] I can integrate by parts to find the area enclosed by a spiral.
:::

:::recap
- \(x = r\cos\theta\), \(y = r\sin\theta\), \(r^2 = x^2 + y^2\), \(\tan\theta = \dfrac yx\) with the quadrant checked. \(r \geq 0\); \(\theta\) in radians.
- To convert equations, substitute; multiply a polar equation by \(r\) to make \(r\cos\theta\), \(r\sin\theta\) or \(r^2\) appear.
- Sketching: where \(r \geq 0\), symmetry, greatest and least \(r\), \(r = 0\) (tangent at the pole), intersections with the initial line.
- Standard curves: \(r = 2a\cos\theta\) circle; \(r = a(1 + \cos\theta)\) cardioid; \(r = a\cos n\theta\) rose; \(r = a\theta\) and \(r = a\mathrm{e}^{k\theta}\) spirals.
- Greatest distance from the initial line: maximise \(r\sin\theta\).
- Area: \(\tfrac12\int_\alpha^\beta r^2\,d\theta\), with \(\theta\) in radians and only where \(r \geq 0\). Between curves: \(\tfrac12\int\left(r_1^2 - r_2^2\right)d\theta\).
- Common lost marks: degrees, forgetting \(\tfrac12\) or the square, and double-counting a curve traced with \(r < 0\).
:::

:::links
- read: [Polar coordinates](https://tutorial.math.lamar.edu/Classes/CalcII/PolarCoordinates.aspx) · Paul's Online Notes · conversions and sketching standard curves
- read: [Area with polar coordinates](https://tutorial.math.lamar.edu/Classes/CalcII/PolarArea.aspx) · Paul's Online Notes · areas of loops and between curves
- watch: [Area bounded by a polar curve](https://www.examsolutions.net/tutorials/area-bounded-polar-curve/) · ExamSolutions · a worked area question
- practise: [Polar coordinates](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:polar) · Khan Academy · conversions and graphs
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · type r = 1 + cos(theta) and other polar equations
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Vectors: the vector product and planes](#math.fm.vectors) extends vectors to three dimensions with the vector product and the equation of a plane.
