@chapter math.p3.trig
@title Further trigonometry
@level as
@paper CAIE P2/P3 · Edexcel IAL P3 · AQA/OCR/Edexcel Pure Year 2
@time 9–11 hours
@summary The reciprocal functions secant, cosecant and cotangent and their graphs; the identities \(\sec^2\theta \equiv 1 + \tan^2\theta\) and \(\operatorname{cosec}^2\theta \equiv 1 + \cot^2\theta\); compound angle and double angle formulae; and writing \(a\sin\theta + b\cos\theta\) as \(R\sin(\theta \pm \alpha)\) or \(R\cos(\theta \pm \alpha)\), with exact values, proofs and equations.

:::why
The identities in this chapter let you rewrite one trigonometric expression as another. That is what turns an equation you cannot solve into one you can, and what makes integrals of \(\sin^2 x\) possible later. The \(R\sin(\theta + \alpha)\) form combines two waves into one, which is how engineers find the strength of an alternating current and the maximum height of a tide. Almost all the formulae here are on MF19 (the \(R\)-form is the exception), so the skill is knowing which to use and when.
:::

**Before you start**, you need [Trigonometry](#math.p1.trig): exact values, the unit circle, the graphs of sine, cosine and tangent, and solving equations in an interval. Factorising quadratics from [Quadratics](#math.p1.quadratics) is used in the equations.

## Secant, cosecant and cotangent

The three reciprocal functions are defined from the main ones.

:::def Secant, cosecant, cotangent
\[\sec\theta = \frac{1}{\cos\theta} \qquad \operatorname{cosec}\theta = \frac{1}{\sin\theta} \qquad \cot\theta = \frac{1}{\tan\theta} = \frac{\cos\theta}{\sin\theta}\]
Each is undefined where its denominator is zero: \(\sec\theta\) when \(\cos\theta = 0\) (at \(90^\circ, 270^\circ, \ldots\)), \(\operatorname{cosec}\theta\) and \(\cot\theta\) when \(\sin\theta = 0\) (at \(0^\circ, 180^\circ, 360^\circ, \ldots\)).
:::

The calculator has no sec, cosec or cot keys: use the reciprocal. So \(\sec 40^\circ = \dfrac{1}{\cos 40^\circ} = 1.305\). To solve \(\sec\theta = 3\), solve \(\cos\theta = \dfrac13\).

:::plot The graphs of \(y = \sec x\) and \(y = \operatorname{cosec} x\). Each has vertical asymptotes where the matching sine or cosine is zero, and no values between −1 and 1.
--f "1/cos(x)" --f "1/sin(x)" --label "y = sec x" --label "y = cosec x" --deg --x 0 360 --y -4 4 --xstep 90 --legend tr
:::

:::plot The graph of \(y = \cot x\). It has asymptotes at 0°, 180° and 360°, passes through (90°, 0) and (270°, 0), and has period 180°.
--f "1/tan(x)" --label "y = cot x" --deg --x 0 360 --y -4 4 --xstep 90 --legend tr
:::

:::key Features of the reciprocal graphs
- \(y = \sec x\): period \(360^\circ\), symmetrical about the \(y\)-axis, passes through \((0, 1)\); \(|\sec x| \ge 1\), so the range is \(y \le -1\) or \(y \ge 1\). Minimum points at the maxima of cosine.
- \(y = \operatorname{cosec} x\): period \(360^\circ\); \(|\operatorname{cosec} x| \ge 1\). It is the graph of \(\sec x\) shifted \(90^\circ\) to the right.
- \(y = \cot x\): period \(180^\circ\), range all real values, decreasing between asymptotes.
- Where the original function is \(\pm 1\), its reciprocal is also \(\pm 1\): the curves touch there.
:::

### Two more Pythagorean identities

Divide \(\sin^2\theta + \cos^2\theta = 1\) by \(\cos^2\theta\) to get \(\tan^2\theta + 1 = \sec^2\theta\). Divide by \(\sin^2\theta\) to get \(1 + \cot^2\theta = \operatorname{cosec}^2\theta\).

:::key Identities
\[\sec^2\theta \equiv 1 + \tan^2\theta \qquad \operatorname{cosec}^2\theta \equiv 1 + \cot^2\theta\]
Together with \(\sin^2\theta + \cos^2\theta \equiv 1\), these are on MF19. Use \(\sec^2\theta\) to turn an equation containing both \(\sec\theta\) and \(\tan\theta\) into a quadratic in \(\sec\theta\) alone (and \(\operatorname{cosec}\theta\), \(\cot\theta\) likewise).
:::

:::eg Solve \(2\tan^2 x + \sec x = 1\) for \(0^\circ \le x \le 360^\circ\).
Replace \(\tan^2 x\) by \(\sec^2 x - 1\):
\[\begin{aligned} 2(\sec^2 x - 1) + \sec x &= 1 \\ 2\sec^2 x + \sec x - 3 &= 0 \\ (2\sec x + 3)(\sec x - 1) &= 0 \end{aligned}\]
So \(\sec x = 1\) or \(\sec x = -\tfrac32\). Take reciprocals: \(\cos x = 1\) gives \(x = 0^\circ, 360^\circ\). \(\cos x = -\tfrac23\) gives \(x = 131.8^\circ\) and \(360^\circ - 131.8^\circ = 228.2^\circ\). The solutions are \(0^\circ, 131.8^\circ, 228.2^\circ, 360^\circ\).
:::

:::eg Solve \(\cot^2\theta + 3\operatorname{cosec}\theta - 3 = 0\) for \(0^\circ < \theta < 360^\circ\).
Replace \(\cot^2\theta\) by \(\operatorname{cosec}^2\theta - 1\): \(\operatorname{cosec}^2\theta + 3\operatorname{cosec}\theta - 4 = 0\), so \((\operatorname{cosec}\theta + 4)(\operatorname{cosec}\theta - 1) = 0\).

\(\operatorname{cosec}\theta = 1\) gives \(\sin\theta = 1\), so \(\theta = 90^\circ\). \(\operatorname{cosec}\theta = -4\) gives \(\sin\theta = -\tfrac14\), so \(\theta = 180^\circ + 14.5^\circ = 194.5^\circ\) or \(360^\circ - 14.5^\circ = 345.5^\circ\).
:::

## Compound angle formulae

A common mistake is to believe \(\sin(A + B) = \sin A + \sin B\). Test it: \(\sin 90^\circ = 1\), but \(\sin 60^\circ + \sin 30^\circ = 0.866 + 0.5 = 1.366\). The correct formulae are:

:::formula Compound angles
\[\sin(A \pm B) = \sin A\cos B \pm \cos A\sin B\]
\[\cos(A \pm B) = \cos A\cos B \mp \sin A\sin B\]
\[\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A\tan B}\]
Take care with the signs: in the cosine formula the sign in the middle is **opposite** to the sign in the bracket (\(\cos(A + B)\) has a minus). All three are on MF19.
:::

