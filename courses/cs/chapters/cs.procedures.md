@chapter cs.procedures
@title Procedures, functions and parameters
@level as
@paper CAIE 9618 Paper 2 (and Paper 4 at A Level)
@time 6–8 hours
@summary Large programs are built from small named modules. You will learn to write procedures and functions, pass values in by value or by reference, tell local variables from global ones, and write the "write a function that …" answers that Paper 2 asks for, in pseudocode and in Python.

:::why
Every long Paper 2 question is really several short modules: one that validates a code, one that counts matching records, one that converts a date. Examiners award marks for the header, for each parameter, for the RETURN and for the way you call the module, so a student who can write modules cleanly collects marks that others lose on layout alone. The same skills are what Paper 4 asks you to type as real Python functions.
:::

**Before you start**, you should be able to use arrays, records and loops from [Data types, records and arrays](#cs.datatypes), and the string functions from [Programming from zero](#cs.f.basics) and [Programming basics: variables, selection and loops](#cs.programming).

:::try Warm-up
Q: `DECLARE Marks : ARRAY[1:8] OF INTEGER`. What is the index of the last element, and how many elements are there? (from [Data types, records and arrays](#cs.datatypes))
A: The upper bound is 8, so the last element is `Marks[8]`, and there are \(8 - 1 + 1 = 8\) elements.
Q: What does `MID("ABCDEFGH", 2, 3)` return? (from [Programming from zero](#cs.f.basics))
A: `"BCD"`: three characters starting at position 2.
Q: Why does swapping `Values[J]` and `Values[J + 1]` need a temporary variable? (from [Data types, records and arrays](#cs.datatypes))
A: The first assignment overwrites one of the two values, so the original must be stored before it is lost.
:::

:::note How code appears in this course
Pseudocode follows the Cambridge Pseudocode Guide for 2027–2029: keywords in capitals, `←` for assignment, three-space indents. The sentence before each code block says which language it is. A block introduced by "Output:" shows exactly what the program prints. Every Python example in this chapter has been run to check its output.
:::

## Why programs are split into modules

Imagine a canteen in Accra that sells meals all day. If one person did the cooking, the serving, the cleaning and the accounts, nothing would be done well, and nobody else could help. A real canteen has jobs: a cook, a cashier, a cleaner. Each job has a name and a purpose, and a new worker can be told "you are the cashier" without learning everything else.

A program works the same way. Instead of one long list of statements, you write small, named pieces of code and then use them as often as you like. This is called **modular programming**, and it follows directly from the decomposition you met in [Computational thinking and algorithms](#cs.algorithms): break a problem into smaller problems, solve each one, then combine them.

:::def Module
A named, self-contained section of a program that does one job. In Cambridge pseudocode a module is a procedure or a function.
:::

Using modules gives five benefits, and Paper 2 questions ask you to state them.

- **Reuse.** Write the code once and call it from many places. If the same check is needed in six places, you do not write it six times.
- **Easier testing.** A small module can be tested on its own with a few inputs before it is joined to the rest.
- **Teamwork.** Different programmers can write different modules at the same time, provided they agree what each module takes in and gives back.
- **Readability.** `CALL PrintReceipt(...)` says what happens. Fifteen lines of OUTPUT statements do not.
- **Easier maintenance.** To change how a code is validated, you change one module, not every place where the check was copied.

Cambridge pseudocode has two kinds of module. A **procedure** does a job. A **function** does a job and also gives a value back. The next sections take them in turn.

## Procedures

A procedure is the simplest module: a group of statements with a name. To run it you write its name after the keyword CALL.

:::def Procedure
A named module that carries out a task when it is called. It may take parameters, but it does not return a value.
:::

:::def Call
The statement that runs a module. When a procedure finishes, the program carries on with the statement after the call.
:::

In pseudocode, a procedure that takes no parameters is defined with empty brackets, and called with `CALL` and empty brackets. A café in Accra prints its menu in several places, so the menu is a procedure.

```pseudocode
PROCEDURE ShowMenu()
   OUTPUT "1. Order a drink"
   OUTPUT "2. Order food"
   OUTPUT "3. Pay"
ENDPROCEDURE

OUTPUT "Welcome to the Accra Cafe"
CALL ShowMenu()
OUTPUT "Choose an option"
```

Output:

```output
Welcome to the Accra Cafe
1. Order a drink
2. Order food
3. Pay
Choose an option
```

The definition between `PROCEDURE` and `ENDPROCEDURE` does nothing by itself. It only tells the computer what `ShowMenu` means. The program starts at the first statement that is outside any module (the main program), runs `OUTPUT "Welcome …"`, reaches `CALL ShowMenu()`, jumps into the procedure, runs its three OUTPUT lines, and returns to the statement after the call.

:::html
<figure class="fig small"><svg viewBox="0 0 340 292" role="img" aria-label="A call and return diagram drawn top to bottom. The main program box lists: Side ← 5, then CALL Square(Side) highlighted, then OUTPUT Done. An arrow labelled 1: N ← 5 goes down from the CALL line to a procedure box headed 2: the procedure runs, which lists PROCEDURE Square(N : INTEGER), OUTPUT N * N and ENDPROCEDURE. An arrow labelled 3: return goes back up from the procedure to the main program, to the statement after the call, OUTPUT Done."><text class="tl tb" x="20" y="16">Main program</text><rect class="fm s-acc sw2" x="20" y="24" width="300" height="96"/><text class="tl" x="32" y="50">Side ← 5</text><rect class="f1" x="24" y="62" width="292" height="24"/><text class="tl" x="32" y="79">CALL Square(Side)</text><text class="tl" x="32" y="108">OUTPUT "Done"</text><rect class="fm s-acc sw2" x="20" y="170" width="300" height="108"/><text class="tl tb" x="32" y="192">2: the procedure runs</text><text class="tl" x="32" y="218">PROCEDURE Square(N : INTEGER)</text><text class="tl" x="56" y="242">OUTPUT N * N</text><text class="tl" x="32" y="266">ENDPROCEDURE</text><line class="c1 sw2" x1="170" y1="86" x2="170" y2="166" marker-end="url(#ah)"/><text class="tl" x="178" y="140">1: N ← 5</text><line class="c2 sw2" x1="290" y1="168" x2="290" y2="104" marker-end="url(#ah)"/><text class="tl te" x="282" y="160">3: return</text></svg><figcaption>A procedure call. The highlighted statement passes the value 5 to the procedure, the procedure runs its statements (step 2), and control then returns to the statement after the call.</figcaption></figure>
:::

:::key Procedure in pseudocode
- Define: `PROCEDURE <identifier>()` for no parameters, or `PROCEDURE <identifier>(<name> : <type>, …)` for parameters, then the statements, then `ENDPROCEDURE`.
- Call: `CALL <identifier>()` or `CALL <identifier>(<value>, …)`. A call is a complete statement on its own line.
- Define a module before the main program uses it, or follow the order the question gives.
:::

In Python the keyword is `def`, the body is indented, and a call is just the name with brackets. Python has no separate "procedure": it is a function that does not return a value.

```python
def show_menu():
    print("1. Order a drink")
    print("2. Order food")
    print("3. Pay")


print("Welcome to the Accra Cafe")
show_menu()
print("Choose an option")
```

Output:

```output
Welcome to the Accra Cafe
1. Order a drink
2. Order food
3. Pay
Choose an option
```

Python names follow `snake_case` (`show_menu`); pseudocode names use PascalCase (`ShowMenu`).

## Parameters and arguments

`ShowMenu` prints the same text every time. Most jobs depend on data: print a ticket for *this* passenger, not for nobody. A **parameter** is a slot in the module's header that receives a value each time the module is called.

:::def Parameter
A variable named in the header of a module that receives a value when the module is called. It is used like a local variable inside the module.
:::

:::def Argument
The actual value (or variable) given in the call, which is passed to the matching parameter.
:::

The two words are easy to mix up. The **parameter** is in the *definition* (`Seats : INTEGER`). The **argument** is in the *call* (`3`). The guide says the arguments must be of the correct data type and in the same sequence as the parameters in the definition.

```pseudocode
PROCEDURE PrintTicket(Name : STRING, Seats : INTEGER, Price : REAL)
   DECLARE Total : REAL
   Total ← Seats * Price
   OUTPUT "Ticket for ", Name
   OUTPUT Seats, " seats at ", Price, " each: ", Total
ENDPROCEDURE

CALL PrintTicket("Wanjiru", 3, 12.5)
```

Output:

```output
Ticket for Wanjiru
3 seats at 12.5 each: 37.5
```

When the call runs, `Name` becomes `"Wanjiru"`, `Seats` becomes 3 and `Price` becomes 12.5, in that order. Total is declared inside the procedure, so it exists only while the procedure runs. Swapping the arguments, as in `CALL PrintTicket(3, "Wanjiru", 12.5)`, is an error: a number is given where a STRING is expected.

:::warn Order and type must match
Arguments are matched to parameters by **position**, not by name. `CALL PrintTicket("Wanjiru", 12.5, 3)` has the right types in the wrong order: 12.5 is not a whole number of seats. Check the count, the order and the types of every argument against the header.
:::

The same procedure in Python needs no types:

```python
def print_ticket(name, seats, price):
    total = seats * price
    print("Ticket for", name)
    print(seats, "seats at", price, "each:", total)


print_ticket("Wanjiru", 3, 12.5)
```

Output:

```output
Ticket for Wanjiru
3 seats at 12.5 each: 37.5
```

An argument can be a literal (`3`), a variable (`Seats`) or any expression (`Adults + Children`). The expression is worked out first and its value is passed.

## Passing parameters: by value and by reference

What happens if the procedure changes a parameter? The answer depends on **how** the value was passed. Cambridge pseudocode has two ways, chosen with a keyword in front of the parameter in the header.

:::def Passing by value (BYVAL)
The procedure receives a **copy** of the argument's value. Changing the parameter inside the module does not change the variable in the calling code.
:::

:::def Passing by reference (BYREF)
The procedure receives a **reference to the original variable**, so the parameter is another name for it. Changing the parameter changes the variable in the calling code. The argument must therefore be a variable.
:::

If the keyword is missing, the guide says to assume the parameter is passed by value. The guide also says that if several parameters use the same method, the keyword need not be repeated; this course writes it every time, which is always correct.

Here are the same two lines of code, once by value and once by reference. A quiz game keeps a player's score in `Points`.

```pseudocode
PROCEDURE AddBonusCopy(BYVAL Score : INTEGER)
   Score ← Score + 10
   OUTPUT "Inside: ", Score
ENDPROCEDURE

PROCEDURE AddBonus(BYREF Score : INTEGER)
   Score ← Score + 10
   OUTPUT "Inside: ", Score
ENDPROCEDURE

DECLARE Points : INTEGER
Points ← 40
CALL AddBonusCopy(Points)
OUTPUT "After copy: ", Points
CALL AddBonus(Points)
OUTPUT "After reference: ", Points
```

Output:

```output
Inside: 50
After copy: 40
Inside: 50
After reference: 50
```

:::eg Tracing BYVAL and BYREF
Complete a trace table for the program above. Use columns Points, Score and OUTPUT.

For the **by value** call, Score is a separate variable that starts as a copy of Points. For the **by reference** call, Score is not a separate variable: it is Points under another name, so a change to Score is a change to Points. Write the change in both columns.

By value, `CALL AddBonusCopy(Points)`:

| Points | Score | OUTPUT |
|---|---|---|
| 40 | | |
| | 40 | |
| | 50 | Inside: 50 |
| | | After copy: 40 |

By reference, `CALL AddBonus(Points)`:

| Points | Score | OUTPUT |
|---|---|---|
| 40 | 40 | |
| 50 | 50 | Inside: 50 |
| | | After reference: 50 |

In the first table Points never changes from 40. In the second, Points and Score always have the same value, because they are one variable.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 225" role="img" aria-label="Two panels. Panel one, BYVAL: the procedure gets a copy. The variable Points holds 40 and is unchanged. An arrow labelled copy goes to a separate box for the parameter Score, which now holds 50. Panel two, BYREF: one box holding 50 has two names pointing at it, Points and Score, because it is one box holding 50."><text class="tl tb" x="10" y="20">BYVAL: the procedure gets a copy</text><rect class="fm s-acc sw2" x="20" y="32" width="90" height="36"/><text class="tl tc" x="65" y="56">40</text><rect class="fm s-acc sw2" x="230" y="32" width="90" height="36"/><text class="tl tc" x="275" y="56">50</text><line class="c1 sw2" x1="116" y1="58" x2="224" y2="58" marker-end="url(#ah)"/><text class="tl tc" x="170" y="48">copy</text><text class="tl tc" x="65" y="86">Points</text><text class="tl tc" x="65" y="104">unchanged</text><text class="tl tc" x="275" y="86">Score</text><text class="tl tc" x="275" y="104">the copy changed</text><text class="tl tb" x="10" y="140">BYREF: one variable, two names</text><rect class="fm s-acc sw2" x="125" y="152" width="90" height="36"/><text class="tl tc" x="170" y="176">50</text><text class="tl" x="20" y="176">Points</text><line class="c1 sw2" x1="72" y1="170" x2="119" y2="170" marker-end="url(#ah)"/><text class="tl" x="278" y="176">Score</text><line class="c1 sw2" x1="272" y1="170" x2="221" y2="170" marker-end="url(#ah)"/><text class="tl tc" x="170" y="210">one box holding 50</text></svg><figcaption>By value, the procedure changes its own copy and Points stays 40. By reference, Points and Score are two names for one box, so the change reaches the caller.</figcaption></figure>
:::

:::key When to use which
- **BYVAL** when the module only needs to read the value (the default, and the safe choice).
- **BYREF** when the module must give a result back through the parameter, or when it must change the caller's variable.
- A BYREF argument must be a variable. A literal such as `5` or an expression such as `X + 1` has no place in memory to change, so `CALL AddBonus(5)` is an error.
:::

The textbook BYREF example is a swap. Here it is with new data. A shop stores the stock count of a product in `Opening` and `Closing`, and wants the two exchanged.

```pseudocode
PROCEDURE SwapStock(BYREF Morning : INTEGER, BYREF Evening : INTEGER)
   DECLARE Temp : INTEGER
   Temp ← Morning
   Morning ← Evening
   Evening ← Temp
ENDPROCEDURE

DECLARE Opening, Closing : INTEGER
Opening ← 14
Closing ← 9
CALL SwapStock(Opening, Closing)
OUTPUT Opening, " ", Closing
```

Output:

```output
9 14
```

:::eg Tracing the swap
Complete a trace table for the program above, with columns Opening, Closing, Morning, Evening, Temp and OUTPUT. Then say what would be output if the parameters were BYVAL.

Morning is another name for Opening and Evening is another name for Closing, so each change is written in both columns.

| Opening | Closing | Morning | Evening | Temp | OUTPUT |
|---|---|---|---|---|---|
| 14 | 9 | 14 | 9 | | |
| | | | | 14 | |
| 9 | | 9 | | | |
| | 14 | | 14 | | |
| | | | | | 9 14 |

If the parameters were BYVAL, Morning and Evening would be copies. The procedure would swap the copies and finish, and Opening and Closing would stay 14 and 9. The output would be `14 9`: the procedure would run correctly and do nothing useful.
:::

### Passing by value and by reference in Python

Python does not have the keywords BYVAL and BYREF. What it does is simpler to state and different from both. When you call a function, the parameter becomes a **new name for the same object**. Whether the caller sees a change then depends on whether the object can be changed.

- **Numbers, strings and Booleans cannot be changed.** Assigning to the parameter makes it refer to a new object, and the caller's variable still refers to the old one. This behaves like BYVAL.
- **A list can be changed in place.** Assigning to an element (`scores[0] = 5`) changes the one list that both the caller and the function see. This behaves like BYREF.

```python
def add_bonus(score):
    score = score + 10
    print("Inside:", score)


points = 40
add_bonus(points)
print("Outside:", points)
```

Output:

```output
Inside: 50
Outside: 40
```

```python
def add_bonus_all(scores):
    for i in range(len(scores)):
        scores[i] = scores[i] + 10


points = [40, 25, 30]
add_bonus_all(points)
print(points)
```

Output:

```output
[50, 35, 40]
```

The second program changes the caller's list. But the rule is about changing the **object**, not about assigning to the parameter name. A line such as `scores = [0, 0, 0]` inside the function only points the local name at a new list.

```python
def replace(scores):
    scores = [0, 0, 0]
    print("Inside:", scores)


points = [40, 25, 30]
replace(points)
print("Outside:", points)
```

Output:

```output
Inside: [0, 0, 0]
Outside: [40, 25, 30]
```

To get the effect of BYREF for a number, a Python function **returns** the new value and the caller stores it. Python can return several values at once, and the caller unpacks them. This is how you write the swap:

```python
def swap_stock(morning, evening):
    return evening, morning


opening = 14
closing = 9
opening, closing = swap_stock(opening, closing)
print(opening, closing)
```

Output:

```output
9 14
```

:::warn Python cannot pass an integer by reference
A student who writes `def swap(a, b): a, b = b, a` and calls `swap(x, y)` finds that nothing changes, because `a` and `b` are new names that are swapped, and `x` and `y` are untouched. Return the new values and assign them in the caller.
:::

## Functions

A procedure does a job. Often what you want is an **answer**: the price after a discount, the larger of two numbers, whether a password is valid. A function is a module that sends a single value back to the place where it was called.

:::def Function
A named module that takes zero or more parameters and returns exactly one value. It is called as part of an expression, never as a statement on its own.
:::

:::def Return value
The single value a function sends back with the keyword RETURN. When RETURN runs, the value replaces the function call in the expression, and the function ends at once.
:::

The header of a function states the **data type of the value it returns** after the keyword RETURNS. Here is a function for a shop in Nairobi that takes a percentage off a price.

```pseudocode
FUNCTION Discounted(Price : REAL, Percent : INTEGER) RETURNS REAL
   DECLARE Reduction : REAL
   Reduction ← Price * Percent / 100
   RETURN Price - Reduction
ENDFUNCTION

DECLARE Postage, Total : REAL
Postage ← 4.5
Total ← Discounted(80.0, 25) + Postage
OUTPUT "Pay: ", Total
```

Output:

```output
Pay: 64.5
```

Follow what the computer does with the line `Total ← Discounted(80.0, 25) + Postage`. It calls the function with Price 80.0 and Percent 25. Inside, Reduction is \(80.0 \times 25 \div 100 = 20.0\) and the RETURN sends back \(80.0 - 20.0 = 60.0\). That value **replaces the call**, so the statement becomes `Total ← 60.0 + Postage`, which is 64.5. The expression is then finished as normal.

:::key Function in pseudocode
- Define: `FUNCTION <identifier>(<name> : <type>, …) RETURNS <type>` (empty brackets for no parameters), the statements including at least one `RETURN <value>`, then `ENDFUNCTION`.
- Call it **inside an expression**: `X ← Max(A, B)`, `OUTPUT Max(A, B)`, `IF IsValid(Code) THEN`. Never with CALL.
- The value after RETURN must match the type after RETURNS.
- Never pass a parameter of a function by reference.
:::

:::warn Three habits that lose marks
1. `CALL Discounted(80.0, 25)` is wrong for a function: the returned value would have nowhere to go.
2. A function that uses `OUTPUT` instead of `RETURN` prints the answer but gives the caller nothing to use in an expression.
3. Leaving out `RETURNS <type>` from the header, or putting a RETURNS on a procedure.
:::

The Python function uses `return`. Python also shows what happens when the habit goes wrong: a function without `return` gives back the special value `None`.

```python
def discounted(price, percent):
    reduction = price * percent / 100
    return price - reduction


postage = 4.5
total = discounted(80.0, 25) + postage
print("Pay:", total)


def double(n):
    print(n * 2)


result = double(4)
print(result)
```

Output:

```output
Pay: 64.5
8
None
```

`double` prints 8 but returns nothing, so `result` is `None`. If you try to add 1 to it, Python stops with a `TypeError`.

### Returning early

The statement RETURN ends the function immediately. Nothing after it runs. This lets you write a function as a list of cases, each one finishing the job as soon as the answer is known. A leap year is divisible by 4, except that a century year is a leap year only when it is divisible by 400. A function can test the cases from the most special to the least.

```pseudocode
FUNCTION IsLeapYear(TheYear : INTEGER) RETURNS BOOLEAN
   IF TheYear MOD 400 = 0 THEN
      RETURN TRUE
   ENDIF
   IF TheYear MOD 100 = 0 THEN
      RETURN FALSE
   ENDIF
   IF TheYear MOD 4 = 0 THEN
      RETURN TRUE
   ENDIF
   RETURN FALSE
ENDFUNCTION
```

:::eg Using a function in a condition
A calendar program needs to know the number of days in February. Test the function above with 2000, 1900, 2028 and 2027, then write pseudocode that outputs 29 or 28 for a year typed in.

Work through each year and say which RETURN runs first.

| TheYear | First test that is true | Value returned |
|---|---|---|
| 2000 | `MOD 400 = 0` | TRUE |
| 1900 | `MOD 100 = 0` (1900 MOD 400 is 300) | FALSE |
| 2028 | `MOD 4 = 0` (2028 MOD 100 is 28) | TRUE |
| 2027 | none, so the last RETURN | FALSE |

The function returns a Boolean, so the call can be the whole condition of an IF:

```pseudocode
DECLARE Entered : INTEGER
INPUT Entered
IF IsLeapYear(Entered) THEN
   OUTPUT 29
ELSE
   OUTPUT 28
ENDIF
```

Note `IF IsLeapYear(Entered) THEN`, not `IF IsLeapYear(Entered) = TRUE THEN`. Both work, but the first is shorter and reads like English: "if it is a leap year".
:::

The same function in Python, tested on the four years:

```python
def is_leap_year(the_year):
    if the_year % 400 == 0:
        return True
    if the_year % 100 == 0:
        return False
    if the_year % 4 == 0:
        return True
    return False


for year in [2000, 1900, 2028, 2027]:
    print(year, is_leap_year(year))
```

Output:

```output
2000 True
1900 False
2028 True
2027 False
```

### Procedure or function?

Paper 2 asks you to explain **where each one is appropriate**. The test is whether the caller needs a single value back.

:::cols
:::col Use a procedure when
the module **does** something and the caller needs no value back: print a menu, draw a border, write a record to a file, reset a set of variables. A procedure may still give several results through BYREF parameters.
:::
:::col Use a function when
the module **works out one value** that the caller will use straight away in an expression, a condition or an assignment: a total, a larger number, a TRUE/FALSE test, a converted string.
:::
:::

:::exam "Explain why a function is more appropriate"
The mark is for a reason tied to the scenario. "The module calculates a single value, the price after discount, that the main program uses in an expression [B1], so it can be called inside the calculation and the result replaces the call [B1]" scores. "Functions return values" is only the definition.
:::

## The header and the interface

Look back at the first line of a module. It tells a programmer everything they need in order to **use** the module without reading its body.

:::def Header
The first line of a procedure or function: the keyword (PROCEDURE or FUNCTION), the identifier, the list of parameters with their data types, and, for a function, the data type of the return value.
:::

:::def Interface
Everything another part of the program needs to know to use a module: its identifier, the number, order and data types of its parameters, whether each is passed by value or by reference, and the type of any return value. The statements inside the module are not part of the interface.
:::

For the function `Discounted` the interface is:

| Part | In the header | What it means for a caller |
|---|---|---|
| Identifier | `Discounted` | the name to call |
| Parameter 1 | `Price : REAL` | pass a real number first |
| Parameter 2 | `Percent : INTEGER` | pass a whole number second |
| Passing method | none shown, so BYVAL | the caller's variables are never changed |
| Return type | `RETURNS REAL` | the call can be used where a real number is expected |

This is why modules help teamwork. If two programmers agree the interface, one can write `Discounted` while the other writes the code that calls it, and they can fit together without either one reading the other's statements. A structure chart, which you will draw in [The development life cycle and program design](#cs.development), shows exactly these things: which module calls which, and which values pass between them.

:::eg Writing a header from a description (exam style)
A function `Average` is needed. It takes three whole numbers, Test1, Test2 and Test3, and returns their mean, which may have a fractional part. Write the header, and say what type the function's result must be declared as. [4 marks]

```pseudocode
FUNCTION Average(Test1 : INTEGER, Test2 : INTEGER, Test3 : INTEGER) RETURNS REAL
```

- keyword FUNCTION with the identifier `Average` [B1]
- three parameters, each with a name and the type INTEGER [B1]
- `RETURNS REAL` after the brackets [B1]
- the result is REAL because `/` always gives a REAL, and a mean may have a fractional part [B1]

A header on its own is enough when the question asks only for the header. Do not write the body unless asked.
:::

## Local and global variables

Where is a variable allowed to be used? The answer is its **scope**.

:::def Local variable
A variable declared inside a module. It can be used only inside that module and exists only while the module is running. Parameters are also local.
:::

:::def Global variable
A variable declared outside every module, in the main program. Any module can read and change it, and it exists for the whole run of the program.
:::

:::def Scope
The part of a program where a variable can be used.
:::

```pseudocode
DECLARE Counter : INTEGER

PROCEDURE CountUp()
   DECLARE Increase : INTEGER
   Increase ← 2
   Counter ← Counter + Increase
   OUTPUT "Inside: ", Counter
ENDPROCEDURE

Counter ← 10
CALL CountUp()
CALL CountUp()
OUTPUT "Outside: ", Counter
```

Output:

```output
Inside: 12
Inside: 14
Outside: 14
```

Counter is global: the procedure changes it, and the main program sees the change. Increase is local: it is created each time `CountUp` runs and disappears when it ends. A final statement `OUTPUT Increase` in the main program would be an error, because Increase is not in scope there.

In Python, a variable assigned inside a function is local by default. To change a global variable you must say `global` first.

```python
counter = 10


def count_up():
    global counter
    increase = 2
    counter = counter + increase
    print("Inside:", counter)


count_up()
count_up()
print("Outside:", counter)
```

Output:

```output
Inside: 12
Inside: 14
Outside: 14
```

If you leave out the line `global counter`, Python decides `counter` is a local variable of the function, and `counter + increase` tries to read it before it has a value. The program stops with this message:

```text
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

### Why global variables cause bugs

Global variables look convenient, but every module that can change them is a place where the value might be changed wrongly. The next program is meant to count the words read, but `CountLetters` uses the same global name for its own purpose.

```pseudocode
DECLARE Count : INTEGER

PROCEDURE CountLetters(Word : STRING)
   Count ← LENGTH(Word)
   OUTPUT Word, " has ", Count, " letters"
ENDPROCEDURE

Count ← 0
CALL CountLetters("river")
Count ← Count + 1
CALL CountLetters("mountain")
Count ← Count + 1
OUTPUT "Words read: ", Count
```

Output:

```output
river has 5 letters
mountain has 8 letters
Words read: 9
```

Only two words were read, but the program says 9: after the first call Count is 5, then 6, then the second call overwrites it with 8, then 9. The same thing in Python, with its fix:

```python
count = 0


def count_letters(word):
    global count
    count = len(word)
    print(word, "has", count, "letters")


count_letters("river")
count = count + 1
count_letters("mountain")
count = count + 1
print("Words read:", count)


def count_letters_fixed(word):
    letters = len(word)
    print(word, "has", letters, "letters")


count = 0
count_letters_fixed("river")
count = count + 1
count_letters_fixed("mountain")
count = count + 1
print("Words read:", count)
```

Output:

```output
river has 5 letters
mountain has 8 letters
Words read: 9
river has 5 letters
mountain has 8 letters
Words read: 2
```

The fix uses a local variable (`letters`) with a different name, so the module cannot disturb anything outside it.

:::key Local or global?
- Prefer **local variables and parameters**. A module that uses only its own variables can be tested alone and copied into another program.
- Use a global variable only when the whole program really shares one thing, such as the main array of records that a question says is "global", or a constant such as a tax rate.
- A global variable can be changed by any module, so a wrong value is hard to trace, two modules may reuse a name by accident, and a module that relies on a global cannot be reused without it.
:::

## Modules that work with arrays and records

Paper 2 modules usually work on data held in an array. A typical question says "the global 1D array `Stops` holds the six bus stops" and asks for a function that searches it. The Cambridge guide does not print a syntax for passing a whole array as a parameter, so in pseudocode the question either makes the array global, as here, or states the header it wants. In Python you pass the list as an argument, as you would any other value.

A bus company in Lima keeps its stops in order along one route. The function returns the **position** of a stop, or 0 when it is not on the route (0 is a safe signal, because positions start at 1).

```pseudocode
DECLARE Stops : ARRAY[1:6] OF STRING

FUNCTION FindStop(SearchName : STRING) RETURNS INTEGER
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 6
      IF Stops[Index] = SearchName THEN
         RETURN Index
      ENDIF
   NEXT Index
   RETURN 0
ENDFUNCTION
```

With `Stops` holding Central, Harbour, Market, Station, Hospital and Stadium, `FindStop("Station")` returns 4 and `FindStop("Airport")` returns 0. The first RETURN ends the function as soon as the stop is found, so the search is efficient. The pointer to remember is the final `RETURN 0`: it runs only when the loop has finished without a match.

```python
stops = ["Central", "Harbour", "Market", "Station", "Hospital", "Stadium"]


def find_stop(search_name):
    for index in range(len(stops)):
        if stops[index] == search_name:
            return index + 1
    return 0


print(find_stop("Station"), find_stop("Airport"))
```

Output:

```output
4 0
```

The Python list counts from 0, so the function returns `index + 1` to give the pseudocode position 4. Some mark schemes prefer a WHILE loop with a flag to a RETURN inside a FOR loop; the course accepts both, and the guide states that a RETURN ends the function at once. When a question says "efficient", make sure the loop stops at the first match by one of these routes.

Counting is the other standard job, and a function is ideal because the answer is one number. A teacher in Kumasi wants to know how many of ten scores reach a pass mark.

```pseudocode
DECLARE Scores : ARRAY[1:10] OF INTEGER

FUNCTION CountAtLeast(Limit : INTEGER) RETURNS INTEGER
   DECLARE Index, Count : INTEGER
   Count ← 0
   FOR Index ← 1 TO 10
      IF Scores[Index] >= Limit THEN
         Count ← Count + 1
      ENDIF
   NEXT Index
   RETURN Count
ENDFUNCTION
```

In Python the list is an argument, so the function works on any list and needs no global at all. That is better design, and the pseudocode version is global only because the guide has no array-parameter syntax.

```python
def count_at_least(scores, limit):
    count = 0
    for score in scores:
        if score >= limit:
            count = count + 1
    return count


marks = [45, 72, 38, 90, 66, 81, 54, 70, 29, 77]
print(count_at_least(marks, 60))
```

Output:

```output
6
```

:::eg Counting matching records (exam style)
A library keeps its loans in a global array `Loans` of 100 records of this type. A loan is overdue when `DaysLate` is greater than the number of days given by the user. Write a function `CountOverdue` that takes that number as a parameter and returns how many loans are overdue. [4 marks]

```pseudocode
TYPE Loan
   DECLARE Borrower : STRING
   DECLARE DaysLate : INTEGER
ENDTYPE

DECLARE Loans : ARRAY[1:100] OF Loan

FUNCTION CountOverdue(Limit : INTEGER) RETURNS INTEGER
   DECLARE Index, Count : INTEGER
   Count ← 0
   FOR Index ← 1 TO 100
      IF Loans[Index].DaysLate > Limit THEN
         Count ← Count + 1
      ENDIF
   NEXT Index
   RETURN Count
ENDFUNCTION
```

- header with a parameter for the limit and `RETURNS INTEGER` [B1]
- counter initialised to 0 [B1]
- loop through all 100 records, comparing the `DaysLate` field with the limit [B1]
- `RETURN Count` after the loop, not inside it [B1]

Every element must be examined, because the count cannot be known until the last one, so this time a FOR loop is the efficient choice. A `RETURN` inside the loop would end the function after the first match.
:::

The same function in Python, using a class as the record type and six sample loans:

```python
class Loan:
    def __init__(self, borrower, days_late):
        self.borrower = borrower
        self.days_late = days_late


loans = [Loan("Ife", 0), Loan("Joy", 5), Loan("Kofi", 12),
         Loan("Lina", 0), Loan("Musa", 30), Loan("Nia", 8)]


def count_overdue(limit):
    count = 0
    for loan in loans:
        if loan.days_late > limit:
            count = count + 1
    return count


print(count_overdue(7))
```

Output:

```output
3
```

Kofi (12), Musa (30) and Nia (8) are more than 7 days late.

## Writing efficient modules

Paper 2 often says "write **efficient** pseudocode". For modules this means a few habits.

:::key Efficient pseudocode
- **Stop when the job is done.** If a search finds its answer, leave at once (a flag in a WHILE loop, or an early RETURN) instead of looping to the end.
- **Do not repeat work.** If you need a function's result more than once, call it once and keep the result in a variable.
- **Do not repeat a calculation in a loop** when its value does not change from one pass to the next; work it out once before the loop.
- **Use the right loop.** FOR when every element must be visited, WHILE or REPEAT when the loop can stop early.
- **Use a sensible number of variables and modules.** One variable per purpose, one module per job.
:::

Here a program counts the overdue loans in the previous example and acts on the number three times:

```pseudocode
IF CountOverdue(7) > 10 THEN
   OUTPUT "Send reminders"
ENDIF
IF CountOverdue(7) > 0 THEN
   OUTPUT "Overdue books exist"
ENDIF
OUTPUT "Overdue: ", CountOverdue(7)
```

Every call runs the loop of 100 records, so this program examines \(3 \times 100 = 300\) records and always gets the same answer. The efficient version calls the function once:

```pseudocode
DECLARE Overdue : INTEGER
Overdue ← CountOverdue(7)
IF Overdue > 10 THEN
   OUTPUT "Send reminders"
ENDIF
IF Overdue > 0 THEN
   OUTPUT "Overdue books exist"
ENDIF
OUTPUT "Overdue: ", Overdue
```

This examines only 100 records. The same idea applies to a function that must find a space in a piece of text. A version that always visits every character, even after finding a space, does wasted work; a version that returns at the first space does not. In `"Cape Town"` the space is character 5, so the efficient function stops after 5 characters, not 9.

```pseudocode
FUNCTION HasSpace(Text : STRING) RETURNS BOOLEAN
   DECLARE Index : INTEGER
   FOR Index ← 1 TO LENGTH(Text)
      IF MID(Text, Index, 1) = " " THEN
         RETURN TRUE
      ENDIF
   NEXT Index
   RETURN FALSE
ENDFUNCTION
```

```python
def has_space(text):
    for index in range(len(text)):
        if text[index] == " ":
            return True
    return False


print(has_space("Cape Town"), has_space("Lagos"))
```

Output:

```output
True False
```

## Exam-style functions

Most "write a function" questions have the same shape: a short rule, some string handling, a loop, and a RETURN. Work out the plan before writing: what goes in (the parameters), what comes out (the RETURN type), and what the loop must check. These two examples are typical of Paper 2. In each, the question gives the insert functions it needs.

:::eg Validate a password (exam style)
A school in Lagos accepts a password only if it is at least 8 characters long, contains at least one digit and contains at least one upper-case letter A to Z. The insert gives LENGTH, MID, IS_NUM and ASC. Write a function `ValidPassword` that takes the password as a string and returns TRUE if it meets all three rules and FALSE otherwise. [6 marks]

Plan: the input is a STRING and the output is a BOOLEAN. If the length is wrong the answer is known at once, so return FALSE early. Otherwise look at every character, remembering in two flags whether a digit and an upper-case letter have been seen. The answer is TRUE only if both flags are TRUE after the loop.

```pseudocode
FUNCTION ValidPassword(Password : STRING) RETURNS BOOLEAN
   DECLARE Index : INTEGER
   DECLARE ThisChar : CHAR
   DECLARE HasDigit, HasUpper : BOOLEAN
   IF LENGTH(Password) < 8 THEN
      RETURN FALSE
   ENDIF
   HasDigit ← FALSE
   HasUpper ← FALSE
   FOR Index ← 1 TO LENGTH(Password)
      ThisChar ← MID(Password, Index, 1)
      IF IS_NUM(ThisChar) THEN
         HasDigit ← TRUE
      ENDIF
      IF ASC(ThisChar) >= ASC('A') AND ASC(ThisChar) <= ASC('Z') THEN
         HasUpper ← TRUE
      ENDIF
   NEXT Index
   RETURN HasDigit AND HasUpper
ENDFUNCTION
```

- header: FUNCTION, a STRING parameter and `RETURNS BOOLEAN` [B1]
- length less than 8 returns FALSE [B1]
- loop through every character of the password, extracting each with MID [B1]
- sets a flag (or returns) when a character is a digit, using IS_NUM [B1]
- sets a flag (or returns) when a character is between 'A' and 'Z', for example by ASC [B1]
- returns TRUE only when both conditions are met, after the loop [B1]

(Accept `ThisChar >= 'A' AND ThisChar <= 'Z'`, since CHAR comparisons use the character codes. Accept a loop that exits early once both flags are TRUE.)
:::

```python
def valid_password(password):
    if len(password) < 8:
        return False
    has_digit = False
    has_upper = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
        if "A" <= ch <= "Z":
            has_upper = True
    return has_digit and has_upper


for test in ["river2027", "River", "Rivers2027", "RIVERSIDE"]:
    print(test, valid_password(test))
```

Output:

```output
river2027 False
River False
Rivers2027 True
RIVERSIDE False
```

`river2027` has no upper-case letter, `River` is too short, and `RIVERSIDE` has no digit.

:::eg Convert a date string (exam style)
A clinic in Lahore stores dates as strings in the form `"14/03/2027"`. The global array `Months`, with bounds 1 to 12, already holds the names `"January"` to `"December"`. The insert gives LEFT, MID, RIGHT, STR_TO_NUM and NUM_TO_STR. Write a function `DateToText` that takes a date string and returns it in words, without a leading zero on the day, so that `"14/03/2027"` gives `"14 March 2027"` and `"05/11/2026"` gives `"5 November 2026"`. [5 marks]

Plan: the day is the first 2 characters, the month number is the 2 characters starting at position 4, and the year is the last 4. Converting the day to a number and back removes the zero, and the month number is the index into the array.

```pseudocode
FUNCTION DateToText(DateText : STRING) RETURNS STRING
   DECLARE DayNumber, MonthNumber : INTEGER
   DayNumber ← STR_TO_NUM(LEFT(DateText, 2))
   MonthNumber ← STR_TO_NUM(MID(DateText, 4, 2))
   RETURN NUM_TO_STR(DayNumber) & " " & Months[MonthNumber] & " " & RIGHT(DateText, 4)
ENDFUNCTION
```

- header with a STRING parameter and `RETURNS STRING` [B1]
- day extracted with LEFT (or MID) and converted with STR_TO_NUM [B1]
- month extracted with `MID(DateText, 4, 2)` and converted to a number [B1]
- the month number used as the index into `Months` [B1]
- RETURN joins the day, the month name and the year (RIGHT or MID), with spaces, using `&` [B1]

(Use NUM_TO_STR for the day: `&` joins strings, not a string and a number.)
:::

```python
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def date_to_text(date_text):
    day = int(date_text[0:2])
    month = int(date_text[3:5])
    return str(day) + " " + months[month - 1] + " " + date_text[6:]


print(date_to_text("14/03/2027"))
print(date_to_text("05/11/2026"))
```

Output:

```output
14 March 2027
5 November 2026
```

In Python, `date_text[0:2]` is `LEFT(DateText, 2)`, `date_text[3:5]` is `MID(DateText, 4, 2)` and `date_text[6:]` is `RIGHT(DateText, 4)`. The list `months` counts from 0, so the month number is reduced by 1.

:::exam Writing a module answer
Write the header exactly as the question gives it, with every type. Declare your local variables. Use the parameter names from the header inside the body. Put a RETURN on every route through a function. Test your answer on one normal value and one awkward one (an empty string, a value at the limit) before you move on.
:::

:::eg Spot the error: a function that prints instead of returning
Question: Write a function `Mean2` that takes two REAL numbers and returns their mean. Then write a statement that outputs the mean of 7.5 and 9.0. [4 marks]

A student wrote:

```pseudocode
01  FUNCTION Mean2(A : REAL, B : REAL) RETURNS REAL
02     OUTPUT (A + B) / 2
03  ENDFUNCTION
04  OUTPUT Mean2(7.5, 9.0)
```

Line 01 is a correct header with both parameters and RETURNS REAL [B1]. Line 02 calculates \((A + B) / 2\) correctly [B1]. **Line 02 uses OUTPUT where it needs `RETURN (A + B) / 2`: the function prints 8.25 itself and sends nothing back, so the call in line 04 has no value to output** [B0]. Line 04 correctly calls the function inside the OUTPUT statement, without CALL [B1]. The answer scores 3 out of 4.

The fix is one word: `RETURN (A + B) / 2`. Line 04 then outputs the value that replaces the call, 8.25. A good habit is to read the last statement of every function and ask "which value leaves here?".
:::

:::try Start easy, finish at exam standard
Q: In `PROCEDURE Greet(Name : STRING)`, name the identifier and the parameter.
A: The identifier is `Greet` (the name used to call it). `Name` is the parameter, with the type STRING.
Q: Write a procedure `Divider` with no parameters that outputs ten dashes, and the statement that calls it.
A: A procedure with no parameters has empty brackets, and so does the call.

```pseudocode
PROCEDURE Divider()
   OUTPUT "----------"
ENDPROCEDURE

CALL Divider()
```

Q: Write the header of a procedure `ShowTotal` that takes a STRING `Item` and an INTEGER `Quantity`.
A: `PROCEDURE ShowTotal(Item : STRING, Quantity : INTEGER)`
Q: `Double` is a function. Say what is wrong with the statement `CALL Double(4)` and correct it.
A: A function is never called with CALL, and its returned value must be used. Write `Result ← Double(4)` or `OUTPUT Double(4)`.
Q: `FUNCTION Square(N : INTEGER) RETURNS INTEGER` returns \(N \times N\). What is the value of `Square(5) + Square(2)`?
A: Replace each call by its value: \(25 + 4 = 29\).
Q: `PROCEDURE Triple(BYREF N : INTEGER)` runs `N ← N * 3`. What is output by `X ← 4`, `CALL Triple(X)`, `OUTPUT X`? What would it output if the parameter were BYVAL?
A: By reference, X changes, so it outputs 12. By value, the procedure triples a copy, so X stays 4.
Q: Write a function `IsEven` that takes an INTEGER and returns TRUE when it is even.
A: A number is even when the remainder after dividing by 2 is 0.

```pseudocode
FUNCTION IsEven(N : INTEGER) RETURNS BOOLEAN
   IF N MOD 2 = 0 THEN
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION
```

(The one-line `RETURN N MOD 2 = 0` is also correct.)
Q: What does this Python print? `def f(a, b): return a - b` then `print(f(10, 4), f(4, 10))`.
A: `6 -6`. Arguments are matched by position, so the order matters.
Q: Give two benefits of writing a program as modules.
A: Any two of: a module can be reused in many places; each module can be tested alone; different programmers can write different modules; the program is easier to read and to change.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Write the header of a function `Perimeter` that takes two REAL values, `Width` and `Depth`, and returns a REAL value.
A: `FUNCTION Perimeter(Width : REAL, Depth : REAL) RETURNS REAL`

- identifier and both parameters with their types [B1]
- `RETURNS REAL` [B1]

Q: [3 marks] ★ State the output of this program.

```pseudocode
PROCEDURE Adjust(BYREF A : INTEGER, BYVAL B : INTEGER)
   A ← A * 2
   B ← B + A
   OUTPUT "In: ", A, " ", B
ENDPROCEDURE

DECLARE X, Y : INTEGER
X ← 5
Y ← 3
CALL Adjust(X, Y)
OUTPUT "Out: ", X, " ", Y
```

H: A is another name for X, but B is only a copy of Y.
A: Trace the call: A is X, so A becomes 10 and X becomes 10. B is a copy of Y (3), so B becomes \(3 + 10 = 13\).

```output
In: 10 13
Out: 10 3
```

- first line `In: 10 13` [B1]
- X is 10 after the call because it was passed by reference [B1]
- Y is still 3 because it was passed by value, so the second line is `Out: 10 3` [B1]

Q: [4 marks] ★★ Read this code.

```pseudocode
FUNCTION Cube(Number : INTEGER) RETURNS INTEGER
   RETURN Number * Number * Number
ENDFUNCTION

Volume ← Cube(4) + 1
```

(a) Identify the parameter and the argument. [2]

(b) State the value returned by the function and the value assigned to Volume. [2]
H: The parameter is in the definition; the argument is in the call.
A: (a) The parameter is `Number` [B1]. The argument is `4` [B1].

(b) The function returns \(4 \times 4 \times 4 = 64\) [B1], so Volume is \(64 + 1 = 65\) [B1].

Q: [6 marks] ★★ A warehouse in Quito uses product codes of exactly 6 characters. The first two must be upper-case letters A to Z and the last four must be digits, for example `AB1234`. The insert gives LENGTH, MID, IS_NUM and ASC. Write a function `ValidCode` that takes a code as a string and returns TRUE if it is valid and FALSE otherwise.
H: A wrong length is wrong whatever the characters are: check it first and return at once.
H: Two short loops, one for positions 1 and 2 and one for positions 3 to 6, are easier than one loop with a complicated condition.
A: One possible answer:

```pseudocode
FUNCTION ValidCode(Code : STRING) RETURNS BOOLEAN
   DECLARE Index : INTEGER
   DECLARE ThisChar : CHAR
   IF LENGTH(Code) <> 6 THEN
      RETURN FALSE
   ENDIF
   FOR Index ← 1 TO 2
      ThisChar ← MID(Code, Index, 1)
      IF ASC(ThisChar) < ASC('A') OR ASC(ThisChar) > ASC('Z') THEN
         RETURN FALSE
      ENDIF
   NEXT Index
   FOR Index ← 3 TO 6
      IF NOT IS_NUM(MID(Code, Index, 1)) THEN
         RETURN FALSE
      ENDIF
   NEXT Index
   RETURN TRUE
ENDFUNCTION
```

- function header with a STRING parameter and `RETURNS BOOLEAN` [B1]
- length not equal to 6 returns FALSE [B1]
- loop over the first two characters [B1]
- tests that each is between 'A' and 'Z' and returns FALSE if not [B1]
- loop over characters 3 to 6, using IS_NUM to test for digits and returning FALSE if not [B1]
- `RETURN TRUE` only after all the checks have passed [B1]

Q: [5 marks] ★★ A kitchen timer shows minutes and seconds. Write a procedure `SplitTime` that takes a whole number of seconds by value and gives back the whole minutes and the remaining seconds by reference. Then write the statements that call it for 135 seconds and output the result in the form `2 min 15 s`.
H: DIV gives the whole number of times one value goes into another, MOD gives the remainder.
H: A literal such as 135 can be passed only to a BYVAL parameter. The two results need variables in the call.
A: One possible answer:

```pseudocode
PROCEDURE SplitTime(BYVAL TotalSeconds : INTEGER, BYREF Minutes : INTEGER, BYREF Seconds : INTEGER)
   Minutes ← TotalSeconds DIV 60
   Seconds ← TotalSeconds MOD 60
ENDPROCEDURE

DECLARE M, S : INTEGER
CALL SplitTime(135, M, S)
OUTPUT M, " min ", S, " s"
```

- header with three parameters and their types [B1]
- `TotalSeconds` by value and the other two BYREF [B1]
- minutes calculated with `DIV 60` (135 DIV 60 = 2) [B1]
- seconds calculated with `MOD 60` (135 MOD 60 = 15) [B1]
- CALL with a value and two variables as arguments, and the output in the stated form [B1]

Q: [8 marks] ★★★ A weather station in Kathmandu stores the rainfall in millimetres for each of the 12 months of a year in a global array `Rain`, declared `ARRAY[1:12] OF REAL`.

(a) Write a function `Wettest` that returns the number of the month with the most rainfall. [3]

(b) Write a procedure `ShowAbove` that takes a REAL limit by value and outputs the month number and the rainfall of every month with more rainfall than the limit. [3]

(c) Write the statements that output the result of `Wettest` and call `ShowAbove` with a limit of 100.0. [2]
H: For (a) keep the number of the best month, not only its value, as in the highest value algorithm from [Data types, records and arrays](#cs.datatypes).
H: In (c) one of the two statements uses CALL and one does not.
A: (a) One possible answer:

```pseudocode
FUNCTION Wettest() RETURNS INTEGER
   DECLARE Index, BestMonth : INTEGER
   BestMonth ← 1
   FOR Index ← 2 TO 12
      IF Rain[Index] > Rain[BestMonth] THEN
         BestMonth ← Index
      ENDIF
   NEXT Index
   RETURN BestMonth
ENDFUNCTION
```

- header with `RETURNS INTEGER` and empty brackets [B1]
- compares each month with the best so far and stores the month number [B1]
- `RETURN BestMonth` after the loop [B1]

(b) One possible answer:

```pseudocode
PROCEDURE ShowAbove(BYVAL Limit : REAL)
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 12
      IF Rain[Index] > Limit THEN
         OUTPUT "Month ", Index, ": ", Rain[Index]
      ENDIF
   NEXT Index
ENDPROCEDURE
```

- header with a REAL parameter (by value) [B1]
- loop through all 12 months [B1]
- compares each month with the limit and outputs the month number and rainfall [B1]

(c)

```pseudocode
OUTPUT "Wettest month: ", Wettest()
CALL ShowAbove(100.0)
```

- the function called inside the OUTPUT statement, without CALL [B1]
- `CALL ShowAbove(100.0)` [B1]

For the readings 12.5, 30.0, 78.5, 120.0, 210.5, 150.0, 98.0, 85.5, 160.0, 140.0, 40.0 and 15.0 the function returns 5, and the procedure outputs months 4, 5, 6, 9 and 10.

Q: [7 marks] ★★★ Read this program.

```pseudocode
DECLARE Total : INTEGER

PROCEDURE AddToTotal(Amount : INTEGER)
   DECLARE Doubled : INTEGER
   Doubled ← Amount * 2
   Total ← Total + Doubled
   OUTPUT "Total is ", Total
ENDPROCEDURE

Total ← 0
CALL AddToTotal(5)
CALL AddToTotal(3)
OUTPUT "Final: ", Total
OUTPUT Doubled
```

(a) State the three lines that are output before the program stops. [3]

(b) The last statement causes an error. Explain why. [2]

(c) State two disadvantages of using the global variable Total in the procedure. [2]
H: The first call adds \(5 \times 2\) to Total, the second adds \(3 \times 2\).
A: (a) The first call makes Total 10, the second makes it \(10 + 6 = 16\).

```output
Total is 10
Total is 16
Final: 16
```

- `Total is 10` [B1]
- `Total is 16` [B1]
- `Final: 16` [B1]

(b) Doubled is a local variable of the procedure [B1], so it exists only while the procedure runs and cannot be used in the main program [B1].

(c) Any two of: any module can change Total, so a wrong value is hard to trace; the procedure cannot be reused or tested without the global variable, because it depends on something outside itself; another module might use the same name for a different purpose and corrupt it [B1] [B1]. (Accept: the procedure should receive and return values through parameters.)
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A function `IsPrime` must decide whether an integer N, where N is at least 2, is prime (its only divisors are 1 and N). Write an efficient function using a WHILE loop that tests the divisors D = 2, 3, 4 and so on, **stops at the first divisor found**, and only tests values of D while \(D \times D \le N\). State how many values of D are tested for N = 97 and for N = 91, and how many a version that tests every D from 2 to N − 1 would test for N = 97.
H: If N has a divisor larger than its square root, it also has one smaller than its square root, so testing beyond \(D \times D > N\) is wasted work.
H: RETURN ends the function immediately, so a divisor found means RETURN FALSE at once.
A: One possible answer:

```pseudocode
FUNCTION IsPrime(N : INTEGER) RETURNS BOOLEAN
   DECLARE D : INTEGER
   D ← 2
   WHILE D * D <= N
      IF N MOD D = 0 THEN
         RETURN FALSE
      ENDIF
      D ← D + 1
   ENDWHILE
   RETURN TRUE
ENDFUNCTION
```

- D starts at 2 [B1]
- loop condition \(D \times D \le N\) [B1]
- tests `N MOD D = 0` [B1]
- RETURN FALSE immediately when a divisor is found [B1]
- RETURN TRUE after the loop (no divisor found) [B1]
- N = 97 tests D = 2 to 9, which is 8 values; N = 91 tests D = 2 to 7 and stops at 7 because \(91 = 7 \times 13\), which is 6 values [B1]

The version that tests every D from 2 to 96 makes 95 tests for N = 97. The early exit and the square-root limit together save 87 of them.

Q: [5 marks] ★★★ A student writes this Python and expects it to swap `x` and `y`.

```python
def swap(a, b):
    a, b = b, a


x = 3
y = 8
swap(x, y)
print(x, y)
```

(a) State what it prints and explain why. [2]

(b) Rewrite the call (and the function) so that `x` and `y` really are swapped. [1]

(c) A function `swap_first_two(items)` contains the single line `items[0], items[1] = items[1], items[0]`. Explain why this changes the caller's list, whereas the line `items = [items[1], items[0]]` would not. [2]
H: Think about whether a function changes an object or only changes which object a name refers to.
A: (a) It prints `3 8` [B1]. The parameters `a` and `b` are new names for the numbers, and swapping them changes only those two names, so `x` and `y` are untouched [B1].

(b) Return the values and assign them in the caller [B1]:

```python
def swap(a, b):
    return b, a


x = 3
y = 8
x, y = swap(x, y)
print(x, y)
```

Output:

```output
8 3
```

(c) The first line changes elements of the one list object that the caller and the function both refer to [B1]. The second line builds a new list and points the local name `items` at it, so the caller's list is not changed [B1].
:::

:::quiz
? Which statement correctly uses the function `Max(A, B)`, which returns the larger of two integers?
- `CALL Max(3, 7)`
+ `Biggest ← Max(3, 7)`
- `Max(3, 7)` on a line by itself
- `RETURN Biggest ← Max 3, 7`
> A function is used inside an expression, so its returned value replaces the call. CALL is for procedures only, and a bare call on its own line would throw the returned value away.
? In `CALL Draw(Size, 4)` for `PROCEDURE Draw(Length : INTEGER, Lines : INTEGER)`, which description is correct?
- `Length` and `Lines` are the arguments; `Size` and `4` are the parameters.
+ `Size` and `4` are the arguments; `Length` and `Lines` are the parameters.
- All four are parameters.
- `Size` is the identifier of the procedure.
> The parameters are in the definition and receive the values. The arguments are the values in the call, matched by position: Size goes to Length and 4 goes to Lines.
? A procedure has the header `PROCEDURE Bump(BYVAL N : INTEGER)` and runs `N ← N + 1`. A program sets `X ← 7`, calls `CALL Bump(X)`, then outputs X. What is output?
+ 7
- 8
- 1
- An error, because N is changed.
> BYVAL passes a copy, so the procedure changes only its own N. X is still 7. The answer 8 is what you would get with BYREF.
? Which call is valid for `PROCEDURE Reset(BYREF N : INTEGER)`?
+ `CALL Reset(Count)`
- `CALL Reset(5)`
- `CALL Reset(Count + 1)`
- `CALL Reset("Count")`
> A BYREF parameter is another name for the caller's variable, so the argument must be a variable. A literal or an expression has no variable to change.
? `FUNCTION Double(N : INTEGER) RETURNS INTEGER` returns `N * 2`. What does `OUTPUT Double(4) + Double(3)` output?
- 43
- 8
+ 14
- 6
> Each call is replaced by its value: \(8 + 6 = 14\). The answer 43 joins the digits as if the results were strings.
? A variable declared inside a procedure is a local variable. Which statement about it is true?
- It can be used by every module in the program.
+ It can be used only inside that procedure, and it exists only while the procedure runs.
- It keeps its value between calls.
- It is passed to the main program when the procedure ends.
> Scope is the part of a program where a variable can be used. A local variable's scope is its own module. Sharing a value with the rest of the program needs a global variable, a parameter or a RETURN.
? What does this Python print? `def add_one(n): n = n + 1`, then `x = 5`, `add_one(x)`, `print(x)`.
- 6
+ 5
- None
- An error
> The parameter n is a new name for the number 5. Adding 1 makes n refer to a new number, and x still refers to 5. A number cannot be changed in place, so this behaves like BYVAL.
? What does this Python print? `def add_item(items): items.append(9)`, then `data = [1]`, `add_item(data)`, `print(data)`.
- `[1]`
+ `[1, 9]`
- `[9]`
- None
> The function changes the one list object that data and items both refer to, so the caller sees the new item. A list can be changed in place, so this behaves like BYREF.
? What happens to the statements after a RETURN that has just run?
- They run as normal, then the function ends.
+ They are skipped, because RETURN ends the function immediately.
- They run only if the value returned is TRUE.
- They are run again by the next call.
> The guide states that the execution of RETURN is immediate and any later lines are omitted. This is why a function can return early from inside a loop.
:::

:::checklist What you can now do
- [ ] I can explain why programs are split into modules and name the benefits.
- [ ] I can define and call a procedure, with no parameters or with one or more, and say where a procedure is appropriate.
- [ ] I can use the terms parameter, argument, header, interface and return value correctly.
- [ ] I can pass a parameter by value or by reference and predict the effect on the caller's variable.
- [ ] I can define and call a function, using the returned value in an expression, and say where a function is appropriate.
- [ ] I can distinguish local and global variables and state the problems with global variables.
- [ ] I can write modules that search or count in an array or an array of records.
- [ ] I can write efficient pseudocode that stops early and does not repeat calls.
- [ ] I can write "write a function that …" answers with the insert functions: validation and conversion.
- [ ] I can write the same modules in Python with `def`, `return` and `global`, and explain how Python behaves like BYVAL and BYREF.
:::

:::recap
- A module is a named, self-contained piece of a program. Modules give reuse, easier testing, teamwork, readability and easier maintenance.
- A procedure does a job: `PROCEDURE Name(…)` … `ENDPROCEDURE`, called with `CALL Name(…)`. A function returns one value: `FUNCTION Name(…) RETURNS <type>` … `RETURN <value>` … `ENDFUNCTION`, called inside an expression and never with CALL.
- Parameters are in the header; arguments are in the call; they match by position and type. The header plus the passing methods and return type is the interface.
- BYVAL passes a copy (the default). BYREF passes the original variable, so changes reach the caller; the argument must be a variable. Never use BYREF with a function.
- RETURN ends the function at once, and the returned value replaces the call.
- Local variables (and parameters) exist only inside their module; global variables are shared by all modules and are a common source of bugs.
- Efficient modules stop as soon as the job is done and call a function once, keeping the result.
- In Python: `def`, `return`, `global`. Numbers and strings behave like BYVAL, a list changed in place behaves like BYREF, and to give a number back you return it.
:::

:::links
- practise: [Structured programming: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/11-programming-/structured-programming/exam-questions/) · Save My Exams · 9618-style questions on procedures and functions, with mark schemes [paid]
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run a function from this chapter line by line and watch the parameters and local variables appear and disappear
- read: [Python functions](https://www.w3schools.com/python/python_functions.asp) · W3Schools · a short lesson on def, parameters and return, with try-it boxes
- read: [Defining functions in the Python tutorial](https://docs.python.org/3/tutorial/controlflow.html) · Python.org · the official explanation of def, default values and return
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · section 8, the official rules for procedures, functions, BYVAL and BYREF

Links checked 13 November 2026.
:::

Next: [Text files, stacks, queues and linked lists](#cs.structures)
