@chapter math.s2.sampling
@title Sampling and estimation
@level a2
@paper CAIE P6 (S2) · Edexcel IAL S3 · UK Further Maths Statistics
@time 6–8 hours
@summary You rarely measure a whole population, so you learn about it from a sample. You will learn what makes a sample random, why the sample mean \(\bar X\) is itself a random variable with mean \(\mu\) and variance \(\sigma^2/n\), the central limit theorem, unbiased estimates of the mean and variance, and confidence intervals for a population mean and a population proportion.

:::why
Opinion polls, quality checks and medical trials all work the same way. Nobody can ask every voter, test every bulb or treat every patient, so you take a sample and use it to say something about everyone, together with an honest statement of how uncertain that is. This chapter shows how to do that: what makes a sample trustworthy, how much sample means vary, and how to give a range that is likely to contain the true value.
:::

**Before you start**, you need \(E(X)\) and \(\mathrm{Var}(X)\) from [Discrete random variables](#math.s1.drv), the normal distribution from [The normal distribution](#math.s1.normal), and the rules for sums and multiples of random variables from [Linear combinations of random variables](#math.s2.linear). Mean and standard deviation of data are in [Representing and summarising data](#math.s1.data).

## Populations and samples

:::def Population and sample
The **population** is the whole collection of items you want to know about (all the bulbs a factory makes, all the voters in a country). A **sample** is a smaller group taken from the population and measured. A **census** measures every item in the population.
:::

A census is often impossible or silly: it can cost too much, take too long, or destroy the items (you cannot test the lifetime of every bulb by running it until it fails). So we sample. A sample is only useful if it **represents** the population, and the way to achieve that is randomness.

:::def Random sample
A sample in which every member of the population has the same chance of being chosen, and in which the choices are independent of each other.
:::

A non-random method gives a **biased** sample: one that is likely to be unrepresentative in a particular direction. Common faults:

- **Convenient groups.** Asking only your friends, or the first 30 people to arrive, picks people who are not typical.
- **Self-selection.** A phone-in or online poll collects only those who care enough to reply, usually those with strong views.
- **Wrong place or time.** A survey about exercise carried out in a gym will overstate how much the population exercises.
- **A list that is incomplete.** Choosing names from a phone book misses people with no landline.

:::eg A head teacher wants to know how many hours students sleep. She asks the first 30 students to reach school on Monday. Give two reasons why this is an unsatisfactory sample.
The sample is not random: students who arrive first may live close to school, or travel by a particular bus, so they may sleep differently from the rest. Only one day is used, and Monday may not be typical. Only 30 students are asked, so the sample may be too small to represent the whole school, and some students are certain to have no chance of being picked.
:::

### Using random numbers

To take a random sample you need every member to have the same chance, and a computer or calculator can supply random numbers.

:::steps
1. List or number the population, for example 1 to 80 (or 01 to 80).
2. Generate random numbers with the same number of digits, for example two-digit numbers.
3. Ignore any number outside the list (such as 00 or 91 to 99) and any repeat of a number already chosen.
4. Continue until you have the sample size you need, then select the members with those numbers.
:::

:::eg A company has 80 employees. Describe how to use random numbers to select a sample of 5.
Number the employees 01 to 80. Generate two-digit random numbers. If a number is 00, or greater than 80, or has already been chosen, ignore it. Continue until 5 different numbers between 01 and 80 have been chosen, and select the employees with those numbers.
:::

## The sample mean as a random variable

Take a sample of \(n\) values from a population with mean \(\mu\) and variance \(\sigma^2\), and work out its mean \(\bar x\). Take another sample and you get a different \(\bar x\). So before you take the sample, the mean is a random variable, written \(\bar X\).

:::def Sampling distribution of the mean
The distribution of the sample mean \(\bar X\) over all possible samples of size \(n\) from the population.
:::

The rules for combining variables give the mean and variance of \(\bar X\) at once. Let \(X_1, \dots, X_n\) be independent observations of \(X\), where \(E(X) = \mu\) and \(\mathrm{Var}(X) = \sigma^2\). Then \(X_1 + \dots + X_n\) has mean \(n\mu\) and variance \(n\sigma^2\). Dividing by \(n\) multiplies the mean by \(\tfrac1n\) and the variance by \(\tfrac{1}{n^2}\):
\[E(\bar X) = \frac{n\mu}{n} = \mu \qquad \mathrm{Var}(\bar X) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}\]

