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
(c) Use the complement: no die shows a 6 in \(5\times 5 = 25\) outcomes, so \(P = 1 - \dfrac{25}{36} = \dfrac{11}{36}\).
:::

## Combining events: addition and Venn diagrams

:::key Probability of "A or B"
\[P(A \cup B) = P(A) + P(B) - P(A \cap B)\]
\(A \cup B\) means "\(A\) or \(B\) or both"; \(A \cap B\) means "\(A\) and \(B\)". Subtract the overlap so it is not counted twice.
:::

A **Venn diagram** shows the sample space as a rectangle and each event as a region. Fill in the overlap first (the intersection), then work outwards.

:::eg Of 40 students, 25 like tea (\(T\)), 18 like coffee (\(C\)) and 8 like both. Find the number who like neither, \(P(T \cup C)\), \(P(T \mid C)\), and say whether \(T\) and \(C\) are independent.
Start with the overlap: 8 like both. Tea only: \(25 - 8 = 17\). Coffee only: \(18 - 8 = 10\). At least one: \(17 + 8 + 10 = 35\), so neither: \(40 - 35 = 5\).
\(P(T \cup C) = \dfrac{35}{40} = \dfrac78\).
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

For independent repeated trials, multiply: the probability of tossing a fair coin 3 times and getting at least one head is \(1 - \left(\tfrac12\right)^3 = \tfrac78\), and the probability that a fair die first shows a six on the third throw is \(\left(\tfrac56\right)^2\times\tfrac16 = \tfrac{25}{216} = 0.116\).

## Tree diagrams

A **tree diagram** shows the stages of an experiment as branches. Each branch carries a probability; **multiply along** a path to find the probability of that sequence, and **add** the results of the paths that make up an event. The probabilities leaving any one point sum to 1.

When items are drawn **without replacement**, the probabilities on the second stage change, because the numbers in the bag have changed.

:::eg A bag contains 5 red and 3 blue counters. Two are drawn without replacement. Find the probability of (a) two red, (b) one of each colour, (c) two blue.
First draw: \(P(R) = \dfrac58\), \(P(B) = \dfrac38\). If the first is red, 4 red and 3 blue remain (7 counters): \(P(R) = \dfrac47\), \(P(B) = \dfrac37\). If the first is blue, 5 red and 2 blue remain: \(P(R) = \dfrac57\), \(P(B) = \dfrac27\).
(a) \(P(RR) = \dfrac58\times\dfrac47 = \dfrac{20}{56} = \dfrac{5}{14}\).
(b) \(P(RB) + P(BR) = \dfrac58\times\dfrac37 + \dfrac38\times\dfrac57 = \dfrac{30}{56} = \dfrac{15}{28}\).
(c) \(P(BB) = \dfrac38\times\dfrac27 = \dfrac{6}{56} = \dfrac{3}{28}\).
Check: \(\dfrac{10}{28} + \dfrac{15}{28} + \dfrac{3}{28} = 1\) ✓.
:::

## Conditional probability

:::key Conditional probability
\[P(A \mid B) = \frac{P(A \cap B)}{P(B)}\]
This is read "the probability of \(A\) given \(B\)". The condition \(B\) shrinks the sample space to \(B\) alone. Rearranged, it gives the multiplication rule \(P(A \cap B) = P(B) \times P(A \mid B)\), which is what a tree diagram uses.
:::

To answer a "given that" question with a tree: find the probability of the **event with the condition** (the numerator, a branch product), find the probability of the **condition itself** (the denominator, a sum of branch products), and divide.

A factory has two machines. Machine A makes 60% of the items and 3% of its items are defective; machine B makes 40% and 5% of its items are defective. The tree diagram shows the situation.

