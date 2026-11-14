@chapter cs.float
@title Floating-point numbers
@level a2
@paper CAIE 9618 Paper 3
@time 5–7 hours
@summary How a computer stores real numbers with a fractional part: binary fractions, fixed point, and floating point with a two's complement mantissa and exponent. You will convert between floating point and denary, normalise a number, work out the range and precision of a format, and explain rounding errors, overflow and underflow.

:::why
The number 0.1 cannot be stored exactly by any computer, and 0.1 + 0.2 is not quite 0.3. That is not a bug: it follows from how real numbers are stored. Paper 3 asks you to convert floating-point patterns by hand, normalise them and explain what happens when a number is too big, too small or not exactly representable. Programmers who understand this write code that compares prices and measurements safely.
:::

**Before you start**, you should be comfortable with binary and two's complement integers from [Number systems and binary arithmetic](#cs.data).

:::try Warm-up
Q: What denary number does the 8-bit two's complement pattern 10110100 represent? (from [Number systems and binary arithmetic](#cs.data))
A: The left-hand bit is worth −128, so the value is \(-128 + 32 + 16 + 4 = -76\).
Q: What range of denary values can a 4-bit two's complement number store? (from [Number systems and binary arithmetic](#cs.data))
A: From \(-2^{3} = -8\) to \(2^{3} - 1 = 7\).
Q: What is overflow when two integers are added? (from [Number systems and binary arithmetic](#cs.data))
A: The result is too large (or too negative) to fit in the number of bits available, so the stored result is wrong.
:::

## Real numbers in binary

You know that the columns of a binary integer have place values 1, 2, 4, 8 and so on, doubling each step to the left. The same pattern continues to the **right** of a **binary point**, where each column is **half** the one before.

| Column | 1 | . | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 |
|---|---|---|---|---|---|---|---|---|---|
| Denary value | 1 | . | 0.5 | 0.25 | 0.125 | 0.0625 | 0.03125 | 0.015625 | 0.0078125 |

So \(0.1011_2 = \tfrac12 + \tfrac18 + \tfrac1{16} = 0.6875\), and \(101.01_2 = 4 + 1 + \tfrac14 = 5.25\).

### Denary fractions to binary

To convert the fractional part of a denary number, **multiply by 2 repeatedly**. Each time, the digit before the point is the next bit, and you carry on with what is left after the point. Take 0.6875:

| Step | Multiply | Result | Bit |
|---|---|---|---|
| 1 | 0.6875 × 2 | 1.375 | 1 |
| 2 | 0.375 × 2 | 0.75 | 0 |
| 3 | 0.75 × 2 | 1.5 | 1 |
| 4 | 0.5 × 2 | 1.0 | 1 |

The remainder is now 0, so the answer is exact: \(0.6875 = 0.1011_2\). To convert a whole number plus a fraction, convert each part separately: \(13.375 = 1101_2 + 0.011_2 = 1101.011_2\).

Some fractions never reach 0. Try 0.1:

| Step | Multiply | Result | Bit |
|---|---|---|---|
| 1 | 0.1 × 2 | 0.2 | 0 |
| 2 | 0.2 × 2 | 0.4 | 0 |
| 3 | 0.4 × 2 | 0.8 | 0 |
| 4 | 0.8 × 2 | 1.6 | 1 |
| 5 | 0.6 × 2 | 1.2 | 1 |
| 6 | 0.2 × 2 | 0.4 | 0 |

After step 5 the remainder is 0.2 again, which is the remainder after step 1, so the bits repeat for ever: 0.1 is 0.000110011001100110011… in binary, where the group 0011 repeats without end. This is the key to the last section: a stored number has a fixed number of bits, so a value such as 0.1 has to be cut off, and the stored value is only close to 0.1.

```python
def fraction_to_binary(x, places):
    bits = ""
    for _ in range(places):
        x = x * 2
        bits = bits + str(int(x))
        x = x - int(x)
    return bits

print(fraction_to_binary(0.6875, 4))
print(fraction_to_binary(0.375, 3))
print(fraction_to_binary(0.1, 12))
```

Output:

```output
1011
011
000110011001
```

:::note A fraction terminates only if its denominator is a power of 2
0.6875 is \(\tfrac{11}{16}\) and 0.375 is \(\tfrac38\): both denominators are powers of 2, so the binary expansion ends. 0.1 is \(\tfrac1{10}\), and 10 is not a power of 2, so it never ends. This is the same reason \(\tfrac13\) never ends in denary.
:::

## Fixed point

:::def Fixed-point representation
A way of storing a real number in which the binary point is at a fixed position in the bit pattern, so a set number of bits are used for the whole part and a set number for the fractional part.
:::

Suppose 8 bits are split as 4 bits before the point and 4 after. The pattern 0101.1010 means \(4 + 1 + 0.5 + 0.125 = 5.625\). The largest value is 1111.1111, which is \(15\tfrac{15}{16} = 15.9375\), and the smallest step between values is \(\tfrac1{16} = 0.0625\).

That is the problem. With the point fixed, there is one range and one step size for every number. This format cannot store 100 (too big), nor 0.001 (smaller than the step), nor 3.14159 accurately. To store both very large and very small numbers, the point has to **float**.

## Floating point

Scientists write a very large or small number in standard form: \(0.00000234 = 2.34 \times 10^{-6}\). The digits (2.34) say how precisely the number is known, and the power of ten (−6) says how big it is. A floating-point number does exactly the same in binary: a **mantissa** holds the digits and an **exponent** says where the binary point goes.

:::def Floating-point representation
A way of storing a real number as a mantissa and an exponent. The value is the mantissa multiplied by 2 raised to the power of the exponent, so the binary point can "float" to suit the size of the number.
:::

:::def Mantissa
The part of a floating-point number that holds the significant digits of the number. In this course it is a two's complement fraction with the binary point immediately after the sign bit.
:::

:::def Exponent
The part of a floating-point number that holds the power of 2 by which the mantissa is multiplied. It is a two's complement integer, and it moves the binary point.
:::

:::key The Cambridge floating-point format
- A floating-point number is a **mantissa** followed by an **exponent**; the question says how many bits each has, for example "8 bits for the mantissa and 4 bits for the exponent".
- Both are **two's complement**. The first bit of each is the sign bit, with a negative place value.
- The mantissa is a **fraction**: the binary point is **after the sign bit**. An 8-bit mantissa has place values \(-1, \tfrac12, \tfrac14, \tfrac18, \tfrac1{16}, \tfrac1{32}, \tfrac1{64}, \tfrac1{128}\).
- The exponent is an integer: a 4-bit exponent has place values \(-8, 4, 2, 1\) and runs from −8 to 7.
- **value = mantissa × 2^exponent**.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 342 168" role="img" aria-label="A row of twelve bit boxes holding 0 1 0 1 1 0 0 0, then 0 0 1 1. The first eight are the mantissa with place values minus 1, then 2 to the minus 1 down to 2 to the minus 7; a dot after the first box marks the binary point. The last four are the exponent with place values minus 8, 4, 2 and 1. The first box of each part is the sign bit. The value is 0.1011000 times 2 cubed, which is 5.5."><text class="tl ti" x="20" y="16">A 12-bit floating-point number</text><text class="tl tc" x="116" y="40">mantissa (8 bits)</text><text class="tl tc" x="274" y="40">exponent (4 bits)</text><rect class="f1 s-acc sw2" x="20" y="46" width="24" height="28"/><text class="tl tc tb" x="32" y="65">0</text><text class="tl tc" x="32" y="100">−1</text><rect class="fm s-acc sw2" x="44" y="46" width="24" height="28"/><text class="tl tc tb" x="56" y="65">1</text><text class="tl tc" x="56" y="100">2⁻¹</text><rect class="fm s-acc sw2" x="68" y="46" width="24" height="28"/><text class="tl tc tb" x="80" y="65">0</text><text class="tl tc" x="80" y="100">2⁻²</text><rect class="fm s-acc sw2" x="92" y="46" width="24" height="28"/><text class="tl tc tb" x="104" y="65">1</text><text class="tl tc" x="104" y="100">2⁻³</text><rect class="fm s-acc sw2" x="116" y="46" width="24" height="28"/><text class="tl tc tb" x="128" y="65">1</text><text class="tl tc" x="128" y="100">2⁻⁴</text><rect class="fm s-acc sw2" x="140" y="46" width="24" height="28"/><text class="tl tc tb" x="152" y="65">0</text><text class="tl tc" x="152" y="100">2⁻⁵</text><rect class="fm s-acc sw2" x="164" y="46" width="24" height="28"/><text class="tl tc tb" x="176" y="65">0</text><text class="tl tc" x="176" y="100">2⁻⁶</text><rect class="fm s-acc sw2" x="188" y="46" width="24" height="28"/><text class="tl tc tb" x="200" y="65">0</text><text class="tl tc" x="200" y="100">2⁻⁷</text><rect class="f1 s-acc sw2" x="226" y="46" width="24" height="28"/><text class="tl tc tb" x="238" y="65">0</text><text class="tl tc" x="238" y="100">−8</text><rect class="fm s-acc sw2" x="250" y="46" width="24" height="28"/><text class="tl tc tb" x="262" y="65">0</text><text class="tl tc" x="262" y="100">4</text><rect class="fm s-acc sw2" x="274" y="46" width="24" height="28"/><text class="tl tc tb" x="286" y="65">1</text><text class="tl tc" x="286" y="100">2</text><rect class="fm s-acc sw2" x="298" y="46" width="24" height="28"/><text class="tl tc tb" x="310" y="65">1</text><text class="tl tc" x="310" y="100">1</text><circle class="fi" cx="44" cy="82" r="2.5"/><text class="tl tc" x="32" y="122">sign bit</text><text class="tl tc" x="238" y="122">sign bit</text><text class="tl" x="20" y="144">dot = binary point (after the sign bit)</text><text class="tl" x="20" y="162">0.1011000 × 2³ = 5.5</text></svg><figcaption>The pattern 01011000 0011 split into an 8-bit mantissa and a 4-bit exponent. Both are two's complement numbers: the sign bit has a negative place value. The mantissa is a fraction with the binary point after its sign bit.</figcaption></figure>
:::

In the figure the mantissa is \(0.1011000_2 = \tfrac12 + \tfrac18 + \tfrac1{16} = 0.6875\) and the exponent is \(0011_2 = 3\), so the value is \(0.6875 \times 2^3 = 5.5\). Multiplying by \(2^3\) moves the binary point three places to the right: \(0.1011000 \to 0101.1000\), which is \(4 + 1 + 0.5 = 5.5\).

### Floating point to denary

:::steps
1. Split the pattern into the mantissa and the exponent, using the numbers of bits the question gives.
2. Convert the **exponent** to denary first. It is two's complement, so the sign bit counts as a negative number.
3. **Move the binary point** of the mantissa by that many places: **right** if the exponent is positive, **left** if it is negative. Fill any new places on the right with 0s. When moving left, fill the new places with copies of the sign bit.
4. Read the new pattern using place values, with the sign bit negative. (Or check: the mantissa value times \(2^{\text{exponent}}\).)
:::

:::eg Floating point to denary, positive exponent (exam style)
A floating-point number has an 8-bit mantissa and a 4-bit exponent, both in two's complement. Convert each pattern to denary. (a) Mantissa 01011000, exponent 0011. (b) Mantissa 10110000, exponent 0010.

(a) The exponent 0011 is 3. [B1]
The mantissa is 0.1011000. Moving the point 3 places right gives 0101.1000. [B1]
\(4 + 1 + 0.5 = 5.5\). [B1]

(b) The exponent 0010 is 2. [B1]
The mantissa is 1.0110000. Moving the point 2 places right gives 101.10000. [B1]
The sign bit now has place value \(-4\), so \(-4 + 1 + 0.5 = -2.5\). [B1]

Check (b): the mantissa is \(-1 + \tfrac14 + \tfrac18 = -\tfrac58\), and \(-\tfrac58 \times 2^2 = -2.5\).
:::

A negative **exponent** moves the point to the **left**, making the number smaller.

:::eg Floating point to denary, negative exponent
Using the same format (8-bit mantissa, 4-bit exponent), convert (a) mantissa 01100000, exponent 1110, and (b) mantissa 10100000, exponent 1101.

(a) The exponent 1110 is \(-8 + 4 + 2 = -2\). [B1]
The mantissa 0.1100000 with the point moved 2 places left is 0.001100000. [B1]
\(\tfrac18 + \tfrac1{16} = 0.1875\). [B1]

(b) The exponent 1101 is \(-8 + 4 + 1 = -3\). [B1]
The mantissa 1.0100000 with the point moved 3 places left, filling with 1s, is 1.1110100000. [B1]
This is \(-1 + \tfrac12 + \tfrac14 + \tfrac18 + \tfrac1{32} = -0.09375\). [B1]

Check (b): the mantissa is \(-1 + \tfrac14 = -\tfrac34\), and \(-\tfrac34 \div 8 = -\tfrac{3}{32} = -0.09375\).
:::

The same method in Python. The function uses `Fraction`, which does exact arithmetic, so there is no rounding in the answers:

```python
from fractions import Fraction

def twos(bits):
    value = int(bits, 2)
    if bits[0] == "1":
        value = value - 2 ** len(bits)
    return value

def to_denary(mantissa, exponent):
    fraction = Fraction(twos(mantissa), 2 ** (len(mantissa) - 1))
    return fraction * Fraction(2) ** twos(exponent)

def is_normalised(mantissa):
    return mantissa[0] != mantissa[1]

for pattern in ["010110000011", "101100000010", "011000001110", "101000001101"]:
    mantissa = pattern[:8]
    exponent = pattern[8:]
    value = to_denary(mantissa, exponent)
    print(mantissa, exponent, value, float(value), is_normalised(mantissa))
```

Output:

```output
01011000 0011 11/2 5.5 True
10110000 0010 -5/2 -2.5 True
01100000 1110 3/16 0.1875 True
10100000 1101 -3/32 -0.09375 True
```

The first value, `11/2`, is the exact fraction 5.5. The last column is explained in the next section.

:::warn The exponent is two's complement too
The commonest slip is to read the exponent as an ordinary binary number. 1110 is −2, not 14. Always give the sign bit of the exponent its negative place value, and say the exponent in denary before you move the point.
:::

### Denary to floating point

Going the other way, you build the pattern. Take 6.25.

:::steps
1. Convert the number (ignoring its sign) to binary, using the doubling method for the fraction.
2. **Move the binary point** until the number is written as \(0.1\ldots\). Count the places. Moving the point **left** \(k\) places means the exponent is \(+k\); moving it **right** \(k\) places means the exponent is \(-k\).
3. The mantissa is a 0 (the sign bit), the point, then the digits, padded on the right with 0s to fill the bits. If there are more digits than room, the number is **rounded**.
4. If the number is **negative**, take the two's complement of the positive mantissa: invert every bit and add 1.
5. Write the exponent in two's complement with the number of bits given. Join the mantissa and the exponent.
:::

:::eg Denary to floating point (exam style)
Write each number as a normalised floating-point number with an 8-bit mantissa and a 4-bit exponent, both in two's complement. (a) 6.25 (b) −3.5

(a) 6.25 in binary is 110.01 (\(4 + 2 + 0.25\)). [B1]
Moving the point 3 places left gives 0.11001, so the exponent is +3, which is 0011. [B1]
The mantissa is 0.1100100 (padded with zeros to 8 bits), so the answer is 01100100 0011. [B1]

(b) 3.5 in binary is 11.1, and the positive mantissa is 0.1110000 with exponent +2 (0010). [B1]
Two's complement of 0.1110000: invert to get 1.0001111, add 1 to get 1.0010000. [B1]
The answer is 10010000 0010. [B1]

Check: the mantissa 1.0010000 is \(-1 + \tfrac18 = -0.875\), and \(-0.875 \times 4 = -3.5\).
:::

Now a number below 1, and the awkward case, a negative number that is an exact power of two.

:::eg Denary to floating point: a small number, and −4
Same format. (a) 0.15625 (b) −4

(a) \(0.15625 = 0.00101_2\) (\(\tfrac18 + \tfrac1{32}\)). [B1]
Moving the point 2 places right gives 0.101, so the exponent is −2, which is 1110. [B1]
The mantissa is 0.1010000. The answer is 01010000 1110. [B1]

(b) 4 is 100 in binary. Moving the point 3 places left gives 0.100, so the positive mantissa is 0.1000000 with exponent +3. [B1]
Inverting gives 1.0111111 and adding 1 gives 1.1000000. This starts 1.1, so it is **not normalised**. [B1]
Shift the mantissa left one place and subtract 1 from the exponent: 1.0000000 with exponent +2. The answer is 10000000 0010. [B1]

Check: the mantissa 1.0000000 is exactly \(-1\), and \(-1 \times 2^2 = -4\).
:::

:::eg A number with a whole part and a fraction
Write 13.375 as a normalised number with an 8-bit mantissa and a 4-bit exponent.

\(13 = 1101_2\) and \(0.375 = 0.011_2\), so \(13.375 = 1101.011_2\). [B1]
Moving the point 4 places left gives 0.1101011, so the exponent is +4, which is 0100. [B1]
The mantissa is 0.1101011: seven digits after the point, which exactly fills the 8-bit mantissa. The answer is 01101011 0100. [B1]

Check: \(0.1101011_2 = \tfrac{107}{128}\), and \(\tfrac{107}{128} \times 16 = 13.375\).

If the digits do not fit, the number is rounded: look at the first digit that does not fit, add 1 to the last digit kept if it is a 1, and drop it if it is a 0. Exam questions normally choose numbers that fit; when one does not, say that you rounded.
:::

The pattern for −4 is worth remembering: **a mantissa of 1.0000000 means exactly −1**, which is why the most negative value in the format has a mantissa of 1.0000000.

```python
from fractions import Fraction
import math

def to_floating(x, mantissa_bits, exponent_bits):
    x = Fraction(x)
    if x == 0:
        return "0" * mantissa_bits, "0" * exponent_bits
    negative = x < 0
    size = abs(x)
    exponent = 0
    while size >= 1:
        size = size / 2
        exponent = exponent + 1
    while size < Fraction(1, 2):
        size = size * 2
        exponent = exponent - 1
    if negative and size == Fraction(1, 2):
        size = Fraction(1)
        exponent = exponent - 1
    whole = math.floor(size * 2 ** (mantissa_bits - 1) + Fraction(1, 2))
    if whole == 2 ** (mantissa_bits - 1) and not negative:
        whole = 2 ** (mantissa_bits - 2)
        exponent = exponent + 1
    if negative:
        whole = -whole
    mantissa = format(whole % 2 ** mantissa_bits, "0" + str(mantissa_bits) + "b")
    exponent_pattern = format(exponent % 2 ** exponent_bits, "0" + str(exponent_bits) + "b")
    return mantissa, exponent_pattern

for number in ["6.25", "-3.5", "0.15625", "-4", "0.1"]:
    mantissa, exponent = to_floating(Fraction(number), 8, 4)
    print(number, mantissa, exponent)
```

Output:

```output
6.25 01100100 0011
-3.5 10010000 0010
0.15625 01010000 1110
-4 10000000 0010
0.1 01100110 1101
```

The first four rows match the worked examples. The loop that halves `size` until it is below 1 and doubles it until it is at least a half **is** "moving the binary point". The last row is the number 0.1, which has to be rounded, so it is not exact: a later section shows its value is 0.099609375.

## Normalisation

The same value can be written in several ways. In the 8 + 4 format, 5.5 is 01011000 0011, but it is also 00101100 0100 (the mantissa 0.0101100 is half as big and the exponent is one bigger) and 00010110 0101. Only the first uses the mantissa to the full.

:::def Normalisation
Adjusting a floating-point number so that the mantissa uses as many bits as possible for the significant digits: the point is moved, and the exponent adjusted to match, until a positive mantissa starts 0.1 and a negative mantissa starts 1.0. The first two bits of a normalised mantissa are always different.
:::

:::key Recognising a normalised number
- Positive mantissa: starts **01** (0.1…). Negative mantissa: starts **10** (1.0…).
- So the first two bits differ. If they are the same (00 or 11), the number is **not** normalised.
- The value 0 cannot be normalised: the mantissa is all zeros.
:::

**Why normalise?**

- **To keep the most precision.** The mantissa has a fixed number of bits. A leading 0 (positive) or 1 (negative) after the sign bit carries no information, so the mantissa wastes a bit that could hold a significant digit.
- **To give one representation of each value.** Without a rule, 5.5 has many patterns. With it, each number has exactly one, which makes comparing two numbers simple.

### How to normalise

If the first two bits are equal, **shift the mantissa left** one place (a zero joins on the right) and **subtract 1 from the exponent**. Each shift doubles the mantissa and halves the power of two, so the value is unchanged. Repeat until the first two bits differ.

:::eg Normalising a floating-point number
The 8 + 4 pattern 00011010 0100 is not normalised. (a) Convert it to denary. (b) Normalise it and show the value is unchanged.

(a) The exponent 0100 is 4. The mantissa 0.0011010 is \(\tfrac18 + \tfrac1{16} + \tfrac1{64} = \tfrac{13}{64}\). The value is \(\tfrac{13}{64} \times 16 = 3.25\). [B1]

(b) The first two bits are 00, so shift left. 00110100 with exponent 0011 (3) is still 00, so shift again. [B1]
01101000 with exponent 0010 (2): the first two bits are now 01. [B1]
The normalised number is 01101000 0010, and \(0.1101000 \times 2^2 = 0.8125 \times 4 = 3.25\). [B1]
:::

A **negative** mantissa is normalised in the same way, but the repeated bit is 1. For example, 11100110 0011 is \(-\tfrac{13}{64} \times 8 = -1.625\), and after two left shifts it is 10011000 0001, which is \(-\tfrac{13}{16} \times 2 = -1.625\).

:::warn Do not normalise a negative number to 0.1…
A negative mantissa is normalised when it starts **1.0**. A student who writes −3.5 with mantissa 1.1110000 has not normalised it. A mantissa starting 1.1 can be shifted left, which is what makes room for another significant bit.
:::

Try the widget below: it shows the mantissa, exponent and value for a pattern, and its **Normalise** button does one shift at a time. Start with the pattern loaded, press Normalise twice and check that the value stays at 3.25. Then flip some bits, or type a denary value to see the nearest number the format can hold.

:::html
<div class="widget" data-w="cs-float" data-m="8" data-e="4" data-bits="00011010 0100"></div>
:::

## Range and precision

A floating-point format of \(m\) mantissa bits and \(e\) exponent bits has a **largest** and a **smallest** value, and gaps between neighbours.

:::def Range
The span of values a format can store, from the largest to the smallest in size. A longer exponent gives a greater range, because the point can be moved further.
:::

:::def Precision
How exactly a format can store a value. It depends on the number of bits in the mantissa: more mantissa bits mean more significant digits and a smaller gap between neighbouring values.
:::

For 8 + 4 bits, the exponent runs from −8 to 7 and the mantissa has 7 bits after the point.

:::key Limits of an 8-bit mantissa, 4-bit exponent format
| Value | Mantissa | Exponent | Value in denary |
|---|---|---|---|
| Largest positive | 0.1111111 | +7 (0111) | \(\tfrac{127}{128} \times 2^7 = 127\) |
| Smallest positive (normalised) | 0.1000000 | −8 (1000) | \(\tfrac12 \times 2^{-8} = \tfrac1{512} = 0.001953125\) |
| Most negative | 1.0000000 | +7 (0111) | \(-1 \times 2^7 = -128\) |
:::

:::eg The limits of a 10 + 6 format (exam style)
A floating-point format has a 10-bit mantissa and a 6-bit exponent, both in two's complement. Give the largest positive value and the smallest positive normalised value, as expressions in powers of 2, and the exponent range.

The 6-bit exponent has place values \(-32, 16, 8, 4, 2, 1\), so it runs from \(-32\) to \(+31\). [B1]
The largest mantissa is 0.111111111 (nine 1s after the point), which is \(1 - 2^{-9}\). The largest positive value is \(\left(1 - 2^{-9}\right) \times 2^{31}\), which is 2 143 289 344. [B1]
The smallest positive normalised mantissa is 0.100000000, which is \(\tfrac12\), with the smallest exponent, \(-32\). The value is \(2^{-1} \times 2^{-32} = 2^{-33}\), about \(1.2 \times 10^{-10}\). [B1]
Compare with 8 + 4: the exponent range grows from \(-8\) to 7 to \(-32\) to 31, so the largest value grows from 127 to over two thousand million. [B1]
:::

In patterns: the largest positive number is 01111111 0111, the smallest positive normalised number is 01000000 1000, and the most negative number is 10000000 0111.

For any format, with \(m\) mantissa bits and \(e\) exponent bits: the exponent runs from \(-2^{e-1}\) to \(2^{e-1} - 1\), and the mantissa's biggest value is \(1 - 2^{-(m-1)}\). The largest positive value uses the biggest mantissa with the biggest exponent. The smallest positive normalised value uses the smallest normalised mantissa, \(\tfrac12\), with the most negative exponent.

### Changing the split of bits

The total number of bits is fixed, so a bit given to one part is taken from the other.

| Format (12 bits) | Bits after the point | Exponent range | Largest positive | Smallest positive (normalised) | Smallest mantissa step |
|---|---|---|---|---|---|
| 9 + 3 | 8 | −4 to 3 | 7.96875 | 0.03125 | 0.00390625 |
| 8 + 4 | 7 | −8 to 7 | 127 | 0.001953125 | 0.0078125 |
| 7 + 5 | 6 | −16 to 15 | 32256 | 1/131072 | 0.015625 |

:::key Range against precision
- **More bits for the mantissa:** greater precision (a smaller gap between stored values), but a smaller range.
- **More bits for the exponent:** greater range (larger and smaller numbers can be stored), but less precision.
:::

:::warn More exponent bits do not improve accuracy
"More bits for the exponent makes it more accurate" is wrong and loses marks. Accuracy (precision) comes from the **mantissa**. The exponent gives **range**.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 128" role="img" aria-label="A number line from 0 to 1.75 with sixteen tick marks, the representable positive values. They fall in four groups of four, for exponents minus 2, minus 1, 0 and 1. The ticks are very close together near 0.125 and spread further apart in each group: the gaps are 0.03125, 0.0625, 0.125 and 0.25."><text class="tl ti" x="20" y="16">All 16 positive normalised values</text><path class="ln-m thin" d="M 20 52 L 330 52"/><path class="c1 sw2" d="M 41.25 38 L 41.25 52"/><path class="c1 sw2" d="M 46.5625 38 L 46.5625 52"/><path class="c1 sw2" d="M 51.875 38 L 51.875 52"/><path class="c1 sw2" d="M 57.1875 38 L 57.1875 52"/><path class="c1 sw2" d="M 62.5 38 L 62.5 52"/><path class="c1 sw2" d="M 73.125 38 L 73.125 52"/><path class="c1 sw2" d="M 83.75 38 L 83.75 52"/><path class="c1 sw2" d="M 94.375 38 L 94.375 52"/><path class="c1 sw2" d="M 105 38 L 105 52"/><path class="c1 sw2" d="M 126.25 38 L 126.25 52"/><path class="c1 sw2" d="M 147.5 38 L 147.5 52"/><path class="c1 sw2" d="M 168.75 38 L 168.75 52"/><path class="c1 sw2" d="M 190 38 L 190 52"/><path class="c1 sw2" d="M 232.5 38 L 232.5 52"/><path class="c1 sw2" d="M 275 38 L 275 52"/><path class="c1 sw2" d="M 317.5 38 L 317.5 52"/><path class="ln" d="M 20 34 L 20 52"/><text class="tl tc" x="20.0" y="72">0</text><text class="tl tc" x="62.5" y="72">0.25</text><text class="tl tc" x="105.0" y="72">0.5</text><text class="tl tc" x="190.0" y="72">1</text><text class="tl tc" x="317.5" y="72">1.75</text><text class="tl tc" x="49" y="96">−2</text><text class="tl tc" x="78" y="96">−1</text><text class="tl tc" x="137" y="96">0</text><text class="tl tc" x="254" y="96">1</text><text class="tl tc" x="170" y="118">exponent of each group of four ticks</text></svg><figcaption>Every positive normalised value of a format with a 4-bit mantissa and a 2-bit exponent. The gap between neighbours doubles whenever the exponent goes up by one, so large numbers are stored less precisely than small ones.</figcaption></figure>
:::

The figure shows a tiny format (a 4-bit mantissa and a 2-bit exponent) with all 16 of its positive normalised values. Each group of four has the same exponent, and the gap between neighbours doubles from one group to the next: 0.03125, 0.0625, 0.125, 0.25. Near zero the values are packed closely; far from zero they are spread out. The **relative** error stays about the same, which is the point of floating point. A number that falls in a gap must be rounded to a neighbour.

## Approximation, rounding errors, overflow and underflow

### A binary representation is an approximation

Only numbers that are a sum of powers of 2 (with the available number of bits) are stored exactly: 5.5, 0.1875 and −4 above. Most decimals are not, because their binary expansion never ends. When the mantissa runs out of bits, the extra bits are dropped or rounded.

:::def Rounding error
The difference between a real number and the nearest value that the format can store. It happens because a floating-point number has only a fixed number of mantissa bits.
:::

:::eg The number 0.1 in an 8 + 4 format
Find the stored value of 0.1 in the format with an 8-bit mantissa and a 4-bit exponent, and the size of the error.

\(0.1 = 0.000110011001\ldots_2\). Moving the point 3 places right to get 0.110011001… gives an exponent of −3 (1101). [B1]
The mantissa has 7 bits after the point: 0.1100110|01100… The bits after the cut start with 0, so the digits are cut: the mantissa is 0.1100110. [B1]
The pattern is 01100110 1101. The stored value is \(0.1100110_2 \times 2^{-3} = \tfrac{51}{64} \times \tfrac18 = \tfrac{51}{512} = 0.099609375\). [B1]
The rounding error is \(0.1 - 0.099609375 = 0.000390625\), which is about 0.39% of 0.1. [B1]
:::

Python's real numbers use the same idea with a bigger format (64 bits), so the error is far smaller but not zero:

```python
from fractions import Fraction

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(abs((0.1 + 0.2) - 0.3) < 1e-9)
total = 0.0
for _ in range(10):
    total = total + 0.1
print(total, total == 1.0)
pence = 0
for _ in range(10):
    pence = pence + 10
print(pence, pence == 100)
print(Fraction(0.1))
print(1e308 * 10)
print(1e-320 / 1e10)
```

Output:

```output
0.30000000000000004
False
True
0.9999999999999999 False
100 True
3602879701896397/36028797018963968
inf
0.0
```

Line by line: 0.1 and 0.2 are both slightly wrong when stored, and the tiny errors show up in the sum. The comparison with `==` fails, but testing that the difference is smaller than a small tolerance passes. Adding 0.1 ten times, the rounding errors **accumulate**, so the total is 0.9999999999999999, not 1.0; counting in whole pence with integers is exact. `Fraction(0.1)` shows the exact value Python really stores, which is not one tenth.

:::key Safe habits with real numbers
- Never test two real numbers for equality with `=`: test that their difference is smaller than a small tolerance.
- Never use a REAL as a loop counter that is compared for equality; count with an INTEGER.
- Store money in whole units of the smallest coin (pence, cents) as an INTEGER.
- Rounding errors add up over many calculations, so the more operations, the less trustworthy the last digits.
:::

### Overflow and underflow

:::def Overflow
The error that occurs when the result of a calculation is larger than the largest value the format can store, because the exponent needed is greater than the exponent bits allow.
:::

:::def Underflow
The error that occurs when the result of a calculation is smaller in size than the smallest non-zero value the format can store (it is too close to zero), because the exponent needed is more negative than the exponent bits allow. The value is usually stored as zero.
:::

In the 8 + 4 format the largest value is 127, so \(100 + 100 = 200\) overflows. The smallest positive normalised value is \(\tfrac1{512}\), so a result such as \(\tfrac1{1000}\) underflows and would be stored as 0. In Python, `1e308 * 10` overflows to `inf` and `1e-320 / 1e10` underflows to `0.0`, as the output above shows.

:::exam Which error?
Overflow: too **big**, the exponent is too large. Underflow: too **close to zero**, the exponent is too negative. Both are about the exponent and so about **range**. A rounding error is about the **mantissa**, and so about precision.
:::

## Spot the error

:::eg Spot the error
A question: "The 8-bit mantissa 01100000 and the 4-bit exponent 1110 are both in two's complement. Convert the number to denary."

Student's answer: "The exponent 1110 is 14. The mantissa 0.1100000 is 0.5 + 0.25 = 0.75. I move the point 14 places right. The value is \(0.75 \times 2^{14} = 12288\)."

Find the slip, mark it and give the correct answer.

- The mantissa conversion 0.1100000 = 0.75 is correct, [B1] and the method (multiply by a power of 2) is correct.
- The exponent is two's complement, so 1110 is \(-8 + 4 + 2 = -2\), not 14. This is the slip, and it loses the exponent mark.
- With the exponent −2 the point moves 2 places **left**: \(0.75 \times 2^{-2} = 0.1875\). The final answer mark is lost as well.

The answer 12288 should have been a warning: this format's largest number is 127, so a result of 12288 is impossible.
:::

## Try it yourself

:::try Start easy, finish at exam standard
Q: Convert the binary number 0.1101 to denary.
A: \(\tfrac12 + \tfrac14 + \tfrac1{16} = 0.8125\).
Q: Convert 0.4375 to binary.
A: \(0.4375 \times 2 = 0.875\) (0), \(0.875 \times 2 = 1.75\) (1), \(0.75 \times 2 = 1.5\) (1), \(0.5 \times 2 = 1.0\) (1). The answer is 0.0111.
Q: A 4-bit exponent holds 1010. What is its denary value, and which way does the point move?
A: \(-8 + 2 = -6\), so the binary point moves 6 places to the left.
Q: An 8-bit mantissa and a 4-bit exponent hold 01010000 0010. Convert the number to denary.
A: The exponent is 2. The mantissa is 0.1010000, which is 0.625. Moving the point 2 places right gives 010.1000, which is 2.5.
Q: Which of these mantissas are normalised? (a) 01001100 (b) 10110000 (c) 11100000 (d) 00110000
A: A mantissa is normalised if its first two bits differ. (a) 01, yes. (b) 10, yes. (c) 11, no. (d) 00, no.
Q: Write −1.75 as a normalised number with an 8-bit mantissa and a 4-bit exponent.
A: 1.75 is 1.11 in binary, so the positive mantissa is 0.1110000 with exponent +1. Invert to 1.0001111 and add 1 to get 1.0010000. The exponent is 0001. The answer is 10010000 0001. Check: \(-0.875 \times 2 = -1.75\).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A floating-point number is stored with an 8-bit mantissa and a 4-bit exponent, both in two's complement. The mantissa is 01101000 and the exponent is 0100. Convert the number to denary.
H: Find the exponent first, then move the point that many places.
A: Mark points:

- the exponent 0100 is 4 [B1]
- the point in 0.1101000 moves 4 places right, giving 01101.000 [B1]
- \(8 + 4 + 1 = 13\) [B1]

Q: [3 marks] ★★ The same format holds mantissa 10110000 and exponent 1110. Convert the number to denary.
H: The exponent is negative, so the point moves left. The mantissa is negative.
A: Mark points:

- the exponent 1110 is \(-8 + 4 + 2 = -2\) [B1]
- the mantissa is \(-1 + \tfrac14 + \tfrac18 = -\tfrac58\), or the point moves 2 places left [B1]
- \(-\tfrac58 \times 2^{-2} = -\tfrac{5}{32} = -0.15625\) [B1]

Q: [3 marks] ★★ Write 22.5 as a normalised floating-point number with an 8-bit mantissa and a 4-bit exponent, both in two's complement.
H: 22.5 is \(16 + 4 + 2 + 0.5\).
A: Mark points:

- 22.5 in binary is 10110.1 [B1]
- the point moves 5 places left to give 0.101101, so the exponent is +5, which is 0101 [B1]
- the mantissa is 0.1011010 and the answer is 01011010 0101 [B1]

Q: [3 marks] ★★ Write −5.25 as a normalised floating-point number with an 8-bit mantissa and a 4-bit exponent, both in two's complement.
H: Find the positive pattern first, then take the two's complement of the mantissa.
A: Mark points:

- 5.25 is 101.01, which is 0.1010100 with exponent +3 (0011) [B1]
- two's complement of the mantissa: invert to 1.0101011, add 1 to give 1.0101100 [B1]
- the answer is 10101100 0011 [B1]

Q: [2 marks] ★ State two reasons why floating-point numbers are normalised.
A: Mark points (any two):

- to store the number with the greatest possible precision, because no mantissa bit is wasted on a leading 0 (or 1) [B1]
- so that each number has only one representation, which makes comparing two numbers simpler [B1]

Q: [2 marks] ★ A floating-point format of 12 bits has a mantissa of 8 bits and an exponent of 4 bits. State the effect on the range and the precision of moving one bit from the mantissa to the exponent.
A: Mark points:

- the range increases, because a bigger exponent is possible [B1]
- the precision decreases, because the mantissa has fewer bits [B1]

Q: [5 marks] ★★ A floating-point format has a 6-bit mantissa and a 4-bit exponent, both in two's complement. Give the pattern and the denary value of (a) the largest positive number [2], (b) the smallest positive number that is normalised [2] and (c) the most negative number [1].
H: The largest positive has the largest mantissa and the largest exponent.
A: (a) 011111 0111 [B1]. The value is \(\tfrac{31}{32} \times 2^7 = 124\). [B1]

(b) 010000 1000 [B1]. The value is \(\tfrac12 \times 2^{-8} = \tfrac1{512}\), which is 0.001953125. [B1]

(c) The most negative value is 100000 0111, which is \(-1 \times 2^7 = -128\). [B1]

Q: [4 marks] ★★★ A program adds 0.1 to a variable `Total` ten times and then outputs "Equal" if `Total = 1.0`. The program does not output "Equal". Explain why, and describe how the test could be made reliable.
H: Think about how 0.1 is stored, and what repeated addition does to the error.
A: Mark points:

- 0.1 cannot be represented exactly in binary, because its binary expansion is recurring [B1]
- so it is stored as an approximation, with a rounding error [B1]
- the errors accumulate over the ten additions, so the total is not exactly 1.0 [B1]
- compare using a tolerance, for example testing whether the difference is less than a very small number, or count in whole units (integers) [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A scientist uses 16 bits for each stored measurement. Format X has a 12-bit mantissa and a 4-bit exponent. Format Y has a 10-bit mantissa and a 6-bit exponent. Distances in the experiment range from 0.001 metres to 10 000 000 metres. (a) Calculate the largest positive value of each format. [2] (b) Calculate the smallest positive normalised value of each format. [2] (c) State, with reasons, which format the scientist should use, and which is better for precision. [2]
H: The largest value of a format is \(\left(1 - 2^{-(m-1)}\right) \times 2^{2^{e-1}-1}\); the smallest positive normalised value is \(2^{-1} \times 2^{-2^{e-1}}\).
H: X has the better precision, but is its range big enough?
A: (a) Format X: \(\left(1 - 2^{-11}\right) \times 2^{7} = 127.9375\) [B1]. Format Y: \(\left(1 - 2^{-9}\right) \times 2^{31} = 2\,143\,289\,344\) [B1].

(b) Format X: \(2^{-1} \times 2^{-8} = 2^{-9} \approx 0.00195\) [B1]. Format Y: \(2^{-1} \times 2^{-32} = 2^{-33} \approx 1.2 \times 10^{-10}\) [B1].

(c) Format Y, because X cannot store 10 000 000 (its largest value is only about 128) while Y can store the whole range from 0.001 to 10 000 000 [B1]. Format X has more mantissa bits (11 after the point against 9), so it is the more precise [B1], but its range is too small for the data.

Q: [4 marks] ★★★ A format has a 4-bit mantissa and a 2-bit exponent, both in two's complement (the figure earlier in this section shows its positive normalised values). (a) How many different positive normalised values does it have? [1] (b) Show that the gap between neighbouring values with exponent \(-2\) is 0.03125, and state the gap for exponent 1. [2] (c) State what this shows about the precision of large numbers compared with small ones. [1]
H: With a 4-bit mantissa, the mantissa of a positive normalised number can be 0.100, 0.101, 0.110 or 0.111.
A: (a) Four mantissas for each of four exponents gives \(4 \times 4 = 16\) values [B1].

(b) The mantissas differ by \(\tfrac18\), so for exponent \(-2\) the gap is \(\tfrac18 \times 2^{-2} = \tfrac1{32} = 0.03125\) [B1]. For exponent 1 it is \(\tfrac18 \times 2 = 0.25\) [B1].

(c) The gaps get bigger as the numbers get bigger, so large numbers are stored with a larger absolute error than small numbers [B1].
:::

## Quiz

:::quiz
? Which mantissa is normalised and negative?
- 11001100
+ 10110000
- 01101100
- 00110000
> A negative mantissa is normalised when it starts 10. 11001100 starts 11, so it is not normalised, and the other two are positive mantissas.
? In a floating-point number, which part mainly decides the range of values that can be stored?
- the mantissa
+ the exponent
- the sign bit of the mantissa
- the position of the binary point in the mantissa
> The exponent decides how far the point can move, so it sets the range. The mantissa decides the precision.
? A 12-bit format moves one bit from the exponent to the mantissa. What happens?
- The range increases and the precision decreases.
+ The range decreases and the precision increases.
- Both the range and the precision increase.
- Neither changes, because the total number of bits is the same.
> Fewer exponent bits means a smaller range; more mantissa bits means more precision. The total number of bits does not change, but how they are shared does.
? What is the denary value of the 4-bit two's complement exponent 1101?
- 13
- −5
+ −3
- 3
> \(-8 + 4 + 1 = -3\). Reading it as unsigned gives 13 and forgetting the 4 gives −5.
? Why can the number 0.1 not be stored exactly in binary?
- Binary cannot store numbers less than 1.
+ Its binary expansion is recurring, so it cannot be completed in a fixed number of bits.
- The exponent is too small.
- Computers round every number to one decimal place.
> 0.1 is \(\tfrac1{10}\) and 10 is not a power of 2, so its binary expansion goes on for ever: 0.0001100110011… The stored value is only the nearest approximation.
? An 8 + 4 format has a largest value of 127. A result of 200 is produced. What is this error called?
- Underflow
+ Overflow
- Rounding error
- Truncation
> The result is larger than the largest storable value, which is overflow. Underflow is a result too close to zero.
? Normalising the pattern 00101100 0101 gives which pattern?
- 00101100 0110
+ 01011000 0100
- 01011000 0101
- 10110000 0100
> Shift the mantissa left one place and subtract 1 from the exponent: 01011000 with exponent 0100. The value is unchanged: 11 in both. 01011000 0101 would double the value.
? A student uses `if total == 1.0` after adding 0.1 ten times and the test fails. What is the best fix?
- Add 0.1 eleven times.
+ Test whether the difference between total and 1.0 is smaller than a small tolerance.
- Declare total as an INTEGER and keep adding 0.1.
- Use a larger exponent.
> The test fails because of accumulated rounding error. A tolerance accepts values that are very close. A larger exponent does not make the mantissa more accurate.
:::

:::checklist What you can now do
- [ ] I can describe the format of a binary floating-point number: a two's complement mantissa with the point after the sign bit, and a two's complement exponent.
- [ ] I can convert a floating-point pattern to denary, including negative mantissas and negative exponents.
- [ ] I can convert a denary number (positive or negative) to a normalised floating-point pattern.
- [ ] I can state what normalisation is, why it is used, and normalise a number by shifting.
- [ ] I can state the effect of changing the number of bits allocated to the mantissa and the exponent (range against precision).
- [ ] I can work out the largest, smallest positive normalised and most negative values of a format.
- [ ] I can explain why a binary representation is only an approximation and why 0.1 cannot be stored exactly.
- [ ] I can explain overflow, underflow and rounding errors, and how to avoid them in a program.
:::

:::recap
- Binary fractions have place values ½, ¼, ⅛, … Multiply a fraction by 2 repeatedly to convert it to binary. Only fractions whose denominator is a power of 2 end; 0.1 does not.
- Fixed point has one range and one step size. Floating point stores a **mantissa** and an **exponent**: value = mantissa × 2^exponent.
- Both are two's complement. The mantissa is a fraction with the point after the sign bit. A negative exponent moves the point left.
- Floating point to denary: exponent first, move the point, read by place values. Denary to floating point: write in binary, move the point until it is 0.1…, the number of places is the exponent, then take the two's complement for a negative number.
- A normalised mantissa has first two bits different: 01… (positive) or 10… (negative). Normalise by shifting left and subtracting 1 from the exponent. Normalising gives maximum precision and a single representation.
- For 8 + 4 bits: largest 127, smallest positive normalised 1/512, most negative −128. More mantissa bits: more precision. More exponent bits: more range.
- Rounding errors come from the finite mantissa and accumulate. Do not test reals for equality; use a tolerance or integers.
- Overflow: the result is too large for the exponent. Underflow: too close to zero, stored as 0.
:::

:::links
- practise: [Floating-point numbers: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/13-data-representation-/floating-point-numbers-representation-and-manipulation/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- explore: [Floating-point converter](https://www.101computing.net/floating-point-binary-converter/) · 101 Computing · convert between floating point and denary and check your working
- explore: [Binary conversion practice](https://www.101computing.net/binary-converter/) · 101 Computing · practise the binary skills this chapter builds on
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists
- read: [ZNotes 9618 notes](https://znotes.org/caie/as-level/computer-science-9618/) · ZNotes · free summary notes for the syllabus
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · run the converters in this chapter line by line

Links checked 13 November 2026.
:::

Next: [Protocols, TCP/IP and packet switching](#cs.networks2)
