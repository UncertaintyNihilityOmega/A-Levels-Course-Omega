@chapter math.p3.algebra
@title Modulus and polynomials
@level as
@paper CAIE P2/P3 · Edexcel IAL P2–P3 · AQA/OCR/Edexcel Pure Year 1–2
@time 7–9 hours
@summary The modulus function: its graph, equations and inequalities. Polynomials: division by a linear or quadratic expression, the remainder and factor theorems, finding unknown coefficients and solving cubic and quartic equations.

:::why
The modulus gives the size of a number without its sign, which is how we describe errors, tolerances and distances. Polynomial division and the factor theorem are the tools for solving cubic equations, which the quadratic formula cannot do. Both appear again in partial fractions, integration and curve sketching, so you will use them for the rest of the course. This chapter is examined in Paper 2 and Paper 3 of the Cambridge syllabus.
:::

**Before you start**, you need quadratics and inequalities from [Quadratics](#math.p1.quadratics), the transformations of graphs in [Functions](#math.p1.functions), and expanding and factorising in [Algebra from scratch](#math.f.algebra).

## The modulus

:::def Modulus
The modulus of a real number \(x\), written \(|x|\), is its size (distance from zero), whatever its sign:
\[|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}\]
So \(|5| = 5\) and \(|-5| = 5\). The modulus is never negative.
:::

For a linear expression, \(|ax + b|\) equals \(ax + b\) when that is positive or zero, and \(-(ax + b)\) when it is negative. So the graph of \(y = |ax + b|\) is the graph of \(y = ax + b\) with the part below the \(x\)-axis **reflected** above it. It is V-shaped. The vertex is on the \(x\)-axis at \(x = -\dfrac{b}{a}\), where \(ax + b = 0\).

:::plot The graph of \(y = |2x - 3|\) is the line \(y = 2x - 3\) with the part below the x-axis reflected. The vertex is at (1.5, 0) and the y-intercept is 3.
--f "abs(2*x-3)" --label "y = |2x − 3|" --x -2 5 --y -1 8 --pt "1.5,0,(1.5, 0)@s" --pt "0,3,(0, 3)@ne" --legend tr
:::

To sketch \(y = |ax + b|\): mark the vertex \((-\tfrac ba, 0)\), the \(y\)-intercept \((0, |b|)\) and draw two straight lines with gradients \(\pm a\). This is the only type of modulus graph you must draw: the syllabus does not include \(|f(x)|\) for non-linear \(f\).

## Equations with a modulus

An equation \(|ax + b| = c\) means \(ax + b\) is a distance \(c\) from zero, so it equals \(c\) or \(-c\). If \(c < 0\) there is no solution, because a modulus cannot be negative.

:::eg Solve (a) \(|2x - 3| = 7\), (b) \(|x + 1| = -2\)
(a) \(2x - 3 = 7\) gives \(x = 5\), and \(2x - 3 = -7\) gives \(x = -2\). Check \(x = -2\): \(|-4 - 3| = 7\). ✓

(b) A modulus is never negative, so there is no solution.
:::

When both sides contain a variable, the most reliable method is to **square both sides**, using the fact that \(|a|^2 = a^2\). This turns the equation into a quadratic.

:::key Squaring with a modulus
\[|a| = |b| \iff a^2 = b^2\]
For \(|a| = b\), where \(b\) may contain \(x\), square both sides to get \(a^2 = b^2\), then **check every solution** in the original equation: squaring can add false answers (those where \(b < 0\)).
:::

:::eg Solve (a) \(|x - 2| = |3x + 4|\), (b) \(|x + 1| = 2x - 4\)
(a) Square both sides:
\[\begin{aligned} (x - 2)^2 &= (3x + 4)^2 \\ x^2 - 4x + 4 &= 9x^2 + 24x + 16 \\ 8x^2 + 28x + 12 &= 0 \\ 2x^2 + 7x + 3 &= 0 \end{aligned}\]
So \((2x + 1)(x + 3) = 0\), giving \(x = -\tfrac12\) or \(x = -3\). Both are valid: for \(x = -\tfrac12\), \(|-2.5| = 2.5 = |2.5|\), and for \(x = -3\), \(|-5| = 5 = |-5|\).

(b) Square both sides: \((x + 1)^2 = (2x - 4)^2\), so \(x^2 + 2x + 1 = 4x^2 - 16x + 16\) and \(3x^2 - 18x + 15 = 0\), which simplifies to \(x^2 - 6x + 5 = 0\). So \(x = 1\) or \(x = 5\). Check each in \(|x + 1| = 2x - 4\):

