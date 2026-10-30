@chapter bio.stats
@title Statistics for biologists
@level a2
@paper CAIE 9700 Papers 4 and 5
@time 5–6 hours
@summary Biological data vary, so conclusions need statistics. You will learn the three types of data, how samples and probability work, how to describe data with the mean, median, mode, range, standard deviation, standard error and 95% confidence intervals, how to draw and read error bars, how to write a null hypothesis, and how to choose, calculate and interpret the chi-squared test, the t-test, Pearson's correlation and Spearman's rank correlation.

:::why
Living things vary, and so does every measurement you make on them. Two plots of the same crop never give exactly the same yield, so when one fertiliser "beats" another you must ask whether the difference is real or just chance. Statistics gives you a fair, agreed way to answer. Papers 4 and 5 give you a formula and a table of critical values and expect you to finish a calculation, choose the right test and write a conclusion in the correct words. This chapter brings together tests you have already met in [Dihybrid crosses and the chi-squared test](#bio.dihybrid), [Variation](#bio.variation) and [Biodiversity](#bio.biodiversity), gives each one a fresh worked example, and shows you how to choose between them.
:::

**Before you start**, you should know the mean, range and graph skills from [Maths skills for biology](#bio.maths), the ideas of normal distribution and standard deviation from [Variation](#bio.variation), and how a ratio such as 3 : 1 comes from a genetic cross in [Inheritance](#bio.inheritance). The maths course has a longer treatment of [the normal distribution](#math.s1.normal) and of [hypothesis testing](#math.s2.hypothesis) if you want more practice.

:::try Warm-up
Q: In the t-test, how do you calculate the degrees of freedom? (from [Variation](#bio.variation))
A: \(n_1 + n_2 - 2\), where \(n_1\) and \(n_2\) are the numbers of values in the two samples.
Q: A cross between two heterozygous parents (\(Aa \times Aa\)) is expected to give what ratio of dominant to recessive offspring? (from [Inheritance](#bio.inheritance))
A: 3 dominant : 1 recessive.
Q: Why must quadrats be placed at random when sampling a habitat? (from [Biodiversity](#bio.biodiversity))
A: To avoid bias: if the investigator chooses where to sample, the sample may not represent the whole habitat, so the results cannot be applied to it.
:::

## Types of data

Before you choose a graph, a calculation or a test, you must know what kind of data you have. There are three kinds in the syllabus.

:::def Nominal data
Data sorted into named categories that have no natural order, for example blood group, flower colour or the habitat where an animal is found. You count how many fall into each category.
:::

:::def Ordinal data
Data sorted into categories that can be put in a meaningful order, but where the gaps between the categories are not equal or not measured, for example an abundance scale (rare, occasional, frequent, abundant) or a rank from 1 to 10.
:::

:::def Continuous data
Data from measurements that can take any value within a range, for example length, mass, time, temperature or concentration. The values can be added, averaged and compared in size.
:::

| type | example | what you can do |
|---|---|---|
| nominal | eye colour of 50 people | count each category; give percentages or frequencies |
| ordinal | lichen abundance on a scale of 1 to 5 | put in order; find the median or mode; rank |
| continuous | length of 50 leaves in mm | find the mean and standard deviation; plot a scatter graph |

A count such as "17 snails in a quadrat" is a whole number, but when you sort animals or plants into classes and count how many are in each class, you are using frequency data of the nominal kind. If you rank counts from smallest to largest, you are treating them as ordinal data. The skill is to say which kind the data are *in the test you are using* and why.

:::eg State the type of data (nominal, ordinal or continuous) in each case. (a) The number of seeds that germinate with a red coat and the number with a brown coat. (b) The mass in grams of each seed. (c) Seeds ranked from 1 (smallest) to 8 (largest) by eye.
(a) Nominal: the seeds are sorted into two categories (coat colour) and counted. [B1]

(b) Continuous: mass is measured and can take any value within a range. [B1]

(c) Ordinal: the ranks put the seeds in order but do not say how much bigger each seed is. [B1]

A weaker answer says "numbers" for all three. The type of data depends on how the values are used, not on whether they look like numbers.
:::

## Samples and populations

:::def Population
All the individuals of one type that you want to find out about, for example all the beech trees in a wood or all adults with type 2 diabetes.
:::

:::def Sample
A smaller group taken from the population and measured, so that the results can be used to make statements about the whole population.
:::

You can almost never measure a whole population, so you measure a sample. Four principles make a sample fair:

- **Random selection**: every individual has an equal chance of being chosen, so the investigator's choice cannot bias the sample (use random numbers for coordinates, as in [Biodiversity](#bio.biodiversity)).
- **Large enough**: a bigger sample is less affected by one unusual individual, and the sample mean is closer to the population mean.
- **Representative**: the sample comes from the whole population, not only the easy-to-reach part. Sampling only beside a path gives results for the path.
- **Independent**: each measurement is on a different individual, not repeated measurements on one individual counted as separate points.

:::warn Repeats are not a larger sample
Measuring the same leaf five times shows how precisely you can measure that leaf. It does not tell you about the variation between leaves. A sample of five leaves needs five different leaves.
:::

## Chance and probability

:::def Probability
A number between 0 (cannot happen) and 1 (certain), found by dividing the number of ways an outcome can occur by the total number of equally likely outcomes. It can be written as a fraction, a decimal or a percentage.
:::

Genetic ratios are probabilities. When two heterozygous parents (\(Aa \times Aa\)) have a child, each gamete carries \(A\) or \(a\) with probability \(\tfrac12\), so the probability of the child being \(aa\) is \(\tfrac12 \times \tfrac12 = \tfrac14\). A 3 : 1 ratio means that each child has a probability of \(\tfrac34\) of showing the dominant feature. A ratio describes what happens in a very large number of births, but each individual birth is a separate chance event: the probability does not "remember" the earlier children.

:::key Two rules for combining probabilities
1. **"And" rule (independent events)**: multiply. The probability that two independent events both happen is \(P(A) \times P(B)\).
2. **"Or" rule (events that cannot both happen)**: add. The probability of one outcome or the other is \(P(A) + P(B)\).
:::

:::eg Two parents are both carriers of the recessive allele that causes cystic fibrosis (\(Cc \times Cc\)). Find the probability that (a) their first child has cystic fibrosis, (b) both of two children have it, (c) exactly one of two children has it.
(a) The child must receive \(c\) from each parent: \(\tfrac12 \times \tfrac12 = \tfrac14\). [B1]

(b) The two children are independent, so multiply: \(\tfrac14 \times \tfrac14 = \tfrac1{16}\). [B1]

(c) Either the first child has it and the second does not, or the other way round. Each order has probability \(\tfrac14 \times \tfrac34 = \tfrac3{16}\), and the two orders are added: [M1]

\[\begin{aligned} P &= \tfrac3{16} + \tfrac3{16} \\ &= \tfrac38 \end{aligned}\]

So the probability is \(\tfrac38\) (0.375). [A1]

Notice that a family of two children does not have to show a 3 : 1 ratio. Ratios appear only in large numbers.
:::

### What "p = 0.05" means

Real results never match a prediction exactly, because chance affects which gametes meet, which individual you sample and what you measure. A statistical test calculates how likely it is that a difference as big as the one you found would occur **by chance alone** if nothing else were acting.

:::def Probability value, \(p\)
The probability that a difference (or a relationship) at least as large as the one found in the data would arise by chance alone. In Cambridge Biology the standard level is \(p = 0.05\), a 5% probability.
:::

If the probability of getting your result by chance alone is less than 5%, scientists agree to treat the difference as **significant**: unlikely to be due to chance. If the probability is 5% or more, the difference **could be due to chance**. The 5% line is a convention, not a law of nature, so a result is not "nearly" or "very nearly" significant: it is either on one side of the critical value or the other.

## Describing data

A mass of numbers is hard to understand. **Descriptive statistics** summarise them in a few values.

:::def Mean
The sum of all the values divided by the number of values: \(\bar{x} = \dfrac{\sum x}{n}\).
:::

:::def Median
The middle value when the data are put in order (the mean of the two middle values if there is an even number of values).
:::

:::def Mode
The most frequent value (a data set can have more than one mode, or none).
:::

:::def Range
The difference between the largest and the smallest value. It uses only two values, so one extreme value can change it a lot.
:::

:::eg The numbers of aphids on nine rose leaves were 2, 3, 3, 4, 4, 4, 5, 7 and 24. Find the mean, median, mode and range, and say which best describes a typical leaf.
\[\begin{aligned} \text{mean} &= \frac{2+3+3+4+4+4+5+7+24}{9} \\ &= \frac{56}{9} = 6.2 \end{aligned}\]

The values are already in order, so the median is the fifth value, 4. The mode is 4 (it appears three times) and the range is \(24 - 2 = 22\).

The mean (6.2) is higher than seven of the nine leaves because of the one leaf with 24 aphids. The median and the mode (both 4) describe a typical leaf better. The data are **skewed**, so the mean is not a fair summary of the middle.
:::

### Normal and non-normal distributions

When you measure a continuous feature in many individuals, a **frequency graph** shows how the values are spread. Many biological features give a symmetrical, bell-shaped **normal distribution**: most values lie close to the mean, and fewer lie far away on either side. The mean, median and mode are all at the same place.

:::plot A normal distribution is symmetrical: the mean, median and mode are all at the peak.
--f "100*exp(0-((x-50)/12)**2/2)+0*sqrt(90-x)" --label "normal distribution" --x 0 100 --y 0 130 --xlabel "value" --ylabel "frequency" --pt "50,100,mean = median = mode@ne" --legend tr --alt "A symmetrical bell-shaped curve with its peak at a value of 50. The frequency falls away equally on both sides of the peak."
:::

A **non-normal** distribution is not symmetrical, or has more than one peak. In a skewed distribution a long tail of extreme values pulls the mean towards the tail, away from the mode.

:::plot A skewed distribution has a long tail on one side. The mean (30) lies in the tail, further from the peak than the mode (20).
--f "1.8473*x**2*exp(0-x/10)+0*sqrt(105-x)" --label "skewed distribution" --x 0 120 --y 0 130 --xlabel "value" --ylabel "frequency" --pt "20,100,mode@n" --pt "30,82.8,mean@ne" --legend tr --alt "A curve that rises steeply to a peak at a value of 20 and then falls slowly, with a long tail to the right that almost reaches zero by 100. The mean at 30 is further along the tail than the peak."
:::

Whether data are normal matters because the t-test and Pearson's correlation are only valid for data that are approximately normally distributed. If the data are skewed, or only ranks, you use a rank test instead. In an exam, the question will say or show whether the data are normally distributed. In your own work you can plot a histogram or a stem-and-leaf plot and look for a symmetrical bell shape.

## Spread: standard deviation, standard error and confidence intervals

Two samples can have the same mean but very different spread. A farmer is interested in the mean mass of a pig, but also in whether all pigs are close to the mean. Three related statistics describe spread and reliability.

:::formula Standard deviation (provided in the exam)
\[s = \sqrt{\frac{\sum (x - \bar{x})^2}{n - 1}}\]
\(x\) = each value, \(\bar{x}\) = the sample mean, \(n\) = the number of values. The denominator is \(n - 1\) because the values are a sample, not the whole population.
:::

:::def Standard deviation (\(s\))
A measure of how far the individual values in a sample are spread around the mean. About 95% of the values in a normal distribution lie within two standard deviations of the mean.
:::

:::formula Standard error and 95% confidence interval (provided in the exam)
\[\mathrm{SE} = \frac{s}{\sqrt{n}} \qquad 95\%\ \mathrm{CI} = \bar{x} \pm 2 \times \mathrm{SE}\]
(The factor 2 is the syllabus's approximation.)
:::

:::def Standard error (SE)
A measure of how reliable a sample mean is as an estimate of the population mean. It is found from the standard deviation and the sample size, and it falls as the sample gets larger.
:::

:::def 95% confidence interval
The range of values, \(\bar{x} \pm 2\) SE, within which the population mean lies with 95% confidence. Roughly, if you took many samples and calculated an interval for each, about 95 in 100 of the intervals would contain the true mean.
:::

:::cols
:::col Standard deviation
- Describes the **spread of the individuals** in the sample.
- Does not shrink as you collect more data (it settles down to a value).
- Large SD means the individuals vary a lot.
- Use it to say how variable the feature is.
:::
:::col Standard error
- Describes how **reliable the mean** is.
- Shrinks as \(n\) grows: four times the sample halves the SE.
- Small SE means the sample mean is probably close to the true mean.
- Use it for error bars and to compare means.
:::
:::

:::eg The root lengths, in mm, of six bean seedlings were 34, 29, 38, 31, 35 and 31. Calculate the mean, the standard deviation, the standard error and the 95% confidence interval.
Work out the mean, then each deviation from it, squared.

\[\begin{aligned} \bar{x} &= \frac{34+29+38+31+35+31}{6} \\ &= \frac{198}{6} = 33.0\,\mathrm{mm} \end{aligned}\]

| root length, \(x\) / mm | \(x - \bar{x}\) | \((x - \bar{x})^2\) |
|---|---|---|
| 34 | 1 | 1 |
| 29 | −4 | 16 |
| 38 | 5 | 25 |
| 31 | −2 | 4 |
| 35 | 2 | 4 |
| 31 | −2 | 4 |

\(\sum (x - \bar{x})^2 = 54\). Use \(n - 1 = 5\):

\[\begin{aligned} s &= \sqrt{\frac{54}{5}} \\ &= \sqrt{10.8} = 3.29\,\mathrm{mm} \end{aligned}\]

\[\begin{aligned} \mathrm{SE} &= \frac{3.286}{\sqrt{6}} \\ &= 1.34\,\mathrm{mm} \end{aligned}\]

\[\begin{aligned} 95\%\ \mathrm{CI} &= 33.0 \pm 2 \times 1.342 \\ &= 33.0 \pm 2.68 \\ &= 30.3\ \text{to}\ 35.7\,\mathrm{mm} \end{aligned}\]

The mean root length is 33.0 mm, and we can be 95% confident that the mean of all such seedlings lies between 30.3 and 35.7 mm.
:::

:::warn Four slips with spread
**Dividing by \(n\) instead of \(n - 1\)** gives an SD that is too small. **Confusing SD and SE**: the SE is the SD divided by \(\sqrt{n}\), so it is always smaller. **Forgetting the square root** of the sum of squares, or of \(n\). **Writing the interval as one number**: a confidence interval has a lower and an upper limit.
:::

### Error bars

Graphs of means should show how reliable each mean is. **Error bars** are short vertical lines through the top of each bar or point, one half-length above and one below the mean. They can show the standard deviation (spread of the data), the standard error, or the 95% confidence interval. The graph must say which.

For a bar chart or a graph of means, the error bar for 95% CI runs from \(\bar{x} - 2\,\mathrm{SE}\) to \(\bar{x} + 2\,\mathrm{SE}\).

<figure class="fig small"><svg viewBox="0 0 340 262" role="img" aria-label="Bar chart of mean stem length in millimetres for three groups of ten seedlings, with error bars showing the 95% confidence interval: control 33.0, fertiliser X 36.0 and fertiliser Y 42.0. The error bars of the control and fertiliser X overlap; the error bars of fertiliser X and fertiliser Y do not."><path class="ax" d="M52 34L52 206L324 206"/><path class="ln" d="M48 206L52 206"/><text class="ts" x="44" y="209" text-anchor="end">0</text><path class="ln" d="M48 171.6L52 171.6"/><text class="ts" x="44" y="174.6" text-anchor="end">10</text><path class="ln" d="M48 137.2L52 137.2"/><text class="ts" x="44" y="140.2" text-anchor="end">20</text><path class="ln" d="M48 102.8L52 102.8"/><text class="ts" x="44" y="105.8" text-anchor="end">30</text><path class="ln" d="M48 68.4L52 68.4"/><text class="ts" x="44" y="71.4" text-anchor="end">40</text><path class="ln" d="M48 34L52 34"/><text class="ts" x="44" y="37" text-anchor="end">50</text><text class="tl" x="6" y="14">mean stem length / mm</text><rect class="f1 s-acc sw2" x="87" y="92.48" width="50" height="113.52"/><path class="ln thick" d="M112 85.3004L112 99.6596"/><path class="ln thick" d="M104 85.3004L120 85.3004"/><path class="ln thick" d="M104 99.6596L120 99.6596"/><text class="tl" x="112" y="223" text-anchor="middle">control</text><rect class="f1 s-acc sw2" x="172" y="82.16" width="50" height="123.84"/><path class="ln thick" d="M197 74.5452L197 89.7748"/><path class="ln thick" d="M189 74.5452L205 74.5452"/><path class="ln thick" d="M189 89.7748L205 89.7748"/><text class="tl" x="197" y="223" text-anchor="middle">fertiliser</text><text class="tl" x="197" y="238" text-anchor="middle">X</text><rect class="f1 s-acc sw2" x="257" y="61.52" width="50" height="144.48"/><path class="ln thick" d="M282 54.7755L282 68.2645"/><path class="ln thick" d="M274 54.7755L290 54.7755"/><path class="ln thick" d="M274 68.2645L290 68.2645"/><text class="tl" x="282" y="223" text-anchor="middle">fertiliser</text><text class="tl" x="282" y="238" text-anchor="middle">Y</text><text class="tl" x="52" y="256">bars: mean ± 95% CI (n = 10)</text></svg><figcaption>Mean stem length with error bars of mean ± 95% CI (± 2 SE). The bars of the control and fertiliser X overlap, so that difference may be due to chance. The bars of fertiliser X and fertiliser Y do not overlap, so that difference is probably significant.</figcaption></figure>

:::key Reading error bars (a rule of thumb)
- If the 95% CI error bars of two means **overlap**, the difference between the means is probably **not significant**: it could be due to chance.
- If they **do not overlap**, the difference is probably **significant**.
- This is only a guide. A statistical test, such as the t-test, decides. Bars that show SD cannot be used in this way, because SD does not describe how reliable the mean is.
:::

:::eg Tomato seedlings (10 per group) were grown with no fertiliser (control), with fertiliser X and with fertiliser Y. The stem length after 14 days was measured. The control had a mean of 33.0 mm and \(s = 3.3\) mm, fertiliser X a mean of 36.0 mm and \(s = 3.5\) mm, and fertiliser Y a mean of 42.0 mm and \(s = 3.1\) mm. Calculate the 95% confidence interval for each group and say which differences are probably significant.
For each group \(\mathrm{SE} = s \div \sqrt{10}\) and the interval is \(\bar{x} \pm 2\,\mathrm{SE}\). [M1]

| group | mean / mm | SE / mm | 95% CI / mm |
|---|---|---|---|
| control | 33.0 | 1.04 | 30.9 to 35.1 |
| fertiliser X | 36.0 | 1.11 | 33.8 to 38.2 |
| fertiliser Y | 42.0 | 0.98 | 40.0 to 44.0 |

The intervals are correct [A1].

Control and X overlap (35.1 is above 33.8), so the difference of 3.0 mm is probably not significant. [B1]

X and Y do not overlap (38.2 is below 40.0), so the difference of 6.0 mm is probably significant, and Y is also different from the control. [B1]

The stems of Y are longer than those of X and the control. A t-test would be needed to be sure about X and the control.
:::

:::exam Describe, then explain
"Describe" a graph with error bars: give the trend and the values with units ("fertiliser Y gave a mean stem length of 42.0 mm compared with 33.0 mm for the control"), then say whether the error bars overlap. "Explain" needs the biological reason as well, for example why the fertiliser might increase growth. Never use error bars to explain *why*; they only tell you whether a difference is likely to be real.
:::

## Hypotheses and significance

:::def Null hypothesis
A statement that there is no significant difference between the things being compared (or no correlation, or no difference between observed and expected results). The test calculates how likely the data are if this statement is true.
:::

You write the null hypothesis *before* you do the test, and it always says "no". The test then decides whether you can **reject** it. For each test it takes the same form:

| test | null hypothesis |
|---|---|
| chi-squared | There is no significant difference between the observed and the expected results. |
| t-test | There is no significant difference between the mean of (sample 1) and the mean of (sample 2). |
| Pearson / Spearman | There is no correlation between (variable 1) and (variable 2). |

Every test turns your data into one number (the **calculated value**, such as \(\chi^2\), \(t\), \(r\) or \(r_s\)) and you compare it with a **critical value** from a table. The table is given in the question. Which row to use depends on the **degrees of freedom**, which you must work out yourself.

:::def Degrees of freedom
A number that depends on the size of the data set and decides which row of the table of critical values you use. For \(\chi^2\) it is the number of classes minus 1; for the t-test it is \(n_1 + n_2 - 2\).
:::

:::def Critical value
The value in a statistical table that your calculated value must reach (or pass) for the result to be significant at the stated probability, usually \(p = 0.05\).
:::

:::key What to write for each test (at \(p = 0.05\))
- **Chi-squared**: if calculated \(\chi^2\) is **less than** the critical value, the difference between observed and expected is **not significant**, it is due to chance, and the null hypothesis is accepted. If **greater**, the difference is **significant**, the null hypothesis is rejected, and the observed results do not fit the expected ones.
- **t-test**: if calculated \(t\) is **greater than** the critical value, there is a **significant difference** between the means (the null hypothesis is rejected). If less, there is no significant difference.
- **Pearson or Spearman**: if the **size** of \(r\) or \(r_s\) (ignoring the sign) is **greater than** the critical value, there is a **significant correlation**: positive if the value is positive, negative if it is negative. If less, there is no significant correlation.
:::

:::warn Words that lose marks
**"Significant" does not mean "important" or "large".** It means unlikely to be due to chance alone. A tiny difference can be significant in a big sample. **Never write "proved".** A test shows that a difference is unlikely to be chance, not that a hypothesis is certain. **"No significant difference" is not "the same".** And a result either is or is not significant: do not write "nearly significant".
:::

## Choosing the right test

Each test answers a different question and is valid only for certain data and conditions. If you use the wrong test, the answer is meaningless.

:::key Choosing a test
| question | data | test | conditions for validity |
|---|---|---|---|
| Do observed numbers fit the numbers expected? | nominal (frequencies in classes) | chi-squared | one row or column of counts; expected values from a ratio or from "no preference" |
| Do two sample means differ? | continuous | t-test | two samples; each approximately normally distributed; similar standard deviations; fewer than 30 values is allowed |
| Do two variables change together in a straight line? | continuous | Pearson's correlation | both normally distributed; scatter graph shows a possible linear relationship; at least 5 pairs, ideally 10 or more |
| Do two variables change together (rising or falling, not necessarily straight)? | ordinal, ranked, or continuous but not normal | Spearman's rank correlation | more than 5 pairs, ideally 10 to 30; points independent; random sample |
:::

:::eg A student made five studies. For each, name the statistical test and give one reason. (a) The numbers of pea plants with round and with wrinkled seeds, compared with a 3 : 1 ratio. (b) The lengths of 15 fish from a lake and 12 from a river, both normally distributed with similar spread. (c) The number of snails and the pH in 12 ponds, where the counts are not normally distributed. (d) Wing length and body mass in 20 beetles, both normally distributed and the scatter graph is a straight band. (e) Eight stretches of river ranked from 1 to 8 for cleanliness, and the number of mayfly larvae in each.
(a) Chi-squared: the data are nominal frequencies compared with an expected ratio. [B1]

(b) t-test: two samples of continuous, normally distributed data with similar spread. [B1]

(c) Spearman's rank: the counts are not normal, so ranks are used. [B1]

(d) Pearson's correlation: both variables are continuous and normal and the relationship looks linear. [B1]

(e) Spearman's rank: one variable is ordinal (a ranking), so a rank test is needed. [B1]
:::

## The chi-squared test

You met this test in [Dihybrid crosses and the chi-squared test](#bio.dihybrid). Use it for **counts in classes** when you can work out the numbers you expect.

:::formula Chi-squared (provided in the exam)
\[\chi^2 = \sum \frac{(O - E)^2}{E}\]
\(O\) = observed number in a class, \(E\) = expected number in that class. Degrees of freedom \(=\) number of classes \(- 1\) (not given).
:::

The expected number in each class comes from the hypothesis. For "no preference" between \(c\) classes, \(E = \text{total} \div c\). For a ratio such as 3 : 1, share the total in that ratio. Use the real counts, never percentages. The syllabus tests only one row (or one column) of data.

:::eg Woodlice were placed in a choice chamber with four parts: damp and dark, damp and light, dry and dark, dry and light. After 10 minutes 180 woodlice were counted: 66 in damp and dark, 38 in damp and light, 54 in dry and dark and 22 in dry and light. Test whether the woodlice are spread evenly between the four parts.
**Null hypothesis.** There is no significant difference between the observed number of woodlice in each part and the number expected if they are spread evenly.

**Expected.** If there is no preference, each part should hold \(180 \div 4 = 45\) woodlice.

| part | O | E | \((O - E)^2 \div E\) |
|---|---|---|---|
| damp, dark | 66 | 45 | 9.80 |
| damp, light | 38 | 45 | 1.09 |
| dry, dark | 54 | 45 | 1.80 |
| dry, light | 22 | 45 | 11.76 |

\[\begin{aligned} \chi^2 &= 9.80 + 1.09 + 1.80 + 11.76 \\ &= 24.4 \end{aligned}\]

**Degrees of freedom.** \(4 - 1 = 3\). The critical value at \(p = 0.05\) is 7.81.

**Conclusion.** \(24.4 > 7.81\), so there is a significant difference between the observed and expected numbers. The null hypothesis is rejected: the woodlice are not spread evenly. The numbers show that they prefer the dark (120 against 60) and, within the dark, the damp part (66 against 54).
:::

The widget below does the sum for you. Change the counts and watch the \(\chi^2\) value and conclusion change; try making the counts nearly equal.

:::html
<div class="widget" data-w="bio-chisq" data-obs="66,38,54,22" data-ratio="1:1:1:1" data-names="damp and dark,damp and light,dry and dark,dry and light"></div>
:::

## The t-test

Use the t-test to compare the **means of two samples** of continuous, normally distributed data with similar standard deviations. [Variation](#bio.variation) has the first worked examples; here is the full routine again with new data.

:::formula t-test (provided in the exam)
\[t = \frac{|\bar{x}_1 - \bar{x}_2|}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}\]
\(|\ |\) means ignore the sign. Degrees of freedom \(= n_1 + n_2 - 2\) (not given).
:::

In a Paper 4 or 5 question the standard deviations are often not given. You may be given the means and the sum of the squared deviations, \(\sum (x - \bar{x})^2\), for each sample and asked to finish. Calculate \(s\) for each sample first.

:::eg The heart rate of eight water fleas (Daphnia) was counted in beats per minute at 15 °C and at 25 °C. Part of the working is given: at 15 °C the mean was 151 beats per minute and \(\sum (x - \bar{x})^2 = 832\); at 25 °C the mean was 187 and \(\sum (x - \bar{x})^2 = 892\). Complete the t-test.
**Null hypothesis.** There is no significant difference between the mean heart rate at 15 °C and at 25 °C.

**Standard deviations.** Use \(n - 1 = 7\) for each sample.

\[\begin{aligned} s_1 &= \sqrt{\frac{832}{7}} = 10.9 \\ s_2 &= \sqrt{\frac{892}{7}} = 11.3 \end{aligned}\]

The two standard deviations are similar, so the t-test is suitable.

**t.**

\[\begin{aligned} t &= \frac{|151 - 187|}{\sqrt{\dfrac{118.86}{8} + \dfrac{127.43}{8}}} \\ &= \frac{36}{\sqrt{14.857 + 15.929}} \\ &= \frac{36}{5.548} = 6.49 \end{aligned}\]

**Degrees of freedom.** \(8 + 8 - 2 = 14\). The critical value at \(p = 0.05\) is 2.14.

**Conclusion.** \(6.49 > 2.14\), so there is a significant difference between the mean heart rates. The null hypothesis is rejected. The difference is unlikely to be due to chance: the heart rate is higher at 25 °C (mean 187) than at 15 °C (mean 151).
:::

The raw readings behind that example are in the widget. Change one reading to an extreme value and see how \(t\) falls when the spread rises.

:::html
<div class="widget" data-w="bio-ttest" data-a="134, 140, 146, 150, 152, 158, 162, 166" data-b="172, 176, 181, 184, 189, 191, 196, 207"></div>
:::

## Correlation

The chi-squared and t-tests ask whether groups differ. **Correlation** asks whether two measured variables change together.

:::def Correlation
A relationship in which two variables tend to change together. In a positive correlation both increase; in a negative correlation one increases as the other decreases. The size of a correlation coefficient shows how closely the points follow the pattern.
:::

A **scatter graph** shows the pairs of values as points. The independent variable (or the one you think affects the other) goes on the x-axis. A correlation coefficient, \(r\) for Pearson and \(r_s\) for Spearman, runs from \(-1\) (perfect negative) through 0 (no correlation) to \(+1\) (perfect positive). A value near \(\pm 1\) means the points lie close to the pattern; a value near 0 means they are scattered. The sign gives the direction, but the **size** is compared with the critical value.

### Pearson's linear correlation

:::formula Pearson's correlation coefficient (provided in the exam)
\[r = \frac{\sum xy - n\bar{x}\bar{y}}{(n-1)\,s_x s_y}\]
\(n\) = number of pairs, \(\bar{x}\), \(\bar{y}\) = the means, \(s_x\), \(s_y\) = the standard deviations (with \(n - 1\)). The critical value depends on \(n\) (given in a table).
:::

You may be given \(\sum xy\), the means and the standard deviations and be asked to finish the calculation.

:::eg Soil nitrate (mg per kg of soil) and the height of grass (cm) were measured at seven sites. Part of the working is given: \(n = 7\), \(\bar{x} = 40\), \(\bar{y} = 25\), \(\sum xy = 8230\), \(s_x = 21.602\), \(s_y = 9.747\). Complete the test of correlation. The critical value for \(n = 7\) at \(p = 0.05\) is 0.754.
**Null hypothesis.** There is no correlation between soil nitrate and the height of grass.

**Numerator.**

\[\begin{aligned} \sum xy - n\bar{x}\bar{y} &= 8230 - 7 \times 40 \times 25 \\ &= 8230 - 7000 \\ &= 1230 \end{aligned}\]

**Denominator and r.**

\[\begin{aligned} (n - 1)\,s_x s_y &= 6 \times 21.602 \times 9.747 \\ &= 1263.3 \\ r &= \frac{1230}{1263.3} = 0.974 \end{aligned}\]

**Conclusion.** \(0.974 > 0.754\), so there is a significant positive correlation between soil nitrate and the height of the grass. The null hypothesis is rejected. Pearson's test is valid only if both variables are normally distributed and the scatter graph is roughly a straight line.
:::

### Spearman's rank correlation

:::formula Spearman's rank correlation coefficient (provided in the exam)
\[r_s = 1 - \frac{6\sum D^2}{n^3 - n}\]
\(D\) = the difference between the two ranks of a pair, \(n\) = number of pairs.
:::

Rank each variable separately from smallest (rank 1) to largest. Ties share the mean of the ranks they would have taken. Then find \(D\) and \(D^2\) for each pair.

:::eg The number of barnacles per 100 cm² was counted on rock at nine heights above the low-tide mark. The counts are not normally distributed. Test for a correlation between height on the shore and the number of barnacles. The critical value for \(n = 9\) at \(p = 0.05\) is 0.700.
**Null hypothesis.** There is no correlation between the height on the shore and the number of barnacles.

| height / m | barnacles per 100 cm² | rank (height) | rank (barnacles) | \(D\) | \(D^2\) |
|---|---|---|---|---|---|
| 0.5 | 210 | 1 | 9 | −8 | 64 |
| 0.9 | 180 | 2 | 7 | −5 | 25 |
| 1.2 | 195 | 3 | 8 | −5 | 25 |
| 1.8 | 120 | 4 | 6 | −2 | 4 |
| 2.1 | 96 | 5 | 4 | 1 | 1 |
| 2.6 | 110 | 6 | 5 | 1 | 1 |
| 3.0 | 40 | 7 | 2 | 5 | 25 |
| 3.4 | 52 | 8 | 3 | 5 | 25 |
| 4.1 | 18 | 9 | 1 | 8 | 64 |

\(\sum D^2 = 234\).

\[\begin{aligned} r_s &= 1 - \frac{6 \times 234}{9^3 - 9} \\ &= 1 - \frac{1404}{720} \\ &= -0.95 \end{aligned}\]

**Conclusion.** The size of \(r_s\) is 0.95, which is greater than 0.700, so there is a significant negative correlation: the number of barnacles falls with height up the shore. The null hypothesis is rejected.
:::

### Correlation is not causation

A significant correlation shows that two variables change together. It does **not** show that one causes the other. The reasons are always the same three.

- A **third factor** may cause both. On the shore, time out of the water affects barnacle feeding *and* the temperature and drying that barnacles face; height only stands for those.
- The **cause may act the other way** round.
- It may be **chance**, especially with few points.

Only an experiment, in which one variable is changed and the others are kept the same, can show cause. Write "there is a significant negative correlation between … and …", then give a possible explanation with "may be because".

## Finishing a partly completed calculation

:::exam Partly completed calculations
Papers 4 and 5 will not ask you to do all the steps of \(s\), \(t\), \(r\) or \(r_s\) from scratch. A typical question prints the means, the sums or part of a table and says "complete the calculation". Do this: (1) write the formula; (2) substitute the numbers given and the ones you work out, one line at a time; (3) give the answer to 3 significant figures (one more than the data, as the syllabus allows); (4) work out the degrees of freedom yourself; (5) compare with the critical value and write the conclusion in words that mention the variables. Working earns the method mark even if the arithmetic slips.
:::

:::eg Spot the error: a chi-squared test. [3]
A gardener crossed two heterozygous plants and expected 3 purple : 1 white. She counted 51 purple and 29 white (80 in total). Test whether the results fit the expected ratio. A student wrote this answer.

Line 1: The expected numbers are 60 purple and 20 white, so \(\chi^2 = \dfrac{9^2}{60} + \dfrac{9^2}{20} = 5.40\).
Line 2: There are 2 classes, so the degrees of freedom are 1 and the critical value is 3.84.
Line 3: \(5.40 > 3.84\), so we accept the null hypothesis: the results fit a 3 : 1 ratio.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: when the calculated \(\chi^2\) is greater than the critical value the difference is significant and the null hypothesis is rejected, so the results do not fit 3 : 1. The mark is lost [B0].**

Correct Line 3: "\(5.40 > 3.84\), so there is a significant difference between the observed and expected numbers. The null hypothesis is rejected and the results do not fit a 3 : 1 ratio." With that change the answer scores 3 marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State whether each is nominal, ordinal or continuous data: (a) blood group; (b) the mass of a leaf in mg; (c) the abundance of a moss given as 1 (rare) to 5 (very common).
A: (a) Nominal. (b) Continuous. (c) Ordinal.
Q: The numbers of eggs in seven nests were 3, 4, 4, 5, 4, 6 and 9. Calculate the mean, median, mode and range.
A: Mean \(= 35 \div 7 = 5\). The ordered values are 3, 4, 4, 4, 5, 6, 9, so the median is 4. The mode is 4. The range is \(9 - 3 = 6\).
Q: A sample of 16 plants has a mean height of 52 cm and a standard deviation of 4.2 cm. Calculate the standard error and the 95% confidence interval.
A: \(\mathrm{SE} = 4.2 \div \sqrt{16} = 1.05\) cm. The interval is \(52 \pm 2 \times 1.05 = 52 \pm 2.1\), so 49.9 to 54.1 cm.
Q: Give the degrees of freedom for (a) a chi-squared test with five classes; (b) a t-test on samples of 12 and 9 values.
A: (a) \(5 - 1 = 4\). (b) \(12 + 9 - 2 = 19\).
Q: Two heterozygous pea plants (\(Tt \times Tt\)) are crossed. Find the probability that an offspring is dwarf (\(tt\)), and the probability that none of three offspring is dwarf.
A: Dwarf: \(\tfrac14\). Tall (not dwarf): \(\tfrac34\). None of three dwarf: \(\left(\tfrac34\right)^3 = \tfrac{27}{64}\) (0.42).
Q: Write the null hypothesis for a Spearman's rank test on the fur length of mice and the altitude at which they were caught.
A: There is no correlation between fur length and altitude.
Q: A correlation of \(r = -0.82\) is found from 10 pairs. The critical value for \(n = 10\) at \(p = 0.05\) is 0.632. State the conclusion.
A: The size of \(r\) (0.82) is greater than 0.632, so there is a significant negative correlation. The null hypothesis is rejected.
Q: The 95% confidence interval bars of two means are 12.0 ± 3.0 and 14.0 ± 3.0. Do the bars overlap? What can you say about the difference?
A: The intervals are 9.0 to 15.0 and 11.0 to 17.0, so they overlap. The difference is probably not significant: it could be due to chance. A t-test would decide.
Q: Across 20 lakes, the number of fish species is positively correlated with the area of the lake. A student says that making a lake larger will increase the number of species. Give one reason why the correlation does not prove this.
A: A third factor could cause both, for example larger lakes also have more habitats, a greater variety of depths and more food, so area may not be the cause. (Or: the correlation could be chance.)
Q: Why is the sample standard deviation calculated with \(n - 1\) and not \(n\)?
A: The values in a sample are closer to their own mean than to the true population mean, so dividing by \(n\) would underestimate the spread of the population. Using \(n - 1\) corrects this.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The masses of eight snails have a mean of 12.5 g and \(\sum (x - \bar{x})^2 = 63.0\). Calculate (a) the standard deviation, (b) the standard error and (c) the 95% confidence interval for the mean mass.
H: Divide the sum of squares by \(n - 1\) before taking the square root.
A: (a) \(s = \sqrt{63.0 \div 7}\) [M1] \(= 3.00\) g [A1]
(b) \(\mathrm{SE} = 3.00 \div \sqrt{8} = 1.06\) g [A1]
(c) \(12.5 \pm 2 \times 1.06 = 12.5 \pm 2.12\), so 10.4 g to 14.6 g [A1]
Q: [4 marks] ★ A scientist expected snail shells to be striped and unstriped in a 3 : 1 ratio. Of 160 snails, 118 were striped and 42 were unstriped. Test the fit using a chi-squared test. The critical value for the correct number of degrees of freedom at \(p = 0.05\) is 3.84.
H: Find the expected numbers by sharing 160 in the ratio 3 : 1.
A: Expected: 120 striped and 40 unstriped. [B1]
\(\chi^2 = \dfrac{(118 - 120)^2}{120} + \dfrac{(42 - 40)^2}{40}\) [M1] \(= 0.033 + 0.100 = 0.13\) [A1]
\(0.13 < 3.84\), so there is no significant difference between the observed and expected numbers; the results fit a 3 : 1 ratio and the null hypothesis is accepted. [B1]
Q: [6 marks] ★★ The mass of 1000 grains was measured for samples of two varieties of wheat. Variety A: \(n = 10\), mean 42.6 g, \(s = 3.1\) g. Variety B: \(n = 12\), mean 38.9 g, \(s = 3.7\) g. The data are normally distributed. Complete a t-test to find whether the means differ significantly.
H: Write the null hypothesis first. Then substitute into the formula, and work out the degrees of freedom yourself.
H: Compare with a critical value of 2.09 for the degrees of freedom you find.
A: Null hypothesis: there is no significant difference between the mean grain mass of the two varieties. [B1]
\(t = \dfrac{|42.6 - 38.9|}{\sqrt{\dfrac{3.1^2}{10} + \dfrac{3.7^2}{12}}} = \dfrac{3.7}{\sqrt{0.961 + 1.141}}\) [M1]
\(= \dfrac{3.7}{1.450} = 2.55\) [A1]
Degrees of freedom \(= 10 + 12 - 2 = 20\) [B1]
\(2.55 > 2.09\), so there is a significant difference between the means. [B1]
The null hypothesis is rejected: variety A has the greater mean grain mass, and the difference is unlikely to be due to chance. [B1]
Q: [5 marks] ★★ Algae were grown in three culture solutions. The mean number of cells (× 10⁴ per cm³) after 6 days, with the 95% confidence interval, was: solution P, 52 ± 6; solution Q, 61 ± 7; solution R, 83 ± 8. (a) Describe the effect of the solution on cell number. (b) Which differences are probably significant? Explain how you decided. (c) The interval for solution Q was found from 10 flasks. Calculate the standard deviation of the cell numbers in solution Q.
H: A 95% confidence interval is \(\bar{x} \pm 2\) SE, so the figure after the ± sign is 2 SE.
H: For (c), SE \(= s \div \sqrt{n}\), so \(s = \) SE \(\times \sqrt{n}\).
A: (a) The number of cells increases from 52 (solution P) to 61 (solution Q) to 83 × 10⁴ per cm³ (solution R). [B1]
(b) P (46 to 58) and Q (54 to 68) overlap, so the difference between P and Q is probably not significant. [B1]
R (75 to 91) overlaps neither P nor Q, so R is probably significantly different from both. [B1]
(c) \(\mathrm{SE} = 7 \div 2 = 3.5\) [M1]; \(s = 3.5 \times \sqrt{10} = 11.1\) × 10⁴ per cm³ [A1]
Q: [5 marks] ★★ Wing length (mm) and body mass (g) were measured in six beetles. Part of the working is given: \(n = 6\), \(\bar{x} = 12.0\), \(\bar{y} = 4.0\), \(\sum xy = 298.4\), \(s_x = 2.366\), \(s_y = 0.934\). Finish the calculation of Pearson's correlation coefficient and state whether it is significant, if the critical value for \(n = 6\) at \(p = 0.05\) is 0.811.
H: Numerator: \(\sum xy - n\bar{x}\bar{y}\). Denominator: \((n - 1)\,s_x s_y\).
A: Numerator \(= 298.4 - 6 \times 12.0 \times 4.0 = 10.4\) [M1]
Denominator \(= 5 \times 2.366 \times 0.934 = 11.05\) [M1]
\(r = 10.4 \div 11.05 = 0.941\) [A1]
\(0.941 > 0.811\), so the correlation is significant [B1]
and positive: beetles with longer wings tend to have a greater body mass. [B1]
Q: [6 marks] ★★★ The temperature of eight stretches of a stream and the number of caddis fly larvae in each were recorded.

| temperature / °C | larvae per sample |
|---|---|
| 8 | 48 |
| 9 | 52 |
| 11 | 41 |
| 12 | 35 |
| 14 | 38 |
| 15 | 22 |
| 17 | 25 |
| 19 | 14 |

(a) Explain why Spearman's rank correlation is more suitable than Pearson's if the counts are not normally distributed. (b) Calculate \(r_s\). (c) The critical value for \(n = 8\) at \(p = 0.05\) is 0.738. State the conclusion.
H: Rank each column from smallest (1) to largest. Then find \(D\), square it and add.
A: (a) Spearman's test does not need normally distributed data, because it uses ranks, and Pearson's test is valid only for normally distributed data. [B1]
(b) Ranks of temperature 1 to 8; ranks of larvae 7, 8, 6, 4, 5, 2, 3, 1. \(D\) values are −6, −6, −3, 0, 0, 4, 4, 7, so \(\sum D^2 = 162\) (the squares are 36, 36, 9, 0, 0, 16, 16 and 49). [M1]
\(r_s = 1 - \dfrac{6 \times 162}{8^3 - 8}\) [M1] \(= 1 - 1.929 = -0.929\) [A1]
(c) The size of \(r_s\) (0.929) is greater than 0.738, so there is a significant negative correlation: the number of larvae falls as the temperature rises. [B1]
The null hypothesis is rejected. [B1]
Q: [6 marks] (#bio.variation) ★★★ The beak depth of a sample of 50 finches from one island had a mean of 9.4 mm and a standard deviation of 0.6 mm. (a) Calculate the standard error and the 95% confidence interval for the mean. (b) Explain why a sample of 200 finches would give a more reliable estimate of the mean. (c) Assuming that beak depth is normally distributed, between which values would about 95% of the finches lie?
H: For (c) the standard deviation, not the standard error, describes the individuals.
A: (a) \(\mathrm{SE} = 0.6 \div \sqrt{50}\) [M1] \(= 0.085\) mm [A1]
Interval: \(9.4 \pm 2 \times 0.085 = 9.23\) to \(9.57\) mm [A1]
(b) \(\mathrm{SE} = s \div \sqrt{n}\), so a larger \(n\) gives a smaller SE. [B1]
The sample mean is then likely to be closer to the true mean of the population (a narrower confidence interval). [B1]
(c) \(9.4 \pm 2 \times 0.6\), so 8.2 mm to 10.6 mm. [B1]
Q: [7 marks] (#bio.dihybrid) ★★★ In maize, purple kernels (dominant) and smooth kernels (dominant) are controlled by two genes on different chromosomes. Two plants heterozygous for both genes were crossed and gave 160 kernels: 96 purple smooth, 28 purple wrinkled, 25 yellow smooth and 11 yellow wrinkled. (a) Show that the probability that a kernel is purple and smooth is \(\tfrac9{16}\). (b) Use a chi-squared test to decide whether the results fit a 9 : 3 : 3 : 1 ratio. The critical value for the correct degrees of freedom at \(p = 0.05\) is 7.81.
H: For (a), each gene is inherited independently, so multiply the two probabilities.
H: For (b), share 160 in the ratio 9 : 3 : 3 : 1 to get the expected numbers.
A: (a) The probability of purple is \(\tfrac34\) and the probability of smooth is \(\tfrac34\). [B1]
The genes assort independently, so multiply: \(\tfrac34 \times \tfrac34 = \tfrac9{16}\). [B1]
(b) Expected: 90, 30, 30 and 10. [B1]
\[\begin{aligned} \chi^2 &= \dfrac{(96-90)^2}{90} + \dfrac{(28-30)^2}{30} \\ &\quad + \dfrac{(25-30)^2}{30} + \dfrac{(11-10)^2}{10} \end{aligned}\] [M1]
\(= 0.40 + 0.13 + 0.83 + 0.10 = 1.47\) [A1]
Degrees of freedom \(= 4 - 1 = 3\). \(1.47 < 7.81\), so there is no significant difference between observed and expected numbers. [B1]
The results fit a 9 : 3 : 3 : 1 ratio, so the null hypothesis is accepted. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Two populations of grass (A and B) each have a sample of 25 plants with the same mean height of 50.0 cm. In A the standard deviation is 4.0 cm; in B it is 12.0 cm. (a) Calculate the standard error and the 95% confidence interval of the mean for each. (b) Explain what the results show about the reliability of each mean and about the plants in each population.
H: Work out SE for A and for B separately, then compare the widths of the intervals.
H: For (b), separate the reliability of the mean (SE) from the variation between plants (SD).
A: (a) \(\mathrm{SE} = s \div \sqrt{n}\), with \(\sqrt{25} = 5\) [M1]
For A, SE \(= 4.0 \div 5 = 0.80\) cm [A1]; for B, SE \(= 12.0 \div 5 = 2.4\) cm [A1]
Intervals: A is 48.4 to 51.6 cm and B is 45.2 to 54.8 cm. [A1]
(b) The mean of A is more reliable: its interval is narrower (SE 0.80 against 2.4). [B1]
The plants in B vary more in height, because its standard deviation is three times as large, so its sample mean is a less precise estimate even with the same sample size. [B1]
Q: [6 marks] ★★★ A research team tested 20 different plant extracts, one at a time, for an effect on the growth of a fungus. Each test compared the extract with a control using a t-test at \(p = 0.05\). Only one extract gave a significant difference. (a) If none of the extracts has any real effect, state the probability that one particular test gives a significant result by chance. (b) Calculate the probability that at least one of the 20 tests gives a significant result by chance. (c) Suggest two ways in which the team could check whether the significant extract really inhibits the fungus.
H: For (b), find the probability that all 20 tests are not significant, then subtract from 1.
A: (a) 0.05 (5%). [B1]
(b) The probability that one test is not significant is 0.95, so all 20 not significant is \(0.95^{20} = 0.358\) [M1]; the probability of at least one significant is \(1 - 0.358 = 0.64\) [A1]
So one significant result in 20 tests is what chance alone is likely to give. [B1]
(c) Repeat the investigation on that extract with new samples (and more replicates) to see if the result is repeatable. [B1]
Use a stricter significance level, such as \(p = 0.01\), or test a range of concentrations to see if the effect increases with concentration. [B1]
:::

:::quiz
? A student counts the number of beetles with each of three wing-case colours in a sample of 60. What type of data is this?
+ nominal
- ordinal
- continuous
- normally distributed
> The beetles are sorted into named categories (colours) and counted. The categories have no natural order, so the data are nominal.
? A sample has a standard deviation of 8.0. The sample size is increased from 25 to 100 and the standard deviation stays at 8.0. What happens to the standard error?
+ It halves, from 1.6 to 0.8.
- It stays the same, because the standard deviation is the same.
- It falls to a quarter, from 1.6 to 0.4.
- It doubles, because there are more values.
> SE \(= s \div \sqrt{n}\). Four times the sample size doubles \(\sqrt{n}\), so the SE halves. It does not fall to a quarter, because of the square root.
? A chi-squared test has six classes. How many degrees of freedom are used to find the critical value?
+ 5
- 6
- 4
- 10
> For chi-squared, degrees of freedom = number of classes − 1 = 5. Using 6 forgets to subtract 1.
? A t-test gives a calculated \(t\) of 1.80. The critical value at \(p = 0.05\) is 2.10. Which conclusion is correct?
+ There is no significant difference between the means; any difference could be due to chance.
- There is a significant difference between the means.
- The means are the same.
- The difference is almost significant, so the null hypothesis is probably false.
> The calculated t is less than the critical value, so the difference is not significant. "Not significant" does not mean "the same", and a result is not "almost" significant.
? Which test should be used to look for a relationship between the abundance of a moss recorded on a scale of 1 to 5 and the depth of soil?
+ Spearman's rank correlation
- Pearson's correlation
- the t-test
- the chi-squared test
> The moss data are ordinal (a ranked scale), so a rank test is needed. Pearson's correlation needs continuous, normally distributed data.
? What does \(p < 0.05\) mean for a statistical test?
+ There is less than a 5% probability that the result arose by chance alone.
- There is a 95% probability that the hypothesis is true.
- The difference is large and important.
- The experiment is free from error.
> \(p\) is the probability of getting a result at least this extreme by chance alone if the null hypothesis is true. It says nothing about the size or importance of the difference, or about errors in the method.
? The 95% confidence interval error bars for two means overlap. What is the best conclusion?
+ The difference is probably not significant, but a statistical test is needed to be sure.
- The difference is significant.
- The two means are exactly equal.
- The standard deviations must be equal.
> Overlapping 95% confidence intervals suggest the difference could be due to chance. It is a rule of thumb, not a test, and the means are only probably not different.
? Spearman's rank correlation for ten pairs gives \(r_s = -0.71\). The critical value is 0.648. What is the conclusion?
+ There is a significant negative correlation.
- There is no significant correlation, because the value is negative.
- There is a significant positive correlation.
- The null hypothesis is accepted.
> The sign shows the direction, and only the size is compared with the critical value. 0.71 is greater than 0.648, so the correlation is significant and negative, and the null hypothesis is rejected.
? A scientist finds a significant positive correlation between the number of sheep and the number of flies on farms. What can she conclude?
+ The two variables change together; a third factor, such as farm size, may cause both.
- The sheep cause the flies.
- The flies cause the number of sheep to increase.
- The correlation is not real.
> A significant correlation shows that the variables change together, not which causes which. Only a controlled experiment shows cause.
:::

:::checklist What you can now do
- [ ] I can classify data as nominal, ordinal or continuous and explain how that affects the test I use.
- [ ] I can explain the principles of sampling and why a sample must be random, large enough and representative.
- [ ] I can use probability to describe genetic ratios and combine probabilities with the "and" and "or" rules.
- [ ] I can explain what \(p = 0.05\) means and why a result is significant or not significant.
- [ ] I can recognise normal and non-normal distributions and calculate the mean, median, mode and range.
- [ ] I can calculate a sample standard deviation, standard error and 95% confidence interval, and say what each shows.
- [ ] I can plot and read error bars and use overlap as a guide to significance.
- [ ] I can write a null hypothesis for each test and the conclusion in the correct words.
- [ ] I can choose between the chi-squared test, the t-test, Pearson's correlation and Spearman's rank correlation, and state the conditions for each.
- [ ] I can calculate or finish the chi-squared test, the t-test, Pearson's \(r\) and Spearman's \(r_s\), working out the degrees of freedom and using a table of critical values.
- [ ] I can explain why a correlation does not show cause.
:::

:::recap
- Data are nominal (named categories), ordinal (ranked) or continuous (measured). Samples must be random, large enough, representative and independent.
- Probabilities multiply for "and" and add for "or". \(p = 0.05\): a 5% probability that the result is due to chance alone.
- Mean, median, mode, range. Normal distribution: symmetrical, mean = median = mode. In a skewed distribution the mean is pulled towards the tail.
- \(s = \sqrt{\sum (x-\bar{x})^2 \div (n-1)}\); SE \(= s \div \sqrt{n}\); 95% CI \(= \bar{x} \pm 2\) SE. SD shows spread of the data, SE the reliability of the mean.
- Error bars: overlapping 95% CI bars suggest the difference is probably not significant; bars that do not overlap suggest it is significant. A test decides.
- Null hypothesis: no significant difference (or no correlation). Chi-squared: calculated less than critical means not significant. t, \(r\), \(r_s\): size greater than critical means significant.
- Degrees of freedom: chi-squared, classes − 1; t-test, \(n_1 + n_2 - 2\). They are not given.
- Chi-squared: nominal counts, observed v expected. t-test: two sample means, continuous, normal, similar SD. Pearson: continuous, normal, linear. Spearman: ranked or not normal.
- Correlation is not causation: a third factor, the reverse direction, or chance.
:::

:::links
- read: [CAIE A Level Biology: practical skills and statistics](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/practical-skills/) · Physics & Maths Tutor · free notes and questions on data handling and statistical tests
- practise: [Topic questions (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topic-questions/) · Save My Exams · exam questions with mark schemes by topic [paid]
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [Khan Academy Biology](https://www.khanacademy.org/science/biology) · Khan Academy · free lessons if you want another explanation of the ideas behind sampling and variation
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · real questions that use these tests [unofficial]

Links checked 24 October 2026.
:::

Next: [Planning investigations (Paper 5)](#bio.planning) shows how to design an investigation whose results you can analyse with these methods.
