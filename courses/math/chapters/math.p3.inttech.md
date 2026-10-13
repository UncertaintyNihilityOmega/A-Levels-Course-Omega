@chapter math.p3.inttech
@title Integration techniques: parts, substitution and partial fractions
@level a2
@paper CAIE P3 · Edexcel IAL P4 · AQA/OCR/Edexcel Pure Year 2
@time 9–11 hours
@summary The A2 toolkit for integrals that are not in the standard list: the reverse chain rule for \(f'(x)/f(x)\), partial fractions, integration by parts (including \(\ln x\) and a repeated application), and a given substitution with its limits changed. A table at the end helps you pick the method.

:::why
The standard integrals only cover the functions you can write down at once. Real problems throw up products such as \(x e^{-x}\), quotients such as \(\dfrac{x}{x^2 + 1}\), and roots inside fractions. A rate of change like \(\dfrac{dV}{dt} = t e^{-t/2}\) is a product, and to find the volume you must integrate it. This chapter gives you four moves that cover almost everything a Paper 3 integral can ask. Each one undoes a differentiation rule you already know: the chain rule, the product rule, and the algebra of adding fractions.
:::

**Before you start**, you need the standard integrals from [Further integration](#math.p3.integ), the rules from [Differentiation](#math.p3.diff), and partial fractions from [Partial fractions and the binomial series](#math.p3.partial). Every method here ends with a standard integral, so keep that list to hand.

:::try Warm-up
Q: Differentiate \(x e^{2x}\). (from [Further differentiation](#math.p3.diff))
A: Product rule: \(e^{2x} + 2xe^{2x} = (1 + 2x)e^{2x}\).
Q: Express \(\dfrac{3}{(x - 1)(x + 2)}\) in partial fractions. (from [Partial fractions and the binomial series](#math.p3.partial))
A: \(3 = A(x + 2) + B(x - 1)\) gives \(A = 1\) at \(x = 1\) and \(B = -1\) at \(x = -2\), so \(\dfrac{1}{x - 1} - \dfrac{1}{x + 2}\).
Q: Find \(\displaystyle\int_0^{\pi/4} \sec^2 x\,dx\). (from [Further integration](#math.p3.integ))
A: \(\Big[\tan x\Big]_0^{\pi/4} = 1 - 0 = 1\).
:::

## Integrals of the form f′(x)/f(x)

:::def Integrand
The integrand is the function being integrated, the expression between the integral sign and \(dx\). Every method in this chapter rewrites the integrand into something you can integrate at sight.
:::

Differentiate \(\ln|f(x)|\) with the chain rule and you get \(\dfrac{f'(x)}{f(x)}\). Reversing this gives a result that handles a whole family of integrals at once.

:::key Reverse chain rule for a logarithm
\[\int \frac{f'(x)}{f(x)}\,dx = \ln|f(x)| + c\]
It applies when the numerator is the derivative of the denominator, or a constant multiple of it. This result is on MF19.
:::

The skill is to spot that the top is (a multiple of) the derivative of the bottom. If it is only out by a constant factor, multiply and divide to fix it.

:::eg Find (a) \(\displaystyle\int \frac{x}{x^2 + 4}\,dx\), (b) \(\displaystyle\int \tan x\,dx\), and (c) \(\displaystyle\int_0^2 \frac{3x^2 + 2}{x^3 + 2x + 1}\,dx\), giving (c) to 3 significant figures.
(a) The derivative of \(x^2 + 4\) is \(2x\), and the numerator is \(x = \tfrac12(2x)\):
\[\int \frac{x}{x^2 + 4}\,dx = \tfrac12\int \frac{2x}{x^2 + 4}\,dx = \tfrac12\ln(x^2 + 4) + c\]
No modulus signs are needed because \(x^2 + 4 > 0\).

(b) Write \(\tan x = \dfrac{\sin x}{\cos x}\). The derivative of \(\cos x\) is \(-\sin x\), so
\[\int \frac{\sin x}{\cos x}\,dx = -\int \frac{-\sin x}{\cos x}\,dx = -\ln|\cos x| + c = \ln|\sec x| + c\]

(c) The derivative of \(x^3 + 2x + 1\) is \(3x^2 + 2\), exactly the numerator:
\[\int_0^2 \frac{3x^2 + 2}{x^3 + 2x + 1}\,dx = \Big[\ln|x^3 + 2x + 1|\Big]_0^2 = \ln 13 - \ln 1 = 2.56\ \text{(3 s.f.)}\]
:::

:::proof Why the integral of f′/f is a logarithm
Let \(y = \ln|\mathrm{f}(x)|\). If \(\mathrm{f}(x) > 0\), then \(y = \ln \mathrm{f}(x)\) and the chain rule gives \(\dfrac{dy}{dx}\) \(= \dfrac{1}{\mathrm{f}(x)} \times \mathrm{f}'(x)\).
If \(\mathrm{f}(x) < 0\), then \(|\mathrm{f}(x)| = -\mathrm{f}(x)\), so \(y = \ln\big(-\mathrm{f}(x)\big)\) and \(\dfrac{dy}{dx}\) \(= \dfrac{-\mathrm{f}'(x)}{-\mathrm{f}(x)}\). The two minus signs cancel.
Both cases give \(\dfrac{d}{dx}\ln|\mathrm{f}(x)|\) \(= \dfrac{\mathrm{f}'(x)}{\mathrm{f}(x)}\). Integration undoes differentiation, so \(\displaystyle\int\dfrac{\mathrm{f}'(x)}{\mathrm{f}(x)}\,dx\) \(= \ln|\mathrm{f}(x)| + c\). The modulus signs are there because \(\ln\) is only defined for positive numbers.
:::

:::warn Check the numerator is really the derivative
\(\displaystyle\int\frac{1}{x^2 + 4}\,dx\) is **not** a logarithm, because the numerator \(1\) is not a multiple of \(2x\). It is an inverse tangent: \(\tfrac12\tan^{-1}\!\left(\tfrac x2\right) + c\). Differentiate the denominator before you decide.
:::

## Partial fractions in integration

A fraction with a factorised denominator can be split into simple parts, and each part is a standard integral. For a part \(\dfrac{A}{ax + b}\), the result is \(\dfrac Aa\ln|ax + b|\). For a part \(\dfrac{C}{(x + k)^2}\), write it as \(C(x + k)^{-2}\) and integrate to get \(-\dfrac{C}{x + k}\).

:::eg Find \(\displaystyle\int_2^4 \frac{5x + 1}{(x - 1)(x + 2)}\,dx\), giving your answer to 3 significant figures.
Split into partial fractions: \(\dfrac{5x + 1}{(x - 1)(x + 2)}\) \(= \dfrac{A}{x - 1} + \dfrac{B}{x + 2}\), so \(5x + 1 = A(x + 2) + B(x - 1)\). Put \(x = 1\): \(6 = 3A\), so \(A = 2\). Put \(x = -2\): \(-9 = -3B\), so \(B = 3\).
\[\int_2^4 \left(\frac{2}{x - 1} + \frac{3}{x + 2}\right)dx = \Big[2\ln|x - 1| + 3\ln|x + 2|\Big]_2^4\]
\[= (2\ln 3 + 3\ln 6) - (2\ln 1 + 3\ln 4) = 2\ln 3 + 3\ln\tfrac64 = 3.41\ \text{(3 s.f.)}\]
:::

:::eg Show that \(\displaystyle\int_2^3 \frac{x^2 + 3}{x^2 - 1}\,dx\) \(= 1 + 2\ln\tfrac32\).
The numerator and denominator have the same degree, so divide first: \(x^2 + 3 = (x^2 - 1) + 4\), hence
\[\frac{x^2 + 3}{x^2 - 1} = 1 + \frac{4}{(x - 1)(x + 1)} = 1 + \frac{2}{x - 1} - \frac{2}{x + 1}\]
(for the last step, \(4 = A(x + 1) + B(x - 1)\) gives \(A = 2\) at \(x = 1\) and \(B = -2\) at \(x = -1\)). Now integrate:
\[\Big[x + 2\ln(x - 1) - 2\ln(x + 1)\Big]_2^3 = (3 + 2\ln 2 - 2\ln 4) - (2 + 0 - 2\ln 3)\]
\[= 1 + 2\ln 2 - 4\ln 2 + 2\ln 3 = 1 - 2\ln 2 + 2\ln 3 = 1 + 2\ln\tfrac32\]
:::

:::eg Find \(\displaystyle\int_2^4 \frac{3x + 1}{(x - 1)(x + 2)^2}\,dx\), giving the exact answer.
Write \(\dfrac{3x + 1}{(x - 1)(x + 2)^2}\) \(= \dfrac{A}{x - 1} + \dfrac{B}{x + 2} + \dfrac{C}{(x + 2)^2}\), so \(3x + 1\) \(= A(x + 2)^2 + B(x - 1)(x + 2) + C(x - 1)\). Put \(x = 1\): \(4 = 9A\), so \(A = \tfrac49\). Put \(x = -2\): \(-5 = -3C\), so \(C = \tfrac53\). Comparing \(x^2\): \(0 = A + B\), so \(B = -\tfrac49\).
\[\int_2^4\left(\frac{4/9}{x - 1} - \frac{4/9}{x + 2} + \frac{5/3}{(x + 2)^2}\right)dx = \Big[\tfrac49\ln\left|\tfrac{x - 1}{x + 2}\right| - \tfrac{5}{3(x + 2)}\Big]_2^4\]
At \(x = 4\): \(\tfrac49\ln\tfrac12 - \tfrac5{18}\). At \(x = 2\): \(\tfrac49\ln\tfrac14 - \tfrac5{12}\). Subtracting, and using \(\ln\tfrac12 - \ln\tfrac14 = \ln 2\):
\[\tfrac49\ln 2 + \tfrac{5}{12} - \tfrac{5}{18} = \tfrac49\ln 2 + \tfrac{5}{36}\]
:::

## Integration by parts

The product rule says \(\dfrac{d}{dx}(uv)\) \(= u\dfrac{dv}{dx} + v\dfrac{du}{dx}\). Integrate both sides and rearrange, and you get a rule for integrating a product.

:::key Integration by parts
\[\int u\,\frac{dv}{dx}\,dx = uv - \int v\,\frac{du}{dx}\,dx\]
For a definite integral, apply the limits to the \(uv\) term as well: \(\displaystyle\int_a^b u\,\frac{dv}{dx}\,dx\) \(= \Big[uv\Big]_a^b - \int_a^b v\,\frac{du}{dx}\,dx\). This formula is on MF19.
:::

:::proof Where integration by parts comes from
Start with the product rule for two functions \(u\) and \(v\) of \(x\): \(\dfrac{d}{dx}(uv)\) \(= u\dfrac{dv}{dx} + v\dfrac{du}{dx}\).
Integrate both sides with respect to \(x\). The left side is the function \(uv\), because integration undoes differentiation: \(uv\) \(= \displaystyle\int u\dfrac{dv}{dx}\,dx + \int v\dfrac{du}{dx}\,dx\).
Subtract the last integral from both sides: \(\displaystyle\int u\dfrac{dv}{dx}\,dx\) \(= uv - \int v\dfrac{du}{dx}\,dx\).
So parts swaps one integral for another. It helps when the new integral, with \(\dfrac{du}{dx}\) in place of \(u\), is simpler. For example, with \(u = x\) the \(x\) becomes \(1\).
:::

Choose \(u\) as the factor that becomes **simpler** when you differentiate it, and \(\dfrac{dv}{dx}\) as the factor you can integrate. A power of \(x\) (which loses a power each time) is the usual \(u\), unless the other factor is \(\ln x\) or an inverse trigonometric function, which you cannot integrate directly but can differentiate.

:::eg Find \(\displaystyle\int x\sin 2x\,dx\), and hence evaluate \(\displaystyle\int_0^{\pi/2} x\sin 2x\,dx\).
Let \(u = x\) and \(\dfrac{dv}{dx} = \sin 2x\). Then \(\dfrac{du}{dx} = 1\) and \(v = -\tfrac12\cos 2x\).
\[\int x\sin 2x\,dx = -\tfrac12 x\cos 2x - \int\left(-\tfrac12\cos 2x\right)dx = -\tfrac12 x\cos 2x + \tfrac14\sin 2x + c\]
For the definite integral, at \(x = \tfrac\pi2\) the value is \(-\tfrac12\cdot\tfrac\pi2\cdot(-1) + 0\) \(= \tfrac\pi4\), and at \(x = 0\) it is \(0\). So \(\displaystyle\int_0^{\pi/2} x\sin 2x\,dx\) \(= \dfrac\pi4\).
:::

:::eg Find \(\displaystyle\int \ln x\,dx\) and \(\displaystyle\int_1^e x\ln x\,dx\).
For \(\ln x\) there is only one factor, so write it as \(\ln x \times 1\): let \(u = \ln x\) and \(\dfrac{dv}{dx} = 1\). Then \(\dfrac{du}{dx} = \dfrac1x\) and \(v = x\).
\[\int \ln x\,dx = x\ln x - \int x\cdot\frac1x\,dx = x\ln x - x + c\]
For \(x\ln x\): let \(u = \ln x\) and \(\dfrac{dv}{dx} = x\), so \(v = \tfrac12x^2\):
\[\int_1^e x\ln x\,dx = \Big[\tfrac12x^2\ln x\Big]_1^e - \int_1^e \tfrac12 x\,dx = \tfrac12e^2 - \Big[\tfrac14x^2\Big]_1^e = \tfrac12e^2 - \tfrac14e^2 + \tfrac14 = \tfrac14(e^2 + 1)\]
which is \(2.10\) to 3 significant figures.
:::

When the power of \(x\) is 2 or more, one application of parts lowers the power by one, so you apply it again.

:::eg Evaluate \(\displaystyle\int_0^1 x^2e^{-x}\,dx\), giving your answer to 3 significant figures.
Let \(u = x^2\) and \(\dfrac{dv}{dx} = e^{-x}\), so \(\dfrac{du}{dx} = 2x\) and \(v = -e^{-x}\):
\[\int x^2e^{-x}\,dx = -x^2e^{-x} + \int 2xe^{-x}\,dx\]
Apply parts again to \(\displaystyle\int 2xe^{-x}\,dx\) with \(u = 2x\), \(v = -e^{-x}\): it equals \(-2xe^{-x} + \displaystyle\int 2e^{-x}\,dx\) \(= -2xe^{-x} - 2e^{-x}\). So
\[\int x^2e^{-x}\,dx = -e^{-x}\left(x^2 + 2x + 2\right) + c\]
\[\int_0^1 x^2e^{-x}\,dx = -e^{-1}(5) + 2 = 2 - \frac5e = 0.161\ \text{(3 s.f.)}\]
:::

:::eg Find the exact value of \(\displaystyle\int_0^1 x\tan^{-1}x\,dx\).
Let \(u = \tan^{-1}x\), so \(\dfrac{du}{dx} = \dfrac{1}{1 + x^2}\), and \(\dfrac{dv}{dx} = x\), so \(v = \tfrac12x^2\).
\[\int_0^1 x\tan^{-1}x\,dx = \Big[\tfrac12x^2\tan^{-1}x\Big]_0^1 - \tfrac12\int_0^1 \frac{x^2}{1 + x^2}\,dx = \frac\pi8 - \tfrac12\int_0^1\left(1 - \frac{1}{1 + x^2}\right)dx\]
(because \(x^2 = (1 + x^2) - 1\)). The last integral is \(\Big[x - \tan^{-1}x\Big]_0^1\) \(= 1 - \dfrac\pi4\). So the result is
\[\frac\pi8 - \tfrac12\left(1 - \frac\pi4\right) = \frac\pi4 - \frac12\]
:::

:::eg The volume \(V\) litres of water in a tank changes at rate \(\dfrac{dV}{dt} = te^{-t/2}\) litres per minute, where \(t\) is the time in minutes. How much water flows in during the first 4 minutes?
The amount is \(\displaystyle\int_0^4 te^{-t/2}\,dt\). Let \(u = t\) and \(\dfrac{dv}{dt} = e^{-t/2}\), so \(\dfrac{du}{dt} = 1\) and \(v = -2e^{-t/2}\):
\[\int_0^4 te^{-t/2}\,dt = \Big[-2te^{-t/2}\Big]_0^4 + 2\int_0^4 e^{-t/2}\,dt = -8e^{-2} + 2\Big[-2e^{-t/2}\Big]_0^4\]
\[= -8e^{-2} - 4e^{-2} + 4 = 4 - 12e^{-2} = 2.38\ \text{litres (3 s.f.)}\]
:::

:::warn Slips in parts
Keep the minus sign: the rule is \(uv\) **minus** the new integral. Do not drop the limits from the \(uv\) term in a definite integral. If the new integral is harder than the one you started with, you chose \(u\) and \(\frac{dv}{dx}\) the wrong way round, so swap them. Do not add the constant of integration until the last integral is done (and of course not at all for a definite integral).
:::

## Integration by substitution

A substitution replaces \(x\) by a new variable \(u\) so that the integral becomes a standard one. In Cambridge Paper 3 the substitution is **given in the question**, so your job is to carry it out correctly. There are four things to change: the function, \(dx\), the limits (if definite), and finally nothing should still contain \(x\).

:::key The substitution routine
1. Differentiate the substitution to find \(\dfrac{du}{dx}\) (or \(\dfrac{dx}{du}\)) and replace \(dx\).
2. Rewrite the whole integrand in terms of \(u\).
3. For a definite integral, **change the limits** to \(u\)-values and do not go back to \(x\).
4. Integrate in \(u\). For an indefinite integral, substitute back to finish in \(x\).
:::

:::proof Why substitution works, and why the limits change
Suppose \(\mathrm{F}\) is an antiderivative of \(\mathrm{f}\), so \(\mathrm{F}'(u) = \mathrm{f}(u)\), and let \(u = \mathrm{g}(x)\). The chain rule gives \(\dfrac{d}{dx}\,\mathrm{F}\big(\mathrm{g}(x)\big)\) \(= \mathrm{F}'\big(\mathrm{g}(x)\big)\,\mathrm{g}'(x)\) \(= \mathrm{f}(u)\dfrac{du}{dx}\).
Integrate both sides with respect to \(x\):
\[\int \mathrm{f}(u)\dfrac{du}{dx}\,dx = \mathrm{F}\big(\mathrm{g}(x)\big) = \mathrm{F}(u) = \int \mathrm{f}(u)\,du\]
So \(\dfrac{du}{dx}\,dx\) can be replaced by \(du\). That is the same as writing \(du = \mathrm{g}'(x)\,dx\).
For a definite integral from \(x = a\) to \(x = b\): \(\Big[\mathrm{F}\big(\mathrm{g}(x)\big)\Big]_a^b\) \(= \mathrm{F}\big(\mathrm{g}(b)\big) - \mathrm{F}\big(\mathrm{g}(a)\big)\). This is \(\mathrm{F}(u)\) evaluated from \(u = \mathrm{g}(a)\) to \(u = \mathrm{g}(b)\), so the limits become the \(u\)-values.
:::

:::eg Use the substitution \(u = x + 1\) to evaluate \(\displaystyle\int_0^3 \frac{x}{\sqrt{x + 1}}\,dx\).
\(u = x + 1\), so \(du = dx\) and \(x = u - 1\). When \(x = 0\), \(u = 1\); when \(x = 3\), \(u = 4\).
\[\int_1^4 \frac{u - 1}{\sqrt u}\,du = \int_1^4\left(u^{1/2} - u^{-1/2}\right)du = \Big[\tfrac23u^{3/2} - 2u^{1/2}\Big]_1^4\]
\[= \left(\tfrac{16}{3} - 4\right) - \left(\tfrac23 - 2\right) = \tfrac43 + \tfrac43 = \tfrac83\]
:::

:::eg (Exam style) Use the substitution \(u = \sin x\) to show that \(\displaystyle\int_0^{\pi/2}\sin^2 2x\cos x\,dx\) \(= \frac{8}{15}\).
Since \(\sin 2x = 2\sin x\cos x\), we have \(\sin^2 2x\cos x = 4\sin^2x\cos^3x\) \(= 4\sin^2x\cos^2x\cdot\cos x\). [M1] Now \(\cos^2 x = 1 - u^2\), and \(du = \cos x\,dx\). [B1] The limits change: \(x = 0\) gives \(u = 0\), and \(x = \tfrac\pi2\) gives \(u = 1\). [B1]
\[\int_0^1 4u^2(1 - u^2)\,du = \Big[\tfrac43u^3 - \tfrac45u^5\Big]_0^1 \quad [A1]\]
\[= \tfrac43 - \tfrac45 = \frac{8}{15} \quad [A1]\]
:::

:::eg (Exam style) Use the substitution \(u = \sqrt x\) to find the exact value of \(\displaystyle\int_1^4 \frac{1}{x + \sqrt x}\,dx\).
\(u = \sqrt x\) gives \(x = u^2\), so \(dx = 2u\,du\). [B1] The limits: \(x = 1\) gives \(u = 1\) and \(x = 4\) gives \(u = 2\). [B1] The integrand becomes
\[\frac{2u}{u^2 + u} = \frac{2u}{u(u + 1)} = \frac{2}{u + 1} \quad [M1]\]
\[\int_1^2 \frac{2}{u + 1}\,du = \Big[2\ln(u + 1)\Big]_1^2 = 2\ln 3 - 2\ln 2 = 2\ln\tfrac32 \quad [M1\ A1]\]
:::

## Long exam questions

Real questions chain the methods: one part sets up an integral, the next evaluates it. Read the whole question first, because an early part (such as partial fractions) usually feeds a later one.

:::eg (Exam style) The curve \(C\) has equation \(y = \dfrac{6x + 7}{(x + 1)(2x + 3)}\) for \(x \ge 0\). (a) Express \(y\) in partial fractions. (b) Find the exact area of the region bounded by \(C\), the \(x\)-axis and the lines \(x = 0\) and \(x = 2\), in the form \(\ln k\). (c) Hence, or otherwise, show that the gradient of \(C\) is negative for all \(x \ge 0\).
**(a)** Let \(\dfrac{6x + 7}{(x + 1)(2x + 3)}\) \(= \dfrac{A}{x + 1} + \dfrac{B}{2x + 3}\), so \(6x + 7 = A(2x + 3) + B(x + 1)\). [M1]
Put \(x = -1\): \(1 = A\). Put \(x = -\tfrac32\): \(-2 = -\tfrac12B\), so \(B = 4\). [A1 A1]
\[y = \frac{1}{x + 1} + \frac{4}{2x + 3}\]

**(b)** The area is \(\displaystyle\int_0^2 \left(\frac{1}{x + 1} + \frac{4}{2x + 3}\right)dx\). [M1] The second term is \(\dfrac{4}{2x + 3}\) \(= 2 \times \dfrac{2}{2x + 3}\), a multiple of \(\dfrac{\mathrm{f}'}{\mathrm{f}}\), so
\[\Big[\ln(x + 1) + 2\ln(2x + 3)\Big]_0^2 \quad [A1\ A1]\]
\[= (\ln 3 + 2\ln 7) - (0 + 2\ln 3) = 2\ln 7 - \ln 3 = \ln\frac{49}{3} \quad [A1]\]
**(c)** Differentiate the partial fractions: \(\dfrac{dy}{dx}\) \(= -\dfrac{1}{(x + 1)^2} - \dfrac{8}{(2x + 3)^2}\). [M1 A1] Both terms are negative because the squares are positive, so the gradient is negative for all \(x \ge 0\). [B1]
Check: the area \(\ln\dfrac{49}{3} = 2.79\). The curve falls from \(y = 2.33\) at \(x = 0\) to \(y = 0.90\) at \(x = 2\), so over a width of \(2\) the area must lie between \(1.8\) and \(4.7\). ✓
:::

:::eg (Exam style) (a) Use the substitution \(u = \sqrt x\) to show that \(\displaystyle\int_0^4 e^{\sqrt x}\,dx\) \(= \int_0^2 2ue^u\,du\). (b) Hence find the exact value of \(\displaystyle\int_0^4 e^{\sqrt x}\,dx\). (c) Hence find the exact value of \(\displaystyle\int_0^4 \left(1 + e^{\sqrt x}\right)dx\).
**(a)** \(u = \sqrt x\) gives \(x = u^2\), so \(dx = 2u\,du\). [B1] The integrand \(e^{\sqrt x}\) becomes \(e^u\), so the integral is \(\displaystyle\int e^u \cdot 2u\,du\). [M1] The limits: \(x = 0\) gives \(u = 0\), and \(x = 4\) gives \(u = 2\). [B1]
\[\int_0^4 e^{\sqrt x}\,dx = \int_0^2 2ue^u\,du\]
**(b)** The letter \(u\) is already the variable, so call the parts \(p\) and \(q\): let \(p = 2u\) and \(\dfrac{dq}{du} = e^u\), so \(\dfrac{dp}{du} = 2\) and \(q = e^u\). [M1]
\[\int_0^2 2ue^u\,du = \Big[2ue^u\Big]_0^2 - \int_0^2 2e^u\,du = 4e^2 - \Big[2e^u\Big]_0^2 \quad [A1\ M1]\]
\[= 4e^2 - (2e^2 - 2) = 2e^2 + 2 \quad [A1\ A1]\]
**(c)** \(\displaystyle\int_0^4 1\,dx = 4\), so the integral is \(4 + 2e^2 + 2 = 2e^2 + 6\). [M1 A1]
Check: \(2e^2 + 2 = 16.8\). The curve \(y = e^{\sqrt x}\) rises from \(1\) at \(x = 0\) to \(e^2 = 7.39\) at \(x = 4\), so over a width of \(4\) an area of \(16.8\) (an average height of \(4.2\)) is sensible. ✓
:::

## Choosing the method

Read the integrand and ask the questions in this order:

| What you see | First move |
|---|---|
| Top is the derivative of the bottom (or a multiple) | \(\ln|\text{bottom}|\), the \(f'/f\) rule |
| Algebraic fraction with a factorised denominator | Partial fractions (divide first if the degree is not lower) |
| Product of a power of \(x\) and \(e^{kx}\), \(\sin kx\) or \(\cos kx\) | By parts, \(u\) = the power of \(x\) |
| \(\ln x\) alone, or \(x^n\ln x\), or \(x^n\tan^{-1}x\) | By parts, \(u\) = the log or inverse trig function |
| A substitution is given | Use it, and change the limits |
| Powers of \(\sin\) or \(\cos\) | Identities from [Further integration](#math.p3.integ) first |

:::exam What earns marks
- **Show the setup.** In "show that" questions, write \(u\), \(\frac{dv}{dx}\), \(\frac{du}{dx}\) and \(v\), then the parts formula. The method mark is for the correct structure.
- **Change the limits** in a substitution (a mark in its own right). You may also go back to \(x\) and use the original limits, but that is longer and risks an error.
- **Exact** means keep \(\ln\), \(\pi\) and \(e\) in your answer; do not convert to a decimal.
- Both \(\dfrac{f'}{f}\) and parts are on MF19, but the substitution routine and partial fractions are not: practise them until they are automatic.
:::

:::board Other boards
Edexcel IAL P4 and the Year 2 Pure courses of AQA, OCR and Edexcel teach all four methods: \(f'/f\), partial fractions, parts and substitution. The Cambridge Paper 3 syllabus gives the substitution in the question, so check your own board's specification to see whether you may have to choose one yourself.
:::

:::eg Spot the error: a substitution with the limits left alone
A student answered "Use the substitution \(u = x^2 + 1\) to find \(\displaystyle\int_0^2 x\sqrt{x^2 + 1}\,dx\)" [5 marks].

Line 1: \(u = x^2 + 1\), so \(du = 2x\,dx\) and \(x\,dx = \tfrac12\,du\).
Line 2: \(\displaystyle\int_0^2 x\sqrt{x^2 + 1}\,dx\) \(= \tfrac12\int_0^2 u^{1/2}\,du\).
Line 3: \(= \tfrac12\left[\tfrac23u^{3/2}\right]_0^2\) \(= \tfrac13 \times 2^{3/2}\) \(= 0.943\).

Line 1 scores [B1]. **Line 2 scores [M1 B0].** The integrand in \(u\) is right, but \(0\) and \(2\) are values of \(x\). Once the variable is \(u\), the limits must be \(u\)-values: \(x = 0\) gives \(u = 1\) and \(x = 2\) gives \(u = 5\). Line 3 has a correct antiderivative [A1], but the answer is wrong [A0], because it depends on the correct limits. The student scores 3 out of 5.

Correct working:
\[\tfrac12\int_1^5 u^{1/2}\,du = \tfrac13\Big[u^{3/2}\Big]_1^5 = \tfrac13\left(5\sqrt5 - 1\right) = 3.39\]

**Check:** the integrand is \(1.41\) at \(x = 1\) and \(4.47\) at \(x = 2\), so over a width of \(2\) the area must be well above \(0.943\). The answer \(3.39\) fits.
:::

:::try Start easy, finish at exam standard
Q: Find \(\displaystyle\int \frac{2x}{x^2 + 5}\,dx\).
A: The numerator is the derivative of the denominator: \(\ln(x^2 + 5) + c\).
Q: Evaluate \(\displaystyle\int_0^{\ln 2}\frac{e^x}{1 + e^x}\,dx\), giving your answer to 3 significant figures.
A: The numerator is the derivative of \(1 + e^x\): \(\Big[\ln(1 + e^x)\Big]_0^{\ln 2}\) \(= \ln 3 - \ln 2 = \ln\tfrac32 = 0.405\).
Q: Evaluate \(\displaystyle\int_1^2\frac{x + 5}{(x + 1)(x + 2)}\,dx\), giving your answer to 3 significant figures.
A: \(x + 5 = A(x + 2) + B(x + 1)\): \(x = -1\) gives \(A = 4\); \(x = -2\) gives \(B = -3\). So \(\Big[4\ln(x + 1) - 3\ln(x + 2)\Big]_1^2\) \(= 4\ln\tfrac32 - 3\ln\tfrac43\) \(= 0.759\).
Q: Find \(\displaystyle\int_0^{\pi/2} x\cos x\,dx\).
A: \(u = x\), \(\frac{dv}{dx} = \cos x\): \(\Big[x\sin x\Big]_0^{\pi/2} - \displaystyle\int_0^{\pi/2}\sin x\,dx\) \(= \dfrac\pi2 - 1\).
Q: Evaluate \(\displaystyle\int_0^1 xe^{3x}\,dx\), giving your answer to 3 significant figures.
A: \(u = x\), \(v = \tfrac13e^{3x}\): \(\Big[\tfrac13xe^{3x}\Big]_0^1 - \tfrac13\displaystyle\int_0^1 e^{3x}\,dx\) \(= \tfrac13e^3 - \tfrac19(e^3 - 1)\) \(= \tfrac{2e^3 + 1}{9} = 4.57\).
Q: Evaluate \(\displaystyle\int_1^2\frac{\ln x}{x^2}\,dx\), giving your answer to 3 significant figures.
A: \(u = \ln x\), \(\frac{dv}{dx} = x^{-2}\), \(v = -\dfrac1x\): \(\Big[-\dfrac{\ln x}{x}\Big]_1^2 + \displaystyle\int_1^2 x^{-2}\,dx\) \(= -\dfrac{\ln 2}{2} + \Big[-\dfrac1x\Big]_1^2\) \(= -\dfrac{\ln 2}{2} + \dfrac12 = 0.153\).
Q: Find \(\displaystyle\int x^2\sin x\,dx\).
A: First: \(-x^2\cos x + \displaystyle\int 2x\cos x\,dx\). Second, on \(\displaystyle\int 2x\cos x\,dx\): \(2x\sin x - \displaystyle\int 2\sin x\,dx\) \(= 2x\sin x + 2\cos x\). So the result is \(-x^2\cos x + 2x\sin x + 2\cos x + c\).
Q: Use the substitution \(u = 1 + x\) to evaluate \(\displaystyle\int_0^1\frac{x}{(1 + x)^3}\,dx\).
A: \(x = u - 1\), limits 1 to 2: \(\displaystyle\int_1^2\left(u^{-2} - u^{-3}\right)du\) \(= \Big[-u^{-1} + \tfrac12u^{-2}\Big]_1^2\) \(= \left(-\tfrac12 + \tfrac18\right) - \left(-1 + \tfrac12\right)\) \(= \tfrac18\).
Q: (Exam style) Use the substitution \(u = \cos x\) to show that \(\displaystyle\int_0^{\pi/2}\sin^3x\,dx\) \(= \frac23\).
A: \(\sin^3x = \sin^2x\cdot\sin x\) \(= (1 - u^2)\sin x\), and \(du = -\sin x\,dx\). The limits: \(x = 0\) gives \(u = 1\), \(x = \tfrac\pi2\) gives \(u = 0\). So \(\displaystyle\int_1^0 -(1 - u^2)\,du\) \(= \int_0^1(1 - u^2)\,du\) \(= \Big[u - \tfrac13u^3\Big]_0^1\) \(= \tfrac23\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find the exact value of \(\displaystyle\int_0^2 \frac{3x^2}{x^3 + 1}\,dx\).
A: The numerator is the derivative of the denominator, so the integral is \(\Big[\ln(x^3 + 1)\Big]_0^2\). [M1 A1] This is \(\ln 9 - \ln 1 = \ln 9\). [A1]
Q: [4 marks] ★ Find the exact value of \(\displaystyle\int_0^1 xe^{-2x}\,dx\).
A: Let \(u = x\) and \(\dfrac{dv}{dx} = e^{-2x}\), so \(v = -\tfrac12e^{-2x}\). [M1]
\[\Big[-\tfrac12xe^{-2x}\Big]_0^1 + \tfrac12\int_0^1 e^{-2x}\,dx = -\tfrac12e^{-2} + \tfrac12\Big[-\tfrac12e^{-2x}\Big]_0^1\]
[A1] This is \(-\tfrac12e^{-2} - \tfrac14e^{-2} + \tfrac14\). [M1] The result is \(\tfrac14 - \tfrac34e^{-2}\). [A1]
Q: [5 marks] ★★ Use the substitution \(u = 1 + \sqrt x\) to find the value of \(\displaystyle\int_0^4 \frac{1}{1 + \sqrt x}\,dx\), giving your answer to 3 significant figures.
A: \(x = (u - 1)^2\), so \(dx = 2(u - 1)\,du\). [B1] The limits: \(x = 0\) gives \(u = 1\) and \(x = 4\) gives \(u = 3\). [B1] The integrand becomes \(\dfrac{2(u - 1)}{u} = 2 - \dfrac2u\). [M1] 
\[\int_1^3\left(2 - \dfrac2u\right)du = \Big[2u - 2\ln u\Big]_1^3 = (6 - 2\ln 3) - 2\]
[A1] The result is \(4 - 2\ln 3 = 1.80\). [A1]
Q: [6 marks] ★★ Find the exact value of \(\displaystyle\int_0^2 \frac{5x + 7}{(x + 1)(x + 3)}\,dx\), giving your answer in the form \(\ln k\).
A: \(5x + 7 = A(x + 3) + B(x + 1)\). [M1] Put \(x = -1\): \(2 = 2A\), so \(A = 1\). Put \(x = -3\): \(-8 = -2B\), so \(B = 4\). [A1 A1]
\[\Big[\ln(x + 1) + 4\ln(x + 3)\Big]_0^2 = (\ln 3 + 4\ln 5) - (0 + 4\ln 3)\]
[M1 A1] This is \(4\ln 5 - 3\ln 3 = \ln\dfrac{625}{27}\). [A1]
Q: [5 marks] ★★ Find the exact value of \(\displaystyle\int_1^e x^3\ln x\,dx\).
A: Let \(u = \ln x\) and \(\dfrac{dv}{dx} = x^3\), so \(\dfrac{du}{dx} = \dfrac1x\) and \(v = \tfrac14x^4\). [M1]
\[\Big[\tfrac14x^4\ln x\Big]_1^e - \tfrac14\int_1^e x^3\,dx = \tfrac14e^4 - \Big[\tfrac1{16}x^4\Big]_1^e\]
[A1 M1] This is \(\tfrac14e^4 - \tfrac1{16}e^4 + \tfrac1{16}\). [A1] The result is \(\dfrac{3e^4 + 1}{16}\). [A1]
Q: [9 marks] (#math.p3.diff) ★★★ The curve \(C\) has equation \(y = xe^{-x}\) for \(x \ge 0\). (a) Find the coordinates of the stationary point of \(C\) and determine its nature. (b) Find the exact area of the region bounded by \(C\), the \(x\)-axis and the line \(x = 1\).
H: In (a), use the product rule on \(xe^{-x}\), then factorise so \(e^{-x}\) is a common factor.
H: Use the second derivative to decide the nature of the stationary point.
H: In (b), integrate by parts with \(u = x\) and \(\dfrac{dv}{dx} = e^{-x}\).
A: (a) \(\dfrac{dy}{dx} = e^{-x} - xe^{-x}\) \(= (1 - x)e^{-x}\). [M1 A1] This is zero when \(x = 1\), and \(y = e^{-1}\), so the point is \(\left(1, \dfrac1e\right)\). [A1] \(\dfrac{d^2y}{dx^2}\) \(= -e^{-x} - (1 - x)e^{-x}\), which is \((x - 2)e^{-x}\), and at \(x = 1\) it is \(-e^{-1} < 0\). [M1] So the point is a maximum. [A1] (b)
\[\int_0^1 xe^{-x}\,dx = \Big[-xe^{-x}\Big]_0^1 + \int_0^1 e^{-x}\,dx\]
[M1 A1]
\[= -e^{-1} + \Big[-e^{-x}\Big]_0^1 = -e^{-1} - e^{-1} + 1\]
[M1] The area is \(1 - \dfrac2e\). [A1]
Q: [9 marks] (#math.p3.partial) ★★★ (a) Use the substitution \(u = e^x\) to show that \(\displaystyle\int_0^{\ln 3}\frac{e^x}{e^{2x} + 3e^x + 2}\,dx\) can be written as \(\displaystyle\int_1^3 \frac{1}{(u + 1)(u + 2)}\,du\). (b) Hence find the exact value of the integral, in the form \(\ln k\).
H: Write \(e^{2x}\) as \(u^2\) and find \(du\) in terms of \(dx\). The numerator \(e^x\,dx\) is exactly \(du\).
H: In (b), split \(\dfrac{1}{(u + 1)(u + 2)}\) into partial fractions.
H: Combine the logarithms at the end: \(\ln a - \ln b = \ln\dfrac ab\).
A: (a) \(u = e^x\), so \(du = e^x\,dx\) and \(e^{2x} = u^2\). [B1] The integral becomes \(\displaystyle\int \dfrac{du}{u^2 + 3u + 2}\) [M1] with \(u^2 + 3u + 2 = (u + 1)(u + 2)\). The limits: \(x = 0\) gives \(u = 1\), and \(x = \ln 3\) gives \(u = 3\). [B1] (b) \(1 = A(u + 2) + B(u + 1)\): \(u = -1\) gives \(A = 1\) and \(u = -2\) gives \(B = -1\). [M1 A1 A1]
\[\int_1^3\left(\dfrac{1}{u + 1} - \dfrac{1}{u + 2}\right)du = \Big[\ln(u + 1) - \ln(u + 2)\Big]_1^3\]
[M1] This is \((\ln 4 - \ln 5) - (\ln 2 - \ln 3)\). [A1] \(= \ln\dfrac{4 \times 3}{5 \times 2}\) \(= \ln\dfrac65\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ For integers \(n \ge 0\), let \(I_n = \displaystyle\int_0^1 x^ne^x\,dx\). (a) Show that \(I_n = e - nI_{n-1}\) for \(n \ge 1\). (b) Find \(I_0\) and hence find the exact value of \(I_3\).
H: In (a), use parts with \(u = x^n\) and \(\dfrac{dv}{dx} = e^x\).
H: In (b), \(I_0\) is an easy integral. Then use the result from (a) with \(n = 1\), then \(n = 2\), then \(n = 3\).
A: (a) Let \(u = x^n\) and \(\dfrac{dv}{dx} = e^x\), so \(\dfrac{du}{dx} = nx^{n-1}\) and \(v = e^x\). [M1] \(I_n\) \(= \Big[x^ne^x\Big]_0^1 - n\displaystyle\int_0^1 x^{n-1}e^x\,dx\). [A1] \(= e - nI_{n-1}\), since \(1^ne^1 = e\) and \(0^ne^0 = 0\) for \(n \ge 1\). [A1] (b) \(I_0 = \displaystyle\int_0^1 e^x\,dx\) \(= e - 1\). [B1] Then \(I_1 = e - 1 \times I_0 = e - (e - 1)\) \(= 1\), [M1] \(I_2 = e - 2I_1 = e - 2\), [A1] and \(I_3 = e - 3I_2 = e - 3(e - 2) = 6 - 2e\). [A1]
Q: [6 marks] ★★★ Let \(I\) \(= \displaystyle\int_0^{\pi/2} e^x\sin x\,dx\) and \(J\) \(= \displaystyle\int_0^{\pi/2} e^x\cos x\,dx\). (a) Use parts on \(I\) to show that \(I = e^{\pi/2} - J\). (b) Use parts on \(J\) to find another relation between \(I\) and \(J\). (c) Hence find the exact value of \(I\).
H: In (a), let \(u = \sin x\) and \(\dfrac{dv}{dx} = e^x\). In (b), let \(u = \cos x\) and \(\dfrac{dv}{dx} = e^x\).
H: You now have two equations in the two unknowns \(I\) and \(J\). Eliminate \(J\).
A: (a) \(I\) \(= \Big[e^x\sin x\Big]_0^{\pi/2} - \displaystyle\int_0^{\pi/2} e^x\cos x\,dx\) [M1] \(= e^{\pi/2} - J\). [A1] (b)
\[J = \Big[e^x\cos x\Big]_0^{\pi/2} + \int_0^{\pi/2} e^x\sin x\,dx = (0 - 1) + I\]
So \(J = I - 1\). [M1 A1] (c) Substitute: \(I = e^{\pi/2} - (I - 1)\), [M1] so \(2I = e^{\pi/2} + 1\) and \(I = \tfrac12\left(e^{\pi/2} + 1\right)\). [A1]
:::

:::quiz
? What is \(\displaystyle\int\frac{x}{x^2 + 1}\,dx\)?
- \(\ln(x^2 + 1) + c\)
+ \(\tfrac12\ln(x^2 + 1) + c\)
- \(\tan^{-1}x + c\)
- \(\dfrac{x^2}{2(x^2 + 1)} + c\)
> The derivative of \(x^2 + 1\) is \(2x\), so the numerator \(x\) is half of it. Half of \(\ln(x^2 + 1)\) is the answer; differentiate to check.
? To find \(\displaystyle\int xe^{2x}\,dx\) by parts, which choice is best?
+ \(u = x\) and \(\dfrac{dv}{dx} = e^{2x}\)
- \(u = e^{2x}\) and \(\dfrac{dv}{dx} = x\)
- \(u = xe^{2x}\) and \(\dfrac{dv}{dx} = 1\)
- Parts cannot be used here.
> Choose \(u\) to be the part that gets simpler when differentiated: \(x\) becomes \(1\). The other way round gives a harder integral \(\int \tfrac12x^2e^{2x}\,dx\).
? Using \(u = \sin x\) for \(\displaystyle\int_0^{\pi/2}\sin^2x\cos x\,dx\), what are the new limits?
- \(0\) and \(\tfrac\pi2\)
+ \(0\) and \(1\)
- \(1\) and \(0\)
- \(0\) and \(\infty\)
> \(u = \sin 0 = 0\) and \(u = \sin\tfrac\pi2 = 1\). The integral becomes \(\int_0^1 u^2\,du = \tfrac13\).
? What is \(\displaystyle\int\ln x\,dx\)?
- \(\dfrac1x + c\)
- \(x\ln x + c\)
+ \(x\ln x - x + c\)
- \(\dfrac{\ln x}{x} - x + c\)
> By parts with \(u = \ln x\) and \(\frac{dv}{dx} = 1\): \(x\ln x - \int 1\,dx\). Differentiate \(x\ln x - x\) to confirm it gives \(\ln x\).
? What must you do first to integrate \(\dfrac{x^2 + 3}{x^2 - 1}\) by partial fractions?
- Factorise the numerator.
+ Divide, because the numerator has the same degree as the denominator.
- Use the substitution \(u = x^2\).
- Nothing, because partial fractions work directly.
> A fraction can only be split into partial fractions if it is proper (numerator of lower degree). Here \(\frac{x^2+3}{x^2-1}\) \(= 1 + \frac{4}{x^2-1}\).
:::

:::checklist What you can now do
- [ ] I can integrate a fraction whose top is the derivative of its bottom, or a constant multiple of it, as a logarithm.
- [ ] I can integrate an algebraic fraction by partial fractions, dividing first when it is not proper.
- [ ] I can integrate a product by parts, choosing \(u\) so that it gets simpler when differentiated.
- [ ] I can integrate \(\ln x\), \(x^n\ln x\) and \(x\tan^{-1}x\) by parts.
- [ ] I can apply parts twice when a power of \(x\) of 2 or more is multiplied by \(e^{kx}\), \(\sin kx\) or \(\cos kx\).
- [ ] I can carry out a given substitution and change the limits of a definite integral.
- [ ] I can give an exact answer with \(\ln\), \(\pi\) or \(e\), and choose the right method for an unfamiliar integral.
:::

:::recap
- \(\displaystyle\int\frac{f'(x)}{f(x)}\,dx\) \(= \ln|f(x)| + c\); check that the numerator is the derivative of the denominator, or a constant multiple of it.
- Partial fractions turn a fraction into terms \(\dfrac{A}{ax+b}\to\dfrac Aa\ln|ax+b|\) and \(\dfrac{C}{(x+k)^2}\to-\dfrac{C}{x+k}\). Divide first if the fraction is not proper.
- By parts: \(\displaystyle\int u\frac{dv}{dx}\,dx\) \(= uv - \int v\frac{du}{dx}\,dx\). Take \(u\) as the part that simplifies (a power of \(x\), \(\ln x\), \(\tan^{-1}x\)). Repeat if a power of \(x\) remains.
- \(\displaystyle\int\ln x\,dx\) \(= x\ln x - x + c\), by parts with \(\frac{dv}{dx} = 1\).
- Substitution: replace \(dx\), rewrite the whole integrand in \(u\), and change the limits of a definite integral.
- Exact answers keep \(\ln\), \(\pi\) and \(e\); give decimals only when asked for significant figures.
:::

:::links
- watch: [Integration by parts](https://www.examsolutions.net/tutorials/integration-by-parts/) · ExamSolutions · choosing u and dv/dx
- watch: [Integration by substitution](https://www.examsolutions.net/tutorials/integration-substitution/) · ExamSolutions · changing the variable and the limits
- practise: [CAIE Pure 3 further integration exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/integration/further-integration/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Product Rule & Integration by Parts](https://undergroundmathematics.org/product-rule) · Underground Mathematics · rich problems linking the two
- explore: [Chain Rule & Integration by Substitution](https://undergroundmathematics.org/chain-rule) · Underground Mathematics · rich problems linking the two
- read: [Integration by parts](https://tutorial.math.lamar.edu/Classes/CalcII/IntegrationByParts.aspx) · Paul's Online Notes · many worked examples

Links checked 3 October 2026.
:::
Next: [Differential equations](#math.p3.diffeq).