The main uses are exact values for angles that are sums or differences of \(30^\circ\), \(45^\circ\), \(60^\circ\), \(90^\circ\), and rewriting expressions to solve equations.

:::eg Find the exact values of \(\sin 75^\circ\) and \(\tan 105^\circ\).
Write \(75^\circ = 45^\circ + 30^\circ\):
\[\sin 75^\circ = \sin 45^\circ\cos 30^\circ + \cos 45^\circ\sin 30^\circ = \frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2} + \frac{\sqrt2}{2}\cdot\frac12 = \frac{\sqrt6 + \sqrt2}{4}\]
Write \(105^\circ = 60^\circ + 45^\circ\):
\[\tan 105^\circ = \frac{\tan 60^\circ + \tan 45^\circ}{1 - \tan 60^\circ\tan 45^\circ} = \frac{\sqrt3 + 1}{1 - \sqrt3} = \frac{(\sqrt3 + 1)(1 + \sqrt3)}{(1 - \sqrt3)(1 + \sqrt3)} = \frac{4 + 2\sqrt3}{-2} = -(2 + \sqrt3)\]
Check: \(\sin 75^\circ = 0.9659\) and \(\tfrac{\sqrt6 + \sqrt2}{4} = 0.9659\). ✓
:::

:::eg Angle \(A\) is acute with \(\sin A = \tfrac35\), and angle \(B\) is obtuse with \(\cos B = -\tfrac{5}{13}\). Find \(\sin(A + B)\).
Draw or use \(\sin^2 + \cos^2 = 1\): \(\cos A = \tfrac45\) (positive, acute) and \(\sin B = \tfrac{12}{13}\) (positive, obtuse).
\[\sin(A + B) = \sin A\cos B + \cos A\sin B = \tfrac35\left(-\tfrac5{13}\right) + \tfrac45\cdot\tfrac{12}{13} = \frac{-15 + 48}{65} = \frac{33}{65}\]
:::

