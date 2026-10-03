@chapter math.s2.linear
@title Linear combinations of random variables
@level a2
@paper CAIE P6 (S2) · Edexcel IAL S3 · UK Further Maths Statistics
@time 4–6 hours
@summary How to find the mean and variance of expressions such as \(aX + b\) and \(aX \pm bY\), and when the answer is again a normal or Poisson distribution. You will learn the rules, the difference between \(X_1 + X_2\) and \(2X\), and how to answer "total mass" and "difference in time" questions.

:::why
Real quantities are built from other quantities. The mass of a parcel is the mass of the box plus the mass of the contents. The time of a journey is a sum of the stages. A lift carries several people, and a machine fills many bottles. Once you can find the mean and variance of a combination, you can answer questions such as "what is the chance that four people overload the lift?" with the normal tables you already know.
:::

**Before you start**, you need \(E(X)\) and \(\mathrm{Var}(X)\) from [Discrete random variables](#math.s1.drv), the normal distribution from [The normal distribution](#math.s1.normal) and the Poisson distribution from [The Poisson distribution](#math.s2.poisson).

## Changing a variable: \(aX + b\)

Suppose \(C\) is the temperature in a classroom in degrees Celsius, with mean 18 and variance 4. The temperature in degrees Fahrenheit is \(F = 1.8C + 32\). What are the mean and variance of \(F\)?

Two different things happen:

- **Adding a constant** (the 32) moves every value up by 32. The mean moves up by 32, but the values are no more spread out than before. The variance does not change.
- **Multiplying by a constant** (the 1.8) stretches every value away from zero. The mean is multiplied by 1.8. The spread is multiplied by 1.8 too, so the standard deviation is multiplied by 1.8 and the **variance by \(1.8^2\)**.

:::key Linear change of a variable
For any random variable \(X\) and constants \(a\) and \(b\):
\[E(aX + b) = aE(X) + b \qquad \mathrm{Var}(aX + b) = a^2\,\mathrm{Var}(X)\]
- The constant \(b\) affects the mean only.
- The multiplier \(a\) is squared in the variance. If \(a\) is negative, \(a^2\) is still positive.
- Standard deviation: \(\mathrm{sd}(aX + b) = |a|\,\mathrm{sd}(X)\).
You may use these results without proof. Learn them: MF19 does not give the rule for \(\mathrm{Var}(aX + bY)\).
:::

:::eg \(C\) has mean 18 and variance 4. Find the mean, variance and standard deviation of \(F = 1.8C + 32\).
\[E(F) = 1.8 \times 18 + 32 = 64.4\]
\[\mathrm{Var}(F) = 1.8^2 \times 4 = 12.96\]
The standard deviation is \(\sqrt{12.96} = 3.6\), which is also \(1.8 \times 2\), the old standard deviation times the multiplier.
:::

:::eg The number of items \(X\) in an online order has \(E(X) = 2.6\) and \(\mathrm{Var}(X) = 1.04\). Postage is \(£4\) plus \(£1.50\) per item. Find the mean and standard deviation of the postage.
Postage \(P = 4 + 1.5X\).
\[E(P) = 4 + 1.5 \times 2.6 = 7.9\]
\[\mathrm{Var}(P) = 1.5^2 \times 1.04 = 2.34, \quad \mathrm{sd}(P) = \sqrt{2.34} = 1.53\]
The mean postage is \(£7.90\) and the standard deviation is \(£1.53\) (3 s.f.). The fixed charge of \(£4\) adds nothing to the spread.
:::

For a **discrete** variable you can test the rule with a table.

:::eg \(X\) takes the values 1, 2, 3 with probabilities 0.2, 0.5, 0.3. Find \(E(3X - 2)\) and \(\mathrm{Var}(3X - 2)\), and check by listing the values of \(3X - 2\).
\(E(X) = 0.2 + 1.0 + 0.9 = 2.1\), \(E(X^2) = 0.2 + 2.0 + 2.7 = 4.9\), so \(\mathrm{Var}(X) = 4.9 - 2.1^2 = 0.49\).

\(E(3X - 2) = 3 \times 2.1 - 2 = 4.3\) and \(\mathrm{Var}(3X - 2) = 9 \times 0.49 = 4.41\).

Check: \(3X - 2\) takes the values 1, 4, 7 with the same probabilities. Its mean is \(0.2 + 2.0 + 2.1 = 4.3\). Its mean of squares is \(0.2 + 8 + 14.7 = 22.9\), and \(22.9 - 4.3^2 = 4.41\). The rule agrees.
:::

:::warn Variance is not linear
\(\mathrm{Var}(3X - 2)\) is not \(3\,\mathrm{Var}(X) - 2\). Square the multiplier and drop the constant. The most common slip is to forget the square, giving \(3 \times 0.49 = 1.47\) instead of \(4.41\).
:::

## Combining two variables: \(aX + bY\)

Now take two different random variables \(X\) and \(Y\), for example the mass of a box and the mass of its contents.

:::key Linear combination of two variables
For any random variables \(X\) and \(Y\):
\[E(aX + bY) = aE(X) + bE(Y)\]
If \(X\) and \(Y\) are **independent**, then
\[\mathrm{Var}(aX + bY) = a^2\,\mathrm{Var}(X) + b^2\,\mathrm{Var}(Y)\]
- The mean rule always holds, independent or not.
- The variance rule needs independence. Knowing the value of one variable must tell you nothing about the other.
- **Variances add even when you subtract the variables**: \(\mathrm{Var}(X - Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)\), because \((-1)^2 = 1\).
- Both rules extend to three or more variables.
:::

Why do the variances add for a difference? A difference such as \(X - Y\) can be unusually large if \(X\) is high and \(Y\) is low, or unusually small if \(X\) is low and \(Y\) is high. Two sources of variation make the result less predictable, not more.

:::eg \(E(X) = 5\), \(E(Y) = 2\), \(\mathrm{Var}(X) = 4\), \(\mathrm{Var}(Y) = 9\), and \(X\) and \(Y\) are independent. Find the mean and variance of \(2X - 3Y + 1\).
\[E(2X - 3Y + 1) = 2 \times 5 - 3 \times 2 + 1 = 5\]
\[\mathrm{Var}(2X - 3Y + 1) = 2^2 \times 4 + (-3)^2 \times 9 = 16 + 81 = 97\]
The constant 1 does not enter the variance, and the minus sign in front of \(3Y\) disappears when it is squared.
:::

## \(X_1 + X_2\) is not the same as \(2X\)

This is the idea examiners test most.

:::def Independent observations of \(X\)
If \(X_1\) and \(X_2\) are independent observations of \(X\), they are two separate, independent random variables, each with the same distribution as \(X\). So \(E(X_1) = E(X_2) = E(X)\) and \(\mathrm{Var}(X_1) = \mathrm{Var}(X_2) = \mathrm{Var}(X)\).
:::

Compare two situations. A machine fills bottles with \(X \sim N(500, 4^2)\) millilitres.

- **\(2X\)**: you weigh one bottle and double it, as if the second bottle were an exact copy. If the bottle is 4 ml over, the double is 8 ml over.
- **\(X_1 + X_2\)**: you take two different bottles. One may be over and the other under, and the errors partly cancel.

Both have mean \(1000\), but the spread differs:
\[\mathrm{Var}(2X) = 2^2 \times 16 = 64 \qquad \mathrm{Var}(X_1 + X_2) = 16 + 16 = 32\]

:::plot Both distributions have mean 1000 ml. The total of two different bottles, \(X_1 + X_2\), has variance 32 and is narrower and taller than twice one bottle, \(2X\), which has variance 64.
--f "exp(-((x-1000)**2)/(2*32))/sqrt(2*pi*32)" --f "exp(-((x-1000)**2)/(2*64))/sqrt(2*pi*64)" --label "X₁ + X₂ (variance 32)" --label "2X (variance 64)" --x 975 1025 --y 0 0.08 --vline 1010 --legend tl --xlabel "total volume (ml)"
:::

The tail beyond 1010 ml shows the difference. For \(X_1 + X_2\), \(P(\text{total} > 1010) = P\!\left(Z > \dfrac{10}{\sqrt{32}}\right) = P(Z > 1.768) = 0.0385\). For \(2X\), \(P(2X > 1010) = P\!\left(Z > \dfrac{10}{8}\right) = 0.106\). Treating two bottles as one doubled bottle nearly triples the chance of a large total.

:::warn Two bottles or one doubled?
Look for the word "independent" and for how the quantities are described. "The total mass of 2 bags" means \(X_1 + X_2\) (variance \(2\sigma^2\)). "A bag is weighed and the result doubled", or "twice the mass of one bag", means \(2X\) (variance \(4\sigma^2\)). Using \(2X\) when you need \(X_1 + X_2\) loses every accuracy mark after the variance.
:::

### Sums of \(n\) independent observations

For \(n\) independent observations \(X_1, X_2, \dots, X_n\) of \(X\), with \(E(X) = \mu\) and \(\mathrm{Var}(X) = \sigma^2\):
\[E(X_1 + \dots + X_n) = n\mu \qquad \mathrm{Var}(X_1 + \dots + X_n) = n\sigma^2\]
The standard deviation grows only like \(\sqrt{n}\), not like \(n\). This is why averages are more reliable than single readings, which the [sampling chapter](#math.s2.sampling) builds on.

## Combinations of normal variables

:::key Normal variables
If \(X \sim N(\mu_X, \sigma_X^2)\) and \(Y \sim N(\mu_Y, \sigma_Y^2)\) are independent, then
\[aX + bY \sim N\!\left(a\mu_X + b\mu_Y,\; a^2\sigma_X^2 + b^2\sigma_Y^2\right)\]
Also, \(aX + b\) is normal when \(X\) is normal. The same holds for any number of independent normal variables.
:::

So the mean and variance come from the rules above, and the **shape** is normal. Then you can use the standard method from [The normal distribution](#math.s1.normal): define the new variable, state its distribution, standardise and read the probability.

:::steps
1. Name the combination, for example \(T = X_1 + X_2 + X_3 + X_4\) or \(D = B - C\).
2. Find \(E\) and \(\mathrm{Var}\) with the rules. State that the variables are independent.
3. Write the distribution: \(T \sim N(\text{mean},\ \text{variance})\).
4. Translate the question into an inequality for \(T\) (for "\(B\) takes less time than \(C\)" this is \(B - C < 0\)).
5. Standardise with \(z = \dfrac{t - \text{mean}}{\sqrt{\text{variance}}}\) and use \(\Phi\).
:::

:::eg The mass of an adult passenger is \(X \sim N(75, 8^2)\) kg. A lift is overloaded if the total mass of four independent passengers exceeds 320 kg. Find the probability of overload, and the total mass that is exceeded with probability 0.05.
Let \(T = X_1 + X_2 + X_3 + X_4\). Then \(E(T) = 4 \times 75 = 300\) and \(\mathrm{Var}(T) = 4 \times 64 = 256\), so \(T \sim N(300, 16^2)\).

\[P(T > 320) = P\!\left(Z > \frac{320 - 300}{16}\right) = P(Z > 1.25) = 1 - 0.8944 = 0.106\]

For the second part, \(P(T > k) = 0.05\) means \(\Phi\!\left(\dfrac{k - 300}{16}\right) = 0.95\), so \(\dfrac{k - 300}{16} = 1.645\) and \(k = 300 + 1.645 \times 16 = 326\) kg (3 s.f.).
:::

:::eg A student can travel to school by bus or by bike. The bus journey time is \(B \sim N(25, 4^2)\) minutes and the bike time is \(C \sim N(28, 3^2)\) minutes, independently. Find the probability that on a given day the bus is quicker than the bike.
Bus quicker means \(B < C\), that is \(B - C < 0\). Let \(D = B - C\).
\[E(D) = 25 - 28 = -3 \qquad \mathrm{Var}(D) = 16 + 9 = 25\]
So \(D \sim N(-3, 5^2)\).
\[P(D < 0) = P\!\left(Z < \frac{0 - (-3)}{5}\right) = \Phi(0.6) = 0.726\]
Sense check: the bus is quicker on average by 3 minutes, so a probability above one half is right.
:::

:::eg (Exam style) The mass of a croissant is \(X \sim N(60, 5^2)\) grams and the mass of a pain au chocolat is \(Y \sim N(80, 6^2)\) grams, independently. A box holds 2 croissants and 1 pain au chocolat, all chosen at random. Find the probability that the contents of a box weigh more than 215 g. [5 marks]
Let \(T = X_1 + X_2 + Y\), where \(X_1\) and \(X_2\) are independent croissants. Note that this is **not** \(2X + Y\).
\[E(T) = 60 + 60 + 80 = 200\] [B1]
\[\mathrm{Var}(T) = 25 + 25 + 36 = 86\] [M1 A1]
So \(T \sim N(200, 86)\) and the standard deviation is \(\sqrt{86} = 9.274\).
\[P(T > 215) = P\!\left(Z > \frac{215 - 200}{\sqrt{86}}\right) = P(Z > 1.617)\] [M1]
\[= 1 - 0.9471 = 0.0529\] [A1]
:::

## Combinations of Poisson variables

:::key Sum of independent Poisson variables
If \(X \sim \mathrm{Po}(\lambda)\) and \(Y \sim \mathrm{Po}(\mu)\) are independent, then
\[X + Y \sim \mathrm{Po}(\lambda + \mu)\]
This extends to any number of independent Poisson variables.
:::

This matches the interval rule from the [Poisson chapter](#math.s2.poisson): events in two separate intervals, each at a constant average rate, add up to a Poisson count with the combined mean.

:::eg Calls to helpline A in an hour follow \(\mathrm{Po}(3.2)\) and calls to helpline B follow \(\mathrm{Po}(1.8)\), independently. Find the probability that the total number of calls in an hour is (a) exactly 6, (b) at least 3.
Let \(T = A + B\). Then \(T \sim \mathrm{Po}(5)\).

(a) \(P(T = 6) = e^{-5}\dfrac{5^6}{6!} = 0.146\).

(b) \(P(T \ge 3) = 1 - P(T \le 2) = 1 - e^{-5}\left(1 + 5 + \dfrac{25}{2}\right) = 1 - 18.5e^{-5} = 0.875\).
:::

Take care. Only a **sum** of independent Poissons is Poisson. A difference and a multiple are not.

:::warn Poisson traps
- \(X - Y\) is not Poisson: it can be negative.
- \(2X\) is not Poisson. If \(X \sim \mathrm{Po}(2)\), then \(2X\) has mean 4 but variance \(2^2 \times 2 = 8\). A Poisson variable has mean equal to variance, so \(2X\) cannot be Poisson.
- \(X_1 + X_2\), two independent observations of \(X \sim \mathrm{Po}(2)\), is \(\mathrm{Po}(4)\), with mean and variance both 4.
You can still find \(E\) and \(\mathrm{Var}\) of \(X - Y\) and \(2X\) with the general rules, but you cannot use Poisson tables for them.
:::

:::exam Presentation
Define each new variable with a letter, state "independent" where the question allows it, and write the full distribution before you standardise: \(T \sim N(300, 256)\). Marks go to the mean, the variance (watch the squares) and the standardisation. Give the variance, not the standard deviation, as the second parameter of \(N(\cdot,\cdot)\). Keep \(z\)-values to 3 s.f. and the final probability to 3 s.f.
:::

:::board
- **Edexcel IAL**: combinations of random variables are in IAL S3, not S2.
- **UK A Level (AQA 7357, Edexcel 9MA0, OCR H240)**: there is no Poisson distribution in the single A Level, so the Poisson part is Further Maths only.
- The rules \(E(aX + b)\) and \(\mathrm{Var}(aX + b)\) are standard everywhere.
:::

:::try Start easy, finish at exam standard
Q: \(E(X) = 10\) and \(\mathrm{Var}(X) = 3\). Find \(E(4X - 1)\), \(\mathrm{Var}(4X - 1)\) and \(\mathrm{Var}(-2X)\).
A: \(E(4X - 1) = 40 - 1 = 39\). \(\mathrm{Var}(4X - 1) = 16 \times 3 = 48\). \(\mathrm{Var}(-2X) = (-2)^2 \times 3 = 12\).
Q: \(X\) and \(Y\) are independent with \(E(X) = 6\), \(\mathrm{Var}(X) = 2\), \(E(Y) = 9\), \(\mathrm{Var}(Y) = 5\). Find the mean and variance of \(3X - Y\).
A: \(E = 18 - 9 = 9\). \(\mathrm{Var} = 9 \times 2 + 1 \times 5 = 23\).
Q: \(X\) has mean 12 and variance 9. Find the mean and variance of \(X_1 + X_2 + X_3\), three independent observations of \(X\), and of \(3X\).
A: \(E(X_1 + X_2 + X_3) = 36\) and \(\mathrm{Var} = 27\). \(E(3X) = 36\) and \(\mathrm{Var}(3X) = 9 \times 9 = 81\).
Q: \(X \sim N(50, 6^2)\) and \(Y \sim N(40, 8^2)\) are independent. State the distribution of \(X + Y\) and find \(P(X + Y > 100)\).
A: \(X + Y \sim N(90, 100)\). \(P(X + Y > 100) = P(Z > 1) = 1 - 0.8413 = 0.159\).
Q: With \(X\) and \(Y\) as in the previous question, find \(P(X > Y + 5)\).
A: \(X - Y - 5 \sim N(50 - 40 - 5,\ 36 + 64) = N(5, 100)\). \(P(X - Y - 5 > 0) = P\!\left(Z > \dfrac{0 - 5}{10}\right) = P(Z > -0.5) = \Phi(0.5) = 0.691\).
Q: Apples have mass \(X \sim N(150, 20^2)\) grams. Find the probability that 6 randomly chosen apples have a total mass of more than 1 kg.
A: \(T \sim N(900, 6 \times 400 = 2400)\), sd \(= 48.99\). \(P(T > 1000) = P(Z > 2.041) = 0.0206\).
Q: \(X \sim \mathrm{Po}(2.5)\) and \(Y \sim \mathrm{Po}(1.5)\) are independent. Find \(P(X + Y = 2)\) and explain why \(X - Y\) is not Poisson.
A: \(X + Y \sim \mathrm{Po}(4)\), so \(P(X + Y = 2) = e^{-4}\dfrac{4^2}{2} = 8e^{-4} = 0.147\). \(X - Y\) can take negative values, and a Poisson variable cannot.
Q: Boxes of tea have mass \(X \sim N(250, 3^2)\) g. A carton holds 12 boxes (independent) and the empty carton has mass \(M \sim N(80, 2^2)\) g, independent of the boxes. Find the probability that a full carton has mass less than 3070 g.
A: \(T = X_1 + \dots + X_{12} + M\). \(E(T) = 3000 + 80 = 3080\). \(\mathrm{Var}(T) = 12 \times 9 + 4 = 112\). \(P(T < 3070) = P\!\left(Z < \dfrac{-10}{\sqrt{112}}\right) = \Phi(-0.945) = 0.172\).
Q: (Exam style) The time \(A\) minutes for Anna to run 5 km is \(N(27, 2.5^2)\) and the time \(B\) minutes for Ben is \(N(26, 3^2)\), independent. (a) Find the probability that Anna beats Ben. (b) Find the probability that the combined time of Anna and Ben is under 50 minutes. [7 marks]
A: (a) \(A - B \sim N(1, 6.25 + 9 = 15.25)\) [M1 A1]. Anna wins if \(A - B < 0\): \(P = \Phi\!\left(\dfrac{-1}{3.905}\right) = \Phi(-0.256) = 0.399\). [M1 A1] (b) \(A + B \sim N(53, 15.25)\) [B1]. \(P(A + B < 50) = \Phi\!\left(\dfrac{-3}{3.905}\right) = \Phi(-0.768) = 0.221\). [M1 A1]
Q: (Exam style) Packets of sugar have mass \(X\) with mean 1010 g and standard deviation 12 g. Packets are put into bags of 4, and a bag's mass is the total of 4 independent packets. Find the mean and standard deviation of the mass of a bag. A shop owner says "the standard deviation of a bag is \(4 \times 12 = 48\) g". Explain the mistake. [4 marks]
A: \(E = 4 \times 1010 = 4040\) g [B1]. \(\mathrm{Var} = 4 \times 144 = 576\) [M1], so the standard deviation is \(24\) g [A1]. The owner multiplied the standard deviation by 4. That treats the four packets as copies of one packet (\(4X\), standard deviation 48). The packets are independent, so their errors partly cancel and the variances add. [B1]
:::

:::quiz Check your understanding
? \(\mathrm{Var}(X) = 5\). What is \(\mathrm{Var}(3X + 2)\)?
- 17
- 15
+ 45
- 47
> Multiply the variance by \(3^2 = 9\) and ignore the constant: \(9 \times 5 = 45\). 15 forgets to square, and adding 2 is never part of a variance.
? \(X\) and \(Y\) are independent with \(\mathrm{Var}(X) = 4\) and \(\mathrm{Var}(Y) = 1\). What is \(\mathrm{Var}(X - Y)\)?
- 3
+ 5
- 9
- 15
> Variances add for a difference: \(4 + 1 = 5\). Subtracting the variances, giving 3, is the classic slip.
? \(X \sim N(10, 2^2)\). What is the variance of \(X_1 + X_2\) (two independent observations) and of \(2X\)?
- 8 and 8
- 4 and 4
+ 8 and 16
- 16 and 8
> \(\mathrm{Var}(X_1 + X_2) = 4 + 4 = 8\) but \(\mathrm{Var}(2X) = 2^2 \times 4 = 16\). Two separate observations are less variable than one doubled.
? \(X \sim \mathrm{Po}(3)\) and \(Y \sim \mathrm{Po}(4)\) are independent. Which statement is true?
- \(X - Y \sim \mathrm{Po}(-1)\)
- \(2X \sim \mathrm{Po}(6)\)
+ \(X + Y \sim \mathrm{Po}(7)\)
- \(X + Y \sim \mathrm{Po}(12)\)
> Only the sum of independent Poisson variables is Poisson, and the means add: 7. A difference can be negative, and \(2X\) has mean 6 but variance 12, so it is not Poisson.
? The masses of two items are independent, \(N(20, 3^2)\) and \(N(30, 4^2)\). The total mass has standard deviation:
- 7
- 25
+ 5
- 1
> The variance of the total is \(9 + 16 = 25\), so the standard deviation is \(\sqrt{25} = 5\). Adding the standard deviations (7) or the variances without square-rooting (25) are the usual errors.
:::

:::recap
- \(E(aX + b) = aE(X) + b\) and \(\mathrm{Var}(aX + b) = a^2\mathrm{Var}(X)\): the constant moves the mean only; the multiplier is squared.
- \(E(aX + bY) = aE(X) + bE(Y)\) always. For independent \(X, Y\): \(\mathrm{Var}(aX + bY) = a^2\mathrm{Var}(X) + b^2\mathrm{Var}(Y)\). Variances add for a difference.
- \(X_1 + X_2\) (two independent observations) has variance \(2\sigma^2\). \(2X\) has variance \(4\sigma^2\). For \(n\) observations the sum has mean \(n\mu\) and variance \(n\sigma^2\).
- Independent normals: any linear combination is normal. Find the mean and variance, then standardise.
- Independent Poissons: the sum is \(\mathrm{Po}(\lambda + \mu)\). Differences and multiples are not Poisson.
:::

:::note Learn more online
- **Watch:** [Var(aX + bY) for independent X and Y](https://www.examsolutions.net/tutorials/varax-by-a2varx-b2vary-for-independent-x-and-y/) · ExamSolutions · why the variances add
- **Practise:** [CAIE S2 linear combinations exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/topic-questions/statistical-distributions/linear-combinations-of-random-variables/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Practise:** [Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) · Khan Academy · the random variables unit
- **Read:** [Introductory Statistics 2e (free textbook)](https://openstax.org/details/books/introductory-statistics-2e) · OpenStax · random variables explained with exercises
- **Papers:** [9709 Paper 6 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-7/) · Physics & Maths Tutor · their page "cie-paper-7" holds Paper 6 *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Continuous random variables](#math.s2.crv).
