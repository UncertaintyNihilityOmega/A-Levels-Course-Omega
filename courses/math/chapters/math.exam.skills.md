@chapter math.exam.skills
@title Writing maths for marks
@level guide
@paper CAIE 9709 · all papers
@time 2 hours
@summary What the command words in a maths exam ask for, how method, accuracy and independent marks work, how follow-through and accuracy rules affect your answer, and how to lay out long working so that every mark you earned is visible.

:::why
Two students can know the same mathematics and score 15 marks apart. The difference is usually not knowledge: it is how they write. An examiner can only award a mark for what is on the page. This chapter shows what that means line by line.
:::

**Before you start:** the general advice in [Exam technique](#road.technique) and [Command words decoded](#road.commands) applies to every subject. This chapter is the mathematics version. The calculator rules are in [Your calculator](#math.calc).

## The command words of mathematics

Each of these words tells you what to write, and what you may leave out.

| Command | What it asks | What the examiner needs to see |
|---|---|---|
| **Find**, **calculate**, **determine** | get the answer | a method, then the answer to the right accuracy |
| **Solve** | find every value that satisfies the equation | working, then **all** solutions in the stated interval |
| **Show that** | prove a result that is given in the question | every step from the start to the printed answer, with no gaps and no working backwards |
| **Verify** | check that a value satisfies something | substitute the value, show both sides, say they are equal |
| **State** | write down, no working needed | the answer only; working earns nothing extra |
| **Exact** | no decimals | surds, fractions, \(\pi\), \(\ln 2\), \(e\) |
| **Hence** | use the previous part | the result you were just given or proved |
| **Hence or otherwise** | any valid method | usually the previous part is quicker, but another method is allowed |
| **Sketch** | shape and key features, not to scale | axes, intercepts, turning points, asymptotes, with coordinates marked |
| **Express in the form** | rewrite in a given structure | the constants in the stated form, e.g. \(a(x + b)^2 + c\) |
| **Give a reason** | one line of justification | a mathematical reason, not "it is obvious" |

:::warn "Hence" means use it
If a question says "hence", a solution that ignores the previous part and starts again may lose the marks, even if it is correct. The question is testing whether you can use the result you have just found. If you can see a quicker way that does not use it, check the wording: "hence or otherwise" allows it, plain "hence" does not.
:::

:::eg Show that: no gaps, no working backwards
**(a)** Show that the equation \(2\sin^2\theta = 3\cos\theta\) can be written as \(2\cos^2\theta + 3\cos\theta - 2 = 0\). **(b)** Hence solve the equation for \(0^\circ \le \theta \le 360^\circ\). [6 marks]

**(a)** Start from the left and finish at the printed result:

\[\begin{aligned} 2\sin^2\theta &= 3\cos\theta \\ 2(1 - \cos^2\theta) &= 3\cos\theta \quad [\text{M1: use } \sin^2\theta = 1 - \cos^2\theta] \\ 2 - 2\cos^2\theta - 3\cos\theta &= 0 \\ 2\cos^2\theta + 3\cos\theta - 2 &= 0 \quad [\text{A1: the printed result}] \end{aligned}\]

**(b)** The question says "hence", so factorise the quadratic in \(\cos\theta\):

\[\begin{aligned} (2\cos\theta - 1)(\cos\theta + 2) &= 0 \quad [\text{M1}] \\ \cos\theta &= \tfrac12 \quad \text{or} \quad \cos\theta = -2 \end{aligned}\]

\(\cos\theta = -2\) has no solution, because \(-1 \le \cos\theta \le 1\) [B1] (say why it is rejected). From \(\cos\theta = \tfrac12\), \(\theta = 60^\circ\) [A1] and \(\theta = 360^\circ - 60^\circ = 300^\circ\) [A1].

*Why it earns the marks:* part (a) shows the identity used and arrives at the exact printed result. A common failure is to start from the answer and work back to \(2\sin^2\theta = 3\cos\theta\): "show that" needs the forward direction. Part (b) uses the form from (a), rejects the impossible root with a reason, and finds both solutions in the interval.
:::

## Method, accuracy and independent marks

A mark scheme has three kinds of mark.

- **M (method).** Awarded for using a correct method, even if you make an arithmetic slip. "M1" means one method mark.
- **A (accuracy).** Awarded for a correct answer or step, but **only if the method mark was earned**. An A mark cannot exist without the M mark before it. So a lucky correct answer with a wrong method scores nothing.
- **B (independent).** Awarded for a correct fact, result or statement that does not depend on a method, such as stating \(\cos 60^\circ = \tfrac12\) or giving a reason.

You will also meet these abbreviations in the mark schemes published with past papers.

| Abbreviation | Meaning | What it means for you |
|---|---|---|
| **cao** | correct answer only | the final answer must be right: no follow-through, no marks for a near-miss |
| **ft** | follow through | marks given for correct working from your own earlier wrong answer |
| **awrt** | answer which rounds to | e.g. awrt 2.09 allows 2.0945…, 2.094 or 2.09 |
| **oe** | or equivalent | any equivalent form of the answer scores, such as \(\tfrac{3}{6}\) for \(\tfrac12\) |
| **isw** | ignore subsequent working | once the correct answer appears, tidying it up (even wrongly) does not cost the mark |
| **dep** | dependent | the mark depends on the previous method mark |

:::eg How follow-through works
The line \(l\) passes through \((1, 2)\) and \((3, 8)\). **(a)** Find the equation of \(l\). [3 marks] **(b)** Find the \(x\)-coordinate of the point of \(l\) where \(y = 10\). [2 marks]

A student makes a slip in part (a) and writes the gradient as \(\dfrac{8 - 2}{3 - 1} = 2\) (it is 3). Then:

\[y - 2 = 2(x - 1) \quad\Rightarrow\quad y = 2x\]

*Part (a):* M1 for the gradient method, **A0** for the wrong gradient, and A0 for the wrong equation, because the line must be correct. The correct line is \(y = 3x - 1\).

*Part (b):* with their line, \(2x = 10\), so \(x = 5\). The method is right and uses the student's own equation, so the examiner awards **M1 and A1ft**. With the correct line \(3x - 1 = 10\) the answer is \(x = \tfrac{11}{3}\).

*Lesson:* one slip cost two marks in part (a), but part (b) was not wasted. This is why you should always attempt the later parts, even if you suspect an earlier answer is wrong. It is also why you must show each step: a bare "5" with no line shown has no method for the examiner to follow.
:::

## Accuracy

- **3 significant figures** for any non-exact answer, and **degrees to 1 decimal place**, unless the question says otherwise. If the exact answer is 5, writing 5.00 is fine, but 5.0001 is not required.
- **Work with more figures than you write.** Keep the full calculator value in the working, or at least 4 significant figures, and round only the final answer. Rounding to 3 s.f. in the middle can push the last digit of the final answer off by one, and an A mark can depend on that last digit.
- **Say which form you give.** If the question says "exact", give a surd such as \(3\sqrt2\), not 4.24. If it asks for "3 significant figures", give 4.24, not \(3\sqrt2\).
- **Units.** In Mechanics and Statistics, write units where they are needed: N, m s⁻¹, J, W. In a probability answer, a plain number between 0 and 1 is right.
- **Money, lengths and angles in context:** give a sensible number of figures and say what the answer means ("the car's speed is 12.4 m s⁻¹").

:::eg Exact means exact
Find the exact value of \(\displaystyle\int_0^{\pi/6} \cos 2x\,dx\). [3 marks]

\[\begin{aligned} \int_0^{\pi/6} \cos 2x\,dx &= \Big[\tfrac12 \sin 2x\Big]_0^{\pi/6} \quad [\text{M1 A1}] \\ &= \tfrac12 \sin\tfrac{\pi}{3} - \tfrac12 \sin 0 \\ &= \tfrac12 \times \tfrac{\sqrt3}{2} = \frac{\sqrt3}{4} \quad [\text{A1}] \end{aligned}\]

The last mark is for \(\dfrac{\sqrt3}{4}\) (or an equivalent exact form). The decimal 0.433 is correct but is not "exact", so it would lose the A mark. (The question did not ask for a decimal, so the calculator is not needed. If it did, you would still write the exact form first.)
:::

## Verify, state and sketch

**Verify** means substitute. To verify that \(x = 2\) is a root of \(x^3 - 2x - 4 = 0\), write

\[2^3 - 2(2) - 4 = 8 - 4 - 4 = 0\]

and finish with "so \(x = 2\) is a root". Both the arithmetic and the conclusion are marked. When asked to **state** something, write the answer only: extra working earns nothing and wastes time.

When you **sketch**, the marks are for the features, not the artistry. Draw and label:

1. both axes, with the intercepts as coordinates, for example \((0, 5)\) and \((3, 0)\);
2. the correct overall shape (parabola, cubic, exponential growth or decay, a trig wave over the stated interval);
3. turning points and asymptotes, with their equations, such as \(x = 2\) or \(y = 0\);
4. behaviour at both ends, so the curve does not just stop.

A neat curve with the wrong feature loses the mark; a rough curve with every feature labelled gains it.

## Laying out a long answer

Long questions (the final two of a mock paper) are worth the most and are the easiest to mark badly. Use this routine.

1. **Read the whole question first,** including every part. Later parts often give a hint about the first.
2. **Write the key formula or equation before you substitute.** "\(F = ma\)" or "\(\sin^2\theta + \cos^2\theta = 1\)" earns the M1 even if the arithmetic fails.
3. **One idea per line, equals signs in a column,** and give each result its label. Do not cross out working unless you replace it.
4. **Draw a diagram** for every geometry, vector and mechanics question. Mark all given values on it.
5. **Finish with a sentence** in context when the question is a word problem: "The particle is at rest at \(t = 4\) s."
6. **Check** with a quick estimate, a substitution back, or the sign of the answer. Where a check fails, you still have time to fix it.

If you run out of time on a part, write the first line of the method anyway. Method marks are awarded for a correct start.

:::exam Do not cross out unless you replace
If you cross out a solution and have no replacement, the examiner may mark the crossed-out work. If you cross it out and write a different solution, the replacement is marked. Do not rub out a partly correct answer to keep the page neat.
:::

:::tip The one-page habit
Keep a one-page list of your own most frequent lost marks (a missing \(+c\), a squared bracket, the wrong mode, a lost solution). Read it before every practice paper and every exam. The most valuable item on the list is the one you wrote last week.
:::

:::recap
- Command words decide what to write: "show that" needs every step from start to printed answer; "exact" bans decimals; "hence" means use the previous part; "state" needs no working.
- M marks are for method, A marks depend on the method, B marks are independent.
- "cao" means no follow-through; "ft" means your own earlier answer can be used; "awrt" accepts anything that rounds to the given figures.
- Give 3 s.f. and 1 d.p. for angles, working with full accuracy until the end.
- When you sketch, mark intercepts, turning points and asymptotes with coordinates and equations.
- Write the formula before the substitution, one idea per line, and a closing sentence in context.
- Always attempt later parts of a question, even if an earlier answer may be wrong.
:::

Next: [Paper 1 survival guide](#math.exam.p1)