:::eg Solve \(\sin(x + 30^\circ) = 2\cos x\) for \(0^\circ \le x \le 360^\circ\).
Expand the left side: \(\sin x\cos 30^\circ + \cos x\sin 30^\circ = 2\cos x\), so \(\dfrac{\sqrt3}{2}\sin x + \dfrac12\cos x = 2\cos x\). Collect: \(\dfrac{\sqrt3}{2}\sin x = \dfrac32\cos x\). Divide by \(\cos x\). This is safe, because if \(\cos x\) were zero the equation would force \(\sin x = 0\) too, which is impossible:
\[\tan x = \frac{3}{\sqrt3} = \sqrt3\]
So \(x = 60^\circ\) or \(240^\circ\).
:::

## Double angle formulae

Put \(B = A\) in the compound formulae.

:::formula Double angles
\[\sin 2A = 2\sin A\cos A\]
\[\cos 2A = \cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A\]
\[\tan 2A = \frac{2\tan A}{1 - \tan^2 A}\]
There are three forms of \(\cos 2A\). Choose the one that leaves the same function as the rest of your equation. All are on MF19.
:::

:::eg Given \(\sin\theta = \tfrac35\) with \(\theta\) acute, find \(\sin 2\theta\), \(\cos 2\theta\) and \(\tan 2\theta\).
\(\cos\theta = \tfrac45\), so \(\sin 2\theta = 2 \times \tfrac35 \times \tfrac45 = \tfrac{24}{25}\). Using \(\cos 2\theta = 1 - 2\sin^2\theta = 1 - 2 \times \tfrac{9}{25} = \tfrac{7}{25}\). Then \(\tan 2\theta = \dfrac{24/25}{7/25} = \tfrac{24}{7}\).
Check: \(\left(\tfrac{24}{25}\right)^2 + \left(\tfrac7{25}\right)^2 = \tfrac{576 + 49}{625} = 1\). ✓
:::

:::eg Solve (a) \(\cos 2x + 3\sin x = 2\) for \(0^\circ \le x \le 360^\circ\), (b) \(\sin 2x = \cos x\) for \(-\pi \le x \le \pi\).
(a) Use \(\cos 2x = 1 - 2\sin^2 x\), because the other term is \(\sin x\):
\[\begin{aligned} 1 - 2\sin^2 x + 3\sin x &= 2 \\ 2\sin^2 x - 3\sin x + 1 &= 0 \\ (2\sin x - 1)(\sin x - 1) &= 0 \end{aligned}\]
So \(\sin x = \tfrac12\) gives \(x = 30^\circ, 150^\circ\), and \(\sin x = 1\) gives \(x = 90^\circ\). The solutions are \(30^\circ, 90^\circ, 150^\circ\).

(b) \(2\sin x\cos x = \cos x\), so \(\cos x(2\sin x - 1) = 0\). Do **not** divide by \(\cos x\). Either \(\cos x = 0\), giving \(x = \pm\dfrac{\pi}{2}\), or \(\sin x = \tfrac12\), giving \(x = \dfrac{\pi}{6}\) and \(\dfrac{5\pi}{6}\). Four solutions: \(x = -\dfrac{\pi}{2}, \dfrac{\pi}{6}, \dfrac{\pi}{2}, \dfrac{5\pi}{6}\).
:::

### Proving identities with the new formulae

Use the same approach as before: start from one side, change it step by step. Look for \(1 + \cos 2\theta = 2\cos^2\theta\) and \(1 - \cos 2\theta = 2\sin^2\theta\). These come straight from the forms of \(\cos 2\theta\).