:::html
<figure class="fig"><svg viewBox="0 0 480 200" role="img" aria-label="Tree diagram. Machine A with probability 0.6 leads to defective 0.03 and good 0.97; machine B with probability 0.4 leads to defective 0.05 and good 0.95. The four joint probabilities are 0.018, 0.582, 0.020 and 0.380."><path class="ln" d="M20 100L150 50M20 100L150 150M150 50L320 25M150 50L320 75M150 150L320 125M150 150L320 175"/><circle class="fa" cx="20" cy="100" r="3"/><circle class="fa" cx="150" cy="50" r="3"/><circle class="fa" cx="150" cy="150" r="3"/><circle class="fa" cx="320" cy="25" r="3"/><circle class="fa" cx="320" cy="75" r="3"/><circle class="fa" cx="320" cy="125" r="3"/><circle class="fa" cx="320" cy="175" r="3"/><text class="tl halo tc" x="85" y="64">0.6</text><text class="tl halo tc" x="85" y="142">0.4</text><text class="tl halo tc" x="235" y="30">0.03</text><text class="tl halo tc" x="235" y="78">0.97</text><text class="tl halo tc" x="235" y="117">0.05</text><text class="tl halo tc" x="235" y="168">0.95</text><text class="tl tb" x="158" y="40">A</text><text class="tl tb" x="158" y="172">B</text><text class="tl tb" x="336" y="29">defective</text><text class="tl tb" x="336" y="79">good</text><text class="tl tb" x="336" y="129">defective</text><text class="tl tb" x="336" y="179">good</text><text class="tl ti" x="474" y="29" text-anchor="end">0.018</text><text class="tl ti" x="474" y="79" text-anchor="end">0.582</text><text class="tl ti" x="474" y="129" text-anchor="end">0.020</text><text class="tl ti" x="474" y="179" text-anchor="end">0.380</text></svg><figcaption>Tree diagram for the two machines. Multiply along each path for the joint probabilities on the right; they sum to 1.</figcaption></figure>
:::

:::eg (Real context) An item from the factory above is chosen at random. Find the probability it is defective, and the probability that it came from machine B given that it is defective.
\(P(D) = P(A \cap D) + P(B \cap D) = 0.6\times 0.03 + 0.4\times 0.05 = 0.018 + 0.020 = 0.038\).
Given that the item is defective, the probability that it came from B is
\[P(B \mid D) = \frac{P(B \cap D)}{P(D)} = \frac{0.020}{0.038} = 0.526\ \text{(3 s.f.)}\]
Although B makes fewer items, a defective item is slightly more likely to come from B than from A, because B's defect rate is higher.
:::

