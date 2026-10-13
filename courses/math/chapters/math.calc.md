@chapter math.calc
@title Your calculator: exam skills
@level guide
@paper CAIE 9709 · all papers
@time 2 hours
@summary How to set up and use a scientific calculator in the 9709 papers: angle mode, keeping full accuracy, table mode for iteration and the trapezium rule, statistics mode, and the distribution functions as checks. Includes what you must still write down to earn the marks.

:::why
A scientific calculator is allowed in every 9709 paper, and a student who knows it well saves minutes and avoids slips. A student who knows it badly loses marks to the wrong mode, to rounding too early, and to answers with no working. This chapter is about using the machine as a fast, reliable checker, never as a replacement for the method.
:::

## What is allowed, and what earns marks

You need a **scientific calculator** for every paper, and a ruler. Graphical calculators, computers, and calculators that do algebra, differentiation or integration symbolically are not permitted. If your calculator can integrate or solve equations symbolically, check the model rules before you buy it. The calculators in this chapter, the Casio fx-991EX, the Casio fx-991CW and the TI-30X Pro MathPrint, are the ones this guide covers, but the ideas apply to any approved scientific model.

:::exam No marks for unsupported answers
Cambridge gives **no marks for an answer that comes straight from a calculator with no working shown**. Write the equation, the substitution or the formula you used, then the result. For "show that" and "exact" questions the algebra is the answer: a calculator decimal can never prove an exact result. If a question needs a numerical method, state the numbers you used (the table of values, the iterations).
:::

## Set up before every paper

Do these in the first minute of every paper, and again after any reset.

1. **Angle mode.** Check the screen for **D** (degrees) or **R** (radians). Pure papers use both: trigonometric equations in degrees are common, and calculus and radian questions need radians. Set the mode in the SETUP menu (Casio: the shift key then the menu key) or the mode key (TI). Before each trig calculation, look at the mode again.
2. **Number display.** Use the normal "Math" display for exact fractions and surds, and press the S⇔D key (Casio) to see the decimal when you need it.
3. **Clear memories.** Clear stored variables and statistics lists, so old data does not leak into your answer.

The cost of the wrong mode is large. Here is the same input in two modes:

\[\sin 30 = 0.5 \text{ (degree mode)}, \qquad \sin 30 = -0.988 \text{ (radian mode)}\]

:::warn The silent mode error
The calculator never warns you that the mode is wrong. A radian-mode answer to a degree question looks like a perfectly valid number, so you lose every mark that depends on it. Before each trigonometric calculation, glance at the D or R on the screen. A quick test: \(\sin 30\) should give 0.5 in degree mode.
:::

## Full accuracy: ANS and memories

**Never type a rounded intermediate value back in.** The accuracy rule in this course is: work with the full calculator value, and round only the final answer. Two tools do this.

- **Ans** holds the last result. Press the Ans key (or start a new line with an operator, which the calculator fills as Ans) to continue from the exact value.
- **Memories** A, B, C … store a value. Store a result in the calculator's STO key and recall it by its letter.

\(\textbf{Example.}\) Solve \(3x^2 - 5x - 4 = 0\) to 3 significant figures with the formula. Store the square root first:

\[\begin{aligned} x &= \dfrac{5 \pm \sqrt{(-5)^2 - 4(3)(-4)}}{2 \times 3} = \dfrac{5 \pm \sqrt{73}}{6} \\ \sqrt{73} &= 8.5440\ldots \\ x &= 2.26 \text{ or } x = -0.591 \end{aligned}\]

Notice that you write the formula with its numbers in, write the exact surd, and give the decimals last. That earns the M1 for a correct method, and the A1 for each answer.

:::tip Brackets with negatives
Always bracket a negative number before squaring: type \((-5)^2\) to get 25. Typing \(-5^2\) gives \(-25\). The same applies to \(b^2 - 4ac\) when \(b\) is negative, to powers of negative numbers, and to the negative sign in the denominator of a fraction. In "Math" display, use the fraction template for numerators and denominators, so that \(\dfrac{5 + 8.544}{6}\) is not typed as \(5 + 8.544 \div 6\).
:::

