@group Pure Mathematics 1
@chapter math.p1.functions
@title Functions
@level as
@paper CAIE P1 · Edexcel IAL P1/P2 · UK Pure Years 1–2
@time 6–8 hours
@summary A function is a rule that turns each input into exactly one output. You will learn domain and range, one-one and many-one functions, composite and inverse functions, how restricting a domain makes an inverse possible, and how changes to an equation move, stretch and reflect a graph.

:::why
Every formula in science and business is a function: put in a time, get out a distance; put in a price, get out a profit. The language of functions (input, output, domain, range, inverse) lets you say exactly what a formula can and cannot do. It also gives you graph transformations, which let you sketch new curves from ones you already know, and it is the language that calculus is written in. Paper 1 regularly includes a multi-part functions question that combines a completed square, a range, an inverse and a composite function.
:::

**Before you start**, you should be comfortable with [Quadratics](#math.p1.quadratics), especially completing the square, and with graphs from [Coordinates and straight lines](#math.f.graphs).

## What is a function?

A function is a machine. You feed in a number, the machine follows a fixed rule, and out comes a new number. The square-root button on a calculator is a function: feed in 25 and you always get 5, never two different answers. That "one answer only" property is the heart of the definition.

:::def Function
A rule that gives exactly one output for each allowed input.
:::

There are two ways to write the same function. Both of these mean "double the input, then add 3":

\[f(x) = 2x + 3 \qquad\text{or}\qquad f : x \mapsto 2x + 3\]

Read \(f(4)\) as "f of 4". It is the output when the input is 4, so \(f(4) = 2(4) + 3 = 11\). The second form reads "f maps \(x\) to \(2x + 3\)". Cambridge uses both forms.

:::def Domain
The set of all allowed input values of a function.
:::

:::def Range
The set of all output values that the function actually produces.
:::

The symbol \(\mathbb{R}\) stands for the real numbers (every number on the number line), and \(x \in \mathbb{R}\) means "\(x\) is any real number". If a question gives no domain, use the largest set of real numbers for which the rule works. At this level only two things stop a rule working: dividing by zero and taking the square root of a negative number.

| Function | Largest domain | Reason |
|---|---|---|
| \(\dfrac{1}{x - 3}\) | \(x \neq 3\) | cannot divide by 0 |
| \(\sqrt{x - 2}\) | \(x \geq 2\) | cannot take the root of a negative |
| \(\dfrac{1}{\sqrt{x - 2}}\) | \(x > 2\) | the root must be positive, because it is also a denominator |

To find the range, ask "which \(y\)-values does the graph reach?" A sketch or a completed square usually answers it.

:::tip Write the range with f(x) or y
Write \(f(x) \geq -3\) or \(y \geq -3\). Never write \(x \geq -3\): \(x\) is the input, and the range is about outputs.
:::

:::eg A function is defined by \(f(x) = x^2 - 4x + 1\) for \(0 \leq x \leq 5\). Find the range of \(f\).
Complete the square: \(f(x) = (x - 2)^2 - 3\). The graph is ∪-shaped with its lowest point at \(x = 2\), which lies inside the domain, so the least value is \(-3\).

Now check both ends of the domain: \(f(0) = 1\) and \(f(5) = 25 - 20 + 1 = 6\). The graph falls from \(1\) to \(-3\), then rises to \(6\), so the greatest value is the larger end value, \(6\).

The range is \(-3 \leq f(x) \leq 6\).

**Common error:** writing \(1 \leq f(x) \leq 6\) from the end values alone. That misses the dip to \(-3\) at the vertex.
:::

## One-one and many-one functions

Compare \(f(x) = x^3\) and \(g(x) = x^2\). Every output of \(x^3\) comes from one input only. But \(g(2) = 4\) and \(g(-2) = 4\): two different inputs give the same output.

:::def One-one function
A function in which each output comes from exactly one input.
:::

:::def Many-one function
A function in which at least one output comes from two or more different inputs.
:::

The **horizontal line test** tells you which kind you have. Draw horizontal lines across the graph. If any line cuts the graph more than once, the function is many-one. If every line cuts it at most once, it is one-one.

:::html
<figure class="fig wide"><svg viewBox="0 0 620 270" role="img" aria-label="Two graphs with a horizontal line drawn across each: y equals x squared is cut twice, y equals x cubed is cut once"><path class="gr" d="M30.0 30.0V230.0 M72.7 30.0V230.0 M115.3 30.0V230.0 M158.0 30.0V230.0 M200.7 30.0V230.0 M243.3 30.0V230.0 M286.0 30.0V230.0 M30.0 207.6H286.0 M30.0 170.2H286.0 M30.0 132.8H286.0 M30.0 95.4H286.0 M30.0 58.0H286.0"/><path class="ax" d="M158.0 234.0V24.0" marker-end="url(#ahm)"/><path class="ax" d="M26.0 207.6H292.0" marker-end="url(#ahm)"/><text class="tl ti" x="290.0" y="200.6" text-anchor="end">x</text><text class="tl ti" x="165.0" y="34.0">y</text><text class="ts tc" x="30.0" y="222.6">−3</text><text class="ts tc" x="72.7" y="222.6">−2</text><text class="ts tc" x="115.3" y="222.6">−1</text><text class="ts tc" x="200.7" y="222.6">1</text><text class="ts tc" x="243.3" y="222.6">2</text><text class="ts tc" x="286.0" y="222.6">3</text><text class="ts te" x="153.0" y="174.2">2</text><text class="ts te" x="153.0" y="136.8">4</text><text class="ts te" x="153.0" y="99.4">6</text><text class="ts te" x="153.0" y="62.0">8</text><text class="ts te" x="153.0" y="221.6">0</text><path class="c1" d="M30.0 39.3L31.1 42.1L32.1 44.9L33.2 47.7L34.3 50.4L35.3 53.1L36.4 55.7L37.5 58.4L38.5 61.0L39.6 63.6L40.7 66.2L41.7 68.8L42.8 71.3L43.9 73.8L44.9 76.3L46.0 78.8L47.1 81.2L48.1 83.6L49.2 86.0L50.3 88.4L51.3 90.7L52.4 93.1L53.5 95.4L54.5 97.7L55.6 99.9L56.7 102.1L57.7 104.3L58.8 106.5L59.9 108.7L60.9 110.8L62.0 112.9L63.1 115.0L64.1 117.1L65.2 119.1L66.3 121.2L67.3 123.2L68.4 125.1L69.5 127.1L70.5 129.0L71.6 130.9L72.7 132.8L73.7 134.7L74.8 136.5L75.9 138.3L76.9 140.1L78.0 141.9L79.1 143.6L80.1 145.3L81.2 147.0L82.3 148.7L83.3 150.3L84.4 152.0L85.5 153.6L86.5 155.1L87.6 156.7L88.7 158.2L89.7 159.7L90.8 161.2L91.9 162.7L92.9 164.1L94.0 165.5L95.1 166.9L96.1 168.3L97.2 169.6L98.3 170.9L99.3 172.2L100.4 173.5L101.5 174.8L102.5 176.0L103.6 177.2L104.7 178.4L105.7 179.5L106.8 180.7L107.9 181.8L108.9 182.9L110.0 183.9L111.1 185.0L112.1 186.0L113.2 187.0L114.3 187.9L115.3 188.9L116.4 189.8L117.5 190.7L118.5 191.6L119.6 192.4L120.7 193.3L121.7 194.1L122.8 194.8L123.9 195.6L124.9 196.3L126.0 197.1L127.1 197.7L128.1 198.4L129.2 199.1L130.3 199.7L131.3 200.3L132.4 200.8L133.5 201.4L134.5 201.9L135.6 202.4L136.7 202.9L137.7 203.4L138.8 203.8L139.9 204.2L140.9 204.6L142.0 204.9L143.1 205.3L144.1 205.6L145.2 205.9L146.3 206.2L147.3 206.4L148.4 206.6L149.5 206.8L150.5 207.0L151.6 207.1L152.7 207.3L153.7 207.4L154.8 207.5L155.9 207.5L156.9 207.6L158.0 207.6L159.1 207.6L160.1 207.5L161.2 207.5L162.3 207.4L163.3 207.3L164.4 207.1L165.5 207.0L166.5 206.8L167.6 206.6L168.7 206.4L169.7 206.2L170.8 205.9L171.9 205.6L172.9 205.3L174.0 204.9L175.1 204.6L176.1 204.2L177.2 203.8L178.3 203.4L179.3 202.9L180.4 202.4L181.5 201.9L182.5 201.4L183.6 200.8L184.7 200.3L185.7 199.7L186.8 199.1L187.9 198.4L188.9 197.7L190.0 197.1L191.1 196.3L192.1 195.6L193.2 194.8L194.3 194.1L195.3 193.3L196.4 192.4L197.5 191.6L198.5 190.7L199.6 189.8L200.7 188.9L201.7 187.9L202.8 187.0L203.9 186.0L204.9 185.0L206.0 183.9L207.1 182.9L208.1 181.8L209.2 180.7L210.3 179.5L211.3 178.4L212.4 177.2L213.5 176.0L214.5 174.8L215.6 173.5L216.7 172.2L217.7 170.9L218.8 169.6L219.9 168.3L220.9 166.9L222.0 165.5L223.1 164.1L224.1 162.7L225.2 161.2L226.3 159.7L227.3 158.2L228.4 156.7L229.5 155.1L230.5 153.6L231.6 152.0L232.7 150.3L233.7 148.7L234.8 147.0L235.9 145.3L236.9 143.6L238.0 141.9L239.1 140.1L240.1 138.3L241.2 136.5L242.3 134.7L243.3 132.8L244.4 130.9L245.5 129.0L246.5 127.1L247.6 125.1L248.7 123.2L249.7 121.2L250.8 119.1L251.9 117.1L252.9 115.0L254.0 112.9L255.1 110.8L256.1 108.7L257.2 106.5L258.3 104.3L259.3 102.1L260.4 99.9L261.5 97.7L262.5 95.4L263.6 93.1L264.7 90.7L265.7 88.4L266.8 86.0L267.9 83.6L268.9 81.2L270.0 78.8L271.1 76.3L272.1 73.8L273.2 71.3L274.3 68.8L275.3 66.2L276.4 63.6L277.5 61.0L278.5 58.4L279.6 55.7L280.7 53.1L281.7 50.4L282.8 47.7L283.9 44.9L284.9 42.1L286.0 39.3"/><path class="ln-m dash" d="M30.0 132.8L286.0 132.8"/><circle class="fi" cx="72.7" cy="132.8" r="4"/><circle class="fi" cx="243.3" cy="132.8" r="4"/><text class="tl halo" x="64.7" y="125.8" text-anchor="end">(−2, 4)</text><text class="tl halo" x="251.3" y="125.8" text-anchor="start">(2, 4)</text><text class="tb tc" x="150.0" y="20.0" text-anchor="middle">y = x²: many-one</text><text class="tl tc" x="150.0" y="262.0" text-anchor="middle">the line meets it twice</text><path class="gr" d="M361.6 30.0V230.0 M419.8 30.0V230.0 M478.0 30.0V230.0 M536.2 30.0V230.0 M594.4 30.0V230.0 M350.0 214.2H606.0 M350.0 172.1H606.0 M350.0 130.0H606.0 M350.0 87.9H606.0 M350.0 45.8H606.0"/><path class="ax" d="M478.0 234.0V24.0" marker-end="url(#ahm)"/><path class="ax" d="M346.0 130.0H612.0" marker-end="url(#ahm)"/><text class="tl ti" x="610.0" y="123.0" text-anchor="end">x</text><text class="tl ti" x="485.0" y="34.0">y</text><text class="ts tc" x="361.6" y="145.0">−2</text><text class="ts tc" x="419.8" y="145.0">−1</text><text class="ts tc" x="536.2" y="145.0">1</text><text class="ts tc" x="594.4" y="145.0">2</text><text class="ts te" x="473.0" y="218.2">−8</text><text class="ts te" x="473.0" y="176.1">−4</text><text class="ts te" x="473.0" y="91.9">4</text><text class="ts te" x="473.0" y="49.8">8</text><text class="ts te" x="473.0" y="144.0">0</text><path class="c1" d="M355.3 228.6L356.4 226.1L357.5 223.6L358.5 221.1L359.6 218.7L360.7 216.3L361.7 214.0L362.8 211.7L363.9 209.5L364.9 207.3L366.0 205.1L367.1 203.0L368.1 200.9L369.2 198.8L370.3 196.8L371.3 194.9L372.4 192.9L373.5 191.0L374.5 189.2L375.6 187.4L376.7 185.6L377.7 183.9L378.8 182.2L379.9 180.5L380.9 178.9L382.0 177.3L383.1 175.7L384.1 174.2L385.2 172.7L386.3 171.3L387.3 169.8L388.4 168.4L389.5 167.1L390.5 165.8L391.6 164.5L392.7 163.2L393.7 162.0L394.8 160.8L395.9 159.6L396.9 158.5L398.0 157.4L399.1 156.3L400.1 155.2L401.2 154.2L402.3 153.2L403.3 152.2L404.4 151.3L405.5 150.4L406.5 149.5L407.6 148.6L408.7 147.8L409.7 147.0L410.8 146.2L411.9 145.5L412.9 144.7L414.0 144.0L415.1 143.3L416.1 142.7L417.2 142.0L418.3 141.4L419.3 140.8L420.4 140.2L421.5 139.7L422.5 139.1L423.6 138.6L424.7 138.1L425.7 137.6L426.8 137.2L427.9 136.7L428.9 136.3L430.0 135.9L431.1 135.5L432.1 135.2L433.2 134.8L434.3 134.5L435.3 134.2L436.4 133.8L437.5 133.6L438.5 133.3L439.6 133.0L440.7 132.8L441.7 132.5L442.8 132.3L443.9 132.1L444.9 131.9L446.0 131.8L447.1 131.6L448.1 131.4L449.2 131.3L450.3 131.1L451.3 131.0L452.4 130.9L453.5 130.8L454.5 130.7L455.6 130.6L456.7 130.5L457.7 130.4L458.8 130.4L459.9 130.3L460.9 130.3L462.0 130.2L463.1 130.2L464.1 130.1L465.2 130.1L466.3 130.1L467.3 130.1L468.4 130.0L469.5 130.0L470.5 130.0L471.6 130.0L472.7 130.0L473.7 130.0L474.8 130.0L475.9 130.0L476.9 130.0L478.0 130.0L479.1 130.0L480.1 130.0L481.2 130.0L482.3 130.0L483.3 130.0L484.4 130.0L485.5 130.0L486.5 130.0L487.6 130.0L488.7 129.9L489.7 129.9L490.8 129.9L491.9 129.9L492.9 129.8L494.0 129.8L495.1 129.7L496.1 129.7L497.2 129.6L498.3 129.6L499.3 129.5L500.4 129.4L501.5 129.3L502.5 129.2L503.6 129.1L504.7 129.0L505.7 128.9L506.8 128.7L507.9 128.6L508.9 128.4L510.0 128.2L511.1 128.1L512.1 127.9L513.2 127.7L514.3 127.5L515.3 127.2L516.4 127.0L517.5 126.7L518.5 126.4L519.6 126.2L520.7 125.8L521.7 125.5L522.8 125.2L523.9 124.8L524.9 124.5L526.0 124.1L527.1 123.7L528.1 123.3L529.2 122.8L530.3 122.4L531.3 121.9L532.4 121.4L533.5 120.9L534.5 120.3L535.6 119.8L536.7 119.2L537.7 118.6L538.8 118.0L539.9 117.3L540.9 116.7L542.0 116.0L543.1 115.3L544.1 114.5L545.2 113.8L546.3 113.0L547.3 112.2L548.4 111.4L549.5 110.5L550.5 109.6L551.6 108.7L552.7 107.8L553.7 106.8L554.8 105.8L555.9 104.8L556.9 103.7L558.0 102.6L559.1 101.5L560.1 100.4L561.2 99.2L562.3 98.0L563.3 96.8L564.4 95.5L565.5 94.2L566.5 92.9L567.6 91.6L568.7 90.2L569.7 88.7L570.8 87.3L571.9 85.8L572.9 84.3L574.0 82.7L575.1 81.1L576.1 79.5L577.2 77.8L578.3 76.1L579.3 74.4L580.4 72.6L581.5 70.8L582.5 69.0L583.6 67.1L584.7 65.1L585.7 63.2L586.8 61.2L587.9 59.1L588.9 57.0L590.0 54.9L591.1 52.7L592.1 50.5L593.2 48.3L594.3 46.0L595.3 43.7L596.4 41.3L597.5 38.9L598.5 36.4L599.6 33.9L600.7 31.4"/><path class="ln-m dash" d="M350.0 87.9L606.0 87.9"/><circle class="fi" cx="570.4" cy="87.9" r="4"/><text class="tl halo" x="562.4" y="79.9" text-anchor="end">(1.59, 4)</text><text class="tb tc" x="470.0" y="20.0" text-anchor="middle">y = x³: one-one</text><text class="tl tc" x="470.0" y="262.0" text-anchor="middle">the line meets it once</text></svg><figcaption>The horizontal line test. A horizontal line that cuts a graph twice shows two inputs with the same output, so the function is many-one. If every horizontal line cuts at most once, the function is one-one.</figcaption></figure>
:::

A mapping where one input gives two outputs (such as \(y = \pm\sqrt{x}\)) is not a function at all. This matters because **only one-one functions have inverses**.

## Composite functions

Sometimes you run one machine and feed its output into a second. The result is a **composite function**. Write \(fg(x)\) for \(f(g(x))\): apply \(g\) first, then \(f\). Work from the right.

:::eg \(f(x) = 2x + 1\) and \(g(x) = x^2 - 3\), for \(x \in \mathbb{R}\). Find \(fg(x)\) and \(gf(x)\), and solve \(gf(x) = 6\).
Start with \(fg(x)\): put \(g(x)\) into \(f\).
\[\begin{aligned} fg(x) &= f\big(g(x)\big) = f(x^2 - 3) \\ &= 2(x^2 - 3) + 1 \\ &= 2x^2 - 5 \end{aligned}\]
Now \(gf(x)\): put \(f(x)\) into \(g\).
\[\begin{aligned} gf(x) &= g\big(f(x)\big) = g(2x + 1) \\ &= (2x + 1)^2 - 3 \\ &= 4x^2 + 4x - 2 \end{aligned}\]
The two answers differ, so order matters.

To solve \(gf(x) = 6\):
\[\begin{aligned} 4x^2 + 4x - 2 &= 6 \\ 4x^2 + 4x - 8 &= 0 \\ x^2 + x - 2 &= 0 \\ (x + 2)(x - 1) &= 0 \end{aligned}\]
Hence \(x = -2\) or \(x = 1\).

**Check:** \(f(1) = 3\) and \(g(3) = 9 - 3 = 6\). It works.
:::

Writing \(f^2(x)\) means \(ff(x)\), "do \(f\) twice". For \(fg\) to exist, every output of \(g\) must be an allowed input for \(f\). With \(f(x) = \sqrt{x}\) and \(g(x) = x - 5\) for \(x \geq 5\), the outputs of \(g\) are all at least 0, so \(fg(x) = \sqrt{x - 5}\) is fine. If \(g\) were defined for all real \(x\), some outputs would be negative and \(fg\) would break down.

:::warn Read composites from the right
\(fg(x)\) is not "\(f\) times \(g\)", and it does not mean "\(f\) first". It means \(f(g(x))\), so \(g\) acts first. Mixing up \(fg\) and \(gf\) is a very common way to lose marks.
:::

## Inverse functions

An **inverse function** undoes what the original did. If \(f\) turns 3 into 7, then \(f^{-1}\) turns 7 back into 3. A kettle that heats water is undone by letting it cool; subtracting 5 undoes adding 5.

:::def Inverse function
For a one-one function \(f\), the inverse function \(f^{-1}\) reverses \(f\): if \(f(a) = b\) then \(f^{-1}(b) = a\). The domain of \(f^{-1}\) is the range of \(f\), and the range of \(f^{-1}\) is the domain of \(f\).
:::

So \(f^{-1}f(x) = x\) and \(ff^{-1}(x) = x\). To find an inverse:

:::steps
1. Write \(y = f(x)\).
2. Rearrange to make \(x\) the subject.
3. Replace \(y\) by \(x\) in your answer, and write it as \(f^{-1}(x)\).
4. State the domain of \(f^{-1}\): it is the range of \(f\).
:::

:::eg \(f(x) = \dfrac{2x + 1}{x - 3}\) for \(x \neq 3\). Find \(f^{-1}(x)\), and state its domain.
Write \(y = \dfrac{2x + 1}{x - 3}\) and clear the fraction. Then collect the \(x\) terms on one side and factorise:
\[\begin{aligned} y(x - 3) &= 2x + 1 \\ xy - 3y &= 2x + 1 \\ xy - 2x &= 3y + 1 \\ x(y - 2) &= 3y + 1 \\ x &= \frac{3y + 1}{y - 2} \end{aligned}\]
So \(f^{-1}(x) = \dfrac{3x + 1}{x - 2}\).

For the domain, find the range of \(f\). Since \(2x + 1 = 2(x - 3) + 7\), we can write \(f(x) = 2 + \dfrac{7}{x - 3}\). The fraction is never zero, so \(f(x)\) never equals 2. The range is \(f(x) \neq 2\), so the domain of \(f^{-1}\) is \(x \neq 2\). This matches the denominator of \(f^{-1}(x)\).

**Check:** \(f(4) = 9\) and \(f^{-1}(9) = \dfrac{28}{7} = 4\). We return to the start.
:::

:::warn f⁻¹ is not 1/f
The "\(-1\)" in \(f^{-1}(x)\) labels the inverse function. It does **not** mean \(\dfrac{1}{f(x)}\). For \(f(x) = 2x\), the inverse is \(f^{-1}(x) = \tfrac{x}{2}\), while \(\dfrac{1}{f(x)} = \dfrac{1}{2x}\).
:::

### The graph of an inverse

Because \(f\) takes \(a\) to \(b\) and \(f^{-1}\) takes \(b\) back to \(a\), every point \((a, b)\) on the graph of \(f\) matches a point \((b, a)\) on the graph of \(f^{-1}\). Swapping coordinates is a **reflection in the line \(y = x\)**. Domain and range swap as well.

:::html
<figure class="fig"><svg viewBox="0 0 470 450" role="img" aria-label="A curve and its inverse reflected in the line y equals x"><path class="gr" d="M34.0 14V424 M86.2 14V424 M138.5 14V424 M190.8 14V424 M243.0 14V424 M295.2 14V424 M347.5 14V424 M399.8 14V424 M452.0 14V424 M34 424.0H452 M34 372.8H452 M34 321.5H452 M34 270.2H452 M34 219.0H452 M34 167.8H452 M34 116.5H452 M34 65.2H452 M34 14.0H452"/><path class="ax" d="M86.2 428V8" marker-end="url(#ahm)"/><path class="ax" d="M30 372.8H458" marker-end="url(#ahm)"/><text class="tl ti" x="454" y="366" text-anchor="end">x</text><text class="tl ti" x="93" y="18">y</text><text class="ts tc" x="34.0" y="388">−1</text><text class="ts tc" x="138.5" y="388">1</text><text class="ts tc" x="190.8" y="388">2</text><text class="ts tc" x="243.0" y="388">3</text><text class="ts tc" x="295.2" y="388">4</text><text class="ts tc" x="347.5" y="388">5</text><text class="ts tc" x="399.8" y="388">6</text><text class="ts tc" x="452.0" y="388">7</text><text class="ts te" x="81" y="428.0">−1</text><text class="ts te" x="81" y="325.5">1</text><text class="ts te" x="81" y="274.2">2</text><text class="ts te" x="81" y="223.0">3</text><text class="ts te" x="81" y="171.8">4</text><text class="ts te" x="81" y="120.5">5</text><text class="ts te" x="81" y="69.2">6</text><text class="ts te" x="81" y="18.0">7</text><text class="ts te" x="81" y="387">0</text><path class="c1" d="M190.8 321.5L192.1 321.5L193.4 321.4L194.7 321.2L196.0 321.0L197.3 320.7L198.6 320.3L199.9 319.9L201.2 319.4L202.5 318.9L203.8 318.3L205.1 317.6L206.4 316.9L207.7 316.1L209.0 315.2L210.3 314.3L211.7 313.3L213.0 312.2L214.3 311.1L215.6 309.9L216.9 308.7L218.2 307.4L219.5 306.0L220.8 304.6L222.1 303.1L223.4 301.5L224.7 299.8L226.0 298.1L227.3 296.4L228.6 294.6L229.9 292.7L231.2 290.7L232.5 288.7L233.9 286.6L235.2 284.5L236.5 282.3L237.8 280.0L239.1 277.6L240.4 275.2L241.7 272.8L243.0 270.2L244.3 267.7L245.6 265.0L246.9 262.3L248.2 259.5L249.5 256.6L250.8 253.7L252.1 250.7L253.5 247.7L254.8 244.6L256.1 241.4L257.4 238.2L258.7 234.9L260.0 231.5L261.3 228.1L262.6 224.6L263.9 221.0L265.2 217.4L266.5 213.7L267.8 210.0L269.1 206.2L270.4 202.3L271.7 198.4L273.0 194.4L274.4 190.3L275.7 186.2L277.0 182.0L278.3 177.7L279.6 173.4L280.9 169.0L282.2 164.5L283.5 160.0L284.8 155.5L286.1 150.8L287.4 146.1L288.7 141.3L290.0 136.5L291.3 131.6L292.6 126.6L293.9 121.6L295.2 116.5L296.6 111.3L297.9 106.1L299.2 100.8L300.5 95.5L301.8 90.1L303.1 84.6L304.4 79.1L305.7 73.4L307.0 67.8L308.3 62.0L309.6 56.2L310.9 50.4L312.2 44.5L313.5 38.5L314.8 32.4L316.2 26.3L317.5 20.1L318.7 14.0"/><path class="c2" d="M138.5 270.2L139.8 262.1L141.1 258.8L142.4 256.2L143.7 254.0L145.0 252.1L146.3 250.4L147.6 248.8L148.9 247.3L150.3 245.9L151.6 244.6L152.9 243.4L154.2 242.2L155.5 241.0L156.8 239.9L158.1 238.9L159.4 237.8L160.7 236.8L162.0 235.9L163.3 234.9L164.6 234.0L165.9 233.1L167.2 232.2L168.5 231.4L169.8 230.6L171.2 229.7L172.5 228.9L173.8 228.1L175.1 227.4L176.4 226.6L177.7 225.9L179.0 225.1L180.3 224.4L181.6 223.7L182.9 223.0L184.2 222.3L185.5 221.6L186.8 221.0L188.1 220.3L189.4 219.6L190.8 219.0L192.1 218.4L193.4 217.7L194.7 217.1L196.0 216.5L197.3 215.9L198.6 215.3L199.9 214.7L201.2 214.1L202.5 213.5L203.8 213.0L205.1 212.4L206.4 211.8L207.7 211.3L209.0 210.7L210.3 210.2L211.7 209.6L213.0 209.1L214.3 208.5L215.6 208.0L216.9 207.5L218.2 207.0L219.5 206.4L220.8 205.9L222.1 205.4L223.4 204.9L224.7 204.4L226.0 203.9L227.3 203.4L228.6 202.9L229.9 202.5L231.2 202.0L232.5 201.5L233.9 201.0L235.2 200.5L236.5 200.1L237.8 199.6L239.1 199.1L240.4 198.7L241.7 198.2L243.0 197.8L244.3 197.3L245.6 196.9L246.9 196.4L248.2 196.0L249.5 195.5L250.8 195.1L252.1 194.7L253.5 194.2L254.8 193.8L256.1 193.4L257.4 192.9L258.7 192.5L260.0 192.1L261.3 191.7L262.6 191.3L263.9 190.9L265.2 190.4L266.5 190.0L267.8 189.6L269.1 189.2L270.4 188.8L271.7 188.4L273.0 188.0L274.4 187.6L275.7 187.2L277.0 186.8L278.3 186.4L279.6 186.0L280.9 185.6L282.2 185.3L283.5 184.9L284.8 184.5L286.1 184.1L287.4 183.7L288.7 183.4L290.0 183.0L291.3 182.6L292.6 182.2L293.9 181.9L295.2 181.5L296.6 181.1L297.9 180.7L299.2 180.4L300.5 180.0L301.8 179.7L303.1 179.3L304.4 178.9L305.7 178.6L307.0 178.2L308.3 177.9L309.6 177.5L310.9 177.1L312.2 176.8L313.5 176.4L314.8 176.1L316.2 175.7L317.5 175.4L318.8 175.1L320.1 174.7L321.4 174.4L322.7 174.0L324.0 173.7L325.3 173.3L326.6 173.0L327.9 172.7L329.2 172.3L330.5 172.0L331.8 171.7L333.1 171.3L334.4 171.0L335.7 170.7L337.1 170.3L338.4 170.0L339.7 169.7L341.0 169.4L342.3 169.0L343.6 168.7L344.9 168.4L346.2 168.1L347.5 167.8L348.8 167.4L350.1 167.1L351.4 166.8L352.7 166.5L354.0 166.2L355.3 165.8L356.6 165.5L357.9 165.2L359.3 164.9L360.6 164.6L361.9 164.3L363.2 164.0L364.5 163.7L365.8 163.4L367.1 163.1L368.4 162.7L369.7 162.4L371.0 162.1L372.3 161.8L373.6 161.5L374.9 161.2L376.2 160.9L377.5 160.6L378.8 160.3L380.2 160.0L381.5 159.7L382.8 159.4L384.1 159.1L385.4 158.8L386.7 158.6L388.0 158.3L389.3 158.0L390.6 157.7L391.9 157.4L393.2 157.1L394.5 156.8L395.8 156.5L397.1 156.2L398.4 155.9L399.8 155.7L401.1 155.4L402.4 155.1L403.7 154.8L405.0 154.5L406.3 154.2L407.6 153.9L408.9 153.7L410.2 153.4L411.5 153.1L412.8 152.8L414.1 152.5L415.4 152.3L416.7 152.0L418.0 151.7L419.3 151.4L420.7 151.2L422.0 150.9L423.3 150.6L424.6 150.3L425.9 150.1L427.2 149.8L428.5 149.5L429.8 149.2L431.1 149.0L432.4 148.7L433.7 148.4L435.0 148.2L436.3 147.9L437.6 147.6L438.9 147.4L440.2 147.1L441.6 146.8L442.9 146.6L444.2 146.3L445.5 146.0L446.8 145.8L448.1 145.5L449.4 145.2L450.7 145.0L452.0 144.7"/><path class="ln-m dash" d="M34.0 424.0L35.3 422.7L36.6 421.4L37.9 420.2L39.2 418.9L40.5 417.6L41.8 416.3L43.1 415.0L44.4 413.8L45.8 412.5L47.1 411.2L48.4 409.9L49.7 408.6L51.0 407.3L52.3 406.1L53.6 404.8L54.9 403.5L56.2 402.2L57.5 400.9L58.8 399.7L60.1 398.4L61.4 397.1L62.7 395.8L64.0 394.5L65.3 393.2L66.7 392.0L68.0 390.7L69.3 389.4L70.6 388.1L71.9 386.8L73.2 385.6L74.5 384.3L75.8 383.0L77.1 381.7L78.4 380.4L79.7 379.2L81.0 377.9L82.3 376.6L83.6 375.3L84.9 374.0L86.2 372.8L87.6 371.5L88.9 370.2L90.2 368.9L91.5 367.6L92.8 366.3L94.1 365.1L95.4 363.8L96.7 362.5L98.0 361.2L99.3 359.9L100.6 358.7L101.9 357.4L103.2 356.1L104.5 354.8L105.8 353.5L107.1 352.2L108.5 351.0L109.8 349.7L111.1 348.4L112.4 347.1L113.7 345.8L115.0 344.6L116.3 343.3L117.6 342.0L118.9 340.7L120.2 339.4L121.5 338.2L122.8 336.9L124.1 335.6L125.4 334.3L126.7 333.0L128.1 331.8L129.4 330.5L130.7 329.2L132.0 327.9L133.3 326.6L134.6 325.3L135.9 324.1L137.2 322.8L138.5 321.5L139.8 320.2L141.1 318.9L142.4 317.7L143.7 316.4L145.0 315.1L146.3 313.8L147.6 312.5L148.9 311.2L150.3 310.0L151.6 308.7L152.9 307.4L154.2 306.1L155.5 304.8L156.8 303.6L158.1 302.3L159.4 301.0L160.7 299.7L162.0 298.4L163.3 297.2L164.6 295.9L165.9 294.6L167.2 293.3L168.5 292.0L169.8 290.8L171.2 289.5L172.5 288.2L173.8 286.9L175.1 285.6L176.4 284.3L177.7 283.1L179.0 281.8L180.3 280.5L181.6 279.2L182.9 277.9L184.2 276.7L185.5 275.4L186.8 274.1L188.1 272.8L189.4 271.5L190.8 270.2L192.1 269.0L193.4 267.7L194.7 266.4L196.0 265.1L197.3 263.8L198.6 262.6L199.9 261.3L201.2 260.0L202.5 258.7L203.8 257.4L205.1 256.2L206.4 254.9L207.7 253.6L209.0 252.3L210.3 251.0L211.7 249.7L213.0 248.5L214.3 247.2L215.6 245.9L216.9 244.6L218.2 243.3L219.5 242.1L220.8 240.8L222.1 239.5L223.4 238.2L224.7 236.9L226.0 235.7L227.3 234.4L228.6 233.1L229.9 231.8L231.2 230.5L232.5 229.2L233.9 228.0L235.2 226.7L236.5 225.4L237.8 224.1L239.1 222.8L240.4 221.6L241.7 220.3L243.0 219.0L244.3 217.7L245.6 216.4L246.9 215.2L248.2 213.9L249.5 212.6L250.8 211.3L252.1 210.0L253.5 208.8L254.8 207.5L256.1 206.2L257.4 204.9L258.7 203.6L260.0 202.3L261.3 201.1L262.6 199.8L263.9 198.5L265.2 197.2L266.5 195.9L267.8 194.7L269.1 193.4L270.4 192.1L271.7 190.8L273.0 189.5L274.4 188.3L275.7 187.0L277.0 185.7L278.3 184.4L279.6 183.1L280.9 181.8L282.2 180.6L283.5 179.3L284.8 178.0L286.1 176.7L287.4 175.4L288.7 174.2L290.0 172.9L291.3 171.6L292.6 170.3L293.9 169.0L295.2 167.8L296.6 166.5L297.9 165.2L299.2 163.9L300.5 162.6L301.8 161.3L303.1 160.1L304.4 158.8L305.7 157.5L307.0 156.2L308.3 154.9L309.6 153.7L310.9 152.4L312.2 151.1L313.5 149.8L314.8 148.5L316.2 147.2L317.5 146.0L318.8 144.7L320.1 143.4L321.4 142.1L322.7 140.8L324.0 139.6L325.3 138.3L326.6 137.0L327.9 135.7L329.2 134.4L330.5 133.2L331.8 131.9L333.1 130.6L334.4 129.3L335.7 128.0L337.1 126.8L338.4 125.5L339.7 124.2L341.0 122.9L342.3 121.6L343.6 120.3L344.9 119.1L346.2 117.8L347.5 116.5L348.8 115.2L350.1 113.9L351.4 112.7L352.7 111.4L354.0 110.1L355.3 108.8L356.6 107.5L357.9 106.2L359.3 105.0L360.6 103.7L361.9 102.4L363.2 101.1L364.5 99.8L365.8 98.6L367.1 97.3L368.4 96.0L369.7 94.7L371.0 93.4L372.3 92.2L373.6 90.9L374.9 89.6L376.2 88.3L377.5 87.0L378.8 85.8L380.2 84.5L381.5 83.2L382.8 81.9L384.1 80.6L385.4 79.3L386.7 78.1L388.0 76.8L389.3 75.5L390.6 74.2L391.9 72.9L393.2 71.7L394.5 70.4L395.8 69.1L397.1 67.8L398.4 66.5L399.8 65.2L401.1 64.0L402.4 62.7L403.7 61.4L405.0 60.1L406.3 58.8L407.6 57.6L408.9 56.3L410.2 55.0L411.5 53.7L412.8 52.4L414.1 51.2L415.4 49.9L416.7 48.6L418.0 47.3L419.3 46.0L420.7 44.7L422.0 43.5L423.3 42.2L424.6 40.9L425.9 39.6L427.2 38.3L428.5 37.1L429.8 35.8L431.1 34.5L432.4 33.2L433.7 31.9L435.0 30.7L436.3 29.4L437.6 28.1L438.9 26.8L440.2 25.5L441.6 24.3L442.9 23.0L444.2 21.7L445.5 20.4L446.8 19.1L448.1 17.8L449.4 16.6L450.7 15.3L452.0 14.0"/><circle class="fi" cx="190.8" cy="321.5" r="4"/><text class="tl halo" x="197.8" y="338.5" text-anchor="start">(2, 1)</text><circle class="fi" cx="138.5" cy="270.2" r="4"/><text class="tl halo" x="131.5" y="261.2" text-anchor="end">(1, 2)</text><circle class="fi" cx="295.2" cy="116.5" r="4"/><text class="tl halo" x="302.2" y="133.5" text-anchor="start">(4, 5)</text><circle class="fi" cx="347.5" cy="167.8" r="4"/><text class="tl halo" x="354.5" y="184.8" text-anchor="start">(5, 4)</text><text class="tl halo ta" x="324" y="45">y = f(x)</text><text class="tl halo ta2" x="366" y="124">y = f⁻¹(x)</text><text class="tl halo" x="452" y="64" text-anchor="end">y = x</text></svg><figcaption>The graph of f(x) = (x − 2)² + 1 for x ≥ 2 and its inverse f⁻¹(x) = 2 + √(x − 1) for x ≥ 1 are mirror images in the dashed line y = x. Each point swaps its coordinates, and the domain and range swap places.</figcaption></figure>
:::

If a question asks you to solve \(f(x) = f^{-1}(x)\) and \(f\) is an increasing function, the two graphs meet on the line \(y = x\), so it is enough to solve \(f(x) = x\).

## Restricting a domain

The function \(f(x) = x^2 - 4x + 7\) for \(x \in \mathbb{R}\) is many-one: the parabola is symmetrical, so two inputs share each output. But we are free to choose the domain. If we cut the parabola in half at its line of symmetry, each half is one-one and has an inverse. The line of symmetry comes from the completed square:

\[f(x) = (x - 2)^2 + 3\]

The vertex is \((2, 3)\). Restricting to \(x \geq 2\) keeps the right-hand half, whose range is \(f(x) \geq 3\). To find the inverse, rearrange \(y = (x - 2)^2 + 3\) to get \((x - 2)^2 = y - 3\), so \(x - 2 = \pm\sqrt{y - 3}\). Which sign? The original domain is \(x \geq 2\), so \(x - 2\) is positive and we take the plus sign:

\[f^{-1}(x) = 2 + \sqrt{x - 3}, \qquad x \geq 3\]

Had the domain been \(x \leq 2\), we would take the minus sign, giving \(f^{-1}(x) = 2 - \sqrt{x - 3}\).

:::exam Domains in inverse questions
"Find the smallest value of \(k\) for which \(f\) is one-one when \(x \geq k\)" asks for the \(x\)-coordinate of the vertex. Marks for "state the domain of \(f^{-1}\)" are easy to lose: it is always the **range** of \(f\), written with \(x\), for example \(x \geq 3\).
:::

:::eg (Exam style) The function \(f\) is defined by \(f(x) = 3x^2 - 12x + 5\) for \(x \geq k\). (a) Express \(f(x)\) in the form \(a(x - p)^2 + q\). (b) State the smallest value of \(k\) for which \(f\) is one-one. (c) For this value of \(k\), find \(f^{-1}(x)\) and state its domain.
**(a)** Take out a factor of 3 from the first two terms, then complete the square inside:
\[\begin{aligned} 3x^2 - 12x + 5 &= 3(x^2 - 4x) + 5 \\ &= 3\big[(x - 2)^2 - 4\big] + 5 \end{aligned}\] [M1]
\[= 3(x - 2)^2 - 7\] [A1]

**(b)** The line of symmetry is \(x = 2\), so the smallest value is \(k = 2\). [B1]

**(c)** Let \(y = 3(x - 2)^2 - 7\). Then \(\dfrac{y + 7}{3} = (x - 2)^2\). [M1]

Because \(x \geq 2\), take the positive root: \(x = 2 + \sqrt{\dfrac{y + 7}{3}}\), so
\[f^{-1}(x) = 2 + \sqrt{\frac{x + 7}{3}}\] [A1]

The domain of \(f^{-1}\) is the range of \(f\). The least value of \(f\) is \(-7\), so the domain is \(x \geq -7\). [B1]
:::

## Transformations of graphs

If you know the graph of \(y = f(x)\), you can sketch many related graphs without plotting points. Each change to the equation moves, stretches or reflects the picture in a predictable way.

| Equation | Transformation of \(y = f(x)\) |
|---|---|
| \(y = f(x) + a\) | translation \(\begin{pmatrix}0\\a\end{pmatrix}\): up \(a\)<br>\((x, y) \to (x,\, y + a)\) |
| \(y = f(x + a)\) | translation \(\begin{pmatrix}-a\\0\end{pmatrix}\): left \(a\)<br>\((x, y) \to (x - a,\, y)\) |
| \(y = af(x)\) | stretch parallel to the \(y\)-axis, scale factor \(a\)<br>\((x, y) \to (x,\, ay)\) |
| \(y = f(ax)\) | stretch parallel to the \(x\)-axis, scale factor \(\tfrac{1}{a}\)<br>\((x, y) \to (\tfrac{x}{a},\, y)\) |
| \(y = -f(x)\) | reflection in the \(x\)-axis<br>\((x, y) \to (x,\, -y)\) |
| \(y = f(-x)\) | reflection in the \(y\)-axis<br>\((x, y) \to (-x,\, y)\) |

Why does \(f(x + 2)\) move the graph **left**? Suppose \(f(3) = 5\), so \((3, 5)\) lies on \(y = f(x)\). On the new graph, the input that gives output 5 is the one with \(x + 2 = 3\), that is \(x = 1\). The point has moved from \((3, 5)\) to \((1, 5)\), two units to the left. The same reasoning shows that \(f(2x)\) reaches every output when \(x\) is only half as big, so the graph is squashed towards the \(y\)-axis.

:::key The inside/outside rule
Changes **outside** the bracket act on \(y\) and do what you expect: \(+a\) lifts, \(\times a\) stretches vertically.
Changes **inside** the bracket act on \(x\) and do the opposite: \(x + a\) moves left, \(ax\) squashes horizontally by \(\tfrac{1}{a}\).
:::

Try the sliders. The first curve is \(y = x^2\) and the second is the transformed copy. Move \(c\) and \(d\) to slide the copy sideways and up or down. Move \(a\) to stretch it, and push \(a\) below zero to flip it over.

:::html
<div class="widget" data-w="graph" data-fns="x^2; a*(x - c)^2 + d" data-x="-6,6" data-y="-6,10" data-params="a=1,-3,3,0.1; c=0,-4,4,0.5; d=0,-5,5,0.5" data-labels="y = x²; y = a(x − c)² + d"></div>
:::

When transformations are combined, work in the order you would calculate. For \(y = 3f(x) + 1\), start with \(f(x)\), multiply by 3, then add 1: stretch first, then translate. For a bracket such as \(f(2x - 4)\), first factorise it as \(f\big(2(x - 2)\big)\). Then squash by \(\tfrac12\) parallel to the \(x\)-axis, and translate 2 to the right.

:::warn Order matters
\(3f(x) + 1\) and \(3\big(f(x) + 1\big) = 3f(x) + 3\) are different graphs. Always stretch before you translate vertically. A full description of a transformation needs its type and its details: a translation needs a vector, a stretch needs a direction and a scale factor, and a reflection needs a line.
:::

:::eg (Exam style) The curve \(y = f(x)\) has a minimum point at \((2, -3)\). Write down the coordinates of the minimum point on each curve: (a) \(y = f(x + 1) - 4\), (b) \(y = 2f(x)\), (c) \(y = f(3x)\), (d) \(y = -f(x)\). (e) Describe fully the two transformations that map \(y = f(x)\) onto \(y = 3f(x - 2) + 1\), and give the image of the minimum point.
**(a)** Left 1 and down 4: \((2 - 1,\; -3 - 4) = (1, -7)\). [B1]

**(b)** The \(y\)-coordinate doubles: \((2, -6)\). [B1]

**(c)** The \(x\)-coordinate is divided by 3: \(\left(\tfrac{2}{3}, -3\right)\). [B1]

**(d)** The graph is reflected in the \(x\)-axis: \((2, 3)\), and it is now a **maximum** point. [B1]

**(e)** A stretch parallel to the \(y\)-axis with scale factor 3, [B1] followed by a translation of \(\begin{pmatrix}2\\1\end{pmatrix}\). [B1]

The minimum point moves \((2, -3) \to (2, -9) \to (4, -8)\). [B1]
:::

:::board
Cambridge puts all of this in Paper 1 (AS). The UK boards (AQA, OCR, Pearson Edexcel) split it: graph transformations are in Year 1, but domain and range, composite and inverse functions, and modulus functions are A Level (Year 2) content. Edexcel IAL covers the same ideas across P1 and P2. Notation differs slightly: Cambridge often writes \(f : x \mapsto 2x + 3\), the UK boards usually write \(f(x) = 2x + 3\), and every board accepts both. Modulus functions such as \(y = |f(x)|\) are in Cambridge Paper 3; see [Algebra: modulus, polynomials and partial fractions](#math.p3.algebra).
:::

:::try Start easy, finish at exam standard
Q: Let \(f(x) = 3x - 5\). Find \(f(4)\), \(f(-2)\) and the value of \(x\) for which \(f(x) = 10\).
A: \(f(4) = 12 - 5 = 7\) and \(f(-2) = -6 - 5 = -11\). Solving \(3x - 5 = 10\) gives \(3x = 15\), so \(x = 5\).
Q: The function \(g\) is defined by \(g(x) = 2x^2 - 8x + 3\) for \(x \geq 3\). Find the range of \(g\).
A: Complete the square: \(g(x) = 2(x - 2)^2 - 5\), with its vertex at \(x = 2\). That is **not** in the domain \(x \geq 3\). For \(x \geq 3\) the graph only rises, so the least value is \(g(3) = 18 - 24 + 3 = -3\). The range is \(g(x) \geq -3\).
Q: \(f(x) = x + 4\) and \(g(x) = 3x^2\) for \(x \in \mathbb{R}\). Find \(fg(x)\) and \(gf(x)\), and solve \(fg(x) = gf(x)\).
A: \(fg(x) = 3x^2 + 4\) and \(gf(x) = 3(x + 4)^2 = 3x^2 + 24x + 48\). Setting them equal, the \(3x^2\) terms cancel: \(4 = 24x + 48\), so \(24x = -44\) and \(x = -\tfrac{11}{6}\).
Q: Find the inverse of \(f(x) = \dfrac{5}{x - 2}\) for \(x \neq 2\), and state the domain of \(f^{-1}\).
A: Let \(y = \dfrac{5}{x - 2}\). Then \(x - 2 = \dfrac{5}{y}\), so \(x = 2 + \dfrac{5}{y}\) and \(f^{-1}(x) = 2 + \dfrac{5}{x}\). The fraction \(\dfrac{5}{x - 2}\) is never zero, so the range of \(f\) is \(f(x) \neq 0\). The domain of \(f^{-1}\) is therefore \(x \neq 0\).
Q: \(f(x) = x^2 - 6x + 10\) for \(x \geq k\). (a) Write \(f(x)\) in completed square form. (b) State the smallest \(k\) for which \(f\) is one-one. (c) For this \(k\), find \(f^{-1}(x)\) and its domain.
A: (a) \(f(x) = (x - 3)^2 + 1\). (b) The vertex is at \(x = 3\), so \(k = 3\). (c) \(y - 1 = (x - 3)^2\), and since \(x \geq 3\) we take the positive root: \(f^{-1}(x) = 3 + \sqrt{x - 1}\). The range of \(f\) is \(f(x) \geq 1\), so the domain of \(f^{-1}\) is \(x \geq 1\).
Q: State the single transformation that maps \(y = f(x)\) onto (a) \(y = f(x - 3)\), (b) \(y = 2f(x)\), (c) \(y = f\!\left(\tfrac{1}{2}x\right)\), (d) \(y = f(-x)\).
A: (a) A translation of \(\begin{pmatrix}3\\0\end{pmatrix}\), that is 3 units to the right. (b) A stretch parallel to the \(y\)-axis with scale factor 2. (c) A stretch parallel to the \(x\)-axis with scale factor 2, because the scale factor is \(1 \div \tfrac12\). (d) A reflection in the \(y\)-axis.
Q: (Exam style) (a) Express \(x^2 - 6x + 4\) in the form \((x - p)^2 + q\). (b) Describe the translation that maps the curve \(y = x^2\) onto the curve \(y = x^2 - 6x + 4\). (c) Write down the equation of the line of symmetry of \(y = x^2 - 6x + 4\).
A: (a) Half of \(-6\) is \(-3\), so \(x^2 - 6x = (x - 3)^2 - 9\) and \(x^2 - 6x + 4 = (x - 3)^2 - 5\). [M1 A1]
(b) Comparing with \(y = f(x - 3) - 5\) where \(f(x) = x^2\): a translation of \(\begin{pmatrix}3\\-5\end{pmatrix}\), that is 3 right and 5 down. [B1]
(c) The vertex is at \((3, -5)\), so the line of symmetry is \(x = 3\). [B1]
Q: (Exam style) \(f(x) = 3x - 2\) and \(g(x) = x^2 + 1\) for \(x \in \mathbb{R}\). (a) Find \(gf(x)\). (b) Solve \(gf(x) = 10\). (c) Find \(f^{-1}(x)\) and solve \(f(x) = f^{-1}(x)\).
A: (a) \(gf(x) = (3x - 2)^2 + 1 = 9x^2 - 12x + 5\). [M1 A1]
(b) \((3x - 2)^2 + 1 = 10\), so \((3x - 2)^2 = 9\) and \(3x - 2 = \pm 3\). Hence \(x = \tfrac{5}{3}\) or \(x = -\tfrac{1}{3}\). [M1 A1]
(c) From \(y = 3x - 2\) we get \(x = \dfrac{y + 2}{3}\), so \(f^{-1}(x) = \dfrac{x + 2}{3}\). [B1]
Solving \(3x - 2 = \dfrac{x + 2}{3}\): \(9x - 6 = x + 2\), so \(8x = 8\) and \(x = 1\). [M1 A1] (Because \(f\) is increasing, solving \(f(x) = x\) gives the same answer: \(3x - 2 = x\), \(x = 1\).)
:::

:::quiz
? The function \(f(x) = x^2\) is defined for all real \(x\). Which statement is true?
- \(f\) is one-one and has an inverse.
+ \(f\) is many-one, so it has no inverse as it stands.
- The range of \(f\) is all real numbers.
- \(f\) is not a function because \(f(2) = f(-2)\).
> Both 2 and \(-2\) give the output 4, so \(f\) is many-one. That is allowed for a function (each input still has one output), but a many-one function has no inverse. Its range is \(f(x) \geq 0\).
? \(f(x) = 2x + 1\) and \(g(x) = x - 4\). What is \(fg(x)\)?
+ \(2x - 7\)
- \(2x - 3\)
- \(2x^2 - 7x - 4\)
- \(2x - 8\)
> \(fg(x) = f(g(x)) = 2(x - 4) + 1 = 2x - 7\). The answer \(2x - 3\) is \(gf(x)\), found by applying the functions in the wrong order.
? How does the graph of \(y = f(x + 2)\) compare with the graph of \(y = f(x)\)?
- It moves 2 units to the right.
+ It moves 2 units to the left.
- It moves 2 units up.
- It is stretched by scale factor 2 parallel to the \(x\)-axis.
> A change inside the bracket acts on \(x\) and does the opposite of what you expect. The point \((3, 5)\) on \(y = f(x)\) becomes \((1, 5)\) on \(y = f(x + 2)\).
? \(f(x) = (x - 2)^2 + 1\) has domain \(x \geq 2\). What is the domain of \(f^{-1}\)?
- \(x \geq 2\)
+ \(x \geq 1\)
- \(x \geq 0\)
- all real numbers
> The domain of \(f^{-1}\) is the range of \(f\). The least value of \(f\) is 1, so the domain of \(f^{-1}\) is \(x \geq 1\). The value 2 is the domain of \(f\), which becomes the range of \(f^{-1}\).
:::

:::recap
- A function gives exactly one output for each input. The domain is the set of allowed inputs and the range is the set of outputs produced. Write the range with \(f(x)\) or \(y\).
- A function is one-one if each output comes from one input (horizontal line test). Only one-one functions have inverses.
- \(fg(x) = f(g(x))\): apply \(g\) first. In general \(fg \neq gf\).
- To find \(f^{-1}\): write \(y = f(x)\), make \(x\) the subject, then swap letters. Its domain is the range of \(f\), and its graph is the reflection of \(f\) in \(y = x\).
- To make a quadratic one-one, restrict its domain to one side of the vertex, which you find by completing the square. Choose the \(\pm\) in the inverse to match the original domain.
- Outside the bracket, \(f(x) + a\) and \(af(x)\) act on \(y\) as expected. Inside, \(f(x + a)\) moves left by \(a\) and \(f(ax)\) stretches horizontally by \(\tfrac{1}{a}\). \(-f(x)\) reflects in the \(x\)-axis and \(f(-x)\) in the \(y\)-axis.
- For combined transformations, work in the order you would calculate: stretch first, then translate.
:::

Next: [Coordinate geometry](#math.p1.coord) uses equations to describe straight lines and circles, and you will meet transformed circles again there.
