@chapter math.f.algebra
@title Algebra from scratch
@level pre
@paper Prior knowledge for CAIE 9709 · Edexcel IAL · AQA/OCR/Edexcel (GCSE or IGCSE Algebra)
@time 5–7 hours
@summary Letters as numbers: simplifying, expanding and factorising, algebraic fractions, changing the subject of a formula, linear equations and inequalities, simultaneous equations and substitution.

:::why
Algebra is the language of A Level Mathematics. A formula, a graph, a rate of change and a probability are all written with letters, and every exam question asks you to rearrange them. Quick, accurate algebra matters as much as understanding: a correct method still loses its accuracy marks if a sign or a bracket slips.
:::

**Before you start**, you need the arithmetic in [Numbers, fractions and percentages](#math.f.numbers): fractions, negatives and BIDMAS. The next chapter, [Indices, surds and standard form](#math.f.powers), adds powers to the rules below.

:::try Warm-up
Q: Work out \(\dfrac35 - \dfrac14\). (from [Numbers, fractions and percentages](#math.f.numbers))
A: Use the common denominator 20: \(\dfrac{12}{20} - \dfrac{5}{20} = \dfrac{7}{20}\).
Q: Increase \(\pounds 80\) by \(15\%\). (from [Numbers, fractions and percentages](#math.f.numbers))
A: The multiplier is \(1.15\), so \(80 \times 1.15 = \pounds 92\).
Q: Write \(72\) as a product of prime factors. (from [Numbers, fractions and percentages](#math.f.numbers))
A: \(72 = 8 \times 9 = 2^3 \times 3^2\).
:::

## Letters stand for numbers

A letter in algebra is a number that is unknown or that can change. Every rule of arithmetic still holds, so you can test any algebra rule by replacing the letters with numbers.

:::def Term, expression, equation
A **term** is one piece of an expression, such as \(5x\) or \(-2y^2\), with its sign. An **expression** is terms added or subtracted, such as \(3x^2 - 4x + 7\). An **equation** says two expressions are equal and can be solved, such as \(3x - 5 = 10\). A **formula** is an equation that links quantities, such as \(v = u + at\).
:::

In \(5x\) the number \(5\) is the **coefficient** of \(x\). \(5x\) means \(5 \times x\). Also \(ab\) means \(a \times b\), and \(x^2\) means \(x \times x\). **Like terms** have exactly the same letters and powers, so \(3x^2\) and \(-7x^2\) are like terms, but \(3x^2\) and \(3x\) are not. You can add and subtract only like terms.

:::eg Simplify \(4a + 3b - a + 5b - 2\) and \(3x^2y \times 4xy^3\)
Collect like terms: \(4a - a = 3a\) and \(3b + 5b = 8b\), so the first expression is \(3a + 8b - 2\).

For the product, multiply the numbers and then each letter: \(3 \times 4 = 12\), \(x^2 \times x = x^3\), \(y \times y^3 = y^4\). The answer is \(12x^3y^4\).
:::

:::tip Test with a number
If you are not sure two expressions are equal, put \(x = 10\) (or any simple number) into both. \(\dfrac{x+6}{6}\) and \(x + 1\) are not equal, because at \(x = 12\) they give \(3\) and \(13\). One failed test proves they differ. A passed test is not a proof, but it is a good warning light.
:::

## Expanding brackets

To **expand** a bracket, multiply every term inside by the term outside. The sign travels with the term: \(-3(x - 4) = -3x + 12\).

For two brackets, multiply each term of the first by each term of the second. Then collect like terms.

:::eg Expand and simplify \((x + 3)(x - 5)\), \((2x - 3)(x + 4)\) and \((3x - 2)^2\)
\[\begin{aligned} (x + 3)(x - 5) &= x^2 - 5x + 3x - 15 \\ &= x^2 - 2x - 15 \end{aligned}\]
\[\begin{aligned} (2x - 3)(x + 4) &= 2x^2 + 8x - 3x - 12 \\ &= 2x^2 + 5x - 12 \end{aligned}\]
A squared bracket is two brackets: \((3x - 2)^2 = (3x - 2)(3x - 2)\), so
\[\begin{aligned} (3x - 2)^2 &= 9x^2 - 6x - 6x + 4 \\ &= 9x^2 - 12x + 4 \end{aligned}\]
:::

:::warn \((a + b)^2\) is not \(a^2 + b^2\)
\((a + b)^2 = a^2 + 2ab + b^2\). The middle term \(2ab\) is the one students forget. Test it: \((2 + 3)^2 = 25\), but \(2^2 + 3^2 = 13\). The same rule gives \((a - b)^2 = a^2 - 2ab + b^2\), and \((a + b)(a - b) = a^2 - b^2\), where the middle terms cancel.
:::

With three brackets, expand two of them first, then multiply that result by the third bracket.

:::eg Expand \((x + 1)(x - 2)(x + 4)\)
First, \((x + 1)(x - 2) = x^2 - x - 2\). Then multiply by \((x + 4)\), term by term:
\[\begin{aligned} (x^2 - x - 2)(x + 4) &= x^3 + 4x^2 - x^2 - 4x - 2x - 8 \\ &= x^3 + 3x^2 - 6x - 8 \end{aligned}\]
Check with \(x = 1\): the original gives \(2 \times (-1) \times 5 = -10\), and the answer gives \(1 + 3 - 6 - 8 = -10\).
:::

## Factorising

**Factorising** is the reverse of expanding: write an expression as a product. Always try these in order.

:::steps
1. **Common factor.** Take out the largest number and the highest power of each letter that divides every term: \(12x^2y - 18xy^2 = 6xy(2x - 3y)\).
2. **Difference of two squares.** \(a^2 - b^2 = (a - b)(a + b)\). So \(x^2 - 49 = (x - 7)(x + 7)\) and \(4x^2 - 25 = (2x - 5)(2x + 5)\).
3. **Quadratic \(x^2 + bx + c\).** Find two numbers that multiply to \(c\) and add to \(b\). For \(x^2 + 7x + 12\), the numbers are \(3\) and \(4\), so it is \((x + 3)(x + 4)\).
:::

:::eg Factorise \(x^2 - x - 20\), then \(x^2 - 10x + 24\)
For \(x^2 - x - 20\) the product is \(-20\), so the numbers have opposite signs. The pair \(-5\) and \(4\) add to \(-1\): \((x - 5)(x + 4)\).

For \(x^2 - 10x + 24\) the product is positive and the sum is negative, so both numbers are negative: \(-4\) and \(-6\). The answer is \((x - 4)(x - 6)\).

Always expand back to check: \((x - 5)(x + 4) = x^2 + 4x - 5x - 20\). ✓
:::

Quadratics with \(a \ne 1\) (such as \(6x^2 + 7x - 3\)) and the quadratic formula are in [Quadratics](#math.p1.quadratics).

## Algebraic fractions

Algebraic fractions obey the same rules as number fractions. To **simplify**, factorise the top and the bottom, then cancel **factors**.

:::warn Cancel factors, never terms
In \(\dfrac{x + 6}{6}\) you cannot cancel the 6s, because \(6\) is only part of the top line, joined by a plus sign. You may cancel only things that multiply the whole top and the whole bottom: \(\dfrac{6(x + 1)}{6} = x + 1\).
:::

:::eg Simplify \(\dfrac{x^2 - 9}{x^2 + 5x + 6}\)
Factorise both lines: \(\dfrac{(x - 3)(x + 3)}{(x + 2)(x + 3)}\). The factor \((x + 3)\) appears on top and bottom, so it cancels: \(\dfrac{x - 3}{x + 2}\) (valid for \(x \ne -3\)).
:::

To **add or subtract**, use a common denominator (usually the product of the denominators, or the lowest common multiple if they share a factor). To **multiply**, cancel factors then multiply across. To **divide**, multiply by the reciprocal.

:::eg Write \(\dfrac{2}{x + 1} + \dfrac{3}{x - 2}\) as a single fraction, and simplify \(\dfrac{x^2 - 4}{x + 5} \div \dfrac{x - 2}{3x + 15}\)
The common denominator is \((x + 1)(x - 2)\):
\[\begin{aligned} \frac{2}{x + 1} + \frac{3}{x - 2} &= \frac{2(x - 2) + 3(x + 1)}{(x + 1)(x - 2)} \\ &= \frac{2x - 4 + 3x + 3}{(x + 1)(x - 2)} = \frac{5x - 1}{(x + 1)(x - 2)} \end{aligned}\]
For the division, flip the second fraction and factorise everything:
\[\frac{(x - 2)(x + 2)}{x + 5} \times \frac{3(x + 5)}{x - 2} = 3(x + 2)\]
because \((x - 2)\) and \((x + 5)\) each cancel.
:::

## Linear equations and inequalities

To solve an equation, do the same thing to both sides until \(x\) stands alone. If there are fractions, multiply every term by the common denominator first. If \(x\) is on both sides, collect the \(x\) terms on one side.

:::eg Solve \(\dfrac{2x - 1}{3} + \dfrac{x + 2}{4} = 2\)
Multiply every term by 12, the lowest common denominator:
\[\begin{aligned} 4(2x - 1) + 3(x + 2) &= 24 \\ 8x - 4 + 3x + 6 &= 24 \\ 11x &= 22 \\ x &= 2 \end{aligned}\]
Check: \(\dfrac{3}{3} + \dfrac{4}{4} = 2\). ✓
:::

Many exam questions give the information in words. Choose a letter for the unknown, write each sentence as an equation, then solve it and answer in words.

:::eg A rectangle is \(3\) cm longer than it is wide. Its perimeter is \(34\) cm. Find its length and width.
Let the width be \(w\) cm, so the length is \((w + 3)\) cm. The perimeter is twice the sum of the sides:
\[\begin{aligned} 2\big(w + (w + 3)\big) &= 34 \\ 4w + 6 &= 34 \\ w &= 7 \end{aligned}\]
The width is \(7\) cm and the length is \(10\) cm. Check: \(2(7 + 10) = 34\). ✓
:::

An **inequality** uses \(<\), \(>\), \(\le\) or \(\ge\). You solve it in the same way, with one extra rule.

:::key Inequality rule
Add or subtract anything on both sides: the sign stays. Multiply or divide both sides by a **positive** number: the sign stays. Multiply or divide both sides by a **negative** number: the sign **reverses**. For example \(3 > 1\), but \(-3 < -1\).
:::

:::eg Solve \(5 - 3x > 17\) and \(-2 < 2x + 1 \le 9\)
\[\begin{aligned} 5 - 3x &> 17 \\ -3x &> 12 \\ x &< -4 \end{aligned}\]
Dividing by \(-3\) reversed the sign. For the double inequality, do the same to all three parts: subtract 1 to get \(-3 < 2x \le 8\), then divide by 2 to get \(-1.5 < x \le 4\).
Check the first with \(x = -5\): \(5 + 15 = 20 > 17\). ✓
:::

## Simultaneous equations

Two unknowns need two equations. There are two methods; use whichever is shorter.

:::cols
:::col Elimination
Make the coefficient of one letter the same in both equations, then add or subtract to remove it. Best when both equations look like \(ax + by = c\).
:::
:::col Substitution
Rearrange one equation to get one letter alone, then replace it in the other equation. Best when one letter already has coefficient 1. It is the only method for a linear equation with a quadratic.
:::
:::

:::eg Solve (a) \(3x + 2y = 12\), \(5x - 2y = 4\) and (b) \(2x + 3y = 13\), \(4x - y = 5\)
(a) The \(y\) coefficients are \(+2\) and \(-2\), so add the equations: \(8x = 16\), giving \(x = 2\). Substitute into the first: \(6 + 2y = 12\), so \(y = 3\). Check in the second: \(10 - 6 = 4\). ✓

(b) From the second equation \(y = 4x - 5\). Substitute into the first:
\[\begin{aligned} 2x + 3(4x - 5) &= 13 \\ 14x - 15 &= 13 \\ x &= 2, \quad y = 3 \end{aligned}\]
:::

## Substitution and changing the subject

To **substitute** into a formula, replace each letter by its value, using brackets around every negative number.

:::eg Use \(s = ut + \tfrac12 at^2\) to find \(s\) when \(u = -2\), \(a = 3\) and \(t = 5\)
\[s = (-2)(5) + \tfrac12(3)(5)^2 = -10 + 37.5 = 27.5\]
:::

The **subject** of a formula is the letter on its own on one side, such as \(v\) in \(v = u + at\). To change the subject, undo operations in the reverse order, doing the same to both sides. For example, to make \(t\) the subject of \(s = ut + \tfrac12 at^2\) you would need the quadratic formula, but to make \(a\) the subject you undo step by step: \(2(s - ut) = at^2\), so \(a = \dfrac{2(s - ut)}{t^2}\). If the new subject appears twice, collect all the terms that contain it on one side, **factorise**, then divide.

:::eg (Exam style) Make \(x\) the subject of \(y = \dfrac{2x + 1}{x - 3}\).
Multiply both sides by \((x - 3)\) to remove the fraction:
\[y(x - 3) = 2x + 1\] [M1]
Expand: \(yx - 3y = 2x + 1\). Collect the \(x\) terms on one side and everything else on the other:
\[yx - 2x = 1 + 3y\] [M1]
Factorise the left side to bring \(x\) out once:
\[x(y - 2) = 1 + 3y\] [M1]
\[x = \frac{3y + 1}{y - 2}\] [A1]
Check with \(x = 4\): \(y = \dfrac{9}{1} = 9\). The answer gives \(\dfrac{28}{7} = 4\). ✓
:::

:::exam Showing algebra for method marks
"Show that" and "make \(x\) the subject" questions award a method mark for each valid step, so write one change per line. If the mark scheme says "factorise", the step with the bracket is the mark: do not jump from \(yx - 2x = 1 + 3y\) straight to the answer. Check numerically on scrap paper if you have time.
:::

:::eg Spot the error: solve the inequality \(3(x - 2) \geq 5x + 4\).
The question is worth 3 marks. A student wrote this answer.

Line 1: \(3x - 6 \geq 5x + 4\)
Line 2: \(-2x \geq 10\)
Line 3: \(x \geq -5\)

Lines 1 and 2 are correct: the bracket is expanded, and the \(x\) terms and numbers are collected [M1] [A1]. **Line 3 is wrong.** Dividing both sides by \(-2\) reverses the inequality, so \(\geq\) must become \(\leq\). The final accuracy mark is lost [A0], and the student scores 2 out of 3.

Correct line 3: \(x \leq -5\). [A1]

Check with numbers. Test \(x = -6\), which is in the correct answer: the left side is \(3(-8) = -24\) and the right side is \(5(-6) + 4 = -26\), and \(-24 \geq -26\) is true. Now test \(x = 0\), which is in the student's answer: the left side is \(-6\) and the right side is \(4\), and \(-6 \geq 4\) is false. A one-minute check of a value from each side of the boundary catches the slip.
:::

:::try Start easy, finish at exam standard
Q: Simplify \(4(2x - 3) - 3(x - 5)\).
A: \(8x - 12 - 3x + 15 = 5x + 3\).
Q: Expand and simplify (a) \((2x - 3)(x + 5)\), (b) \((x - 4)^2\), (c) \((x - 1)(x + 2)(x - 3)\).
A: (a) \(2x^2 + 10x - 3x - 15 = 2x^2 + 7x - 15\).

(b) \(x^2 - 8x + 16\).

(c) \((x - 1)(x + 2) = x^2 + x - 2\), then
\[\begin{aligned} (x^2 + x - 2)(x - 3) &= x^3 - 3x^2 + x^2 - 3x - 2x + 6 \\ &= x^3 - 2x^2 - 5x + 6 \end{aligned}\]
Q: Factorise (a) \(15x^2 - 10x\), (b) \(4x^2 - 25\), (c) \(x^2 - 3x - 28\).
A: (a) \(5x(3x - 2)\). (b) \((2x - 5)(2x + 5)\). (c) Numbers with product \(-28\) and sum \(-3\) are \(-7\) and \(4\): \((x - 7)(x + 4)\).
Q: Simplify \(\dfrac{x^2 - x - 12}{x^2 - 16}\).
A: \(\dfrac{(x - 4)(x + 3)}{(x - 4)(x + 4)} = \dfrac{x + 3}{x + 4}\).
Q: Write \(\dfrac{1}{x + 2} - \dfrac{1}{x + 5}\) as a single fraction.
A: \(\dfrac{(x + 5) - (x + 2)}{(x + 2)(x + 5)} = \dfrac{3}{(x + 2)(x + 5)}\).
Q: Solve (a) \(3(2x - 1) = 5x + 4\), (b) \(7 - 2x \le 15\).
A: (a) \(6x - 3 = 5x + 4\), so \(x = 7\).

(b) \(-2x \le 8\), and dividing by \(-2\) reverses the sign: \(x \ge -4\).
Q: Solve the simultaneous equations \(3x - 2y = 11\), \(x + 4y = 6\).
A: From the second, \(x = 6 - 4y\). Then \(3(6 - 4y) - 2y = 11\), so \(18 - 14y = 11\) and \(y = \tfrac12\). Then \(x = 6 - 2 = 4\). Check: \(12 - 1 = 11\). ✓
Q: (Exam style) Make \(t\) the subject of \(v = \dfrac{3t}{t + 2}\).
A: \(v(t + 2) = 3t\). [M1] So \(vt + 2v = 3t\) and \(2v = 3t - vt\). [M1] Factorise: \(2v = t(3 - v)\). [M1] So \(t = \dfrac{2v}{3 - v}\). [A1]
:::

:::try Exam practice ★ to ★★★
Q: [5 marks] ★ (a) Factorise fully \(6x^2y - 9xy^2\). (b) Expand and simplify \((2x - 3)(x + 4) - (x - 1)^2\).
A: (a) The common factor is \(3xy\): \(6x^2y - 9xy^2 = 3xy(2x - 3y)\). [M1 A1] (b) \((2x - 3)(x + 4) = 2x^2 + 5x - 12\). [M1] \((x - 1)^2 = x^2 - 2x + 1\), and this whole bracket is subtracted: \(2x^2 + 5x - 12 - x^2 + 2x - 1\). [M1] \(= x^2 + 7x - 13\). [A1]
Q: [3 marks] ★ The volume of a cone is \(V = \tfrac13\pi r^2 h\). Make \(r\) the subject of the formula.
A: Multiply by 3: \(3V = \pi r^2 h\). [M1] Divide by \(\pi h\): \(r^2 = \dfrac{3V}{\pi h}\). [M1] Take the square root: \(r = \sqrt{\dfrac{3V}{\pi h}}\). [A1]
Q: [4 marks] ★★ Solve \(\dfrac{3x - 1}{4} - \dfrac{x + 2}{3} = 1\).
A: Multiply every term by 12: \(3(3x - 1) - 4(x + 2) = 12\). [M1] Expand: \(9x - 3 - 4x - 8 = 12\). [M1] So \(5x = 23\) [A1] and \(x = 4.6\). [A1] Check: \(\dfrac{3(4.6) - 1}{4} = 3.2\) and \(\dfrac{4.6 + 2}{3} = 2.2\); the difference is \(1\). ✓
Q: [4 marks] ★★ Solve the simultaneous equations \(3x + 2y = 4\) and \(5x - 3y = 13\).
A: Multiply the first by 3 and the second by 2 to match the \(y\) coefficients: \(9x + 6y = 12\) and \(10x - 6y = 26\). [M1] Add: \(19x = 38\), so \(x = 2\). [A1 A1] Substitute: \(6 + 2y = 4\), so \(y = -1\). [A1] Check in the second equation: \(10 + 3 = 13\). ✓
Q: [4 marks] ★★ Simplify \(\dfrac{2x^2 + x - 6}{x^2 - 4}\).
A: Factorise the numerator: \((2x - 3)(x + 2)\). [B1] Factorise the denominator (difference of two squares): \((x - 2)(x + 2)\). [B1] Cancel the common factor \((x + 2)\): [M1] \(\dfrac{2x - 3}{x - 2}\). [A1]
Q: [3 marks] ★★ Show that the sum of the squares of any two consecutive integers is always odd.
A: Let the integers be \(n\) and \(n + 1\). The sum of squares is
\[\begin{aligned} n^2 + (n + 1)^2 &= n^2 + n^2 + 2n + 1 \\ &= 2n^2 + 2n + 1 \end{aligned}\] [M1 A1]
This equals \(2(n^2 + n) + 1\), which is one more than a multiple of \(2\), so it is odd. [B1]
Q: [4 marks] (#math.f.numbers) ★★★ The numbers of boys and girls in a club are in the ratio \(3 : 2\). When \(6\) boys leave and \(4\) girls join, the numbers of boys and girls are equal. How many members did the club have at the start?
H: Write the numbers of boys and girls as \(3k\) and \(2k\).
H: Use the sentence about equal numbers to write an equation in \(k\).
A: Boys \(= 3k\) and girls \(= 2k\). [M1] After the change they are equal: \(3k - 6 = 2k + 4\). [M1] So \(k = 10\) [A1] and the club had \(3k + 2k = 50\) members. [A1] Check: \(30 - 6 = 24 = 20 + 4\). ✓
Q: [7 marks] ★★★ A rectangular garden has a perimeter of \(40\) m and an area of \(91\) m². (a) Show that the width \(w\) m satisfies \(w^2 - 20w + 91 = 0\). (b) Find the length and width of the garden. (c) A path \(1\) m wide goes all the way round the outside of the garden. Find the area of the path.
H: If the perimeter is 40, then length plus width is 20. So the length is \(20 - w\).
H: Write the area as \(w(20 - w)\) and set it equal to \(91\).
H: For (c), the garden plus the path is a larger rectangle. How much longer and wider is it?
A: (a) Length \(+\) width \(= 20\), so the length is \((20 - w)\). [B1] The area gives \(w(20 - w) = 91\) [M1], so \(20w - w^2 = 91\) and \(w^2 - 20w + 91 = 0\). [A1] (b) \((w - 7)(w - 13) = 0\) [M1] so the sides are \(7\) m and \(13\) m. [A1] (c) The path adds \(1\) m on each side, so the outer rectangle is \(15\) m by \(9\) m with area \(135\) m². [M1] The path has area \(135 - 91 = 44\) m². [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Given that \(x + \dfrac1x = 5\), find (a) the value of \(x^2 + \dfrac{1}{x^2}\), (b) the value of \(x^3 + \dfrac{1}{x^3}\).
H: Square both sides of \(x + \dfrac1x = 5\). What does the middle term of the expansion become?
H: For (b), expand \(\left(x + \dfrac1x\right)^3\). The two middle terms are both multiples of \(x + \dfrac1x\).
A: (a) \(\left(x + \dfrac1x\right)^2 = x^2 + 2 + \dfrac{1}{x^2}\) [M1], so \(25 = x^2 + 2 + \dfrac{1}{x^2}\) and \(x^2 + \dfrac1{x^2} = 23\). [A1] (b)
\[\begin{aligned} \left(x + \dfrac1x\right)^3 &= x^3 + 3x + \dfrac3x + \dfrac1{x^3} \\ &= x^3 + \dfrac{1}{x^3} + 3\left(x + \dfrac1x\right) \end{aligned}\] [M1]
So \(125 = x^3 + \dfrac1{x^3} + 15\) [M1], giving \(x^3 + \dfrac1{x^3} = 110\). [A1] Check: \(x = \dfrac{5 + \sqrt{21}}{2} = 4.791\); then \(x^3 = 109.98\) and \(\dfrac{1}{x^3} = 0.009\), which add to \(110\).
Q: [5 marks] ★★★ Find the values of \(k\) for which the simultaneous equations \(kx + 3y = 6\) and \(4x + (k + 1)y = 9\) have no solution.
H: Eliminate \(y\): multiply the first equation by \((k + 1)\) and the second by 3, then subtract.
H: You get an equation of the form (something)\(\,x =\) (something). When can it have no solution?
H: It has none when the coefficient of \(x\) is zero but the right-hand side is not. Check that second condition for each value of \(k\).
A: Multiply the first by \((k + 1)\) and the second by 3: \(k(k + 1)x + 3(k + 1)y = 6(k + 1)\) and \(12x + 3(k + 1)y = 27\). Subtract: \((k^2 + k - 12)x = 6k - 21\). [M1 A1] There is no solution when the coefficient of \(x\) is zero but the right-hand side is not. [M1] \(k^2 + k - 12 = (k + 4)(k - 3) = 0\), so \(k = 3\) or \(k = -4\). [A1] For \(k = 3\) the right-hand side is \(-3\), and for \(k = -4\) it is \(-45\); neither is zero, so both values give no solution. [A1] Meaning: the two lines are parallel but different.
:::

:::quiz
? Expand \((x + 3)^2\).
- \(x^2 + 9\)
- \(x^2 + 3x + 9\)
+ \(x^2 + 6x + 9\)
- \(x^2 + 6\)
> A squared bracket is two brackets: \(x^2 + 3x + 3x + 9\). The middle term \(6x\) is the one that goes missing in \(x^2 + 9\).
? Which of these is a correct simplification?
- \(\dfrac{x + 6}{6} = x + 1\)
+ \(\dfrac{6x + 6}{6} = x + 1\)
- \(\dfrac{x^2 + 4}{x + 4} = x\)
- \(\dfrac{3 + x}{3 + y} = \dfrac{x}{y}\)
> Only a factor of the whole top line can cancel. In \(\tfrac{6x + 6}{6}\) the top is \(6(x + 1)\), so the 6 is a factor. In the other options the cancelled number or term is only part of a sum.
? Solve \(-2x > 6\).
- \(x > -3\)
+ \(x < -3\)
- \(x > 3\)
- \(x < 3\)
> Dividing by \(-2\) reverses the inequality, so \(x < -3\). Forgetting to reverse gives \(x > -3\).
? Make \(x\) the subject of \(y = \dfrac{x + 1}{x - 1}\).
- \(x = y - 2\)
- \(x = \dfrac{y - 1}{y + 1}\)
+ \(x = \dfrac{y + 1}{y - 1}\)
- \(x = \dfrac{y}{y - 1}\)
> \(y(x - 1) = x + 1\), so \(yx - x = y + 1\) and \(x(y - 1) = y + 1\). The answer has the same form as the original, which is a feature of this formula. The option \(\tfrac{y - 1}{y + 1}\) is the reciprocal, which comes from dividing by the wrong bracket. The option \(y - 2\) comes from treating the fraction as if it had no denominator.
? Solve \(-3x < 12\).
- \(x < -4\)
+ \(x > -4\)
- \(x < 4\)
- \(x > 4\)
> Dividing both sides by \(-3\) reverses the inequality, so \(x > -4\). The option \(x < -4\) divides correctly but keeps the sign. The options with \(4\) lose the minus sign.
:::

:::checklist What you can now do
- [ ] I can simplify expressions, expand single and double brackets, and factorise common factors, differences of two squares and quadratics \(x^2 + bx + c\).
- [ ] I can add, simplify and divide algebraic fractions.
- [ ] I can solve linear equations, including ones with fractions, and linear inequalities (reversing the sign when I multiply or divide by a negative).
- [ ] I can solve a pair of simultaneous equations by elimination or by substitution.
- [ ] I can change the subject of a formula, including when the subject is squared.
- [ ] I can turn a worded problem into an equation and check my answer in the original problem.
:::

:::recap
- A letter is a number: test any rule by putting numbers in.
- Collect like terms only. Expand every term in a bracket, and \((a + b)^2 = a^2 + 2ab + b^2\).
- Factorise in order: common factor, difference of two squares, then the quadratic with sum and product.
- Cancel factors, never terms. Add algebraic fractions over a common denominator.
- Multiply or divide an inequality by a negative number and the sign reverses.
- Simultaneous equations: eliminate one letter, or substitute. When the new subject appears twice, collect, factorise, divide.
:::

:::links
- watch: [Expanding two brackets](https://www.examsolutions.net/tutorials/expanding-two-brackets/) · ExamSolutions · short video with examples
- watch: [Linear inequalities](https://www.examsolutions.net/tutorials/linear-inequalities/) · ExamSolutions · why the sign flips when you divide by a negative
- practise: [Algebra 1](https://www.khanacademy.org/math/algebra) · Khan Academy · mastery practice with instant feedback
- explore: [Area Model Algebra](https://phet.colorado.edu/en/simulations/area-model-algebra) · PhET · see why brackets expand the way they do
- explore: [Thinking about Algebra](https://undergroundmathematics.org/thinking-about-algebra) · Underground Mathematics · problems that build fluency and insight
- read: [Algebra notes](https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx) · Paul's Online Notes · clear notes with many worked examples

Links checked 3 October 2026.
:::
Next: [Indices, surds and standard form](#math.f.powers).
