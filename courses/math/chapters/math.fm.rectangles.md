@chapter math.fm.rectangles
@title Sums, rectangles and bounds
@level fm
@paper CAIE 9231 Paper 2
@time 4–5 hours
@summary A sum and an integral are close relatives: the area under a curve can be approximated by the areas of rectangles, and the total area of the rectangles is a sum. You will use rectangles to bound an integral, to prove inequalities for sums such as \(\ln(n+1) < \sum \frac1r < 1 + \ln n\), to estimate a sum to a given accuracy, and to turn the limit of a sum into an integral.

:::why
Some sums have no formula. There is no neat expression for \(1 + \tfrac12 + \tfrac13 + \dots + \tfrac1n\), yet you can say exactly how fast it grows and where it sits: between two logarithms. The same idea decides whether an infinite series settles down to a value or runs off to infinity, and the reverse idea (a sum of many thin rectangles becomes an integral) is how definite integrals are defined in the first place. This is the bridge between discrete mathematics and calculus.
:::

**Before you start**, you need integration and the area under a curve from [Integration](#math.p1.integ), sigma notation and the standard sums from [Summation of series](#math.fm.series), and logarithmic and reciprocal integrals from [Further integration](#math.p3.integ), where the trapezium rule also appears as a way of estimating an area.

:::try Warm-up
Q: Find \(\displaystyle\int_1^5\frac1x\,dx\). (from [Further integration](#math.p3.integ))
A: \(\left[\ln x\right]_1^5 = \ln 5 - \ln 1 = \ln 5\).
Q: Use the standard formula to find \(\displaystyle\sum_{r=1}^{10}r^2\). (from [Summation of series](#math.fm.series))
A: \(\dfrac{n(n+1)(2n+1)}{6} = \dfrac{10 \times 11 \times 21}{6} = 385\).
Q: Is \(f(x) = \sqrt x\) increasing or decreasing for \(x > 0\)? (from [Differentiation](#math.p1.diff))
A: \(f'(x) = \dfrac{1}{2\sqrt x} > 0\), so \(f\) is increasing.
:::

## Estimating an area with rectangles

To estimate the area under a curve from \(x = a\) to \(x = b\), cut the interval into \(n\) strips of equal width \(h = \dfrac{b-a}{n}\) and draw a rectangle on each strip. The height of the rectangle comes from the curve, either at the left edge of the strip or at the right edge. The total area of the rectangles is the estimate.

:::def Left and right rectangles
On a strip from \(x\) to \(x + h\), the **left rectangle** has height \(f(x)\) and the **right rectangle** has height \(f(x + h)\). The area of a rectangle is height times width, so with unit width (\(h = 1\)) its area is just its height.
:::

Which estimate is too big and which too small depends on whether the curve rises or falls. Look at the strip of a decreasing curve: the curve is highest at the left edge, so the left rectangle sticks out above the curve and the right rectangle fits underneath it.

:::key Upper and lower rectangle sums
- If \(f\) is **decreasing**: left rectangles give an **upper** bound for the area, right rectangles a **lower** bound.
- If \(f\) is **increasing**: left rectangles give a **lower** bound, right rectangles an **upper** bound.
In both cases, (area of the upper rectangles) \(-\) (area of the lower rectangles) \(= h\,|f(b) - f(a)|\), because all the heights cancel except the first and last.
:::

That last line is worth seeing once. Take \(f\) decreasing, with left sum \(h\left[f(a) + f(a+h) + \dots + f(b-h)\right]\) and right sum \(h\left[f(a+h) + \dots + f(b-h) + f(b)\right]\). Subtract: everything cancels except \(h\left[f(a) - f(b)\right]\). So the true area is trapped in a gap of width \(h\left[f(a) - f(b)\right]\), and halving the strip width halves the gap.

:::eg Estimate \(\displaystyle\int_1^3\frac1x\,dx\) using four strips, and say whether each estimate is too big or too small.
The strip width is \(h = \dfrac{3 - 1}{4} = 0.5\), so the edges are \(x = 1, 1.5, 2, 2.5, 3\). Since \(\dfrac1x\) is decreasing:

Left rectangles (upper bound):
\[0.5\left(\frac11 + \frac1{1.5} + \frac12 + \frac1{2.5}\right) = 0.5(1 + 0.6667 + 0.5 + 0.4) = 1.283\]
Right rectangles (lower bound):
\[0.5\left(\frac1{1.5} + \frac12 + \frac1{2.5} + \frac13\right) = 0.5(0.6667 + 0.5 + 0.4 + 0.3333) = 0.950\]
So \(0.950 < \displaystyle\int_1^3\frac1x\,dx < 1.283\). The exact value is \(\ln 3 = 1.0986\), inside the interval.

**Check** the gap: \(h\left[f(1) - f(3)\right] = 0.5\left(1 - \tfrac13\right) = 0.333\), and \(1.283 - 0.950 = 0.333\).
:::

In the widget below, \(y = \dfrac1x\) from \(x = 1\) to \(x = 6\) is filled with strips. Switch between left edge and right edge, then raise the number of strips: the left estimate falls towards \(\ln 6 = 1.792\) from above and the right estimate rises towards it from below. The gap between them is \(h\left(1 - \tfrac16\right)\), so it shrinks in proportion to the strip width.

:::html
<div class="widget" data-w="area" data-f="1/x" data-x="1,6" data-n="5" data-mode="riemann"></div>
:::

## Rectangles of unit width: bounds for sums

Now take strips of width 1 and put the corners on whole numbers. The area of each rectangle is its height, which is a term of a sum. So the sum \(f(1) + f(2) + \dots + f(n)\) is the total area of a row of unit rectangles, and you can compare that area with an integral. The curve \(y = \dfrac1x\) is the model case, because its integral is \(\ln x\).

:::html
<figure class="fig small"><svg viewBox="8 8 312 212" role="img" aria-label="The graph of y equals 1 over x from x equals 1 to x equals 5. Four solid rectangles of width 1 stand on the intervals from 1 to 2, 2 to 3, 3 to 4 and 4 to 5, with heights f(1), f(2), f(3) and f(4), and lie above the curve. Four dashed rectangles with heights f(2), f(3), f(4) and f(5) on the same intervals lie below the curve.">
<rect class="fm s-acc" x="40.0" y="40.0" width="62" height="150.0"/>
<rect class="fm s-acc" x="102.0" y="115.0" width="62" height="75.0"/>
<rect class="fm s-acc" x="164.0" y="140.0" width="62" height="50.0"/>
<rect class="fm s-acc" x="226.0" y="152.5" width="62" height="37.5"/>
<rect class="ln-m thin dash" fill="none" x="40.0" y="115.0" width="62" height="75.0"/>
<rect class="ln-m thin dash" fill="none" x="102.0" y="140.0" width="62" height="50.0"/>
<rect class="ln-m thin dash" fill="none" x="164.0" y="152.5" width="62" height="37.5"/>
<rect class="ln-m thin dash" fill="none" x="226.0" y="160.0" width="62" height="30.0"/>
<line class="ax" x1="30" y1="190" x2="300" y2="190" marker-end="url(#ah)"/>
<line class="ax" x1="40" y1="200" x2="40" y2="22" marker-end="url(#ah)"/>
<path class="c1 sw2" fill="none" d="M40.0 40.0 L50.3 61.4 L60.7 77.5 L71.0 90.0 L81.3 100.0 L91.7 108.2 L102.0 115.0 L112.3 120.8 L122.7 125.7 L133.0 130.0 L143.3 133.8 L153.7 137.1 L164.0 140.0 L174.3 142.6 L184.7 145.0 L195.0 147.1 L205.3 149.1 L215.7 150.9 L226.0 152.5 L236.3 154.0 L246.7 155.4 L257.0 156.7 L267.3 157.9 L277.7 159.0 L288.0 160.0"/>
<text class="ts" x="37" y="205">1</text>
<text class="ts" x="99" y="205">2</text>
<text class="ts" x="161" y="205">3</text>
<text class="ts" x="223" y="205">4</text>
<text class="ts" x="285" y="205">5</text>
<text class="tl" x="296" y="205">x</text>
<text class="tl" x="22" y="20">y</text>
<text class="tl halo" x="44" y="34">f(1)</text>
<text class="tl halo" x="106" y="109">f(2)</text>
<text class="tl halo" x="168" y="134">f(3)</text>
<text class="tl halo" x="230" y="146">f(4)</text>
<text class="tl halo" x="214" y="104">y = 1/x</text>
</svg><figcaption>A decreasing curve, \(f(x) = \dfrac1x\). The solid rectangles with heights \(f(1), \dots, f(4)\) lie above the curve; the dashed rectangles with heights \(f(2), \dots, f(5)\) lie below it. Four rectangles cover the interval from 1 to 5.</figcaption></figure>
:::

Read the figure carefully, because the arguments below all come from it.
- There are **four** rectangles from \(x = 1\) to \(x = 5\): in general \(n - 1\) rectangles from \(x = 1\) to \(x = n\).
- The solid rectangle on \([r, r+1]\) has height \(f(r)\), the value at its left end. Its area is \(\dfrac1r\), and because the curve is falling it lies above the curve.
- The dashed rectangle on \([r, r+1]\) has height \(f(r+1)\) and area \(\dfrac{1}{r+1}\). It lies below the curve.

Writing "the area of the rectangles is more than the area under the curve" as sums and an integral gives an inequality between a sum and a logarithm.

:::eg (Exam style) (a) By considering rectangles of unit width under the curve \(y = \dfrac1x\), show that \(\displaystyle\sum_{r=2}^n\frac1r < \ln n\) for \(n \ge 2\). (b) By considering rectangles of unit width above the curve, show that \(\displaystyle\sum_{r=1}^n\frac1r > \ln(n+1)\). (c) Hence find bounds for \(\displaystyle\sum_{r=1}^{100}\frac1r\), rounding the lower bound down and the upper bound up to 3 s.f.
**(a)** On the interval \([r-1, r]\) take a rectangle of height \(\dfrac1r\) (the value at the right-hand end). Its width is 1, so its area is \(\dfrac1r\). [B1]
Since \(\dfrac1x\) is decreasing, this rectangle lies below the curve, so its area is less than the area under the curve between \(x = r-1\) and \(x = r\). [B1]
Adding the \(n - 1\) rectangles, \(r = 2, 3, \dots, n\), which together cover \([1, n]\):
\[\sum_{r=2}^n\frac1r < \int_1^n\frac1x\,dx\] [M1]
\[\int_1^n\frac1x\,dx = \left[\ln x\right]_1^n = \ln n\] [A1]
**(b)** On the interval \([r, r+1]\) take a rectangle of height \(\dfrac1r\), the value at the left-hand end. It lies above the curve, so its area is more than the area under the curve. [B1]
Adding the \(n\) rectangles for \(r = 1, \dots, n\), which cover \([1, n+1]\):
\[\sum_{r=1}^n\frac1r > \int_1^{n+1}\frac1x\,dx\] [M1]
\[\sum_{r=1}^n\frac1r > \ln(n+1)\] [A1]
**(c)** Add the missing first term to (a): \(\displaystyle\sum_{r=1}^n\frac1r < 1 + \ln n\). Together with (b), for \(n \ge 2\),
\[\ln(n+1) < \sum_{r=1}^n\frac1r < 1 + \ln n\] [B1]
For \(n = 100\): \(\ln 101 = 4.6151\) and \(1 + \ln 100 = 5.6052\). [M1]
\[4.61 < \sum_{r=1}^{100}\frac1r < 5.61\] [A1]
**Check**: the true value is \(5.187\), inside the bounds.
:::

Part (c) shows the habit of the topic: the exact sum is awkward, but two logarithms trap it. The bounds are not close, but they are cheap: they cost one integral. The difference between the sum and \(\ln n\) tends to a number near \(0.5772\) (Euler's constant), but 9231 asks only for the inequalities.

:::warn Wrong side, wrong count
Two slips cost most of the marks in this topic. **Wrong side:** for a decreasing curve the left rectangles are the *upper* ones. Sketch the curve and a rectangle, and look at which corner touches the curve before you write "<" or ">". **Wrong count:** unit rectangles from \(x = 1\) to \(x = n\) number \(n - 1\), not \(n\). The sum is \(\sum_{r=1}^{n-1}f(r)\) (left ends) or \(\sum_{r=2}^nf(r)\) (right ends), and the first or last term is easy to lose. Match the limits of the sum to the limits of the integral: \(n\) rectangles cover \([1, n+1]\).
:::

:::exam The word "considering"
When a question says "by considering the sum of the areas of the rectangles", it expects you to **say** which rectangles (their width, height and the interval they stand on), whether they lie above or below the curve and why (the curve is decreasing), the inequality between the sum and the integral, and the integration. Use a strict inequality (\(<\)) when the rectangles do not fit the curve exactly. Mark schemes credit a clear sketch and a sentence such as "the area of each rectangle is less than the area under the curve, since \(f\) is decreasing".
:::

### How many terms? Estimating a sum to a given size

Because \(\ln(n+1)\) grows without limit, the lower bound shows that \(1 + \tfrac12 + \tfrac13 + \dots\) never settles to a finite value: it **diverges**, though very slowly.

:::eg Use the bounds \(\ln(n+1) < \displaystyle\sum_{r=1}^n\frac1r < 1 + \ln n\) to find a value of \(n\) that guarantees \(\displaystyle\sum_{r=1}^n\frac1r > 10\), and a value below which this is impossible.
**Guaranteed.** It is enough that the lower bound exceeds 10: \(\ln(n+1) \ge 10\) means \(n + 1 \ge e^{10} = 22026.5\), so \(n \ge 22026\) guarantees the sum exceeds 10.

**Impossible.** If the sum exceeds 10, the upper bound must too: \(1 + \ln n > 10\) means \(\ln n > 9\), so \(n > e^9 = 8103.1\). For \(n \le 8103\) the sum cannot exceed 10.

So the smallest such \(n\) lies between 8104 and 22026. (A computer finds that it is 12367.)
:::

## Increasing functions

When \(f\) is increasing the roles swap: now the right rectangles are the upper ones. Take \(f(x) = \sqrt x\) and rectangles on \([r-1, r]\). The curve is highest at the right end, so a rectangle of height \(\sqrt r\) lies above it, and a rectangle of height \(\sqrt{r-1}\) lies below it. Starting at \(x = 0\) makes the integral neat, since \(\displaystyle\int_0^n\sqrt x\,dx = \tfrac23n^{3/2}\).

:::html
<figure class="fig small"><svg viewBox="8 8 312 212" role="img" aria-label="The graph of y equals the square root of x from x equals 0 to x equals 4. Four solid rectangles of width 1 stand on the intervals 0 to 1, 1 to 2, 2 to 3 and 3 to 4 with heights f(1), f(2), f(3) and f(4), and lie above the curve. Three dashed rectangles on the intervals 1 to 2, 2 to 3 and 3 to 4 have heights f(1), f(2) and f(3) and lie below the curve.">
<rect class="fm s-acc" x="40.0" y="120.0" width="62" height="70.0"/>
<rect class="fm s-acc" x="102.0" y="91.0" width="62" height="99.0"/>
<rect class="fm s-acc" x="164.0" y="68.8" width="62" height="121.2"/>
<rect class="fm s-acc" x="226.0" y="50.0" width="62" height="140.0"/>
<rect class="ln-m thin dash" fill="none" x="102.0" y="120.0" width="62" height="70.0"/>
<rect class="ln-m thin dash" fill="none" x="164.0" y="91.0" width="62" height="99.0"/>
<rect class="ln-m thin dash" fill="none" x="226.0" y="68.8" width="62" height="121.2"/>
<line class="ax" x1="30" y1="190" x2="300" y2="190" marker-end="url(#ah)"/>
<line class="ax" x1="40" y1="200" x2="40" y2="22" marker-end="url(#ah)"/>
<path class="c1 sw2" fill="none" d="M40.0 190.0 L50.3 161.4 L60.7 149.6 L71.0 140.5 L81.3 132.8 L91.7 126.1 L102.0 120.0 L112.3 114.4 L122.7 109.2 L133.0 104.3 L143.3 99.6 L153.7 95.2 L164.0 91.0 L174.3 87.0 L184.7 83.1 L195.0 79.3 L205.3 75.7 L215.7 72.2 L226.0 68.8 L236.3 65.4 L246.7 62.2 L257.0 59.0 L267.3 56.0 L277.7 52.9 L288.0 50.0"/>
<text class="ts" x="28" y="205">0</text>
<text class="ts" x="99" y="205">1</text>
<text class="ts" x="161" y="205">2</text>
<text class="ts" x="223" y="205">3</text>
<text class="ts" x="285" y="205">4</text>
<text class="tl" x="296" y="205">x</text>
<text class="tl" x="22" y="20">y</text>
<text class="tl halo" x="48" y="114">f(1)</text>
<text class="tl halo" x="110" y="85">f(2)</text>
<text class="tl halo" x="172" y="63">f(3)</text>
<text class="tl halo" x="234" y="44">f(4)</text>
<text class="tl halo" x="232" y="140">y = √x</text>
</svg><figcaption>An increasing curve, \(f(x) = \sqrt x\). The solid rectangles on \([r-1, r]\) have height \(f(r)\) and lie above the curve; the dashed rectangles have height \(f(r-1)\) and lie below it.</figcaption></figure>
:::

:::eg (Exam style) (a) By considering rectangles of unit width on \([r-1, r]\), show that \(\displaystyle\sum_{r=1}^n\sqrt r > \tfrac23n^{3/2}\). (b) Show that \(\displaystyle\sum_{r=1}^n\sqrt r < \tfrac23n^{3/2} + \sqrt n\). (c) Find the exact bounds for \(n = 100\).
**(a)** The rectangle on \([r-1, r]\) with height \(\sqrt r\) has area \(\sqrt r\). Since \(\sqrt x\) is increasing, this rectangle lies above the curve. [B1]
Adding the rectangles for \(r = 1, \dots, n\), which cover \([0, n]\):
\[\sum_{r=1}^n\sqrt r > \int_0^n\sqrt x\,dx\] [M1]
\[\int_0^n x^{1/2}\,dx = \left[\tfrac23x^{3/2}\right]_0^n = \tfrac23n^{3/2}\] [A1]
**(b)** The rectangle on \([r-1, r]\) with height \(\sqrt{r-1}\) lies below the curve. Adding the rectangles for \(r = 2, \dots, n\) (the one for \(r = 1\) has height 0):
\[\sum_{r=2}^n\sqrt{r-1} < \int_0^n\sqrt x\,dx\] [B1]
The left side is \(\displaystyle\sum_{r=1}^{n-1}\sqrt r\), which is \(\displaystyle\sum_{r=1}^n\sqrt r - \sqrt n\):
\[\sum_{r=1}^n\sqrt r - \sqrt n < \tfrac23n^{3/2}\] [M1]
\[\sum_{r=1}^n\sqrt r < \tfrac23n^{3/2} + \sqrt n\] [A1]
**(c)** With \(n = 100\): \(n^{3/2} = 1000\) and \(\sqrt n = 10\), so
\[\frac{2000}{3} < \sum_{r=1}^{100}\sqrt r < \frac{2030}{3}\] [M1 A1]
**Check**: the bounds are \(666.7\) and \(676.7\), and the true sum is \(671.5\).
:::

The two bounds differ by \(\sqrt n\), a small fraction of the size of the sum when \(n\) is large. Dividing through by \(n^{3/2}\) shows \(\displaystyle\frac{1}{n^{3/2}}\sum_{r=1}^n\sqrt r\) lies between \(\tfrac23\) and \(\tfrac23 + \dfrac{1}{n}\), so it tends to \(\tfrac23\) as \(n \to \infty\).

:::key Method for a bound on \(\displaystyle\sum f(r)\)
1. Sketch \(y = f(x)\) and decide whether \(f\) is increasing or decreasing.
2. Choose the rectangles (on \([r-1, r]\) or on \([r, r+1]\)) so that the sum of their heights is the sum you want, or the sum with one term added or removed.
3. Say whether the rectangles lie above or below the curve, and why.
4. Write the inequality between the sum and \(\displaystyle\int f(x)\,dx\), with limits that match the intervals the rectangles cover.
5. Integrate, then add or take away the term you left out.
:::

## Other sums

The same method works for any function that is increasing throughout the interval or decreasing throughout it. Here are three more, each showing a different use.

### A sum that converges: \(\displaystyle\sum\frac{1}{r^2}\)

The function \(\dfrac{1}{x^2}\) falls quickly, so the sum \(1 + \tfrac14 + \tfrac19 + \dots\) does settle to a value. Rectangles give the value to as many decimal places as you like, by adding up the first few terms exactly and bounding the rest.

:::eg (Exam style) (a) For integers \(N \ge 1\) and \(n > N\), show that
\[\frac{1}{N+1} - \frac{1}{n+1} < \sum_{r=N+1}^n\frac{1}{r^2} < \frac1N - \frac1n\]
(b) Given that \(\displaystyle\sum_{r=1}^{10}\frac{1}{r^2} = 1.549768\) to 6 decimal places, use \(N = 10\) and let \(n \to \infty\) to show that the sum to infinity lies between 1.64 and 1.65.
**(a)** The function \(\dfrac{1}{x^2}\) is decreasing. A rectangle on \([r-1, r]\) with height \(\dfrac{1}{r^2}\) lies below the curve; adding the rectangles for \(r = N+1, \dots, n\), which cover \([N, n]\): [B1]
\[\sum_{r=N+1}^n\frac{1}{r^2} < \int_N^n\frac{1}{x^2}\,dx = \left[-\frac1x\right]_N^n = \frac1N - \frac1n\] [M1 A1]
A rectangle on \([r, r+1]\) with height \(\dfrac{1}{r^2}\) lies above the curve; adding those for \(r = N+1, \dots, n\), which cover \([N+1, n+1]\): [B1]
\[\sum_{r=N+1}^n\frac{1}{r^2} > \int_{N+1}^{n+1}\frac{1}{x^2}\,dx = \frac{1}{N+1} - \frac{1}{n+1}\] [M1 A1]
**(b)** Take \(N = 10\). As \(n \to \infty\), both \(\dfrac1n\) and \(\dfrac{1}{n+1}\) tend to 0, so the tail \(\displaystyle\sum_{r=11}^\infty\frac{1}{r^2}\) satisfies
\[\frac{1}{11} \le \text{tail} \le \frac{1}{10}\] [M1]
Add the first ten terms: \(1.549768 + 0.090909 = 1.640677\) and \(1.549768 + 0.1 = 1.649768\). [A1]
\[1.64 < \sum_{r=1}^\infty\frac{1}{r^2} < 1.65\] [A1]
**Check**: the sum to infinity is \(\dfrac{\pi^2}{6} = 1.6449\), inside the bounds.
:::

A small \(N\) gives a neat bound. With \(N = 1\) the upper bound says \(\sum_{r=2}^n\dfrac{1}{r^2} < 1 - \dfrac1n\), so \(\sum_{r=1}^n\dfrac{1}{r^2} < 2 - \dfrac1n < 2\) for every \(n\). A sum of positive terms that never passes 2 must converge: the partial sums keep increasing (each new term is positive) and never pass 2, so they must settle to a limit (accept this as a fact).

To reach a stated accuracy, notice the width of the bracket: it is \(\dfrac1N - \dfrac{1}{N+1} = \dfrac{1}{N(N+1)}\), which is below 0.001 as soon as \(N \ge 32\), so the tail is pinned to within 0.001 after 32 exact terms.

### A sum of a quickly changing function: \(\displaystyle\sum e^{-r}\)

:::eg Use rectangles to find bounds for \(\displaystyle\sum_{r=1}^5e^{-r}\), and compare them with the exact sum of the geometric series.
The function \(e^{-x}\) is decreasing. Rectangles on \([r-1, r]\) with height \(e^{-r}\) lie below the curve and cover \([0, 5]\):
\[\sum_{r=1}^5e^{-r} < \int_0^5e^{-x}\,dx = 1 - e^{-5} = 0.993\]
Rectangles on \([r, r+1]\) with height \(e^{-r}\) lie above the curve and cover \([1, 6]\):
\[\sum_{r=1}^5e^{-r} > \int_1^6e^{-x}\,dx = e^{-1} - e^{-6} = 0.365\]
So \(0.365 < \displaystyle\sum_{r=1}^5e^{-r} < 0.993\).

The sum is a geometric series with first term \(e^{-1}\) and ratio \(e^{-1}\): \(\displaystyle\frac{e^{-1}\left(1 - e^{-5}\right)}{1 - e^{-1}} = \frac{1 - e^{-5}}{e - 1} = 0.578\), well inside the bounds.
:::

The gap is wide because \(e^{-x}\) falls by a factor of 2.7 across each strip, far too fast for unit-width rectangles. The lesson: rectangles are the tool for sums with **no** formula. When a series is geometric or arithmetic, or the method of differences works, use the exact sum.

### Sums of logarithms

For an increasing function such as \(\ln x\), the right rectangles are the upper ones. The sum \(\displaystyle\sum_{r=1}^n\ln r\) is \(\ln(n!)\), because \(\ln 1 + \ln 2 + \dots + \ln n = \ln(1 \times 2 \times \dots \times n)\). Bounding it gives a size for \(n!\). You will do this in the exam practice.

## Sums as integrals: strips whose width tends to zero

So far the strips have had width 1. Now let the number of strips \(n\) tend to infinity while the interval stays fixed. Divide \([0, 1]\) into \(n\) strips of width \(\dfrac1n\) with edges \(\dfrac rn\) for \(r = 0, 1, \dots, n\). The right rectangle on the \(r\)th strip has height \(f\left(\dfrac rn\right)\) and width \(\dfrac1n\), so the right-hand sum is
\[\frac1n\sum_{r=1}^nf\left(\frac rn\right)\]
As \(n \to \infty\) the strips become thinner, the rectangles fit the curve more closely, and the sum tends to the area.

:::key Limit of a sum as an integral
For a function \(f\) that is continuous on \([0, 1]\),
\[\lim_{n\to\infty}\frac1n\sum_{r=1}^nf\left(\frac rn\right) = \int_0^1f(x)\,dx\]
More generally, strips of width \(h = \dfrac{b-a}{n}\) give \(\displaystyle\lim_{n\to\infty}h\sum_{r=1}^nf(a + rh) = \int_a^bf(x)\,dx\). To use it, **write the term as \(\dfrac1n \times f\left(\dfrac rn\right)\)**, spot \(f\), read off the limits from the smallest and largest value of \(\dfrac rn\), and integrate.
:::

:::proof Why the limit is the integral
For an increasing \(f\), the right-hand sum \(R_n\) is an upper bound and the left-hand sum \(L_n = \dfrac1n\sum_{r=0}^{n-1}f\left(\dfrac rn\right)\) is a lower bound for the integral:
\[L_n \le \int_0^1f(x)\,dx \le R_n\]
Subtract: all terms cancel except the last of \(R_n\) and the first of \(L_n\), so
\[R_n - L_n = \frac1n\left[f(1) - f(0)\right]\]
This tends to 0 as \(n \to \infty\). The integral is trapped between two sums whose difference tends to 0, so each sum tends to the integral. (For \(f(x) = x^2\) and \(n = 10\): \(R_{10} = 0.385\), \(L_{10} = 0.285\), and the difference is \(0.1 = \tfrac{1}{10}(1 - 0)\).)
:::

An exam question often asks for this argument in closed form: the two sums are worked out with the formula for \(\sum r^2\), and the difference is shown to tend to 0.

:::eg (Exam style) The region under \(y = 1 + x^2\) for \(0 \le x \le 1\) is divided into \(n\) strips of width \(\dfrac1n\). (a) By considering the rectangles that lie above the curve, show that \(\displaystyle\int_0^1\left(1 + x^2\right)dx < U_n = 1 + \dfrac{(n+1)(2n+1)}{6n^2}\). (b) By considering the rectangles that lie below the curve, show that the integral is greater than \(L_n = 1 + \dfrac{(n-1)(2n-1)}{6n^2}\). (c) Show that \(U_n - L_n = \dfrac1n\), and hence find the value of the integral.
**(a)** The function is increasing on \([0, 1]\), so on the \(r\)th strip, from \(\dfrac{r-1}{n}\) to \(\dfrac rn\), the highest point of the curve is at the right-hand end. A rectangle of height \(f\left(\dfrac rn\right) = 1 + \dfrac{r^2}{n^2}\) and width \(\dfrac1n\) therefore lies above the curve. [B1]
\[\int_0^1\left(1 + x^2\right)dx < U_n = \frac1n\sum_{r=1}^n\left(1 + \frac{r^2}{n^2}\right) = \frac1n \times n + \frac{1}{n^3}\sum_{r=1}^nr^2\] [M1 A1]
Use \(\displaystyle\sum_{r=1}^nr^2 = \frac{n(n+1)(2n+1)}{6}\):
\[U_n = 1 + \frac{n(n+1)(2n+1)}{6n^3} = 1 + \frac{(n+1)(2n+1)}{6n^2}\] [A1]
**(b)** The lowest point on the \(r\)th strip is at the left-hand end, where the height is \(f\left(\dfrac{r-1}{n}\right) = 1 + \dfrac{(r-1)^2}{n^2}\), so these rectangles lie below the curve: [B1]
\[L_n = \frac1n\sum_{r=1}^n\left(1 + \frac{(r-1)^2}{n^2}\right) = 1 + \frac{1}{n^3}\sum_{s=0}^{n-1}s^2\] [M1]
where \(s = r - 1\). The sum runs to \(n - 1\), so the formula is used with \(n - 1\) in place of \(n\): \(\displaystyle\sum_{s=1}^{n-1}s^2 = \frac{(n-1)n(2n-1)}{6}\). [M1]
\[L_n = 1 + \frac{(n-1)n(2n-1)}{6n^3} = 1 + \frac{(n-1)(2n-1)}{6n^2}\] [A1]
**(c)** Expand the two brackets: \((n+1)(2n+1) = 2n^2 + 3n + 1\) and \((n-1)(2n-1) = 2n^2 - 3n + 1\). So
\[U_n - L_n = \frac{\left(2n^2 + 3n + 1\right) - \left(2n^2 - 3n + 1\right)}{6n^2} = \frac{6n}{6n^2} = \frac1n\] [M1]
As \(n \to \infty\), \(U_n - L_n \to 0\), and \(U_n \to 1 + \dfrac{2}{6} = \dfrac43\). The integral lies between \(L_n\) and \(U_n\), which both tend to \(\dfrac43\), so \(\displaystyle\int_0^1\left(1 + x^2\right)dx = \dfrac43\). [A1]
**Check** with \(n = 10\): \(U_{10} = 1 + \dfrac{11 \times 21}{600} = 1.385\) and \(L_{10} = 1 + \dfrac{9 \times 19}{600} = 1.285\). The difference is \(0.1 = \dfrac1{10}\), and \(\dfrac43 = 1.333\) lies between them. Direct integration gives \(\left[x + \dfrac{x^3}{3}\right]_0^1 = \dfrac43\).
:::

:::eg Find \(\displaystyle\lim_{n\to\infty}\frac{1}{n^3}\sum_{r=1}^nr^2\), (a) as an integral and (b) using the formula for \(\sum r^2\).
**(a)** Write \(\dfrac{r^2}{n^3} = \dfrac1n \times \left(\dfrac rn\right)^2\), so \(f(x) = x^2\). The values of \(\dfrac rn\) run from \(\dfrac1n \to 0\) up to 1:
\[\lim_{n\to\infty}\frac1n\sum_{r=1}^n\left(\frac rn\right)^2 = \int_0^1x^2\,dx = \frac13\]
**(b)** \(\displaystyle\sum_{r=1}^nr^2 = \frac{n(n+1)(2n+1)}{6}\), so
\[\frac{1}{n^3}\sum_{r=1}^nr^2 = \frac{(n+1)(2n+1)}{6n^2} = \frac16\left(1 + \frac1n\right)\left(2 + \frac1n\right) \to \frac{2}{6} = \frac13\]
The two methods agree. Method (a) is the only one that works when there is no formula for the sum.
:::

The skill is in the rewriting. In an exam the sum is usually given in a form that is *almost* \(\dfrac1n\sum f\left(\dfrac rn\right)\), and you divide top and bottom by a power of \(n\).

:::eg (Exam style) Find the exact value of (a) \(\displaystyle\lim_{n\to\infty}\sum_{r=1}^n\frac{1}{n+r}\), (b) \(\displaystyle\lim_{n\to\infty}\sum_{r=1}^n\frac{n}{n^2 + r^2}\).
**(a)** Divide the numerator and denominator by \(n\):
\[\frac{1}{n+r} = \frac1n \times \frac{1}{1 + \frac rn}\] [M1]
So \(f(x) = \dfrac{1}{1+x}\), and \(\dfrac rn\) runs from near 0 to 1. [A1]
\[\lim_{n\to\infty}\sum_{r=1}^n\frac{1}{n+r} = \int_0^1\frac{1}{1+x}\,dx = \left[\ln(1+x)\right]_0^1\] [M1]
\[= \ln 2\] [A1]
**(b)** Divide the numerator and denominator by \(n^2\):
\[\frac{n}{n^2 + r^2} = \frac1n \times \frac{1}{1 + \left(\frac rn\right)^2}\] [M1]
So \(f(x) = \dfrac{1}{1 + x^2}\) and the limits are 0 and 1. [A1]
\[\int_0^1\frac{1}{1+x^2}\,dx = \left[\tan^{-1}x\right]_0^1\] [M1]
\[= \frac\pi4\] [A1]
**Check** with \(n = 100\): the sums are \(0.6907\) and \(0.7829\), close to \(\ln 2 = 0.6931\) and \(\tfrac\pi4 = 0.7854\). The error is about \(\dfrac{1}{2n}\) times the change in \(f\).
:::

When the sum runs from \(r = 1\) to \(2n\), the largest value of \(\dfrac rn\) is 2, and the limits become 0 and 2. When it runs from \(r = n+1\) to \(2n\) (for example \(\sum_{r=n+1}^{2n}\dfrac1r\)), change the index: put \(r = n + s\) with \(s = 1, \dots, n\), then \(\dfrac1r = \dfrac1n \times \dfrac{1}{1 + s/n}\), which is part (a) again. The answer \(\ln 2\) says that \(\dfrac1{n+1} + \dots + \dfrac1{2n}\) tends to \(\ln 2\): in the language of the earlier section, write \(H_n = 1 + \tfrac12 + \dots + \dfrac1n\) (the sum of the first \(n\) terms of \(\dfrac1r\)), and then \(H_{2n} - H_n \to \ln 2\).

:::eg Find \(\displaystyle\lim_{n\to\infty}\frac1n\sum_{r=1}^{2n}\frac rn\).
Here \(\dfrac rn\) runs from near 0 up to \(\dfrac{2n}{n} = 2\), so the limits of the integral are 0 and 2, and \(f(x) = x\):
\[\lim_{n\to\infty}\frac1n\sum_{r=1}^{2n}\frac rn = \int_0^2x\,dx = 2\]
**Check** exactly: \(\dfrac{1}{n^2}\sum_{r=1}^{2n}r = \dfrac{1}{n^2} \times \dfrac{2n(2n+1)}{2} = \dfrac{2n+1}{n} = 2 + \dfrac1n \to 2\).
:::

:::board
This chapter follows the Cambridge 9231 syllabus (outcome 2.4c). In 9231 you may be given a diagram of the rectangles or asked to draw your own; either way, say which rectangles you use and which side of the curve they lie on. If you study another board's Further Maths, check its content list before relying on this chapter.
:::

:::eg Spot the error: Show that \(\displaystyle\sum_{r=1}^n\frac1r > \ln(n+1)\) [4 marks].
A student wrote this answer.

Line 1: "Take rectangles of width 1 on \([r, r+1]\) with height \(\dfrac1r\), so the area of each is \(\dfrac1r\)."
Line 2: "\(\dfrac1x\) is decreasing, so each rectangle lies above the curve."
Line 3: "So the sum of the \(n\) rectangle areas is more than \(\displaystyle\int_1^n\frac1x\,dx\)."
Line 4: "\(\displaystyle\int_1^n\frac1x\,dx = \ln n\), so \(\displaystyle\sum_{r=1}^n\frac1r > \ln n\), which is the result."

Lines 1 and 2 describe the right rectangles and the right side of the curve. [B1] [B1]

Line 3 uses the right method, comparing the sum of the areas with an integral, so it keeps the method mark. [M1]

**Line 3 has the slip, and line 4 loses the accuracy mark.** The \(n\) rectangles on \([1, 2], [2, 3], \dots, [n, n+1]\) cover the interval from 1 to \(n+1\), not from 1 to \(n\). The integral should be \(\displaystyle\int_1^{n+1}\frac1x\,dx = \ln(n+1)\). The student's \(\ln n\) is a weaker result, not the printed one, and "which is the result" is false: \(\ln n < \ln(n+1)\). [A0] The student scores 3 out of 4.

Correct line 4: \(\displaystyle\sum_{r=1}^n\frac1r > \int_1^{n+1}\frac1x\,dx = \ln(n+1)\). [A1]

**Check** with \(n = 1\): the claim is \(1 > \ln 2 = 0.693\), true. The student's version, \(1 > \ln 1 = 0\), is true too but too weak.
:::

:::try Start easy, finish at exam standard
Q: Use four rectangles of equal width to find a lower and an upper bound for \(\displaystyle\int_0^2e^{-x}\,dx\).
A: The width is 0.5, and \(e^{-x}\) is decreasing. Left rectangles (upper): \(0.5\left(1 + e^{-0.5} + e^{-1} + e^{-1.5}\right) = 1.0988\). Right rectangles (lower): \(0.5\left(e^{-0.5} + e^{-1} + e^{-1.5} + e^{-2}\right)\), and the bracket is \(0.6065 + 0.3679 + 0.2231 + 0.1353 = 1.3328\), so the sum is \(0.6664\). So \(0.666 < \displaystyle\int_0^2e^{-x}\,dx < 1.10\); the exact value is \(1 - e^{-2} = 0.865\).
Q: Write down the sum of the heights of the unit rectangles on \([1, 2], [2, 3], \dots, [9, 10]\) with left-hand heights for \(y = \dfrac{1}{x^2}\), using sigma notation. Is it more or less than \(\displaystyle\int_1^{10}\frac{1}{x^2}\,dx\)?
A: \(\displaystyle\sum_{r=1}^9\frac{1}{r^2}\). The curve is decreasing, so the left rectangles lie above it: the sum is **more** than \(\displaystyle\int_1^{10}\frac{1}{x^2}\,dx = 0.9\).
Q: Show that \(\displaystyle\sum_{r=2}^n\frac{1}{r^3} < \frac12 - \frac{1}{2n^2}\).
A: Rectangles on \([r-1, r]\) with height \(\dfrac{1}{r^3}\) lie below the decreasing curve \(y = \dfrac{1}{x^3}\), so the sum is less than \(\displaystyle\int_1^nx^{-3}\,dx = \left[-\dfrac{1}{2x^2}\right]_1^n = \dfrac12 - \dfrac{1}{2n^2}\).
Q: Find \(\displaystyle\lim_{n\to\infty}\frac1n\sum_{r=1}^n\left(\frac rn\right)^3\).
A: \(f(x) = x^3\) on \([0, 1]\): \(\displaystyle\int_0^1x^3\,dx = \frac14\).
Q: Find \(\displaystyle\lim_{n\to\infty}\sum_{r=1}^n\frac{n}{(n+r)^2}\).
A: \(\dfrac{n}{(n+r)^2} = \dfrac1n \times \dfrac{1}{\left(1 + \frac rn\right)^2}\), so the limit is \(\displaystyle\int_0^1\frac{1}{(1+x)^2}\,dx = \left[-\frac{1}{1+x}\right]_0^1 = \frac12\).
Q: The curve \(y = \ln x\) is increasing. Which rectangles, left or right, give an upper bound for \(\displaystyle\int_1^6\ln x\,dx\) with unit strips, and what is the bound?
A: The right rectangles: heights \(\ln 2, \ln 3, \dots, \ln 6\), so the bound is \(\ln 2 + \ln 3 + \dots + \ln 6 = \ln 720 = 6.58\). (The exact value is \(6\ln 6 - 5 = 5.75\).)
Q: Use the bounds for \(\displaystyle\sum\frac1r\) to show that \(\displaystyle\sum_{r=1}^{1000}\frac1r < 8\).
A: \(\displaystyle\sum_{r=1}^{1000}\frac1r < 1 + \ln 1000 = 1 + 6.908 = 7.908 < 8\).
Q: Show that \(\displaystyle\lim_{n\to\infty}\frac{1}{n^{3/2}}\sum_{r=1}^n\sqrt r = \frac23\) by writing it as an integral.
A: \(\dfrac{\sqrt r}{n^{3/2}} = \dfrac1n\sqrt{\dfrac rn}\), so the limit is \(\displaystyle\int_0^1\sqrt x\,dx = \tfrac23\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Use rectangles of width 0.5 to find a lower bound and an upper bound for \(\displaystyle\int_0^2x^2\,dx\).
A: \(x^2\) is increasing, so left rectangles give the lower bound: \(0.5\left(0^2 + 0.5^2 + 1^2 + 1.5^2\right)\) [M1] \(= 1.75\). [A1]
Right rectangles give the upper bound: \(0.5\left(0.5^2 + 1^2 + 1.5^2 + 2^2\right) = 3.75\). [A1]
Q: [5 marks] ★★ By considering rectangles of unit width, show that \(2\sqrt{n+1} - 2 < \displaystyle\sum_{r=1}^n\frac{1}{\sqrt r} < 2\sqrt n - 1\) for \(n \ge 2\).
A: \(y = x^{-1/2}\) is decreasing. A rectangle on \([r, r+1]\) of height \(\dfrac{1}{\sqrt r}\) lies above the curve. [B1]
Adding for \(r = 1, \dots, n\): \(\displaystyle\sum_{r=1}^n\frac{1}{\sqrt r} > \int_1^{n+1}x^{-1/2}\,dx\) [M1] \(= \left[2\sqrt x\right]_1^{n+1} = 2\sqrt{n+1} - 2\). [A1]
A rectangle on \([r-1, r]\) of height \(\dfrac{1}{\sqrt r}\) lies below the curve; adding for \(r = 2, \dots, n\): \(\displaystyle\sum_{r=2}^n\frac{1}{\sqrt r} < \int_1^nx^{-1/2}\,dx = 2\sqrt n - 2\). [M1]
Adding the term \(r = 1\), which is 1: \(\displaystyle\sum_{r=1}^n\frac{1}{\sqrt r} < 2\sqrt n - 1\). [A1]
Q: [6 marks] ★★ (a) Show that \(\displaystyle\int_1^n\ln x\,dx = n\ln n - n + 1\). (b) By considering rectangles of unit width, show that \(n\ln n - n + 1 < \ln(n!) < (n+1)\ln n - n + 1\) for \(n \ge 2\).
A: (a) By parts, \(u = \ln x\), \(\dfrac{dv}{dx} = 1\): \(\left[x\ln x\right]_1^n - \displaystyle\int_1^n1\,dx\) [M1] \(= n\ln n - (n - 1)\). [A1]
(b) \(\ln x\) is increasing. Rectangles on \([r-1, r]\) of height \(\ln r\) lie above the curve; for \(r = 2, \dots, n\) they cover \([1, n]\): \(\displaystyle\sum_{r=2}^n\ln r > \int_1^n\ln x\,dx\). [B1]
Since \(\displaystyle\sum_{r=2}^n\ln r = \ln(n!)\), this gives \(\ln(n!) > n\ln n - n + 1\). [A1]
Rectangles on \([r, r+1]\) of height \(\ln r\) lie below the curve; for \(r = 1, \dots, n-1\): \(\displaystyle\sum_{r=1}^{n-1}\ln r < \int_1^n\ln x\,dx\), that is \(\ln(n!) - \ln n < n\ln n - n + 1\). [M1]
So \(\ln(n!) < (n+1)\ln n - n + 1\). [A1]
Q: [4 marks] ★★ Find the exact value of \(\displaystyle\lim_{n\to\infty}\frac1n\sum_{r=1}^n\sqrt{1 + \frac{3r}{n}}\).
A: With \(x = \dfrac rn\), \(f(x) = \sqrt{1 + 3x}\), and the limits are 0 and 1. [M1 A1]
\[\int_0^1(1 + 3x)^{1/2}\,dx = \left[\tfrac29(1 + 3x)^{3/2}\right]_0^1\] [M1]
\[= \tfrac29(8 - 1) = \frac{14}{9}\] [A1]
Q: [5 marks] ★★ Find the exact value of \(\displaystyle\lim_{n\to\infty}\sum_{r=1}^n\frac{1}{n + 2r}\).
A: \(\dfrac{1}{n + 2r} = \dfrac1n \times \dfrac{1}{1 + 2\frac rn}\). [M1]
So \(f(x) = \dfrac{1}{1 + 2x}\). [A1] The limits are 0 and 1. [B1]
\[\int_0^1\frac{1}{1 + 2x}\,dx = \left[\tfrac12\ln(1 + 2x)\right]_0^1\] [M1]
\[= \tfrac12\ln 3\] [A1]
Q: [10 marks] (#math.fm.series) ★★★ (a) By considering rectangles of unit width, show that \(\dfrac{n^3}{3} < \displaystyle\sum_{r=1}^nr^2 < \dfrac{n^3}{3} + n^2\). (b) Use the standard formula for \(\displaystyle\sum r^2\) to show that the exact sum lies between these bounds. (c) Hence find the limit of \(\dfrac{1}{n^3}\displaystyle\sum_{r=1}^nr^2\) as \(n \to \infty\).
H: In (a) use the increasing curve \(y = x^2\) from \(x = 0\) to \(x = n\), with rectangles on \([r-1, r]\) of height \(r^2\) (above) and \((r-1)^2\) (below).
H: The sum of the lower rectangles is \(\displaystyle\sum_{r=1}^{n-1}r^2 = \displaystyle\sum_{r=1}^nr^2 - n^2\).
H: In (b), expand \(\dfrac{n(n+1)(2n+1)}{6}\) and subtract \(\dfrac{n^3}{3}\).
A: (a) Rectangles on \([r-1, r]\) with height \(r^2\) lie above the increasing curve. [B1]
\(\displaystyle\sum_{r=1}^nr^2 > \int_0^nx^2\,dx = \dfrac{n^3}{3}\). [M1 A1]
Rectangles on \([r-1, r]\) with height \((r-1)^2\) lie below the curve: \(\displaystyle\sum_{r=1}^{n-1}r^2 < \dfrac{n^3}{3}\), so \(\displaystyle\sum_{r=1}^nr^2 - n^2 < \dfrac{n^3}{3}\). [M1]
\(\displaystyle\sum_{r=1}^nr^2 < \dfrac{n^3}{3} + n^2\). [A1]
(b) \(\dfrac{n(n+1)(2n+1)}{6} = \dfrac{n^3}{3} + \dfrac{n^2}{2} + \dfrac n6\). [B1]
The excess over \(\dfrac{n^3}{3}\) is \(\dfrac{n^2}{2} + \dfrac n6\) [M1], which is positive and less than \(n^2\) for \(n \ge 1\) (since \(\dfrac n6 < \dfrac{n^2}{2}\)). So the exact sum lies between the bounds. [A1]
(c) Divide the inequality by \(n^3\): \(\dfrac13 < \dfrac{1}{n^3}\displaystyle\sum r^2 < \dfrac13 + \dfrac1n\). [M1]
As \(n \to \infty\), \(\dfrac1n \to 0\), so the limit is \(\dfrac13\). [A1]
Q: [11 marks] (#math.p3.integ) ★★★ (a) By considering rectangles of unit width on the curve \(y = \dfrac{1}{2x+1}\), show that \(\tfrac12\ln\dfrac{2n+3}{3} < \displaystyle\sum_{r=1}^n\frac{1}{2r+1} < \dfrac13 + \tfrac12\ln\dfrac{2n+1}{3}\) for \(n \ge 2\). (b) Evaluate both bounds for \(n = 40\) to 3 significant figures. (c) Find the smallest integer \(n\) for which the lower bound exceeds 3.
H: The curve is decreasing: rectangles on \([r, r+1]\) of height \(\dfrac{1}{2r+1}\) lie above it and cover \([1, n+1]\).
H: Rectangles on \([r-1, r]\) of height \(\dfrac{1}{2r+1}\) lie below it and cover \([1, n]\) when \(r = 2, \dots, n\); the term \(r = 1\) is \(\dfrac13\).
H: \(\displaystyle\int\frac{1}{2x+1}\,dx = \tfrac12\ln(2x+1)\). For (c), solve \(\tfrac12\ln\dfrac{2n+3}{3} > 3\).
A: (a) Above the curve: \(\displaystyle\sum_{r=1}^n\frac{1}{2r+1} > \int_1^{n+1}\frac{1}{2x+1}\,dx\) [B1 M1] \(= \left[\tfrac12\ln(2x+1)\right]_1^{n+1} = \tfrac12\ln\dfrac{2n+3}{3}\). [A1]
Below the curve: \(\displaystyle\sum_{r=2}^n\frac{1}{2r+1} < \int_1^n\frac{1}{2x+1}\,dx = \tfrac12\ln\dfrac{2n+1}{3}\). [B1 M1]
Add the first term \(\dfrac13\): \(\displaystyle\sum_{r=1}^n\frac{1}{2r+1} < \dfrac13 + \tfrac12\ln\dfrac{2n+1}{3}\). [A1]
(b) Lower: \(\tfrac12\ln\dfrac{83}{3} = 1.66\). Upper: \(\dfrac13 + \tfrac12\ln\dfrac{81}{3} = 1.98\). [B1 B1]
(The true sum is \(1.84\).)
(c) \(\tfrac12\ln\dfrac{2n+3}{3} > 3\) means \(\dfrac{2n+3}{3} > e^6 = 403.43\) [M1], so \(2n + 3 > 1210.3\) and \(n > 603.6\). [A1]
The smallest integer is \(n = 604\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ Let \(d_n = \displaystyle\sum_{r=1}^n\frac1r - \ln n\) for \(n \ge 1\). (a) Show that \(d_n - d_{n+1} = \ln\dfrac{n+1}{n} - \dfrac{1}{n+1}\). (b) By considering a rectangle on \([n, n+1]\) under \(y = \dfrac1x\), show that \(d_n - d_{n+1} > 0\). (c) Show that \(d_n > 0\) for all \(n\). (d) Deduce that \(d_n\) tends to a limit between 0 and 1.
H: Write out \(d_{n+1}\): it has one more term of the sum, and \(\ln(n+1)\) in place of \(\ln n\).
H: The rectangle on \([n, n+1]\) with height \(\dfrac{1}{n+1}\) lies below the curve, so its area \(\dfrac{1}{n+1}\) is less than \(\displaystyle\int_n^{n+1}\frac1x\,dx\).
H: A sequence that keeps decreasing but stays positive cannot fall below 0, so it settles to a limit.
A: (a) Write out both terms:
\[d_n - d_{n+1} = \left(H_n - \ln n\right) - \left(H_{n+1} - \ln(n+1)\right)\] [M1]
where \(H_n = \displaystyle\sum_{r=1}^n\frac1r\) and \(H_{n+1} = H_n + \dfrac{1}{n+1}\). So \(d_n - d_{n+1} = \ln(n+1) - \ln n - \dfrac{1}{n+1} = \ln\dfrac{n+1}{n} - \dfrac{1}{n+1}\). [A1]
(b) The rectangle on \([n, n+1]\) with height \(\dfrac{1}{n+1}\) has area \(\dfrac{1}{n+1}\) and lies below the decreasing curve, so \(\dfrac{1}{n+1} < \displaystyle\int_n^{n+1}\frac1x\,dx = \ln\dfrac{n+1}{n}\). [B1] Hence \(d_n - d_{n+1} > 0\). [A1]
(c) From the unit-rectangle bound \(\displaystyle\sum_{r=1}^n\frac1r > \ln(n+1) > \ln n\), so \(d_n > 0\). [M1 A1]
(d) The sequence is decreasing (by (b)) and bounded below by 0 (by (c)), so it converges to a limit \(L \ge 0\). [B1] Since \(d_1 = 1\) and the sequence is decreasing, \(L < 1\). [B1]
(The limit is Euler's constant, \(0.5772\ldots\)).
Q: [6 marks] ★★★ Use the bounds \(\ln(n+1) < \displaystyle\sum_{r=1}^n\frac1r < 1 + \ln n\) to show that the least \(n\) for which \(\displaystyle\sum_{r=1}^n\frac1r > 5\) satisfies \(55 \le n \le 148\).
H: If the sum exceeds 5, the upper bound must exceed 5 too.
H: If the lower bound is at least 5, the sum certainly exceeds 5.
A: Suppose \(\displaystyle\sum_{r=1}^n\frac1r > 5\). Then \(1 + \ln n > 5\) [M1], so \(\ln n > 4\) and \(n > e^4 = 54.6\), giving \(n \ge 55\). [A1 A1]
If \(\ln(n+1) \ge 5\), then the sum exceeds 5. [M1] This holds when \(n + 1 \ge e^5 = 148.4\), that is for \(n \ge 148\). [A1]
So the least \(n\) is at most 148. Together, \(55 \le n \le 148\). [A1]
(A computer finds that the least \(n\) is 83.)
:::

:::quiz
? The curve \(y = f(x)\) is decreasing. Unit rectangles on \([r, r+1]\) have height \(f(r)\). How does their total area compare with \(\displaystyle\int_1^{n}f(x)\,dx\) for \(r = 1, \dots, n-1\)?
+ It is greater: the rectangles lie above the curve
- It is less: the rectangles lie below the curve
- It is equal when \(n\) is large
- It depends on the value of \(f(1)\)
> A decreasing curve is highest at the left end of each strip, so a rectangle whose height is the left-end value sticks out above the curve. The opposite (less) belongs to right-end heights, or to an increasing curve with left-end heights.
? Unit rectangles on \([r, r+1]\) for \(r = 1, \dots, n\) have height \(\dfrac1r\). Which integral does their total area compare with?
+ \(\displaystyle\int_1^{n+1}\frac1x\,dx\)
- \(\displaystyle\int_1^{n}\frac1x\,dx\)
- \(\displaystyle\int_0^{n}\frac1x\,dx\)
- \(\displaystyle\int_1^{n+2}\frac1x\,dx\)
> There are \(n\) rectangles and each has width 1, starting at \(x = 1\), so they end at \(x = n + 1\). Using \(n\) as the upper limit is the "wrong count" slip, and \(\displaystyle\int_0^n\) fails because \(\dfrac1x\) is undefined at 0.
? How many unit-width rectangles stand between \(x = 1\) and \(x = n\)?
+ \(n - 1\)
- \(n\)
- \(n + 1\)
- \(n - 2\)
> The width of the interval is \(n - 1\) and each rectangle has width 1. This is why the right-end sum runs from \(r = 2\) to \(n\), and the left-end sum from \(r = 1\) to \(n - 1\).
? What is \(\displaystyle\lim_{n\to\infty}\frac1n\sum_{r=1}^nf\left(\dfrac rn\right)\)?
+ \(\displaystyle\int_0^1f(x)\,dx\)
- \(\displaystyle\int_1^nf(x)\,dx\)
- \(\displaystyle\int_0^nf(x)\,dx\)
- \(0\), because \(\dfrac1n \to 0\)
> The values \(\dfrac rn\) run from near 0 to 1, so the limits are 0 and 1. The factor \(\dfrac1n\) tends to 0 but it multiplies a sum of \(n\) terms that grows, and their product is the area.
? What is \(\displaystyle\lim_{n\to\infty}\sum_{r=1}^n\frac{1}{n+r}\)?
+ \(\ln 2\)
- \(0\)
- \(1\)
- \(\infty\)
> Writing \(\dfrac{1}{n+r} = \dfrac1n \times \dfrac{1}{1 + r/n}\) gives \(\displaystyle\int_0^1\dfrac{1}{1+x}\,dx = \ln 2\). Each term tends to 0 but there are \(n\) of them, so the limit is not 0; the sum does not diverge because the terms are of size \(\dfrac1n\).
? For an increasing function, which unit rectangles give an upper bound for the area?
+ Those whose height is the value at the right-hand end of the strip
- Those whose height is the value at the left-hand end of the strip
- Both give an upper bound
- Neither: rectangles only give estimates, not bounds
> On an increasing curve the right-end value is the largest on the strip, so the rectangle covers the curve. Left ends give a lower bound; the pairs swap for a decreasing curve.
:::

:::checklist What you can now do
- [ ] I can estimate the area under a curve with left and right rectangles, and say which estimate is an upper bound and which a lower bound.
- [ ] I can sketch unit rectangles for an increasing or decreasing function and count them correctly.
- [ ] I can use rectangles to prove an inequality for a sum, such as \(\ln(n+1) < \sum \dfrac1r < 1 + \ln n\), matching the limits of the sum to the limits of the integral.
- [ ] I can shift the index to get both an upper and a lower bound, adding or removing the first or last term.
- [ ] I can bound sums such as \(\sum\dfrac{1}{r^2}\), \(\sum\sqrt r\), \(\sum e^{-r}\) and \(\ln(n!)\).
- [ ] I can use bounds to estimate a sum to a given accuracy, or to find how many terms are needed.
- [ ] I can write the limit of \(\dfrac1n\sum f\left(\dfrac rn\right)\) as an integral and evaluate it, finding the limits from the range of \(\dfrac rn\).
- [ ] I can rearrange a sum such as \(\sum\dfrac{n}{n^2 + r^2}\) into the form \(\dfrac1n\sum f\left(\dfrac rn\right)\).
:::

:::recap
- Left and right rectangles trap the area: for a decreasing curve left rectangles give the upper bound; for an increasing curve right rectangles do. The gap between them is \(h\,|f(b) - f(a)|\).
- Unit rectangles on \([r, r+1]\) or \([r-1, r]\) turn \(\sum f(r)\) into an area; \(n - 1\) rectangles span \([1, n]\), and \(n\) rectangles span \([1, n+1]\).
- \(\ln(n+1) < \displaystyle\sum_{r=1}^n\frac1r < 1 + \ln n\); \(\displaystyle\sum_{r=1}^n\frac1{r^2} < 2 - \frac1n\); \(\tfrac23n^{3/2} < \displaystyle\sum_{r=1}^n\sqrt r < \tfrac23n^{3/2} + \sqrt n\).
- Say which rectangles, above or below the curve, and why; use strict inequalities; match the limits of the integral to the rectangles.
- \(\displaystyle\lim_{n\to\infty}\frac1n\sum_{r=1}^nf\left(\frac rn\right) = \int_0^1f(x)\,dx\): pull out \(\dfrac1n\), spot \(f\), read the limits from the range of \(\dfrac rn\).
- Use rectangles when no formula for the sum exists; use the exact formula when it does.
:::

:::links
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · free booklets with answers, including series and sums
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · worked video solutions by topic
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot a curve and its unit rectangles, and compare the sum with the integral
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Arc length and surface area](#math.fm.arclength) uses integration to measure the length of a curve and the area of the surface formed when it is spun about an axis.
