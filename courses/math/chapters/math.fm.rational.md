@chapter math.fm.rational
@title Rational functions and their graphs
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary A rational function is one polynomial divided by another. You will find its vertical, horizontal and oblique asymptotes, its intercepts and turning points, whether it crosses its own asymptote, and the set of values it takes (using a discriminant), then put every feature into a clean sketch.

:::why
The graph of a rational function is built from pieces that run off to infinity, hug a line, and sometimes turn back. Reading those pieces correctly is a skill that comes up again and again in Further Mathematics: in inequalities, in integration, in the behaviour of a model for large inputs. It is also a reliable source of marks, because every feature can be found by a short, mechanical step.
:::

**Before you start**, you need the discriminant from [Quadratics](#math.p1.quadratics), the idea of range from [Functions](#math.p1.functions), the quotient rule from [Further differentiation](#math.p3.diff) and polynomial division from [Modulus and polynomials](#math.p3.algebra). Turning points by differentiation are in [Differentiation](#math.p1.diff).

:::try Warm-up
Q: Find the set of values of \(k\) for which \(x^2 + kx + 9 = 0\) has real roots. (from [Quadratics](#math.p1.quadratics))
A: Real roots need \(k^2 - 36 \geq 0\), so \(k \leq -6\) or \(k \geq 6\).
Q: Divide \(x^2 - x + 3\) by \(x - 2\), giving the quotient and the remainder. (from [Modulus and polynomials](#math.p3.algebra))
A: \(x^2 - x + 3 = (x - 2)(x + 1) + 5\), so the quotient is \(x + 1\) and the remainder is 5.
Q: Differentiate \(\dfrac{x}{x + 1}\). (from [Further differentiation](#math.p3.diff))
A: By the quotient rule, \(\dfrac{(x + 1) - x}{(x + 1)^2} = \dfrac{1}{(x + 1)^2}\).
:::

## What a rational function is

A fraction of two whole numbers is a rational number. In the same way, a fraction of two polynomials is a rational function.

:::def Rational function
A function that can be written as \(f(x) = \dfrac{p(x)}{q(x)}\), where \(p(x)\) and \(q(x)\) are polynomials and \(q(x)\) is not the zero polynomial. It is defined for every \(x\) except those where \(q(x) = 0\).
:::

:::def Asymptote
A straight line that a curve gets closer and closer to, as \(x\) or \(y\) becomes very large in size (positive or negative). A **vertical** asymptote has the form \(x = a\), a **horizontal** one \(y = b\), and an **oblique** (sloping) one \(y = mx + c\).
:::

The syllabus asks for rational functions whose numerator and denominator have degree **at most 2**, so every function in this chapter is a linear or quadratic divided by a linear or quadratic. You are not asked to plot points carefully. You are asked for a sketch that shows the **significant features**: asymptotes, intersections with the axes and turning points. A good sketch is built in a fixed order, and each step below is one item of that order.

## Vertical asymptotes

The function is undefined where the denominator is zero. At such a point there are two possibilities.

- The numerator is **not** zero there. The fraction becomes huge, so the curve shoots off to \(+\infty\) or \(-\infty\) next to that \(x\)-value. There is a **vertical asymptote**.
- The numerator is **also** zero there. A common factor cancels and the graph has a single missing point, a "hole", but no asymptote (see the end of this chapter).

:::key Vertical asymptotes
For \(f(x) = \dfrac{p(x)}{q(x)}\) in its simplest form, each solution of \(q(x) = 0\) gives a vertical asymptote \(x = a\). Find which way the curve goes on each side of it with a **sign test**: put in a value just less than \(a\), then one just greater, and find the sign of \(p\) and of \(q\). A positive fraction goes to \(+\infty\), a negative one to \(-\infty\).
:::

The sign test is worth doing every time. The two sides of a vertical asymptote can go in the same direction or in opposite directions, and only the test tells you which.

:::eg Sketch \(y = \dfrac{2x + 1}{x - 3}\), showing the asymptotes and the intersections with the axes.
**Vertical asymptote.** The denominator is zero at \(x = 3\), where the numerator is 7. So \(x = 3\) is an asymptote.

**Sign test.** Just to the right, \(x = 3.1\): the numerator is positive and the denominator is \(+0.1\), so \(y \to +\infty\). Just to the left, \(x = 2.9\): the numerator is positive and the denominator is \(-0.1\), so \(y \to -\infty\).

**Large \(x\).** Divide the numerator by the denominator:
\[\frac{2x + 1}{x - 3} = 2 + \frac{7}{x - 3}\]
As \(x \to \pm\infty\) the fraction \(\dfrac{7}{x - 3}\) goes to 0, so \(y \to 2\). The horizontal asymptote is \(y = 2\). For large positive \(x\) the fraction is positive, so the curve is above \(y = 2\) on the right. For large negative \(x\) it is negative, so the curve is below \(y = 2\) on the left.

**Axes.** When \(x = 0\), \(y = -\tfrac13\). When \(y = 0\), \(2x + 1 = 0\), so \(x = -\tfrac12\).

**Turning points.** \(\dfrac{dy}{dx} = -\dfrac{7}{(x - 3)^2}\), which is never zero, and is negative everywhere it is defined. So each branch is always falling and there are no turning points.
:::

:::plot The curve \(y = \dfrac{2x + 1}{x - 3}\) has the dashed vertical asymptote \(x = 3\) and the dashed horizontal asymptote \(y = 2\). Both branches fall as \(x\) increases.
--f "(2*x+1)/(x-3)" --label "y = (2x + 1)/(x − 3)" --x -7 11 --y -9 13 --vline 3 --hline 2 --xstep 5 --pt "0,-0.3333,(0, −1/3)@se" --pt "-0.5,0,(−1/2, 0)@sw" --legend tr
:::

## Horizontal asymptotes

For large \(|x|\), only the highest powers of \(x\) matter. In \(\dfrac{3x^2 + 5}{x^2 - 4}\) the \(x^2\) terms dominate, and the fraction behaves like \(\dfrac{3x^2}{x^2} = 3\). Comparing the **degrees** of the numerator and denominator settles every case.

:::key Large-\(x\) behaviour of \(\dfrac{p(x)}{q(x)}\)
| Degree of \(p\) compared with \(q\) | What happens as \(x \to \pm\infty\) |
|---|---|
| less | \(y \to 0\): the horizontal asymptote is \(y = 0\) (the \(x\)-axis) |
| equal | \(y \to\) (leading coefficient of \(p\)) \(\div\) (leading coefficient of \(q\)): a horizontal asymptote |
| one more | no horizontal asymptote: an **oblique** asymptote (next sections) |
:::

To see which side of the asymptote the curve is on, look at \(f(x) - b\) for large \(x\): it is the remainder term after dividing, and its sign is the answer.

:::eg Sketch \(y = \dfrac{2x - 1}{(x + 1)(x - 3)}\).
**Vertical asymptotes.** \(x = -1\) and \(x = 3\). The numerator is \(-3\) at \(x = -1\) and \(5\) at \(x = 3\).

**Horizontal asymptote.** The degree of the numerator (1) is less than that of the denominator (2), so \(y = 0\).

**Signs.** Put the sign of the numerator and of each bracket in a table, using a value in each interval.

| Interval | \(2x - 1\) | \(x + 1\) | \(x - 3\) | \(y\) |
|---|---|---|---|---|
| \(x < -1\) | \(-\) | \(-\) | \(-\) | \(-\) |
| \(-1 < x < \tfrac12\) | \(-\) | \(+\) | \(-\) | \(+\) |
| \(\tfrac12 < x < 3\) | \(+\) | \(+\) | \(-\) | \(-\) |
| \(x > 3\) | \(+\) | \(+\) | \(+\) | \(+\) |

So the curve goes to \(-\infty\) as \(x \to -1^-\) and to \(+\infty\) as \(x \to -1^+\), then to \(-\infty\) as \(x \to 3^-\) and to \(+\infty\) as \(x \to 3^+\). For large \(|x|\) it is below the \(x\)-axis on the left and above it on the right.

**Axes.** \(x = 0\) gives \(y = \tfrac13\). \(y = 0\) gives \(x = \tfrac12\).

**Turning points.** By the quotient rule the numerator of \(\dfrac{dy}{dx}\) is
\[2(x^2 - 2x - 3) - (2x - 1)(2x - 2) = -2x^2 + 2x - 8\]
Its discriminant is \(4 - 64 < 0\), so the numerator is never zero. It is negative for every \(x\), so there are no turning points and every branch falls.
:::

:::plot The curve crosses its own horizontal asymptote, the \(x\)-axis, at \(x = \tfrac12\). The middle branch falls from \(+\infty\) to \(-\infty\) between the asymptotes \(x = -1\) and \(x = 3\), and the \(y\)-intercept is \(\left(0, \tfrac{1}{3}\right)\).
--f "(2*x-1)/((x+1)*(x-3))" --label "y = (2x − 1)/((x + 1)(x − 3))" --x -7 9 --y -7 7 --vline -1 --vline 3 --xstep 4 --pt "0.5,0,(1/2, 0)@ne" --legend tr
:::

Notice that this curve **crosses** its horizontal asymptote, at \(x = \tfrac12\). An asymptote describes what the curve does far away, not whether it meets the line nearby. A horizontal asymptote can be crossed once, several times or never; a vertical one can never be crossed, because \(f\) is undefined there.

## A quadratic over a quadratic

When the degrees are equal there is a horizontal asymptote \(y = b\) where \(b\) is the ratio of the leading coefficients. If the function is even (\(f(-x) = f(x)\)) the graph is symmetrical about the \(y\)-axis, which halves the work.

:::eg Sketch \(y = \dfrac{x^2 - 4}{x^2 - 1}\), and show that it has a turning point at \((0, 4)\).
**Vertical asymptotes.** \(x^2 - 1 = 0\) gives \(x = \pm 1\). The numerator is \(-3\) at both.

**Horizontal asymptote.** The leading coefficients are 1 and 1, so \(y = 1\). Write the function as
\[\frac{x^2 - 4}{x^2 - 1} = 1 - \frac{3}{x^2 - 1}\]
For \(|x| > 1\) the fraction \(\dfrac{3}{x^2 - 1}\) is positive, so the outer branches lie **below** \(y = 1\) and never meet it. For \(|x| < 1\) the curve lies above \(y = 1\).

**Symmetry.** \(f(-x) = f(x)\), so the curve is symmetrical about the \(y\)-axis.

**Axes.** \(x = 0\) gives \(y = 4\). \(y = 0\) gives \(x = \pm 2\).

**Turning point.** By the quotient rule,
\[\frac{dy}{dx} = \frac{2x(x^2 - 1) - (x^2 - 4)(2x)}{(x^2 - 1)^2} = \frac{6x}{(x^2 - 1)^2}\]
This is zero only at \(x = 0\). It is negative for \(-1 < x < 0\) and positive for \(0 < x < 1\), so \((0, 4)\) is a minimum. On the outer branches \(\dfrac{dy}{dx}\) has the sign of \(x\): the right branch rises towards \(y = 1\) from below, the left branch falls away from \(y = 1\).
:::

:::plot Between the asymptotes \(x = -1\) and \(x = 1\) the curve is a "U" with its minimum at \((0, 4)\). The outer branches approach \(y = 1\) from below.
--f "(x**2-4)/(x**2-1)" --label "y = (x² − 4)/(x² − 1)" --x -5 5 --y -7 9 --vline -1 --vline 1 --hline 1 --xstep 4 --pt "0,4,(0, 4)@se" --pt "2,0,(2, 0)@se" --pt "-2,0,(−2, 0)@sw" --legend tr
:::

## Oblique asymptotes

When the numerator has degree **one more** than the denominator, dividing gives a linear quotient plus a remainder term that shrinks to zero.

:::key Oblique asymptote
If \(\dfrac{p(x)}{q(x)} = mx + c + \dfrac{r(x)}{q(x)}\) with \(\dfrac{r(x)}{q(x)} \to 0\) as \(x \to \pm\infty\), then \(y = mx + c\) is an oblique asymptote. The curve lies **above** it where the remainder term is positive and **below** it where the remainder term is negative.
:::

For a quadratic over a linear, \(\dfrac{ax^2 + bx + c}{x - h}\) always becomes \(mx + k + \dfrac{R}{x - h}\) where \(R\) is the value of the numerator at \(x = h\) (by the remainder theorem). So the curve has one vertical asymptote \(x = h\), and the sign of \(R\) decides which side of the oblique line each branch lies on.

:::eg Find the asymptotes of \(y = \dfrac{x^2 - 3x + 6}{x - 1}\), the coordinates of its stationary points, and sketch it.
**Division.** \(x^2 - 3x + 6 = (x - 1)(x - 2) + 4\), so
\[y = x - 2 + \frac{4}{x - 1}\]
The vertical asymptote is \(x = 1\). The oblique asymptote is \(y = x - 2\), because \(\dfrac{4}{x - 1} \to 0\).

**Sides.** The remainder term \(\dfrac{4}{x - 1}\) is positive for \(x > 1\) and negative for \(x < 1\). So the right branch is above the oblique line and the left branch below it. Near \(x = 1\): as \(x \to 1^+\), \(y \to +\infty\); as \(x \to 1^-\), \(y \to -\infty\).

**Stationary points.**
\[\frac{dy}{dx} = 1 - \frac{4}{(x - 1)^2}\]
Setting this to zero gives \((x - 1)^2 = 4\), so \(x = 3\) or \(x = -1\). Then \(y = 3\) when \(x = 3\), and \(y = -5\) when \(x = -1\). The points are \((3, 3)\) and \((-1, -5)\).

**Nature.** On the right branch the curve comes down from \(+\infty\) and goes up to follow \(y = x - 2\), so \((3, 3)\) is a minimum. On the left branch it rises from the asymptote, then falls to \(-\infty\): \((-1, -5)\) is a maximum.

**Axes.** \(x = 0\) gives \(y = -6\). The numerator \(x^2 - 3x + 6\) has discriminant \(9 - 24 < 0\), so there are no \(x\)-intercepts.
:::

:::plot The curve has a maximum at \((-1, -5)\) on its left branch and a minimum at \((3, 3)\) on its right branch. The dashed vertical line is \(x = 1\); the sloping line is the oblique asymptote \(y = x - 2\).
--f "(x**2-3*x+6)/(x-1)" --f "x-2" --label "y = (x² − 3x + 6)/(x − 1)" --label "y = x − 2" --x -7 9 --y -14 14 --vline 1 --xstep 4 --pt "3,3,minimum (3, 3)@se" --pt "-1,-5,maximum (−1, −5)@nw" --pt "0,-6,(0, −6)@e" --legend tl
:::

Slide \(k\) in the graph below. The curve is \(y = \dfrac{x^2 - 3x + k}{x - 1}\). The numerator at \(x = 1\) is \(k - 2\), so this is the value of the remainder \(R\). For \(k > 2\) the curve has two turning points; for \(k < 2\) it has none, because \(R\) is negative and each branch is monotonic; at \(k = 2\) the numerator is \((x - 1)(x - 2)\), the fraction cancels and you get the line \(y = x - 2\) with a hole at \(x = 1\).

:::html
<div class="widget" data-w="graph" data-fns="(x^2 - 3*x + k)/(x - 1)" data-x="-6,8" data-y="-12,12" data-params="k=6,-2,10,0.5" data-labels="y = (x² − 3x + k)/(x − 1)"></div>
:::

:::warn Missing the oblique asymptote
If the numerator has degree one more than the denominator and you write "horizontal asymptote \(y = 0\)" or "none", you lose the marks. Divide every time the degrees differ by exactly one, and give the equation \(y = mx + c\), not just "there is an oblique asymptote".
:::

## Turning points

There are two ways to find the turning points of a rational function. You should be able to use both, and each is a check on the other.

**By calculus.** Differentiate with the quotient rule, \(f'(x) = \dfrac{p'q - pq'}{q^2}\). The denominator \(q^2\) is never negative, so the sign of \(f'\) is the sign of the numerator \(p'q - pq'\). Solve \(p'q - pq' = 0\), then decide the nature of each point from the sign of \(f'\) on each side (or from the branch the point lies on, as above). If the function can be split as \(mx + c + \dfrac{R}{x - h}\), differentiate that instead: it is shorter.

**By the discriminant.** Next section.

## The set of values taken by the function

The **range** of a rational function is the set of values of \(y\) it takes. The graph shows it, but you can also find it algebraically, and the algebra gives the \(y\)-coordinates of the turning points without any differentiation.

The idea: \(y\) is a value taken by the function exactly when the equation \(y = f(x)\) has at least one real solution \(x\). Rewrite that equation as a quadratic in \(x\) and ask when it has real roots.

:::steps
1. Write \(y = \dfrac{p(x)}{q(x)}\) and multiply out: \(y\,q(x) = p(x)\).
2. Collect everything on one side to get a quadratic in \(x\), with coefficients that depend on \(y\).
3. For a real \(x\) to exist the discriminant must satisfy \(b^2 - 4ac \geq 0\). This is an inequality in \(y\): solve it.
4. Check separately any value of \(y\) that makes the coefficient of \(x^2\) zero: there the equation is not a quadratic and the discriminant does not apply.
:::

:::eg Find the set of values taken by \(y = \dfrac{x^2 - 3x + 6}{x - 1}\), and show that the result agrees with the turning points found above.
Multiply out and collect terms:
\[\begin{aligned}
y(x - 1) &= x^2 - 3x + 6 \\
x^2 - (3 + y)x + (6 + y) &= 0
\end{aligned}\]
For a real \(x\) the discriminant must be at least zero:
\[\begin{aligned}
(3 + y)^2 - 4(6 + y) &\geq 0 \\
y^2 + 2y - 15 &\geq 0 \\
(y + 5)(y - 3) &\geq 0
\end{aligned}\]
The parabola \(y^2 + 2y - 15\) opens upwards, so it is non-negative **outside** its roots: \(y \leq -5\) or \(y \geq 3\).

So the function takes no values strictly between \(-5\) and 3. These are the \(y\)-values of the turning points \((-1, -5)\) and \((3, 3)\): at those \(y\) the discriminant is exactly zero, a repeated root, which is where a horizontal line touches the curve without crossing it.
:::

:::eg Find the set of values taken by \(y = \dfrac{x^2 - 4}{x^2 - 1}\).
Multiply out: \(y(x^2 - 1) = x^2 - 4\), so
\[(y - 1)x^2 - (y - 4) = 0\]
This is a quadratic in \(x\) with \(a = y - 1\), \(b = 0\), \(c = -(y - 4)\). The discriminant is
\[0 - 4(y - 1)\bigl(-(y - 4)\bigr) = 4(y - 1)(y - 4)\]
For a real \(x\) we need \(4(y - 1)(y - 4) \geq 0\), so \(y \leq 1\) or \(y \geq 4\).

Now check \(y = 1\) separately, because it makes the coefficient of \(x^2\) zero. The equation becomes \(0 = -(1 - 4) = 3\), which is false. So \(y = 1\) is **not** taken.

The set of values is \(y < 1\) or \(y \geq 4\). This matches the sketch: the outer branches fill everything below 1 (never reaching it) and the middle "U" starts at its minimum 4.
:::

:::warn Two traps in the discriminant method
**Direction.** \(b^2 - 4ac \geq 0\) for an upward parabola in \(y\) gives "outside the roots" (\(y \leq \alpha\) or \(y \geq \beta\)), not "between". Sketch the parabola if you are unsure. **The special value.** If some \(y\) makes the \(x^2\) coefficient zero, test it by substitution; it may be taken or not taken, and the discriminant cannot tell you.
:::

### A real context

:::eg A workshop makes \(n\) wooden stools in a week. The weekly cost, in pounds, is \(0.02n^2 + 5n + 2000\), where \(2000\) is the fixed cost. (a) Show that the average cost per stool is \(A = 0.02n + 5 + \dfrac{2000}{n}\), and write down its oblique asymptote. (b) Find the number of stools that gives the least average cost, and that cost, to 3 significant figures.
(a) Divide the cost by \(n\):
\[A = \frac{0.02n^2 + 5n + 2000}{n} = 0.02n + 5 + \frac{2000}{n}\]
As \(n\) grows, \(\dfrac{2000}{n} \to 0\), so \(A\) approaches the line \(A = 0.02n + 5\). In words: for large output the fixed cost is spread so thinly that only the variable cost per stool is left.

(b) By calculus:
\[\frac{dA}{dn} = 0.02 - \frac{2000}{n^2} = 0 \quad\Rightarrow\quad n^2 = 100\,000\]
so \(n = \sqrt{100\,000} = 316.2\). A workshop makes whole stools, so it makes 316 of them, and the least value of the average cost is
\[A = 0.02\sqrt{100\,000} + 5 + \frac{2000}{\sqrt{100\,000}} = 17.65\]
(\(A(316) = 17.649\) is the same to 4 s.f.: the curve is very flat near its minimum.)
**Check with the discriminant.** \(An = 0.02n^2 + 5n + 2000\) gives \(0.02n^2 + (5 - A)n + 2000 = 0\). A real \(n\) needs \((A - 5)^2 - 4(0.02)(2000) \geq 0\), that is \((A - 5)^2 \geq 160\). As \(A > 5\) for \(n > 0\), \(A \geq 5 + \sqrt{160} = 17.65\). The two methods agree: the least average cost is about \(\pounds 17.65\) per stool.
:::

## Does the curve cross its asymptote?

To find where a curve meets its horizontal asymptote \(y = b\), solve \(f(x) = b\). If there is a solution, the curve crosses (or touches) the asymptote there. If the equation has no solution, the curve never meets it. For an oblique asymptote \(y = mx + c\), solve \(f(x) = mx + c\), which is the same as setting the remainder term to zero: \(\dfrac{r(x)}{q(x)} = 0\).

:::eg Show that the curve \(y = \dfrac{2x^2 - 3x}{x^2 - 1}\) crosses its horizontal asymptote, and find the coordinates of the crossing point. Describe its position relative to the asymptote far from the origin.
The leading coefficients are 2 and 1, so the horizontal asymptote is \(y = 2\). The vertical asymptotes are \(x = \pm 1\).

Set \(y = 2\):
\[\begin{aligned}
2x^2 - 3x &= 2(x^2 - 1) \\
-3x &= -2 \\
x &= \tfrac23
\end{aligned}\]
The curve meets \(y = 2\) at the single point \(\left(\tfrac23, 2\right)\), and crosses it there.

**Far from the origin.** \(y - 2 = \dfrac{2 - 3x}{x^2 - 1}\). For large positive \(x\) this is negative, so the curve is below the asymptote on the right. For large negative \(x\) it is positive, so the curve is above it on the left.

**Axes.** \(x = 0\) gives \(y = 0\), and \(y = 0\) gives \(x = 0\) or \(x = \tfrac32\). The numerator of \(\dfrac{dy}{dx}\) is \(3x^2 - 4x + 3\), with discriminant \(16 - 36 < 0\), so there are no turning points.
:::

:::plot The curve crosses its horizontal asymptote \(y = 2\) once, at \(\left(\tfrac23, 2\right)\). The dashed vertical lines are \(x = -1\) and \(x = 1\).
--f "(2*x**2-3*x)/(x**2-1)" --label "y = (2x² − 3x)/(x² − 1)" --x -6 7 --y -7 9 --vline -1 --vline 1 --hline 2 --xstep 4 --pt "0.6667,2,(2/3, 2)@ne" --pt "1.5,0,(3/2, 0)@se" --legend tr
:::

### Holes

If numerator and denominator share a factor, cancel it **before** looking for asymptotes. For example,
\[\frac{x^2 + x - 6}{x - 2} = \frac{(x + 3)(x - 2)}{x - 2} = x + 3 \quad (x \neq 2)\]
The graph is the straight line \(y = x + 3\) with a single point missing at \(x = 2\), where \(y\) would be 5. There is no asymptote at \(x = 2\). Mark the hole with an open circle and write its coordinates \((2, 5)\).

:::steps
1. **Factorise** the numerator and denominator and cancel any common factor (note any hole).
2. **Vertical asymptotes:** the zeros of the denominator. Sign-test each side.
3. **Horizontal or oblique asymptote:** compare degrees; divide if the degree of the numerator is one more.
4. **Intercepts:** \(x = 0\) for the \(y\)-intercept; numerator \(= 0\) for the \(x\)-intercepts.
5. **Turning points:** the numerator of \(f'(x)\) equal to zero, or the discriminant method. Check the nature from the sides of the asymptotes.
6. **Crossing the asymptote:** solve \(f(x) = b\) (or the remainder equal to 0).
7. **Draw:** dashed asymptotes first, then each branch, ending close to its asymptote. Label every intercept and turning point with its coordinates.
:::

## Putting it together

:::eg (Exam style) The curve \(C\) has equation \(y = f(x)\) where \(f(x) = \dfrac{(x - 2)^2}{x + 1}\), \(x \neq -1\). (a) Find the equations of the asymptotes of \(C\). (b) Find the coordinates of the stationary points of \(C\). (c) Sketch \(C\), showing the asymptotes and the coordinates of the intersections with the axes and of the stationary points. (d) Find, in exact form, the set of values of \(x\) for which \(f(x) \leq 2\).
**(a)** The denominator is zero at \(x = -1\) where the numerator is 9, so \(x = -1\) is an asymptote. [B1]

Divide the numerator \(x^2 - 4x + 4\) by \(x + 1\):
\[x^2 - 4x + 4 = (x + 1)(x - 5) + 9\] [M1]
\[f(x) = x - 5 + \frac{9}{x + 1}\]
So the oblique asymptote is \(y = x - 5\). [A1]

**(b)** Differentiate the divided form:
\[\frac{dy}{dx} = 1 - \frac{9}{(x + 1)^2}\] [M1]
Setting this to zero:
\[(x + 1)^2 = 9\] [M1]
\[x = 2 \quad\text{or}\quad x = -4\] [A1]
Then \(f(2) = 0\) and \(f(-4) = \dfrac{36}{-3} = -12\). The stationary points are \((2, 0)\) and \((-4, -12)\). [A1]

**(c)** The \(y\)-intercept is \((0, 4)\). The curve touches the \(x\)-axis at \((2, 0)\), because that is also a stationary point. The remainder \(\dfrac{9}{x + 1}\) is positive for \(x > -1\), so the right branch is above \(y = x - 5\), and negative for \(x < -1\), so the left branch is below it.

On the right branch the curve falls from \(+\infty\) at \(x = -1^+\), passes through \((0, 4)\), touches the axis at the minimum \((2, 0)\) and rises along \(y = x - 5\). On the left branch it rises from below the oblique line to the maximum \((-4, -12)\), then falls to \(-\infty\) at \(x = -1^-\).
- Both asymptotes drawn, with the branches on the correct sides of \(x = -1\). [B1]
- Intercepts \((0, 4)\) and \((2, 0)\) shown, the curve touching the axis at \((2, 0)\). [B1]
- Stationary points shown at \((2, 0)\) and \((-4, -12)\), with the curve approaching the oblique asymptote. [B1]

**(d)** Find where \(f(x) = 2\):
\[\begin{aligned}
(x - 2)^2 &= 2(x + 1) \\
x^2 - 6x + 2 &= 0
\end{aligned}\] [M1]
\[x = 3 \pm \sqrt{7}\] [A1]
The critical values are \(3 - \sqrt{7}\) (about 0.354), \(3 + \sqrt{7}\) (about 5.65) and the asymptote \(x = -1\). [B1]

From the sketch, the right branch is below \(y = 2\) between the two roots, and the whole left branch is below the \(x\)-axis, so below \(y = 2\). [M1]
\[x < -1 \quad\text{or}\quad 3 - \sqrt{7} \leq x \leq 3 + \sqrt{7}\] [A1]
**Check** with \(x = 1\): \(f(1) = \tfrac12 \leq 2\), in the range. With \(x = 6\): \(f(6) = \tfrac{16}{7} > 2\), out of the range.
:::

:::plot The curve \(y = \dfrac{(x - 2)^2}{x + 1}\) touches the \(x\)-axis at its minimum \((2, 0)\) and has a maximum at \((-4, -12)\). The vertical asymptote is \(x = -1\) and the oblique asymptote is \(y = x - 5\).
--f "(x-2)**2/(x+1)" --f "x-5" --label "y = (x − 2)²/(x + 1)" --label "y = x − 5" --x -9 9 --y -26 14 --vline -1 --xstep 5 --pt "2,0,minimum (2, 0)@se" --pt "-4,-12,maximum (−4, −12)@s" --pt "0,4,(0, 4)@ne" --legend tl
:::

:::board
UK Further Maths (AQA 7367) also lists sketching rational functions, including oblique asymptotes, as compulsory content, so the skills carry over. 9231 limits numerator and denominator to degree at most 2 and asks for the set of values taken; check your own specification for its limits.
:::

:::exam Sketching marks
Detailed plotting is not required: a sketch earns marks for **features**. Label the equation of every asymptote, the coordinates of every intercept and turning point, and make sure each branch approaches its asymptote on the correct side. A curve that crosses a vertical asymptote, or ends before it reaches the asymptote, loses the mark. Nothing in this chapter is on MF19: the quotient rule and the discriminant are for you to remember. Show the division that gives an oblique asymptote, because the line \(y = mx + c\) needs a method mark.
:::

:::eg Spot the error: find the set of values taken by \(g(x) = \dfrac{x^2 + 4}{x}\), \(x \neq 0\), for 4 marks.
A student wrote this answer.

Line 1: \(yx = x^2 + 4\), so \(x^2 - yx + 4 = 0\)
Line 2: for real \(x\), \(y^2 - 16 \geq 0\)
Line 3: \((y - 4)(y + 4) \geq 0\), so \(-4 \leq y \leq 4\)

Line 1 rearranges to a quadratic in \(x\). [M1] Line 2 uses the discriminant correctly. [M1] Line 3 finds the critical values \(y = \pm 4\) correctly. [A1]

**The set in line 3 has the wrong direction.** [A0] The parabola \((y - 4)(y + 4)\) opens upwards, so it is non-negative **outside** its roots. The student scores 3 out of 4.

Correct line 3: \(y \leq -4\) or \(y \geq 4\). [A1]

**Check:** \(g(2) = 4\) and \(g(-2) = -4\), and \(g(1) = 5\) is above 4. The value \(y = 0\) would need \(x^2 = -4\), which is impossible, so no value near 0 is taken.
:::

:::try Start easy, finish at exam standard
Q: Write down the vertical asymptote and the horizontal asymptote of \(y = \dfrac{3x - 2}{x + 4}\).
A: The denominator is zero at \(x = -4\), so \(x = -4\) is the vertical asymptote. The degrees are equal and the leading coefficients are 3 and 1, so \(y = 3\) is the horizontal asymptote.
Q: Find the intersections of \(y = \dfrac{x - 6}{x + 2}\) with the axes.
A: When \(x = 0\), \(y = -3\). When \(y = 0\), \(x = 6\). The points are \((0, -3)\) and \((6, 0)\).
Q: Find the asymptotes of \(y = \dfrac{x^2 + 3}{x + 1}\).
A: \(x^2 + 3 = (x + 1)(x - 1) + 4\), so \(y = x - 1 + \dfrac{4}{x + 1}\). The asymptotes are \(x = -1\) and \(y = x - 1\).
Q: Which side of the line \(y = x - 1\) is the curve \(y = \dfrac{x^2 + 3}{x + 1}\) on, for \(x > -1\) and for \(x < -1\)?
A: The remainder term is \(\dfrac{4}{x + 1}\). It is positive for \(x > -1\), so the curve is above the line there; it is negative for \(x < -1\), so the curve is below the line there.
Q: Use the sign of \(y\) in each interval to describe the behaviour of \(y = \dfrac{x}{(x - 2)(x + 3)}\) just either side of each vertical asymptote.
A: At \(x = -3^-\), \(x < 0\), \((x - 2) < 0\), \((x + 3) < 0\), so \(y\) is negative: \(y \to -\infty\). At \(x = -3^+\) the last factor is positive, so \(y \to +\infty\). At \(x = 2^-\): \(x > 0\), \(x - 2 < 0\), \(x + 3 > 0\), so \(y \to -\infty\). At \(x = 2^+\), \(y \to +\infty\).
Q: Find the set of values taken by \(y = \dfrac{x}{x^2 + 4}\).
A: \(yx^2 - x + 4y = 0\). For real \(x\): \(1 - 16y^2 \geq 0\), so \(-\tfrac14 \leq y \leq \tfrac14\). (At \(y = 0\) the equation is \(x = 0\), which is fine.)
Q: Find the coordinates of the stationary points of \(y = \dfrac{x^2}{x - 2}\).
A: \(\dfrac{dy}{dx} = \dfrac{2x(x - 2) - x^2}{(x - 2)^2} = \dfrac{x(x - 4)}{(x - 2)^2}\), which is zero at \(x = 0\) and \(x = 4\). The points are \((0, 0)\) and \((4, 8)\).
Q: Does the curve \(y = \dfrac{x^2 + 1}{x^2 - 4}\) cross its horizontal asymptote?
A: The asymptote is \(y = 1\). Setting \(x^2 + 1 = x^2 - 4\) gives \(1 = -4\), which is impossible. The curve never meets the asymptote.
Q: Simplify \(\dfrac{x^2 - 9}{x^2 - 3x}\) and describe the graph, including any hole.
A: \(\dfrac{(x - 3)(x + 3)}{x(x - 3)} = \dfrac{x + 3}{x}\) for \(x \neq 3\). There is a vertical asymptote at \(x = 0\) and the horizontal asymptote \(y = 1\), and a hole at \(x = 3\) where \(y = 2\).
Q: The curve \(y = \dfrac{x^2 + k}{x}\) has a minimum point at \(x = 3\), where \(k\) is a positive constant. Find \(k\).
A: \(y = x + \dfrac{k}{x}\), so \(\dfrac{dy}{dx} = 1 - \dfrac{k}{x^2}\). Put \(x = 3\): \(1 - \dfrac{k}{9} = 0\), so \(k = 9\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Find the equations of the asymptotes of \(y = \dfrac{3x - 1}{x + 2}\).
A: The denominator is zero at \(x = -2\). [B1] The degrees are equal, so divide the leading coefficients: [M1] \(y = 3\). [A1]
Q: [4 marks] ★ Find the set of values taken by \(f(x) = \dfrac{x}{x^2 + 9}\).
A: \(y(x^2 + 9) = x\), so \(yx^2 - x + 9y = 0\). [M1]
For real \(x\), \(1 - 36y^2 \geq 0\). [M1]
\(y^2 \leq \tfrac{1}{36}\) [A1], so \(-\tfrac16 \leq y \leq \tfrac16\). [A1]
Q: [5 marks] ★★ The curve \(y = \dfrac{2x^2 - 3x + 5}{x - 2}\) has an oblique asymptote. Find its equation, and state whether the curve is above or below it for \(x > 2\).
A: Divide: \(2x^2 - 3x + 5 = (x - 2)(2x + 1) + 7\). [M1]
So \(y = 2x + 1 + \dfrac{7}{x - 2}\) [A1], and the asymptotes are \(x = 2\) [B1] and \(y = 2x + 1\). [A1]
For \(x > 2\) the remainder \(\dfrac{7}{x - 2}\) is positive, so the curve is above the oblique asymptote. [B1]
Q: [5 marks] ★★ The curve \(y = \dfrac{3x^2 - 2x}{x^2 - 4}\) has three asymptotes. Find their equations, and find the coordinates of the point where the curve crosses its horizontal asymptote.
A: The vertical asymptotes are \(x = 2\) and \(x = -2\). [B1]
The degrees are equal and the leading coefficients are 3 and 1, so \(y = 3\). [M1 A1]
Set \(3x^2 - 2x = 3(x^2 - 4)\), so \(-2x = -12\) [M1]. The point is \((6, 3)\). [A1]
Q: [7 marks] ★★ The average cost, in pounds, of producing \(n\) items is \(C = \dfrac{n^2 + 40n + 400}{n}\) for \(n > 0\). (a) Show, using a discriminant, that \(C \geq 80\). (b) Find the value of \(n\) that gives \(C = 80\).
A: (a) \(Cn = n^2 + 40n + 400\), so \(n^2 + (40 - C)n + 400 = 0\). [M1]
For a real \(n\): \((40 - C)^2 - 1600 \geq 0\). [M1]
\((C - 40)^2 \geq 1600\) [A1], so \(C - 40 \geq 40\) or \(C - 40 \leq -40\). [M1]
For \(n > 0\) every term of \(C\) is positive and \(C > 40\), so \(C \geq 80\). [A1]
(b) At \(C = 80\) the quadratic has a repeated root \(n = -\dfrac{40 - C}{2}\) [M1] \(= 20\). [A1]
Q: [9 marks] (#math.p3.diff) ★★★ The curve \(C\) has equation \(y = \dfrac{x^2}{x - 2}\). (a) Use the quotient rule to find the coordinates of the stationary points of \(C\). (b) Show that there are no points on \(C\) with \(0 < y < 8\).
H: The numerator of \(\dfrac{dy}{dx}\) factorises as \(x(x - 4)\).
H: For (b), write \(y(x - 2) = x^2\) as a quadratic in \(x\).
H: A real \(x\) needs a non-negative discriminant; the inequality will be "outside the roots".
A: (a) \(\dfrac{dy}{dx} = \dfrac{2x(x - 2) - x^2}{(x - 2)^2}\) [M1 A1]
\(= \dfrac{x^2 - 4x}{(x - 2)^2}\), which is zero when \(x(x - 4) = 0\) [M1]
\(x = 0\) or \(x = 4\) [A1]. The points are \((0, 0)\) [A1] and \((4, 8)\). [A1]
(b) \(x^2 - yx + 2y = 0\), and for real \(x\): \(y^2 - 8y \geq 0\). [M1]
\(y(y - 8) \geq 0\), so \(y \leq 0\) or \(y \geq 8\). [M1]
So no point has \(0 < y < 8\). [A1]
Q: [12 marks] (#math.p1.quadratics) ★★★ The curve \(C\) has equation \(y = \dfrac{(x - 1)(x + 2)}{x - 2}\). (a) Find the equations of the asymptotes of \(C\). (b) Show that \(y\) takes no values between 1 and 9. (c) Find the coordinates of the stationary points. (d) Sketch \(C\), showing the asymptotes and the axis intersections.
H: Expand the numerator, \(x^2 + x - 2\), and divide by \(x - 2\): the remainder is the value of the numerator at \(x = 2\).
H: In (b), the discriminant of \(x^2 + (1 - y)x + (2y - 2) = 0\) is \((y - 1)(y - 9)\).
H: In (c), at \(y = 1\) and \(y = 9\) the quadratic has a repeated root \(x = \dfrac{y - 1}{2}\).
A: (a) \(x = 2\). [B1] \(x^2 + x - 2 = (x - 2)(x + 3) + 4\), so \(y = x + 3 + \dfrac{4}{x - 2}\) [M1], and the oblique asymptote is \(y = x + 3\). [A1]
(b) \(y(x - 2) = x^2 + x - 2\), so \(x^2 + (1 - y)x + (2y - 2) = 0\). [M1]
Discriminant \(= (1 - y)^2 - 4(2y - 2) = y^2 - 10y + 9\) [A1]
For real \(x\), \((y - 1)(y - 9) \geq 0\) [M1], so \(y \leq 1\) or \(y \geq 9\): no values between 1 and 9. [A1]
(c) The repeated root is \(x = \dfrac{y - 1}{2}\): \(y = 1\) gives \(x = 0\) and \(y = 9\) gives \(x = 4\). [M1] The points are \((0, 1)\) and \((4, 9)\). [A1]
(d) Asymptotes \(x = 2\) and \(y = x + 3\) drawn, with the curve above the oblique line for \(x > 2\) and below it for \(x < 2\). [B1]
Intercepts \((1, 0)\), \((-2, 0)\) and \((0, 1)\) shown. [B1]
Stationary points \((0, 1)\) (a maximum) and \((4, 9)\) (a minimum) shown. [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ The curve \(C_k\) has equation \(y = \dfrac{x^2 + k}{x - 1}\), where \(k\) is a constant. (a) Show that \(C_k\) has stationary points only if \(k > -1\). (b) For \(k = 3\), find the set of values taken by \(y\). (c) Show that when \(k < -1\) the curve takes every real value.
H: Use the quotient rule, or divide to get \(x + 1 + \dfrac{k + 1}{x - 1}\), and look at the numerator of \(\dfrac{dy}{dx}\).
H: The discriminant method gives a quadratic in \(y\): \(y^2 - 4y - 4k \geq 0\).
A: (a) \(y = x + 1 + \dfrac{k + 1}{x - 1}\), so \(\dfrac{dy}{dx} = 1 - \dfrac{k + 1}{(x - 1)^2}\). [M1]
This is zero when \((x - 1)^2 = k + 1\) [M1], which has a real solution only if \(k + 1 \geq 0\). If \(k = -1\) the fraction vanishes and the curve is a straight line with a hole, with no stationary point, so stationary points need \(k > -1\). [A1]
(b) \(y(x - 1) = x^2 + 3\), so \(x^2 - yx + y + 3 = 0\) and the discriminant is \(y^2 - 4y - 12 \geq 0\). [M1]
\((y - 6)(y + 2) \geq 0\), so \(y \leq -2\) or \(y \geq 6\). [A1]
(c) In general \(x^2 - yx + (y + k) = 0\) has discriminant \(y^2 - 4y - 4k\). [M1] As a quadratic in \(y\) this has discriminant \(16 + 16k < 0\) for \(k < -1\), and its leading coefficient is positive, so \(y^2 - 4y - 4k > 0\) for every \(y\): every real value is taken. [A1]
Q: [7 marks] ★★★ A thin lens of focal length 10 cm gives an image at distance \(v\) from the lens of an object at distance \(u\), where \(u > 10\) and \(\dfrac1u + \dfrac1v = \dfrac1{10}\). (a) Show that \(v = \dfrac{10u}{u - 10}\), and that the distance \(D = u + v\) between the object and its image is \(D = \dfrac{u^2}{u - 10}\). (b) Show that \(D \geq 40\), and find the value of \(u\) for which \(D = 40\).
H: Make \(v\) the subject, then put \(u + v\) over a common denominator.
H: Write \(D(u - 10) = u^2\) as a quadratic in \(u\) and use the discriminant.
A: (a) \(\dfrac1v = \dfrac1{10} - \dfrac1u = \dfrac{u - 10}{10u}\), so \(v = \dfrac{10u}{u - 10}\). [M1 A1]
\(D = u + \dfrac{10u}{u - 10} = \dfrac{u(u - 10) + 10u}{u - 10} = \dfrac{u^2}{u - 10}\). [A1]
(b) \(u^2 - Du + 10D = 0\); for real \(u\), \(D^2 - 40D \geq 0\). [M1]
So \(D \leq 0\) or \(D \geq 40\). For \(u > 10\), \(D > 0\), so \(D \geq 40\). [A1]
At \(D = 40\) the repeated root is \(u = \dfrac{D}{2}\) [M1] \(= 20\), so \(u = 20\) cm (image also 20 cm away). [A1]
:::

:::quiz
? What is the horizontal asymptote of \(y = \dfrac{3x^2 + 1}{x^2 - 4}\)?
- \(y = 0\)
+ \(y = 3\)
- \(y = \dfrac14\)
- It has none
> The degrees are equal, so the horizontal asymptote is the ratio of the leading coefficients, \(y = 3\). The answer \(y = 0\) is for a numerator of lower degree, and \(x = \pm 2\) are the vertical asymptotes.
? What is the oblique asymptote of \(y = \dfrac{x^2 + 1}{x - 2}\)?
- \(y = x\)
- \(y = x - 2\)
+ \(y = x + 2\)
- \(y = x + 5\)
> \(x^2 + 1 = (x - 2)(x + 2) + 5\), so \(y = x + 2 + \dfrac{5}{x - 2}\). The asymptote is the quotient only: the 5 belongs to the remainder, which tends to 0.
? The discriminant method for the range of \(y = f(x)\) gives \((y - 2)(y + 3) \geq 0\). What are the values taken (assuming no special values)?
- \(-3 \leq y \leq 2\)
+ \(y \leq -3\) or \(y \geq 2\)
- \(y \leq 2\) or \(y \geq -3\), which is every value
- \(y \geq 2\) only
> A product of two brackets is non-negative when both are non-negative or both non-positive: outside the roots, \(y \leq -3\) or \(y \geq 2\). The "between" answer comes from reading the inequality the wrong way round.
? Which statement about the curve \(y = \dfrac{(x - 1)(x + 2)}{(x - 1)(x - 3)}\) is correct?
- It has vertical asymptotes \(x = 1\) and \(x = 3\)
+ It has a vertical asymptote \(x = 3\) and a hole at \(x = 1\)
- It has a vertical asymptote \(x = 1\) and a hole at \(x = 3\)
- It has no asymptotes
> The factor \(x - 1\) cancels, leaving \(\dfrac{x + 2}{x - 3}\). So \(x = 1\) is a hole (where \(y = -\tfrac32\)) and \(x = 3\) is the only vertical asymptote.
? A rational function has the horizontal asymptote \(y = 1\). Which statement is always true?
- The curve never meets \(y = 1\)
- The curve meets \(y = 1\) exactly once
+ The curve may or may not meet \(y = 1\): solve \(f(x) = 1\) to find out
- The curve crosses \(y = 1\) at every turning point
> An asymptote describes the behaviour for large \(|x|\) only. Some curves cross it once, some never, and the only reliable test is to solve \(f(x) = 1\).
? Why is the sign test needed at a vertical asymptote?
- Because the curve always goes to \(+\infty\) on the right
+ Because the two sides can go to \(+\infty\) or \(-\infty\), and the sketch must show which
- Because the curve crosses the asymptote
- Because it gives the turning points
> The direction depends on the signs of the numerator and denominator on each side. Two sides may go the same way (for example an even power in the denominator) or opposite ways.
:::

:::checklist What you can now do
- [ ] I can find the vertical asymptotes of a rational function and use a sign test to say which way the curve goes on each side.
- [ ] I can find horizontal asymptotes by comparing degrees, and say which side of them the curve lies.
- [ ] I can find an oblique asymptote by division, and say which side of it each branch lies.
- [ ] I can find the intercepts and the turning points of a rational function, by the quotient rule or by splitting into a quotient and a remainder.
- [ ] I can find the set of values taken by a rational function using a discriminant, check any special value, and link it to the turning points.
- [ ] I can decide whether a curve crosses its horizontal or oblique asymptote and find where.
- [ ] I can cancel a common factor and mark the hole.
- [ ] I can sketch a rational function showing asymptotes, axis intersections and turning points, and use the sketch to solve an inequality in exact form.
:::

:::recap
- Vertical asymptotes: zeros of the denominator (after cancelling common factors); sign-test each side.
- Compare degrees: numerator lower gives \(y = 0\); equal gives the ratio of leading coefficients; one higher gives an oblique asymptote \(y = mx + c\) by division.
- The remainder term \(\dfrac{R}{x - h}\) tells you which side of the oblique (or horizontal) asymptote the curve is on.
- Turning points: numerator of \(f'(x)\) equals zero, or the repeated root of the discriminant equation.
- Range: write \(y\,q(x) = p(x)\) as a quadratic in \(x\), require the discriminant \(\geq 0\) (inequality in \(y\)), and check any \(y\) that makes the \(x^2\) coefficient zero.
- A curve can cross a horizontal or oblique asymptote: solve \(f(x) = b\) or remainder \(= 0\). It can never cross a vertical asymptote.
- A cancelled factor leaves a hole, not an asymptote.
- A sketch shows: asymptotes with their equations, intercepts and turning points with coordinates, each branch on the correct side.
:::

:::links
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · tutorials on every Further Pure topic, including sketching rational functions
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · graded questions with answers on rational functions and their graphs
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · type in a rational function and slide a constant to see asymptotes and turning points move
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Graphs related to y = f(x)](#math.fm.graphs) shows how the graphs of \(|f(x)|\), \(f(|x|)\), \(\dfrac{1}{f(x)}\) and \(y^2 = f(x)\) grow out of the graph of \(y = f(x)\).
