@chapter cs.usertypes
@title User-defined types, file organisation and hashing
@level a2
@paper CAIE 9618 Paper 3 (and Paper 4)
@time 5–7 hours
@summary The built-in types are not always enough, so programmers define their own: enumerated types, pointers, sets, records and classes. You will also learn how files are organised (serial, sequential and random), how a program reaches a record (sequential or direct access) and how a hashing algorithm turns a key into an address, including what to do when two keys collide.

:::why
Real programs describe things the built-in types cannot: a seat that is free, held or sold; a link from one item to the next; a set of valid discount codes; a bank account with a number, a holder and a balance. User-defined types let you say exactly that, and file organisation decides how fast the data can be found again. Paper 3 asks you to define types, choose an organisation for a scenario and work through a hashing algorithm; Paper 4 asks you to build the same ideas as Python code.
:::

**Before you start**, you should know records and arrays from [Data types, records and arrays](#cs.datatypes) and text files from [Text files, stacks, queues and linked lists](#cs.structures).

:::try Warm-up
Q: Which pseudocode keyword ends a record definition, and how do you give the field `Mark` of the record variable `Pupil` the value 70? (from [Data types, records and arrays](#cs.datatypes))
A: `ENDTYPE` ends it, and `Pupil.Mark ← 70` sets the field, using dot notation.
Q: What is \(47 \text{ MOD } 5\)? (from [Programming basics](#cs.programming))
A: 47 divided by 5 is 9 remainder 2, so \(47 \text{ MOD } 5 = 2\).
Q: Which file mode adds new lines to the end of a text file without erasing what is there? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: APPEND, as in `OPENFILE "Log.txt" FOR APPEND`. WRITE would erase the old contents.
:::

## Why programmers define their own types

Every language has built-in types: INTEGER, REAL, CHAR, STRING, BOOLEAN and DATE in the pseudocode guide. They are enough for single values, but real problems need more. A traffic light is always red, amber or green, and no built-in type says that. A program that follows a chain of items needs a value that means "the place where the next item is stored". A seat has a row, a number, a price and a status together.

:::def User-defined data type
A data type that the programmer defines, built from the data types the language already provides, for data that a built-in type does not describe well.
:::

The pseudocode guide adds that data structures a language does not provide must be constructed from the ones it does. That is why this chapter has two kinds of user-defined type.

:::def Non-composite data type
A user-defined type that is a single value rather than a collection of other data items. The syllabus names two: the enumerated type and the pointer.
:::

:::def Composite data type
A type that holds a collection of data items, of one or more data types, under one identifier. The syllabus names the set, the record and the class (and its objects).
:::

The main reasons to define a type are these:

- **It limits the values.** A variable of an enumerated type can hold only the values listed, so a mistake such as a status of "Sodl" is caught at once instead of travelling through the program.
- **It describes the data.** `Seat.Status ← Sold` says more than `Seat.Status ← 2`.
- **It groups related data.** One record holds all the fields of a seat, and can be passed around as one item.
- **It lets the program refer to a place in memory.** A pointer is the tool for that.

## Enumerated types

:::def Enumerated data type
A non-composite data type that has a defined list of possible values. A variable of the type can hold any one of the listed values and nothing else.
:::

In pseudocode the values are listed in brackets after the type name, exactly as the guide writes it:

```pseudocode
TYPE Season = (Spring, Summer, Autumn, Winter)

DECLARE ThisSeason : Season
DECLARE NextSeason : Season

ThisSeason ← Autumn
NextSeason ← Winter
```

Three details are examined.

- The values are **identifiers, not strings**. You write `ThisSeason ← Autumn`, never `ThisSeason ← "Autumn"`. They are not integers either, so `ThisSeason ← 2` is wrong.
- The values come in the order you list them. That is why the guide's own example finds the next season by adding 1 to a variable of this kind.
- An enumerated variable works well in a CASE structure, because there are only a few possible values to test.

```pseudocode
CASE OF ThisSeason
   Spring : OUTPUT "Plant the seeds"
   Summer : OUTPUT "Water every day"
   OTHERWISE : OUTPUT "Leave the garden to rest"
ENDCASE
```

Python has no TYPE statement for this, but its `enum` module does the job. Each member has a name and a value, and a value of the enumeration is not a string, which matches the pseudocode rule.

```python
from enum import Enum

class Season(Enum):
    SPRING = 0
    SUMMER = 1
    AUTUMN = 2
    WINTER = 3

this_season = Season.AUTUMN
next_season = Season((this_season.value + 1) % 4)
print(this_season, next_season)
print(this_season.name, this_season.value)
print(this_season == "AUTUMN")
print([s.name for s in Season])
```

Output:

```output
Season.AUTUMN Season.WINTER
AUTUMN 2
False
['SPRING', 'SUMMER', 'AUTUMN', 'WINTER']
```

The `% 4` wraps round, so the season after winter is spring. The third line shows that `Season.AUTUMN` is not equal to the string `"AUTUMN"`: the value is a member of the enumeration, not text.

:::warn An enumerated value is not a string
`Free`, `Held` and `Sold` are not `"Free"`, `"Held"` and `"Sold"`. If you put quotes round them in an exam answer you have written a string, and the variable would then have to be declared STRING, which allows any text at all. That loses the point of the type.
:::

## Pointers

Every variable lives at an address in memory. A **pointer** is a variable whose value is one of those addresses.

:::def Pointer
A non-composite data type that references (holds the address of) a memory location. The data type of the pointer says what kind of data is stored at that location.
:::

The guide declares the type with a caret, then declares variables of it without one:

```pseudocode
TYPE TIntPointer = ^INTEGER

DECLARE Score : INTEGER
DECLARE Ptr : TIntPointer

Score ← 40
Ptr ← ^Score
OUTPUT Ptr^
Score ← 55
OUTPUT Ptr^
```

`^Score` means "the address of Score", so `Ptr ← ^Score` stores that address in `Ptr`. `Ptr^` means "the value stored at the address in `Ptr`". The program outputs 40, then 55: the pointer does not hold a copy of the value, so it sees the change.

:::html
<figure class="fig small"><svg viewBox="0 0 340 140" role="img" aria-label="A box called Ptr holds the number 3012. An arrow labelled points to runs from it to a box called Score at address 3012, which holds the value 40. Under the pointer box: Ptr holds an address. Under the Score box: Ptr^ is 40."><text class="tl ti" x="20" y="16">Memory</text><rect class="fm s-acc sw2" x="20" y="40" width="100" height="36"/><text class="tl tc tb" x="70" y="63">3012</text><text class="tl tc" x="70" y="98">Ptr</text><rect class="fm s-acc sw2" x="220" y="40" width="100" height="36"/><text class="tl tc tb" x="270" y="63">40</text><text class="tl tc" x="270" y="98">Score</text><text class="tl tc" x="270" y="30">address 3012</text><path class="c1 sw2" d="M 120 58 L 212 58" marker-end="url(#ah)"/><text class="tl tc" x="166" y="48">points to</text><text class="tl tc" x="70" y="126">Ptr holds an address</text><text class="tl tc" x="270" y="126">Ptr^ is 40</text></svg><figcaption>A pointer holds an address, not a value. Following the pointer (Ptr^) gives the value stored at that address, here 40.</figcaption></figure>
:::

The address 3012 in the figure is invented for the picture: a program never needs to know the real number. What matters is the arrow. Pointers are how data structures such as linked lists and trees are built: each node holds a value and a pointer to the next node, as in [Text files, stacks, queues and linked lists](#cs.structures), where the same idea used array indexes instead.

:::eg Reading a pointer
Explain the output of this pseudocode, using the type from this section.

```pseudocode
DECLARE A, B : INTEGER
DECLARE P : TIntPointer

A ← 10
B ← A
P ← ^A
A ← 25
OUTPUT B, " ", P^
```

`B ← A` copies the **value** 10 into B, and B never changes again. [B1]
`P ← ^A` stores the **address** of A in P, so `P^` always gives the current value of A. [B1]
After `A ← 25`, `P^` is 25, so the program outputs `10 25`. [B1]
:::

Python has no pointer type and no `^`. A Python variable holds a **reference** to an object, which is the same idea hidden inside the language, and it is why two names can refer to the same list.

```python
scores = [40, 55]
alias = scores
alias.append(70)
print(scores)
print(alias is scores)
duplicate = list(scores)
duplicate.append(99)
print(scores, duplicate)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

first = Node(10)
first.next = Node(20)
print(first.next.value)
```

Output:

```output
[40, 55, 70]
True
[40, 55, 70] [40, 55, 70, 99]
20
```

`alias = scores` does not copy the list; it makes a second name for it, so adding to `alias` changes `scores`. `list(scores)` makes a real copy. The `Node` class holds a reference to the next node in its `next` field, which is how a linked list is built in Python.

## Composite types: record, set and class

:::def Record
A composite data type that groups several data items, which can be of different data types, under one identifier. Each item is a field, reached by dot notation.
:::

You met records in [Data types, records and arrays](#cs.datatypes). A record field can itself be of a user-defined type, which is how the types in this chapter combine. A record is a type for **data only**.

:::def Set
A composite data type that holds an unordered collection of distinct values of one data type. A value is either in the set or not; it cannot be in it twice.
:::

The guide defines a set type, and then a set with the values in it, using DEFINE:

```pseudocode
TYPE LetterSet = SET OF CHAR
DEFINE Vowels ('A', 'E', 'I', 'O', 'U') : LetterSet
```

The first line creates the type: a set whose members are CHARs. The second creates a set called `Vowels` of that type, holding five values. The guide does not list the set operations, so an examination question describes what it wants in words ("test whether a letter is in the set"). In Python, `set` has them built in:

```python
vowels = {"A", "E", "I", "O", "U"}
print("E" in vowels, "T" in vowels)
letters = {"S", "E", "T", "S", "E", "T"}
print(len(letters), sorted(letters))
print(sorted(vowels | letters), sorted(vowels & letters))
```

Output:

```output
True False
3 ['E', 'S', 'T']
['A', 'E', 'I', 'O', 'S', 'T', 'U'] ['E']
```

The set `letters` was written with six items but holds three, because the duplicates are dropped. `|` is the union (everything in either set) and `&` is the intersection (only what is in both). A set is the right choice when the question is "is this value one of the allowed ones?" and the order does not matter: valid discount codes, permitted file extensions, the vowels of a language.

:::def Class and object
A class defines a composite type that holds data (its properties) and the procedures and functions that act on that data (its methods). An object is one instance of a class, created from it.
:::

A class goes one step beyond a record, because it carries behaviour as well as data. [Object-oriented programming](#cs.oop) covers classes fully; here you need only the idea and the guide's layout:

```pseudocode
CLASS TSeat
   PRIVATE Status : SeatStatus
   PUBLIC PROCEDURE NEW()
      Status ← Free
   ENDPROCEDURE
   PUBLIC FUNCTION IsFree() RETURNS BOOLEAN
      RETURN Status = Free
   ENDFUNCTION
ENDCLASS
```

`PRIVATE` data can be reached only through the class's own methods, and `NEW` is the constructor that runs when an object is created. The same class in Python, together with an enumerated type for the status:

```python
from enum import Enum

class SeatStatus(Enum):
    FREE = 0
    HELD = 1
    SOLD = 2

class Seat:
    def __init__(self, row, number, price):
        self.row = row
        self.number = number
        self.price = price
        self.status = SeatStatus.FREE
        self.buyer = ""

    def sell(self, buyer):
        if self.status == SeatStatus.SOLD:
            return False
        self.status = SeatStatus.SOLD
        self.buyer = buyer
        return True

screen = [Seat("A", n, 6.50) for n in range(1, 5)]
print(screen[1].sell("Ana"), screen[1].sell("Ben"))
print([seat.status.name for seat in screen])
```

Output:

```output
True False
['FREE', 'SOLD', 'FREE', 'FREE']
```

The method `sell` refuses the second sale of the same seat, so the rule "a seat is sold once" lives inside the class instead of being repeated everywhere the program sells a seat.

:::key The user-defined types of the syllabus
| Type | Kind | What it is for | Pseudocode |
|---|---|---|---|
| Enumerated | non-composite | one value from a fixed list of names | `TYPE Season = (Spring, Summer, Autumn, Winter)` |
| Pointer | non-composite | the address of a value of a given type | `TYPE TIntPointer = ^INTEGER`, `Ptr ← ^Score`, `Ptr^` |
| Record | composite | different items about one thing | `TYPE … DECLARE … ENDTYPE`, `Pupil.Mark` |
| Set | composite | distinct values of one type, unordered, with membership tests | `TYPE LetterSet = SET OF CHAR`, `DEFINE …` |
| Class / object | composite | data together with the methods that use it | `CLASS … ENDCLASS` |
:::

### Choosing and designing a type

Paper 3 gives a problem and asks which type to use, and then to write its definition. Ask these questions in order.

1. **One value from a short fixed list of names?** Enumerated.
2. **Several items of different types describing one thing?** Record. If the thing also needs rules (such as "refuse a second sale"), a class.
3. **A group of distinct values where only membership matters?** Set.
4. **A value that stands for where another value is stored?** Pointer.
5. **Many things of the same kind in order, found by position?** An array, of records if each thing has several fields.

:::eg Designing the types for a cinema booking system (exam style)
A cinema in Manila sells seats for each showing. For every seat it stores the row (a letter), the seat number, the status (free, held while the customer pays, or sold), the price and, once sold, the buyer's name. Staff can enter a discount code; the valid codes are "STU", "SEN" and "KID". There are 80 seats in the screen.

(a) Write pseudocode to define an enumerated type SeatStatus. [1]
(b) Write pseudocode to define a record type TSeat for one seat. [3]
(c) Write a declaration for an array Screen that stores all 80 seats. [1]
(d) Write pseudocode to define a set type CodeSet and a set ValidCodes holding the three codes. [2]
(e) Explain why an enumerated type is better than a STRING for the status. [2]

```pseudocode
TYPE SeatStatus = (Free, Held, Sold)

TYPE TSeat
   DECLARE Row : CHAR
   DECLARE Number : INTEGER
   DECLARE Status : SeatStatus
   DECLARE Price : REAL
   DECLARE Buyer : STRING
ENDTYPE

DECLARE Screen : ARRAY[1:80] OF TSeat

TYPE CodeSet = SET OF STRING
DEFINE ValidCodes ("STU", "SEN", "KID") : CodeSet
```

(a) `TYPE SeatStatus = (Free, Held, Sold)`, with the three values in brackets and no quotes. [B1]

(b) `TYPE TSeat` … `ENDTYPE` enclosing the fields [B1]; Row as CHAR, Number as INTEGER, Price as REAL and Buyer as STRING [B1]; the Status field declared with the type SeatStatus [B1].

(c) `DECLARE Screen : ARRAY[1:80] OF TSeat` [B1].

(d) `TYPE CodeSet = SET OF STRING` [B1]; `DEFINE ValidCodes ("STU", "SEN", "KID") : CodeSet` [B1].

(e) Only the three listed values can be assigned, so a misspelling cannot be stored or must be rejected [B1]; the code is easier to read and check because the values have meaningful names [B1]. (Accept: stored efficiently as a small number.)
:::

A good design also chooses the **simplest** type that works. Row is a CHAR because it is always one letter; the price is REAL because it has pence or cents; and the buyer is a STRING because it is text. The advice from [Data types, records and arrays](#cs.datatypes) still applies inside the record.

## File organisation

Programs keep data in files, and the way the records are laid out in a file decides how quickly one of them can be found, how easily a new one can be added and whether the file can be listed in order. There are three organisations.

:::def Serial file
A file in which records are stored in the order they were added (usually chronological order). Nothing about the records' keys decides where a record goes.
:::

:::def Sequential file
A file in which records are stored in order of a key field, such as ascending account number.
:::

:::def Random file
A file in which each record is stored at an address calculated from its record key, usually by a hashing algorithm, and in which the records have a fixed length so that any address can be reached directly.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 360 222" role="img" aria-label="Three rows of boxes show the same six records. Serial file: 6045, 2171, 9308, 4417, 1052, 7734 in the order they arrived. Sequential file: 1052, 2171, 4417, 6045, 7734, 9308 in key order. Random file with eight slots: slot 1 empty, slot 2 holds 4417, slot 3 empty, slot 4 holds 2171, slot 5 holds 9308, slot 6 holds 6045, slot 7 holds 1052 and slot 8 holds 7734."><text class="tl ti" x="20" y="16">Serial: in order of arrival</text><rect class="fm s-acc sw2" x="20" y="24" width="52" height="28"/><text class="tl tc" x="46" y="43">6045</text><rect class="fm s-acc sw2" x="72" y="24" width="52" height="28"/><text class="tl tc" x="98" y="43">2171</text><rect class="fm s-acc sw2" x="124" y="24" width="52" height="28"/><text class="tl tc" x="150" y="43">9308</text><rect class="fm s-acc sw2" x="176" y="24" width="52" height="28"/><text class="tl tc" x="202" y="43">4417</text><rect class="fm s-acc sw2" x="228" y="24" width="52" height="28"/><text class="tl tc" x="254" y="43">1052</text><rect class="fm s-acc sw2" x="280" y="24" width="52" height="28"/><text class="tl tc" x="306" y="43">7734</text><text class="tl ti" x="20" y="82">Sequential: in order of the key</text><rect class="fm s-acc sw2" x="20" y="90" width="52" height="28"/><text class="tl tc" x="46" y="109">1052</text><rect class="fm s-acc sw2" x="72" y="90" width="52" height="28"/><text class="tl tc" x="98" y="109">2171</text><rect class="fm s-acc sw2" x="124" y="90" width="52" height="28"/><text class="tl tc" x="150" y="109">4417</text><rect class="fm s-acc sw2" x="176" y="90" width="52" height="28"/><text class="tl tc" x="202" y="109">6045</text><rect class="fm s-acc sw2" x="228" y="90" width="52" height="28"/><text class="tl tc" x="254" y="109">7734</text><rect class="fm s-acc sw2" x="280" y="90" width="52" height="28"/><text class="tl tc" x="306" y="109">9308</text><text class="tl ti" x="20" y="148">Random: at the address the hash gives</text><rect class="fp s-acc sw2" x="20" y="156" width="40" height="28"/><text class="tl tc" x="40" y="202">1</text><rect class="fm s-acc sw2" x="60" y="156" width="40" height="28"/><text class="tl tc" x="80" y="175">4417</text><text class="tl tc" x="80" y="202">2</text><rect class="fp s-acc sw2" x="100" y="156" width="40" height="28"/><text class="tl tc" x="120" y="202">3</text><rect class="fm s-acc sw2" x="140" y="156" width="40" height="28"/><text class="tl tc" x="160" y="175">2171</text><text class="tl tc" x="160" y="202">4</text><rect class="fm s-acc sw2" x="180" y="156" width="40" height="28"/><text class="tl tc" x="200" y="175">9308</text><text class="tl tc" x="200" y="202">5</text><rect class="fm s-acc sw2" x="220" y="156" width="40" height="28"/><text class="tl tc" x="240" y="175">6045</text><text class="tl tc" x="240" y="202">6</text><rect class="f1 s-acc sw2" x="260" y="156" width="40" height="28"/><text class="tl tc" x="280" y="175">1052</text><text class="tl tc" x="280" y="202">7</text><rect class="f1 s-acc sw2" x="300" y="156" width="40" height="28"/><text class="tl tc" x="320" y="175">7734</text><text class="tl tc" x="320" y="202">8</text></svg><figcaption>The same six account numbers in three organisations. In the random file each key goes to its key MOD 8, plus 1; 1052 and 7734 found their slots taken and moved on to the next free one (the two darker boxes). The numbers under the bottom row are the slot addresses, and slots 1 and 3 stay empty.</figcaption></figure>
:::

:::warn Serial is not sequential
The two words sound alike and examiners test the difference. **Serial** means in the order the records arrived, with no sorting. **Sequential** means sorted by a key field. A file of transactions written as they happen is serial. A file of customers kept in order of customer number is sequential.
:::

### How the records are reached: sequential and direct access

:::def Sequential access
Reading the records of a file one after another, starting at the beginning, until the required record is reached (or the end of the file).
:::

:::def Direct access
Going straight to the location of a required record without reading the records before it.
:::

The syllabus pairs the access methods with the organisations like this:

| Organisation | Records are stored | Access method | Good for | Weak at |
|---|---|---|---|---|
| Serial | in the order they arrived | sequential only | logs, transactions, anything only ever added to | finding one record; listing in key order |
| Sequential | in order of the key | sequential; direct if there is an index | processing every record in key order, merging, reports | adding a record in the middle; single look-ups without an index |
| Random | at an address worked out from the key | direct | fetching one record at once | listing in key order; empty slots waste space |

**Serial files.** A new record is added at the end, which is quick, and nothing needs sorting. To find a record, the program reads from the start and compares each key, so a file of \(n\) records needs \(n\) reads in the worst case. Serial files suit **logs and transaction files**: a till records every sale in the order it happens, and the file is later read from start to finish.

**Sequential files.** Because the records are in key order, the program can process the file in one pass and can stop early when it passes the place where a record would be. Adding a record is awkward: it must go in its correct place, so a new copy of the file is written with the new record in position. Large sequential files are therefore updated in **batches**, as the next example shows.

**Direct access to a sequential file** needs an **index**: a small separate table listing each key and where its record is. The program looks the key up in the index, then goes straight to that record number.

| Key in the index | 1052 | 2171 | 4417 | 6045 | 7734 | 9308 |
|---|---|---|---|---|---|---|
| Record number | 1 | 2 | 3 | 4 | 5 | 6 |

To read account 6045, the program finds 6045 in the index, learns that the record is number 4, and uses `SEEK` to go to record 4. The records themselves are the sequential file in the figure above.

**Random files** keep fixed-length records so that the address of record number \(k\) is simply \((k - 1) \times\) the record length. Which record number goes with which key is decided by the hashing algorithm in the next section. The guide describes the file as having a **file pointer** that can be moved to any address, then a record read or written there.

### Batch updating a sequential file

A master file holds the permanent records in key order. During the month a **transaction file** collects the changes, and it is sorted into the same key order. A batch run then reads both once, in step, and writes a **new master file**. The old master is kept as a backup.

For each key, the program compares the next master record with the next transaction and acts on the lower key:

1. The master key is lower: copy the master record to the new file unchanged.
2. The keys are equal and the transaction is a change: write the changed record. If it is a delete: write nothing.
3. The transaction key is lower (an addition): write the new record.

```python
master = [(101, "Aziz", 400), (105, "Bea", 520), (110, "Carlos", 380), (120, "Dara", 610)]
transactions = [("C", 105, "Bea", 560), ("D", 110, None, None), ("A", 112, "Elif", 450)]

new_master = []
i = 0
j = 0
while i < len(master) or j < len(transactions):
    if j == len(transactions) or (i < len(master) and master[i][0] < transactions[j][1]):
        new_master.append(master[i])
        i = i + 1
    else:
        action, key, name, pay = transactions[j]
        if action == "A":
            new_master.append((key, name, pay))
            j = j + 1
        elif action == "C":
            new_master.append((key, name, pay))
            i = i + 1
            j = j + 1
        else:
            i = i + 1
            j = j + 1

for record in new_master:
    print(record)
```

Output:

```output
(101, 'Aziz', 400)
(105, 'Bea', 560)
(112, 'Elif', 450)
(120, 'Dara', 610)
```

Each file is read once from start to finish and never searched, which is why a sequential file suits a payroll run: every employee is processed once, in key order, whatever the size of the file.

### Choosing an organisation

An answer to "choose an organisation" gives **the organisation, the access method and a reason that uses the scenario**.

| Scenario | Organisation | Access | Reason |
|---|---|---|---|
| Monthly payroll for 400 staff | sequential | sequential | every record is processed each run, in key order, so no direct access is needed |
| An airline checking one passenger's seat at the desk | random | direct | one record must be found at once among millions, in any order |
| A till recording every sale | serial | sequential | records are only ever added in time order and read through at the end |
| A library catalogue searched at the desk and listed in order each month | sequential with an index | direct and sequential | one file serves both jobs |

:::exam Name both parts
The mark scheme usually has one mark for the organisation, one for the access method and one for a reason tied to the scenario. "Random, because it is faster" earns one mark at most: say that the record is found directly from its key without reading the others.
:::

## Hashing

A random file has no search to do: the record's key is turned into its address by a calculation.

:::def Hashing algorithm
A calculation that takes a record key and produces an address (a position in the file or table) at which the record is stored. The same key always gives the same address.
:::

The most common calculation, and the one Paper 3 uses, is the **remainder** of the key divided by the number of slots:

:::key A simple hashing algorithm
For a file of \(N\) slots with addresses starting at 0: address = `Key MOD N`.
For addresses starting at 1: address = `Key MOD N + 1`.
- The result is always in the range 0 to \(N - 1\) (or 1 to \(N\)), so it is always a valid address.
- The same key always gives the same address, which is what makes look-up possible.
- Use the form the question gives. Check where the addresses start.
:::

A different approach is **folding**: split the key into parts, add the parts and then take MOD.

:::eg Hashing by folding
A file has 11 slots, numbered 1 to 11. The hash adds the first three digits of a six-digit staff number to the last three digits and then applies `MOD 11 + 1`. Find the address for staff number 483912.

The two parts are 483 and 912. [B1]
\(483 + 912 = 1395\). [B1]
\(1395 \text{ MOD } 11 = 9\), because \(11 \times 126 = 1386\) and \(1395 - 1386 = 9\), so the address is \(9 + 1 = 10\). [B1]
:::

### Collisions

A file with 11 slots can hold only 11 records, but keys are far more numerous than that, so two different keys will sometimes give the same address.

:::def Collision
The event that two different record keys produce the same address from the hashing algorithm, so that the second record cannot be stored at its calculated address.
:::

A collision is **normal, not an error**. The file must have a rule for what to do. There are two standard rules.

- **Linear probing** (open addressing): try the next address, then the next, until a free slot is found. After the last address, wrap round to the first.
- **Overflow area**: keep a separate area of the file. A record that finds its slot taken goes in the overflow area, and the main slot records where the overflow record is.

:::eg Storing keys with linear probing
A bank in Accra stores account numbers in a random file of 11 slots, numbered 1 to 11. The address is `Key MOD 11 + 1`, and if the slot is taken the next slot is tried, wrapping from 11 back to 1. The file starts empty. Store these keys in this order: 4023, 5117, 2064, 8830, 1479, 3306, 7712, 4045.

Work out each home address, then use probing when it is taken.

| Key | Key MOD 11 | Home slot | Slots tried | Stored in slot |
|---|---|---|---|---|
| 4023 | 8 | 9 | 9 | 9 |
| 5117 | 2 | 3 | 3 | 3 |
| 2064 | 7 | 8 | 8 | 8 |
| 8830 | 8 | 9 | 9, 10 | 10 |
| 1479 | 5 | 6 | 6 | 6 |
| 3306 | 6 | 7 | 7 | 7 |
| 7712 | 1 | 2 | 2 | 2 |
| 4045 | 8 | 9 | 9, 10, 11 | 11 |

All eight home addresses are correct. [B1]
8830 collides with 4023 at slot 9 and goes to slot 10. [B1]
4045 collides at 9 and 10 and goes to slot 11. [B1]
All other keys are stored at their home slot. [B1]
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 300" role="img" aria-label="A column of eleven slots numbered 1 to 11 holding account numbers: slot 2 holds 7712, slot 3 holds 5117, slot 6 holds 1479, slot 7 holds 3306, slot 8 holds 2064, slot 9 holds 4023, slot 10 holds 8830 and slot 11 holds 4045. Slots 1, 4 and 5 are empty. 8830 and 4045 are marked as having home slot 9."><text class="tl ti" x="20" y="16">Random file of 11 slots</text><rect class="fp s-acc sw2" x="50" y="26" width="90" height="24"/><text class="tl te" x="40" y="43">1</text><text class="tl tc" x="95" y="43">empty</text><rect class="fm s-acc sw2" x="50" y="50" width="90" height="24"/><text class="tl te" x="40" y="67">2</text><text class="tl tc" x="95" y="67">7712</text><rect class="fm s-acc sw2" x="50" y="74" width="90" height="24"/><text class="tl te" x="40" y="91">3</text><text class="tl tc" x="95" y="91">5117</text><rect class="fp s-acc sw2" x="50" y="98" width="90" height="24"/><text class="tl te" x="40" y="115">4</text><text class="tl tc" x="95" y="115">empty</text><rect class="fp s-acc sw2" x="50" y="122" width="90" height="24"/><text class="tl te" x="40" y="139">5</text><text class="tl tc" x="95" y="139">empty</text><rect class="fm s-acc sw2" x="50" y="146" width="90" height="24"/><text class="tl te" x="40" y="163">6</text><text class="tl tc" x="95" y="163">1479</text><rect class="fm s-acc sw2" x="50" y="170" width="90" height="24"/><text class="tl te" x="40" y="187">7</text><text class="tl tc" x="95" y="187">3306</text><rect class="fm s-acc sw2" x="50" y="194" width="90" height="24"/><text class="tl te" x="40" y="211">8</text><text class="tl tc" x="95" y="211">2064</text><rect class="fm s-acc sw2" x="50" y="218" width="90" height="24"/><text class="tl te" x="40" y="235">9</text><text class="tl tc" x="95" y="235">4023</text><rect class="f1 s-acc sw2" x="50" y="242" width="90" height="24"/><text class="tl te" x="40" y="259">10</text><text class="tl tc" x="95" y="259">8830</text><text class="tl" x="152" y="259">home slot 9</text><rect class="f1 s-acc sw2" x="50" y="266" width="90" height="24"/><text class="tl te" x="40" y="283">11</text><text class="tl tc" x="95" y="283">4045</text><text class="tl" x="152" y="283">home slot 9</text></svg><figcaption>The file after eight keys are stored with the address Key MOD 11 + 1 and linear probing. 8830 and 4045 both hash to slot 9, which 4023 already holds, so they were placed in the next free slots, 10 and 11 (the two darker boxes).</figcaption></figure>
:::

Notice how the collision at slot 9 pushed two records along: a long chain of full slots makes the next collision more likely to be long too. The fuller the file, the more probing every store and every search needs, which is why a hashed file is made larger than the number of records it will hold.

### Searching after collisions

To find a record the program repeats the same route as the store. It computes the home address and reads that slot. If the key matches, it is found. If the slot holds a different key, it moves to the next slot, wrapping round. **An empty slot means the key was never stored**, so the search stops there and reports "not found".

In the file above, a search for 4045 reads slots 9, 10 and 11 (three reads). A search for 6000 has home address \(6000 \text{ MOD } 11 + 1 = 6\); it reads slots 6, 7, 8, 9, 10 and 11, wraps to slot 1, finds it empty and stops: seven reads to learn that the key is absent.

### Deleting from a hashed file

You cannot simply empty a slot. Suppose 8830 is deleted by blanking slot 10. A later search for 4045 reads slot 9 (4023, not it), then slot 10 (empty), and stops with "not found", although 4045 is in slot 11. The chain was broken.

The fix is a **deletion marker**: a special value in the key field, such as -1, meaning "a record was here and was removed". A search treats a marker as a full slot and carries on. A store treats it as free and may reuse it.

### Hashing in pseudocode with random files

The guide's file commands are `OPENFILE … FOR RANDOM`, `SEEK` to move the file pointer to an address, `GETRECORD` to read the record there into a variable of the record type and `PUTRECORD` to write a record at the file pointer, replacing what was there. It says the address is usually the record number counted from the start and that it is good practice to explain how addresses are computed. Always `SEEK` before each `GETRECORD` or `PUTRECORD`, as the guide's own example does.

The definitions the next programs share (an empty slot has a key of 0, a deleted slot -1) are these.

```pseudocode
TYPE TAccount
   DECLARE AccountKey : INTEGER
   DECLARE Holder : STRING
   DECLARE Balance : REAL
ENDTYPE

CONSTANT Slots = 11

FUNCTION Hash(Key : INTEGER) RETURNS INTEGER
   RETURN (Key MOD Slots) + 1
ENDFUNCTION
```

First, a procedure creates the file with every slot empty, because a random file has to hold a record in every position before slots can be tested:

```pseudocode
PROCEDURE CreateFile()
   DECLARE Blank : TAccount
   DECLARE Address : INTEGER
   Blank.AccountKey ← 0
   Blank.Holder ← ""
   Blank.Balance ← 0.0
   OPENFILE "Accounts.Dat" FOR RANDOM
   FOR Address ← 1 TO Slots
      SEEK "Accounts.Dat", Address
      PUTRECORD "Accounts.Dat", Blank
   NEXT Address
   CLOSEFILE "Accounts.Dat"
ENDPROCEDURE
```

:::eg Writing a record to a random file (exam style)
Accounts are stored in the random file "Accounts.Dat", which has 11 record slots numbered 1 to 11 and was created with every slot empty. A slot is empty when its AccountKey is 0. The function Hash gives the home address of a key. Write a procedure StoreAccount(NewAccount : TAccount) that stores a new account at its home address, or at the next empty slot if that one is taken, wrapping round from slot 11 to slot 1. Assume the file is not full. [7]

```pseudocode
PROCEDURE StoreAccount(NewAccount : TAccount)
   DECLARE Address : INTEGER
   DECLARE Existing : TAccount
   DECLARE Placed : BOOLEAN
   Address ← Hash(NewAccount.AccountKey)
   Placed ← FALSE
   OPENFILE "Accounts.Dat" FOR RANDOM
   WHILE NOT Placed
      SEEK "Accounts.Dat", Address
      GETRECORD "Accounts.Dat", Existing
      IF Existing.AccountKey = 0 THEN
         SEEK "Accounts.Dat", Address
         PUTRECORD "Accounts.Dat", NewAccount
         Placed ← TRUE
      ELSE
         Address ← (Address MOD Slots) + 1
      ENDIF
   ENDWHILE
   CLOSEFILE "Accounts.Dat"
ENDPROCEDURE
```

- the home address found by calling Hash with the new account's key [B1]
- the file opened in RANDOM mode and closed at the end [B1]
- a loop that repeats until a record has been placed [B1]
- `SEEK` to the address, then `GETRECORD` to read the existing record [B1]
- a test for an empty slot (AccountKey = 0) [B1]
- `SEEK` to the same address and `PUTRECORD` of the new account when it is empty [B1]
- otherwise move to the next address, wrapping from 11 to 1 (for example `(Address MOD Slots) + 1`) [B1]
:::

The trick `(Address MOD Slots) + 1` is the wrap. For addresses 1 to 10 it adds 1; for address 11 it gives \(11 \text{ MOD } 11 + 1 = 1\). If the file counted from 0, the next address would be `(Address + 1) MOD Slots`.

The search follows the same route and stops at an empty slot. It returns the address where the key is, or 0 if the key is not present. A key of -1 (a deleted record) is not 0 and is not the key sought, so the search skips it.

```pseudocode
FUNCTION FindAccount(SearchKey : INTEGER) RETURNS INTEGER
   DECLARE Address, Tries, Result : INTEGER
   DECLARE Existing : TAccount
   DECLARE Finished : BOOLEAN
   Address ← Hash(SearchKey)
   Tries ← 0
   Result ← 0
   Finished ← FALSE
   OPENFILE "Accounts.Dat" FOR RANDOM
   WHILE NOT Finished AND Tries < Slots
      SEEK "Accounts.Dat", Address
      GETRECORD "Accounts.Dat", Existing
      IF Existing.AccountKey = SearchKey THEN
         Result ← Address
         Finished ← TRUE
      ELSE
         IF Existing.AccountKey = 0 THEN
            Finished ← TRUE
         ELSE
            Address ← (Address MOD Slots) + 1
            Tries ← Tries + 1
         ENDIF
      ENDIF
   ENDWHILE
   CLOSEFILE "Accounts.Dat"
   RETURN Result
ENDFUNCTION
```

`Tries` is a safeguard: in a completely full file with no empty slot, the search would otherwise loop for ever. Deleting overwrites the record with a marker:

```pseudocode
PROCEDURE DeleteAccount(SearchKey : INTEGER)
   DECLARE Address : INTEGER
   DECLARE Marker : TAccount
   Address ← FindAccount(SearchKey)
   IF Address <> 0 THEN
      Marker.AccountKey ← -1
      Marker.Holder ← ""
      Marker.Balance ← 0.0
      OPENFILE "Accounts.Dat" FOR RANDOM
      SEEK "Accounts.Dat", Address
      PUTRECORD "Accounts.Dat", Marker
      CLOSEFILE "Accounts.Dat"
   ENDIF
ENDPROCEDURE
```

When a store is combined with deletion, the empty test in StoreAccount becomes `Existing.AccountKey <= 0`, so a marked slot can be reused.

### The same ideas in Python

A hash table in a Python list shows the whole algorithm in a few lines. The list has 11 positions numbered 0 to 10, so the address `key % SLOTS` is already the list index, and the printed slot numbers add 1 to match the pseudocode.

```python
SLOTS = 11
DELETED = -1
table = [0] * SLOTS

def hash_index(key):
    return key % SLOTS

def store(key):
    index = hash_index(key)
    for _ in range(SLOTS):
        if table[index] <= 0:
            table[index] = key
            return index + 1
        index = (index + 1) % SLOTS
    return None

def find(key):
    index = hash_index(key)
    for _ in range(SLOTS):
        if table[index] == key:
            return index + 1
        if table[index] == 0:
            return None
        index = (index + 1) % SLOTS
    return None

def delete(key):
    slot = find(key)
    if slot is not None:
        table[slot - 1] = DELETED
    return slot

for key in [4023, 5117, 2064, 8830, 1479, 3306, 7712, 4045]:
    print(key, "stored in slot", store(key))
print("find 4045:", find(4045), " find 6000:", find(6000))
delete(8830)
print("find 4045 after deleting 8830:", find(4045))
print(table)
```

Output:

```output
4023 stored in slot 9
5117 stored in slot 3
2064 stored in slot 8
8830 stored in slot 10
1479 stored in slot 6
3306 stored in slot 7
7712 stored in slot 2
4045 stored in slot 11
find 4045: 11  find 6000: None
find 4045 after deleting 8830: 11
[0, 7712, 5117, 0, 0, 1479, 3306, 2064, 4023, -1, 4045]
```

The marker (-1 in the list) keeps the chain intact, so 4045 is still found after 8830 is deleted. Python's own `dict` is a hash table built on the same idea, which is why looking up a key in a dictionary is fast.

A real random file stores **fixed-length records**, so that address \(\times\) record length gives the position in bytes. The `struct` module packs a record into a fixed number of bytes: `"<i16sd"` means a 4-byte integer, 16 bytes of text and an 8-byte real, 28 bytes in all. `seek` moves the file pointer and `write` and `read` use it, just as `SEEK`, `PUTRECORD` and `GETRECORD` do. The file-handling chapter [File processing and exception handling](#cs.fileproc) uses them in more depth.

```python
import struct

RECORD = struct.Struct("<i16sd")
SLOTS = 11
EMPTY = RECORD.pack(0, b"", 0.0)

def home_slot(key):
    return key % SLOTS + 1

def position(slot):
    return (slot - 1) * RECORD.size

with open("accounts.dat", "w+b") as f:
    for _ in range(SLOTS):
        f.write(EMPTY)
    people = [(4023, "Amara", 250.0), (8830, "Bilal", 99.5), (5117, "Chen", 1200.0)]
    for key, holder, balance in people:
        slot = home_slot(key)
        while True:
            f.seek(position(slot))
            stored_key = struct.unpack("<i", f.read(4))[0]
            if stored_key <= 0:
                break
            slot = slot % SLOTS + 1
        f.seek(position(slot))
        f.write(RECORD.pack(key, holder.encode(), balance))
        print(key, "written at slot", slot)
    f.seek(position(home_slot(5117)))
    key, holder, balance = RECORD.unpack(f.read(RECORD.size))
    print(key, holder.rstrip(b"\x00").decode(), balance)
print("record size:", RECORD.size, "bytes; file size:", SLOTS * RECORD.size)
```

Output:

```output
4023 written at slot 9
8830 written at slot 10
5117 written at slot 3
5117 Chen 1200.0
record size: 28 bytes; file size: 308
```

:::note Why a random file wastes space
The file always has room for every slot, empty or not, so a random file is larger than a serial file holding the same records. That is the price of reaching any record in one step. It is also why a random file cannot be listed in key order without reading and sorting everything.
:::

## Spot the error

:::eg Spot the error
A student was asked: "A hashed file uses `Key MOD 11 + 1` and linear probing. Explain how a record is deleted, and why a record cannot be removed by setting its slot back to empty." The file is the one in the figure above, with 4023 in slot 9, 8830 in slot 10 and 4045 in slot 11.

Student's answer: "Delete 8830 by writing an empty record in slot 10, with key 0. This is fine because the slot is then free for a new record. A search for any other key still works because it uses the hash."

Find the mistake, say what goes wrong with a worked case, and give the correct method.

- **The mistake.** A slot with key 0 means "never used", and a search stops at the first such slot. [B1]
- **A case where it fails.** A search for 4045 has home slot 9, reads 4023 (not it), reads slot 10 (now empty) and stops with "not found", although 4045 is in slot 11. [B1]
- **The fix.** Write a deletion marker such as -1 into the key field. A search treats a marker as a full slot and carries on, and a new record may be stored in a marked slot. [B1]

The final sentence of the student's answer is also wrong: the hash gives only the **first** place to look, so searching still depends on the probing chain being unbroken.
:::

## Try it yourself

:::try Start easy, finish at exam standard
Q: Write a pseudocode type `Direction` that can hold only North, South, East or West, then declare a variable `Heading` of the type and set it to East.
A: `TYPE Direction = (North, South, East, West)`, then `DECLARE Heading : Direction`, then `Heading ← East`. The values have no quotes.
Q: State what the following outputs: `DECLARE N : INTEGER`, `DECLARE P : TIntPointer`, `N ← 7`, `P ← ^N`, `N ← N + 1`, `OUTPUT P^`.
A: `P^` is the value now stored in N. N becomes 8, so the output is 8.
Q: A set is defined as `TYPE DigitSet = SET OF CHAR` and `DEFINE Even ('0', '2', '4', '6', '8') : DigitSet`. Why does `Even` hold five items even if the list in DEFINE is written with the digit '4' twice?
A: A set holds distinct values only, so a repeated value is stored once.
Q: What is the address of key 85 in a file of 13 slots numbered 1 to 13 using `Key MOD 13 + 1`? What is the address of key 85 if the slots are numbered from 0?
A: \(85 \text{ MOD } 13 = 7\) because \(13 \times 6 = 78\) and \(85 - 78 = 7\). The address is \(7 + 1 = 8\) when the slots start at 1, and 7 when they start at 0.
Q: Which organisation, serial or sequential, is each of these? (a) The orders a website receives, stored as they arrive. (b) Customer records kept in ascending customer number.
A: (a) Serial, because the records are in the order they arrived. (b) Sequential, because the records are in order of a key.
Q: A file of 7 slots (numbered 0 to 6) uses `Key MOD 7` and linear probing. Show where 16, 23 and 9 are stored, in that order.
A: \(16 \text{ MOD } 7 = 2\), so 16 goes in slot 2. \(23 \text{ MOD } 7 = 2\), which is taken, so 23 goes in slot 3. \(9 \text{ MOD } 7 = 2\), and slots 2 and 3 are taken, so 9 goes in slot 4.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A school in Kampala stores each candidate's award as Pass, Merit or Distinction, together with the candidate's name and mark. Write pseudocode to define an enumerated type Award and a record type TResult that uses it.
A: One possible answer:

```pseudocode
TYPE Award = (Pass, Merit, Distinction)

TYPE TResult
   DECLARE Candidate : STRING
   DECLARE Mark : INTEGER
   DECLARE Grade : Award
ENDTYPE
```

- `TYPE Award = (Pass, Merit, Distinction)` with the values listed and unquoted [B1]
- `TYPE TResult` … `ENDTYPE` enclosing the fields [B1]
- the three fields declared with suitable types, the last of type Award [B1]

Q: [4 marks] ★ Describe the difference between a serial file and a sequential file.
A: Mark points:

- In a serial file the records are stored in the order they were added [B1]
- and are not sorted by any key. [B1]
- In a sequential file the records are stored in order of a key field [B1]
- so a new record must be inserted in its correct place, which means writing a new copy of the file. [B1]

Q: [3 marks] ★★ (#cs.usertypes) A bakery chain in Lagos pays 400 staff once a month, from a master file of employees. Justify the use of a sequential file with sequential access for the payroll run.
H: Think about which records the program needs: one, or all of them?
A: Mark points:

- Every employee record is processed in each payroll run, so direct access is not needed [B1]
- the records are in key order, so the master file can be read once, from start to finish, in step with a transaction file of changes [B1]
- no space is wasted on empty slots, unlike a random file. [B1]

Q: [4 marks] ★★ A random file has 7 slots numbered 1 to 7. The address is `Key MOD 7 + 1`. If a slot is taken, the next slot is tried, wrapping from slot 7 to slot 1. Show the contents of the file after the keys 38, 27, 59, 16, 41 and 70 are stored in that order, and state how many of the six keys collided.
H: Work out the home address of every key first.
A: Home addresses: 38 gives 4, 27 gives 7, 59 gives 4, 16 gives 3, 41 gives 7, 70 gives 1.

| Slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Key | 41 | 70 | 16 | 38 | 59 | empty | 27 |

- 38, 27 and 16 in slots 4, 7 and 3 [B1]
- 59 in slot 5, because slot 4 is taken [B1]
- 41 in slot 1, because slot 7 is taken and the search wraps round [B1]
- 70 in slot 2, because its home slot 1 is taken; three keys collided (59, 41 and 70) [B1]

Q: [6 marks] ★★★ (#cs.usertypes) A warehouse in Chennai stores parts in the random file "Parts.Dat", which holds 13 records at addresses 0 to 12. Each record has the type TPart, with the fields PartNo : INTEGER, Description : STRING and Quantity : INTEGER. A slot is empty when PartNo is 0. The home address of a part is `PartNo MOD 13`. Write a procedure StorePart(NewPart : TPart) that stores a part at its home address or at the next empty slot, wrapping round from 12 to 0. Assume the file is not full.
H: Compute the home address with MOD, as the question says, and use `(Address + 1) MOD 13` to move on, because the addresses start at 0.
A: One possible answer:

```pseudocode
PROCEDURE StorePart(NewPart : TPart)
   DECLARE Address : INTEGER
   DECLARE Existing : TPart
   DECLARE Placed : BOOLEAN
   Address ← NewPart.PartNo MOD 13
   Placed ← FALSE
   OPENFILE "Parts.Dat" FOR RANDOM
   WHILE NOT Placed
      SEEK "Parts.Dat", Address
      GETRECORD "Parts.Dat", Existing
      IF Existing.PartNo = 0 THEN
         SEEK "Parts.Dat", Address
         PUTRECORD "Parts.Dat", NewPart
         Placed ← TRUE
      ELSE
         Address ← (Address + 1) MOD 13
      ENDIF
   ENDWHILE
   CLOSEFILE "Parts.Dat"
ENDPROCEDURE
```

- the home address calculated as `PartNo MOD 13` [B1]
- the file opened in RANDOM mode and closed [B1]
- a loop that continues until the part is placed [B1]
- `SEEK` and `GETRECORD` to read the record at the current address, then a test of PartNo = 0 [B1]
- `SEEK` and `PUTRECORD` of the new part into the empty slot [B1]
- the next address calculated with wrap round, `(Address + 1) MOD 13` [B1]

Q: [5 marks] ★★ State what is output by this pseudocode and explain why the two values it shows differ, although both were set from Stock. Use the type `TIntPointer = ^INTEGER`.

```pseudocode
DECLARE Stock, Backup : INTEGER
DECLARE Link : TIntPointer

Stock ← 12
Backup ← Stock
Link ← ^Stock
Stock ← 9
OUTPUT Backup, " ", Link^
```

H: One of the variables holds a copy of a value, the other a way to reach the original.
A: The output is `12 9`. [B1]

- `Backup ← Stock` copies the value 12, so a later change to Stock does not change Backup [B1]
- `Link ← ^Stock` stores the address of Stock in Link, not a copy of its value [B1]
- `Link^` follows the address to the value stored there, which is now 9 [B1]
- so the output shows the old value for Backup and the new value for Link^ [B1]

Q: [4 marks] ★★ A set type and a set are defined with `TYPE DigitSet = SET OF CHAR` and `DEFINE Odd ('1', '3', '5', '7', '9') : DigitSet`. (a) State the data type of the values that can be members of DigitSet. [1] (b) State three properties of a set that an array does not have. [3]
A: (a) CHAR. [B1]

(b) Any three from (other valid properties, such as the set operations union and intersection, are accepted):

- a set holds each value only once, so there are no duplicates [B1]
- the values in a set are not in any order [B1]
- a value is not reached by an index, but tested for membership [B1]

Q: [4 marks] ★★★ An airline holds 2 million passenger records. A desk clerk must display any one passenger's record almost at once, given the booking number, and a nightly job lists all bookings in booking number order. Choose an organisation and access method for the file for the desk, and explain how the nightly job could be supported.
H: One organisation is best at single look-ups and another at listing in order. Which one gives the most mark points?
A: Mark points:

- random organisation with direct access for the desk, [B1]
- because a hashing algorithm turns the booking number into the record's address, so the record is read without reading the others [B1]
- the nightly listing is slow from a random file because the records are not in key order, [B1]
- so either the list is produced by reading every record and sorting it, or the data is kept as a sequential file with an index, which gives both direct access and an ordered pass. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A shop gives its products codes that are multiples of ten: 120, 230, 340, 450, 560, 670, 780 and 890. They are stored in a random file of 10 slots numbered 0 to 9, with the address `Key MOD 10` and linear probing. (a) Show that every key has the same home address. [2] (b) Work out the total number of slots read to find each of the eight keys once. [2] (c) The file is changed to 13 slots, numbered 0 to 12, with `Key MOD 13`. Show that the keys now have different home addresses and give the new total. [2]
H: Add up reads per key: the first key stored is found in one read, the second in two, and so on.
H: A key that sits at its home address is found in one read.
A: (a) Every key ends in 0, so `Key MOD 10` is 0 for all eight. [B1] All eight keys have home address 0 [B1]
(b) The keys are stored in slots 0 to 7, in the order given, so they are found in 1, 2, 3, 4, 5, 6, 7 and 8 reads. [B1] The total is \(1 + 2 + \dots + 8 = 36\) reads [B1]
(c) The home addresses are 3, 9, 2, 8, 1, 7, 0 and 6, all different [B1]; every key is found in one read, so the total is 8 [B1]

The lesson: a hash function should spread the keys. If the keys share a pattern (here the last digit) and the number of slots shares a factor with that pattern, many keys fall on a few addresses and the file behaves like a long serial search.

Q: [5 marks] ★★★ A sequential file holds 5000 customer records. Staff need to look up single records quickly. The file keeps an index with one entry per block of 100 records: the highest key in the block. Explain how the index lets a look-up use direct access, and state the greatest number of reads needed to find a record, compared with sequential access of the whole file.
H: Find the right block from the index, then read only that block.
A: Mark points:

- 5000 records in blocks of 100 gives 50 blocks and so 50 index entries [B1]
- the index is read in order until the first entry whose highest key is greater than or equal to the key wanted; this identifies the block [B1]
- the program then uses direct access (SEEK) to the start of that block [B1]
- and reads at most 100 records, sequentially, until the key is found [B1]
- so at most \(50 + 100 = 150\) reads, instead of up to 5000 for sequential access of the whole file [B1]
:::

## Quiz

:::quiz
? Which statement about an enumerated type is correct?
- Its values are strings, so they must be written in quotes.
+ A variable of the type can hold only one of the values listed in its definition.
- It is a composite type, because it holds several values.
- Its values are integers, so `Season ← 2` is allowed.
> An enumerated type is a non-composite type with a fixed list of named values. The values are identifiers, not strings and not integers.
? Given `TYPE Season = (Spring, Summer, Autumn, Winter)` and `DECLARE ThisSeason : Season`, which assignment is valid?
- `ThisSeason ← "Winter"`
- `ThisSeason ← 4`
+ `ThisSeason ← Winter`
- `ThisSeason ← Season`
> The value is written as the identifier Winter. "Winter" is a string, 4 is an integer and Season is the name of the type.
? What does a pointer variable hold?
- A copy of a value
- A whole record
+ The address of a memory location
- The name of a procedure
> A pointer holds an address. Following it with `^` after the name gives the value stored there.
? How does a serial file differ from a sequential file?
- A serial file can only hold text.
+ A serial file stores records in the order they were added, a sequential file in order of a key field.
- A serial file uses direct access and a sequential file does not.
- They are the same, except that a sequential file has fixed-length records.
> The difference is the order of the records. Nothing in a serial file depends on a key; a sequential file is sorted by one.
? An airline needs to find one passenger's record at once among millions. Which organisation and access method fits best?
- Serial, with sequential access
- Sequential, with sequential access
+ Random, with direct access
- Random, with sequential access
> A random file puts each record at an address computed from its key, so direct access reaches it without reading the others.
? A file has 11 slots numbered 1 to 11 and the address is `Key MOD 11 + 1`. Which address does key 100 give?
- 1
+ 2
- 9
- 11
> 100 MOD 11 is 1, because 11 × 9 = 99, so the address is 1 + 1 = 2. The answer 1 forgets the +1 that the numbering from 1 needs.
? What is a collision?
- Two records with the same key being stored in the file
- The file running out of empty slots
+ Two different keys giving the same address
- A search failing to find a key
> A collision is two different keys hashing to the same address. It is normal, and the file has a rule such as linear probing to deal with it.
? Why is a deleted record in a hashed file marked, instead of the slot being set back to empty?
- An empty slot is slower to search.
- Marked slots cannot be reused.
+ A search stops at an empty slot, so emptying it could hide records stored after it by probing.
- The record length changes when a slot is emptied.
> Searches stop at the first empty slot. A marker says "something was here" so the search carries on, and a new record may still reuse the slot.
? How many items does the set `{3, 5, 3, 7, 5}` hold?
- 5
- 2
+ 3
- 1
> A set keeps each value once, so it holds 3, 5 and 7: three items.
:::

:::checklist What you can now do
- [ ] I can explain why user-defined data types are necessary, and the difference between non-composite and composite types.
- [ ] I can define an enumerated type, declare variables of it and use its values correctly (not as strings).
- [ ] I can define a pointer type, use `^` to take an address and `Ptr^` to read the value, and explain the difference from a copy.
- [ ] I can define a record, a set (with DEFINE) and say what a class and an object are, and write them in Python.
- [ ] I can choose and design a type for a problem and justify the choice.
- [ ] I can describe serial, sequential and random files and the sequential and direct access methods that go with them.
- [ ] I can choose a file organisation and access method for a scenario and give a reason.
- [ ] I can apply a hashing algorithm (MOD and folding) to find an address, resolve collisions and search a hashed file.
- [ ] I can write pseudocode that reads and writes a random file with SEEK, GETRECORD and PUTRECORD.
:::

:::recap
- A user-defined type is built by the programmer from built-in types. Non-composite: enumerated, pointer. Composite: set, record, class/object.
- An enumerated type has a fixed list of values written as identifiers: `TYPE Season = (Spring, Summer, Autumn, Winter)`. They are not strings or integers.
- A pointer holds an address: `TYPE TIntPointer = ^INTEGER`, `Ptr ← ^Score`, and `Ptr^` is the value at that address. Python has references instead.
- A set holds distinct unordered values of one type: `TYPE LetterSet = SET OF CHAR` with `DEFINE`. A record groups fields; a class adds methods.
- Serial: in order of arrival. Sequential: in order of a key. Random: at an address calculated from the key. Serial and sequential files are read sequentially; sequential (with an index) and random files can be accessed directly.
- Master files and batch updates suit sequential files; a single quick look-up suits a random file; a log suits a serial file. Name the organisation, the access and a reason from the scenario.
- A hashing algorithm gives an address from a key: `Key MOD N` (+ 1 if addresses start at 1). The same key always gives the same address.
- A collision (two keys, one address) is normal. Linear probing tries the next slot and wraps round; an overflow area is the other method. A search stops at an empty slot, and a deleted slot needs a marker.
- A random file is accessed with `OPENFILE … FOR RANDOM`, `SEEK`, `GETRECORD` and `PUTRECORD`; the records have a fixed length.
:::

:::links
- practise: [User-defined data types: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/13-data-representation-/user-defined-data-types/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [File organisation and access: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/13-data-representation-/file-organisation-and-access-/exam-questions/) · Save My Exams · questions on file types, hashing and collisions [paid]
- explore: [Hash tables](https://visualgo.net/en/hashtable) · VisuAlgo · insert, search and delete keys and watch collisions being resolved
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run the hash table in this chapter line by line
- read: [Python classes](https://docs.python.org/3/tutorial/classes.html) · Python.org · the official tutorial on classes and objects
- read: [The 2027–2029 Pseudocode Guide](https://www.cambridgeinternational.org/Images/721401-2027-2029-pseudocode-guide.pdf) · Cambridge · the official rules for user-defined types and random files

Links checked 13 November 2026.
:::

Next: [Floating-point numbers](#cs.float)
