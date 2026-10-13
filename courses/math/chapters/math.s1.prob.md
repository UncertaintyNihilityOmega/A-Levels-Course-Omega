@chapter math.s1.prob
@title Probability
@level a2
@paper CAIE P5 (check your specification for other boards)
@time 8–10 hours
@summary Probability from first principles: sample spaces and equally likely outcomes, Venn diagrams, mutually exclusive and independent events, tree diagrams with and without replacement, conditional probability \(P(A \mid B)\), and probabilities found by counting with permutations and combinations.

:::why
Probability puts a number on uncertainty: the chance a part is faulty, a flight is late, a test returns a false alarm. The rules are few, but the exam questions are long, because real situations have several stages and conditions. A tree diagram or a Venn diagram turns the words into a picture, and the same three or four rules read the answer off the picture.
:::

**Before you start**, you need fractions, decimals and percentages from [Numbers from scratch](#math.f.numbers) and the counting methods from [Permutations and combinations](#math.s1.perms).

:::try Warm-up
Q: Work out \(\dfrac38 \times \dfrac47\) and give the answer as a fraction in its simplest form. (from [Numbers from scratch](#math.f.numbers))
A: \(\dfrac{12}{56} = \dfrac{3}{14}\).
Q: Solve \(0.8 = 0.6 + b - 0.6b\). (from [Algebra from scratch](#math.f.algebra))
A: Collect the terms in \(b\): \(0.8 = 0.6 + 0.4b\), so \(0.4b = 0.2\) and \(b = 0.5\).
Q: In how many ways can a committee of 3 be chosen from 8 people? (from [Permutations and combinations](#math.s1.perms))
A: Order does not matter, so \(\dbinom83 = 56\).
:::

## Sample spaces and equally likely outcomes

:::def Event, sample space and probability
An **event** is an outcome, or a set of outcomes, of an experiment. The **sample space** is the set of all possible outcomes. When all outcomes are **equally likely**, the probability of an event \(A\) is
\[P(A) = \frac{\text{number of outcomes in } A}{\text{total number of outcomes}}\]
Probabilities lie between 0 (impossible) and 1 (certain). The **complement** \(A'\) is "\(A\) does not happen", and \(P(A') = 1 - P(A)\).
:::

:::eg Two fair dice are rolled. Find the probability that (a) the total is 7, (b) the total is at least 10, (c) at least one die shows a 6.
The sample space has \(6 \times 6 = 36\) equally likely outcomes.
(a) The pairs with total 7 are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1): 6 outcomes, so \(\dfrac{6}{36} = \dfrac16\).
(b) Total at least 10: (4,6), (5,5), (6,4), (5,6), (6,5), (6,6): 6 outcomes, so \(\dfrac16\).
(c) Use the complement: no die shows a 6 in \(5\times 5 = 25\) outcomes, so \(P = 1 - \dfrac{25}{36}\) \(= \dfrac{11}{36}\).
:::

## Combining events: addition and Venn diagrams

:::key Probability of "A or B"
\[P(A \cup B) = P(A) + P(B) - P(A \cap B)\]
\(A \cup B\) means "\(A\) or \(B\) or both"; \(A \cap B\) means "\(A\) and \(B\)". Subtract the overlap so it is not counted twice.
:::

A **Venn diagram** shows the sample space as a rectangle and each event as a region. Fill in the overlap first (the intersection), then work outwards.

:::eg Of 40 students, 25 like tea (\(T\)), 18 like coffee (\(C\)) and 8 like both. Find the number who like neither, \(P(T \cup C)\), \(P(T \mid C)\), and say whether \(T\) and \(C\) are independent.
Start with the overlap: 8 like both. Tea only: \(25 - 8 = 17\). Coffee only: \(18 - 8 = 10\). At least one: \(17 + 8 + 10 = 35\), so neither: \(40 - 35 = 5\).
\(P(T \cup C) = \dfrac{35}{40}\) \(= \dfrac78\).
\(P(T \mid C)\) is the probability of tea given coffee: restrict to the 18 coffee drinkers, 8 of whom like tea. So \(P(T \mid C) = \dfrac{8}{18} = \dfrac49\).
Independence needs \(P(T \cap C) = P(T)P(C)\). Here \(P(T \cap C) = \dfrac{8}{40} = 0.2\), but \(P(T)P(C) = 0.625 \times 0.45 = 0.28125\). They differ, so \(T\) and \(C\) are not independent.
:::

## Mutually exclusive and independent events

:::def Mutually exclusive and independent
Events \(A\) and \(B\) are **mutually exclusive** if they cannot both happen: \(P(A \cap B) = 0\), so \(P(A \cup B) = P(A) + P(B)\).
Events \(A\) and \(B\) are **independent** if the occurrence of one does not change the probability of the other: \(P(A \cap B) = P(A) \times P(B)\), equivalently \(P(A \mid B) = P(A)\).
:::

:::warn Exclusive is not independent
These are different ideas, and often confused. If \(A\) and \(B\) are mutually exclusive and both have non-zero probability, they are **not** independent: if \(A\) happens, then \(B\) cannot, so knowing about \(A\) changes the probability of \(B\) to 0. Test independence with the product rule, never by looking at a Venn diagram.
:::

:::eg \(P(A) = 0.4\) and \(P(B) = 0.5\). Find \(P(A \cup B)\) if (a) \(A\) and \(B\) are independent, (b) \(A\) and \(B\) are mutually exclusive.
(a) \(P(A \cap B) = 0.4 \times 0.5 = 0.2\), so \(P(A \cup B) = 0.4 + 0.5 - 0.2 = 0.7\).
(b) \(P(A \cap B) = 0\), so \(P(A \cup B) = 0.4 + 0.5 = 0.9\).
:::

For independent repeated trials, multiply: the probability of tossing a fair coin 3 times and getting at least one head is \(1 - \left(\tfrac12\right)^3 = \tfrac78\), and the probability that a fair die first shows a six on the third throw is \(\left(\tfrac56\right)^2\times\tfrac16\) \(= \tfrac{25}{216} = 0.116\).

## Tree diagrams

A **tree diagram** shows the stages of an experiment as branches. Each branch carries a probability; **multiply along** a path to find the probability of that sequence, and **add** the results of the paths that make up an event. The probabilities leaving any one point sum to 1.

When items are drawn **without replacement**, the probabilities on the second stage change, because the numbers in the bag have changed.

:::eg A bag contains 5 red and 3 blue counters. Two are drawn without replacement. Find the probability of (a) two red, (b) one of each colour, (c) two blue.
First draw: \(P(R) = \dfrac58\), \(P(B) = \dfrac38\). If the first is red, 4 red and 3 blue remain (7 counters): \(P(R) = \dfrac47\), \(P(B) = \dfrac37\). If the first is blue, 5 red and 2 blue remain: \(P(R) = \dfrac57\), \(P(B) = \dfrac27\).
(a) \(P(RR) = \dfrac58\times\dfrac47\) \(= \dfrac{20}{56} = \dfrac{5}{14}\).
(b) \(P(RB) + P(BR)\) \(= \dfrac58\times\dfrac37 + \dfrac38\times\dfrac57\) \(= \dfrac{30}{56} = \dfrac{15}{28}\).
(c) \(P(BB) = \dfrac38\times\dfrac27\) \(= \dfrac{6}{56} = \dfrac{3}{28}\).
Check: \(\dfrac{10}{28} + \dfrac{15}{28} + \dfrac{3}{28}\) \(= 1\) ✓.
:::

## Conditional probability

:::key Conditional probability
\[P(A \mid B) = \frac{P(A \cap B)}{P(B)}\]
This is read "the probability of \(A\) given \(B\)". The condition \(B\) shrinks the sample space to \(B\) alone. Rearranged, it gives the multiplication rule \(P(A \cap B) = P(B) \times P(A \mid B)\), which is what a tree diagram uses.
:::

:::proof Why you multiply along a branch (the multiplication rule)
Imagine \(N\) equally likely outcomes, so that the number of outcomes in an event \(E\) is \(N \times P(E)\). Then \(A\) contains \(N\,P(A)\) outcomes.
Now look only at the outcomes in \(A\). The fraction of them that are also in \(B\) is, by the meaning of "given", \(P(B \mid A)\). So the number of outcomes in both \(A\) and \(B\) is
\[N\,P(A) \times P(B \mid A)\]
Divide by \(N\) to turn the count back into a probability:
\[P(A \cap B) = P(A) \times P(B \mid A)\]
This is the rule a tree diagram uses: the first branch carries \(P(A)\), the second carries \(P(B \mid A)\), and you multiply. If \(A\) does not affect \(B\), then \(P(B \mid A) = P(B)\) and the rule becomes \(P(A \cap B) = P(A)\,P(B)\), the test for independence. Move the sliders and step through it:

:::html
<div class="widget" data-w="proof" data-proof="tree"></div>
:::
:::

To answer a "given that" question with a tree: find the probability of the **event with the condition** (the numerator, a branch product), find the probability of the **condition itself** (the denominator, a sum of branch products), and divide.

A factory has two machines. Machine A makes 60% of the items and 3% of its items are defective; machine B makes 40% and 5% of its items are defective. The tree diagram shows the situation.

:::html
<figure class="fig"><svg viewBox="0 0 480 200" role="img" aria-label="Tree diagram. Machine A with probability 0.6 leads to defective 0.03 and good 0.97; machine B with probability 0.4 leads to defective 0.05 and good 0.95. The four joint probabilities are 0.018, 0.582, 0.020 and 0.380."><path class="ln" d="M20 100L150 50M20 100L150 150M150 50L320 25M150 50L320 75M150 150L320 125M150 150L320 175"/><circle class="fa" cx="20" cy="100" r="3"/><circle class="fa" cx="150" cy="50" r="3"/><circle class="fa" cx="150" cy="150" r="3"/><circle class="fa" cx="320" cy="25" r="3"/><circle class="fa" cx="320" cy="75" r="3"/><circle class="fa" cx="320" cy="125" r="3"/><circle class="fa" cx="320" cy="175" r="3"/><text class="tl halo tc" x="85" y="64">0.6</text><text class="tl halo tc" x="85" y="142">0.4</text><text class="tl halo tc" x="235" y="30">0.03</text><text class="tl halo tc" x="235" y="78">0.97</text><text class="tl halo tc" x="235" y="117">0.05</text><text class="tl halo tc" x="235" y="168">0.95</text><text class="tl tb" x="158" y="40">A</text><text class="tl tb" x="158" y="172">B</text><text class="tl tb" x="336" y="29">defective</text><text class="tl tb" x="336" y="79">good</text><text class="tl tb" x="336" y="129">defective</text><text class="tl tb" x="336" y="179">good</text><text class="tl ti" x="474" y="29" text-anchor="end">0.018</text><text class="tl ti" x="474" y="79" text-anchor="end">0.582</text><text class="tl ti" x="474" y="129" text-anchor="end">0.020</text><text class="tl ti" x="474" y="179" text-anchor="end">0.380</text></svg><figcaption>Tree diagram for the two machines. Multiply along each path for the joint probabilities on the right; they sum to 1.</figcaption></figure>
:::

:::eg (Real context) An item from the factory above is chosen at random. Find the probability it is defective, and the probability that it came from machine B given that it is defective.
\(P(D) = P(A \cap D) + P(B \cap D)\) \(= 0.6\times 0.03 + 0.4\times 0.05\) \(= 0.018 + 0.020 = 0.038\).
Given that the item is defective, the probability that it came from B is
\[P(B \mid D) = \frac{P(B \cap D)}{P(D)} = \frac{0.020}{0.038} = 0.526\ \text{(3 s.f.)}\]
Although B makes fewer items, a defective item is slightly more likely to come from B than from A, because B's defect rate is higher.
:::

:::eg (Exam style) The probability that it rains on a given day is 0.3. When it rains, the probability that Karim is late for work is 0.4. When it does not rain, the probability that he is late is 0.1. Find the probability that Karim is late, and the probability that it rained given that he is late. [6 marks]
Let \(R\) be rain and \(L\) be late. \(P(R \cap L) = 0.3\times 0.4 = 0.12\) [M1] and \(P(R' \cap L) = 0.7\times 0.1 = 0.07\). [M1]
\(P(L) = 0.12 + 0.07 = 0.19\). [A1]
\(P(R \mid L)\) \(= \dfrac{P(R \cap L)}{P(L)}\) \(= \dfrac{0.12}{0.19}\) [M1] [A1] \(= 0.632\ \text{(3 s.f.)}\). [A1]
:::

## Probability using counting

When outcomes are equally likely, count the favourable and total outcomes with combinations and permutations. Choose the same type of count (order or no order) for the top and the bottom.

:::eg A committee of 4 is chosen at random from 5 men and 4 women. Find the probability that (a) it contains exactly 2 women, (b) it contains at least one woman.
Total: \(\dbinom94 = 126\).
(a) \(\dfrac{\dbinom42\dbinom52}{126}\) \(= \dfrac{6\times 10}{126}\) \(= \dfrac{10}{21} = 0.476\).
(b) No woman: \(\dbinom54 = 5\) committees, so \(P = 1 - \dfrac{5}{126}\) \(= \dfrac{121}{126} = 0.960\).
:::

## Long exam questions

:::eg (Exam style) The probability that Maya's bus is late on a given day is 0.25. When the bus is late, the probability that she misses her first lesson is 0.6. When the bus is not late, the probability that she misses it is 0.1. (a) Find the probability that she misses her first lesson on a given day. (b) Given that she misses her first lesson, find the probability that the bus was late. (c) On two different days, which can be treated as independent, find the probability that she misses her first lesson on exactly one of them. (d) Show that "the bus is late" and "Maya misses her first lesson" are not independent. [11 marks]
Let \(L\) be "the bus is late" and \(M\) be "she misses her first lesson".
(a) The two paths to \(M\) are \(L \cap M\) and \(L' \cap M\):
\[P(L \cap M) = 0.25 \times 0.6 = 0.15\]
[M1]
\[P(L' \cap M) = 0.75 \times 0.1 = 0.075\]
[M1] so \(P(M) = 0.15 + 0.075 = 0.225\). [A1]
(b) Use the conditional probability formula with the condition \(M\) in the denominator:
\[P(L \mid M) = \frac{P(L \cap M)}{P(M)} = \frac{0.15}{0.225}\]
[M1 A1] which is \(\dfrac23 = 0.667\). [A1]
(c) Exactly one miss can happen in two ways: she misses on the first day only, or on the second day only. [M1] Each way has probability \(0.225 \times 0.775\), because the days are independent, so
\[P = 2 \times 0.225 \times 0.775 = 0.349\]
[M1 A1]
(d) If the events were independent, \(P(L \cap M)\) would equal \(P(L)\,P(M)\). [M1] But \(P(L)\,P(M) = 0.25 \times 0.225\) \(= 0.05625\), which is not \(0.15\). So the events are not independent. [A1]
(Check on (d): \(P(M \mid L) = 0.6\) is not equal to \(P(M) = 0.225\), so knowing the bus is late changes the chance of missing the lesson.)
:::

:::eg (Exam style) A bag contains 5 red, 4 blue and 3 green counters. Three counters are drawn at random, without replacement. Find the probability that (a) all three are the same colour, (b) exactly two are red, (c) exactly two are red, given that at least one is red. [10 marks]
There are 12 counters, so the number of ways of choosing 3 is \(\dbinom{12}{3} = 220\). [B1]
(a) The three can be all red, all blue or all green:
\[\binom53 + \binom43 + \binom33 = 10 + 4 + 1 = 15\]
[M1 A1] so the probability is \(\dfrac{15}{220} = \dfrac{3}{44}\) \(= 0.0682\). [A1]
(b) Choose 2 of the 5 red counters and 1 of the 7 others:
\[\binom52\binom71 = 10 \times 7 = 70\]
[M1 A1] so the probability is \(\dfrac{70}{220} = \dfrac{7}{22}\) \(= 0.318\). [A1]
(c) If exactly two are red then at least one is red, so the numerator is the answer to (b): \(P(\text{2 red} \mid \text{at least 1 red})\) \(= \dfrac{P(\text{2 red})}{P(\text{at least 1 red})}\). [M1] For the denominator use the complement. The number of selections with no red counter is \(\dbinom73 = 35\), so
\[P(\text{at least 1 red}) = 1 - \frac{35}{220} = \frac{37}{44}\]
[B1] The answer is
\[\frac{7/22}{37/44} = \frac{14}{37} = 0.378\]
[A1]
(Check: \(70 \div 185 = \dfrac{14}{37}\), where 185 is the number of selections with at least one red, \(220 - 35\).)
:::

:::exam What earns marks
- **Define events** at the start (\(R\) for rain, \(L\) for late), then use the notation \(P(R \mid L)\) so the method is clear.
- **For a "given that" question**, write the fraction \(\dfrac{P(A \cap B)}{P(B)}\) with both parts shown. The denominator is the probability of the condition.
- **Independent or not?** Show the product test with numbers: compare \(P(A \cap B)\) with \(P(A)P(B)\).
- **Without replacement**: change the second-stage probabilities. Check that branches leaving a point add to 1.
- Give probabilities as exact fractions or to 3 significant figures, and never above 1.
- **Reasonableness**: a probability that needs "at least one" often comes quicker as \(1 - P(\text{none})\).
:::

:::board Other boards
Edexcel IAL S1 and the UK A Level courses (AQA, OCR, Edexcel) cover the same probability rules: Venn diagrams, tree diagrams, conditional probability and independence.
:::

:::eg Spot the error: the wrong condition
A box holds 40 items. Machine X made 15 of them and machine Y made 25. Of X's items, 4% are faulty; of Y's items, 2% are faulty. A student wrote this answer to "An item is chosen at random and is faulty. Find the probability that it was made by machine X" [4 marks].

Line 1: \(P(X \cap F)\) \(= \dfrac{15}{40} \times 0.04 = 0.015\).
Line 2: \(P(X \mid F)\) \(= \dfrac{P(X \cap F)}{P(X)}\) \(= \dfrac{0.015}{0.375} = 0.04\).

**Line 1 is correct [B1].** **Line 2 scores [M0 M0 A0].** The student has divided by \(P(X)\), but the condition in "given that it is faulty" is \(F\), so the denominator must be \(P(F)\). That means the method mark for finding \(P(F)\) (the sum of both paths) is not earned, the method mark for dividing by it is not earned, and the answer mark is lost. The student scores 1 out of 4.

Correct working: \(P(Y \cap F)\) \(= \dfrac{25}{40} \times 0.02 = 0.0125\), so \(P(F) = 0.015 + 0.0125 = 0.0275\). [M1] Then
\[P(X \mid F) = \frac{0.015}{0.0275} = 0.545\]
[M1 A1]

**Check:** the student's answer, \(0.04\), is just the faulty rate of machine X from the question, which is \(P(F \mid X)\). That is a different quantity. Machine X makes fewer items but a higher share of faults, so about half of the faulty items coming from X is sensible. ✓
:::

:::try Start easy, finish at exam standard
Q: Two fair dice are rolled. Find the probability that the product of the scores is 12.
A: The pairs are (2,6), (3,4), (4,3), (6,2): 4 outcomes out of 36, so \(\dfrac19\).
Q: \(P(A) = 0.5\), \(P(B) = 0.3\) and \(P(A \cap B) = 0.1\). Find \(P(A \cup B)\) and \(P(A \mid B)\). Are \(A\) and \(B\) independent?
A: \(P(A \cup B) = 0.5 + 0.3 - 0.1 = 0.7\). \(P(A \mid B) = \dfrac{0.1}{0.3}\) \(= \dfrac13\). \(P(A)P(B) = 0.15 \ne 0.1\), so they are not independent.
Q: \(A\) and \(B\) are independent, \(P(A) = 0.6\) and \(P(A \cup B) = 0.8\). Find \(P(B)\).
A: \(0.8 = 0.6 + b - 0.6b\), so \(0.4b = 0.2\) and \(P(B) = 0.5\).
Q: A bag has 4 red and 6 green counters. Two are drawn without replacement. Find the probability that both are green, and the probability that they are different colours.
A: \(P(GG) = \dfrac6{10}\times\dfrac59\) \(= \dfrac13\). Different: \(\dfrac4{10}\times\dfrac69 + \dfrac6{10}\times\dfrac49\) \(= \dfrac{48}{90}\) \(= \dfrac8{15}\).
Q: A fair die is thrown repeatedly. Find the probability that the first six is on the 4th throw.
A: \(\left(\dfrac56\right)^3\times\dfrac16\) \(= \dfrac{125}{1296} = 0.0965\).
Q: In a group of 60 people, 35 swim, 28 cycle and 10 do neither. Find the number who do both, and \(P(\text{swim} \mid \text{cycle})\).
A: At least one: \(60 - 10 = 50 = 35 + 28 - x\), so \(x = 13\). \(P = \dfrac{13}{28} = 0.464\).
Q: The probability of rain is 0.2. If it rains, the probability that a football match is cancelled is 0.7; if it does not rain, 0.1. Find \(P(\text{cancelled})\) and \(P(\text{rain} \mid \text{cancelled})\).
A: \(P(C) = 0.2\times 0.7 + 0.8\times 0.1\) \(= 0.14 + 0.08 = 0.22\). \(P(R \mid C) = \dfrac{0.14}{0.22}\) \(= 0.636\).
Q: Three people are chosen at random from 7 boys and 5 girls. Find the probability that all are girls, and the probability that at least one is a boy.
A: \(\dfrac{\dbinom53}{\dbinom{12}{3}}\) \(= \dfrac{10}{220} = \dfrac1{22}\) \(= 0.0455\). At least one boy: \(1 - \dfrac1{22} = \dfrac{21}{22}\) \(= 0.955\).
Q: (Exam style) A bag contains 6 red and 4 blue counters. Three counters are drawn without replacement. Find the probability that all three are the same colour, and the probability that they are red given that all three are the same colour. [5 marks]
A: \(P(RRR)\) \(= \dfrac6{10}\times\dfrac59\times\dfrac48\) \(= \dfrac{120}{720}\) and \(P(BBB)\) \(= \dfrac4{10}\times\dfrac39\times\dfrac28\) \(= \dfrac{24}{720}\). [M1 A1] \(P(\text{same}) = \dfrac{144}{720}\) \(= 0.2\). [A1] \(P(\text{red} \mid \text{same})\) \(= \dfrac{120/720}{144/720}\) [M1] \(= \dfrac{5}{6} = 0.833\). [A1]
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ \(P(A) = 0.35\), \(P(B) = 0.45\) and \(P(A \cap B) = 0.15\). Find (a) \(P(A \cup B)\), (b) \(P(A \mid B)\).
A: (a) \(P(A \cup B) = 0.35 + 0.45 - 0.15\) \(= 0.65\). [M1 A1] (b) \(P(A \mid B) = \dfrac{0.15}{0.45}\) \(= \dfrac13\). [B1]
Q: [3 marks] ★ Two fair dice are rolled. Find the probability that the two scores differ by exactly 2.
A: There are 36 equally likely outcomes. [B1] The pairs are (1,3), (2,4), (3,5), (4,6) and the same four reversed, which is 8 outcomes. [M1] The probability is \(\dfrac{8}{36} = \dfrac29\). [A1]
Q: [4 marks] ★★ In a group of 60 people, 32 read a newspaper (\(N\)), 24 listen to the radio (\(R\)) and 9 do neither. Find the number who do both, and \(P(N \mid R)\).
A: At least one: \(60 - 9 = 51\). [M1] So \(51 = 32 + 24 - x\) [M1] and \(x = 5\) people do both. [A1] Given \(R\), 5 of the 24 radio listeners read a newspaper: \(P(N \mid R) = \dfrac{5}{24} = 0.208\). [A1]
Q: [5 marks] ★★ A bag has 7 white and 3 black counters. Two are drawn without replacement. Find the probability that (a) they are different colours, (b) the second counter is white.
A: (a) \(P(WB) = \dfrac{7}{10} \times \dfrac39\) \(= \dfrac{21}{90}\) and \(P(BW) = \dfrac{3}{10} \times \dfrac79\) \(= \dfrac{21}{90}\). [M1] Add the two orders: [M1] \(\dfrac{42}{90} = \dfrac{7}{15}\). [A1] (b) The second is white after a white first, or after a black first:
\[\frac{7}{10} \times \frac69 + \frac{3}{10} \times \frac79 = \frac{42}{90} + \frac{21}{90}\]
[M1] \(= \dfrac{63}{90} = \dfrac{7}{10}\). [A1]
Q: [5 marks] ★★ \(A\) and \(B\) are independent events with \(P(A) = 0.3\) and \(P(A \cup B) = 0.65\). Find \(P(B)\) and \(P(A' \cap B')\).
A: Independence gives \(P(A \cap B) = 0.3\,P(B)\). [M1] Then
\[0.65 = 0.3 + P(B) - 0.3\,P(B)\]
[M1] so \(0.35 = 0.7\,P(B)\) and \(P(B) = 0.5\). [A1] The event \(A' \cap B'\) is "neither", so \(P(A' \cap B') = 1 - 0.65\) [M1] \(= 0.35\). [A1]
Q: [5 marks] ★★ In a town, 2% of people have a certain condition. A test gives a positive result for 95% of people who have it and for 8% of people who do not. A person is chosen at random. Find the probability that (a) the test is positive, (b) the person has the condition, given that the test is positive.
A: (a) Positive and has it: \(0.02 \times 0.95 = 0.019\). Positive and does not have it: \(0.98 \times 0.08 = 0.0784\). [M1] The sum is \(0.0974\). [A1] (b)
\[P(\text{condition} \mid \text{positive}) = \frac{0.019}{0.0974}\]
[M1 A1] which is \(0.195\) to 3 s.f. [A1] (Most positive results come from the large group without the condition, so the answer is small.)
Q: [4 marks] ★★ (#math.s1.perms) The letters of the word BANANA are arranged in a random order. Find the probability that the two N's are next to each other.
A: The number of arrangements is \(\dfrac{6!}{3!\,2!} = 60\). [B1] Glue the N's into a block: the block with B, A, A, A makes 5 items with the A repeated three times, so there are \(\dfrac{5!}{3!} = 20\) arrangements. [M1 A1] The probability is \(\dfrac{20}{60} = \dfrac13\). [A1]
Q: [9 marks] (#math.p1.quadratics) ★★★ A bag contains 4 red counters and \(n\) blue counters. Two counters are drawn at random without replacement. The probability that both are red is \(\dfrac16\). (a) Show that \(n^2 + 7n - 60 = 0\) and find \(n\). (b) Find the probability that the two counters are different colours. (c) Given that the two counters are different colours, find the probability that the first one drawn was red.
H: There are \(4 + n\) counters. Write \(P(RR)\) as a product of two fractions in terms of \(n\) and put it equal to \(\dfrac16\).
H: Multiply out to get \((n + 4)(n + 3) = 72\). Expand, rearrange, and factorise. Reject the negative root.
H: For (c), \(P(\text{first red} \mid \text{different})\) \(= \dfrac{P(RB)}{P(RB) + P(BR)}\).
A: (a) \(P(RR)\) \(= \dfrac{4}{n + 4} \times \dfrac{3}{n + 3}\) \(= \dfrac{12}{(n + 4)(n + 3)}\). [M1] Setting this equal to \(\dfrac16\) gives \((n + 4)(n + 3) = 72\). [A1] Expanding, \(n^2 + 7n + 12 = 72\), so \(n^2 + 7n - 60 = 0\). [M1] Then \((n + 12)(n - 5) = 0\), so \(n = 5\) [A1] (reject \(n = -12\), because \(n\) is a count). [B1] (b) With 9 counters, \(P(RB) = \dfrac49 \times \dfrac58\) \(= \dfrac{20}{72}\), and \(P(BR) = \dfrac59 \times \dfrac48\) \(= \dfrac{20}{72}\). [M1] So \(P(\text{different}) = \dfrac{40}{72}\) \(= \dfrac59\). [A1] (c) \(\dfrac{20/72}{40/72}\) [M1] \(= \dfrac12\). [A1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ In a game show there is a car behind one of three doors, chosen at random. A contestant picks door 1. The host, who knows where the car is, then opens one of the other two doors to show no car. If the car is behind door 1 he chooses at random between doors 2 and 3. Otherwise he must open the door with no car that is not door 1. The host opens door 3. Find the probability that the car is behind door 2, so decide whether the contestant should switch.
H: Let \(C_1, C_2, C_3\) be "car behind door 1, 2, 3" and \(H_3\) be "host opens door 3". You want \(P(C_2 \mid H_3)\).
H: Find \(P(H_3 \mid C_1)\), \(P(H_3 \mid C_2)\) and \(P(H_3 \mid C_3)\) from the host's rule. One of them is 0.
H: \(P(H_3)\) is the sum of three paths, each of the form \(P(C_i) \times P(H_3 \mid C_i)\).
A: Each \(P(C_i) = \dfrac13\). [B1] If the car is behind door 1, the host picks door 3 half the time: \(P(H_3 \mid C_1) = \dfrac12\). [M1] If the car is behind door 2, he must open door 3: \(P(H_3 \mid C_2) = 1\). If the car is behind door 3, he cannot open it: \(P(H_3 \mid C_3) = 0\). [B1 B1] Then
\[P(H_3) = \frac13 \times \frac12 + \frac13 \times 1 + \frac13 \times 0 = \frac12\]
[M1] and
\[P(C_2 \mid H_3) = \frac{\frac13 \times 1}{\frac12} = \frac23\]
[M1 A1] The car is behind door 2 with probability \(\dfrac23\), and behind door 1 with probability \(\dfrac13\), so the contestant should switch.
Q: [4 marks] ★★★ A group of 5 people are chosen at random. Assume that each person is equally likely to have a birthday on any of 365 days, independently of the others. Find the probability that (a) all 5 birthdays are different, (b) at least two of the 5 share a birthday.
H: Build the probability person by person: the second person must avoid the first person's birthday, the third must avoid the first two, and so on.
H: "At least two share" is the complement of "all different".
A: (a) The second person avoids one date, the third avoids two, and so on: [M1]
\[\frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \frac{362}{365} \times \frac{361}{365} = 0.973\]
[A1] (b) \(P(\text{at least two share})\) \(= 1 - 0.9729\) [M1] \(= 0.0271\). [A1]
:::

:::quiz
? \(A\) and \(B\) are mutually exclusive with \(P(A) = 0.3\) and \(P(B) = 0.4\). What is \(P(A \cup B)\)?
- \(0.12\)
+ \(0.7\)
- \(0.58\)
- \(0.1\)
> Mutually exclusive means \(P(A \cap B) = 0\), so the probabilities add. \(0.12\) is the product, used for independent events.
? Which condition shows that \(A\) and \(B\) are independent?
- \(P(A \cap B) = 0\)
- \(P(A \cup B) = P(A) + P(B)\)
+ \(P(A \cap B) = P(A)\,P(B)\)
- \(P(A) = P(B)\)
> Independence is the product rule. The first two describe mutually exclusive events, which cannot be independent unless one has probability 0.
? What is \(P(A \mid B)\)?
- \(\dfrac{P(A \cap B)}{P(A)}\)
+ \(\dfrac{P(A \cap B)}{P(B)}\)
- \(P(A)\,P(B)\)
- \(P(A \cup B) - P(B)\)
> The condition goes in the denominator: divide the overlap by the probability of the event you are given.
? Two cards are drawn without replacement from a pack. Why do the second-stage probabilities change?
- Because the cards are shuffled again.
+ Because the first card has been removed, so the numbers left are different.
- They do not change.
- Because the events are mutually exclusive.
> Without replacement, the first draw changes what is left, so the second draw depends on the first.
? A bag has 3 red and 2 blue counters. Two are drawn without replacement. What is \(P(\text{both red})\)?
- \(\dfrac35\times\dfrac35 = \dfrac9{25}\)
+ \(\dfrac35\times\dfrac24 = \dfrac3{10}\)
- \(\dfrac35\times\dfrac25 = \dfrac6{25}\)
- \(\dfrac{3}{5}\)
> After one red is removed, 2 red remain among 4 counters, so \(\dfrac35\times\dfrac24 = \dfrac3{10}\).
:::

:::checklist What you can now do
- [ ] I can list the sample space for two dice or coins and find a probability by counting equally likely outcomes.
- [ ] I can use \(P(A \cup B)\) \(= P(A) + P(B) - P(A \cap B)\) and the complement \(P(A') = 1 - P(A)\).
- [ ] I can fill in a Venn diagram, starting from the overlap, and read probabilities from it.
- [ ] I can tell mutually exclusive events from independent ones, and test independence with \(P(A \cap B) = P(A)\,P(B)\).
- [ ] I can draw a tree diagram, with and without replacement, and multiply along the branches and add between them.
- [ ] I can find a conditional probability \(P(A \mid B)\) from a tree, a Venn diagram or the formula.
- [ ] I can find a probability by counting selections or arrangements with permutations and combinations.
:::

:::recap
- Equally likely outcomes: \(P(A) = \dfrac{n(A)}{n(S)}\); \(P(A') = 1 - P(A)\).
- \(P(A \cup B)\) \(= P(A) + P(B) - P(A \cap B)\). Mutually exclusive: \(P(A \cap B) = 0\). Independent: \(P(A \cap B) = P(A)P(B)\).
- Mutually exclusive events with non-zero probabilities are not independent.
- Tree diagrams: multiply along branches, add between paths; branches from one point sum to 1; without replacement, update the numbers.
- \(P(A \mid B)\) \(= \dfrac{P(A \cap B)}{P(B)}\): restrict to \(B\), then find the fraction in \(A\).
- Counting probabilities: favourable \(\div\) total, using combinations when order does not matter.
:::

:::links
- watch: [Conditional probability with tree diagrams](https://www.examsolutions.net/tutorials/conditional-probability-tree-diagrams/) · ExamSolutions · P(A given B) from a tree
- watch: [Exam questions: tree diagrams](https://www.examsolutions.net/tutorials/exam-questions-tree-diagrams/) · ExamSolutions · exam-style questions solved on video
- practise: [CAIE S1 further probability exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/probability/further-probability/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Basic probability](https://seeing-theory.brown.edu/basic-probability/index.html) · Seeing Theory · simulate coins and dice and watch the long run
- explore: [Compound probability](https://seeing-theory.brown.edu/compound-probability/index.html) · Seeing Theory · Venn diagrams and conditional probability you can play with

Links checked 3 October 2026.
:::
Next: [Discrete random variables: binomial and geometric](#math.s1.drv).