\(x = 1\): left side \(|2| = 2\), right side \(2 - 4 = -2\). Not equal, so reject.

\(x = 5\): left side \(6\), right side \(6\). ✓

The only solution is \(x = 5\).
:::

The false root has a meaning. Squaring \(|x + 1| = 2x - 4\) also solves \(|x + 1| = -(2x - 4)\), which is the line \(y = 2x - 4\) reflected in the \(x\)-axis. The value \(x = 1\) belongs to that equation, not to the original. A sketch of the two graphs shows the solutions as the \(x\)-coordinates where they meet. Here is one for a different equation, \(|2x - 1| = x + 4\), which has two valid solutions.

:::plot The graphs of \(y = |2x - 1|\) and \(y = x + 4\) meet at (−1, 3) and (5, 9). Between those points the V is below the line.
--f "abs(2*x-1)" --f "x+4" --label "y = |2x − 1|" --label "y = x + 4" --x -4 7 --y -1 12 --pt "-1,3,(−1, 3)@se" --pt "5,9,(5, 9)@se" --legend tl
:::

## Inequalities with a modulus

The distance idea gives the standard results. \(|x - a| < b\) means \(x\) is within \(b\) of \(a\).

:::key Modulus inequalities (\(b > 0\))
\[|x - a| < b \iff a - b < x < a + b\]
\[|x - a| > b \iff x < a - b \ \text{ or } \ x > a + b\]
For \(|ax + b| < c\), write \(-c < ax + b < c\) and solve. For \(|f(x)| < |g(x)|\), square both sides to get \(f(x)^2 < g(x)^2\), rearrange to \(0\) on one side and use a sketch of the quadratic.
:::

:::eg Solve (a) \(|2x - 3| < 5\), (b) \(|x + 2| \ge 3\)
(a) \(-5 < 2x - 3 < 5\). Add 3: \(-2 < 2x < 8\). Divide by 2: \(-1 < x < 4\).

(b) Either \(x + 2 \ge 3\) or \(x + 2 \le -3\), so \(x \ge 1\) or \(x \le -5\).
:::

:::eg A machine part has length \(L\) cm and is acceptable if it differs from the target \(12.5\) cm by at most \(0.2\) cm. Write this using a modulus and find the acceptable lengths.
The condition is \(|L - 12.5| \le 0.2\). So \(-0.2 \le L - 12.5 \le 0.2\), giving \(12.3 \le L \le 12.7\) cm.
:::

:::eg (Exam style) Solve the inequality \(|2x - 1| > |x + 3|\).
Both sides are non-negative, so square both: \((2x - 1)^2 > (x + 3)^2\). [M1]
\[\begin{aligned} 4x^2 - 4x + 1 &> x^2 + 6x + 9 \\ 3x^2 - 10x - 8 &> 0 \end{aligned}\] [A1]
Factorise: \((3x + 2)(x - 4) > 0\), so the critical values are \(x = -\tfrac23\) and \(x = 4\). [M1]
The quadratic opens upward, so it is positive outside the roots: [M1]
\[x < -\tfrac23 \quad \text{or} \quad x > 4\] [A1]
Check \(x = 0\): \(|-1| = 1\) is not greater than \(|3| = 3\), and \(0\) is between the roots. ✓
:::

When one side is a plain expression, not a modulus, use \(|a| < b \iff -b < a < b\) (which needs \(b > 0\)).

:::eg Solve \(|x - 3| < 2x\).
The right side must be positive, so we need \(-2x < x - 3 < 2x\).

From \(x - 3 < 2x\): \(x > -3\). From \(-2x < x - 3\): \(3x > 3\), so \(x > 1\).

Both must hold, so \(x > 1\). (Squaring would also give \(x < -3\), which is not valid because there the right side \(2x\) is negative.) Check \(x = 2\): \(|-1| = 1 < 4\). ✓
:::

:::warn Modulus slips
- \(|x| = 3\) has **two** solutions, \(x = \pm 3\), but \(|x| < 3\) is the single interval \(-3 < x < 3\), and \(|x| > 3\) is two separate pieces.
- \(|a + b| \ne |a| + |b|\) in general: \(|3 + (-5)| = 2\) but \(|3| + |-5| = 8\).
- After squaring, always check solutions against the original equation. Do not square an inequality unless both sides are non-negative.
:::

## Polynomials and division

