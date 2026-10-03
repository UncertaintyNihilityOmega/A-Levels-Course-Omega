@chapter math.p1.quadratics
@title Quadratics
@level as
@paper CAIE P1 · Edexcel IAL P1 · AQA/OCR/Edexcel Pure
@time 6–8 hours
@summary A quadratic is any expression whose highest power of \(x\) is \(x^2\). You will learn to solve quadratic equations in three ways, read their graphs, count their solutions without solving, and handle quadratic inequalities and simultaneous equations.

:::why
Quadratics are the first topic in Paper 1 and they come back everywhere: in coordinate geometry, functions, calculus, mechanics and physics. A ball thrown in the air, the area of a field, the profit of a business at different prices: all of these are modelled by quadratics. If this chapter feels solid, a large part of A Level Pure Mathematics becomes easier.
:::

**Before you start**, you should be comfortable with [Algebra from scratch](#math.f.algebra) (expanding brackets, factorising, rearranging) and with [Powers, roots, surds and standard form](#math.f.powers).

## What is a quadratic?

Start with an expression you already know, like \(3x + 5\). The highest power of \(x\) is \(x^1\), so we call it **linear**: its graph is a straight line. Now allow an \(x^2\) term, for example \(x^2 - 2x - 3\). The graph is no longer straight. It bends into a symmetrical U-shape called a **parabola**, and the expression is called a **quadratic**.

:::def Quadratic expression
An expression that can be written in the form \(ax^2 + bx + c\), where \(a\), \(b\) and \(c\) are constants and \(a \neq 0\).
:::

The numbers \(a\), \(b\) and \(c\) are called **coefficients**. In \(2x^2 - 7x + 3\) we have \(a = 2\), \(b = -7\) and \(c = 3\). Notice that the sign belongs to the number: \(b\) is \(-7\), not \(7\). Getting this wrong is the most common way to lose marks later in this chapter.

:::def Coefficient
The number multiplying a power of the variable. In \(ax^2 + bx + c\), \(a\) is the coefficient of \(x^2\), \(b\) is the coefficient of \(x\), and \(c\) is the constant term.
:::

A **quadratic equation** sets a quadratic equal to zero, such as \(x^2 - 2x - 3 = 0\). Its solutions are called **roots**. Most quadratic equations have two roots, some have one, and some have no real roots at all. By the end of this chapter you will be able to predict which, before solving anything.

:::def Root (of an equation)
A value of the variable that makes the equation true. The real roots of \(f(x) = 0\) are the \(x\)-coordinates where the graph of \(y = f(x)\) meets the \(x\)-axis.
:::

## The shape of a quadratic graph

Every quadratic graph is a parabola, and four facts let you sketch one quickly.

1. **Which way up?** If \(a > 0\) the graph is ∪-shaped (it has a lowest point). If \(a < 0\) it is ∩-shaped (it has a highest point).
2. **Where does it cross the \(y\)-axis?** Put \(x = 0\): you get \(y = c\). So the \(y\)-intercept is \((0, c)\).
3. **Where does it cross the \(x\)-axis?** At the roots of \(ax^2 + bx + c = 0\), if there are any.
4. **Where is the turning point?** The lowest or highest point is called the **vertex**. The graph is symmetrical about a vertical line through the vertex, called the **line of symmetry**.

:::html
<figure class="fig"><svg viewBox="0 0 560 320" role="img" aria-label="Parabola y equals x squared minus 2x minus 3 with roots at minus 1 and 3 and vertex at 1, minus 4"><path class="gr" d="M34.0 14V294 M97.5 14V294 M161.0 14V294 M224.5 14V294 M288.0 14V294 M351.5 14V294 M415.0 14V294 M478.5 14V294 M542.0 14V294 M34 270.7H542 M34 224.0H542 M34 177.3H542 M34 130.7H542 M34 84.0H542 M34 37.3H542"/><path class="ax" d="M224.5 298V8" marker-end="url(#ahm)"/><path class="ax" d="M30 177.3H548" marker-end="url(#ahm)"/><text class="tl ti" x="544" y="170" text-anchor="end">x</text><text class="tl ti" x="232" y="18">y</text><text class="ts tc" x="34.0" y="192">−3</text><text class="ts tc" x="97.5" y="192">−2</text><text class="ts tc" x="161.0" y="192">−1</text><text class="ts tc" x="288.0" y="192">1</text><text class="ts tc" x="351.5" y="192">2</text><text class="ts tc" x="415.0" y="192">3</text><text class="ts tc" x="478.5" y="192">4</text><text class="ts tc" x="542.0" y="192">5</text><text class="ts te" x="220" y="274.7">−4</text><text class="ts te" x="220" y="228.0">−2</text><text class="ts te" x="220" y="134.7">2</text><text class="ts te" x="220" y="88.0">4</text><text class="ts te" x="220" y="41.3">6</text><text class="ts te" x="220" y="191">0</text><path class="ln-m dash" d="M288.0 14V294"/><path class="c1" d="M77.4 14.0L78.5 16.6L80.0 20.4L81.6 24.2L83.2 28.0L84.8 31.7L86.4 35.5L88.0 39.1L89.6 42.8L91.1 46.4L92.7 50.0L94.3 53.6L95.9 57.2L97.5 60.7L99.1 64.2L100.7 67.6L102.3 71.0L103.9 74.4L105.4 77.8L107.0 81.1L108.6 84.5L110.2 87.7L111.8 91.0L113.4 94.2L115.0 97.4L116.5 100.6L118.1 103.7L119.7 106.8L121.3 109.9L122.9 112.9L124.5 116.0L126.1 118.9L127.7 121.9L129.2 124.8L130.8 127.7L132.4 130.6L134.0 133.5L135.6 136.3L137.2 139.1L138.8 141.8L140.4 144.5L141.9 147.2L143.5 149.9L145.1 152.5L146.7 155.2L148.3 157.7L149.9 160.3L151.5 162.8L153.1 165.3L154.6 167.8L156.2 170.2L157.8 172.6L159.4 175.0L161.0 177.3L162.6 179.7L164.2 181.9L165.8 184.2L167.3 186.4L168.9 188.6L170.5 190.8L172.1 193.0L173.7 195.1L175.3 197.2L176.9 199.2L178.5 201.2L180.0 203.2L181.6 205.2L183.2 207.1L184.8 209.1L186.4 210.9L188.0 212.8L189.6 214.6L191.2 216.4L192.8 218.2L194.3 219.9L195.9 221.6L197.5 223.3L199.1 224.9L200.7 226.6L202.3 228.1L203.9 229.7L205.5 231.2L207.0 232.7L208.6 234.2L210.2 235.7L211.8 237.1L213.4 238.5L215.0 239.8L216.6 241.1L218.2 242.4L219.7 243.7L221.3 244.9L222.9 246.2L224.5 247.3L226.1 248.5L227.7 249.6L229.3 250.7L230.8 251.8L232.4 252.8L234.0 253.8L235.6 254.8L237.2 255.7L238.8 256.7L240.4 257.5L242.0 258.4L243.5 259.2L245.1 260.0L246.7 260.8L248.3 261.6L249.9 262.3L251.5 263.0L253.1 263.6L254.7 264.2L256.2 264.8L257.8 265.4L259.4 265.9L261.0 266.5L262.6 266.9L264.2 267.4L265.8 267.8L267.4 268.2L269.0 268.6L270.5 268.9L272.1 269.2L273.7 269.5L275.3 269.7L276.9 270.0L278.5 270.1L280.1 270.3L281.6 270.4L283.2 270.5L284.8 270.6L286.4 270.7L288.0 270.7L289.6 270.7L291.2 270.6L292.8 270.5L294.3 270.4L295.9 270.3L297.5 270.1L299.1 270.0L300.7 269.7L302.3 269.5L303.9 269.2L305.5 268.9L307.1 268.6L308.6 268.2L310.2 267.8L311.8 267.4L313.4 266.9L315.0 266.5L316.6 265.9L318.2 265.4L319.8 264.8L321.3 264.2L322.9 263.6L324.5 263.0L326.1 262.3L327.7 261.6L329.3 260.8L330.9 260.0L332.4 259.2L334.0 258.4L335.6 257.5L337.2 256.7L338.8 255.7L340.4 254.8L342.0 253.8L343.6 252.8L345.2 251.8L346.7 250.7L348.3 249.6L349.9 248.5L351.5 247.3L353.1 246.2L354.7 244.9L356.3 243.7L357.8 242.4L359.4 241.1L361.0 239.8L362.6 238.5L364.2 237.1L365.8 235.7L367.4 234.2L369.0 232.7L370.6 231.2L372.1 229.7L373.7 228.1L375.3 226.6L376.9 224.9L378.5 223.3L380.1 221.6L381.7 219.9L383.2 218.2L384.8 216.4L386.4 214.6L388.0 212.8L389.6 210.9L391.2 209.1L392.8 207.1L394.4 205.2L395.9 203.2L397.5 201.2L399.1 199.2L400.7 197.2L402.3 195.1L403.9 193.0L405.5 190.8L407.1 188.6L408.7 186.4L410.2 184.2L411.8 181.9L413.4 179.7L415.0 177.3L416.6 175.0L418.2 172.6L419.8 170.2L421.3 167.8L422.9 165.3L424.5 162.8L426.1 160.3L427.7 157.7L429.3 155.2L430.9 152.5L432.5 149.9L434.1 147.2L435.6 144.5L437.2 141.8L438.8 139.1L440.4 136.3L442.0 133.5L443.6 130.6L445.2 127.7L446.8 124.8L448.3 121.9L449.9 118.9L451.5 116.0L453.1 112.9L454.7 109.9L456.3 106.8L457.9 103.7L459.4 100.6L461.0 97.4L462.6 94.2L464.2 91.0L465.8 87.7L467.4 84.5L469.0 81.1L470.6 77.8L472.2 74.4L473.7 71.0L475.3 67.6L476.9 64.2L478.5 60.7L480.1 57.2L481.7 53.6L483.3 50.0L484.8 46.4L486.4 42.8L488.0 39.1L489.6 35.5L491.2 31.7L492.8 28.0L494.4 24.2L496.0 20.4L497.6 16.6L498.6 14.0"/><text class="tl halo ta" x="42" y="30">y = x² − 2x − 3</text><circle class="fi" cx="161.0" cy="177.3" r="4"/><text class="tl halo" x="154.0" y="168.3" text-anchor="end">root x = −1</text><circle class="fi" cx="415.0" cy="177.3" r="4"/><text class="tl halo" x="422.0" y="194.3" text-anchor="start">root x = 3</text><circle class="fi" cx="288.0" cy="270.7" r="4"/><text class="tl halo" x="297.0" y="274.7" text-anchor="start">vertex (1, −4)</text><circle class="fi" cx="224.5" cy="247.3" r="4"/><text class="tl halo" x="215.5" y="251.3" text-anchor="end">(0, −3)</text></svg><figcaption>The graph of y = x² − 2x − 3 is a ∪-shaped parabola. It crosses the x-axis at the roots, crosses the y-axis at c = −3, and is symmetrical about the dashed line x = 1 through its vertex.</figcaption></figure>
:::

:::analogy
Think of the parabola as a bowl. Water poured into a ∪-shaped bowl collects at the bottom, which is the vertex. The two roots are where the rim of the bowl crosses the table top (the \(x\)-axis). If the whole bowl sits above the table, there are no crossing points, so there are no real roots.
:::

Use the sliders below to change \(a\), \(b\) and \(c\) and watch what happens. Make \(a\) negative and the bowl flips. Change \(c\) and the whole graph slides up or down. Notice what happens to the roots as the vertex rises above the \(x\)-axis.

:::html
<div class="widget" data-w="graph" data-fns="a*x^2 + b*x + c" data-x="-6,6" data-y="-8,10" data-params="a=1,-3,3,0.1; b=-2,-8,8,0.5; c=-3,-8,8,0.5" data-labels="y = ax² + bx + c"></div>
:::

## Method 1: solving by factorising

Factorising works because of one simple fact.

:::key The zero product rule
If \(A \times B = 0\), then \(A = 0\) or \(B = 0\) (or both).
:::

So if we can write a quadratic as two brackets multiplied together, each bracket gives us one root.

### When \(a = 1\)

To factorise \(x^2 + bx + c\), look for two numbers that **multiply to give \(c\)** and **add to give \(b\)**.

:::eg Solve \(x^2 - 5x + 6 = 0\)
We need two numbers that multiply to \(+6\) and add to \(-5\). Try the factor pairs of 6: \((1, 6)\), \((2, 3)\), \((-1, -6)\), \((-2, -3)\). Only \(-2\) and \(-3\) add to \(-5\).

\[x^2 - 5x + 6 = (x - 2)(x - 3) = 0\]

So \(x - 2 = 0\) or \(x - 3 = 0\), giving \(x = 2\) or \(x = 3\).

**Check:** \(2^2 - 5(2) + 6 = 4 - 10 + 6 = 0\). It works.
:::

### When \(a \neq 1\): the "ac method"

Multiply \(a\) by \(c\). Find two numbers that multiply to \(ac\) and add to \(b\). Use them to split the middle term, then factorise in pairs.

:::eg Solve \(2x^2 + 7x - 4 = 0\)
Here \(ac = 2 \times (-4) = -8\). Two numbers that multiply to \(-8\) and add to \(7\) are \(8\) and \(-1\).

Split the middle term: \(2x^2 + 8x - x - 4 = 0\)

Factorise in pairs: \(2x(x + 4) - 1(x + 4) = 0\)

Take out the common bracket: \((2x - 1)(x + 4) = 0\)

So \(x = \tfrac{1}{2}\) or \(x = -4\).
:::

:::warn Never divide by \(x\)
To solve \(x^2 = 3x\), it is tempting to divide both sides by \(x\) and get \(x = 3\). But this loses a solution, because \(x\) might be zero (and you cannot divide by zero). Instead, rearrange to \(x^2 - 3x = 0\), factorise to \(x(x - 3) = 0\), and get **both** answers: \(x = 0\) or \(x = 3\).
:::

Factorising is the quickest method when it works. It only works neatly when the roots are rational (whole numbers or fractions). If you cannot find the two numbers within about a minute, switch to one of the next two methods.

## Method 2: completing the square

Completing the square rewrites a quadratic so you can see its vertex immediately. Exam questions often say "express in the form \(a(x + p)^2 + q\)" or "\((x - p)^2 + q\)". That is a request to complete the square.

The idea comes from expanding a squared bracket:

\[(x + 3)^2 = x^2 + 6x + 9\]

So \(x^2 + 6x\) is "nearly" \((x + 3)^2\). It is just missing the \(9\):

\[x^2 + 6x = (x + 3)^2 - 9\]

:::key Completing the square (when \(a = 1\))
\[x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2\]
Halve the coefficient of \(x\) to get the number in the bracket, then subtract that number squared.
:::

:::eg Write \(x^2 + 6x + 11\) in the form \((x + p)^2 + q\). Hence state the minimum point.
Half of \(6\) is \(3\), so

\[x^2 + 6x + 11 = (x + 3)^2 - 9 + 11 = (x + 3)^2 + 2\]

A square is never negative, so \((x + 3)^2 \geq 0\). The smallest value of the whole expression is \(0 + 2 = 2\), and this happens when \(x + 3 = 0\), that is \(x = -3\).

The minimum point of \(y = x^2 + 6x + 11\) is \((-3, 2)\).
:::

:::tip Reading the vertex from completed square form
For \(y = a(x + p)^2 + q\), the vertex is at \((-p, q)\). Watch the sign: \((x - 4)^2\) gives \(x = +4\), while \((x + 4)^2\) gives \(x = -4\).
:::

### When \(a \neq 1\)

Take \(a\) out as a factor of the \(x^2\) and \(x\) terms first, complete the square inside the bracket, then multiply back out.

:::eg Express \(2x^2 - 12x + 7\) in the form \(a(x + b)^2 + c\). Hence state the coordinates of the vertex of \(y = 2x^2 - 12x + 7\) and the range of \(f(x) = 2x^2 - 12x + 7\).
Factor 2 out of the first two terms:
\[2x^2 - 12x + 7 = 2(x^2 - 6x) + 7\]
Complete the square inside the bracket: \(x^2 - 6x = (x - 3)^2 - 9\). [M1]
\[= 2\big[(x - 3)^2 - 9\big] + 7 = 2(x - 3)^2 - 18 + 7\]
\[= 2(x - 3)^2 - 11\] [A1]

So \(a = 2\), \(b = -3\), \(c = -11\).

The vertex is at \((3, -11)\). [B1] Because \(a = 2 > 0\), this is a minimum, so the range is \(f(x) \geq -11\). [B1]

**Check:** put \(x = 0\) into both forms. \(2(0)^2 - 12(0) + 7 = 7\) and \(2(0 - 3)^2 - 11 = 18 - 11 = 7\). They match.
:::

You can also solve equations by completing the square: rewrite the equation, then take square roots. Remember that taking a square root gives **two** answers, positive and negative.

:::eg Solve \(x^2 + 4x - 1 = 0\), giving exact answers.
\[(x + 2)^2 - 4 - 1 = 0 \quad\Rightarrow\quad (x + 2)^2 = 5\]
\[x + 2 = \pm\sqrt{5} \quad\Rightarrow\quad x = -2 \pm \sqrt{5}\]
"Exact" means leave the surd in. As decimals these are \(0.236\) and \(-4.24\) (3 s.f.).
:::

## Method 3: the quadratic formula

If you complete the square on the general quadratic \(ax^2 + bx + c = 0\), you get a formula that solves **every** quadratic equation.

:::key The quadratic formula
The solutions of \(ax^2 + bx + c = 0\) are
\[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\]
:::

:::eg Solve \(3x^2 - 4x - 2 = 0\), giving your answers correct to 3 significant figures.
Identify the coefficients carefully, signs included: \(a = 3\), \(b = -4\), \(c = -2\).
\[x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(3)(-2)}}{2(3)} = \frac{4 \pm \sqrt{16 + 24}}{6} = \frac{4 \pm \sqrt{40}}{6}\] [M1]
\[x = 1.72 \quad\text{or}\quad x = -0.387\] [A1]
:::

