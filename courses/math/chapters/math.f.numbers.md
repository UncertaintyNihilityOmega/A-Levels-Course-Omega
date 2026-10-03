@chapter math.f.numbers
@title Numbers, fractions and percentages
@level pre
@paper Prior knowledge for CAIE 9709 · Edexcel IAL · AQA/OCR/Edexcel (GCSE or IGCSE Number)
@time 4–6 hours
@summary The arithmetic that every A Level assumes: types of number, negatives, the order of operations, fractions, decimals, percentages and multipliers, ratio and proportion, rounding, estimation, primes, HCF and LCM.

:::why
Every A Level question uses arithmetic. Calculators are allowed in Cambridge 9709, but a calculator cannot repair a wrong idea. A student who is unsure about fractions, negatives or percentages loses marks in algebra, statistics and mechanics too, and cannot tell when an answer is absurd. A few hours here make every later chapter easier.
:::

You need nothing except basic school arithmetic. If a section feels easy, try its questions in the box at the end and move on. The next chapter, [Algebra from scratch](#math.f.algebra), turns these rules into letters.

## Types of number

Numbers come in families, and each family sits inside a bigger one.

:::def Integer
A whole number, positive, negative or zero: \(\ldots, -2, -1, 0, 1, 2, \ldots\)
:::

:::def Rational number
A number that can be written as a fraction \(\dfrac{a}{b}\) with \(a\) and \(b\) integers and \(b \neq 0\). Its decimal form stops (such as \(0.25\)) or repeats for ever (such as \(0.333\ldots\)).
:::

:::def Irrational number
A number that cannot be written as a fraction of two integers. Its decimal form never stops and never repeats, for example \(\sqrt{2}\), \(\pi\) and \(e\).
:::

Together, rational and irrational numbers make up the **real numbers**: every point on the number line. The **natural numbers** are the counting numbers \(1, 2, 3, \ldots\) The symbols \(\mathbb{N}\), \(\mathbb{Z}\), \(\mathbb{Q}\) and \(\mathbb{R}\) are shorthand you will meet in function questions, such as "\(x \in \mathbb{R}\)", which means "\(x\) is a real number".

:::html
<figure class="fig"><svg viewBox="0 0 600 300" role="img" aria-label="Nested sets: natural numbers inside integers inside rational numbers; rational and irrational numbers together make the real numbers">
<rect class="fm" x="8" y="8" width="584" height="284" rx="14"/>
<text class="tb" x="24" y="32">Real numbers, ℝ</text>
<rect class="f1 s-acc sw2" x="24" y="44" width="384" height="236" rx="12"/>
<text class="tb" x="40" y="68">Rational numbers, ℚ</text>
<text class="ts" x="40" y="85">fractions such as ½, −¾, 0.25, 0.333…</text>
<rect class="f2 s-acc2 sw2" x="44" y="98" width="306" height="170" rx="10"/>
<text class="tb" x="60" y="122">Integers, ℤ</text>
<text class="ts" x="60" y="139">…, −3, −2, −1, 0, 1, 2, 3, …</text>
<rect class="fh s-mute sw1" x="64" y="152" width="196" height="100" rx="8"/>
<text class="tb" x="80" y="176">Natural numbers, ℕ</text>
<text class="ts" x="80" y="193">1, 2, 3, 4, …</text>
<text class="ts" x="80" y="210">the counting numbers</text>
<rect class="fp s-mute sw1 dash" x="424" y="44" width="152" height="236" rx="12"/>
<text class="tb tc" x="500" y="108">Irrational</text>
<text class="tb tc" x="500" y="126">numbers</text>
<text class="tc" x="500" y="158">√2, π, e</text>
<text class="ts tc" x="500" y="186">decimals that never</text>
<text class="ts tc" x="500" y="202">end or repeat</text>
</svg><figcaption>Every natural number is an integer, every integer is rational, and every rational number is real. Irrational numbers are real but not rational.</figcaption></figure>
:::

## Negative numbers

Picture a number line: adding moves you right, subtracting moves you left. The signs follow four rules.

| Situation | Rule | Example |
|---|---|---|
| Subtracting a negative | Same as adding | \(5 - (-3) = 8\) |
| Adding a negative | Same as subtracting | \(5 + (-3) = 2\) |
| Multiplying or dividing, same signs | Positive answer | \((-4) \times (-6) = 24\) |
| Multiplying or dividing, different signs | Negative answer | \(12 \div (-3) = -4\) |

:::warn Squaring a negative number
\(-3^2\) means \(-(3^2) = -9\), because the power acts before the minus sign. \((-3)^2 = (-3) \times (-3) = 9\). This slip causes many errors in the quadratic formula, so use brackets every time you square a negative number.
:::

## The order of operations

Calculations are done in a fixed order, remembered as **BIDMAS**: Brackets, Indices (powers and roots), Division and Multiplication, then Addition and Subtraction. Division and multiplication share the same rank, so work left to right. Addition and subtraction also share a rank. A fraction line and a root sign act like brackets.

:::eg Work out \(3 + 4 \times 2^2 - 10 \div 5\)
Indices first: \(2^2 = 4\). Then multiplication and division, left to right: \(4 \times 4 = 16\) and \(10 \div 5 = 2\). Finally \(3 + 16 - 2 = 17\).
:::

:::eg Work out \(12 - (3 - 7)^2 \div 2\)
Brackets: \(3 - 7 = -4\). Indices: \((-4)^2 = 16\). Division: \(16 \div 2 = 8\). Subtraction: \(12 - 8 = 4\).
:::

:::tip Brackets on the calculator
To work out \(\dfrac{5 + 7}{2 \times 3}\), type \((5 + 7) \div (2 \times 3)\) and get \(2\). Without the brackets the calculator computes \(5 + 7 \div 2 \times 3 = 15.5\).
:::

## Fractions

A fraction \(\dfrac{a}{b}\) has a **numerator** \(a\) on top and a **denominator** \(b\) below. Fractions such as \(\tfrac24\) and \(\tfrac36\) are **equivalent** to \(\tfrac12\): multiply or divide top and bottom by the same number. To **simplify** a fraction, divide both parts by their highest common factor (explained at the end of this chapter).

:::steps
1. **Add or subtract:** write both fractions over a common denominator, then add or subtract the numerators only.
2. **Multiply:** multiply the numerators and multiply the denominators. Cancel common factors first to keep the numbers small.
3. **Divide:** turn the second fraction upside down (its **reciprocal**) and multiply.
4. **Mixed numbers:** change \(2\tfrac13\) to the improper fraction \(\tfrac73\) before doing anything else.
:::

:::eg Work out \(\dfrac34 + \dfrac56\) and \(3\tfrac14 - 1\tfrac56\)
The lowest common denominator of 4 and 6 is 12:
\[\frac34 + \frac56 = \frac{9}{12} + \frac{10}{12} = \frac{19}{12} = 1\tfrac{7}{12}\]
Change to improper fractions: \(3\tfrac14 = \tfrac{13}{4}\) and \(1\tfrac56 = \tfrac{11}{6}\). Then
\[\frac{13}{4} - \frac{11}{6} = \frac{39}{12} - \frac{22}{12} = \frac{17}{12} = 1\tfrac{5}{12}\]
:::

:::eg Work out \(2\tfrac13 \times 1\tfrac12\) and \(\dfrac58 \div \dfrac{15}{16}\)
\[2\tfrac13 \times 1\tfrac12 = \frac{7}{3} \times \frac{3}{2} = \frac{7}{2} = 3\tfrac12\]
(the 3s cancel). For the division, flip the second fraction and cancel:
\[\frac58 \div \frac{15}{16} = \frac58 \times \frac{16}{15} = \frac{1 \times 2}{1 \times 3} = \frac23\]
:::

:::warn Never add fractions straight across
\(\tfrac12 + \tfrac13\) is not \(\tfrac25\). The answer must be bigger than \(\tfrac12\), and \(\tfrac25\) is smaller. The correct answer is \(\tfrac36 + \tfrac26 = \tfrac56\). The same rules work for fractions that contain letters.
:::

## Decimals and recurring decimals

Each place to the right of the decimal point is ten times smaller: tenths, hundredths, thousandths. To change a fraction to a decimal, divide the top by the bottom: \(\tfrac38 = 3 \div 8 = 0.375\). To go back, write the decimal over a power of 10 and simplify: \(0.35 = \tfrac{35}{100} = \tfrac{7}{20}\).

Some fractions never terminate. \(\tfrac13 = 0.333\ldots\) is written \(0.\dot{3}\), where the dot marks the repeating digit. For a block of digits, a dot goes over the first and last digit, so \(0.272727\ldots = 0.\dot{2}\dot{7}\). Every recurring decimal is a rational number, and there is a method to find its fraction.

:::eg Write \(0.\dot{2}\dot{7}\) as a fraction in its simplest form.
Let \(x = 0.272727\ldots\) Two digits repeat, so multiply by 100: \(100x = 27.272727\ldots\) Subtract the first line from the second so the repeating part disappears:
\[99x = 27 \quad\Rightarrow\quad x = \frac{27}{99} = \frac{3}{11}\]
Check: \(3 \div 11 = 0.2727\ldots\) The same idea sums geometric series in [Series](#math.p1.series).
:::

## Percentages

:::def Percentage
A fraction with denominator 100. "Per cent" means "out of 100", so \(45\% = \dfrac{45}{100} = 0.45\).
:::

To change a percentage to a decimal, divide by 100. To find a percentage of an amount, multiply by the decimal: \(35\%\) of \(80 = 0.35 \times 80 = 28\). To find a **percentage change**, always compare with the **original** value:

\[\text{percentage change} = \frac{\text{change}}{\text{original}} \times 100\%\]

The most useful tool is the **multiplier**.

:::key Percentage multipliers
- Increase by \(p\%\): multiply by \(1 + \dfrac{p}{100}\). So \(+15\%\) is \(\times 1.15\).
- Decrease by \(p\%\): multiply by \(1 - \dfrac{p}{100}\). So \(-20\%\) is \(\times 0.8\).
- Repeat a change \(n\) times: multiply by the multiplier to the power \(n\).
- Undo a change: **divide** by the multiplier.
:::

:::eg A phone falls in price from $250 to $210. Find the percentage decrease.
\[\frac{250 - 210}{250} \times 100\% = \frac{40}{250} \times 100\% = 16\%\]
:::

:::eg After a 20% discount a jacket costs $64. What was the original price?
The sale price is \(80\%\) of the original, so \(\text{original} \times 0.8 = 64\) and
\[\text{original} = \frac{64}{0.8} = 80\]
Check: \(20\%\) of \(80\) is \(16\), and \(80 - 16 = 64\). Taking \(20\%\) off \(64\), or multiplying it by \(1.2\), would be wrong, because the \(20\%\) was taken from the original price, not from \(64\).
:::

:::eg $5000 is invested at 4% compound interest a year. How much is it worth after 3 years?
Each year the amount is multiplied by \(1.04\):
\[5000 \times 1.04^3 = 5624.32\]
The investment is worth $5624.32.
:::

## Ratio and proportion

A **ratio** compares quantities. Simplify it by dividing every part by their highest common factor: \(18 : 24 : 30 = 3 : 4 : 5\). To share an amount in a ratio, add the parts, find the value of one part, then multiply.

:::eg Share $240 in the ratio 3 : 5.
There are \(3 + 5 = 8\) parts, and \(240 \div 8 = 30\) per part. The shares are $90 and $150 (that is \(3 \times 30\) and \(5 \times 30\)). Check: \(90 + 150 = 240\).
:::

Two quantities are in **direct proportion** if doubling one doubles the other (\(y = kx\)). Find the value of one unit first. They are in **inverse proportion** if doubling one halves the other (\(y = \dfrac{k}{x}\)): the product stays constant.

:::eg 12 biscuits need 250 g of flour. How much flour for 30 biscuits? Five workers take 12 days to build a wall; how long would 8 workers take?
Flour: \(250 \div 12\) g per biscuit, so \(250 \div 12 \times 30 = 625\) g.

Workers: more workers means fewer days, so use inverse proportion. The job is \(5 \times 12 = 60\) worker-days, so 8 workers take \(60 \div 8 = 7.5\) days.
:::

## Rounding, significant figures and estimation

:::def Significant figures
The digits of a number counted from the first non-zero digit on the left. Zeros at the start are not significant: \(0.00397\) has 3 significant figures. Zeros that come after another digit are significant if they show accuracy: \(2.10\) has 3.
:::

To round to a given place, look at the digit **after** it. If it is 5 or more, round up; otherwise leave the digit as it is. Then fill any gap before the decimal point with zeros.

| Number | 2 decimal places | 3 significant figures |
|---|---|---|
| \(47.8564\) | \(47.86\) | \(47.9\) |
| \(0.003972\) | \(0.00\) | \(0.00397\) |
| \(58\,762.4\) | \(58\,762.40\) | \(58\,800\) |
| \(2.0996\) | \(2.10\) | \(2.10\) |

The second row shows why significant figures matter for small numbers: two decimal places destroy all the information. In the last row the zero must be written, because \(2.1\) would claim only 2 significant figures.

:::exam Accuracy rules in Cambridge papers
Unless the question says otherwise, give non-exact answers to **3 significant figures**, and angles in degrees to **1 decimal place**. Money is normally given to 2 decimal places. "Exact" means leave fractions, surds and \(\pi\) in the answer. Never round in the middle of a calculation: keep the full value on your calculator, use the answer key, and round only the final answer. Early rounding can cost the accuracy mark.
:::

**Estimation** checks that an answer is sensible. Round each number to 1 significant figure and calculate.

:::eg Estimate \(\dfrac{6.82 \times 29.4}{0.48}\), then use a calculator.
\(\dfrac{7 \times 30}{0.5} = \dfrac{210}{0.5} = 420\). A calculator gives \(417.725\ldots\), which is \(418\) to 3 significant figures. The two answers agree, so a slip such as a misplaced decimal point is unlikely.
:::

## Primes, factors and multiples

:::def Prime number
A whole number greater than 1 whose only factors are 1 and itself. The first primes are \(2, 3, 5, 7, 11, 13, \ldots\) The number 2 is the only even prime.
:::

Every whole number greater than 1 is a product of primes in exactly one way, apart from the order. To find it, divide repeatedly by the smallest prime that fits: \(84 = 2 \times 42 = 2 \times 2 \times 21 = 2^2 \times 3 \times 7\). To test whether \(n\) is prime, try the primes up to \(\sqrt{n}\). For 91, \(\sqrt{91} \approx 9.5\), and \(7 \times 13 = 91\), so 91 is not prime.

:::def Highest common factor (HCF)
The largest whole number that divides exactly into each of the given numbers.
:::

:::def Lowest common multiple (LCM)
The smallest positive whole number that each of the given numbers divides into exactly.
:::

:::eg Find the HCF and LCM of 84 and 90.
\(84 = 2^2 \times 3 \times 7\) and \(90 = 2 \times 3^2 \times 5\).

**HCF:** take the primes common to both, each to its **lowest** power: \(2 \times 3 = 6\).

**LCM:** take every prime that appears, each to its **highest** power: \(2^2 \times 3^2 \times 5 \times 7 = 1260\).

Check: \(\text{HCF} \times \text{LCM} = 6 \times 1260 = 7560 = 84 \times 90\). This check works for any two numbers.
:::

The HCF simplifies fractions (\(\tfrac{84}{90} = \tfrac{14}{15}\)) and the LCM gives common denominators. It also solves timing problems: two lights that flash every 12 seconds and every 18 seconds flash together every \(\text{LCM}(12, 18) = 36\) seconds.

:::try Start easy, finish at exam standard
Q: Work out \(8 - 2 \times (5 - 9)^2 + 12 \div 4\).
A: Brackets: \(5 - 9 = -4\). Indices: \((-4)^2 = 16\). Multiplication and division: \(2 \times 16 = 32\) and \(12 \div 4 = 3\). So \(8 - 32 + 3 = -21\).
Q: Work out (a) \(\dfrac23 + \dfrac35\), (b) \(3\tfrac12 \div 1\tfrac34\), (c) \(\dfrac56 \times \dfrac{9}{10}\).

A: (a) \(\dfrac{10}{15} + \dfrac{9}{15} = \dfrac{19}{15} = 1\tfrac{4}{15}\).

(b) \(\dfrac72 \div \dfrac74 = \dfrac72 \times \dfrac47 = \dfrac{4}{2} = 2\).

(c) \(\dfrac{5 \times 9}{6 \times 10} = \dfrac{45}{60} = \dfrac34\).
Q: Show that \(0.7\dot{2} = \dfrac{13}{18}\).
A: Let \(x = 0.7222\ldots\) Then \(100x = 72.222\ldots\) and \(10x = 7.222\ldots\) Subtracting, \(90x = 65\), so \(x = \dfrac{65}{90} = \dfrac{13}{18}\).
Q: (a) Increase 340 by 12.5%. (b) A laptop costs $480 after a 20% reduction. Find its original price.
A: (a) \(340 \times 1.125 = 382.5\).

(b) \(480 \div 0.8 = 600\). The original price was $600.
Q: A car costs $18 000 new and loses 15% of its value each year. Find its value after 3 years, to the nearest dollar.
A: The multiplier is \(0.85\). Value \(= 18\,000 \times 0.85^3 = 11\,054.25\), so the value is $11 054 to the nearest dollar.
Q: (a) Share 360 in the ratio 2 : 3 : 7. (b) Six pumps empty a tank in 10 hours. How long do 4 pumps take?
A: (a) There are 12 parts and \(360 \div 12 = 30\), so the shares are 60, 90 and 210.

(b) Inverse proportion: \(6 \times 10 = 60\) pump-hours, and \(60 \div 4 = 15\) hours.
Q: (a) Round 0.0486 to 2 significant figures. (b) Round 6382.5 to 3 significant figures. (c) Estimate \(\dfrac{38.7 \times 4.92}{0.0987}\) by rounding each number to 1 significant figure.
A: (a) \(0.049\). (b) \(6380\). (c) \(\dfrac{40 \times 5}{0.1} = 2000\) (the exact value is about \(1930\)).
Q: (Exam style) (a) Find the HCF and the LCM of 72 and 108. (b) Hence write \(\dfrac{17}{72} + \dfrac{11}{108}\) as a single fraction.
A: (a) \(72 = 2^3 \times 3^2\) and \(108 = 2^2 \times 3^3\). HCF \(= 2^2 \times 3^2 = 36\). [M1 A1] LCM \(= 2^3 \times 3^3 = 216\). [A1]

(b) The common denominator is the LCM, 216: \(\dfrac{17}{72} = \dfrac{51}{216}\) and \(\dfrac{11}{108} = \dfrac{22}{216}\). [M1] The sum is \(\dfrac{73}{216}\). [A1]
:::

:::quiz
? Which of these numbers is irrational?
- \(\dfrac{22}{7}\)
- \(\sqrt{16}\)
- \(0.\dot{3}\)
+ \(\sqrt{7}\)
> \(\tfrac{22}{7}\) is a fraction, so it is rational (it is only close to \(\pi\)). \(\sqrt{16} = 4\) and \(0.\dot{3} = \tfrac13\) are rational. \(\sqrt{7}\) is not a whole number or a fraction, so it is irrational.
? What is the value of \(-4^2\) by the rules of BIDMAS?
- \(16\)
+ \(-16\)
- \(8\)
- \(-8\)
> The power acts first: \(4^2 = 16\), and then the minus sign applies, giving \(-16\). To get \(16\) you must write \((-4)^2\).
? After an 8% increase a price is $135. What was the price before the increase?
- $124.20
+ $125
- $145.80
- $127
> The multiplier is \(1.08\), so you undo it by dividing: \(135 \div 1.08 = 125\). Taking 8% off \(135\) gives \(124.20\), which is a common wrong answer.
? Round \(0.0070684\) to 3 significant figures.
- \(0.007\)
- \(0.0071\)
+ \(0.00707\)
- \(0.01\)
> The first significant figure is the 7 after the leading zeros. Three significant figures are \(7, 0, 6\), and the next digit is 8, so the 6 rounds up to 7, giving \(0.00707\).
:::

:::recap
- Natural numbers sit inside integers, integers inside rational numbers, and rational plus irrational numbers make the real numbers.
- Follow BIDMAS. Square negative numbers with brackets: \(-3^2 = -9\) but \((-3)^2 = 9\).
- Fractions: add with a common denominator, multiply straight across, divide by flipping the second fraction. Change mixed numbers to improper fractions first.
- Percentage change is the change divided by the **original**. Use multipliers: \(\times 1.15\) for \(+15\%\), \(\times 0.8\) for \(-20\%\), and divide to reverse.
- Ratio and proportion: find the value of one part or one unit first.
- Round to 3 significant figures unless told otherwise; round only at the end; estimate to check.
- HCF uses the lowest powers of common primes; LCM uses the highest powers of all primes.
:::

Next: [Algebra from scratch](#math.f.algebra).
