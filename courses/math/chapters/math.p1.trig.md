@chapter math.p1.trig
@title Trigonometry
@level as
@paper CAIE P1 · Edexcel IAL P1–P2 · AQA/OCR/Edexcel Pure Year 1
@time 8–10 hours
@summary The sine, cosine and tangent of any angle; their graphs and transformations in degrees and radians; exact values; principal values of the inverse functions; the identities \(\tan\theta \equiv \dfrac{\sin\theta}{\cos\theta}\) and \(\sin^2\theta + \cos^2\theta \equiv 1\); and finding all the solutions of trigonometric equations in an interval.

:::why
Trigonometry describes anything that repeats: sound waves, tides, orbits and alternating current. In Paper 1 a typical question asks you to prove an identity and then solve an equation with it. The method is the same every time, and it is easy to lose marks by missing solutions. This chapter gives you a routine that finds every solution.
:::

**Before you start**, you need right-angled trigonometry and exact values from [Geometry and trigonometry basics](#math.f.geometry), radians from [Circular measure](#math.p1.circular), and graph transformations from [Functions](#math.p1.functions). Factorising quadratics ([Quadratics](#math.p1.quadratics)) is used in the equations.

## Trigonometric functions of any angle

In a right-angled triangle, angles are below \(90^\circ\). To define \(\sin\theta\), \(\cos\theta\) and \(\tan\theta\) for any angle, use the **unit circle**: a circle of radius 1 centred at the origin. Measure the angle \(\theta\) anticlockwise from the positive \(x\)-axis and let \(P\) be the point where the arm meets the circle.

:::def Sine, cosine and tangent of any angle
For a point \(P\) on the unit circle at angle \(\theta\) from the positive \(x\)-axis: \(\cos\theta\) is the \(x\)-coordinate of \(P\) and \(\sin\theta\) is the \(y\)-coordinate of \(P\). The tangent is \(\tan\theta = \dfrac{\sin\theta}{\cos\theta}\), the gradient of the arm, which is undefined when \(\cos\theta = 0\).
:::

Drag the point round the circle. Watch how sine (height) and cosine (sideways) change sign as the point moves through the four quadrants, and find the angles where they are equal.

:::html
<div class="widget" data-w="unitcircle" data-angle="30"></div>
:::

The signs follow the quadrant. The mnemonic **CAST** (start in the bottom right and go anticlockwise) names the function that is positive: **C**osine in quadrant 4, **A**ll in quadrant 1, **S**ine in quadrant 2, **T**angent in quadrant 3.

| Quadrant | Angle | \(\sin\) | \(\cos\) | \(\tan\) |
|---|---|---|---|---|
| 1 | \(0^\circ\) to \(90^\circ\) | \(+\) | \(+\) | \(+\) |
| 2 | \(90^\circ\) to \(180^\circ\) | \(+\) | \(-\) | \(-\) |
| 3 | \(180^\circ\) to \(270^\circ\) | \(-\) | \(-\) | \(+\) |
| 4 | \(270^\circ\) to \(360^\circ\) | \(-\) | \(+\) | \(-\) |

Reflecting the point in the axes gives the relations between angles. These relate any angle to an **acute** angle \(\theta\) with the same size of sine, cosine or tangent.

:::key Related angles
\[\sin(180^\circ - \theta) = \sin\theta \qquad \cos(360^\circ - \theta) = \cos\theta \qquad \tan(180^\circ + \theta) = \tan\theta\]
\[\sin(-\theta) = -\sin\theta \qquad \cos(-\theta) = \cos\theta \qquad \tan(-\theta) = -\tan\theta\]
The values repeat every \(360^\circ\) for sine and cosine, and every \(180^\circ\) for tangent. In radians replace \(180^\circ\) by \(\pi\) and \(360^\circ\) by \(2\pi\).
:::

:::eg Find the exact values of \(\sin 150^\circ\), \(\cos 240^\circ\), \(\tan 135^\circ\) and \(\cos\dfrac{5\pi}{6}\).
\(\sin 150^\circ = \sin(180^\circ - 30^\circ) = \sin 30^\circ = \dfrac12\).

\(\cos 240^\circ\): in quadrant 3 cosine is negative, and the acute angle is \(240^\circ - 180^\circ = 60^\circ\), so \(\cos 240^\circ = -\cos 60^\circ = -\dfrac12\).

\(\tan 135^\circ = -\tan 45^\circ = -1\).

\(\dfrac{5\pi}{6} = 150^\circ\) is in quadrant 2, so cosine is negative: \(\cos\dfrac{5\pi}{6} = -\cos\dfrac{\pi}{6} = -\dfrac{\sqrt3}{2}\).
:::

For reference, the exact values for the acute angles from [Geometry and trigonometry basics](#math.f.geometry), now in both measures:

| \(\theta\) | \(0\) | \(30^\circ = \dfrac{\pi}{6}\) | \(45^\circ = \dfrac{\pi}{4}\) | \(60^\circ = \dfrac{\pi}{3}\) | \(90^\circ = \dfrac{\pi}{2}\) |
|---|---|---|---|---|---|
| \(\sin\theta\) | \(0\) | \(\dfrac12\) | \(\dfrac{\sqrt2}{2}\) | \(\dfrac{\sqrt3}{2}\) | \(1\) |
| \(\cos\theta\) | \(1\) | \(\dfrac{\sqrt3}{2}\) | \(\dfrac{\sqrt2}{2}\) | \(\dfrac12\) | \(0\) |
| \(\tan\theta\) | \(0\) | \(\dfrac{\sqrt3}{3}\) | \(1\) | \(\sqrt3\) | undefined |

## Graphs of sine, cosine and tangent

:::plot The graphs of \(y = \sin x\) and \(y = \cos x\) for \(0^\circ \le x \le 360^\circ\). Both have a maximum of 1, a minimum of \(-1\) and a period of \(360^\circ\). The cosine graph is the sine graph shifted \(90^\circ\) to the left.
--f "sin(x)" --f "cos(x)" --label "y = sin x" --label "y = cos x" --deg --x 0 360 --y -1.5 1.5 --xstep 90 --legend tr
:::

:::key Properties of the graphs
- \(y = \sin x\) and \(y = \cos x\): period \(360^\circ\) (\(2\pi\)), range \(-1 \le y \le 1\). Sine passes through \((0, 0)\); cosine starts at \((0, 1)\).
- \(y = \tan x\): period \(180^\circ\) (\(\pi\)), range all real numbers. It has **asymptotes** (vertical lines it never reaches) at \(x = 90^\circ\), \(270^\circ\), and so on. It passes through the origin.
- The graphs continue in both directions for ever. The curve for negative angles is found by the symmetry: sine is odd (rotates \(180^\circ\) about the origin), cosine is even (mirrors in the \(y\)-axis).
:::

## Transformations of trigonometric graphs

The transformations from [Functions](#math.p1.functions) apply to trigonometric graphs.

:::key Transformations
For \(y = a\sin(bx + c) + d\) (and similarly for cosine):
- \(a\): stretch parallel to the \(y\)-axis, scale factor \(a\). The **amplitude** (half the height from top to bottom) becomes \(|a|\).
- \(b\): stretch parallel to the \(x\)-axis, scale factor \(\dfrac1b\). The period becomes \(\dfrac{360^\circ}{b}\) (or \(\dfrac{2\pi}{b}\)).
- \(c\): translation by \(-\dfrac{c}{b}\) in the \(x\)-direction. \(y = \sin(x + 30^\circ)\) moves \(30^\circ\) to the **left**.
- \(d\): translation by \(d\) up the \(y\)-axis.
The tangent graph has period \(\dfrac{180^\circ}{b}\) instead.
:::

:::plot The graphs of \(y = 3\sin x\) (amplitude 3) and \(y = 1 - \cos 2x\) (period \(180^\circ\), range 0 to 2).
--f "3*sin(x)" --f "1-cos(2*x)" --label "y = 3 sin x" --label "y = 1 − cos 2x" --deg --x 0 360 --y -3.5 3.5 --xstep 90 --legend tr
:::

:::plot The graph of \(y = \tan x\) and the translated graph \(y = \tan(x + 45^\circ)\), which is \(y = \tan x\) shifted \(45^\circ\) to the left. The asymptotes of the second graph are at \(45^\circ\) and \(225^\circ\).
--f "tan(x)" --f "tan(x+45)" --label "y = tan x" --label "y = tan(x + 45°)" --deg --x 0 360 --y -4 4 --xstep 90 --vline 90 --vline 270 --legend tr
:::

:::eg (Exam style) The function \(\mathrm{f}\) is defined by \(\mathrm{f}(x) = 1 - \cos 2x\) for \(0^\circ \le x \le 360^\circ\). (a) State the range of \(\mathrm{f}\) and its period. (b) Describe the transformations that map \(y = \cos x\) to \(y = 1 - \cos 2x\). (c) Solve \(\mathrm{f}(x) = 1\).
**(a)** \(\cos 2x\) lies between \(-1\) and \(1\), so \(1 - \cos 2x\) lies between \(0\) and \(2\). The range is \(0 \le \mathrm{f}(x) \le 2\). [B1] The period is \(\dfrac{360^\circ}{2} = 180^\circ\). [B1]

**(b)** A stretch parallel to the \(x\)-axis with scale factor \(\tfrac12\) gives \(\cos 2x\). [B1] A reflection in the \(x\)-axis gives \(-\cos 2x\), and a translation of \(\begin{pmatrix}0\\1\end{pmatrix}\) gives \(1 - \cos 2x\). [B1]

**(c)** \(1 - \cos 2x = 1\) gives \(\cos 2x = 0\). [M1] For \(0^\circ \le x \le 360^\circ\), the angle \(2x\) is in the range \(0^\circ\) to \(720^\circ\): \(2x = 90^\circ, 270^\circ, 450^\circ, 630^\circ\). [M1]
\[x = 45^\circ, 135^\circ, 225^\circ, 315^\circ\] [A1]
:::

## Inverse functions and principal values

Your calculator's \(\sin^{-1}\), \(\cos^{-1}\) and \(\tan^{-1}\) give only **one** angle. Sine is not one-one over all angles, so its inverse needs a restricted domain (see [Functions](#math.p1.functions)).

:::key Principal values
\[\sin^{-1}x:\ -90^\circ \le y \le 90^\circ \quad (-\tfrac{\pi}{2} \text{ to } \tfrac{\pi}{2})\]
\[\cos^{-1}x:\ 0^\circ \le y \le 180^\circ \quad (0 \text{ to } \pi)\]
\[\tan^{-1}x:\ -90^\circ < y < 90^\circ \quad (-\tfrac{\pi}{2} \text{ to } \tfrac{\pi}{2})\]
The ranges are on MF19. The calculator answer is the **principal value**; other solutions come from the symmetry of the graph.
:::

So \(\sin^{-1}(-0.5) = -30^\circ\), \(\cos^{-1}(-0.5) = 120^\circ\) and \(\tan^{-1}(1) = 45^\circ\). Note that \(\sin^{-1}x\) means "the inverse function", not \(\dfrac{1}{\sin x}\).

## Solving trigonometric equations

To find **all** the solutions in an interval, find the principal value \(\alpha\) with the calculator, then use the symmetry of the graph to find the other angles.

:::key All solutions in a given interval
- \(\sin\theta = k\): \(\theta = \alpha\) or \(180^\circ - \alpha\), then add or subtract multiples of \(360^\circ\).
- \(\cos\theta = k\): \(\theta = \alpha\) or \(360^\circ - \alpha\) (equivalently \(\pm\alpha\)), then add or subtract multiples of \(360^\circ\).
- \(\tan\theta = k\): \(\theta = \alpha\), then add or subtract multiples of \(180^\circ\).
In radians use \(\pi\) and \(2\pi\). Sketching the graph of the function and marking \(k\) shows how many solutions to expect.
:::

:::eg Solve for \(0^\circ \le x \le 360^\circ\): (a) \(\sin x = 0.7\), (b) \(\cos x = -0.3\), (c) \(\tan x = -2\).
(a) The calculator gives \(\alpha = 44.4^\circ\). The other solution is \(180^\circ - 44.4^\circ = 135.6^\circ\). So \(x = 44.4^\circ\) or \(135.6^\circ\).

(b) The calculator gives \(107.5^\circ\) (obtuse, because the cosine is negative). The other solution is \(360^\circ - 107.5^\circ = 252.5^\circ\). So \(x = 107.5^\circ\) or \(252.5^\circ\).

(c) The calculator gives \(-63.4^\circ\), outside the interval. Add \(180^\circ\) to get \(116.6^\circ\), and add \(360^\circ\) to get \(296.6^\circ\). So \(x = 116.6^\circ\) or \(296.6^\circ\).
:::

When the equation contains \(\sin 2x\), \(\cos 3x\) or \(\sin(x - 20^\circ)\), treat the whole angle as one unknown, **change the interval** to match, solve, then work back to \(x\).

:::eg Solve (a) \(\sin 2x = 0.5\) for \(0^\circ \le x \le 360^\circ\), (b) \(\cos 2x = 0.3\) for \(0^\circ \le x \le 360^\circ\), (c) \(\sin(x - 20^\circ) = 0.4\) for \(0^\circ \le x \le 360^\circ\), (d) \(\sin\left(x + \dfrac{\pi}{6}\right) = \dfrac12\) for \(0 \le x \le 2\pi\).
(a) Let \(u = 2x\), so \(0^\circ \le u \le 720^\circ\). Then \(\sin u = 0.5\): \(u = 30^\circ, 150^\circ\), and \(+360^\circ\): \(390^\circ, 510^\circ\). Divide by 2:
\[x = 15^\circ, 75^\circ, 195^\circ, 255^\circ\]

(b) \(u = 2x\) between \(0^\circ\) and \(720^\circ\). The calculator gives \(72.5^\circ\); the other value in the first turn is \(360^\circ - 72.5^\circ = 287.5^\circ\). Adding \(360^\circ\) gives \(432.5^\circ\) and \(647.5^\circ\). Divide by 2: \(x = 36.3^\circ, 143.7^\circ, 216.3^\circ, 323.7^\circ\).

(c) Let \(u = x - 20^\circ\), so \(-20^\circ \le u \le 340^\circ\). Then \(\sin u = 0.4\): \(u = 23.6^\circ\) or \(156.4^\circ\). Add \(20^\circ\): \(x = 43.6^\circ\) or \(176.4^\circ\).

(d) Let \(u = x + \dfrac{\pi}{6}\), so \(\dfrac{\pi}{6} \le u \le \dfrac{13\pi}{6}\). Then \(\sin u = \dfrac12\) gives \(u = \dfrac{\pi}{6}\), \(\dfrac{5\pi}{6}\), \(\dfrac{13\pi}{6}\). Subtract \(\dfrac{\pi}{6}\): \(x = 0\), \(\dfrac{2\pi}{3}\), \(2\pi\).
:::

:::warn Where solutions go missing
- With \(\sin 2x\), the interval for \(2x\) is **twice** as long, so there are twice as many solutions. Stopping at the first two loses half the marks.
- With a shift, such as \(x - 20^\circ\), the interval moves: do not apply the original interval to \(u\).
- Always check the calculator is in the right mode (degrees or radians).
- Round only at the end. Give degrees to 1 decimal place and radians to 3 significant figures unless exact.
:::

### Negative intervals

If the interval includes negative angles, the calculator's principal value is often already in the interval. Sketch the graph and draw the horizontal line \(y = k\) first. The number of crossings is the number of solutions you must find.

:::plot Solving \(\sin x = -\tfrac23\) in \(-180^\circ \le x \le 180^\circ\): the line \(y = -\tfrac23\) meets the sine graph twice, both times below the axis.
--f "sin(x)" --label "y = sin x" --deg --x -180 180 --y -1.5 1.5 --xstep 90 --hline -0.667 --pt "-41.8,-0.667,x = −41.8°@ne" --pt "-138.2,-0.667,x = −138.2°@nw" --legend tr
:::

:::eg Solve (a) \(3\sin x = -2\) for \(-180^\circ \le x \le 180^\circ\), and (b) \(2\cos 2x = 1\) for \(-\pi \le x \le \pi\).
(a) \(\sin x = -\tfrac23\). The figure shows two crossings. The calculator gives \(-41.8^\circ\), which is in the interval. By symmetry about \(x = -90^\circ\) the other solution is \(-180^\circ - (-41.8^\circ) = -138.2^\circ\). So \(x = -41.8^\circ\) or \(-138.2^\circ\).

(b) \(\cos 2x = \tfrac12\). Let \(u = 2x\), so \(-2\pi \le u \le 2\pi\), which is two full turns, so expect four solutions. The principal value is \(u = \dfrac{\pi}{3}\), and cosine is even, so also \(u = -\dfrac{\pi}{3}\). Adding and subtracting \(2\pi\) gives \(u = \dfrac{5\pi}{3}\) and \(u = -\dfrac{5\pi}{3}\). Divide by 2:
\[x = \pm\frac{\pi}{6},\ \pm\frac{5\pi}{6}\]
:::

## Identities

An **identity** is true for every value of the variable. It is written with \(\equiv\), unlike an equation that has particular solutions. Two identities do almost all the work.

:::key The two identities
\[\tan\theta \equiv \frac{\sin\theta}{\cos\theta} \qquad \sin^2\theta + \cos^2\theta \equiv 1\]
Rearranged: \(\sin^2\theta \equiv 1 - \cos^2\theta\) and \(\cos^2\theta \equiv 1 - \sin^2\theta\). Both are on MF19. The second is Pythagoras on the unit circle: \(\cos\theta\) and \(\sin\theta\) are the legs of a right-angled triangle with hypotenuse \(1\).
:::

:::eg Simplify (a) \(\dfrac{\sin\theta\cos\theta}{\tan\theta}\) and (b) \(\dfrac{\sin^2\theta}{1 - \cos^2\theta}\). Then prove that \(\sin^4\theta - \cos^4\theta \equiv \sin^2\theta - \cos^2\theta\).
(a) Replace \(\tan\theta\): \(\dfrac{\sin\theta\cos\theta}{\sin\theta/\cos\theta} = \sin\theta\cos\theta \times \dfrac{\cos\theta}{\sin\theta} = \cos^2\theta\).

(b) The denominator is \(\sin^2\theta\), so the fraction equals \(1\).

For the proof, factorise as a difference of two squares:
\[\sin^4\theta - \cos^4\theta = (\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta) = (\sin^2\theta - \cos^2\theta) \times 1\]
which is the right-hand side. ∎
:::

To **prove** an identity, start from one side (usually the more complicated), change it step by step until it matches the other side, and do not work on both sides at once. Useful tools: replace \(\tan\theta\) by \(\sin/\cos\), replace \(\sin^2\theta\) by \(1 - \cos^2\theta\), combine fractions, and factorise.

:::eg (Exam style) (a) Prove that \(\dfrac{\sin\theta}{1 + \cos\theta} + \dfrac{1 + \cos\theta}{\sin\theta} \equiv \dfrac{2}{\sin\theta}\). (b) Hence solve \(\dfrac{\sin\theta}{1 + \cos\theta} + \dfrac{1 + \cos\theta}{\sin\theta} = 4\) for \(0^\circ \le \theta \le 360^\circ\).
**(a)** Use a common denominator:
\[\text{LHS} = \frac{\sin^2\theta + (1 + \cos\theta)^2}{\sin\theta(1 + \cos\theta)}\] [M1]
Expand the bracket: \(\sin^2\theta + 1 + 2\cos\theta + \cos^2\theta\). Use \(\sin^2\theta + \cos^2\theta = 1\):
\[= \frac{1 + 1 + 2\cos\theta}{\sin\theta(1 + \cos\theta)} = \frac{2(1 + \cos\theta)}{\sin\theta(1 + \cos\theta)}\] [M1 A1]
Cancel the common factor: \(\dfrac{2}{\sin\theta}\) = RHS. ∎ [A1]

**(b)** By part (a), the equation is \(\dfrac{2}{\sin\theta} = 4\), so \(\sin\theta = \tfrac12\). [M1]
\[\theta = 30^\circ \text{ or } 150^\circ\] [A1]
Both solutions keep \(\sin\theta \ne 0\) and \(1 + \cos\theta \ne 0\), so they are valid. [B1]
:::

## Equations that need an identity

If an equation contains both \(\sin\) and \(\cos\) (or \(\tan\)), use an identity to leave only one function. Often this gives a quadratic in \(\sin\theta\) or \(\cos\theta\).

:::steps
1. Rewrite so there is one trigonometric function (use \(\sin^2 = 1 - \cos^2\) or \(\tan = \sin/\cos\)).
2. Rearrange to a quadratic in that function and factorise (or use the formula).
3. Reject any value with absolute value above 1 (the range of sine and cosine).
4. Solve each remaining equation for all angles in the interval.
:::

:::eg Solve \(2\sin^2 x + 3\cos x = 0\) for \(0^\circ \le x \le 360^\circ\).
Replace \(\sin^2 x\) by \(1 - \cos^2 x\):
\[\begin{aligned} 2(1 - \cos^2 x) + 3\cos x &= 0 \\ 2\cos^2 x - 3\cos x - 2 &= 0 \\ (2\cos x + 1)(\cos x - 2) &= 0 \end{aligned}\]
So \(\cos x = -\tfrac12\) or \(\cos x = 2\). The second is impossible because \(\cos x \le 1\). From \(\cos x = -\tfrac12\), \(x = 120^\circ\) or \(240^\circ\).
Check: \(x = 120^\circ\) gives \(2\left(\tfrac34\right) + 3\left(-\tfrac12\right) = 0\). ✓
:::

:::eg Solve \(\tan x = 2\sin x\) for \(0^\circ \le x \le 360^\circ\).
Do **not** divide by \(\sin x\), which would lose solutions. Write \(\tan x = \dfrac{\sin x}{\cos x}\) and multiply out:
\[\begin{aligned} \sin x &= 2\sin x\cos x \\ \sin x(1 - 2\cos x) &= 0 \end{aligned}\]
So \(\sin x = 0\), giving \(x = 0^\circ, 180^\circ, 360^\circ\), or \(\cos x = \tfrac12\), giving \(x = 60^\circ, 300^\circ\). The five solutions are \(0^\circ, 60^\circ, 180^\circ, 300^\circ, 360^\circ\).
:::

:::eg (Exam style) (a) Show that the equation \(3\tan\theta = 2\cos\theta\) can be written as \(2\sin^2\theta + 3\sin\theta - 2 = 0\). (b) Hence solve the equation for \(0^\circ \le \theta \le 360^\circ\).
**(a)** Replace \(\tan\theta\): \(\dfrac{3\sin\theta}{\cos\theta} = 2\cos\theta\), so \(3\sin\theta = 2\cos^2\theta\). [M1]
Use \(\cos^2\theta = 1 - \sin^2\theta\): \(3\sin\theta = 2 - 2\sin^2\theta\). [M1]
\[2\sin^2\theta + 3\sin\theta - 2 = 0\] [A1]

**(b)** Factorise: \((2\sin\theta - 1)(\sin\theta + 2) = 0\). [M1] So \(\sin\theta = \tfrac12\) or \(\sin\theta = -2\); the second has no solution. [A1]
\[\theta = 30^\circ \text{ or } 150^\circ\] [A1]
:::

:::exam Showing a trig solution
- State the identity you use. "Using \(\sin^2\theta + \cos^2\theta = 1\)" earns the method mark even if the arithmetic slips later.
- Reject impossible values (such as \(\sin\theta = -2\)) with a reason. If you silently drop them, you lose a mark.
- A request for exact values in radians, for example "\(x = \dfrac{\pi}{3}\)", is not satisfied by decimals.
:::

:::board Other boards
Edexcel IAL, AQA, OCR and Edexcel (UK) cover the same graphs, exact values, identities and equations in their first Pure year, usually both in degrees and radians. UK Further Maths and some boards add general solutions such as \(x = 30^\circ + 360^\circ n\); Cambridge 9709 asks only for solutions in a given interval. Secant, cosecant, cotangent and compound angles come later: see [Further trigonometry](#math.p3.trig).
:::

:::try Start easy, finish at exam standard
Q: Write down the exact value of (a) \(\sin 300^\circ\), (b) \(\cos\dfrac{2\pi}{3}\), (c) \(\tan 210^\circ\).
A: (a) \(-\sin 60^\circ = -\dfrac{\sqrt3}{2}\). (b) \(-\cos\dfrac{\pi}{3} = -\dfrac12\). (c) \(\tan 30^\circ = \dfrac{\sqrt3}{3}\) (quadrant 3, tangent positive).
Q: State the amplitude, period and range of (a) \(y = 4\sin x\), (b) \(y = 2\cos 3x + 1\).
A: (a) Amplitude 4, period \(360^\circ\), range \(-4 \le y \le 4\). (b) Amplitude 2, period \(\dfrac{360^\circ}{3} = 120^\circ\), range \(-1 \le y \le 3\).
Q: Solve for \(0^\circ \le x \le 360^\circ\): (a) \(\sin x = -0.5\), (b) \(2\cos x = 1.2\).
A: (a) \(\alpha = -30^\circ\). Solutions \(210^\circ\) and \(330^\circ\). (b) \(\cos x = 0.6\): \(x = 53.1^\circ\) or \(360^\circ - 53.1^\circ = 306.9^\circ\).
Q: Solve \(3\tan 3x = 4.5\) for \(0^\circ \le x \le 180^\circ\).
A: \(\tan 3x = 1.5\). \(3x\) is between \(0^\circ\) and \(540^\circ\). \(\alpha = 56.3^\circ\), so \(3x = 56.3^\circ, 236.3^\circ, 416.3^\circ\), and \(x = 18.8^\circ, 78.8^\circ, 138.8^\circ\).
Q: Solve \(\cos\left(x - \dfrac{\pi}{3}\right) = \dfrac{\sqrt3}{2}\) for \(0 \le x \le 2\pi\).
A: Let \(u = x - \dfrac{\pi}{3}\), so \(-\dfrac{\pi}{3} \le u \le \dfrac{5\pi}{3}\). \(\cos u = \dfrac{\sqrt3}{2}\) gives \(u = \pm\dfrac{\pi}{6}\). Add \(\dfrac{\pi}{3}\): \(x = \dfrac{\pi}{6}\) or \(\dfrac{\pi}{2}\).
Q: Prove that \(\tan\theta + \dfrac{1}{\tan\theta} \equiv \dfrac{1}{\sin\theta\cos\theta}\).
A: LHS \(= \dfrac{\sin\theta}{\cos\theta} + \dfrac{\cos\theta}{\sin\theta} = \dfrac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta} = \dfrac{1}{\sin\theta\cos\theta}\). ∎
Q: Solve \(6\cos^2 x + \sin x = 5\) for \(0^\circ \le x \le 360^\circ\).
A: \(6(1 - \sin^2 x) + \sin x = 5\) gives \(6\sin^2 x - \sin x - 1 = 0\), so \((3\sin x + 1)(2\sin x - 1) = 0\). Then \(\sin x = -\tfrac13\) gives \(x = 199.5^\circ, 340.5^\circ\), and \(\sin x = \tfrac12\) gives \(x = 30^\circ, 150^\circ\).
Q: Simplify \(\dfrac{\cos^2\theta}{1 - \sin\theta}\) and hence solve \(\dfrac{\cos^2\theta}{1 - \sin\theta} = 1.5\) for \(0^\circ \le \theta \le 360^\circ\).
A: \(\dfrac{1 - \sin^2\theta}{1 - \sin\theta} = 1 + \sin\theta\). Then \(1 + \sin\theta = 1.5\), so \(\sin\theta = 0.5\) and \(\theta = 30^\circ\) or \(150^\circ\).
Q: (Exam style) (a) Show that the equation \(4\sin^2\theta = 3 - 4\cos\theta\) can be written \(4\cos^2\theta - 4\cos\theta - 1 = 0\). (b) Hence solve it for \(0^\circ \le \theta \le 360^\circ\).
A: (a) Replace \(\sin^2\theta\) by \(1 - \cos^2\theta\): \(4 - 4\cos^2\theta = 3 - 4\cos\theta\). [M1] Rearranging gives \(4\cos^2\theta - 4\cos\theta - 1 = 0\). [A1] (b) The formula gives \(\cos\theta = \dfrac{4 \pm \sqrt{32}}{8} = \dfrac{1 \pm \sqrt2}{2}\), so \(\cos\theta = 1.207\) (impossible) or \(-0.2071\). [M1 A1] Then \(\theta = 102.0^\circ\) or \(258.0^\circ\). [A1]
:::

:::quiz
? What is the exact value of \(\sin 150^\circ\)?
+ \(\dfrac12\)
- \(-\dfrac12\)
- \(\dfrac{\sqrt3}{2}\)
- \(-\dfrac{\sqrt3}{2}\)
> \(150^\circ = 180^\circ - 30^\circ\), and \(\sin(180^\circ - \theta) = \sin\theta\), so \(\sin 150^\circ = \sin 30^\circ = \tfrac12\). The sine is positive in quadrant 2. The value \(\tfrac{\sqrt3}{2}\) is the cosine of \(30^\circ\).
? How many solutions does \(\sin x = 0.3\) have in \(0^\circ \le x \le 720^\circ\)?
- \(2\)
+ \(4\)
- \(3\)
- \(8\)
> Each full turn of \(360^\circ\) has two solutions (\(17.5^\circ\) and \(162.5^\circ\)), so two turns have four. People often give two, forgetting that the interval covers two turns.
? What is the period of \(y = \sin 3x\)?
- \(1080^\circ\)
- \(360^\circ\)
+ \(120^\circ\)
- \(60^\circ\)
> The period is \(\dfrac{360^\circ}{3} = 120^\circ\). The graph is stretched in the \(x\)-direction by a factor \(\tfrac13\), so it repeats three times as often. Multiplying by 3 gives \(1080^\circ\), the wrong direction.
? What is the principal value of \(\sin^{-1}(-0.5)\)?
- \(210^\circ\)
- \(330^\circ\)
+ \(-30^\circ\)
- \(30^\circ\)
> The principal value of \(\sin^{-1}\) lies between \(-90^\circ\) and \(90^\circ\), so it is \(-30^\circ\). The angles \(210^\circ\) and \(330^\circ\) are solutions of \(\sin x = -0.5\) in \(0^\circ\) to \(360^\circ\), but they are not principal values.
? Solving \(\sin x \cos x = \sin x\) by dividing both sides by \(\sin x\) leaves \(\cos x = 1\). What is wrong?
- Nothing, the method is fine.
+ It loses the solutions where \(\sin x = 0\).
- \(\cos x\) cannot equal 1.
- You must divide by \(\cos x\) instead.
> Dividing by \(\sin x\) assumes it is not zero. Instead write \(\sin x(\cos x - 1) = 0\): then \(\sin x = 0\) or \(\cos x = 1\), and you keep every solution.
:::

:::recap
- On the unit circle, \(\cos\theta\) is the \(x\)-coordinate and \(\sin\theta\) the \(y\)-coordinate; \(\tan\theta = \sin\theta/\cos\theta\). Signs follow CAST.
- Related angles: \(\sin(180^\circ - \theta) = \sin\theta\), \(\cos(360^\circ - \theta) = \cos\theta\), \(\tan(180^\circ + \theta) = \tan\theta\), \(\sin(-\theta) = -\sin\theta\), \(\cos(-\theta) = \cos\theta\).
- Sine and cosine have period \(360^\circ\) and range \([-1, 1]\); tangent has period \(180^\circ\) and asymptotes. For \(y = a\sin(bx + c) + d\): amplitude \(|a|\), period \(360^\circ/b\).
- Principal values: \(\sin^{-1}\) in \([-90^\circ, 90^\circ]\), \(\cos^{-1}\) in \([0^\circ, 180^\circ]\), \(\tan^{-1}\) in \((-90^\circ, 90^\circ)\).
- To solve: principal value, then symmetry for others, then add periods. For \(\sin 2x\), work with \(2x\) and double the interval.
- Identities: \(\tan\theta \equiv \sin\theta/\cos\theta\) and \(\sin^2\theta + \cos^2\theta \equiv 1\). Prove from one side. Never divide by something that might be zero.
:::

:::note Learn more online
- **Watch:** [Trig equations in different ranges](https://www.examsolutions.net/tutorials/trig-equations-different-ranges/) · ExamSolutions · finding every solution in an interval
- **Watch:** [Exam questions: trig identities](https://www.examsolutions.net/tutorials/exam-questions-trigonometric-identities/) · ExamSolutions · prove-and-solve questions on video
- **Practise:** [CAIE Pure 1 trig equations exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/trigonometry/trigonometric-equations/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Trig Tour](https://phet.colorado.edu/en/simulations/trig-tour) · PhET · the unit circle and the graphs move together
- **Explore:** [Trigonometry: Triangles to Functions](https://undergroundmathematics.org/trigonometry-triangles-to-functions) · Underground Mathematics · from triangles to graphs, with rich problems
- **Read:** [How to learn trigonometry intuitively](https://betterexplained.com/articles/intuitive-trigonometry/) · BetterExplained · a picture-first explanation of sin, cos and tan

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Series](#math.p1.series).
