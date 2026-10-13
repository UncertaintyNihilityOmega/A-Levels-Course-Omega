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

:::try Warm-up
Q: Evaluate \(2^3 \times 3^2\). (from [Indices, surds and standard form](#math.f.powers))
A: \(8 \times 9 = 72\).
Q: Find the coefficient of \(x^2\) in the expansion of \((1 + x)^5\). (from [Series](#math.p1.series))
A: It is the binomial coefficient \(\dbinom52\) \(= \dfrac{5 \times 4}{2 \times 1} = 10\), the middle of the row 1, 5, 10, 10, 5, 1.
Q: Work out \(\dfrac{7 \times 6 \times 5 \times 4}{4 \times 3 \times 2 \times 1}\). (from [Numbers from scratch](#math.f.numbers))
A: Cancel the 4: \(\dfrac{7 \times 6 \times 5}{3 \times 2 \times 1}\) \(= \dfrac{210}{6} = 35\). This is \(\dbinom74\), which you will meet in the first example below.
:::

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

:::proof Why there are \(n!\) arrangements, and where \({}^{n}P_r = \dfrac{n!}{(n-r)!}\) comes from
Fill \(r\) places in a line from \(n\) different objects. The first place can take any of the \(n\) objects. Whichever is used, \(n - 1\) remain for the second place, then \(n - 2\) for the third, and so on. The \(r^{\text{th}}\) place has \(n - r + 1\) choices left. By the multiplication principle the number of arrangements is
\[{}^{n}P_r = n(n - 1)(n - 2)\cdots(n - r + 1)\]
Multiply and divide by \((n - r)(n - r - 1)\cdots 2 \times 1\) \(= (n - r)!\). The top becomes \(n!\), so
\[{}^{n}P_r = \frac{n!}{(n - r)!}\]
Putting \(r = n\) (arranging all the objects) gives \(\dfrac{n!}{0!}\), which is \(n!\) only if \(0! = 1\). That is why \(0!\) is defined as 1. Check: \({}^{10}P_3 = 10 \times 9 \times 8\) \(= 720\), and \(\dfrac{10!}{7!} = 720\) too.
:::

:::proof Why \(\dbinom{n}{r} = \dfrac{{}^{n}P_r}{r!}\)
Count the arrangements of \(r\) objects chosen from \(n\) in two ways.
First way: there are \({}^{n}P_r\) of them, as above.
Second way: first choose which \(r\) objects are used, in \(\dbinom{n}{r}\) ways. Then arrange those \(r\) objects in a line, in \(r!\) ways. By the multiplication principle there are \(\dbinom{n}{r} \times r!\) arrangements.
Both counts are of the same arrangements, so \({}^{n}P_r = \dbinom{n}{r}\, r!\). Divide by \(r!\) and use the formula for \({}^{n}P_r\):
\[\binom{n}{r} = \frac{{}^{n}P_r}{r!} = \frac{n!}{r!\,(n - r)!}\]
Check with the squad of 4 from 7: \({}^{7}P_4 = 840\) and \(\dfrac{840}{4!} = 35\).
:::

:::eg In a race with 10 runners, how many ways can the gold, silver and bronze medals be awarded? How many ways can a squad of 4 be chosen from 7 players? In how many of those squads is Priya included?
Medals: order matters, so \({}^{10}P_3 = 10 \times 9 \times 8\) \(= 720\).
Squad: order does not matter, so \(\binom{7}{4} = \dfrac{7!}{4!\,3!} = 35\).
Priya included: she fills one place, and 3 more are chosen from the other 6: \(\binom{6}{3} = 20\).
:::

## Arrangements with repeated items

If some of the \(n\) items are identical, many of the \(n!\) arrangements look the same. Divide by the number of ways of rearranging each group of identical items.

:::key Arrangements with repeats
The number of arrangements of \(n\) items, of which \(p\) are identical of one kind, \(q\) are identical of another kind, and so on, is
\[\frac{n!}{p!\,q!\cdots}\]
:::

:::proof Why we divide by \(p!\,q!\)
Suppose \(n\) items include \(p\) identical items of one kind and \(q\) of another. Pretend for a moment that every item has its own label (A₁, A₂, A₃, N₁, N₂ and so on). Then all the items are different and there are \(n!\) arrangements.
Now remove the labels. Take one arrangement that you can actually see, such as BANANA. Swapping the three A's among themselves gives \(3!\) labelled arrangements that look the same, and swapping the two N's gives \(2!\) more. So every visible arrangement was counted \(p! \times q!\) times in the \(n!\).
The number of visible arrangements is therefore \(\dfrac{n!}{p!\,q!}\). Check with BANANA: \(\dfrac{720}{3! \times 2!} = 60\), the value found below.
:::

:::eg Find the number of arrangements of the letters of (a) BANANA, (b) MISSISSIPPI. For STATISTICS, find the number of arrangements in which the three S's are together.
(a) BANANA has 6 letters: B once, A three times, N twice. \(\dfrac{6!}{3!\,2!} = \dfrac{720}{12}\) \(= 60\).
(b) MISSISSIPPI has 11 letters: M once, I four times, S four times, P twice. \(\dfrac{11!}{4!\,4!\,2!}\) \(= \dfrac{39\,916\,800}{1152} = 34\,650\).
STATISTICS has 10 letters: S three times, T three times, I twice, A once, C once. Treat SSS as a single block. There are then 8 items: the block, T, T, T, I, I, A, C, with T three times and I twice. The number of arrangements is \(\dfrac{8!}{3!\,2!}\) \(= \dfrac{40\,320}{12} = 3360\).
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
Total: \({}^{7}P_4 = 7\times 6\times 5\times 4\) \(= 840\).
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

## Long exam questions

Real questions have several parts, and each part often reuses the last. Work through these, then cover the working and try them again.

:::eg (Exam style) The digits 1, 2, 3, 4, 5, 6, 7 and 8 are used to make five-digit numbers. No digit is used more than once in a number. (a) How many five-digit numbers can be made? (b) How many of them are even? (c) How many of them are even and greater than 60 000? (d) How many of them contain both of the digits 1 and 2? [10 marks]
(a) The number is a permutation of 5 digits from 8:
\[{}^{8}P_5 = 8 \times 7 \times 6 \times 5 \times 4 = 6720\]
[B1]
(b) Fill the restricted slot first. The last digit is 2, 4, 6 or 8, which is 4 choices. [M1] The other four slots are filled from the remaining 7 digits in \(7 \times 6 \times 5 \times 4 = 840\) ways. So there are \(4 \times 840 = 3360\) even numbers. [A1] (Half of the total, as expected.)
(c) Greater than 60 000 means the first digit is 6, 7 or 8, so split by the first digit. [M1]
First digit 6 or 8 (these are both even, so the last digit cannot be the same one): the last digit is an even digit other than the first. That is 3 choices. The three middle slots are filled from the remaining 6 digits in \(6 \times 5 \times 4 = 120\) ways. So each of these first digits gives \(3 \times 120 = 360\) numbers, and together \(720\). [A1]
First digit 7: the last digit can be any of the 4 even digits, and the middle slots give 120 ways, so \(4 \times 120 = 480\). [A1]
Total even and greater than 60 000: \(720 + 480 = 1200\). [A1]
(d) Choose the positions for the digits 1 and 2: the digit 1 can go in any of 5 places and the digit 2 in any of the other 4, which is \({}^{5}P_2 = 20\) ways. [M1] The other three places are filled from the remaining 6 digits in \({}^{6}P_3 = 120\) ways. [M1] Total \(20 \times 120 = 2400\). [A1]
:::

:::eg (Exam style) A school council of 6 members is chosen from 5 teachers and 8 students. (a) How many different councils are possible? (b) How many have exactly 2 teachers? (c) How many have at least 2 teachers? (d) Mr Rao and Ms Lee are two of the teachers. How many councils do not contain both of them? (e) A council is chosen at random from all the possible councils. Find the probability that it has exactly 2 teachers. [11 marks]
(a) There are 13 people and order does not matter:
\[\binom{13}{6} = 1716\]
[B1]
(b) Choose 2 teachers from 5 and 4 students from 8:
\[\binom52\binom84 = 10 \times 70 = 700\]
[M1 A1]
(c) "At least 2" is easiest as the total minus the cases with 0 or 1 teacher. [M1] With no teacher, all 6 come from the 8 students: \(\dbinom86 = 28\). [B1] With one teacher: \(\dbinom51\dbinom85 = 5 \times 56 = 280\). [B1] So the number is \(1716 - 28 - 280 = 1408\). [A1]
(d) Count the councils that contain both, then subtract. If Mr Rao and Ms Lee are both in, the other 4 places are chosen from the remaining 11 people: \(\dbinom{11}{4} = 330\). [M1] So \(1716 - 330 = 1386\) councils do not contain both. [A1]
(e) The probability is the favourable count over the total count:
\[\frac{700}{1716} = \frac{175}{429} = 0.408\]
[M1 A1]
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

:::eg Spot the error: arrangements of COMMITTEE
A student wrote this answer to "Find the number of arrangements of the letters of COMMITTEE" [3 marks].

Line 1: There are 9 letters. M, T and E each appear twice.
Line 2: Number of arrangements \(= \dfrac{9!}{2! + 2! + 2!}\) \(= \dfrac{362\,880}{6}\) \(= 60\,480\).

**Line 1 is correct [B1].** It finds the length of the word and the three repeated letters. **Line 2 scores [M0]:** the repeats must be divided out **one after another**, so the denominator is the **product** \(2! \times 2! \times 2!\), not the sum. A wrong denominator is a wrong method, so the method mark is lost, and the answer mark is lost too [A0]. The student scores 1 out of 3.

Correct working:
\[\frac{9!}{2!\,2!\,2!} = \frac{362\,880}{8} = 45\,360\]
[M1 A1]

**Check:** each pair of identical letters halves the count, because swapping the two copies gives an arrangement that looks the same. Three pairs halve it three times, so the divisor is \(2 \times 2 \times 2 = 8\), not \(6\). ✓
:::

:::try Start easy, finish at exam standard
Q: Evaluate \(\dfrac{6!}{4!}\) and \(\dbinom94\).
A: \(\dfrac{6!}{4!} = 6\times 5 = 30\). \(\dbinom94\) \(= \dfrac{9\times 8\times 7\times 6}{4\times 3\times 2\times 1}\) \(= 126\).
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

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ A club has 9 members. (a) In how many ways can a president and a treasurer be chosen? (b) In how many ways can a committee of 3 be chosen?
A: (a) The order matters, so \({}^{9}P_2 = 9 \times 8 = 72\). [B1] (b) The order does not matter, so \(\dbinom93 = 84\). [B1]
Q: [4 marks] ★ The 6 letters of the word STATIC are arranged in a line. Find the number of arrangements (a) in total, (b) that begin with S.
A: (a) The letter T appears twice, so the number is \(\dfrac{6!}{2!} = 360\). [M1 A1] (b) With S fixed first, arrange the other five letters T, A, T, I, C: \(\dfrac{5!}{2!} = 60\). [M1 A1]
Q: [5 marks] ★★ Four-digit numbers are formed from the digits 0 to 9. A number cannot start with 0 and no digit is used twice. How many of these numbers are even?
A: Split by the last digit. [M1] If the last digit is 0, the first three slots take \(9 \times 8 \times 7 = 504\) ways. [A1] If the last digit is 2, 4, 6 or 8 (4 choices), the first digit cannot be 0 or the last digit, so it has 8 choices. [M1] The second slot has 8 choices (0 is now allowed) and the third has 7, so this case gives \(4 \times 8 \times 8 \times 7 = 1792\). [A1] The total is \(504 + 1792 = 2296\). [A1]
Q: [4 marks] ★★ A team of 4 is chosen from 6 juniors and 5 seniors. The team must contain at least one junior and at least one senior. How many teams are there?
A: Without restriction there are \(\dbinom{11}{4} = 330\) teams. [B1] Remove the all-junior teams, \(\dbinom64 = 15\), [B1] and the all-senior teams, \(\dbinom54 = 5\). [B1] The number is \(330 - 15 - 5 = 310\). [A1]
Q: [5 marks] ★★ Seven people stand in a row. Dev must stand at one of the two ends, and Eva and Fay must stand next to each other. How many arrangements are there?
A: Dev can take either end, which is 2 choices. [B1] With Dev fixed, treat Eva and Fay as one block: the block and the other four people make 5 items. [M1] These can be arranged in \(5! = 120\) ways, and Eva and Fay can swap inside the block, so \(120 \times 2 = 240\). [M1 A1] The total is \(2 \times 240 = 480\). [A1]
Q: [4 marks] ★★ A committee of 4 is chosen at random from 5 men and 3 women. Find the probability that it contains exactly 2 women.
A: The number of possible committees is \(\dbinom84 = 70\). [B1] The number with exactly 2 women is
\[\binom32\binom52 = 3 \times 10 = 30\]
[M1 A1] so the probability is \(\dfrac{30}{70} = \dfrac37\). [A1]
Q: [8 marks] (#math.p1.quadratics) ★★★ A club has \(n\) members. The number of ways of choosing a president and a secretary is 45 more than the number of ways of choosing a committee of 2. (a) Find \(n\). (b) Four of the members are left-handed. How many committees of 3 contain at least one left-handed member?
H: Write both counts in terms of \(n\): the posts give \(n(n - 1)\), and the committee gives \(\dfrac{n(n - 1)}{2}\).
H: The difference of the two counts is \(\dfrac{n(n - 1)}{2}\), so you get \(n(n - 1) = 90\), which is a quadratic.
H: Factorise \(n^2 - n - 90\), then say why one root is rejected. For (b), count all committees and subtract those with no left-handed member.
A: (a) The posts: \({}^{n}P_2 = n(n - 1)\). The committee: \(\dbinom n2 = \dfrac{n(n - 1)}{2}\). [M1] The difference is \(\dfrac{n(n - 1)}{2} = 45\), so \(n^2 - n - 90 = 0\). [A1] Then \((n - 10)(n + 9) = 0\). [M1] So \(n = 10\). [A1] The root \(n = -9\) is rejected because a number of members cannot be negative. [B1] (b) All committees: \(\dbinom{10}{3} = 120\). [B1] Committees with no left-handed member, chosen from the other 6: \(\dbinom63 = 20\). [B1] So \(120 - 20 = 100\). [A1]
Q: [8 marks] ★★★ The 10 letters of the word BOOKKEEPER are arranged in a line. Find the number of arrangements (a) in total, (b) in which the three E's are together, (c) in which no two E's are next to each other.
H: The word has O twice, K twice and E three times. In (a) divide out each repeated letter.
H: For (b), glue EEE into one block and count the arrangements of the 8 items, remembering the O's and K's.
H: For (c), arrange the 7 letters that are not E first. They leave 8 gaps (including both ends). Choose 3 different gaps for the E's.
A: (a) \(\dfrac{10!}{2!\,2!\,3!}\) [M1] \(= \dfrac{3\,628\,800}{24} = 151\,200\). [A1] (b) The block EEE with B, O, O, K, K, P, R makes 8 items. [M1] The O's and K's are repeated: \(\dfrac{8!}{2!\,2!} = 10\,080\). [M1 A1] (c) The 7 letters B, O, O, K, K, P, R can be arranged in \(\dfrac{7!}{2!\,2!} = 1260\) ways. [B1] They leave 8 gaps, and the three identical E's go into 3 different gaps in \(\dbinom83 = 56\) ways. [M1] The total is \(1260 \times 56 = 70\,560\). [A1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A convex polygon has 12 sides and so 12 vertices. (a) Find the number of diagonals. (b) Find the number of triangles that can be drawn with their vertices at three of the 12 vertices. (c) Find the number of those triangles that have none of their sides along a side of the polygon.
H: A diagonal joins two vertices that are not neighbours. Count all pairs of vertices, then remove the sides.
H: For (c), count the triangles that do use polygon sides and subtract. A triangle can have two polygon sides (three consecutive vertices) or exactly one.
H: For exactly one side: pick the side (12 ways). The third vertex cannot be either end of that side or a neighbour of either end.
A: (a) Every pair of vertices is joined by a side or a diagonal, so the diagonals number \(\dbinom{12}{2} - 12 = 66 - 12 = 54\). [M1 A1] (b) Any three vertices make a triangle: \(\dbinom{12}{3} = 220\). [B1] (c) Triangles with two polygon sides use three consecutive vertices, and there are 12 of them. [B1] Triangles with exactly one polygon side: choose the side in 12 ways. The third vertex cannot be one of the 4 vertices at or next to the ends of that side, so it has \(12 - 4 = 8\) choices. [M1] That gives \(12 \times 8 = 96\). [A1] The number of triangles using at least one side is \(12 + 96 = 108\), so the number using none is \(220 - 108 = 112\). [M1 A1]
Q: [6 marks] ★★★ A walker goes from \((0, 0)\) to \((6, 4)\) on a grid, moving one unit right or one unit up at each step. (a) How many different routes are there? (b) How many routes pass through the point \((3, 2)\)? (c) How many routes avoid \((3, 2)\)?
H: Every route is a sequence of 10 steps, 6 of them "right" and 4 of them "up". Which steps are "up"?
H: A route through \((3, 2)\) is a route from \((0, 0)\) to \((3, 2)\) followed by a route from \((3, 2)\) to \((6, 4)\). Multiply the two counts.
A: (a) Choose which 4 of the 10 steps are "up": \(\dbinom{10}{4} = 210\). [M1 A1] (b) From \((0, 0)\) to \((3, 2)\) there are 3 rights and 2 ups: \(\dbinom52 = 10\) routes. [M1] From \((3, 2)\) to \((6, 4)\) the steps are the same, so there are also \(\dbinom52 = 10\) routes. [M1] Together \(10 \times 10 = 100\). [A1] (c) \(210 - 100 = 110\). [A1]
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

:::checklist What you can now do
- [ ] I can use the multiplication principle, filling the restricted slots first, and add the counts when the cases are alternatives.
- [ ] I can say whether a question is about a permutation (order matters) or a combination (order does not matter).
- [ ] I can calculate \({}^{n}P_r\) and \(\dbinom{n}{r}\) and use \(n!\).
- [ ] I can count the arrangements of a word or set of items with repeated letters.
- [ ] I can count arrangements in which some items must be together, apart, or at the ends.
- [ ] I can count numbers formed from digits under conditions such as even, odd or greater than a given value.
- [ ] I can count selections with conditions such as "exactly", "at least one" and "must include", by cases or by subtracting the complement.
- [ ] I can count the ways of seating people in two or more rows.
:::

:::recap
- Multiplication principle: multiply the choices for successive tasks; add when the cases are alternatives.
- \(n!\) arranges \(n\) different objects in a line; \({}^{n}P_r = \dfrac{n!}{(n-r)!}\) when order matters; \(\dbinom nr = \dfrac{n!}{r!\,(n-r)!}\) when it does not.
- With repeated items, divide by \(p!\,q!\cdots\) for each group of identical items.
- Together: glue into a block and multiply by the arrangements inside. Apart: total minus together. Fixed slots: fill them first.
- Selections: multiply combinations for each group; "at least one" is total minus none.
- Always check: whole number, smaller than the total, and a check by a second method where possible.
:::

:::links
- watch: [Permutations with items together](https://www.examsolutions.net/tutorials/permutations-with-restrictions-letters-items-together/) · ExamSolutions · the "glue them together" method
- watch: [Probability using permutations and combinations](https://www.examsolutions.net/tutorials/probability-using-permutations-and-combinations/) · ExamSolutions · counting to find probabilities
- practise: [CAIE S1 permutations and combinations exam questions](https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/topic-questions/probability/permutations-and-combinations/exam-questions/) · Save My Exams · with mark schemes [paid]
- explore: [Counting & Binomials](https://undergroundmathematics.org/counting-and-binomials) · Underground Mathematics · rich counting problems
- papers: [9709 Paper 5 past papers](https://www.physicsandmathstutor.com/a-level-maths-papers/cie-paper-6/) · Physics & Maths Tutor · their page "cie-paper-6" holds Paper 5 [unofficial]

Links checked 3 October 2026.
:::
Next: [Probability](#math.s1.prob).
