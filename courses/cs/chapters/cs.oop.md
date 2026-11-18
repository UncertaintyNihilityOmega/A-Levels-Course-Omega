@chapter cs.oop
@title Object-oriented programming
@level a2
@paper CAIE 9618 Papers 3 and 4
@time 7–9 hours
@summary Object-oriented programming builds a program from objects that hold their own data and the methods that work on it. You will learn classes, objects, constructors, encapsulation with getters and setters, inheritance, polymorphism and containment, draw class diagrams, and design and write classes in pseudocode and Python.

:::why
Large programs are made of many kinds of thing that each have data and behaviour: accounts, vehicles, tickets, game characters. Object-oriented programming (OOP) keeps each thing's data and the code that uses it together in one place, so a team can change one part without breaking the rest. Paper 3 asks you to use the terms, read and complete class diagrams and write class pseudocode. Paper 4 asks you to write classes, subclasses and lists of objects on a computer and test them.
:::

**Before you start**, you should be comfortable with records from [Data types, records and arrays](#cs.datatypes), functions and parameters from [Procedures, functions and parameters](#cs.procedures), and the idea of a recursive structure from [Recursion](#cs.recursion).

:::try Warm-up
Q: A record type `Book` has the fields Title, Author and Price. How do you read the Price field of a variable `ThisBook`? (from [Data types, records and arrays](#cs.datatypes))
A: With dot notation: `ThisBook.Price`.
Q: What is the difference between a function and a procedure? (from [Procedures, functions and parameters](#cs.procedures))
A: A function returns a value and is used inside an expression. A procedure does not return a value.
Q: Why does a recursive function need a base case? (from [Recursion](#cs.recursion))
A: Without a base case, the function keeps calling itself and the stack overflows. The base case answers directly and stops the calls.
:::

## Classes and objects

A record groups data. Think about a pet: it has a name and an age (data), and it can speak (behaviour). A record keeps only the data. OOP keeps both together, in one unit called an **object**.

You do not write every object separately. You write a **class** once, which describes all objects of one kind, and then create as many objects from it as you need.

:::def Class
A template that defines the attributes (data) and methods (behaviour) that every object of that kind has.
:::

:::def Object
A single item created from a class, with its own values for the attributes. An object is an **instance** of its class, and making one is called instantiation.
:::

:::def Instance
One particular object of a class. `Kito` the cat and `Zuri` the dog are two instances of classes that describe pets.
:::

:::analogy
A class is like a cookie cutter and an object is a cookie. The cutter fixes the shape; each cookie is a separate thing, and you can decorate one without changing the others. Every `Pet` object has a name and an age, but each has its own name and its own age.
:::

:::def Attribute
A data item that belongs to a class and holds part of an object's state, such as the Name of a pet. It is also called a property.
:::

:::def Method
A subroutine that belongs to a class. It is a procedure or function that works on the object's attributes.
:::

:::def Constructor
A special method that runs when an object is created and sets the starting values of its attributes. In Cambridge pseudocode it is called `NEW`; in Python it is `__init__`.
:::

### A first class in Python

Start with Python, which you can run. A class begins with `class` and a name. Inside it, each method is a function with `self` as its first parameter.

```python
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(self.name, "makes a sound")


first_pet = Pet("Kito", 3)
second_pet = Pet("Zuri", 5)
print(first_pet.name, first_pet.age)
print(second_pet.name, second_pet.age)
second_pet.speak()
```

Output:

```output
Kito 3
Zuri 5
Zuri makes a sound
```

Read it from the bottom. `Pet("Kito", 3)` creates a new object and runs `__init__` on it, so `first_pet` has the name Kito and the age 3. `Pet("Zuri", 5)` creates a second, separate object. `second_pet.speak()` calls the method `speak` on the object `second_pet`.

**`self`** means "the object this method is working on". When you call `second_pet.speak()`, Python passes `second_pet` in as `self`, so `self.name` is Zuri's name. You never write `self` when you call a method, but you must write it as the first parameter when you define one, and in front of every attribute inside the class.

### A first class in pseudocode

Cambridge pseudocode writes a class between `CLASS` and `ENDCLASS`. Each attribute and method says whether it is `PRIVATE` or `PUBLIC`. The constructor is a procedure called `NEW`.

```pseudocode
CLASS Pet
   PRIVATE Name : STRING
   PRIVATE Age : INTEGER

   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER)
      Name ← GivenName
      Age ← GivenAge
   ENDPROCEDURE

   PUBLIC FUNCTION GetName() RETURNS STRING
      RETURN Name
   ENDFUNCTION

   PUBLIC FUNCTION Speak() RETURNS STRING
      RETURN "..."
   ENDFUNCTION
ENDCLASS
```

Objects are created with `NEW` and the class name, and the values for the constructor go in brackets. A method is called with dot notation, as a record field is read.

```pseudocode
DECLARE FirstPet : Pet
DECLARE SecondPet : Pet
FirstPet ← NEW Pet("Kito", 3)
SecondPet ← NEW Pet("Zuri", 5)
OUTPUT FirstPet.GetName(), " says ", FirstPet.Speak()
OUTPUT SecondPet.GetName(), " says ", SecondPet.Speak()
```

This outputs `Kito says ...` and `Zuri says ...`. The parameters of the constructor are called `GivenName` and `GivenAge` so they are different from the attributes `Name` and `Age` that they set.

:::note How method calls are written
The Pseudocode Guide writes the call of a method with dot notation, for example `Player.SetAttempts(5)`, and writes the constructor as `PUBLIC PROCEDURE NEW(...)`. If an exam question prints its own method calls with `CALL` in front, copy the question's style. Members are public unless the code says otherwise, but state `PUBLIC` or `PRIVATE` every time in your own answers.

The guide does not show how to declare a variable that will hold an object. This course writes `DECLARE FirstPet : Pet`, using the class name as the type, as it does for a record type, and later an array whose element type is a class (`ARRAY[1:3] OF Pet`). The guide also has no keyword for overriding: a subclass simply declares a method with the same name. Both are common usage, not rules quoted from the guide; if a question shows another style, follow the question.
:::

| | Cambridge pseudocode | Python |
|---|---|---|
| define a class | `CLASS Pet` … `ENDCLASS` | `class Pet:` |
| constructor | `PUBLIC PROCEDURE NEW(…)` | `def __init__(self, …):` |
| create an object | `FirstPet ← NEW Pet("Kito", 3)` | `first_pet = Pet("Kito", 3)` |
| call a method | `FirstPet.GetName()` | `first_pet.get_name()` |
| an attribute inside a method | `Name` | `self.name` |
| private attribute | `PRIVATE Name : STRING` | `self.__name` (the convention used in this course) |

:::warn Four slips with classes
- **Forgetting `self`.** In Python every method needs `self` as its first parameter, and `self.` in front of an attribute. Without it, `name = given_name` makes an ordinary local variable that vanishes when the method ends.
- **Leaving out the brackets.** `my_pet.get_name` is the method itself, not its result. Write `my_pet.get_name()`.
- **Naming the constructor after the class in pseudocode.** The constructor is always `NEW`. `PUBLIC PROCEDURE Pet(…)` is not a constructor.
- **Forgetting that a class makes nothing.** `CLASS Pet … ENDCLASS` only describes pets, as `TYPE` only describes a record. No object exists until `NEW` creates one.
:::

## Encapsulation: private data, public methods

In the first Python program, anybody could write `first_pet.age = -400`. Nothing would stop it. In a large program, data that anyone can change anywhere is a source of bugs: you cannot tell which code broke it.

:::def Encapsulation
Keeping the attributes of an object private, so that they can be read or changed only through the object's own public methods. It protects the data and lets the class check every change.
:::

In pseudocode, `PRIVATE` makes an attribute usable only inside its own class, and `PUBLIC` makes a method usable from outside. A private attribute is reached through two kinds of public method.

:::def Getter
A public method that returns the value of a private attribute, so that other code can read it. Its name usually starts with Get.
:::

:::def Setter
A public method that sets the value of a private attribute, so that other code can change it. It can check the new value first. Its name usually starts with Set.
:::

:::key Encapsulation in a class
1. Declare every attribute `PRIVATE`.
2. Give a **getter** for each attribute that other code needs to read.
3. Give a **setter** only for an attribute that is allowed to change, and put the **validation** in the setter: reject a value that makes no sense.
4. Make the methods other code needs `PUBLIC`.
:::

Here is `Pet` with a getter for each attribute and a setter for the age, which refuses a negative age. Compared with the earlier version, it adds `GetAge` and `SetAge`.

```pseudocode
CLASS Pet
   PRIVATE Name : STRING
   PRIVATE Age : INTEGER

   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER)
      Name ← GivenName
      Age ← GivenAge
   ENDPROCEDURE

   PUBLIC FUNCTION GetName() RETURNS STRING
      RETURN Name
   ENDFUNCTION

   PUBLIC FUNCTION GetAge() RETURNS INTEGER
      RETURN Age
   ENDFUNCTION

   PUBLIC PROCEDURE SetAge(NewAge : INTEGER)
      IF NewAge >= 0 THEN
         Age ← NewAge
      ENDIF
   ENDPROCEDURE

   PUBLIC FUNCTION Speak() RETURNS STRING
      RETURN "..."
   ENDFUNCTION
ENDCLASS
```

The same class in Python. Python has no true private attributes. By convention, and in this course, an attribute whose name starts with two underscores (`self.__age`) is treated as private: Python renames it inside the class, so code outside cannot reach it by that name.

```python
class Pet:
    def __init__(self, given_name, given_age):
        self.__name = given_name
        self.__age = given_age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age

    def speak(self):
        return "..."


pet = Pet("Kito", 3)
print(pet.get_name(), pet.get_age())
pet.set_age(-5)
print(pet.get_age())
pet.set_age(4)
print(pet.get_age())
try:
    print(pet.__age)
except AttributeError:
    print("AttributeError: __age cannot be reached from outside")
```

Output:

```output
Kito 3
3
4
AttributeError: __age cannot be reached from outside
```

The setter rejected −5, so the age stayed 3. It accepted 4. The last two lines show the point of private data: `pet.__age` fails from outside the class, and the only way to read the age is `get_age()`.

:::warn Changing a private attribute from outside
In pseudocode, `FirstPet.Age ← 10` is an error when `Age` is private: only methods of the class can touch it. Write `FirstPet.SetAge(10)` instead. An exam answer that assigns to a private attribute from the main program loses the encapsulation mark.
:::

### Why bother with getters and setters?

A setter is a gatekeeper. Because every change goes through `SetAge`, a rule such as "an age is never negative" is written in one place and holds for the whole program. If the rule changes later, you change one method. A getter lets the class change how it stores the data (for example, storing a date of birth instead of an age) without breaking the code that calls `GetAge`.

A setter often has a rule beyond "not negative". It can also return a BOOLEAN that tells the caller whether the change was accepted:

```pseudocode
PUBLIC FUNCTION SetAge(NewAge : INTEGER) RETURNS BOOLEAN
   IF NewAge >= 0 THEN
      Age ← NewAge
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION
```

:::eg Writing a class with a constructor, a getter and a method (exam style)
A courier company in Quito stores each parcel's destination (a string) and mass in kilograms (a real number). A parcel is heavy if its mass is more than 20.0 kg. Write pseudocode for a class `Parcel` with private attributes, a constructor, a getter for the mass and a method `IsHeavy` that returns TRUE for a heavy parcel. Then write the statements to create a parcel for "Quito" with a mass of 23.5 and output whether it is heavy. [7 marks]

Take the parts in order: attributes, constructor, getter, the method, then the use.

```pseudocode
CLASS Parcel
   PRIVATE Destination : STRING
   PRIVATE Mass : REAL

   PUBLIC PROCEDURE NEW(GivenDestination : STRING, GivenMass : REAL)
      Destination ← GivenDestination
      Mass ← GivenMass
   ENDPROCEDURE

   PUBLIC FUNCTION GetMass() RETURNS REAL
      RETURN Mass
   ENDFUNCTION

   PUBLIC FUNCTION IsHeavy() RETURNS BOOLEAN
      RETURN Mass > 20.0
   ENDFUNCTION
ENDCLASS

DECLARE Item : Parcel
Item ← NEW Parcel("Quito", 23.5)
OUTPUT Item.IsHeavy()
```

Mark points:

- `CLASS Parcel` … `ENDCLASS` enclosing the members [B1]
- both attributes declared `PRIVATE` with correct types (STRING, REAL) [B1]
- constructor `PUBLIC PROCEDURE NEW` with two parameters [B1]
- constructor assigns both attributes from the parameters [B1]
- getter `GetMass` declared as a function that returns the mass (REAL) [B1]
- `IsHeavy` returns TRUE when Mass > 20.0 and FALSE otherwise (`RETURN Mass > 20.0` or an IF) [B1]
- creates the object with `NEW Parcel("Quito", 23.5)` and calls `IsHeavy` to output TRUE [B1]

(A REAL literal such as 20.0 needs a digit after the point. The output is TRUE because 23.5 > 20.0.)
:::

## Inheritance

A cat and a dog are both pets: both have a name and an age, and both can speak. If you write a separate `Cat` class and a separate `Dog` class, you copy the same attributes and methods twice, and a change has to be made twice.

**Inheritance** lets a new class start from an existing one.

:::def Inheritance
A mechanism in which a class takes on the attributes and methods of another class and may add its own. It reuses code and models an "is a" relationship.
:::

:::def Superclass
The class that is inherited from. It is also called the parent class or base class. Here the superclass is `Pet`.
:::

:::def Subclass
A class that inherits from another class. It is also called the child class or derived class. Here `Cat` and `Dog` are subclasses of `Pet`.
:::

The relationship is called **"is a"**: a Cat is a Pet. The subclass has everything the superclass has, plus its own extra attributes and methods.

:::html
<figure class="fig small"><svg viewBox="0 0 350 526" role="img" aria-label="A class diagram. The class Pet has private attributes Name (STRING) and Age (INTEGER) and public methods NEW, GetName, GetAge, SetAge and Speak. Below it, the class Cat has the private attribute Breed (STRING) and the public methods NEW, GetBreed and Speak, and the class Dog has the private attribute Trained (BOOLEAN) and the public methods NEW, IsTrained and Speak. A line down the left side joins Cat and Dog to an arrow that points at Pet, labelled Cat and Dog inherit from Pet."><rect class="fm s-acc sw2" x="36" y="12" width="300" height="174"/><line class="ln" x1="36" y1="40" x2="336" y2="40"/><line class="ln" x1="36" y1="86" x2="336" y2="86"/><text class="tl tb tc" x="186" y="31">Pet</text><text class="tl" x="46" y="56">− Name : STRING</text><text class="tl" x="46" y="74">− Age : INTEGER</text><text class="tl" x="46" y="102">+ NEW(GivenName, GivenAge)</text><text class="tl" x="46" y="120">+ GetName() : STRING</text><text class="tl" x="46" y="138">+ GetAge() : INTEGER</text><text class="tl" x="46" y="156">+ SetAge(NewAge : INTEGER)</text><text class="tl" x="46" y="174">+ Speak() : STRING</text><rect class="fm s-acc sw2" x="36" y="242" width="300" height="120"/><line class="ln" x1="36" y1="270" x2="336" y2="270"/><line class="ln" x1="36" y1="298" x2="336" y2="298"/><text class="tl tb tc" x="186" y="261">Cat</text><text class="tl" x="46" y="286">− Breed : STRING</text><text class="tl" x="46" y="314">+ NEW(GivenName, GivenAge, GivenBreed)</text><text class="tl" x="46" y="332">+ GetBreed() : STRING</text><text class="tl" x="46" y="350">+ Speak() : STRING</text><rect class="fm s-acc sw2" x="36" y="394" width="300" height="120"/><line class="ln" x1="36" y1="422" x2="336" y2="422"/><line class="ln" x1="36" y1="450" x2="336" y2="450"/><text class="tl tb tc" x="186" y="413">Dog</text><text class="tl" x="46" y="438">− Trained : BOOLEAN</text><text class="tl" x="46" y="466">+ NEW(GivenName, GivenAge, TrainedFlag)</text><text class="tl" x="46" y="484">+ IsTrained() : BOOLEAN</text><text class="tl" x="46" y="502">+ Speak() : STRING</text><path class="ln" d="M36,256 L12,256 L12,32 L36,32" fill="none" marker-end="url(#ah)"/><path class="ln" d="M36,408 L12,408 L12,256" fill="none"/><text class="tl" x="46" y="220">Cat and Dog inherit from Pet</text></svg><figcaption>Cat and Dog inherit from Pet: the line down the left joins both to the arrow that points at Pet. Each box has three compartments: the class name, its attributes and its methods. Cat and Dog do not repeat Name, Age, GetName, GetAge or SetAge: they inherit them.</figcaption></figure>
:::

In pseudocode, a subclass is declared with `INHERITS`. Its constructor first calls the superclass constructor with `SUPER.NEW(…)`, so the inherited attributes are set, and then sets its own attributes.

```pseudocode
CLASS Cat INHERITS Pet
   PRIVATE Breed : STRING

   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER, GivenBreed : STRING)
      SUPER.NEW(GivenName, GivenAge)
      Breed ← GivenBreed
   ENDPROCEDURE

   PUBLIC FUNCTION GetBreed() RETURNS STRING
      RETURN Breed
   ENDFUNCTION
ENDCLASS

DECLARE MyCat : Cat
MyCat ← NEW Cat("Kito", 3, "Tabby")
OUTPUT MyCat.GetName(), " is a ", MyCat.GetBreed()
```

This outputs `Kito is a Tabby`. `GetBreed` belongs to `Cat`. `GetName` is inherited from `Pet`, so a `Cat` object can use it without `Cat` repeating it.

In Python, the superclass goes in brackets after the class name, and `super().__init__(…)` runs its constructor.

```python
class Pet:
    def __init__(self, given_name, given_age):
        self.__name = given_name
        self.__age = given_age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def speak(self):
        return "..."


class Cat(Pet):
    def __init__(self, given_name, given_age, given_breed):
        super().__init__(given_name, given_age)
        self.__breed = given_breed

    def get_breed(self):
        return self.__breed

    def bad_name(self):
        return self.__name


my_cat = Cat("Kito", 3, "Tabby")
print(my_cat.get_name(), my_cat.get_age(), my_cat.get_breed())
print(isinstance(my_cat, Pet))
try:
    my_cat.bad_name()
except AttributeError:
    print("AttributeError: Cat cannot see the private Name of Pet")
```

Output:

```output
Kito 3 Tabby
True
AttributeError: Cat cannot see the private Name of Pet
```

(The `Pet` class is written out again so that this program runs by itself.) Three things happen. The cat uses `get_name()` and `get_age()`, which it inherited. `isinstance(my_cat, Pet)` is `True`: a Cat is a Pet. And `bad_name` shows that a private attribute belongs to the class that declares it: even a subclass must use the superclass's public methods (`get_name`) to reach it.

:::warn Inheritance is not for every relationship
Use inheritance only when the sentence "a Cat **is a** Pet" is true. A Library is not a kind of Book, and a Car is not a kind of Engine. For those, one object **has** the other, which is containment, shown later in this chapter. Choosing inheritance where containment fits is a common design mistake.
:::

## Polymorphism and overriding

A `Cat` says "Meow" and a `Dog` says "Woof", yet both are Pets and both have a `Speak` method. The subclass can **override** the method it inherited by declaring its own method with the same name and parameters.

:::def Overriding
Writing a method in a subclass that has the same name as a method in the superclass, so that objects of the subclass use the new version instead of the inherited one.
:::

:::def Polymorphism
The ability of objects of different classes to respond to the same method call in their own way. The same call, such as `Speak()`, can do something different for each class, and the version that runs depends on the object.
:::

In pseudocode, overriding is just a method with the same name in the subclass. The classes below extend the `Pet` and `Cat` above.

```pseudocode
CLASS Cat INHERITS Pet
   PRIVATE Breed : STRING

   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER, GivenBreed : STRING)
      SUPER.NEW(GivenName, GivenAge)
      Breed ← GivenBreed
   ENDPROCEDURE

   PUBLIC FUNCTION GetBreed() RETURNS STRING
      RETURN Breed
   ENDFUNCTION

   PUBLIC FUNCTION Speak() RETURNS STRING
      RETURN "Meow"
   ENDFUNCTION
ENDCLASS

CLASS Dog INHERITS Pet
   PRIVATE Trained : BOOLEAN

   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER, TrainedFlag : BOOLEAN)
      SUPER.NEW(GivenName, GivenAge)
      Trained ← TrainedFlag
   ENDPROCEDURE

   PUBLIC FUNCTION IsTrained() RETURNS BOOLEAN
      RETURN Trained
   ENDFUNCTION

   PUBLIC FUNCTION Speak() RETURNS STRING
      RETURN "Woof"
   ENDFUNCTION
ENDCLASS
```

Now the polymorphism. An array of type `Pet` can hold a `Cat`, a `Dog` and a plain `Pet`, because each is a Pet. One loop makes the same call on every element, and each object answers in its own way.

```pseudocode
DECLARE Pets : ARRAY[1:3] OF Pet
DECLARE Index : INTEGER
Pets[1] ← NEW Cat("Kito", 3, "Tabby")
Pets[2] ← NEW Dog("Rex", 5, TRUE)
Pets[3] ← NEW Pet("Zuri", 2)
FOR Index ← 1 TO 3
   OUTPUT Pets[Index].GetName(), " says ", Pets[Index].Speak()
NEXT Index
```

The output is `Kito says Meow`, `Rex says Woof` and `Zuri says ...`. The loop does not test the class of each pet: that is the benefit. A new subclass, such as a `Rabbit`, would work in the same loop without changing it.

In Python the same idea is written like this. Each class that overrides `speak` simply defines its own:

```python
class Pet:
    def __init__(self, given_name, given_age):
        self.__name = given_name
        self.__age = given_age

    def get_name(self):
        return self.__name

    def speak(self):
        return "..."


class Cat(Pet):
    def __init__(self, given_name, given_age, given_breed):
        super().__init__(given_name, given_age)
        self.__breed = given_breed

    def speak(self):
        return "Meow"


class Dog(Pet):
    def __init__(self, given_name, given_age, trained_flag):
        super().__init__(given_name, given_age)
        self.__trained = trained_flag

    def speak(self):
        return "Woof"


pets = [Cat("Kito", 3, "Tabby"), Dog("Rex", 5, True), Pet("Zuri", 2)]
for animal in pets:
    print(animal.get_name(), "says", animal.speak())
```

Output:

```output
Kito says Meow
Rex says Woof
Zuri says ...
```

:::key Overriding and polymorphism
- A subclass **overrides** a method by defining one with the **same name** and parameters as the superclass.
- **Polymorphism**: one call on objects of different classes, each class giving its own result. It is why a list of mixed objects can be processed by one loop.
- The superclass's constructor is reached with `SUPER.NEW(…)` in pseudocode and `super().__init__(…)` in Python.
:::

:::exam Explain, do not just define
"Explain what is meant by polymorphism" gets the mark for the idea that the same method call produces different behaviour for objects of different classes, and a second mark for an example (a `Speak` method that gives `"Meow"` for a Cat and `"Woof"` for a Dog). Name the method and the classes; a bare definition is not enough.
:::

## Containment (aggregation)

Some relationships are not "is a" but "has a". A library **has** books. A car **has** an engine. A playlist **has** songs. In OOP, one object has another object as one of its attributes. This is containment.

:::def Containment (aggregation)
A relationship in which an object of one class has, as one of its attributes, one or more objects of another class. It models a "has a" relationship, and the contained objects exist as objects in their own right.
:::

| | Inheritance | Containment |
|---|---|---|
| Relationship | "is a" | "has a" |
| Example | a Cat **is a** Pet | a Library **has** Books |
| How it is written | `CLASS Cat INHERITS Pet` | an attribute whose type is another class |
| What is shared | the attributes and methods of the superclass | nothing is inherited; the object calls the other object's methods |

:::html
<figure class="fig small"><svg viewBox="0 0 300 402" role="img" aria-label="A class diagram showing containment. The class Library has private attributes Name (STRING) and Books (an array of Book) and public methods NEW, AddBook and CountOnLoan. Below it, the class Book has private attributes Title, Author and OnLoan and public methods NEW, GetTitle, IsOnLoan and Borrow. A line with a diamond at the Library end, labelled contains many, joins Library to Book: a Library contains many Books."><rect class="fm s-acc sw2" x="25" y="12" width="250" height="138"/><line class="ln" x1="25" y1="40" x2="275" y2="40"/><line class="ln" x1="25" y1="86" x2="275" y2="86"/><text class="tl tb tc" x="150" y="31">Library</text><text class="tl" x="35" y="56">− Name : STRING</text><text class="tl" x="35" y="74">− Books : ARRAY OF Book</text><text class="tl" x="35" y="102">+ NEW(GivenName)</text><text class="tl" x="35" y="120">+ AddBook(NewBook : Book)</text><text class="tl" x="35" y="138">+ CountOnLoan() : INTEGER</text><rect class="fm s-acc sw2" x="25" y="216" width="250" height="174"/><line class="ln" x1="25" y1="244" x2="275" y2="244"/><line class="ln" x1="25" y1="308" x2="275" y2="308"/><text class="tl tb tc" x="150" y="235">Book</text><text class="tl" x="35" y="260">− Title : STRING</text><text class="tl" x="35" y="278">− Author : STRING</text><text class="tl" x="35" y="296">− OnLoan : BOOLEAN</text><text class="tl" x="35" y="324">+ NEW(GivenTitle, GivenAuthor)</text><text class="tl" x="35" y="342">+ GetTitle() : STRING</text><text class="tl" x="35" y="360">+ IsOnLoan() : BOOLEAN</text><text class="tl" x="35" y="378">+ Borrow() : BOOLEAN</text><line class="ln" x1="150" y1="174" x2="150" y2="216"/><polygon class="fp s-acc sw2" points="150,150 158,162 150,174 142,162"/><text class="tl halo" x="162" y="200">contains many</text></svg><figcaption>A Library contains many Books. The diamond sits at the Library end of the line, the class that holds the others. Library does not inherit from Book.</figcaption></figure>
:::

In pseudocode, the Library holds its books in an array whose element type is `Book`. The class `Book` must be written first, with its own getters and a `Borrow` method.

```pseudocode
CLASS Book
   PRIVATE Title : STRING
   PRIVATE Author : STRING
   PRIVATE OnLoan : BOOLEAN

   PUBLIC PROCEDURE NEW(GivenTitle : STRING, GivenAuthor : STRING)
      Title ← GivenTitle
      Author ← GivenAuthor
      OnLoan ← FALSE
   ENDPROCEDURE

   PUBLIC FUNCTION GetTitle() RETURNS STRING
      RETURN Title
   ENDFUNCTION

   PUBLIC FUNCTION IsOnLoan() RETURNS BOOLEAN
      RETURN OnLoan
   ENDFUNCTION

   PUBLIC FUNCTION Borrow() RETURNS BOOLEAN
      IF OnLoan THEN
         RETURN FALSE
      ELSE
         OnLoan ← TRUE
         RETURN TRUE
      ENDIF
   ENDFUNCTION
ENDCLASS

CLASS Library
   PRIVATE Name : STRING
   PRIVATE Books : ARRAY[1:50] OF Book
   PRIVATE BookCount : INTEGER

   PUBLIC PROCEDURE NEW(GivenName : STRING)
      Name ← GivenName
      BookCount ← 0
   ENDPROCEDURE

   PUBLIC PROCEDURE AddBook(NewBook : Book)
      BookCount ← BookCount + 1
      Books[BookCount] ← NewBook
   ENDPROCEDURE

   PUBLIC FUNCTION CountOnLoan() RETURNS INTEGER
      DECLARE Total, Index : INTEGER
      Total ← 0
      FOR Index ← 1 TO BookCount
         IF Books[Index].IsOnLoan() THEN
            Total ← Total + 1
         ENDIF
      NEXT Index
      RETURN Total
   ENDFUNCTION
ENDCLASS
```

The method `CountOnLoan` asks each `Book` object whether it is on loan: the Library does not touch a book's private `OnLoan` itself. That is encapsulation and containment working together. The same design in Python, with a list for the books:

```python
class Book:
    def __init__(self, given_title, given_author):
        self.__title = given_title
        self.__author = given_author
        self.__on_loan = False

    def get_title(self):
        return self.__title

    def is_on_loan(self):
        return self.__on_loan

    def borrow(self):
        if self.__on_loan:
            return False
        self.__on_loan = True
        return True


class Library:
    def __init__(self, given_name):
        self.__name = given_name
        self.__books = []

    def add_book(self, new_book):
        self.__books.append(new_book)

    def count_on_loan(self):
        total = 0
        for book in self.__books:
            if book.is_on_loan():
                total = total + 1
        return total

    def borrow_title(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book.borrow()
        return False


school = Library("Kumasi School Library")
school.add_book(Book("Rivers of the World", "N. Okafor"))
school.add_book(Book("Starting with Python", "L. Mendes"))
school.add_book(Book("The Night Sky", "R. Iqbal"))
print(school.borrow_title("The Night Sky"))
print(school.borrow_title("The Night Sky"))
print(school.borrow_title("Missing Book"))
print(school.count_on_loan())
```

Output:

```output
True
False
False
1
```

The first request succeeds. The second returns `False` because the book is already on loan. The third returns `False` because no such title exists. Only one book is on loan.

## Class diagrams

A **class diagram** shows the classes of a program and how they relate, without any code. Each class is a box with three compartments.

:::key Reading a class diagram
1. **Top compartment:** the class name.
2. **Middle compartment:** the attributes, each with its data type (`Name : STRING`).
3. **Bottom compartment:** the methods, with their parameters and the type they return (`GetAge() : INTEGER`).
4. An arrow from a subclass to its superclass shows **inheritance**.
5. A line with a diamond at one end shows **containment**: the diamond is at the class that contains the others.
6. This course draws `−` before a private member and `+` before a public one. Cambridge's own class diagrams often leave out the `−` and `+`, list getters without a return type (`GetPetName()`) and may show the constructor as `Constructor()` (9618/31 November 2024 mark scheme). Follow the style of the diagram the question prints.
:::

The first diagram in this chapter has `Pet` at the top and an arrow that points at it from `Cat` and `Dog`. Read it by walking down: `Cat` has everything `Pet` has, plus `Breed` and `GetBreed`. The second diagram has no arrow, because neither class inherits from the other. They are joined by the containment line.

To **draw** a class diagram from a description, find the class name, then list the data (attributes) with a type for each, then list the actions (methods). A constructor and getters are normally included.

:::eg Completing a class diagram from a description
A class `Parcel` stores the destination (a string) and the mass in kilograms (a real number). It has a constructor, a getter for the mass and a method `IsHeavy` that returns TRUE or FALSE. Complete its class diagram. [4 marks]

| Parcel |
|---|
| attributes: − Destination : STRING, − Mass : REAL |
| methods: + NEW(GivenDestination : STRING, GivenMass : REAL), + GetMass() : REAL, + IsHeavy() : BOOLEAN |

The class name `Parcel` in the top compartment [B1]. Both attributes with the correct types, STRING and REAL, in the middle compartment [B1]. The constructor, with its two parameters, and the getter in the bottom compartment [B1]. `IsHeavy` with the return type BOOLEAN [B1].
:::

## Designing classes from a scenario

A programming task usually begins with a description, not with code. A reliable way to find the classes is to read the description for nouns and verbs.

:::steps
1. **Underline the nouns.** Each important thing the program stores is a candidate **class**: member, coach, session.
2. **Find the data each noun has.** These become its **attributes**, each with a data type.
3. **Underline the verbs.** What can each thing do, or what is done to it? These become **methods**.
4. **Look for "is a".** Two classes that share attributes and methods may share a **superclass**.
5. **Look for "has a".** An object that holds other objects uses **containment**.
6. **Make the attributes private**, add getters and setters where needed, and give each class a constructor.
:::

:::eg Designing the classes for a sports club
A sports club in Santiago needs a program to manage its training sessions. Every person, a member or a coach, has a name. A member also has a membership number. A coach also has a speciality, such as swimming. A session has a day, a start time, a limit on the number of places, one coach and a list of the members who have booked. A member can book a place in a session. Identify the classes, give each class suitable attributes and methods, and name the relationships. [8 marks]

Underline the nouns: person, member, coach, session, name, membership number, speciality, day, start time, places. Member and Coach both have a name, which is shared data, so they can inherit from a superclass `Person`. A Session holds one coach and a list of members, which is containment.

| Class | Attributes | Methods |
|---|---|---|
| Person | Name : STRING | NEW, GetName |
| Member (inherits Person) | MembershipNumber : STRING | NEW, GetMembershipNumber |
| Coach (inherits Person) | Speciality : STRING | NEW, GetSpeciality |
| Session | Day : STRING, StartTime : STRING, Places : INTEGER, SessionCoach : Coach, Booked : ARRAY OF Member | NEW, Book(Participant : Member) : BOOLEAN, PlacesLeft() : INTEGER |

Relationships: Member and Coach **inherit** from Person (a member is a person) [B1] [B1]. Session **contains** one Coach and many Members (a session has a coach and has members) [B1] [B1]. Classes identified: Person, Member, Coach and Session [B1]. Suitable private attributes for each with a data type [B1]. A method `Book` that adds a member if there are places left [B1]. A getter or `PlacesLeft` method [B1].

The membership number is a STRING because it is an identifier, as in [Data types, records and arrays](#cs.datatypes). `Book` returns a BOOLEAN so the caller can tell whether the member got a place.
:::

## A complete task: Paper 4 style

Paper 4 gives you a scenario, supplied data files and several parts, and asks you to save your program and paste the code and a screenshot of the output into an evidence document. A task with a parent class, subclasses, overriding, a file and a list of objects is typical. Here is one, built in four parts.

First, the data file. In the exam it is supplied; to run this program yourself, create it with this code.

```python
rows = ["C,GH-2041-27,Hatchback,60,4",
        "C,GH-5530-26,Saloon,75,5",
        "V,GH-1188-25,Panel van,90,1200",
        "V,GH-7720-27,Pickup,85,800",
        "C,GH-3094-27,Estate,80,7"]
file = open("vehicles.txt", "w")
for row in rows:
    file.write(row + "\n")
file.close()
```

The file `vehicles.txt` then contains one vehicle per line:

```text
C,GH-2041-27,Hatchback,60,4
C,GH-5530-26,Saloon,75,5
V,GH-1188-25,Panel van,90,1200
V,GH-7720-27,Pickup,85,800
C,GH-3094-27,Estate,80,7
```

:::eg Vehicle hire (Paper 4 style)
A vehicle hire company in Accra stores its vehicles in the text file `vehicles.txt`. Each line has five fields separated by commas: the type (`C` for a car, `V` for a van), the registration, the model, the daily rate in Ghana cedis (a whole number), and the last field, which is the number of seats for a car or the maximum load in kilograms for a van. [20 marks]

(a) Write a class `Vehicle` with private attributes for the registration, model and daily rate, a constructor, getters, a method `get_cost(days)` that returns the daily rate multiplied by the number of days, and a method `describe` that returns the registration and the model, separated by a space. [5]

(b) Write a class `Car` that inherits from `Vehicle`, with a private attribute for the number of seats, whose `describe` adds the seats. Write a class `Van` that inherits from `Vehicle`, with a private attribute for the maximum load in kilograms, whose `describe` adds the load, and whose `get_cost` adds a fixed loading charge of 100 to the cost of the hire. [7]

(c) Write code that reads the file, creates a `Car` or a `Van` object for each line and stores the objects in a list. [5]

(d) Output the description and the cost of a 5-day hire for every vehicle in the list, then the total cost of all of them. [3]

One program answers all four parts. Comments mark each part.

```python
class Vehicle:  # (a) the superclass
    def __init__(self, registration, model, daily_rate):
        self.__registration = registration
        self.__model = model
        self.__daily_rate = daily_rate

    def get_registration(self):
        return self.__registration

    def get_model(self):
        return self.__model

    def get_daily_rate(self):
        return self.__daily_rate

    def get_cost(self, days):
        return self.__daily_rate * days

    def describe(self):
        return self.__registration + " " + self.__model


class Car(Vehicle):  # (b) the subclasses
    def __init__(self, registration, model, daily_rate, seats):
        super().__init__(registration, model, daily_rate)
        self.__seats = seats

    def describe(self):
        return super().describe() + ", " + str(self.__seats) + " seats"


class Van(Vehicle):
    def __init__(self, registration, model, daily_rate, load_kg):
        super().__init__(registration, model, daily_rate)
        self.__load_kg = load_kg

    def get_cost(self, days):
        return super().get_cost(days) + 100

    def describe(self):
        return super().describe() + ", load " + str(self.__load_kg) + " kg"


fleet = []  # (c) read the file and create the objects
file = open("vehicles.txt", "r")
for line in file:
    parts = line.strip().split(",")
    if parts[0] == "C":
        fleet.append(Car(parts[1], parts[2], int(parts[3]), int(parts[4])))
    else:
        fleet.append(Van(parts[1], parts[2], int(parts[3]), int(parts[4])))
file.close()

DAYS = 5  # (d) output the costs
total = 0
for vehicle in fleet:
    cost = vehicle.get_cost(DAYS)
    total = total + cost
    print(vehicle.describe() + ":", cost)
print("Total for", DAYS, "days:", total)
```

Output:

```output
GH-2041-27 Hatchback, 4 seats: 300
GH-5530-26 Saloon, 5 seats: 375
GH-1188-25 Panel van, load 1200 kg: 550
GH-7720-27 Pickup, load 800 kg: 525
GH-3094-27 Estate, 7 seats: 400
Total for 5 days: 2150
```

Mark points:

- `class Vehicle` with a constructor storing the registration, model and daily rate as private attributes [B1] [B1]
- getters for the private attributes [B1]
- `get_cost` returns the daily rate multiplied by the days [B1]
- `describe` returns the registration, a space and the model [B1]
- `class Car(Vehicle)` whose constructor calls `super().__init__` with the three values [B1]
- Car stores the seats as a private attribute [B1]
- Car overrides `describe` to add the seats [B1]
- `class Van(Vehicle)` whose constructor calls `super().__init__` and stores the load as a private attribute [B1]
- Van overrides `describe` to add the load [B1]
- Van overrides `get_cost` [B1]
- the Van version adds 100 to the cost from the superclass (`super().get_cost(days) + 100`) [B1]
- opens the file for reading and closes it [B1]
- reads each line, removes the end of line and splits it at the commas [B1]
- uses the first field to choose between creating a `Car` and a `Van` [B1]
- converts the rate and the last field to integers [B1]
- appends each object to a list [B1]
- loops through the list and calls `get_cost(5)` and `describe()` for each object [B1]
- keeps a running total of the costs and outputs it after the loop [B1]
- output matches the one shown, with the costs 300, 375, 550, 525, 400 and the total 2150 [B1]

(Accept the registration, model and rate stored under other names. An answer that tests the class of each object before calling `get_cost` still works, but loses the polymorphism the task is about. A van cost of 450 instead of 550 means the loading charge of 100 was left out.)
:::

Notice how the loop in part (d) is polymorphic: `vehicle.get_cost(DAYS)` is the same call for every object, and a `Van` adds its loading charge by itself. The last step in a Paper 4 task is testing. A good test is to compare the program's output with a hand calculation. The hatchback costs \(60 \times 5 = 300\) and the panel van costs \(90 \times 5 + 100 = 550\), and both agree with the output. A test table is a good habit:

| Test | Expected | Shown |
|---|---|---|
| 5-day cost of a car with rate 60 | 300 | 300 |
| 5-day cost of a van with rate 90 | 550 | 550 |
| total for all five vehicles | 2150 | 2150 |

### Two names, one object (Python)

:::warn A Python variable is a reference
A Python variable holds a reference to an object, not a copy of it. After `second = first`, both names refer to the **same** object, so a change made through one is visible through the other.
:::

This program shows it:

```python
class Counter:
    def __init__(self):
        self.count = 0


first = Counter()
second = first
second.count = 5
print(first.count)
third = Counter()
print(third.count)
```

Output:

```output
5
0
```

`first` and `second` are the same object, so `first.count` is 5. `Counter()` made a new object, `third`, with its own count of 0. To get a separate object you must create one with the constructor.

## Common mistakes and exam technique

:::warn Slips that cost marks
- **Making attributes public.** A class whose attributes are not `PRIVATE`, or code that changes a private attribute directly, loses the encapsulation marks.
- **Setters without validation** when the question asks for a rule (for example a negative age). The check belongs inside the setter.
- **Inheritance used for "has a".** A Library that `INHERITS Book` is wrong. Use an attribute that holds the books.
- **Calling `SUPER.NEW` in the wrong place or forgetting it.** The subclass constructor must call the superclass constructor to set the inherited attributes.
- **Mixing up class and object.** `Pet` is a class; `FirstPet` is an object. Methods are called on objects, not on the class name.
:::

:::exam Writing OOP answers
- Write the class in the order: attributes (with `PRIVATE`), constructor, getters, setters, other methods.
- Give every method its parameters and its return type in a function header (`RETURNS INTEGER`).
- When you create objects, use `NEW` and assign to a variable you have declared.
- In a design question, name each class, give its attributes with types, give its methods, and say whether each relationship is "is a" (inheritance) or "has a" (containment).
- Use the terms exactly: attribute, method, constructor, getter, setter, superclass, subclass, overriding.
:::

:::eg Spot the error: a constructor with the wrong name
Question: Write pseudocode for a class `Ticket` with private attributes `Price` (REAL) and `Seat` (STRING), a constructor that sets both, a getter for the price, and a setter `SetPrice` that does not allow a negative price. [4 marks]

A student wrote:

```pseudocode
01  CLASS Ticket
02     PRIVATE Price : REAL
03     PRIVATE Seat : STRING
04     PUBLIC PROCEDURE Ticket(GivenPrice : REAL, GivenSeat : STRING)
05        Price ← GivenPrice
06        Seat ← GivenSeat
07     ENDPROCEDURE
08     PUBLIC FUNCTION GetPrice() RETURNS REAL
09        RETURN Price
10     ENDFUNCTION
11     PUBLIC PROCEDURE SetPrice(NewPrice : REAL)
12        IF NewPrice >= 0.0 THEN
13           Price ← NewPrice
14        ENDIF
15     ENDPROCEDURE
16  ENDCLASS
```

Lines 02 and 03 declare both attributes `PRIVATE` with the right types [B1]. **Line 04 names the constructor `Ticket`. In Cambridge pseudocode the constructor of every class is called `NEW`, so this is an ordinary procedure and `NEW Ticket(…)` would fail. The constructor mark is lost** [B0]. The getter on lines 08 to 10 returns the price [B1]. The setter on lines 11 to 15 checks that the price is not negative before changing it [B1]. The answer scores 3 out of 4.

The corrected line is `PUBLIC PROCEDURE NEW(GivenPrice : REAL, GivenSeat : STRING)`. The habit of naming the constructor after the class comes from other languages, and it is the most common slip in this topic.
:::

:::try Start easy, finish at exam standard
Q: A class `Book` has the attributes Title and Author and the method `GetTitle`. Say which of these is the class, an attribute and a method, and describe what an object of the class is.
A: `Book` is the class. Title and Author are attributes. `GetTitle` is a method. An object of the class is one particular book, such as the book with the title "The Night Sky", with its own values for Title and Author.
Q: In Python, write the statement that creates a `Pet` object for a pet called "Mina" aged 2 and stores it in `my_pet`, then the statement that outputs the result of calling `speak` on it.
A: `my_pet = Pet("Mina", 2)` creates the object and runs the constructor. `print(my_pet.speak())` calls the method, with brackets, and outputs the result.
Q: What does `self` refer to inside a method?
A: The object on which the method was called, so `self.name` is the name of that object.
Q: Why should the attributes of a class be private?
A: Other code can then change them only through the class's methods, so the class can check every change (validation) and the data cannot be set to a wrong value by accident. It also lets the class change how it stores data without breaking other code.
Q: `CLASS Cat INHERITS Pet`. Name the superclass and the subclass, and say what a Cat object inherits.
A: `Pet` is the superclass and `Cat` is the subclass. A Cat object inherits the attributes and methods of Pet, such as `GetName`.
Q: For each pair, say whether the relationship is "is a" (inheritance) or "has a" (containment): a car and an engine; a teacher and a person; a school and its classrooms.
A: A car has an engine: containment. A teacher is a person: inheritance. A school has classrooms: containment.
Q: Write the pseudocode header line of a public getter `GetAge` for a private INTEGER attribute `Age`.
A: `PUBLIC FUNCTION GetAge() RETURNS INTEGER`, followed by `RETURN Age` and `ENDFUNCTION`.
Q: A student writes `print(my_pet.get_name)` in Python and gets a strange message about a method instead of the name. What is the mistake?
A: The brackets are missing. `my_pet.get_name` is the method itself; `my_pet.get_name()` calls it and gives the name.
Q: Write the class header in Python for a class `Rabbit` that inherits from `Pet`, and say what a Rabbit needs to write if it should answer "Squeak" to `speak`.
A: `class Rabbit(Pet):`. It overrides `speak`: it defines a method `speak` that returns "Squeak". It inherits the rest of Pet.
Q: A class `Speaker` has a private INTEGER attribute `Volume`. Write pseudocode for a setter `SetVolume` that accepts only values from 0 to 10 inclusive.
A: Use IF to check both limits before the assignment.

```pseudocode
PUBLIC PROCEDURE SetVolume(NewVolume : INTEGER)
   IF NewVolume >= 0 AND NewVolume <= 10 THEN
      Volume ← NewVolume
   ENDIF
ENDPROCEDURE
```
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ (a) State the difference between a class and an object. [2] (b) State what is meant by encapsulation. [2]
A: Two marks for each part.

- a class is a template (definition) that describes the attributes and methods of all objects of that kind [B1]
- an object is one instance of a class, created from it, with its own values for the attributes [B1]
- encapsulation is keeping the attributes private, so they are accessed only through the object's methods [B1]
- this protects the data: the methods (setters) can validate every change [B1]

Q: [4 marks] ★★ A music app stores each song's title (a string), the artist (a string) and the length in seconds (an integer). A song is long if it lasts more than 300 seconds. Complete the class diagram for a class `Song`, giving the attributes and the methods, which must include a constructor, getters for all three attributes and a method `IsLong`. (Write the three compartments as a list.)
H: Three compartments: the name, the attributes with types, the methods with return types.
H: How does `IsLong` report its answer?
A: One possible answer:

| Song |
|---|
| attributes: − Title : STRING, − Artist : STRING, − Length : INTEGER |
| methods: + NEW(GivenTitle : STRING, GivenArtist : STRING, GivenLength : INTEGER), + GetTitle() : STRING, + GetArtist() : STRING, + GetLength() : INTEGER, + IsLong() : BOOLEAN |

- class name `Song` [B1]
- three attributes with the correct types (STRING, STRING, INTEGER) [B1]
- constructor and the three getters, with return types [B1]
- `IsLong` with the return type BOOLEAN [B1]

Q: [6 marks] ★★ A bank in Lima stores each account's holder (a string) and balance (a real number). Write pseudocode for a class `Account` with private attributes, a constructor, a getter `GetBalance`, and a method `Deposit(Amount : REAL)` that adds the amount to the balance only if the amount is greater than 0.0.
H: Attributes first (`PRIVATE`), then the constructor `NEW`, then the getter, then `Deposit`.
H: The check goes inside `Deposit`, before the balance changes.
A: One possible answer:

```pseudocode
CLASS Account
   PRIVATE Holder : STRING
   PRIVATE Balance : REAL

   PUBLIC PROCEDURE NEW(GivenHolder : STRING, GivenBalance : REAL)
      Holder ← GivenHolder
      Balance ← GivenBalance
   ENDPROCEDURE

   PUBLIC FUNCTION GetBalance() RETURNS REAL
      RETURN Balance
   ENDFUNCTION

   PUBLIC PROCEDURE Deposit(Amount : REAL)
      IF Amount > 0.0 THEN
         Balance ← Balance + Amount
      ENDIF
   ENDPROCEDURE
ENDCLASS
```

- `CLASS Account` … `ENDCLASS` [B1]
- both attributes `PRIVATE` with the correct types [B1]
- constructor `NEW` that sets both attributes from its parameters [B1]
- `GetBalance` returns the balance with a REAL return type [B1]
- `Deposit` tests that `Amount > 0.0` [B1]
- adds the amount to the balance only when the test is true [B1]

(After `Deposit(50.0)` on an account that starts with 20.0, `GetBalance` returns 70.0. After `Deposit(-5.0)` the balance is unchanged.)

Q: [5 marks] ★★ A school stores every person's name. A `Student` is a person who also has a form (a string, for example "10B"). The class `Person` is already written, with a private attribute `Name`, a constructor `NEW(GivenName : STRING)` and a getter `GetName`. Write pseudocode for the class `Student` that inherits from `Person`, with a constructor that takes the name and the form, and a getter `GetForm`.
H: The header needs `INHERITS`.
H: Set the inherited attribute by calling the superclass constructor first.
A: One possible answer:

```pseudocode
CLASS Student INHERITS Person
   PRIVATE Form : STRING

   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenForm : STRING)
      SUPER.NEW(GivenName)
      Form ← GivenForm
   ENDPROCEDURE

   PUBLIC FUNCTION GetForm() RETURNS STRING
      RETURN Form
   ENDFUNCTION
ENDCLASS
```

- `CLASS Student INHERITS Person` [B1]
- private attribute `Form` of type STRING [B1]
- constructor `NEW` with two parameters [B1]
- calls `SUPER.NEW(GivenName)` to set the name [B1]
- assigns `Form` and provides the getter `GetForm` [B1]

Q: [3 marks] ★★ A music app has a class `Playlist` and a class `Song`. A programmer says that `Playlist` should inherit from `Song`. Explain why this is wrong and which relationship should be used.
A: One mark each:

- inheritance is an "is a" relationship, and a playlist is not a kind of song [B1]
- a playlist **has** songs, so the relationship is containment (aggregation) [B1]
- the `Playlist` class should have an attribute holding a collection of `Song` objects (for example an array or list), with a method to add a song [B1]

Q: [10 marks] ★★★ A geometry program stores shapes. Write Python code for a class `Shape` with a private name, a constructor, a getter `get_name` and a method `area` that returns 0. Write a class `Rectangle` that inherits from `Shape`, with a private width and height, whose `area` returns the width multiplied by the height. Write a class `Square` that inherits from `Shape`, with a private side, whose `area` returns the side multiplied by itself. Create a list with a rectangle of width 7 and height 4 and a square of side 5, and output the name and the area of each shape. State the output.
H: Both subclasses call `super().__init__(name)` to set the name.
H: The loop calls `area()` on each element; it should not test which class the object belongs to.
H: Rectangle: 7 × 4. Square: 5 × 5.
A: One possible answer:

```python
class Shape:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.__side = side

    def area(self):
        return self.__side * self.__side


shapes = [Rectangle(7, 4), Square(5)]
for shape in shapes:
    print(shape.get_name(), shape.area())
```

```output
Rectangle 28
Square 25
```

- `Shape` has a private name set by its constructor [B1]
- `get_name` returns the name [B1]
- `Shape.area` returns 0 [B1]
- `class Rectangle(Shape)` whose constructor calls `super().__init__` and stores the width and height [B1]
- `Rectangle.area` overrides the method and returns width × height [B1]
- `class Square(Shape)` with a constructor that calls `super().__init__` and stores the side [B1]
- `Square.area` overrides the method and returns side × side [B1]
- a list holding a `Rectangle(7, 4)` and a `Square(5)` [B1]
- one loop that calls `area()` and `get_name()` on every shape without testing its class [B1]
- the output `Rectangle 28` and `Square 25` [B1]

Q: [4 marks] ★★ The class below is called by the program that follows it. Give the output and explain the second value.

```pseudocode
CLASS Thermostat
   PRIVATE Target : INTEGER

   PUBLIC PROCEDURE NEW(GivenTarget : INTEGER)
      Target ← GivenTarget
   ENDPROCEDURE

   PUBLIC FUNCTION GetTarget() RETURNS INTEGER
      RETURN Target
   ENDFUNCTION

   PUBLIC PROCEDURE SetTarget(NewTarget : INTEGER)
      IF NewTarget >= 10 AND NewTarget <= 30 THEN
         Target ← NewTarget
      ENDIF
   ENDPROCEDURE
ENDCLASS

DECLARE Room : Thermostat
Room ← NEW Thermostat(20)
Room.SetTarget(35)
OUTPUT Room.GetTarget()
Room.SetTarget(18)
OUTPUT Room.GetTarget()
Room.SetTarget(5)
OUTPUT Room.GetTarget()
```

H: Check each call of `SetTarget` against the range 10 to 30.
A: The output is 20, 18 and 18.

- the first output is 20, because 35 is outside the range 10 to 30 and the setter rejects it [B1]
- the second output is 18, because 18 is inside the range and the target is changed [B1]
- the third output is 18, because 5 is outside the range, so the target keeps its last accepted value [B1]
- the validation inside the setter is what protects the private attribute [B1]

Q: [8 marks] ★★★ A bus company in Lima wants a program to record its journeys. A bus has a registration number and a seating capacity. A driver has a name and a licence number. A journey has a route name, a date, one bus, one driver and a list of the passengers' names. Design the classes. For each class, give its name and two attributes, and one method. Then, for the Journey class, state which classes it contains and explain why this is containment and not inheritance.
H: Underline the nouns for the classes and the data. Journey holds other objects.
A: One possible answer:

| Class | Attributes | Method |
|---|---|---|
| Bus | Registration : STRING, Capacity : INTEGER | GetCapacity() : INTEGER |
| Driver | Name : STRING, LicenceNumber : STRING | GetName() : STRING |
| Journey | RouteName : STRING, JourneyDate : DATE, JourneyBus : Bus, JourneyDriver : Driver, Passengers : ARRAY OF STRING | AddPassenger(PassengerName : STRING) : BOOLEAN |

- classes Bus, Driver and Journey identified [B1]
- two suitable private attributes for Bus, with data types [B1]
- two suitable private attributes for Driver, with data types [B1]
- Journey has suitable attributes with data types, including a Bus and a Driver [B1]
- a suitable method for each class (for example a getter, or `AddPassenger`) [B1]
- Journey contains a Bus object and a Driver object (and the passengers) [B1]
- a journey **has** a bus and a driver; it is not a kind of bus or driver, so the relationship is "has a" (containment), not "is a" [B1]
- attributes private and accessed through methods (encapsulation) [B1]

(Accept other reasonable attributes and names. `AddPassenger` should refuse a passenger when the bus is full, using `Capacity`.)
:::

:::try Stretch for A*
Q: [8 marks] ★★★ A tree is made of nodes. Paper 4 asks for classes `Node` and `Tree` that store whole numbers in a binary search tree. `Node` holds a value and two private attributes `left` and `right` for its sub-trees, each either another `Node` or `None`. `Node` has a recursive method `add(value)`, which places the value in the left sub-tree if it is smaller than the node's value and otherwise in the right, creating a new `Node` where the place is empty, and a recursive method `in_order(result)` that appends the values to a list in ascending order. `Tree` has a private root, a method `add(value)` and a method `in_order()` that returns the list. Write the classes, add the values 8, 3, 10, 1 and 6 in that order, and output the result of `in_order()`. This question joins [Recursion](#cs.recursion) and OOP.
H: A new `Node` is created when the place where the value belongs is `None`. Otherwise the method calls itself on that sub-tree.
H: The tree's own `add` has a special case: if the root is `None`, the new node becomes the root.
H: In-order: left sub-tree, then the node's value, then the right sub-tree. The base case is a missing sub-tree.
A: One possible answer:

```python
class Node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    def add(self, value):
        if value < self.__value:
            if self.__left is None:
                self.__left = Node(value)
            else:
                self.__left.add(value)
        else:
            if self.__right is None:
                self.__right = Node(value)
            else:
                self.__right.add(value)

    def in_order(self, result):
        if self.__left is not None:
            self.__left.in_order(result)
        result.append(self.__value)
        if self.__right is not None:
            self.__right.in_order(result)


class Tree:
    def __init__(self):
        self.__root = None

    def add(self, value):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__root.add(value)

    def in_order(self):
        result = []
        if self.__root is not None:
            self.__root.in_order(result)
        return result


tree = Tree()
for value in (8, 3, 10, 1, 6):
    tree.add(value)
print(tree.in_order())
```

```output
[1, 3, 6, 8, 10]
```

- `Node` with a constructor and private value, left and right (the sub-trees start as `None`) [B1]
- `Node.add` compares the value and chooses the left or the right sub-tree [B1]
- creates a new `Node` when the chosen sub-tree is `None` [B1]
- otherwise calls `add` recursively on that sub-tree [B1]
- `Node.in_order` calls itself on the left sub-tree, appends its own value, then calls itself on the right sub-tree [B1]
- `Tree` with a private root that starts as `None`, and `add` that creates the root node or calls `Node.add` [B1]
- `Tree.in_order` creates a list, starts the traversal only if there is a root, and returns the list [B1]
- the output `[1, 3, 6, 8, 10]` [B1]

(Each `Node` has the same shape as the whole tree, which is why the methods are recursive. The base case of `in_order` is a sub-tree that is `None`: the method is never called on it.)

Q: [7 marks] ★★★ A bank has two kinds of account. Every account has a private balance and a method `withdraw(amount)` that returns `True` and reduces the balance if the account can pay, and otherwise returns `False` and leaves the balance unchanged. A `SavingsAccount` can pay only if the balance is at least the amount. A `CurrentAccount` has an overdraft limit and can pay if the balance minus the amount is not below minus the limit. Write Python classes `Account`, `SavingsAccount` and `CurrentAccount` that give this behaviour, with `Account` holding the balance and the shared getter, and the subclasses overriding a method `can_pay(amount)` that `withdraw` uses. Test them with a savings account of 100 and a current account of 100 with an overdraft limit of 50, each asked to withdraw 120, and state the results.
H: `withdraw` is written once in `Account`. It calls `self.can_pay(amount)`, and each subclass answers differently: that is polymorphism.
H: The balance is private to `Account`, so the subclasses reach it through `get_balance()`.
H: Current account: 100 − 120 = −20, which is not below −50.
A: One possible answer:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def can_pay(self, amount):
        return False

    def withdraw(self, amount):
        if self.can_pay(amount):
            self.__balance = self.__balance - amount
            return True
        return False


class SavingsAccount(Account):
    def can_pay(self, amount):
        return self.get_balance() >= amount


class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.__overdraft_limit = overdraft_limit

    def can_pay(self, amount):
        return self.get_balance() - amount >= -self.__overdraft_limit


savings = SavingsAccount(100)
current = CurrentAccount(100, 50)
print(savings.withdraw(120), savings.get_balance())
print(current.withdraw(120), current.get_balance())
```

```output
False 100
True -20
```

- `Account` with a private balance, a constructor and a getter [B1]
- `withdraw` in `Account` that calls `can_pay`, reduces the balance and returns `True` when payment is possible [B1]
- `withdraw` returns `False` and leaves the balance unchanged otherwise [B1]
- `SavingsAccount` overrides `can_pay` to test that the balance is at least the amount [B1]
- `CurrentAccount` with a constructor that calls `super().__init__` and stores the overdraft limit [B1]
- `CurrentAccount.can_pay` tests that the balance after the withdrawal is not below minus the limit [B1]
- the results `False 100` for the savings account and `True -20` for the current account [B1]
:::

:::quiz
? What is the difference between a class and an object?
- They are the same thing with different names.
+ A class is a template; an object is one instance created from it.
- A class is one instance; an object is the template.
- A class holds only methods; an object holds only attributes.
> A class (for example `Pet`) defines the attributes and methods. An object (for example `Kito`) is a particular instance with its own values.
? What is the constructor called in Cambridge pseudocode?
- the name of the class
- `INIT`
+ `NEW`
- `CREATE`
> The constructor of every class is a procedure called `NEW`. `__init__` is the Python name, and naming it after the class is the habit of some other languages.
? Why is a setter given the job of checking a value?
- Because pseudocode will not run without a check.
- Because getters cannot return a value.
+ Because every change to the private attribute goes through it, so the rule is kept in one place.
- Because private attributes cannot be read.
> Encapsulation makes the setter the only way to change the attribute, so validation there protects the data. Getters do return values, and private attributes can be read through them.
? Which relationship is best modelled with inheritance?
- a Library and its Books
- a Car and its Engine
+ a Student and a Person
- a Playlist and its Songs
> A student **is a** person, so Student can inherit from Person. A library, a car and a playlist each **have** the other items, which is containment.
? A `Dog` class overrides `Speak`. What does that mean?
- The Dog class cannot use any inherited method.
- The superclass method is deleted for every class.
+ Dog has its own `Speak`, with the same name as Pet's, and Dog objects use it instead of the inherited one.
- `Speak` runs automatically when the object is created.
> Overriding replaces the inherited version for objects of the subclass only. Pet objects still use the original.
? A list holds a Cat, a Dog and a Pet, and a loop calls `Speak()` on each. What is this an example of?
- encapsulation
+ polymorphism
- containment
- recursion
> The same call gives different results depending on the class of each object. That is polymorphism. Encapsulation is about private data, and containment is "has a".
? In Python, a subclass method uses `self.__name` where `__name` was set in the superclass. What happens?
- It works because a subclass inherits all attributes.
- It returns an empty string.
+ It raises an AttributeError, because the private attribute belongs to the superclass; the subclass must use a getter.
- It changes the superclass for every object.
> Python renames a double-underscore attribute for the class that defines it, so another class cannot reach it by that name. Use the public getter instead.
? After `second = first`, where `first` is a Python object, `second.count = 5` is run. What is `first.count`?
- unchanged
+ 5
- 0
- an error
> Both names refer to the same object, so the change shows through `first` as well. A separate object needs its own call to the constructor.
:::

:::checklist What you can now do
- [ ] I can define and use the terms object, class, instance, attribute (property), method and constructor.
- [ ] I can write a class in pseudocode and in Python with a constructor (`NEW` and `__init__`) and create objects from it.
- [ ] I can explain encapsulation and write private attributes with public getters and setters, including validation in a setter.
- [ ] I can write a subclass that inherits from a superclass, using `INHERITS`, `SUPER.NEW` and `super().__init__`.
- [ ] I can explain overriding and polymorphism and show them with a list of objects of different classes.
- [ ] I can explain containment (aggregation) and say whether a relationship is "is a" or "has a".
- [ ] I can read, complete and draw a class diagram with its three compartments, the inheritance arrow and the containment line.
- [ ] I can design the classes for a scenario by finding nouns (classes and attributes) and verbs (methods).
- [ ] I can write a Paper 4 style program that reads a file, builds a list of objects, calls their methods and tests the output.
:::

:::recap
- A **class** is a template; an **object** (instance) is one made from it with `NEW` (pseudocode) or `ClassName(...)` (Python). A class has **attributes** (data) and **methods** (behaviour). The **constructor** is `NEW` in pseudocode and `__init__` in Python.
- **Encapsulation**: private attributes, public methods. A **getter** reads an attribute, a **setter** changes it and can **validate**. In Python the course convention is a double underscore (`self.__age`).
- **Inheritance** (`CLASS Cat INHERITS Pet`; `class Cat(Pet):`): the subclass gets the superclass's attributes and methods and calls `SUPER.NEW(…)` or `super().__init__(…)`. It is an "is a" relationship.
- **Overriding**: a subclass method with the same name replaces the inherited one. **Polymorphism**: the same call on objects of different classes behaves differently, so a mixed list is processed by one loop.
- **Containment (aggregation)**: an object has other objects as attributes ("has a"): a Library has Books. Do not use inheritance for "has a".
- A **class diagram** has three compartments: name, attributes with types, methods with return types. An arrow shows inheritance; a line with a diamond shows containment.
- Design from a description: nouns are classes and attributes, verbs are methods; look for "is a" and "has a".
- In Python, assigning an object to a second name does not copy it.
:::

:::links
- practise: [Object-oriented programming: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/20-further-programming-/object-oriented-programming/exam-questions/) · Save My Exams · 9618-style OOP questions with mark schemes [paid]
- read: [Python classes](https://docs.python.org/3/tutorial/classes.html) · Python.org · the official tutorial chapter on classes and inheritance
- read: [Python classes and objects](https://www.w3schools.com/python/python_classes.asp) · W3Schools · short lessons with try-it boxes
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste a class from this chapter and watch the objects appear in memory
- watch: [Craig 'n' Dave](https://www.youtube.com/@craigndave) · Craig 'n' Dave · A Level videos on OOP (UK boards; the ideas overlap 9618)

Links checked 13 November 2026.
:::

Next: [Programming paradigms: low-level, imperative and declarative](#cs.paradigms)