:::warn Sign slips in the formula
Two errors cost more marks than any others: writing \(-b\) as \(-4\) when \(b = -4\) (it should be \(+4\)), and squaring a negative \(b\) wrongly. \((-4)^2 = 16\), but if you type \(-4^2\) into a calculator you get \(-16\). Always use brackets: \((-4)^2\).
:::

:::exam Which method should I use?
If the question says **"factorise"**, **"complete the square"** or **"express in the form…"**, you must use that method. Otherwise, try factorising first; if it does not work quickly, use the formula. If the question asks for **exact** answers, keep surds such as \(\sqrt{5}\). If it asks for **3 significant figures**, give exactly three. Cambridge examiners deduct for wrong accuracy.
:::

## The discriminant: how many roots?

Look again at the quadratic formula. The part under the square root, \(b^2 - 4ac\), decides everything:

- If it is **positive**, \(\pm\sqrt{\phantom{x}}\) gives two different answers, so there are **two distinct real roots**.
- If it is **zero**, \(\pm\sqrt{0}\) adds and subtracts nothing, so there is **one repeated root** (often called "equal roots").
- If it is **negative**, there is no real square root, so there are **no real roots**.

:::def Discriminant
The quantity \(b^2 - 4ac\) for the quadratic \(ax^2 + bx + c\). Its sign tells you how many real roots the equation \(ax^2 + bx + c = 0\) has.
:::

