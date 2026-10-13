@chapter math.s2.crv
@title Continuous random variables
@level a2
@paper CAIE P6 (S2) · Edexcel IAL S2 · UK Further Maths Statistics
@time 6–8 hours
@summary A continuous random variable, such as a waiting time or a mass, is described by a probability density function, and probabilities are areas under its graph. You will learn the properties of a pdf, how to find an unknown constant, and how to find probabilities, the mean, the variance, the median and percentiles by integration, including pdfs on an infinite interval.

:::why
Waiting times, masses, lengths and temperatures can take any value in a range, so you cannot list their probabilities one by one as you can for dice or coins. Instead you describe them with a curve, and you find probabilities by calculating areas, which means integrating. This chapter is where Paper 3 calculus meets statistics, and it also explains where the normal distribution curve comes from.
:::

**Before you start**, you need integration of powers of \(x\) and definite integrals from [Integration](#math.p1.integ), and \(E(X)\) and \(\mathrm{Var}(X)\) for discrete variables from [Discrete random variables](#math.s1.drv). The normal distribution in [The normal distribution](#math.s1.normal) is the best-known example of what follows.

:::try Warm-up
Q: Evaluate \(\displaystyle\int_1^4 (3x^2 - 2x)\,dx\). (from [Integration](#math.p1.integ))
A: \(\left[x^3 - x^2\right]_1^4\) \(= (64 - 16) - (1 - 1)\) \(= 48\).
Q: \(X \sim B(8, 0.25)\). Write down \(E(X)\) and \(\mathrm{Var}(X)\). (from [Discrete random variables](#math.s1.drv))
A: \(E(X) = np = 8 \times 0.25 = 2\) and \(\mathrm{Var}(X) = npq\) \(= 8 \times 0.25 \times 0.75\) \(= 1.5\).
Q: \(E(X) = 5\) and \(\mathrm{Var}(X) = 2\). Find \(E(2X - 3)\) and \(\mathrm{Var}(2X - 3)\). (from [Linear combinations of random variables](#math.s2.linear))
A: \(E(2X - 3) = 2 \times 5 - 3 = 7\) and \(\mathrm{Var}(2X - 3) = 2^2 \times 2 = 8\).
:::

## Probability as area

A **discrete** random variable takes separate values, such as the score on a die. A **continuous** random variable can take any value in an interval, such as the time you wait for a bus.

Suppose you record 1000 waiting times and draw a histogram with the **frequency density** on the vertical axis, scaled so that the total area is 1. Make the classes narrower and narrower and the steps blur into a smooth curve. That curve is the **probability density function**, and the area under it between two values is the probability of landing between them.

:::def Continuous random variable
A random variable that can take any value in an interval (which may have no upper or lower limit). Its distribution is described by a probability density function.
:::

:::def Probability density function (pdf)
A function \(f(x)\) with \(f(x) \ge 0\) for all \(x\) whose graph has total area 1. The probability that \(X\) lies between \(a\) and \(b\) is the area under \(f\) from \(a\) to \(b\).
:::

:::key Properties of a pdf
Let \(X\) have pdf \(f(x)\), defined on one interval and taken as 0 outside it.
- \(f(x) \ge 0\) everywhere.
- Total area 1: \(\displaystyle\int_{-\infty}^{\infty} f(x)\,dx = 1\), which in practice means integrating over the interval where \(f\) is not zero.
- \(\displaystyle P(a < X < b) = \int_a^b f(x)\,dx\).
- \(P(X = a) = 0\) for any single value \(a\), because a single point has no width. So \(P(X < a)\) and \(P(X \le a)\) are equal, and strict and non-strict inequalities make no difference.
- \(f(x)\) is **not** a probability. It can be larger than 1 (a narrow, tall curve), but the area never is.
:::

:::eg The waiting time \(T\) minutes for a train has pdf \(f(t) = \dfrac{10 - t}{50}\) for \(0 \le t \le 10\), and \(f(t) = 0\) otherwise. Show that \(f\) is a valid pdf and find \(P(T > 5)\).
Check the total area:
\[\int_0^{10} \frac{10 - t}{50}\,dt = \frac{1}{50}\left[10t - \frac{t^2}{2}\right]_0^{10} = \frac{1}{50}(100 - 50) = 1\]
Also \(f(t) \ge 0\) on the interval, so it is a valid pdf. Now
\[P(T > 5) = \int_5^{10} \frac{10 - t}{50}\,dt = \frac{1}{50}\left[10t - \frac{t^2}{2}\right]_5^{10} = \frac{1}{50}(50 - 37.5) = 0.25\]
:::

:::plot The pdf \(f(t) = (10 - t)/50\). The shaded area from 5 to 10 is \(P(T > 5) = 0.25\). Short waits are more likely than long ones.
--f "(10-x)/50" --label "f(t) = (10 − t)/50" --x 0 10 --y 0 0.24 --shade "0,5,10" --xlabel "t (minutes)" --legend tr
:::

## Finding an unknown constant

Many questions give a pdf with an unknown constant \(k\). The area must be 1, so integrate, set the result equal to 1 and solve for \(k\).

:::steps
1. Integrate \(f(x)\) over the whole interval, keeping \(k\) as a factor.
2. Put the result equal to 1 and solve for \(k\).
3. Check that \(f(x) \ge 0\) over the interval. A negative \(f\) means a mistake.
:::

:::eg The random variable \(X\) has pdf \(f(x) = kx^2\) for \(0 \le x \le 3\) and 0 otherwise. Find \(k\) and \(P(1 < X < 2)\).
\[\int_0^3 kx^2\,dx = k\left[\frac{x^3}{3}\right]_0^3 = 9k = 1 \quad\Rightarrow\quad k = \frac19\]
\[P(1 < X < 2) = \frac19\left[\frac{x^3}{3}\right]_1^2 = \frac19\left(\frac83 - \frac13\right) = \frac{7}{27} = 0.259\]
:::

:::eg \(X\) has pdf \(f(x) = kx(4 - x)\) for \(0 \le x \le 4\). Find \(k\) and \(P(X > 3)\).
Expand first: \(x(4 - x) = 4x - x^2\).
\[\int_0^4 k(4x - x^2)\,dx = k\left[2x^2 - \frac{x^3}{3}\right]_0^4 = k\left(32 - \frac{64}{3}\right) = \frac{32k}{3} = 1\]
So \(k = \dfrac{3}{32}\).
\[P(X > 3) = \frac{3}{32}\left[2x^2 - \frac{x^3}{3}\right]_3^4 = \frac{3}{32}\left(\frac{32}{3} - 9\right) = \frac{3}{32} \times \frac53 = \frac{5}{32} = 0.156\]
:::

## Mean and variance

For a discrete variable, \(E(X) = \sum x\,p\). For a continuous variable the sum becomes an integral.

:::key Mean and variance of a continuous variable
\[E(X) = \int x\,f(x)\,dx \qquad E(X^2) = \int x^2 f(x)\,dx\]
\[\mathrm{Var}(X) = E(X^2) - \left[E(X)\right]^2\]
- Integrate over the interval where \(f\) is not zero.
- More generally \(E(g(X)) = \int g(x)\,f(x)\,dx\).
- Both formulas are on MF19. The standard deviation is \(\sqrt{\mathrm{Var}(X)}\).
- If the pdf is symmetrical about a line \(x = c\), then \(E(X) = c\) and \(c\) is also the median.
:::

:::eg For \(f(x) = \dfrac{3}{32}x(4 - x)\), \(0 \le x \le 4\), find \(E(X)\) and \(\mathrm{Var}(X)\).
The curve \(y = f(x)\) is symmetrical about \(x = 2\), so \(E(X) = 2\). Check by integration:
\[E(X) = \frac{3}{32}\int_0^4 (4x^2 - x^3)\,dx = \frac{3}{32}\left[\frac{4x^3}{3} - \frac{x^4}{4}\right]_0^4 = \frac{3}{32}\left(\frac{256}{3} - 64\right) = 2\]
\[E(X^2) = \frac{3}{32}\int_0^4 (4x^3 - x^4)\,dx = \frac{3}{32}\left[x^4 - \frac{x^5}{5}\right]_0^4 = \frac{3}{32}\left(256 - \frac{1024}{5}\right) = 4.8\]
\[\mathrm{Var}(X) = 4.8 - 2^2 = 0.8\]
:::

:::eg The waiting time \(T\) from the first example has \(f(t) = \dfrac{10 - t}{50}\) for \(0 \le t \le 10\). Find the mean waiting time and the standard deviation.
\[E(T) = \frac{1}{50}\int_0^{10} (10t - t^2)\,dt = \frac{1}{50}\left[5t^2 - \frac{t^3}{3}\right]_0^{10} = \frac{1}{50}\left(500 - \frac{1000}{3}\right) = \frac{10}{3}\]
\[E(T^2) = \frac{1}{50}\int_0^{10} (10t^2 - t^3)\,dt = \frac{1}{50}\left[\frac{10t^3}{3} - \frac{t^4}{4}\right]_0^{10} = \frac{1}{50}\left(\frac{10000}{3} - 2500\right) = \frac{50}{3}\]
\[\mathrm{Var}(T) = \frac{50}{3} - \left(\frac{10}{3}\right)^2 = \frac{50}{9} = 5.556\]
The mean is \(3.33\) minutes, below the midpoint 5 because short waits are more likely, and the standard deviation is \(\sqrt{50/9} = 2.36\) minutes.
:::

:::warn Variance slips
- Forgetting to subtract \([E(X)]^2\). \(E(X^2)\) alone is not the variance.
- Subtracting \(E(X)\) instead of \([E(X)]^2\).
- Using \(\int x^2 f(x)\,dx\) with limits that do not match the interval of the pdf.
A variance can never be negative: if you get one, recheck \(E(X^2)\) and \(E(X)\).
:::

## Median and percentiles

:::def Median and percentiles
The **median** \(m\) of a continuous variable is the value with half the probability below it: \(P(X < m) = 0.5\). The \(p\)th **percentile** is the value \(q\) with \(P(X < q) = p/100\). The lower quartile, median and upper quartile are the 25th, 50th and 75th percentiles.
:::

:::key Finding a median or percentile
Integrate from the lower end of the interval up to an unknown value \(m\) and set the area equal to the required probability:
\[\int_{a}^{m} f(x)\,dx = 0.5 \quad\text{(median)} \qquad \int_{a}^{q} f(x)\,dx = \frac{p}{100} \quad(p\text{th percentile})\]
Then solve for \(m\) or \(q\). The median is **not** the midpoint of the interval unless the pdf is symmetrical.
:::

:::eg \(X\) has pdf \(f(x) = \dfrac{1}{2\sqrt{x}}\) for \(1 \le x \le 4\). Show that this is a valid pdf, then find \(E(X)\) and the median.
Write \(f(x) = \tfrac12 x^{-1/2}\). Area: \(\displaystyle\int_1^4 \tfrac12 x^{-1/2}\,dx = \left[x^{1/2}\right]_1^4\) \(= 2 - 1\) \(= 1\), so it is valid.

\[E(X) = \int_1^4 \tfrac12 x^{1/2}\,dx = \left[\tfrac13 x^{3/2}\right]_1^4 = \tfrac13(8 - 1) = \tfrac73 = 2.33\]

For the median, integrate from the lower limit 1 up to \(m\):
\[\int_1^m \tfrac12 x^{-1/2}\,dx = \left[x^{1/2}\right]_1^m = \sqrt{m} - 1 = 0.5\]
So \(\sqrt{m} = 1.5\) and \(m = 2.25\).
:::

:::plot The median of \(f(x) = \dfrac{1}{2\sqrt{x}}\) is 2.25, not the midpoint 2.5. The shaded area from 1 to 2.25 is 0.5.
--f "0.5/sqrt(x)" --label "f(x) = 1/(2√x)" --x 1 4 --y 0 0.6 --shade "0,1,2.25" --vline 2.25 --legend tr
:::

:::eg For \(f(x) = \dfrac{3}{8}x^2\), \(0 \le x \le 2\), find the 90th percentile.
Check: \(\int_0^2 \tfrac38 x^2\,dx = \tfrac38 \times \tfrac83 = 1\). Now
\[\int_0^q \tfrac38 x^2\,dx = \tfrac18 q^3 = 0.9 \quad\Rightarrow\quad q^3 = 7.2 \quad\Rightarrow\quad q = 1.93\]
:::

:::tip Setting up percentiles
Always integrate from the **lower limit of the domain**, not from 0 (unless that is the lower limit). In the median example the lower limit was 1, and the constant \(-1\) came from there. After solving, check that the answer lies inside the interval.
:::

The cumulative distribution function is not in the Cambridge syllabus, so you never need to name it. Integrating from the lower limit to \(m\), as above, is all that is required.

## Mean, median and the shape of the curve

When the pdf has a long tail on the right, a few large values pull the mean to the right of the median (positive skew). With a long tail on the left, the mean is below the median (negative skew). For a symmetrical pdf they are equal. You can use the shape to check an answer: for \(f(t) = (10 - t)/50\), a long right tail gives a mean (3.33) above the median \((10 - 5\sqrt2 = 2.93)\).

## Pdfs on an infinite interval

A pdf can stretch to infinity, as long as the total area is still 1. The area under \(f(x) = 1/x^4\) from 1 to infinity is finite, because \(1/x^4\) falls away quickly. To integrate, replace the infinite limit by a number \(b\) and let \(b\) get large; every term in \(b\) with a negative power then tends to 0.

:::eg \(X\) has pdf \(f(x) = \dfrac{k}{x^4}\) for \(x \ge 1\) and 0 otherwise. Find \(k\), \(P(X > 2)\), \(E(X)\), \(\mathrm{Var}(X)\), the median and \(E(1/X)\).
\[\int_1^\infty kx^{-4}\,dx = k\left[-\frac{x^{-3}}{3}\right]_1^\infty = k\left(0 + \frac13\right) = \frac k3 = 1\]
So \(k = 3\). As \(x \to \infty\), \(x^{-3} \to 0\).

\[P(X > 2) = \int_2^\infty 3x^{-4}\,dx = \left[-x^{-3}\right]_2^\infty = 0 + \frac18 = \frac18 = 0.125\]
\[E(X) = \int_1^\infty 3x^{-3}\,dx = \left[-\frac{3}{2}x^{-2}\right]_1^\infty = \frac32\]
\[E(X^2) = \int_1^\infty 3x^{-2}\,dx = \left[-3x^{-1}\right]_1^\infty = 3 \quad\Rightarrow\quad \mathrm{Var}(X) = 3 - \frac94 = \frac34\]
Median: \(\displaystyle\int_1^m 3x^{-4}\,dx = 1 - m^{-3} = 0.5\), so \(m^{-3} = 0.5\) and \(m = 2^{1/3} = 1.26\).

\[E\!\left(\frac1X\right) = \int_1^\infty \frac1x \times 3x^{-4}\,dx = \int_1^\infty 3x^{-5}\,dx = \left[-\frac34 x^{-4}\right]_1^\infty = \frac34\]
The mean 1.5 is above the median 1.26, as expected for a long right tail.
:::

:::warn Infinite limits
Show the step "as \(x \to \infty\), \(x^{-3} \to 0\)" in your working or write the limit explicitly, as the method mark depends on it. Do not substitute "infinity" into a formula as if it were a number. Also, not every power gives a finite answer: \(\int_1^\infty x^{-1}\,dx\) does not settle on a number, so a pdf like \(k/x\) on \([1, \infty)\) cannot exist.
:::

## Exam-style questions

:::eg (Exam style) The random variable \(X\) has pdf \(f(x) = kx^2\) for \(0 \le x \le 2\) and 0 otherwise. (a) Show that \(k = \dfrac38\). (b) Find \(E(X)\) and \(\mathrm{Var}(X)\). (c) Find the median of \(X\), and say how it compares with the mean. [9 marks]
(a) \(\displaystyle\int_0^2 kx^2\,dx = k\left[\frac{x^3}{3}\right]_0^2 = \frac{8k}{3}\) [M1]. Setting this equal to 1 gives \(k = \dfrac38\). [A1]

(b) \[E(X) = \int_0^2 \frac38 x^3\,dx = \frac38\left[\frac{x^4}{4}\right]_0^2 = \frac38 \times 4 = \frac32\] [M1 A1]
\[E(X^2) = \int_0^2 \frac38 x^4\,dx = \frac38\left[\frac{x^5}{5}\right]_0^2 = \frac38 \times \frac{32}{5} = \frac{12}{5}\] [M1]
\[\mathrm{Var}(X) = \frac{12}{5} - \left(\frac32\right)^2 = 2.4 - 2.25 = 0.15\] [A1]

(c) \(\displaystyle\int_0^m \frac38 x^2\,dx = \frac{m^3}{8} = \frac12\) [M1], so \(m^3 = 4\) and \(m = 1.59\). [A1]
The median (1.59) is larger than the mean (1.5). The pdf rises towards \(x = 2\) and has its long tail on the left, so the mean is pulled below the median. [B1]
:::

:::eg (Exam style) \(X\) has pdf \(f(x) = \dfrac{k}{x^5}\) for \(x \ge 1\) and 0 otherwise. (a) Find \(k\). (b) Find \(E(X)\) and \(\mathrm{Var}(X)\). (c) Find the median. [8 marks]
(a) \(\displaystyle\int_1^\infty kx^{-5}\,dx = k\left[-\frac{x^{-4}}{4}\right]_1^\infty\) \(= \frac{k}{4}\) [M1], so \(k = 4\). [A1]

(b) \(\displaystyle E(X) = \int_1^\infty 4x^{-4}\,dx\) \(= \left[-\frac43 x^{-3}\right]_1^\infty\) \(= \frac43\) [M1 A1]
\[E(X^2) = \int_1^\infty 4x^{-3}\,dx = \left[-2x^{-2}\right]_1^\infty = 2\] [M1]
\[\mathrm{Var}(X) = 2 - \frac{16}{9} = \frac29 = 0.222\] [A1]

(c) \(\displaystyle\int_1^m 4x^{-5}\,dx = 1 - m^{-4} = 0.5\), so \(m^4 = 2\) and \(m = 2^{1/4} = 1.19\). [M1 A1]
:::

:::exam Technique
- "Show that" means you must display the integration and the substitution of limits, not only the result.
- State the interval for each integral. For \(E(X)\) and \(E(X^2)\) use the same limits as the pdf.
- Give exact fractions where they are natural, then 3 s.f. for a decimal answer.
- For a median or percentile, write the equation \(\int_a^m f(x)\,dx = 0.5\) first: that is the method mark.
- Sketching the pdf, even roughly, lets you check the sign of your answers and the position of the mean and median.
:::

:::board
- **Edexcel IAL**: continuous random variables are in IAL S2. That specification also uses the cumulative distribution function \(F(x)\), which CAIE does not examine.
- **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: continuous random variables defined by a pdf are not in the single A Level. They appear in Further Maths statistics.
:::

:::eg Spot the error: where the median integral starts
A student answered this question [4 marks]: "\(X\) has pdf \(f(x) = kx\) for \(1 \le x \le 3\) and 0 otherwise. (a) Find \(k\). (b) Find the median of \(X\)."

Line 1: \(\displaystyle\int_1^3 kx\,dx = k\left[\frac{x^2}{2}\right]_1^3 = 4k\) \(= 1\), so \(k = \dfrac14\).
Line 2: For the median, \(\displaystyle\int_0^m \frac{x}{4}\,dx = \frac{m^2}{8} = 0.5\).
Line 3: \(m^2 = 4\), so the median is \(m = 2\).

**Line 1 earns [M1 A1]**. **Lines 2 and 3 score [M0 A0]**. The median equation must integrate from the lower end of the interval, which is 1, not from 0, because there is no probability below 1. Starting at 0 adds an area that does not exist, so the equation is wrong from the start. The student scores 2 out of 4.

Correct working: \(\displaystyle\int_1^m \frac{x}{4}\,dx = \frac{m^2 - 1}{8} = 0.5\), [M1] so \(m^2 = 5\) and \(m = 2.24\). [A1]

**Check:** the pdf rises from 1 to 3, so more probability lies on the right and the median should be above the midpoint 2. The student's 2 is not, and \(2.24\) is.
:::

:::try Start easy, finish at exam standard
Q: \(X\) has pdf \(f(x) = kx\) for \(0 \le x \le 4\). Find \(k\), \(P(X < 2)\), \(E(X)\) and the lower and upper quartiles.
A: \(\int_0^4 kx\,dx = 8k = 1\), so \(k = \tfrac18\). \(P(X < 2) = \tfrac{x^2}{16}\Big|_0^2 = \tfrac14\). \(E(X) = \int_0^4 \tfrac{x^2}{8}\,dx = \tfrac{64}{24}\) \(= \tfrac83\). For a quartile \(q\): \(\tfrac{q^2}{16} = 0.25\) gives \(q = 2\); \(\tfrac{q^2}{16} = 0.75\) gives \(q = \sqrt{12} = 3.46\).
Q: \(X\) has pdf \(f(x) = k(x + 1)\) for \(0 \le x \le 2\). Find \(k\) and \(E(X)\).
A: \(\int_0^2 k(x + 1)\,dx\) \(= k\left[\tfrac{x^2}{2} + x\right]_0^2 = 4k\) \(= 1\), so \(k = \tfrac14\). \(E(X) = \tfrac14\int_0^2 (x^2 + x)\,dx\) \(= \tfrac14\left(\tfrac83 + 2\right) = \tfrac76\).
Q: \(f(x) = \dfrac{3}{16}(4 - x^2)\) for \(0 \le x \le 2\). Show that it is a valid pdf, then find \(P(X > 1)\) and \(E(X)\).
A: Area: \(\tfrac{3}{16}\left[4x - \tfrac{x^3}{3}\right]_0^2\) \(= \tfrac{3}{16}\left(8 - \tfrac83\right) = 1\). \(P(X > 1) = \tfrac{3}{16}\left[4x - \tfrac{x^3}{3}\right]_1^2\) \(= \tfrac{3}{16}\left(\tfrac{16}{3} - \tfrac{11}{3}\right) = \tfrac{5}{16}\). \(E(X) = \tfrac{3}{16}\left[2x^2 - \tfrac{x^4}{4}\right]_0^2\) \(= \tfrac{3}{16}(8 - 4) = \tfrac34\).
Q: \(f(x) = \tfrac12\sin x\) for \(0 \le x \le \pi\) (radians). Show that it is a valid pdf, then find \(P\left(X < \tfrac\pi3\right)\) and the median.
A: \(\int_0^\pi \tfrac12\sin x\,dx = \tfrac12\left[-\cos x\right]_0^\pi\) \(= \tfrac12(1 + 1) = 1\). \(P\left(X < \tfrac\pi3\right) = \tfrac12\left[-\cos x\right]_0^{\pi/3}\) \(= \tfrac12\left(1 - \tfrac12\right) = \tfrac14\). The pdf is symmetrical about \(x = \tfrac\pi2\), so the median is \(\tfrac\pi2 = 1.57\).
Q: \(X\) has pdf \(f(x) = \dfrac{24}{x^4}\) for \(x \ge 2\). Show that the area is 1, then find \(E(X)\), \(\mathrm{Var}(X)\), the median and \(P(X > 5)\).
A: Area: \(\left[-8x^{-3}\right]_2^\infty = 0 + 1 = 1\). \(E(X) = \int_2^\infty 24x^{-3}\,dx\) \(= \left[-12x^{-2}\right]_2^\infty\) \(= 3\). \(E(X^2) = \int_2^\infty 24x^{-2}\,dx\) \(= \left[-24x^{-1}\right]_2^\infty\) \(= 12\), so \(\mathrm{Var}(X) = 12 - 9 = 3\). Median: \(1 - 8m^{-3} = 0.5\), so \(m^3 = 16\) and \(m = 2.52\). \(P(X > 5) = 8 \times 5^{-3} = 0.064\).
Q: The pdf of \(X\) is symmetrical about \(x = 6\) on \(2 \le x \le 10\). State \(E(X)\) and the median, and explain why. The variance is known to be 3.2. Find \(E(X^2)\).
A: Both equal 6, because the area is balanced either side of the line of symmetry. \(E(X^2) = \mathrm{Var}(X) + [E(X)]^2\) \(= 3.2 + 36 = 39.2\).
Q: \(X\) has pdf \(f(x) = \dfrac{k}{\sqrt{x}}\) for \(1 \le x \le 9\). Find \(k\), then find \(P(X < 4)\).
A: \(\int_1^9 kx^{-1/2}\,dx = k\left[2\sqrt{x}\right]_1^9\) \(= 4k = 1\), so \(k = \tfrac14\). \(P(X < 4) = \tfrac14\left[2\sqrt{x}\right]_1^4\) \(= \tfrac14(4 - 2)\) \(= \tfrac12\).
Q: Explain why \(f(x) = x - 1\) for \(0 \le x \le 3\) cannot be a pdf, even though \(\int_0^3 (x - 1)\,dx\) can be made equal to 1 by multiplying by a constant.
A: \(f(x)\) is negative for \(0 \le x < 1\), and a pdf must satisfy \(f(x) \ge 0\) everywhere. No positive constant \(k\) can fix that, because \(k(x - 1)\) is still negative on that part. (If \(k\) were negative, the pdf would be negative on \(1 < x \le 3\).)
Q: (Exam style) \(X\) has pdf \(f(x) = k\sqrt{x}\) for \(0 \le x \le 4\) and 0 otherwise. (a) Show that \(k = \tfrac{3}{16}\). (b) Find \(E(X)\) and \(\mathrm{Var}(X)\). (c) Find the median. [8 marks]
A: (a) \(\int_0^4 kx^{1/2}\,dx = k\left[\tfrac23 x^{3/2}\right]_0^4\) \(= \tfrac{16k}{3}\) [M1], so \(k = \tfrac{3}{16}\). [A1] (b) \(E(X) = \tfrac{3}{16}\int_0^4 x^{3/2}\,dx\) \(= \tfrac{3}{16}\left[\tfrac25 x^{5/2}\right]_0^4\) \(= \tfrac{3}{16} \times \tfrac{64}{5} = 2.4\). [M1 A1] \(E(X^2) = \tfrac{3}{16}\left[\tfrac27 x^{7/2}\right]_0^4\) \(= \tfrac{3}{16} \times \tfrac{256}{7} = \tfrac{48}{7}\). [M1] \(\mathrm{Var}(X) = \tfrac{48}{7} - 2.4^2\) \(= \tfrac{192}{175}\) \(= 1.10\). [A1] (c) \(\tfrac{3}{16} \times \tfrac23 m^{3/2} = \tfrac18 m^{3/2}\) \(= 0.5\), so \(m^{3/2} = 4\) and \(m = 4^{2/3} = 2.52\). [M1 A1]
Q: (Exam style) A machine part has length \(X\) cm with pdf \(f(x) = \dfrac{3}{x^4}\) for \(x \ge 1\), as in the worked example. A part is rejected if \(X > 2\). A batch of 50 independent parts is made. Find the expected number of rejects, and the probability that exactly 5 are rejected. [4 marks]
A: \(P(X > 2) = \tfrac18\) [M1 A1]. The number of rejects \(R \sim B\!\left(50, \tfrac18\right)\), so \(E(R) = 6.25\). \(P(R = 5) = \binom{50}{5}\left(\tfrac18\right)^5\left(\tfrac78\right)^{45}\) \(= 0.159\). [M1 A1]
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The random variable \(X\) has pdf \(f(x) = k(6 - x)\) for \(0 \le x \le 4\) and 0 otherwise. Find \(k\) and \(P(X < 2)\).
A: \(\displaystyle\int_0^4 k(6 - x)\,dx\) \(= k\left[6x - \frac{x^2}{2}\right]_0^4\) \(= 16k\) [M1] so \(k = \dfrac{1}{16}\). [A1] \(P(X < 2) = \dfrac{1}{16}\left[6x - \dfrac{x^2}{2}\right]_0^2\) [M1] \(= \dfrac{10}{16} = 0.625\). [A1]
Q: [6 marks] ★ \(f(x) = \dfrac{2x}{9}\) for \(0 \le x \le 3\) and 0 otherwise. (a) Show that \(f\) is a valid pdf. (b) Find \(E(X)\). (c) Find \(\mathrm{Var}(X)\).
A: (a) \(f(x) \ge 0\) on the interval, and \(\displaystyle\int_0^3 \frac{2x}{9}\,dx = \left[\frac{x^2}{9}\right]_0^3\) [M1] \(= 1\), so \(f\) is a valid pdf. [A1] (b) \(E(X) = \displaystyle\int_0^3 \frac{2x^2}{9}\,dx\) \(= \left[\frac{2x^3}{27}\right]_0^3\) [M1] \(= 2\). [A1] (c) \(E(X^2) = \displaystyle\int_0^3 \frac{2x^3}{9}\,dx\) \(= \left[\frac{x^4}{18}\right]_0^3\) \(= 4.5\), [M1] so \(\mathrm{Var}(X) = 4.5 - 2^2 = 0.5\). [A1]
Q: [5 marks] ★★ \(X\) has pdf \(f(x) = \dfrac{2}{x^3}\) for \(x \ge 1\) and 0 otherwise. (a) Find \(P(X > 3)\). (b) Find the median of \(X\).
A: (a) \(P(X > 3) = \displaystyle\int_3^\infty 2x^{-3}\,dx\) \(= \left[-x^{-2}\right]_3^\infty\) [M1] \(= 0 + \dfrac19 = 0.111\), using \(x^{-2} \to 0\) as \(x \to \infty\). [A1] (b) \(\displaystyle\int_1^m 2x^{-3}\,dx = 1 - m^{-2}\) [M1] \(= 0.5\), [A1] so \(m^2 = 2\) and \(m = 1.41\). [A1]
Q: [5 marks] ★★ \(f(x) = \dfrac{3x^2}{26}\) for \(1 \le x \le 3\) and 0 otherwise. Find the lower quartile, the upper quartile and the interquartile range.
A: For a quartile \(q\): \(\displaystyle\int_1^q \frac{3x^2}{26}\,dx = \frac{q^3 - 1}{26}\). [M1] Lower quartile: \(\dfrac{q^3 - 1}{26} = 0.25\), so \(q^3 = 7.5\) and \(q = 1.96\). [A1] Upper quartile: \(\dfrac{q^3 - 1}{26} = 0.75\), [M1] so \(q^3 = 20.5\) and \(q = 2.74\). [A1] The interquartile range is \(2.7369 - 1.9574 = 0.779\). [A1]
Q: [6 marks] ★★ \(X\) has pdf \(f(x) = k(x - 1)(5 - x)\) for \(1 \le x \le 5\) and 0 otherwise. (a) Show that \(k = \dfrac{3}{32}\). (b) Write down \(E(X)\), giving a reason. (c) Find \(P(X > 4)\).
A: (a) \(f(x) = k(-x^2 + 6x - 5)\), so \(\displaystyle\int_1^5 k(-x^2 + 6x - 5)\,dx\) \(= k\left[-\frac{x^3}{3} + 3x^2 - 5x\right]_1^5\) [M1] \(= k\left(\frac{25}{3} + \frac{7}{3}\right) = \frac{32k}{3} = 1\), so \(k = \dfrac{3}{32}\). [A1] (b) The graph is a parabola that is symmetrical about \(x = 3\), the midpoint of 1 and 5, [B1] so \(E(X) = 3\). [B1] (c) \(P(X > 4)\) \(= \dfrac{3}{32}\left[-\dfrac{x^3}{3} + 3x^2 - 5x\right]_4^5\) [M1] \(= \dfrac{3}{32}\left(\dfrac{25}{3} - \dfrac{20}{3}\right) = \dfrac{5}{32}\) \(= 0.156\). [A1]
Q: [8 marks] ★★ \(X\) has pdf \(f(x) = \dfrac{k}{x^6}\) for \(x \ge 1\) and 0 otherwise. (a) Show that \(k = 5\). (b) Find \(E(X)\) and \(\mathrm{Var}(X)\). (c) Find the median.
A: (a) \(\displaystyle\int_1^\infty kx^{-6}\,dx = k\left[-\frac{x^{-5}}{5}\right]_1^\infty\) [M1] \(= \dfrac{k}{5} = 1\), so \(k = 5\). [A1] (b) \(E(X) = \displaystyle\int_1^\infty 5x^{-5}\,dx\) \(= \left[-\frac54 x^{-4}\right]_1^\infty\) \(= \frac54\). [M1 A1] \(E(X^2) = \displaystyle\int_1^\infty 5x^{-4}\,dx\) \(= \left[-\frac53 x^{-3}\right]_1^\infty\) \(= \frac53\), [M1] so \(\mathrm{Var}(X) = \dfrac53 - \dfrac{25}{16} = \dfrac{5}{48}\) \(= 0.104\). [A1] (c) \(\displaystyle\int_1^m 5x^{-6}\,dx = 1 - m^{-5} = 0.5\), so \(m^5 = 2\) and \(m = 1.15\). [M1 A1]
Q: [11 marks] (#math.s2.linear) ★★★ The random variable \(X\) has pdf \(f(x) = a + bx\) for \(0 \le x \le 2\) and 0 otherwise, where \(a\) and \(b\) are constants. It is given that \(E(X) = 1.2\). (a) Find \(a\) and \(b\). (b) Find \(P(X > 1)\) and \(\mathrm{Var}(X)\). (c) \(X_1\) and \(X_2\) are independent observations of \(X\). Find \(E(X_1 - X_2)\) and \(\mathrm{Var}(X_1 - X_2)\).
H: You have two unknowns, so you need two equations: one from total area 1 and one from \(E(X) = 1.2\).
H: Total area: \(\displaystyle\int_0^2 (a + bx)\,dx = 2a + 2b\). For the mean, integrate \(x(a + bx)\) over the same interval.
H: In (c), variances of independent variables add for a difference, as in [Linear combinations](#math.s2.linear).
A: (a) \(\displaystyle\int_0^2 (a + bx)\,dx = 2a + 2b\) \(= 1\). [M1 A1] \(E(X) = \displaystyle\int_0^2 (ax + bx^2)\,dx\) \(= 2a + \frac{8b}{3}\) \(= 1.2\). [M1] Subtracting \(2a + 2b = 1\) gives \(\dfrac{2b}{3} = 0.2\), so \(b = 0.3\) and \(a = 0.2\). [A1] (b) \(P(X > 1)\) \(= \displaystyle\int_1^2 (0.2 + 0.3x)\,dx\) \(= \left[0.2x + 0.15x^2\right]_1^2\) [M1] \(= 0.65\). [A1] \(E(X^2)\) \(= \displaystyle\int_0^2 (0.2x^2 + 0.3x^3)\,dx\) \(= \dfrac{0.2 \times 8}{3} + 0.3 \times 4\) \(= 1.7333\), so \(\mathrm{Var}(X) = 1.7333 - 1.2^2\) \(= 0.293\). [M1 A1] (c) \(E(X_1 - X_2) = 1.2 - 1.2 = 0\). [B1] The variables are independent, so \(\mathrm{Var}(X_1 - X_2)\) \(= 0.2933 + 0.2933\) [M1] \(= 0.587\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ \(X\) has pdf \(f(x) = 2x\) for \(0 \le x \le 1\) and 0 otherwise, and \(Y = X^2\). (a) For \(0 \le y \le 1\), show that \(P(Y \le y) = y\). (b) What does this tell you about the pdf of \(Y\)? (c) Find \(E(Y)\) in two ways and check that they agree.
H: \(Y \le y\) is the same event as \(X \le \sqrt{y}\), because \(X\) is never negative. Integrate the pdf of \(X\) up to \(\sqrt{y}\).
H: If \(P(Y \le y) = y\), the area under the pdf of \(Y\) up to \(y\) is \(y\). What height gives that?
H: One way uses the pdf of \(Y\). The other uses \(E(Y) = E(X^2) = \int x^2 f(x)\,dx\).
A: (a) \(Y \le y\) means \(X^2 \le y\), that is \(X \le \sqrt{y}\). [M1] \(P(X \le \sqrt{y}) = \displaystyle\int_0^{\sqrt{y}} 2x\,dx\) \(= \left[x^2\right]_0^{\sqrt{y}}\) \(= y\). [A1] (b) The area up to \(y\) grows at rate 1, so the pdf of \(Y\) is the constant \(1\) on \(0 \le y \le 1\): \(Y\) is uniformly spread. [B1] (c) Using the pdf of \(Y\): \(E(Y) = \displaystyle\int_0^1 y \times 1\,dy = \frac12\). [M1] Using \(X\): \(E(Y) = E(X^2)\) \(= \displaystyle\int_0^1 x^2 \times 2x\,dx\) \(= \left[\frac{x^4}{2}\right]_0^1 = \frac12\). [M1] The two answers agree. [A1]
Q: [5 marks] ★★★ (a) Show that \(f(x) = \dfrac{1}{x^2}\) for \(x \ge 1\) is a valid pdf. (b) Show that \(E(X)\) cannot be found. (c) Find the median, and explain how the median can exist when the mean does not.
H: For (b), write \(E(X) = \displaystyle\int_1^b x \times \frac{1}{x^2}\,dx\) and see what happens as \(b\) gets large.
H: The median only needs probabilities (areas), not the average of very large values.
A: (a) \(f(x) \ge 0\) and \(\displaystyle\int_1^\infty x^{-2}\,dx = \left[-x^{-1}\right]_1^\infty\) \(= 0 + 1 = 1\). [M1 A1] (b) \(\displaystyle\int_1^b \frac{1}{x}\,dx = \ln b\), which grows without limit as \(b \to \infty\), [M1] so the integral for \(E(X)\) does not settle on a number. [A1] (c) \(\displaystyle\int_1^m x^{-2}\,dx = 1 - \frac{1}{m} = 0.5\), so \(m = 2\). The median is found from areas, which are finite, whereas the mean depends on very large values and these occur often enough, with a tail this heavy, to prevent the average settling. [B1]
:::

:::quiz Check your understanding
? Which statement must be true for every probability density function \(f(x)\)?
- \(f(x) \le 1\) for all \(x\)
- \(f(x)\) gives the probability that \(X = x\)
+ the total area under the graph is 1
- \(f(x)\) is symmetrical
> A pdf is non-negative with total area 1. The height \(f(x)\) is not a probability and can exceed 1, and there is no requirement for symmetry.
? \(X\) is a continuous random variable. What is \(P(X = 3)\)?
- \(f(3)\)
- \(\tfrac13\)
+ 0
- cannot be found
> A single point has no width, so no area. This is why \(P(X < 3) = P(X \le 3)\) for a continuous variable.
? \(f(x) = kx\) for \(0 \le x \le 2\). What is \(k\)?
- 2
- \(\tfrac14\)
+ \(\tfrac12\)
- 1
> \(\int_0^2 kx\,dx = 2k = 1\), so \(k = \tfrac12\). Getting \(\tfrac14\) comes from forgetting the \(\tfrac12\) when integrating \(x\).
? \(E(X^2) = 10\) and \(E(X) = 3\). What is \(\mathrm{Var}(X)\)?
- 7
- 13
- 91
+ 1
> \(\mathrm{Var}(X) = E(X^2) - [E(X)]^2\) \(= 10 - 9\) \(= 1\). Taking \(10 - 3 = 7\) forgets to square the mean.
? The median \(m\) of a continuous variable on \(a \le x \le b\) is found by solving:
- \(m = \dfrac{a + b}{2}\)
- \(f(m) = 0.5\)
+ \(\displaystyle\int_a^m f(x)\,dx = 0.5\)
- \(\displaystyle\int_a^b x f(x)\,dx = m\)
> The median has half the area below it. The midpoint only works for a symmetrical pdf, \(f(m) = 0.5\) confuses height with area, and the last option is the mean.
:::

:::checklist What you can now do
- [ ] I can check that a function is a valid pdf: non-negative, with total area 1.
- [ ] I can find an unknown constant \(k\) (or two constants) in a pdf by integrating.
- [ ] I can find \(P(a < X < b)\) by integrating the pdf, and explain why \(P(X = a) = 0\).
- [ ] I can find \(E(X)\), \(E(X^2)\) and \(\mathrm{Var}(X)\) by integration.
- [ ] I can find the median, quartiles and other percentiles by integrating from the lower limit of the domain.
- [ ] I can work with a pdf on an infinite interval, such as \(\dfrac{3}{x^4}\) for \(x \ge 1\), and show the limit step.
- [ ] I can use symmetry and the shape of the pdf to say where the mean and the median lie.
:::

:::recap
- A pdf has \(f(x) \ge 0\) and total area 1. \(P(a < X < b) = \int_a^b f(x)\,dx\), and \(P(X = a) = 0\).
- To find \(k\), integrate over the interval, set equal to 1 and solve.
- \(E(X) = \int x f(x)\,dx\), \(E(X^2) = \int x^2 f(x)\,dx\), \(\mathrm{Var}(X) = E(X^2) - [E(X)]^2\). Symmetry about \(c\) gives \(E(X) = c\) and median \(c\).
- Median and percentiles: \(\int_a^m f(x)\,dx = 0.5\) (or \(p/100\)), integrating from the lower limit of the domain.
- Infinite intervals: integrate to a limit, then let it tend to infinity; negative powers tend to 0. Show that step.
- A long right tail puts the mean above the median; a long left tail puts it below.
:::

:::links
- watch: [Finding k in a pdf](https://www.examsolutions.net/tutorials/finding-constant-k-in-a-pdf/) · ExamSolutions · total area equals 1
- watch: [Median, quartiles and percentiles from a pdf](https://www.examsolutions.net/tutorials/finding-median-quartiles-percentiles/) · ExamSolutions · areas up to the median
- practise: [CAIE S2 continuous random variables exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/topic-questions/statistical-distributions/continuous-random-variables/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Probability distributions](https://seeing-theory.brown.edu/probability-distributions/index.html) · Seeing Theory · continuous distributions as areas
- papers: [9709 Paper 6 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-7/) · Physics & Maths Tutor · papers with mark schemes [unofficial]

Links checked 3 October 2026.
:::
Next: [Sampling and estimation](#math.s2.sampling).
