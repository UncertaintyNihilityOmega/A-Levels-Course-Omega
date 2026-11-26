@chapter math.fm.hyperbolic
@title Hyperbolic functions
@level fm
@paper CAIE 9231 Paper 2 · AQA/OCR/Edexcel Further Maths Core Pure
@time 5–7 hours
@summary The hyperbolic functions \(\sinh x\), \(\cosh x\), \(\tanh x\) and their reciprocals are built from \(e^x\) and \(e^{-x}\). You will learn their graphs, prove and use their identities (which echo the trigonometric ones), solve hyperbolic equations, and define and derive the logarithmic forms of the inverse functions.

:::why
A cable hanging between two poles does not hang in a parabola. It hangs in the curve \(y = a\cosh\frac{x}{a}\), a catenary, and a falling object that meets air resistance has speed \(V\tanh(kt)\). Hyperbolic functions are what you get from \(e^x\) when you keep only the even part or only the odd part. They behave like the trigonometric functions (identities, derivatives, integrals) with a few sign changes, so everything you know about sine and cosine helps. They also turn awkward integrals into easy ones, which the rest of Further Pure 2 uses constantly.
:::

**Before you start**, you need exponentials and logarithms from [Logarithms and exponentials](#math.p3.logs), the double-angle identities from [Further trigonometry](#math.p3.trig), and the habit of treating a quadratic in \(e^x\) as an ordinary quadratic. Proof by direct algebra is examined in this chapter: you will be asked to "prove" identities starting from definitions.

:::try Warm-up
Q: Solve \(e^{2x} - 5e^x + 6 = 0\), giving exact answers. (from [Logarithms and exponentials](#math.p3.logs))
A: Put \(u = e^x\): \(u^2 - 5u + 6 = 0\), so \(u = 2\) or \(u = 3\). Then \(x = \ln 2\) or \(x = \ln 3\).
Q: Simplify \(e^{\ln 5 + 2\ln 3}\). (from [Logarithms and exponentials](#math.p3.logs))
A: \(e^{\ln 5} \times e^{\ln 9} = 5 \times 9 = 45\).
Q: Write \(\cos^2 x\) in terms of \(\cos 2x\). (from [Further trigonometry](#math.p3.trig))
A: \(\cos 2x = 2\cos^2 x - 1\), so \(\cos^2 x = \tfrac12(1 + \cos 2x)\).
:::

## Definitions

Any function can be split into an even part and an odd part. For \(e^x\) those parts are so useful that they get their own names. Write \(e^x = \frac{e^x + e^{-x}}{2} + \frac{e^x - e^{-x}}{2}\). The first piece is unchanged when you replace \(x\) by \(-x\) (it is even); the second changes sign (it is odd).

:::def Hyperbolic sine and cosine
\[\sinh x = \frac{e^x - e^{-x}}{2} \qquad \cosh x = \frac{e^x + e^{-x}}{2}\]
Say "shine" and "cosh". The names stand for "hyperbolic sine" and "hyperbolic cosine".
:::

:::def Hyperbolic tangent and the reciprocal functions
\[\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}\]
\[\operatorname{sech} x = \frac{1}{\cosh x} \qquad \operatorname{cosech} x = \frac{1}{\sinh x} \qquad \coth x = \frac{1}{\tanh x} = \frac{\cosh x}{\sinh x}\]
Say "tanch", "sheck", "cosheck" and "coth". \(\operatorname{cosech} x\) and \(\coth x\) are undefined at \(x = 0\).
:::

The two most useful facts come straight from the definitions. Add them, then subtract them:

:::key \(e^x\) and \(e^{-x}\) in hyperbolic form
\[e^x = \cosh x + \sinh x \qquad e^{-x} = \cosh x - \sinh x\]
\(\cosh x\) is even, \(\sinh x\) and \(\tanh x\) are odd:
\[\cosh(-x) = \cosh x \qquad \sinh(-x) = -\sinh x \qquad \tanh(-x) = -\tanh x\]
:::

At \(x = 0\) the exponentials are both 1, so \(\sinh 0 = \frac{1 - 1}{2} = 0\), \(\cosh 0 = \frac{1 + 1}{2} = 1\) and \(\tanh 0 = 0\).

| \(x\) | \(-1\) | 0 | 1 | 2 |
|---|---|---|---|---|
| \(\sinh x\) | \(-1.175\) | 0 | 1.175 | 3.627 |
| \(\cosh x\) | 1.543 | 1 | 1.543 | 3.762 |
| \(\tanh x\) | \(-0.7616\) | 0 | 0.7616 | 0.9640 |

Your calculator has \(\sinh\), \(\cosh\) and \(\tanh\) keys (usually under a hyp button). Use them to check your work.

The relations \(e^{\pm x} = \cosh x \pm \sinh x\) let you switch between the two languages, which is how most equations in this chapter are solved.

:::eg Express \(5e^x - 3e^{-x}\) in the form \(a\cosh x + b\sinh x\), and express \(6\cosh x + 2\sinh x\) in terms of \(e^x\) and \(e^{-x}\).
Replace \(e^x\) by \(\cosh x + \sinh x\) and \(e^{-x}\) by \(\cosh x - \sinh x\):
\[\begin{aligned}
5e^x - 3e^{-x} &= 5(\cosh x + \sinh x) - 3(\cosh x - \sinh x) \\
&= 2\cosh x + 8\sinh x
\end{aligned}\]
For the second, use the definitions directly:
\[\begin{aligned}
6\cosh x + 2\sinh x &= 3(e^x + e^{-x}) + (e^x - e^{-x}) \\
&= 4e^x + 2e^{-x}
\end{aligned}\]
**Check** at \(x = 0\): \(5 - 3 = 2 = 2\cosh 0 + 8\sinh 0\), and \(6 = 4 + 2\).
:::

:::note Why "hyperbolic"?
Every point \((\cos t, \sin t)\) lies on the circle \(x^2 + y^2 = 1\). Every point \((\cosh t, \sinh t)\) lies on one branch of the hyperbola \(x^2 - y^2 = 1\), because \(\cosh^2 t - \sinh^2 t = 1\) (proved below). That is the whole reason for the name, and the reason the identities look like the trigonometric ones with a sign changed.
:::

:::eg A cable hangs between two poles 30 m apart. Taking the origin on the ground below its lowest point, its height above the ground at horizontal distance \(x\) metres from that point is \(y = 25\cosh\frac{x}{25} - 19\). Find (a) the lowest height, (b) the height at each pole, (c) how far the cable sags below the tops of the poles.
(a) At \(x = 0\), \(\cosh 0 = 1\), so \(y = 25 - 19 = 6\) m.

(b) The poles are at \(x = \pm 15\). Because \(\cosh\) is even, both poles have the same height:
\[y = 25\cosh 0.6 - 19 = 25 \times 1.18547 - 19 = 10.64\ \text{m}\]
(c) The sag is the difference, \(10.64 - 6 = 4.64\) m.

**Check**: the curve is flat at the bottom and rises on both sides, which matches a cable that sags between two supports.
:::

## Graphs of the hyperbolic functions

Because \(e^{-x}\) shrinks quickly for large positive \(x\), both \(\sinh x\) and \(\cosh x\) look like \(\tfrac12 e^x\) there: \(\cosh x\) is a little above it, \(\sinh x\) a little below. For large negative \(x\) they look like \(\pm\tfrac12 e^{-x}\).

:::plot The curves y = sinh x and y = cosh x. Both approach y = ½eˣ as x grows; cosh x is even with minimum value 1 at (0, 1), and sinh x is odd, passing through the origin with no turning point.
--f "(exp(x)-exp(-x))/2" --f "(exp(x)+exp(-x))/2" --f "exp(x)/2" --label "y = sinh x" --label "y = cosh x" --label "y = ½eˣ" --x -2.5 2.5 --y -7 11 --pt "0,1,(0, 1)@ne" --legend tl
:::

The graph of \(y = \cosh x\) is exactly the shape of the hanging cable above. For \(\tanh x\), divide top and bottom by \(e^x\): \(\tanh x = \dfrac{1 - e^{-2x}}{1 + e^{-2x}}\). As \(x \to \infty\) this tends to 1, and as \(x \to -\infty\) it tends to \(-1\).

:::plot The curves y = tanh x and y = coth x. tanh x is odd and rises through the origin, staying between the asymptotes y = −1 and y = 1. coth x has the same asymptotes y = ±1 and also the asymptote x = 0.
--f "(exp(x)-exp(-x))/(exp(x)+exp(-x))" --f "(exp(x)+exp(-x))/(exp(x)-exp(-x))+0*sqrt(abs(x)-0.01)" --label "y = tanh x" --label "y = coth x" --x -3 3 --y -3 3 --hline 1 --hline -1 --legend tr
:::

The two reciprocals follow by taking \(1/\cosh x\) and \(1/\sinh x\).

:::plot The curves y = sech x and y = cosech x. sech x has maximum value 1 at (0, 1) and tends to 0 on both sides. cosech x is odd, undefined at x = 0, with the axes as asymptotes.
--f "2/(exp(x)+exp(-x))" --f "2/(exp(x)-exp(-x))+0*sqrt(abs(x)-0.01)" --label "y = sech x" --label "y = cosech x" --x -3 3 --y -3 3 --legend tr
:::

:::key Properties of the six graphs
| Function | Domain | Range | Symmetry and key features |
|---|---|---|---|
| \(\sinh x\) | all real \(x\) | all real | odd, through \((0, 0)\), increasing |
| \(\cosh x\) | all real \(x\) | \(y \ge 1\) | even, minimum \((0, 1)\) |
| \(\tanh x\) | all real \(x\) | \(-1 < y < 1\) | odd, asymptotes \(y = \pm 1\) |
| \(\operatorname{sech} x\) | all real \(x\) | \(0 < y \le 1\) | even, maximum \((0, 1)\), asymptote \(y = 0\) |
| \(\operatorname{cosech} x\) | \(x \ne 0\) | \(y \ne 0\) | odd, asymptotes \(x = 0\) and \(y = 0\) |
| \(\coth x\) | \(x \ne 0\) | \(\lvert y \rvert > 1\) | odd, asymptotes \(x = 0\) and \(y = \pm 1\) |
:::

When you sketch one, mark the asymptotes and the intercepts. Unlike \(\sin x\), none of these repeats: they are not periodic.

The usual transformations from [Further trigonometry](#math.p3.trig) and [Functions](#math.p1.functions) apply: stretch, translate and reflect in the same way.

:::eg (Exam style) Sketch the curve \(y = 1 + 2\tanh x\). State the equations of its asymptotes and the coordinates of the points where it crosses the axes.
The graph of \(y = \tanh x\) lies between \(y = -1\) and \(y = 1\). Stretching by factor 2 in the \(y\)-direction puts it between \(-2\) and \(2\); adding 1 shifts it up. [M1]

The asymptotes are \(y = 3\) (as \(x \to \infty\)) and \(y = -1\) (as \(x \to -\infty\)). [B1]

At \(x = 0\), \(y = 1 + 2\tanh 0 = 1\): the \(y\)-intercept is \((0, 1)\). [B1]

For the \(x\)-intercept solve \(1 + 2\tanh x = 0\):
\[\tanh x = -\tfrac12\] Multiply top and bottom of \(\tanh x = \dfrac{\mathrm{e}^x - \mathrm{e}^{-x}}{\mathrm{e}^x + \mathrm{e}^{-x}}\) by \(\mathrm{e}^x\) to get \(\tanh x = \dfrac{\mathrm{e}^{2x} - 1}{\mathrm{e}^{2x} + 1}\), so \(\dfrac{\mathrm{e}^{2x} - 1}{\mathrm{e}^{2x} + 1} = -\tfrac12\), \(2\mathrm{e}^{2x} - 2 = -\mathrm{e}^{2x} - 1\), \(\mathrm{e}^{2x} = \tfrac13\) and
\[x = \tfrac12\ln\tfrac13 = -\tfrac12\ln 3\] [M1 A1]
(This is \(-\tanh^{-1}\tfrac12\): the inverse function \(\tanh^{-1}\) is defined later in this chapter.)
The curve is increasing throughout, so it crosses the axes once each. The \(x\)-intercept is \(\left(-\tfrac12\ln 3,\ 0\right) = (-0.549, 0)\).
:::

:::plot The curve y = 1 + 2 tanh x rises from the asymptote y = −1 on the left to the asymptote y = 3 on the right. It crosses the y-axis at (0, 1) and the x-axis at about (−0.549, 0).
--f "1+2*(exp(x)-exp(-x))/(exp(x)+exp(-x))" --label "y = 1 + 2 tanh x" --x -3 3 --y -2 4 --hline 3 --hline -1 --pt "0,1,(0, 1)@se" --pt "-0.5493,0,(−0.549, 0)@nw" --legend tr
:::

## Identities

Every trigonometric identity has a hyperbolic partner. The most important one replaces \(\cos^2 + \sin^2 \equiv 1\).

:::eg (Exam style) Starting from the definitions of \(\cosh x\) and \(\sinh x\) in terms of \(e^x\), prove that \(\cosh^2 x - \sinh^2 x \equiv 1\).
Substitute the definitions:
\[\cosh^2 x - \sinh^2 x = \frac{(e^x + e^{-x})^2}{4} - \frac{(e^x - e^{-x})^2}{4}\] [M1]
Expand both squares. Note that \(e^x \times e^{-x} = 1\):
\[\begin{aligned}
&= \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4}
\end{aligned}\] [M1]
The \(e^{2x}\) and \(e^{-2x}\) terms cancel:
\[= \frac{4}{4} = 1\] [A1]
:::

Dividing the identity by \(\cosh^2 x\) or by \(\sinh^2 x\) gives two more, exactly as dividing \(\sin^2 + \cos^2 \equiv 1\) gives the tangent and cotangent identities.

:::eg (Exam style) Starting from the definitions in terms of \(e^u\), prove that \(1 - \tanh^2 u \equiv \operatorname{sech}^2 u\).
\[1 - \tanh^2 u = 1 - \frac{(e^u - e^{-u})^2}{(e^u + e^{-u})^2}\] [M1]
Use a common denominator:
\[= \frac{(e^u + e^{-u})^2 - (e^u - e^{-u})^2}{(e^u + e^{-u})^2}\] [M1]
The numerator is \((e^{2u} + 2 + e^{-2u}) - (e^{2u} - 2 + e^{-2u}) = 4\), so
\[1 - \tanh^2 u = \frac{4}{(e^u + e^{-u})^2} = \frac{1}{\cosh^2 u} = \operatorname{sech}^2 u\] [A1]
**Alternative**: divide \(\cosh^2 u - \sinh^2 u \equiv 1\) by \(\cosh^2 u\). Use that if the question does not say "from the definitions".
:::

:::key Hyperbolic identities
\[\begin{aligned}
\cosh^2 x - \sinh^2 x &\equiv 1 \\
1 - \tanh^2 x &\equiv \operatorname{sech}^2 x \\
\coth^2 x - 1 &\equiv \operatorname{cosech}^2 x
\end{aligned}\]
\[\begin{aligned}
\sinh 2x &\equiv 2\sinh x\cosh x \\
\cosh 2x &\equiv \cosh^2 x + \sinh^2 x \equiv 2\cosh^2 x - 1 \equiv 1 + 2\sinh^2 x \\
\tanh 2x &\equiv \frac{2\tanh x}{1 + \tanh^2 x}
\end{aligned}\]
\[\begin{aligned}
\sinh(A \pm B) &\equiv \sinh A\cosh B \pm \cosh A\sinh B \\
\cosh(A \pm B) &\equiv \cosh A\cosh B \pm \sinh A\sinh B \\
\tanh(A \pm B) &\equiv \frac{\tanh A \pm \tanh B}{1 \pm \tanh A\tanh B}
\end{aligned}\]
:::

Notice the signs: \(\cosh 2x\) contains \(\cosh^2 x + \sinh^2 x\) (plus), and \(\cosh(A + B)\) has a plus where \(\cos(A + B)\) has a minus. Everything else matches the trigonometric version.

### Osborn's rule: a checking tool, not a proof

**Osborn's rule** says: to turn a trigonometric identity into a hyperbolic one, replace each function by its hyperbolic version and change the sign of any term that contains a product of two sines (including \(\sin^2\), and \(\tan^2\) because \(\tan^2 = \sin^2/\cos^2\)). For example \(\cos 2x = \cos^2 x - \sin^2 x\) becomes \(\cosh 2x = \cosh^2 x + \sinh^2 x\). Use it to remember the identities and to spot a sign slip. It is **not** a proof: an exam question that says "prove" or "show that" wants the working from the definitions (or from an identity you have just proved).

:::eg (Exam style) Starting from the definitions in terms of exponentials, prove that \(\sinh(A + B) \equiv \sinh A\cosh B + \cosh A\sinh B\).
Work from the right-hand side:
\[\sinh A\cosh B + \cosh A\sinh B = \frac{(e^A - e^{-A})(e^B + e^{-B})}{4} + \frac{(e^A + e^{-A})(e^B - e^{-B})}{4}\] [M1]
Expand each product of brackets:
\[\begin{aligned}
(e^A - e^{-A})(e^B + e^{-B}) &= e^{A+B} + e^{A-B} - e^{-A+B} - e^{-A-B} \\
(e^A + e^{-A})(e^B - e^{-B}) &= e^{A+B} - e^{A-B} + e^{-A+B} - e^{-A-B}
\end{aligned}\] [M1]
Add them. The \(e^{A-B}\) and \(e^{-A+B}\) terms cancel:
\[\text{sum} = 2e^{A+B} - 2e^{-A-B}\] [A1]
Divide by 4:
\[\frac{2e^{A+B} - 2e^{-(A+B)}}{4} = \frac{e^{A+B} - e^{-(A+B)}}{2} = \sinh(A + B)\] [A1]
:::

The other compound-angle results follow the same way, or from this one. For example, dividing the formulas for \(\sinh(A + B)\) and \(\cosh(A + B)\) and then dividing top and bottom by \(\cosh A\cosh B\) gives \(\tanh(A + B)\). Put \(B = A\) to get the double-angle forms, and use \(\cosh^2 x - \sinh^2 x = 1\) for the other forms of \(\cosh 2x\) (for example \(\cosh^2 x + \sinh^2 x = 2\cosh^2 x - 1\)). The \(A - B\) versions follow by replacing \(B\) with \(-B\), since \(\sinh(-B) = -\sinh B\) and \(\cosh(-B) = \cosh B\).

:::eg (Exam style) Prove that \(\tanh(A + B) \equiv \dfrac{\tanh A + \tanh B}{1 + \tanh A\tanh B}\), using the compound-angle formulas for \(\sinh\) and \(\cosh\).
\[\tanh(A + B) = \frac{\sinh(A + B)}{\cosh(A + B)} = \frac{\sinh A\cosh B + \cosh A\sinh B}{\cosh A\cosh B + \sinh A\sinh B}\] [M1]
Divide every term, top and bottom, by \(\cosh A\cosh B\):
\[\tanh(A + B) = \frac{\dfrac{\sinh A}{\cosh A} + \dfrac{\sinh B}{\cosh B}}{1 + \dfrac{\sinh A}{\cosh A}\times\dfrac{\sinh B}{\cosh B}}\] [M1]
\[= \frac{\tanh A + \tanh B}{1 + \tanh A\tanh B}\] [A1]
:::

:::eg (Exam style) Prove that \(\dfrac{\sinh 2x}{1 + \cosh 2x} \equiv \tanh x\).
Use \(\sinh 2x = 2\sinh x\cosh x\) on the top, and \(\cosh 2x = 2\cosh^2 x - 1\) on the bottom:
\[\frac{\sinh 2x}{1 + \cosh 2x} = \frac{2\sinh x\cosh x}{1 + (2\cosh^2 x - 1)}\] [M1]
\[= \frac{2\sinh x\cosh x}{2\cosh^2 x}\] [M1]
\[= \frac{\sinh x}{\cosh x} = \tanh x\] [A1]
Choosing the form of \(\cosh 2x\) that makes the "1" cancel is the key. This is the hyperbolic partner of \(\dfrac{\sin 2x}{1 + \cos 2x} \equiv \tan x\).
:::

:::eg Given that \(\cosh x = \frac53\) and \(x > 0\), find the exact values of \(\sinh x\), \(\tanh x\), \(\sinh 2x\), \(\cosh 2x\) and \(e^x\).
From \(\cosh^2 x - \sinh^2 x = 1\): \(\sinh^2 x = \frac{25}{9} - 1 = \frac{16}{9}\). For \(x > 0\), \(\sinh x > 0\), so \(\sinh x = \frac43\).

\[\tanh x = \frac{4/3}{5/3} = \frac45\]
\[\sinh 2x = 2 \times \frac43 \times \frac53 = \frac{40}{9} \qquad \cosh 2x = \frac{25}{9} + \frac{16}{9} = \frac{41}{9}\]
\[e^x = \cosh x + \sinh x = \frac53 + \frac43 = 3\]
**Check**: \(\cosh^2 2x - \sinh^2 2x = \frac{1681 - 1600}{81} = 1\).
:::

The reciprocal functions need no new ideas: find the \(\cosh\), \(\sinh\) or \(\tanh\) first, then invert.

:::eg Given that \(\tanh x = \dfrac{5}{13}\), find \(\operatorname{sech} x\), \(\coth x\) and \(\operatorname{cosech} x\), given \(x > 0\).
\[\operatorname{sech}^2 x = 1 - \tanh^2 x = 1 - \frac{25}{169} = \frac{144}{169}\]
Since \(\operatorname{sech} x > 0\) always, \(\operatorname{sech} x = \tfrac{12}{13}\), so \(\cosh x = \tfrac{13}{12}\).

\[\coth x = \frac{1}{\tanh x} = \frac{13}{5}\]
\(\sinh x = \tanh x\cosh x = \tfrac{5}{13} \times \tfrac{13}{12} = \tfrac{5}{12}\), so \(\operatorname{cosech} x = \tfrac{12}{5}\).

**Check** with \(\coth^2 x - 1 = \operatorname{cosech}^2 x\): \(\tfrac{169}{25} - 1 = \tfrac{144}{25}\).
:::

:::warn Signs and the square root
Taking \(\sinh x = \pm\frac43\) loses a mark: the question's condition \(x > 0\) decides the sign (\(\sinh x\) has the same sign as \(x\)). And \(\cosh 2x \equiv \cosh^2 x - \sinh^2 x\) is wrong: that expression is always 1.
:::

## Inverse hyperbolic functions

The inverse of \(\sinh\) is easy: \(\sinh\) is increasing for all \(x\), so it has an inverse on the whole real line. \(\tanh\) is also increasing, and takes every value between \(-1\) and 1. But \(\cosh\) is not one-to-one (it is even), so we restrict it to \(x \ge 0\), exactly as we restrict \(\cos\) to \([0, \pi]\) to define \(\cos^{-1}\).

:::def Inverse hyperbolic functions
\(y = \sinh^{-1} x\) means \(x = \sinh y\), for all real \(x\) (range: all real \(y\)).

\(y = \cosh^{-1} x\) means \(x = \cosh y\) with \(y \ge 0\), for \(x \ge 1\) (range: \(y \ge 0\)).

\(y = \tanh^{-1} x\) means \(x = \tanh y\), for \(-1 < x < 1\) (range: all real \(y\)).

They are also called \(\operatorname{arsinh}\), \(\operatorname{arcosh}\) and \(\operatorname{artanh}\). Note that \(\sinh^{-1} x\) means the inverse function, not \(\dfrac{1}{\sinh x}\).
:::

:::plot The curves y = sinh⁻¹x and y = cosh⁻¹x are reflections of y = sinh x and the right-hand half of y = cosh x in the line y = x. cosh⁻¹x starts at (1, 0) and has vertical gradient there.
--f "log(x+sqrt(x**2+1))" --f "log(x+sqrt(x**2-1))+0*sqrt(x-1)" --label "y = sinh⁻¹x" --label "y = cosh⁻¹x" --x -3 6 --y -2.5 3 --pt "1,0,(1, 0)@se" --legend tl
:::

Because \(\sinh\) and \(\cosh\) are built from \(e^x\), their inverses can be written with natural logarithms. MF19 lists the results, but "show that" or "derive" questions want the working.

:::key Logarithmic forms of the inverses
\[\begin{aligned}
\sinh^{-1} x &= \ln\left(x + \sqrt{x^2 + 1}\right) \\
\cosh^{-1} x &= \ln\left(x + \sqrt{x^2 - 1}\right), \quad x \ge 1 \\
\tanh^{-1} x &= \tfrac12\ln\frac{1 + x}{1 - x}, \quad \lvert x \rvert < 1
\end{aligned}\]
These are given in MF19. If a question says "show that" or "prove", derive them as below.
:::

:::eg (Exam style) Show that \(\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)\).
Let \(y = \sinh^{-1} x\), so \(x = \sinh y = \dfrac{e^y - e^{-y}}{2}\). Multiply by \(2e^y\):
\[2xe^y = e^{2y} - 1\] [M1]
Rearrange into a quadratic in \(e^y\):
\[\left(e^y\right)^2 - 2x\,e^y - 1 = 0\] [A1]
Solve with the quadratic formula:
\[e^y = \frac{2x \pm \sqrt{4x^2 + 4}}{2} = x \pm \sqrt{x^2 + 1}\] [M1]
Now \(e^y > 0\). Since \(\sqrt{x^2 + 1} > \lvert x \rvert\), the root \(x - \sqrt{x^2 + 1}\) is negative and is rejected. So \(e^y = x + \sqrt{x^2 + 1}\) and
\[y = \ln\left(x + \sqrt{x^2 + 1}\right)\] [A1]
:::

The same method works for \(\cosh^{-1}\), but this time both roots are positive, and the condition \(y \ge 0\) has to choose.

:::eg (Exam style) Show that \(\cosh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right)\) for \(x \ge 1\).
Let \(y = \cosh^{-1} x\), so \(y \ge 0\) and \(x = \cosh y = \dfrac{e^y + e^{-y}}{2}\). Multiply by \(2e^y\):
\[2xe^y = e^{2y} + 1\] [M1]
\[\left(e^y\right)^2 - 2x\,e^y + 1 = 0\] [A1]
\[e^y = x \pm \sqrt{x^2 - 1}\] [M1]
For \(x \ge 1\) both values are positive, and their product is 1, so the smaller one is the reciprocal of the larger. Since \(y \ge 0\), \(e^y \ge 1\), which is the larger root:
\[y = \ln\left(x + \sqrt{x^2 - 1}\right)\] [A1]
The other root gives \(y = -\ln\left(x + \sqrt{x^2 - 1}\right)\), which is negative, so it would be \(-\cosh^{-1} x\).
:::

:::eg (Exam style) Show that \(\tanh^{-1} x = \tfrac12\ln\dfrac{1 + x}{1 - x}\) for \(\lvert x \rvert < 1\).
Let \(y = \tanh^{-1} x\), so
\[x = \tanh y = \frac{e^y - e^{-y}}{e^y + e^{-y}} = \frac{e^{2y} - 1}{e^{2y} + 1}\] [M1]
(multiply top and bottom by \(e^y\)). Rearrange for \(e^{2y}\):
\[x\,e^{2y} + x = e^{2y} - 1\ \Rightarrow\ e^{2y}(1 - x) = 1 + x\] [M1]
\[e^{2y} = \frac{1 + x}{1 - x}, \quad y = \tfrac12\ln\frac{1 + x}{1 - x}\] [A1]
:::

:::warn \(\cosh^{-1}\) has one value, not two
Solving \(\cosh y = 2\) gives \(y = \pm\ln\left(2 + \sqrt3\right)\), but \(\cosh^{-1} 2\) is only the positive one, \(\ln\left(2 + \sqrt3\right)\). Put the \(\pm\) in when you solve an equation for \(x\) from \(\cosh x\); never write it in \(\cosh^{-1} x\) itself.
:::

:::eg Find exact values of (a) \(\sinh^{-1}\tfrac34\), (b) \(\cosh^{-1} 2\), (c) \(\tanh^{-1}\tfrac12\).
(a) \(\sqrt{\tfrac{9}{16} + 1} = \tfrac54\), so \(\sinh^{-1}\tfrac34 = \ln\left(\tfrac34 + \tfrac54\right) = \ln 2\).

(b) \(\sqrt{4 - 1} = \sqrt3\), so \(\cosh^{-1} 2 = \ln\left(2 + \sqrt3\right)\).

(c) \(\tanh^{-1}\tfrac12 = \tfrac12\ln\dfrac{3/2}{1/2} = \tfrac12\ln 3\).

**Check** (a): \(\sinh(\ln 2) = \dfrac{2 - \frac12}{2} = \dfrac34\).
:::

:::eg Return to the cable \(y = 25\cosh\frac{x}{25} - 19\). At what horizontal distances from the lowest point is the cable 8 m above the ground?
\[\begin{aligned}
25\cosh\frac{x}{25} - 19 &= 8 \\
\cosh\frac{x}{25} &= \frac{27}{25} = 1.08
\end{aligned}\]
Now invert, remembering the cable is symmetric so there are two solutions:
\[\frac{x}{25} = \pm\cosh^{-1} 1.08 = \pm\ln\left(1.08 + \sqrt{1.08^2 - 1}\right) = \pm 0.3974\]
So \(x = \pm 9.93\) m (3 s.f.), about 9.9 m either side of the lowest point.
:::

## Solving hyperbolic equations

There are two main methods. Choose by looking at what the equation contains.

:::steps
1. If the equation mixes \(\cosh x\) and \(\sinh x\) to the first power (\(a\cosh x + b\sinh x = c\)), write both in terms of \(e^x\), put \(t = e^x\), multiply by \(t\) to clear \(e^{-x} = \frac1t\), and solve the quadratic in \(t\).
2. Reject any \(t \le 0\) with a reason: \(e^x\) is always positive. Then \(x = \ln t\).
3. If the equation has squares or a double angle, use an identity to get an equation in one function, solve for that function, and use the log form or the inverse key.
4. Check each answer in the original equation.
:::

:::eg Solve \(4\sinh x + 3\cosh x = 4\), giving the exact solution.
Put \(t = e^x\) with \(\sinh x = \frac12\left(t - \frac1t\right)\) and \(\cosh x = \frac12\left(t + \frac1t\right)\):
\[2\left(t - \frac1t\right) + \frac32\left(t + \frac1t\right) = 4\]
Combine like terms and multiply by \(2t\):
\[\begin{aligned}
\tfrac72 t - \tfrac1{2t} &= 4 \\
7t^2 - 8t - 1 &= 0
\end{aligned}\]
\[t = \frac{8 \pm \sqrt{92}}{14} = \frac{4 \pm \sqrt{23}}{7}\]
Since \(e^x > 0\) and \(\sqrt{23} > 4\), the root \(\frac{4 - \sqrt{23}}{7}\) is negative: reject it. So
\[x = \ln\left(\frac{4 + \sqrt{23}}{7}\right) = 0.228\ (3\ \text{s.f.})\]
**Check**: \(x = 0.2284\) gives \(4(0.2304) + 3(1.0261) = 4.00\).
:::

:::eg (Exam style) Solve \(\cosh 2x = 3\sinh x + 1\), giving the answers in exact logarithmic form.
Use \(\cosh 2x = 1 + 2\sinh^2 x\) so the equation involves only \(\sinh x\):
\[1 + 2\sinh^2 x = 3\sinh x + 1\] [M1]
\[\sinh x\,(2\sinh x - 3) = 0\] [A1]
So \(\sinh x = 0\) or \(\sinh x = \tfrac32\).

\(\sinh x = 0\) gives \(x = 0\). [B1]

\(\sinh x = \tfrac32\) gives
\[x = \ln\left(\tfrac32 + \sqrt{\tfrac94 + 1}\right) = \ln\frac{3 + \sqrt{13}}{2}\] [M1 A1]
Numerically \(x = 1.19\). Dividing both sides by \(\sinh x\) at the start would have lost the root \(x = 0\).
:::

:::eg Solve \(3\cosh x = 2 + 4\sinh^2 x\).
Use \(\sinh^2 x = \cosh^2 x - 1\):
\[\begin{aligned}
3\cosh x &= 2 + 4\cosh^2 x - 4 \\
4\cosh^2 x - 3\cosh x - 2 &= 0
\end{aligned}\]
\[\cosh x = \frac{3 \pm \sqrt{41}}{8}\]
\(\cosh x \ge 1\), and \(\frac{3 - \sqrt{41}}{8} < 0\), so only \(\cosh x = \frac{3 + \sqrt{41}}{8} = 1.175\) is possible. Because \(\cosh\) is even there are two solutions:
\[x = \pm\ln\left(c + \sqrt{c^2 - 1}\right), \quad c = \frac{3 + \sqrt{41}}{8}\]
\[x = \pm 0.5839\ \text{(4 s.f.)}\]
:::

:::eg Solve \(\tanh 2x = \tfrac45\) in two ways: (a) directly, (b) using the double-angle formula for \(\tanh 2x\).
(a) \(2x = \tanh^{-1}\tfrac45 = \tfrac12\ln\dfrac{9/5}{1/5} = \tfrac12\ln 9 = \ln 3\), so \(x = \tfrac12\ln 3\).

(b) Put \(t = \tanh x\) in \(\tanh 2x = \dfrac{2t}{1 + t^2}\):
\[\begin{aligned}
\frac{2t}{1 + t^2} &= \frac45 \\
10t &= 4 + 4t^2 \\
2t^2 - 5t + 2 &= 0 \\
(2t - 1)(t - 2) &= 0
\end{aligned}\]
\(\tanh x\) must lie between \(-1\) and 1, so \(t = 2\) is rejected and \(t = \tfrac12\). Then \(x = \tanh^{-1}\tfrac12 = \tfrac12\ln 3\), the same answer.
:::

:::eg A skydiver of a certain design falls with speed \(v = 40\tanh(0.25t)\) m s\(^{-1}\) at time \(t\) seconds. (a) Find the speed the skydiver approaches. (b) Find the exact time at which the speed is 30 m s\(^{-1}\).
(a) As \(t \to \infty\), \(\tanh(0.25t) \to 1\), so \(v \to 40\) m s\(^{-1}\): the terminal speed.

(b) \(40\tanh(0.25t) = 30\) gives \(\tanh(0.25t) = \tfrac34\).
\[0.25t = \tanh^{-1}\tfrac34 = \tfrac12\ln\frac{7/4}{1/4} = \tfrac12\ln 7\]
\[t = 2\ln 7 = 3.89\ \text{s}\ (3\ \text{s.f.})\]
:::

:::eg For waves of wavelength \(\lambda = 60\) m on water of depth \(d\) metres, a standard model gives the wave speed \(c\) by \(c^2 = \dfrac{g\lambda}{2\pi}\tanh\dfrac{2\pi d}{\lambda}\). Take \(g = 10\). (a) Find the speed in very deep water. (b) Find the speed when \(d = 10\). (c) Find the depth at which the speed is 95% of the deep-water speed.
(a) For deep water \(\tanh \to 1\), so
\[c^2 = \frac{10 \times 60}{2\pi} = 95.49, \quad c = 9.77\ \text{m s}^{-1}\]
(b) With \(d = 10\), \(\tanh\dfrac{2\pi \times 10}{60} = \tanh 1.0472 = 0.7807\). Then \(c^2 = 95.49 \times 0.7807 = 74.55\), so \(c = 8.63\) m s\(^{-1}\).

(c) Speed 95% of the deep-water value means \(c^2\) is \(0.95^2 = 0.9025\) of the deep-water value, so \(\tanh\dfrac{2\pi d}{60} = 0.9025\):
\[\frac{2\pi d}{60} = \tanh^{-1} 0.9025 = \tfrac12\ln\frac{1.9025}{0.0975} = 1.4855\]
\[d = \frac{60 \times 1.4855}{2\pi} = 14.2\ \text{m}\]
The model says that in water deeper than about 14 m (a quarter of the wavelength) waves travel at nearly their deep-water speed.
:::

:::exam Hyperbolic equations in the exam
Give exact answers in logarithmic form unless the question asks for decimals. State why you reject a root ("\(e^x > 0\)" or "\(\cosh x \ge 1\)"); a bare crossing-out loses the accuracy mark. MF19 gives \(\cosh^2 - \sinh^2 \equiv 1\), \(\sinh 2x\), \(\cosh 2x \equiv \cosh^2 + \sinh^2\), and the three log forms. It does **not** give the other double-angle forms, the compound-angle formulas or the reciprocal identities: learn them or derive them from the first three.
:::

:::board
UK Further Maths (Edexcel 9FM0 Core Pure) includes hyperbolic functions and their inverses; Edexcel writes the inverses as \(\operatorname{arsinh}\), \(\operatorname{arcosh}\) and \(\operatorname{artanh}\). The definitions, identities and logarithmic forms are the same as here.
:::

:::eg Spot the error: given that \(\sinh x = \frac34\), find the value of \(\cosh 2x\) for 3 marks.
A student wrote this answer.

Line 1: \(\cosh^2 x = 1 + \sinh^2 x = 1 + \tfrac{9}{16} = \tfrac{25}{16}\), so \(\cosh x = \tfrac54\).
Line 2: \(\cosh 2x = \cosh^2 x - \sinh^2 x = \tfrac{25}{16} - \tfrac{9}{16} = 1\)

Line 1 is correct and earns the first mark. [B1]

**Line 2 uses a wrong formula, so the method mark is lost and the accuracy mark with it.** [M0] [A0] The expression \(\cosh^2 x - \sinh^2 x\) is the identity that always equals 1; \(\cosh 2x\) is \(\cosh^2 x + \sinh^2 x\). The student scores 1 out of 3.

Correct line 2: \(\cosh 2x = \tfrac{25}{16} + \tfrac{9}{16} = \tfrac{17}{8}\). [M1] [A1]

**Check**: \(\sinh x = \tfrac34\) means \(x = \ln 2\), and \(\cosh(2\ln 2) = \dfrac{4 + \frac14}{2} = \dfrac{17}{8}\).
:::

:::try Start easy, finish at exam standard
Q: Use your calculator to find \(\sinh 1.5\), \(\cosh 1.5\) and \(\tanh 1.5\) to 4 significant figures, and check that \(\cosh^2 1.5 - \sinh^2 1.5 = 1\).
A: \(\sinh 1.5 = 2.129\), \(\cosh 1.5 = 2.352\), \(\tanh 1.5 = 0.9051\). Then \(5.534 - 4.534 = 1.000\).
Q: Write down the range of \(y = 3\cosh x\) and the equation of the asymptotes of \(y = 5\tanh x\).
A: \(\cosh x \ge 1\), so \(y \ge 3\). The asymptotes of \(y = 5\tanh x\) are \(y = 5\) and \(y = -5\).
Q: Given that \(\sinh x = \tfrac{12}{5}\), find \(\cosh x\), \(\tanh x\) and \(x\) in exact form.
A: \(\cosh^2 x = 1 + \tfrac{144}{25} = \tfrac{169}{25}\), and \(\cosh x > 0\), so \(\cosh x = \tfrac{13}{5}\). Then \(\tanh x = \tfrac{12}{13}\). \(e^x = \tfrac{13}{5} + \tfrac{12}{5} = 5\), so \(x = \ln 5\).
Q: Express \(\sinh 3x\) in terms of \(\sinh x\) only.
A: \(\sinh 3x = \sinh 2x\cosh x + \cosh 2x\sinh x = 2\sinh x\cosh^2 x + (1 + 2\sinh^2 x)\sinh x\). Put \(\cosh^2 x = 1 + \sinh^2 x\): \(2s(1 + s^2) + s + 2s^3 = 4s^3 + 3s\). So \(\sinh 3x = 4\sinh^3 x + 3\sinh x\).
Q: Find exact values of \(\sinh^{-1}\tfrac{5}{12}\) and \(\cosh^{-1}\tfrac{17}{8}\).
A: \(\sqrt{\tfrac{25}{144} + 1} = \tfrac{13}{12}\), so \(\sinh^{-1}\tfrac{5}{12} = \ln\tfrac{18}{12} = \ln\tfrac32\). \(\sqrt{\tfrac{289}{64} - 1} = \tfrac{15}{8}\), so \(\cosh^{-1}\tfrac{17}{8} = \ln 4\).
Q: Solve \(\tanh x = \tfrac35\), giving \(x\) in the form \(\ln k\).
A: \(x = \tfrac12\ln\dfrac{8/5}{2/5} = \tfrac12\ln 4 = \ln 2\).
Q: Solve \(\cosh x + \sinh x = 5\).
A: \(\cosh x + \sinh x = e^x\), so \(e^x = 5\) and \(x = \ln 5\).
Q: Solve \(5\cosh x - 3\sinh x = 5\).
A: With \(t = e^x\): \(\tfrac52\left(t + \tfrac1t\right) - \tfrac32\left(t - \tfrac1t\right) = 5\), that is \(t + \tfrac4t = 5\), so \(t^2 - 5t + 4 = 0\) and \(t = 1\) or \(t = 4\). Then \(x = 0\) or \(x = \ln 4\).
Q: Prove that \(\cosh x + \sinh x \equiv e^x\) and hence that \((\cosh x + \sinh x)^n \equiv \cosh nx + \sinh nx\).
A: \(\cosh x + \sinh x = \dfrac{e^x + e^{-x} + e^x - e^{-x}}{2} = e^x\). Then \((e^x)^n = e^{nx} = \cosh nx + \sinh nx\).
Q: Solve \(2\sinh^2 x - 3\cosh x = 0\).
A: \(2(\cosh^2 x - 1) - 3\cosh x = 0\), so \(2\cosh^2 x - 3\cosh x - 2 = 0\) and \((2\cosh x + 1)(\cosh x - 2) = 0\). \(\cosh x = -\tfrac12\) is impossible, so \(\cosh x = 2\) and \(x = \pm\ln\left(2 + \sqrt3\right)\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Given that \(\sinh x = \frac{5}{12}\), find the exact values of \(\cosh x\) and \(\tanh x\), and show that \(e^x = \frac32\).
A: \(\cosh^2 x = 1 + \tfrac{25}{144} = \tfrac{169}{144}\), and \(\cosh x > 0\), so \(\cosh x = \tfrac{13}{12}\). [B1] \(\tanh x = \tfrac{5/12}{13/12} = \tfrac{5}{13}\). [B1] \(e^x = \cosh x + \sinh x = \tfrac{18}{12} = \tfrac32\). [B1]
Q: [3 marks] ★★ Starting from the definitions in terms of exponentials, prove that \(\sinh 2x \equiv 2\sinh x\cosh x\).
A: \(2\sinh x\cosh x = 2 \times \dfrac{e^x - e^{-x}}{2} \times \dfrac{e^x + e^{-x}}{2}\) [M1]
\[= \frac{e^{2x} - e^{-2x}}{2}\] [M1]
since \((e^x - e^{-x})(e^x + e^{-x}) = e^{2x} - e^{-2x}\). This is \(\sinh 2x\). [A1]
Q: [5 marks] ★★ Solve \(7\cosh x - 3\sinh x = 8\), giving the answers in exact logarithmic form.
A: With \(t = e^x\): \(\tfrac72\left(t + \tfrac1t\right) - \tfrac32\left(t - \tfrac1t\right) = 8\). [M1]
\[2t + \frac5t = 8\ \Rightarrow\ 2t^2 - 8t + 5 = 0\] [A1]
\[t = \frac{8 \pm \sqrt{24}}{4} = 2 \pm \frac{\sqrt6}{2}\] [M1]
Both values are positive, so \(x = \ln\left(2 + \tfrac{\sqrt6}{2}\right)\) [A1] or \(x = \ln\left(2 - \tfrac{\sqrt6}{2}\right)\). [A1]
Q: [5 marks] ★★ Solve \(\cosh 2x - 5\sinh x = 7\), giving the answers in exact logarithmic form.
A: \(1 + 2\sinh^2 x - 5\sinh x = 7\) [M1], so \(2\sinh^2 x - 5\sinh x - 6 = 0\). [A1]
\[\sinh x = \frac{5 \pm \sqrt{73}}{4}\] [M1]
Each value is attainable because \(\sinh\) takes every real value. With \(s = \frac{5 \pm \sqrt{73}}{4}\), \(x = \ln\left(s + \sqrt{s^2 + 1}\right)\): about \(1.93\) [A1] and \(-0.798\). [A1]
Q: [4 marks] ★ Find the exact value of (a) \(\sinh^{-1}\frac{8}{15}\), (b) \(\cosh^{-1}\frac{13}{5}\), giving each as a single logarithm.
A: (a) \(\sqrt{\tfrac{64}{225} + 1} = \tfrac{17}{15}\) [M1], so \(\sinh^{-1}\tfrac{8}{15} = \ln\tfrac{25}{15} = \ln\tfrac53\). [A1]
(b) \(\sqrt{\tfrac{169}{25} - 1} = \tfrac{12}{5}\) [M1], so \(\cosh^{-1}\tfrac{13}{5} = \ln 5\). [A1]
Q: [4 marks] ★★ A falling object has speed \(v = 30\tanh(0.3t)\) m s\(^{-1}\) after \(t\) seconds. (a) Write down the speed it approaches. (b) Find the time when its speed is 90% of that value.
A: (a) 30 m s\(^{-1}\), since \(\tanh \to 1\). [B1]
(b) \(\tanh(0.3t) = 0.9\), so \(0.3t = \tfrac12\ln\dfrac{1.9}{0.1}\) [M1] \(= \tfrac12\ln 19\). [A1] \(t = \dfrac{\ln 19}{0.6} = 4.91\) s. [A1]
Q: [3 marks] ★★ Use the compound-angle formula for \(\tanh(A + B)\) to show that \(\tanh^{-1} x + \tanh^{-1} y = \tanh^{-1}\dfrac{x + y}{1 + xy}\), where \(\lvert x \rvert, \lvert y \rvert < 1\).
A: Let \(A = \tanh^{-1} x\) and \(B = \tanh^{-1} y\), so \(\tanh A = x\) and \(\tanh B = y\). [B1]
\[\tanh(A + B) = \frac{x + y}{1 + xy}\] [M1]
Apply \(\tanh^{-1}\) to both sides: \(A + B = \tanh^{-1}\dfrac{x + y}{1 + xy}\). [A1]
Q: [5 marks] ★★ The curves \(y = 2\cosh x\) and \(y = 3 + \sinh x\) intersect. Find the \(x\)-coordinates of the points of intersection in exact form, and the corresponding \(y\)-coordinates to 3 significant figures.
A: \(2\cosh x - \sinh x = 3\). With \(t = e^x\): \(\left(t + \tfrac1t\right) - \tfrac12\left(t - \tfrac1t\right) = 3\). [M1]
\[\tfrac t2 + \tfrac{3}{2t} = 3\ \Rightarrow\ t^2 - 6t + 3 = 0\] [A1]
\(t = 3 \pm \sqrt6\), both positive. [M1]
\(x = \ln\left(3 + \sqrt6\right)\) and \(x = \ln\left(3 - \sqrt6\right)\). [A1]
The \(y\)-values are \(5.63\) and \(2.37\). [A1]
Q: [8 marks] (#math.p3.trig) ★★★ (a) Prove that \(\cosh 3x \equiv 4\cosh^3 x - 3\cosh x\). (b) Hence solve \(\cosh 3x = 11\cosh x\), giving the answers in exact form.
H: Write \(3x = 2x + x\) and use the compound-angle formula for \(\cosh(A + B)\).
H: Use \(\cosh 2x = 2\cosh^2 x - 1\) and \(\sinh 2x = 2\sinh x\cosh x\), then replace \(\sinh^2 x\) by \(\cosh^2 x - 1\).
H: In (b), after substituting you can divide by \(\cosh x\) because it is never zero.
A: (a) \(\cosh 3x = \cosh 2x\cosh x + \sinh 2x\sinh x\) [M1]
\[= (2\cosh^2 x - 1)\cosh x + 2\sinh^2 x\cosh x\] [M1]
\[= (2\cosh^2 x - 1)\cosh x + 2(\cosh^2 x - 1)\cosh x\] [M1]
\[= 4\cosh^3 x - 3\cosh x\] [A1]
(b) \(4\cosh^3 x - 3\cosh x = 11\cosh x\), and \(\cosh x \ne 0\), so \(\cosh^2 x = \tfrac72\). [M1 A1]
\(\cosh x = \sqrt{\tfrac72}\) (positive). [B1]
\[x = \pm\ln\left(\sqrt{\tfrac72} + \sqrt{\tfrac52}\right)\] [A1]
Q: [8 marks] (#math.fm.series) ★★★ (a) Show that \(2\sinh\tfrac12\cosh r \equiv \sinh\left(r + \tfrac12\right) - \sinh\left(r - \tfrac12\right)\). (b) Use the method of differences to show that \(\displaystyle\sum_{r=1}^{n}\cosh r = \dfrac{\sinh\left(n + \frac12\right) - \sinh\frac12}{2\sinh\frac12}\). (c) Find \(\displaystyle\sum_{r=1}^{10}\cosh r\) to 3 significant figures.
H: Expand \(\sinh\left(r + \tfrac12\right)\) and \(\sinh\left(r - \tfrac12\right)\) with the compound-angle formula; most terms cancel.
H: Write out the first three and last two lines of \(\sum \left[\sinh\left(r + \tfrac12\right) - \sinh\left(r - \tfrac12\right)\right]\) and cancel.
A: (a) Expand with the compound-angle formulas:
\[\begin{aligned}
&\sinh\left(r + \tfrac12\right) - \sinh\left(r - \tfrac12\right) \\
&= \left(\sinh r\cosh\tfrac12 + \cosh r\sinh\tfrac12\right) \\
&\quad - \left(\sinh r\cosh\tfrac12 - \cosh r\sinh\tfrac12\right)
\end{aligned}\] [M1]
\[= 2\cosh r\sinh\tfrac12\] [A1]
(b) \(2\sinh\tfrac12\sum\cosh r = \sum\left[\sinh\left(r + \tfrac12\right) - \sinh\left(r - \tfrac12\right)\right]\) [M1]
The sum telescopes to \(\sinh\left(n + \tfrac12\right) - \sinh\tfrac12\) [M1 A1], and dividing by \(2\sinh\tfrac12\) gives the result. [A1]
(c) \(\dfrac{\sinh 10.5 - \sinh 0.5}{2\sinh 0.5}\) [M1] \(= 11\,300\) (3 s.f.), that is \(1.13 \times 10^4\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ (a) Express \(5\cosh x - 4\sinh x\) in the form \(R\cosh(x - \alpha)\), where \(R > 0\), giving \(R\) and \(\alpha\) exactly. (b) Write down the least value of \(5\cosh x - 4\sinh x\). (c) Solve \(5\cosh x - 4\sinh x = 5\).
H: Expand \(R\cosh(x - \alpha) = R\cosh x\cosh\alpha - R\sinh x\sinh\alpha\) and compare coefficients.
H: Divide the two equations to get \(\tanh\alpha\), then use \(\cosh^2 - \sinh^2 = 1\) to find \(R\).
H: In (c) the equation becomes \(\cosh(x - \alpha) = \frac53\).
A: (a) \(R\cosh\alpha = 5\) and \(R\sinh\alpha = 4\). [M1]
Dividing, \(\tanh\alpha = \tfrac45\), so \(\alpha = \tfrac12\ln\dfrac{9/5}{1/5} = \ln 3\). [A1]
\(R^2\left(\cosh^2\alpha - \sinh^2\alpha\right) = 25 - 16 = 9\), so \(R = 3\). [M1 A1]
So \(5\cosh x - 4\sinh x = 3\cosh(x - \ln 3)\).
(b) The least value of \(\cosh\) is 1, so the least value is 3. [B1]
(c) \(\cosh(x - \ln 3) = \tfrac53\), so \(x - \ln 3 = \pm\ln\left(\tfrac53 + \tfrac43\right) = \pm\ln 3\). [M1 A1]
So \(x = 2\ln 3\) or \(x = 0\). [A1]
Q: [8 marks] ★★★ Let \(t = \tanh\tfrac{x}{2}\). (a) Show that \(\sinh x = \dfrac{2t}{1 - t^2}\) and \(\cosh x = \dfrac{1 + t^2}{1 - t^2}\). (b) Hence solve \(3\cosh x + 5\sinh x = 5\), giving the answer in exact form.
H: Use \(\sinh x = 2\sinh\tfrac{x}{2}\cosh\tfrac{x}{2}\) and divide top and bottom by \(\cosh^2\tfrac{x}{2}\).
H: For \(\cosh x\) use \(\cosh x = \cosh^2\tfrac{x}{2} + \sinh^2\tfrac{x}{2}\), and \(1 - \tanh^2 = \operatorname{sech}^2\).
H: In (b) a quadratic in \(t\) has two roots, but \(\lvert t \rvert < 1\).
A: (a) Use \(1 = \cosh^2\tfrac{x}{2} - \sinh^2\tfrac{x}{2}\): \(\sinh x = \dfrac{2\sinh\frac{x}{2}\cosh\frac{x}{2}}{\cosh^2\frac{x}{2} - \sinh^2\frac{x}{2}}\). [M1]
Divide top and bottom by \(\cosh^2\tfrac{x}{2}\): \(\sinh x = \dfrac{2t}{1 - t^2}\). [A1]
\(\cosh x = \dfrac{\cosh^2\frac{x}{2} + \sinh^2\frac{x}{2}}{\cosh^2\frac{x}{2} - \sinh^2\frac{x}{2}}\) [M1] \(= \dfrac{1 + t^2}{1 - t^2}\). [A1]
(b) \(3(1 + t^2) + 10t = 5(1 - t^2)\) [M1], so \(4t^2 + 5t - 1 = 0\). [A1]
\(t = \dfrac{-5 \pm \sqrt{41}}{8}\). Since \(\lvert t \rvert < 1\), only \(t = \dfrac{-5 + \sqrt{41}}{8}\) is possible. [M1]
\(x = 2\tanh^{-1} t = \ln\dfrac{1 + t}{1 - t} = \ln\dfrac{5 + \sqrt{41}}{8}\) \((= 0.354)\). [A1]
:::

:::quiz
? Which identity is correct?
+ \(\cosh^2 x - \sinh^2 x \equiv 1\)
- \(\cosh^2 x + \sinh^2 x \equiv 1\)
- \(\sinh^2 x - \cosh^2 x \equiv 1\)
- \(\cosh^2 x - \sinh^2 x \equiv -1\)
> The hyperbolic identity has a minus sign: \(\cosh^2 x - \sinh^2 x = 1\). The sum \(\cosh^2 x + \sinh^2 x\) is \(\cosh 2x\), not 1, and the reverse difference is \(-1\).
? Given that \(\cosh x = \frac54\) and \(x < 0\), what is \(\sinh x\)?
+ \(-\dfrac34\)
- \(\dfrac34\)
- \(\pm\dfrac34\)
- \(\dfrac{9}{16}\)
> \(\sinh^2 x = \frac{25}{16} - 1 = \frac{9}{16}\), and \(\sinh x\) has the same sign as \(x\), so it is \(-\frac34\). Writing \(\pm\) ignores the condition; \(\frac{9}{16}\) is \(\sinh^2 x\).
? Which is equal to \(\cosh 2x\)?
- \(\cosh^2 x - \sinh^2 x\)
- \(2\sinh x\cosh x\)
+ \(1 + 2\sinh^2 x\)
- \(2\cosh^2 x + 1\)
> \(\cosh 2x = \cosh^2 x + \sinh^2 x = 1 + 2\sinh^2 x = 2\cosh^2 x - 1\). The first option is always 1, the second is \(\sinh 2x\), and the last has the wrong sign.
? What is the range of \(y = \tanh x\)?
- \(y \ge 1\)
- all real numbers
+ \(-1 < y < 1\)
- \(-1 \le y \le 1\)
> \(\tanh x\) approaches \(\pm 1\) but never reaches them, so the inequalities are strict. All reals is the range of \(\sinh x\), and \(y \ge 1\) is the range of \(\cosh x\).
? Solving \(\cosh x = 2\) gives which values of \(x\)?
- \(\ln\left(2 + \sqrt3\right)\) only
+ \(\pm\ln\left(2 + \sqrt3\right)\)
- \(\ln\left(2 - \sqrt3\right)\) only
- \(\ln 2\) or \(-\ln 2\)
> \(\cosh\) is even, so the solutions come in a pair: \(x = \pm\cosh^{-1} 2\), and \(\cosh^{-1} 2 = \ln\left(2 + \sqrt3\right)\). \(\ln 2\) comes from forgetting the \(\sqrt{x^2 - 1}\) term.
? Which is a correct statement about \(\sinh^{-1} x\)?
- It equals \(\dfrac{1}{\sinh x}\)
- It is defined only for \(x \ge 0\)
+ \(\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)\) for all real \(x\)
- \(\sinh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right)\)
> \(\sinh^{-1}\) is the inverse function, defined for every real \(x\); the reciprocal is \(\operatorname{cosech} x\). The \(x^2 - 1\) form belongs to \(\cosh^{-1}\).
? In the substitution \(t = e^x\) for \(a\cosh x + b\sinh x = c\), a root \(t = -0.4\) should be
- kept, giving \(x = \ln 0.4\)
+ rejected, because \(e^x > 0\) for all real \(x\)
- kept, giving \(x = -\ln 0.4\)
- rejected only if \(c\) is negative
> \(e^x\) is always positive, so a negative \(t\) corresponds to no real \(x\). Taking \(\ln\) of a negative number is not allowed.
:::

:::checklist What you can now do
- [ ] I can write down the definitions of \(\sinh x\), \(\cosh x\), \(\tanh x\), \(\operatorname{sech} x\), \(\operatorname{cosech} x\) and \(\coth x\) in terms of \(e^x\), and use \(e^{\pm x} = \cosh x \pm \sinh x\).
- [ ] I can sketch the graphs of all six hyperbolic functions, marking asymptotes and intercepts, and state their domains and ranges.
- [ ] I can prove hyperbolic identities from the definitions, and use them (including double-angle and compound-angle forms).
- [ ] I can use Osborn's rule as a check, and I know it is not a proof.
- [ ] I can solve equations of the form \(a\cosh x + b\sinh x = c\) using \(t = e^x\), rejecting invalid roots with a reason.
- [ ] I can solve equations involving squares or double angles by turning them into one hyperbolic function.
- [ ] I can state the domain and range of \(\sinh^{-1}\), \(\cosh^{-1}\) and \(\tanh^{-1}\).
- [ ] I can derive the logarithmic forms of the inverse functions and use them to find exact values.
:::

:::recap
- \(\sinh x = \dfrac{e^x - e^{-x}}{2}\), \(\cosh x = \dfrac{e^x + e^{-x}}{2}\), \(\tanh x = \dfrac{\sinh x}{\cosh x}\); \(\operatorname{sech}\), \(\operatorname{cosech}\) and \(\coth\) are reciprocals. \(e^{\pm x} = \cosh x \pm \sinh x\).
- \(\cosh\) is even with minimum value 1; \(\sinh\) and \(\tanh\) are odd; \(\tanh\) lies between \(-1\) and 1.
- \(\cosh^2 x - \sinh^2 x \equiv 1\); \(1 - \tanh^2 x \equiv \operatorname{sech}^2 x\); \(\coth^2 x - 1 \equiv \operatorname{cosech}^2 x\).
- \(\sinh 2x \equiv 2\sinh x\cosh x\); \(\cosh 2x \equiv \cosh^2 x + \sinh^2 x \equiv 2\cosh^2 x - 1 \equiv 1 + 2\sinh^2 x\). Compound angles: \(\cosh(A + B)\) has a plus where \(\cos(A + B)\) has a minus.
- Osborn's rule: replace each function and change the sign of any product of two sines. A checking tool only.
- Solve \(a\cosh x + b\sinh x = c\) with \(t = e^x\) (reject \(t \le 0\)); otherwise use an identity to get one function.
- \(\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)\); \(\cosh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right)\) for \(x \ge 1\), with \(\cosh^{-1} x \ge 0\); \(\tanh^{-1} x = \frac12\ln\frac{1 + x}{1 - x}\) for \(\lvert x \rvert < 1\). Derive them by solving a quadratic in \(e^y\).
- Solving \(\cosh x = k\) gives \(x = \pm\cosh^{-1} k\); \(\cosh^{-1} k\) itself is only the positive value.
:::

:::links
- watch: [Hyperbolic identities](https://www.examsolutions.net/tutorials/hyperbolic-identities/) · ExamSolutions · proving and using the identities, step by step
- watch: [Further Maths tutorials index](https://www.examsolutions.net/further-maths/) · ExamSolutions · hyperbolic functions and inverses in the Further Pure list
- practise: [Further topics booklets](https://madasmaths.com/archive_maths_booklets_further_topics_various.html) · MadAsMaths · the hyperbolic functions booklets have graded questions with answers
- explore: [Desmos graphing calculator](https://www.desmos.com/calculator) · Desmos · plot \(\sinh x\), \(\cosh x\) and \(\tfrac12 e^x\) together
- papers: [9231 Paper 2 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-fp2/) · Physics & Maths Tutor · real Paper 2 questions with mark schemes [unofficial]

Links checked 20 November 2026.
:::
Next: [Further differentiation and Maclaurin series](#math.fm.diff) differentiates the hyperbolic and inverse functions, finds second derivatives of implicit and parametric curves, and builds series that approximate a function near zero.
