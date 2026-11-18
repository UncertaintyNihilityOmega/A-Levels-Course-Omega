@chapter cs.mock.p4
@title Mock Paper 4: Practical
@level mock
@paper CAIE 9618 Paper 4
@time 2 h 30 min
@summary A full-length Paper 4 mock for home use: three programming tasks worth 20, 25 and 30 marks that you write and test in Python on your own computer. Question 1 builds a linked list in global arrays, Question 2 reads a text file into objects with exception handling, a sort and a second file, and Question 3 uses inheritance and recursion on a tree of departments. Every part has a model program that runs, the exact output it prints, and a mark scheme with one mark point per mark.

:::exam Read these instructions first
- You have **2 hours 30 minutes**. The clock above starts when you open the paper. Stop at the end of the time, then press **Finish** to see the mark schemes.
- Use a computer **with no internet**. The real paper allows Java, Python or Visual Basic in console mode; this mock expects **Python in console mode**, and every model program is Python. Other correct programs earn the same marks.
- Carry out **every instruction** in each task. Save each program with the **exact file name** the task gives, and use the **exact identifier names** given.
- Make the source files by copying each text block that says "Save this as" into a plain text file with that name, in the folder where your programs are.
- Make an **evidence document** (any word processor or text file) and save it as `evidence_M4`. After each part, paste the program code into the part's heading in the document. For a testing part, run the program, take a screenshot of the console that shows all the output, and paste it in too. Save the document often.
- **Answer all three questions.** The marks for each part are shown in brackets, for example [5]. The total for the paper is **75 marks**: Question 1 is 20 marks, Question 2 is 25 marks and Question 3 is 30 marks.
- Plan about 1.8 minutes per mark, which leaves about 15 minutes for the evidence: a 30-mark question deserves about 54 minutes.
- When the time is up, press Finish, mark each answer honestly (a mark only for a feature that your program really has, and a screenshot only if it was taken), enter your mark for each question, and use the chapters listed to revise.
:::

