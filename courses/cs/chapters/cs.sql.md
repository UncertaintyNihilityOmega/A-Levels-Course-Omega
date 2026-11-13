@chapter cs.sql
@title DBMS and SQL
@level as
@paper CAIE 9618 Paper 1
@time 5–7 hours
@summary The language every database system understands. You will learn what DDL and DML are, write CREATE TABLE statements with keys, ask questions with SELECT (WHERE, ORDER BY, GROUP BY, INNER JOIN, SUM, COUNT, AVG), change data with INSERT, UPDATE and DELETE, and read a query to say what it outputs.

:::why
A database is only useful if you can create it, fill it and ask it questions. SQL (Structured Query Language) is how you do all three, in almost every database system in the world. Paper 1 gives you a database design and asks you to write the statements for it, or gives you a statement and asks what it does. Both skills come from a handful of patterns, and every pattern here is run against real data, so you can see exactly what comes out.
:::

**Before you start**, you should know tables, primary keys and foreign keys from [Databases: the relational model and normalisation](#cs.databases), and the data types from [Data types, records and arrays](#cs.datatypes).

:::try Warm-up
Q: Which kind of key links a record in one table to a record in another? (from [Databases: the relational model and normalisation](#cs.databases))
A: A foreign key. It holds the primary key values of the other table.
Q: Which data type would you use for a club fee of 12.50, and which for a club code such as "CO01"? (from [Data types, records and arrays](#cs.datatypes))
A: REAL for the fee (it has a fractional part) and STRING for the code (text that is never used in arithmetic). SQL calls the string type VARCHAR.
Q: Which part of the DBMS receives a query, finds an efficient way to carry it out, and runs it? (from [Databases: the relational model and normalisation](#cs.databases))
A: The query processor.
:::

## What SQL is

You met the DBMS in the last chapter: the software between the users and the stored data. You talk to it in a language, and the language the industry has agreed on is **SQL**. SQL has two jobs, and the syllabus gives each its own name.

:::def Structured Query Language (SQL)
The standard language for working with a relational database. The same language is used to define the structure of a database and to query and change the data in it.
:::

:::def Data definition language (DDL)
The part of SQL used to create and change the structure of a database: its tables, fields, data types and keys. Examples: CREATE DATABASE, CREATE TABLE, ALTER TABLE.
:::

:::def Data manipulation language (DML)
The part of SQL used to retrieve and maintain the data in the tables: asking questions with SELECT, and adding, changing and removing records with INSERT INTO, UPDATE and DELETE FROM.
:::

:::def Query
A request to the DBMS for data that meets stated conditions, written in SQL (for example, with SELECT). The DBMS's query processor carries it out and returns the result.
:::

| Job | Part of SQL | Statements in this chapter |
|---|---|---|
| Build or change the structure | DDL | CREATE DATABASE, CREATE TABLE, ALTER TABLE, PRIMARY KEY, FOREIGN KEY |
| Ask questions | DML | SELECT … FROM, WHERE, ORDER BY, GROUP BY, INNER JOIN, SUM, COUNT, AVG |
| Maintain the data | DML | INSERT INTO, UPDATE, DELETE FROM |

The syllabus asks for a limited set of statements, and queries on **at most two tables**. SQL itself has many more, and you will not need them in the exam. This chapter uses only the statements above.

:::note How SQL is written in this course
Keywords are written in capitals and each clause starts a new line, which makes a statement easy to read. A statement ends with a semicolon. Text values go in single quotes (`'Chess'`), numbers do not (`50`). The names of tables and fields are the ones in the question: copy them exactly.
:::

## The data used in this chapter

The examples use two tables from a school's clubs database. In the last chapter a student could join many clubs through a link table. A query may use only two tables, so here each student's one **main club** is stored in STUDENT. ClubCode in STUDENT is a foreign key to the primary key ClubCode in CLUB.

**Club**

| ClubCode | ClubName | MeetingDay | Room | Fee |
|---|---|---|---|---|
| CH01 | Chess | Monday | B12 | 5.00 |
| CO01 | Coding | Tuesday | L3 | 12.50 |
| DR01 | Drama | Wednesday | Hall | 8.00 |
| FB01 | Football | Thursday | Field | 10.00 |
| RB01 | Robotics | Friday | L3 | 15.00 |
| SW01 | Swimming | Saturday | Pool | 20.00 |

**Student**

| StudentID | FirstName | Form | BirthDate | Points | ClubCode |
|---|---|---|---|---|---|
| 101 | Amina | 10A | 2011-03-14 | 46 | CO01 |
| 102 | Bilal | 10A | 2011-07-02 | 31 | FB01 |
| 103 | Chioma | 10B | 2010-11-23 | 58 | CH01 |
| 104 | Dev | 10B | 2011-01-30 | 24 | RB01 |
| 105 | Elena | 11A | 2010-05-19 | 67 | DR01 |
| 106 | Farid | 11A | 2010-09-08 | 39 | CO01 |
| 107 | Grace | 11B | 2010-12-01 | 52 | FB01 |
| 108 | Hiro | 11B | 2011-02-17 | 41 | CO01 |
| 109 | Ingrid | 10A | 2011-08-25 | 29 | DR01 |
| 110 | Jamal | 10B | 2011-04-09 | 35 | RB01 |
| 111 | Kofi | 11A | 2010-06-30 | 63 | CH01 |
| 112 | Lucia | 11B | 2010-10-12 | 55 | CO01 |

Points are house points that students earn. Swimming has no students yet, and that detail matters later. In the examples below, each answer is the result of running the statement on exactly these rows.

## Data definition: creating the structure

The DBMS carries out all creation and changing of the structure with DDL. You start with the database itself.

```text
CREATE DATABASE SchoolClubs;
```

Then you create each table, naming its fields and giving every field a data type. The syllabus lists seven.

| Data type | Holds | Example value |
|---|---|---|
| CHARACTER | exactly one character | `'Y'` |
| VARCHAR(n) | text of up to n characters | `'Chioma'` |
| BOOLEAN | TRUE or FALSE | TRUE |
| INTEGER | a whole number | `46` |
| REAL | a number with a fractional part | `12.5` |
| DATE | a calendar date | `'2026-11-13'` |
| TIME | a time of day | `'15:30:00'` |

A date or a time is written as text in quotes. This course writes dates year first (`'2011-03-14'`), which also puts them in the right order when sorted; use the layout the question shows.

Two keys are declared inside CREATE TABLE. `PRIMARY KEY (field)` names the primary key, and `FOREIGN KEY (field) REFERENCES Table (Field)` says which field links to which other table. A foreign key can only point at a table that exists, so you **create the table that is referred to first**.

:::key CREATE TABLE
```text
CREATE TABLE TableName (
   Field1 DataType,
   Field2 DataType,
   PRIMARY KEY (Field1),
   FOREIGN KEY (Field2) REFERENCES OtherTable (OtherField)
);
```
Fields are separated by commas, with no comma after the last line. The table that is referred to is created first.
:::

The two tables of the clubs database, CLUB first:

```text
CREATE TABLE Club (
   ClubCode VARCHAR(4),
   ClubName VARCHAR(20),
   MeetingDay VARCHAR(9),
   Room VARCHAR(5),
   Fee REAL,
   PRIMARY KEY (ClubCode)
);
```

```text
CREATE TABLE Student (
   StudentID INTEGER,
   FirstName VARCHAR(15),
   Form VARCHAR(3),
   BirthDate DATE,
   Points INTEGER,
   ClubCode VARCHAR(4),
   PRIMARY KEY (StudentID),
   FOREIGN KEY (ClubCode) REFERENCES Club (ClubCode)
);
```

Read the second statement line by line. StudentID is a whole number and the primary key. ClubCode is text of up to 4 characters, and the `FOREIGN KEY` line says its values must match a ClubCode in Club. That line is what gives the DBMS the information it needs to enforce referential integrity (see [Databases: the relational model and normalisation](#cs.databases)).

### Changing a table

Tables change as needs change. `ALTER TABLE` changes the definition of a table that already exists. The most common change is adding a field. The new field is empty for every record that is already in the table.

```text
ALTER TABLE Student ADD Email VARCHAR(40);
```

(Some systems write `ADD COLUMN`. The meaning is the same.)

:::eg Write a CREATE TABLE statement (exam style)
A clinic in Lahore stores appointments in a table called Appointment. Each appointment has an AppointmentID (a whole number, the primary key), a PatientID (a whole number that links to the PatientID in the table Patient), the date of the appointment, the start time, and whether the appointment has been confirmed (true or false). Write the SQL statement to create the table Appointment. [5 marks]

Work down the description and give every item a name and a type. The first fields are the ones you name; the keys come last.

```text
CREATE TABLE Appointment (
   AppointmentID INTEGER,
   PatientID INTEGER,
   AppointmentDate DATE,
   StartTime TIME,
   Confirmed BOOLEAN,
   PRIMARY KEY (AppointmentID),
   FOREIGN KEY (PatientID) REFERENCES Patient (PatientID)
);
```

- `CREATE TABLE Appointment` with the field list in brackets, separated by commas [B1]
- AppointmentID and PatientID given the type INTEGER [B1]
- date, time and confirmed given DATE, TIME and BOOLEAN [B1]
- `PRIMARY KEY (AppointmentID)` [B1]
- `FOREIGN KEY (PatientID) REFERENCES Patient (PatientID)` [B1]

(The name of the date field is your choice; the data types are what score. A time stored as text, such as VARCHAR(5), does not earn the TIME mark.)
:::

## Querying data with SELECT

A SELECT statement reads data and never changes it. It says **which fields** to show, **which table** to take them from, and then, optionally, which rows, in what order and how to summarise them.

### SELECT … FROM

`SELECT` is followed by the fields you want, separated by commas, and `FROM` names the table. A star `*` means every field.

```text
SELECT *
FROM Club;
```

| ClubCode | ClubName | MeetingDay | Room | Fee |
|---|---|---|---|---|
| CH01 | Chess | Monday | B12 | 5.00 |
| CO01 | Coding | Tuesday | L3 | 12.50 |
| DR01 | Drama | Wednesday | Hall | 8.00 |
| FB01 | Football | Thursday | Field | 10.00 |
| RB01 | Robotics | Friday | L3 | 15.00 |
| SW01 | Swimming | Saturday | Pool | 20.00 |

To see only some fields, name them. The result has only those columns, in the order you wrote them.

```text
SELECT FirstName, Form
FROM Student;
```

| FirstName | Form |
|---|---|
| Amina | 10A |
| Bilal | 10A |
| Chioma | 10B |
| Dev | 10B |
| Elena | 11A |
| Farid | 11A |
| Grace | 11B |
| Hiro | 11B |
| Ingrid | 10A |
| Jamal | 10B |
| Kofi | 11A |
| Lucia | 11B |

Rows come back in whatever order the DBMS finds convenient (here the order they were entered). Only `ORDER BY` guarantees an order.

### WHERE: choosing rows

`WHERE` keeps only the rows for which a condition is true. A condition compares a field with a value.

| Operator | Meaning |
|---|---|
| `=` | equal to |
| `<>` | not equal to |
| `<` and `<=` | less than; less than or equal to |
| `>` and `>=` | greater than; greater than or equal to |

```text
SELECT FirstName, Points
FROM Student
WHERE Points > 50;
```

| FirstName | Points |
|---|---|
| Chioma | 58 |
| Elena | 67 |
| Grace | 52 |
| Kofi | 63 |
| Lucia | 55 |

The result has five rows: Points 58, 67, 52, 63 and 55 are all above 50.

:::warn Text in quotes, numbers without
`Points > 50` compares with a number, which has no quotes. `Form = '10A'` compares with text, which does. Without the quotes, SQL takes `10A` for the name of a field and fails. In reverse, `Points > '50'` compares with the text "50", which sorts differently from the number 50. Match the quotes to the data type of the field.
:::

```text
SELECT FirstName, Form
FROM Student
WHERE Form = '10A';
```

| FirstName | Form |
|---|---|
| Amina | 10A |
| Bilal | 10A |
| Ingrid | 10A |

Dates compare in the same way, as text in quotes. This finds the students born before 1 January 2011:

```text
SELECT FirstName, BirthDate
FROM Student
WHERE BirthDate < '2011-01-01';
```

| FirstName | BirthDate |
|---|---|
| Chioma | 2010-11-23 |
| Elena | 2010-05-19 |
| Farid | 2010-09-08 |
| Grace | 2010-12-01 |
| Kofi | 2010-06-30 |
| Lucia | 2010-10-12 |

Join conditions with `AND` (both must be true) and `OR` (at least one must be true).

```text
SELECT FirstName, Form
FROM Student
WHERE Form = '10B' AND Points >= 30;
```

| FirstName | Form |
|---|---|
| Chioma | 10B |
| Jamal | 10B |

Dev is in 10B but has 24 points, so the second condition is false for him and he is left out.

:::warn AND is worked out before OR
When one WHERE has both, SQL works out the ANDs first, as in arithmetic where multiplication comes before addition. Use brackets whenever you mix them. The two queries below show the difference.
:::

The first is read as "Form 10A, or (Form 10B and over 40 points)":

```text
SELECT FirstName
FROM Student
WHERE Form = '10A' OR Form = '10B' AND Points > 40;
```

| FirstName |
|---|
| Amina |
| Bilal |
| Chioma |
| Ingrid |

Brackets make the order you mean explicit: "(Form 10A or Form 10B) and over 40 points":

```text
SELECT FirstName
FROM Student
WHERE (Form = '10A' OR Form = '10B') AND Points > 40;
```

| FirstName |
|---|
| Amina |
| Chioma |

Bilal (31 points) and Ingrid (29) appeared in the first result only because the OR let all of Form 10A through.

### ORDER BY: sorting the result

`ORDER BY` sorts the rows by a field. `ASC` is ascending (the default) and `DESC` is descending. Put it last.

```text
SELECT FirstName, Points
FROM Student
ORDER BY Points DESC;
```

| FirstName | Points |
|---|---|
| Elena | 67 |
| Kofi | 63 |
| Chioma | 58 |
| Lucia | 55 |
| Grace | 52 |
| Amina | 46 |
| Hiro | 41 |
| Farid | 39 |
| Jamal | 35 |
| Bilal | 31 |
| Ingrid | 29 |
| Dev | 24 |

Give two fields to sort by one and then break ties with the other. Here the students are sorted by form, and within each form by points, highest first.

```text
SELECT FirstName, Form, Points
FROM Student
ORDER BY Form, Points DESC;
```

| FirstName | Form | Points |
|---|---|---|
| Amina | 10A | 46 |
| Bilal | 10A | 31 |
| Ingrid | 10A | 29 |
| Chioma | 10B | 58 |
| Jamal | 10B | 35 |
| Dev | 10B | 24 |
| Elena | 11A | 67 |
| Kofi | 11A | 63 |
| Farid | 11A | 39 |
| Lucia | 11B | 55 |
| Grace | 11B | 52 |
| Hiro | 11B | 41 |

### Aggregate functions: SUM, COUNT and AVG

An **aggregate function** works on many rows and returns one value.

:::key The three aggregate functions
- `COUNT(*)` counts the rows. `COUNT(Field)` counts the rows where that field has a value.
- `SUM(Field)` adds up the values in a numeric field.
- `AVG(Field)` gives the mean of the values in a numeric field.

An aggregate with no GROUP BY gives **one row** for the whole table (or for the rows that WHERE keeps).
:::

```text
SELECT COUNT(*), SUM(Points), AVG(Points)
FROM Student;
```

| COUNT(*) | SUM(Points) | AVG(Points) |
|---|---|---|
| 12 | 540 | 45.0 |

There are 12 students with 540 points between them, so the mean is \(540 \div 12 = 45\). WHERE applies before the aggregate, so you can summarise just some rows:

```text
SELECT AVG(Points)
FROM Student
WHERE Form = '10B';
```

| AVG(Points) |
|---|
| 39.0 |

The 10B students have 58, 24 and 35 points: \(117 \div 3 = 39\).

:::warn COUNT(*) is not always COUNT(Field)
A field can be empty, which SQL calls NULL. `COUNT(*)` counts every row, but `COUNT(Field)` skips the rows where the field is empty. Use `COUNT(*)` to count records, and `COUNT(Field)` only when you really want to count the values that exist.
:::

In this small table of contacts, two people have no phone number.

**Contact**

| ContactID | Name | Phone |
|---|---|---|
| 1 | Asha | 0712 000 111 |
| 2 | Bruno | |
| 3 | Carla | 0733 222 444 |
| 4 | Dmitri | |

```text
SELECT COUNT(*), COUNT(Phone)
FROM Contact;
```

| COUNT(*) | COUNT(Phone) |
|---|---|
| 4 | 2 |

### GROUP BY: one result per group

A summary of the whole table is rarely enough. You usually want one summary **for each group**: for each club, or for each form. `GROUP BY` puts the rows into groups that share a value, and the aggregate is worked out once for each group.

```text
SELECT ClubCode, COUNT(*)
FROM Student
GROUP BY ClubCode;
```

| ClubCode | COUNT(*) |
|---|---|
| CH01 | 2 |
| CO01 | 4 |
| DR01 | 2 |
| FB01 | 2 |
| RB01 | 2 |

The DBMS puts the twelve students into five groups, one for each club code, and counts the rows in each. There is no row for SW01, because no student has that code, so there is nothing to put in a group. Other aggregates work the same way:

```text
SELECT ClubCode, AVG(Points)
FROM Student
GROUP BY ClubCode;
```

| ClubCode | AVG(Points) |
|---|---|
| CH01 | 60.5 |
| CO01 | 45.25 |
| DR01 | 48.0 |
| FB01 | 41.5 |
| RB01 | 29.5 |

```text
SELECT Form, SUM(Points)
FROM Student
GROUP BY Form;
```

| Form | SUM(Points) |
|---|---|
| 10A | 106 |
| 10B | 117 |
| 11A | 169 |
| 11B | 148 |

(The four sums add up to 540, the total found earlier.)

:::warn The GROUP BY rule
When a query has GROUP BY, every plain field in the SELECT list must be in the GROUP BY, and everything else must be inside an aggregate. `SELECT FirstName, COUNT(*) FROM Student GROUP BY ClubCode` is invalid, because a group of four students has four first names and the DBMS cannot pick one. Ask yourself: "which fields name the groups?" Those go in GROUP BY, and they are the plain fields to show.
:::

### INNER JOIN: using two tables together

The names of the clubs are in CLUB and the students in STUDENT. To list each student with the name of their club, you must **join** the tables: pair each student record with the club record that has the same ClubCode.

`INNER JOIN … ON` does this. `ON` states the condition for a pair to match, almost always a foreign key equal to the primary key it refers to. Only pairs that match appear in the result.

```text
SELECT Student.FirstName, Student.ClubCode, Club.ClubCode, Club.ClubName
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
WHERE Student.StudentID < 104;
```

| FirstName | ClubCode | ClubCode | ClubName |
|---|---|---|---|
| Amina | CO01 | CO01 | Coding |
| Bilal | FB01 | FB01 | Football |
| Chioma | CH01 | CH01 | Chess |

The two ClubCode columns are equal in every row, because that is what `ON` demanded. When both tables have a field with the same name, you must say which table you mean by writing `Table.Field`. It is good practice to write the table name in front of every field in a join, as here.

A normal query then follows: choose the fields you need from both tables.

```text
SELECT Student.FirstName, Club.ClubName
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
ORDER BY Student.FirstName;
```

| FirstName | ClubName |
|---|---|
| Amina | Coding |
| Bilal | Football |
| Chioma | Chess |
| Dev | Robotics |
| Elena | Drama |
| Farid | Coding |
| Grace | Football |
| Hiro | Coding |
| Ingrid | Drama |
| Jamal | Robotics |
| Kofi | Chess |
| Lucia | Coding |

WHERE can use a field of either table. Which students go to a club that meets on Tuesday, and which room do they go to?

```text
SELECT Student.FirstName, Club.Room
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
WHERE Club.MeetingDay = 'Tuesday'
ORDER BY Student.FirstName;
```

| FirstName | Room |
|---|---|
| Amina | L3 |
| Farid | L3 |
| Hiro | L3 |
| Lucia | L3 |

A join can also be grouped. This counts the students in each club, using the club's name, not its code:

```text
SELECT Club.ClubName, COUNT(*)
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
GROUP BY Club.ClubName;
```

| ClubName | COUNT(*) |
|---|---|
| Chess | 2 |
| Coding | 4 |
| Drama | 2 |
| Football | 2 |
| Robotics | 2 |

Swimming is missing again, and this time it is because of the join: an INNER JOIN keeps only the pairs that match, and no student matches SW01.

:::warn Do not forget the ON condition
Without the matching condition the DBMS has no rule for pairing records. Some systems report an error. Others pair every student with every club: \(12 \times 6 = 72\) rows, mostly nonsense. Every INNER JOIN needs an ON that compares a foreign key with its primary key.
:::

Fees are in CLUB and the students who pay them are in STUDENT, so a join lets you total them. If every student pays the fee of their club, the school collects:

```text
SELECT SUM(Club.Fee)
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode;
```

| SUM(Club.Fee) |
|---|
| 126.00 |

The check: Chess \(2 \times 5 = 10\), Coding \(4 \times 12.50 = 50\), Drama \(2 \times 8 = 16\), Football \(2 \times 10 = 20\), Robotics \(2 \times 15 = 30\), and \(10 + 50 + 16 + 20 + 30 = 126\).

:::key The order of clauses
Clauses must be written in this order. Leave out the ones you do not need, but never swap them.

```text
SELECT   fields or aggregate functions
FROM     table
INNER JOIN second table ON matching condition
WHERE    condition on single rows
GROUP BY fields that name the groups
ORDER BY fields to sort by
```
The DBMS finds the rows (FROM and JOIN), keeps those that pass WHERE, makes the groups, works out the aggregates, then sorts.
:::

### Writing a query from a description

Exam questions describe a result in words. A steady routine finds the clauses.

:::steps
1. **SELECT**: which fields does the answer show? If it is a total, count or mean, which aggregate?
2. **FROM**: which table holds those fields? If they come from two tables, add `INNER JOIN … ON` with the key match.
3. **WHERE**: which rows count? Each condition on a single row goes here, with quotes on text and dates.
4. **GROUP BY**: is the answer "for each …"? Then the "each" field names the groups.
5. **ORDER BY**: does it say sorted, highest first, in alphabetical order?
:::

:::exam Writing SQL in Paper 1
Copy table and field names exactly as the question gives them. Mark schemes award a mark for each clause, so write every clause the question needs: the `ON` condition of a join and the quotes round text and dates are the marks students most often lose. When a question says "state the output", draw a table with the column headings and the rows in the order the query produces them.
:::

:::eg Write a query with a join (exam style)
The Student and Club tables are as printed earlier. Write an SQL query that displays the first name of every student born before 1 January 2011, together with the name of their club, in order of club name and then first name. [5 marks]

Both fields come from different tables, so the query needs a join. "Born before 1 January 2011" is a WHERE condition on a date. Two sort fields are separated by a comma.

```text
SELECT Student.FirstName, Club.ClubName
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
WHERE Student.BirthDate < '2011-01-01'
ORDER BY Club.ClubName, Student.FirstName;
```

- `SELECT` with FirstName and ClubName [B1]
- `FROM Student INNER JOIN Club` [B1]
- `ON Student.ClubCode = Club.ClubCode` [B1]
- `WHERE` BirthDate before 2011-01-01, with the date in quotes [B1]
- `ORDER BY` ClubName then FirstName [B1]

The query returns these rows:

| FirstName | ClubName |
|---|---|
| Chioma | Chess |
| Kofi | Chess |
| Farid | Coding |
| Lucia | Coding |
| Elena | Drama |
| Grace | Football |

(Accept the join written with the tables the other way round, `FROM Club INNER JOIN Student ON …`.)
:::

:::eg State the output of a query (exam style)
State the output of the following query. [3 marks]

```text
SELECT Club.ClubName, SUM(Student.Points)
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
GROUP BY Club.ClubName;
```

Read it from the inside out: the join pairs students with their clubs, GROUP BY makes one group for each club name, and SUM adds the points of the students in each group. There are five groups, because Swimming has no students. For Chess, Chioma (58) and Kofi (63) give 121.

| ClubName | SUM(Student.Points) |
|---|---|
| Chess | 121 |
| Coding | 181 |
| Drama | 96 |
| Football | 83 |
| Robotics | 59 |

- two columns with the club name and the sum [B1]
- one row for each of the five clubs with students, and no row for Swimming [B1]
- all five sums correct: 121, 181, 96, 83, 59 [B1]

(Coding is the largest: \(46 + 39 + 41 + 55 = 181\).)
:::

### Build and test queries yourself

The tool below holds the same two tables. Choose the fields, the table or the join, a condition, a grouping and an order, and it writes the SQL and shows the result. Try these: select ClubName and FirstName with the join; then switch to COUNT(*) with GROUP BY ClubName; then add a WHERE on Points and watch the groups change. If a combination is not valid SQL, it explains why.

:::html
<div class="widget" data-w="cs-sql" data-db="school"></div>
:::

## Changing data: INSERT, UPDATE and DELETE

These three statements maintain the data. They are DML too, but unlike SELECT they **change** the table. Each subsection below starts from the tables exactly as printed.

### INSERT INTO: adding a record

`INSERT INTO` names the table, then `VALUES` gives one value for each field, in the order the table has its fields. You can name the fields first (safer, because the order is then explicit), or leave the list out when you give a value for every field.

```text
INSERT INTO Student (StudentID, FirstName, Form, BirthDate, Points, ClubCode)
VALUES (113, 'Mina', '10A', '2011-05-05', 0, 'SW01');
```

```text
INSERT INTO Student
VALUES (114, 'Noor', '11B', '2010-09-14', 0, 'SW01');
```

Both add a student to the Swimming club. A SELECT confirms the table now holds them:

```text
SELECT StudentID, FirstName, ClubCode
FROM Student
WHERE StudentID > 112;
```

| StudentID | FirstName | ClubCode |
|---|---|---|
| 113 | Mina | SW01 |
| 114 | Noor | SW01 |

### UPDATE: changing records

`UPDATE` names the table, `SET` gives the new value of one or more fields, and `WHERE` says **which records** to change.

```text
UPDATE Student
SET Points = Points + 10
WHERE ClubCode = 'RB01';
```

The expression `Points + 10` is worked out for each record that WHERE selects, so each Robotics student gets 10 more points.

```text
SELECT FirstName, Points
FROM Student
WHERE ClubCode = 'RB01';
```

| FirstName | Points |
|---|---|
| Dev | 34 |
| Jamal | 45 |

(They had 24 and 35 before.) To change several fields in one record, separate the assignments with commas:

```text
UPDATE Club
SET MeetingDay = 'Sunday', Room = 'Pool 2'
WHERE ClubCode = 'SW01';
```

```text
SELECT *
FROM Club
WHERE ClubCode = 'SW01';
```

| ClubCode | ClubName | MeetingDay | Room | Fee |
|---|---|---|---|---|
| SW01 | Swimming | Sunday | Pool 2 | 20.00 |

### DELETE FROM: removing records

`DELETE FROM` removes the records that WHERE selects.

```text
DELETE FROM Student
WHERE StudentID = 112;
```

```text
SELECT COUNT(*)
FROM Student;
```

| COUNT(*) |
|---|
| 11 |

:::warn UPDATE and DELETE need a WHERE
A statement with no WHERE applies to **every** record in the table. `DELETE FROM Student;` removes all the students and leaves an empty table, and `UPDATE Student SET Points = 0;` wipes every score. Always write the WHERE first, and in real work test it with a SELECT that has the same WHERE before you change anything.
:::

```text
DELETE FROM Student;
```

```text
SELECT COUNT(*)
FROM Student;
```

| COUNT(*) |
|---|
| 0 |

### Changes the database refuses

The foreign key declared in CREATE TABLE is checked on every change. A statement that would break referential integrity is rejected, and nothing in the table changes.

```text
-- rejected: there is no club XX99
INSERT INTO Student
VALUES (115, 'Omar', '10B', '2011-02-02', 0, 'XX99');
```

```text
-- rejected: students still refer to this club
DELETE FROM Club
WHERE ClubCode = 'DR01';
```

To remove the Drama club you must deal with its students first, then remove the club. Do it in this order:

```text
DELETE FROM Student
WHERE ClubCode = 'DR01';
```

```text
DELETE FROM Club
WHERE ClubCode = 'DR01';
```

:::eg Write maintenance statements (exam style)
Using the Student and Club tables, write SQL statements to: (a) add a new student with StudentID 115, first name 'Omar', form '10B', born on 2011-02-02, with 0 points, who has joined the club with code RB01 [3]; (b) add 5 points to every student in form 11A [3]; (c) remove the student with StudentID 115 [2]. [8 marks]

Each statement names a table, so decide which statement type each part needs: INSERT INTO, UPDATE, DELETE FROM.

(a)

```text
INSERT INTO Student
VALUES (115, 'Omar', '10B', '2011-02-02', 0, 'RB01');
```

- `INSERT INTO Student` [B1]
- `VALUES` with all six values in the order of the fields [B1]
- text and the date in quotes, numbers without [B1]

(b)

```text
UPDATE Student
SET Points = Points + 5
WHERE Form = '11A';
```

- `UPDATE Student` [B1]
- `SET Points = Points + 5` [B1]
- `WHERE Form = '11A'` with the form in quotes, so that only form 11A changes [B1]

(c)

```text
DELETE FROM Student
WHERE StudentID = 115;
```

- `DELETE FROM Student` [B1]
- `WHERE StudentID = 115` [B1]
:::

:::eg Spot the error: the missing join condition
Question: Write an SQL query to display the first name and points of each student in the Chess club who has more than 50 points, with the highest points first. [4 marks]

A student wrote:

```text
01  SELECT FirstName, Points
02  FROM Student INNER JOIN Club
03  WHERE ClubName = 'Chess' AND Points > 50
04  ORDER BY Points DESC;
```

Line 01 selects the right fields [B1]. **Line 02 joins the two tables but has no `ON` condition, so the DBMS has no rule for which student matches which club. That mark is lost** [B0]. Line 03 gives both conditions [B1]. Line 04 sorts highest first [B1]. The answer scores 3 out of 4.

Without a join condition every student would be paired with every club (72 pairs) before WHERE chooses among them, and the result would be wrong or an error. The corrected statement gives the right rows:

```text
SELECT Student.FirstName, Student.Points
FROM Student
INNER JOIN Club ON Student.ClubCode = Club.ClubCode
WHERE Club.ClubName = 'Chess' AND Student.Points > 50
ORDER BY Student.Points DESC;
```

| FirstName | Points |
|---|---|
| Kofi | 63 |
| Chioma | 58 |
:::

## Practice data: a shop

The practice questions use a different database: a small chain of shops in Accra and Kumasi. Product holds what the shops sell and Sale records each sale of a product. ProductID in Sale is a foreign key to ProductID in Product. Here are the tables.

**Product**

| ProductID | ProductName | Category | Price | Stock |
|---|---|---|---|---|
| 1 | Notebook | Stationery | 2.50 | 120 |
| 2 | Pen | Stationery | 0.80 | 300 |
| 3 | Backpack | Bags | 24.00 | 35 |
| 4 | Calculator | Electronics | 18.50 | 40 |
| 5 | Headphones | Electronics | 32.00 | 22 |
| 6 | Water bottle | Outdoor | 7.50 | 60 |
| 7 | Torch | Outdoor | 11.00 | 25 |
| 8 | Ruler | Stationery | 1.20 | 150 |
| 9 | Lunch box | Kitchen | 9.00 | 45 |

**Sale**

| SaleID | ProductID | Quantity | SaleDate | Branch |
|---|---|---|---|---|
| 1 | 3 | 2 | 2026-10-01 | Accra |
| 2 | 1 | 10 | 2026-10-01 | Kumasi |
| 3 | 5 | 1 | 2026-10-02 | Accra |
| 4 | 2 | 25 | 2026-10-02 | Accra |
| 5 | 4 | 3 | 2026-10-03 | Kumasi |
| 6 | 6 | 4 | 2026-10-03 | Accra |
| 7 | 1 | 6 | 2026-10-04 | Accra |
| 8 | 9 | 2 | 2026-10-04 | Kumasi |
| 9 | 3 | 1 | 2026-10-05 | Kumasi |
| 10 | 7 | 3 | 2026-10-05 | Accra |
| 11 | 8 | 12 | 2026-10-06 | Kumasi |
| 12 | 5 | 2 | 2026-10-06 | Kumasi |
| 13 | 2 | 15 | 2026-10-07 | Kumasi |
| 14 | 4 | 1 | 2026-10-07 | Accra |
| 15 | 6 | 3 | 2026-10-08 | Kumasi |

The same widget can check your answers against these tables:

:::html
<div class="widget" data-w="cs-sql" data-db="shop"></div>
:::

:::try Start easy, finish at exam standard
Q: State the output of this query.

```text
SELECT ProductName, Price
FROM Product
WHERE Category = 'Electronics';
```

A: Two products are in the Electronics category.

| ProductName | Price |
|---|---|
| Calculator | 18.50 |
| Headphones | 32.00 |

Q: Write a query to display the name and stock of every product with fewer than 50 items in stock, with the lowest stock first.
A: The field to sort by is Stock, ascending (the default).

```text
SELECT ProductName, Stock
FROM Product
WHERE Stock < 50
ORDER BY Stock;
```

| ProductName | Stock |
|---|---|
| Headphones | 22 |
| Torch | 25 |
| Backpack | 35 |
| Calculator | 40 |
| Lunch box | 45 |

Q: Write a query to count the sales made in the Accra branch, and give its output.
A: Count the rows after WHERE has chosen the Accra ones.

```text
SELECT COUNT(*)
FROM Sale
WHERE Branch = 'Accra';
```

| COUNT(*) |
|---|
| 7 |

Q: What does this query output?

```text
SELECT SUM(Quantity)
FROM Sale
WHERE ProductID = 1;
```

A: It adds the quantities of the sales of product 1 (Notebook): sale 2 sold 10 and sale 7 sold 6.

| SUM(Quantity) |
|---|
| 16 |

Q: State the output of this query.

```text
SELECT Branch, SUM(Quantity)
FROM Sale
GROUP BY Branch;
```

A: One row for each branch, with the total quantity sold there.

| Branch | SUM(Quantity) |
|---|---|
| Accra | 42 |
| Kumasi | 48 |

Q: Write the output of `SELECT AVG(Price) FROM Product WHERE Category = 'Stationery';`
A: The three Stationery prices are 2.50, 0.80 and 1.20, so the mean is \(4.50 \div 3 = 1.5\).

```text
SELECT AVG(Price)
FROM Product
WHERE Category = 'Stationery';
```

| AVG(Price) |
|---|
| 1.5 |

Q: The price of a Pen rises to 0.90. Write the SQL statement that makes the change.
A: UPDATE with a WHERE that selects only the Pen.

```text
UPDATE Product
SET Price = 0.90
WHERE ProductName = 'Pen';
```

Q: Sale 15 was entered by mistake. Write a statement to delete it.
A: DELETE FROM with the primary key in the WHERE.

```text
DELETE FROM Sale
WHERE SaleID = 15;
```

Q: Explain why `SELECT ProductID, COUNT(*) FROM Sale GROUP BY Branch;` is not valid.
A: The groups are made by Branch, but ProductID is a plain field that is not in the GROUP BY. A branch has many different ProductID values and the DBMS cannot choose one. Either group by ProductID, or leave ProductID out of the SELECT.
Q: A new product is added to Product: ProductID 10, 'Eraser', category 'Stationery', price 0.60, stock 200. Write the statement.
A: One value for each field, in the order of the table.

```text
INSERT INTO Product
VALUES (10, 'Eraser', 'Stationery', 0.60, 200);
```
:::

:::try Exam practice ★ to ★★★
Q: [7 marks] ★★ The shops' database is created from the Product and Sale tables printed above. (a) Write an SQL statement to create the table Product. ProductName and Category hold up to 20 and 12 characters, Price is a number with decimals, Stock is a whole number and ProductID is a whole number and the primary key. [3] (b) Write an SQL statement to create the table Sale. SaleDate holds a date, Branch holds up to 10 characters, and ProductID is a foreign key that refers to ProductID in Product. [4]
H: Create Product first, because Sale refers to it.
H: In (b), the foreign key line is `FOREIGN KEY (field) REFERENCES Table (Field)`.
A: (a)

```text
CREATE TABLE Product (
   ProductID INTEGER,
   ProductName VARCHAR(20),
   Category VARCHAR(12),
   Price REAL,
   Stock INTEGER,
   PRIMARY KEY (ProductID)
);
```

- `CREATE TABLE Product` with all five fields in brackets [B1]
- correct data types: INTEGER, VARCHAR(20), VARCHAR(12), REAL, INTEGER [B1]
- `PRIMARY KEY (ProductID)` [B1]

(b)

```text
CREATE TABLE Sale (
   SaleID INTEGER,
   ProductID INTEGER,
   Quantity INTEGER,
   SaleDate DATE,
   Branch VARCHAR(10),
   PRIMARY KEY (SaleID),
   FOREIGN KEY (ProductID) REFERENCES Product (ProductID)
);
```

- `CREATE TABLE Sale` with all five fields [B1]
- SaleDate as DATE and Branch as VARCHAR(10), the others INTEGER [B1]
- a primary key given for the table, `PRIMARY KEY (SaleID)` [B1]
- `FOREIGN KEY (ProductID) REFERENCES Product (ProductID)` [B1]

Q: [2 marks] ★ The shop wants to record the name of each product's supplier, up to 25 characters. Write a statement to change the Product table to hold it.
A: ALTER TABLE is the statement for changing the structure.

```text
ALTER TABLE Product ADD Supplier VARCHAR(25);
```

- `ALTER TABLE Product` [B1]
- `ADD Supplier VARCHAR(25)` [B1]

Q: [4 marks] ★ Write a query to display the name and price of all products that cost more than 10, with the dearest first.
A: One possible answer:

```text
SELECT ProductName, Price
FROM Product
WHERE Price > 10
ORDER BY Price DESC;
```

| ProductName | Price |
|---|---|
| Headphones | 32.00 |
| Backpack | 24.00 |
| Calculator | 18.50 |
| Torch | 11.00 |

- `SELECT ProductName, Price` [B1]
- `FROM Product` [B1]
- `WHERE Price > 10` (no quotes round the number) [B1]
- `ORDER BY Price DESC` [B1]

Q: [5 marks] ★★ Write a query to display the SaleID, the product name and the quantity of every sale made in the Kumasi branch, in alphabetical order of product name.
H: The product name is in Product and the branch is in Sale, so you need an INNER JOIN.
H: The ON condition compares the two ProductID fields.
A: One possible answer:

```text
SELECT Sale.SaleID, Product.ProductName, Sale.Quantity
FROM Sale
INNER JOIN Product ON Sale.ProductID = Product.ProductID
WHERE Sale.Branch = 'Kumasi'
ORDER BY Product.ProductName;
```

| SaleID | ProductName | Quantity |
|---|---|---|
| 9 | Backpack | 1 |
| 5 | Calculator | 3 |
| 12 | Headphones | 2 |
| 8 | Lunch box | 2 |
| 2 | Notebook | 10 |
| 13 | Pen | 15 |
| 11 | Ruler | 12 |
| 15 | Water bottle | 3 |

- `SELECT` with the three fields from the correct tables [B1]
- `FROM Sale INNER JOIN Product` [B1]
- `ON Sale.ProductID = Product.ProductID` [B1]
- `WHERE Sale.Branch = 'Kumasi'` with the text in quotes [B1]
- `ORDER BY Product.ProductName` [B1]

Q: [5 marks] ★★ State the output of this query, row by row.

```text
SELECT Product.Category, SUM(Sale.Quantity)
FROM Sale
INNER JOIN Product ON Sale.ProductID = Product.ProductID
GROUP BY Product.Category;
```

H: Work out the category of each sale first, then add the quantities in each category.
H: The groups are listed in alphabetical order of category. Electronics: sales 3, 5, 12 and 14.
A: Group the sales by the category of their product and add up the quantities.

| Category | SUM(Sale.Quantity) |
|---|---|
| Bags | 3 |
| Electronics | 7 |
| Kitchen | 2 |
| Outdoor | 10 |
| Stationery | 68 |

- Bags 3 [B1] (sales 1 and 9: 2 + 1)
- Electronics 7 [B1] (sales 3, 5, 12, 14: 1 + 3 + 2 + 1)
- Kitchen 2 [B1] and Outdoor 10 [B1] (4 + 3 + 3)
- Stationery 68 [B1] (10 + 25 + 6 + 12 + 15)

(The five sums add up to 90, the total quantity of all fifteen sales.)

Q: [6 marks] ★★★ Write SQL queries to display: (a) the mean price of the products in each category [3]; (b) the number of sales made in each branch [3].
H: "In each" means GROUP BY. The grouping field is also the plain field you display.
A: (a)

```text
SELECT Category, AVG(Price)
FROM Product
GROUP BY Category;
```

| Category | AVG(Price) |
|---|---|
| Bags | 24.00 |
| Electronics | 25.25 |
| Kitchen | 9.00 |
| Outdoor | 9.25 |
| Stationery | 1.50 |

- `SELECT Category, AVG(Price)` [B1]
- `FROM Product` [B1]
- `GROUP BY Category` [B1]

(b)

```text
SELECT Branch, COUNT(*)
FROM Sale
GROUP BY Branch;
```

| Branch | COUNT(*) |
|---|---|
| Accra | 7 |
| Kumasi | 8 |

- `SELECT Branch, COUNT(*)` [B1]
- `FROM Sale` [B1]
- `GROUP BY Branch` [B1]

Q: [7 marks] ★★★ (a) Write a statement to add a sale with SaleID 16, product 7, quantity 2, date 2026-10-09, branch 'Accra'. [2] (b) After sale 5 the shop has 3 fewer calculators. Write a statement to reduce the Stock of ProductID 4 by 3. [3] (c) Write a statement to delete all sales made before 2026-10-03. [2]
H: For (b), the new value depends on the old value in the same field.
A: (a)

```text
INSERT INTO Sale
VALUES (16, 7, 2, '2026-10-09', 'Accra');
```

- `INSERT INTO Sale` [B1]
- `VALUES` with the five values in the order of the fields, text and date in quotes [B1]

(b)

```text
UPDATE Product
SET Stock = Stock - 3
WHERE ProductID = 4;
```

- `UPDATE Product` [B1]
- `SET Stock = Stock - 3` [B1]
- `WHERE ProductID = 4` so only that product changes [B1]

(c)

```text
DELETE FROM Sale
WHERE SaleDate < '2026-10-03';
```

- `DELETE FROM Sale` [B1]
- `WHERE SaleDate < '2026-10-03'` with the date in quotes [B1]

Q: [4 marks] ★★★ Describe what this query does and state its output.

```text
SELECT Branch, SUM(Quantity)
FROM Sale
WHERE SaleDate >= '2026-10-05'
GROUP BY Branch
ORDER BY SUM(Quantity) DESC;
```

H: WHERE keeps only some sales before the groups are made.
A: It totals the quantity sold in each branch for sales made on or after 5 October 2026 [B1], and lists the branch with the larger total first [B1].

| Branch | SUM(Quantity) |
|---|---|
| Kumasi | 33 |
| Accra | 4 |

- Kumasi 33 [B1] (sales 9, 11, 12, 13 and 15: 1 + 12 + 2 + 15 + 3)
- Accra 4 [B1] (sales 10 and 14: 3 + 1)
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The shops stop selling the Ruler (ProductID 8). Sale 11 is the only sale of a Ruler. (a) Write the two statements that remove the Ruler and its sale from the database, in an order that the DBMS will accept, and explain why the order matters. [4] (b) A manager tries to run `INSERT INTO Sale VALUES (17, 12, 1, '2026-10-09', 'Accra');`. There is no product 12. Explain what happens and why. [2]
H: Which table is the parent, and which one holds the foreign key?
H: Think about what DELETE FROM Product would leave behind if Sale 11 still existed.
A: (a)

```text
DELETE FROM Sale
WHERE ProductID = 8;
```

```text
DELETE FROM Product
WHERE ProductID = 8;
```

- the Sale record is deleted first, with `WHERE ProductID = 8` [B1]
- the Product record is deleted second, with `WHERE ProductID = 8` [B1]
- the order matters because Sale has a foreign key to Product [B1], and deleting the product first would leave a sale that refers to a product that does not exist, so referential integrity would reject (refuse) the statement [B1]

(b) The DBMS rejects (refuses) the INSERT [B1] because ProductID 12 in the new record does not match any ProductID in Product, so it would break referential integrity [B1].

Q: [5 marks] ★★★ A student wrote this query to list each product category sold in the Kumasi branch with the total quantity sold, the largest total first. It does not work.

```text
SELECT Category, SUM(Quantity)
FROM Sale INNER JOIN Product
WHERE Branch = 'Kumasi'
GROUP BY ProductName
ORDER BY Quantity DESC;
```

Identify three errors, and write the corrected query.
H: Check the join, then which fields name the groups, then what a grouped query is allowed to sort by.
A: Error 1: the INNER JOIN has no `ON` condition, so the tables are not matched [B1]. Error 2: the query shows Category but groups by ProductName; the plain field in SELECT must be the field in GROUP BY, and the question wants one row for each category [B1]. Error 3: ORDER BY Quantity sorts by a plain field that is not in the groups; a grouped query sorts by the aggregate, `SUM(Sale.Quantity)` [B1].

Corrected query:

```text
SELECT Product.Category, SUM(Sale.Quantity)
FROM Sale
INNER JOIN Product ON Sale.ProductID = Product.ProductID
WHERE Sale.Branch = 'Kumasi'
GROUP BY Product.Category
ORDER BY SUM(Sale.Quantity) DESC;
```

- `INNER JOIN Product ON Sale.ProductID = Product.ProductID` [B1]
- `GROUP BY Product.Category` and `ORDER BY SUM(Sale.Quantity) DESC` [B1]

| Category | SUM(Sale.Quantity) |
|---|---|
| Stationery | 37 |
| Electronics | 5 |
| Outdoor | 3 |
| Kitchen | 2 |
| Bags | 1 |

Stationery leads with \(10 + 12 + 15 = 37\) items in Kumasi.
:::

:::quiz
? Which statement is part of the data definition language (DDL)?
- SELECT
- UPDATE
+ ALTER TABLE
- DELETE FROM
> DDL creates and changes the structure of the database. SELECT, UPDATE and DELETE FROM work on the data in the tables, so they are DML.
? What does `SELECT COUNT(*) FROM Student WHERE Form = '10A';` return for the data in this chapter?
- 12
- 0
+ 3
- 10
> WHERE keeps the three students in form 10A (Amina, Bilal and Ingrid) before COUNT works. 12 is the count for the whole table.
? In a query, which order of clauses is correct?
- SELECT, FROM, ORDER BY, WHERE, GROUP BY
- SELECT, FROM, GROUP BY, WHERE, ORDER BY
+ SELECT, FROM, WHERE, GROUP BY, ORDER BY
- FROM, SELECT, WHERE, ORDER BY, GROUP BY
> The clauses always come in the order SELECT, FROM (with any join), WHERE, GROUP BY, ORDER BY.
? Which condition is correct for a text field Form that holds values such as 10A?
- `WHERE Form = 10A`
- `WHERE Form == '10A'`
+ `WHERE Form = '10A'`
- `WHERE 'Form' = 10A`
> Text goes in single quotes and equality is a single `=`. Without the quotes SQL looks for a field called 10A.
? What is wrong with `SELECT Form, Points, COUNT(*) FROM Student GROUP BY Form;`?
- COUNT(*) cannot be used with GROUP BY.
- GROUP BY must come before FROM.
+ Points is a plain field that is not in the GROUP BY.
- Form cannot be selected with a group.
> Every plain field in the SELECT list must be one of the GROUP BY fields. A form has many different Points values, so the DBMS cannot show one.
? `UPDATE Club SET Fee = 0;` is run with no WHERE. What happens?
- Nothing: the statement is rejected because it has no WHERE.
- Only the first record changes.
+ Every record in Club has its Fee set to 0.
- Only the records that have a fee greater than 0 change.
> Without a WHERE, UPDATE and DELETE FROM apply to every record, which is why they need care.
? An INNER JOIN of Student and Club ON the ClubCode fields is run on the chapter's data. Why does Swimming not appear in the result?
- Swimming has no fee.
+ No student has the club code SW01, so no pair matches it.
- INNER JOIN removes the last row of the table.
- The ON condition compares text, not numbers.
> INNER JOIN returns only pairs that match the ON condition. A club with no students never matches, so it is left out.
:::

:::checklist What you can now do
- [ ] I can explain that the DBMS uses DDL for the structure and DML for queries and data maintenance, and that SQL is the standard for both.
- [ ] I can write CREATE DATABASE and CREATE TABLE statements with the data types CHARACTER, VARCHAR(n), BOOLEAN, INTEGER, REAL, DATE and TIME.
- [ ] I can add a primary key with PRIMARY KEY (field) and a foreign key with FOREIGN KEY (field) REFERENCES Table (Field).
- [ ] I can change a table with ALTER TABLE.
- [ ] I can write SELECT … FROM queries with WHERE, ORDER BY and GROUP BY.
- [ ] I can use SUM, COUNT and AVG, with and without GROUP BY.
- [ ] I can join two tables with INNER JOIN … ON and use Table.Field names.
- [ ] I can write INSERT INTO, UPDATE and DELETE FROM statements, and I know why they need a WHERE.
- [ ] I can read a given SQL statement and state its output.
:::

:::recap
- SQL is the industry-standard language. DDL (CREATE DATABASE, CREATE TABLE, ALTER TABLE) defines the structure. DML (SELECT, INSERT INTO, UPDATE, DELETE FROM) queries and maintains the data.
- CREATE TABLE lists fields with data types (CHARACTER, VARCHAR(n), BOOLEAN, INTEGER, REAL, DATE, TIME), then `PRIMARY KEY (field)` and `FOREIGN KEY (field) REFERENCES Table (Field)`. Create the referred-to table first.
- Clause order: SELECT, FROM, WHERE, GROUP BY, ORDER BY. Text and dates go in quotes, numbers do not. AND is worked out before OR: use brackets.
- SUM, COUNT and AVG return one value per query, or one per group with GROUP BY. Plain fields in the SELECT list must be in the GROUP BY. `COUNT(*)` counts rows; `COUNT(Field)` counts values that exist.
- INNER JOIN … ON matches a foreign key to its primary key and keeps only the matching pairs. Without the ON, rows are paired with every row. Write `Table.Field` when names repeat.
- INSERT INTO … VALUES adds a record, UPDATE … SET … WHERE changes records, DELETE FROM … WHERE removes them. Without WHERE they act on every record. The DBMS rejects changes that break referential integrity.
:::

:::links
- practise: [SQLBolt](https://sqlbolt.com/) · SQLBolt · interactive SQL lessons with exercises, from SELECT to joins and aggregates
- read: [W3Schools SQL tutorial](https://www.w3schools.com/sql/) · W3Schools · short SQL lessons with try-it boxes
- read: [SQL INNER JOIN](https://www.w3schools.com/sql/sql_join_inner.asp) · W3Schools · the INNER JOIN statement with examples
- read: [SQL GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp) · W3Schools · grouping rows and using aggregate functions
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free topic explanations and questions on databases and SQL (written for UK boards)
- papers: [PapaCambridge 9618 past papers](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · Paper 1 database questions with mark schemes [unofficial]

Links checked 13 November 2026.
:::

Next: [Computational thinking and algorithms](#cs.algorithms)
