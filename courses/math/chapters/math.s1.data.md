@chapter math.s1.data
@title Representing and summarising data
@level a2
@paper CAIE P5 (check your specification for other boards)
@time 8–10 hours
@summary How to display data (stem-and-leaf diagrams including back-to-back, box plots, histograms with unequal class widths, cumulative frequency graphs) and how to summarise it: mean, median, mode, quartiles, interquartile range, variance and standard deviation from raw, grouped and coded data, and from two data sets combined.

:::why
Data arrives as a long list of numbers that nobody can read. A good diagram shows the shape at a glance, and a few well-chosen numbers say where the data is centred and how spread out it is. Those two ideas, centre and spread, are what you use to compare two bus routes, two drugs or two batches of components. This chapter gives you the standard tools and tells you which one to use and why.
:::

**Before you start**, you need fractions and percentages from [Numbers from scratch](#math.f.numbers), substitution and rearranging from [Algebra from scratch](#math.f.algebra), and the idea of a scale on a graph from [Graphs from scratch](#math.f.graphs).

:::try Warm-up
Q: A class of 40 students has 7 left-handed students. What percentage is that? (from [Numbers from scratch](#math.f.numbers))
A: \(\dfrac{7}{40} = 0.175\), so \(17.5\%\).
Q: Rearrange \(\bar x = \dfrac{\sum x}{n}\) to find \(\sum x\) when \(\bar x = 12.5\) and \(n = 8\). (from [Algebra from scratch](#math.f.algebra))
A: Multiply both sides by \(n\): \(\sum x = n\bar x = 8 \times 12.5 = 100\).
Q: Find the gradient of the straight line through \((10, 12)\) and \((20, 42)\). (from [Graphs from scratch](#math.f.graphs))
A: \(\dfrac{42 - 12}{20 - 10} = 3\). You will use this idea to read a median from a cumulative frequency graph.
:::

## Types of data and choosing a diagram

:::def Discrete, continuous and grouped data
**Discrete** data takes separate values, usually counts (number of children). **Continuous** data can take any value in a range, usually measurements (time, mass, height). **Grouped** data is sorted into classes, so you no longer know the exact values.
:::

| Diagram | Best for | Strengths | Weaknesses |
|---|---|---|---|
| Stem-and-leaf | Small sets (up to about 50 values) | Keeps every value; shows shape; easy to read median and quartiles | Awkward for large sets; needs a key |
| Back-to-back stem-and-leaf | Comparing two small sets | Shows both shapes against one stem | Same as above |
| Box plot | Comparing sets | Shows median, quartiles and range at a glance; compact | Hides the shape between the quartiles and the individual values |
| Histogram | Large continuous grouped data | Shows shape; copes with unequal class widths | Loses the individual values |
| Cumulative frequency graph | Large grouped data | Reads off median, quartiles, percentiles, and proportions above or below a value | Does not show shape directly |

## Stem-and-leaf diagrams

A stem-and-leaf diagram splits each value into a **stem** (the leading digits) and a **leaf** (the last digit). Put the leaves in order, and always include a **key**.

:::eg The journey times, in minutes, of 15 trips by route A were 23, 31, 28, 35, 42, 27, 31, 38, 45, 29, 33, 36, 31, 24 and 40. Draw an ordered stem-and-leaf diagram and find the median, quartiles, interquartile range, mode and range.
| Stem | Leaves |
|---|---|
| 2 | 3 4 7 8 9 |
| 3 | 1 1 1 3 5 6 8 |
| 4 | 0 2 5 |

Key: 3 | 1 means 31 minutes.

There are \(n = 15\) values. The median is the \(8^{\text{th}}\) value, which is **31**. For the quartiles, take the median of each half (leaving out the middle value): the lower half is 23, 24, 27, 28, 29, 31, 31, so \(Q_1 = 28\); the upper half is 33, 35, 36, 38, 40, 42, 45, so \(Q_3 = 38\). The interquartile range is \(\text{IQR} = Q_3 - Q_1 = 10\). The mode is **31** (it appears three times) and the range is \(45 - 23 = 22\).
:::

To compare two sets, write a **back-to-back** diagram: the two sets share the stems, with one set's leaves on each side. The leaves of the left side are written in order **reading outwards from the stem**.

:::eg Route B took 26, 30, 32, 34, 35, 35, 37, 38, 39, 41 and 44 minutes. Draw a back-to-back diagram with route A.
| Route A | | Route B |
|---:|:---:|:---|
| 9 8 7 4 3 | 2 | 6 |
| 8 6 5 3 1 1 1 | 3 | 0 2 4 5 5 7 8 9 |
| 5 2 0 | 4 | 1 4 |

Key: for A, 1 | 3 means 31 minutes; for B, 3 | 0 means 30 minutes.

Route B's median (the \(6^{\text{th}}\) of 11 values) is 35, against 31 for A. B is slower on average, but its values are more tightly grouped.
:::

## Median, quartiles and box plots

:::key Five-number summary and the box plot
The **five-number summary** is the minimum, \(Q_1\), the median, \(Q_3\) and the maximum. A **box plot** (box-and-whisker diagram) draws a box from \(Q_1\) to \(Q_3\) with a line at the median, and whiskers out to the minimum and maximum. The width of the box is the IQR. Draw it on a scale.
:::

:::html
<figure class="fig wide"><svg viewBox="0 0 540 125" role="img" aria-label="Two box plots on a scale from 20 to 50 minutes. Route A: minimum 23, quartiles 28 and 38, median 31, maximum 45. Route B: minimum 26, quartiles 32 and 39, median 35, maximum 44."><path class="ax" d="M26 100H520" marker-end="url(#ahm)"/><path class="ln thin" d="M30 97V103"/><text class="ts tc" x="30" y="116">20</text><path class="ln thin" d="M110 97V103"/><text class="ts tc" x="110" y="116">25</text><path class="ln thin" d="M190 97V103"/><text class="ts tc" x="190" y="116">30</text><path class="ln thin" d="M270 97V103"/><text class="ts tc" x="270" y="116">35</text><path class="ln thin" d="M350 97V103"/><text class="ts tc" x="350" y="116">40</text><path class="ln thin" d="M430 97V103"/><text class="ts tc" x="430" y="116">45</text><path class="ln thin" d="M510 97V103"/><text class="ts tc" x="510" y="116">50</text><path class="ln" d="M78 41H158M318 41H430M78 36V46M430 36V46"/><rect class="f1 s-acc sw2" x="158" y="30" width="160" height="22"/><path class="ln thick" d="M206 30V52"/><text class="tl tb" x="78" y="25">Route A</text><path class="ln" d="M126 79H222M334 79H414M126 74V84M414 74V84"/><rect class="f1 s-acc sw2" x="222" y="68" width="112" height="22"/><path class="ln thick" d="M270 68V90"/><text class="tl tb" x="126" y="63">Route B</text></svg><figcaption>Box plots of the journey times in minutes. Route A has the lower median (31 against 35) but the wider box (IQR 10 against 7) and the wider range.</figcaption></figure>
:::

For route B, the lower half is 26, 30, 32, 34, 35, so \(Q_1 = 32\), and the upper half is 37, 38, 39, 41, 44, so \(Q_3 = 39\), giving IQR 7.

:::warn Quartiles and outliers
Methods for finding quartiles from small data sets differ slightly between textbooks. This course takes the median of each half, leaving out the middle value when \(n\) is odd. If a question gives a rule for outliers, apply it exactly. A common rule is that a value is an **outlier** if it is more than \(1.5 \times \text{IQR}\) above \(Q_3\) or below \(Q_1\). For route A, \(Q_3 + 1.5\times 10 = 53\) and \(Q_1 - 15 = 13\), so there are no outliers.
:::

Use the widget to change the data and see how the mean, median and spread react. Add a large value and compare how far each statistic moves.

:::html
<div class="widget" data-w="stats" data-values="23, 24, 27, 28, 29, 31, 31, 31, 33, 35, 36, 38, 40, 42, 45"></div>
:::

## Mean and standard deviation

For \(n\) values with \(\sum x\) and \(\sum x^2\):

:::key Mean, variance and standard deviation
\[\bar x = \frac{\sum x}{n} \qquad \text{variance} = \frac{\sum x^2}{n} - \bar x^2 \qquad \text{standard deviation} = \sqrt{\text{variance}}\]
For a frequency table, use \(\sum fx\) and \(\sum fx^2\) with \(n = \sum f\). The mean and standard deviation formulae are given on MF19, but the form \(\sqrt{\dfrac{\sum x^2}{n} - \bar x^2}\) is the quicker one to use, so practise it.
:::

The mean uses every value, so it is pulled by outliers; the median and IQR are **resistant** and are better for skewed data. The standard deviation measures the typical distance from the mean; a larger value means more spread.

:::proof Why variance = mean of the squares minus the square of the mean
The variance is defined as the mean squared distance from the mean: \(\dfrac{\sum (x - \bar x)^2}{n}\). Expand the bracket in each term:
\[\sum (x - \bar x)^2 = \sum x^2 - 2\bar x\sum x + \sum \bar x^2\]
The mean \(\bar x\) is one fixed number, so \(\sum \bar x^2 = n\bar x^2\). Also \(\sum x = n\bar x\), by the definition of the mean. Substitute both:
\[\sum (x - \bar x)^2 = \sum x^2 - 2n\bar x^2 + n\bar x^2 = \sum x^2 - n\bar x^2\]
Divide by \(n\):
\[\frac{\sum (x - \bar x)^2}{n} = \frac{\sum x^2}{n} - \bar x^2\]
So the quick form gives the same answer as the definition, without finding every \(x - \bar x\). Check with 4, 6, 8, 10, 12 (mean 8): the squared distances are 16, 4, 0, 4, 16, which total 40, and \(\dfrac{40}{5} = 8\), the value found above.
:::

:::eg For the 15 route A times, \(\sum x = 493\). Find the mean. For the data set 4, 6, 8, 10, 12 find the mean and standard deviation.
\(\bar x = \dfrac{493}{15} = 32.9\) minutes (3 s.f.).
For 4, 6, 8, 10, 12: \(\sum x = 40\), so \(\bar x = 8\); \(\sum x^2 = 16 + 36 + 64 + 100 + 144\) \(= 360\). Variance \(= \dfrac{360}{5} - 8^2 = 8\), so the standard deviation is \(\sqrt8 = 2.83\).
:::

### Frequency tables

:::eg The number of goals scored in a match was recorded for 30 matches: 1 goal in 3 matches, 2 in 7, 3 in 10, 4 in 6 and 5 in 4. Find the mean, standard deviation and median.
\(\sum f = 30\), \(\sum fx = 3 + 14 + 30 + 24 + 20 = 91\), so \(\bar x = \dfrac{91}{30} = 3.03\).
\(\sum fx^2 = 3 + 28 + 90 + 96 + 100\) \(= 317\), so variance \(= \dfrac{317}{30} - \left(\dfrac{91}{30}\right)^2\) \(= 1.366\) and the standard deviation is \(1.17\).
The cumulative frequencies are 3, 10, 20, 26, 30. The median is between the 15th and 16th values; both are in the group with 3 goals, so the median is **3**.
:::

### Coded data

When the numbers are large, subtract a constant \(a\) first and work with \(y = x - a\). The mean is \(\bar x = \bar y + a\), and **the standard deviation is unchanged** by subtracting a constant (the spread does not move). Dividing every value by \(b\) divides the standard deviation by \(b\) as well.

:::eg The masses \(x\) grams of 10 parcels satisfy \(\sum (x - 60) = 24\) and \(\sum (x - 60)^2 = 410\). Find the mean and standard deviation of \(x\).
Let \(y = x - 60\). \(\bar y = \dfrac{24}{10} = 2.4\), so \(\bar x = 62.4\). The variance of \(y\) is \(\dfrac{410}{10} - 2.4^2 = 41 - 5.76\) \(= 35.24\). The variance of \(x\) is the same, so the standard deviation is \(\sqrt{35.24} = 5.94\) grams.
:::

### Combining two data sets

:::eg Set A has 12 values with mean 15 and standard deviation 2. Set B has 8 values with mean 20 and standard deviation 3. Find the mean and standard deviation of all 20 values.
Mean \(= \dfrac{12\times 15 + 8\times 20}{20}\) \(= \dfrac{340}{20} = 17\).
From the variance formula, \(\sum x^2 = n(\sigma^2 + \bar x^2)\). Set A: \(12(4 + 225) = 2748\). Set B: \(8(9 + 400) = 3272\). Total \(= 6020\).
Variance \(= \dfrac{6020}{20} - 17^2 = 301 - 289\) \(= 12\), so the standard deviation is \(\sqrt{12} = 3.46\).
:::

:::eg (Exam style) The times \(t\) seconds of 25 runners satisfy \(\sum t = 600\) and \(\sum t^2 = 14\,700\). (a) Find the mean and standard deviation. (b) A 26th runner takes 30 seconds. Find the new mean and standard deviation.
(a) \(\bar t = \dfrac{600}{25} = 24\). [B1] Variance \(= \dfrac{14\,700}{25} - 24^2\) \(= 588 - 576 = 12\). [M1] Standard deviation \(= \sqrt{12} = 3.46\). [A1]
(b) New \(\sum t = 630\) and \(\sum t^2 = 14\,700 + 900 = 15\,600\), with \(n = 26\). [M1] New mean \(= \dfrac{630}{26} = 24.2\). [A1] Variance \(= \dfrac{15\,600}{26} - \left(\dfrac{630}{26}\right)^2\) \(= 600 - 587.13\) \(= 12.87\), so the standard deviation is \(3.59\). [A1]
The added runner is above the mean, so both the mean and the spread have risen.
:::

## Histograms and unequal class widths

In a histogram of continuous data the **area** of each bar is proportional to the frequency. When the class widths differ, the height must be the **frequency density**:

:::key Frequency density
\[\text{frequency density} = \frac{\text{frequency}}{\text{class width}} \qquad\text{so}\qquad \text{frequency} = \text{frequency density} \times \text{class width}\]
The vertical axis is labelled "frequency density". Bars touch for continuous data.
:::

:::eg (Real context) The waiting times of 80 customers at a bank were: 0 to 10 minutes, 12 customers; 10 to 20, 30; 20 to 40, 24; 40 to 60, 14. Draw a histogram and estimate the mean and standard deviation.
Frequency densities: \(\frac{12}{10} = 1.2\), \(\frac{30}{10} = 3\), \(\frac{24}{20} = 1.2\), \(\frac{14}{20} = 0.7\). The histogram is drawn below.

To estimate the mean and standard deviation, use the **midpoints** of the classes (5, 15, 30, 50) as if every value in a class equalled its midpoint. This gives \(\sum fx\) \(= 12(5) + 30(15) + 24(30) + 14(50)\) \(= 1930\), so \(\bar x = \dfrac{1930}{80} = 24.1\) minutes. Also \(\sum fx^2\) \(= 12(25) + 30(225) + 24(900) + 14(2500)\) \(= 63\,650\), so the variance is \(\dfrac{63\,650}{80} - 24.125^2 = 213.6\) and the standard deviation is \(14.6\) minutes. Both are estimates, because the exact values are not known.
:::

:::html
<figure class="fig"><svg viewBox="0 0 520 178" role="img" aria-label="Histogram of waiting times with frequency density 1.2 for 0 to 10, 3 for 10 to 20, 1.2 for 20 to 40 and 0.7 for 40 to 60 minutes."><path class="ax" d="M36 150H500" marker-end="url(#ahm)"/><path class="ax" d="M40 154V20" marker-end="url(#ahm)"/><rect class="f1 s-acc sw2" x="40.0" y="109.2" width="75.0" height="40.8"/><text class="tl tc" x="78" y="104">1.2</text><rect class="f1 s-acc sw2" x="115.0" y="48.0" width="75.0" height="102.0"/><text class="tl tc" x="152" y="43">3</text><rect class="f1 s-acc sw2" x="190.0" y="109.2" width="150.0" height="40.8"/><text class="tl tc" x="265" y="104">1.2</text><rect class="f1 s-acc sw2" x="340.0" y="126.2" width="150.0" height="23.8"/><text class="tl tc" x="415" y="121">0.7</text><text class="ts tc" x="40" y="166">0</text><text class="ts tc" x="115" y="166">10</text><text class="ts tc" x="190" y="166">20</text><text class="ts tc" x="340" y="166">40</text><text class="ts tc" x="490" y="166">60</text><path class="gr" d="M40 116H490"/><text class="ts te" x="35" y="119">1</text><path class="gr" d="M40 82H490"/><text class="ts te" x="35" y="85">2</text><path class="gr" d="M40 48H490"/><text class="ts te" x="35" y="51">3</text><text class="tl ti" x="496" y="144" text-anchor="end">minutes</text><text class="tl ti" x="46" y="18">frequency density</text></svg><figcaption>Histogram of waiting times. The tallest bar is the shortest class, because that class holds the most customers per minute.</figcaption></figure>
:::

## Cumulative frequency

A **cumulative frequency graph** (ogive) plots the number of values **below** each class's upper boundary. Plot at the **upper class boundary**, and join the points with straight lines (or a smooth curve, if you are told the data is smooth). Then read off:

- the **median** at \(\tfrac12 n\);
- the **quartiles** at \(\tfrac14 n\) and \(\tfrac34 n\);
- the **\(p\)th percentile** at \(\tfrac{p}{100}n\).

:::eg For the 80 customers, use a cumulative frequency graph to estimate the median, the quartiles, the interquartile range and the number of customers who waited more than 30 minutes.
Cumulative frequencies at the upper boundaries 10, 20, 40, 60 are 12, 42, 66, 80, with 0 at 0. The graph is drawn below.

Median: the \(40^{\text{th}}\) value. Between (10, 12) and (20, 42), so by interpolation \(10 + \dfrac{40 - 12}{30}\times 10\) \(= 19.3\) minutes.
\(Q_1\): the \(20^{\text{th}}\) value, \(10 + \dfrac{20 - 12}{30}\times 10\) \(= 12.7\) minutes.
\(Q_3\): the \(60^{\text{th}}\) value, between (20, 42) and (40, 66): \(20 + \dfrac{60 - 42}{24}\times 20 = 35\) minutes.
\(\text{IQR} = 35 - 12.7 = 22.3\) minutes.
Waiting more than 30 minutes: cumulative frequency at 30 is \(42 + \dfrac{10}{20}\times 24 = 54\), so \(80 - 54 = 26\) customers.
:::

:::html
<figure class="fig"><svg viewBox="0 0 520 198" role="img" aria-label="Cumulative frequency graph of waiting times through the points (0, 0), (10, 12), (20, 42), (40, 66) and (60, 80), with dashed lines marking the lower quartile at 12.7, the median at 19.3 and the upper quartile at 35."><path class="ax" d="M36 160H500" marker-end="url(#ahm)"/><path class="ax" d="M40 164V24" marker-end="url(#ahm)"/><path class="gr" d="M40 130H490"/><text class="ts te" x="35" y="133">20</text><path class="gr" d="M40 100H490"/><text class="ts te" x="35" y="103">40</text><path class="gr" d="M40 70H490"/><text class="ts te" x="35" y="73">60</text><path class="gr" d="M40 40H490"/><text class="ts te" x="35" y="43">80</text><text class="ts tc" x="40" y="176">0</text><text class="ts tc" x="190" y="176">20</text><text class="ts tc" x="340" y="176">40</text><text class="ts tc" x="490" y="176">60</text><path class="c1" d="M40.0 160.0L115.0 142.0L190.0 97.0L340.0 61.0L490.0 40.0"/><circle class="fa" cx="40.0" cy="160.0" r="3"/><circle class="fa" cx="115.0" cy="142.0" r="3"/><circle class="fa" cx="190.0" cy="97.0" r="3"/><circle class="fa" cx="340.0" cy="61.0" r="3"/><circle class="fa" cx="490.0" cy="40.0" r="3"/><path class="ln thin dash" d="M40 130.0H135.0V160"/><text class="tl tc halo" x="135" y="190">12.7</text><path class="ln thin dash" d="M40 100.0H185.0V160"/><text class="tl tc halo" x="185" y="190">19.3</text><path class="ln thin dash" d="M40 70.0H302.5V160"/><text class="tl tc halo" x="302" y="190">35</text><text class="tl ti" x="496" y="154" text-anchor="end">minutes</text><text class="tl ti" x="46" y="18">cumulative frequency</text></svg><figcaption>Cumulative frequency graph of the waiting times. The dashed lines read off \(Q_1 \approx 12.7\), the median \(\approx 19.3\) and \(Q_3 = 35\) minutes.</figcaption></figure>
:::

:::exam What earns marks
- **Comparing data sets**: use one measure of centre and one of spread, and write a sentence in context: "Route B has the higher median time (35 against 31), so it is slower on average, but its IQR is smaller (7 against 10), so its times are more consistent." Quoting numbers without a conclusion earns little.
- Use the **median and IQR** when the data is skewed or has outliers, and the **mean and standard deviation** when it is roughly symmetric.
- **Histograms**: label the vertical axis "frequency density", and show the working \(\text{frequency}\) \(= \text{FD}\times\text{width}\).
- **Standard deviation**: divide by \(n\) (not \(n - 1\)) in this chapter. Do not round the mean before squaring it.
- **Coded data**: subtracting a constant changes the mean but not the standard deviation.
:::

:::board Other boards
Edexcel IAL S1 and the UK A Level statistics courses cover the same displays and summary measures. Methods for the quartiles of a small data set, and the rule for outliers, vary between boards, so use the method your specification names. UK A Level courses also introduce the large data set, which has no counterpart in Cambridge 9709.
:::

:::eg Spot the error: variance from \(\sum x\) and \(\sum x^2\)
A student wrote this answer to "The scores \(x\) of 8 players satisfy \(\sum x = 56\) and \(\sum x^2 = 436\). Find the mean and the standard deviation of the scores" [3 marks].

Line 1: Mean \(= \dfrac{56}{8} = 7\).
Line 2: Variance \(= \dfrac{436}{8} - 7 = 54.5 - 7 = 47.5\).
Line 3: Standard deviation \(= \sqrt{47.5} = 6.89\).

**Line 1 is correct [B1].** **Line 2 scores [M0].** It subtracts the mean \(7\), but the formula subtracts the **square** of the mean, \(7^2 = 49\). A wrong formula is a wrong method, so the method mark is lost. **Line 3 scores [A0]:** the square root is taken correctly, but an accuracy mark cannot be earned after a method mark has been lost. The student scores 1 out of 3.

Correct working: variance \(= \dfrac{436}{8} - 7^2\) \(= 54.5 - 49 = 5.5\) [M1], so the standard deviation is \(\sqrt{5.5} = 2.35\) [A1].

**Check:** the mean of the squares is always the variance plus the square of the mean. The student's answer implies \(47.5 + 49 = 96.5\), but the data gives \(\dfrac{436}{8} = 54.5\). They do not match. The correct variance gives \(5.5 + 49 = 54.5\). ✓
:::

:::try Start easy, finish at exam standard
Q: Find the median, mode, range and interquartile range of 7, 3, 9, 3, 12, 8, 3, 15.
A: Sorted: 3, 3, 3, 7, 8, 9, 12, 15. Median \(= \dfrac{7 + 8}{2} = 7.5\); mode 3; range 12. Lower half 3, 3, 3, 7 gives \(Q_1 = 3\); upper half 8, 9, 12, 15 gives \(Q_3 = 10.5\). IQR \(= 7.5\).
Q: Find the mean and standard deviation of 4, 6, 8, 10, 12 using \(\sum x^2\).
A: \(\bar x = 8\), \(\sum x^2 = 360\), variance \(= 72 - 64 = 8\), standard deviation \(= 2.83\).
Q: A frequency table has \(x = 1, 2, 3, 4, 5\) with frequencies 3, 7, 10, 6, 4. Find the mean and standard deviation.
A: \(n = 30\), \(\sum fx = 91\), \(\sum fx^2 = 317\). Mean \(= 3.03\); variance \(= \dfrac{317}{30} - \left(\dfrac{91}{30}\right)^2\) \(= 1.366\); standard deviation \(= 1.17\).
Q: The class 20 to 25 has frequency 18, and the class 25 to 40 has frequency 24. Find the frequency density of each class.
A: \(\dfrac{18}{5} = 3.6\) and \(\dfrac{24}{15} = 1.6\).
Q: For 15 values, \(\sum (x - 20) = -15\) and \(\sum (x - 20)^2 = 135\). Find the mean and standard deviation of \(x\).
A: \(\overline{x - 20} = -1\), so \(\bar x = 19\). Variance \(= \dfrac{135}{15} - (-1)^2 = 8\), so the standard deviation is \(2.83\).
Q: A group of 15 students has mean mark 8 and a group of 10 has mean mark 13. Find the mean of all 25.
A: \(\dfrac{15\times 8 + 10\times 13}{25}\) \(= \dfrac{250}{25} = 10\).
Q: Use the cumulative frequencies in the customer example to estimate the 90th percentile.
A: The \(72^{\text{nd}}\) value is in the class 40 to 60 (66 to 80): \(40 + \dfrac{72 - 66}{14}\times 20\) \(= 48.6\) minutes.
Q: The data 12, 14, 15, 15, 16, 17, 18, 19, 40 includes a possible outlier. A value is an outlier if it is more than \(1.5\times\text{IQR}\) above \(Q_3\) or below \(Q_1\). Test 40.
A: Median 16. Lower half 12, 14, 15, 15 gives \(Q_1 = 14.5\); upper half 17, 18, 19, 40 gives \(Q_3 = 18.5\). IQR \(= 4\). Upper fence \(= 18.5 + 6 = 24.5\). Since \(40 > 24.5\), it is an outlier.
Q: (Exam style) Route A has median 31 and IQR 10; route B has median 35 and IQR 7. Compare the routes in context. [3 marks]
A: Route A has the lower median (31 against 35), so its journeys are quicker on average. [B1] Route B has the smaller IQR (7 against 10), so its times are more consistent. [B1] So A is quicker typically but less reliable, and B is slower but more predictable. [B1]
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ The ages of the 11 members of a chess club are 14, 17, 17, 19, 22, 23, 25, 28, 29, 31 and 36. Find the median, the lower quartile, the upper quartile and the interquartile range.
A: There are 11 values, so the median is the \(6^{\text{th}}\): \(23\). [B1] The lower half is 14, 17, 17, 19, 22, so \(Q_1 = 17\). [B1] The upper half is 25, 28, 29, 31, 36, so \(Q_3 = 29\). [B1] The interquartile range is \(29 - 17 = 12\). [B1]
Q: [3 marks] ★ For 20 values, \(\sum x = 260\) and \(\sum x^2 = 3600\). Find the mean and the standard deviation.
A: The mean is \(\dfrac{260}{20} = 13\). [B1] The variance is
\[\frac{3600}{20} - 13^2 = 180 - 169 = 11\]
[M1] so the standard deviation is \(\sqrt{11} = 3.32\). [A1]
Q: [5 marks] ★★ The table shows the number of faults \(x\) found in each of a batch of items. The frequencies are 6, 11, \(k\), 5 and 2 for \(x = 0, 1, 2, 3, 4\). The mean number of faults is 1.5. (a) Find \(k\). (b) Find the standard deviation.
A: (a) \(\sum f = 24 + k\) and \(\sum fx = 11 + 2k + 15 + 8 = 34 + 2k\). [M1] The mean gives
\[\frac{34 + 2k}{24 + k} = 1.5\]
so \(34 + 2k = 36 + 1.5k\). [M1] Then \(0.5k = 2\), so \(k = 4\). [A1] (b) Now \(\sum f = 28\) and \(\sum fx^2 = 0 + 11 + 16 + 45 + 32\) \(= 104\). The variance is
\[\frac{104}{28} - 1.5^2 = 1.464\]
[M1] and the standard deviation is \(1.21\). [A1]
Q: [5 marks] ★★ A histogram of times \(t\) minutes has four bars. The heights, which are frequency densities, are 1.4 for \(0 \le t < 10\), 3.5 for \(10 \le t < 20\), 2 for \(20 \le t < 40\) and 0.5 for \(40 \le t < 70\). (a) Find the total frequency. (b) Estimate the median.
A: (a) Frequency \(=\) frequency density \(\times\) class width, so the frequencies are \(14\), \(35\), \(40\) and \(15\). [M1] The total is \(104\). [A1] (b) The median is the \(52^{\text{nd}}\) value. The cumulative frequencies are 14, 49, 89, 104, so it lies in the class 20 to 40. [M1] Interpolating,
\[20 + \frac{52 - 49}{40} \times 20 = 21.5\]
[M1] so the median is about \(21.5\) minutes. [A1]
Q: [4 marks] ★★ For 25 values of \(x\), \(\sum (x - 30) = -50\) and the standard deviation of \(x\) is 4. Find the mean of \(x\) and the value of \(\sum (x - 30)^2\).
A: The mean of \(x - 30\) is \(\dfrac{-50}{25} = -2\), so \(\bar x = 28\). [B1] Subtracting a constant does not change the spread, so the variance of \(x - 30\) is \(4^2 = 16\). [M1] Then
\[\frac{\sum (x - 30)^2}{25} - (-2)^2 = 16\]
[M1] so \(\sum (x - 30)^2 = 25 \times 20 = 500\). [A1]
Q: [5 marks] ★★ Ten values have \(\sum x = 120\) and \(\sum x^2 = 1550\). An eleventh value \(a\) is added, and the mean of all 11 values is 12.5. (a) Find \(a\). (b) Find the standard deviation of the 11 values.
A: (a) The new total is \(11 \times 12.5 = 137.5\), so \(a = 137.5 - 120 = 17.5\). [M1 A1] (b) The new \(\sum x^2\) is \(1550 + 17.5^2 = 1856.25\). [M1] The variance is
\[\frac{1856.25}{11} - 12.5^2 = 168.75 - 156.25 = 12.5\]
[M1] so the standard deviation is \(\sqrt{12.5} = 3.54\). [A1]
Q: [5 marks] ★★ The lengths of 70 leaves, in mm, are summarised by the cumulative frequencies 8, 26, 52, 64 and 70 for lengths below 20, 30, 40, 60 and 80. (a) Estimate the median. (b) Estimate how many leaves are longer than 50 mm.
A: (a) The median is the \(35^{\text{th}}\) value, in the class 30 to 40. [M1] Interpolating,
\[30 + \frac{35 - 26}{52 - 26} \times 10 = 33.46\]
[M1] so the median is about \(33.5\) mm. [A1] (b) The cumulative frequency at 50 is \(52 + \dfrac{10}{20} \times 12 = 58\). [M1] So \(70 - 58 = 12\) leaves are longer than 50 mm. [A1]
Q: [7 marks] (#math.p1.series) ★★★ Seven positive numbers form an arithmetic progression with common difference \(d\), where \(d > 0\). Their sum is 140 and the sum of their squares is 3052. (a) Show that the middle number is 20. (b) Find \(d\). (c) Write down the smallest number.
H: Use \(S_n\) \(= \dfrac{n}{2}\left(2a + (n - 1)d\right)\) with \(n = 7\). The middle (fourth) term is \(a + 3d\).
H: Write the seven numbers as \(20 - 3d, 20 - 2d, \ldots, 20 + 3d\). When you square and add, the terms in \(d\) cancel in pairs.
H: The squares add up to \(7 \times 20^2\) plus \(d^2\) times \((9 + 4 + 1 + 0 + 1 + 4 + 9)\).
A: (a) \(S_7 = \dfrac72(2a + 6d) = 7(a + 3d)\). [M1] This equals 140, so \(a + 3d = 20\), which is the fourth term. [A1] (b) The numbers are \(20 + kd\) for \(k = -3, \ldots, 3\). [M1] The cross terms cancel, so
\[\sum x^2 = 7 \times 400 + 28d^2 = 2800 + 28d^2\]
[A1] Then \(2800 + 28d^2 = 3052\), so \(d^2 = 9\). [M1] Since \(d > 0\), \(d = 3\). [A1] (c) The smallest number is \(20 - 9 = 11\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A depot is built at position \(a\) km along a straight road. Customers live at positions \(x_1, \ldots, x_n\), and the cost of serving each one is \((x - a)^2\). (a) By writing \(x - a = (x - \bar x) + (\bar x - a)\), show that the total cost is \(n\sigma^2 + n(\bar x - a)^2\), where \(\sigma^2\) is the variance of the positions. (b) Hence write down the best position and the least cost for customers at 2, 5, 6, 9 and 13 km. (c) Find the total cost if the depot is at 10 km.
H: Square the bracket: \((x - a)^2\) \(= (x - \bar x)^2 + 2(x - \bar x)(\bar x - a)\) \(+ (\bar x - a)^2\). Then add over all customers.
H: What is \(\sum (x - \bar x)\)? Use the definition of the mean.
H: In (b), \(n(\bar x - a)^2\) is never negative. When is it smallest?
A: (a) Squaring and adding gives
\[\sum (x - a)^2 = \sum (x - \bar x)^2 + 2(\bar x - a)\sum (x - \bar x) + n(\bar x - a)^2\]
[M1] Here \(\sum (x - \bar x) = \sum x - n\bar x\) \(= 0\). [M1] Also \(\sum (x - \bar x)^2 = n\sigma^2\) by the definition of variance. So the total cost is \(n\sigma^2 + n(\bar x - a)^2\). [A1] (b) The second term is zero only when \(a = \bar x\), and is otherwise positive, so the best position is the mean, \(a = \dfrac{35}{5} = 7\) km. [B1] The least cost is \(n\sigma^2\). Here \(\sum x^2 = 315\), so \(\sigma^2 = 63 - 49 = 14\) and the least cost is \(5 \times 14 = 70\). [B1] (c) At \(a = 10\) the cost is \(70 + 5 \times (7 - 10)^2 = 115\). [M1 A1]
Q: [7 marks] ★★★ A scientist records \(n\) readings with mean 10 and standard deviation 2. She removes one faulty reading of 16, and the mean of the remaining readings is 9.5. (a) Find \(n\). (b) Find the standard deviation of the remaining readings. (c) Explain why it is smaller than 2.
H: The total of all \(n\) readings is \(10n\). After removing 16 the total is \(10n - 16\), shared among \(n - 1\) readings.
H: Use \(\sum x^2 = n(\sigma^2 + \bar x^2)\) to find the original sum of squares, then remove \(16^2\).
A: (a) \(10n - 16 = 9.5(n - 1)\). [M1] Then \(0.5n = 6.5\), so \(n = 13\). [A1] (b) The original \(\sum x^2 = 13(4 + 100) = 1352\). [B1] After removing 16 it is \(1352 - 256 = 1096\) for 12 readings. [M1] The variance is
\[\frac{1096}{12} - 9.5^2 = 91.33 - 90.25 = 1.083\]
[M1] so the standard deviation is \(1.04\). [A1] (c) The removed reading was \(\dfrac{16 - 10}{2} = 3\) standard deviations above the mean, so it was far from the rest and added a lot to the spread. [B1]
:::

:::quiz
? A histogram has classes 0 to 10 (frequency 20) and 10 to 30 (frequency 20). What is true of the bar heights?
- They are equal.
+ The first bar is twice as tall as the second.
- The second bar is twice as tall as the first.
- You cannot tell without the total.
> Frequency density is frequency divided by width: \(20/10 = 2\) and \(20/20 = 1\). Equal frequencies on unequal widths give unequal heights.
? Which statistic changes least if one extreme value is added to a large data set?
- The mean
- The range
- The standard deviation
+ The median
> The median depends only on the middle of the ordered data. The mean, range and standard deviation all use the extreme value.
? Which formula gives the variance of a data set?
- \(\dfrac{\sum x^2}{n}\)
+ \(\dfrac{\sum x^2}{n} - \bar x^2\)
- \(\dfrac{\sum x^2}{n} - \bar x\)
- \(\left(\dfrac{\sum x}{n}\right)^2\)
> Variance is the mean of the squares minus the square of the mean. Forgetting to square the mean, or subtracting nothing, is a common slip.
? Every value in a data set is increased by 10. What happens to the mean and standard deviation?
- Both increase by 10.
+ The mean increases by 10 and the standard deviation is unchanged.
- The mean is unchanged and the standard deviation increases by 10.
- Both are unchanged.
> Adding a constant shifts the whole data set but does not change how spread out it is.
? In a cumulative frequency graph, where do you plot each point?
- At the midpoint of its class
- At the lower class boundary
+ At the upper class boundary
- At the class width
> Cumulative frequency counts the values up to the upper boundary, so each point sits above that boundary.
:::

:::checklist What you can now do
- [ ] I can choose a suitable display for a data set and say what its strengths and weaknesses are.
- [ ] I can draw and read a stem-and-leaf diagram, including a back-to-back one, with a key.
- [ ] I can find the median, quartiles, IQR, mode and range of a small data set and draw a box plot.
- [ ] I can draw a histogram with unequal class widths using frequency density, and read frequencies from one.
- [ ] I can draw a cumulative frequency graph and read off the median, quartiles, percentiles and the number above or below a value.
- [ ] I can find the mean and standard deviation from raw data, from a frequency table, from grouped data and from \(\sum x\) and \(\sum x^2\).
- [ ] I can work with coded data such as \(\sum (x - a)\) and \(\sum (x - a)^2\), and combine the means and standard deviations of two sets.
- [ ] I can compare two data sets using one measure of centre, one of spread and a sentence in context.
:::

:::recap
- Choose the display for the job: stem-and-leaf for small sets (with a key), box plot to compare, histogram for grouped continuous data, cumulative frequency for percentiles.
- Median and quartiles come from the ordered data; \(\text{IQR} = Q_3 - Q_1\). Median and IQR resist outliers.
- \(\bar x = \dfrac{\sum x}{n}\), variance \(= \dfrac{\sum x^2}{n} - \bar x^2\); for a frequency table use \(\sum fx\) and \(\sum fx^2\). For grouped data use midpoints, and say the results are estimates.
- Coding: subtracting \(a\) changes the mean by \(a\) but leaves the standard deviation unchanged. Combine sets using \(\sum x^2 = n(\sigma^2 + \bar x^2)\).
- Histogram height \(= \text{frequency density}\) \(= \dfrac{\text{frequency}}{\text{class width}}\).
- Cumulative frequency graph: plot at upper boundaries; read the median at \(\tfrac12n\), the quartiles at \(\tfrac14n\) and \(\tfrac34n\).
- When comparing, give a measure of centre, a measure of spread and a sentence in context.
:::

:::links
- watch: [Histograms](https://www.examsolutions.net/tutorials/histograms/) · ExamSolutions · frequency density and class widths
- watch: [Exam questions: mean and standard deviation](https://www.examsolutions.net/tutorials/exam-questions-calculating-the-mean-and-standard-deviation/) · ExamSolutions · from raw data and from Σx, Σx²
- practise: [CAIE S1 representation of data exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/data-presentation-and-interpretation/representation-of-data/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) · Khan Academy · units on displaying and summarising data
- read: [Introductory Statistics 2e (free textbook)](https://openstax.org/details/books/introductory-statistics-2e) · OpenStax · the descriptive statistics chapter
- papers: [9709 Paper 5 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-6/) · Physics & Maths Tutor · their page "cie-paper-6" holds Paper 5 (9709/5) [unofficial]

Links checked 3 October 2026.
:::
Next: [Permutations and combinations](#math.s1.perms).
