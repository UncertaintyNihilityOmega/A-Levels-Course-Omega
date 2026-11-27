@chapter math.fm.chisq
@title Chi-squared goodness of fit
@level fm
@paper CAIE 9231 Paper 4
@time 5–7 hours
@summary A goodness-of-fit test asks whether data could plausibly have come from a stated distribution. You will turn a hypothesis (uniform, given ratios, binomial, Poisson, geometric, normal or a given PDF) into expected frequencies, combine classes so each expected frequency is at least 5, calculate \(X^2 = \sum \dfrac{(O - E)^2}{E}\), find the degrees of freedom (reduced for every parameter estimated from the data), compare with the \(\chi^2\) table, and write a conclusion in context.

:::why
Every model in statistics is a claim: "this die is fair", "faults follow a binomial distribution", "calls arrive at random". A claim can be checked against what really happened, and the chi-squared test is the standard tool that measures, in one number, how far the counts you observed are from the counts the claim predicts. It is how a quality controller decides a process has drifted and how a scientist decides a theory fits, and it is the one test that works for any distribution you can write down.
:::

**Before you start**, you need the binomial and geometric distributions from [Discrete random variables: binomial and geometric](#math.s1.drv), the Poisson distribution from [The Poisson distribution](#math.s2.poisson), normal probabilities from [The normal distribution](#math.s1.normal), probabilities from a PDF from [Continuous random variables](#math.fm.crv), and the language of hypothesis tests (null and alternative hypothesis, significance level, critical value) from [Hypothesis testing](#math.s2.hypothesis). The table lookup works as it did for the \(t\) table in [The t-distribution: one-sample tests and intervals](#math.fm.inference).

:::try Warm-up
Q: \(X \sim \mathrm{B}(5, 0.2)\). Find \(P(X = 2)\). (from [Discrete random variables: binomial and geometric](#math.s1.drv))
A: \(P(X = 2) = \binom{5}{2}(0.2)^2(0.8)^3 = 10 \times 0.04 \times 0.512 = 0.2048\).
Q: \(X \sim \mathrm{Po}(2.2)\). Find \(P(X = 3)\) to 3 significant figures. (from [The Poisson distribution](#math.s2.poisson))
A: \(P(X = 3) = \dfrac{\mathrm{e}^{-2.2}\,2.2^3}{3!} = 0.1966\), so 0.197.
Q: \(X \sim \mathrm{N}(250, 4^2)\). Find \(P(X < 244)\). (from [The normal distribution](#math.s1.normal))
A: \(z = \dfrac{244 - 250}{4} = -1.5\), so \(P(X < 244) = \Phi(-1.5) = 0.0668\).
:::

## Observed and expected frequencies

Roll a die 120 times. If it is fair you expect each face about 20 times, but you will not see exactly 20 each time: chance alone makes the counts wobble. Suppose your counts are 15, 25, 22, 18, 24 and 16. Is that the ordinary wobble of a fair die, or does it point to a biased one? To answer, you need a number that measures the gap between what you saw and what the claim predicts, and a way to judge how big a gap is too big.

:::def Observed frequency
The number of observations that actually fall in a class, written \(O\). The observed frequencies add up to the total number of observations \(N\).
:::

:::def Expected frequency
The number of observations the hypothesised model predicts for a class, written \(E\). It equals \(N\) times the probability the model gives to that class, so it need not be a whole number. The expected frequencies also add up to \(N\).
:::

:::def Goodness-of-fit test
A hypothesis test of whether observed frequencies are consistent with the frequencies predicted by a stated distribution. The null hypothesis says the model fits; the alternative says it does not.
:::

The differences \(O - E\) are the natural starting point, but they always add to zero (both totals are \(N\)), so you square them. A gap of 5 matters a lot when you expect 10 and hardly at all when you expect 1000, so you also divide each squared gap by the expected frequency for its class.

:::key The test statistic
\[X^2 = \sum \frac{(O - E)^2}{E}\]
The sum runs over all classes. \(X^2 = 0\) means a perfect match, and the larger \(X^2\) is, the worse the fit. An equivalent form, quicker with a calculator when the \(E\) values are exact, is
\[X^2 = \sum \frac{O^2}{E} - N\]
:::

Many books write the statistic as \(\chi^2\) (Greek chi, squared). In this chapter the statistic calculated from data is \(X^2\), and \(\chi^2_\nu\) names the distribution it is compared with.

:::proof Why the two forms of the statistic agree
Expand the square in each term and sum:
\[\begin{aligned}
\sum \frac{(O - E)^2}{E} &= \sum \frac{O^2 - 2OE + E^2}{E} \\
&= \sum \frac{O^2}{E} - 2\sum O + \sum E
\end{aligned}\]
Here \(\sum O = N\) because the observed frequencies add to the total, and \(\sum E = N\) because the expected frequencies do too. So the right-hand side is \(\sum \dfrac{O^2}{E} - 2N + N = \sum \dfrac{O^2}{E} - N\). The identity needs \(\sum E = N\) exactly, so do not use it with rounded \(E\) values that no longer add to \(N\).
:::

### How big is too big?

If the model is right, \(X^2\) is not zero: chance alone gives a positive value every time. What matters is how likely a value as large as yours is. Provided the expected frequencies are not too small, the statistic then follows (approximately) a **chi-squared distribution**, written \(\chi^2_\nu\), where \(\nu\) (Greek nu) is the number of **degrees of freedom**. It is a continuous distribution on \(x \ge 0\) with a long tail to the right, and its mean is \(\nu\). The picture shows how its shape depends on \(\nu\).

:::plot The density of \(\chi^2_\nu\) for \(\nu = 2\) and \(\nu = 6\). Both curves live on \(x \ge 0\) and have a tail on the right. For \(\nu = 2\) the curve falls from the start, and for \(\nu = 6\) the peak has moved right, to \(x = 4\).
--f "exp(-x/2)/2" --f "x**2*exp(-x/2)/16" --label "ν = 2" --label "ν = 6" --x 0 16 --y 0 0.6 --legend tr
:::

A badly fitting model makes \(X^2\) large, so the test is **one-tailed, in the upper tail**: you reject the model only when \(X^2\) is bigger than a critical value. The MF19 table of the \(\chi^2\) distribution gives, for each \(\nu\), the value \(x\) with \(P(W \le x) = p\), where \(W\) stands for any variable with the \(\chi^2_\nu\) distribution (it is a different letter from the data variable \(X\) and from the statistic \(X^2\)). For a test at the 5% level you want 5% in the upper tail, so you read the column \(p = 0.95\). The columns you can use for a test at each level are in the next box.

:::key Reading the \(\chi^2\) table
The table prints the value \(x\) with \(P(W \le x) = p\), for \(W \sim \chi^2_\nu\), for nine values of \(p\) (0.01, 0.025, 0.05, 0.9, 0.95, 0.975, 0.99, 0.995 and 0.999) and for \(\nu = 1\) to 25, then 30, 40, 50 and so on up to 100.

| Significance level (upper tail) | Column \(p\) |
|---|---|
| 10% | 0.9 |
| 5% | 0.95 |
| 2.5% | 0.975 |
| 1% | 0.99 |
| 0.5% | 0.995 |
| 0.1% | 0.999 |

Reject \(H_0\) when \(X^2 >\) the critical value.
:::

The columns \(p = 0.01\), 0.025 and 0.05 are lower-tail values. They matter only if you wonder whether a fit is suspiciously good; the syllabus asks you to use the upper tail.

Here are the values you will meet most often, so you can check your reading of the table.

| \(\nu\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 5% (\(p = 0.95\)) | 3.841 | 5.991 | 7.815 | 9.488 | 11.070 | 12.592 | 14.067 | 15.507 |
| 1% (\(p = 0.99\)) | 6.635 | 9.210 | 11.345 | 13.277 | 15.086 | 16.812 | 18.475 | 20.090 |

:::plot The 5% critical region of \(\chi^2_4\): the shaded area to the right of 9.488 has probability 0.05. A statistic that lands in it is unusually large for a model that fits.
--f "x*exp(-x/2)/4" --label "ν = 4" --x 0 16 --y 0 0.25 --shade "0,9.488,16" --vline 9.488 --pt "9.488,0.0206,critical value 9.488@ne" --legend tr
:::

Try the widget below. Set \(\nu = 5\) and the level to 5%, then type a statistic: 4.5 (the die from the start of the chapter) falls well short of the critical value, while 12 would be in the critical region. Then raise \(\nu\) and notice that the critical value grows, and that the curve peaks further right.

:::html
<div class="widget" data-w="fm-chisq" data-v="5" data-alpha="0.05" data-x2="4.5"></div>
:::

## The procedure and degrees of freedom

Every goodness-of-fit question follows the same route, and mark schemes give a mark at almost every step.

:::steps
1. State the hypotheses in words: \(H_0\): the data follow the stated distribution; \(H_1\): they do not.
2. Find each expected frequency, \(E = N \times P(\text{class})\), from the model.
3. Combine classes (adjacent ones) until every \(E\) is at least 5.
4. Calculate \(X^2 = \sum \dfrac{(O - E)^2}{E}\) over the combined classes.
5. Find \(\nu = n - 1 - k\), where \(n\) is the number of classes after combining and \(k\) is the number of parameters estimated from the data.
6. Read the upper-tail critical value for \(\nu\) at the given level.
7. Compare, and write a conclusion in the context of the question.
:::

:::def Degrees of freedom
The number of class frequencies that can vary freely. For a goodness-of-fit test, \(\nu = n - 1 - k\) for \(n\) classes and \(k\) parameters estimated from the data.
:::

Why subtract 1? Because the expected frequencies are built to add to \(N\), the observed ones are not free: once you know \(n - 1\) of them, the last is \(N\) minus the rest. Why subtract one more for each estimated parameter? Because estimating (say) \(p\) from the data forces the fitted model to be as close to the data as it can be in that one respect, so the fit looks better than it should and there is one fewer way for the counts to differ.

:::key Degrees of freedom for common models
\(n\) is the number of classes after combining.

| Model, with its parameters | Estimated from the data | \(\nu\) |
|---|---|---|
| uniform, given ratios, given probabilities or PDF | none | \(n - 1\) |
| binomial \(\mathrm{B}(m, p)\), \(p\) given | none | \(n - 1\) |
| binomial \(\mathrm{B}(m, p)\), \(p\) estimated | \(p\) | \(n - 2\) |
| Poisson or geometric, parameter given | none | \(n - 1\) |
| Poisson or geometric, parameter estimated (the mean) | one | \(n - 2\) |
| normal, \(\mu\) and \(\sigma\) given | none | \(n - 1\) |
| normal, \(\mu\) and \(\sigma\) both estimated | two | \(n - 3\) |
:::

The key phrase in a question is "estimated from the data" (or "using the sample mean"). A value that the hypothesis states, such as "the probability of a fault is 0.2", or that comes from a different source, costs no degrees of freedom.

### The rule of 5

The chi-squared distribution is only an approximation to the true distribution of \(X^2\), and a poor one when some expected frequencies are tiny: a class with \(E = 0.3\) that happens to catch one observation contributes \(\dfrac{(1 - 0.3)^2}{0.3} = 1.63\) all by itself. The syllabus rule is that every expected frequency must be at least 5, which you achieve by combining classes.

- Combine **adjacent** classes, normally at a tail. Classes such as "0", "1", "2" and "3 or more" merge from the end. Do not merge the first class with the last.
- Combine **before** you calculate \(X^2\): add the \(E\) values and add the \(O\) values of the merged classes, then use the merged classes.
- Combine only as much as you need. A class with \(E = 5.04\) stays alone. But if the small classes at the end of the table still add up to less than 5, they must all join the next class in, however large it is (see the two binomial examples below).
- \(\nu\) uses the **new** number of classes.

:::warn The three lost marks that come up again and again
(1) Calculating \(\dfrac{(O - E)^2}{E}\) for the small classes and combining afterwards: you must merge first, then calculate. (2) Using \(\nu = n - 1\) when a parameter was estimated from the data. (3) Rounding expected frequencies early: keep full calculator values, or at least 3 decimal places, and check they still add to \(N\).
:::

## Fitting a model: from hypothesis to expected frequencies

The skill of turning a hypothesis into expected frequencies is the heart of every goodness-of-fit question. Whatever the model, the recipe is: list the classes, find the probability of each class under \(H_0\), and multiply by \(N\). The last class is often open-ended ("6 or more"), and its probability is \(1 - \) (the sum of the others), which also makes the expected frequencies add up to \(N\) automatically.

### A uniform distribution and given ratios

For a fair die, a fair spinner or "all days equally likely", every class has probability \(\dfrac1n\), so \(E = \dfrac{N}{n}\). For a hypothesis stated as a ratio, such as 9 : 3 : 3 : 1, the probabilities are the shares of the ratio, \(\dfrac{9}{16}, \dfrac{3}{16}, \dfrac{3}{16}, \dfrac{1}{16}\).

:::eg The die at the start of the chapter was rolled 120 times. The frequencies of 1 to 6 were 15, 25, 22, 18, 24 and 16. Test, at the 5% significance level, whether the die is fair.
\(H_0\): the die is fair (the six faces are equally likely). \(H_1\): the die is not fair.

If the die is fair, each face has probability \(\tfrac16\), so every expected frequency is \(120 \times \tfrac16 = 20 \geq 5\). No class needs combining.

| Face | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| \(O\) | 15 | 25 | 22 | 18 | 24 | 16 |
| \(E\) | 20 | 20 | 20 | 20 | 20 | 20 |
| \((O - E)^2\) | 25 | 25 | 4 | 4 | 16 | 16 |

\[X^2 = \frac{25 + 25 + 4 + 4 + 16 + 16}{20} = \frac{90}{20} = 4.5\]
There are 6 classes and no parameter was estimated, so \(\nu = 6 - 1 = 5\). The critical value for 5% is 11.070. Since \(4.5 < 11.070\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the die is biased.

**Check** with the other form:
\[\sum \frac{O^2}{E} - N = \frac{225 + 625 + 484 + 324 + 576 + 256}{20} - 120 = 124.5 - 120 = 4.5\]
:::

Do not read "do not reject" as "the die is fair". The data are consistent with a fair die; a small bias might simply be hidden by the sample size.

:::eg A gardener crosses two kinds of sweet pea. A genetic model predicts four plant types in the ratio 9 : 3 : 3 : 1. Of 320 plants, 160, 84, 52 and 24 are of the four types. Test at the 5% level whether the model fits, and say which type is most responsible for the result.
\(H_0\): the plant types occur in the ratio 9 : 3 : 3 : 1. \(H_1\): they do not.

Under \(H_0\) the probabilities are \(\tfrac{9}{16}\), \(\tfrac{3}{16}\), \(\tfrac{3}{16}\), \(\tfrac{1}{16}\), so the expected frequencies are \(180\), \(60\), \(60\) and \(20\), all at least 5.

| Type | A | B | C | D |
|---|---|---|---|---|
| \(O\) | 160 | 84 | 52 | 24 |
| \(E\) | 180 | 60 | 60 | 20 |
| \(\dfrac{(O - E)^2}{E}\) | 2.222 | 9.600 | 1.067 | 0.800 |

\[X^2 = 2.222 + 9.600 + 1.067 + 0.800 = 13.69\]
\(\nu = 4 - 1 = 3\), and the 5% critical value is 7.815. Since \(13.69 > 7.815\), reject \(H_0\): there is sufficient evidence, at the 5% level, that the plant types do not occur in the ratio 9 : 3 : 3 : 1.

Type B contributes 9.600, over two thirds of \(X^2\). There are 84 plants of type B where the model expects 60, so the model underestimates how common that type is. The result is also significant at the 1% level, because 13.69 is above 11.345.
:::

## The binomial distribution

For a hypothesis \(X \sim \mathrm{B}(m, p)\), the classes are the values \(0, 1, 2, \dots, m\), and \(E_r = N\binom{m}{r}p^r(1 - p)^{m - r}\). The probability \(p\) is either **given** by the hypothesis (then \(\nu = n - 1\)) or **estimated from the data** (then \(\nu = n - 2\)). When you have to estimate it, the number of trials \(m\) is fixed by the situation and \(p\) comes from the mean:
\[\hat p = \frac{\text{sample mean}}{m} = \frac{\sum x f}{m\,N}\]
because \(E(X) = mp\). The hat means "estimate of".

:::eg A supplier claims that each item it makes is faulty with probability 0.2, independently. A buyer inspects 200 packs of 5 items and records the number of faulty items in each: 60 packs had 0, 88 had 1, 40 had 2, 10 had 3, 2 had 4 and none had 5. Test whether \(\mathrm{B}(5, 0.2)\) fits, at the 5% level.
\(H_0\): the number of faulty items in a pack follows \(\mathrm{B}(5, 0.2)\). \(H_1\): it does not.

\(E_r = 200\binom{5}{r}(0.2)^r(0.8)^{5-r}\):

| Faulty | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| \(O\) | 60 | 88 | 40 | 10 | 2 | 0 |
| \(E\) | 65.536 | 81.92 | 40.96 | 10.24 | 1.28 | 0.064 |

The last three \(E\) values are 10.24, 1.28 and 0.064, so combine classes 3, 4 and 5 into "3 or more". Classes 4 and 5 together give only \(1.28 + 0.064 = 1.344\), still below 5, so they must join class 3 even though its own \(E = 10.24\) is above 5. Then \(E = 10.24 + 1.28 + 0.064 = 11.584\) and \(O = 10 + 2 + 0 = 12\). That leaves four classes.

| Faulty | 0 | 1 | 2 | 3 or more |
|---|---|---|---|---|
| \(O\) | 60 | 88 | 40 | 12 |
| \(E\) | 65.536 | 81.92 | 40.96 | 11.584 |
| \(\dfrac{(O - E)^2}{E}\) | 0.4676 | 0.4512 | 0.0225 | 0.0149 |

\[X^2 = 0.4676 + 0.4512 + 0.0225 + 0.0149 = 0.956\]
The probability 0.2 was given, so \(\nu = 4 - 1 = 3\), and the critical value is 7.815. Since \(0.956 < 7.815\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the number of faulty items does not follow \(\mathrm{B}(5, 0.2)\).
:::

When \(p\) is estimated, there is one more step at the start. Here is a full exam-style question in that shape: the expected frequencies are partly given, one is to be shown, classes are combined, and the model is criticised.

:::eg (Exam style) A factory packs components in boxes of 6. The number \(X\) of faulty components in each of 200 boxes is recorded.

| \(x\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Frequency | 55 | 62 | 41 | 26 | 10 | 5 | 1 |

A manager suggests that \(X \sim \mathrm{B}(6, p)\). (a) Show that the data give an estimate \(p = 0.244\) (3 s.f.). (b) With this estimate, the expected frequencies for \(x = 0, 1, 3, 4, 5, 6\), to 2 decimal places, are 37.29, 72.28, 25.14, 6.09, 0.79 and 0.04. Show that the expected frequency for \(x = 2\) is 58.37. (c) Test at the 5% level whether \(\mathrm{B}(6, p)\) is a suitable model. (d) Give one reason, in context, why the binomial model may not be appropriate.
**(a)** The sample mean is
\[\bar x = \frac{0 \times 55 + 1 \times 62 + 2 \times 41 + 3 \times 26 + 4 \times 10 + 5 \times 5 + 6 \times 1}{200} = \frac{293}{200} = 1.465\] [M1]
Since \(E(X) = 6p\), \(\hat p = \dfrac{1.465}{6} = 0.2442\), which is 0.244 to 3 s.f. [A1]

**(b)**
\[E_2 = 200 \times \binom{6}{2}\,\hat p^2(1 - \hat p)^4\] [M1]
\[= 200 \times 15 \times \left(\frac{1.465}{6}\right)^2\left(1 - \frac{1.465}{6}\right)^4 = 58.37\] [A1]
Use the unrounded \(\hat p = \dfrac{1.465}{6}\): the rounded 0.2442 would give 58.38. The 2 d.p. values add to 200.00, which is a good check.

**(c)** \(H_0\): the number of faulty components in a box follows \(\mathrm{B}(6, p)\). \(H_1\): it does not. [B1]

The expected frequencies for 4, 5 and 6 faulty components are 6.09, 0.79 and 0.04. The last two are below 5, and together they give only \(0.79 + 0.04 = 0.83\), still below 5, so they must join class 4 even though \(6.09\) is above 5 on its own. Combine classes 4, 5 and 6: \(E = 6.92\) and \(O = 10 + 5 + 1 = 16\).

| \(x\) | 0 | 1 | 2 | 3 | 4 or more |
|---|---|---|---|---|---|
| \(O\) | 55 | 62 | 41 | 26 | 16 |
| \(E\) | 37.29 | 72.28 | 58.37 | 25.14 | 6.92 |

\[X^2 = \frac{(55 - 37.29)^2}{37.29} + \frac{(62 - 72.28)^2}{72.28} + \dots + \frac{(16 - 6.92)^2}{6.92}\] [M1]
\[= 8.41 + 1.46 + 5.17 + 0.03 + 11.91 = 27.0\] [A1]
There are 5 classes and \(p\) was estimated, so \(\nu = 5 - 1 - 1 = 3\). The 5% critical value is 7.815.

Since \(27.0 > 7.815\), reject \(H_0\): there is sufficient evidence, at the 5% level, that the number of faulty components does not follow a binomial distribution. [M1 A1]

**(d)** Components made one after another on the same machine may share a fault, so whether they are faulty may not be independent. Equally, the probability of a fault may differ from box to box (for example between shifts). [B1]

The data say the same thing: there are more boxes with no faulty components (55 against 37.29) and more with four or more (16 against 6.92) than the model expects, which is what a probability that varies from box to box would produce.
:::

## The Poisson and geometric distributions

For \(X \sim \mathrm{Po}(\lambda)\), the classes are \(0, 1, 2, \dots\), with a last class "\(r\) or more". The parameter \(\lambda\) is the mean of \(X\), so when it is estimated you use the sample mean \(\bar x\), and \(\nu = n - 2\). If the data table ends in an open class such as "6 or more", the question has to give you the mean (or the individual values), because you cannot calculate it from the table alone.

\[E_r = N\,\frac{\mathrm{e}^{-\lambda}\lambda^r}{r!} \qquad \text{last class: } E = N - \sum (\text{the other } E)\]

:::eg (Exam style) A call centre records the number of calls received in each of 100 five-minute intervals.

| Calls | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Intervals | 20 | 22 | 20 | 14 | 10 | 8 | 6 |

No interval had more than 6 calls. (a) Show that the mean number of calls is 2.2. (b) A manager suggests that the number of calls follows a Poisson distribution. Using the mean found in (a) as the estimate of \(\lambda\), test this at the 5% level. (c) Calculate the variance of the data and use it to say why the Poisson model is not suitable.
**(a)**
\[\bar x = \frac{0 + 22 + 40 + 42 + 40 + 40 + 36}{100} = \frac{220}{100} = 2.2\] [M1 A1]

**(b)** \(H_0\): the number of calls follows a Poisson distribution (with \(\lambda\) estimated by 2.2). \(H_1\): it does not. [B1]

\(E_r = 100 \times \dfrac{\mathrm{e}^{-2.2}\,2.2^r}{r!}\), and the last class ("6 or more") is \(N\) minus the others:

| Calls | 0 | 1 | 2 | 3 | 4 | 5 | 6 or more |
|---|---|---|---|---|---|---|---|
| \(E\) | 11.08 | 24.38 | 26.81 | 19.66 | 10.82 | 4.76 | 2.49 |

Classes 5 and "6 or more" have \(E < 5\), so combine them: \(O = 8 + 6 = 14\) and \(E = 4.76 + 2.49 = 7.25\). [M1 A1]

\[\begin{aligned}
X^2 &= \frac{(20 - 11.08)^2}{11.08} + \frac{(22 - 24.38)^2}{24.38} + \frac{(20 - 26.81)^2}{26.81} \\
&\quad + \frac{(14 - 19.66)^2}{19.66} + \frac{(10 - 10.82)^2}{10.82} + \frac{(14 - 7.25)^2}{7.25}
\end{aligned}\] [M1]
\[= 7.18 + 0.23 + 1.73 + 1.63 + 0.06 + 6.29 = 17.1\] [A1]
There are 6 classes and \(\lambda\) was estimated from the data, so \(\nu = 6 - 1 - 1 = 4\). The critical value is 9.488. (If a question had instead stated \(\lambda = 2.2\) as part of the hypothesis, \(\nu\) would be \(6 - 1 = 5\), with critical value 11.070; the statistic is the same and the conclusion is the same here.)

Since \(17.1 > 9.488\), reject \(H_0\): there is sufficient evidence, at the 5% level, that the number of calls does not follow a Poisson distribution. [M1 A1]

**(c)** The variance is
\[\frac{0 + 22 + 80 + 126 + 160 + 200 + 216}{100} - 2.2^2 = 8.04 - 4.84 = 3.2\] [B1]
A Poisson distribution has variance equal to its mean, but 3.2 is well above 2.2. The calls are more spread out than a Poisson model allows: they may arrive in bursts, so they are not independent, or the rate may change through the day. [B1]
:::

The value of 17.1 comes mostly from the classes "0" (7.18) and "5 or more" (6.29): too many quiet intervals and too many busy ones, and too few of the middling kind. That pattern, a broad spread compared with the model, is how a changing rate shows up in a goodness-of-fit table.

The geometric distribution \(X \sim \mathrm{Geo}(p)\) counts the trials up to and including the first success: \(P(X = r) = (1 - p)^{r-1}p\) for \(r = 1, 2, 3, \dots\), and \(P(X \geq r) = (1 - p)^{r-1}\), which gives the probability of the open last class directly. Since \(E(X) = \dfrac1p\), an estimate from data is \(\hat p = \dfrac{1}{\bar x}\).

:::eg A basketball player shoots until she scores. She does this 100 times and records the number of shots needed each time. The 100 attempts needed 260 shots in all, and the frequencies of 1, 2, 3, 4, 5 and "6 or more" shots were 41, 22, 14, 11, 5 and 7. Test at the 5% level whether the number of shots follows a geometric distribution.
\(H_0\): the number of shots follows \(\mathrm{Geo}(p)\) for some \(p\). \(H_1\): it does not.

The sample mean is \(\bar x = \dfrac{260}{100} = 2.6\), so \(\hat p = \dfrac{1}{2.6} = \dfrac{5}{13} = 0.3846\) and \(1 - \hat p = \dfrac{8}{13}\).

\(E_r = 100\left(\tfrac{8}{13}\right)^{r-1}\tfrac{5}{13}\) for \(r = 1, \dots, 5\), and for "6 or more" \(E = 100\left(\tfrac{8}{13}\right)^5\):

| Shots | 1 | 2 | 3 | 4 | 5 | 6 or more |
|---|---|---|---|---|---|---|
| \(O\) | 41 | 22 | 14 | 11 | 5 | 7 |
| \(E\) | 38.46 | 23.67 | 14.57 | 8.96 | 5.52 | 8.83 |
| \(\dfrac{(O - E)^2}{E}\) | 0.168 | 0.118 | 0.022 | 0.463 | 0.048 | 0.378 |

All \(E\) values are at least 5, so nothing is combined. \(X^2 = 1.196\). There are 6 classes and \(p\) was estimated, so \(\nu = 6 - 2 = 4\); the critical value is 9.488. Since \(1.20 < 9.488\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the number of shots needed does not follow a geometric distribution.
:::

## Continuous distributions

A continuous variable has no natural classes, so the data arrive already grouped, with class boundaries. The probability of a class is the area under the PDF between its boundaries, found from \(\int f(x)\,\mathrm{d}x\) or from normal tables. The end classes are open ("less than 244", "256 or more"), so the whole real line is covered and the probabilities add to 1.

:::eg The masses of tins of beans are claimed to follow \(\mathrm{N}(250, 4^2)\) grams. The masses of 200 tins are grouped into five classes. Test at the 5% level whether the claim fits.

| Mass \(m\) (g) | \(m < 244\) | \(244 \leq m < 248\) | \(248 \leq m < 252\) | \(252 \leq m < 256\) | \(m \geq 256\) |
|---|---|---|---|---|---|
| \(O\) | 18 | 45 | 70 | 52 | 15 |

\(H_0\): the masses follow \(\mathrm{N}(250, 4^2)\). \(H_1\): they do not.

Standardise the boundaries with \(z = \dfrac{m - 250}{4}\): they become \(-1.5\), \(-0.5\), \(0.5\) and \(1.5\). The class probabilities are
\[\begin{aligned}
P(m < 244) &= \Phi(-1.5) = 0.0668 \\
P(244 \leq m < 248) &= \Phi(-0.5) - \Phi(-1.5) = 0.3085 - 0.0668 = 0.2417 \\
P(248 \leq m < 252) &= \Phi(0.5) - \Phi(-0.5) = 0.3829
\end{aligned}\]
and by symmetry the last two classes have probabilities 0.2417 and 0.0668. Multiply by 200:

| Class | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| \(O\) | 18 | 45 | 70 | 52 | 15 |
| \(E\) | 13.36 | 48.35 | 76.58 | 48.35 | 13.36 |
| \(\dfrac{(O - E)^2}{E}\) | 1.610 | 0.232 | 0.566 | 0.276 | 0.201 |

\(X^2 = 2.885\). The mean and standard deviation were given, so \(\nu = 5 - 1 = 4\), and the critical value is 9.488. Since \(2.89 < 9.488\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the masses do not follow \(\mathrm{N}(250, 4^2)\).
:::

If the question had estimated both \(\mu\) and \(\sigma\) from the data (for instance with \(\mu = \bar x\)), you would calculate the probabilities in the same way with those values and take \(\nu = 5 - 1 - 2 = 2\). Questions on the normal distribution do not involve a long calculation: either the parameters are given or the question tells you the estimates to use.

A hypothesis can also give the PDF of a continuous variable. Integrate over each class.

:::eg A continuous random variable \(X\) takes values from 0 to 4. A model says its PDF is \(f(x) = \dfrac{x}{8}\) for \(0 \leq x \leq 4\). A sample of 160 observations has 14, 26, 55 and 65 values in the classes \(0 \leq x < 1\), \(1 \leq x < 2\), \(2 \leq x < 3\) and \(3 \leq x \leq 4\). Test the model at the 5% level.
First check that this is a PDF: \(\displaystyle\int_0^4 \frac{x}{8}\,\mathrm{d}x = \left[\frac{x^2}{16}\right]_0^4 = 1\).

\(H_0\): \(X\) has PDF \(\dfrac{x}{8}\) on \([0, 4]\). \(H_1\): it does not.

The probability of the class from \(a\) to \(b\) is \(\dfrac{b^2 - a^2}{16}\), so the four probabilities are \(\tfrac{1}{16}\), \(\tfrac{3}{16}\), \(\tfrac{5}{16}\) and \(\tfrac{7}{16}\), and the expected frequencies are \(10\), \(30\), \(50\) and \(70\).

| Class | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| \(O\) | 14 | 26 | 55 | 65 |
| \(E\) | 10 | 30 | 50 | 70 |
| \(\dfrac{(O - E)^2}{E}\) | 1.600 | 0.533 | 0.500 | 0.357 |

\[X^2 = 1.600 + 0.533 + 0.500 + 0.357 = 2.99\]
No parameter was estimated, so \(\nu = 4 - 1 = 3\), and the critical value is 7.815. Since \(2.99 < 7.815\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, that the sample does not come from this distribution.
:::

## Reading the result

### Which classes cause the result?

The terms \(\dfrac{(O - E)^2}{E}\) show where the model and the data disagree. A class with a large term is the main reason for a rejection, and comparing \(O\) with \(E\) there tells you the direction: more than expected, or fewer. That is the comment examiners look for in a context question, as in the sweet peas (type B) and the call centre (very quiet and very busy intervals).

### Criticising a model

A model can fail because the mathematics of the distribution is not what is happening. In the exam, give a reason in the context of the question.

- **Binomial** \(\mathrm{B}(m, p)\): each trial must be independent, and \(p\) must be the same for every trial. A reason in context: the items in a box come from one machine, so a fault in one makes a fault in the next more likely; or the faulty rate changes between shifts.
- **Poisson**: events must occur independently, at random, at a constant average rate. A reason in context: calls come in bursts after an advertisement, or the rate is higher at lunchtime.
- **Geometric**: the trials must be independent with a constant probability of success, so a player who improves with practice breaks the model.
- **Normal**: the variable must be continuous with a symmetric bell shape; a skewed variable such as waiting times does not fit.

When a model is not rejected, say so carefully. The test has not shown that the model is right, only that the data give no good reason to doubt it.

### Wording the conclusion

:::exam How the marks are earned
The June 2025 Paper 4 goodness-of-fit test (a binomial model, [5]) was marked:
- B1 for the hypotheses in words, naming the distribution and the data;
- M1 for an expression of the right form with the classes correctly combined;
- A1 for the value of \(X^2\);
- M1 for comparing it with the critical value (printed in the scheme, with no separate mark) and stating reject or do not reject;
- A1 for a correct conclusion in context from correct working.

So \(\nu\) and the critical value earn nothing on their own, but a wrong \(\nu\) costs the final mark. When the expected frequencies are not given, finding them earns M1 A1 as well.
- Write the conclusion in context with "evidence" language: "there is sufficient evidence, at the 5% level, that the number of calls does not follow a Poisson distribution", or "there is insufficient evidence ... that the die is biased".
- Do not write "the data prove the model", "accept \(H_1\)" or "the model is wrong", and do not write "no evidence" for a non-significant result: write "insufficient evidence" or "not enough evidence".
- Write \(\nu\) down anyway: it shows the examiner which critical value you meant.
- The \(\chi^2\) table is printed in MF19, so you read the critical value from it. The formula \(X^2 = \sum \dfrac{(O - E)^2}{E}\) and the rule \(\nu = n - 1 - k\) are not printed: learn them.
:::

:::eg (Exam style) A four-sided spinner has faces numbered 1 to 4. It is claimed that the probability of scoring \(r\) is \(P(X = r) = kr\), where \(k\) is a constant. The spinner is spun 150 times and the scores 1, 2, 3 and 4 occur 22, 27, 41 and 60 times. (a) Show that \(k = 0.1\). (b) Test the claim at the 10% significance level.
**(a)** The probabilities add to 1:
\[k(1 + 2 + 3 + 4) = 1\] [M1]
\[10k = 1, \quad k = 0.1\] [A1]

**(b)** \(H_0\): \(P(X = r) = 0.1r\) for \(r = 1, 2, 3, 4\). \(H_1\): the probabilities are not of this form. [B1]

The expected frequencies are \(150 \times 0.1r\):
\[E = 15,\ 30,\ 45,\ 60\] [M1 A1]
All are at least 5, and no parameter was estimated from the data.
\[X^2 = \frac{(22 - 15)^2}{15} + \frac{(27 - 30)^2}{30} + \frac{(41 - 45)^2}{45} + \frac{(60 - 60)^2}{60}\] [M1]
\[= 3.267 + 0.300 + 0.356 + 0 = 3.92\] [A1]
\(\nu = 4 - 1 = 3\), and the critical value for 10% (the column \(p = 0.9\)) is 6.251.

Since \(3.92 < 6.251\), do not reject \(H_0\): there is insufficient evidence, at the 10% level, that the scores do not follow this distribution. [M1 A1]
:::

:::board
Edexcel IAL Statistics 3 also covers goodness-of-fit tests, with the same statistic and the same rule that expected frequencies must reach 5. The CAIE questions rely on the MF19 \(\chi^2\) table, and 9231 never asks for a continuity or Yates correction.
:::

:::eg Spot the error: the number \(X\) of seeds that germinate in a packet of 4 is recorded for 120 packets: 29, 43, 28, 17 and 3 packets for \(X = 0, 1, 2, 3, 4\). A student tests at the 5% level whether \(X \sim \mathrm{B}(4, p)\), with \(p\) estimated from the data, for 7 marks.
A student wrote this answer.

Line 1: \(H_0\): the number of seeds germinating follows \(\mathrm{B}(4, p)\). \(H_1\): it does not. [B1]
Line 2: \(\bar x = \dfrac{162}{120} = 1.35\), \(\hat p = 0.3375\). Expected frequencies 23.12, 47.11, 36.00, 12.23, 1.56. Combine the last two: 13.78, with \(O = 20\). [M1 A1]
Line 3: \(X^2 = 1.497 + 0.358 + 1.776 + 2.805 = 6.44\) [M1 A1]
Line 4: \(\nu = 4 - 1 = 3\), critical value 7.815
Line 5: \(6.44 < 7.815\), so do not reject \(H_0\): there is insufficient evidence that the binomial model is unsuitable. [M1 A0]

Lines 1 to 3 are correct and earn all five of their marks.

**Line 4 uses the wrong \(\nu\).** The student forgot that \(p\) was estimated from the data, so there is a second degree of freedom to subtract. No mark is printed against \(\nu\) itself, but the conclusion mark is for a correct conclusion from correct working, so line 5 loses it. Line 5 still earns its method mark, because the student compared the statistic with the critical value they had found; only the accuracy mark (a correct conclusion) is lost. The student scores 6 out of 7.

Correct line 4: \(\nu = 4 - 1 - 1 = 2\), critical value 5.991.
Correct line 5: \(6.44 > 5.991\), so reject \(H_0\): there is sufficient evidence, at the 5% level, that the number of seeds germinating does not follow a binomial distribution. [M1 A1] The wrong \(\nu\) reversed the conclusion.
:::

:::try Start easy, finish at exam standard
Q: A spinner has 5 equal sectors and is spun 100 times. The sectors come up 24, 18, 22, 15 and 21 times. Find \(X^2\) to test whether the spinner is fair, and give the critical value at 5%.
A: \(E = 20\) for each sector. \(X^2 = \dfrac{16 + 4 + 4 + 25 + 1}{20} = \dfrac{50}{20} = 2.5\). \(\nu = 4\), critical value 9.488. Since \(2.5 < 9.488\), do not reject \(H_0\): insufficient evidence at the 5% level that the spinner is unfair.
Q: State \(\nu\) for each test. (a) A uniform distribution with 7 classes. (b) A Poisson distribution whose mean is estimated from the data, with 6 classes after combining. (c) A binomial distribution with \(p\) estimated from the data, with 8 classes that are combined to 5. (d) A normal distribution with \(\mu\) and \(\sigma\) both estimated, with 6 classes.
A: (a) \(\nu = 7 - 1 = 6\). (b) \(\nu = 6 - 1 - 1 = 4\). (c) The combined number, 5, counts: \(\nu = 5 - 1 - 1 = 3\). (d) \(\nu = 6 - 1 - 2 = 3\).
Q: A coin is tossed three times, and the number of heads is recorded for 80 sets of three tosses: 14, 27, 29 and 10 sets for 0, 1, 2 and 3 heads. Test at the 5% level whether \(X \sim \mathrm{B}(3, 0.5)\).
A: \(P = \tfrac18, \tfrac38, \tfrac38, \tfrac18\), so \(E = 10, 30, 30, 10\), all at least 5. \(X^2 = \dfrac{16}{10} + \dfrac{9}{30} + \dfrac{1}{30} + 0 = 1.933\). \(\nu = 3\), critical value 7.815. Do not reject \(H_0\): insufficient evidence that the binomial model with \(p = 0.5\) does not fit.
Q: The expected frequencies in six classes are 1.8, 6.2, 15.5, 24.0, 12.1 and 4.4. Combine adjacent classes so that every expected frequency is at least 5, and state the new number of classes.
A: Class 1 (1.8) is below 5, so merge it with class 2: \(1.8 + 6.2 = 8.0\). Class 6 (4.4) is below 5, so merge it with class 5: \(12.1 + 4.4 = 16.5\). The classes are 8.0, 15.5, 24.0 and 16.5, so 4 classes. (The observed frequencies of the merged classes are merged in the same way.)
Q: A model says three types of item occur in the ratio 3 : 2 : 1. Among 180 items there are 78, 70 and 32 of the three types. Test the model at the 5% level.
A: \(E = 90, 60, 30\). \(X^2 = \dfrac{144}{90} + \dfrac{100}{60} + \dfrac{4}{30} = 1.6 + 1.667 + 0.133 = 3.4\). \(\nu = 2\), critical value 5.991. Since \(3.4 < 5.991\), do not reject \(H_0\): insufficient evidence that the ratio is not 3 : 2 : 1.
Q: The number of typing slips per page is thought to follow \(\mathrm{Po}(1.5)\). Of 60 pages, 10 have no slips, 24 have exactly one and 26 have two or more. Test at the 5% level.
A: \(P(0) = \mathrm{e}^{-1.5} = 0.2231\), \(P(1) = 1.5\mathrm{e}^{-1.5} = 0.3347\), \(P(\geq 2) = 1 - 0.2231 - 0.3347 = 0.4422\). \(E = 13.39, 20.08, 26.53\). \(X^2 = 0.857 + 0.765 + 0.011 = 1.63\). The mean 1.5 was given, so \(\nu = 3 - 1 = 2\), critical value 5.991. Do not reject \(H_0\): insufficient evidence that slips do not follow \(\mathrm{Po}(1.5)\).
Q: Use \(\sum \dfrac{O^2}{E} - N\) to confirm \(X^2\) for the first question of this block.
A: \(\sum O^2 = 576 + 324 + 484 + 225 + 441 = 2050\), so \(\dfrac{2050}{20} - 100 = 102.5 - 100 = 2.5\), the same.
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ A spinner has 5 equal sectors and is spun 100 times. The sectors come up 27, 15, 22, 18 and 18 times. Test, at the 5% significance level, whether the spinner is fair.
A: \(H_0\): the spinner is fair. \(H_1\): it is not fair. [B1]
\(E = 20\) for each sector, and \(X^2 = \dfrac{49 + 25 + 4 + 4 + 4}{20} = 4.3\). [M1 A1]
\(\nu = 4\), critical value 9.488.
\(4.3 < 9.488\), so do not reject \(H_0\): insufficient evidence, at the 5% level, that the spinner is unfair. [M1 A1]
Q: [4 marks] ★ A \(\mathrm{Po}(\lambda)\) distribution, with \(\lambda\) estimated from a sample of 100, gives expected frequencies 3.9, 14.6, 25.8, 27.4, 17.6, 7.4 and 3.3 for \(0, 1, 2, \dots, 5\) and "6 or more". Combine classes so that each expected frequency is at least 5, state the resulting number of classes and the degrees of freedom, and find the 5% critical value.
A: The first class (3.9) joins the second: \(3.9 + 14.6 = 18.5\); the last (3.3) joins the one before: \(7.4 + 3.3 = 10.7\). [M1]
The classes are 18.5, 25.8, 27.4, 17.6 and 10.7, so 5 classes. [A1]
\(\nu = 5 - 1 - 1 = 3\) because \(\lambda\) was estimated. [B1]
Critical value 7.815. [B1]
Q: [7 marks] ★★ In a game, each player throws a dart until it hits the target. It is claimed that \(X\), the number of throws needed, has a geometric distribution \(\mathrm{Geo}(0.3)\). For 100 players the numbers of throws needed were 1, 2, 3, 4, 5, 6, 7 and "8 or more" for 34, 20, 13, 12, 7, 5, 3 and 6 players. Test the claim at the 5% level.
H: \(P(X = r) = 0.7^{r-1} \times 0.3\) and \(P(X \geq r) = 0.7^{r-1}\).
H: Check which expected frequencies fall below 5.
A: \(H_0\): the number of throws follows \(\mathrm{Geo}(0.3)\). \(H_1\): it does not. [B1]
\(E = 30, 21, 14.7, 10.29, 7.203, 5.042\) for 1 to 6, then \(3.529\) for 7 and \(100 \times 0.7^7 = 8.235\) for "8 or more". Combine the last two classes: \(E = 11.76\), \(O = 3 + 6 = 9\). [M1 A1]
\[X^2 = \frac{16}{30} + \frac{1}{21} + \dots + \frac{(9 - 11.76)^2}{11.76}\] [M1]
\[\begin{aligned}
&0.533 + 0.048 + 0.197 + 0.284 \\
&\quad + 0.006 + 0.000 + 0.650 = 1.72
\end{aligned}\] [A1]
7 classes, no estimated parameter: \(\nu = 6\), critical value 12.592.
\(1.72 < 12.592\), so do not reject \(H_0\): insufficient evidence, at the 5% level, that the number of throws does not follow \(\mathrm{Geo}(0.3)\). [M1 A1]
Q: [8 marks] ★★ A continuous random variable \(X\) has PDF \(f(x) = \dfrac{3x^2}{8}\) for \(0 \leq x \leq 2\), according to a model. A sample of 160 observations has 3, 19, 44 and 94 values in the classes \(0 \leq x < 0.5\), \(0.5 \leq x < 1\), \(1 \leq x < 1.5\) and \(1.5 \leq x \leq 2\). Test the model at the 5% level.
H: The probability of a class from \(a\) to \(b\) is \(\dfrac{b^3 - a^3}{8}\).
A: \(H_0\): \(X\) has the stated PDF. \(H_1\): it does not. [B1]
The class probabilities are \(\dfrac{b^3 - a^3}{8}\): \(\tfrac{1}{64}\), \(\tfrac{7}{64}\), \(\tfrac{19}{64}\), \(\tfrac{37}{64}\). [M1]
\(E = 2.5, 17.5, 47.5, 92.5\). [A1]
The first class has \(E < 5\), so combine the first two: \(E = 20\), \(O = 22\). [M1]
\[X^2 = \frac{(22 - 20)^2}{20} + \frac{(44 - 47.5)^2}{47.5} + \frac{(94 - 92.5)^2}{92.5}\] [M1]
\[= 0.200 + 0.258 + 0.024 = 0.482\] [A1]
3 classes: \(\nu = 2\), critical value 5.991.
\(0.482 < 5.991\), so do not reject \(H_0\): insufficient evidence, at the 5% level, that the sample does not come from this distribution. [M1 A1]
Q: [7 marks] ★★ The lengths of 120 metal bars are grouped. The model is \(\mathrm{N}(\mu, \sigma^2)\), where \(\mu = 50\) and \(\sigma = 6\) are the sample mean and standard deviation. The numbers of bars with lengths \(x < 44\), \(44 \leq x < 50\), \(50 \leq x < 56\) and \(x \geq 56\) are 25, 36, 42 and 17. Test at the 5% level whether the model fits.
H: The boundaries are \(\mu - \sigma\), \(\mu\) and \(\mu + \sigma\).
H: Two parameters were estimated.
A: \(H_0\): the lengths follow \(\mathrm{N}(50, 6^2)\). \(H_1\): they do not. [B1]
\(z = -1, 0, 1\), and the probabilities are \(0.1587, 0.3413, 0.3413, 0.1587\). [M1]
\(E = 19.04, 40.96, 40.96, 19.04\). [A1]
\[\begin{aligned}
X^2 &= \frac{(25 - 19.04)^2}{19.04} + \frac{(36 - 40.96)^2}{40.96} \\
&\quad + \frac{(42 - 40.96)^2}{40.96} + \frac{(17 - 19.04)^2}{19.04}
\end{aligned}\] [M1]
\[= 1.867 + 0.601 + 0.026 + 0.218 = 2.71\] [A1]
4 classes, 2 parameters estimated: \(\nu = 4 - 1 - 2 = 1\), critical value 3.841.
\(2.71 < 3.841\), so do not reject \(H_0\): insufficient evidence, at the 5% level, that the lengths do not follow this normal distribution. [M1 A1]
Q: [3 marks] ★ A technician records, for each of 150 batches of 10 sensors from one production line, the number \(X\) of sensors that fail a test, and models \(X \sim \mathrm{B}(10, p)\). State two conditions needed for the model, in the context of the sensors, and give one reason why the model may fail.
A: The sensors fail independently of each other. [B1]
The probability of failing is the same for every sensor. [B1]
A reason: sensors made one after another on the same line may share a fault (or the probability may drift between batches as the machine wears), so independence or constant \(p\) fails. [B1]
Q: [9 marks] (#math.s2.poisson) ★★★ A proofreader records the number of errors on each of 150 pages: 40, 55, 31, 15, 7 and 2 pages have 0, 1, 2, 3, 4 and 5 errors. (a) Show that the mean number of errors per page is \(\tfrac43\). (b) Test, at the 5% level, whether the number of errors per page follows a Poisson distribution.
H: Use \(\lambda = \tfrac43\) and \(P(X = r) = \dfrac{\mathrm{e}^{-\lambda}\lambda^r}{r!}\). The data table has classes 0 to 5, and the last class is "5 or more" (its \(E\) is \(150\) minus the other five \(E\) values); after combining, the last class is "4 or more".
H: Look for expected frequencies below 5 at the end.
H: \(\nu\) reflects that \(\lambda\) was estimated.
A: (a) \(\sum xf = 0 + 55 + 62 + 45 + 28 + 10 = 200\), so \(\bar x = \dfrac{200}{150} = \dfrac43\). [M1 A1]
(b) \(H_0\): the number of errors per page follows a Poisson distribution. \(H_1\): it does not. [B1]
With \(\lambda = \tfrac43\): \(E = 150P(X = r)\) gives 39.54, 52.72, 35.15 and 15.62 for 0 to 3; \(E\) for 4 errors is 5.21; \(E\) for 5 errors (taken as the last class, "5 or more") is 150 minus the other five \(E\) values, which is 1.77. Since 1.77 is below 5, combine 4 and 5: \(E = 6.97\) (for "4 or more") and \(O = 7 + 2 = 9\). [M1 A1]
\[\begin{aligned}
X^2 &= \frac{(40 - 39.54)^2}{39.54} + \frac{(55 - 52.72)^2}{52.72} + \frac{(31 - 35.15)^2}{35.15} \\
&\quad + \frac{(15 - 15.62)^2}{15.62} + \frac{(9 - 6.97)^2}{6.97}
\end{aligned}\] [M1]
\[= 0.005 + 0.099 + 0.489 + 0.025 + 0.589 = 1.21\] [A1]
5 classes, \(\lambda\) estimated: \(\nu = 5 - 1 - 1 = 3\), critical value 7.815.
\(1.21 < 7.815\), so do not reject \(H_0\): insufficient evidence, at the 5% level, that the number of errors does not follow a Poisson distribution. [M1 A1]
Q: [10 marks] (#math.s1.drv) ★★★ The number \(X\) of seeds that germinate in each of 120 packets of 5 seeds is recorded: 4, 20, 46, 32, 14 and 4 packets have 0, 1, 2, 3, 4 and 5 germinating. It is suggested that \(X \sim \mathrm{B}(5, p)\). (a) Find the estimate of \(p\) from the data, giving the sample mean. (b) Show that the expected frequency for \(X = 0\) is 4.86, to 3 s.f. (c) Combine classes where necessary and test the suggestion at the 5% level.
H: \(\hat p = \dfrac{\bar x}{5}\).
H: Two classes at each end have an expected frequency below 5 or close to it: check them one at a time.
H: After combining there are four classes. How many parameters were estimated?
A: (a) \(\bar x = \dfrac{0 + 20 + 92 + 96 + 56 + 20}{120} = \dfrac{284}{120} = 2.3667\) [M1]
\(\hat p = \dfrac{2.3667}{5} = 0.4733\) [A1]
(b) \(E_0 = 120(1 - \hat p)^5\) [M1] \(= 120 \times 0.5267^5 = 4.86\) [A1]
(c) \(H_0\): the number of seeds germinating follows \(\mathrm{B}(5, p)\). \(H_1\): it does not. [B1]
The other expected frequencies are 21.85, 39.28, 35.30, 15.86 and 2.85. The first (4.86) and last (2.85) are below 5, so each joins its neighbour: classes 0 and 1 (\(E = 26.71\), \(O = 24\)) and classes 4 and 5 (\(E = 18.71\), \(O = 18\)); both merged values are above 5, so nothing more is needed. [M1]
\[\begin{aligned}
X^2 &= \frac{(24 - 26.71)^2}{26.71} + \frac{(46 - 39.28)^2}{39.28} \\
&\quad + \frac{(32 - 35.30)^2}{35.30} + \frac{(18 - 18.71)^2}{18.71}
\end{aligned}\] [M1]
\[= 0.276 + 1.151 + 0.308 + 0.027 = 1.76\] [A1]
4 classes, \(p\) estimated: \(\nu = 4 - 1 - 1 = 2\), critical value 5.991.
\(1.76 < 5.991\), so do not reject \(H_0\): insufficient evidence, at the 5% level, that the number of seeds germinating does not follow a binomial distribution. [M1 A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A goodness-of-fit test has just two classes, with observed frequencies \(x\) and \(n - x\) and expected frequencies \(np\) and \(n(1 - p)\). (a) Show that \(X^2 = \dfrac{(x - np)^2}{np(1 - p)}\). (b) Hence explain why the 5% critical value of \(\chi^2_1\), 3.841, is the square of 1.960.
H: \((x - np) + ((n - x) - n(1 - p)) = 0\), so the two deviations are equal in size.
H: Put \(d = x - np\) and combine the two fractions: \(\dfrac{1}{p} + \dfrac{1}{1 - p} = \dfrac{1}{p(1 - p)}\).
A: (a) Let \(d = x - np\). Then \((n - x) - n(1 - p) = -d\). [B1]
\[X^2 = \frac{d^2}{np} + \frac{d^2}{n(1 - p)}\] [M1]
\[= \frac{d^2}{n}\left(\frac1p + \frac{1}{1 - p}\right) = \frac{d^2}{n}\cdot\frac{1}{p(1 - p)} = \frac{(x - np)^2}{np(1 - p)}\] [M1 A1]
(b) The binomial \(\mathrm{B}(n, p)\) has mean \(np\) and variance \(np(1 - p)\), so for large \(n\), \(Z = \dfrac{x - np}{\sqrt{np(1 - p)}}\) is approximately \(\mathrm{N}(0, 1)\), and \(X^2 = Z^2\). [B1]
A two-tailed 5% test on \(Z\) rejects when \(|Z| > 1.960\), which is the same as \(Z^2 > 1.960^2 = 3.842\): this is the critical value 3.841 of \(\chi^2_1\) (the small gap is rounding). [B1]
Q: [6 marks] ★★★ The die from the worked example (frequencies 15, 25, 22, 18, 24, 16 in 120 rolls) gave \(X^2 = 4.5\). Suppose the same relative frequencies were observed in a sample \(k\) times as big (\(120k\) rolls). (a) Show that \(X^2\) is multiplied by \(k\). (b) Find the smallest whole number \(k\) for which the test at the 5% level would reject \(H_0\). (c) Comment on what this says about small biases.
H: Every \(O\) and every \(E\) is multiplied by \(k\), so each term \(\dfrac{(O - E)^2}{E}\) is multiplied by \(k^2/k\).
H: You need \(4.5k > 11.070\).
A: (a) With \(kO\) and \(kE\) in place of \(O\) and \(E\), each term becomes \(\dfrac{(kO - kE)^2}{kE} = k\,\dfrac{(O - E)^2}{E}\), so \(X^2\) becomes \(4.5k\). [M1 A1]
(b) \(\nu = 5\) does not change, so the critical value is still 11.070. We need \(4.5k > 11.070\), so \(k > 2.46\). [M1 A1]
The smallest whole number is \(k = 3\) (360 rolls), giving \(X^2 = 13.5 > 11.070\). [A1]
(c) With the proportions fixed, a larger sample turns the same small imbalance into a rejection: a slightly biased die is hard to detect with 120 rolls and easy with 360. So "do not reject" can only mean the sample was too small to show a bias. [B1]
:::

:::quiz
? A Poisson distribution has \(\lambda\) estimated from the sample mean, and 6 classes remain after combining. What is \(\nu\)?
- \(5\)
+ \(4\)
- \(6\)
- \(3\)
> \(\nu = n - 1 - k = 6 - 1 - 1 = 4\). Using 5 forgets the estimated parameter, 6 forgets both reductions, and 3 subtracts a parameter that was not estimated.
? The expected frequencies in a goodness-of-fit test are 2.9, 6.1, 18.4, 22.0 and 10.6. What should you do before calculating \(X^2\)?
- Calculate all five terms, then combine the small ones
- Delete the class with \(E = 2.9\) from the table
+ Combine the first class with the second, then calculate with four classes
- Round every expected frequency to the nearest whole number
> The class with \(E = 2.9\) is below 5, so merge it with its neighbour (observed and expected) first. Deleting a class throws away data, and combining after calculating is the lost mark in the warning.
? You test at the 5% level and find \(X^2 = 6.2\) with \(\nu = 3\). The conclusion is
- reject \(H_0\), because \(6.2 > 5.991\)
+ do not reject \(H_0\): insufficient evidence at the 5% level that the model does not fit
- the model is proved to be correct
- reject \(H_0\), because the statistic is above 5
> The critical value for \(\nu = 3\) at 5% is 7.815, and \(6.2 < 7.815\). The value 5.991 belongs to \(\nu = 2\), the statistic does not "prove" the model, and the number 5 has nothing to do with the level.
? Which column of the \(\chi^2\) table gives the critical value for a 1% goodness-of-fit test?
- \(p = 0.01\)
- \(p = 0.005\)
+ \(p = 0.99\)
- \(p = 0.975\)
> The test is in the upper tail, so 1% above the critical value means \(P(X \leq x) = 0.99\). The column \(p = 0.01\) is the lower tail, and 0.975 is for a 2.5% test.
? A binomial model with \(p = 0.35\) stated in the question gives 5 classes after combining. What is \(\nu\)?
- \(3\)
+ \(4\)
- \(5\)
- \(2\)
> The probability was given, not estimated from the data, so only the total constraint applies: \(\nu = 5 - 1 = 4\). Subtracting another 1 is the common error.
? A table has \(O = 12\) and \(E = 8\) in one class. Which expression gives its contribution to \(X^2\)?
+ \(\dfrac{(12 - 8)^2}{8}\)
- \(\dfrac{(12 - 8)^2}{12}\)
- \(\dfrac{12 - 8}{8}\)
- \(\dfrac{(12 - 8)^2}{8^2}\)
> The statistic divides the squared difference by the expected frequency. Dividing by \(O\), omitting the square or squaring \(E\) all change the measure.
:::

:::checklist What you can now do
- [ ] I can turn a hypothesis (uniform, given ratios, binomial, Poisson, geometric, a normal distribution or a given PDF) into expected frequencies for data, with the open end class found as the remainder.
- [ ] I can estimate a parameter from the data (\(\hat p = \bar x / m\), \(\lambda = \bar x\), \(\hat p = 1/\bar x\)) when the question says to.
- [ ] I can combine adjacent classes so that every expected frequency is at least 5, before calculating \(X^2\).
- [ ] I can calculate \(X^2 = \sum \dfrac{(O - E)^2}{E}\) and check it with \(\sum \dfrac{O^2}{E} - N\).
- [ ] I can find the degrees of freedom \(\nu = n - 1 - k\), reducing it for each parameter estimated from the data.
- [ ] I can read the upper-tail critical value from the \(\chi^2\) table for the right level and \(\nu\).
- [ ] I can state the hypotheses, compare, and write a conclusion in context using "sufficient evidence" language.
- [ ] I can say which classes contribute most and give a reason, in context, why a binomial, Poisson or geometric model may be unsuitable.
:::

:::recap
- \(X^2 = \sum \dfrac{(O - E)^2}{E}\), where \(E = N \times P(\text{class})\) under \(H_0\); the equivalent form is \(\sum \dfrac{O^2}{E} - N\). Neither is on MF19; the \(\chi^2\) table is.
- \(H_0\): the data fit the model. The test is one-tailed: reject when \(X^2\) is above the upper-tail critical value (column \(p = 0.95\) for 5%, \(0.99\) for 1%).
- Combine adjacent classes, before calculating, until every \(E \geq 5\).
- \(\nu = n - 1 - k\): \(n\) classes after combining, \(k\) parameters estimated from the data. Parameters given by the hypothesis cost nothing.
- Estimates: binomial \(\hat p = \bar x / m\); Poisson \(\lambda = \bar x\); geometric \(\hat p = 1 / \bar x\). The open last class has probability \(1 -\) the sum of the others.
- Conclusion in context: "sufficient (or insufficient) evidence, at the 5% level, that the data do not follow ...". A non-significant result does not prove the model.
- The terms \((O - E)^2 / E\) show which classes disagree most; model reasons: independence, constant \(p\) or constant rate.
:::

:::links
- read: [The chi-square distribution](https://openstax.org/books/introductory-statistics-2e/pages/11-introduction) · OpenStax · goodness of fit with worked examples and the table logic
- practise: [Chi-square tests](https://www.khanacademy.org/math/statistics-probability/inference-categorical-data-chi-square-tests) · Khan Academy · goodness-of-fit practice with feedback
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · free graded questions with answers
- explore: [Frequentist inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) · Seeing Theory · how sampling variation makes test statistics wobble
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Chi-squared tests for independence](#math.fm.contingency) uses the same statistic on a table of counts, to ask whether two categorical variables are linked.
