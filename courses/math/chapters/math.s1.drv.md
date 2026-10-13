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

:::try Warm-up
Q: Solve \(2^n = 50\), giving \(n\) to 3 significant figures. (from [Exponentials and logarithms](#math.p3.logs))
A: Take logarithms: \(n\ln 2 = \ln 50\), so \(n = \dfrac{\ln 50}{\ln 2} = 5.64\).
Q: In how many ways can 3 people be chosen from 10? (from [Permutations and combinations](#math.s1.perms))
A: Order does not matter: \(\dbinom{10}{3} = 120\).
Q: A fair die is thrown. Find the probability that the first six comes on the third throw. (from [Probability](#math.s1.prob))
A: Two non-sixes and then a six: \(\left(\dfrac56\right)^2 \times \dfrac16\) \(= \dfrac{25}{216} = 0.116\).
:::

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
\(E(X)\) \(= 1(0.1) + 2(0.2) + 3(0.3) + 4(0.4)\) \(= 0.1 + 0.4 + 0.9 + 1.6 = 3\).
\(E(X^2)\) \(= 1(0.1) + 4(0.2) + 9(0.3) + 16(0.4)\) \(= 0.1 + 0.8 + 2.7 + 6.4\) \(= 10\).
\(\mathrm{Var}(X) = 10 - 3^2 = 1\), so the standard deviation is 1.
:::

:::eg The random variable \(X\) has the table below, with \(E(X) = 1.6\). Find \(a\) and \(b\), then \(\mathrm{Var}(X)\).

| \(x\) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| \(P(X = x)\) | 0.2 | \(a\) | 0.3 | \(b\) |

The probabilities sum to 1: \(0.2 + a + 0.3 + b = 1\), so \(a + b = 0.5\).
From the mean: \(0(0.2) + 1(a) + 2(0.3) + 3b = 1.6\), so \(a + 3b = 1\).
Subtract: \(2b = 0.5\), so \(b = 0.25\) and \(a = 0.25\).
\(E(X^2) = 0 + 0.25 + 4(0.3) + 9(0.25)\) \(= 0.25 + 1.2 + 2.25 = 3.7\), so \(\mathrm{Var}(X) = 3.7 - 1.6^2 = 1.14\).
:::

:::eg (Real context) A game costs £2 to play. A fair die is rolled: a 6 pays £5, a 4 or 5 pays £1, and anything else pays nothing. Let \(X\) be the player's net gain in pounds. Find \(E(X)\) and the standard deviation.
The net gain is the prize minus the £2 stake. A 6 gives \(5 - 2 = 3\); a 4 or 5 gives \(1 - 2 = -1\); otherwise \(-2\).

| \(x\) | \(-2\) | \(-1\) | \(3\) |
|---|---|---|---|
| \(P(X = x)\) | \(\frac36\) | \(\frac26\) | \(\frac16\) |

\(E(X)\) \(= -2\cdot\frac12 - 1\cdot\frac13 + 3\cdot\frac16\) \(= -1 - 0.3333 + 0.5 = -0.833\). The player loses about 83p per game on average.
\(E(X^2)\) \(= 4\cdot\frac12 + 1\cdot\frac13 + 9\cdot\frac16\) \(= 3.833\), so \(\mathrm{Var}(X) = 3.833 - 0.833^2\) \(= 3.139\) and the standard deviation is \(1.77\).
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

:::proof Why \(E(X) = np\) for the binomial distribution
By definition, \(E(X)\) \(= \sum_{r=0}^{n} r\binom{n}{r}p^r q^{n-r}\). The term for \(r = 0\) is zero, so start at \(r = 1\).
For \(r \ge 1\), cancel \(r\) with the factorial in \(r!\):
\[r\binom{n}{r} = \frac{r \times n!}{r!\,(n-r)!} = \frac{n!}{(r-1)!\,(n-r)!} = n\binom{n-1}{r-1}\]
Substitute, and take out one factor \(n\) and one factor \(p\):
\[E(X) = np\sum_{r=1}^{n}\binom{n-1}{r-1}p^{r-1}q^{n-r}\]
Put \(s = r - 1\). The sum becomes \(\sum_{s=0}^{n-1}\binom{n-1}{s}p^s q^{(n-1)-s}\), which is the binomial expansion of \((p + q)^{n-1}\). Since \(p + q = 1\), this is \(1\).
So \(E(X) = np\). Check with \(B(2, 0.5)\): \(0(0.25) + 1(0.5) + 2(0.25) = 1\) \(= 2 \times 0.5\).
:::

:::eg \(X \sim B(10, 0.3)\). Find (a) \(P(X = 3)\), (b) \(P(X \le 2)\), (c) \(P(X \ge 4)\), (d) the mean and variance.
(a) \(P(X = 3)\) \(= \dbinom{10}{3}(0.3)^3(0.7)^7\) \(= 120\times 0.027\times 0.0823543\) \(= 0.267\).
(b) \(P(X \le 2) = P(0) + P(1) + P(2)\) \(= 0.7^{10} + 10(0.3)(0.7)^9 + 45(0.3)^2(0.7)^8\)
So \(P(X \le 2)\) \(= 0.0282 + 0.1211 + 0.2335\) \(= 0.383\).
(c) \(P(X \ge 4) = 1 - P(X \le 3)\) \(= 1 - (0.3828 + 0.2668) = 0.350\).
(d) \(E(X) = 10\times 0.3 = 3\) and \(\mathrm{Var}(X)\) \(= 10\times 0.3\times 0.7 = 2.1\).
:::

The widget draws the distribution, highlights a range, and gives \(P(a \le X \le b)\), the mean and the variance. Change \(n\) and \(p\) to see the shape: it is skewed for small or large \(p\), and symmetric at \(p = 0.5\).

:::html
<div class="widget" data-w="discrete" data-dist="binomial" data-n="10" data-p="0.3" data-range="0,2"></div>
:::

:::eg (Real context) A factory finds that 4% of its light bulbs are defective, independently of each other. A box holds 20 bulbs. Find the probability that a box has no defective bulbs, and that it has at most 2.
Let \(X\) be the number of defective bulbs in a box. \(X \sim B(20, 0.04)\).
\(P(X = 0) = 0.96^{20} = 0.442\).
\(P(X \le 2)\) \(= 0.96^{20} + 20(0.04)(0.96)^{19}\) \(+ 190(0.04)^2(0.96)^{18}\) \(= 0.4420 + 0.3683 + 0.1458 = 0.956\).
:::

:::eg (Exam style) The probability that a bulb is defective is 0.04, independently. Find the smallest number \(n\) of bulbs in a sample so that the probability of at least one defective bulb is greater than 0.9. [4 marks]
\(P(\text{at least one defective})\) \(= 1 - 0.96^n > 0.9\). [M1]
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

:::proof Why \(E(X) = \dfrac{1}{p}\) for the geometric distribution
By definition, \(E(X) = \sum_{r=1}^{\infty} r\,q^{r-1}p\) \(= p\,(1 + 2q + 3q^2 + 4q^3 + \cdots)\). Call the bracket \(S\).
Multiply \(S\) by \(q\) and subtract:
\[S - qS = (1 + 2q + 3q^2 + \cdots) - (q + 2q^2 + 3q^3 + \cdots) = 1 + q + q^2 + \cdots\]
The right-hand side is a geometric series with first term 1 and common ratio \(q\). Because \(0 < q < 1\), it has a sum to infinity of \(\dfrac{1}{1 - q}\). Since \(S - qS = S(1 - q)\), we get
\[S(1 - q) = \frac{1}{1 - q} \qquad\text{so}\qquad S = \frac{1}{(1 - q)^2} = \frac{1}{p^2}\]
Therefore \(E(X) = p \times \dfrac{1}{p^2}\) \(= \dfrac1p\). Check with a fair die: \(p = \dfrac16\) gives \(E(X) = 6\) throws.
:::

:::eg A fair die is thrown until a six appears. Find the probability the first six is on the 4th throw, the probability that more than 4 throws are needed, the probability of a six within the first 3 throws, and the expected number of throws.
\(p = \dfrac16\), \(q = \dfrac56\).
\(P(X = 4)\) \(= \left(\dfrac56\right)^3\dfrac16\) \(= 0.0965\).
\(P(X > 4) = \left(\dfrac56\right)^4\) \(= 0.482\).
\(P(X \le 3) = 1 - P(X > 3)\) \(= 1 - \left(\dfrac56\right)^3 = 0.421\).
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
\(P(X = 3) = \dbinom83(0.35)^3(0.65)^5\) \(= 56\times 0.042875\times 0.116029\) \(= 0.279\). [M1 A1]
\(P(X \ge 5) = P(5) + P(6) + P(7) + P(8)\) \(= 0.106\). [M1 A1]
\(E(X) = 8\times 0.35 = 2.8\) and \(\mathrm{Var}(X)\) \(= 8\times 0.35\times 0.65 = 1.82\). [B1]
For the geometric case, \(Y \sim \mathrm{Geo}(0.35)\) and \(P(Y = 3) = 0.65^2\times 0.35 = 0.148\). [B1]
:::

## Long exam questions

:::eg (Exam style) The discrete random variable \(X\) has the probability distribution shown, and \(E(X) = 1.65\).

| \(x\) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| \(P(X = x)\) | 0.15 | \(a\) | 0.35 | \(b\) |

(a) Find the values of \(a\) and \(b\). (b) Find \(\mathrm{Var}(X)\). (c) Two independent values of \(X\) are observed. Find the probability that their sum is 3. [10 marks]
(a) The probabilities add up to 1: \(0.15 + a + 0.35 + b = 1\), so \(a + b = 0.5\). [M1]
The mean is 1.65: \(0(0.15) + 1(a) + 2(0.35) + 3b = 1.65\), so \(a + 3b = 0.95\). [M1]
Subtract the first equation from the second: \(2b = 0.45\), so \(b = 0.225\). [A1] Then \(a = 0.275\). [A1]
(b) \(E(X^2)\) \(= 0 + 1(0.275) + 4(0.35) + 9(0.225)\) [M1] \(= 0.275 + 1.4 + 2.025 = 3.7\). [A1]
\(\mathrm{Var}(X) = 3.7 - 1.65^2\) \(= 3.7 - 2.7225 = 0.9775\), which is \(0.978\) to 3 s.f. [A1]
(c) The sum is 3 when the two values are \((0, 3)\), \((3, 0)\), \((1, 2)\) or \((2, 1)\). [M1] The order matters, so each pair of different values can occur in two ways: [M1]
\[2(0.15)(0.225) + 2(0.275)(0.35) = 0.0675 + 0.1925 = 0.26\]
[A1]
:::

:::eg (Exam style) A machine makes bolts. Each bolt is faulty with probability 0.08, independently of the others. A packet contains 15 bolts. (a) Find the probability that a packet contains exactly 2 faulty bolts. (b) A packet is rejected if it contains 2 or more faulty bolts. Show that the probability that a packet is rejected is 0.340, to 3 significant figures. (c) A customer buys 10 packets. Find the probability that exactly 2 of them are rejected. (d) Comment on whether the model is realistic. [10 marks]
(a) Let \(X\) be the number of faulty bolts in a packet. \(X \sim B(15, 0.08)\). [B1]
\[P(X = 2) = \binom{15}{2}(0.08)^2(0.92)^{13} = 105 \times 0.0064 \times 0.33825\]
[M1] \(= 0.227\). [A1]
(b) A rejected packet has \(X \ge 2\), so use the complement: \(P(X \ge 2) = 1 - P(X \le 1)\). [M1]
\[P(X = 0) = 0.92^{15} = 0.2863 \qquad P(X = 1) = 15(0.08)(0.92)^{14} = 0.3734\]
[A1] so \(P(X \ge 2) = 1 - 0.6597 = 0.340\). [A1]
(c) Let \(Y\) be the number of rejected packets. \(Y \sim B(10, 0.3403)\). [B1]
\[P(Y = 2) = \binom{10}{2}(0.3403)^2(0.6597)^8\]
[M1] \(= 45 \times 0.11580 \times 0.035873\) \(= 0.187\). [A1]
(d) The model needs the bolts to be faulty independently. If a fault comes from a machine setting that drifts, faulty bolts would come in runs, so the faults would not be independent and the true variation between packets would be larger than the model suggests. [B1]
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

:::eg Spot the error: "at least" with a binomial
A student wrote this answer to "\(X \sim B(12, 0.25)\). Find \(P(X \ge 3)\)" [3 marks]. Use \(P(X \le 2) = 0.3907\) and \(P(X \le 3) = 0.6488\).

Line 1: \(X \sim B(12, 0.25)\).
Line 2: \(P(X \ge 3) = 1 - P(X \le 3)\) \(= 1 - 0.6488 = 0.351\).

**Line 1 earns [B1]** for stating the model. **Line 2 scores [M0 A0].** The complement of "\(X\) is at least 3" is "\(X\) is at most **2**", not "at most 3". The student has removed the value \(X = 3\) as well, so the method is wrong and the answer mark is lost. The student scores 1 out of 3.

Correct working: \(P(X \ge 3) = 1 - P(X \le 2)\) [M1] \(= 1 - 0.3907 = 0.609\). [A1]

**Check:** the mean is \(12 \times 0.25 = 3\), so a value of 3 or more should be a little more likely than not. The student's \(0.351\) is too small, and \(0.609\) is sensible. ✓
:::

:::try Start easy, finish at exam standard
Q: \(P(X = x) = k(5 - x)\) for \(x = 1, 2, 3, 4\). Find \(k\), \(E(X)\) and \(\mathrm{Var}(X)\).
A: \(k(4 + 3 + 2 + 1) = 1\), so \(k = 0.1\) and the probabilities are 0.4, 0.3, 0.2, 0.1. \(E(X) = 0.4 + 0.6 + 0.6 + 0.4 = 2\). \(E(X^2) = 0.4 + 1.2 + 1.8 + 1.6 = 5\). \(\mathrm{Var}(X) = 5 - 4 = 1\).
Q: \(X\) takes the values 2, 4, 6, 8 with probabilities 0.1, 0.4, 0.3, 0.2. Find \(E(X)\) and the standard deviation.
A: \(E(X) = 0.2 + 1.6 + 1.8 + 1.6 = 5.2\). \(E(X^2) = 0.4 + 6.4 + 10.8 + 12.8\) \(= 30.4\). \(\mathrm{Var}(X) = 30.4 - 27.04 = 3.36\); standard deviation \(1.83\).
Q: \(X \sim B(6, 0.5)\). Find \(P(X = 2)\) and \(P(X \ge 5)\).
A: \(P(X = 2) = \dfrac{15}{64} = 0.234\). \(P(X \ge 5) = \dfrac{6 + 1}{64} = 0.109\).
Q: \(X \sim B(15, 0.4)\). Find \(P(X \le 6)\), \(P(X = 6)\), the mean and the variance.
A: \(P(X \le 6) = 0.610\). \(P(X = 6)\) \(= \dbinom{15}{6}(0.4)^6(0.6)^9 = 0.207\). Mean \(= 6\), variance \(= 15\times 0.4\times 0.6 = 3.6\).
Q: A fair die is thrown 5 times. Find the probability of at least one six.
A: \(1 - \left(\dfrac56\right)^5 = 0.598\).
Q: \(X \sim \mathrm{Geo}(0.2)\). Find \(P(X = 5)\), \(P(X > 5)\) and \(E(X)\).
A: \(P(X = 5) = 0.8^4\times 0.2 = 0.0819\). \(P(X > 5) = 0.8^5 = 0.328\). \(E(X) = 5\).
Q: Each free throw scores with probability 0.7. Find the probability that the first score comes on the 3rd throw and the expected number of throws.
A: \(0.3^2\times 0.7 = 0.063\); the expected number is \(\dfrac1{0.7} = 1.43\).
Q: Bulbs are defective with probability 0.04. Find the smallest sample size \(n\) so that the probability of at least one defective bulb exceeds 0.95.
A: \(1 - 0.96^n > 0.95\), so \(0.96^n < 0.05\) and \(n > \dfrac{\ln 0.05}{\ln 0.96} = 73.4\). So \(n = 74\).
Q: (Exam style) A multiple-choice test has 12 questions, each with four options, one correct. A student guesses every answer. Find the probability of exactly 4 correct answers, and of at least one correct answer. State one assumption needed. [6 marks]
A: \(X \sim B(12, 0.25)\). [B1] \(P(X = 4)\) \(= \dbinom{12}{4}(0.25)^4(0.75)^8\) \(= 495\times 0.00390625\times 0.100113\) \(= 0.194\). [M1 A1] \(P(X \ge 1) = 1 - 0.75^{12}\) \(= 1 - 0.0317 = 0.968\). [M1 A1] The answers to different questions are independent, with the same probability 0.25 of being right each time. [B1]
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The random variable \(X\) takes the values 1, 2, 3, 4 with probabilities 0.2, 0.4, \(k\) and 0.1. (a) Find \(k\). (b) Find \(E(X)\).
A: (a) The probabilities sum to 1: \(0.2 + 0.4 + k + 0.1 = 1\). [M1] So \(k = 0.3\). [A1] (b) \(E(X)\) \(= 1(0.2) + 2(0.4) + 3(0.3) + 4(0.1)\) [M1] \(= 0.2 + 0.8 + 0.9 + 0.4 = 2.3\). [A1]
Q: [4 marks] ★ \(X \sim B(8, 0.4)\). Find \(P(X = 3)\), \(E(X)\) and \(\mathrm{Var}(X)\).
A: \(P(X = 3) = \dbinom83(0.4)^3(0.6)^5\) [M1] \(= 56 \times 0.064 \times 0.07776\) \(= 0.279\). [A1] \(E(X) = 8 \times 0.4 = 3.2\). [B1] \(\mathrm{Var}(X)\) \(= 8 \times 0.4 \times 0.6 = 1.92\). [B1]
Q: [4 marks] ★ \(X \sim \mathrm{Geo}(0.15)\). Find \(P(X = 4)\), \(P(X > 6)\) and \(E(X)\).
A: \(P(X = 4) = 0.85^3 \times 0.15\) [M1] \(= 0.0921\). [A1] \(P(X > 6) = 0.85^6 = 0.377\). [B1] \(E(X) = \dfrac{1}{0.15} = 6.67\). [B1]
Q: [4 marks] ★★ \(X \sim B(20, 0.15)\). Find \(P(X \ge 3)\).
A: State the model \(X \sim B(20, 0.15)\). [B1] The complement of "at least 3" is "at most 2": \(P(X \ge 3) = 1 - P(X \le 2)\). [M1] Now
\[P(X \le 2) = 0.85^{20} + 20(0.15)(0.85)^{19} + 190(0.15)^2(0.85)^{18}\]
[M1] which is \(0.0388 + 0.1368 + 0.2293 = 0.4049\). So \(P(X \ge 3) = 0.595\). [A1]
Q: [4 marks] ★★ \(X \sim \mathrm{Geo}(0.3)\). Find the smallest value of \(r\) such that \(P(X \le r) > 0.95\).
A: \(P(X \le r) = 1 - 0.7^r > 0.95\), so \(0.7^r < 0.05\). [M1 A1] Take logarithms and reverse the inequality, because \(\ln 0.7\) is negative: \(r > \dfrac{\ln 0.05}{\ln 0.7} = 8.40\). [M1] The smallest whole number is \(r = 9\). [A1]
Q: [3 marks] ★★ A farmer packs eggs in boxes of 12. About 6% of eggs are cracked. A student suggests that the number of cracked eggs in a box is \(B(12, 0.06)\). State the conditions needed for this model, and explain why a box that was dropped on the way to the shop would break one of them.
A: The model needs a fixed number of trials, two outcomes, a constant probability 0.06 of a cracked egg, and independent eggs. [B1] If the box was dropped, a crack in one egg makes cracks in its neighbours more likely, so the eggs are not independent. [B1] The probability of a crack is also higher than 0.06 for that box, so the constant probability condition fails too. [B1]
Q: [8 marks] ★★ A player pays £3 to play a game. A fair coin is tossed up to three times and the game stops at the first head. If the first head is on toss 1 the player wins £5, on toss 2 wins £4 and on toss 3 wins £2. If there is no head in three tosses, the player wins nothing. Let \(X\) be the player's net gain in pounds. Find (a) the distribution of \(X\), (b) \(E(X)\), (c) the standard deviation of \(X\).
A: (a) The net gains are \(5 - 3 = 2\), \(4 - 3 = 1\), \(2 - 3 = -1\) and \(0 - 3 = -3\). [B1] Their probabilities are \(\dfrac12\), \(\dfrac14\), \(\dfrac18\) and \(\dfrac18\), which sum to 1. [B1] So \(X = 2, 1, -1, -3\) with \(P(X = x)\) \(= \dfrac12, \dfrac14, \dfrac18, \dfrac18\) respectively. (b) \(E(X)\) \(= 2\left(\tfrac12\right) + 1\left(\tfrac14\right) - 1\left(\tfrac18\right) - 3\left(\tfrac18\right)\) [M1] \(= 1 + 0.25 - 0.125 - 0.375 = 0.75\). The player gains 75p per game on average. [A1] (c) \(E(X^2)\) \(= 4\left(\tfrac12\right) + 1\left(\tfrac14\right) + 1\left(\tfrac18\right) + 9\left(\tfrac18\right)\) \(= 3.5\). [M1 A1] The variance is \(3.5 - 0.75^2 = 2.9375\) [M1] and the standard deviation is \(1.71\). [A1]
Q: [9 marks] (#math.p3.logs) ★★★ \(X \sim B(n, p)\) has mean 6 and variance 4.2. (a) Find \(n\) and \(p\). (b) Find \(P(X = 6)\). (c) A new sample of \(m\) independent trials, each with the same probability of success \(p\), is taken. Find the smallest value of \(m\) for which the probability of at least one success is greater than 0.99.
H: You have two equations: \(np = 6\) and \(npq = 4.2\). Divide the second by the first to find \(q\).
H: For (c), "at least one success" is \(1 - q^m\). Write \(1 - q^m > 0.99\) and take logarithms.
H: Taking logarithms of a number less than 1 gives a negative value, so the inequality reverses when you divide by it.
A: (a) Dividing, \(\dfrac{npq}{np} = \dfrac{4.2}{6}\), so \(q = 0.7\). [M1 A1] Then \(p = 0.3\) and \(n = \dfrac{6}{0.3} = 20\). [A1] (b) \(P(X = 6)\) \(= \dbinom{20}{6}(0.3)^6(0.7)^{14}\) [M1] \(= 38\,760 \times 0.000729 \times 0.0067822\) \(= 0.192\). [A1] (c) \(1 - 0.7^m > 0.99\), so \(0.7^m < 0.01\). [M1] Taking logarithms, \(m\ln 0.7 < \ln 0.01\). Since \(\ln 0.7 < 0\), dividing reverses the inequality: [M1] \(m > \dfrac{\ln 0.01}{\ln 0.7} = 12.9\). [A1] The smallest whole number is \(m = 13\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ Anil and Beth take turns to throw a fair die, Anil first. The first person to throw a six wins. Find the probability that Anil wins, and say who has the advantage.
H: Anil wins on his first throw with probability \(\dfrac16\). His second throw is the third throw of the game, so for him to win on it, the first two throws must both be non-sixes.
H: List the probabilities of Anil winning on his 1st, 2nd and 3rd throws. What kind of sequence is this, and what is its common ratio?
H: Use the sum to infinity \(\dfrac{a}{1 - r}\) of a geometric series. Beth's probability is what is left.
A: Anil wins on throw 1 with probability \(\dfrac16\). [B1] His second throw is the third throw of the game. He wins on it if throws 1 and 2 are non-sixes and throw 3 is a six: \(\left(\dfrac56\right)^2\dfrac16\). On his third throw (the fifth of the game) the probability is \(\left(\dfrac56\right)^4\dfrac16\). [M1] The probabilities form a geometric series with first term \(\dfrac16\). [M1] The common ratio is \(\left(\dfrac56\right)^2\) \(= \dfrac{25}{36}\). [A1] Since \(|r| < 1\), the sum to infinity exists: [M1]
\[P(\text{Anil wins}) = \frac{\frac16}{1 - \frac{25}{36}} = \frac{\frac16}{\frac{11}{36}} = \frac{6}{11}\]
[A1] So Beth wins with probability \(\dfrac{5}{11}\). Anil has the advantage because he throws first. [B1]
Q: [6 marks] ★★★ \(X \sim \mathrm{Geo}(p)\) and \(q = 1 - p\). (a) Show that for positive integers \(a\) and \(b\), \(P(X > a + b \mid X > a) = P(X > b)\). (b) A call is answered on any attempt with probability 0.2, independently. Eve has already tried 5 times without success. Find the probability that she needs more than 3 further attempts. (c) What does the result in (a) say about the geometric distribution?
H: \(P(X > a + b \mid X > a)\) \(= \dfrac{P(X > a + b \text{ and } X > a)}{P(X > a)}\). If \(X > a + b\), then \(X > a\) is automatic.
H: Use \(P(X > r) = q^r\) for each part and simplify the powers.
A: (a) If \(X > a + b\) then \(X > a\) as well, so the numerator is just \(P(X > a + b)\). [M1] Then
\[P(X > a + b \mid X > a) = \frac{q^{a+b}}{q^a}\]
[M1] \(= q^b = P(X > b)\). [A1] (b) With \(a = 5\) and \(b = 3\), the probability is \(P(X > 3) = 0.8^3\) [M1] \(= 0.512\). [A1] (c) Past failures make no difference to how many more trials are needed: the geometric distribution has no memory. [B1]
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

:::checklist What you can now do
- [ ] I can write down a probability distribution table and find an unknown value from \(\sum P(X = x) = 1\).
- [ ] I can find \(E(X)\), \(E(X^2)\) and \(\mathrm{Var}(X)\) from a distribution table, including when two unknowns are found from the mean.
- [ ] I can decide whether a situation fits \(B(n, p)\) and state the conditions.
- [ ] I can find binomial probabilities, including "at most", "at least" and "more than", and the mean \(np\) and variance \(npq\).
- [ ] I can decide whether a situation fits \(\mathrm{Geo}(p)\) and find \(P(X = r)\), \(P(X > r)\) and the mean \(\dfrac1p\).
- [ ] I can find the smallest number of trials needed for a given probability, using logarithms.
- [ ] I can say whether the independence and constant probability conditions are realistic in a given context.
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