:::eg (Exam style) The probability that it rains on a given day is 0.3. When it rains, the probability that Karim is late for work is 0.4. When it does not rain, the probability that he is late is 0.1. Find the probability that Karim is late, and the probability that it rained given that he is late. [6 marks]
Let \(R\) be rain and \(L\) be late. \(P(R \cap L) = 0.3\times 0.4 = 0.12\) [M1] and \(P(R' \cap L) = 0.7\times 0.1 = 0.07\). [M1]
\(P(L) = 0.12 + 0.07 = 0.19\). [A1]
\(P(R \mid L) = \dfrac{P(R \cap L)}{P(L)} = \dfrac{0.12}{0.19} [\text{M1 A1}] = 0.632\ \text{(3 s.f.)}\). [A1]
:::

## Probability using counting

When outcomes are equally likely, count the favourable and total outcomes with combinations and permutations. Choose the same type of count (order or no order) for the top and the bottom.

:::eg A committee of 4 is chosen at random from 5 men and 4 women. Find the probability that (a) it contains exactly 2 women, (b) it contains at least one woman.
Total: \(\dbinom94 = 126\).
(a) \(\dfrac{\dbinom42\dbinom52}{126} = \dfrac{6\times 10}{126} = \dfrac{10}{21} = 0.476\).
(b) No woman: \(\dbinom54 = 5\) committees, so \(P = 1 - \dfrac{5}{126} = \dfrac{121}{126} = 0.960\).
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

:::try Start easy, finish at exam standard
Q: Two fair dice are rolled. Find the probability that the product of the scores is 12.
A: The pairs are (2,6), (3,4), (4,3), (6,2): 4 outcomes out of 36, so \(\dfrac19\).
Q: \(P(A) = 0.5\), \(P(B) = 0.3\) and \(P(A \cap B) = 0.1\). Find \(P(A \cup B)\) and \(P(A \mid B)\). Are \(A\) and \(B\) independent?
A: \(P(A \cup B) = 0.5 + 0.3 - 0.1 = 0.7\). \(P(A \mid B) = \dfrac{0.1}{0.3} = \dfrac13\). \(P(A)P(B) = 0.15 \ne 0.1\), so they are not independent.
Q: \(A\) and \(B\) are independent, \(P(A) = 0.6\) and \(P(A \cup B) = 0.8\). Find \(P(B)\).
A: \(0.8 = 0.6 + b - 0.6b\), so \(0.4b = 0.2\) and \(P(B) = 0.5\).
Q: A bag has 4 red and 6 green counters. Two are drawn without replacement. Find the probability that both are green, and the probability that they are different colours.
A: \(P(GG) = \dfrac6{10}\times\dfrac59 = \dfrac13\). Different: \(\dfrac4{10}\times\dfrac69 + \dfrac6{10}\times\dfrac49 = \dfrac{48}{90} = \dfrac8{15}\).
Q: A fair die is thrown repeatedly. Find the probability that the first six is on the 4th throw.
A: \(\left(\dfrac56\right)^3\times\dfrac16 = \dfrac{125}{1296} = 0.0965\).
Q: In a group of 60 people, 35 swim, 28 cycle and 10 do neither. Find the number who do both, and \(P(\text{swim} \mid \text{cycle})\).
A: At least one: \(60 - 10 = 50 = 35 + 28 - x\), so \(x = 13\). \(P = \dfrac{13}{28} = 0.464\).
Q: The probability of rain is 0.2. If it rains, the probability that a football match is cancelled is 0.7; if it does not rain, 0.1. Find \(P(\text{cancelled})\) and \(P(\text{rain} \mid \text{cancelled})\).
A: \(P(C) = 0.2\times 0.7 + 0.8\times 0.1 = 0.14 + 0.08 = 0.22\). \(P(R \mid C) = \dfrac{0.14}{0.22} = 0.636\).
Q: Three people are chosen at random from 7 boys and 5 girls. Find the probability that all are girls, and the probability that at least one is a boy.
A: \(\dfrac{\dbinom53}{\dbinom{12}{3}} = \dfrac{10}{220} = \dfrac1{22} = 0.0455\). At least one boy: \(1 - \dfrac1{22} = \dfrac{21}{22} = 0.955\).
Q: (Exam style) A bag contains 6 red and 4 blue counters. Three counters are drawn without replacement. Find the probability that all three are the same colour, and the probability that they are red given that all three are the same colour. [5 marks]
A: \(P(RRR) = \dfrac6{10}\times\dfrac59\times\dfrac48 = \dfrac{120}{720}\) and \(P(BBB) = \dfrac4{10}\times\dfrac39\times\dfrac28 = \dfrac{24}{720}\). [M1 A1] \(P(\text{same}) = \dfrac{144}{720} = 0.2\). [A1] \(P(\text{red} \mid \text{same}) = \dfrac{120/720}{144/720} [\text{M1}] = \dfrac{5}{6} = 0.833\). [A1]
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

:::recap
- Equally likely outcomes: \(P(A) = \dfrac{n(A)}{n(S)}\); \(P(A') = 1 - P(A)\).
- \(P(A \cup B) = P(A) + P(B) - P(A \cap B)\). Mutually exclusive: \(P(A \cap B) = 0\). Independent: \(P(A \cap B) = P(A)P(B)\).
- Mutually exclusive events with non-zero probabilities are not independent.
- Tree diagrams: multiply along branches, add between paths; branches from one point sum to 1; without replacement, update the numbers.
- \(P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}\): restrict to \(B\), then find the fraction in \(A\).
- Counting probabilities: favourable \(\div\) total, using combinations when order does not matter.
:::

:::note Learn more online
- **Watch:** [Conditional probability with tree diagrams](https://www.examsolutions.net/tutorials/conditional-probability-tree-diagrams/) · ExamSolutions · P(A given B) from a tree
- **Watch:** [Exam questions: tree diagrams](https://www.examsolutions.net/tutorials/exam-questions-tree-diagrams/) · ExamSolutions · exam-style questions solved on video
- **Practise:** [CAIE S1 further probability exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/probability/further-probability/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Basic probability](https://seeing-theory.brown.edu/basic-probability/index.html) · Seeing Theory · simulate coins and dice and watch the long run
- **Explore:** [Compound probability](https://seeing-theory.brown.edu/compound-probability/index.html) · Seeing Theory · Venn diagrams and conditional probability you can play with

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Discrete random variables: binomial and geometric](#math.s1.drv).
