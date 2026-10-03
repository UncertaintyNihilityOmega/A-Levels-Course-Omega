@chapter math.s1.drv
@title Discrete random variables: binomial and geometric
@level a2
@paper CAIE P5 (check your specification for other boards)
@time 9–11 hours
@summary Discrete random variables and their probability distribution tables, the expectation \(E(X)\) and variance \(\mathrm{Var}(X)\); then the two standard models: the binomial distribution \(B(n, p)\) for a count of successes in \(n\) trials, and the geometric distribution \(\mathrm{Geo}(p)\) for the number of trials until the first success. Includes how to choose the right model.

:::why
Many questions are about a count: how many faulty items in a box, how many heads in ten tosses, how many attempts until a first success. A random variable turns each outcome into a number, and a distribution tells you how likely each number is. Two models cover a huge range of counting situations, and recognising which one applies is the main skill.
:::

**Before you start**, you need probability from [Probability](#math.s1.prob), combinations \(\binom{n}{r}\) from [Permutations and combinations](#math.s1.perms), and powers and logarithms from [Exponentials and logarithms](#math.p3.logs).

## Random variables and distribution tables

:::def Discrete random variable
A **random variable** \(X\) takes a numerical value that depends on the outcome of a random experiment. It is **discrete** if it takes separate values, such as 0, 1, 2, 3. Its **probability distribution** lists each value \(x\) with its probability \(P(X = x)\) (a table, or a formula). The probabilities always sum to 1:
\[\sum P(X = x) = 1\]
:::

:::eg The discrete random variable \(X\) has \(P(X = x) = kx\) for \(x = 1, 2, 3, 4\). Find \(k\) and draw up the table.
\(k(1 + 2 + 3 + 4) = 1\), so \(10k = 1\) and \(k = 0.1\).

| \(x\) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| \(P(X = x)\) | 0.1 | 0.2 | 0.3 | 0.4 |
:::

## Expectation and variance

:::key Expectation and variance
\[E(X) = \sum x\,P(X = x) \qquad E(X^2) = \sum x^2\,P(X = x)\]
\[\mathrm{Var}(X) = E(X^2) - \left[E(X)\right]^2\]
\(E(X)\) is the long-run average (the mean of the distribution). The standard deviation is \(\sqrt{\mathrm{Var}(X)}\).
:::

:::eg For the distribution \(P(X = x) = 0.1x\) with \(x = 1, 2, 3, 4\), find \(E(X)\) and \(\mathrm{Var}(X)\).
\(E(X) = 1(0.1) + 2(0.2) + 3(0.3) + 4(0.4) = 0.1 + 0.4 + 0.9 + 1.6 = 3\).
\(E(X^2) = 1(0.1) + 4(0.2) + 9(0.3) + 16(0.4) = 0.1 + 0.8 + 2.7 + 6.4 = 10\).
\(\mathrm{Var}(X) = 10 - 3^2 = 1\), so the standard deviation is 1.
:::

:::eg The random variable \(X\) has the table below, with \(E(X) = 1.6\). Find \(a\) and \(b\), then \(\mathrm{Var}(X)\).

| \(x\) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| \(P(X = x)\) | 0.2 | \(a\) | 0.3 | \(b\) |

The probabilities sum to 1: \(0.2 + a + 0.3 + b = 1\), so \(a + b = 0.5\).
From the mean: \(0(0.2) + 1(a) + 2(0.3) + 3b = 1.6\), so \(a + 3b = 1\).
Subtract: \(2b = 0.5\), so \(b = 0.25\) and \(a = 0.25\).
\(E(X^2) = 0 + 0.25 + 4(0.3) + 9(0.25) = 0.25 + 1.2 + 2.25 = 3.7\), so \(\mathrm{Var}(X) = 3.7 - 1.6^2 = 1.14\).
:::

:::eg (Real context) A game costs £2 to play. A fair die is rolled: a 6 pays £5, a 4 or 5 pays £1, and anything else pays nothing. Let \(X\) be the player's net gain in pounds. Find \(E(X)\) and the standard deviation.
The net gain is the prize minus the £2 stake. A 6 gives \(5 - 2 = 3\); a 4 or 5 gives \(1 - 2 = -1\); otherwise \(-2\).

| \(x\) | \(-2\) | \(-1\) | \(3\) |
|---|---|---|---|
| \(P(X = x)\) | \(\frac36\) | \(\frac26\) | \(\frac16\) |

\(E(X) = -2\cdot\frac12 - 1\cdot\frac13 + 3\cdot\frac16 = -1 - 0.3333 + 0.5 = -0.833\). The player loses about 83p per game on average.
\(E(X^2) = 4\cdot\frac12 + 1\cdot\frac13 + 9\cdot\frac16 = 3.833\), so \(\mathrm{Var}(X) = 3.833 - 0.833^2 = 3.139\) and the standard deviation is \(1.77\).
:::

## The binomial distribution

:::def Binomial distribution
\(X \sim B(n, p)\) when \(X\) counts the **number of successes** in \(n\) trials and:
1. there is a **fixed number** \(n\) of trials;
2. each trial has just **two outcomes**, success or failure;
3. the trials are **independent**;
4. the probability of success \(p\) is **the same** for every trial.
:::

:::key Binomial formulae
For \(X \sim B(n, p)\), with \(q = 1 - p\):
\[P(X = r) = \binom{n}{r}p^r q^{n-r} \qquad E(X) = np \qquad \mathrm{Var}(X) = npq\]
The probability formula and the mean and variance are on MF19.
:::

The reasoning behind the formula: one particular sequence with \(r\) successes and \(n - r\) failures has probability \(p^r q^{n-r}\), and there are \(\binom nr\) different sequences. For "at most", "at least" and "more than", add the individual probabilities, or use the complement, remembering that \(P(X \ge r) = 1 - P(X \le r - 1)\).

:::eg \(X \sim B(10, 0.3)\). Find (a) \(P(X = 3)\), (b) \(P(X \le 2)\), (c) \(P(X \ge 4)\), (d) the mean and variance.
(a) \(P(X = 3) = \dbinom{10}{3}(0.3)^3(0.7)^7 = 120\times 0.027\times 0.0823543 = 0.267\).
(b) \(P(X \le 2) = P(0) + P(1) + P(2) = 0.7^{10} + 10(0.3)(0.7)^9 + 45(0.3)^2(0.7)^8\)
\(\phantom{(b)\ P(X \le 2)} = 0.0282 + 0.1211 + 0.2335 = 0.383\).
(c) \(P(X \ge 4) = 1 - P(X \le 3) = 1 - (0.3828 + 0.2668) = 0.350\).
(d) \(E(X) = 10\times 0.3 = 3\) and \(\mathrm{Var}(X) = 10\times 0.3\times 0.7 = 2.1\).
:::

The widget draws the distribution, highlights a range, and gives \(P(a \le X \le b)\), the mean and the variance. Change \(n\) and \(p\) to see the shape: it is skewed for small or large \(p\), and symmetric at \(p = 0.5\).

:::html
<div class="widget" data-w="discrete" data-dist="binomial" data-n="10" data-p="0.3" data-range="0,2"></div>
:::

:::eg (Real context) A factory finds that 4% of its light bulbs are defective, independently of each other. A box holds 20 bulbs. Find the probability that a box has no defective bulbs, and that it has at most 2.
Let \(X\) be the number of defective bulbs in a box. \(X \sim B(20, 0.04)\).
\(P(X = 0) = 0.96^{20} = 0.442\).
\(P(X \le 2) = 0.96^{20} + 20(0.04)(0.96)^{19} + 190(0.04)^2(0.96)^{18} = 0.4420 + 0.3683 + 0.1458 = 0.956\).
:::

:::eg (Exam style) The probability that a bulb is defective is 0.04, independently. Find the smallest number \(n\) of bulbs in a sample so that the probability of at least one defective bulb is greater than 0.9. [4 marks]
\(P(\text{at least one defective}) = 1 - 0.96^n > 0.9\). [M1]
So \(0.96^n < 0.1\). [A1] Take logarithms: \(n\ln 0.96 < \ln 0.1\). Since \(\ln 0.96\) is negative, divide and reverse the inequality: \(n > \dfrac{\ln 0.1}{\ln 0.96} = 56.4\). [M1]
The smallest whole number is \(n = 57\). [A1]
Check: \(0.96^{56} = 0.1017 > 0.1\) (not enough) and \(0.96^{57} = 0.0976 < 0.1\) ✓.
:::

## The geometric distribution

:::def Geometric distribution
\(X \sim \mathrm{Geo}(p)\) when \(X\) is the **number of the trial on which the first success occurs**, for independent trials with the same probability of success \(p\). \(X\) can be 1, 2, 3, … with no upper limit.
:::

:::key Geometric formulae
For \(X \sim \mathrm{Geo}(p)\), with \(q = 1 - p\):
\[P(X = r) = q^{r-1}p \qquad P(X > r) = q^r \qquad E(X) = \frac{1}{p}\]
The first formula and the mean are on MF19. To have \(r - 1\) failures and then a success, multiply \(q^{r-1}\) by \(p\). To need **more than** \(r\) trials, the first \(r\) trials must all fail: \(q^r\).
:::

:::eg A fair die is thrown until a six appears. Find the probability the first six is on the 4th throw, the probability that more than 4 throws are needed, the probability of a six within the first 3 throws, and the expected number of throws.
\(p = \dfrac16\), \(q = \dfrac56\).
\(P(X = 4) = \left(\dfrac56\right)^3\dfrac16 = 0.0965\).
\(P(X > 4) = \left(\dfrac56\right)^4 = 0.482\).
\(P(X \le 3) = 1 - P(X > 3) = 1 - \left(\dfrac56\right)^3 = 0.421\).
\(E(X) = \dfrac{1}{1/6} = 6\) throws.
:::

:::eg A basketball player scores each free throw with probability 0.7, independently. Find the probability that the first score is on the 3rd throw, and the mean number of throws needed.
\(X \sim \mathrm{Geo}(0.7)\). \(P(X = 3) = 0.3^2\times 0.7 = 0.063\). Mean \(= \dfrac{1}{0.7} = 1.43\) throws.
:::

The widget shows the geometric distribution. The bars always get shorter, and the smaller \(p\) is, the longer the tail.

:::html
<div class="widget" data-w="discrete" data-dist="geometric" data-p="0.25" data-range="1,3"></div>
:::

## Choosing the model

:::key Binomial or geometric?
- **Binomial**: a **fixed number** of trials, and you count the **successes**. "How many of the 20 bulbs are faulty?"
- **Geometric**: **no fixed number** of trials, and you count the **trials until the first success**. "How many bulbs must I test before I find a faulty one?"
:::

In both models the trials must be independent with a constant probability. In real situations this is only an approximation, so exam questions often ask you to comment: for example, picking from a small batch without replacement makes later trials depend on earlier ones.

:::eg (Exam style) A biased coin lands heads with probability 0.35. It is tossed 8 times. Find the probability of exactly 3 heads and of at least 5 heads, and the mean and variance of the number of heads. The coin is then tossed until it lands heads: find the probability that this takes exactly 3 tosses. [7 marks]
Let \(X\) be the number of heads in 8 tosses. \(X \sim B(8, 0.35)\). [B1]
\(P(X = 3) = \dbinom83(0.35)^3(0.65)^5 = 56\times 0.042875\times 0.116029 = 0.279\). [M1 A1]
\(P(X \ge 5) = P(5) + P(6) + P(7) + P(8) = 0.106\). [M1 A1]
\(E(X) = 8\times 0.35 = 2.8\) and \(\mathrm{Var}(X) = 8\times 0.35\times 0.65 = 1.82\). [B1]
For the geometric case, \(Y \sim \mathrm{Geo}(0.35)\) and \(P(Y = 3) = 0.65^2\times 0.35 = 0.148\). [B1]
:::

:::exam What earns marks
- **State the model and its parameters**: "Let \(X\) be the number of defective bulbs. \(X \sim B(20, 0.04)\)." This earns a mark on its own.
- **Show the unrounded formula**, such as \(\dbinom{10}{3}(0.3)^3(0.7)^7\), then the value.
- For "at least" or "more than", use the complement: \(P(X \ge 4) = 1 - P(X \le 3)\). The most common error is \(1 - P(X \le 4)\).
- Quote the **conditions** in a sentence when asked why a binomial model is suitable, and say whether each one is reasonable in the situation.
- **Variance**: \(E(X^2) - [E(X)]^2\). Subtract the **square** of the mean, not the mean.
:::

:::board Other boards
The UK A Level courses (AQA, OCR, Edexcel) include the binomial distribution and the expectation and variance of a discrete random variable. Edexcel IAL splits them: discrete random variables are in S1 and the binomial distribution is in S2. The geometric distribution is part of Cambridge Paper 5; if you are not taking Cambridge, check your own specification before spending time on it.
:::

:::try Start easy, finish at exam standard
Q: \(P(X = x) = k(5 - x)\) for \(x = 1, 2, 3, 4\). Find \(k\), \(E(X)\) and \(\mathrm{Var}(X)\).
A: \(k(4 + 3 + 2 + 1) = 1\), so \(k = 0.1\) and the probabilities are 0.4, 0.3, 0.2, 0.1. \(E(X) = 0.4 + 0.6 + 0.6 + 0.4 = 2\). \(E(X^2) = 0.4 + 1.2 + 1.8 + 1.6 = 5\). \(\mathrm{Var}(X) = 5 - 4 = 1\).
Q: \(X\) takes the values 2, 4, 6, 8 with probabilities 0.1, 0.4, 0.3, 0.2. Find \(E(X)\) and the standard deviation.
A: \(E(X) = 0.2 + 1.6 + 1.8 + 1.6 = 5.2\). \(E(X^2) = 0.4 + 6.4 + 10.8 + 12.8 = 30.4\). \(\mathrm{Var}(X) = 30.4 - 27.04 = 3.36\); standard deviation \(1.83\).
Q: \(X \sim B(6, 0.5)\). Find \(P(X = 2)\) and \(P(X \ge 5)\).
A: \(P(X = 2) = \dfrac{15}{64} = 0.234\). \(P(X \ge 5) = \dfrac{6 + 1}{64} = 0.109\).
Q: \(X \sim B(15, 0.4)\). Find \(P(X \le 6)\), \(P(X = 6)\), the mean and the variance.
A: \(P(X \le 6) = 0.610\). \(P(X = 6) = \dbinom{15}{6}(0.4)^6(0.6)^9 = 0.207\). Mean \(= 6\), variance \(= 15\times 0.4\times 0.6 = 3.6\).
Q: A fair die is thrown 5 times. Find the probability of at least one six.
A: \(1 - \left(\dfrac56\right)^5 = 0.598\).
Q: \(X \sim \mathrm{Geo}(0.2)\). Find \(P(X = 5)\), \(P(X > 5)\) and \(E(X)\).
A: \(P(X = 5) = 0.8^4\times 0.2 = 0.0819\). \(P(X > 5) = 0.8^5 = 0.328\). \(E(X) = 5\).
Q: Each free throw scores with probability 0.7. Find the probability that the first score comes on the 3rd throw and the expected number of throws.
A: \(0.3^2\times 0.7 = 0.063\); the expected number is \(\dfrac1{0.7} = 1.43\).
Q: Bulbs are defective with probability 0.04. Find the smallest sample size \(n\) so that the probability of at least one defective bulb exceeds 0.95.
A: \(1 - 0.96^n > 0.95\), so \(0.96^n < 0.05\) and \(n > \dfrac{\ln 0.05}{\ln 0.96} = 73.4\). So \(n = 74\).
Q: (Exam style) A multiple-choice test has 12 questions, each with four options, one correct. A student guesses every answer. Find the probability of exactly 4 correct answers, and of at least one correct answer. State one assumption needed. [5 marks]
A: \(X \sim B(12, 0.25)\). [B1] \(P(X = 4) = \dbinom{12}{4}(0.25)^4(0.75)^8 = 495\times 0.00390625\times 0.100113 = 0.194\). [M1 A1] \(P(X \ge 1) = 1 - 0.75^{12} = 1 - 0.0317 = 0.968\). [M1 A1] The answers to different questions are independent, with the same probability 0.25 of being right each time. [B1]
:::

:::quiz
? Which of these is **not** suitable for a binomial model?
- The number of sixes in 10 throws of a fair die.
- The number of faulty bulbs in a box of 20, each independently faulty with probability 0.04.
+ The number of hearts when 5 cards are dealt from a pack, without replacement.
- The number of heads in 8 tosses of a fair coin.
> Without replacement, the probability of a heart changes after each card, so the trials are not independent with a constant \(p\).
? \(X \sim B(20, 0.3)\). What is \(E(X)\)?
- \(0.3\)
+ \(6\)
- \(4.2\)
- \(20\)
> The mean is \(np = 20\times 0.3 = 6\). The variance is \(npq = 4.2\).
? \(X \sim \mathrm{Geo}(0.2)\). What is \(P(X > 3)\)?
- \(0.2^3\)
- \(1 - 0.8^3\)
+ \(0.8^3 = 0.512\)
- \(0.8^2\times 0.2\)
> More than 3 trials are needed only if the first 3 all fail, which has probability \(0.8^3\).
? In \(\mathrm{Var}(X) = E(X^2) - [E(X)]^2\), a student gets \(E(X) = 3\) and \(E(X^2) = 12\). What is the variance?
- \(9\)
+ \(3\)
- \(6\)
- \(-3\)
> \(12 - 3^2 = 3\). Subtracting \(3\) instead of \(3^2\) gives 9, a common slip.
? The probabilities in a distribution table for \(X\) add to 1.2. What is wrong?
- Nothing: probabilities can exceed 1.
- The mean is wrong.
+ The probabilities of a complete distribution must sum to exactly 1, so one or more values are wrong.
- The variable is continuous.
> A valid distribution has \(\sum P(X = x) = 1\); a sum of 1.2 means at least one probability has been miscalculated.
:::

:::recap
- A discrete random variable has a distribution table with \(\sum P(X = x) = 1\); \(E(X) = \sum xP(X = x)\), \(E(X^2) = \sum x^2P(X = x)\), \(\mathrm{Var}(X) = E(X^2) - [E(X)]^2\).
- \(X \sim B(n, p)\): fixed \(n\), two outcomes, independent trials, constant \(p\). \(P(X = r) = \dbinom nr p^r q^{n-r}\), \(E(X) = np\), \(\mathrm{Var}(X) = npq\).
- \(X \sim \mathrm{Geo}(p)\): trials until the first success. \(P(X = r) = q^{r-1}p\), \(P(X > r) = q^r\), \(E(X) = \dfrac1p\).
- "At least" uses the complement: \(P(X \ge r) = 1 - P(X \le r - 1)\).
- State the model and parameters; comment on the conditions when asked.
:::

:::links
- watch: [The binomial distribution](https://www.examsolutions.net/tutorials/binomial-distribution/) · ExamSolutions · B(n, p) probabilities step by step
- watch: [Binomial distributions](https://www.3blue1brown.com/lessons/binomial-distributions) · 3Blue1Brown · where the binomial formula comes from
- watch: [Exam questions: discrete random variables](https://www.examsolutions.net/tutorials/exam-questions-discrete-random-variables/) · ExamSolutions · tables, E(X) and Var(X)
- practise: [CAIE S1 binomial and geometric exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/statistical-distributions/binomial-and-geometric-distribution/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Plinko Probability](https://phet.colorado.edu/en/simulations/plinko-probability) · PhET · watch a binomial distribution build up ball by ball
- explore: [Probability distributions](https://seeing-theory.brown.edu/probability-distributions/index.html) · Seeing Theory · interactive discrete distributions

Links checked 3 October 2026.
:::
Next: [The normal distribution](#math.s1.normal).