:::html
<figure class="fig wide"><svg viewBox="0 0 600 230" role="img" aria-label="Three parabolas: one crossing the x-axis twice, one touching it once, one not meeting it"><rect class="fm" x="0" y="0" width="190" height="230" rx="10"/><path class="ax" d="M8 107.5H182"/><path class="ax" d="M95.0 14V170.0"/><path class="c1" d="M10.0 45.0L11.4 48.7L12.8 52.4L14.2 56.0L15.7 59.5L17.1 63.0L18.5 66.4L19.9 69.7L21.3 73.0L22.8 76.2L24.2 79.4L25.6 82.5L27.0 85.5L28.4 88.5L29.8 91.4L31.2 94.2L32.7 97.0L34.1 99.7L35.5 102.4L36.9 105.0L38.3 107.5L39.8 110.0L41.2 112.4L42.6 114.7L44.0 117.0L45.4 119.2L46.8 121.4L48.2 123.5L49.7 125.5L51.1 127.5L52.5 129.4L53.9 131.2L55.3 133.0L56.7 134.7L58.2 136.4L59.6 138.0L61.0 139.5L62.4 141.0L63.8 142.4L65.2 143.7L66.7 145.0L68.1 146.2L69.5 147.4L70.9 148.5L72.3 149.5L73.8 150.5L75.2 151.4L76.6 152.2L78.0 153.0L79.4 153.7L80.8 154.4L82.2 155.0L83.7 155.5L85.1 156.0L86.5 156.4L87.9 156.7L89.3 157.0L90.8 157.2L92.2 157.4L93.6 157.5L95.0 157.5L96.4 157.5L97.8 157.4L99.2 157.2L100.7 157.0L102.1 156.7L103.5 156.4L104.9 156.0L106.3 155.5L107.8 155.0L109.2 154.4L110.6 153.7L112.0 153.0L113.4 152.2L114.8 151.4L116.2 150.5L117.7 149.5L119.1 148.5L120.5 147.4L121.9 146.2L123.3 145.0L124.7 143.7L126.2 142.4L127.6 141.0L129.0 139.5L130.4 138.0L131.8 136.4L133.2 134.7L134.7 133.0L136.1 131.2L137.5 129.4L138.9 127.5L140.3 125.5L141.8 123.5L143.2 121.4L144.6 119.2L146.0 117.0L147.4 114.7L148.8 112.4L150.2 110.0L151.7 107.5L153.1 105.0L154.5 102.4L155.9 99.7L157.3 97.0L158.8 94.2L160.2 91.4L161.6 88.5L163.0 85.5L164.4 82.5L165.8 79.4L167.2 76.2L168.7 73.0L170.1 69.7L171.5 66.4L172.9 63.0L174.3 59.5L175.8 56.0L177.2 52.4L178.6 48.7L180.0 45.0"/><circle class="fr" cx="38.3" cy="107.5" r="5"/><circle class="fr" cx="151.7" cy="107.5" r="5"/><text class="tc tb" x="95.0" y="194">b² − 4ac > 0</text><text class="tl tc" x="95.0" y="214">two distinct real roots</text><rect class="fm" x="205" y="0" width="190" height="230" rx="10"/><path class="ax" d="M213 107.5H387"/><path class="ax" d="M300.0 14V170.0"/><path class="c1" d="M226.3 23.0L227.8 26.2L229.2 29.4L230.6 32.5L232.0 35.5L233.4 38.5L234.8 41.4L236.2 44.2L237.7 47.0L239.1 49.7L240.5 52.4L241.9 55.0L243.3 57.5L244.8 60.0L246.2 62.4L247.6 64.7L249.0 67.0L250.4 69.2L251.8 71.4L253.2 73.5L254.7 75.5L256.1 77.5L257.5 79.4L258.9 81.2L260.3 83.0L261.8 84.7L263.2 86.4L264.6 88.0L266.0 89.5L267.4 91.0L268.8 92.4L270.2 93.7L271.7 95.0L273.1 96.2L274.5 97.4L275.9 98.5L277.3 99.5L278.8 100.5L280.2 101.4L281.6 102.2L283.0 103.0L284.4 103.7L285.8 104.4L287.2 105.0L288.7 105.5L290.1 106.0L291.5 106.4L292.9 106.7L294.3 107.0L295.8 107.2L297.2 107.4L298.6 107.5L300.0 107.5L301.4 107.5L302.8 107.4L304.2 107.2L305.7 107.0L307.1 106.7L308.5 106.4L309.9 106.0L311.3 105.5L312.8 105.0L314.2 104.4L315.6 103.7L317.0 103.0L318.4 102.2L319.8 101.4L321.2 100.5L322.7 99.5L324.1 98.5L325.5 97.4L326.9 96.2L328.3 95.0L329.8 93.7L331.2 92.4L332.6 91.0L334.0 89.5L335.4 88.0L336.8 86.4L338.2 84.7L339.7 83.0L341.1 81.2L342.5 79.4L343.9 77.5L345.3 75.5L346.8 73.5L348.2 71.4L349.6 69.2L351.0 67.0L352.4 64.7L353.8 62.4L355.2 60.0L356.7 57.5L358.1 55.0L359.5 52.4L360.9 49.7L362.3 47.0L363.8 44.2L365.2 41.4L366.6 38.5L368.0 35.5L369.4 32.5L370.8 29.4L372.2 26.2L373.7 23.0"/><circle class="fr" cx="300.0" cy="107.5" r="5"/><text class="tc tb" x="300.0" y="194">b² − 4ac = 0</text><text class="tl tc" x="300.0" y="214">one repeated root</text><rect class="fm" x="410" y="0" width="190" height="230" rx="10"/><path class="ax" d="M418 107.5H592"/><path class="ax" d="M505.0 14V170.0"/><path class="c1" d="M442.7 22.0L444.1 24.7L445.5 27.4L446.9 30.0L448.3 32.5L449.8 35.0L451.2 37.4L452.6 39.7L454.0 42.0L455.4 44.2L456.8 46.4L458.2 48.5L459.7 50.5L461.1 52.5L462.5 54.4L463.9 56.2L465.3 58.0L466.8 59.7L468.2 61.4L469.6 63.0L471.0 64.5L472.4 66.0L473.8 67.4L475.2 68.7L476.7 70.0L478.1 71.2L479.5 72.4L480.9 73.5L482.3 74.5L483.8 75.5L485.2 76.4L486.6 77.2L488.0 78.0L489.4 78.7L490.8 79.4L492.2 80.0L493.7 80.5L495.1 81.0L496.5 81.4L497.9 81.7L499.3 82.0L500.8 82.2L502.2 82.4L503.6 82.5L505.0 82.5L506.4 82.5L507.8 82.4L509.2 82.2L510.7 82.0L512.1 81.7L513.5 81.4L514.9 81.0L516.3 80.5L517.8 80.0L519.2 79.4L520.6 78.7L522.0 78.0L523.4 77.2L524.8 76.4L526.2 75.5L527.7 74.5L529.1 73.5L530.5 72.4L531.9 71.2L533.3 70.0L534.8 68.7L536.2 67.4L537.6 66.0L539.0 64.5L540.4 63.0L541.8 61.4L543.2 59.7L544.7 58.0L546.1 56.2L547.5 54.4L548.9 52.5L550.3 50.5L551.8 48.5L553.2 46.4L554.6 44.2L556.0 42.0L557.4 39.7L558.8 37.4L560.2 35.0L561.7 32.5L563.1 30.0L564.5 27.4L565.9 24.7L567.3 22.0"/><text class="tc tb" x="505.0" y="194">b² − 4ac < 0</text><text class="tl tc" x="505.0" y="214">no real roots</text></svg><figcaption>The discriminant tells you how many times the parabola meets the x-axis, without solving anything. Red dots mark the real roots.</figcaption></figure>
:::

