@chapter math.exam.p5
@title Paper 5 survival guide
@level guide
@paper CAIE 9709 Paper 5 · Edexcel IAL S1 and S2 · UK Statistics
@time 1 hour
@summary Cambridge Paper 5 (Probability and Statistics 1): length, marks, a timing plan, what MF19 and the normal tables give you and what you must learn, a topic list with chapters, the marks students lose most often, and a final-week checklist.

:::why
Paper 5 is the statistics paper that every AS student can take, and it is the base for Paper 6. It rewards precise reading: whether events are independent, which probability a question wants, which distribution models a situation. This guide shows where marks are won and lost.
:::

## The paper at a glance

| Fact | Paper 5 |
|---|---|
| Name | Probability and Statistics 1 |
| Time | 1 hour 15 minutes |
| Marks | 50 |
| Weighting | 40% of an AS (with P1), 20% of an A Level |
| Used in | AS route P1 + P5; both A Level routes (1 and 2) |
| Tools | scientific calculator, ruler, MF19 including the normal distribution tables |
| Accuracy | 3 s.f. unless the question says otherwise; probabilities to 3 s.f. |

Paper 5 assumes Paper 1 algebra. Probability uses the notation \(P(A)\), \(P(A \cup B)\), \(P(A \cap B)\), \(P(A \mid B)\) and \(A'\). Knowledge (AO1) is 55% of the marks and application (AO2) is 45%.

## A timing plan

The paper gives 75 minutes for 50 marks: **1.5 minutes per mark**. Aim for **1.3 minutes per mark**: 65 minutes of work, with about 10 minutes to check. Statistics questions often have a short setup and a long chain of parts, so read the whole setup before the first part, and define your distribution in words and symbols once (for example, "\(X \sim B(10, 0.3)\)") so that every later part is quick.

## Formulas and tables: what you are given and what you must learn

**MF19 gives you:** the mean and standard deviation (ungrouped and grouped); \(E(X)\) and \(\mathrm{Var}(X)\); the binomial and geometric probability formulae with their means and variances; and the **normal distribution tables**.

**You must learn:**

| Topic | What to know |
|---|---|
| Probability | \(P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}\); independence means \(P(A \cap B) = P(A) \times P(B)\); the addition rule |
| Counting | \(n!\), \(\binom{n}{r}\), arrangements with repeats and restrictions (together, not together) |
| Normal distribution | standardisation \(z = \dfrac{x - \mu}{\sigma}\); how to read the tables; the **continuity correction** for the binomial |
| Approximation | the binomial is approximately normal when \(np > 5\) and \(nq > 5\) |
| Data | the median and quartiles from a cumulative frequency graph; coded data \(\Sigma(x - a)\), \(\Sigma(x - a)^2\) |

:::exam Show the standardisation
For the normal distribution the syllabus asks for **full standardisation** to be shown: write \(z = \dfrac{x - \mu}{\sigma}\) with the numbers in, then the probability from the tables. The calculator's normal function can check your answer, but the line with \(z\) in it earns the method mark. See [Your calculator](#math.calc) for how to use the distribution keys as a check.
:::

## Topic list

| Topic | Chapter | Know cold |
|---|---|---|
| Representation of data | [Data](#math.s1.data) | choosing a diagram, comparing with mean, median, IQR and standard deviation, coded data |
| Permutations and combinations | [Permutations and combinations](#math.s1.perms) | arrangements with repeats, restrictions, selections |
| Probability | [Probability](#math.s1.prob) | tree diagrams, conditional probability, independent and exclusive events |
| Discrete random variables | [Discrete random variables](#math.s1.drv) | tables, \(E(X)\), \(\mathrm{Var}(X)\), binomial, geometric |
| The normal distribution | [The normal distribution](#math.s1.normal) | standardise, inverse problems, approximating the binomial |

## The marks students lose most often

- **Data:** quartiles by an unclear method; ignoring an outlier question's definition; comparing two data sets without using a measure of both average **and** spread, and without context.
- **Counting:** mixing up permutations and combinations: if order matters, it is a permutation; for "together", treat the group as one item and then arrange within it.
- **Probability:** treating "mutually exclusive" as "independent" (two non-zero-probability exclusive events are never independent); not writing \(P(A \mid B)\) as a fraction with the right denominator.
- **Random variables:** forgetting that the probabilities must sum to 1 and using that to find an unknown; subtracting \([E(X)]^2\) incorrectly for the variance.
- **Binomial and geometric:** not stating the conditions (fixed \(n\), two outcomes, independent trials, constant \(p\)); "at least" mis-handled: \(P(X \ge 3) = 1 - P(X \le 2)\).
- **Normal:** standardising with the variance instead of the standard deviation (for \(N(50, 64)\), divide by 8); a negative \(z\) written as a negative probability; no continuity correction.

:::warn Where the A marks go
In the normal distribution, a "wrong \(\sigma\)" often costs every later mark in that question. Write the line "\(\sigma = \sqrt{64} = 8\)" the moment you see a variance.
:::

## Final week

:::checklist Final week
- [ ] I have done at least two full timed Paper 5 papers in the last 14 days and marked them
- [ ] I can find the mean, standard deviation and quartiles, from raw, grouped and coded data
- [ ] I can compare two data sets in context using a measure of average and a measure of spread
- [ ] I can count arrangements and selections, including repeats and "together" or "not together"
- [ ] I can draw a tree diagram and find a conditional probability
- [ ] I can test whether two events are independent using the multiplication rule
- [ ] I can build a probability distribution table and find \(E(X)\) and \(\mathrm{Var}(X)\)
- [ ] I can use the binomial and geometric distributions and state why they are suitable
- [ ] I can standardise, use the tables, and solve an inverse normal problem
- [ ] I can approximate a binomial by a normal with a continuity correction
:::

## Your progress on Paper 5

:::progress P5
:::

The full mock paper for this exam is [Mock paper: Probability and Statistics 1 (A)](#math.mock.p5a): take it as one sitting, timed, with your calculator and MF19. For short mixed questions across the whole paper, use [Mixed practice: Statistics 1](#math.mixed.stats1).

:::links
- papers: [9709 Paper 5 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-6/) · Physics & Maths Tutor · their page "cie-paper-6" holds Paper 5 [unofficial]

Links checked 3 October 2026.
:::

:::recap
- Paper 5: 1 h 15, 50 marks, 40% of an AS and 20% of an A Level; calculator, ruler, MF19 with normal tables.
- MF19 gives mean and SD, \(E(X)\), \(\mathrm{Var}(X)\), the binomial and geometric formulas and the tables; learn conditional probability, independence, counting, standardisation and the continuity correction.
- Show the standardisation, and divide by \(\sigma\), not \(\sigma^2\).
- Plan 1.3 minutes per mark; leave about 10 minutes to check.
- Most lost marks come from exclusive-versus-independent mix-ups, "at least" slips and a missing continuity correction.
:::

Next: [Paper 6 survival guide](#math.exam.p6)
