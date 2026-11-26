@chapter math.fm.integ
@title Further integration: hyperbolic and inverse forms
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary You will integrate the hyperbolic functions, recognise the three standard integrals that give \(\sin^{-1}\), \(\sinh^{-1}\) and \(\cosh^{-1}\), and handle harder cases by completing the square and by trigonometric and hyperbolic substitutions. You will also meet the 9709 techniques (parts, \(t = \tan\frac{x}{2}\)) applied to harder integrals, and give definite integrals in exact logarithmic form.
:::why
Integrals involving a square root of a quadratic turn up everywhere a circle, an ellipse or a hyperbola does: the area of a window, the volume of a cooling tower, the length of a cable. The old technique is to draw a right-angled triangle and use sine and cosine. The newer technique is hyperbolic: because \(\cosh^2 u - \sinh^2 u = 1\), a substitution \(x = a\sinh u\) removes the root from \(\sqrt{x^2 + a^2}\) in one line. Between them, the two substitutions cover every integral of this type that the exam sets.
:::

**Before you start**, you need integration by parts, substitution and partial fractions from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech), the standard integrals and areas from [Further integration](#math.p3.integ), the hyperbolic identities and inverse functions from [Hyperbolic functions](#math.fm.hyperbolic), and the derivatives of the inverse functions from [Further differentiation and Maclaurin series](#math.fm.diff).

:::try Warm-up
Q: Find \(\displaystyle\int\frac{2x}{x^2 + 3}\,dx\). (from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech))
A: The numerator is the derivative of the denominator, so the integral is \(\ln\left(x^2 + 3\right) + c\).
Q: Find \(\displaystyle\int\frac{1}{x^2 + 4}\,dx\). (from [Further integration](#math.p3.integ))
A: Use \(\displaystyle\int\frac{1}{x^2 + a^2}\,dx = \frac1a\tan^{-1}\frac xa\) with \(a = 2\): \(\tfrac12\tan^{-1}\tfrac x2 + c\).
Q: Show that \(\cosh^2x = \tfrac12(1 + \cosh 2x)\). (from [Hyperbolic functions](#math.fm.hyperbolic))
A: \(\cosh 2x = 2\cosh^2x - 1\), so \(2\cosh^2x = 1 + \cosh 2x\).
:::

## Integrating the hyperbolic functions

Each derivative from [Further differentiation and Maclaurin series](#math.fm.diff) can be read backwards. For example, \(\dfrac{d}{dx}\sinh x = \cosh x\), so \(\displaystyle\int\cosh x\,dx = \sinh x + c\).

:::key Integrals of the hyperbolic functions
\[\begin{aligned}
\int\sinh x\,dx &= \cosh x + c & \int\cosh x\,dx &= \sinh x + c \\
\int\operatorname{sech}^2x\,dx &= \tanh x + c & \int\operatorname{cosech}^2x\,dx &= -\coth x + c \\
\int\tanh x\,dx &= \ln\cosh x + c & \int\coth x\,dx &= \ln\lvert\sinh x\rvert + c
\end{aligned}\]
For a linear argument divide by the coefficient: \(\displaystyle\int\cosh kx\,dx = \dfrac1k\sinh kx + c\).
:::

MF19 gives \(\int\sinh x\), \(\int\cosh x\) and \(\int\operatorname{sech}^2x\). The \(\tanh\) result comes from writing \(\tanh x = \sinh x / \cosh x\) and noticing that the numerator is the derivative of the denominator (as in [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech)). No modulus is needed in \(\ln\cosh x\) because \(\cosh x > 0\).

:::eg Find (a) \(\displaystyle\int\left(3\cosh 2x - \sinh\tfrac x2\right)dx\), (b) \(\displaystyle\int_0^1\sinh 2x\,dx\), (c) \(\displaystyle\int_0^{\ln 3}\tanh x\,dx\).
(a) Divide by the coefficient of \(x\) in each argument:
\[\int\left(3\cosh 2x - \sinh\tfrac x2\right)dx = \tfrac32\sinh 2x - 2\cosh\tfrac x2 + c\]
(b) \[\int_0^1\sinh 2x\,dx = \left[\tfrac12\cosh 2x\right]_0^1 = \tfrac12(\cosh 2 - 1) = 1.38\ (3\ \text{s.f.})\]
(c) \(\displaystyle\int_0^{\ln 3}\tanh x\,dx = \left[\ln\cosh x\right]_0^{\ln 3}\). Now \(\cosh(\ln 3) = \dfrac{3 + \frac13}{2} = \dfrac53\), and \(\ln\cosh 0 = 0\), so the value is \(\ln\tfrac53\).
:::

### Powers of \(\sinh\) and \(\cosh\)

Squares need an identity, as for \(\sin^2x\) and \(\cos^2x\) in [Further integration](#math.p3.integ). The ones to use are \(\cosh^2x = \tfrac12(1 + \cosh 2x)\) and \(\sinh^2x = \tfrac12(\cosh 2x - 1)\). Notice the sign: \(\sinh^2\) has a minus.

:::eg Find the exact value of \(\displaystyle\int_0^{\ln 2}\cosh^2x\,dx\).
\[\begin{aligned}
\int_0^{\ln 2}\cosh^2x\,dx &= \tfrac12\int_0^{\ln 2}(1 + \cosh 2x)\,dx \\
&= \tfrac12\left[x + \tfrac12\sinh 2x\right]_0^{\ln 2}
\end{aligned}\]
Now \(\sinh(2\ln 2) = \dfrac{4 - \frac14}{2} = \dfrac{15}{8}\), so
\[\tfrac12\left(\ln 2 + \tfrac{15}{16}\right) = \tfrac12\ln 2 + \tfrac{15}{32}\]
**Check**: this is \(0.8153\), and \(\cosh^2x\) is between 1 and \(\cosh^2(\ln 2) = 1.5625\) on an interval of length \(\ln 2 = 0.693\), so the integral lies between 0.69 and 1.08.
:::

An odd power of \(\sinh x\) or \(\cosh x\) can be split, keeping one factor for the substitution. For \(\int\sinh^3x\,dx\) write \(\sinh^3x = \sinh x\left(\cosh^2x - 1\right)\) and let \(u = \cosh x\), so \(du = \sinh x\,dx\):
\[\int\sinh^3x\,dx = \int\left(u^2 - 1\right)du = \frac{\cosh^3x}{3} - \cosh x + c\]
The same idea works for any odd power: keep one factor of \(\sinh x\) (or \(\cosh x\)), turn the rest into the other function with \(\cosh^2x - \sinh^2x = 1\), and substitute. An even power needs the double-angle identities instead.

:::eg (Exam style) Use the substitution \(u = \cosh x\) to find the exact value of \(\displaystyle\int_0^{\ln 3}\sinh^3x\,dx\).
Split off one factor of \(\sinh x\), and write the other two in terms of \(\cosh x\):
\[\sinh^3x = \sinh x\left(\cosh^2x - 1\right)\] [M1]
With \(u = \cosh x\), \(du = \sinh x\,dx\), so the integrand becomes \(\left(u^2 - 1\right)du\): [A1]

Limits: \(x = 0\) gives \(u = \cosh 0 = 1\). \(x = \ln 3\) gives \(u = \cosh(\ln 3) = \dfrac{3 + \frac13}{2} = \dfrac53\). [B1]
\[\int_1^{5/3}\left(u^2 - 1\right)du = \left[\frac{u^3}{3} - u\right]_1^{5/3}\] [M1]
At the top, \(\dfrac{125}{81} - \dfrac53 = \dfrac{125 - 135}{81} = -\dfrac{10}{81}\). At the bottom, \(\dfrac13 - 1 = -\dfrac23 = -\dfrac{54}{81}\). So
\[\text{value} = -\frac{10}{81} + \frac{54}{81} = \frac{44}{81}\] [A1]
**Check**: \(\sinh^3x\) rises from 0 to \(\sinh^3(\ln 3) = \left(\tfrac43\right)^3 = 2.37\) over an interval of length 1.10, and it is small until \(x\) is large. \(\tfrac{44}{81} = 0.543\) is a believable fraction of the box \(1.10 \times 2.37\).
:::

:::eg Find \(\displaystyle\int_0^1 x\cosh x\,dx\), giving your answer in terms of \(e\).
Use integration by parts with \(u = x\), \(\dfrac{dv}{dx} = \cosh x\), so \(v = \sinh x\):
\[\int x\cosh x\,dx = x\sinh x - \int\sinh x\,dx = x\sinh x - \cosh x\]
\[\int_0^1 x\cosh x\,dx = (\sinh 1 - \cosh 1) - (0 - 1) = 1 - e^{-1}\]
because \(\sinh 1 - \cosh 1 = -e^{-1}\). That is \(0.632\).
:::

:::eg The cable \(y = 25\cosh\frac{x}{25} - 19\) hangs between poles at \(x = \pm 15\) (distances in metres). Find the area between the cable and the ground.
The area is \(\displaystyle\int_{-15}^{15}\left(25\cosh\frac{x}{25} - 19\right)dx\). The antiderivative of \(25\cosh\frac{x}{25}\) is \(625\sinh\frac{x}{25}\):
\[\left[625\sinh\frac{x}{25} - 19x\right]_{-15}^{15} = 2\left(625\sinh 0.6 - 285\right)\]
\[= 1250\sinh 0.6 - 570 = 225.8\ \text{m}^2\ (4\ \text{s.f.})\]
Both parts of the bracket are odd functions of \(x\), so doubling the value at \(x = 15\) gives the whole area. Dividing by the 30 m between the poles gives the mean height of the cable above the ground, \(225.8 \div 30 = 7.53\) m.
:::

## The three standard inverse forms

The derivatives of \(\sin^{-1}\), \(\sinh^{-1}\) and \(\cosh^{-1}\) give three integrals that you must be able to recognise. The letter \(a\) is a positive constant.

:::key Standard integrals with square roots (in MF19)
\[\begin{aligned}
\int\frac{1}{\sqrt{a^2 - x^2}}\,dx &= \sin^{-1}\frac xa + c & \lvert x \rvert < a \\
\int\frac{1}{\sqrt{x^2 + a^2}}\,dx &= \sinh^{-1}\frac xa + c & \text{all } x \\
\int\frac{1}{\sqrt{x^2 - a^2}}\,dx &= \cosh^{-1}\frac xa + c & x > a
\end{aligned}\]
The last two can be written with logarithms: \(\sinh^{-1}\dfrac xa = \ln\dfrac{x + \sqrt{x^2 + a^2}}{a}\) and \(\cosh^{-1}\dfrac xa = \ln\dfrac{x + \sqrt{x^2 - a^2}}{a}\). The constant \(-\ln a\) can be absorbed in \(c\), so \(\ln\left(x + \sqrt{x^2 \pm a^2}\right) + c\) is also correct.
:::

:::def Standard form
An integrand that matches the derivative of a known function exactly, so that the integral can be written down without working. A great many harder integrals are reduced to a standard form by an algebraic step (taking out a factor, completing the square) or by a substitution.
:::

To prove one of them you may differentiate the answer, or substitute.

:::eg (Exam style) Show by differentiation that \(\displaystyle\int\frac{1}{\sqrt{a^2 - x^2}}\,dx = \sin^{-1}\frac xa + c\), where \(a > 0\) and \(\lvert x \rvert < a\).
The derivative of \(\sin^{-1}u\) is \(\dfrac{1}{\sqrt{1 - u^2}}\). With \(u = \dfrac xa\) the chain rule gives
\[\frac{d}{dx}\sin^{-1}\frac xa = \frac{1}{\sqrt{1 - \frac{x^2}{a^2}}}\times\frac1a\] [M1 A1]
\[= \frac{1}{\sqrt{a^2 - x^2}}\] [A1]
Multiply \(a\) into the root: \(a\sqrt{1 - \frac{x^2}{a^2}} = \sqrt{a^2 - x^2}\). The derivative equals the integrand, so the result holds.
:::

Differentiating \(\sinh^{-1}\dfrac xa\) in the same way gives \(\dfrac{1}{\sqrt{\left(\frac xa\right)^2 + 1}}\times\dfrac1a = \dfrac{1}{\sqrt{x^2 + a^2}}\), which is the integrand.

:::eg (Exam style) Use the substitution \(x = a\sinh u\) to show that \(\displaystyle\int\frac{1}{\sqrt{x^2 + a^2}}\,dx = \sinh^{-1}\frac xa + c\).
\(x = a\sinh u\) gives \(\dfrac{dx}{du} = a\cosh u\). [B1]

The root becomes
\[\sqrt{x^2 + a^2} = \sqrt{a^2\sinh^2u + a^2} = a\sqrt{\cosh^2u} = a\cosh u\] [M1]
since \(\cosh u > 0\). Then
\[\int\frac{a\cosh u}{a\cosh u}\,du = \int 1\,du = u + c\] [A1]
and \(u = \sinh^{-1}\dfrac xa\), so the result is \(\sinh^{-1}\dfrac xa + c\). [A1]
:::

:::eg Find (a) \(\displaystyle\int\frac{1}{\sqrt{9 - 4x^2}}\,dx\), (b) \(\displaystyle\int_0^2\frac{1}{\sqrt{x^2 + 9}}\,dx\), (c) \(\displaystyle\int_3^5\frac{1}{\sqrt{x^2 - 4}}\,dx\).
(a) The coefficient of \(x^2\) must be 1 inside the root, so take out the 4:
\[\sqrt{9 - 4x^2} = 2\sqrt{\tfrac94 - x^2}\]
\[\int\frac{dx}{2\sqrt{\left(\frac32\right)^2 - x^2}} = \tfrac12\sin^{-1}\frac{2x}{3} + c\]
(b) The form \(\sqrt{x^2 + a^2}\) with \(a = 3\):
\[\int_0^2\frac{dx}{\sqrt{x^2 + 9}} = \left[\sinh^{-1}\frac x3\right]_0^2 = \sinh^{-1}\tfrac23 = \ln\frac{2 + \sqrt{13}}{3}\]
That is \(0.625\) to 3 s.f. (using \(\sinh^{-1}0 = 0\)).

(c) The form \(\sqrt{x^2 - a^2}\) with \(a = 2\), valid because \(x \ge 3 > 2\):
\[\left[\cosh^{-1}\frac x2\right]_3^5 = \cosh^{-1}\tfrac52 - \cosh^{-1}\tfrac32\]
Each is a logarithm: \(\cosh^{-1}\tfrac52 = \ln\left(\tfrac52 + \tfrac{\sqrt{21}}{2}\right)\) and \(\cosh^{-1}\tfrac32 = \ln\left(\tfrac32 + \tfrac{\sqrt5}{2}\right)\), so
\[\text{value} = \ln\frac{5 + \sqrt{21}}{3 + \sqrt5} = 0.604\ (3\ \text{s.f.})\]
:::

:::warn Which form is it?
Look at the signs under the root. \(a^2 - x^2\) gives \(\sin^{-1}\) (a circle-like integrand, defined only for \(\lvert x \rvert < a\)). \(x^2 + a^2\) gives \(\sinh^{-1}\) (defined for all \(x\)). \(x^2 - a^2\) gives \(\cosh^{-1}\) (defined only for \(x > a\)). Using \(\sin^{-1}\) for a plus sign is the commonest error, and it loses the method mark as well.
:::

:::plot The curves y = 1/√(x² + 9) and y = 1/√(9 − x²) for 0 ≤ x ≤ 2.9. The shaded area under the first curve is ∫₀² 1/√(x² + 9) dx = sinh⁻¹(2/3) = 0.625. The second curve has a vertical asymptote at x = 3, which is why the sin⁻¹ form needs |x| < a.
--f "1/sqrt(x**2+9)" --f "1/sqrt(9-x**2)" --label "y = 1/√(x² + 9)" --label "y = 1/√(9 − x²)" --x 0 2.9 --y 0 1.5 --shade "0,0,2" --legend tl
:::

Two related forms have no root. From 9709, \(\int\dfrac{1}{x^2 + a^2}\,dx = \dfrac1a\tan^{-1}\dfrac xa\), and the log forms \(\int\dfrac{1}{a^2 - x^2}\,dx = \dfrac{1}{2a}\ln\left\lvert\dfrac{a + x}{a - x}\right\rvert\) and \(\int\dfrac{1}{x^2 - a^2}\,dx = \dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert\) are all on MF19 (found by partial fractions). For \(\lvert x \rvert < a\), the first of the log forms equals \(\dfrac1a\tanh^{-1}\dfrac xa\), because \(\tanh^{-1}u = \tfrac12\ln\dfrac{1 + u}{1 - u}\).

:::eg Evaluate \(\displaystyle\int_0^{1/2}\frac{1}{1 - x^2}\,dx\) in two ways.
By partial fractions, \(\dfrac{1}{1 - x^2} = \dfrac12\left(\dfrac{1}{1 - x} + \dfrac{1}{1 + x}\right)\), so
\[\int_0^{1/2} = \tfrac12\left[-\ln(1 - x) + \ln(1 + x)\right]_0^{1/2} = \tfrac12\ln\frac{3/2}{1/2} = \tfrac12\ln 3\]
By inverse function: \(\dfrac{d}{dx}\tanh^{-1}x = \dfrac{1}{1 - x^2}\), so the integral is \(\tanh^{-1}\tfrac12 = \tfrac12\ln 3\), the same.
:::

## Completing the square

An integrand with a quadratic under the root often fits one of the standard forms after you complete the square. Write the quadratic as \(\pm(x + p)^2 \pm q\), then replace \(x + p\) by a single letter in your head: the integral is \(\sin^{-1}\), \(\sinh^{-1}\) or \(\cosh^{-1}\) of \(\dfrac{x + p}{\sqrt q}\).

:::steps
1. Make the coefficient of \(x^2\) equal to \(1\) (or \(-1\)) by taking a factor out of the root.
2. Complete the square: \(x^2 + bx + c = \left(x + \tfrac b2\right)^2 + \left(c - \tfrac{b^2}{4}\right)\).
3. Match with \(a^2 - u^2\), \(u^2 + a^2\) or \(u^2 - a^2\), where \(u = x + \tfrac b2\).
4. Integrate. Since \(\dfrac{du}{dx} = 1\), a shift adds no extra factor.
:::

:::eg Find \(\displaystyle\int\frac{1}{\sqrt{x^2 + 2x}}\,dx\) for \(x > 0\).
Complete the square: \(x^2 + 2x = (x + 1)^2 - 1\). So with \(u = x + 1\) and \(a = 1\) the integrand is \(\dfrac{1}{\sqrt{u^2 - 1}}\):
\[\int\frac{dx}{\sqrt{(x + 1)^2 - 1}} = \cosh^{-1}(x + 1) + c\]
Equivalently \(\ln\left(x + 1 + \sqrt{x^2 + 2x}\right) + c\), since \(\sqrt{(x + 1)^2 - 1} = \sqrt{x^2 + 2x}\).
:::

:::eg (a) Find \(\displaystyle\int_{-2}^{1}\frac{1}{\sqrt{5 - 4x - x^2}}\,dx\). (b) Find \(\displaystyle\int_1^3\frac{1}{\sqrt{x^2 - 2x + 5}}\,dx\), in exact form.
(a) \(5 - 4x - x^2 = 9 - (x + 2)^2\) (check: \(9 - x^2 - 4x - 4 = 5 - 4x - x^2\)).
\[\int_{-2}^{1}\frac{dx}{\sqrt{9 - (x + 2)^2}} = \left[\sin^{-1}\frac{x + 2}{3}\right]_{-2}^{1} = \sin^{-1}1 - \sin^{-1}0 = \frac\pi2\]
(b) \(x^2 - 2x + 5 = (x - 1)^2 + 4\):
\[\int_1^3\frac{dx}{\sqrt{(x - 1)^2 + 2^2}} = \left[\sinh^{-1}\frac{x - 1}{2}\right]_1^3 = \sinh^{-1}1 - 0 = \ln\left(1 + \sqrt2\right)\]
:::

:::eg Find the exact value of \(\displaystyle\int_0^1\frac{1}{\sqrt{x^2 + 2x + 2}}\,dx\).
\(x^2 + 2x + 2 = (x + 1)^2 + 1\), so the integral is of the form \(\dfrac{1}{\sqrt{u^2 + 1}}\) with \(u = x + 1\):
\[\left[\sinh^{-1}(x + 1)\right]_0^1 = \sinh^{-1}2 - \sinh^{-1}1\]
Write each as a logarithm: \(\sinh^{-1}2 = \ln\left(2 + \sqrt5\right)\) and \(\sinh^{-1}1 = \ln\left(1 + \sqrt2\right)\). So
\[\text{value} = \ln\frac{2 + \sqrt5}{1 + \sqrt2} = 0.562\ (3\ \text{s.f.})\]
:::

If the numerator is linear, split it into a multiple of the derivative of the quadratic and a constant. The first part integrates to a root; the second is a standard form.

:::eg (Exam style) Find \(\displaystyle\int\frac{x + 3}{\sqrt{x^2 + 2x + 5}}\,dx\).
The derivative of \(x^2 + 2x + 5\) is \(2x + 2\). Write
\[x + 3 = \tfrac12(2x + 2) + 2\] [M1]
\[\int\frac{x + 3}{\sqrt{x^2 + 2x + 5}}\,dx = \tfrac12\int\frac{2x + 2}{\sqrt{x^2 + 2x + 5}}\,dx + 2\int\frac{dx}{\sqrt{x^2 + 2x + 5}}\]
For the first integral let \(w = x^2 + 2x + 5\); it gives \(\tfrac12 \times 2\sqrt w = \sqrt{x^2 + 2x + 5}\). [A1]

For the second, \(x^2 + 2x + 5 = (x + 1)^2 + 4\) [M1]:
\[2\sinh^{-1}\frac{x + 1}{2}\] [A1]
\[\text{Total: } \sqrt{x^2 + 2x + 5} + 2\sinh^{-1}\frac{x + 1}{2} + c\] [A1]
**Check** by differentiating: the second term gives \(\dfrac{2}{\sqrt{x^2 + 2x + 5}}\), the first gives \(\dfrac{x + 1}{\sqrt{x^2 + 2x + 5}}\), and together \(\dfrac{x + 3}{\sqrt{x^2 + 2x + 5}}\).
:::

## Integrals containing a square root: substitution

Sometimes the root is in the numerator, as in \(\int\sqrt{a^2 - x^2}\,dx\) (the area under a circle), or inside a bigger expression. A substitution chosen to remove the root works every time.

:::key Substitutions to remove a root
| Expression | Substitution | The root becomes |
|---|---|---|
| \(\sqrt{a^2 - x^2}\) | \(x = a\sin\theta\) | \(a\cos\theta\) |
| \(\sqrt{x^2 + a^2}\) | \(x = a\sinh u\) | \(a\cosh u\) |
| \(\sqrt{x^2 - a^2}\) | \(x = a\cosh u\) | \(a\sinh u\) |
Always find \(dx\) (for example \(dx = a\cosh u\,du\)) and change the limits at the same time.
:::

:::def Hyperbolic substitution
A substitution \(x = a\sinh u\) or \(x = a\cosh u\), chosen so that \(\cosh^2u - \sinh^2u = 1\) removes a square root of the form \(\sqrt{x^2 \pm a^2}\). It plays the part for \(x^2 \pm a^2\) that \(x = a\sin\theta\) plays for \(a^2 - x^2\).
:::

:::eg (Exam style) Use the substitution \(x = 3\sin\theta\) to show that \(\displaystyle\int_0^3\sqrt{9 - x^2}\,dx = \dfrac{9\pi}{4}\).
\(x = 3\sin\theta\) gives \(dx = 3\cos\theta\,d\theta\), and \(\sqrt{9 - x^2} = \sqrt{9\cos^2\theta} = 3\cos\theta\) for \(0 \le \theta \le \tfrac\pi2\). [M1 A1]

Limits: \(x = 0\) gives \(\theta = 0\) and \(x = 3\) gives \(\theta = \tfrac\pi2\). [B1]
\[\int_0^{\pi/2}9\cos^2\theta\,d\theta = \tfrac92\int_0^{\pi/2}(1 + \cos 2\theta)\,d\theta\] [M1]
\[= \tfrac92\left[\theta + \tfrac12\sin 2\theta\right]_0^{\pi/2} = \tfrac92 \times \tfrac\pi2 = \frac{9\pi}{4}\] [A1]
This is a quarter of the area of a circle of radius 3, which is a useful check.
:::

:::eg Use the substitution \(x = 2\sinh u\) to find the exact value of \(\displaystyle\int_0^1\sqrt{x^2 + 4}\,dx\).
\(x = 2\sinh u\), so \(dx = 2\cosh u\,du\), and \(\sqrt{x^2 + 4} = \sqrt{4\sinh^2u + 4} = 2\cosh u\).

Limits: \(x = 0\) gives \(u = 0\). \(x = 1\) gives \(\sinh u = \tfrac12\), so \(u = \sinh^{-1}\tfrac12 = \ln\dfrac{1 + \sqrt5}{2}\).

\[\begin{aligned}
\int_0^1\sqrt{x^2 + 4}\,dx &= \int_0^{u_1}2\cosh u \times 2\cosh u\,du \\
&= 4\int_0^{u_1}\cosh^2u\,du \\
&= 2\int_0^{u_1}(1 + \cosh 2u)\,du \\
&= \left[2u + \sinh 2u\right]_0^{u_1}
\end{aligned}\]
Use \(\sinh 2u = 2\sinh u\cosh u\). At the upper limit \(\sinh u = \tfrac12\) and \(\cosh u = \sqrt{1 + \tfrac14} = \tfrac{\sqrt5}{2}\), so \(\sinh 2u_1 = 2 \times \tfrac12 \times \tfrac{\sqrt5}{2} = \tfrac{\sqrt5}{2}\):
\[\text{value} = 2\sinh^{-1}\tfrac12 + \tfrac{\sqrt5}{2} = 2\ln\frac{1 + \sqrt5}{2} + \frac{\sqrt5}{2} = 2.08\ (3\ \text{s.f.})\]
**Check**: \(\sqrt{x^2 + 4}\) goes from 2 to \(\sqrt5 = 2.24\) over a unit interval, so the area should be a little over 2.
:::

The third row of the table, \(x = a\cosh u\), works the same way, but now the root is \(\sqrt{x^2 - a^2} = a\sinh u\) and the limits need \(\cosh^{-1}\).

:::eg (Exam style) Use the substitution \(x = 2\cosh u\) to find the exact value of \(\displaystyle\int_2^4\sqrt{x^2 - 4}\,dx\).
\(x = 2\cosh u\) gives \(\dfrac{dx}{du} = 2\sinh u\), and
\[\sqrt{x^2 - 4} = \sqrt{4\cosh^2u - 4} = 2\sqrt{\sinh^2u} = 2\sinh u\] [B1]
since \(\sinh u \ge 0\) for \(u \ge 0\). The integrand becomes
\[2\sinh u \times 2\sinh u = 4\sinh^2u = 2\left(\cosh 2u - 1\right)\] [M1 A1]
Limits: \(x = 2\) gives \(\cosh u = 1\), so \(u = 0\). \(x = 4\) gives \(\cosh u = 2\), so \(u = \cosh^{-1}2 = \ln\left(2 + \sqrt3\right)\). [B1]
\[\int_0^{u_1}2\left(\cosh 2u - 1\right)du = \left[\sinh 2u - 2u\right]_0^{u_1}\]
At the top \(\cosh u = 2\) and \(\sinh u = \sqrt{4 - 1} = \sqrt3\), so \(\sinh 2u_1 = 2\sinh u_1\cosh u_1 = 2 \times \sqrt3 \times 2 = 4\sqrt3\). [M1]
\[\text{value} = 4\sqrt3 - 2\ln\left(2 + \sqrt3\right) = 4.29\ (3\ \text{s.f.})\] [A1]
**Check** with the general result for \(\sqrt{x^2 - a^2}\) given just below: \(\tfrac12\left[x\sqrt{x^2 - 4} - 4\cosh^{-1}\tfrac x2\right]_2^4 = \tfrac12\left(4\sqrt{12} - 4\ln\left(2 + \sqrt3\right)\right) = 4\sqrt3 - 2\ln\left(2 + \sqrt3\right)\), the same.
:::

The same working for the other two cases gives general results. They are not in MF19, so you derive them when a question asks (or learn them for speed).

:::key Integrals of the square roots
\[\begin{aligned}
\int\sqrt{a^2 - x^2}\,dx &= \tfrac12\left[x\sqrt{a^2 - x^2} + a^2\sin^{-1}\tfrac xa\right] + c \\
\int\sqrt{x^2 + a^2}\,dx &= \tfrac12\left[x\sqrt{x^2 + a^2} + a^2\sinh^{-1}\tfrac xa\right] + c \\
\int\sqrt{x^2 - a^2}\,dx &= \tfrac12\left[x\sqrt{x^2 - a^2} - a^2\cosh^{-1}\tfrac xa\right] + c
\end{aligned}\]
:::

Each can be verified by differentiating. For the first, the derivative of \(x\sqrt{a^2 - x^2}\) is \(\sqrt{a^2 - x^2} - \dfrac{x^2}{\sqrt{a^2 - x^2}}\) and that of \(a^2\sin^{-1}\dfrac xa\) is \(\dfrac{a^2}{\sqrt{a^2 - x^2}}\). Add them: \(\sqrt{a^2 - x^2} + \dfrac{a^2 - x^2}{\sqrt{a^2 - x^2}} = 2\sqrt{a^2 - x^2}\), and the factor \(\tfrac12\) leaves the integrand.

:::eg A circular window has radius 1.5 m. A horizontal bar crosses it 0.9 m above the centre. Find the area of the part of the window above the bar.
Put the origin at the centre. At height \(y\) the circle \(x^2 + y^2 = 2.25\) has half-width \(\sqrt{2.25 - y^2}\), so the strip at that height has width \(2\sqrt{2.25 - y^2}\). The part above the bar runs from \(y = 0.9\) to \(y = 1.5\):
\[A = \int_{0.9}^{1.5}2\sqrt{2.25 - y^2}\,dy = \left[y\sqrt{2.25 - y^2} + 2.25\sin^{-1}\frac{y}{1.5}\right]_{0.9}^{1.5}\]
At \(y = 1.5\): \(0 + 2.25 \times \dfrac\pi2 = 3.534\). At \(y = 0.9\): \(0.9 \times 1.2 + 2.25\sin^{-1}0.6 = 1.08 + 1.448 = 2.528\).
\[A = 3.534 - 2.528 = 1.01\ \text{m}^2\ (3\ \text{s.f.})\]
**Check**: the whole window has area \(\pi \times 1.5^2 = 7.07\) m\(^2\), and this cap is a small piece near the top, so about 1 m\(^2\) is believable.
:::

:::eg A cooling tower is modelled so that its vertical cross-section is bounded on the right by the curve \(x = \sqrt{100 + 4y^2}\), where \(x\) and \(y\) are in metres and \(y\) is the height above the narrowest point. Find the area of the cross-section between \(y = 0\) and \(y = 15\) (both sides of the axis \(x = 0\)).
The cross-section is symmetric, so the area is \(\displaystyle\int_0^{15}2\sqrt{100 + 4y^2}\,dy = 4\int_0^{15}\sqrt{25 + y^2}\,dy\).

Use the result for \(\sqrt{y^2 + a^2}\) with \(a = 5\):
\[4 \times \tfrac12\left[y\sqrt{y^2 + 25} + 25\sinh^{-1}\frac y5\right]_0^{15} = 2\left(15\sqrt{250} + 25\sinh^{-1}3\right)\]
With \(\sqrt{250} = 15.81\) and \(\sinh^{-1}3 = \ln\left(3 + \sqrt{10}\right) = 1.818\):
\[\text{area} = 2(237.2 + 45.46) = 565\ \text{m}^2\ (3\ \text{s.f.})\]
**Check**: the width is 20 m at \(y = 0\) and \(2\sqrt{1000} = 63.2\) m at \(y = 15\); the average width of about 38 m over a height of 15 m gives roughly 570 m\(^2\).
:::

:::eg The curve \(y = \cosh x\) between \(x = 0\) and \(x = 1\) is rotated through \(2\pi\) about the \(x\)-axis to make a vase. Find the exact volume (in cubic units).
\[V = \pi\int_0^1\cosh^2x\,dx = \frac\pi2\int_0^1(1 + \cosh 2x)\,dx = \frac\pi2\left[x + \tfrac12\sinh 2x\right]_0^1\]
\[V = \frac\pi2\left(1 + \tfrac12\sinh 2\right) = \frac\pi2 + \frac{\pi}{4}\sinh 2 = 4.42\ (3\ \text{s.f.})\]
**Check**: the radius runs from 1 to \(\cosh 1 = 1.54\), so the volume lies between \(\pi \times 1^2 \times 1 = 3.14\) and \(\pi \times 1.54^2 \times 1 = 7.5\).
:::

:::eg (Exam style) (a) Show that \(\dfrac{d}{dx}\left(x\sqrt{x^2 + 1}\right) = 2\sqrt{x^2 + 1} - \dfrac{1}{\sqrt{x^2 + 1}}\). (b) Hence find \(\displaystyle\int\sqrt{x^2 + 1}\,dx\).
(a) Product rule with \(u = x\) and \(v = \sqrt{x^2 + 1}\), \(v' = \dfrac{x}{\sqrt{x^2 + 1}}\):
\[\frac{d}{dx}\left(x\sqrt{x^2 + 1}\right) = \sqrt{x^2 + 1} + \frac{x^2}{\sqrt{x^2 + 1}}\] [M1 A1]
Write \(x^2 = \left(x^2 + 1\right) - 1\):
\[= \sqrt{x^2 + 1} + \frac{x^2 + 1}{\sqrt{x^2 + 1}} - \frac{1}{\sqrt{x^2 + 1}} = 2\sqrt{x^2 + 1} - \frac{1}{\sqrt{x^2 + 1}}\] [A1]
(b) Integrate the result of (a):
\[x\sqrt{x^2 + 1} = 2\int\sqrt{x^2 + 1}\,dx - \int\frac{dx}{\sqrt{x^2 + 1}}\] [M1]
\[\int\sqrt{x^2 + 1}\,dx = \tfrac12\left[x\sqrt{x^2 + 1} + \sinh^{-1}x\right] + c\] [A1]
This is the \(a = 1\) case of the general result, found with no substitution at all.
:::

:::eg Use the substitution \(x = \sin\theta\) to find the exact value of \(\displaystyle\int_0^{1/2}\frac{x^2}{\sqrt{1 - x^2}}\,dx\).
\(dx = \cos\theta\,d\theta\) and \(\sqrt{1 - x^2} = \cos\theta\), so the integrand becomes \(\sin^2\theta\,d\theta\). The limits are \(\theta = 0\) and \(\theta = \sin^{-1}\tfrac12 = \tfrac\pi6\).
\[\int_0^{\pi/6}\sin^2\theta\,d\theta = \tfrac12\int_0^{\pi/6}(1 - \cos 2\theta)\,d\theta = \tfrac12\left[\theta - \tfrac12\sin 2\theta\right]_0^{\pi/6}\]
\[= \tfrac12\left(\frac\pi6 - \tfrac12 \times \frac{\sqrt3}{2}\right) = \frac{\pi}{12} - \frac{\sqrt3}{8}\]
which is \(0.0453\). This is the circular twin of the previous example: \(\sin^2\theta\) (with a minus in \(1 - \cos 2\theta\)) against \(\sinh^2u\) (with a minus in \(\cosh 2u - 1\)).
:::

:::eg Use \(x = \sinh u\) to find \(\displaystyle\int_0^1\frac{x^2}{\sqrt{x^2 + 1}}\,dx\), in exact form.
\(dx = \cosh u\,du\) and \(\sqrt{x^2 + 1} = \cosh u\), so the integrand becomes \(\sinh^2u\,du\). The limits are \(u = 0\) and \(u = \sinh^{-1}1 = \ln\left(1 + \sqrt2\right)\).
\[\int\sinh^2u\,du = \tfrac12\int(\cosh 2u - 1)\,du = \tfrac14\sinh 2u - \tfrac12u = \tfrac12\sinh u\cosh u - \tfrac12u\]
At the upper limit \(\sinh u = 1\) and \(\cosh u = \sqrt2\):
\[\text{value} = \tfrac12\sqrt2 - \tfrac12\ln\left(1 + \sqrt2\right) = 0.266\ (3\ \text{s.f.})\]
:::

:::warn Substitution slips
Three things go wrong. Forgetting \(dx = a\cosh u\,du\) leaves an integral in \(u\) with the wrong power. Keeping the old limits: when you change variable from \(x\) to \(u\) the limits change too (or you go back to \(x\) before substituting). And mixing the circular and hyperbolic versions: \(\sinh^2u\) integrates to \(\tfrac14\sinh 2u - \tfrac12u\), with the minus on the \(u\) term; \(\sin^2\theta\) integrates to \(\tfrac12\theta - \tfrac14\sin 2\theta\), with the minus on the trigonometric term.
:::

## Harder integrals: 9709 techniques again

Any integration question in 9231 can need the methods of [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech) in a harder form. Three appear again and again; the first two are 9709 methods, and the third, \(t = \tan\frac x2\), is new in this chapter.

**Parts twice.** When the integrand is \(e^{ax}\) times \(\sin bx\) or \(\cos bx\), integrate by parts twice. The original integral reappears, and you solve for it.

:::eg Find \(\displaystyle\int e^x\sin x\,dx\), and evaluate \(\displaystyle\int_0^\pi e^x\sin x\,dx\).
Let \(I = \int e^x\sin x\,dx\). With \(u = \sin x\) and \(\dfrac{dv}{dx} = e^x\):
\[I = e^x\sin x - \int e^x\cos x\,dx\]
Parts again, with \(u = \cos x\):
\[\int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I\]
So \(I = e^x\sin x - e^x\cos x - I\), giving
\[I = \tfrac12e^x(\sin x - \cos x) + c\]
\[\int_0^\pi e^x\sin x\,dx = \tfrac12e^\pi(0 + 1) - \tfrac12(0 - 1) = \tfrac12\left(e^\pi + 1\right) = 12.1\]
:::

**Parts with an inverse function.** An inverse function on its own can be integrated by parts by writing it as \(1 \times f^{-1}(x)\).

:::eg Show that \(\displaystyle\int_0^1\sinh^{-1}x\,dx = \ln\left(1 + \sqrt2\right) + 1 - \sqrt2\).
Take \(u = \sinh^{-1}x\) and \(\dfrac{dv}{dx} = 1\). Then \(\dfrac{du}{dx} = \dfrac{1}{\sqrt{x^2 + 1}}\) and \(v = x\):
\[\int\sinh^{-1}x\,dx = x\sinh^{-1}x - \int\frac{x}{\sqrt{x^2 + 1}}\,dx\]
For the last integral let \(w = x^2 + 1\), \(dw = 2x\,dx\): \(\displaystyle\int\frac{x}{\sqrt{x^2 + 1}}\,dx = \sqrt{x^2 + 1}\).
\[\int_0^1\sinh^{-1}x\,dx = \left[x\sinh^{-1}x - \sqrt{x^2 + 1}\right]_0^1 = \left(\sinh^{-1}1 - \sqrt2\right) - (0 - 1)\]
Since \(\sinh^{-1}1 = \ln\left(1 + \sqrt2\right)\), this is \(\ln\left(1 + \sqrt2\right) + 1 - \sqrt2 = 0.467\).
:::

**The substitution \(t = \tan\frac x2\)** (this one is new here: it was not in the 9709 chapters). It converts \(\sin x\) and \(\cos x\) to rational functions of \(t\). MF19 gives \(\sin x = \dfrac{2t}{1 + t^2}\) and \(\cos x = \dfrac{1 - t^2}{1 + t^2}\). To see where they come from, use the double-angle formulae with the angle \(\tfrac x2\): \(\sin x = 2\sin\tfrac x2\cos\tfrac x2 = 2t\cos^2\tfrac x2\) and \(\cos x = \cos^2\tfrac x2 - \sin^2\tfrac x2 = (1 - t^2)\cos^2\tfrac x2\), and \(\cos^2\tfrac x2 = \dfrac{1}{1 + \tan^2\frac x2} = \dfrac{1}{1 + t^2}\). You must also write \(dx\): differentiating \(t = \tan\frac x2\) gives \(\dfrac{dt}{dx} = \tfrac12\sec^2\tfrac x2 = \tfrac12\left(1 + \tan^2\tfrac x2\right) = \tfrac12\left(1 + t^2\right)\), so \(dx = \dfrac{2\,dt}{1 + t^2}\).

:::eg (Exam style) Use the substitution \(t = \tan\frac x2\) to show that \(\displaystyle\int_0^{\pi/2}\frac{1}{2 + \cos x}\,dx = \frac{\pi}{3\sqrt3}\).
\(\cos x = \dfrac{1 - t^2}{1 + t^2}\) and \(dx = \dfrac{2\,dt}{1 + t^2}\). Then
\[2 + \cos x = \frac{2\left(1 + t^2\right) + 1 - t^2}{1 + t^2} = \frac{3 + t^2}{1 + t^2}\] [M1 A1]
\[\int\frac{1}{2 + \cos x}\,dx = \int\frac{1 + t^2}{3 + t^2}\times\frac{2}{1 + t^2}\,dt = \int\frac{2}{3 + t^2}\,dt\] [M1 A1]
Limits: \(x = 0\) gives \(t = 0\); \(x = \tfrac\pi2\) gives \(t = \tan\tfrac\pi4 = 1\). [B1]
\[\int_0^1\frac{2}{3 + t^2}\,dt = \left[\frac{2}{\sqrt3}\tan^{-1}\frac{t}{\sqrt3}\right]_0^1 = \frac{2}{\sqrt3}\times\frac\pi6 = \frac{\pi}{3\sqrt3}\] [A1]
:::

Sometimes a question hands you the substitution. Then the work is to follow it faithfully and spot which standard form appears.

:::eg (Exam style) Use the substitution \(u = e^x\) to find the exact value of \(\displaystyle\int_0^{\ln 3}\frac{e^x}{\sqrt{e^{2x} + 16}}\,dx\).
\(u = e^x\), so \(du = e^x\,dx\), and \(e^{2x} = u^2\). [M1]

Limits: \(x = 0\) gives \(u = 1\) and \(x = \ln 3\) gives \(u = 3\). [B1]
\[\int_1^3\frac{du}{\sqrt{u^2 + 16}}\] [A1]
This is the \(\sinh^{-1}\) form with \(a = 4\):
\[\left[\sinh^{-1}\frac u4\right]_1^3 = \sinh^{-1}\tfrac34 - \sinh^{-1}\tfrac14\] [M1]
Now \(\sinh^{-1}\tfrac34 = \ln 2\) and \(\sinh^{-1}\tfrac14 = \ln\left(\tfrac14 + \tfrac{\sqrt{17}}{4}\right) = \ln\dfrac{1 + \sqrt{17}}{4}\), so
\[\text{value} = \ln 2 - \ln\frac{1 + \sqrt{17}}{4} = \ln\frac{8}{1 + \sqrt{17}}\] [A1]
which is \(0.446\) to 3 s.f.
:::

:::eg For each integral, say which method you would use and the first line of working. (Do not evaluate.)
(a) \(\displaystyle\int\frac{1}{\sqrt{12 + 4x - x^2}}\,dx\): complete the square, \(12 + 4x - x^2 = 16 - (x - 2)^2\), then \(\sin^{-1}\dfrac{x - 2}{4}\).

(b) \(\displaystyle\int\frac{2x - 1}{\sqrt{x^2 + 4}}\,dx\): split into \(\dfrac{2x}{\sqrt{x^2 + 4}}\), which is \(2\sqrt{x^2 + 4}\), and \(\dfrac{-1}{\sqrt{x^2 + 4}}\), which is \(-\sinh^{-1}\dfrac x2\).

(c) \(\displaystyle\int\sqrt{x^2 - 16}\,dx\): substitute \(x = 4\cosh u\) (the root becomes \(4\sinh u\)).

(d) \(\displaystyle\int\frac{1}{3 + 2\cos x}\,dx\): \(t = \tan\frac x2\), since there is only \(\cos x\) in a denominator.

(e) \(\displaystyle\int\cosh^2 3x\,dx\): use \(\cosh^2 3x = \tfrac12(1 + \cosh 6x)\).
:::

:::key Choosing the method
| Integrand | Method |
|---|---|
| \(\dfrac{1}{\sqrt{a^2 - x^2}}\), \(\dfrac{1}{\sqrt{x^2 \pm a^2}}\) | standard form (with a factor taken out) |
| \(\dfrac{1}{\sqrt{\text{quadratic}}}\) | complete the square, then standard form |
| \(\dfrac{\text{linear}}{\sqrt{\text{quadratic}}}\) | split the numerator, then one of the above |
| \(\sqrt{a^2 - x^2}\), \(\sqrt{x^2 \pm a^2}\) | \(x = a\sin\theta\), \(a\sinh u\) or \(a\cosh u\) |
| \(\sinh^2x\), \(\cosh^2x\) | double-angle identity |
| \(e^{ax}\) times \(\sin\) or \(\cos\) | parts twice |
| \(\dfrac{1}{a + b\cos x}\) or \(\dfrac{1}{a + b\sin x}\) | \(t = \tan\frac x2\) |
| an inverse function alone | parts with \(\dfrac{dv}{dx} = 1\) |
:::

:::exam What MF19 gives you in this chapter
MF19 gives \(\int\sinh x\), \(\int\cosh x\), \(\int\operatorname{sech}^2x\), \(\int\sec x\), \(\int\operatorname{cosec}x\), the three root forms \(\sin^{-1}\), \(\sinh^{-1}\), \(\cosh^{-1}\), the 9709 entries (\(\tan^{-1}\) form and the two log forms), and \(\sin x\), \(\cos x\) in terms of \(t = \tan\frac x2\). It does **not** give \(\int\tanh x\), the integrals of \(\sinh^2x\) or \(\cosh^2x\), or the results for \(\int\sqrt{a^2 \pm x^2}\,dx\). When a question says "use the substitution …" you must use it and show the change of variable, the limits and \(dx\). Exact answers (with \(\ln\) or \(\sinh^{-1}\) written as a logarithm) are expected unless a decimal is asked for.
:::

:::board
UK Further Maths (Edexcel 9FM0 Core Pure, AQA 7367) includes integrals that lead to inverse trigonometric and inverse hyperbolic functions, and integration by hyperbolic and trigonometric substitution. The methods match this chapter.
:::

:::eg Spot the error: use \(x = 2\sinh u\) to find the exact value of \(\displaystyle\int_0^2\sqrt{x^2 + 4}\,dx\), for 5 marks.
A student wrote this answer.

Line 1: \(x = 2\sinh u\), \(dx = 2\cosh u\,du\), \(\sqrt{x^2 + 4} = 2\cosh u\), so the integral is \(\displaystyle\int 4\cosh^2u\,du\)
Line 2: \(= \displaystyle\int 2(1 + \cosh 2u)\,du = 2u + \sinh 2u\)
Line 3: \(= \left[2u + \sinh 2u\right]_0^2 = 4 + \sinh 4 = 31.3\)

Lines 1 and 2 are correct and earn the first four marks. [M1] [A1] [M1] [A1]

**Line 3 substitutes the \(x\)-limits into an expression in \(u\), so the final accuracy mark is lost.** [A0] The limits must change with the variable: \(x = 2\) gives \(\sinh u = 1\), so \(u = \sinh^{-1}1 = \ln\left(1 + \sqrt2\right)\). The student scores 4 out of 5.

Correct line 3: with \(\sinh u = 1\) and \(\cosh u = \sqrt2\), \(\sinh 2u = 2\sqrt2\), so the value is \(2\ln\left(1 + \sqrt2\right) + 2\sqrt2\). [A1]

**Check** with the standard result: \(\tfrac12\left[2\sqrt8 + 4\sinh^{-1}1\right] = 2\sqrt2 + 2\sinh^{-1}1\), the same, \(= 4.59\).
:::

:::try Start easy, finish at exam standard
Q: Find (a) \(\displaystyle\int\left(2\sinh 3x + \cosh\tfrac x2\right)dx\), (b) \(\displaystyle\int\operatorname{sech}^2 4x\,dx\).
A: (a) \(\tfrac23\cosh 3x + 2\sinh\tfrac x2 + c\). (b) \(\tfrac14\tanh 4x + c\).
Q: Find the exact value of \(\displaystyle\int_0^{\ln 2}\sinh^2x\,dx\).
A: \(\tfrac12\left[\tfrac12\sinh 2x - x\right]_0^{\ln 2} = \tfrac12\left(\tfrac{15}{16} - \ln 2\right) = \tfrac{15}{32} - \tfrac12\ln 2\).
Q: Find \(\displaystyle\int\frac{1}{\sqrt{16 - x^2}}\,dx\) and \(\displaystyle\int\frac{1}{\sqrt{x^2 + 16}}\,dx\).
A: \(\sin^{-1}\dfrac x4 + c\) and \(\sinh^{-1}\dfrac x4 + c\).
Q: Find \(\displaystyle\int_1^2\frac{1}{\sqrt{x^2 - 1}}\,dx\) in exact form.
A: \(\left[\cosh^{-1}x\right]_1^2 = \cosh^{-1}2 - 0 = \ln\left(2 + \sqrt3\right)\).
Q: Find \(\displaystyle\int\frac{1}{\sqrt{4x^2 + 9}}\,dx\).
A: \(\dfrac{1}{2\sqrt{x^2 + \frac94}}\), so \(\tfrac12\sinh^{-1}\dfrac{2x}{3} + c\).
Q: Find \(\displaystyle\int\frac{1}{\sqrt{x^2 - 6x + 13}}\,dx\).
A: \(x^2 - 6x + 13 = (x - 3)^2 + 4\), so \(\sinh^{-1}\dfrac{x - 3}{2} + c\).
Q: Show that \(\displaystyle\int_2^3\frac{1}{x^2 - 1}\,dx = \tfrac12\ln\tfrac32\).
A: \(\dfrac{1}{x^2 - 1} = \tfrac12\left(\dfrac{1}{x - 1} - \dfrac{1}{x + 1}\right)\), so the integral is \(\tfrac12\left[\ln\dfrac{x - 1}{x + 1}\right]_2^3 = \tfrac12\left(\ln\tfrac12 - \ln\tfrac13\right) = \tfrac12\ln\tfrac32\).
Q: Find \(\displaystyle\int\frac{x}{\sqrt{x^2 + 9}}\,dx\).
A: Let \(u = x^2 + 9\): \(\sqrt{x^2 + 9} + c\). The numerator is the derivative of what is under the root, so no inverse function is needed.
Q: Find \(\displaystyle\int_0^3\sqrt{9 - x^2}\,dx\).
A: A quarter of a circle of radius 3: \(\tfrac14\pi(9) = \dfrac{9\pi}{4}\). By the formula, \(\tfrac12\left[x\sqrt{9 - x^2} + 9\sin^{-1}\tfrac x3\right]_0^3 = \tfrac12 \times 9 \times \tfrac\pi2 = \tfrac{9\pi}{4}\).
Q: Use \(x = 3\cosh u\) to show that \(\displaystyle\int\sqrt{x^2 - 9}\,dx = \tfrac12\left[x\sqrt{x^2 - 9} - 9\cosh^{-1}\tfrac x3\right] + c\).
A: \(dx = 3\sinh u\,du\) and \(\sqrt{x^2 - 9} = 3\sinh u\), so the integral is \(9\int\sinh^2u\,du = \tfrac92\left(\sinh u\cosh u - u\right)\). With \(\cosh u = \tfrac x3\) and \(\sinh u = \tfrac{\sqrt{x^2 - 9}}{3}\) this is \(\tfrac12\left[x\sqrt{x^2 - 9} - 9\cosh^{-1}\tfrac x3\right]\).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ (a) Find \(\displaystyle\int 6\sinh 2x\,dx\). (b) Find the exact value of \(\displaystyle\int_0^{\ln 3}\cosh x\,dx\).
A: (a) \(3\cosh 2x + c\). [M1 A1]
(b) \(\left[\sinh x\right]_0^{\ln 3} = \sinh(\ln 3)\) [M1] \(= \dfrac{3 - \frac13}{2} = \dfrac43\). [A1]
Q: [4 marks] ★ Find (a) \(\displaystyle\int\frac{1}{\sqrt{25 - 4x^2}}\,dx\), (b) \(\displaystyle\int\frac{1}{\sqrt{9x^2 + 16}}\,dx\).
A: (a) \(\dfrac{1}{2\sqrt{\frac{25}{4} - x^2}}\) so \(\tfrac12\sin^{-1}\dfrac{2x}{5} + c\). [M1 A1]
(b) \(\dfrac{1}{3\sqrt{x^2 + \frac{16}{9}}}\) so \(\tfrac13\sinh^{-1}\dfrac{3x}{4} + c\). [M1 A1]
Q: [5 marks] ★★ Find the exact value of \(\displaystyle\int_5^7\frac{1}{\sqrt{x^2 - 6x + 8}}\,dx\).
A: \(x^2 - 6x + 8 = (x - 3)^2 - 1\) [M1]
\[\int_5^7\frac{dx}{\sqrt{(x - 3)^2 - 1}} = \left[\cosh^{-1}(x - 3)\right]_5^7\] [A1]
\[= \cosh^{-1}4 - \cosh^{-1}2\] [M1]
\[= \ln\left(4 + \sqrt{15}\right) - \ln\left(2 + \sqrt3\right)\] [A1]
\[= \ln\frac{4 + \sqrt{15}}{2 + \sqrt3} \quad (= 0.746)\] [A1]
Q: [5 marks] ★★ Find the exact value of \(\displaystyle\int_0^{\ln 3}\sinh^2x\,dx\).
A: \(\sinh^2x = \tfrac12(\cosh 2x - 1)\) [M1]
\[\int_0^{\ln 3}\sinh^2x\,dx = \tfrac12\left[\tfrac12\sinh 2x - x\right]_0^{\ln 3}\] [A1]
\(\sinh(2\ln 3) = \dfrac{9 - \frac19}{2} = \dfrac{40}{9}\) [M1]
\[= \tfrac12\left(\tfrac{20}{9} - \ln 3\right)\] [A1]
\[= \tfrac{10}{9} - \tfrac12\ln 3\] [A1]
Q: [5 marks] ★★ Use integration by parts to show that \(\displaystyle\int_0^{1/2}\sin^{-1}x\,dx = \dfrac{\pi}{12} + \dfrac{\sqrt3}{2} - 1\).
A: \(u = \sin^{-1}x\), \(\dfrac{dv}{dx} = 1\), so \(\dfrac{du}{dx} = \dfrac{1}{\sqrt{1 - x^2}}\) and \(v = x\). [M1]
\[\int\sin^{-1}x\,dx = x\sin^{-1}x - \int\frac{x}{\sqrt{1 - x^2}}\,dx\] [A1]
\[\int\frac{x}{\sqrt{1 - x^2}}\,dx = -\sqrt{1 - x^2}\] [M1 A1]
\[\left[x\sin^{-1}x + \sqrt{1 - x^2}\right]_0^{1/2} = \tfrac12 \times \tfrac\pi6 + \tfrac{\sqrt3}{2} - 1\] [A1]
Q: [7 marks] ★★★ Use the substitution \(x = \sinh u\) to show that \(\displaystyle\int_1^2\frac{1}{x^2\sqrt{x^2 + 1}}\,dx = \sqrt2 - \frac{\sqrt5}{2}\).
H: Find \(dx\) and the root in terms of \(u\); one factor cancels.
H: You will need \(\int\operatorname{cosech}^2u\,du = -\coth u\).
H: Change the limits: \(\sinh u = 1\) and \(\sinh u = 2\). Then \(\coth u = \dfrac{\cosh u}{\sinh u}\).
A: \(dx = \cosh u\,du\) and \(\sqrt{x^2 + 1} = \cosh u\). [B1]
\[\int\frac{\cosh u}{\sinh^2u\cosh u}\,du = \int\operatorname{cosech}^2u\,du\] [M1 A1]
\[= -\coth u\] [A1]
Limits: \(\sinh u = 1\) and \(\sinh u = 2\). [B1]
At \(\sinh u = 2\): \(\cosh u = \sqrt5\), so \(\coth u = \dfrac{\sqrt5}{2}\). At \(\sinh u = 1\): \(\coth u = \sqrt2\). [M1]
\[\left[-\coth u\right] = -\frac{\sqrt5}{2} + \sqrt2\] [A1]
Q: [10 marks] (#math.p3.inttech) ★★★ (a) Use the substitution \(t = \tan\frac x2\) to show that \(\displaystyle\int_0^{\pi/2}\frac{1}{5 + 3\cos x}\,dx = \tfrac12\tan^{-1}\tfrac12\). (b) Find \(\displaystyle\int_0^{\pi/2}e^x\cos x\,dx\) by integrating by parts twice.
H: In (a) write \(\cos x\) and \(dx\) in terms of \(t\); the factor \(1 + t^2\) cancels.
H: The limits are \(t = 0\) and \(t = 1\).
H: In (b) after two applications of parts the original integral appears on the right: solve for it.
A: (a) \(5 + 3\cos x = \dfrac{5\left(1 + t^2\right) + 3\left(1 - t^2\right)}{1 + t^2} = \dfrac{8 + 2t^2}{1 + t^2}\) [M1 A1]
\[\int\frac{1}{5 + 3\cos x}\,dx = \int\frac{1 + t^2}{8 + 2t^2}\times\frac{2}{1 + t^2}\,dt = \int\frac{dt}{4 + t^2}\] [M1 A1]
Limits \(t = 0\) to \(t = 1\). [B1]
\[\left[\tfrac12\tan^{-1}\tfrac t2\right]_0^1 = \tfrac12\tan^{-1}\tfrac12\] [A1]
(b) \(I = \int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx\) [M1]
\[\int e^x\sin x\,dx = e^x\sin x - I\] [A1]
So \(I = \tfrac12e^x(\sin x + \cos x)\) [M1], and \(\displaystyle\int_0^{\pi/2}e^x\cos x\,dx = \tfrac12\left(e^{\pi/2} - 1\right)\). [A1]
Q: [8 marks] (#math.p3.integ) ★★★ The region \(R\) is bounded by the curve \(y = \dfrac{1}{\sqrt{x^2 + 9}}\), the \(x\)-axis and the lines \(x = 0\) and \(x = 4\). (a) Show that the area of \(R\) is \(\ln 3\). (b) Find the exact volume of the solid formed when \(R\) is rotated through \(2\pi\) radians about the \(x\)-axis.
H: For (a) use \(\sinh^{-1}\dfrac xa\) and evaluate \(\sinh^{-1}\tfrac43\) as a logarithm.
H: For (b) the volume is \(\pi\int y^2\,dx\), and \(y^2\) has no root.
A: (a) Area \(= \displaystyle\int_0^4\frac{dx}{\sqrt{x^2 + 9}} = \left[\sinh^{-1}\frac x3\right]_0^4\) [M1 A1]
\[= \sinh^{-1}\tfrac43 = \ln\left(\tfrac43 + \sqrt{\tfrac{16}{9} + 1}\right) = \ln\left(\tfrac43 + \tfrac53\right)\] [M1]
\[= \ln 3\] [A1]
(b) \(V = \pi\displaystyle\int_0^4\frac{dx}{x^2 + 9}\) [M1] \(= \pi\left[\tfrac13\tan^{-1}\tfrac x3\right]_0^4\) [A1]
\[= \frac\pi3\tan^{-1}\tfrac43\] [A1] \(= 0.971\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A skylight is the part of the ellipse \(\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1\) (units of metres) for which \(x \ge 3\). Find its area to 3 significant figures.
H: Solve for \(y\) in the upper half and double.
H: Use \(x = 5\sin\theta\); the root becomes \(5\cos\theta\) and \(\theta\) runs from \(\sin^{-1}\tfrac35\) to \(\tfrac\pi2\).
H: \(\cos^2\theta = \tfrac12(1 + \cos 2\theta)\).
A: \(y = \tfrac35\sqrt{25 - x^2}\) in the upper half, so the area is \(A = 2\displaystyle\int_3^5\tfrac35\sqrt{25 - x^2}\,dx\). [M1 M1]
\(x = 5\sin\theta\), \(dx = 5\cos\theta\,d\theta\), \(\sqrt{25 - x^2} = 5\cos\theta\). Limits \(\theta_0 = \sin^{-1}\tfrac35\) and \(\tfrac\pi2\). [M1]
\[A = \frac65\int_{\theta_0}^{\pi/2}25\cos^2\theta\,d\theta\] [A1]
\[= 30 \times \tfrac12\left[\theta + \tfrac12\sin 2\theta\right]_{\theta_0}^{\pi/2}\] [M1 A1]
At \(\theta_0\): \(\sin\theta_0 = \tfrac35\), \(\cos\theta_0 = \tfrac45\), \(\sin 2\theta_0 = \tfrac{24}{25}\), so
\[A = 15\left[\tfrac\pi2 - \theta_0 - \tfrac12\left(\tfrac{24}{25}\right)\right] = 15\left(1.5708 - 0.6435 - 0.48\right) = 6.71\ \text{m}^2\] [M1 A1]
Q: [5 marks] ★★★ (a) By substituting \(u = \sinh x\), show that \(\displaystyle\int\operatorname{sech}x\,dx = \tan^{-1}(\sinh x) + c\). (b) Find the exact value of \(\displaystyle\int_0^{\ln 3}\operatorname{sech}x\,dx\).
H: Write \(\operatorname{sech}x = \dfrac{\cosh x}{\cosh^2x}\) and use \(\cosh^2x = 1 + \sinh^2x\).
H: The integral becomes a standard \(\tan^{-1}\) form.
A: (a) \(\operatorname{sech}x = \dfrac{\cosh x}{1 + \sinh^2x}\), and \(du = \cosh x\,dx\). [M1]
\[\int\frac{du}{1 + u^2} = \tan^{-1}u + c = \tan^{-1}(\sinh x) + c\] [M1 A1]
(b) \(\sinh(\ln 3) = \tfrac43\), so the value is \(\tan^{-1}\tfrac43 - \tan^{-1}0 = \tan^{-1}\tfrac43\) \((= 0.927)\). [M1 A1]
:::

:::quiz
? What is \(\displaystyle\int\frac{1}{\sqrt{x^2 + 25}}\,dx\)?
+ \(\sinh^{-1}\dfrac x5 + c\)
- \(\sin^{-1}\dfrac x5 + c\)
- \(\cosh^{-1}\dfrac x5 + c\)
- \(\dfrac15\sinh^{-1}\dfrac x5 + c\)
> A plus sign under the root gives the \(\sinh^{-1}\) form with no extra factor. \(\sin^{-1}\) needs \(a^2 - x^2\), \(\cosh^{-1}\) needs \(x^2 - a^2\), and the standard form has no \(\dfrac1a\) in front.
? What is \(\displaystyle\int\frac{1}{\sqrt{9 - 4x^2}}\,dx\)?
- \(\sin^{-1}\dfrac{2x}{3} + c\)
+ \(\tfrac12\sin^{-1}\dfrac{2x}{3} + c\)
- \(2\sin^{-1}\dfrac{2x}{3} + c\)
- \(\tfrac13\sin^{-1}\dfrac{2x}{3} + c\)
> Taking the 4 out of the root gives a factor \(\dfrac{1}{2}\). Differentiating \(\tfrac12\sin^{-1}\tfrac{2x}{3}\) gives \(\tfrac12 \times \dfrac{2/3}{\sqrt{1 - 4x^2/9}} = \dfrac{1}{\sqrt{9 - 4x^2}}\).
? When using \(x = 3\sinh u\) in \(\displaystyle\int\frac{dx}{\sqrt{x^2 + 9}}\), what is \(dx\)?
- \(3\sinh u\,du\)
+ \(3\cosh u\,du\)
- \(\dfrac{1}{3\cosh u}\,du\)
- \(-3\cosh u\,du\)
> The derivative of \(\sinh u\) is \(\cosh u\), with no minus sign. Leaving out the factor \(3\cosh u\) is the commonest slip in this method.
? What is \(\displaystyle\int\tanh x\,dx\)?
- \(\operatorname{sech}^2x + c\)
- \(\ln\sinh x + c\)
+ \(\ln\cosh x + c\)
- \(\tanh^{-1}x + c\)
> \(\tanh x = \dfrac{\sinh x}{\cosh x}\), and the numerator is the derivative of the denominator. \(\operatorname{sech}^2x\) is the derivative of \(\tanh x\), not its integral.
? Which identity should you use to integrate \(\sinh^2x\)?
- \(\sinh^2x = \tfrac12(\cosh 2x + 1)\)
+ \(\sinh^2x = \tfrac12(\cosh 2x - 1)\)
- \(\sinh^2x = 1 - \cosh^2x\)
- \(\sinh^2x = 2\sinh x\cosh x\)
> \(\cosh 2x = 1 + 2\sinh^2x\), so \(\sinh^2x = \tfrac12(\cosh 2x - 1)\). The plus version is for \(\cosh^2x\), and the last option is \(\sinh 2x\).
? A definite integral \(\displaystyle\int_0^2\ldots dx\) is evaluated with \(x = 2\sinh u\). The limits for \(u\) are
- 0 and 2
+ 0 and \(\sinh^{-1}1\)
- 0 and \(\sinh 2\)
- 0 and \(\cosh^{-1}1\)
> When \(x = 2\), \(2\sinh u = 2\), so \(\sinh u = 1\) and \(u = \sinh^{-1}1\). Keeping the \(x\)-limits is the slip in the Spot the error example.
:::

:::checklist What you can now do
- [ ] I can integrate \(\sinh\), \(\cosh\), \(\operatorname{sech}^2\), \(\tanh\) and \(\coth\), with a linear argument, and use identities to integrate \(\sinh^2x\) and \(\cosh^2x\).
- [ ] I can recognise and integrate \(\dfrac{1}{\sqrt{a^2 - x^2}}\), \(\dfrac{1}{\sqrt{x^2 + a^2}}\) and \(\dfrac{1}{\sqrt{x^2 - a^2}}\), including when the coefficient of \(x^2\) is not 1.
- [ ] I can complete the square to bring a quadratic under a root to a standard form, and split a linear numerator.
- [ ] I can use \(x = a\sin\theta\), \(x = a\sinh u\) and \(x = a\cosh u\) to integrate expressions with a square root, changing \(dx\) and the limits.
- [ ] I can find \(\int\sqrt{a^2 - x^2}\,dx\), \(\int\sqrt{x^2 + a^2}\,dx\) and \(\int\sqrt{x^2 - a^2}\,dx\) by substitution.
- [ ] I can use 9709 methods in harder cases: parts twice, parts with an inverse function and \(t = \tan\frac x2\).
- [ ] I can write definite integrals in exact logarithmic form, using the log form of the inverse hyperbolic functions.
:::

:::recap
- \(\int\sinh x = \cosh x\), \(\int\cosh x = \sinh x\), \(\int\operatorname{sech}^2x = \tanh x\), \(\int\tanh x = \ln\cosh x\); divide by \(k\) for \(\sinh kx\) and \(\cosh kx\).
- \(\cosh^2x = \tfrac12(1 + \cosh 2x)\) and \(\sinh^2x = \tfrac12(\cosh 2x - 1)\) integrate squares; split odd powers and substitute \(u = \cosh x\) or \(\sinh x\).
- \(\displaystyle\int\frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}\frac xa\), \(\displaystyle\int\frac{dx}{\sqrt{x^2 + a^2}} = \sinh^{-1}\frac xa\), \(\displaystyle\int\frac{dx}{\sqrt{x^2 - a^2}} = \cosh^{-1}\frac xa\) (all in MF19). Take out any coefficient of \(x^2\) first.
- Complete the square when the quadratic under the root has an \(x\) term; split a linear numerator into a derivative part and a constant.
- Substitutions: \(x = a\sin\theta\), \(a\sinh u\), \(a\cosh u\) for the three roots. Find \(dx\) and change the limits.
- \(\int\sqrt{x^2 + a^2}\,dx = \tfrac12\left[x\sqrt{x^2 + a^2} + a^2\sinh^{-1}\tfrac xa\right]\), and similarly for the others (derive these).
- Parts twice for \(e^x\sin x\); parts with \(\dfrac{dv}{dx} = 1\) for \(\sinh^{-1}x\), \(\sin^{-1}x\); \(t = \tan\frac x2\) with \(dx = \dfrac{2\,dt}{1 + t^2}\) for \(\dfrac{1}{a + b\cos x}\).
- Give exact answers: \(\sinh^{-1}u = \ln\left(u + \sqrt{u^2 + 1}\right)\).
:::

:::links
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · integration with hyperbolic functions and inverse standard forms
- practise: [Further integration booklets](https://madasmaths.com/archive_maths_booklets_further_topics_integration.html) · MadAsMaths · graded integration questions with answers
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · hyperbolic functions and calculus booklets
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot an integrand and check an area with a numerical integral
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Reduction formulae](#math.fm.reduction) builds a recurrence for a whole family of integrals, such as \(\int\sin^nx\,dx\), and uses it to evaluate any member of the family.
