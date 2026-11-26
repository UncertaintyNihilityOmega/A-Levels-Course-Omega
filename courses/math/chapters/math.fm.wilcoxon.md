@chapter math.fm.wilcoxon
@title Wilcoxon tests
@level fm
@paper CAIE 9231 Paper 4
@time 6–7 hours
@summary The Wilcoxon tests keep the idea of the sign test but use the sizes of the differences through their ranks. You will carry out the signed-rank test for one sample and for matched pairs, and the rank-sum test for two independent samples, using the MF19 tables for small samples and a normal approximation for large ones, know why symmetry is needed, and choose between the five tests of the course.
:::why
The sign test is safe but wasteful: a difference of 0.1 and a difference of 100 count the same. Wilcoxon's idea is to rank the differences by size, so a big difference carries more weight than a small one, while still never using the actual values (so one wild outlier cannot dominate as it does in a t-test). The price is one extra assumption, symmetry. The Wilcoxon tests are the standard non-parametric tests for medians and for comparing two samples, and they appear in Paper 4 alongside the sign test.
:::

**Before you start**, you need the sign test and the idea of a non-parametric test from [Non-parametric tests: the sign test](#math.fm.nonpar), the normal approximation with a continuity correction from [The normal distribution](#math.s1.normal), and the sum of the first \(n\) integers from [Summation of series](#math.fm.series). The t-tests that these tests are an alternative to are in [Comparing two means](#math.fm.twosample).

:::try Warm-up
Q: In a sign test, 2 of 10 differences are negative. For \(H_1\): median difference \(> 0\), find the \(p\)-value. (from [Non-parametric tests: the sign test](#math.fm.nonpar))
A: \(S \sim B(10, \tfrac12)\), and \(P(S \le 2) = \dfrac{56}{1024} = 0.0547\). That is more than 0.05, so do not reject \(H_0\).
Q: Find \(1 + 2 + 3 + \dots + 12\), using the formula for \(\sum r\). (from [Summation of series](#math.fm.series))
A: \(\dfrac{n(n + 1)}{2} = \dfrac{12 \times 13}{2} = 78\).
Q: \(Y \sim N(150, 1225)\). Find \(P(Y < 88.5)\). (from [The normal distribution](#math.s1.normal))
A: \(z = \dfrac{88.5 - 150}{35} = -1.757\), so \(P = 0.0394\).
:::

## Ranks, and why the sizes matter

To **rank** a set of values, put them in order from smallest to largest and number them \(1, 2, 3, \dots\). The smallest value has rank 1.

:::def Rank
The position of a value when all the values are arranged in increasing order: the smallest has rank 1 and the largest has rank \(n\). (In 9231 questions no two values are equal, so ranks are never shared.)
:::

:::eg Rank the values 14.2, 9.8, 17.5, 11.0, 12.6, 9.1.
In increasing order: 9.1, 9.8, 11.0, 12.6, 14.2, 17.5.

| Value | 14.2 | 9.8 | 17.5 | 11.0 | 12.6 | 9.1 |
|---|---|---|---|---|---|---|
| Rank | 5 | 2 | 6 | 3 | 4 | 1 |

**Check**: the ranks use every number from 1 to 6 once, and they add up to \(\tfrac{6 \times 7}{2} = 21\).
:::

Why not stay with signs? Look at two data sets of five differences from a claimed median. Both have 2 positive and 3 negative signs, so the sign test treats them identically.

| | Differences | Positive ones are |
|---|---|---|
| Set A | \(+1, +2, -9, -8, -7\) | the two smallest in size |
| Set B | \(+9, +8, -1, -2, -7\) | the two largest in size |

In Set A the data lie mostly well below the claimed median; in Set B they are balanced by large positive differences. Ranks capture that. Rank the sizes \(|d|\) and add the ranks of the positive differences: in Set A the positive ranks are 1 and 2 (sum 3), in Set B they are 5 and 4 (sum 9). The sum of the positive ranks is a number that is small when the positive differences are small, and it uses the sizes without needing the actual values.

## What the Wilcoxon tests assume: symmetry

The Wilcoxon signed-rank test needs an extra assumption that the sign test does not.

:::def Symmetrical distribution
A distribution is symmetrical about a value \(m\) if the probability density at \(m + a\) equals the density at \(m - a\) for every \(a\). The centre of symmetry is then the median (and the mean, if it exists).
:::

Suppose the population is symmetrical about the median \(m_0\) claimed in \(H_0\). Then a deviation of \(+5\) is exactly as likely as a deviation of \(-5\): whether a value is above or below \(m_0\) is a fair coin toss **and** it tells you nothing about how far from \(m_0\) the value is. So when you rank the sizes \(|x - m_0|\), each rank carries a plus or a minus sign independently with probability \(\tfrac12\). If the population were skewed, positive deviations would tend to be larger than negative ones, even when the median is right, and the sums of ranks would be pushed one way: you would reject true hypotheses too often.

:::key Basis of the Wilcoxon signed-rank test
If the population (or, for matched pairs, the population of differences) is **symmetrical** about the hypothesised median, then under \(H_0\) each of the ranks \(1, 2, \dots, n\) of the sizes \(|d|\) is equally likely to belong to a positive or a negative difference, independently. The sum of the ranks of the positive differences, \(P\), is then the sum of a random subset of \(\{1, \dots, n\}\), whose distribution can be counted exactly.
:::

:::warn Wilcoxon needs symmetry, the sign test does not
"The sign test does not need symmetry" is a mark in the exam. If the differences are clearly skewed (a histogram with a long tail on one side, or one huge difference), say that the Wilcoxon signed-rank test is not appropriate and use the sign test, which needs only independence. The rank-sum test and the signed-rank test are both valid only for symmetrical distributions, so check the shape when you can.
:::

## The signed-rank test for one sample

:::steps
1. Let \(m\) be the population median. State \(H_0: m = m_0\) and \(H_1\).
2. Find each difference \(d = x - m_0\) (all non-zero in 9231).
3. Rank the **absolute values** \(|d|\): smallest \(|d|\) gets rank 1.
4. Add the ranks of the positive differences, \(P\), and of the negative differences, \(Q\). Check \(P + Q = \dfrac{n(n + 1)}{2}\).
5. Take \(T = \min(P, Q)\), the smaller of the two.
6. From the MF19 table, find the largest value of \(T\) that leads to rejection, for your \(n\), level and number of tails. **Reject \(H_0\) if \(T\) is less than or equal to it.**
7. Conclude in context.
:::

:::key The MF19 signed-rank table
MF19 gives, for \(n = 6\) to 20, "the largest value of \(T\) which will lead to rejection of the null hypothesis": reject when \(T \le\) table value. The columns are one-tailed levels 0.05, 0.025, 0.01, 0.005, which are the same as two-tailed 0.1, 0.05, 0.02, 0.01. A dash means rejection is impossible at that level for that \(n\). For \(n > 20\) use the normal approximation below. The values come from counting every possible set of signs: each is the largest \(T\) with \(P(T \le t)\) at most the level.
:::

The table, with the two-tailed level in brackets:

| \(n\) | 0.05 (2-tail 0.1) | 0.025 (0.05) | 0.01 (0.02) | 0.005 (0.01) |
|---|---|---|---|---|
| 6 | 2 | 0 | – | – |
| 7 | 3 | 2 | 0 | – |
| 8 | 5 | 3 | 1 | 0 |
| 9 | 8 | 5 | 3 | 1 |
| 10 | 10 | 8 | 5 | 3 |
| 11 | 13 | 10 | 7 | 5 |
| 12 | 17 | 13 | 9 | 7 |
| 13 | 21 | 17 | 12 | 9 |
| 14 | 25 | 21 | 15 | 12 |
| 15 | 30 | 25 | 19 | 15 |
| 16 | 35 | 29 | 23 | 19 |
| 17 | 41 | 34 | 27 | 23 |
| 18 | 47 | 40 | 32 | 27 |
| 19 | 53 | 46 | 37 | 32 |
| 20 | 60 | 52 | 43 | 37 |

To see where a table value comes from, take \(n = 4\) and list the 16 equally likely ways the ranks 1, 2, 3, 4 can carry plus signs. The sum \(P\) of the positive ranks takes these values:

| \(P\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ways | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 |

(For example \(P = 3\) happens for \(\{3\}\) and \(\{1, 2\}\).) So \(P(P \le 1) = \tfrac{2}{16} = 0.125\) and \(P(P \le 0) = \tfrac1{16}\). For larger \(n\) the same counting gives the table.

:::eg A manufacturer claims that the median standby time of a phone battery is 50 hours. The standby times of 9 randomly chosen batteries, in hours, are 44, 48, 51, 43, 41, 53, 46, 42, 45. Assuming the population is symmetrical, test at the 5% level whether the median is different from 50 hours.
Let \(m\) be the population median standby time. \(H_0: m = 50\) and \(H_1: m \ne 50\).

The differences \(d = x - 50\) and the ranks of \(|d|\):

| \(x\) | 44 | 48 | 51 | 43 | 41 | 53 | 46 | 42 | 45 |
|---|---|---|---|---|---|---|---|---|---|
| \(d\) | \(-6\) | \(-2\) | \(+1\) | \(-7\) | \(-9\) | \(+3\) | \(-4\) | \(-8\) | \(-5\) |
| rank of \(\lvert d\rvert\) | 6 | 2 | 1 | 7 | 9 | 3 | 4 | 8 | 5 |

The positive differences have ranks 1 and 3, so \(P = 4\). The negative ranks add to \(Q = 6 + 2 + 7 + 9 + 4 + 8 + 5 = 41\). **Check**: \(4 + 41 = 45 = \tfrac{9 \times 10}{2}\).

\(T = \min(4, 41) = 4\). The test is two-tailed at 5%, so use the column "two-tailed 0.05" (one-tailed 0.025) with \(n = 9\): the table value is 5.

Since \(4 \le 5\), reject \(H_0\). There is sufficient evidence at the 5% level that the median standby time is not 50 hours (it seems to be lower: most differences are negative).
:::

:::warn Which sum for a one-tailed test
For a one-tailed test the data must lean the way \(H_1\) says before the table is any use. With \(H_1: m > m_0\) you expect large positive differences, so \(Q\) should be small; the statistic is then \(Q\). With \(H_1: m < m_0\) the statistic is \(P\). If \(\min(P, Q)\) belongs to the wrong sign, \(H_0\) cannot be rejected, however small \(T\) is.
:::

:::eg (Exam style) A farmer claims that the median mass of the eggs from her hens is 60 g. A random sample of 8 eggs has masses, in grams, 56, 61, 52, 62, 57, 50, 55, 53. The distribution of egg masses is known to be symmetrical. Use a Wilcoxon signed-rank test at the 5% level to test whether the median mass is less than 60 g.
Let \(m\) be the population median mass. \(H_0: m = 60\) and \(H_1: m < 60\). [B1]

The differences \(d = x - 60\) and the ranks of \(|d|\) are

| \(d\) | \(-4\) | \(+1\) | \(-8\) | \(+2\) | \(-3\) | \(-10\) | \(-5\) | \(-7\) |
|---|---|---|---|---|---|---|---|---|
| rank of \(\lvert d\rvert\) | 4 | 1 | 7 | 2 | 3 | 8 | 5 | 6 |

[M1 M1] (differences, then signed ranks)
The positive differences have ranks 1 and 2, so \(P = 3\) (and \(Q = 36 - 3 = 33\)). \(H_1\) says the median is smaller, so we expect few positive differences and \(T = P = 3\). [A1]

For \(n = 8\), a one-tailed test at 5%, MF19 gives 5.

Since \(3 \le 5\), reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the median egg mass is less than 60 g. [A1]
:::

## Matched pairs

When each subject gives a pair of readings, find the difference for each pair and run the single-sample signed-rank test on the differences, with \(m_0 = 0\). The population of differences must be symmetrical (the two populations themselves need not be).

:::key Wilcoxon matched-pairs signed-rank test
For pairs \((x_i, y_i)\) let \(d_i = x_i - y_i\) and let \(m\) be the population median of the differences. To test whether the populations are identical, \(H_0: m = 0\). Rank \(|d_i|\), find \(P\) and \(Q\), and take \(T = \min(P, Q)\) for a two-tailed test. Reject \(H_0\) if \(T\) is less than or equal to the MF19 value for \(n\) pairs.
:::

:::eg (Exam style) Ten drivers have their reaction time, in milliseconds, measured before and after a driving-awareness course.

| Driver | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Before | 312 | 295 | 340 | 301 | 288 | 325 | 310 | 297 | 333 | 318 |
| After | 298 | 286 | 343 | 279 | 281 | 307 | 315 | 286 | 308 | 302 |

(a) Assuming that the differences come from a symmetrical population, use a Wilcoxon matched-pairs signed-rank test at the 5% level to test whether the course reduces the median reaction time. (b) Carry out a sign test at the 5% level on the same data. State whether the two tests agree. (c) Explain any difference.
(a) Let \(m\) be the population median of (before) \(-\) (after). \(H_0: m = 0\) and \(H_1: m > 0\). [B1]

Differences \(d\) (before \(-\) after) and the ranks of \(|d|\):

| Driver | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| \(d\) | 14 | 9 | \(-3\) | 22 | 7 | 18 | \(-5\) | 11 | 25 | 16 |
| rank of \(\lvert d\rvert\) | 6 | 4 | 1 | 9 | 3 | 8 | 2 | 5 | 10 | 7 |

[M1 M1] (differences, then signed ranks)
\(H_1\) predicts mostly positive differences, so the relevant sum is that of the negative differences: \(Q = 1 + 2 = 3\) (and \(P = 55 - 3 = 52\)). \(T = 3\). [A1]

For \(n = 10\), one-tailed 5%, MF19 gives 10.

Since \(3 \le 10\), reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the course reduces the median reaction time. [A1]

(b) Let \(S\) be the number of positive differences, \(S \sim B(10, \tfrac12)\) under \(H_0\). There are 2 negative differences, and for \(H_1\) we need
\[P(\text{at most 2 negative}) = \frac{1 + 10 + 45}{1024} = 0.0547\] [B1]
Since \(0.0547 > 0.05\), do not reject \(H_0\) [M1]: the sign test finds insufficient evidence at 5%, so the two tests **disagree**. [A1]

(c) The sign test uses only the number of drivers who got slower (2 of 10). The Wilcoxon test also uses the sizes: the two drivers who got slower did so by the smallest amounts (3 ms and 5 ms), while the improvements are large. That extra information makes the Wilcoxon test more powerful, so it detects the effect. [B1] [B1]
:::

:::exam Contrasting conclusions
When the Wilcoxon and sign tests disagree, the explanation the examiner wants is that the Wilcoxon test takes account of the **magnitudes** (through the ranks) while the sign test only counts signs, so the Wilcoxon test is more powerful. The sign test is the safer choice only if the differences may not be symmetrical.
:::

## Large samples: the normal approximation for signed-rank

The table stops at \(n = 20\). For larger \(n\) (and "where appropriate") the sum of the ranks \(P\) is approximately normal. The mean and variance are on MF19.

:::key Normal approximation for the signed-rank statistic
For \(n\) differences, under \(H_0\), the sum of the positive ranks \(P\) (and likewise \(Q\) and \(T\) when you use them as the statistic) has
\[\text{mean } \frac{n(n + 1)}{4} \qquad \text{variance } \frac{n(n + 1)(2n + 1)}{24}\]
and for large \(n\), \(P \approx N\left(\dfrac{n(n + 1)}{4}, \dfrac{n(n + 1)(2n + 1)}{24}\right)\). Use a continuity correction, because \(P\) takes whole-number values: for a lower tail \(P(P \le t) \approx P(Y < t + 0.5)\).
:::

:::proof Why the mean and variance are \(\tfrac{n(n+1)}{4}\) and \(\tfrac{n(n+1)(2n+1)}{24}\)
Write \(P = \sum_{r=1}^{n} r\,I_r\), where \(I_r = 1\) if the difference with rank \(r\) is positive and 0 otherwise.
1. Under \(H_0\) and symmetry, each \(I_r\) is 1 with probability \(\tfrac12\), independently of the others.
2. So \(E(I_r) = \tfrac12\) and \(\mathrm{Var}(I_r) = \tfrac14\).
3. \(E(P) = \sum r \times \tfrac12 = \tfrac12 \cdot \dfrac{n(n + 1)}{2} = \dfrac{n(n + 1)}{4}\), using \(\sum r\).
4. The \(I_r\) are independent, so \(\mathrm{Var}(P) = \sum r^2 \times \tfrac14 = \tfrac14 \cdot \dfrac{n(n + 1)(2n + 1)}{6}\), using \(\sum r^2\) from [Summation of series](#math.fm.series).
5. Simplifying step 4 gives \(\dfrac{n(n + 1)(2n + 1)}{24}\).
:::

:::eg (Exam style) A random sample of 24 observations is taken from a symmetrical population to test \(H_0: m = 35\) against \(H_1: m < 35\). The differences from 35 are ranked by size, and the sum of the ranks of the positive differences is \(P = 88\). Test at the 5% level.
\(H_0: m = 35\), \(H_1: m < 35\). Small \(P\) supports \(H_1\), so the statistic is \(P = 88\). [B1]

Since \(n = 24 > 20\) the table cannot be used. Under \(H_0\),
\[\text{mean} = \frac{24 \times 25}{4} = 150, \qquad \text{variance} = \frac{24 \times 25 \times 49}{24} = 1225\] [B1 B1]
so \(P \approx Y \sim N(150, 35^2)\).

\[P(P \le 88) \approx P(Y < 88.5)\] [M1]
\[z = \frac{88.5 - 150}{35} = -1.757 \qquad P(Z < -1.757) = 0.0394\] [A1]
Since \(0.0394 < 0.05\) (equivalently \(-1.757 < -1.645\)), reject \(H_0\). There is sufficient evidence at the 5% level that the median is less than 35. [A1]
:::

:::warn Continuity correction goes the right way
For a lower tail \(P(P \le 88)\), the boundary is \(88.5\) (add 0.5), as the whole of the value 88 must be included. Using 87.5 gives \(z = -1.786\), a different answer. For an upper tail \(P(P \ge a)\) use \(a - 0.5\).
:::

## The rank-sum test for two independent samples

Now there are two separate samples, with no pairing. Sample sizes may differ. The question is whether the two populations are the same, or one tends to take larger values.

The idea: put the two samples together, rank all \(m + n\) values from 1 upwards, then add up the ranks that belong to one sample. If the populations are identical, the ranks are shared out randomly and the sums are about what you would expect from their sizes. If one population tends to be larger, its values collect the high ranks.

:::steps
1. State \(H_0\): the two populations are identical (in particular, they have the same median), and \(H_1\): one is shifted, in the direction or directions stated.
2. Let \(m\) be the size of the **smaller** sample and \(n\) the size of the larger (\(m \le n\)); if the sizes are equal, either sample can be the first one.
3. Rank all \(m + n\) values together, smallest first. Let \(R_m\) be the sum of the ranks of the smaller sample.
4. Find \(R_m' = m(n + m + 1) - R_m\): the sum the ranks would have if the ranking were reversed.
5. \(W = \min(R_m, R_m')\). Compare with the MF19 value for \(m\), \(n\), level and tails: reject \(H_0\) if \(W \le\) the table value.
6. Conclude in context.
:::

:::key The rank-sum table and statistic
MF19 gives the largest value of \(W\) which leads to rejection, for \(m \le n\), \(m\) and \(n\) from 3 to 10, with one-tailed levels 0.05, 0.025, 0.01 (two-tailed 0.1, 0.05, 0.02). \(W\) is the smaller of \(R_m\) and \(m(n + m + 1) - R_m\). Reject when \(W \le\) table value. For larger samples use the normal approximation for \(R_m\), below.
:::

An extract of the table (rows \(m\), columns \(n\); the full table goes up to 10). One-tailed 5% (two-tailed 10%):

| \(m \backslash n\) | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| 3 | 6 | 6 | 7 | 8 | 8 | 9 |
| 4 | | 11 | 12 | 13 | 14 | 15 |
| 5 | | | 19 | 20 | 21 | 23 |
| 6 | | | | 28 | 29 | 31 |
| 7 | | | | | 39 | 41 |
| 8 | | | | | | 51 |

One-tailed 2.5% (two-tailed 5%), where "–" means rejection is impossible:

| \(m \backslash n\) | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| 3 | – | – | 6 | 7 | 7 | 8 |
| 4 | | 10 | 11 | 12 | 13 | 14 |
| 5 | | | 17 | 18 | 20 | 21 |
| 6 | | | | 26 | 27 | 29 |
| 7 | | | | | 36 | 38 |
| 8 | | | | | | 49 |

One-tailed 1% (two-tailed 2%):

| \(m \backslash n\) | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| 3 | – | – | – | – | 6 | 6 |
| 4 | | – | 10 | 11 | 11 | 12 |
| 5 | | | 16 | 17 | 18 | 19 |
| 6 | | | | 24 | 25 | 27 |
| 7 | | | | | 34 | 35 |
| 8 | | | | | | 45 |

:::eg (Exam style) A factory has two machines, X and Y, filling pots. The times, in seconds, to fill a sample of pots are

- Machine X (8 pots): 41, 38, 47, 52, 44, 49, 40, 55
- Machine Y (6 pots): 36, 43, 39, 35, 46, 37

Use a Wilcoxon rank-sum test at the 5% level to test whether the median fill times of the two machines are different.
\(H_0\): the two populations of fill times are identical. \(H_1\): they are not (their medians differ). [B1]

The smaller sample is Y, so \(m = 6\) and \(n = 8\). Rank all 14 values:

| Time | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 43 | 44 | 46 | 47 | 49 | 52 | 55 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Machine | Y | Y | Y | X | Y | X | X | Y | X | Y | X | X | X | X |
| Rank | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

[M1]
Machine Y has ranks 1, 2, 3, 5, 8, 10, so \(R_m = 29\). [A1]

\(m(n + m + 1) - R_m = 6 \times 15 - 29 = 61\), so \(W = \min(29, 61) = 29\). [M1]

For \(m = 6\), \(n = 8\), a two-tailed test at 5% (one-tailed 2.5%), MF19 gives 29.

Since \(29 \le 29\), reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the median fill times of the machines differ (Y is quicker). [A1]
:::

:::warn Equality counts as rejection
The table value is "the largest value of \(W\) which leads to rejection", so \(W\) **equal** to the table value is in the critical region. In the example above \(W = 29\) and the table value is 29: reject. Do not write "\(W\) must be less than".
:::

:::warn Which sample, which sum
The statistic uses the sum of the ranks of the **smaller** sample. Using the larger sample's ranks, or the larger of the two sums, gives the wrong answer (the table is built for \(m \le n\)). For a one-tailed test, the sample you expect to have small values must have the small rank sum.
:::

### Large samples: the rank-sum normal approximation

:::key Normal approximation for \(R_m\)
When \(m\) or \(n\) is larger than 10, the sum of the ranks \(R_m\) of the sample of size \(m\) is approximately normal, with mean and variance (on MF19)
\[E(R_m) = \tfrac12 m(m + n + 1) \qquad \mathrm{Var}(R_m) = \frac{mn(m + n + 1)}{12}\]
Use a continuity correction: \(P(R_m \le r) \approx P(Y < r + 0.5)\) and \(P(R_m \ge r) \approx P(Y > r - 0.5)\).
:::

The mean is easy to remember. If the populations are identical, the \(m + n\) ranks have average \(\tfrac{m + n + 1}{2}\), and the sample's \(m\) ranks have a sum of \(m\) times that.

:::eg (Exam style) A botanist measures the heights of two independent random samples of seedlings grown with fertiliser A (12 plants) and fertiliser B (15 plants). The 27 heights are ranked together, and the sum of the ranks of the 12 plants with fertiliser A is 128. Test, at the 5% level, whether the median heights differ.
\(H_0\): the populations of heights are identical. \(H_1\): they are not. [B1]

\(m = 12\), \(n = 15\), \(R_m = 128\). Under \(H_0\):
\[E(R_m) = \tfrac12 \times 12 \times 28 = 168 \qquad \mathrm{Var}(R_m) = \frac{12 \times 15 \times 28}{12} = 420\] [B1 B1]
\(R_m \approx Y \sim N(168, 420)\), and 128 is in the lower tail:
\[P(R_m \le 128) \approx P(Y < 128.5)\] [M1]
\[z = \frac{128.5 - 168}{\sqrt{420}} = -1.927\] [A1]
The test is two-tailed, so compare \(-1.927\) with \(-1.960\). Since \(-1.927 > -1.960\) (the tail probability is \(0.0270 > 0.025\)), do not reject \(H_0\). There is not sufficient evidence at the 5% level that the median heights differ. [A1]
:::

## Choosing the right test

Five tests compare medians or means in this part of the course. The choice depends on how the data were collected and what you can assume.

| Situation | Normal population | Symmetrical, not normal | Shape unknown or skewed |
|---|---|---|---|
| One sample, test a centre | one-sample t-test (mean) | Wilcoxon signed-rank (median) | sign test (median) |
| Paired samples | paired t-test (mean of differences) | Wilcoxon matched-pairs signed-rank | paired sign test |
| Two independent samples | two-sample t-test, or a normal test for large samples | Wilcoxon rank-sum | (Wilcoxon rank-sum is the usual non-parametric choice) |

- Paired data (the same subjects twice, or matched subjects) use a paired test on the differences. Independent samples of different sizes, with no pairing, use the two-sample tests. Never use the rank-sum test on paired data.
- The sign test uses the fewest assumptions and the least information; the t-test the most of both; the Wilcoxon tests are in between.
- All the tests assume random samples.

:::eg (Exam style) The differences (time after \(-\) time before) in a paired experiment on 11 volunteers are, in seconds, 0.4, 0.9, 0.3, 1.1, 0.2, \(-0.1\), 0.6, 7.8, 0.5, \(-0.3\), 0.8. (a) Give a reason why a Wilcoxon matched-pairs signed-rank test might not be appropriate. (b) Test, at the 5% level, whether the median time is greater after than before, using a sign test.
(a) One difference, 7.8, is far larger than the rest, so the distribution of differences is probably skewed and not symmetrical, which the Wilcoxon test requires. [B1]

(b) Let \(m\) be the population median of the differences. \(H_0: m = 0\) and \(H_1: m > 0\). [B1]

There are 9 positive and 2 negative differences. Let \(S\) be the number of negative differences, \(S \sim B(11, \tfrac12)\) under \(H_0\).
\[P(S \le 2) = \frac{1 + 11 + 55}{2048} = 0.0327\] [M1 A1]
Since \(0.0327 < 0.05\), reject \(H_0\). There is sufficient evidence at the 5% level that the median time is greater after than before. [A1]
:::

:::exam What MF19 gives, and what it does not
MF19 gives: the two Wilcoxon tables (largest \(T\) or \(W\) leading to rejection, \(T\) and \(W\) being the smaller of two sums), and the mean and variance for the normal approximations. It does **not** give the sign-test rules (compute with \(B(n, \tfrac12)\)), the hypotheses, the ranking procedure or the formula \(m(n + m + 1) - R_m\) for the other sum. Learn those. Questions in 9231 never ask you to rank tied values or zero differences, so you do not need a rule for ties; a data set that has repeated values or outliers is, however, an accepted reason for saying a Wilcoxon test might not be appropriate.
:::

:::exam "Suggest why a Wilcoxon test might not be appropriate"
This one-mark question has been set with data in a stem-and-leaf diagram. The mark scheme accepted: the data has outliers, or is skewed, or lacks symmetry, so the population may not be symmetrical (and also a comment about tied ranks). State that the Wilcoxon test needs a symmetrical population and say what in the data suggests it is not. For a paired t-test the matching assumption is that the **population of differences** is normal: "the data are normal" does not earn the mark.
:::

:::board
The Wilcoxon signed-rank and rank-sum tests are the same tests as in other specifications, but the 9231 papers give the critical values in MF19 as "the largest value which leads to rejection" and never ask for tied ranks or zero differences. The description above is the 9231 version.
:::

:::eg Spot the error: a one-tailed Wilcoxon signed-rank test at the 5% level is applied to 7 differences from 0: \(+2, -9, +4, +1, -3, +6, +5\), with \(H_0: m = 0\) and \(H_1: m > 0\). The test is worth 5 marks.
A student wrote this answer.

Line 1: \(H_0: m = 0\), \(H_1: m > 0\)
Line 2: Order the differences: \(-9, -3, +1, +2, +4, +5, +6\), with ranks 1 to 7. The negative differences have ranks 1 and 2, so \(Q = 3\).
Line 3: For \(n = 7\), one-tailed 5%, the table value is 3. \(3 \le 3\), so reject \(H_0\).

Line 1 is correct. [B1] Line 3 compares the student's own \(T\) with the correct table value and draws the matching conclusion, which earns the comparison method mark. [M1]

**Line 2 ranks the signed differences, not their absolute values.** A negative difference is not "small": its **size** is what is ranked. This is a wrong method, so the ranking mark and the mark for \(T\) are lost. [M0] [A0] The conclusion in context needs correct working, so it is lost too. [A0] The student scores 2 out of 5.

Correct line 2: ranking \(|d|\): 1, 2, 3, 4, 5, 6, 9 gives ranks 1, 2, 3, 4, 5, 6, 7. The negative differences, \(-9\) and \(-3\), have ranks 7 and 3, so \(Q = 10\) (and \(P = 18\)). \(10 > 3\), so do not reject \(H_0\): there is not sufficient evidence at the 5% level that the median is greater than 0.
:::

:::try Practice
Q: Rank 31, 17, 24, 40, 12 from smallest to largest.
A: In order: 12, 17, 24, 31, 40. The ranks in the original order are 4, 2, 3, 5, 1.
Q: For 12 differences, what must \(P + Q\) equal, and if \(P = 25\), what is \(T\)?
A: \(P + Q = \dfrac{12 \times 13}{2} = 78\), so \(Q = 53\) and \(T = \min(25, 53) = 25\).
Q: The differences from a claimed median are \(+5, -2, +9, -4, +1, +7\). Find \(P\) and \(Q\).
A: \(|d|\) ranks: 1 \(\to\) 1, 2 \(\to\) 2, 4 \(\to\) 3, 5 \(\to\) 4, 7 \(\to\) 5, 9 \(\to\) 6. Positive differences (\(+5, +9, +1, +7\)) have ranks 4, 6, 1, 5, so \(P = 16\). Negative ones (\(-2, -4\)) have ranks 2 and 3, so \(Q = 5\). Check: \(16 + 5 = 21\).
Q: Use MF19 values from the chapter. For \(n = 12\) in a two-tailed test at 5%, \(T = 14\). Conclusion?
A: The table value (one-tailed 0.025) is 13. \(14 > 13\), so do not reject \(H_0\).
Q: A rank-sum test has samples of size 7 and 5. Which is \(m\)?
A: \(m = 5\), the smaller sample, and \(n = 7\).
Q: With \(m = 5\), \(n = 7\) and \(R_m = 36\), find \(W\).
A: \(m(n + m + 1) = 5 \times 13 = 65\), so the other sum is \(65 - 36 = 29\) and \(W = \min(36, 29) = 29\).
Q: For \(n = 30\) differences, state the mean and variance of \(P\) under \(H_0\).
A: Mean \(\dfrac{30 \times 31}{4} = 232.5\); variance \(\dfrac{30 \times 31 \times 61}{24} = 2363.75\).
Q: Which test: ten athletes' times in the morning and the evening, differences symmetrical but not normal?
A: Wilcoxon matched-pairs signed-rank test (paired data, symmetrical differences, not normal).
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ A magazine claims the median time to charge a certain phone is 250 minutes. A random sample of 8 phones has charge times 243, 261, 238, 255, 247, 236, 259, 249 minutes. Assuming the population is symmetrical, use a Wilcoxon signed-rank test at the 5% level to test whether the median is different from 250.
A: \(H_0: m = 250\), \(H_1: m \ne 250\). [B1]
\(d = -7, +11, -12, +5, -3, -14, +9, -1\). Ranks of \(|d|\): 4, 6, 7, 3, 2, 8, 5, 1. [M1]
\(P = 6 + 3 + 5 = 14\), \(Q = 22\), \(T = 14\). [A1]
Two-tailed 5%, \(n = 8\): table value 3.
\(14 > 3\): do not reject \(H_0\). [M1] There is not sufficient evidence at the 5% level that the median charge time is not 250 minutes. [A1]
Q: [5 marks] ★ Two independent samples of a plant's mass in grams are A: 9, 12, 10, 8 and B: 14, 15, 17, 22, 18, 11. Use a rank-sum test at the 5% level to test whether the median mass of A is less than that of B.
A: \(H_0\): the populations are identical; \(H_1\): the median mass of A is less than that of B. [B1]
\(m = 4\) (A), \(n = 6\). Combined ranks: 8 (1), 9 (2), 10 (3), 11 (4), 12 (5), 14 (6), 15 (7), 17 (8), 18 (9), 22 (10). [M1]
\(R_m = 1 + 2 + 3 + 5 = 11\); the other sum is \(4 \times 11 - 11 = 33\); \(W = 11\). [A1]
One-tailed 5%, \(m = 4\), \(n = 6\): table value 13.
\(11 \le 13\): reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the median mass of A is less than that of B. [A1]
Q: [6 marks] ★★ Nine students sit two tests. Test 1: 82, 75, 91, 68, 77, 85, 72, 88, 79. Test 2: 78, 77, 83, 65, 70, 86, 60, 79, 73. The differences (test 1 minus test 2) are from a symmetrical population. Use a Wilcoxon matched-pairs signed-rank test at the 5% level to test whether the median scores on the two tests are different.
A: \(H_0: m = 0\), \(H_1: m \ne 0\), where \(m\) is the median of the differences. [B1]
\(d = 4, -2, 8, 3, 7, -1, 12, 9, 6\). [M1]
Ranks of \(|d|\): 4, 2, 7, 3, 6, 1, 9, 8, 5. [M1]
\(Q = 2 + 1 = 3\) (negative differences), \(P = 42\), \(T = 3\). [A1]
Two-tailed 5%, \(n = 9\): table value 5.
\(3 \le 5\): reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the median scores differ. [A1]
Q: [6 marks] ★★ A random sample of 5 values from population A is 31, 25, 26, 29, 34, and an independent random sample of 7 values from population B is 27, 36, 42, 33, 40, 45, 39. Use a rank-sum test at the 5% level to test whether the populations are identical.
A: \(H_0\): the populations are identical, \(H_1\): they are not. [B1]
\(m = 5\) (the sample from A), \(n = 7\). Ranks of the combined values: 25 (1), 26 (2), 27 (3), 29 (4), 31 (5), 33 (6), 34 (7), 36 (8), 39 (9), 40 (10), 42 (11), 45 (12). [M1]
\(R_m = 1 + 2 + 4 + 5 + 7 = 19\). [A1] The other sum is \(5 \times 13 - 19 = 46\), so \(W = 19\). [M1]
Two-tailed 5%, \(m = 5\), \(n = 7\): table value 20.
\(19 \le 20\): reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the populations differ. [A1]
Q: [5 marks] ★★ A symmetrical population has median \(m\). To test \(H_0: m = 100\) against \(H_1: m < 100\), 30 values are ranked by their distance from 100, and the sum of the ranks of those above 100 is 150. Use a normal approximation to test at the 5% level.
A: \(H_0: m = 100\), \(H_1: m < 100\); the statistic is \(P = 150\). [B1]
Mean \(\dfrac{30 \times 31}{4} = 232.5\) [B1], variance \(\dfrac{30 \times 31 \times 61}{24} = 2363.75\). [B1]
\(z = \dfrac{150.5 - 232.5}{\sqrt{2363.75}} = -1.687\). [M1]
\(-1.687 < -1.645\), so reject \(H_0\). There is sufficient evidence at the 5% level that the median is less than 100. [A1]
Q: [11 marks] (#math.fm.nonpar) ★★★ Nine people count their errors in a typing test before and after a course. Before: 61, 48, 70, 55, 62, 77, 53, 66, 74. After: 55, 50, 61, 51, 63, 66, 46, 63, 62. (a) Assuming the differences are from a symmetrical distribution, use a Wilcoxon matched-pairs signed-rank test at the 5% level to test whether the course reduces the median number of errors. (b) Use a sign test at the 5% level on the same data. (c) Explain why the two tests reach different conclusions.
H: Let \(d\) = before \(-\) after. The course reduces errors if \(d\) is mostly positive, so the sum to look at is the one for the negative differences.
H: In (b), count the negative differences and use \(B(9, \tfrac12)\).
H: For (c), compare what the two tests use from the data.
A: (a) Let \(m\) be the population median of (before) \(-\) (after). \(H_0: m = 0\), \(H_1: m > 0\). [B1]
\(d = 6, -2, 9, 4, -1, 11, 7, 3, 12\). [M1] Ranks of \(|d|\): 5, 2, 7, 4, 1, 8, 6, 3, 9. [M1]
\(Q = 2 + 1 = 3\), \(P = 42\), and \(T = Q = 3\). [A1]
One-tailed 5%, \(n = 9\): table value 8.
\(3 \le 8\): reject \(H_0\). [M1] There is sufficient evidence at the 5% level that the course reduces the median number of errors. [A1]
(b) There are 2 negative differences out of 9, \(S \sim B(9, \tfrac12)\). \(P(S \le 2) = \dfrac{1 + 9 + 36}{512} = 0.0898\). [M1 A1]
\(0.0898 > 0.05\): do not reject \(H_0\). [A1]
(c) The two negative differences are the smallest in size (1 and 2). The Wilcoxon test uses this through the ranks, and the sign test only counts them, so the Wilcoxon test is the more powerful. [B1] [B1]
Q: [9 marks] ★★★ Random samples of 11 and 14 values come from two populations. The 25 values are ranked together, and the sum of the ranks of the sample of 11 is 176. (a) Explain why the normal approximation, not the table, is used. (b) State the mean and variance of the sum of ranks of the sample of 11 under \(H_0\). (c) Test at the 10% level, two-tailed, whether the populations are identical. (d) State one assumption you need.
H: Remember \(m\) is the size of the smaller sample.
H: \(R_m = 176\) is in the upper tail, so use \(P(R_m \ge 176) \approx P(Y > 175.5)\).
H: For (d), think about independence and shape.
A: (a) The table of MF19 covers samples only up to size 10, and one sample here has size 14. [B1]
(b) \(m = 11\), \(n = 14\). Mean \(\tfrac12 \times 11 \times 26 = 143\) [B1], variance \(\dfrac{11 \times 14 \times 26}{12} = 333.67\) (3 s.f.). [B1]
(c) \(H_0\): the populations are identical; \(H_1\): they are not. [B1]
\(P(R_m \ge 176) \approx P(Y > 175.5)\), \(z = \dfrac{175.5 - 143}{\sqrt{333.67}} = 1.779\) [M1 A1]
The tail probability is 0.0376, which is less than 0.05 (each tail of a two-tailed 10% test), so reject \(H_0\). [M1]
There is sufficient evidence at the 10% level that the populations differ. [A1]
(d) The samples are random and independent of each other, (and the populations are similar in shape, differing at most in position). [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ (a) Show that a two-tailed signed-rank test at the 5% level cannot reject \(H_0\) when \(n = 5\) but can when \(n = 6\). (b) For \(n = 7\), list the sets of ranks whose sum is at most 2 and hence confirm the MF19 value 2 for a one-tailed test at the 2.5% level.
H: The smallest possible value of \(P\) is 0, which happens for exactly one of the \(2^n\) sign patterns.
H: Each tail of a two-tailed 5% test must have probability at most 0.025.
A: (a) \(P(P = 0) = \dfrac{1}{2^n}\). For \(n = 5\) this is \(\dfrac1{32} = 0.03125 > 0.025\), so even the most extreme result cannot be in the critical region. [M1 A1] For \(n = 6\), \(P(P \le 0) = \dfrac1{64} = 0.0156 \le 0.025\) but \(P(P \le 1) = \dfrac{2}{64} = 0.03125 > 0.025\), so the table value is 0. [A1]
(b) Sets with sum at most 2: \(\{\}\) (sum 0), \(\{1\}\), \(\{2\}\). [B1] So \(P(P \le 2) = \dfrac{3}{128} = 0.0234 \le 0.025\). [M1] The set \(\{3\}\) and \(\{1, 2\}\) both have sum 3, giving \(P(P \le 3) = \dfrac{5}{128} = 0.039 > 0.025\), so the largest value that leads to rejection is 2. [A1 A1]
Q: [6 marks] ★★★ Samples of sizes \(m\) and \(n\) are ranked together, giving ranks \(1, \dots, m + n\). (a) Show that if the ranking is reversed (the largest value gets rank 1), the sum of the ranks of the sample of size \(m\) becomes \(m(m + n + 1) - R_m\). (b) Hence explain why \(W = \min(R_m, m(m + n + 1) - R_m)\) is a sensible statistic for a two-tailed test. (c) For \(m = n = 3\), show that a two-tailed test at the 5% level can never reject, but a one-tailed test at 5% rejects when \(R_m \le 6\).
H: A value of rank \(r\) becomes rank \(m + n + 1 - r\).
H: In (c), list the \(\binom{6}{3} = 20\) equally likely sets of ranks; how many have sum 6 or less?
A: (a) A value with rank \(r\) gets rank \(m + n + 1 - r\) when the order is reversed. [M1] Summing over the \(m\) values: \(m(m + n + 1) - R_m\). [A1]
(b) A very small \(R_m\) means sample \(m\) holds the lowest values; a very large \(R_m\) means it holds the highest. In terms of reversed ranks, an extreme in the upper tail is the same as an extreme in the lower tail, so the smaller of the two sums measures how extreme the result is, whichever way. [B1]
(c) Only \(\{1, 2, 3\}\) has sum 6, so \(P(R_m \le 6) = \dfrac{1}{20} = 0.05\). [M1 A1] A one-tailed test at 5% rejects for \(R_m \le 6\), as in MF19. For a two-tailed test, each tail would need probability at most 0.025, but the smallest tail probability is 0.05, so it can never reject. [A1]
:::

:::quiz
? In a Wilcoxon signed-rank test, which values are ranked?
+ The absolute values of the differences \(|x - m_0|\)
- The original values \(x\)
- The signed differences \(x - m_0\), so the most negative has rank 1
- The positive differences only
> The sizes of the differences are ranked, then each rank is given its sign back. Ranking the signed differences is the commonest error.
? For 10 differences, \(P = 17\). What is \(Q\)?
+ \(38\)
- \(17\)
- \(55\)
- \(28\)
> \(P + Q = \dfrac{10 \times 11}{2} = 55\), so \(Q = 38\). The test statistic is then \(T = \min(17, 38) = 17\) for a two-tailed test.
? A Wilcoxon signed-rank test at the 5% level (two-tailed), \(n = 11\), gives \(T = 10\). The MF19 value is 10. What is the conclusion?
+ Reject \(H_0\), because \(T\) equals the largest value that leads to rejection
- Do not reject \(H_0\), because \(T\) must be less than the table value
- Reject \(H_1\)
- The test cannot be used because \(n > 10\)
> MF19 gives "the largest value of \(T\) which will lead to rejection", so equality rejects.
? Which assumption does the signed-rank test need that the sign test does not?
+ The population (or the differences) is symmetrical
- The population is normal
- The samples are random
- The population has a known variance
> Symmetry is the extra assumption. Randomness is needed by every test, and normality only by the t-test.
? In a rank-sum test the samples have sizes 9 and 6. Which sample's ranks are summed to give \(R_m\)?
+ The sample of size 6, the smaller one
- The sample of size 9
- Whichever has the larger sum
- Both, added together
> The table is built for \(m \le n\) with \(R_m\) from the smaller sample. Both sums together always make \(\tfrac{(m + n)(m + n + 1)}{2}\), which tests nothing.
? Which test is suitable for two independent samples of different sizes from symmetrical populations that are not normal?
+ The Wilcoxon rank-sum test
- The Wilcoxon matched-pairs signed-rank test
- The paired t-test
- The paired sign test
> The data are not paired, so the paired tests are wrong. With no normality, the rank-sum test is the non-parametric choice.
? For \(n = 30\) in the signed-rank normal approximation, what is the mean of \(P\)?
+ \(232.5\)
- \(465\)
- \(15.5\)
- \(2363.75\)
> The mean is \(\dfrac{n(n + 1)}{4} = 232.5\). 465 is \(\tfrac{n(n + 1)}{2}\), the total of the ranks, and 2363.75 is the variance.
:::

:::checklist What you can now do
- [ ] I can rank data and explain why the Wilcoxon tests use ranks to take account of the sizes of the differences.
- [ ] I can state why the Wilcoxon tests are valid only for symmetrical distributions, and when to prefer the sign test.
- [ ] I can carry out a single-sample Wilcoxon signed-rank test, finding \(P\), \(Q\) and \(T\) and using the MF19 table.
- [ ] I can carry out a Wilcoxon matched-pairs signed-rank test on paired data and compare it with a sign test.
- [ ] I can carry out a Wilcoxon rank-sum test, finding \(R_m\) for the smaller sample and \(W\), and using the MF19 table.
- [ ] I can use the normal approximations \(N\left(\tfrac{n(n + 1)}{4}, \tfrac{n(n + 1)(2n + 1)}{24}\right)\) and \(N\left(\tfrac12 m(m + n + 1), \tfrac{mn(m + n + 1)}{12}\right)\) with a continuity correction.
- [ ] I can choose between the sign, signed-rank, rank-sum, paired t and two-sample t tests, and justify the choice.
:::

:::recap
- Rank the sizes: the smallest has rank 1. The Wilcoxon tests use ranks, so sizes count but outliers cannot dominate.
- Signed-rank: rank \(|d|\), \(P\) = sum of positive ranks, \(Q\) = sum of negative ranks, \(P + Q = \tfrac{n(n + 1)}{2}\), \(T = \min(P, Q)\); reject if \(T \le\) the MF19 value. One-tailed tests need the data to lean the way \(H_1\) says.
- The signed-rank tests need a symmetrical distribution (of the population, or of the differences); the sign test does not.
- Matched pairs: take differences, then signed-rank.
- Rank-sum: \(m \le n\), \(R_m\) from the smaller sample, \(W = \min(R_m, m(n + m + 1) - R_m)\); reject if \(W \le\) table value.
- Normal approximations: signed-rank mean \(\tfrac{n(n + 1)}{4}\), variance \(\tfrac{n(n + 1)(2n + 1)}{24}\); rank-sum mean \(\tfrac12 m(m + n + 1)\), variance \(\tfrac{mn(m + n + 1)}{12}\); continuity correction \(\pm 0.5\).
- Wilcoxon is more powerful than the sign test because it uses magnitudes; the t-test is more powerful still when the data are normal.
:::

:::links
- practise: [Two-sample tests and intervals](https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples) · Khan Academy · the comparing-two-groups logic the rank-sum test shares
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · hypothesis-testing practice with answers
- explore: [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory · see how sample statistics vary
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Probability generating functions](#math.fm.pgf) turns a probability distribution into a function, so that means, variances and sums of independent variables come from algebra and calculus.
