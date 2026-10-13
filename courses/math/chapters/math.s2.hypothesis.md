@chapter math.s2.hypothesis
@title Hypothesis testing
@level a2
@paper CAIE P6 (S2) · Edexcel IAL S2 and S3 · AQA/OCR/Edexcel Statistics (Poisson tests in Further Maths)
@time 8–10 hours
@summary A hypothesis test uses sample evidence to decide whether a claim about a population is believable. You will learn the language of tests, how to test a binomial or Poisson probability from one observation (by direct probabilities, critical regions or a normal approximation), how to test a population mean, and how to find the probabilities of Type I and Type II errors.

:::why
Is a coin fair? Has a new fertiliser improved the yield? Is the factory still filling bottles correctly? Questions like these are answered by data that carry chance variation, so the answer is never certain. A hypothesis test gives a disciplined way to decide, and to say how likely you are to be wrong. It is the most widely used idea in statistics, and it brings together everything in this part of the course: the binomial, Poisson and normal distributions, the sampling distribution of the mean, and probability calculations.
:::

**Before you start**, you need the binomial distribution from [Discrete random variables](#math.s1.drv), the normal approximation from [The normal distribution](#math.s1.normal), the Poisson distribution from [The Poisson distribution](#math.s2.poisson), and the distribution of the sample mean from [Sampling and estimation](#math.s2.sampling).

:::try Warm-up
Q: \(X \sim B(15, 0.4)\). Find \(P(X \le 4)\). (from [Discrete random variables](#math.s1.drv))
A: Add the five terms, or use the calculator's binomial function: \(P(X \le 4) = 0.217\).
Q: \(X \sim \mathrm{Po}(2.5)\). Find \(P(X \ge 4)\). (from [The Poisson distribution](#math.s2.poisson))
A: "At least 4" is the complement of "at most 3": \(P(X \ge 4) = 1 - P(X \le 3)\) \(= 1 - 0.7576 = 0.242\).
Q: \(X \sim N(50, 8^2)\). Find the probability that the mean of a random sample of 16 observations is greater than 52. (from [Sampling and estimation](#math.s2.sampling))
A: \(\bar X \sim N\!\left(50, \dfrac{8^2}{16}\right)\) \(= N(50, 2^2)\), so \(P(\bar X > 52) = P(Z > 1)\) \(= 0.159\).
:::

## The idea of a hypothesis test

:::analogy A trial
In a court the starting position is that the defendant is innocent. The jury convicts only if the evidence is so unlikely under that assumption that it is "beyond reasonable doubt". A hypothesis test works in the same way: assume the claim is true, then ask how unlikely your data would be. Only if they are very unlikely do you reject the claim. Failing to convict does not prove innocence, and failing to reject a hypothesis does not prove it true.
:::

:::def Null hypothesis and alternative hypothesis
The **null hypothesis** \(H_0\) is the claim you assume to be true, stated as a value of a parameter, for example \(H_0: p = 0.3\). The **alternative hypothesis** \(H_1\) is what you will conclude if the evidence is strong enough to reject \(H_0\), for example \(H_1: p < 0.3\).
:::

:::def One-tailed and two-tailed tests
In a **one-tailed** test \(H_1\) says the parameter is greater than, or less than, the null value (\(>\) or \(<\)). In a **two-tailed** test \(H_1\) says only that it is different (\(\ne\)). Use the wording of the question: "has increased" or "is lower" means one-tailed, "has changed" or "is different" means two-tailed.
:::

:::def Test statistic, significance level, critical region
The **test statistic** is the quantity calculated from the sample (a count \(X\), or a mean \(\bar X\)). The **significance level** is the probability, set in advance, of rejecting \(H_0\) when it is actually true, typically 5% or 1%. The **critical region** (or rejection region) is the set of values of the test statistic for which \(H_0\) is rejected. The values outside it form the **acceptance region**. The edge of the critical region is the **critical value**.
:::

There are two equivalent ways to decide.

- **Probability method.** Find the probability, assuming \(H_0\), of a result **at least as extreme** as the one observed. If it is smaller than the significance level (halved in each tail for a two-tailed test), reject \(H_0\).
- **Critical region method.** Find, before looking at the data, the set of values that would lead to rejection, then see whether the observed value lies in it.

:::steps
1. Define the parameter and write \(H_0\) and \(H_1\) in terms of it, for example \(H_0: p = 0.3,\ H_1: p < 0.3\), where \(p\) is the probability that a randomly chosen item is faulty.
2. State the distribution of the test statistic **assuming \(H_0\) is true**, for example \(X \sim B(20, 0.3)\).
3. Find the probability of the observed result or a more extreme one (or find the critical region).
4. Compare with the significance level. For a two-tailed test use half the significance level in each tail.
5. State whether you reject \(H_0\), then write the conclusion **in the context of the question**.
:::

:::key Writing the conclusion
- If you reject \(H_0\): "There is sufficient evidence at the 5% significance level to suggest that [\(H_1\) in context]."
- If you do not reject \(H_0\): "There is insufficient evidence at the 5% significance level to suggest that [\(H_1\) in context]."
- Never write "\(H_0\) is true", "\(H_0\) is proved" or "accept \(H_0\)" as a definite fact. A test cannot prove \(H_0\); it can only fail to find evidence against it.
:::

## Testing a binomial probability

When you test a probability \(p\) using a count of successes in a fixed number of trials, the test statistic is \(X \sim B(n, p)\) under \(H_0\).

:::eg A manufacturer says that 30% of its components are faulty. After a process change, a random sample of 20 components contains 2 faulty ones. Test at the 5% significance level whether the proportion of faulty components has decreased.
Let \(p\) be the probability that a component is faulty.
\[H_0: p = 0.3 \qquad H_1: p < 0.3\]
This is one-tailed. Under \(H_0\), \(X \sim B(20, 0.3)\). We want the probability of 2 or fewer faulty components:
\[P(X \le 2) = 0.0355\]
Since \(0.0355 < 0.05\), we reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the proportion of faulty components has decreased.
:::

Notice that the probability is \(P(X \le 2)\), not \(P(X = 2)\). The results 0, 1 and 2 are all **at least as extreme** as 2 in the direction of \(H_1\), so we add up the whole tail.

:::html
<div class="widget" data-w="discrete" data-dist="binomial" data-n="20" data-p="0.3" data-range="0,2"></div>
:::

Set the range to \(0\) to \(2\) and read the total probability, which is the shaded tail. Change the range to see how far the tail would have to extend to pass 5%.

### Critical regions

A critical region is found before you collect the data. You choose the values in the tail so that the probability of landing in the region under \(H_0\) is **as large as possible without exceeding** the significance level.

:::eg \(X \sim B(20, 0.3)\) under \(H_0: p = 0.3\). Find the critical region for a 5% one-tailed test with (a) \(H_1: p < 0.3\) and (b) \(H_1: p > 0.3\), and state the actual significance level of each.
(a) \(P(X \le 2) = 0.0355\) and \(P(X \le 3) = 0.1071\). The second is above 5%, so the critical region is \(X \le 2\). The actual significance level is \(3.55\%\).

(b) \(P(X \ge 10) = 1 - P(X \le 9)\) \(= 0.0480\) and \(P(X \ge 9) = 0.1133\). The critical region is \(X \ge 10\). The actual significance level is \(4.80\%\).
:::

The **actual significance level** is the probability of being in the critical region when \(H_0\) is true. It is below the nominal 5% because a discrete variable cannot hit 5% exactly.

### Two-tailed tests

For \(H_1: p \ne p_0\), the evidence against \(H_0\) can be in either tail, so **split the significance level** and use half in each tail.

:::eg A coin is thrown 20 times and lands heads 15 times. Test at the 5% significance level whether the coin is biased.
Let \(p\) be the probability of heads. \(H_0: p = 0.5\), \(H_1: p \ne 0.5\). Two-tailed, so each tail has \(2.5\%\).

Under \(H_0\), \(X \sim B(20, 0.5)\). The observed value 15 is in the upper tail:
\[P(X \ge 15) = 0.0207\]
Since \(0.0207 < 0.025\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the coin is biased.

Critical region: lower tail \(P(X \le 5) = 0.0207\) and \(P(X \le 6) = 0.0577\), so \(X \le 5\). By symmetry the upper tail is \(X \ge 15\). The critical region is \(X \le 5\) or \(X \ge 15\), with actual significance level \(2 \times 0.0207 = 4.14\%\).
:::

:::warn Tail slips
- Using the whole 5% in one tail of a two-tailed test. Compare each tail with 2.5%.
- Using \(P(X = 15)\) instead of \(P(X \ge 15)\). The tail probability includes everything at least as extreme.
- For the upper tail, \(P(X \ge 15) = 1 - P(X \le 14)\), not \(1 - P(X \le 15)\).
- Writing \(H_0: p \ne 0.5\). The null hypothesis always states one value, with an equals sign.
:::

## Testing a Poisson mean

For counts of random events in an interval, the model is \(X \sim \mathrm{Po}(\lambda)\) and the hypotheses are about \(\lambda\), the mean number of events in the interval. The method is identical, with Poisson probabilities.

:::eg A call centre receives on average 6 calls per hour. After an advertising campaign it receives 12 calls in one randomly chosen hour. Test at the 5% level whether the mean number of calls per hour has increased.
Let \(\lambda\) be the mean number of calls per hour. \(H_0: \lambda = 6\), \(H_1: \lambda > 6\). Under \(H_0\), \(X \sim \mathrm{Po}(6)\).
\[P(X \ge 12) = 1 - P(X \le 11) = 0.0201\]
Since \(0.0201 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the mean number of calls per hour has increased. (At the 1% level the same result would not be significant, as \(0.0201 > 0.01\).)
:::

When the observation covers a different interval from the stated rate, **rescale \(\lambda\) to the interval you observe** before testing.

:::eg A website fails on average 0.8 times per day. In a randomly chosen 5-day week it fails 7 times. Test at the 5% level whether the failure rate has increased.
For 5 days the mean under \(H_0\) is \(0.8 \times 5 = 4\). Let \(\lambda\) be the mean number of failures per 5 days. \(H_0: \lambda = 4\), \(H_1: \lambda > 4\), \(X \sim \mathrm{Po}(4)\).
\[P(X \ge 7) = 1 - P(X \le 6) = 0.1107\]
Since \(0.1107 > 0.05\), do not reject \(H_0\). There is insufficient evidence at the 5% level to suggest that the failure rate has increased.
:::

## Normal approximations in tests

When \(n\) is large the exact binomial probabilities are hard to find by hand. Use the normal approximations from earlier chapters **under \(H_0\)**, with a continuity correction.

- Binomial: \(X \sim B(n, p)\) is approximately \(N(np, np(1 - p))\) when \(np\) and \(n(1-p)\) are both greater than 5.
- Poisson: \(X \sim \mathrm{Po}(\lambda)\) is approximately \(N(\lambda, \lambda)\) when \(\lambda > 15\).

:::eg A telesales firm says 40% of its calls end in a sale. A manager thinks it is higher. In a random sample of 100 calls, 50 end in a sale. Test at the 5% level.
\(H_0: p = 0.4\), \(H_1: p > 0.4\). Under \(H_0\), \(X \sim B(100, 0.4)\). Here \(np = 40\) and \(npq = 24\), so approximately \(Y \sim N(40, 24)\).

The result is \(X \ge 50\). With a continuity correction, \(P(X \ge 50) \approx P(Y > 49.5)\):
\[z = \frac{49.5 - 40}{\sqrt{24}} = 1.939 \qquad P(Z > 1.939) = 0.0262\]
Since \(0.0262 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that more than 40% of calls end in a sale.
:::

:::eg Defects in a type of cable occur at a mean rate of 25 per kilometre. A new supplier's cable has 35 defects in a randomly chosen kilometre. Test at the 5% level whether the rate is higher.
\(H_0: \lambda = 25\), \(H_1: \lambda > 25\). Under \(H_0\), \(X \sim \mathrm{Po}(25)\), and as \(\lambda > 15\), \(X \approx N(25, 25)\).
\[P(X \ge 35) \approx P(Y > 34.5), \quad z = \frac{34.5 - 25}{5} = 1.9, \quad P(Z > 1.9) = 0.0287\]
Since \(0.0287 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the new cable has a higher mean number of defects per kilometre.
:::

:::tip Continuity correction direction
For \(P(X \ge a)\) use \(P(Y > a - 0.5)\). For \(P(X \le a)\) use \(P(Y < a + 0.5)\). Sketch the tail if you are unsure: you include the whole bar for the value \(a\).
:::

## Testing a population mean

To test a claim about the mean \(\mu\) of a population, take a random sample of size \(n\) and use its mean \(\bar x\) as the test statistic. This needs the population to be **normal with known variance**, or a **large sample** (then use \(s^2\) as an estimate of \(\sigma^2\)). Under \(H_0: \mu = \mu_0\),
\[\bar X \sim N\!\left(\mu_0, \frac{\sigma^2}{n}\right)\]
so you standardise with \(z = \dfrac{\bar x - \mu_0}{\sigma/\sqrt{n}}\) and use the normal tables.

:::eg Bags of flour are supposed to have mean mass 500 g, with standard deviation 12 g. A random sample of 36 bags has mean mass 496.5 g. Test at the 5% level whether the mean mass is lower than 500 g.
Let \(\mu\) be the mean mass of a bag. \(H_0: \mu = 500\), \(H_1: \mu < 500\). Assume the standard deviation is still 12 g.
Under \(H_0\), \(\bar X \sim N\!\left(500, \dfrac{12^2}{36}\right)\) \(= N(500, 2^2)\).
\[P(\bar X < 496.5) = P\!\left(Z < \frac{496.5 - 500}{2}\right) = P(Z < -1.75) = 0.0401\]
Since \(0.0401 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the mean mass is below 500 g.
:::

:::html
<div class="widget" data-w="normal" data-mu="500" data-sigma="2" data-a="496.5" data-mode="below"></div>
:::

The curve is the distribution of \(\bar X\) under \(H_0\), and the shaded area is the probability of a sample mean as low as 496.5 g. Change the boundary to see where the area becomes 5%.

:::eg A machine fills tins with mean 100 g and standard deviation 6 g. A sample of 25 tins has mean 102.8 g. Test at the 5% level whether the mean has changed. Find the critical region for \(\bar X\).
\(H_0: \mu = 100\), \(H_1: \mu \ne 100\). Two-tailed. Under \(H_0\), \(\bar X \sim N\!\left(100, \dfrac{36}{25}\right)\), standard deviation \(1.2\).
\[z = \frac{102.8 - 100}{1.2} = 2.333 \qquad P(\bar X > 102.8) = P(Z > 2.333) = 0.00982\]
Compare with \(0.025\): \(0.00982 < 0.025\), so reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the mean mass has changed.

Critical region: the tails each have 2.5%, so the critical values are \(z = \pm 1.96\):
\[100 \pm 1.96 \times 1.2 = 100 \pm 2.352\]
The critical region is \(\bar X < 97.65\) or \(\bar X > 102.35\) (2 d.p.). Since 102.8 is in it, we reject \(H_0\).
:::

:::eg A random sample of 80 items has mean 34.2 and unbiased variance estimate \(s^2 = 5.6^2\). Test at the 5% level whether the population mean exceeds 33.
\(H_0: \mu = 33\), \(H_1: \mu > 33\). The sample is large, so \(\bar X \approx N\!\left(33, \dfrac{5.6^2}{80}\right)\), standard deviation \(0.6261\).
\[z = \frac{34.2 - 33}{0.6261} = 1.917 \qquad P(Z > 1.917) = 0.0276\]
Since \(0.0276 < 0.05\), reject \(H_0\): there is sufficient evidence at the 5% level to suggest that the population mean exceeds 33. At the 1% level we would not reject.
:::

:::warn Mean tests: the usual errors
- Standardising with \(\sigma\) instead of \(\sigma/\sqrt{n}\). The test is about the **mean** of the sample.
- Comparing a probability for the upper tail with the whole significance level in a two-tailed test.
- Using \(s\) for \(\sigma\) with a small sample from an unspecified population. The syllabus tests need a normal population with known variance, or a large sample.
- Reaching a conclusion about the sample ("the sample mean is too high") instead of the population mean.
:::

## Type I and Type II errors

A test can go wrong in two ways.

:::def Type I and Type II errors
A **Type I error** is rejecting \(H_0\) when it is true. A **Type II error** is not rejecting \(H_0\) when it is false (that is, when \(H_1\) is true).
:::

| | \(H_0\) true | \(H_0\) false |
|---|---|---|
| Reject \(H_0\) | **Type I error** | correct |
| Do not reject \(H_0\) | correct | **Type II error** |

:::key Probabilities of the errors
- Type I: \(P(\text{reject } H_0 \mid H_0 \text{ true})\). This is the probability that the test statistic falls in the critical region when \(H_0\) holds, which is the **actual significance level**.
- Type II: \(P(\text{do not reject } H_0 \mid H_1 \text{ true})\). This is the probability that the test statistic falls in the acceptance region. The question gives a specific value of the parameter that makes \(H_1\) true, and you calculate with that value.
:::

:::eg In the component test (\(X \sim B(20, p)\), \(H_0: p = 0.3\), \(H_1: p < 0.3\), critical region \(X \le 2\)), find the probability of a Type I error, and the probability of a Type II error when in fact \(p = 0.1\).
Type I: \(P(X \le 2 \mid p = 0.3)\) \(= 0.0355\).

Type II: the test does not reject when \(X \ge 3\). If \(p = 0.1\), \(X \sim B(20, 0.1)\):
\[P(X \ge 3) = 1 - P(X \le 2) = 1 - 0.6769 = 0.323\]
So there is a 32.3% chance that the test fails to detect the improvement.
:::

:::eg In the flour test (\(\bar X \sim N(500, 2^2)\) under \(H_0: \mu = 500\), \(H_1: \mu < 500\), 5% level), find the critical region for \(\bar X\) and the probability of a Type II error if the true mean is 495 g.
Critical region: \(\bar x < 500 - 1.645 \times 2\) \(= 496.71\). Type I probability is 5%.

If \(\mu = 495\), \(\bar X \sim N(495, 2^2)\). A Type II error occurs when \(\bar X \ge 496.71\):
\[P(\bar X \ge 496.71) = P\!\left(Z \ge \frac{496.71 - 495}{2}\right) = P(Z \ge 0.855) = 1 - 0.8037 = 0.196\]
:::

The probability of a Type II error depends on how far the true value is from the null value: the closer it is, the harder the difference is to detect, and the larger the Type II probability. A larger sample, or a larger significance level, reduces it.

## Exam-style questions

:::eg (Exam style) A courier company claims that 15% of its parcels arrive late. A customer believes the proportion is higher and finds that 7 of 25 randomly chosen parcels arrived late. (a) Test the customer's belief at the 5% significance level. (b) Find the critical region for the test and the actual significance level. [8 marks]
(a) Let \(p\) be the probability that a parcel arrives late. \(H_0: p = 0.15\), \(H_1: p > 0.15\). [B1]
Under \(H_0\), \(X \sim B(25, 0.15)\). [B1]
\[P(X \ge 7) = 1 - P(X \le 6) = 0.0695\] [M1 A1]
Since \(0.0695 > 0.05\), do not reject \(H_0\). There is insufficient evidence at the 5% level to suggest that the proportion of late parcels is more than 15%. [A1 for the comparison, B1 for the conclusion in context]

(b) \(P(X \ge 8) = 0.0255\) and \(P(X \ge 7) = 0.0695\). [M1] The critical region is \(X \ge 8\), and the actual significance level is \(2.55\%\). [A1]
:::

:::eg (Exam style) The number of flaws in a 10 m length of cloth is modelled by \(\mathrm{Po}(3.5)\). After the loom is serviced, a 20 m length contains 2 flaws. (a) Test at the 5% level whether the mean number of flaws has decreased. (b) Find the critical region for this test. (c) Find the probability of a Type II error if the mean number of flaws per 20 m is now 4. [9 marks]
(a) Let \(\lambda\) be the mean number of flaws in 20 m. Under \(H_0\), \(\lambda = 7\). \(H_0: \lambda = 7\), \(H_1: \lambda < 7\). [B1 B1]
\[P(X \le 2) = e^{-7}\left(1 + 7 + \frac{49}{2}\right) = 32.5e^{-7} = 0.0296\] [M1 A1]
Since \(0.0296 < 0.05\), reject \(H_0\): there is sufficient evidence at the 5% level to suggest that the mean number of flaws has decreased. [A1]

(b) \(P(X \le 3) = 0.0818 > 0.05\), so the critical region is \(X \le 2\). [M1 A1]

(c) A Type II error occurs when \(X \ge 3\) and \(X \sim \mathrm{Po}(4)\):
\[P(X \ge 3) = 1 - P(X \le 2) = 1 - 0.2381 = 0.762\] [M1 A1]
:::

:::eg (Exam style) A machine fills tins with mean mass 400 g and standard deviation 5 g. A sample of 16 tins has mean mass 402.6 g. (a) Test at the 5% significance level whether the mean has changed. (b) Find the critical region and the probability of a Type II error if the true mean is 403 g. [10 marks]
(a) \(H_0: \mu = 400\), \(H_1: \mu \ne 400\) [B1]. Under \(H_0\), \(\bar X \sim N\!\left(400, \dfrac{25}{16}\right)\), standard deviation \(1.25\). [B1]
\[z = \frac{402.6 - 400}{1.25} = 2.08 \qquad P(Z > 2.08) = 0.0188\] [M1 A1]
Since \(0.0188 < 0.025\) (two-tailed), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the mean mass of the tins has changed. [A1 B1]

(b) Critical values: \(400 \pm 1.96 \times 1.25\) \(= 400 \pm 2.45\). The critical region is \(\bar X < 397.55\) or \(\bar X > 402.45\). [M1 A1]
If \(\mu = 403\), \(\bar X \sim N(403, 1.25^2)\), and a Type II error occurs for \(397.55 \le \bar X \le 402.45\):
\[P = \Phi\!\left(\frac{402.45 - 403}{1.25}\right) - \Phi\!\left(\frac{397.55 - 403}{1.25}\right) = \Phi(-0.44) - \Phi(-4.36) = 0.330\] [M1 A1]
:::

:::exam Technique
- Always define the parameter and state \(H_0\) and \(H_1\) in terms of it, with the significance level in the conclusion.
- Compare like with like: a probability with the significance level (halved for a two-tailed test), or a \(z\)-value with the critical \(z\)-value.
- Your last sentence must be in context and must not be over-certain: "sufficient evidence to suggest", "insufficient evidence to suggest".
- For a Type II probability, the question gives the true parameter value. Use it for the distribution, but use the critical region found under \(H_0\).
- If a question says "the null hypothesis is rejected", the observed value is in the critical region, and the probability of that is the actual significance level.
:::

:::board
- **Edexcel IAL**: hypothesis tests for the binomial and Poisson distributions are in IAL S2.
- **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: the single A Level has binomial hypothesis tests, tests for the mean of a normal distribution and tests for correlation (see [Correlation and regression](#math.s.regression)). It has no Poisson tests.
:::

:::try Start easy, finish at exam standard
Q: State suitable hypotheses for each: (a) a coin is thought to be biased, (b) a spinner is thought to land on red less often than \(\tfrac14\) of the time, (c) a new drug is thought to raise the mean recovery rate above 60%.
A: (a) \(H_0: p = 0.5\), \(H_1: p \ne 0.5\) (two-tailed). (b) \(H_0: p = 0.25\), \(H_1: p < 0.25\). (c) \(H_0: p = 0.6\), \(H_1: p > 0.6\). In each case \(p\) is the probability of the event.
Q: \(X \sim B(12, 0.5)\) under \(H_0: p = 0.5\), \(H_1: p > 0.5\). Observed \(X = 10\). Test at the 5% level.
A: \(P(X \ge 10) = 0.0193\). This is less than 0.05, so reject \(H_0\). There is sufficient evidence at the 5% level to suggest \(p > 0.5\).
Q: A die is rolled 30 times and shows a six 9 times. Test at the 10% level whether the probability of a six is greater than \(\tfrac16\).
A: \(H_0: p = \tfrac16\), \(H_1: p > \tfrac16\), \(X \sim B(30, \tfrac16)\). \(P(X \ge 9) = 1 - P(X \le 8)\) \(= 0.0506\). Since \(0.0506 < 0.10\), reject \(H_0\). There is sufficient evidence at the 10% level to suggest the die is biased towards sixes.
Q: \(X \sim B(25, 0.4)\) under \(H_0: p = 0.4\). Find the critical region for a 5% one-tailed test with \(H_1: p < 0.4\), and the actual significance level.
A: \(P(X \le 5) = 0.0294\) and \(P(X \le 6) = 0.0736\). The critical region is \(X \le 5\), with actual significance level 2.94%.
Q: A factory says that 8% of its bulbs are faulty. A random sample of 30 bulbs contains 5 faulty. Test at the 5% level whether the proportion is higher.
A: \(H_0: p = 0.08\), \(H_1: p > 0.08\), \(X \sim B(30, 0.08)\). \(P(X \ge 5) = 0.0874\). This is greater than 0.05, so do not reject \(H_0\). There is insufficient evidence at the 5% level that the proportion of faulty bulbs is higher than 8%.
Q: Emails arrive at a mean rate of 3 per hour. In a random hour 8 emails arrive. Test at the 5% level whether the rate has increased.
A: \(H_0: \lambda = 3\), \(H_1: \lambda > 3\), \(X \sim \mathrm{Po}(3)\). \(P(X \ge 8) = 1 - P(X \le 7)\) \(= 0.0119\). This is less than 0.05, so reject \(H_0\): sufficient evidence to suggest the rate has increased.
Q: A coin is tossed 80 times and lands heads 50 times. Use a normal approximation to test at the 5% level whether the coin is biased towards heads.
A: \(H_0: p = 0.5\), \(H_1: p > 0.5\). \(X \approx N(40, 20)\). \(P(X \ge 50) \approx P(Y > 49.5)\), \(z = \dfrac{9.5}{\sqrt{20}} = 2.124\), probability 0.0168. This is less than 0.05, so reject \(H_0\): sufficient evidence of a bias towards heads.
Q: The mass of a sack is normal with standard deviation 2.4 kg. The claimed mean is 25 kg. A sample of 9 sacks has mean 23.9 kg. Test at the 5% level whether the mean is lower than claimed.
A: \(H_0: \mu = 25\), \(H_1: \mu < 25\). \(\bar X \sim N(25, 0.8^2)\). \(z = \dfrac{23.9 - 25}{0.8} = -1.375\), \(P(Z < -1.375) = 0.0846\). This is greater than 0.05, so do not reject \(H_0\): insufficient evidence that the mean is lower than 25 kg.
Q: Explain, in context, what a Type I error and a Type II error mean for a test of whether a new medicine is better than the old one.
A: Type I: concluding that the new medicine is better when it is not (rejecting a true \(H_0\)). Type II: concluding there is not enough evidence that it is better when it really is (failing to reject a false \(H_0\)).
Q: (Exam style) The proportion of seeds that germinate is claimed to be 0.7. A gardener plants 10 seeds and 4 germinate. (a) Test at the 5% level whether the proportion is less than claimed. (b) Find the critical region and the probability of a Type II error if the true proportion is 0.5. [8 marks]
A: (a) \(H_0: p = 0.7\), \(H_1: p < 0.7\), \(X \sim B(10, 0.7)\) [B1 B1]. \(P(X \le 4) = 0.0473\) [M1 A1]. Since \(0.0473 < 0.05\), reject \(H_0\): sufficient evidence at the 5% level to suggest the proportion that germinate is less than 0.7. [A1] (b) \(P(X \le 3) = 0.0106\) and \(P(X \le 4) = 0.0473\), so the critical region is \(X \le 4\). [M1 A1] If \(p = 0.5\), \(X \sim B(10, 0.5)\), and a Type II error occurs for \(X \ge 5\): \(P(X \ge 5) = 1 - P(X \le 4)\) \(= 1 - 0.377 = 0.623\). [A1]
Q: (Exam style) A sample of 100 values from a population with standard deviation 15 has mean 53.5. Test at the 1% significance level whether the population mean is greater than 50, and state what a Type I error would mean here. [6 marks]
A: \(H_0: \mu = 50\), \(H_1: \mu > 50\) [B1]. \(\bar X \sim N(50, 1.5^2)\) [B1]. \(z = \dfrac{3.5}{1.5} = 2.333\), \(P(Z > 2.333) = 0.00982\) [M1 A1]. Since \(0.00982 < 0.01\), reject \(H_0\): sufficient evidence at the 1% level that the mean exceeds 50. [A1] A Type I error would be concluding that the mean is greater than 50 when it is actually 50. [B1]
:::

:::eg Spot the error: one tail or two?
A student answered this question [5 marks]: "A coin is thrown 30 times and lands heads 20 times. Test at the 5% significance level whether the coin is biased."

Line 1: \(H_0: p = 0.5\), \(H_1: p \ne 0.5\), where \(p\) is the probability of heads.
Line 2: Under \(H_0\), \(X \sim B(30, 0.5)\), and \(P(X \ge 20) = 0.0494\).
Line 3: \(0.0494 < 0.05\), so reject \(H_0\). There is sufficient evidence that the coin is biased.

**Line 1 earns [B1]** and **line 2 earns [M1 A1]**. **Line 3 scores [M0 A0]**. The alternative hypothesis is two-tailed, so the 5% must be split, with 2.5% in each tail, and the student compared the upper tail with the whole 5%. Since \(0.0494 > 0.025\), the result is not significant. The student scores 3 out of 5.

Correct working: compare \(0.0494\) with \(0.025\). [M1] Since \(0.0494 > 0.025\), do not reject \(H_0\). There is insufficient evidence, at the 5% level, to suggest that the coin is biased. [A1]

**Check:** 20 heads in 30 throws is a fairly common result for a fair coin. By symmetry, 10 or fewer heads is just as likely, so being "this far from 15 in either direction" has probability about \(2 \times 0.0494 = 0.099\), almost 10%.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ A spinner is claimed to land on red with probability 0.25. Jo thinks the probability is lower. In 12 spins the spinner lands on red once. Test Jo's belief at the 5% significance level.
A: Let \(p\) be the probability of red. \(H_0: p = 0.25\), \(H_1: p < 0.25\). [B1] Under \(H_0\), \(X \sim B(12, 0.25)\), and \(P(X \le 1) = 0.1584\). [M1 A1] Since \(0.158 > 0.05\), do not reject \(H_0\). There is insufficient evidence at the 5% level to suggest that the probability of red is less than 0.25. [B1]
Q: [4 marks] ★ Rolls of cloth contain faults at random, with a mean of 3.5 faults per roll. A new supplier's roll contains 8 faults. Test, at the 5% significance level, whether the mean number of faults per roll has increased.
A: Let \(\lambda\) be the mean number of faults per roll. \(H_0: \lambda = 3.5\), \(H_1: \lambda > 3.5\). [B1] Under \(H_0\), \(X \sim \mathrm{Po}(3.5)\). [B1] \(P(X \ge 8) = 1 - P(X \le 7)\) [M1] \(= 1 - 0.9733 = 0.0267\). Since \(0.0267 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest that the mean number of faults per roll has increased. [A1]
Q: [6 marks] ★★ \(X \sim B(25, p)\) is used to test \(H_0: p = 0.4\) against \(H_1: p \ne 0.4\) at the 5% significance level. Find the critical region, and the actual significance level of the test.
A: Under \(H_0\), \(X \sim B(25, 0.4)\) and each tail has probability at most 0.025. [B1] Lower tail: \(P(X \le 4) = 0.0095\) and \(P(X \le 5) = 0.0294\), which is too big, [M1] so the lower region is \(X \le 4\). [A1] Upper tail: \(P(X \ge 16) = 0.0132\) and \(P(X \ge 15) = 0.0344\), which is too big, [M1] so the upper region is \(X \ge 16\). [A1] The critical region is \(X \le 4\) or \(X \ge 16\), and the actual significance level is \(0.00947 + 0.01317 = 0.0226\), that is 2.26%. [A1]
Q: [6 marks] ★★ A company says that 20% of its emails are marked as spam. A manager believes the proportion is higher. In a random sample of 120 emails, 33 are marked as spam. Use a normal approximation to test the manager's belief at the 5% significance level.
A: Let \(p\) be the proportion marked as spam. \(H_0: p = 0.2\), \(H_1: p > 0.2\). [B1] Under \(H_0\), \(X \sim B(120, 0.2)\), which is approximately \(N(24, 19.2)\), since \(np = 24 > 5\) and \(nq = 96 > 5\). [B1] \(P(X \ge 33) \approx P(Y > 32.5)\) [M1] with \(z = \dfrac{32.5 - 24}{\sqrt{19.2}} = 1.940\). [A1] \(1 - \Phi(1.940)\) \(= 0.0262 < 0.05\), so reject \(H_0\). [M1] There is sufficient evidence at the 5% level to suggest that the proportion of emails marked as spam is more than 20%. [A1]
Q: [6 marks] ★★ A machine makes washers with thickness that is normally distributed with standard deviation 3.2 (in hundredths of a mm). The mean is supposed to be 30. A random sample of 40 washers has mean 31.1. Test, at the 5% significance level, whether the mean has changed.
A: \(H_0: \mu = 30\), \(H_1: \mu \ne 30\), where \(\mu\) is the mean thickness. [B1] Under \(H_0\), \(\bar X \sim N\!\left(30, \dfrac{3.2^2}{40}\right)\). [B1] The standard deviation of \(\bar X\) is \(0.506\), so \(z = \dfrac{31.1 - 30}{0.506} = 2.174\). [M1 A1] This is a two-tailed test, so compare \(P(Z > 2.174) = 0.0149\) with 0.025 (or \(2.174\) with the critical value \(1.96\)). [M1] Reject \(H_0\): there is sufficient evidence at the 5% level to suggest that the mean thickness has changed. [A1]
Q: [6 marks] ★★ A call centre receives complaints at random. A test of \(H_0: \lambda = 2\) against \(H_1: \lambda > 2\), where \(\lambda\) is the mean number of complaints in an hour, uses the critical region \(X \ge 6\) for the number \(X\) of complaints in a randomly chosen hour. (a) Find the probability of a Type I error. (b) Find the probability of a Type II error when the true mean is 4. (c) Explain in context what a Type II error means here.
A: (a) Under \(H_0\), \(X \sim \mathrm{Po}(2)\). \(P(X \ge 6) = 1 - P(X \le 5)\) [M1] \(= 1 - 0.9834 = 0.0166\). [A1] (b) If \(\lambda = 4\), \(X \sim \mathrm{Po}(4)\). [B1] A Type II error is not rejecting, which means \(X \le 5\): [M1] \(P(X \le 5) = 0.785\). [A1] (c) The manager concludes that there is no evidence that the mean number of complaints per hour has increased, when it really has. [B1]
Q: [10 marks] (#math.s2.sampling) ★★★ A machine fills packets with a normally distributed mass, with standard deviation 4 g. The mean is supposed to be 250 g. A manager suspects that the mean is lower, and tests \(H_0: \mu = 250\) against \(H_1: \mu < 250\) at the 5% level, using the mean of a random sample of 25 packets. (a) Find the critical region for the sample mean. (b) Find the probability of a Type II error if the true mean is 248 g. (c) The manager wants this Type II probability to be below 0.1 using a larger sample, with the same critical-region rule at the 5% level. Find the smallest sample size \(n\).
H: Under \(H_0\), \(\bar X \sim N\!\left(250, \dfrac{4^2}{n}\right)\). The critical region is \(\bar X < 250 - 1.645\dfrac{4}{\sqrt{n}}\).
H: A Type II error means the sample mean is not in the critical region, even though the true mean is 248. Use \(\bar X \sim N(248, \dots)\) with the same standard deviation.
H: For (c), write the Type II probability as \(P(\bar X \ge c)\) for \(\bar X \sim N(248, 16/n)\), and require \(\dfrac{c - 248}{4/\sqrt{n}} > 1.282\). Test values of \(n\) near 34.
A: (a) Under \(H_0\), \(\bar X \sim N\!\left(250, \dfrac{16}{25}\right)\), with standard deviation 0.8. [B1] The critical region is \(\bar X < 250 - 1.645 \times 0.8\) [M1] \(= 248.7\) (to 3 s.f.; exactly 248.68). [A1] (b) If \(\mu = 248\), \(\bar X \sim N(248, 0.8^2)\). [B1] A Type II error occurs when \(\bar X \ge 248.68\): \(P(\bar X \ge 248.68)\) \(= P\!\left(Z \ge \dfrac{0.684}{0.8}\right)\) [M1] \(= P(Z \ge 0.855) = 0.196\). [A1] (c) For general \(n\), the critical value is \(c = 250 - 1.645\dfrac{4}{\sqrt{n}}\), and the Type II probability is \(P\!\left(Z \ge \dfrac{c - 248}{4/\sqrt{n}}\right)\). [M1] We need \(\dfrac{c - 248}{4/\sqrt{n}} > 1.282\), that is \(\dfrac{\sqrt{n}}{4}\left(2 - \dfrac{6.58}{\sqrt{n}}\right) > 1.282\), so \(0.5\sqrt{n} - 1.645 > 1.282\). [M1] This gives \(\sqrt{n} > 5.854\), so \(n > 34.3\). [A1] The smallest sample size is \(n = 35\). [A1] Check: for \(n = 35\) the Type II probability is 0.0946, and for \(n = 34\) it is 0.1019.
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A coin is thrown \(n\) times and a one-tailed test at the 5% level is used for \(H_0: p = 0.5\) against \(H_1: p > 0.5\), where \(p\) is the probability of heads. (a) Show that the test can never reject \(H_0\) if \(n = 4\), and find the smallest \(n\) for which it can reject. (b) For \(n = 10\), find the critical region and the actual significance level. (c) For \(n = 10\), find the probability of a Type II error when the coin is in fact biased with \(p = 0.8\), and comment.
H: The most extreme result for \(H_1: p > 0.5\) is that every throw is a head. What is its probability under \(H_0\)?
H: For (b) and (c), use \(X \sim B(10, 0.5)\) under \(H_0\) and \(X \sim B(10, 0.8)\) when \(p = 0.8\).
A: (a) The most extreme result is \(n\) heads out of \(n\), with probability \(0.5^n\). For \(n = 4\) this is \(0.0625 > 0.05\), so even four heads out of four is not significant. [M1 A1] For \(n = 5\) it is \(0.5^5 = 0.03125 < 0.05\), so the smallest \(n\) is 5. [A1] (b) \(P(X \ge 9) = 0.0107\) and \(P(X \ge 8) = 0.0547 > 0.05\). [M1] The critical region is \(X \ge 9\) and the actual significance level is 1.07%. [A1] (c) A Type II error occurs when \(X \le 8\). With \(p = 0.8\), \(P(X \le 8)\) \(= 1 - P(X = 9) - P(X = 10)\) \(= 1 - 0.3758 = 0.624\). [M1 A1] The test misses a coin this biased about 62% of the time. With only 10 throws the test is weak, and a larger \(n\) is needed to detect a bias of this size. [B1]
Q: [4 marks] ★★★ A researcher carries out 20 independent hypothesis tests, each at the 5% significance level, on data where \(H_0\) is true every time. (a) State the distribution of the number of tests that reject \(H_0\). (b) Find the probability that at least one test rejects \(H_0\). (c) What does this suggest about a researcher who reports only the tests that "worked"?
H: Each test rejects a true \(H_0\) with probability equal to the significance level, independently of the others.
H: "At least one" is the complement of "none": find \(P(R = 0) = 0.95^{20}\) first.
A: (a) The number of rejections is \(R \sim B(20, 0.05)\). [B1] (b) \(P(R \ge 1) = 1 - 0.95^{20}\) [M1] \(= 0.642\). [A1] (c) Even when nothing is going on, a "significant" result is more likely than not (about a 64% chance). Reporting only those tests gives a misleading picture of the evidence. [B1]
:::

:::quiz Check your understanding
? What does the significance level of a test measure?
- the probability that \(H_0\) is true
+ the probability of rejecting \(H_0\) when it is true
- the probability of a Type II error
- the probability that \(H_1\) is true
> The significance level is the chance of a Type I error: rejecting a true null hypothesis. It is not the probability that either hypothesis is true.
? A coin is tested with \(H_0: p = 0.5\), \(H_1: p \ne 0.5\) at the 5% level. Each tail of the critical region should have probability at most:
- 5%
+ 2.5%
- 10%
- 1%
> A two-tailed test splits the significance level between the two tails: 2.5% each.
? The observed value is \(X = 15\) in a test of \(H_1: p > 0.5\) with \(X \sim B(20, 0.5)\). Which probability do you calculate?
- \(P(X = 15)\)
- \(P(X \le 15)\)
+ \(P(X \ge 15)\)
- \(1 - P(X \ge 15)\)
> The "at least as extreme" tail in the direction of \(H_1\) is \(P(X \ge 15)\). The single point probability misses the more extreme values.
? A test does not reject \(H_0\). Which conclusion is correct?
- \(H_0\) is true
- \(H_1\) is false
+ there is insufficient evidence to reject \(H_0\) at this significance level
- the sample is wrong
> A test can only fail to find evidence. It never proves \(H_0\). The conclusion should say there is insufficient evidence for \(H_1\), in context.
? A Type II error is:
- rejecting \(H_0\) when \(H_0\) is true
+ not rejecting \(H_0\) when \(H_0\) is false
- rejecting \(H_1\) when \(H_1\) is true
- accepting a result that is not significant
> Type II means failing to detect a real effect. Rejecting a true \(H_0\) is a Type I error.
? A two-tailed test at the 5% level gives an upper-tail probability of 0.04. What is the conclusion?
- Reject \(H_0\), because \(0.04 < 0.05\).
+ Do not reject \(H_0\), because \(0.04 > 0.025\).
- Reject \(H_0\), because \(0.04 < 0.10\).
- Accept that \(H_0\) is true.
> In a two-tailed test each tail gets half the significance level, 0.025. A tail probability of 0.04 is too large to reject, but that does not prove \(H_0\) is true.
? To find the probability of a Type II error you calculate a probability using:
- the null value of the parameter, \(H_0\)
+ a specific value of the parameter for which \(H_1\) is true, and the acceptance region
- the observed value of the test statistic
- the significance level only
> A Type II error is not rejecting when \(H_0\) is false, so you need a particular true value (given in the question) and the probability of landing in the acceptance region under it. Using the null value gives the probability of a correct decision, not an error.
:::

:::checklist What you can now do
- [ ] I can write \(H_0\) and \(H_1\) correctly, define the parameter, and decide between a one-tailed and a two-tailed test.
- [ ] I can test a binomial probability from one observation, using a direct probability or a critical region.
- [ ] I can test a Poisson mean, rescaling \(\lambda\) to the interval observed.
- [ ] I can use a normal approximation, with a continuity correction, in a binomial or Poisson test.
- [ ] I can test a population mean for a normal population with known variance, or with a large sample.
- [ ] I can find a critical region and its actual significance level, halving the level for a two-tailed test.
- [ ] I can write a conclusion in context, using "sufficient evidence" or "insufficient evidence", and never "accept \(H_0\) as true".
- [ ] I can explain Type I and Type II errors in context and find the probability of each.
:::

:::recap
- \(H_0\) states one value of the parameter (with \(=\)). \(H_1\) is \(<\), \(>\) (one-tailed) or \(\ne\) (two-tailed). Assume \(H_0\), find the probability of the result or more extreme, compare with the significance level (halved in each tail of a two-tailed test).
- Critical region: the largest tail whose probability does not exceed the significance level. The actual significance level is its probability under \(H_0\).
- Binomial: \(X \sim B(n, p_0)\). Poisson: \(X \sim \mathrm{Po}(\lambda_0)\), rescaled to the observed interval. Large \(n\) or \(\lambda > 15\): normal approximation with a continuity correction.
- Mean: \(\bar X \sim N(\mu_0, \sigma^2/n)\) under \(H_0\) (normal population with known variance, or large sample using \(s^2\)). Standardise with \(\sigma/\sqrt{n}\).
- Conclude in context: "sufficient evidence to suggest" or "insufficient evidence to suggest". Never "\(H_0\) is true".
- Type I error: rejecting a true \(H_0\); probability is the actual significance level. Type II: not rejecting a false \(H_0\); probability is found using a stated true parameter value and the acceptance region.
:::

:::links
- watch: [Type I and Type II errors](https://www.examsolutions.net/tutorials/type-i-error-and-type-ii-errors/) · ExamSolutions · what each error means and its probability
- watch: [Exam questions: binomial hypothesis tests](https://www.examsolutions.net/tutorials/exam-questions-hypothesis-tests-binomial-distribution/) · ExamSolutions · exam-style questions solved on video
- practise: [CAIE S2 hypothesis testing exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/topic-questions/hypothesis-testing/hypothesis-testing/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) · Khan Academy · the significance tests unit
- explore: [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory · p-values and intervals you can simulate
- papers: [9709 Paper 6 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-7/) · Physics & Maths Tutor · papers with mark schemes [unofficial]

Links checked 3 October 2026.
:::
Next: [Correlation and regression](#math.s.regression).
