@chapter cs.security
@title Security, privacy and data integrity
@level as
@paper CAIE 9618 Paper 1
@time 4–6 hours
@summary How data and computer systems are attacked and protected (malware, hackers, phishing, pharming, passwords, firewalls, encryption, access rights), and how a program keeps data accurate: validation checks including the modulo-11 check digit, verification by double entry, and parity, block parity and checksums for data in transit.

:::why
Almost everything you do online depends on data being kept private, safe and correct: your messages, your bank balance, your exam results. Paper 1 asks you to name the threats, describe how each protection works, choose the right validation check for a form field, and calculate check digits, parity bits and checksums by hand. The calculations are short and every mark is earned by a clear step.
:::

**Before you start**, you should know how characters are stored as binary codes from [Number systems and binary arithmetic](#cs.data) and what the operating system and a virus checker do from [System software: operating systems and translators](#cs.software).

:::try Warm-up
Q: The ASCII code for the capital letter `A` is 65. Write it as a 7-bit binary number. (from [Number systems and binary arithmetic](#cs.data))
A: \(65 = 64 + 1\), so the 7-bit code is `1000001`.
Q: What does the Domain Name System (DNS) do? (from [The internet: IP addresses, DNS and streaming](#cs.internet))
A: It translates a domain name that a person types (such as a website's name) into the IP address of the server, so the browser knows where to send its request.
Q: Why must a virus checker be updated regularly? (from [System software: operating systems and translators](#cs.software))
A: It compares files with a database of known malware, so it can find new malware only after the database has been updated.
:::

## Security, privacy and integrity

These three words sound alike and examiners test the difference, so learn each as a separate idea.

:::def Data security
Protecting data from unauthorised access, and from accidental or deliberate damage, corruption or loss.
:::

:::def Data privacy
The right of a person or an organisation to keep their personal or sensitive information private, and to control how it is collected, stored, used and shared with others.
:::

:::def Data integrity
The accuracy, completeness and consistency of data: it is correct and has not been changed or corrupted by mistake or by an attack.
:::

| Idea | The question it answers | Example of it going wrong |
|---|---|---|
| Security | Is the data protected from people who should not have it, and from damage or loss? | A hacker copies a customer database; a fire destroys the only copy of the records |
| Privacy | Is personal data collected, used and shared only in ways the person expects and has agreed to? | A shop passes its customers' addresses to an advertiser without permission |
| Integrity | Is the data correct and complete? | A pupil's mark of 71 is typed as 17 |

The ideas overlap. A security failure (a hacker steals a file) often causes a privacy failure (private details are now public), and a hacker who changes data harms integrity. But a company can respect privacy rules and still have insecure computers, or have perfectly secure computers that store wrong data.

### Why data and systems need protecting

Data security means protecting the **data**; system security means protecting the **computer system** itself: its hardware, software and network, so that it keeps working. Both matter.

:::key The need for security
- **Data**: personal and financial data can be used for fraud; a company's records are valuable; data may be needed again, so its loss or corruption costs time and money; laws in many countries make organisations responsible for protecting personal data; a company that loses its customers' trust loses business.
- **The system**: an attack or failure can stop the system working (a hospital cannot read records, a shop cannot take payments); malware can damage files and spread to other computers; fixing and recovering costs money and time.
:::

Not every risk is an attacker. Data can be lost through accidental deletion, a hardware fault, a power cut, a fire, or a stolen laptop. Good security plans for these too, mainly with back-ups from [System software: operating systems and translators](#cs.software).

## Threats

### Hackers and malware

:::def Hacker
A person who gains access to a computer system or its data without permission.
:::

A hacker may guess or steal a password, use a fault in some software, or trick a user into helping. The motive might be to steal data, to damage or change it, or just to show it can be done. (Some people are paid by organisations to try to break into their systems, so that the weaknesses can be fixed before a criminal finds them. That is legal because they have permission. You meet it again in [Ethics, ownership and the impact of AI](#cs.ethics).)

:::def Malware
Malicious software: any program written to damage a computer system, disrupt its use, or gain access to data without the owner's knowledge. It is short for "malicious software".
:::

You must know two kinds of malware.

:::def Virus
A program that copies itself into other programs or files on a computer. It runs when the infected program or file is opened, and can spread when infected files are shared. It may delete or corrupt data, or slow the computer down.
:::

:::def Spyware
Malware that secretly records what a user does, such as the keys they press, the websites they visit or the passwords they enter, and sends the information to someone else.
:::

A virus is often caught from an infected email attachment, a download, or a USB stick. Spyware often arrives hidden inside a program that the user chose to install. The difference to remember: a virus's main action is **damaging or spreading**; spyware's main action is **spying** and sending information away.

### Phishing and pharming

Both attacks aim to get your private details, such as a password or card number. They differ in how.

:::def Phishing
An attempt to obtain someone's private details by sending a message, such as an email or a text, that pretends to come from a trusted organisation and persuades the user to follow a link to a fake website and type their details in.
:::

:::def Pharming
An attack that redirects a user to a fake website even though they type the correct web address. Malicious code on the user's computer, or a change to the records of a DNS server, sends the browser to the criminal's website, which looks like the real one.
:::

| | Phishing | Pharming |
|---|---|---|
| How it starts | A message the user receives and chooses to act on | Malicious code on the computer, or a changed DNS record |
| What the user does | Clicks a link in the message | Types the correct address |
| The user is sent to | A fake website | A fake website |
| Why it works | Trust: the message looks genuine | The address is right, so nothing looks wrong |

:::warn Do not mix up phishing and pharming
A common wrong answer says that pharming "sends an email". The key words for **phishing** are *message* and *persuades the user to click*; for **pharming** they are *redirects* and *without the user doing anything wrong*.
:::

## Protecting data and systems

Every measure protects against some threats and none protects against everything. Layers of protection work better than any single one.

### User accounts, passwords and authentication

A **user account** gives each person their own identity on a computer or network. It has a username and a **password**. The system then knows who is using it, can give each user only the access they need, and can record what they did.

:::def Authentication
Proving that a user is who they claim to be, before they are given access to a system or to data.
:::

There are three kinds of evidence, and the strongest systems combine two of them:

| Kind | Meaning | Example |
|---|---|---|
| Something you **know** | a secret | a password or a PIN |
| Something you **have** | an object | a phone that receives a one-time code, a card |
| Something you **are** | a body feature | a fingerprint, a face |

:::key A strong password
- long (many characters) and not a real word or a name, date of birth or "12345";
- a mix of upper-case and lower-case letters, digits and symbols;
- different for every account, never shared, and changed if you think it has been seen;
- a system can also lock the account after several wrong attempts, so a hacker cannot simply try thousands of guesses.
:::

:::def Biometrics
Authentication that uses a measurable physical feature of a person, such as a fingerprint, the pattern of the iris, the face or the voice.
:::

Biometrics are hard to forget, lose or hand over, and they are difficult to copy. But the equipment costs more, it can wrongly reject a genuine user (a cut finger, a cold) or occasionally accept the wrong person, and a person cannot change a fingerprint if the stored copy is stolen. Collecting biometric data also raises privacy questions.

:::def Digital signature
A way of showing that a message or document really came from the person who claims to have sent it, and has not been changed on the way. It is created from the content of the document using a secret that only the sender has.
:::

A digital signature is a form of authentication for documents and messages: it works like a handwritten signature that also fails if anyone alters the text. How it is made is an A Level topic in [Encryption, SSL/TLS and digital certificates](#cs.security2).

### Firewall, anti-virus and anti-spyware

:::def Firewall
Hardware or software that sits between a computer or private network and an outside network, such as the internet. It examines the data (packets) going in and out and blocks anything that does not meet its rules.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 262" role="img" aria-label="A firewall between the internet at the top and a private network at the bottom. Allowed traffic passes down through the firewall to the private network. Blocked traffic, drawn dashed, stops at the firewall."><rect class="fm s-acc sw2" x="30" y="10" width="280" height="34"/><text class="tl tc" x="170" y="32">The internet</text><line class="ln" x1="100" y1="48" x2="100" y2="96" marker-end="url(#ah)"/><text class="tl" x="108" y="76">allowed</text><line class="ln dash" x1="240" y1="48" x2="240" y2="96" marker-end="url(#ah)"/><text class="tl" x="248" y="76">blocked</text><rect class="f1 s-acc sw2" x="30" y="100" width="280" height="58"/><text class="tl tc tb" x="170" y="122">Firewall</text><text class="tl tc" x="170" y="142">checks each packet</text><line class="ln" x1="100" y1="162" x2="100" y2="210" marker-end="url(#ah)"/><text class="tl" x="108" y="190">allowed</text><rect class="fm s-acc sw2" x="30" y="214" width="280" height="34"/><text class="tl tc" x="170" y="236">Private network</text></svg><figcaption>A firewall checks each packet against its rules. Packets the rules allow pass through; the rest are stopped.</figcaption></figure>
:::

The rules look at where a packet comes from and goes to (its IP addresses, from [The internet: IP addresses, DNS and streaming](#cs.internet)), which program or service it is for, and whether it is part of a connection that someone inside started. A firewall can be set to block traffic from addresses known to be harmful, or to allow only certain services through. It also checks traffic going **out**, so malware that has already got in cannot easily send stolen data away. A firewall can be a separate hardware device at the edge of a network, or software on one computer.

:::def Anti-virus software
Software that scans files and running programs for viruses and other malware, by comparing them with a database of known malware and by watching for suspicious behaviour, and that quarantines or removes what it finds.
:::

**Anti-spyware** software does the same job for spyware: it scans for programs that secretly record the user's activity, and blocks and removes them. Both must be kept up to date, because new malware appears all the time. They can scan files when they are opened (real-time protection) and the whole disk on a schedule.

### Encryption

:::def Encryption
Scrambling data using a key, so that it cannot be understood by anyone who does not have the right key. The original data is plaintext; the scrambled result is ciphertext.
:::

Encryption does not stop a criminal from intercepting data or from stealing a laptop. It makes what they get **useless**, because it is unreadable without the key. It is used for data stored on a disk and for data sent across a network.

The program below uses the simplest kind of encryption, a shift cipher, to make the idea of a key concrete. The key is the size of the shift. Each letter is moved along the alphabet by the key, wrapping from Z back to A.

```python
def shift_encrypt(text, key):
    result = ""
    for letter in text:
        code = (ord(letter) - ord("A") + key) % 26
        result = result + chr(code + ord("A"))
    return result


print(shift_encrypt("HELLO", 3))
print(shift_encrypt("KHOOR", 23))
```

Output:

```output
KHOOR
HELLO
```

With key 3, `HELLO` becomes `KHOOR`. Shifting by 23 (that is, 26 − 3) undoes it. Anyone who does not know the key sees only `KHOOR`. A shift cipher is far too weak for real use, because there are only 25 keys to try. Real encryption, and why it is hard to break, are in [Encryption, SSL/TLS and digital certificates](#cs.security2).

### Access rights

:::def Access rights
The permissions given to a user, or to a group of users, that decide what they may do with each file, folder or resource: for example read it, write to (change) it, or execute (run) it.
:::

A school stores marks in a file. The teacher can read and write, the head of department can read, and pupils can do nothing with it. Rights can be given to a single user or to a group (for example "teachers") so that new users get the right rights as soon as they join the group. Give each user the **least** access they need to do their job.

| File | Teachers | Pupils | Office staff |
|---|---|---|---|
| Test marks | read and write | no access | read |
| Class notices | read and write | read | read |
| Marking program | read and execute | no access | no access |

### Which protection answers which threat

:::key Threats and defences
| Threat | Main defences |
|---|---|
| Hacker | strong passwords and lock-out; firewall; access rights; encryption (so stolen data is unreadable); biometric or two-factor authentication |
| Virus | anti-virus kept up to date; do not open unknown attachments or run unknown programs; firewall; back-ups to restore |
| Spyware | anti-spyware; install only trusted software; firewall (stops it sending information out) |
| Phishing | spam filter; never follow a link in a message to log in (type the address yourself); check the sender and the web address; training for staff |
| Pharming | anti-malware (it removes the code that redirects); check that the address and the security padlock are correct; secure DNS |
| Data stolen or intercepted | encryption |
| Data lost or damaged | back-ups kept on a separate device or place; protection from fire and power failure |
:::

### From a stand-alone computer to a network

A computer on its own is exposed to fewer attacks than one on a network, because a stranger cannot reach it from the other side of the world. As more computers are connected, more protection is needed.

| Setting | Typical measures |
|---|---|
| Stand-alone home PC | user account and password; anti-virus and anti-spyware, kept up to date; careful with downloads and attachments; back-ups; a lock on the room or laptop |
| School or office network | all of those, plus: a firewall at the edge; separate user accounts with access rights by user or group; stronger authentication; encryption of sensitive files and of data sent over wireless links; staff training about phishing |

:::eg Choosing security measures (exam style)
A clinic in Lahore stores patient records on a network of computers. The network is connected to the internet. Describe three measures the clinic should use to keep the records secure. [6 marks]

Each measure needs a **description** (one mark) and how it protects the records (one mark).

- User accounts and passwords: each member of staff logs in with their own username and a strong password [B1], so only authorised people can open the records and the system can record who looked at them [B1].
- Firewall: examines the data going into and out of the network and blocks anything that does not meet its rules [B1], so a hacker on the internet cannot reach the records, and spyware cannot send them out [B1].
- Encryption: the records are stored and sent in scrambled form that needs a key to read [B1], so if the data is intercepted or a computer is stolen, it cannot be understood [B1].

Other creditworthy answers: access rights (doctors can change a record, receptionists only read it), anti-virus software kept up to date, biometric logins, back-ups.
:::

:::exam Match the measure to the threat
"Describe" questions need a precise action; "explain how it protects" needs the **threat** it blocks. "A firewall protects the network" earns little. "A firewall blocks traffic that does not meet its rules, so a hacker cannot reach the records" earns the mark.
:::

## Keeping data accurate: validation and verification

Security stops people from changing data they should not. **Integrity** is about whether the data is correct to begin with, and stays correct when it is typed in, stored and transmitted. Two different kinds of check protect it.

:::def Validation
An automatic check made by a program, when data is entered, that the data is reasonable and follows the rules for that field. It cannot prove that the data is correct, only that it is acceptable.
:::

:::def Verification
A check that data has been copied or entered accurately: that what is stored or received matches what was originally typed or sent.
:::

:::cols
:::col Validation
Is this data **reasonable**? "An age of 200 is impossible." Done automatically by the program, against a rule.
:::
:::col Verification
Is this data **the same as the original**? "The two entries match." Done by comparing a copy with the source, by a person or by the computer.
:::
:::

Validation cannot prove that data is correct. If a pupil's age is 17 and the operator types 71, a range check for ages 11 to 19 rejects 71, but if the operator types 14 instead of 17, every validation rule is satisfied and the data is wrong. Only verification, or checking against the source, can catch that.

### Validation checks

You need to know seven checks. A **validation rule** is the condition the data must meet; a **validation message** tells the user what is wrong. The table gives each check and an example. Data is entered by a user and the program tests it.

:::key The validation checks
| Check | What it tests | Example rule | Valid and invalid |
|---|---|---|---|
| Range | the value is between a lower and an upper limit | age from 11 to 19 | 15 passes; 10 and 20 fail |
| Limit | the value is not beyond **one** limit | quantity of at least 0 | 0 and 25 pass; −3 fails |
| Length | the number of characters is as required | a PIN of exactly 4 characters | `4821` passes; `482` fails |
| Presence | the field has not been left empty | name must be entered | `Amina` passes; an empty box fails |
| Format | the characters follow the required pattern | two capital letters then three digits | `KT402` passes; `kt402` and `KT4O2` fail |
| Existence | the value is one that really exists in a list or file | a student number that is on the register | `S1043` passes if it is on the register |
| Check digit | an extra digit, calculated from the others, agrees | modulo-11 check on a product code | see the next section |
:::

A **range check** has two limits; a **limit check** has only one (a minimum or a maximum). The ones that students muddle most: a **length check** counts characters (`4821` has length 4) but does not test what they are; a **format check** tests the pattern but a valid format does not mean the code exists.

:::eg Writing a range check
A school's software asks for the age of a new pupil. Ages must be from 11 to 19 inclusive. Write pseudocode that keeps asking for an age until a valid one is entered, and displays a message each time an invalid age is typed. [4 marks]

```pseudocode
DECLARE Age : INTEGER

REPEAT
   OUTPUT "Enter age (11 to 19): "
   INPUT Age
   IF Age < 11 OR Age > 19 THEN
      OUTPUT "Invalid: age must be from 11 to 19"
   ENDIF
UNTIL Age >= 11 AND Age <= 19
```

- input of an age inside a loop that repeats until a valid age is entered [B1]
- tests the lower limit (11) [B1]
- tests the upper limit (19), combined correctly with OR (invalid) or AND (valid) [B1]
- displays a message for an invalid age [B1]
:::

The same in Python. The program shows the console when the user types 25, then 9, then 15.

```python
age = int(input("Enter age (11 to 19): "))
while age < 11 or age > 19:
    print("Invalid: age must be from 11 to 19")
    age = int(input("Enter age (11 to 19): "))
print("Accepted:", age)
```

Output, when the user types 25, then 9, then 15:

```output
Enter age (11 to 19): 25
Invalid: age must be from 11 to 19
Enter age (11 to 19): 9
Invalid: age must be from 11 to 19
Enter age (11 to 19): 15
Accepted: 15
```

:::warn Test the type before the range
If the user types `abc`, `int("abc")` stops the program with a `ValueError`, and in pseudocode comparing text with a number is an error. A real program checks that the input is a number first (a **type check**, for example with the insert's `IS_NUM`), and only then applies the range check.
:::

Each of the other checks is a short condition. Here are all the checks from the table as Python functions, tested on the examples in the table.

```python
def range_check(age):
    return age >= 11 and age <= 19


def length_check(pin):
    return len(pin) == 4


def presence_check(name):
    return name != ""


def format_check(code):
    return (len(code) == 5 and code[:2].isalpha() and code[:2].isupper()
            and code[2:].isdigit())


def limit_check(quantity):
    return quantity >= 0


def existence_check(student_id, register):
    return student_id in register


register = ["S1042", "S1043", "S1077"]
print(range_check(15), range_check(10))
print(length_check("4821"), length_check("482"))
print(presence_check("Amina"), presence_check(""))
print(format_check("KT402"), format_check("kt402"), format_check("KT4O2"))
print(limit_check(0), limit_check(-3))
print(existence_check("S1043", register), existence_check("S2000", register))
```

Output:

```output
True False
True False
True False
True False False
True False
True False
```

In pseudocode, the format check uses the string functions from the insert. This version checks the pattern "two capital letters, then three digits", by testing each character's ASCII code.

```pseudocode
DECLARE Code, Ch : STRING
DECLARE Position : INTEGER
DECLARE Valid : BOOLEAN

INPUT Code
Valid ← TRUE
IF LENGTH(Code) <> 5 THEN
   Valid ← FALSE
ELSE
   FOR Position ← 1 TO 2
      Ch ← MID(Code, Position, 1)
      IF ASC(Ch) < ASC('A') OR ASC(Ch) > ASC('Z') THEN
         Valid ← FALSE
      ENDIF
   NEXT Position
   FOR Position ← 3 TO 5
      Ch ← MID(Code, Position, 1)
      IF ASC(Ch) < ASC('0') OR ASC(Ch) > ASC('9') THEN
         Valid ← FALSE
      ENDIF
   NEXT Position
ENDIF
IF Valid = TRUE THEN
   OUTPUT "Accepted"
ELSE
   OUTPUT "Format not valid"
ENDIF
```

An **existence check** is a search: the value must be found in the list. This is the linear search from [Data types, records and arrays](#cs.datatypes) used as a check.

```pseudocode
DECLARE Register : ARRAY[1:3] OF STRING
DECLARE StudentID : STRING
DECLARE Index : INTEGER
DECLARE Found : BOOLEAN

Register[1] ← "S1042"
Register[2] ← "S1043"
Register[3] ← "S1077"
INPUT StudentID
Found ← FALSE
FOR Index ← 1 TO 3
   IF Register[Index] = StudentID THEN
      Found ← TRUE
   ENDIF
NEXT Index
IF Found = FALSE THEN
   OUTPUT "No such student"
ENDIF
```

:::eg Choosing validation checks (exam style)
An online shop's order form has these fields. State one suitable validation check for each, and describe the rule. [8 marks]

(a) quantity: a whole number of items, at most 20 and at least 1. (b) delivery name. (c) security code on the back of a payment card: exactly three digits. (d) product code: one capital letter followed by four digits, for example `T7731`.

Each answer needs the **name of a check** and a **rule that fits the field**. The check must suit the field: a length check would not test whether a quantity is between 1 and 20.

(a) A range check [B1]: the quantity must be from 1 to 20 inclusive [B1].

(b) A presence check [B1]: the field must not be left empty [B1].

(c) A length check [B1]: the code must have exactly 3 characters [B1]. (A format check, "three digits", is also accepted, because the rule is about what the characters are.)

(d) A format check [B1]: the first character must be a capital letter and the next four must be digits [B1].
:::

### The check digit

A check digit protects codes such as product numbers, library member numbers and book numbers. It is an extra digit added to the end of the code, calculated from the other digits. When the code is typed, the computer repeats the calculation and compares the result with the digit that was typed. If they differ, the code was entered wrongly.

:::def Check digit
An extra digit added to the end of a code, calculated from the other digits of the code by an agreed method, so that a program can check that the code has been entered correctly.
:::

The usual method in this course is **modulo 11 with weights**. Each digit is multiplied by a **weight** that depends on its position, so that swapping two digits changes the answer. "Modulo 11" means "the remainder when dividing by 11".

:::key Calculating a modulo-11 check digit
For a code of \(n\) digits:
1. Give the digits the weights \(n + 1,\ n,\ \ldots,\ 3,\ 2\), from left to right (the first digit has the biggest weight; the last has weight 2).
2. Multiply each digit by its weight and add the products. This is the **total**.
3. Divide the total by 11 and find the **remainder**.
4. The check digit is \(11 - \text{remainder}\). If the remainder is 0, the check digit is 0 (not 11). If the answer is 10, the check digit is written **X**.
5. Add the check digit to the end of the code.
:::

:::eg Calculating a check digit (exam style)
A product code has seven digits, 4829316. Calculate its modulo-11 check digit. [4 marks]

There are 7 digits, so the weights are 8, 7, 6, 5, 4, 3, 2.

| Digit | 4 | 8 | 2 | 9 | 3 | 1 | 6 |
|---|---|---|---|---|---|---|---|
| Weight | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Product | 32 | 56 | 12 | 45 | 12 | 3 | 12 |

Each digit is multiplied by its weight. [M1]

Total: \(32 + 56 + 12 + 45 + 12 + 3 + 12 = 172\). [A1]

Remainder: \(172 \div 11 = 15\) remainder 7, because \(11 \times 15 = 165\). [M1]

Check digit: \(11 - 7 = 4\). [A1] The full code is **48293164**.
:::

To check a code that has been typed, give the check digit the weight 1 and add it to the total. A correct code has a total that is an exact multiple of 11. For 48293164 the total is \(172 + 4 \times 1 = 176 = 11 \times 16\), so the code is valid.

If the remainder is 1, then \(11 - 1 = 10\), and the check digit cannot be written as one digit, so it is written as the letter **X**. Take 627093 (six digits, weights 7, 6, 5, 4, 3, 2): the products are 42, 12, 35, 0, 27 and 6, the total is 122, and \(122 = 11 \times 11 + 1\), so the remainder is 1 and the check digit is X. The full code is 627093X. A remainder of 0 gives a check digit of 0: for 7352 the total is 66, which is exactly \(11 \times 6\), so the check digit is 0 and the code is 73520.

```pseudocode
DECLARE Code : STRING
DECLARE Position, Digit, Weight, Total, Remainder, CheckDigit : INTEGER

INPUT Code               // seven digits, for example 4829316
Total ← 0
FOR Position ← 1 TO 7
   Digit ← STR_TO_NUM(MID(Code, Position, 1))
   Weight ← 9 - Position      // 8 for the first digit, 2 for the last
   Total ← Total + Digit * Weight
NEXT Position
Remainder ← Total MOD 11
CheckDigit ← (11 - Remainder) MOD 11
IF CheckDigit = 10 THEN
   OUTPUT Code & "X"
ELSE
   OUTPUT Code & NUM_TO_STR(CheckDigit)
ENDIF
```

The last mod 11 turns 11 (when the remainder is 0) into 0. The Python version works for a code of any length, and also verifies a code:

```python
def check_digit(code):
    n = len(code)
    total = 0
    for position in range(n):
        total = total + int(code[position]) * (n + 1 - position)
    remainder = total % 11
    digit = (11 - remainder) % 11
    return "X" if digit == 10 else str(digit)


def is_valid(full_code):
    return check_digit(full_code[:-1]) == full_code[-1]


print(check_digit("4829316"), check_digit("627093"), check_digit("7352"))
print(is_valid("48293164"), is_valid("48293614"))
```

Output:

```output
4 X 0
True False
```

The second line shows the point of the method. The code 48293614 is 48293164 with the sixth and seventh digits swapped, and it is rejected.

:::key What a modulo-11 check digit catches
- Any **single wrong digit**, for example 4829316**4** typed as 4829316**5** (for codes of up to ten characters including the check digit, as in this course).
- Any **two neighbouring digits swapped** (a transposition, a very common typing error).
- It does **not** catch every error: two errors can cancel out, and a code that has the right check digit may still be a code nobody has issued. A check digit is validation: it shows the code is possible, not that it is right.
:::

Some codes use a different rule. Book numbers of 13 digits use **modulo 10**: the weights alternate 1 and 3 (the digit next to the check digit has weight 3, and the check digit has weight 1, so for an even number of digits the weights read 1, 3, 1, 3 from the left), the total is found, and the check digit is \(10 - (\text{total} \bmod 10)\), or 0 if that gives 10. For 315806 the weights are 1, 3, 1, 3, 1, 3, the total is \(3 + 3 + 5 + 24 + 0 + 18 = 53\), the remainder is 3, and the check digit is 7. A modulo-10 check misses a swap of two neighbouring digits that differ by 5. Questions tell you the weights and the modulus. Use the method they give.

Try the widget. It shows each product, the total, the remainder and the check digit, and it can check a full code. Try swapping two digits in a code that is valid and watch the verdict change.

:::html
<div class="widget" data-w="cs-check" data-mode="check" data-method="11" data-code="4829316"></div>
:::

## Verification

### During data entry

Verification during entry checks that what was typed matches the source. The two methods in the syllabus:

:::cols
:::col Visual check
The person who typed the data reads what is on the screen (or a printout) and compares it with the original document, and corrects any difference. It is cheap, but people miss errors in their own work, and it takes time.
:::
:::col Double entry
The data is typed **twice**, by the same person or by two people, and the computer compares the two entries. If they differ, one of them is wrong and the user is asked to type it again. It is slower, but a person is unlikely to make exactly the same mistake twice. It is used for passwords and for important data.
:::
:::

```pseudocode
DECLARE First, Second : STRING

REPEAT
   OUTPUT "Enter the new password: "
   INPUT First
   OUTPUT "Enter it again: "
   INPUT Second
   IF First <> Second THEN
      OUTPUT "The two entries do not match. Try again."
   ENDIF
UNTIL First = Second
```

Double entry shows that the two entries are **the same**, not that they are correct: if someone makes the same mistake twice, the check passes. It also does not tell the person which entry is wrong.

:::eg Spot the error: validation or verification?
Question: Explain the difference between validation and verification. [4 marks]

A student wrote:

```text
01  Validation is when the computer checks that the data entered is
02  reasonable and follows rules, such as a range check.
03  It proves that the data is correct.
04  Verification is when the data is checked to see that it has been
05  copied or typed accurately, for example by entering it twice.
06  The computer compares the two entries and reports a difference.
```

Lines 01 and 02 give a correct description of validation: a check that data is reasonable and follows rules [B1]. **Line 03 is wrong: validation cannot prove that data is correct.** A range check on an age accepts 14 even if the true age is 17 [B0]. Lines 04 and 05 describe verification correctly, as a check that data was copied accurately, with double entry as the example [B1]. Line 06 adds a correct detail of how the computer compares the entries [B1]. The answer scores 3 out of 4.

A fourth mark for validation would need a true statement, such as "a validation check can only accept data that is possible; it does not detect a wrong but reasonable value".
:::

### During data transfer

When data is sent from one place to another (over a network, or from a disk to memory), bits can be changed by electrical interference or a fault. The receiver needs a way to **detect** that the data has changed. The methods work by sending a little **extra** data, calculated from the original, that the receiver recalculates and compares.

#### Parity check

:::def Parity bit
An extra bit added to a group of bits, usually a byte, so that the total number of 1s is always even (even parity) or always odd (odd parity). The receiver counts the 1s and reports an error if the number is not what was agreed.
:::

Seven bits of data are enough for an ASCII character, so the eighth bit of a byte is free to be the parity bit. Suppose the two computers agree to use **even parity**, with the parity bit as the **left-most bit** (the most significant bit, MSB). The sender counts the 1s in the data and chooses the parity bit that makes the total even. (A question tells you which type of parity to use and whether the parity bit is the left-most or the right-most bit of the byte; the counting is the same either way.)

For `A`, the 7-bit code is `1000001`, which has two 1s, an even number, so the parity bit is 0 and the byte sent is `01000001`. For `T`, the code is `1010100`, which has three 1s, so the parity bit is 1 and the byte is `11010100` (four 1s). With **odd parity** the choice is reversed: `A` becomes `11000001` (three 1s) and `T` becomes `01010100` (three 1s).

```python
def parity_bit(data_bits, even=True):
    ones = data_bits.count("1")
    if even:
        return str(ones % 2)
    return str(1 - ones % 2)


for letter in "AT":
    bits = format(ord(letter), "07b")
    print(letter, bits, parity_bit(bits), parity_bit(bits, even=False))
```

Output:

```output
A 1000001 0 1
T 1010100 1 0
```

The columns show the letter, its 7 bits, the even-parity bit and the odd-parity bit.

```pseudocode
DECLARE DataBits, ParityBit : STRING
DECLARE Index, Ones : INTEGER

INPUT DataBits                  // seven characters, each "0" or "1"
Ones ← 0
FOR Index ← 1 TO 7
   IF MID(DataBits, Index, 1) = "1" THEN
      Ones ← Ones + 1
   ENDIF
NEXT Index
IF Ones MOD 2 = 0 THEN
   ParityBit ← "0"             // even parity: already an even number of 1s
ELSE
   ParityBit ← "1"
ENDIF
OUTPUT ParityBit & DataBits
```

The receiver counts the 1s in each byte it receives. With even parity, a byte with an odd number of 1s must have been damaged. If a single bit flips in transit, the count changes by one, from even to odd, so the error is **detected**.

:::key Limits of a parity check
- It detects a **single** flipped bit, or any odd number of flips in a byte.
- It does **not** detect two flipped bits in the same byte (the count is still even), or any even number.
- It tells you **which byte** (or at least that one is wrong) but not **which bit**, so it cannot correct the error. The data must be sent again.
:::

:::eg Parity bits (exam style)
(a) The 7-bit code for `K` is 1001011. Write the byte sent using even parity, with the parity bit as the left-most bit. [2 marks] (b) A system uses odd parity. State whether the byte 01101001 was received correctly. [2 marks]

(a) The code 1001011 has four 1s, an even number, so the parity bit is 0 [B1] and the byte is **01001011** [B1].

(b) The byte 01101001 contains four 1s [B1], an even number, but odd parity needs an odd number, so the byte contains an error [B1].
:::

#### Block parity

A single parity bit cannot say which bit is wrong. **Block parity** fixes that by checking in two directions. The data is sent in a block of bytes. Each byte has its own parity bit (the **row** check), and after the last byte the sender adds an extra **parity byte**, which has one parity bit for each **column** of the block.

The word SECURED has seven letters, so it fills seven bytes. Here are the ASCII codes, each with its even-parity bit on the left, followed by the parity byte:

| Byte | Character | Parity bit | 7 data bits | Whole byte |
|---|---|---|---|---|
| 1 | S | 0 | 1010011 | 01010011 |
| 2 | E | 1 | 1000101 | 11000101 |
| 3 | C | 1 | 1000011 | 11000011 |
| 4 | U | 0 | 1010101 | 01010101 |
| 5 | R | 1 | 1010010 | 11010010 |
| 6 | E | 1 | 1000101 | 11000101 |
| 7 | D | 0 | 1000100 | 01000100 |
| 8 (parity byte) | | | | 01010011 |

The first bit of the parity byte is the parity of the first column (the column of the parity bits themselves): the column has 0, 1, 1, 0, 1, 1, 0, which is four 1s, so the parity bit is 0. The second bit of the parity byte is the parity of column 1 (the first data bit): 1, 1, 1, 1, 1, 1, 1 is seven 1s, so the bit is 1. Each of the eight columns is done in the same way, so that every row and every column of the whole block has an even number of 1s.

Suppose one bit is changed in transit. The receiver checks every row and every column. A flipped bit makes exactly one row and exactly one column fail, and the error is where they cross.

:::html
<figure class="fig small"><svg viewBox="0 0 350 312" role="img" aria-label="An eight by eight grid of bits: seven data bytes for the word SECURED and a parity byte, with the parity bit on the left of each byte. One bit has been flipped. Byte 4 fails its row check and data bit 3 fails its column check, so the error is at byte 4, data bit 3."><text class="tl tc tb" x="105.0" y="28">P</text><text class="tl tc tb" x="131.0" y="28">1</text><text class="tl tc tb" x="157.0" y="28">2</text><text class="tl tc tb" x="183.0" y="28">3</text><text class="tl tc tb" x="209.0" y="28">4</text><text class="tl tc tb" x="235.0" y="28">5</text><text class="tl tc tb" x="261.0" y="28">6</text><text class="tl tc tb" x="287.0" y="28">7</text><text class="tl tc tb" x="324" y="28">row</text><text class="tl te" x="84" y="58">byte 1</text><rect class="fm s-acc sw2" x="92" y="40" width="26" height="26"/><text class="tl tc" x="105.0" y="58">0</text><rect class="fm s-acc sw2" x="118" y="40" width="26" height="26"/><text class="tl tc" x="131.0" y="58">1</text><rect class="fm s-acc sw2" x="144" y="40" width="26" height="26"/><text class="tl tc" x="157.0" y="58">0</text><rect class="fm s-acc sw2" x="170" y="40" width="26" height="26"/><text class="tl tc" x="183.0" y="58">1</text><rect class="fm s-acc sw2" x="196" y="40" width="26" height="26"/><text class="tl tc" x="209.0" y="58">0</text><rect class="fm s-acc sw2" x="222" y="40" width="26" height="26"/><text class="tl tc" x="235.0" y="58">0</text><rect class="fm s-acc sw2" x="248" y="40" width="26" height="26"/><text class="tl tc" x="261.0" y="58">1</text><rect class="fm s-acc sw2" x="274" y="40" width="26" height="26"/><text class="tl tc" x="287.0" y="58">1</text><text class="tl te" x="84" y="84">byte 2</text><rect class="fm s-acc sw2" x="92" y="66" width="26" height="26"/><text class="tl tc" x="105.0" y="84">1</text><rect class="fm s-acc sw2" x="118" y="66" width="26" height="26"/><text class="tl tc" x="131.0" y="84">1</text><rect class="fm s-acc sw2" x="144" y="66" width="26" height="26"/><text class="tl tc" x="157.0" y="84">0</text><rect class="fm s-acc sw2" x="170" y="66" width="26" height="26"/><text class="tl tc" x="183.0" y="84">0</text><rect class="fm s-acc sw2" x="196" y="66" width="26" height="26"/><text class="tl tc" x="209.0" y="84">0</text><rect class="fm s-acc sw2" x="222" y="66" width="26" height="26"/><text class="tl tc" x="235.0" y="84">1</text><rect class="fm s-acc sw2" x="248" y="66" width="26" height="26"/><text class="tl tc" x="261.0" y="84">0</text><rect class="fm s-acc sw2" x="274" y="66" width="26" height="26"/><text class="tl tc" x="287.0" y="84">1</text><text class="tl te" x="84" y="110">byte 3</text><rect class="fm s-acc sw2" x="92" y="92" width="26" height="26"/><text class="tl tc" x="105.0" y="110">1</text><rect class="fm s-acc sw2" x="118" y="92" width="26" height="26"/><text class="tl tc" x="131.0" y="110">1</text><rect class="fm s-acc sw2" x="144" y="92" width="26" height="26"/><text class="tl tc" x="157.0" y="110">0</text><rect class="fm s-acc sw2" x="170" y="92" width="26" height="26"/><text class="tl tc" x="183.0" y="110">0</text><rect class="fm s-acc sw2" x="196" y="92" width="26" height="26"/><text class="tl tc" x="209.0" y="110">0</text><rect class="fm s-acc sw2" x="222" y="92" width="26" height="26"/><text class="tl tc" x="235.0" y="110">0</text><rect class="fm s-acc sw2" x="248" y="92" width="26" height="26"/><text class="tl tc" x="261.0" y="110">1</text><rect class="fm s-acc sw2" x="274" y="92" width="26" height="26"/><text class="tl tc" x="287.0" y="110">1</text><text class="tl te" x="84" y="136">byte 4</text><rect class="fm s-acc sw2" x="92" y="118" width="26" height="26"/><text class="tl tc" x="105.0" y="136">0</text><rect class="fm s-acc sw2" x="118" y="118" width="26" height="26"/><text class="tl tc" x="131.0" y="136">1</text><rect class="fm s-acc sw2" x="144" y="118" width="26" height="26"/><text class="tl tc" x="157.0" y="136">0</text><rect class="f1 s-acc sw2" x="170" y="118" width="26" height="26"/><text class="tl tc" x="183.0" y="136">0</text><rect class="fm s-acc sw2" x="196" y="118" width="26" height="26"/><text class="tl tc" x="209.0" y="136">0</text><rect class="fm s-acc sw2" x="222" y="118" width="26" height="26"/><text class="tl tc" x="235.0" y="136">1</text><rect class="fm s-acc sw2" x="248" y="118" width="26" height="26"/><text class="tl tc" x="261.0" y="136">0</text><rect class="fm s-acc sw2" x="274" y="118" width="26" height="26"/><text class="tl tc" x="287.0" y="136">1</text><text class="tl tc tb" x="324" y="136">✗</text><text class="tl te" x="84" y="162">byte 5</text><rect class="fm s-acc sw2" x="92" y="144" width="26" height="26"/><text class="tl tc" x="105.0" y="162">1</text><rect class="fm s-acc sw2" x="118" y="144" width="26" height="26"/><text class="tl tc" x="131.0" y="162">1</text><rect class="fm s-acc sw2" x="144" y="144" width="26" height="26"/><text class="tl tc" x="157.0" y="162">0</text><rect class="fm s-acc sw2" x="170" y="144" width="26" height="26"/><text class="tl tc" x="183.0" y="162">1</text><rect class="fm s-acc sw2" x="196" y="144" width="26" height="26"/><text class="tl tc" x="209.0" y="162">0</text><rect class="fm s-acc sw2" x="222" y="144" width="26" height="26"/><text class="tl tc" x="235.0" y="162">0</text><rect class="fm s-acc sw2" x="248" y="144" width="26" height="26"/><text class="tl tc" x="261.0" y="162">1</text><rect class="fm s-acc sw2" x="274" y="144" width="26" height="26"/><text class="tl tc" x="287.0" y="162">0</text><text class="tl te" x="84" y="188">byte 6</text><rect class="fm s-acc sw2" x="92" y="170" width="26" height="26"/><text class="tl tc" x="105.0" y="188">1</text><rect class="fm s-acc sw2" x="118" y="170" width="26" height="26"/><text class="tl tc" x="131.0" y="188">1</text><rect class="fm s-acc sw2" x="144" y="170" width="26" height="26"/><text class="tl tc" x="157.0" y="188">0</text><rect class="fm s-acc sw2" x="170" y="170" width="26" height="26"/><text class="tl tc" x="183.0" y="188">0</text><rect class="fm s-acc sw2" x="196" y="170" width="26" height="26"/><text class="tl tc" x="209.0" y="188">0</text><rect class="fm s-acc sw2" x="222" y="170" width="26" height="26"/><text class="tl tc" x="235.0" y="188">1</text><rect class="fm s-acc sw2" x="248" y="170" width="26" height="26"/><text class="tl tc" x="261.0" y="188">0</text><rect class="fm s-acc sw2" x="274" y="170" width="26" height="26"/><text class="tl tc" x="287.0" y="188">1</text><text class="tl te" x="84" y="214">byte 7</text><rect class="fm s-acc sw2" x="92" y="196" width="26" height="26"/><text class="tl tc" x="105.0" y="214">0</text><rect class="fm s-acc sw2" x="118" y="196" width="26" height="26"/><text class="tl tc" x="131.0" y="214">1</text><rect class="fm s-acc sw2" x="144" y="196" width="26" height="26"/><text class="tl tc" x="157.0" y="214">0</text><rect class="fm s-acc sw2" x="170" y="196" width="26" height="26"/><text class="tl tc" x="183.0" y="214">0</text><rect class="fm s-acc sw2" x="196" y="196" width="26" height="26"/><text class="tl tc" x="209.0" y="214">0</text><rect class="fm s-acc sw2" x="222" y="196" width="26" height="26"/><text class="tl tc" x="235.0" y="214">1</text><rect class="fm s-acc sw2" x="248" y="196" width="26" height="26"/><text class="tl tc" x="261.0" y="214">0</text><rect class="fm s-acc sw2" x="274" y="196" width="26" height="26"/><text class="tl tc" x="287.0" y="214">0</text><text class="tl te" x="84" y="240">parity byte</text><rect class="fm s-acc sw2" x="92" y="222" width="26" height="26"/><text class="tl tc" x="105.0" y="240">0</text><rect class="fm s-acc sw2" x="118" y="222" width="26" height="26"/><text class="tl tc" x="131.0" y="240">1</text><rect class="fm s-acc sw2" x="144" y="222" width="26" height="26"/><text class="tl tc" x="157.0" y="240">0</text><rect class="fm s-acc sw2" x="170" y="222" width="26" height="26"/><text class="tl tc" x="183.0" y="240">1</text><rect class="fm s-acc sw2" x="196" y="222" width="26" height="26"/><text class="tl tc" x="209.0" y="240">0</text><rect class="fm s-acc sw2" x="222" y="222" width="26" height="26"/><text class="tl tc" x="235.0" y="240">0</text><rect class="fm s-acc sw2" x="248" y="222" width="26" height="26"/><text class="tl tc" x="261.0" y="240">1</text><rect class="fm s-acc sw2" x="274" y="222" width="26" height="26"/><text class="tl tc" x="287.0" y="240">1</text><text class="tl te tb" x="84" y="268">column</text><text class="tl tc tb" x="183.0" y="268">✗</text><text class="tl tc tb" x="196" y="296">error: byte 4, data bit 3</text></svg><figcaption>A received block with even parity. The row check fails for byte 4 and the column check fails for data bit 3. The shaded bit where they meet is the error.</figcaption></figure>
:::

In the figure, the column labelled P holds the parity bits and the columns 1 to 7 hold the data bits. Byte 4 is now `01000101`, which has three 1s, an odd number, so its row fails. Data bit 3 (the column labelled 3) now has three 1s down it, so its column fails. The bit where byte 4 meets column 3 is wrong, and the receiver can **correct** it by flipping it: the byte becomes `01010101`, the letter U again.

```python
word = "SECURED"
block = []
for letter in word:
    bits = format(ord(letter), "07b")
    block.append(str(bits.count("1") % 2) + bits)
parity_byte = ""
for column in range(8):
    ones = 0
    for row in block:
        ones = ones + int(row[column])
    parity_byte = parity_byte + str(ones % 2)
block.append(parity_byte)
for row in block:
    print(row)

received = [list(row) for row in block]
received[3][3] = "0" if received[3][3] == "1" else "1"
bad_rows = []
for r in range(8):
    if received[r].count("1") % 2 == 1:
        bad_rows.append(r + 1)
bad_columns = []
for c in range(8):
    ones = 0
    for r in range(8):
        ones = ones + int(received[r][c])
    if ones % 2 == 1:
        bad_columns.append(c)
print("Rows failing:", bad_rows, "columns failing:", bad_columns)
print("Error at byte", bad_rows[0], "data bit", bad_columns[0])
```

Output:

```output
01010011
11000101
11000011
01010101
11010010
11000101
01000100
01010011
Rows failing: [4] columns failing: [3]
Error at byte 4 data bit 3
```

(The program numbers the bytes from 1 and the columns from 0, with column 0 the parity bit, so "data bit 3" is column 3.) The widget below lets you do the same: click any bit to flip it, or press the buttons to corrupt bits at random, and see which rows and columns fail.

:::html
<div class="widget" data-w="cs-check" data-mode="parity" data-parity="even"></div>
:::

:::key What block parity can and cannot do
- **One** wrong bit: exactly one row and one column fail, and their crossing is the bit. It can be **located and corrected**.
- **Two** wrong bits in different rows and different columns: two rows and two columns fail, but there are four crossings, so you cannot tell which two are wrong. It is **detected** but not located.
- Two wrong bits in the same row: no row fails (the count is still even), but two columns fail. It is detected by the column check but cannot be located.
- Four wrong bits at the corners of a rectangle (two in each of two rows, in the same two columns): every row and every column still has an even count, so the errors **escape detection**.
:::

:::eg Locating an error with block parity (exam style)
A block of four bytes is sent with a parity byte, using even parity with the parity bit on the left. Bit 1 is the first bit to the right of the parity bit. The block received is shown. Find the byte and the bit that is wrong, and state what the receiver does to correct it. [4 marks]

| Byte | Parity bit | Bit 1 | Bit 2 | Bit 3 | Bit 4 | Bit 5 | Bit 6 | Bit 7 |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| 2 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 4 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| Parity byte | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |

Check the rows first, then the columns, and write down every count.

Rows: byte 1 has four 1s, byte 2 has five, byte 3 has two, byte 4 has four and the parity byte has four. Only byte 2 has an odd number, so byte 2 fails. [B1]

Columns: from the parity bit column to Bit 7 the numbers of 1s are 4, 4, 0, 0, 2, 3, 2 and 4. Only the Bit 5 column has an odd number, so it fails. [B1]

The wrong bit is where the failing row and the failing column cross: **byte 2, Bit 5**. [B1]

The receiver flips that bit from 0 to 1, so byte 2 becomes 11001111. [B1]
:::

#### Checksum

:::def Checksum
A value calculated from a block of data and sent with it. The receiver calculates the value again from the data it received and compares it with the checksum that arrived. If they differ, the data has been changed.
:::

A simple checksum adds up the values of all the bytes in the block. The total can be much bigger than one byte, so only the remainder after dividing by 256 is kept, which always fits in one byte. This is a calculation of the kind \(\text{total} \bmod 256\).

:::eg Calculating a checksum (exam style)
A block holds four bytes with the denary values 52, 200, 117 and 83. The checksum is the total of the bytes modulo 256. (a) Calculate the checksum. [4 marks] (b) The receiver receives the bytes 52, 200, 119 and 83 and the checksum from part (a). Show that the receiver detects an error. [2 marks]

(a) Add the bytes: \(52 + 200 + 117 + 83 = 452\). [M1] [A1]

Divide by 256 and keep the remainder: \(452 - 256 = 196\). [M1] The checksum is **196**. [A1]

(b) The receiver adds the bytes it received: \(52 + 200 + 119 + 83 = 454\), and \(454 - 256 = 198\). [B1] This differs from the checksum 196 that was sent, so an error has been detected. [B1]
:::

```python
data = [52, 200, 117, 83]
checksum = sum(data) % 256
print("Total:", sum(data), "checksum:", checksum)

received = [52, 200, 119, 83]
print("Matches:", sum(received) % 256 == checksum)

swapped = [200, 52, 117, 83]
print("Matches:", sum(swapped) % 256 == checksum)
```

Output:

```output
Total: 452 checksum: 196
Matches: False
Matches: True
```

The last line is a warning. When two bytes swap places the total is unchanged, so this checksum does not notice. Nor does it notice two errors that cancel each other, such as one byte that is 3 too big and another that is 3 too small.

```pseudocode
DECLARE Data : ARRAY[1:4] OF INTEGER
DECLARE Index, Total, Checksum : INTEGER

Data[1] ← 52
Data[2] ← 200
Data[3] ← 117
Data[4] ← 83
Total ← 0
FOR Index ← 1 TO 4
   Total ← Total + Data[Index]
NEXT Index
Checksum ← Total MOD 256
OUTPUT "Checksum: ", Checksum
```

:::key Checking data: which method for which job
| Method | When used | What it checks | Weakness |
|---|---|---|---|
| Range, format, length, presence, limit, existence | on entry | the value is reasonable (validation) | cannot tell a reasonable wrong value from a right one |
| Check digit | on entry of a code | the code is possible (validation) | does not catch every error; a made-up code can be correct |
| Visual check, double entry | on entry | the data matches the source (verification) | a person can repeat the same mistake; slow |
| Parity bit | transfer, per byte | one bit has flipped | misses two flips in one byte; cannot say which bit |
| Block parity | transfer, per block | one bit has flipped, and which one | can miss four errors in a rectangle |
| Checksum | transfer, per block | the data has changed | misses swapped bytes and errors that cancel |
:::

Parity, block parity and checksums only **detect** errors (block parity can also locate a single one). When an error is detected, the usual response is to ask the sender to send the block again.

:::tip Do the calculation, then check it
For a check digit, add the check digit to the total with weight 1 and confirm you get a multiple of 11. For parity, count the 1s again in the finished byte. For a checksum, add the bytes a second time. All three checks take a few seconds and catch most slips.
:::

:::try Start easy, finish at exam standard
Q: State one difference between a virus and spyware.
A: A virus copies itself into other files and can damage data or spread to other computers; spyware secretly records what the user does and sends the information to someone else.
Q: A date-of-birth field must not be later than today's date. Which validation check is this?
A: A limit check, because there is only one limit (the date cannot be after today).
Q: Which validation check makes sure the user does not leave the username box empty?
A: A presence check.
Q: Give the even-parity bit for the 7-bit code 1101001.
A: The code has four 1s, an even number, so the parity bit is 0.
Q: Give the odd-parity bit for the 7-bit code 0110101.
A: The code has four 1s. To make the total odd, the parity bit is 1.
Q: Calculate the checksum (total modulo 256) of the bytes 10, 20 and 250.
A: \(10 + 20 + 250 = 280\), and \(280 - 256 = 24\). The checksum is 24.
Q: Calculate the modulo-11 check digit for the code 2749 (weights 5, 4, 3, 2).
A: \(2 \times 5 + 7 \times 4 + 4 \times 3 + 9 \times 2 = 10 + 28 + 12 + 18 = 68\). \(68 = 11 \times 6 + 2\), so the remainder is 2 and the check digit is \(11 - 2 = 9\). The full code is 27499.
Q: A user receives an email, apparently from their bank, asking them to click a link and "confirm their password". What type of attack is this?
A: Phishing: a message pretending to be from a trusted organisation that persuades the user to enter their details on a fake website.
Q: Give two ways to reduce the risk of phishing.
A: Do not click links in unexpected messages (type the website address yourself); check the sender's address and the web address; use a spam filter; train staff to recognise phishing messages.
Q: Does encryption stop a hacker from intercepting data on a network? Explain.
A: No. The hacker can still copy the data, but because it is scrambled, they cannot understand it without the key.
Q: A pupil's mark of 82 is accidentally typed as 28. Which checks could detect this, and which could not?
A: A range check from 0 to 100 would not detect it, because 28 is within the range. Verification (visual check or double entry) could detect it, because the typed value would not match the source.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ For each event, state whether it mainly affects data security, data privacy or data integrity. (a) A hospital worker gives patients' addresses to a company that sells medicines, without the patients' permission. (b) A typing error stores a mark of 71 as 17. (c) A thief breaks into a server room and steals a hard disk.
A: (a) Data privacy [B1] (b) Data integrity [B1] (c) Data security [B1]

Q: [4 marks] ★ (a) Describe what is meant by phishing. [2] (b) State two ways in which a user can protect themselves from phishing. [2]
A: (a) Phishing is a message (such as an email or text) that appears to come from a trusted organisation [B1] and persuades the user to follow a link to a fake website and give their private details [B1].

(b) Any two of: do not click links in unexpected messages (type the address yourself); check the sender's address and the web address; do not give passwords in response to a message; use a spam filter. [B1] [B1]

Q: [6 marks] ★★ A company in Lima has a network connected to the internet. (a) Describe how a firewall protects the network. [3] (b) The company considers using fingerprints instead of passwords to log in. Describe two advantages and one disadvantage of using fingerprints. [3]
H: For (a), say what the firewall examines, what it does with it, and what that achieves.
A: (a) The firewall examines the data (packets) going into and out of the network [B1] and blocks any that do not meet its rules [B1], so that hackers cannot get in, and malware or spyware cannot send data out [B1].

(b) Advantages (any two): a fingerprint cannot be forgotten or guessed [B1]; it is much harder to share or copy than a password [B1]. Disadvantage (any one): the scanners cost more; a genuine user may be rejected (for example with a cut or dirty finger); a fingerprint cannot be changed if the stored copy is stolen [B1].

Q: [8 marks] ★★ A school collects entries for a sports day on a form. State one suitable validation check for each field and describe the rule. (a) Year group: a whole number from 7 to 13. (b) House: one of Red, Blue, Green or Gold. (c) Emergency telephone number: it must be given. (d) Entry code: two capital letters followed by two digits, for example `SD07`.
H: Each check needs a name and a rule that fits that field.
A: (a) Range check [B1]: the year group must be at least 7 and at most 13 [B1].

(b) Existence check [B1]: the house must be one of the four names in the list [B1]. (A list of allowed values; accept "lookup" or "existence".)

(c) Presence check [B1]: the field must not be left empty [B1].

(d) Format check [B1]: the first two characters must be capital letters and the last two must be digits [B1]. (A length check of 4 characters is an accepted second check.)

Q: [6 marks] ★★ A product code has seven digits, 3926175, and is followed by a modulo-11 check digit calculated with the weights 8, 7, 6, 5, 4, 3, 2. (a) Calculate the check digit. [4] (b) A clerk types the six-digit code 891360, where the last digit is the check digit, using the weights 6, 5, 4, 3, 2, 1. Show that the code is not valid. [2]
H: For (b), multiply every digit including the last by its weight, add them, and test for a multiple of 11.
A: (a) The products are 24, 63, 12, 30, 4, 21 and 10 [M1]. The total is 164 [A1]. \(164 = 11 \times 14 + 10\), so the remainder is 10 [M1], and the check digit is \(11 - 10 = 1\) [A1].

(b) Multiply every digit, including the check digit, by its weight and add:

\[\begin{aligned} 8 \times 6 + 9 \times 5 + 1 \times 4 + 3 \times 3 + 6 \times 2 + 0 \times 1 &= 48 + 45 + 4 + 9 + 12 + 0 \\ &= 118 \end{aligned}\]

The total is 118 [M1]. \(118 = 11 \times 10 + 8\), which is not a multiple of 11, so the code is not valid [A1].

Q: [6 marks] ★★ (#cs.security) (a) The 7-bit ASCII code for `J` is 1001010. Write the byte that is transmitted using even parity, with the parity bit as the left-most bit. [2] (b) A system uses odd parity, with the parity bit as the left-most bit. It receives the bytes 01100111, 10110010, 11000001 and 00001011. State which byte contains an error and why. [2] (c) Explain why a parity check cannot detect every error. [2]
A: (a) The code has three 1s, an odd number, so the parity bit is 1 [B1] and the byte is **11001010** [B1].

(b) The byte 10110010 [B1] contains four 1s, which is an even number, but odd parity requires an odd number [B1]. (The other three bytes contain five, three and three 1s.)

(c) If two bits in the same byte are changed [B1], the number of 1s is still even (or still odd), so the byte still passes the check [B1].

Q: [8 marks] ★★★ (#cs.security) A block of four bytes is sent with a parity byte, using even parity with the parity bit as the left-most bit. The block received is shown. Bit 1 is the first bit to the right of the parity bit.

| Byte | Parity bit | Bit 1 | Bit 2 | Bit 3 | Bit 4 | Bit 5 | Bit 6 | Bit 7 |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 1 |
| 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 3 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 4 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| Parity byte | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |

(a) Identify the byte and the bit that contain the error, showing the checks you make. [3] (b) State the correct value of that byte. [1] (c) Explain why block parity can locate the error but a parity bit on each byte alone cannot. [2] (d) Describe one set of errors that block parity would **not** detect. [2]
H: Count the 1s in every row and every column. Exactly one row and one column should be odd.
A: (a) Byte 3 has three 1s (an odd number), so it fails the row check [B1]. In the columns, Bit 6 has one 1 (an odd number) while every other column has an even number [B1]. The error is in byte 3, Bit 6, where the failing row and column cross [B1].

(b) The bit is changed from 0 to 1, so byte 3 is 11000110 [B1].

(c) A parity bit on each byte only shows that the byte contains a wrong bit, not which of its bits [B1]. The extra column check means that the failing row and the failing column cross at one bit, which is the one that is wrong [B1].

(d) Four wrong bits at the corners of a rectangle, that is, two bits in each of two rows, in the same two columns [B1]. Every row and every column then still has an even number of 1s, so no check fails [B1].
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A modulo-11 check digit uses the weights \(w\) and \(w - 1\) for two neighbouring digits \(a\) (the left one) and \(b\) (the right one). A clerk swaps them. Show that the total changes by \(a - b\), and explain why this means a transposition is always detected, unless the two digits are equal.
H: Write the contribution of the two digits before and after the swap, then subtract.
H: What is the biggest that \(|a - b|\) can be? (A digit is 0 to 9; the check digit X counts as 10.)
A: Before the swap the two digits contribute \(a \times w + b \times (w - 1)\). After the swap they contribute \(b \times w + a \times (w - 1)\). [B1]

The difference (before minus after) is \(a w + b w - b - b w - a w + a = a - b\). So the total changes by exactly \(a - b\). [B1]

A valid code has a total that is a multiple of 11, so the changed total is still a multiple of 11 only if \(a - b\) is a multiple of 11. [B1]

The digits are 0 to 9 (or 10 for X), so \(a - b\) is between −10 and 10. The only multiple of 11 in that range is 0, so the total stays a multiple of 11 only if \(a = b\). [B1]

If \(a = b\) the swap changes nothing, so there is no error to detect. Any other swap makes the total not a multiple of 11, so the code is rejected. [B1]

Q: [5 marks] ★★★ A 4-digit code uses a modulo-10 check digit with the weights 1, 3, 1, 3 (left to right), and the check digit is \(10 - (\text{total} \bmod 10)\), or 0 if that gives 10. (a) Calculate the check digit for 4271 and for 4721. [3] (b) Explain what this shows about this check digit. [2]
H: The two codes differ only by a swap of two neighbouring digits, 2 and 7.
A: (a) For 4271: \(4 \times 1 + 2 \times 3 + 7 \times 1 + 1 \times 3 = 4 + 6 + 7 + 3 = 20\) [B1], and \(20 \bmod 10 = 0\), so the check digit is 0 [B1]. For 4721: \(4 + 7 \times 3 + 2 + 3 = 4 + 21 + 2 + 3 = 30\), and \(30 \bmod 10 = 0\), so the check digit is also 0 [B1].

(b) The two codes get the same check digit, so a swap of the neighbouring digits 2 and 7 is **not detected** [B1]. The weights 1 and 3 differ by 2, so swapping two digits that differ by 5 changes the total by \(2 \times 5 = 10\), a multiple of 10 [B1].
:::

:::quiz
? Which statement describes data privacy?
- Data is protected from being deleted by a fault.
+ A person decides how their personal information is collected and shared.
- The data is correct and complete.
- Data is stored in an encrypted form.
> Privacy is about control over personal information. Protection from deletion or damage is security, correctness is integrity, and encryption is one security measure.
? Which attack redirects a user who types the correct web address to a fake website?
- Phishing
- A virus
+ Pharming
- Spyware
> Pharming redirects the browser using malicious code or a changed DNS record. Phishing relies on a message that persuades the user to click.
? What does a firewall do?
- Scans files for known viruses and deletes them.
+ Examines data going into and out of a network and blocks data that does not meet its rules.
- Scrambles data so that only someone with a key can read it.
- Makes a copy of the files on another disk.
> Scanning for viruses is anti-virus, scrambling is encryption and copying files is back-up.
? A validation check shows that an age of 150 is not allowed. Which type of check is most likely?
- Presence check
- Existence check
+ Range check
- Check digit
> A range check tests that a value lies between limits. A presence check only tests that something has been entered.
? A pupil types a mark of 41 instead of 14. Both are inside the allowed range of 0 to 50. Which check could detect the mistake?
- A range check
- A format check
+ Double entry
- A length check
> The value is reasonable, so validation cannot see it is wrong. Typing the data twice and comparing the two entries (verification) shows that they differ.
? A byte is sent using even parity. The receiver gets 10110100. What does the receiver conclude?
- The byte is correct, because it has four 1s.
+ The byte is correct, because it has an even number of 1s.
- The byte contains an error, because it has an even number of 1s.
- The byte contains an error, because it has an odd number of 1s.
> 10110100 has four 1s, an even number, so it passes an even parity check. (The byte could still contain two wrong bits.)
? Which error can block parity find and correct?
- Two bits changed in the same byte.
+ One bit changed anywhere in the block.
- Four bits changed at the corners of a rectangle.
- Two bytes swapped over.
> One wrong bit makes one row and one column fail, so the bit where they cross is located and can be flipped. The other errors are not located, and the last two are not even detected.
? What does the check digit X represent in a modulo-11 code?
- The remainder was 0.
- The remainder was 11.
+ The check digit calculated was 10, which cannot be written as one digit.
- The code is not valid.
> A check digit of \(11 - \text{remainder}\) can be 10 when the remainder is 1. Writing 10 would take two characters, so the letter X is used.
? Which statement about encryption is correct?
- It stops a hacker from copying data sent over a network.
- It removes viruses from files.
+ It makes data unreadable to anyone without the key.
- It proves who sent a message.
> Intercepted encrypted data is still there, but it is scrambled. Proving who sent a message is the job of a digital signature.
:::

:::checklist What you can now do
- [ ] I can explain the difference between data security, data privacy and data integrity, with an example of each.
- [ ] I can explain why data and the system need protecting.
- [ ] I can describe the threats: hackers, malware (viruses and spyware), phishing and pharming, and how each works.
- [ ] I can describe how user accounts and passwords, authentication (digital signatures, biometrics), firewalls, anti-virus, anti-spyware, encryption and access rights protect data and systems.
- [ ] I can choose measures for a scenario, from a stand-alone computer to a network, and say how each restricts the risk.
- [ ] I can explain the difference between validation and verification, and why validation cannot prove data is correct.
- [ ] I can choose and write a range, limit, length, presence, format or existence check for a field.
- [ ] I can calculate and verify a modulo-11 check digit, including the X case.
- [ ] I can describe visual checks and double entry as verification during data entry.
- [ ] I can calculate parity bits, find an error with a parity block, and calculate and check a checksum, and say what each can and cannot detect.
:::

:::recap
- Security protects data from unauthorised access and damage; privacy is a person's control over their personal data; integrity is accuracy and completeness.
- Threats: hackers; malware, including viruses (copy themselves into files) and spyware (secretly record and send data); phishing (a message persuades you to use a fake site); pharming (you are redirected to a fake site even though you typed the right address).
- Protections: user accounts and strong passwords, authentication (something you know, have or are; biometrics; digital signatures), firewall, anti-virus, anti-spyware, encryption (data unreadable without the key), access rights (read, write, execute, by user or group), back-ups.
- Validation checks that data is reasonable, using range, limit, length, presence, format, existence and check digit checks. It cannot prove data is correct. Verification checks that data was copied accurately: visual check, double entry.
- Modulo-11 check digit: weights \(n + 1\) down to 2, total, remainder after dividing by 11, check digit \(11 - \text{remainder}\) (remainder 0 gives 0; 10 is written X). To verify, give the check digit weight 1; the total must be a multiple of 11. It detects any single wrong digit and any swap of neighbours.
- Parity bit: makes the count of 1s even (even parity) or odd (odd parity); detects an odd number of flipped bits in a byte. Block parity adds a parity byte; one failing row and one failing column locate a single wrong bit. Checksum: total of the bytes modulo 256, recalculated by the receiver.
:::

:::links
- practise: [Data security: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/6-security-privacy-and-data-integrity-/data-security/exam-questions/) · Save My Exams · 9618-style questions on threats and protection [paid]
- practise: [Data integrity: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/6-security-privacy-and-data-integrity-/data-integrity/exam-questions/) · Save My Exams · validation, verification, parity and check digit questions [paid]
- read: [Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography) · Khan Academy · from simple ciphers to public keys, free
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on security, passwords and how attacks work
- read: [ZNotes: 9618 AS notes](https://znotes.org/caie/as-level/computer-science-9618/) · ZNotes · free summary notes for the AS course

Links checked 13 November 2026.
:::

Next: [Ethics, ownership and the impact of AI](#cs.ethics)
