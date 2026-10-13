@chapter math.mixed.stats2
@title Mixed practice: Statistics 2
@level ref
@paper CAIE 9709 Paper 6 · Edexcel IAL S2 · UK Statistics Year 2
@time 3–4 hours
@summary Twenty-nine short questions that mix every topic of Statistics 2 (the Poisson distribution, linear combinations, continuous random variables, sampling and estimation, hypothesis testing), ordered from ★ to ★★★. Each answer is a mark scheme, and each question names the chapter to revise.

:::why
In the exam you are never told which chapter a question comes from. A Paper 6 question could be a Poisson probability, a sum of normals, an integral of a density, a confidence interval or a hypothesis test, and recognising which is half of the marks. This page mixes everything on purpose, so that you have to decide every time.
:::

:::tip How to use this page
Do the questions in order, a few at a time, on paper, with a calculator and the normal tables. ★ questions are one idea (2 to 3 marks), ★★ questions are exam standard for a typical Paper 6 question, ★★★ questions need two or more ideas together. Mark yourself with the scheme, and under each answer the **Revise** link takes you to the chapter for that topic. Keep a list of the chapters that come up more than once: they are your weak spots.
:::

:::try Warm-up ★
Q: [2 marks] (#math.s2.poisson) ★ The random variable \(X \sim \mathrm{Po}(3)\). Find \(P(X = 2)\).
A: Use \(P(X = r) = e^{-\lambda}\dfrac{\lambda^r}{r!}\): [M1]
\[ P(X = 2) = e^{-3}\,\frac{3^2}{2!} = 0.224 \]
[A1]
Q: [2 marks] (#math.s2.poisson) ★ The random variable \(X \sim \mathrm{Po}(3)\). Find \(P(X \ge 2)\).
A: [M1]
\[ P(X \ge 2) = 1 - P(0) - P(1) = 1 - e^{-3}(1 + 3) \]
\(= 0.801\). [A1]
Q: [2 marks] (#math.s2.poisson) ★ Cars pass a point at random, at a mean rate of 6 per hour. Find the probability that no car passes in a 10-minute period.
A: In 10 minutes the mean is \(\lambda = 1\). [M1]
\(P(0) = e^{-1} = 0.368\). [A1]
Q: [2 marks] (#math.s2.linear) ★ The random variable \(X\) has mean 4 and variance 5. Find \(E(3X + 2)\) and \(\mathrm{Var}(3X + 2)\).
A: \(E(3X + 2) = 3 \times 4 + 2 = 14\). [B1]
\(\mathrm{Var}(3X + 2) = 3^2 \times 5 = 45\). [B1]
Q: [2 marks] (#math.s2.linear) ★ The independent random variables \(X\) and \(Y\) have means 10 and 7 and variances 4 and 9. Find \(E(X - Y)\) and \(\mathrm{Var}(X - Y)\).
A: \(E(X - Y) = 10 - 7 = 3\). [B1]
The variances add, even for a difference: \(\mathrm{Var}(X - Y) = 4 + 9 = 13\). [B1]
Q: [3 marks] (#math.s2.crv) ★ The random variable \(X\) has probability density function \(f(x) = kx\) for \(0 \le x \le 4\), and \(f(x) = 0\) otherwise. Find \(k\) and \(P(X < 2)\).
A: The total area is 1: [M1]
\[ \int_0^4 kx\,dx = 8k = 1 \]
So \(k = \tfrac18\). [A1]
\[ P(X < 2) = \int_0^2 \frac{x}{8}\,dx = \frac{4}{16} = \frac14 \]
[A1]
Q: [2 marks] (#math.s2.crv) ★ The random variable \(X\) has probability density function \(f(x) = 3x^2\) for \(0 \le x \le 1\), and 0 otherwise. Find \(E(X)\).
A: [M1]
\[ E(X) = \int_0^1 x \cdot 3x^2\,dx = \int_0^1 3x^3\,dx \]
\(= \dfrac34\). [A1]
Q: [3 marks] (#math.s2.sampling) ★ A random sample of 5 observations has \(\sum x = 45\) and \(\sum x^2 = 445\). Calculate unbiased estimates of the population mean and variance.
A: The estimate of the mean is \(\bar x = \dfrac{45}{5} = 9\). [B1]
The unbiased variance estimate divides by \(n - 1\): [M1]
\[ s^2 = \frac{1}{4}\Big(445 - \frac{45^2}{5}\Big) = \frac{40}{4} = 10 \]
[A1]
Q: [3 marks] (#math.s2.sampling) ★ The random variable \(X \sim N(80, 36)\). A random sample of 9 values of \(X\) is taken, with mean \(\bar X\). Find \(P(\bar X > 83)\).
A: The mean of a sample of size 9 has distribution \(\bar X \sim N\big(80, \tfrac{36}{9}\big) = N(80, 4)\). [B1]
\(z = \dfrac{83 - 80}{2} = 1.5\). [M1]
\(P(\bar X > 83) = 1 - \Phi(1.5) = 0.0668\). [A1]
Q: [3 marks] (#math.s2.hypothesis) ★ A coin is tossed 10 times and lands heads 9 times. Test, at the 5% significance level, whether the coin is biased towards heads.
A: Let \(p\) be the probability of heads. \(H_0: p = 0.5\); \(H_1: p > 0.5\). [B1]
Assuming \(H_0\), \(X \sim B(10, 0.5)\): [M1]
\[ P(X \ge 9) = \frac{10 + 1}{1024} = 0.0107 \]
[A1] This is less than 0.05, so reject \(H_0\): there is evidence that the coin is biased towards heads.
:::

:::try Exam standard ★★
Q: [3 marks] (#math.s2.poisson) ★★ Cars arrive at a toll booth at random, at a mean rate of 12 per hour. Find the probability that at least 3 cars arrive in a 15-minute period.
A: In 15 minutes the mean is \(\lambda = 3\), so \(X \sim \mathrm{Po}(3)\). [M1]
\[ P(X \ge 3) = 1 - e^{-3}\Big(1 + 3 + \frac{9}{2}\Big) \]
[M1] \(= 1 - 8.5e^{-3} = 0.577\). [A1]
Q: [3 marks] (#math.s2.poisson) ★★ The random variable \(X \sim B(80, 0.04)\). Use a suitable approximation to find \(P(X \le 2)\).
A: \(n = 80 > 50\) and \(np = 3.2 < 5\), so approximate by \(\mathrm{Po}(3.2)\). [B1]
\[ P(X \le 2) \approx e^{-3.2}\Big(1 + 3.2 + \frac{3.2^2}{2}\Big) \]
[M1] \(= 0.380\). [A1]
Q: [4 marks] (#math.s2.poisson) ★★ The random variable \(X \sim \mathrm{Po}(\lambda)\) and \(P(X = 0) = 0.2\).

(a) Find the value of \(\lambda\). [2]

(b) Find \(P(X \ge 2)\). [2]
A: (a) \(P(X = 0) = e^{-\lambda} = 0.2\). [M1]
\(\lambda = \ln 5 = 1.609\). [A1]

(b) [M1]
\[ P(X \ge 2) = 1 - e^{-\lambda}(1 + \lambda) = 1 - 0.2(1 + 1.609) \]
\(= 0.478\). [A1]
Q: [4 marks] (#math.s2.poisson) ★★ The random variable \(X \sim \mathrm{Po}(25)\). Use a suitable approximation to find \(P(X < 20)\).
A: Since \(\lambda = 25 > 15\), use \(N(25, 25)\). [B1]
With a continuity correction: [M1]
\[ P(X < 20) = P(X \le 19) \approx P(N < 19.5) \]
\[ z = \frac{19.5 - 25}{5} = -1.1 \]
[M1] \(P = \Phi(-1.1) = 0.136\). [A1]
Q: [4 marks] (#math.s2.linear) ★★ The independent random variables \(X \sim N(40, 9)\) and \(Y \sim N(25, 16)\). Find \(P(X > Y + 10)\).
A: Write \(D = X - Y\). Then \(E(D) = 40 - 25 = 15\). [M1]
\(\mathrm{Var}(D) = 9 + 16 = 25\) (variances add), so \(D \sim N(15, 25)\). [M1]
We need \(P(D > 10)\): \(z = \dfrac{10 - 15}{5} = -1\). [M1]
\(P = 1 - \Phi(-1) = 0.841\). [A1]
Q: [5 marks] (#math.s2.linear) ★★ The random variable \(X \sim N(12, 4)\). Four independent observations \(X_1, X_2, X_3, X_4\) of \(X\) are made, and \(S = X_1 + X_2 + X_3 + X_4\).

(a) Find \(P(S > 50)\). [3]

(b) The random variable \(T = 4X\). Find \(P(T > 50)\). [2]
A: (a) \(E(S) = 4 \times 12 = 48\). [B1]
The observations are independent, so \(\mathrm{Var}(S) = 4 \times 4 = 16\). [M1]
\(z = \dfrac{50 - 48}{4} = 0.5\), so \(P(S > 50) = 1 - \Phi(0.5) = 0.309\). [A1]

(b) \(E(T) = 48\) but \(\mathrm{Var}(T) = 4^2 \times 4 = 64\) (one observation multiplied by 4). [M1]
\(z = \dfrac{50 - 48}{8} = 0.25\), so \(P(T > 50) = 0.401\). [A1]
Q: [5 marks] (#math.s2.crv) ★★ The random variable \(X\) has probability density function \(f(x) = kx(2 - x)\) for \(0 \le x \le 2\), and \(f(x) = 0\) otherwise.

(a) Show that \(k = \dfrac34\). [2]

(b) Find \(P(X > 1.5)\). [2]

(c) Write down \(E(X)\), giving a reason. [1]
A: (a) [M1]
\[ \int_0^2 k(2x - x^2)\,dx = k\Big[x^2 - \frac{x^3}{3}\Big]_0^2 = k\Big(4 - \frac83\Big) = \frac{4k}{3} \]
This equals 1, so \(k = \dfrac34\). [A1]

(b) [M1]
\[ P(X > 1.5) = \frac34\Big[x^2 - \frac{x^3}{3}\Big]_{1.5}^{2} = \frac34\Big(\frac43 - 1.125\Big) \]
\(= \dfrac{5}{32} = 0.156\). [A1]

(c) \(E(X) = 1\), because the graph of \(f\) is symmetrical about \(x = 1\). [B1]
Q: [4 marks] (#math.s2.crv) ★★ The random variable \(X\) has probability density function \(f(x) = \dfrac{2}{x^3}\) for \(x \ge 1\), and \(f(x) = 0\) otherwise.

(a) Find \(E(X)\). [2]

(b) Find the median of \(X\). [2]
A: (a) [M1]
\[ E(X) = \int_1^\infty x\cdot\frac{2}{x^3}\,dx = \int_1^\infty 2x^{-2}\,dx \]
\(= \Big[-\dfrac{2}{x}\Big]_1^\infty = 2\). [A1]

(b) The median \(m\) satisfies [M1]
\[ \int_1^m 2x^{-3}\,dx = 1 - m^{-2} = \frac12 \]
\(m^2 = 2\), so \(m = \sqrt2 = 1.41\). [A1]
Q: [3 marks] (#math.s2.sampling) ★★ A random sample of 64 observations from a normal population with standard deviation 8 has mean 52.3. Find a 90% confidence interval for the population mean.
A: The critical value for 90% is \(z = 1.645\). [B1]
The standard error is \(\dfrac{8}{\sqrt{64}} = 1\), so the interval is \(52.3 \pm 1.645 \times 1\). [M1]
\((50.7,\ 53.9)\). [A1]
Q: [4 marks] (#math.s2.sampling) ★★ A population has mean 20 and variance 36, and is not normally distributed. A random sample of 50 observations is taken, with mean \(\bar X\). Find \(P(\bar X > 21.5)\).
A: The sample is large, so by the central limit theorem \(\bar X\) is approximately normal. [B1]
\(\bar X \approx N\big(20, \tfrac{36}{50}\big)\), with standard error \(\sqrt{0.72} = 0.8485\). [M1]
\(z = \dfrac{21.5 - 20}{0.8485} = 1.768\). [M1]
\(P(\bar X > 21.5) = 1 - \Phi(1.768) = 0.0385\). [A1]
Q: [4 marks] (#math.s2.hypothesis) ★★ The number of faults per hour in a machine is modelled by \(\mathrm{Po}(\lambda)\). A test is carried out of \(H_0: \lambda = 6\) against \(H_1: \lambda > 6\), at the 5% level, based on the number of faults in one hour. Find the critical region and the actual significance level of the test.
A: We need the smallest \(c\) with \(P(X \ge c) \le 0.05\) under \(\mathrm{Po}(6)\). [M1]
\(P(X \ge 10) = 0.0839 > 0.05\) but \(P(X \ge 11) = 0.0426 \le 0.05\). [A1]
So the critical region is \(X \ge 11\). [M1]
The actual significance level is \(0.0426\) (4.26%). [A1]
:::

:::try Stretch ★★★
Q: [8 marks] (#math.s2.hypothesis) ★★★ A drug company claims that 40% of patients recover from an illness within a week without treatment. A doctor believes the proportion is lower. Of 20 patients chosen at random, 4 recovered within a week.

(a) Test, at the 5% significance level, whether the doctor's belief is supported. [4]

(b) Find the critical region for the test, and the probability of a Type I error. [2]

(c) Given that the true proportion who recover is 0.2, find the probability of a Type II error. [2]
A: (a) \(H_0: p = 0.4\); \(H_1: p < 0.4\). [B1]
Under \(H_0\), \(X \sim B(20, 0.4)\): [M1]
\[ P(X \le 4) = 0.0510 \]
[A1] This is greater than 0.05, so do not reject \(H_0\): there is insufficient evidence at the 5% level that the proportion recovering is less than 40%. [A1]

(b) \(P(X \le 3) = 0.0160 \le 0.05\) but \(P(X \le 4) = 0.0510 > 0.05\), so the critical region is \(X \le 3\). [M1]
The probability of a Type I error is \(P(X \le 3 \mid p = 0.4) = 0.0160\). [A1]

(c) A Type II error is failing to reject \(H_0\) when \(p = 0.2\), that is \(X \ge 4\) with \(X \sim B(20, 0.2)\). [M1]
\[ P(X \ge 4) = 1 - P(X \le 3) = 1 - 0.4114 = 0.589 \]
[A1]
Q: [7 marks] (#math.s2.crv) ★★★ The random variable \(X\) has probability density function \(f(x) = kx(4 - x)\) for \(0 \le x \le 3\), and \(f(x) = 0\) otherwise.

(a) Show that \(k = \dfrac19\). [2]

(b) Find \(E(X)\). [2]

(c) Find \(\mathrm{Var}(X)\). [3]
A: (a) [M1]
\[ \int_0^3 k(4x - x^2)\,dx = k\Big[2x^2 - \frac{x^3}{3}\Big]_0^3 = k(18 - 9) = 9k \]
This equals 1, so \(k = \dfrac19\). [A1]

(b) [M1]
\[ E(X) = \frac19\int_0^3 (4x^2 - x^3)\,dx \]
\[ = \frac19\Big[\frac{4x^3}{3} - \frac{x^4}{4}\Big]_0^3 = \frac19(36 - 20.25) = \frac74 \]
[A1]

(c) [M1]
\[ E(X^2) = \frac19\int_0^3 (4x^3 - x^4)\,dx = \frac19\Big[x^4 - \frac{x^5}{5}\Big]_0^3 = \frac19(81 - 48.6) = 3.6 \]
\[ \mathrm{Var}(X) = E(X^2) - [E(X)]^2 = 3.6 - \Big(\frac74\Big)^2 \]
[M1] \(= 0.5375 = 0.538\). [A1]
Q: [8 marks] (#math.s2.sampling) ★★★ The lifetimes of a certain type of battery are normally distributed with standard deviation 12 hours. A random sample of 100 batteries has a mean lifetime of 410 hours.

(a) Find a 99% confidence interval for the population mean lifetime. [3]

(b) The manufacturer claims that the mean lifetime is 415 hours. Comment on this claim, using your interval. [2]

(c) Find the smallest sample size that would give a 99% confidence interval of width less than 4 hours. [3]
A: (a) The critical value for 99% is \(z = 2.576\). [B1]
The standard error is \(\dfrac{12}{\sqrt{100}} = 1.2\), so the interval is \(410 \pm 2.576 \times 1.2 = 410 \pm 3.09\). [M1]
\((407,\ 413)\) to 3 s.f. [A1]

(b) The value 415 lies outside the interval. [B1]
So the data do not support the claim: the mean lifetime is probably less than 415 hours. [B1]

(c) The width is \(2 \times 2.576 \times \dfrac{12}{\sqrt n} < 4\). [M1]
\[ \sqrt n > \frac{2 \times 2.576 \times 12}{4} = 15.46 \]
[A1] So \(n > 238.9\), and the smallest sample size is \(n = 239\). [A1]
Q: [7 marks] (#math.s2.poisson) ★★★ Customers arrive at a shop at random. Those paying by card arrive at a mean rate of 8 per hour, and those paying by cash at a mean rate of 9 per hour, independently.

(a) State the distribution of the total number of customers arriving in an hour. [1]

(b) Use a suitable approximation to find the probability that at least 22 customers arrive in a given hour. [4]

(c) Give a reason why a Poisson distribution might not be a good model for the number of customers arriving. [2]
A: (a) The sum of independent Poisson variables is Poisson: \(T \sim \mathrm{Po}(17)\). [B1]

(b) Since \(\lambda = 17 > 15\), approximate by \(N(17, 17)\). [B1]
With a continuity correction, \(P(T \ge 22) \approx P(N > 21.5)\). [M1]
\[ z = \frac{21.5 - 17}{\sqrt{17}} = 1.091 \]
[M1] \(P = 1 - \Phi(1.091) = 0.138\). [A1]

(c) Customers may arrive in groups, so arrivals are not independent of each other. [B1]
The rate may change through the day (busy and quiet times), so the mean rate is not constant. [B1]
Q: [8 marks] (#math.s2.hypothesis) ★★★ A random sample of 100 observations of a variable \(X\) gives \(\sum x = 5260\) and \(\sum x^2 = 285\,000\).

(a) Calculate the sample mean and an unbiased estimate of the population variance. [3]

(b) Test, at the 5% significance level, whether the population mean differs from 50. [5]
A: (a) The sample mean is \(\bar x = \dfrac{5260}{100} = 52.6\). [B1]
The unbiased variance estimate: [M1]
\[ s^2 = \frac{1}{99}\Big(285\,000 - \frac{5260^2}{100}\Big) = \frac{8324}{99} = 84.1 \]
[A1]

(b) \(H_0: \mu = 50\); \(H_1: \mu \ne 50\) (two-tailed). [B1]
The sample is large, so use \(\bar X \sim N\big(50, \tfrac{84.08}{100}\big)\), with standard error \(\sqrt{0.8408} = 0.9170\). [M1]
\[ z = \frac{52.6 - 50}{0.9170} = 2.84 \]
[A1] For a two-tailed test at 5%, the critical values are \(\pm 1.96\), and \(2.84 > 1.96\). [M1]
So reject \(H_0\): there is evidence at the 5% level that the population mean is different from 50. [A1]
Q: [8 marks] (#math.s2.linear) ★★★ The masses of apples are normally distributed with mean 150 g and standard deviation 20 g. The masses of plums are normally distributed with mean 60 g and standard deviation 10 g. A bag contains 4 apples and 6 plums, all chosen independently.

(a) Find the probability that the total mass of the contents of a bag exceeds 1000 g. [5]

(b) Find the probability that the mass of a randomly chosen apple is less than twice the mass of a randomly chosen plum. [3]
A: (a) The expected total is \(E(T) = 4 \times 150 + 6 \times 60 = 960\). [B1]
For independent items the variances of the individual masses add (not \(4^2\) times one apple): [M1]
\[ \mathrm{Var}(T) = 4 \times 20^2 + 6 \times 10^2 = 1600 + 600 = 2200 \]
So \(T \sim N(960, 2200)\). [A1]
\[ z = \frac{1000 - 960}{\sqrt{2200}} = 0.853 \]
[M1] \(P(T > 1000) = 1 - \Phi(0.853) = 0.197\). [A1]

(b) Let \(D = A - 2P\). \(E(D) = 150 - 120 = 30\), and \(\mathrm{Var}(D) = 400 + 2^2 \times 100 = 800\). [M1]
\(z = \dfrac{0 - 30}{\sqrt{800}} = -1.061\). [M1]
\(P(D < 0) = \Phi(-1.061) = 0.144\). [A1]
Q: [6 marks] (#math.s2.hypothesis) ★★★ The number of emails received by an office in an hour is modelled as \(\mathrm{Po}(\lambda)\), where \(\lambda = 30\) on a normal working day. On the day after a product launch, 38 emails are received in an hour. Test, at the 5% significance level, whether the mean number of emails has increased, using a suitable approximation.
A: \(H_0: \lambda = 30\); \(H_1: \lambda > 30\). [B1]
Under \(H_0\), since \(\lambda > 15\), \(X\) is approximately \(N(30, 30)\). [B1]
With a continuity correction, \(P(X \ge 38) \approx P(N > 37.5)\). [M1]
\[ z = \frac{37.5 - 30}{\sqrt{30}} = 1.369 \]
[M1] \(P = 1 - \Phi(1.369) = 0.0855\). [A1]
This is greater than 0.05, so do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the mean number of emails has increased. [A1]
Q: [8 marks] (#math.s2.hypothesis) ★★★ The random variable \(X\) has a Poisson distribution with mean \(\lambda\). A test of \(H_0: \lambda = 2\) against \(H_1: \lambda > 2\) is carried out, based on one observation of \(X\). The null hypothesis is rejected if \(X \ge 5\).

(a) Find the probability of a Type I error. [2]

(b) Given that in fact \(\lambda = 4\), find the probability of a Type II error. [2]

The rejection rule is changed, so that \(H_0\) is rejected if \(X \ge 6\).

(c) Find the new probability of a Type I error, and the new probability of a Type II error when \(\lambda = 4\). [3]

(d) Comment on how the two error probabilities have changed. [1]
A: (a) A Type I error is rejecting \(H_0\) when \(\lambda = 2\): [M1]
\[ P(X \ge 5 \mid \lambda = 2) = 1 - P(X \le 4) = 1 - 0.9473 = 0.0527 \]
[A1]

(b) A Type II error is not rejecting \(H_0\) when \(\lambda = 4\), so \(X \le 4\): [M1]
\[ P(X \le 4 \mid \lambda = 4) = 0.6288 \]
[A1] That is 0.629.

(c) New Type I: [M1]
\[ P(X \ge 6 \mid \lambda = 2) = 1 - 0.9834 = 0.0166 \]
[A1]
New Type II: \(P(X \le 5 \mid \lambda = 4) = 0.785\). [A1]

(d) The probability of a Type I error has fallen (from 0.0527 to 0.0166) but the probability of a Type II error has risen (from 0.629 to 0.785): making the test stricter reduces one error and increases the other. [B1]
:::
