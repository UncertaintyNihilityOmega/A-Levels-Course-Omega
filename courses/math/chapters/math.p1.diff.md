@chapter math.p1.diff
@title Differentiation
@level as
@paper CAIE P1 · Edexcel IAL P1–P3 · AQA/OCR/Edexcel Pure Year 1
@time 8–10 hours
@summary Differentiation finds the gradient of a curve at any point. You will learn what a derivative means, how to differentiate powers of \(x\) and composite functions with the chain rule, and how to use derivatives for tangents and normals, increasing and decreasing functions, stationary points, rates of change and maximum or minimum problems.

:::why
A straight line has one gradient, but almost everything that changes in the real world changes at a varying rate: the speed of a car, the growth of a population, the cost of making one more item. Differentiation measures that rate exactly, at any instant. It is the most important idea in Paper 1, it carries a large share of the marks, and Integration, Mechanics and every later calculus chapter are built on it.
:::

**Before you start**, you need negative and fractional indices from [Indices, surds and standard form](#math.f.powers), the equation of a line and perpendicular gradients from [Coordinate geometry](#math.p1.coord), and composite functions from [Functions](#math.p1.functions). Factorising and solving quadratics, from [Quadratics](#math.p1.quadratics), appear in almost every example.

:::try Warm-up
Q: Write \(\dfrac{5}{\sqrt{x}}\) as a power of \(x\). (from [Indices, surds and standard form](#math.f.powers))
A: \(\sqrt{x} = x^{1/2}\), so \(\dfrac{5}{\sqrt{x}} = 5x^{-1/2}\).
Q: Solve \(3x^2 - 6x - 9 = 0\). (from [Quadratics](#math.p1.quadratics))
A: Divide by 3: \(x^2 - 2x - 3 = 0\), so \((x - 3)(x + 1) = 0\) and \(x = 3\) or \(x = -1\).
Q: Find the gradient of any line perpendicular to \(3x + 4y = 8\). (from [Coordinate geometry](#math.p1.coord))
A: The line is \(y = -\tfrac34 x + 2\), gradient \(-\tfrac34\). The perpendicular gradient is \(\tfrac43\).
:::

## The gradient of a curve

The gradient of a straight line is the same everywhere: it rises by the same amount for every step to the right. A curve is different. On \(y = x^3\) the graph is almost flat near the origin and very steep at \(x = 3\). So for a curve we can only talk about its gradient **at a particular point**.

:::def Tangent
A straight line that touches a curve at a point and has the same direction as the curve there.
:::

:::def Gradient of a curve at a point
The gradient of the tangent to the curve at that point.
:::

To measure the gradient of the tangent we use chords. A **chord** is a straight line joining two points on the curve. Take the point \(P(2, 8)\) on \(y = x^3\) and a second point \(Q\) a little further along, with \(x\)-coordinate \(2 + h\). The gradient of the chord \(PQ\) is

\[\text{gradient of } PQ = \frac{(2 + h)^3 - 8}{h} = \frac{12h + 6h^2 + h^3}{h} = 12 + 6h + h^2\]

Now slide \(Q\) towards \(P\) by making \(h\) smaller and smaller:

| \(h\) | 1 | 0.1 | 0.01 | 0.001 |
|---|---|---|---|---|
| gradient of \(PQ\) | 19 | 12.61 | 12.0601 | 12.006001 |

The chord gradients get closer and closer to 12. As \(Q\) approaches \(P\), the chord turns into the tangent, so the gradient of the curve at \(P\) is **12**. Mathematicians say that 12 is the **limit** of the chord gradients as \(h\) tends to zero.

:::plot The chord PQ (h = 1) has gradient 19. The tangent at P(2, 8) has gradient 12, the limit of the chord gradients.
--f "x**3" --f "19*x-30" --f "12*x-16" --label "y = x³" --label "chord PQ" --label "tangent at P" --x -1.5 3.5 --y -4 32 --pt "2,8,P(2, 8)@se" --pt "3,27,Q(3, 27)@w" --legend tl
:::

Drag the slider to shrink \(h\) and watch the chord swing round until it lies along the tangent. Its gradient, \(12 + 6h + h^2\), closes in on 12.

:::html
<div class="widget" data-w="graph" data-fns="x^3; ((2+h)^3 - 8)/h*(x - 2) + 8" data-x="-0.5,3.5" data-y="-4,32" data-params="h=1,0.01,1.5,0.01" data-points="2,8; 2+h,(2+h)^3" data-labels="y = x³; chord through P(2, 8)"></div>
:::

## The derivative

If you repeat the chord calculation at a general point \((x, x^3)\) instead of at \(x = 2\), you find that the gradient of \(y = x^3\) is \(3x^2\) at every point. At \(x = 2\) this gives \(3 \times 4 = 12\), as before. The formula \(3x^2\) is called the **derivative** of \(x^3\).

:::def Derivative
The derivative of \(y = f(x)\) is the function that gives the gradient of the curve at each value of \(x\). It is written \(\dfrac{dy}{dx}\) or \(f'(x)\).
:::

Finding the derivative is called **differentiating**. Read \(\dfrac{dy}{dx}\) as "d y by d x": it is one symbol meaning "the rate of change of \(y\) with respect to \(x\)", not a fraction you can cancel. Read \(f'(x)\) as "f dash of x". So if \(f(x) = x^3\), then \(f'(x) = 3x^2\) and \(f'(2) = 12\).

You will not be asked to derive results from chords in a Cambridge exam, but you should understand the idea: **the derivative is the limit of chord gradients**.

## Differentiating powers of \(x\)

Repeating the chord method for other powers reveals a pattern: \(x^2\) has derivative \(2x\), \(x^3\) has \(3x^2\), \(x^4\) has \(4x^3\). The power comes down in front, and the new power is one less. The rule works for every rational power, including negative powers and fractions.

:::key Differentiating powers
\[\text{If } y = x^n \text{ then } \frac{dy}{dx} = nx^{n-1} \qquad (n \text{ any rational number})\]
- A constant multiple stays: if \(y = kx^n\) then \(\dfrac{dy}{dx} = knx^{n-1}\).
- Differentiate a sum or difference term by term.
- A constant on its own differentiates to 0 (the graph \(y = c\) is flat).
- In particular \(\dfrac{d}{dx}(kx) = k\): the gradient of a straight line.
:::

:::proof Why the power rule works (positive whole-number powers)
Take the point \(P(x, x^n)\) and a second point \(Q\) at \(x + h\). The chord \(PQ\) has gradient
\[\frac{(x + h)^n - x^n}{h}\]
Expand \((x + h)^n\) with the binomial theorem from [Series](#math.p1.series):
\[(x + h)^n = x^n + nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \dots + h^n\]
The first term cancels \(x^n\), and every other term has a factor \(h\), so dividing by \(h\) gives
\[\text{gradient of } PQ = nx^{n-1} + \binom{n}{2}x^{n-2}h + \dots + h^{n-1}\]
Now let \(h\) tend to 0. Every term that still contains \(h\) tends to 0, and only \(nx^{n-1}\) is left. The gradient of the curve at \(P\) is therefore \(nx^{n-1}\). For \(n = 3\) this is the \(3x^2 + 3xh + h^2 \to 3x^2\) you met above.

:::html
<div class="widget" data-w="proof" data-proof="chordlimit"></div>
:::
:::

:::eg Differentiate \(y = 4x^3 - 5x^2 + 7x - 2\).
Work term by term. Bring each power down and reduce it by one:
\[\frac{dy}{dx} = 4(3x^2) - 5(2x) + 7 - 0 = 12x^2 - 10x + 7\]
:::

Roots and fractions must be **rewritten as powers of \(x\)** before you differentiate.

:::steps
1. Write roots as fractional powers: \(\sqrt{x} = x^{1/2}\), \(\sqrt[3]{x^2} = x^{2/3}\).
2. Write \(x\) in a denominator as a negative power: \(\dfrac{1}{x^2} = x^{-2}\), \(\dfrac{5}{\sqrt{x}} = 5x^{-1/2}\).
3. Keep number coefficients separate: \(\dfrac{3}{2x} = \dfrac32 x^{-1}\), but \(\dfrac{1}{(2x)^2} = \dfrac14 x^{-2}\).
4. Differentiate, then rewrite the answer without negative powers if the question wants it "simplified".
:::

:::eg Differentiate \(y = 6\sqrt{x} - \dfrac{4}{x^2} + \dfrac{3}{2x}\).
Rewrite every term as a power of \(x\):
\[y = 6x^{1/2} - 4x^{-2} + \tfrac32 x^{-1}\]
Differentiate term by term. Take care with the negative powers: \(-2 - 1 = -3\) and \(-1 - 1 = -2\).
\[\frac{dy}{dx} = 6 \cdot \tfrac12 x^{-1/2} - 4(-2)x^{-3} + \tfrac32(-1)x^{-2} = 3x^{-1/2} + 8x^{-3} - \tfrac32 x^{-2}\]
In fraction form: \(\dfrac{dy}{dx} = \dfrac{3}{\sqrt{x}} + \dfrac{8}{x^3} - \dfrac{3}{2x^2}\).
:::

:::eg Differentiate (a) \(y = (2x + 1)(x - 3)\), (b) \(y = \dfrac{x^2 + 3}{\sqrt{x}}\).
There is no rule in Paper 1 for a product or a quotient, so turn each into a sum of powers first.

(a) Expand: \(y = 2x^2 - 5x - 3\), so \(\dfrac{dy}{dx} = 4x - 5\).

(b) Split the fraction over its denominator, then use the index laws:
\[y = \frac{x^2}{x^{1/2}} + \frac{3}{x^{1/2}} = x^{3/2} + 3x^{-1/2}\]
\[\frac{dy}{dx} = \tfrac32 x^{1/2} - \tfrac32 x^{-3/2}\]
:::

:::warn Two classic slips
**Differentiating a product bracket by bracket.** The derivative of \((2x + 1)(x - 3)\) is not \(2 \times 1 = 2\). Expand first.
**Moving the coefficient into the power.** \(\dfrac{3}{2x}\) is \(\tfrac32 x^{-1}\), not \(3(2x)^{-1}\) treated as \(3 \times 2x^{-1}\). Write the number and the power of \(x\) separately before you differentiate.
:::

Once you have \(f'(x)\), substitute a value of \(x\) to get the gradient at a point, or solve \(f'(x) = k\) to find where the gradient has a given value.

:::eg \(f(x) = x^3 - 6x + 1\). Find the gradient of the curve \(y = f(x)\) at \(x = -1\), and find the coordinates of the points where the gradient is 6.
\(f'(x) = 3x^2 - 6\), so at \(x = -1\) the gradient is \(f'(-1) = 3 - 6 = -3\).

For a gradient of 6: \(3x^2 - 6 = 6\), so \(x^2 = 4\) and \(x = 2\) or \(x = -2\).

Find each \(y\) from \(f(x)\), not from \(f'(x)\): \(f(2) = 8 - 12 + 1 = -3\) and \(f(-2) = -8 + 12 + 1 = 5\). The points are \((2, -3)\) and \((-2, 5)\).
:::

## The chain rule

How would you differentiate \(y = (3x - 1)^5\)? Expanding a fifth power is slow, and \(\sqrt{2x^2 + 1}\) cannot be expanded at all. These are **composite functions**: a function of a function. The chain rule handles them.

:::key The chain rule
If \(y\) is a function of \(u\), and \(u\) is a function of \(x\), then
\[\frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx}\]
For powers of a bracket this gives the shortcut
\[\frac{d}{dx}\big[(f(x))^n\big] = n\big(f(x)\big)^{n-1} \times f'(x)\]
"Differentiate the outside, keep the inside, then multiply by the derivative of the inside."
:::

:::proof Why the chain rule works (the idea)
Change \(x\) by a small amount \(\delta x\). Then \(u\) changes by \(\delta u\), and \(y\) changes by \(\delta y\), because \(y\) depends on \(u\).
For any such small changes the fractions can be multiplied, since \(\delta u\) cancels:
\[\frac{\delta y}{\delta x} = \frac{\delta y}{\delta u} \times \frac{\delta u}{\delta x}\]
Now let \(\delta x \to 0\). Then \(\delta u \to 0\) as well, and each fraction tends to its derivative:
\[\frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx}\]
This is the idea, not a full proof: it assumes \(\delta u \neq 0\). A complete proof handles the case where \(u\) does not change.
:::

:::eg Differentiate \(y = (3x - 1)^5\).
Let \(u = 3x - 1\), so \(y = u^5\).
\[\frac{dy}{du} = 5u^4 \qquad \frac{du}{dx} = 3\]
\[\frac{dy}{dx} = 5u^4 \times 3 = 15(3x - 1)^4\]
With the shortcut: bring down the 5, lower the power to 4, keep \((3x - 1)\), multiply by 3.
:::

:::eg Differentiate (a) \(y = \sqrt{2x^2 + 1}\), (b) \(y = \dfrac{8}{(4 - x)^3}\).
(a) Write \(y = (2x^2 + 1)^{1/2}\). The inside has derivative \(4x\).
\[\frac{dy}{dx} = \tfrac12(2x^2 + 1)^{-1/2} \times 4x = \frac{2x}{\sqrt{2x^2 + 1}}\]
(b) Write \(y = 8(4 - x)^{-3}\). The inside, \(4 - x\), has derivative \(-1\).
\[\frac{dy}{dx} = 8 \times (-3)(4 - x)^{-4} \times (-1) = \frac{24}{(4 - x)^4}\]
The two minus signs cancel, so the gradient is positive everywhere it exists.
:::

:::warn Do not lose the inside derivative
Writing \(\dfrac{d}{dx}(3x - 1)^5 = 5(3x - 1)^4\) is the most common chain-rule error. It loses the factor 3 and the accuracy mark. Watch for an inside derivative of \(-1\), as in \((4 - x)^{-3}\): it flips the sign of the whole answer.
:::

## The second derivative

The derivative \(\dfrac{dy}{dx}\) is itself a function of \(x\), so you can differentiate it again. The result is the **second derivative**, written \(\dfrac{d^2y}{dx^2}\) or \(f''(x)\). It measures how fast the gradient is changing.

:::eg Find \(\dfrac{dy}{dx}\) and \(\dfrac{d^2y}{dx^2}\) for \(y = x^4 - 2x^3 + 5x\).
\[\frac{dy}{dx} = 4x^3 - 6x^2 + 5 \qquad \frac{d^2y}{dx^2} = 12x^2 - 12x\]
:::

If \(f''(x) > 0\), the gradient is increasing, so the curve bends like the bottom of a ∪. If \(f''(x) < 0\), the gradient is decreasing, so the curve bends like the top of a ∩. You will use this to tell maximum points from minimum points.

## Tangents and normals

The tangent at a point has gradient \(f'(a)\). The **normal** is the line through the same point at right angles to the tangent.

:::def Normal
The straight line through a point on a curve that is perpendicular to the tangent at that point.
:::

:::key Tangent and normal at \((x_1, y_1)\)
- Gradient of the tangent: \(m = \dfrac{dy}{dx}\) evaluated at \(x = x_1\).
- Gradient of the normal: \(-\dfrac{1}{m}\) (perpendicular gradients multiply to \(-1\)).
- Equation of either line: \(y - y_1 = (\text{gradient})(x - x_1)\).
:::

In the graph below the red line is the tangent at the red point and the dashed line is a chord from that point to a second point a distance \(h\) to the right. Drag the red point along the curve, and shrink \(h\) with its slider: the chord gradient closes in on the tangent gradient. Where is the tangent horizontal?

:::html
<div class="widget" data-w="graph" data-fns="x^3 - 3*x" data-x="-2.5,3" data-y="-5,6" data-tangent="1.5" data-chord="1"></div>
:::

:::eg (Exam style) The curve \(y = x^2 - \dfrac{4}{x}\) passes through \(P(2, 2)\). (a) Find the equations of the tangent and the normal to the curve at \(P\). (b) The tangent meets the \(x\)-axis at \(A\) and the normal meets the \(x\)-axis at \(B\). Find the area of triangle \(PAB\).
**(a)** Write \(y = x^2 - 4x^{-1}\) and differentiate:
\[\frac{dy}{dx} = 2x + 4x^{-2} = 2x + \frac{4}{x^2}\] [M1 A1]
At \(x = 2\): \(\dfrac{dy}{dx} = 4 + 1 = 5\). [A1]
Tangent: \(y - 2 = 5(x - 2)\), so \(y = 5x - 8\). [A1]
The normal has gradient \(-\tfrac15\): \(y - 2 = -\tfrac15(x - 2)\), which gives \(x + 5y - 12 = 0\). [M1 A1]

**(b)** On the \(x\)-axis \(y = 0\). Tangent: \(0 = 5x - 8\), so \(A\) is \(\left(\tfrac85, 0\right)\). Normal: \(x - 12 = 0\), so \(B\) is \((12, 0)\). [M1]
The base \(AB = 12 - 1.6 = 10.4\) and the height is the \(y\)-coordinate of \(P\), which is 2.
\[\text{Area} = \tfrac12 \times 10.4 \times 2 = 10.4\] [A1]
:::

:::tip Leave lines in the requested form
If no form is asked for, \(y = mx + c\) is fine. If the question says "in the form \(ax + by + c = 0\)", multiply out the fractions so \(a\), \(b\) and \(c\) are integers, as with \(x + 5y - 12 = 0\) above.
:::

## Increasing and decreasing functions

Where the gradient is positive the graph rises from left to right; where it is negative the graph falls.

:::def Increasing and decreasing functions
A function is **increasing** on an interval if \(f'(x) > 0\) for every \(x\) in that interval, and **decreasing** if \(f'(x) < 0\) there.
:::

:::eg Find the set of values of \(x\) for which \(y = x^3 - 3x^2 - 9x + 5\) is decreasing.
\[\frac{dy}{dx} = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x - 3)(x + 1)\]
Decreasing means \(\dfrac{dy}{dx} < 0\). The quadratic \(3(x - 3)(x + 1)\) is ∪-shaped with roots \(-1\) and \(3\), so it is negative between them: \(-1 < x < 3\).
:::

To show that a function is increasing **for all** \(x\), show that \(f'(x)\) is always positive. Completing the square usually does it.

:::eg Show that \(f(x) = x^3 + 3x^2 + 6x - 2\) is an increasing function.
\[f'(x) = 3x^2 + 6x + 6 = 3(x^2 + 2x + 2) = 3\big[(x + 1)^2 + 1\big] = 3(x + 1)^2 + 3\]
A square is never negative, so \(f'(x) \geq 3 > 0\) for all \(x\). Therefore \(f\) is an increasing function.
:::

## Stationary points

At the top of a hill or the bottom of a valley the tangent is horizontal, so the gradient is zero.

:::def Stationary point
A point on a curve where \(\dfrac{dy}{dx} = 0\). A stationary point is a **maximum point** if the curve changes from rising to falling there, and a **minimum point** if it changes from falling to rising.
:::

:::plot The curve y = x³ − 3x² − 9x + 5 has a maximum point at (−1, 10) and a minimum point at (3, −22). It decreases between them.
--f "x**3-3*x**2-9*x+5" --label "y = x³ − 3x² − 9x + 5" --x -3 5 --y -28 18 --pt "-1,10,maximum (−1, 10)@nw" --pt "3,-22,minimum (3, −22)@e" --legend tr
:::

:::key Finding and classifying stationary points
1. Find \(\dfrac{dy}{dx}\) and solve \(\dfrac{dy}{dx} = 0\) for \(x\).
2. Substitute each \(x\) into the equation of the **curve** to find \(y\).
3. Find \(\dfrac{d^2y}{dx^2}\) at each point:
   - \(\dfrac{d^2y}{dx^2} < 0\): a **maximum** (the gradient is decreasing through zero).
   - \(\dfrac{d^2y}{dx^2} > 0\): a **minimum** (the gradient is increasing through zero).
   - \(\dfrac{d^2y}{dx^2} = 0\): the test gives no answer; check the sign of \(\dfrac{dy}{dx}\) on each side.
:::

:::eg (Exam style) Find the coordinates of the stationary points on the curve \(y = x^3 - 3x^2 - 9x + 5\), and determine the nature of each.
\[\frac{dy}{dx} = 3x^2 - 6x - 9\] [B1]
Set it equal to zero: \(3(x - 3)(x + 1) = 0\), so \(x = 3\) or \(x = -1\). [M1 A1]
Find \(y\): when \(x = -1\), \(y = -1 - 3 + 9 + 5 = 10\); when \(x = 3\), \(y = 27 - 27 - 27 + 5 = -22\). [A1]
\[\frac{d^2y}{dx^2} = 6x - 6\] [M1]
At \(x = -1\): \(\dfrac{d^2y}{dx^2} = -12 < 0\), so \((-1, 10)\) is a maximum point. At \(x = 3\): \(\dfrac{d^2y}{dx^2} = 12 > 0\), so \((3, -22)\) is a minimum point. [A1]
:::

The second-derivative test is quickest, but there is another method that always works. Look at the sign of \(\dfrac{dy}{dx}\) just to the left and just to the right of the stationary point.

| \(x\) | \(-1.1\) | \(-1\) | \(-0.9\) | \(2.9\) | \(3\) | \(3.1\) |
|---|---|---|---|---|---|---|
| sign of \(\dfrac{dy}{dx}\) | \(+\) | \(0\) | \(-\) | \(-\) | \(0\) | \(+\) |
| shape | ╱ | — | ╲ | ╲ | — | ╱ |

At \(x = -1\) the curve rises, levels off, then falls: a maximum. At \(x = 3\) it falls, levels off, then rises: a minimum.

:::eg Find the stationary points of \(y = x + \dfrac{9}{x}\) and determine their nature.
Write \(y = x + 9x^{-1}\), so \(\dfrac{dy}{dx} = 1 - 9x^{-2} = 1 - \dfrac{9}{x^2}\).

Setting this to zero: \(x^2 = 9\), so \(x = 3\) or \(x = -3\). Then \(y = 3 + 3 = 6\) and \(y = -3 - 3 = -6\).

\(\dfrac{d^2y}{dx^2} = 18x^{-3} = \dfrac{18}{x^3}\). At \(x = 3\) it is \(\tfrac{18}{27} > 0\), so \((3, 6)\) is a minimum. At \(x = -3\) it is \(-\tfrac{18}{27} < 0\), so \((-3, -6)\) is a maximum.
:::

The maximum point here is **lower** than the minimum point. That is not a contradiction: maximum and minimum describe the shape of the curve near the point (a local hilltop or valley), not the largest and smallest values of \(y\) overall.

:::plot y = x + 9/x has a maximum at (−3, −6) and a minimum at (3, 6). The curve has two separate branches because x = 0 is not allowed.
--f "x+9/x" --label "y = x + 9/x" --x -9 9 --y -16 16 --xstep 3 --pt "3,6,minimum (3, 6)@se" --pt "-3,-6,maximum (−3, −6)@nw" --legend tl
:::

:::exam Sketching from calculus
"Sketch the curve" questions give marks for the correct shape, the stationary points and the axis intercepts, labelled with coordinates. Find where the curve crosses the \(y\)-axis (put \(x = 0\)) and, if it is easy, the \(x\)-axis (put \(y = 0\)). You do not need a scale or plotted points. Points of inflexion are not in the Cambridge syllabus.
:::

## Rates of change

The derivative \(\dfrac{dy}{dx}\) is the rate at which \(y\) changes as \(x\) changes. When the variable is time \(t\), it is a rate in the everyday sense. If \(V\) is the volume of water in a tank in m³ and \(t\) is the time in minutes, then \(\dfrac{dV}{dt}\) is the rate of flow in m³ per minute. A positive value means \(V\) is increasing; a negative value means it is decreasing. In Mechanics, velocity is the rate of change of displacement, \(v = \dfrac{ds}{dt}\).

Often two quantities change together. When a circular ripple spreads, its radius \(r\) and its area \(A\) both increase with time. If you know how fast \(r\) grows, the chain rule gives how fast \(A\) grows.

:::key Connected rates of change
\[\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt}\]
Find \(\dfrac{dA}{dr}\) by differentiating the formula that links \(A\) and \(r\). Then multiply by the rate you are given, or divide by it if the unknown rate is \(\dfrac{dr}{dt}\).
:::

:::eg (Exam style) Oil spreads on water in a circle. The radius increases at a constant rate of 0.5 m s⁻¹. Find the rate at which the area is increasing when the radius is 20 m.
The area is \(A = \pi r^2\), so \(\dfrac{dA}{dr} = 2\pi r\). When \(r = 20\), \(\dfrac{dA}{dr} = 40\pi\). [M1]
\[\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt} = 40\pi \times 0.5 = 20\pi\] [M1]
The area is increasing at \(20\pi = 62.8\,\mathrm{m^2\,s^{-1}}\) (3 s.f.). [A1]
:::

:::eg (Exam style) Air is pumped into a spherical balloon at a constant rate of \(100\,\mathrm{cm^3\,s^{-1}}\). Find the rate at which the radius is increasing at the instant when the radius is 5 cm.
For a sphere \(V = \tfrac43\pi r^3\), so \(\dfrac{dV}{dr} = 4\pi r^2\). When \(r = 5\), \(\dfrac{dV}{dr} = 100\pi\). [B1]
The chain rule gives \(\dfrac{dV}{dt} = \dfrac{dV}{dr} \times \dfrac{dr}{dt}\), so
\[100 = 100\pi \times \frac{dr}{dt} \quad\Rightarrow\quad \frac{dr}{dt} = \frac{1}{\pi}\] [M1]
The radius is increasing at \(\dfrac{1}{\pi} = 0.318\,\mathrm{cm\,s^{-1}}\) (3 s.f.). [A1]
:::

:::tip Write the chain first
Before you put in numbers, write the chain rule with the letters of the question, for example \(\dfrac{dV}{dt} = \dfrac{dV}{dr} \times \dfrac{dr}{dt}\). The method mark is for this line, and it shows you at once whether to multiply or divide.
:::

## Maximum and minimum problems

Stationary points answer practical questions: the largest volume of a box, the least cost, the greatest area of a field.

:::steps
1. Write the quantity to be maximised or minimised as a formula. Use the information in the question to express it in terms of **one** variable.
2. Differentiate and solve "derivative \(= 0\)".
3. Reject values that make no sense in the context (negative lengths, zero widths).
4. Use the second derivative to show that the value gives a maximum (or a minimum).
5. Answer the question that was asked: often the maximum value itself, not just \(x\).
:::

:::eg (Exam style) A square sheet of card has sides of 24 cm. Equal squares of side \(x\) cm are cut from each corner, and the sides are folded up to make an open box. (a) Show that the volume of the box is \(V = 4x^3 - 96x^2 + 576x\). (b) Find the maximum volume and show that it is a maximum.
**(a)** The base is a square of side \(24 - 2x\) and the height is \(x\), so
\[V = x(24 - 2x)^2 = x(576 - 96x + 4x^2) = 4x^3 - 96x^2 + 576x\] [B1]
**(b)**
\[\frac{dV}{dx} = 12x^2 - 192x + 576 = 12(x^2 - 16x + 48) = 12(x - 4)(x - 12)\] [M1 A1]
So \(x = 4\) or \(x = 12\). When \(x = 12\) the base has side \(24 - 24 = 0\), so reject it: \(x = 4\). [A1]
\[\frac{d^2V}{dx^2} = 24x - 192, \quad \text{which is } 96 - 192 = -96 < 0 \text{ at } x = 4\] [M1]
so this is a maximum. The maximum volume is \(V = 4 \times 16^2 = 1024\,\mathrm{cm^3}\). [A1]
:::

:::plot The volume V = x(24 − 2x)² for 0 < x < 12. The greatest volume, 1024 cm³, comes from cutting squares of side 4 cm.
--f "x*(24-2*x)**2" --label "V = x(24 − 2x)²" --x 0 12 --y 0 1200 --pt "4,1024,maximum (4, 1024)@ne" --xlabel "x (cm)" --ylabel "V (cm³)" --legend tr
:::

:::board
Cambridge P1 covers everything in this chapter, including the chain rule and connected rates of change; derivatives of \(e^x\), \(\ln x\) and trigonometric functions come in [Further differentiation](#math.p3.diff). Edexcel IAL spreads the same ideas over P1 to P3, with the chain rule in P3. The UK A Levels (AQA, OCR, Edexcel) also require **differentiation from first principles**, a formal version of the chord argument, and second-year work on points of inflexion and concave and convex curves. Neither is in Cambridge 9709.
:::

:::exam What MF19 gives you
MF19 lists the derivative of \(x^n\) but not the chain rule, the conditions for maximum and minimum, or the formulas for areas and volumes used in rates questions (except the sphere and the cone). Learn them. Give a reason, such as "\(\dfrac{d^2y}{dx^2} < 0\) so maximum", every time you state the nature of a point: the mark depends on it.
:::

:::eg Spot the error: find the equation of the normal to \(y = x^2 - 4x + 7\) at the point where \(x = 3\).
A student wrote this answer.

Line 1: \(\dfrac{dy}{dx} = 2x - 4\)
Line 2: At \(x = 3\), \(\dfrac{dy}{dx} = 2\)
Line 3: The normal has gradient \(-\tfrac12\)
Line 4: \(y - 2 = -\tfrac12(x - 3)\), so \(x + 2y - 7 = 0\)

Lines 1 to 3 are correct and earn the first three marks [M1 A1 M1]. **Line 4 loses the last mark [A0].** The student used the gradient, 2, as the \(y\)-coordinate of the point. The point on the curve comes from the equation of the **curve**: \(y = 9 - 12 + 7 = 4\), so the point is \((3, 4)\).

Correct line 4: \(y - 4 = -\tfrac12(x - 3)\), so \(2y - 8 = -x + 3\) and \(x + 2y - 11 = 0\). [A1]

Always find the \(y\)-coordinate by substituting into \(y = f(x)\), never into \(f'(x)\).
:::

:::try Start easy, finish at exam standard
Q: Differentiate \(y = 5x^4 - 3x^2 + 8x - 7\).
A: \(\dfrac{dy}{dx} = 20x^3 - 6x + 8\).
Q: Differentiate \(f(x) = 4\sqrt{x} - \dfrac{6}{x^3}\).
A: \(f(x) = 4x^{1/2} - 6x^{-3}\), so \(f'(x) = 2x^{-1/2} + 18x^{-4} = \dfrac{2}{\sqrt{x}} + \dfrac{18}{x^4}\).
Q: Differentiate \(y = (x^2 - 3)(2x + 1)\).
A: Expand first: \(y = 2x^3 + x^2 - 6x - 3\), so \(\dfrac{dy}{dx} = 6x^2 + 2x - 6\).
Q: Differentiate \(y = (5 - 2x)^6\).
A: Chain rule with inside derivative \(-2\): \(\dfrac{dy}{dx} = 6(5 - 2x)^5 \times (-2) = -12(5 - 2x)^5\).
Q: Find the gradient of \(y = \dfrac{6}{\sqrt{3x + 1}}\) at the point where \(x = 1\).
A: \(y = 6(3x + 1)^{-1/2}\), so \(\dfrac{dy}{dx} = 6 \times \left(-\tfrac12\right)(3x + 1)^{-3/2} \times 3 = -9(3x + 1)^{-3/2}\). At \(x = 1\): \(-9 \times 4^{-3/2} = -\dfrac{9}{8}\).
Q: Find the equation of the normal to \(y = x^3 - 2x + 1\) at the point where \(x = 1\).
A: At \(x = 1\), \(y = 0\). \(\dfrac{dy}{dx} = 3x^2 - 2 = 1\), so the normal has gradient \(-1\). Normal: \(y - 0 = -1(x - 1)\), that is \(y = 1 - x\).
Q: Find the set of values of \(x\) for which \(f(x) = 2x^3 - 9x^2 + 12x\) is increasing.
A: \(f'(x) = 6x^2 - 18x + 12 = 6(x - 1)(x - 2)\). This is positive outside the roots: \(x < 1\) or \(x > 2\).
Q: Find the stationary points of \(y = 2x^3 + 3x^2 - 12x + 4\) and determine their nature.
A: \(\dfrac{dy}{dx} = 6x^2 + 6x - 12 = 6(x + 2)(x - 1) = 0\), so \(x = -2\) or \(x = 1\). Points: \((-2, 24)\) and \((1, -3)\). [M1 A1 A1]
\(\dfrac{d^2y}{dx^2} = 12x + 6\): at \(x = -2\) it is \(-18 < 0\), a maximum; at \(x = 1\) it is \(18 > 0\), a minimum. [M1 A1]
Q: The edges of a cube increase at 0.2 cm s⁻¹. Find the rate of increase of the volume when the edge is 5 cm.
A: \(V = x^3\), so \(\dfrac{dV}{dx} = 3x^2 = 75\) when \(x = 5\). Then \(\dfrac{dV}{dt} = 75 \times 0.2 = 15\,\mathrm{cm^3\,s^{-1}}\). [M1 A1]
Q: (Exam style) A farmer has 60 m of fencing to make a rectangular pen against a long straight wall, so only three sides need fencing. The two sides at right angles to the wall are each \(x\) m long. (a) Show that the area is \(A = 60x - 2x^2\). (b) Find the maximum area, showing that it is a maximum.
A: (a) The side parallel to the wall is \(60 - 2x\), so \(A = x(60 - 2x) = 60x - 2x^2\). [B1]
(b) \(\dfrac{dA}{dx} = 60 - 4x = 0\) gives \(x = 15\). [M1 A1] \(\dfrac{d^2A}{dx^2} = -4 < 0\), so it is a maximum. [B1] The maximum area is \(15 \times 30 = 450\,\mathrm{m^2}\). [A1]
Q: (Exam style) The curve \(y = ax^2 + \dfrac{b}{x}\) has a stationary point at \((1, 6)\). Find \(a\) and \(b\), and determine the nature of the stationary point.
A: The point lies on the curve: \(a + b = 6\). [B1]
\(\dfrac{dy}{dx} = 2ax - \dfrac{b}{x^2}\), which is 0 at \(x = 1\): \(2a - b = 0\). [M1 A1]
Adding the two equations: \(3a = 6\), so \(a = 2\) and \(b = 4\). [A1]
\(\dfrac{d^2y}{dx^2} = 2a + \dfrac{2b}{x^3} = 4 + 8 = 12 > 0\) at \(x = 1\), so it is a minimum point. [M1 A1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find \(\dfrac{dy}{dx}\) when \(y = 3x^4 - \dfrac{5}{x^2} + 6\sqrt{x}\).
A: \(y = 3x^4 - 5x^{-2} + 6x^{1/2}\), so \(\dfrac{dy}{dx} = 12x^3 + 10x^{-3} + 3x^{-1/2}\), that is \(12x^3 + \dfrac{10}{x^3} + \dfrac{3}{\sqrt{x}}\). [B1] [B1] [B1] (one for each term)
Q: [3 marks] ★ \(f(x) = \sqrt{4x - 3}\). Find \(f'(3)\).
A: \(f(x) = (4x - 3)^{1/2}\), so \(f'(x) = \tfrac12(4x - 3)^{-1/2} \times 4 = 2(4x - 3)^{-1/2}\). [M1 A1] \(f'(3) = 2 \times 9^{-1/2} = \tfrac23\). [A1]
Q: [4 marks] ★★ \(f(x) = x^3 + 6x^2 + 15x - 4\). Show that \(f\) is an increasing function for all real \(x\).
A: \(f'(x) = 3x^2 + 12x + 15\). [B1] \(= 3(x^2 + 4x + 5) = 3\big[(x + 2)^2 + 1\big]\). [M1 A1] A square is never negative, so \(f'(x) \geq 3 > 0\) for all \(x\), and \(f\) is increasing. [A1]
Q: [6 marks] ★★ The curve \(y = x^3 - 6x^2 + 9x + 2\) has two stationary points. Find their coordinates and determine their nature.
A: \(\dfrac{dy}{dx} = 3x^2 - 12x + 9\). [B1] Setting it to 0: \(3(x - 1)(x - 3) = 0\), so \(x = 1\) or \(x = 3\). [M1 A1] \(y = 1 - 6 + 9 + 2 = 6\) and \(y = 27 - 54 + 27 + 2 = 2\), so the points are \((1, 6)\) and \((3, 2)\). [A1] \(\dfrac{d^2y}{dx^2} = 6x - 12\). [M1] It is \(-6 < 0\) at \(x = 1\), a maximum, and \(6 > 0\) at \(x = 3\), a minimum. [A1]
Q: [6 marks] ★★ The tangent to the curve \(y = 2\sqrt{x}\) at the point \(P\) where \(x = 4\) meets the \(x\)-axis at \(A\) and the \(y\)-axis at \(B\). Find the area of triangle \(OAB\), where \(O\) is the origin.
A: At \(x = 4\), \(y = 4\). [B1] \(\dfrac{dy}{dx} = x^{-1/2}\), so the gradient at \(P\) is \(\tfrac12\). [M1 A1] Tangent: \(y - 4 = \tfrac12(x - 4)\), so \(y = \tfrac12 x + 2\). [A1] It meets the axes at \(A(-4, 0)\) and \(B(0, 2)\). [M1] Area \(= \tfrac12 \times 4 \times 2 = 4\). [A1]
Q: [4 marks] ★★ The side \(x\) cm of a square increases at a constant rate. When \(x = 12\), the area of the square is increasing at \(6\,\mathrm{cm^2\,s^{-1}}\). Find the rate at which (a) \(x\) is increasing, (b) the perimeter is increasing.
A: \(A = x^2\), so \(\dfrac{dA}{dx} = 2x = 24\) at \(x = 12\). [M1] \(\dfrac{dA}{dt} = \dfrac{dA}{dx} \times \dfrac{dx}{dt}\) gives \(6 = 24 \times \dfrac{dx}{dt}\), so \(\dfrac{dx}{dt} = 0.25\,\mathrm{cm\,s^{-1}}\). [A1] (b) \(P = 4x\), so \(\dfrac{dP}{dt} = 4 \times 0.25 = 1\,\mathrm{cm\,s^{-1}}\). [M1 A1]
Q: [10 marks] (#math.f.geometry) ★★★ A closed cylindrical tin has radius \(r\) cm and height \(h\) cm. Its volume is \(250\pi\,\mathrm{cm^3}\). (a) Show that the total surface area is \(S = 2\pi r^2 + \dfrac{500\pi}{r}\). (b) Find the value of \(r\) for which \(S\) has a stationary value. (c) Show that this is a minimum and find the minimum surface area, to 3 s.f.
H: Use the volume \(\pi r^2 h = 250\pi\) to write \(h\) in terms of \(r\), so the area has only one variable.
H: The surface area is two circles plus the curved surface: \(S = 2\pi r^2 + 2\pi r h\). Substitute \(h\).
H: Write \(\dfrac{500\pi}{r}\) as \(500\pi r^{-1}\) before you differentiate.
A: (a) \(h = \dfrac{250}{r^2}\). [B1] \(S = 2\pi r^2 + 2\pi r h\) [M1] \(= 2\pi r^2 + 2\pi r \times \dfrac{250}{r^2} = 2\pi r^2 + \dfrac{500\pi}{r}\). [A1] (b) \(\dfrac{dS}{dr} = 4\pi r - 500\pi r^{-2}\). [M1 A1] Setting it to 0: \(r^3 = 125\) [M1], so \(r = 5\). [A1] (c) \(\dfrac{d^2S}{dr^2} = 4\pi + 1000\pi r^{-3}\), which is \(4\pi + 8\pi = 12\pi > 0\) at \(r = 5\), so it is a minimum. [M1 A1] \(S = 50\pi + 100\pi = 150\pi = 471\,\mathrm{cm^2}\) (3 s.f.). [A1]
Q: [7 marks] (#math.p1.coord) ★★★ The point \(P\left(a, \dfrac{12}{a}\right)\) lies on the curve \(y = \dfrac{12}{x}\), where \(a > 0\). The tangent to the curve at \(P\) meets the \(x\)-axis at \(A\) and the \(y\)-axis at \(B\). Show that the area of triangle \(OAB\) is 24, whatever the value of \(a\).
H: Write \(y = 12x^{-1}\) and find the gradient at \(x = a\).
H: Use \(y - y_1 = m(x - x_1)\) at \(P\), then put \(y = 0\) and \(x = 0\) in turn.
H: The intercepts come out as \(x = 2a\) and \(y = \dfrac{24}{a}\).
A: \(\dfrac{dy}{dx} = -12x^{-2}\), so the gradient at \(P\) is \(-\dfrac{12}{a^2}\). [M1 A1] Tangent: \(y - \dfrac{12}{a} = -\dfrac{12}{a^2}(x - a)\). [M1] When \(y = 0\): \(-\dfrac{12}{a} = -\dfrac{12}{a^2}(x - a)\), so \(x - a = a\) and \(A = (2a, 0)\). [A1] When \(x = 0\): \(y = \dfrac{12}{a} + \dfrac{12}{a} = \dfrac{24}{a}\), so \(B = \left(0, \dfrac{24}{a}\right)\). [A1] Area \(= \tfrac12 \times 2a \times \dfrac{24}{a}\) [M1] \(= 24\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Find the set of values of \(k\) for which the equation \(x^3 - 3x^2 - 9x + k = 0\) has three distinct real roots.
H: Rewrite as \(x^3 - 3x^2 - 9x = -k\). The roots are the points where the horizontal line \(y = -k\) meets the curve \(y = x^3 - 3x^2 - 9x\).
H: Find the stationary points of that curve. A horizontal line meets a ∪∩-shaped cubic three times only if it lies between the two turning values.
A: Let \(g(x) = x^3 - 3x^2 - 9x\). Then \(g'(x) = 3(x - 3)(x + 1)\), so the stationary points are at \(x = -1\) and \(x = 3\). [M1 A1] \(g(-1) = 5\), a maximum, and \(g(3) = -27\), a minimum. [A1 A1] The line \(y = -k\) meets the curve three times exactly when it lies strictly between the minimum and the maximum: \(-27 < -k < 5\). [M1] So \(-5 < k < 27\). [A1]
Q: [7 marks] ★★★ The tangent to \(y = x^3\) at the point \(A(a, a^3)\), where \(a \neq 0\), meets the curve again at \(B\). Show that the gradient of the curve at \(B\) is four times its gradient at \(A\).
H: Find the tangent at \(A\), then put its equation equal to \(y = x^3\) to find where they meet.
H: You get a cubic in \(x\) with a repeated root at \(x = a\) (the tangent touches there). Expand \((x - a)^2(x + 2a)\) to check the cubic.
A: The gradient at \(A\) is \(3a^2\), so the tangent is \(y - a^3 = 3a^2(x - a)\), that is \(y = 3a^2 x - 2a^3\). [M1 A1] Meeting the curve: \(x^3 - 3a^2 x + 2a^3 = 0\). [M1] This factorises as \((x - a)^2(x + 2a) = 0\). [M1 A1] The repeated root \(x = a\) is the point of contact, so \(B\) has \(x = -2a\). [A1] The gradient at \(B\) is \(3(-2a)^2 = 12a^2 = 4 \times 3a^2\). [A1]
:::

:::quiz
? What is the derivative of \(\dfrac{4}{x^2}\)?
+ \(-\dfrac{8}{x^3}\)
- \(\dfrac{4}{2x}\)
- \(-\dfrac{8}{x}\)
- \(\dfrac{8}{x^3}\)
> Write \(\dfrac{4}{x^2} = 4x^{-2}\). Then the derivative is \(4 \times (-2)x^{-3} = -8x^{-3}\). Differentiating the denominator on its own gives \(\tfrac{4}{2x}\), which is wrong, and lowering \(-2\) to \(-1\) instead of \(-3\) gives \(-\tfrac{8}{x}\).
? What is \(\dfrac{dy}{dx}\) when \(y = (2x + 3)^4\)?
- \(4(2x + 3)^3\)
+ \(8(2x + 3)^3\)
- \(8(2x + 3)^4\)
- \(4(2)^3\)
> Chain rule: \(4(2x + 3)^3\) times the derivative of the inside, which is 2. The answer \(4(2x + 3)^3\) forgets the inside derivative.
? At a stationary point, \(\dfrac{d^2y}{dx^2} = -5\). What kind of point is it?
+ A maximum point
- A minimum point
- A point of inflexion
- It cannot be decided
> A negative second derivative means the gradient is decreasing through zero, from positive to negative: the curve rises then falls, so it is a maximum.
? The tangent to a curve at \(P\) has gradient 4. What is the gradient of the normal at \(P\)?
- \(-4\)
+ \(-\dfrac14\)
- \(\dfrac14\)
- \(4\)
> Perpendicular gradients multiply to \(-1\), so the normal has gradient \(-\dfrac{1}{4}\). Changing only the sign, or only taking the reciprocal, does not give a perpendicular line.
? The radius of a circle increases at 2 cm s⁻¹. How fast is the area increasing when the radius is 3 cm?
- \(6\pi\) cm² s⁻¹
- \(4\pi\) cm² s⁻¹
+ \(12\pi\) cm² s⁻¹
- \(36\pi\) cm² s⁻¹
> \(\dfrac{dA}{dr} = 2\pi r = 6\pi\) when \(r = 3\), and \(\dfrac{dA}{dt} = 6\pi \times 2 = 12\pi\). Stopping at \(6\pi\) forgets to multiply by \(\dfrac{dr}{dt}\).
:::

:::checklist What you can now do
- [ ] I can explain the gradient of a curve as the limit of chord gradients.
- [ ] I can differentiate sums of powers of \(x\), including roots and fractions I first rewrite as powers.
- [ ] I can use the chain rule to differentiate a bracket raised to a power.
- [ ] I can find the second derivative and use it to tell a maximum from a minimum.
- [ ] I can find the equation of a tangent or a normal at a given point.
- [ ] I can find where a function is increasing or decreasing, and show that it is increasing for all \(x\).
- [ ] I can find stationary points and justify their nature.
- [ ] I can solve connected rates of change problems with the chain rule.
- [ ] I can set up and solve a maximum or minimum problem in one variable.
:::

:::recap
- The gradient of a curve at a point is the gradient of its tangent, the limit of the gradients of chords through that point.
- \(\dfrac{d}{dx}(x^n) = nx^{n-1}\) for any rational \(n\). Rewrite roots and fractions as powers of \(x\), and expand products, before differentiating.
- Chain rule: \(\dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}\). For a bracket: \(n(\text{bracket})^{n-1} \times\) (derivative of the inside).
- Tangent gradient \(m = f'(a)\); normal gradient \(-\dfrac1m\); use \(y - y_1 = m(x - x_1)\).
- Increasing where \(f'(x) > 0\), decreasing where \(f'(x) < 0\).
- Stationary points: solve \(\dfrac{dy}{dx} = 0\). \(\dfrac{d^2y}{dx^2} < 0\) means maximum, \(> 0\) means minimum; if it is 0, check the gradient on each side.
- Connected rates: \(\dfrac{dA}{dt} = \dfrac{dA}{dr} \times \dfrac{dr}{dt}\).
- Optimisation: one variable, differentiate, solve, reject impossible values, justify the maximum or minimum, answer the question.
:::

:::links
- watch: [The Essence of Calculus](https://www.3blue1brown.com/lessons/essence-of-calculus) · 3Blue1Brown · the whole idea of calculus, visually
- watch: [The paradox of the derivative](https://www.3blue1brown.com/lessons/derivatives) · 3Blue1Brown · what "instantaneous rate of change" really means
- watch: [Exam questions: connected rates of change](https://www.examsolutions.net/tutorials/exam-questions-connected-rates-of-change/) · ExamSolutions · the chain rule in rates questions
- practise: [CAIE Pure 1 applications of differentiation](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/differentiation/applications-of-differentiation/exam-questions/) · Save My Exams · tangents, stationary points, rates [paid]
- practise: [Calculus 1](https://www.khanacademy.org/math/calculus-1) · Khan Academy · derivative skills with instant feedback
- explore: [Calculus Grapher](https://phet.colorado.edu/en/simulations/calculus-grapher) · PhET · draw a curve and see its derivative
- explore: [Calculus of Powers](https://undergroundmathematics.org/calculus-of-powers) · Underground Mathematics · rich problems on differentiating powers

Links checked 3 October 2026.
:::
Next: [Integration](#math.p1.integ) reverses differentiation and uses it to find areas and volumes.
