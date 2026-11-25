@chapter math.fm.crv
@title Continuous random variables
@level fm
@paper CAIE 9231 Paper 4
@time 5–6 hours
@summary A continuous random variable is described by its probability density function (PDF) or its cumulative distribution function (CDF). You will work with PDFs that change form from one interval to the next, move between the PDF and the CDF, find medians, quartiles and percentiles, find \(E(g(X))\) for any function \(g\), and use the CDF to find the distribution of a related variable such as \(Y = X^3\).

:::why
Real measurements such as waiting times, lifetimes and masses rarely follow one neat formula on one interval: a component may be most likely to fail early, then rarely, then never after a fixed date. A piecewise PDF models this, and the CDF turns "how likely is a value below \(x\)?" into a single formula. The same CDF method also gives the distribution of a new quantity built from the old one (the cost of a repair, the square of a speed), which is how new distributions are found throughout statistics.
:::

**Before you start**, you need the idea of a PDF, probability as area, the mean and the median from [Continuous random variables](#math.s2.crv), and integration of powers from [Integration](#math.p1.integ). The normal distribution from [The normal distribution](#math.s1.normal) appears only as a comparison.

:::try Warm-up
Q: A random variable has PDF \(f(x) = kx\) for \(0 \le x \le 3\) and 0 otherwise. Find \(k\). (from [Continuous random variables](#math.s2.crv))
A: The area must be 1: \(\displaystyle\int_0^3 kx\,dx = \tfrac92 k = 1\), so \(k = \tfrac29\).
Q: Evaluate \(\displaystyle\int_1^2 (3x^2 - 2)\,dx\). (from [Integration](#math.p1.integ))
A: \(\big[x^3 - 2x\big]_1^2 = (8 - 4) - (1 - 2) = 5\).
Q: \(X\) has PDF \(f(x) = \dfrac{x}{8}\) for \(0 \le x \le 4\). Find \(P(X > 2)\). (from [Continuous random variables](#math.s2.crv))
A: \(P(X > 2) = \displaystyle\int_2^4 \frac{x}{8}\,dx = \frac{16 - 4}{16} = \frac34\).
:::

## Probability density functions

A **continuous random variable** can take any value in an interval, so the chance of any one exact value is 0. Probabilities come from areas under a curve.

:::def Probability density function (PDF)
A function \(f\) such that \(P(a < X < b) = \displaystyle\int_a^b f(x)\,dx\) for all \(a < b\). It satisfies \(f(x) \ge 0\) for all \(x\), and the total area under its graph is 1: \(\displaystyle\int_{-\infty}^{\infty} f(x)\,dx = 1\).
:::

Because single values have probability 0, it makes no difference whether you write \(<\) or \(\le\): \(P(X \le 3) = P(X < 3)\). That is false for discrete variables, so do not carry the habit over in the other direction.

### A PDF that changes form

In 9709 the PDF was usually one expression on one interval. In 9231 it is often **piecewise**: a different expression on each of several intervals, and 0 outside them.

:::key Piecewise PDF
A PDF may be defined by several rules, for example
\[f(x) = \begin{cases} \dfrac{1}{10} & 0 \le x < 2 \\[4pt] \dfrac15 & 2 \le x \le 6 \\[4pt] 0 & \text{otherwise} \end{cases}\]
- Each piece must be \(\ge 0\) on its own interval.
- The areas of all the pieces add up to 1 (here \(2 \times \tfrac1{10} + 4 \times \tfrac15 = 1\)).
- The graph does **not** have to be continuous: this one jumps from \(\tfrac1{10}\) to \(\tfrac15\) at \(x = 2\). Both boundary values are allowed because a single point has probability 0.
- To find a probability, split the integral at every boundary that lies inside the interval.
:::

:::eg A random variable \(X\) has PDF \(f(x) = kx\) for \(0 \le x < 2\), \(f(x) = 2k\) for \(2 \le x \le 5\), and 0 otherwise. Find \(k\) and \(P(1 < X < 3)\).
The total area is 1. The first piece is a triangle and the second a rectangle:
\[\int_0^2 kx\,dx + \int_2^5 2k\,dx = 2k + 6k = 8k = 1\]
so \(k = \tfrac18\). Now split \(P(1 < X < 3)\) at the boundary \(x = 2\):
\[\begin{aligned}
P(1 < X < 3) &= \int_1^2 \frac{x}{8}\,dx + \int_2^3 \frac14\,dx \\
&= \frac{4 - 1}{16} + \frac14 = \frac{3}{16} + \frac{4}{16} = \frac{7}{16}
\end{aligned}\]
**Check by area**: the first part is a trapezium of width 1 with parallel sides \(\tfrac18\) and \(\tfrac14\), area \(\tfrac{3}{16}\); the second is a rectangle \(1 \times \tfrac14\).
:::

When constants are hidden in the formulas, every piece of information gives one equation. The total area is 1. A graph that is continuous at a boundary gives one more (the two pieces agree there). A given probability, mean or median gives another.

:::html
<figure class="fig small"><svg viewBox="0 0 350 190" role="img" aria-label="A piecewise PDF. It rises in a straight line from the origin to x = 2, where the rule is labelled a x. It is flat from x = 2 to x = 5, labelled b, and falls in a straight line to zero at x = 7, labelled c times (7 minus x). Dotted lines mark x = 2 and x = 5. The x-axis is marked 0, 2, 5 and 7.">
<line class="ax" x1="40" y1="150" x2="326" y2="150"/>
<line class="ax" x1="40" y1="150" x2="40" y2="20"/>
<line class="ln-m thin dash" x1="116" y1="50" x2="116" y2="150"/>
<line class="ln-m thin dash" x1="230" y1="50" x2="230" y2="150"/>
<polyline class="c1 sw2" fill="none" points="40,150 116,50 230,50 306,150"/>
<text class="tl" x="50" y="18">f(x)</text>
<text class="tl" x="318" y="144">x</text>
<text class="ts" x="116" y="166" text-anchor="middle">2</text>
<text class="ts" x="230" y="166" text-anchor="middle">5</text>
<text class="ts" x="306" y="166" text-anchor="middle">7</text>
<text class="ts" x="40" y="166" text-anchor="middle">0</text>
<text class="tl halo" x="52" y="86">ax</text>
<text class="tl halo" x="173" y="40" text-anchor="middle">b</text>
<text class="tl halo" x="284" y="96">c(7 − x)</text>
</svg><figcaption>The shape of a PDF with three unknown constants. The graph is continuous, so the pieces agree at \(x = 2\) and at \(x = 5\).</figcaption></figure>
:::

:::eg (Exam style) The PDF of \(X\) is shown in the diagram: \(f(x) = ax\) for \(0 \le x \le 2\), \(f(x) = b\) for \(2 < x \le 5\), \(f(x) = c(7 - x)\) for \(5 < x \le 7\), and \(f(x) = 0\) otherwise. The graph is continuous. (a) Find the values of \(a\), \(b\) and \(c\). (b) Find \(P(3 < X < 6)\).
**(a)** Continuity at \(x = 2\) gives \(2a = b\); continuity at \(x = 5\) gives \(b = 2c\). [B1] [B1]
The total area is 1:
\[\int_0^2 ax\,dx + \int_2^5 b\,dx + \int_5^7 c(7 - x)\,dx = 2a + 3b + 2c = 1\] [M1]
Substitute \(b = 2a\) and \(c = a\):
\[2a + 6a + 2a = 10a = 1\] [A1]
So \(a = \tfrac1{10}\), \(b = \tfrac15\) and \(c = \tfrac1{10}\). [A1]
**(b)** Split at \(x = 5\):
\[\begin{aligned}
P(3 < X < 6) &= \int_3^5 \frac15\,dx + \int_5^6 \frac{7 - x}{10}\,dx \\
&= \frac25 + \frac{1}{10}\left[7x - \frac{x^2}{2}\right]_5^6 \\
&= \frac25 + \frac{1}{10}\big(24 - 22.5\big) = \frac{11}{20}
\end{aligned}\] [M1] [A1]
:::

A given mean is a second equation, because \(E(X)\) is also an integral of the unknowns.

:::eg The PDF of \(X\) is \(f(x) = a + bx\) for \(0 \le x \le 2\) and 0 otherwise, and \(E(X) = \tfrac{10}{9}\). Find \(a\) and \(b\), and check that \(f \ge 0\).
The total area is 1:
\[\int_0^2 (a + bx)\,dx = 2a + 2b = 1\]
The mean is \(\tfrac{10}{9}\):
\[E(X) = \int_0^2 (ax + bx^2)\,dx = 2a + \frac{8b}{3} = \frac{10}{9}\]
Subtract the first equation from the second: \(\dfrac{8b}{3} - 2b = \dfrac{10}{9} - 1\), so \(\dfrac{2b}{3} = \dfrac19\) and \(b = \dfrac16\). Then \(2a = 1 - \dfrac13\) gives \(a = \dfrac13\).

\(f(x) = \dfrac13 + \dfrac{x}{6}\) is positive on \([0, 2]\), so it is a valid PDF. (If the solution had made \(f\) negative somewhere, the data would have been impossible.)
:::

## The cumulative distribution function

The PDF gives probabilities by integrating. The **CDF** does the integrating once, for every \(x\), and keeps the result as a formula.

:::def Cumulative distribution function (CDF)
\(F(x) = P(X \le x)\). For a continuous variable with PDF \(f\),
\[F(x) = \int_{-\infty}^{x} f(t)\,dt\]
:::

:::key Properties of the CDF
- \(F(x)\) is defined for **every** real \(x\): it is 0 below the smallest possible value and 1 above the largest.
- \(F\) never decreases, and \(F\) is continuous (even when \(f\) jumps).
- \(f(x) = F'(x)\) wherever \(F\) can be differentiated.
- \(P(a < X < b) = F(b) - F(a)\) and \(P(X > a) = 1 - F(a)\).
- For a piecewise PDF, integrate one piece at a time, and **start each new piece from the value of \(F\) at the end of the last one**.
:::

Here is the running example of this chapter, used for most of the next three sections. The PDF is a triangle on \([0, 4]\) with its peak at \(x = 1\):
\[f(x) = \begin{cases} \dfrac{x}{2} & 0 \le x \le 1 \\[4pt] \dfrac{4 - x}{6} & 1 < x \le 4 \\[4pt] 0 & \text{otherwise} \end{cases}\]
The area is \(\tfrac12 \times 4 \times \tfrac12 = 1\), as it should be. Both pieces equal \(\tfrac12\) at \(x = 1\), so the graph is continuous.

:::eg Find the CDF of the running example.
Work up the line from the left.

For \(x < 0\) nothing has happened yet: \(F(x) = 0\).

For \(0 \le x \le 1\): \(F(x) = \displaystyle\int_0^x \frac{t}{2}\,dt = \frac{x^2}{4}\). At the end of this piece \(F(1) = \tfrac14\).

For \(1 < x \le 4\): the probability up to 1 is \(\tfrac14\), and then more accumulates:
\[\begin{aligned}
F(x) &= \frac14 + \int_1^x \frac{4 - t}{6}\,dt \\
&= \frac14 + \frac16\left[4t - \frac{t^2}{2}\right]_1^x \\
&= \frac14 + \frac{8x - x^2 - 7}{12} = \frac{8x - x^2 - 4}{12}
\end{aligned}\]
For \(x > 4\) everything has happened: \(F(x) = 1\). The formula above does reach 1 at the top: \(F(4) = \tfrac{32 - 16 - 4}{12} = 1\).
\[F(x) = \begin{cases} 0 & x < 0 \\[2pt] \dfrac{x^2}{4} & 0 \le x \le 1 \\[4pt] \dfrac{8x - x^2 - 4}{12} & 1 < x \le 4 \\[4pt] 1 & x > 4 \end{cases}\]
**Check**: the two middle pieces agree at \(x = 1\) (\(\tfrac14\) and \(\tfrac{3}{12}\)).
:::

:::plot The PDF of the running example: two straight pieces meeting at the peak (1, 1/2). The area under both pieces together is 1.
--f "x/2+0*sqrt(1-x)+0*sqrt(x)" --f "(4-x)/6+0*sqrt(x-1)+0*sqrt(4-x)" --label "f(x) = x/2 (0 ≤ x ≤ 1)" --label "f(x) = (4 − x)/6 (1 < x ≤ 4)" --x -0.5 4.8 --y 0 0.75 --pt "1,0.5,(1, 1/2)@ne" --legend tr
:::

:::plot The CDF of the same variable. It is 0 to the left of 0, climbs along two curved pieces that join at (1, 1/4), and is 1 from \(x = 4\) onwards. The median, where \(F = 1/2\), is about 1.55.
--f "x**2/4+0*sqrt(1-x)+0*sqrt(x)" --f "(8*x-x**2-4)/12+0*sqrt(x-1)+0*sqrt(4-x)" --label "F(x) = x²/4 (0 ≤ x ≤ 1)" --label "F(x) = (8x − x² − 4)/12 (1 < x ≤ 4)" --x -0.5 4.8 --y 0 1.5 --pt "1,0.25,(1, 1/4)@se" --pt "1.551,0.5,median ≈ 1.55@nw" --pt "4,1,(4, 1)@sw" --legend tr
:::

Read the two graphs together. Where the PDF is high, probability piles up quickly, so the CDF is steep: the CDF above climbs fastest at \(x = 1\), where the PDF peaks, and flattens out as the PDF falls towards 0 at \(x = 4\). A flat stretch of \(F\) is an interval with no probability, and a CDF can never go down. The gradient of \(F\) at a point is the height of \(f\) there, and the height of \(F\) is the area of \(f\) so far.

:::warn Say what \(F\) is everywhere
A CDF is a function of every real \(x\). An answer that stops at "\(F(x) = \dfrac{8x - x^2 - 4}{12}\) for \(1 < x \le 4\)" has not defined \(F\) for \(x < 0\) and \(x > 4\); the mark scheme has a separate mark for the 0 and the 1. The other classic loss is to integrate the second piece from its own start, \(\displaystyle\int_1^x \dots\), and forget to add \(F(1)\). A quick test: the pieces must join with no gap, and \(F\) must reach exactly 1 at the top of the range.
:::

### From the CDF back to the PDF

Differentiating the CDF recovers the PDF, one piece at a time. Outside the range, \(F\) is constant, so the PDF is 0.

:::eg The CDF of \(X\) is \(F(x) = 0\) for \(x < 2\), \(F(x) = \dfrac{x^2 - 4}{12}\) for \(2 \le x \le 4\), and \(F(x) = 1\) for \(x > 4\). Find the PDF of \(X\) and \(P(X > 3)\).
\[f(x) = F'(x) = \frac{2x}{12} = \frac{x}{6} \quad (2 \le x \le 4)\]
and \(f(x) = 0\) otherwise. (Check: \(F(4) = \tfrac{12}{12} = 1\).) For the probability, use the complement:
\[P(X > 3) = 1 - F(3) = 1 - \frac{9 - 4}{12} = \frac{7}{12}\]
You can confirm this by integrating the PDF: \(\displaystyle\int_3^4 \frac{x}{6}\,dx = \frac{16 - 9}{12} = \frac{7}{12}\).
:::

If a question gives you the CDF with an unknown constant, use the facts that \(F\) reaches 1 at the top, and that it is continuous where pieces join.

:::eg \(X\) has CDF \(F(x) = 0\) for \(x < 1\), \(F(x) = \dfrac{(x - 1)^2}{c}\) for \(1 \le x \le 4\), and \(F(x) = 1\) for \(x > 4\). Find \(c\), the PDF, and \(P(2 < X < 3)\).
\(F(4) = 1\): \(\dfrac{3^2}{c} = 1\), so \(c = 9\).
\[f(x) = \frac{2(x - 1)}{9} \quad (1 \le x \le 4)\]
\[P(2 < X < 3) = F(3) - F(2) = \frac{4}{9} - \frac19 = \frac13\]
:::

## Median, quartiles and percentiles

The \(p\)-th **percentile** is the value below which \(p\%\) of the distribution lies. Because \(F(x)\) is exactly the probability of being below \(x\), you find it by solving an equation.

:::key Percentiles from the CDF
- The median \(m\): \(F(m) = \tfrac12\).
- The lower and upper quartiles \(Q_1\), \(Q_3\): \(F(Q_1) = \tfrac14\), \(F(Q_3) = \tfrac34\).
- The \(p\)-th percentile: \(F(x) = \dfrac{p}{100}\).
- Choose the correct piece of \(F\) first: compare the target with the values of \(F\) at the boundaries. Then solve, and keep the root that lies inside that piece.
:::

:::eg For the running example, find the median, the quartiles, the interquartile range and the 90th percentile.
The values of \(F\) at the boundaries are \(F(0) = 0\), \(F(1) = \tfrac14\), \(F(4) = 1\).

**Median.** \(\tfrac12\) is above \(F(1) = \tfrac14\), so the median is in the second piece:
\[\begin{aligned}
\frac{8m - m^2 - 4}{12} &= \frac12 \\
m^2 - 8m + 10 &= 0 \\
m &= 4 \pm \sqrt{6}
\end{aligned}\]
Only \(m = 4 - \sqrt{6} = 1.55\) lies in \([1, 4]\); the other root, 6.45, is outside the range.

**Lower quartile.** \(F(1) = \tfrac14\) exactly, so \(Q_1 = 1\). (If you wrongly solve \(\tfrac{x^2}{4} = \tfrac14\) you still get 1, but only because the boundary was lucky.)

**Upper quartile.**
\[\begin{aligned}
\frac{8x - x^2 - 4}{12} &= \frac34 \\
x^2 - 8x + 13 &= 0 \\
Q_3 &= 4 - \sqrt{3} = 2.27
\end{aligned}\]
The interquartile range is \(Q_3 - Q_1 = 3 - \sqrt{3} = 1.27\).

**90th percentile.** \(8x - x^2 - 4 = 10.8\), so \(x^2 - 8x + 14.8 = 0\) and \(x = 4 - \sqrt{1.2} = 2.90\).
:::

The median is not the mean here. The distribution is skewed to the right (a short steep rise, a long gentle fall), so the mean (found below as \(\tfrac53 = 1.67\)) is above the median (1.55), which is above the mode (1).

:::def Mode
The mode of a continuous random variable is the value of \(x\) at which the PDF has its greatest value. Find it by sketching \(f\), or by solving \(f'(x) = 0\) when \(f\) is smooth, and also check the ends of the intervals: for the running example the maximum is at the boundary point \(x = 1\), where the derivative does not exist, and the mode is 1.
:::

Sometimes the equation \(F(m) = \tfrac12\) cannot be solved exactly. Then you show the median lies in a short interval by a **change of sign**: \(F(a) - \tfrac12\) and \(F(b) - \tfrac12\) have opposite signs, and \(F\) is continuous, so the median is between \(a\) and \(b\).

:::eg The continuous random variable \(X\) has PDF \(f(x) = 12x^2(1 - x)\) for \(0 \le x \le 1\) and 0 otherwise. (a) Find the mode. (b) Find \(E(X)\) and \(\mathrm{Var}(X)\). (c) Show that the median lies between 0.6 and 0.65.
**(a)** Differentiate \(f(x) = 12x^2 - 12x^3\): \(f'(x) = 24x - 36x^2 = 12x(2 - 3x)\), which is 0 at \(x = \tfrac23\). The values at the ends are \(f(0) = f(1) = 0\), so \(x = \tfrac23\) is the maximum and the mode is \(\tfrac23\).

**(b)**
\[\begin{aligned}
E(X) &= \int_0^1 12x^3(1 - x)\,dx = 12\left(\frac14 - \frac15\right) = \frac35 \\
E(X^2) &= \int_0^1 12x^4(1 - x)\,dx = 12\left(\frac15 - \frac16\right) = \frac25 \\
\mathrm{Var}(X) &= \frac25 - \frac{9}{25} = \frac{1}{25}
\end{aligned}\]
**(c)** The CDF is \(F(x) = \displaystyle\int_0^x (12t^2 - 12t^3)\,dt = 4x^3 - 3x^4\). Then
\[F(0.6) = 4(0.216) - 3(0.1296) = 0.4752 < 0.5, \qquad F(0.65) = 4(0.274625) - 3(0.17850625) = 0.5630 > 0.5\]
\(F\) is continuous and increasing, so \(F(m) = 0.5\) for some \(m\) between 0.6 and 0.65. (The value is 0.614.)

Here the mode \(0.667\) is above the median \(0.614\), which is above the mean \(0.6\). This PDF is skewed to the left (a long tail towards 0), so the order is the reverse of the running example, which was skewed to the right. Do not quote an ordering without looking at the shape.
:::

:::eg (Exam style) The continuous random variable \(X\) has CDF \(F(x) = 0\) for \(x < 0\), \(F(x) = \dfrac{x(12 - x)}{36}\) for \(0 \le x \le 6\), and \(F(x) = 1\) for \(x > 6\). (a) Verify that \(F\) is a CDF, by finding \(F(6)\) and showing \(F\) never decreases. (b) Find the PDF of \(X\). (c) Find the median of \(X\), giving the answer to 3 significant figures. (d) Find the value of \(a\) such that \(P(X \le a) = 0.9\).
**(a)** \(F(6) = \dfrac{6 \times 6}{36} = 1\), so \(F\) joins on to 1. [B1]
\(F'(x) = \dfrac{12 - 2x}{36} = \dfrac{6 - x}{18}\), which is at least 0 for \(0 \le x \le 6\), so \(F\) does not decrease. [B1]
**(b)**
\[f(x) = \frac{6 - x}{18} \quad (0 \le x \le 6)\]
and 0 otherwise. [B1]
**(c)** Solve \(F(m) = \tfrac12\):
\[\begin{aligned}
\frac{m(12 - m)}{36} &= \frac12 \\
m^2 - 12m + 18 &= 0
\end{aligned}\] [M1]
\[m = 6 - \sqrt{18} = 1.76\] [A1]
(the root \(6 + \sqrt{18}\) is above 6). [B1]
**(d)** \(a^2 - 12a + 32.4 = 0\), so \(a = 6 - \sqrt{3.6}\) \(= 4.10\). [M1] [A1]
:::

## Expectation and variance

The mean of a continuous variable replaces the sum \(\sum x\,p\) by the integral \(\int x f(x)\,dx\). The same step works for any function of \(X\).

:::key Expectation and variance
- \(E(X) = \mu = \displaystyle\int_{-\infty}^{\infty} x\,f(x)\,dx\)
- \(E\big(g(X)\big) = \displaystyle\int_{-\infty}^{\infty} g(x)\,f(x)\,dx\) for any function \(g\)
- \(\mathrm{Var}(X) = E(X^2) - \big(E(X)\big)^2\), where \(E(X^2) = \displaystyle\int x^2 f(x)\,dx\)
- \(E(aX + b) = aE(X) + b\) and \(\mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)\)
- For a piecewise PDF, integrate over each piece and add. The integral only has to run over the range where \(f\) is not 0.
:::

Be careful with the second bullet. In general \(E(g(X))\) is **not** \(g(E(X))\): for example \(E(X^2) \ne \big(E(X)\big)^2\) (their difference is the variance), and \(E\!\left(\dfrac1X\right) \ne \dfrac{1}{E(X)}\). The only functions that pass through the \(E\) unchanged are the linear ones \(aX + b\).

:::proof Why \(\mathrm{Var}(X) = E(X^2) - \mu^2\) for a continuous variable
Start from the definition \(\mathrm{Var}(X) = E\big((X - \mu)^2\big)\). Using \(g(x) = (x - \mu)^2\):
\[\mathrm{Var}(X) = \int (x - \mu)^2 f(x)\,dx\]
Expand the bracket and split the integral:
\[\mathrm{Var}(X) = \int x^2 f(x)\,dx - 2\mu \int x f(x)\,dx + \mu^2 \int f(x)\,dx\]
The first integral is \(E(X^2)\). The second is \(\mu\), by definition. The third is 1, because the total area is 1. So
\[\mathrm{Var}(X) = E(X^2) - 2\mu \times \mu + \mu^2 \times 1 = E(X^2) - \mu^2\]
:::

:::eg For the running example, find \(E(X)\), \(E(X^2)\) and \(\mathrm{Var}(X)\).
Integrate over each piece and add:
\[\begin{aligned}
E(X) &= \int_0^1 x \cdot \frac{x}{2}\,dx + \int_1^4 x \cdot \frac{4 - x}{6}\,dx \\
&= \left[\frac{x^3}{6}\right]_0^1 + \frac16\left[2x^2 - \frac{x^3}{3}\right]_1^4 \\
&= \frac16 + \frac16\left(\frac{32}{3} - \frac53\right) = \frac16 + \frac32 = \frac53
\end{aligned}\]
\[\begin{aligned}
E(X^2) &= \int_0^1 \frac{x^3}{2}\,dx + \int_1^4 \frac{x^2(4 - x)}{6}\,dx \\
&= \frac18 + \frac16\left[\frac{4x^3}{3} - \frac{x^4}{4}\right]_1^4 \\
&= \frac18 + \frac16\left(\frac{64}{3} - \frac{13}{12}\right) = \frac18 + \frac{27}{8} = \frac72
\end{aligned}\]
\[\mathrm{Var}(X) = \frac72 - \left(\frac53\right)^2 = \frac{63 - 50}{18} = \frac{13}{18}\]
:::

:::eg A continuous random variable has PDF \(f(x) = \dfrac{3}{x^4}\) for \(x \ge 1\) and 0 otherwise. Show that this is a PDF, and find \(E(X)\), \(\mathrm{Var}(X)\) and \(E\!\left(\dfrac1X\right)\). Does \(E(X^3)\) exist?
The area is
\[\int_1^\infty 3x^{-4}\,dx = \left[-x^{-3}\right]_1^\infty = 0 - (-1) = 1\]
and \(f \ge 0\), so it is a PDF.
\[\begin{aligned}
E(X) &= \int_1^\infty 3x^{-3}\,dx = \left[-\tfrac32 x^{-2}\right]_1^\infty = \tfrac32 \\
E(X^2) &= \int_1^\infty 3x^{-2}\,dx = \left[-3x^{-1}\right]_1^\infty = 3 \\
\mathrm{Var}(X) &= 3 - \left(\tfrac32\right)^2 = \tfrac34 \\
E\!\left(\frac1X\right) &= \int_1^\infty \frac1x \cdot \frac{3}{x^4}\,dx = \left[-\tfrac34 x^{-4}\right]_1^\infty = \tfrac34
\end{aligned}\]
Note \(E(1/X) = \tfrac34\) but \(1/E(X) = \tfrac23\): they are different.

\(E(X^3) = \displaystyle\int_1^\infty 3x^{-1}\,dx = \big[3\ln x\big]_1^\infty\) grows without limit, so \(E(X^3)\) does not exist. A mean can exist when a higher moment does not: this is why mark schemes say "converges" in questions on infinite ranges.
:::

### A real context

:::eg The lifetime \(T\) of a component, in years, has PDF \(f(t) = \dfrac{3t(4 - t)}{32}\) for \(0 \le t \le 4\), and 0 otherwise. (a) Verify that this is a PDF. (b) Find \(P(T > 3)\). (c) Find \(E(T)\) and \(\mathrm{Var}(T)\). (d) A replacement costs \(\pounds C\) where \(C = 10 + \dfrac{24}{T}\) (the cost per year of service falls as the component lasts longer). Find the expected cost \(E(C)\).
**(a)**
\[\int_0^4 \frac{3}{32}(4t - t^2)\,dt = \frac{3}{32}\left[2t^2 - \frac{t^3}{3}\right]_0^4 = \frac{3}{32} \times \frac{32}{3} = 1\]
and \(f \ge 0\) on \([0, 4]\).

**(b)** The CDF is \(F(t) = \dfrac{3}{32}\left(2t^2 - \dfrac{t^3}{3}\right) = \dfrac{6t^2 - t^3}{32}\) on \([0, 4]\), so
\[P(T > 3) = 1 - F(3) = 1 - \frac{54 - 27}{32} = \frac{5}{32}\]

**(c)** The graph is symmetric about \(t = 2\), so \(E(T) = 2\). To confirm:
\[E(T^2) = \frac{3}{32}\int_0^4 (4t^3 - t^4)\,dt = \frac{3}{32}\left(256 - \frac{1024}{5}\right) = 4.8\]
\[\mathrm{Var}(T) = 4.8 - 2^2 = 0.8\]

**(d)** \(E(C) = 10 + 24\,E\!\left(\dfrac1T\right)\), using \(E(aX + b) = aE(X) + b\) with \(X = \dfrac1T\):
\[E\!\left(\frac1T\right) = \frac{3}{32}\int_0^4 (4 - t)\,dt = \frac{3}{32} \times 8 = \frac34\]
so \(E(C) = 10 + 24 \times \tfrac34 = \pounds 28\). Compare \(10 + \dfrac{24}{E(T)} = \pounds 22\): using \(E(T)\) inside the formula would give the wrong cost.
:::

When \(g\) is defined in pieces, the integral is split at the same places. If \(g\) is a constant on each piece, \(E(g(X))\) is a probability-weighted average of those constants, and the probabilities come from the CDF.

:::eg The component above (\(f(t) = \dfrac{3t(4 - t)}{32}\) on \([0, 4]\), \(F(t) = \dfrac{6t^2 - t^3}{32}\)) is sold with a warranty. If it fails in the first year the company refunds \(\pounds 60\); if it fails in the second year, \(\pounds 20\); after that nothing. Find the expected refund.
Let the refund be \(R\), so \(R = 60\) for \(T < 1\), \(R = 20\) for \(1 \le T < 2\) and \(R = 0\) for \(T \ge 2\).
\[\begin{aligned}
P(T < 1) &= F(1) = \frac{6 - 1}{32} = \frac{5}{32} \\
P(1 \le T < 2) &= F(2) - F(1) = \frac{24 - 8}{32} - \frac{5}{32} = \frac{11}{32}
\end{aligned}\]
\[E(R) = 60 \times \frac{5}{32} + 20 \times \frac{11}{32} + 0 = \frac{300 + 220}{32} = \pounds 16.25\]
:::

## The distribution of a related variable

Suppose \(Y\) is built from \(X\), for example \(Y = X^3\) or \(Y = \dfrac1X\). To find the PDF of \(Y\), do not substitute into the PDF of \(X\): find the **CDF** of \(Y\) first. For any \(y\),
\[G(y) = P(Y \le y)\]
and the inequality \(Y \le y\) can be turned into an inequality about \(X\), which \(F\) already handles.

:::steps
1. Write \(G(y) = P(Y \le y) = P\big(h(X) \le y\big)\), where \(Y = h(X)\).
2. Solve the inequality for \(X\). If \(h\) is **increasing**, \(h(X) \le y\) becomes \(X \le h^{-1}(y)\). If \(h\) is **decreasing**, the inequality **reverses**: \(X \ge h^{-1}(y)\).
3. Write the probability with \(F\): \(G(y) = F\big(h^{-1}(y)\big)\) for an increasing \(h\), and \(1 - F\big(h^{-1}(y)\big)\) for a decreasing one.
4. State the range of \(Y\) from the range of \(X\), and say \(G(y) = 0\) below it and \(G(y) = 1\) above it.
5. Differentiate: the PDF of \(Y\) is \(g(y) = G'(y)\), on the range of \(Y\) only.
:::

:::eg \(X\) has PDF \(f(x) = \dfrac{x}{2}\) for \(0 \le x \le 2\) and 0 otherwise. Find the CDF and PDF of \(Y = X^3\).
First the CDF of \(X\): \(F(x) = \dfrac{x^2}{4}\) for \(0 \le x \le 2\).

\(Y = X^3\) is increasing, and \(X\) takes values 0 to 2, so \(Y\) takes values 0 to \(2^3 = 8\). For \(0 \le y \le 8\):
\[\begin{aligned}
G(y) &= P(X^3 \le y) = P\big(X \le y^{1/3}\big) \\
&= F\big(y^{1/3}\big) = \frac{y^{2/3}}{4}
\end{aligned}\]
So \(G(y) = 0\) for \(y < 0\), \(G(y) = \dfrac{y^{2/3}}{4}\) for \(0 \le y \le 8\), and \(G(y) = 1\) for \(y > 8\). (Check: \(G(8) = \tfrac44 = 1\).)

Differentiate:
\[g(y) = \frac{d}{dy}\left(\frac{y^{2/3}}{4}\right) = \frac{1}{6}\,y^{-1/3} \quad (0 < y \le 8)\]
**Check**: the area under \(g\) is \(\displaystyle\int_0^8 \tfrac16 y^{-1/3}\,dy = \tfrac16 \times \tfrac32 \times 8^{2/3} = \tfrac16 \times \tfrac32 \times 4 = 1\).
:::

The PDF of \(Y\) is not \(f\) with \(x\) replaced by \(y^{1/3}\): the density of \(Y\) is large near \(y = 0\) because many values of \(X\) are squeezed into a small interval of cubes. The derivative takes care of that squeeze automatically.

For a **decreasing** function the inequality turns round.

:::eg \(X\) has PDF \(f(x) = \dfrac{3}{x^4}\) for \(x \ge 1\). Find the PDF of \(Y = \dfrac1X\).
The CDF of \(X\) is \(F(x) = \displaystyle\int_1^x 3t^{-4}\,dt = 1 - x^{-3}\) for \(x \ge 1\).

\(X\) takes values from 1 upwards, so \(Y = \dfrac1X\) takes values in \((0, 1]\). \(\dfrac1X\) is decreasing, so for \(0 < y \le 1\):
\[\begin{aligned}
G(y) &= P\left(\frac1X \le y\right) = P\left(X \ge \frac1y\right) \\
&= 1 - F\left(\frac1y\right) = 1 - \left(1 - y^3\right) = y^3
\end{aligned}\]
Then \(g(y) = 3y^2\) for \(0 < y \le 1\).
**Check**: \(\displaystyle\int_0^1 3y^2\,dy = 1\). Also \(E(Y) = \displaystyle\int_0^1 3y^3\,dy = \tfrac34\), which matches \(E(1/X) = \tfrac34\) found earlier by the other method.
:::

:::warn Three lost marks in the CDF method
1. **Reversed inequality.** For a decreasing \(h\) the direction turns round, so \(G(y) = 1 - F(\dots)\), not \(F(\dots)\).
2. **Wrong limits for \(Y\).** Work out where \(Y\) lives from where \(X\) lives, using the end values (here \(0\) to \(8\), or \(0\) to \(1\)). A \(g(y)\) with no range, or \(G\) with no 0 and 1 outside, loses a mark.
3. **Stopping at \(G\).** The question usually asks for the **PDF**: differentiate.
:::

The first piece of each worked example above is one-to-one, so the method is straightforward. The same method can handle a PDF in several pieces: find \(G\) piece by piece, with the pieces of \(F\), and the pieces of \(g\) come out of the pieces of \(G\).

:::eg (Exam style) The continuous random variable \(X\) has PDF \(f(x) = kx\) for \(0 \le x \le 1\), \(f(x) = k\) for \(1 < x \le 3\), and \(f(x) = 0\) otherwise. (a) Show that \(k = \tfrac25\). (b) Find \(E(X)\). (c) Find the median of \(X\). (d) Find the CDF and the PDF of \(Y = X^2\).
**(a)** The total area is 1:
\[\int_0^1 kx\,dx + \int_1^3 k\,dx = \frac{k}{2} + 2k = \frac{5k}{2} = 1\] [M1]
so \(k = \tfrac25\). [A1]
**(b)**
\[\begin{aligned}
E(X) &= \int_0^1 \frac25 x^2\,dx + \int_1^3 \frac25 x\,dx \\
&= \frac{2}{15} + \frac15\left[x^2\right]_1^3 \\
&= \frac{2}{15} + \frac{8}{5} = \frac{26}{15}
\end{aligned}\] [M1] [A1] [A1]
**(c)** \(F(1) = \tfrac15\), which is below \(\tfrac12\), so the median lies in the second piece, where \(F(x) = \tfrac15 + \tfrac25(x - 1) = \dfrac{2x - 1}{5}\). [M1]
\[\frac{2m - 1}{5} = \frac12 \quad\Rightarrow\quad m = \frac74 = 1.75\] [A1]
**(d)** The CDF of \(X\) is \(F(x) = \dfrac{x^2}{5}\) for \(0 \le x \le 1\) and \(\dfrac{2x - 1}{5}\) for \(1 < x \le 3\). Since \(X\) is positive, \(Y = X^2\) is increasing for the values that occur, and \(Y\) takes values from 0 to 9. [B1]
\[G(y) = P(X^2 \le y) = P\big(X \le \sqrt{y}\big) = F\big(\sqrt{y}\big)\] [M1]
For \(0 \le y \le 1\), \(\sqrt{y} \le 1\) and \(G(y) = \dfrac{y}{5}\). For \(1 < y \le 9\), \(\sqrt{y}\) is in the second piece and \(G(y) = \dfrac{2\sqrt{y} - 1}{5}\). [A1]
Differentiate each piece:
\[g(y) = \begin{cases} \dfrac15 & 0 < y \le 1 \\[4pt] \dfrac{1}{5\sqrt{y}} & 1 < y \le 9 \end{cases}\] [M1] [A1]
**Check**: \(\tfrac15 \times 1 + \displaystyle\int_1^9 \frac{dy}{5\sqrt{y}} = \tfrac15 + \tfrac25 \times (3 - 1) = 1\).
:::

:::exam Presenting a CDF answer
Give \(F\) for every \(x\), with the intervals shown. Show the line \(G(y) = F(\sqrt{y})\) (or its equivalent) before any algebra: that line earns the method mark even if the later working goes wrong. When asked for "the distribution of \(Y\)" give the PDF and its range, not only the CDF. Exact answers (fractions and surds) are expected unless the question asks for decimals; otherwise give 3 significant figures.
:::

## Spot the error, practice and stretch

:::eg Spot the error: \(X\) has PDF \(f(x) = \dfrac{x}{6}\) for \(0 \le x \le 2\), \(f(x) = \dfrac13\) for \(2 < x \le 4\), and 0 otherwise. (a) Find the CDF of \(X\) [4 marks]. (b) Find the median [2 marks].
A student wrote this answer.

Line 1: \(0 \le x \le 2\): \(F(x) = \displaystyle\int_0^x \frac{t}{6}\,dt = \frac{x^2}{12}\)
Line 2: \(2 < x \le 4\): \(F(x) = \displaystyle\int_2^x \frac13\,dt = \frac{x - 2}{3}\)
Line 3: \(F(x) = 0\) for \(x < 0\) and \(F(x) = 1\) for \(x > 4\)
Line 4: \(\dfrac{x - 2}{3} = \dfrac12\), so the median is \(3.5\)

Line 1 is correct. [B1] Line 3 is correct. [B1]

**Line 2 loses two marks.** [M0] [A0] The student started the second integral at 2 and forgot to add \(F(2) = \tfrac{4}{12} = \tfrac13\). The check shows it: this formula gives \(F(4) = \tfrac23\), not 1. The correct line is \(F(x) = \tfrac13 + \tfrac{x - 2}{3} = \dfrac{x - 1}{3}\).

Line 4 uses the student's own \(F\) in the right piece, so it scores follow-through marks. [M1] [A1 FT] The student scores 4 out of 6. The correct median is from \(\dfrac{m - 1}{3} = \dfrac12\), so \(m = 2.5\).
:::

:::try Start easy, finish at exam standard
Q: \(X\) has PDF \(f(x) = \dfrac{3}{26}x^2\) for \(1 \le x \le 3\) and 0 otherwise. Show that the area is 1 and find \(P(X > 2)\).
A: \(\displaystyle\int_1^3 \frac{3}{26}x^2\,dx = \frac{1}{26}\left[x^3\right]_1^3 = \frac{27 - 1}{26} = 1\). \(P(X > 2) = \dfrac{27 - 8}{26} = \dfrac{19}{26}\).
Q: \(X\) has PDF \(f(x) = \tfrac14\) for \(0 \le x < 1\), \(f(x) = \tfrac12\) for \(1 \le x \le 2.5\), and 0 otherwise. Verify that it is a PDF and find \(F(2)\).
A: Area \(= \tfrac14 + 1.5 \times \tfrac12 = 1\). \(F(2) = \tfrac14 + \tfrac12 \times 1 = \tfrac34\).
Q: Given \(F(x) = \dfrac{x^3}{27}\) for \(0 \le x \le 3\) (0 below, 1 above), find the PDF and the median.
A: \(f(x) = \dfrac{x^2}{9}\) for \(0 \le x \le 3\). \(\dfrac{m^3}{27} = \dfrac12\), so \(m = 3 \times 0.5^{1/3} = 2.38\) to 3 s.f.
Q: \(X\) has PDF \(f(x) = \dfrac{x}{8}\) for \(0 \le x \le 4\). Find \(E(X)\), \(\mathrm{Var}(X)\) and \(E(\sqrt{X})\).
A: \(E(X) = \displaystyle\int_0^4 \frac{x^2}{8}\,dx = \frac{8}{3}\). \(E(X^2) = \displaystyle\int_0^4 \frac{x^3}{8}\,dx = 8\), so \(\mathrm{Var}(X) = 8 - \tfrac{64}{9} = \tfrac89\). \(E(\sqrt{X}) = \displaystyle\int_0^4 \frac{x^{3/2}}{8}\,dx = \frac18 \times \frac25 \times 32 = \frac85\).
Q: \(X\) has CDF \(F(x) = \dfrac{x^2}{16}\) for \(0 \le x \le 4\). Find the CDF and PDF of \(Y = 2X + 1\).
A: \(Y\) is increasing and takes values 1 to 9. \(G(y) = P\!\left(X \le \frac{y - 1}{2}\right) = \dfrac{(y - 1)^2}{64}\) for \(1 \le y \le 9\), so \(g(y) = \dfrac{y - 1}{32}\).
Q: \(X\) has PDF \(f(x) = \tfrac12\) for \(0 \le x \le 2\) (uniform). Find the PDF of \(Y = X^2\).
A: \(G(y) = P(X \le \sqrt{y}) = \dfrac{\sqrt{y}}{2}\) for \(0 \le y \le 4\), so \(g(y) = \dfrac{1}{4\sqrt{y}}\).
Q: \(X\) has PDF \(f(x) = \dfrac{x}{2}\) for \(0 \le x \le 2\). Find the PDF of \(Y = 4 - X\).
A: \(Y\) is decreasing and takes values 2 to 4. \(G(y) = P(4 - X \le y) = P(X \ge 4 - y) = 1 - \dfrac{(4 - y)^2}{4}\), so \(g(y) = \dfrac{4 - y}{2}\) for \(2 \le y \le 4\).
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ The continuous random variable \(X\) has CDF \(F(x) = 0\) for \(x < 1\), \(F(x) = \dfrac{(x - 1)^2}{9}\) for \(1 \le x \le 4\), and \(F(x) = 1\) for \(x > 4\). Find the PDF of \(X\), \(P(2 < X < 3)\) and the median.
A: \(f(x) = \dfrac{2(x - 1)}{9}\) for \(1 \le x \le 4\), 0 otherwise. [B1]
\(P(2 < X < 3) = F(3) - F(2)\) [M1] \(= \dfrac49 - \dfrac19 = \dfrac13\). [A1]
\(\dfrac{(m - 1)^2}{9} = \dfrac12\) [M1], so \(m = 1 + \dfrac{3}{\sqrt{2}} = 3.12\). [A1]
Q: [6 marks] ★★ The PDF of \(X\) is \(f(x) = \dfrac{x}{8}\) for \(0 \le x \le 4\) and 0 otherwise. Find \(E(X)\), \(\mathrm{Var}(X)\) and \(E(\sqrt{X})\).
A: \(E(X) = \displaystyle\int_0^4 \frac{x^2}{8}\,dx = \frac83\). [M1] [A1]
\(E(X^2) = \displaystyle\int_0^4 \frac{x^3}{8}\,dx = 8\), so \(\mathrm{Var}(X) = 8 - \dfrac{64}{9} = \dfrac89\). [M1] [A1]
\(E(\sqrt{X}) = \displaystyle\int_0^4 \frac{x^{3/2}}{8}\,dx = \frac18 \times \frac25 \times 32 = \frac85\). [M1] [A1]
Q: [5 marks] ★★ \(X\) has PDF \(f(x) = \dfrac{3x^2}{8}\) for \(0 \le x \le 2\) and 0 otherwise. Find the CDF and the PDF of \(Y = 2X + 1\).
A: \(F(x) = \dfrac{x^3}{8}\) for \(0 \le x \le 2\). [B1]
\(Y\) takes values 1 to 5. \(G(y) = P\!\left(X \le \dfrac{y - 1}{2}\right)\) [M1] \(= \dfrac{(y - 1)^3}{64}\) for \(1 \le y \le 5\) (0 below, 1 above). [A1]
\(g(y) = \dfrac{3(y - 1)^2}{64}\) for \(1 \le y \le 5\). [M1] [A1]
Q: [7 marks] ★★ The PDF of \(X\) is \(f(x) = \dfrac{2x}{9}\) for \(0 \le x \le 3\) and 0 otherwise. (a) Find the CDF and PDF of \(Y = \sqrt{X}\). (b) Find \(E(Y)\) in two ways.
A: (a) \(F(x) = \dfrac{x^2}{9}\). \(Y\) takes values 0 to \(\sqrt3\). [B1]
\(G(y) = P(\sqrt{X} \le y) = P(X \le y^2) = F(y^2)\) [M1] \(= \dfrac{y^4}{9}\) for \(0 \le y \le \sqrt{3}\). [A1]
\(g(y) = \dfrac{4y^3}{9}\) for \(0 \le y \le \sqrt{3}\). [A1]
(b) \(E(Y) = \displaystyle\int_0^{\sqrt3} y \cdot \frac{4y^3}{9}\,dy = \frac{4}{45}\left(\sqrt3\right)^5 = \frac{4\sqrt3}{5}\). [M1] [A1]
Using \(E(\sqrt{X}) = \displaystyle\int_0^3 \sqrt{x} \cdot \frac{2x}{9}\,dx = \frac{4}{45} \times 3^{5/2}\), the same value, \(1.39\) to 3 s.f. [A1]
Q: [10 marks] (#math.s2.crv) ★★★ The PDF of \(X\) is \(f(x) = ax\) for \(0 \le x \le 2\), \(f(x) = \dfrac{a(6 - x)}{2}\) for \(2 < x \le 6\), and 0 otherwise. (a) Find \(a\). (b) Find the CDF of \(X\). (c) Find the median of \(X\).
H: The pieces join at \(x = 2\), so the graph is a triangle. The area is \(2a + 4a\).
H: For the second piece of \(F\), start from \(F(2)\), or integrate from the right using \(1 - \displaystyle\int_x^6\).
H: Decide which piece contains the median by comparing \(F(2)\) with \(\tfrac12\).
A: (a) \(\displaystyle\int_0^2 ax\,dx + \int_2^6 \frac{a(6 - x)}{2}\,dx = 2a + 4a = 6a = 1\) [M1] [A1], so \(a = \tfrac16\). [A1]
(b) \(F(x) = \dfrac{x^2}{12}\) for \(0 \le x \le 2\), and \(F(2) = \tfrac13\). [B1]
For \(2 < x \le 6\): \(F(x) = \tfrac13 + \displaystyle\int_2^x \frac{6 - t}{12}\,dt\) [M1] \(= 1 - \dfrac{(6 - x)^2}{24}\). [A1]
\(F(x) = 0\) for \(x < 0\) and \(1\) for \(x > 6\). [B1]
(c) \(F(2) = \tfrac13 < \tfrac12\), so \(m\) is in the second piece. [M1]
\((6 - m)^2 = 12\), so \(m = 6 - 2\sqrt3 = 2.54\). [A1] [A1]
Q: [12 marks] (#math.p3.integ) ★★★ The PDF of \(X\) is \(f(x) = \dfrac1x\) for \(1 \le x \le \mathrm{e}\) and 0 otherwise. (a) Show that this is a PDF and find the CDF. (b) Find the median. (c) Find \(E(X)\) and \(\mathrm{Var}(X)\). (d) Find the CDF of \(Y = \ln X\) and describe the distribution of \(Y\).
H: \(\displaystyle\int \dfrac1x\,dx = \ln x\).
H: For \(E(X^2)\) the integrand is \(x^2 \cdot \dfrac1x = x\).
H: In (d), \(Y = \ln X\) is increasing, so \(G(y) = F(\mathrm{e}^y)\); give the range of \(Y\).
A: (a) \(\displaystyle\int_1^{\mathrm{e}} \frac1x\,dx = \ln \mathrm{e} - \ln 1 = 1\). [B1]
\(F(x) = \ln x\) for \(1 \le x \le \mathrm{e}\), with 0 below 1 and 1 above \(\mathrm{e}\). [B1] [B1]
(b) \(\ln m = \tfrac12\), so \(m = \sqrt{\mathrm{e}} = 1.65\). [M1] [A1]
(c) \(E(X) = \displaystyle\int_1^{\mathrm{e}} 1\,dx = \mathrm{e} - 1 = 1.72\). [M1] [A1]
\(E(X^2) = \displaystyle\int_1^{\mathrm{e}} x\,dx = \dfrac{\mathrm{e}^2 - 1}{2}\), so \(\mathrm{Var}(X) = \dfrac{\mathrm{e}^2 - 1}{2} - (\mathrm{e} - 1)^2 = 0.242\). [M1] [A1]
(d) \(Y\) takes values 0 to 1. \(G(y) = P(\ln X \le y) = P(X \le \mathrm{e}^y) = F(\mathrm{e}^y) = y\) for \(0 \le y \le 1\). [M1] [A1]
So \(g(y) = 1\) on \([0, 1]\): \(Y\) is uniformly distributed on \([0, 1]\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ \(X\) has PDF \(f(x) = \dfrac32 x^2\) for \(-1 \le x \le 1\) and 0 otherwise. Find the CDF and PDF of \(Y = X^2\). Why can you not use \(G(y) = F(\sqrt{y})\) here?
H: \(Y \le y\) means \(-\sqrt{y} \le X \le \sqrt{y}\): both signs of \(X\) count.
H: First find \(F(x) = \dfrac{x^3 + 1}{2}\) for \(-1 \le x \le 1\).
A: \(F(x) = \dfrac{x^3 + 1}{2}\) for \(-1 \le x \le 1\). [B1]
\(Y = X^2\) is not increasing on \([-1, 1]\): both \(X = 0.5\) and \(X = -0.5\) give \(Y = 0.25\). So \(Y \le y\) means \(-\sqrt{y} \le X \le \sqrt{y}\). [M1]
\[G(y) = F\big(\sqrt{y}\big) - F\big(-\sqrt{y}\big) = \frac{y^{3/2} + 1}{2} - \frac{1 - y^{3/2}}{2} = y^{3/2}\] [M1] [A1]
for \(0 \le y \le 1\), so \(g(y) = \tfrac32\sqrt{y}\) on \(0 < y \le 1\). [M1] [A1]
Q: [8 marks] ★★★ \(X\) has PDF \(f(x) = \dfrac{2}{(x + 1)^3}\) for \(x \ge 0\) and 0 otherwise. (a) Find the CDF and \(E(X)\). (b) Show that \(E(X) = \displaystyle\int_0^\infty \big(1 - F(x)\big)\,dx\) here. (c) Show that \(\mathrm{Var}(X)\) does not exist.
H: For (a), write \(\dfrac{2x}{(x + 1)^3} = \dfrac{2}{(x + 1)^2} - \dfrac{2}{(x + 1)^3}\).
H: For (c), \(E(X^2)\) has integrand \(\dfrac{2x^2}{(x + 1)^3}\), which behaves like \(\dfrac2x\) for large \(x\).
A: (a) \(F(x) = \displaystyle\int_0^x 2(t + 1)^{-3}\,dt = 1 - \dfrac{1}{(x + 1)^2}\). [M1] [A1]
\(E(X) = \displaystyle\int_0^\infty \left(\frac{2}{(x + 1)^2} - \frac{2}{(x + 1)^3}\right)dx = \left[-\frac{2}{x + 1} + \frac{1}{(x + 1)^2}\right]_0^\infty = 0 - (-2 + 1) = 1\). [M1] [A1]
(b) \(1 - F(x) = \dfrac{1}{(x + 1)^2}\), and \(\displaystyle\int_0^\infty \frac{dx}{(x + 1)^2} = \left[-\frac{1}{x + 1}\right]_0^\infty = 1\), the same value. [M1] [A1]
(c) \(E(X^2) = \displaystyle\int_0^\infty \frac{2x^2}{(x + 1)^3}\,dx\). For \(x \ge 1\), \(\dfrac{2x^2}{(x + 1)^3} \ge \dfrac{2x^2}{8x^3} = \dfrac{1}{4x}\), and \(\displaystyle\int_1^\infty \dfrac{dx}{4x}\) diverges, so \(E(X^2)\) and \(\mathrm{Var}(X)\) do not exist. [M1] [A1]
:::

:::quiz
? \(X\) has PDF \(f(x) = kx\) for \(0 \le x \le 2\). What is \(F(5)\)?
+ \(1\)
- \(25k\)
- \(0\)
- \(F(5)\) is not defined because \(f(5) = 0\)
> \(F(x)\) is defined for every real \(x\): it is 1 above the top of the range. \(25k\) just substitutes into the formula for the middle piece, and 0 would be right below the range, not above it.
? \(F(x) = \dfrac{x^2}{9}\) for \(0 \le x \le 3\) (0 below, 1 above). What is the median?
+ \(\dfrac{3}{\sqrt{2}} \approx 2.12\)
- \(4.5\)
- \(1.5\)
- \(\dfrac{9}{2\sqrt{2}} \approx 3.18\)
> Solve \(\dfrac{m^2}{9} = \dfrac12\): \(m^2 = 4.5\) and \(m = 2.12\). The value 4.5 forgets the square root, and 1.5 is the middle of the interval, which is not the median unless the PDF is symmetric.
? \(X\) has CDF \(F\). Which is the CDF of \(Y = X^2\), for \(X \ge 0\)?
+ \(G(y) = F(\sqrt{y})\)
- \(G(y) = F(y^2)\)
- \(G(y) = \sqrt{F(y)}\)
- \(G(y) = 1 - F(\sqrt{y})\)
> \(X^2 \le y\) means \(X \le \sqrt{y}\), so \(G(y) = F(\sqrt{y})\). Squaring inside \(F\) goes the wrong way, and \(1 - F\) is for decreasing functions.
? \(X\) has CDF \(F\) on \(x > 0\) and \(Y = \dfrac1X\). What is \(G(y)\) for \(y > 0\)?
+ \(1 - F\!\left(\dfrac1y\right)\)
- \(F\!\left(\dfrac1y\right)\)
- \(\dfrac{1}{F(y)}\)
- \(1 - F(y)\)
> \(\dfrac1X \le y\) means \(X \ge \dfrac1y\) (the inequality reverses for a decreasing function), and \(P(X \ge \tfrac1y) = 1 - F(\tfrac1y)\).
? \(E(X) = 2\) and \(\mathrm{Var}(X) = 3\). What is \(E(X^2)\)?
+ \(7\)
- \(4\)
- \(3\)
- \(1\)
> \(E(X^2) = \mathrm{Var}(X) + (E(X))^2 = 3 + 4 = 7\). The value 4 treats \(E(X^2)\) as \((E(X))^2\), and 3 confuses \(E(X^2)\) with the variance.
? A piecewise PDF is \(f(x) = \dfrac{x}{6}\) on \([0, 2]\) and \(\dfrac13\) on \((2, 4]\). Which is \(F(x)\) for \(2 < x \le 4\)?
+ \(\dfrac13 + \dfrac{x - 2}{3}\)
- \(\dfrac{x - 2}{3}\)
- \(\dfrac{x}{3}\)
- \(\dfrac{x^2}{12} + \dfrac{x}{3}\)
> Each new piece starts from the value of \(F\) at the end of the previous one: \(F(2) = \tfrac13\). The answer \(\tfrac{x - 2}{3}\) forgets that constant, so \(F(4)\) would be \(\tfrac23\), not 1.
:::

:::checklist What you can now do
- [ ] I can use a PDF that is defined piecewise: sketch it, find unknown constants from the total area and continuity, and find probabilities by splitting the integral.
- [ ] I can find \(E(X)\), \(E(X^2)\), \(\mathrm{Var}(X)\), \(E(g(X))\) and the mode of a continuous random variable, including on an infinite range.
- [ ] I can find the CDF from the PDF, giving every interval and starting each piece from the previous value.
- [ ] I can find the PDF from the CDF by differentiating, and use \(F(b) - F(a)\) for probabilities.
- [ ] I can find the median, quartiles and any percentile by solving \(F(x) = p\) in the correct piece.
- [ ] I can find the CDF and PDF of \(Y = h(X)\) for an increasing or a decreasing function, with the range of \(Y\).
- [ ] I can check my answers: areas sum to 1, pieces of \(F\) join, \(F\) reaches 1.
:::

:::recap
- A PDF has \(f \ge 0\) and total area 1; it may be piecewise and need not be continuous. \(P(a < X < b) = \int_a^b f\).
- CDF: \(F(x) = P(X \le x) = \int_{-\infty}^x f\), defined for every \(x\) (0 below the range, 1 above). \(f = F'\). Each piece of \(F\) starts from the previous value.
- Percentiles: solve \(F(x) = p/100\) in the right piece and keep the root inside it. Median \(F(m) = \tfrac12\).
- \(E(g(X)) = \int g(x)f(x)\,dx\); \(\mathrm{Var}(X) = E(X^2) - \mu^2\). \(E(g(X)) \ne g(E(X))\) unless \(g\) is linear. The mode is where \(f\) is greatest.
- For \(Y = h(X)\): \(G(y) = P(h(X) \le y)\), written with \(F\); the inequality reverses for a decreasing \(h\). State the range of \(Y\), then \(g = G'\).
:::

:::links
- watch: [Finding k in a pdf](https://www.examsolutions.net/tutorials/finding-constant-k-in-a-pdf/) · ExamSolutions · total area equals 1
- watch: [Median, quartiles and percentiles from a pdf](https://www.examsolutions.net/tutorials/finding-median-quartiles-percentiles/) · ExamSolutions · areas up to the median
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · free booklets with answers
- explore: [Probability distributions](https://seeing-theory.brown.edu/probability-distributions/index.html) · Seeing Theory · continuous distributions as areas
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [The t-distribution: one-sample tests and intervals](#math.fm.inference) uses the sample mean and variance to test and estimate a mean when the population variance is unknown.
