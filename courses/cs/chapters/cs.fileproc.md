@chapter cs.fileproc
@title File processing and exception handling
@level a2
@paper CAIE 9618 Papers 3 and 4
@time 5–7 hours
@summary Programs keep data in files and meet problems at run time. You will write code that opens, reads, writes and closes text files, processes serial, sequential and random files record by record, and uses exception handling so that a missing file or a bad value does not crash the program.
:::why
A program that forgets everything when it stops is not much use: marks, stock, orders and settings all live in files. Files are also where programs fail in real life, because a file may be missing, a line may hold nonsense or the user may type letters where a number is needed. Paper 4 gives you a text file to read, split and process, and expects the program not to crash. Paper 3 asks you to explain exception handling and to write code for the three kinds of file.
:::

**Before you start**, you should know the file commands and the file modes from [Text files, stacks, queues and linked lists](#cs.structures), the three file organisations from [User-defined types, file organisation and hashing](#cs.usertypes), and records as classes from [Data types, records and arrays](#cs.datatypes).

:::try Warm-up
Q: A program opens an existing file in `"w"` mode and writes one line. What happens to the lines that were already in the file? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: They are lost. Opening a file for writing makes it empty first. Use `"a"` (append) to add to the end.
Q: A line is read from a file as `"A100,Rice,250,40\n"`. What does `line.strip().split(",")` give? (from [Programming from zero](#cs.f.basics))
A: `strip()` removes the `"\n"` at the end, and `split(",")` cuts the text at each comma, giving the list `['A100', 'Rice', '250', '40']`. Every item is still a string.
Q: What is the difference between a serial file and a sequential file? (from [User-defined types, file organisation and hashing](#cs.usertypes))
A: A serial file holds records in the order they arrived. A sequential file holds them in order of a key field.
:::

:::note Pseudocode and Python in this chapter
The file commands in pseudocode (`OPENFILE`, `READFILE`, `WRITEFILE`, `EOF`, `CLOSEFILE`, and for random files `SEEK`, `GETRECORD` and `PUTRECORD`) are exactly those of the Cambridge Pseudocode Guide. The guide has no exception keywords, so a question that needs exception handling describes it in words. The Python examples create their own sample files, so each one runs on its own, and every output shown has been produced by running the program.
:::

## Files, records and fields

A **file** is a named collection of data kept on backing storage, so it survives when the program stops. Programs usually store many items of the same shape, such as the products of a shop, so the data is divided into records and fields.

:::def Record
A group of related data items (fields) about one thing, for example one product in a shop. Every record in a file has the same fields in the same order.
:::

:::def Field
One data item inside a record, for example a product's code, name, price or number in stock.
:::

A **text file** stores each record as a line of characters. The fields are separated by a comma, so a line such as `A100,Rice,250,40` holds the code, the name, the price in shillings and the number in stock. In this chapter a small shop in Nairobi keeps its stock in such a file.

The three organisations you met in [User-defined types, file organisation and hashing](#cs.usertypes) change **how the records are arranged**, and so how a program must process them.

| Organisation | How the records are arranged | How a program reaches a record | Adding a record |
|---|---|---|---|
| Serial | in the order they arrived | read from the start until found | write it at the end (append) |
| Sequential | in order of the key field | read from the start; can stop early when the key has been passed | copy the file to a new one with the record in its place |
| Random | at fixed-size positions, a record number apart | go straight to the record by its address | write the record at its address |

The rest of the chapter shows the code for each, then turns to exceptions.

## Text files in Python

You met the pseudocode commands in the earlier chapter. A recap of the Python equivalents:

| Job | Pseudocode | Python |
|---|---|---|
| open to read | `OPENFILE "F.txt" FOR READ` | `open("F.txt", "r")` |
| open to write (erases) | `OPENFILE "F.txt" FOR WRITE` | `open("F.txt", "w")` |
| open to add at the end | `OPENFILE "F.txt" FOR APPEND` | `open("F.txt", "a")` |
| read one line | `READFILE "F.txt", Line` | `line = file.readline()` or `for line in file` |
| write one line | `WRITEFILE "F.txt", Data` | `file.write(data + "\n")` |
| end of file | `EOF("F.txt")` | `readline()` returns `""`, or the `for` loop ends |
| close | `CLOSEFILE "F.txt"` | `file.close()`, or leave a `with` block |

:::def File mode
The way a file is opened, which decides what the program may do with it: `"r"` to read, `"w"` to write (the old contents are erased) and `"a"` to append (new data goes after the existing data).
:::

### Writing and reading records

To write a record, join the fields with commas, turning numbers into strings with `str()`, and end the line with `"\n"`. To read a record, take off the newline with `strip()`, cut the line into fields with `split(",")`, and **convert** the fields that are numbers with `int()` or `float()`, because every field arrives as a string.

```python
products = [("A100", "Rice", 250, 40), ("A205", "Beans", 180, 12), ("A310", "Maize flour", 140, 0)]

with open("stock.txt", "w") as file:
    for code, name, price, stock in products:
        file.write(code + "," + name + "," + str(price) + "," + str(stock) + "\n")

with open("stock.txt", "r") as file:
    for line in file:
        fields = line.strip().split(",")
        code = fields[0]
        name = fields[1]
        price = int(fields[2])
        stock = int(fields[3])
        print(name, "costs", price, "and", stock, "are in stock; value", price * stock)
```

Output:

```output
Rice costs 250 and 40 are in stock; value 10000
Beans costs 180 and 12 are in stock; value 2160
Maize flour costs 140 and 0 are in stock; value 0
```

:::key Reading a record from a text file
1. Read one line.
2. `strip()` removes the `"\n"` (and spaces) at the ends.
3. `split(",")` gives a list of strings, one per field.
4. Convert the numeric fields with `int()` or `float()`.
5. Use the fields: print them, test them or store them in an object.

Writing is the reverse: build one string from the fields, with `str()` for the numbers and `"\n"` at the end.
:::

:::warn Opening in "w" mode erases the file
`open("stock.txt", "w")` empties the file the moment it opens, even if you never write to it. If you meant to add a record to the end, use `"a"`. If you meant to change a record, you must copy or rewrite the others as well. The slip is silent: the program runs without an error and the old data is gone.
:::

:::warn A forgotten strip() leaves "\n" on the last field
In `"A100,Rice,250,40\n"` the last field is `"40\n"`, not `"40"`. `int("40\n")` happens to work, but comparing the text `"40\n" == "40"` is False, and printing it adds an empty line. Strip every line you read, before you split it.
:::

## Serial files

A serial file holds the records in the order they arrived, so the program only ever **appends**. A shop's till does this: each sale is a line holding the product code and the quantity sold. Searching has no shortcut. The program must read every record, because nothing says where a code will be.

```python
def record_sale(code, quantity):
    with open("sales.txt", "a") as file:
        file.write(code + "," + str(quantity) + "\n")

def units_sold(code):
    total = 0
    reads = 0
    with open("sales.txt", "r") as file:
        for line in file:
            reads = reads + 1
            fields = line.strip().split(",")
            if fields[0] == code:
                total = total + int(fields[1])
    return total, reads

with open("sales.txt", "w") as file:
    file.write("")
record_sale("A100", 3)
record_sale("B120", 1)
record_sale("A100", 2)
record_sale("A205", 5)
print(units_sold("A100"))
print(units_sold("C999"))
```

Output:

```output
(5, 4)
(0, 4)
```

Both searches read all four lines, even though C999 is absent and A100 appears early. A serial file has no order to use. The first statement after `def` that opens the file for writing makes the file empty before the sales are recorded, so the example starts from a clean file.

In pseudocode the same two jobs are one append and one loop. Each line holds a four-character code, a comma and the quantity, so the quantity starts at the sixth character.

```pseudocode
OPENFILE "Sales.txt" FOR APPEND
WRITEFILE "Sales.txt", Code & "," & NUM_TO_STR(Quantity)
CLOSEFILE "Sales.txt"
```

```pseudocode
DECLARE Line : STRING
DECLARE Total : INTEGER

Total ← 0
OPENFILE "Sales.txt" FOR READ
WHILE NOT EOF("Sales.txt")
   READFILE "Sales.txt", Line
   IF LEFT(Line, 4) = "A100" THEN
      Total ← Total + STR_TO_NUM(MID(Line, 6, LENGTH(Line) - 5))
   ENDIF
ENDWHILE
CLOSEFILE "Sales.txt"
OUTPUT "Units of A100 sold: ", Total
```

With the four sales above, `Total` becomes \(3 + 2 = 5\) and the output is `Units of A100 sold: 5`. The first block appends one line; it is the pseudocode for `record_sale`.

## Sequential files

In a sequential file the records are in order of a key field, here the product code in ascending order. That order lets a search **stop early**: as soon as the program reads a key greater than the one it wants, the record cannot appear later in the file.

```python
with open("stock.txt", "w") as file:
    file.write("A100,Rice,250,40\nA205,Beans,180,12\nA310,Maize flour,140,0\nB120,Cooking oil,520,8\n")

def find_record(target):
    reads = 0
    with open("stock.txt", "r") as file:
        for line in file:
            reads = reads + 1
            fields = line.strip().split(",")
            if fields[0] == target:
                return fields, reads
            if fields[0] > target:
                return None, reads
    return None, reads

for code in ["A205", "A250", "Z999"]:
    fields, reads = find_record(code)
    print(code, fields, "after", reads, "reads")
```

Output:

```output
A205 ['A205', 'Beans', '180', '12'] after 2 reads
A250 None after 3 reads
Z999 None after 4 reads
```

A205 is found at the second read. A250 is not in the file, but the program stops at the third record, A310, because A310 is greater than A250. Z999 is greater than every key, so it reads all four. Compare the serial file: it would read every line every time.

The same early-stop search in pseudocode needs three reasons to leave the loop: the record was found, the key was passed, or the end of the file was reached.

```pseudocode
DECLARE Line, FileCode : STRING
DECLARE Found, TooFar : BOOLEAN

Found ← FALSE
TooFar ← FALSE
OPENFILE "Stock.txt" FOR READ
WHILE NOT EOF("Stock.txt") AND NOT Found AND NOT TooFar
   READFILE "Stock.txt", Line
   FileCode ← LEFT(Line, 4)
   IF FileCode = Target THEN
      Found ← TRUE
   ELSE
      IF FileCode > Target THEN
         TooFar ← TRUE
      ENDIF
   ENDIF
ENDWHILE
CLOSEFILE "Stock.txt"
IF Found THEN
   OUTPUT Line
ELSE
   OUTPUT "Not found"
ENDIF
```

### Inserting, deleting and updating a record

A text file cannot have a line pushed into its middle. To change a sequential file, the program **copies it to a new file**, changing as it goes, and then the new file replaces the old one. For an insertion the copy writes the new record just before the first record with a greater key (or at the end if there is none). A deletion skips the record. An update writes the changed line in place of the old one.

```python
import os

def insert_record(new_line):
    new_key = new_line.split(",")[0]
    inserted = False
    with open("stock.txt", "r") as old, open("stock_new.txt", "w") as new:
        for line in old:
            if not inserted and line.strip().split(",")[0] > new_key:
                new.write(new_line + "\n")
                inserted = True
            new.write(line)
        if not inserted:
            new.write(new_line + "\n")
    os.replace("stock_new.txt", "stock.txt")

with open("stock.txt", "w") as file:
    file.write("A100,Rice,250,40\nA205,Beans,180,12\nA310,Maize flour,140,0\nB120,Cooking oil,520,8\n")

insert_record("A250,Sugar,200,30")
insert_record("C100,Salt,50,100")
with open("stock.txt", "r") as file:
    print(file.read(), end="")
```

Output:

```output
A100,Rice,250,40
A205,Beans,180,12
A250,Sugar,200,30
A310,Maize flour,140,0
B120,Cooking oil,520,8
C100,Salt,50,100
```

Two things in this program are worth noticing. Opening `stock.txt` for reading and `stock_new.txt` for writing in one `with` line keeps both files open together. And `os.replace` renames the new file over the old one in one step, so the old file is only replaced once the new file is complete. The record A250 was written before A310, the first key that is greater. The record C100 had no greater key, so the `if not inserted` line at the end wrote it last.

### Merging two sorted files

Two sequential files in the same key order can be combined into one in a single pass. Read one line from each, write the smaller key and read a replacement from the file it came from. When one file runs out, copy the rest of the other.

```python
with open("north.txt", "w") as file:
    file.write("A100,Rice\nA310,Maize flour\nB120,Cooking oil\n")
with open("south.txt", "w") as file:
    file.write("A205,Beans\nA250,Sugar\nC100,Salt\n")

with open("north.txt", "r") as north, open("south.txt", "r") as south, open("all.txt", "w") as merged:
    a = north.readline()
    b = south.readline()
    while a != "" and b != "":
        if a.split(",")[0] <= b.split(",")[0]:
            merged.write(a)
            a = north.readline()
        else:
            merged.write(b)
            b = south.readline()
    while a != "":
        merged.write(a)
        a = north.readline()
    while b != "":
        merged.write(b)
        b = south.readline()

with open("all.txt", "r") as file:
    print(file.read(), end="")
```

Output:

```output
A100,Rice
A205,Beans
A250,Sugar
A310,Maize flour
B120,Cooking oil
C100,Salt
```

`readline()` returns an empty string at the end of a file, so `a != ""` means "the north file still has a line". Each file is read once from start to finish, so merging \(n\) records takes about \(n\) reads, however large the files are. This is the same idea as the merge in [User-defined types, file organisation and hashing](#cs.usertypes), but with files instead of lists.

## Random files

A random file stores its records at fixed-size positions, so the program can go straight to record number \(n\) without reading the ones before it. For that to work **every record must have the same length**. In pseudocode that comes free, because the file holds records of a declared type. In Python you get it by padding each field to a fixed width.

:::html
<figure class="fig small"><svg viewBox="0 0 350 150" role="img" aria-label="A random file drawn as four boxes in a row, record 1 to record 4, each 25 bytes long. Tick marks below show where each record starts: byte 0, 25, 50, 75, and the end of the file at byte 100. An arrow labelled seek(50) points at the start of record 3. The formula under the picture is position equals n minus 1, times 25."><rect class="fm s-acc sw2" x="20" y="52" width="78" height="36"/><text class="tl tc" x="59" y="75">record 1</text><rect class="fm s-acc sw2" x="98" y="52" width="78" height="36"/><text class="tl tc" x="137" y="75">record 2</text><rect class="fm s-acc sw2" x="176" y="52" width="78" height="36"/><text class="tl tc" x="215" y="75">record 3</text><rect class="fm s-acc sw2" x="254" y="52" width="78" height="36"/><text class="tl tc" x="293" y="75">record 4</text><line class="ln-m thin" x1="20" y1="88" x2="20" y2="98"/><text class="tl tc" x="20" y="114">0</text><line class="ln-m thin" x1="98" y1="88" x2="98" y2="98"/><text class="tl tc" x="98" y="114">25</text><line class="ln-m thin" x1="176" y1="88" x2="176" y2="98"/><text class="tl tc" x="176" y="114">50</text><line class="ln-m thin" x1="254" y1="88" x2="254" y2="98"/><text class="tl tc" x="254" y="114">75</text><line class="ln-m thin" x1="332" y1="88" x2="332" y2="98"/><text class="tl tc" x="332" y="114">100</text><text class="tl tc" x="176" y="22">seek(50)</text><line class="ln" x1="176" y1="30" x2="176" y2="52" marker-end="url(#ah)"/><text class="tl" x="20" y="140">position = (n − 1) × 25</text></svg><figcaption>Four records of 25 bytes each. Record \(n\) starts at byte \((n - 1) \times 25\), so record 3 starts at byte 50, and seek(50) moves the file position there without reading records 1 and 2.</figcaption></figure>
:::

In pseudocode the commands are `SEEK` (move to the address of a record), `GETRECORD` (read the record at that address into a variable of the record type) and `PUTRECORD` (write a variable there, replacing what was stored). The guide's own example does a `SEEK` before each `GETRECORD` and `PUTRECORD`, and so does this one. To take 5 from the stock of the record at address 2:

```pseudocode
TYPE TProduct
   DECLARE Code : STRING
   DECLARE Name : STRING
   DECLARE Price : INTEGER
   DECLARE Stock : INTEGER
ENDTYPE

DECLARE Item : TProduct

OPENFILE "Stock.Dat" FOR RANDOM
SEEK "Stock.Dat", 2
GETRECORD "Stock.Dat", Item
Item.Stock ← Item.Stock - 5
SEEK "Stock.Dat", 2
PUTRECORD "Stock.Dat", Item
CLOSEFILE "Stock.Dat"
```

The record is read, changed in memory, and written back **to the same address**. No other record is touched, which is the advantage over a sequential file, where the whole file would be copied.

In Python, each record here is a text of exactly 25 characters: a code of 4, a name of 12, a price of 5, a stock of 3, and the `"\n"` that ends the line. `ljust(12)` pads a string on the right with spaces to width 12, and `rjust(5)` pads on the left. The file is opened in **binary mode** (`"wb"`, `"r+b"`) so that a position in the file is a count of bytes, and text is converted with `encode()` and `decode()`. The mode `"r+b"` allows reading and writing in the same file without erasing it.

```python
import os

RECORD_LENGTH = 25

def make_record(code, name, price, stock):
    return (code.ljust(4) + name.ljust(12) + str(price).rjust(5) + str(stock).rjust(3) + "\n").encode()

def read_record(file, number):
    file.seek((number - 1) * RECORD_LENGTH)
    text = file.read(RECORD_LENGTH).decode()
    return text[0:4], text[4:16].strip(), int(text[16:21]), int(text[21:24])

def write_record(file, number, record):
    file.seek((number - 1) * RECORD_LENGTH)
    file.write(record)

with open("stock.dat", "wb") as file:
    file.write(make_record("A100", "Rice", 250, 40))
    file.write(make_record("A205", "Beans", 180, 12))
    file.write(make_record("A310", "Maize flour", 140, 0))
    file.write(make_record("B120", "Cooking oil", 520, 8))

with open("stock.dat", "r+b") as file:
    print(read_record(file, 3))
    code, name, price, stock = read_record(file, 2)
    write_record(file, 2, make_record(code, name, price, stock - 5))
    print(read_record(file, 2))
print("file size:", os.path.getsize("stock.dat"), "bytes")
```

Output:

```output
('A310', 'Maize flour', 140, 0)
('A205', 'Beans', 180, 7)
file size: 100 bytes
```

Reading record 3 starts at byte \((3 - 1) \times 25 = 50\) and takes 25 bytes. The update of record 2 changes 12 to 7 in place, and the file is still exactly \(4 \times 25 = 100\) bytes, because the new record is the same length as the old one. That is why the fields are padded: a record that grew would overwrite the start of the next one.

A random file in a real system usually computes the record number from the key with a hashing algorithm, as in [User-defined types, file organisation and hashing](#cs.usertypes). Here the code in the example simply gives the record number to `read_record`.

:::key Choosing the right file operation
- **Serial**: append to add; read the whole file to search; never stops early.
- **Sequential**: read in key order; stop early when the key has been passed; to insert, delete or update, copy to a new file and replace the old one; merge two files in one pass.
- **Random**: fixed-length records; position = (record number − 1) × record length; `SEEK` then `GETRECORD` or `PUTRECORD` in pseudocode, `seek` then `read` or `write` in Python; update in place.
:::

:::eg Choosing the file organisation (exam style)
A school in Lagos needs three files. (a) A record of every login to the library computers, added as each login happens and read through once a term. (b) A payroll file of 300 staff, processed in full every month in order of staff number. (c) A booking file in which one seat's record must be found and changed straight away while the customer waits. For each file, state the organisation that suits it and give a reason. [6 marks]

Name the organisation first, then tie the reason to the scenario, as in [User-defined types, file organisation and hashing](#cs.usertypes).

- (a) Serial, because records are only ever added at the end in the order they happen [B1] and they are read through from start to finish, so no order or direct access is needed [B1]
- (b) Sequential, because every record is processed each month in key order [B1] and a single pass over a file already in order is quick, with no need to find one record [B1]
- (c) Random, because the record can be reached directly from its key with `SEEK`, without reading the others [B1] and can be rewritten in place, so the customer does not wait [B1]
:::

## Exceptions

:::def Exception
An event that occurs while a program is running and disrupts its normal flow, such as a file that cannot be found, a division by zero or a value that cannot be converted. If nothing handles it, the program stops with an error message.
:::

:::def Exception handling
Code that detects an exception when it happens and deals with it, so that the program can recover, report the problem clearly or end safely instead of crashing.
:::

Without handling, one bad line in a file ends the whole program. Python's common exceptions, each with a cause that matters in this chapter, are these.

| Exception | Raised when | Example |
|---|---|---|
| `FileNotFoundError` | a file that is opened for reading does not exist | `open("missing.txt", "r")` |
| `ValueError` | a value has the right type but cannot be used | `int("abc")` |
| `ZeroDivisionError` | a number is divided by zero | `total / 0` |
| `IndexError` | a list index is outside the list | `items[5]` when the list has 3 items |

### try and except

The risky code goes in a **try block**. The code that deals with a problem goes in an **except block**, naming the exception it handles.

:::def Try block
The block of code that is run first and may raise an exception. If it raises one, the rest of the block is skipped.
:::

:::def Except block
The block of code that runs when the try block raises the exception it names. It handles the problem, after which the program carries on after the whole `try` statement.
:::

```python
numbers = [4, 8, 15]

try:
    average = sum(numbers) / (len(numbers) - 3)
except ZeroDivisionError:
    print("ZeroDivisionError: the divisor was zero")

try:
    age = int("abc")
except ValueError:
    print("ValueError: 'abc' is not a whole number")

try:
    print(numbers[3])
except IndexError:
    print("IndexError: there is no item at index 3")

try:
    file = open("missing.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: missing.txt does not exist")
print("The program carries on")
```

Output:

```output
ZeroDivisionError: the divisor was zero
ValueError: 'abc' is not a whole number
IndexError: there is no item at index 3
FileNotFoundError: missing.txt does not exist
The program carries on
```

Each of the four statements would have stopped the program. Because each is inside a `try`, the program prints a message and reaches the last line.

### else and finally

Two more parts are optional. The **else block** runs only if the try block raised **no** exception: it holds the code that depends on the try having worked. The **finally block** runs **always**, whether an exception happened or not, and even if a `return` is reached first. It is the right place to close a file.

:::html
<figure class="fig small"><svg viewBox="0 0 350 310" role="img" aria-label="A flow diagram of try and except. The try block runs first. If there is no exception, control passes to the optional else block. If an exception is raised, control passes to the matching except block. Both routes then reach the optional finally block, which always runs, and the program continues."><rect class="fm s-acc sw2" x="100" y="12" width="150" height="34" rx="4"/><text class="tl tb tc" x="175" y="34">try block</text><rect class="fm s-acc sw2" x="15" y="118" width="140" height="34" rx="4"/><text class="tl tb tc" x="85" y="140">else block</text><rect class="fm s-acc sw2" x="195" y="118" width="140" height="34" rx="4"/><text class="tl tb tc" x="265" y="140">except block</text><rect class="fm s-acc sw2" x="100" y="206" width="150" height="34" rx="4"/><text class="tl tb tc" x="175" y="228">finally block</text><rect class="fm s-acc sw2" x="100" y="272" width="150" height="30" rx="4"/><text class="tl tb tc" x="175" y="294">program continues</text><line class="ln" x1="140" y1="46" x2="90" y2="118" marker-end="url(#ah)"/><line class="ln" x1="210" y1="46" x2="260" y2="118" marker-end="url(#ah)"/><line class="ln" x1="90" y1="152" x2="140" y2="206" marker-end="url(#ah)"/><line class="ln" x1="260" y1="152" x2="210" y2="206" marker-end="url(#ah)"/><line class="ln" x1="175" y1="240" x2="175" y2="272" marker-end="url(#ah)"/><text class="tl halo" x="15" y="86">none</text><text class="tl halo" x="252" y="86">exception</text></svg><figcaption>The try block runs first. With no exception the else block runs; with an exception the matching except block runs. Either way the finally block runs next. The else and finally blocks are optional.</figcaption></figure>
:::

This function totals the whole numbers in a file, one per line. It handles a missing file and a line that is not a number, and it always closes the file it opened.

```python
def read_total(name):
    total = 0
    file = None
    try:
        file = open(name, "r")
        for line in file:
            total = total + int(line.strip())
    except FileNotFoundError:
        print("Cannot find", name)
        return None
    except ValueError:
        print("A line in", name, "is not a whole number")
        return None
    else:
        print("Read", name, "without a problem")
        return total
    finally:
        if file is not None:
            file.close()
            print("Closed", name)

with open("nums.txt", "w") as f:
    f.write("10\n20\n30\n")
with open("bad.txt", "w") as f:
    f.write("10\nx\n30\n")

print(read_total("nums.txt"))
print(read_total("bad.txt"))
print(read_total("gone.txt"))
```

Output:

```output
Read nums.txt without a problem
Closed nums.txt
60
A line in bad.txt is not a whole number
Closed bad.txt
None
Cannot find gone.txt
None
```

Follow the first call: the try block succeeds, the else block prints its message and reaches `return total`, but the finally block still runs **before** the function returns, which is why "Closed nums.txt" comes before the 60. In the second call the exception happens on line 2; `bad.txt` is open at that point, so the finally block closes it. In the third call the file never opened, so `file` is still `None` and finally closes nothing.

A `with` block already closes the file for you, even when an exception happens. Use `with` for simple file code, and `finally` when something else must always happen.

### Validating input with an exception

User input is the commonest source of exceptions: `input()` returns text, and `int()` raises `ValueError` if the text is not a whole number. A loop that keeps asking until the conversion works is a standard Paper 4 pattern.

```python
def read_whole_number(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("Please type a whole number.")

quantity = read_whole_number("Quantity: ")
print("You ordered", quantity)
```

Output, when the user types `two`, then nothing, then 12:

```output
Quantity: two
Please type a whole number.
Quantity: 
Please type a whole number.
Quantity: 12
You ordered 12
```

### Raising an exception

Your own code can **raise** an exception when it finds a problem it cannot handle where it is. The caller then decides what to do.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("The amount must be positive")
    if amount > balance:
        raise ValueError("Not enough money in the account")
    return balance - amount

for request in [50, 400, -5]:
    try:
        print("New balance:", withdraw(120, request))
    except ValueError as error:
        print("Refused:", error)
```

Output:

```output
New balance: 70
Refused: Not enough money in the account
Refused: The amount must be positive
```

`as error` gives a name to the exception, so its message can be printed. The function `withdraw` does not print anything or ask the user anything. It only reports the problem, and the code that called it decides what to do about it.

### Pseudocode and exceptions

The Pseudocode Guide has no `TRY` or `EXCEPT` keywords. A question that needs exception handling in pseudocode describes it in words, for example "if the file cannot be opened, output a message and stop". Your answer then explains the same structure in plain language: what is tried, which problem is detected, and what the program does instead. In Python you write the real statements.

### When is exception handling appropriate?

:::key When to use exception handling
- **Use it** for events outside the program's control: a file that may be missing or damaged, input from a user, data from a network or a device. The program cannot prevent these, so it must be ready for them.
- **Handle the exception you expect**, naming it (`FileNotFoundError`, `ValueError`). A bare `except:` catches every error, including mistakes in your own code, and hides them.
- **Do not use it to hide a logic error.** If a loop runs off the end of a list because of a wrong bound, fix the bound. Catching `IndexError` and carrying on would leave the program giving wrong answers.
- **Prefer a simple test when one is easy**: `if len(items) > 0` is clearer than waiting for a `ZeroDivisionError`.
:::

:::exam Why exception handling is important (2 marks)
Two points earn the marks: the program **does not crash or stop unexpectedly** when something goes wrong, and it can **recover, or give the user a clear message**, so no data is lost and the user knows what to do. Examples that fit: a missing file, invalid input, a full disk.
:::

## A complete Paper 4 style task

Paper 4 tasks give you a text file and ask you to read it, process it and output a result. This is a typical one. A courier company in Quito keeps its parcels in `Parcels.txt`, one parcel per line: the parcel ID, the destination city and the mass in grams.

:::eg Reading records into objects, with a missing file (exam style)
The file `Parcels.txt` holds these five lines.

```text
PX101,Quito,2400
PX102,Lima,850
PX103,Quito,1200
PX104,Bogota,3100
PX105,Lima,500
```

Write a Python program that: (a) defines a class `Parcel` for one parcel; (b) has a function `load_parcels(filename)` that reads every parcel into a list of `Parcel` objects and returns the list, and if the file is not found outputs `File not found:` followed by the file name and returns an empty list; (c) outputs the number of parcels, the total mass in kilograms, the ID and mass of the heaviest parcel and the number of parcels for Quito. [10 marks]

The first lines of the program create the sample file so that it can be run on its own; in the exam the file is given to you.

```python
class Parcel:
    def __init__(self, parcel_id, city, grams):
        self.parcel_id = parcel_id
        self.city = city
        self.grams = grams

def load_parcels(filename):
    parcels = []
    try:
        with open(filename, "r") as file:
            for line in file:
                fields = line.strip().split(",")
                parcels.append(Parcel(fields[0], fields[1], int(fields[2])))
    except FileNotFoundError:
        print("File not found:", filename)
    return parcels

with open("Parcels.txt", "w") as file:
    file.write("PX101,Quito,2400\nPX102,Lima,850\nPX103,Quito,1200\nPX104,Bogota,3100\nPX105,Lima,500\n")

parcels = load_parcels("Parcels.txt")
total = 0
heaviest = parcels[0]
quito_count = 0
for parcel in parcels:
    total = total + parcel.grams
    if parcel.grams > heaviest.grams:
        heaviest = parcel
    if parcel.city == "Quito":
        quito_count = quito_count + 1
print("Parcels:", len(parcels))
print("Total mass:", total / 1000, "kg")
print("Heaviest:", heaviest.parcel_id, "with", heaviest.grams, "g")
print("Parcels for Quito:", quito_count)
print(len(load_parcels("Missing.txt")))
```

Output:

```output
Parcels: 5
Total mass: 8.05 kg
Heaviest: PX104 with 3100 g
Parcels for Quito: 2
File not found: Missing.txt
0
```

The last line tests the missing file: the function prints its message and returns an empty list, so the length is 0 and the program does not crash. The total mass is \(2400 + 850 + 1200 + 3100 + 500 = 8050\) g, which is 8.05 kg.

- class `Parcel` with an `__init__` that stores the three attributes [B1]
- file opened for reading (with `open(..., "r")`) and every line read in a loop [B1]
- `strip()` and `split(",")` used on each line [B1]
- mass converted with `int()` [B1]
- a `Parcel` object created for each line and added to the list [B1]
- `except FileNotFoundError` around the file handling [B1]
- message `File not found:` and the file name output, and an empty list returned [B1]
- total mass and the heaviest parcel found with a loop [B1]
- number of parcels for Quito counted [B1]
- all four results output correctly, with the mass converted to kilograms [B1]
:::

Here is a second task on the same data: write the parcels to a new file in order of mass, heaviest first. A sort works on the list of objects and the new file is written afterwards.

```python
class Parcel:
    def __init__(self, parcel_id, city, grams):
        self.parcel_id = parcel_id
        self.city = city
        self.grams = grams

parcels = [Parcel("PX101", "Quito", 2400), Parcel("PX102", "Lima", 850), Parcel("PX103", "Quito", 1200),
           Parcel("PX104", "Bogota", 3100), Parcel("PX105", "Lima", 500)]

for boundary in range(len(parcels) - 1, 0, -1):
    for j in range(boundary):
        if parcels[j].grams < parcels[j + 1].grams:
            temp = parcels[j]
            parcels[j] = parcels[j + 1]
            parcels[j + 1] = temp

with open("Heaviest.txt", "w") as file:
    for parcel in parcels:
        file.write(parcel.parcel_id + "," + parcel.city + "," + str(parcel.grams) + "\n")

with open("Heaviest.txt", "r") as file:
    print(file.read(), end="")
```

Output:

```output
PX104,Bogota,3100
PX101,Quito,2400
PX103,Quito,1200
PX102,Lima,850
PX105,Lima,500
```

The sort is the bubble sort from [Data types, records and arrays](#cs.datatypes), with the comparison turned round (`<`) so that the larger mass moves to the front, and it swaps whole **objects**, so each parcel keeps its own city and ID.

:::eg Spot the error: adding a visitor to a log
A museum in Accra keeps `visitors.txt`, one name per line. A student wrote a function to add a visitor, then tested it on a file that held Ana and Ben.

```python
with open("visitors.txt", "w") as file:
    file.write("Ana\nBen\n")

def add_visitor(name):
    with open("visitors.txt", "w") as file:
        file.write(name + "\n")

add_visitor("Chen")
with open("visitors.txt", "r") as file:
    print(file.read(), end="")
```

Output:

```output
Chen
```

**Question:** Identify the mistake, say what was lost and give the correction. [3 marks]

- Mistake: the file is opened in `"w"` mode, which erases the existing contents [B1]
- Effect: Ana and Ben were lost, and the file now holds only Chen [B1]
- Fix: open the file in `"a"` mode (append), so the new name goes after the existing lines [B1]

The program raised no error, which makes this slip hard to see. Test a file function on a file that already holds data, not only on an empty one.
:::

:::warn Three slips with exceptions
These lose marks again and again.

- **A bare `except:`** that catches everything. It hides mistakes, so the program carries on with wrong results. Name the exception: `except FileNotFoundError:`.
- **Closing a file that never opened.** If `open` raises an exception, there is no file to close. Use a `with` block, or test that the file was opened (`if file is not None`) before closing it in `finally`.
- **Putting too much in the try block.** Keep the `try` to the statements that can raise the exception, so that an unrelated mistake does not get caught by accident.
:::

:::try Start easy, finish at exam standard
Q: State the file mode (read, write or append) that you would use to add a new line to the end of an existing log file.
A: Append (`"a"` in Python, `FOR APPEND` in pseudocode).
Q: A line read from a file is `"B120,Cooking oil,520,8\n"`. Write the Python statements that give the price as an integer.
A: `fields = line.strip().split(",")` then `price = int(fields[2])`, so the price is 520.
Q: What is the output? `try:` then `print(int("12"))`, `print(int("x"))`, `print("done")` then `except ValueError:` then `print("bad")`. (The three `print` statements are all inside the `try` block.)
A: The first `print` outputs 12. The second raises a `ValueError`, so the rest of the try block is skipped and `bad` is output. The output is `12` then `bad`. `done` is never printed.
Q: In a serial file of 500 records, how many records must be read, at most, to find one with a given key? What about a sequential file whose key is not in the file?
A: A serial file needs up to 500 reads, because the key could be the last record or absent. In a sequential file the search stops when a key greater than the wanted one is read, which can be well before the end.
Q: Records in a random file are 40 bytes long and the first record starts at byte 0. At which byte does record 6 start?
A: \((6 - 1) \times 40 = 200\).
Q: Give one example of an exception that can happen when a program reads a file, and one that can happen when it reads a number typed by the user.
A: A file: `FileNotFoundError` (the file is missing). A typed number: `ValueError` (the text is not a whole number).
Q: Why is `except:` with no exception name poor practice?
A: It catches every error, including mistakes in the program itself, so a bug is hidden and the program carries on with wrong results.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ A program uses these Python statements. (a) `open("report.txt", "w")` to create each day's report (b) `open("log.txt", "a")` to record each login (c) `open("settings.txt", "r")` to load settings. State the effect of each mode, and what would happen to the existing log if `"w"` were used by mistake in (b).
A: One mark each.

- (a) `"w"` creates the file, or empties it if it exists, so each day starts a new report [B1]
- (b) `"a"` adds new lines after the existing ones, so earlier logins are kept [B1]
- (c) `"r"` opens the file only to read it; it must already exist [B1]
- `"w"` in (b) would erase all the earlier logins each time the file was opened [B1]

Q: [2 marks] ★ Explain why exception handling is important in a program that reads files supplied by users.
A: One mark per point, up to two.

- the program does not crash if the file is missing or contains invalid data [B1]
- the program can display a helpful message or recover, for example ask for another file [B1]
- (accept: files can be closed safely so that no data is lost)

Q: [4 marks] ★★ State the output of this program. The function is called twice.

```python
def share(total, people):
    try:
        result = total // people
    except ZeroDivisionError:
        print("nobody to share with")
        return 0
    else:
        print("shared")
        return result
    finally:
        print("done")

print(share(20, 4))
print(share(20, 0))
```

H: The finally block runs before the function returns its value.
H: `20 // 0` raises ZeroDivisionError, so the else block is skipped.
A: The output is:

```output
shared
done
5
nobody to share with
done
0
```

- `shared` is output first by the else block [B1]
- `done` is output by finally, then 5 is printed (so 5 comes after `done`) [B1]
- `nobody to share with` is output for the second call, and the else block does not run [B1]
- `done` is output again, then 0 is printed [B1]

Q: [5 marks] ★★ A visitors' log, `Log.txt`, has one entry per line: a name, a comma and a two-digit hour, such as `Ana,09`. Write pseudocode to output how many entries have an hour of 12 or later.
H: The hour is the last two characters of the line: use `RIGHT` and `STR_TO_NUM`.
A: One possible answer:

```pseudocode
DECLARE Line : STRING
DECLARE Count : INTEGER

Count ← 0
OPENFILE "Log.txt" FOR READ
WHILE NOT EOF("Log.txt")
   READFILE "Log.txt", Line
   IF STR_TO_NUM(RIGHT(Line, 2)) >= 12 THEN
      Count ← Count + 1
   ENDIF
ENDWHILE
CLOSEFILE "Log.txt"
OUTPUT "Late entries: ", Count
```

- file opened FOR READ and closed at the end [B1]
- loop that repeats until `EOF` is true, with `READFILE` inside the loop [B1]
- the hour taken from the line (`RIGHT(Line, 2)`) and converted to a number [B1]
- compared with 12 and a counter increased when it is 12 or more [B1]
- count initialised to 0 before the loop and output after it [B1]

Q: [6 marks] ★★ A sequential file `Products.txt` holds one product per line, in ascending order of the product code: `C100,Pens,40`, `C140,Ink,15` and `C200,Paper,60`. Write a Python function `insert(new_line)` that adds a new line to the file in the correct position and keeps the file in order, using a second file. Show the file after `insert("C170,Tape,25")`.
H: Copy the lines to the new file one at a time. Write the new line just before the first line whose code is greater.
H: A new line with the largest code must still be written: test for that after the loop.
A: One possible answer:

```python
import os

def insert(new_line):
    new_code = new_line.split(",")[0]
    inserted = False
    with open("Products.txt", "r") as old, open("Products_new.txt", "w") as new:
        for line in old:
            if not inserted and line.split(",")[0] > new_code:
                new.write(new_line + "\n")
                inserted = True
            new.write(line)
        if not inserted:
            new.write(new_line + "\n")
    os.replace("Products_new.txt", "Products.txt")

with open("Products.txt", "w") as file:
    file.write("C100,Pens,40\nC140,Ink,15\nC200,Paper,60\n")
insert("C170,Tape,25")
with open("Products.txt", "r") as file:
    print(file.read(), end="")
```

```output
C100,Pens,40
C140,Ink,15
C170,Tape,25
C200,Paper,60
```

- original file opened for reading and a new file opened for writing [B1]
- each line is read in a loop and copied to the new file [B1]
- the code of the new line is compared with the code of each line [B1]
- the new line is written before the first greater code, and only once (a flag) [B1]
- a new line with the greatest code is written after the loop [B1]
- the new file replaces the old file (or the old file is overwritten from the new one) [B1]

Q: [4 marks] ★★ A random file stores records that are each 30 bytes long. The first record starts at byte 0. (a) Calculate the byte at which record 12 starts. (b) Write the Python statement that moves the file position there, for a file object `file`. (c) Explain why every record in a random file must have the same length.
A: One mark per point.

- (a) \((12 - 1) \times 30 = 330\) [B1]
- (b) `file.seek(330)` (or `file.seek((12 - 1) * 30)`) [B1]
- (c) the position of a record is calculated by multiplying the record number by the record length, so that only works if every record is the same size [B1]
- a longer record would overwrite the start of the next record when written in place, and a shorter one would leave the position of later records wrong [B1]

Q: [10 marks] ★★★ A weather centre in Kenya stores readings in `Rain.txt`, one per line: the station name and the rainfall in millimetres, separated by a comma. Some lines may hold `n/a` instead of a number. The file holds these lines.

```text
Nakuru,12
Kisumu,31
Mombasa,n/a
Eldoret,18
Nyeri,9
```

Write a Python program with a class `Reading` and a function `load(filename)` that reads the valid readings into a list of objects, skips and counts lines whose rainfall is not a whole number, and handles a missing file by outputting a message. Output the number of valid readings, the number of skipped lines, the total rainfall, the wettest station and the number of stations with more than 10 mm.
H: Put the `int()` conversion in its own `try` inside the loop, so one bad line does not stop the others.
H: Use a second `try` (or the same function) around `open` for the missing file.
A: One possible answer:

```python
class Reading:
    def __init__(self, station, rainfall):
        self.station = station
        self.rainfall = rainfall

skipped = 0

def load(filename):
    global skipped
    readings = []
    try:
        with open(filename, "r") as file:
            for line in file:
                fields = line.strip().split(",")
                try:
                    readings.append(Reading(fields[0], int(fields[1])))
                except ValueError:
                    skipped = skipped + 1
    except FileNotFoundError:
        print("Cannot open", filename)
    return readings

with open("Rain.txt", "w") as file:
    file.write("Nakuru,12\nKisumu,31\nMombasa,n/a\nEldoret,18\nNyeri,9\n")

readings = load("Rain.txt")
total = 0
wettest = readings[0]
wet_count = 0
for reading in readings:
    total = total + reading.rainfall
    if reading.rainfall > wettest.rainfall:
        wettest = reading
    if reading.rainfall > 10:
        wet_count = wet_count + 1
print("Valid readings:", len(readings))
print("Skipped lines:", skipped)
print("Total rainfall:", total, "mm")
print("Wettest:", wettest.station)
print("Stations over 10 mm:", wet_count)
```

```output
Valid readings: 4
Skipped lines: 1
Total rainfall: 70 mm
Wettest: Kisumu
Stations over 10 mm: 3
```

- class `Reading` with `__init__` storing the station and the rainfall [B1]
- file opened for reading and each line read in a loop [B1]
- `strip()` and `split(",")` used [B1]
- rainfall converted with `int()` inside a `try` [B1]
- `except ValueError` that counts the bad line and carries on [B1]
- `except FileNotFoundError` around the file handling, with a message [B1]
- valid readings stored as objects in a list [B1]
- total rainfall and the number over 10 mm calculated [B1]
- wettest station found with a loop [B1]
- all five results output [B1]

Q: [6 marks] ★★★ A list `readings` holds four `Reading` objects (attributes `station` and `rainfall`): `Nakuru` 12, `Kisumu` 31, `Eldoret` 18 and `Nyeri` 9. Write Python to sort the list into descending order of rainfall using a sort you write yourself, then write the sorted readings to the file `Sorted.txt`, one per line as `station,rainfall`.
H: Swap whole objects, not just the rainfall values.
H: Open the new file in `"w"` mode and write the list in its sorted order.
A: One possible answer:

```python
class Reading:
    def __init__(self, station, rainfall):
        self.station = station
        self.rainfall = rainfall

readings = [Reading("Nakuru", 12), Reading("Kisumu", 31), Reading("Eldoret", 18), Reading("Nyeri", 9)]

for boundary in range(len(readings) - 1, 0, -1):
    for j in range(boundary):
        if readings[j].rainfall < readings[j + 1].rainfall:
            temp = readings[j]
            readings[j] = readings[j + 1]
            readings[j + 1] = temp

with open("Sorted.txt", "w") as file:
    for reading in readings:
        file.write(reading.station + "," + str(reading.rainfall) + "\n")

with open("Sorted.txt", "r") as file:
    print(file.read(), end="")
```

```output
Kisumu,31
Eldoret,18
Nakuru,12
Nyeri,9
```

- nested loops that compare neighbouring objects [B1]
- comparison that puts the larger rainfall first (descending) [B1]
- the whole objects swapped using a temporary variable [B1]
- file opened in `"w"` mode for output [B1]
- every object written as `station,rainfall` with `str()` for the number [B1]
- a newline written after each record, and the file closed (or a `with` block used) [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Two sequential files hold records in ascending order of a three-digit key. `Q1.txt` holds `105,Aziz`, `120,Bea` and `160,Carlos`. `Q2.txt` holds `110,Dara`, `120,Eli` and `170,Femi`. Write Python to merge them into `Merged.txt`, in key order. If the same key is in both files, write the record from `Q1.txt` only and skip the one from `Q2.txt`.
H: Work through both files together, as in the merge in this chapter, but when the keys are equal, read the next line from **both** files.
H: When one file has run out, copy the rest of the other.
A: One possible answer:

```python
with open("Q1.txt", "w") as file:
    file.write("105,Aziz\n120,Bea\n160,Carlos\n")
with open("Q2.txt", "w") as file:
    file.write("110,Dara\n120,Eli\n170,Femi\n")

with open("Q1.txt", "r") as first, open("Q2.txt", "r") as second, open("Merged.txt", "w") as merged:
    a = first.readline()
    b = second.readline()
    while a != "" and b != "":
        key_a = int(a.split(",")[0])
        key_b = int(b.split(",")[0])
        if key_a < key_b:
            merged.write(a)
            a = first.readline()
        elif key_a > key_b:
            merged.write(b)
            b = second.readline()
        else:
            merged.write(a)
            a = first.readline()
            b = second.readline()
    while a != "":
        merged.write(a)
        a = first.readline()
    while b != "":
        merged.write(b)
        b = second.readline()

with open("Merged.txt", "r") as file:
    print(file.read(), end="")
```

```output
105,Aziz
110,Dara
120,Bea
160,Carlos
170,Femi
```

- one line read from each file before the loop, and the loop runs while both have lines [B1]
- keys compared as numbers (`int`) [B1]
- the smaller key is written and the next line read from that file only [B1]
- equal keys: the record from `Q1.txt` is written, and a line is read from both files [B1]
- the remaining lines of whichever file is not finished are copied after the loop [B1]
- the result has each key once, in ascending order, with `120,Eli` omitted [B1]

Q: [5 marks] ★★★ Write a function `check_mark(text)` that returns the mark as an integer, and **raises** a `ValueError` with the message `not a whole number` if the text cannot be converted, or `out of range` if the mark is below 0 or above 100. Then write a loop that calls it on the texts `72`, `abc`, `130`, `-4` and `100`, and outputs either `Mark:` and the value or `Rejected`, the text, a dash and the message.
H: Convert inside a `try`. If it fails, raise a new `ValueError` with your own message.
H: The loop needs its own `try` and `except ValueError as error`.
A: One possible answer:

```python
def check_mark(text):
    try:
        mark = int(text)
    except ValueError:
        raise ValueError("not a whole number")
    if mark < 0 or mark > 100:
        raise ValueError("out of range")
    return mark

for text in ["72", "abc", "130", "-4", "100"]:
    try:
        print("Mark:", check_mark(text))
    except ValueError as error:
        print("Rejected", text, "-", error)
```

```output
Mark: 72
Rejected abc - not a whole number
Rejected 130 - out of range
Rejected -4 - out of range
Mark: 100
```

- conversion with `int()` inside a `try` in the function [B1]
- a `ValueError` raised with the message `not a whole number` when the conversion fails [B1]
- a `ValueError` raised with the message `out of range` for marks below 0 or above 100 [B1]
- the loop calls the function inside a `try` with `except ValueError as error` [B1]
- the right line is output for each of the five texts [B1]
:::

:::quiz
? A file already holds ten records. A program opens it with `open("data.txt", "w")` and writes one record. How many records does the file hold afterwards?
- 11
- 10
+ 1
- 0
> `"w"` erases the contents when the file is opened, so only the new record remains. To keep the ten and add one, the mode is `"a"`.
? Why does `"A100,Rice,250,40\n".split(",")[3]` not equal `"40"`?
- `split` always loses the last field.
+ the last field still has the newline character, `"40\n"`
- the fields are numbers, not strings
- `split(",")` starts counting at 1
> The line was not stripped. `strip()` removes the `"\n"` before the split, and the last field is then `"40"`.
? Which statement about searching a sequential file is correct?
- It must always read every record.
+ It can stop as soon as it reads a key greater than the one it is looking for.
- It can go straight to any record.
- It needs fixed-length records.
> Because the keys are in order, a larger key means the wanted key cannot come later. A serial file cannot do this, and direct access belongs to random files.
? Records in a random file are 50 bytes long. At which byte does record 4 start, if record 1 starts at byte 0?
- 200
+ 150
- 100
- 50
> The position is \((4 - 1) \times 50 = 150\). 200 forgets to subtract 1, as if records were numbered from 0.
? What is the purpose of a `finally` block?
- It runs only when an exception has occurred.
- It runs only when no exception has occurred.
+ It runs whether or not an exception occurred, for example to close a file.
- It stops the program.
> `else` is the block for no exception and `except` is the block for an exception. `finally` always runs.
? Which is the best reason NOT to write a bare `except:` around a whole program?
- It makes the program slower.
- Python does not allow it.
+ It catches errors in the program's own logic, hiding them.
- It stops the program from closing files.
> A bare `except:` catches every exception, so a mistake such as a wrong index would be swallowed and the program would carry on with wrong results. Name the exception you expect.
? A function `withdraw` finds that the amount is more than the balance. Which is the better design?
- Print a message and carry on, as if the withdrawal worked.
+ Raise a `ValueError`, and let the code that called it decide what to do.
- Return the balance with no sign that anything went wrong.
- Close the program.
> Raising an exception reports the problem to the caller without hiding it. The caller can show a message, ask again or stop.
:::

:::checklist What you can now do
- [ ] I can open a text file for reading, writing and appending, and close it (or use `with`).
- [ ] I can read a record from a file, using `strip()`, `split(",")` and type conversion, and write a record as one line.
- [ ] I can process a serial file by appending records and reading the whole file to search.
- [ ] I can process a sequential file: search and stop early, and insert, delete or update by copying to a new file.
- [ ] I can merge two sorted files in one pass.
- [ ] I can process a random file with fixed-length records using `SEEK`, `GETRECORD` and `PUTRECORD`, and `seek` in Python, and calculate a record's position.
- [ ] I can explain what an exception is and why exception handling is important.
- [ ] I can write `try`, `except`, `else` and `finally` code for a missing file, bad input and division by zero.
- [ ] I can say when exception handling is appropriate and when it is not.
:::

:::recap
- A text file holds a record per line, with comma-separated fields. Read: `strip()`, `split(",")`, convert. Write: join with commas, `str()` for numbers, `"\n"` at the end.
- Modes: `"r"` read, `"w"` write (**erases**), `"a"` append. A `with` block closes the file.
- **Serial**: append to add, read all to search. **Sequential**: in key order, so a search can stop early; insert, delete and update by copying to a new file; merge in one pass. **Random**: fixed-length records, position = (n − 1) × record length, update in place.
- Pseudocode random files: `SEEK`, then `GETRECORD` or `PUTRECORD`, and `SEEK` again before writing the record back.
- An **exception** is a run-time event that disrupts the program, such as `FileNotFoundError`, `ValueError`, `ZeroDivisionError` or `IndexError`. **Exception handling** deals with it so the program does not crash.
- `try` (risky code), `except` (handle it), `else` (no exception), `finally` (always runs); `raise` makes your own exception. Name the exception, never use a bare `except:`, and do not use handling to hide logic errors.
- Pseudocode has no exception keywords: a question describes the handling in words.
:::

:::links
- practise: [File processing and exception handling: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/20-further-programming-/file-processing-and-exception-handling/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- read: [Reading and writing files](https://docs.python.org/3/tutorial/inputoutput.html) · Python.org · the official tutorial on `open`, `with` and reading lines
- read: [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html) · Python.org · `try`, `except`, `else`, `finally` and `raise` explained
- read: [Python file handling](https://www.w3schools.com/python/python_file_handling.asp) · W3Schools · short lessons with try-it boxes
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste a function from this chapter and step through a `try` and `finally`
- practise: [Exercism Python](https://exercism.org/tracks/python) · Exercism · free exercises with feedback

Links checked 13 November 2026.
:::

Next: [Python for Paper 4: the practical toolkit](#cs.python)