:::eg (Exam style) (a) Show that \(\operatorname{cosec}2\theta + \cot 2\theta \equiv \cot\theta\). (b) Hence find the exact value of \(\cot 15^\circ\).
**(a)** Write everything in sine and cosine of \(2\theta\):
\[\operatorname{cosec}2\theta + \cot 2\theta = \frac{1}{\sin 2\theta} + \frac{\cos 2\theta}{\sin 2\theta} = \frac{1 + \cos 2\theta}{\sin 2\theta}\] [M1]
Use \(1 + \cos 2\theta = 2\cos^2\theta\) and \(\sin 2\theta = 2\sin\theta\cos\theta\):
\[= \frac{2\cos^2\theta}{2\sin\theta\cos\theta}\] [M1 A1]
\[= \frac{\cos\theta}{\sin\theta} = \cot\theta\] ∎ [A1]

**(b)** Put \(\theta = 15^\circ\): \(\cot 15^\circ = \operatorname{cosec}30^\circ + \cot 30^\circ = 2 + \sqrt3\). [M1 A1]
Check: \(\tan 15^\circ = 0.2679\) and \(1 \div 0.2679 = 3.732 = 2 + \sqrt3\). ✓
:::

:::eg (Exam style) (a) Show that \(\tan(\theta + 45^\circ) \equiv \dfrac{1 + \tan\theta}{1 - \tan\theta}\). (b) Hence solve \(\tan(\theta + 45^\circ) = 6\tan\theta\) for \(0^\circ \le \theta \le 180^\circ\).
**(a)** \(\tan(\theta + 45^\circ) = \dfrac{\tan\theta + \tan 45^\circ}{1 - \tan\theta\tan 45^\circ}\) [M1] and \(\tan 45^\circ = 1\), so the result is \(\dfrac{1 + \tan\theta}{1 - \tan\theta}\). ∎ [A1]

**(b)** Let \(t = \tan\theta\). Then \(\dfrac{1 + t}{1 - t} = 6t\), so \(1 + t = 6t - 6t^2\). [M1]
\[6t^2 - 5t + 1 = 0 \implies (2t - 1)(3t - 1) = 0\] [M1 A1]
So \(\tan\theta = \tfrac12\) or \(\tan\theta = \tfrac13\), giving \(\theta = 26.6^\circ\) or \(18.4^\circ\). [A1]
Check \(t = \tfrac12\): \(\dfrac{1.5}{0.5} = 3 = 6 \times \tfrac12\). ✓
:::

## The form \(R\sin(\theta \pm \alpha)\)

Two waves of the same frequency, \(a\sin\theta\) and \(b\cos\theta\), add up to a single wave. Compare \(R\sin(\theta + \alpha) = R\sin\theta\cos\alpha + R\cos\theta\sin\alpha\) with \(a\sin\theta + b\cos\theta\). Matching coefficients gives \(R\cos\alpha = a\) and \(R\sin\alpha = b\). Squaring and adding gives \(R^2 = a^2 + b^2\); dividing gives \(\tan\alpha = \dfrac{b}{a}\).

:::key Harmonic form
For \(a > 0\) and \(b > 0\):
\[a\sin\theta + b\cos\theta = R\sin(\theta + \alpha) \qquad R = \sqrt{a^2 + b^2},\ \tan\alpha = \dfrac{b}{a}\]
\[a\cos\theta + b\sin\theta = R\cos(\theta - \alpha) \qquad R = \sqrt{a^2 + b^2},\ \tan\alpha = \dfrac{b}{a}\]
With a minus sign in the expression, expand \(R\sin(\theta - \alpha)\) or \(R\cos(\theta + \alpha)\) and match in the same way. Choose \(R > 0\) and an acute \(\alpha\). To get \(\alpha\) right, write \(R\cos\alpha = \dots\) and \(R\sin\alpha = \dots\) first, then check the quadrant.
:::

:::eg Express \(3\sin\theta + 4\cos\theta\) in the form \(R\sin(\theta + \alpha)\), and \(2\sin\theta - \cos\theta\) in the form \(R\sin(\theta - \alpha)\).
Match \(3\sin\theta + 4\cos\theta = R\sin\theta\cos\alpha + R\cos\theta\sin\alpha\): \(R\cos\alpha = 3\), \(R\sin\alpha = 4\). Then \(R = \sqrt{9 + 16} = 5\) and \(\tan\alpha = \tfrac43\), so \(\alpha = 53.13^\circ\):
\[3\sin\theta + 4\cos\theta = 5\sin(\theta + 53.13^\circ)\]
For the second, \(R\sin(\theta - \alpha) = R\sin\theta\cos\alpha - R\cos\theta\sin\alpha\). Match: \(R\cos\alpha = 2\), \(R\sin\alpha = 1\). So \(R = \sqrt5\) and \(\tan\alpha = \tfrac12\), \(\alpha = 26.57^\circ\):
\[2\sin\theta - \cos\theta = \sqrt5\sin(\theta - 26.57^\circ)\]
:::

