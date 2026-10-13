@chapter math.mock.p5a
@title Mock paper: Probability and Statistics 1 (A)
@level mock
@paper CAIE 9709 Paper 5 · Edexcel IAL S1 · UK Statistics Year 1
@time 1 h 15 min
@summary A complete original mock for Paper 5 (Probability and Statistics 1): 9 questions, 50 marks, 1 hour 15 minutes, rising in difficulty, with a full mark scheme. Sit it in one go, then mark yourself and see which chapters to revise.

:::why
Paper 5 rewards candidates who turn words into the right model quickly: counting, a tree, a table, a binomial or a normal. This mock gives you 50 marks to practise choosing the model against the clock, at 1.5 minutes per mark.
:::

:::exam Instructions
- Answer **all** questions. The total is **50 marks** and you have **1 hour 15 minutes**.
- You may use a scientific calculator and the MF19 formula booklet, which includes the normal distribution tables. Graphical calculators and calculators with symbolic algebra, differentiation or integration are **not** allowed.
- Show every step. A correct answer with no working may score no marks.
- Give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**, unless the question says otherwise.
- Press **Start the clock**, answer on paper, and press **Finish and mark** only when you are done. The mark scheme appears then: give yourself the marks, one question at a time.
:::

:::try
Q: [3 marks] (#math.s1.data) A set of 12 values \(x\) has \(\sum(x - 20) = 15\) and \(\sum(x - 20)^2 = 240\). Find the mean and the standard deviation of the 12 values.
A: The mean is \(20 + \dfrac{15}{12} = 21.25\). [B1]
The variance of the coded values \(x - 20\) is the variance of \(x\): [M1]
\[ \frac{240}{12} - \Big(\frac{15}{12}\Big)^2 = 20 - 1.5625 = 18.4375 \]
So the standard deviation is \(\sqrt{18.4375} = 4.29\). [A1]
:::

:::try
Q: [4 marks] (#math.s1.perms) The letters of the word STATISTICS are arranged in a line.

(a) Find the number of different arrangements. [2]

(b) Find the number of different arrangements in which the two letters I are next to each other. [2]
A: (a) There are 10 letters, with S three times, T three times and I twice: [M1]
\[ \frac{10!}{3!\,3!\,2!} = 50\,400 \]
[A1]

(b) Treat the two letters I as a single object. There are then 9 objects, with S three times and T three times: [M1]
\[ \frac{9!}{3!\,3!} = 10\,080 \]
[A1]
:::

:::try
Q: [4 marks] (#math.s1.perms) A committee of 4 people is to be chosen from 6 men and 5 women. The committee must include at least 2 women. In how many ways can the committee be chosen?
A: Consider the cases by the number of women, 2, 3 or 4: [M1]
- 2 women and 2 men: \(\binom52\binom62 = 10 \times 15 = 150\). [B1]
- 3 women and 1 man: \(\binom53\binom61 = 10 \times 6 = 60\), and 4 women: \(\binom54 = 5\). [B1]

The total is \(150 + 60 + 5 = 215\). [A1]
(Check by complement:
\[ \binom{11}{4} - \binom64 - 5\binom63 = 330 - 15 - 100 = 215 \]
)
:::

:::try
Q: [5 marks] (#math.s1.prob) On any day it rains with probability 0.3. If it rains, the bus is late with probability 0.2. If it does not rain, the bus is late with probability 0.05.

(a) Find the probability that the bus is late on a randomly chosen day. [3]

(b) Given that the bus is late, find the probability that it rained. [2]
A: (a) Draw a tree with rain / no rain and late / not late: P(rain) = 0.3 and P(no rain) = 0.7. [B1]
\[ P(\text{late}) = 0.3 \times 0.2 + 0.7 \times 0.05 = 0.06 + 0.035 \]
[M1] So \(P(\text{late}) = 0.095\). [A1]

(b) [M1]
\[ P(\text{rain} \mid \text{late}) = \frac{P(\text{rain and late})}{P(\text{late})} = \frac{0.06}{0.095} \]
\(= \dfrac{12}{19} = 0.632\). [A1]
:::

:::try
Q: [7 marks] (#math.s1.data) The times, in minutes, taken by 90 people to complete a puzzle are summarised below.

Time \(t\): \(0 \le t < 10\): 6 people; \(10 \le t < 20\): 14 people; \(20 \le t < 30\): 30 people; \(30 \le t < 40\): 24 people; \(40 \le t < 60\): 16 people.

(a) Use linear interpolation to estimate the median and the interquartile range of the times. [4]

(b) Calculate estimates of the mean and the standard deviation of the times. [3]
A: (a) The cumulative frequencies at the upper boundaries are 6, 20, 50, 74, 90. The median is the 45th value, which lies in \(20 \le t < 30\): [M1]
\[ \text{median} \approx 20 + \frac{45 - 20}{30} \times 10 = 28.3 \]
[A1] The lower quartile is the 22.5th value: \(20 + \dfrac{2.5}{30} \times 10 = 20.83\). The upper quartile is the 67.5th value, in \(30 \le t < 40\): \(30 + \dfrac{17.5}{24} \times 10 = 37.29\). [M1]
\[ \text{IQR} \approx 37.29 - 20.83 = 16.5 \]
[A1]

(b) Use the mid-points 5, 15, 25, 35, 50:
\[ \sum fx = 30 + 210 + 750 + 840 + 800 = 2630 \]
So the mean is \(\dfrac{2630}{90} = 29.2\). [B1]
\[ \sum fx^2 = 150 + 3150 + 18750 + 29400 + 40000 = 91\,450 \]
[M1]
\[ \sigma = \sqrt{\frac{91\,450}{90} - 29.22^2} = 12.7 \]
[A1]
:::

:::try
Q: [5 marks] (#math.s1.drv) A discrete random variable \(X\) takes the values 1, 2, 3 and 4, with \(P(X = 1) = 0.1\), \(P(X = 2) = 0.3\), \(P(X = 3) = k\) and \(P(X = 4) = 3k\).

(a) Show that \(k = 0.15\). [2]

(b) Find \(E(X)\). [1]

(c) Find \(\mathrm{Var}(X)\). [2]
A: (a) The probabilities add up to 1: \(0.1 + 0.3 + k + 3k = 1\). [M1]
\(4k = 0.6\), so \(k = 0.15\). [A1]

(b) The distribution is 0.1, 0.3, 0.15, 0.45 for \(x = 1, 2, 3, 4\), so
\[ E(X) = 0.1 + 0.6 + 0.45 + 1.8 = 2.95 \]
[B1]

(c) \(E(X^2) = 0.1 + 1.2 + 1.35 + 7.2 = 9.85\). [M1]
\[ \mathrm{Var}(X) = 9.85 - 2.95^2 = 1.1475 = 1.15 \]
[A1]
:::

:::try
Q: [5 marks] (#math.s1.drv) A darts player hits the bull with each throw with probability 0.3, independently of all other throws.

(a) Find the probability that the first bull is hit on the 4th throw. [2]

(b) Find the expected number of throws up to and including the first bull. [1]

(c) Find the probability that more than 5 throws are needed to hit the first bull. [2]
A: (a) The first three throws miss and the fourth hits (a geometric distribution with \(p = 0.3\)): [M1]
\[ 0.7^3 \times 0.3 = 0.103 \]
[A1]

(b) \(E = \dfrac1p = \dfrac{1}{0.3} = 3.33\). [B1]

(c) More than 5 throws are needed exactly when the first five all miss: [M1]
\[ 0.7^5 = 0.168 \]
[A1]
:::

:::try
Q: [7 marks] (#math.s1.prob) A bag contains 4 red counters and 5 white counters. Three counters are taken from the bag at random, without replacement. The random variable \(X\) is the number of red counters taken.

(a) Show that \(P(X = 2) = \dfrac{5}{14}\). [2]

(b) Draw up the probability distribution table for \(X\). [2]

(c) Find \(E(X)\) and \(\mathrm{Var}(X)\). [3]
A: (a) Choose 2 of the 4 red and 1 of the 5 white, out of the \(\binom93 = 84\) equally likely selections: [M1]
\[ P(X = 2) = \frac{\binom42\binom51}{\binom93} = \frac{6 \times 5}{84} = \frac{5}{14} \]
[A1]

(b) Similarly \(P(X = 0) = \dfrac{\binom53}{84} = \dfrac{10}{84} = \dfrac{5}{42}\). [B1]
\(P(X = 1) = \dfrac{4 \times 10}{84} = \dfrac{10}{21}\) and \(P(X = 3) = \dfrac{4}{84} = \dfrac{1}{21}\). [B1]
(The four probabilities \(\tfrac{5}{42}, \tfrac{20}{42}, \tfrac{15}{42}, \tfrac{2}{42}\) add up to 1.)

(c) \(E(X) = \dfrac{10}{21} + \dfrac{10}{14} + \dfrac{3}{21} = \dfrac43\). [B1]
\(E(X^2) = \dfrac{10}{21} + \dfrac{4 \times 5}{14} + \dfrac{9}{21} = \dfrac73\). [M1]
\[ \mathrm{Var}(X) = \frac73 - \Big(\frac43\Big)^2 = \frac59 \]
[A1]
:::

:::try
Q: [10 marks] (#math.s1.normal) The masses of apples from an orchard are normally distributed with mean 160 g and standard deviation 20 g.

(a) Find the probability that a randomly chosen apple has a mass greater than 190 g. [2]

(b) The heaviest 15% of apples are sold as Grade A. Find the least mass of a Grade A apple. [3]

A box contains 10 randomly chosen apples.

(c) Find the probability that at least 2 of them have a mass greater than 190 g. [2]

A crate contains 200 randomly chosen apples.

(d) Use a suitable approximation to find the probability that more than 20 of the apples in the crate have a mass greater than 190 g. [3]
A: (a) Standardise: \(z = \dfrac{190 - 160}{20} = 1.5\). [M1]
\[ P(X > 190) = 1 - \Phi(1.5) = 1 - 0.9332 = 0.0668 \]
[A1]

(b) The upper 15% means \(\Phi(z) = 0.85\), so \(z = 1.036\) (tables give 1.04). [B1]
\[ \frac{m - 160}{20} = 1.036 \]
[M1] So \(m = 160 + 20.73 = 181\) g. [A1]

(c) Let \(Y\) be the number heavier than 190 g, so \(Y \sim B(10, 0.0668)\). [M1]
\[ P(Y \ge 2) = 1 - 0.9332^{10} - 10(0.0668)(0.9332)^9 = 0.141 \]
[A1]

(d) \(W \sim B(200, 0.0668)\) has \(np = 13.36 > 5\) and \(nq > 5\), so use \(N(13.36, 12.47)\), where the variance is \(npq = 200 \times 0.0668 \times 0.9332\). [M1]
With a continuity correction: [M1]
\[ P(W > 20) = P(W \ge 21) \approx P(N > 20.5) \]
\[ z = \frac{20.5 - 13.36}{\sqrt{12.47}} = 2.02 \quad\Rightarrow\quad P = 1 - \Phi(2.02) = 0.0216 \]
[A1] (Accept 0.0217 using the table value for \(z = 2.02\).)
:::

## Question → chapter to revise

| Question | Marks | Topic | Chapter to revise |
|---|---|---|---|
| 1 | 3 | Coded mean and standard deviation | [Representing and summarising data](#math.s1.data) |
| 2 | 4 | Arrangements with repeated letters | [Permutations and combinations](#math.s1.perms) |
| 3 | 4 | Selections with a condition | [Permutations and combinations](#math.s1.perms) |
| 4 | 5 | Tree diagram, conditional probability | [Probability](#math.s1.prob) |
| 5 | 7 | Grouped data: median, IQR, mean, SD | [Representing and summarising data](#math.s1.data) |
| 6 | 5 | Probability distribution table, \(E(X)\), \(\mathrm{Var}(X)\) | [Discrete random variables: binomial and geometric](#math.s1.drv) |
| 7 | 5 | Geometric distribution | [Discrete random variables: binomial and geometric](#math.s1.drv) |
| 8 | 7 | Counting probability, distribution of a count | [Probability](#math.s1.prob) and [Discrete random variables: binomial and geometric](#math.s1.drv) |
| 9 | 10 | Normal, binomial and the normal approximation | [The normal distribution](#math.s1.normal) |