:::def Polynomial
An expression of the form \(a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0\), where the powers are non-negative integers. The highest power \(n\) is the **degree**. A degree 2 polynomial is quadratic, degree 3 is cubic and degree 4 is quartic.
:::

You can divide polynomials in the same way you divide whole numbers: \(17 \div 5 = 3\) remainder \(2\) means \(17 = 5 \times 3 + 2\). For polynomials:

\[f(x) = (\text{divisor}) \times (\text{quotient}) + \text{remainder}\]

where the remainder has lower degree than the divisor. Dividing by a linear divisor \((x - a)\) gives a constant remainder. Dividing by a quadratic gives a remainder of the form \(px + q\).

Use long division. Divide the leading term of what is left by the leading term of the divisor, multiply back, subtract, and repeat. Write missing powers as \(0x^2\) so columns line up.

:::eg Divide \(2x^3 - 5x^2 + x + 6\) by \(x - 2\).
\(2x^3 \div x = 2x^2\). Multiply back: \(2x^2(x - 2) = 2x^3 - 4x^2\). Subtract: \(-x^2 + x + 6\).
\(-x^2 \div x = -x\). Multiply: \(-x(x - 2) = -x^2 + 2x\). Subtract: \(-x + 6\).
\(-x \div x = -1\). Multiply: \(-1(x - 2) = -x + 2\). Subtract: \(4\).

The quotient is \(2x^2 - x - 1\) and the remainder is \(4\):
\[2x^3 - 5x^2 + x + 6 = (x - 2)(2x^2 - x - 1) + 4\]
Check: \((x - 2)(2x^2 - x - 1) = 2x^3 - 5x^2 + x + 2\), and adding 4 gives \(2x^3 - 5x^2 + x + 6\). ✓
:::

:::eg Divide \(x^4 + 2x^3 - 7x^2 + 3x + 5\) by \(x^2 + x - 1\).
\(x^4 \div x^2 = x^2\). Multiply: \(x^2(x^2 + x - 1) = x^4 + x^3 - x^2\). Subtract: \(x^3 - 6x^2 + 3x + 5\).
\(x^3 \div x^2 = x\). Multiply: \(x^3 + x^2 - x\). Subtract: \(-7x^2 + 4x + 5\).
\(-7x^2 \div x^2 = -7\). Multiply: \(-7x^2 - 7x + 7\). Subtract: \(11x - 2\).

The quotient is \(x^2 + x - 7\) and the remainder is \(11x - 2\) (degree 1, lower than the divisor).
:::

## The remainder and factor theorems

You do not always need the full division. The remainder alone is found by substitution.

:::key Remainder theorem and factor theorem
- **Remainder theorem:** when \(f(x)\) is divided by \((x - a)\), the remainder is \(f(a)\). When divided by \((ax + b)\), the remainder is \(f\left(-\dfrac{b}{a}\right)\).
- **Factor theorem:** \((x - a)\) is a factor of \(f(x)\) if and only if \(f(a) = 0\). Similarly \((ax + b)\) is a factor if and only if \(f\left(-\dfrac ba\right) = 0\).
Reason: \(f(x) = (x - a)q(x) + r\). Put \(x = a\) and the bracket vanishes, leaving \(f(a) = r\).
:::

:::eg Find the remainder when \(f(x) = 2x^3 - 3x^2 - 11x + 6\) is divided by (a) \(x - 1\), (b) \(2x + 3\). Show that \((x - 3)\) is a factor.
(a) \(f(1) = 2 - 3 - 11 + 6 = -6\).

(b) The root of \(2x + 3\) is \(x = -\tfrac32\):
\[f\left(-\tfrac32\right) = 2\left(-\tfrac{27}{8}\right) - 3\left(\tfrac94\right) - 11\left(-\tfrac32\right) + 6 = -6.75 - 6.75 + 16.5 + 6 = 9\]
(c) \(f(3) = 54 - 27 - 33 + 6 = 0\), so \((x - 3)\) is a factor.
:::

## Solving polynomial equations

To solve a cubic \(f(x) = 0\): try small factors of the constant term (\(\pm1, \pm2, \pm3, \ldots\)) until \(f(a) = 0\); that gives a factor \((x - a)\). Divide to get a quadratic, then factorise or use the formula. For a leading coefficient other than 1, the possible rational roots are \(\dfrac{\text{factor of constant}}{\text{factor of leading coefficient}}\).