:::key Distribution of the sample mean
For a random sample of size \(n\) from a population with mean \(\mu\) and variance \(\sigma^2\):
\[E(\bar X) = \mu \qquad \mathrm{Var}(\bar X) = \frac{\sigma^2}{n} \qquad \text{standard deviation of } \bar X = \frac{\sigma}{\sqrt{n}}\]
- **If \(X\) is normal**, then \(\bar X \sim N\!\left(\mu, \dfrac{\sigma^2}{n}\right)\) exactly, for any \(n\).
- **Central limit theorem**: if \(n\) is large, \(\bar X\) is approximately \(N\!\left(\mu, \dfrac{\sigma^2}{n}\right)\) **whatever the shape of the population**. A sample of 30 or more is usually treated as large.
- The variance of \(\bar X\) shrinks as \(n\) grows: means of big samples are more reliable than single values.
:::

The result \(\bar X \sim N(\mu, \sigma^2/n)\) is on MF19. The sentence "the sample mean is normal because the sample is large" earns a mark in an exam, so say it.

:::plot A single value \(X \sim N(100, 15^2)\) is spread out. The mean of a sample of 9 has the same centre but standard deviation \(15/\sqrt{9} = 5\), so it is three times narrower.
--f "exp(-((x-100)**2)/(2*225))/sqrt(2*pi*225)" --f "exp(-((x-100)**2)/(2*25))/sqrt(2*pi*25)" --label "X, standard deviation 15" --label "mean of 9, standard deviation 5" --x 55 145 --y 0 0.09 --legend tl
:::

:::eg \(X \sim N(100, 15^2)\). Find (a) \(P(X > 105)\) and (b) the probability that the mean of a random sample of 9 observations exceeds 105.
(a) \(P(X > 105) = P\!\left(Z > \dfrac{105 - 100}{15}\right) = P(Z > 0.333) = 0.369\).

(b) \(\bar X \sim N\!\left(100, \dfrac{15^2}{9}\right) = N(100, 5^2)\), so
\[P(\bar X > 105) = P\!\left(Z > \frac{105 - 100}{5}\right) = P(Z > 1) = 0.159\]
A mean of 9 values is much less likely than a single value to be far from \(\mu\).
:::

