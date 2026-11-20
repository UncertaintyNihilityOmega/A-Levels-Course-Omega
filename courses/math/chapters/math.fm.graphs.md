@chapter math.fm.graphs
@title Graphs related to y = f(x)
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 4–6 hours
@summary From one sketch of y = f(x) you can draw four related graphs: y = |f(x)|, y = f(|x|), y = 1/f(x) and y² = f(x). You will learn the rule for each, apply them to polynomials and rational functions, and use the sketches to solve equations and inequalities exactly.

:::why
A good sketch of one graph is worth four. Reflect the parts below the axis and you have \(|f(x)|\); invert the heights and you have \(\dfrac{1}{f(x)}\); take square roots and you have \(y^2 = f(x)\). Examiners use these relationships to set equations and inequalities where algebra alone is slow or risky, because a sketch shows at once which regions work and which roots to throw away.
:::

**Before you start**, you need the sketching skills of [Rational functions and their graphs](#math.fm.rational), the modulus function from [Modulus and polynomials](#math.p3.algebra) and graph transformations from [Functions](#math.p1.functions).

:::try Warm-up
Q: Solve \(|2x - 1| = 5\). (from [Modulus and polynomials](#math.p3.algebra))
A: \(2x - 1 = 5\) or \(2x - 1 = -5\), so \(x = 3\) or \(x = -2\).
Q: How is the graph of \(y = f(-x)\) related to the graph of \(y = f(x)\)? (from [Functions](#math.p1.functions))
A: It is the reflection of \(y = f(x)\) in the \(y\)-axis.
Q: Write down the equations of the asymptotes of \(y = \dfrac{x + 1}{x - 2}\). (from [Rational functions and their graphs](#math.fm.rational))
A: The denominator is zero at \(x = 2\), so \(x = 2\) is a vertical asymptote. The degrees are equal, so \(y = 1\) is the horizontal asymptote.
:::

## The five graphs

Start with a sketch of \(y = f(x)\). Four other graphs can be drawn from it **without any new calculation**, by applying a rule to the sketch.

:::key The related graphs at a glance
| Graph | What to do with the sketch of \(y = f(x)\) |
|---|---|
| \(y = \lvert f(x)\rvert\) | Keep the parts on or above the \(x\)-axis. Reflect the parts below it in the \(x\)-axis. |
| \(y = f(\lvert x\rvert)\) | Keep the part with \(x \geq 0\), delete the part with \(x < 0\), and reflect what is left in the \(y\)-axis. |
| \(y = \dfrac{1}{f(x)}\) | Replace each height by its reciprocal (rules below). |
| \(y^2 = f(x)\) | Keep only where \(f(x) \geq 0\). Plot \(y = \pm\sqrt{f(x)}\): a curve symmetrical about the \(x\)-axis. |
:::

You will also be expected to use the transformations from [Functions](#math.p1.functions) (translations, stretches, reflections), and to combine them: \(y = \lvert f(x) \rvert\) followed by a translation, for example. This chapter looks at each new rule in turn, then uses the sketches to solve problems.

## The graph of \(y = |f(x)|\)

:::def Modulus of a function
\(|f(x)|\) is the non-negative number equal to \(f(x)\) when \(f(x) \geq 0\) and to \(-f(x)\) when \(f(x) < 0\). It is the size of \(f(x)\) without its sign.
:::

:::def False root
A solution of an equation found by squaring or by splitting a modulus into branches that does not satisfy the original equation or the condition of its branch. Check every candidate in the original equation.
:::

The modulus \(|f(x)|\) is the **size** of \(f(x)\) without its sign, so the graph never goes below the \(x\)-axis. Where \(f(x) \geq 0\) the graphs of \(y = |f(x)|\) and \(y = f(x)\) are the same. Where \(f(x) < 0\), \(|f(x)| = -f(x)\), which is the reflection of the curve in the \(x\)-axis.

:::key \(y = |f(x)|\)
- Reflect every part of \(y = f(x)\) that is below the \(x\)-axis in the \(x\)-axis. Everything else stays.
- The graph never goes below the \(x\)-axis. Where \(f\) crosses the axis at a simple root, \(|f|\) has a **corner** (a sharp "V").
- A minimum of \(f\) below the axis becomes a maximum of \(|f|\), with its \(y\)-value made positive.
- Asymptotes below the axis are reflected too: \(y = -3\) becomes \(y = 3\), and a vertical asymptote that goes to \(-\infty\) goes to \(+\infty\) instead.
:::

:::eg Sketch \(y = |f(x)|\) where \(f(x) = (x + 2)(x - 1)(x - 3) = x^3 - 2x^2 - 5x + 6\), and write down the coordinates of its local maxima.
**Sketch \(y = f(x)\) first.** It crosses the \(x\)-axis at \(-2\), \(1\) and \(3\), and the \(y\)-axis at \(y = 6\). It has a local maximum between \(-2\) and \(1\), and a local minimum between \(1\) and \(3\). Differentiate: \(f'(x) = 3x^2 - 4x - 5 = 0\) gives \(x = \dfrac{2 \pm \sqrt{19}}{3}\), that is \(x = -0.786\) and \(x = 2.12\). At \(x = -0.786\), \(f = 8.21\); at \(x = 2.12\), \(f = -4.06\).

**Reflect the negative parts.** \(f < 0\) for \(x < -2\) and for \(1 < x < 3\). The part for \(1 < x < 3\) (a dip) is reflected into a bump on top of the axis, with its peak at \((2.12, 4.06)\). The part for \(x < -2\) goes down to \(-\infty\) as \(x \to -\infty\): after reflecting, it goes up to \(+\infty\), so the left end of the graph rises.

**Corners** appear at \((-2, 0)\), \((1, 0)\) and \((3, 0)\).

The local maxima of \(y = |f(x)|\) are \((-0.786, 8.21)\) and \((2.12, 4.06)\).
:::

:::plot Both curves are drawn: \(y = x^3 - 2x^2 - 5x + 6\) and, on top of it, \(y = |x^3 - 2x^2 - 5x + 6|\). They agree where \(f \geq 0\). The parts of \(f\) below the axis, for \(x < -2\) and for \(1 < x < 3\), are reflected upwards, so \(|f|\) has corners at the three roots.
--f "x**3-2*x**2-5*x+6" --f "abs(x**3-2*x**2-5*x+6)" --label "y = f(x)" --label "y = |f(x)|" --x -3 3.6 --y -9 20 --pt "2.12,4.06,(2.12, 4.06)@ne" --legend tr
:::

## The graph of \(y = f(|x|)\)

Here \(|x|\) is put **inside** the function. For \(x \geq 0\), \(|x| = x\), so the graph is the same as \(y = f(x)\). For \(x < 0\), \(|x| = -x\), so \(f(|x|) = f(-x)\), which is the reflection of \(y = f(x)\) in the \(y\)-axis. Whatever \(y = f(x)\) does for negative \(x\) is forgotten.

:::key \(y = f(|x|)\)
- Keep the part of \(y = f(x)\) with \(x \geq 0\); delete the part with \(x < 0\); reflect the kept part in the \(y\)-axis.
- The graph is **symmetric about the \(y\)-axis** (an even function) and has the same \(y\)-intercept as \(y = f(x)\).
- If \(f\) is not flat at \(x = 0\), the graph has a **corner** at the \(y\)-axis.
- A vertical asymptote at \(x = a > 0\) appears at both \(x = a\) and \(x = -a\); one at \(x = -a\) disappears.
:::

Do not confuse the two: \(|f(x)|\) reflects the parts **below the \(x\)-axis**; \(f(|x|)\) reflects the part **right of the \(y\)-axis**. For \(f(x) = x - 2\), \(|f(x)| = |x - 2|\) is a V with its corner at \((2, 0)\), while \(f(|x|) = |x| - 2\) is a V with its corner at \((0, -2)\).

:::eg Sketch \(y = f(|x|)\) where \(f(x) = x^2 - 2x - 3\). Find where it meets the axes, and its stationary points.
For \(x \geq 0\) the graph is \(y = x^2 - 2x - 3 = (x - 1)^2 - 4\), with minimum \((1, -4)\). It crosses the \(x\)-axis where \((x - 3)(x + 1) = 0\): for \(x \geq 0\) only \(x = 3\) counts. The \(y\)-intercept is \((0, -3)\).

Reflect the \(x \geq 0\) part in the \(y\)-axis. The left half is the mirror image: minimum \((-1, -4)\) and an \(x\)-intercept at \(x = -3\).

So the graph meets the \(x\)-axis at \((-3, 0)\) and \((3, 0)\), and the \(y\)-axis at \((0, -3)\). It has two minima, \((-1, -4)\) and \((1, -4)\). At \(x = 0\) there is a local maximum with a **corner**: the gradient is \(-2\) just to the right and \(+2\) just to the left, so the point \((0, -3)\) is a peak, not a smooth top.
:::

:::plot The graph of \(y = f(x)\) (a parabola) and of \(y = f(|x|)\) for \(f(x) = x^2 - 2x - 3\). The second is symmetric about the \(y\)-axis, with two minima at \((\pm 1, -4)\) and a corner at \((0, -3)\).
--f "x**2-2*x-3" --f "x**2-2*abs(x)-3" --label "y = f(x)" --label "y = f(|x|)" --x -4 4.5 --y -6 14 --xstep 3 --pt "1,-4,(1, −4)@se" --pt "-1,-4,(−1, −4)@sw" --pt "0,-3,(0, −3)@ne" --legend tr
:::

## The graph of \(y = \dfrac{1}{f(x)}\)

The reciprocal turns large values into small ones and small values into large ones. Each feature of \(y = f(x)\) has a partner on the graph of \(y = \dfrac{1}{f(x)}\).

:::key \(y = \dfrac{1}{f(x)}\)
- **Same sign.** \(\dfrac{1}{f}\) is positive where \(f\) is positive and negative where \(f\) is negative. It is not defined where \(f = 0\).
- **Zeros of \(f\)** become **vertical asymptotes** of \(\dfrac{1}{f}\). Which way it goes: \(f \to 0^+\) gives \(\dfrac{1}{f} \to +\infty\); \(f \to 0^-\) gives \(-\infty\).
- **Vertical asymptotes of \(f\)** (where \(f \to \pm\infty\)) become points where \(\dfrac{1}{f} \to 0\): the curve meets the \(x\)-axis there.
- **Large \(|f|\)** (including a horizontal or oblique asymptote with \(|f| \to \infty\)) gives \(\dfrac{1}{f} \to 0\): the \(x\)-axis becomes an asymptote. A horizontal asymptote \(y = b\) (\(b \neq 0\)) of \(f\) gives \(y = \dfrac1b\). An asymptote \(y = 0\) of \(f\) gives a curve that goes to \(\pm\infty\).
- **Maxima and minima swap.** Where \(f\) has a local minimum or maximum at height \(m \neq 0\), \(\dfrac{1}{f}\) has a stationary point at the same \(x\), of height \(\dfrac1m\), of the opposite type. If \(f\) is increasing, \(\dfrac{1}{f}\) is decreasing, and vice versa.
- **Invariant points.** Where \(f(x) = 1\) or \(f(x) = -1\) the two graphs meet, because \(\dfrac{1}{1} = 1\) and \(\dfrac{1}{-1} = -1\).
:::

:::eg Sketch \(y = \dfrac{1}{f(x)}\) where \(f(x) = x^2 - 4\). Mark its asymptotes and turning point, and the points where it meets \(y = f(x)\).
**Features of \(f\).** Zeros at \(x = \pm 2\); a minimum \((0, -4)\); \(f \to +\infty\) as \(x \to \pm\infty\); positive for \(|x| > 2\), negative for \(|x| < 2\).

**Vertical asymptotes** of \(\dfrac{1}{f}\) at \(x = \pm 2\). For \(x\) just beyond 2, \(f\) is small and positive, so \(\dfrac{1}{f} \to +\infty\); for \(x\) just inside 2, \(f\) is small and negative, so \(\dfrac{1}{f} \to -\infty\). The same happens at \(x = -2\) (by symmetry).

**Horizontal asymptote.** As \(x \to \pm\infty\), \(f \to \infty\), so \(\dfrac{1}{f} \to 0^+\): \(y = 0\).

**Turning point.** The minimum \((0, -4)\) of \(f\) becomes a **maximum** \(\left(0, -\tfrac14\right)\). Between the asymptotes the curve is an upside-down "U" below the axis.

**Invariant points.** \(f = 1\) at \(x^2 = 5\), and \(f = -1\) at \(x^2 = 3\). The graphs meet at \((\pm\sqrt{5}, 1)\) and \((\pm\sqrt{3}, -1)\).
:::

:::plot The curve \(y = \dfrac{1}{x^2 - 4}\) (with its asymptotes \(x = \pm 2\) and \(y = 0\)) and the parabola \(y = x^2 - 4\) it came from. They meet where \(f = \pm 1\).
--f "x**2-4" --f "1/(x**2-4)" --label "y = f(x) = x² − 4" --label "y = 1/f(x)" --x -4.5 4.5 --y -6 6 --vline -2 --vline 2 --xstep 4 --pt "0,-0.25,(0, −1/4)@ne" --pt "2.236,1,(√5, 1)@se" --pt "-2.236,1,(−√5, 1)@sw" --legend tr
:::

Slide \(a\) in the graph below. The first curve is \(y = f(x) = x^2 - a\); the second is \(y = \dfrac{1}{f(x)}\). While \(a > 0\), \(f\) has two zeros, so \(\dfrac1f\) has two vertical asymptotes. As \(a\) falls to 0 the zeros merge into one at \(x = 0\) (a double zero), and for \(a < 0\) the function \(f\) has no zeros at all, so \(\dfrac{1}{f}\) has no asymptotes and is a smooth bump: the minimum of \(f\) at \((0, -a)\) gives a maximum of \(\dfrac{1}{f}\) at \(\left(0, -\dfrac1a\right)\).

:::html
<div class="widget" data-w="graph" data-fns="x^2 - a; 1/(x^2 - a)" data-x="-5,5" data-y="-6,6" data-params="a=4,-4,6,0.5" data-labels="y = f(x) = x² − a; y = 1/f(x)"></div>
:::

When \(f\) has no zeros there are no vertical asymptotes in \(\dfrac{1}{f}\). For instance \(f(x) = x^2 - 2x + 5 = (x - 1)^2 + 4\) is always at least 4, so \(\dfrac{1}{f}\) is always positive with a **maximum** \(\left(1, \tfrac14\right)\), and \(\dfrac{1}{f} \to 0^+\) as \(x \to \pm\infty\).

:::eg The curve \(y = f(x)\) has \(f(x) = \dfrac{x - 1}{x + 2}\). Describe the graph of \(y = \dfrac{1}{f(x)}\) and say where it meets \(y = f(x)\).
\(\dfrac{1}{f(x)} = \dfrac{x + 2}{x - 1}\): numerator and denominator are swapped.

The features of \(f\): zero at \(x = 1\) (becomes a vertical asymptote \(x = 1\) of \(\dfrac1f\)); vertical asymptote \(x = -2\) (becomes a zero of \(\dfrac{1}{f}\)); horizontal asymptote \(y = 1\) (stays \(y = 1\), because \(\dfrac11 = 1\)). \(f(0) = -\tfrac12\) so \(\dfrac{1}{f}\) passes through \((0, -2)\).

Where the graphs meet: \(f = \pm 1\). \(f = 1\) has no solution (\(x - 1 = x + 2\) is false: this is why the asymptote \(y = 1\) is never met). \(f = -1\) gives \(x - 1 = -(x + 2)\), so \(x = -\tfrac12\), and the graphs meet at \(\left(-\tfrac12, -1\right)\).
:::

:::warn Do not take reciprocals of coordinates blindly
A point \((a, m)\) on \(y = f(x)\) gives \(\left(a, \dfrac1m\right)\) on \(y = \dfrac{1}{f(x)}\): the \(x\)-coordinate stays and only the height is inverted. A minimum at height 3 becomes a maximum at height \(\dfrac13\): not at \(x = \dfrac13\). Remember also that a **zero** of \(f\) is not a point at all on the new graph: it is an asymptote.
:::

## The graph of \(y^2 = f(x)\)

Writing \(y^2 = f(x)\) says the **square** of \(y\) is \(f(x)\). Because a square is never negative, there are points only where \(f(x) \geq 0\), and for each such \(x\) there are **two** values of \(y\): \(y = \sqrt{f(x)}\) and \(y = -\sqrt{f(x)}\).

:::key \(y^2 = f(x)\)
- **No curve** where \(f(x) < 0\). The graph exists only over the \(x\)-values where \(y = f(x)\) is on or above the \(x\)-axis.
- **Symmetric about the \(x\)-axis**: draw \(y = \sqrt{f(x)}\) (above the axis) and reflect it.
- Where \(f(x) = 0\) the curve meets the \(x\)-axis. If \(f\) cuts the axis there with a non-zero gradient, the curve has a **vertical tangent** (the "nose" of the curve), because \(2y\dfrac{dy}{dx} = f'(x)\) and \(y \to 0\).
- Where \(f\) has a turning point at height \(h > 0\), the curve has points of greatest or least \(|y|\), equal to \(\sqrt{h}\), at the same \(x\).
- Where \(0 < f < 1\), \(\sqrt{f} > f\); where \(f > 1\), \(\sqrt{f} < f\). The curve \(y^2 = f\) is flatter than \(y = f\) when \(f\) is large.
:::

:::eg Describe the graph of \(y^2 = x^2 - 4\) and of \(y^2 = 4 - x^2\).
**\(y^2 = x^2 - 4\).** \(f(x) = x^2 - 4 \geq 0\) when \(|x| \geq 2\). So there is no curve for \(-2 < x < 2\), and two separate parts, one for \(x \geq 2\) and one for \(x \leq -2\), each symmetric about the \(x\)-axis, with vertical tangents at \((\pm 2, 0)\). Rearranged, \(x^2 - y^2 = 4\) is a **hyperbola**; for large \(x\), \(y \approx \pm x\).

**\(y^2 = 4 - x^2\).** \(f(x) \geq 0\) when \(|x| \leq 2\). Rearranged, \(x^2 + y^2 = 4\): a **circle**, centre the origin, radius 2, with vertical tangents at \((\pm 2, 0)\) and greatest \(|y| = \sqrt{4} = 2\) at \(x = 0\).
:::

:::eg Sketch \(y^2 = (x + 1)(x - 1)(x - 3)\).
\(f(x) = (x + 1)(x - 1)(x - 3) = x^3 - 3x^2 - x + 3\) is a cubic with positive leading coefficient and roots at \(-1\), \(1\) and \(3\). Its sign: negative for \(x < -1\), positive for \(-1 < x < 1\), negative for \(1 < x < 3\), positive for \(x > 3\).

So \(y^2 = f(x)\) has two parts:
- an **oval** for \(-1 \leq x \leq 1\), with vertical tangents at \((-1, 0)\) and \((1, 0)\);
- an **open branch** for \(x \geq 3\), starting at \((3, 0)\) with a vertical tangent and spreading out as \(x\) grows.

Nothing is drawn for \(x < -1\) or for \(1 < x < 3\).

The cubic has a local maximum where \(f'(x) = 3x^2 - 6x - 1 = 0\), at \(x = 1 - \dfrac{2}{\sqrt 3} = -0.155\), where \(f = 3.08\). So the greatest \(|y|\) on the oval is \(\sqrt{3.08} = 1.75\).
:::

:::plot The curve \(y^2 = (x + 1)(x - 1)(x - 3)\): an oval between \(x = -1\) and \(x = 1\), and a separate open branch starting at \(x = 3\). Each is symmetric about the \(x\)-axis, with a vertical tangent where it meets the axis. There is no curve for \(1 < x < 3\).
--f "sqrt(x**3-3*x**2-x+3)" --f "-sqrt(x**3-3*x**2-x+3)" --label "y = √f(x)" --label "y = −√f(x)" --x -2 5 --y -8 8 --xstep 2 --legend tr
:::

:::eg A designer models the boundary of a small ornamental pond by the oval part of the curve \(y^2 = (x + 1)(x - 1)(x - 3)\), with \(x\) and \(y\) in units of 10 metres. Find the length of the pond from end to end, and its greatest width, to the nearest metre.
The oval runs from \(x = -1\) to \(x = 1\): a length of 2 units, which is 20 m.

The width at a given \(x\) is \(2\sqrt{f(x)}\), greatest where \(f\) is greatest on the oval. From the previous example, \(f\) is greatest, \(3.079\), at \(x = 1 - \dfrac{2}{\sqrt{3}}\). So the greatest width is
\[2\sqrt{3.079} = 3.51 \text{ units} = 35.1 \text{ m}\]
The pond is 20 m long and 35 m wide at its widest: it is wider than it is long, because the oval is "squashed" along the \(x\)-axis.
:::

:::warn Where \(f\) is negative there is no graph
The most common slip with \(y^2 = f(x)\) is to draw a curve below the \(x\)-axis for \(x\) where \(f(x) < 0\), copying the sketch of \(y = f(x)\). Square roots of negative numbers are not real. Shade or mark the \(x\)-intervals where \(f < 0\) as "no curve" before drawing anything.
:::

## Using sketches to solve equations and inequalities

A sketch shows **how many** solutions to expect and **where** they lie, which guards against lost and false roots. Equations with a modulus produce false roots: check each root against the branch it came from.

:::eg Solve \(|x^2 - 2x - 3| < 2x + 1\).
**Sketch.** Draw \(y = |x^2 - 2x - 3|\) (the parabola with the part between its roots \(-1\) and 3 reflected into a bump of height 4 at \(x = 1\)) and the line \(y = 2x + 1\), which crosses the \(x\)-axis at \(x = -\tfrac12\). The inequality holds where the modulus graph is **below** the line.

**Intersections.** Each branch of the modulus graph gives its own equation.

Right-hand and left-hand arms, where \(x^2 - 2x - 3 \geq 0\) (for \(x \leq -1\) or \(x \geq 3\)):
\[\begin{aligned}
x^2 - 2x - 3 &= 2x + 1 \\
x^2 - 4x - 4 &= 0 \\
x &= 2 \pm 2\sqrt{2}
\end{aligned}\]
Only \(x = 2 + 2\sqrt{2} = 4.83\) lies in \(x \geq 3\). The other root, \(2 - 2\sqrt{2} = -0.83\), is **not** in the region where this branch applies (\(x \leq -1\)), so it is a false root.

The middle bump, \(-1 \leq x \leq 3\), where the modulus graph is \(-(x^2 - 2x - 3)\):
\[\begin{aligned}
-x^2 + 2x + 3 &= 2x + 1 \\
x^2 &= 2
\end{aligned}\]
Only \(x = \sqrt{2}\) lies in \(-1 \leq x \leq 3\); \(x = -\sqrt{2} = -1.41\) is a false root.

**Read the sketch.** For \(x < -\tfrac12\) the line is below the \(x\)-axis, so it is below the modulus graph (which is never negative): the inequality fails. For \(-\tfrac12 < x < \sqrt{2}\) the bump is above the line (at \(x = -\tfrac12\) the bump is 1.75 high and the line is at 0). The two graphs meet at \(x = \sqrt{2}\) and at \(x = 2 + 2\sqrt{2}\), and between those the line is above the graph. Beyond \(2 + 2\sqrt{2}\) the parabola's right arm climbs above the line again.

\[\sqrt{2} < x < 2 + 2\sqrt{2}\]
**Check** with \(x = 3\): \(|9 - 6 - 3| = 0 < 7\). True. With \(x = 1\): \(|-4| = 4 < 3\). False, as it should be.
:::

:::plot The graph of \(y = |x^2 - 2x - 3|\) and the line \(y = 2x + 1\). The line is above the graph between the intersections at \(x = \sqrt{2}\) and \(x = 2 + 2\sqrt{2}\), which is where the inequality \(|x^2 - 2x - 3| < 2x + 1\) holds. The line meets the \(x\)-axis at \(x = -\tfrac12\).
--f "abs(x**2-2*x-3)" --f "2*x+1" --label "y = |x² − 2x − 3|" --label "y = 2x + 1" --x -2.5 6 --y -2 14 --xstep 2 --pt "1.414,3.828,(√2, 1 + 2√2)@se" --pt "4.828,10.657,(2 + 2√2, 5 + 4√2)@se" --legend tl
:::

:::eg Use the sketch of \(y = \dfrac{1}{x^2 - 4}\) to solve \(\dfrac{1}{x^2 - 4} \geq 1\).
On the graph, \(\dfrac{1}{x^2 - 4}\) is at least 1 only on the two branches that rise to \(+\infty\) at \(x = \pm 2\), that is for \(|x| > 2\), and only up to the points where \(\dfrac{1}{f} = 1\): \(x = \pm\sqrt{5}\).

So \(2 < x \leq \sqrt{5}\) or \(-\sqrt{5} \leq x < -2\).

**Algebraic check.** \(\dfrac{1}{x^2 - 4} \geq 1\) needs \(x^2 - 4 > 0\) (so that \(\dfrac{1}{x^2 - 4}\) is positive), and then multiplying by it keeps the inequality: \(1 \geq x^2 - 4\), so \(x^2 \leq 5\). Together: \(4 < x^2 \leq 5\), which is the same set.
:::

### Inequalities with rational functions in exact form

Sketches are best when the question gives a graph. When the inequality is between two **algebraic** fractions, the safest route is to move everything to one side, form a **single fraction**, find the critical values (zeros of the numerator and of the denominator), and test the sign in each interval.

:::warn Never multiply by something of unknown sign
Multiplying an inequality by \(x - 1\) is correct only if \(x - 1 > 0\); if it is negative the inequality reverses. You do not know which. Either multiply by a **square** such as \((x - 1)^2\), which is never negative, or move all terms to one side and use a sign table. Cross-multiplying "to clear the fractions" is the commonest way to lose solutions.
:::

:::eg Find the exact set of values of \(x\) for which \(\dfrac{2x}{x + 3} > \dfrac{1}{x - 1}\).
Move everything to one side and combine:
\[\begin{aligned}
\frac{2x}{x + 3} - \frac{1}{x - 1} &> 0 \\
\frac{2x(x - 1) - (x + 3)}{(x + 3)(x - 1)} &> 0 \\
\frac{2x^2 - 3x - 3}{(x + 3)(x - 1)} &> 0
\end{aligned}\]
The numerator is zero when \(x = \dfrac{3 \pm \sqrt{9 + 24}}{4} = \dfrac{3 \pm \sqrt{33}}{4}\), that is \(-0.686\) and \(2.186\). The denominator is zero at \(x = -3\) and \(x = 1\).

The four critical values in order are \(-3\), \(\dfrac{3 - \sqrt{33}}{4}\), \(1\), \(\dfrac{3 + \sqrt{33}}{4}\). For large \(x\) the fraction is positive (the numerator's leading coefficient and the denominator's are both positive). The sign changes at every critical value, since each is a simple zero or a simple pole.

| Interval | Sign of the fraction |
|---|---|
| \(x > \frac{3 + \sqrt{33}}{4}\) | \(+\) |
| \(1 < x < \frac{3 + \sqrt{33}}{4}\) | \(-\) |
| \(\frac{3 - \sqrt{33}}{4} < x < 1\) | \(+\) |
| \(-3 < x < \frac{3 - \sqrt{33}}{4}\) | \(-\) |
| \(x < -3\) | \(+\) |

The fraction is positive for
\[x < -3 \quad\text{or}\quad \frac{3 - \sqrt{33}}{4} < x < 1 \quad\text{or}\quad x > \frac{3 + \sqrt{33}}{4}\]
**Check** with \(x = 0\): \(0 > \dfrac{1}{-1} = -1\), true, and \(0\) is in \(\left(\tfrac{3 - \sqrt{33}}{4}, 1\right)\). With \(x = 1.5\): \(\dfrac{3}{4.5} = 0.667 > \dfrac{1}{0.5} = 2\), false, and \(1.5\) is in the excluded interval.
:::

A sketch gives the same set quickly when one side is a line, as here.

:::eg Use a sketch to find the set of values of \(x\) for which \(\dfrac{x^2 - 4}{x^2 - 1} > 2\), and confirm it algebraically.
The curve \(y = \dfrac{x^2 - 4}{x^2 - 1}\) is the one sketched in [Rational functions and their graphs](#math.fm.rational): asymptotes \(x = \pm 1\) and \(y = 1\), with a minimum at \((0, 4)\) between the vertical asymptotes. The outer branches stay below \(y = 1\), so below \(y = 2\). The middle branch lies at or above 4, so above \(y = 2\) for every \(x\) between the asymptotes.

The solution is \(-1 < x < 1\).

**Algebraic check.**
\[\begin{aligned}
\frac{x^2 - 4}{x^2 - 1} - 2 &> 0 \\
\frac{x^2 - 4 - 2x^2 + 2}{x^2 - 1} &> 0 \\
\frac{-(x^2 + 2)}{x^2 - 1} &> 0
\end{aligned}\]
The numerator is always negative, so the fraction is positive only when \(x^2 - 1 < 0\), that is \(-1 < x < 1\).
:::

:::plot The curve \(y = \dfrac{x^2 - 4}{x^2 - 1}\) against the line \(y = 2\). The curve is above the line only on the middle branch, between the asymptotes \(x = -1\) and \(x = 1\).
--f "(x**2-4)/(x**2-1)" --hline 2 --vline -1 --vline 1 --label "y = (x² − 4)/(x² − 1)" --x -4 4 --y -6 9 --xstep 2 --legend tr
:::

## Putting it together

:::eg (Exam style) The function \(f\) is defined by \(f(x) = \dfrac{(x - 2)^2}{x + 1}\), \(x \neq -1\). The graph of \(y = f(x)\) has asymptotes \(x = -1\) and \(y = x - 5\), a minimum point at \((2, 0)\) and a maximum point at \((-4, -12)\). (a) Sketch the graph of \(y = \dfrac{1}{f(x)}\), stating the equations of the asymptotes and the coordinates of the stationary point and of the intercepts. (b) Sketch the graph of \(y = f(|x|)\). (c) Find, in exact form, the set of values of \(x\) for which \(|f(x)| < 2\).
**(a)** The zero of \(f\) at \(x = 2\) (a repeated zero, with \(f \geq 0\) either side) gives a vertical asymptote \(x = 2\), with \(\dfrac{1}{f} \to +\infty\) on both sides. [B1]

The asymptote \(x = -1\) of \(f\) becomes a zero of \(\dfrac{1}{f}\): the curve passes through \((-1, 0)\). For \(x > -1\), \(f > 0\), so on \(-1 < x < 2\) the curve rises from \((-1, 0)\) to \(+\infty\). For \(x < -1\), \(f < 0\), so the curve is below the axis, rising to \((-1, 0)\). [B1]

The maximum \((-4, -12)\) of \(f\) gives a minimum \(\left(-4, -\tfrac{1}{12}\right)\). [B1]

As \(x \to \pm\infty\), \(|f| \to \infty\), so \(\dfrac{1}{f} \to 0\): the \(x\)-axis is an asymptote, approached from below on the left and from above on the right. The \(y\)-intercept is \(\left(0, \tfrac14\right)\), since \(f(0) = 4\). [B1]

**(b)** Keep the part with \(x \geq 0\) and reflect it in the \(y\)-axis. The graph is symmetric about the \(y\)-axis. [B1]

Minima at \((2, 0)\) and \((-2, 0)\), and a peak with a corner at \((0, 4)\). [B1]

There is no vertical asymptote now (\(x = -1\) was on the deleted part, and \(x = 1\) is not an asymptote). The oblique asymptotes are \(y = x - 5\) for large positive \(x\) and \(y = -x - 5\) for large negative \(x\). [B1]

**(c)** Find where \(f(x) = 2\) (this applies on the right branch, where \(f \geq 0\)):
\[\begin{aligned}
(x - 2)^2 &= 2(x + 1) \\
x^2 - 6x + 2 &= 0
\end{aligned}\] [M1]
\[x = 3 \pm \sqrt{7}\] [A1]
On the left branch \(f \leq -12\), so \(|f| \geq 12\). Alternatively \(f = -2\) gives \(x^2 - 2x + 6 = 0\), with discriminant \(4 - 24 < 0\), so there is no solution. Either way, the left branch contributes nothing. [M1]

On the right branch, \(|f| = f\) is below 2 between the two roots. [M1]
\[3 - \sqrt{7} < x < 3 + \sqrt{7}\] [A1]
(The inequality is strict because \(|f| = 2\) at the ends.) **Check**: \(f(1) = 0.5 < 2\), true.
:::

:::plot The graph of \(y = \dfrac{1}{f(x)} = \dfrac{x + 1}{(x - 2)^2}\) for the example above. It has the vertical asymptote \(x = 2\), meets the \(x\)-axis at \(x = -1\), has a minimum at \(\left(-4, -\tfrac1{12}\right)\) and crosses the \(y\)-axis at \(\left(0, \tfrac14\right)\).
--f "(x+1)/(x-2)**2" --label "y = 1/f(x) = (x + 1)/(x − 2)²" --x -10 8 --y -0.2 0.6 --vline 2 --xstep 5 --pt "-4,-0.0833,(−4, −1/12)@se" --pt "-1,0,(−1, 0)@ne" --pt "0,0.25,(0, 1/4)@ne" --legend tl
:::

:::plot The graph of \(y = f(|x|) = \dfrac{(|x| - 2)^2}{|x| + 1}\) for the same \(f\): symmetric about the \(y\)-axis, with minima at \((\pm 2, 0)\), a peak with a corner at \((0, 4)\), and oblique asymptotes \(y = |x| - 5\).
--f "(abs(x)-2)**2/(abs(x)+1)" --f "abs(x)-5" --label "y = f(|x|)" --label "y = |x| − 5" --x -10 10 --y -8 10 --xstep 5 --pt "2,0,(2, 0)@se" --pt "-2,0,(−2, 0)@sw" --pt "0,4,(0, 4)@ne" --legend tr
:::

:::exam Sketch questions
Label every feature the question asks for: asymptote equations, intercepts, turning points. For \(y = \dfrac{1}{f}\) mark which way each branch goes at the asymptotes; for \(y = f(|x|)\) draw the corner on the \(y\)-axis, not a smooth curve. When an exam says "hence", use your sketch for the solution. Nothing in this chapter is on MF19. When an inequality asks for an **exact** set, give the critical values as surds or fractions (such as \(3 \pm \sqrt{7}\)) with the correct inequality signs, and test one value from each interval.
:::

:::eg Spot the error: solve \(|x - 4| < 2x - 5\), for 4 marks.
A student wrote this answer.

Line 1: \(x - 4 = 2x - 5\), so \(x = 1\)
Line 2: \(-(x - 4) = 2x - 5\), so \(x = 3\)
Line 3: the graphs meet at \(x = 1\) and \(x = 3\), so the inequality is true for \(x > 1\)

Lines 1 and 2 solve both branches of the modulus. [M1] They give both candidates correctly. [A1]

**Line 3 does not check the candidates.** [M0] At \(x = 1\), \(2x - 5 = -3\), which is negative, but \(|x - 4|\) cannot equal \(-3\): \(x = 1\) is a false root from the branch \(x - 4 = 2x - 5\), which only applies for \(x \geq 4\). The student also does not look at where the graphs are relative to each other. [A0] The student scores 2 out of 4.

Correct line 3: a sketch shows the V with vertex \((4, 0)\) and the line \(y = 2x - 5\) meeting it only once, at \(x = 3\), after which the line is above the V. [M1] So the solution is \(x > 3\). [A1]

**Check**: \(x = 5\): \(1 < 5\), true. \(x = 2\): \(2 < -1\), false, as is every \(x\) below 3.
:::

:::try Start easy, finish at exam standard
Q: Describe how to obtain the graph of \(y = |x - 3|\) from that of \(y = x - 3\).
A: Reflect the part of the line below the \(x\)-axis (that is, for \(x < 3\)) in the \(x\)-axis. The result is a V with its vertex at \((3, 0)\).
Q: The graph of \(y = f(x)\) has a minimum at \((2, -5)\). What are the coordinates of the corresponding point on \(y = |f(x)|\)?
A: The minimum is below the axis, so it is reflected: \((2, 5)\), which is a local maximum of \(|f|\).
Q: Sketch \(y = f(|x|)\) for \(f(x) = x^2 - 4\) and state the intercepts.
A: \(f(|x|) = |x|^2 - 4 = x^2 - 4\), because \(|x|^2 = x^2\). The graph is unchanged: intercepts \((\pm 2, 0)\) and \((0, -4)\). (An even function has \(f(|x|) = f(x)\).)
Q: \(f(x) = x^2 - 6x + 5\). Write down the \(x\)-intercepts of \(y = f(|x|)\).
A: For \(x \geq 0\), \(x^2 - 6x + 5 = 0\) gives \(x = 1\) and \(x = 5\). By symmetry \(x = -1\) and \(x = -5\) too. The intercepts are \((\pm 1, 0)\) and \((\pm 5, 0)\).
Q: The graph of \(y = f(x)\) has a maximum at \((3, 4)\) and crosses the \(x\)-axis at \(x = 1\) and \(x = 5\). Describe \(y = \dfrac{1}{f(x)}\) near these points.
A: At \(x = 1\) and \(x = 5\), \(f = 0\), so there are vertical asymptotes \(x = 1\) and \(x = 5\). The maximum \((3, 4)\) becomes a minimum \(\left(3, \tfrac14\right)\) (this is the "U" between the asymptotes).
Q: For which \(x\) does \(y^2 = 9 - x^2\) have points on the curve, and what shape is it?
A: \(9 - x^2 \geq 0\), so \(-3 \leq x \leq 3\). It is the circle \(x^2 + y^2 = 9\).
Q: Where is there no graph of \(y^2 = x(x - 4)\)?
A: \(x(x - 4) < 0\) for \(0 < x < 4\), so there is no curve there.
Q: Solve \(|3x - 2| = x + 4\), and check each root.
A: \(3x - 2 = x + 4\) gives \(x = 3\); \(-(3x - 2) = x + 4\) gives \(x = -\tfrac12\). Check: \(|9 - 2| = 7 = 3 + 4\), and \(\left|-\tfrac32 - 2\right| = \tfrac72 = -\tfrac12 + 4\). Both work.
Q: Solve \(\dfrac{1}{x - 1} > 2\).
A: Move over: \(\dfrac{1 - 2(x - 1)}{x - 1} = \dfrac{3 - 2x}{x - 1} > 0\). The critical values are 1 and \(\tfrac32\), and the fraction is positive between them: \(1 < x < \tfrac32\).
Q: How many solutions does \(|x^2 - 4| = k\) have for \(k = 2\), \(k = 4\) and \(k = 6\)?
A: The graph of \(|x^2 - 4|\) has a "W" shape with corners at \((\pm 2, 0)\) and a local maximum \((0, 4)\). A line \(y = 2\) meets it four times; \(y = 4\) meets it three times (touching the top of the bump); \(y = 6\) meets it twice.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Sketch the graph of \(y = |x^2 - 4x|\), stating the coordinates of the axis intercepts and of the maximum point.
A: The parabola \(x^2 - 4x\) is negative for \(0 < x < 4\); reflect that part. [B1] The graph meets the axes at \((0, 0)\) and \((4, 0)\), with corners at both. [B1] The maximum on the bump is \((2, 4)\). [B1]
Q: [3 marks] ★ Sketch the graph of \(y = x^2 - 4x - 5\) and use it to sketch \(y = f(|x|)\) where \(f(x) = x^2 - 4x - 5\).
A: \(y = f(|x|)\) is symmetrical about the \(y\)-axis. [B1] It crosses the axes at \((\pm 5, 0)\) and \((0, -5)\). [B1] The minima are at \((\pm 2, -9)\), with a corner at \((0, -5)\). [B1]
Q: [5 marks] ★★ The function \(f\) is defined by \(f(x) = x^2 - 5x + 4\). Sketch the graph of \(y = \dfrac{1}{f(x)}\), showing the asymptotes, the \(y\)-intercept and the coordinates of the turning point.
A: \(f(x) = (x - 1)(x - 4)\), so the vertical asymptotes are \(x = 1\) and \(x = 4\). [B1]
\(\dfrac{1}{f} \to 0\) as \(x \to \pm\infty\), so \(y = 0\) is an asymptote, and the outer branches are above the axis (\(f > 0\)). [B1]
The minimum of \(f\) is \(f\left(\tfrac52\right) = -\tfrac94\), so \(\dfrac{1}{f}\) has a maximum at \(\left(\tfrac52, -\tfrac49\right)\). [B1]
The middle branch lies below the axis, between the asymptotes. [B1]
The \(y\)-intercept is \(\left(0, \tfrac14\right)\). [B1]
Q: [4 marks] ★★ Sketch the curve \(y^2 = (x - 1)(x - 5)\), stating where it has no points, the intercepts, and the equations of its asymptotes.
A: \((x - 1)(x - 5) < 0\) for \(1 < x < 5\), so no points there. [B1]
The curve is symmetrical about the \(x\)-axis and meets it at \((1, 0)\) and \((5, 0)\) with vertical tangents. [B1]
\(y^2 = (x - 3)^2 - 4\), so for large \(|x|\), \(y \approx \pm(x - 3)\). [B1] The asymptotes are \(y = x - 3\) and \(y = -(x - 3)\). [B1]
Q: [6 marks] ★★ Find the set of values of \(x\) for which \(\dfrac{3}{x - 1} < x + 1\).
A: \(\dfrac{3}{x - 1} - (x + 1) < 0\) [M1]
\(\dfrac{3 - (x^2 - 1)}{x - 1} = \dfrac{4 - x^2}{x - 1} < 0\) [A1]
Critical values \(x = -2\), \(1\), \(2\). [M1 A1]
The fraction is negative for \(-2 < x < 1\) and for \(x > 2\) (test \(x = 0\): \(\tfrac{4}{-1} < 0\); \(x = 3\): \(\tfrac{-5}{2} < 0\); \(x = 1.5\): positive; \(x = -3\): \(\tfrac{-5}{-4}\), positive). [M1]
\(-2 < x < 1\) or \(x > 2\). [A1]
Q: [6 marks] ★★ (a) Solve \(|x^2 - 4| = 3x\). (b) Hence solve \(|x^2 - 4| < 3x\).
A: (a) \(x^2 - 4 = 3x\) gives \(x^2 - 3x - 4 = 0\), so \(x = 4\) or \(x = -1\); \(-(x^2 - 4) = 3x\) gives \(x^2 + 3x - 4 = 0\), so \(x = 1\) or \(x = -4\). [M1 A1]
Since \(|x^2 - 4| \geq 0\), \(3x \geq 0\), so \(x = -1\) and \(x = -4\) are false roots. [M1]
The solutions are \(x = 1\) and \(x = 4\). [A1]
(b) On a sketch the line \(y = 3x\) is above the graph of \(|x^2 - 4|\) between the two intersections. [B1]
\(1 < x < 4\). [A1]
Q: [12 marks] (#math.fm.rational) ★★★ The curve \(C\) has equation \(y = f(x)\), where \(f(x) = \dfrac{x^2}{x - 2}\). (a) Find the equations of the asymptotes, and sketch \(C\), given that its stationary points are \((0, 0)\) and \((4, 8)\). (b) Sketch the graph of \(y = \dfrac{1}{f(x)}\), showing the stationary point and the asymptotes. (c) Find the set of values of \(x\) for which \(f(x) < 3x\).
H: For (a), divide: \(x^2 = (x - 2)(x + 2) + 4\), so \(f(x) = x + 2 + \dfrac{4}{x - 2}\).
H: In (b), \(f\) has a double zero at \(x = 0\) and \(f \leq 0\) for \(x < 2\): which way does \(\dfrac1f\) go at \(x = 0\)?
H: In (c), form a single fraction with a numerator that factorises: \(x(x - 3)\).
A: (a) \(x = 2\) [B1] and \(y = x + 2\). [M1 A1]
The curve has a maximum at the origin (left branch, below the oblique asymptote) and a minimum at \((4, 8)\) (right branch, above it). The sketch shows both branches, asymptotes and stationary points. [B1]
(b) \(\dfrac{1}{f} = \dfrac{x - 2}{x^2}\): vertical asymptote \(x = 0\), with \(\dfrac1f \to -\infty\) on both sides; [B1] zero at \(x = 2\); [B1]
maximum \(\left(4, \tfrac18\right)\); [B1] asymptote \(y = 0\), approached from below on the left and from above on the right. [B1]
(c) \(\dfrac{x^2}{x - 2} - 3x < 0\), that is \(\dfrac{x^2 - 3x(x - 2)}{x - 2} = \dfrac{-2x(x - 3)}{x - 2} < 0\). [M1 A1]
So \(\dfrac{x(x - 3)}{x - 2} > 0\), with critical values 0, 2, 3. [M1]
Positive for \(0 < x < 2\) or \(x > 3\). [A1]
Q: [10 marks] ★★★ The curve \(C\) has equation \(y = \dfrac{x^2 + 3}{x + 1}\), \(x \neq -1\), with a minimum at \((1, 2)\) and a maximum at \((-3, -6)\). (a) Sketch \(C\), including its asymptotes, and sketch \(y = |f(x)|\) where \(f(x) = \dfrac{x^2 + 3}{x + 1}\). (b) Find, in exact form, the set of values of \(x\) for which \(\dfrac{x^2 + 3}{x + 1} > 3\).
H: Divide: \(x^2 + 3 = (x + 1)(x - 1) + 4\), so the asymptotes are \(x = -1\) and \(y = x - 1\).
H: For (b), the inequality becomes \(\dfrac{x^2 - 3x}{x + 1} > 0\) after subtracting 3 and combining.
A: (a) Asymptotes \(x = -1\) and \(y = x - 1\) [B1 B1], stationary points shown, right branch above the oblique line. [B1]
\(|f|\): reflect the left branch (below the axis), so the maximum becomes a minimum \((-3, 6)\) and the left branch rises towards \(+\infty\) as \(x \to -\infty\) and at \(x = -1\). [B1] The right branch is unchanged. [B1]
(b) \(\dfrac{x^2 + 3}{x + 1} - 3 = \dfrac{x^2 + 3 - 3x - 3}{x + 1} = \dfrac{x(x - 3)}{x + 1} > 0\). [M1 A1]
Critical values \(-1\), \(0\), \(3\). [M1]
Positive for \(-1 < x < 0\) or \(x > 3\). [M1 A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ (a) Sketch the graph of \(y = |x^2 - 4|\). (b) Find the number of real solutions of \(|x^2 - 4| = k\) for each real value of \(k\). (c) How does the answer change for \(f(|x|) = k\), where \(f(x) = x^2 - 4\)?
H: The local maximum of the bump between \(x = -2\) and \(x = 2\) is at height 4.
H: Count intersections of a horizontal line with the graph, for \(k\) in each interval.
A: (a) A "W": corners \((\pm 2, 0)\), a local maximum \((0, 4)\), rising to infinity for \(|x| > 2\). [B1]
(b) \(k < 0\): none. \(k = 0\): 2. [B1] \(0 < k < 4\): 4. [B1] \(k = 4\): 3. [B1] \(k > 4\): 2. [B1]
(c) \(f(|x|) = x^2 - 4\) is unchanged (even function), so \(x^2 - 4 = k\) has 2 solutions for \(k > -4\), 1 solution for \(k = -4\), none for \(k < -4\). [B1]
Q: [8 marks] ★★★ The curve \(C\) has equation \(y^2 = (x - 1)^2(x + 2)\). (a) Show that \(C\) is symmetric about the \(x\)-axis and exists only for \(x \geq -2\). (b) Show that \(C\) passes through \((1, 0)\) with two different gradients there, and find them. (c) Find the greatest value of \(y\) on the loop that lies between \(x = -2\) and \(x = 1\), and sketch \(C\).
H: \((x - 1)^2 \geq 0\), so the sign of \(f\) is the sign of \(x + 2\).
H: Near \(x = 1\), write \(y = \pm(x - 1)\sqrt{x + 2}\) and differentiate.
H: On the loop \(y^2 = (1 - x)^2(x + 2)\): maximise this product.
A: (a) \(y^2\) is unchanged when \(y\) is replaced by \(-y\). [B1] \((x - 1)^2 \geq 0\), so \(y^2 \geq 0\) needs \(x + 2 \geq 0\), \(x \geq -2\). [B1]
(b) \(y = \pm(x - 1)\sqrt{x + 2}\), so \(\dfrac{dy}{dx} = \pm\left[\sqrt{x + 2} + \dfrac{x - 1}{2\sqrt{x + 2}}\right]\). [M1]
At \(x = 1\) this is \(\pm\sqrt{3}\): two branches cross at \((1, 0)\) with gradients \(\sqrt{3}\) and \(-\sqrt{3}\). [A1]
(c) Let \(g = (1 - x)^2(x + 2)\). Then \(g' = -2(1 - x)(x + 2) + (1 - x)^2 = (1 - x)(-3 - 3x)\). [M1] This is zero at \(x = -1\) (for \(-2 < x < 1\)). [A1]
\(g(-1) = 4 \times 1 = 4\), so the greatest \(y\) is 2. [A1]
The sketch shows the loop from \((-2, 0)\) (vertical tangent) through \((-1, \pm 2)\) back to the crossing point \((1, 0)\), and two branches continuing to the right, spreading out. [B1]
:::

:::quiz
? The graph of \(y = f(x)\) has a minimum at \((3, -2)\). What is the corresponding point on \(y = |f(x)|\)?
- \((3, -2)\), unchanged
+ \((3, 2)\), a local maximum
- \((-3, 2)\)
- \(\left(3, -\tfrac12\right)\)
> The minimum is below the \(x\)-axis, so reflecting it in the \(x\)-axis gives \((3, 2)\), and it becomes a local maximum. \((-3, 2)\) is a reflection in the wrong axis, and \(\left(3, -\tfrac12\right)\) belongs to \(\dfrac{1}{f}\).
? Which description of \(y = f(|x|)\) is correct?
- Reflect the parts below the \(x\)-axis in the \(x\)-axis
+ Keep the part with \(x \geq 0\) and reflect it in the \(y\)-axis
- Reflect the whole graph in the \(y\)-axis and keep both copies
- Keep the part with \(x \leq 0\) and reflect it in the \(x\)-axis
> \(f(|x|) = f(x)\) for \(x \geq 0\), and \(f(-x)\) for \(x < 0\): the right half is kept and mirrored. The first option describes \(|f(x)|\).
? The graph of \(y = f(x)\) crosses the \(x\)-axis at \(x = 2\). What happens to \(y = \dfrac{1}{f(x)}\) there?
- It crosses the \(x\)-axis at \(x = 2\)
+ It has a vertical asymptote \(x = 2\)
- It has a minimum at \(x = 2\)
- It is the same graph
> \(f(2) = 0\), so \(\dfrac{1}{f(2)}\) is undefined and the values near it are huge. A zero of \(f\) becomes a vertical asymptote of \(\dfrac{1}{f}\).
? For which \(x\) does \(y^2 = x^2 - 9\) have points on its graph?
- \(-3 \leq x \leq 3\)
+ \(x \leq -3\) or \(x \geq 3\)
- All \(x\)
- \(x \geq 3\) only
> \(x^2 - 9 \geq 0\) gives \(x \leq -3\) or \(x \geq 3\). The first option is the circle \(y^2 = 9 - x^2\). The curve is symmetric about the \(x\)-axis and has a branch on each side.
? A student solves \(\dfrac{1}{x - 2} > 3\) by multiplying both sides by \(x - 2\) and gets \(x < \tfrac73\). What goes wrong?
- Nothing: this is correct
+ \(x - 2\) can be negative, which reverses the inequality; the correct set is \(2 < x < \tfrac73\)
- The inequality should be \(x > \tfrac73\)
- The student should have divided by 3 first
> If \(x < 2\) then \(\dfrac{1}{x - 2}\) is negative, so it cannot exceed 3. The solution needs \(x - 2 > 0\), giving \(2 < x < \tfrac73\). Multiplying by an expression of unknown sign is the error.
? The two branches of \(|x - 1| = 2x - 5\) give \(x = 4\) and \(x = 2\). Which are solutions?
- Both
- Neither
+ Only \(x = 4\)
- Only \(x = 2\)
> At \(x = 4\): \(|3| = 3 = 2(4) - 5\), true. At \(x = 2\): \(2x - 5 = -1\), but \(|x - 1|\) cannot be negative, so \(x = 2\) is a false root. Always check each candidate in the original equation.
:::

:::checklist What you can now do
- [ ] I can sketch \(y = |f(x)|\) from \(y = f(x)\) by reflecting the parts below the \(x\)-axis, and find its corners and maxima.
- [ ] I can sketch \(y = f(|x|)\) by reflecting the right half in the \(y\)-axis and find its corner on the \(y\)-axis.
- [ ] I can sketch \(y = \dfrac{1}{f(x)}\) from \(y = f(x)\): asymptotes, zeros, swapped maxima and minima, and the invariant points.
- [ ] I can sketch \(y^2 = f(x)\), stating where there is no curve and where the tangent is vertical.
- [ ] I can use a sketch to solve an equation or inequality involving a modulus, rejecting false roots.
- [ ] I can solve an inequality between rational functions in exact form, using a single fraction and a sign table.
- [ ] I can say how many solutions an equation like \(|f(x)| = k\) has for each \(k\).
:::

:::recap
- \(y = |f(x)|\): reflect the parts below the \(x\)-axis in the \(x\)-axis; corners at the roots.
- \(y = f(|x|)\): keep \(x \geq 0\), reflect in the \(y\)-axis; symmetric about the \(y\)-axis, with a corner on it.
- \(y = \dfrac{1}{f(x)}\): zeros of \(f\) become vertical asymptotes; vertical asymptotes of \(f\) become zeros; maxima and minima swap with heights inverted; the sign is kept; \(f = \pm 1\) are invariant points.
- \(y^2 = f(x)\): no curve where \(f < 0\); symmetric about the \(x\)-axis; vertical tangent where \(f\) crosses the axis.
- Solve equations with a modulus by taking both branches, then check each root against its branch.
- Inequalities: one side zero, single fraction, critical values, sign table. Never multiply by an expression of unknown sign.
:::

:::links
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · tutorials on every Further Pure topic, including sketching related graphs
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · graded questions with answers on curve sketching and inequalities
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · type \(y = |f(x)|\), \(y = f(|x|)\) and \(y = 1/f(x)\) for any \(f\) and compare
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Polar coordinates](#math.fm.polar) describes a point by its distance and direction from a fixed point, and finds areas with \(\tfrac12 \int r^2\,d\theta\).