:::eg Solve (a) \(x^3 - 4x^2 + x + 6 = 0\), (b) \(2x^3 - 3x^2 - 11x + 6 = 0\), (c) \(x^3 - x^2 - 3x - 1 = 0\) giving exact answers.
(a) \(f(2) = 8 - 16 + 2 + 6 = 0\), so \((x - 2)\) is a factor. Dividing: \(x^3 - 4x^2 + x + 6 = (x - 2)(x^2 - 2x - 3) = (x - 2)(x - 3)(x + 1)\). The solutions are \(x = 2, 3, -1\).

(b) From the earlier example \(f(3) = 0\). Dividing by \((x - 3)\): \(2x^3 - 3x^2 - 11x + 6 = (x - 3)(2x^2 + 3x - 2) = (x - 3)(2x - 1)(x + 2)\). The solutions are \(x = 3, \tfrac12, -2\).

(c) Try \(x = -1\): \(-1 - 1 + 3 - 1 = 0\), so \((x + 1)\) is a factor. Dividing: \((x + 1)(x^2 - 2x - 1)\). The quadratic has discriminant \(4 + 4 = 8\), so \(x = \dfrac{2 \pm \sqrt8}{2} = 1 \pm \sqrt2\). The solutions are \(x = -1\), \(1 + \sqrt2\), \(1 - \sqrt2\).
:::

A polynomial with an unknown coefficient can be found by substituting a known root or remainder. Write one equation for each piece of information, then solve them together.

:::eg (Exam style) The polynomial \(f(x) = x^3 + ax^2 + bx - 6\) has a factor \((x - 1)\) and leaves a remainder of \(12\) when divided by \((x + 2)\). (a) Find \(a\) and \(b\). (b) Solve \(f(x) = 0\).
**(a)** Factor theorem: \(f(1) = 0\), so \(1 + a + b - 6 = 0\), giving \(a + b = 5\). [M1 A1]
Remainder theorem: \(f(-2) = 12\), so \(-8 + 4a - 2b - 6 = 12\), giving \(2a - b = 13\). [M1 A1]
Add the equations: \(3a = 18\), so \(a = 6\) and \(b = -1\). [A1]

**(b)** \(f(x) = x^3 + 6x^2 - x - 6\). Divide by \((x - 1)\): \(f(x) = (x - 1)(x^2 + 7x + 6)\). [M1]
\[f(x) = (x - 1)(x + 1)(x + 6)\] [A1]
So \(x = 1\), \(-1\) or \(-6\). [A1]
Check: \(f(-1) = -1 + 6 + 1 - 6 = 0\). ✓
:::

:::eg (Exam style) An open box is made from a rectangular sheet of card 30 cm by 20 cm by cutting a square of side \(x\) cm from each corner and folding up the sides. The volume of the box is \(1008\) cm³. (a) Show that \(x^3 - 25x^2 + 150x - 252 = 0\). (b) Show that \(x = 3\) is a solution and find the other value of \(x\) that is possible.
**(a)** The box has length \(30 - 2x\), width \(20 - 2x\) and height \(x\). [B1]
\[x(30 - 2x)(20 - 2x) = 1008 \implies 4x^3 - 100x^2 + 600x = 1008\] [M1]
Divide by 4: \(x^3 - 25x^2 + 150x - 252 = 0\). [A1]

**(b)** \(f(3) = 27 - 225 + 450 - 252 = 0\), so \(x = 3\) is a solution and \((x - 3)\) is a factor. [M1]
\[x^3 - 25x^2 + 150x - 252 = (x - 3)(x^2 - 22x + 84)\] [M1]
The quadratic has discriminant \(484 - 336 = 148\), so \(x = \dfrac{22 \pm \sqrt{148}}{2} = 11 \pm \sqrt{37}\), which is \(17.08\) or \(4.917\). [M1]
The width \(20 - 2x\) must be positive, so \(x < 10\). The other possible value is \(x = 11 - \sqrt{37} = 4.92\) cm (3 s.f.). [A1]
:::

:::exam Presenting polynomial work
- When a question says "hence" or "show that \(x = 3\) is a root", **substitute** and show the arithmetic; then divide to find the quadratic. Mark schemes give a method mark for the division or for the coefficient comparison.
- Write the division in full or use coefficients: if \(f(x) = (x - 3)(x^2 + px + q)\), compare the \(x^2\) terms and the constant term to find \(p\) and \(q\).
- Look at the context for restrictions on the answer (here \(x < 10\)). Reject roots that do not fit.
:::