:::eg Find the values of \(k\) for which \(x^2 + kx + 9 = 0\) has equal roots.
Equal roots means the discriminant is zero: \(a = 1\), \(b = k\), \(c = 9\).
\[k^2 - 4(1)(9) = 0 \quad\Rightarrow\quad k^2 = 36 \quad\Rightarrow\quad k = \pm 6\]
**Check:** with \(k = 6\), \(x^2 + 6x + 9 = (x + 3)^2\), which does have a repeated root.
:::

### Lines meeting curves

A favourite Paper 1 question asks when a straight line **meets**, **touches** (is a **tangent** to), or **misses** a curve. The method is always the same: set the two equations equal, rearrange into a quadratic equal to zero, and look at its discriminant.

| The line… | Number of meeting points | Discriminant |
|---|---|---|
| cuts the curve | 2 | \(b^2 - 4ac > 0\) |
| touches the curve (tangent) | 1 | \(b^2 - 4ac = 0\) |
| misses the curve | 0 | \(b^2 - 4ac < 0\) |

:::eg Find the set of values of \(k\) for which the line \(y = kx - 1\) intersects the curve \(y = x^2 + 3\) at two distinct points.
At intersection the \(y\)-values are equal:
\[x^2 + 3 = kx - 1 \quad\Rightarrow\quad x^2 - kx + 4 = 0\] [M1]
Two distinct points means two distinct roots, so the discriminant is positive:
\[(-k)^2 - 4(1)(4) > 0 \quad\Rightarrow\quad k^2 > 16\] [M1]
\(k^2 > 16\) when \(k > 4\) or \(k < -4\) (see inequalities below). [A1]
:::