## Table mode: iteration, sign changes and the trapezium rule

Table mode lists the values of a function \(f(x)\) at chosen inputs. It turns three slow tasks into one-minute checks.

**Sign change.** To locate a root of \(f(x) = x^3 - 2x - 5\), enter the function and a table from \(x = 2\) in steps of 0.1:

| \(x\) | 2 | 2.1 | 2.2 |
|---|---|---|---|
| \(f(x)\) | \(-1\) | \(0.061\) | \(1.248\) |

\(f(2) < 0\) and \(f(2.1) > 0\), and \(f\) is continuous, so a root lies between 2 and 2.1. You write that sentence with the two values: the table alone is not the answer.

**Iteration.** To run \(x_{n+1} = \sqrt[3]{2x_n + 5}\) from \(x_1 = 2\), type 2 and press equals, then type the formula using **Ans** for \(x_n\) and press equals again and again. Each press gives the next term, with full accuracy. The terms \(x_2\) to \(x_6\) are 2.0801, 2.0924, 2.0942, 2.0945, 2.0945, so the root is 2.09 to 3 s.f. Write the successive values in your answer, to at least the accuracy the question wants plus one figure.

**Trapezium rule.** To estimate \(\displaystyle\int_0^1 \frac{1}{1 + x^2}\,dx\) with 4 strips, tabulate \(f\) at \(x = 0, 0.25, 0.5, 0.75, 1\) (strip width \(h = 0.25\)):

| \(x\) | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|
| \(y\) | 1 | 0.9412 | 0.8 | 0.64 | 0.5 |

\[\begin{aligned} T &= \tfrac12 (0.25)\big[\,1 + 0.5 + 2(0.9412 + 0.8 + 0.64)\,\big] \\ &= 0.125 \times 6.2624 = 0.783 \end{aligned}\]

The table did the arithmetic, but you still write the \(y\)-values and the bracket. The trapezium rule is not in MF19, so you must remember the formula.

:::tip Casio and TI table mode
**Casio fx-991EX and fx-991CW:** open Table from the main menu, type \(f(x)\), choose the start, end and step, and read the values (the CW lets you add a second function, \(g(x)\)). **TI-30X Pro MathPrint:** use the table key, enter \(f(x)\), and set the start and step in the table setup. Menus differ slightly between models, so run through the steps once with a function you know, such as \(x^2\), well before the exam.
:::

## Statistics mode

Use statistics mode for \(\bar x\), \(\sigma\), \(\Sigma x\) and \(\Sigma x^2\) from a list of data, and for the regression line.

For the data 4, 7, 7, 9, 13, enter the list and ask for one-variable statistics. You read:

| \(n\) | \(\Sigma x\) | \(\Sigma x^2\) | \(\bar x\) | \(\sigma_x\) | \(s_x\) |
|---|---|---|---|---|---|
| 5 | 40 | 364 | 8 | 2.97 | 3.32 |

Two symbols look alike and mean different things. \(\sigma_x\) divides by \(n\) (the standard deviation of a population or of the data itself) and \(s_x\) divides by \(n - 1\) (the unbiased estimate, used in sampling and estimation). Which one you need depends on the question: in Paper 5, "the standard deviation of the data" is \(\sigma_x\); in Paper 6, "an unbiased estimate of the variance" uses \(s_x^2\).

\[\sigma = \sqrt{\dfrac{364}{5} - 8^2} = \sqrt{8.8} = 2.97, \qquad s^2 = \dfrac{364 - 5(8)^2}{4} = 11\]

For two-variable data \((1, 2), (2, 3), (3, 5), (4, 6)\), the regression line option gives \(y = 0.5 + 1.4x\) (that is \(a = 0.5\), \(b = 1.4\)), the same as \(b = S_{xy}/S_{xx} = 7/5\) by hand.

