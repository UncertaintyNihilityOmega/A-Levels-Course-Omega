@chapter cs.data
@title Number systems and binary arithmetic
@level as
@paper CAIE 9618 Paper 1
@time 6–8 hours
@summary How a computer stores whole numbers and text as bits: binary, denary and hexadecimal, binary-coded decimal, one's and two's complement for negative numbers, binary addition and subtraction with overflow, the binary and decimal size prefixes, and the character sets ASCII and Unicode.

:::why
Everything a computer holds, from a photo to a bank balance to this sentence, is stored as patterns of 0s and 1s. If you can move between binary, denary and hexadecimal, add in binary and say what happens when a result does not fit, you understand what the processor actually works with. Paper 1 asks for these skills with no calculator, so every method in this chapter is one you can do by hand.
:::

**Before you start**, you should be able to run a short Python program and use `print`, from [Programming from zero](#cs.f.basics). The Python boxes in this chapter are for checking your answers; in the exam you work by hand.

:::try Warm-up
Q: What does `print(23 // 4, 23 % 4)` display? (from [Programming from zero](#cs.f.basics))
A: It displays `5 3`. `//` is whole-number division (23 ÷ 4 = 5 remainder 3) and `%` gives the remainder.
Q: What does `print(2 ** 4)` display? In Python, `**` means "to the power of". (from [Programming from zero](#cs.f.basics))
A: It displays `16`, because \(2^4 = 2 \times 2 \times 2 \times 2 = 16\).
Q: What does `print("3" + "4")` display, and why is it not 7? (from [Programming from zero](#cs.f.basics))
A: It displays `34`. The quotation marks make these strings (text), and `+` joins text instead of adding numbers.
:::

:::note How code appears in this course
Python blocks are Python 3 and have been run: the block after a program, introduced by "Output:", is exactly what it prints. Pseudocode follows the Cambridge Pseudocode Guide for 2027–2029. Binary patterns are written as strings of 0s and 1s with every bit shown: write all 8 bits in an 8-bit answer, including leading zeros.
:::

## Why computers use binary

A processor is built from billions of tiny electronic switches. A switch is either off or on, and it is easy to tell the two apart reliably, even when there is a little electrical noise. Binary uses exactly two symbols, 0 and 1, so each switch (or each small region of a memory chip, a disc or a wire) can hold one of them. Any value, however large, is stored as a pattern of these two states.

:::def Bit
A binary digit: the smallest unit of data in a computer, with the value 0 or 1.
:::

:::def Byte
A group of 8 bits. It is the unit in which memory sizes are counted.
:::

:::def Nibble
A group of 4 bits, half a byte. One nibble holds one hexadecimal digit or one binary-coded decimal digit.
:::

:::def Binary
The base 2 number system. It has two digits, 0 and 1, and each place is worth twice the place to its right.
:::

:::def Denary
The base 10 number system we use every day, with the digits 0 to 9. Each place is worth ten times the place to its right. (Also called decimal.)
:::

A group of \(n\) bits can form \(2^n\) different patterns, because each extra bit doubles the number of possibilities. One bit gives 2 patterns, 8 bits give \(2^8 = 256\), and 16 bits give \(2^{16} = 65\,536\).

### Place values

In denary the number 253 means 2 hundreds, 5 tens and 3 ones: the place values are 100, 10 and 1, each ten times the one to its right. Binary works the same way with 2 instead of 10. Reading from the right, the place values of an 8-bit number are:

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Power of 2 | \(2^7\) | \(2^6\) | \(2^5\) | \(2^4\) | \(2^3\) | \(2^2\) | \(2^1\) | \(2^0\) |

The left-hand bit is the **most significant bit** (MSB) because it is worth the most; the right-hand bit is the **least significant bit** (LSB). Counting in binary follows the same pattern as counting in denary: when a place reaches its largest digit, it returns to 0 and the next place increases by one.

| Denary | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Binary | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 |

The largest unsigned value in 8 bits is 11111111, which is \(128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255\), that is \(2^8 - 1\). In general, \(n\) unsigned bits hold the values 0 to \(2^n - 1\).

## Binary and decimal prefixes

Memory and file sizes are quoted in kilobytes, megabytes and so on, but there are two different meanings in use, and the exam expects you to know both.

:::def Kibibyte (and the other binary prefixes)
A kibibyte (KiB) is \(2^{10} = 1024\) bytes. The binary prefixes are based on powers of 2: kibi (\(2^{10}\)), mebi (\(2^{20}\)), gibi (\(2^{30}\)) and tebi (\(2^{40}\)).
:::

:::def Kilobyte (and the other decimal prefixes)
A kilobyte (kB) is \(10^3 = 1000\) bytes. The decimal prefixes are based on powers of 10: kilo (\(10^3\)), mega (\(10^6\)), giga (\(10^9\)) and tera (\(10^{12}\)).
:::

| Binary prefix | Symbol | Bytes | Decimal prefix | Symbol | Bytes |
|---|---|---|---|---|---|
| kibi | KiB | \(2^{10}\) = 1 024 | kilo | kB | \(10^{3}\) = 1 000 |
| mebi | MiB | \(2^{20}\) = 1 048 576 | mega | MB | \(10^{6}\) = 1 000 000 |
| gibi | GiB | \(2^{30}\) = 1 073 741 824 | giga | GB | \(10^{9}\) = 1 000 000 000 |
| tebi | TiB | \(2^{40}\) = 1 099 511 627 776 | tera | TB | \(10^{12}\) = 1 000 000 000 000 |

Each binary step multiplies by 1024 (or \(2^{10}\)), so 1 MiB = 1024 KiB and 1 GiB = 1024 MiB. Each decimal step multiplies by 1000. The binary unit is always a little bigger than the matching decimal unit: a gibibyte is about 7% more than a gigabyte.

:::key Converting sizes
- To go **down** a unit (MiB to KiB, GiB to MiB), multiply by 1024. To go **up** a unit, divide by 1024.
- Use the same rule with 1000 for the decimal units.
- Use the prefix the question uses. If a question says "KiB", use 1024; if it says "kB", use 1000. If it says both, convert each exactly and say which you used.
- 1 byte = 8 bits, so bits to bytes is a division by 8.
:::

:::eg Why a 500 GB drive shows less than 500 GiB
A shop in Accra sells a drive labelled "500 GB". The computer reports its capacity in gibibytes. Explain why the computer shows a number smaller than 500 and calculate it.

The maker uses the decimal prefix, so the drive holds \(500 \times 10^9\) bytes. [B1] The computer counts in binary units, and one gibibyte is \(2^{30} = 1\,073\,741\,824\) bytes, a larger unit than the gigabyte, so the same number of bytes is a smaller number of gibibytes. [B1]

\[ \frac{500 \times 10^9}{2^{30}} = \frac{500\,000\,000\,000}{1\,073\,741\,824} \approx 465.7 \text{ GiB} \]

The drive has not lost any space. Two different units are being used for the same number of bytes. (An exam would not ask for the division by hand: it asks for the reason.)
:::

:::eg Converting between binary-prefix units
A video file is 3 MiB. State its size in bytes. A different file is 8192 KiB: state its size in MiB.

\(3 \text{ MiB} = 3 \times 2^{20} = 3 \times 1\,048\,576 = 3\,145\,728\) bytes. [B1]

\(8192 \text{ KiB} \div 1024 = 8\) MiB. [B1] (Check: \(8192 = 8 \times 1024\), and \(1024 = 2^{10}\) is exactly the step from KiB to MiB.)
:::

## Converting between denary and binary

### Binary to denary

Write the place values over the bits, then add the place values that have a 1.

:::eg Binary to denary
Convert 10101101 to denary.

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Bit | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |

\(128 + 32 + 8 + 4 + 1 = 173\). [B1]
:::

### Denary to binary

There are two reliable methods. Use whichever you find easier, and check one with the other.

**Method 1: place values.** Go along the place values from the left. If the place value fits into what is left, write 1 and subtract it; otherwise write 0.

**Method 2: repeated division by 2.** Divide the number by 2, write down the remainder (0 or 1), divide the whole-number answer by 2 again, and carry on until the answer is 0. The remainders, **read from the last to the first**, are the binary number.

:::eg Denary to binary, both ways
Convert 173 to 8-bit binary.

Method 1: 173 ≥ 128, so write 1, leaving 45. 45 < 64, write 0. 45 ≥ 32, write 1, leaving 13. 13 < 16, write 0. 13 ≥ 8, write 1, leaving 5. 5 ≥ 4, write 1, leaving 1. 1 < 2, write 0. 1 ≥ 1, write 1, leaving 0. The pattern is 10101101. [B1]

Method 2:

| Division | Whole-number answer | Remainder |
|---|---|---|
| 173 ÷ 2 | 86 | 1 |
| 86 ÷ 2 | 43 | 0 |
| 43 ÷ 2 | 21 | 1 |
| 21 ÷ 2 | 10 | 1 |
| 10 ÷ 2 | 5 | 0 |
| 5 ÷ 2 | 2 | 1 |
| 2 ÷ 2 | 1 | 0 |
| 1 ÷ 2 | 0 | 1 |

The remainders from the bottom up are 1, 0, 1, 0, 1, 1, 0, 1, so the number is 10101101, the same as before. [B1]
:::

:::warn Fixed width means all the bits
If the question says "8-bit", the answer has eight digits. The number 5 is 00000101, not 101. Pad on the left with zeros. Leaving the zeros off can lose the mark, and for negative numbers it changes the meaning completely.
:::

The division method is itself an algorithm, and Paper 2 may ask you to write it. In pseudocode, using the `MOD`, `DIV`, `NUM_TO_STR` and `&` (join) operations from the insert:

```pseudocode
DECLARE Number : INTEGER
DECLARE Bits : STRING

INPUT Number
Bits ← ""
WHILE Number > 0
   Bits ← NUM_TO_STR(Number MOD 2) & Bits
   Number ← Number DIV 2
ENDWHILE
OUTPUT Bits
```

Each remainder is joined on the **left** of the string, which is the same as reading the remainders from the last to the first. A trace for the input 13:

| Number | Bits | OUTPUT |
|---|---|---|
| 13 | "" | |
| | "1" | |
| 6 | | |
| | "01" | |
| 3 | | |
| | "101" | |
| 1 | | |
| | "1101" | |
| 0 | | |
| | | 1101 |

The same algorithm in Python:

```python
number = 13
bits = ""
while number > 0:
    bits = str(number % 2) + bits
    number = number // 2
print(bits)
```

Output:

```output
1101
```

The loop gives an empty string for the input 0, so a complete program treats 0 as a special case.

### Checking with Python

Python has functions for these conversions. They are for checking your hand working, not for the exam. `bin()` gives a string starting `0b`; `format(n, "08b")` gives exactly 8 bits; `int(text, 2)` converts a binary string to a number.

```python
number = 173
print(bin(number), format(number, "08b"))
print(hex(number), format(number, "X"))
print(int("10101101", 2), int("AD", 16))
print(ord("A"), chr(66))
```

Output:

```output
0b10101101 10101101
0xad AD
173 173
65 B
```

## Hexadecimal

Long binary numbers are hard to read and easy to copy wrongly: a student can lose a digit in 1010110111110010 without noticing. Hexadecimal fixes this. It is base 16, so it needs 16 digits: 0 to 9, then the letters A to F for ten to fifteen.

:::def Hexadecimal
The base 16 number system. It uses the digits 0 to 9 and the letters A to F (A = 10, B = 11, C = 12, D = 13, E = 14, F = 15). Each place is worth 16 times the place to its right.
:::

| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| Denary | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Binary | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 |

| Hex | 8 | 9 | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|---|
| Denary | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| Binary | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

The key fact is that **one hexadecimal digit is exactly one nibble**: 16 = \(2^4\), so 4 bits cover exactly the 16 values of a hex digit. That makes conversion between binary and hex a matter of grouping, with no arithmetic.

:::key Binary and hexadecimal
- **Binary to hex:** split the bits into groups of 4 starting from the **right** (add zeros on the left if the last group is short), then replace each group by its hex digit.
- **Hex to binary:** replace each hex digit by its 4 bits.
- **Hex to denary:** multiply each digit by its place value (…, 256, 16, 1) and add. **Denary to hex:** divide by 16 repeatedly (remainders are the digits, read from last to first), or convert to binary and group.
:::

:::eg Binary, hex and denary
(a) Convert 10101101 to hexadecimal. (b) Convert 3F9 to binary and to denary. (c) Convert 205 to hexadecimal.

(a) Groups of 4: 1010 and 1101. 1010 is 10, which is A; 1101 is 13, which is D. The answer is **AD**. [B1] (Check: \(10 \times 16 + 13 = 173\), which is the value of 10101101.)

(b) 3 is 0011, F is 1111 and 9 is 1001, so 3F9 is **0011 1111 1001**. [B1] In denary: \(3 \times 256 + 15 \times 16 + 9 \times 1 = 768 + 240 + 9 = 1017\). [B1]

(c) \(205 \div 16 = 12\) remainder 13. 12 is C and 13 is D, so 205 is **CD**. [B1] (Check: \(12 \times 16 + 13 = 205\).)
:::

### Why hexadecimal is used

Hexadecimal is a shorthand for binary. It is not a different way for the computer to store data: the computer still holds bits. People use hex because:

- it is shorter than binary: one hex digit stands for 4 bits, so an 8-bit byte is two digits and a 32-bit number is eight;
- it is quicker to read and easier to copy without mistakes than a long string of 0s and 1s;
- it converts to and from binary easily, with no calculation.

Typical uses:

| Use | Example | Why hex suits it |
|---|---|---|
| Colour codes in web pages | `#FF8000` is red FF, green 80, blue 00 | each colour is one byte, so two hex digits |
| Memory addresses | `0x7FFE` in a debugger | addresses are long binary numbers |
| MAC addresses | `3C:52:82:1A:9F:07` (12 hex digits) | the 48-bit address is much shorter in hex |
| Error and status codes | a fault report that shows `0x1A4F` | short, and easy to quote to a support team |
| Machine code and assembly | `&4A` in assembly language | shows each byte compactly |

For the colour `#FF8000`: FF is 255 (full red), 80 is 128 (about half green) and 00 is 0 (no blue), which is orange. Each of the three bytes can be 0 to 255, so a 24-bit colour code can describe \(2^{24} = 16\,777\,216\) colours.

:::warn Reading hex
Hex digits A to F are digits, not variables: B is eleven, not "the letter B". Always write them in capitals in this course, and do not confuse the hex number 10 (which is sixteen) with denary ten. In an answer, say which base you mean if there is any doubt (for example "AD in hexadecimal").
:::

## Binary-coded decimal (BCD)

Some devices need to show a denary number digit by digit: a clock face, a till display, a calculator. Converting a pure binary number back into separate denary digits needs division. **Binary-coded decimal** avoids that by storing each denary digit separately in its own nibble.

:::def Binary-coded decimal (BCD)
A way of storing a denary number in which each denary digit (0 to 9) is stored as its own 4-bit binary code. The digits 0000 to 1001 are valid; the patterns 1010 to 1111 are not used.
:::

To encode a number, write each denary digit as 4 bits and keep the digits in order. To decode, read each nibble as one digit.

:::eg Encoding and decoding BCD
(a) Write 2057 in BCD. (b) Decode 1001 0111 0011 as a denary number. (c) Compare with ordinary binary.

(a) 2 → 0010, 0 → 0000, 5 → 0101, 7 → 0111. The BCD is **0010 0000 0101 0111**. [B1]

(b) 1001 is 9, 0111 is 7 and 0011 is 3, so the number is **973**. [B1]

(c) The number 59 in BCD is 0101 1001 (digits 5 and 9). In ordinary binary 59 is 00111011. They are different patterns, so a BCD value must never be read as binary: 0101 1001 read as binary would be 89. [B1]
:::

If two BCD digits are stored in one byte (called **packed** BCD), one byte can store 00 to 99. Ordinary binary in the same byte stores 0 to 255. So BCD uses more bits for the same range: the cost is some wasted space (the patterns 1010 to 1111 are never used), and arithmetic is harder.

:::key Uses of BCD
- Digital displays, clocks and watches, and calculators: each digit goes straight to one display character, with no conversion.
- Money values, where every denary digit must be held exactly, for example a till showing 12.50.
- Any device that mostly shows numbers rather than calculating with them.
:::

:::warn BCD is not binary
BCD is a code for denary digits, and each nibble stands for one digit. The nibble 1010 is **not valid** BCD, because there is no denary digit ten. A pattern such as 0001 0010 is 12 in BCD but 18 in binary. State which one a question means.
:::

## Negative numbers: one's and two's complement

So far every number has been unsigned (zero or positive). To store negative integers we need a way of showing the sign inside the bits. This syllabus uses two methods, both built on the idea of "flipping" bits.

:::def One's complement
A way of representing a negative integer: take the binary pattern of the positive number and invert every bit (0 becomes 1 and 1 becomes 0). The left-hand bit is 1 for a negative number.
:::

In 8-bit one's complement, 25 is 00011001 and −25 is 11100110. The method is easy, but it has two problems: there are **two zeros** (00000000 is +0 and 11111111 is −0), and adding needs an extra correction step. For those reasons computers use two's complement.

:::def Two's complement
A way of representing signed integers in which the most significant bit has a negative place value. For an \(n\)-bit number that bit is worth \(-2^{n-1}\) (in 8 bits, −128) and every other bit has its usual positive place value. To negate a number, invert all the bits and add 1.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 330 148" role="img" aria-label="The eight place values of an 8-bit two's complement number: minus 128, 64, 32, 16, 8, 4, 2 and 1. Below them is the bit pattern 1 0 1 1 0 1 1 1, with the left-hand bit marked as the sign bit. The sum shown is minus 128 plus 32 plus 16 plus 4 plus 2 plus 1, which equals minus 73."><text class="tl ti" x="21" y="16">Place values, 8-bit two's complement</text><rect class="f1 s-acc sw2" x="21" y="26" width="36" height="36"/><text class="tl tc tb" x="39" y="48" style="font-size:10.5px">−128</text><rect class="fm s-acc sw2" x="57" y="26" width="36" height="36"/><text class="tl tc" x="75" y="49">64</text><rect class="fm s-acc sw2" x="93" y="26" width="36" height="36"/><text class="tl tc" x="111" y="49">32</text><rect class="fm s-acc sw2" x="129" y="26" width="36" height="36"/><text class="tl tc" x="147" y="49">16</text><rect class="fm s-acc sw2" x="165" y="26" width="36" height="36"/><text class="tl tc" x="183" y="49">8</text><rect class="fm s-acc sw2" x="201" y="26" width="36" height="36"/><text class="tl tc" x="219" y="49">4</text><rect class="fm s-acc sw2" x="237" y="26" width="36" height="36"/><text class="tl tc" x="255" y="49">2</text><rect class="fm s-acc sw2" x="273" y="26" width="36" height="36"/><text class="tl tc" x="291" y="49">1</text><text class="tl tc tb" x="39" y="86">1</text><text class="tl tc" x="75" y="86">0</text><text class="tl tc" x="111" y="86">1</text><text class="tl tc" x="147" y="86">1</text><text class="tl tc" x="183" y="86">0</text><text class="tl tc" x="219" y="86">1</text><text class="tl tc" x="255" y="86">1</text><text class="tl tc" x="291" y="86">1</text><text class="tl tc" x="39" y="108">sign bit</text><text class="tl tc tb" x="165" y="134">−128 + 32 + 16 + 4 + 2 + 1 = −73</text></svg><figcaption>The pattern 10110111 in 8-bit two's complement. The left-hand bit is worth −128, so a 1 there makes the number negative. The other seven bits add 32 + 16 + 4 + 2 + 1 = 55, giving −128 + 55 = −73.</figcaption></figure>
:::

The place-value view explains the range. With \(n\) bits, the smallest number has only the MSB set, \(-2^{n-1}\); the largest has every bit except the MSB set, \(2^{n-1} - 1\).

:::key Range of an n-bit two's complement integer
From \(-2^{n-1}\) to \(2^{n-1} - 1\). In 8 bits that is −128 to 127; in 16 bits it is −32 768 to 32 767. There is **one** zero (all bits 0), and one more negative value than positive. If the MSB is 1, the number is negative.
:::

### Converting both ways

:::steps
1. **Denary to two's complement.** If the number is positive, write its ordinary binary with the MSB 0. If it is negative, write the binary of the **positive** value (in the full width), invert every bit, then add 1.
2. **Two's complement to denary.** If the MSB is 0, read it as ordinary binary. If the MSB is 1, either add the place values with the MSB counted as −128 (the figure), or invert the bits, add 1 and put a minus sign in front of the result.
:::

:::eg Two's complement in an exam question
A sensor in a cold store in Nairobi sends each temperature, in °C, as an 8-bit two's complement integer.

(a) Show how the temperature −19 is sent. (b) Write that pattern in hexadecimal. (c) The sensor sends 11110110. What temperature is that? (d) State the lowest temperature the sensor can send.

(a) 19 is 00010011. [B1] Invert the bits: 11101100. Add 1: **11101101**. [B1] (Check: \(-128 + 64 + 32 + 8 + 4 + 1 = -19\).)

(b) Split into 1110 and 1101, which are E and D, so the pattern is **ED**. [B1]

(c) The MSB is 1, so the number is negative. Using place values: \(-128 + 64 + 32 + 16 + 4 + 2 = -10\). [M1] [A1] The temperature is **−10 °C**. (Check by the other method: invert 11110110 to get 00001001, add 1 to get 00001010 = 10, so the value is −10.)

(d) The lowest value has only the MSB set, 10000000, which is **−128 °C**. [B1]
:::

Try the widget, and use it to check your own working. Enter a denary number or a binary or hexadecimal string, change the number of bits, and see every representation. Then try a number that is too big for the number of bits.

:::html
<div class="widget" data-w="cs-binary" data-bits="8" data-value="-37" data-mode="convert"></div>
:::

:::warn The two common slips
- **Forgetting the +1.** Inverting alone gives one's complement. For −45 the inverted pattern 11010010 is *not* the answer; adding 1 gives 11010011.
- **Starting from the negative number.** Always write the pattern of the **positive** value first (45, not −45), then invert and add 1, once.
:::

Whenever you have an answer, check it with the place values: add the 1-bits, counting the left-hand bit as −128. It takes ten seconds and catches both slips.

```python
def to_twos(value, bits):
    return format(value & (2 ** bits - 1), "0" + str(bits) + "b")


def from_twos(pattern):
    value = int(pattern, 2)
    if pattern[0] == "1":
        value = value - 2 ** len(pattern)
    return value


print(to_twos(-59, 8), to_twos(59, 8))
print(from_twos("11000101"), from_twos("01011101"))
```

Output:

```output
11000101 00111011
-59 93
```

`value & (2 ** bits - 1)` keeps only the lowest `bits` bits of the number, which for a negative number gives exactly its two's complement pattern.

## Binary addition

Binary addition follows the same column method as denary addition, but there are only four cases in each column, because a column can only hold 0 or 1 and anything bigger carries to the next column.

| Column sum | Write | Carry |
|---|---|---|
| 0 + 0 | 0 | 0 |
| 0 + 1 or 1 + 0 | 1 | 0 |
| 1 + 1 | 0 | 1 |
| 1 + 1 + 1 (with a carry in) | 1 | 1 |

(1 + 1 = 10 in binary: write 0, carry 1. 1 + 1 + 1 = 11: write 1, carry 1.) Work from the right, one column at a time, writing the carry above the next column.

:::eg Adding two 8-bit numbers
Add 00101101 and 01001110, and check in denary.

The carries are written above the column they go into.

```text
carries   00011000
          00101101
        + 01001110
        ----------
          01111011
```

The result is 01111011. [B1] Check: 00101101 is 45, 01001110 is 78 and 01111011 is 123, and \(45 + 78 = 123\). [B1]
:::

### Subtraction: add the two's complement

A processor does not need a separate subtraction circuit. To work out \(A - B\), it adds \(A\) to the two's complement of \(B\), which is \(-B\). If the addition produces a **carry out** of the left-hand column, that extra bit is discarded, because the result must stay within the same number of bits.

:::steps
1. Write both numbers in the full number of bits.
2. Find the two's complement of the number being subtracted (invert, add 1).
3. Add it to the first number.
4. Discard any carry out of the leftmost column. The answer is the remaining bits.
:::

:::eg Subtracting with two's complement
Work out 93 − 58 in 8 bits.

93 is 01011101 and 58 is 00111010. [B1] Invert 58: 11000101, add 1 to get −58 as **11000110**. [B1]

```text
carries   10111000
          01011101
        + 11000110
        ----------
        1 00100011
```

The carry out of the left-hand column (the 1 on the left) is discarded, leaving 00100011. [B1] This is \(32 + 2 + 1 = 35\), and \(93 - 58 = 35\). [B1]
:::

## Overflow

An 8-bit register can only hold 8 bits. If the true answer needs more, the register holds the wrong value.

:::def Overflow
An error that occurs when the result of a calculation is too large (or too small) to be stored in the number of bits available.
:::

How you recognise overflow depends on how the bits are interpreted.

- **Unsigned numbers.** The range is 0 to 255. If the addition produces a carry out of the leftmost column, the real answer is 256 or more and the 8 bits hold the wrong value.
- **Two's complement (signed) numbers.** The range is −128 to 127. Overflow has happened when **two positive numbers give a negative result**, or **two negative numbers give a positive result**. Adding numbers of opposite signs can never overflow.

:::eg Three additions in 8 bits
(a) Add 100 and 50 as two's complement numbers. (b) Add −100 and −50. (c) Add 200 and 100 as unsigned numbers.

(a) 100 is 01100100 and 50 is 00110010.

```text
carries   11000000
          01100100
        + 00110010
        ----------
          10010110
```

The result 10010110 has MSB 1, so it reads as \(-128 + 16 + 4 + 2 = -106\). Two positive numbers have given a negative result, so **overflow has occurred**: the true answer, 150, is larger than 127. [B1]

(b) −100 is 10011100 and −50 is 11001110.

```text
carries   00111000
          10011100
        + 11001110
        ----------
        1 01101010
```

The carry out is discarded, leaving 01101010, which is +106. Two negative numbers have given a positive result, so **overflow has occurred**: the true answer, −150, is smaller than −128. [B1]

(c) 200 is 11001000 and 100 is 01100100.

```text
carries   10000000
          11001000
        + 01100100
        ----------
        1 00101100
```

There is a carry out of the leftmost column. The 8 bits hold 00101100 = 44, but \(200 + 100 = 300\), which needs 9 bits. **Unsigned overflow has occurred.** [B1]
:::

:::warn A carry out is not always an overflow
Adding −1 and −1 in two's complement gives 11111111 + 11111111 = 1 11111110. There is a carry out, but the 8 bits that remain, 11111110, are −2, the correct answer. There is **no overflow**: two negative numbers gave a negative result. For signed numbers, look at the signs, not at the carry out. For unsigned numbers, the carry out is the sign of overflow.
:::

:::exam Saying what overflow is
"The result is too big" earns less than "the result needs more bits than are available in the register, so the stored value is wrong". If a question asks you to identify overflow, name the signs: "two positive numbers gave a negative result".
:::

What happens in a real program when overflow occurs? That depends on the processor and language: the stored result may be wrong without any warning, or the processor may set a flag that software can test. The exam only asks you to recognise it and explain why it happens.

```python
def add_signed(a, b, bits=8):
    result = (a + b) & (2 ** bits - 1)
    if result >= 2 ** (bits - 1):
        signed = result - 2 ** bits
    else:
        signed = result
    return format(result, "0" + str(bits) + "b"), signed, signed != a + b


print(add_signed(100, 50))
print(add_signed(-1, -1))
```

Output:

```output
('10010110', -106, True)
('11111110', -2, False)
```

The third value is `True` when the stored answer differs from the true answer, which is exactly overflow.

## Character sets: ASCII and Unicode

Text is stored as numbers. Each character (a letter, digit, punctuation mark or symbol) is given a unique number, called its **character code**, and the code is stored in binary.

:::def Character set
The set of characters a computer system can recognise and represent, each with its own unique binary code.
:::

:::def ASCII
The American Standard Code for Information Interchange: a character set that uses 7 bits per character, so it can represent 128 different characters (letters, digits, punctuation and control codes). Extended ASCII uses 8 bits, so it can represent 256 characters.
:::

:::def Unicode
A character set that gives a unique code to the characters of nearly all the world's writing systems, as well as symbols and emoji. It uses more bits per character than ASCII (an encoding can use 8, 16 or 32 bits per character), so it can represent far more characters.
:::

The codes of ASCII are arranged in order, so you can calculate with them. The code of 'A' is 65 and the capital letters follow in order: 'B' is 66, 'C' is 67, up to 'Z'. The lower-case letters are in order too, starting at 'a' = 97, so each lower-case letter is exactly 32 more than its capital. The digit characters '0' to '9' are 48 to 57. You do not need to memorise the codes: a question gives the ones you need, as the pseudocode `ASC` example in the insert does.

:::warn The code for '7' is not 7
The character '7' is stored using the code 55 in ASCII, not the number 7. The digit characters have codes in order, so '7' is 7 more than '0' (48 + 7 = 55). A program that reads a digit typed at the keyboard must subtract the code of '0' to get its value. In Python, `ord("7")` is 55 and `int("7")` is 7.
:::

:::eg Using the order of the codes
In ASCII the character 'A' has the code 65. (a) What is the code of 'F'? (b) Which character has the code 69? (c) How many bits are needed to store the word "HELLO" in extended ASCII?

(a) 'F' is 5 letters after 'A', so its code is \(65 + 5 = 70\). [B1]

(b) \(69 - 65 = 4\), so it is the letter 4 after 'A': 'E'. [B1]

(c) 5 characters at 8 bits each is \(5 \times 8 = 40\) bits (5 bytes). [B1]
:::

### Why Unicode?

ASCII has only 128 characters (256 in extended ASCII), enough for English, but not for Arabic, Chinese, Hindi, accented letters in many European languages, or emoji. Different countries once used different extended sets, so the same code could show different letters on different computers. Unicode solves this with one set that covers all of them. The first 128 Unicode codes match ASCII, so plain English text is unchanged.

The cost is size. In one common Unicode encoding (UTF-8), the ASCII characters take one byte and others take two, three or four bytes, so a text in a script such as Hindi needs more storage than the same number of characters in ASCII. Other encodings use 16 or 32 bits for every character.

```python
word = "Lagos"
print([ord(letter) for letter in word])
print(len(word.encode("utf-8")), len("é".encode("utf-8")), len("€".encode("utf-8")))
```

Output:

```output
[76, 97, 103, 111, 115]
5 2 3
```

:::analogy
A character set is like a phrase book in which every phrase has a page number. Sending the page number is enough, as long as both sides own the same book. ASCII is a small book. Unicode is a huge one that every country shares.
:::

:::board
Cambridge 9618 asks you to describe ASCII, extended ASCII and Unicode and to explain why Unicode is used, but never to remember a particular code: a question gives any codes you need. AQA A Level Computer Science (7517) expects the same ideas, and its on-screen Paper 1 includes questions that use a skeleton program released before the exam.
:::

:::eg Spot the error: two's complement
Question: Show how the number −45 is stored as an 8-bit two's complement integer. [3 marks]

A student wrote:

```text
01  45 = 00101101
02  Invert the bits: 11010010
03  The answer is 11010010
```

Line 01 writes the positive value correctly in 8 bits [B1]. Line 02 inverts every bit correctly [B1]. **Line 03 stops too early: the student has found the one's complement and has not added 1** [B0]. The answer scores 2 out of 3.

The fix is one more line: \(11010010 + 1 = 11010011\). The check shows the difference: 11010011 gives \(-128 + 64 + 16 + 2 + 1 = -45\), but the student's answer gives \(-128 + 64 + 16 + 2 = -46\). A place-value check takes ten seconds and catches this slip every time.
:::

:::eg Spot the error: overflow
Question: Add 11111111 and 11111111, both 8-bit two's complement integers, and state whether overflow occurs. [4 marks]

A student wrote:

```text
01  11111111 + 11111111 = 1 11111110
02  The 8-bit result is 11111110
03  There is a carry out of the left-hand column, so overflow has occurred
04  The result is wrong because the true answer needs 9 bits
```

Line 01 shows the addition correctly [B1]. Line 02 keeps 8 bits and discards the carry out [B1]. **Line 03 confuses a carry out with overflow** [B0]. **Line 04 gives a reason for a conclusion that is wrong** [B0]. The answer scores 2 out of 4.

The correct reasoning: 11111111 is −1 in two's complement, so the sum is \(-1 + -1 = -2\), and 11111110 is −2. Two negative numbers have given a negative result, so there is **no overflow**.
:::

:::try Start easy, finish at exam standard
Q: How many different patterns can 10 bits form, and what is the largest unsigned value?
A: \(2^{10} = 1024\) patterns. The values run from 0 to \(2^{10} - 1 = 1023\).
Q: Convert 106 to 8-bit binary.
A: 106 = 64 + 32 + 8 + 2, so the bits are 01101010.
Q: Convert 11010110 to denary.
A: \(128 + 64 + 16 + 4 + 2 = 214\).
Q: Convert 10111100 to hexadecimal and 7E to 8-bit binary.
A: 1011 is B and 1100 is C, so 10111100 is BC. 7 is 0111 and E is 1110, so 7E is 01111110.
Q: Convert 2F to denary and 255 to hexadecimal.
A: \(2 \times 16 + 15 = 47\). \(255 \div 16 = 15\) remainder 15, and 15 is F, so 255 is FF.
Q: Write 307 in BCD. What denary number is 1001 0110?
A: 3 → 0011, 0 → 0000, 7 → 0111, so 0011 0000 0111. 1001 is 9 and 0110 is 6, so the number is 96.
Q: Give the one's complement and the two's complement of 00011010.
A: Inverting gives the one's complement, 11100101. Adding 1 gives the two's complement, 11100110 (which is −26: \(-128 + 64 + 32 + 4 + 2 = -26\)).
Q: What is the denary value of 10000001 as an 8-bit two's complement integer? What are the largest and smallest values?
A: \(-128 + 1 = -127\). The largest is 127 (01111111) and the smallest is −128 (10000000).
Q: Add 00110110 and 00011011 and give the answer in denary.
A: The sum is 01010001, which is \(64 + 16 + 1 = 81\). (Check: 54 + 27 = 81.)
Q: How many GiB are in 2 TiB, and how many bytes are in 2 KiB?
A: 1 TiB = 1024 GiB, so 2 TiB = 2048 GiB. \(2 \times 1024 = 2048\) bytes.
Q: The ASCII code of 'a' is 97. What is the code of 'd', and what is the code of 'D'?
A: 'd' is 3 after 'a', so 100. Capitals are 32 below the lower-case letters, so 'D' is \(100 - 32 = 68\).
Q: Write the denary number 77 as a hexadecimal number using the division method, and check it by converting back.
A: \(77 \div 16 = 4\) remainder 13, so the digits are 4 and D (13): 4D. Check: \(4 \times 16 + 13 = 77\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Convert the denary number 203 into (a) an 8-bit binary number [2] and (b) hexadecimal [1].
A: (a) 203 = 128 + 64 + 8 + 2 + 1, so the pattern is 11001011. [B1] [B1] (one mark for the method, one for the correct 8 bits)

(b) 1100 is C and 1011 is B, so the answer is CB. [B1]

Q: [4 marks] ★ A phone stores photos of 4 MiB each. (a) How many MiB are in a 2 GiB memory card? [1] (b) How many whole photos fit on the card? [2] (c) State which is the larger unit, 1 MB or 1 MiB. [1]
H: 1 GiB is 1024 MiB.
A: (a) \(2 \times 1024 = 2048\) MiB. [B1]

(b) \(2048 \div 4 = 512\) photos. [M1] [A1]

(c) 1 MiB (\(2^{20}\) bytes) is larger than 1 MB (\(10^6\) bytes). [B1]

Q: [6 marks] ★★ A kitchen scale in a school in Kampala shows its mass using binary-coded decimal (BCD). (a) Show the BCD for the mass 482 grams. [2] (b) Explain why BCD suits a numerical display. [1] (c) State why 0101 1010 cannot be a valid BCD number. [1] (d) Give one use of hexadecimal and one reason it is used instead of binary. [2]
A: (a) 4 → 0100, 8 → 1000, 2 → 0010, giving 0100 1000 0010. [B1] (each digit is coded in its own 4 bits) [B1] (correct nibbles in order)

(b) Each denary digit is stored separately, so it can be sent straight to a display digit with no conversion. [B1]

(c) 1010 (the second nibble) is ten, and BCD digits only go from 0 to 9 (0000 to 1001). [B1]

(d) One use: colour codes, memory addresses or MAC addresses. [B1] Reason: it is shorter and easier to read and write than binary (one hex digit represents 4 bits). [B1]

Q: [4 marks] ★★ (a) Show how −93 is stored as an 8-bit two's complement integer. [3] (b) State the range of values that can be stored in 8-bit two's complement. [1]
H: Start from +93, not −93.
A: (a) 93 = 64 + 16 + 8 + 4 + 1 = 01011101. [B1] Invert the bits: 10100010. [B1] Add 1: 10100011. [B1]

(b) −128 to 127. [B1]

Q: [5 marks] ★★ Two 8-bit two's complement integers, 01101011 and 00111001, are added together. (a) Show the binary addition, giving the 8-bit result. [2] (b) State the denary value of each of the two numbers. [1] (c) State whether overflow has occurred, and explain your answer. [2]
H: Look at the sign bit of each number and of the result.
A: (a) The result is 10100100. [B1] Carries shown correctly in the working (for example 11110110 written above the columns, with the last carry going into the sign bit). [B1]

(b) 107 and 57. [B1]

(c) Yes, overflow has occurred. [B1] Two positive numbers have given a result with the MSB 1, which is negative (−92); the true answer, 164, is larger than 127. [B1]

Q: [6 marks] ★★ Use two's complement to work out 100 − 37 in 8 bits. Show all your working.
H: Convert both numbers, find −37, add, then deal with the carry out.
A: 100 = 01100100. [B1] 37 = 00100101. [B1] Invert 37: 11011010, add 1: 11011011, which is −37. [B1]

```text
carries   10000000
          01100100
        + 11011011
        ----------
        1 00111111
```

The addition is shown with correct bits. [B1] The carry out of the leftmost column is discarded. [B1] The result is 00111111 = 63. [B1]

Q: [8 marks] ★★★ A messaging app is used by pupils in several countries. (a) Explain why the app stores text using Unicode instead of ASCII. [3] (b) In ASCII the code for 'C' is 67. State the code for 'H'. [1] (c) State how many different characters 7-bit ASCII can represent. [1] (d) The message "Kumasi 2027" has 11 characters, including the space. State the number of bits needed to store it in 8-bit extended ASCII, and in an encoding that uses 32 bits for every character. [2] (e) State one effect on file size of changing from ASCII to a 32-bit Unicode encoding. [1]
H: For (d), multiply the number of characters by the bits per character.
A: (a) ASCII has only 128 characters (256 in extended ASCII), too few for all the scripts the pupils use. [B1] Unicode has a unique code for the characters of nearly all languages (and symbols and emoji). [B1] Unicode uses more bits per character, so it has many more possible codes. [B1]

(b) 'H' is 5 after 'C', so 72. [B1]

(c) \(2^7 = 128\). [B1]

(d) \(11 \times 8 = 88\) bits. [B1] \(11 \times 32 = 352\) bits. [B1]

(e) The file becomes larger (four times as large for plain text). [B1]

Q: [8 marks] ★★★ A register holds the 8-bit two's complement number 10010110. (a) State its denary value. [2] (b) Write the number in hexadecimal. [1] (c) The binary number 01101110 is added to it. Show the 8-bit result and state its denary value. [3] (d) State whether overflow occurs, with a reason. [2]
H: For (d), think about what happens when the two numbers have different signs.
A: (a) \(-128 + 16 + 4 + 2\) [M1] = −106 [A1]

(b) 1001 and 0110 give 96. [B1]

(c) 10010110 + 01101110 gives 1 00000100, so the 8-bit result (after discarding the carry out) is 00000100. [B1] [B1] The denary value is 4. [B1]

(d) No overflow occurs. [B1] The numbers have opposite signs (one negative, one positive), so the result cannot be outside the range. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Two's complement is not quite symmetric. (a) Find the two's complement negation of −128 in 8 bits by inverting and adding 1, and say what you find. [3] (b) Explain why +128 cannot be stored as an 8-bit two's complement integer. [1] (c) State one consequence for a program that negates a number that might be −128. [1]
H: Start from 10000000 and apply the rule once.
H: Think about the largest value that fits with the MSB equal to 0.
A: (a) −128 is 10000000. [B1] Inverting gives 01111111. [B1] Adding 1 gives 10000000 again, which is −128: negating −128 gives the same number back. [B1]

(b) The largest positive value is 127 (01111111); +128 would need 9 bits, because 10000000 means −128 in this system. [B1]

(c) The program can give a wrong result (overflow) without warning, for example when it tries to calculate the absolute value of the smallest number. [B1]

Q: [6 marks] ★★★ A bank in Dhaka stores a 12-digit account number. It is considering storing it as packed BCD or as an ordinary binary integer. You are given that \(2^{39} = 549\,755\,813\,888\) and \(2^{40} = 1\,099\,511\,627\,776\). (a) State the number of bits packed BCD needs. [1] (b) Show that 40 bits are enough, and 39 are not, for the largest 12-digit number. [3] (c) Give two reasons why the bank might still choose BCD. [2]
H: The largest 12-digit number is 999 999 999 999, which is \(10^{12} - 1\).
A: (a) 12 digits at 4 bits each is 48 bits. [B1]

(b) The largest 12-digit number is 999 999 999 999, one less than \(10^{12}\). [B1] This is larger than \(2^{39}\), so 39 bits are not enough. [B1] It is smaller than \(2^{40}\), so 40 bits are enough. [B1] (BCD uses 8 more bits than binary: one sixth of its 48.)

(c) Each digit can be sent straight to a display or printer with no conversion. [B1] Every denary digit is held exactly, which matters for numbers such as account numbers and money. [B1]
:::

:::quiz
? What is the denary value of the binary number 00101101?
- 41
+ 45
- 43
- 180
> 32 + 8 + 4 + 1 = 45. The answer 41 forgets the 4; 43 counts the 1 in the 4s column as 2; 180 reads the place values from the wrong end (starting with 1 at the left).
? How many bytes are in 1 KiB?
- 1000
+ 1024
- 1048576
- 8
> A kibibyte is \(2^{10} = 1024\) bytes. 1000 is the decimal kilobyte (kB); 1 048 576 is a mebibyte.
? One hexadecimal digit represents exactly:
- 2 bits
- 3 bits
+ 4 bits
- 8 bits
> 16 = \(2^4\), so four bits give exactly the 16 values of one hex digit. Eight bits (a byte) need two hex digits.
? What is 1001 0101 in BCD?
- 149
+ 95
- 21
- 4
> Each nibble is one digit: 1001 is 9 and 0101 is 5. Reading it as binary would give 149, a different value.
? What is the 8-bit two's complement pattern for −1?
- 10000001
+ 11111111
- 00000001
- 11111110
> 1 is 00000001. Invert to 11111110 and add 1 to get 11111111. The pattern 10000001 is −127, and 11111110 is −2.
? Two 8-bit two's complement numbers 01100100 and 01100100 are added. What is the best description of the result?
- Correct, with no overflow, because there is no carry out.
+ The result is 11001000, which is negative, so overflow has occurred.
- The result needs a ninth bit, so there is a carry out.
- The result is 11001000 and means 200.
> 100 + 100 = 200 is larger than 127, so the result 11001000 reads as −56: two positive numbers gave a negative one. There is no carry out here, so a carry out is not how signed overflow is spotted.
? Which statement about ASCII and Unicode is correct?
- Unicode uses fewer bits per character, so files are smaller.
- ASCII can represent more characters than Unicode.
+ Unicode can represent the characters of many writing systems because it has many more codes than ASCII.
- The character code for '7' is the number 7.
> Unicode has far more codes, and the cost is that characters may use more bits. The digit '7' has a code of its own (55 in ASCII), not the value 7.
? A hard drive is sold as 1 TB. A computer reports its size in TiB. What does it show?
- Exactly 1 TiB.
- More than 1 TiB.
+ Less than 1 TiB.
- It cannot be compared.
> 1 TB is \(10^{12}\) bytes and 1 TiB is \(2^{40}\) (about \(1.1 \times 10^{12}\)) bytes, so the same drive is about 0.91 TiB.
:::

:::checklist What you can now do
- [ ] I can state the sizes of the binary and decimal prefixes (kibi/kilo, mebi/mega, gibi/giga, tebi/tera) and convert between units.
- [ ] I can convert integers between binary, denary and hexadecimal, by hand.
- [ ] I can write a denary number in binary-coded decimal and decode BCD.
- [ ] I can explain the practical uses of hexadecimal and BCD.
- [ ] I can write negative integers in one's complement and two's complement and convert them back.
- [ ] I can state the range of an n-bit two's complement integer.
- [ ] I can add binary numbers and subtract by adding a two's complement.
- [ ] I can explain overflow and identify it in signed and unsigned additions.
- [ ] I can describe ASCII, extended ASCII and Unicode and explain why Unicode is used.
- [ ] I can write the division method for binary conversion as pseudocode.
:::

:::recap
- A bit is 0 or 1; a nibble is 4 bits; a byte is 8 bits. \(n\) bits give \(2^n\) patterns; unsigned values run 0 to \(2^n - 1\).
- Binary prefixes are powers of 2 (1 KiB = 1024 bytes); decimal prefixes are powers of 10 (1 kB = 1000 bytes). Use the prefix the question uses.
- Denary to binary: subtract place values or divide by 2 and read the remainders from last to first. Always write all the bits asked for.
- One hex digit is one nibble. Group in 4s from the right. Hex is a shorthand for binary: shorter, easier to read, used for colours, addresses and MAC addresses.
- BCD stores each denary digit in 4 bits (valid nibbles 0000 to 1001); used for displays and for money. It is not the same as binary.
- Two's complement: invert and add 1; MSB is worth −128 in 8 bits; range \(-2^{n-1}\) to \(2^{n-1} - 1\); one zero. One's complement has two zeros.
- Subtract by adding the two's complement and discarding the carry out.
- Overflow: the result needs more bits than are available. Signed: two positives give a negative, or two negatives give a positive. Unsigned: a carry out of the leftmost column.
- ASCII is 7 bits (128 characters), extended ASCII is 8 bits (256), Unicode has many more characters and uses more bits. Character codes are in order, and the code for '7' is not 7.
:::

:::links
- practise: [Data representation: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/1-information-representation/data-representation/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- explore: [Binary converter](https://www.101computing.net/binary-converter/) · 101 Computing · practise converting between binary and denary
- read: [Bits, bytes and the internet](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · free lessons on how computers store numbers and text
- read: [What is Unicode?](https://home.unicode.org/) · Unicode Consortium · the organisation that maintains the character set
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run the Python checks in this chapter line by line

Links checked 13 November 2026.
:::

Next: [Images, sound and compression](#cs.media)