## Quadratic inequalities

To solve \(x^2 - x - 12 > 0\) you need all the values of \(x\) that make the quadratic positive, not just a couple of numbers. The reliable method has three steps.

:::steps
1. **Solve the equation** \(x^2 - x - 12 = 0\) to find the critical values. Here \((x - 4)(x + 3) = 0\), so \(x = 4\) or \(x = -3\).
2. **Sketch the graph.** \(a = 1 > 0\), so it is ∪-shaped, crossing the \(x\)-axis at \(-3\) and \(4\).
3. **Read off the answer.** "\(> 0\)" means "where is the graph above the \(x\)-axis?" That is to the left of \(-3\) and to the right of \(4\): \(x < -3\) or \(x > 4\).
:::

If the question had been \(x^2 - x - 12 < 0\) (below the axis), the answer would be the part in the middle: \(-3 < x < 4\).

:::eg Solve \(2x^2 + 5x - 3 \leq 0\).
Factorise: \((2x - 1)(x + 3) = 0\) gives critical values \(x = \tfrac12\) and \(x = -3\). [M1]

The graph is ∪-shaped, and "\(\leq 0\)" means on or below the axis, which is between the roots. The end points are included because of the "\(=\)" in \(\leq\):
\[-3 \leq x \leq \tfrac{1}{2}\] [A1]
:::

