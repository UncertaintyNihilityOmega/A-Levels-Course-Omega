@chapter math.exam.p6
@title Paper 6 survival guide
@level guide
@paper CAIE 9709 Paper 6 · Edexcel IAL S2 and S3 · UK Statistics
@time 1 hour
@summary Cambridge Paper 6 (Probability and Statistics 2): length, marks, a timing plan, what MF19 gives you and what you must learn, a topic list with chapters, the marks students lose most often, and a final-week checklist.

:::why
Paper 6 is the second statistics paper of the A Level. It builds on Paper 5 and uses Paper 3 calculus, and it is where statistics becomes inference: you decide whether data support a claim. Written conclusions in context carry many of its marks, so the habits in this guide matter as much as the formulas.
:::

## The paper at a glance

| Fact | Paper 6 |
|---|---|
| Name | Probability and Statistics 2 |
| Time | 1 hour 15 minutes |
| Marks | 50 |
| Weighting | 20% of an A Level (not used in an AS) |
| Used in | A Level route 2 (P1 + P3 + P5 + P6). It cannot be combined with P4 |
| Tools | scientific calculator, ruler, MF19 including the normal distribution tables |
| Accuracy | 3 s.f. unless the question says otherwise |

Paper 6 assumes Paper 5 and the calculus of Paper 3. Knowledge (AO1) is 55% of the marks and application (AO2) is 45%.

## A timing plan

The paper gives 75 minutes for 50 marks: **1.5 minutes per mark**. Aim for **1.3 minutes per mark**: 65 minutes of work, and about 10 minutes to check. Continuous random variable questions are calculus-heavy, so allow a little more time there and less on short Poisson probability parts.

## Formulas: what MF19 gives you and what you must learn

**MF19 gives you:** the Poisson probability formula with its mean and variance; \(E(X)\) and \(\mathrm{Var}(X)\) for a continuous random variable as integrals; the unbiased estimates \(\bar x\) and \(s^2\); the Central Limit Theorem, \(\bar X \sim N\!\left(\mu, \dfrac{\sigma^2}{n}\right)\); the distribution of a sample proportion, \(N\!\left(p, \dfrac{p(1 - p)}{n}\right)\); and the normal tables.

**You must learn:**

| Topic | What to know |
|---|---|
| Poisson | the conditions; approximation to a binomial (roughly \(n > 50\) and \(np < 5\)); normal approximation (\(\lambda > 15\)) with a continuity correction |
| Linear combinations | \(E(aX + bY) = aE(X) + bE(Y)\); \(\mathrm{Var}(aX + bY) = a^2\mathrm{Var}(X) + b^2\mathrm{Var}(Y)\) for independent \(X\) and \(Y\); sums of independent normals and Poissons |
| Confidence intervals | the formulas for a mean and a proportion, and what "95% confident" means |
| Hypothesis tests | hypotheses, tails, critical regions, Type I and Type II errors |
| Continuous random variables | the median and percentiles from areas under a pdf |

:::exam Hypotheses in words, conclusions in context
Write \(H_0\) and \(H_1\) with the parameter named (for example, \(H_0: \lambda = 3\), where \(\lambda\) is the mean number of faults per day). After the calculation, write a two-part conclusion: "There is (insufficient) evidence at the 5% level to support the claim that…". Never write "accept \(H_0\) is true" or "prove". The conclusion in context is a separate mark.
:::

## Topic list

