@chapter math.s2.poisson
@title The Poisson distribution
@level a2
@paper CAIE P6 (S2) · Edexcel IAL S2 · UK Further Maths Statistics
@time 5–7 hours
@summary The Poisson distribution models the number of random events in a fixed interval of time or space, such as calls per hour or flaws per metre. You will learn its conditions, formula, mean and variance, how to rescale it, and how it approximates the binomial and is approximated by the normal distribution.

:::why
How many calls will a rescue centre receive between 2 am and 3 am? How many flaws will a 50 m cable have? How many goals will a team score? Each of these is a count of events that happen at random but with a steady average rate. Staffing, spare parts and guarantees all depend on knowing how likely each count is. The Poisson distribution is the standard model for this kind of problem, and it is one of the main ideas in Cambridge Paper 6.
:::

**Before you start**, you should know the binomial distribution from [Discrete random variables](#math.s1.drv) and the normal distribution from [The normal distribution](#math.s1.normal). You will also use the number \(e \approx 2.718\) from [Logarithms and exponentials](#math.p3.logs).

## Counting random events

The binomial distribution counts successes in a fixed number of trials, so its count can never exceed \(n\). Many real counts have no trials and no upper limit: emails arriving in an hour, typing errors on a page, atoms decaying in a second. The count could be \(0, 1, 2, 3, \dots\) and, in principle, anything larger. The Poisson distribution models counts like these.

:::def Poisson distribution
The distribution of a random variable \(X\) that counts events in a fixed interval of time or space when the events occur singly, at random, independently of each other and at a constant average rate. We write \(X \sim \mathrm{Po}(\lambda)\), where \(\lambda\) is the mean number of events in the interval.
:::

The three conditions need a closer look, because exam questions ask you to state them and to say when they fail.

1. **Singly.** Two events cannot happen at exactly the same moment or place. Cars that arrive in convoys break this rule.
2. **Independently and at random.** One event does not make another more or less likely. Road accidents in fog often fail this, because one crash causes the next.
3. **Constant average rate.** The mean number of events is the same for every interval of the same size. Calls to a pizza shop fail this, because Friday evening is far busier than Monday afternoon.

:::exam Conditions in context
"State a condition for a Poisson model" wants the condition written in the context of the question, for example "the calls arrive independently of each other". A bare "it is random" is too vague. For "explain why the model may not be suitable", say which condition fails and why.
:::

## The formula, the mean and the variance

:::key The Poisson distribution
If \(X \sim \mathrm{Po}(\lambda)\), then
\[P(X = r) = \frac{e^{-\lambda}\,\lambda^{r}}{r!}, \qquad r = 0, 1, 2, 3, \dots\]
\[E(X) = \lambda \qquad\text{and}\qquad \mathrm{Var}(X) = \lambda\]
:::

Here \(r!\) means \(r \times (r-1) \times \dots \times 1\), and \(0! = 1\). The probability of no events is \(P(X = 0) = e^{-\lambda}\). All the probabilities add to 1 because \(1 + \lambda + \frac{\lambda^2}{2!} + \cdots = e^{\lambda}\).

The mean and the variance are equal. That is unusual and useful: if data have a mean and a variance that are very different, a Poisson model is doubtful.

:::html
<figure class="fig wide"><svg viewBox="0 0 600 230" role="img" aria-label="Three bar charts of Poisson distributions with means 1, 4 and 16"><rect class="fm" x="0" y="0" width="190" height="230" rx="10"/><rect class="f1 s-acc sw1" x="20" y="57.1" width="19.1" height="120.9"/><rect class="f1 s-acc sw1" x="42.1" y="57.1" width="19.1" height="120.9"/><rect class="f1 s-acc sw1" x="64.3" y="117.6" width="19.1" height="60.4"/><rect class="f1 s-acc sw1" x="86.5" y="157.9" width="19.1" height="20.1"/><rect class="f1 s-acc sw1" x="108.6" y="173" width="19.1" height="5"/><rect class="f1 s-acc sw1" x="130.8" y="177" width="19.1" height="1"/><rect class="f1 s-acc sw1" x="153" y="177.8" width="19.1" height="0.2"/><path class="ax" d="M10 178H184"/><path class="ax" d="M29.5 178v4"/><text class="ts tc" x="29.5" y="195">0</text><path class="ax" d="M51.7 178v4"/><text class="ts tc" x="51.7" y="195">1</text><path class="ax" d="M73.8 178v4"/><text class="ts tc" x="73.8" y="195">2</text><path class="ax" d="M96 178v4"/><text class="ts tc" x="96" y="195">3</text><path class="ax" d="M118.2 178v4"/><text class="ts tc" x="118.2" y="195">4</text><path class="ax" d="M140.3 178v4"/><text class="ts tc" x="140.3" y="195">5</text><path class="ax" d="M162.5 178v4"/><text class="ts tc" x="162.5" y="195">6</text><text class="tc tb" x="95" y="24">λ = 1</text><text class="tl ti tc" x="95" y="218">r</text><rect class="fm" x="205" y="0" width="190" height="230" rx="10"/><rect class="f1 s-acc sw1" x="222.3" y="166.5" width="10.5" height="11.5"/><rect class="f1 s-acc sw1" x="234.5" y="132" width="10.5" height="46"/><rect class="f1 s-acc sw1" x="246.8" y="86.1" width="10.5" height="91.9"/><rect class="f1 s-acc sw1" x="259" y="55.5" width="10.5" height="122.5"/><rect class="f1 s-acc sw1" x="271.3" y="55.5" width="10.5" height="122.5"/><rect class="f1 s-acc sw1" x="283.5" y="80" width="10.5" height="98"/><rect class="f1 s-acc sw1" x="295.7" y="112.6" width="10.5" height="65.4"/><rect class="f1 s-acc sw1" x="308" y="140.7" width="10.5" height="37.3"/><rect class="f1 s-acc sw1" x="320.2" y="159.3" width="10.5" height="18.7"/><rect class="f1 s-acc sw1" x="332.5" y="169.7" width="10.5" height="8.3"/><rect class="f1 s-acc sw1" x="344.7" y="174.7" width="10.5" height="3.3"/><rect class="f1 s-acc sw1" x="356.9" y="176.8" width="10.5" height="1.2"/><rect class="f1 s-acc sw1" x="369.2" y="177.6" width="10.5" height="0.4"/><path class="ax" d="M215 178H389"/><path class="ax" d="M227.6 178v4"/><text class="ts tc" x="227.6" y="195">0</text><path class="ax" d="M252 178v4"/><text class="ts tc" x="252" y="195">2</text><path class="ax" d="M276.5 178v4"/><text class="ts tc" x="276.5" y="195">4</text><path class="ax" d="M301 178v4"/><text class="ts tc" x="301" y="195">6</text><path class="ax" d="M325.5 178v4"/><text class="ts tc" x="325.5" y="195">8</text><path class="ax" d="M350 178v4"/><text class="ts tc" x="350" y="195">10</text><path class="ax" d="M374.4 178v4"/><text class="ts tc" x="374.4" y="195">12</text><text class="tc tb" x="300" y="24">λ = 4</text><text class="tl ti tc" x="300" y="218">r</text><rect class="fm" x="410" y="0" width="190" height="230" rx="10"/><rect class="f1 s-acc sw1" x="425.6" y="177.6" width="5.1" height="0.4"/><rect class="f1 s-acc sw1" x="431.6" y="176.8" width="5.1" height="1.2"/><rect class="f1 s-acc sw1" x="437.6" y="174.8" width="5.1" height="3.2"/><rect class="f1 s-acc sw1" x="443.6" y="170.6" width="5.1" height="7.4"/><rect class="f1 s-acc sw1" x="449.6" y="163.2" width="5.1" height="14.8"/><rect class="f1 s-acc sw1" x="455.5" y="151.7" width="5.1" height="26.3"/><rect class="f1 s-acc sw1" x="461.5" y="136" width="5.1" height="42"/><rect class="f1 s-acc sw1" x="467.5" y="116.9" width="5.1" height="61.1"/><rect class="f1 s-acc sw1" x="473.5" y="96.5" width="5.1" height="81.5"/><rect class="f1 s-acc sw1" x="479.5" y="77.7" width="5.1" height="100.3"/><rect class="f1 s-acc sw1" x="485.5" y="63.4" width="5.1" height="114.6"/><rect class="f1 s-acc sw1" x="491.5" y="55.7" width="5.1" height="122.3"/><rect class="f1 s-acc sw1" x="497.4" y="55.7" width="5.1" height="122.3"/><rect class="f1 s-acc sw1" x="503.4" y="62.9" width="5.1" height="115.1"/><rect class="f1 s-acc sw1" x="509.4" y="75.7" width="5.1" height="102.3"/><rect class="f1 s-acc sw1" x="515.4" y="91.9" width="5.1" height="86.1"/><rect class="f1 s-acc sw1" x="521.4" y="109.1" width="5.1" height="68.9"/><rect class="f1 s-acc sw1" x="527.4" y="125.5" width="5.1" height="52.5"/><rect class="f1 s-acc sw1" x="533.4" y="139.8" width="5.1" height="38.2"/><rect class="f1 s-acc sw1" x="539.3" y="151.4" width="5.1" height="26.6"/><rect class="f1 s-acc sw1" x="545.3" y="160.3" width="5.1" height="17.7"/><rect class="f1 s-acc sw1" x="551.3" y="166.7" width="5.1" height="11.3"/><rect class="f1 s-acc sw1" x="557.3" y="171" width="5.1" height="7"/><rect class="f1 s-acc sw1" x="563.3" y="173.9" width="5.1" height="4.1"/><rect class="f1 s-acc sw1" x="569.3" y="175.6" width="5.1" height="2.4"/><rect class="f1 s-acc sw1" x="575.3" y="176.7" width="5.1" height="1.3"/><rect class="f1 s-acc sw1" x="581.2" y="177.3" width="5.1" height="0.7"/><path class="c2" d="M425.8 177L427.1 176.8L428.5 176.6L429.8 176.3L431.1 176L432.5 175.7L433.8 175.3L435.2 174.9L436.5 174.4L437.8 173.8L439.2 173.1L440.5 172.4L441.8 171.6L443.2 170.7L444.5 169.6L445.8 168.5L447.2 167.2L448.5 165.8L449.9 164.3L451.2 162.6L452.5 160.8L453.9 158.8L455.2 156.7L456.5 154.4L457.9 151.9L459.2 149.2L460.6 146.4L461.9 143.4L463.2 140.3L464.6 136.9L465.9 133.5L467.2 129.9L468.6 126.1L469.9 122.3L471.2 118.3L472.6 114.3L473.9 110.2L475.3 106L476.6 101.8L477.9 97.7L479.3 93.6L480.6 89.5L481.9 85.6L483.3 81.8L484.6 78.1L485.9 74.6L487.3 71.3L488.6 68.3L490 65.5L491.3 63L492.6 60.8L494 59L495.3 57.5L496.6 56.3L498 55.6L499.3 55.2L500.7 55.2L502 55.5L503.3 56.3L504.7 57.4L506 58.9L507.3 60.7L508.7 62.9L510 65.4L511.3 68.1L512.7 71.2L514 74.4L515.4 77.9L516.7 81.6L518 85.4L519.4 89.4L520.7 93.4L522 97.5L523.4 101.7L524.7 105.8L526.1 110L527.4 114.1L528.7 118.1L530.1 122.1L531.4 126L532.7 129.7L534.1 133.3L535.4 136.8L536.7 140.1L538.1 143.3L539.4 146.3L540.8 149.1L542.1 151.8L543.4 154.3L544.8 156.6L546.1 158.7L547.4 160.7L548.8 162.6L550.1 164.2L551.4 165.8L552.8 167.2L554.1 168.4L555.5 169.6L556.8 170.6L558.1 171.5L559.5 172.4L560.8 173.1L562.1 173.8L563.5 174.3L564.8 174.8L566.2 175.3L567.5 175.7L568.8 176L570.2 176.3L571.5 176.6L572.8 176.8L574.2 177L575.5 177.1L576.8 177.3L578.2 177.4L579.5 177.5L580.9 177.6L582.2 177.7L583.5 177.7L584.9 177.8L586.2 177.8"/><path class="ax" d="M420 178H594"/><path class="ax" d="M434.2 178v4"/><text class="ts tc" x="434.2" y="195">5</text><path class="ax" d="M464.1 178v4"/><text class="ts tc" x="464.1" y="195">10</text><path class="ax" d="M494 178v4"/><text class="ts tc" x="494" y="195">15</text><path class="ax" d="M524 178v4"/><text class="ts tc" x="524" y="195">20</text><path class="ax" d="M553.9 178v4"/><text class="ts tc" x="553.9" y="195">25</text><path class="ax" d="M583.8 178v4"/><text class="ts tc" x="583.8" y="195">30</text><text class="tc tb" x="505" y="24">λ = 16</text><text class="tl ti tc" x="505" y="218">r</text></svg><figcaption>Poisson probabilities P(X = r) for three means (vertical scales differ). For a small mean the bars pile up against 0 and tail off to the right. As λ grows the shape becomes symmetric and bell-like; the curve on the right is N(16, 16).</figcaption></figure>
:::

:::tip Building probabilities step by step
Each probability comes from the one before: \(P(X = r + 1) = \dfrac{\lambda}{r + 1}\,P(X = r)\). For \(\lambda = 4\): \(P(0) = e^{-4} = 0.0183\), then \(P(1) = 4 \times 0.0183 = 0.0733\), then \(P(2) = \frac{4}{2} \times 0.0733 = 0.1465\). Keep full calculator accuracy and round only at the end.
:::

Poisson counts have no upper limit, so "at least" and "more than" need the complement.

| Words in the question | Meaning | Calculate |
|---|---|---|
| at most 3, no more than 3 | \(X \le 3\) | \(P(0) + P(1) + P(2) + P(3)\) |
| fewer than 3 | \(X \le 2\) | \(P(0) + P(1) + P(2)\) |
| at least 3 | \(X \ge 3\) | \(1 - P(X \le 2)\) |
| more than 3 | \(X \ge 4\) | \(1 - P(X \le 3)\) |

:::eg Emails arrive at random, with a mean of 4 per hour. Find the probability that in a given hour (a) exactly 3 arrive, (b) at most 2 arrive, (c) at least 6 arrive.
Let \(X\) be the number of emails in an hour. Then \(X \sim \mathrm{Po}(4)\).

(a) \(P(X = 3) = \dfrac{e^{-4}\,4^{3}}{3!} = \dfrac{32}{3}e^{-4} = 0.195\)

(b) \(P(X \le 2) = e^{-4}\left(1 + 4 + \dfrac{4^{2}}{2}\right) = 13e^{-4} = 0.238\)

(c) "At least 6" is the opposite of "at most 5", so
\[P(X \ge 6) = 1 - e^{-4}\left(1 + 4 + 8 + \tfrac{32}{3} + \tfrac{32}{3} + \tfrac{128}{15}\right) = 1 - 0.7851 = 0.215\]
:::

## Changing the interval

The mean \(\lambda\) belongs to one particular interval. Because the rate is constant, a longer or shorter interval has a proportionally larger or smaller mean.

:::key Scaling the mean
If events occur at a constant average rate of \(k\) per unit of time (or length, or area), the number of events in an interval of size \(t\) has distribution \(\mathrm{Po}(kt)\).
:::

Always write down the new distribution before you calculate. Counts in separate intervals add, and so do their means: if the number of emails in one hour is \(\mathrm{Po}(4)\), the number in two hours is \(\mathrm{Po}(8)\). [Linear combinations of random variables](#math.s2.linear) proves this.

:::warn Scale the mean, not the probability
If \(P(\text{no flaws in 10 m}) = 0.449\), then \(P(\text{no flaws in 20 m})\) is **not** \(2 \times 0.449\). Double the mean to \(\lambda = 1.6\) and recalculate: \(e^{-1.6} = 0.202\). As a check, both 10 m halves must be flawless, and \(0.449^{2} = 0.202\).
:::

:::eg Flaws occur at random in a cable at an average rate of 0.8 per 10 m. Find the probability that (a) a 25 m length has no flaws, (b) a 5 m length has at least 2 flaws.
(a) In 25 m the mean is \(0.8 \times 2.5 = 2.0\), so \(X \sim \mathrm{Po}(2)\) and
\[P(X = 0) = e^{-2} = 0.135\]
(b) In 5 m the mean is \(0.8 \times 0.5 = 0.4\), so \(Y \sim \mathrm{Po}(0.4)\) and
\[P(Y \ge 2) = 1 - P(Y = 0) - P(Y = 1) = 1 - e^{-0.4}(1 + 0.4) = 1 - 0.9384 = 0.0616\]
:::

## Poisson as an approximation to the binomial

A binomial \(B(n, p)\) with large \(n\) and small \(p\) counts rare events among many trials, which is the Poisson situation. Its mean is \(np\) and its variance is \(npq\). When \(p\) is small, \(q = 1 - p\) is close to 1, so the variance is close to the mean, just as for a Poisson variable. That is why \(\mathrm{Po}(np)\) fits.

| | Binomial \(B(n, p)\) | Poisson \(\mathrm{Po}(\lambda)\) |
|---|---|---|
| What is counted | successes in \(n\) trials | events in an interval |
| Possible values | \(0, 1, \dots, n\) | \(0, 1, 2, \dots\) with no limit |
| Mean and variance | \(np\) and \(npq\) | both equal to \(\lambda\) |
| Parameters | two: \(n\) and \(p\) | one: \(\lambda\) |

:::key Poisson approximation to the binomial
If \(X \sim B(n, p)\) with \(n > 50\) and \(np < 5\), then \(X\) is approximately \(\mathrm{Po}(np)\).
:::

:::eg In a factory 2% of light bulbs are faulty, independently of each other. A random sample of 150 bulbs is tested. (a) Explain why a Poisson distribution is a suitable approximation. (b) Use it to find the probability that at most 2 bulbs are faulty. (c) Find the exact probability and comment.
(a) Let \(X\) be the number of faulty bulbs, so \(X \sim B(150, 0.02)\). Here \(n = 150 > 50\) and \(np = 3 < 5\). [B1] So \(X\) is approximately \(\mathrm{Po}(3)\). [B1]

(b) \(P(X \le 2) \approx e^{-3}\left(1 + 3 + \dfrac{9}{2}\right) = 8.5e^{-3}\) [M1] \(= 0.423\) [A1]

(c) Exactly, \(P(X \le 2) = 0.98^{150} + 150(0.02)(0.98)^{149} + \binom{150}{2}(0.02)^{2}(0.98)^{148} = 0.421\). [B1] The two answers differ by only 0.002, so the approximation is very good. [B1]
:::

## The normal approximation to the Poisson

Look again at the third panel of the figure. When \(\lambda\) is large the Poisson distribution is nearly symmetric and bell-shaped, so a normal curve with the same mean and variance fits it.

:::key Normal approximation to the Poisson
If \(X \sim \mathrm{Po}(\lambda)\) with \(\lambda > 15\), then \(X\) is approximately \(N(\lambda, \lambda)\). The mean is \(\lambda\), the variance is \(\lambda\) and the standard deviation is \(\sqrt{\lambda}\).
:::

A Poisson variable takes whole numbers only, while a normal variable is continuous. In the figure below, the bar for \(r = 20\) is centred on 20 and stretches from 19.5 to 20.5. To include the whole bar we start the normal area at 19.5. This adjustment is called the continuity correction.

:::def Continuity correction
The adjustment of 0.5 made when a discrete variable (taking whole numbers) is approximated by a continuous one, so that each whole number is represented by the interval from 0.5 below to 0.5 above it.
:::

:::html
<figure class="fig"><svg viewBox="0 0 580 250" role="img" aria-label="Bars for Poisson with mean 16 with the bars from 20 upwards highlighted and a normal curve; the cut-off is at 19.5"><rect class="f1 s-acc sw1" x="38.6" y="187.7" width="24" height="18.3"/><rect class="f1 s-acc sw1" x="65.3" y="173.4" width="24" height="32.6"/><rect class="f1 s-acc sw1" x="91.9" y="153.8" width="24" height="52.2"/><rect class="f1 s-acc sw1" x="118.5" y="130.1" width="24" height="75.9"/><rect class="f1 s-acc sw1" x="145.2" y="104.8" width="24" height="101.2"/><rect class="f1 s-acc sw1" x="171.8" y="81.4" width="24" height="124.6"/><rect class="f1 s-acc sw1" x="198.5" y="63.6" width="24" height="142.4"/><rect class="f1 s-acc sw1" x="225.1" y="54.2" width="24" height="151.8"/><rect class="f1 s-acc sw1" x="251.7" y="54.2" width="24" height="151.8"/><rect class="f1 s-acc sw1" x="278.4" y="63.1" width="24" height="142.9"/><rect class="f1 s-acc sw1" x="305" y="79" width="24" height="127"/><rect class="f1 s-acc sw1" x="331.6" y="99" width="24" height="107"/><rect class="f3 s-red sw1" x="358.3" y="120.4" width="24" height="85.6"/><rect class="f3 s-red sw1" x="384.9" y="140.8" width="24" height="65.2"/><rect class="f3 s-red sw1" x="411.5" y="158.6" width="24" height="47.4"/><rect class="f3 s-red sw1" x="438.2" y="173" width="24" height="33"/><rect class="f3 s-red sw1" x="464.8" y="184" width="24" height="22"/><rect class="f3 s-red sw1" x="491.4" y="191.9" width="24" height="14.1"/><rect class="f3 s-red sw1" x="518.1" y="197.3" width="24" height="8.7"/><path class="c2" d="M29.3 192.4L33.1 191.3L36.9 190.2L40.6 189L44.4 187.7L48.2 186.3L51.9 184.8L55.7 183.3L59.5 181.7L63.2 180L67 178.2L70.8 176.4L74.5 174.5L78.3 172.4L82.1 170.3L85.8 168.1L89.6 165.8L93.4 163.5L97.1 161L100.9 158.5L104.7 155.9L108.4 153.2L112.2 150.5L116 147.6L119.7 144.8L123.5 141.8L127.3 138.8L131 135.7L134.8 132.6L138.6 129.4L142.3 126.2L146.1 123L149.9 119.8L153.6 116.5L157.4 113.2L161.2 109.9L164.9 106.7L168.7 103.4L172.5 100.2L176.2 97L180 93.9L183.8 90.8L187.5 87.8L191.3 84.8L195.1 82L198.8 79.2L202.6 76.5L206.4 73.9L210.1 71.5L213.9 69.2L217.7 67L221.4 64.9L225.2 63L229 61.3L232.7 59.7L236.5 58.3L240.3 57L244 55.9L247.8 55.1L251.6 54.3L255.3 53.8L259.1 53.5L262.9 53.4L266.6 53.4L270.4 53.7L274.2 54.1L277.9 54.7L281.7 55.5L285.5 56.5L289.2 57.7L293 59L296.8 60.5L300.5 62.2L304.3 64.1L308.1 66L311.8 68.2L315.6 70.4L319.4 72.8L323.1 75.4L326.9 78L330.7 80.7L334.4 83.6L338.2 86.5L342 89.5L345.7 92.5L349.5 95.6L353.3 98.8L357 102L360.8 105.2L364.6 108.5L368.3 111.8L372.1 115L375.9 118.3L379.6 121.6L383.4 124.8L387.2 128L390.9 131.2L394.7 134.3L398.5 137.4L402.2 140.5L406 143.4L409.8 146.4L413.5 149.2L417.3 152L421.1 154.7L424.8 157.4L428.6 159.9L432.4 162.4L436.1 164.8L439.9 167.1L443.7 169.4L447.4 171.5L451.2 173.6L455 175.5L458.7 177.4L462.5 179.2L466.3 181L470 182.6L473.8 184.2L477.6 185.7L481.3 187.1L485.1 188.4L488.9 189.6L492.6 190.8L496.4 192L500.2 193L503.9 194L507.7 194.9L511.5 195.8L515.2 196.6L519 197.4L522.8 198.1L526.5 198.7L530.3 199.3L534.1 199.9L537.8 200.4L541.6 200.9L545.4 201.4L549.1 201.8L552.9 202.2L556.7 202.5"/><path class="ln-m dash" d="M356.9 206V33.1"/><path class="ax" d="M20 206H568"/><path class="ax" d="M50.6 206v4"/><text class="ts tc" x="50.6" y="223">8</text><path class="ax" d="M103.9 206v4"/><text class="ts tc" x="103.9" y="223">10</text><path class="ax" d="M157.2 206v4"/><text class="ts tc" x="157.2" y="223">12</text><path class="ax" d="M210.4 206v4"/><text class="ts tc" x="210.4" y="223">14</text><path class="ax" d="M263.7 206v4"/><text class="ts tc" x="263.7" y="223">16</text><path class="ax" d="M317 206v4"/><text class="ts tc" x="317" y="223">18</text><path class="ax" d="M370.2 206v4"/><text class="ts tc" x="370.2" y="223">20</text><path class="ax" d="M423.5 206v4"/><text class="ts tc" x="423.5" y="223">22</text><path class="ax" d="M476.8 206v4"/><text class="ts tc" x="476.8" y="223">24</text><path class="ax" d="M530 206v4"/><text class="ts tc" x="530" y="223">26</text><text class="ts te" x="350.9" y="35.4">19.5</text><text class="tl tr tc" x="468.8" y="97.3">P(X ≥ 20) ≈ P(Y > 19.5)</text><text class="ts tc" x="468.8" y="114.3">bars from 20 upwards</text><text class="tl ta2 tc" x="135.9" y="70.6">Y ~ N(16, 16)</text><text class="tl ti te" x="556.7" y="242">r</text></svg><figcaption>To approximate P(X ≥ 20) the bars for 20, 21, 22, … are replaced by the area under the normal curve to the right of 19.5, the left edge of the bar for 20. This is the continuity correction.</figcaption></figure>
:::

Let \(Y\) be the normal variable.

| Poisson probability | Normal calculation |
|---|---|
| \(P(X = 20)\) | \(P(19.5 < Y < 20.5)\) |
| \(P(X \le 20)\) | \(P(Y < 20.5)\) |
| \(P(X < 20)\) | \(P(Y < 19.5)\) |
| \(P(X \ge 20)\) | \(P(Y > 19.5)\) |
| \(P(X > 20)\) | \(P(Y > 20.5)\) |

:::tip A reliable routine
First rewrite the inequality so it contains "\(\le\)" or "\(\ge\)" and a whole number (so \(X < 20\) becomes \(X \le 19\)). Then add 0.5 to a "\(\le\)" value and subtract 0.5 from a "\(\ge\)" value. A quick sketch of the bars confirms the choice.
:::

:::eg \(X \sim \mathrm{Po}(24)\). Use a normal approximation to find \(P(X \ge 30)\).
Since \(\lambda = 24 > 15\), use \(Y \sim N(24, 24)\), so \(\sigma = \sqrt{24} = 4.899\).

\[P(X \ge 30) \approx P(Y > 29.5)\] 
Standardise: \(z = \dfrac{29.5 - 24}{\sqrt{24}} = 1.123\), so
\[P(Y > 29.5) = 1 - \Phi(1.123) = 0.131\]
The exact Poisson answer is 0.132, so the approximation is good.
:::

:::warn Variance, not standard deviation
For \(N(\lambda, \lambda)\) the second number is the **variance**. Divide by \(\sqrt{\lambda}\), not by \(\lambda\), when you standardise. Forgetting the continuity correction costs a mark in every exam question on this topic.
:::

:::eg Cars pass a speed camera at random, at a constant average rate of 3.2 per minute. (a) State two conditions needed for a Poisson model. (b) Find the probability that exactly 2 cars pass in a given minute. (c) Find the probability that fewer than 3 cars pass in a 30-second period. (d) Use a suitable approximation to find the probability that more than 20 cars pass in a 5-minute period.
(a) Cars pass singly (never two at exactly the same instant) and independently of each other. [B1 B1]

(b) \(X \sim \mathrm{Po}(3.2)\), so \(P(X = 2) = \dfrac{e^{-3.2}\,3.2^{2}}{2!} = 0.209\). [M1 A1]

(c) In 30 seconds the mean is 1.6, so \(Y \sim \mathrm{Po}(1.6)\). [B1]
\[P(Y < 3) = P(Y \le 2) = e^{-1.6}\left(1 + 1.6 + \frac{1.6^{2}}{2}\right) = 0.783\] [M1 A1]

(d) In 5 minutes the mean is 16, so \(W \sim \mathrm{Po}(16)\). Since \(16 > 15\), \(W\) is approximately \(N(16, 16)\). [B1]
"More than 20" means \(W \ge 21\), so \(P(W > 20) \approx P(N > 20.5)\). [M1]
\[z = \frac{20.5 - 16}{\sqrt{16}} = 1.125, \qquad 1 - \Phi(1.125) = 0.130\] [M1 A1]
:::

:::board
**Cambridge 9709** examines the Poisson distribution only in Paper 6 (Probability and Statistics 2) and states the conditions \(n > 50\), \(np < 5\) and \(\lambda > 15\). **Edexcel IAL** covers it in Statistics 2 with the same two approximations, but describes the conditions loosely ("\(n\) large, \(p\) small", "\(\lambda\) large"), so follow the wording of the question. **AQA, OCR and Edexcel A Level Mathematics** in the UK do not include the Poisson distribution; it appears in their A Level Further Mathematics statistics options.
:::

:::try Start easy, finish at exam standard
Q: \(X \sim \mathrm{Po}(1.5)\). Find (a) \(P(X = 2)\), (b) \(P(X \ge 1)\).
A: (a) \(P(X = 2) = \dfrac{e^{-1.5} \times 1.5^{2}}{2} = 0.251\).
(b) \(P(X \ge 1) = 1 - P(X = 0) = 1 - e^{-1.5} = 0.777\).
Q: Say whether a Poisson model is reasonable in each case. If not, state which condition fails or why the variable is not Poisson. (a) The number of texts you receive in each hour of a whole day. (b) The number of sixes in 12 rolls of a die. (c) The number of accidents per day on a motorway, when one crash in fog is usually followed by several more.
A: (a) Not reasonable: the rate is not constant (many more texts in the evening than at 4 am), and conversations make texts dependent.
(b) Not Poisson: there are a fixed number of trials (12), so the count cannot exceed 12. It is binomial, \(B(12, \tfrac16)\).
(c) Not reasonable: accidents are not independent, because one crash makes another more likely.
Q: Typing errors occur at random, at a mean rate of 2 per page. Find the probability of (a) no errors on one page, (b) at least one error in 3 pages, (c) exactly 4 errors in 2 pages.
A: (a) \(X \sim \mathrm{Po}(2)\): \(P(X = 0) = e^{-2} = 0.135\).
(b) In 3 pages the mean is 6: \(P(Y \ge 1) = 1 - e^{-6} = 0.998\).
(c) In 2 pages the mean is 4: \(P(W = 4) = \dfrac{e^{-4}\,4^{4}}{4!} = 0.195\).
Q: \(X \sim \mathrm{Po}(\lambda)\) and \(P(X = 0) = 0.2\). Find \(\lambda\) and hence \(P(X = 1)\).
A: \(e^{-\lambda} = 0.2\), so \(\lambda = \ln 5 = 1.609\). Then \(P(X = 1) = \lambda e^{-\lambda} = 1.609 \times 0.2 = 0.322\).
Q: \(Y \sim \mathrm{Po}(\lambda)\) and \(P(Y = 3) = 2P(Y = 2)\). Find \(\lambda\) and \(P(Y \le 4)\).
A: \(\dfrac{P(Y = 3)}{P(Y = 2)} = \dfrac{\lambda}{3}\), so \(\dfrac{\lambda}{3} = 2\) and \(\lambda = 6\). [M1 A1]
\(P(Y \le 4) = e^{-6}\left(1 + 6 + 18 + 36 + 54\right) = 115e^{-6} = 0.285\). [M1 A1]
Q: \(X \sim B(80, 0.03)\). Show that a Poisson approximation is suitable and use it to find \(P(X \ge 3)\).
A: \(n = 80 > 50\) and \(np = 2.4 < 5\), so \(X\) is approximately \(\mathrm{Po}(2.4)\).
\(P(X \ge 3) = 1 - e^{-2.4}\left(1 + 2.4 + \dfrac{2.4^{2}}{2}\right) = 1 - 0.5697 = 0.430\).
Q: \(X \sim \mathrm{Po}(20)\). Use a normal approximation to find \(P(X < 15)\).
A: \(X\) is approximately \(Y \sim N(20, 20)\). \(P(X < 15) = P(X \le 14) \approx P(Y < 14.5)\). [M1]
\(z = \dfrac{14.5 - 20}{\sqrt{20}} = -1.230\), so the probability is \(\Phi(-1.230) = 0.109\). [M1 A1]
Q: (Exam style) A bakery sells a speciality loaf at random, at a mean rate of 4 loaves per day. (a) The bakery bakes 7 loaves each day. Find the probability that it runs out, meaning demand is more than 7. (b) The bakery wants the probability of running out to be less than 1%. What is the smallest number of loaves it should bake each day? (c) Baking 7 loaves a day, find the probability that it runs out on exactly 2 of the next 5 days.
A: (a) \(X \sim \mathrm{Po}(4)\). \(P(X > 7) = 1 - P(X \le 7) = 1 - 0.9489 = 0.0511\). [M1 A1]
(b) We need \(P(X > n) < 0.01\), that is \(P(X \le n) > 0.99\). [M1]
\(P(X \le 8) = 0.9786\), which is too small, but \(P(X \le 9) = 0.9919\). The bakery should bake 9 loaves. [A1]
(c) The days are independent, so the number of run-out days is \(B(5, 0.0511)\). [M1]
\(P(\text{exactly 2}) = \binom{5}{2}(0.0511)^{2}(0.9489)^{3} = 0.0223\). [A1]
:::

:::quiz Quick check
? Which of these is **not** a condition for a Poisson model?
- Events occur independently of each other
- Events occur at a constant average rate
+ There is a fixed number of trials
- Events occur singly
> A fixed number of trials belongs to the binomial distribution. A Poisson count has no upper limit.
? Cars pass a point at a mean rate of 6 per minute. The number passing in 20 seconds has the distribution
- \(\mathrm{Po}(6)\)
+ \(\mathrm{Po}(2)\)
- \(\mathrm{Po}(18)\)
- \(\mathrm{Po}(0.33)\)
> 20 seconds is one third of a minute, so the mean is \(6 \times \tfrac13 = 2\).
? \(X \sim \mathrm{Po}(25)\). Which expression gives the normal approximation to \(P(X \ge 30)\)?
+ \(P(Y > 29.5)\) with \(Y \sim N(25, 25)\)
- \(P(Y > 30.5)\) with \(Y \sim N(25, 25)\)
- \(P(Y > 29.5)\) with \(Y \sim N(25, 5)\)
- \(P(Y > 30)\) with \(Y \sim N(25, 25)\)
> "30 or more" starts at the lower edge of the bar for 30, which is 29.5. The variance is 25, so the second number in \(N(25, 25)\) is correct.
? \(X \sim B(200, 0.01)\). Which approximation is suitable?
+ \(\mathrm{Po}(2)\)
- \(\mathrm{Po}(200)\)
- \(N(200, 0.01)\)
- \(\mathrm{Po}(0.01)\)
> Here \(n = 200 > 50\) and \(np = 2 < 5\), so use \(\mathrm{Po}(np) = \mathrm{Po}(2)\).
:::

:::recap
- A Poisson variable counts events in a fixed interval when events occur singly, independently and at a constant average rate. Write \(X \sim \mathrm{Po}(\lambda)\).
- \(P(X = r) = \dfrac{e^{-\lambda}\lambda^{r}}{r!}\) for \(r = 0, 1, 2, \dots\), with \(E(X) = \mathrm{Var}(X) = \lambda\).
- "At least" and "more than" use the complement: \(P(X \ge 3) = 1 - P(X \le 2)\).
- Scale the mean, never the probability: rate \(k\) per unit gives \(\mathrm{Po}(kt)\) over an interval of size \(t\).
- If \(X \sim B(n, p)\) with \(n > 50\) and \(np < 5\), then \(X \approx \mathrm{Po}(np)\).
- If \(X \sim \mathrm{Po}(\lambda)\) with \(\lambda > 15\), then \(X \approx N(\lambda, \lambda)\). Use the continuity correction of 0.5.
- In exam answers, state conditions in context and show the substituted formula before the calculator value.
:::

Next: [Linear combinations of random variables](#math.s2.linear) shows how to add independent random variables, including Poisson ones.