:::warn Two inequalities cannot be squashed together the wrong way
For "\(x < -3\) or \(x > 4\)" never write \(-3 > x > 4\). That would mean \(x\) is less than \(-3\) **and** greater than \(4\) at the same time, which is impossible. Write two separate inequalities joined by "or". A combined form like \(-3 < x < 4\) is only correct for the region **between** the roots.
:::

## Simultaneous equations: one linear, one quadratic

When one equation is linear and the other is quadratic, use **substitution**: rearrange the linear equation to make one letter the subject, then substitute into the quadratic.

:::eg Solve the simultaneous equations \(y = x + 1\) and \(x^2 + y^2 = 25\).
Substitute \(y = x + 1\) into the second equation:
\[x^2 + (x + 1)^2 = 25 \quad\Rightarrow\quad 2x^2 + 2x + 1 - 25 = 0 \quad\Rightarrow\quad x^2 + x - 12 = 0\] [M1]
\[(x + 4)(x - 3) = 0 \quad\Rightarrow\quad x = -4 \text{ or } x = 3\] [A1]
Now find each \(y\) from the **linear** equation: \(x = -4 \Rightarrow y = -3\), and \(x = 3 \Rightarrow y = 4\). [A1]

Solutions: \((-4, -3)\) and \((3, 4)\). Geometrically, these are the two points where the line crosses the circle of radius 5.
:::

