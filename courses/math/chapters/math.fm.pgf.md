@chapter math.fm.pgf
@title Probability generating functions
@level fm
@paper CAIE 9231 Paper 4
@time 5–6 hours
@summary A probability generating function packs a whole discrete distribution into one function of t. You will construct it from a table and for the uniform, binomial, geometric and Poisson distributions, read probabilities from its coefficients, find means and variances by differentiating, find unknown constants, and use the fact that the PGF of a sum of independent variables is the product of their PGFs.
:::why
Adding independent random variables is awkward with probability tables: you have to sum over every way of making each total. A probability generating function (PGF) turns that sum into a product, and turns means and variances into derivatives. It is the same trick as turning multiplication into addition with logarithms: change the form of the problem so the difficult operation becomes an easy one. PGFs are also the quickest way to show, for instance, that the sum of two independent Poisson variables is again Poisson.
:::

**Before you start**, you need expected value, variance, the binomial and geometric distributions from [Discrete random variables: binomial and geometric](#math.s1.drv), the Poisson distribution from [The Poisson distribution](#math.s2.poisson), the binomial theorem and the sum to infinity of a geometric progression from [Series: binomial expansion and progressions](#math.p1.series), the series for \(\mathrm{e}^x\) from [Further differentiation and Maclaurin series](#math.fm.diff), and the chain rule from [Further differentiation](#math.p3.diff).

:::try Warm-up
Q: Find \(1 + \tfrac13 + \tfrac19 + \dots\) (from [Series: binomial expansion and progressions](#math.p1.series))
A: A geometric progression with \(a = 1\) and \(r = \tfrac13\), so the sum to infinity is \(\dfrac{1}{1 - \tfrac13} = \dfrac32\).
Q: Expand \((0.6 + 0.4t)^2\). (from [Series: binomial expansion and progressions](#math.p1.series))
A: \(0.36 + 2(0.6)(0.4)t + 0.16t^2 = 0.36 + 0.48t + 0.16t^2\).
Q: Differentiate \(\mathrm{e}^{3(t - 1)}\) and evaluate at \(t = 1\). (from [Further differentiation](#math.p3.diff))
A: By the chain rule the derivative is \(3\mathrm{e}^{3(t - 1)}\), which is \(3\) at \(t = 1\).
:::

## The probability generating function

Suppose \(X\) takes the whole-number values \(0, 1, 2, \dots\) with probabilities \(p_0, p_1, p_2, \dots\). Make a polynomial (or power series) with one term for each value, using the probability as the coefficient and the value as the power of \(t\):
\[p_0 + p_1 t + p_2 t^2 + \dots\]
The variable \(t\) is a dummy: it just holds each probability in its own slot, like the place holders in a number. The powers of \(t\) record the values of \(X\) and the coefficients record the probabilities.

:::def Probability generating function (PGF)
For a discrete random variable \(X\) taking integer values, the PGF is the function of \(t\)
\[G_X(t) = \mathrm{E}\left(t^X\right) = \sum_x \mathrm{P}(X = x)\,t^x\]
the sum being over all values \(x\) that \(X\) can take. It is written \(G(t)\) when it is clear which variable is meant.
:::

The two forms of the definition say the same thing: \(\mathrm{E}(t^X)\) is "the expected value of \(t^X\)", found as for any function of \(X\) by multiplying each value of \(t^x\) by its probability and adding.

:::eg The random variable \(X\) has the distribution below. Write down \(G_X(t)\), and check that \(G_X(1) = 1\).

| \(x\) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| \(\mathrm{P}(X = x)\) | 0.1 | 0.3 | 0.4 | 0.2 |

Multiply each probability by \(t\) to the power of its value:
\[G_X(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3\]
At \(t = 1\) every power of \(t\) is 1, so \(G_X(1) = 0.1 + 0.3 + 0.4 + 0.2 = 1\).
:::

Notice the constant term. The value \(x = 0\) contributes \(\mathrm{P}(X = 0) \times t^0 = \mathrm{P}(X = 0)\), so it is a constant, not zero. Leaving it out is a common slip.

:::key Properties of a PGF
- \(G(1) = \sum \mathrm{P}(X = x) = 1\), because the probabilities add to 1.
- \(G(0) = \mathrm{P}(X = 0)\).
- The coefficient of \(t^r\) in \(G(t)\) is \(\mathrm{P}(X = r)\). By differentiating, \(\mathrm{P}(X = r) = \dfrac{G^{(r)}(0)}{r!}\), where \(G^{(r)}\) is the \(r\)th derivative.
- A PGF determines the distribution completely: two variables with the same PGF have the same distribution.
:::

If \(X\) can take negative integer values, the PGF has negative powers of \(t\): \(t^{-1}\) belongs to \(X = -1\). Such a PGF is still evaluated at \(t = 1\) and still gives \(G(1) = 1\), and the rest of the chapter works unchanged. You will see one in the exam examples below.

:::eg The PGF of \(X\) is \(G(t) = \dfrac{t}{2 - t}\) for \(|t| < 2\). Find \(\mathrm{P}(X = 1)\), \(\mathrm{P}(X = 2)\) and \(\mathrm{P}(X = 3)\).
Write it as a series in \(t\). Since \(\dfrac{t}{2 - t} = \dfrac{t}{2}\left(1 - \dfrac{t}{2}\right)^{-1}\), the sum to infinity of a geometric progression gives
\[G(t) = \frac{t}{2}\left(1 + \frac{t}{2} + \frac{t^2}{4} + \dots\right) = \frac{t}{2} + \frac{t^2}{4} + \frac{t^3}{8} + \dots\]
The coefficients give \(\mathrm{P}(X = 1) = \tfrac12\), \(\mathrm{P}(X = 2) = \tfrac14\), \(\mathrm{P}(X = 3) = \tfrac18\).

**Check** with differentiation: \(G'(t) = \dfrac{2}{(2 - t)^2}\), so \(G'(0) = \tfrac12 = \mathrm{P}(X = 1)\), as above.
:::

:::eg Three fair coins are tossed and \(X\) is the number of heads. Write down \(G_X(t)\) from the probabilities, then show that it equals \(\left(\tfrac12 + \tfrac12 t\right)^3\).

| \(x\) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| \(\mathrm{P}(X = x)\) | \(\tfrac18\) | \(\tfrac38\) | \(\tfrac38\) | \(\tfrac18\) |

\[G_X(t) = \tfrac18 + \tfrac38 t + \tfrac38 t^2 + \tfrac18 t^3\]
By the binomial theorem \(\left(\tfrac12 + \tfrac12 t\right)^3 = \tfrac18\left(1 + t\right)^3 = \tfrac18\left(1 + 3t + 3t^2 + t^3\right)\), which is the same. The PGF has factorised into a cube because \(X\) is the sum of three independent single tosses, each with PGF \(\tfrac12 + \tfrac12 t\). That is exactly the product rule you meet later in this chapter.
:::

:::eg The PGF of \(X\) is \(G(t) = \dfrac{1}{2 - t}\) for \(|t| < 2\). Use differentiation at \(t = 0\) to find \(\mathrm{P}(X = 0)\), \(\mathrm{P}(X = 1)\) and \(\mathrm{P}(X = 2)\), and check with a series.
\(\mathrm{P}(X = 0) = G(0) = \tfrac12\).

\[G'(t) = \frac{1}{(2 - t)^2} \qquad G''(t) = \frac{2}{(2 - t)^3}\]
\[\mathrm{P}(X = 1) = G'(0) = \tfrac14 \qquad \mathrm{P}(X = 2) = \frac{G''(0)}{2!} = \frac{2/8}{2} = \tfrac18\]
**Check**: \(\dfrac{1}{2 - t} = \tfrac12\left(1 - \tfrac t2\right)^{-1} = \tfrac12 + \tfrac14 t + \tfrac18 t^2 + \dots\), the same three coefficients. This is the number of failures before the first success when \(p = \tfrac12\).
:::

## PGFs of the standard distributions

Every standard distribution you know has a PGF that comes from a series you know. MF19 gives the definition \(G_X(t) = \mathrm{E}(t^X)\) and the formulae for the mean and variance (below), but **not** the PGFs of the four distributions, so you must be able to find each one.

### Discrete uniform

If \(X\) takes each of the values \(1, 2, \dots, n\) with probability \(\tfrac1n\),
\[G_X(t) = \frac1n\left(t + t^2 + \dots + t^n\right) = \frac{t(1 - t^n)}{n(1 - t)}\]
The second form uses the sum of a geometric progression with first term \(t\) and ratio \(t\) (for \(t \ne 1\)).

### Binomial

If \(X \sim B(n, p)\), put \(q = 1 - p\). The probability \(\mathrm{P}(X = x) = \binom{n}{x}p^x q^{n - x}\), so
\[G_X(t) = \sum_{x=0}^{n} \binom{n}{x} q^{n - x}(pt)^x = (q + pt)^n\]
by the binomial theorem with "\(a\)" \(= q\) and "\(b\)" \(= pt\).

### Geometric

If \(X \sim \mathrm{Geo}(p)\) is the number of trials up to and including the first success, \(\mathrm{P}(X = x) = q^{x - 1}p\) for \(x = 1, 2, \dots\), so
\[G_X(t) = \sum_{x=1}^{\infty} q^{x-1}p\,t^x = pt\left(1 + qt + (qt)^2 + \dots\right) = \frac{pt}{1 - qt}\]
This is a geometric progression with first term \(pt\) and ratio \(qt\), so the sum to infinity is valid for \(|qt| < 1\), that is \(|t| < \tfrac1q\). In particular it covers \(t = 1\), since \(q < 1\).

### Poisson

If \(X \sim \mathrm{Po}(\lambda)\), \(\mathrm{P}(X = x) = \dfrac{\mathrm{e}^{-\lambda}\lambda^x}{x!}\), so
\[G_X(t) = \sum_{x=0}^{\infty} \frac{\mathrm{e}^{-\lambda}(\lambda t)^x}{x!} = \mathrm{e}^{-\lambda}\sum_{x=0}^{\infty} \frac{(\lambda t)^x}{x!} = \mathrm{e}^{-\lambda}\mathrm{e}^{\lambda t} = \mathrm{e}^{\lambda(t - 1)}\]
using \(\mathrm{e}^y = \sum \dfrac{y^x}{x!}\).

:::key PGFs to know
| Distribution | \(G_X(t)\) |
|---|---|
| Discrete uniform on \(1, \dots, n\) | \(\dfrac{1}{n}\left(t + t^2 + \dots + t^n\right)\) |
| \(B(n, p)\) | \((q + pt)^n\), with \(q = 1 - p\) |
| \(\mathrm{Geo}(p)\) | \(\dfrac{pt}{1 - qt}\) |
| \(\mathrm{Po}(\lambda)\) | \(\mathrm{e}^{\lambda(t - 1)}\) |

Check each at \(t = 1\): \(\tfrac1n \times n = 1\), \(1^n = 1\), \(\dfrac{p}{1 - q} = 1\), \(\mathrm{e}^0 = 1\).
:::

:::eg \(X \sim B(6, 0.3)\). Write down \(G_X(t)\) and find \(\mathrm{P}(X = 2)\) from the coefficient of \(t^2\).
\[G_X(t) = (0.7 + 0.3t)^6\]
The \(t^2\) term of the binomial expansion is \(\binom62 (0.7)^4 (0.3t)^2\), so
\[\mathrm{P}(X = 2) = 15 \times 0.7^4 \times 0.3^2 = 0.324\]
which is the ordinary binomial probability, found this way.
:::

:::eg A learner driver passes the test at each attempt with probability 0.4, independently. Let \(X\) be the number of attempts up to and including the first pass. (a) Write down the PGF of \(X\). (b) Find \(\mathrm{P}(X = 3)\) from the coefficient of \(t^3\). (c) Find the mean and variance of \(X\) from the PGF.
(a) \(X \sim \mathrm{Geo}(0.4)\), so with \(p = 0.4\) and \(q = 0.6\),
\[G_X(t) = \frac{0.4t}{1 - 0.6t}\]
(b) Expand: \(G_X(t) = 0.4t\left(1 + 0.6t + 0.36t^2 + \dots\right)\), so the coefficient of \(t^3\) is \(0.4 \times 0.36 = 0.144\). That is \(q^2p\), as it should be.

(c) \(G_X'(t) = \dfrac{0.4}{(1 - 0.6t)^2}\), so \(G_X'(1) = \dfrac{0.4}{0.16} = 2.5\). \(G_X''(t) = \dfrac{0.48}{(1 - 0.6t)^3}\), so \(G_X''(1) = \dfrac{0.48}{0.064} = 7.5\).
\[\mathrm{Var}(X) = 7.5 + 2.5 - 6.25 = 3.75\]
**Check**: \(\dfrac1p = 2.5\) and \(\dfrac{q}{p^2} = \dfrac{0.6}{0.16} = 3.75\).
:::

:::plot The PGF of \(B(6, 0.3)\), \(G(t) = (0.7 + 0.3t)^6\), passes through \((1, 1)\). Its tangent there, labelled in the key, has gradient \(G'(1) = np = 1.8\), the mean. The curve starts at \(G(0) = 0.7^6 = 0.118 = \mathrm{P}(X = 0)\).
--f "(0.7+0.3*x)**6" --f "1+1.8*(x-1)" --label "G(t)" --label "tangent at t = 1" --x 0 1.2 --y 0 2.2 --pt "1,1,(1, 1)@se" --legend tl
:::

The widget shows each of the four distributions as a bar chart of \(\mathrm{P}(X = x)\) next to the graph of \(G(t)\) for \(0 \le t \le 1.2\), with the tangent at \(t = 1\). Try the binomial first, then change \(p\): the tangent's gradient is \(\mathrm{E}(X)\), which you will prove in the next section. The "sum of two" switch multiplies the PGF by a second independent copy.

:::html
<div class="widget" data-w="fm-pgf" data-dist="binomial" data-params="n=6,p=0.3"></div>
:::

## Mean and variance from the PGF

Differentiate \(G(t) = \sum p_x t^x\) term by term:
\[G'(t) = \sum x\,p_x t^{x - 1} \qquad\text{so}\qquad G'(1) = \sum x\,p_x = \mathrm{E}(X)\]
Differentiate again: \(G''(t) = \sum x(x - 1)p_x t^{x - 2}\), so \(G''(1) = \sum x(x - 1)p_x = \mathrm{E}\left(X(X - 1)\right) = \mathrm{E}(X^2) - \mathrm{E}(X)\).

:::key Mean and variance from \(G\)
\[\mathrm{E}(X) = G'(1) \qquad \mathrm{Var}(X) = G''(1) + G'(1) - \left\{G'(1)\right\}^2\]
Both formulae are in MF19.
:::

:::proof Why the variance formula holds
1. \(G''(1) = \mathrm{E}(X^2) - \mathrm{E}(X)\), as shown above, so \(\mathrm{E}(X^2) = G''(1) + G'(1)\) (using \(G'(1) = \mathrm{E}(X)\)).
2. By the definition of variance, \(\mathrm{Var}(X) = \mathrm{E}(X^2) - \{\mathrm{E}(X)\}^2\).
3. Substituting step 1 into step 2 gives \(\mathrm{Var}(X) = G''(1) + G'(1) - \{G'(1)\}^2\).
:::

:::warn \(G''(1)\) is not \(\mathrm{E}(X^2)\)
\(G''(1) = \mathrm{E}(X^2) - \mathrm{E}(X)\), not \(\mathrm{E}(X^2)\). Two slips follow: writing \(\mathrm{Var}(X) = G''(1) - \{G'(1)\}^2\) (a missing \(+G'(1)\)) and writing \(\mathrm{E}(X^2) = G''(1)\). Use the formula as printed.
:::

:::eg For the distribution of the first example, \(G(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3\), find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\).
\[G'(t) = 0.3 + 0.8t + 0.6t^2 \qquad G''(t) = 0.8 + 1.2t\]
\[G'(1) = 1.7 \qquad G''(1) = 2.0\]
\[\mathrm{E}(X) = 1.7 \qquad \mathrm{Var}(X) = 2.0 + 1.7 - 1.7^2 = 0.81\]
**Check** directly: \(\mathrm{E}(X^2) = 0.3 + 1.6 + 1.8 = 3.7\), and \(3.7 - 2.89 = 0.81\).
:::

Now derive the means and variances you already know from the PGFs. Each is a check on the method and a good way to see the pattern \(G''(1)\) uses.

:::eg Use the PGF to find the mean and variance of (a) \(B(n, p)\), (b) \(\mathrm{Geo}(p)\), (c) \(\mathrm{Po}(\lambda)\).
(a) \(G(t) = (q + pt)^n\), so
\[G'(t) = np(q + pt)^{n-1} \qquad G''(t) = n(n - 1)p^2(q + pt)^{n-2}\]
At \(t = 1\), \(q + p = 1\), so \(G'(1) = np\) and \(G''(1) = n(n - 1)p^2\). Then
\[\mathrm{Var}(X) = n(n - 1)p^2 + np - n^2p^2 = np - np^2 = npq\]
(b) \(G(t) = \dfrac{pt}{1 - qt}\), so
\[G'(t) = \frac{p}{(1 - qt)^2} \qquad G''(t) = \frac{2pq}{(1 - qt)^3}\]
\[G'(1) = \frac{p}{p^2} = \frac1p \qquad G''(1) = \frac{2pq}{p^3} = \frac{2q}{p^2}\]
\[\mathrm{Var}(X) = \frac{2q}{p^2} + \frac1p - \frac1{p^2} = \frac{2q + p - 1}{p^2} = \frac{q}{p^2}\]
using \(p - 1 = -q\).

(c) \(G(t) = \mathrm{e}^{\lambda(t - 1)}\), so \(G'(t) = \lambda\mathrm{e}^{\lambda(t-1)}\) and \(G''(t) = \lambda^2\mathrm{e}^{\lambda(t-1)}\). At \(t = 1\): \(G'(1) = \lambda\), \(G''(1) = \lambda^2\), and
\[\mathrm{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda\]
:::

For the uniform distribution on \(1, \dots, n\), use the sum form (the closed form is "0 over 0" at \(t = 1\)): \(G'(1) = \tfrac1n\sum x = \dfrac{n + 1}{2}\) and \(G''(1) = \tfrac1n\sum x(x - 1) = \dfrac{(n - 1)(n + 1)}{3}\), so \(\mathrm{Var}(X) = \dfrac{n^2 - 1}{12}\).

:::eg (Exam style) The PGF of \(X\) is \(G(t) = k(2 + t^2)(1 + 3t^2)\), where \(k\) is a constant. (a) Show that \(k = \tfrac1{12}\). (b) Find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\). (c) Write down the distribution of \(X\) in a table.
(a) The probabilities add to 1, so \(G(1) = 1\). [B1]
\[k(2 + 1)(1 + 3) = 1 \quad\Rightarrow\quad 12k = 1 \quad\Rightarrow\quad k = \tfrac1{12}\] [M1 A1]
(b) Expand first: \(G(t) = \tfrac1{12}\left(2 + 7t^2 + 3t^4\right)\).
\[G'(t) = \tfrac1{12}(14t + 12t^3) \qquad G''(t) = \tfrac1{12}(14 + 36t^2)\]
\[G'(1) = \tfrac{26}{12} = \tfrac{13}{6} \qquad G''(1) = \tfrac{50}{12} = \tfrac{25}{6}\] [M1 A1]
\[\mathrm{Var}(X) = \tfrac{25}{6} + \tfrac{13}{6} - \left(\tfrac{13}{6}\right)^2 = \tfrac{228 - 169}{36} = \tfrac{59}{36}\] [M1 A1]
(c) Read the coefficients: \(X\) takes only the even values 0, 2, 4.

| \(x\) | 0 | 2 | 4 |
|---|---|---|---|
| \(\mathrm{P}(X = x)\) | \(\tfrac16\) | \(\tfrac7{12}\) | \(\tfrac14\) |

[B1]
**Check**: \(\mathrm{E}(X) = 2 \times \tfrac7{12} + 4 \times \tfrac14 = \tfrac{13}{6}\).
:::

:::tip A PGF in \(t^2\)
When \(G\) contains only even powers of \(t\), \(X\) takes only even values. Differentiate carefully: \(\dfrac{d}{dt}\left(t^2\right) = 2t\), so an expression in \(t^2\) still needs the chain rule. Expanding the brackets first, as above, avoids the product rule.
:::

## Unknown constants

A PGF with an unknown constant is solved with the two facts you have: \(G(1) = 1\) and, if the mean is given, \(G'(1) = \mathrm{E}(X)\). Count the unknowns and the equations. If two constants appear, you need two equations: one from \(G(1) = 1\), one from the mean (or the variance, or a probability).

:::eg (Exam style) The discrete random variable \(X\) has PGF \(G_X(t) = kt^{-1}(at + 1)^2\), where \(a\) and \(k\) are positive constants, and \(\mathrm{E}(X) = \tfrac12\). (a) Show that \(a = 3\) and find \(k\). (b) Find \(\mathrm{Var}(X)\). (c) Three independent observations of \(X\) are taken, and \(Y\) is their sum. Find \(\mathrm{P}(Y = 1)\).
(a) Expand: \(G_X(t) = k\left(a^2 t + 2a + t^{-1}\right)\).

Using \(G_X(1) = 1\):
\[k(a + 1)^2 = 1\] [B1]
Differentiate: \(G_X'(t) = k\left(a^2 - t^{-2}\right)\), so \(G_X'(1) = k(a^2 - 1) = \tfrac12\). [M1]

Eliminate \(k\) by dividing the second equation by the first (this method mark depends on the previous ones):
\[\frac{a^2 - 1}{(a + 1)^2} = \frac{a - 1}{a + 1} = \frac12\] [DM1]
\[2a - 2 = a + 1 \quad\Rightarrow\quad a = 3\] [A1]
Then \(16k = 1\), so \(k = \tfrac1{16}\). [B1]

(b) \(G_X''(t) = 2kt^{-3}\), so \(G_X''(1) = \tfrac18\). [B1 FT]
\[\mathrm{Var}(X) = \tfrac18 + \tfrac12 - \tfrac14 = \tfrac38\] [B1 FT]
(c) \(G_X(t) = \dfrac{9t + 6 + t^{-1}}{16}\), so \(X\) takes the values \(-1, 0, 1\) with probabilities \(\tfrac1{16}, \tfrac6{16}, \tfrac9{16}\). The PGF of \(Y\) is
\[G_Y(t) = \left(G_X(t)\right)^3 = \frac{(3t + 1)^6}{16^3\,t^3}\] [B1]
We need the coefficient of \(t^1\), so the coefficient of \(t^4\) in \((1 + 3t)^6\) is needed: \(\binom64 3^4 = 1215\). [M1]
\[\mathrm{P}(Y = 1) = \frac{1215}{4096} = 0.297\] [A1]

**Check**: \(\mathrm{E}(Y) = 3 \times \tfrac12 = \tfrac32\) and \(\mathrm{P}(Y = 3) = \left(\tfrac9{16}\right)^3 = 0.178\), which is plausible beside 0.297 for the next value down.
:::

:::warn Mean given, not the probabilities
When the question says "\(\mathrm{E}(X) = \tfrac12\)" it is giving you \(G'(1) = \tfrac12\), not \(G(1)\). Always write \(G(1) = 1\) as well: it is a free equation and is usually the first mark.
:::

## Sums of independent random variables

Let \(X\) and \(Y\) be independent, and let \(S = X + Y\). Then
\[G_S(t) = \mathrm{E}\left(t^{X + Y}\right) = \mathrm{E}\left(t^X t^Y\right) = \mathrm{E}\left(t^X\right)\mathrm{E}\left(t^Y\right) = G_X(t)\,G_Y(t)\]
The third step is the one that needs independence: for independent variables the expected value of a product is the product of the expected values.

:::key PGF of a sum
If \(X\) and \(Y\) are **independent**, then \(G_{X + Y}(t) = G_X(t)\,G_Y(t)\). For \(n\) independent copies of \(X\), the sum has PGF \(\left(G_X(t)\right)^n\).
:::

:::eg Two fair dice are thrown. Use PGFs to find the distribution of the total, and \(\mathrm{P}(\text{total} = 7)\).
For one die \(G(t) = \tfrac16\left(t + t^2 + t^3 + t^4 + t^5 + t^6\right)\). The total has PGF
\[G_S(t) = \frac1{36}\left(t + t^2 + \dots + t^6\right)^2\]
The coefficient of \(t^7\) is the number of ways of making 7 from two numbers from 1 to 6, found by pairing powers: \(t^1t^6 + t^2t^5 + t^3t^4 + t^4t^3 + t^5t^2 + t^6t^1\), six pairs. So \(\mathrm{P}(S = 7) = \tfrac6{36} = \tfrac16\).

The same expansion gives every total: the coefficients rise 1, 2, 3, 4, 5, 6 and fall 5, 4, 3, 2, 1, over 36.

**Check** with the mean: \(G'(1)\) for one die is 3.5, and for the sum it is \(2 \times 3.5 = 7\), because \(G_S' = 2G\,G'\) and \(G(1) = 1\).
:::

:::eg \(X\) and \(Y\) are independent. \(X\) takes the values 0, 1, 2 with probabilities 0.5, 0.3, 0.2, and \(Y\) takes the values 0, 1 with probabilities 0.6, 0.4. Find the distribution of \(X + Y\) by multiplying PGFs.
\[G_X(t) = 0.5 + 0.3t + 0.2t^2 \qquad G_Y(t) = 0.6 + 0.4t\]
\[\begin{aligned}
G_{X+Y}(t) &= (0.5 + 0.3t + 0.2t^2)(0.6 + 0.4t) \\
&= 0.30 + (0.20 + 0.18)t + (0.12 + 0.12)t^2 + 0.08t^3 \\
&= 0.30 + 0.38t + 0.24t^2 + 0.08t^3
\end{aligned}\]
So \(\mathrm{P}(X + Y = 0, 1, 2, 3) = 0.30, 0.38, 0.24, 0.08\), which add to 1.

The coefficient of \(t^1\) is \(0.5 \times 0.4 + 0.3 \times 0.6\): the ways of making a total of 1, that is \((0, 1)\) and \((1, 0)\). Multiplying the PGFs does the "sum over all the ways" automatically.
:::

:::eg (Exam style) A fair spinner has four equal sectors numbered 1 to 4. It is spun twice, and \(S\) is the sum of the two scores. (a) Write down the PGF of one spin. (b) Find the PGF of \(S\) and \(\mathrm{P}(S = 5)\). (c) Use the PGF of \(S\) to find \(\mathrm{E}(S)\) and \(\mathrm{Var}(S)\).
(a) \(G(t) = \tfrac14\left(t + t^2 + t^3 + t^4\right)\). [B1]

(b) The spins are independent, so
\[G_S(t) = \tfrac1{16}\left(t + t^2 + t^3 + t^4\right)^2\] [M1]
The coefficient of \(t^5\) comes from the pairs \(t \cdot t^4\), \(t^2 \cdot t^3\), \(t^3 \cdot t^2\), \(t^4 \cdot t\): four of them, so \(\mathrm{P}(S = 5) = \tfrac4{16} = \tfrac14\). [A1]

(c) Write \(G = G_S\) and \(g(t) = \tfrac14(t + t^2 + t^3 + t^4)\), so \(G = g^2\). Then \(G' = 2gg'\) and \(G'' = 2g'^2 + 2gg''\). At \(t = 1\), \(g = 1\), \(g' = \tfrac14(1 + 2 + 3 + 4) = \tfrac52\) and \(g'' = \tfrac14(0 + 2 + 6 + 12) = 5\). [M1]
\[G'(1) = 5 \qquad G''(1) = 2\left(\tfrac52\right)^2 + 2 \times 5 = \tfrac{45}{2}\] [A1]
\[\mathrm{Var}(S) = \tfrac{45}{2} + 5 - 25 = \tfrac52\] [A1]
**Check**: a single spin has \(\mathrm{Var} = \dfrac{4^2 - 1}{12} = \tfrac54\), and two independent spins have twice that.
:::

:::eg (Exam style) \(X\) has PGF \((a + bt)^n\), where \(a\), \(b\) and \(n\) are constants, \(a + b = 1\), \(\mathrm{E}(X) = 2.4\) and \(\mathrm{Var}(X) = 1.92\). Find \(a\), \(b\) and \(n\).
This is the PGF of a binomial distribution, with \(q = a\) and \(p = b\) (they are positive and add to 1). [B1]

From the PGF, \(G'(1) = nb(a + b)^{n-1} = nb\) and \(G''(1) = n(n - 1)b^2\). So
\[nb = 2.4 \qquad n(n - 1)b^2 + 2.4 - 2.4^2 = 1.92\] [M1]
The second equation gives \(n(n - 1)b^2 = 5.28\), and \(n(n - 1)b^2 = (nb)^2 - nb^2 = 5.76 - nb^2\), so \(nb^2 = 0.48\). [M1]
Divide by \(nb = 2.4\): \(b = 0.2\), so \(a = 0.8\) and \(n = \dfrac{2.4}{0.2} = 12\). [A1 A1]

**Check**: \(npq = 12 \times 0.2 \times 0.8 = 1.92\).
:::

The most useful consequence is that sums of independent variables of the same family stay in the family. In each case the PGF of the sum is a product of two PGFs of the same form.

:::key Sums within a family
- \(X \sim B(n, p)\) and \(Y \sim B(m, p)\) independent (**same \(p\)**): \(G_{X+Y}(t) = (q + pt)^{n+m}\), so \(X + Y \sim B(n + m, p)\).
- \(X \sim \mathrm{Po}(\lambda)\) and \(Y \sim \mathrm{Po}(\mu)\) independent: \(G_{X+Y}(t) = \mathrm{e}^{(\lambda + \mu)(t - 1)}\), so \(X + Y \sim \mathrm{Po}(\lambda + \mu)\).
:::

:::eg (Exam style) Two independent counters, A and B, serve customers. The numbers of customers arriving at A and B in a minute are \(X \sim \mathrm{Po}(1.5)\) and \(Y \sim \mathrm{Po}(2.5)\). Use PGFs to show that the total \(T = X + Y\) has a Poisson distribution, and find \(\mathrm{P}(T = 2)\).
\[G_X(t) = \mathrm{e}^{1.5(t - 1)} \qquad G_Y(t) = \mathrm{e}^{2.5(t - 1)}\] [B1]
The variables are independent, so
\[G_T(t) = G_X(t)\,G_Y(t) = \mathrm{e}^{1.5(t-1) + 2.5(t-1)} = \mathrm{e}^{4(t - 1)}\] [M1 A1]
This is the PGF of \(\mathrm{Po}(4)\), and a PGF determines the distribution, so \(T \sim \mathrm{Po}(4)\). [A1]
\[\mathrm{P}(T = 2) = \mathrm{e}^{-4}\frac{4^2}{2!} = 0.147\] [A1]
:::

:::proof Why means and variances add for independent variables
Let \(S = X + Y\) with \(X\), \(Y\) independent, so \(G_S = G_XG_Y\) and \(G_X(1) = G_Y(1) = 1\).
1. The product rule gives \(G_S' = G_X'G_Y + G_XG_Y'\), so \(G_S'(1) = G_X'(1) + G_Y'(1)\). That is \(\mathrm{E}(S) = \mathrm{E}(X) + \mathrm{E}(Y)\).
2. Differentiate again: \(G_S'' = G_X''G_Y + 2G_X'G_Y' + G_XG_Y''\), so \(G_S''(1) = G_X''(1) + 2G_X'(1)G_Y'(1) + G_Y''(1)\).
3. Write \(a = G_X'(1)\) and \(b = G_Y'(1)\). Then \(\mathrm{Var}(S) = G_S''(1) + (a + b) - (a + b)^2\).
4. Substitute step 2 and expand \((a + b)^2 = a^2 + 2ab + b^2\): the \(2ab\) cancels, leaving \(\left[G_X''(1) + a - a^2\right] + \left[G_Y''(1) + b - b^2\right]\).
5. That is \(\mathrm{Var}(S) = \mathrm{Var}(X) + \mathrm{Var}(Y)\), the rule you already know, now seen as a consequence of the product rule.
:::

:::eg (Exam style) \(X \sim B(5, p)\) and \(Y \sim B(7, p)\) are independent, with the same unknown \(p\). (a) Use PGFs to show that \(X + Y \sim B(12, p)\). (b) Hence show that \(\mathrm{P}(X = 2 \mid X + Y = 4)\) does not depend on \(p\), and find its value.
(a) \(G_X(t) = (q + pt)^5\) and \(G_Y(t) = (q + pt)^7\). [B1] By independence, \(G_{X+Y}(t) = (q + pt)^{5+7} = (q + pt)^{12}\), the PGF of \(B(12, p)\), so \(X + Y \sim B(12, p)\). [M1 A1]

(b) \(X = 2\) and \(X + Y = 4\) together mean \(X = 2\) and \(Y = 2\). By independence
\[\mathrm{P}(X = 2 \mid X + Y = 4) = \frac{\mathrm{P}(X = 2)\,\mathrm{P}(Y = 2)}{\mathrm{P}(X + Y = 4)}\] [M1]
\[= \frac{\binom52 p^2q^3 \times \binom72 p^2q^5}{\binom{12}{4}p^4q^8} = \frac{10 \times 21}{495}\] [M1 A1]
The powers of \(p\) and \(q\) cancel (\(p^4q^8\) top and bottom), so the answer is independent of \(p\): \(\dfrac{210}{495} = \dfrac{14}{33} = 0.424\). [A1]
:::

Binomials with different \(p\) do **not** combine. If \(X \sim B(2, 0.3)\) and \(Y \sim B(3, 0.5)\), the sum has PGF \((0.7 + 0.3t)^2(0.5 + 0.5t)^3\), which is not of the form \((q + pt)^n\) for any single \(p\). The PGF is still correct: you can still read probabilities from its coefficients.

:::eg \(X\) and \(Y\) are independent, each with the geometric distribution \(\mathrm{Geo}\left(\tfrac13\right)\) (the number of trials to the first success). Find the PGF of \(S = X + Y\) and \(\mathrm{P}(S = 5)\).
With \(p = \tfrac13\) and \(q = \tfrac23\), \(G_X(t) = \dfrac{t/3}{1 - 2t/3} = \dfrac{t}{3 - 2t}\). So
\[G_S(t) = \frac{t^2}{(3 - 2t)^2} = \frac{t^2}{9}\left(1 - \tfrac23 t\right)^{-2}\]
Using the binomial series \((1 - u)^{-2} = 1 + 2u + 3u^2 + 4u^3 + \dots\) with \(u = \tfrac23 t\):
\[G_S(t) = \frac{t^2}{9}\left(1 + 2\left(\tfrac23 t\right) + 3\left(\tfrac23 t\right)^2 + 4\left(\tfrac23 t\right)^3 + \dots\right)\]
The coefficient of \(t^5\) is \(\tfrac19 \times 4 \times \left(\tfrac23\right)^3 = \dfrac{32}{243}\), so \(\mathrm{P}(S = 5) = \dfrac{32}{243} = 0.132\).

**Check** directly: \(\mathrm{P}(S = 5) = \sum_{x=1}^{4}\mathrm{P}(X = x)\mathrm{P}(Y = 5 - x)\), and the four terms are equal, each \(q^3p^2 = \tfrac8{243}\), giving \(\tfrac{32}{243}\).
:::

## Recognising a distribution, and linear transformations

Because a PGF determines the distribution, you can name a distribution from its PGF: match it with the table of standard PGFs.

:::eg Identify the distribution of each variable from its PGF, and give its mean. (a) \(G(t) = \dfrac{(1 + 2t)^4}{81}\). (b) \(G(t) = \mathrm{e}^{3t - 3}\). (c) \(G(t) = \dfrac{t}{2 - t}\).
(a) \(\dfrac{(1 + 2t)^4}{81} = \left(\dfrac{1 + 2t}{3}\right)^4 = \left(\tfrac13 + \tfrac23 t\right)^4\), which is \((q + pt)^n\) with \(q = \tfrac13\), \(p = \tfrac23\), \(n = 4\). So \(X \sim B\left(4, \tfrac23\right)\), mean \(np = \tfrac83\).

(b) \(\mathrm{e}^{3t - 3} = \mathrm{e}^{3(t-1)}\), so \(X \sim \mathrm{Po}(3)\), mean 3.

(c) \(\dfrac{t}{2 - t} = \dfrac{t/2}{1 - t/2}\), which is \(\dfrac{pt}{1 - qt}\) with \(p = q = \tfrac12\). So \(X \sim \mathrm{Geo}\left(\tfrac12\right)\), mean \(\dfrac1p = 2\).
:::

If \(Y = aX + b\), where \(a\) and \(b\) are integers, then
\[G_Y(t) = \mathrm{E}\left(t^{aX + b}\right) = t^b\,\mathrm{E}\left((t^a)^X\right) = t^b\,G_X\left(t^a\right)\]
so the new PGF is found by replacing \(t\) by \(t^a\) and multiplying by \(t^b\). A negative \(b\) gives a negative power of \(t\).

:::eg \(X \sim \mathrm{Po}(2)\) and \(Y = 3X + 1\). Find \(G_Y(t)\), and use it to find \(\mathrm{E}(Y)\) and \(\mathrm{Var}(Y)\).
\[G_Y(t) = t\,\mathrm{e}^{2(t^3 - 1)}\]
Differentiate with the product rule:
\[G_Y'(t) = \mathrm{e}^{2(t^3-1)}\left(1 + 6t^3\right)\]
\[G_Y''(t) = \mathrm{e}^{2(t^3-1)}\left(6t^2(1 + 6t^3) + 18t^2\right)\]
At \(t = 1\): \(G_Y'(1) = 7\) and \(G_Y''(1) = 6 \times 7 + 18 = 60\). So
\[\mathrm{E}(Y) = 7 \qquad \mathrm{Var}(Y) = 60 + 7 - 49 = 18\]
**Check** with the rules from [Linear combinations of random variables](#math.s2.linear): \(\mathrm{E}(3X + 1) = 3 \times 2 + 1 = 7\) and \(\mathrm{Var}(3X + 1) = 9 \times 2 = 18\).
:::

:::warn Dependent variables
The product rule \(G_{X+Y} = G_XG_Y\) needs independence. For \(Y = X\) (completely dependent) \(X + Y = 2X\) has PGF \(G_X(t^2)\), not \(G_X(t)^2\). Always check the wording ("independent") before multiplying. Also, multiplying PGFs adds the variables: it does not give \(XY\).
:::

:::exam What is given, what to show
MF19 gives \(G_X(t) = \mathrm{E}(t^X)\), \(\mathrm{E}(X) = G'(1)\) and \(\mathrm{Var}(X) = G''(1) + G'(1) - \{G'(1)\}^2\). It does not give the PGFs of the four distributions or the product rule for independent variables: learn them. In a "show that" part with a printed answer, show \(G(1) = 1\) as its own line, differentiate before substituting, and show the substitution \(t = 1\). Recent papers give the PGF with an unknown constant and ask you to use \(G(1) = 1\), \(G'(1)\) and a sum of independent observations in one question; the mark scheme credits the equation from \(G(1)\) first, then the equation from \(G'(1)\), then the elimination as a dependent method mark.
:::

:::board
Probability generating functions appear in the Cambridge 9231 syllabus as the standard four examples above (uniform, binomial, geometric, Poisson) with the mean, variance and sum rules. The treatment here is the 9231 one.
:::

:::eg Spot the error: the discrete random variable \(X \sim \mathrm{Geo}(0.2)\). Use the PGF to find \(\mathrm{Var}(X)\). The question is worth 4 marks.
A student wrote this answer.

Line 1: \(G(t) = \dfrac{0.2t}{1 - 0.8t}\), \(G'(t) = \dfrac{0.2}{(1 - 0.8t)^2}\), so \(G'(1) = 5\).
Line 2: \(G''(t) = \dfrac{0.32}{(1 - 0.8t)^3}\), so \(G''(1) = 40\).
Line 3: \(\mathrm{Var}(X) = G''(1) - \{G'(1)\}^2 = 40 - 25 = 15\).

Lines 1 and 2 are correct. [B1] [B1]

**Line 3 leaves out \(+G'(1)\).** The variance formula is \(G''(1) + G'(1) - \{G'(1)\}^2\); \(G''(1)\) is \(\mathrm{E}(X^2) - \mathrm{E}(X)\), not \(\mathrm{E}(X^2)\). A wrong formula scores no method mark, so the accuracy mark is lost too. [M0] [A0] The student scores 2 out of 4.

Correct line 3: \(\mathrm{Var}(X) = 40 + 5 - 25 = 20\), which agrees with \(\dfrac{q}{p^2} = \dfrac{0.8}{0.04} = 20\).
:::

:::try Practice
Q: Write down the PGF of \(X\) with \(\mathrm{P}(X = 1) = 0.15\), \(\mathrm{P}(X = 2) = 0.45\), \(\mathrm{P}(X = 4) = 0.4\), and find \(\mathrm{E}(X)\).
A: \(G(t) = 0.15t + 0.45t^2 + 0.4t^4\). \(G'(t) = 0.15 + 0.9t + 1.6t^3\), so \(\mathrm{E}(X) = G'(1) = 2.65\).
Q: Write down the PGF of \(X \sim \mathrm{Po}(3)\), and verify that \(G(1) = 1\).
A: \(G(t) = \mathrm{e}^{3(t - 1)}\), and \(G(1) = \mathrm{e}^0 = 1\).
Q: \(X \sim B(8, 0.25)\). Write down \(G_X(t)\) and use \(G'(1)\) to find \(\mathrm{E}(X)\).
A: \(G_X(t) = (0.75 + 0.25t)^8\). \(G'(t) = 8(0.25)(0.75 + 0.25t)^7\), so \(G'(1) = 2\).
Q: A spinner shows 1, 2, 3, 4 or 5 with equal probability. Write down its PGF and find \(G'(1)\).
A: \(G(t) = \tfrac15(t + t^2 + t^3 + t^4 + t^5)\), \(G'(1) = \tfrac15(1 + 2 + 3 + 4 + 5) = 3\).
Q: The PGF of \(X\) is \(\dfrac{t}{4 - 3t}\). Identify the distribution and find \(\mathrm{P}(X = 2)\).
A: \(\dfrac{t}{4 - 3t} = \dfrac{t/4}{1 - 3t/4}\), so \(X \sim \mathrm{Geo}\left(\tfrac14\right)\). \(\mathrm{P}(X = 2) = \tfrac34 \times \tfrac14 = \tfrac3{16}\).
Q: \(X \sim B(5, 0.4)\) and \(Y \sim B(7, 0.4)\) are independent. State the distribution of \(X + Y\) and give a reason.
A: \(G_{X+Y}(t) = (0.6 + 0.4t)^5(0.6 + 0.4t)^7 = (0.6 + 0.4t)^{12}\), so \(X + Y \sim B(12, 0.4)\).
Q: \(X\) has PGF \(G(t)\). Write down the PGF of \(Y = X + 3\) and of \(Z = 2X\).
A: \(G_Y(t) = t^3G(t)\) and \(G_Z(t) = G(t^2)\).
Q: \(G(t) = \tfrac14 + \tfrac12 t + \tfrac14 t^2\). Write it as a square, and state the distribution.
A: \(G(t) = \left(\tfrac12 + \tfrac12 t\right)^2\), so \(X \sim B\left(2, \tfrac12\right)\): the number of heads in two fair tosses.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ The random variable \(X\) has PGF \(G(t) = 0.05t + 0.35t^2 + 0.4t^3 + 0.2t^5\). Find \(\mathrm{E}(X)\) and \(\mathrm{P}(X \le 2)\).
A: \(G'(t) = 0.05 + 0.7t + 1.2t^2 + t^4\) [M1], so \(\mathrm{E}(X) = G'(1) = 2.95\). [A1]
\(\mathrm{P}(X \le 2)\) is the sum of the coefficients of \(t\) and \(t^2\): \(0.4\). [B1]
Q: [4 marks] ★ \(X \sim \mathrm{Po}(3)\). Use its PGF to find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\).
A: \(G(t) = \mathrm{e}^{3(t - 1)}\), \(G'(t) = 3\mathrm{e}^{3(t-1)}\), \(G''(t) = 9\mathrm{e}^{3(t-1)}\). [B1]
\(G'(1) = 3 = \mathrm{E}(X)\). [B1]
\(\mathrm{Var}(X) = G''(1) + G'(1) - \{G'(1)\}^2 = 9 + 3 - 9\) [M1] \(= 3\). [A1]
Q: [5 marks] ★★ The random variable \(X\) has PGF \(G(t) = k(3 + 2t)^2\). (a) Find \(k\). (b) Find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\). (c) Identify the distribution of \(X\).
A: (a) \(G(1) = 1\), so \(25k = 1\), \(k = \tfrac1{25}\). [M1 A1]
(b) \(G'(t) = 4k(3 + 2t)\), \(G''(t) = 8k\). \(G'(1) = \tfrac{20}{25} = 0.8\), \(G''(1) = 0.32\). [B1]
\(\mathrm{Var}(X) = 0.32 + 0.8 - 0.64 = 0.48\). [B1]
(c) \(G(t) = \left(\tfrac35 + \tfrac25 t\right)^2\), so \(X \sim B(2, 0.4)\): check \(np = 0.8\) and \(npq = 0.48\). [B1]
Q: [6 marks] ★★ \(X \sim B(6, 0.3)\) and \(Y \sim B(9, 0.3)\) are independent. (a) Find the PGF of \(X + Y\) and identify its distribution. (b) Find \(\mathrm{P}(X + Y = 5)\). (c) Explain why this method would not give a binomial distribution if \(Y\) had parameter \(p = 0.4\).
A: (a) \(G_{X+Y}(t) = (0.7 + 0.3t)^6(0.7 + 0.3t)^9 = (0.7 + 0.3t)^{15}\) [M1], so \(X + Y \sim B(15, 0.3)\). [A1]
(b) \(\mathrm{P}(X + Y = 5) = \binom{15}{5}(0.3)^5(0.7)^{10}\) [M1] \(= 0.206\). [A1]
(c) The PGF would be \((0.7 + 0.3t)^6(0.6 + 0.4t)^9\), which cannot be written as \((q + pt)^{15}\) for a single \(p\), because the two factors differ. [B1 B1]
Q: [6 marks] ★★ The PGF of \(X\) is \(G(t) = k(1 + 2t^2)^2\). (a) Find the value of \(k\). (b) Find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\). (c) Find \(\mathrm{P}(X = 2)\).
A: (a) \(G(1) = 9k = 1\), so \(k = \tfrac19\). [M1 A1]
(b) \(G(t) = \tfrac19(1 + 4t^2 + 4t^4)\), \(G'(t) = \tfrac19(8t + 16t^3)\), \(G''(t) = \tfrac19(8 + 48t^2)\). [M1]
\(G'(1) = \tfrac{24}{9} = \tfrac83\), \(G''(1) = \tfrac{56}{9}\). \(\mathrm{Var}(X) = \tfrac{56}{9} + \tfrac{24}{9} - \tfrac{64}{9} = \tfrac{16}{9}\). [A1 A1]
(c) The coefficient of \(t^2\) is \(\tfrac49\). [B1]
Q: [5 marks] ★★ \(X \sim B(5, 0.4)\) and \(Y = 2X - 1\). (a) Find the PGF of \(Y\). (b) Use it to show that \(\mathrm{E}(Y) = 3\). (c) State the possible values of \(Y\).
A: (a) \(G_Y(t) = t^{-1}G_X(t^2) = t^{-1}(0.6 + 0.4t^2)^5\). [M1 A1]
(b) By the product rule
\[G_Y'(t) = -t^{-2}(0.6 + 0.4t^2)^5 + t^{-1} \times 5(0.6 + 0.4t^2)^4 \times 0.8t\]
At \(t = 1\): \(G_Y'(1) = -1 + 4 = 3\). [M1 A1]
(c) \(Y\) takes the values \(-1, 1, 3, 5, 7, 9\). [B1]
Q: [11 marks] (#math.s1.drv) ★★★ \(X \sim \mathrm{Geo}\left(\tfrac14\right)\). (a) Show that the PGF of \(X\) is \(G_X(t) = \dfrac{t}{4 - 3t}\), stating the values of \(t\) for which it is valid. (b) Use \(G_X\) to find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\). (c) \(X_1\) and \(X_2\) are independent observations of \(X\), and \(S = X_1 + X_2\). Find the PGF of \(S\), and use its expansion to find \(\mathrm{P}(S = 4)\). (d) State \(\mathrm{E}(S)\) and \(\mathrm{Var}(S)\).
H: Write \(\mathrm{P}(X = x) = q^{x-1}p\) and sum the geometric series.
H: \(G_X'(t) = \dfrac{4}{(4 - 3t)^2}\).
H: \(G_S(t) = \dfrac{t^2}{16}\left(1 - \tfrac34 t\right)^{-2}\); use the binomial series.
A: (a) \(G_X(t) = \sum_{x=1}^{\infty}\left(\tfrac34\right)^{x-1}\tfrac14 t^x = \dfrac{t/4}{1 - 3t/4} = \dfrac{t}{4 - 3t}\). [M1 A1] This is valid for \(|t| < \tfrac43\). [B1]
(b) \(G_X'(t) = \dfrac{4}{(4 - 3t)^2}\), \(G_X'(1) = 4\). [M1 A1] \(G_X''(t) = \dfrac{24}{(4 - 3t)^3}\), \(G_X''(1) = 24\), so \(\mathrm{Var}(X) = 24 + 4 - 16 = 12\). [M1 A1]
(c) \(G_S(t) = \dfrac{t^2}{(4 - 3t)^2}\). [B1] \(= \dfrac{t^2}{16}\left(1 + 2\left(\tfrac34 t\right) + 3\left(\tfrac34 t\right)^2 + \dots\right)\), so the coefficient of \(t^4\) is \(\tfrac{3}{16}\left(\tfrac34\right)^2 = \tfrac{27}{256}\). [M1] \(\mathrm{P}(S = 4) = 0.105\). [A1]
(d) \(\mathrm{E}(S) = 8\), \(\mathrm{Var}(S) = 24\) (means and variances add for independent variables). [B1]
Q: [7 marks] ★★★ \(X \sim \mathrm{Po}(2)\) and \(Y \sim B(4, 0.5)\) are independent, and \(W = X + Y\). (a) Write down the PGF of \(W\). (b) Use it to find \(\mathrm{E}(W)\) and \(\mathrm{Var}(W)\). (c) Find \(\mathrm{P}(W = 0)\).
H: \(G_Y(t) = \left(\tfrac{1 + t}{2}\right)^4\).
H: Write \(G_W = \mathrm{e}^{2(t-1)}G_Y\) and use the product rule twice, or the rule "means and variances add" as a check.
A: (a) \(G_W(t) = \mathrm{e}^{2(t - 1)}\left(\dfrac{1 + t}{2}\right)^4\). [B1 B1]
(b) \(G_W'(t) = \mathrm{e}^{2(t-1)}\left[2\left(\tfrac{1+t}{2}\right)^4 + 2\left(\tfrac{1+t}{2}\right)^3\right]\), so \(G_W'(1) = 2 + 2 = 4\). [M1 A1]
\(G_W''(t) = \mathrm{e}^{2(t-1)}\left[4H + 4H' + H''\right]\) with \(H = \left(\tfrac{1+t}{2}\right)^4\), and at \(t = 1\), \(H = 1\), \(H' = 2\), \(H'' = 3\), so \(G_W''(1) = 4 + 8 + 3 = 15\). [M1]
\(\mathrm{Var}(W) = 15 + 4 - 16 = 3\). [A1] (Check: \(2 + 1 = 3\).)
(c) \(\mathrm{P}(W = 0) = G_W(0) = \mathrm{e}^{-2}\left(\tfrac12\right)^4 = \dfrac{\mathrm{e}^{-2}}{16} = 0.00846\). [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ (a) Show that \(\mathrm{P}(X \text{ is even}) = \tfrac12\left(G(1) + G(-1)\right)\) for any PGF \(G\). (b) Hence find \(\mathrm{P}(X \text{ is even})\) when \(X \sim \mathrm{Po}(\lambda)\) and when \(X \sim B(n, p)\). (c) Evaluate the Poisson probability for \(\lambda = 1.5\).
H: \(G(-1) = \sum \mathrm{P}(X = x)(-1)^x\). What happens to the odd terms when you add \(G(1)\)?
H: For the binomial, \(G(-1) = (q - p)^n\).
A: (a) \(G(1) + G(-1) = \sum p_x\left(1 + (-1)^x\right)\) is \(2p_x\) for even \(x\) and 0 for odd \(x\). [M1] So half the sum is \(\mathrm{P}(X \text{ even})\). [A1]
(b) Poisson: \(G(-1) = \mathrm{e}^{-2\lambda}\), so \(\mathrm{P}(\text{even}) = \tfrac12\left(1 + \mathrm{e}^{-2\lambda}\right)\). [M1 A1] Binomial: \(\tfrac12\left(1 + (q - p)^n\right)\). [A1]
(c) \(\tfrac12\left(1 + \mathrm{e}^{-3}\right) = 0.525\). [A1]
Q: [7 marks] ★★★ \(X \sim \mathrm{Geo}(p)\) counts the trials up to the first success, and \(Z = X - 1\) is the number of failures before it. (a) Find the PGF of \(Z\). (b) Use it to find \(\mathrm{E}(Z)\) and \(\mathrm{Var}(Z)\). (c) \(Z_1\) and \(Z_2\) are independent copies of \(Z\). Find \(\mathrm{P}(Z_1 + Z_2 = 3)\) in terms of \(p\) and \(q\).
H: \(G_Z(t) = t^{-1}G_X(t)\).
H: The mean of \(Z\) is \(\mathrm{E}(X) - 1\), and the variance does not change when you subtract a constant.
H: Expand \(\left(1 - qt\right)^{-2}\).
A: (a) \(G_Z(t) = t^{-1}\dfrac{pt}{1 - qt} = \dfrac{p}{1 - qt}\). [M1 A1]
(b) \(G_Z'(t) = \dfrac{pq}{(1 - qt)^2}\), so \(\mathrm{E}(Z) = \dfrac{pq}{p^2} = \dfrac{q}{p}\) [M1 A1]. \(G_Z''(t) = \dfrac{2pq^2}{(1 - qt)^3}\), \(G_Z''(1) = \dfrac{2q^2}{p^2}\), and \(\mathrm{Var}(Z) = \dfrac{2q^2}{p^2} + \dfrac qp - \dfrac{q^2}{p^2} = \dfrac{q^2 + pq}{p^2} = \dfrac{q}{p^2}\), the same as \(\mathrm{Var}(X)\). [A1]
(c) \(G_{Z_1 + Z_2}(t) = \dfrac{p^2}{(1 - qt)^2} = p^2\left(1 + 2qt + 3q^2t^2 + 4q^3t^3 + \dots\right)\), so \(\mathrm{P}(Z_1 + Z_2 = 3) = 4p^2q^3\). [M1 A1]
:::

:::quiz
? What is \(G_X(1)\) for any probability generating function?
+ \(1\)
- \(\mathrm{E}(X)\)
- \(0\)
- \(\mathrm{P}(X = 1)\)
> \(G(1) = \sum \mathrm{P}(X = x) = 1\). \(\mathrm{E}(X)\) is \(G'(1)\), and \(\mathrm{P}(X = 0)\) is \(G(0)\).
? \(X\) has PGF \(\tfrac13 + \tfrac23 t^2\). What is \(\mathrm{P}(X = 2)\)?
+ \(\tfrac23\)
- \(\tfrac13\)
- \(\tfrac43\)
- \(0\), because there is no \(t\) term
> The coefficient of \(t^2\) is \(\tfrac23\). The constant \(\tfrac13\) is \(\mathrm{P}(X = 0)\). There is no \(t\) term because \(X\) cannot equal 1, but \(X = 2\) is possible.
? \(G'(1) = 4\) and \(G''(1) = 20\). What is \(\mathrm{Var}(X)\)?
+ \(8\)
- \(4\)
- \(20\)
- \(24\)
> \(\mathrm{Var}(X) = 20 + 4 - 16 = 8\). The answer 4 uses \(G''(1) - G'(1)\), and 20 takes \(G''(1)\) as the variance, so it forgets \(E(X)^2\).
? \(X\) and \(Y\) are independent with PGFs \(G_X\) and \(G_Y\). Which is the PGF of \(X + Y\)?
+ \(G_X(t)\,G_Y(t)\)
- \(G_X(t) + G_Y(t)\)
- \(G_X(t)\,G_Y(t)\) even if \(X\) and \(Y\) are dependent
- \(G_X\left(G_Y(t)\right)\)
> The product, for independent variables only. A sum of PGFs would have \(G(1) = 2\), which is not a PGF.
? \(X \sim \mathrm{Po}(2)\) and \(Y \sim \mathrm{Po}(5)\) are independent. What is the PGF of \(X + Y\)?
+ \(\mathrm{e}^{7(t - 1)}\)
- \(\mathrm{e}^{10(t - 1)}\)
- \(\mathrm{e}^{2(t-1)} + \mathrm{e}^{5(t-1)}\)
- \(\mathrm{e}^{7t}\)
> The exponents add: \(2 + 5 = 7\). Multiplying the rates (10) confuses product of PGFs with product of parameters, and \(\mathrm{e}^{7t}\) would give \(G(1) \ne 1\).
? \(G_X(t)\) is the PGF of \(X\). What is the PGF of \(X + 3\)?
+ \(t^3G_X(t)\)
- \(G_X(t) + 3\)
- \(G_X(t + 3)\)
- \(G_X(t^3)\)
> Adding a constant 3 multiplies each term by \(t^3\), so \(t^3G_X(t)\). \(G_X(t^3)\) is the PGF of \(3X\).
:::

:::checklist What you can now do
- [ ] I can write down the PGF of a discrete random variable from its distribution, and read probabilities from its coefficients.
- [ ] I can derive and use the PGFs of the discrete uniform, binomial, geometric and Poisson distributions.
- [ ] I can find \(\mathrm{E}(X)\) and \(\mathrm{Var}(X)\) from \(G'(1)\) and \(G''(1)\) using the MF19 formulae.
- [ ] I can find unknown constants in a PGF from \(G(1) = 1\) and given values of the mean or a probability.
- [ ] I can use the fact that the PGF of a sum of independent variables is the product of their PGFs, including to find probabilities.
- [ ] I can recognise a distribution from its PGF and find the PGF of \(aX + b\).
:::

:::recap
- \(G_X(t) = \mathrm{E}(t^X) = \sum \mathrm{P}(X = x)t^x\); \(G(1) = 1\), \(G(0) = \mathrm{P}(X = 0)\), the coefficient of \(t^r\) is \(\mathrm{P}(X = r)\).
- Uniform on \(1, \dots, n\): \(\tfrac1n(t + \dots + t^n)\); \(B(n, p)\): \((q + pt)^n\); \(\mathrm{Geo}(p)\): \(\dfrac{pt}{1 - qt}\); \(\mathrm{Po}(\lambda)\): \(\mathrm{e}^{\lambda(t-1)}\).
- \(\mathrm{E}(X) = G'(1)\) and \(\mathrm{Var}(X) = G''(1) + G'(1) - \{G'(1)\}^2\) (on MF19). \(G''(1)\) is \(\mathrm{E}(X^2) - \mathrm{E}(X)\), not \(\mathrm{E}(X^2)\).
- Independent \(X\), \(Y\): \(G_{X+Y} = G_XG_Y\), so binomials with the same \(p\) and Poissons add within their families.
- \(Y = aX + b\): \(G_Y(t) = t^bG_X(t^a)\); a negative \(b\) gives negative powers of \(t\).
- Unknown constants: use \(G(1) = 1\), then \(G'(1)\) if the mean is given.
:::

:::links
- practise: [Statistics booklets](https://madasmaths.com/archive_maths_booklets_statistics.html) · MadAsMaths · discrete random variable practice with answers
- watch: [Poisson distribution](https://www.examsolutions.net/tutorials/poisson-distribution/) · ExamSolutions · the distribution whose PGF is \(\mathrm{e}^{\lambda(t-1)}\)
- explore: [Probability distributions](https://seeing-theory.brown.edu/probability-distributions/index.html) · Seeing Theory · bar charts of the standard distributions
- papers: [9231 Paper 4 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fps/) · Physics & Maths Tutor · real Paper 4 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Further Pure 1 (Paper 1) survival guide](#math.fm.exam.fp1) begins the exam-preparation guides, one for each Further Mathematics paper.
