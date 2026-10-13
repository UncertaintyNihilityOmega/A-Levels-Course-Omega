@chapter math.mock.p6a
@title Mock paper: Probability and Statistics 2 (A)
@level mock
@paper CAIE 9709 Paper 6 · Edexcel IAL S2 · UK Statistics Year 2
@time 1 h 15 min
@summary A complete original mock for Paper 6 (Probability and Statistics 2): 9 questions, 50 marks, 1 hour 15 minutes, rising in difficulty, with a full mark scheme. Sit it in one go, then mark yourself and see which chapters to revise.

:::why
Paper 6 mixes models (Poisson, normal, continuous distributions) with the language of inference: hypotheses, critical regions, errors, conclusions in context. This mock gives you 50 marks to practise both at 1.5 minutes per mark.
:::

:::exam Instructions
- Answer **all** questions. The total is **50 marks** and you have **1 hour 15 minutes**.
- You may use a scientific calculator and the MF19 formula booklet, which includes the normal distribution tables. Graphical calculators and calculators with symbolic algebra, differentiation or integration are **not** allowed.
- Show every step. A correct answer with no working may score no marks.
- Give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**, unless the question says otherwise.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [4 marks] (#math.s2.poisson) Telephone calls arrive at a helpdesk at random, at a mean rate of 4 per hour.

(a) Find the probability that exactly 3 calls arrive in a given hour. [2]

(b) Find the probability that at least 2 calls arrive in a given half-hour. [2]
A: (a) The number of calls in an hour is \(\mathrm{Po}(4)\): [M1]
\[ P(X = 3) = e^{-4}\,\frac{4^3}{3!} = 0.195 \]
[A1]

(b) In half an hour the mean is 2, so \(Y \sim \mathrm{Po}(2)\) and
\[ P(Y \ge 2) = 1 - P(0) - P(1) = 1 - e^{-2}(1 + 2) \]
[M1] \(= 0.594\). [A1]
:::

:::try
Q: [5 marks] (#math.s2.linear) The random variables \(X\) and \(Y\) are independent, with \(X \sim N(10, 4)\) and \(Y \sim N(5, 9)\). The random variable \(W\) is defined by \(W = 3X - 2Y\). Find \(P(W > 25)\).
A: A linear combination of independent normal variables is normal, with mean \(E(W) = 3(10) - 2(5) = 20\). [B1]
The variance is \(3^2 \times 4 + (-2)^2 \times 9\), because variances add and the coefficients are squared: [M1]
\[ \mathrm{Var}(W) = 36 + 36 = 72 \]
So \(W \sim N(20, 72)\). [A1]
\[ z = \frac{25 - 20}{\sqrt{72}} = 0.589 \]
[M1] \(P(W > 25) = 1 - \Phi(0.589) = 0.278\). [A1]
:::

:::try
Q: [3 marks] (#math.s2.linear) Emails arrive in an office independently at random, at a mean rate of 3.2 per hour for work emails and 1.8 per hour for personal emails. Find the probability that exactly 2 emails in total arrive in a 30-minute period.
A: The sum of two independent Poisson variables is Poisson, so the total in an hour has mean \(3.2 + 1.8 = 5\). [B1]
In 30 minutes the mean is \(\lambda = 2.5\): [M1]
\[ P(N = 2) = e^{-2.5}\,\frac{2.5^2}{2!} = 0.257 \]
[A1]
:::

:::try
Q: [4 marks] (#math.s2.poisson) The random variable \(X\) has the distribution \(\mathrm{Po}(20)\). Use a suitable approximation to find \(P(X > 25)\).
A: Since \(\lambda = 20 > 15\), approximate \(X\) by \(N(20, 20)\) (the mean and variance are both 20). [B1]
With a continuity correction: [M1]
\[ P(X > 25) = P(X \ge 26) \approx P(N > 25.5) \]
\[ z = \frac{25.5 - 20}{\sqrt{20}} = 1.23 \]
[M1] \(P = 1 - \Phi(1.23) = 0.109\). [A1]
:::

:::try
Q: [7 marks] (#math.s2.crv) The continuous random variable \(X\) has probability density function
\[ f(x) = \begin{cases} \dfrac{k}{x^5} & x \ge 1 \\[4pt] 0 & \text{otherwise,} \end{cases} \]
where \(k\) is a constant.
(a) Show that \(k = 4\). [2]
(b) Find \(E(X)\). [2]
(c) Find the median of \(X\). [3]
A: (a) The total area under the curve is 1:
\[ \int_1^\infty kx^{-5}\,dx = \Big[-\frac{k}{4x^4}\Big]_1^\infty = 0 + \frac k4 \]
[M1] So \(\dfrac k4 = 1\) and \(k = 4\). [A1]
(b) [M1]
\[ E(X) = \int_1^\infty x \cdot 4x^{-5}\,dx = \int_1^\infty 4x^{-4}\,dx \]
\[ = \Big[-\frac{4}{3x^3}\Big]_1^\infty = \frac43 \]
[A1]
(c) The median \(m\) satisfies [M1]
\[ \int_1^m 4x^{-5}\,dx = \tfrac12 \]
\[ \Big[-x^{-4}\Big]_1^m = 1 - m^{-4} = \tfrac12 \]
[M1] So \(m^4 = 2\) and \(m = 2^{1/4} = 1.19\). [A1]
:::

:::try
Q: [6 marks] (#math.s2.sampling) The lengths of a certain type of bolt are normally distributed with standard deviation 9 mm. A random sample of 36 bolts has a mean length of 83.4 mm.
(a) Find a 95% confidence interval for the population mean length. [3]
(b) A larger sample is to be taken so that a 95% confidence interval for the mean has a width of less than 4 mm. Find the smallest sample size needed. [3]
A: (a) The critical value for 95% is \(z = 1.96\). [B1]
The interval is \(83.4 \pm 1.96 \times \dfrac{9}{\sqrt{36}} = 83.4 \pm 2.94\). [M1]
So the 95% confidence interval is \((80.5,\ 86.3)\). [A1]
(b) The width is \(2 \times 1.96 \times \dfrac{9}{\sqrt n} < 4\). [M1]
\[ \sqrt n > \frac{2 \times 1.96 \times 9}{4} = 8.82 \]
[A1] So \(n > 77.8\), and the smallest sample size is \(n = 78\). [A1]
:::

:::try
Q: [6 marks] (#math.s2.sampling) (a) A random sample of 12 observations of a variable gives \(\sum x = 300\) and \(\sum x^2 = 8000\). Calculate unbiased estimates of the population mean and variance. [3]
(b) In a random sample of 200 voters, 62 say they intend to vote for a particular candidate. Calculate an approximate 95% confidence interval for the proportion of all voters who intend to vote for that candidate. [3]
A: (a) The estimate of the mean is \(\bar x = \dfrac{300}{12} = 25\). [B1]
The unbiased estimate of the variance divides by \(n - 1\): [M1]
\[ s^2 = \frac{1}{11}\Big(8000 - \frac{300^2}{12}\Big) = \frac{500}{11} = 45.5 \]
[A1]
(b) The sample proportion is \(\hat p = \dfrac{62}{200} = 0.31\), with standard error \(\sqrt{\dfrac{0.31 \times 0.69}{200}} = 0.0327\). [M1]
The interval is \(0.31 \pm 1.96 \times 0.0327\) [M1]
\[ (0.246,\ 0.374) \]
[A1]
:::

:::try
Q: [5 marks] (#math.s2.hypothesis) The number of faults in a length of cloth made by an old process has a Poisson distribution with mean 0.8 per metre. A new process is introduced, and it is claimed that it produces fewer faults. A 5 metre length of cloth made by the new process is found to have 1 fault. Test the claim at the 5% significance level.
A: Let \(\lambda\) be the mean number of faults in a 5 metre length. For the old process \(\lambda = 4\).
\(H_0: \lambda = 4\); \(H_1: \lambda < 4\) (one-tailed). [B1]
Assuming \(H_0\), \(X \sim \mathrm{Po}(4)\). [M1]
\[ P(X \le 1) = e^{-4}(1 + 4) = 0.0916 \]
[A1] Since \(0.0916 > 0.05\), do not reject \(H_0\). [M1]
There is insufficient evidence, at the 5% level, that the new process produces fewer faults. [A1]
:::

:::try
Q: [10 marks] (#math.s2.hypothesis) A machine fills bottles. The volume of liquid in a bottle is normally distributed with standard deviation 4 ml. The machine is set so that the mean volume is 500 ml. After servicing, it is suspected that the mean volume is now lower. A random sample of 25 bottles has a mean volume of 498.9 ml.
(a) Test, at the 5% significance level, whether the mean volume has decreased. [5]
(b) Find the critical region for the sample mean \(\bar X\) in this test. [2]
(c) Given that the true mean volume is in fact 498 ml, find the probability of a Type II error. [3]
A: (a) \(H_0: \mu = 500\); \(H_1: \mu < 500\) (one-tailed). [B1]
Under \(H_0\), \(\bar X \sim N\big(500, \tfrac{4^2}{25}\big)\), so the standard error is 0.8. [M1]
\[ z = \frac{498.9 - 500}{0.8} = -1.375 \]
[A1] The critical value for a 5% one-tailed test is \(-1.645\), and \(-1.375 > -1.645\), so do not reject \(H_0\). [M1]
There is insufficient evidence, at the 5% level, that the mean volume has decreased. [A1]
(b) The critical value of \(\bar X\) is \(500 - 1.645 \times 0.8 = 498.68\). [M1]
So the critical region is \(\bar X < 498.68\) (accept 498.7). [A1]
(c) A Type II error is not rejecting \(H_0\) when the true mean is 498, that is \(\bar X > 498.68\) with \(\bar X \sim N(498, 0.8^2)\). [M1]
\[ z = \frac{498.68 - 498}{0.8} = 0.855 \]
[M1]
\[ P(\text{Type II error}) = 1 - \Phi(0.855) = 0.196 \]
[A1] (Accept 0.191 to 0.198, depending on the critical value used: 498.7 gives 0.191.)
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 4 | Poisson probabilities, changing the interval | [The Poisson distribution](#math.s2.poisson) |
| 2 | 5 | Linear combination of independent normals | [Linear combinations of random variables](#math.s2.linear) |
| 3 | 3 | Sum of independent Poisson variables | [Linear combinations of random variables](#math.s2.linear) |
| 4 | 4 | Normal approximation to a Poisson | [The Poisson distribution](#math.s2.poisson) |
| 5 | 7 | Probability density function, mean, median | [Continuous random variables](#math.s2.crv) |
| 6 | 6 | Confidence interval for a mean, sample size | [Sampling and estimation](#math.s2.sampling) |
| 7 | 6 | Unbiased estimates, confidence interval for a proportion | [Sampling and estimation](#math.s2.sampling) |
| 8 | 5 | Hypothesis test for a Poisson mean | [Hypothesis testing](#math.s2.hypothesis) |
| 9 | 10 | Test for a mean, critical region, Type II error | [Hypothesis testing](#math.s2.hypothesis) |
