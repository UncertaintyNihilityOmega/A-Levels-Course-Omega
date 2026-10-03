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

:::warn Check the numerator is really the derivative
\(\displaystyle\int\frac{1}{x^2 + 4}\,dx\) is **not** a logarithm, because the numerator \(1\) is not a multiple of \(2x\). It is an inverse tangent: \(\tfrac12\tan^{-1}\!\left(\tfrac x2\right) + c\). Differentiate the denominator before you decide.
:::

## Partial fractions in integration

A fraction with a factorised denominator can be split into simple parts, and each part is a standard integral. For a part \(\dfrac{A}{ax + b}\), the result is \(\dfrac Aa\ln|ax + b|\). For a part \(\dfrac{C}{(x + k)^2}\), write it as \(C(x + k)^{-2}\) and integrate to get \(-\dfrac{C}{x + k}\).

:::eg Find \(\displaystyle\int_2^4 \frac{5x + 1}{(x - 1)(x + 2)}\,dx\), giving your answer to 3 significant figures.
Split into partial fractions: \(\dfrac{5x + 1}{(x - 1)(x + 2)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 2}\), so \(5x + 1 = A(x + 2) + B(x - 1)\). Put \(x = 1\): \(6 = 3A\), so \(A = 2\). Put \(x = -2\): \(-9 = -3B\), so \(B = 3\).
\[\int_2^4 \left(\frac{2}{x - 1} + \frac{3}{x + 2}\right)dx = \Big[2\ln|x - 1| + 3\ln|x + 2|\Big]_2^4\]
\[= (2\ln 3 + 3\ln 6) - (2\ln 1 + 3\ln 4) = 2\ln 3 + 3\ln\tfrac64 = 3.41\ \text{(3 s.f.)}\]
:::

:::eg Show that \(\displaystyle\int_2^3 \frac{x^2 + 3}{x^2 - 1}\,dx = 1 + 2\ln\tfrac32\).
The numerator and denominator have the same degree, so divide first: \(x^2 + 3 = (x^2 - 1) + 4\), hence
\[\frac{x^2 + 3}{x^2 - 1} = 1 + \frac{4}{(x - 1)(x + 1)} = 1 + \frac{2}{x - 1} - \frac{2}{x + 1}\]
(for the last step, \(4 = A(x + 1) + B(x - 1)\) gives \(A = 2\) at \(x = 1\) and \(B = -2\) at \(x = -1\)). Now integrate:
\[\Big[x + 2\ln(x - 1) - 2\ln(x + 1)\Big]_2^3 = (3 + 2\ln 2 - 2\ln 4) - (2 + 0 - 2\ln 3)\]
\[= 1 + 2\ln 2 - 4\ln 2 + 2\ln 3 = 1 - 2\ln 2 + 2\ln 3 = 1 + 2\ln\tfrac32\]
:::

:::eg Find \(\displaystyle\int_2^4 \frac{3x + 1}{(x - 1)(x + 2)^2}\,dx\), giving the exact answer.
Write \(\dfrac{3x + 1}{(x - 1)(x + 2)^2} = \dfrac{A}{x - 1} + \dfrac{B}{x + 2} + \dfrac{C}{(x + 2)^2}\), so \(3x + 1 = A(x + 2)^2 + B(x - 1)(x + 2) + C(x - 1)\). Put \(x = 1\): \(4 = 9A\), so \(A = \tfrac49\). Put \(x = -2\): \(-5 = -3C\), so \(C = \tfrac53\). Comparing \(x^2\): \(0 = A + B\), so \(B = -\tfrac49\).
\[\int_2^4\left(\frac{4/9}{x - 1} - \frac{4/9}{x + 2} + \frac{5/3}{(x + 2)^2}\right)dx = \Big[\tfrac49\ln\left|\tfrac{x - 1}{x + 2}\right| - \tfrac{5}{3(x + 2)}\Big]_2^4\]
At \(x = 4\): \(\tfrac49\ln\tfrac12 - \tfrac5{18}\). At \(x = 2\): \(\tfrac49\ln\tfrac14 - \tfrac5{12}\). Subtracting, and using \(\ln\tfrac12 - \ln\tfrac14 = \ln 2\):
\[\tfrac49\ln 2 + \tfrac{5}{12} - \tfrac{5}{18} = \tfrac49\ln 2 + \tfrac{5}{36}\]
:::

## Integration by parts

The product rule says \(\dfrac{d}{dx}(uv) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}\). Integrate both sides and rearrange, and you get a rule for integrating a product.

:::key Integration by parts
\[\int u\,\frac{dv}{dx}\,dx = uv - \int v\,\frac{du}{dx}\,dx\]
For a definite integral, apply the limits to the \(uv\) term as well: \(\displaystyle\int_a^b u\,\frac{dv}{dx}\,dx = \Big[uv\Big]_a^b - \int_a^b v\,\frac{du}{dx}\,dx\). This formula is on MF19.
:::