Once in this form, the expression has a single \(\sin\) or \(\cos\). Its greatest value is \(R\) and its least value is \(-R\). It also becomes easy to solve.

:::plot The curve \(y = 3\sin\theta + 4\cos\theta\) is a sine wave of amplitude 5. The equation \(3\sin\theta + 4\cos\theta = 2.5\) has two solutions in 0° to 360°: 96.9° and 336.9°.
--f "3*sin(x)+4*cos(x)" --label "y = 3 sin θ + 4 cos θ" --deg --x 0 360 --y -6 6 --xstep 90 --hline 2.5 --pt "96.87,2.5,(96.9°, 2.5)@ne" --pt "336.87,2.5,(336.9°, 2.5)@nw" --legend tr
:::

:::eg Solve \(3\sin\theta + 4\cos\theta = 2.5\) for \(0^\circ \le \theta \le 360^\circ\). State the greatest value of \(3\sin\theta + 4\cos\theta\) and the value of \(\theta\) at which it occurs.
Use \(5\sin(\theta + 53.13^\circ) = 2.5\), so \(\sin(\theta + 53.13^\circ) = 0.5\). The angle \(u = \theta + 53.13^\circ\) lies between \(53.13^\circ\) and \(413.13^\circ\). Then \(u = 30^\circ\) (too small), \(150^\circ\) or \(390^\circ\). So \(\theta = 96.87^\circ\) or \(336.87^\circ\), which is \(96.9^\circ\) or \(336.9^\circ\).

The greatest value is \(5\), when \(\sin(\theta + 53.13^\circ) = 1\): \(\theta + 53.13^\circ = 90^\circ\), so \(\theta = 36.87^\circ\) (36.9°).
:::

:::eg Two alternating currents in the same circuit are \(I_1 = 3\sin\theta\) amperes and \(I_2 = 4\cos\theta\) amperes, where \(\theta\) is the phase angle. Find the amplitude of the total current \(I = I_1 + I_2\).
\(I = 3\sin\theta + 4\cos\theta = 5\sin(\theta + 53.13^\circ)\). The amplitude, the greatest value of \(I\), is \(5\) amperes, which is not \(3 + 4 = 7\) because the two currents peak at different times.
:::

:::eg (Exam style) (a) Express \(7\cos\theta - 24\sin\theta\) in the form \(R\cos(\theta + \alpha)\), where \(R > 0\) and \(0^\circ < \alpha < 90^\circ\). (b) Solve \(7\cos\theta - 24\sin\theta = 10\) for \(0^\circ \le \theta \le 360^\circ\). (c) Find the least value of \(\dfrac{40}{30 + 7\cos\theta - 24\sin\theta}\).
**(a)** \(R\cos(\theta + \alpha) = R\cos\theta\cos\alpha - R\sin\theta\sin\alpha\). Match: \(R\cos\alpha = 7\), \(R\sin\alpha = 24\). [M1]
\[R = \sqrt{49 + 576} = 25, \quad \tan\alpha = \tfrac{24}{7} \implies \alpha = 73.74^\circ\] [A1 A1]
So \(7\cos\theta - 24\sin\theta = 25\cos(\theta + 73.74^\circ)\).

**(b)** \(25\cos(\theta + 73.74^\circ) = 10\), so \(\cos(\theta + 73.74^\circ) = 0.4\). [M1] The angle \(u = \theta + 73.74^\circ\) is between \(73.74^\circ\) and \(433.74^\circ\). The principal value is \(66.42^\circ\) (too small), and other solutions are \(360^\circ - 66.42^\circ = 293.58^\circ\) and \(360^\circ + 66.42^\circ = 426.42^\circ\). [M1]
\[\theta = 219.8^\circ \text{ or } 352.7^\circ\] [A1 A1]

**(c)** \(7\cos\theta - 24\sin\theta\) ranges from \(-25\) to \(25\), so the denominator \(30 + \ldots\) ranges from \(5\) to \(55\). [M1] The fraction is least when the denominator is greatest: \(\dfrac{40}{55} = \dfrac{8}{11}\). [A1]
:::

