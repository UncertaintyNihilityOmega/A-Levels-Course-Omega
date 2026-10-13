@chapter math.p1.integ
@title Integration
@level as
@paper CAIE P1 · Edexcel IAL P1–P2 · AQA/OCR/Edexcel Pure Year 1
@time 8–10 hours
@summary Integration as the reverse of differentiation, the constant of integration, integrals of \((ax + b)^n\), definite integrals, areas under curves and between curves, simple improper integrals, and volumes of revolution about either axis.

:::why
Differentiation breaks a quantity into its rate of change. Integration goes the other way: from a rate back to the total, from a gradient back to a curve, and from a curve to the area under it. Distance from speed, volume from flow rate and profit from marginal cost are all integrals. In Paper 1 integration also builds areas and solids of revolution, and the same skills carry on into [Further integration](#math.p3.integ) in Papers 2 and 3.
:::

**Before you start**, you need fractional and negative indices from [Indices, surds and standard form](#math.f.powers) and the rules of [Differentiation](#math.p1.diff). Integration is differentiation run backwards, so every answer can be checked by differentiating it.

:::try Warm-up
Q: Differentiate \(y = x^3 - 6x^2\). (from [Differentiation](#math.p1.diff))
A: \(\dfrac{dy}{dx} = 3x^2 - 12x\).
Q: Write \(\dfrac{6}{\sqrt{x}}\) as a power of \(x\). (from [Indices, surds and standard form](#math.f.powers))
A: \(6x^{-1/2}\).
Q: Solve \(x^2 - 5x + 6 = 0\). (from [Quadratics](#math.p1.quadratics))
A: \((x - 2)(x - 3) = 0\), so \(x = 2\) or \(x = 3\).
:::

## Reversing differentiation

If \(\dfrac{dy}{dx} = 3x^2\), then \(y = x^3\) is one answer. But \(x^3 + 5\) and \(x^3 - 2\) also differentiate to \(3x^2\), because the derivative of a constant is zero. So a whole family of curves has the same gradient function, and they differ only by a constant.

:::def Integration
Integration is the reverse of differentiation. The **indefinite integral** of \(f(x)\), written \(\displaystyle\int f(x)\,dx\), is every function whose derivative is \(f(x)\). It always includes an arbitrary constant \(c\), the **constant of integration**.
:::

To differentiate \(x^n\) you multiply by \(n\) and reduce the power by one. To integrate you do the opposite, in the opposite order: increase the power by one, then divide by the new power.

:::key Integrating powers of \(x\)
\[\int x^n\,dx = \frac{x^{n+1}}{n+1} + c \qquad (n \ne -1)\]
\[\int k\,f(x)\,dx = k\int f(x)\,dx \qquad \int \big(f(x) + g(x)\big)\,dx = \int f(x)\,dx + \int g(x)\,dx\]
This works for every rational \(n\) except \(-1\) (the integral of \(\tfrac1x\) is a logarithm, see [Logarithms and exponentials](#math.p3.logs)). A constant \(k\) integrates to \(kx\), since \(k = kx^0\). MF19 lists \(\int x^n\,dx\), but not the rule for \((ax + b)^n\) below. Never forget \(+\,c\).
:::

Integrate each term separately. As in differentiation, rewrite roots and fractions as powers of \(x\) first (see [Indices, surds and standard form](#math.f.powers)), and expand brackets that are products.

:::eg Find (a) \(\displaystyle\int (3x^2 - 4x + 5)\,dx\), (b) \(\displaystyle\int \left(\sqrt{x} + \frac{3}{x^2}\right)dx\), (c) \(\displaystyle\int (x + 2)(x - 3)\,dx\)
(a) Raise each power by one and divide by the new power:
\[\int (3x^2 - 4x + 5)\,dx = \frac{3x^3}{3} - \frac{4x^2}{2} + 5x + c = x^3 - 2x^2 + 5x + c\]
(b) Write \(\sqrt{x} = x^{1/2}\) and \(\dfrac{3}{x^2} = 3x^{-2}\):
\[\int \left(x^{1/2} + 3x^{-2}\right)dx = \frac{x^{3/2}}{3/2} + \frac{3x^{-1}}{-1} + c = \tfrac23 x^{3/2} - \frac{3}{x} + c\]
(c) Expand first: \((x + 2)(x - 3) = x^2 - x - 6\), so the integral is \(\dfrac{x^3}{3} - \dfrac{x^2}{2} - 6x + c\).
Check (a) by differentiating: \(3x^2 - 4x + 5\). ✓
:::

:::warn The most common slips
- Missing \(+\,c\) in an indefinite integral. This costs a mark every time.
- Dividing by the old power instead of the new one: \(\int x^3\,dx = \dfrac{x^4}{4}\), not \(\dfrac{x^4}{3}\).
- Integrating a product or a quotient term by term: \(\int (x + 2)(x - 3)\,dx\) is **not** \(\frac{x^2}{2} \times \ldots\). Expand first.
- With negative powers, \(\int x^{-2}\,dx = -x^{-1}\), not \(x^{-1}\). The sign comes from dividing by \(-1\).
:::

## Integrating \((ax + b)^n\)

The chain rule says that \(\dfrac{d}{dx}(ax + b)^{n+1} = a(n+1)(ax + b)^n\). The \(a\) comes from differentiating the bracket. To undo it, divide by \(a\) as well as by the new power.

:::key Integral of \((ax + b)^n\)
\[\int (ax + b)^n\,dx = \frac{(ax + b)^{n+1}}{a(n + 1)} + c \qquad (n \ne -1)\]
In words: raise the power by one, then divide by the new power **and** by the coefficient of \(x\) inside the bracket. This applies to a **linear** bracket only.
:::

:::eg Find (a) \(\displaystyle\int (2x + 3)^4\,dx\), (b) \(\displaystyle\int \frac{6}{(3 - x)^2}\,dx\), (c) \(\displaystyle\int (4x - 1)^{-1/2}\,dx\)
(a) \(\dfrac{(2x + 3)^5}{5 \times 2} + c = \dfrac{(2x + 3)^5}{10} + c\).

(b) Write \(6(3 - x)^{-2}\). Here \(a = -1\) and the new power is \(-1\), so the divisor is \((-1)(-1) = 1\):
\[\int 6(3 - x)^{-2}\,dx = \frac{6(3 - x)^{-1}}{1} + c = \frac{6}{3 - x} + c\]
(c) The new power is \(\tfrac12\) and \(a = 4\), so the divisor is \(4 \times \tfrac12 = 2\): \(\dfrac{(4x - 1)^{1/2}}{2} + c = \tfrac12\sqrt{4x - 1} + c\).
Check (a): \(\dfrac{d}{dx}\dfrac{(2x + 3)^5}{10} = \dfrac{5 \times 2(2x + 3)^4}{10} = (2x + 3)^4\). ✓
:::

:::warn The division by \(a\)
\(\int (2x + 3)^4\,dx\) is \(\dfrac{(2x+3)^5}{10}\), not \(\dfrac{(2x+3)^5}{5}\). The check is quick: differentiate your answer and see whether the chain rule factor \(2\) cancels. This does **not** work for \(\int (x^2 + 1)^4\,dx\) or any bracket that is not linear.
:::

## Finding the constant

When a question gives a point on the curve, you can find the particular value of \(c\).

:::eg The gradient of a curve is \(\dfrac{dy}{dx} = 6x^2 - 4\) and the curve passes through \((1, 5)\). Find its equation. A second curve has \(\dfrac{dy}{dx} = 6(2x - 1)^{1/2}\) and passes through \((5, 20)\); find its equation.
Integrate: \(y = 2x^3 - 4x + c\). Substitute \((1, 5)\): \(5 = 2 - 4 + c\), so \(c = 7\). The curve is \(y = 2x^3 - 4x + 7\).

For the second, \(y = \dfrac{6(2x - 1)^{3/2}}{2 \times \frac32} + c = 2(2x - 1)^{3/2} + c\). At \((5, 20)\): \(20 = 2(9)^{3/2} + c = 54 + c\), so \(c = -34\). The curve is \(y = 2(2x - 1)^{3/2} - 34\).
:::

The same idea works for a second derivative: integrate twice and use two conditions to find two constants. Also, in applications such as the flow rate of a tank, \(\dfrac{dV}{dt}\) integrates to \(V\), and the starting volume gives \(c\).

:::eg Water leaks from a tank at a rate of \(\dfrac{dV}{dt} = -(20 - 2t)\) litres per minute for \(0 \le t \le 10\), and the tank holds \(150\) litres at \(t = 0\). Find \(V\) in terms of \(t\) and the volume at \(t = 5\).
\[V = -\int (20 - 2t)\,dt = -(20t - t^2) + c = t^2 - 20t + c\]
When \(t = 0\), \(V = 150\), so \(c = 150\) and \(V = t^2 - 20t + 150\). At \(t = 5\): \(V = 25 - 100 + 150 = 75\) litres.
:::

## Definite integrals

A definite integral has limits and gives a number, not a function. Integrate, put in the upper limit, put in the lower limit, and subtract. The constant \(c\) cancels, so it is not needed.

:::key Definite integral
\[\int_a^b f(x)\,dx = \Big[F(x)\Big]_a^b = F(b) - F(a)\]
where \(F\) is any integral of \(f\). Reversing the limits changes the sign: \(\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx\).
:::

:::eg Evaluate (a) \(\displaystyle\int_1^3 (2x + 1)\,dx\), (b) \(\displaystyle\int_1^4 \sqrt{x}\,dx\)
(a) \(\Big[x^2 + x\Big]_1^3 = (9 + 3) - (1 + 1) = 10\).

(b) \(\Big[\tfrac23 x^{3/2}\Big]_1^4 = \tfrac23(8) - \tfrac23(1) = \dfrac{14}{3}\).
:::

## Area under a curve

If \(y = f(x)\) is above the \(x\)-axis for \(a \le x \le b\), the area between the curve, the \(x\)-axis and the lines \(x = a\) and \(x = b\) is \(\displaystyle\int_a^b y\,dx\).

:::plot The area under \(y = x^2 + 1\) between \(x = 1\) and \(x = 3\) is \(\int_1^3 (x^2 + 1)\,dx = \tfrac{32}{3}\).
--f "x**2+1" --label "y = x² + 1" --x -0.5 4 --y -1 11 --shade "0,1,3" --legend tl
:::

To see why an area is a limit of thin strips, use the strips below: more strips give a better estimate, and the exact area is the value of the integral.

:::html
<div class="widget" data-w="area" data-f="x^2 + 1" data-x="1,3" data-n="4" data-mode="riemann"></div>
:::

:::proof Why integration gives area, and why it reverses differentiation
Let \(A(x)\) be the area under the curve \(y = f(x)\) from a fixed starting point \(a\) up to \(x\). As \(x\) increases, \(A(x)\) grows.

Move from \(x\) to \(x + h\). The area added is a thin strip of width \(h\) whose height is close to \(f(x)\), so
\[A(x + h) - A(x) \approx f(x) \times h\]
Divide by \(h\):
\[\frac{A(x + h) - A(x)}{h} \approx f(x)\]
As \(h \to 0\) the strip gets thinner and the approximation gets exact. The left side becomes the derivative of \(A\), so
\[A'(x) = f(x)\]
The area function is an integral of \(f\): \(A(x) = F(x) + c\) for any \(F\) with \(F' = f\). At the start \(A(a) = 0\), which fixes \(c = -F(a)\). The area up to \(b\) is
\[A(b) = F(b) - F(a)\]
That is the rule for a definite integral.

:::html
<div class="widget" data-w="proof" data-proof="ftc"></div>
:::
:::

:::eg Find the area bounded by \(y = x^2 + 1\), the \(x\)-axis and the lines \(x = 1\) and \(x = 3\).
\[\int_1^3 (x^2 + 1)\,dx = \Big[\tfrac{x^3}{3} + x\Big]_1^3 = (9 + 3) - \left(\tfrac13 + 1\right) = \tfrac{32}{3}\]
The area is \(\tfrac{32}{3}\) square units.
:::

### Areas below the axis

Where a curve is below the \(x\)-axis, \(y\) is negative, so the integral is negative. An area is never negative. When a curve crosses the axis between the limits, **split the integral at each root**, and take the size (the absolute value) of each part.

:::plot The curve \(y = x^2 - 4x + 3\) crosses the x-axis at \(x = 1\) and \(x = 3\). The area from 0 to 1 is above the axis, and the area from 1 to 3 is below it.
--f "x**2-4*x+3" --label "y = x² − 4x + 3" --x -0.5 4 --y -2 4.5 --shade "0,0,3" --pt "1,0,(1, 0)@ne" --pt "3,0,(3, 0)@ne" --legend tr
:::

:::eg Find the total area enclosed between the curve \(y = x^2 - 4x + 3\), the \(x\)-axis, and the lines \(x = 0\) and \(x = 3\).
The roots are \(x = 1\) and \(x = 3\) from \((x - 1)(x - 3) = 0\). An integral of \(F(x) = \tfrac{x^3}{3} - 2x^2 + 3x\):
\[\int_0^1 y\,dx = F(1) - F(0) = \tfrac43 - 0 = \tfrac43 \qquad \int_1^3 y\,dx = F(3) - F(1) = 0 - \tfrac43 = -\tfrac43\]
The second area is below the axis, so its size is \(\tfrac43\). The total area is \(\tfrac43 + \tfrac43 = \tfrac83\).
Warning: the single integral \(\int_0^3 y\,dx = 0\) because the positive and negative parts cancel, but the area is not zero.
:::

A related case integrates with respect to \(y\). The area between a curve, the \(y\)-axis and the lines \(y = c\) and \(y = d\) is \(\displaystyle\int_c^d x\,dy\), with \(x\) written as a function of \(y\). For example, the region bounded by \(y = x^2\), the \(y\)-axis and \(y = 4\) has \(x = \sqrt{y}\), so area \(= \displaystyle\int_0^4 y^{1/2}\,dy = \tfrac23(8) = \tfrac{16}{3}\).

## Area between two graphs

To find the area between a curve and a line, or between two curves, find where they cross, then integrate **top minus bottom**.

:::steps
1. Set the equations equal and solve for the \(x\)-values of the intersections.
2. Sketch, and decide which graph is above in between.
3. Area \(= \displaystyle\int_a^b (y_{\text{top}} - y_{\text{bottom}})\,dx\).
:::

The picture below shades the region enclosed by the line \(y = 2x + 3\) and the curve \(y = x^2\), and works out its area from the two functions. The line is the upper curve between the crossing points, so the area is the integral of "top minus bottom".

:::html
<div class="widget" data-w="graph" data-fns="2*x + 3; x^2" data-x="-2,4" data-y="-1,12" data-shade-between="2*x + 3; x^2"></div>
:::

:::eg Find the area enclosed by the line \(y = 2x + 3\) and the curve \(y = x^2\).
Solve \(x^2 = 2x + 3\): \(x^2 - 2x - 3 = 0\), so \(x = -1\) or \(x = 3\). Between these, the line is above the parabola.
\[\int_{-1}^{3} (2x + 3 - x^2)\,dx = \Big[x^2 + 3x - \tfrac{x^3}{3}\Big]_{-1}^{3} = 9 - \left(-\tfrac53\right) = \tfrac{32}{3}\]
The area is \(\tfrac{32}{3}\).
Check the values: at \(x = 3\) the bracket is \(9 + 9 - 9 = 9\); at \(x = -1\) it is \(1 - 3 + \tfrac13 = -\tfrac53\). ✓
:::

:::eg Find the area enclosed between \(y = \sqrt{x}\) and \(y = x^2\).
The curves meet where \(\sqrt{x} = x^2\), so \(x = 0\) or \(x = 1\). Between 0 and 1, \(\sqrt{x}\) is above \(x^2\) (at \(x = \tfrac14\): \(0.5 > 0.0625\)).
\[\int_0^1 \left(x^{1/2} - x^2\right)dx = \Big[\tfrac23 x^{3/2} - \tfrac{x^3}{3}\Big]_0^1 = \tfrac23 - \tfrac13 = \tfrac13\]
:::

## Improper integrals

A definite integral is **improper** if one limit is infinite, or if the integrand is not defined at an end of the interval. Cambridge asks for simple cases. Replace the problem limit with a letter, integrate, then see what happens as the letter approaches the limit.

:::key Improper integrals
- Infinite limit: \(\displaystyle\int_1^\infty f(x)\,dx = \lim_{t \to \infty}\int_1^t f(x)\,dx\). For a power \(x^{n}\), if \(n < -1\) the term \(t^{n+1} \to 0\), and the integral exists; if \(n > -1\) the term grows and the integral does not exist (it **diverges**).
- Undefined at a limit: \(\displaystyle\int_0^1 f(x)\,dx = \lim_{t \to 0^+}\int_t^1 f(x)\,dx\). For \(x^{n}\) with \(-1 < n < 0\) this converges, as \(t^{n+1} \to 0\).
:::

:::eg Evaluate (a) \(\displaystyle\int_1^\infty x^{-2}\,dx\), (b) \(\displaystyle\int_0^1 x^{-1/2}\,dx\), and show that (c) \(\displaystyle\int_1^\infty x^{-1/2}\,dx\) does not exist.
(a) \(\displaystyle\int_1^t x^{-2}\,dx = \Big[-x^{-1}\Big]_1^t = -\frac1t + 1\). As \(t \to \infty\), \(\frac1t \to 0\), so the integral equals \(1\).

(b) \(x^{-1/2}\) is undefined at \(0\). \(\displaystyle\int_t^1 x^{-1/2}\,dx = \Big[2x^{1/2}\Big]_t^1 = 2 - 2\sqrt{t}\). As \(t \to 0^+\), \(2\sqrt t \to 0\), so the integral equals \(2\).

(c) \(\displaystyle\int_1^t x^{-1/2}\,dx = \Big[2x^{1/2}\Big]_1^t = 2\sqrt{t} - 2\). As \(t \to \infty\) this grows without limit, so the integral does not exist.
:::

:::eg (Exam style) Find the exact value of \(\displaystyle\int_9^\infty 4x^{-3/2}\,dx\).
\[\int_9^t 4x^{-3/2}\,dx = \Big[-8x^{-1/2}\Big]_9^t = -\frac{8}{\sqrt t} + \frac{8}{3}\] [M1 A1]
As \(t \to \infty\), \(\dfrac{8}{\sqrt t} \to 0\), [M1] so the integral equals \(\dfrac83\). [A1]
:::

## Volumes of revolution

When a region is rotated through \(360^\circ\) (\(2\pi\) radians) about an axis, it sweeps out a solid. Slice the solid into thin discs. For rotation about the \(x\)-axis, a disc at position \(x\) has radius \(y\) and thickness \(dx\), so its volume is \(\pi y^2\,dx\).

:::key Volume of revolution
About the \(x\)-axis (from \(x = a\) to \(x = b\)): \(\displaystyle V = \pi\int_a^b y^2\,dx\)

About the \(y\)-axis (from \(y = c\) to \(y = d\)): \(\displaystyle V = \pi\int_c^d x^2\,dy\)
Square the **function** before integrating (\(y^2\) is not \(2y\)); the factor \(\pi\) stays outside. These are not on MF19.
:::

:::proof Why the volume of revolution is π∫y² dx
Cut the solid into thin slices, each of thickness \(\delta x\), by planes at right angles to the \(x\)-axis. Each slice is almost a cylinder. At position \(x\) its radius is \(y\), the distance from the axis to the curve.

The volume of a cylinder is \(\pi r^2 h\), so the volume of the slice is about \(\pi y^2\,\delta x\). Adding all the slices from \(x = a\) to \(x = b\):
\[V \approx \sum \pi y^2\,\delta x\]
As the slices get thinner the approximation gets better, and the sum becomes the integral
\[V = \pi\int_a^b y^2\,dx\]
The discs below show the same thing. Increase the number of discs and watch the stack's volume close in on the exact value.

:::html
<div class="widget" data-w="proof" data-proof="discs"></div>
:::
:::

:::eg The region under \(y = x^2\) for \(0 \le x \le 2\) is rotated about the \(x\)-axis. Find the volume. The region bounded by \(y = x^2\), the \(y\)-axis and \(y = 4\) is rotated about the \(y\)-axis. Find the volume.
About the \(x\)-axis: \(V = \pi\displaystyle\int_0^2 x^4\,dx = \pi\Big[\tfrac{x^5}{5}\Big]_0^2 = \tfrac{32\pi}{5} = 20.1\) (3 s.f.).

About the \(y\)-axis: \(x^2 = y\), so \(V = \pi\displaystyle\int_0^4 y\,dy = \pi\Big[\tfrac{y^2}{2}\Big]_0^4 = 8\pi = 25.1\) (3 s.f.).
Check with a cone: rotating \(y = 2x\) for \(0 \le x \le 3\) gives \(\pi\int_0^3 4x^2\,dx = 36\pi\), the volume of a cone with \(r = 6\), \(h = 3\), since \(\tfrac13\pi(36)(3) = 36\pi\). ✓
:::

Here is the solid from the first part, built from discs. Increase the number of discs and compare the stack's volume with the exact value \(\dfrac{32\pi}{5}\).

:::html
<div class="widget" data-w="area" data-f="x^2" data-x="0,2" data-n="6" data-mode="volume"></div>
:::

If the region is **not bounded by the axis** you rotate about, the solid has a hole. Use the outer curve squared minus the inner curve squared (the washer method).

:::eg The region between \(y = 9 - x^2\) and the line \(y = 5\) is rotated about the \(x\)-axis. Find the volume.
The curves meet where \(9 - x^2 = 5\), so \(x = \pm 2\). The curve is above the line in between, so for each \(x\) the outer radius is \(9 - x^2\) and the inner radius is \(5\):
\[V = \pi\int_{-2}^{2}\left[(9 - x^2)^2 - 5^2\right]dx = \pi\int_{-2}^{2}\left(56 - 18x^2 + x^4\right)dx\]
The integrand is even, so double the integral from 0 to 2:
\[V = 2\pi\Big[56x - 6x^3 + \tfrac{x^5}{5}\Big]_0^2 = 2\pi\left(112 - 48 + \tfrac{32}{5}\right) = \tfrac{704\pi}{5} = 442 \text{ (3 s.f.)}\]
:::

:::warn Volume slips
Do not subtract first and then square: \(\pi\int (y_1 - y_2)^2\,dx\) is wrong. The correct form is \(\pi\int (y_1^2 - y_2^2)\,dx\). Do not forget \(\pi\), and square the whole expression \((9 - x^2)\), including the cross term \(-18x^2\).
:::

## Exam questions

:::eg (Exam style) The curve \(y = 6x - x^2\) and the line \(y = 2x\) enclose a region \(R\). (a) Find the coordinates of the points of intersection. (b) Find the area of the region enclosed. (c) Find the volume generated when this region is rotated through \(360^\circ\) about the \(x\)-axis, giving the answer to 3 significant figures.
**(a)** \(6x - x^2 = 2x \implies x^2 - 4x = 0 \implies x = 0\) or \(x = 4\). [M1 A1] The points are \((0, 0)\) and \((4, 8)\). [A1]

**(b)** The curve is above the line between the points: top minus bottom is \(4x - x^2\). [M1]
\[\text{Area} = \int_0^4 (4x - x^2)\,dx = \Big[2x^2 - \tfrac{x^3}{3}\Big]_0^4 = 32 - \tfrac{64}{3} = \tfrac{32}{3}\] [M1 A1]

**(c)** Outer radius \(6x - x^2\), inner radius \(2x\):
\[V = \pi\int_0^4\left[(6x - x^2)^2 - (2x)^2\right]dx = \pi\int_0^4\left(32x^2 - 12x^3 + x^4\right)dx\] [M1 A1]
\[= \pi\Big[\tfrac{32x^3}{3} - 3x^4 + \tfrac{x^5}{5}\Big]_0^4 = \pi\left(\tfrac{2048}{3} - 768 + \tfrac{1024}{5}\right) = \tfrac{1792\pi}{15}\] [M1]
\[V = 375 \text{ (3 s.f.)}\] [A1]
:::

:::eg (Exam style) A curve passes through \(P(4, 10)\) and has gradient \(\dfrac{dy}{dx} = 3\sqrt{x} - \dfrac{4}{x^2}\). (a) Find the equation of the curve. (b) Find the change in \(y\) as \(x\) increases from \(1\) to \(4\).
**(a)** \(\dfrac{dy}{dx} = 3x^{1/2} - 4x^{-2}\), so \(y = 3 \times \tfrac23 x^{3/2} - 4 \times \dfrac{x^{-1}}{-1} + c = 2x^{3/2} + \dfrac4x + c\). [M1 A1]
At \(P\): \(10 = 2(8) + 1 + c\), so \(c = -7\). [M1] The curve is \(y = 2x^{3/2} + \dfrac4x - 7\). [A1]

**(b)** The change in \(y\) is the definite integral of the gradient, \(y(4) - y(1) = 10 - (2 + 4 - 7) = 10 - (-1) = 11\). [M1 A1]
:::

:::exam What earns marks
- Show the integrated form **before** substituting limits, with square brackets. A bare number gets the answer mark only if it is right.
- For an area between graphs, sketch and state which is on top. Mark schemes give a mark for the correct difference.
- For volumes, write the integral \(\pi\int y^2\,dx\) with the limits, then expand \(y^2\) fully before integrating. An exact answer with \(\pi\) is better than a decimal unless asked.
- If a question says "show that the area is …" every step must be present.
:::

:::board Other boards
Edexcel IAL covers integration of powers in P1 and definite integrals and areas in P2; check its specification for volumes of revolution and improper integrals. UK A Levels (AQA, Edexcel, OCR) include integration of powers, definite integrals and areas in Pure Year 1. Volumes of revolution and improper integrals are in UK Further Maths, so a student on a UK Maths A Level can skip those two sections.
:::

:::eg Spot the error: the region under \(y = x + 1\) for \(0 \le x \le 2\) is rotated through \(360^\circ\) about the \(x\)-axis. Find the volume.
A student wrote this answer.

Line 1: \(V = \pi\displaystyle\int_0^2 y^2\,dx = \pi\int_0^2 (x^2 + 1)\,dx\)
Line 2: \(= \pi\Big[\tfrac{x^3}{3} + x\Big]_0^2\)
Line 3: \(= \pi\left(\tfrac83 + 2\right) = \tfrac{14\pi}{3} = 14.7\)

The formula \(V = \pi\int y^2\,dx\) and the limits are correct [M1]. **Line 1 loses the next marks [A0 A0]:** \((x + 1)^2\) is not \(x^2 + 1\). Squaring a bracket means multiplying it by itself: \((x + 1)^2 = x^2 + 2x + 1\). The middle term has been lost.

Correct working: \(V = \pi\displaystyle\int_0^2 (x + 1)^2\,dx = \pi\Big[\tfrac{(x + 1)^3}{3}\Big]_0^2\) [A1] \(= \pi\left(\tfrac{27}{3} - \tfrac13\right) = \tfrac{26\pi}{3} = 27.2\). [A1]

**Check:** rotating \(y = x + 1\) gives a cone with a flat top removed (a frustum), with radii 1 and 3 and height 2. Its volume is \(\tfrac13\pi \times 2 \times (1 + 3 + 9) = \tfrac{26\pi}{3}\), which agrees.
:::

:::try Start easy, finish at exam standard
Q: Find (a) \(\displaystyle\int (4x^3 - 6x + 1)\,dx\), (b) \(\displaystyle\int \left(\frac{2}{x^3} + \sqrt{x}\right)dx\).
A: (a) \(x^4 - 3x^2 + x + c\). (b) \(\displaystyle\int (2x^{-3} + x^{1/2})\,dx = -x^{-2} + \tfrac23 x^{3/2} + c = -\dfrac{1}{x^2} + \tfrac23 x^{3/2} + c\).
Q: Find \(\displaystyle\int (3x - 1)^5\,dx\) and \(\displaystyle\int \frac{1}{\sqrt{2x + 5}}\,dx\).
A: \(\dfrac{(3x - 1)^6}{18} + c\). Second: \((2x + 5)^{-1/2}\) integrates to \(\dfrac{(2x + 5)^{1/2}}{2 \times \frac12} = \sqrt{2x + 5} + c\).
Q: Given \(\dfrac{dy}{dx} = 4x - 3\) and \(y = 6\) when \(x = 2\), find \(y\) in terms of \(x\).
A: \(y = 2x^2 - 3x + c\). Then \(6 = 8 - 6 + c\), so \(c = 4\) and \(y = 2x^2 - 3x + 4\).
Q: Evaluate \(\displaystyle\int_0^2 (3x^2 - 2x)\,dx\) and \(\displaystyle\int_1^4 \frac{1}{x^2}\,dx\).
A: First: \(\Big[x^3 - x^2\Big]_0^2 = 8 - 4 = 4\). Second: \(\Big[-x^{-1}\Big]_1^4 = -\tfrac14 + 1 = \tfrac34\).
Q: Find the area enclosed by \(y = x(4 - x)\) and the \(x\)-axis.
A: Roots at \(0\) and \(4\). \(\displaystyle\int_0^4 (4x - x^2)\,dx = \Big[2x^2 - \tfrac{x^3}{3}\Big]_0^4 = 32 - \tfrac{64}{3} = \tfrac{32}{3}\).
Q: Find the area enclosed by \(y = x^2 - 2x - 3\) and the \(x\)-axis. Explain why \(\displaystyle\int_{-1}^{3} y\,dx\) is negative.
A: The roots are \(-1\) and \(3\). \(\displaystyle\int_{-1}^{3}(x^2 - 2x - 3)\,dx = \Big[\tfrac{x^3}{3} - x^2 - 3x\Big]_{-1}^{3} = -9 - \tfrac53 = -\tfrac{32}{3}\). The curve is below the axis between the roots, so \(y < 0\) and the integral is negative. The area is \(\tfrac{32}{3}\).
Q: Find the area between the curve \(y = x^2\) and the line \(y = x + 6\).
A: \(x^2 = x + 6\) gives \(x = -2\) or \(3\). \(\displaystyle\int_{-2}^{3}(x + 6 - x^2)\,dx = \Big[\tfrac{x^2}{2} + 6x - \tfrac{x^3}{3}\Big]_{-2}^{3} = \tfrac{27}{2} - \left(-\tfrac{22}{3}\right) = \tfrac{125}{6}\).
Q: Find (a) \(\displaystyle\int_1^\infty 3x^{-4}\,dx\), (b) \(\displaystyle\int_0^4 x^{-1/2}\,dx\).
A: (a) \(\Big[-x^{-3}\Big]_1^\infty = 0 - (-1) = 1\). (b) \(\Big[2x^{1/2}\Big]_0^4 = 4\), with the limit as the lower end tends to \(0\).
Q: The region under \(y = \sqrt{x}\) for \(0 \le x \le 4\) is rotated about the \(x\)-axis. Find the exact volume. Then find the volume formed by rotating the region between \(y = x\) and \(y = x^2\) about the \(x\)-axis.
A: \(V = \pi\displaystyle\int_0^4 x\,dx = \pi\Big[\tfrac{x^2}{2}\Big]_0^4 = 8\pi\). For the second the curves meet at \(0\) and \(1\) with \(y = x\) above: \(V = \pi\displaystyle\int_0^1 (x^2 - x^4)\,dx = \pi\left(\tfrac13 - \tfrac15\right) = \tfrac{2\pi}{15}\).
Q: (Exam style) The curve \(y = \dfrac{12}{x^2}\) is shown for \(x > 0\). The region \(R\) is bounded by the curve, the \(x\)-axis and the lines \(x = 1\) and \(x = 3\). (a) Find the area of \(R\). (b) Find the volume when \(R\) is rotated about the \(x\)-axis, giving the exact value. (c) The region under the curve for \(x \ge 1\) is infinite in length: find its area.
A: (a) \(\displaystyle\int_1^3 12x^{-2}\,dx = \Big[-12x^{-1}\Big]_1^3 = -4 + 12 = 8\). [M1 A1] (b) \(V = \pi\displaystyle\int_1^3 144x^{-4}\,dx = \pi\Big[-48x^{-3}\Big]_1^3 = \pi\left(-\tfrac{48}{27} + 48\right) = \tfrac{416\pi}{9}\). [M1 A1 A1] (c) \(\displaystyle\int_1^\infty 12x^{-2}\,dx = \Big[-12x^{-1}\Big]_1^\infty = 0 + 12 = 12\), using the limit as \(t \to \infty\). [M1 A1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find \(\displaystyle\int \left(4x^3 - \frac{3}{x^2} + 2\sqrt{x}\right)dx\).
A: \(= x^4 - 3\left(\dfrac{x^{-1}}{-1}\right) + 2\left(\dfrac{x^{3/2}}{3/2}\right) + c\) [M1] \(= x^4 + \dfrac{3}{x} + \dfrac43 x^{3/2} + c\). [A1 A1 for the last two terms]
Q: [3 marks] ★ Evaluate \(\displaystyle\int_1^4 (3\sqrt{x} - 2)\,dx\).
A: \(\Big[2x^{3/2} - 2x\Big]_1^4\) [M1 A1] \(= (16 - 8) - (2 - 2) = 8\). [A1]
Q: [5 marks] ★★ A curve has gradient \(\dfrac{dy}{dx} = \dfrac{8}{(2x + 1)^2}\) and passes through \((1, 3)\). Find the equation of the curve.
A: \(\dfrac{dy}{dx} = 8(2x + 1)^{-2}\), so \(y = 8 \times \dfrac{(2x + 1)^{-1}}{-1 \times 2} + c\) [M1 A1] \(= -\dfrac{4}{2x + 1} + c\). Substituting \((1, 3)\): \(3 = -\dfrac43 + c\) [M1] so \(c = \dfrac{13}{3}\). [A1] \(y = \dfrac{13}{3} - \dfrac{4}{2x + 1}\). [A1]
Q: [5 marks] ★★ Find the area of the region between the curve \(y = x^2 - 6x + 8\) and the \(x\)-axis, from \(x = 2\) to \(x = 4\).
A: The curve crosses the axis at \(x = 2\) and \(x = 4\) (\((x - 2)(x - 4) = 0\)), and is below it between them. [B1] \(\displaystyle\int_2^4 (x^2 - 6x + 8)\,dx = \Big[\tfrac{x^3}{3} - 3x^2 + 8x\Big]_2^4\) [M1 A1] \(= \left(\tfrac{64}{3} - 48 + 32\right) - \left(\tfrac83 - 12 + 16\right) = -\tfrac43\). [M1] The area is \(\tfrac43\), because an area is positive. [A1]
Q: [6 marks] ★★ The line \(y = 3x + 4\) meets the curve \(y = x^2\) at two points. Find the area of the region enclosed between the line and the curve.
A: \(x^2 = 3x + 4\), so \((x - 4)(x + 1) = 0\), and \(x = -1\) or \(x = 4\). [M1 A1] The line is above the curve between these points, so the area is \(\displaystyle\int_{-1}^{4} (3x + 4 - x^2)\,dx\). [M1] \(= \Big[\tfrac{3x^2}{2} + 4x - \tfrac{x^3}{3}\Big]_{-1}^{4}\) [A1] \(= \left(24 + 16 - \tfrac{64}{3}\right) - \left(\tfrac32 - 4 + \tfrac13\right)\) [M1] \(= \dfrac{125}{6}\). [A1]
Q: [4 marks] ★★ Find the exact value of \(\displaystyle\int_4^\infty 6x^{-3/2}\,dx\).
A: \(\displaystyle\int 6x^{-3/2}\,dx = -12x^{-1/2}\). [M1 A1] As \(x \to \infty\), \(-12x^{-1/2} \to 0\). [B1] The value is \(0 - \left(-\dfrac{12}{2}\right) = 6\). [A1]
Q: [6 marks] ★★ (a) The region under \(y = 2\sqrt{x}\) for \(0 \le x \le 4\) is rotated through \(360^\circ\) about the \(x\)-axis. Find the volume. (b) The region bounded by \(y = x^2\), the \(y\)-axis and the line \(y = 9\) is rotated through \(360^\circ\) about the \(y\)-axis. Find the volume. Give both answers to 3 significant figures.
A: (a) \(V = \pi\displaystyle\int_0^4 4x\,dx = \pi\Big[2x^2\Big]_0^4\) [M1 A1] \(= 32\pi = 101\). [A1] (b) \(x^2 = y\), so \(V = \pi\displaystyle\int_0^9 y\,dy = \pi\Big[\tfrac{y^2}{2}\Big]_0^9\) [M1 A1] \(= \tfrac{81\pi}{2} = 127\). [A1]
Q: [10 marks] (#math.p1.diff) ★★★ A curve \(C\) has gradient \(\dfrac{dy}{dx} = 3x^2 - 6x\) and has a stationary point at \((2, -1)\). (a) Find the equation of \(C\). (b) Show that \(C\) has a maximum point at \((0, 3)\). (c) The line \(y = 3\) meets \(C\) again at \(x = 3\). Find the area of the region enclosed between \(C\) and the line \(y = 3\).
H: Integrate \(\dfrac{dy}{dx}\), then use the point \((2, -1)\) to find \(c\).
H: For (b), show \(\dfrac{dy}{dx} = 0\) at \(x = 0\) and find the sign of \(\dfrac{d^2y}{dx^2}\).
H: For (c), decide which of the curve and the line is higher between \(x = 0\) and \(x = 3\). Test a value such as \(x = 1\).
A: (a) \(y = x^3 - 3x^2 + c\). [M1 A1] At \((2, -1)\): \(-1 = 8 - 12 + c\) [M1] so \(c = 3\), and \(y = x^3 - 3x^2 + 3\). [A1] (b) At \(x = 0\), \(\dfrac{dy}{dx} = 0\) and \(y = 3\). [B1] \(\dfrac{d^2y}{dx^2} = 6x - 6 = -6 < 0\), so \((0, 3)\) is a maximum. [B1] (c) At \(x = 1\) the curve is at \(y = 1\), below the line \(y = 3\), so the line is above the curve between \(x = 0\) and \(x = 3\). [B1] Area \(= \displaystyle\int_0^3 \big(3 - (x^3 - 3x^2 + 3)\big)\,dx = \int_0^3 (3x^2 - x^3)\,dx\) [M1] \(= \Big[x^3 - \tfrac{x^4}{4}\Big]_0^3\) [A1] \(= 27 - \tfrac{81}{4} = \tfrac{27}{4}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The region \(R\) lies under the curve \(y = 3x^{-3/2}\) and above the \(x\)-axis for \(x \ge 1\). (a) Find the area of \(R\). (b) The region \(R\) is rotated through \(360^\circ\) about the \(x\)-axis. Find the exact volume of the solid.
H: Treat the upper limit as \(\infty\): integrate first, then see what happens to the antiderivative as \(x\) grows.
H: For (b), square \(y\) first: \(y^2 = 9x^{-3}\).
A: (a) \(\displaystyle\int_1^\infty 3x^{-3/2}\,dx = \Big[-6x^{-1/2}\Big]_1^\infty\) [M1 A1] \(= 0 - (-6) = 6\). [A1] (b) \(V = \pi\displaystyle\int_1^\infty 9x^{-3}\,dx = \pi\Big[-\dfrac{9}{2}x^{-2}\Big]_1^\infty\) [M1 A1] \(= \pi\left(0 + \dfrac92\right) = \dfrac{9\pi}{2}\). [A1]
Q: [5 marks] ★★★ The line \(y = kx\), where \(k > 0\), meets the curve \(y = x^2\) at the origin and at a second point \(P\). The area of the region enclosed between the line and the curve is 36. Find \(k\).
H: Find the \(x\)-coordinate of \(P\) in terms of \(k\); it is the upper limit of the integral.
H: The area comes out as a multiple of \(k^3\). Set it equal to 36.
A: \(x^2 = kx\) gives \(x = 0\) or \(x = k\). [B1] Between these, the line is above the curve: area \(= \displaystyle\int_0^k (kx - x^2)\,dx\). [M1] \(= \Big[\tfrac{kx^2}{2} - \tfrac{x^3}{3}\Big]_0^k = \tfrac{k^3}{2} - \tfrac{k^3}{3} = \tfrac{k^3}{6}\). [M1 A1] \(\tfrac{k^3}{6} = 36\), so \(k^3 = 216\) and \(k = 6\). [A1]
:::

:::quiz
? What is \(\displaystyle\int (2x + 1)^3\,dx\)?
- \(\dfrac{(2x + 1)^4}{4} + c\)
+ \(\dfrac{(2x + 1)^4}{8} + c\)
- \(\dfrac{(2x + 1)^4}{2} + c\)
- \(6(2x + 1)^2 + c\)
> The new power is 4 and the coefficient of \(x\) is 2, so divide by \(4 \times 2 = 8\). Dividing by 4 forgets the inner coefficient. The last option is the derivative, not the integral.
? What is the value of \(\displaystyle\int_{-1}^{1} x^3\,dx\)?
- \(\tfrac12\)
- \(-\tfrac12\)
+ \(0\)
- \(\tfrac14\)
> \(\Big[\tfrac{x^4}{4}\Big]_{-1}^{1} = \tfrac14 - \tfrac14 = 0\). The curve is below the axis for \(x < 0\) and above for \(x > 0\), so the signed areas cancel. The total (unsigned) area would be \(\tfrac12\).
? The curve \(y = x^2\) is rotated about the \(x\)-axis from \(x = 0\) to \(x = 1\). Which integral gives the volume?
- \(\pi\displaystyle\int_0^1 2x\,dx\)
- \(\displaystyle\int_0^1 \pi x^2\,dx\)
+ \(\pi\displaystyle\int_0^1 x^4\,dx\)
- \(\pi\displaystyle\int_0^1 x\,dx\)
> The volume is \(\pi\int y^2\,dx\) with \(y = x^2\), so \(y^2 = x^4\). Using \(\pi\int x^2\,dx\) forgets to square \(y\), and using \(2x\) differentiates instead of squaring.
? Which statement is true about \(\displaystyle\int_1^\infty \frac{1}{x^2}\,dx\) and \(\displaystyle\int_1^\infty \frac{1}{\sqrt{x}}\,dx\)?
- Both converge.
- Both diverge.
+ The first converges to 1 and the second diverges.
- The first diverges and the second converges to 2.
> \(\int_1^\infty x^{-2}\,dx = 1\) because \(x^{-1} \to 0\). For \(x^{-1/2}\) the antiderivative \(2\sqrt{x}\) grows without limit. A power of \(x\) must be below \(-1\) for the tail to shrink fast enough.
? The area between the curve \(y = x^2 - 4\) and the \(x\)-axis from \(x = -2\) to \(x = 2\) is
- \(-\tfrac{32}{3}\)
- \(0\)
+ \(\tfrac{32}{3}\)
- \(\tfrac{16}{3}\)
> The curve is below the axis on the whole interval, so the integral is \(-\tfrac{32}{3}\) and the area is its size, \(\tfrac{32}{3}\). The value \(\tfrac{16}{3}\) is the area for \(0 \le x \le 2\) only.
:::

:::checklist What you can now do
- [ ] I can integrate powers of \(x\), including roots and fractions, and sums of them.
- [ ] I can integrate \((ax + b)^n\) for any rational \(n \neq -1\).
- [ ] I can find the constant of integration from a given point.
- [ ] I can evaluate a definite integral, including a simple improper integral with an infinite limit or a limit where the function is undefined.
- [ ] I can find the area under a curve, including parts below the \(x\)-axis.
- [ ] I can find the area between a curve and a line, or between two curves.
- [ ] I can find the volume formed by rotating a region about the \(x\)-axis or the \(y\)-axis.
:::

:::recap
- \(\displaystyle\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + c\) for \(n \ne -1\); integrate term by term and always include \(+\,c\).
- \(\displaystyle\int (ax + b)^n\,dx = \dfrac{(ax + b)^{n+1}}{a(n+1)} + c\): divide by the coefficient of \(x\) as well. Linear brackets only.
- Use a given point to find \(c\). Definite integrals: \([F]_a^b = F(b) - F(a)\), no \(c\).
- Area under a curve \(\int y\,dx\). Split at roots when the curve crosses the axis; areas are positive. Between graphs: \(\int(\text{top} - \text{bottom})\,dx\).
- Improper integrals: replace the infinite or undefined limit by a letter and take the limit. For \(x^n\), it works for \(n < -1\) at \(\infty\) and for \(-1 < n < 0\) at \(0\).
- Volume about the \(x\)-axis \(\pi\int y^2\,dx\); about the \(y\)-axis \(\pi\int x^2\,dy\). With a hole, \(\pi\int(y_{\text{outer}}^2 - y_{\text{inner}}^2)\,dx\).
:::

:::links
- watch: [Integration and the fundamental theorem of calculus](https://www.3blue1brown.com/lessons/integration) · 3Blue1Brown · why area and antiderivatives are linked
- watch: [What does area have to do with slope?](https://www.3blue1brown.com/lessons/area-and-slope) · 3Blue1Brown · the same link seen another way
- watch: [Exam questions: volume of revolution about the x-axis](https://www.examsolutions.net/tutorials/exam-questions-volume-of-revolution-about-the-x-axis/) · ExamSolutions · exam-style questions solved on video
- practise: [CAIE Pure 1 integration exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/integration/integration/exam-questions/) · Save My Exams · with mark schemes [paid]
- read: [Area between curves](https://tutorial.math.lamar.edu/Classes/CalcI/AreaBetweenCurves.aspx) · Paul's Online Notes · worked examples, including with respect to y
- read: [Volumes of solids of revolution (rings)](https://tutorial.math.lamar.edu/Classes/CalcI/VolumeWithRings.aspx) · Paul's Online Notes · the washer method with pictures

Links checked 3 October 2026.
:::
Next: [Modulus and polynomials](#math.p3.algebra).
