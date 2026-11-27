@chapter math.fm.twosample
@title Comparing two means
@level fm
@paper CAIE 9231 Paper 4
@time 6–8 hours
@summary To compare two populations you estimate the difference of their means. You will choose between a pooled two-sample t-test, a paired t-test and a normal test for large samples, calculate a pooled estimate of variance, test for a difference (including a specified non-zero difference), and find confidence intervals for the difference of two means.
:::why
Almost every real experiment compares two things: a new drug against the old one, one fertiliser against another, performance before and after training. The data are never identical, so you need to decide whether the observed gap is bigger than chance would produce. Which test is right depends on how the data were collected, and choosing it correctly is half the marks.
:::

**Before you start**, you need the one-sample t-test, the t table and confidence intervals from [The t-distribution: one-sample tests and intervals](#math.fm.inference), the variance of a difference of independent variables from [Linear combinations of random variables](#math.s2.linear), and unbiased estimates from [Sampling and estimation](#math.s2.sampling).

:::try Warm-up
Q: \(\bar X \sim N\!\left(10, \dfrac{4}{5}\right)\) and \(\bar Y \sim N\!\left(8, \dfrac{9}{10}\right)\) are independent. State the distribution of \(\bar X - \bar Y\). (from [Linear combinations of random variables](#math.s2.linear))
A: A difference of independent normals is normal, with mean \(10 - 8 = 2\) and variance \(\dfrac45 + \dfrac{9}{10} = 1.7\) (variances add): \(N(2, 1.7)\).
Q: State the critical value of \(t\) for a two-tailed test at the 5% level with 11 degrees of freedom. (from [The t-distribution: one-sample tests and intervals](#math.fm.inference))
A: \(p = 0.975\), \(\nu = 11\): \(\pm 2.201\).
Q: A sample of 10 has \(\sum x = 50\) and \(\sum x^2 = 300\). Find the unbiased estimate of the population variance. (from [Sampling and estimation](#math.s2.sampling))
A: \(s^2 = \dfrac{300 - 50^2/10}{9} = \dfrac{50}{9} = 5.56\).
:::

## Choosing the right test

Two questions decide everything.

1. **Are the two samples independent, or are they paired?** Data are **paired** when each value in one sample is naturally linked to one value in the other: the same person measured before and after, twins, two halves of the same object, two methods applied to the same item. Otherwise the samples are **independent**: different people or items in each group.
2. **For independent samples, how big are they, and what is known about the variances?**

:::key Which test?
| Situation | Test | Statistic | Distribution |
|---|---|---|---|
| Paired data | **Paired t-test**: work with the differences \(d = x - y\) | \(t = \dfrac{\bar d - \delta_0}{s_d/\sqrt{n}}\) | \(t_{n-1}\) |
| Independent, small samples from normal populations, variances assumed equal | **Pooled two-sample t-test** | \(t = \dfrac{(\bar x_1 - \bar x_2) - \delta_0}{s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\) | \(t_{n_1+n_2-2}\) |
| Independent, large samples, variances unknown | **Normal test** with estimated variances | \(z = \dfrac{(\bar x_1 - \bar x_2) - \delta_0}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}\) | \(N(0, 1)\) |
| Independent, population variances known | **Normal test** with the true variances | as above with \(\sigma_1^2, \sigma_2^2\) | \(N(0, 1)\) |

Here \(\delta_0\) is the difference claimed by \(H_0\) (most often 0). \(s_p\) (the pooled standard deviation) and \(s_d\) (the standard deviation of the differences) are defined in the sections below.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 360 240" role="img" aria-label="Paired data. Eight people are timed before and after practice. Eight points in the left column, labelled before, are joined by straight lines to eight points in the right column, labelled after. Every line slopes slightly downwards. The mean of the before column is 49.6 and the mean of the after column is 47.0, each shown by a short thick bar beside its column.">
<line class="ax" x1="8" y1="215" x2="8" y2="18"/>
<text class="tl" x="16" y="16">time (s)</text>
<g class="ln-m thin">
<line x1="120" y1="130" x2="250" y2="151"/>
<line x1="120" y1="81" x2="250" y2="95"/>
<line x1="120" y1="179" x2="250" y2="186"/>
<line x1="120" y1="25" x2="250" y2="53"/>
<line x1="120" y1="102" x2="250" y2="116"/>
<line x1="120" y1="60" x2="250" y2="88"/>
<line x1="120" y1="158" x2="250" y2="165"/>
<line x1="120" y1="46" x2="250" y2="74"/>
</g>
<g class="f1 s-acc">
<circle cx="120" cy="130" r="3.5"/>
<circle cx="120" cy="81" r="3.5"/>
<circle cx="120" cy="179" r="3.5"/>
<circle cx="120" cy="25" r="3.5"/>
<circle cx="120" cy="102" r="3.5"/>
<circle cx="120" cy="60" r="3.5"/>
<circle cx="120" cy="158" r="3.5"/>
<circle cx="120" cy="46" r="3.5"/>
<circle cx="250" cy="151" r="3.5"/>
<circle cx="250" cy="95" r="3.5"/>
<circle cx="250" cy="186" r="3.5"/>
<circle cx="250" cy="53" r="3.5"/>
<circle cx="250" cy="116" r="3.5"/>
<circle cx="250" cy="88" r="3.5"/>
<circle cx="250" cy="165" r="3.5"/>
<circle cx="250" cy="74" r="3.5"/>
</g>
<line class="c2 sw3" x1="92" y1="97.6" x2="108" y2="97.6"/>
<line class="c2 sw3" x1="262" y1="116.0" x2="278" y2="116.0"/>
<text class="tl" x="86" y="102" text-anchor="end">mean 49.6</text>
<text class="tl" x="284" y="120">mean 47.0</text>
<text class="tl" x="120" y="232" text-anchor="middle">before</text>
<text class="tl" x="250" y="232" text-anchor="middle">after</text>
</svg><figcaption>Eight people timed before and after practice. People differ a great deal from each other (the spread within each column is large), but every person improved by a similar amount. A paired test looks at the lines; an independent test would see only the large spread within the columns.</figcaption></figure>
:::

:::warn Paired or independent?
Using an independent-sample test on paired data throws away the pairing, so the large differences between individuals swamp the real effect. Using a paired test when the samples are really independent is meaningless (there is no pairing). Look for the wording: "the same", "before and after", "each person", "matched" mean paired; "two groups", "a random sample from each of two" mean independent.
:::

## The pooled estimate of variance

If two normal populations share a common variance \(\sigma^2\), both samples give information about it. It is better to combine the two estimates than to use either alone. The combination weights each sample by its degrees of freedom.

:::def Pooled estimate of a common variance
For two independent samples of sizes \(n_1\) and \(n_2\) from populations with the same variance \(\sigma^2\),
\[s_p^2 = \frac{\sum (x_1 - \bar x_1)^2 + \sum (x_2 - \bar x_2)^2}{n_1 + n_2 - 2}\]
This formula is printed in MF19. Its numerator adds the two sums of squared deviations, and the divisor is the total degrees of freedom, \((n_1 - 1) + (n_2 - 1)\).
:::

Write \(S_{xx} = \sum (x - \bar x)^2 = \sum x^2 - \dfrac{(\sum x)^2}{n}\) for each sample. Then \(s_p^2 = \dfrac{S_{xx1} + S_{xx2}}{n_1 + n_2 - 2}\). Equivalently \(s_p^2 = \dfrac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}\): a weighted mean of the two sample variances, which lies between them and is closer to the one with the bigger sample. It is **not** \(\dfrac{s_1^2 + s_2^2}{2}\) unless \(n_1 = n_2\).

:::proof Why the pooled estimate is unbiased
Each sample variance is an unbiased estimate of \(\sigma^2\) ([Sampling and estimation](#math.s2.sampling)): \(E(S_1^2) = E(S_2^2) = \sigma^2\). Since \(\sum (x - \bar x)^2 = (n - 1)S^2\) for each sample,
\[E\Big[\sum (x_1 - \bar x_1)^2 + \sum (x_2 - \bar x_2)^2\Big] = (n_1 - 1)\sigma^2 + (n_2 - 1)\sigma^2 = (n_1 + n_2 - 2)\sigma^2\]
Dividing by \(n_1 + n_2 - 2\) gives \(E(S_p^2) = \sigma^2\). The divisor is \(n_1 + n_2 - 2\), not \(n_1 + n_2\), for the same reason as \(n - 1\) in one sample: each sample mean uses up one degree of freedom, and there are two sample means.
:::

:::eg Two fertilisers are tried on wheat. The yields (tonnes per hectare) of 6 plots with fertiliser A are 5.8, 6.4, 6.1, 5.9, 6.6, 6.2, and of 7 plots with fertiliser B are 5.4, 5.9, 5.6, 6.0, 5.2, 5.7, 5.5. Find the pooled estimate of variance, assuming a common variance.
Sample A: \(\sum x = 37.0\), \(\sum x^2 = 228.62\), so \(S_{xx} = 228.62 - \dfrac{37.0^2}{6} = 0.4533\).

Sample B: \(\sum x = 39.3\), \(\sum x^2 = 221.11\), so \(S_{xx} = 221.11 - \dfrac{39.3^2}{7} = 0.4686\).
\[s_p^2 = \frac{0.4533 + 0.4686}{6 + 7 - 2} = \frac{0.9219}{11} = 0.08381\]
and \(s_p = 0.2895\). (The two sample variances are 0.0907 and 0.0781; the pooled value lies between them, nearer 0.0781 because sample B is a little larger.)
:::

## The pooled two-sample t-test

:::key Pooled two-sample t-test
**Assumptions:** the two samples are independent random samples; each population is normal; the two populations have the **same variance** (this is stated or assumed, and you must say so).

To test \(H_0: \mu_1 - \mu_2 = \delta_0\), compute
\[t = \frac{(\bar x_1 - \bar x_2) - \delta_0}{s_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}\]
and compare with \(t_\nu\), where \(\nu = n_1 + n_2 - 2\).
:::

The denominator is the estimated standard deviation of \(\bar X_1 - \bar X_2\): the variance of a difference of independent means is \(\dfrac{\sigma^2}{n_1} + \dfrac{\sigma^2}{n_2} = \sigma^2\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)\), with the common \(\sigma^2\) replaced by \(s_p^2\).

:::eg Using the wheat data, test at the 5% level whether fertiliser A gives a greater mean yield than fertiliser B. Assume normal populations with a common variance.
Let \(\mu_A\) and \(\mu_B\) be the population mean yields. \(H_0: \mu_A = \mu_B\), \(H_1: \mu_A > \mu_B\).

\(\bar x_A = 6.1667\), \(\bar x_B = 5.6143\), \(s_p^2 = 0.08381\):
\[\begin{aligned}
\text{standard error} &= \sqrt{0.08381\left(\tfrac16 + \tfrac17\right)} = 0.1611 \\
t &= \frac{6.1667 - 5.6143}{0.1611} = 3.430
\end{aligned}\]
\(\nu = 6 + 7 - 2 = 11\); one-tailed 5% (\(p = 0.95\)): critical value 1.796. Since \(3.430 > 1.796\), reject \(H_0\): there is sufficient evidence, at the 5% level, that fertiliser A gives a greater mean yield.
:::

### Testing for a specified difference

Sometimes the claim is that one mean exceeds the other by a particular amount \(\delta_0\). Then \(H_0: \mu_1 - \mu_2 = \delta_0\) and the statistic subtracts \(\delta_0\) from the difference of means.

:::eg The makers of fertiliser A claim that it increases the yield by more than 0.2 tonnes per hectare compared with fertiliser B. Using the same data, test this claim at the 5% level.
\(H_0: \mu_A - \mu_B = 0.2\), \(H_1: \mu_A - \mu_B > 0.2\).
\[t = \frac{(6.1667 - 5.6143) - 0.2}{0.1611} = 2.188\]
with \(\nu = 11\) and critical value 1.796. Since \(2.188 > 1.796\), reject \(H_0\): there is sufficient evidence, at the 5% level, that the mean yield with A exceeds that with B by more than 0.2 tonnes per hectare.
:::

:::eg (Exam style) Two groups of plants are grown in different soils. After four weeks, the heights \(x\) cm of 8 plants in soil 1 have \(\sum x = 195.2\) and \(\sum x^2 = 4771.96\), and the heights \(y\) cm of 9 plants in soil 2 have \(\sum y = 204.9\) and \(\sum y^2 = 4669.81\). (a) Test, at the 5% level, whether the mean heights in the two soils differ. (b) State two assumptions needed for the test.
**(a)** Let \(\mu_1, \mu_2\) be the population mean heights in soils 1 and 2. \(H_0: \mu_1 = \mu_2\), \(H_1: \mu_1 \ne \mu_2\). [B1]
\[S_{xx1} = 4771.96 - \frac{195.2^2}{8} = 9.08, \qquad S_{xx2} = 4669.81 - \frac{204.9^2}{9} = 4.92\]
\[s_p^2 = \frac{9.08 + 4.92}{8 + 9 - 2}\] [M1]
\[= 0.9333\] [A1]
The means are \(\bar x = 24.4\) and \(\bar y = 22.767\).
\[t = \frac{24.4 - 22.767}{\sqrt{0.9333\left(\frac18 + \frac19\right)}}\] [M1]
\[= 3.479\] [A1]
\(\nu = 15\); two-tailed 5% (\(p = 0.975\)): critical values \(\pm 2.131\). [B1]
Since \(3.479 > 2.131\), reject \(H_0\). [M1]
There is sufficient evidence, at the 5% level, that the mean heights in the two soils differ. [A1]
**(b)** The heights in each soil are normally distributed. [B1] The two populations have the same variance. [B1]
:::

:::exam Showing the pooled method
Show the formula \(s_p^2 = \dfrac{S_{xx1} + S_{xx2}}{n_1 + n_2 - 2}\) with its numbers before you give the value: it earns the method mark, and the same value feeds the statistic and any confidence interval. MF19 prints this formula, but you must remember the standard error \(s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}\) and the degrees of freedom \(n_1 + n_2 - 2\).
:::

## The paired t-test

For paired data, subtract within each pair and treat the differences as **one** sample. Let \(d = x - y\) for each pair (decide the direction first and keep it), with mean \(\bar d\) and unbiased standard deviation \(s_d\). If the population of differences is normal with mean \(\mu_d\), then \(\dfrac{\bar d - \mu_d}{s_d/\sqrt{n}} \sim t_{n-1}\).

:::key Paired t-test
**Assumptions:** the pairs are a random sample; the **differences** are normally distributed (the original values need not be).
\[H_0: \mu_d = \delta_0 \qquad t = \frac{\bar d - \delta_0}{s_d/\sqrt{n}}, \quad \nu = n - 1\]
where \(n\) is the number of **pairs** and \(\delta_0\) is the difference the null hypothesis states: \(\delta_0 = 0\) tests "no change", and a claim such as "raises the score by more than 3.5" gives \(\delta_0 = 3.5\). Define \(\mu_d\) in words, including the direction: "the population mean of (before − after)".
:::

:::eg Eight people are timed (in seconds) on a puzzle, before and after a week of practice. Before: 45, 52, 38, 60, 49, 55, 41, 57. After: 42, 50, 37, 56, 47, 51, 40, 53. Test at the 5% level whether practice reduces the mean time. Assume the differences are normally distributed.
Let \(d = \) (time before) \(-\) (time after) and \(\mu_d\) the population mean of \(d\). \(H_0: \mu_d = 0\), \(H_1: \mu_d > 0\).

The differences are 3, 2, 1, 4, 2, 4, 1, 4, so \(\sum d = 21\) and \(\sum d^2 = 67\):
\[\bar d = \frac{21}{8} = 2.625, \qquad s_d^2 = \frac{67 - 21^2/8}{7} = 1.696, \qquad s_d = 1.302\]
\[t = \frac{2.625}{1.302/\sqrt{8}} = 5.700\]
\(\nu = 7\); one-tailed 5% (\(p = 0.95\)): critical value 1.895. Since \(5.700 > 1.895\), reject \(H_0\): there is sufficient evidence, at the 5% level, that practice reduces the mean time.

A 95% confidence interval for the mean reduction uses the one-sample method on the differences. With \(\nu = 7\) and \(p = 0.975\), \(t = 2.365\):
\[2.625 \pm 2.365 \times \frac{1.302}{\sqrt{8}} = 2.625 \pm 1.089, \quad (1.54,\ 3.71) \text{ seconds}\]
:::

:::eg (Exam style) A trainer claims that a course raises the score of a trainee, on average, by more than 3.5 points. Eight trainees take the same test before and after the course. Before: 52, 38, 61, 45, 70, 33, 58, 47. After: 57, 44, 64, 52, 75, 35, 66, 51. (a) Test the claim at the 10% level. (b) State an assumption needed for the test. [8 marks]
**(a)** Let \(d = \) (score after) \(-\) (score before) and \(\mu_d\) the population mean of \(d\). \(H_0: \mu_d = 3.5\), \(H_1: \mu_d > 3.5\). [B1]
The differences are 5, 6, 3, 7, 5, 2, 8, 4, so \(\sum d = 40\) and \(\sum d^2 = 228\):
\[\bar d = \frac{40}{8} = 5, \qquad s_d^2 = \frac{228 - 40^2/8}{7}\] [M1]
\[s_d^2 = 4\] [A1]
\[t = \frac{5 - 3.5}{2/\sqrt{8}}\] [M1]
\[t = 2.121\] [A1]
\(\nu = 7\); one-tailed 10% (\(p = 0.90\)): critical value 1.415. [B1]
Since \(2.121 > 1.415\), reject \(H_0\): there is sufficient evidence, at the 10% level, to support the claim that the course raises the mean score by more than 3.5. [A1]
**(b)** The differences are normally distributed. [B1]
:::

:::eg Treating the eight puzzle times above (before and after practice) as two independent samples (wrongly) shows what pairing is worth. The "before" times have mean 49.625 and \(S_{xx} = 20\,129 - \dfrac{397^2}{8} = 427.875\); the "after" times have mean 47.0 and \(S_{xx} = 17\,988 - \dfrac{376^2}{8} = 316\). The pooled variance is
\[s_p^2 = \frac{427.875 + 316}{8 + 8 - 2} = \frac{743.875}{14} = 53.13\]
Then
\[t = \frac{49.625 - 47.0}{\sqrt{53.13\left(\frac18 + \frac18\right)}} = \frac{2.625}{3.645} = 0.720\]
with \(\nu = 14\) and critical value 1.761. The statistic is nowhere near significant. The people vary a lot from each other (the within-sample variance 53 is large), which hides the steady improvement of about 2.6 seconds each. The paired test removes the person-to-person variation and finds a clear effect: it is much more sensitive for paired data.
:::

:::eg (Exam style) A garage measures the fuel consumption, in kilometres per litre, of 9 cars with and without a fuel additive. For each car let \(d\) be the consumption with the additive minus the consumption without it. The results give \(\sum d = 25.2\) and \(\sum d^2 = 142.56\). Test, at the 5% level, whether the additive changes the mean fuel consumption. Assume the differences are normally distributed.
Let \(\mu_d\) be the population mean of \(d\). \(H_0: \mu_d = 0\), \(H_1: \mu_d \ne 0\). [B1]
\[\bar d = \frac{25.2}{9} = 2.8, \qquad s_d^2 = \frac{142.56 - 25.2^2/9}{8}\] [M1]
\[= 9.0\] [A1]
\[t = \frac{2.8}{\sqrt{9/9}}\] [M1]
\[= 2.8\] [A1]
\(\nu = 8\); two-tailed 5% (\(p = 0.975\)): critical values \(\pm 2.306\). [B1]
Since \(2.8 > 2.306\), reject \(H_0\): there is sufficient evidence, at the 5% level, that the additive changes the mean fuel consumption (the sample suggests it increases it). [A1]
:::

## Large samples: the normal test

When both samples are large (the usual guide is 30 or more), the central limit theorem makes each sample mean approximately normal whatever the population, and \(s_1^2\) and \(s_2^2\) are close to the true variances. Then no assumption of a normal population or equal variances is needed.

:::key Two-sample normal test (large samples)
\[\bar X_1 - \bar X_2 \approx N\!\left(\mu_1 - \mu_2,\ \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}\right)\]
With \(\sigma_1^2\), \(\sigma_2^2\) unknown, estimate each by its own \(s^2\) (**do not pool**):
\[z = \frac{(\bar x_1 - \bar x_2) - \delta_0}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}} \sim N(0, 1)\]
Use the normal critical values (1.645 one-tailed 5%, 1.960 two-tailed 5%, 2.326 one-tailed 1%, 2.576 two-tailed 1%). If the true variances are known, use \(\sigma_1^2\) and \(\sigma_2^2\) in place of \(s_1^2\) and \(s_2^2\); that test is exact for normal populations whatever the sample sizes.
:::

:::eg (Exam style) A teacher compares test scores in two schools. A random sample of 50 students from school A has \(\sum x = 4120\) and \(\sum x^2 = 341\,252\). A random sample of 60 students from school B has \(\sum y = 4800\) and \(\sum y^2 = 386\,891\). Test, at the 5% level, whether the mean scores in the two schools differ.
Let \(\mu_A\) and \(\mu_B\) be the population mean scores. \(H_0: \mu_A = \mu_B\), \(H_1: \mu_A \ne \mu_B\). [B1]
\[\bar x = 82.4, \quad s_A^2 = \frac{341\,252 - 4120^2/50}{49} = 36\] [M1]
\[\bar y = 80, \quad s_B^2 = \frac{386\,891 - 4800^2/60}{59} = 49\] [A1]
The samples are large, so use the normal distribution with the estimated variances:
\[z = \frac{82.4 - 80}{\sqrt{\frac{36}{50} + \frac{49}{60}}}\] [M1]
\[= \frac{2.4}{1.240} = 1.936\] [A1]
Critical values \(\pm 1.960\). [B1]
Since \(-1.960 < 1.936 < 1.960\), do not reject \(H_0\): there is not sufficient evidence, at the 5% level, that the mean scores differ. [A1]
:::

The statistic is very close to the boundary: \(P(|Z| > 1.936) = 0.0529\), just above 5%. A one-tailed test with \(H_1: \mu_A > \mu_B\) would have rejected at 5%, because \(1.936 > 1.645\). This is why you must fix \(H_1\) from the wording before looking at the data.

:::eg Two machines fill packets with known standard deviations of 4 g and 5 g. A random sample of 9 packets from machine 1 has mean 104.2 g and a random sample of 12 from machine 2 has mean 101.0 g. The fills are normally distributed. Test, at the 5% level, whether machine 1 gives the greater mean fill.
\(H_0: \mu_1 = \mu_2\), \(H_1: \mu_1 > \mu_2\). The variances \(16\) and \(25\) are known, so the test is exact (no large-sample argument is needed).
\[z = \frac{104.2 - 101.0}{\sqrt{\frac{16}{9} + \frac{25}{12}}} = \frac{3.2}{1.965} = 1.629\]
The critical value is 1.645. Since \(1.629 < 1.645\), do not reject \(H_0\): there is not sufficient evidence, at the 5% level, that machine 1 has the greater mean fill.
:::

:::warn Do not pool in the normal test
In the large-sample normal test the two variances are estimated separately, \(\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}\). Pooling needs the assumption that the variances are equal and gives a \(t\), not a \(z\). Equally, do not use \(\sqrt{\dfrac{s_1^2 + s_2^2}{n}}\)-style shortcuts: each variance is divided by **its own** sample size.
:::

## Confidence intervals for a difference of means

A confidence interval for \(\mu_1 - \mu_2\) has the same shape as the test statistic: the difference of sample means, plus or minus a critical value times the standard error.

:::key Confidence intervals for \(\mu_1 - \mu_2\)
- **Pooled t interval** (small samples, normal populations, common variance): \(\displaystyle (\bar x_1 - \bar x_2) \pm t\,s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}\), with \(\nu = n_1 + n_2 - 2\) and \(p = 1 - \dfrac{\alpha}{2}\).
- **Normal interval** (large samples, or known variances): \(\displaystyle (\bar x_1 - \bar x_2) \pm z\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}\) (with \(\sigma^2\) if known).
- **Paired**: the one-sample interval on the differences, \(\bar d \pm t\dfrac{s_d}{\sqrt{n}}\).
- If the interval **contains 0**, a two-tailed test of \(\mu_1 = \mu_2\) at the matching level (95% interval, 5% test) does not reject \(H_0\). If it excludes 0, it does.
:::