:::warn Show the sums
A question that gives \(\Sigma x\) and \(\Sigma x^2\) wants the formula and the substitution, for example \(\sqrt{364/5 - 8^2}\). A bare "2.97" from the calculator's \(\sigma_x\) key scores less if the examiner cannot see how you got it. Use the calculator to check your working, not to replace it.
:::

## Distribution functions as checks

Casio's Distribution menu and the TI's DISTR menu give probabilities for the Normal, Binomial and Poisson distributions. They are fast checks, but the exam still expects the method written down.

| Question | Calculator check | Answer |
|---|---|---|
| \(X \sim B(12, 0.3)\), find \(P(X \le 4)\) | binomial cumulative with \(n = 12\), \(p = 0.3\), \(x = 4\) | 0.724 |
| \(X \sim N(50, 36)\), find \(P(X > 56)\) | normal cumulative from 56 to a large number, \(\mu = 50\), \(\sigma = 6\) | 0.159 |
| \(X \sim N(50, 36)\), find \(a\) with \(P(X < a) = 0.9\) | inverse normal, area 0.9, \(\sigma = 6\), \(\mu = 50\) | 57.7 |
| \(X \sim \mathrm{Po}(3.2)\), find \(P(X \ge 2)\) | \(1 -\) Poisson cumulative at \(x = 1\) | 0.829 |

Notice three details.

- **\(\sigma\), not the variance.** The calculator asks for the standard deviation. The notation \(N(50, 36)\) gives the variance 36, so enter \(\sigma = 6\).
- **"At least" needs a subtraction.** Cumulative functions give \(P(X \le x)\). For \(P(X \ge 2)\) use \(1 - P(X \le 1)\).
- **Standardise anyway.** In Paper 5 the syllabus asks you to *show full standardisation*: write \(z = \dfrac{56 - 50}{6} = 1\), then \(P(Z > 1)\). The calculator confirms 0.1587, but the line with \(z\) earns the method mark.

:::exam The method mark survives, the calculator mark does not
If you write \(z = (56 - 50)/6 = 1\) and then a wrong decimal, you keep the M1. If you write only "0.159 from calculator" and it is right, an examiner may still withhold marks for missing method. Write the standardisation, the table lookup or the probability formula, then the number.
:::

## The equation solver: a check, not the answer

The equation solver finds roots of equations such as \(x^3 - 2x - 5 = 0\) (\(x = 2.09\), to 3 s.f.). Use it to **check** an answer you derived, for example the root of a quadratic or the result of an iteration. It does not earn marks for the working: a question that says "show that" or "use the iterative formula" asks for the method itself. Never use the solver for a "solve algebraically" question without showing the algebra.

:::tip Practise the exact keys
Rehearse each procedure on a topic you already know: the table for a sign change, the Ans loop for an iteration, one-variable statistics for a small list, and one cumulative probability of each type. Do it on the same calculator you will use in the exam, with the same mode settings, so the menus are automatic.
:::

:::recap
- A scientific calculator is allowed in every 9709 paper; graphical and symbolic ones are not.
- No marks are given for an unsupported calculator answer: always write the working, and the algebra for "show that" and "exact".
- Check the D or R on the screen before every trigonometric calculation.
- Keep full accuracy with Ans and memories; round only the final answer to 3 s.f. (angles to 1 d.p.).
- Bracket negatives: \((-5)^2 = 25\), but \(-5^2 = -25\).
- Table mode gives sign changes, iteration (with Ans) and the trapezium-rule values; write the values down.
- \(\sigma_x\) divides by \(n\); \(s_x\) divides by \(n - 1\). Choose the one the question needs.
- Distribution keys ask for \(\sigma\), not the variance, and cumulative keys give \(P(X \le x)\). Show the standardisation or the probability sum.
:::

Next: [Writing maths for marks](#math.exam.skills)
