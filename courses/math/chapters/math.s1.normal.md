@chapter math.s1.normal
@title The normal distribution
@level a2
@paper CAIE P5 (check your specification for other boards)
@time 9–11 hours
@summary The normal distribution \(N(\mu, \sigma^2)\): its bell-shaped curve, standardising with \(Z = \dfrac{X - \mu}{\sigma}\), reading probabilities from the normal table in both directions, finding \(\mu\) and \(\sigma\) from given probabilities, and using a normal distribution to approximate a binomial one with a continuity correction.

:::why
Heights, masses of packed goods, measurement errors and exam marks all pile up around a typical value and thin out symmetrically on either side. The normal distribution is the mathematical model of that pattern, and it is the most used distribution in statistics. Once you can standardise, one table answers every question about every normal distribution.
:::

**Before you start**, you need the probability rules in [Probability](#math.s1.prob), the mean and standard deviation in [Representing and summarising data](#math.s1.data), the binomial distribution in [Discrete random variables: binomial and geometric](#math.s1.drv), and solving simultaneous equations from [Algebra from scratch](#math.f.algebra).

## The normal curve

A **continuous random variable** takes any value in a range, and its probabilities are **areas under a curve** (the probability density curve). For a continuous variable \(P(X = a) = 0\), so \(P(X < a)\) and \(P(X \le a)\) are the same.

:::def Normal distribution
\(X \sim N(\mu, \sigma^2)\) means \(X\) is normally distributed with **mean** \(\mu\) and **variance** \(\sigma^2\) (so the **standard deviation** is \(\sigma\)). The graph is a symmetrical bell shape centred on \(\mu\); the total area under it is 1. About 68% of the values lie within one standard deviation of the mean, about 95% within two, and nearly all within three.
:::

Notice the notation: the second number in \(N(50, 8^2)\) is the **variance**, \(\sigma^2 = 64\), so \(\sigma = 8\).

## Standardising

All normal curves have the same shape; they differ only in centre and scale. To use one table for all of them, convert \(X\) to the **standard normal** variable \(Z\), which has mean 0 and standard deviation 1.

:::key Standardising
\[Z = \frac{X - \mu}{\sigma} \sim N(0, 1)\]
\(\Phi(z) = P(Z \le z)\) is the area to the left of \(z\). The normal table gives \(\Phi(z)\) for \(z \ge 0\). By symmetry, \(\Phi(-z) = 1 - \Phi(z)\) and \(P(Z > z) = 1 - \Phi(z)\).
:::

The \(z\)-value says how many standard deviations a value is from the mean. Always sketch the curve and shade the area you want; this shows whether to subtract from 1.

:::plot The standard normal curve with the area \(P(-1 < Z < 1.25)\) shaded. It equals \(\Phi(1.25) - \Phi(-1) = 0.8944 - 0.1587 = 0.7357\).
--f "0.39894*exp(-(x**2)/2)" --label "N(0, 1)" --x -4 4 --y 0 0.45 --shade "0,-1,1.25" --vline 0 --legend tr
:::

:::eg \(X \sim N(50, 8^2)\). Find (a) \(P(X < 58)\), (b) \(P(X > 45)\), (c) \(P(42 < X < 60)\).
(a) \(z = \dfrac{58 - 50}{8} = 1\), so \(P(X < 58) = \Phi(1) = 0.8413\).
(b) \(z = \dfrac{45 - 50}{8} = -0.625\). \(P(X > 45) = P(Z > -0.625) = \Phi(0.625) = 0.734\).
(c) \(z\)-values \(\dfrac{42 - 50}{8} = -1\) and \(\dfrac{60 - 50}{8} = 1.25\). \(P(-1 < Z < 1.25) = \Phi(1.25) - \Phi(-1) = 0.8944 - 0.1587 = 0.736\).
:::

The widget shades the area between any two values, or below or above one, for any mean and standard deviation, and shows the \(z\)-values. Use it to check your table answers.

:::html
<div class="widget" data-w="normal" data-mu="50" data-sigma="8" data-a="42" data-b="60" data-mode="between"></div>
:::

:::eg (Real context) Bags of flour are filled with mass \(X\) grams, where \(X \sim N(500, 6^2)\). Find the proportion of bags with mass below 490 g, and the mass exceeded by 10% of bags.
\(z = \dfrac{490 - 500}{6} = -1.667\), so \(P(X < 490) = \Phi(-1.667) = 1 - \Phi(1.667) = 0.0478\): about 4.8% of bags.
For the mass \(m\) exceeded by 10% of bags, \(P(X > m) = 0.1\), so \(P(X < m) = 0.9\). The table (inverse) gives \(z = 1.2816\). Then \(m = 500 + 1.2816\times 6 = 507.7\) g.
:::

:::eg (Real context) Anna scores 70 in a test where the marks are \(N(62, 8^2)\), and 63 in a second test where the marks are \(N(55, 5^2)\). Which is the better performance relative to the other candidates?
Test 1: \(z = \dfrac{70 - 62}{8} = 1\), so she beat \(\Phi(1) = 84.1\%\) of candidates.
Test 2: \(z = \dfrac{63 - 55}{5} = 1.6\), so she beat \(\Phi(1.6) = 94.5\%\) of candidates.
Her second mark is the better performance, even though it is the lower mark, because it is further above the mean in standard deviations.
:::

:::eg A machine makes rods whose lengths, in cm, are \(N(20.0, 0.15^2)\). Rods are rejected if the length is outside the range 19.7 cm to 20.3 cm. What proportion is rejected, and how many rejects would you expect in a batch of 500?
The limits are \(\dfrac{19.7 - 20}{0.15} = -2\) and \(\dfrac{20.3 - 20}{0.15} = 2\). \(P(\text{accepted}) = \Phi(2) - \Phi(-2) = 0.9772 - 0.0228 = 0.9545\).
Proportion rejected \(= 1 - 0.9545 = 0.0455\). In a batch of 500 you expect \(500\times 0.0455 = 22.75\), so about 23 rods.
:::

## Using the table in reverse

Sometimes the probability is given and you need the value. Find the \(z\) with \(\Phi(z) = p\) (the table in reverse, or the percentage points table), then convert back with \(x = \mu + z\sigma\).

:::key Inverse normal
If \(P(X < x) = p\), find \(z\) with \(\Phi(z) = p\), then \(x = \mu + z\sigma\). If \(p < 0.5\), \(z\) is **negative**: use \(z = -\Phi^{-1}(1 - p)\). Common values: \(\Phi^{-1}(0.9) = 1.2816\), \(\Phi^{-1}(0.95) = 1.6449\), \(\Phi^{-1}(0.975) = 1.9600\).
:::

:::eg \(X \sim N(50, 8^2)\). Find \(k\) such that \(P(X < k) = 0.9\). Then find \(\sigma\) if \(Y \sim N(100, \sigma^2)\) and \(P(Y > 110) = 0.05\).
\(\Phi(z) = 0.9\) gives \(z = 1.2816\), so \(k = 50 + 1.2816\times 8 = 60.3\).
For \(Y\): \(P(Y > 110) = 0.05\), so \(P(Y < 110) = 0.95\) and \(z = 1.6449\). So \(\dfrac{110 - 100}{\sigma} = 1.6449\), giving \(\sigma = \dfrac{10}{1.6449} = 6.08\).
:::

## Finding the mean and the standard deviation

When both \(\mu\) and \(\sigma\) are unknown, two probabilities give two equations. Standardise each and solve the pair simultaneously. You must show the standardising (each \(z\)-value), not only the final answer.

:::eg (Exam style) The random variable \(X \sim N(\mu, \sigma^2)\). It is given that \(P(X < 30) = 0.2\) and \(P(X > 50) = 0.1\). Find \(\mu\) and \(\sigma\). [6 marks]
\(P(X < 30) = 0.2\) gives \(\dfrac{30 - \mu}{\sigma} = -0.8416\). [M1 A1]
\(P(X > 50) = 0.1\) means \(P(X < 50) = 0.9\), so \(\dfrac{50 - \mu}{\sigma} = 1.2816\). [M1 A1]
Subtract the first equation from the second: \(\dfrac{20}{\sigma} = 1.2816 + 0.8416 = 2.1232\), so \(\sigma = 9.42\). [M1]
Then \(\mu = 30 + 0.8416\times 9.42 = 37.9\). [A1]
Check: \(50 - 37.9 = 12.1\) and \(12.1/9.42 = 1.28\) ✓.
:::

:::warn Common slips
Use \(\sigma\), not \(\sigma^2\), when standardising: if the variance is given as 64, divide by 8. Never put a negative in front of a standard deviation. For a "more than" probability, subtract from 1 first. When \(p < 0.5\), the \(z\)-value is negative; a positive \(z\) there gives an answer above the mean instead of below.
:::

## Normal approximation to the binomial

A binomial distribution with large \(n\) is awkward to calculate directly, but it looks like a bell. If \(X \sim B(n, p)\) with \(np > 5\) and \(nq > 5\), then approximately
\[X \approx Y \sim N(np,\ npq)\]
Because \(X\) is **discrete** and \(Y\) is continuous, apply a **continuity correction**: treat the whole number \(r\) as the interval from \(r - 0.5\) to \(r + 0.5\).

| Binomial probability | Normal probability |
|---|---|
| \(P(X \le r)\) | \(P(Y < r + 0.5)\) |
| \(P(X < r)\) | \(P(Y < r - 0.5)\) |
| \(P(X \ge r)\) | \(P(Y > r - 0.5)\) |
| \(P(X > r)\) | \(P(Y > r + 0.5)\) |
| \(P(X = r)\) | \(P(r - 0.5 < Y < r + 0.5)\) |

:::eg \(X \sim B(40, 0.3)\). Use a normal approximation to find \(P(X \le 15)\) and \(P(X = 10)\). Compare with the exact values.
\(np = 12 > 5\) and \(nq = 28 > 5\), so use \(Y \sim N(12, 8.4)\), with \(\sigma = \sqrt{8.4} = 2.898\).
\(P(X \le 15) \approx P(Y < 15.5)\); \(z = \dfrac{15.5 - 12}{2.898} = 1.208\), so the probability is \(\Phi(1.208) = 0.886\). The exact binomial value is \(0.885\).
\(P(X = 10) \approx P(9.5 < Y < 10.5)\); \(z\)-values \(-0.863\) and \(-0.518\), so \(\Phi(-0.518) - \Phi(-0.863) = 0.108\). The exact value is \(0.113\).
The approximation is good for probabilities near the middle of the distribution.
:::

:::eg (Exam style) A drug cures a patient with probability 0.4. It is given to 80 patients independently. Use a normal approximation to find the probability that at least 36 are cured. [5 marks]
\(X \sim B(80, 0.4)\). \(np = 32\) and \(nq = 48\), both greater than 5, so \(X \approx Y \sim N(32, 19.2)\). [B1 B1]
\(P(X \ge 36) \approx P(Y > 35.5)\) (continuity correction). [M1]
\(z = \dfrac{35.5 - 32}{\sqrt{19.2}} = \dfrac{3.5}{4.382} = 0.799\). [M1]
\(P(Z > 0.799) = 1 - \Phi(0.799) = 0.212\). [A1]
:::

:::exam What earns marks
- **Sketch** the curve with the shaded area and the \(z\)-values; the picture shows whether to subtract from 1.
- **Show the standardising** line: \(z = \dfrac{x - \mu}{\sigma}\) with the numbers, before the table value.
- **Inverse problems**: state the \(z\)-value (with sign) before forming the equation. For two unknowns, write both equations, then eliminate.
- **Approximation**: state the conditions \(np > 5\), \(nq > 5\), the distribution \(N(np, npq)\), and the continuity-corrected inequality.
- The variance is \(\sigma^2\): do not forget to take the square root. Give final answers to 3 significant figures.
:::

:::board Other boards
Edexcel IAL S1 and the UK A Level courses (AQA, OCR, Edexcel) also cover the normal distribution, standardising and the inverse problem. Cambridge Paper 5 gives you a normal table in the exam, so you work by standardising and reading the table. If your board lets you use the normal function on a calculator, the method (sketch, \(z\)-values, conclusion) is the same.
:::

:::try Start easy, finish at exam standard
Q: \(X \sim N(65, 5^2)\). Find \(P(X > 72)\), \(P(X < 60)\) and \(P(60 < X < 72)\).
A: \(P(X > 72) = 1 - \Phi(1.4) = 0.0808\). \(P(X < 60) = \Phi(-1) = 0.159\). \(P(60 < X < 72) = \Phi(1.4) - \Phi(-1) = 0.9192 - 0.1587 = 0.761\).
Q: \(X \sim N(24, 4^2)\). Find \(P(X > 30)\).
A: \(z = \dfrac{30 - 24}{4} = 1.5\), so \(P = 1 - \Phi(1.5) = 0.0668\).
Q: \(X \sim N(70, 12^2)\). Find the lower quartile of \(X\).
A: \(\Phi(z) = 0.25\) gives \(z = -0.6745\). The lower quartile is \(70 - 0.6745\times 12 = 61.9\).
Q: Find \(a\) with \(\Phi(a) = 0.1\), and \(b\) with \(\Phi(b) = 0.7\).
A: \(a = -1.2816\) and \(b = 0.5244\).
Q: \(X \sim N(\mu, 6^2)\) and \(P(X < 40) = 0.0668\). Find \(\mu\).
A: \(z = -1.5\), so \(\dfrac{40 - \mu}{6} = -1.5\) and \(\mu = 49.0\).
Q: \(X \sim N(\mu, \sigma^2)\) with \(P(X < 20) = 0.1\) and \(P(X > 30) = 0.2\). Find \(\mu\) and \(\sigma\).
A: \(\dfrac{20 - \mu}{\sigma} = -1.2816\) and \(\dfrac{30 - \mu}{\sigma} = 0.8416\). Subtract: \(\dfrac{10}{\sigma} = 2.1232\), so \(\sigma = 4.71\) and \(\mu = 20 + 1.2816\times 4.71 = 26.0\).
Q: \(X \sim B(50, 0.4)\). Use a normal approximation to find \(P(X \le 24)\).
A: \(np = 20\), \(npq = 12\), so \(Y \sim N(20, 12)\). \(P(Y < 24.5)\): \(z = \dfrac{4.5}{3.464} = 1.299\), so \(P = 0.903\).
Q: \(X \sim B(60, 0.5)\). Use a normal approximation to find \(P(X > 35)\).
A: \(Y \sim N(30, 15)\). \(P(Y > 35.5)\): \(z = \dfrac{5.5}{3.873} = 1.420\), so \(P = 1 - \Phi(1.420) = 0.0778\).
Q: (Exam style) Heights of adult men in a town are normally distributed with mean 172 cm. 15% of men are taller than 180 cm. Find the standard deviation, and then the proportion of men shorter than 165 cm. [6 marks]
A: \(P(X < 180) = 0.85\) so \(z = 1.0364\). [M1 A1] \(\dfrac{180 - 172}{\sigma} = 1.0364\), so \(\sigma = 7.72\). [M1 A1] \(z = \dfrac{165 - 172}{7.72} = -0.907\), so \(P(X < 165) = \Phi(-0.907) = 0.182\), about 18.2%. [M1 A1]
:::

:::quiz
? \(X \sim N(50, 16)\). What is the standard deviation?
- 16
+ 4
- 8
- 256
> The second parameter is the variance, 16, so the standard deviation is \(\sqrt{16} = 4\).
? \(Z \sim N(0, 1)\) and \(\Phi(1.5) = 0.9332\). What is \(P(Z < -1.5)\)?
- \(0.9332\)
+ \(0.0668\)
- \(-0.9332\)
- \(0.4668\)
> By symmetry \(\Phi(-1.5) = 1 - \Phi(1.5) = 0.0668\). A probability can never be negative.
? You are told \(P(X < k) = 0.2\) for a normal \(X\). The \(z\)-value for \(k\) is:
- positive, about 0.8416
+ negative, about \(-0.8416\)
- exactly 0
- 0.2
> A probability below 0.5 puts \(k\) below the mean, so \(z\) is negative.
? \(X \sim B(100, 0.3)\) is approximated by a normal \(Y\). Which is the correct continuity correction for \(P(X \ge 35)\)?
- \(P(Y > 35.5)\)
+ \(P(Y > 34.5)\)
- \(P(Y > 35)\)
- \(P(Y < 34.5)\)
> \(X \ge 35\) includes 35, which covers the interval from 34.5 upwards, so use \(Y > 34.5\).
? Which conditions allow a normal approximation to \(B(n, p)\)?
- \(n > 5\)
- \(p < 0.5\)
+ \(np > 5\) and \(nq > 5\)
- \(n > 100\)
> The normal approximation works when both the expected number of successes and the expected number of failures are greater than 5.
:::

:::recap
- \(X \sim N(\mu, \sigma^2)\): symmetric bell, mean \(\mu\), standard deviation \(\sigma\). Areas are probabilities; \(P(X = a) = 0\).
- Standardise: \(Z = \dfrac{X - \mu}{\sigma} \sim N(0, 1)\). Use \(\Phi(-z) = 1 - \Phi(z)\); sketch to decide what to subtract.
- Inverse: find \(z\) from \(\Phi(z) = p\) (negative for \(p < 0.5\)), then \(x = \mu + z\sigma\).
- Two unknowns: standardise both probabilities and solve the two equations simultaneously.
- Approximating \(B(n, p)\): need \(np > 5\) and \(nq > 5\); use \(N(np, npq)\) with a continuity correction \(\pm 0.5\).
:::

:::links
- watch: [Normal distribution probabilities](https://www.examsolutions.net/tutorials/probability-normal-distribution/) · ExamSolutions · standardising and using the table
- watch: [Normal approximation to the binomial](https://www.examsolutions.net/tutorials/normal-approximation-binomial-distribution/) · ExamSolutions · the continuity correction in action
- watch: [Why π is in the normal distribution](https://www.3blue1brown.com/lessons/gaussian-integral) · 3Blue1Brown · for the curious: the shape of the bell curve
- practise: [CAIE S1 normal distribution exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/statistical-distributions/normal-distribution/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Probability distributions](https://seeing-theory.brown.edu/probability-distributions/index.html) · Seeing Theory · change μ and σ and watch the curve
- papers: [9709 Paper 5 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-6/) · Physics & Maths Tutor · their page "cie-paper-6" holds Paper 5 [unofficial]

Links checked 3 October 2026.
:::
Next: [The Poisson distribution](#math.s2.poisson).
