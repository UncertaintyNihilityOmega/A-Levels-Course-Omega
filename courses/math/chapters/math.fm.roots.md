@chapter math.fm.roots
@title Roots of polynomial equations
@level fm
@paper CAIE 9231 Paper 1 · AQA/OCR/Edexcel Further Maths Core Pure
@time 6–8 hours
@summary The roots of a polynomial equation are tied to its coefficients by simple rules. You will learn those rules for quadratic, cubic and quartic equations, use them to find sums such as \(\alpha^2 + \beta^2 + \gamma^2\) without solving the equation, find unknown coefficients from facts about the roots, and use a substitution to build a new equation whose roots are related to the old ones.

:::why
Most cubic and quartic equations cannot be solved neatly, yet you can still say a great deal about their roots: their sum, their product, the sum of their squares, even whether they are all real. Further Mathematics opens with this idea because it is pure algebra at its most efficient, and it returns throughout the course: in eigenvalues, in complex numbers and in the characteristic equations of differential equations.
:::

**Before you start**, you need the factor theorem and polynomial division from [Modulus and polynomials](#math.p3.algebra), the quadratic formula and the discriminant from [Quadratics](#math.p1.quadratics), and complex conjugates from [Complex numbers](#math.p3.complex). Expanding brackets such as \((a + b)^3\), from [Series: binomial expansion and progressions](#math.p1.series), appears in almost every example.

:::try Warm-up
Q: Show that \(x - 2\) is a factor of \(x^3 - 3x^2 + 4\). (from [Modulus and polynomials](#math.p3.algebra))
A: Put \(x = 2\): \(8 - 12 + 4 = 0\). By the factor theorem, \(x - 2\) is a factor.
Q: Solve \(x^2 - 4x + 13 = 0\). (from [Complex numbers](#math.p3.complex))
A: \(x = \dfrac{4 \pm \sqrt{16 - 52}}{2} = \dfrac{4 \pm 6\mathrm{i}}{2}\), so \(x = 2 + 3\mathrm{i}\) or \(x = 2 - 3\mathrm{i}\).
Q: Expand \((a + b)^3\). (from [Series: binomial expansion and progressions](#math.p1.series))
A: \((a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3\).
:::

## Roots and coefficients of a quadratic

Suppose the quadratic equation \(ax^2 + bx + c = 0\) has roots \(\alpha\) and \(\beta\) (the Greek letters alpha and beta). Then \(x - \alpha\) and \(x - \beta\) are factors of the quadratic, so the quadratic must be \(a(x - \alpha)(x - \beta)\). Expanding that and matching it with \(ax^2 + bx + c\) links the roots to the coefficients.

:::def Root of a polynomial equation
A number (real or complex) that makes the polynomial equal to zero. A polynomial equation of degree \(n\) has exactly \(n\) roots, counting repeated roots and complex roots.
:::

:::def Coefficient
The number multiplying a power of \(x\) in a polynomial. In \(2x^3 - 5x + 1\), the coefficient of \(x^3\) is 2, of \(x^2\) is 0 and of \(x\) is \(-5\); the constant term is 1.
:::

Expand the factorised form:
\[a(x - \alpha)(x - \beta) = ax^2 - a(\alpha + \beta)x + a\alpha\beta\]
This is the same polynomial as \(ax^2 + bx + c\), so the coefficients match: \(-a(\alpha + \beta) = b\) and \(a\alpha\beta = c\).

:::key Roots of a quadratic
If \(\alpha\) and \(\beta\) are the roots of \(ax^2 + bx + c = 0\), then
\[\alpha + \beta = -\frac{b}{a} \qquad \alpha\beta = \frac{c}{a}\]
Conversely, a quadratic with roots \(\alpha\) and \(\beta\) is
\[x^2 - (\alpha + \beta)x + \alpha\beta = 0\]
"\(x^2\) minus the sum times \(x\), plus the product."
:::

:::eg The equation \(2x^2 - 5x + 7 = 0\) has roots \(\alpha\) and \(\beta\). Write down \(\alpha + \beta\) and \(\alpha\beta\).
Here \(a = 2\), \(b = -5\), \(c = 7\).
\[\alpha + \beta = -\frac{-5}{2} = \frac52 \qquad \alpha\beta = \frac72\]
You did not need the roots themselves. In fact they are complex: the discriminant is \(25 - 56 = -31 < 0\). The rules work for complex roots just as well.
:::

### Symmetric functions of two roots

An expression such as \(\alpha^2 + \beta^2\) does not change if you swap \(\alpha\) and \(\beta\). Expressions like this can always be written in terms of \(\alpha + \beta\) and \(\alpha\beta\), so you can evaluate them straight from the coefficients.

:::def Symmetric function of the roots
An expression in the roots that is unchanged when any two roots are swapped, such as \(\alpha + \beta\), \(\alpha^2 + \beta^2\) or \(\dfrac{1}{\alpha} + \dfrac{1}{\beta}\).
:::

The trick is always the same: start from a power of \(\alpha + \beta\) and remove what you do not want.

:::key Useful identities for two roots
\[\begin{aligned}
\alpha^2 + \beta^2 &= (\alpha + \beta)^2 - 2\alpha\beta \\
\frac{1}{\alpha} + \frac{1}{\beta} &= \frac{\alpha + \beta}{\alpha\beta} \\
\alpha^3 + \beta^3 &= (\alpha + \beta)^3 - 3\alpha\beta(\alpha + \beta) \\
(\alpha - \beta)^2 &= (\alpha + \beta)^2 - 4\alpha\beta
\end{aligned}\]
:::

:::eg For the roots of \(2x^2 - 5x + 7 = 0\), find (a) \(\alpha^2 + \beta^2\), (b) \(\dfrac{1}{\alpha} + \dfrac{1}{\beta}\), (c) \(\alpha^3 + \beta^3\).
Use \(\alpha + \beta = \tfrac52\) and \(\alpha\beta = \tfrac72\).

(a)
\[\alpha^2 + \beta^2 = \left(\tfrac52\right)^2 - 2 \times \tfrac72 = \tfrac{25}{4} - 7 = -\tfrac34\]
A sum of two squares is negative. That is impossible for real numbers, and it confirms that the roots are not real.

(b)
\[\frac{1}{\alpha} + \frac{1}{\beta} = \frac{5/2}{7/2} = \frac57\]
(c)
\[\begin{aligned}
\alpha^3 + \beta^3 &= \left(\tfrac52\right)^3 - 3 \times \tfrac72 \times \tfrac52 \\
&= \tfrac{125}{8} - \tfrac{210}{8} = -\tfrac{85}{8}
\end{aligned}\]
:::

### Forming a new quadratic

To build an equation whose roots are, say, \(\alpha^2\) and \(\beta^2\), find their sum and their product, then use "\(x^2\) minus the sum times \(x\), plus the product".

:::eg Find a quadratic equation with integer coefficients whose roots are \(\alpha^2\) and \(\beta^2\), where \(\alpha\) and \(\beta\) are the roots of \(2x^2 - 5x + 7 = 0\).
The sum of the new roots is \(\alpha^2 + \beta^2 = -\tfrac34\), found above. The product is \(\alpha^2\beta^2 = (\alpha\beta)^2 = \tfrac{49}{4}\).

The new equation is \(x^2 + \tfrac34 x + \tfrac{49}{4} = 0\). Multiply by 4 for integer coefficients: \(4x^2 + 3x + 49 = 0\).
:::

## Cubic equations

A cubic equation \(ax^3 + bx^2 + cx + d = 0\) has three roots \(\alpha\), \(\beta\), \(\gamma\) (gamma). The same idea works: the cubic is \(a(x - \alpha)(x - \beta)(x - \gamma)\), so expand and compare coefficients.

:::proof Why the cubic relations hold
Multiply out two brackets first:
\[(x - \alpha)(x - \beta) = x^2 - (\alpha + \beta)x + \alpha\beta\]
Multiply by \((x - \gamma)\) and collect each power of \(x\):
\[\begin{aligned}
(x - \alpha)(x - \beta)(x - \gamma) &= x^3 - (\alpha + \beta)x^2 + \alpha\beta x \\
&\quad - \gamma x^2 + \gamma(\alpha + \beta)x - \alpha\beta\gamma \\
&= x^3 - (\alpha + \beta + \gamma)x^2 \\
&\quad + (\alpha\beta + \beta\gamma + \gamma\alpha)x - \alpha\beta\gamma
\end{aligned}\]
Multiply by \(a\) and match with \(ax^3 + bx^2 + cx + d\): the \(x^2\) terms give \(-a(\alpha + \beta + \gamma) = b\), the \(x\) terms give \(a(\alpha\beta + \beta\gamma + \gamma\alpha) = c\), and the constants give \(-a\alpha\beta\gamma = d\). Dividing by \(a\) gives the three rules below.
:::

Writing out every term gets long, so we use sigma notation for symmetric sums: \(\sum \alpha\) means the sum of the roots, \(\sum \alpha\beta\) the sum of the products of the roots in pairs, and so on.

:::key Roots of a cubic
If \(\alpha\), \(\beta\), \(\gamma\) are the roots of \(ax^3 + bx^2 + cx + d = 0\), then
\[\begin{aligned}
\textstyle\sum \alpha &= \alpha + \beta + \gamma = -\frac{b}{a} \\
\textstyle\sum \alpha\beta &= \alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a} \\
\alpha\beta\gamma &= -\frac{d}{a}
\end{aligned}\]
The signs alternate: minus, plus, minus.
:::

:::eg The cubic equation \(2x^3 - 3x^2 + 4x - 5 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Write down \(\sum \alpha\), \(\sum \alpha\beta\) and \(\alpha\beta\gamma\).
Here \(a = 2\), \(b = -3\), \(c = 4\), \(d = -5\).
\[\textstyle\sum \alpha = -\frac{-3}{2} = \frac32 \qquad \sum \alpha\beta = \frac42 = 2 \qquad \alpha\beta\gamma = -\frac{-5}{2} = \frac52\]
:::

:::warn Signs and missing terms
The sum and the product carry a minus sign; the pairs do not. If a power of \(x\) is missing, its coefficient is 0: for \(x^3 - 7x + 6 = 0\), \(\sum \alpha = 0\), not \(-7\). Write \(a\), \(b\), \(c\), \(d\) down before you use them.
:::

### Symmetric functions of three roots

The identities extend to three roots. Squaring the sum gives every square once and every pair twice:
\[\left(\textstyle\sum \alpha\right)^2 = \alpha^2 + \beta^2 + \gamma^2 + 2(\alpha\beta + \beta\gamma + \gamma\alpha)\]

:::key Useful identities for three roots
\[\begin{aligned}
\textstyle\sum \alpha^2 &= \left(\textstyle\sum \alpha\right)^2 - 2\textstyle\sum \alpha\beta \\
\textstyle\sum \frac{1}{\alpha} &= \frac{\sum \alpha\beta}{\alpha\beta\gamma} \\
\textstyle\sum \alpha^2\beta^2 &= \left(\textstyle\sum \alpha\beta\right)^2 - 2\alpha\beta\gamma\textstyle\sum \alpha
\end{aligned}\]
For \(\sum \alpha^3\) and higher powers, use the equation itself (next section).
:::

The second identity comes from a common denominator:
\[\frac{1}{\alpha} + \frac{1}{\beta} + \frac{1}{\gamma} = \frac{\beta\gamma + \alpha\gamma + \alpha\beta}{\alpha\beta\gamma}\]

### Sums of powers: let the equation do the work

Every root satisfies the equation. If \(\alpha\) is a root of \(x^3 - 2x^2 + 4x + 3 = 0\), then \(\alpha^3 = 2\alpha^2 - 4\alpha - 3\), and the same is true for \(\beta\) and \(\gamma\). Add the three lines and you have \(\sum \alpha^3\) in terms of sums you already know. Multiply each line by \(\alpha\) first and you get \(\sum \alpha^4\), and so on.

:::key Sums of powers of the roots
Write \(S_n = \alpha^n + \beta^n + \gamma^n\), so \(S_0 = 3\), \(S_1 = \sum \alpha\) and \(S_2 = \sum \alpha^2\). For the roots of \(ax^3 + bx^2 + cx + d = 0\),
\[aS_{n+3} + bS_{n+2} + cS_{n+1} + dS_n = 0\]
With \(n = 0\): \(aS_3 + bS_2 + cS_1 + 3d = 0\). Remember \(S_0 = 3\), not 1: the constant \(d\) appears once for each root.
The same idea works for any degree: for a quartic \(S_0 = 4\) and the relation has five terms. With \(n = -1\) it gives \(S_{-1} = \sum \dfrac{1}{\alpha}\) as well.
:::

:::eg (Exam style) The cubic equation \(x^3 - 2x^2 + 4x + 3 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Find the values of (a) \(\alpha^2 + \beta^2 + \gamma^2\), (b) \(\dfrac{1}{\alpha} + \dfrac{1}{\beta} + \dfrac{1}{\gamma}\), (c) \(\alpha^3 + \beta^3 + \gamma^3\).
From the coefficients: \(\sum \alpha = 2\), \(\sum \alpha\beta = 4\), \(\alpha\beta\gamma = -3\).

**(a)**
\[\textstyle\sum \alpha^2 = 2^2 - 2 \times 4\] [M1]
\[= -4\] [A1]
**(b)**
\[\textstyle\sum \frac{1}{\alpha} = \frac{\sum \alpha\beta}{\alpha\beta\gamma} = \frac{4}{-3}\] [M1]
\[= -\tfrac43\] [A1]
**(c)** Each root satisfies \(x^3 = 2x^2 - 4x - 3\). Add the three equations:
\[S_3 = 2S_2 - 4S_1 - 3 \times 3\] [M1 A1]
\[S_3 = 2(-4) - 4(2) - 9 = -25\] [A1]
**Check** with an identity: \(\left(\sum \alpha\right)^3 - 3\sum \alpha \sum \alpha\beta + 3\alpha\beta\gamma = 8 - 24 - 9 = -25\).
:::

The answer to (a) is negative, so the roots cannot all be real. A cubic always has at least one real root (its graph must cross the x-axis), so this one has one real root and two complex conjugate roots.

:::exam Using the equation versus long identities
The identity \(\sum \alpha^3 = \left(\sum \alpha\right)^3 - 3\sum \alpha \sum \alpha\beta + 3\alpha\beta\gamma\) is easy to get wrong in an exam. The "add the equations" method needs nothing to be memorised, and mark schemes accept either. Show the line \(S_3 = \dots\) with letters before numbers: that line earns the method mark.
:::

### Harder symmetric functions

Two more tricks cover almost everything else an exam can ask.

- **Reciprocal powers.** Put each fraction over the common denominator \(\alpha\beta\gamma\) (or its square). For example \(\sum \dfrac{1}{\alpha\beta} = \dfrac{\gamma + \alpha + \beta}{\alpha\beta\gamma} = \dfrac{\sum \alpha}{\alpha\beta\gamma}\), and \(\sum \dfrac{1}{\alpha^2} = \dfrac{\sum \alpha^2\beta^2}{(\alpha\beta\gamma)^2}\).
- **The missing root.** In a cubic, \(\alpha + \beta = \sum \alpha - \gamma\). So an expression built from \(\alpha + \beta\), \(\beta + \gamma\), \(\gamma + \alpha\) becomes an expression in single roots.

:::eg The cubic \(x^3 + 3x^2 - x + 2 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Find (a) \(\sum \alpha^2\beta^2\), (b) \(\sum \dfrac{1}{\alpha^2}\), (c) \((\alpha + \beta)(\beta + \gamma)(\gamma + \alpha)\).
From the coefficients: \(\sum \alpha = -3\), \(\sum \alpha\beta = -1\), \(\alpha\beta\gamma = -2\).

(a) Square \(\sum \alpha\beta\): each \(\alpha^2\beta^2\) appears once, and every cross term contains \(\alpha\beta\gamma\) times a single root.
\[\begin{aligned}
\textstyle\sum \alpha^2\beta^2 &= \left(\textstyle\sum \alpha\beta\right)^2 - 2\alpha\beta\gamma\textstyle\sum \alpha \\
&= (-1)^2 - 2(-2)(-3) = -11
\end{aligned}\]
(b) Over the common denominator \((\alpha\beta\gamma)^2 = 4\):
\[\textstyle\sum \frac{1}{\alpha^2} = \frac{\sum \alpha^2\beta^2}{(\alpha\beta\gamma)^2} = -\frac{11}{4}\]
(c) Each bracket is the sum of all three roots minus the third: \(\alpha + \beta = -3 - \gamma\), and so on. So the product is \((-3 - \alpha)(-3 - \beta)(-3 - \gamma)\).

The cubic is \(p(x) = (x - \alpha)(x - \beta)(x - \gamma)\), so this product is exactly \(p(-3)\):
\[p(-3) = -27 + 27 + 3 + 2 = 5\]
:::

The last part used a neat idea: \((k - \alpha)(k - \beta)(k - \gamma)\) is just the monic cubic evaluated at \(x = k\). Divide by the leading coefficient first if it is not 1.

### Unknown coefficients

If you know something about the roots (they form an arithmetic progression, one is the sum of the others, one is complex), the relations give equations for the unknown coefficients.

:::eg (Exam style) The roots of \(x^3 - 9x^2 + kx - 24 = 0\) form an arithmetic progression. Find \(k\) and solve the equation.
Write the roots as \(\alpha - e\), \(\alpha\), \(\alpha + e\), where \(e\) is the common difference. Their sum is \(3\alpha = 9\), so \(\alpha = 3\) is a root. [B1]

Substitute \(x = 3\):
\[27 - 81 + 3k - 24 = 0\] [M1]
\[3k = 78, \quad k = 26\] [A1]
Divide by the known factor \(x - 3\) (this method mark depends on the first one):
\[x^3 - 9x^2 + 26x - 24 = (x - 3)(x^2 - 6x + 8)\] [M1]
\[= (x - 3)(x - 2)(x - 4)\]
The roots are 2, 3 and 4. [A1]

**Check**: they form an arithmetic progression and their product is 24, which matches \(-\tfrac{d}{a} = 24\).
:::

The second M1 is a **dependent method mark**, written DM1 in 9231 mark schemes: it is given only if the M1 before it was earned. Here, factorising with a wrong \(k\) earns nothing.

When a real polynomial has a complex root, its conjugate is also a root ([Complex numbers](#math.p3.complex)). The product of a conjugate pair is the real number \(|z|^2\), which makes the relations easy to use.

:::eg (Exam style) The equation \(x^3 + px^2 + qx + 10 = 0\), where \(p\) and \(q\) are real, has a root \(1 + 2\mathrm{i}\). Find the other two roots and the values of \(p\) and \(q\).
The coefficients are real, so \(1 - 2\mathrm{i}\) is also a root. [B1]

Let the third root be \(\gamma\). The pair has product \((1 + 2\mathrm{i})(1 - 2\mathrm{i}) = 1 + 4 = 5\) and sum 2.

Product of the roots:
\[5\gamma = -10, \quad \gamma = -2\] [M1 A1]
Sum and pairs:
\[\begin{aligned}
\textstyle\sum \alpha &= 2 + (-2) = 0 = -p \\
\textstyle\sum \alpha\beta &= 5 + (-2)(2) = 1 = q
\end{aligned}\] [M1]
So \(p = 0\) and \(q = 1\): the equation is \(x^3 + x + 10 = 0\). [A1]

**Check**: \((-2)^3 + (-2) + 10 = 0\).
:::

:::plot The curve y = x³ + x + 10 crosses the x-axis only once, at x = −2. The other two roots, 1 ± 2i, are complex, so they do not show on the graph.
--f "x**3+x+10" --label "y = x³ + x + 10" --x -3 2.5 --y -22 40 --pt "-2,0,(−2, 0)@nw" --legend tr
:::

The coefficients fix the symmetric sums even when you cannot see the roots. In the graph below the cubic is \(y = x^3 - 6x^2 + 11x - 6 + k\). Slide \(k\): only the constant term changes, so only the product of the roots changes. While the curve crosses the x-axis three times, read off the crossings and check that they still add to about 6. When it crosses only once, the other two roots have become a complex conjugate pair, and the three roots still add to exactly 6.

:::html
<div class="widget" data-w="graph" data-fns="x^3 - 6*x^2 + 11*x - 6 + k" data-x="-0.5,4.5" data-y="-3,3" data-params="k=0,-1.5,1.5,0.05" data-labels="y = x³ − 6x² + 11x − 6 + k"></div>
:::

### A real context

:::eg A storage container is a cuboid whose length, width and height, in metres, are the three roots of \(x^3 - 9x^2 + 23x - 14 = 0\). Without solving the equation, find (a) the total length of its 12 edges, (b) its surface area, (c) its volume, (d) the length of a diagonal from one corner to the opposite corner.
Let the edges be \(\alpha\), \(\beta\), \(\gamma\), so \(\sum \alpha = 9\), \(\sum \alpha\beta = 23\) and \(\alpha\beta\gamma = 14\).

(a) There are four edges of each length: \(4\sum \alpha = 36\) m.

(b) The six faces come in pairs of areas \(\alpha\beta\), \(\beta\gamma\), \(\gamma\alpha\): \(2\sum \alpha\beta = 46\,\mathrm{m^2}\).

(c) The volume is \(\alpha\beta\gamma = 14\,\mathrm{m^3}\).

(d) By Pythagoras in three dimensions, the diagonal is \(\sqrt{\alpha^2 + \beta^2 + \gamma^2}\):
\[\textstyle\sum \alpha^2 = 9^2 - 2 \times 23 = 35\]
The diagonal is \(\sqrt{35} = 5.92\) m (3 s.f.).

The roots are about 0.885, 3.25 and 4.86, none of them a nice number, so the relations really are the quick route.
:::

## Quartic equations

A quartic equation has four roots \(\alpha\), \(\beta\), \(\gamma\), \(\delta\) (delta). Expanding \(a(x - \alpha)(x - \beta)(x - \gamma)(x - \delta)\) gives the same pattern with one more line. \(\sum \alpha\beta\) now has six terms (every pair) and \(\sum \alpha\beta\gamma\) has four (every triple).

:::key Roots of a quartic
If \(\alpha\), \(\beta\), \(\gamma\), \(\delta\) are the roots of \(ax^4 + bx^3 + cx^2 + dx + e = 0\), then
\[\begin{aligned}
\textstyle\sum \alpha &= -\frac{b}{a} &\qquad \textstyle\sum \alpha\beta &= \frac{c}{a} \\
\textstyle\sum \alpha\beta\gamma &= -\frac{d}{a} &\qquad \alpha\beta\gamma\delta &= \frac{e}{a}
\end{aligned}\]
The pattern for any degree: the sum of the products of the roots taken \(k\) at a time is \((-1)^k \times\) (coefficient \(k\) places after the leading one) \(\div\) (leading coefficient). So the product of all the roots is \(+\frac{e}{a}\) for a quartic but \(-\frac{d}{a}\) for a cubic.
:::

The identities you met carry over: \(\sum \alpha^2 = \left(\sum \alpha\right)^2 - 2\sum \alpha\beta\) still holds, and
\[\textstyle\sum \frac{1}{\alpha} = \frac{\sum \alpha\beta\gamma}{\alpha\beta\gamma\delta}\]

:::eg The quartic \(3x^4 - 2x^3 + 5x - 6 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\), \(\delta\). Find \(\sum \alpha\), \(\sum \alpha\beta\), \(\sum \alpha\beta\gamma\), \(\alpha\beta\gamma\delta\) and \(\sum \alpha^2\).
Here \(a = 3\), \(b = -2\), \(c = 0\) (there is no \(x^2\) term), \(d = 5\), \(e = -6\).
\[\begin{aligned}
\textstyle\sum \alpha &= \tfrac23 &\qquad \textstyle\sum \alpha\beta &= 0 \\
\textstyle\sum \alpha\beta\gamma &= -\tfrac53 &\qquad \alpha\beta\gamma\delta &= -2
\end{aligned}\]
\[\textstyle\sum \alpha^2 = \left(\tfrac23\right)^2 - 2 \times 0 = \tfrac49\]
:::

:::eg (Exam style) The quartic equation \(x^4 + 2x^3 + 3x^2 - x + 6 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\), \(\delta\). (a) Find \(\sum \alpha^2\). (b) Deduce that the equation has at least two non-real roots. (c) Find \(\sum \dfrac{1}{\alpha}\).
**(a)** \(\sum \alpha = -2\) and \(\sum \alpha\beta = 3\).
\[\textstyle\sum \alpha^2 = (-2)^2 - 2 \times 3\] [M1]
\[= -2\] [A1]
**(b)** If all four roots were real, each \(\alpha^2\) would be at least 0 and so would their sum. The sum is \(-2 < 0\), so at least one root is non-real; non-real roots of a real polynomial come in conjugate pairs, so there are at least two. [B1]

**(c)** \(\sum \alpha\beta\gamma = -\tfrac{-1}{1} = 1\) and \(\alpha\beta\gamma\delta = 6\).
\[\textstyle\sum \frac{1}{\alpha} = \frac{\sum \alpha\beta\gamma}{\alpha\beta\gamma\delta} = \frac16\] [M1 A1]
:::

:::plot The quartic y = x⁴ + 2x³ + 3x² − x + 6 stays above the x-axis (its least value is about 5.92), so all four roots are non-real. Part (b) only promised at least two.
--f "x**4+2*x**3+3*x**2-x+6" --label "y = x⁴ + 2x³ + 3x² − x + 6" --x -1.5 2 --y 0 65 --pt "0.144,5.92,least value ≈ 5.92@se" --legend tr
:::

:::warn \(\sum \alpha^2 < 0\) proves something, \(\sum \alpha^2 > 0\) does not
A negative \(\sum \alpha^2\) proves that some roots are non-real. A positive value proves nothing: complex roots can still have a positive sum of squares. Never write "\(\sum \alpha^2 > 0\), so the roots are real".
:::

## Equations with related roots: substitution

Often you need an equation whose roots are related to the old ones: \(2\alpha, 2\beta, 2\gamma\), or \(\alpha + 1, \dots\), or \(\alpha^2, \dots\). You could find the new sum, pairs and product one by one, but a **substitution** builds the whole equation at once.

The idea: if \(y = 2x\), then whenever \(x\) is a root of the old equation, \(y\) is a root of the new one. So write the old \(x\) in terms of \(y\) and substitute.

:::steps
1. Write the new root in terms of the old: \(y = 2x\), \(y = x + 1\), \(y = \frac{1}{x}\), \(y = x^2\), …
2. Rearrange to make \(x\) the subject: \(x = \frac{y}{2}\), \(x = y - 1\), \(x = \frac{1}{y}\), \(x = \sqrt{y}\), …
3. Substitute into the old equation.
4. Clear fractions (or roots) and simplify. Write the answer in \(y\), or rename \(y\) as \(x\) if the question asks for an equation in \(x\).
:::

:::eg The cubic \(x^3 - 4x^2 + x + 6 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Find a cubic equation with roots \(2\alpha\), \(2\beta\), \(2\gamma\).
Let \(y = 2x\), so \(x = \tfrac{y}{2}\). Substitute:
\[\frac{y^3}{8} - \frac{4y^2}{4} + \frac{y}{2} + 6 = 0\]
Multiply by 8:
\[y^3 - 8y^2 + 4y + 48 = 0\]
**Check**: the new sum should be \(2\sum \alpha = 2 \times 4 = 8\), and \(-\tfrac{-8}{1} = 8\).
:::

For **reciprocals** the substitution \(x = \frac{1}{y}\) reverses the order of the coefficients: \(ax^3 + bx^2 + cx + d = 0\) becomes \(dy^3 + cy^2 + by + a = 0\) once you multiply by \(y^3\).

For **squares** the substitution is \(x = \sqrt{y}\). Collect the odd powers of \(x\) on one side, because they leave a \(\sqrt{y}\), then square both sides.

:::eg The cubic \(x^3 + 2x^2 - 3x + 5 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Find a cubic equation with roots \(\alpha^2\), \(\beta^2\), \(\gamma^2\), and hence find \(\alpha^4 + \beta^4 + \gamma^4\).
Separate the odd and even powers of \(x\):
\[x^3 - 3x = -(2x^2 + 5), \quad\text{so}\quad x(x^2 - 3) = -(2x^2 + 5)\]
Put \(x = \sqrt{y}\), so \(x^2 = y\):
\[\sqrt{y}\,(y - 3) = -(2y + 5)\]
Square both sides:
\[\begin{aligned}
y(y - 3)^2 &= (2y + 5)^2 \\
y^3 - 6y^2 + 9y &= 4y^2 + 20y + 25 \\
y^3 - 10y^2 - 11y - 25 &= 0
\end{aligned}\]
The roots of this equation are \(\alpha^2\), \(\beta^2\), \(\gamma^2\). Their sum of squares is \(\sum \alpha^4\):
\[\textstyle\sum \alpha^4 = 10^2 - 2(-11) = 122\]
**Check**: the new sum, 10, should equal \(\sum \alpha^2 = (-2)^2 - 2(-3) = 10\).
:::

The missing-root idea gives a substitution too. If the new roots are \(\beta + \gamma\), \(\gamma + \alpha\), \(\alpha + \beta\), each one is \(\sum \alpha - x\) for an old root \(x\).

:::eg The cubic \(x^3 + 3x^2 - x + 2 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Find a cubic equation with roots \(\beta + \gamma\), \(\gamma + \alpha\), \(\alpha + \beta\).
Here \(\sum \alpha = -3\), so each new root is \(y = -3 - x\), and \(x = -3 - y = -(y + 3)\).

Substitute:
\[-(y + 3)^3 + 3(y + 3)^2 + (y + 3) + 2 = 0\]
Expand each bracket:
\[\begin{aligned}
-(y^3 + 9y^2 + 27y + 27) + (3y^2 + 18y + 27) \\
+ y + 3 + 2 = 0 \\
-y^3 - 6y^2 - 8y + 5 = 0
\end{aligned}\]
Multiply by \(-1\): \(y^3 + 6y^2 + 8y - 5 = 0\).

**Check**: the new product is 5, matching \((\alpha + \beta)(\beta + \gamma)(\gamma + \alpha) = 5\) from the previous section, and the new sum is \(2\sum \alpha = -6\).
:::

:::warn Substitute the inverse
If the new roots are \(y = 2x + 1\), you substitute \(x = \dfrac{y - 1}{2}\), not \(2x + 1\). Students who substitute \(y\) itself get an equation whose roots are \(\dfrac{\alpha - 1}{2}\), the wrong way round. Check your answer with the new sum of roots.
:::

:::eg (Exam style) The cubic equation \(x^3 - 3x^2 + 5x - 2 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). (a) Find a cubic equation whose roots are \(2\alpha + 1\), \(2\beta + 1\), \(2\gamma + 1\). (b) Find the value of \((2\alpha + 1)^2 + (2\beta + 1)^2 + (2\gamma + 1)^2\). (c) Find the value of \(\dfrac{1}{2\alpha + 1} + \dfrac{1}{2\beta + 1} + \dfrac{1}{2\gamma + 1}\).
**(a)** Let \(y = 2x + 1\), so \(x = \dfrac{y - 1}{2}\). [B1]
\[\frac{(y - 1)^3}{8} - \frac{3(y - 1)^2}{4} + \frac{5(y - 1)}{2} - 2 = 0\]
Multiply by 8:
\[(y - 1)^3 - 6(y - 1)^2 + 20(y - 1) - 16 = 0\] [M1]
\[\begin{aligned}
&y^3 - 3y^2 + 3y - 1 - 6y^2 + 12y - 6 \\
&\quad + 20y - 20 - 16 = 0
\end{aligned}\]
\[y^3 - 9y^2 + 35y - 43 = 0\] [A1]
**(b)** For the new roots, \(\sum y = 9\) and \(\sum y_1y_2 = 35\).
\[\textstyle\sum y^2 = 9^2 - 2 \times 35\] [M1]
\[= 11\] [A1] (FT)
**(c)** The product of the new roots is 43.
\[\textstyle\sum \frac{1}{y} = \frac{35}{43}\] [M1 A1]
:::

The A1 (FT) in (b) means "follow through", written A1 FT in mark schemes: a student with a wrong equation in (a) who uses it correctly in (b) still gets this mark.

:::board
In the UK A Levels (AQA, Edexcel, OCR), roots of polynomials are part of Further Mathematics core pure content, for quadratics, cubics and quartics as here; none of this is in single A Level Mathematics. The ideas, notation \(\sum \alpha\) and the substitution method are the same.
:::

:::exam What MF19 gives you
Nothing in this chapter is on the formula list: learn the relations for degrees 2, 3 and 4 and the identity for \(\sum \alpha^2\). The syllabus says substitutions are **not** given for the easiest cases (reciprocals, squares, simple linear functions such as \(2\alpha + 1\)), so you must choose them yourself; harder ones are given. Questions often say "find the value of" a symmetric sum: give an exact fraction, not a decimal.
:::

:::eg Spot the error: the cubic \(2x^3 + 3x^2 - 4x + 1 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). Find (a) \(\sum \alpha^2\), (b) \(\sum \dfrac{1}{\alpha}\), each for 2 marks.
A student wrote this answer.

Line 1: \(\sum \alpha = -\tfrac32\), \(\sum \alpha\beta = -2\), \(\alpha\beta\gamma = \tfrac12\)
Line 2: \(\sum \alpha^2 = \tfrac94 - 2(-2) = \tfrac{25}{4}\)
Line 3: \(\sum \dfrac{1}{\alpha} = \dfrac{-2}{1/2} = -4\)

Line 2 is correct and earns both marks of (a). [M1] [A1]

**Line 3 uses the right method but loses the accuracy mark.** [M1] [A0] The slip is in line 1: for a cubic the product of the roots is \(-\dfrac{d}{a}\), so \(\alpha\beta\gamma = -\tfrac12\), not \(\tfrac12\). The student scores 3 out of 4.

Correct line 3: \(\sum \dfrac{1}{\alpha} = \dfrac{-2}{-1/2} = 4\). [A1]

**Check** with reciprocals: \(x = \frac1y\) turns the equation into \(y^3 - 4y^2 + 3y + 2 = 0\), whose roots add to 4.
:::

:::try Start easy, finish at exam standard
Q: The roots of \(x^2 + 6x - 2 = 0\) are \(\alpha\) and \(\beta\). Find \(\alpha + \beta\), \(\alpha\beta\) and \(\alpha^2 + \beta^2\).
A: \(\alpha + \beta = -6\), \(\alpha\beta = -2\), and \(\alpha^2 + \beta^2 = 36 - 2(-2) = 40\).
Q: The roots of \(3x^2 - x + 4 = 0\) are \(\alpha\) and \(\beta\). Find \(\dfrac{1}{\alpha} + \dfrac{1}{\beta}\) and \(\dfrac{\alpha}{\beta} + \dfrac{\beta}{\alpha}\).
A: \(\alpha + \beta = \tfrac13\), \(\alpha\beta = \tfrac43\). So \(\dfrac{1}{\alpha} + \dfrac{1}{\beta} = \dfrac{1/3}{4/3} = \dfrac14\).
Next, \(\alpha^2 + \beta^2 = \tfrac19 - \tfrac83 = -\tfrac{23}{9}\), so
\[\frac{\alpha}{\beta} + \frac{\beta}{\alpha} = \frac{\alpha^2 + \beta^2}{\alpha\beta} = \frac{-23/9}{4/3} = -\frac{23}{12}\]
Q: The roots of \(x^2 - 5x + 3 = 0\) are \(\alpha\) and \(\beta\). Find a quadratic equation with roots \(\alpha + 2\) and \(\beta + 2\).
A: New sum: \(5 + 4 = 9\). New product: \(\alpha\beta + 2(\alpha + \beta) + 4 = 3 + 10 + 4 = 17\). The equation is \(x^2 - 9x + 17 = 0\).
Q: The roots of \(4x^3 - 8x^2 + x + 3 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Write down \(\sum \alpha\), \(\sum \alpha\beta\), \(\alpha\beta\gamma\), and find \(\sum \alpha^2\).
A: \(\sum \alpha = 2\), \(\sum \alpha\beta = \tfrac14\), \(\alpha\beta\gamma = -\tfrac34\). Then \(\sum \alpha^2 = 4 - \tfrac12 = \tfrac72\).
Q: The roots of \(x^3 + 4x^2 - 2x + 7 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Find \(\sum \dfrac{1}{\alpha}\) and \(\sum \alpha^2\).
A: \(\sum \alpha = -4\), \(\sum \alpha\beta = -2\), \(\alpha\beta\gamma = -7\). So \(\sum \dfrac{1}{\alpha} = \dfrac{-2}{-7} = \dfrac27\) and \(\sum \alpha^2 = 16 + 4 = 20\).
Q: The roots of \(x^3 - 4x^2 + 2x + 5 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Find \((\alpha + \beta)(\beta + \gamma)(\gamma + \alpha)\).
A: \(\sum \alpha = 4\), so the product is \((4 - \alpha)(4 - \beta)(4 - \gamma) = p(4)\), where \(p(x) = x^3 - 4x^2 + 2x + 5\). \(p(4) = 64 - 64 + 8 + 5 = 13\).
Q: The roots of \(2x^4 + 3x^3 - x^2 + 5x - 4 = 0\) are \(\alpha\), \(\beta\), \(\gamma\), \(\delta\). Write down the four symmetric sums and find \(\sum \alpha^2\).
A: \(\sum \alpha = -\tfrac32\), \(\sum \alpha\beta = -\tfrac12\), \(\sum \alpha\beta\gamma = -\tfrac52\), \(\alpha\beta\gamma\delta = -2\). Then \(\sum \alpha^2 = \tfrac94 + 1 = \tfrac{13}{4}\).
Q: The roots of \(x^3 - 2x^2 + x - 5 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Find a cubic equation with roots \(3\alpha\), \(3\beta\), \(3\gamma\).
A: Put \(x = \tfrac{y}{3}\): \(\dfrac{y^3}{27} - \dfrac{2y^2}{9} + \dfrac{y}{3} - 5 = 0\). Multiply by 27: \(y^3 - 6y^2 + 9y - 135 = 0\).
Q: The roots of \(x^3 + 2x^2 - 7x + 3 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Find a cubic equation with roots \(\dfrac{1}{\alpha}\), \(\dfrac{1}{\beta}\), \(\dfrac{1}{\gamma}\).
A: Put \(x = \tfrac1y\) and multiply by \(y^3\): \(1 + 2y - 7y^2 + 3y^3 = 0\), that is \(3y^3 - 7y^2 + 2y + 1 = 0\).
Q: The roots of \(x^3 - 7x^2 + kx - 8 = 0\) form a geometric progression. Find \(k\) and the roots.
A: Write the roots as \(\dfrac{a}{r}\), \(a\), \(ar\). Their product is \(a^3 = 8\), so \(a = 2\) is a root. Then \(8 - 28 + 2k - 8 = 0\), so \(k = 14\). [M1 A1]
\(x^3 - 7x^2 + 14x - 8 = (x - 2)(x^2 - 5x + 4) = (x - 2)(x - 1)(x - 4)\): the roots are 1, 2, 4. [M1 A1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ The roots of \(2x^2 + 3x - 6 = 0\) are \(\alpha\) and \(\beta\). Find the value of \(\alpha^2 + \beta^2\).
A: \(\alpha + \beta = -\tfrac32\) and \(\alpha\beta = -3\). [B1] \(\alpha^2 + \beta^2 = \tfrac94 - 2(-3)\) [M1] \(= \tfrac{33}{4}\). [A1]
Q: [4 marks] ★ The roots of \(x^3 - 5x^2 + 2x + 4 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Find \(\sum \alpha^2\) and \(\sum \dfrac{1}{\alpha}\).
A: \(\sum \alpha = 5\), \(\sum \alpha\beta = 2\), \(\alpha\beta\gamma = -4\). [B1]
\(\sum \alpha^2 = 25 - 4\) [M1] \(= 21\). [A1]
\(\sum \dfrac{1}{\alpha} = \dfrac{2}{-4} = -\dfrac12\). [B1]
Q: [4 marks] ★★ The roots of \(x^4 - 3x^3 + 2x^2 + x - 4 = 0\) are \(\alpha\), \(\beta\), \(\gamma\), \(\delta\). Find \(\sum \alpha^2\) and \(\sum \dfrac{1}{\alpha}\).
A: \(\sum \alpha = 3\), \(\sum \alpha\beta = 2\), so \(\sum \alpha^2 = 9 - 4\) [M1] \(= 5\). [A1]
\(\sum \alpha\beta\gamma = -1\) and \(\alpha\beta\gamma\delta = -4\), so \(\sum \dfrac{1}{\alpha} = \dfrac{-1}{-4}\) [M1] \(= \dfrac14\). [A1]
Q: [3 marks] ★★ Show that the equation \(x^4 - 2x^3 + 4x^2 + 3x + 1 = 0\) cannot have four real roots.
A: \(\sum \alpha = 2\) and \(\sum \alpha\beta = 4\), so \(\sum \alpha^2 = 4 - 8\) [M1] \(= -4\). [A1]
A sum of squares of real numbers cannot be negative, so the roots are not all real. [B1]
Q: [5 marks] ★★ The equation \(x^3 - 6x^2 + kx - 6 = 0\) has one root equal to the sum of the other two. Find \(k\) and solve the equation.
A: Let the roots be \(\alpha\), \(\beta\), \(\alpha + \beta\). The sum of all three is \(2(\alpha + \beta) = 6\), so \(\alpha + \beta = 3\) and 3 is a root. [B1]
\(27 - 54 + 3k - 6 = 0\) [M1], so \(k = 11\). [A1]
\(x^3 - 6x^2 + 11x - 6 = (x - 3)(x^2 - 3x + 2)\) [M1] (dependent), so the roots are 1, 2, 3. [A1]
Q: [5 marks] ★★ The roots of \(x^3 - x^2 + 3x + 2 = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Use the substitution \(y = x^2\) to find a cubic equation with roots \(\alpha^2\), \(\beta^2\), \(\gamma^2\). Hence find \(\sum \alpha^4\).
A: Odd powers on one side: \(x(x^2 + 3) = x^2 - 2\). Put \(x = \sqrt{y}\): \(\sqrt{y}\,(y + 3) = y - 2\). [M1]
Square: \(y(y + 3)^2 = (y - 2)^2\) [M1], so
\[\begin{aligned}
y^3 + 6y^2 + 9y &= y^2 - 4y + 4 \\
y^3 + 5y^2 + 13y - 4 &= 0
\end{aligned}\] [A1]
\(\sum \alpha^4 = (-5)^2 - 2(13)\) [M1] \(= -1\). [A1]
Q: [8 marks] (#math.p3.complex) ★★★ The cubic equation \(x^3 + ax^2 + bx + 26 = 0\), where \(a\) and \(b\) are real, has a root \(-3 + 2\mathrm{i}\). (a) Write down a second root, giving a reason. (b) Find the third root and the values of \(a\) and \(b\). (c) Find the value of \(\alpha^2 + \beta^2 + \gamma^2\), where \(\alpha\), \(\beta\), \(\gamma\) are the three roots.
H: Non-real roots of a polynomial with real coefficients come in conjugate pairs.
H: The product of the conjugate pair is \(|-3 + 2\mathrm{i}|^2 = 13\), and their sum is \(-6\). Use \(\alpha\beta\gamma = -\tfrac{d}{a}\) first.
H: For (c), use \(\left(\sum \alpha\right)^2 - 2\sum \alpha\beta\) with the values of \(a\) and \(b\) you found.
A: (a) \(-3 - 2\mathrm{i}\), because the coefficients are real, so non-real roots occur in conjugate pairs. [B1]
(b) Product of the pair \(= 9 + 4 = 13\), so \(13\gamma = -26\) [M1] and \(\gamma = -2\). [A1]
\(\sum \alpha = -6 - 2 = -8 = -a\), so \(a = 8\). [M1 A1]
\(\sum \alpha\beta = 13 + (-2)(-6) = 25 = b\). [A1]
(c) \(\sum \alpha^2 = 8^2 - 2 \times 25\) [M1] \(= 14\). [A1]
Q: [9 marks] (#math.p3.algebra) ★★★ The cubic equation \(x^3 + 3x^2 - 2x - 1 = 0\) has roots \(\alpha\), \(\beta\), \(\gamma\). (a) Use the substitution \(y = \dfrac{1}{x + 1}\) to show that the equation with roots \(\dfrac{1}{\alpha + 1}\), \(\dfrac{1}{\beta + 1}\), \(\dfrac{1}{\gamma + 1}\) is \(3y^3 - 5y^2 + 1 = 0\). (b) Write down \(\sum \dfrac{1}{\alpha + 1}\). (c) Find \(\sum \dfrac{1}{(\alpha + 1)^2}\). (d) Find \(\sum \dfrac{1}{(\alpha + 1)^3}\).
H: Make \(x\) the subject: \(x = \dfrac{1}{y} - 1 = \dfrac{1 - y}{y}\). Substitute, then multiply every term by \(y^3\).
H: The new equation has no \(y\) term, so \(\sum y_1y_2 = 0\).
H: For (d), use \(3S_3 - 5S_2 + 0 \times S_1 + 1 \times S_0 = 0\) with \(S_0 = 3\).
A: (a) \(x = \dfrac{1 - y}{y}\). [B1]
\[\frac{(1 - y)^3}{y^3} + \frac{3(1 - y)^2}{y^2} - \frac{2(1 - y)}{y} - 1 = 0\]
Multiply by \(y^3\):
\[(1 - y)^3 + 3y(1 - y)^2 - 2y^2(1 - y) - y^3 = 0\] [M1]
\[\begin{aligned}
&1 - 3y + 3y^2 - y^3 + 3y - 6y^2 + 3y^3 \\
&\quad - 2y^2 + 2y^3 - y^3 = 0
\end{aligned}\]
which simplifies to \(3y^3 - 5y^2 + 1 = 0\). [A1]
(b) \(\sum y = \dfrac53\). [B1]
(c) \(\sum y^2 = \left(\tfrac53\right)^2 - 2 \times 0\) [M1] \(= \dfrac{25}{9}\). [A1]
(d) \(3S_3 - 5S_2 + S_0 = 0\), so \(3S_3 = 5S_2 - 3\). [M1]
\(3S_3 = \dfrac{125}{9} - \dfrac{27}{9} = \dfrac{98}{9}\) [A1], so \(S_3 = \dfrac{98}{27}\). [A1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The roots of \(x^3 + ax^2 + bx + c = 0\), where \(a\), \(b\), \(c\) are non-zero, are in geometric progression. Prove that \(b^3 = a^3c\).
H: Write the roots as \(\dfrac{\alpha}{r}\), \(\alpha\), \(\alpha r\). What does the product give?
H: Compare \(\sum \alpha\beta\) with \(\alpha \times \sum \alpha\): they are equal for roots in geometric progression.
A: Let the roots be \(\dfrac{\alpha}{r}\), \(\alpha\), \(\alpha r\). Their product is \(\alpha^3 = -c\). [B1]
Their sum is \(\alpha\left(\dfrac1r + 1 + r\right) = -a\). [B1]
The pairs give
\[\textstyle\sum \alpha\beta = \alpha^2\left(\frac1r + r + 1\right) = b\] [M1]
so \(b = \alpha \times \alpha\left(\dfrac1r + 1 + r\right) = \alpha(-a)\), and \(\alpha = -\dfrac{b}{a}\). [A1]
Then \(\alpha^3 = -c\) gives \(-\dfrac{b^3}{a^3} = -c\) [M1], so \(b^3 = a^3c\). [A1]
Q: [6 marks] ★★★ Find the values of \(k\) for which \(x^3 - 3x + k = 0\) has a repeated root, and solve the equation in each case.
H: Call the roots \(\alpha\), \(\alpha\), \(\beta\) and write down the three relations.
H: The sum gives \(\beta = -2\alpha\). Put that into \(\sum \alpha\beta = -3\).
A: Roots \(\alpha\), \(\alpha\), \(\beta\): \(2\alpha + \beta = 0\), \(\alpha^2 + 2\alpha\beta = -3\), \(\alpha^2\beta = -k\). [M1]
So \(\beta = -2\alpha\) and \(\alpha^2 - 4\alpha^2 = -3\), giving \(\alpha^2 = 1\). [M1 A1]
If \(\alpha = 1\), \(\beta = -2\) and \(k = 2\): \(x^3 - 3x + 2 = (x - 1)^2(x + 2)\). [A1]
If \(\alpha = -1\), \(\beta = 2\) and \(k = -2\): \(x^3 - 3x - 2 = (x + 1)^2(x - 2)\). [A1]
So \(k = 2\) or \(k = -2\). [A1]
:::

:::quiz
? What is the sum of the roots of \(3x^3 - 6x^2 + x - 4 = 0\)?
+ \(2\)
- \(-2\)
- \(6\)
- \(-6\)
> \(\sum \alpha = -\dfrac{b}{a} = -\dfrac{-6}{3} = 2\). Answering \(-2\) forgets the minus sign in the rule, and \(\pm 6\) forgets to divide by the leading coefficient 3.
? What is the product of the roots of \(2x^3 + 5x^2 - x + 8 = 0\)?
- \(4\)
+ \(-4\)
- \(8\)
- \(-\dfrac12\)
> For a cubic, \(\alpha\beta\gamma = -\dfrac{d}{a} = -\dfrac{8}{2} = -4\). The answer 4 uses the quartic sign, 8 forgets to divide, and \(-\dfrac12\) uses the \(x\) coefficient.
? Three roots have \(\sum \alpha = 3\) and \(\sum \alpha\beta = 5\). What is \(\sum \alpha^2\)?
+ \(-1\)
- \(4\)
- \(19\)
- It cannot be negative, so the data are impossible
> \(\sum \alpha^2 = 3^2 - 2 \times 5 = -1\). The answer 4 forgets the factor 2. A negative value is possible: it shows two of the roots are complex.
? What is the product of the roots of \(x^4 - 3x^2 + 7 = 0\)?
+ \(7\)
- \(-7\)
- \(-3\)
- \(0\)
> For a quartic the product is \(+\dfrac{e}{a} = 7\). The sign is minus only for odd degree; \(-3\) is the coefficient of \(x^2\), which gives \(\sum \alpha\beta\).
? The roots of \(ax^3 + bx^2 + cx + d = 0\) are \(\alpha\), \(\beta\), \(\gamma\). Which equation has roots \(\dfrac1\alpha\), \(\dfrac1\beta\), \(\dfrac1\gamma\)?
- \(ax^3 - bx^2 + cx - d = 0\)
+ \(dx^3 + cx^2 + bx + a = 0\)
- \(\dfrac{x^3}{a} + \dfrac{x^2}{b} + \dfrac{x}{c} + \dfrac1d = 0\)
- \(ax^3 + bx^2 + cx + d = 0\) with \(x\) replaced by \(x^{-1}\) and nothing else
> Substitute \(x = \dfrac1y\) and multiply by \(y^3\): the coefficients reverse. Changing alternate signs gives roots \(-\alpha\), and taking reciprocals of the coefficients means nothing.
? To find an equation with roots \(\alpha^2\), \(\beta^2\), \(\gamma^2\), what do you substitute into the original equation?
- \(x = y^2\)
+ \(x = \sqrt{y}\), after putting the odd powers of \(x\) on one side
- \(y = \sqrt{x}\)
- \(x = 2y\)
> The new root is \(y = x^2\), so substitute the inverse, \(x = \sqrt{y}\), then square to remove the root. Substituting \(x = y^2\) gives an equation whose roots are the square roots of the old ones.
:::

:::checklist What you can now do
- [ ] I can state the relations between the roots and coefficients of quadratic, cubic and quartic equations, with the right signs.
- [ ] I can evaluate symmetric functions such as \(\sum \alpha^2\), \(\sum \dfrac{1}{\alpha}\) and \(\sum \alpha^2\beta^2\) from the coefficients.
- [ ] I can use the equation itself to find sums of powers such as \(\sum \alpha^3\).
- [ ] I can find unknown coefficients from facts about the roots: a progression, a root equal to the sum of the others, a complex root.
- [ ] I can use a negative \(\sum \alpha^2\) to show that an equation has non-real roots.
- [ ] I can choose and use a substitution to find an equation whose roots are related to the original roots (linear, reciprocal, square).
- [ ] I can use a transformed equation to find harder sums such as \(\sum \alpha^4\) or \(\sum \dfrac{1}{2\alpha + 1}\).
:::

:::recap
- Quadratic \(ax^2 + bx + c = 0\): \(\alpha + \beta = -\dfrac{b}{a}\), \(\alpha\beta = \dfrac{c}{a}\).
- Cubic \(ax^3 + bx^2 + cx + d = 0\): \(\sum \alpha = -\dfrac{b}{a}\), \(\sum \alpha\beta = \dfrac{c}{a}\), \(\alpha\beta\gamma = -\dfrac{d}{a}\).
- Quartic: \(\sum \alpha = -\dfrac{b}{a}\), \(\sum \alpha\beta = \dfrac{c}{a}\), \(\sum \alpha\beta\gamma = -\dfrac{d}{a}\), \(\alpha\beta\gamma\delta = \dfrac{e}{a}\). Signs alternate, starting with minus.
- \(\sum \alpha^2 = \left(\sum \alpha\right)^2 - 2\sum \alpha\beta\); \(\sum \dfrac{1}{\alpha}\) = (sum of products of all but one root) ÷ (product of all roots).
- Sums of powers: every root satisfies the equation, so \(aS_{n+3} + bS_{n+2} + cS_{n+1} + dS_n = 0\), with \(S_0 = 3\) for a cubic.
- A negative \(\sum \alpha^2\) means some roots are non-real; non-real roots of a real polynomial come in conjugate pairs.
- Related roots: write \(y\) in terms of \(x\), make \(x\) the subject, substitute, clear fractions. Reciprocals reverse the coefficients; for squares, put odd powers on one side and square.
- Check every new equation with its sum of roots.
:::

:::links
- watch: [Roots and coefficients of a cubic](https://www.examsolutions.net/tutorials/relationships-roots-coefficients-cubic-equation/) · ExamSolutions · the cubic relations and symmetric functions, step by step
- watch: [Roots and coefficients of a quartic](https://www.examsolutions.net/tutorials/relationships-roots-coefficients-quartic-equation/) · ExamSolutions · the same ideas one degree higher
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · the "roots of polynomial equations" booklet has graded questions with answers
- practise: [Roots of polynomials exam questions](https://www.savemyexams.com/a-level/further-maths/edexcel/17/core-pure/topic-questions/further-algebra-and-functions/roots-of-polynomials/exam-questions/) · Save My Exams · Edexcel questions on the same skills [paid]
- explore: [Polynomials station](https://undergroundmathematics.org/polynomials) · Underground Mathematics · rich problems about roots and coefficients
- papers: [9231 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp1/) · Physics & Maths Tutor · real Paper 1 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Summation of series](#math.fm.series) uses formulas for \(\sum r\), \(\sum r^2\) and \(\sum r^3\), and the method of differences, to add up long series exactly.
