@chapter math.s1.perms
@title Permutations and combinations
@level a2
@paper CAIE P5 (check your specification for other boards)
@time 7–9 hours
@summary Counting without listing: the multiplication principle, factorials, permutations (order matters) and combinations (order does not), arrangements with repeated items, arrangements with restrictions such as "together", "apart" and "at the ends", selections with conditions such as "at least one", and people seated in rows.

:::why
How many different four-digit PIN codes are there? How many ways can a team of five be picked from twelve people? How many arrangements of the letters in a word? Counting by writing out every case soon becomes impossible, but a few rules turn any of these into a short calculation. These counting rules are also the engine behind probability: when all outcomes are equally likely, a probability is a count divided by a count.
:::

**Before you start**, you need confident arithmetic with fractions and powers from [Numbers from scratch](#math.f.numbers), and the idea of a factorial from the binomial coefficients in [Series](#math.p1.series).

## The multiplication principle

:::key Multiplication principle
If one task can be done in \(m\) ways and, for each of these, a second task can be done in \(n\) ways, then the two tasks together can be done in \(m \times n\) ways. This extends to any number of tasks. If the tasks are **alternatives** (either one or the other, not both), **add** the counts.
:::

Think of filling slots from left to right: write a box for each place, put the number of choices in each box, and multiply. Handle any restriction **first**, in the slot it affects.

:::eg A café offers 4 starters, 6 mains and 3 desserts. How many different three-course meals are there? How many if a diner skips either the starter or the dessert but not both (still choosing a main)?
Three courses: \(4 \times 6 \times 3 = 72\).
Skipping the starter: \(6 \times 3 = 18\) meals; skipping the dessert: \(4 \times 6 = 24\) meals. These are alternatives, so add: \(18 + 24 = 42\).
:::

## Factorials, permutations and combinations

:::def Factorial
\(n!\) (read "\(n\) factorial") is the product \(n \times (n-1) \times \cdots \times 2 \times 1\), with \(0! = 1\). It is the number of ways to arrange \(n\) different objects in a line. For example, \(5! = 120\).
:::

:::def Permutation and combination
A **permutation** is an arrangement in which the **order matters**; a **combination** is a selection in which the **order does not matter**. The number of ways to arrange \(r\) objects chosen from \(n\) different objects, and the number of ways to select \(r\) from \(n\), are
\[{}^{n}P_r = \frac{n!}{(n-r)!} \qquad \binom{n}{r} = {}^{n}C_r = \frac{n!}{r!\,(n-r)!}\]
Each selection of \(r\) objects can be arranged in \(r!\) orders, so \({}^{n}P_r = r! \times \binom{n}{r}\).
:::

Ask yourself: if I swap two of the chosen things, is it a different outcome? A president and a secretary (yes, order matters: permutation). A committee of two (no: combination). The formula for \(\binom{n}{r}\) is on MF19; the permutation formula is not, but you can always build it from the slots: \({}^{n}P_r\) is \(r\) factors starting from \(n\) and counting down.

:::eg In a race with 10 runners, how many ways can the gold, silver and bronze medals be awarded? How many ways can a squad of 4 be chosen from 7 players? In how many of those squads is Priya included?
Medals: order matters, so \({}^{10}P_3 = 10 \times 9 \times 8 = 720\).
Squad: order does not matter, so \(\binom{7}{4} = \dfrac{7!}{4!\,3!} = 35\).
Priya included: she fills one place, and 3 more are chosen from the other 6: \(\binom{6}{3} = 20\).
:::

## Arrangements with repeated items

If some of the \(n\) items are identical, many of the \(n!\) arrangements look the same. Divide by the number of ways of rearranging each group of identical items.

:::key Arrangements with repeats
The number of arrangements of \(n\) items, of which \(p\) are identical of one kind, \(q\) are identical of another kind, and so on, is
\[\frac{n!}{p!\,q!\cdots}\]
:::

:::eg Find the number of arrangements of the letters of (a) BANANA, (b) MISSISSIPPI. For STATISTICS, find the number of arrangements in which the three S's are together.
(a) BANANA has 6 letters: B once, A three times, N twice. \(\dfrac{6!}{3!\,2!} = \dfrac{720}{12} = 60\).
(b) MISSISSIPPI has 11 letters: M once, I four times, S four times, P twice. \(\dfrac{11!}{4!\,4!\,2!} = \dfrac{39\,916\,800}{1152} = 34\,650\).
STATISTICS has 10 letters: S three times, T three times, I twice, A once, C once. Treat SSS as a single block. There are then 8 items: the block, T, T, T, I, I, A, C, with T three times and I twice. The number of arrangements is \(\dfrac{8!}{3!\,2!} = \dfrac{40\,320}{12} = 3360\).
:::

## Restrictions: together, apart, at the ends

:::key Techniques for restrictions
- **Together**: glue the items into one block, arrange the block with the others, then multiply by the number of arrangements **inside** the block.
- **Not together (apart)**: count **all** arrangements and subtract those with the items together.
- **Fixed positions** (at the ends, first digit nonzero, last digit even): fill the restricted slots first.
:::

:::eg Eight people stand in a row. Find the number of arrangements (a) with no restriction, (b) in which Anna and Ben are next to each other, (c) in which Anna and Ben are not next to each other, (d) in which Anna and Ben are at the two ends.
(a) \(8! = 40\,320\).
(b) Glue Anna and Ben into one block. There are 7 items to arrange: \(7!\) ways. Inside the block they can be in 2 orders. Total \(2 \times 5040 = 10\,080\).
(c) Not next to each other: \(40\,320 - 10\,080 = 30\,240\).
(d) Anna and Ben take the two end places in 2 ways, and the other 6 people fill the middle in \(6! = 720\) ways. Total \(2 \times 720 = 1440\).
:::

:::eg Four-digit numbers are formed from the digits 1, 2, 3, 4, 5, 6, 7, each used at most once. How many numbers are there, and how many are (a) even, (b) odd, (c) greater than 5000?
Total: \({}^{7}P_4 = 7\times 6\times 5\times 4 = 840\).
(a) Even: the last digit is 2, 4 or 6, so 3 choices. Fill that slot first, then the other three slots in \(6\times 5\times 4 = 120\) ways. Total \(3 \times 120 = 360\).
(b) Odd: the last digit is 1, 3, 5 or 7, so \(4 \times 120 = 480\) (check: \(360 + 480 = 840\)).
(c) Greater than 5000: the first digit is 5, 6 or 7, so \(3 \times 6\times 5\times 4 = 360\).
:::

If a number may start with 0 (digits 0 to 9), be careful: the first digit has only 9 choices, not 10. For example, four-digit numbers with no repeated digit: \(9 \times 9 \times 8 \times 7 = 4536\).

## Selections with conditions

For selections, use \(\binom{n}{r}\) for each group separately and multiply. For "at least" conditions, add the cases, or subtract the complement from the total, whichever has fewer cases.

:::eg A team of 5 is chosen from 6 boys and 4 girls. Find the number of teams (a) with no restriction, (b) with exactly 2 girls, (c) with at least one girl, (d) that include Zara, one of the girls.
(a) \(\dbinom{10}{5} = 252\).
(b) 2 girls from 4 and 3 boys from 6: \(\dbinom42\dbinom63 = 6\times 20 = 120\).
(c) The only team with no girls is the 5 boys chosen from 6: \(\dbinom65 = 6\). So at least one girl: \(252 - 6 = 246\).
(d) Zara is in; choose the other 4 from the remaining 9 people: \(\dbinom94 = 126\).
:::

:::eg (Exam style) A committee of 5 is to be chosen from 7 men and 4 women. Find the number of possible committees in which there are at least 2 women. [5 marks]
Total committees: \(\dbinom{11}{5} = 462\). [B1]
"At least 2 women" is easiest as the total minus the cases with 0 or 1 woman. [M1]
0 women: \(\dbinom75 = 21\). [B1]
1 woman: \(\dbinom41\dbinom74 = 4\times 35 = 140\). [B1]
Number with at least 2 women \(= 462 - 21 - 140 = 301\). [A1]
Check by adding the cases: 2 women \(\dbinom42\dbinom73 = 6\times 35 = 210\); 3 women \(\dbinom43\dbinom72 = 4\times 21 = 84\); 4 women \(\dbinom44\dbinom71 = 7\); \(210 + 84 + 7 = 301\) ✓.
:::

## People in rows

Seating people in more than one row is the same as arranging them in a line with the rows as consecutive blocks of places. Count the ways to place the restricted people first.

:::eg Eight students are seated in two rows of four, a front row and a back row, for a photograph. In how many ways can they be seated? In how many ways are Anna and Ben both in the front row?
Total: the 8 seats are all different, so \(8! = 40\,320\).
Anna and Ben in the front row: Anna has 4 seats, then Ben has 3, giving \({}^{4}P_2 = 12\) ways. The other 6 students fill the remaining 6 seats in \(6! = 720\) ways. Total \(12 \times 720 = 8640\).
:::

:::eg (Real context) A security code uses 3 different letters chosen from A to H, followed by 2 different digits chosen from 1 to 9. How many codes are possible? How many codes contain the letter A?
Letters: \({}^{8}P_3 = 8\times 7\times 6 = 336\). Digits: \({}^{9}P_2 = 9\times 8 = 72\). Total \(336\times 72 = 24\,192\).
Codes containing the letter A: choose the position of A in the three letter slots (3 ways), then fill the other two letter slots from the remaining 7 letters in \({}^{7}P_2 = 42\) ways. So there are \(3\times 42 = 126\) letter arrangements containing A, and \(126\times 72 = 9072\) codes.
:::

:::exam What earns marks
- **State what is being counted** and whether order matters ("order matters, so permutations"). The method mark follows the model, not the arithmetic.
- **For "together"**, show the block and the inside arrangements; **for "apart"**, show the total and the subtraction.
- **"At least"** questions: choose the shorter route (cases, or total minus complement) and show the cases.
- Write out the calculation (\({}^{10}P_3 = 10\times 9\times 8\)) as well as the answer, and check for sensible size (the answer should be a whole number less than the total).
- Arrangements in a circle are not examined in this course.
:::

:::board Other boards
The UK A Level courses (AQA, OCR, Edexcel) use \(\binom{n}{r}\) in the binomial distribution and in probability. Arrangements with restrictions are a Cambridge Paper 5 topic, and Edexcel IAL S1 does not include them. If you are not taking Cambridge, check your specification before spending long on the harder sections.
:::

:::try Start easy, finish at exam standard
Q: Evaluate \(\dfrac{6!}{4!}\) and \(\dbinom94\).
A: \(\dfrac{6!}{4!} = 6\times 5 = 30\). \(\dbinom94 = \dfrac{9\times 8\times 7\times 6}{4\times 3\times 2\times 1} = 126\).
Q: How many arrangements are there of the letters of LETTER?
A: 6 letters with E twice and T twice: \(\dfrac{6!}{2!\,2!} = 180\).
Q: How many arrangements are there of the letters of MISSISSIPPI?
A: \(\dfrac{11!}{4!\,4!\,2!} = 34\,650\).
Q: Three-digit numbers are formed from the digits 1 to 9, no digit repeated. How many are even?
A: The last digit has 4 choices (2, 4, 6, 8); the first two slots then have \(8\times 7 = 56\) ways. \(4\times 56 = 224\).
Q: Five different books are placed on a shelf. In how many arrangements are two particular maths books next to each other?
A: Glue them: 4 items, so \(4! = 24\) arrangements, and 2 orders inside the block. Total \(48\).
Q: In how many ways can 3 people be chosen from 8 for a committee, and in how many ways for the posts of chair, secretary and treasurer?
A: Committee: \(\dbinom83 = 56\). Posts: \({}^{8}P_3 = 336\) (which is \(3!\times 56\)).
Q: A committee of 5 is chosen from 7 men and 4 women. Find the number of committees containing at least 2 women, by adding the cases.
A: \(210 + 84 + 7 = 301\).
Q: Five boys and three girls stand in a row so that no two girls are next to each other. How many arrangements are there?
A: Arrange the 5 boys first: \(5! = 120\). This leaves 6 gaps (the four between boys and the two ends), and the 3 girls take 3 different gaps in \({}^{6}P_3 = 120\) ways. Total \(120\times 120 = 14\,400\).
Q: (Exam style) The 10 letters of STATISTICS are arranged in a line. Find the number of arrangements in which the three S's are together. Find also the number of arrangements which begin and end with a T. [5 marks]
A: Together: block SSS with the T, T, T, I, I, A, C gives 8 items, so \(\dfrac{8!}{3!\,2!} = 3360\). [M1 A1] Begin and end with T: use two of the three T's at the ends, leaving 8 letters S, S, S, T, I, I, A, C in the middle, with S three times and I twice: \(\dfrac{8!}{3!\,2!} = 3360\). [M1 A1 A1]
:::

:::quiz
? A committee of 3 is chosen from 10 people. How many ways?
- \(10\times 9\times 8 = 720\)
+ \(\dbinom{10}{3} = 120\)
- \(3! = 6\)
- \(10^3 = 1000\)
> The order of choosing does not matter, so it is a combination. 720 would count the same committee in all \(3! = 6\) orders.
? How many arrangements are there of the letters of LEVEL?
- \(5! = 120\)
- \(\dfrac{5!}{2!} = 60\)
+ \(\dfrac{5!}{2!\,2!} = 30\)
- \(\dfrac{5!}{4!} = 5\)
> LEVEL has L twice and E twice, so divide by \(2!\) for each repeated letter.
? Four people are arranged in a line with two of them, Sam and Tia, required to be next to each other. How many arrangements?
- \(3! = 6\)
+ \(2\times 3! = 12\)
- \(4! - 3! = 18\)
- \(2\times 4! = 48\)
> Treat Sam and Tia as one block: \(3!\) ways to arrange 3 items, times 2 for the order inside the block.
? Which is the easiest way to count the teams of 5 from 6 boys and 4 girls with at least one girl?
- Add the cases of 1, 2, 3, 4 girls.
+ Subtract the all-boys teams from the total.
- Multiply \(\dbinom41\) by \(\dbinom{9}{4}\).
- Use \({}^{10}P_5\).
> The complement "no girls" is a single case, \(\dbinom65 = 6\), so \(252 - 6\). Multiplying \(\dbinom41\dbinom94\) counts teams with two or more girls more than once.
? Which equation links permutations and combinations?
- \({}^{n}P_r = \dbinom nr\)
+ \({}^{n}P_r = r!\times\dbinom nr\)
- \(\dbinom nr = r!\times {}^{n}P_r\)
- \({}^{n}P_r = \dbinom{n}{r} \div n!\)
> Each combination of \(r\) items can be arranged in \(r!\) orders, so there are \(r!\) times as many permutations as combinations.
:::

:::recap
- Multiplication principle: multiply the choices for successive tasks; add when the cases are alternatives.
- \(n!\) arranges \(n\) different objects in a line; \({}^{n}P_r = \dfrac{n!}{(n-r)!}\) when order matters; \(\dbinom nr = \dfrac{n!}{r!\,(n-r)!}\) when it does not.
- With repeated items, divide by \(p!\,q!\cdots\) for each group of identical items.
- Together: glue into a block and multiply by the arrangements inside. Apart: total minus together. Fixed slots: fill them first.
- Selections: multiply combinations for each group; "at least one" is total minus none.
- Always check: whole number, smaller than the total, and a check by a second method where possible.
:::

:::note Learn more online
- **Watch:** [Permutations with items together](https://www.examsolutions.net/tutorials/permutations-with-restrictions-letters-items-together/) · ExamSolutions · the "glue them together" method
- **Watch:** [Probability using permutations and combinations](https://www.examsolutions.net/tutorials/probability-using-permutations-and-combinations/) · ExamSolutions · counting to find probabilities
- **Practise:** [CAIE S1 permutations and combinations exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/probability/permutations-and-combinations/exam-questions/) · Save My Exams · with mark schemes *(some content paid)*
- **Explore:** [Counting & Binomials](https://undergroundmathematics.org/counting-and-binomials) · Underground Mathematics · rich counting problems
- **Papers:** [9709 Paper 5 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-6/) · Physics & Maths Tutor · their page "cie-paper-6" holds Paper 5 *(unofficial archive)*

These sites open in your browser and need the internet. Links checked 3 October 2026.
:::

Next: [Probability](#math.s1.prob).
