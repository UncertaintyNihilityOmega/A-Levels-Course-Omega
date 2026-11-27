@chapter math.fm.contingency
@title Chi-squared tests for independence
@level fm
@paper CAIE 9231 Paper 4
@time 4–6 hours
@summary A contingency table counts people or things by two categories at once. You will test whether the two categories are independent (no association): find each expected frequency as row total times column total over grand total, combine rows or columns so every expected frequency is at least 5, calculate \(X^2\) with \(\nu = (r - 1)(c - 1)\) degrees of freedom, and explain in context which cells caused the result.

:::why
Does the way students travel to school affect whether they arrive on time? Does a medicine work better for one age group than another? Do customers in different towns prefer different products? Each question asks whether two categories are linked, and the data come as a table of counts. The chi-squared test of independence answers it with the same statistic as the goodness-of-fit test, and it is how researchers decide, from a survey, whether a connection is real or could just be chance.
:::

**Before you start**, you need independent events and \(P(A \cap B) = P(A)P(B)\) from [Probability](#math.s1.prob), and the statistic \(X^2\), the rule of 5, the table of \(\chi^2\) values and the wording of a conclusion from [Chi-squared goodness of fit](#math.fm.chisq). Hypothesis testing in general is in [Hypothesis testing](#math.s2.hypothesis).

:::try Warm-up
Q: \(A\) and \(B\) are independent events with \(P(A) = 0.4\) and \(P(B) = 0.3\). Find \(P(A \cap B)\). (from [Probability](#math.s1.prob))
A: For independent events \(P(A \cap B) = P(A) \times P(B) = 0.4 \times 0.3 = 0.12\).
Q: A goodness-of-fit test has 6 classes after combining, and one parameter was estimated from the data. State \(\nu\) and the 5% critical value. (from [Chi-squared goodness of fit](#math.fm.chisq))
A: \(\nu = 6 - 1 - 1 = 4\), and the critical value (column \(p = 0.95\)) is 9.488.
Q: Observed frequencies are 12 and 18 and both expected frequencies are 15. Find \(X^2\). (from [Chi-squared goodness of fit](#math.fm.chisq))
A: \(X^2 = \dfrac{(12 - 15)^2}{15} + \dfrac{(18 - 15)^2}{15} = 0.6 + 0.6 = 1.2\).
:::

## Contingency tables and association

A survey asks 300 students how they travel to school (cycle or bus) and whether they arrived on time yesterday. Each student goes in exactly one of four boxes, and the counts form a table.

:::def Contingency table
A table of counts in which each observation is classified by two categorical variables, one down the rows and one across the columns. The counts in the cells are the **observed frequencies**. The totals along the edges are the **row totals** and **column totals**, and the total of all observations is the **grand total** \(N\).
:::

| | On time | Late | Total |
|---|---|---|---|
| Cycle | 78 | 22 | 100 |
| Bus | 110 | 90 | 200 |
| Total | 188 | 112 | 300 |

Look at the rows. Among cyclists, \(\tfrac{78}{100} = 78\%\) were on time; among bus users \(\tfrac{110}{200} = 55\%\). Is that gap a real difference between the two ways of travelling, or just the ordinary variation you get from sampling 300 students? The test of independence decides.

:::def Independent, associated
Two categorical variables are **independent** if knowing the category of one tells you nothing about the other: in every row the shares across the columns are the same. If they are not independent, there is an **association** between them.
:::

The hypotheses always say this in words, naming both variables:

:::key Hypotheses for a test of independence
\(H_0\): there is no association between (variable 1) and (variable 2); that is, they are independent.
\(H_1\): there is an association between (variable 1) and (variable 2).
Name the variables in context ("travel method" and "arriving on time"), not "the rows" and "the columns". Writing "dependent" instead of "associated" is accepted, but never "causes".
:::

## Expected frequencies

If \(H_0\) is true, the probability that an observation falls in row \(i\) and column \(j\) is the product of the two separate probabilities. The best estimates of those probabilities come from the totals: the probability of row \(i\) is \(\dfrac{R_i}{N}\) and of column \(j\) is \(\dfrac{C_j}{N}\), where \(R_i\) and \(C_j\) are the row and column totals.

:::key Expected frequency
\[E_{ij} = \frac{R_i \times C_j}{N} = \frac{\text{row total} \times \text{column total}}{\text{grand total}}\]
Calculate this for every cell. The expected frequencies have the same row totals and column totals as the observed ones.
:::

:::proof Why the expected frequency is row total times column total over grand total
Under independence, \(P(\text{row } i \text{ and column } j) = P(\text{row } i) \times P(\text{column } j)\). Estimate \(P(\text{row } i)\) by \(\dfrac{R_i}{N}\), the proportion of all observations in row \(i\), and \(P(\text{column } j)\) by \(\dfrac{C_j}{N}\). The expected number of the \(N\) observations in that cell is \(N\) times the probability:
\[E_{ij} = N \times \frac{R_i}{N} \times \frac{C_j}{N} = \frac{R_i C_j}{N}\]
In the travel table, 100 of 300 students cycle and 188 of 300 are on time, so independence predicts \(300 \times \tfrac{100}{300} \times \tfrac{188}{300} = \tfrac{100 \times 188}{300} = 62.67\) cyclists on time.
:::

Once all the expected frequencies are found, the test statistic is the same as before:
\[X^2 = \sum \frac{(O - E)^2}{E}\]
summed over every cell of the table.

## Degrees of freedom

:::key Degrees of freedom for a contingency table
For a table with \(r\) rows and \(c\) columns (the totals are not counted),
\[\nu = (r - 1)(c - 1)\]
Compare \(X^2\) with the upper-tail critical value of \(\chi^2_\nu\), as for goodness of fit.
:::

Here is why. The expected table has to match the row and column totals. So once you have chosen the cells in all but one row and all but one column, there are \((r - 1)(c - 1)\) cells you can choose freely and the rest are fixed by the totals. Another way to count: the table has \(rc\) cells; one degree of freedom is lost because the frequencies add to \(N\), and \((r - 1) + (c - 1)\) more because the row and column probabilities were estimated from the data. Then \(rc - 1 - (r - 1) - (c - 1) = (r - 1)(c - 1)\).

| Table | \(2 \times 2\) | \(2 \times 3\) | \(3 \times 3\) | \(3 \times 4\) | \(4 \times 5\) |
|---|---|---|---|---|---|
| \(\nu\) | 1 | 2 | 4 | 6 | 12 |

:::steps
1. State \(H_0\) (no association between the two variables, named in context) and \(H_1\).
2. Add up the row totals, column totals and grand total.
3. Calculate every \(E = \dfrac{\text{row total} \times \text{column total}}{\text{grand total}}\).
4. If any \(E\) is below 5, combine adjacent rows or columns, find the new totals and recalculate \(E\) for the new table.
5. Calculate \(X^2 = \sum \dfrac{(O - E)^2}{E}\) over all cells of the table you are using.
6. Find \(\nu = (r - 1)(c - 1)\) from the **new** table size, and read the critical value from the \(\chi^2\) table.
7. Compare, and write a conclusion in context.
:::

This is the goodness-of-fit test with a different way to find \(E\) and \(\nu\). The table below shows what changes.

| | Goodness of fit | Independence |
|---|---|---|
| Data | one row of class frequencies | two-way table |
| \(H_0\) | the data follow a stated distribution | no association between two variables |
| \(E\) | \(N \times P(\text{class})\) from the model | \(\dfrac{\text{row total} \times \text{column total}}{N}\) |
| \(\nu\) | classes \(- 1 -\) parameters estimated | \((r - 1)(c - 1)\) |
| Rule of 5 | combine adjacent classes | combine adjacent rows or columns |

Try the widget. A \(3 \times 4\) table has \(\nu = 6\). With the level at 5%, type the statistic 22.88 (from the worked example later in this chapter) and see where it falls, then change the level to 1%.

:::html
<div class="widget" data-w="fm-chisq" data-v="6" data-alpha="0.05" data-x2="22.88"></div>
:::

## Worked examples: \(2 \times 2\) and \(2 \times 3\)

:::eg The travel data above: of 100 cyclists, 78 were on time; of 200 bus users, 110 were on time. Test at the 5% significance level whether arriving on time is associated with the way students travel.
\(H_0\): there is no association between travel method and arriving on time. \(H_1\): there is an association.

The totals are in the table: rows 100 and 200, columns 188 and 112, \(N = 300\). The expected frequencies are
\[E_{11} = \frac{100 \times 188}{300} = 62.67, \quad E_{12} = \frac{100 \times 112}{300} = 37.33\]
\[E_{21} = \frac{200 \times 188}{300} = 125.3, \quad E_{22} = \frac{200 \times 112}{300} = 74.67\]
All are at least 5. The contributions \(\dfrac{(O - E)^2}{E}\) are:

| | On time | Late |
|---|---|---|
| Cycle | 3.752 | 6.298 |
| Bus | 1.876 | 3.149 |

\[X^2 = 3.752 + 6.298 + 1.876 + 3.149 = 15.07\]
The table has 2 rows and 2 columns, so \(\nu = (2 - 1)(2 - 1) = 1\) and the 5% critical value is 3.841. Since \(15.07 > 3.841\), reject \(H_0\): there is sufficient evidence, at the 5% level, of an association between travel method and arriving on time. The result is also significant at 1%, because 15.07 is above 6.635.

Cyclists were on time more often than independence predicts (78 against 62.67) and late less often (22 against 37.33): the data suggest cyclists are more reliably on time. The test shows a link, not the reason for it.
:::

For a \(2 \times 2\) table, \(\nu = 1\) and 9231 does not use a continuity correction (Yates' correction).

:::eg A school asks 190 students which revision method helps most: flashcards, past papers or notes. Of 90 Year 12 students, 28, 45 and 17 chose these; of 100 Year 13 students, 22, 60 and 18. Test at the 5% level whether the choice of method is associated with year group.
\(H_0\): there is no association between year group and favourite revision method. \(H_1\): there is an association.

Row totals 90 and 100; column totals 50, 105 and 35; \(N = 190\).

| | Flashcards | Past papers | Notes |
|---|---|---|---|
| Year 12: \(O\) | 28 | 45 | 17 |
| Year 12: \(E\) | 23.68 | 49.74 | 16.58 |
| Year 13: \(O\) | 22 | 60 | 18 |
| Year 13: \(E\) | 26.32 | 55.26 | 18.42 |

For example \(E_{11} = \dfrac{90 \times 50}{190} = 23.68\). The contributions are 0.786, 0.451, 0.011 for Year 12 and 0.708, 0.406, 0.010 for Year 13:
\[X^2 = 0.786 + 0.451 + 0.011 + 0.708 + 0.406 + 0.010 = 2.37\]
\(\nu = (2 - 1)(3 - 1) = 2\), and the critical value is 5.991. Since \(2.37 < 5.991\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, of an association between year group and favourite revision method.
:::

:::warn Use frequencies, never percentages
The test needs the actual counts. A table of percentages (or proportions) has lost \(N\), and \(X^2\) grows in proportion to \(N\) (a sample twice as big with the same proportions doubles \(X^2\)), so the answer would be meaningless. If a question gives percentages and a sample size, turn them back into frequencies first.
:::

## Combining rows and columns

The chi-squared approximation needs every expected frequency to be at least 5, exactly as in goodness of fit. Small expected frequencies happen when a category is rare: a row or column with a small total.

- Combine **adjacent** categories that make sense together: age bands next to each other, "agree" with "strongly agree", "2 cars" with "3 or more". Never combine unlike categories just to fix a number.
- Add the **observed** frequencies of the merged rows or columns, work out the new totals, and calculate the expected frequencies for the new table. Adding the old expected frequencies of the merged cells gives the same values, which is a good check.
- Do it **before** calculating \(X^2\). Then \(\nu = (r - 1)(c - 1)\) uses the **new** number of rows and columns.
- Combine only as much as you need.

:::eg A transport survey of 270 adults records age group and usual way to travel to work.

| | Train | Bus | Car | Total |
|---|---|---|---|---|
| 18 to 29 | 28 | 24 | 28 | 80 |
| 30 to 49 | 40 | 32 | 38 | 110 |
| 50 to 64 | 20 | 12 | 36 | 68 |
| 65 and over | 2 | 2 | 8 | 12 |
| Total | 90 | 70 | 110 | 270 |

Test at the 5% level whether the way people travel is associated with age group.
\(H_0\): there is no association between age group and usual way to travel. \(H_1\): there is an association.

The expected frequencies for the last row are \(\dfrac{12 \times 90}{270} = 4.00\), \(\dfrac{12 \times 70}{270} = 3.11\) and \(\dfrac{12 \times 110}{270} = 4.89\), all below 5. Combine the last two rows ("50 and over"), the adjacent ones, to give a row \(22, 14, 44\) with total 80.

| | Train | Bus | Car |
|---|---|---|---|
| 18 to 29: \(O\) (\(E\)) | 28 (26.67) | 24 (20.74) | 28 (32.59) |
| 30 to 49: \(O\) (\(E\)) | 40 (36.67) | 32 (28.52) | 38 (44.81) |
| 50 and over: \(O\) (\(E\)) | 22 (26.67) | 14 (20.74) | 44 (32.59) |

The contributions are 0.067, 0.512, 0.647; 0.303, 0.425, 1.036; 0.817, 2.191, 3.993.
\[X^2 = 9.99\]
The new table has 3 rows and 3 columns: \(\nu = (3 - 1)(3 - 1) = 4\), with critical value 9.488. Since \(9.99 > 9.488\), reject \(H_0\): there is sufficient evidence, at the 5% level, of an association between age group and the usual way to travel. The largest contributions are in the last row: people aged 50 and over use the bus less (14 against 20.74) and the car more (44 against 32.59) than independence predicts.
:::

Notice the trap in the working: if you had kept the four rows and used \(\nu = (4 - 1)(3 - 1) = 6\), you would have got a slightly larger statistic (about 10.96), but with \(\nu = 6\) the critical value is 12.592, so you would not have rejected. The rule of 5 is not a technicality: it can change the conclusion.

## Which cells matter

The terms \(\dfrac{(O - E)^2}{E}\), one per cell, show where the table departs from independence. After a rejection, name the cells with the largest terms and say, in context, whether \(O\) is above or below \(E\). Examiners reward that comparison of observed and expected frequencies: a mark for the right cell, a second for the comparison.

:::eg (Exam style) A school records how 420 students in Years 7, 9 and 11 travel to school.

| | Walk | Cycle | Bus | Car | Total |
|---|---|---|---|---|---|
| Year 7 | 36 | 12 | 30 | 42 | 120 |
| Year 9 | 38 | 22 | 40 | 40 | 140 |
| Year 11 | 20 | 38 | 56 | 46 | 160 |
| Total | 94 | 72 | 126 | 128 | 420 |

(a) Test at the 5% significance level whether the way students travel is independent of their year group. (b) State which cell contributes most to the test statistic, and describe what it shows about the students.
**(a)** \(H_0\): there is no association between year group and way of travelling. \(H_1\): there is an association. [B1]

The expected frequencies are \(\dfrac{\text{row total} \times \text{column total}}{420}\). For example \(E_{11} = \dfrac{120 \times 94}{420} = 26.86\).

| | Walk | Cycle | Bus | Car |
|---|---|---|---|---|
| Year 7 | 26.86 | 20.57 | 36.00 | 36.57 |
| Year 9 | 31.33 | 24.00 | 42.00 | 42.67 |
| Year 11 | 35.81 | 27.43 | 48.00 | 48.76 |

All are at least 5, so no rows or columns are combined. [M1 A1]

The values of \(\dfrac{(O - E)^2}{E}\) are

| | Walk | Cycle | Bus | Car |
|---|---|---|---|---|
| Year 7 | 3.112 | 3.571 | 1.000 | 0.806 |
| Year 9 | 1.418 | 0.167 | 0.095 | 0.167 |
| Year 11 | 6.980 | 4.074 | 1.333 | 0.156 |

\[X^2 = 3.112 + 3.571 + 1.000 + \dots + 0.156 = 22.9\] [M1 A1]
\(\nu = (3 - 1)(4 - 1) = 6\), and the 5% critical value is 12.592. Since \(22.9 > 12.592\), reject \(H_0\): there is sufficient evidence, at the 5% level, of an association between year group and way of travelling to school. [M1 A1]

**(b)** The largest contribution is 6.980: Year 11 students who walk. [B1]
Only 20 Year 11 students walk, against 35.81 expected if travel and year group were independent, so older students walk much less than the table for all years predicts (they cycle more: 38 against 27.43). [DB1]
:::

The method mark for the comparison needed the right \(\nu\) (6) and its critical value: a wrong \(\nu\) cannot earn it, so the degrees-of-freedom line is worth writing down every time.

:::eg (Exam style) A survey of 320 households in three towns records the number of cars each household owns.

| | 0 cars | 1 car | 2 cars | 3 or more | Total |
|---|---|---|---|---|---|
| Town A | 46 | 30 | 12 | 2 | 90 |
| Town B | 50 | 38 | 14 | 8 | 110 |
| Town C | 44 | 50 | 22 | 4 | 120 |
| Total | 140 | 118 | 48 | 14 | 320 |

(a) Test at the 5% level whether the number of cars owned is associated with the town. (b) Explain why two of the columns were combined, and state the effect on \(\nu\).
**(a)** \(H_0\): there is no association between town and number of cars owned. \(H_1\): there is an association. [B1]

The expected frequency for "3 or more" is \(\dfrac{90 \times 14}{320} = 3.94\) for Town A, 4.81 for Town B and 5.25 for Town C. [M1]

Two of these are below 5, so combine the last two columns ("2 or more"), the neighbours that make sense together. The new column has observed frequencies 14, 22 and 26 and total 62. [M1]

| | 0 cars | 1 car | 2 or more |
|---|---|---|---|
| Town A: \(O\) (\(E\)) | 46 (39.38) | 30 (33.19) | 14 (17.44) |
| Town B: \(O\) (\(E\)) | 50 (48.13) | 38 (40.56) | 22 (21.31) |
| Town C: \(O\) (\(E\)) | 44 (52.50) | 50 (44.25) | 26 (23.25) |

All the expected frequencies are now at least 5. [A1]

The contributions are 1.115, 0.306, 0.678; 0.073, 0.162, 0.022; 1.376, 0.747, 0.325.
\[X^2 = 1.115 + 0.306 + 0.678 + \dots + 0.325 = 4.80\] [M1 A1]
\(\nu = (3 - 1)(3 - 1) = 4\), and the critical value is 9.488. Since \(4.80 < 9.488\), do not reject \(H_0\): there is insufficient evidence, at the 5% level, of an association between the town and the number of cars owned. [M1 A1]

**(b)** Two of the expected frequencies in the last column were below 5, and the chi-squared approximation is not reliable then. [B1]
The table went from 4 columns to 3, so \(\nu\) is \((3 - 1)(3 - 1) = 4\) rather than \((3 - 1)(4 - 1) = 6\). [B1]
:::

:::exam What the June 2026 Paper 4 question showed
The June 2026 Paper 4 included an 8-mark test of independence on a \(3 \times 3\) table of three bus companies (A, B and C) against whether a journey was on time, late or cancelled, with one small expected frequency (3.50). Its marks went to: both hypotheses, naming the two variables (B1); the expected frequencies seen (M1, then A1 for all correct to 3 significant figures); combining rows or columns (M1); the contributions, with at least two correct expressions (M1) and the statistic (A1); comparing with the correct critical value (M1); a conclusion in context (A1). A solution that did not combine could earn at most 5 of the 8 marks. A two-mark part then asked which of the three companies was least reliable and why, by comparing observed and expected frequencies. In the conclusion the scheme accepted "association" for "not independent", did not accept "no evidence", and wanted "insufficient evidence" (or "not enough evidence") for a non-significant result. The MF19 table is printed, so you read the critical value from it; the rule \(E = \dfrac{RC}{N}\), \(X^2 = \sum \dfrac{(O - E)^2}{E}\) and \(\nu = (r - 1)(c - 1)\) must be learned.
:::

:::board
Edexcel IAL Statistics 3 also tests independence in contingency tables with the same statistic and the same rule that expected frequencies must be at least 5. In 9231 a \(2 \times 2\) table is tested without Yates' correction; if a textbook applies it, ignore that step here.
:::

:::eg Spot the error: the satisfaction of customers at three branches (Low, Medium, High) is recorded for 300 customers. Branch A: 2, 34, 44; Branch B: 6, 50, 64; Branch C: 2, 26, 72. A student tests at the 5% level whether satisfaction is associated with branch, for 8 marks.
A student wrote this answer.

Line 1: \(H_0\): no association between branch and satisfaction. \(H_1\): there is an association. [B1]
Line 2: The expected frequencies in the Low column are 2.67, 4.00 and 3.33, all below 5. [M1] [A1]
Line 3: Combine Low and Medium, giving observed frequencies 36, 44; 56, 64; 28, 72. [M1]
Line 4:
\[X^2 = 0.500 + 0.333 + 1.333 + 0.889 + 3.600 + 2.400 = 9.06\] [M1] [A1]
Line 5: \(\nu = (3 - 1)(3 - 1) = 4\), critical value 9.488. \(9.06 < 9.488\), so do not reject \(H_0\): insufficient evidence of an association. [M0] [A0]

Lines 1 to 4 are correct and earn their six marks.

**Line 5 uses the wrong \(\nu\).** After combining, the table has 3 rows and 2 columns, so \(\nu = (3 - 1)(2 - 1) = 2\), not 4. The student used the size of the original table. With the wrong critical value the comparison earns no method mark, and the conclusion, which is the opposite of the right one, earns no accuracy mark. The student scores 6 out of 8.

Correct line 5: \(\nu = 2\), critical value 5.991, and \(9.06 > 5.991\). [M1]
Reject \(H_0\): there is sufficient evidence, at the 5% level, of an association between branch and satisfaction. [A1]
:::

:::try Start easy, finish at exam standard
Q: A \(2 \times 2\) table has observed frequencies 24, 16 in the first row and 36, 24 in the second. Find the expected frequencies and \(X^2\), and say what the result shows.
A: Row totals 40 and 60, column totals 60 and 40, \(N = 100\). \(E = \dfrac{40 \times 60}{100} = 24\), \(16\), \(36\), \(24\). These equal the observed values, so \(X^2 = 0\): the proportions in the two rows are identical (60% and 40% in the columns each time), which is perfect independence.
Q: State \(\nu\) for a test of independence on (a) a table with 2 rows and 2 columns, (b) 4 rows and 3 columns, (c) 3 rows and 5 columns, (d) a table with 4 rows and 5 columns in which two rows are combined.
A: (a) \(1 \times 1 = 1\). (b) \(3 \times 2 = 6\). (c) \(2 \times 4 = 8\). (d) Combining gives 3 rows and 5 columns: \(2 \times 4 = 8\).
Q: The expected frequencies in a \(2 \times 3\) table are 3.2, 12.8, 14.0 in row 1 and 4.8, 19.2, 21.0 in row 2. Which columns should be combined, what are the new expected frequencies, and what is \(\nu\)?
A: The first column has two values below 5, so combine columns 1 and 2: \(3.2 + 12.8 = 16.0\) and \(4.8 + 19.2 = 24.0\). The new expected frequencies are 16.0, 14.0, 24.0, 21.0, all at least 5, and \(\nu = (2 - 1)(2 - 1) = 1\).
Q: A \(2 \times 2\) table has rows 18, 12 and 10, 20. Test at the 5% level whether the two variables are independent.
A: Row totals 30 and 30, column totals 28 and 32, \(N = 60\). \(E = 14, 16, 14, 16\). \(X^2 = \dfrac{16}{14} + \dfrac{16}{16} + \dfrac{16}{14} + \dfrac{16}{16} = 4.29\). \(\nu = 1\), critical value 3.841. Since \(4.29 > 3.841\), reject \(H_0\): sufficient evidence, at the 5% level, of an association.
Q: A \(2 \times 3\) table has rows 25, 35, 20 and 15, 25, 30. Test at the 5% level whether the variables are independent.
A: Row totals 80 and 70, column totals 40, 60, 50, \(N = 150\). \(E = 21.33, 32.00, 26.67\) and \(18.67, 28.00, 23.33\). 
\[X^2 = 0.630 + 0.281 + 1.667 + 0.720 + 0.321 + 1.905 = 5.52\]
Then \(\nu = 2\), critical value 5.991. Since \(5.52 < 5.991\), do not reject \(H_0\): insufficient evidence of an association.
Q: A student turns every row of a table into percentages (each row adds to 100) and then calculates \(X^2\) from those. Explain why this is wrong.
A: \(E\) and \(X^2\) must be built from the real counts. Percentages replace each row total by 100 and so change \(N\); since \(X^2\) grows in proportion to the sample size, the statistic would not be comparable with the critical value. Convert back to frequencies using the row totals.
Q: Write \(H_0\) and \(H_1\) for a test of whether the snack chosen (crisps, fruit or biscuits) is associated with age group (under 12, or 12 and over).
A: \(H_0\): there is no association between choice of snack and age group (they are independent). \(H_1\): there is an association between choice of snack and age group.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ Students are classified by weekly revision (under 5 hours, 5 to 10 hours, over 10 hours) and grade (C or below, B, A or above). The totals are rows 70, 80, 80 and columns 60, 80, 90, with 230 students. (a) Show that the expected number with under 5 hours and a grade of C or below is 18.3 to 3 s.f. (b) A test of independence is carried out at the 5% level. State \(\nu\) and the critical value.
A: (a) \(E = \dfrac{70 \times 60}{230}\) [M1] \(= 18.26 = 18.3\) (3 s.f.) [A1]
(b) \(\nu = (3 - 1)(3 - 1) = 4\) [B1] and the critical value is 9.488. [B1]
Q: [6 marks] ★ Two training programmes were compared. Of 100 people on programme A, 45 passed and 55 failed; of 100 on programme B, 30 passed and 70 failed. Test at the 1% level whether passing is associated with the programme.
A: \(H_0\): there is no association between programme and result. \(H_1\): there is an association. [B1]
Column totals 75 and 125, so \(E = 37.5, 62.5, 37.5, 62.5\). [M1]
\(X^2 = \dfrac{7.5^2}{37.5} + \dfrac{7.5^2}{62.5} + \dfrac{7.5^2}{37.5} + \dfrac{7.5^2}{62.5}\) [M1] \(= 1.5 + 0.9 + 1.5 + 0.9 = 4.8\) [A1]
\(\nu = 1\), and the 1% critical value is 6.635, so \(4.8 < 6.635\). [M1]
Do not reject \(H_0\): insufficient evidence, at the 1% level, of an association between programme and result. [A1]
Q: [7 marks] ★★ Customers at three cafés rate the service as poor, fair or good. Café 1: 3, 25, 52; Café 2: 9, 38, 63; Café 3: 8, 27, 65. Test at the 5% level whether the rating is associated with the café. Check whether any rows or columns need combining.
H: The grand total is 290; row totals 80, 110, 100; column totals 20, 90, 180.
H: The smallest expected frequency is in the "poor" column.
A: \(H_0\): there is no association between café and rating. \(H_1\): there is an association. [B1]
\(E = \dfrac{\text{row} \times \text{column}}{290}\): the smallest is \(\dfrac{80 \times 20}{290} = 5.52\), so all are at least 5 and nothing is combined. [M1 A1]
\[\begin{aligned}
X^2 &= 1.148 + 0.001 + 0.111 + 0.264 + 0.437 \\
&\quad + 0.408 + 0.177 + 0.525 + 0.138 = 3.21
\end{aligned}\] [M1 A1]
\(\nu = (3 - 1)(3 - 1) = 4\), critical value 9.488; \(3.21 < 9.488\). [M1]
Do not reject \(H_0\): insufficient evidence, at the 5% level, of an association between café and rating. [A1]
Q: [9 marks] ★★ Year 12 and Year 13 students choose where to revise: library, home or school. Some of the table has been lost.

| | Library | Home | School | Total |
|---|---|---|---|---|
| Year 12 | 18 | 22 | \(a\) | 60 |
| Year 13 | 32 | \(b\) | \(c\) | 90 |
| Total | 50 | 50 | 50 | 150 |

(a) Find \(a\), \(b\) and \(c\). (b) Test at the 5% level whether the choice of venue is associated with year group.
H: Every row and every column adds to its total.
A: (a) \(a = 60 - 18 - 22 = 20\) [M1], \(b = 50 - 22 = 28\), \(c = 50 - 20 = 30\) (check: \(32 + 28 + 30 = 90\)). [A1]
(b) \(H_0\): there is no association between year group and venue. \(H_1\): there is an association. [B1]
\(E = \dfrac{60 \times 50}{150} = 20\) for each Year 12 cell and \(\dfrac{90 \times 50}{150} = 30\) for each Year 13 cell. [M1 A1]
\(X^2 = \dfrac{4}{20} + \dfrac{4}{20} + 0 + \dfrac{4}{30} + \dfrac{4}{30} + 0\) [M1] \(= 0.667\) [A1]
\(\nu = (2 - 1)(3 - 1) = 2\), critical value 5.991; \(0.667 < 5.991\). [M1]
Do not reject \(H_0\): insufficient evidence, at the 5% level, of an association between year group and venue. [A1]
Q: [5 marks] ★★ 230 students are classified by weekly revision (under 5 hours, 5 to 10 hours, over 10 hours; row totals 70, 80, 80) and grade (C or below, B, A or above; column totals 60, 80, 90). The test statistic is \(X^2 = 25.4\), and the cell contributions are

| | C or below | B | A or above |
|---|---|---|---|
| Under 5 hours | 7.55 | 0.02 | 5.61 |
| 5 to 10 hours | 0.04 | 0.17 | 0.05 |
| Over 10 hours | 5.66 | 0.29 | 5.99 |

(a) Carry out the test at the 1% level. (b) Identify the two largest contributions in the table (they are two of the four corner cells) and describe what they show. The four corner cells have: under 5 hours, C or below: \(O = 30\), \(E = 18.3\); over 10 hours, C or below: \(O = 10\), \(E = 20.9\); under 5 hours, A or above: \(O = 15\), \(E = 27.4\); over 10 hours, A or above: \(O = 45\), \(E = 31.3\).
A: (a) \(\nu = 4\), 1% critical value 13.277. [B1] \(25.4 > 13.277\) [M1], so reject \(H_0\): sufficient evidence, at the 1% level, of an association between revision hours and grade. [A1]
(b) Under 5 hours with C or below (7.55): 30 against 18.3 expected, so students who revise little are more often at the lower grade than independence predicts. [B1]
Over 10 hours with A or above (5.99): 45 against 31.3 expected, so students who revise a lot more often reach A or above. [B1]
Q: [10 marks] ★★★ A company records years of service and job satisfaction for 254 employees.

| | Low | Medium | High | Total |
|---|---|---|---|---|
| Under 1 year | 3 | 4 | 7 | 14 |
| 1 to 4 years | 30 | 42 | 28 | 100 |
| 5 to 9 years | 26 | 26 | 38 | 90 |
| 10 years or more | 14 | 22 | 14 | 50 |
| Total | 73 | 94 | 87 | 254 |

(a) Show that two expected frequencies in the first row are below 5 and explain what to do. (b) Test at the 5% level whether job satisfaction is associated with years of service.
H: The expected frequency of a cell is its row total times its column total over 254.
H: Combine the first row with its neighbour, then redo all the expected frequencies for the 3 rows.
H: For the new table \(\nu = (3 - 1)(3 - 1)\).
A: (a) \(E = \dfrac{14 \times 73}{254} = 4.02\) and \(\dfrac{14 \times 87}{254} = 4.80\) are below 5. [B1]
The chi-squared approximation is unreliable, so combine the first row with the adjacent row, "1 to 4 years". [B1]
(b) \(H_0\): there is no association between years of service and job satisfaction. \(H_1\): there is an association. [B1]
The combined row "under 5 years" has \(O = 33, 46, 35\) (total 114). [M1]
The expected frequencies are \(32.76, 42.19, 39.05\); \(25.87, 33.31, 30.83\); \(14.37, 18.50, 17.13\), all at least 5. [M1 A1]
\[\begin{aligned}
X^2 &= 0.002 + 0.344 + 0.420 + 0.001 + 1.603 \\
&\quad + 1.669 + 0.010 + 0.661 + 0.571 = 5.28
\end{aligned}\] [M1 A1]
\(\nu = 4\), critical value 9.488, and \(5.28 < 9.488\). [M1]
Do not reject \(H_0\): insufficient evidence, at the 5% level, of an association between years of service and job satisfaction. [A1]
Q: [10 marks] (#math.s1.prob) ★★★ Two hundred people are asked whether they own a car and whether they own a bike. Of the 80 who own a car, 56 own a bike; of the 120 who do not own a car, 64 own a bike. (a) Assuming that owning a car and owning a bike are independent, find the probability that a randomly chosen person owns both, and the expected number of people who own both. (b) Test at the 5% level whether the ownerships are independent. (c) Find \(P(\text{bike} \mid \text{car})\) and \(P(\text{bike} \mid \text{no car})\) from the data and comment.
H: Use \(P(A \cap B) = P(A)P(B)\) for independent events.
H: The expected number is \(200\) times that probability; it is the same as \(\dfrac{80 \times 120}{200}\).
H: Independence means the two conditional probabilities are equal.
A: (a) \(P(\text{car}) = \dfrac{80}{200} = 0.4\) and \(P(\text{bike}) = \dfrac{120}{200} = 0.6\). [B1]
\(P(\text{both}) = 0.4 \times 0.6 = 0.24\) [M1], so the expected number is \(200 \times 0.24 = 48\). [A1]
(b) \(H_0\): there is no association between owning a car and owning a bike. \(H_1\): there is an association. [B1]
\(E = 48, 32, 72, 48\), so \(X^2 = \dfrac{64}{48} + \dfrac{64}{32} + \dfrac{64}{72} + \dfrac{64}{48}\) [M1] \(= 1.333 + 2.000 + 0.889 + 1.333 = 5.56\) [A1]
\(\nu = 1\), critical value 3.841, and \(5.56 > 3.841\): reject \(H_0\); there is sufficient evidence, at the 5% level, of an association between owning a car and owning a bike. [M1 A1]
(c) \(P(\text{bike} \mid \text{car}) = \dfrac{56}{80} = 0.7\) and \(P(\text{bike} \mid \text{no car}) = \dfrac{64}{120} = 0.533\). [B1]
Car owners are more likely to own a bike (0.7 against 0.533); these would be equal if the two were independent. [B1]
Q: [4 marks] ★ A test of independence on a table with 3 rows (age group) and 5 columns (favourite sport) gives \(X^2 = 21.5\). Carry out the test at the 1% level.
A: \(\nu = (3 - 1)(5 - 1) = 8\) [B1] and the 1% critical value is 20.090. [B1]
\(21.5 > 20.090\) [M1], so reject \(H_0\): sufficient evidence, at the 1% level, of an association between age group and favourite sport. [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ A \(2 \times 2\) table has observed frequencies \(a, b\) in row 1 and \(c, d\) in row 2, with row totals \(R_1, R_2\), column totals \(C_1, C_2\) and grand total \(N\). (a) Show that \(X^2 = \dfrac{N(ad - bc)^2}{R_1R_2C_1C_2}\). (b) Use the result to find \(X^2\) for the table with rows 45, 55 and 30, 70.
H: Show that \(a - E_{11} = \dfrac{ad - bc}{N}\), and that the other three differences are the same size.
H: \(\dfrac{1}{R_1} + \dfrac{1}{R_2} = \dfrac{N}{R_1R_2}\), and the same for the columns.
A: (a) \(E_{11} = \dfrac{R_1C_1}{N}\), so
\[\begin{aligned}
a - E_{11} &= \frac{aN - (a + b)(a + c)}{N} \\
&= \frac{a(a + b + c + d) - (a^2 + ac + ab + bc)}{N} = \frac{ad - bc}{N}
\end{aligned}\] [M1 A1]
The other differences are \(\pm\dfrac{ad - bc}{N}\), because the observed and expected tables have the same totals. [B1]
So \(X^2 = \dfrac{(ad - bc)^2}{N^2}\sum \dfrac{1}{E} = \dfrac{(ad - bc)^2}{N^2} \cdot N\left(\dfrac{1}{R_1} + \dfrac{1}{R_2}\right)\left(\dfrac{1}{C_1} + \dfrac{1}{C_2}\right)\) [M1] because \(E_{ij} = \dfrac{R_iC_j}{N}\).
\(= \dfrac{(ad - bc)^2}{N} \cdot \dfrac{N}{R_1R_2} \cdot \dfrac{N}{C_1C_2} = \dfrac{N(ad - bc)^2}{R_1R_2C_1C_2}\) [A1]
(b) \(ad - bc = 45 \times 70 - 55 \times 30 = 1500\), \(N = 200\), \(R_1R_2 = 100 \times 100\), \(C_1C_2 = 75 \times 125\). [M1]
\(X^2 = \dfrac{200 \times 1500^2}{10000 \times 9375} = 4.8\) [A1]
Q: [7 marks] ★★★ In a trial, 40 patients receive treatment A and \(a\) of them recover; of 60 patients on treatment B, 30 recover. (a) Show that \(X^2 = \dfrac{150(a - 20)^2}{(a + 30)(70 - a)}\). (b) Find the values of \(a\) (a whole number from 0 to 40) for which a test at the 5% level concludes that recovery is associated with the treatment. (c) Explain what happens at \(a = 20\).
H: Use the formula from the previous question with \(N = 100\) and \(R_1 = 40\), \(R_2 = 60\).
H: The inequality \(150(a - 20)^2 > 3.841(a + 30)(70 - a)\) is a quadratic in \(a\).
A: (a) Recovered: \(a\) and 30; not recovered: \(40 - a\) and 30. \(ad - bc = 30a - 30(40 - a) = 60(a - 20)\); \(C_1 = a + 30\), \(C_2 = 70 - a\). [M1]
\(X^2 = \dfrac{100 \times 3600(a - 20)^2}{40 \times 60 \times (a + 30)(70 - a)} = \dfrac{150(a - 20)^2}{(a + 30)(70 - a)}\) [A1]
(b) \(\nu = 1\), so reject when \(X^2 > 3.841\): \(150(a - 20)^2 > 3.841(a + 30)(70 - a)\) [M1]
\(153.841a^2 - 6153.6a + 51934 > 0\) [M1], whose roots are \(a = 12.10\) and \(a = 27.90\). [A1]
So the test rejects \(H_0\) for \(a \leq 12\) or \(a \geq 28\). [A1]
(c) At \(a = 20\), \(X^2 = 0\): both treatments have a recovery proportion of \(\tfrac{30}{60} = \tfrac12\) and the variables are exactly independent. The expression is symmetrical about \(a = 20\). [B1]
:::

:::quiz
? How many degrees of freedom does a test of independence have for a table with 4 rows and 5 columns, and no combining?
- \(20\)
- \(9\)
+ \(12\)
- \(19\)
> \(\nu = (4 - 1)(5 - 1) = 12\). Using 20 counts the cells, 19 subtracts only the total, and 9 adds the rows and columns.
? A table has a row total of 60, a column total of 45 and a grand total of 300. What is the expected frequency of the cell where they meet?
- \(105\)
- \(0.09\)
+ \(9\)
- \(2700\)
> \(E = \dfrac{60 \times 45}{300} = 9\). The product alone, 2700, forgets to divide by the grand total, and 0.09 is a probability, not a frequency.
? Which is the correct null hypothesis for a test of whether favourite subject and gender are linked?
- Favourite subject depends on gender
- Gender causes the choice of favourite subject
+ There is no association between favourite subject and gender
- Favourite subject and gender are not independent
> \(H_0\) says there is no association (independence). The other options are alternatives, and a test can never show that one variable causes the other.
? Some expected frequencies in a \(4 \times 3\) table are below 5, so two rows are combined, leaving a \(3 \times 3\) table. What is \(\nu\)?
- \(6\)
+ \(4\)
- \(9\)
- \(3\)
> \(\nu\) uses the new size: \((3 - 1)(3 - 1) = 4\). The value 6 is the original table's \((4 - 1)(3 - 1)\), the error shown in the Spot the error.
? A test at the 5% level gives \(X^2 = 8.2\) with \(\nu = 4\). What is the conclusion?
- Reject \(H_0\): there is an association
+ Do not reject \(H_0\): insufficient evidence of an association
- Do not reject \(H_0\): there is no association
- Reject \(H_0\), because \(8.2 > 5.991\)
> The critical value for \(\nu = 4\) is 9.488, and \(8.2 < 9.488\), so \(H_0\) is not rejected. It does not prove there is no association, only that the evidence is insufficient. The value 5.991 belongs to \(\nu = 2\).
? Which of these does a contingency table test need as its data?
- Percentages in each row
- Proportions of each column
+ Observed frequencies (counts)
- Row means
> The statistic is built from counts, because \(X^2\) depends on the total number of observations. Percentages and proportions discard \(N\).
:::

:::checklist What you can now do
- [ ] I can set up a contingency table with its row, column and grand totals and state \(H_0\) and \(H_1\) in context (no association between two named variables).
- [ ] I can find each expected frequency as row total times column total over grand total, and explain why that follows from independence.
- [ ] I can combine adjacent rows or columns so every expected frequency is at least 5, and recalculate the expected frequencies for the new table.
- [ ] I can calculate \(X^2 = \sum \dfrac{(O - E)^2}{E}\) for a table, including a \(2 \times 2\) table without Yates' correction.
- [ ] I can find \(\nu = (r - 1)(c - 1)\) from the table I am actually using, after any combining.
- [ ] I can read the critical value from the \(\chi^2\) table and write a conclusion in context with "evidence" language.
- [ ] I can say which cells contribute most to \(X^2\) and describe, in context, whether the observed frequency is above or below the expected one.
- [ ] I can recover missing cells of a table from its totals, and link independence to \(P(A \cap B) = P(A)P(B)\).
:::

:::recap
- \(H_0\): no association between the two variables (name both in context); \(H_1\): there is an association. A significant result shows a link, not a cause.
- \(E = \dfrac{\text{row total} \times \text{column total}}{\text{grand total}}\), because independence gives \(P(\text{cell}) = P(\text{row}) \times P(\text{column})\).
- \(X^2 = \sum \dfrac{(O - E)^2}{E}\) over all cells; \(\nu = (r - 1)(c - 1)\); upper-tail critical value from the \(\chi^2\) table (\(p = 0.95\) for 5%).
- Every \(E\) must be at least 5: combine adjacent rows or columns first, recalculate \(E\), and take \(\nu\) from the new table size.
- Use counts, never percentages. No Yates' correction in 9231, also for \(2 \times 2\).
- Large terms \(\dfrac{(O - E)^2}{E}\) show where the association is: compare \(O\) and \(E\) for that cell in context.
- Conclusion: "sufficient evidence, at the 5% level, of an association between ..." or "insufficient evidence of an association between ...", never "no evidence" or "proves".
:::

:::links
- read: [The chi-square distribution](https://openstax.org/books/introductory-statistics-2e/pages/11-introduction) · OpenStax · tests of independence with worked tables
- practise: [Chi-square tests](https://www.khanacademy.org/math/statistics-probability/inference-categorical-data-chi-square-tests) · Khan Academy · independence and contingency-table practice with feedback
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · free graded questions with answers
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Non-parametric tests: the sign test](#math.fm.nonpar) drops the assumption that the data come from a normal distribution.
