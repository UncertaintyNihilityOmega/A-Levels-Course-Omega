@chapter math.fm.nonpar
@title Non-parametric tests: the sign test
@level fm
@paper CAIE 9231 Paper 4
@time 4–5 hours
@summary A non-parametric test makes no assumption about the shape of the population, which is what you need when data are skewed, have outliers or are only ranked. You will learn the idea behind such tests, then use the sign test for one sample and for paired samples, with exact binomial probabilities for small samples and a normal approximation for large ones, and compare it with the t-test.

:::why
Many real data sets are not normal: waiting times, incomes, reaction times and ratings are skewed or bunched, and a single wild value can wreck a mean. A t-test then rests on an assumption you cannot defend. The sign test asks a much simpler question, "is each value above or below the claimed median?", and answers it with the binomial distribution you already know. It is the cheapest test there is, and the way it fails (it throws information away) explains why the Wilcoxon tests of the next chapter exist.
:::

**Before you start**, you need the binomial distribution from [Discrete random variables: binomial and geometric](#math.s1.drv), the logic of a hypothesis test (hypotheses, tail probability, significance level, critical region, conclusion in context) from [Hypothesis testing](#math.s2.hypothesis), and the normal approximation with a continuity correction from [The normal distribution](#math.s1.normal). The t-test it is compared with is in [The t-distribution: one-sample tests and intervals](#math.fm.inference) and [Comparing two means](#math.fm.twosample).

:::try Warm-up
Q: \(X \sim B(10, \tfrac12)\). Find \(P(X \le 2)\). (from [Discrete random variables: binomial and geometric](#math.s1.drv))
A: \(P(X \le 2) = \dfrac{1 + 10 + 45}{1024} = \dfrac{56}{1024} = 0.0547\) (3 s.f.), because \(P(X = r) = \binom{10}{r}\left(\tfrac12\right)^{10}\).
Q: Under \(H_0\), \(X \sim B(20, 0.3)\). A sample gives \(X = 2\), and \(H_1: p < 0.3\). Find the probability of a result at least this extreme (the \(p\)-value) and state the conclusion at the 5% level. (from [Hypothesis testing](#math.s2.hypothesis))
A: \(P(X \le 2) = 0.0355 < 0.05\), so reject \(H_0\): there is sufficient evidence at the 5% level that \(p < 0.3\).
Q: \(X \sim B(50, \tfrac12)\). Use a normal approximation to estimate \(P(X \ge 30)\). (from [The normal distribution](#math.s1.normal))
A: \(X \approx Y \sim N(25, 12.5)\). With a continuity correction, \(P(Y > 29.5)\): \(z = \dfrac{4.5}{\sqrt{12.5}} = 1.273\), so the probability is \(1 - 0.8984 = 0.102\).
:::

## Parametric and non-parametric tests

Every test you have met so far starts by assuming a **family** of distributions. The one-sample t-test assumes the population is normal. A binomial test assumes fixed \(n\) and constant \(p\). The test then asks about a **parameter** of that family: a mean \(\mu\), a variance \(\sigma^2\), a probability \(p\). Such tests are called parametric.

:::def Parametric test
A hypothesis test that assumes the population has a particular form of distribution (for example normal) and tests a statement about one of its parameters (for example \(\mu\)).
:::

:::def Non-parametric test
A hypothesis test that does not assume the population has a particular form of distribution. It is also called a **distribution-free** test.
:::

A non-parametric test usually works with the **order** of the data, or only the **signs** of differences, instead of their exact values. That is why it still works when the data are skewed, when they contain outliers, or when only a ranking is recorded.

| | Parametric (for example t-test) | Non-parametric (sign test) |
|---|---|---|
| Assumes | a distribution (normal) | almost nothing about the shape |
| Tests | a mean | a median |
| Uses | every value | only whether each value is above or below |
| Best when | the assumption is believable | data are skewed, have outliers or are ranks |
| Cost | wrong answers if the assumption fails | less powerful: needs stronger evidence |

The last row is the price. If the population really is normal, a t-test finds a real difference more often than a sign test does. We say the t-test is more **powerful** (it is less likely to miss a real effect). A non-parametric test is a safe choice when you cannot trust the assumption, and a wasteful one when you can.

:::warn Non-parametric does not mean "no conditions"
A sign test still needs a **random sample** and **independent** observations. It also needs the population to be continuous, so that "equal to the median" almost never happens. In 9231 questions no observation ever equals the median being tested and no difference is zero, so you never have to discard anything.
:::

## The median and the idea of the sign test

A non-parametric test cannot talk about the mean, because the mean depends on the whole shape of the distribution and is dragged about by outliers. It talks about the **median**.

:::def Population median
The value \(m\) such that a randomly chosen member of a continuous population is below \(m\) with probability \(\tfrac12\) and above \(m\) with probability \(\tfrac12\): \(P(X < m) = P(X > m) = \tfrac12\).
:::

Suppose someone claims the median of a population is \(m_0\). Take a random sample of \(n\) values. If the claim is true, each value is equally likely to fall above or below \(m_0\), whatever the shape of the distribution. Replace every value by a sign: \(+\) if it is above \(m_0\), \(-\) if it is below. The signs behave like \(n\) independent fair coin tosses.

:::key The sign test (single sample)
To test \(H_0: m = m_0\), where \(m\) is the population median, give each observation \(x\) the sign of \(x - m_0\). Let \(S\) be the number of \(+\) signs. If \(H_0\) is true,
\[S \sim B\left(n, \tfrac12\right)\]
The same distribution holds for any population shape, which is why the test is distribution-free. The **\(p\)-value** is the probability, under \(H_0\), of a result at least as extreme as the one observed:
- \(H_1: m > m_0\): \(P(S \ge s)\), where \(s\) is the observed number of \(+\) signs.
- \(H_1: m < m_0\): \(P(S \le s)\).
- \(H_1: m \ne m_0\): double the probability of the tail the data fall in, or compare that tail with \(\tfrac12\alpha\).

Reject \(H_0\) when the \(p\)-value is at most the significance level \(\alpha\).
:::

:::steps
1. Define the median: "Let \(m\) be the population median."
2. State \(H_0: m = m_0\) and \(H_1\) (one-tailed or two-tailed, decided by the question's wording).
3. Write the sign of each \(x - m_0\) and count the \(+\) signs (or \(-\) signs).
4. State "Under \(H_0\), \(S \sim B(n, \tfrac12)\)" and find the tail probability.
5. Compare with \(\alpha\) (or \(\tfrac12\alpha\) for a two-tailed test).
6. Conclude in context, in words that are not too strong: "there is (or is not) sufficient evidence at the 5% level that …".
:::

Because the distribution is \(B(n, \tfrac12)\), every probability has the form \(\dfrac{\text{whole number}}{2^n}\). With small \(n\) you can write them down exactly:
\[P(S \le k) = \frac{1}{2^n}\left[\binom{n}{0} + \binom{n}{1} + \dots + \binom{n}{k}\right]\]
There is no sign-test table on MF19, so you work these out with your calculator's binomial cumulative function, or by adding the terms.

:::eg A bus company says that the median length of a journey on route 14 is 25 minutes. Passengers think that journeys are quicker. The times, in minutes, of 10 random journeys are 22, 19, 27, 21, 18, 24, 23, 20, 26, 17. Test at the 5% significance level whether the median journey time is less than 25 minutes.
Let \(m\) be the population median journey time, in minutes.
\[H_0: m = 25 \qquad H_1: m < 25\]
The signs of \(x - 25\) are: \(-,-,+,-,-,-,-,-,+,-\). There are 2 plus signs and 8 minus signs. Let \(S\) be the number of plus signs. Under \(H_0\), \(S \sim B(10, \tfrac12)\). Small values of \(S\) support \(H_1\), so we need
\[P(S \le 2) = \frac{1 + 10 + 45}{1024} = 0.0547\]
Since \(0.0547 > 0.05\), do not reject \(H_0\). There is not sufficient evidence at the 5% level to conclude that the median journey time is less than 25 minutes.

Notice how close the call is. With only 1 plus sign, \(P(S \le 1) = \tfrac{11}{1024} = 0.0107\) and the result would have been significant.
:::

### Two-tailed tests

For \(H_1: m \ne m_0\) either tail counts as evidence, so the 5% is split into 2.5% in each tail. Find the tail the data are in (the smaller count) and compare its probability with \(\tfrac12\alpha\); equivalently double it and compare with \(\alpha\).

:::eg (Exam style) A shopkeeper believes that the median amount spent by a customer is \$40. A random sample of 12 customers spent \$52, \$47, \$61, \$45, \$38, \$55, \$49, \$58, \$43, \$66, \$51 and \$36. Use a sign test at the 5% level to test whether the median amount spent is different from \$40.
Let \(m\) be the population median amount spent, in dollars. \(H_0: m = 40\) and \(H_1: m \ne 40\). [B1]

The values above 40 give \(+\): there are 10 plus signs and 2 minus signs. [B1]

Under \(H_0\), the number of minus signs \(S \sim B(12, \tfrac12)\). The minus signs are the smaller count, so we look at the lower tail.
\[P(S \le 2) = \frac{1 + 12 + 66}{4096} = 0.0193\] [M1 A1]
The test is two-tailed, so compare with \(\tfrac12 \times 0.05 = 0.025\). Since \(0.0193 < 0.025\), reject \(H_0\). [M1]

There is sufficient evidence at the 5% level that the median amount spent is not \$40. [A1]

**Check** by doubling: \(2 \times 0.0193 = 0.0386 < 0.05\), the same conclusion. At the 1% level, \(0.0193 > 0.005\), so the result is not significant at 1%.
:::

:::warn Three tail slips
- **Comparing a two-tailed tail with the full \(\alpha\).** A tail of 0.0193 is below 0.05 but the test needs 0.025 in each tail, or the doubled value 0.0386 against 0.05. Never compare the single tail with 5%.
- **Using the wrong tail.** The tail must be the one the data lean towards. If \(H_1: m > m_0\) but most signs are minus, \(P(S \ge s)\) is large and \(H_0\) stands, whatever the size of the "lower" tail.
- **Using \(P(S = s)\).** The \(p\)-value includes every result at least as extreme: \(P(S \le s)\) or \(P(S \ge s)\).
:::

### Critical regions

You can also decide the rule before collecting data. The **critical region** is the set of values of \(S\) for which you reject \(H_0\): take the tail with total probability as large as possible without exceeding \(\alpha\) (or \(\tfrac12\alpha\) in each tail of a two-tailed test). Because \(B(n, \tfrac12)\) is symmetric, the upper tail is the mirror image of the lower: if \(S \le k\) is in the critical region then so is \(S \ge n - k\).

The table gives the largest \(k\) with \(P(S \le k) \le\) the stated tail probability, for \(B(n, \tfrac12)\). A dash means even \(S = 0\) is too likely.

| \(n\) | 5% in one tail | 2.5% in one tail | 1% in one tail |
|---|---|---|---|
| 6 | 0 | 0 | – |
| 7 | 0 | 0 | 0 |
| 8 | 1 | 0 | 0 |
| 9 | 1 | 1 | 0 |
| 10 | 1 | 1 | 0 |
| 11 | 2 | 1 | 1 |
| 12 | 2 | 2 | 1 |
| 13 | 3 | 2 | 1 |
| 14 | 3 | 2 | 2 |
| 15 | 3 | 3 | 2 |
| 16 | 4 | 3 | 2 |
| 17 | 4 | 4 | 3 |
| 18 | 5 | 4 | 3 |
| 19 | 5 | 4 | 4 |
| 20 | 5 | 5 | 4 |

The table is for your understanding, not a table you will be given: in an exam you find the critical region from \(B(n, \tfrac12)\) yourself. The row \(n = 12\), "2.5% in one tail", gives \(k = 2\), which is why the shopkeeper's \(S = 2\) was just inside the region.

:::eg Find the critical region for a two-tailed sign test at the 5% level when \(n = 15\), and state the probability of a Type I error. In the test, \(S\) is the number of plus signs.
Each tail may have probability at most 0.025. Under \(H_0\), \(S \sim B(15, \tfrac12)\).
\[\begin{aligned}
P(S \le 3) &= \frac{1 + 15 + 105 + 455}{32768} = \frac{576}{32768} = 0.0176 \\
P(S \le 4) &= \frac{576 + 1365}{32768} = 0.0592
\end{aligned}\]
\(0.0176 \le 0.025\) but \(0.0592 > 0.025\), so the lower tail is \(S \le 3\). By symmetry the upper tail is \(S \ge 12\).

The critical region is \(S \le 3\) or \(S \ge 12\).

The probability of a Type I error (rejecting \(H_0\) when it is true) is the actual significance level, \(2 \times 0.0176 = 0.0352\), that is 3.52%, below the nominal 5% because \(S\) is discrete.
:::

## The paired-sample sign test

Often each subject is measured twice: before and after a treatment, with method A and with method B. The two measurements for one subject are **paired**, and it is the difference that matters. Form \(d = x_A - x_B\) for each pair. If the two populations are identical (the treatment has no effect), the differences are as likely to be positive as negative, so the median of the differences is 0.

:::key The sign test for paired samples
For pairs \((x_i, y_i)\) let \(d_i = x_i - y_i\) and let \(m\) be the population median of the differences. To test whether the populations are identical:
\[H_0: m = 0\]
Treat the signs of the \(d_i\) exactly as in the single-sample test: under \(H_0\), the number of positive differences is \(B(n, \tfrac12)\), where \(n\) is the number of pairs.
:::

This is the single-sample sign test with \(m_0 = 0\) applied to the differences. You must decide in advance which way you subtract and state it, because \(H_1\) depends on it.

:::eg (Exam style) Eight athletes run 5 km before and after a training programme. Their times, in minutes, are

| Athlete | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| Before | 24.1 | 26.3 | 23.8 | 27.5 | 25.2 | 28.0 | 24.9 | 26.7 |
| After | 23.4 | 25.1 | 24.0 | 26.2 | 24.6 | 26.9 | 24.4 | 25.7 |

Use a sign test at the 5% level to test whether the programme reduces the median time.
Let \(m\) be the population median of (time before) \(-\) (time after). \(H_0: m = 0\) and \(H_1: m > 0\). [B1]

The differences are
\[+0.7,\ +1.2,\ -0.2,\ +1.3,\ +0.6,\ +1.1,\ +0.5,\ +1.0\]
so 7 are positive and 1 is negative. [B1]

Under \(H_0\), the number of positive differences \(S \sim B(8, \tfrac12)\).
\[P(S \ge 7) = \frac{8 + 1}{256} = 0.0352\] [M1 A1]
Since \(0.0352 < 0.05\), reject \(H_0\). [M1]

There is sufficient evidence at the 5% level that the training programme reduces the median 5 km time. [A1]
:::

:::exam Wording a conclusion
Your last line needs three things: the decision about \(H_0\), the level, and the claim in the context of the question ("the median 5 km time is reduced"). Avoid "proves" and "accept \(H_1\)". When the result is not significant say "there is not sufficient evidence", never "the programme has no effect": you have not shown that.
:::

## Large samples: the normal approximation

For large \(n\) the exact sum of binomial terms is long. \(S \sim B(n, \tfrac12)\) has mean \(\tfrac12 n\) and variance \(\tfrac14 n\), and since \(np = n/2\) is large it is well approximated by a normal distribution.

:::key Normal approximation for the sign test
If \(S \sim B(n, \tfrac12)\) and \(n\) is large (the usual rule is \(np > 5\) and \(nq > 5\), so \(n \ge 11\), and in practice \(n\) is 20 or more),
\[S \approx Y \sim N\left(\tfrac{n}{2}, \tfrac{n}{4}\right)\]
Use a continuity correction, because \(S\) takes whole-number values: \(P(S \ge s) \approx P(Y > s - 0.5)\) and \(P(S \le s) \approx P(Y < s + 0.5)\).
:::

:::eg (Exam style) A random sample of 40 pupils sits a reaction test. The test's designers claim that the median reaction time is 280 ms. 27 of the 40 pupils have times above 280 ms. Test at the 5% level whether the median is greater than 280 ms, using a normal approximation.
Let \(m\) be the population median reaction time. \(H_0: m = 280\) and \(H_1: m > 280\). [B1]

Let \(S\) be the number of times above 280 ms. Under \(H_0\), \(S \sim B(40, \tfrac12)\), so \(S \approx Y \sim N(20, 10)\). [M1 A1]

\[P(S \ge 27) \approx P(Y > 26.5)\] [M1]
\[z = \frac{26.5 - 20}{\sqrt{10}} = 2.055 \qquad P(Z > 2.055) = 0.0199\] [A1]
Since \(0.0199 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level that the median reaction time is greater than 280 ms. [A1]

**Check** with the exact value: \(P(S \ge 27)\) for \(B(40, \tfrac12)\) is 0.0192, so the approximation is good.
:::

:::tip Which count to use in the exam
A common slip is to use \(P(S > 27)\) instead of \(P(S \ge 27)\), then correct to \(Y > 27.5\). "At least 27" means 27 is included, so the boundary is half a unit below 27.
:::

## What the sign test costs: comparing tests

The sign test uses only the direction of each difference. A pair that changed by 0.01 counts the same as a pair that changed by 100. Information thrown away makes the test less powerful. Compare the two questions:

- **t-test (paired).** Are the *sizes* of the differences, on average, large compared with their variation? Needs the differences to be normal (or the sample large).
- **Sign test.** Are *more than half* of the differences positive? Needs only that the differences are independent.

When the t-test's assumption is believable, it will reject a false \(H_0\) more often. When the data are skewed, or one difference is huge because of a recording error, the t-test's mean and standard deviation are distorted but the sign test is untouched.

:::eg (Exam style) A coffee shop's records show that the median number of drinks bought per customer per month was 8. The owner believes that after a loyalty card was introduced the median has increased. She records the number of drinks bought in one month by each of 14 randomly chosen customers. The results are shown in the stem-and-leaf diagram.

| Stem | Leaves |
|---|---|
| 0 | 4 5 7 |
| 1 | 0 2 2 5 8 9 |
| 2 | 1 3 |
| 3 | 4 |
| 4 | 0 |
| 5 | (none) |
| 6 | (none) |
| 7 | (none) |
| 8 | 6 |

Key: 2 \| 3 represents 23 drinks.

(a) Suggest a reason why a Wilcoxon signed-rank test might not be appropriate. (b) Use a sign test at the 5% level to investigate the owner's belief.
(a) The Wilcoxon signed-rank test (the next chapter) ranks the sizes of the differences and needs the population to be roughly symmetrical, so an outlier or heavy skew rules it out. The data contain an outlier (86) and are skewed, so the population may not be symmetrical. [B1] (A repeated value such as the two 12s would give tied ranks, which is also an accepted comment, although 9231 never asks you to rank tied values.)

(b) \(H_0\): the population median is 8. \(H_1\): the population median is greater than 8. [B1]

Under \(H_0\), the number \(S\) of values above 8 has \(S \sim B(14, \tfrac12)\). [B1] Eleven values are above 8 (10 and everything larger) and three are below (4, 5 and 7).

\[P(S \ge 11) = \frac{364 + 91 + 14 + 1}{16384}\] [M1]
\[= \frac{470}{16384} = 0.0287\] [A1]
Since \(0.0287 < 0.05\), reject \(H_0\). [M1]

There is sufficient evidence at the 5% level to support the owner's belief that the median number of drinks per customer has increased. [A1]

The sign test counted the 86 as one more "above 8". A t-test would have been pulled strongly by it.
:::

:::exam How the sign test is marked
A recent 9231 mark scheme for a sign test of this kind gives separate marks for: the hypotheses (the **population median**, stated with a value: not "mean" or "average"), writing the distribution \(B(n, 0.5)\), a binomial probability with the right tail, its value, the comparison with the level, and a conclusion in context with careful language ("sufficient evidence to support …"; never "proves"). It also allowed a normal approximation \(N\left(\tfrac n2, \tfrac n4\right)\) for a sample as small as 15, so the examiners do not penalise it, but the exact binomial is what the question is built for and is safer. Hypotheses about a mean score no marks.
:::

:::eg (Exam style) A teacher records the time, in seconds, that each of 12 students takes to solve a puzzle with and without background music. In 9 cases the time was shorter with the music, and in 3 it was longer. The differences (time without music minus time with music) are strongly skewed. (a) Give one reason for using a sign test rather than a paired t-test. (b) Test at the 5% level whether the median time is shorter with music. (c) The teacher gives every student the puzzle without music first, then with music. Explain why this design may be unreliable and suggest an improvement.
(a) The differences are not normally distributed (they are skewed), so the assumption of the paired t-test fails; the sign test does not need a normal population. [B1]

(b) Let \(m\) be the population median of (time without music) \(-\) (time with music). \(H_0: m = 0\) and \(H_1: m > 0\). [B1]

The number of positive differences \(S \sim B(12, \tfrac12)\) under \(H_0\).
\[P(S \ge 9) = \frac{220 + 66 + 12 + 1}{4096} = \frac{299}{4096} = 0.0730\] [M1 A1]
Since \(0.0730 > 0.05\), do not reject \(H_0\). There is not sufficient evidence at the 5% level that the median time is shorter with music. [A1]

(c) Doing the puzzle a second time gives practice: the second attempt may be quicker whatever the music (an **order effect**). Improve it by allocating the order at random, or having half the students (chosen at random) do the music version first. [B1] [B1]
:::

:::note Experimental design in matched pairs
Examiners like these points: pair the subjects on purpose (same person twice, or two matched people); randomise which treatment comes first or which member of each pair receives which treatment; use a random sample of subjects so the result can be applied to the population; allow a gap between the two attempts so the first does not affect the second; and say a bigger sample makes a test more reliable.
:::

:::board
This chapter describes the Cambridge 9231 sign test. In 9231 the data never contain a value equal to the median being tested or a zero difference, so no observation is discarded (repeated values can occur in a data set, and are then a reason for doubting a Wilcoxon test), and the test is written with the binomial \(B(n, \tfrac12)\) (a normal approximation only when \(n\) is large).
:::

:::eg Spot the error: a two-tailed sign test at the 5% level is used on the median of 14 values, with \(H_0: m = 30\) and \(H_1: m \ne 30\). Three values are below 30 and 11 are above. The test is worth 4 marks.
A student wrote this answer.

Line 1: Under \(H_0\), the number of values below 30 is \(S \sim B(14, \tfrac12)\).
Line 2: \(P(S \le 3) = \dfrac{1 + 14 + 91 + 364}{16384} = 0.0287\)
Line 3: \(0.0287 < 0.05\), so reject \(H_0\). There is sufficient evidence at the 5% level that the median is not 30.

Lines 1 and 2 are correct. [M1] [A1]

**Line 3 compares a single tail with the whole 5%.** The test is two-tailed, so the tail must be compared with 0.025 (or doubled to 0.0574 and compared with 0.05). Since \(0.0287 > 0.025\), \(H_0\) is not rejected. The comparison is a wrong method, so that mark is lost along with the conclusion mark. [M0] [A0] The student scores 2 out of 4.

Correct line 3: \(0.0287 > 0.025\), so do not reject \(H_0\). There is not sufficient evidence at the 5% level that the median is different from 30.
:::

:::try Practice
Q: Find \(P(S \le 3)\) for \(S \sim B(9, \tfrac12)\).
A: \(\dfrac{1 + 9 + 36 + 84}{512} = \dfrac{130}{512} = 0.254\).
Q: A population median is claimed to be 8.0. A sample of 11 values has 9 above 8.0. Test \(H_0: m = 8\) against \(H_1: m > 8\) at the 5% level.
A: \(S \sim B(11, \tfrac12)\). \(P(S \ge 9) = \dfrac{55 + 11 + 1}{2048} = 0.0327 < 0.05\), so reject \(H_0\): there is sufficient evidence at the 5% level that the median exceeds 8.
Q: A two-tailed test at the 5% level has \(n = 10\). 8 values are above \(m_0\). Is \(H_0\) rejected?
A: The upper tail: \(P(S \ge 8) = \dfrac{45 + 10 + 1}{1024} = 0.0547\). That is more than 0.025, so do not reject \(H_0\).
Q: What is the critical region for a one-tailed sign test with \(H_1: m < m_0\), \(n = 12\), at the 5% level?
A: \(P(S \le 2) = \dfrac{79}{4096} = 0.0193\) and \(P(S \le 3) = \dfrac{299}{4096} = 0.0730\), so the critical region is \(S \le 2\).
Q: In a paired sign test the differences are \(+3, -1, +5, +2, +4, +7, -2\). How many positive differences are there, and what is \(n\)?
A: There are 5 positive differences and \(n = 7\) pairs. The sizes of the differences do not matter.
Q: Why must a non-parametric test of a median still be based on a random sample?
A: The sign test's binomial model needs independent observations each with probability \(\tfrac12\) of being above the median. A biased sample breaks that, whatever the shape of the population.
Q: Use the normal approximation to estimate \(P(S \le 22)\) for \(S \sim B(60, \tfrac12)\).
A: \(S \approx N(30, 15)\). \(P(S \le 22) \approx P(Y < 22.5)\): \(z = \dfrac{-7.5}{\sqrt{15}} = -1.936\), so the probability is 0.0264.
Q: Write down \(H_0\) and \(H_1\) for a paired sign test to see whether a new fertiliser changes the median yield of a plot, where each plot is split in two halves and \(d\) = yield with new minus yield with old.
A: Let \(m\) be the population median of \(d\). \(H_0: m = 0\) and \(H_1: m \ne 0\) (two-tailed, since the question asks whether the yield "changes").
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The manufacturer of a type of bulb claims that the median lifetime is 120 hours. A random sample of 9 bulbs has 7 lifetimes above 120 hours. Test, at the 5% level, whether the median lifetime is greater than 120 hours.
A: Let \(m\) be the population median lifetime. \(H_0: m = 120\), \(H_1: m > 120\). [B1]
Under \(H_0\) the number above 120, \(S\), has \(S \sim B(9, \tfrac12)\). \(P(S \ge 7) = \dfrac{36 + 9 + 1}{512} = 0.0898\) [M1 A1]
\(0.0898 > 0.05\): do not reject \(H_0\). There is not sufficient evidence at the 5% level that the median lifetime is greater than 120 hours. [A1]
Q: [4 marks] ★ Find the critical region for a two-tailed sign test at the 5% level when \(n = 11\), and the actual significance level of the test.
A: Under \(H_0\), \(S \sim B(11, \tfrac12)\). \(P(S \le 1) = \dfrac{12}{2048} = 0.00586\) and \(P(S \le 2) = \dfrac{67}{2048} = 0.0327\). [M1]
Each tail must be at most 0.025, so the lower tail is \(S \le 1\). [A1]
By symmetry the critical region is \(S \le 1\) or \(S \ge 10\). [A1]
Actual significance level \(= 2 \times 0.00586 = 0.0117\). [B1]
Q: [6 marks] ★★ Eight patients have their systolic blood pressure, in mm Hg, measured before and after taking a drug. Before: 148, 152, 139, 160, 145, 157, 151, 143. After: 141, 150, 142, 151, 138, 149, 153, 136. Use a sign test at the 5% level to test whether the drug lowers the median blood pressure.
A: Let \(m\) be the population median of (before) \(-\) (after). \(H_0: m = 0\), \(H_1: m > 0\). [B1]
The differences are \(+7, +2, -3, +9, +7, +8, -2, +7\). There are 6 positive and 2 negative. [B1]
Under \(H_0\), \(S \sim B(8, \tfrac12)\). \(P(S \ge 6) = \dfrac{28 + 8 + 1}{256}\) [M1] \(= 0.145\). [A1]
\(0.145 > 0.05\), so do not reject \(H_0\). [M1]
There is not sufficient evidence at the 5% level that the drug lowers the median blood pressure. [A1]
Q: [5 marks] ★★ A random sample of 60 values from a population is taken, and 38 of them are above 15.0. Use a normal approximation to a binomial distribution to test, at the 5% level, whether the population median is different from 15.0.
A: \(H_0: m = 15\), \(H_1: m \ne 15\). [B1]
Under \(H_0\) the number above 15, \(S\), has \(S \approx Y \sim N(30, 15)\). [M1]
\(P(S \ge 38) \approx P(Y > 37.5)\) [M1]: \(z = \dfrac{7.5}{\sqrt{15}} = 1.936\), probability \(0.0264\). [A1]
Two-tailed, so compare with 0.025: \(0.0264 > 0.025\), do not reject \(H_0\). There is not sufficient evidence at the 5% level that the median differs from 15.0. [A1]
Q: [6 marks] ★★ A two-tailed sign test is carried out on 18 values and \(H_0\) is rejected if the number of plus signs is at most 4 or at least 14. (a) Find the probability of a Type I error. (b) In fact, each value is below the tested median with probability 0.7, independently, so the number of plus signs is \(B(18, 0.3)\). Find the probability of a Type II error.
A: (a) Under \(H_0\), \(S \sim B(18, \tfrac12)\). \(P(S \le 4) = \dfrac{1 + 18 + 153 + 816 + 3060}{262144} = 0.0154\) [M1 A1]
By symmetry \(P(S \ge 14)\) is the same, so the Type I error probability is \(2 \times 0.0154 = 0.0309\). [A1]
(b) A Type II error is failing to reject, so \(5 \le S \le 13\). [B1]
\(P(5 \le S \le 13) = 1 - P(S \le 4) - P(S \ge 14)\) with \(S \sim B(18, 0.3)\), and \(P(S \ge 14)\) is negligible (about \(4 \times 10^{-5}\)). [M1]
\(P(S \le 4) = 0.3327\), so the probability is \(1 - 0.3327 - 0.00004 = 0.667\) (3 s.f.). [A1]
Q: [9 marks] (#math.fm.inference) ★★★ A café owner thinks customers wait a median of 6 minutes to be served. Waiting times for 10 customers, in minutes, are 3.2, 4.1, 2.8, 9.5, 5.0, 3.7, 6.8, 4.4, 2.9, 3.5. (a) Explain why a sign test may be better than a t-test for these data. (b) Carry out a sign test at the 5% level to test whether the median wait is less than 6 minutes. (c) Use the sign test result to explain why a test that used the sizes of the times might reach a different conclusion. (d) State one way of making sure the sample is representative.
H: Count how many times are above 6, then use \(B(10, \tfrac12)\).
H: The mean of the data is much larger than the median because of one value; what does that say about a t-test?
H: For (c), compare how much information each test uses.
A: (a) Waiting times are often skewed, and the value 9.5 looks like an outlier, so the normality assumption of a t-test is doubtful; the sign test needs no such assumption. [B1]
(b) Let \(m\) be the population median wait. \(H_0: m = 6\), \(H_1: m < 6\). [B1]
The values above 6 are 9.5 and 6.8: 2 plus signs. \(S \sim B(10, \tfrac12)\). [B1]
\(P(S \le 2) = \dfrac{56}{1024} = 0.0547\) [M1 A1] \(> 0.05\), so do not reject \(H_0\). Not sufficient evidence at the 5% level that the median wait is less than 6 minutes. [A1]
(c) The sign test ignores how far below 6 the other eight times are (most are 2 to 3 minutes below). A test using the sizes would use that information, and the evidence may then be strong enough. [B1 B1]
(d) Choose customers at random (for example every \(k\)th customer through the day, at different times of day). [B1]
Q: [8 marks] (#math.s2.hypothesis) ★★★ A sign test is to be carried out at the 5% level with \(H_0: m = 50\) and \(H_1: m < 50\), using a sample of 25 values. (a) Use the exact binomial distribution to find the critical region. (b) Use a normal approximation to find the largest value of \(S\) whose approximate \(P(S \le s)\) is below 0.05, and compare it with (a). (c) In the sample, 7 values are below 50. State the conclusion.
H: In (a), find \(P(S \le k)\) for \(B(25, \tfrac12)\) until it passes 0.05.
H: In (b), \(S \approx N(12.5, 6.25)\) and \(P(S \le s) \approx P(Y < s + 0.5)\); the critical \(z\) is \(-1.645\).
A: (a) Under \(H_0\) the number below 50 is \(S \sim B(25, \tfrac12)\). [B1] \(P(S \le 7) = 0.0216\) and \(P(S \le 8) = 0.0539\). [M1 A1]
The critical region is \(S \le 7\). [A1]
(b) \(S \approx N(12.5, 6.25)\). [B1] Need \(\dfrac{s + 0.5 - 12.5}{2.5} < -1.645\), so \(s < 7.89\), giving \(s \le 7\). [M1 A1] The approximation agrees with the exact region.
(c) 7 is in the critical region, so reject \(H_0\). There is sufficient evidence at the 5% level that the median is less than 50. [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A sign test with \(H_0: m = m_0\) against \(H_1: m > m_0\) uses 10 observations and rejects \(H_0\) when 9 or 10 are above \(m_0\). (a) Find its significance level. (b) The population is actually such that each observation is above \(m_0\) with probability 0.8. Find the probability that the test rejects \(H_0\) (the **power** of the test at this alternative). (c) For the population of (b), explain what happens to this power as \(n\) is increased and the critical region is chosen the same way.
H: In (a) use \(B(10, \tfrac12)\); in (b) use \(B(10, 0.8)\) and the same event.
H: The power is the probability of being in the critical region when \(H_0\) is false.
A: (a) \(P(S \ge 9) = \dfrac{10 + 1}{1024} = 0.0107\). [M1 A1]
(b) With \(S \sim B(10, 0.8)\): \(P(S \ge 9) = 10(0.8)^9(0.2) + (0.8)^{10}\) [M1] \(= 0.2684 + 0.1074 = 0.376\). [A1]
(c) The power increases towards 1, because with more observations the proportion above \(m_0\) is close to 0.8, far from 0.5, and falls in the critical region almost surely. [B1 B1]
Q: [4 marks] ★★★ A sign test is a one-tailed test at the 1% level with all of the \(n\) differences positive. Show that the smallest \(n\) for which this result is significant is 7. Explain why a t-test could still reject \(H_0\) when a sign test cannot, even with all the differences positive and the same \(n\).
H: With every sign positive, \(P(S = n) = \left(\tfrac12\right)^n\).
H: Think about the sizes of the differences.
A: \(P(\text{all } n \text{ positive}) = \left(\tfrac12\right)^n\). [M1] \(\left(\tfrac12\right)^6 = 0.0156 > 0.01\) and \(\left(\tfrac12\right)^7 = 0.00781 < 0.01\). [A1] So \(n = 7\) is the smallest. [A1]
Even with all positive signs for \(n = 6\), the sign test cannot reach 1%, whatever the sizes. A t-test uses the sizes of the differences: large, consistent differences give a very large \(t\) value. [B1]
:::

:::quiz
? A sign test is used for \(H_0: m = 50\) with 12 observations, 9 above 50 and 3 below, \(H_1: m > 50\). Which probability is the \(p\)-value?
+ \(P(S \ge 9)\) for \(S \sim B(12, \tfrac12)\)
- \(P(S = 9)\) for \(S \sim B(12, \tfrac12)\)
- \(P(S \le 9)\) for \(S \sim B(12, \tfrac12)\)
- \(P(S \ge 9)\) for \(S \sim B(12, 0.75)\)
> The \(p\)-value is the probability of a result at least as extreme in the direction of \(H_1\): \(P(S \ge 9)\) under \(H_0\). \(P(S = 9)\) leaves out the more extreme results; \(P(S \le 9)\) is the wrong tail; and \(p\) is \(\tfrac12\) under \(H_0\), not the observed 0.75.
? A two-tailed sign test at the 5% level gives a tail probability of 0.031. What should you do?
+ Compare with 0.025, or double to 0.062 and compare with 0.05: do not reject
- Compare with 0.05: reject
- Compare 0.031 with 0.10: reject
- Use the other tail
> The 5% is shared between two tails: 0.031 is more than 0.025. Comparing a single tail with the whole 5% is the commonest slip.
? Which of these is an assumption of the sign test for a single sample?
+ The observations are independent and come from a random sample
- The population is normal
- The population is symmetrical
- The population variance is known
> The sign test needs no shape assumption (it is distribution-free). Symmetry is needed for the Wilcoxon tests, and normality for the t-test.
? Under \(H_0\), what are the mean and variance of the number of plus signs in a sign test with \(n = 40\)?
+ Mean 20, variance 10
- Mean 20, variance 20
- Mean 40, variance 10
- Mean 20, variance 5
> \(B(n, \tfrac12)\) has mean \(\tfrac12 n = 20\) and variance \(n \times \tfrac12 \times \tfrac12 = 10\). Variance 20 forgets the \(\tfrac14\), and the standard deviation is \(\sqrt{10}\).
? In a paired sign test the differences are \(+1.2, -0.4, +3.1, +0.2, -0.7, +2.5, +0.9\). What is \(n\) and the number of plus signs?
+ \(n = 7\), 5 plus signs
- \(n = 7\), total of the positive differences 7.9
- \(n = 5\), 5 plus signs
- \(n = 14\), 5 plus signs
> There are 7 pairs, of which 5 differences are positive. The sizes are ignored, and each pair is one trial, not two.
? Which statement about the sign test and the t-test is correct?
+ The sign test can be used on skewed data but is less powerful than the t-test when the data are normal
- The sign test is always the better test because it needs fewer assumptions
- The sign test tests the mean and the t-test tests the median
- The sign test needs a larger sample than the t-test to be valid
> Fewer assumptions buy safety but cost power. The sign test tests the median, and it can be used for samples of any size (exact binomial for small samples).
:::

:::checklist What you can now do
- [ ] I can explain what a non-parametric test is, and when one is more suitable than a parametric test.
- [ ] I can state the basis of the sign test: under \(H_0\) the number of plus signs is \(B(n, \tfrac12)\).
- [ ] I can state hypotheses about a population median and carry out a single-sample sign test, one-tailed or two-tailed, with exact binomial probabilities.
- [ ] I can find the critical region and the actual significance level of a sign test.
- [ ] I can carry out a paired-sample sign test on the differences and state a conclusion in context.
- [ ] I can use a normal approximation \(N(\tfrac n2, \tfrac n4)\) with a continuity correction for large \(n\).
- [ ] I can compare the sign test with the t-test and comment on experimental design (order effects, randomisation).
:::

:::recap
- A non-parametric (distribution-free) test makes no assumption about the shape of the population; it tests a median, uses signs or ranks and is less powerful than a parametric test when the parametric assumptions hold.
- Sign test: give each \(x - m_0\) a sign; under \(H_0: m = m_0\) the number of plus signs \(S \sim B(n, \tfrac12)\).
- The \(p\)-value is the tail probability at least as extreme as the data in the direction of \(H_1\); for a two-tailed test compare the tail with \(\tfrac12\alpha\).
- Paired data: use the differences, \(H_0:\) median difference is 0.
- Large \(n\): \(S \approx N(\tfrac n2, \tfrac n4)\) with a continuity correction.
- Conclusions are about evidence in context; "not significant" is not "no effect".
- Design: randomise the order of treatments to avoid order effects, and use a random sample.
:::

:::links
- practise: [Significance tests, one sample](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample) · Khan Academy · the logic of hypothesis tests, which the sign test reuses
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · graded hypothesis-testing questions with answers
- explore: [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory · sampling and testing by simulation
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Wilcoxon tests](#math.fm.wilcoxon) replace signs by ranks, so the sizes of the differences count, at the cost of one extra assumption: symmetry.
