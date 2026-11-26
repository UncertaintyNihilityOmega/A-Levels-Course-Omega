@chapter math.fm.mock.p4
@title Mock Paper 4: Further Probability and Statistics
@level mock
@paper CAIE 9231 Paper 4
@time 1 h 30 min
@summary A complete original mock for 9231 Paper 4 (Further Probability and Statistics): 6 questions, 50 marks, 1 hour 30 minutes, laid out like the real papers (marks 7, 10, 8, 7, 9, 9) and covering a two-sample normal test, a piecewise PDF with the CDF of a related variable, a chi-squared goodness-of-fit test, a pooled t confidence interval, a Wilcoxon matched-pairs test against a sign test, and a probability generating function. Full mark scheme with accepted alternatives and every critical value; sit it in one go, mark yourself and see which chapters to revise.

:::why
Paper 4 is the Further Probability and Statistics paper: 50 marks in 90 minutes, six or so questions, each a complete test or a calculation with a probability distribution. The marks are won by two habits: setting a test out in the order the mark scheme rewards (hypotheses, test statistic, critical value, comparison, conclusion in context), and keeping exact arithmetic in the calculus and generating-function questions. This mock has the same number of questions, the same spread of marks and the same kinds of task as the real papers, but every question is new. Do it under exam conditions first, then use the mark scheme to see what the examiner is looking for line by line.
:::

:::exam Instructions
- Answer **all** questions. The total is **50 marks** and you have **1 hour 30 minutes**.
- You will need the list of formulae **MF19**, which contains the tables of the normal, \(t\), \(\chi^2\) and Wilcoxon distributions that you need. You should use a calculator where appropriate: only a scientific calculator, no graphical or symbolic algebra calculator.
- You must show all necessary working clearly; **no marks will be given for unsupported answers from a calculator**.
- Give non-exact numerical answers correct to **3 significant figures**, or **1 decimal place for angles in degrees**, unless the question says otherwise.
- The number of marks for each question or part question is shown in brackets [ ]. Roughly one and three-quarter minutes per mark leaves a few minutes at the end.
- In a hypothesis test, state your hypotheses, show the test statistic and the critical value or probability you compare it with, and end with a conclusion **in the context of the question**.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::tip A time plan
At 1.8 minutes per mark the paper needs about 90 minutes, so aim for about 1.5 minutes per mark and keep the last ten to twelve minutes to go back. A reasonable split is Question 1: 10 min, Question 2: 15 min, Question 3: 12 min, Question 4: 10 min, Question 5: 13 min, Question 6: 13 min, which leaves about 17 minutes. In every test, write the hypotheses before touching a calculator: they are the first mark and they tell you which tail you are in.
:::

