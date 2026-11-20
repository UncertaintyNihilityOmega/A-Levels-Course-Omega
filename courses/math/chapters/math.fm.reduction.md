@chapter math.fm.reduction
@title Reduction formulae
@level fm
@paper CAIE 9231 Paper 2
@time 5–6 hours
@summary Some integrals come in a whole family, such as \(\int_0^{\pi/2}\sin^n x\,dx\) for every \(n\). A reduction formula links one member of the family to a simpler one, so that a hard integral shrinks, step by step, to one you can do at sight. You will derive reduction formulae by parts, by an identity and from a given derivative, and use them to find exact values.

:::why
Evaluating \(\int_0^{\pi/2}\sin^8 x\,dx\) by expanding \(\sin^8 x\) is painful, and for \(\sin^{20} x\) it is hopeless. A reduction formula does it with eight lines of arithmetic, for any power, and the same idea gives exact values for integrals that have no neat antiderivative at all, such as \(\int_0^1 x^n e^{-x}\,dx\) for large \(n\). In Further Mathematics it is the standard way to deal with a whole family of integrals at once.
:::

**Before you start**, you need integration by parts from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech), the idea of a recurrence from [Proof by induction](#math.fm.induction), and the hyperbolic functions and their integrals from [Further integration: hyperbolic and inverse forms](#math.fm.integ). Volumes of revolution, from [Integration](#math.p1.integ), appear in one example.

:::try Warm-up
Q: Find \(\displaystyle\int_0^{\pi/2}x\cos x\,dx\). (from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech))
A: Take \(u = x\), \(\dfrac{dv}{dx} = \cos x\): \(\left[x\sin x\right]_0^{\pi/2} - \displaystyle\int_0^{\pi/2}\sin x\,dx = \dfrac{\pi}{2} - 1\).
Q: Differentiate \(x^2e^{-x}\). (from [Further differentiation](#math.p3.diff))
A: By the product rule, \(2xe^{-x} - x^2e^{-x} = x(2 - x)e^{-x}\).
Q: A sequence has \(u_1 = 3\) and \(u_{n+1} = 2u_n - 1\). Find \(u_4\). (from [Proof by induction](#math.fm.induction))
A: \(u_2 = 5\), \(u_3 = 9\), \(u_4 = 17\). Each term comes from the one before: that is a recurrence.
:::

## What a reduction formula is

Look at the integrals
\[\int_0^1 x e^{-x}\,dx, \qquad \int_0^1 x^2 e^{-x}\,dx, \qquad \int_0^1 x^3 e^{-x}\,dx, \quad \dots\]
Each is done by parts, and each by-parts step leaves an integral with a smaller power of \(x\). The pattern is the same every time, so it is worth doing once, for a general power \(n\), and keeping the result.

:::def Reduction formula
A formula that expresses an integral \(I_n\) in terms of the same kind of integral with a smaller index, such as \(I_{n-1}\) or \(I_{n-2}\). Applying it repeatedly reduces \(I_n\) to \(I_0\) or \(I_1\), which can be integrated directly.
:::

The letter \(I_n\) (or \(J_n\), \(T_n\), \(u_n\)) is the name of the whole integral with the number \(n\) in it. For example \(I_n = \displaystyle\int_0^1 x^ne^{-x}\,dx\) means \(I_3 = \displaystyle\int_0^1 x^3e^{-x}\,dx\). A reduction formula is a recurrence relation, like \(u_{n+1} = 2u_n - 1\) in the warm-up, whose terms are integrals.

:::steps
1. Name the family: write \(I_n = \int \dots\) with the limits.
2. Integrate by parts, taking \(u\) to be the part whose power drops when you differentiate it (or use an identity, or a given derivative).
3. Evaluate the boundary term \([uv]\) at both limits. Check each end: do not assume it is 0.
4. Rewrite what is left so that it is a multiple of \(I_{n-1}\) or \(I_{n-2}\), using an identity if needed (for example \(\cos^2x = 1 - \sin^2x\)). If \(I_n\) itself comes back, collect it on the left.
5. Rearrange to \(I_n = \dots\) and state which values of \(n\) it holds for.
6. To use it: compute the base integral (\(I_0\) or \(I_1\)) directly, then step up one line at a time.
:::

## Powers of \(x\) times an exponential

The simplest family multiplies \(x^n\) by \(e^{-x}\). Differentiating \(x^n\) lowers the power, and \(e^{-x}\) integrates without changing, so by parts does exactly what we want.

:::eg (Exam style) Let \(I_n = \displaystyle\int_0^1 x^ne^{-x}\,dx\) for \(n \ge 0\). (a) Show that \(I_n = nI_{n-1} - e^{-1}\) for \(n \ge 1\). (b) Hence find \(I_3\) in terms of \(e\).
**(a)** Take \(u = x^n\) and \(\dfrac{dv}{dx} = e^{-x}\), so \(\dfrac{du}{dx} = nx^{n-1}\) and \(v = -e^{-x}\). [M1]
\[I_n = \left[-x^ne^{-x}\right]_0^1 + n\int_0^1 x^{n-1}e^{-x}\,dx\] [A1]
At \(x = 1\) the boundary term is \(-e^{-1}\); at \(x = 0\) it is 0, because \(n \ge 1\) makes \(x^n = 0\). The remaining integral is \(I_{n-1}\), so
\[I_n = -e^{-1} + nI_{n-1}\] [A1]
**(b)** The formula needs a starting value, found directly:
\[I_0 = \int_0^1e^{-x}\,dx = \left[-e^{-x}\right]_0^1 = 1 - e^{-1}\] [B1]
Now build up one line at a time:
\[\begin{aligned}
I_1 &= 1\cdot I_0 - e^{-1} = 1 - 2e^{-1} \\
I_2 &= 2I_1 - e^{-1} = 2 - 5e^{-1} \\
I_3 &= 3I_2 - e^{-1} = 6 - 16e^{-1}
\end{aligned}\] [M1]
\[I_3 = 6 - \frac{16}{e}\] [A1]
**Check**: \(6 - \dfrac{16}{e} = 0.1139\). On \(0 \le x \le 1\) we have \(e^{-1} \le e^{-x} \le 1\), so \(I_3\) lies between \(\tfrac14e^{-1} = 0.092\) and \(\tfrac14\). It does.
:::

Why take \(u = x^n\) and not \(u = e^{-x}\)? Because the first choice makes the power fall, and the second makes it rise: with \(u = e^{-x}\) and \(\dfrac{dv}{dx} = x^n\) you would get a term in \(\displaystyle\int x^{n+1}e^{-x}\,dx\), a harder integral of the same family, which moves away from the base case. The rule for choosing is always the same: pick the part that gets **simpler** when you differentiate it as \(u\), and the part you can integrate as \(\dfrac{dv}{dx}\).

Notice that the formula gave \(I_1\) correctly without a separate by-parts step: \(n = 1\) is allowed because \(x^1 = 0\) at \(x = 0\). The formula must not be used for \(n = 0\): it would give \(I_0 = -e^{-1}\), which is wrong, because for \(n = 0\) the boundary term at \(x = 0\) is \(-1\), not 0 (\(x^0 = 1\)). That is why \(I_0\) is integrated directly.

:::warn Boundary terms
A boundary term \(\left[uv\right]_0^1\) is not automatically zero. Here the end \(x = 0\) gives 0 but the end \(x = 1\) gives \(-e^{-1}\); forgetting the second end loses the \(-e^{-1}\) in every line that follows. Evaluate both ends every time, and say why an end is 0 ("\(x^n = 0\) at \(x = 0\) for \(n \ge 1\)").
:::

Many real quantities have this shape: something rises like a power and then dies away exponentially.

:::eg (Exam style) A drug is absorbed at the rate \(12t^3e^{-t}\) milligrams per hour, \(t\) hours after it is given. Find the total absorbed in the first hour, giving your answer in terms of \(e\) and to 3 significant figures.
The total is the integral of the rate:
\[\int_0^1 12t^3e^{-t}\,dt = 12I_3\] [B1]
where \(I_3\) is the integral in the previous example. [M1]
\[12\left(6 - \frac{16}{e}\right) = 72 - \frac{192}{e}\] [A1]
This is \(1.37\) mg to 3 s.f.
:::

## Powers of sine and cosine

The most important family is \(I_n = \displaystyle\int_0^{\pi/2}\sin^nx\,dx\). Writing \(\sin^nx = \sin^{n-1}x \times \sin x\) lets you integrate \(\sin x\) and differentiate \(\sin^{n-1}x\), which lowers the power. The \(\cos^2x\) that appears is rewritten with \(\cos^2x = 1 - \sin^2x\), and that brings \(I_n\) back on the right, which is why the formula steps down by 2.

:::eg (Exam style) Let \(I_n = \displaystyle\int_0^{\pi/2}\sin^nx\,dx\) for \(n \ge 0\). (a) Show that \(I_n = \dfrac{n-1}{n}I_{n-2}\) for \(n \ge 2\). (b) Hence find \(I_5\) exactly.
**(a)** Take \(u = \sin^{n-1}x\) and \(\dfrac{dv}{dx} = \sin x\), so \(\dfrac{du}{dx} = (n-1)\sin^{n-2}x\cos x\) and \(v = -\cos x\). [M1]
\[I_n = \left[-\sin^{n-1}x\cos x\right]_0^{\pi/2} + (n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2x\,dx\] [A1]
The boundary term is 0 at both ends: at \(x = \tfrac\pi2\) because \(\cos\tfrac\pi2 = 0\), and at \(x = 0\) because \(\sin^{n-1}0 = 0\) for \(n \ge 2\). Replace \(\cos^2x\) by \(1 - \sin^2x\): [DM1]
\[\begin{aligned}
I_n &= (n-1)\int_0^{\pi/2}\left(\sin^{n-2}x - \sin^nx\right)dx \\
&= (n-1)\left(I_{n-2} - I_n\right)
\end{aligned}\]
Collect the \(I_n\) terms: \(I_n + (n-1)I_n = (n-1)I_{n-2}\), so \(nI_n = (n-1)I_{n-2}\), and
\[I_n = \frac{n-1}{n}I_{n-2}\] [A1]
**(b)** An odd index steps down to \(I_1\):
\[I_1 = \int_0^{\pi/2}\sin x\,dx = \left[-\cos x\right]_0^{\pi/2} = 1\] [B1]
\[I_5 = \tfrac45I_3 = \tfrac45 \times \tfrac23I_1\] [M1]
\[I_5 = \frac{8}{15}\] [A1]
**Check**: \(\sin^5x\) is at most \(\sin^3x\), and \(I_3 = \dfrac23 = 0.667 > 0.533 = I_5\).
:::

The formula links \(I_n\) to \(I_{n-2}\), so the chain stops at \(I_0\) when \(n\) is even and at \(I_1\) when \(n\) is odd.

:::key Integrals of \(\sin^nx\) and \(\cos^nx\) from 0 to \(\tfrac\pi2\)
\[I_n = \int_0^{\pi/2}\sin^nx\,dx = \frac{n-1}{n}I_{n-2} \qquad (n \ge 2), \qquad I_0 = \frac\pi2, \quad I_1 = 1\]
\(\displaystyle\int_0^{\pi/2}\cos^nx\,dx\) has the same value, because \(\cos x = \sin\left(\tfrac\pi2 - x\right)\) and the interval \(0\) to \(\tfrac\pi2\) is symmetric under \(x \to \tfrac\pi2 - x\).

| \(n\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| \(I_n\) | \(\dfrac\pi2\) | 1 | \(\dfrac\pi4\) | \(\dfrac23\) | \(\dfrac{3\pi}{16}\) | \(\dfrac{8}{15}\) | \(\dfrac{5\pi}{32}\) |

Even \(n\): a multiple of \(\pi\). Odd \(n\): a rational number.
:::

:::tip Test a new formula on a small value of \(n\)
Before trusting a reduction formula, try \(n = 2\) (or \(n = 1\)), where you can integrate directly. Here \(I_2 = \tfrac12I_0 = \tfrac\pi4\), and \(\int_0^{\pi/2}\sin^2x\,dx = \left[\tfrac x2 - \tfrac{\sin 2x}{4}\right]_0^{\pi/2} = \tfrac\pi4\). The two agree. A wrong sign or a wrong factor shows up at once.
:::

The next example uses the cosine version and a volume of revolution from [Integration](#math.p1.integ): the volume is \(\pi\displaystyle\int y^2\,dx\).

:::eg (Exam style) A designer models a decorative spindle. The region under \(y = \cos^3x\) for \(0 \le x \le \tfrac\pi2\), with \(x\) and \(y\) in decimetres, is rotated through \(2\pi\) radians about the \(x\)-axis. Find the exact volume, and its value in litres to 3 s.f. (1 litre is 1 cubic decimetre).
The volume is
\[V = \pi\int_0^{\pi/2}y^2\,dx = \pi\int_0^{\pi/2}\cos^6x\,dx\] [M1]
Use the reduction formula for \(n = 6\) (the cosine integral has the same values as the sine integral):
\[\begin{aligned}
\int_0^{\pi/2}\cos^6x\,dx &= \tfrac56 \times \tfrac34 \times \tfrac12 \times \int_0^{\pi/2}1\,dx \\
&= \tfrac{15}{48} \times \tfrac\pi2
\end{aligned}\] [M1]
\[\int_0^{\pi/2}\cos^6x\,dx = \frac{5\pi}{32}\] [A1]
\[V = \pi \times \frac{5\pi}{32} = \frac{5\pi^2}{32}\ \text{dm}^3 = 1.54\ \text{litres}\] [A1]
**Check**: \(\cos^3x\) is at most 1, so the solid fits inside a cylinder of radius 1 dm and length \(\tfrac\pi2\) dm, volume \(\tfrac{\pi^2}{2} = 4.93\) dm\(^3\). The answer is smaller, as it should be.
:::

:::warn Which way does the index step?
The sine and cosine formula steps down by **2**, not 1: \(I_6\) comes from \(I_4\), then \(I_2\), then \(I_0\). Writing \(I_6 = \tfrac56I_5\) is a wrong formula and earns nothing. Before you start, write the chain of indices you will use (\(6 \to 4 \to 2 \to 0\)) so you know which base value you need.
:::

### Using the sine formula after a substitution

Many integrals turn into sine or cosine powers after a substitution from [Integration techniques: parts, substitution and partial fractions](#math.p3.inttech). The reduction formula then finishes the job.

:::eg (Exam style) Use the substitution \(x = \sin\theta\) to show that \(\displaystyle\int_0^1x^5\sqrt{1-x^2}\,dx = \int_0^{\pi/2}\sin^5\theta\cos^2\theta\,d\theta\). Hence find the exact value of the integral.
With \(x = \sin\theta\): \(dx = \cos\theta\,d\theta\), \(\sqrt{1 - x^2} = \sqrt{\cos^2\theta} = \cos\theta\) (positive for \(0 \le \theta \le \tfrac\pi2\)), and the limits \(x = 0, 1\) become \(\theta = 0, \tfrac\pi2\). [M1]
\[\int_0^1x^5\sqrt{1-x^2}\,dx = \int_0^{\pi/2}\sin^5\theta\cos\theta\cos\theta\,d\theta = \int_0^{\pi/2}\sin^5\theta\cos^2\theta\,d\theta\] [A1]
Now \(\cos^2\theta = 1 - \sin^2\theta\), so the integral is \(I_5 - I_7\) in the notation of the key box: [M1]
\[\int_0^{\pi/2}\left(\sin^5\theta - \sin^7\theta\right)d\theta = I_5 - I_7\]
From the table and the chain, \(I_5 = \tfrac{8}{15}\) and \(I_7 = \tfrac67I_5 = \tfrac{16}{35}\). [B1]
\[I_5 - I_7 = \frac{56}{105} - \frac{48}{105} = \frac{8}{105}\] [A1]
**Check**: \(\tfrac{8}{105} = 0.0762\). The integrand \(x^5\sqrt{1-x^2}\) is 0 at \(x = 0\) and \(x = 1\) and at most about 0.26 (near \(x = 0.9\)), on an interval of length 1, so an area of 0.08 is sensible.
:::

### A faster way to run the chain

Because every step multiplies by a fraction, you can write the whole chain in one line, as the spindle example did. For an even index the fractions end with \(\tfrac12\) and the base value \(I_0 = \tfrac\pi2\); for an odd index they end with \(\tfrac23\) and the base value \(I_1 = 1\):
\[I_8 = \tfrac78 \times \tfrac56 \times \tfrac34 \times \tfrac12 \times \tfrac\pi2 = \frac{35\pi}{256} \qquad I_9 = \tfrac89 \times \tfrac67 \times \tfrac45 \times \tfrac23 \times 1 = \frac{128}{315}\]
Count the fractions as a check: \(I_8\) steps through \(8 \to 6 \to 4 \to 2 \to 0\), so there are four fractions; \(I_9\) steps through \(9 \to 7 \to 5 \to 3 \to 1\), so there are four fractions too. Each numerator is one less than its denominator, and the denominators are the indices you pass through.

### When the limits are not 0 and \(\tfrac\pi2\)

On \(0\) to \(\tfrac\pi2\) the boundary terms of the sine formula vanish, which is why it is so clean. With any other limits they do not, and the formula acquires an extra term that you must evaluate. The working is identical; only the boundary term changes. Without limits, the same by-parts step gives the indefinite form
\[\int\sin^nx\,dx = -\frac{\sin^{n-1}x\cos x}{n} + \frac{n-1}{n}\int\sin^{n-2}x\,dx\]
and you substitute the limits into the first term.

:::eg (Exam style) Let \(A_n = \displaystyle\int_0^{\pi/3}\sin^nx\,dx\) for \(n \ge 0\). (a) Show that \(nA_n = (n-1)A_{n-2} - \tfrac12\left(\tfrac{\sqrt3}{2}\right)^{n-1}\) for \(n \ge 2\). (b) Hence find \(A_4\) exactly.
**(a)** Take \(u = \sin^{n-1}x\) and \(\dfrac{dv}{dx} = \sin x\), so \(v = -\cos x\). [M1]
\[A_n = \left[-\sin^{n-1}x\cos x\right]_0^{\pi/3} + (n-1)\int_0^{\pi/3}\sin^{n-2}x\cos^2x\,dx\] [A1]
Replace \(\cos^2x\) by \(1 - \sin^2x\), so the integral is \(A_{n-2} - A_n\): [DM1]
\[A_n = \left[-\sin^{n-1}x\cos x\right]_0^{\pi/3} + (n-1)\left(A_{n-2} - A_n\right)\]
At \(x = \tfrac\pi3\), \(\sin x = \tfrac{\sqrt3}{2}\) and \(\cos x = \tfrac12\), so the boundary term is \(-\tfrac12\left(\tfrac{\sqrt3}{2}\right)^{n-1}\); at \(x = 0\) it is 0. Collecting \(A_n\):
\[nA_n = (n-1)A_{n-2} - \tfrac12\left(\tfrac{\sqrt3}{2}\right)^{n-1}\] [A1]
**(b)** \(A_0 = \displaystyle\int_0^{\pi/3}1\,dx = \tfrac\pi3\). [B1]
\[\begin{aligned}
2A_2 &= A_0 - \tfrac12 \times \tfrac{\sqrt3}{2} = \tfrac\pi3 - \tfrac{\sqrt3}{4} \\
4A_4 &= 3A_2 - \tfrac12 \times \tfrac{3\sqrt3}{8} = \tfrac\pi2 - \tfrac{3\sqrt3}{8} - \tfrac{3\sqrt3}{16}
\end{aligned}\] [M1]
\[A_4 = \frac\pi8 - \frac{9\sqrt3}{64}\] [A1]
**Check**: \(\displaystyle\int\sin^4x\,dx = \tfrac{3x}{8} - \tfrac{\sin 2x}{4} + \tfrac{\sin 4x}{32}\); at \(\tfrac\pi3\) this is \(\tfrac\pi8 - \tfrac{\sqrt3}{8} - \tfrac{\sqrt3}{64}\), which equals the answer.
:::

## Powers of tan: an identity instead of parts

Not every family needs integration by parts. For \(T_n = \displaystyle\int_0^{\pi/4}\tan^nx\,dx\), use \(\tan^2x = \sec^2x - 1\) to split off a piece that integrates at sight, because \(\sec^2x\) is the derivative of \(\tan x\).

:::eg (Exam style) Let \(T_n = \displaystyle\int_0^{\pi/4}\tan^nx\,dx\) for \(n \ge 0\). (a) Show that \(T_n + T_{n-2} = \dfrac{1}{n-1}\) for \(n \ge 2\). (b) Hence find \(T_5\) exactly.
**(a)** Write \(\tan^nx = \tan^{n-2}x\left(\sec^2x - 1\right)\), so
\[T_n = \int_0^{\pi/4}\tan^{n-2}x\sec^2x\,dx - \int_0^{\pi/4}\tan^{n-2}x\,dx\] [M1]
The first integral has the form \(\int u^{n-2}\,du\) with \(u = \tan x\):
\[\int_0^{\pi/4}\tan^{n-2}x\sec^2x\,dx = \left[\frac{\tan^{n-1}x}{n-1}\right]_0^{\pi/4}\] [A1]
At \(x = \tfrac\pi4\), \(\tan x = 1\), and at \(x = 0\) it is 0, so this equals \(\dfrac{1}{n-1}\). Hence \(T_n = \dfrac{1}{n-1} - T_{n-2}\), that is
\[T_n + T_{n-2} = \frac{1}{n-1}\] [A1]
**(b)** The chain \(5 \to 3 \to 1\) stops at \(T_1\):
\[T_1 = \int_0^{\pi/4}\tan x\,dx = \left[\ln\sec x\right]_0^{\pi/4} = \ln\sqrt2 = \tfrac12\ln 2\] [B1]
\[\begin{aligned}
T_3 &= \tfrac12 - T_1 = \tfrac12 - \tfrac12\ln 2 \\
T_5 &= \tfrac14 - T_3 = -\tfrac14 + \tfrac12\ln 2
\end{aligned}\] [M1]
\[T_5 = \tfrac12\ln 2 - \tfrac14\] [A1]
**Check**: \(\tfrac12\ln 2 - \tfrac14 = 0.0966\), small and positive, as \(\tan^5x \le 1\) and is tiny for most of the interval.
:::

Here the formula has a **plus** sign between the two integrals. You subtract to isolate the one you want: \(T_n = \dfrac{1}{n-1} - T_{n-2}\). The even chain ends at \(T_0 = \tfrac\pi4\).

## Powers of sec: using a given derivative

In harder cases the question hands you the idea. The syllabus example is \(\displaystyle\int_0^{\pi/4}\sec^nx\,dx\), "by considering \(\dfrac{d}{dx}\left(\tan x\sec^{n-2}x\right)\)". The method is always the same: differentiate the expression you are given, simplify, integrate between the limits, and rearrange.

:::eg (Exam style) Let \(J_n = \displaystyle\int_0^{\pi/4}\sec^nx\,dx\). (a) Show that \(\dfrac{d}{dx}\left(\tan x\sec^{n-2}x\right) = (n-1)\sec^nx - (n-2)\sec^{n-2}x\). (b) Hence show that \((n-1)J_n = 2^{\frac{n-2}{2}} + (n-2)J_{n-2}\) for \(n \ge 2\). (c) Find the exact value of \(\displaystyle\int_0^{\pi/4}\sec^6x\,dx\).
**(a)** Use the product rule, with \(\dfrac{d}{dx}\sec^{n-2}x = (n-2)\sec^{n-2}x\tan x\):
\[\begin{aligned}
\frac{d}{dx}\left(\tan x\sec^{n-2}x\right) &= \sec^2x \cdot \sec^{n-2}x + \tan x \cdot (n-2)\sec^{n-2}x\tan x \\
&= \sec^nx + (n-2)\tan^2x\sec^{n-2}x
\end{aligned}\] [M1 A1]
Replace \(\tan^2x\) by \(\sec^2x - 1\): [DM1]
\[\begin{aligned}
&= \sec^nx + (n-2)\left(\sec^nx - \sec^{n-2}x\right) \\
&= (n-1)\sec^nx - (n-2)\sec^{n-2}x
\end{aligned}\] [A1]
**(b)** Integrate both sides from 0 to \(\tfrac\pi4\):
\[\left[\tan x\sec^{n-2}x\right]_0^{\pi/4} = (n-1)J_n - (n-2)J_{n-2}\] [M1]
At \(\tfrac\pi4\), \(\tan x = 1\) and \(\sec x = \sqrt2\), so the bracket is \(\left(\sqrt2\right)^{n-2} = 2^{\frac{n-2}{2}}\); at 0 it is \(0 \times 1 = 0\). [A1]
\[(n-1)J_n = 2^{\frac{n-2}{2}} + (n-2)J_{n-2}\] [A1]
**(c)** \(J_2 = \displaystyle\int_0^{\pi/4}\sec^2x\,dx = \left[\tan x\right]_0^{\pi/4} = 1\). [B1]
\[\begin{aligned}
J_4 &= \tfrac13\left(2^1 + 2J_2\right) = \tfrac43 \\
J_6 &= \tfrac15\left(2^2 + 4J_4\right) = \tfrac15\left(4 + \tfrac{16}{3}\right)
\end{aligned}\] [M1]
\[J_6 = \frac{28}{15}\] [A1]
**Check**: \(\displaystyle\int\sec^4x\,dx = \tan x + \tfrac13\tan^3x\), which gives \(1 + \tfrac13 = \tfrac43\) for \(J_4\).
:::

When the question gives you a derivative, do not look for another method. Differentiate it exactly as written; the formula to prove is always what you get after one use of an identity.

## Other families

The same six steps work for any family where a power drops under differentiation. Here are three more, each with its own twist.

### Powers of \(\ln x\)

Differentiating \((\ln x)^n\) gives \(n(\ln x)^{n-1}\times\dfrac1x\), and the \(\dfrac1x\) cancels the \(x\) that comes from integrating 1. Take \(\dfrac{dv}{dx} = 1\).

:::eg (Exam style) Let \(L_n = \displaystyle\int_1^e(\ln x)^n\,dx\). (a) Show that \(L_n = e - nL_{n-1}\) for \(n \ge 1\). (b) Hence find \(L_3\) exactly.
**(a)** Take \(u = (\ln x)^n\) and \(\dfrac{dv}{dx} = 1\), so \(\dfrac{du}{dx} = \dfrac{n(\ln x)^{n-1}}{x}\) and \(v = x\). [M1]
\[L_n = \left[x(\ln x)^n\right]_1^e - n\int_1^e(\ln x)^{n-1}\,dx\] [A1]
At \(x = e\), \(\ln e = 1\), so the boundary term is \(e \times 1 = e\); at \(x = 1\), \(\ln 1 = 0\), so it is 0. Hence
\[L_n = e - nL_{n-1}\] [A1]
**(b)** \(L_0 = \displaystyle\int_1^e1\,dx = e - 1\). [B1]
\[\begin{aligned}
L_1 &= e - L_0 = 1 \\
L_2 &= e - 2L_1 = e - 2 \\
L_3 &= e - 3L_2 = 6 - 2e
\end{aligned}\] [M1]
\[L_3 = 6 - 2e\] [A1]
**Check**: \(6 - 2e = 0.563\). On \(1 \le x \le e\), \(0 \le \ln x \le 1\), so \(\left(\ln x\right)^3\) is below \(\ln x\), and \(L_1 = 1\) is bigger. It is.
:::

### A root: \(x^n\sqrt{1-x}\)

Here you integrate the root, not the power, so the power of \(x\) drops. A new idea is needed: \((1-x)^{3/2}\) is not a multiple of \(\sqrt{1-x}\), but \((1-x)^{3/2} = (1-x)\sqrt{1-x}\), and splitting it makes \(K_n\) reappear.

:::eg (Exam style) Let \(K_n = \displaystyle\int_0^1x^n\sqrt{1-x}\,dx\). (a) Show that \(K_n = \dfrac{2n}{2n+3}K_{n-1}\) for \(n \ge 1\). (b) Hence find \(\displaystyle\int_0^1x^3\sqrt{1-x}\,dx\).
**(a)** Take \(u = x^n\) and \(\dfrac{dv}{dx} = (1-x)^{1/2}\), so \(\dfrac{du}{dx} = nx^{n-1}\) and \(v = -\tfrac23(1-x)^{3/2}\). [M1]
\[K_n = \left[-\tfrac23x^n(1-x)^{3/2}\right]_0^1 + \tfrac{2n}{3}\int_0^1x^{n-1}(1-x)^{3/2}\,dx\] [A1]
The boundary term is 0 at both ends: \((1-x)^{3/2} = 0\) at \(x = 1\), and \(x^n = 0\) at \(x = 0\). [B1]
Write \((1-x)^{3/2} = (1-x)(1-x)^{1/2}\), so the integral is \(\displaystyle\int_0^1\left(x^{n-1} - x^n\right)(1-x)^{1/2}dx = K_{n-1} - K_n\): [M1]
\[K_n = \tfrac{2n}{3}\left(K_{n-1} - K_n\right)\]
\[\left(1 + \tfrac{2n}{3}\right)K_n = \tfrac{2n}{3}K_{n-1}, \quad\text{so}\quad K_n = \frac{2n}{2n+3}K_{n-1}\] [A1]
**(b)** \(K_0 = \displaystyle\int_0^1(1-x)^{1/2}\,dx = \left[-\tfrac23(1-x)^{3/2}\right]_0^1 = \tfrac23\). [B1]
\[\begin{aligned}
K_1 &= \tfrac25 \times \tfrac23 = \tfrac{4}{15} \\
K_2 &= \tfrac47 \times \tfrac{4}{15} = \tfrac{16}{105} \\
K_3 &= \tfrac69 \times \tfrac{16}{105}
\end{aligned}\] [M1]
\[K_3 = \frac{32}{315}\] [A1]
**Check** for \(K_1\) by substituting \(w = 1 - x\): \(\displaystyle\int_0^1(1-w)\sqrt w\,dw = \tfrac23 - \tfrac25 = \tfrac{4}{15}\).
:::

### Hyperbolic powers

The hyperbolic functions follow the circular ones, with one sign change: \(\cosh^2x = 1 + \sinh^2x\), not \(1 - \sinh^2x\). Use the identities from [Hyperbolic functions](#math.fm.hyperbolic). Because the limit is \(\ln 2\), the values \(\cosh(\ln 2) = \tfrac54\) and \(\sinh(\ln 2) = \tfrac34\) come from the exponential definitions.

:::eg (Exam style) Let \(C_n = \displaystyle\int_0^{\ln 2}\cosh^nx\,dx\). (a) Show that \(nC_n = \tfrac34\left(\tfrac54\right)^{n-1} + (n-1)C_{n-2}\) for \(n \ge 2\). (b) Hence find \(C_4\) exactly.
**(a)** Take \(u = \cosh^{n-1}x\) and \(\dfrac{dv}{dx} = \cosh x\), so \(\dfrac{du}{dx} = (n-1)\cosh^{n-2}x\sinh x\) and \(v = \sinh x\). [M1]
\[C_n = \left[\cosh^{n-1}x\sinh x\right]_0^{\ln 2} - (n-1)\int_0^{\ln 2}\cosh^{n-2}x\sinh^2x\,dx\] [A1]
Replace \(\sinh^2x\) by \(\cosh^2x - 1\): [DM1]
\[\begin{aligned}
C_n &= \left[\cosh^{n-1}x\sinh x\right]_0^{\ln 2} - (n-1)\left(C_n - C_{n-2}\right)
\end{aligned}\]
The boundary term is \(\left(\tfrac54\right)^{n-1}\tfrac34\) at \(\ln 2\) and 0 at 0, because \(\sinh 0 = 0\). Collect \(C_n\): \(C_n + (n-1)C_n = \tfrac34\left(\tfrac54\right)^{n-1} + (n-1)C_{n-2}\), so
\[nC_n = \tfrac34\left(\tfrac54\right)^{n-1} + (n-1)C_{n-2}\] [A1]
**(b)** \(C_0 = \displaystyle\int_0^{\ln 2}1\,dx = \ln 2\). [B1]
\[\begin{aligned}
2C_2 &= \tfrac34 \times \tfrac54 + C_0 = \tfrac{15}{16} + \ln 2 \\
4C_4 &= \tfrac34\left(\tfrac54\right)^3 + 3C_2 = \tfrac{375}{256} + \tfrac{3}{2}\left(\tfrac{15}{16} + \ln 2\right)
\end{aligned}\] [M1]
\[C_4 = \frac{735}{1024} + \tfrac38\ln 2\] [A1]
**Check**: \(\tfrac{735}{1024} + \tfrac38\ln 2 = 0.978\). On \(0 \le x \le \ln 2\), \(\cosh^4x\) lies between 1 and \(\left(\tfrac54\right)^4 = 2.44\), and the interval has length 0.693, so \(C_4\) lies between 0.69 and 1.69.
:::

The same working for \(S_n = \displaystyle\int_0^a\sinh^nx\,dx\) uses \(\dfrac{dv}{dx} = \sinh x\), \(v = \cosh x\) and \(\cosh^2x = 1 + \sinh^2x\), and gives \(nS_n = \sinh^{n-1}a\cosh a - (n-1)S_{n-2}\), with a minus sign where the cosh version has a plus. You will derive it in the practice questions.

:::key Which method for which family
| Family | Method | Steps in \(n\) |
|---|---|---|
| \(x^ne^{\pm x}\), \(x^n\sin x\), \(x^n\cos x\) | by parts, \(u = x^n\) | \(n \to n-1\) (\(n \to n-2\) for sine and cosine, which need two parts) |
| \(\sin^nx\), \(\cos^nx\) | by parts, then \(\cos^2 = 1 - \sin^2\) | \(n \to n-2\) |
| \(\tan^nx\) | \(\tan^2 = \sec^2 - 1\), no parts | \(n \to n-2\) |
| \(\sec^nx\) | derivative of \(\tan x\sec^{n-2}x\) | \(n \to n-2\) |
| \((\ln x)^n\) | by parts, \(\dfrac{dv}{dx} = 1\) | \(n \to n-1\) |
| \(x^n\sqrt{1-x}\) | by parts, then split \((1-x)^{3/2}\) | \(n \to n-1\) |
| \(\cosh^nx\), \(\sinh^nx\) | by parts, then \(\cosh^2 = 1 + \sinh^2\) | \(n \to n-2\) |
:::

:::exam Wording, accuracy and method marks
"Show that" means every line of the derivation is marked, so write the by-parts choice (\(u = \dots\), \(\dfrac{dv}{dx} = \dots\)), the boundary term with both ends, and the rearrangement. "Hence" means you must use the formula you have just proved. Give exact answers (fractions, \(\pi\), \(e\), \(\ln 2\)) unless asked for a decimal. None of these formulae is on MF19: you must derive or learn them. Never "fudge" towards a printed answer: if your result disagrees with the given one, look for the slip, because examiners see a sign that changes from nowhere.
:::

:::board
This chapter follows the Cambridge 9231 syllabus (outcome 2.4b). Further Maths specifications from other boards place further integration in different units and may not ask for hints in the same way, so check the content list of your own specification to see which of these families you need.
:::

:::eg Spot the error: Let \(I_n = \displaystyle\int_0^1x^ne^{-x}\,dx\). Show that \(I_n = nI_{n-1} - e^{-1}\) for \(n \ge 1\) [3 marks].
A student wrote this answer.

Line 1: \(u = x^n\), \(\dfrac{dv}{dx} = e^{-x}\), \(\dfrac{du}{dx} = nx^{n-1}\), \(v = e^{-x}\)
Line 2: \(I_n = \left[x^ne^{-x}\right]_0^1 - n\displaystyle\int_0^1x^{n-1}e^{-x}\,dx\)
Line 3: \(I_n = e^{-1} - nI_{n-1}\)
Line 4: "This is not the printed answer, so I changed the signs": \(I_n = nI_{n-1} - e^{-1}\).

Lines 1 and 2 use the right method: parts with \(u = x^n\), so the student earns the method mark. [M1]

**Line 1 contains the slip, and it costs the accuracy marks.** The integral of \(e^{-x}\) is \(-e^{-x}\), not \(e^{-x}\): the minus sign from the chain rule was dropped. Line 2 is therefore wrong. [A0] Line 4 is a fudge: nothing in the working produces the changed signs, so the final mark is not earned. [A0] The student scores 1 out of 3.

Correct line 1: \(v = -e^{-x}\). Then line 2 reads \(I_n = \left[-x^ne^{-x}\right]_0^1 + n\displaystyle\int_0^1x^{n-1}e^{-x}\,dx\) [A1], and evaluating the boundary term gives \(-e^{-1}\), so \(I_n = nI_{n-1} - e^{-1}\) with no fudge. [A1]

**Check** the sign with \(n = 1\): \(I_1 = \displaystyle\int_0^1xe^{-x}\,dx = 1 - 2e^{-1} = 0.264\), and \(1\cdot I_0 - e^{-1} = 1 - 2e^{-1}\). The wrong version, \(e^{-1} - I_0 = 2e^{-1} - 1 = -0.264\), is negative, which is impossible for a positive integrand.
:::

:::try Start easy, finish at exam standard
Q: Let \(I_n = \displaystyle\int_0^{\pi/2}\sin^nx\,dx\). Use \(I_n = \dfrac{n-1}{n}I_{n-2}\) to find \(I_7\).
A: \(I_7 = \tfrac67 \times \tfrac45 \times \tfrac23 \times I_1\) with \(I_1 = 1\), so \(I_7 = \dfrac{48}{105} = \dfrac{16}{35}\).
Q: Let \(U_n = \displaystyle\int_0^1x^ne^{3x}\,dx\). Show that \(U_n = \tfrac13e^3 - \tfrac n3U_{n-1}\) and find \(U_2\) exactly.
A: Take \(u = x^n\), \(v = \tfrac13e^{3x}\): \(U_n = \left[\tfrac13x^ne^{3x}\right]_0^1 - \tfrac n3U_{n-1} = \tfrac13e^3 - \tfrac n3U_{n-1}\).
\(U_0 = \tfrac13\left(e^3 - 1\right)\), then \(U_1 = \tfrac13e^3 - \tfrac13U_0 = \tfrac19\left(2e^3 + 1\right)\), then \(U_2 = \tfrac13e^3 - \tfrac23U_1 = \tfrac{1}{27}\left(5e^3 - 2\right)\).
Q: Let \(T_n = \displaystyle\int_0^{\pi/4}\tan^nx\,dx\). Use \(T_n + T_{n-2} = \dfrac{1}{n-1}\) to find \(T_6\) exactly.
A: \(T_0 = \tfrac\pi4\). \(T_2 = 1 - \tfrac\pi4\), \(T_4 = \tfrac13 - T_2 = \tfrac\pi4 - \tfrac23\), \(T_6 = \tfrac15 - T_4 = \tfrac{13}{15} - \tfrac\pi4\).
Q: Use \(2J_3 = \sqrt2 + J_1\), from \((n-1)J_n = 2^{\frac{n-2}{2}} + (n-2)J_{n-2}\), and \(J_1 = \ln\left(1 + \sqrt2\right)\) to find \(\displaystyle\int_0^{\pi/4}\sec^3x\,dx\) to 3 s.f.
A: \(J_3 = \tfrac12\left(\sqrt2 + \ln\left(1 + \sqrt2\right)\right) = \tfrac12(1.4142 + 0.8814) = 1.15\).
Q: With \(L_n = \displaystyle\int_1^e(\ln x)^n\,dx\) and \(L_n = e - nL_{n-1}\), find \(L_5\) exactly, given \(L_3 = 6 - 2e\).
A: \(L_4 = e - 4L_3 = 9e - 24\), then \(L_5 = e - 5L_4 = 120 - 44e\).
Q: With \(K_n = \displaystyle\int_0^1x^n\sqrt{1-x}\,dx\) and \(K_n = \dfrac{2n}{2n+3}K_{n-1}\), find \(K_4\), given \(K_3 = \dfrac{32}{315}\).
A: \(K_4 = \tfrac{8}{11} \times \tfrac{32}{315} = \dfrac{256}{3465}\).
Q: Use \(nC_n = \tfrac34\left(\tfrac54\right)^{n-1} + (n-1)C_{n-2}\) to find \(\displaystyle\int_0^{\ln 2}\cosh^3x\,dx\).
A: \(C_1 = \sinh(\ln 2) = \tfrac34\). \(3C_3 = \tfrac34 \times \tfrac{25}{16} + 2 \times \tfrac34 = \tfrac{75}{64} + \tfrac{96}{64} = \tfrac{171}{64}\), so \(C_3 = \dfrac{57}{64}\).
Q: Without calculating, find \(\displaystyle\int_0^{\pi/2}\sin^{10}x\,dx \div \int_0^{\pi/2}\sin^8x\,dx\).
A: The ratio is \(\dfrac{I_{10}}{I_8} = \dfrac{10-1}{10} = \dfrac{9}{10}\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Given that \(I_n = \displaystyle\int_0^{\pi/2}\cos^nx\,dx\) satisfies \(I_n = \dfrac{n-1}{n}I_{n-2}\) for \(n \ge 2\), find \(I_9\) exactly.
A: \(I_9 = \tfrac89 \times \tfrac67 \times \tfrac45 \times \tfrac23 \times I_1\) [M1] and \(I_1 = \displaystyle\int_0^{\pi/2}\cos x\,dx = 1\). [B1]
\(I_9 = \dfrac{384}{945} = \dfrac{128}{315}\). [A1]
Q: [6 marks] ★★ Let \(E_n = \displaystyle\int_0^1x^ne^{2x}\,dx\) for \(n \ge 0\). (a) Show that \(E_n = \tfrac12e^2 - \tfrac n2E_{n-1}\) for \(n \ge 1\). (b) Hence find \(E_2\) exactly.
A: (a) Take \(u = x^n\) and \(\dfrac{dv}{dx} = e^{2x}\), so \(v = \tfrac12e^{2x}\). [M1]
\[E_n = \left[\tfrac12x^ne^{2x}\right]_0^1 - \tfrac n2\int_0^1x^{n-1}e^{2x}\,dx\] [A1]
The boundary term is \(\tfrac12e^2 - 0\), so \(E_n = \tfrac12e^2 - \tfrac n2E_{n-1}\). [A1]
(b) \(E_0 = \left[\tfrac12e^{2x}\right]_0^1 = \tfrac12\left(e^2 - 1\right)\). [B1]
\[\begin{aligned}
E_1 &= \tfrac12e^2 - \tfrac12E_0 = \tfrac14\left(e^2 + 1\right) \\
E_2 &= \tfrac12e^2 - E_1
\end{aligned}\] [M1]
\(E_2 = \dfrac14\left(e^2 - 1\right)\). [A1]
Q: [7 marks] ★★ Let \(Q_n = \displaystyle\int_0^{\pi/2}x^n\cos x\,dx\) for \(n \ge 0\). (a) Show that \(Q_n = \left(\tfrac\pi2\right)^n - n(n-1)Q_{n-2}\) for \(n \ge 2\). (b) Hence find \(Q_2\) exactly.
A: (a) First by parts with \(u = x^n\), \(\dfrac{dv}{dx} = \cos x\): [M1]
\[Q_n = \left[x^n\sin x\right]_0^{\pi/2} - n\int_0^{\pi/2}x^{n-1}\sin x\,dx = \left(\tfrac\pi2\right)^n - n\int_0^{\pi/2}x^{n-1}\sin x\,dx\] [A1]
Second by parts on the remaining integral, with \(u = x^{n-1}\), \(\dfrac{dv}{dx} = \sin x\): [DM1]
\[\int_0^{\pi/2}x^{n-1}\sin x\,dx = \left[-x^{n-1}\cos x\right]_0^{\pi/2} + (n-1)\int_0^{\pi/2}x^{n-2}\cos x\,dx = (n-1)Q_{n-2}\]
because \(\cos\tfrac\pi2 = 0\) and \(x^{n-1} = 0\) at \(x = 0\) for \(n \ge 2\). Hence \(Q_n = \left(\tfrac\pi2\right)^n - n(n-1)Q_{n-2}\). [A1]
(b) \(Q_0 = \displaystyle\int_0^{\pi/2}\cos x\,dx = 1\). [B1]
\(Q_2 = \left(\tfrac\pi2\right)^2 - 2Q_0\) [M1] \(= \dfrac{\pi^2}{4} - 2\). [A1]
Q: [7 marks] ★★ Let \(S_n = \displaystyle\int_0^{\ln 3}\sinh^nx\,dx\). (a) Show that \(nS_n = \tfrac53\left(\tfrac43\right)^{n-1} - (n-1)S_{n-2}\) for \(n \ge 2\). (b) Hence find \(S_2\) exactly.
A: (a) Take \(u = \sinh^{n-1}x\) and \(\dfrac{dv}{dx} = \sinh x\), so \(v = \cosh x\). [M1]
\[S_n = \left[\sinh^{n-1}x\cosh x\right]_0^{\ln 3} - (n-1)\int_0^{\ln 3}\sinh^{n-2}x\cosh^2x\,dx\] [A1]
Replace \(\cosh^2x\) by \(1 + \sinh^2x\): the integral becomes \(S_{n-2} + S_n\). [DM1]
At \(\ln 3\): \(\sinh = \tfrac{3 - 1/3}{2} = \tfrac43\) and \(\cosh = \tfrac{3 + 1/3}{2} = \tfrac53\); at 0 the term is 0. So \(S_n = \tfrac53\left(\tfrac43\right)^{n-1} - (n-1)\left(S_{n-2} + S_n\right)\), which rearranges to the result. [A1]
(b) \(S_0 = \ln 3\). [B1]
\(2S_2 = \tfrac53 \times \tfrac43 - S_0\) [M1], so \(S_2 = \dfrac{10}{9} - \tfrac12\ln 3\). [A1]
Q: [10 marks] (#math.p3.inttech) ★★★ Let \(I_n = \displaystyle\int_0^1\left(1 - x^2\right)^n\,dx\) for \(n \ge 0\). (a) Show that \(I_n = \dfrac{2n}{2n+1}I_{n-1}\) for \(n \ge 1\). (b) Hence find \(I_3\). (c) Use the substitution \(x = \sin\theta\) to show that \(I_n = \displaystyle\int_0^{\pi/2}\cos^{2n+1}\theta\,d\theta\).
H: For (a), integrate by parts with \(u = \left(1 - x^2\right)^n\) and \(\dfrac{dv}{dx} = 1\), so \(v = x\).
H: In the new integral you will meet \(x^2\): write it as \(1 - \left(1 - x^2\right)\).
H: For (c), \(dx = \cos\theta\,d\theta\), and \(1 - \sin^2\theta = \cos^2\theta\).
A: (a) With \(u = \left(1 - x^2\right)^n\), \(v = x\): [M1]
\[I_n = \left[x\left(1 - x^2\right)^n\right]_0^1 + 2n\int_0^1x^2\left(1 - x^2\right)^{n-1}\,dx\] [A1]
The boundary term is 0 at both ends. Write \(x^2 = 1 - \left(1 - x^2\right)\): [DM1]
\[I_n = 2n\left(I_{n-1} - I_n\right), \quad\text{so}\quad (2n + 1)I_n = 2nI_{n-1}\] [A1]
(b) \(I_0 = 1\). [B1]
\(I_3 = \tfrac67 \times \tfrac45 \times \tfrac23 \times I_0\) [M1] \(= \dfrac{16}{35}\). [A1]
(c) \(x = \sin\theta\) gives \(dx = \cos\theta\,d\theta\) and \(\left(1 - x^2\right)^n = \cos^{2n}\theta\). [M1]
The limits \(x = 0, 1\) become \(\theta = 0, \tfrac\pi2\). [B1]
So \(I_n = \displaystyle\int_0^{\pi/2}\cos^{2n}\theta\cos\theta\,d\theta = \int_0^{\pi/2}\cos^{2n+1}\theta\,d\theta\). [A1]
(Check: for \(n = 3\) this is \(\int_0^{\pi/2}\cos^7\theta\,d\theta = \tfrac{16}{35}\), the same as (b).)
Q: [9 marks] (#math.fm.induction) ★★★ Let \(u_n = \displaystyle\int_0^{\pi/2}\sin^{2n}x\,dx\) for \(n \ge 0\). Given that \(I_m = \dfrac{m-1}{m}I_{m-2}\), where \(I_m = \displaystyle\int_0^{\pi/2}\sin^mx\,dx\): (a) show that \(u_n = \dfrac{2n-1}{2n}u_{n-1}\). (b) Prove by induction that \(u_n = \dfrac{(2n)!\,\pi}{2^{2n+1}(n!)^2}\) for all integers \(n \ge 0\). (c) Find \(\displaystyle\int_0^{\pi/2}\sin^{10}x\,dx\).
H: In (a), put \(m = 2n\).
H: In the inductive step multiply the numerator and the denominator by \(2k + 2\), so that \((2k+1)(2k+2)(2k)!\) becomes \((2k+2)!\).
H: For (c), \(10 = 2n\) with \(n = 5\).
A: (a) Put \(m = 2n\): \(I_{2n} = \dfrac{2n-1}{2n}I_{2n-2}\), that is \(u_n = \dfrac{2n-1}{2n}u_{n-1}\). [M1 A1]
(b) For \(n = 0\): \(u_0 = \tfrac\pi2\) and the formula gives \(\dfrac{0!\,\pi}{2 \times 1} = \tfrac\pi2\). So true for \(n = 0\). [B1]
Assume true for \(n = k\): \(u_k = \dfrac{(2k)!\,\pi}{2^{2k+1}(k!)^2}\). [B1]
Then
\[u_{k+1} = \frac{2k+1}{2k+2}u_k = \frac{(2k+1)(2k)!\,\pi}{(2k+2)\,2^{2k+1}(k!)^2}\] [M1]
Multiply the top and bottom by \(2k + 2\):
\[u_{k+1} = \frac{(2k+2)!\,\pi}{(2k+2)^2\,2^{2k+1}(k!)^2} = \frac{(2k+2)!\,\pi}{2^{2k+3}\left((k+1)!\right)^2}\] [A1]
because \((2k+2)^2(k!)^2 = 4\left((k+1)!\right)^2\). This is the formula with \(n = k + 1\). So true for \(n = k + 1\); true for \(n = 0\), hence by induction true for all integers \(n \ge 0\). [A1]
(c) \(\displaystyle\int_0^{\pi/2}\sin^{10}x\,dx = u_5 = \dfrac{10!\,\pi}{2^{11}(5!)^2}\) [M1] \(= \dfrac{63\pi}{512}\). [A1]
Q: [12 marks] (#math.p1.integ) ★★★ Let \(V_n = \displaystyle\int_{\pi/6}^{\pi/2}\operatorname{cosec}^nx\,dx\) for \(n \ge 0\). (a) Show that \(\dfrac{d}{dx}\left(\cot x\operatorname{cosec}^{n-2}x\right) = (n-2)\operatorname{cosec}^{n-2}x - (n-1)\operatorname{cosec}^nx\). (b) Hence show that \((n-1)V_n = 2^{n-2}\sqrt3 + (n-2)V_{n-2}\) for \(n \ge 2\). (c) Find \(V_4\) exactly. (d) The region under \(y = \operatorname{cosec}^2x\) for \(\tfrac\pi6 \le x \le \tfrac\pi2\) is rotated through \(2\pi\) about the \(x\)-axis. Find the exact volume.
H: Use the product rule, with \(\dfrac{d}{dx}\cot x = -\operatorname{cosec}^2x\) and \(\dfrac{d}{dx}\operatorname{cosec}x = -\operatorname{cosec}x\cot x\). Then use \(\cot^2x = \operatorname{cosec}^2x - 1\).
H: At \(x = \tfrac\pi6\), \(\cot x = \sqrt3\) and \(\operatorname{cosec}x = 2\). At \(x = \tfrac\pi2\), \(\cot x = 0\).
H: For (c), start from \(V_2 = \left[-\cot x\right]\) between the limits. For (d), the volume is \(\pi\displaystyle\int y^2\,dx\).
A: (a)
\[\begin{aligned}
\frac{d}{dx}\left(\cot x\operatorname{cosec}^{n-2}x\right) &= -\operatorname{cosec}^2x\operatorname{cosec}^{n-2}x \\
&\quad + \cot x \cdot (n-2)\operatorname{cosec}^{n-2}x\left(-\cot x\right) \\
&= -\operatorname{cosec}^nx - (n-2)\cot^2x\operatorname{cosec}^{n-2}x
\end{aligned}\] [M1 A1]
Replace \(\cot^2x\) by \(\operatorname{cosec}^2x - 1\): [DM1]
\[= -\operatorname{cosec}^nx - (n-2)\operatorname{cosec}^nx + (n-2)\operatorname{cosec}^{n-2}x = (n-2)\operatorname{cosec}^{n-2}x - (n-1)\operatorname{cosec}^nx\] [A1]
(b) Integrate from \(\tfrac\pi6\) to \(\tfrac\pi2\): \(\left[\cot x\operatorname{cosec}^{n-2}x\right] = (n-2)V_{n-2} - (n-1)V_n\). [M1]
At \(\tfrac\pi2\) the bracket is 0; at \(\tfrac\pi6\) it is \(\sqrt3 \times 2^{n-2}\). So the bracket is \(0 - \sqrt3 \times 2^{n-2}\). [A1]
Hence \(-\sqrt3 \times 2^{n-2} = (n-2)V_{n-2} - (n-1)V_n\), so \((n-1)V_n = 2^{n-2}\sqrt3 + (n-2)V_{n-2}\). [A1]
(c) \(V_2 = \left[-\cot x\right]_{\pi/6}^{\pi/2} = 0 + \sqrt3 = \sqrt3\). [B1]
\(3V_4 = 4\sqrt3 + 2V_2 = 6\sqrt3\) [M1], so \(V_4 = 2\sqrt3\). [A1]
(d) \(V = \pi\displaystyle\int_{\pi/6}^{\pi/2}\left(\operatorname{cosec}^2x\right)^2dx = \pi V_4\) [M1] \(= 2\sqrt3\,\pi\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ Let \(I_n = \displaystyle\int_0^{\pi/2}\sin^nx\,dx\). (a) Show that \(nI_nI_{n-1} = (n-1)I_{n-1}I_{n-2}\) for \(n \ge 2\). (b) Deduce that \(I_nI_{n-1} = \dfrac{\pi}{2n}\) for \(n \ge 1\). (c) By comparing \(I_{n-1}\), \(I_n\) and \(I_{n+1}\) on the interval, show that \(\sqrt{\dfrac{\pi}{2(n+1)}} \le I_n \le \sqrt{\dfrac{\pi}{2n}}\).
H: Multiply both sides of \(nI_n = (n-1)I_{n-2}\) by \(I_{n-1}\). The quantity \(nI_nI_{n-1}\) then does not change as \(n\) changes.
H: On \(0 \le x \le \tfrac\pi2\), \(0 \le \sin x \le 1\), so each power of \(\sin x\) is at most the one before it. What does that say about \(I_{n+1} \le I_n \le I_{n-1}\)?
A: (a) Multiply \(nI_n = (n-1)I_{n-2}\) by \(I_{n-1}\). [M1] This gives \(nI_nI_{n-1} = (n-1)I_{n-1}I_{n-2}\). [A1]
(b) Let \(P_n = nI_nI_{n-1}\). Part (a) says \(P_n = P_{n-1}\) for \(n \ge 2\), so \(P_n = P_1 = 1 \times I_1I_0\) [M1] \(= 1 \times \tfrac\pi2\). [B1]
So \(nI_nI_{n-1} = \tfrac\pi2\), that is \(I_nI_{n-1} = \dfrac{\pi}{2n}\). [A1]
(c) For \(0 \le \sin x \le 1\), \(\sin^{n+1}x \le \sin^nx \le \sin^{n-1}x\), so \(I_{n+1} \le I_n \le I_{n-1}\). [B1]
Then \(I_n^2 \le I_nI_{n-1} = \dfrac{\pi}{2n}\), giving the upper bound. [M1]
And \(I_n^2 \ge I_nI_{n+1} = \dfrac{\pi}{2(n+1)}\), giving the lower bound. [A1]
(Check with \(n = 10\): \(I_{10} = \tfrac{63\pi}{512} = 0.3866\), between \(\sqrt{\pi/22} = 0.3779\) and \(\sqrt{\pi/20} = 0.3963\).)
Q: [6 marks] ★★★ Let \(V_{m,n} = \displaystyle\int_0^1x^m(1-x)^n\,dx\) for integers \(m, n \ge 0\). (a) By parts, show that \(V_{m,n} = \dfrac{n}{m+1}V_{m+1,n-1}\) for \(n \ge 1\). (b) Hence find \(V_{4,3}\).
H: Here the index \(m\) goes **up** while \(n\) goes down. Take \(u = (1-x)^n\) and \(\dfrac{dv}{dx} = x^m\).
H: Apply the formula three times, until the second index is 0.
A: (a) With \(u = (1-x)^n\) and \(v = \dfrac{x^{m+1}}{m+1}\): [M1]
\[V_{m,n} = \left[\frac{x^{m+1}(1-x)^n}{m+1}\right]_0^1 + \frac{n}{m+1}\int_0^1x^{m+1}(1-x)^{n-1}\,dx\] [A1]
The boundary term is 0 at both ends (\(n \ge 1\)), and the integral is \(V_{m+1,n-1}\). [B1]
(b) \(V_{4,3} = \tfrac35V_{5,2} = \tfrac35 \times \tfrac26V_{6,1} = \tfrac35 \times \tfrac26 \times \tfrac17V_{7,0}\) [M1]
\(V_{7,0} = \displaystyle\int_0^1x^7\,dx = \tfrac18\). [B1]
\(V_{4,3} = \dfrac{6}{210} \times \dfrac18 = \dfrac{1}{280}\). [A1]
:::

:::quiz
? Which is the reduction formula for \(I_n = \displaystyle\int_0^{\pi/2}\sin^nx\,dx\)?
+ \(I_n = \dfrac{n-1}{n}I_{n-2}\)
- \(I_n = \dfrac{n-1}{n}I_{n-1}\)
- \(I_n = \dfrac{n}{n-1}I_{n-2}\)
- \(I_n = (n-1)I_{n-2}\)
> The by-parts step leaves \(\sin^{n-2}x\cos^2x\), which is why the index drops by 2, and collecting \(I_n\) gives \(nI_n = (n-1)I_{n-2}\). Stepping by 1 is the classic slip; the other two forget to move the \(n\).
? For \(I_n = \displaystyle\int_0^1x^ne^{-x}\,dx\) with \(n \ge 1\), what is the boundary term \(\left[-x^ne^{-x}\right]_0^1\)?
+ \(-e^{-1}\)
- \(0\)
- \(e^{-1}\)
- \(-1\)
> At \(x = 1\) it is \(-e^{-1}\); at \(x = 0\) it is 0 because \(x^n = 0\). The term is not 0 overall (that is the habit of sine integrals, where both ends vanish), and its sign is negative because \(v = -e^{-x}\).
? To evaluate \(\displaystyle\int_0^{\pi/2}\sin^7x\,dx\) with \(I_n = \dfrac{n-1}{n}I_{n-2}\), which value ends the chain?
+ \(I_1 = 1\)
- \(I_0 = \dfrac\pi2\)
- \(I_2 = \dfrac\pi4\)
- \(I_{-1}\), found from the formula
> The chain \(7 \to 5 \to 3 \to 1\) steps down by 2, so it ends at \(I_1\). The formula holds only for \(n \ge 2\); there is no \(I_{-1}\) in it, and \(I_0\) belongs to the even chain.
? For \(T_n = \displaystyle\int_0^{\pi/4}\tan^nx\,dx\), which is correct for \(n \ge 2\)?
+ \(T_n + T_{n-2} = \dfrac{1}{n-1}\)
- \(T_n - T_{n-2} = \dfrac{1}{n-1}\)
- \(T_n + T_{n-2} = \dfrac{1}{n}\)
- \(T_n = \dfrac{n-1}{n}T_{n-2}\)
> From \(\tan^n = \tan^{n-2}\left(\sec^2 - 1\right)\): the first part integrates to \(\dfrac{\tan^{n-1}x}{n-1}\), which is \(\dfrac{1}{n-1}\) between the limits. The sign comes from \(\sec^2 - 1\); the last option is the sine formula.
? In the proof of the \(\sec^n\) formula, what does \(\tan^2x\sec^{n-2}x\) become?
+ \(\sec^nx - \sec^{n-2}x\)
- \(\sec^{n-2}x - 1\)
- \(\sec^nx + \sec^{n-2}x\)
- \(\left(\sec x - 1\right)^n\)
> Replace \(\tan^2x\) by \(\sec^2x - 1\) and multiply by \(\sec^{n-2}x\): \(\sec^2x\sec^{n-2}x = \sec^nx\). The sign is minus because \(\tan^2 = \sec^2 - 1\), and the other options mis-handle the powers.
? A student finds \(I_3\) from \(I_n = nI_{n-1} - e^{-1}\) starting from \(I_0 = 1\). What is wrong?
+ \(I_0 = \displaystyle\int_0^1e^{-x}\,dx = 1 - e^{-1}\), not 1
- The formula cannot start at \(I_0\), only at \(I_1\)
- \(I_0 = 0\) because the power of \(x\) is 0
- Nothing: \(I_0 = 1\) because \(x^0 = 1\)
> The base case is the integral itself, \(\int_0^1 e^{-x}\,dx\), and the factor \(x^0 = 1\) does not make it equal to 1. The formula is valid from \(n = 1\), which needs \(I_0\); every later value is wrong if \(I_0\) is wrong.
:::

:::checklist What you can now do
- [ ] I can say what \(I_n\) means and what a reduction formula does, and use one to step down to a base case.
- [ ] I can derive a reduction formula by parts for \(x^ne^{\pm x}\), \(x^n\sin x\), \(x^n\cos x\), \((\ln x)^n\) and \(x^n\sqrt{1-x}\), evaluating the boundary terms correctly.
- [ ] I can derive and use the reduction formula for \(\int_0^{\pi/2}\sin^nx\,dx\), and for the cosine integral.
- [ ] I can derive reduction formulae for \(\tan^nx\) (by an identity) and \(\sec^nx\) (from a given derivative).
- [ ] I can derive and use reduction formulae for \(\cosh^nx\) and \(\sinh^nx\).
- [ ] I can adapt the sine formula when the limits are not 0 and \(\tfrac\pi2\), so that a boundary term survives.
- [ ] I can find an exact value of a definite integral from a reduction formula and a base case.
- [ ] I can use a reduction formula in a context, such as a volume of revolution.
- [ ] I can state the range of \(n\) for which a formula holds, and test it on a small value of \(n\).
:::

:::recap
- A reduction formula links \(I_n\) to \(I_{n-1}\) or \(I_{n-2}\); apply it down to \(I_0\) or \(I_1\), found directly.
- By parts: choose \(u\) to be the part whose power falls; evaluate **both** ends of the boundary term; if \(I_n\) reappears, collect it.
- \(\displaystyle\int_0^{\pi/2}\sin^nx\,dx = \dfrac{n-1}{n}\int_0^{\pi/2}\sin^{n-2}x\,dx\), with \(I_0 = \dfrac\pi2\), \(I_1 = 1\); the cosine integral is the same.
- \(\displaystyle\int_0^1x^ne^{-x}\,dx\): \(I_n = nI_{n-1} - e^{-1}\) with \(I_0 = 1 - e^{-1}\).
- \(T_n + T_{n-2} = \dfrac{1}{n-1}\) for \(\displaystyle\int_0^{\pi/4}\tan^nx\,dx\); \(\sec^n\): differentiate \(\tan x\sec^{n-2}x\) and use \(\tan^2 = \sec^2 - 1\).
- \((\ln x)^n\): \(L_n = e - nL_{n-1}\) on \([1, e]\). \(\cosh^n\) uses \(\sinh^2 = \cosh^2 - 1\); \(\sinh^n\) uses \(\cosh^2 = 1 + \sinh^2\).
- "Show that" earns marks line by line; "hence" means use the result; answers are exact; never fudge a sign.
:::

:::links
- practise: [Further integration booklets](https://madasmaths.com/archive_maths_booklets_further_topics_integration.html) · MadAsMaths · free booklets with answers on reduction formulae, arc length and surface area
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · worked video solutions by topic, including integration
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]
- practise: [9231 papers by year](https://www.savemyexams.com/a-level/further-maths/cie/past-papers/) · Save My Exams · past papers to try once you can derive each formula

Links checked 20 November 2026.
:::
Next: [Sums, rectangles and bounds](#math.fm.rectangles) shows how areas of rectangles under a curve give inequalities and limits for sums such as \(\sum \frac1r\).