:::eg (Exam style) The systolic blood pressures, in mm Hg, of two independent random groups of patients on different treatments are summarised below. Group 1 has \(n_1 = 10\), \(\sum x_1 = 1496\), \(\sum x_1^2 = 224\,224\). Group 2 has \(n_2 = 11\), \(\sum x_2 = 1563\), \(\sum x_2^2 = 222\,329\). Assume both populations are normal with the same variance. (a) Find a 95% confidence interval for the difference between the population means. (b) State whether the interval supports a difference between the means at the 5% level.
**(a)**
\[S_{xx1} = 224\,224 - \frac{1496^2}{10} = 422.4, \qquad S_{xx2} = 222\,329 - \frac{1563^2}{11} = 240.9\]
\[s_p^2 = \frac{422.4 + 240.9}{10 + 11 - 2} = 34.91\] [M1] [A1]
The sample means are \(149.6\) and \(142.09\), so the difference is \(7.51\). With \(\nu = 19\) and \(p = 0.975\), \(t = 2.093\). [B1]
\[7.51 \pm 2.093\sqrt{34.91\left(\tfrac{1}{10} + \tfrac{1}{11}\right)}\] [M1]
\[= 7.51 \pm 5.40: \quad (2.11,\ 12.9)\] [A1]
**(b)** The interval does not contain 0, so a two-tailed test at the 5% level would reject \(H_0: \mu_1 = \mu_2\): the interval supports a difference. [B1]
:::

