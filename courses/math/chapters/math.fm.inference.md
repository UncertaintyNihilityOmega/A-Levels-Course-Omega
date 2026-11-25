@chapter math.fm.inference
@title The t-distribution: one-sample tests and intervals
@level fm
@paper CAIE 9231 Paper 4
@time 5–6 hours
@summary When you test a mean or build a confidence interval from a small sample and you do not know the population variance, the normal distribution is no longer correct and the t-distribution takes its place. You will learn what it is and how to read its table, how to run a one-sample t-test, and how to find and use a confidence interval for a mean.

:::why
In 9709 you tested a mean using a normal distribution, and you either knew the population variance or had a large sample. In practice you often have 8 or 12 measurements and no knowledge of the true spread. Dividing by the sample's own standard deviation adds a second source of uncertainty, and the t-distribution is the exact correction for it. It is the standard tool whenever a small sample from a normal population is all there is, and it is the foundation for comparing two means in the next chapter.
:::

**Before you start**, you need hypothesis tests for a mean and the idea of significance level from [Hypothesis testing](#math.s2.hypothesis), unbiased estimates \(\bar x\) and \(s^2\) and normal confidence intervals from [Sampling and estimation](#math.s2.sampling), and standardising from [The normal distribution](#math.s1.normal).

:::try Warm-up
Q: A sample of 5 values has \(\sum x = 40\) and \(\sum x^2 = 340\). Find unbiased estimates of the mean and variance of the population. (from [Sampling and estimation](#math.s2.sampling))
A: \(\bar x = 8\) and \(s^2 = \dfrac{340 - 40^2/5}{4} = \dfrac{20}{4} = 5\).
Q: For a population with variance 36, what is the standard deviation of the mean of a random sample of 9? (from [Sampling and estimation](#math.s2.sampling))
A: \(\dfrac{\sigma}{\sqrt{n}} = \dfrac{6}{3} = 2\).
Q: State the critical region for a two-tailed test at the 5% level using \(Z \sim N(0, 1)\). (from [Hypothesis testing](#math.s2.hypothesis))
A: Reject \(H_0\) if \(Z < -1.960\) or \(Z > 1.960\), because \(P(Z > 1.960) = 0.025\) in each tail.
:::

## Why a new distribution?

Suppose a population is normal with mean \(\mu\) and you take a random sample of size \(n\). In 9709 you met
\[Z = \frac{\bar X - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)\]
which needs \(\sigma\). If \(\sigma\) is unknown, the natural step is to replace it by the sample estimate \(s\):
\[T = \frac{\bar X - \mu}{S/\sqrt{n}}\]
The trouble is that \(S\) is itself random. A small sample can by chance have a spread much smaller or larger than the population's. When \(S\) is small by chance the denominator is small and \(T\) is large, so extreme values of \(T\) are more likely than extreme values of \(Z\). The distribution of \(T\) has the same bell shape but **heavier tails**.

:::def Student's t-distribution
If \(X_1, \dots, X_n\) is a random sample from a normal distribution with mean \(\mu\), and \(\bar X\) and \(S^2\) are the sample mean and unbiased variance estimate, then \(T = \dfrac{\bar X - \mu}{S/\sqrt{n}}\) has the **t-distribution with \(\nu = n - 1\) degrees of freedom**, written \(T \sim t_\nu\).
:::

:::def Degrees of freedom
The number of values that are free to vary once a sample statistic is fixed. Here \(\nu = n - 1\): the sample mean uses up one of the \(n\) values, because once \(n - 1\) of them and \(\bar x\) are known, the last is fixed. The variance estimate \(s^2\) has \(n - 1\) degrees of freedom.
:::

:::key Properties of the t-distribution
- Symmetric about 0, bell-shaped, with mean 0 (for \(\nu > 1\)).
- It has **heavier tails** than \(N(0, 1)\): for the same tail probability you must go further out. The smaller \(\nu\) is, the heavier the tails.
- As \(\nu \to \infty\), \(t_\nu\) tends to \(N(0, 1)\). By \(\nu = 30\) the two are close, which is why the last row of the MF19 table (\(\nu = \infty\)) holds the normal percentage points.
- It is exact only when the population is normal.
:::

:::plot A \(t\) distribution with 4 degrees of freedom has the same bell shape as \(N(0, 1)\) but is lower in the middle and higher in the tails. The line at \(x = 2\) cuts off the upper tail: \(P(T > 2) = 0.0581\) for \(t_4\), against 0.0228 for the normal.
--f "0.3989*exp(-(x**2)/2)" --f "0.375*(1+x**2/4)**(-2.5)" --label "N(0, 1)" --label "t with 4 degrees of freedom" --x -4.5 4.5 --y 0 0.55 --vline 2 --legend tl
:::

The widget below draws the \(t\) density for any number of degrees of freedom next to the normal curve and shades the critical region. Keep it open while you read the next section.

:::html
<div class="widget" data-w="fm-tdist" data-v="9" data-alpha="0.05" data-tails="2" data-t="2.9"></div>
:::

Start with \(\nu = 9\): the critical value for a two-tailed 5% test is 2.262, further out than the normal 1.960. Slide \(\nu\) down to 2 and the critical value balloons to 4.303, which is the price of having almost no information about the spread. Press the \(\infty\) button and the two curves coincide.

## Reading the t table in MF19

MF19 prints the percentage points of the t-distribution. A row is a number of degrees of freedom \(\nu\) (1 to 30, then 40, 60, 120 and \(\infty\)); a column is a probability \(p\), and the entry is the value \(t\) with \(P(T \le t) = p\). The columns are \(p\) = 0.75, 0.90, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999 and 0.9995. An extract:

| \(\nu\) | \(p = 0.90\) | \(p = 0.95\) | \(p = 0.975\) | \(p = 0.99\) | \(p = 0.995\) |
|---|---|---|---|---|---|
| 5 | 1.476 | 2.015 | 2.571 | 3.365 | 4.032 |
| 9 | 1.383 | 1.833 | 2.262 | 2.821 | 3.250 |
| 14 | 1.345 | 1.761 | 2.145 | 2.624 | 2.977 |
| 24 | 1.318 | 1.711 | 2.064 | 2.492 | 2.797 |
| \(\infty\) | 1.282 | 1.645 | 1.960 | 2.326 | 2.576 |

:::key Which column?
The table is a one-tail table: it gives the point with probability \(p\) **below** it, so \(1 - p\) is in the upper tail.
- One-tailed test at significance level \(\alpha\) (upper tail): use \(p = 1 - \alpha\). For a lower-tail test the critical value is the negative of that.
- Two-tailed test at level \(\alpha\): \(\alpha/2\) in each tail, so \(p = 1 - \dfrac{\alpha}{2}\), and the critical values are \(\pm t\).
- \(100(1 - \alpha)\%\) confidence interval: the same as a two-tailed test, \(p = 1 - \dfrac{\alpha}{2}\). For a 95% interval use \(p = 0.975\); for 99% use \(p = 0.995\); for 90% use \(p = 0.95\).
:::

:::eg Find the critical value for each case. (a) \(\nu = 9\), two-tailed test at 5%. (b) \(\nu = 14\), one-tailed test at 1%. (c) \(\nu = 24\), two-tailed test at 2%. (d) \(\nu = 5\), 90% confidence interval.
(a) Two tails of 2.5%: \(p = 0.975\). The row \(\nu = 9\) gives \(t = 2.262\), so reject if \(|t| > 2.262\).

(b) One tail of 1%: \(p = 0.99\), \(\nu = 14\): \(t = 2.624\).

(c) Two tails of 1% each: \(p = 0.99\), \(\nu = 24\): \(t = 2.492\), so \(\pm 2.492\).

(d) A 90% interval leaves 5% in each tail: \(p = 0.95\), \(\nu = 5\): \(t = 2.015\).
:::

:::warn Wrong column, wrong conclusion
The most common slip is reading the one-tailed column (\(p = 0.95\)) for a two-tailed 5% test: that gives 1.833 instead of 2.262 for \(\nu = 9\), and a test statistic of 2.0 is wrongly declared significant. Say the tail probability out loud: "5% two-tailed means 2.5% in each tail, so \(p = 0.975\)."
:::

## The one-sample t-test

You are testing a claim about the mean \(\mu\) of one normal population whose variance is unknown, using a small random sample.

:::key One-sample t-test
**Assumptions:** the population is normal (or the question says to assume it), the sample is random, and \(\sigma^2\) is unknown.

Under \(H_0: \mu = \mu_0\), the test statistic
\[t = \frac{\bar x - \mu_0}{s/\sqrt{n}} \qquad \text{has the } t_{n-1} \text{ distribution}\]
where
\[\bar x = \frac{\sum x}{n}, \qquad s^2 = \frac{1}{n - 1}\left(\sum x^2 - \frac{(\sum x)^2}{n}\right)\]
Both are unbiased estimates ([Sampling and estimation](#math.s2.sampling)): \(s^2\) divides by \(n - 1\), never \(n\).
:::

The wording of a question decides \(H_1\):

| The question says | \(H_1\) | Tails |
|---|---|---|
| "has changed", "is different from", "is not" | \(\mu \ne \mu_0\) | two-tailed |
| "is greater than", "has increased", "exceeds" | \(\mu > \mu_0\) | upper tail |
| "is less than", "has decreased", "is below" | \(\mu < \mu_0\) | lower tail |

\(H_0\) is always "\(\mu = \mu_0\)", the exact value the claim names. Decide the tails from the wording before you look at the data: choosing the tail after seeing which way the sample mean fell is not a fair test.

:::steps
1. Define \(\mu\) in words. State \(H_0: \mu = \mu_0\) and \(H_1\) (one-tailed \(\mu > \mu_0\) or \(\mu < \mu_0\), or two-tailed \(\mu \ne \mu_0\)). State the significance level.
2. Find \(\bar x\) and \(s^2\) (with divisor \(n - 1\)) from the data.
3. Calculate \(t = \dfrac{\bar x - \mu_0}{s/\sqrt{n}}\) and \(\nu = n - 1\).
4. Read the critical value from MF19 (the right column for the number of tails).
5. Compare, then conclude in context, in careful wording: "there is sufficient evidence at the 5% level that …" or "there is not sufficient evidence …".
:::

:::eg A manufacturer claims that a toy runs for 50 hours on one set of batteries. A consumer group tests 10 toys, chosen at random, and records the running times \(x\) hours: \(\sum x = 477.3\) and \(\sum x^2 = 22\,818.73\). Assuming the times are normally distributed, test at the 5% level whether the mean running time is less than 50 hours.
Let \(\mu\) be the population mean running time in hours. \(H_0: \mu = 50\), \(H_1: \mu < 50\) (one-tailed).

\[\bar x = \frac{477.3}{10} = 47.73\]
\[s^2 = \frac{1}{9}\left(22\,818.73 - \frac{477.3^2}{10}\right) = \frac{37.201}{9} = 4.133\]
so \(s = 2.033\) and the standard error is \(\dfrac{s}{\sqrt{10}} = 0.6429\). Then
\[t = \frac{47.73 - 50}{0.6429} = -3.531\]
with \(\nu = 9\). The lower-tail critical value for 5% comes from the \(p = 0.95\) column: \(-1.833\).

Since \(-3.531 < -1.833\), the statistic is in the critical region: reject \(H_0\). There is sufficient evidence, at the 5% level, that the mean running time is less than 50 hours.

(The value \(-3.531\) is beyond \(-3.250\), the point for \(p = 0.995\), so the test would also reject at the 0.5% level. The table cannot give an exact \(p\)-value: you can only say between which two columns the statistic lies.)
:::

When the data come as a list, find \(\bar x\) and \(s\) with your calculator's statistics mode (the \(s_x\) or \(\sigma_{n-1}\) key); the statistic and the critical value are then the same.

:::eg The masses, in grams, of 8 randomly chosen packets of rice, labelled 250 g, are 248.1, 251.6, 247.3, 249.9, 252.4, 246.8, 250.7, 248.5. Assuming the masses are normally distributed, test at the 5% level whether the mean mass differs from 250 g.
Let \(\mu\) be the population mean mass of a packet in grams. \(H_0: \mu = 250\), \(H_1: \mu \ne 250\) (two-tailed).

Calculator: \(n = 8\), \(\bar x = 249.41\), \(s = 2.051\) (the unbiased estimate), so \(\dfrac{s}{\sqrt{8}} = 0.7252\).
\[t = \frac{249.4125 - 250}{0.7252} = -0.8102\]
\(\nu = 7\); two-tailed 5% uses \(p = 0.975\): critical values \(\pm 2.365\).

Since \(-2.365 < -0.8102 < 2.365\), the statistic is not in the critical region: do not reject \(H_0\). There is not sufficient evidence, at the 5% level, that the mean mass differs from 250 g.
:::

The conclusion depends on the significance level you chose, so the level must be set before the test. The next example uses the same data at two levels.

:::eg A random sample of 6 gauges from a normal population gives readings 14.2, 15.8, 13.9, 16.1, 15.0, 14.7 (in units). A claim is made that the mean reading is 15.5 units. Test whether the mean is less than 15.5, at (a) the 5% level and (b) the 10% level.
Let \(\mu\) be the population mean reading. \(H_0: \mu = 15.5\), \(H_1: \mu < 15.5\).

\(n = 6\), \(\bar x = 14.95\), \(s = 0.8689\), so \(\dfrac{s}{\sqrt{6}} = 0.3547\) and
\[t = \frac{14.95 - 15.5}{0.3547} = -1.550\]
with \(\nu = 5\).

(a) 5% lower tail: critical value \(-2.015\). Since \(-1.550 > -2.015\), do not reject \(H_0\): not sufficient evidence at the 5% level.

(b) 10% lower tail (\(p = 0.90\)): critical value \(-1.476\). Since \(-1.550 < -1.476\), reject \(H_0\): sufficient evidence at the 10% level that the mean is below 15.5.

The evidence is moderate: stronger than a 10% fluke, weaker than a 5% one.
:::

:::eg A random sample of 12 values from a normal population has mean 20.4 and standard deviation 1.8, calculated with divisor \(n\) (the "population" standard deviation key). Test at the 5% level whether the population mean differs from 19.5.
The given 1.8 divides by \(n\), so it is not \(s\). Convert: the sum of squared deviations is \(12 \times 1.8^2 = 38.88\), and
\[s^2 = \frac{38.88}{11} = 3.535, \qquad s = 1.880\]
\(H_0: \mu = 19.5\), \(H_1: \mu \ne 19.5\). The standard error is \(\dfrac{1.880}{\sqrt{12}} = 0.5427\):
\[t = \frac{20.4 - 19.5}{0.5427} = 1.658\]
With \(\nu = 11\) and \(p = 0.975\) the critical values are \(\pm 2.201\). Since \(1.658 < 2.201\), do not reject \(H_0\): there is not sufficient evidence, at the 5% level, that the mean differs from 19.5.

Had you used 1.8 as \(s\), you would have got \(t = 1.732\): the same conclusion here, but a different number, and in a closer test a different conclusion.
:::

:::eg (Exam style) A bus company says that the journey between two stops takes a mean of 8.2 minutes. A passenger group believes journeys take longer. They time 12 journeys, chosen at random, and record the times \(x\) minutes: \(\sum x = 104.8\) and \(\sum x^2 = 917.74\). (a) Test the passenger group's belief at the 5% significance level. (b) State an assumption needed for the test.
**(a)** Let \(\mu\) be the population mean journey time in minutes. \(H_0: \mu = 8.2\), \(H_1: \mu > 8.2\). [B1]
\[s^2 = \frac{1}{11}\left(917.74 - \frac{104.8^2}{12}\right)\] [M1]
\[= 0.2261\] [A1]
The sample mean is \(\bar x = \dfrac{104.8}{12} = 8.733\).
\[t = \frac{8.733 - 8.2}{\sqrt{0.2261/12}}\] [M1]
\[= 3.886\] [A1]
\(\nu = 11\); one-tailed 5% (\(p = 0.95\)): critical value \(1.796\). [B1]
Since \(3.886 > 1.796\), reject \(H_0\). [M1]
There is sufficient evidence, at the 5% level, that the mean journey time is more than 8.2 minutes. [A1]
**(b)** The journey times are normally distributed (and the 12 journeys are a random sample). [B1]
:::

The critical value also converts into a critical region for the sample mean itself: rearrange \(t > t_{crit}\) into \(\bar x > \mu_0 + t_{crit}\dfrac{s}{\sqrt{n}}\).

:::eg A machine is set to fill bags with a mean of 30 units. A random sample of 16 bags from a normal population has \(s = 2.4\). A test is run at the 5% level of \(H_0: \mu = 30\) against \(H_1: \mu > 30\). Find the critical region for \(\bar x\), and compare it with the region you would get from the normal distribution with \(\sigma = 2.4\).
\(\nu = 15\), \(p = 0.95\): \(t_{crit} = 1.753\). The standard error is \(\dfrac{2.4}{\sqrt{16}} = 0.6\).
\[\bar x > 30 + 1.753 \times 0.6 = 31.05\]
With the normal distribution (\(z = 1.645\)) the region would be \(\bar x > 30 + 1.645 \times 0.6 = 30.99\). The t-region starts a little further out, so it is harder to reject \(H_0\): that extra caution is the price of not knowing \(\sigma\).
:::

### The assumption of normality

The t-distribution is exact only if the population is normal. With a small sample you cannot test that properly, so a question either tells you to assume it or asks you to state it.

- **State it.** "The population of running times is normally distributed" is the assumption for every t-test and interval in this chapter. The sample must also be random: each member equally likely to be chosen, and chosen independently.
- **Why it matters less as \(n\) grows.** By the central limit theorem ([Sampling and estimation](#math.s2.sampling)) the sample mean is nearly normal for a large sample whatever the population. The t-test is also fairly forgiving of mild departures from normality when the population is symmetric with no extreme outliers.
- **When it fails.** For a small sample from a clearly skewed population, or one with outliers, a t-test can mislead. The 9231 course offers tests that do not need normality (the sign test and the Wilcoxon tests, see [Non-parametric tests](#math.fm.nonpar)), at the price of using less of the information in the data.

:::exam z or t?
- Population variance \(\sigma^2\) **given**, or a known \(\sigma\): normal test with \(z\) (as in [Hypothesis testing](#math.s2.hypothesis)), whatever the size of the sample, provided the population is normal (or the sample is large).
- \(\sigma^2\) **unknown**, population normal, sample small: **t-test** with \(\nu = n - 1\).
- \(\sigma^2\) unknown, sample large: t and \(z\) are almost the same; a question that wants the normal approximation tells you (the next chapter uses it for two samples).
- The question may say "unbiased estimate" or give \(\sum x^2\): that signals you must compute \(s^2\) yourself.
Give 3 significant figures for \(t\) and quote the table value exactly as printed.
:::

## Confidence intervals for a mean

A confidence interval gives a range of plausible values for \(\mu\). In 9709 it used \(\sigma\) and \(z\) ([Sampling and estimation](#math.s2.sampling)). With \(\sigma\) unknown and a small normal sample, use \(s\) and \(t\).

:::key Confidence interval for a mean (small sample, \(\sigma\) unknown)
A \(100(1 - \alpha)\%\) confidence interval for \(\mu\) is
\[\bar x \pm t\,\frac{s}{\sqrt{n}}\]
where \(t\) is the value from MF19 with \(\nu = n - 1\) and \(p = 1 - \dfrac{\alpha}{2}\). The interval is symmetric about \(\bar x\); half its width is \(t\,\dfrac{s}{\sqrt{n}}\).
:::

:::proof Why the interval is \(\bar x \pm t s/\sqrt{n}\)
For a normal population, \(T = \dfrac{\bar X - \mu}{S/\sqrt{n}} \sim t_{n-1}\). Let \(t\) be the value with \(P(-t < T < t) = 0.95\), that is \(p = 0.975\). Then
\[P\left(-t < \frac{\bar X - \mu}{S/\sqrt{n}} < t\right) = 0.95\]
Multiply through by \(S/\sqrt{n}\), which is positive:
\[P\left(-t\frac{S}{\sqrt{n}} < \bar X - \mu < t\frac{S}{\sqrt{n}}\right) = 0.95\]
Multiply by \(-1\) (which reverses both inequalities) and add \(\bar X\):
\[P\left(\bar X - t\frac{S}{\sqrt{n}} < \mu < \bar X + t\frac{S}{\sqrt{n}}\right) = 0.95\]
The ends of the interval are random, because they depend on the sample. Substituting the observed \(\bar x\) and \(s\) gives the interval you report. A value \(\mu_0\) lies inside the interval exactly when \(\left|\dfrac{\bar x - \mu_0}{s/\sqrt{n}}\right| < t\), the same inequality that decides a two-tailed test.
:::

:::eg The heights, in centimetres, of 9 seedlings chosen at random after 10 days are 12.4, 13.1, 11.8, 12.9, 13.6, 12.2, 12.7, 13.3, 12.5. Assuming normality, find a 95% confidence interval for the mean height.
\(n = 9\): \(\bar x = 12.72\), \(s = 0.5652\), so \(\dfrac{s}{\sqrt{9}} = 0.1884\).

\(\nu = 8\), 95% interval: \(p = 0.975\), \(t = 2.306\).
\[12.722 \pm 2.306 \times 0.1884 = 12.722 \pm 0.4344\]
The 95% confidence interval is \((12.3, 13.2)\) cm to 3 s.f. (\(12.288\) to \(13.157\)).
:::

:::eg A random sample of 12 plates from a normal population has widths \(x\) cm with \(\sum x = 42.32\) and \(\sum x^2 = 149.391\). (a) Find a 99% confidence interval for the mean width. (b) A supplier says the mean width is 3.40 cm. Does the interval support this at the 1% significance level?
**(a)** \(\bar x = \dfrac{42.32}{12} = 3.5267\) and
\[s^2 = \frac{1}{11}\left(149.391 - \frac{42.32^2}{12}\right) = 0.012952\]
so \(s = 0.11380\) and \(\dfrac{s}{\sqrt{12}} = 0.03285\).

\(\nu = 11\), 99% interval: \(p = 0.995\), \(t = 3.106\).
\[3.5267 \pm 3.106 \times 0.03285 = 3.5267 \pm 0.1020\]
The interval is \((3.42, 3.63)\) cm (to 3 s.f.; exactly \(3.4246\) to \(3.6287\)).

**(b)** The value 3.40 is outside the interval, so the data do not support the supplier's claim: a two-tailed test of \(H_0: \mu = 3.40\) at the 1% level would reject \(H_0\). (Check: \(t = \dfrac{3.5267 - 3.40}{0.03285} = 3.856 > 3.106\).)
:::

:::key Reading a confidence interval
- A 95% confidence interval is produced by a method that captures the true mean in 95% of random samples. For *this* interval you cannot say "there is a 95% probability that \(\mu\) lies in it": \(\mu\) is fixed, and either it is in the interval or it is not.
- An interval **excludes** a value \(\mu_0\) exactly when a two-tailed test of \(H_0: \mu = \mu_0\) rejects \(H_0\) at the matching level (95% interval: 5% test; 99% interval: 1% test).
- A higher confidence level gives a **wider** interval; a larger sample (smaller \(s/\sqrt{n}\), and a smaller \(t\)) gives a **narrower** one.
:::

:::eg (Exam style) A random sample of 15 observations from a normal population has \(\sum x = 612\) and \(\sum x^2 = 25\,098.4\). (a) Find a 98% confidence interval for the population mean. (b) A researcher claims the population mean is 42. State, with a reason, whether the interval is consistent with this claim.
**(a)** \(\bar x = \dfrac{612}{15} = 40.8\).
\[s^2 = \frac{1}{14}\left(25\,098.4 - \frac{612^2}{15}\right) = 9.2\] [M1] [A1]
\(\nu = 14\), 98% interval: \(p = 0.99\), \(t = 2.624\). [B1]
\[40.8 \pm 2.624\sqrt{\frac{9.2}{15}}\] [M1]
\[= 40.8 \pm 2.055: \quad (38.7, 42.9)\] [A1]
**(b)** 42 lies inside the interval, so the interval is consistent with the claim: a two-tailed test at the 2% level would not reject \(\mu = 42\). [B1]
:::

## Spot the error, practice and stretch

:::eg Spot the error: a random sample of 9 lengths from a normal population has \(\sum x = 558\) and \(\sum x^2 = 34\,668\). Test at the 5% level whether the population mean differs from 60. (8 marks)
A student wrote this answer.

Line 1: \(H_0: \mu = 60\), \(H_1: \mu \ne 60\)
Line 2: \(s^2 = \dfrac{1}{8}\left(34\,668 - \dfrac{558^2}{9}\right) = 9\)
Line 3: \(t = \dfrac{62 - 60}{3/\sqrt{9}} = 2\), with \(\nu = 8\)
Line 4: Critical value (\(p = 0.95\)): 1.860
Line 5: \(2 > 1.860\), so reject \(H_0\): the mean differs from 60.

Lines 1 to 3 are correct: hypotheses [B1], variance [M1] [A1], statistic [M1] [A1].

**Line 4 loses the critical value mark.** [B0] The test is two-tailed, so the 5% is split into 2.5% in each tail and the column is \(p = 0.975\): the critical value is 2.306, not 1.860. The student used the one-tailed column.

Line 5 compares the statistic with the student's own critical value, so the method and the conclusion follow through. [M1] [A1 FT] The student scores 7 out of 8, but the conclusion is wrong: \(2 < 2.306\), so \(H_0\) is **not** rejected. There is not sufficient evidence, at the 5% level, that the mean differs from 60.
:::

:::try Start easy, finish at exam standard
Q: Write down the critical values for these tests: \(\nu = 12\), two-tailed 5%; \(\nu = 12\), 90% confidence interval; \(\nu = 12\), one-tailed 1%.
A: Two-tailed 5%: \(p = 0.975\), \(\pm 2.179\). A 90% interval: \(p = 0.95\), \(1.782\). One-tailed 1%: \(p = 0.99\), \(2.681\).
Q: A sample of 16 has \(\bar x = 52.9\) and \(s = 6\). Find the t statistic for testing \(H_0: \mu = 50\), and its degrees of freedom.
A: \(\dfrac{s}{\sqrt{n}} = 1.5\); \(t = \dfrac{2.9}{1.5} = 1.933\); \(\nu = 15\).
Q: For \(\nu = 15\), is \(t = 1.933\) significant at 5% in a one-tailed test? In a two-tailed test?
A: One-tailed: critical value 1.753, and \(1.933 > 1.753\), so significant. Two-tailed: critical value 2.131, and \(1.933 < 2.131\), so not significant.
Q: A random sample of 7 values from a normal population has \(\sum x = 203\) and \(\sum x^2 = 5908\). Find a 90% confidence interval for the mean.
A: \(\bar x = 29\), \(s^2 = \dfrac{5908 - 203^2/7}{6} = 3.5\); \(\nu = 6\), \(p = 0.95\), \(t = 1.943\). Interval: \(29 \pm 1.943\sqrt{3.5/7} = 29 \pm 1.374\): \((27.6, 30.4)\).
Q: The 95% confidence interval for a mean is \((4.1, 5.3)\). Find the sample mean. Is the value 5.5 plausible at the 5% level?
A: The mean is the midpoint, 4.7. The value 5.5 is outside the interval, so a two-tailed test at 5% would reject \(\mu = 5.5\).
Q: Explain why the t-distribution has heavier tails than the normal distribution.
A: \(s\) is estimated from a small sample and varies. When \(s\) happens to be small, \(\dfrac{\bar x - \mu}{s/\sqrt{n}}\) becomes large, so extreme values are more likely than for \(Z\), which has a fixed denominator.
Q: Which is wider for the same data: a 95% or a 99% confidence interval? Why?
A: The 99% interval, because \(p = 0.995\) gives a larger \(t\) than \(p = 0.975\) for the same \(\nu\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ For \(\nu = 12\), state the critical values for (a) a two-tailed test at the 5% level, (b) a one-tailed test at the 1% level, (c) a 90% confidence interval.
A: (a) \(\pm 2.179\). [B1] (b) \(2.681\). [B1] (c) \(1.782\). [B1]
Q: [6 marks] ★★ The times, in seconds, taken by 10 randomly chosen workers to assemble a part are 24.1, 26.3, 25.8, 27.0, 24.9, 26.1, 25.4, 27.2, 25.9, 26.5. The times are normally distributed. Test at the 5% level whether the mean time differs from 25.0 seconds.
A: \(H_0: \mu = 25.0\), \(H_1: \mu \ne 25.0\), where \(\mu\) is the population mean time. [B1]
\(\bar x = 25.92\), \(s = 0.9402\); \(t = \dfrac{25.92 - 25.0}{0.9402/\sqrt{10}}\) [M1] \(= 3.094\). [A1]
\(\nu = 9\), two-tailed 5%: critical value \(\pm 2.262\). [B1]
\(3.094 > 2.262\), so reject \(H_0\). [M1]
There is sufficient evidence at the 5% level that the mean time differs from 25.0 s. [A1]
Q: [5 marks] ★★ A random sample of 7 observations from a normal population has \(\sum x = 203\) and \(\sum x^2 = 5908\). Find a 90% confidence interval for the population mean.
A: \(\bar x = 29\). \(s^2 = \dfrac{5908 - 203^2/7}{6} = 3.5\). [M1] [A1]
\(\nu = 6\), \(p = 0.95\): \(t = 1.943\). [B1]
\(29 \pm 1.943\sqrt{\dfrac{3.5}{7}}\) [M1] giving \((27.6, 30.4)\). [A1]
Q: [8 marks] ★★ A scientist claims the mean of a normal population is at least 120. A random sample of 14 values has \(\sum x = 1645\) and \(\sum x^2 = 193\,755.5\). Test the claim at the 5% level, with \(H_1: \mu < 120\).
A: \(H_0: \mu = 120\), \(H_1: \mu < 120\). [B1]
\(\bar x = 117.5\), \(s^2 = \dfrac{193\,755.5 - 1645^2/14}{13} = 36\). [M1] [A1]
\(t = \dfrac{117.5 - 120}{6/\sqrt{14}}\) [M1] \(= -1.559\). [A1]
\(\nu = 13\), one-tailed 5%: critical value \(-1.771\). [B1]
\(-1.559 > -1.771\): do not reject \(H_0\). [M1]
There is not sufficient evidence, at the 5% level, that the population mean is below 120. [A1]
Q: [4 marks] ★★ A random sample of 20 observations from a normal population has \(s = 8\). A two-tailed test of \(H_0: \mu = 100\) is carried out at the 5% level. Find the critical region for the sample mean \(\bar x\).
A: \(\nu = 19\), \(p = 0.975\): \(t = 2.093\). [B1]
\(\dfrac{s}{\sqrt{n}} = \dfrac{8}{\sqrt{20}} = 1.789\), and \(2.093 \times 1.789 = 3.744\). [M1] [A1]
Reject \(H_0\) if \(\bar x < 96.3\) or \(\bar x > 103.7\) (1 d.p.). [A1]
Q: [10 marks] (#math.s2.hypothesis) ★★★ A random sample of 16 observations from a normal population has mean 53.6 and unbiased variance estimate \(s^2 = 36\). It is claimed that the population mean is 50. (a) Test, at the 5% level, whether the mean is greater than 50. (b) Repeat the test at the 1% level. (c) A student uses \(N(0, 1)\) instead of the t-distribution in (b). What conclusion does the student reach, and why is it unreliable?
H: The standard error is \(\dfrac{6}{\sqrt{16}} = 1.5\); the statistic is the same for both parts.
H: At 1% one-tailed with \(\nu = 15\), use the \(p = 0.99\) column.
H: For (c) compare the normal critical value 2.326 with your statistic.
A: (a) \(H_0: \mu = 50\), \(H_1: \mu > 50\). [B1] \(t = \dfrac{53.6 - 50}{6/4}\) [M1] \(= 2.4\). [A1]
\(\nu = 15\), critical value 1.753. [B1] \(2.4 > 1.753\), so reject \(H_0\): sufficient evidence at the 5% level that the mean exceeds 50. [A1]
(b) Critical value 2.602. [B1] \(2.4 < 2.602\): do not reject; not sufficient evidence at the 1% level. [A1]
(c) With \(z = 2.326\), \(2.4 > 2.326\) the student would reject \(H_0\). [B1]
This is unreliable: with \(\sigma\) unknown and \(n = 16\) the correct reference is \(t_{15}\), whose tails are heavier. Using the normal gives too small a critical value, so the true probability of wrongly rejecting is more than 1%. [B1] [B1]
Q: [9 marks] (#math.s2.sampling) ★★★ The thicknesses, in mm, of 8 randomly chosen washers, from a normal population, are 5.12, 4.87, 5.31, 4.95, 5.20, 5.05, 4.78, 5.22. (a) Find a 95% confidence interval for the mean thickness. (b) The manufacturing process has a known standard deviation of 0.15 mm. Find the 95% confidence interval that uses this value, and compare its width with the interval in (a). (c) Explain why the interval in (a) is wider.
H: Use \(\sum x = 40.5\) and \(\sum x^2 = 205.2692\).
H: In (b), the normal critical value is 1.960 and the standard error is \(\dfrac{0.15}{\sqrt8}\).
A: (a) \(\bar x = 5.0625\), \(s^2 = \dfrac{205.2692 - 40.5^2/8}{7} = 0.03399\), \(s = 0.1844\). [M1] [A1]
\(\nu = 7\), \(p = 0.975\): \(t = 2.365\). [B1]
\(5.0625 \pm 2.365\dfrac{0.1844}{\sqrt{8}}\) [M1] giving \((4.91, 5.22)\), width 0.308. [A1]
(b) \(5.0625 \pm 1.960 \times \dfrac{0.15}{\sqrt{8}}\) [M1] giving \((4.96, 5.17)\), width 0.208. [A1]
(c) The interval in (a) estimates \(\sigma\) from only 8 values, which adds uncertainty, and uses \(t_7\) which is wider than the normal. [B1]
The sample's \(s = 0.184\) also happens to be larger than 0.15. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A 95% confidence interval for a normal mean, from a sample of 10 observations, is \((41.2, 46.8)\). Find the sample mean and the unbiased estimate of the standard deviation, and hence find the 99% confidence interval from the same sample.
H: The sample mean is the midpoint; the half-width is \(t\dfrac{s}{\sqrt{n}}\) with \(\nu = 9\).
H: Use \(t = 2.262\) for 95% and \(t = 3.250\) for 99%.
A: \(\bar x = \dfrac{41.2 + 46.8}{2} = 44\). [B1]
Half-width \(= 2.8 = 2.262 \times \dfrac{s}{\sqrt{10}}\) [M1], so \(s = \dfrac{2.8\sqrt{10}}{2.262} = 3.914\). [A1]
99%: half-width \(= 3.250 \times \dfrac{3.914}{\sqrt{10}}\) [M1] \(= 4.023\). [A1]
Interval: \((40.0, 48.0)\). [A1]
Q: [5 marks] ★★★ A scientist wants the half-width of a 95% confidence interval for a normal mean to be at most half of the sample standard deviation, \(\tfrac12 s\). What is the smallest sample size that guarantees this, if \(s\) is the same for every sample size? Use the MF19 table.
H: The condition is \(t\dfrac{s}{\sqrt{n}} \le \tfrac12 s\), that is \(\dfrac{t}{\sqrt{n}} \le 0.5\), with \(\nu = n - 1\) and \(p = 0.975\).
H: Try \(n = 16, 17, 18\) and read the table values 2.131, 2.120, 2.110.
A: The condition is \(\dfrac{t_{n-1}}{\sqrt{n}} \le 0.5\). [M1]
\(n = 16\): \(\dfrac{2.131}{4} = 0.533\). \(n = 17\): \(\dfrac{2.120}{\sqrt{17}} = 0.514\). [M1] [A1]
\(n = 18\): \(\dfrac{2.110}{\sqrt{18}} = 0.497 \le 0.5\). [A1]
So the smallest sample size is 18. [A1]
:::

:::quiz
? A random sample of 12 values is used for a one-sample t-test. How many degrees of freedom does the \(t\) statistic have?
+ \(11\)
- \(12\)
- \(10\)
- \(13\)
> \(\nu = n - 1 = 11\). Using 12 forgets that the sample mean uses one degree of freedom.
? \(\nu = 9\). What is the critical value for a two-tailed test at the 5% significance level?
+ \(2.262\)
- \(1.833\)
- \(2.821\)
- \(1.960\)
> Two tails of 2.5% give \(p = 0.975\), which is 2.262. The value 1.833 is the one-tailed column (\(p = 0.95\)), 2.821 is for 1% one-tailed, and 1.960 is the normal value, wrong for a small sample with unknown variance.
? A sample of 5 has \(\sum x = 40\) and \(\sum x^2 = 340\). What is \(s^2\), the unbiased variance estimate?
+ \(5\)
- \(4\)
- \(\sqrt{5}\)
- \(20\)
> \(s^2 = \dfrac{340 - 320}{4} = 5\). The value 4 divides by \(n\), \(\sqrt5\) is \(s\) not \(s^2\), and 20 is the sum of squares about the mean, not yet divided.
? A 95% confidence interval for a mean is \((12.3, 13.2)\). Which statement is correct?
+ If the method were repeated with many random samples, about 95% of the intervals would contain \(\mu\).
- There is a 95% probability that \(\mu\) lies between 12.3 and 13.2.
- 95% of the population lies between 12.3 and 13.2.
- 95% of future sample means will lie between 12.3 and 13.2.
> The 95% describes the long-run success of the method. For one calculated interval, \(\mu\) is either in it or not, and the interval describes the mean, not the spread of individual values or of other sample means.
? As the degrees of freedom \(\nu\) increase, what happens to the t-distribution?
+ It gets closer to \(N(0, 1)\).
- It becomes more skewed to the right.
- Its tails become heavier.
- Its variance becomes 0.
> The \(t_\nu\) curve has tails that thin out as \(\nu\) grows, and for \(\nu = \infty\) it is exactly \(N(0, 1)\). It is always symmetric about 0.
? A random sample of 8 values from a normal population with unknown variance is used to test a mean. Which test is appropriate?
+ A t-test with \(\nu = 7\)
- A z-test using \(s\) in place of \(\sigma\)
- A t-test with \(\nu = 8\)
- A z-test with \(\sigma = 1\)
> With a small sample and unknown variance the t-test is exact, with \(n - 1 = 7\) degrees of freedom. Replacing \(\sigma\) by \(s\) in a z-test ignores the extra uncertainty, and 8 forgets the \(-1\).
:::

:::board
This chapter follows the 9231 Further Probability and Statistics syllabus (Paper 4, also part of AS Further Mathematics). The t-distribution table is printed in MF19, so you read critical values from it rather than calculating them. If you are using another board's Further Statistics course, check its specification for where t-tests appear and which tables it provides.
:::

:::checklist What you can now do
- [ ] I can explain why \(s\) is used in place of \(\sigma\) and why that makes the t-distribution have heavier tails than \(N(0, 1)\), with \(\nu = n - 1\).
- [ ] I can read the MF19 t table, choosing the right column for one-tailed tests, two-tailed tests and confidence intervals.
- [ ] I can carry out a one-sample t-test for a mean, from raw data or from \(\sum x\) and \(\sum x^2\), with full hypotheses, statistic, critical value and a conclusion in context.
- [ ] I can state the assumptions of the t-test (a random sample from a normal population).
- [ ] I can find a confidence interval for a mean from a small sample using the t-distribution.
- [ ] I can use a confidence interval to decide whether a stated mean is plausible, and interpret the interval correctly.
- [ ] I can find the critical region for \(\bar x\) from a t-test.
:::

:::recap
- When \(\sigma\) is unknown and the sample is small, \(\dfrac{\bar X - \mu}{S/\sqrt{n}} \sim t_{n-1}\) for a normal population: symmetric, heavier tails than \(N(0, 1)\), tending to \(N(0, 1)\) as \(\nu \to \infty\).
- \(s^2 = \dfrac{1}{n - 1}\left(\sum x^2 - \dfrac{(\sum x)^2}{n}\right)\). Never divide by \(n\) for \(s^2\).
- MF19 column: one-tailed test \(p = 1 - \alpha\); two-tailed test or \(100(1 - \alpha)\%\) interval \(p = 1 - \alpha/2\).
- One-sample t-test: \(t = \dfrac{\bar x - \mu_0}{s/\sqrt{n}}\), \(\nu = n - 1\); conclude in context with "sufficient evidence" wording.
- Confidence interval: \(\bar x \pm t\dfrac{s}{\sqrt{n}}\). A value outside the interval is rejected by the matching two-tailed test; a wider interval means more confidence or less data.
- State the assumption: the population is normal (and the sample is random).
:::

:::links
- watch: [Confidence interval for a population mean](https://www.examsolutions.net/tutorials/confidence-interval-for-a-population-mean/) · ExamSolutions · building and reading an interval
- practise: [Significance tests, one sample](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample) · Khan Academy · exercises on tests for a mean
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · free booklets with answers
- explore: [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory · draw samples and watch confidence intervals hit or miss
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Comparing two means](#math.fm.twosample) extends t-tests and intervals to two samples: pooled variance, paired data and large samples.
