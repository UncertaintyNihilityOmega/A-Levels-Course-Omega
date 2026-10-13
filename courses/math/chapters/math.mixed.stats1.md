@chapter math.mixed.stats1
@title Mixed practice: Statistics 1
@level ref
@paper CAIE 9709 Paper 5 · Edexcel IAL S1 · UK Statistics Year 1
@time 3–4 hours
@summary Twenty-nine short questions that mix every topic of Statistics 1 (data, permutations and combinations, probability, discrete random variables, the normal distribution), ordered from ★ to ★★★. Each answer is a mark scheme, and each question names the chapter to revise.

:::why
In the exam you are never told which chapter a question comes from. A statistics question could need a counting rule, a tree, a table of a random variable, a binomial or a normal, and choosing the model is half of the marks. This page mixes everything on purpose, so that you have to decide every time.
:::

:::tip How to use this page
Do the questions in order, a few at a time, on paper, with a calculator and the normal tables. ★ questions are one idea (2 to 3 marks), ★★ questions are exam standard for a typical Paper 5 question, ★★★ questions need two or more ideas together. Mark yourself with the scheme, and under each answer the **Revise** link takes you to the chapter for that topic. Keep a list of the chapters that come up more than once: they are your weak spots.
:::

:::try Warm-up ★
Q: [2 marks] (#math.s1.data) ★ Find the mean and the median of the values 3, 7, 7, 9, 12, 15, 16, 21.
A: The sum is 90 and there are 8 values, so the mean is \(\dfrac{90}{8} = 11.25\). [B1]
The median is halfway between the 4th and 5th values: \(\dfrac{9 + 12}{2} = 10.5\). [B1]
Q: [2 marks] (#math.s1.data) ★ Five values have \(\sum x = 60\) and \(\sum x^2 = 800\). Find their standard deviation.
A: The mean is 12, so the variance is \(\dfrac{800}{5} - 12^2 = 160 - 144 = 16\). [M1]
The standard deviation is \(\sqrt{16} = 4\). [A1]
Q: [2 marks] (#math.s1.data) ★ Eight values \(x\) have \(\sum(x - 50) = -12\). Find the mean of the values.
A: The mean of the coded values is \(\dfrac{-12}{8} = -1.5\). [M1]
So the mean of \(x\) is \(50 - 1.5 = 48.5\). [A1]
Q: [2 marks] (#math.s1.perms) ★ (a) In how many ways can 5 different books be arranged in a line on a shelf? (b) In how many ways can 3 books be chosen from 8 different books?
A: (a) \(5! = 120\). [B1]

(b) \(\dbinom83 = 56\). [B1]
Q: [2 marks] (#math.s1.perms) ★ How many different arrangements are there of the letters of the word LEVEL?
A: There are 5 letters, with L twice and E twice: [M1]
\[ \frac{5!}{2!\,2!} = 30 \]
[A1]
Q: [3 marks] (#math.s1.prob) ★ Events \(A\) and \(B\) are independent, with \(P(A) = 0.4\) and \(P(B) = 0.5\). Find \(P(A \cap B)\) and \(P(A \cup B)\).
A: For independent events \(P(A \cap B) = 0.4 \times 0.5 = 0.2\). [B1]
\(P(A \cup B) = P(A) + P(B) - P(A \cap B)\) [M1] \(= 0.4 + 0.5 - 0.2 = 0.7\). [A1]
Q: [2 marks] (#math.s1.prob) ★ Two fair dice are thrown. Find the probability that the sum of the scores is 8.
A: The outcomes with sum 8 are (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), which is 5 of the 36 equally likely outcomes. [M1]
Probability \(= \dfrac{5}{36}\). [A1]
Q: [2 marks] (#math.s1.drv) ★ The random variable \(X \sim B(10, 0.3)\). Find \(P(X = 4)\).
A: Use \(P(X = r) = \binom nr p^r q^{n-r}\): [M1]
\[ P(X = 4) = \binom{10}{4}(0.3)^4(0.7)^6 = 0.200 \]
[A1]
Q: [3 marks] (#math.s1.drv) ★ The random variable \(X\) has the distribution: \(x = 0, 1, 2, 3\) with probabilities 0.4, 0.3, 0.2, 0.1. Find \(E(X)\) and \(\mathrm{Var}(X)\).
A: \(E(X) = 0 + 0.3 + 0.4 + 0.3 = 1\). [B1]
\(E(X^2) = 0 + 0.3 + 0.8 + 0.9 = 2\). [M1]
\(\mathrm{Var}(X) = 2 - 1^2 = 1\). [A1]
Q: [2 marks] (#math.s1.normal) ★ The random variable \(X \sim N(50, 16)\). Find \(P(X > 56)\).
A: The standard deviation is 4, so \(z = \dfrac{56 - 50}{4} = 1.5\). [M1]
\(P(X > 56) = 1 - \Phi(1.5) = 0.0668\). [A1]
:::

:::try Exam standard ★★
Q: [3 marks] (#math.s1.data) ★★ In a histogram, the bar for the class 10–20 is 2 cm wide and 6 cm tall, and represents 24 people. The bar for the class 20–40 represents 30 people. Find the width and the height of the bar for the class 20–40.
A: Frequency is proportional to area. The first bar has area 12 cm² for 24 people, so 0.5 cm² represents one person. [M1]
The class 20–40 is twice as wide as 10–20, so its bar is 4 cm wide. [A1]
Its area is \(30 \times 0.5 = 15\) cm², so the height is \(\dfrac{15}{4} = 3.75\) cm. [A1]
Q: [4 marks] (#math.s1.data) ★★ The times, in minutes, taken by 100 people to complete a task are summarised in a table: \(0\text{–}10\): 5 people; \(10\text{–}20\): 15; \(20\text{–}40\): 40; \(40\text{–}80\): 30; \(80\text{–}120\): 10. Use linear interpolation to estimate the median and the 80th percentile.
A: The cumulative frequencies at the upper boundaries are 5, 20, 60, 90, 100. The median is the 50th value, in the class \(20\text{–}40\): [M1]
\[ 20 + \frac{50 - 20}{40} \times 20 = 35 \]
[A1] The 80th percentile is the 80th value, in the class \(40\text{–}80\): [M1]
\[ 40 + \frac{80 - 60}{30} \times 40 = 66.7 \]
[A1]
Q: [5 marks] (#math.s1.data) ★★ Group \(A\) has 10 values with mean 12 and standard deviation 2. Group \(B\) has 15 values with mean 16 and standard deviation 3. Find the mean and the standard deviation of all 25 values combined.
A: The total of the values is \(10 \times 12 + 15 \times 16 = 360\), so the combined mean is \(\dfrac{360}{25} = 14.4\). [M1] [A1]
For each group, \(\sum x^2 = n(\sigma^2 + \bar x^2)\): group \(A\) gives \(10(4 + 144) = 1480\) and group \(B\) gives \(15(9 + 256) = 3975\). [M1]
The combined variance is [M1]
\[ \frac{1480 + 3975}{25} - 14.4^2 = 218.2 - 207.36 = 10.84 \]
So the standard deviation is \(\sqrt{10.84} = 3.29\). [A1]
Q: [3 marks] (#math.s1.perms) ★★ Five boys and four girls stand in a line so that no two boys are next to each other and no two girls are next to each other. In how many ways can they be arranged?
A: With 5 boys and 4 girls the only pattern that works is B G B G B G B G B. [M1]
The boys can be arranged in \(5!\) ways and the girls in \(4!\) ways: [M1]
\[ 5! \times 4! = 120 \times 24 = 2880 \]
[A1]
Q: [4 marks] (#math.s1.perms) ★★ Four-digit numbers are formed using four different digits chosen from 1 to 9.

(a) How many such numbers are there? [2]

(b) How many of them are even? [2]
A: (a) There are 9 choices for the first digit, 8 for the second, 7 for the third and 6 for the fourth: [M1]
\[ 9 \times 8 \times 7 \times 6 = 3024 \]
[A1]

(b) The last digit must be one of 2, 4, 6, 8, so 4 choices. Fill it first, then the others from the remaining 8 digits: [M1]
\[ 4 \times 8 \times 7 \times 6 = 1344 \]
[A1]
Q: [4 marks] (#math.s1.prob) ★★ For events \(A\) and \(B\), \(P(A) = 0.5\), \(P(B) = 0.4\) and \(P(A \cup B) = 0.7\). Find \(P(A \cap B)\), and show that \(A\) and \(B\) are independent.
A: \(P(A \cup B) = P(A) + P(B) - P(A \cap B)\), so \(0.7 = 0.9 - P(A \cap B)\). [M1]
\(P(A \cap B) = 0.2\). [A1]
\(P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{0.2}{0.4} = 0.5\). [M1]
This equals \(P(A)\) (equivalently \(P(A)P(B) = 0.2 = P(A \cap B)\)), so \(A\) and \(B\) are independent. [A1]
Q: [3 marks] (#math.s1.prob) ★★ A bag contains 5 red and 3 blue counters. Two counters are taken at random without replacement. Find the probability that they are the same colour.
A: Both red or both blue: [M1]
\[ \frac58 \times \frac47 + \frac38 \times \frac27 = \frac{20}{56} + \frac{6}{56} \]
[M1] \(= \dfrac{13}{28} = 0.464\). [A1]
Q: [4 marks] (#math.s1.drv) ★★ Each item made by a machine is defective with probability 0.2, independently. A sample of 15 items is taken.

(a) Find the probability that at most 2 items are defective. [2]

(b) Find the mean and the variance of the number of defective items. [2]
A: (a) The number defective is \(X \sim B(15, 0.2)\): [M1]
\[ P(X \le 2) = 0.8^{15} + 15(0.2)(0.8)^{14} + \binom{15}{2}(0.2)^2(0.8)^{13} = 0.398 \]
[A1]

(b) Mean \(= np = 3\). [B1] Variance \(= npq = 15 \times 0.2 \times 0.8 = 2.4\). [B1]
Q: [4 marks] (#math.s1.drv) ★★ A biased coin lands heads with probability 0.25. It is tossed until the first head appears. Let \(X\) be the number of tosses.

(a) Find \(P(X = 5)\). [2]

(b) Find \(P(X \le 3)\). [2]
A: (a) \(X\) is geometric with \(p = 0.25\): the first four tosses are tails and the fifth is a head. [M1]
\[ P(X = 5) = 0.75^4 \times 0.25 = 0.0791 \]
[A1]

(b) \(P(X \le 3)\) is 1 minus the probability that the first three tosses are all tails: [M1]
\[ P(X \le 3) = 1 - 0.75^3 \]
\(= 0.578\). [A1]
Q: [5 marks] (#math.s1.normal) ★★ The random variable \(X \sim N(\mu, \sigma^2)\) is such that \(P(X < 30) = 0.2\) and \(P(X > 50) = 0.1\). Find the values of \(\mu\) and \(\sigma\).
A: From the tables, \(\Phi(z) = 0.2\) gives \(z = -0.8416\). [B1]
\(P(X > 50) = 0.1\) means \(\Phi(z) = 0.9\), so \(z = 1.2816\). [B1]
Standardise both: [M1]
\[ \frac{30 - \mu}{\sigma} = -0.8416, \qquad \frac{50 - \mu}{\sigma} = 1.2816 \]
Subtracting, \(\dfrac{20}{\sigma} = 2.1232\), so \(\sigma = 9.42\). [A1]
Then \(\mu = 30 + 0.8416 \times 9.42 = 37.9\). [A1]
Q: [4 marks] (#math.s1.normal) ★★ The random variable \(X \sim B(100, 0.4)\). Use a suitable approximation to find \(P(X \ge 45)\).
A: \(np = 40 > 5\) and \(nq = 60 > 5\), so use \(N(40, 24)\), because \(npq = 100 \times 0.4 \times 0.6 = 24\). [B1]
With a continuity correction, \(P(X \ge 45) \approx P(N > 44.5)\). [M1]
\[ z = \frac{44.5 - 40}{\sqrt{24}} = 0.919 \]
[M1] \(P = 1 - \Phi(0.919) = 0.179\). [A1]
:::

:::try Stretch ★★★
Q: [8 marks] (#math.s1.data) ★★★ The masses, in kg, of 40 bags of sugar are summarised by \(\sum x = 1020\) and \(\sum x^2 = 26\,500\).

(a) Calculate the mean and the standard deviation of the masses. [3]

Assume that the masses are normally distributed with the mean and standard deviation found in part (a).

(b) Find the probability that a randomly chosen bag has a mass less than 20 kg. [2]

A further bag of mass 31 kg is added to the 40 bags.

(c) Find the mean and the standard deviation of the masses of all 41 bags. [3]
A: (a) The mean is \(\dfrac{1020}{40} = 25.5\). [B1]
The variance is [M1]
\[ \frac{26\,500}{40} - 25.5^2 = 662.5 - 650.25 = 12.25 \]
So the standard deviation is 3.5. [A1]

(b) \(z = \dfrac{20 - 25.5}{3.5} = -1.571\). [M1]
\[ P(X < 20) = \Phi(-1.571) = 1 - 0.9419 = 0.0581 \]
This is 0.058 to 3 s.f. (accept 0.0582 from tables). [A1]

(c) The new total is \(1020 + 31 = 1051\), so the mean is \(\dfrac{1051}{41} = 25.6\). [B1]
The new \(\sum x^2 = 26\,500 + 961 = 27\,461\), so the variance is [M1]
\[ \frac{27\,461}{41} - 25.634^2 = 12.67 \]
and the standard deviation is 3.56. [A1]
Q: [7 marks] (#math.s1.perms) ★★★ Seven people, including Ann, Ben and Cal, stand in a line.

(a) How many arrangements are there in which Ann and Ben are not next to each other? [3]

(b) How many arrangements are there in which Ann, Ben and Cal are all next to each other? [2]

(c) One arrangement is chosen at random. Find the probability that Ann and Ben are at the two ends of the line. [2]
A: (a) The total number of arrangements is \(7! = 5040\). [M1]
With Ann and Ben together, treat them as one object: \(2 \times 6! = 1440\). [M1]
Not together: \(5040 - 1440 = 3600\). [A1]

(b) Treat the three as one object, arranged internally in \(3!\) ways: [M1]
\[ 5! \times 3! = 720 \]
[A1]

(c) Ann and Ben take the two ends in 2 ways, and the other five people fill the middle in \(5!\) ways: \(2 \times 120 = 240\). [M1]
The probability is \(\dfrac{240}{5040} = \dfrac{1}{21} = 0.0476\). [A1]
Q: [8 marks] (#math.s1.prob) ★★★ In a certain population 2% of people have a particular disease. A test gives a positive result for 95% of people who have the disease and for 4% of people who do not.

(a) Find the probability that a randomly chosen person tests positive. [3]

(b) Given that a person tests positive, find the probability that they have the disease. [2]

A second, independent test of the same kind is given to a person, and it is also positive. The person's results on the two tests are independent, given whether or not they have the disease.

(c) Given that both tests are positive, find the probability that the person has the disease. [3]
A: (a) Draw a tree: disease (0.02) then positive (0.95); no disease (0.98) then positive (0.04). [B1]
\[ P(\text{positive}) = 0.02 \times 0.95 + 0.98 \times 0.04 = 0.019 + 0.0392 \]
[M1] \(= 0.0582\). [A1]

(b) \(P(\text{disease} \mid \text{positive}) = \dfrac{0.019}{0.0582}\). [M1]
\(= 0.326\). [A1]

(c) Both positive with the disease: \(0.02 \times 0.95^2 = 0.01805\). [M1]
Both positive without the disease: \(0.98 \times 0.04^2 = 0.001568\). [M1]
\[ P(\text{disease} \mid \text{both}) = \frac{0.01805}{0.01805 + 0.001568} = 0.920 \]
[A1]
Q: [9 marks] (#math.s1.drv) ★★★ The discrete random variable \(X\) takes the values 1, 2, 3, 4, with \(P(X = x) = kx^2\).

(a) Show that \(k = \dfrac{1}{30}\). [2]

(b) Find \(E(X)\). [2]

(c) Find \(\mathrm{Var}(X)\). [2]

Two independent observations of \(X\) are made.

(d) Find the probability that their sum is 5. [3]
A: (a) The probabilities add up to 1: \(k(1 + 4 + 9 + 16) = 1\). [M1]
\(30k = 1\), so \(k = \dfrac1{30}\). [A1]

(b) The probabilities are \(\dfrac{1}{30}, \dfrac{4}{30}, \dfrac{9}{30}, \dfrac{16}{30}\). [M1]
\[ E(X) = \frac{1 + 8 + 27 + 64}{30} = \frac{100}{30} = \frac{10}{3} \]
[A1]

(c) [M1]
\[ E(X^2) = \frac{1 + 16 + 81 + 256}{30} = \frac{354}{30} = 11.8 \]
\[ \mathrm{Var}(X) = 11.8 - \Big(\frac{10}{3}\Big)^2 = 0.689 \]
[A1]

(d) The sum is 5 for the pairs (1, 4), (4, 1), (2, 3), (3, 2). [M1]
\[ P = 2\Big(\frac{1}{30} \times \frac{16}{30} + \frac{4}{30} \times \frac{9}{30}\Big) = \frac{2(16 + 36)}{900} \]
[M1] \(= 0.116\). [A1]
Q: [6 marks] (#math.s1.drv) ★★★ A seed germinates with probability 0.8, independently of other seeds. Seeds are sold in packets of 10. A packet is called good if at least 8 of its seeds germinate.

(a) Find the probability that a packet is good. [3]

Five packets are chosen at random.

(b) Find the probability that exactly 3 of them are good. [2]

(c) Packets are tested one at a time until a good packet is found. Find the expected number of packets tested. [1]
A: (a) Let \(X\) be the number germinating, so \(X \sim B(10, 0.8)\). [M1]
\[ P(X \ge 8) = \binom{10}{8}(0.8)^8(0.2)^2 + 10(0.8)^9(0.2) + 0.8^{10} \]
[M1] \(= 0.678\). [A1]

(b) The number of good packets is \(Y \sim B(5, 0.6778)\): [M1]
\[ P(Y = 3) = \binom53(0.6778)^3(0.3222)^2 = 0.323 \]
[A1]

(c) The number tested is geometric with \(p = 0.6778\), so \(E = \dfrac{1}{0.6778} = 1.48\). [B1]
Q: [7 marks] (#math.s1.normal) ★★★ A machine cuts rods whose lengths, in cm, are normally distributed with standard deviation 0.8. The machine is set so that 4% of the rods are shorter than 49.5 cm.

(a) Find the mean length of the rods. [3]

(b) Find the probability that a rod is longer than 52 cm. [2]

A sample of 20 rods is taken at random.

(c) Find the probability that at most 1 rod is longer than 52 cm. [2]
A: (a) \(\Phi(z) = 0.04\) gives \(z = -1.751\). [B1]
\[ \frac{49.5 - \mu}{0.8} = -1.751 \]
[M1] So \(\mu = 49.5 + 1.751 \times 0.8 = 50.9\). [A1]

(b) \(z = \dfrac{52 - 50.9}{0.8} = 1.375\). [M1]
\(P(L > 52) = 1 - \Phi(1.375) = 0.0846\). [A1]

(c) The number longer than 52 cm is \(B(20, 0.0846)\): [M1]
\[ P(\le 1) = 0.9154^{20} + 20(0.0846)(0.9154)^{19} = 0.486 \]
[A1]
Q: [5 marks] (#math.s1.normal) ★★★ A fair coin is tossed 50 times. Let \(X\) be the number of heads.

(a) Explain why a normal distribution can be used to approximate the distribution of \(X\), and state its parameters. [2]

(b) Use this approximation to find the probability that between 20 and 28 heads, inclusive, are obtained. [3]
A: (a) \(X \sim B(50, 0.5)\) with \(np = 25 > 5\) and \(nq = 25 > 5\), so \(X\) is approximately \(N(25, 12.5)\), because \(npq = 12.5\). [B1] [B1]

(b) With a continuity correction, \(P(20 \le X \le 28) \approx P(19.5 < N < 28.5)\). [M1]
The limits are \(z = \dfrac{19.5 - 25}{\sqrt{12.5}} = -1.556\) and \(z = \dfrac{28.5 - 25}{\sqrt{12.5}} = 0.990\). [M1]
\[ \Phi(0.990) - \Phi(-1.556) = 0.8389 - 0.0599 = 0.779 \]
[A1]
Q: [8 marks] (#math.s1.prob) ★★★ A bag contains 4 red and 6 blue counters. Three counters are taken at random, without replacement, and \(X\) is the number of red counters taken.

(a) Draw up the probability distribution table for \(X\). [3]

(b) Find \(E(X)\). [2]

All three counters are now returned to the bag. This experiment is repeated 8 times in total, independently.

(c) Find the probability that \(X = 2\) in exactly 2 of the 8 experiments. [3]
A: (a) There are \(\binom{10}{3} = 120\) equally likely selections: [M1]
\[ P(X = r) = \frac{\binom4r\binom{6}{3-r}}{120} \]
\(P(X = 0) = \dfrac{20}{120} = \dfrac16\) and \(P(X = 1) = \dfrac{4 \times 15}{120} = \dfrac12\). [A1]
\(P(X = 2) = \dfrac{6 \times 6}{120} = \dfrac{3}{10}\) and \(P(X = 3) = \dfrac{4}{120} = \dfrac1{30}\). [A1]

(b) \(E(X) = 0 + \dfrac12 + \dfrac{6}{10} + \dfrac{3}{30}\). [M1]
\(= 1.2\). [A1]

(c) The number of experiments with \(X = 2\) is \(Y \sim B(8, 0.3)\): [M1]
\[ P(Y = 2) = \binom82(0.3)^2(0.7)^6 \]
[M1] \(= 0.296\). [A1]
:::