:::eg Using the school scores (large samples), find a 95% confidence interval for \(\mu_A - \mu_B\).
Difference of sample means: \(82.4 - 80 = 2.4\). Standard error \(\sqrt{\dfrac{36}{50} + \dfrac{49}{60}} = 1.240\), and \(z = 1.960\) for 95%:
\[2.4 \pm 1.960 \times 1.240 = 2.4 \pm 2.43\]
The interval is \((-0.03,\ 4.83)\). It contains 0, in agreement with the test above (just failing to reject at 5%). A 90% interval (\(z = 1.645\)) would be \(2.4 \pm 2.04 = (0.36,\ 4.44)\), which excludes 0.
:::

## Spot the error, practice and stretch

:::eg Spot the error: random samples of 5 plants from group 1 and 10 plants from group 2, assumed to come from normal populations with a common variance, give \(\bar x_1 = 20\), \(\sum x_1^2 = 2032\), \(\sum x_1 = 100\) and \(\bar x_2 = 17.5\), \(\sum x_2^2 = 3080.5\), \(\sum x_2 = 175\). Test at the 5% level whether the means differ. (8 marks)
A student wrote this answer.

Line 1: \(H_0: \mu_1 = \mu_2\), \(H_1: \mu_1 \ne \mu_2\)
Line 2: \(S_{xx1} = 32\) and \(S_{xx2} = 18\), so \(s_1^2 = 8\) and \(s_2^2 = 2\)
Line 3: \(s_p^2 = \dfrac{8 + 2}{2} = 5\)
Line 4: \(t = \dfrac{2.5}{\sqrt{5\left(\frac15 + \frac1{10}\right)}} = 2.041\), with \(\nu = 13\)
Line 5: Critical values \(\pm 2.160\)
Line 6: \(2.041 < 2.160\), so do not reject \(H_0\).

