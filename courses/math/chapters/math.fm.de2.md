@chapter math.fm.de2
@title Second order differential equations
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 7–9 hours
@summary A second order linear equation with constant coefficients has a general solution made of two parts: a complementary function, found from an auxiliary quadratic whose roots can be real, repeated or complex, and a particular integral, found by trying a suitable form and comparing coefficients. You will find both, fit initial conditions, use the substitution \(x = e^{t}\) to turn an equation with variable coefficients into one with constant coefficients, and read the answers as oscillations that die away or grow.

:::why
Anything that oscillates or settles obeys a second order equation: a mass on a spring with a damper, a car's suspension, current in a circuit with a coil and a capacitor, a swinging door that closes smoothly. The same two-part method (a natural motion that fades, plus a response to the push) solves all of them. Understanding it also explains why a gentle push at exactly the right rhythm can build up a huge swing.
:::

**Before you start**, you need complex roots of quadratics from [Complex numbers](#math.p3.complex), the product and chain rules from [Further differentiation](#math.p3.diff), and integrating factors from [First order differential equations](#math.fm.de). The exponential form \(e^{\mathrm{i}\theta}\), used again in [De Moivre's theorem and trigonometry](#math.fm.complex), is why complex roots give cosines and sines, and \(\cosh\) and \(\sinh\) from [Hyperbolic functions](#math.fm.hyperbolic) give an alternative form in one case.

:::try Warm-up
Q: Solve \(m^2 - 4m + 13 = 0\). (from [Complex numbers](#math.p3.complex))
A: \(m = \dfrac{4 \pm \sqrt{16 - 52}}{2} = \dfrac{4 \pm 6\mathrm{i}}{2}\), so \(m = 2 \pm 3\mathrm{i}\).
Q: Differentiate \(xe^{-2x}\) with respect to \(x\). (from [Further differentiation](#math.p3.diff))
A: Product rule: \(1 \cdot e^{-2x} + x \cdot (-2e^{-2x}) = (1 - 2x)e^{-2x}\).
Q: Find the general solution of \(\dfrac{dy}{dx} + 3y = 6\). (from [First order differential equations](#math.fm.de))
A: \(I = e^{3x}\), so \(\dfrac{d}{dx}(ye^{3x}) = 6e^{3x}\), \(ye^{3x} = 2e^{3x} + c\) and \(y = 2 + ce^{-3x}\).
:::

## Linear equations with constant coefficients

A **second order** differential equation contains \(\dfrac{d^2y}{dx^2}\) as its highest derivative. The ones in this chapter have the form
\[a\frac{d^2y}{dx^2} + b\frac{dy}{dx} + cy = f(x)\]
where \(a\), \(b\), \(c\) are constants and \(a \neq 0\). They are **linear** (\(y\), \(y'\) and \(y''\) appear only to the first power, never multiplied together) with **constant coefficients** (\(a\), \(b\), \(c\) do not depend on \(x\)).

If \(f(x) = 0\) the equation is called **homogeneous**. Its solutions are the equation's "natural" behaviour, with nothing pushing it. The right side \(f(x)\) is the push, or forcing.

:::def Complementary function
The general solution of the homogeneous equation \(ay'' + by' + cy = 0\). For a second order equation it contains **two** arbitrary constants. Written CF.
:::

:::def Particular integral
Any one solution of the full equation \(ay'' + by' + cy = f(x)\), with no arbitrary constants. Written PI.
:::

:::key General solution
\[\text{general solution} = \text{complementary function} + \text{particular integral}\]
The two arbitrary constants in the general solution come from the complementary function. A **particular solution** is the one member of the family that fits two conditions, usually \(y\) and \(\dfrac{dy}{dx}\) at one value of \(x\).
:::

:::proof Why complementary function plus particular integral gives every solution
Write \(L[y]\) for \(ay'' + by' + cy\). Differentiation is linear, so \(L[y_1 + y_2] = L[y_1] + L[y_2]\) and \(L[ky] = kL[y]\).
- Let \(y_p\) be a particular integral, so \(L[y_p] = f\).
- Let \(y_c\) be any solution of the homogeneous equation, so \(L[y_c] = 0\).
- Then \(L[y_c + y_p] = 0 + f = f\), so \(y_c + y_p\) solves the full equation.
- Conversely, if \(y\) is any solution of the full equation, then \(L[y - y_p] = f - f = 0\).
- So \(y - y_p\) is a solution of the homogeneous equation, and \(y = (y - y_p) + y_p\) has the form CF + PI.
:::

The same idea appeared at the end of [First order differential equations](#math.fm.de): two solutions of a first order linear equation differ by a multiple of \(e^{-\int P\,dx}\), the complementary part. Now the complementary part has two arbitrary constants, because a second order equation needs two integrations to undo.

## The complementary function

### Why \(e^{mx}\)

What function is nearly unchanged by differentiating? An exponential. Try \(y = e^{mx}\), so \(y' = me^{mx}\) and \(y'' = m^2e^{mx}\), in \(ay'' + by' + cy = 0\):
\[\left(am^2 + bm + c\right)e^{mx} = 0\]
Since \(e^{mx}\) is never zero, \(y = e^{mx}\) is a solution exactly when \(m\) satisfies the quadratic equation \(am^2 + bm + c = 0\).

:::def Auxiliary equation
For \(ay'' + by' + cy = 0\), the quadratic \(am^2 + bm + c = 0\). Its roots \(m\) are the exponents that make \(e^{mx}\) a solution. Written AE.
:::

A quadratic has three possible kinds of roots, and each gives a different shape of solution.

:::key The complementary function, by the roots of the auxiliary equation
| Roots of the AE | Complementary function |
|---|---|
| distinct real \(m_1, m_2\) | \(Ae^{m_1x} + Be^{m_2x}\) |
| repeated real \(m\) | \((A + Bx)e^{mx}\) |
| complex \(p \pm q\mathrm{i}\) | \(e^{px}(A\cos qx + B\sin qx)\) |
In each case \(y\) equals the expression shown. For complex roots \(q > 0\).
\(A\) and \(B\) are arbitrary real constants. The case is decided by the discriminant \(b^2 - 4ac\): positive, zero, negative.
:::

**Distinct real roots.** Each root gives its own solution, and \(A\) times one plus \(B\) times the other is still a solution (by the linearity above). That is a two-constant family, so it is the general solution.

**A repeated root** gives only one exponential, \(e^{mx}\), but a second solution is needed. It is \(xe^{mx}\).

:::proof Why \(xe^{mx}\) is a second solution when \(m\) is a repeated root
Divide the equation by \(a\) so that it is \(y'' + 2\beta y' + \gamma y = 0\). A repeated root means \(\beta^2 = \gamma\) and the root is \(m = -\beta\).
- Take \(y = xe^{mx}\). By the product rule, \(y' = (1 + mx)e^{mx}\).
- Differentiate again: \(y'' = (2m + m^2x)e^{mx}\).
- Substitute with \(\beta = -m\) and \(\gamma = m^2\):
\[y'' - 2my' + m^2y = e^{mx}\left[(2m + m^2x) - 2m(1 + mx) + m^2x\right]\]
- The bracket is \(2m + m^2x - 2m - 2m^2x + m^2x = 0\), so \(xe^{mx}\) is a solution.
:::

**Complex roots.** If \(m = p + q\mathrm{i}\), then \(e^{mx} = e^{px}e^{\mathrm{i}qx} = e^{px}(\cos qx + \mathrm{i}\sin qx)\), by the exponential form of [Complex numbers](#math.p3.complex). The real equation has real coefficients, so the real part \(e^{px}\cos qx\) and the imaginary part \(e^{px}\sin qx\) are each solutions on their own. Combining them with arbitrary real constants gives the form in the table. The conjugate root \(p - q\mathrm{i}\) gives nothing new.

:::eg Find the general solution of (a) \(y'' - 5y' + 6y = 0\), (b) \(y'' + 6y' + 9y = 0\), (c) \(y'' + 2y' + 5y = 0\).
(a) AE: \(m^2 - 5m + 6 = 0\), \((m - 2)(m - 3) = 0\), so \(m = 2\) or \(3\):
\[y = Ae^{2x} + Be^{3x}\]
(b) AE: \(m^2 + 6m + 9 = 0\), \((m + 3)^2 = 0\), so \(m = -3\) (repeated):
\[y = (A + Bx)e^{-3x}\]
(c) AE: \(m^2 + 2m + 5 = 0\), \(m = \dfrac{-2 \pm \sqrt{4 - 20}}{2} = -1 \pm 2\mathrm{i}\), so \(p = -1\), \(q = 2\):
\[y = e^{-x}(A\cos 2x + B\sin 2x)\]
:::

:::eg Find the general solution of (a) \(y'' + 9y = 0\), (b) \(y'' - 9y = 0\), (c) \(4y'' + 12y' + 9y = 0\).
(a) AE: \(m^2 + 9 = 0\), \(m = \pm 3\mathrm{i}\). Here \(p = 0\), \(q = 3\), and \(e^{0x} = 1\):
\[y = A\cos 3x + B\sin 3x\]
(b) AE: \(m^2 - 9 = 0\), \(m = \pm 3\):
\[y = Ae^{3x} + Be^{-3x}\]
This can also be written \(y = C\cosh 3x + D\sinh 3x\), which is handy when conditions are given at \(x = 0\), because \(\cosh 0 = 1\) and \(\sinh 0 = 0\) (see [Hyperbolic functions](#math.fm.hyperbolic)).
(c) Keep the leading coefficient 4 in the AE: \(4m^2 + 12m + 9 = 0\), \((2m + 3)^2 = 0\), so \(m = -\tfrac32\) (repeated):
\[y = (A + Bx)e^{-3x/2}\]
:::

### Fitting two conditions

Two arbitrary constants need two conditions, usually the value of \(y\) and of \(\dfrac{dy}{dx}\) at \(x = 0\). Substitute the first into the solution, **differentiate** the solution, then substitute the second.

:::eg Solve \(y'' + 2y' + 5y = 0\), given that \(y = 1\) and \(\dfrac{dy}{dx} = 0\) when \(x = 0\).
From the example above, \(y = e^{-x}(A\cos 2x + B\sin 2x)\). When \(x = 0\), \(y = 1\), so \(A = 1\).

Differentiate with the product rule:
\[\frac{dy}{dx} = -e^{-x}(A\cos 2x + B\sin 2x) + e^{-x}(-2A\sin 2x + 2B\cos 2x)\]
When \(x = 0\), \(\dfrac{dy}{dx} = -A + 2B = 0\), so \(B = \tfrac12\):
\[y = e^{-x}\left(\cos 2x + \tfrac12\sin 2x\right)\]
:::

The widget below solves \(a y'' + b y' + c y = 0\) for any \(b\), \(c\) (here \(a = 1\)) and the starting values \(y(0)\) and \(y'(0)\). It names the case from the discriminant and draws the exact solution. The dashed curves, when they appear, are the envelope \(\pm Re^{px}\) that the oscillation stays inside.

:::html
<div class="widget" data-w="fm-de" data-a="1" data-b="2" data-c="5" data-y0="1" data-v0="0"></div>
:::

Try these. Start at \(b = 2\), \(c = 5\) (roots \(-1 \pm 2\mathrm{i}\), the example above). Move \(b\) to 0: the decay stops and the oscillation never dies (\(p = 0\)). Make \(b\) negative: the oscillation grows. Now return to \(b = 4\) and slide \(c\) down from 5: at \(c = 4\) the roots become repeated, and below 4 they are real and the oscillation disappears. The boundary between oscillating and not is the discriminant \(b^2 - 4c = 0\). Then change \(y(0)\) and \(y'(0)\) and watch that the shape stays the same while its size and phase change.

## First order equations with constant coefficients

The same CF-plus-PI route solves first order equations \(a\dfrac{dy}{dx} + by = f(x)\). The auxiliary equation is \(am + b = 0\), so \(m = -\dfrac ba\) and the complementary function is \(Ae^{-bx/a}\). You met the integrating-factor method for these in [First order differential equations](#math.fm.de); the new method gives the same answer and it is the one that generalises to second order.

## Particular integrals

The complementary function solves the "unforced" equation. To solve the full equation you also need one function that, put into the left side, gives \(f(x)\). The idea is a **trial form** with unknown coefficients: choose a function of the same family as \(f\), substitute, and choose the coefficients to make both sides agree.

:::key Trial forms for the particular integral
| If \(f(x)\) is… | try \(y =\) |
|---|---|
| polynomial, degree \(n\) | polynomial, degree \(n\), with **every** power |
| \(ke^{bx}\) | \(\lambda e^{bx}\) |
| cos, sin or both | \(\lambda\cos px + \mu\sin px\), **both** terms, always |
| a sum of these | the sum of the trial forms |
For a quadratic, for example, try \(\lambda x^2 + \mu x + \nu\), even if \(f\) has no \(x\) term.
If the trial form is already part of the complementary function, it gives 0 on the left and cannot work. Multiply it by \(x\) (by \(x^2\) if \(e^{bx}\) corresponds to a repeated root). In 9231 questions the form is given when this happens: for example "show that \(kx\cos 2x\) is a particular integral".
:::

:::steps
1. Find the complementary function first: it shows whether the trial form clashes.
2. Choose the trial form from the table.
3. Differentiate it as many times as the equation needs.
4. Substitute, then compare coefficients: powers of \(x\) for a polynomial; the \(\cos\) and \(\sin\) terms for a trig function; the \(e^{bx}\) term for an exponential.
5. Write general solution \(=\) CF \(+\) PI.
:::

**Why both cos and sin?** Differentiating \(\cos px\) gives \(\sin px\), and the middle term \(by'\) mixes them. A trial form with only a cosine cannot produce a matching equation unless \(b = 0\).

:::eg Find the general solution of \(y'' + 2y' - 3y = 12x + 4\).
CF: \(m^2 + 2m - 3 = (m + 3)(m - 1) = 0\), so \(y_c = Ae^{x} + Be^{-3x}\). No clash, since the right side has no exponential.

PI: \(f\) is a polynomial of degree 1, so try \(y = \lambda x + \mu\). Then \(y' = \lambda\) and \(y'' = 0\):
\[0 + 2\lambda - 3(\lambda x + \mu) = 12x + 4\]
Compare coefficients of \(x\): \(-3\lambda = 12\), so \(\lambda = -4\). Compare constants: \(2\lambda - 3\mu = 4\), so \(-8 - 3\mu = 4\) and \(\mu = -4\).

The PI is \(-4x - 4\) and
\[y = Ae^{x} + Be^{-3x} - 4x - 4\]
:::

:::eg Find the general solution of \(y'' - y' - 6y = 12e^{4x}\).
CF: \(m^2 - m - 6 = (m - 3)(m + 2) = 0\), so \(y_c = Ae^{3x} + Be^{-2x}\). The exponent 4 is not a root, so there is no clash.

PI: try \(y = \lambda e^{4x}\), so \(y' = 4\lambda e^{4x}\) and \(y'' = 16\lambda e^{4x}\):
\[(16 - 4 - 6)\lambda e^{4x} = 12e^{4x} \quad\Rightarrow\quad 6\lambda = 12 \quad\Rightarrow\quad \lambda = 2\]
\[y = Ae^{3x} + Be^{-2x} + 2e^{4x}\]
:::

:::eg Find the general solution of \(y'' + 3y' + 2y = 10\cos x\).
CF: \(m^2 + 3m + 2 = (m + 1)(m + 2) = 0\), so \(y_c = Ae^{-x} + Be^{-2x}\).

PI: try \(y = \lambda\cos x + \mu\sin x\), so \(y' = -\lambda\sin x + \mu\cos x\) and \(y'' = -\lambda\cos x - \mu\sin x\). Substitute:
\[\begin{aligned}
&(-\lambda\cos x - \mu\sin x) + 3(-\lambda\sin x + \mu\cos x) + 2(\lambda\cos x + \mu\sin x) \\
&\quad = (\lambda + 3\mu)\cos x + (\mu - 3\lambda)\sin x = 10\cos x
\end{aligned}\]
Compare the \(\cos x\) terms: \(\lambda + 3\mu = 10\). Compare the \(\sin x\) terms: \(\mu - 3\lambda = 0\), so \(\mu = 3\lambda\). Then \(\lambda + 9\lambda = 10\), so \(\lambda = 1\), \(\mu = 3\).
\[y = Ae^{-x} + Be^{-2x} + \cos x + 3\sin x\]
Notice that \(\mu\) is not zero even though \(f\) had no sine in it.
:::

:::warn A cosine on the right still needs a sine in the trial form
For \(y'' + 3y' + 2y = 10\cos x\), a trial form \(\lambda\cos x\) alone gives \(\lambda\cos x + 3(-\lambda\sin x) + \dots\): a stray \(\sin x\) term that nothing on the right can cancel. Always include \(\lambda\cos px + \mu\sin px\), whichever of the two \(f\) contains.
:::

### When the trial form is already in the complementary function

If \(f\) is a solution of the homogeneous equation, the trial form gives \(0\). Multiplying by \(x\) fixes that.

:::eg Find the general solution of \(y'' - 3y' + 2y = 5e^{2x}\).
CF: \(m^2 - 3m + 2 = (m - 1)(m - 2) = 0\), so \(y_c = Ae^{x} + Be^{2x}\). The right side contains \(e^{2x}\), and 2 is a root, so \(\lambda e^{2x}\) would give \(0\). Try \(y = kxe^{2x}\):
\[\begin{aligned}
y' &= k(1 + 2x)e^{2x} \\
y'' &= k(4 + 4x)e^{2x}
\end{aligned}\]
Substitute:
\[k\left[(4 + 4x) - 3(1 + 2x) + 2x\right]e^{2x} = k(1)e^{2x} = 5e^{2x}\]
The terms in \(x\) cancel, as they always do, so \(k = 5\):
\[y = Ae^{x} + Be^{2x} + 5xe^{2x}\]
If 2 were a repeated root, \(kx^2e^{2x}\) would be needed instead.
:::

The next example is the one the syllabus names: the trial form is given, and you find the coefficient.

:::eg Given that \(y = kx\cos 2x\) is a particular integral of \(y'' + 4y = \sin 2x\), find \(k\), and write down the general solution.
Differentiate with the product rule:
\[\begin{aligned}
y' &= k\cos 2x - 2kx\sin 2x \\
y'' &= -2k\sin 2x - 2k\sin 2x - 4kx\cos 2x = -4k\sin 2x - 4kx\cos 2x
\end{aligned}\]
Substitute into \(y'' + 4y\):
\[-4k\sin 2x - 4kx\cos 2x + 4kx\cos 2x = -4k\sin 2x\]
The \(x\cos 2x\) terms cancel. So \(-4k\sin 2x = \sin 2x\) and \(k = -\tfrac14\).

The CF has AE \(m^2 + 4 = 0\), \(m = \pm 2\mathrm{i}\), so
\[y = A\cos 2x + B\sin 2x - \tfrac14x\cos 2x\]
The forcing \(\sin 2x\) has the same frequency as the natural oscillations \(\cos 2x\) and \(\sin 2x\). That is **resonance**: the PI \(-\tfrac14x\cos 2x\) oscillates with an amplitude that grows in proportion to \(x\), without limit.
:::

## Initial conditions: the whole solution, always

A particular solution fits \(y\) and \(y'\) at a point. The rule is the same as for first order equations, with one trap: the conditions apply to the **general solution**, which already includes the PI. Find the CF and PI, add them, then use the conditions.

:::eg Solve \(y'' + 2y' - 3y = 12x + 4\), given that \(y = 0\) and \(\dfrac{dy}{dx} = -4\) when \(x = 0\).
From the example above, the general solution is \(y = Ae^{x} + Be^{-3x} - 4x - 4\). Differentiate:
\[\frac{dy}{dx} = Ae^{x} - 3Be^{-3x} - 4\]
At \(x = 0\): \(y = A + B - 4 = 0\), so \(A + B = 4\). Also \(\dfrac{dy}{dx} = A - 3B - 4 = -4\), so \(A = 3B\).

Then \(4B = 4\), so \(B = 1\) and \(A = 3\):
\[y = 3e^{x} + e^{-3x} - 4x - 4\]
**Check**: \(y(0) = 3 + 1 - 4 = 0\), and \(y'(0) = 3 - 3 - 4 = -4\).
:::

Questions on this topic are long (the June 2025 Paper 2 equation was worth 10 marks). They chain the steps in order: complementary function, particular integral, general solution, conditions.

:::eg (Exam style) The differential equation \(\dfrac{d^2y}{dx^2} + 4\dfrac{dy}{dx} + 13y = 26x + 21\) is given. (a) Find the complementary function. (b) Find the particular integral of the form \(y = \lambda x + \mu\). (c) Find the solution for which \(y = 3\) and \(\dfrac{dy}{dx} = 1\) when \(x = 0\).
**(a)** The auxiliary equation is \(m^2 + 4m + 13 = 0\) [M1]
\[m = \frac{-4 \pm \sqrt{16 - 52}}{2} = -2 \pm 3\mathrm{i}\] [A1]
\[y_c = e^{-2x}(A\cos 3x + B\sin 3x)\] [A1]
**(b)** Let \(y = \lambda x + \mu\), so \(y' = \lambda\) and \(y'' = 0\). [B1]
\[4\lambda + 13(\lambda x + \mu) = 26x + 21\] [M1]
Comparing \(x\): \(13\lambda = 26\), so \(\lambda = 2\). Comparing constants: \(8 + 13\mu = 21\), so \(\mu = 1\). The PI is \(2x + 1\). [A1]
**(c)** The general solution is
\[y = e^{-2x}(A\cos 3x + B\sin 3x) + 2x + 1\] [B1]
When \(x = 0\), \(y = 3\): \(A + 1 = 3\), so \(A = 2\). [M1]
Differentiate:
\[\frac{dy}{dx} = -2e^{-2x}(A\cos 3x + B\sin 3x) + e^{-2x}(-3A\sin 3x + 3B\cos 3x) + 2\]
When \(x = 0\), \(\dfrac{dy}{dx} = 1\): \(-2A + 3B + 2 = 1\), so \(-4 + 3B + 2 = 1\) and \(B = 1\). [M1]
\[y = e^{-2x}(2\cos 3x + \sin 3x) + 2x + 1\] [A1]
**Check**: \(y(0) = 2 + 1 = 3\).
:::

:::warn The three most common lost marks
1. **Trial form without the sine (or cosine).** Use \(\lambda\cos px + \mu\sin px\) every time.
2. **Using the conditions on the CF alone.** The general solution is CF + PI. Add the PI first, then differentiate the whole expression, then use the two conditions.
3. **A clash left unnoticed.** If the trial form is part of the CF, substituting gives \(0 = f(x)\). Multiply by \(x\) (or \(x^2\)).
:::

## Modelling oscillations

A mass on a spring, with a damper (like a car's shock absorber) and perhaps a driving force, has displacement \(x\) at time \(t\) satisfying
\[m\frac{d^2x}{dt^2} + c\frac{dx}{dt} + kx = F(t)\]
Newton's second law gives the left side: \(m\ddot{x}\) is mass times acceleration; the spring pulls back with a force proportional to the displacement; the damper resists with a force proportional to the speed. The details of the spring (Hooke's law) come in [Hooke's law and elastic energy](#math.fm.elastic); here the equation is given.

With no forcing (\(F = 0\)) the roots of the auxiliary equation describe the motion:

| Roots | What the mass does | Common name |
|---|---|---|
| complex, real part \(p < 0\) | oscillates, amplitude shrinking | light damping |
| real and repeated | returns to rest fastest, no oscillation | critical damping |
| real, distinct, negative | returns to rest slowly, no oscillation | heavy damping |

:::eg A mass of 2 kg on a spring is damped, so that its displacement \(x\) metres after \(t\) seconds satisfies \(2\dfrac{d^2x}{dt^2} + 8\dfrac{dx}{dt} + 26x = 0\). The mass is released from rest at \(x = 0.5\). Find \(x\) in terms of \(t\), and the period of the oscillation.
Divide by 2: \(\ddot{x} + 4\dot{x} + 13x = 0\). AE: \(m^2 + 4m + 13 = 0\), so \(m = -2 \pm 3\mathrm{i}\) and
\[x = e^{-2t}(A\cos 3t + B\sin 3t)\]
Released from rest at \(x = 0.5\) means \(x(0) = 0.5\) and \(\dot{x}(0) = 0\). So \(A = 0.5\). The derivative at \(t = 0\) is \(-2A + 3B\), so \(-1 + 3B = 0\) and \(B = \tfrac13\):
\[x = e^{-2t}\left(\tfrac12\cos 3t + \tfrac13\sin 3t\right)\]
The oscillation has angular frequency 3, so its period is \(\dfrac{2\pi}{3} = 2.09\) s (3 s.f.). Between one maximum and the next, the factor \(e^{-2t}\) shrinks the amplitude by \(e^{-4\pi/3} = 0.0152\): it is damped almost completely within a single cycle. This is light damping, but only just.
:::

:::eg (Exam style) The displacement \(x\) metres of a particle at time \(t\) seconds satisfies \(\dfrac{d^2x}{dt^2} + 2\dfrac{dx}{dt} + 5x = 10\cos t\). (a) Show that a particular integral is \(2\cos t + \sin t\). (b) Find the general solution. (c) Given that \(x = 1\) and \(\dfrac{dx}{dt} = 0\) when \(t = 0\), find \(x\) in terms of \(t\). (d) Describe the motion for large \(t\).
**(a)** Let \(x = \lambda\cos t + \mu\sin t\), so \(\dot{x} = -\lambda\sin t + \mu\cos t\) and \(\ddot{x} = -\lambda\cos t - \mu\sin t\). Substitute:
\[(4\lambda + 2\mu)\cos t + (4\mu - 2\lambda)\sin t = 10\cos t\] [M1]
\[4\lambda + 2\mu = 10, \qquad 4\mu - 2\lambda = 0\] [M1]
The second gives \(\lambda = 2\mu\), so \(10\mu = 10\): \(\mu = 1\), \(\lambda = 2\). The PI is \(2\cos t + \sin t\). [A1]
**(b)** AE: \(m^2 + 2m + 5 = 0\), so \(m = -1 \pm 2\mathrm{i}\). [M1]
\[x_c = e^{-t}(A\cos 2t + B\sin 2t)\] [A1]
\[x = e^{-t}(A\cos 2t + B\sin 2t) + 2\cos t + \sin t\] [B1]
**(c)** At \(t = 0\), \(x = 1\): \(A + 2 = 1\), so \(A = -1\). [M1]
Differentiate:
\[\dot{x} = -e^{-t}(A\cos 2t + B\sin 2t) + e^{-t}(-2A\sin 2t + 2B\cos 2t) - 2\sin t + \cos t\]
At \(t = 0\), \(\dot{x} = -A + 2B + 1 = 0\), so \(1 + 2B + 1 = 0\) and \(B = -1\). [M1]
\[x = -e^{-t}(\cos 2t + \sin 2t) + 2\cos t + \sin t\] [A1]
**(d)** The term in \(e^{-t}\) tends to 0 (it is the **transient**), so for large \(t\) the particle oscillates as \(2\cos t + \sin t\): period \(2\pi\) s and amplitude \(\sqrt{2^2 + 1^2} = \sqrt5 = 2.24\) m. [B1]
:::

### Long-term behaviour

The complementary function is the natural motion, the PI is the response to the push. The solution of an equation whose roots all have negative real part is therefore *transient plus steady response*.

:::plot The particle of the last example: the solution \(x = -e^{-t}(\cos 2t + \sin 2t) + 2\cos t + \sin t\) starts at \(x = 1\) and, within about 3 seconds, merges with the steady oscillation \(2\cos t + \sin t\) of amplitude \(\sqrt5\). The gap between the curves is the transient \(e^{-t}(\ldots)\), which dies away.
--f "-exp(-x)*(cos(2*x)+sin(2*x))+2*cos(x)+sin(x)" --f "2*cos(x)+sin(x)" --label "full solution x(t)" --label "steady state 2cos t + sin t" --x 0 13 --y -3 4 --xlabel t --ylabel x --legend tr
:::

:::key Long-term behaviour from the roots
- If every root of the AE has a **negative real part** (\(m < 0\), or \(p < 0\)), the complementary function tends to 0: it is a **transient**. For large \(x\) the solution behaves like the particular integral.
- If a root has a **positive real part**, the complementary function grows without bound, and the PI cannot rescue it.
- If the roots are **purely imaginary** (\(p = 0\)), the complementary function oscillates forever with constant amplitude.
:::

## A substitution: \(x = e^{t}\)

Equations such as \(ax^2y'' + bxy' + cy = f(x)\), where the power of \(x\) matches the order of the derivative, do not have constant coefficients. The substitution \(x = e^t\) (so \(t = \ln x\), for \(x > 0\)) turns them into equations that do. You must be able to derive how the derivatives change, as 9231 questions ask you to.

:::eg (Exam style) With \(x = e^{t}\), show that \(x\dfrac{dy}{dx} = \dfrac{dy}{dt}\) and \(x^2\dfrac{d^2y}{dx^2} = \dfrac{d^2y}{dt^2} - \dfrac{dy}{dt}\).
Since \(x = e^t\), \(\dfrac{dx}{dt} = e^t = x\), so \(\dfrac{dt}{dx} = \dfrac1x\). [B1]

By the chain rule:
\[\frac{dy}{dx} = \frac{dy}{dt}\frac{dt}{dx} = \frac1x\frac{dy}{dt}\] [M1]
Multiply by \(x\): \(x\dfrac{dy}{dx} = \dfrac{dy}{dt}\). [A1]

For the second derivative, differentiate \(\dfrac{dy}{dx} = \dfrac1x\dfrac{dy}{dt}\) with respect to \(x\) with the product rule. The derivative of \(\dfrac{dy}{dt}\) with respect to \(x\) needs the chain rule again:
\[\frac{d^2y}{dx^2} = -\frac{1}{x^2}\frac{dy}{dt} + \frac1x\left(\frac{d^2y}{dt^2}\cdot\frac1x\right)\] [M1]
Multiply by \(x^2\):
\[x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}\] [A1]
:::

:::key Reducing \(ax^2y'' + bxy' + cy\) with \(x = e^t\)
\[x\frac{dy}{dx} = \frac{dy}{dt} \qquad x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}\]
So \(ax^2y'' + bxy' + cy = f(x)\) becomes \(a\dfrac{d^2y}{dt^2} + (b - a)\dfrac{dy}{dt} + cy = f(e^t)\), which has constant coefficients. Solve in \(t\), then replace \(t\) by \(\ln x\) (and \(e^{t}\) by \(x\)).
:::

:::eg Use \(x = e^t\) to solve \(x^2\dfrac{d^2y}{dx^2} - 2x\dfrac{dy}{dx} + 2y = 2x^3\) for \(x > 0\).
Replace each derivative term and \(x^3 = e^{3t}\):
\[\left(\frac{d^2y}{dt^2} - \frac{dy}{dt}\right) - 2\frac{dy}{dt} + 2y = 2e^{3t} \quad\Rightarrow\quad \frac{d^2y}{dt^2} - 3\frac{dy}{dt} + 2y = 2e^{3t}\]
CF: \(m^2 - 3m + 2 = (m - 1)(m - 2) = 0\), so \(y_c = Ae^{t} + Be^{2t}\). PI: try \(y = ke^{3t}\), so \((9 - 9 + 2)k = 2\) and \(k = 1\).

\[y = Ae^{t} + Be^{2t} + e^{3t}\]
Now put \(e^t = x\):
\[y = Ax + Bx^2 + x^3\]
**Check**: \(y = x^3\) gives \(x^2(6x) - 2x(3x^2) + 2x^3 = 2x^3\), as required.
:::

:::eg (Exam style) The differential equation \(x^2\dfrac{d^2y}{dx^2} + 3x\dfrac{dy}{dx} + 5y = 10\ln x\), for \(x > 0\), is given. (a) Use the substitution \(x = e^{t}\) to show that it becomes \(\dfrac{d^2y}{dt^2} + 2\dfrac{dy}{dt} + 5y = 10t\). (b) Find the general solution for \(y\) in terms of \(x\).
**(a)** Since \(\dfrac{dt}{dx} = \dfrac1x\), the chain rule gives \(x\dfrac{dy}{dx} = \dfrac{dy}{dt}\). [B1]
Differentiating \(\dfrac{dy}{dx} = \dfrac1x\dfrac{dy}{dt}\) again with the product and chain rules:
\[\frac{d^2y}{dx^2} = -\frac{1}{x^2}\frac{dy}{dt} + \frac{1}{x^2}\frac{d^2y}{dt^2}\] [M1]
\[x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2} - \frac{dy}{dt}\] [A1]
Substitute, with \(\ln x = t\):
\[\frac{d^2y}{dt^2} - \frac{dy}{dt} + 3\frac{dy}{dt} + 5y = 10t\]
so \(\dfrac{d^2y}{dt^2} + 2\dfrac{dy}{dt} + 5y = 10t\), as required. [A1]
**(b)** AE: \(m^2 + 2m + 5 = 0\), so \(m = -1 \pm 2\mathrm{i}\). [M1]
\[y_c = e^{-t}(A\cos 2t + B\sin 2t)\] [A1]
PI: try \(y = \lambda t + \mu\), so \(2\lambda + 5\lambda t + 5\mu = 10t\). [M1]
Then \(\lambda = 2\) and \(4 + 5\mu = 0\), so \(\mu = -\tfrac45\). [A1]
\[y = e^{-t}(A\cos 2t + B\sin 2t) + 2t - \tfrac45\] [A1]
Replace \(t = \ln x\) and \(e^{-t} = \dfrac1x\):
\[y = \frac{1}{x}\left[A\cos(2\ln x) + B\sin(2\ln x)\right] + 2\ln x - \frac45\] [A1]
:::

For initial conditions in \(x\), note that \(x = 1\) corresponds to \(t = 0\), and \(x\dfrac{dy}{dx} = \dfrac{dy}{dt}\), so at \(x = 1\) the two derivatives are equal.

:::board
UK Further Maths (Edexcel 9FM0, AQA 7367, OCR H245) teaches second order linear equations with constant coefficients, complementary function and particular integral, so the methods in this chapter carry across. The 9231 substitution \(x = e^t\) is given in the question there too.
:::

:::exam What to learn, and where marks go
None of this is on MF19: learn the three cases of the complementary function, the trial forms in the table and the clash rule. In "find the particular integral" questions with a given form, the M1 is for differentiating twice and substituting, and the A1 for the coefficient. In "show that" questions every line of the substitution must be shown. When you apply conditions, differentiate the general solution (CF + PI) with the product rule and give the final answer as \(y = \ldots\). Use exact values: \(\tfrac45\), not 0.8, unless the question asks for decimals.
:::

:::eg Spot the error: Solve \(y'' + 5y' + 6y = 12\), given that \(y = 0\) and \(\dfrac{dy}{dx} = 1\) when \(x = 0\) (7 marks).
A student wrote this answer.

Line 1: AE \(m^2 + 5m + 6 = 0\), \(m = -2\) or \(-3\), so \(y_c = Ae^{-2x} + Be^{-3x}\)
Line 2: PI: try \(y = \lambda\), then \(6\lambda = 12\), so \(\lambda = 2\)
Line 3: general solution \(y = Ae^{-2x} + Be^{-3x} + 2\)
Line 4: conditions on \(y_c\): \(A + B = 0\) and \(-2A - 3B = 1\), so \(B = -1\), \(A = 1\)
Line 5: \(y = e^{-2x} - e^{-3x} + 2\)

Lines 1 to 3 are correct: the complementary function [B1], the substituted trial form [M1] giving \(\lambda = 2\) [A1], and the general solution [B1].

**Line 4 applies the conditions to the complementary function alone.** The conditions belong to the whole solution, including the PI, so the method mark is lost [M0] and the two accuracy marks with it [A0] [A0]. The student scores 4 out of 7. The answer is even wrong at the start: \(y(0) = 1 - 1 + 2 = 2\), not 0.

Correct line 4: \(y(0) = A + B + 2 = 0\), so \(A + B = -2\), and \(y'(0) = -2A - 3B = 1\). [M1]
Solving: \(B = 3\) and \(A = -5\). [A1]
Correct line 5: \(y = -5e^{-2x} + 3e^{-3x} + 2\). [A1]

**Check**: \(y(0) = -5 + 3 + 2 = 0\) and \(y'(0) = 10 - 9 = 1\).
:::

:::try Start easy, finish at exam standard
Q: Find the general solution of \(y'' - 7y' + 12y = 0\).
A: \(m^2 - 7m + 12 = (m - 3)(m - 4) = 0\), so \(y = Ae^{3x} + Be^{4x}\).
Q: Solve \(4y'' + 12y' + 9y = 0\), given that \(y = 2\) and \(\dfrac{dy}{dx} = 0\) when \(x = 0\).
A: \((2m + 3)^2 = 0\), so \(y = (A + Bx)e^{-3x/2}\). \(y(0) = 2\) gives \(A = 2\). \(\dfrac{dy}{dx} = \left[B - \tfrac32(A + Bx)\right]e^{-3x/2}\), so at \(x = 0\): \(B - 3 = 0\), \(B = 3\). Then \(y = (2 + 3x)e^{-3x/2}\).
Q: Solve \(y'' + 16y = 0\), given that \(y = 0\) and \(\dfrac{dy}{dx} = 8\) when \(x = 0\).
A: \(m = \pm 4\mathrm{i}\), so \(y = A\cos 4x + B\sin 4x\). \(y(0) = 0\) gives \(A = 0\); \(y' = 4B\cos 4x\) gives \(4B = 8\). So \(y = 2\sin 4x\).
Q: Find the general solution of \(y'' - 4y' + 3y = 3x^2 - 5x + 1\).
A: CF: \((m - 1)(m - 3) = 0\), so \(y_c = Ae^{x} + Be^{3x}\). PI: try \(y = \lambda x^2 + \mu x + \nu\). Then \(2\lambda - 4(2\lambda x + \mu) + 3(\lambda x^2 + \mu x + \nu) = 3x^2 - 5x + 1\). Compare \(x^2\): \(\lambda = 1\). Compare \(x\): \(-8 + 3\mu = -5\), so \(\mu = 1\). Compare constants: \(2 - 4 + 3\nu = 1\), so \(\nu = 1\). \(y = Ae^{x} + Be^{3x} + x^2 + x + 1\).
Q: Find the general solution of \(y'' + y' - 6y = 10e^{2x}\).
A: CF: \((m + 3)(m - 2) = 0\), so \(y_c = Ae^{2x} + Be^{-3x}\). Since 2 is a root, try \(y = kxe^{2x}\): \(y' = k(1 + 2x)e^{2x}\), \(y'' = k(4 + 4x)e^{2x}\). Then \(k[(4 + 4x) + (1 + 2x) - 6x] = 5k = 10\), so \(k = 2\). \(y = Ae^{2x} + Be^{-3x} + 2xe^{2x}\).
Q: Find the general solution of \(y'' + 4y' + 4y = 8e^{-2x}\).
A: CF: \((m + 2)^2 = 0\), \(y_c = (A + Bx)e^{-2x}\). Both \(e^{-2x}\) and \(xe^{-2x}\) are in the CF, so try \(y = kx^2e^{-2x}\). Then \(y'' + 4y' + 4y = 2ke^{-2x}\), so \(2k = 8\), \(k = 4\). \(y = (A + Bx + 4x^2)e^{-2x}\).
Q: Find a particular integral of \(y'' + 9y = 5\cos 2x + 10\sin 2x\).
A: Try \(y = \lambda\cos 2x + \mu\sin 2x\): \(y'' = -4\lambda\cos 2x - 4\mu\sin 2x\), so \(5\lambda\cos 2x + 5\mu\sin 2x = 5\cos 2x + 10\sin 2x\). \(\lambda = 1\), \(\mu = 2\), and the PI is \(\cos 2x + 2\sin 2x\).
Q: Use \(x = e^t\) to solve \(x^2\dfrac{d^2y}{dx^2} + x\dfrac{dy}{dx} - 4y = 0\) for \(x > 0\).
A: The equation becomes \(\dfrac{d^2y}{dt^2} - \dfrac{dy}{dt} + \dfrac{dy}{dt} - 4y = 0\), that is \(\dfrac{d^2y}{dt^2} - 4y = 0\). AE: \(m = \pm 2\), so \(y = Ae^{2t} + Be^{-2t} = Ax^2 + \dfrac{B}{x^2}\).
Q: Given that \(y = kx\sin 3x\) is a particular integral of \(y'' + 9y = 12\cos 3x\), find \(k\).
A: \(y' = k\sin 3x + 3kx\cos 3x\), \(y'' = 6k\cos 3x - 9kx\sin 3x\). Then \(y'' + 9y = 6k\cos 3x\), so \(6k = 12\) and \(k = 2\).
Q: Given that \(y = kx^2e^{-x}\) is a particular integral of \(y'' + 2y' + y = 6e^{-x}\), find \(k\).
A: \(y' = k(2x - x^2)e^{-x}\), \(y'' = k(2 - 4x + x^2)e^{-x}\). Then
\[y'' + 2y' + y = k\left[2 - 4x + x^2 + 4x - 2x^2 + x^2\right]e^{-x} = 2ke^{-x}\]
so \(2k = 6\) and \(k = 3\).
Q: Find the general solution of \(\dfrac{dy}{dx} + y = 4x\) using the complementary function and a particular integral.
A: AE: \(m + 1 = 0\), \(y_c = Ae^{-x}\). Try \(y = \lambda x + \mu\): \(\lambda + \lambda x + \mu = 4x\), so \(\lambda = 4\) and \(\mu = -4\). \(y = Ae^{-x} + 4x - 4\).
Q: Find the general solution of \(\dfrac{dy}{dx} - 2y = 5\sin x\).
A: \(y_c = Ae^{2x}\). Try \(y = \lambda\cos x + \mu\sin x\): \((\mu - 2\lambda)\cos x + (-\lambda - 2\mu)\sin x = 5\sin x\), so \(\mu = 2\lambda\) and \(-5\lambda = 5\). \(\lambda = -1\), \(\mu = -2\). \(y = Ae^{2x} - \cos x - 2\sin x\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find the general solution of \(y'' - 6y' + 25y = 0\).
A: AE: \(m^2 - 6m + 25 = 0\) [M1], \(m = \dfrac{6 \pm \sqrt{36 - 100}}{2} = 3 \pm 4\mathrm{i}\). [A1]
\(y = e^{3x}(A\cos 4x + B\sin 4x)\). [A1]
Q: [5 marks] ★ Find the general solution of \(y'' - 5y' + 6y = 12x - 4\).
A: AE: \((m - 2)(m - 3) = 0\) [M1], so \(y_c = Ae^{2x} + Be^{3x}\). [A1]
PI: try \(y = \lambda x + \mu\): \(-5\lambda + 6\lambda x + 6\mu = 12x - 4\) [M1], so \(\lambda = 2\) and \(\mu = 1\). [A1]
\(y = Ae^{2x} + Be^{3x} + 2x + 1\). [B1]
Q: [6 marks] ★★ The displacement of a charge satisfies \(\dfrac{dq}{dt} + 2q = 5\sin t\), with \(q = 0\) when \(t = 0\). Find \(q\) in terms of \(t\) and describe its behaviour for large \(t\).
A: CF: \(q_c = Ae^{-2t}\). [B1]
PI: try \(q = \lambda\cos t + \mu\sin t\): \((\mu + 2\lambda)\cos t + (2\mu - \lambda)\sin t = 5\sin t\). [M1]
So \(\mu = -2\lambda\) and \(-5\lambda = 5\): \(\lambda = -1\), \(\mu = 2\). [A1]
\(q = Ae^{-2t} + 2\sin t - \cos t\). At \(t = 0\), \(q = 0\): \(A - 1 = 0\) [M1], so \(q = e^{-2t} + 2\sin t - \cos t\). [A1]
As \(t \to \infty\), \(e^{-2t} \to 0\), so \(q\) oscillates as \(2\sin t - \cos t\), with amplitude \(\sqrt5\). [B1]
Q: [8 marks] ★★ (a) Given that \(y = kx\cos 2x\) is a particular integral of \(y'' + 4y = 8\sin 2x\), find \(k\). (b) Hence find the solution for which \(y = 1\) and \(\dfrac{dy}{dx} = 0\) when \(x = 0\).
A: (a) \(y' = k\cos 2x - 2kx\sin 2x\) [M1], \(y'' = -4k\sin 2x - 4kx\cos 2x\). [A1]
\(y'' + 4y = -4k\sin 2x\) [M1], so \(-4k = 8\) and \(k = -2\). [A1]
(b) \(y = A\cos 2x + B\sin 2x - 2x\cos 2x\). [B1]
\(y(0) = A = 1\). [M1]
\[y' = -2A\sin 2x + 2B\cos 2x - 2\cos 2x + 4x\sin 2x\]
so \(y'(0) = 2B - 2 = 0\) gives \(B = 1\). [M1]
\(y = \cos 2x + \sin 2x - 2x\cos 2x\). [A1]
Q: [8 marks] ★★ (a) Use the substitution \(x = e^{t}\) to show that \(x^2\dfrac{d^2y}{dx^2} + 4x\dfrac{dy}{dx} + 2y = 0\) becomes \(\dfrac{d^2y}{dt^2} + 3\dfrac{dy}{dt} + 2y = 0\). (b) Find the general solution for \(y\) in terms of \(x\). (c) Find the solution for which \(y = 2\) and \(\dfrac{dy}{dx} = -3\) when \(x = 1\).
A: (a) \(\dfrac{dy}{dx} = \dfrac1x\dfrac{dy}{dt}\) [M1], and differentiating again, \(x^2\dfrac{d^2y}{dx^2} = \dfrac{d^2y}{dt^2} - \dfrac{dy}{dt}\). [M1 A1]
Then \(\dfrac{d^2y}{dt^2} - \dfrac{dy}{dt} + 4\dfrac{dy}{dt} + 2y = 0\) gives the result. [A1]
(b) AE: \((m + 1)(m + 2) = 0\) [M1], so \(y = Ae^{-t} + Be^{-2t} = \dfrac{A}{x} + \dfrac{B}{x^2}\). [A1]
(c) \(y(1) = A + B = 2\) and \(\dfrac{dy}{dx} = -\dfrac{A}{x^2} - \dfrac{2B}{x^3}\), so \(-A - 2B = -3\) [M1]. Then \(B = 1\), \(A = 1\) and \(y = \dfrac1x + \dfrac{1}{x^2}\). [A1]
Q: [10 marks] (#math.fm.de) ★★★ The differential equation \(\dfrac{d^2y}{dx^2} + 3\dfrac{dy}{dx} + 2y = 6e^{-x}\) is given. (a) Show that, with \(v = \dfrac{dy}{dx} + y\), the equation becomes \(\dfrac{dv}{dx} + 2v = 6e^{-x}\). (b) Solve this equation for \(v\). (c) Hence find the general solution for \(y\), and state its particular integral.
H: \(\dfrac{dv}{dx} = \dfrac{d^2y}{dx^2} + \dfrac{dy}{dx}\). Add \(2v\) to it.
H: In (b) and (c) use an integrating factor each time: first \(e^{2x}\), then \(e^{x}\) for \(\dfrac{dy}{dx} + y = v\).
H: The part of your answer in \(xe^{-x}\) is the particular integral, because \(-1\) is a root of the auxiliary equation.
A: (a) \(\dfrac{dv}{dx} + 2v = \dfrac{d^2y}{dx^2} + \dfrac{dy}{dx} + 2\dfrac{dy}{dx} + 2y\) [M1]
\(= \dfrac{d^2y}{dx^2} + 3\dfrac{dy}{dx} + 2y = 6e^{-x}\). [A1]
(b) \(I = e^{2x}\). [B1]
\(\dfrac{d}{dx}(ve^{2x}) = 6e^{x}\) [M1], so \(ve^{2x} = 6e^{x} + c\) [A1], and \(v = 6e^{-x} + ce^{-2x}\). [A1]
(c) \(\dfrac{dy}{dx} + y = 6e^{-x} + ce^{-2x}\), with \(I = e^{x}\). [B1]
\(\dfrac{d}{dx}(ye^{x}) = 6 + ce^{-x}\) [M1], so \(ye^{x} = 6x - ce^{-x} + d\) [A1].
\(y = 6xe^{-x} - ce^{-2x} + de^{-x}\), with PI \(6xe^{-x}\). [A1]
Q: [10 marks] ★★★ A system satisfies \(y'' + 2ky' + 25y = 0\), where \(k \geq 0\) is the damping constant. (a) For \(k = 3\), find the general solution. (b) Find the set of values of \(k\) for which the general solution does not contain sines or cosines, and give the solution when \(k\) takes the smallest such value. (c) For that value of \(k\), find the solution with \(y = 2\) and \(y' = 0\) when \(x = 0\), and show that \(y > 0\) for all \(x \geq 0\).
H: The solution has no sines or cosines when the roots of the auxiliary equation are real.
H: At the boundary the roots are equal, so the solution has the form \((A + Bx)e^{mx}\).
H: Differentiate \((A + Bx)e^{-5x}\) with the product rule, then put in \(y = 2\), \(y' = 0\).
A: (a) AE: \(m^2 + 6m + 25 = 0\) [M1], \(m = -3 \pm 4\mathrm{i}\) [A1], \(y = e^{-3x}(A\cos 4x + B\sin 4x)\). [A1]
(b) The roots of \(m^2 + 2km + 25 = 0\) are real when \(4k^2 - 100 \geq 0\) [M1], so \(k \geq 5\). [A1]
For \(k = 5\) the root is \(m = -5\) (repeated), so \(y = (A + Bx)e^{-5x}\). [B1]
(c) \(y(0) = A = 2\). [B1]
\(y' = \left[B - 5(A + Bx)\right]e^{-5x}\), so \(y'(0) = B - 10 = 0\) and \(B = 10\). [M1]
\(y = (2 + 10x)e^{-5x}\). [A1]
Both factors are positive for \(x \geq 0\), so \(y > 0\); and \(y \to 0\) as \(x \to \infty\). [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A swing is pushed at exactly its natural frequency: \(\dfrac{d^2y}{dt^2} + 9y = 6\cos 3t\), starting at rest in the lowest position, so \(y = 0\) and \(\dfrac{dy}{dt} = 0\) when \(t = 0\). (a) Show that \(y = kt\sin 3t\) is a particular integral, and find \(k\). (b) Find \(y\) in terms of \(t\), and explain why the swing eventually leaves the range of the model.
H: The CF is \(A\cos 3t + B\sin 3t\), so \(\cos 3t\) on the right clashes with it. That is why the trial form has a factor \(t\).
H: Differentiate \(kt\sin 3t\) twice with the product rule. The \(t\sin 3t\) terms should cancel in \(y'' + 9y\).
A: (a) \(y' = k\sin 3t + 3kt\cos 3t\) [M1], \(y'' = 6k\cos 3t - 9kt\sin 3t\). [A1]
\(y'' + 9y = 6k\cos 3t\) [M1], so \(6k = 6\) and \(k = 1\). [A1]
(b) \(y = A\cos 3t + B\sin 3t + t\sin 3t\). [B1]
\(y(0) = A = 0\). \(y' = 3B\cos 3t + \sin 3t + 3t\cos 3t\), so \(y'(0) = 3B = 0\). [M1]
\(y = t\sin 3t\). [A1]
The swing's amplitude is \(t\), which grows without limit: this is **resonance**. A real swing would hit its limits (or the model of a constant frame would fail) long before.
Q: [6 marks] ★★★ (a) Show that the substitution \(x = e^t\) transforms \(x^2\dfrac{d^2y}{dx^2} - 3x\dfrac{dy}{dx} + 4y = 0\) into \(\dfrac{d^2y}{dt^2} - 4\dfrac{dy}{dt} + 4y = 0\). (b) Hence show that the general solution is \(y = x^2(A + B\ln x)\).
H: Use \(x\dfrac{dy}{dx} = \dfrac{dy}{dt}\) and \(x^2\dfrac{d^2y}{dx^2} = \dfrac{d^2y}{dt^2} - \dfrac{dy}{dt}\), derived as above.
H: The auxiliary equation of the new equation has a repeated root; then change back with \(e^{2t} = x^2\) and \(t = \ln x\).
A: (a) \(\left(\dfrac{d^2y}{dt^2} - \dfrac{dy}{dt}\right) - 3\dfrac{dy}{dt} + 4y = 0\) [M1 A1], which simplifies to \(\dfrac{d^2y}{dt^2} - 4\dfrac{dy}{dt} + 4y = 0\). [A1]
(b) AE: \((m - 2)^2 = 0\) [M1], so \(y = (A + Bt)e^{2t}\). [A1]
With \(e^{2t} = x^2\) and \(t = \ln x\), \(y = x^2(A + B\ln x)\). [A1]
:::

:::quiz
? The auxiliary equation of \(y'' + 4y' + 13y = 0\) has roots \(-2 \pm 3\mathrm{i}\). What is the complementary function?
+ \(e^{-2x}(A\cos 3x + B\sin 3x)\)
- \(e^{3x}(A\cos 2x + B\sin 2x)\)
- \((A + Bx)e^{-2x}\)
- \(Ae^{-2x} + Be^{3x}\)
> With roots \(p \pm q\mathrm{i}\) the exponential factor uses \(p\) (the real part, \(-2\)) and the cosines use \(q\) (the imaginary part, 3). The second option swaps them, the third is for a repeated root, and the fourth is for two real roots.
? Which trial form finds a particular integral of \(y'' + y' - 6y = 5e^{2x}\)?
+ \(kxe^{2x}\)
- \(ke^{2x}\)
- \(kx^2e^{2x}\)
- \(ke^{-2x}\)
> The roots of \(m^2 + m - 6 = 0\) are 2 and \(-3\), so \(e^{2x}\) is in the complementary function and \(ke^{2x}\) would give 0. Multiply by \(x\); \(x^2\) is only needed for a repeated root.
? What is the correct trial form for a particular integral when \(f(x) = 3\sin 2x\)?
+ \(\lambda\cos 2x + \mu\sin 2x\)
- \(\lambda\sin 2x\)
- \(\lambda\cos 2x\)
- \(\lambda x\sin 2x\)
> Differentiating \(\sin 2x\) produces \(\cos 2x\), so both terms are needed. A single term leaves a mismatch; the factor \(x\) is only for a clash with the complementary function.
? A student must find the solution with \(y = 1\) and \(y' = 0\) at \(x = 0\). When should the two conditions be used?
+ After adding the particular integral to the complementary function
- On the complementary function, before the particular integral is found
- On the particular integral only
- Never: the general solution already fits any conditions
> The conditions belong to the whole general solution, CF + PI. Using them on the CF alone gives wrong constants, because the PI also contributes to \(y(0)\) and \(y'(0)\).
? The roots of an auxiliary equation are \(-1 \pm 2\mathrm{i}\). What does the complementary function do as \(x\) increases?
+ Oscillates, with the amplitude shrinking towards 0
- Oscillates, with the amplitude growing
- Oscillates with constant amplitude
- Decays to 0 without oscillating
> The factor \(e^{-x}\) shrinks while \(\cos 2x\) and \(\sin 2x\) keep oscillating. A real part of 0 would give constant amplitude, and no imaginary part would give no oscillation.
? With \(x = e^t\), what is \(x^2\dfrac{d^2y}{dx^2}\) in terms of \(t\)?
+ \(\dfrac{d^2y}{dt^2} - \dfrac{dy}{dt}\)
- \(\dfrac{d^2y}{dt^2}\)
- \(\dfrac{d^2y}{dt^2} + \dfrac{dy}{dt}\)
- \(\dfrac1x\dfrac{d^2y}{dt^2}\)
> The product rule on \(\dfrac1x\dfrac{dy}{dt}\) gives an extra term \(-\dfrac{1}{x^2}\dfrac{dy}{dt}\), so after multiplying by \(x^2\) there is a minus \(\dfrac{dy}{dt}\). Forgetting this term is the most common slip.
:::

:::checklist What you can now do
- [ ] I can state what the complementary function and particular integral are, and that the general solution is their sum.
- [ ] I can find the complementary function of a first or second order linear equation with constant coefficients when the auxiliary roots are distinct, repeated or complex.
- [ ] I can find a particular integral for a polynomial, an exponential or a \(\cos px\) and \(\sin px\) right-hand side, including the factor \(x\) when it clashes with the CF.
- [ ] I can find the coefficient in a given particular integral, such as \(kx\cos 2x\) for \(y'' + 4y = \sin 2x\).
- [ ] I can use the substitution \(x = e^t\) to reduce \(ax^2y'' + bxy' + cy = f(x)\) to a constant-coefficient equation, derive the new derivatives, and solve.
- [ ] I can use initial conditions on \(y\) and \(\dfrac{dy}{dx}\) to find a particular solution from the full general solution.
- [ ] I can interpret a solution as a damped or forced oscillation, naming the transient and the long-term behaviour from the roots.
:::

:::recap
- \(ay'' + by' + cy = f(x)\): general solution \(=\) CF \(+\) PI. The CF has two arbitrary constants.
- AE \(am^2 + bm + c = 0\): distinct real \(\to Ae^{m_1x} + Be^{m_2x}\); repeated \(\to (A + Bx)e^{mx}\); complex \(p \pm q\mathrm{i} \to e^{px}(A\cos qx + B\sin qx)\).
- PI trial forms: polynomial of the same degree (all powers); \(\lambda e^{bx}\); \(\lambda\cos px + \mu\sin px\) (both terms). If the form is in the CF, multiply by \(x\) (or \(x^2\) for a repeated root).
- Resonance: forcing at the natural frequency gives a PI such as \(kx\cos 2x\) whose amplitude grows.
- Initial conditions apply to the whole general solution: add the PI, differentiate, then use both conditions.
- \(x = e^t\): \(x\dfrac{dy}{dx} = \dfrac{dy}{dt}\) and \(x^2\dfrac{d^2y}{dx^2} = \dfrac{d^2y}{dt^2} - \dfrac{dy}{dt}\). Solve in \(t\), then \(t = \ln x\).
- Long term: roots with negative real part give a transient that dies away; the solution then follows the PI.
:::

:::links
- watch: [Second order DEs equal to zero](https://www.examsolutions.net/tutorials/how-to-solve-second-order-linear-differential-equations-that-equal-zero/) · ExamSolutions · the three cases of the auxiliary equation worked through
- watch: [Euler's formula with introductory group theory](https://www.3blue1brown.com/lessons/eulers-formula-dynamically) · 3Blue1Brown · why complex roots give cosines and sines
- read: [Second order equations](https://tutorial.math.lamar.edu/Classes/DE/IntroSecondOrder.aspx) · Paul's Online Notes · the same auxiliary-equation method with more examples
- practise: [Differential equations](https://www.khanacademy.org/math/differential-equations) · Khan Academy · second order linear exercises with feedback
- explore: [Masses and springs](https://phet.colorado.edu/en/simulations/masses-and-springs) · PhET · see damping and oscillation on a real spring
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions on differential equations with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Projectiles](#math.fm.projectiles) opens Further Mechanics: the path of a particle under gravity, found from its horizontal and vertical motion.
