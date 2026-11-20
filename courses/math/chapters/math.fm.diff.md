@chapter math.fm.diff
@title Further differentiation and Maclaurin series
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary You will differentiate the hyperbolic functions and the inverse trigonometric and inverse hyperbolic functions, find second derivatives of curves given implicitly or by parameters, and build Maclaurin series: polynomials that match a function and its derivatives at zero. You will use the standard series from MF19, combine them, derive new ones by repeated differentiation, and use them to approximate values and find limits.

:::why
Differentiation tells you how a function changes at a point. Repeating it tells you almost everything about the function near that point: its value, slope, curvature, and so on. A Maclaurin series packs all of that into a polynomial that you can evaluate by hand, which is how calculators and computers find \(\sin x\) and \(e^x\) in the first place. The first half of this chapter adds the new derivatives you need; the second half uses them to build series, and shows why \(\cosh\) of a small number looks like a parabola.
:::

**Before you start**, you need the chain, product and quotient rules and implicit and parametric first derivatives from [Further differentiation](#math.p3.diff), the hyperbolic functions and their inverses from [Hyperbolic functions](#math.fm.hyperbolic), and the binomial series for rational powers from [Modulus and polynomials](#math.p3.algebra).

:::try Warm-up
Q: Differentiate \(x^2e^{3x}\). (from [Further differentiation](#math.p3.diff))
A: Product rule: \(2xe^{3x} + 3x^2e^{3x} = xe^{3x}(2 + 3x)\).
Q: A curve has \(x = t^2\) and \(y = 2t\). Find \(\dfrac{dy}{dx}\). (from [Further differentiation](#math.p3.diff))
A: \(\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt} = \dfrac{2}{2t} = \dfrac1t\).
Q: Expand \((1 + x)^{-1/2}\) as far as \(x^2\). (from [Modulus and polynomials](#math.p3.algebra))
A: \(1 + \left(-\tfrac12\right)x + \dfrac{\left(-\frac12\right)\left(-\frac32\right)}{2}x^2 = 1 - \tfrac12 x + \tfrac38 x^2\).
:::

## Derivatives of hyperbolic functions

Start with the definitions, because \(e^x\) is easy to differentiate. Since \(\sinh x = \tfrac12\left(e^x - e^{-x}\right)\),
\[\frac{d}{dx}\sinh x = \tfrac12\left(e^x + e^{-x}\right) = \cosh x\]
and in the same way \(\dfrac{d}{dx}\cosh x = \tfrac12\left(e^x - e^{-x}\right) = \sinh x\). Notice there is no minus sign: that is the biggest difference from \(\sin\) and \(\cos\).

:::key Derivatives of the hyperbolic functions
\[\begin{aligned}
\frac{d}{dx}\sinh x &= \cosh x & \frac{d}{dx}\cosh x &= \sinh x \\
\frac{d}{dx}\tanh x &= \operatorname{sech}^2 x & \frac{d}{dx}\operatorname{sech} x &= -\operatorname{sech} x\tanh x \\
\frac{d}{dx}\operatorname{cosech} x &= -\operatorname{cosech} x\coth x & \frac{d}{dx}\coth x &= -\operatorname{cosech}^2 x
\end{aligned}\]
With the chain rule, \(\dfrac{d}{dx}\sinh f(x) = f'(x)\cosh f(x)\), and so on.
:::

MF19 gives the derivatives of \(\sinh x\), \(\cosh x\) and \(\tanh x\). The reciprocal ones you derive when needed, by the quotient or chain rule.

:::eg (Exam style) Show that \(\dfrac{d}{dx}\tanh x = \operatorname{sech}^2 x\).
Write \(\tanh x = \dfrac{\sinh x}{\cosh x}\) and use the quotient rule:
\[\frac{d}{dx}\tanh x = \frac{\cosh x\cdot\cosh x - \sinh x\cdot\sinh x}{\cosh^2 x}\] [M1 A1]
The numerator is \(\cosh^2 x - \sinh^2 x = 1\), so
\[\frac{d}{dx}\tanh x = \frac{1}{\cosh^2 x} = \operatorname{sech}^2 x\] [A1]
:::

:::eg (Exam style) Show that \(\dfrac{d}{dx}\operatorname{sech} x = -\operatorname{sech} x\tanh x\).
Write \(\operatorname{sech} x = (\cosh x)^{-1}\) and use the chain rule:
\[\frac{d}{dx}(\cosh x)^{-1} = -(\cosh x)^{-2}\sinh x\] [M1]
\[= -\frac{1}{\cosh x}\times\frac{\sinh x}{\cosh x} = -\operatorname{sech} x\tanh x\] [A1]
:::

The derivatives of \(\operatorname{cosech}\) and \(\coth\) are found the same way: \(\operatorname{cosech} x = (\sinh x)^{-1}\) gives \(-\operatorname{cosech} x\coth x\), and \(\coth x = \cosh x / \sinh x\) gives \(\dfrac{\sinh^2 x - \cosh^2 x}{\sinh^2 x} = -\operatorname{cosech}^2 x\).

:::warn \(\cosh\) differentiates to \(+\sinh\)
\(\dfrac{d}{dx}\cosh x = +\sinh x\), not \(-\sinh x\). The minus signs belong to the derivatives of the reciprocal functions \(\operatorname{sech}\), \(\operatorname{cosech}\) and \(\coth\). Test a result by looking at the graph: \(\cosh x\) is increasing for \(x > 0\), so its gradient there must be positive.
:::

:::eg Differentiate (a) \(\sinh 3x\), (b) \(x^2\cosh 2x\), (c) \(\tanh\left(x^2\right)\), (d) \(\ln\cosh x\).
(a) Chain rule with inner function \(3x\): \(\dfrac{d}{dx}\sinh 3x = 3\cosh 3x\).

(b) Product rule with \(u = x^2\) and \(v = \cosh 2x\), \(v' = 2\sinh 2x\):
\[\frac{d}{dx}\left(x^2\cosh 2x\right) = 2x\cosh 2x + 2x^2\sinh 2x\]
(c) The inner function \(x^2\) has derivative \(2x\):
\[\frac{d}{dx}\tanh\left(x^2\right) = 2x\operatorname{sech}^2\left(x^2\right)\]
(d) The chain rule for \(\ln\): \(\dfrac{d}{dx}\ln\cosh x = \dfrac{\sinh x}{\cosh x} = \tanh x\).
:::

:::eg (Exam style) The curve \(y = \cosh x - 2x\) has a stationary point. Find its exact coordinates and determine its nature.
\[\frac{dy}{dx} = \sinh x - 2\] [M1]
At a stationary point \(\sinh x = 2\), so
\[x = \sinh^{-1} 2 = \ln\left(2 + \sqrt5\right)\] [A1]
For the \(y\)-coordinate, \(\cosh x = \sqrt{1 + \sinh^2 x} = \sqrt5\):
\[y = \sqrt5 - 2\ln\left(2 + \sqrt5\right)\] [M1 A1]
\[\frac{d^2y}{dx^2} = \cosh x = \sqrt5 > 0\] [B1]
so the point \(\left(\ln\left(2 + \sqrt5\right),\ \sqrt5 - 2\ln\left(2 + \sqrt5\right)\right)\) is a minimum, approximately \((1.44, -0.651)\).
:::

:::eg Find the equation of the tangent to \(y = \sinh x\) at the point where \(x = \ln 2\), giving the answer in exact form.
\[\sinh(\ln 2) = \frac{2 - \frac12}{2} = \frac34 \qquad \cosh(\ln 2) = \frac{2 + \frac12}{2} = \frac54\]
The gradient is \(\dfrac{dy}{dx} = \cosh x = \dfrac54\). The tangent is
\[y - \tfrac34 = \tfrac54\left(x - \ln 2\right)\]
that is \(y = \tfrac54 x + \tfrac34 - \tfrac54\ln 2\), or \(4y = 5x + 3 - 5\ln 2\).
:::

:::eg The cable from [Hyperbolic functions](#math.fm.hyperbolic), \(y = 25\cosh\frac{x}{25} - 19\) (metres), is attached to a pole at \(x = 15\). Find the angle it makes with the horizontal there, and the horizontal distance from the lowest point at which the gradient is 1.
\[\frac{dy}{dx} = 25 \times \frac{1}{25}\sinh\frac{x}{25} = \sinh\frac{x}{25}\]
At \(x = 15\): gradient \(= \sinh 0.6 = 0.6367\), so the angle is \(\tan^{-1} 0.6367 = 32.5^\circ\).

Gradient 1: \(\sinh\dfrac{x}{25} = 1\), so \(x = 25\sinh^{-1} 1 = 25\ln\left(1 + \sqrt2\right) = 22.0\) m (3 s.f.). Since \(\sinh\) is odd the gradient is also \(-1\) at \(x = -22.0\).
:::

## Derivatives of inverse trigonometric and inverse hyperbolic functions

Each of these comes from the same idea: if \(y = f^{-1}(x)\), then \(x = f(y)\), so \(\dfrac{dx}{dy} = f'(y)\) and \(\dfrac{dy}{dx} = \dfrac{1}{f'(y)}\). Then rewrite \(f'(y)\) in terms of \(x\) with an identity.

:::key Derivatives of inverse functions
\[\begin{aligned}
\frac{d}{dx}\sin^{-1}x &= \frac{1}{\sqrt{1 - x^2}} & \frac{d}{dx}\sinh^{-1}x &= \frac{1}{\sqrt{x^2 + 1}} \\
\frac{d}{dx}\cos^{-1}x &= -\frac{1}{\sqrt{1 - x^2}} & \frac{d}{dx}\cosh^{-1}x &= \frac{1}{\sqrt{x^2 - 1}} \\
\frac{d}{dx}\tan^{-1}x &= \frac{1}{1 + x^2} & \frac{d}{dx}\tanh^{-1}x &= \frac{1}{1 - x^2}
\end{aligned}\]
Valid for \(\lvert x \rvert < 1\) (\(\sin^{-1}\), \(\cos^{-1}\), \(\tanh^{-1}\)), \(x > 1\) (\(\cosh^{-1}\)) and all real \(x\) (\(\sinh^{-1}\), \(\tan^{-1}\)).
:::

Compare the left and right columns: the hyperbolic versions swap a minus for a plus under the root (and in the \(\tan^{-1}\) case, a plus for a minus). That mirrors \(\cosh^2 - \sinh^2 = 1\) versus \(\cos^2 + \sin^2 = 1\).

:::eg (Exam style) Show that \(\dfrac{d}{dx}\sin^{-1}x = \dfrac{1}{\sqrt{1 - x^2}}\) for \(-1 < x < 1\).
Let \(y = \sin^{-1}x\), so \(x = \sin y\) with \(-\tfrac\pi2 \le y \le \tfrac\pi2\). [B1]

Differentiate with respect to \(y\): \(\dfrac{dx}{dy} = \cos y\), so
\[\frac{dy}{dx} = \frac{1}{\cos y}\] [M1]
On this interval \(\cos y \ge 0\), so \(\cos y = +\sqrt{1 - \sin^2 y} = \sqrt{1 - x^2}\) and
\[\frac{dy}{dx} = \frac{1}{\sqrt{1 - x^2}}\] [A1]
:::

:::eg (Exam style) Show that \(\dfrac{d}{dx}\cosh^{-1}x = \dfrac{1}{\sqrt{x^2 - 1}}\) for \(x > 1\).
Let \(y = \cosh^{-1}x\), so \(x = \cosh y\) with \(y > 0\). [B1]

\[\frac{dx}{dy} = \sinh y \quad\text{so}\quad \frac{dy}{dx} = \frac{1}{\sinh y}\] [M1]
Since \(y > 0\), \(\sinh y > 0\), so \(\sinh y = +\sqrt{\cosh^2 y - 1} = \sqrt{x^2 - 1}\). [M1]
\[\frac{dy}{dx} = \frac{1}{\sqrt{x^2 - 1}}\] [A1]
:::

:::eg (Exam style) Show that \(\dfrac{d}{dx}\tanh^{-1}x = \dfrac{1}{1 - x^2}\) for \(\lvert x \rvert < 1\).
Let \(y = \tanh^{-1}x\), so \(x = \tanh y\). [B1]

\[\frac{dx}{dy} = \operatorname{sech}^2 y = 1 - \tanh^2 y = 1 - x^2\] [M1]
\[\frac{dy}{dx} = \frac{1}{1 - x^2}\] [A1]
:::

:::eg (Exam style) Use the logarithmic form of \(\sinh^{-1}x\) to show that \(\dfrac{d}{dx}\sinh^{-1}x = \dfrac{1}{\sqrt{x^2 + 1}}\).
Start with \(y = \ln\left(x + \sqrt{x^2 + 1}\right)\). The derivative of \(\ln u\) is \(\dfrac{u'}{u}\), with \(u = x + \sqrt{x^2 + 1}\) and
\[u' = 1 + \frac{x}{\sqrt{x^2 + 1}} = \frac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1}}\] [M1 A1]
\[\frac{dy}{dx} = \frac{u'}{u} = \frac{\sqrt{x^2 + 1} + x}{\sqrt{x^2 + 1}\left(x + \sqrt{x^2 + 1}\right)} = \frac{1}{\sqrt{x^2 + 1}}\] [A1]
:::

:::eg Differentiate (a) \(\sinh^{-1}2x\), (b) \(\cos^{-1}\left(x^2\right)\), (c) \(\tanh^{-1}\sqrt x\), (d) \(x\sin^{-1}x + \sqrt{1 - x^2}\).
(a) \(\dfrac{d}{dx}\sinh^{-1}(2x) = \dfrac{2}{\sqrt{4x^2 + 1}}\).

(b) \(\dfrac{d}{dx}\cos^{-1}\left(x^2\right) = -\dfrac{2x}{\sqrt{1 - x^4}}\).

(c) With \(u = \sqrt x\) and \(u' = \dfrac{1}{2\sqrt x}\):
\[\frac{d}{dx}\tanh^{-1}\sqrt x = \frac{1}{1 - x}\times\frac{1}{2\sqrt x} = \frac{1}{2\sqrt x\,(1 - x)}\]
(d) The product rule on the first term, and the chain rule on the second:
\[\begin{aligned}
\frac{d}{dx}\left[x\sin^{-1}x + \sqrt{1 - x^2}\right] &= \sin^{-1}x + \frac{x}{\sqrt{1 - x^2}} - \frac{x}{\sqrt{1 - x^2}} \\
&= \sin^{-1}x
\end{aligned}\]
That is a hint that \(\int \sin^{-1}x\,dx\) can be done by parts.
:::

:::eg (Exam style) Given that \(y = \tanh^{-1}(\sin x)\) for \(-\tfrac\pi2 < x < \tfrac\pi2\), show that \(\dfrac{dy}{dx} = \sec x\).
With \(u = \sin x\), \(\dfrac{du}{dx} = \cos x\), so
\[\frac{dy}{dx} = \frac{1}{1 - \sin^2 x}\times\cos x\] [M1 A1]
\[= \frac{\cos x}{\cos^2 x} = \sec x\] [A1]
So \(\tanh^{-1}(\sin x)\) is an antiderivative of \(\sec x\), which is how MF19's \(\int\sec x\,dx\) can be written.
:::

## Second derivatives of implicit and parametric curves

### Implicit differentiation, twice

To find \(\dfrac{d^2y}{dx^2}\) for a relation between \(x\) and \(y\), differentiate the whole equation, with respect to \(x\), once to find \(\dfrac{dy}{dx}\), then differentiate that result again, remembering that \(y\) and \(\dfrac{dy}{dx}\) are both functions of \(x\). The product rule appears often. At a given point, substitute \(x\), \(y\) and \(\dfrac{dy}{dx}\) at the end.

:::eg (Exam style) A curve has equation \(x^2 + xy + y^2 = 3\). Find the value of \(\dfrac{dy}{dx}\) and of \(\dfrac{d^2y}{dx^2}\) at the point \((1, 1)\).
Differentiate with respect to \(x\), using the product rule on \(xy\):
\[2x + y + x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0\] [M1 A1]
At \((1, 1)\): \(3 + 3\dfrac{dy}{dx} = 0\), so \(\dfrac{dy}{dx} = -1\). [A1]

Differentiate again. The term \(y + x\dfrac{dy}{dx}\) gives \(\dfrac{dy}{dx} + \dfrac{dy}{dx} + x\dfrac{d^2y}{dx^2}\), and \(2y\dfrac{dy}{dx}\) gives \(2\left(\dfrac{dy}{dx}\right)^2 + 2y\dfrac{d^2y}{dx^2}\):
\[2 + 2\frac{dy}{dx} + x\frac{d^2y}{dx^2} + 2\left(\frac{dy}{dx}\right)^2 + 2y\frac{d^2y}{dx^2} = 0\] [M1 A1]
At \((1, 1)\) with \(\dfrac{dy}{dx} = -1\):
\[2 - 2 + \frac{d^2y}{dx^2} + 2 + 2\frac{d^2y}{dx^2} = 0 \quad\Rightarrow\quad \frac{d^2y}{dx^2} = -\frac23\] [A1]
**Check**: near \((1, 1)\) the curve is \(y = \dfrac{-x + \sqrt{12 - 3x^2}}{2}\), which gives \(y = 1.0968\) at \(x = 0.9\) and \(y = 0.8966\) at \(x = 1.1\). The second difference \(\dfrac{1.0968 + 0.8966 - 2}{0.1^2} = -0.66\) agrees with \(-\tfrac23\).
:::

An alternative is to solve first for \(\dfrac{dy}{dx}\) as a fraction in \(x\) and \(y\), then differentiate the fraction by the quotient rule. It usually leads to more algebra: differentiating the equation again, as above, and substituting the numbers at the end is quicker.

### Parametric curves

If \(x = x(t)\) and \(y = y(t)\), the first derivative is \(\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}\). The second derivative asks how this gradient changes with \(x\), not with \(t\), so the chain rule is needed again.

:::key Second derivative of a parametric curve
\[\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)}{\dfrac{dx}{dt}}\]
Find \(\dfrac{dy}{dx}\) as a function of \(t\), differentiate that with respect to \(t\), then divide by \(\dfrac{dx}{dt}\).
:::

:::warn Do not divide the second derivatives
\(\dfrac{d^2y}{dx^2} \ne \dfrac{d^2y/dt^2}{d^2x/dt^2}\). That quotient has no meaning. This is the most common slip in this topic and it loses every mark after the first derivative.
:::

:::eg (Exam style) A curve has parametric equations \(x = \cosh t\), \(y = \sinh t\). Show that \(\dfrac{d^2y}{dx^2} = -\operatorname{cosech}^3 t\) for \(t \ne 0\).
\[\frac{dx}{dt} = \sinh t, \qquad \frac{dy}{dt} = \cosh t\]
\[\frac{dy}{dx} = \frac{\cosh t}{\sinh t} = \coth t\] [M1 A1]
Differentiate this with respect to \(t\), and divide by \(\dfrac{dx}{dt}\):
\[\frac{d^2y}{dx^2} = \frac{-\operatorname{cosech}^2 t}{\sinh t}\] [M1]
\[= -\operatorname{cosech}^3 t\] [A1]
**Check** with the Cartesian form: the curve is \(x^2 - y^2 = 1\), and differentiating implicitly twice gives \(\dfrac{d^2y}{dx^2} = -\dfrac{1}{y^3}\), the same as \(-\operatorname{cosech}^3 t\) since \(y = \sinh t\).
:::

:::eg (Exam style) A curve has parametric equations \(x = t^2 + 1\), \(y = t^3 - 3t\). (a) Show that \(\dfrac{dy}{dx} = \dfrac{3(t^2 - 1)}{2t}\). (b) Find \(\dfrac{d^2y}{dx^2}\) in terms of \(t\). (c) Find the coordinates of the stationary points and determine their nature.
(a) \(\dfrac{dx}{dt} = 2t\) and \(\dfrac{dy}{dt} = 3t^2 - 3\), so
\[\frac{dy}{dx} = \frac{3t^2 - 3}{2t} = \frac{3(t^2 - 1)}{2t}\] [M1 A1]
(b) Write \(\dfrac{dy}{dx} = \dfrac32\left(t - \dfrac1t\right)\). Differentiate with respect to \(t\):
\[\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac32\left(1 + \frac{1}{t^2}\right)\] [M1]
Divide by \(\dfrac{dx}{dt} = 2t\):
\[\frac{d^2y}{dx^2} = \frac{3\left(1 + t^{-2}\right)}{4t} = \frac{3\left(t^2 + 1\right)}{4t^3}\] [A1]
(c) Stationary points: \(\dfrac{dy}{dx} = 0\) gives \(t^2 = 1\), so \(t = \pm1\). [B1]

For \(t = 1\): \((x, y) = (2, -2)\). For \(t = -1\): \((x, y) = (2, 2)\). [B1]

At \(t = 1\), \(\dfrac{d^2y}{dx^2} = \dfrac{3 \times 2}{4} = \dfrac32 > 0\): a minimum. [M1]

At \(t = -1\), \(\dfrac{d^2y}{dx^2} = \dfrac{3 \times 2}{-4} = -\dfrac32 < 0\): a maximum. [A1]
:::

:::eg (Exam style) A curve has parametric equations \(x = 2\sinh t\), \(y = \cosh 2t\). Find \(\dfrac{d^2y}{dx^2}\) and explain your answer by writing \(y\) in terms of \(x\).
\[\frac{dx}{dt} = 2\cosh t, \qquad \frac{dy}{dt} = 2\sinh 2t = 4\sinh t\cosh t\]
\[\frac{dy}{dx} = \frac{4\sinh t\cosh t}{2\cosh t} = 2\sinh t\] [M1 A1]
\[\frac{d^2y}{dx^2} = \frac{2\cosh t}{2\cosh t} = 1\] [M1 A1]
The Cartesian form agrees: \(y = \cosh 2t = 1 + 2\sinh^2 t = 1 + \dfrac{x^2}{2}\), a parabola whose second derivative is the constant 1. [B1]
:::

## Maclaurin series

A polynomial \(a_0 + a_1x + a_2x^2 + a_3x^3 + \dots\) can be made to behave like a function \(f\) near \(x = 0\) by choosing its coefficients so that its value and derivatives at 0 match those of \(f\). The constant term must be \(f(0)\), the coefficient of \(x\) must be \(f'(0)\), and so on. Each time you differentiate a term \(a_nx^n\) \(n\) times, you get \(n!\,a_n\), which is why factorials appear.

:::proof Where the coefficients come from
Suppose \(f(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + \dots\) near \(x = 0\).
Put \(x = 0\): all terms except the first vanish, so \(f(0) = a_0\).
Differentiate: \(f'(x) = a_1 + 2a_2x + 3a_3x^2 + \dots\). Put \(x = 0\): \(f'(0) = a_1\).
Differentiate again: \(f''(x) = 2a_2 + 6a_3x + \dots\), so \(f''(0) = 2a_2\), that is \(a_2 = \dfrac{f''(0)}{2!}\).
Again: \(f'''(x) = 6a_3 + \dots\), so \(a_3 = \dfrac{f'''(0)}{3!}\).
Each differentiation of \(a_rx^r\) \(r\) times leaves \(r!\,a_r\) and kills the lower terms, so \(a_r = \dfrac{f^{(r)}(0)}{r!}\).
This assumes that \(f\) can be written as a power series: the syllabus does not ask you to prove that, or to derive the general term.
:::

:::def Maclaurin series
The power series \(f(0) + xf'(0) + \dfrac{x^2}{2!}f''(0) + \dots\) built from the derivatives of \(f\) at \(x = 0\). Stopping after the term in \(x^n\) gives the Maclaurin polynomial of degree \(n\).
:::

:::def Range of validity
The set of values of \(x\) for which the infinite series converges to the function. Inside it, adding more terms improves the approximation; outside it, the partial sums move away from the function.
:::

:::key Maclaurin series (in MF19)
\[f(x) = f(0) + xf'(0) + \frac{x^2}{2!}f''(0) + \dots + \frac{x^r}{r!}f^{(r)}(0) + \dots\]
The more terms you keep, the better the polynomial matches \(f\) near 0. A series with terms up to \(x^n\) is called a polynomial of degree \(n\). The series is only a faithful copy of \(f\) for \(x\) in its **range of validity**.
:::

:::eg (Exam style) Use successive differentiation to find the Maclaurin series of \(\ln(1 + x)\) up to and including the term in \(x^3\).
\[\begin{aligned}
f(x) &= \ln(1 + x) & f(0) &= 0 \\
f'(x) &= (1 + x)^{-1} & f'(0) &= 1 \\
f''(x) &= -(1 + x)^{-2} & f''(0) &= -1 \\
f'''(x) &= 2(1 + x)^{-3} & f'''(0) &= 2
\end{aligned}\] [M1 A1]
Substitute into the formula:
\[\ln(1 + x) = 0 + x(1) + \frac{x^2}{2!}(-1) + \frac{x^3}{3!}(2) = x - \frac{x^2}{2} + \frac{x^3}{3}\] [M1 A1]
:::

The standard series are in MF19, so you rarely derive them. You must know how to use them.

:::key Standard series in MF19, with their ranges of validity
\[\begin{aligned}
e^x &= 1 + x + \frac{x^2}{2!} + \dots + \frac{x^r}{r!} + \dots && \text{all } x \\
\ln(1 + x) &= x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + \frac{(-1)^{r+1}x^r}{r} + \dots && -1 < x \le 1 \\
\sin x &= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots + \frac{(-1)^rx^{2r+1}}{(2r + 1)!} + \dots && \text{all } x \\
\cos x &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots + \frac{(-1)^rx^{2r}}{(2r)!} + \dots && \text{all } x \\
\tan^{-1}x &= x - \frac{x^3}{3} + \frac{x^5}{5} - \dots + \frac{(-1)^rx^{2r+1}}{2r + 1} + \dots && -1 \le x \le 1 \\
\sinh x &= x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots + \frac{x^{2r+1}}{(2r + 1)!} + \dots && \text{all } x \\
\cosh x &= 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots + \frac{x^{2r}}{(2r)!} + \dots && \text{all } x \\
\tanh^{-1}x &= x + \frac{x^3}{3} + \frac{x^5}{5} + \dots + \frac{x^{2r+1}}{2r + 1} + \dots && -1 < x < 1
\end{aligned}\]
The binomial series \((1 + x)^n\) (\(\lvert x \rvert < 1\) for non-integer \(n\)) is also given, from [Modulus and polynomials](#math.p3.algebra). Series for \(\tan x\), \(\sec x\), \(\sin^{-1}x\), \(\tanh x\), \(\sinh^{-1}x\) and combinations are **not** given: derive them.
:::

Compare the \(\sinh\) and \(\sin\) series: the same terms, but the hyperbolic one has no alternating signs. The same goes for \(\cosh\) and \(\cos\), and \(\tanh^{-1}\) and \(\tan^{-1}\).

To get a series for a function of \(2x\), or \(x^2\), or \(-x\), substitute into a standard series: replacing \(x\) by \(2x\) in the series for \(e^x\) gives \(1 + 2x + \dfrac{4x^2}{2} + \dfrac{8x^3}{6} + \dots\). The range of validity changes with the substitution: the \(\ln(1 + 2x)\) series needs \(-1 < 2x \le 1\), that is \(-\tfrac12 < x \le \tfrac12\).

### Seeing the polynomial approach the function

The widget below draws a function and its Maclaurin polynomial of the degree you choose. Start with \(\sin x\) and slide the degree up from 1: the polynomial hugs the curve near 0 and the match spreads outwards. Then choose \(\ln(1 + x)\) or \(\tan^{-1}x\): the polynomial follows the curve only inside the range of validity, and flies off outside it, however many terms you add. Move the \(x_0\) slider to see the error \(f(x_0) - p(x_0)\) shrink near 0 and blow up far from it.

:::html
<div class="widget" data-w="fm-maclaurin" data-f="sin" data-n="3" data-x="-6,6"></div>
:::

### Combining series

:::eg (Exam style) Find the Maclaurin series for \(e^{2x}\sin x\) up to and including the term in \(x^3\).
Write the two standard series, replacing \(x\) by \(2x\) in the first:
\[e^{2x} = 1 + 2x + 2x^2 + \tfrac43x^3 + \dots \qquad \sin x = x - \tfrac16x^3 + \dots\] [M1 A1]
Multiply, keeping only terms up to \(x^3\):
\[\begin{aligned}
e^{2x}\sin x &= x + 2x^2 + 2x^3 - \tfrac16x^3 + \dots \\
&= x + 2x^2 + \tfrac{11}{6}x^3 + \dots
\end{aligned}\] [M1 A1]
Here \(2x^3\) comes from \(2x^2 \times x\) and \(-\tfrac16x^3\) from \(1 \times \left(-\tfrac16x^3\right)\). Terms like \(2x \times \left(-\tfrac16x^3\right)\) have degree 4, so they are dropped.
:::

:::eg Find the series for \(\ln(1 + \sin x)\) up to \(x^3\) by substituting \(u = \sin x\) into \(\ln(1 + u)\). Then confirm it by differentiating.
\[\sin x = x - \tfrac16x^3 + \dots, \quad \ln(1 + u) = u - \tfrac12u^2 + \tfrac13u^3 - \dots\]
Substitute and keep terms to \(x^3\): \(u = x - \tfrac16x^3\), \(u^2 = x^2 + \dots\) (the next term is degree 4) and \(u^3 = x^3 + \dots\):
\[\ln(1 + \sin x) = x - \tfrac16x^3 - \tfrac12x^2 + \tfrac13x^3 = x - \tfrac12x^2 + \tfrac16x^3\]
**By differentiation**: \(f(x) = \ln(1 + \sin x)\), \(f(0) = 0\).
\[\begin{aligned}
f'(x) &= \frac{\cos x}{1 + \sin x} & f'(0) &= 1 \\
f''(x) &= \frac{-\sin x(1 + \sin x) - \cos^2x}{(1 + \sin x)^2} = \frac{-1}{1 + \sin x} & f''(0) &= -1 \\
f'''(x) &= \frac{\cos x}{(1 + \sin x)^2} & f'''(0) &= 1
\end{aligned}\]
So the series is \(x - \dfrac{x^2}{2} + \dfrac{x^3}{6}\), the same.
:::

:::eg (Exam style) Find the Maclaurin series for \(\sec x\) up to and including the term in \(x^4\), using the series for \(\cos x\) and the binomial series.
\[\sec x = \frac{1}{\cos x} = \left(1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots\right)^{-1}\] [M1]
Write \(\cos x = 1 - u\) with \(u = \dfrac{x^2}{2} - \dfrac{x^4}{24}\). Then \(\dfrac{1}{1 - u} = 1 + u + u^2 + \dots\) [M1]
\[\begin{aligned}
\sec x &= 1 + \left(\frac{x^2}{2} - \frac{x^4}{24}\right) + \left(\frac{x^2}{2}\right)^2 + \dots \\
&= 1 + \frac{x^2}{2} + \left(\frac14 - \frac1{24}\right)x^4 + \dots
\end{aligned}\] [A1]
\[\sec x = 1 + \frac{x^2}{2} + \frac{5x^4}{24} + \dots\] [A1]
Only \(u\) and \(u^2\) are needed: \(u^3\) starts at \(x^6\).
:::

:::eg Use the binomial series to find the Maclaurin series of \(\sinh^{-1}x\) up to the term in \(x^5\), by working from its derivative. Then do the same for \(\tanh^{-1}x\).
The derivative is \(\dfrac{d}{dx}\sinh^{-1}x = \left(1 + x^2\right)^{-1/2}\). The binomial series with \(x\) replaced by \(x^2\) is
\[\left(1 + x^2\right)^{-1/2} = 1 - \tfrac12x^2 + \tfrac38x^4 - \dots\]
Integrate term by term. The constant of integration is \(\sinh^{-1}0 = 0\):
\[\sinh^{-1}x = x - \frac{x^3}{6} + \frac{3x^5}{40} - \dots\]
For \(\tanh^{-1}x\) the derivative is \(\dfrac{1}{1 - x^2} = 1 + x^2 + x^4 + \dots\), so \(\tanh^{-1}x = x + \dfrac{x^3}{3} + \dfrac{x^5}{5} + \dots\), which is the MF19 series. This "differentiate, expand, integrate" route is often quicker than successive differentiation.
:::

When you multiply two series, decide how many terms each needs: to get all terms up to \(x^n\) in the product, keep terms up to \(x^n\) in both.

### Successive differentiation

Some functions have a derivative that is expressed using the function itself. Then each new derivative can be found by differentiating that relation, which is easier than differentiating the original. The classic case is \(y = \tan x\): since \(\dfrac{dy}{dx} = \sec^2x = 1 + \tan^2x\), we have \(y' = 1 + y^2\).

:::eg (Exam style) Given that \(y = \tan x\), show that \(\dfrac{dy}{dx} = 1 + y^2\). Hence find the Maclaurin series of \(\tan x\) up to and including the term in \(x^5\).
\(\dfrac{dy}{dx} = \sec^2x = 1 + \tan^2x = 1 + y^2\). [B1]

Differentiate the relation repeatedly, using the chain rule and then the product rule:
\[\begin{aligned}
y'' &= 2yy' \\
y''' &= 2(y')^2 + 2yy'' \\
y^{(4)} &= 4y'y'' + 2y'y'' + 2yy''' = 6y'y'' + 2yy''' \\
y^{(5)} &= 6(y'')^2 + 6y'y''' + 2y'y''' + 2yy^{(4)}
\end{aligned}\] [M1 A1]
At \(x = 0\): \(y = 0\) and \(y' = 1 + 0 = 1\). Then
\[y'' = 0, \quad y''' = 2, \quad y^{(4)} = 0, \quad y^{(5)} = 8 \times 1 \times 2 = 16\] [M1 A1]
\[\tan x = x + \frac{2x^3}{3!} + \frac{16x^5}{5!} = x + \frac{x^3}{3} + \frac{2x^5}{15} + \dots\] [A1]
:::

:::eg (Exam style) Given that \(y = e^{\sin x}\), show that \(\dfrac{dy}{dx} = y\cos x\). Hence find the Maclaurin series of \(y\) up to and including the term in \(x^3\).
\(\dfrac{dy}{dx} = e^{\sin x}\cos x = y\cos x\). [B1]

Differentiate again with the product rule:
\[\begin{aligned}
y'' &= y'\cos x - y\sin x \\
y''' &= y''\cos x - 2y'\sin x - y\cos x
\end{aligned}\] [M1 A1]
At \(x = 0\): \(y = 1\), \(y' = 1\), \(y'' = 1\), \(y''' = 1 - 0 - 1 = 0\). [M1]
\[e^{\sin x} = 1 + x + \frac{x^2}{2} + 0\times x^3 + \dots\] [A1]
The term in \(x^3\) is zero. The next non-zero term is \(-\tfrac18x^4\), which you can find by composing the series for \(e^u\) with \(u = \sin x\).
:::

:::warn Truncating and factorials
Two slips cost most marks in this topic. Dividing by the wrong factorial: the coefficient of \(x^3\) is \(f'''(0)/3! = f'''(0)/6\), never \(f'''(0)/3\). And dropping terms too early in a product: if you need terms up to \(x^3\), the product \(e^{2x}\sin x\) needs the \(x^2\) term of \(e^{2x}\) and the \(x\) term of \(\sin x\), as well as the \(x^3\) term of \(\sin x\).
:::

### Using a series

A Maclaurin polynomial is a way to calculate. For \(x\) inside the range of validity and near 0, the first few terms give a good estimate. A series also lets you find a limit when direct substitution gives \(\dfrac00\).

:::eg Use the series for \(\ln(1 + x)\) to estimate \(\ln 1.1\) using terms up to \(x^4\), and compare with your calculator.
Put \(x = 0.1\) in \(\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dfrac{x^4}{4}\):
\[0.1 - 0.005 + 0.000333 - 0.000025 = 0.095308\]
The calculator gives \(\ln 1.1 = 0.095310\). The error is about \(2 \times 10^{-6}\), the size of the next term \(\dfrac{x^5}{5}\).
:::

:::eg (Exam style) Use Maclaurin series to find \(\displaystyle\lim_{x \to 0}\frac{\sinh x - x\cos x}{x^3}\).
Substituting \(x = 0\) gives \(\tfrac00\), so expand the numerator:
\[\sinh x = x + \frac{x^3}{6} + \dots \qquad x\cos x = x - \frac{x^3}{2} + \dots\] [M1 A1]
\[\sinh x - x\cos x = \left(\tfrac16 + \tfrac12\right)x^3 + \dots = \tfrac23x^3 + \dots\] [M1]
The terms in \(x\) cancel, and dividing by \(x^3\) leaves \(\tfrac23\) plus terms that tend to 0, so the limit is \(\tfrac23\). [A1]
:::

:::eg In a model of a hanging cable \(y = a\cosh\frac{x}{a}\). Use the Maclaurin series to show that when \(x\) is small compared with \(a\) the cable is close to the parabola \(y = a + \dfrac{x^2}{2a}\). Test this on the cable \(y = 25\cosh\frac{x}{25} - 19\) at \(x = 15\).
\[\cosh u = 1 + \frac{u^2}{2} + \frac{u^4}{24} + \dots\]
With \(u = \dfrac xa\): \(y = a\left(1 + \dfrac{x^2}{2a^2} + \dfrac{x^4}{24a^4} + \dots\right) = a + \dfrac{x^2}{2a} + \dots\) The first omitted term is \(\dfrac{x^4}{24a^3}\), small when \(\dfrac xa\) is small.

For the cable, with \(u = 0.6\): \(\cosh 0.6 = 1.18547\) exactly. The parabola gives \(1 + 0.18 = 1.18\), so \(y = 25(1.18) - 19 = 10.50\). With the quartic term, \(1 + 0.18 + 0.0054 = 1.1854\) and \(y = 10.635\). The exact height is \(10.637\) m, so the parabola is about 0.14 m too low at the pole, and the quartic term brings it within 0.002 m.
:::

:::eg A student approximates \(\sin\theta\) by \(\theta\) for a swinging pendulum with a maximum angle of \(0.5\) radians. Find the percentage error in \(\sin 0.5\), and the percentage error if the term in \(\theta^3\) is kept.
\(\sin 0.5 = 0.479426\). Using \(\theta\) alone gives \(0.5\):
\[\text{error} = \frac{0.5 - 0.479426}{0.479426} \times 100 = 4.29\%\]
With the cubic term, \(0.5 - \dfrac{0.5^3}{6} = 0.5 - 0.020833 = 0.479167\), so
\[\text{error} = \frac{0.479426 - 0.479167}{0.479426} \times 100 = 0.0540\%\]
One extra term cuts the error by a factor of about 80. For a larger angle the first approximation gets worse quickly.
:::

:::exam What MF19 gives you in this chapter
MF19 gives the derivatives of \(\sinh x\), \(\cosh x\), \(\tanh x\), \(\sin^{-1}x\), \(\cos^{-1}x\), \(\sinh^{-1}x\), \(\cosh^{-1}x\) and \(\tanh^{-1}x\), the general Maclaurin series and the standard series listed in the key box above. It does **not** give the derivatives of \(\operatorname{sech}\), \(\operatorname{cosech}\) and \(\coth\), nor the series for \(\tan x\), \(\sec x\) and \(\sin^{-1}x\). "Show that" questions want the derivation (quotient rule, implicit differentiation) even when the result is in MF19. Say which series you are using, state the validity if the question asks, and write "up to and including the term in \(x^n\)" in your own head: a missing term loses the accuracy mark.
:::

:::board
UK Further Maths (Edexcel 9FM0 Core Pure, AQA 7367) includes Maclaurin series and hyperbolic functions, with the same methods as here. Neither is part of single A Level Mathematics.
:::

:::eg Spot the error: a curve has parametric equations \(x = t^3 + t\), \(y = t^2\). Find \(\dfrac{d^2y}{dx^2}\) in terms of \(t\), for 4 marks.
A student wrote this answer.

Line 1: \(\dfrac{dy}{dx} = \dfrac{2t}{3t^2 + 1}\)
Line 2: \(\dfrac{d^2y}{dx^2} = \dfrac{d^2y/dt^2}{d^2x/dt^2} = \dfrac{2}{6t} = \dfrac{1}{3t}\)

Line 1 is correct and earns the first two marks. [M1] [A1]

**Line 2 uses a wrong method, so the next two marks are lost.** [M0] [A0] The quotient of the two second derivatives is not \(\dfrac{d^2y}{dx^2}\): you must differentiate \(\dfrac{dy}{dx}\) with respect to \(t\), then divide by \(\dfrac{dx}{dt}\). The student scores 2 out of 4.

Correct line 2:
\[\frac{d}{dt}\left(\frac{2t}{3t^2 + 1}\right) = \frac{2\left(3t^2 + 1\right) - 2t(6t)}{\left(3t^2 + 1\right)^2} = \frac{2 - 6t^2}{\left(3t^2 + 1\right)^2}\] [M1]
Divide by \(\dfrac{dx}{dt} = 3t^2 + 1\):
\[\frac{d^2y}{dx^2} = \frac{2 - 6t^2}{\left(3t^2 + 1\right)^3}\] [A1]
**Check** at \(t = 0\): the curve near the origin is \(y \approx x^2\) (since \(x \approx t\)), whose second derivative is 2, and the formula gives \(\dfrac{2}{1} = 2\).
:::

:::try Start easy, finish at exam standard
Q: Differentiate (a) \(\cosh 5x\), (b) \(\sinh x\cosh x\), (c) \(\coth 2x\).
A: (a) \(5\sinh 5x\). (b) \(\cosh^2x + \sinh^2x\) (that is \(\cosh 2x\)). (c) \(-2\operatorname{cosech}^2 2x\).
Q: Find \(\dfrac{d}{dx}\left(e^{3x}\tanh x\right)\).
A: Product rule: \(3e^{3x}\tanh x + e^{3x}\operatorname{sech}^2x = e^{3x}\left(3\tanh x + \operatorname{sech}^2x\right)\).
Q: Differentiate (a) \(\sin^{-1}3x\), (b) \(\cosh^{-1}(2x)\), (c) \(\tanh^{-1}\left(x^3\right)\).
A: (a) \(\dfrac{3}{\sqrt{1 - 9x^2}}\). (b) \(\dfrac{2}{\sqrt{4x^2 - 1}}\). (c) \(\dfrac{3x^2}{1 - x^6}\).
Q: Show that if \(y = A\cosh kx + B\sinh kx\) then \(\dfrac{d^2y}{dx^2} = k^2y\).
A: \(\dfrac{dy}{dx} = Ak\sinh kx + Bk\cosh kx\) and \(\dfrac{d^2y}{dx^2} = Ak^2\cosh kx + Bk^2\sinh kx = k^2y\).
Q: Find the gradient of \(y = x\sinh^{-1}x\) at \(x = \tfrac34\), in exact form.
A: \(\dfrac{dy}{dx} = \sinh^{-1}x + \dfrac{x}{\sqrt{x^2 + 1}}\). At \(x = \tfrac34\), \(\sqrt{\tfrac{9}{16} + 1} = \tfrac54\), so \(\sinh^{-1}\tfrac34 = \ln 2\) and the gradient is \(\ln 2 + \dfrac{3/4}{5/4} = \ln 2 + \tfrac35\).
Q: The curve \(x^3 + y^3 = 9xy\) passes through \((2, 4)\). Show that \(\dfrac{dy}{dx} = \dfrac{3y - x^2}{y^2 - 3x}\) and find its value at \((2, 4)\).
A: \(3x^2 + 3y^2y' = 9y + 9xy'\), so \(y'\left(3y^2 - 9x\right) = 9y - 3x^2\) and \(y' = \dfrac{3y - x^2}{y^2 - 3x}\). At \((2, 4)\): \(\dfrac{12 - 4}{16 - 6} = \dfrac45\).
Q: Write down the Maclaurin series for \(\cosh 2x\) up to \(x^4\), and for \(\dfrac{1}{1 + x}\) up to \(x^3\).
A: \(\cosh 2x = 1 + \dfrac{(2x)^2}{2} + \dfrac{(2x)^4}{24} = 1 + 2x^2 + \tfrac23x^4\). \(\dfrac{1}{1 + x} = 1 - x + x^2 - x^3\).
Q: Find the series for \(\ln(1 - x)\) and give its range of validity.
A: Replace \(x\) by \(-x\) in \(\ln(1 + x)\): \(-x - \dfrac{x^2}{2} - \dfrac{x^3}{3} - \dots\), valid for \(-1 \le x < 1\) (since \(-1 < -x \le 1\)).
Q: Find the Maclaurin series of \(\sin^{-1}x\) up to \(x^3\) by successive differentiation.
A: \(f' = (1 - x^2)^{-1/2}\), \(f'(0) = 1\). \(f'' = x(1 - x^2)^{-3/2}\), \(f''(0) = 0\). \(f''' = (1 - x^2)^{-3/2} + 3x^2(1 - x^2)^{-5/2}\), \(f'''(0) = 1\). With \(f(0) = 0\): \(\sin^{-1}x = x + \dfrac{x^3}{6} + \dots\).
Q: Use \(\sin x\) and \(\cos x\) series to find \(\displaystyle\lim_{x \to 0}\frac{\cos x - 1 + \frac12x^2}{x^4}\).
A: \(\cos x - 1 + \tfrac12x^2 = \dfrac{x^4}{24} - \dots\), so the limit is \(\dfrac{1}{24}\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Differentiate with respect to \(x\), simplifying where possible: (a) \(x\sinh 4x\), (b) \(\ln\cosh 5x\).
A: (a) \(\sinh 4x + 4x\cosh 4x\). [M1 A1]
(b) \(\dfrac{5\sinh 5x}{\cosh 5x} = 5\tanh 5x\). [M1 A1]
Q: [3 marks] ★ Starting from \(\coth x = \dfrac{\cosh x}{\sinh x}\), show that \(\dfrac{d}{dx}\coth x = -\operatorname{cosech}^2x\).
A: Quotient rule: \(\dfrac{\sinh x\cdot\sinh x - \cosh x\cdot\cosh x}{\sinh^2x}\) [M1 A1]
\[= \frac{-1}{\sinh^2x} = -\operatorname{cosech}^2x\] [A1]
Q: [5 marks] ★★ (a) Find \(\dfrac{d}{dx}\cosh^{-1}(2x + 1)\), simplifying your answer. (b) Given that \(y = \tanh^{-1}(\sin x)\), show that \(\dfrac{dy}{dx} = \sec x\).
A: (a) \(\dfrac{2}{\sqrt{(2x + 1)^2 - 1}}\) [M1] \(= \dfrac{2}{\sqrt{4x^2 + 4x}} = \dfrac{1}{\sqrt{x^2 + x}}\). [A1]
(b) \(\dfrac{dy}{dx} = \dfrac{\cos x}{1 - \sin^2x}\) [M1 A1] \(= \dfrac{\cos x}{\cos^2x} = \sec x\). [A1]
Q: [6 marks] ★★ The curve \(x^3 + y^3 = 6xy\) passes through the point \((3, 3)\). Find the value of \(\dfrac{dy}{dx}\) and of \(\dfrac{d^2y}{dx^2}\) at this point.
A: Differentiate: \(3x^2 + 3y^2\dfrac{dy}{dx} = 6y + 6x\dfrac{dy}{dx}\). [M1 A1]
At \((3, 3)\): \(27 + 27y' = 18 + 18y'\), so \(\dfrac{dy}{dx} = -1\). [A1]
Differentiate \(x^2 + y^2y' = 2y + 2xy'\) again:
\[2x + 2y(y')^2 + y^2y'' = 2y' + 2y' + 2xy''\] [M1 A1]
At \((3, 3)\): \(6 + 6 + 9y'' = -4 + 6y''\), so \(\dfrac{d^2y}{dx^2} = -\dfrac{16}{3}\). [A1]
Q: [5 marks] ★★ A curve has parametric equations \(x = 2\sinh t\), \(y = \cosh 2t\). Find \(\dfrac{d^2y}{dx^2}\), and confirm your answer from the Cartesian equation.
A: \(\dfrac{dy}{dx} = \dfrac{2\sinh 2t}{2\cosh t} = 2\sinh t\). [M1 A1]
\(\dfrac{d^2y}{dx^2} = \dfrac{2\cosh t}{2\cosh t} = 1\). [M1 A1]
Cartesian: \(y = 1 + 2\sinh^2t = 1 + \dfrac{x^2}{2}\), so \(\dfrac{d^2y}{dx^2} = 1\). [B1]
Q: [6 marks] ★★ (a) Find the Maclaurin series for \(e^x\cos x\) up to and including the term in \(x^3\). (b) Hence find \(\displaystyle\lim_{x \to 0}\frac{e^x\cos x - 1 - x}{x^3}\).
A: (a) \(\left(1 + x + \tfrac{x^2}{2} + \tfrac{x^3}{6}\right)\left(1 - \tfrac{x^2}{2}\right)\) [M1 A1]
\[= 1 + x + \tfrac{x^2}{2} - \tfrac{x^2}{2} + \tfrac{x^3}{6} - \tfrac{x^3}{2} = 1 + x - \tfrac13x^3\] [M1 A1]
(b) \(e^x\cos x - 1 - x = -\tfrac13x^3 + \dots\) [M1], so the limit is \(-\tfrac13\). [A1]
Q: [8 marks] (#math.p3.diffeq) ★★★ A function \(y\) satisfies \(\dfrac{dy}{dx} = x + y^2\), with \(y = 1\) when \(x = 0\). (a) Show that \(\dfrac{d^2y}{dx^2} = 1 + 2y\dfrac{dy}{dx}\) and find an expression for \(\dfrac{d^3y}{dx^3}\). (b) Find the Maclaurin series for \(y\) up to and including the term in \(x^3\). (c) Use it to estimate \(y\) when \(x = 0.1\).
H: Differentiate \(\dfrac{dy}{dx} = x + y^2\) with respect to \(x\); \(y^2\) needs the chain rule.
H: For the third derivative differentiate \(1 + 2y\dfrac{dy}{dx}\) with the product rule.
H: Evaluate each derivative at \(x = 0\) using \(y = 1\), then \(y' = 0 + 1 = 1\).
A: (a) \(y'' = 1 + 2yy'\) [M1 A1], \(y''' = 2(y')^2 + 2yy''\). [A1]
(b) \(y(0) = 1\), \(y'(0) = 1\), \(y''(0) = 1 + 2 = 3\), \(y'''(0) = 2 + 2(3) = 8\). [B1]
\[y = 1 + x + \frac{3x^2}{2} + \frac{8x^3}{6} = 1 + x + \tfrac32x^2 + \tfrac43x^3\] [M1 A1]
(c) \(y(0.1) \approx 1 + 0.1 + 0.015 + 0.001333\) [M1] \(= 1.116\) (4 s.f.). [A1]
Q: [11 marks] (#math.fm.hyperbolic) ★★★ Let \(y = \left(\sin^{-1}x\right)^2\) for \(-1 < x < 1\). (a) Show that \(\left(1 - x^2\right)\dfrac{d^2y}{dx^2} - x\dfrac{dy}{dx} = 2\). (b) Differentiate this equation to show that \(\left(1 - x^2\right)y''' - 3xy'' - y' = 0\). (c) Find the Maclaurin series for \(y\) up to and including the term in \(x^4\).
H: Find \(y'\) first: it is \(\dfrac{2\sin^{-1}x}{\sqrt{1 - x^2}}\). Rearrange to \(\sqrt{1 - x^2}\,y' = 2\sin^{-1}x\) before differentiating again.
H: In (b), differentiate each term of \(\left(1 - x^2\right)y'' - xy' = 2\) with the product rule.
H: For \(y^{(4)}\) differentiate the result of (b) once more and put \(x = 0\).
A: (a) \(y' = \dfrac{2\sin^{-1}x}{\sqrt{1 - x^2}}\), so \(\sqrt{1 - x^2}\,y' = 2\sin^{-1}x\). [M1 A1]
Differentiate: \(\sqrt{1 - x^2}\,y'' - \dfrac{x}{\sqrt{1 - x^2}}y' = \dfrac{2}{\sqrt{1 - x^2}}\). [M1]
Multiply by \(\sqrt{1 - x^2}\): \(\left(1 - x^2\right)y'' - xy' = 2\). [A1]
(b) \(\left(1 - x^2\right)y''' - 2xy'' - xy'' - y' = 0\) [M1], so \(\left(1 - x^2\right)y''' - 3xy'' - y' = 0\). [A1]
(c) \(y(0) = 0\), \(y'(0) = 0\), and from (a) \(y''(0) = 2\). [B1] From (b), \(y'''(0) = 0\). [B1]
Differentiating (b):
\[\left(1 - x^2\right)y^{(4)} - 2xy''' - 3xy''' - 3y'' - y'' = 0\]
that is \(\left(1 - x^2\right)y^{(4)} - 5xy''' - 4y'' = 0\). [M1] At 0: \(y^{(4)}(0) = 4 \times 2 = 8\). [A1]
\[y = \frac{2x^2}{2!} + \frac{8x^4}{4!} = x^2 + \frac{x^4}{3} + \dots\] [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ Let \(t = \tanh x\). (a) Show that \(\dfrac{dt}{dx} = 1 - t^2\). (b) Use this relation to find the Maclaurin series of \(\tanh x\) up to and including the term in \(x^5\). (c) By integrating your series, find the series for \(\ln\cosh x\) up to and including the term in \(x^6\).
H: In (b), differentiate \(t' = 1 - t^2\) repeatedly, as for \(\tan x\) with \(y' = 1 + y^2\), but with a different sign.
H: \(t(0) = 0\), \(t'(0) = 1\). Then \(t'' = -2tt'\) and so on.
H: In (c), \(\dfrac{d}{dx}\ln\cosh x = \tanh x\), and \(\ln\cosh 0 = 0\).
A: (a) \(\dfrac{dt}{dx} = \operatorname{sech}^2x = 1 - \tanh^2x = 1 - t^2\). [B1]
(b) \(t'' = -2tt'\), \(t''' = -2(t')^2 - 2tt''\), \(t^{(4)} = -6t't'' - 2tt'''\), \(t^{(5)} = -6(t'')^2 - 8t't''' - 2tt^{(4)}\). [M1 A1]
At \(0\): \(t = 0\), \(t' = 1\), \(t'' = 0\), \(t''' = -2\), \(t^{(4)} = 0\), \(t^{(5)} = 16\). [M1 A1]
\[\tanh x = x - \frac{2x^3}{6} + \frac{16x^5}{120} = x - \frac{x^3}{3} + \frac{2x^5}{15} - \dots\] [A1]
(c) \(\ln\cosh x = \int\tanh x\,dx = \dfrac{x^2}{2} - \dfrac{x^4}{12} + \dfrac{x^6}{45} + c\), and \(c = 0\) since \(\ln\cosh 0 = 0\). [M1 A1]
Q: [6 marks] ★★★ (a) Show that \(\ln\dfrac{1 + x}{1 - x} = 2\left(x + \dfrac{x^3}{3} + \dfrac{x^5}{5} + \dots\right)\) for \(\lvert x \rvert < 1\). (b) Choose \(x\) so that \(\dfrac{1 + x}{1 - x} = 2\), and use the first four terms of the series to estimate \(\ln 2\) to 4 decimal places.
H: Use \(\ln\dfrac{1 + x}{1 - x} = \ln(1 + x) - \ln(1 - x)\) and the series for each.
H: Solve \(\dfrac{1 + x}{1 - x} = 2\) for \(x\): a small value gives fast convergence.
A: (a) \(\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dots\) and \(\ln(1 - x) = -x - \dfrac{x^2}{2} - \dfrac{x^3}{3} - \dots\). [M1 A1]
Subtract: the even powers cancel and the odd powers double: \(2\left(x + \dfrac{x^3}{3} + \dfrac{x^5}{5} + \dots\right)\). [A1]
(b) \(1 + x = 2 - 2x\), so \(x = \tfrac13\). [B1]
\(\ln 2 \approx 2\left(\tfrac13 + \dfrac{1}{81} + \dfrac{1}{1215} + \dfrac{1}{15309}\right)\) [M1] \(= 0.6931\). [A1]
:::

:::quiz
? What is \(\dfrac{d}{dx}\cosh 3x\)?
+ \(3\sinh 3x\)
- \(-3\sinh 3x\)
- \(\sinh 3x\)
- \(3\cosh 3x\)
> \(\cosh\) differentiates to \(+\sinh\), and the chain rule brings out the factor 3. The minus sign belongs to \(\cos\); forgetting the 3 or keeping \(\cosh\) are the other slips.
? What is \(\dfrac{d}{dx}\tanh x\)?
- \(\cosh^2x\)
+ \(\operatorname{sech}^2x\)
- \(-\operatorname{sech}^2x\)
- \(\dfrac{1}{\sinh^2x}\)
> The quotient rule gives \(\dfrac{\cosh^2x - \sinh^2x}{\cosh^2x} = \operatorname{sech}^2x\). The minus version is \(\coth x\) differentiated, and \(\dfrac{1}{\sinh^2x}\) is \(\operatorname{cosech}^2x\).
? What is \(\dfrac{d}{dx}\cosh^{-1}x\) for \(x > 1\)?
- \(\dfrac{1}{\sqrt{1 - x^2}}\)
+ \(\dfrac{1}{\sqrt{x^2 - 1}}\)
- \(\dfrac{1}{\sqrt{x^2 + 1}}\)
- \(\dfrac{1}{x^2 - 1}\)
> From \(x = \cosh y\): \(\dfrac{dy}{dx} = \dfrac{1}{\sinh y} = \dfrac{1}{\sqrt{x^2 - 1}}\). The \(1 - x^2\) version is \(\sin^{-1}\), the plus version is \(\sinh^{-1}\), and no square root is the \(\tanh^{-1}\) pattern.
? For \(x = f(t)\), \(y = g(t)\), which formula is correct?
- \(\dfrac{d^2y}{dx^2} = \dfrac{d^2y/dt^2}{d^2x/dt^2}\)
- \(\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}\left(\dfrac{dy}{dx}\right) \times \dfrac{dx}{dt}\)
+ \(\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}\left(\dfrac{dy}{dx}\right) \div \dfrac{dx}{dt}\)
- \(\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)\)
> You want the rate of change of \(\dfrac{dy}{dx}\) with respect to \(x\), and \(\dfrac{d}{dx} = \dfrac{1}{dx/dt}\dfrac{d}{dt}\), so you divide by \(\dfrac{dx}{dt}\). Dividing second derivatives is the classic slip.
? What is the coefficient of \(x^3\) in the Maclaurin series of a function with \(f'''(0) = 12\)?
- 12
- 4
+ 2
- 36
> The coefficient is \(\dfrac{f'''(0)}{3!} = \dfrac{12}{6} = 2\). Using 12 forgets the factorial, 4 divides by 3, and 36 multiplies by 3.
? The series \(x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dots\) for \(\ln(1 + x)\) is valid for
+ \(-1 < x \le 1\)
- all real \(x\)
- \(-1 \le x \le 1\)
- \(\lvert x \rvert < \tfrac12\)
> At \(x = -1\), \(\ln 0\) is undefined, so \(-1\) is excluded; at \(x = 1\) the alternating series converges to \(\ln 2\), so 1 is included. Outside \([-1, 1]\) the terms grow.
? To find the series for \(e^{2x}\sin x\) up to \(x^3\), which terms are needed?
- \(e^{2x}\) up to \(x^3\) only
- \(\sin x\) up to \(x\) only
+ \(e^{2x}\) up to \(x^2\) and \(\sin x\) up to \(x^3\)
- both up to \(x^1\)
> Every pair of terms with total degree 3 or less must be present: \(x^2\) from \(e^{2x}\) times \(x\) from \(\sin x\), and \(1\) times \(x^3\). Truncating too early loses the \(x^3\) coefficient.
:::

:::checklist What you can now do
- [ ] I can differentiate \(\sinh\), \(\cosh\), \(\tanh\), \(\operatorname{sech}\), \(\operatorname{cosech}\) and \(\coth\), with the chain, product and quotient rules.
- [ ] I can derive the derivatives of \(\sin^{-1}x\), \(\cos^{-1}x\), \(\sinh^{-1}x\), \(\cosh^{-1}x\) and \(\tanh^{-1}x\), and use them with the chain rule.
- [ ] I can find \(\dfrac{d^2y}{dx^2}\) for a relation given implicitly, and evaluate it at a point.
- [ ] I can find \(\dfrac{d^2y}{dx^2}\) for a curve given parametrically, dividing by \(\dfrac{dx}{dt}\) and not by \(\dfrac{d^2x}{dt^2}\).
- [ ] I can derive the first few terms of a Maclaurin series by successive differentiation, including cases such as \(y' = 1 + y^2\) for \(\tan x\).
- [ ] I can use the standard series from MF19 and state their ranges of validity.
- [ ] I can combine series by substitution and multiplication, keeping exactly the terms needed.
- [ ] I can use a series to approximate a value or to find a limit.
:::

:::recap
- \(\dfrac{d}{dx}\sinh x = \cosh x\), \(\dfrac{d}{dx}\cosh x = \sinh x\), \(\dfrac{d}{dx}\tanh x = \operatorname{sech}^2x\); \(\operatorname{sech}\), \(\operatorname{cosech}\), \(\coth\) have a minus sign: \(-\operatorname{sech}x\tanh x\), \(-\operatorname{cosech}x\coth x\), \(-\operatorname{cosech}^2x\).
- \(\dfrac{d}{dx}\sin^{-1}x = \dfrac{1}{\sqrt{1 - x^2}}\), \(\dfrac{d}{dx}\sinh^{-1}x = \dfrac{1}{\sqrt{x^2 + 1}}\), \(\dfrac{d}{dx}\cosh^{-1}x = \dfrac{1}{\sqrt{x^2 - 1}}\), \(\dfrac{d}{dx}\tanh^{-1}x = \dfrac{1}{1 - x^2}\), \(\dfrac{d}{dx}\tan^{-1}x = \dfrac{1}{1 + x^2}\). Derive from \(x = f(y)\) and \(\dfrac{dy}{dx} = \dfrac{1}{f'(y)}\).
- Implicit second derivative: differentiate the equation twice, product rule on \(xy\) and \(y\,y'\) terms, substitute at the end.
- Parametric: \(\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}\left(\dfrac{dy}{dx}\right) \div \dfrac{dx}{dt}\).
- Maclaurin: \(f(x) = f(0) + xf'(0) + \dfrac{x^2}{2!}f''(0) + \dots\); the coefficient of \(x^r\) is \(f^{(r)}(0)/r!\).
- MF19 series: \(e^x\), \(\ln(1 + x)\) (\(-1 < x \le 1\)), \(\sin x\), \(\cos x\), \(\tan^{-1}x\) (\(-1 \le x \le 1\)), \(\sinh x\), \(\cosh x\), \(\tanh^{-1}x\) (\(-1 < x < 1\)). \(\tan x = x + \tfrac13x^3 + \tfrac2{15}x^5 + \dots\) is derived, from \(y' = 1 + y^2\).
- Substitute into a series to replace \(x\) by \(2x\) or \(x^2\); multiply series keeping every term up to the required degree.
- A series approximates a function near 0 and inside its range of validity; it finds limits of the form \(\tfrac00\).
:::

:::links
- watch: [Maclaurin's series expansion](https://www.examsolutions.net/tutorials/maclaurins-series-expansion/) · ExamSolutions · deriving series by successive differentiation
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · differentiation of hyperbolic and inverse functions in the Further Pure list
- read: [Taylor series](https://tutorial.math.lamar.edu/Classes/CalcII/TaylorSeries.aspx) · Paul's Online Notes · Maclaurin is the case about 0
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · Maclaurin series and hyperbolic calculus booklets with answers
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot a function and a partial sum of its series together
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Further integration: hyperbolic and inverse forms](#math.fm.integ) integrates hyperbolic functions and the three inverse standard forms, with trigonometric and hyperbolic substitutions.