| Topic | Chapter | Know cold |
|---|---|---|
| Poisson distribution | [Poisson distribution](#math.s2.poisson) | conditions, scaling \(\lambda\), approximations |
| Linear combinations | [Linear combinations](#math.s2.linear) | \(\mathrm{Var}(aX + b) = a^2\mathrm{Var}(X)\); \(X_1 + X_2\) versus \(2X\) |
| Continuous random variables | [Continuous random variables](#math.s2.crv) | find \(k\), probabilities as areas, mean, variance, median |
| Sampling and estimation | [Sampling and estimation](#math.s2.sampling) | \(\sigma^2/n\), CLT, unbiased estimates, confidence intervals |
| Hypothesis testing | [Hypothesis testing](#math.s2.hypothesis) | binomial, Poisson and mean tests; Type I and II errors |

The [Correlation and regression](#math.s.regression) chapter is for the UK A Levels and is not part of Paper 6.

## The marks students lose most often

- **Poisson:** doubling the probability instead of the mean (if \(P(\text{none in 10 m}) = 0.449\), the probability for 20 m is not \(0.898\)); forgetting the continuity correction; dividing by \(\lambda\) instead of \(\sqrt\lambda\) when standardising.
- **Linear combinations:** \(\mathrm{Var}(3X - 2) = 9\,\mathrm{Var}(X)\), not \(3\,\mathrm{Var}(X) - 2\); confusing two independent items \(X_1 + X_2\) (variance \(2\sigma^2\)) with one item doubled \(2X\) (variance \(4\sigma^2\)); calling \(2X\) or \(X - Y\) Poisson.
- **Continuous random variables:** forgetting to subtract \([E(X)]^2\) for the variance; substituting "infinity" without writing a limit.
- **Sampling:** the standard deviation of \(\bar X\) is \(\sigma/\sqrt n\); using \(\sigma/n\) or \(\sigma^2/n\) in the standardisation; saying "95% of the data" or "95% probability the mean is in this interval".
- **Hypothesis tests:** putting the whole 5% in one tail of a two-tailed test; using \(P(X = 15)\) instead of \(P(X \ge 15)\); standardising a mean test with \(\sigma\) instead of \(\sigma/\sqrt n\); a conclusion with no context.

:::warn Type I and Type II
The probability of a Type I error equals the actual significance level of the test (the probability of being in the rejection region when \(H_0\) is true). A Type II error is a failure to reject \(H_0\) when it is false: to find its probability you need a specific alternative value of the parameter. Write which case you are computing.
:::

## Final week

:::checklist Final week
- [ ] I have done at least two full timed Paper 6 papers in the last 14 days and marked them
- [ ] I can state the conditions for a Poisson model and scale \(\lambda\) correctly
- [ ] I can use a normal approximation to a Poisson with a continuity correction
- [ ] I can find the mean and variance of \(aX + bY\), and decide when a sum is normal or Poisson
- [ ] I can find \(k\), probabilities, the mean, variance and median for a pdf, including one with an infinite domain
- [ ] I can write the distribution of \(\bar X\) and use the Central Limit Theorem
- [ ] I can find an unbiased estimate of a mean and a variance, and a confidence interval
- [ ] I can carry out a binomial, Poisson and mean test, with hypotheses and a conclusion in context
- [ ] I can find the probability of a Type I and a Type II error
- [ ] I have revised the Paper 5 topics that Paper 6 assumes
:::

## Your progress on Paper 6

:::progress P6
:::

The full mock paper for this exam is [Mock paper: Probability and Statistics 2 (A)](#math.mock.p6a): take it as one sitting, timed, with your calculator and MF19. For short mixed questions across the whole paper, use [Mixed practice: Statistics 2](#math.mixed.stats2).

:::links
- papers: [9709 Paper 6 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-7/) · Physics & Maths Tutor · their page "cie-paper-7" holds Paper 6 [unofficial]

Links checked 3 October 2026.
:::

:::recap
- Paper 6: 1 h 15, 50 marks, 20% of an A Level; route 2 only (P1 + P3 + P5 + P6); calculator, ruler, MF19 with tables.
- MF19 gives the Poisson formula, continuous \(E\) and \(\mathrm{Var}\), unbiased estimates, the CLT and the sample-proportion distribution; learn the approximation conditions, continuity corrections, \(\mathrm{Var}(aX + bY)\) and the confidence-interval formulas.
- State hypotheses with the parameter named and finish with a conclusion in context.
- Plan 1.3 minutes per mark; leave about 10 minutes to check.
- Most lost marks come from scaling a probability instead of the mean, forgetting the square in a variance, the wrong tail, and a missing context sentence.
:::

Next: [Mixed practice: Pure 1](#math.mixed.pure1)