:::tip Pair your answers
Always present the answers as pairs, \((x, y)\). An examiner cannot give the final mark for "\(x = -4, 3\) and \(y = -3, 4\)" if it is unclear which \(y\) goes with which \(x\).
:::

## Disguised quadratics

Some equations are quadratics in disguise. If an equation contains a quantity and its square, such as \(x^2\) and \(x^4\), or \(\sqrt{x}\) and \(x\), substitute a new letter.

:::eg Solve \(x^4 - 5x^2 + 4 = 0\).
Let \(u = x^2\). Then \(x^4 = u^2\), and the equation becomes
\[u^2 - 5u + 4 = 0 \quad\Rightarrow\quad (u - 1)(u - 4) = 0 \quad\Rightarrow\quad u = 1 \text{ or } u = 4\]
Go back to \(x\): \(x^2 = 1\) gives \(x = \pm 1\), and \(x^2 = 4\) gives \(x = \pm 2\). There are four solutions: \(x = -2, -1, 1, 2\).
:::

:::eg Solve \(2x - 7\sqrt{x} + 3 = 0\).
Let \(u = \sqrt{x}\), so \(x = u^2\):
\[2u^2 - 7u + 3 = 0 \quad\Rightarrow\quad (2u - 1)(u - 3) = 0 \quad\Rightarrow\quad u = \tfrac{1}{2} \text{ or } u = 3\]
Then \(x = u^2\), so \(x = \tfrac{1}{4}\) or \(x = 9\). Because \(\sqrt{x}\) can never be negative, any negative value of \(u\) would have to be rejected. Here both are positive, so both answers stand.
:::

:::board
All boards teach the same quadratics content in their first Pure paper (Cambridge P1, Edexcel IAL P1, and Year 1 Pure for AQA, OCR and Edexcel in the UK). The UK boards also expect you to use the discriminant inside **proof** questions ("prove that the equation has no real roots for all values of \(k\)"). Cambridge mostly tests it through line-and-curve intersections and the range of a function.
:::

:::try Start easy, finish at exam standard
Q: Solve \(x^2 + 7x + 10 = 0\) by factorising.
A: Two numbers that multiply to 10 and add to 7 are 2 and 5. \((x + 2)(x + 5) = 0\), so \(x = -2\) or \(x = -5\).
Q: Solve \(3x^2 - 10x - 8 = 0\) by factorising.
A: \(ac = -24\). Two numbers that multiply to \(-24\) and add to \(-10\) are \(-12\) and \(2\).
\(3x^2 - 12x + 2x - 8 = 3x(x - 4) + 2(x - 4) = (3x + 2)(x - 4)\), so \(x = -\tfrac{2}{3}\) or \(x = 4\).
Q: Express \(x^2 - 8x + 3\) in the form \((x + p)^2 + q\) and state the coordinates of the minimum point of \(y = x^2 - 8x + 3\).
A: Half of \(-8\) is \(-4\): \(x^2 - 8x + 3 = (x - 4)^2 - 16 + 3 = (x - 4)^2 - 13\). The minimum point is \((4, -13)\).
Q: Solve \(5x^2 + 2x - 1 = 0\), giving your answers correct to 3 significant figures.
A: \(x = \dfrac{-2 \pm \sqrt{4 + 20}}{10} = \dfrac{-2 \pm \sqrt{24}}{10}\), so \(x = 0.290\) or \(x = -0.690\).
Q: Find the set of values of \(k\) for which \(kx^2 + 4x + k = 0\) has no real roots.
A: No real roots means \(b^2 - 4ac < 0\): \(16 - 4k^2 < 0\), so \(k^2 > 4\), giving \(k < -2\) or \(k > 2\).
Q: Solve the inequality \(x^2 + 2x - 15 < 0\).
A: \((x + 5)(x - 3) = 0\) gives critical values \(-5\) and \(3\). The graph is ∪-shaped and we want the part below the axis: \(-5 < x < 3\).
Q: Solve the simultaneous equations \(y = 2x - 1\) and \(y = x^2 - 4x + 4\).
A: \(x^2 - 4x + 4 = 2x - 1 \Rightarrow x^2 - 6x + 5 = 0 \Rightarrow (x - 1)(x - 5) = 0\). [M1]
\(x = 1 \Rightarrow y = 1\) and \(x = 5 \Rightarrow y = 9\). Solutions \((1, 1)\) and \((5, 9)\). [A1 A1]
Q: (Exam style) \(f(x) = -x^2 + 6x - 5\).
(a) Express \(f(x)\) in the form \(a - (x - b)^2\).
(b) State the maximum value of \(f(x)\) and the value of \(x\) at which it occurs.
(c) Find the set of values of \(k\) for which the line \(y = k\) meets the curve \(y = f(x)\) at two distinct points.
A: (a) \(-x^2 + 6x - 5 = -(x^2 - 6x) - 5 = -\big[(x - 3)^2 - 9\big] - 5 = 4 - (x - 3)^2\). [M1 A1]
(b) A square is never negative, so the largest value is \(4\), when \(x = 3\). [B1]
(c) The horizontal line \(y = k\) cuts the ∩-shaped curve twice when it is below the maximum: \(k < 4\). [B1]
Q: Solve \(x - 6\sqrt{x} + 8 = 0\).
A: Let \(u = \sqrt{x}\): \(u^2 - 6u + 8 = 0 \Rightarrow (u - 2)(u - 4) = 0 \Rightarrow u = 2\) or \(4\). So \(x = 4\) or \(x = 16\).
:::