:::try
Q: [20 marks] (#cs.adts) A call centre in Manila keeps a waiting list of ticket numbers as a **linked list**, stored in global arrays so that the numbers stay in ascending order. Save your program as `Question1_M4.py`.

The list uses a global array `List` of 10 objects of the class `ListNode`. Each node has two attributes: `Data` (the ticket number, an integer) and `Pointer` (the index of the next node, an integer). The pointer value -1 means there is no next node. The global variable `StartPointer` holds the index of the first node in the list, or -1 if the list is empty. The unused nodes form a second linked list, the free list, and the global variable `FreePointer` holds the index of the first free node, or -1 if there are no free nodes.

(a) Write program code to declare the class `ListNode` and the global array `List` of 10 `ListNode` objects. Set `StartPointer` to -1, and set up the free list so that `FreePointer` is 0, the pointer of each node points to the next node in the array, and the pointer of the last node is -1. Copy your program code into the evidence document. [3]

(b) Write a procedure `AddItem(Value)` that adds the ticket number to the list so that the numbers stay in ascending order. A new node is taken from the front of the free list. If there is no free node, the procedure outputs `List full` and does not change the list. Copy your program code into the evidence document. [5]

(c) Write a procedure `OutputList()` that outputs the word `List:` followed by every ticket number in the list in order, on one line, each number after a space, for example `List: 15 28 40`. If the list is empty it outputs `List empty`. Copy your program code into the evidence document. [3]

(d) Write a function `DeleteItem(Value)` that removes the node that holds the ticket number from the list and returns the node to the front of the free list. The function returns `True` if the number was found and `False` if it was not. Copy your program code into the evidence document. [4]

(e) Write a main program that carries out these steps in order, and run it.

- add the ticket numbers 40, 15, 62, 28 and 51, in that order
- call `OutputList()`
- call `DeleteItem` for 28 and then for 99, outputting `28 deleted` and `99 not found` (each message made from the number and `deleted` or `not found`)
- call `OutputList()`, then output `Free pointer:` followed by the value of `FreePointer`
- add the ticket number 33, call `OutputList()`, then output `Free pointer:` and the value of `FreePointer` again

Copy your program code into the evidence document and take a screenshot of the output. [5]
A: (a)

```python
class ListNode:
    def __init__(self):
        self.Data = 0
        self.Pointer = -1


List = [ListNode() for Index in range(10)]
StartPointer = -1
FreePointer = 0
for Index in range(9):
    List[Index].Pointer = Index + 1
```

- class `ListNode` with the attributes `Data` and `Pointer` set in the constructor [B1]
- global array `List` of 10 `ListNode` objects, and `StartPointer` set to -1 [B1]
- `FreePointer` set to 0, with each pointer set to the next index and the last pointer left as -1 [B1]

(b)

```python
def AddItem(Value):
    global StartPointer, FreePointer
    if FreePointer == -1:
        print("List full")
        return
    NewNode = FreePointer
    FreePointer = List[NewNode].Pointer
    List[NewNode].Data = Value
    Previous = -1
    Current = StartPointer
    while Current != -1 and List[Current].Data < Value:
        Previous = Current
        Current = List[Current].Pointer
    List[NewNode].Pointer = Current
    if Previous == -1:
        StartPointer = NewNode
    else:
        List[Previous].Pointer = NewNode
```

- checks for no free node, outputs `List full` and stops without changing the list [B1]
- takes the first free node and moves `FreePointer` on to the next free node [B1]
- stores the value in the new node [B1]
- searches the list for the position, keeping the previous node and the current node, and stopping at the first larger number or the end (the test that `Current` is not -1 is written first) [B1]
- links the new node in: its pointer is set to `Current`, and either `StartPointer` (when it goes first) or the previous node's pointer is set to the new node [B1]

(c)

```python
def OutputList():
    if StartPointer == -1:
        print("List empty")
    else:
        Line = "List:"
        Current = StartPointer
        while Current != -1:
            Line = Line + " " + str(List[Current].Data)
            Current = List[Current].Pointer
        print(Line)
```

- outputs `List empty` when `StartPointer` is -1 [B1]
- follows the pointers from `StartPointer` until the pointer is -1 [B1]
- outputs the numbers in order on one line in the format `List: 15 28 40` [B1]

(d)

```python
def DeleteItem(Value):
    global StartPointer, FreePointer
    Previous = -1
    Current = StartPointer
    while Current != -1 and List[Current].Data != Value:
        Previous = Current
        Current = List[Current].Pointer
    if Current == -1:
        return False
    if Previous == -1:
        StartPointer = List[Current].Pointer
    else:
        List[Previous].Pointer = List[Current].Pointer
    List[Current].Pointer = FreePointer
    FreePointer = Current
    return True
```

- searches for the value, keeping the previous node [B1]
- returns `False` when the end of the list is reached without finding it [B1]
- removes the node: `StartPointer` is changed if it was the first node, otherwise the previous node's pointer skips it [B1]
- puts the node at the front of the free list (its pointer is the old `FreePointer`, and `FreePointer` is its index) and returns `True` [B1]

(e)

```python
for Number in [40, 15, 62, 28, 51]:
    AddItem(Number)
OutputList()
for Number in [28, 99]:
    if DeleteItem(Number):
        print(str(Number) + " deleted")
    else:
        print(str(Number) + " not found")
OutputList()
print("Free pointer:", FreePointer)
AddItem(33)
OutputList()
print("Free pointer:", FreePointer)
```

The program prints:

```output
List: 15 28 40 51 62
28 deleted
99 not found
List: 15 40 51 62
Free pointer: 3
List: 15 33 40 51 62
Free pointer: 5
```

- the five numbers added in the order given [B1]
- `OutputList()` called after the additions, after the deletions and after adding 33 [B1]
- `DeleteItem` called for 28 and 99, with the correct messages [B1]
- 33 added after the deletion, and `FreePointer` output twice (3, then 5: the node freed by 28 is reused for 33) [B1]
- screenshot showing the output above [B1]

(Other correct programs, and the same program in Java or Visual Basic, earn the same marks. Do not give the screenshot mark if the output shown differs from the output above.)
:::

:::try
Q: [25 marks] (#cs.fileproc) A film festival in Valencia keeps its entries in a text file. Save the data below as `Films.txt`. Each line holds the title, the director, the length in minutes and the audience rating, separated by commas. Some lines are faulty. The file never holds more than 12 films. Save your program as `Question2_M4.py`.

```text
The Quiet Harbour,Elena Marsh,112,7.8
Copper Sky,Tomasz Wren,134,8.4
Night Market,Aiko Tanaka,96,6.9
Ninety Steps,Rafael Costa,ninety,7.1
Salt Roads,Imani Okoye,127,8.1
Paper Boats,Liam Brandt,88,6.2
Winter Orchard,Sofia Petrov,141
Glass Mountain,Chen Wei,119,8.4
Last Tram,Ayesha Rahman,103,7.5
Red Lanterns,Mateo Ruiz,122,7.8
```

(a) Write program code to declare the class `Film` with the attributes `Title`, `Director`, `Minutes` and `Rating`, set by a constructor with four parameters in that order. Declare a global array `Films` that can hold 12 `Film` objects, with every element empty (`None`), and a global integer `FilmCount` set to 0. Copy your program code into the evidence document. [4]

(b) Write a procedure `LoadFilms(FileName)` that reads the text file and stores one `Film` object in `Films` for every correct line, increasing `FilmCount` for each. `Minutes` must be stored as an integer and `Rating` as a real number. A faulty line is a line that does not have four items, or whose length or rating is not a number. For each faulty line the procedure outputs `Line` followed by the line number and `ignored`, and carries on. If the file does not exist the procedure outputs `File not found:` followed by the file name and stops. When the whole file has been read, the procedure outputs the number of films now stored, followed by `films loaded`. Copy your program code into the evidence document. [8]

(c) Write a procedure `SortFilms()` that sorts the stored films into descending order of `Rating`, using an insertion sort that you write yourself. Films with the same rating must stay in the order in which they were read from the file. Do not use a built-in sorting routine. Copy your program code into the evidence document. [6]

(d) Write a procedure `OutputTop(N)` that outputs the first N films of the sorted array, one per line, in the form `1. Copper Sky (8.4)`, that is, the rank, a full stop and a space, the title, and the rating in brackets. The procedure must not output more films than are stored. Write a main program that calls `LoadFilms("Films.txt")`, then `LoadFilms("Missing.txt")`, then `SortFilms()` and then `OutputTop(3)`. Copy your program code into the evidence document and take a screenshot of the output. [4]

(e) Write a procedure `WriteLongFilms(MinMinutes)` that writes the title of every stored film whose length is greater than `MinMinutes` to the text file `Long.txt`, one title per line, in the order of the sorted array. The procedure then outputs the number of films written, followed by `films written to Long.txt`. Add a call with the value 120 to the end of your main program. Copy your program code into the evidence document and take a screenshot of the output. [3]
A: (a)

```python
class Film:
    def __init__(self, Title, Director, Minutes, Rating):
        self.Title = Title
        self.Director = Director
        self.Minutes = Minutes
        self.Rating = Rating


Films = [None] * 12
FilmCount = 0
```

- class `Film` with the four attributes [B1]
- constructor with four parameters in the order given, each stored in its attribute [B1]
- global array `Films` of 12 elements, each `None` [B1]
- global `FilmCount` set to 0 [B1]

(b)

```python
def LoadFilms(FileName):
    global FilmCount
    LineNumber = 0
    try:
        File = open(FileName, "r")
    except FileNotFoundError:
        print("File not found: " + FileName)
        return
    for Line in File:
        LineNumber = LineNumber + 1
        try:
            Title, Director, Minutes, Rating = Line.strip().split(",")
            Films[FilmCount] = Film(Title, Director, int(Minutes), float(Rating))
            FilmCount = FilmCount + 1
        except ValueError:
            print("Line " + str(LineNumber) + " ignored")
    File.close()
    print(str(FilmCount) + " films loaded")
```

- procedure with the parameter `FileName`, and the file opened for reading inside exception handling [B1]
- a missing file outputs `File not found:` and the file name, and the procedure stops [B1]
- every line of the file read in a loop, with the line number counted [B1]
- each line split at the commas into four items [B1]
- the length converted to an integer and the rating to a real number [B1]
- a `Film` object stored in `Films[FilmCount]`, and `FilmCount` increased, only for a correct line [B1]
- a faulty line is caught by exception handling (a wrong number of items, or an item that is not a number) and outputs `Line n ignored` [B1]
- the file closed, and the number of films stored output with `films loaded` [B1]

(c)

```python
def SortFilms():
    for Index in range(1, FilmCount):
        Current = Films[Index]
        Position = Index - 1
        while Position >= 0 and Films[Position].Rating < Current.Rating:
            Films[Position + 1] = Films[Position]
            Position = Position - 1
        Films[Position + 1] = Current
```

- an outer loop from the second stored film to the last stored film (using `FilmCount`, so the empty elements are not touched) [B1]
- the film being placed is held in a variable [B1]
- an inner loop that moves back along the sorted part, with the test that the position is not below 0 written first [B1]
- the comparison is on `Rating`, with a strict `<` so that the order is descending and films with equal ratings stay in file order [B1]
- each film with a lower rating is moved one place along [B1]
- the held film is placed in the gap [B1]

(d)

```python
def OutputTop(N):
    for Rank in range(min(N, FilmCount)):
        print(str(Rank + 1) + ". " + Films[Rank].Title + " (" + str(Films[Rank].Rating) + ")")


LoadFilms("Films.txt")
LoadFilms("Missing.txt")
SortFilms()
OutputTop(3)
```

The program prints:

```output
Line 4 ignored
Line 7 ignored
8 films loaded
File not found: Missing.txt
1. Copper Sky (8.4)
2. Glass Mountain (8.4)
3. Salt Roads (8.1)
```

- `OutputTop` outputs rank, title and rating in the format given, one film per line [B1]
- the loop stops at `FilmCount` if N is larger (for example using `min`) [B1]
- the main program calls the four procedures in the order given [B1]
- screenshot showing the output above [B1]

(e)

```python
def WriteLongFilms(MinMinutes):
    Count = 0
    File = open("Long.txt", "w")
    for Index in range(FilmCount):
        if Films[Index].Minutes > MinMinutes:
            File.write(Films[Index].Title + "\n")
            Count = Count + 1
    File.close()
    print(str(Count) + " films written to Long.txt")


WriteLongFilms(120)
```

The program prints:

```output
3 films written to Long.txt
```

`Long.txt` then contains:

```text
Copper Sky
Salt Roads
Red Lanterns
```

- `Long.txt` opened for writing and closed [B1]
- a loop over the stored films that writes the title of each film longer than `MinMinutes` on its own line [B1]
- the count output in the format given, with the call using 120 and a screenshot of the output [B1]

(Other correct programs, and the same program in Java or Visual Basic, earn the same marks. For the evidence mark in (d) the screenshot must show the output of all four calls.)
:::

:::try
Q: [30 marks] (#cs.oop) A company in Warsaw stores its structure as a tree of departments, written with object-oriented programming. Every department has a name, a budget in whole currency units and a list of the departments that report to it. Some departments are sales departments, which also have a sales target. Save your program as `Question3_M4.py`.

Use these two classes. Attributes must be private.

| Department |
|---|
| Name : STRING |
| Budget : INTEGER |
| Children : ARRAY OF Department |
| constructor(Name, Budget) |
| GetName() |
| GetBudget() |
| AddChild(Child) |
| Describe() |
| TotalBudget() |
| Display(Level) |
| FindDepartment(SearchName) |

| SalesDepartment (inherits from Department) |
|---|
| Target : INTEGER |
| constructor(Name, Budget, Target) |
| GetTarget() |
| Describe() |

(a) Write program code to declare the class `Department`, with a constructor that sets the name and the budget and starts with an empty list of children, and the methods `GetName`, `GetBudget` and `AddChild`. The method `Describe` returns a string made from the name, a colon, a space and the budget, for example `Finance: 60000`. Copy your program code into the evidence document. [5]

(b) Write program code to declare the class `SalesDepartment`, which inherits from `Department`. Its constructor takes the name, the budget and the target, and uses the constructor of the superclass. Add the method `GetTarget`. Override `Describe` so that it returns the string from the superclass followed by a space and the target in brackets after the word `target`, for example `Sales: 120000 (target 90)`. Copy your program code into the evidence document. [5]

(c) Write a recursive method `TotalBudget` of the class `Department` that returns the budget of the department added to the total budgets of all the departments that report to it, at every level. Copy your program code into the evidence document. [5]

(d) Write a recursive method `Display(Level)` of the class `Department` that outputs the result of `Describe` for the department, indented by three spaces for each level, and then does the same for each department that reports to it, one level further in. The first call uses level 0. Copy your program code into the evidence document. [5]

(e) Write a recursive method `FindDepartment(SearchName)` of the class `Department` that searches the department and all the departments below it for the name. It returns the department object when it is found, and `None` if it is not. Copy your program code into the evidence document. [5]

(f) Write a main program that creates these objects: `Head Office` (budget 50000); sales departments `Sales` (120000, target 90), `Retail` (45000, target 40) and `Online` (38000, target 25); and departments `Finance` (60000), `Payroll` (15000) and `IT` (80000). Head Office has Sales, Finance and IT reporting to it. Sales has Retail and Online reporting to it, and Finance has Payroll reporting to it. The program then

- calls `Display(0)` for Head Office
- outputs `Total budget:` followed by the total budget of Head Office, and `Sales total:` followed by the total budget of Sales
- searches Head Office for `Payroll` and then for `Legal`, outputting the description of the department when it is found and the name followed by `not found` when it is not

Copy your program code into the evidence document and take a screenshot of the output. [5]
A: (a)

```python
class Department:
    def __init__(self, Name, Budget):
        self.__Name = Name
        self.__Budget = Budget
        self.__Children = []

    def GetName(self):
        return self.__Name

    def GetBudget(self):
        return self.__Budget

    def AddChild(self, Child):
        self.__Children.append(Child)

    def Describe(self):
        return self.__Name + ": " + str(self.__Budget)
```

- class `Department` with the three attributes declared private (double underscore in Python) [B1]
- constructor with the name and budget parameters that sets the attributes and starts the list of children empty [B1]
- `GetName` and `GetBudget` return the attributes [B1]
- `AddChild` adds the department to the list of children [B1]
- `Describe` returns the name, a colon, a space and the budget as a string [B1]

(b)

```python
class SalesDepartment(Department):
    def __init__(self, Name, Budget, Target):
        super().__init__(Name, Budget)
        self.__Target = Target

    def GetTarget(self):
        return self.__Target

    def Describe(self):
        return super().Describe() + " (target " + str(self.__Target) + ")"
```

- `SalesDepartment` declared as inheriting from `Department` [B1]
- constructor with three parameters that calls the superclass constructor with the name and the budget [B1]
- private attribute `Target` set from the parameter, and `GetTarget` returns it [B1]
- `Describe` overridden with the same name [B1]
- the overriding `Describe` uses the superclass `Describe` and adds ` (target ` and the target in brackets [B1]

(c) The methods of (c), (d) and (e) are written inside the class `Department`. They are shown here as the lines to add to the class from (a), after `Describe`:

```python
    def TotalBudget(self):
        Total = self.__Budget
        for Child in self.__Children:
            Total = Total + Child.TotalBudget()
        return Total
```

- the method starts with the department's own budget [B1]
- loops through all the children [B1]
- calls `TotalBudget` recursively on each child [B1]
- adds each result to the total [B1]
- returns the total (a department with no children stops the recursion, because the loop does nothing) [B1]

(d)

```python
    def Display(self, Level):
        print("   " * Level + self.Describe())
        for Child in self.__Children:
            Child.Display(Level + 1)
```

- the method has the parameter `Level` [B1]
- outputs the description indented by three spaces for each level [B1]
- loops through the children [B1]
- calls `Display` recursively on each child [B1]
- with `Level + 1` as the argument [B1]

(e)

```python
    def FindDepartment(self, SearchName):
        if self.__Name == SearchName:
            return self
        for Child in self.__Children:
            Found = Child.FindDepartment(SearchName)
            if Found is not None:
                return Found
        return None
```

- returns the object itself when its name is the search name (the base case) [B1]
- loops through the children [B1]
- calls `FindDepartment` recursively on each child with the same name [B1]
- returns the result as soon as it is not `None` [B1]
- returns `None` after the loop, when the name was not found [B1]

(f)

```python
Company = Department("Head Office", 50000)
Sales = SalesDepartment("Sales", 120000, 90)
Retail = SalesDepartment("Retail", 45000, 40)
Online = SalesDepartment("Online", 38000, 25)
Finance = Department("Finance", 60000)
Payroll = Department("Payroll", 15000)
IT = Department("IT", 80000)
Company.AddChild(Sales)
Company.AddChild(Finance)
Company.AddChild(IT)
Sales.AddChild(Retail)
Sales.AddChild(Online)
Finance.AddChild(Payroll)
Company.Display(0)
print("Total budget: " + str(Company.TotalBudget()))
print("Sales total: " + str(Sales.TotalBudget()))
for Name in ["Payroll", "Legal"]:
    Found = Company.FindDepartment(Name)
    if Found is None:
        print(Name + " not found")
    else:
        print(Found.Describe())
```

The program prints:

```output
Head Office: 50000
   Sales: 120000 (target 90)
      Retail: 45000 (target 40)
      Online: 38000 (target 25)
   Finance: 60000
      Payroll: 15000
   IT: 80000
Total budget: 408000
Sales total: 203000
Payroll: 15000
Legal not found
```

- the seven objects created, with `SalesDepartment` for Sales, Retail and Online and `Department` for the others [B1]
- `AddChild` used to join the departments into the tree as described [B1]
- `Display(0)` called, and the two totals output with the labels given [B1]
- both searches made, outputting the description when found and `Legal not found` when not [B1]
- screenshot showing the output above [B1]

(Other correct programs, and the same program in Java or Visual Basic, earn the same marks. In Python the three methods of (c), (d) and (e) must be inside the class `Department`; a method written outside the class earns no mark for being a method.)
:::

Next: [Computer Science: the course map](#cs.overview)