:::board Other boards
Edexcel IAL covers the modulus and the factor and remainder theorems in P2 and P3 (modulus functions with graphs and inequalities appear in P3). UK A Levels (AQA, Edexcel, OCR) include the factor theorem in Pure Year 1 and the modulus function in Year 2. Cambridge restricts the modulus graph to linear expressions, so do not expect \(|f(x)|\) for other functions in a Cambridge paper.
:::

:::try Start easy, finish at exam standard
Q: Solve (a) \(|3x - 1| = 8\), (b) \(|x - 4| = |x + 2|\).
A: (a) \(3x - 1 = 8\) gives \(x = 3\); \(3x - 1 = -8\) gives \(x = -\tfrac73\). (b) Square: \(x^2 - 8x + 16 = x^2 + 4x + 4\), so \(12 = 12x\) and \(x = 1\). Check: \(|-3| = 3 = |3|\). ✓
Q: Sketch \(y = |3x + 6|\), giving the intercepts.
A: A V-shape with vertex \((-2, 0)\) and \(y\)-intercept \((0, 6)\); gradient \(3\) on the right and \(-3\) on the left.
Q: Solve (a) \(|2x + 1| < 7\), (b) \(|x - 3| \ge 4\).
A: (a) \(-7 < 2x + 1 < 7\) gives \(-4 < x < 3\). (b) \(x - 3 \ge 4\) or \(x - 3 \le -4\), so \(x \ge 7\) or \(x \le -1\).
Q: Solve \(|x - 1| = 3x + 5\), and check your answers.
A: Square: \(x^2 - 2x + 1 = 9x^2 + 30x + 25\), so \(8x^2 + 32x + 24 = 0\) and \(x^2 + 4x + 3 = 0\), giving \(x = -1\) or \(x = -3\). Check \(x = -1\): \(|-2| = 2\) and \(3(-1) + 5 = 2\). ✓ Check \(x = -3\): \(|-4| = 4\) but \(3(-3) + 5 = -4\). ✗ So \(x = -1\) only.
Q: Find the remainder when \(f(x) = x^3 - 5x + 3\) is divided by (a) \(x - 2\), (b) \(x + 1\), (c) \(2x - 1\).
A: (a) \(f(2) = 8 - 10 + 3 = 1\). (b) \(f(-1) = -1 + 5 + 3 = 7\). (c) \(f\left(\tfrac12\right) = \tfrac18 - \tfrac52 + 3 = \tfrac58\).
Q: Divide \(x^3 + 3x^2 - 4x - 12\) by \(x + 3\), and hence solve \(x^3 + 3x^2 - 4x - 12 = 0\).
A: The quotient is \(x^2 - 4\) and the remainder is \(0\) (since \(f(-3) = -27 + 27 + 12 - 12 = 0\)). So \(f(x) = (x + 3)(x - 2)(x + 2)\) and \(x = -3, 2, -2\).
Q: Show that \((x + 2)\) is a factor of \(x^3 + 4x^2 + x - 6\) and solve the equation \(x^3 + 4x^2 + x - 6 = 0\).
A: \(f(-2) = -8 + 16 - 2 - 6 = 0\), so \((x + 2)\) is a factor. Dividing: \((x + 2)(x^2 + 2x - 3) = (x + 2)(x + 3)(x - 1)\). The solutions are \(x = -2, -3, 1\).
Q: Divide \(2x^4 - x^3 + 3x - 1\) by \(x^2 - x + 1\) and state the quotient and remainder.
A: \(2x^2 \cdot (x^2 - x + 1) = 2x^4 - 2x^3 + 2x^2\), leaving \(x^3 - 2x^2 + 3x - 1\). Next \(x(x^2 - x + 1) = x^3 - x^2 + x\), leaving \(-x^2 + 2x - 1\). Next \(-1(x^2 - x + 1) = -x^2 + x - 1\), leaving \(x\). The quotient is \(2x^2 + x - 1\) and the remainder is \(x\).
Q: Solve the inequality \(|x + 1| < |2x - 5|\).
A: Square both sides: \(x^2 + 2x + 1 < 4x^2 - 20x + 25\), so \(3x^2 - 22x + 24 > 0\). Factorise: \((3x - 4)(x - 6) > 0\), with critical values \(\tfrac43\) and \(6\). So \(x < \tfrac43\) or \(x > 6\). Check \(x = 0\): \(1 < 5\) ✓; \(x = 3\): \(4 < 1\) false, and \(3\) is between the roots ✓.
Q: (Exam style) The polynomial \(f(x) = 2x^3 + ax^2 + bx + 6\) is divisible by \((x - 2)\) and leaves remainder \(18\) when divided by \((x + 1)\). (a) Find \(a\) and \(b\). (b) Factorise \(f(x)\) completely and solve \(f(x) = 0\).
A: (a) \(f(2) = 16 + 4a + 2b + 6 = 0\), so \(2a + b = -11\). [M1 A1] \(f(-1) = -2 + a - b + 6 = 18\), so \(a - b = 14\). [M1 A1] Adding: \(3a = 3\), so \(a = 1\) and \(b = -13\). [A1] (b) \(f(x) = 2x^3 + x^2 - 13x + 6 = (x - 2)(2x^2 + 5x - 3)\). [M1] \(= (x - 2)(2x - 1)(x + 3)\), so \(x = 2, \tfrac12, -3\). [A1 A1]
:::