Line 1 is correct. [B1]

**Line 3 loses the method and accuracy marks for the pooled variance.** [M0] [A0] The student averaged the two sample variances. With sizes 5 and 10 they must be weighted by their degrees of freedom: \(s_p^2 = \dfrac{32 + 18}{5 + 10 - 2} = 3.846\), not 5.

Line 4 uses the correct form of the statistic with the student's value, so it keeps the method mark and its accuracy mark follows through. [M1] [A1 FT] Line 5 is correct. [B1] Line 6 compares correctly with the critical value. [M1] [A1 FT]

The student scores 6 out of 8 but reaches the wrong conclusion. The correct value is \(t = \dfrac{2.5}{\sqrt{3.846 \times 0.3}} = 2.327 > 2.160\): reject \(H_0\). There is sufficient evidence, at the 5% level, that the means differ.
:::

:::try Start easy, finish at exam standard
Q: Decide the test: (a) the weights of 12 patients before and after a diet; (b) the heights of 8 randomly chosen girls and 9 randomly chosen boys from normal populations with common variance; (c) the lifetimes of 80 bulbs of brand P and 90 of brand Q.
A: (a) Paired t-test (same patients). (b) Pooled two-sample t-test, \(\nu = 15\). (c) Large independent samples: the two-sample normal test with \(s_P^2/80 + s_Q^2/90\).
Q: Sample 1: \(n = 7\), \(\sum x = 84\), \(\sum x^2 = 1050\). Sample 2: \(n = 9\), \(\sum x = 99\), \(\sum x^2 = 1100\). Find the pooled estimate of variance.
A: \(S_{xx1} = 1050 - \dfrac{84^2}{7} = 42\) and \(S_{xx2} = 1100 - \dfrac{99^2}{9} = 11\), so \(s_p^2 = \dfrac{53}{14} = 3.786\).
Q: Two independent samples give \(s_p = 2.4\) with \(n_1 = 6\), \(n_2 = 10\). Find the standard error of \(\bar x_1 - \bar x_2\) and the degrees of freedom.
A: \(2.4\sqrt{\dfrac16 + \dfrac1{10}} = 2.4 \times 0.5164 = 1.239\); \(\nu = 14\).
Q: Paired differences \(d\) have \(n = 10\), \(\bar d = 1.2\), \(s_d = 2.0\). Find \(t\) for \(H_0: \mu_d = 0\), and say whether \(H_1: \mu_d \ne 0\) is supported at 5%.
A: \(t = \dfrac{1.2}{2.0/\sqrt{10}} = 1.897\). Critical value (\(\nu = 9\), \(p = 0.975\)) is 2.262, and \(1.897 < 2.262\), so no.
Q: \(n_1 = 40\), \(\bar x_1 = 15.2\), \(s_1^2 = 6\); \(n_2 = 50\), \(\bar x_2 = 14.1\), \(s_2^2 = 8\). Find \(z\) for \(H_0: \mu_1 = \mu_2\).
A: \(z = \dfrac{1.1}{\sqrt{6/40 + 8/50}} = \dfrac{1.1}{0.5568} = 1.976\).
Q: A 95% confidence interval for \(\mu_1 - \mu_2\) is \((-1.2, 4.6)\). What does this say about a test of \(H_0: \mu_1 = \mu_2\) at 5%? Find \(\bar x_1 - \bar x_2\).
A: 0 is inside, so \(H_0\) is not rejected at the 5% level. The difference of means is the midpoint, 1.7.
Q: Explain why a test that treats paired data as independent is less likely to detect a real difference.
A: The between-subject variation inflates the variance estimate and hides the within-pair difference. Pairing removes the between-subject variation.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ State, with a reason, which test (paired t, pooled two-sample t, or normal two-sample) is appropriate for each. (a) The resting heart rates of 10 athletes are recorded before and after a training course. (b) 60 randomly chosen adults in town X and 75 in town Y are asked their daily screen time, and the means and unbiased variances are compared. (c) The breaking strengths of 6 cables of type A and 8 cables of type B, from normal populations with the same variance, are compared. (d) The yields of two fields are compared using 12 and 15 samples from normal populations whose variances (known from long records) are 3.5 and 4.2.
A: (a) Paired t-test: the same athletes, before and after. [B1] (b) Normal two-sample test with the estimated variances: large independent samples. [B1] (c) Pooled two-sample t-test, \(\nu = 12\). [B1] (d) Normal two-sample test using the known variances. [B1]
Q: [7 marks] ★★ Random samples of 6 and 7 values are taken from normal populations with a common variance. The first sample is 31, 35, 29, 33, 36, 30 and the second is 27, 30, 26, 29, 31, 28, 25. Test at the 5% level whether the mean of the first population exceeds that of the second by more than 2.
A: \(H_0: \mu_1 - \mu_2 = 2\), \(H_1: \mu_1 - \mu_2 > 2\). [B1]
\(S_{xx1} = 6312 - \dfrac{194^2}{6} = 39.33\), \(S_{xx2} = 5516 - \dfrac{196^2}{7} = 28\). \(s_p^2 = \dfrac{39.33 + 28}{11} = 6.121\). [M1] [A1]
\(\bar x_1 - \bar x_2 = 32.33 - 28 = 4.333\). \(t = \dfrac{4.333 - 2}{\sqrt{6.121\left(\frac16 + \frac17\right)}}\) [M1] \(= 1.695\). [A1]
\(\nu = 11\), critical value 1.796. [B1]
\(1.695 < 1.796\): do not reject \(H_0\); there is not sufficient evidence, at the 5% level, that the first mean exceeds the second by more than 2. [A1]
Q: [6 marks] ★★ Six people are tested for reaction time (in hundredths of a second) with the left hand and the right hand. The differences, left minus right, are 2, 3, 1, 4, 0, 4. Test at the 5% level whether the mean reaction time differs between hands, assuming the differences are normally distributed.
A: \(H_0: \mu_d = 0\), \(H_1: \mu_d \ne 0\), where \(\mu_d\) is the population mean of left minus right. [B1]
\(\bar d = \dfrac{14}{6} = 2.333\), \(s_d^2 = \dfrac{46 - 14^2/6}{5} = 2.667\). [M1] [A1]
\(t = \dfrac{2.333}{\sqrt{2.667/6}} = 3.500\). [M1] [A1]
\(\nu = 5\), critical values \(\pm 2.571\): reject \(H_0\); sufficient evidence at the 5% level that the means differ. [B1]
Q: [7 marks] ★★ A random sample of 45 students from one school has mean score 12.8 and unbiased variance estimate \(3.1^2\). A random sample of 55 students from another school has mean 11.9 and unbiased variance estimate \(2.8^2\). Test, at the 5% level, whether the mean score is higher in the first school.
A: \(H_0: \mu_1 = \mu_2\), \(H_1: \mu_1 > \mu_2\). [B1]
The samples are large, so use the normal distribution. [B1]
\(z = \dfrac{12.8 - 11.9}{\sqrt{\frac{3.1^2}{45} + \frac{2.8^2}{55}}}\) [M1] \(= \dfrac{0.9}{0.5967} = 1.508\). [A1]
Critical value 1.645. [B1] \(1.508 < 1.645\): do not reject \(H_0\). [M1]
There is not sufficient evidence, at the 5% level, that the first school's mean is higher. [A1]
Q: [10 marks] ★★★ Two independent samples from normal populations with a common variance give: sample 1, \(n_1 = 12\), \(\sum x_1 = 300\), \(\sum x_1^2 = 7750\); sample 2, \(n_2 = 10\), \(\sum x_2 = 203\), \(\sum x_2^2 = 4260.9\). (a) Find the pooled estimate of the common variance. (b) Find a 95% confidence interval for \(\mu_1 - \mu_2\). (c) State what this shows about a test at the 5% level of \(H_0: \mu_1 = \mu_2\). (d) Find a 99% confidence interval for \(\mu_1 - \mu_2\) and say whether the data show a difference at the 1% level.
H: \(S_{xx1} = 7750 - \dfrac{300^2}{12}\) and \(S_{xx2} = 4260.9 - \dfrac{203^2}{10}\).
H: \(\nu = 20\). The \(t\) values are 2.086 for 95% and 2.845 for 99%.
H: The standard error is \(s_p\sqrt{\frac{1}{12} + \frac{1}{10}}\).
A: (a) \(S_{xx1} = 250\), \(S_{xx2} = 140\), so \(s_p^2 = \dfrac{390}{20} = 19.5\). [M1] [A1] [A1]
(b) Difference \(25 - 20.3 = 4.7\); standard error \(\sqrt{19.5\left(\frac1{12} + \frac1{10}\right)} = 1.891\). [M1]
\(t = 2.086\): \(4.7 \pm 2.086 \times 1.891 = 4.7 \pm 3.944\), that is \((0.756,\ 8.64)\). [B1] [A1]
(c) 0 lies outside the interval, so \(H_0\) is rejected at the 5% level. [B1]
(d) \(t = 2.845\): \(4.7 \pm 2.845 \times 1.891 = 4.7 \pm 5.38\), that is \((-0.68,\ 10.1)\). [M1] [A1]
It contains 0, so there is not sufficient evidence, at the 1% level, of a difference. [B1]
Q: [12 marks] (#math.fm.inference) ★★★ Eight athletes' times (seconds) for a sprint are recorded before and after a training scheme. Before: 21.4, 20.8, 22.9, 21.1, 23.5, 22.2, 20.6, 22.7. After: 20.9, 20.5, 22.1, 20.8, 22.6, 21.6, 20.4, 21.8. (a) Test at the 5% level whether the scheme reduces the mean time, assuming the differences are normally distributed. (b) A second analyst treats the two lists as independent samples and uses a pooled two-sample test. Find the statistic she obtains, and her conclusion at the 5% level. (c) Explain why the two conclusions differ and which is correct.
H: The differences (before minus after) are 0.5, 0.3, 0.8, 0.3, 0.9, 0.6, 0.2, 0.9 with \(\sum d = 4.5\) and \(\sum d^2 = 3.09\).
H: For (b), \(\sum x = 175.2\), \(\sum x^2 = 3844.96\), \(\sum y = 170.7\), \(\sum y^2 = 3646.83\).
H: The pooled variance is about 0.900.
A: (a) \(H_0: \mu_d = 0\), \(H_1: \mu_d > 0\), \(d\) = before \(-\) after. [B1]
\(\bar d = 0.5625\), \(s_d^2 = \dfrac{3.09 - 4.5^2/8}{7} = 0.07982\). [M1] [A1]
\(t = \dfrac{0.5625}{\sqrt{0.07982/8}} = 5.631\); \(\nu = 7\), critical value 1.895. [M1] [A1] [B1]
Reject \(H_0\): sufficient evidence at 5% that the scheme reduces the mean time. [A1]
(b) \(s_p^2 = \dfrac{8.08 + 4.519}{14} = 0.8999\); \(t = \dfrac{21.9 - 21.3375}{\sqrt{0.8999\left(\frac18 + \frac18\right)}}\) [M1] \(= 1.186\). [A1]
\(\nu = 14\), critical value 1.761: do not reject \(H_0\). [A1]
(c) The athletes differ a lot in speed (variance between athletes about 0.9) but each improved by a similar small amount (variance of the differences about 0.08). The independent test lets the large between-athlete spread hide the effect. [B1]
The samples are paired (the same athletes), so the paired test in (a) is the correct one. [B1]
Q: [8 marks] ★★★ The independent samples below are taken from normal populations. Sample P: \(n = 9\), \(\sum x = 118.8\), \(\sum x^2 = 1583.28\). Sample Q: \(n = 12\), \(\sum x = 131.4\), \(\sum x^2 = 1447.26\). Find the pooled estimate of variance and test, at the 10% level, whether \(\mu_P - \mu_Q\) differs from 2.
H: Two-tailed at 10%: \(p = 0.95\).
H: \(S_{xx} = \sum x^2 - \dfrac{(\sum x)^2}{n}\) for each sample, then add.
A: \(S_{xxP} = 1583.28 - \dfrac{118.8^2}{9} = 15.12\), \(S_{xxQ} = 1447.26 - \dfrac{131.4^2}{12} = 8.43\). [M1] [A1]
\(s_p^2 = \dfrac{15.12 + 8.43}{19} = 1.239\). [A1]
\(H_0: \mu_P - \mu_Q = 2\), \(H_1: \mu_P - \mu_Q \ne 2\). [B1]
\(\bar x_P = 13.2\), \(\bar x_Q = 10.95\); \(t = \dfrac{(13.2 - 10.95) - 2}{\sqrt{1.239\left(\frac19 + \frac1{12}\right)}}\) [M1] \(= \dfrac{0.25}{0.4909} = 0.5092\). [A1]
\(\nu = 19\), critical values \(\pm 1.729\). \(|0.5092| < 1.729\), so do not reject \(H_0\). [B1] [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Show that the pooled variance \(s_p^2\) is a weighted mean of \(s_1^2\) and \(s_2^2\) with weights \(n_1 - 1\) and \(n_2 - 1\). For samples of sizes 5 and 10 with \(s_1^2 = 8\) and \(s_2^2 = 2\), explain, using the weights, why \(\dfrac{s_1^2 + s_2^2}{2} = 5\) overstates the pooled value.
H: Write \(\sum (x - \bar x)^2 = (n - 1)s^2\) for each sample.
H: The weights are 4 and 9.
A: \(\sum (x_1 - \bar x_1)^2 = (n_1 - 1)s_1^2\) and likewise for sample 2. [M1]
So \(s_p^2 = \dfrac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{(n_1 - 1) + (n_2 - 1)}\), a weighted mean with weights \(n_1 - 1\) and \(n_2 - 1\). [A1]
Here the weights are 4 and 9: \(s_p^2 = \dfrac{4 \times 8 + 9 \times 2}{13} = \dfrac{50}{13} = 3.846\). [M1] [A1]
The larger sample has the smaller variance and more weight, so the pooled value is nearer 2 than 8. The simple average 5 gives each sample equal weight. [B1]
Q: [6 marks] ★★★ Two independent samples of the same size \(n\) are taken from normal populations with common variance, and the pooled estimate is \(s_p = 4\). The difference in sample means is exactly 3. Use the MF19 table to find the smallest \(n\) for which a two-tailed pooled t-test at the 5% level would reject \(H_0: \mu_1 = \mu_2\).
H: The statistic is \(t = \dfrac{3}{4\sqrt{2/n}}\), with \(\nu = 2n - 2\).
H: Reject when \(t\) exceeds the critical value. Try \(n = 14\) and \(n = 15\), using the table values 2.056 (\(\nu = 26\)) and 2.048 (\(\nu = 28\)).
A: \(t = \dfrac{3}{4\sqrt{2/n}}\) and \(\nu = 2n - 2\). Reject when \(4\sqrt{\dfrac2n} \times t_{crit} \le 3\). [M1]
\(n = 14\): \(\nu = 26\), \(t_{crit} = 2.056\), and \(2.056 \times 4\sqrt{\tfrac{2}{14}} = 3.108 > 3\), so no rejection. [M1] [A1]
\(n = 15\): \(\nu = 28\), \(t_{crit} = 2.048\), and \(2.048 \times 4\sqrt{\tfrac{2}{15}} = 2.991 < 3\), so rejection. [M1] [A1]
The smallest sample size is \(n = 15\) in each group. [A1]
:::

:::quiz
? The same 20 people are weighed before and after a diet. Which test compares the mean weights?
+ A paired t-test with \(\nu = 19\)
- A pooled two-sample t-test with \(\nu = 38\)
- A normal two-sample test
- A one-sample t-test with \(\nu = 20\)
> The two weights belong to the same person, so the data are paired: use the 20 differences, with \(n - 1 = 19\) degrees of freedom. A pooled test would ignore the pairing.
? Two independent samples have sizes 8 and 11. How many degrees of freedom does the pooled t-test have?
+ \(17\)
- \(19\)
- \(18\)
- \(8\)
> \(\nu = n_1 + n_2 - 2 = 17\). Each sample mean uses one degree of freedom. The value 19 forgets both \(-1\)s and 18 forgets one.
? Which is the correct pooled estimate of variance for samples of size 5 and 10 with unbiased variances 8 and 2?
+ \(\dfrac{4 \times 8 + 9 \times 2}{13} = 3.85\)
- \(\dfrac{8 + 2}{2} = 5\)
- \(\dfrac{5 \times 8 + 10 \times 2}{15} = 4\)
- \(\dfrac{8 \times 2}{10} = 1.6\)
> The weights are the degrees of freedom, \(n_i - 1\). The plain average ignores the sample sizes, and weighting by \(n_i\) (not \(n_i - 1\)) divides by the wrong total.
? In a normal test for two large independent samples, the standard error of \(\bar x_1 - \bar x_2\) is
+ \(\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}\)
- \(\sqrt{\dfrac{s_1^2 + s_2^2}{n_1 + n_2}}\)
- \(\dfrac{s_1}{\sqrt{n_1}} - \dfrac{s_2}{\sqrt{n_2}}\)
- \(s_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}\)
> Variances of independent means add, each divided by its own sample size. Subtracting standard deviations is a classic error (variances add, even for a difference), and the last option is the pooled t-test's standard error.
? A 95% confidence interval for \(\mu_1 - \mu_2\) is \((0.4, 3.6)\). What follows about a two-tailed test of \(H_0: \mu_1 = \mu_2\) at the 5% level?
+ \(H_0\) is rejected, because 0 is outside the interval.
- \(H_0\) is not rejected, because the interval is narrow.
- \(H_0\) is rejected only if the interval is symmetric about 0.
- Nothing follows: tests and intervals are unrelated.
> A value outside the interval is rejected by the matching test. The interval is always symmetric about \(\bar x_1 - \bar x_2\), not about 0.
? For paired data the sample means are 20 and 18 and the standard deviation of the differences is 1. Which statement is correct?
+ The paired t-test looks at the differences, so the spread within each sample does not matter.
- The test must use the pooled variance of the two samples.
- The test needs the two populations to have equal variances.
- The paired test has \(2n - 2\) degrees of freedom.
> The paired t-test is a one-sample test on the differences, with \(n - 1\) degrees of freedom. Equal variances and pooling belong to independent samples.
:::