:::try
Q: [7 marks] (#math.fm.twosample) A courier company has two depots, \(P\) and \(Q\). The depot manager at \(P\) believes that parcels from \(P\) take longer to deliver than parcels from \(Q\). The delivery time, in minutes, is recorded for a random sample of \(45\) parcels from \(P\), with \(\sum x = 1962\) and \(\sum (x - \bar x)^2 = 1584\), and for a random sample of \(60\) parcels from \(Q\), with \(\sum y = 2472\) and \(\sum (y - \bar y)^2 = 2891\).

(a) Test the manager's belief at the 5% significance level. [6]

(b) Explain why it is not necessary to assume that the delivery times are normally distributed. [1]
A: (a) Let \(\mu_P\) and \(\mu_Q\) be the population mean delivery times, in minutes, from depots \(P\) and \(Q\).
\[H_0: \mu_P = \mu_Q \qquad H_1: \mu_P > \mu_Q\]
[B1]
The sample means are \(\bar x = \dfrac{1962}{45} = 43.6\) and \(\bar y = \dfrac{2472}{60} = 41.2\). Unbiased estimates of the variances:
\[s_P^2 = \frac{1584}{44} = 36 \qquad s_Q^2 = \frac{2891}{59} = 49\]
[M1]
The samples are large, so use a normal test with the variances estimated separately:
\[z = \frac{\bar x - \bar y}{\sqrt{\dfrac{s_P^2}{45} + \dfrac{s_Q^2}{60}}}\]
[M1]
\[z = \frac{43.6 - 41.2}{\sqrt{0.8 + 0.8167}} = \frac{2.4}{1.2715} = 1.89\]
[A1]
This is a one-tailed test at 5%, so the critical value is \(1.645\). \(1.89 > 1.645\), so reject \(H_0\). [M1]
There is sufficient evidence, at the 5% level, that the mean delivery time from depot \(P\) is longer than from depot \(Q\). [A1]
(Equivalent: the \(p\)-value is \(P(Z > 1.89) = 0.0295 < 0.05\).)

(b) The samples are large, so by the central limit theorem the sample means are approximately normally distributed whatever the population distributions, and the sample variances are close to the population variances. [B1]
:::

:::try
Q: [10 marks] (#math.fm.crv) The continuous random variable \(X\) has probability density function
\[f(x) = \begin{cases} kx & 0 \le x \le 1,\\ \tfrac13 k(4 - x) & 1 < x \le 4,\\ 0 & \text{otherwise,}\end{cases}\]
where \(k\) is a constant.

(a) Show that \(k = \tfrac12\). [2]

(b) Show that, for \(1 \le x \le 4\), the cumulative distribution function of \(X\) is \(\mathrm{F}(x) = \dfrac{-x^2 + 8x - 4}{12}\). [3]

(c) Find the median of \(X\). [2]

The random variable \(Y\) is defined by \(Y = X^2\).

(d) Find the probability density function of \(Y\) for \(1 < y < 16\). [3]
A: (a) The total probability is 1:
\[\int_0^1 kx\,dx + \int_1^4 \tfrac13 k(4 - x)\,dx = 1\]
[M1]
\[\frac{k}{2} + \frac{k}{3}\left[4x - \frac{x^2}{2}\right]_1^4 = \frac{k}{2} + \frac{k}{3}\left(8 - \frac72\right) = \frac{k}{2} + \frac{3k}{2} = 2k\]
so \(2k = 1\) and \(k = \tfrac12\). [A1] (given result: the integrals must be shown)

(b) With \(k = \tfrac12\), \(f(x) = \tfrac12 x\) on \([0, 1]\) and \(f(x) = \tfrac16(4 - x)\) on \((1, 4]\). The probability up to \(x = 1\) is \(\mathrm{F}(1) = \int_0^1 \tfrac12 t\,dt = \tfrac14\). For \(1 \le x \le 4\):
\[\mathrm{F}(x) = \frac14 + \int_1^x \tfrac16(4 - t)\,dt\]
[M1]
\[\mathrm{F}(x) = \frac14 + \frac16\left[4t - \frac{t^2}{2}\right]_1^x = \frac14 + \frac16\left(4x - \frac{x^2}{2} - \frac72\right)\]
[A1]
\[\mathrm{F}(x) = \frac{3 + 8x - x^2 - 7}{12} = \frac{-x^2 + 8x - 4}{12}\]
[A1] (given result)
(Check: \(\mathrm{F}(1) = \tfrac{3}{12}\) and \(\mathrm{F}(4) = \tfrac{-16 + 32 - 4}{12} = 1\).)

(c) \(\mathrm{F}(1) = \tfrac14 < \tfrac12\), so the median \(m\) is in \((1, 4]\):
\[\frac{-m^2 + 8m - 4}{12} = \frac12 \quad\Rightarrow\quad m^2 - 8m + 10 = 0\]
[M1]
\[m = 4 \pm \sqrt6\]
Only \(4 - \sqrt6\) is in the interval \((1, 4]\), so \(m = 1.55\). [A1]

(d) For \(y\) between 1 and 16, \(\sqrt y\) is between 1 and 4. Since \(X \ge 0\),
\[\mathrm{G}(y) = \mathrm{P}(Y \le y) = \mathrm{P}\left(X \le \sqrt y\right) = \mathrm{F}\left(\sqrt y\right)\]
[M1]
\[\mathrm{G}(y) = \frac{-y + 8\sqrt y - 4}{12}\]
[A1]
Differentiate:
\[g(y) = \frac{1}{12}\left(-1 + \frac{4}{\sqrt y}\right) = \frac{4 - \sqrt y}{12\sqrt y}\]
[A1]
(Check at \(y = 4\): \(g(4) = \tfrac{2}{24} = \tfrac1{12}\), and \(f(2)/(2 \times 2) = \tfrac{1/3}{4} = \tfrac1{12}\).)
:::

:::try
Q: [8 marks] (#math.fm.chisq) A factory packs light bulbs in boxes of 4. The manager claims that the number of faulty bulbs in a box has the distribution \(\mathrm{B}(4, 0.3)\). For a random sample of 150 boxes, the numbers of faulty bulbs are summarised in the table, together with the expected frequencies for 0, 1 and 2 faulty bulbs on the manager's claim.

| Faulty bulbs | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Observed frequency | 24 | 58 | 46 | 19 | 3 |
| Expected frequency | 36.015 | 61.74 | 39.69 | | |

(a) Calculate the expected frequencies for 3 and 4 faulty bulbs. [2]

(b) Carry out a goodness-of-fit test, at the 5% significance level, of the manager's claim. [6]
A: (a) Expected frequencies for \(\mathrm{B}(4, 0.3)\) in 150 boxes:
\[E_3 = 150 \times \binom43 (0.3)^3(0.7) = 11.34\]
[M1]
\[E_4 = 150 \times (0.3)^4 = 1.215\]
[A1] (both values; \(150 - 36.015 - 61.74 - 39.69 = 12.555\) is a check on their sum)

(b) \(H_0\): \(\mathrm{B}(4, 0.3)\) is a suitable model for the number of faulty bulbs per box. \(H_1\): it is not a suitable model. [B1]
The expected frequency for 4 faulty bulbs is less than 5, so combine the last two classes (3 or more faulty bulbs): \(O = 22\), \(E = 12.555\). There are now 4 classes. [M1]

| Faulty bulbs | 0 | 1 | 2 | 3 or more |
|---|---|---|---|---|
| \(O\) | 24 | 58 | 46 | 22 |
| \(E\) | 36.015 | 61.74 | 39.69 | 12.555 |
| \(\dfrac{(O - E)^2}{E}\) | 4.008 | 0.227 | 1.003 | 7.105 |

\[X^2 = \sum\frac{(O - E)^2}{E} = 4.008 + 0.227 + 1.003 + 7.105\]
[M1]
\[X^2 = 12.3\]
[A1] (awrt 12.3)
No parameter was estimated, so \(\nu = 4 - 1 = 3\), and the 5% critical value is \(7.815\).
\(12.3 > 7.815\), so reject \(H_0\). [M1] (compare with the critical value for the right \(\nu\), and say reject or do not reject)
There is sufficient evidence, at the 5% level, that \(\mathrm{B}(4, 0.3)\) is not a suitable model for the number of faulty bulbs in a box. [A1] (correct conclusion in context from correct working; "no evidence" is not accepted)
(The largest contributions are from 0 faulty bulbs, observed far below expectation, and from 3 or more, observed far above: the faults are more common than 30% per bulb.)
:::

:::try
Q: [7 marks] (#math.fm.twosample) A food scientist measures the vitamin content, in suitable units, of the same fruit grown with two types of fertiliser, \(A\) and \(B\). Independent random samples give the following summaries.

| Fertiliser | Sample size | \(\sum x\) | \(\sum x^2\) |
|---|---|---|---|
| \(A\) | 8 | 196 | 4830 |
| \(B\) | 10 | 229 | 5291 |

It is assumed that the vitamin content is normally distributed with the same variance for both types of fertiliser.

(a) Calculate the pooled estimate of the common variance. [3]

(b) Find a 95% confidence interval for the difference between the population mean vitamin content with fertiliser \(A\) and with fertiliser \(B\). [3]

(c) State what the interval suggests about the effect of the fertiliser. [1]
A: (a) For each sample find \(\sum (x - \bar x)^2 = \sum x^2 - \dfrac{(\sum x)^2}{n}\):
\[S_A = 4830 - \frac{196^2}{8} = 28 \qquad S_B = 5291 - \frac{229^2}{10} = 46.9\]
[M1]
The pooled estimate (MF19) is
\[s_p^2 = \frac{S_A + S_B}{n_A + n_B - 2} = \frac{28 + 46.9}{16}\]
[M1]
\[s_p^2 = 4.68\]
[A1] (4.68125)

(b) The sample means are \(\bar x = 24.5\) and \(\bar y = 22.9\), so \(\bar x - \bar y = 1.6\). There are \(8 + 10 - 2 = 16\) degrees of freedom, and the 5% two-tailed (97.5% one-tailed) value of \(t\) is \(2.120\). [B1]
The interval is
\[1.6 \pm 2.120\sqrt{4.68125\left(\tfrac18 + \tfrac1{10}\right)} = 1.6 \pm 2.120 \times 1.0263\]
[M1]
\[(-0.576,\ 3.78)\]
[A1] (awrt \(-0.576\) and \(3.78\))

(c) The interval contains 0, so there is insufficient evidence, at the 5% level, of a difference between the mean vitamin content with the two fertilisers. [B1]
:::

:::try
Q: [9 marks] (#math.fm.wilcoxon) A teacher records the scores of nine students in a test before and after a revision course.

| Student | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Before | 52 | 61 | 48 | 70 | 55 | 66 | 43 | 58 | 64 |
| After | 61 | 75 | 45 | 81 | 61 | 61 | 56 | 65 | 79 |

(a) Assuming that the population of differences is symmetrical, use a Wilcoxon matched-pairs signed-rank test, at the 5% significance level, to test whether the revision course increases the median score. [5]

(b) Carry out a sign test, at the 5% significance level, on the same data. [3]

(c) Explain why the conclusions of the two tests are different. [1]
A: (a) Let \(m\) be the population median of the difference (after \(-\) before). \(H_0: m = 0\) and \(H_1: m > 0\). [B1]
The differences (after \(-\) before) and the ranks of their absolute values:

| Student | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| \(d\) | 9 | 14 | \(-3\) | 11 | 6 | \(-5\) | 13 | 7 | 15 |
| rank of \(\lvert d\rvert\) | 5 | 8 | 1 | 6 | 3 | 2 | 7 | 4 | 9 |

[M1] (differences and an attempt at signed ranks)
\(H_1\) predicts mostly positive differences, so the test statistic is the sum of the ranks of the negative differences: \(T = 1 + 2 = 3\) (and the positive ranks sum to \(45 - 3 = 42\)). [A1] The critical value for \(n = 9\), one-tailed at 5%, is \(8\) (MF19).
\(3 \le 8\), so reject \(H_0\). [M1] (their \(T\) compared with 8) There is sufficient evidence, at the 5% level, that the revision course increases the median score. [A1]

(b) Let \(S\) be the number of students whose score increased. Under \(H_0\), \(S \sim \mathrm{B}(9, \tfrac12)\), and \(S = 7\) was observed. For \(H_1: p > \tfrac12\) the \(p\)-value is
\[\mathrm{P}(S \ge 7) = \frac{36 + 9 + 1}{512} = 0.0898\]
[B1]
\(0.0898 > 0.05\), so do not reject \(H_0\). [M1] There is insufficient evidence, at the 5% level, that the course increases the median score: the opposite conclusion to part (a). [A1]

(c) The sign test uses only the number of students who improved (7 of 9). The Wilcoxon test also uses the sizes of the differences: the two students whose score fell did so by the two smallest amounts (3 and 5 marks), so the Wilcoxon test makes use of more information and is more powerful. [B1]
:::

:::try
Q: [9 marks] (#math.fm.pgf) The discrete random variable \(X\) has probability generating function
\[\mathrm{G}_X(t) = k(1 + t)(3 + t)\]
where \(k\) is a constant.

(a) Find the value of \(k\). [1]

(b) Use \(\mathrm{G}_X(t)\) to find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\). [4]

The random variable \(Y\) has a Poisson distribution with mean 2 and is independent of \(X\). The random variable \(W = X + Y\).

(c) Find the probability generating function of \(W\). [2]

(d) Use the probability generating function of \(W\) to find \(\mathrm{P}(W = 1)\). [2]
A: (a) \(\mathrm{G}_X(1) = 1\), so \(k \times 2 \times 4 = 1\) and \(k = \tfrac18\). [B1]

(b) Expand: \(\mathrm{G}_X(t) = \dfrac{t^2 + 4t + 3}{8}\). Then \(\mathrm{G}_X'(t) = \dfrac{2t + 4}{8}\) and \(\mathrm{G}_X''(t) = \dfrac{2}{8}\). [M1]
\[\mathrm{E}(X) = \mathrm{G}_X'(1) = \frac68 = \frac34\]
[A1]
\[\mathrm{Var}(X) = \mathrm{G}_X''(1) + \mathrm{G}_X'(1) - \left[\mathrm{G}_X'(1)\right]^2 = \frac14 + \frac34 - \frac{9}{16}\]
[M1]
\[\mathrm{Var}(X) = \frac{7}{16}\]
[A1] (0.4375)
(Check from the distribution: \(\mathrm{P}(X = 0, 1, 2) = \tfrac38, \tfrac12, \tfrac18\).)

(c) The probability generating function of \(\mathrm{Po}(2)\) is \(\mathrm{e}^{2(t - 1)}\). For independent variables the generating function of the sum is the product:
\[\mathrm{G}_W(t) = \frac{(1 + t)(3 + t)}{8}\,\mathrm{e}^{2(t - 1)}\]
[M1 A1]

(d) \(\mathrm{P}(W = 1)\) is the coefficient of \(t\), which is \(\mathrm{G}_W'(0)\). By the product rule,
\[\mathrm{G}_W'(t) = \left[\frac{2t + 4}{8} + \frac{2\left(t^2 + 4t + 3\right)}{8}\right]\mathrm{e}^{2(t - 1)}\]
[M1]
\[\mathrm{G}_W'(0) = \left(\frac48 + \frac68\right)\mathrm{e}^{-2} = \frac54\,\mathrm{e}^{-2} = 0.169\]
[A1] (alternative: \(\mathrm{P}(X = 0)\mathrm{P}(Y = 1) + \mathrm{P}(X = 1)\mathrm{P}(Y = 0) = \tfrac38 \times 2\mathrm{e}^{-2} + \tfrac12\,\mathrm{e}^{-2}\), M1 A1)
:::

:::warn Where marks are usually lost on a paper like this
- **A test with no hypotheses or no context in the conclusion** (Questions 1, 3 and 5). The first mark is for the hypotheses, in words or with defined symbols, and the last is for a conclusion that says "sufficient evidence" or "insufficient evidence" about the situation in the question. "Reject \(H_0\)" on its own earns nothing.
- **Using the wrong divisor or the wrong table** (Questions 1, 3 and 4). Variances are estimated by dividing by \(n - 1\), the degrees of freedom of a pooled \(t\) test are \(n_1 + n_2 - 2\), and a \(\chi^2\) test has \(\nu = \text{classes} - 1 - \text{parameters estimated}\) after the classes have been combined.
- **Not combining classes with an expected frequency below 5** (Question 3). Do it before you calculate \(\sum(O - E)^2/E\), and count the degrees of freedom from the combined table.
- **Losing the support of a density or the limits in a change of variable** (Question 2). Write the range of \(y\) beside the formula for \(\mathrm{G}(y)\), and say whether \(\mathrm{F}\) is the quadratic or the first piece.
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 7 | Two-sample test of means with large samples, unbiased variances | [Comparing two means](#math.fm.twosample) |
| 2 | 10 | Piecewise PDF, CDF, median, PDF of \(Y = X^2\) | [Continuous random variables](#math.fm.crv) |
| 3 | 8 | Expected frequencies, combining classes, goodness of fit | [Chi-squared goodness of fit](#math.fm.chisq) |
| 4 | 7 | Pooled variance and a \(t\) confidence interval | [Comparing two means](#math.fm.twosample) (and [The t-distribution: one-sample tests and intervals](#math.fm.inference)) |
| 5 | 9 | Wilcoxon matched-pairs test, sign test, comparing the two | [Wilcoxon tests](#math.fm.wilcoxon) (and [Non-parametric tests: the sign test](#math.fm.nonpar)) |
| 6 | 9 | PGF: mean, variance, sum of independent variables, a probability | [Probability generating functions](#math.fm.pgf) |