:::quiz
? What are the solutions of \(|x - 4| = 6\)?
- \(x = 10\) only
- \(x = -2\) only
+ \(x = 10\) or \(x = -2\)
- \(x = 2\) or \(x = -10\)
> The expression \(x - 4\) equals \(6\) or \(-6\). That gives \(x = 10\) or \(x = -2\). Giving only one answer loses a mark, and \(x = 2\) or \(-10\) comes from moving the \(4\) with the wrong sign.
? Which is the solution of \(|x - 2| < 3\)?
- \(x < 5\)
- \(x < -1\) or \(x > 5\)
+ \(-1 < x < 5\)
- \(x > -1\)
> \(|x - 2| < 3\) means \(x\) is within \(3\) of \(2\), so \(-1 < x < 5\). The option with "or" is the solution of \(|x - 2| > 3\).
? The remainder when \(f(x) = x^3 + 2x - 5\) is divided by \((x - 2)\) is
- \(-5\)
+ \(7\)
- \(2\)
- \(-17\)
> The remainder theorem gives \(f(2) = 8 + 4 - 5 = 7\). The value \(-5\) is \(f(0)\), and \(-17\) is \(f(-2)\), the usual sign slip of using the number in the bracket instead of its root.
? \(f(x) = x^3 - 3x^2 + kx + 6\) has a factor \((x - 3)\). What is \(k\)?
+ \(k = -2\)
- \(k = -6\)
- \(k = 2\)
- \(k = 0\)
> \(f(3) = 27 - 27 + 3k + 6 = 3k + 6 = 0\), so \(k = -2\). Forgetting that the terms \(27\) and \(-27\) cancel, or dropping the constant 6, gives the other values.
:::

:::recap
- \(|x|\) is the size of \(x\). \(|ax + b| = c\) gives \(ax + b = \pm c\) (none if \(c < 0\)). \(|a| = |b| \iff a^2 = b^2\); check answers after squaring.
- \(|x - a| < b \iff a - b < x < a + b\), and \(|x - a| > b\) is two pieces. The graph of \(y = |ax + b|\) is a V with vertex \(\left(-\tfrac ba, 0\right)\).
- Polynomial division: \(f(x) = \text{divisor} \times \text{quotient} + \text{remainder}\), remainder of lower degree than the divisor. Write missing powers as \(0x^n\).
- Remainder theorem: the remainder on dividing by \((x - a)\) is \(f(a)\); by \((ax + b)\) it is \(f(-b/a)\). Factor theorem: \(f(a) = 0 \iff (x - a)\) is a factor.
- To solve a cubic: find one root by trial, divide, then solve the quadratic. Unknown coefficients: one equation per condition.
:::

:::links
- watch: [Modulus inequalities](https://www.examsolutions.net/tutorials/modulus-inequalities/) · ExamSolutions · squaring both sides and the graphical method
- watch: [Exam questions: remainder theorem](https://www.examsolutions.net/tutorials/exam-questions-remainder-theorem/) · ExamSolutions · factor and remainder theorem questions on video
- practise: [CAIE Pure 3 modulus exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/algebra-and-functions/modulus-functions/exam-questions/) · Save My Exams · with mark schemes [paid]
- practise: [CAIE Pure 3 polynomials exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-3/topic-questions/algebra-and-functions/polynomials/exam-questions/) · Save My Exams · division, factor and remainder theorems [paid]
- explore: [Polynomials & Rational Functions](https://undergroundmathematics.org/polynomials) · Underground Mathematics · rich problems on polynomials
- papers: [9709 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-2/) · Physics & Maths Tutor · Paper 2 (AS) has this topic too [unofficial]

Links checked 3 October 2026.
:::
Next: [Logarithms and exponentials](#math.p3.logs).
