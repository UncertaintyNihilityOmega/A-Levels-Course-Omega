@chapter cs.recursion
@title Recursion
@level a2
@paper CAIE 9618 Papers 3 and 4
@time 5–7 hours
@summary A recursive subroutine solves a problem by calling itself on a smaller version of the same problem. You will learn its two essential features, write and trace recursive functions in pseudocode and Python, see how the call stack makes it work, and decide when recursion beats a loop.

:::why
Some problems are far easier to describe by a rule that uses itself: a folder holds files and more folders, a family tree holds people and their own family trees, a sorted list can be searched by searching half of it. Recursion is how a program follows such a rule, and Paper 3 asks you to trace recursive pseudocode, explain how the stack is used and say when recursion is a good choice. In Paper 4 you write recursive functions on a computer and test them.
:::

**Before you start**, you should be comfortable with functions and parameters from [Procedures, functions and parameters](#cs.procedures), and with stacks from [Text files, stacks, queues and linked lists](#cs.structures).

:::try Warm-up
Q: What does a function do that a procedure does not? (from [Procedures, functions and parameters](#cs.procedures))
A: A function returns a value to the place where it was called, so it is used inside an expression. A procedure does not return a value.
Q: Items are pushed onto a stack in the order 4, 9, 2. In what order are they popped? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: 2, 9, 4. A stack is last in, first out: the most recently pushed item is popped first.
Q: A function declares a local variable `Total`. Where can `Total` be used? (from [Procedures, functions and parameters](#cs.procedures))
A: Only inside that function, and each call of the function gets its own copy of it.
:::

## What recursion is

Ask a person in a queue how many people stand in front of them. They do not count the queue. They ask the person ahead: "How many are in front of you?", wait for the answer, and add one. That person asks the next, and so on. The first person in the queue, who has nobody ahead, answers 0 at once. Each answer then travels back down the queue, one more than the one before.

Nobody solved the whole problem. Each person solved a **smaller version of the same problem** and added one step. That is recursion.

:::def Recursion
A way of solving a problem in which a subroutine calls itself, each time with a smaller or simpler version of the problem, until a case is reached that can be answered directly.
:::

A subroutine that does this is a **recursive subroutine**. Here is the smallest useful example, a countdown. In pseudocode:

```pseudocode
PROCEDURE Launch(N : INTEGER)
   IF N = 0 THEN
      OUTPUT "Lift off!"
   ELSE
      OUTPUT N
      CALL Launch(N - 1)
   ENDIF
ENDPROCEDURE

CALL Launch(3)
```

The same in Python:

```python
def launch(n):
    if n == 0:
        print("Lift off!")
    else:
        print(n)
        launch(n - 1)


launch(3)
```

Output:

```output
3
2
1
Lift off!
```

`Launch(3)` outputs 3, then calls `Launch(2)`, which outputs 2 and calls `Launch(1)`, which outputs 1 and calls `Launch(0)`. That call outputs "Lift off!" and calls nothing, so the chain stops. The procedure calls itself, but with a smaller argument each time.

### The two essential features

A recursive subroutine that works has exactly two parts. Without either, it fails.

:::def Base case
The case in which a recursive subroutine can give its answer directly, without calling itself. It stops the recursion. It is also called the stopping condition.
:::

:::def General case
The case in which a recursive subroutine calls itself with a changed argument that is closer to the base case. It is also called the recursive case.
:::

:::key The essential features of recursion
1. A **base case** that is answered without another call.
2. A **general case** that calls the subroutine again with an argument that moves **towards** the base case.
3. Every possible argument must eventually reach the base case. If it cannot, the calls never stop.
:::

In `Launch`, the base case is `N = 0` and the general case outputs N and calls `Launch(N - 1)`. The argument falls by one each call, so it reaches 0.

:::analogy
Russian dolls: you open a doll and find a smaller doll inside, and open that, until you reach the smallest doll, which does not open. Opening a doll is the general case. The smallest doll that cannot be opened is the base case. A set of dolls with no smallest one would never end.
:::

## Writing recursive functions

A recursive function returns a value, and the value comes from combining the answer to the smaller problem with a little extra work. The easiest way to write one is to ask four questions in order.

:::key Writing a recursive function: four questions
1. **What is the smallest case?** Write it as the base case, and decide what it returns.
2. **What is the smaller problem?** The argument for the next call, for example `N - 1`, or a string without its first character.
3. **How do I build the answer?** Combine the value the smaller call returns with the current argument: `N * Factorial(N - 1)`.
4. **Does every call move towards the base case?** If not, it never stops.
:::

### Factorial

The factorial of a positive whole number \(n\), written \(n!\), is the product of all the whole numbers from 1 to \(n\). So \(4! = 4 \times 3 \times 2 \times 1 = 24\). It already has a recursive definition: \(n! = n \times (n-1)!\), and \(1! = 1\). The smallest case is \(1! = 1\) (and \(0! = 1\) by convention).

In pseudocode:

```pseudocode
FUNCTION Factorial(N : INTEGER) RETURNS INTEGER
   IF N <= 1 THEN
      RETURN 1
   ELSE
      RETURN N * Factorial(N - 1)
   ENDIF
ENDFUNCTION
```

The same in Python:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))
print(factorial(10))
```

Output:

```output
24
3628800
```

Read the general case slowly: `RETURN N * Factorial(N - 1)`. The function does not know the value of `Factorial(N - 1)` yet. It starts a new call, waits for its answer, multiplies by N and then returns. This waiting is what the call stack, later in this chapter, keeps track of.

:::eg Tracing Factorial(4)
Complete a table showing every call to `Factorial(4)`, what each call is waiting for and the value each returns.

Work in two directions. Going **down**, each call that is not the base case starts another call. Going **back up**, each call receives its answer and returns its own.

| Call | N | Base case? | What it does | Returns |
|---|---|---|---|---|
| Factorial(4) | 4 | no | waits for Factorial(3) | 4 × 6 = 24 |
| Factorial(3) | 3 | no | waits for Factorial(2) | 3 × 2 = 6 |
| Factorial(2) | 2 | no | waits for Factorial(1) | 2 × 1 = 2 |
| Factorial(1) | 1 | yes | answers directly | 1 |

The calls are made in the order 4, 3, 2, 1 (top to bottom of the table). The values are returned in the opposite order: 1, then 2, then 6, then 24. The call `Factorial(4)` is the first to start and the last to finish. Four calls are made in all.
:::

### Adding up a list

A recursive function can also work its way along a list. The smaller problem is "the list from the next position onwards". The base case is "no items left", which adds nothing.

In pseudocode, using the global array `Scores` with bounds 1 to 5, which holds 4, 8, 15, 16 and 23:

```pseudocode
FUNCTION SumFrom(Index : INTEGER) RETURNS INTEGER
   IF Index > 5 THEN
      RETURN 0
   ELSE
      RETURN Scores[Index] + SumFrom(Index + 1)
   ENDIF
ENDFUNCTION

OUTPUT SumFrom(1)
```

`SumFrom(1)` is \(4 + (8 + (15 + (16 + (23 + 0))))= 66\). The base case returns 0, the neutral value for adding. In Python the list is passed in, and the index counts from 0:

```python
scores = [4, 8, 15, 16, 23]


def sum_from(items, index):
    if index == len(items):
        return 0
    return items[index] + sum_from(items, index + 1)


print(sum_from(scores, 0))
```

Output:

```output
66
```

Here the argument moves **up** towards the base case (`index` rises to the length of the list) rather than down. That is fine: what matters is that each call gets closer.

### Powers, digits and strings

The same four questions solve many small problems.

**Power.** \(b^e = b \times b^{e-1}\), and \(b^0 = 1\).

```pseudocode
FUNCTION Power(Base : INTEGER, Exp : INTEGER) RETURNS INTEGER
   IF Exp = 0 THEN
      RETURN 1
   ELSE
      RETURN Base * Power(Base, Exp - 1)
   ENDIF
ENDFUNCTION
```

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


print(power(2, 10))
print(power(3, 4))
```

Output:

```output
1024
81
```

**Counting the digits of a whole number.** A number below 10 has one digit. Any other number has one more digit than the number you get by dropping its last digit, which is `N DIV 10`.

```pseudocode
FUNCTION CountDigits(N : INTEGER) RETURNS INTEGER
   IF N < 10 THEN
      RETURN 1
   ELSE
      RETURN 1 + CountDigits(N DIV 10)
   ENDIF
ENDFUNCTION
```

`CountDigits(48271)` calls `CountDigits(4827)`, then 482, 48 and 4: five calls, and the answer is 5. The Python version has the same shape, with `//` for DIV:

```python
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


print(count_digits(48271))
```

Output:

```output
5
```

**Reversing a string.** A string of length 0 or 1 is its own reverse. Otherwise, reverse everything after the first character, then put the first character on the end. `MID(S, 2, LENGTH(S) - 1)` is the string without its first character and `LEFT(S, 1)` is the first character.

```pseudocode
FUNCTION Reverse(S : STRING) RETURNS STRING
   IF LENGTH(S) <= 1 THEN
      RETURN S
   ELSE
      RETURN Reverse(MID(S, 2, LENGTH(S) - 1)) & LEFT(S, 1)
   ENDIF
ENDFUNCTION
```

```python
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


print(reverse("STACK"))
```

Output:

```output
KCATS
```

`Reverse("STACK")` is `Reverse("TACK") & "S"`, which is `(Reverse("ACK") & "T") & "S"`, and so on down to `Reverse("K")`, which is "K". The answer builds up as the calls return: "K", "KC", "KCA", "KCAT", "KCATS".

:::warn Return the result of the recursive call
The recursive call produces a value. If you write `Factorial(N - 1)` on a line of its own and then `RETURN N`, the value is thrown away and the function returns the wrong answer. A recursive function nearly always **returns** an expression that contains the recursive call: `RETURN N * Factorial(N - 1)`.
:::

:::warn A base case that is never reached
`Factorial(-3)` with the base case `IF N = 0` would call `Factorial(-4)`, `Factorial(-5)` and so on for ever, because the argument moves away from 0. Choose a base case that every allowed argument reaches, such as `N <= 1`, or check the input first.
:::

## Tracing recursive code

Paper 3 gives you recursive pseudocode and asks for "the value returned" or "the output". The method never changes.

:::steps
1. Write the first call with its argument.
2. Follow the code: if the base case is true, write what it returns. Otherwise write the new call, with its new argument, on the next row. Do **not** work out the answer yet.
3. Keep going until a base case is reached.
4. Work **back up**: the base case's value replaces the call that was waiting for it, and so on, one row at a time, until the first call has its value.
:::

:::eg Tracing a function with two parameters (exam style)
The function below is called with `Mystery(5, 3)`.

```pseudocode
FUNCTION Mystery(A : INTEGER, B : INTEGER) RETURNS INTEGER
   IF B = 0 THEN
      RETURN 0
   ELSE
      RETURN A + Mystery(A, B - 1)
   ENDIF
ENDFUNCTION
```

(a) Complete a table of the calls. [3 marks]

(b) State the value returned by `Mystery(5, 3)` and say what the function calculates. [2 marks]

(a) Only B changes, so the argument B moves from 3 towards the base case B = 0.

| Call | A | B | Base case? | Returns |
|---|---|---|---|---|
| Mystery(5, 3) | 5 | 3 | no | 5 + 10 = 15 |
| Mystery(5, 2) | 5 | 2 | no | 5 + 5 = 10 |
| Mystery(5, 1) | 5 | 1 | no | 5 + 0 = 5 |
| Mystery(5, 0) | 5 | 0 | yes | 0 |

The four calls in the correct order, with B falling from 3 to 0 [B1]. The base case identified at B = 0, returning 0 [B1]. The values returned working back up: 5, 10, 15 [B1].

(b) The value returned is 15 [B1]. The function calculates \(A \times B\) by adding A to itself B times, so it multiplies [B1].
:::

### When the output comes matters

A procedure can output before the recursive call, after it, or both. The order of the output changes completely, so always trace which line comes first.

```pseudocode
PROCEDURE CountDown(N : INTEGER)
   IF N > 0 THEN
      OUTPUT N
      CALL CountDown(N - 1)
   ENDIF
ENDPROCEDURE

PROCEDURE CountUp(N : INTEGER)
   IF N > 0 THEN
      CALL CountUp(N - 1)
      OUTPUT N
   ENDIF
ENDPROCEDURE
```

`CountDown` outputs **before** it calls itself, so the output is in the order the calls are made. `CountUp` outputs **after** the call returns, so the first output happens only when the deepest call has finished. In Python:

```python
def count_down(n):
    if n > 0:
        print(n)
        count_down(n - 1)


def count_up(n):
    if n > 0:
        count_up(n - 1)
        print(n)


count_down(3)
print("--")
count_up(3)
```

Output:

```output
3
2
1
--
1
2
3
```

The base case here is `N = 0`, and when it is reached the procedure does nothing at all. That is allowed: a base case does not have to return a value or output anything.

If a procedure outputs both before and after, the output goes down and then back up:

```python
def both(n):
    if n > 0:
        print("down", n)
        both(n - 1)
        print("up", n)


both(3)
```

Output:

```output
down 3
down 2
down 1
up 1
up 2
up 3
```

The `down` lines are printed as the calls are made (3, 2, 1). The `up` lines are printed as the calls finish, in the reverse order (1, 2, 3), because the call that started last finishes first. This reversal is the stack at work.

## The call stack

How does the computer remember that `Factorial(4)` is waiting for `Factorial(3)`, which is waiting for `Factorial(2)`? It uses a **stack**, the last in, first out structure from [Text files, stacks, queues and linked lists](#cs.structures). Every time a subroutine is called, a block of memory for that call is pushed onto the stack. When the call finishes, the block is popped.

:::def Call stack
The area of memory that holds the stack frames of the subroutine calls that have started but not yet finished. The newest call is on the top.
:::

:::def Stack frame
The block of memory pushed onto the call stack for one subroutine call. It holds the return address, the parameters and the local variables of that call.
:::

The **return address** is the place in the calling code where the program must carry on once this call finishes. For `Factorial(3)` called from `Factorial(4)`, it is the point in `Factorial(4)` where the answer is multiplied by 4.

Each call has **its own frame**, so it has its own copy of `N`. This is why recursion works: `Factorial(4)` has `N = 4` and `Factorial(3)` has `N = 3` at the same time. If all calls shared one memory location for `N`, the second call would overwrite the first call's value.

:::html
<figure class="fig small"><svg viewBox="0 0 344 330" role="img" aria-label="The call stack while Factorial(4) is running, drawn as four boxes with the newest on top. Top: Factorial(1), N = 1, base case, returns 1. Then Factorial(2), N = 2, waiting for Factorial(1), returns 2 × 1 = 2. Then Factorial(3), N = 3, waiting for Factorial(2), returns 3 × 2 = 6. Bottom: Factorial(4), N = 4, waiting for Factorial(3), returns 4 × 6 = 24."><text class="tl tb" x="8" y="18">Call stack, deepest point</text><rect class="f1 s-acc sw2" x="8" y="34" width="246" height="62" rx="4"/><text class="tl tb" x="18" y="53">Factorial(1)</text><text class="tl" x="18" y="71">N = 1: base case</text><text class="tl" x="18" y="89">returns 1</text><text class="tl" x="264" y="70">newest</text><rect class="fm s-acc sw2" x="8" y="102" width="246" height="62" rx="4"/><text class="tl tb" x="18" y="121">Factorial(2)</text><text class="tl" x="18" y="139">N = 2: waiting for Factorial(1)</text><text class="tl" x="18" y="157">returns 2 × 1 = 2</text><rect class="fm s-acc sw2" x="8" y="170" width="246" height="62" rx="4"/><text class="tl tb" x="18" y="189">Factorial(3)</text><text class="tl" x="18" y="207">N = 3: waiting for Factorial(2)</text><text class="tl" x="18" y="225">returns 3 × 2 = 6</text><rect class="fm s-acc sw2" x="8" y="238" width="246" height="62" rx="4"/><text class="tl tb" x="18" y="257">Factorial(4)</text><text class="tl" x="18" y="275">N = 4: waiting for Factorial(3)</text><text class="tl" x="18" y="293">returns 4 × 6 = 24</text><text class="tl" x="264" y="274">oldest</text><text class="tl" x="8" y="320">bottom of the stack: the first call</text></svg><figcaption>The stack when the base case of Factorial(4) runs: four frames, each with its own N. The frames below are waiting; each will receive its answer as the one above it is popped.</figcaption></figure>
:::

The figure shows the moment the base case runs. Follow the whole story:

1. `Factorial(4)` is called. A frame with `N = 4` is pushed.
2. It calls `Factorial(3)`. A new frame is pushed on top. The frame below waits.
3. The same happens for `Factorial(2)` and `Factorial(1)`. There are now four frames.
4. `Factorial(1)` meets the base case and returns 1. Its frame is **popped**, and the program jumps to the return address in `Factorial(2)`, which can now work out \(2 \times 1\).
5. Each frame in turn returns its value and is popped: 2, then 6, then 24. When the last frame is popped, the stack is empty and the program carries on after the original call.

:::def Unwinding
The stage of a recursive call in which the base case has been reached and the calls return one after another, each popping its frame and passing its value to the call below.
:::

The widget runs this story one step at a time for six built-in functions.

:::html
<div class="widget" data-w="cs-calls" data-fn="factorial" data-n="4"></div>
:::

Try this: step through `factorial` with N = 4 and watch the frames pile up, then pop. Switch to `countdown` (outputs before the call) and `countup` (outputs after it) with N = 3 and see why the output order differs. Choose `fib` with N = 4 and watch how often the call count rises.

### What happens when the base case is missing

The stack has a fixed size. A recursive subroutine with no base case, or one that never reaches it, keeps pushing frames until the stack is full.

:::def Stack overflow
An error that happens when the call stack runs out of memory, because too many calls have been made and not finished. It is caused by infinite recursion or by recursion that is too deep for the stack.
:::

Python protects itself by counting the depth of calls. Its default limit is 1000. When a program goes past it, Python raises `RecursionError` and the program can catch it. This example works down to a depth of 500, then fails at 5000:

```python
import sys


def depth(n):
    if n == 0:
        return 0
    return 1 + depth(n - 1)


print(sys.getrecursionlimit())
print(depth(500))
try:
    print(depth(5000))
except RecursionError:
    print("RecursionError: the stack is full")
```

Output:

```output
1000
500
RecursionError: the stack is full
```

`depth(5000)` has a base case and every call moves towards it, so it would work if the stack were larger. It fails because 5000 frames are too many. A stack overflow therefore has two causes: infinite recursion, and legitimate recursion that is too deep.

### What a compiler has to do

The programmer writes `RETURN N * Factorial(N - 1)` and the translator turns it into machine code. For recursion to work, the code it generates for every call must do these things.

:::key Translating a recursive call: what the compiler must generate
1. **Before the call:** push a new stack frame holding the return address (the instruction after the call), the values of the parameters, and space for the local variables.
2. **Jump** to the start of the subroutine, which now uses the data in its own frame.
3. **On return:** place the returned value where the caller can find it (for example in a register), **pop** the frame, and jump to the return address.
4. Local variables and parameters are found **relative to the top of the stack**, never at one fixed address, so that each call has its own copies.
:::

A compiler or interpreter that gave each variable one fixed memory address could not support recursion, because the second call would overwrite the first. Using a stack for frames is what allows a subroutine to call itself, and it also allows any chain of calls: a procedure that calls another that calls another is using the same stack. Recursion is only the case where the chain returns to the same subroutine. The stack of [Text files, stacks, queues and linked lists](#cs.structures) is the same stack that the processor uses for subroutine calls.

## Fibonacci and the cost of recursion

The Fibonacci numbers start 0, 1 and each later number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. The rule is already recursive, so the function is easy to write. It has **two** base cases (N = 0 and N = 1) and **two** recursive calls.

```pseudocode
FUNCTION Fib(N : INTEGER) RETURNS INTEGER
   IF N <= 1 THEN
      RETURN N
   ELSE
      RETURN Fib(N - 1) + Fib(N - 2)
   ENDIF
ENDFUNCTION
```

The figure shows every call made by `Fib(4)`.

:::html
<figure class="fig small"><svg viewBox="0 0 320 246" role="img" aria-label="The call tree of Fib(4), nine calls in all. Fib(4) calls Fib(3) and Fib(2). Fib(3) calls Fib(2) and Fib(1). Each Fib(2) calls Fib(1) and Fib(0). The two Fib(2) boxes are shaded because the same calculation is done twice; Fib(1) appears three times."><line class="ln-m" x1="179.2" y1="42.0" x2="109.5" y2="73.0"/><line class="ln-m" x1="179.2" y1="42.0" x2="249.0" y2="73.0"/><line class="ln-m" x1="109.5" y1="97.0" x2="63.0" y2="128.0"/><line class="ln-m" x1="109.5" y1="97.0" x2="156.0" y2="128.0"/><line class="ln-m" x1="63.0" y1="152.0" x2="32.0" y2="183.0"/><line class="ln-m" x1="63.0" y1="152.0" x2="94.0" y2="183.0"/><line class="ln-m" x1="249.0" y1="97.0" x2="218.0" y2="128.0"/><line class="ln-m" x1="249.0" y1="97.0" x2="280.0" y2="128.0"/><rect class="fm s-acc sw2" x="5.0" y="183.0" width="54" height="24" rx="4"/><text class="tl tc" x="32.0" y="200.0">Fib(1)</text><rect class="fm s-acc sw2" x="67.0" y="183.0" width="54" height="24" rx="4"/><text class="tl tc" x="94.0" y="200.0">Fib(0)</text><rect class="f1 s-acc sw2" x="36.0" y="128.0" width="54" height="24" rx="4"/><text class="tl tc" x="63.0" y="145.0">Fib(2)</text><rect class="fm s-acc sw2" x="129.0" y="128.0" width="54" height="24" rx="4"/><text class="tl tc" x="156.0" y="145.0">Fib(1)</text><rect class="fm s-acc sw2" x="82.5" y="73.0" width="54" height="24" rx="4"/><text class="tl tc" x="109.5" y="90.0">Fib(3)</text><rect class="fm s-acc sw2" x="191.0" y="128.0" width="54" height="24" rx="4"/><text class="tl tc" x="218.0" y="145.0">Fib(1)</text><rect class="fm s-acc sw2" x="253.0" y="128.0" width="54" height="24" rx="4"/><text class="tl tc" x="280.0" y="145.0">Fib(0)</text><rect class="f1 s-acc sw2" x="222.0" y="73.0" width="54" height="24" rx="4"/><text class="tl tc" x="249.0" y="90.0">Fib(2)</text><rect class="fm s-acc sw2" x="152.2" y="18.0" width="54" height="24" rx="4"/><text class="tl tc" x="179.2" y="35.0">Fib(4)</text><text class="tl tc" x="160" y="238">9 calls; shaded boxes repeat work</text></svg><figcaption>The call tree of Fib(4). The two shaded Fib(2) calls do exactly the same work, and Fib(1) is called three times.</figcaption></figure>
:::

A **call tree** shows one box per call, with lines to the calls it makes. The tree is a way of tracing: the leaves are base cases, and the value of every box is the sum of the two below it. Here `Fib(2) = 1 + 0 = 1`, so `Fib(3) = 1 + 1 = 2` and `Fib(4) = 2 + 1 = 3`.

The tree also shows the problem. `Fib(2)` is worked out twice, because nothing remembers the first answer. For larger N the repetition explodes. This program counts the calls:

```python
calls = 0


def fib(n):
    global calls
    calls = calls + 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for n in (4, 5, 10, 20):
    calls = 0
    value = fib(n)
    print("fib(" + str(n) + ") =", value, "calls:", calls)
```

Output:

```output
fib(4) = 3 calls: 9
fib(5) = 5 calls: 15
fib(10) = 55 calls: 177
fib(20) = 6765 calls: 21891
```

Each increase of N by 1 makes the number of calls grow by about 1.6 times. `fib(30)` makes 2 692 537 calls, and the number of calls for each N is more than the value of the Fibonacci number itself. Only 20 distinct values are needed to find `fib(20)`, but nearly 22 000 calls are made.

A loop does the same job in N steps, keeping only the last two values:

```python
def fib_loop(n):
    previous, current = 0, 1
    for i in range(n):
        previous, current = current, previous + current
    return previous


print(fib_loop(20), fib_loop(30))
```

Output:

```output
6765 832040
```

:::note Remembering answers (not needed for the exam)
A recursive function can also store each answer the first time it is found and reuse it. This is called memoisation. With a dictionary, `fib(20)` needs only 39 calls instead of 21 891:

```python
memory = {}
calls = 0


def fib_fast(n):
    global calls
    calls = calls + 1
    if n <= 1:
        return n
    if n not in memory:
        memory[n] = fib_fast(n - 1) + fib_fast(n - 2)
    return memory[n]


print(fib_fast(20), "calls:", calls)
```

Output:

```output
6765 calls: 39
```
:::

The lesson for the exam is simple: a recursive function that makes **two** or more recursive calls on overlapping problems can be very slow, and Paper 3 may ask you to say why.

## Recursion on searching and on trees

Recursion is at its best when the problem splits into smaller copies of itself. Two cases from [Searching, sorting and Big O](#cs.algorithms2) and [Abstract data types: stacks, queues, lists, trees and graphs](#cs.adts) are natural.

### Recursive binary search

A binary search looks at the middle item of a sorted list and then searches only one half. "Searching one half" is the same problem on a smaller list, so the search can be written recursively. The two parameters `Low` and `High` mark the part of the list still under consideration. If `Low > High`, nothing is left: that is the base case for "not found". The other base case is "the middle item is the target".

In pseudocode, with the global array `Codes` of bounds 1 to 10 holding 5, 9, 14, 20, 27, 33, 38, 44, 51, 60 in ascending order. The function returns the position of the target, or 0 if it is not there:

```pseudocode
FUNCTION BinarySearch(Low : INTEGER, High : INTEGER, Target : INTEGER) RETURNS INTEGER
   DECLARE Mid : INTEGER
   IF Low > High THEN
      RETURN 0
   ELSE
      Mid ← (Low + High) DIV 2
      IF Codes[Mid] = Target THEN
         RETURN Mid
      ELSE
         IF Codes[Mid] < Target THEN
            RETURN BinarySearch(Mid + 1, High, Target)
         ELSE
            RETURN BinarySearch(Low, Mid - 1, Target)
         ENDIF
      ENDIF
   ENDIF
ENDFUNCTION

OUTPUT BinarySearch(1, 10, 38)
```

Search for 38. Each call and what it does:

| Call | Low | High | Mid | Codes[Mid] | What happens |
|---|---|---|---|---|---|
| 1 | 1 | 10 | 5 | 27 | 27 < 38: search the upper half |
| 2 | 6 | 10 | 8 | 44 | 44 > 38: search the lower half |
| 3 | 6 | 7 | 6 | 33 | 33 < 38: search the upper half |
| 4 | 7 | 7 | 7 | 38 | found: return 7 |

Four calls are made and 7 is returned back through all four. Searching for 30, which is not in the list, runs `Low = 6`, `High = 5` after four calls and so returns 0. The same function in Python, with the list counting from 0 and `-1` meaning "not found":

```python
codes = [5, 9, 14, 20, 27, 33, 38, 44, 51, 60]


def binary_search(items, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return binary_search(items, mid + 1, high, target)
    return binary_search(items, low, mid - 1, target)


print(binary_search(codes, 0, len(codes) - 1, 38))
print(binary_search(codes, 0, len(codes) - 1, 30))
```

Output:

```output
6
-1
```

Index 6 in Python is position 7 in the pseudocode, because Python counts from 0. A list of \(n\) items needs at most about \(\log_2 n\) calls, so the stack stays shallow: a list of a million items needs at most 20 frames. That is why recursion is safe for divide and conquer.

### Recursion on a tree

A binary tree is a node with a left tree and a right tree, each of which is a node with its own two trees, or is empty. The structure is itself recursive, so recursion fits it better than a loop. The empty tree is the base case.

The pseudocode in [Abstract data types: stacks, queues, lists, trees and graphs](#cs.adts) writes this with arrays of pointers. Here is the same idea in Python, with a class `Node` as a record. `insert` adds a value to a binary search tree, and `in_order` returns the values in order. In-order means: the left tree first, then the node, then the right tree.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


root = None
for value in (40, 25, 60, 10, 30, 50, 70):
    root = insert(root, value)
print(in_order(root))
print(height(root))
```

Output:

```output
[10, 25, 30, 40, 50, 60, 70]
3
```

All three functions have the same shape: the base case is the empty tree (`None`), and the general case handles the node and makes one recursive call for each subtree. This is the pattern the Paper 4 tree task uses: one recursive call for the left side and one for the right.

## Recursion or iteration

Every recursive function can be written with a loop, and every loop can be written recursively. The choice is about which gives clearer, safer code.

| | Recursion | Iteration (a loop) |
|---|---|---|
| Code | often shorter and closer to the definition | often longer for tree-like problems |
| Memory | one stack frame per call: depth \(n\) uses space proportional to \(n\) | a few variables, however many repeats |
| Speed | slower, because each call has set-up and return work | faster |
| Risk | stack overflow if too deep or the base case is missing | an infinite loop if the condition never ends |
| Best for | trees, divide and conquer, naturally recursive rules | simple counting, totals, repeated steps |

:::key When recursion is a good choice
- The data or problem is **recursive by nature**: trees, folders inside folders, nested structures.
- The problem **splits into smaller copies** of itself (divide and conquer), as in binary search and merge-style algorithms.
- The recursion is **not very deep**, so stack space is not a worry.
- Clear, short code matters more than the last bit of speed or memory.
:::

Avoid recursion when a simple loop does the job (adding up numbers, counting), when the depth could be very large, and when the same sub-problems are repeated many times, as in `Fib`.

### Converting between the two

A recursive function that makes one call at the end converts to a loop by turning the parameter into a loop variable. In pseudocode, iterative `Factorial`:

```pseudocode
FUNCTION FactorialLoop(N : INTEGER) RETURNS INTEGER
   DECLARE Result, Count : INTEGER
   Result ← 1
   FOR Count ← 2 TO N
      Result ← Result * Count
   NEXT Count
   RETURN Result
ENDFUNCTION
```

In Python:

```python
def factorial_loop(n):
    result = 1
    for count in range(2, n + 1):
        result = result * count
    return result


print(factorial_loop(4), factorial_loop(10))
```

Output:

```output
24 3628800
```

The loop uses one result variable and no stack frames. Going the other way, from loop to recursion, follow this table.

| In the loop | In the recursive version |
|---|---|
| the loop variable | the parameter, changed in the recursive call |
| the loop condition ending the loop | the base case |
| the running total, started before the loop | the value returned by the base case, then combined on the way back |
| the body of the loop | the work done in the general case |

For example, the loop `FOR Count ← 1 TO N: Total ← Total + Count * Count` becomes `SumSquares(N)`: the base case `N = 0` returns 0, and the general case returns `N * N + SumSquares(N - 1)`.

A recursive function can also carry the running total as an extra parameter, called an **accumulator**. The answer is then complete at the base case, and no work remains after the recursive call.

```python
def factorial_acc(n, total):
    if n <= 1:
        return total
    return factorial_acc(n - 1, total * n)


print(factorial_acc(5, 1))
```

Output:

```output
120
```

Python still pushes a frame for every call here, so this does not remove the risk of overflow in Python. Some languages translate such a call into a jump so that the stack does not grow. You do not need that for the exam: only the idea that the answer is built on the way down instead of on the way back.

## Common mistakes

:::warn Three slips that cost marks
- **No base case, or one that is never reached.** The recursion never stops. Check that every allowed argument ends at the base case.
- **Ignoring the returned value.** `Factorial(N - 1)` on its own line does nothing useful. Return an expression that includes the call.
- **Output in the wrong order.** Output before the call comes out in call order; output after the call comes out in reverse. Trace both.
:::

:::exam Tracing and explaining
- **"State the value returned" / "State the output":** write the calls in a table, then work back up. Show the working: marks go to the sequence, not only the final value.
- **"Explain how the stack is used":** say that each call pushes a frame (return address, parameters, local variables), the frames pile up until the base case, the base case returns and its frame is popped, and the others are popped in reverse order as each returns its value.
- **"Explain why recursion may be unsuitable":** each call uses a stack frame, so deep recursion can cause a stack overflow, and it is slower than a loop.
:::

:::eg Spot the error: a function that ignores its own answer
Question: Write a recursive function `SumTo` that returns the sum of the whole numbers from 1 to N, for N ≥ 0. For example `SumTo(4)` returns 10. [4 marks]

A student wrote:

```pseudocode
01  FUNCTION SumTo(N : INTEGER) RETURNS INTEGER
02     IF N = 0 THEN
03        RETURN 0
04     ELSE
05        SumTo(N - 1)
06        RETURN N
07     ENDIF
08  ENDFUNCTION
```

Line 02 tests the base case N = 0 [B1]. Line 03 returns 0, the correct value for the sum of no numbers [B1]. Line 05 makes the recursive call with the argument N − 1, which moves towards the base case [B1]. **Line 06 returns N alone: the value returned by `SumTo(N - 1)` on line 05 is thrown away, so the function never adds the smaller sums. The last mark is lost** [B0]. The answer scores 3 out of 4.

To see the damage, trace `SumTo(3)`. It calls `SumTo(2)`, which calls `SumTo(1)`, which calls `SumTo(0)`. Each call returns its own N and ignores the answer below it, so `SumTo(3)` returns 3, not 6. The fix is to return the call: `RETURN N + SumTo(N - 1)`.
:::

:::try Start easy, finish at exam standard
Q: A programmer writes `FUNCTION Bad(N : INTEGER) RETURNS INTEGER` whose only statement is `RETURN N * Bad(N - 1)`. What is wrong with it?
A: It has no base case, so nothing stops the calls. It keeps calling itself until the stack overflows.
Q: What does `Factorial(6)` return, using the function in this chapter?
A: \(6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720\).
Q: How many calls to `Power` are made by `Power(2, 5)`, and what does it return?
A: Exp falls through 5, 4, 3, 2, 1 and 0, so six calls are made. It returns \(2^5 = 32\).
Q: The function `SumDigits(N)` is `IF N < 10 THEN RETURN N ELSE RETURN (N MOD 10) + SumDigits(N DIV 10)`. Trace `SumDigits(274)`.
A: `SumDigits(274)` is \(4 + \) `SumDigits(27)`. `SumDigits(27)` is \(7 + \) `SumDigits(2)`, and `SumDigits(2)` returns 2 (base case). Working back, 27 gives \(7 + 2 = 9\) and 274 gives \(4 + 9 = 13\). Three calls; the value is 13.
Q: What is output by `CALL Rise(4)`? `PROCEDURE Rise(N : INTEGER)`, `IF N > 0 THEN`, `CALL Rise(N - 1)`, `OUTPUT N * N`, `ENDIF`, `ENDPROCEDURE`.
A: The output comes after the call, so the squares appear from the deepest call upwards: 1, 4, 9, 16.
Q: What does this Python print? `def f(n):` then `if n == 0:` `return ""` then `return str(n) + f(n - 1)`, called as `print(f(4))`.
A: `f(4)` is "4" + `f(3)`, which is "3" + `f(2)`, and so on, ending with "" for `f(0)`. It prints `4321`.
Q: Factorial(5) is running its base case. How many stack frames are on the stack, counting the frame of the base case?
A: Five: one each for N = 5, 4, 3, 2 and 1.
Q: Write a recursive function `Stars(N)` that returns a string of N asterisks, for example `Stars(4)` returns `"****"`. The function is called with N ≥ 0.
A: The smallest case is no stars, an empty string. Otherwise one star is joined to the string of N − 1 stars.

```pseudocode
FUNCTION Stars(N : INTEGER) RETURNS STRING
   IF N = 0 THEN
      RETURN ""
   ELSE
      RETURN "*" & Stars(N - 1)
   ENDIF
ENDFUNCTION
```

Q: This loop totals the squares of 1 to N. Rewrite it as a recursive Python function `sum_squares(n)` and give the value of `sum_squares(4)`. `total = 0`, then `for i in range(1, n + 1):`, then `total = total + i * i`.
A: The loop variable becomes the parameter, the end of the loop becomes the base case `n == 0`, and each call adds `n * n` to the sum of the squares below it.

```python
def sum_squares(n):
    if n == 0:
        return 0
    return n * n + sum_squares(n - 1)


print(sum_squares(4))
```

The value is \(16 + 9 + 4 + 1 = 30\).

```output
30
```

Q: Give one reason why a loop may be preferred to recursion for adding up the numbers 1 to 100 000.
A: Recursion would need 100 000 stack frames, which would overflow the stack (and uses more memory and time). A loop needs only a total and a counter.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State two essential features of a recursive subroutine.
A: One mark for each feature:

- a base case (stopping condition) that is answered without calling the subroutine again [B1]
- a general case that calls the subroutine with a changed argument that moves towards the base case [B1]

Q: [3 marks] ★★ The function below is called with `Collect(6)`.

```pseudocode
FUNCTION Collect(N : INTEGER) RETURNS INTEGER
   IF N = 0 THEN
      RETURN 0
   ELSE
      IF (N MOD 2) = 0 THEN
         RETURN N + Collect(N - 1)
      ELSE
         RETURN Collect(N - 1)
      ENDIF
   ENDIF
ENDFUNCTION
```

State the value returned, and the total number of calls made, with a reason for each.
H: Even values of N add N; odd values add nothing but still make a call.
H: N goes 6, 5, 4, 3, 2, 1, 0: the call with N = 0 is a call too.
A: Trace the argument of every call.

- the even values 6, 4 and 2 are added and the odd values add nothing, so the value returned is 12 [B1]
- the calls have N = 6, 5, 4, 3, 2, 1 and 0 [B1]
- so seven calls are made, the last being the base case [B1]

Q: [4 marks] ★★ The procedure below is called with `CALL Echo(5)`. State the output.

```pseudocode
PROCEDURE Echo(N : INTEGER)
   IF N > 1 THEN
      OUTPUT N
      CALL Echo(N - 2)
      OUTPUT N
   ELSE
      OUTPUT "end"
   ENDIF
ENDPROCEDURE
```

H: Write each call: Echo(5), then Echo(3), then Echo(1).
H: The second OUTPUT runs only after the call below it has returned.
A: The calls are `Echo(5)`, `Echo(3)` and `Echo(1)`. The output is, one item per line: 5, 3, end, 3, 5.

- 5 output first, before the recursive call [B1]
- 3 output second [B1]
- "end" output by the base case (N = 1) [B1]
- 3 then 5 output on the way back, after the calls return, in that order [B1]

Q: [4 marks] ★★ Explain how the call stack is used when `Power(2, 3)` is called, using the `Power` function in this chapter.
A: The marks are for the stack behaviour, with the function's values.

- each call pushes a stack frame holding the return address, the parameters (Base and Exp) and any local variables [B1]
- the calls `Power(2, 3)`, `Power(2, 2)`, `Power(2, 1)` and `Power(2, 0)` are pushed in turn, so there are four frames at the deepest point [B1]
- `Power(2, 0)` meets the base case and returns 1, and its frame is popped [B1]
- each remaining frame is popped as it returns (2 × 1 = 2, 2 × 2 = 4, 2 × 4 = 8), most recent first, and the last value, 8, is returned to the calling program [B1]

Q: [6 marks] ★★ Write a recursive function `HalveCount` in pseudocode that takes an integer N ≥ 1 and returns the number of times N can be halved with `DIV 2` before the result is 1 or less. For example `HalveCount(8)` returns 3. State the value returned by `HalveCount(40)`.
H: What is the answer when N is already 1?
H: One halving, plus the number of halvings of `N DIV 2`.
A: One possible answer:

```pseudocode
FUNCTION HalveCount(N : INTEGER) RETURNS INTEGER
   IF N <= 1 THEN
      RETURN 0
   ELSE
      RETURN 1 + HalveCount(N DIV 2)
   ENDIF
ENDFUNCTION
```

- function header with an integer parameter and `RETURNS INTEGER` [B1]
- base case `N <= 1` that returns 0 without calling the function [B1]
- recursive call using `N DIV 2` as the argument [B1]
- adds 1 to the value returned by the call [B1]
- the value of the call is returned (`RETURN`) in the general case [B1]
- `HalveCount(40)` returns 5, because 40, 20, 10, 5, 2, 1 take five halvings [B1]

Q: [8 marks] ★★★ A text-messaging app checks whether a word is a palindrome (it reads the same forwards and backwards, such as "noon"). (a) Write a recursive Python function `is_palindrome(text)` that returns `True` or `False`. (b) Write three calls that test it, one with an odd-length palindrome, one with an even-length palindrome and one that is not a palindrome, and give the output of each.
H: A string of 0 or 1 characters is a palindrome.
H: Otherwise the first and last characters must match, and the characters between them must be a palindrome. `text[1:-1]` is the string without its first and last characters.
H: Return the result of the recursive call; do not print it.
A: One possible answer:

```python
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


print(is_palindrome("level"))
print(is_palindrome("noon"))
print(is_palindrome("stack"))
```

```output
True
True
False
```

- base case: a string of length 0 or 1 returns `True` [B1]
- compares the first and last characters [B1]
- returns `False` when they differ [B1]
- recursive call on the string without its first and last characters [B1]
- the result of the recursive call is returned [B1]
- three test calls of the three required kinds [B1]
- correct output for the odd-length and even-length palindromes (`True`, `True`) [B1]
- correct output for the non-palindrome (`False`) [B1]

Q: [4 marks] ★★ A programmer can write a program to process the folders on a disk either recursively or with a loop. Give two advantages and two disadvantages of using recursion.
A: Any two advantages and two disadvantages:

- shorter and clearer code, because folders inside folders are a recursive structure [B1]
- fits divide and conquer, so the code follows the definition and is easier to check [B1]
- each call uses a stack frame, so a deep set of folders needs a lot of memory [B1]
- very deep recursion can cause a stack overflow, and calls are slower than a loop [B1]

Q: [6 marks] ★★★ A staircase can be climbed taking one or two steps at a time. The function below returns the number of different ways to climb N steps.

```pseudocode
FUNCTION Ways(N : INTEGER) RETURNS INTEGER
   IF N <= 1 THEN
      RETURN 1
   ELSE
      RETURN Ways(N - 1) + Ways(N - 2)
   ENDIF
ENDFUNCTION
```

(a) State the value returned by `Ways(4)`. [2] (b) State how many calls to `Ways` are made when `Ways(4)` is called. [2] (c) Explain why `Ways(40)` would be very slow, and give one way to make it faster. [2]
H: Draw the call tree, as for `Fib(4)`. The base cases return 1.
H: `Ways(2)` is the sum `Ways(1) + Ways(0)`.
A: Work out the small values first: `Ways(0) = 1`, `Ways(1) = 1`, `Ways(2) = 2`, `Ways(3) = 3`.

- `Ways(4) = Ways(3) + Ways(2)` [B1]
- \(3 + 2 = 5\) [B1]
- calls: `Ways(4)`, `Ways(3)`, `Ways(2)`, `Ways(1)`, `Ways(0)`, `Ways(1)`, `Ways(2)`, `Ways(1)`, `Ways(0)` [B1]
- so 9 calls in all [B1]
- the same values are worked out again and again (for example `Ways(2)` twice), so the number of calls grows very fast as N rises [B1]
- store the answers already found and reuse them (memoisation), or use a loop [B1]
:::

:::try Stretch for A*
Q: [7 marks] ★★★ `Power(Base, Exp)` in this chapter makes \(\text{Exp} + 1\) calls. A faster function uses \(b^e = (b^{e/2})^2\) when \(e\) is even. (a) Write a recursive pseudocode function `FastPower(Base, Exp)` that uses this, and `Base * FastPower(Base, Exp - 1)` when Exp is odd. (b) List the values of Exp in the calls made by `FastPower(2, 10)` and say how many calls there are.
H: When Exp is even, make **one** call with `Exp DIV 2`, store the answer, and multiply it by itself. Two calls would undo the saving.
H: When Exp is odd, subtract 1 to make it even.
A: One possible answer:

```pseudocode
FUNCTION FastPower(Base : INTEGER, Exp : INTEGER) RETURNS INTEGER
   DECLARE Half : INTEGER
   IF Exp = 0 THEN
      RETURN 1
   ELSE
      IF (Exp MOD 2) = 0 THEN
         Half ← FastPower(Base, Exp DIV 2)
         RETURN Half * Half
      ELSE
         RETURN Base * FastPower(Base, Exp - 1)
      ENDIF
   ENDIF
ENDFUNCTION
```

- base case `Exp = 0` returns 1 [B1]
- even case: one call with `Exp DIV 2`, the answer stored and squared [B1]
- odd case: `Base * FastPower(Base, Exp - 1)` [B1]
- the choice between even and odd made with `MOD 2` [B1]
- Exp values: 10, 5, 4, 2, 1, 0 [B1]
- six calls (against 11 for the simple `Power`) [B1]
- the answer returned is 1024 [B1]

The same function in Python, counting the calls:

```python
calls = 0


def fast_power(base, exp):
    global calls
    calls = calls + 1
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = fast_power(base, exp // 2)
        return half * half
    return base * fast_power(base, exp - 1)


print(fast_power(2, 10), "calls:", calls)
```

```output
1024 calls: 6
```

The depth of the recursion is about \(\log_2\) of the exponent, so this version can find \(2^{1000}\) with a handful of frames, where the simple version would need 1000.

Q: [7 marks] ★★★ In the puzzle Tower of Hanoi, N discs of different sizes sit on a peg. They must be moved to another peg, one disc at a time, never placing a bigger disc on a smaller one, using a third peg as a spare. To move N discs: move N − 1 discs to the spare peg, move disc N to the target peg, then move the N − 1 discs from the spare peg onto the target. (a) Write a recursive procedure `Hanoi(N, Source, Target, Spare)` that outputs each move as, for example, "Move disc 1 from A to B". (b) State the output of `CALL Hanoi(2, "A", "C", "B")`. (c) State the number of moves needed for 5 discs.
H: The base case is "no discs": do nothing.
H: Moving N − 1 discs is the same problem, with the roles of the pegs changed.
H: Each extra disc doubles the moves and adds one: 1, 3, 7, 15 …
A: One possible answer:

```pseudocode
PROCEDURE Hanoi(N : INTEGER, Source : STRING, Target : STRING, Spare : STRING)
   IF N > 0 THEN
      CALL Hanoi(N - 1, Source, Spare, Target)
      OUTPUT "Move disc ", N, " from ", Source, " to ", Target
      CALL Hanoi(N - 1, Spare, Target, Source)
   ENDIF
ENDPROCEDURE
```

- the procedure does nothing when N is 0 (the base case; `IF N > 0`) [B1]
- first recursive call moves N − 1 discs from Source to Spare [B1]
- outputs the move of disc N from Source to Target between the two calls [B1]
- second recursive call moves N − 1 discs from Spare to Target [B1]
- for `Hanoi(2, "A", "C", "B")`: "Move disc 1 from A to B", then "Move disc 2 from A to C" [B1]
- and finally "Move disc 1 from B to C" [B1]
- 5 discs need \(2^5 - 1 = 31\) moves [B1]

The same procedure in Python, run for three discs, shows seven moves (\(2^3 - 1\)):

```python
def hanoi(n, source, target, spare):
    if n > 0:
        hanoi(n - 1, source, spare, target)
        print("Move disc", n, "from", source, "to", target)
        hanoi(n - 1, spare, target, source)


hanoi(3, "A", "C", "B")
```

```output
Move disc 1 from A to C
Move disc 2 from A to B
Move disc 1 from C to B
Move disc 3 from A to C
Move disc 1 from B to A
Move disc 2 from B to C
Move disc 1 from A to C
```
:::

:::quiz
? What does the base case of a recursive subroutine do?
- It calls the subroutine with a larger argument.
+ It gives an answer directly, without another recursive call, and so stops the recursion.
- It counts how many calls have been made.
- It pops the stack frames.
> The base case is the stopping condition. Without it, or if it is never reached, the subroutine calls itself until the stack overflows.
? `PROCEDURE Show(N)` is `IF N > 0 THEN`, `CALL Show(N - 1)`, `OUTPUT N`, `ENDIF`. What does `CALL Show(3)` output?
- 3, 2, 1
- 3
+ 1, 2, 3
- 0, 1, 2, 3
> The output comes after the recursive call, so the first value output is from the deepest call that does anything: N = 1. The calls then finish in the order 1, 2, 3. Outputting before the call would give 3, 2, 1.
? Which items are held in a stack frame?
- only the value that the call returns
+ the return address, the parameters and the local variables of the call
- the whole program code
- the values of every other call
> Each frame holds the data for one call: where to resume, its own arguments and its own local variables. The returned value is passed back as the frame is popped.
? How many calls are made by `Factorial(5)`, using `IF N <= 1 THEN RETURN 1 ELSE RETURN N * Factorial(N - 1)`?
- 4
+ 5
- 6
- 120
> The calls have N = 5, 4, 3, 2 and 1, so five calls. The answer 120 is the value returned, not the number of calls; 4 forgets the call with N = 1, and 6 adds a call with N = 0 that is never made.
? A recursive Python function has no base case. What happens when it is called?
- It returns 0.
- It runs once and stops.
+ Python raises a RecursionError when the depth limit is passed.
- It loops for ever without using memory.
> Every call needs a new stack frame, so the stack fills. In Python the interpreter notices when the depth passes its limit (1000 by default) and raises RecursionError. In other languages the result is a stack overflow.
? For which problem is recursion the best fit?
- adding up the numbers 1 to 100 000
- counting how many times a key is pressed
+ visiting every node of a binary tree
- repeating a message ten times
> A binary tree is made of smaller trees, so one recursive call for each side matches its structure. The other jobs are simple counting that a loop does using less memory.
? Why is a recursive `Fib(30)` slow?
- Because Fibonacci numbers are very large.
- Because the stack frames are big.
+ Because it works out the same smaller values again and again: it makes 2 692 537 calls.
- Because Python is slow at addition.
> Each call to `Fib(N)` makes two calls, and the calls overlap: `Fib(2)` is worked out many times. The number of calls grows by about 1.6 times for each increase of N. The numbers themselves are small (832 040).
? What happens during unwinding?
- The program starts again from the first call.
- New frames are pushed for every parameter.
+ Each call returns its value to the call below, popping its frame, starting from the base case.
- The stack is emptied at once.
> After the base case, the calls finish one after another, newest first. Each one receives the value from the call it was waiting for, uses it, and returns its own.
:::

:::checklist What you can now do
- [ ] I can state the essential features of recursion: a base case and a general case that moves towards it.
- [ ] I can write a recursive function in pseudocode and in Python for a numerical, string or list problem.
- [ ] I can trace a recursive function with a table of calls and returned values, and with a call tree.
- [ ] I can state the output of a recursive procedure that outputs before or after its recursive call.
- [ ] I can explain how the call stack and stack frames (return address, parameters, local variables) make recursion work, and what unwinding is.
- [ ] I can explain what causes a stack overflow and what a compiler must do to translate recursive code.
- [ ] I can say why a naive recursive Fibonacci is slow.
- [ ] I can write recursive binary search and tree traversals.
- [ ] I can decide when recursion is better than iteration and convert simple functions between the two.
:::

:::recap
- Recursion: a subroutine that calls itself on a smaller problem. It needs a **base case** (answered directly) and a **general case** (calls itself, moving towards the base case).
- To write one: smallest case first, then the smaller problem, then how to build the answer, then check that every call moves towards the base case. Return the value of the call.
- Trace with a table of calls going down and values coming back up. Output before the call comes out in call order; output after the call comes out in reverse.
- The **call stack** holds one **stack frame** (return address, parameters, local variables) for each unfinished call. The base case returns, then the frames are popped in reverse order: **unwinding**.
- Too many frames, or no base case, gives a **stack overflow** (in Python, `RecursionError`, default limit 1000).
- A compiler must push a frame (return address, parameters, local space) before a call and pop it on return, finding variables relative to the top of the stack.
- A naive recursive Fibonacci repeats work: 9 calls for `Fib(4)`, 177 for `Fib(10)`, 21 891 for `Fib(20)`.
- Use recursion for trees and divide and conquer; use a loop for simple repetition, deep recursion and repeated overlapping calls.
:::

:::links
- practise: [Recursion: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/19-computational-thinking-and-problem-solving-/recursion/exam-questions/) · Save My Exams · 9618-style recursion questions with mark schemes [paid]
- explore: [Recursion animations](https://visualgo.net/en/recursion) · VisuAlgo · watch the call tree grow and the stack frames pile up
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste a recursive function from this chapter and watch the frames appear and disappear
- read: [Algorithms: recursion](https://www.khanacademy.org/computing/computer-science/algorithms) · Khan Academy · a second explanation, with factorial and palindromes
- practise: [Exercism: Python track](https://exercism.org/tracks/python) · Exercism · free exercises, several of which suit recursion

Links checked 13 November 2026.
:::

Next: [Object-oriented programming](#cs.oop)
