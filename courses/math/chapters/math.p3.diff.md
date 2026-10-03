@chapter math.p3.diff
@title Further differentiation
@level as a2
@paper CAIE P2/P3 · Edexcel IAL P3–P4 · AQA/OCR/Edexcel Pure Year 2
@time 9–11 hours
@summary Derivatives of \(e^x\), \(\ln x\), \(\sin x\), \(\cos x\) and \(\tan x\) with the chain rule; the product and quotient rules; tangents, normals and stationary points of these functions; parametric and implicit differentiation; and \(\tan^{-1}x\) in Paper 3.

:::why
In [Differentiation](#math.p1.diff) you could only differentiate powers of \(x\). Real change is rarely a power: populations grow like \(e^{kt}\), waves are sines and cosines, and costs may involve logarithms. This chapter gives you the derivatives of those functions and the product and quotient rules, which let you differentiate anything built from them. Parametric and implicit differentiation then handle curves that are not written as \(y = f(x)\).
:::

**Before you start**, you need [Differentiation](#math.p1.diff) (the chain rule, tangents, stationary points), [Logarithms and exponentials](#math.p3.logs) and [Further trigonometry](#math.p3.trig). All angles in this chapter are in **radians**.

## Derivatives of the standard functions

The number \(e\) is special because the graph of \(y = e^x\) has gradient equal to its height at every point. At \(x = 1\) the height is \(e = 2.718\ldots\), and the gradient is also \(e\).

:::plot The graph of \(y = e^x\) and its tangent at (1, e). The tangent is y = ex, so its gradient is e, the same as the height of the curve at that point.
--f "exp(x)" --f "2.71828*x" --label "y = eˣ" --label "tangent at x = 1" --x -2 3 --y -1 10 --pt "1,2.71828,(1, e)@nw" --legend tl
:::

:::key Derivatives to know (radians)
\[\frac{d}{dx}(e^x) = e^x \qquad \frac{d}{dx}(\ln x) = \frac1x\]
\[\frac{d}{dx}(\sin x) = \cos x \qquad \frac{d}{dx}(\cos x) = -\sin x \qquad \frac{d}{dx}(\tan x) = \sec^2 x\]
These are on MF19. With a linear inside function, the chain rule multiplies by the coefficient \(a\) of \(x\):
\[\frac{d}{dx}e^{ax+b} = ae^{ax+b} \qquad \frac{d}{dx}\ln(ax+b) = \frac{a}{ax+b}\]
\[\frac{d}{dx}\sin(ax+b) = a\cos(ax+b) \qquad \frac{d}{dx}\cos(ax+b) = -a\sin(ax+b) \qquad \frac{d}{dx}\tan(ax+b) = a\sec^2(ax+b)\]
:::

:::warn Radians only
These derivatives are true **only when \(x\) is in radians**. If an angle is in degrees, \(\dfrac{d}{dx}\sin x^\circ = \dfrac{\pi}{180}\cos x^\circ\). Set the calculator to radian mode for every calculus question, even if the question gives no unit.
:::

:::eg Differentiate (a) \(3e^{2x} - 4\ln x\), (b) \(5\sin 3x + \cos\left(\tfrac x2\right)\), (c) \(\tan 4x\), (d) \(\ln(5x - 2)\)
(a) \(\dfrac{dy}{dx} = 3 \times 2e^{2x} - \dfrac4x = 6e^{2x} - \dfrac4x\).

(b) \(\dfrac{dy}{dx} = 5 \times 3\cos 3x - \tfrac12\sin\left(\tfrac x2\right) = 15\cos 3x - \tfrac12\sin\tfrac x2\).

(c) \(\dfrac{dy}{dx} = 4\sec^2 4x\).

(d) \(\dfrac{dy}{dx} = \dfrac{5}{5x - 2}\).
:::

### The chain rule for composite functions

For a general inside function, use the chain rule from [Differentiation](#math.p1.diff): if \(y = f(u)\) and \(u = g(x)\), then
\[\frac{dy}{dx} = \frac{dy}{du} \times \frac{du}{dx}\]
In words: differentiate the outside function (leaving the inside alone), then multiply by the derivative of the inside.

:::eg Differentiate (a) \(e^{x^2}\), (b) \(\sin^2 x\), (c) \((3 + 2e^x)^4\), (d) \(\ln(\cos x)\)
(a) Inside \(x^2\), outside \(e^u\): \(\dfrac{dy}{dx} = e^{x^2} \times 2x = 2xe^{x^2}\).

(b) Write \(y = (\sin x)^2\). Outside \(u^2\), inside \(\sin x\): \(\dfrac{dy}{dx} = 2\sin x \times \cos x = 2\sin x\cos x\).

(c) \(\dfrac{dy}{dx} = 4(3 + 2e^x)^3 \times 2e^x = 8e^x(3 + 2e^x)^3\).

(d) \(\dfrac{dy}{dx} = \dfrac{1}{\cos x} \times (-\sin x) = -\tan x\).
:::

## The product rule

If \(y\) is the **product** of two functions of \(x\), you cannot differentiate each factor and multiply. The correct rule is:

:::key Product rule
If \(y = uv\), where \(u\) and \(v\) are functions of \(x\), then
\[\frac{dy}{dx} = u\frac{dv}{dx} + v\frac{du}{dx}\]
In words: first times the derivative of the second, plus second times the derivative of the first. It is on MF19, written \(\dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}\).
:::

:::eg Differentiate (a) \(x^2e^{3x}\), (b) \(x\ln x\), (c) \(e^x\sin 2x\)
(a) Let \(u = x^2\) and \(v = e^{3x}\), so \(u' = 2x\) and \(v' = 3e^{3x}\).
\[\frac{dy}{dx} = x^2 \times 3e^{3x} + e^{3x} \times 2x = xe^{3x}(3x + 2)\]
(b) \(u = x\), \(v = \ln x\): \(\dfrac{dy}{dx} = x \times \dfrac1x + \ln x \times 1 = 1 + \ln x\).

(c) \(u = e^x\), \(v = \sin 2x\), so \(v' = 2\cos 2x\):
\[\frac{dy}{dx} = e^x \times 2\cos 2x + \sin 2x \times e^x = e^x(2\cos 2x + \sin 2x)\]
Check (b) by writing \(y = x\ln x\) at \(x = 1\): the formula gives \(1 + 0 = 1\), and the gradient of \(y = x\ln x\) there is \(1\). ✓
:::

## The quotient rule

:::key Quotient rule
If \(y = \dfrac{u}{v}\), then
\[\frac{dy}{dx} = \frac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}\]
The numerator is "bottom times derivative of top, minus top times derivative of bottom". The order matters because of the minus sign. It is on MF19.
:::

:::eg Differentiate (a) \(\dfrac{\sin x}{x}\), (b) \(\dfrac{e^{2x}}{x + 1}\). Then use the quotient rule to show that \(\dfrac{d}{dx}(\tan x) = \sec^2 x\).
(a) \(u = \sin x\), \(v = x\): \(\dfrac{dy}{dx} = \dfrac{x\cos x - \sin x \times 1}{x^2} = \dfrac{x\cos x - \sin x}{x^2}\).

(b) \(u = e^{2x}\), \(v = x + 1\): \(\dfrac{dy}{dx} = \dfrac{(x + 1)2e^{2x} - e^{2x} \times 1}{(x + 1)^2} = \dfrac{e^{2x}(2x + 1)}{(x + 1)^2}\).

For \(\tan x = \dfrac{\sin x}{\cos x}\), take \(u = \sin x\) and \(v = \cos x\):
\[\frac{d}{dx}\tan x = \frac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x\]
:::

:::tip Choosing a rule
Sometimes it is quicker to rewrite. \(\dfrac{\sin x}{x}\) is a quotient, but \(x^{-1}\sin x\) is a product, and both need the same work. For \(\dfrac{1}{(2x+1)^3}\), write \((2x + 1)^{-3}\) and use the chain rule alone. Use the quotient rule when the numerator and denominator are both genuinely functions of \(x\).
:::

## Tangents, normals and stationary points

The method is unchanged from [Differentiation](#math.p1.diff): the derivative gives the gradient of the tangent; the normal has the gradient \(-\dfrac{1}{m}\); a stationary point has \(\dfrac{dy}{dx} = 0\), and \(\dfrac{d^2y}{dx^2}\) (or the sign of \(\dfrac{dy}{dx}\) either side) shows the nature.

:::eg Find the stationary point of \(y = xe^{-x}\) and determine its nature.
Product rule with \(u = x\), \(v = e^{-x}\), \(v' = -e^{-x}\): \(\dfrac{dy}{dx} = x(-e^{-x}) + e^{-x} = e^{-x}(1 - x)\).

This is zero when \(x = 1\), because \(e^{-x}\) is never zero. Then \(y = e^{-1}\). Differentiate again: \(\dfrac{d^2y}{dx^2} = e^{-x}(-1) + (1 - x)(-e^{-x}) = e^{-x}(x - 2)\). At \(x = 1\) this is \(-e^{-1} < 0\), so the point \(\left(1, \dfrac1e\right)\) is a **maximum**.
:::

:::eg (Exam style) The curve \(y = \dfrac{\ln x}{x}\) is defined for \(x > 0\). (a) Show that \(\dfrac{dy}{dx} = \dfrac{1 - \ln x}{x^2}\). (b) Find the exact coordinates of the stationary point and determine its nature.
**(a)** Quotient rule with \(u = \ln x\), \(v = x\):
\[\frac{dy}{dx} = \frac{x \times \frac1x - \ln x \times 1}{x^2}\] [M1 A1]
\[= \frac{1 - \ln x}{x^2}\] ∎ [A1]

**(b)** Set \(\dfrac{dy}{dx} = 0\): \(1 - \ln x = 0\), so \(\ln x = 1\) and \(x = e\). [M1] Then \(y = \dfrac{\ln e}{e} = \dfrac1e\). The stationary point is \(\left(e, \dfrac1e\right)\). [A1]

For its nature, differentiate the quotient again: \(\dfrac{d^2y}{dx^2} = \dfrac{x^2\left(-\frac1x\right) - (1 - \ln x)(2x)}{x^4} = \dfrac{2\ln x - 3}{x^3}\). [M1] At \(x = e\) this is \(\dfrac{2 - 3}{e^3} = -\dfrac{1}{e^3} < 0\), so the point is a **maximum**. [A1]
:::

:::plot The curve \(y = \dfrac{\ln x}{x}\) has a maximum point at (e, 1/e), about (2.72, 0.368).
--f "log(x)/x" --label "y = (ln x)/x" --x 0.2 8 --y -2 0.6 --pt "2.71828,0.36788,maximum (e, 1/e)@ne" --legend br
:::

:::eg Find the stationary point of \(y = x^2\ln x\) (for \(x > 0\)) and its nature, and the equation of the tangent to \(y = e^{2x} + 3x\) at \(x = 0\).
Product rule: \(\dfrac{dy}{dx} = x^2 \times \dfrac1x + \ln x \times 2x = x + 2x\ln x = x(1 + 2\ln x)\). Setting this to zero with \(x > 0\) gives \(\ln x = -\tfrac12\), so \(x = e^{-1/2} = 0.6065\), and \(y = x^2\ln x = e^{-1}\left(-\tfrac12\right) = -\dfrac{1}{2e} = -0.184\). The second derivative is \(\dfrac{d^2y}{dx^2} = 2\ln x + 3\), which is \(2 > 0\) at that point. So it is a minimum at \((0.607, -0.184)\).

For the tangent, \(\dfrac{dy}{dx} = 2e^{2x} + 3\). At \(x = 0\): the gradient is \(5\) and \(y = 1\). The tangent is \(y = 5x + 1\).
:::

## Parametric differentiation

Sometimes \(x\) and \(y\) are both given in terms of a third variable, the **parameter**, such as \(t\). For example, a ball's position at time \(t\) has \(x = 2t\) and \(y = 5t - t^2\).

:::def Parametric equations
A curve is given by parametric equations when \(x\) and \(y\) are each written as a function of a third variable, the parameter (usually \(t\) or \(\theta\)). Each value of the parameter gives one point \((x, y)\) on the curve.
:::

:::key Parametric differentiation
If \(x = f(t)\) and \(y = g(t)\), then
\[\frac{dy}{dx} = \frac{dy/dt}{dx/dt}\]
This is the chain rule \(\dfrac{dy}{dx} = \dfrac{dy}{dt} \times \dfrac{dt}{dx}\) with \(\dfrac{dt}{dx} = \dfrac{1}{dx/dt}\). The answer is usually in terms of \(t\). It is on MF19.
:::

:::eg A curve is given by \(x = t^3\), \(y = 3t^2\). Find \(\dfrac{dy}{dx}\) in terms of \(t\), and the equation of the tangent at \(t = 2\).
\(\dfrac{dx}{dt} = 3t^2\) and \(\dfrac{dy}{dt} = 6t\), so \(\dfrac{dy}{dx} = \dfrac{6t}{3t^2} = \dfrac{2}{t}\).

At \(t = 2\): \(x = 8\), \(y = 12\), gradient \(= 1\). The tangent is \(y - 12 = 1(x - 8)\), so \(y = x + 4\).
:::

:::eg (Exam style) A curve has parametric equations \(x = t^2\), \(y = t^3 - 3t\). (a) Find \(\dfrac{dy}{dx}\) in terms of \(t\). (b) Find the equation of the tangent at the point where \(t = 2\), in the form \(ax + by + c = 0\). (c) Find the coordinates of the points where the tangent is horizontal.
**(a)** \(\dfrac{dx}{dt} = 2t\), \(\dfrac{dy}{dt} = 3t^2 - 3\). [B1]
\[\frac{dy}{dx} = \frac{3t^2 - 3}{2t}\] [M1 A1]

**(b)** At \(t = 2\): \(x = 4\), \(y = 8 - 6 = 2\), and \(\dfrac{dy}{dx} = \dfrac{12 - 3}{4} = \dfrac94\). [B1 B1]
\[y - 2 = \tfrac94(x - 4) \implies 4y - 8 = 9x - 36 \implies 9x - 4y - 28 = 0\] [M1 A1]

**(c)** A horizontal tangent has \(\dfrac{dy}{dx} = 0\): \(3t^2 - 3 = 0\), so \(t = \pm 1\) (and \(2t \ne 0\)). [M1] When \(t = 1\): \((1, -2)\). When \(t = -1\): \((1, 2)\). [A1]
:::

## Implicit differentiation

Some curves, such as the circle \(x^2 + y^2 = 25\) or \(x^2 + xy + y^2 = 7\), cannot easily be written as \(y = f(x)\). You can still find \(\dfrac{dy}{dx}\) by differentiating **every term with respect to \(x\)**, remembering that \(y\) depends on \(x\). A term in \(y\) needs the chain rule: \(\dfrac{d}{dx}(y^2) = 2y\dfrac{dy}{dx}\). A product such as \(xy\) needs the product rule.

:::def Implicit equation
An equation linking \(x\) and \(y\) in which \(y\) is not written as a function of \(x\) alone, such as \(x^2 + y^2 = 25\). The relation still defines the gradient of the curve at each point.
:::

:::key Implicit differentiation
- Differentiate each term with respect to \(x\). For a function of \(y\), \(\dfrac{d}{dx}f(y) = f'(y)\dfrac{dy}{dx}\).
- \(\dfrac{d}{dx}(xy) = x\dfrac{dy}{dx} + y\).
- Collect the terms containing \(\dfrac{dy}{dx}\) on one side, factorise, and divide.
The answer usually contains both \(x\) and \(y\).
:::

:::eg Find \(\dfrac{dy}{dx}\) for \(x^2 + y^2 = 25\), and the gradient at \((3, 4)\). Then find the equation of the tangent to \(x^2 + xy + y^2 = 7\) at \((2, 1)\).
\(2x + 2y\dfrac{dy}{dx} = 0\), so \(\dfrac{dy}{dx} = -\dfrac xy\). At \((3, 4)\) the gradient is \(-\tfrac34\), which is perpendicular to the radius (gradient \(\tfrac43\)). ✓

For the second curve: \(2x + \left(x\dfrac{dy}{dx} + y\right) + 2y\dfrac{dy}{dx} = 0\). Collect: \(\dfrac{dy}{dx}(x + 2y) = -(2x + y)\), so
\[\frac{dy}{dx} = -\frac{2x + y}{x + 2y}\]
At \((2, 1)\): \(-\dfrac{5}{4}\). The tangent is \(y - 1 = -\tfrac54(x - 2)\), which gives \(5x + 4y - 14 = 0\). The point \((2, 1)\) is on the curve since \(4 + 2 + 1 = 7\). ✓
:::

:::eg (Exam style) The curve \(C\) has equation \(xe^y + y = 3\). (a) Verify that \((3, 0)\) lies on \(C\). (b) Find the gradient of \(C\) at \((3, 0)\). (c) Find the equation of the normal at this point.
**(a)** \(3e^0 + 0 = 3\). ✓ [B1]

**(b)** Differentiate with respect to \(x\) using the product rule on \(xe^y\):
\[e^y + xe^y\frac{dy}{dx} + \frac{dy}{dx} = 0\] [M1 A1]
\[\frac{dy}{dx} = -\frac{e^y}{xe^y + 1}\] [M1]
At \((3, 0)\): \(-\dfrac{1}{3 + 1} = -\dfrac14\). [A1]

**(c)** The normal has gradient \(4\). [M1] \(y - 0 = 4(x - 3)\), so \(y = 4x - 12\). [A1]
:::

### Differentiating \(\tan^{-1}x\) (Paper 3 only)

If \(y = \tan^{-1}x\), then \(x = \tan y\). Differentiate both sides with respect to \(x\): \(1 = \sec^2 y\dfrac{dy}{dx}\). Use \(\sec^2 y = 1 + \tan^2 y = 1 + x^2\).

:::key Derivative of \(\tan^{-1}x\) (Paper 3 only)
\[\frac{d}{dx}\left(\tan^{-1}x\right) = \frac{1}{1 + x^2}\]
This is on MF19. With a linear inside function, \(\dfrac{d}{dx}\tan^{-1}(ax) = \dfrac{a}{1 + a^2x^2}\). The derivatives of \(\sin^{-1}x\) and \(\cos^{-1}x\) are not required.
:::

:::eg Differentiate \(\tan^{-1}(2x)\) and \(x\tan^{-1}x\).
\(\dfrac{d}{dx}\tan^{-1}(2x) = \dfrac{2}{1 + 4x^2}\).

Product rule: \(\dfrac{d}{dx}\left(x\tan^{-1}x\right) = x \times \dfrac{1}{1 + x^2} + \tan^{-1}x \times 1 = \dfrac{x}{1 + x^2} + \tan^{-1}x\).
:::

## Rates of change in context

The derivative of a quantity that grows or decays exponentially is proportional to the quantity itself.

:::eg The population of a colony is \(P = 200e^{0.03t}\). Find the rate of growth when \(t = 10\). A hot drink cools according to \(T = 20 + 80e^{-0.1t}\) degrees Celsius after \(t\) minutes; find the rate of change of temperature at \(t = 5\).
\(\dfrac{dP}{dt} = 200 \times 0.03e^{0.03t} = 6e^{0.03t}\). At \(t = 10\): \(6e^{0.3} = 8.10\) per year. Notice \(\dfrac{dP}{dt} = 0.03P\): the growth rate is proportional to the population.

\(\dfrac{dT}{dt} = 80(-0.1)e^{-0.1t} = -8e^{-0.1t}\). At \(t = 5\): \(-8e^{-0.5} = -4.85\), so the drink is cooling at \(4.85\,^\circ\mathrm{C}\) per minute.
:::

:::exam Presenting differentiation
- Name the rule you use ("product rule with \(u = \ldots\), \(v = \ldots\)"), write \(u'\) and \(v'\), then combine. Marks go for each correct derivative.
- Simplify only after you have shown the unsimplified result, and factorise common factors such as \(e^{3x}\) when you need to solve \(\dfrac{dy}{dx} = 0\).
- For "show that" parts, show the full application of the rule and each simplification. For stationary points, give exact coordinates (with \(e\) or \(\ln\)) unless the question asks for decimals.
- In implicit questions, state the point is on the curve if asked to verify, and keep \(\dfrac{dy}{dx}\) terms together before factorising.
:::

:::board Other boards
Edexcel IAL covers the chain, product and quotient rules and the derivatives of \(e^x\), \(\ln x\) and the trigonometric functions in P3, and parametric and implicit differentiation in P4. UK A Levels (AQA, Edexcel, OCR) cover these in Pure Year 2. Cambridge Paper 2 includes everything above except \(\tan^{-1}x\), which is Paper 3 only.
:::

:::try Start easy, finish at exam standard
Q: Differentiate (a) \(4e^{-3x}\), (b) \(2\ln(3x + 1)\), (c) \(\sin(2x - 1)\), (d) \(\tan 3x\).
A: (a) \(-12e^{-3x}\). (b) \(\dfrac{6}{3x + 1}\). (c) \(2\cos(2x - 1)\). (d) \(3\sec^2 3x\).
Q: Differentiate (a) \(e^{\sin x}\), (b) \(\cos^3 x\), (c) \(\ln(x^2 + 1)\).
A: (a) \(\cos x\,e^{\sin x}\). (b) \(3\cos^2 x \times (-\sin x) = -3\sin x\cos^2 x\). (c) \(\dfrac{2x}{x^2 + 1}\).
Q: Differentiate (a) \(x^3\sin x\), (b) \(e^{2x}\cos x\), (c) \(\sqrt{x}\ln x\).
A: (a) \(x^3\cos x + 3x^2\sin x\). (b) \(e^{2x}(2\cos x - \sin x)\). (c) \(\sqrt{x} \cdot \dfrac1x + \ln x \cdot \dfrac{1}{2\sqrt{x}} = \dfrac{1}{\sqrt x} + \dfrac{\ln x}{2\sqrt x} = \dfrac{2 + \ln x}{2\sqrt x}\).
Q: Differentiate (a) \(\dfrac{x}{e^{x}}\), (b) \(\dfrac{1 + \sin x}{\cos x}\).
A: (a) \(\dfrac{e^x \cdot 1 - x e^x}{e^{2x}} = \dfrac{1 - x}{e^x}\). (b) \(\dfrac{\cos x \cdot \cos x - (1 + \sin x)(-\sin x)}{\cos^2 x} = \dfrac{\cos^2 x + \sin x + \sin^2 x}{\cos^2 x} = \dfrac{1 + \sin x}{\cos^2 x}\).
Q: Find the gradient of the tangent to \(y = \tan 2x\) at \(x = \dfrac{\pi}{8}\), giving an exact answer.
A: \(\dfrac{dy}{dx} = 2\sec^2 2x\). At \(x = \dfrac\pi8\): \(2\sec^2\dfrac\pi4 = 2 \times 2 = 4\).
Q: Find the equation of the tangent to \(y = e^{2x} - 3x\) at the point where \(x = 0\).
A: \(\dfrac{dy}{dx} = 2e^{2x} - 3 = -1\) at \(x = 0\), and \(y = 1\). The tangent is \(y = -x + 1\).
Q: Find the stationary point of \(y = e^{2x} - 6x\) and show it is a minimum.
A: \(\dfrac{dy}{dx} = 2e^{2x} - 6 = 0\), so \(e^{2x} = 3\) and \(x = \tfrac12\ln 3 = 0.549\). \(y = 3 - 3\ln 3 = -0.296\). \(\dfrac{d^2y}{dx^2} = 4e^{2x} = 12 > 0\), so a minimum.
Q: A curve has \(x = 3t - 1\), \(y = t^2 + 2t\). Find \(\dfrac{dy}{dx}\) in terms of \(t\) and the equation of the normal at \(t = 1\).
A: \(\dfrac{dy}{dx} = \dfrac{2t + 2}{3}\). At \(t = 1\): point \((2, 3)\), gradient \(\tfrac43\). Normal gradient \(-\tfrac34\): \(y - 3 = -\tfrac34(x - 2)\), so \(3x + 4y - 18 = 0\).
Q: Verify that \((2, 1)\) lies on the curve \(x^2 + 2xy - y^2 = 7\), and find \(\dfrac{dy}{dx}\) and the gradient at that point.
A: \(4 + 4 - 1 = 7\). ✓ \(2x + 2y + 2x\dfrac{dy}{dx} - 2y\dfrac{dy}{dx} = 0\), so \(\dfrac{dy}{dx} = \dfrac{x + y}{y - x}\). At \((2, 1)\): \(\dfrac{3}{-1} = -3\).
Q: (Exam style) The curve \(y = x^2e^{-x}\) has two stationary points. (a) Show that \(\dfrac{dy}{dx} = xe^{-x}(2 - x)\). (b) Find the exact coordinates of the stationary points and determine their nature. (c) Write down the range of \(y\) for \(x \ge 0\).
A: (a) Product rule: \(x^2(-e^{-x}) + e^{-x}(2x) = e^{-x}(2x - x^2) = xe^{-x}(2 - x)\). [M1 A1] (b) Zero when \(x = 0\) or \(x = 2\). [M1] Points \((0, 0)\) and \(\left(2, 4e^{-2}\right)\). [A1] Second derivative: \(\dfrac{d}{dx}\left[e^{-x}(2x - x^2)\right] = e^{-x}(2 - 2x) - e^{-x}(2x - x^2) = e^{-x}(x^2 - 4x + 2)\). [M1] At \(x = 0\): \(2 > 0\), a minimum. At \(x = 2\): \(e^{-2}(4 - 8 + 2) = -2e^{-2} < 0\), a maximum. [A1] (c) For \(x \ge 0\), \(0 \le y \le 4e^{-2}\). [B1]
:::

:::quiz
? What is \(\dfrac{d}{dx}\left(e^{5x}\right)\)?
- \(e^{5x}\)
+ \(5e^{5x}\)
- \(5xe^{5x - 1}\)
- \(\dfrac{e^{5x}}{5}\)
> \(e^{5x}\) differentiates to \(5e^{5x}\) (chain rule). The option \(5xe^{5x-1}\) wrongly applies the power rule, and dividing by 5 is what happens when you integrate.
? What is \(\dfrac{d}{dx}\left(\ln(3x)\right)\)?
- \(\dfrac{3}{x}\)
- \(\dfrac{1}{3x}\)
+ \(\dfrac1x\)
- \(3\ln x\)
> \(\ln(3x) = \ln 3 + \ln x\), so the derivative is \(\dfrac1x\). The chain rule gives \(\dfrac{3}{3x} = \dfrac1x\) too. The \(3\) cancels, which many students do not expect.
? Which is \(\dfrac{d}{dx}\left(x\sin x\right)\)?
- \(\cos x\)
- \(x\cos x\)
+ \(\sin x + x\cos x\)
- \(\sin x - x\cos x\)
> By the product rule, \(x\cos x + \sin x\cdot 1\). Differentiating the factors separately and multiplying gives \(1 \times \cos x = \cos x\), which is wrong.
? If \(x = t^2\) and \(y = 2t\), what is \(\dfrac{dy}{dx}\)?
- \(\dfrac{t}{1}\)
+ \(\dfrac{1}{t}\)
- \(\dfrac{2t}{2}\)
- \(t\)
> \(\dfrac{dy}{dt} = 2\) and \(\dfrac{dx}{dt} = 2t\), so \(\dfrac{dy}{dx} = \dfrac{2}{2t} = \dfrac1t\). Inverting the fraction gives \(t\), a very common slip.
? For \(xy + y^2 = 6\), implicit differentiation gives
- \(y + 2y\dfrac{dy}{dx} = 0\)
+ \(y + x\dfrac{dy}{dx} + 2y\dfrac{dy}{dx} = 0\)
- \(x + y + 2y = 0\)
- \(x\dfrac{dy}{dx} + 2y = 0\)
> The term \(xy\) needs the product rule (\(y + x\dfrac{dy}{dx}\)) and \(y^2\) needs the chain rule (\(2y\dfrac{dy}{dx}\)). The first option forgets the \(x\dfrac{dy}{dx}\) part.
:::

:::recap
- \((e^x)' = e^x\), \((\ln x)' = \dfrac1x\), \((\sin x)' = \cos x\), \((\cos x)' = -\sin x\), \((\tan x)' = \sec^2 x\), all in **radians**. With \(ax + b\) inside, multiply by \(a\).
- Chain rule: \(\dfrac{dy}{dx} = \dfrac{dy}{du}\dfrac{du}{dx}\). Product rule: \((uv)' = uv' + vu'\). Quotient rule: \(\left(\dfrac uv\right)' = \dfrac{vu' - uv'}{v^2}\).
- Tangent and normal gradients are \(m\) and \(-\dfrac1m\). Stationary points: \(\dfrac{dy}{dx} = 0\), with \(\dfrac{d^2y}{dx^2}\) for the nature.
- Parametric: \(\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}\). Implicit: differentiate each term in \(x\); \(\dfrac{d}{dx}y^2 = 2y\dfrac{dy}{dx}\), and the product rule for \(xy\).
- Paper 3 only: \(\dfrac{d}{dx}\tan^{-1}x = \dfrac{1}{1 + x^2}\).
:::

:::links
- watch: [Visualizing the chain rule and product rule](https://www.3blue1brown.com/lessons/chain-rule-and-product-rule) · 3Blue1Brown · why the rules are true
- watch: [What's so special about Euler's number e?](https://www.3blue1brown.com/lessons/eulers-number) · 3Blue1Brown · why eˣ is its own derivative
- watch: [Implicit differentiation, what's going on here?](https://www.3blue1brown.com/lessons/implicit-differentiation) · 3Blue1Brown · the idea behind the method
- watch: [Differentiating parametric functions](https://www.examsolutions.net/tutorials/differentiation-parametric-functions/) · ExamSolutions · dy/dx from dy/dt and dx/dt
- practise: [CAIE Pure 3 further differentiation exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/differentiation/further-differentiation/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Calculus of Trigonometry & Logarithms](https://undergroundmathematics.org/calculus-trig-log) · Underground Mathematics · rich problems on these derivatives

Links checked 3 October 2026.
:::
Next: [Further integration](#math.p3.integ).
