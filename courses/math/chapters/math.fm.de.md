@chapter math.fm.de
@title First order differential equations
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 5–6 hours
@summary Many first order differential equations cannot be solved by separating the variables, but a linear one can always be solved with an integrating factor. You will learn that method, spot equations that are already a product derivative, use a given substitution (such as \(y = ux\) or \(z = 1/y\)) to turn an equation into a solvable one, fit initial conditions, and read the solution in a real context such as a mixing tank or a cooling body.

:::why
Rates of change are everywhere: salt flowing into a tank, a drug leaving the blood, a cup of tea cooling in a room whose temperature is itself changing. When the rate depends on both the quantity and the time, the variables cannot be separated, yet the equation is still solvable. The integrating factor is the tool that does it, and the same idea of "make the left side one derivative" returns in the next chapter for second order equations.
:::

**Before you start**, you need separation of variables and initial conditions from [Differential equations](#math.p3.diffeq), integration by parts from [Integration techniques](#math.p3.inttech), and \(e^{\ln x}\) from [Logarithms and exponentials](#math.p3.logs). One example uses \(\sinh x\), \(\cosh x\) and \(\tanh x\) from [Hyperbolic functions](#math.fm.hyperbolic).

:::try Warm-up
Q: Find the general solution of \(\dfrac{dy}{dx} = \dfrac{y}{x}\) for \(x, y > 0\). (from [Differential equations](#math.p3.diffeq))
A: Separate: \(\displaystyle\int \frac{1}{y}\,dy = \int \frac{1}{x}\,dx\), so \(\ln y = \ln x + c\), and \(y = Ax\) with \(A = e^{c}\).
Q: Find \(\displaystyle\int xe^{-2x}\,dx\). (from [Integration techniques](#math.p3.inttech))
A: By parts with \(u = x\): \(-\tfrac12xe^{-2x} + \tfrac12\displaystyle\int e^{-2x}\,dx = -\tfrac12xe^{-2x} - \tfrac14e^{-2x} + c\).
Q: Simplify \(e^{-4\ln x}\) for \(x > 0\). (from [Logarithms and exponentials](#math.p3.logs))
A: \(e^{-4\ln x} = e^{\ln x^{-4}} = x^{-4}\).
:::

## Linear equations and the integrating factor

In [Differential equations](#math.p3.diffeq) you separated the variables. That works only when the equation splits into "something with \(y\)" times "something with \(x\)". Look at
\[\frac{dy}{dx} - 2y = x\]
You cannot get all the \(y\) terms on one side and all the \(x\) terms on the other, so separation fails. But there is another way in. Multiply the equation by \(e^{-2x}\):
\[e^{-2x}\frac{dy}{dx} - 2e^{-2x}y = xe^{-2x}\]
The left side is exactly the product-rule derivative of \(ye^{-2x}\), because \(\dfrac{d}{dx}\left(ye^{-2x}\right) = e^{-2x}\dfrac{dy}{dx} - 2e^{-2x}y\). So the equation says \(\dfrac{d}{dx}\left(ye^{-2x}\right) = xe^{-2x}\), and one integration finishes the job. The factor \(e^{-2x}\) is the **integrating factor**: it turns the left side into a single derivative.

:::def First order linear differential equation
A differential equation that can be written \(\dfrac{dy}{dx} + P(x)\,y = Q(x)\), where \(P\) and \(Q\) are functions of \(x\) only (or constants). "Linear" means \(y\) and \(\dfrac{dy}{dx}\) appear only to the first power and are never multiplied together.
:::

:::def Integrating factor
For \(\dfrac{dy}{dx} + P(x)\,y = Q(x)\), the integrating factor is \(e^{\int P\,dx}\). Multiplying the equation by it makes the left side the derivative of (integrating factor) \(\times\, y\).
:::

:::def General solution and particular solution
The **general solution** of a first order equation has one arbitrary constant and describes a whole family of curves. A **particular solution** is the one curve of the family that fits a given condition, such as "\(y = 3\) when \(x = 0\)" (an **initial condition**).
:::

:::key Solving \(\dfrac{dy}{dx} + P(x)y = Q(x)\)
:::steps
1. Write the equation in **standard form** \(\dfrac{dy}{dx} + Py = Q\): divide every term by the coefficient of \(\dfrac{dy}{dx}\) first.
2. Integrating factor \(I = e^{\int P\,dx}\). No constant is needed in \(\int P\,dx\). Simplify \(e^{\ln\cdots}\).
3. Multiply through: \(\dfrac{d}{dx}(Iy) = IQ\).
4. Integrate both sides: \(Iy = \displaystyle\int IQ\,dx + c\). The constant \(c\) goes in now.
5. Divide by \(I\) to give \(y\) in terms of \(x\).
:::
:::

:::proof Why the integrating factor works
Let \(I = e^{\int P\,dx}\).
- By the chain rule, \(\dfrac{dI}{dx} = P \cdot e^{\int P\,dx} = PI\), because the derivative of \(\int P\,dx\) is \(P\).
- Multiply the standard form by \(I\): \(I\dfrac{dy}{dx} + PIy = IQ\).
- Replace \(PI\) by \(\dfrac{dI}{dx}\): the left side is \(I\dfrac{dy}{dx} + \dfrac{dI}{dx}y\).
- That is the product rule for \(\dfrac{d}{dx}(Iy)\), so \(\dfrac{d}{dx}(Iy) = IQ\).
- A different constant in \(\int P\,dx\) multiplies \(I\) by a positive constant, which multiplies both sides of the equation by that constant and changes nothing. That is why you may leave the constant out.
:::

:::eg Find the general solution of \(\dfrac{dy}{dx} - 2y = x\).
The equation is already in standard form with \(P = -2\) and \(Q = x\).
\[I = e^{\int -2\,dx} = e^{-2x}\]
Multiply through:
\[\frac{d}{dx}\left(ye^{-2x}\right) = xe^{-2x}\]
Integrate the right side by parts with \(u = x\) and \(dv = e^{-2x}\,dx\):
\[\begin{aligned}
ye^{-2x} &= -\tfrac12xe^{-2x} + \tfrac12\int e^{-2x}\,dx \\
&= -\tfrac12xe^{-2x} - \tfrac14e^{-2x} + c
\end{aligned}\]
Divide by \(e^{-2x}\):
\[y = -\tfrac12x - \tfrac14 + ce^{2x}\]
**Check**: \(\dfrac{dy}{dx} = -\tfrac12 + 2ce^{2x}\), so \(\dfrac{dy}{dx} - 2y = -\tfrac12 + x + \tfrac12 = x\). The \(c\) terms cancel, as they must.
:::

The solution is a family of curves, one for each \(c\). The picture below is a **slope field**. At each point \((x, y)\) a short line segment is drawn with gradient \(\dfrac{dy}{dx}\), here \(2y + x\), so the segments show which way a solution would be heading at that point; a solution curve is a curve that follows the segments. In the field below the equation is \(\dfrac{dy}{dx} = 2y + x\), and clicking sets a starting point from which the curve is drawn. The starting point \((-1, 0.25)\) lies on the line \(y = -\tfrac12x - \tfrac14\) (the member with \(c = 0\)), and the curve drawn through it is that straight line. Click above and below that line to start other curves: every other member of the family runs away exponentially, upwards for \(c > 0\) and downwards for \(c < 0\).

:::html
<div class="widget" data-w="slopefield" data-f="2*y+x" data-x="-3,3" data-y="-4,4" data-start="-1,0.25"></div>
:::

:::eg Find the general solution of \(x\dfrac{dy}{dx} - 4y = x\) for \(x > 0\).
The coefficient of \(\dfrac{dy}{dx}\) is \(x\), so divide every term by \(x\) first:
\[\frac{dy}{dx} - \frac{4}{x}y = 1\]
Now \(P = -\dfrac{4}{x}\):
\[I = e^{\int -4/x\,dx} = e^{-4\ln x} = e^{\ln x^{-4}} = x^{-4}\]
Multiply through and integrate:
\[\begin{aligned}
\frac{d}{dx}\left(x^{-4}y\right) &= x^{-4} \\
x^{-4}y &= -\tfrac13x^{-3} + c \\
y &= -\tfrac13x + cx^4
\end{aligned}\]
**Check**: \(x\dfrac{dy}{dx} - 4y = x\left(-\tfrac13 + 4cx^3\right) - 4\left(-\tfrac13x + cx^4\right) = -\tfrac13x + \tfrac43x = x\).
:::

:::warn Divide first, and watch the logarithm
Divide by the coefficient of \(\dfrac{dy}{dx}\) before you read off \(P\). In \(x\dfrac{dy}{dx} - 4y = x\) the \(P\) is \(-\dfrac4x\), not \(-4\), and the right side becomes \(1\), not \(x\). Next, \(\int \dfrac{1}{x}\,dx = \ln|x|\), so the integrating factor is really \(|x|^{-4}\). Any constant multiple of an integrating factor works (multiplying the whole equation by \(-1\) changes nothing), so take \(x > 0\), as questions state, or drop the modulus signs. Finally, add \(+c\) at the integration step, before you divide by \(I\), or the term \(cx^4\) comes out wrong.
:::

:::eg Find the general solution of \(\coth x\dfrac{dy}{dx} + y = \cosh x\) for \(x > 0\).
Divide by \(\coth x\). Since \(\dfrac{1}{\coth x} = \tanh x\), the standard form is
\[\frac{dy}{dx} + (\tanh x)\,y = \cosh x\tanh x = \sinh x\]
The integrating factor needs \(\int \tanh x\,dx = \int \dfrac{\sinh x}{\cosh x}\,dx = \ln\cosh x\) (the top is the derivative of the bottom):
\[I = e^{\ln\cosh x} = \cosh x\]
Multiply through and integrate:
\[\begin{aligned}
\frac{d}{dx}\left(y\cosh x\right) &= \sinh x\cosh x \\
y\cosh x &= \tfrac12\sinh^2 x + c \\
y &= \frac{\tfrac12\sinh^2x + c}{\cosh x}
\end{aligned}\]
The step \(\int \sinh x\cosh x\,dx = \tfrac12\sinh^2x\) is the reverse chain rule, using \(\dfrac{d}{dx}\sinh x = \cosh x\) from [Hyperbolic functions](#math.fm.hyperbolic).
:::

:::eg Solve \(\sin x\dfrac{dy}{dx} + 2y\cos x = 1\) for \(0 < x < \pi\), given that \(y = 2\) when \(x = \tfrac{\pi}{2}\).
Divide by \(\sin x\), the coefficient of \(\dfrac{dy}{dx}\):
\[\frac{dy}{dx} + 2\cot x\,y = \frac{1}{\sin x}\]
\(\displaystyle\int 2\cot x\,dx = 2\ln\sin x\) (the top of \(\cot x = \dfrac{\cos x}{\sin x}\) is the derivative of the bottom), so
\[I = e^{2\ln\sin x} = \sin^2x\]
Multiply through and integrate:
\[\begin{aligned}
\frac{d}{dx}\left(y\sin^2x\right) &= \sin^2x \cdot \frac{1}{\sin x} = \sin x \\
y\sin^2x &= -\cos x + c
\end{aligned}\]
At \(x = \tfrac\pi2\), \(\sin x = 1\) and \(\cos x = 0\), so \(2 = c\):
\[y = \frac{2 - \cos x}{\sin^2x}\]
Notice that the original left side was already \(\dfrac{d}{dx}\left(y\sin^2x\right)\) divided by \(\sin x\): the integrating factor found the hidden product for you.
:::

When \(P\) is a polynomial, \(\int P\,dx\) is a polynomial and the integrating factor is an exponential of it.

:::eg Find the general solution of \(\dfrac{dy}{dx} + 2xy = 4x\), and say what happens to \(y\) as \(x \to \pm\infty\).
\(P = 2x\), so \(I = e^{\int 2x\,dx} = e^{x^2}\). Multiply through:
\[\begin{aligned}
\frac{d}{dx}\left(ye^{x^2}\right) &= 4xe^{x^2} \\
ye^{x^2} &= 2e^{x^2} + c \\
y &= 2 + ce^{-x^2}
\end{aligned}\]
The integral \(\int 4xe^{x^2}\,dx\) is a reverse chain rule: the factor \(2x\) is the derivative of the power. Because \(e^{-x^2} \to 0\) in both directions, every solution tends to \(y = 2\) as \(x \to \pm\infty\). The line \(y = 2\) is itself a solution (take \(c = 0\)).
:::

## Equations that are already a product derivative

Sometimes the left side is a product derivative before you do anything. Then \(I = 1\) in disguise and you can integrate straight away. The patterns to spot:
\[\begin{aligned}
x\frac{dy}{dx} + y &= \frac{d}{dx}(xy) \\
\cos x\frac{dy}{dx} - y\sin x &= \frac{d}{dx}(y\cos x) \\
x^2\frac{dy}{dx} + 2xy &= \frac{d}{dx}(x^2y)
\end{aligned}\]

:::eg Solve (a) \(x\dfrac{dy}{dx} + y = 6x^2\) and (b) \(\cos x\dfrac{dy}{dx} - y\sin x = 2x\), for \(x > 0\) and \(-\tfrac{\pi}{2} < x < \tfrac{\pi}{2}\) respectively.
(a) The left side is \(\dfrac{d}{dx}(xy)\):
\[xy = \int 6x^2\,dx = 2x^3 + c, \qquad y = 2x^2 + \frac{c}{x}\]
(b) The left side is \(\dfrac{d}{dx}(y\cos x)\):
\[y\cos x = x^2 + c, \qquad y = (x^2 + c)\sec x\]
If you meet one of these and prefer the standard method, it gives the same answer: in (a) dividing by \(x\) gives \(P = \dfrac1x\) and \(I = x\), which is the factor already sitting there.
:::

## Fitting initial conditions

The general solution has one constant, so one condition fixes it. Substitute the pair of values into the **whole** solution (after the constant is in, not before) and solve for \(c\).

For \(\dfrac{dy}{dx} - 2y = x\) with \(y = 1\) when \(x = 0\): \(1 = -\tfrac14 + c\), so \(c = \tfrac54\) and the particular solution is \(y = -\tfrac12x - \tfrac14 + \tfrac54e^{2x}\).

Exam questions at this level are long and chain the skills: put into standard form, find the integrating factor, integrate by parts, fit the condition, then say what happens for large \(x\).

:::eg (Exam style) The differential equation \(x\dfrac{dy}{dx} + 2y = xe^{-x}\) is to be solved for \(x > 0\). (a) Show that an integrating factor is \(x^2\). (b) Find the solution for which \(y = 0\) when \(x = 1\). (c) Describe the behaviour of \(y\) as \(x \to \infty\).
**(a)** Divide by \(x\) to reach standard form:
\[\frac{dy}{dx} + \frac{2}{x}y = e^{-x}\] [B1]
\[I = e^{\int 2/x\,dx} = e^{2\ln x}\] [M1]
\[= e^{\ln x^2} = x^2\] [A1]
**(b)** Multiply by \(I\):
\[\frac{d}{dx}\left(x^2y\right) = x^2e^{-x}\] [M1]
Integrate by parts, taking \(u = x^2\), then again with \(u = 2x\):
\[\begin{aligned}
\int x^2e^{-x}\,dx &= -x^2e^{-x} + \int 2xe^{-x}\,dx \\
&= -x^2e^{-x} - 2xe^{-x} - 2e^{-x} + c
\end{aligned}\] [M1 A1]
So \(x^2y = -e^{-x}(x^2 + 2x + 2) + c\). Put \(x = 1\), \(y = 0\):
\[0 = -5e^{-1} + c, \qquad c = 5e^{-1}\] [M1 A1]
\[y = \frac{5e^{-1} - e^{-x}(x^2 + 2x + 2)}{x^2}\] [A1]
**(c)** As \(x \to \infty\), \(e^{-x}(x^2 + 2x + 2) \to 0\), so the numerator tends to \(5e^{-1}\) and \(y \approx \dfrac{5}{ex^2} \to 0\). [B1]
:::

## Substitutions

Some equations are not linear or separable as they stand, but become one after a change of variable. At this level **the substitution is given**: the question says "use the substitution \(y = ux\)" or "use \(z = \dfrac1y\)". Your job is to carry it out without slips: differentiate the new variable, replace every \(y\) and \(\dfrac{dy}{dx}\), simplify, solve, then put the original variable back.

### Homogeneous equations: \(y = ux\)

:::def Homogeneous first order equation
An equation that can be written \(\dfrac{dy}{dx} = f\!\left(\dfrac{y}{x}\right)\): the right side depends on \(x\) and \(y\) only through the ratio \(\dfrac yx\). For example \(\dfrac{x + y}{x - y}\) (divide top and bottom by \(x\)) is of this kind.
:::

Put \(y = ux\), where \(u\) is a new unknown function of \(x\). The product rule gives
\[\frac{dy}{dx} = u + x\frac{du}{dx}\]
Substitute, and the \(x\)'s disappear from the right side, leaving a separable equation in \(u\) and \(x\).

:::eg Use the substitution \(y = ux\) to find the general solution of \(\dfrac{dy}{dx} = \dfrac{x + y}{x - y}\) for \(x > 0\).
With \(y = ux\) the right side is \(\dfrac{x + ux}{x - ux} = \dfrac{1 + u}{1 - u}\). So
\[\begin{aligned}
u + x\frac{du}{dx} &= \frac{1 + u}{1 - u} \\
x\frac{du}{dx} &= \frac{1 + u}{1 - u} - u = \frac{1 + u - u + u^2}{1 - u} = \frac{1 + u^2}{1 - u}
\end{aligned}\]
Separate the variables and integrate:
\[\int \frac{1 - u}{1 + u^2}\,du = \int \frac{1}{x}\,dx\]
\[\tan^{-1}u - \tfrac12\ln(1 + u^2) = \ln x + c\]
Replace \(u\) by \(\dfrac yx\) and use \(\ln x + \tfrac12\ln\!\left(1 + \dfrac{y^2}{x^2}\right) = \tfrac12\ln(x^2 + y^2)\):
\[\tan^{-1}\!\frac{y}{x} = \tfrac12\ln(x^2 + y^2) + c\]
**Check** by implicit differentiation: the left side gives \(\dfrac{x\,y' - y}{x^2 + y^2}\), the right gives \(\dfrac{x + yy'}{x^2 + y^2}\). Equating, \(xy' - y = x + yy'\), so \(y'(x - y) = x + y\).
:::

In polar form that answer reads \(\theta = \ln r + c\), that is \(r = Ae^{\theta}\): the curves are logarithmic spirals (see [Polar coordinates](#math.fm.polar)). The substitution did not just solve the equation; it found the natural coordinates for it.

:::eg (Exam style) The differential equation \(\dfrac{dy}{dx} = \dfrac{x^2 + y^2}{xy}\) is to be solved for \(x > 0\), \(y > 0\). (a) Use the substitution \(y = ux\) to show that \(x\dfrac{du}{dx} = \dfrac1u\). (b) Find \(y\) in terms of \(x\), given that \(y = 2\) when \(x = 1\). (c) State the set of values of \(x\) for which your solution is defined.
**(a)** With \(y = ux\):
\[\frac{dy}{dx} = u + x\frac{du}{dx}\] [B1]
\[u + x\frac{du}{dx} = \frac{x^2 + u^2x^2}{x \cdot ux} = \frac{1 + u^2}{u}\] [M1]
\[x\frac{du}{dx} = \frac{1 + u^2}{u} - u\] [M1]
\[= \frac{1}{u}\] [A1]
**(b)** Separate and integrate:
\[\int u\,du = \int \frac1x\,dx \quad\Rightarrow\quad \tfrac12u^2 = \ln x + c\] [M1 A1]
When \(x = 1\), \(y = 2\), so \(u = 2\): \(2 = 0 + c\), \(c = 2\). [M1]
\[u^2 = 2\ln x + 4, \qquad y = x\sqrt{2\ln x + 4}\] [A1]
(positive root, since \(y > 0\)).
**(c)** The square root needs \(2\ln x + 4 > 0\) [M1], so \(\ln x > -2\) and \(x > e^{-2}\). [A1]
:::

### Reducing to a linear equation: \(z = \dfrac1y\)

When the equation has a term in \(y^2\) or \(y^3\) it is not linear, but a substitution such as \(z = \dfrac1y\) can make it linear in \(z\). The new derivative comes from the chain rule: if \(z = y^{-1}\) then \(\dfrac{dz}{dx} = -y^{-2}\dfrac{dy}{dx}\). Replace \(\dfrac{dy}{dx}\) using the original equation, simplify, and every \(y\) should reappear as \(z\).

:::eg (Exam style) The differential equation \(\dfrac{dy}{dx} + \dfrac{y}{x} = xy^2\) is to be solved for \(0 < x < 3\) and \(y > 0\). (a) Use the substitution \(z = \dfrac1y\) to show that \(\dfrac{dz}{dx} - \dfrac{z}{x} = -x\). (b) Find the general solution for \(z\) in terms of \(x\). (c) Given that \(y = \tfrac12\) when \(x = 1\), find \(y\) in terms of \(x\).
**(a)** \(z = y^{-1}\), so by the chain rule
\[\frac{dz}{dx} = -y^{-2}\frac{dy}{dx}\] [M1]
From the equation, \(\dfrac{dy}{dx} = xy^2 - \dfrac yx\). Substitute:
\[\frac{dz}{dx} = -y^{-2}\left(xy^2 - \frac yx\right)\] [M1]
\[= -x + \frac{1}{xy} = -x + \frac{z}{x}\] [A1]
Rearranging, \(\dfrac{dz}{dx} - \dfrac zx = -x\), as required.
**(b)** The equation is linear in \(z\) with \(P = -\dfrac1x\):
\[I = e^{-\ln x} = \frac1x\] [B1]
\[\frac{d}{dx}\left(\frac zx\right) = -1\] [M1]
\[\frac zx = -x + c \quad\Rightarrow\quad z = cx - x^2\] [A1 A1]
**(c)** When \(x = 1\), \(y = \tfrac12\), so \(z = 2\): \(2 = c - 1\), \(c = 3\). [M1 A1]
\[y = \frac1z = \frac{1}{3x - x^2}\] [A1]
Since \(y > 0\) needs \(3x - x^2 > 0\), the solution holds for \(0 < x < 3\) and \(y\) grows without bound as \(x \to 3\).
:::

## Modelling with first order equations

A differential equation models a situation by stating a rate. To use it you must do three things: **build** the equation from the words, **solve** it, and **interpret** the answer, which includes what happens in the long run.

**Mixing problems.** The rate of change of the amount of a substance is "rate in minus rate out". The rate out is the concentration (amount divided by volume) times the flow rate. If the volume changes with time, the equation is linear with a variable coefficient, which is where the integrating factor earns its keep.

:::eg (Exam style) A tank contains 100 litres of water in which 5 kg of salt is dissolved. Brine containing 0.2 kg of salt per litre flows into the tank at 6 litres per minute. The mixture is kept uniform and flows out at 4 litres per minute. Let \(x\) kg be the mass of salt in the tank after \(t\) minutes. (a) Show that \(\dfrac{dx}{dt} + \dfrac{2x}{50 + t} = 1.2\). (b) Find \(x\) in terms of \(t\). (c) Find the mass of salt in the tank when \(t = 50\).
**(a)** Salt enters at \(6 \times 0.2 = 1.2\) kg per minute. [B1]
The volume is \(100 + 2t\) litres (it gains 2 litres each minute), so the concentration is \(\dfrac{x}{100 + 2t}\) kg per litre and salt leaves at
\[4 \times \frac{x}{100 + 2t} = \frac{2x}{50 + t}\] [B1]
\[\frac{dx}{dt} = 1.2 - \frac{2x}{50 + t} \quad\Rightarrow\quad \frac{dx}{dt} + \frac{2x}{50 + t} = 1.2\] [A1]
**(b)** \(P = \dfrac{2}{50 + t}\), so
\[I = e^{2\ln(50 + t)} = (50 + t)^2\] [M1 A1]
\[\frac{d}{dt}\left[(50 + t)^2x\right] = 1.2(50 + t)^2\] [M1]
\[(50 + t)^2x = 0.4(50 + t)^3 + c\] [A1]
When \(t = 0\), \(x = 5\): \(5 \times 2500 = 0.4 \times 125\,000 + c\), so \(c = -37\,500\). [M1]
\[x = 0.4(50 + t) - \frac{37\,500}{(50 + t)^2}\] [A1]
**(c)** When \(t = 50\): \(x = 0.4 \times 100 - \dfrac{37\,500}{10\,000} = 36.25\) kg. [B1]

**Interpretation**: the volume is then 200 litres, so the concentration is \(\dfrac{36.25}{200} = 0.181\) kg per litre (3 s.f.). As \(t\) grows the second term of \(x\) dies away, leaving \(x \approx 0.4(50 + t)\). That equals \(0.2(100 + 2t) = 0.2V\), where \(V\) is the volume, so the concentration in the tank tends to the concentration of the incoming brine, 0.2 kg per litre.
:::

**Heating and cooling.** Newton's law of cooling says an object's temperature \(\theta\) changes at a rate proportional to the difference between \(\theta\) and the surroundings: \(\dfrac{d\theta}{dt} = -k(\theta - A)\). If the surrounding temperature \(A\) is itself changing, the equation is linear with a right side that depends on \(t\).

:::eg A metal block at 80 °C is placed in a room whose temperature, in °C, is \(10 + 0.5t\) after \(t\) minutes, because the heating is on. The block cools according to \(\dfrac{d\theta}{dt} = -0.1\left(\theta - 10 - 0.5t\right)\). Find \(\theta\) in terms of \(t\) and describe the long-term behaviour.
Rearrange into standard form:
\[\frac{d\theta}{dt} + 0.1\theta = 1 + 0.05t\]
\[I = e^{0.1t}\]
\[\frac{d}{dt}\left(\theta e^{0.1t}\right) = (1 + 0.05t)e^{0.1t}\]
By parts, \(\displaystyle\int 0.05te^{0.1t}\,dt = 0.5te^{0.1t} - 5e^{0.1t}\) and \(\displaystyle\int e^{0.1t}\,dt = 10e^{0.1t}\), so
\[\theta e^{0.1t} = e^{0.1t}(5 + 0.5t) + c\]
\[\theta = 5 + 0.5t + ce^{-0.1t}\]
At \(t = 0\), \(\theta = 80\): \(c = 75\), so \(\theta = 5 + 0.5t + 75e^{-0.1t}\).

The term \(75e^{-0.1t}\) is the **transient**: it dies away. What is left, \(5 + 0.5t\), is the **steady behaviour**: the block warms at the same rate as the room (0.5 °C per minute) but stays 5 °C **below** it, trailing the room temperature, as a real object with thermal inertia does.
:::

:::plot The block's temperature \(\theta = 5 + 0.5t + 75e^{-0.1t}\) falls from 80 °C and settles into a line parallel to the room temperature \(10 + 0.5t\), 5 °C below it.
--f "5+0.5*x+75*exp(-0.1*x)" --f "10+0.5*x" --label "block θ" --label "room" --x 0 60 --y 0 110 --xlabel "t (min)" --ylabel "°C" --legend tr
:::

**Long-term behaviour.** Many solutions have the shape *transient + steady part*. For a linear equation with \(P\) a positive constant, the integrating factor \(e^{Pt}\) makes the complementary term \(ce^{-Pt}\) die away, and the particular part is what remains. Whenever a question asks "what happens as \(t \to \infty\)?", look for the terms that tend to 0 and describe what is left.

## Choosing a method

Faced with a first order equation, ask these questions in order. The 9231 papers tell you the substitution when one is needed, so for most questions the choice is between the first three.

| If the equation… | …then use |
|---|---|
| separates into \(g(y)\,dy = f(x)\,dx\) | separation of variables ([Differential equations](#math.p3.diffeq)) |
| has a left side that is already \(\dfrac{d}{dx}(\text{product})\) | integrate directly |
| is linear, \(\dfrac{dy}{dx} + Py = Q\) | integrating factor |
| has a right side that depends only on \(\dfrac yx\) | \(y = ux\) |
| has a power of \(y\) in a term, with a substitution given | the substitution, then one of the methods above |

A useful test for "linear": \(y\) and \(\dfrac{dy}{dx}\) appear only to the first power, and nothing multiplies them together. In \(\dfrac{dy}{dx} + \dfrac{y}{x} = xy^2\) the \(y^2\) breaks that rule, which is why the question supplies \(z = \dfrac1y\). An equation can be both linear and separable (\(\dfrac{dy}{dx} + 2y = 6\) is), and then either method works: use the quicker one, but remember the integrating factor never fails on a linear equation.

:::board
UK Further Maths (Edexcel 9FM0, AQA 7367, OCR H245) teaches integrating factors and second order linear equations with constant coefficients, so the methods in this chapter and the next carry across. Where a substitution is needed, UK papers also give it in the question.
:::

:::exam What to learn, and where marks go
The integrating factor method is **not** on MF19: learn the five steps, and learn that you must divide by the coefficient of \(\dfrac{dy}{dx}\) first. Marks are usually B1 for the standard form or the integrating factor, M1 for "integrating factor times the right side", A1 for the integral, M1 for using the condition and A1 for the final expression. When a question says "show that", every line must be visible, because the final answer is given and the marks are for the working. Give the answer as \(y = \ldots\) unless the question allows an implicit form.
:::

:::eg Spot the error: Find the general solution of \(x\dfrac{dy}{dx} + 3y = 8x^2\) for \(x > 0\) (7 marks).
A student wrote this answer.

Line 1: \(\dfrac{dy}{dx} + \dfrac{3}{x}y = 8x^2\)
Line 2: \(I = e^{3\ln x} = x^3\)
Line 3: \(\dfrac{d}{dx}\left(x^3y\right) = 8x^5\), so \(x^3y = \tfrac43x^6 + c\)
Line 4: \(y = \tfrac43x^3 + \dfrac{c}{x^3}\)

The method is right throughout, but **line 1 divides the left side by \(x\) and forgets the right side**: \(8x^2 \div x = 8x\), not \(8x^2\). The method mark for dividing is earned [M1] but the accuracy mark is lost [A0].

Line 2 is correct. [B1]

Lines 3 and 4 do exactly what the method asks with the equation the student wrote, so the integration and the division earn their method marks [M1] [M1] and, because later marks follow through a slip made earlier, both accuracy marks too [A1 FT] [A1 FT]. The student scores 6 out of 7.

Correct line 1: \(\dfrac{dy}{dx} + \dfrac3xy = 8x\). [A1]
Then \(\dfrac{d}{dx}(x^3y) = 8x^4\), \(x^3y = \tfrac85x^5 + c\), and \(y = \tfrac85x^2 + \dfrac{c}{x^3}\).

**Check**: \(x\left(\tfrac{16}{5}x - \tfrac{3c}{x^4}\right) + 3\left(\tfrac85x^2 + \tfrac{c}{x^3}\right) = \tfrac{16}{5}x^2 + \tfrac{24}{5}x^2 = 8x^2\).
:::

:::try Start easy, finish at exam standard
Q: Find the general solution of \(\dfrac{dy}{dx} + 3y = 8e^{x}\).
A: \(I = e^{3x}\), so \(\dfrac{d}{dx}(ye^{3x}) = 8e^{4x}\), giving \(ye^{3x} = 2e^{4x} + c\) and \(y = 2e^{x} + ce^{-3x}\).
Q: Find the general solution of \(\dfrac{dy}{dx} + y\tan x = \cos x\) for \(-\tfrac{\pi}{2} < x < \tfrac{\pi}{2}\).
A: \(\int \tan x\,dx = \ln\sec x\), so \(I = \sec x\). Then \(\dfrac{d}{dx}(y\sec x) = \cos x\sec x = 1\), so \(y\sec x = x + c\) and \(y = (x + c)\cos x\).
Q: Find the general solution of \(x\dfrac{dy}{dx} - 3y = x^4\) for \(x > 0\).
A: Divide by \(x\): \(\dfrac{dy}{dx} - \dfrac3xy = x^3\), so \(I = x^{-3}\). Then \(\dfrac{d}{dx}(x^{-3}y) = 1\), \(x^{-3}y = x + c\), and \(y = x^4 + cx^3\).
Q: Solve \(x\dfrac{dy}{dx} + y = 6x^2\) for \(x > 0\) by recognising a product derivative.
A: The left side is \(\dfrac{d}{dx}(xy)\), so \(xy = 2x^3 + c\) and \(y = 2x^2 + \dfrac cx\).
Q: Solve \(\dfrac{dy}{dx} + 2y = 4x\), given that \(y = 3\) when \(x = 0\).
A: \(I = e^{2x}\) and \(\dfrac{d}{dx}(ye^{2x}) = 4xe^{2x}\). By parts, \(ye^{2x} = 2xe^{2x} - e^{2x} + c\), so \(y = 2x - 1 + ce^{-2x}\). Then \(3 = -1 + c\) gives \(c = 4\) and \(y = 2x - 1 + 4e^{-2x}\).
Q: The current \(i\) amperes in a circuit satisfies \(0.5\dfrac{di}{dt} + 4i = 6e^{-2t}\), with \(i = 0\) when \(t = 0\). Find \(i\), and the time at which \(i\) is greatest.
A: Standard form: \(\dfrac{di}{dt} + 8i = 12e^{-2t}\), so \(I = e^{8t}\) and \(\dfrac{d}{dt}(ie^{8t}) = 12e^{6t}\). Then \(ie^{8t} = 2e^{6t} + c\), and \(i = 2e^{-2t} + ce^{-8t}\). With \(i(0) = 0\), \(c = -2\), so \(i = 2\left(e^{-2t} - e^{-8t}\right)\). Greatest when \(\dfrac{di}{dt} = -4e^{-2t} + 16e^{-8t} = 0\), so \(e^{6t} = 4\) and \(t = \dfrac{\ln 4}{6} = 0.231\) s (3 s.f.).
Q: Use \(y = ux\) to solve \(\dfrac{dy}{dx} = \dfrac{x + 2y}{x}\) for \(x > 0\).
A: \(u + x\dfrac{du}{dx} = 1 + 2u\), so \(x\dfrac{du}{dx} = 1 + u\). Then \(\displaystyle\int \frac{1}{1 + u}\,du = \int \frac{1}{x}\,dx\), \(\ln|1 + u| = \ln x + c\), \(1 + u = Ax\), and \(y = Ax^2 - x\).
Q: A population \(P\) of fish (in thousands) satisfies \(\dfrac{dP}{dt} - 0.05P = -3\), where \(t\) is in years and the \(-3\) is the harvest. Given that \(P = 50\) when \(t = 0\), find \(P\) and the time at which the fish die out.
A: \(I = e^{-0.05t}\), so \(\dfrac{d}{dt}(Pe^{-0.05t}) = -3e^{-0.05t}\) and \(Pe^{-0.05t} = 60e^{-0.05t} + c\), so \(P = 60 + ce^{0.05t}\). Then \(c = -10\) and \(P = 60 - 10e^{0.05t}\). \(P = 0\) when \(e^{0.05t} = 6\), \(t = 20\ln 6 = 35.8\) years (3 s.f.).
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Find the general solution of \(x\dfrac{dy}{dx} + 5y = 10x\) for \(x > 0\).
A: Standard form \(\dfrac{dy}{dx} + \dfrac5xy = 10\), so \(I = e^{5\ln x} = x^5\). [B1]
\(\dfrac{d}{dx}(x^5y) = 10x^5\) [M1], so \(x^5y = \tfrac53x^6 + c\). [A1]
\(y = \tfrac53x + cx^{-5}\). [A1]
Q: [5 marks] ★ Find the general solution of \(\dfrac{dy}{dx} + y = \sinh x\), giving \(y\) in terms of \(x\).
A: \(I = e^{x}\). [B1]
\(\dfrac{d}{dx}(ye^{x}) = e^{x}\sinh x\) [M1]. Write \(\sinh x = \tfrac12(e^{x} - e^{-x})\), so the right side is \(\tfrac12(e^{2x} - 1)\) and \(ye^{x} = \tfrac14e^{2x} - \tfrac12x + c\). [M1 A1]
\(y = \tfrac14e^{x} - \tfrac12xe^{-x} + ce^{-x}\). [A1]
Q: [5 marks] ★★ Solve \((x + 1)\dfrac{dy}{dx} - y = (x + 1)^2\) for \(x > -1\), given that \(y = 3\) when \(x = 0\).
A: Standard form: \(\dfrac{dy}{dx} - \dfrac{1}{x + 1}y = x + 1\). \(I = e^{-\ln(x + 1)} = \dfrac{1}{x + 1}\). [B1]
\(\dfrac{d}{dx}\left(\dfrac{y}{x + 1}\right) = 1\) [M1], so \(\dfrac{y}{x + 1} = x + c\) and \(y = (x + c)(x + 1)\). [A1]
\(y = 3\) at \(x = 0\): \(3 = c\) [M1], so \(y = (x + 3)(x + 1)\). [A1]
Q: [9 marks] ★★ A drug is given to a patient by a drip. The concentration \(c\) mg per litre in the blood after \(t\) hours satisfies \(\dfrac{dc}{dt} + 0.4c = 5e^{-0.1t}\), with \(c = 0\) when \(t = 0\). (a) Find \(c\) in terms of \(t\). (b) Find the time at which the concentration is greatest, and its greatest value.
A: (a) \(I = e^{0.4t}\). [B1]
\(\dfrac{d}{dt}(ce^{0.4t}) = 5e^{0.3t}\) [M1], so \(ce^{0.4t} = \tfrac{50}{3}e^{0.3t} + k\). [A1]
\(c = 0\) at \(t = 0\): \(k = -\tfrac{50}{3}\) [M1 A1], so \(c = \tfrac{50}{3}\left(e^{-0.1t} - e^{-0.4t}\right)\). [A1]
(b) \(\dfrac{dc}{dt} = \tfrac{50}{3}\left(-0.1e^{-0.1t} + 0.4e^{-0.4t}\right) = 0\) gives \(e^{0.3t} = 4\) [M1], so \(t = \dfrac{\ln 4}{0.3} = 4.62\) hours. [A1]
Then \(c = \tfrac{50}{3}\left(4^{-1/3} - 4^{-4/3}\right) = 7.87\) mg per litre. [A1]
Q: [6 marks] ★★ Use the substitution \(y = ux\) to solve \(x\dfrac{dy}{dx} = y + xe^{y/x}\) for \(0 < x < e\), given that \(y = 0\) when \(x = 1\).
A: \(\dfrac{dy}{dx} = u + x\dfrac{du}{dx}\). [B1]
The equation is \(\dfrac{dy}{dx} = \dfrac yx + e^{y/x} = u + e^{u}\), so \(x\dfrac{du}{dx} = e^{u}\). [M1]
\(\displaystyle\int e^{-u}\,du = \int \frac1x\,dx\) [M1], so \(-e^{-u} = \ln x + c\). [A1]
\(u = 0\) at \(x = 1\): \(-1 = c\). [M1]
\(e^{-u} = 1 - \ln x\), so \(y = ux = -x\ln(1 - \ln x)\). [A1]
Q: [9 marks] (#math.p3.inttech) ★★★ The differential equation \(\dfrac{dy}{dx} + y = xy^3\), with \(y > 0\), is to be solved. (a) Use the substitution \(z = \dfrac{1}{y^2}\) to show that \(\dfrac{dz}{dx} - 2z = -2x\). (b) Find the general solution for \(z\). (c) Given that \(y = 1\) when \(x = 0\), find \(y\) in terms of \(x\).
H: \(z = y^{-2}\), so \(\dfrac{dz}{dx} = -2y^{-3}\dfrac{dy}{dx}\). Replace \(\dfrac{dy}{dx}\) from the equation.
H: In (b) the integrating factor is \(e^{-2x}\), and \(\displaystyle\int -2xe^{-2x}\,dx\) needs parts.
H: In (c) find \(z\) when \(x = 0\) first, then take \(y = z^{-1/2}\).
A: (a) \(\dfrac{dz}{dx} = -2y^{-3}\dfrac{dy}{dx}\) [M1]
\(= -2y^{-3}(xy^3 - y)\) [M1]
\(= -2x + 2y^{-2} = -2x + 2z\), so \(\dfrac{dz}{dx} - 2z = -2x\). [A1]
(b) \(I = e^{-2x}\). [B1]
\(\dfrac{d}{dx}(ze^{-2x}) = -2xe^{-2x}\) [M1]
By parts: \(ze^{-2x} = xe^{-2x} + \tfrac12e^{-2x} + c\) [M1], so \(z = x + \tfrac12 + ce^{2x}\). [A1]
(c) \(y = 1\) at \(x = 0\) gives \(z = 1\): \(1 = \tfrac12 + c\), \(c = \tfrac12\). [M1]
\(y = \left(x + \tfrac12 + \tfrac12e^{2x}\right)^{-1/2}\). [A1]
Q: [10 marks] (#math.fm.hyperbolic) ★★★ The differential equation \(\dfrac{dy}{dx} + 2y\coth x = 4\cosh x\) is to be solved for \(x > 0\). (a) Show that an integrating factor is \(\sinh^2x\). (b) Find the solution for which \(y = 2\) when \(x = \ln 2\). (c) Show that \(y e^{-x} \to \tfrac23\) as \(x \to \infty\).
H: \(\coth x = \dfrac{\cosh x}{\sinh x}\), and the top is the derivative of the bottom.
H: In (b), \(\displaystyle\int \cosh x\sinh^2x\,dx\) is a reverse chain rule. Remember \(\sinh(\ln 2) = \tfrac34\).
H: In (c), write \(\sinh x\) in terms of \(e^{x}\) and let \(x \to \infty\).
A: (a) \(\displaystyle\int \coth x\,dx = \ln\sinh x\) [B1], so \(I = e^{2\ln\sinh x}\) [M1] \(= \sinh^2x\). [A1]
(b) \(\dfrac{d}{dx}\left(y\sinh^2x\right) = 4\cosh x\sinh^2x\) [M1]
\(y\sinh^2x = \tfrac43\sinh^3x + c\) [M1 A1]
At \(x = \ln 2\), \(\sinh x = \tfrac34\): \(2 \times \tfrac{9}{16} = \tfrac43 \times \tfrac{27}{64} + c\), so \(c = \tfrac{9}{8} - \tfrac{9}{16} = \tfrac{9}{16}\). [M1]
\(y = \tfrac43\sinh x + \dfrac{9}{16\sinh^2x}\). [A1]
(c) \(ye^{-x} = \tfrac43 \cdot \tfrac12\left(1 - e^{-2x}\right) + \dfrac{9e^{-x}}{16\sinh^2x}\). [B1]
As \(x \to \infty\) the second term tends to 0 and the first to \(\tfrac23\). [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Find \(x\) in terms of \(y\) given \(\dfrac{dy}{dx} = \dfrac{1}{x + y^2}\) and \(x = 0\) when \(y = 0\).
H: This is not linear in \(y\). Turn it upside down: \(\dfrac{dx}{dy} = x + y^2\), and treat \(x\) as the unknown function of \(y\).
H: Now it is a first order linear equation for \(x\) in the variable \(y\), with integrating factor \(e^{-y}\).
A: \(\dfrac{dx}{dy} = x + y^2\), so \(\dfrac{dx}{dy} - x = y^2\). [M1]
\(I = e^{-y}\) [B1], so \(\dfrac{d}{dy}\left(xe^{-y}\right) = y^2e^{-y}\). [M1]
Parts twice: \(xe^{-y} = -e^{-y}(y^2 + 2y + 2) + c\). [A1]
\(x = 0\), \(y = 0\): \(0 = -2 + c\), \(c = 2\). [M1]
\(x = 2e^{y} - y^2 - 2y - 2\). [A1]
Q: [4 marks] ★★★ The functions \(y_1\) and \(y_2\) are two different solutions of \(\dfrac{dy}{dx} + 2y = Q(x)\), for the same function \(Q\). Show that the difference \(w = y_1 - y_2\) is \(Ce^{-2x}\) for a constant \(C\), and deduce that the two solutions get closer together as \(x \to \infty\).
H: Subtract the two equations. What equation does \(w\) satisfy?
H: Solve that equation (separate, or use the integrating factor).
A: Subtracting the equations, \(\dfrac{dw}{dx} + 2w = 0\). [M1 A1]
Then \(\dfrac{d}{dx}\left(we^{2x}\right) = 0\), so \(we^{2x} = C\) and \(w = Ce^{-2x}\). [M1]
\(e^{-2x} \to 0\), so \(y_1 - y_2 \to 0\): the solutions converge, whatever \(Q\) is. [A1]
This is the idea behind "general solution = complementary function + particular integral" in the next chapter: the complementary part \(Ce^{-2x}\) is the same for every solution and dies away.
:::

:::quiz
? What is the integrating factor for \(x\dfrac{dy}{dx} - 4y = x\) with \(x > 0\)?
+ \(x^{-4}\)
- \(e^{-4x}\)
- \(x^{4}\)
- \(e^{-4/x}\)
> Divide by \(x\) first: \(P = -\dfrac4x\), and \(e^{-4\ln x} = x^{-4}\). The answer \(e^{-4x}\) reads \(P = -4\) off the equation without dividing, \(x^4\) drops the minus sign, and \(e^{-4/x}\) forgets to integrate \(\dfrac1x\) as a logarithm.
? Which line is the correct next step after finding the integrating factor \(I\) for \(\dfrac{dy}{dx} + Py = Q\)?
+ \(\dfrac{d}{dx}(Iy) = IQ\)
- \(\dfrac{d}{dx}(Iy) = Q\)
- \(Iy = \displaystyle\int Q\,dx\)
- \(y = I\displaystyle\int Q\,dx\)
> Multiplying both sides by \(I\) gives \(IQ\) on the right, and the left becomes \(\dfrac{d}{dx}(Iy)\). Forgetting to multiply the right side by \(I\) is the most common slip.
? The substitution \(y = ux\), where \(u\) is a function of \(x\), gives \(\dfrac{dy}{dx} =\)
+ \(u + x\dfrac{du}{dx}\)
- \(x\dfrac{du}{dx}\)
- \(u + \dfrac{du}{dx}\)
- \(u\)
> Use the product rule on \(u \times x\): \(\dfrac{d}{dx}(ux) = u \cdot 1 + x\dfrac{du}{dx}\). Dropping \(u\) treats \(u\) as a constant multiple only of the derivative; dropping \(x\) forgets the factor \(x\).
? The general solution of a first order differential equation contains
+ one arbitrary constant
- two arbitrary constants
- no arbitrary constant
- as many constants as there are terms in the equation
> One integration is needed, so one constant appears. Second order equations have two.
? For \(\dfrac{dy}{dx} + y\tan x = 2\), what is the integrating factor on \(-\tfrac\pi2 < x < \tfrac\pi2\)?
+ \(\sec x\)
- \(\cos x\)
- \(e^{\tan x}\)
- \(\ln\sec x\)
> \(\int \tan x\,dx = \ln\sec x\), and the integrating factor is \(e^{\ln\sec x} = \sec x\). The answer \(\ln\sec x\) forgets the exponential; \(\cos x\) has the wrong sign in the power.
? The solution of a linear equation is \(y = 5 + 3e^{-2x}\). What does \(y\) approach as \(x \to \infty\)?
+ \(5\)
- \(8\)
- \(0\)
- \(3\)
> The term \(3e^{-2x}\) tends to 0, so only the constant 5 is left. The value 8 is \(y\) at \(x = 0\), not the limit.
:::

:::checklist What you can now do
- [ ] I can write a first order linear equation in the standard form \(\dfrac{dy}{dx} + Py = Q\) and find its integrating factor, simplifying \(e^{\ln\cdots}\).
- [ ] I can use an integrating factor to find the general solution, including equations such as \(x\dfrac{dy}{dx} - 4y = x\) and \(\coth x\dfrac{dy}{dx} + y = \cosh x\).
- [ ] I can spot an equation whose left side is already a product derivative and integrate it directly.
- [ ] I can use a given substitution \(y = ux\) to reduce a homogeneous equation to a separable one and solve it.
- [ ] I can use a given substitution such as \(z = \dfrac1y\) to reduce an equation to a first order linear equation and solve it.
- [ ] I can use initial conditions to find a particular solution and state where it is defined.
- [ ] I can build a differential equation from a rate statement (a mixing tank, cooling, a circuit, a harvest), solve it, and interpret the transient and long-term behaviour.
:::

:::recap
- Standard form \(\dfrac{dy}{dx} + Py = Q\): divide by the coefficient of \(\dfrac{dy}{dx}\) first.
- Integrating factor \(I = e^{\int P\,dx}\); \(\dfrac{d}{dx}(Iy) = IQ\); integrate, add \(+c\), divide by \(I\).
- Simplify \(e^{\ln f} = f\) and \(e^{k\ln x} = x^k\); the modulus in \(\ln|x|\) does not matter for an integrating factor.
- If the left side is already a product derivative, such as \(x\dfrac{dy}{dx} + y\), integrate directly.
- \(y = ux\) gives \(\dfrac{dy}{dx} = u + x\dfrac{du}{dx}\) and turns \(\dfrac{dy}{dx} = f\!\left(\dfrac yx\right)\) into a separable equation.
- \(z = \dfrac1y\) gives \(\dfrac{dz}{dx} = -y^{-2}\dfrac{dy}{dx}\); replace \(\dfrac{dy}{dx}\) from the equation and every \(y\) should become \(z\).
- A particular solution uses the condition in the whole solution, after \(+c\) is in.
- Modelling: rate in minus rate out; check the units; the transient dies away and the rest is the long-term behaviour.
:::

:::links
- watch: [Integrating factor: dy/dx + Py = Q](https://www.examsolutions.net/tutorials/solving-equations-form-dydx-py-q-using-integrating-factor/) · ExamSolutions · the five steps worked on several examples
- watch: [Differential equations, a tourist's guide](https://www.3blue1brown.com/lessons/differential-equations) · 3Blue1Brown · what a solution means, seen as a flow
- read: [Linear first order equations](https://tutorial.math.lamar.edu/Classes/DE/Linear.aspx) · Paul's Online Notes · the same method with extra examples and the reasoning
- practise: [Differential equations](https://www.khanacademy.org/math/differential-equations) · Khan Academy · first order equations with exercises
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 differential equation questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Second order differential equations](#math.fm.de2) solves equations with a second derivative, using a complementary function and a particular integral.
