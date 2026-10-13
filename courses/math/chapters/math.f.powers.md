@chapter math.f.powers
@title Indices, surds and standard form
@level pre
@paper Prior knowledge for CAIE 9709 · Edexcel IAL · AQA/OCR/Edexcel (GCSE or IGCSE Number and Algebra)
@time 5–6 hours
@summary The laws of indices with positive, zero, negative and fractional powers; simplifying, adding and multiplying surds and rationalising denominators; calculations in standard form.

:::why
Powers and roots are in every part of A Level. Differentiating \(\dfrac{3}{\sqrt{x}}\) needs you to write it as \(3x^{-1/2}\). The quadratic formula, circles, trigonometry and the normal distribution produce square roots that you must leave in exact form. Exponential growth, logarithms and the Poisson distribution all rest on the index laws. If you master this chapter, a whole class of "exact value" and "simplify" questions becomes routine.
:::

**Before you start**, you need [Algebra from scratch](#math.f.algebra) (expanding brackets and factorising). The next chapter, [Graphs and straight lines](#math.f.graphs), uses indices to name curve shapes.

:::try Warm-up
Q: Write \(90\) as a product of prime factors. (from [Numbers, fractions and percentages](#math.f.numbers))
A: \(90 = 2 \times 45 = 2 \times 3 \times 15 = 2 \times 3^2 \times 5\).
Q: Expand and simplify \((x + 3)(x - 3)\). (from [Algebra from scratch](#math.f.algebra))
A: \(x^2 - 3x + 3x - 9 = x^2 - 9\).
Q: Make \(x\) the subject of \(y = 3x - 5\). (from [Algebra from scratch](#math.f.algebra))
A: \(y + 5 = 3x\), so \(x = \dfrac{y + 5}{3}\).
:::

## Indices and their laws

\(a^n\) means \(a\) multiplied by itself \(n\) times. The number \(a\) is the **base** and \(n\) is the **index** (also called the power or exponent). So \(2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32\). The plural of index is **indices**.

The laws follow from counting factors. \(a^3 \times a^4 = (a \times a \times a)(a \times a \times a \times a) = a^7\): there are \(3 + 4\) factors of \(a\) altogether.

:::key The laws of indices
For any base \(a \ne 0\) and indices \(m\) and \(n\):
- \(a^m \times a^n = a^{m+n}\)
- \(a^m \div a^n = a^{m-n}\)
- \((a^m)^n = a^{mn}\)
- \((ab)^n = a^n b^n\) and \(\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}\)
- \(a^0 = 1\)
- \(a^{-n} = \dfrac{1}{a^n}\)
- \(a^{1/n} = \sqrt[n]{a}\) and \(a^{m/n} = \left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}\)
:::

The laws for products and quotients work only when the **bases are the same**. \(2^3 \times 3^2\) cannot be combined. Here is why the less obvious ones are true:

- **Zero index.** \(a^3 \div a^3 = 1\), and by the subtraction law it equals \(a^{3-3} = a^0\). So \(a^0 = 1\).
- **Negative index.** \(a^0 \div a^3 = a^{-3}\), and also \(\dfrac{1}{a^3}\). So a negative index means "one over". It does **not** make the number negative: \(2^{-3} = \dfrac18\).
- **Fractional index.** \(a^{1/2} \times a^{1/2} = a^1\), so \(a^{1/2}\) is the number which squares to \(a\), the square root. In the same way, \(a^{1/3}\) is the cube root.

:::proof Why the index laws work
For positive whole numbers \(m\) and \(n\), \(a^m\) means \(m\) copies of \(a\) multiplied together.

- **Multiplying.** \(a^m \times a^n\) is \(m\) copies of \(a\) followed by \(n\) more copies. That is \(m + n\) copies, so it equals \(a^{m+n}\).
- **Dividing** (with \(m > n\)). \(a^m \div a^n\) is \(m\) copies of \(a\) over \(n\) copies of \(a\). Cancel \(n\) copies from top and bottom and \(m - n\) copies are left: \(a^{m-n}\).
- **Power of a power.** \((a^m)^n\) is \(n\) groups of \(m\) copies of \(a\). That is \(mn\) copies: \(a^{mn}\).
- **Power of a product.** \((ab)^n = (ab)(ab)\cdots(ab)\). Rearrange the factors into \(n\) copies of \(a\) and \(n\) copies of \(b\): \(a^n b^n\).

These proofs work for whole-number indices. The other indices are then **defined** so that the laws keep working:

- If \(a^n \div a^n = a^{n-n} = a^0\) is to follow the division law, and \(a^n \div a^n = 1\), then \(a^0 = 1\).
- If \(a^{-n} \times a^n = a^{-n+n} = a^0 = 1\) is to follow the multiplication law, then \(a^{-n}\) must be the reciprocal \(\dfrac{1}{a^n}\).
- If \(\left(a^{1/n}\right)^n = a^{\frac1n \times n} = a\) is to follow the power law, then \(a^{1/n}\) is the number whose \(n\)th power is \(a\): the \(n\)th root.

Finally \(a^{m/n} = \left(a^{1/n}\right)^m\) by the power law again. This shows that the laws are not a list to memorise: they are one idea, counting factors, extended carefully.
:::

:::eg Evaluate (a) \(25^{1/2}\), (b) \(8^{2/3}\), (c) \(16^{-3/4}\), (d) \(\left(\dfrac{4}{9}\right)^{-1/2}\)
(a) \(25^{1/2} = \sqrt{25} = 5\).

(b) Take the root first, because it keeps the numbers small: \(8^{2/3} = \left(\sqrt[3]{8}\right)^2 = 2^2 = 4\).

(c) Handle the minus sign by flipping to a reciprocal, then the fraction: \(16^{-3/4} = \dfrac{1}{16^{3/4}} = \dfrac{1}{\left(\sqrt[4]{16}\right)^3} = \dfrac{1}{2^3} = \dfrac18\).

(d) A negative power flips the fraction: \(\left(\dfrac49\right)^{-1/2} = \left(\dfrac94\right)^{1/2} = \dfrac32\).
:::

:::eg Simplify \(\dfrac{(2x^3)^2 \times 3x^{-1}}{6x^4}\) and write \(\dfrac{5}{\sqrt{x}}\) and \(\dfrac{2}{3x^2}\) as powers of \(x\)
Work on the number and on each letter separately:
\[\frac{(2x^3)^2 \times 3x^{-1}}{6x^4} = \frac{4x^6 \times 3x^{-1}}{6x^4} = \frac{12x^5}{6x^4} = 2x\]
For the other two: \(\dfrac{5}{\sqrt{x}} = \dfrac{5}{x^{1/2}} = 5x^{-1/2}\) and \(\dfrac{2}{3x^2} = \dfrac23 x^{-2}\). Only \(x\) is in the denominator, so only \(x\) gets the negative index: the 3 stays below as \(\tfrac23\).
:::

:::tip Why this matters for calculus
The rules for differentiating and integrating are written for powers \(x^n\). Before you differentiate \(\dfrac{3}{\sqrt{x}}\) or integrate \(\sqrt[3]{x}\), write it as a power: \(3x^{-1/2}\) and \(x^{1/3}\). See [Differentiation](#math.p1.diff) and [Integration](#math.p1.integ).
:::

:::warn Common slips with indices
- \(2^{-3}\) is \(\tfrac18\), not \(-8\) and not \(-6\).
- \(\dfrac{1}{2x^{-1}}\) is \(\dfrac{x}{2}\): the index \(-1\) belongs to \(x\) only. 
- \(a^m + a^n\) does not simplify, and \((a + b)^2 \ne a^2 + b^2\).
- \(4^{1/2}\) is \(2\), not \(\tfrac14\) and not \(8\).
:::

An **equation with an unknown index** can often be solved by writing both sides with the same base: if \(2^x = 32\) then \(2^x = 2^5\), so \(x = 5\).

:::eg Solve \(9^{x} = 27\)
Write both sides as powers of 3: \((3^2)^x = 3^3\), so \(3^{2x} = 3^3\). The bases match, so the indices are equal: \(2x = 3\) and \(x = 1.5\). Check: \(9^{1.5} = 3^3 = 27\). ✓
:::

## Surds

A square root of a non-square whole number such as \(\sqrt{2}\), \(\sqrt{3}\) or \(\sqrt{7}\) is irrational: its decimal never ends. Written as a root, it is exact. A calculator's decimal is only an approximation.

:::def Surd
An irrational number that is a root of a rational number, such as \(\sqrt{5}\) or \(3 + \sqrt{2}\). An exact answer leaves the surd in the answer instead of using a rounded decimal.
:::

Two rules do almost everything.

:::key Rules for surds
For \(a, b \ge 0\): \(\sqrt{ab} = \sqrt{a}\,\sqrt{b}\) and \(\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}}\). Also \(\sqrt{a}\,\sqrt{a} = a\). 

There is **no** rule for sums: \(\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}\). Check: \(\sqrt{9 + 16} = 5\), but \(\sqrt{9} + \sqrt{16} = 7\).
:::

:::proof \(\sqrt2\) is irrational
This is a **proof by contradiction**: assume the opposite, and show that it leads to nonsense.

Suppose \(\sqrt2\) is rational. Then \(\sqrt2 = \dfrac pq\), where \(p\) and \(q\) are whole numbers with no common factor (any fraction can be cancelled to lowest terms).
Square both sides: \(2 = \dfrac{p^2}{q^2}\), so \(p^2 = 2q^2\).
That makes \(p^2\) even. An odd number squared is odd, so \(p\) itself must be even. Write \(p = 2r\).
Substitute: \((2r)^2 = 2q^2\), so \(4r^2 = 2q^2\) and \(q^2 = 2r^2\).
That makes \(q^2\) even, so \(q\) is even too.
Now \(p\) and \(q\) are both even, so they share the factor \(2\). That contradicts "no common factor".
The assumption led to a contradiction, so it is false: \(\sqrt2\) cannot be written as a fraction. It is irrational. The same idea, with "divisible by 3" in place of "even", shows that \(\sqrt3\) is irrational too.
:::

To **simplify** a surd, find the biggest square number that divides the number under the root. Square numbers to know: \(4, 9, 16, 25, 36, 49, 64, 81, 100\).

You can add and subtract only **like surds** (the same surd), the way you add like terms: \(3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}\). Different surds may become alike after simplifying.

:::eg Simplify (a) \(\sqrt{72}\), (b) \(\sqrt{50} + \sqrt{18} - \sqrt{8}\), (c) \(\sqrt{6} \times \sqrt{15}\)
(a) \(72 = 36 \times 2\), so \(\sqrt{72} = 6\sqrt{2}\).

(b) Simplify each: \(\sqrt{50} = 5\sqrt2\), \(\sqrt{18} = 3\sqrt2\), \(\sqrt{8} = 2\sqrt2\). Now they are alike: \(5\sqrt2 + 3\sqrt2 - 2\sqrt2 = 6\sqrt2\).

(c) \(\sqrt{6} \times \sqrt{15} = \sqrt{90} = \sqrt{9 \times 10} = 3\sqrt{10}\).
:::

To expand brackets that contain surds, multiply term by term as in algebra, remembering \(\sqrt{a}\,\sqrt{a} = a\).

:::eg Expand and simplify \((3 + \sqrt{5})(2 - \sqrt{5})\) and \((2 + \sqrt{3})^2\)
\[\begin{aligned} (3 + \sqrt5)(2 - \sqrt5) &= 6 - 3\sqrt5 + 2\sqrt5 - 5 \\ &= 1 - \sqrt5 \end{aligned}\]
\[\begin{aligned} (2 + \sqrt3)^2 &= 4 + 2\sqrt3 + 2\sqrt3 + 3 \\ &= 7 + 4\sqrt3 \end{aligned}\]
:::

## Rationalising the denominator

A fraction such as \(\dfrac{1}{\sqrt{2}}\) is easier to use if the denominator is a whole number. **Rationalising** removes the surd from the denominator by multiplying top and bottom by the same thing. It does not change the value, because you multiply by 1.

- **One surd:** multiply by that surd. \(\dfrac{6}{\sqrt{3}} = \dfrac{6\sqrt3}{\sqrt3\,\sqrt3} = \dfrac{6\sqrt3}{3} = 2\sqrt3\).
- **A sum or difference with a surd:** multiply by the **conjugate**, the same two terms with the opposite sign in the middle. The product \((a + \sqrt b)(a - \sqrt b) = a^2 - b\) has no surd, because it is a difference of two squares.

:::eg (Exam style) Express \(\dfrac{4}{3 - \sqrt{5}}\) in the form \(a + b\sqrt{5}\), where \(a\) and \(b\) are rational.
Multiply top and bottom by the conjugate \(3 + \sqrt5\):
\[\frac{4}{3 - \sqrt5} \times \frac{3 + \sqrt5}{3 + \sqrt5} = \frac{4(3 + \sqrt5)}{9 - 5}\] [M1]
The denominator is \((3 - \sqrt5)(3 + \sqrt5) = 9 - 5 = 4\). [A1]
\[= \frac{4(3 + \sqrt5)}{4} = 3 + \sqrt5\] [A1]
So \(a = 3\) and \(b = 1\). Check: \(\dfrac{4}{3 - 2.236} = 5.236\) and \(3 + 2.236 = 5.236\). ✓
:::

:::eg (Exam style) Show that \(\dfrac{\sqrt{3} + 1}{\sqrt{3} - 1}\) can be written as \(2 + \sqrt{3}\).
Multiply top and bottom by \(\sqrt3 + 1\):
\[\frac{(\sqrt3 + 1)(\sqrt3 + 1)}{(\sqrt3 - 1)(\sqrt3 + 1)} = \frac{3 + 2\sqrt3 + 1}{3 - 1}\] [M1 A1]
\[= \frac{4 + 2\sqrt3}{2} = 2 + \sqrt3\] [A1]
Dividing the top by 2 divides **both** terms. 
:::

:::exam Exact values and "show that"
"Exact" means no calculator decimal in the answer. A "show that" question gives the answer, so every line of working must be there: the conjugate, the expanded numerator, and the denominator that becomes a whole number. Using the calculator decimal as the proof earns nothing.
:::

## Standard form

:::def Standard form
A number written as \(a \times 10^n\), where \(1 \le a < 10\) and \(n\) is an integer. Standard form is used for very large and very small numbers.
:::

Count how many places the decimal point moves. \(45\,000 = 4.5 \times 10^4\) (moved 4 places left, so the index is \(+4\)). \(0.00032 = 3.2 \times 10^{-4}\) (moved 4 places right, so the index is \(-4\)).

To multiply or divide, handle the numbers and the powers of 10 separately, using the index laws. If the number part leaves the range 1 to 10, adjust.

:::eg Work out (a) \((3 \times 10^5)(4 \times 10^7)\), (b) \(\dfrac{6 \times 10^{-3}}{1.5 \times 10^{5}}\), (c) \((2.4 \times 10^6) + (3 \times 10^5)\)
(a) \(3 \times 4 = 12\) and \(10^5 \times 10^7 = 10^{12}\), so the product is \(12 \times 10^{12} = 1.2 \times 10^{13}\).

(b) \(6 \div 1.5 = 4\) and \(10^{-3} \div 10^{5} = 10^{-8}\), so the answer is \(4 \times 10^{-8}\).

(c) Write both with the same power of 10 before adding: \(2.4 \times 10^6 + 0.3 \times 10^6 = 2.7 \times 10^6\).
:::

:::tip Standard form on the calculator
Use the \(\times 10^x\) or EXP key, not "\(\times 10\) then \(\wedge\)". Typing \(3\) EXP \(5\) enters \(3 \times 10^5\). Typing \(3 \times 10^{-4}\) with the power in brackets is also safe. In Cambridge answers, \(3.2\mathrm{E}{-4}\) on the screen should be copied as \(3.2 \times 10^{-4}\).
:::

:::eg Spot the error: express \((4 + \sqrt3)^2\) in the form \(a + b\sqrt3\), where \(a\) and \(b\) are integers.
The question is worth 2 marks. A student wrote this answer.

Line 1: \((4 + \sqrt3)^2 = 4^2 + (\sqrt3)^2\)
Line 2: \(= 16 + 3 = 19\)

**Line 1 is wrong.** The student squared each term separately, which leaves out the middle terms. Squaring a bracket means multiplying it by itself, so there are four products, not two. This is a wrong method, not a slip in arithmetic, so the method mark is lost [M0] and the answer cannot earn its accuracy mark [A0]. The student scores 0 out of 2.

Correct working: \((4 + \sqrt3)(4 + \sqrt3) = 16 + 4\sqrt3 + 4\sqrt3 + 3\) [M1] \(= 19 + 8\sqrt3\). [A1]

Check with decimals: \(4 + \sqrt3 = 5.732\) and \(5.732^2 = 32.86\). The correct answer gives \(19 + 8(1.732) = 32.86\). The student's \(19\) is nowhere near, and the check takes ten seconds.
:::

:::try Start easy, finish at exam standard
Q: Evaluate (a) \(3^{-2}\), (b) \(81^{3/4}\), (c) \(\left(\dfrac{27}{8}\right)^{-2/3}\).
A: (a) \(\dfrac19\). (b) \(\left(\sqrt[4]{81}\right)^3 = 3^3 = 27\). (c) \(\left(\dfrac{8}{27}\right)^{2/3} = \left(\dfrac23\right)^2 = \dfrac49\).
Q: Simplify \(\dfrac{(3x^2y)^3}{9x^4y}\).
A: \(\dfrac{27x^6y^3}{9x^4y} = 3x^2y^2\).
Q: Write as a single power of \(x\) (a) \(\dfrac{4}{x^3}\) times \(x^{1/2}\), (b) \(\dfrac{1}{\sqrt[3]{x}}\).
A: (a) \(4x^{-3} \times x^{1/2} = 4x^{-5/2}\). (b) \(x^{-1/3}\).
Q: Solve (a) \(4^{x} = 64\), (b) \(8^{x} = 4\).
A: (a) \(4^x = 4^3\), so \(x = 3\). (b) \(2^{3x} = 2^2\), so \(3x = 2\) and \(x = \tfrac23\).
Q: Simplify (a) \(\sqrt{108}\), (b) \(\sqrt{45} + \sqrt{80}\), (c) \(\sqrt{12} \times \sqrt{27}\).
A: (a) \(\sqrt{36 \times 3} = 6\sqrt3\). (b) \(3\sqrt5 + 4\sqrt5 = 7\sqrt5\). (c) \(\sqrt{324} = 18\), or \(2\sqrt3 \times 3\sqrt3 = 6 \times 3 = 18\).
Q: Expand and simplify \((4 - \sqrt{3})(1 + 2\sqrt{3})\).
A: \(4 + 8\sqrt3 - \sqrt3 - 2 \times 3 = -2 + 7\sqrt3\).
Q: Rationalise the denominator of (a) \(\dfrac{10}{\sqrt{5}}\), (b) \(\dfrac{6}{4 + \sqrt{7}}\).
A: (a) \(\dfrac{10\sqrt5}{5} = 2\sqrt5\). (b)
\[\dfrac{6(4 - \sqrt7)}{16 - 7} = \dfrac{6(4 - \sqrt7)}{9} = \dfrac{2(4 - \sqrt7)}{3} = \dfrac{8 - 2\sqrt7}{3}\]
Q: (Exam style) Express \(\dfrac{\sqrt{5} + 2}{\sqrt{5} - 2}\) in the form \(a + b\sqrt{5}\), where \(a\) and \(b\) are integers.
A: Multiply by \(\sqrt5 + 2\): numerator \((\sqrt5 + 2)^2 = 9 + 4\sqrt5\), [M1 A1] denominator \(5 - 4 = 1\). [A1] So the answer is \(9 + 4\sqrt5\). [A1]
Q: A virus has diameter \(1.2 \times 10^{-7}\) m. How many viruses in a row make 3 mm? Give the answer in standard form.
A: \(3\text{ mm} = 3 \times 10^{-3}\) m. Number \(= \dfrac{3 \times 10^{-3}}{1.2 \times 10^{-7}} = 2.5 \times 10^{4}\).
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Evaluate \(\left(\dfrac{27}{8}\right)^{-2/3}\).
A: A negative index means the reciprocal, and \(\tfrac13\) means the cube root: \(\left(\dfrac{27}{8}\right)^{-2/3} = \left(\dfrac{8}{27}\right)^{2/3} = \left(\dfrac23\right)^2\). [M1] \(= \dfrac49\). [A1]
Q: [3 marks] ★ Express \(\sqrt{75} + \sqrt{12} - \sqrt{27}\) in the form \(a\sqrt3\).
A: \(\sqrt{75} = 5\sqrt3\), \(\sqrt{12} = 2\sqrt3\) and \(\sqrt{27} = 3\sqrt3\). [M1] [A1] (M1 for any two correct, A1 for all three) So the sum is \(5\sqrt3 + 2\sqrt3 - 3\sqrt3 = 4\sqrt3\). [A1]
Q: [3 marks] ★★ Rationalise the denominator of \(\dfrac{6}{3 - \sqrt3}\), giving your answer in the form \(a + b\sqrt3\).
A: Multiply top and bottom by the conjugate \(3 + \sqrt3\): \(\dfrac{6(3 + \sqrt3)}{(3 - \sqrt3)(3 + \sqrt3)}\). [M1] The denominator is \(9 - 3 = 6\). [A1] So the fraction is \(3 + \sqrt3\). [A1]
Q: [3 marks] ★★ Solve \(4^{x+1} = 8^{x-1}\).
A: Write both sides as powers of \(2\): \(2^{2(x+1)} = 2^{3(x-1)}\). [M1] The bases match, so \(2x + 2 = 3x - 3\). [M1] \(x = 5\). [A1] Check: \(4^6 = 4096 = 8^4\).
Q: [3 marks] ★★ Without a calculator, work out \(\dfrac{(6.4 \times 10^{7})(2.5 \times 10^{-3})}{8 \times 10^{2}}\), giving your answer in standard form.
A: Numbers: \(6.4 \times 2.5 = 16\) [M1], then \(16 \div 8 = 2\). [M1] Powers of ten: \(10^{7 + (-3) - 2} = 10^2\). The answer is \(2 \times 10^2\). [A1]
Q: [4 marks] ★★ Simplify \((5x^2y^3)^2 \div (10x^3y^{-1})\).
A: \((5x^2y^3)^2 = 25x^4y^6\). [M1 A1] Divide: the numbers give \(\dfrac{25}{10} = \dfrac52\), and subtracting indices gives \(x^{4-3} = x\) and \(y^{6-(-1)} = y^7\). [M1] The answer is \(\dfrac52\,x\,y^7\). [A1]
Q: [4 marks] ★★ One bacterium has a mass of \(1.5 \times 10^{-12}\) g. (a) Find the mass of \(4 \times 10^{9}\) of these bacteria, in grams, in standard form. (b) How many of these bacteria have a total mass of \(1\) kg? Give your answer in standard form to 3 significant figures.
A: (a) \((1.5 \times 10^{-12})(4 \times 10^{9}) = 6 \times 10^{-3}\) g. [M1 A1] (b) \(1\) kg \(= 1000 = 10^3\) g [B1], so the number is \(\dfrac{10^3}{1.5 \times 10^{-12}} = 6.67 \times 10^{14}\). [A1]
Q: [6 marks] (#math.f.algebra) ★★★ (a) Express \(\dfrac{1 + \sqrt3}{2 - \sqrt3}\) in the form \(a + b\sqrt3\), where \(a\) and \(b\) are integers. (b) Given that \((p + \sqrt5)^2 = 21 + q\sqrt5\), where \(p\) is a positive integer and \(q\) is an integer, find \(p\) and \(q\).
H: For (a), multiply top and bottom by the conjugate of the denominator. Expand the top with all four products.
H: For (b), expand the bracket first. The terms without a surd must equal \(21\); the terms with \(\sqrt5\) must match too.
A: (a) Multiply by \(\dfrac{2 + \sqrt3}{2 + \sqrt3}\): the numerator is
\[\begin{aligned} (1 + \sqrt3)(2 + \sqrt3) &= 2 + \sqrt3 + 2\sqrt3 + 3 \\ &= 5 + 3\sqrt3 \end{aligned}\] [M1 A1] The denominator is \(4 - 3 = 1\), so the answer is \(5 + 3\sqrt3\). [A1] (b) \((p + \sqrt5)^2 = p^2 + 2p\sqrt5 + 5\). [M1] The numbers without a surd: \(p^2 + 5 = 21\), so \(p^2 = 16\) and \(p = 4\). [A1] The terms with \(\sqrt5\): \(q = 2p = 8\). [A1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Solve \(2^{2x} - 5 \times 2^x + 4 = 0\).
H: Write \(2^{2x}\) as \((2^x)^2\).
H: Let \(y = 2^x\). You get an ordinary quadratic in \(y\). Remember to turn each value of \(y\) back into \(x\).
A: Let \(y = 2^x\). Then \(2^{2x} = (2^x)^2 = y^2\), so \(y^2 - 5y + 4 = 0\). [M1 A1] \((y - 1)(y - 4) = 0\), so \(y = 1\) or \(y = 4\). [M1 A1] Then \(2^x = 1\) gives \(x = 0\) and \(2^x = 4\) gives \(x = 2\). [A1] Check \(x = 2\): \(2^4 - 5(4) + 4 = 0\). ✓
Q: [5 marks] ★★★ Find integers \(a\) and \(b\) such that \(\sqrt{11 + 6\sqrt2} = a + b\sqrt2\).
H: Square both sides. Then compare the part of each side without a surd and the part with \(\sqrt2\).
H: You need two whole numbers whose product is \(3\).
A: Squaring:
\[\begin{aligned} 11 + 6\sqrt2 &= (a + b\sqrt2)^2 \\ &= a^2 + 2b^2 + 2ab\sqrt2 \end{aligned}\] [M1] Since \(\sqrt2\) is irrational, the two parts must match separately: \(a^2 + 2b^2 = 11\) [A1] and \(2ab = 6\), so \(ab = 3\). [A1] The positive whole-number pairs with product \(3\) are \((1, 3)\) and \((3, 1)\). [M1] Only \(a = 3\), \(b = 1\) gives \(9 + 2 = 11\). [A1] So \(\sqrt{11 + 6\sqrt2} = 3 + \sqrt2\). Check: \(3 + 1.414 = 4.414\) and \(\sqrt{11 + 8.485} = \sqrt{19.485} = 4.414\). ✓
:::

:::quiz
? What is the value of \(2^{-3}\)?
- \(-8\)
- \(-6\)
+ \(\dfrac18\)
- \(\dfrac16\)
> A negative index means a reciprocal: \(2^{-3} = \dfrac{1}{2^3} = \dfrac18\). The option \(-8\) wrongly makes the answer negative, and \(\tfrac16\) multiplies \(2 \times 3\) instead of using the power.
? Which expression equals \(x^{-1/2}\)?
- \(-\sqrt{x}\)
- \(\dfrac{1}{2x}\)
+ \(\dfrac{1}{\sqrt{x}}\)
- \(\dfrac{x}{2}\)
> The fraction \(\tfrac12\) means "square root" and the minus sign means "one over". So \(x^{-1/2} = \dfrac{1}{x^{1/2}} = \dfrac{1}{\sqrt x}\).
? Simplify \(\sqrt{75}\).
- \(15\sqrt{5}\)
- \(3\sqrt{5}\)
+ \(5\sqrt{3}\)
- \(25\sqrt{3}\)
> The largest square factor of 75 is 25, and \(75 = 25 \times 3\), so \(\sqrt{75} = 5\sqrt3\). If you wrote \(25\sqrt3\), you forgot to take the square root of 25.
? Rationalise \(\dfrac{1}{2 + \sqrt{3}}\).
- \(\dfrac{2 + \sqrt3}{7}\)
+ \(2 - \sqrt{3}\)
- \(\dfrac{2 - \sqrt3}{7}\)
- \(2 + \sqrt3\)
> Multiply top and bottom by the conjugate \(2 - \sqrt3\): the denominator is \(4 - 3 = 1\), so the answer is \(2 - \sqrt3\). The options with a denominator of 7 come from adding \(4 + 3\) instead of subtracting. The option \(2 + \sqrt3\) is a sign slip in the numerator.
? What is the value of \(\left(\dfrac14\right)^{-3/2}\)?
- \(\dfrac18\)
+ \(8\)
- \(-8\)
- \(\dfrac16\)
> The negative index flips the fraction: \(\left(\tfrac14\right)^{-3/2} = 4^{3/2} = \left(\sqrt4\right)^3 = 8\). The option \(\tfrac18\) ignores the minus sign, \(-8\) wrongly makes the answer negative, and \(\tfrac16\) multiplies \(4\) by \(\tfrac32\) instead of using it as an index.
? What is \((3 \times 10^{4}) \times (4 \times 10^{5})\) in standard form?
- \(12 \times 10^{9}\)
+ \(1.2 \times 10^{10}\)
- \(1.2 \times 10^{20}\)
- \(7 \times 10^{9}\)
> Multiply the numbers (\(3 \times 4 = 12\)) and add the indices (\(4 + 5 = 9\)), giving \(12 \times 10^9\). That is not standard form, because 12 is not between 1 and 10: write it as \(1.2 \times 10^{10}\). Multiplying the indices gives the second wrong option, and adding everything gives \(7 \times 10^{9}\).
:::

:::checklist What you can now do
- [ ] I can use the laws of indices, including zero, negative and fractional indices.
- [ ] I can write \(\dfrac{5}{\sqrt{x}}\) or \(\sqrt[3]{x}\) as a power of \(x\), ready for calculus.
- [ ] I can simplify surds and expand brackets that contain surds.
- [ ] I can rationalise a denominator, including one with a conjugate pair.
- [ ] I can solve an equation where the unknown is in the index, by matching bases.
- [ ] I can calculate with numbers in standard form and give an answer to the accuracy asked.
:::

:::recap
- Index laws: add when multiplying, subtract when dividing, multiply for a power of a power; \(a^0 = 1\); \(a^{-n} = 1/a^n\); \(a^{m/n} = (\sqrt[n]{a})^m\).
- Write roots and reciprocals as powers of \(x\) before using calculus: \(\dfrac{1}{\sqrt x} = x^{-1/2}\).
- Simplify a surd by taking out the largest square factor. Add only like surds. \(\sqrt{a+b} \ne \sqrt a + \sqrt b\).
- Rationalise by multiplying top and bottom: by the surd, or by the conjugate \(a - \sqrt b\) of \(a + \sqrt b\).
- Standard form is \(a \times 10^n\) with \(1 \le a < 10\); compute the number and the power of 10 separately.
:::

:::links
- watch: [Introduction to surds](https://www.examsolutions.net/tutorials/surds-introduction-simplifying/) · ExamSolutions · simplifying surds step by step
- watch: [Fractional indices](https://www.examsolutions.net/tutorials/rational-fractional-indices/) · ExamSolutions · what a power of one half or two thirds means
- practise: [Algebra 2](https://www.khanacademy.org/math/algebra2) · Khan Academy · units on exponents and radicals
- read: [Algebra index](https://www.mathsisfun.com/algebra/index.html) · Maths is Fun · short pages on exponents, surds and standard form
- read: [Algebra and Trigonometry 2e (free textbook)](https://openstax.org/details/books/algebra-and-trigonometry-2e) · OpenStax · the prerequisites chapter covers exponents, radicals and scientific notation

Links checked 3 October 2026.
:::
Next: [Graphs and straight lines](#math.f.graphs).