:::warn Trig traps in this chapter
- \(\sin(A + B) \ne \sin A + \sin B\), and \(\cos 2A \ne 2\cos A\). Use the formulae.
- The sign in \(\cos(A \pm B)\) is the opposite of the one in the bracket.
- In \(a\sin\theta + b\cos\theta = R\sin(\theta + \alpha)\), \(\tan\alpha = \dfrac ba\) (b over a, not a over b). Check the final form by putting in \(\theta = 0\).
- When the equation reads \(\sin 2x = \cos x\) or \(\tan 2x = 3\tan x\), factorise rather than dividing, otherwise you lose the solutions where the divisor is zero.
- Work with the whole angle: for \(R\sin(\theta + \alpha) = k\), change the interval to \(\alpha\) to \(360^\circ + \alpha\).
:::

:::exam Technique
- State the formula you use ("using \(\cos 2\theta = 1 - 2\sin^2\theta\)"). Method marks depend on it.
- "Exact" means surds like \(\dfrac{\sqrt6 + \sqrt2}{4}\), not decimals. Show the sum or difference of known angles (e.g. \(75^\circ = 45^\circ + 30^\circ\)).
- For the \(R\)-form, give \(R\) exactly if it is a surd and \(\alpha\) to 1 d.p. (or 3 s.f. in radians) unless told otherwise. Keep the full calculator value for later steps.
- For "hence" questions, use the given result: do not start again from the original equation.
:::

:::board Other boards
Edexcel IAL covers sec, cosec, cot, the compound and double angle formulae and the \(R\)-form in P3, and the UK A Levels (AQA, Edexcel, OCR) cover them in Pure Year 2. Small-angle approximations appear in UK specifications but are not in the Cambridge syllabus. In Cambridge 9709 the compound angle, double angle and Pythagorean identities are all on MF19, but the \(R\)-form is not: you derive it each time.
:::

