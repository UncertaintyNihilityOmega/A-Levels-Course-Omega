@chapter math.s.regression
@title Correlation and regression (UK boards)
@level ext
@paper Edexcel IAL S1 · AQA 7357 / Edexcel 9MA0 / OCR H240 Statistics · not in CAIE 9709
@time 4–6 hours
@summary Scatter diagrams show whether two variables move together. You will learn to describe correlation, to calculate and interpret the product moment correlation coefficient \(r\), to find the least squares regression line \(y = a + bx\) from summary statistics, to use it for prediction without extrapolating, and to test whether a sample correlation is evidence of a real relationship.

:::why
Does more revision mean higher marks? Do hotter days use less gas? Many real questions are about how two quantities are related, not just how one behaves. Correlation measures how closely two variables follow a straight-line pattern, and regression gives the best line for predicting one from the other. This chapter is **not in the CAIE 9709 syllabus**: it is for students on Edexcel IAL or the UK A Level courses, and a good extension for everyone else.
:::

**Before you start**, you need the mean and standard deviation from [Representing and summarising data](#math.s1.data) and the equation of a straight line from [Coordinate geometry](#math.p1.coord). For the test at the end, you need the ideas in [Hypothesis testing](#math.s2.hypothesis).

:::try Warm-up
Q: Find the equation of the line through \((2, 3)\) with gradient 4. (from [Coordinate geometry](#math.p1.coord))
A: \(y - 3 = 4(x - 2)\), so \(y = 4x - 5\).
Q: A data set has \(n = 10\), \(\sum x = 140\) and \(\sum x^2 = 2516\). Find \(\sum x^2 - \dfrac{(\sum x)^2}{n}\). (from [Representing and summarising data](#math.s1.data))
A: \(2516 - \dfrac{140^2}{10}\) \(= 2516 - 1960 = 556\). This is \(n\) times the variance of the \(x\) values.
Q: A test of \(H_0: p = 0.4\) against \(H_1: p < 0.4\) gives a probability of 0.031. Write the conclusion at the 5% significance level. (from [Hypothesis testing](#math.s2.hypothesis))
A: \(0.031 < 0.05\), so reject \(H_0\). There is sufficient evidence at the 5% level to suggest that \(p\) is less than 0.4, where \(p\) is stated in context.
:::

## Scatter diagrams and correlation

Suppose you record, for each of eight students, the hours \(x\) they revised and the score \(y\) they got. Each student is a point \((x, y)\) on a **scatter diagram**. If one variable is thought to influence the other, put the influencing variable on the horizontal axis. It is called the **explanatory** (or independent) variable. The other is the **response** (or dependent) variable.

:::def Correlation
A measure of how closely two variables follow a linear pattern. **Positive correlation**: as \(x\) increases, \(y\) tends to increase. **Negative correlation**: as \(x\) increases, \(y\) tends to decrease. **No correlation**: no linear pattern.
:::

:::html
<figure class="fig"><svg viewBox="0 0 590 195" role="img" aria-label="Three scatter diagrams: the points rise from left to right (positive correlation), fall from left to right (negative correlation), and are scattered with no pattern (no correlation)."><path class="ax" d="M20 160H180M20 160V35"/><circle class="fi" cx="36" cy="142" r="3.5"/><circle class="fi" cx="52" cy="126" r="3.5"/><circle class="fi" cx="68" cy="131" r="3.5"/><circle class="fi" cx="84" cy="111" r="3.5"/><circle class="fi" cx="100" cy="105" r="3.5"/><circle class="fi" cx="116" cy="89" r="3.5"/><circle class="fi" cx="132" cy="84" r="3.5"/><circle class="fi" cx="148" cy="65" r="3.5"/><circle class="fi" cx="164" cy="62" r="3.5"/><text class="tl" x="100" y="186" text-anchor="middle">Positive correlation</text><path class="ax" d="M215 160H375M215 160V35"/><circle class="fi" cx="231" cy="58" r="3.5"/><circle class="fi" cx="247" cy="74" r="3.5"/><circle class="fi" cx="263" cy="69" r="3.5"/><circle class="fi" cx="279" cy="89" r="3.5"/><circle class="fi" cx="295" cy="95" r="3.5"/><circle class="fi" cx="311" cy="111" r="3.5"/><circle class="fi" cx="327" cy="116" r="3.5"/><circle class="fi" cx="343" cy="135" r="3.5"/><circle class="fi" cx="359" cy="138" r="3.5"/><text class="tl" x="295" y="186" text-anchor="middle">Negative correlation</text><path class="ax" d="M410 160H570M410 160V35"/><circle class="fi" cx="426" cy="100" r="3.5"/><circle class="fi" cx="442" cy="64" r="3.5"/><circle class="fi" cx="458" cy="124" r="3.5"/><circle class="fi" cx="474" cy="82" r="3.5"/><circle class="fi" cx="490" cy="136" r="3.5"/><circle class="fi" cx="506" cy="70" r="3.5"/><circle class="fi" cx="522" cy="112" r="3.5"/><circle class="fi" cx="538" cy="88" r="3.5"/><circle class="fi" cx="554" cy="118" r="3.5"/><text class="tl" x="490" y="186" text-anchor="middle">No correlation</text></svg><figcaption>The three basic patterns on a scatter diagram.</figcaption></figure>
:::

When you describe a scatter diagram, say the **direction** (positive or negative), the **strength** (the closer the points are to a straight line, the stronger) and name the variables in context, for example "strong positive correlation between hours revised and score". Also look for **outliers**, points far from the pattern, which can distort the numbers below, and for **curved** patterns, where a straight-line measure is the wrong tool.

:::warn Correlation is not causation
Two variables can be strongly correlated without one causing the other. Ice cream sales and drownings both rise on hot days, because heat influences both. A third variable like this is called a **lurking variable**. In an exam, say "correlation does not imply causation" and, if you can, name a plausible lurking variable.
:::

## The product moment correlation coefficient

To put a number on the strength, use the **product moment correlation coefficient** \(r\) (PMCC). It is calculated from three sums of squares and products, which measure spread in \(x\), spread in \(y\), and how \(x\) and \(y\) vary together.

:::key Sums of squares and the PMCC
For \(n\) pairs \((x, y)\):
\[S_{xx} = \sum x^2 - \frac{(\sum x)^2}{n} \qquad S_{yy} = \sum y^2 - \frac{(\sum y)^2}{n} \qquad S_{xy} = \sum xy - \frac{\sum x \sum y}{n}\]
\[r = \frac{S_{xy}}{\sqrt{S_{xx}\,S_{yy}}}\]
- \(-1 \le r \le 1\).
- \(r = 1\): all points lie exactly on a line with positive gradient. \(r = -1\): exactly on a line with negative gradient.
- \(r\) near 0: no linear correlation. (There may still be a curved relationship.)
- \(r\) is unchanged if you change the units of \(x\) or \(y\) (for example cm to m), or add a constant to every value.
- \(r\) says nothing about the gradient of the line: \(r = 0.9\) does not mean the gradient is 0.9.
:::

:::eg Eight students record the hours \(x\) they revised and their test score \(y\):

| \(x\) | 2 | 3 | 5 | 6 | 8 | 9 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|
| \(y\) | 48 | 47 | 60 | 58 | 66 | 74 | 71 | 84 |

Calculate \(r\) and interpret it.
The sums are \(\sum x = 56\), \(\sum y = 508\), \(\sum x^2 = 484\), \(\sum y^2 = 33\,406\) and \(\sum xy = 3868\).
\[S_{xx} = 484 - \frac{56^2}{8} = 92 \qquad S_{yy} = 33\,406 - \frac{508^2}{8} = 1148 \qquad S_{xy} = 3868 - \frac{56 \times 508}{8} = 312\]
\[r = \frac{312}{\sqrt{92 \times 1148}} = \frac{312}{324.99} = 0.960\]
There is strong positive linear correlation between hours of revision and test score: more revision goes with higher scores.
:::

:::warn Describing \(r\)
Use the words "linear" and the context: "an \(r\) of 0.96 shows strong positive linear correlation between hours revised and score". Do not write "the gradient is 0.96", "96% of the marks come from revision", or "revision causes the score".
:::

## The least squares regression line

If the pattern is roughly linear you can draw a line through the points and use it to predict. The best line is the one that makes the vertical distances from the points to the line as small as possible overall.

:::def Residual and least squares
The **residual** of a point is the vertical distance from the point to the line: observed \(y\) minus predicted \(y\). The **least squares regression line** of \(y\) on \(x\) is the line \(y = a + bx\) for which the sum of the squares of the residuals is as small as possible.
:::

:::key Regression line of \(y\) on \(x\)
\[y = a + bx \qquad b = \frac{S_{xy}}{S_{xx}} \qquad a = \bar y - b\bar x\]
- The line always passes through the mean point \((\bar x, \bar y)\).
- \(b\) is the **gradient**: for each increase of 1 in \(x\), the predicted \(y\) changes by \(b\).
- \(a\) is the **intercept**: the predicted \(y\) when \(x = 0\). It may have no sensible meaning if \(x = 0\) is outside the data.
- Use it to predict \(y\) from \(x\), where \(x\) is the explanatory variable. The line of \(x\) on \(y\) is a different line and should not be used for that.
:::

:::proof Why \(b = S_{xy}/S_{xx}\) and \(a = \bar y - b\bar x\)
Choose \(a\) and \(b\) to make the sum of squared residuals \(S = \sum (y - a - bx)^2\) as small as possible. Treat \(S\) as a function of \(a\) and \(b\). At the minimum both slopes are zero. Differentiating with respect to \(a\), with \(b\) fixed:
\[\frac{\partial S}{\partial a} = -2\sum (y - a - bx) = 0 \quad\Rightarrow\quad \sum y - na - b\sum x = 0\]
Divide by \(n\): \(\bar y = a + b\bar x\), so \(a = \bar y - b\bar x\). The line passes through \((\bar x, \bar y)\).

Differentiating with respect to \(b\), with \(a\) fixed:
\[\frac{\partial S}{\partial b} = -2\sum x(y - a - bx) = 0 \quad\Rightarrow\quad \sum xy - a\sum x - b\sum x^2 = 0\]
Substitute \(a = \bar y - b\bar x\) and use \(\sum x = n\bar x\), \(\sum y = n\bar y\):
\[\sum xy - n\bar x\bar y = b\left(\sum x^2 - n\bar x^2\right)\]
The left side is \(S_{xy}\) and the bracket is \(S_{xx}\), so \(b = \dfrac{S_{xy}}{S_{xx}}\). Check with \(x = 1, 2, 3\), \(y = 2, 3, 7\): \(S_{xy} = 5\) and \(S_{xx} = 2\), so \(b = 2.5\), \(a = 4 - 2.5 \times 2 = -1\), and the residuals are \(0.5, -1, 0.5\), which add to 0.
:::

:::eg For the revision data, find the regression line of score on hours, interpret \(a\) and \(b\), and predict the score for a student who revises for 10 hours.
\(b = \dfrac{S_{xy}}{S_{xx}} = \dfrac{312}{92} = 3.391\). The means are \(\bar x = \dfrac{56}{8} = 7\) and \(\bar y = \dfrac{508}{8} = 63.5\), so
\[a = 63.5 - 3.391 \times 7 = 39.76\]
The line is \(y = 39.8 + 3.39x\) (3 s.f.).

Interpretation: each extra hour of revision is associated with about 3.4 more marks. A student who did no revision would be predicted to score about 40.

For \(x = 10\): \(y = 39.76 + 3.391 \times 10\) \(= 73.7\), a predicted score of about 74.
:::

:::plot The eight points and their least squares line \(y = 39.76 + 3.391x\). The line passes through the mean point (7, 63.5).
--f "39.76+3.391*x" --label "y = 39.76 + 3.391x" --x 0 14 --y 30 95 --pt "2,48" --pt "3,47" --pt "5,60" --pt "6,58" --pt "8,66" --pt "9,74" --pt "11,71" --pt "12,84" --pt "7,63.5,mean point (7, 63.5)@se" --xlabel "hours revised" --ylabel "score" --legend tl
:::

Residuals show how far each point is from the line. For the student with \(x = 9\), \(y = 74\), the prediction is \(39.76 + 3.391 \times 9 = 70.3\), so the residual is \(74 - 70.3 = 3.7\): this student did better than the line predicts. The residuals always add up to 0.

## Using the line: interpolation and extrapolation

:::def Interpolation and extrapolation
**Interpolation** is predicting \(y\) for a value of \(x\) inside the range of the data. **Extrapolation** is predicting for a value of \(x\) outside the range.
:::

Interpolation is usually reliable if the correlation is strong. Extrapolation is not: the pattern may not continue. In the revision example the data cover \(x\) from 2 to 12. For a student revising 20 hours the line predicts \(39.76 + 3.391 \times 20 = 107.6\), which is above a maximum score of 100 and clearly nonsense. A prediction is also less trustworthy when \(r\) is small, when there are very few points, or when the data come from a different group of people.

:::tip Commenting on a prediction
Two points earn the mark: say whether \(x\) lies inside or outside the data range (so interpolation or extrapolation), and say what that means for reliability. For example: "10 hours is within the range 2 to 12 and \(r\) is close to 1, so the estimate is reliable."
:::

## A hypothesis test for correlation

The sample \(r\) comes from a sample, so it might be large just by chance even if the population has no correlation. A **hypothesis test for correlation** asks whether \(r\) is far enough from 0 to be evidence of correlation in the whole population. Let \(\rho\) ("rho") be the population correlation coefficient.

:::steps
1. State \(H_0: \rho = 0\) and \(H_1: \rho > 0\) (or \(\rho < 0\)) for a one-tailed test, or \(H_1: \rho \ne 0\) for a two-tailed test. Say what \(\rho\) represents in context.
2. Find the sample size \(n\), the significance level and the critical value from the PMCC table supplied.
3. Compare: reject \(H_0\) if \(|r|\) is greater than the critical value (and has the right sign for a one-tailed test).
4. Write a conclusion in context.
:::

Critical values depend on \(n\) and on the board's tables, so use the table in your exam. For illustration, the 5% one-tailed critical values are:

| \(n\) | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| 5% one-tailed | 0.7293 | 0.6694 | 0.6215 | 0.5822 | 0.5494 | 0.5214 | 0.4973 |

For a two-tailed test at 5% use the 2.5% one-tailed values, for example 0.7067 for \(n = 8\) and 0.6319 for \(n = 10\).

:::eg For the 8 revision students \(r = 0.960\). Test at the 5% significance level whether there is positive correlation between hours revised and score in the population of all such students.
Let \(\rho\) be the population correlation coefficient between hours revised and score. \(H_0: \rho = 0\), \(H_1: \rho > 0\).
For \(n = 8\) the 5% one-tailed critical value is 0.6215. Since \(0.960 > 0.6215\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest positive correlation between hours revised and score.
:::

:::eg A sample of 7 pairs has \(r = 0.58\). Test at the 5% level whether there is positive correlation.
\(H_0: \rho = 0\), \(H_1: \rho > 0\). For \(n = 7\) the critical value is 0.6694. Since \(0.58 < 0.6694\), do not reject \(H_0\). There is insufficient evidence at the 5% level to suggest positive correlation. With only 7 pairs, even a correlation of 0.58 could easily arise by chance.
:::

## Exam-style question

:::eg (Exam style) A gas company records the mean monthly temperature \(x\,^\circ\)C and the gas used \(y\) (in units of 100 kWh) for 10 months. The data are summarised by \(\sum x = 140\), \(\sum y = 562\), \(\sum x^2 = 2516\), \(\sum y^2 = 34\,990\), \(\sum xy = 6506\). The temperatures range from 2 to 26. (a) Find \(r\) and describe the relationship. (b) Find the regression line of \(y\) on \(x\). (c) Estimate the gas used in a month with mean temperature 12 °C and comment on the reliability, and comment on an estimate for 30 °C. (d) Test at the 5% level (two-tailed) whether there is correlation, given that the critical value for \(n = 10\) is 0.6319. [13 marks]
(a) \(S_{xx} = 2516 - \dfrac{140^2}{10} = 556\), \(S_{yy} = 34\,990 - \dfrac{562^2}{10}\) \(= 3405.6\), \(S_{xy} = 6506 - \dfrac{140 \times 562}{10}\) \(= -1362\). [M1 A1]
\[r = \frac{-1362}{\sqrt{556 \times 3405.6}} = -0.990\] [M1 A1]
There is very strong negative linear correlation: warmer months use less gas. [B1]

(b) \(b = \dfrac{-1362}{556} = -2.45\). [M1] \(\bar x = 14\), \(\bar y = 56.2\), so \(a = 56.2 - (-2.4496)(14)\) \(= 90.5\). [M1] The line is \(y = 90.5 - 2.45x\). [A1]

(c) \(x = 12\): \(y = 90.495 - 2.4496 \times 12\) \(= 61.1\), about 6110 kWh. [B1] 12 is inside the range 2 to 26 and \(r\) is close to \(-1\), so the estimate is reliable. [B1] For 30 °C the line gives \(17.0\), but 30 is outside the data range, so this is extrapolation and may not be reliable. [B1]

(d) \(H_0: \rho = 0\), \(H_1: \rho \ne 0\). [B1] \(|r| = 0.990 > 0.6319\), so reject \(H_0\). There is sufficient evidence at the 5% level to suggest correlation between mean monthly temperature and gas used. [B1]
:::

:::exam What earns the marks
- Show the sums of squares \(S_{xx}\), \(S_{yy}\), \(S_{xy}\) separately: even if \(r\) is wrong, the method marks remain.
- Check the sign of \(r\) matches the sign of \(S_{xy}\) and of \(b\). They always share the same sign.
- Write comments in context and with the right words: "linear", "positive/negative", "strong/weak", "within/outside the range".
- Round \(r\), \(a\) and \(b\) to 3 s.f. unless told otherwise, but keep full values for later steps.
:::

:::board
- **CAIE 9709 does not examine correlation or regression**, so this chapter is optional for CAIE students.
- **Edexcel IAL**: correlation and regression are in IAL S1. Questions use \(S_{xx}\), \(S_{yy}\) and \(S_{xy}\).
- **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: scatter diagrams, correlation, regression lines and a hypothesis test for correlation using a table of critical values are in the course.
:::

:::eg Spot the error: which sum goes underneath
A student answered this question [5 marks]: "For 5 pairs, \(\sum x = 15\), \(\sum y = 40\), \(\sum x^2 = 55\), \(\sum y^2 = 340\) and \(\sum xy = 118\). Find the regression line of \(y\) on \(x\)."

Line 1: \(S_{xx} = 55 - \dfrac{15^2}{5} = 10\), \(S_{yy} = 340 - \dfrac{40^2}{5} = 20\), \(S_{xy} = 118 - \dfrac{15 \times 40}{5} = -2\).
Line 2: \(b = \dfrac{S_{xy}}{S_{yy}} = \dfrac{-2}{20} = -0.1\).
Line 3: \(a = \bar y - b\bar x\) \(= 8 - (-0.1)(3)\) \(= 8.3\), so \(y = 8.3 - 0.1x\).

**Line 1 earns [M1 A1]**. **Line 2 scores [M0 A0]**: the gradient of the line of \(y\) on \(x\) is \(S_{xy}/S_{xx}\), because \(x\) is the explanatory variable. Dividing by \(S_{yy}\) gives the gradient of the line of \(x\) on \(y\), which is a different line. **Line 3** uses the right method for \(a\) but with the wrong gradient, so the last mark [A0] is lost. The student scores 2 out of 5.

Correct working: \(b = \dfrac{-2}{10} = -0.2\), [M1 A1] \(a = 8 - (-0.2)(3) = 8.6\), so \(y = 8.6 - 0.2x\). [A1]

**Check:** the correct line passes through the mean point \((3, 8)\): \(8.6 - 0.2 \times 3 = 8\). The student's line does too, because of how \(a\) was found, so this check cannot catch the slip. Instead use the pair of gradients: \(b = -0.2\) and \(S_{xy}/S_{yy} = -0.1\) multiply to \(r^2\), since \((-0.2)(-0.1) = 0.02\) and \(r^2 = \dfrac{(-2)^2}{10 \times 20} = 0.02\). The student's \(-0.1\) belongs to the line of \(x\) on \(y\).
:::

:::try Start easy, finish at exam standard
Q: Describe the correlation you would expect between (a) the age of a used car and its price, (b) the height of adults and their shoe size, (c) a person's height and the number of their siblings.
A: (a) Negative: older cars sell for less. (b) Positive: taller people tend to have larger feet. (c) No correlation: there is no reason for the two to be related.
Q: \(S_{xx} = 40\), \(S_{yy} = 90\) and \(S_{xy} = -54\). Find \(r\) and the gradient \(b\) of the regression line of \(y\) on \(x\).
A: \(r = \dfrac{-54}{\sqrt{40 \times 90}} = \dfrac{-54}{60}\) \(= -0.9\). \(b = \dfrac{-54}{40} = -1.35\).
Q: For 6 pairs, \(\sum x = 30\), \(\sum y = 42\), \(\sum x^2 = 200\), \(\sum y^2 = 330\), \(\sum xy = 250\). Find \(r\) and the regression line of \(y\) on \(x\).
A: \(S_{xx} = 200 - 150 = 50\), \(S_{yy} = 330 - 294 = 36\), \(S_{xy} = 250 - 210 = 40\). \(r = \dfrac{40}{\sqrt{1800}} = 0.943\). \(b = \dfrac{40}{50} = 0.8\), \(a = 7 - 0.8 \times 5 = 3\). The line is \(y = 3 + 0.8x\).
Q: A regression line of ice cream sales \(y\) (in £100) on hours of sunshine \(x\) is \(y = 12.4 + 2.7x\). Interpret the numbers 2.7 and 12.4.
A: Each extra hour of sunshine is associated with £270 more sales on average (2.7 × £100). 12.4 is the predicted sales, £1240, with no sunshine; it may not be meaningful if the data include no days with no sun.
Q: The data for the line in the previous question had \(x\) between 2 and 10. Estimate sales for \(x = 6\) and for \(x = 14\), and comment.
A: \(x = 6\): \(12.4 + 16.2 = 28.6\), so £2860, and this is interpolation, so reasonably reliable. \(x = 14\): \(12.4 + 37.8 = 50.2\), so £5020, which is extrapolation, so unreliable.
Q: The points \((-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)\) lie exactly on the curve \(y = x^2\). Show that \(r = 0\) and explain what this means.
A: \(\sum x = 0\), so \(S_{xy} = \sum xy - 0\) \(= (-8 - 1 + 0 + 1 + 8) = 0\), giving \(r = 0\). There is no **linear** correlation, although \(y\) is completely determined by \(x\). \(r\) only measures straight-line patterns.
Q: A sample of 9 pairs has \(r = 0.71\). Test at the 5% level (critical value 0.5822 for a one-tailed test with \(n = 9\)) whether there is positive correlation.
A: \(H_0: \rho = 0\), \(H_1: \rho > 0\). Since \(0.71 > 0.5822\), reject \(H_0\). There is sufficient evidence at the 5% level to suggest positive correlation.
Q: A student finds a strong positive correlation between the number of fire engines sent to a fire and the damage it causes, and says "fire engines cause damage". Explain the error.
A: Correlation does not imply causation. A lurking variable, the size of the fire, causes both more fire engines to be sent and more damage.
Q: (Exam style) A sample of 12 pairs of data has \(r = -0.45\). Test at the 5% significance level whether there is negative correlation. The one-tailed critical value for \(n = 12\) is 0.4973. [4 marks]
A: \(H_0: \rho = 0\), \(H_1: \rho < 0\) [B1]. The critical region is \(r < -0.4973\) [M1]. Since \(-0.45\) is not less than \(-0.4973\) (that is, \(|r| = 0.45 < 0.4973\)) [A1], do not reject \(H_0\). There is insufficient evidence at the 5% level to suggest negative correlation. [B1]
Q: (Exam style) For the data \(\sum x = 90\), \(\sum y = 120\), \(\sum x^2 = 1000\), \(\sum xy = 1300\), with \(n = 10\), find the regression line of \(y\) on \(x\), and state the point through which the line passes. [6 marks]
A: \(S_{xy} = 1300 - \dfrac{90 \times 120}{10}\) \(= 220\). \(S_{xx} = 1000 - \dfrac{90^2}{10} = 190\). [M1 A1] \(b = \dfrac{220}{190} = 1.158\). [A1] \(\bar x = 9\), \(\bar y = 12\), \(a = 12 - 1.158 \times 9 = 1.58\). [M1 A1] The line is \(y = 1.58 + 1.16x\) and it passes through the mean point \((9, 12)\). [B1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A scatter diagram of the hours \(x\) a student watches television each week and their exam mark \(y\) gives \(r = -0.85\). (a) Describe the correlation. (b) Explain why this does not show that watching television lowers exam marks.
A: (a) There is strong negative linear correlation between hours of television and exam mark. [B1 B1] (b) Correlation does not imply causation: a lurking variable such as the amount of time spent studying could cause both, so the data alone do not show that television is the cause. [B1]
Q: [4 marks] ★ Six students have values \(x = 1, 2, 3, 4, 5, 6\) and \(y = 5, 7, 6, 9, 10, 12\). Given that \(\sum x = 21\), \(\sum y = 49\), \(\sum x^2 = 91\), \(\sum y^2 = 435\) and \(\sum xy = 195\), find the product moment correlation coefficient.
A: \(S_{xx} = 91 - \dfrac{21^2}{6} = 17.5\), \(S_{yy} = 435 - \dfrac{49^2}{6} = 34.83\), \(S_{xy} = 195 - \dfrac{21 \times 49}{6}\) \(= 23.5\). [M1 A1 A1] \(r = \dfrac{23.5}{\sqrt{17.5 \times 34.83}}\) \(= 0.952\). [A1]
Q: [6 marks] ★★ Use the data and sums in the previous question. (a) Find the equation of the regression line of \(y\) on \(x\). (b) Estimate \(y\) when \(x = 4.5\), and when \(x = 10\), commenting on the reliability of each.
A: (a) \(b = \dfrac{S_{xy}}{S_{xx}} = \dfrac{23.5}{17.5}\) \(= 1.343\). [M1 A1] \(\bar x = 3.5\) and \(\bar y = 8.167\), so \(a = 8.167 - 1.343 \times 3.5\) \(= 3.467\). [M1] The line is \(y = 3.47 + 1.34x\). [A1] (b) For \(x = 4.5\), \(y = 3.467 + 1.343 \times 4.5\) \(= 9.51\). This is interpolation (4.5 is inside the range 1 to 6) with \(r\) close to 1, so the estimate is reliable. [B1] For \(x = 10\), \(y = 16.9\). This is extrapolation, since 10 is outside the range of the data, so it may not be reliable. [B1]
Q: [4 marks] ★★ A sample of 10 pairs of values has \(r = -0.58\). Test, at the 5% significance level, whether there is any correlation between the two variables. The two-tailed critical value for \(n = 10\) is 0.6319.
A: Let \(\rho\) be the population correlation coefficient. \(H_0: \rho = 0\), \(H_1: \rho \ne 0\). [B1] The critical region is \(|r| > 0.6319\). [M1] Since \(|r| = 0.58 < 0.6319\), do not reject \(H_0\). [A1] There is insufficient evidence at the 5% level to suggest that there is correlation between the variables. [B1]
Q: [5 marks] ★★ The cost \(\pounds y\) of a taxi journey of \(x\) km is modelled by the regression line \(y = 2.4 + 1.15x\), found from journeys of between 3 km and 25 km. (a) Interpret the values 1.15 and 2.4 in context. (b) Estimate the cost of a 40 km journey and comment. (c) Explain why this line should not be used to estimate the distance for a cost of £20.
A: (a) Each extra kilometre adds about £1.15 to the cost on average. [B1] 2.4 is the fixed charge (the cost of a journey of 0 km), though no journey in the data was that short. [B1] (b) \(y = 2.4 + 1.15 \times 40 = 48.4\), so about £48.40. This is extrapolation (40 is outside 3 to 25), so it may be unreliable. [B1 B1] (c) The line of \(y\) on \(x\) minimises vertical distances for predicting cost from distance. To predict distance from cost you need the line of \(x\) on \(y\), which is a different line. [B1]
Q: [6 marks] ★★ For 9 pairs of values, \(S_{xx} = 48\), \(S_{yy} = 130\), \(S_{xy} = -72\), \(\bar x = 6\) and \(\bar y = 40\). Find (a) \(r\), (b) the regression line of \(y\) on \(x\).
A: (a) \(r = \dfrac{-72}{\sqrt{48 \times 130}}\) [M1] \(= -0.911\). [A1] (b) \(b = \dfrac{-72}{48} = -1.5\). [M1 A1] \(a = 40 - (-1.5)(6) = 49\), [M1] so \(y = 49 - 1.5x\). [A1]
Q: [10 marks] (#math.s2.hypothesis) ★★★ The hours \(x\) that 8 students revised and their scores \(y\) have \(S_{xx} = 92\), \(S_{yy} = 1148\), \(S_{xy} = 312\), \(\sum x = 56\), \(\sum y = 508\), \(\sum x^2 = 484\), \(\sum y^2 = 33\,406\) and \(\sum xy = 3868\). The regression line of score on hours is \(y = 39.76 + 3.391x\) and \(r = 0.960\). (a) A teacher records the revision time in minutes instead of hours. State the new value of \(r\) and find the new gradient. (b) Then every score is increased by 5 bonus marks. State the effect on \(r\) and on the gradient, and find the new intercept. (c) Going back to the original data, a ninth student revised for 10 hours and scored 20. Find the new value of \(r\) for all 9 students. Test at the 5% level (one-tailed critical value 0.5822 for \(n = 9\)) whether there is positive correlation, and comment on the effect of this student.
H: Changing units multiplies every \(x\) by 60. How does that change \(S_{xx}\) and \(S_{xy}\), and what happens to \(r\) and \(b = S_{xy}/S_{xx}\)?
H: Adding 5 to every \(y\) moves the mean of \(y\) up by 5 but does not change any distances from the mean.
H: For (c) update the five sums with the new point, then recalculate \(S_{xx}\), \(S_{yy}\) and \(S_{xy}\) for \(n = 9\).
A: (a) The correlation coefficient does not depend on units, so \(r = 0.960\) still. [B1] Multiplying \(x\) by 60 multiplies \(S_{xx}\) by \(60^2\) and \(S_{xy}\) by 60, so the gradient is divided by 60: [M1] \(b' = \dfrac{3.391}{60} = 0.0565\). [A1] (b) Adding a constant to every score leaves \(r\) and the gradient unchanged. [B1] The mean score rises by 5 and the line still passes through the mean point, so the intercept becomes \(39.76 + 5 = 44.8\). [B1] (c) The new sums are \(\sum x = 66\), \(\sum y = 528\), \(\sum x^2 = 584\), \(\sum y^2 = 33\,806\), \(\sum xy = 4068\), so [M1] \(S_{xx} = 584 - \dfrac{66^2}{9} = 100\), \(S_{yy} = 33\,806 - \dfrac{528^2}{9} = 2830\), \(S_{xy} = 4068 - \dfrac{66 \times 528}{9}\) \(= 196\), and \(r = \dfrac{196}{\sqrt{100 \times 2830}} = 0.368\). [A1] \(H_0: \rho = 0\), \(H_1: \rho > 0\). Since \(0.368 < 0.5822\), do not reject \(H_0\): [M1 A1] there is insufficient evidence at the 5% level to suggest positive correlation. One unusual student has turned a strongly significant result into a non-significant one, so single outliers can have a large effect on \(r\). [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ For a regression of \(y\) on \(x\) with \(y = a + bx\), (a) show that the line passes through \((\bar x, \bar y)\); (b) show that the residuals \(y - (a + bx)\) add up to 0; (c) the regression line of \(x\) on \(y\) is \(x = c + dy\) with \(d = \dfrac{S_{xy}}{S_{yy}}\). Show that \(bd = r^2\). Check with the revision data.
H: Start from \(a = \bar y - b\bar x\). Rearrange it to show that the point \((\bar x, \bar y)\) satisfies \(y = a + bx\).
H: For (c), write \(b\) and \(d\) using \(S_{xx}\), \(S_{yy}\) and \(S_{xy}\), and multiply.
A: (a) Since \(a = \bar y - b\bar x\), we have \(\bar y = a + b\bar x\), [M1] so the point \((\bar x, \bar y)\) lies on the line. [A1] (b) \(\sum (y - a - bx)\) \(= n\bar y - na - bn\bar x\) [M1] \(= n(\bar y - a - b\bar x) = 0\). [A1] (c) \(bd = \dfrac{S_{xy}}{S_{xx}} \times \dfrac{S_{xy}}{S_{yy}}\) \(= \dfrac{S_{xy}^2}{S_{xx}S_{yy}}\) [M1] \(= \left(\dfrac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}\right)^2 = r^2\). [A1] Check: \(b = 3.391\) and \(d = \dfrac{312}{1148} = 0.2718\), and \(bd = 0.9217 = 0.960^2\). The two lines coincide only when \(r = \pm 1\).
Q: [5 marks] ★★★ Group A has the points \((1, 10), (2, 11), (3, 12)\) and group B has the points \((6, 2), (7, 3), (8, 4)\). (a) Find the correlation coefficient within each group. (b) Combine the six points and find \(r\) for the combined data. (c) Explain what this shows about data from different groups.
H: Each group lies exactly on a line of gradient 1.
H: For the combined data \(\bar x = 4.5\) and \(\bar y = 7\). Work with deviations from these means.
A: (a) Each group lies exactly on a line with gradient 1, so \(r = 1\) for each. [B1] (b) For the combined data the deviations \(x - 4.5\) are \(-3.5, -2.5, -1.5, 1.5, 2.5, 3.5\) and \(y - 7\) are \(3, 4, 5, -5, -4, -3\). Then \(S_{xx} = 41.5\), \(S_{yy} = 100\) and \(S_{xy} = -56\). [M1 A1] So \(r = \dfrac{-56}{\sqrt{41.5 \times 100}}\) \(= -0.869\). [A1] (c) Each group has a perfect positive relationship, but the combined data show strong negative correlation. Mixing groups with different levels can reverse the apparent relationship, so look for subgroups before interpreting \(r\). [B1]
:::

:::quiz Check your understanding
? \(r = -0.95\). Which statement is correct?
+ There is strong negative linear correlation.
- There is weak negative correlation.
- \(y\) decreases by 0.95 for every unit increase in \(x\).
- 95% of the values of \(y\) are explained by \(x\) being negative.
> A value close to \(-1\) means strong negative linear correlation. The size of \(r\) is not the gradient.
? The least squares regression line of \(y\) on \(x\) always passes through:
- the origin
- the first data point
+ the mean point \((\bar x, \bar y)\)
- the point \((\sum x, \sum y)\)
> \(a = \bar y - b\bar x\) means that \(\bar y = a + b\bar x\), so the line passes through \((\bar x, \bar y)\).
? Which of these can **not** be a value of \(r\)?
- \(-1\)
- 0
- 0.2
+ 1.3
> The correlation coefficient always lies between \(-1\) and 1.
? The regression line \(y = 5 + 2.5x\) is based on data with \(x\) between 10 and 40. Which prediction is least reliable?
- \(x = 15\)
- \(x = 25\)
+ \(x = 80\)
- \(x = 38\)
> 80 is far outside the range 10 to 40, so it is extrapolation. The others are interpolation.
? You change \(y\) from centimetres to metres. What happens to \(r\)?
- it is divided by 100
+ it stays the same
- it is multiplied by 100
- it becomes negative
> \(r\) is unaffected by a change of units, which is a positive linear change. The gradient \(b\) changes, but \(r\) does not.
:::

:::checklist What you can now do
- [ ] I can describe a scatter diagram: direction, strength, outliers and curved patterns.
- [ ] I can calculate \(S_{xx}\), \(S_{yy}\), \(S_{xy}\) and the product moment correlation coefficient \(r\) from summary statistics.
- [ ] I can interpret \(r\) in context, and explain why correlation does not imply causation.
- [ ] I can find the least squares regression line \(y = a + bx\) and interpret \(a\) and \(b\) in context.
- [ ] I can use the line to predict, and say whether a prediction is interpolation or extrapolation and how reliable it is.
- [ ] I can test for correlation using a table of critical values, and write the conclusion in context.
- [ ] I can say how changing units, or adding a constant, or one extra outlier changes \(r\) and the line.
:::

:::recap
- Describe a scatter diagram by direction, strength and context. Correlation is not causation.
- \(S_{xx} = \sum x^2 - \dfrac{(\sum x)^2}{n}\), \(S_{yy}\) likewise, \(S_{xy} = \sum xy - \dfrac{\sum x\sum y}{n}\). \(r = \dfrac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}\), with \(-1 \le r \le 1\).
- Regression of \(y\) on \(x\): \(y = a + bx\), \(b = \dfrac{S_{xy}}{S_{xx}}\), \(a = \bar y - b\bar x\). The line passes through \((\bar x, \bar y)\).
- Interpret \(b\) as the change in \(y\) per unit \(x\). Interpolate with care, and do not extrapolate.
- Test for correlation: \(H_0: \rho = 0\). Reject if \(|r|\) exceeds the critical value for \(n\) and the significance level. Conclude in context.
:::

:::links
- watch: [Regression](https://www.examsolutions.net/tutorials/regression/) · ExamSolutions · the least squares line from summary statistics
- watch: [Hypothesis testing for zero correlation](https://www.examsolutions.net/tutorials/hypothesis-testing-zero-correlation/) · ExamSolutions · the UK-board test
- practise: [Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) · Khan Academy · units on scatter plots and correlation
- explore: [Least-Squares Regression](https://phet.colorado.edu/en/simulations/least-squares-regression) · PhET · place points and watch the line and r change
- explore: [Regression analysis](https://seeing-theory.brown.edu/regression-analysis/index.html) · Seeing Theory · interactive least squares

Links checked 3 October 2026.
:::
Next: [Forces and equilibrium](#math.m.forces).