:::eg The waiting time \(T\) minutes for a train has mean \(\dfrac{10}{3}\) and variance \(\dfrac{50}{9}\), and a distribution that is not normal (the pdf is \((10 - t)/50\), see [Continuous random variables](#math.s2.crv)). The mean of 50 independent waiting times is \(\bar T\). Find \(P(\bar T > 4)\).
The sample size is large, so by the central limit theorem \(\bar T\) is approximately normal, with
\[E(\bar T) = \frac{10}{3}, \qquad \mathrm{Var}(\bar T) = \frac{50/9}{50} = \frac19\]
So \(\bar T \approx N\!\left(\dfrac{10}{3}, \left(\dfrac13\right)^2\right)\) and
\[P(\bar T > 4) = P\!\left(Z > \frac{4 - 10/3}{1/3}\right) = P(Z > 2) = 0.0228\]
:::

:::warn \(\sigma^2/n\) slips
- The standard deviation of \(\bar X\) is \(\sigma/\sqrt{n}\), not \(\sigma/n\), and not \(\sigma^2/n\) (that is the variance).
- Put the **variance** \(\sigma^2/n\) as the second parameter of \(N(\cdot,\cdot)\), but divide by the **standard deviation** \(\sigma/\sqrt{n}\) when standardising.
- A question about one item uses \(X\) with \(\sigma\). A question about the mean of a sample uses \(\bar X\) with \(\sigma/\sqrt{n}\). Read which one is asked.
:::

## Unbiased estimates of the population mean and variance

Usually \(\mu\) and \(\sigma^2\) are unknown, and you **estimate** them from a sample.

:::def Unbiased estimator
A statistic is an unbiased estimator of a population parameter if its expected value equals the parameter. In simple terms, it is right on average: it does not tend to be too high or too low.
:::

The sample mean \(\bar x\) is an unbiased estimate of \(\mu\), since \(E(\bar X) = \mu\). The variance needs more care. The spread of a sample about its own mean \(\bar x\) is on average smaller than the spread of the population about \(\mu\), because \(\bar x\) sits in the middle of the sample. Dividing by \(n - 1\) instead of \(n\) corrects for this.

:::key Unbiased estimates from a sample
For a sample \(x_1, \dots, x_n\):
\[\bar x = \frac{\sum x}{n} \qquad s^2 = \frac{1}{n - 1}\sum (x - \bar x)^2 = \frac{1}{n - 1}\left(\sum x^2 - \frac{(\sum x)^2}{n}\right)\]
- \(\bar x\) is an unbiased estimate of \(\mu\). \(s^2\) is an unbiased estimate of \(\sigma^2\).
- The sample variance with divisor \(n\) is **not** the unbiased estimate.
- Both estimators are on MF19. On a calculator, \(s\) is the "\(\sigma_{n-1}\)" or "\(s_x\)" key.
- Use \(s^2\) in place of \(\sigma^2\) when \(\sigma^2\) is unknown (for large samples).
:::

:::eg Find unbiased estimates of the population mean and variance from the sample 12, 15, 11, 18, 14.
\(n = 5\) and \(\sum x = 70\), so \(\bar x = 14\).
\[\sum (x - \bar x)^2 = (-2)^2 + 1^2 + (-3)^2 + 4^2 + 0^2 = 4 + 1 + 9 + 16 + 0 = 30\]
\[s^2 = \frac{30}{5 - 1} = 7.5\]
If you had divided by 5 you would get 6, which is too small on average.
:::

:::eg A sample of 25 observations has \(\sum x = 300\) and \(\sum x^2 = 3900\). Find unbiased estimates of the population mean and variance.
\[\bar x = \frac{300}{25} = 12 \qquad s^2 = \frac{1}{24}\left(3900 - \frac{300^2}{25}\right) = \frac{3900 - 3600}{24} = \frac{300}{24} = 12.5\]
:::

## Confidence intervals for a mean

A single estimate \(\bar x\) will not equal \(\mu\) exactly. A **confidence interval** gives a range that is likely to contain \(\mu\).

Suppose \(X\) is normal with known standard deviation \(\sigma\), so \(\bar X \sim N(\mu, \sigma^2/n)\). For a 95% interval, find \(z\) with \(P(-z < Z < z) = 0.95\), which is \(z = 1.96\). Then with probability 0.95,
\[\mu - 1.96\frac{\sigma}{\sqrt{n}} < \bar X < \mu + 1.96\frac{\sigma}{\sqrt{n}}\]
Rearranging, \(\mu\) lies within \(1.96\,\sigma/\sqrt{n}\) of \(\bar X\). With the observed value \(\bar x\) this gives the interval below.

:::key Confidence interval for a population mean
For a sample of size \(n\) with mean \(\bar x\), the \(c\%\) confidence interval for \(\mu\) is
\[\bar x - z\frac{\sigma}{\sqrt{n}} \;<\; \mu \;<\; \bar x + z\frac{\sigma}{\sqrt{n}}\]
where \(z\) satisfies \(P(-z < Z < z) = c/100\).

| Confidence | 90% | 95% | 98% | 99% |
|---|---|---|---|---|
| \(z\) | 1.645 | 1.960 | 2.326 | 2.576 |

- Use when the population is **normal with known \(\sigma\)** (any \(n\)), or when \(n\) is **large** (use \(s\) for \(\sigma\) if \(\sigma\) is unknown).
- The formula is not on MF19: learn it, and learn how to find \(z\) from the table of the normal distribution.
- The margin of error is \(z\sigma/\sqrt{n}\); the interval has width \(2z\sigma/\sqrt{n}\).
:::

:::eg Bags of flour have masses that are normal with standard deviation 12 g. A random sample of 36 bags has mean mass 502 g. Find a 95% confidence interval for the mean mass of all bags.
\[\frac{\sigma}{\sqrt{n}} = \frac{12}{6} = 2\]
\[502 \pm 1.96 \times 2 = 502 \pm 3.92\]
The 95% confidence interval is \(498 < \mu < 506\) (3 s.f.; exactly \(498.08\) to \(505.92\)).
:::

:::eg A large sample of 80 items has mean 34.2 and unbiased variance estimate \(s^2 = 5.6^2\). Find a 98% confidence interval for the population mean.
The sample is large, so use \(s\) in place of \(\sigma\). \(\dfrac{5.6}{\sqrt{80}} = 0.6261\) and \(z = 2.326\).
\[34.2 \pm 2.326 \times 0.6261 = 34.2 \pm 1.456\]
The 98% confidence interval is \(32.7 < \mu < 35.7\).
:::

### Reading and using a confidence interval

:::warn What "95% confident" means
The population mean \(\mu\) is a fixed number. It is the interval that changes from sample to sample. A 95% confidence interval means: **if you took many samples and made an interval from each in the same way, about 95% of the intervals would contain \(\mu\)**. Do not say "95% of the population is in the interval", and avoid "there is a 95% chance \(\mu\) is in this interval" in an exam unless you phrase it as the method's success rate.
:::

How the width changes:

- **A higher confidence level** (99% instead of 95%) gives a larger \(z\), so a wider interval. You buy more certainty with less precision.
- **A larger sample size** \(n\) gives a narrower interval, since the width is proportional to \(1/\sqrt{n}\). To halve the width you need four times the sample.
- **A larger \(\sigma\)** gives a wider interval.

:::eg The standard deviation of a population is 8. How large a sample is needed so that a 95% confidence interval for the mean has width at most 2?
The width is \(2 \times 1.96 \times \dfrac{8}{\sqrt{n}} \le 2\), so \(\sqrt{n} \ge 15.68\) and \(n \ge 245.9\).
Round **up**: the smallest sample is \(n = 246\).
:::

:::eg A 95% confidence interval for the mean of a normal population, based on a sample of 25 with known standard deviation \(\sigma\), is \((48.2, 51.8)\). Find the sample mean and \(\sigma\).
The interval is symmetrical about the sample mean, so \(\bar x\) is the midpoint:
\[\bar x = \frac{48.2 + 51.8}{2} = 50\]
The margin of error is half the width: \(51.8 - 50 = 1.8\). So
\[1.96 \times \frac{\sigma}{\sqrt{25}} = 1.8 \quad\Rightarrow\quad \sigma = \frac{1.8 \times 5}{1.96} = 4.59\]
:::

## Confidence intervals for a proportion

Sometimes the quantity of interest is a proportion \(p\) of the population with some property (voters who support a party, items that are faulty). In a sample of \(n\), let \(X\) be the number with the property and \(\hat p = X/n\) the **sample proportion**. Since \(X \sim B(n, p)\) and a large binomial is approximately normal,
\[\hat p \approx N\!\left(p, \frac{p(1 - p)}{n}\right)\]
This is on MF19. The true \(p\) is unknown, so in the interval we replace it by \(\hat p\).

:::key Approximate confidence interval for a proportion
From a large sample with sample proportion \(\hat p\), an approximate \(c\%\) confidence interval for \(p\) is
\[\hat p - z\sqrt{\frac{\hat p(1 - \hat p)}{n}} \;<\; p \;<\; \hat p + z\sqrt{\frac{\hat p(1 - \hat p)}{n}}\]
with \(z\) from the same table as before. This interval is not on MF19: learn it.
:::

:::eg In a random sample of 200 voters, 56 say they will vote for party A. Find an approximate 95% confidence interval for the proportion of all voters who support A.
\(\hat p = \dfrac{56}{200} = 0.28\).
\[\sqrt{\frac{0.28 \times 0.72}{200}} = 0.03175\]
\[0.28 \pm 1.96 \times 0.03175 = 0.28 \pm 0.0622\]
The interval is \(0.218 < p < 0.342\).
:::

:::eg In a random sample of 500 people, 240 support a new road. Find a 90% confidence interval for the proportion who support it. Does the interval show that a majority of the population supports the road?
\(\hat p = 0.48\), \(\sqrt{\dfrac{0.48 \times 0.52}{500}} = 0.02234\), \(z = 1.645\).
\[0.48 \pm 1.645 \times 0.02234 = 0.48 \pm 0.0368\]
The interval is \(0.443 < p < 0.517\). It includes values both below and above 0.5, so the sample does not show that a majority supports the road.
:::

## Exam-style questions

:::eg (Exam style) The time \(T\) seconds for a robot to complete a task has a mean \(\mu\) and a standard deviation of 4.5. A random sample of 60 times has \(\sum t = 1830\) and \(\sum t^2 = 57\,000\). (a) Find unbiased estimates of the population mean and variance. (b) Find a 95% confidence interval for \(\mu\), using your estimate of the variance. (c) The manufacturer claims \(\mu = 30\). Comment. [8 marks]
(a) \(\bar t = \dfrac{1830}{60} = 30.5\). [B1]
\[s^2 = \frac{1}{59}\left(57\,000 - \frac{1830^2}{60}\right) = \frac{57\,000 - 55\,815}{59} = \frac{1185}{59} = 20.08\] [M1 A1]

(b) The sample is large, so \(\bar T\) is approximately normal and we can use \(s\) for \(\sigma\). [B1] \(\dfrac{s}{\sqrt{n}} = \sqrt{\dfrac{20.08}{60}} = 0.5786\).
\[30.5 \pm 1.96 \times 0.5786 = 30.5 \pm 1.13\] [M1]
The interval is \(29.4 < \mu < 31.6\). [A1]

(c) The value 30 is inside the interval, so the data are consistent with the claim \(\mu = 30\). [B1 B1: inside the interval, and "consistent", not "proves".]
:::

:::eg (Exam style) The mass of a certain type of biscuit has a population mean of 25 g and standard deviation 8 g, and a distribution that is not normal. A packet contains 64 biscuits, which you may treat as a random sample. Find the probability that the mean mass of the biscuits in a packet exceeds 26.5 g. Explain why you can use a normal distribution. [5 marks]
The sample is large (64), so by the central limit theorem \(\bar X\) is approximately normal. [B1]
\[E(\bar X) = 25, \qquad \mathrm{Var}(\bar X) = \frac{8^2}{64} = 1\] [B1]
\[P(\bar X > 26.5) = P\!\left(Z > \frac{26.5 - 25}{1}\right) = P(Z > 1.5)\] [M1 A1]
\[= 1 - 0.9332 = 0.0668\] [A1]
:::

:::eg (Exam style) A machine fills bags of nuts. The mass \(X\) g is normally distributed with standard deviation 9 g. A sample of 16 bags has mean 502.5 g. (a) Find a 95% confidence interval for the mean mass. (b) Find the smallest sample size for which the width of a 95% confidence interval is less than 4 g. [6 marks]
(a) \(\dfrac{9}{\sqrt{16}} = 2.25\), so \(502.5 \pm 1.96 \times 2.25 = 502.5 \pm 4.41\). [M1 A1] The interval is \((498, 507)\). [A1]

(b) \(2 \times 1.96 \times \dfrac{9}{\sqrt{n}} < 4\) [M1], so \(\sqrt{n} > 8.82\) and \(n > 77.8\). [A1] The smallest sample size is \(n = 78\). [A1]
:::

:::exam Technique
- State why your method is valid: "normal population with known variance", or "\(n\) is large, so by the central limit theorem \(\bar X\) is approximately normal".
- Use \(\sigma^2/n\) for the variance of \(\bar X\), and quote the confidence interval with the inequality \(a < \mu < b\) or as a bracket pair, to 3 s.f.
- When asked to comment on a claimed value, say whether it lies inside the interval, and word the conclusion in context: "consistent with" or "does not support".
- Always round a required sample size **up**.
:::

:::board
- **Edexcel IAL**: sampling and confidence intervals are in IAL S3. IAL also names sampling methods, which CAIE does not test.
- **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: the single A Level covers sampling methods by name and hypothesis tests, but not confidence intervals or the central limit theorem. Those are in UK Further Maths.
:::

:::try Start easy, finish at exam standard
Q: A radio phone-in asks listeners "Do you think the council wastes money?". Give two reasons why the result is not representative of all residents.
A: Listeners who phone in choose themselves, and tend to be those with strong views, so the sample is self-selected. Not all residents listen to that station, so some have no chance of being included.
Q: Describe how to use random numbers to choose a sample of 4 pupils from a list of 60.
A: Number the pupils 01 to 60. Generate two-digit random numbers. Ignore 00, numbers above 60 and repeats. Continue until four different numbers from 01 to 60 are found, and choose those pupils.
Q: \(X \sim N(50, 12^2)\). Find the distribution of the mean \(\bar X\) of 9 independent observations, and \(P(\bar X > 54)\).
A: \(\bar X \sim N\!\left(50, \tfrac{144}{9}\right) = N(50, 16)\). \(P(\bar X > 54) = P\!\left(Z > \tfrac{4}{4}\right) = P(Z > 1) = 0.159\).
Q: A population has mean 20 and standard deviation 6 (shape unknown). The mean \(\bar X\) of a sample of 100 is taken. Find \(P(\bar X < 19)\) and explain why a normal distribution can be used.
A: \(n = 100\) is large, so by the central limit theorem \(\bar X \approx N(20, 0.36)\). \(P(\bar X < 19) = P\!\left(Z < \tfrac{-1}{0.6}\right) = \Phi(-1.667) = 0.0478\).
Q: Find unbiased estimates of the population mean and variance from the sample 8, 11, 9, 14, 13, 10.
A: \(\sum x = 65\), \(\bar x = 10.83\). \(\sum x^2 = 731\). \(s^2 = \tfrac15\left(731 - \tfrac{65^2}{6}\right) = \tfrac{26.83}{5} = 5.37\).
Q: A sample of 50 values has \(\sum x = 620\) and \(\sum x^2 = 8100\). Find unbiased estimates of \(\mu\) and \(\sigma^2\).
A: \(\bar x = 12.4\). \(s^2 = \tfrac{1}{49}\left(8100 - \tfrac{620^2}{50}\right) = \tfrac{412}{49} = 8.41\).
Q: A normal population has standard deviation 5. A sample of 25 has mean 48. Find a 90% confidence interval for the population mean.
A: \(\tfrac{5}{\sqrt{25}} = 1\). \(48 \pm 1.645 \times 1 = 48 \pm 1.645\), so \(46.4 < \mu < 49.6\).
Q: A large sample of 64 has mean 120 and unbiased variance estimate \(16^2\). Find a 99% confidence interval for the population mean, and say what happens to its width if the sample size is quadrupled.
A: \(\tfrac{16}{\sqrt{64}} = 2\). \(120 \pm 2.576 \times 2 = 120 \pm 5.152\), so \(114.8 < \mu < 125.2\). The width is proportional to \(1/\sqrt{n}\). Quadrupling \(n\) doubles \(\sqrt{n}\), so the width is halved.
Q: In a random sample of 250 customers, 100 say they are satisfied. Find an approximate 95% confidence interval for the proportion of all customers who are satisfied.
A: \(\hat p = 0.4\). \(\sqrt{\tfrac{0.4 \times 0.6}{250}} = 0.03098\). \(0.4 \pm 1.96 \times 0.03098 = 0.4 \pm 0.0607\), so \(0.339 < p < 0.461\).
Q: A student says "A 95% confidence interval for the mean is \((40, 44)\), so 95% of all the values in the population lie between 40 and 44". Explain the mistake.
A: The interval is for the **mean** of the population, not for individual values. Individual values vary far more than the mean of a sample. The correct meaning is that 95% of intervals constructed in this way would contain the true mean.
Q: (Exam style) The heights of a type of plant are normally distributed with standard deviation 6.5 cm. A sample of 40 plants has mean height 52.4 cm. (a) Find a 99% confidence interval for the mean height. (b) A gardener says the mean height is 56 cm. Comment. [5 marks]
A: (a) \(\tfrac{6.5}{\sqrt{40}} = 1.0277\). \(52.4 \pm 2.576 \times 1.0277 = 52.4 \pm 2.647\), so \(49.8 < \mu < 55.0\). [M1 A1 A1] (b) 56 is outside the interval, so the data do not support the gardener's claim. [B1 B1]
:::

:::quiz Check your understanding
? A sample has \(n = 5\) and \(\sum (x - \bar x)^2 = 30\). What is the unbiased estimate of the population variance?
+ 7.5
- 6
- 5
- 30
> Divide by \(n - 1 = 4\): \(30/4 = 7.5\). Dividing by 5 gives 6, which tends to be too small.
? A population has standard deviation 12. What is the standard deviation of the mean of samples of size 16?
- 12
- 0.75
+ 3
- 9
> \(\sigma/\sqrt{n} = 12/4 = 3\). The value 0.75 comes from dividing by 16 instead of \(\sqrt{16}\).
? Which statement about a 95% confidence interval for \(\mu\) is correct?
- 95% of the population lies in the interval
- 95% of sample means lie in the interval
+ about 95% of intervals made in this way from different samples would contain \(\mu\)
- \(\mu\) is a random variable that falls in the interval with probability 0.95
> The population mean is a fixed number. It is the interval that varies from sample to sample, and about 95% of such intervals capture \(\mu\).
? The sample size is increased and the confidence level stays at 95%. The confidence interval becomes:
- wider
+ narrower
- the same width
- no longer valid
> The width is \(2z\sigma/\sqrt{n}\), which falls as \(n\) grows. A higher confidence level, not a larger \(n\), is what widens an interval.
? A population is strongly skewed with mean \(\mu\) and variance \(\sigma^2\). For \(n = 60\), the distribution of \(\bar X\) is approximately:
- skewed in the same way as \(X\)
- \(N(\mu, \sigma^2)\)
+ \(N\!\left(\mu, \dfrac{\sigma^2}{60}\right)\)
- \(N\!\left(\mu, \dfrac{\sigma}{60}\right)\)
> The central limit theorem makes \(\bar X\) approximately normal for large \(n\), with variance \(\sigma^2/n\). The population's skew disappears in the mean.
:::

:::recap
- A random sample gives every member an equal chance and independent selection; convenient or self-selected samples are biased. Use random numbers: number the list, ignore out-of-range numbers and repeats.
- \(E(\bar X) = \mu\) and \(\mathrm{Var}(\bar X) = \sigma^2/n\). \(\bar X\) is exactly \(N(\mu, \sigma^2/n)\) for a normal population and approximately so for large \(n\) (central limit theorem).
- Unbiased estimates: \(\bar x\) for \(\mu\) and \(s^2 = \dfrac{1}{n - 1}\left(\sum x^2 - \dfrac{(\sum x)^2}{n}\right)\) for \(\sigma^2\).
- Confidence interval for a mean: \(\bar x \pm z\sigma/\sqrt{n}\) (known \(\sigma\), or large \(n\) with \(s\)). \(z = 1.645, 1.960, 2.326, 2.576\) for 90%, 95%, 98%, 99%.
- Confidence interval for a proportion: \(\hat p \pm z\sqrt{\hat p(1 - \hat p)/n}\) for large \(n\).
- A higher confidence level or smaller \(n\) widens the interval. Round sample sizes up. Interpret as "about 95% of such intervals contain \(\mu\)".
:::

:::note Learn more online
- **Watch:** [But what is the Central Limit Theorem?](https://www.3blue1brown.com/lessons/clt) · 3Blue1Brown · why sample means become normal
- **Watch:** [The central limit theorem](https://www.examsolutions.net/tutorials/central-limit-theorem/) · ExamSolutions · the exam use of X̄ ~ N(μ, σ²/n)
- **Watch:** [Confidence interval for a population mean](https://www.examsolutions.net/tutorials/confidence-interval-for-a-population-mean/) · ExamSolutions · building and reading an interval
- **Practise:** [CAIE S2 sampling and estimation exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/topic-questions/statistical-sampling-and-estimation/sampling-and-estimation/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory · draw samples and watch confidence intervals hit or miss

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Hypothesis testing](#math.s2.hypothesis).