Choose \(u\) as the factor that becomes **simpler** when you differentiate it, and \(\dfrac{dv}{dx}\) as the factor you can integrate. A power of \(x\) (which loses a power each time) is the usual \(u\), unless the other factor is \(\ln x\) or an inverse trigonometric function, which you cannot integrate directly but can differentiate.

:::eg Find \(\displaystyle\int x\sin 2x\,dx\), and hence evaluate \(\displaystyle\int_0^{\pi/2} x\sin 2x\,dx\).
Let \(u = x\) and \(\dfrac{dv}{dx} = \sin 2x\). Then \(\dfrac{du}{dx} = 1\) and \(v = -\tfrac12\cos 2x\).
\[\int x\sin 2x\,dx = -\tfrac12 x\cos 2x - \int\left(-\tfrac12\cos 2x\right)dx = -\tfrac12 x\cos 2x + \tfrac14\sin 2x + c\]
For the definite integral, at \(x = \tfrac\pi2\) the value is \(-\tfrac12\cdot\tfrac\pi2\cdot(-1) + 0 = \tfrac\pi4\), and at \(x = 0\) it is \(0\). So \(\displaystyle\int_0^{\pi/2} x\sin 2x\,dx = \dfrac\pi4\).
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
Apply parts again to \(\displaystyle\int 2xe^{-x}\,dx\) with \(u = 2x\), \(v = -e^{-x}\): it equals \(-2xe^{-x} + \displaystyle\int 2e^{-x}\,dx = -2xe^{-x} - 2e^{-x}\). So
\[\int x^2e^{-x}\,dx = -e^{-x}\left(x^2 + 2x + 2\right) + c\]
\[\int_0^1 x^2e^{-x}\,dx = -e^{-1}(5) + 2 = 2 - \frac5e = 0.161\ \text{(3 s.f.)}\]
:::

:::eg Find the exact value of \(\displaystyle\int_0^1 x\tan^{-1}x\,dx\).
Let \(u = \tan^{-1}x\), so \(\dfrac{du}{dx} = \dfrac{1}{1 + x^2}\), and \(\dfrac{dv}{dx} = x\), so \(v = \tfrac12x^2\).
\[\int_0^1 x\tan^{-1}x\,dx = \Big[\tfrac12x^2\tan^{-1}x\Big]_0^1 - \tfrac12\int_0^1 \frac{x^2}{1 + x^2}\,dx = \frac\pi8 - \tfrac12\int_0^1\left(1 - \frac{1}{1 + x^2}\right)dx\]
(because \(x^2 = (1 + x^2) - 1\)). The last integral is \(\Big[x - \tan^{-1}x\Big]_0^1 = 1 - \dfrac\pi4\). So the result is
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

:::eg Use the substitution \(u = x + 1\) to evaluate \(\displaystyle\int_0^3 \frac{x}{\sqrt{x + 1}}\,dx\).
\(u = x + 1\), so \(du = dx\) and \(x = u - 1\). When \(x = 0\), \(u = 1\); when \(x = 3\), \(u = 4\).
\[\int_1^4 \frac{u - 1}{\sqrt u}\,du = \int_1^4\left(u^{1/2} - u^{-1/2}\right)du = \Big[\tfrac23u^{3/2} - 2u^{1/2}\Big]_1^4\]
\[= \left(\tfrac{16}{3} - 4\right) - \left(\tfrac23 - 2\right) = \tfrac43 + \tfrac43 = \tfrac83\]
:::

:::eg (Exam style) Use the substitution \(u = \sin x\) to show that \(\displaystyle\int_0^{\pi/2}\sin^2 2x\cos x\,dx = \frac{8}{15}\).
Since \(\sin 2x = 2\sin x\cos x\), we have \(\sin^2 2x\cos x = 4\sin^2x\cos^3x = 4\sin^2x\cos^2x\cdot\cos x\). [M1] Now \(\cos^2 x = 1 - u^2\), and \(du = \cos x\,dx\). [B1] The limits change: \(x = 0\) gives \(u = 0\), and \(x = \tfrac\pi2\) gives \(u = 1\). [B1]
\[\int_0^1 4u^2(1 - u^2)\,du = \Big[\tfrac43u^3 - \tfrac45u^5\Big]_0^1 \quad [A1]\]
\[= \tfrac43 - \tfrac45 = \frac{8}{15} \quad [A1]\]
:::

:::eg (Exam style) Use the substitution \(u = \sqrt x\) to find the exact value of \(\displaystyle\int_1^4 \frac{1}{x + \sqrt x}\,dx\).
\(u = \sqrt x\) gives \(x = u^2\), so \(dx = 2u\,du\). [B1] The limits: \(x = 1\) gives \(u = 1\) and \(x = 4\) gives \(u = 2\). [B1] The integrand becomes
\[\frac{2u}{u^2 + u} = \frac{2u}{u(u + 1)} = \frac{2}{u + 1} \quad [M1]\]
\[\int_1^2 \frac{2}{u + 1}\,du = \Big[2\ln(u + 1)\Big]_1^2 = 2\ln 3 - 2\ln 2 = 2\ln\tfrac32 \quad [M1\ A1]\]
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