:::board
This chapter follows the 9231 Further Probability and Statistics syllabus. The pooled variance formula is printed in MF19, and the t table is too; the standard error of a difference of means and the choice of test are for you to know. If you also study another board's Further Statistics course, check its specification for which two-sample tests it requires.
:::

:::checklist What you can now do
- [ ] I can calculate a pooled estimate of a common variance from raw or summarised data.
- [ ] I can choose between a paired t-test, a pooled two-sample t-test and a normal test, and justify the choice.
- [ ] I can carry out a pooled two-sample t-test, including for a specified non-zero difference.
- [ ] I can carry out a paired t-test and give the assumption about the differences.
- [ ] I can carry out a normal test for the difference of means with large samples or known variances, without pooling.
- [ ] I can find a confidence interval for the difference of means (pooled t, normal, or paired).
- [ ] I can use a confidence interval to decide a two-tailed test at the matching level.
- [ ] I can state the assumptions of each test.
:::

:::recap
- Paired data (same individuals, matched pairs): one-sample t-test on the differences, \(\nu = n - 1\). Independent samples: a pooled t-test (small, normal, equal variances, \(\nu = n_1 + n_2 - 2\)) or a normal test (large samples, or known variances).
- Pooled variance (MF19): \(s_p^2 = \dfrac{S_{xx1} + S_{xx2}}{n_1 + n_2 - 2}\), a weighted mean with weights \(n_i - 1\).
- Pooled t: \(t = \dfrac{(\bar x_1 - \bar x_2) - \delta_0}{s_p\sqrt{1/n_1 + 1/n_2}}\).
- Normal test: \(z = \dfrac{(\bar x_1 - \bar x_2) - \delta_0}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}\): never pool.
- Confidence interval for \(\mu_1 - \mu_2\): difference of means \(\pm\) critical value \(\times\) standard error; 0 inside means the matching two-tailed test does not reject.
- Assumptions: pooled t needs normal populations with equal variances; paired t needs normal differences; the normal test needs large samples (or known variances).
:::

:::links
- watch: [Confidence interval for a population mean](https://www.examsolutions.net/tutorials/confidence-interval-for-a-population-mean/) · ExamSolutions · building and reading an interval
- practise: [Two-sample tests and intervals](https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples) · Khan Academy · exercises on comparing two means
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · free booklets with answers
- read: [Hypothesis testing with two samples](https://openstax.org/books/introductory-statistics-2e/pages/10-introduction) · OpenStax · independent and matched samples explained
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Chi-squared goodness of fit](#math.fm.chisq) moves from means to counts: testing whether data follow a stated distribution.