:::quiz
? How many real roots does \(2x^2 + 3x + 5 = 0\) have?
- Two
- One
+ None
> The discriminant is \(3^2 - 4(2)(5) = 9 - 40 = -31\). It is negative, so there are no real roots.
? Which is \(x^2 - 10x + 4\) written in completed square form?
+ \((x - 5)^2 - 21\)
- \((x - 5)^2 + 4\)
- \((x - 10)^2 - 96\)
- \((x + 5)^2 - 21\)
> Half of \(-10\) is \(-5\), so \(x^2 - 10x = (x - 5)^2 - 25\). Then \(-25 + 4 = -21\).
? What are the coordinates of the vertex of \(y = 3(x - 2)^2 + 7\)?
- \((-2, 7)\)
+ \((2, 7)\)
- \((2, -7)\)
- \((3, 7)\)
> In \(a(x + p)^2 + q\) form the vertex is \((-p, q)\). Here the bracket is \((x - 2)\), so \(x = 2\), and \(q = 7\).
? Which set of values satisfies \(x^2 < 9\)?
+ \(-3 < x < 3\)
- \(x < 3\)
- \(x < -3\) or \(x > 3\)
- \(x < \pm 3\)
> The graph of \(y = x^2 - 9\) is below the axis between its roots \(-3\) and \(3\). "\(x < 3\)" alone would wrongly include values like \(-10\).
:::

:::recap
- A quadratic has the form \(ax^2 + bx + c\) with \(a \neq 0\). Its graph is a parabola: ∪-shaped if \(a > 0\), ∩-shaped if \(a < 0\).
- Three ways to solve \(ax^2 + bx + c = 0\): factorising (fastest when it works), completing the square (also gives the vertex), and the formula \(x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}\) (always works).
- In completed square form \(a(x + p)^2 + q\), the vertex is \((-p, q)\).
- The discriminant \(b^2 - 4ac\) gives the number of real roots: positive means 2, zero means 1 repeated root, negative means none.
- For a line and a curve: set them equal, form a quadratic, and use the discriminant (2 points, tangent, or no meeting).
- For inequalities: find critical values, sketch, then read the region from the graph.
- Substitute a new letter for disguised quadratics such as \(x^4 - 5x^2 + 4 = 0\).
:::

:::note Learn more online
- **Watch:** [Completing the square](https://www.examsolutions.net/tutorials/completing-the-square/) · ExamSolutions · the method shown slowly, with examples
- **Watch:** [Exam questions: roots and the discriminant](https://www.examsolutions.net/tutorials/exam-questions-roots-and-discriminant/) · ExamSolutions · exam-style questions solved on video
- **Practise:** [CAIE Pure 1 quadratics exam questions](https://www.savemyexams.com/a-level/maths/cie/20/pure-1/topic-questions/algebra-and-functions/quadratics/exam-questions/) · Save My Exams · questions sorted by difficulty, with mark schemes *(some content paid)*
- **Explore:** [Graphing Quadratics](https://phet.colorado.edu/en/simulations/graphing-quadratics) · PhET · move a, b and c and watch the vertex and roots
- **Explore:** [Quadratics](https://undergroundmathematics.org/quadratics) · Underground Mathematics · rich problems for stretch
- **Papers:** [9709 Paper 1 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-1/) · Physics & Maths Tutor · find the quadratics questions in real papers *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Functions](#math.p1.functions) builds on everything here, including the range of a quadratic.