:::try Start easy, finish at exam standard
Q: Find, to 3 significant figures, (a) \(\sec 50^\circ\), (b) \(\cot 20^\circ\), (c) \(\operatorname{cosec} 1.2\) (radians).
A: (a) \(\dfrac{1}{\cos 50^\circ} = 1.56\). (b) \(\dfrac{1}{\tan 20^\circ} = 2.75\). (c) \(\dfrac{1}{\sin 1.2} = 1.07\).
Q: Solve \(\sec\theta = -2.5\) for \(0^\circ \le \theta \le 360^\circ\).
A: \(\cos\theta = -0.4\), so \(\theta = 113.6^\circ\) or \(246.4^\circ\).
Q: Solve \(\tan^2\theta = 3 + \sec\theta\) for \(0^\circ \le \theta \le 360^\circ\).
A: \(\sec^2\theta - 1 = 3 + \sec\theta\), so \(\sec^2\theta - \sec\theta - 4 = 0\). That does not factorise: \(\sec\theta = \dfrac{1 \pm \sqrt{17}}{2} = 2.562\) or \(-1.562\). Then \(\cos\theta = 0.3903\) gives \(\theta = 67.0^\circ, 293.0^\circ\), and \(\cos\theta = -0.6402\) gives \(\theta = 129.8^\circ, 230.2^\circ\).
Q: Find the exact value of \(\cos 15^\circ\) using \(15^\circ = 60^\circ - 45^\circ\).
A: \(\cos 15^\circ = \cos 60^\circ\cos 45^\circ + \sin 60^\circ\sin 45^\circ = \dfrac12\cdot\dfrac{\sqrt2}{2} + \dfrac{\sqrt3}{2}\cdot\dfrac{\sqrt2}{2} = \dfrac{\sqrt2 + \sqrt6}{4}\).
Q: Given \(\cos A = \tfrac{12}{13}\) with \(A\) acute and \(\sin B = \tfrac{3}{5}\) with \(B\) acute, find \(\cos(A - B)\).
A: \(\sin A = \tfrac{5}{13}\), \(\cos B = \tfrac45\). \(\cos(A - B) = \tfrac{12}{13}\cdot\tfrac45 + \tfrac5{13}\cdot\tfrac35 = \tfrac{48 + 15}{65} = \tfrac{63}{65}\).
Q: (a) Given that \(\sin\theta = \tfrac{3}{5}\) and \(\theta\) is acute, find the exact values of \(\sin 2\theta\) and \(\cos 2\theta\). (b) Solve \(\sin 2x = \sin x\) for \(0^\circ \le x \le 360^\circ\).
A: (a) \(\sin 2\theta = \tfrac{24}{25}\), \(\cos 2\theta = \tfrac{7}{25}\). (b) \(2\sin x\cos x = \sin x\), so \(\sin x(2\cos x - 1) = 0\). Then \(\sin x = 0\) gives \(0^\circ, 180^\circ, 360^\circ\) and \(\cos x = \tfrac12\) gives \(60^\circ, 300^\circ\).
Q: Solve \(2\cos 2x + 3\cos x + 1 = 0\) for \(0^\circ \le x \le 360^\circ\).
A: \(2(2\cos^2 x - 1) + 3\cos x + 1 = 0\), so \(4\cos^2 x + 3\cos x - 1 = 0\), \((4\cos x - 1)(\cos x + 1) = 0\). \(\cos x = \tfrac14\) gives \(75.5^\circ, 284.5^\circ\); \(\cos x = -1\) gives \(180^\circ\).
Q: Prove that \(\dfrac{\sin 2\theta}{1 + \cos 2\theta} \equiv \tan\theta\).
A: \(\dfrac{2\sin\theta\cos\theta}{2\cos^2\theta} = \dfrac{\sin\theta}{\cos\theta} = \tan\theta\). ∎
Q: Express \(5\sin\theta + 12\cos\theta\) in the form \(R\sin(\theta + \alpha)\), and state its greatest value. Solve \(5\sin\theta + 12\cos\theta = 6.5\) for \(0^\circ \le \theta \le 360^\circ\).
A: \(R = 13\), \(\tan\alpha = \tfrac{12}{5}\), \(\alpha = 67.38^\circ\). Greatest value \(13\). Solve \(\sin(\theta + 67.38^\circ) = 0.5\): \(u = 150^\circ\) or \(390^\circ\) (and \(30^\circ\) is too small), so \(\theta = 82.6^\circ\) or \(322.6^\circ\).
Q: (Exam style) (a) Express \(\sqrt3\cos\theta + \sin\theta\) in the form \(R\cos(\theta - \alpha)\) with exact \(R\) and \(\alpha\) in radians. (b) Hence solve \(\sqrt3\cos\theta + \sin\theta = \sqrt2\) for \(0 \le \theta \le 2\pi\).
A: (a) \(R\cos\alpha = \sqrt3\), \(R\sin\alpha = 1\), so \(R = 2\) and \(\tan\alpha = \dfrac{1}{\sqrt3}\), \(\alpha = \dfrac{\pi}{6}\). [M1 A1 A1] The form is \(2\cos\left(\theta - \dfrac{\pi}{6}\right)\). (b) \(\cos\left(\theta - \dfrac\pi6\right) = \dfrac{\sqrt2}{2}\). [M1] The angle \(u = \theta - \dfrac{\pi}{6}\) lies between \(-\dfrac{\pi}{6}\) and \(\dfrac{11\pi}{6}\). The values with \(\cos u = \dfrac{\sqrt2}{2}\) are \(u = \dfrac\pi4\) and \(u = \dfrac{7\pi}{4}\) (the value \(-\dfrac\pi4\) is below \(-\dfrac\pi6\), so it is out of range). [M1] Add \(\dfrac\pi6\): \(\theta = \dfrac{5\pi}{12}\) or \(\theta = \dfrac{23\pi}{12}\). [A1]
:::

