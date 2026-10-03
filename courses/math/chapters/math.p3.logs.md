@chapter math.p3.logs
@title Logarithms and exponentials
@level as
@paper CAIE P2/P3 · Edexcel IAL P2–P3 · AQA/OCR/Edexcel Pure Year 1–2
@time 7–9 hours
@summary Logarithms as the inverse of indices, the laws of logarithms, the functions \(e^x\) and \(\ln x\) and their graphs, solving equations and inequalities where the unknown is an index, and turning \(y = kx^n\) and \(y = ka^x\) into straight-line graphs.

:::why
Many real quantities change by a constant factor in equal steps: money at compound interest, a growing population, a cooling drink, the decay of a radioactive sample. Their formulas have the unknown in the index, and ordinary algebra cannot solve \(3^x = 20\). Logarithms are the tool that can. They also let you turn a curved graph into a straight line, which is how scientists find the law behind a set of measurements.
:::

**Before you start**, you need the index laws from [Indices, surds and standard form](#math.f.powers), the idea of an inverse function and the reflection in \(y = x\) from [Functions](#math.p1.functions), and quadratics from [Quadratics](#math.p1.quadratics).

## Logarithms

The equation \(2^3 = 8\) says "2 to the power 3 is 8". A logarithm asks the question the other way round: "to what power must I raise 2 to get 8?" The answer is \(3\), and we write \(\log_2 8 = 3\).

:::def Logarithm
For \(a > 0\), \(a \ne 1\) and \(b > 0\), the logarithm of \(b\) to base \(a\), written \(\log_a b\), is the power to which \(a\) must be raised to give \(b\):
\[\log_a b = c \iff a^c = b\]
You cannot take the logarithm of zero or of a negative number, because no power of a positive base gives them.
:::

So \(\log_{10} 1000 = 3\), \(\log_2 \tfrac18 = -3\), \(\log_9 3 = \tfrac12\) (since \(9^{1/2} = 3\)). Two results hold for every base: \(\log_a 1 = 0\) (because \(a^0 = 1\)) and \(\log_a a = 1\).

:::eg Find (a) \(\log_5 125\), (b) \(\log_{10} 0.01\), (c) \(\log_{4} 2\), (d) the value of \(x\) if \(\log_x 64 = 3\).
(a) \(5^3 = 125\), so the answer is \(3\).

(b) \(0.01 = 10^{-2}\), so the answer is \(-2\).

(c) \(4^{1/2} = 2\), so the answer is \(\tfrac12\).

(d) \(x^3 = 64\), so \(x = 4\).
:::

### Laws of logarithms

The laws of logarithms are the index laws read backwards. If \(a^p = x\) and \(a^q = y\), then \(xy = a^{p+q}\), which says \(\log_a xy = p + q = \log_a x + \log_a y\).

:::key Laws of logarithms (any valid base)
\[\log_a x + \log_a y = \log_a (xy) \qquad \log_a x - \log_a y = \log_a \left(\frac{x}{y}\right)\]
\[\log_a (x^k) = k\log_a x \qquad \log_a \left(\frac1x\right) = -\log_a x\]
\[\log_a a = 1 \qquad \log_a 1 = 0 \qquad a^{\log_a x} = x \qquad \log_a (a^x) = x\]
The laws work only when the **bases are the same**. They are not on MF19. There is no law for \(\log_a(x + y)\).
:::

:::warn What the laws do not say
\(\log(x + y)\) is not \(\log x + \log y\). \(\dfrac{\log x}{\log y}\) is not \(\log x - \log y\), and \((\log x)^2\) is not \(2\log x\). Test with numbers: \(\log_{10}(10 + 90) = \log_{10}100 = 2\), but \(\log_{10}10 + \log_{10}90 = 1 + 1.954 = 2.954\). The product law would need \(\log_{10}(10 \times 90) = \log_{10} 900\).
:::

:::eg Write as a single logarithm: (a) \(2\log 3 + \log 5 - \log 15\), (b) \(\log_2 40 - \log_2 5\). Express \(\log \dfrac{a^2 b}{\sqrt{c}}\) in terms of \(p = \log a\), \(q = \log b\) and \(r = \log c\).
(a) \(2\log 3 = \log 9\), so \(\log 9 + \log 5 - \log 15 = \log\dfrac{9 \times 5}{15} = \log 3\).

(b) \(\log_2\dfrac{40}{5} = \log_2 8 = 3\).

For the third, split using the laws: \(\log a^2 + \log b - \log c^{1/2} = 2p + q - \tfrac12 r\).
:::

Equations with logs: combine into a single log on each side, then remove the logs; or write the equation as an index equation. **Always check** that every log argument is positive for your answer.

:::eg Solve (a) \(\log_3 x + \log_3 (x + 2) = 1\), (b) \(2\log x = \log(x + 6)\)
(a) Combine: \(\log_3 x(x + 2) = 1\), so \(x(x + 2) = 3^1 = 3\). Then \(x^2 + 2x - 3 = 0\), giving \((x + 3)(x - 1) = 0\), so \(x = 1\) or \(x = -3\). The log of \(-3\) does not exist, so reject it: \(x = 1\).

(b) \(2\log x = \log x^2\), so \(\log x^2 = \log (x + 6)\), and \(x^2 = x + 6\). Then \(x^2 - x - 6 = 0\), so \(x = 3\) or \(x = -2\). Only \(x = 3\) has \(\log x\) defined. Check: \(2\log 3 = \log 9 = \log(3 + 6)\). ✓
:::

:::tip Which base?
Calculators have \(\log\) (base 10) and \(\ln\) (base \(e\)). The Cambridge syllabus does not ask for the change of base formula, so you will not need to compute \(\log_5 7\) directly. To solve \(a^x = b\), take \(\log\) or \(\ln\) of **both sides**, as in the next sections.
:::

## The exponential function and natural logarithm

Many processes grow at a rate proportional to their size. The special number that makes the rate of change of \(e^x\) equal to \(e^x\) itself is \(e = 2.71828\ldots\), an irrational number like \(\pi\). We will use this in [Differentiation](#math.p3.diff).

:::def Natural logarithm
The natural logarithm \(\ln x\) is the logarithm to base \(e\): \(\ln x = \log_e x\). The functions \(e^x\) and \(\ln x\) are inverses of each other: \(\ln(e^x) = x\) for all \(x\), and \(e^{\ln x} = x\) for \(x > 0\).
:::

Because they are inverse functions, their graphs are reflections of each other in the line \(y = x\) (see [Functions](#math.p1.functions)).

:::plot The graph of \(y = e^x\) passes through (0, 1) and has the x-axis as an asymptote. The graph of \(y = \ln x\) passes through (1, 0) and has the y-axis as an asymptote. They are reflections in the line y = x.
--f "exp(x)" --f "log(x)" --f "x" --label "y = eˣ" --label "y = ln x" --label "y = x" --x -3 4 --y -3 6 --pt "0,1,(0, 1)@nw" --pt "1,0,(1, 0)@se" --legend tl
:::

:::key Properties of \(e^x\) and \(\ln x\)
- \(y = e^x\): domain all real \(x\), range \(y > 0\), passes through \((0, 1)\), increasing, asymptote \(y = 0\).
- \(y = \ln x\): domain \(x > 0\), range all real \(y\), passes through \((1, 0)\), increasing, asymptote \(x = 0\).
- \(y = e^{kx}\) with \(k > 0\) is exponential **growth**; with \(k < 0\) it is exponential **decay**. Both pass through \((0, 1)\) and have asymptote \(y = 0\).
- The laws of logs apply to \(\ln\): \(\ln a + \ln b = \ln ab\), \(\ln a^k = k\ln a\), \(\ln e = 1\).
:::

:::plot Exponential growth \(y = e^{2x}\) and decay \(y = e^{-x}\). Both pass through (0, 1). Growth rises steeply for \(x > 0\); decay falls towards the x-axis.
--f "exp(2*x)" --f "exp(-x)" --label "y = e²ˣ" --label "y = e⁻ˣ" --x -2 2 --y -1 8 --pt "0,1,(0, 1)@ne" --legend tr
:::

## Equations with the unknown in the index

To solve \(a^x = b\), take logarithms of both sides, then use \(\log a^x = x\log a\) to bring the index down. Any base works, but use \(\ln\) or \(\log\) on the calculator.

:::steps
1. Isolate the power: get the form \(a^{f(x)} = b\).
2. Take \(\ln\) (or \(\log\)) of both sides.
3. Use \(\ln a^{f(x)} = f(x)\ln a\) and solve the resulting linear equation.
:::

:::eg Solve (a) \(3^x = 20\), (b) \(2^{x+1} = 5^x\), (c) \(e^{2x} = 7\), (d) \(\ln(2x - 1) = 3\)
(a) \(x\ln 3 = \ln 20\), so \(x = \dfrac{\ln 20}{\ln 3} = 2.73\) (3 s.f.).

(b) \((x + 1)\ln 2 = x\ln 5\), so \(x\ln 2 + \ln 2 = x\ln 5\), giving \(\ln 2 = x(\ln 5 - \ln 2)\). Then \(x = \dfrac{\ln 2}{\ln 5 - \ln 2} = \dfrac{\ln 2}{\ln 2.5} = 0.756\) (3 s.f.).

(c) \(2x = \ln 7\), so \(x = \tfrac12 \ln 7 = 0.973\).

(d) Use \(e\) as the base on both sides: \(2x - 1 = e^3\), so \(x = \dfrac{e^3 + 1}{2} = 10.5\) (3 s.f.).
Check (a): \(3^{2.727} = 20.0\). ✓
:::

Some equations are quadratics in disguise. Substitute \(u = e^x\) (or \(u = 3^x\)), solve for \(u\), then go back. Since \(e^x > 0\), reject any negative \(u\).

:::eg Solve (a) \(e^{2x} - 5e^x + 6 = 0\), (b) \(3^{2x} - 4 \times 3^x - 45 = 0\)
(a) Let \(u = e^x\). Then \(u^2 - 5u + 6 = 0\), so \((u - 2)(u - 3) = 0\) and \(e^x = 2\) or \(e^x = 3\). Therefore \(x = \ln 2\) or \(x = \ln 3\) (0.693 or 1.10).

(b) Let \(u = 3^x\), so \(u^2 - 4u - 45 = 0\), which factorises as \((u - 9)(u + 5) = 0\). Then \(3^x = 9\) gives \(x = 2\), and \(3^x = -5\) has no solution. So \(x = 2\).
:::

### Inequalities

Take logs of both sides in the same way. If you divide by a **negative** number, reverse the inequality. Remember that \(\ln a < 0\) when \(0 < a < 1\).

:::eg Solve (a) \(2^x > 50\), (b) \(0.5^x < 0.1\). Find the smallest integer \(n\) for which \(1.05^n > 2\).
(a) \(x\ln 2 > \ln 50\), and \(\ln 2 > 0\), so \(x > \dfrac{\ln 50}{\ln 2} = 5.64\).

(b) \(x\ln 0.5 < \ln 0.1\). Now \(\ln 0.5 < 0\), so dividing reverses the inequality: \(x > \dfrac{\ln 0.1}{\ln 0.5} = 3.32\).

For the last: \(n\ln 1.05 > \ln 2\), so \(n > \dfrac{\ln 2}{\ln 1.05} = 14.2\). The smallest integer is \(n = 15\). Check: \(1.05^{14} = 1.980 < 2\) and \(1.05^{15} = 2.079 > 2\). ✓
:::

:::eg (Exam style) The population \(P\) of a colony is modelled by \(P = 200e^{0.03t}\), where \(t\) is the time in years from the start. (a) Find the population when \(t = 10\). (b) Find when the population first reaches \(500\). (c) A sample of a radioactive substance has mass \(N = N_0 e^{-0.1t}\). Find its half-life, the time for the mass to halve.
**(a)** \(P = 200e^{0.3} = 270\) (3 s.f.). [B1]

**(b)** \(200e^{0.03t} = 500\), so \(e^{0.03t} = 2.5\). [M1] Take natural logs: \(0.03t = \ln 2.5\). [M1]
\[t = \frac{\ln 2.5}{0.03} = 30.5 \text{ years}\] [A1]

**(c)** Halving means \(N = \tfrac12 N_0\): \(e^{-0.1t} = \tfrac12\). [M1] Then \(-0.1t = \ln\tfrac12 = -\ln 2\), so
\[t = \frac{\ln 2}{0.1} = 6.93 \text{ time units}\] [A1]
:::

:::eg (Exam style) Solve (a) \(\log_2(x + 5) - \log_2 x = 3\), (b) \(3e^{2x} - 11e^x + 6 = 0\), giving the answers to (b) in exact form.
**(a)** \(\log_2\dfrac{x + 5}{x} = 3\), so \(\dfrac{x + 5}{x} = 2^3 = 8\). [M1 A1]
\[x + 5 = 8x \implies x = \tfrac57\] [A1]
Both \(x\) and \(x + 5\) are positive, so the answer is valid. [B1]

**(b)** Let \(u = e^x\): \(3u^2 - 11u + 6 = 0\), so \((3u - 2)(u - 3) = 0\). [M1 A1]
\[e^x = \tfrac23 \text{ or } e^x = 3 \implies x = \ln\tfrac23 \text{ or } x = \ln 3\] [M1 A1]
Both \(u\) values are positive, so both are valid.
:::

## Straight-line graphs from curved relationships

Experimental data often follows a law of the form \(y = kx^n\) (a power law) or \(y = ka^x\) (exponential). Taking logarithms turns each into a straight line \(Y = mX + c\), from whose gradient and intercept you read the constants.

:::key Reducing to linear form
- \(y = kx^n\): take \(\ln\) of both sides, \(\ln y = n\ln x + \ln k\). Plot \(\ln y\) against \(\ln x\): the gradient is \(n\) and the \(\ln y\)-intercept is \(\ln k\).
- \(y = ka^x\): \(\ln y = x\ln a + \ln k\). Plot \(\ln y\) against \(x\): the gradient is \(\ln a\) and the intercept is \(\ln k\).
- To find \(k\) from the intercept \(c\): \(k = e^c\). To find \(a\) from the gradient \(m\): \(a = e^m\).
:::

:::eg The table gives measurements of \(y\) for four values of \(x\). Show that \(y = kx^n\) fits the data and find \(k\) and \(n\).
| \(x\) | 1 | 2 | 4 | 9 |
|---|---|---|---|---|
| \(y\) | 2.00 | 5.66 | 16.0 | 54.0 |
| \(\ln x\) | 0 | 0.693 | 1.386 | 2.197 |
| \(\ln y\) | 0.693 | 1.733 | 2.773 | 3.989 |

The gradient between the first two points is \(\dfrac{1.733 - 0.693}{0.693 - 0} = 1.50\), and between the last two is \(\dfrac{3.989 - 2.773}{2.197 - 1.386} = 1.50\). The gradient is constant, so the points lie on a straight line and the law \(y = kx^n\) fits, with \(n = 1.5\). The intercept is \(\ln k = 0.693\), so \(k = e^{0.693} = 2\). The law is \(y = 2x^{1.5}\).
:::

:::plot Plotting \(\ln y\) against \(\ln x\) for the data above gives a straight line of gradient 1.5 and intercept 0.693, so \(n = 1.5\) and \(k = e^{0.693} = 2\).
--f "1.5*x+0.693" --label "ln y = 1.5 ln x + 0.693" --x -0.5 2.5 --y -0.5 5 --pt "0,0.693,(0, 0.693)@se" --pt "2.197,3.989,(2.197, 3.989)@se" --xlabel "ln x" --ylabel "ln y" --legend tl
:::

:::eg (Exam style) The variables \(x\) and \(y\) satisfy \(y = Ax^b\), where \(A\) and \(b\) are constants. The graph of \(\ln y\) against \(\ln x\) is a straight line passing through \((0.5, 2.1)\) and \((2.5, 7.1)\). Find \(A\) and \(b\). A second relationship \(y = Ka^x\) gives a line of \(\ln y\) against \(x\) through \((2, 3.1)\) and \((6, 5.1)\); find \(K\) and \(a\).
**First relationship.** Taking logs gives \(\ln y = b\ln x + \ln A\). [M1]
The gradient is \(b = \dfrac{7.1 - 2.1}{2.5 - 0.5} = 2.5\). [M1 A1]
The intercept is found from \(2.1 = 2.5(0.5) + \ln A\), so \(\ln A = 0.85\) and \(A = e^{0.85} = 2.34\). [M1 A1]

**Second relationship.** \(\ln y = x\ln a + \ln K\), with gradient \(\ln a = \dfrac{5.1 - 3.1}{6 - 2} = 0.5\), so \(a = e^{0.5} = 1.65\). [M1 A1]
The intercept: \(3.1 = 0.5(2) + \ln K\), so \(\ln K = 2.1\) and \(K = e^{2.1} = 8.17\). [M1 A1]
:::

:::exam Logs in the exam
- Write each log law you use as a line of working. Method marks go to the combining step and to taking logs of both sides.
- Give the answer in the requested form: "exact" means \(\ln 3\) or \(\dfrac{\ln 20}{\ln 3}\), not a decimal; "to 3 significant figures" means decimal.
- Reject any solution that makes an argument of a logarithm zero or negative, and say why.
- When asked to "show that" a straight-line law fits data, calculate the gradient between several pairs of points, or find the equation of the line through two points and check the others lie on it.
:::

:::board Other boards
Edexcel IAL covers exponentials and logarithms in P2 and \(e^x\) and \(\ln x\) in P3. UK A Levels (AQA, Edexcel, OCR) include the laws of logs, \(e^x\) and \(\ln x\), and reduction of exponential and power laws to linear form in Pure Year 1 and Year 2. The change of base formula is not in the Cambridge syllabus; check whether your board includes it.
:::

:::try Start easy, finish at exam standard
Q: Evaluate (a) \(\log_3 81\), (b) \(\log_{10} 0.001\), (c) \(\log_8 2\), (d) \(\ln e^5\).
A: (a) \(4\). (b) \(-3\). (c) \(\tfrac13\), since \(8^{1/3} = 2\). (d) \(5\).
Q: Write \(3\log 2 + \log 5 - \log 4\) as a single logarithm, and simplify.
A: \(\log 8 + \log 5 - \log 4 = \log\dfrac{8 \times 5}{4} = \log 10 = 1\) (base 10).
Q: Solve \(\log_2 (x - 1) + \log_2 (x + 3) = 5\).
A: \(\log_2 (x - 1)(x + 3) = 5\), so \((x - 1)(x + 3) = 32\) and \(x^2 + 2x - 35 = 0\), giving \((x + 7)(x - 5) = 0\). Reject \(x = -7\). So \(x = 5\).
Q: Solve (a) \(5^x = 12\), (b) \(e^{3x - 1} = 10\), (c) \(\ln(x + 4) = 2\), giving answers to 3 significant figures.
A: (a) \(x = \dfrac{\ln 12}{\ln 5} = 1.54\). (b) \(3x - 1 = \ln 10\), so \(x = \dfrac{1 + \ln 10}{3} = 1.10\). (c) \(x + 4 = e^2\), so \(x = e^2 - 4 = 3.39\).
Q: Solve \(e^{2x} - 7e^x + 12 = 0\).
A: \(u = e^x\): \((u - 3)(u - 4) = 0\), so \(x = \ln 3\) or \(x = \ln 4\) (1.10 or 1.39).
Q: Solve \(4^x - 3 \times 2^x - 4 = 0\).
A: Write \(4^x = (2^x)^2\). With \(u = 2^x\): \(u^2 - 3u - 4 = 0\), so \((u - 4)(u + 1) = 0\). \(2^x = 4\) gives \(x = 2\); \(2^x = -1\) is impossible.
Q: Solve (a) \(3^x < 7\), (b) \(0.8^x \le 0.3\). Find the least integer \(n\) with \(1.2^n > 100\).
A: (a) \(x < \dfrac{\ln 7}{\ln 3} = 1.77\). (b) \(\ln 0.8 < 0\), so \(x \ge \dfrac{\ln 0.3}{\ln 0.8} = 5.40\). Last: \(n > \dfrac{\ln 100}{\ln 1.2} = 25.26\), so \(n = 26\).
Q: A car is worth $20 000 and loses 12% of its value each year, so its value after \(t\) years is \(20\,000 \times 0.88^t\). After how many years is it first worth less than $5000?
A: \(0.88^t < 0.25\), so \(t > \dfrac{\ln 0.25}{\ln 0.88} = 10.84\). It is worth less than $5000 during the 11th year, after 10.84 years.
Q: Sketch \(y = e^{-x} + 1\), marking the intercept and the asymptote.
A: The graph is \(y = e^{-x}\) moved up by 1. The \(y\)-intercept is \((0, 2)\) and the asymptote is \(y = 1\). It decreases, approaching \(y = 1\) as \(x \to \infty\).
Q: (Exam style) The table shows measured values of \(x\) and \(y\), which are related by \(y = ka^x\): \((0, 5)\), \((1, 7.5)\), \((2, 11.25)\), \((3, 16.875)\). (a) Show that \(\ln y\) against \(x\) is a straight line and find its gradient and intercept. (b) Hence state the values of \(k\) and \(a\).
A: (a) \(\ln y = 1.609, 2.015, 2.420, 2.826\). [M1] Each step increases \(\ln y\) by \(0.405\), so the gradient is constant \(= 0.405\). The intercept is \(1.609\). [A1 A1] (b) \(\ln a = 0.405\), so \(a = e^{0.405} = 1.5\), and \(\ln k = 1.609\), so \(k = 5\). [M1 A1]
:::

:::quiz
? What is \(\log_2 8 + \log_2 4\)?
- \(\log_2 12\)
- \(6\)
+ \(5\)
- \(32\)
> Use the product law: \(\log_2 8 + \log_2 4 = \log_2 32 = 5\). Equivalently \(3 + 2 = 5\). Adding the numbers inside gives \(\log_2 12\), multiplying the logs gives \(6\), and \(32\) is the number inside the log, not its value.
? Which of these is equal to \(\ln 12 - \ln 4\)?
+ \(\ln 3\)
- \(\ln 8\)
- \(\dfrac{\ln 12}{\ln 4}\)
- \(\ln 16\)
> The quotient law gives \(\ln\dfrac{12}{4} = \ln 3\). Subtracting the numbers (\(\ln 8\)) and adding them (\(\ln 16\)) are the usual slips, and \(\dfrac{\ln 12}{\ln 4}\) confuses a difference with a quotient.
? Solve \(2^x = 9\).
- \(x = 4.5\)
- \(x = 3\)
+ \(x = \dfrac{\ln 9}{\ln 2} = 3.17\)
- \(x = \ln 9 - \ln 2 = 1.50\)
> Take logs of both sides: \(x\ln 2 = \ln 9\), so \(x = \dfrac{\ln 9}{\ln 2}\). Dividing 9 by 2 gives \(4.5\), and subtracting the logs is the quotient law applied to the wrong thing.
? The graph of \(\ln y\) against \(\ln x\) is a straight line with gradient \(3\) and intercept \(\ln 2\). What is the relationship between \(y\) and \(x\)?
- \(y = 3x^2\)
- \(y = 2e^{3x}\)
+ \(y = 2x^3\)
- \(y = 3x + 2\)
> \(\ln y = 3\ln x + \ln 2 = \ln (2x^3)\), so \(y = 2x^3\). The option \(2e^{3x}\) would come from a graph of \(\ln y\) against \(x\).
? The solution of \(\log_5 (x - 2) = 2\) is
- \(x = 12\)
+ \(x = 27\)
- \(x = 8\)
- \(x = 22\)
> \(x - 2 = 5^2 = 25\), so \(x = 27\). The value \(12\) comes from \(5 \times 2 + 2\), and \(8\) from \(2^3\), both common wrong routes.
:::

:::recap
- \(\log_a b = c \iff a^c = b\); \(\log_a 1 = 0\), \(\log_a a = 1\). No logs of zero or negative numbers.
- Laws: \(\log xy = \log x + \log y\), \(\log\frac xy = \log x - \log y\), \(\log x^k = k\log x\). Same base only. Check arguments are positive at the end.
- \(\ln x = \log_e x\) is the inverse of \(e^x\); the graphs reflect in \(y = x\). \(e^{kx}\) is growth for \(k > 0\) and decay for \(k < 0\).
- To solve \(a^x = b\), take logs of both sides: \(x = \dfrac{\ln b}{\ln a}\). Equations in \(e^x\) or \(a^x\) may be quadratics in \(u = e^x\); reject \(u \le 0\).
- In an inequality, dividing by a negative (such as \(\ln 0.5\)) reverses the sign.
- \(y = kx^n\): plot \(\ln y\) against \(\ln x\) (gradient \(n\), intercept \(\ln k\)). \(y = ka^x\): plot \(\ln y\) against \(x\) (gradient \(\ln a\), intercept \(\ln k\)).
:::

:::note Learn more online
- **Watch:** [Rules of logarithms](https://www.examsolutions.net/tutorials/rules-logs/) · ExamSolutions · the three laws with examples
- **Watch:** [Converting curves to linear form](https://www.examsolutions.net/tutorials/modelling-curves-converting-to-linear-form/) · ExamSolutions · y = kxⁿ and y = k(aˣ) from straight lines
- **Practise:** [CAIE Pure 3 laws of logarithms exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/logarithms-and-exponentials/laws-of-logarithms/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Exponentials & Logarithms](https://undergroundmathematics.org/exp-and-log) · Underground Mathematics · rich problems on exponentials and logs
- **Read:** [An intuitive guide to exponential functions and e](https://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/) · BetterExplained · where e comes from
- **Read:** [Demystifying the natural logarithm](https://betterexplained.com/articles/demystifying-the-natural-logarithm-ln/) · BetterExplained · ln x as "time to grow"

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Further trigonometry](#math.p3.trig).
