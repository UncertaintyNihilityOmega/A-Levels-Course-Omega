@chapter bio.evaluation
@title Analysis, conclusions and evaluation (Paper 5)
@level a2
@paper CAIE 9700 Paper 5
@time 4–5 hours
@summary The second half of Paper 5 gives you results and asks what they show and how far they can be trusted. You will learn how to decide which calculations to do (means without anomalies, percentage change, rates, SE and confidence intervals), judge significance from error bars and tests, justify a statistical test, write a conclusion that stays within the data, deal with anomalies, and evaluate the replication, range, measurement, control and validity of an investigation.

:::why
A set of results means nothing until someone decides what it shows. In Paper 5 you are handed tables, graphs and sometimes a statistical test, and you must pick out the key points, make the right calculations, write a conclusion that the data support and no more, and say how much confidence the evidence deserves. These are the skills of a working scientist reading a paper, and they carry about half of the Paper 5 marks. Most marks are lost by writing "proves", ignoring the numbers, or listing a weakness without saying what it does to the results.
:::

**Before you start**, you should be comfortable with [Statistics for biologists](#bio.stats) (SD, SE, 95% confidence intervals and the four tests) and [Planning investigations (Paper 5)](#bio.planning) (variables, controls, accuracy, repeatability and validity).

:::try Warm-up
Q: A sample has a standard deviation of 6.0 and 9 values. What is the standard error? (from [Statistics for biologists](#bio.stats))
A: \(6.0 \div \sqrt{9} = 2.0\).
Q: What is the difference between accuracy and repeatability? (from [Planning investigations (Paper 5)](#bio.planning))
A: Accuracy is how close a measurement is to the true value; repeatability is whether repeating the investigation gives similar results.
Q: Which axis carries the independent variable on a graph? (from [Maths skills for biology](#bio.maths))
A: The x-axis (horizontal). The dependent variable is on the y-axis.
:::

## What analysis and evaluation questions ask

Paper 5 gives you data from an investigation: a table of results, a graph, sometimes the output of a test. The questions follow a pattern, and the command words tell you what to write.

| command word | what to do |
|---|---|
| calculate | work out a number, show the working, give the unit |
| describe | give the trend or pattern, quoting figures with units |
| compare | give similarities and differences, with figures for both |
| explain | give the biological reason |
| state, identify | give a short answer, a fact or a value |
| suggest | apply what you know to an unfamiliar situation |
| assess, discuss | weigh up the evidence and give a judgement |

You earn marks for four kinds of skill: **handling the data** (calculations, tables, graphs), **judging significance** (SD, SE, error bars, tests), **drawing conclusions** (what the data show, how far the hypothesis is supported, why), and **evaluating** (anomalies, the method, the confidence you can have, improvements).

## Tables and graphs: showing the key points

Show quantitative data in a **table** with the independent variable in the left column, headings that give the quantity and the unit (for example `distance from the road / m`), and no units in the body. A **graph** puts the independent variable on the x-axis and the dependent variable on the y-axis, with labelled axes and units, a scale that uses most of the grid, and plotted points marked clearly. Join points by a best-fit line or curve, or by ruled lines when the pattern between points is not known. Use a **bar chart** when the x-axis shows categories (for example three treatments) and a **line graph** or **scatter graph** when it shows a measured quantity. Bar charts and line graphs of means can carry **error bars**: the graph must say whether they show the standard deviation, the standard error or the 95% confidence interval.

To describe a graph, give the overall trend, then values with units at start, end and the turning point, then any change in the rate. For example, "The mean root length decreased from 38 mm in distilled water to 12 mm at 0.010 mol dm⁻³; it changed little above 0.010 mol dm⁻³."

## Deciding which calculation to do

Before calculating, ask what the question wants to compare. The syllabus names these calculations.

- **Mean** of replicates (leaving out confirmed anomalies).
- **Percentage change** \(= \dfrac{\text{final} - \text{initial}}{\text{initial}} \times 100\). A positive result is a percentage **gain**, a negative one a percentage **loss**. Use it to compare when starting values differ.
- **Rate of change**: the change in the dependent variable divided by the time, or the gradient of a graph (or of a tangent to a curve).
- **Standard deviation, standard error and 95% confidence interval** to judge spread and reliability.
- A **statistical test** when the question asks whether a difference or relationship is significant.

:::eg Four replicate dishes of cress seedlings grown with a fertiliser had dry masses of 3.1, 3.3, 3.2 and 4.9 g. The control mean was 2.5 g. Identify any anomaly, calculate the mean, and find the percentage gain in mass caused by the fertiliser.
The value 4.9 g is far above the other three, which lie within 0.2 g of each other, so it is anomalous. [B1]

The mean without it:

\[\begin{aligned} \bar{x} &= \frac{3.1 + 3.3 + 3.2}{3} \\ &= 3.2\,\mathrm{g} \end{aligned}\]

so the mean is 3.2 g. [B1]

\[\begin{aligned} \text{percentage gain} &= \frac{3.2 - 2.5}{2.5} \times 100 \\ &= 28\% \end{aligned}\]

so the fertiliser gave a 28% gain in dry mass. [B1]

Leaving the anomaly in would give a mean of 3.6 g and a gain of 45%, which overstates the effect of one odd dish. State that you left it out, and why (see below).
:::

## Is the difference significant?

You met the tools in [Statistics for biologists](#bio.stats). In Paper 5 the question often gives **standard deviations** or **standard errors** and asks you to work out whether a difference between means is likely to be real.

- Standard error (SE) \(= s \div \sqrt{n}\). The 95% confidence interval is the mean \(\pm\) 2 SE.
- If the **95% confidence intervals of two means do not overlap**, the difference is probably significant. If they overlap, it may be due to chance.
- Bars that show \(\pm\) 1 SE are shorter than the 95% interval; to judge overlap you may need to double them first.
- A statistical test gives a definite answer; error bars are a quick guide.

:::eg The activity of catalase (in arbitrary units) was measured in extracts of potato tubers stored at three temperatures. Each mean is shown with its standard error. A: 4.1 ± 0.3; B: 6.0 ± 0.4; C: 4.4 ± 0.3. Use the 95% confidence interval (mean ± 2 SE) to decide which differences are probably significant.
The 95% intervals are mean \(\pm\) 2 SE. [M1]

| tubers | mean | 95% interval |
|---|---|---|
| A | 4.1 | 3.5 to 4.7 |
| B | 6.0 | 5.2 to 6.8 |
| C | 4.4 | 3.8 to 5.0 |

The intervals are correct. [A1]

A and C overlap (4.7 is above 3.8), so the difference between A and C is probably not significant. [B1]

B (5.2 to 6.8) overlaps neither A (3.5 to 4.7) nor C (3.8 to 5.0), so B is probably significantly different from both. [B1]

The tubers stored in condition B had the highest catalase activity, which is probably a real difference. A and C may differ only by chance, and a t-test would settle it.
:::

:::warn Overlap is a guide, not a proof
Error bars suggest; a test decides. If a question gives a calculated test value and a critical value, use them. If it gives only error bars or SE, say "probably significant" or "may be due to chance", and say that a statistical test would confirm it.
:::

## Choosing and justifying a test

Paper 5 may ask you to **choose and justify** a test, **state the null hypothesis**, or complete the test and write the conclusion. The rules are in [Statistics for biologists](#bio.stats); here is the way to write the answer.

- Name the **test** and say what question it answers (a difference between two means, a relationship between two variables, or a fit between observed and expected numbers).
- Give the **type of data** (nominal, ordinal or continuous) that makes the test suitable.
- Give a **condition** that is met (normally distributed, similar standard deviations, a straight-line scatter, enough pairs).

:::eg Justify the use of a t-test to compare the mean dry mass of seeds from plants grown in sun with those grown in shade (10 seeds in each sample).
A t-test compares the means of two samples. [B1]

Dry mass is a continuous measurement. [B1]

The values are approximately normally distributed with similar standard deviations; a t-test can be used with fewer than 30 values. [B1]

A weaker answer says "because it is the right test". It names no data type and no condition. The null hypothesis for the same test is: there is no significant difference between the mean dry mass of seeds from sun and shade plants.
:::

## Writing conclusions

A conclusion says what the results show, and no more. Build it in four parts.

:::key A conclusion in four parts
1. **State the finding with data**: the trend or difference, quoting values with units from the table or graph (and the result of the test, if one was done).
2. **Say how far the hypothesis is supported**: "supports", "partly supports", "does not support". Never "proves". Mention the strengths and weaknesses of the evidence if asked.
3. **Explain it biologically**: the mechanism that would cause the result.
4. **Stay within the data**: only the range of the independent variable that was tested, and no cause from a correlation alone. Suggest a further prediction or hypothesis if asked.
:::

:::exam Describe, explain, suggest
"Describe" the pattern first, quoting figures with units. "Explain" needs the biological reason. "Suggest" asks you to apply knowledge to a situation you may not have met, so use the information in the question. Do not explain when you are asked to describe: it earns no marks and costs time.
:::

:::warn Four ways to lose conclusion marks
**"The results prove …"**: data support or fail to support; they do not prove. **Ignoring the numbers**: "the line goes up" earns less than "rose from 12 to 31%". **Going outside the range**: results for 5 to 200 m say nothing about 500 m. **Causes from correlations**: write "is correlated with", then "may be because".
:::

## Anomalies

:::def Anomalous result
A reading or value that does not fit the pattern of the other results, or lies much further from the mean of its replicates than the others do.
:::

To deal with an anomaly:

1. **Identify** it: in a table it is far from the other replicates; on a graph it is a point well off the line or curve.
2. **Suggest a cause**: a mistake in measuring, an error in transferring or timing, an unrepresentative sample (an unusually large seedling), contamination, apparatus not at the right temperature.
3. **Deal with it**: repeat the measurement if possible; if not, exclude it from the mean and say that you did and why. Do not simply delete data that you do not like.
4. **Report** the effect: it would raise or lower the mean, or increase the spread.

## Evaluating an investigation

Evaluation means judging the **confidence** you can have in the conclusions. For each weakness, say what it is, what it does to the results (its effect on confidence), and how to improve it. Marks go to the effect and the improvement, not just the weakness.

| aspect | question to ask | typical weakness, its effect, an improvement |
|---|---|---|
| replication | Were there enough replicates? | Only one or two, so a mean is unreliable and anomalies cannot be found; use at least three, and more if the spread is large |
| range of the IV | Does it cover the expected change? | A narrow range could miss the optimum or the plateau; widen it |
| intervals of the IV | Are there enough values, evenly spaced? | Only three values hide the shape of the curve; use at least five, with smaller steps where the DV changes fast |
| measurement of the DV | Is the apparatus precise and the method objective? | Colour judged by eye is subjective; use a colorimeter. A 10 cm³ cylinder for 2 cm³ gives a large percentage uncertainty; use a syringe |
| control of variables | Were all key variables kept constant? | A temperature that drifts changes the rate; use a thermostatically controlled water bath checked with a thermometer |
| sample | Is it random and representative? | Only easy-to-reach sites; use random sampling |
| validity | Does the result test the hypothesis? | The result is not valid if measurements are inaccurate or a second variable changed with the IV; improve control and measurement |

:::eg A student investigated the effect of sucrose concentration on the change in mass of potato cylinders. She used 0, 0.2, 0.4, 0.6 and 0.8 mol dm⁻³ solutions. She cut one cylinder for each concentration with a knife from different potatoes, left each for 20 minutes, blotted it, and weighed it on a balance reading to 0.1 g. The mass changes ranged from −0.4 g to +0.3 g. Evaluate the method: give three weaknesses, the effect of each on confidence and an improvement for each.
Only one cylinder per concentration, so there is no mean and an anomaly cannot be identified; use at least three cylinders per concentration and calculate a mean. [B1] [B1]

Cylinders were cut with a knife from different potatoes, so surface area and the water potential of the tissue differ between treatments and could cause differences in mass; use a cork borer and cut all cylinders to the same length from one potato. [B1] [B1]

The balance reads to 0.1 g but the changes are only 0.3 to 0.4 g, so each mass is uncertain by ±0.05 g and a change found from two readings by ±0.1 g, which is about 30% of a change of 0.3 g; use a balance reading to 0.01 g, or calculate the percentage change from the starting mass. [B1] [B1]

(Also credit: the intervals of 0.2 mol dm⁻³ are large near the point of no change, so use smaller steps there; blotting is inconsistent, so blot for the same time; 20 minutes may be too short for equilibrium.)
:::

:::exam Evaluation phrases that gain marks
Name the weakness, say what it does ("so the mean is unreliable", "so the shape of the curve is not clear") and say how the improvement helps ("this reduces random error"). "Do it more carefully", "use better equipment" and "do more repeats" on their own gain nothing; say what, why and how many.
:::

## Two full data-analysis questions

Each question below is in the Paper 5 style, with a marked model answer. Cover the answers and try each part first.

<figure class="fig small"><svg viewBox="0 0 340 250" role="img" aria-label="Scatter graph of lichen cover in percent against distance from a road in metres for ten trees. Lichen cover rises from 3 percent at 5 metres to 38 percent at 200 metres; the points rise from left to right with some scatter."><path class="ax" d="M52 34L52 200L324 200"/><path class="ln" d="M48 200L52 200"/><text class="ts" x="44" y="203" text-anchor="end">0</text><path class="ln" d="M48 158.5L52 158.5"/><text class="ts" x="44" y="161.5" text-anchor="end">10</text><path class="ln" d="M48 117L52 117"/><text class="ts" x="44" y="120" text-anchor="end">20</text><path class="ln" d="M48 75.5L52 75.5"/><text class="ts" x="44" y="78.5" text-anchor="end">30</text><path class="ln" d="M48 34L52 34"/><text class="ts" x="44" y="37" text-anchor="end">40</text><path class="ln" d="M52 200L52 204"/><text class="ts" x="52" y="216" text-anchor="middle">0</text><path class="ln" d="M117.5 200L117.5 204"/><text class="ts" x="117.5" y="216" text-anchor="middle">50</text><path class="ln" d="M183 200L183 204"/><text class="ts" x="183" y="216" text-anchor="middle">100</text><path class="ln" d="M248.5 200L248.5 204"/><text class="ts" x="248.5" y="216" text-anchor="middle">150</text><path class="ln" d="M314 200L314 204"/><text class="ts" x="314" y="216" text-anchor="middle">200</text><circle class="f1 s-acc sw2" cx="58.5" cy="187.6" r="3.2"/><circle class="f1 s-acc sw2" cx="65.1" cy="191.7" r="3.2"/><circle class="f1 s-acc sw2" cx="78.2" cy="175.1" r="3.2"/><circle class="f1 s-acc sw2" cx="91.3" cy="162.7" r="3.2"/><circle class="f1 s-acc sw2" cx="117.5" cy="166.8" r="3.2"/><circle class="f1 s-acc sw2" cx="143.7" cy="129.4" r="3.2"/><circle class="f1 s-acc sw2" cx="169.9" cy="108.7" r="3.2"/><circle class="f1 s-acc sw2" cx="209.2" cy="121.1" r="3.2"/><circle class="f1 s-acc sw2" cx="248.5" cy="71.3" r="3.2"/><circle class="f1 s-acc sw2" cx="314.0" cy="42.3" r="3.2"/><text class="tl" x="6" y="14">lichen cover / %</text><text class="tl" x="322" y="238" text-anchor="end">distance from the road / m</text></svg><figcaption>The ten trees of the lichen survey. Lichen cover tends to rise with distance from the road, but the rise is not a perfect straight line.</figcaption></figure>

:::eg Data analysis 1, lichens and a busy road. Lichens are sensitive to air pollution. A student measured the percentage of the trunk covered by lichen on 10 oak trees at different distances from a busy road. The scatter graph shows the results. The student used Spearman's rank correlation. The critical value for \(n = 10\) at \(p = 0.05\) is 0.648.
| distance from road / m | lichen cover / % |
|---|---|
| 5 | 3 |
| 10 | 2 |
| 20 | 6 |
| 30 | 9 |
| 50 | 8 |
| 70 | 17 |
| 90 | 22 |
| 120 | 19 |
| 150 | 31 |
| 200 | 38 |

**(a) State a null hypothesis.** There is no correlation between the distance from the road and the percentage cover of lichen. [B1]

**(b) Explain why Spearman's rank correlation, not Pearson's, was used.** Percentage cover cannot be assumed to be normally distributed (and there are only ten points), but Spearman's test does not need normally distributed data. [B1] The scatter graph shows an increasing relationship that is not clearly a straight line, which suits a rank test better than Pearson's, which looks for a linear relationship. [B1]

**(c) Calculate \(r_s\).** Rank each column from the smallest (1). The distances are ranked 1 to 10. The lichen cover ranks, in the order of the table, are 2, 1, 3, 5, 4, 6, 8, 7, 9 and 10. [B1]

The differences \(D\) are −1, 1, 0, −1, 1, 0, −1, 1, 0 and 0, so \(\sum D^2 = 6\). [B1]

\[\begin{aligned} r_s &= 1 - \frac{6 \times 6}{10^3 - 10} \\ &= 1 - \frac{36}{990} \end{aligned}\] [M1]

\[r_s = 0.964\] [A1]

**(d) State the conclusion of the test.** The calculated \(r_s\) (0.964) is greater than the critical value (0.648), [B1] so there is a significant positive correlation between the distance from the road and lichen cover, [B1] and the null hypothesis is rejected. [B1]

**(e) Explain the result and give a limit to the conclusion.** Lichens absorb water and dissolved substances over their whole surface and are damaged by pollutants such as sulfur dioxide and nitrogen oxides from vehicles, which are most concentrated near the road. [B1] The correlation alone does not show that pollution is the cause: other factors such as light, dust or trunk size could also change with distance. [B1]

**(f) Evaluate the investigation and suggest improvements.** Only ten trees on one road: the result may not apply to other roads; sample more trees on several roads. [B1] The percentage cover was probably judged by eye, which is subjective; place a grid of squares on the trunk and count squares. [B1] Trunk size, tree age and the side of the trunk were not standardised, which could alter the cover; use trees of similar girth and always measure the same side. [B1]
:::

<figure class="fig small"><svg viewBox="0 0 340 262" role="img" aria-label="Bar chart of the mean fall in blood glucose in mmol per cubic decimetre for three groups of twelve mice, with error bars showing one standard error: placebo 0.90, low dose 1.40 and high dose 2.90."><path class="ax" d="M52 34L52 206L324 206"/><path class="ln" d="M48 206L52 206"/><text class="ts" x="44" y="209" text-anchor="end">0</text><path class="ln" d="M48 163L52 163"/><text class="ts" x="44" y="166" text-anchor="end">1</text><path class="ln" d="M48 120L52 120"/><text class="ts" x="44" y="123" text-anchor="end">2</text><path class="ln" d="M48 77L52 77"/><text class="ts" x="44" y="80" text-anchor="end">3</text><path class="ln" d="M48 34L52 34"/><text class="ts" x="44" y="37" text-anchor="end">4</text><text class="tl" x="6" y="14">mean fall in glucose / mmol dm⁻³</text><rect class="f1 s-acc sw2" x="87" y="167.3" width="50" height="38.7"/><path class="ln thick" d="M112 154.39L112 180.21"/><path class="ln thick" d="M104 154.39L120 154.39"/><path class="ln thick" d="M104 180.21L120 180.21"/><text class="tl" x="112" y="223" text-anchor="middle">placebo</text><rect class="f1 s-acc sw2" x="172" y="145.8" width="50" height="60.2"/><path class="ln thick" d="M197 132.022L197 159.578"/><path class="ln thick" d="M189 132.022L205 132.022"/><path class="ln thick" d="M189 159.578L205 159.578"/><text class="tl" x="197" y="223" text-anchor="middle">low dose</text><rect class="f1 s-acc sw2" x="257" y="81.3" width="50" height="124.7"/><path class="ln thick" d="M282 66.2802L282 96.3198"/><path class="ln thick" d="M274 66.2802L290 66.2802"/><path class="ln thick" d="M274 96.3198L290 96.3198"/><text class="tl" x="282" y="223" text-anchor="middle">high dose</text><text class="tl" x="52" y="256">bars: mean ± SE (n = 12 mice)</text></svg><figcaption>Mean fall in blood glucose after four weeks, with error bars of mean ± 1 SE. Compare the placebo and low-dose bars, and the low-dose and high-dose bars.</figcaption></figure>

:::eg Data analysis 2, a drug trial in mice. A drug is thought to lower blood glucose. Thirty-six mice with raised blood glucose were allocated at random to three groups of 12: a placebo, a low dose and a high dose. After four weeks the fall in blood glucose was recorded. The bar chart shows the means with error bars of ± 1 standard error.
| group | mean fall in glucose / mmol dm⁻³ | standard deviation / mmol dm⁻³ |
|---|---|---|
| placebo | 0.90 | 1.04 |
| low dose | 1.40 | 1.11 |
| high dose | 2.90 | 1.21 |

**(a) Calculate the standard error for the high-dose group.**

\[\begin{aligned} \mathrm{SE} &= \frac{s}{\sqrt{n}} \\ &= \frac{1.21}{\sqrt{12}} \end{aligned}\] [M1]

\[\mathrm{SE} = 0.35\,\mathrm{mmol\,dm^{-3}}\] [A1]

**(b) The standard errors for the placebo and low-dose groups are 0.30 and 0.32. Calculate the 95% confidence intervals for the means of the placebo, low-dose and high-dose groups.** Each interval is the mean \(\pm\) 2 SE. [M1]

Placebo: \(0.90 \pm 0.60\), so 0.30 to 1.50. Low dose: \(1.40 \pm 0.64\), so 0.76 to 2.04. High dose: \(2.90 \pm 0.70\), so 2.20 to 3.60. [A1]

**(c) Use the intervals to decide which differences are probably significant.** The placebo and low-dose intervals overlap (1.50 is above 0.76), so that difference may be due to chance. [B1] The low-dose and high-dose intervals do not overlap (2.04 is below 2.20), so that difference is probably significant. [B1] The high-dose interval is also clear of the placebo, so the high dose is probably different from the placebo. [B1]

**(d) State a conclusion about the hypothesis that the drug lowers blood glucose.** Only the high dose gave a fall that was probably significantly greater than the placebo, [B1] while the low dose did not, [B1] so the hypothesis is supported for the high dose but not shown for the low dose. [B1]

**(e) Calculate the percentage increase in the mean fall in the high-dose group compared with the placebo group.**

\[\begin{aligned} \text{increase} &= \frac{2.90 - 0.90}{0.90} \times 100 \\ &= 222\% \end{aligned}\] [M1] [A1]

**(f) Evaluate the trial.** Only 12 mice per group, and the intervals are wide, so confidence is limited; use more mice. [B1] Mice are not people, so the result may not apply to humans; follow with a trial in volunteers. [B1] Glucose was measured only after four weeks and with two doses; measure at several times and use more doses to see the pattern. [B1]
:::

:::eg Spot the error: a conclusion. [3]
A student found a significant negative Spearman correlation (\(r_s = -0.81\), \(n = 12\), critical value 0.587) between altitude (200 to 1800 m) and the number of plant species in 12 quadrats on a mountain. She wrote this conclusion.

Line 1: There is a significant negative correlation between altitude and the number of plant species, because 0.81 is greater than 0.587.
Line 2: The null hypothesis is rejected.
Line 3: This proves that altitude causes fewer species to grow, so a peak at 5000 m would have no plant species.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: a correlation does not prove a cause, because temperature, soil depth and rainfall also change with altitude, and the conclusion cannot be extended beyond the range tested (200 to 1800 m). That mark is lost [B0].**

Correct Line 3: "Species number decreases with altitude between 200 and 1800 m; this may be because the temperature falls and soils are thinner at higher altitudes." With that change the conclusion scores 3 marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: The lengths of four leaves were 12, 13, 12 and 19 mm. Identify the anomaly and calculate the mean without it.
A: 19 mm is the anomaly (it is far from the other three). Mean \(= (12 + 13 + 12) \div 3 = 12.3\) mm.
Q: The mass of a seedling increased from 4.8 g to 5.7 g. Calculate the percentage increase.
A: \((5.7 - 4.8) \div 4.8 \times 100 = 18.75\), so 19%.
Q: A culture of duckweed had 10 fronds on day 0 and 46 on day 6. Calculate the mean rate of increase.
A: \((46 - 10) \div 6 = 6\) fronds per day.
Q: Explain why a conclusion should not say that the results "prove" the hypothesis.
A: A result supports or fails to support a hypothesis. Results come from samples, can be affected by chance and error, and might be explained in another way, so they cannot prove it.
Q: Two means are 8.0 and 9.4. Their standard errors are 0.5 and 0.6. Use 95% intervals to decide whether the difference is probably significant.
A: The intervals are 7.0 to 9.0 and 8.2 to 10.6. They overlap, so the difference may be due to chance (not probably significant).
Q: Suggest two reasons for an anomalous result in an enzyme investigation.
A: Any two: the enzyme and substrate were not at the same temperature when mixed; a wrong volume was measured; the stopwatch was started late; the pipette was not rinsed and carried over solution; the end point was misjudged.
Q: A student studying the effect of temperature on an enzyme used 20, 30 and 40 °C only. Explain why three values are a weakness.
A: Three values do not show the shape of the curve, and the optimum could lie between the values or beyond the range; use at least five temperatures over a wider range.
Q: Write the null hypothesis for a Pearson's correlation test between leaf area and the number of stomata per mm².
A: There is no correlation between leaf area and stomatal density.
Q: The mass of a plant fell from 6.5 g to 5.2 g. Calculate the percentage loss.
A: \((6.5 - 5.2) \div 6.5 \times 100 = 20\%\) loss.
Q: In a rate experiment the temperature of the water bath drifted from 30 to 36 °C. Explain how this reduces the validity of the results and how to prevent it.
A: Temperature affects the rate, so a drift adds a second changing variable and the result is not due only to the independent variable. Use a thermostatically controlled water bath and check the temperature with a thermometer during the experiment.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ The numbers of stomata per mm² counted on five leaves from one tree were 212, 205, 208, 271 and 210. (a) Identify the anomalous result. (b) Calculate the mean without it. (c) Suggest one cause of the anomaly.
A: (a) 271, which is much higher than the other four. [B1]
(b) \((212 + 205 + 208 + 210) \div 4 = 208.75\), so 209 per mm². [B1]
(c) Any one: the count was made on a different part of the leaf; the leaf was from a sunnier position; a counting error was made. [B1]
Q: [4 marks] ★ Ten dry beans had a mass of 3.20 g. After 8 hours in water their mass was 4.48 g. Calculate (a) the percentage gain in mass and (b) the mean rate of mass gain.
A: (a) \((4.48 - 3.20) \div 3.20 \times 100\) [M1] \(= 40.0\%\) [A1]
(b) \(1.28 \div 8\) [M1] \(= 0.16\) g per hour [A1]
Q: [5 marks] ★★ The soil bacteria in plots treated with three fertilisers were counted (in thousands per cm³). The table gives each mean with its 95% confidence interval. (a) Describe the effect of the treatments on the number of bacteria. (b) Use the intervals to decide which differences are probably significant.

| treatment | mean number | 95% confidence interval |
|---|---|---|
| none (control) | 14 | ± 3.0 |
| organic | 23 | ± 4.0 |
| chemical | 17 | ± 3.5 |

H: Work out each interval first, as lower and upper limits.
A: (a) The organic fertiliser gave the highest number, 23 thousand per cm³, compared with 14 in the control. [B1]
The chemical fertiliser gave 17, a smaller increase. [B1]
(b) The intervals are 11.0 to 17.0 (control), 19.0 to 27.0 (organic) and 13.5 to 20.5 (chemical). The organic and control intervals do not overlap, so that difference is probably significant. [B1]
The chemical and control intervals overlap, so that difference may be due to chance. [B1]
The chemical and organic intervals overlap (20.5 is above 19.0), so that difference may also be due to chance. [B1]
Q: [6 marks] ★★ The numbers of mayfly nymphs and the dissolved oxygen concentration (mg dm⁻³) were measured in 14 sections of a stream. Both variables are continuous and normally distributed, and the scatter graph is a straight band of points. The student calculated Pearson's \(r = 0.61\). The critical value for \(n = 14\) at \(p = 0.05\) is 0.532. (a) State a null hypothesis. (b) Justify the use of Pearson's correlation. (c) State the conclusion and one limit to it.
H: Match the test to the data type and the shape of the scatter.
A: (a) There is no correlation between the oxygen concentration and the number of mayfly nymphs. [B1]
(b) Both variables are continuous and normally distributed. [B1]
The scatter graph suggests a linear relationship, and there are more than five pairs. [B1]
(c) The calculated \(r\) (0.61) is greater than the critical value (0.532), so there is a significant positive correlation; the null hypothesis is rejected. [B1]
Mayfly nymphs are more numerous in more oxygenated water. [B1]
The correlation does not show cause: clean water also has less pollution, a different flow and temperature. [B1]
Q: [6 marks] ★★ A student investigated the effect of temperature on the rate of fermentation by yeast. She used 20, 40 and 60 °C, one flask at each, and counted the bubbles of gas leaving a tube in 1 minute, by eye. The sugar solution was warmed in a water bath, but the temperature was not checked again. Give three weaknesses and, for each, an improvement.
H: Think about the number of values, replicates, the measurement and the temperature.
A: Only three temperatures, so the shape of the curve and the optimum are unclear. [B1] Use at least five temperatures over a range that includes the optimum. [B1]
One flask at each temperature, so there is no mean and an anomaly cannot be found. [B1] Use three flasks at each temperature and calculate means. [B1]
Counting bubbles by eye is imprecise, because bubbles vary in size and are easily missed. [B1] Collect the gas in a gas syringe and measure its volume. [B1]
(Also credit: the temperature may have changed during the experiment, so use a thermostatically controlled water bath checked with a thermometer; the same mass of yeast and volume of sugar solution were not stated.)
Q: [8 marks] ★★★ Lettuce seeds (25 per dish) were left to germinate in five dishes with water and in five dishes with 1.0% salt solution. The numbers that germinated were: water 23, 22, 24, 23, 23; salt 18, 15, 17, 16, 19. (a) Calculate the mean percentage germination for each. (b) The standard deviations are 0.71 (water) and 1.58 (salt). Use a t-test to find whether the means differ significantly. The critical value for the correct degrees of freedom at \(p = 0.05\) is 2.31. (c) State the conclusion.
H: Percentage germination is the mean number divided by 25, times 100.
H: Write the null hypothesis, use the formula for \(t\), then work out the degrees of freedom yourself.
A: (a) Water: \(23.0 \div 25 \times 100 = 92\%\). Salt: \(17.0 \div 25 \times 100 = 68\%\). [B1] [B1]
(b) Null hypothesis: there is no significant difference between the mean number of seeds germinating in water and in salt solution. [B1]
\(t = \dfrac{|23.0 - 17.0|}{\sqrt{\dfrac{0.71^2}{5} + \dfrac{1.58^2}{5}}}\) [M1] \(= \dfrac{6.0}{0.775} = 7.7\) [A1]
Degrees of freedom \(= 5 + 5 - 2 = 8\); critical value 2.31. [B1]
(c) \(7.7 > 2.31\), so there is a significant difference between the means. The null hypothesis is rejected. [B1]
Salt solution reduced the percentage of seeds that germinated, from 92% to 68%. [B1]
(Also credit: a likely reason is the lower water potential of the salt solution, which reduces the uptake of water by the seeds.)
Q: [7 marks] ★★★ Three antibiotics (A, B and C) were tested on the same bacterium using discs on agar, with five discs each. The diameter of the clear zone (mm) was recorded as mean ± standard deviation: A 18.0 ± 2.0; B 25.0 ± 2.0; C 22.0 ± 6.5. (a) Calculate the standard error and the 95% confidence interval of the mean for antibiotic A. (b) For B the interval is 23.2 to 26.8 mm. Compare A and B. (c) The standard deviation for C is much larger than for A and B. State what this shows and suggest a cause or improvement.
H: Use \(\mathrm{SE} = s \div \sqrt{n}\), with \(n = 5\).
A: (a) \(\mathrm{SE} = 2.0 \div \sqrt{5}\) [M1] \(= 0.89\) mm [A1]
Interval \(= 18.0 \pm 2 \times 0.894 = 16.2\) to \(19.8\) mm [A1]
(b) The intervals (16.2 to 19.8 and 23.2 to 26.8) do not overlap, [B1] so B probably produces a significantly larger clear zone than A, and B is probably more effective. [B1]
(c) The results for C are more variable, so the mean is less reliable and the results are less repeatable. [B1]
Possible cause or improvement: the agar depth or the density of bacteria in the lawn was not standardised between the discs; standardise them and use more discs. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A farmer compared two wheat varieties. Variety X was sown in the upper half of a field and variety Y in the lower, wetter half. Twelve plots of 1 m² were harvested from each half. The mean yields (with 95% confidence intervals) were X 540 ± 21 g m⁻² and Y 618 ± 24 g m⁻². The farmer concluded that Y is the better variety. (a) Use the intervals to say whether the difference in yield is probably significant. (b) Explain why the conclusion is not valid. (c) Suggest a better design.
H: For (b), what else differs between the two halves of the field?
A: (a) The intervals are 519 to 561 and 594 to 642 g m⁻². They do not overlap. [B1] So the difference is probably significant. [B1]
(b) The variety is confounded with the position in the field: soil moisture, depth and nutrients differ between the halves, [B1] so the difference may be due to the field and not to the variety. [B1]
(c) Sow both varieties in plots at random positions across the whole field (or in blocks, with both varieties in each block). [B1]
Keep the plot size, seed rate and fertiliser the same and use replicate plots. [B1]
Q: [5 marks] ★★★ A pilot study measured the zone of inhibition of five discs: the mean was 40 mm and the standard deviation 6 mm. (a) Calculate the 95% confidence interval for the mean. (b) The investigator wants an interval half as wide. How many discs are needed, assuming the standard deviation stays the same? Explain.
H: The width of the interval depends on the standard error.
A: (a) \(\mathrm{SE} = 6 \div \sqrt{5}\) [M1] \(= 2.68\); interval \(40 \pm 5.4\), so 34.6 to 45.4 mm. [A1] [A1]
(b) \(\mathrm{SE} = s \div \sqrt{n}\), so halving the SE needs \(\sqrt{n}\) to be doubled. [B1]
So \(n\) must be multiplied by 4: 20 discs are needed. [B1]
:::

:::quiz
? The mass of seedlings in two groups started at different values. Which calculation compares the effect of the treatments fairly?
+ the percentage change in mass for each group
- the final mass of each group
- the range of the final masses
- the mode of the starting masses
> Percentage change takes account of the starting value of each group. Comparing final masses ignores the different starting points.
? Four replicate readings are 22, 24, 23 and 41. What is the best way to deal with the 41?
+ Identify it as anomalous, suggest a cause, repeat it if possible, and if it is left out say so and why.
- Delete it without comment because it spoils the pattern.
- Include it, because every reading must be used.
- Replace it with the mean of the other three without saying so.
> An anomaly should be identified and its cause considered. It is excluded only with a stated reason; quietly changing data is not acceptable.
? The 95% confidence interval bars of two means do not overlap. What is the best conclusion?
+ The difference is probably significant.
- The difference is certainly caused by the treatment.
- The difference is not significant.
- The standard deviations are equal.
> Non-overlapping 95% intervals suggest the difference is unlikely to be due to chance. A test or a controlled experiment is needed to be sure of the cause.
? A student's rate graph covers 10 to 40 °C. Which statement is a valid conclusion?
+ The rate increased between 10 and 40 °C.
- The enzyme is denatured at 50 °C.
- The enzyme works best at 37 °C.
- The enzyme will stop at 0 °C.
> A conclusion must stay within the range tested. The data say nothing about 0 °C or 50 °C, and no optimum was shown because the rate was still rising.
? An investigation used only three values of the independent variable. What is the main effect of this on the conclusion?
+ The shape of the relationship is unclear, so confidence is lower.
- The dependent variable cannot be measured.
- The results are inaccurate.
- The control is invalid.
> Three points cannot show whether a trend is straight, curved or has a peak. The measurements may still be accurate.
? Which improvement increases the validity of a rate experiment in which the temperature drifted?
+ Using a thermostatically controlled water bath checked with a thermometer.
- Repeating the experiment more carefully.
- Using a larger beaker.
- Measuring the temperature only at the start.
> Validity needs the independent variable to be the only factor that changes, so the temperature has to be kept constant. "More carefully" is not specific.
? Two means are 10.0 and 11.0. The error bars show ± 1 SE, and each standard error is 0.5. Using 95% intervals (mean ± 2 SE), what do you conclude?
+ The intervals are 9.0 to 11.0 and 10.0 to 12.0; they overlap, so the difference may be due to chance.
- The intervals do not overlap, so the difference is significant.
- The difference is 1.0, so it is significant.
- No conclusion is possible without the sample size.
> The 95% interval is the mean ± 2 SE, which is twice the bar shown (it is ±1.0). The two intervals overlap between 10.0 and 11.0.
? Spearman's rank correlation of ten pairs gives \(r_s = 0.45\). The critical value is 0.648. What is the conclusion?
+ There is no significant correlation; any relationship could be due to chance.
- There is a significant positive correlation.
- There is a weak but significant correlation.
- The null hypothesis is rejected.
> The size of \(r_s\) (0.45) is less than 0.648, so the correlation is not significant, and the null hypothesis is accepted.
:::

:::checklist What you can now do
- [ ] I can use tables and graphs to show the key points of quantitative data, and draw graphs with the independent variable on the x-axis and error bars when needed.
- [ ] I can decide which calculations to do, and calculate means, percentage gain or loss and rates of change.
- [ ] I can use standard deviation, standard error, 95% confidence intervals and error bars to judge whether a difference is likely to be significant.
- [ ] I can choose and justify a statistical test, state a null hypothesis and name the type of data (nominal, ordinal or continuous).
- [ ] I can summarise the main conclusions, quoting data, and say to what extent a hypothesis is supported.
- [ ] I can give a biological explanation of a conclusion and make a further prediction or hypothesis.
- [ ] I can identify anomalous results, suggest causes and say how to deal with them.
- [ ] I can assess replication, the range and intervals of the independent variable, the measurement of the dependent variable and the control of variables.
- [ ] I can make a judgement about the validity of an investigation and how much confidence the conclusions deserve.
- [ ] I can suggest improvements that would increase confidence in the results, and say how each helps.
:::

:::recap
- Describe a graph with the trend and figures with units. Explain with the biological reason.
- Mean (leave out confirmed anomalies, and say so), percentage change \(= \text{change} \div \text{original} \times 100\), rate \(= \text{change} \div \text{time}\) or the gradient.
- 95% CI \(= \bar{x} \pm 2\) SE. Non-overlapping 95% intervals: probably significant. Overlapping: may be due to chance. A test decides.
- Justify a test by data type and conditions. The null hypothesis says "no significant difference" or "no correlation".
- A conclusion: finding with data, how far the hypothesis is supported ("supports", never "proves"), a biological explanation, and a limit (the range tested, correlation is not cause).
- Anomalies: identify, suggest a cause, repeat or exclude with a reason.
- Evaluate: replication, range and intervals of the IV, the measuring method, control of variables, sampling, validity. For each weakness give its effect and an improvement, and say how it helps.
:::

:::links
- read: [CAIE A Level Biology: practical skills notes](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/practical-skills/) · Physics & Maths Tutor · free notes on analysis, conclusions and evaluation
- papers: [Paper 5 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-5/) · Physics & Maths Tutor · real analysis and evaluation questions to practise on [unofficial]
- practise: [Topic questions (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topic-questions/) · Save My Exams · exam questions with mark schemes by topic [paid]
- watch: [CAIE A Level Biology videos](https://cognito.org/specifications/alevel/biology/cie) · Cognito · short videos and questions matched to the syllabus
- read: [ZNotes A2 Biology notes](https://znotes.org/caie/a2-biology-9700/) · ZNotes · free summary notes for the A Level syllabus

Links checked 24 October 2026.
:::

Next: [Paper 1: multiple choice](#bio.exam.p1)