:::try Start easy, finish at exam standard
Q: Find \(\displaystyle\int \frac{2x}{x^2 + 5}\,dx\).
A: The numerator is the derivative of the denominator: \(\ln(x^2 + 5) + c\).
Q: Evaluate \(\displaystyle\int_0^{\ln 2}\frac{e^x}{1 + e^x}\,dx\), giving your answer to 3 significant figures.
A: The numerator is the derivative of \(1 + e^x\): \(\Big[\ln(1 + e^x)\Big]_0^{\ln 2} = \ln 3 - \ln 2 = \ln\tfrac32 = 0.405\).
Q: Evaluate \(\displaystyle\int_1^2\frac{x + 5}{(x + 1)(x + 2)}\,dx\), giving your answer to 3 significant figures.
A: \(x + 5 = A(x + 2) + B(x + 1)\): \(x = -1\) gives \(A = 4\); \(x = -2\) gives \(B = -3\). So \(\Big[4\ln(x + 1) - 3\ln(x + 2)\Big]_1^2 = 4\ln\tfrac32 - 3\ln\tfrac43 = 0.759\).
Q: Find \(\displaystyle\int_0^{\pi/2} x\cos x\,dx\).
A: \(u = x\), \(\frac{dv}{dx} = \cos x\): \(\Big[x\sin x\Big]_0^{\pi/2} - \displaystyle\int_0^{\pi/2}\sin x\,dx = \dfrac\pi2 - 1\).
Q: Evaluate \(\displaystyle\int_0^1 xe^{3x}\,dx\), giving your answer to 3 significant figures.
A: \(u = x\), \(v = \tfrac13e^{3x}\): \(\Big[\tfrac13xe^{3x}\Big]_0^1 - \tfrac13\displaystyle\int_0^1 e^{3x}\,dx = \tfrac13e^3 - \tfrac19(e^3 - 1) = \tfrac{2e^3 + 1}{9} = 4.57\).
Q: Evaluate \(\displaystyle\int_1^2\frac{\ln x}{x^2}\,dx\), giving your answer to 3 significant figures.
A: \(u = \ln x\), \(\frac{dv}{dx} = x^{-2}\), \(v = -\dfrac1x\): \(\Big[-\dfrac{\ln x}{x}\Big]_1^2 + \displaystyle\int_1^2 x^{-2}\,dx = -\dfrac{\ln 2}{2} + \Big[-\dfrac1x\Big]_1^2 = -\dfrac{\ln 2}{2} + \dfrac12 = 0.153\).
Q: Find \(\displaystyle\int x^2\sin x\,dx\).
A: First: \(-x^2\cos x + \displaystyle\int 2x\cos x\,dx\). Second, on \(\displaystyle\int 2x\cos x\,dx\): \(2x\sin x - \displaystyle\int 2\sin x\,dx = 2x\sin x + 2\cos x\). So the result is \(-x^2\cos x + 2x\sin x + 2\cos x + c\).
Q: Use the substitution \(u = 1 + x\) to evaluate \(\displaystyle\int_0^1\frac{x}{(1 + x)^3}\,dx\).
A: \(x = u - 1\), limits 1 to 2: \(\displaystyle\int_1^2\left(u^{-2} - u^{-3}\right)du = \Big[-u^{-1} + \tfrac12u^{-2}\Big]_1^2 = \left(-\tfrac12 + \tfrac18\right) - \left(-1 + \tfrac12\right) = \tfrac18\).
Q: (Exam style) Use the substitution \(u = \cos x\) to show that \(\displaystyle\int_0^{\pi/2}\sin^3x\,dx = \frac23\).
A: \(\sin^3x = \sin^2x\cdot\sin x = (1 - u^2)\sin x\), and \(du = -\sin x\,dx\). The limits: \(x = 0\) gives \(u = 1\), \(x = \tfrac\pi2\) gives \(u = 0\). So \(\displaystyle\int_1^0 -(1 - u^2)\,du = \int_0^1(1 - u^2)\,du = \Big[u - \tfrac13u^3\Big]_0^1 = \tfrac23\).
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
> A fraction can only be split into partial fractions if it is proper (numerator of lower degree). Here \(\frac{x^2+3}{x^2-1} = 1 + \frac{4}{x^2-1}\).
:::

:::recap
- \(\displaystyle\int\frac{f'(x)}{f(x)}\,dx = \ln|f(x)| + c\); check that the numerator is the derivative of the denominator, or a constant multiple of it.
- Partial fractions turn a fraction into terms \(\dfrac{A}{ax+b}\to\dfrac Aa\ln|ax+b|\) and \(\dfrac{C}{(x+k)^2}\to-\dfrac{C}{x+k}\). Divide first if the fraction is not proper.
- By parts: \(\displaystyle\int u\frac{dv}{dx}\,dx = uv - \int v\frac{du}{dx}\,dx\). Take \(u\) as the part that simplifies (a power of \(x\), \(\ln x\), \(\tan^{-1}x\)). Repeat if a power of \(x\) remains.
- \(\displaystyle\int\ln x\,dx = x\ln x - x + c\), by parts with \(\frac{dv}{dx} = 1\).
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
