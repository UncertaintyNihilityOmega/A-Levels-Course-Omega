@chapter math.p3.integ
@title Further integration
@level as a2
@paper CAIE P2/P3 · Edexcel IAL P3–P4 · AQA/OCR/Edexcel Pure Year 2
@time 8–10 hours
@summary Integrals of \(e^{ax+b}\), \(\dfrac{1}{ax+b}\), \(\sin(ax+b)\), \(\cos(ax+b)\) and \(\sec^2(ax+b)\); using trigonometric identities to integrate \(\sin^2 x\), \(\cos^2 x\) and \(\tan^2 x\); areas and volumes with these functions; the trapezium rule; and \(\dfrac{1}{x^2+a^2}\) in Paper 3.

:::why
Integration reverses differentiation, so each new derivative from [Further differentiation](#math.p3.diff) gives a new integral. These integrals measure growth that is accumulated continuously, and the area under a wave. Some functions, such as \(e^{x^2}\), have no antiderivative you can write down. The trapezium rule estimates their integrals numerically, which is a method that scientists and engineers use daily.
:::

**Before you start**, you need [Integration](#math.p1.integ) (areas, definite integrals, volumes of revolution), the derivatives in [Further differentiation](#math.p3.diff), and the double angle formulae from [Further trigonometry](#math.p3.trig). Angles are in radians throughout.

## Standard integrals

Each result below is a derivative read backwards. For example, \(\dfrac{d}{dx}(\sin x) = \cos x\) means \(\displaystyle\int \cos x\,dx\) \(= \sin x + c\).

:::key Standard integrals (radians)
\[\int e^x\,dx = e^x + c \qquad \int \frac1x\,dx = \ln|x| + c\]
\[\int \sin x\,dx = -\cos x + c \qquad \int \cos x\,dx = \sin x + c \qquad \int \sec^2 x\,dx = \tan x + c\]
With a linear inside function \(ax + b\), divide by the coefficient \(a\):
\[\int e^{ax+b}\,dx = \frac1a e^{ax+b} + c \qquad \int \frac{1}{ax+b}\,dx = \frac1a\ln|ax+b| + c\]
\[\int \sin(ax+b)\,dx = -\frac1a\cos(ax+b) + c \qquad \int \cos(ax+b)\,dx = \frac1a\sin(ax+b) + c\]
\[\int \sec^2(ax+b)\,dx = \frac1a\tan(ax+b) + c\]
The basic forms are on MF19; the versions with \(ax + b\) follow from the chain rule. The modulus in \(\ln|x|\) allows for negative \(x\). Never forget \(+\,c\).
:::

:::warn Easy slips with signs and factors
The integral of \(\sin x\) is \(-\cos x\), not \(\cos x\). The integral of \(\cos x\) is \(+\sin x\). Dividing by \(a\) is easy to forget: \(\int e^{3x}\,dx = \tfrac13 e^{3x}\), not \(e^{3x}\) or \(3e^{3x}\). Check every integral by differentiating your answer. Also \(\int \dfrac{1}{x}\,dx = \ln|x|\), not \(\dfrac{x^0}{0}\).
:::

:::eg Find (a) \(\displaystyle\int (3e^{2x} + 4)\,dx\), (b) \(\displaystyle\int \frac{6}{2x + 1}\,dx\), (c) \(\displaystyle\int \left(\sin 4x - 5\cos\tfrac x2\right)dx\), (d) \(\displaystyle\int \sec^2\left(\tfrac{x}{2}\right)dx\)
(a) \(\dfrac32 e^{2x} + 4x + c\).

(b) \(6 \times \dfrac12\ln|2x + 1| + c\) \(= 3\ln|2x + 1| + c\).

(c) \(-\tfrac14\cos 4x - 5 \times 2\sin\tfrac x2 + c\) \(= -\tfrac14\cos 4x - 10\sin\tfrac x2 + c\).

(d) \(2\tan\tfrac x2 + c\) (dividing by \(\tfrac12\) means multiplying by \(2\)).
Check (b) by differentiating: \(3 \times \dfrac{2}{2x + 1}\) \(= \dfrac{6}{2x + 1}\). ✓
:::

Sometimes you must expand or divide before integrating. Never integrate a product or quotient term by term.

:::eg Find (a) \(\displaystyle\int (1 + e^x)^2\,dx\), (b) \(\displaystyle\int \frac{x^2 + 1}{x}\,dx\)
(a) Expand: \((1 + e^x)^2 = 1 + 2e^x + e^{2x}\). So the integral is \(x + 2e^x + \tfrac12 e^{2x} + c\).

(b) Divide each term by \(x\): \(\dfrac{x^2 + 1}{x} = x + \dfrac1x\), so the integral is \(\tfrac12 x^2 + \ln|x| + c\).
:::

### Definite integrals with these functions

Substitute the limits as before. Keep answers exact (in terms of \(\ln\), \(e\) and \(\pi\)) when asked.

:::eg Evaluate exactly (a) \(\displaystyle\int_0^{\ln 2} e^{2x}\,dx\), (b) \(\displaystyle\int_1^3 \frac{1}{x}\,dx\), (c) \(\displaystyle\int_0^{\pi/4}\sec^2 x\,dx\), (d) \(\displaystyle\int_0^{\pi/2}\sin 2x\,dx\)
(a) \(\Big[\tfrac12 e^{2x}\Big]_0^{\ln 2}\) \(= \tfrac12\left(e^{2\ln 2} - 1\right)\) \(= \tfrac12(4 - 1) = \tfrac32\), because \(e^{2\ln 2} = e^{\ln 4} = 4\).

(b) \(\Big[\ln x\Big]_1^3 = \ln 3 - \ln 1\) \(= \ln 3\).

(c) \(\Big[\tan x\Big]_0^{\pi/4} = 1 - 0 = 1\).

(d) \(\Big[-\tfrac12\cos 2x\Big]_0^{\pi/2}\) \(= -\tfrac12\cos\pi + \tfrac12\cos 0\) \(= \tfrac12 + \tfrac12 = 1\).
:::

## Using trigonometric identities

You cannot integrate \(\sin^2 x\) directly, but the double angle formulae rewrite it as a function you can integrate. From \(\cos 2x = 1 - 2\sin^2 x\) and \(\cos 2x = 2\cos^2 x - 1\):

:::key Identities for integration
\[\sin^2 x \equiv \tfrac12(1 - \cos 2x) \qquad \cos^2 x \equiv \tfrac12(1 + \cos 2x) \qquad \tan^2 x \equiv \sec^2 x - 1\]
Also useful: \(\sin x\cos x \equiv \tfrac12\sin 2x\). These identities are the key step in many questions, so learn to spot them.
:::

:::eg Find (a) \(\displaystyle\int \sin^2 x\,dx\), (b) \(\displaystyle\int \cos^2 2x\,dx\), (c) \(\displaystyle\int \tan^2 x\,dx\), (d) \(\displaystyle\int_0^{\pi/4}\sin^2 x\,dx\)
(a) \(\displaystyle\int \tfrac12(1 - \cos 2x)\,dx\) \(= \tfrac12 x - \tfrac14\sin 2x + c\).

(b) Replace \(x\) by \(2x\) in the identity for \(\cos^2\): \(\cos^2 2x = \tfrac12(1 + \cos 4x)\). The integral is \(\tfrac12 x + \tfrac18\sin 4x + c\).

(c) \(\displaystyle\int (\sec^2 x - 1)\,dx\) \(= \tan x - x + c\).

(d) Using (a): \(\Big[\tfrac12 x - \tfrac14\sin 2x\Big]_0^{\pi/4}\) \(= \tfrac{\pi}{8} - \tfrac14\sin\tfrac\pi2\) \(= \dfrac\pi8 - \dfrac14\).
Check: \(\dfrac\pi8 - \dfrac14 = 0.1427\), which is a sensible small area under a curve rising from 0 to 0.5 over a width of 0.785. ✓
:::

## Areas and volumes

The area and volume formulae from [Integration](#math.p1.integ) still apply: area \(= \int y\,dx\) (split at roots), and volume about the \(x\)-axis \(= \pi\int y^2\,dx\).

:::eg Find the area under \(y = \dfrac{1}{2x + 1}\) between \(x = 0\) and \(x = 2\), and the volume generated when \(y = \sin x\) for \(0 \le x \le \pi\) is rotated about the \(x\)-axis.
Area \(= \displaystyle\int_0^2 \frac{1}{2x + 1}\,dx\) \(= \Big[\tfrac12\ln(2x + 1)\Big]_0^2\) \(= \tfrac12\ln 5 = 0.805\) (3 s.f.).

Volume \(= \pi\displaystyle\int_0^\pi \sin^2 x\,dx\) \(= \pi\Big[\tfrac12 x - \tfrac14\sin 2x\Big]_0^\pi\) \(= \pi \times \tfrac\pi2\) \(= \dfrac{\pi^2}{2} = 4.93\) (3 s.f.).
:::

:::eg A website's number of users \(N\) grows at a rate \(\dfrac{dN}{dt} = 5000e^{0.2t}\) users per month, where \(t\) is the time in months. There are 20 000 users at \(t = 0\). Find \(N\) in terms of \(t\), and \(N\) when \(t = 5\).
\(N = \displaystyle\int 5000e^{0.2t}\,dt\) \(= \dfrac{5000}{0.2}e^{0.2t} + c\) \(= 25\,000e^{0.2t} + c\). At \(t = 0\): \(20\,000 = 25\,000 + c\), so \(c = -5000\). Therefore \(N = 25\,000e^{0.2t} - 5000\). When \(t = 5\): \(N = 25\,000e - 5000 = 62\,957\), which is \(63\,000\) users to 3 s.f.
:::

:::eg (Exam style) The region \(R\) is bounded by the curve \(y = \dfrac{3}{2x + 1}\), the \(x\)-axis and the lines \(x = 0\) and \(x = 2\). (a) Find the exact area of \(R\). (b) Find the exact volume generated when \(R\) is rotated through \(360^\circ\) about the \(x\)-axis.
**(a)** Area \(= \displaystyle\int_0^2 \frac{3}{2x + 1}\,dx\) [M1]
\[= \Big[\tfrac32\ln(2x + 1)\Big]_0^2 = \tfrac32\ln 5 - \tfrac32\ln 1 = \tfrac32\ln 5\] [A1 A1]

**(b)** Volume \(= \pi\displaystyle\int_0^2 \frac{9}{(2x + 1)^2}\,dx\) \(= 9\pi\int_0^2 (2x + 1)^{-2}\,dx\) [M1]
\[= 9\pi\Big[-\frac{1}{2(2x + 1)}\Big]_0^2 = 9\pi\left(-\frac1{10} + \frac12\right)\] [M1 A1]
\[= 9\pi \times \tfrac25 = \tfrac{18\pi}{5}\] [A1]
:::

:::try Warm-up
Q: Find \(\displaystyle\int \left(4x^3 - \frac{3}{x^2}\right)dx\). (from [Integration](#math.p1.integ))
A: \(\displaystyle\int \left(4x^3 - 3x^{-2}\right)dx\) \(= x^4 + 3x^{-1} + c\) \(= x^4 + \frac3x + c\).
Q: Write \(\cos^2 x\) in terms of \(\cos 2x\). (from [Further trigonometry](#math.p3.trig))
A: \(\cos 2x = 2\cos^2 x - 1\), so \(\cos^2 x = \tfrac12(1 + \cos 2x)\).
Q: Simplify \(e^{2\ln 3}\). (from [Logarithms and exponentials](#math.p3.logs))
A: \(e^{2\ln 3} = e^{\ln 9} = 9\).
:::

## The trapezium rule

Many functions, such as \(e^{x^2}\) or \(\sqrt{1 + x^3}\), cannot be integrated in closed form. We estimate the area under the curve by splitting it into strips and approximating each strip by a trapezium. (This method is listed for Paper 2 in the Cambridge syllabus.)

:::def Ordinate
An ordinate is the \(y\)-value of a curve at a given \(x\). For the trapezium rule you need the ordinates at the ends of each of the \(n\) equal strips, so \(n\) strips need \(n + 1\) ordinates.
:::

:::formula Trapezium rule
To estimate \(\displaystyle\int_a^b y\,dx\) with \(n\) strips of equal width \(h = \dfrac{b-a}{n}\), use the \(n + 1\) ordinates \(y_0, y_1, \ldots, y_n\):
\[\int_a^b y\,dx \approx \tfrac12 h\Big[y_0 + 2\left(y_1 + y_2 + \cdots + y_{n-1}\right) + y_n\Big]\]
The first and last ordinates are counted once, and every other ordinate twice. It is **not** on MF19, so learn it.
:::

:::proof Where the trapezium rule comes from
Each strip, of width \(h\), is replaced by a trapezium. The two parallel sides are the ordinates at the edges of the strip, and the width \(h\) is the distance between them. The area of a trapezium is the average of the parallel sides times the distance between them, so the first strip has area \(\tfrac12 h(y_0 + y_1)\), the second \(\tfrac12 h(y_1 + y_2)\), and so on up to \(\tfrac12 h(y_{n-1} + y_n)\).
Add them up:
\[\tfrac12 h\big[(y_0 + y_1) + (y_1 + y_2) + \cdots + (y_{n-1} + y_n)\big]\]
Every ordinate except the first and the last belongs to two neighbouring strips, so it appears twice. That gives
\[\tfrac12 h\big[y_0 + 2(y_1 + y_2 + \cdots + y_{n-1}) + y_n\big]\]
Try different numbers of strips below and compare with the exact area.

:::html
<div class="widget" data-w="area" data-f="exp(x^2)" data-x="0,1" data-n="4" data-mode="trapezium"></div>
:::
:::

:::eg Use the trapezium rule with 4 strips to estimate \(\displaystyle\int_0^1 e^{x^2}\,dx\), giving your answer to 4 significant figures.
\(h = \dfrac{1 - 0}{4} = 0.25\). The ordinates are:

| \(x\) | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|
| \(y = e^{x^2}\) | 1 | 1.064494 | 1.284025 | 1.755055 | 2.718282 |

\[\text{Estimate} = \tfrac12(0.25)\Big[1 + 2.718282 + 2(1.064494 + 1.284025 + 1.755055)\Big] = 0.125 \times 11.92543 = 1.491\]
:::

### Overestimate or underestimate?

On each strip the trapezium's top edge is a chord of the curve. If the curve bends **upwards** (convex, \(\dfrac{d^2y}{dx^2} > 0\)), the chord lies above the curve and the trapezium rule gives an **overestimate**. If the curve bends **downwards** (concave, \(\dfrac{d^2y}{dx^2} < 0\)), the chord lies below the curve and the rule gives an **underestimate**. You can show this with a sketch.

:::html
<figure class="fig wide"><svg viewBox="0 0 580 215" role="img" aria-label="Two graphs each with four trapezia. For y equals one over x squared the curve bends upwards and the trapezium tops lie above it, an overestimate. For y equals ln x the curve bends downwards and the trapezium tops lie below it, an underestimate."><path class="ax" d="M10 190.0H245" marker-end="url(#ahm)"/><path class="ax" d="M10.0 194.0V30.0" marker-end="url(#ahm)"/><path class="fi" d="M20.0 190.0L20.0 40.0L72.5 123.3L125.0 152.5L177.5 166.0L230.0 173.3L230.0 190.0Z"/><path class="ln thin" d="M20.0 190.0V40.0M72.5 190.0V123.3M125.0 190.0V152.5M177.5 190.0V166.0M230.0 190.0V173.3"/><path class="c1" d="M20.0 40.0L34.0 73.2L48.0 96.5L62.0 113.5L76.0 126.2L90.0 136.0L104.0 143.7L118.0 149.9L132.0 154.9L146.0 159.0L160.0 162.4L174.0 165.3L188.0 167.8L202.0 169.9L216.0 171.7L230.0 173.3"/><text class="ts tc" x="20.0" y="205.0">1</text><text class="ts tc" x="125.0" y="205.0">2</text><text class="ts tc" x="230.0" y="205.0">3</text><text class="tl ti" x="243" y="184.0" text-anchor="end">x</text><text class="tl tb halo" x="130" y="22" text-anchor="middle">overestimate</text><text class="tl halo" x="125" y="115.0">y = 1/x²</text><path class="ax" d="M320 190.0H555" marker-end="url(#ahm)"/><path class="ax" d="M320.0 194.0V30.0" marker-end="url(#ahm)"/><path class="fi" d="M330.0 190.0L382.5 139.3L435.0 103.4L487.5 75.5L540.0 52.7L540.0 190.0Z"/><path class="ln thin" d="M382.5 190.0V139.3M435.0 190.0V103.4M487.5 190.0V75.5M540.0 190.0V52.7"/><path class="c1" d="M330.0 190.0L344.0 174.4L358.0 160.5L372.0 147.9L386.0 136.6L400.0 126.1L414.0 116.5L428.0 107.6L442.0 99.3L456.0 91.4L470.0 84.1L484.0 77.1L498.0 70.6L512.0 64.3L526.0 58.4L540.0 52.7"/><text class="ts tc" x="330.0" y="205.0">1</text><text class="ts tc" x="435.0" y="205.0">2</text><text class="ts tc" x="540.0" y="205.0">3</text><text class="tl ti" x="553" y="184.0" text-anchor="end">x</text><text class="tl tb halo" x="440" y="22" text-anchor="middle">underestimate</text><text class="tl halo" x="440" y="71.2">y = ln x</text></svg><figcaption>Four trapezia under each curve. Where the curve bends upwards the chord tops lie above it (left), so the rule overestimates. Where it bends downwards they lie below it (right), so the rule underestimates.</figcaption></figure>
:::

The Cambridge syllabus (2.5) accepts a sketch of the curve as the reason, so you do not always need to find the second derivative.

:::eg Explain why the estimate of \(\displaystyle\int_0^1 e^{x^2}\,dx\) above is an overestimate. Then use 4 strips to estimate \(\displaystyle\int_1^3 \ln x\,dx\) and say whether it is an over- or underestimate.
For \(y = e^{x^2}\), \(\dfrac{dy}{dx} = 2xe^{x^2}\) and \(\dfrac{d^2y}{dx^2}\) \(= (2 + 4x^2)e^{x^2} > 0\). The curve bends upwards, so each chord is above the curve and the estimate is an overestimate. (The true value is \(1.463\).)

For \(\ln x\): \(h = 0.5\) and the ordinates are \(0\), \(0.405465\), \(0.693147\), \(0.916291\), \(1.098612\):
\[\tfrac12(0.5)\left[0 + 1.098612 + 2(0.405465 + 0.693147 + 0.916291)\right] = 0.25 \times 5.1284 = 1.282\]
Since \(\dfrac{d^2y}{dx^2}\) \(= -\dfrac{1}{x^2} < 0\), the curve is concave and the rule gives an **underestimate**. (The true value is \(3\ln 3 - 2 = 1.296\).)
:::

:::eg (Exam style) Use the trapezium rule with 4 strips to estimate \(\displaystyle\int_0^\pi \sin x\,dx\), giving 3 significant figures, and state with a reason whether it is an overestimate or underestimate. Compare with the exact value.
\(h = \dfrac{\pi}{4}\). The ordinates are \(0\), \(\tfrac{\sqrt2}{2}\), \(1\), \(\tfrac{\sqrt2}{2}\), \(0\). [B1]
\[\text{Estimate} = \tfrac12\cdot\frac\pi4\left[0 + 2\left(\tfrac{\sqrt2}{2} + 1 + \tfrac{\sqrt2}{2}\right) + 0\right] = \frac\pi8 \times 4.8284 = 1.90\] [M1 A1]
The curve \(y = \sin x\) is concave on \(0 < x < \pi\) (\(\dfrac{d^2y}{dx^2} = -\sin x < 0\)), so the chords lie below the curve and the estimate is an underestimate. [B1] The exact value is \(\displaystyle\int_0^\pi \sin x\,dx\) \(= \Big[-\cos x\Big]_0^\pi = 2\), so the estimate \(1.90\) is below it, as predicted. [B1]
:::

### Integrals of 1/(x² + a²) (Paper 3 only)

The derivative \(\dfrac{d}{dx}\tan^{-1}x\) \(= \dfrac{1}{1 + x^2}\) gives the integral directly.

:::key Integral of \(\dfrac{1}{x^2 + a^2}\) (Paper 3 only)
\[\int \frac{1}{x^2 + a^2}\,dx = \frac1a\tan^{-1}\left(\frac xa\right) + c\]
This is on MF19. For \(\dfrac{1}{px^2 + q}\), take out the factor \(p\) first: \(\dfrac{1}{p}\cdot\dfrac{1}{x^2 + q/p}\).
:::

:::proof Checking the formula by differentiating
To show that \(\displaystyle\int \frac{1}{x^2 + a^2}\,dx\) \(= \frac1a\tan^{-1}\left(\frac xa\right) + c\), differentiate the right-hand side. The derivative of \(\tan^{-1}u\) is \(\dfrac{1}{1 + u^2}\), and here \(u = \dfrac xa\), so \(\dfrac{du}{dx} = \dfrac1a\). By the chain rule
\[\frac{d}{dx}\left[\frac1a\tan^{-1}\left(\frac xa\right)\right] = \frac1a \times \frac{1}{1 + \frac{x^2}{a^2}} \times \frac1a = \frac{1}{a^2 + x^2}\]
The last step multiplies the top and bottom of the fraction by \(a^2\). Integration reverses differentiation, so the formula is right.
:::

:::eg Find (a) \(\displaystyle\int_0^1 \frac{1}{1 + x^2}\,dx\), (b) \(\displaystyle\int \frac{1}{4 + x^2}\,dx\), (c) \(\displaystyle\int \frac{1}{3 + 2x^2}\,dx\)
(a) \(\Big[\tan^{-1}x\Big]_0^1\) \(= \dfrac\pi4 - 0 = \dfrac\pi4\).

(b) \(a = 2\): \(\tfrac12\tan^{-1}\left(\tfrac x2\right) + c\).

(c) \(\dfrac{1}{3 + 2x^2}\) \(= \dfrac12\cdot\dfrac{1}{\tfrac32 + x^2}\), so \(a^2 = \tfrac32\) and \(a = \sqrt{\tfrac32}\):
\[\frac12 \times \frac{1}{\sqrt{3/2}}\tan^{-1}\left(\frac{x}{\sqrt{3/2}}\right) + c = \frac{1}{\sqrt6}\tan^{-1}\left(\sqrt{\tfrac23}\,x\right) + c\]
:::

:::exam Integration technique
- For a definite integral, write the integrated form in square brackets with the limits, then substitute. "Exact" answers contain \(\ln\), \(e\) or \(\pi\).
- If the integrand looks like \(\sin^2 x\), \(\cos^2 x\) or \(\tan^2 x\), state the identity you use. If it is a product of two different functions of \(x\), it is a topic for [Integration techniques](#math.p3.inttech).
- For the trapezium rule, write the table of ordinates, quote the rule, and give the answer to the requested accuracy. For "over or under?", give the reason in terms of the sign of \(\dfrac{d^2y}{dx^2}\) or a sketch of the chords.
:::

:::board Other boards
Edexcel IAL covers these integrals and the trapezium rule across P2 and P3, and more integration in P4. UK A Levels (AQA, Edexcel, OCR) include them in Pure Year 2; the trapezium rule is part of their Year 2 numerical methods. Cambridge lists the trapezium rule for Paper 2 only, and \(\dfrac{1}{x^2 + a^2}\) for Paper 3 only.
:::

:::eg Spot the error: evaluate \(\displaystyle\int_0^{\pi/6}\cos 3x\,dx\)
A student wrote this answer.

Line 1: \(\displaystyle\int \cos 3x\,dx\) \(= \sin 3x\)
Line 2: \(\left[\sin 3x\right]_0^{\pi/6}\) \(= \sin\dfrac\pi2 - \sin 0 = 1\)

Line 1 integrates \(\cos\) to \(\sin\), which is the right idea. [M1] **It loses the accuracy mark [A0]:** when the inside function is \(3x\), integrating divides by \(3\), because differentiating \(\sin 3x\) multiplies by \(3\). Line 2 substitutes the limits correctly into the student's own antiderivative [M1], but the answer is wrong [A0].

Correct working: \(\displaystyle\int \cos 3x\,dx\) \(= \tfrac13\sin 3x\) [M1 A1], so the integral is \(\tfrac13\left(\sin\dfrac\pi2 - \sin 0\right)\) \(= \tfrac13\). [M1 A1]

**Check:** differentiate your answer. \(\dfrac{d}{dx}\left(\tfrac13\sin 3x\right)\) \(= \cos 3x\). ✓ The student's \(\sin 3x\) differentiates to \(3\cos 3x\), which is not the integrand.
:::

:::try Start easy, finish at exam standard
Q: Find (a) \(\displaystyle\int 4e^{-2x}\,dx\), (b) \(\displaystyle\int \frac{5}{3x - 1}\,dx\), (c) \(\displaystyle\int 3\cos(2x + 1)\,dx\), (d) \(\displaystyle\int (\sec^2 3x + 2)\,dx\).
A: (a) \(-2e^{-2x} + c\). (b) \(\tfrac53\ln|3x - 1| + c\). (c) \(\tfrac32\sin(2x + 1) + c\). (d) \(\tfrac13\tan 3x + 2x + c\).
Q: Find (a) \(\displaystyle\int (e^x + 1)^2\,dx\), (b) \(\displaystyle\int \frac{2x^2 - 3}{x}\,dx\).
A: (a) \(\displaystyle\int (e^{2x} + 2e^x + 1)\,dx\) \(= \tfrac12 e^{2x} + 2e^x + x + c\). (b) \(\displaystyle\int \left(2x - \frac3x\right)dx\) \(= x^2 - 3\ln|x| + c\).
Q: Evaluate exactly (a) \(\displaystyle\int_0^1 e^{3x}\,dx\), (b) \(\displaystyle\int_2^5 \frac{3}{x}\,dx\), (c) \(\displaystyle\int_0^{\pi/3}\sin x\,dx\).
A: (a) \(\tfrac13(e^3 - 1)\). (b) \(3\ln 5 - 3\ln 2 = 3\ln\tfrac52\). (c) \(\Big[-\cos x\Big]_0^{\pi/3}\) \(= -\tfrac12 + 1 = \tfrac12\).
Q: Find (a) \(\displaystyle\int \cos^2 x\,dx\), (b) \(\displaystyle\int_0^{\pi/2}\sin^2 3x\,dx\).
A: (a) \(\tfrac12 x + \tfrac14\sin 2x + c\). (b) \(\sin^2 3x = \tfrac12(1 - \cos 6x)\), so \(\Big[\tfrac12 x - \tfrac1{12}\sin 6x\Big]_0^{\pi/2}\) \(= \tfrac\pi4 - \tfrac{1}{12}\sin 3\pi\) \(= \dfrac\pi4\).
Q: Find (a) \(\displaystyle\int (\tan^2 x + 1)\,dx\), (b) \(\displaystyle\int_0^{\pi/4} 4\tan^2 x\,dx\).
A: (a) \(\tan^2 x + 1 = \sec^2 x\), so the integral is \(\tan x + c\). (b) \(4\Big[\tan x - x\Big]_0^{\pi/4}\) \(= 4\left(1 - \dfrac\pi4\right)\) \(= 4 - \pi\).
Q: Use the trapezium rule with 4 strips to estimate \(\displaystyle\int_1^2 \frac1x\,dx\). State whether it is an over- or underestimate and compare with \(\ln 2\).
A: \(h = 0.25\); ordinates \(1, 0.8, 0.666667, 0.571429, 0.5\). Estimate \(= 0.125\left[1.5 + 2(2.038095)\right]\) \(= 0.125 \times 5.576190 = 0.697\). The curve \(y = \tfrac1x\) is convex (\(y'' = \tfrac{2}{x^3} > 0\)), so this is an overestimate. \(\ln 2 = 0.693\). ✓
Q: The region under \(y = e^{x/2}\) from \(x = 0\) to \(x = 2\) is rotated about the \(x\)-axis. Find the exact volume.
A: \(V = \pi\displaystyle\int_0^2 e^x\,dx\) \(= \pi(e^2 - 1)\).
Q: The rate of change of the value \(V\) of a machine is \(\dfrac{dV}{dt} = -4000e^{-0.25t}\) dollars per year, with \(V = 20\,000\) at \(t = 0\). Find \(V\) in terms of \(t\) and the value after 4 years.
A: \(V = \dfrac{-4000}{-0.25}e^{-0.25t} + c\) \(= 16\,000e^{-0.25t} + c\). At \(t = 0\): \(20\,000 = 16\,000 + c\), so \(c = 4000\). After 4 years \(V = 16\,000e^{-1} + 4000 = 9886.07\), about $9890.
Q: (Paper 3) Find (a) \(\displaystyle\int \frac{6}{9 + x^2}\,dx\), (b) \(\displaystyle\int_0^{\sqrt3}\frac{1}{3 + x^2}\,dx\).
A: (a) \(6 \times \tfrac13\tan^{-1}\tfrac x3\) \(= 2\tan^{-1}\tfrac x3 + c\). (b) \(\Big[\tfrac{1}{\sqrt3}\tan^{-1}\tfrac{x}{\sqrt3}\Big]_0^{\sqrt3}\) \(= \tfrac{1}{\sqrt3}\cdot\tfrac\pi4\) \(= \dfrac{\pi}{4\sqrt3}\).
Q: (Exam style) (a) Use the trapezium rule with 4 strips to estimate \(\displaystyle\int_0^2 \sqrt{1 + x^2}\,dx\) to 3 significant figures. (b) State, with a reason, whether your estimate is an overestimate or underestimate.
A: (a) \(h = 0.5\). Ordinates: \(1\), \(\sqrt{1.25} = 1.118034\), \(\sqrt2 = 1.414214\), \(\sqrt{3.25} = 1.802776\), \(\sqrt5 = 2.236068\). [B1] Estimate
\[\begin{aligned} &= 0.25\left[1 + 2.236068 \right. \\ &\qquad \left. + 2(1.118034 + 1.414214 + 1.802776)\right] \\ &= 0.25 \times 11.906116 = 2.98 \end{aligned}\]
[M1 A1] (b) \(y = \sqrt{1 + x^2}\) has \(\dfrac{d^2y}{dx^2}\) \(= (1 + x^2)^{-3/2} > 0\), so it is convex and the estimate is an overestimate. [B1 B1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find \(\displaystyle\int \left(6e^{3x} + \frac{5}{2x + 1}\right)dx\).
A: \(\displaystyle\int 6e^{3x}\,dx\) \(= 2e^{3x}\). [B1] \(\displaystyle\int \frac{5}{2x + 1}\,dx\) \(= \tfrac52\ln|2x + 1|\). [B1] Add the constant: \(2e^{3x} + \tfrac52\ln|2x + 1| + c\). [B1]
Q: [3 marks] ★ Find the exact value of \(\displaystyle\int_0^{\pi/4}\sin 2x\,dx\).
A: \(\displaystyle\int \sin 2x\,dx\) \(= -\tfrac12\cos 2x\). [M1 A1] \(\left[-\tfrac12\cos 2x\right]_0^{\pi/4}\) \(= -\tfrac12(0) + \tfrac12(1)\) \(= \tfrac12\). [A1]
Q: [4 marks] ★★ Find the exact value of \(\displaystyle\int_0^{\pi/4}\tan^2 x\,dx\).
A: \(\tan^2 x = \sec^2 x - 1\). [M1] \(\displaystyle\int (\sec^2 x - 1)\,dx\) \(= \tan x - x\). [A1] \(\left[\tan x - x\right]_0^{\pi/4}\) \(= \left(1 - \tfrac\pi4\right) - 0\). [M1] \(= 1 - \tfrac\pi4\). [A1]
Q: [6 marks] ★★ The region \(R\) is bounded by the curve \(y = \dfrac{1}{\sqrt{2x + 1}}\), the \(x\)-axis and the lines \(x = 0\) and \(x = 4\). Find the exact volume of the solid formed when \(R\) is rotated through \(360^\circ\) about the \(x\)-axis.
A: \(V = \pi\displaystyle\int_0^4 y^2\,dx\). [M1] \(y^2 = \dfrac{1}{2x + 1}\). [A1] \(\displaystyle\int \frac{1}{2x + 1}\,dx\) \(= \tfrac12\ln(2x + 1)\). [M1 A1] \(V\) \(= \pi\left[\tfrac12\ln(2x + 1)\right]_0^4\) \(= \tfrac\pi2(\ln 9 - \ln 1)\). [M1] \(= \tfrac\pi2 \times 2\ln 3 = \pi\ln 3\). [A1]
Q: [4 marks] ★★ Use the trapezium rule with 4 strips to estimate \(\displaystyle\int_0^1 \frac{1}{1 + x^3}\,dx\), giving your answer to 3 significant figures.
A: \(h = 0.25\). [B1] The ordinates are \(1\), \(0.9846\), \(0.8889\), \(0.7033\), \(0.5\). [A1] Area
\[\begin{aligned} &\approx \tfrac12(0.25)\big[1 + 0.5 \\ &\qquad + 2(0.9846 + 0.8889 + 0.7033)\big] \end{aligned}\]
[M1] \(= 0.832\). [A1]
Q: [5 marks] ★★ The rate at which a drug is absorbed is \(\dfrac{dA}{dt} = 12e^{-0.3t}\) mg per hour, where \(t\) is the time in hours after the dose. (a) Find the total amount absorbed in the first 5 hours. (b) State the greatest total amount that can ever be absorbed.
A: (a) \(A\) \(= \displaystyle\int_0^5 12e^{-0.3t}\,dt\) \(= \left[-40e^{-0.3t}\right]_0^5\). [M1 A1] \(= 40(1 - e^{-1.5})\) [M1] \(= 31.1\) mg. [A1] (b) As \(t \to \infty\), \(e^{-0.3t} \to 0\), so the total tends to \(40\) mg. [B1]
Q: [5 marks] ★★ (Paper 3 only) Find the exact area of the region bounded by the curve \(y = \dfrac{6}{4 + x^2}\), the axes and the line \(x = 2\).
A: \(\displaystyle\int \frac{6}{4 + x^2}\,dx\) \(= 6 \times \tfrac12\tan^{-1}\left(\tfrac x2\right)\) \(= 3\tan^{-1}\left(\tfrac x2\right)\). [M1 A1] Area \(= 3\left[\tan^{-1}\left(\tfrac x2\right)\right]_0^2\) \(= 3\left(\tan^{-1}1 - \tan^{-1}0\right)\). [M1] \(\tan^{-1}1 = \tfrac\pi4\), [A1] so the area is \(\tfrac{3\pi}{4}\). [A1]
Q: [10 marks] (#math.p3.diff) ★★★ (a) Differentiate \(xe^{2x}\). (b) Hence find \(\displaystyle\int xe^{2x}\,dx\). (c) Hence find the exact value of \(\displaystyle\int_0^1 xe^{2x}\,dx\).
H: Use the product rule with \(u = x\) and \(v = e^{2x}\).
H: Your answer to (a) contains \(xe^{2x}\) and \(e^{2x}\). Integrate both sides of it, and rearrange to make \(\displaystyle\int xe^{2x}\,dx\) the subject. You know \(\displaystyle\int e^{2x}\,dx\).
H: For (c), substitute the limits into your answer to (b). Keep \(e^2\) exact.
A: (a) \(\dfrac{d}{dx}\left(xe^{2x}\right)\) \(= x \times 2e^{2x} + e^{2x} \times 1\) [M1 A1] \(= e^{2x}(2x + 1)\). [A1] (b) Integrating both sides of \(2xe^{2x} + e^{2x}\) \(= \dfrac{d}{dx}\left(xe^{2x}\right)\) gives \(2\displaystyle\int xe^{2x}\,dx + \tfrac12e^{2x}\) \(= xe^{2x}\). [M1 A1] So \(\displaystyle\int xe^{2x}\,dx\) \(= \tfrac12xe^{2x} - \tfrac14e^{2x} + c\). [M1 A1] (c) \(\left[\tfrac12xe^{2x} - \tfrac14e^{2x}\right]_0^1\) \(= \left(\tfrac12e^2 - \tfrac14e^2\right) - \left(0 - \tfrac14\right)\). [M1 A1] \(= \tfrac14e^2 + \tfrac14\) \(= \tfrac14\left(e^2 + 1\right)\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The curves \(y = \sin x\) and \(y = \sin 2x\) meet at the origin and at the point where \(x = a\), where \(0 < a < \tfrac\pi2\). (a) Find \(a\). (b) Find the exact area of the region enclosed between the two curves for \(0 \le x \le a\).
H: At a meeting point \(\sin 2x = \sin x\). Use the double angle formula and factorise; don't divide by \(\sin x\).
H: Check which curve is higher by trying a value such as \(x = \tfrac\pi6\), then integrate the upper minus the lower.
A: (a) \(2\sin x\cos x = \sin x\), so \(\sin x(2\cos x - 1) = 0\). [M1] \(\cos x = \tfrac12\), so \(a = \tfrac\pi3\). [A1] (b) At \(x = \tfrac\pi6\): \(\sin 2x = 0.866\) and \(\sin x = 0.5\), so \(\sin 2x\) is above. [B1] Area \(= \displaystyle\int_0^{\pi/3}(\sin 2x - \sin x)\,dx\) [M1] \(= \left[-\tfrac12\cos 2x + \cos x\right]_0^{\pi/3}\). [A1] \(= \left(\tfrac14 + \tfrac12\right) - \left(-\tfrac12 + 1\right)\) \(= \tfrac14\). [A1]
Q: [6 marks] ★★★ (Paper 3 only) (a) Show that \(\displaystyle\int_0^1 \frac{1}{1 + x^2}\,dx\) \(= \dfrac\pi4\). (b) Use the trapezium rule with 4 strips to estimate the integral. (c) Hence estimate \(\pi\), giving your answer to 3 significant figures.
H: The integral is \(\tan^{-1}x\) evaluated between the limits.
H: Four strips on \([0, 1]\) have width \(0.25\). Work out the five ordinates.
A: (a) \(\left[\tan^{-1}x\right]_0^1\) \(= \tan^{-1}1 - \tan^{-1}0\) [M1] \(= \tfrac\pi4\). [A1] (b) \(h = 0.25\), with ordinates \(1\), \(0.9412\), \(0.8\), \(0.64\), \(0.5\). [B1] Estimate
\[\begin{aligned} &= \tfrac12(0.25)\big[1 + 0.5 \\ &\qquad + 2(0.9412 + 0.8 + 0.64)\big] \end{aligned}\]
[M1] \(= 0.7828\). [A1] (c) \(\pi \approx 4 \times 0.7828 = 3.13\). [A1]
:::

:::quiz
? What is \(\displaystyle\int e^{4x}\,dx\)?
- \(4e^{4x} + c\)
+ \(\tfrac14 e^{4x} + c\)
- \(e^{4x} + c\)
- \(\dfrac{e^{4x+1}}{4x + 1} + c\)
> Divide by the coefficient of \(x\): \(\tfrac14 e^{4x}\). Multiplying by 4 is differentiation. The last option misapplies the power rule.
? What is \(\displaystyle\int \sin 3x\,dx\)?
- \(3\cos 3x + c\)
- \(-3\cos 3x + c\)
- \(\tfrac13\cos 3x + c\)
+ \(-\tfrac13\cos 3x + c\)
> The integral of \(\sin\) is \(-\cos\), and the inside coefficient 3 divides: \(-\tfrac13\cos 3x\). Dropping the minus sign is the most common error.
? Which is a correct first step to integrate \(\sin^2 x\)?
- \(\sin^2 x = \tfrac12(1 + \cos 2x)\)
+ \(\sin^2 x = \tfrac12(1 - \cos 2x)\)
- \(\sin^2 x = 1 + \cos^2 x\)
- \(\sin^2 x = \dfrac{\sin 2x}{2}\)
> From \(\cos 2x = 1 - 2\sin^2 x\) we get \(\sin^2 x = \tfrac12(1 - \cos 2x)\). The plus version is for \(\cos^2 x\).
? The trapezium rule is used to estimate \(\displaystyle\int_1^3 \dfrac{1}{x^2}\,dx\). Will the estimate be too high or too low?
+ Too high, because the curve is convex.
- Too low, because the curve is decreasing.
- Too high, because the curve is decreasing.
- Exactly right, because the curve is smooth.
> \(y = x^{-2}\) has \(y'' = 6x^{-4} > 0\), so it bends upwards and the chords lie above it: an overestimate. Whether the curve is increasing or decreasing is irrelevant. Only the curvature matters.
? \(\displaystyle\int_0^1 \frac{1}{1 + x^2}\,dx\) equals
- \(\ln 2\)
+ \(\dfrac\pi4\)
- \(\dfrac12\)
- \(\dfrac\pi2\)
> The integral of \(\dfrac{1}{1 + x^2}\) is \(\tan^{-1}x\), and \(\tan^{-1}1 = \dfrac\pi4\). The answer \(\ln 2\) would come from treating it like \(\int \dfrac{1}{1 + x}\,dx\).
:::

:::checklist What you can now do
- [ ] I can integrate \(e^{ax+b}\), \(\dfrac{1}{ax+b}\), \(\sin(ax+b)\), \(\cos(ax+b)\) and \(\sec^2(ax+b)\).
- [ ] I can use a trigonometric identity to integrate \(\sin^2 x\), \(\cos^2 2x\) or \(\tan^2 x\).
- [ ] I can evaluate a definite integral exactly, using \(\ln\) and \(e\) correctly.
- [ ] I can find an area, or a volume of revolution, for a curve with these functions.
- [ ] I can use the trapezium rule and say whether it over- or underestimates.
- [ ] I can integrate \(\dfrac{1}{x^2 + a^2}\) and \(\dfrac{1}{px^2 + q}\) (Paper 3 only).
- [ ] I can use a rate of change in context and integrate it to find a total.
:::

:::recap
- \(\int e^{ax+b}\,dx = \tfrac1a e^{ax+b}\); \(\int\frac{1}{ax+b}\,dx\) \(= \tfrac1a\ln|ax+b|\); \(\int\sin(ax+b)\,dx\) \(= -\tfrac1a\cos(ax+b)\); \(\int\cos(ax+b)\,dx\) \(= \tfrac1a\sin(ax+b)\); \(\int\sec^2(ax+b)\,dx\) \(= \tfrac1a\tan(ax+b)\). Add \(+\,c\).
- Expand brackets and divide quotients before integrating; never integrate products term by term.
- \(\sin^2 x = \tfrac12(1 - \cos 2x)\), \(\cos^2 x = \tfrac12(1 + \cos 2x)\), \(\tan^2 x = \sec^2 x - 1\).
- Trapezium rule: \(\tfrac12 h[y_0 + 2(y_1 + \cdots + y_{n-1}) + y_n]\). Convex curve (\(y'' > 0\)): overestimate. Concave (\(y'' < 0\)): underestimate.
- Paper 3 only: \(\int\frac{1}{x^2 + a^2}\,dx\) \(= \tfrac1a\tan^{-1}\frac xa + c\).
:::

:::links
- watch: [The trapezium rule](https://www.examsolutions.net/tutorials/trapezium-rule/) · ExamSolutions · the method and the table layout
- watch: [Exam questions: trapezium rule](https://www.examsolutions.net/tutorials/exam-questions-trapezium-rule/) · ExamSolutions · including over- and underestimates
- practise: [CAIE Pure 3 further integration exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/integration/further-integration/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [Calculus 2](https://www.khanacademy.org/math/calculus-2) · Khan Academy · integration practice with instant feedback
- papers: [9709 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-2/) · Physics & Maths Tutor · the trapezium rule is examined on Paper 2 [unofficial]

Links checked 3 October 2026.
:::
Next: [Numerical solution of equations](#math.p3.numerical).
