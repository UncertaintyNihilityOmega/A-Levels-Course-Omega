@chapter cs.databases
@title Databases: the relational model and normalisation
@level as
@paper CAIE 9618 Paper 1
@time 6–8 hours
@summary Why a pile of spreadsheet-style files breaks down, and how a relational database fixes it. You will learn the terms (table, record, field, keys, relationships, referential integrity, index), draw entity-relationship diagrams, normalise data to third normal form, and explain what a database management system does.

:::why
Almost every system you use stores its data in a database: your school's register, a shop's stock, a bank's accounts, a booking site. Paper 1 asks you to explain why the database is designed as it is, to draw and read its diagrams, and to take a messy table and turn it into a clean design. The skill is a way of thinking: store each fact once, in the right place, and link the places together. The next chapter, [DBMS and SQL](#cs.sql), then shows how to build and question such a database in the language every database system understands.
:::

**Before you start**, you should know what a record and a field are from [Data types, records and arrays](#cs.datatypes), and how data sizes are measured from [Number systems and binary arithmetic](#cs.data).

:::try Warm-up
Q: Which data type suits a telephone number such as 0712 345 678, and why? (from [Data types, records and arrays](#cs.datatypes))
A: STRING. It is never used in arithmetic, it has a leading zero that an INTEGER would lose, and it contains spaces.
Q: What is a record, and what is a field? (from [Data types, records and arrays](#cs.datatypes))
A: A record groups several data items, which may have different data types, under one identifier. Each item in it is a field.
Q: A file holds 2 000 records of 256 bytes each. How many KiB is that? (from [Number systems and binary arithmetic](#cs.data))
A: \(2000 \times 256 = 512\,000\) bytes, and \(512\,000 \div 1024 = 500\), so the file is 500 KiB.
:::

## Storing data in a file

The clubs coordinator at Harbour View School in Lagos keeps one big spreadsheet of who goes to which after-school club. Every row says that one student attends one club, and gives all the details of both.

| StudentID | StudentName | Form | FormTutor | ClubName | ClubDay | ClubLeader |
|---|---|---|---|---|---|---|
| 101 | Amina Bello | 10A | Mr Adeyemi | Chess | Monday | Mrs Eze |
| 101 | Amina Bello | 10A | Mr Adeyemi | Robotics | Friday | Mr Lawal |
| 102 | Bilal Yusuf | 10A | Mr Adeyemi | Chess | Monday | Mrs Eze |
| 103 | Chioma Obi | 10B | Ms Danjuma | Drama | Wednesday | Ms Okon |
| 103 | Chioma Obi | 10B | Ms Danjuma | Chess | Monday | Mrs Eze |
| 103 | Chioma Obi | 10B | Ms Danjuma | Robotics | Friday | Mr Lawal |
| 104 | Dev Nair | 10B | Ms Danjuma | Robotics | Friday | Mr Lawal |
| 105 | Elena Cruz | 11A | Mrs Hassan | Drama | Wednesday | Ms Okon |
| 106 | Farid Aziz | 11A | Mrs Hassan | Chess | Monday | Mrs Eze |
| 107 | Grace Mensah | 11B | Mr Okafor | Swimming | Saturday | Mr Bello |

This is a **flat file**: one table, stored as a file, that a program reads from the top. It works for ten rows. It starts to hurt as the school grows, and the way it hurts is the reason databases exist.

:::def File-based approach
A way of storing data in which each application keeps its own file (or files), and the structure of each file is built into the programs that use it.
:::

### The limitations of a file-based approach

Look at the table again. The fact "Chess meets on Mondays and is led by Mrs Eze" is stored four times, once for every member. "Mr Adeyemi is the tutor of 10A" is stored three times. Each limitation below starts from a problem you can see in this file.

:::key Limitations of a file-based approach
- **Data redundancy**: the same data is stored many times, which wastes storage and effort.
- **Data inconsistency**: because there are several copies, they can disagree. Change Chess to Tuesday in three rows and miss the fourth, and the file now says the club meets on two days.
- **Data dependence**: the layout of the file (which column comes where, how wide each field is) is written into every program that reads it. Add a column and every program must be changed.
- **Poor security**: the operating system can only allow or refuse access to a whole file. A form tutor who may see who is in a club can also see everything else in the file.
- **Poor data integrity and sharing**: nothing stops a typing error such as "Mnday", and two people who open the file together can overwrite each other's changes.
- **Hard to answer new questions**: "which clubs does Chioma attend?" needs a new program to be written, because the file can only be read in the order it was saved.
:::

### Three anomalies

The redundancy causes three specific faults, called **anomalies**. Examiners like them because they are easy to explain from a table.

:::cols
:::col Update anomaly
Mrs Eze hands over Chess to Mr Rahman. Four rows must be edited. If one is missed, the file contradicts itself.
:::
:::col Insertion anomaly
A new club, Debating, has no members yet. A row needs a student, so the club cannot be recorded until someone joins.
:::
:::col Deletion anomaly
Grace leaves the school and her row is deleted. That row was the only place that recorded the Swimming club, its day, and Mr Okafor as the tutor of 11B.
:::
:::

:::eg Describe two limitations (exam style)
The clubs file above is stored as one flat file. Describe two limitations of storing the data in this way. [4 marks]

Each limitation earns one mark for naming it and one for a description that fits the data.

- Data redundancy: the same data is stored more than once [B1], for example the club day and leader of Chess is repeated in every row for a Chess member [B1].
- Data inconsistency: the copies of one fact can disagree [B1], for example if the leader of Chess is changed in some rows but not in others [B1].

Other limitations that would score are data dependence (programs must know the file layout), no access rights for different users, and no checking of the data entered. A named limitation with no link to the data scores only the first mark.
:::

## The relational model

A **relational database** solves these problems by splitting the data into several tables, one for each kind of thing the database is about, and linking the tables with keys. Nothing is repeated: the leader of Chess is stored once, in a table about clubs. The word "relational" comes from the relations (tables) and from the relationships between them.

:::def Database
An organised collection of data, stored so that it can be accessed, updated and managed by many users and programs.
:::

:::def Relational database
A database in which the data is stored in tables, and relationships between the tables are made by matching the values of fields (keys), so that each fact is stored once.
:::

:::def Entity
Something about which data is stored, such as a student, a form or a club. In a relational database each entity becomes one table.
:::

:::def Table
A set of records about one entity, arranged in rows and columns. Each row is a record and each column is a field.
:::

:::def Record (tuple)
One row of a table: all the data held about one occurrence of an entity, such as one student. In the theory of relational databases a record is called a tuple.
:::

:::def Field (attribute)
One column of a table: one item of data about the entity, such as StudentName. In the theory of relational databases a field is called an attribute.
:::

The clubs file becomes four tables. Read each one and notice what it contains and what it leaves out.

**STUDENT**

| StudentID | StudentName | FormID |
|---|---|---|
| 101 | Amina Bello | 10A |
| 102 | Bilal Yusuf | 10A |
| 103 | Chioma Obi | 10B |
| 104 | Dev Nair | 10B |
| 105 | Elena Cruz | 11A |
| 106 | Farid Aziz | 11A |
| 107 | Grace Mensah | 11B |

**FORM**

| FormID | FormTutor |
|---|---|
| 10A | Mr Adeyemi |
| 10B | Ms Danjuma |
| 11A | Mrs Hassan |
| 11B | Mr Okafor |

**CLUB**

| ClubID | ClubName | ClubDay | ClubLeader |
|---|---|---|---|
| C1 | Chess | Monday | Mrs Eze |
| C2 | Robotics | Friday | Mr Lawal |
| C3 | Drama | Wednesday | Ms Okon |
| C4 | Swimming | Saturday | Mr Bello |

**MEMBERSHIP**

| StudentID | ClubID |
|---|---|
| 101 | C1 |
| 101 | C2 |
| 102 | C1 |
| 103 | C3 |
| 103 | C1 |
| 103 | C2 |
| 104 | C2 |
| 105 | C3 |
| 106 | C1 |
| 107 | C4 |

Mrs Eze now appears once. To change the leader of Chess you edit one cell. A new club is one new row in CLUB, with no member needed. Grace's membership row can go without losing the Swimming club. To find which clubs Chioma attends, the database looks up 103 in MEMBERSHIP and follows each ClubID to the CLUB table.

The terms in the syllabus all have a home in these tables:

| Term | In this database |
|---|---|
| Entity | a student, a form, a club |
| Table | STUDENT, FORM, CLUB, MEMBERSHIP |
| Record (tuple) | one row, such as `101, Amina Bello, 10A` |
| Field (attribute) | one column, such as StudentName |
| Primary key | StudentID in STUDENT; FormID in FORM; ClubID in CLUB |
| Foreign key | FormID in STUDENT; StudentID and ClubID in MEMBERSHIP |
| Relationship | one form has many students; students and clubs (through MEMBERSHIP) |

### How a table design is written

Exam papers write a design as the table name in capitals, then its fields in brackets. This course writes the **primary key in bold** and marks each **foreign key with an asterisk** (an exam may underline the key instead). A field can be both.

:::key Writing a table design
TABLE(**PrimaryKey**, Field, ForeignKey*)

- STUDENT(**StudentID**, StudentName, FormID*)
- FORM(**FormID**, FormTutor)
- CLUB(**ClubID**, ClubName, ClubDay, ClubLeader)
- MEMBERSHIP(**StudentID***, **ClubID***)

In MEMBERSHIP both fields are bold and starred: together they form the primary key, and each one is also a foreign key.
:::

### How the relational model fixes each limitation

:::key What a relational database provides
| Limitation of files | How a relational database (with its DBMS) addresses it |
|---|---|
| Redundancy | Each fact is stored once and tables are linked by keys. |
| Inconsistency | There is one copy of each fact, so one edit changes it everywhere it is used. |
| Data dependence | The structure is stored once, in the database, and programs ask the DBMS for data. The structure can change without every program changing (data independence). |
| Poor security | Access rights can be set for each user or group, and backups are taken. |
| Poor integrity and sharing | Data types and validation rules are enforced, referential integrity is checked, and the DBMS controls several users changing data at once. |
| Hard to answer new questions | A query language (SQL) can ask any question of the linked tables. |
:::

## Keys

A table is useful only if each record can be found and told apart from every other. That is the job of a key.

:::def Primary key
A field (or set of fields) whose value is unique for every record in the table, so that it identifies exactly one record. It can never be empty.
:::

:::def Composite key
A primary key made of two or more fields, where it is the combination of values that is unique. MEMBERSHIP has one: the pair (StudentID, ClubID).
:::

:::def Candidate key
A field, or smallest set of fields, that could be chosen as the primary key because its values are unique for every record. A table can have several candidate keys.
:::

:::def Secondary key
A candidate key that was not chosen as the primary key: an alternative way to identify a record. A DBMS can build an index on a secondary key so that records can be found quickly by it.
:::

:::def Foreign key
A field in one table that holds values of the primary key of another table, which creates a link between the two tables.
:::

:::note Secondary key in other books
Some textbooks use "secondary key" for any field that is indexed to speed up searching, whether or not its values are unique. When an exam asks for a definition, give the idea above (an alternative candidate key, used for searching through an index) and the examiner will recognise it.
:::

A good primary key is unique, never empty, and never changes. That is why StudentID is a better choice than StudentName. Two students can share a name, a name can be misspelt, and a name can change. A made-up ID number avoids all three problems, and this is why almost every table has an ID field.

:::eg Which fields are keys? (exam style)
A company stores its staff in this table.

| EmployeeID | NationalIDNumber | Email | Name | DepartmentCode |
|---|---|---|---|---|
| E101 | 8801-4472 | asha@firm.example | Asha Khan | HR |
| E102 | 7915-0286 | ben@firm.example | Ben Mwale | IT |
| E103 | 9102-3340 | carla@firm.example | Carla Diaz | IT |
| E104 | 8530-7718 | dan@firm.example | Dan Khan | HR |

(a) State the candidate keys. [2] (b) State one field that could not be a candidate key and say why. [2] (c) EmployeeID is chosen as the primary key. Identify a secondary key and the foreign key. [2]

(a) EmployeeID, NationalIDNumber and Email: each value is unique for every employee. [B1] [B1] (one mark for two correct, a second for all three)

(b) Name, because two different employees could have the same name: a key must be unique for any data that may be stored, not only for the rows shown [B1]. DepartmentCode cannot be one either, because several employees share a department [B1].

(c) A secondary key is NationalIDNumber or Email, the candidate keys that were not chosen. [B1] DepartmentCode is the foreign key, because it would hold the primary key values of a DEPARTMENT table. [B1]

A foreign key does **not** have to be unique: many employees can hold the same DepartmentCode.
:::

## Relationships and entity-relationship diagrams

Tables are linked by **relationships**. There are three kinds, named by how many records on each side can be connected.

:::def Relationship
A link between two entities (tables). It is one-to-one, one-to-many or many-to-many, depending on how many records of each entity can be linked to one record of the other.
:::

:::cols
:::col One-to-one (1:1)
One record in A links to at most one record in B, and the other way round. One student has one locker, and a locker belongs to one student.
:::
:::col One-to-many (1:M)
One record in A links to many records in B, but each record in B links to only one in A. One form has many students; each student is in one form.
:::
:::col Many-to-many (M:M)
A record in A links to many in B, and a record in B links to many in A. A student joins many clubs and a club has many students.
:::
:::

An **entity-relationship (E-R) diagram** draws a database design: a box for each entity and a line for each relationship. The ends of the line show the type, in **crow's foot** notation. A single bar means "one" and three prongs (the crow's foot) mean "many".

:::html
<figure class="fig small"><svg viewBox="0 0 340 244" role="img" aria-label="Three small entity-relationship diagrams in crow's foot notation. One-to-one: STUDENT and LOCKER joined by a line with a single bar at each end. One-to-many: FORM and STUDENT, a bar at the FORM end and a crow's foot at the STUDENT end. Many-to-many: STUDENT and CLUB, a crow's foot at both ends."><rect class="fm s-acc sw2" x="20" y="12" width="80" height="36"/><text class="tl tb tc" x="60" y="35">STUDENT</text><rect class="fm s-acc sw2" x="240" y="12" width="80" height="36"/><text class="tl tb tc" x="280" y="35">LOCKER</text><line class="ln" x1="100" y1="30" x2="240" y2="30"/><line class="ln" x1="112" y1="22" x2="112" y2="38"/><line class="ln" x1="228" y1="22" x2="228" y2="38"/><text class="tl tc" x="170" y="22">one-to-one</text><text class="tl tc" x="170" y="70">one student has one locker</text><rect class="fm s-acc sw2" x="20" y="90" width="80" height="36"/><text class="tl tb tc" x="60" y="113">FORM</text><rect class="fm s-acc sw2" x="240" y="90" width="80" height="36"/><text class="tl tb tc" x="280" y="113">STUDENT</text><line class="ln" x1="100" y1="108" x2="240" y2="108"/><line class="ln" x1="112" y1="100" x2="112" y2="116"/><line class="ln" x1="240" y1="99" x2="224" y2="108"/><line class="ln" x1="240" y1="108" x2="224" y2="108"/><line class="ln" x1="240" y1="117" x2="224" y2="108"/><text class="tl tc" x="170" y="100">one-to-many</text><text class="tl tc" x="170" y="148">one form has many students</text><rect class="fm s-acc sw2" x="20" y="168" width="80" height="36"/><text class="tl tb tc" x="60" y="191">STUDENT</text><rect class="fm s-acc sw2" x="240" y="168" width="80" height="36"/><text class="tl tb tc" x="280" y="191">CLUB</text><line class="ln" x1="100" y1="186" x2="240" y2="186"/><line class="ln" x1="100" y1="177" x2="116" y2="186"/><line class="ln" x1="100" y1="186" x2="116" y2="186"/><line class="ln" x1="100" y1="195" x2="116" y2="186"/><line class="ln" x1="240" y1="177" x2="224" y2="186"/><line class="ln" x1="240" y1="186" x2="224" y2="186"/><line class="ln" x1="240" y1="195" x2="224" y2="186"/><text class="tl tc" x="170" y="178">many-to-many</text><text class="tl tc" x="170" y="226">each side has many of the other</text></svg><figcaption>The three kinds of relationship. The bar means one; the crow's foot (three prongs) means many.</figcaption></figure>
:::

:::key How each relationship is built in tables
- **One-to-many**: put a foreign key in the table on the **many** side. Many students are in one form, so STUDENT holds FormID. The foreign key is not unique: ten students can hold the same FormID.
- **One-to-one**: put a foreign key in either table, and make it unique. Often the two tables are simply merged into one.
- **Many-to-many**: it **cannot be stored directly**. A single field cannot hold "many" values without breaking the rules of 1NF (see below). Add a **link table** with a foreign key to each side. The two foreign keys together usually form the link table's composite primary key.
:::

The clubs database shows the rule at work. STUDENT and CLUB are many-to-many, so MEMBERSHIP sits between them. The many-to-many relationship becomes two one-to-many relationships.

:::html
<figure class="fig"><svg viewBox="0 0 580 188" role="img" aria-label="Two diagrams. Top: STUDENT and CLUB joined directly with a crow's foot at both ends, labelled many-to-many and marked as not allowed in a relational database. Bottom: the same data with a link table MEMBERSHIP between them: STUDENT has a bar and MEMBERSHIP a crow's foot on one side, CLUB has a bar and MEMBERSHIP a crow's foot on the other."><rect class="fm s-acc sw2" x="20" y="12" width="120" height="36"/><text class="tl tb tc" x="80" y="35">STUDENT</text><rect class="fm s-acc sw2" x="440" y="12" width="120" height="36"/><text class="tl tb tc" x="500" y="35">CLUB</text><line class="ln" x1="140" y1="30" x2="440" y2="30"/><line class="ln" x1="140" y1="21" x2="156" y2="30"/><line class="ln" x1="140" y1="30" x2="156" y2="30"/><line class="ln" x1="140" y1="39" x2="156" y2="30"/><line class="ln" x1="440" y1="21" x2="424" y2="30"/><line class="ln" x1="440" y1="30" x2="424" y2="30"/><line class="ln" x1="440" y1="39" x2="424" y2="30"/><text class="tl tc" x="290" y="20">many-to-many</text><text class="tl tc" x="290" y="50">cannot be stored directly</text><text class="tl tc" x="290" y="78">so split it with a link table</text><rect class="fm s-acc sw2" x="20" y="116" width="120" height="36"/><text class="tl tb tc" x="80" y="139">STUDENT</text><rect class="fm s-acc sw2" x="220" y="116" width="140" height="36"/><text class="tl tb tc" x="290" y="139">MEMBERSHIP</text><rect class="fm s-acc sw2" x="440" y="116" width="120" height="36"/><text class="tl tb tc" x="500" y="139">CLUB</text><line class="ln" x1="140" y1="134" x2="220" y2="134"/><line class="ln" x1="152" y1="126" x2="152" y2="142"/><line class="ln" x1="220" y1="125" x2="204" y2="134"/><line class="ln" x1="220" y1="134" x2="204" y2="134"/><line class="ln" x1="220" y1="143" x2="204" y2="134"/><line class="ln" x1="360" y1="134" x2="440" y2="134"/><line class="ln" x1="360" y1="125" x2="376" y2="134"/><line class="ln" x1="360" y1="134" x2="376" y2="134"/><line class="ln" x1="360" y1="143" x2="376" y2="134"/><line class="ln" x1="428" y1="126" x2="428" y2="142"/><text class="tl tc" x="290" y="178">two one-to-many relationships</text></svg><figcaption>A many-to-many relationship is resolved by a link table that holds a foreign key to each side.</figcaption></figure>
:::

Why does the link table work? Look at the MEMBERSHIP table. Student 103 appears in three rows (one per club) and club C1 appears in four rows (one per member). Each row records one fact: this student belongs to this club. No field holds a list.

:::eg Draw an E-R diagram (exam style)
A public library stores its members, its books and its loans. A member can borrow many books over time, and a book is borrowed by many members over time. Each loan records one member borrowing one book. Draw an E-R diagram for the three tables and state the type of relationship between each pair of tables. [4 marks]

The wording "borrow many books" and "borrowed by many members" describes a many-to-many relationship between MEMBER and BOOK. LOAN is the link table that holds one record for each time a book is borrowed.

:::html
<figure class="fig small"><svg viewBox="0 0 370 78" role="img" aria-label="Entity-relationship diagram: MEMBER has a one-to-many relationship with LOAN (bar at MEMBER, crow's foot at LOAN), and BOOK has a one-to-many relationship with LOAN (bar at BOOK, crow's foot at LOAN)."><rect class="fm s-acc sw2" x="10" y="20" width="90" height="36"/><text class="tl tb tc" x="55" y="43">MEMBER</text><rect class="fm s-acc sw2" x="140" y="20" width="90" height="36"/><text class="tl tb tc" x="185" y="43">LOAN</text><rect class="fm s-acc sw2" x="270" y="20" width="90" height="36"/><text class="tl tb tc" x="315" y="43">BOOK</text><line class="ln" x1="100" y1="38" x2="140" y2="38"/><line class="ln" x1="112" y1="30" x2="112" y2="46"/><line class="ln" x1="140" y1="29" x2="124" y2="38"/><line class="ln" x1="140" y1="38" x2="124" y2="38"/><line class="ln" x1="140" y1="47" x2="124" y2="38"/><line class="ln" x1="230" y1="38" x2="270" y2="38"/><line class="ln" x1="230" y1="29" x2="246" y2="38"/><line class="ln" x1="230" y1="38" x2="246" y2="38"/><line class="ln" x1="230" y1="47" x2="246" y2="38"/><line class="ln" x1="258" y1="30" x2="258" y2="46"/></svg><figcaption>One member makes many loans, and one book appears in many loans.</figcaption></figure>
:::

- three boxes labelled MEMBER, LOAN and BOOK, with LOAN in the middle [B1]
- a line between MEMBER and LOAN and a line between LOAN and BOOK [B1]
- crow's feet at the LOAN end of both lines, and a single bar (or nothing) at the MEMBER and BOOK ends [B1]
- MEMBER to LOAN is one-to-many, and BOOK to LOAN is one-to-many (so MEMBER to BOOK is many-to-many through LOAN) [B1]
:::

## Referential integrity

A foreign key is a promise: "this value identifies a real record in another table". If the promise is broken, the database holds a record that points at nothing.

:::def Referential integrity
A rule that every foreign key value must match an existing primary key value in the table it refers to, so that a relationship never points at a record that does not exist.
:::

In the clubs database:

- Adding the MEMBERSHIP row `(108, C1)` must be refused if there is no student 108. Otherwise the table records a student who does not exist.
- Adding `(101, C9)` must be refused if there is no club C9.
- Deleting student 103 from STUDENT while MEMBERSHIP still holds three rows for 103 would leave three **orphan** records. The DBMS refuses the delete, or the designer chooses to delete the three membership rows first.
- Changing the primary key of a club (C1 to C7) while MEMBERSHIP still says C1 would break every link to it.

The DBMS checks each of these when the foreign key is declared (the next chapter shows the statement). The database is then protected from a whole class of mistakes, instead of relying on every program to be careful.

## Indexing

Finding the record with StudentID 106 in a table of seven records is easy. In a table of ten million records, checking the records one after another would take far too long. An **index** solves this.

:::def Index
A separate, sorted structure built on one or more fields of a table. It holds each value of the field with a pointer to the record that has it, so the DBMS can find records without reading the whole table.
:::

:::analogy
The index at the back of a textbook lists topics in alphabetical order with page numbers. To find "voltage" you look it up in the sorted index and jump to the page, instead of reading every page from the start. A database index works the same way: sorted values, each with a pointer to where the record is stored.
:::

Here is an index on StudentName for the STUDENT table. The records stay where they are, in the order they were entered (the record number is their position). The index is sorted by name, so a search can halve the range at each step.

| StudentName (sorted) | Record number |
|---|---|
| Amina Bello | 1 |
| Bilal Yusuf | 2 |
| Chioma Obi | 3 |
| Dev Nair | 4 |
| Elena Cruz | 5 |
| Farid Aziz | 6 |
| Grace Mensah | 7 |

Searching a sorted index of a million values needs at most about 20 comparisons, because \(2^{20} = 1\,048\,576\) and each comparison halves the range. Searching the table one record after another may need a million. (The halving method is the binary search in [Searching, sorting and Big O](#cs.algorithms2).)

The primary key is normally indexed automatically. A **secondary key** is the usual field to index when users often search by it, for example a table of employees searched by Email.

:::key Index: benefit and cost
- **Benefit**: much faster searching and sorting on the indexed field, and faster joins between tables on keys.
- **Cost**: the index takes extra storage, and every insert, update or delete must also update the index, so writing is slower. Index the fields that are searched often, not every field.
:::

## Normalisation

How do you decide what the tables should be? You could guess, as we did for the clubs. **Normalisation** is the step-by-step method that finds the right tables for any set of data.

:::def Normalisation
The process of organising the data in a database into tables, by applying a series of rules (normal forms), so that redundancy is removed and the anomalies it causes cannot happen.
:::

The method uses one idea: a **dependency**. One field depends on another when knowing the value of the second tells you the value of the first. A student's name depends on the StudentID: once you have the ID, there is exactly one name. We write StudentID → StudentName.

:::def Dependency
Field B depends on field A (written A → B) when each value of A determines exactly one value of B. In a table, a non-key field should depend on the primary key.
:::

There are three normal forms, each one adding a rule to the one before.

:::def First normal form (1NF)
A table is in 1NF when every field holds one single value (no lists), there are no repeating groups of fields, and there is a primary key that identifies each record.
:::

:::def Second normal form (2NF)
A table is in 2NF when it is in 1NF and has no partial dependencies: every non-key field depends on the whole of the primary key, not on only part of it.
:::

:::def Third normal form (3NF)
A table is in 3NF when it is in 2NF and has no non-key dependencies: no non-key field depends on another non-key field (no transitive dependencies).
:::

:::key Remembering the three forms
Every non-key field must depend on **the key** (1NF), **the whole key** (2NF) and **nothing but the key** (3NF).

- 2NF can only be broken when the primary key is **composite**. A 1NF table whose primary key is one field is already in 2NF.
- 3NF is broken when a non-key field is really described by another non-key field.
:::

### Worked normalisation: an order book

A stationery supplier records each order on one line. The first column is the key. The last column lists every product ordered, so it is a repeating group.

**Unnormalised data**

| OrderID | OrderDate | CustomerID | CustomerName | City | Items ordered |
|---|---|---|---|---|---|
| 5001 | 03/10/2026 | C07 | Mercy Banda | Lusaka | P12 Pencil box 3.50 × 10; P20 Stapler 6.00 × 2 |
| 5002 | 03/10/2026 | C11 | Tariq Rahman | Lahore | P12 Pencil box 3.50 × 4 |
| 5003 | 04/10/2026 | C07 | Mercy Banda | Lusaka | P31 Paper ream 4.75 × 6; P20 Stapler 6.00 × 1; P12 Pencil box 3.50 × 2 |
| 5004 | 05/10/2026 | C15 | Lucas Ortiz | Lima | P31 Paper ream 4.75 × 3 |

The facts behind the data (the dependencies) come from the way the business works, and you must be able to state them: an order has one date and one customer; a customer has one name and one city; a product has one name and one price; and the quantity depends on **which order and which product**.

- OrderID → OrderDate, CustomerID
- CustomerID → CustomerName, City
- ProductID → ProductName, UnitPrice
- (OrderID, ProductID) → Quantity

:::steps
1. **To 1NF.** Remove the repeating group: give every item its own row, repeating the order details, and choose a primary key that identifies each row. An order line is identified by the order and the product together, so the key is the composite (**OrderID**, **ProductID**).
2. **To 2NF.** Look at each non-key field and ask: does it depend on the whole key or only part? Fields that depend on part of the key move to a table of their own.
3. **To 3NF.** In each table, ask whether any non-key field depends on another non-key field. If so, move both to a new table, and leave the one they depend on behind as a foreign key.
:::

**First normal form.** Every field now has one value, and the repeating group is gone. There are seven rows, one for each product on each order.

| **OrderID** | **ProductID** | OrderDate | CustomerID | CustomerName | City | ProductName | UnitPrice | Quantity |
|---|---|---|---|---|---|---|---|---|
| 5001 | P12 | 03/10/2026 | C07 | Mercy Banda | Lusaka | Pencil box | 3.50 | 10 |
| 5001 | P20 | 03/10/2026 | C07 | Mercy Banda | Lusaka | Stapler | 6.00 | 2 |
| 5002 | P12 | 03/10/2026 | C11 | Tariq Rahman | Lahore | Pencil box | 3.50 | 4 |
| 5003 | P31 | 04/10/2026 | C07 | Mercy Banda | Lusaka | Paper ream | 4.75 | 6 |
| 5003 | P20 | 04/10/2026 | C07 | Mercy Banda | Lusaka | Stapler | 6.00 | 1 |
| 5003 | P12 | 04/10/2026 | C07 | Mercy Banda | Lusaka | Pencil box | 3.50 | 2 |
| 5004 | P31 | 05/10/2026 | C15 | Lucas Ortiz | Lima | Paper ream | 4.75 | 3 |

The table is in 1NF, but the redundancy is back: Mercy Banda's name and city appear five times, and the Pencil box's price three times. Change the price of a pencil box and three rows must change.

**Second normal form.** The key has two parts, so test each non-key field against them.

| Field | Depends on | Whole key? |
|---|---|---|
| OrderDate, CustomerID, CustomerName, City | OrderID only | no: partial dependency |
| ProductName, UnitPrice | ProductID only | no: partial dependency |
| Quantity | OrderID and ProductID together | yes |

Move each group of partly dependent fields into a table whose key is the part they depend on.

- ORDERS(**OrderID**, OrderDate, CustomerID, CustomerName, City)
- PRODUCT(**ProductID**, ProductName, UnitPrice)
- ORDERLINE(**OrderID***, **ProductID***, Quantity)

**Third normal form.** ORDERLINE and PRODUCT are already in 3NF. In ORDERS, CustomerName and City do not describe the order. They describe the customer: OrderID → CustomerID → CustomerName. A non-key field (CustomerName) depends on another non-key field (CustomerID). This is a **transitive dependency**. Move the customer fields to their own table, and keep CustomerID in ORDERS as the foreign key.

- CUSTOMER(**CustomerID**, CustomerName, City)
- ORDERS(**OrderID**, OrderDate, CustomerID*)
- PRODUCT(**ProductID**, ProductName, UnitPrice)
- ORDERLINE(**OrderID***, **ProductID***, Quantity)

The tables, with their data:

**CUSTOMER**

| CustomerID | CustomerName | City |
|---|---|---|
| C07 | Mercy Banda | Lusaka |
| C11 | Tariq Rahman | Lahore |
| C15 | Lucas Ortiz | Lima |

**ORDERS**

| OrderID | OrderDate | CustomerID |
|---|---|---|
| 5001 | 03/10/2026 | C07 |
| 5002 | 03/10/2026 | C11 |
| 5003 | 04/10/2026 | C07 |
| 5004 | 05/10/2026 | C15 |

**PRODUCT**

| ProductID | ProductName | UnitPrice |
|---|---|---|
| P12 | Pencil box | 3.50 |
| P20 | Stapler | 6.00 |
| P31 | Paper ream | 4.75 |

**ORDERLINE**

| OrderID | ProductID | Quantity |
|---|---|---|
| 5001 | P12 | 10 |
| 5001 | P20 | 2 |
| 5002 | P12 | 4 |
| 5003 | P31 | 6 |
| 5003 | P20 | 1 |
| 5003 | P12 | 2 |
| 5004 | P31 | 3 |

Nothing has been lost. Joining the tables back together through the keys rebuilds the seven rows of the 1NF table exactly. Nothing is repeated now: Mercy's city is stored once, so moving her to Ndola is a one-cell change.

:::html
<figure class="fig"><svg viewBox="0 0 560 262" role="img" aria-label="Entity-relationship diagram of four tables in crow's foot notation. CUSTOMER (CustomerID primary key, CustomerName, City) has a one-to-many relationship with ORDERS (OrderID primary key, OrderDate, CustomerID foreign key). ORDERS has a one-to-many relationship with ORDERLINE (OrderID and ProductID, both primary key and foreign key, and Quantity). PRODUCT (ProductID primary key, ProductName, UnitPrice) has a one-to-many relationship with ORDERLINE."><rect class="fm s-acc sw2" x="20" y="14" width="190" height="86"/><text class="tl tb tc" x="115" y="32">CUSTOMER</text><line class="ln" x1="20" y1="40" x2="210" y2="40"/><text class="tl" x="28" y="55">CustomerID</text><text class="tl te" x="202" y="55">PK</text><text class="tl" x="28" y="75">CustomerName</text><text class="tl" x="28" y="95">City</text><rect class="fm s-acc sw2" x="340" y="14" width="200" height="86"/><text class="tl tb tc" x="440" y="32">ORDERS</text><line class="ln" x1="340" y1="40" x2="540" y2="40"/><text class="tl" x="348" y="55">OrderID</text><text class="tl te" x="532" y="55">PK</text><text class="tl" x="348" y="75">OrderDate</text><text class="tl" x="348" y="95">CustomerID</text><text class="tl te" x="532" y="95">FK</text><rect class="fm s-acc sw2" x="20" y="160" width="190" height="86"/><text class="tl tb tc" x="115" y="178">PRODUCT</text><line class="ln" x1="20" y1="186" x2="210" y2="186"/><text class="tl" x="28" y="201">ProductID</text><text class="tl te" x="202" y="201">PK</text><text class="tl" x="28" y="221">ProductName</text><text class="tl" x="28" y="241">UnitPrice</text><rect class="fm s-acc sw2" x="340" y="160" width="200" height="86"/><text class="tl tb tc" x="440" y="178">ORDERLINE</text><line class="ln" x1="340" y1="186" x2="540" y2="186"/><text class="tl" x="348" y="201">OrderID</text><text class="tl te" x="532" y="201">PK, FK</text><text class="tl" x="348" y="221">ProductID</text><text class="tl te" x="532" y="221">PK, FK</text><text class="tl" x="348" y="241">Quantity</text><line class="ln" x1="210" y1="54" x2="340" y2="54"/><line class="ln" x1="222" y1="46" x2="222" y2="62"/><line class="ln" x1="340" y1="45" x2="324" y2="54"/><line class="ln" x1="340" y1="54" x2="324" y2="54"/><line class="ln" x1="340" y1="63" x2="324" y2="54"/><text class="tl tc" x="275" y="46">places</text><line class="ln" x1="440" y1="100" x2="440" y2="160"/><line class="ln" x1="432" y1="112" x2="448" y2="112"/><line class="ln" x1="431" y1="160" x2="440" y2="144"/><line class="ln" x1="440" y1="160" x2="440" y2="144"/><line class="ln" x1="449" y1="160" x2="440" y2="144"/><text class="tl" x="450" y="132">contains</text><line class="ln" x1="210" y1="200" x2="340" y2="200"/><line class="ln" x1="222" y1="192" x2="222" y2="208"/><line class="ln" x1="340" y1="191" x2="324" y2="200"/><line class="ln" x1="340" y1="200" x2="324" y2="200"/><line class="ln" x1="340" y1="209" x2="324" y2="200"/><text class="tl tc" x="275" y="192">is sold on</text></svg><figcaption>The finished design from the order example: four tables, linked by foreign keys.</figcaption></figure>
:::

:::warn Common mistakes about normal forms
- "3NF means no repeated data" is incomplete. 3NF means no non-key field depends on another non-key field. Foreign keys are repeated by design: every order for Mercy holds C07.
- 2NF only matters when the key is composite. Never say a table with a single-field primary key fails 2NF.
- A foreign key does not have to be unique. In ORDERS many records hold the same CustomerID.
- Splitting a table is not enough. Each new table needs a primary key, and the link back (the foreign key) must stay, or the data cannot be rejoined.
:::

:::eg Explain why a table is not in 3NF (exam style)
A hotel keeps this table. BookingID is the primary key.

BOOKING(**BookingID**, CheckInDate, GuestID, GuestName, RoomNo, RoomType)

A guest has one name and each room has one type. Explain why the table is not in third normal form, and rewrite the design in 3NF. [5 marks]

A table in 3NF has no non-key field that depends on another non-key field. Look for a pair like that.

- GuestName depends on GuestID, which is not the primary key [B1]
- RoomType depends on RoomNo, which is not the primary key [B1]
- these are dependencies between non-key fields (transitive dependencies), so the table is not in 3NF [B1]
- GUEST(**GuestID**, GuestName) and ROOM(**RoomNo**, RoomType) as separate tables [B1]
- BOOKING(**BookingID**, CheckInDate, GuestID*, RoomNo*) keeping the two foreign keys [B1]

The table is already in 2NF because its primary key is a single field.
:::

:::eg Is it in 2NF? (exam style)
RESULT(**StudentID**, **SubjectCode**, SubjectTitle, Mark) holds one record for each mark a student has scored in a subject. The primary key is composite. Show that the table is not in 2NF and fix it. [4 marks]

- Mark depends on both StudentID and SubjectCode (a mark belongs to one student in one subject), so it depends on the whole key [B1]
- SubjectTitle depends on SubjectCode alone, which is only part of the key, so there is a partial dependency and the table is not in 2NF [B1]
- SUBJECT(**SubjectCode**, SubjectTitle) [B1]
- RESULT(**StudentID***, **SubjectCode***, Mark) [B1]
:::

## The database management system

You do not look after the tables, keys and links by hand. A **database management system (DBMS)** does it. It sits between the users and programs on one side and the stored data on the other, and every request goes through it.

:::def Database management system (DBMS)
Software that creates, manages and controls access to a database. Programs and users send requests to the DBMS, which carries them out on the stored data.
:::

Each feature of a DBMS answers one of the limitations of a file-based approach.

| DBMS feature | What it does | The file-based problem it solves |
|---|---|---|
| Data management | stores, retrieves, updates and deletes data, and keeps the data dictionary up to date | redundancy, inconsistency and data dependence |
| Data modelling | provides tools to define the entities, fields and relationships (the logical schema) | no single agreed structure |
| Data integrity | enforces data types, validation rules and referential integrity, and controls several users at once | errors and overwriting |
| Data security | access rights for each user or group, passwords, and backup procedures | anyone can see or change the whole file |

:::def Data dictionary
A store of information about the database itself (metadata), maintained by the DBMS: the names of the tables and fields, their data types and sizes, validation rules, the keys, and the relationships between tables.
:::

For the STUDENT table of the clubs database, the data dictionary entry could look like this.

| Field | Data type | Size | Validation | Key |
|---|---|---|---|---|
| StudentID | INTEGER | | a whole number from 100 to 999 | primary key |
| StudentName | VARCHAR | 30 | presence check: must not be empty | |
| FormID | CHARACTER | 3 | must match a FormID in FORM | foreign key |

Because the structure is stored once, in the dictionary, a program no longer needs it built in. The DBMS answers "what is the structure?" and the program asks it. That is how a DBMS gives **data independence**.

:::def Logical schema
The description of the whole database as a user or designer sees it: the tables, fields, data types, keys and relationships. It does not say where or how the data is stored on disk.
:::

Because applications use the logical schema, the DBMS can reorganise the files on disk without any program changing.

:::key Data integrity and data security in a DBMS
**Integrity** (the data is correct and consistent): data types and size limits; validation rules; primary keys that must be unique; referential integrity on foreign keys; locking, so that two users cannot overwrite the same record at once.

**Security** (the data is protected): **access rights** that give each user or group of users only the permissions they need (for example a receptionist may add appointments but not delete patient records); passwords to identify users; **backup procedures**, which are regular copies of the database kept in a safe place and used to restore it after a fault, a mistake or an attack.
:::

Two more tools in the DBMS are named in the syllabus, and each has a purpose that examiners ask for.

:::def Developer interface
The tools a DBMS gives to designers and programmers to build and change a database: to define tables, fields, keys and relationships, and to create queries, forms and reports, often through a visual screen or by typing commands, so they do not have to write the storage code themselves.
:::

:::def Query processor
The part of the DBMS that takes a request for data (a query, usually in SQL), checks that it is valid, works out an efficient way to carry it out, and executes it to produce the result.
:::

:::exam Matching a feature to a purpose
Questions usually ask for the purpose of a feature or for a feature that solves a stated problem. Write the feature's name, then what it does, then the problem it fixes: "The data dictionary stores the structure of the database, so programs do not need the layout built in" scores, while "it stores data" does not.
:::

:::eg Spot the error: which normal form fails?
Question: The table below stores pupils and their form tutors. PupilID is the primary key. State which normal form the table first fails and explain why. [3 marks]

PUPIL(**PupilID**, PupilName, FormCode, FormTutor)

A student wrote:

```text
01  The table is not in second normal form.
02  This is because FormTutor depends only on part of the key.
03  FormTutor should be moved to a separate table.
```

Line 01 names the wrong normal form and line 02 gives a wrong reason [B0] [B0]. The primary key is a single field, so there is no "part of the key" and the table is automatically in 2NF. The real fault is that FormTutor depends on FormCode, which is a non-key field, so the table fails **third** normal form. Line 03 is a correct repair [B1], because FormTutor and FormCode should move to a FORM table. The answer scores 1 out of 3.

A correct answer: "The table is in 2NF because the key is one field, but it is not in 3NF [B1] because FormTutor depends on FormCode, a non-key field (a transitive dependency) [B1]. Move FormCode and FormTutor to a new FORM table and keep FormCode in PUPIL as a foreign key [B1]."
:::

:::try Start easy, finish at exam standard
Q: In a database table, what is the difference between a record and a field?
A: A record is one row: all the data about one thing. A field is one column: one item of data about each thing.
Q: A form has many students. Which table holds the foreign key?
A: STUDENT, the table on the many side. It holds the FormID of the form each student is in.
Q: Is a table that has a field PhoneNumbers holding `0712 111 222, 0733 444 555` in 1NF?
A: No. The field holds two values, so it is not atomic. Each number needs its own row, or its own table.
Q: A table in 1NF has the single-field primary key BookID. Is it in 2NF?
A: Yes. 2NF can only be broken by a partial dependency, which needs a composite key, and there is none.
Q: Give one reason why a table of employees uses EmployeeID, not Name, as its primary key.
A: Names are not unique (two employees can share a name), and a name can change or be misspelt. The ID is unique and never changes.
Q: State one benefit and one drawback of adding an index to a field.
A: Benefit: searches on that field are much faster. Drawback: the index takes extra storage, and inserts, updates and deletes are slower because the index must be updated too.
Q: Name the type of relationship between TEACHER and CLASS if a teacher teaches many classes and each class has one teacher, and say where the foreign key goes.
A: One-to-many. The foreign key (TeacherID) goes in CLASS, the table on the many side.
Q: The DBMS refuses to delete a customer who still has orders. Which feature does that, and what does it prevent?
A: Referential integrity. It prevents orphan records: orders whose CustomerID no longer matches any customer.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the type of relationship (one-to-one, one-to-many or many-to-many) between each pair of entities. (a) COUNTRY and CAPITAL CITY, where every country has exactly one capital and every capital belongs to one country. (b) WARD and PATIENT, where a ward holds many patients and each patient is in one ward. (c) DOCTOR and PATIENT, where a patient may see many doctors and a doctor sees many patients.
A: (a) one-to-one [B1] (b) one-to-many [B1] (c) many-to-many [B1]

Q: [4 marks] ★ A company stores its vehicles in the table VEHICLE with the fields Registration, ChassisNumber, Make, Colour and OwnerID. Registration and ChassisNumber are both unique for each vehicle. OwnerID holds the ID of the vehicle's owner, whose details are in an OWNER table. (a) State the candidate keys. [1] (b) The designer chooses Registration as the primary key. Identify the secondary key and give the field that is a foreign key. [2] (c) Explain why Colour is not a suitable primary key. [1]
A: (a) Registration and ChassisNumber [B1]
(b) the secondary key is ChassisNumber, a candidate key not chosen as the primary key [B1]; the foreign key is OwnerID [B1]
(c) many vehicles can have the same colour, so the values are not unique [B1]

Q: [5 marks] ★★ A clinic uses one file with a row for every appointment. Each row repeats the patient's name, address and date of birth. (a) Explain two problems that this causes. [4] (b) State how a relational database avoids the first problem. [1]
H: Think of the update anomaly, and of what happens when a patient moves house.
A: (a) data redundancy: the patient's details are stored again for every appointment [B1], which wastes storage (or means the same fact must be typed many times) [B1]; data inconsistency: if the address is changed in some rows but not in others [B1], the file holds two different addresses for the same patient [B1]
(b) the patient's details are stored once, in a PATIENT table, and each appointment holds only the PatientID as a foreign key [B1]

Q: [5 marks] ★★ A school stores its students in one table: STUDENT(**StudentID**, StudentName, HouseID, HouseName, HouseCaptain). A house has one name and one captain. Explain why this table is not in 3NF and show a design that is. 
H: Ask which non-key fields are really facts about the house, not about the student.
H: Which field links STUDENT to the new table?
A: HouseName and HouseCaptain depend on HouseID [B1], which is a non-key field (a transitive dependency), so the table is not in 3NF [B1]. HOUSE(**HouseID**, HouseName, HouseCaptain) [B1]; STUDENT(**StudentID**, StudentName, HouseID*) [B1]; HouseID in STUDENT is a foreign key linked to HOUSE [B1].

Q: [6 marks] ★★ A medical clinic's DBMS holds patient records. (a) Describe two ways in which the DBMS keeps the data secure. [4] (b) State two items of information that the data dictionary holds about the PATIENT table. [2]
A: (a) access rights: each user or group is given only the permissions they need [B1], for example a receptionist may add appointments but cannot read or change medical notes [B1]; backup procedures: regular copies of the database are made and kept safe [B1], so the data can be restored after a fault or an attack [B1] (passwords with user names also score as one way, with the same two-mark pattern)
(b) any two from: the field names; the data types; the field sizes; the validation rules; the primary key and foreign keys; the relationships with other tables [B1] [B1]

Q: [5 marks] ★★ A language school's students enrol on courses. Each course has many students and a student can enrol on many courses. The date of each enrolment is stored. (a) Explain why the relationship between STUDENT and COURSE cannot be stored directly in two tables. [1] (b) Write a table design, with primary keys and foreign keys marked, that stores the data. [4]
H: A single field cannot hold a list of values.
A: (a) a field would need to hold several values (a list), which breaks first normal form [B1]
(b) STUDENT(**StudentID**, StudentName) and COURSE(**CourseID**, CourseTitle) [B1]; a link table ENROLMENT [B1] with fields StudentID, CourseID and EnrolmentDate [B1]; the primary key is the composite (StudentID, CourseID), each part being a foreign key [B1]

Q: [9 marks] ★★★ A garage records each repair job in a table. A vehicle has one owner, and each type of work has one description.

| JobID | JobDate | Registration | VehicleType | OwnerName | Work done (code, description, hours) |
|---|---|---|---|---|---|
| 301 | 02/11/2026 | KDA214T | Van | Ms Wanjiru | W1 Oil change 0.5; W2 Brake check 1.0 |
| 302 | 02/11/2026 | KBX880M | Saloon | Mr Otieno | W2 Brake check 1.5 |
| 303 | 05/11/2026 | KDA214T | Van | Ms Wanjiru | W1 Oil change 0.5; W3 Tyre rotation 0.75 |
| 304 | 06/11/2026 | KCM059L | Saloon | Ms Achieng | W3 Tyre rotation 1.0 |

(a) State why the table is not in first normal form. [1] (b) Write the primary key of the table once it is in 1NF. [1] (c) Normalise the data to third normal form. Show each table with its primary key and foreign keys marked. [7]
H: A job has one date and one vehicle. A vehicle (Registration) has one type and one owner.
H: The hours depend on the job and the work type together.
A: (a) the last column holds a list of values (a repeating group), so a field has more than one value [B1]
(b) the composite key (JobID, WorkCode) [B1]
(c) JOB(**JobID**, JobDate, Registration*) with the primary key and Registration as a foreign key [B1] [B1]; VEHICLE(**Registration**, VehicleType, OwnerName) [B1]; WORK(**WorkCode**, WorkDescription) [B1]; JOBWORK with the composite primary key (JobID, WorkCode) [B1], each part marked as a foreign key [B1], and Hours kept in JOBWORK because it depends on both parts of the key [B1]

(The vehicle fields leave JOB because they depend on Registration, a transitive dependency. WorkDescription leaves the 1NF table because it depends on WorkCode alone, a partial dependency.)

Q: [6 marks] ★★★ An online shop has an ORDERS table with 2 million records. Each record holds a CustomerID, which is a foreign key to the CUSTOMER table. (a) Explain what referential integrity prevents, using this example. [2] (b) The shop creates an index on CustomerID in ORDERS. Explain how this makes a search for one customer's orders faster. [2] (c) State two disadvantages of adding indexes. [2]
H: What would a record with a CustomerID of 99999 mean if there is no customer 99999?
A: (a) a foreign key value must match an existing primary key value [B1], so an order cannot be added for a customer who does not exist (and a customer with orders cannot be deleted, leaving orphan orders) [B1]
(b) the index holds the CustomerID values in sorted order, each with a pointer to its record [B1], so the DBMS can search the sorted index quickly instead of reading all 2 million records in turn [B1]
(c) the index needs extra storage space [B1]; every insert, update or delete must also update the index, which slows writing [B1]
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A city's bike-share scheme records the following. Each station has an ID, a name and a number of docks. Each bike has an ID and a date it was bought. A rider has an ID and a name. A trip records one rider using one bike from one station and returning it to one station (which may be the same one), with the start time and the end time. (a) State the entities and the relationships between them, with their types. [3] (b) Write the table designs with primary keys and foreign keys marked. [4] (c) Explain why TRIP needs two foreign keys that link to STATION. [1]
H: Which entity holds the "many" side of every relationship?
H: TRIP has to say where it started and where it ended, which are two different facts.
A: (a) entities: STATION, BIKE, RIDER and TRIP [B1]; RIDER to TRIP is one-to-many, and BIKE to TRIP is one-to-many (a rider makes many trips, a bike is used for many trips) [B1]; STATION to TRIP is one-to-many for the start station and again for the end station [B1]
(b) STATION(**StationID**, StationName, Docks) [B1]; BIKE(**BikeID**, DateBought) and RIDER(**RiderID**, RiderName) [B1]; TRIP(**TripID**, RiderID*, BikeID*, StartStationID*, EndStationID*, StartTime, EndTime) [B1]; every foreign key is placed in TRIP, the table on the many side, and has the same data type as the key it refers to [B1]
(c) the start station and the end station are two separate facts about a trip and may be different stations, so each needs its own field, and both are foreign keys to the primary key StationID [B1]

Q: [4 marks] ★★★ A designer suggests copying FormTutor into the STUDENT table of the clubs database "to save looking it up". STUDENT would then be STUDENT(**StudentID**, StudentName, FormID*, FormTutor). Evaluate this idea.
H: Which normal form does it break, and what happens when a tutor changes?
A: It breaks 3NF, because FormTutor depends on FormID, a non-key field [B1]. The tutor's name would be stored once for every student in the form, so the data is redundant [B1]. If a form gets a new tutor, every student record in the form must be changed, and missing one leaves the database inconsistent [B1]. The only benefit is that a search for a student's tutor needs no second table, which saves one lookup, but a join to a small FORM table is fast and this does not outweigh the risk of inconsistent data [B1].
:::

:::quiz
? Which of these describes a many-to-many relationship?
- A form has many students and each student is in one form.
- Each student has one locker and each locker belongs to one student.
+ A student can join many clubs and a club can have many students.
- A club has one leader and a leader runs one club.
> Many-to-many means that records on both sides can link to several on the other. The first option is one-to-many and the second and fourth are one-to-one.
? The primary key of a table is a composite of two fields. What does that mean?
- The table has two primary keys.
- Each of the two fields must be unique on its own.
+ The combination of the two values is unique for every record.
- One of the fields is a foreign key and the other is not.
> A composite key uses two or more fields together. Each field on its own may repeat (a student appears in several memberships), but the pair identifies one record.
? A 1NF table has the single-field primary key OrderID. Which statement is correct?
- It cannot be in 2NF.
+ It is already in 2NF because there is no composite key.
- It must have partial dependencies.
- It must also be in 3NF.
> 2NF removes partial dependencies, which can only exist when the key has more than one field. A single-field key makes the table 2NF automatically, but it may still fail 3NF.
? In the table STAFF(**StaffID**, Name, DeptCode, DeptName), which fault means the table is not in 3NF?
- DeptName is repeated for each department.
- Name depends on StaffID.
+ DeptName depends on DeptCode, which is not the primary key.
- StaffID is not a foreign key.
> A non-key field (DeptName) depends on another non-key field (DeptCode): a transitive dependency. Repeated data is the symptom, not the definition.
? What does referential integrity guarantee?
- Every table has a primary key.
- Every field has the right data type.
+ A foreign key value always matches an existing primary key value.
- A foreign key value is unique.
> Referential integrity stops a record pointing at a record that does not exist. Foreign key values are usually repeated, so uniqueness is wrong.
? Why does a DBMS keep a data dictionary?
- To hold the data that users enter.
- To store backup copies of the tables.
+ To hold information about the structure of the database, so programs do not need it built in.
- To check the spelling of data.
> The dictionary stores metadata: table and field names, types, sizes, rules, keys and relationships. It holds data about the data, not the data itself.
? A drawback of adding an index to a field is that
- searches on the field become slower.
- the field can no longer be updated.
+ inserts, updates and deletes become slower and the index needs storage.
- the field becomes the primary key.
> The index must be kept in step with the table, so every change also changes the index. Searches get faster, not slower.
:::

:::checklist What you can now do
- [ ] I can describe the limitations of a file-based approach: redundancy, inconsistency, data dependence, poor security and integrity.
- [ ] I can describe how a relational database addresses each limitation.
- [ ] I can use the terms entity, table, record, tuple, field and attribute correctly.
- [ ] I can define and identify a primary key, a candidate key, a secondary key, a composite key and a foreign key.
- [ ] I can identify one-to-one, one-to-many and many-to-many relationships, and resolve a many-to-many relationship with a link table.
- [ ] I can draw and read an entity-relationship diagram in crow's foot notation.
- [ ] I can explain referential integrity and what an index is, with a benefit and a cost.
- [ ] I can explain why a table is, or is not, in 1NF, 2NF or 3NF.
- [ ] I can produce a normalised design (to 3NF) from a description, a set of data or a set of tables.
- [ ] I can describe what a DBMS does: data management and the data dictionary, data modelling, the logical schema, integrity, security, the developer interface and the query processor.
:::

:::recap
- A file-based approach has redundancy, inconsistency, data dependence, poor security and poor integrity. Redundancy causes update, insertion and deletion anomalies.
- A relational database stores data in linked tables: entity = table, record (tuple) = row, field (attribute) = column.
- Primary key: unique, never empty, identifies a record. Candidate keys could be primary keys; a secondary key is a candidate key not chosen. A composite key uses two or more fields. A foreign key holds another table's primary key values and need not be unique.
- One-to-many: foreign key on the many side. Many-to-many: a link table with two foreign keys. In crow's foot notation a bar is one and three prongs are many.
- Referential integrity: a foreign key value must match an existing primary key value. An index is a sorted structure that speeds searches but slows writes and uses storage.
- Normalisation: 1NF atomic values, no repeating groups, a primary key; 2NF no partial dependencies; 3NF no non-key dependencies. Every non-key field depends on the key, the whole key and nothing but the key.
- A DBMS provides data management (with the data dictionary), data modelling, the logical schema, data integrity and data security (access rights and backups), a developer interface and a query processor.
:::

:::links
- practise: [SQLBolt](https://sqlbolt.com/) · SQLBolt · interactive lessons that use tables and keys like these (SQL is the next chapter)
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations of relational databases and normalisation, with questions (written for UK boards)
- read: [W3Schools SQL](https://www.w3schools.com/sql/) · W3Schools · short lessons that define the terms used for tables and keys
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · search the channel for "relational databases" for a university explanation
- papers: [PapaCambridge 9618 past papers](https://pastpapers.papacambridge.com/papers/caie/as-and-a-level-computer-science-9618) · PapaCambridge · Paper 1 has a database question; find the topic by scanning the question list [unofficial]

Links checked 13 November 2026.
:::

Next: [DBMS and SQL](#cs.sql)