:::quiz
? What is the exact value of \(\sin 15^\circ\)?
- \(\dfrac{\sqrt6 + \sqrt2}{4}\)
+ \(\dfrac{\sqrt6 - \sqrt2}{4}\)
- \(\dfrac{\sqrt3 - 1}{2}\)
- \(\dfrac{1}{2}\sin 30^\circ\)
> \(\sin 15^\circ = \sin(45^\circ - 30^\circ) = \tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt3}{2} - \tfrac{\sqrt2}{2}\cdot\tfrac12 = \dfrac{\sqrt6 - \sqrt2}{4}\). The plus version is \(\sin 75^\circ\). Halving \(\sin 30^\circ\) is not valid: \(\sin\) of half an angle is not half the sine.
? Which expression equals \(\cos 2\theta\)?
- \(2\cos\theta - 1\)
- \(\cos^2\theta + \sin^2\theta\)
+ \(1 - 2\sin^2\theta\)
- \(2\sin\theta\cos\theta\)
> \(\cos 2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1 = \cos^2\theta - \sin^2\theta\). The option with a single \(\cos\theta\) forgets the square. \(\cos^2\theta + \sin^2\theta = 1\) is the Pythagorean identity, and \(2\sin\theta\cos\theta\) is \(\sin 2\theta\).
? \(\cos(A + B)\) is equal to
- \(\cos A\cos B + \sin A\sin B\)
+ \(\cos A\cos B - \sin A\sin B\)
- \(\sin A\cos B + \cos A\sin B\)
- \(\cos A + \cos B\)
> For cosine the sign in the middle is the opposite of the sign in the bracket, so \(\cos(A + B)\) has a minus. The first option is \(\cos(A - B)\), the third is \(\sin(A + B)\).
? In \(3\sin\theta + 4\cos\theta = R\sin(\theta + \alpha)\), the value of \(\tan\alpha\) is
- \(\tfrac34\)
+ \(\tfrac43\)
- \(5\)
- \(\tfrac35\)
> Matching \(R\cos\alpha = 3\) and \(R\sin\alpha = 4\) gives \(\tan\alpha = \dfrac{R\sin\alpha}{R\cos\alpha} = \tfrac43\). Inverting this to \(\tfrac34\) is the common slip. \(R = 5\), and \(\tfrac35\) is \(\cos\alpha\).
? What is the greatest value of \(\dfrac{1}{4 + 3\sin\theta}\)?
- \(\tfrac17\)
+ \(1\)
- \(\tfrac14\)
- \(\tfrac13\)
> The fraction is greatest when the denominator is smallest, which is \(4 - 3 = 1\), so the greatest value is \(1\). Using \(4 + 3 = 7\) gives the least value, \(\tfrac17\).
:::

:::recap
- \(\sec\theta = \dfrac1{\cos\theta}\), \(\operatorname{cosec}\theta = \dfrac1{\sin\theta}\), \(\cot\theta = \dfrac1{\tan\theta}\); the calculator has no keys, so use the reciprocal. \(|\sec|\) and \(|\operatorname{cosec}| \ge 1\).
- \(\sec^2\theta \equiv 1 + \tan^2\theta\) and \(\operatorname{cosec}^2\theta \equiv 1 + \cot^2\theta\) turn mixed equations into quadratics.
- \(\sin(A \pm B) = \sin A\cos B \pm \cos A\sin B\); \(\cos(A \pm B) = \cos A\cos B \mp \sin A\sin B\); \(\tan(A \pm B) = \dfrac{\tan A \pm \tan B}{1 \mp \tan A\tan B}\).
- \(\sin 2A = 2\sin A\cos A\); \(\cos 2A = \cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A\); \(\tan 2A = \dfrac{2\tan A}{1 - \tan^2 A}\).
- \(a\sin\theta + b\cos\theta = R\sin(\theta + \alpha)\) with \(R = \sqrt{a^2 + b^2}\), \(\tan\alpha = \dfrac ba\). The greatest value is \(R\), the least \(-R\).
- Factorise instead of dividing by a trig function that might be zero. Change the interval when the angle is \(2x\) or \(\theta + \alpha\).
:::

:::links
- watch: [The R-form (harmonic identities)](https://www.examsolutions.net/tutorials/harmonic-identities/) · ExamSolutions · a sin θ + b cos θ as R sin(θ + α)
- watch: [Exam questions: double angles](https://www.examsolutions.net/tutorials/exam-questions-double-angles/) · ExamSolutions · exam-style questions solved on video
- practise: [CAIE Pure 3 compound and double angle exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/trigonometry/compound-and-double-angle-formulae/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [Trigonometry](https://www.khanacademy.org/math/trigonometry) · Khan Academy · units on identities and equations
- explore: [Trigonometry: Compound Angles](https://undergroundmathematics.org/trigonometry-compound-angles) · Underground Mathematics · where the addition formulae come from
- papers: [9709 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-3/) · Physics & Maths Tutor · papers with mark schemes [unofficial]

Links checked 3 October 2026.
:::
Next: [Further differentiation](#math.p3.diff).
