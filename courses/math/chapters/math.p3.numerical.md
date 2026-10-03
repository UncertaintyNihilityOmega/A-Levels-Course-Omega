@chapter math.p3.numerical
@title Numerical solution of equations
@level as
@paper CAIE P2/P3 · Edexcel IAL P3 · AQA/OCR/Edexcel Pure Year 2
@time 5–7 hours
@summary Locating a root by a sign change or by a graph, showing a root to a given accuracy, and finding roots with an iterative formula \(x_{n+1} = \mathrm{F}(x_n)\), including how to build the formula from the equation and when an iteration fails.

:::why
Most equations that come from real problems have no neat algebraic solution. \(e^x + 2x = 10\), \(x = 2\cos x\) and \(x^3 = 2x + 5\) cannot be solved by rearranging. Numerical methods give the answer as accurately as you like, which is how calculators, spreadsheets and engineering software solve them. This chapter teaches the two standard methods: spotting that a root lies between two numbers, and improving a guess again and again.
:::

**Before you start**, you need graph sketching ([Graphs and straight lines](#math.f.graphs)), logarithms and exponentials ([Logarithms and exponentials](#math.p3.logs)), and a calculator with an **ANS** (answer) key. Work in radians for anything with \(\sin\), \(\cos\) or \(\tan\).

## Locating a root

:::def Root of an equation
A root (or solution) of \(\mathrm{f}(x) = 0\) is a value \(\alpha\) such that \(\mathrm{f}(\alpha) = 0\). Graphically it is where the curve \(y = \mathrm{f}(x)\) crosses the \(x\)-axis.
:::

If the graph of a continuous function goes from below the \(x\)-axis to above it, it must cross the axis somewhere in between. That is the idea of the sign change test.

:::key Sign change rule
If \(\mathrm{f}(x)\) is **continuous** on the interval \([a, b]\) and \(\mathrm{f}(a)\) and \(\mathrm{f}(b)\) have **opposite signs**, then \(\mathrm{f}(x) = 0\) has at least one root between \(a\) and \(b\).
To use it in an exam: (1) write the equation as \(\mathrm{f}(x) = 0\), (2) calculate \(\mathrm{f}(a)\) and \(\mathrm{f}(b)\) and quote their values, (3) state "there is a change of sign, and \(\mathrm{f}\) is continuous, so there is a root in the interval."
:::

:::eg Show that \(x^3 + x - 5 = 0\) has a root between \(1\) and \(2\), and that \(e^x + x - 4 = 0\) has a root between \(1\) and \(1.5\).
Let \(\mathrm{f}(x) = x^3 + x - 5\). Then \(\mathrm{f}(1) = 1 + 1 - 5 = -3 < 0\) and \(\mathrm{f}(2) = 8 + 2 - 5 = 5 > 0\). There is a sign change and \(\mathrm{f}\) is continuous, so a root lies between \(1\) and \(2\).

Let \(\mathrm{g}(x) = e^x + x - 4\). Then \(\mathrm{g}(1) = e - 3 = -0.282 < 0\) and \(\mathrm{g}(1.5) = e^{1.5} - 2.5 = 1.98 > 0\). So a root lies in \([1, 1.5]\).
:::

### When the sign change test fails

A sign change always means a root **if the function is continuous**. But the test can mislead you in three ways.

:::warn Three traps
- **A discontinuity.** \(\mathrm{f}(x) = \dfrac1x\) has \(\mathrm{f}(-1) = -1\) and \(\mathrm{f}(1) = 1\), a sign change, but there is no root: the graph jumps across the asymptote at \(x = 0\).
- **No sign change but a root.** \(\mathrm{f}(x) = (x - 1)^2\) touches the axis at \(x = 1\) without crossing it. \(\mathrm{f}(0) = 1\) and \(\mathrm{f}(2) = 1\) have the same sign, yet \(x = 1\) is a root.
- **Two roots in the interval.** If the curve crosses the axis twice between \(a\) and \(b\), the signs at the ends are the same and you miss both roots. For example, \(\mathrm{f}(x) = x^2 - 4\) has \(\mathrm{f}(-3) = 5\) and \(\mathrm{f}(3) = 5\), yet there are roots at \(\pm 2\).
Use a narrow interval and a sketch to avoid these.
:::

### Locating roots with a graph

Sometimes it is easier to split an equation into two simpler graphs and find where they meet. For \(\ln x + x = 3\), rearrange to \(\ln x = 3 - x\) and sketch \(y = \ln x\) and \(y = 3 - x\). The \(x\)-coordinate of each intersection is a root.

:::plot The graphs of \(y = \ln x\) and \(y = 3 - x\) meet once, near x = 2.2, so \(\ln x + x - 3 = 0\) has exactly one root.
--f "log(x)" --f "3-x" --label "y = ln x" --label "y = 3 − x" --x 0.2 4 --y -2 3 --pt "2.2079,0.7921,root near 2.2@ne" --legend tr
:::

The sketch shows there is exactly one root (the curve rises, the line falls). To find where it is, test values: let \(\mathrm{f}(x) = \ln x + x - 3\). Then \(\mathrm{f}(2) = 0.693 + 2 - 3 = -0.307 < 0\) and \(\mathrm{f}(3) = 1.099 > 0\), so the root is between \(2\) and \(3\).

## Showing a root to a given accuracy

To show that \(\alpha = 2.21\) to 2 decimal places, find the interval of numbers that round to 2.21: from \(2.205\) to \(2.215\). If \(\mathrm{f}(2.205)\) and \(\mathrm{f}(2.215)\) have opposite signs, the root lies in that interval and so rounds to 2.21.

:::eg Show that the root of \(\ln x + x - 3 = 0\) is \(2.21\) correct to 2 decimal places.
Let \(\mathrm{f}(x) = \ln x + x - 3\). The bounds are \(2.205\) and \(2.215\).
\[\mathrm{f}(2.205) = 0.7907 + 2.205 - 3 = -0.0043 < 0 \qquad \mathrm{f}(2.215) = 0.7953 + 2.215 - 3 = 0.0103 > 0\]
There is a change of sign in \([2.205, 2.215]\) and \(\mathrm{f}\) is continuous, so the root is \(2.21\) to 2 d.p.
:::

:::exam The interval for "correct to \(n\) decimal places"
For a root \(\alpha = 2.21\) to 2 d.p., use \([2.205, 2.215]\): the endpoints are half a unit in the last place either side. For 3 d.p. use \(\pm 0.0005\); for 1 d.p. use \(\pm 0.05\). Quote the values of \(\mathrm{f}\) at both ends, to at least 2 significant figures, and state the sign change.
:::

## Iteration

Rather than searching blindly, we can improve a guess automatically. The idea is to rearrange \(\mathrm{f}(x) = 0\) into the form \(x = \mathrm{F}(x)\), then use

:::key Iterative formula
\[x_{n+1} = \mathrm{F}(x_n)\]
Start with a first estimate \(x_0\) (or \(x_1\)), compute \(x_1 = \mathrm{F}(x_0)\), then \(x_2 = \mathrm{F}(x_1)\), and so on. If the sequence \(x_0, x_1, x_2, \ldots\) **converges** to a number \(\alpha\), then \(\alpha = \mathrm{F}(\alpha)\), so \(\alpha\) is a root of the original equation.
:::

Why does the limit satisfy the equation? If \(x_n\) gets closer and closer to \(\alpha\), then \(x_{n+1}\) is also close to \(\alpha\), and \(x_{n+1} = \mathrm{F}(x_n)\) turns into \(\alpha = \mathrm{F}(\alpha)\).

:::tip Using the ANS key
Type the starting value and press \(=\). Then type the formula using **ANS** in place of \(x_n\), for example \((2\,\mathrm{ANS} + 5)^{\wedge}(1 \div 3)\), and press \(=\) repeatedly. Each press computes the next term. Write down each term to at least 6 decimal places, or to one more place than you need.
:::

:::eg The equation \(x^3 - 2x - 5 = 0\) has a root \(\alpha\) between \(2\) and \(3\). (a) Show that the equation can be rearranged as \(x = \sqrt[3]{2x + 5}\). (b) Use \(x_{n+1} = \sqrt[3]{2x_n + 5}\) with \(x_0 = 2\) to find \(\alpha\) to 3 decimal places.
(a) \(x^3 = 2x + 5\), so \(x = \sqrt[3]{2x + 5}\).

(b) 
| \(n\) | \(x_n\) |
|---|---|
| 0 | 2 |
| 1 | 2.080084 |
| 2 | 2.092351 |
| 3 | 2.094217 |
| 4 | 2.094501 |
| 5 | 2.094544 |

The values settle at \(2.0945\ldots\), so \(\alpha = 2.095\) to 3 d.p. (Two successive terms must agree to the accuracy asked for before you stop.)
:::

The widget below plots \(y = x\) and \(y = \mathrm{F}(x)\). The staircase starts at \(x_0\), goes up to the curve, across to the line \(y = x\), and so on. It homes in on the intersection, which is the root.

:::html
<div class="widget" data-w="iteration" data-f="(2x+5)^(1/3)" data-x0="2" data-range="1.8,2.4" data-n="8"></div>
:::

Try moving \(x_0\) to the ends of the range: the iteration still reaches the same root. Increase the number of steps to see more decimal places settle.

### Choosing the rearrangement

An equation can be rearranged to \(x = \mathrm{F}(x)\) in many ways, and not all converge. For \(x^3 - 2x - 5 = 0\) another rearrangement is \(x = \dfrac{x^3 - 5}{2}\).

:::eg Try the iteration \(x_{n+1} = \dfrac{x_n^3 - 5}{2}\) with \(x_0 = 2\).
\(x_1 = \dfrac{8 - 5}{2} = 1.5\), \(x_2 = \dfrac{3.375 - 5}{2} = -0.8125\), \(x_3 = \dfrac{-0.536 - 5}{2} = -2.768\), \(x_4 = \dfrac{-21.2 - 5}{2} = -13.1\), \(x_5 \approx -1128\). The terms run away from the root: the iteration **diverges**, even though \(\alpha = \mathrm{F}(\alpha)\) is still true for the exact root.
:::

Here is the same start for this rearrangement. The staircase moves away from the point where the curve meets the line \(y = x\), instead of closing in on it.

:::html
<div class="widget" data-w="iteration" data-f="(x^3-5)/2" data-x0="2" data-range="-3,3" data-n="5"></div>
:::

An iteration may **converge** (the staircase or the cobweb closes in on the root), **diverge** (moves away) or **oscillate** (jump either side of the root). The syllabus does not ask you to prove when it converges, but you should recognise that it can fail. If a question asks you to comment, say "the values are not approaching a limit". If an iteration diverges, rearrange the equation another way.

:::eg The equation \(e^x + 2x - 10 = 0\) has a root near \(1.8\). Show that it can be written \(x = \ln(10 - 2x)\) and use \(x_0 = 1.8\) to find the root to 2 decimal places.
\(e^x = 10 - 2x\), so taking natural logs gives \(x = \ln(10 - 2x)\).

\(x_1 = \ln(6.4) = 1.8563\), \(x_2 = \ln(6.2874) = 1.8385\), \(x_3 = \ln(6.3230) = 1.8442\), \(x_4 = 1.8424\), \(x_5 = 1.8430\), \(x_6 = 1.8428\). The terms alternate above and below the root and close in on it. The root is \(1.84\) to 2 d.p.
:::

### Finding the equation from an iteration

A common question gives the iteration and asks which equation it solves. Replace \(x_n\) and \(x_{n+1}\) by \(\alpha\) and rearrange.

:::eg The iteration \(x_{n+1} = \sqrt{3 + x_n}\) converges to \(\alpha\). Find the equation that \(\alpha\) satisfies, and show that \(\alpha = 2.30\) to 2 decimal places.
\(\alpha = \sqrt{3 + \alpha}\), so \(\alpha^2 = 3 + \alpha\), that is \(\alpha^2 - \alpha - 3 = 0\). The positive solution is \(\alpha = \dfrac{1 + \sqrt{13}}{2} = 2.303\), so \(\alpha = 2.30\) to 2 d.p.
:::

## A real problem and an exam question

:::eg A spherical tank of radius \(1\) m is filled with water to depth \(h\) m. The volume of water is \(V = \dfrac{\pi h^2(3 - h)}{3}\) cubic metres. Find the depth when \(V = 2\).
\(\dfrac{\pi h^2(3 - h)}{3} = 2\) gives \(h^2(3 - h) = \dfrac{6}{\pi}\), so \(h^3 - 3h^2 + \dfrac6\pi = 0\) with \(\dfrac6\pi = 1.9099\). Let \(\mathrm{f}(h) = h^3 - 3h^2 + 1.9099\). Then \(\mathrm{f}(0.9) = 0.209 > 0\) and \(\mathrm{f}(1) = -0.090 < 0\), so the depth is between \(0.9\) m and \(1\) m.

Rearrange \(3h^2 = h^3 + 1.9099\) as \(h_{n+1} = \sqrt{\dfrac{h_n^3 + 1.9099}{3}}\). Starting at \(h_0 = 0.9\): \(0.9379, 0.9548, 0.9627, 0.9664, 0.9683, 0.9691, 0.9695, \ldots\), approaching \(0.970\). Check the sign change: \(\mathrm{f}(0.965) = 0.0148 > 0\) and \(\mathrm{f}(0.975) = -0.0152 < 0\), so \(h = 0.97\) m to 2 d.p.
:::

:::eg (Exam style) The equation \(x^3 - x - 3 = 0\) has one real root \(\alpha\). (a) Show that \(\alpha\) lies between \(1\) and \(2\). (b) Show that \(\alpha\) is a root of \(x = \sqrt[3]{x + 3}\). (c) Use \(x_{n+1} = \sqrt[3]{x_n + 3}\) with \(x_0 = 1.5\) to find \(\alpha\) correct to 3 decimal places, showing your values. (d) Show that your value is correct to 3 decimal places by considering a sign change.
**(a)** Let \(\mathrm{f}(x) = x^3 - x - 3\). \(\mathrm{f}(1) = -3 < 0\) and \(\mathrm{f}(2) = 3 > 0\). [M1] The change of sign, with \(\mathrm{f}\) continuous, shows a root in \([1, 2]\). [A1]

**(b)** \(x^3 = x + 3\), so \(x = \sqrt[3]{x + 3}\). [B1]

**(c)** \(x_1 = \sqrt[3]{4.5} = 1.6510\), \(x_2 = 1.6692\), \(x_3 = 1.6714\), \(x_4 = 1.6717\), \(x_5 = 1.6717\). [M1 A1] So \(\alpha = 1.672\) to 3 d.p. [A1]

**(d)** The bounds are \(1.6715\) and \(1.6725\). \(\mathrm{f}(1.6715) = -0.0015 < 0\) and \(\mathrm{f}(1.6725) = 0.0059 > 0\). [M1 A1] There is a change of sign, so \(\alpha\) lies in this interval and \(\alpha = 1.672\) to 3 d.p. ∎ [A1]
:::

:::board Other boards
Edexcel IAL covers locating roots, iteration and the sign change test in P3. UK A Levels (AQA, Edexcel, OCR) include the same in Pure Year 2, and also cover Newton-Raphson, which is not on the Cambridge 9709 syllabus. Cambridge asks how an iteration relates to the equation, and that it may fail to converge, but not the condition for convergence.
:::

:::try Start easy, finish at exam standard
Q: Show that \(x^3 - 4x + 1 = 0\) has a root between \(1\) and \(2\).
A: Let \(\mathrm{f}(x) = x^3 - 4x + 1\). \(\mathrm{f}(1) = 1 - 4 + 1 = -2 < 0\) and \(\mathrm{f}(2) = 8 - 8 + 1 = 1 > 0\). The sign changes and \(\mathrm{f}\) is continuous, so there is a root in \([1, 2]\).
Q: Explain why the sign change test cannot be used on \(\mathrm{f}(x) = \dfrac{1}{x - 2}\) over \([1, 3]\).
A: \(\mathrm{f}(1) = -1\) and \(\mathrm{f}(3) = 1\) have opposite signs, but \(\mathrm{f}\) is not continuous at \(x = 2\) (it has an asymptote) and \(\mathrm{f}(x) = 0\) has no solution. The test needs a continuous function.
Q: By sketching \(y = e^{-x}\) and \(y = x\) (or otherwise), show that the equation \(e^{-x} = x\) has exactly one root, and show it lies between \(0.5\) and \(0.6\).
A: \(y = e^{-x}\) is decreasing and positive; \(y = x\) is increasing, so they meet once. Let \(\mathrm{f}(x) = e^{-x} - x\). \(\mathrm{f}(0.5) = 0.6065 - 0.5 = 0.1065 > 0\) and \(\mathrm{f}(0.6) = 0.5488 - 0.6 = -0.0512 < 0\). A sign change gives a root in \([0.5, 0.6]\).
Q: Show that the root of \(x^3 + x - 5 = 0\) lies in \([1.5, 1.6]\) and use \(x_{n+1} = \sqrt[3]{5 - x_n}\) with \(x_0 = 1.5\) to find it to 2 decimal places.
A: \(\mathrm{f}(1.5) = 3.375 + 1.5 - 5 = -0.125 < 0\) and \(\mathrm{f}(1.6) = 4.096 + 1.6 - 5 = 0.696 > 0\). The iteration gives \(x_1 = \sqrt[3]{3.5} = 1.5183\), \(x_2 = \sqrt[3]{3.4817} = 1.5155\), \(x_3 = 1.5159\), \(x_4 = 1.5158\). The root is \(1.52\) to 2 d.p.
Q: The iteration \(x_{n+1} = \dfrac{4}{x_n^2 + 1}\) converges to \(\alpha\). Find the cubic equation satisfied by \(\alpha\).
A: \(\alpha = \dfrac{4}{\alpha^2 + 1}\), so \(\alpha(\alpha^2 + 1) = 4\), giving \(\alpha^3 + \alpha - 4 = 0\).
Q: Show that \(2\ln x + x = 6\) can be written \(x = 6 - 2\ln x\). Use this with \(x_0 = 3\) to find the first six values, say what you notice, and show by a sign change that the root is \(3.50\) to 2 decimal places.
A: \(2\ln x = 6 - x\) gives \(x = 6 - 2\ln x\). The values are \(3.8028, 3.3285, 3.5949, 3.4410, 3.5285, 3.4783\). They alternate above and below the root and close in on it slowly, so a sign change check is better for the final accuracy. Let \(\mathrm{f}(x) = 2\ln x + x - 6\): \(\mathrm{f}(3.495) = -0.0023 < 0\) and \(\mathrm{f}(3.505) = 0.0134 > 0\). The root is in \([3.495, 3.505]\), so \(3.50\) to 2 d.p.
Q: A student uses \(x_{n+1} = \dfrac{x_n^3 - 5}{2}\) with \(x_0 = 2\) for \(x^3 - 2x - 5 = 0\). Describe what happens and suggest what to do.
A: The values are \(1.5, -0.8125, -2.768, -13.1, \ldots\), growing without limit: the iteration diverges. Rearrange the equation differently, for example \(x = \sqrt[3]{2x + 5}\).
Q: (Exam style) The equation \(2\cos x = x\) (with \(x\) in radians) has one root \(\alpha\). (a) Show that \(\alpha\) lies between \(1\) and \(1.5\). (b) Show that the equation can be written \(x = \cos^{-1}\left(\dfrac x2\right)\). (c) Use \(x_{n+1} = \cos^{-1}\left(\dfrac{x_n}{2}\right)\) with \(x_0 = 1\) to find \(\alpha\) to 2 decimal places. (d) Show by a sign change that your answer is correct. (e) A student uses \(x_{n+1} = 2\cos x_n\) with \(x_0 = 1\). What happens?
A: (a) \(\mathrm{f}(x) = 2\cos x - x\): \(\mathrm{f}(1) = 0.081 > 0\) and \(\mathrm{f}(1.5) = -1.359 < 0\). [M1 A1] (b) \(\cos x = \dfrac x2\), so \(x = \cos^{-1}\dfrac x2\). [B1] (c) \(x_1 = 1.0472\), \(x_2 = 1.0197\), \(x_3 = 1.0358\), \(x_4 = 1.0264\), \(x_5 = 1.0319\), \(x_6 = 1.0287\), \(x_7 = 1.0306\). [M1 A1] The values settle near \(1.03\), so \(\alpha = 1.03\). [A1] (d) \(\mathrm{f}(1.025) = 0.0132 > 0\) and \(\mathrm{f}(1.035) = -0.0139 < 0\), so the root is in \([1.025, 1.035]\). [M1 A1] (e) The values are \(1.0806, 0.9416, 1.1770, 0.7674, 1.4395, 0.2619, \ldots\) and jump about with growing size: the iteration does not converge. [B1]
:::

:::quiz
? \(\mathrm{f}(x) = x^3 - 6x + 2\) has \(\mathrm{f}(0) = 2\) and \(\mathrm{f}(1) = -3\). What can you conclude?
- There is no root between \(0\) and \(1\).
+ There is a root between \(0\) and \(1\), because the signs differ and \(\mathrm{f}\) is continuous.
- There are exactly two roots between \(0\) and \(1\).
- The root is exactly \(0.5\).
> A sign change on a continuous function means at least one root in the interval. It does not say there is exactly one, and it does not locate the root precisely.
? Which function could fool the sign change test on \([-1, 1]\)?
+ \(\mathrm{f}(x) = \dfrac1x\)
- \(\mathrm{f}(x) = x^3\)
- \(\mathrm{f}(x) = x\)
- \(\mathrm{f}(x) = e^x - 1\)
> \(\dfrac1x\) changes sign between \(-1\) and \(1\) but is discontinuous at \(0\) and has no root. The other three functions are continuous and genuinely cross the axis at \(0\).
? To show that a root is \(1.34\) to 2 decimal places, you test the signs of \(\mathrm{f}\) at
- \(1.3\) and \(1.4\)
- \(1.34\) and \(1.35\)
+ \(1.335\) and \(1.345\)
- \(1.339\) and \(1.341\)
> Numbers that round to \(1.34\) lie in \([1.335, 1.345]\). Testing \(1.3\) and \(1.4\) is too wide, and \(1.34\) and \(1.35\) is not centred on the value.
? The iteration \(x_{n+1} = \sqrt{x_n + 6}\) converges to \(\alpha\). Which equation does \(\alpha\) satisfy?
- \(\alpha^2 = \alpha - 6\)
+ \(\alpha^2 - \alpha - 6 = 0\)
- \(\alpha = \sqrt{\alpha} + 6\)
- \(\alpha^2 + \alpha - 6 = 0\)
> Put \(x_n = x_{n+1} = \alpha\): \(\alpha = \sqrt{\alpha + 6}\), so \(\alpha^2 = \alpha + 6\) and \(\alpha^2 - \alpha - 6 = 0\) (root \(3\)). Watch the sign when you move \(\alpha\) across.
? The sequence \(1.5, -0.8, -2.8, -13.1, \ldots\) is produced by an iteration. What does this show?
- The iteration has converged.
- The root is negative.
+ The iteration diverges, so a different rearrangement is needed.
- The equation has no root.
> Terms that grow without limit mean the iteration is moving away from a root. The root may exist; this rearrangement simply fails to find it.
:::

:::recap
- Sign change rule: if \(\mathrm{f}\) is continuous and \(\mathrm{f}(a)\), \(\mathrm{f}(b)\) have opposite signs, there is a root in \([a, b]\). It can fail at a discontinuity, at a double root or with two roots in the interval.
- To show a root to \(n\) d.p., find a sign change over \(\pm\tfrac12\) of the last decimal place (e.g. \(1.335\) to \(1.345\) for 1.34).
- Rearrange \(\mathrm{f}(x) = 0\) as \(x = \mathrm{F}(x)\) and iterate \(x_{n+1} = \mathrm{F}(x_n)\). A limit \(\alpha\) satisfies \(\alpha = \mathrm{F}(\alpha)\). Use the ANS key and keep extra decimals.
- Iterations can converge steadily, converge by oscillating, or diverge. If one diverges, try another rearrangement.
- To find the equation from an iteration, set \(x_n = x_{n+1} = \alpha\) and rearrange.
:::

:::note Learn more online
- **Watch:** [Solving equations by iteration](https://www.examsolutions.net/tutorials/solutions-of-equations-by-iteration/) · ExamSolutions · xₙ₊₁ = F(xₙ) step by step
- **Watch:** [Exam questions: iteration](https://www.examsolutions.net/tutorials/exam-questions-iteration/) · ExamSolutions · sign change, iteration and accuracy
- **Practise:** [CAIE Pure 3 numerical methods exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/numerical-methods/numerical-solutions-of-equations/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot y = x and y = F(x) and follow the staircase
- **Papers:** [9709 Paper 3 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-3/) · Physics & Maths Tutor · papers with mark schemes *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Partial fractions and the binomial series](#math.p3.partial).
