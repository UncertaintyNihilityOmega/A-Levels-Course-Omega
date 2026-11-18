@chapter cs.algorithms2
@title Searching, sorting and Big O
@level a2
@paper CAIE 9618 Papers 3 and 4
@time 6–8 hours
@summary You will write binary search, insertion sort and the efficient bubble sort in pseudocode and Python, trace them, and count their comparisons on sorted, reversed and random data. Then you will use Big O notation to compare algorithms by the time they take and the memory they use, in the best and the worst case.

:::why
Two programs can give the same answer and still be very different: one finishes a search of a million records in 20 steps, the other needs a million. Computer scientists compare algorithms by counting steps and memory, not by timing them on one machine, and Paper 3 asks you to do exactly that. Paper 4 asks you to write the algorithms as working code, test them and show the output.
:::

**Before you start**, you should be comfortable with arrays, linear search and the bubble sort from [Data types, records and arrays](#cs.datatypes), with functions from [Procedures, functions and parameters](#cs.procedures), and with dry-running an algorithm in a trace table from [Algorithms and computational thinking](#cs.algorithms).

:::try Warm-up
Q: A linear search looks for a value in an array of 10 elements and finds it at position 7. How many comparisons does it make? (from [Data types, records and arrays](#cs.datatypes))
A: 7. A linear search stops as soon as the value is found, so it makes one comparison for each element it checks.
Q: What does `13 DIV 2` give, and what does `13 MOD 2` give? (from [Programming from zero](#cs.f.basics))
A: `13 DIV 2` is 6 (the whole number of times 2 goes into 13) and `13 MOD 2` is 1 (the remainder).
Q: In an efficient bubble sort, what are the two improvements on the basic version? (from [Data types, records and arrays](#cs.datatypes))
A: The boundary shrinks after each pass (the largest value is already in place), and a flag stops the sort when a whole pass makes no swaps.
:::

:::note How code appears in this chapter
Algorithms are shown in Cambridge pseudocode first, then in Python. Python lists count from 0, so a program either uses index `i - 1` for pseudocode position `i`, or keeps element 0 unused so that the numbers match. Each Python program says which it does. Every Python program in this chapter has been run and its output block is exactly what it prints.
:::

## How do we compare algorithms?

A search of 11 names and a search of 11 million names are the same job at different sizes. What matters is how the work grows as the number of items, written \(n\), grows. This chapter measures that growth by counting **comparisons** (and, for sorts, **swaps** or **shifts**), because a count is the same on every computer, while a stopwatch time is not.

Three questions are asked of every algorithm in this chapter.

- How many steps does it take, and how does that change when \(n\) doubles?
- How much extra memory does it need besides the data itself?
- Does the answer depend on how the data starts: already in order, reversed or in a random order?

## Searching a sorted array: binary search

In [Data types, records and arrays](#cs.datatypes) you wrote a linear search. It works on any array, but it is slow on a big one: if the item is not there, it checks every element. The two-line recap of its cost is worth having in front of you.

- Item at position 1: 1 comparison (the **best case**).
- Item at position \(n\), or not present: \(n\) comparisons (the **worst case**).
- On average, for an item that is present, about half the elements are checked.

Here it is as a function that returns the position of the target, or −1 if it is not there. The array `Values` holds 11 integers.

```pseudocode
FUNCTION LinearSearch(Target : INTEGER) RETURNS INTEGER
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 11
      IF Values[Index] = Target THEN
         RETURN Index
      ENDIF
   NEXT Index
   RETURN -1
ENDFUNCTION
```

Now suppose the 11 values are **in order**. You do not need to start at the beginning. If you open a dictionary to look for "lemon", you do not read from "aardvark": you open near the middle, see that you have reached "mango", and know that "lemon" is in the first half. Each look throws away half of what is left.

:::analogy
A friend thinks of a whole number from 1 to 100 and answers only "higher" or "lower" to your guesses. The best first guess is 50. If the answer is "lower", the number is in 1 to 49, so you guess 25, and so on. You never need more than 7 guesses, because \(2^7 = 128\) is more than 100. A binary search plays this game with an array.
:::

:::def Binary search
A search for a value in a sorted array that compares the target with the middle element and discards the half that cannot contain it. The remaining half is searched in the same way, until the value is found or no elements are left.
:::

Binary search has two conditions. If either is false, it gives wrong answers.

:::key Conditions for a binary search
- The data must be **sorted** (into the order the comparison uses), because "the target is smaller than the middle value" only tells you which half to keep if the halves are in order.
- The data must allow **direct access by position**, as an array does, so the middle element can be read at once. A linked list cannot do this: reaching the middle means following pointers from the start.
:::

### The algorithm

Three variables mark the part of the array still in play: `Low` (the first position), `High` (the last position) and `Mid` (the middle one). Each time round the loop, `Mid` is calculated, `Values[Mid]` is compared with the target, and either the search ends or one end moves past `Mid`.

:::key Binary search (iterative)
1. Set `Low` to the first position and `High` to the last.
2. While `Low <= High`, calculate `Mid ← (Low + High) DIV 2`.
3. If `Values[Mid]` equals the target, it is found at `Mid`.
4. If `Values[Mid]` is less than the target, the target can only be to the right: `Low ← Mid + 1`.
5. Otherwise it can only be to the left: `High ← Mid - 1`.
6. If the loop ends because `Low > High`, no element is left: the target is not in the array.
:::

```pseudocode
DECLARE Values : ARRAY[1:11] OF INTEGER

FUNCTION BinarySearch(Target : INTEGER) RETURNS INTEGER
   DECLARE Low, High, Mid : INTEGER
   Low ← 1
   High ← 11
   WHILE Low <= High
      Mid ← (Low + High) DIV 2
      IF Values[Mid] = Target THEN
         RETURN Mid
      ENDIF
      IF Values[Mid] < Target THEN
         Low ← Mid + 1
      ELSE
         High ← Mid - 1
      ENDIF
   ENDWHILE
   RETURN -1
ENDFUNCTION
```

The function returns the position of the target or −1. The value −1 is safe as a "not found" signal because no position is negative. The `+ 1` and `- 1` matter: `Mid` has just been compared and rejected, so it must not be searched again.

Take the sorted array `Values` holding 3, 8, 12, 17, 21, 26, 30, 35, 41, 48 and 55 (positions 1 to 11). The figure follows a search for 35.

:::html
<figure class="fig small"><svg viewBox="0 0 340 198" role="img" aria-label="Binary search for 35 in a sorted array of eleven numbers: 3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55. Pass 1 has Low 1, High 11, Mid 6 (26). Pass 2 has Low 7, High 11, Mid 9 (41). Pass 3 has Low 7, High 8, Mid 7 (30). Pass 4 has Low 8, High 8, Mid 8 (35), so 35 is found at position 8."><text class="tl te" x="52" y="32">pass 1</text><rect class="fm s-acc sw2" x="60" y="14" width="24" height="26"/><text class="tl tc" x="72" y="32">3</text><text class="tl tc tb" x="72" y="54">L</text><rect class="fm s-acc sw2" x="84" y="14" width="24" height="26"/><text class="tl tc" x="96" y="32">8</text><rect class="fm s-acc sw2" x="108" y="14" width="24" height="26"/><text class="tl tc" x="120" y="32">12</text><rect class="fm s-acc sw2" x="132" y="14" width="24" height="26"/><text class="tl tc" x="144" y="32">17</text><rect class="fm s-acc sw2" x="156" y="14" width="24" height="26"/><text class="tl tc" x="168" y="32">21</text><rect class="f1 s-acc sw2" x="180" y="14" width="24" height="26"/><text class="tl tc" x="192" y="32">26</text><text class="tl tc tb" x="192" y="54">M</text><rect class="fm s-acc sw2" x="204" y="14" width="24" height="26"/><text class="tl tc" x="216" y="32">30</text><rect class="fm s-acc sw2" x="228" y="14" width="24" height="26"/><text class="tl tc" x="240" y="32">35</text><rect class="fm s-acc sw2" x="252" y="14" width="24" height="26"/><text class="tl tc" x="264" y="32">41</text><rect class="fm s-acc sw2" x="276" y="14" width="24" height="26"/><text class="tl tc" x="288" y="32">48</text><rect class="fm s-acc sw2" x="300" y="14" width="24" height="26"/><text class="tl tc" x="312" y="32">55</text><text class="tl tc tb" x="312" y="54">H</text><text class="tl te" x="52" y="78">pass 2</text><rect class="fp ln-m thin" x="60" y="60" width="24" height="26"/><text class="tl tc" x="72" y="78">3</text><rect class="fp ln-m thin" x="84" y="60" width="24" height="26"/><text class="tl tc" x="96" y="78">8</text><rect class="fp ln-m thin" x="108" y="60" width="24" height="26"/><text class="tl tc" x="120" y="78">12</text><rect class="fp ln-m thin" x="132" y="60" width="24" height="26"/><text class="tl tc" x="144" y="78">17</text><rect class="fp ln-m thin" x="156" y="60" width="24" height="26"/><text class="tl tc" x="168" y="78">21</text><rect class="fp ln-m thin" x="180" y="60" width="24" height="26"/><text class="tl tc" x="192" y="78">26</text><rect class="fm s-acc sw2" x="204" y="60" width="24" height="26"/><text class="tl tc" x="216" y="78">30</text><text class="tl tc tb" x="216" y="100">L</text><rect class="fm s-acc sw2" x="228" y="60" width="24" height="26"/><text class="tl tc" x="240" y="78">35</text><rect class="f1 s-acc sw2" x="252" y="60" width="24" height="26"/><text class="tl tc" x="264" y="78">41</text><text class="tl tc tb" x="264" y="100">M</text><rect class="fm s-acc sw2" x="276" y="60" width="24" height="26"/><text class="tl tc" x="288" y="78">48</text><rect class="fm s-acc sw2" x="300" y="60" width="24" height="26"/><text class="tl tc" x="312" y="78">55</text><text class="tl tc tb" x="312" y="100">H</text><text class="tl te" x="52" y="124">pass 3</text><rect class="fp ln-m thin" x="60" y="106" width="24" height="26"/><text class="tl tc" x="72" y="124">3</text><rect class="fp ln-m thin" x="84" y="106" width="24" height="26"/><text class="tl tc" x="96" y="124">8</text><rect class="fp ln-m thin" x="108" y="106" width="24" height="26"/><text class="tl tc" x="120" y="124">12</text><rect class="fp ln-m thin" x="132" y="106" width="24" height="26"/><text class="tl tc" x="144" y="124">17</text><rect class="fp ln-m thin" x="156" y="106" width="24" height="26"/><text class="tl tc" x="168" y="124">21</text><rect class="fp ln-m thin" x="180" y="106" width="24" height="26"/><text class="tl tc" x="192" y="124">26</text><rect class="f1 s-acc sw2" x="204" y="106" width="24" height="26"/><text class="tl tc" x="216" y="124">30</text><text class="tl tc tb" x="216" y="146">LM</text><rect class="fm s-acc sw2" x="228" y="106" width="24" height="26"/><text class="tl tc" x="240" y="124">35</text><text class="tl tc tb" x="240" y="146">H</text><rect class="fp ln-m thin" x="252" y="106" width="24" height="26"/><text class="tl tc" x="264" y="124">41</text><rect class="fp ln-m thin" x="276" y="106" width="24" height="26"/><text class="tl tc" x="288" y="124">48</text><rect class="fp ln-m thin" x="300" y="106" width="24" height="26"/><text class="tl tc" x="312" y="124">55</text><text class="tl te" x="52" y="170">pass 4</text><rect class="fp ln-m thin" x="60" y="152" width="24" height="26"/><text class="tl tc" x="72" y="170">3</text><rect class="fp ln-m thin" x="84" y="152" width="24" height="26"/><text class="tl tc" x="96" y="170">8</text><rect class="fp ln-m thin" x="108" y="152" width="24" height="26"/><text class="tl tc" x="120" y="170">12</text><rect class="fp ln-m thin" x="132" y="152" width="24" height="26"/><text class="tl tc" x="144" y="170">17</text><rect class="fp ln-m thin" x="156" y="152" width="24" height="26"/><text class="tl tc" x="168" y="170">21</text><rect class="fp ln-m thin" x="180" y="152" width="24" height="26"/><text class="tl tc" x="192" y="170">26</text><rect class="fp ln-m thin" x="204" y="152" width="24" height="26"/><text class="tl tc" x="216" y="170">30</text><rect class="f1 s-acc sw2" x="228" y="152" width="24" height="26"/><text class="tl tc" x="240" y="170">35</text><text class="tl tc tb" x="240" y="192">LMH</text><rect class="fp ln-m thin" x="252" y="152" width="24" height="26"/><text class="tl tc" x="264" y="170">41</text><rect class="fp ln-m thin" x="276" y="152" width="24" height="26"/><text class="tl tc" x="288" y="170">48</text><rect class="fp ln-m thin" x="300" y="152" width="24" height="26"/><text class="tl tc" x="312" y="170">55</text></svg><figcaption>A search for 35. Each pass halves the part of the array still in play. The cell marked M is the middle one that is compared; L and H mark Low and High. Cells outside the current range are never looked at again. 35 is found at position 8 on pass 4.</figcaption></figure>
:::

:::eg Tracing a binary search that succeeds and one that fails
Using the array `Values` above (3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55), complete a trace table for `BinarySearch(35)` and for `BinarySearch(20)`.

Each row is one trip round the loop: write `Low` and `High`, work out `Mid` with DIV, then compare `Values[Mid]` with the target and decide which end moves.

| Target | Low | High | Mid | Values[Mid] | Decision |
|---|---|---|---|---|---|
| 35 | 1 | 11 | 6 | 26 | 26 < 35, so Low ← 7 |
| | 7 | 11 | 9 | 41 | 41 > 35, so High ← 8 |
| | 7 | 8 | 7 | 30 | 30 < 35, so Low ← 8 |
| | 8 | 8 | 8 | 35 | equal: RETURN 8 |

The search for 35 makes 4 comparisons and returns 8.

| Target | Low | High | Mid | Values[Mid] | Decision |
|---|---|---|---|---|---|
| 20 | 1 | 11 | 6 | 26 | 26 > 20, so High ← 5 |
| | 1 | 5 | 3 | 12 | 12 < 20, so Low ← 4 |
| | 4 | 5 | 4 | 17 | 17 < 20, so Low ← 5 |
| | 5 | 5 | 5 | 21 | 21 > 20, so High ← 4 |

Now `Low` is 5 and `High` is 4, so `Low <= High` is false, the loop ends and the function returns −1. A failed search also makes 4 comparisons, the same as the longest successful one.
:::

Here is the same function in Python. This program keeps element 0 of the list unused, so that positions 1 to 11 are list indexes 1 to 11 and the numbers match the trace tables. It prints each trip round the loop.

```python
values = [None, 3, 8, 12, 17, 21, 26, 30, 35, 41, 48, 55]


def binary_search(target):
    low = 1
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        print("Low", low, "High", high, "Mid", mid, "Values[Mid]", values[mid])
        if values[mid] == target:
            return mid
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print("Position of 35:", binary_search(35))
print("Position of 20:", binary_search(20))
```

Output:

```output
Low 1 High 11 Mid 6 Values[Mid] 26
Low 7 High 11 Mid 9 Values[Mid] 41
Low 7 High 8 Mid 7 Values[Mid] 30
Low 8 High 8 Mid 8 Values[Mid] 35
Position of 35: 8
Low 1 High 11 Mid 6 Values[Mid] 26
Low 1 High 5 Mid 3 Values[Mid] 12
Low 4 High 5 Mid 4 Values[Mid] 17
Low 5 High 5 Mid 5 Values[Mid] 21
Position of 20: -1
```

The widget below runs the same algorithm. Press Step to follow Low, Mid and High under the bars, and change the target to see a search that fails. Switch to Linear with the same target to compare the counts.

:::html
<div class="widget" data-w="cs-sort" data-algo="binary" data-values="3,8,12,17,21,26,30,35,41,48,55" data-target="35"></div>
:::

:::warn Two classic binary search slips
**Using the algorithm on unsorted data.** The code runs without any error and returns −1 or the wrong position, so the fault is easy to miss. Check that the data is sorted first.

**Moving `Low` or `High` to `Mid` instead of past it.** If `Low ← Mid` is written, then with `Low` 10, `High` 11 and a target above `Values[10]`, `Mid` is 10 again, `Low` stays 10 and the loop never ends.
:::

### How many comparisons?

Each pass of the loop compares the target with one element and keeps at most half of the rest. So the number of elements that might hold the target goes \(n, n/2, n/4, \dots\) down to 1. How many times can you halve \(n\) before reaching 1? That count is \(\log_2 n\), and one more comparison is made on the last element.

:::key Binary search: worst case
For \(n\) items the greatest number of comparisons is \(\lfloor \log_2 n \rfloor + 1\), where \(\lfloor x \rfloor\) means "round down to a whole number". Equivalently, it is the smallest \(k\) with \(2^k > n\). **Doubling \(n\) adds one comparison.**
:::

For \(n = 1000\): \(2^9 = 512\) is less than 1000 and \(2^{10} = 1024\) is more, so \(\lfloor \log_2 1000 \rfloor = 9\) and the worst case is 10 comparisons. A linear search of 1000 items may need 1000. With a million items, \(2^{19} = 524\,288\) is below \(10^6\) and \(2^{20} = 1\,048\,576\) is above it, so binary search needs at most 20.

| Items \(n\) | Linear search, worst case | Binary search, worst case |
|---|---|---|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1000 | 1000 | 10 |
| 1 000 000 | 1 000 000 | 20 |

This program counts the comparisons for every possible target (and for one value below and one above the list) in sorted lists of different lengths, and prints the largest count for each.

```python
def comparisons(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        count = count + 1
        if sorted_list[mid] == target:
            return count
        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return count


for n in [1, 3, 7, 10, 100, 1000, 2000]:
    data = list(range(n))
    worst = 0
    for target in range(-1, n + 1):
        worst = max(worst, comparisons(data, target))
    print("n =", n, "worst case:", worst)
```

Output:

```output
n = 1 worst case: 1
n = 3 worst case: 2
n = 7 worst case: 3
n = 10 worst case: 4
n = 100 worst case: 7
n = 1000 worst case: 10
n = 2000 worst case: 11
```

This Python program counts from 0 (`low = 0`, `high = len - 1`), which is how Paper 4 answers usually go. The counts are the same as in pseudocode. Notice \(n = 1000\) gives 10 and \(n = 2000\) gives 11: doubling the data added one comparison.

### Choosing between linear and binary search

:::exam Which search, and why?
Binary search is faster, but it is not always the right answer. Say which conditions hold in the scenario. If the data is **already sorted** and held in an **array**, binary search is far fewer comparisons. If the data is **unsorted** and you will search it **once**, use a linear search: sorting first costs more than one scan. If the data is in a **linked list**, binary search cannot reach the middle directly, so a linear search follows the pointers instead. If the data is searched **many times** and changes rarely, sorting once and using binary search each time pays off (the stretch question at the end of this chapter works out when).
:::

## Insertion sort

Binary search needs sorted data, so you need a way of sorting. You already know bubble sort. **Insertion sort** works the way most people sort playing cards in their hand: pick up the next card and slide it into the right place among the cards you are already holding.

:::def Insertion sort
A sort that builds a sorted part at the front of the array one element at a time. Each pass takes the next unsorted element, shifts the larger elements of the sorted part one place to the right, and inserts the element into the gap.
:::

At the start the sorted part is just the first element (one element is always in order). Each pass makes it one element longer. After pass \(p\), the first \(p + 1\) elements are in order, but they are not necessarily in their final positions, because a later, smaller element may still be inserted in front of them. That is the difference from bubble sort, where each pass puts one value in its final place.

Watch the six values 29, 10, 14, 37, 13 and 5 sorted into ascending order. The elements in the sorted part are in **bold**, and each row shows the array after that pass.

| After pass | Element inserted | Array | Shifts |
|---|---|---|---|
| start | | **29**, 10, 14, 37, 13, 5 | |
| 1 | 10 | **10, 29**, 14, 37, 13, 5 | 1 |
| 2 | 14 | **10, 14, 29**, 37, 13, 5 | 1 |
| 3 | 37 | **10, 14, 29, 37**, 13, 5 | 0 |
| 4 | 13 | **10, 13, 14, 29, 37**, 5 | 3 |
| 5 | 5 | **5, 10, 13, 14, 29, 37** | 5 |

On pass 4 the value 13 is taken out, 37, 29 and 14 each shift one place right, and 13 drops into the gap that is left in front of 14. On pass 3 the value 37 is already bigger than everything in the sorted part, so nothing moves.

:::key Insertion sort (ascending)
```pseudocode
FOR Index ← 2 TO N
   Item ← Values[Index]
   Position ← Index - 1
   WHILE Position >= 1 AND Values[Position] > Item
      Values[Position + 1] ← Values[Position]
      Position ← Position - 1
   ENDWHILE
   Values[Position + 1] ← Item
NEXT Index
```
`Item` holds the value being inserted, so it is not lost when a larger value is copied over its old place. `Position` moves left while the element on its left is larger. When the loop stops, `Position + 1` is the gap.
:::

The loop condition tests `Position >= 1` first. When `Position` reaches 0, the gap is at the very front and there is no `Values[0]` to compare with. The Pseudocode Guide does not say whether `AND` stops at the first false test, but Cambridge's own mark schemes write the loop this way, with the position test first (for example 9618/31, June 2021). In Python, `and` does stop at the first false test, so putting `position >= 0` first protects the second. Code that must not rely on this uses a Boolean flag, as the Python version below does. For descending order, change `>` to `<`.

For the full program, here is the complete array `Values` of six elements, with the declarations.

```pseudocode
DECLARE Values : ARRAY[1:6] OF INTEGER
DECLARE Index, Position, Item : INTEGER

// Values holds 29, 10, 14, 37, 13, 5
FOR Index ← 2 TO 6
   Item ← Values[Index]
   Position ← Index - 1
   WHILE Position >= 1 AND Values[Position] > Item
      Values[Position + 1] ← Values[Position]
      Position ← Position - 1
   ENDWHILE
   Values[Position + 1] ← Item
NEXT Index
```

:::eg Trace one pass of insertion sort
Pass 4 of the sort above starts with `Index` 5 and the array 10, 14, 29, 37, 13, 5. Complete a trace table with columns Index, Item, Position and `Values[1]` to `Values[5]`.

The first row holds the values after `Item ← Values[5]` and `Position ← 4`. Then each time round the WHILE loop, one value moves right and `Position` goes down by one. A blank cell means "unchanged".

| Index | Item | Position | Values[1] | Values[2] | Values[3] | Values[4] | Values[5] |
|---|---|---|---|---|---|---|---|
| 5 | 13 | 4 | 10 | 14 | 29 | 37 | 13 |
| | | 3 | | | | | 37 |
| | | 2 | | | | 29 | |
| | | 1 | | | 14 | | |
| | | | | 13 | | | |

When `Position` is 1, `Values[1]` is 10, which is not greater than 13, so the loop stops. The last row is `Values[Position + 1] ← Item`, which puts 13 in element 2. The array is now 10, 13, 14, 29, 37, with the 5 still waiting. Three shifts were made, and the loop tested four elements against 13: 37, 29, 14 (all larger) and 10 (not larger).
:::

Python version. The loop here uses a Boolean flag, `moving`, so that every comparison of an element with the item is counted in one place. It prints the list after each pass.

```python
values = [29, 10, 14, 37, 13, 5]
comparisons = 0
shifts = 0
for index in range(1, len(values)):
    item = values[index]
    position = index - 1
    moving = True
    while moving and position >= 0:
        comparisons = comparisons + 1
        if values[position] > item:
            values[position + 1] = values[position]
            shifts = shifts + 1
            position = position - 1
        else:
            moving = False
    values[position + 1] = item
    print("After pass", index, values)
print("Comparisons:", comparisons, "Shifts:", shifts)
```

Output:

```output
After pass 1 [10, 29, 14, 37, 13, 5]
After pass 2 [10, 14, 29, 37, 13, 5]
After pass 3 [10, 14, 29, 37, 13, 5]
After pass 4 [10, 13, 14, 29, 37, 5]
After pass 5 [5, 10, 13, 14, 29, 37]
Comparisons: 13 Shifts: 10
```

This list starts at index 0, so `index` 1 in Python is `Index` 2 in pseudocode, which is why Python's "pass 1" matches the first pass of the table. The comparisons are 1, 2, 1, 4 and 5 for the five passes, which add up to 13.

Use the widget to watch the elements shift. Try the "reversed" and "already sorted" buttons and compare the counters.

:::html
<div class="widget" data-w="cs-sort" data-algo="insertion" data-values="29,10,14,37,13,5"></div>
:::

### Sorting records and strings

Insertion sort compares with `>`, so it works on strings (compared character by character by their codes) and on records, if you compare one field and move **whole records**. `Item` and the array must then be of the record type, exactly as `Temp` was for bubble sort in [Data types, records and arrays](#cs.datatypes).

## Bubble sort and insertion sort compared

Both sorts are simple and both are slow on large data, but they behave differently on different starting orders. Counting is the way to see it. For eight values:

- **Sorted** is 1, 2, 3, 4, 5, 6, 7, 8.
- **Reversed** is 8, 7, 6, 5, 4, 3, 2, 1.
- **Random** is 5, 2, 8, 1, 7, 3, 6, 4.

The program below defines the efficient bubble sort (a shrinking boundary and a no-swaps flag, as in [Data types, records and arrays](#cs.datatypes)) and the insertion sort above, each returning its counts, and runs them on the three data sets. It is the same code as before, with the printing removed.

```python
def bubble_sort(values):
    boundary = len(values) - 1
    comparisons = 0
    swaps = 0
    no_swaps = False
    while not no_swaps and boundary > 0:
        no_swaps = True
        for j in range(boundary):
            comparisons = comparisons + 1
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swaps = swaps + 1
                no_swaps = False
        boundary = boundary - 1
    return comparisons, swaps


def insertion_sort(values):
    comparisons = 0
    shifts = 0
    for index in range(1, len(values)):
        item = values[index]
        position = index - 1
        moving = True
        while moving and position >= 0:
            comparisons = comparisons + 1
            if values[position] > item:
                values[position + 1] = values[position]
                shifts = shifts + 1
                position = position - 1
            else:
                moving = False
        values[position + 1] = item
    return comparisons, shifts


data_sets = [("sorted", [1, 2, 3, 4, 5, 6, 7, 8]),
             ("reversed", [8, 7, 6, 5, 4, 3, 2, 1]),
             ("random", [5, 2, 8, 1, 7, 3, 6, 4])]
for name, data in data_sets:
    b = bubble_sort(list(data))
    i = insertion_sort(list(data))
    print(name, "- bubble:", b[0], "comparisons,", b[1], "swaps; insertion:", i[0], "comparisons,", i[1], "shifts")
```

Output:

```output
sorted - bubble: 7 comparisons, 0 swaps; insertion: 7 comparisons, 0 shifts
reversed - bubble: 28 comparisons, 28 swaps; insertion: 28 comparisons, 28 shifts
random - bubble: 25 comparisons, 14 swaps; insertion: 19 comparisons, 14 shifts
```

| Starting order (\(n = 8\)) | Bubble sort comparisons | Insertion sort comparisons | Swaps or shifts (both) |
|---|---|---|---|
| sorted | 7 | 7 | 0 |
| reversed | 28 | 28 | 28 |
| random | 25 | 19 | 14 |

Three things stand out.

- **Sorted data** is the best case for both: one pass over the data, \(n - 1 = 7\) comparisons and no movement.
- **Reversed data** is the worst case for both: every pair is out of order, so \(\tfrac{n(n-1)}{2} = 28\) comparisons and 28 swaps or shifts.
- The number of swaps in bubble sort and the number of shifts in insertion sort are always equal. Each one removes exactly one pair of elements that are in the wrong order relative to each other, and there are 14 such pairs in the random data.

The cost depends on **how far from sorted** the data starts, and on how many items there are. Insertion sort is especially good on data that is nearly sorted, because most elements move only a place or two.

:::tip Comparing sorts in an answer
"Performance depends on the initial order" is a mark point on its own. Say what the order is (sorted, reversed, nearly sorted) and what happens to the count: for the efficient bubble sort and insertion sort, a sorted list needs \(n - 1\) comparisons, and a reversed list needs \(n(n-1)/2\).
:::

Doubling the number of items does something quite different from binary search. For the worst case, \(\tfrac{n(n-1)}{2}\) comparisons give 45 for \(n = 10\), 4950 for \(n = 100\) and 499 500 for \(n = 1000\). Ten times the data takes about a hundred times the comparisons. That growth rate has a name, and the next section gives it one.

## Big O notation

Counting comparisons for one particular \(n\) is useful, but you want a statement about **every** \(n\). Big O notation gives it by keeping only the part of the count that grows fastest.

:::def Time complexity
How the time an algorithm takes (measured as the number of basic steps, such as comparisons) grows as the number of items \(n\) grows.
:::

:::def Space complexity
How the amount of memory an algorithm needs (beyond the space the input data itself occupies) grows as the number of items \(n\) grows.
:::

:::def Big O notation
A way of describing the time or space complexity of an algorithm by the term that grows fastest as \(n\) increases, with any constant multiplier removed. Unless the question says otherwise, it describes the worst case. \(O(n^2)\) is read "order n squared".
:::

Two rules turn a step count into a Big O.

:::key Finding the Big O of a step count
1. **Keep only the fastest-growing term.** \(\tfrac{n^2}{2} + \tfrac{n}{2}\) becomes \(n^2\), because for large \(n\) the \(n^2\) term is far bigger.
2. **Drop constant multipliers and constant additions.** \(3n + 7\) becomes \(n\), and \(\tfrac{n^2}{2}\) becomes \(n^2\).

Big O ignores constants because it describes the **shape of the growth**, not the speed of a particular computer. An algorithm that is \(O(n)\) will beat one that is \(O(n^2)\) once \(n\) is big enough, however the constants fall.
:::

Bubble sort's worst case is \(\tfrac{n(n-1)}{2} = \tfrac{n^2}{2} - \tfrac{n}{2}\) comparisons. Keep the fastest-growing term, \(\tfrac{n^2}{2}\), and drop the \(\tfrac12\): the worst case is \(O(n^2)\).

### The common classes

| Big O | Name | Example | What happens when \(n\) doubles |
|---|---|---|---|
| \(O(1)\) | constant | read one array element; push onto a stack | no change |
| \(O(\log n)\) | logarithmic | binary search | one more step |
| \(O(n)\) | linear | linear search; total of an array | steps double |
| \(O(n \log n)\) | linearithmic | faster sorts such as merge sort (and quick sort, on average) | a little more than double |
| \(O(n^2)\) | polynomial (quadratic) | bubble sort and insertion sort, worst case; two nested loops | steps quadruple |
| \(O(2^n)\) | exponential | trying every subset of \(n\) items | steps are squared |

You are not asked to analyse \(O(n \log n)\) sorts in detail: it is enough to know that sorts better than bubble and insertion exist and belong to this faster class. About \(O(\log n)\): the base of the logarithm does not matter in Big O, because changing the base only multiplies by a constant, and constants are dropped. "Log" does not mean base 10 here.

The program below prints, for \(n = 10\), 100 and 1000, the exact values behind the table of growth rates: \(\log_2 n\) to one decimal place, \(n \log_2 n\) rounded to a whole number, \(n^2\), and the number of digits in \(2^n\).

```python
from math import log2

for n in [10, 100, 1000]:
    print(n, round(log2(n), 1), round(n * log2(n)), n * n, len(str(2 ** n)), "digits in 2^n")
```

Output:

```output
10 3.3 33 100 4 digits in 2^n
100 6.6 664 10000 31 digits in 2^n
1000 10.0 9966 1000000 302 digits in 2^n
```

| \(n\) | \(\log_2 n\) | \(n\) | \(n \log_2 n\) | \(n^2\) | \(2^n\) |
|---|---|---|---|---|---|
| 10 | 3.3 | 10 | 33 | 100 | 1024 |
| 100 | 6.6 | 100 | 664 | 10 000 | a number with 31 digits (about \(1.27 \times 10^{30}\)) |
| 1000 | 10.0 | 1000 | 9966 | 1 000 000 | a number with 302 digits |

An \(O(2^n)\) algorithm is hopeless for all but tiny \(n\): at \(n = 100\), even if a computer did a billion steps a second, it would not finish in your lifetime. The two graphs show the other classes.

:::plot Steps against \(n\): \(n^2\) climbs far above \(n \log_2 n\) as \(n\) grows.
--f "x**2" --f "x*log(x)/log(2)" --x 1 16 --y 0 340 --label "n²" --label "n log₂ n" --legend tr --alt "Two curves for n from 1 to 16. The n squared curve rises steeply to 256 at n = 16. The n log base 2 of n curve rises gently to 64 at n = 16."
:::

:::plot Steps against \(n\): \(\log_2 n\) is almost flat, while \(n\) rises steadily.
--f "x" --f "log(x)/log(2)" --x 1 32 --y 0 42 --label "n" --label "log₂ n" --legend tr --alt "Two curves for n from 1 to 32. The n line rises steadily to 32. The log base 2 of n curve climbs slowly and reaches only 5 at n = 32."
:::

### Finding the Big O of an algorithm

To find the Big O of a piece of code, count how many times the busiest statement runs, as a function of \(n\), then apply the two rules.

:::steps
1. Decide what \(n\) is (the number of elements, rows or items).
2. Find the busiest statement: the one inside the most loops.
3. Count how many times it runs in terms of \(n\). A loop from 1 to \(n\) runs it \(n\) times; one loop inside another runs it \(n \times n\) times; a loop that halves its counter runs about \(\log_2 n\) times.
4. Loops one **after** another add; loops **inside** one another multiply.
5. Keep the fastest-growing term and drop constants.
:::

| Pseudocode | Busiest statement runs | Big O |
|---|---|---|
| `Total ← Scores[1] + Scores[2]` | once | \(O(1)\) |
| `FOR Index ← 1 TO N` then `OUTPUT Names[Index]` | \(N\) times | \(O(n)\) |
| one `FOR` over \(N\) items, then a second `FOR` over the same items | \(N + N = 2N\) | \(O(n)\) |
| `FOR I ← 1 TO N` containing `FOR J ← 1 TO N` | \(N \times N\) | \(O(n^2)\) |
| `FOR I ← 1 TO N` containing `FOR J ← 1 TO I` | \(1 + 2 + \dots + N = \tfrac{N(N+1)}{2}\) | \(O(n^2)\) |
| `WHILE M > 1` with `M ← M DIV 2` inside | \(\lfloor \log_2 M \rfloor\) times | \(O(\log n)\) |

This program counts the steps of three of these for \(n = 8\) and \(n = 16\), so you can watch what doubling does.

```python
for n in [8, 16]:
    single = 0
    for i in range(n):
        single = single + 1
    nested = 0
    for i in range(n):
        for j in range(n):
            nested = nested + 1
    halving = 0
    m = n
    while m > 1:
        m = m // 2
        halving = halving + 1
    print("n =", n, "single loop:", single, "nested loops:", nested, "halving loop:", halving)
```

Output:

```output
n = 8 single loop: 8 nested loops: 64 halving loop: 3
n = 16 single loop: 16 nested loops: 256 halving loop: 4
```

Doubling \(n\) from 8 to 16 doubles the single loop (\(O(n)\)), quadruples the nested loops (\(O(n^2)\)) and adds just one step to the halving loop (\(O(\log n)\)).

:::eg Big O of two pieces of pseudocode (exam style)
State the Big O time complexity of each piece of pseudocode, in terms of \(N\), and give a reason. [4 marks]

(a)

```pseudocode
Count ← 0
FOR Index ← 1 TO N
   IF Marks[Index] >= 50 THEN
      Count ← Count + 1
   ENDIF
NEXT Index
```

(b)

```pseudocode
FOR Row ← 1 TO N
   FOR Column ← 1 TO N
      Grid[Row, Column] ← 0
   NEXT Column
NEXT Row
```

(a) The time complexity is \(O(n)\) [B1] because the loop runs \(N\) times and does a fixed amount of work (one comparison) each time [B1].

(b) The time complexity is \(O(n^2)\) [B1] because the inner loop runs \(N\) times for each of the \(N\) rows, so the assignment runs \(N \times N\) times [B1].

Give the name of the class **and** the reason: the first mark is for the notation, the second for a reason that mentions how many times the loop runs.
:::

### Best case, worst case and average case

An algorithm's cost can depend on the data, so Big O is quoted for particular cases.

:::def Best case
The input for which the algorithm does the least work, such as the target being the first element in a linear search, or the data already being in order for insertion sort.
:::

:::def Worst case
The input for which the algorithm does the most work, such as the target being the last element or absent in a linear search, or the data being in reverse order for insertion sort. Big O is normally quoted for the worst case.
:::

The **average case** is the cost for a typical input, for example about \(n/2\) comparisons for a linear search that finds its item. All the algorithms in this chapter, with their cases:

| Algorithm | Best case | Worst case | Worst case happens when |
|---|---|---|---|
| Linear search | \(O(1)\) | \(O(n)\) | the item is last or absent |
| Binary search | \(O(1)\) | \(O(\log n)\) | the item is found last, or is absent |
| Bubble sort (basic, no flag) | \(O(n^2)\) | \(O(n^2)\) | always the same number of comparisons |
| Bubble sort (flag and boundary) | \(O(n)\) | \(O(n^2)\) | best: sorted; worst: reversed |
| Insertion sort | \(O(n)\) | \(O(n^2)\) | best: sorted; worst: reversed |

The basic bubble sort from [Data types, records and arrays](#cs.datatypes) always makes \(4 \times 4 = 16\) comparisons for five elements, even on sorted data: its best case is as bad as its worst. The flag is what gives the efficient version its \(O(n)\) best case.

### Time and memory

Memory matters as well as time. **Space complexity** counts the extra memory used while the algorithm runs, not the memory of the input.

:::def In-place algorithm
An algorithm that rearranges the data inside the array it is given, using only a small, fixed amount of extra memory (a few variables), however many items there are.
:::

- Linear search and an iterative binary search use a few variables: \(O(1)\) space.
- Bubble sort uses `Temp` and a few counters, and insertion sort uses `Item` and `Position`. Both are in-place sorts with \(O(1)\) extra space.
- A sort that copies the data into a second array of the same size needs \(O(n)\) extra space.
- A **recursive** binary search calls itself with a smaller range. Each call waits on the stack for the one below it, so it holds about \(\log_2 n\) stack frames: \(O(\log n)\) space, where the loop version needs \(O(1)\). Stack frames and recursion are the subject of [Recursion](#cs.recursion).

So there is often a trade-off: an algorithm that is faster may need more memory, and one that needs almost no memory may be slower.

:::warn Big O is not a stopwatch
\(O(n)\) does not mean "exactly \(n\) steps", and an \(O(n^2)\) algorithm is not always slower than an \(O(n)\) one: for tiny \(n\) the constants can dominate. Big O says how the cost **grows**. Also, \(O(\log n)\) is not "log base 10": the base is dropped like any constant.
:::

:::board
Cambridge 9618 asks for Big O notation for time and space complexity in A Level Paper 3. AQA A Level Computer Science (7517) also requires Big O notation for time and space, with a skeleton program for its on-screen exam.
:::

## Spot the error

:::eg Spot the error: a binary search that never ends
Question: The array `Values` has bounds 1 to 11 and holds 3, 8, 12, 17, 21, 26, 30, 35, 41, 48 and 55 in ascending order. Write a function `BinarySearch(Target)` that returns the position of `Target`, or −1 if it is not found. [7 marks]

A student wrote:

```pseudocode
01  FUNCTION BinarySearch(Target : INTEGER) RETURNS INTEGER
02     DECLARE Low, High, Mid : INTEGER
03     Low ← 1
04     High ← 11
05     WHILE Low <= High
06        Mid ← (Low + High) DIV 2
07        IF Values[Mid] = Target THEN
08           RETURN Mid
09        ENDIF
10        IF Values[Mid] < Target THEN
11           Low ← Mid
12        ELSE
13           High ← Mid - 1
14        ENDIF
15     ENDWHILE
16     RETURN -1
17  ENDFUNCTION
```

Line 01 has a correct header and return type [B1]. Lines 03 and 04 set the whole array as the range [B1]. Line 05 repeats while the range is not empty [B1]. Line 06 calculates the middle with DIV [B1]. Lines 07 and 08 return the position when the target is found [B1]. **Line 11 sets `Low ← Mid` instead of `Mid + 1`, so the middle element that has just been rejected stays in the range: the update mark is lost** [B0]. Line 16 returns −1 after the loop [B1]. The answer scores 6 out of 7.

The slip is not only a lost mark: the function can run for ever. Search for 55. Low is 1 and High is 11, Mid is 6, and 26 is less than 55, so Low becomes 6. Mid is 8, then 9, then 10, and each time Low moves up to Mid. At Low 10 and High 11, Mid is \((10 + 11) \text{ DIV } 2 = 10\) and `Values[10]` is 48, which is less than 55, so Low is set to 10 again. Nothing changes, so the loop repeats for ever. The fix is `Low ← Mid + 1` on line 11.
:::

## Try it yourself

:::try Start easy, finish at exam standard
Q: State the two conditions that must be true before a binary search can be used on an array.
A: The data must be sorted, and the elements must be directly accessible by position (as in an array), so the middle element can be read at once.
Q: `Low` is 4 and `High` is 9. What is `Mid` for `Mid ← (Low + High) DIV 2`? What is `Mid` when `Low` is 7 and `High` is 8?
A: \((4 + 9) \text{ DIV } 2 = 13 \text{ DIV } 2 = 6\). Then \((7 + 8) \text{ DIV } 2 = 15 \text{ DIV } 2 = 7\). DIV rounds down, so Mid is never past the middle.
Q: The sorted array `Items` holds 5, 12, 19, 24, 31, 40 and 47 (positions 1 to 7). List `Mid` for each pass of a binary search for 40, and say how many comparisons it makes.
A: Low 1, High 7: Mid is 4 (24 < 40), so Low is 5. Low 5, High 7: Mid is 6, and `Items[6]` is 40: found. The Mid values are 4 and 6: 2 comparisons.
Q: What is the greatest number of comparisons a binary search needs for 500 items? And for 1 item?
A: \(2^8 = 256\) is below 500 and \(2^9 = 512\) is above it, so \(\lfloor \log_2 500 \rfloor = 8\) and the worst case is \(8 + 1 = 9\) comparisons. For 1 item the only comparison is with that item: 1.
Q: Show the array after each pass of an insertion sort (ascending) on 7, 3, 9, 1.
A: Pass 1 inserts 3: 3, 7, 9, 1. Pass 2 inserts 9: it is larger than 7, so nothing moves: 3, 7, 9, 1. Pass 3 inserts 1: 9, 7 and 3 each shift right and 1 goes in front: 1, 3, 7, 9.
Q: How many comparisons and how many shifts does an insertion sort make on 6 values that are already in ascending order?
A: One comparison per pass for the 5 passes after the first element: 5 comparisons and 0 shifts. In general \(n - 1\) comparisons and no shifts.
Q: Both an efficient bubble sort and an insertion sort are run on 5 values in descending order, to put them into ascending order. Each makes the same number of comparisons. What is it, and what is the number of swaps or shifts?
A: Every pair is out of order, so each makes \(\tfrac{5 \times 4}{2} = 10\) comparisons (bubble sort: 4 + 3 + 2 + 1, insertion sort: 1 + 2 + 3 + 4) and 10 swaps or shifts.
Q: State the time complexity, in Big O notation, of reading `Scores[1]`, of a linear search, and of a binary search.
A: Reading one element is \(O(1)\); a linear search is \(O(n)\); a binary search is \(O(\log n)\).
Q: An \(O(n^2)\) sort makes about 10 000 comparisons for 100 items. Roughly how many will it make for 200 items? And an \(O(n)\) search that makes 100 comparisons for 100 items?
A: Doubling \(n\) multiplies \(n^2\) by 4, so about 40 000 comparisons. The \(O(n)\) search doubles, to about 200.
Q: Why is the extra memory used by insertion sort \(O(1)\)?
A: It sorts in the same array and needs only a few variables (`Item`, `Position`, `Index`), however many elements there are.
Q: Write the Big O of an algorithm whose steps are counted by \(5n^2 + 3n + 40\), and say why.
A: \(O(n^2)\). Keep only the fastest-growing term, \(5n^2\), and drop its constant multiplier 5.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ State the Big O time complexity of each piece of pseudocode, in terms of \(N\), and give a reason. (#cs.algorithms2)

(a)

```pseudocode
Total ← 0
FOR Index ← 1 TO N
   Total ← Total + Prices[Index]
NEXT Index
OUTPUT Total
```

(b)

```pseudocode
FOR I ← 1 TO N
   FOR J ← 1 TO N
      IF Matrix[I, J] <> Matrix[J, I] THEN
         Symmetric ← FALSE
      ENDIF
   NEXT J
NEXT I
```

H: Count how many times the busiest statement runs.
A: (a) \(O(n)\) [B1] because the loop runs \(N\) times and each time does one addition [B1].

(b) \(O(n^2)\) [B1] because the comparison inside the inner loop runs \(N\) times for each of the \(N\) values of `I`, so \(N \times N\) times [B1].

Q: [3 marks] ★ Explain why a binary search cannot be used to find a name in an array of names that is in no particular order.
H: Think about what the comparison with the middle element tells you.
A: A binary search compares the target with the middle element to decide which half to discard [B1]. This only works if the elements are in order, so that everything on one side of the middle is smaller and everything on the other is larger [B1]. In an unsorted array the target could be in either half, so discarding a half could throw away the target and the search would give the wrong result [B1].

Q: [6 marks] ★★ The sorted array `Insert` has bounds 1 to 9 and holds 4, 9, 15, 22, 28, 33, 41, 47 and 52. Complete a trace table, with columns Target, Low, High, Mid and `Insert[Mid]`, for a call of `BinarySearch(22)` using the algorithm in this chapter with `High` starting at 9, and state the value returned. Then state the value returned for `BinarySearch(30)`.
H: Write `Low` and `High` before calculating `Mid` on each row.
H: For the second search, stop when `Low > High`.
A: One row for each trip round the loop. For 22:

| Target | Low | High | Mid | Insert[Mid] |
|---|---|---|---|---|
| 22 | 1 | 9 | 5 | 28 |
| | 1 | 4 | 2 | 9 |
| | 3 | 4 | 3 | 15 |
| | 4 | 4 | 4 | 22 |

- first row: Low 1, High 9, Mid 5, with `Insert[5]` = 28 [B1]
- 28 > 22 so High becomes 4, giving Low 1, High 4, Mid 2 (9) [B1]
- 9 < 22 so Low becomes 3, giving Mid 3 (15) [B1]
- 15 < 22 so Low becomes 4, giving Low 4, High 4, Mid 4 (22) [B1]
- the call for 22 returns 4 [B1]
- the call for 30 returns −1 [B1]

For 30: Mid 5 (28) gives Low 6; then Low 6, High 9, Mid 7 (41) gives High 6; then Low 6, High 6, Mid 6 (33) gives High 5; now Low > High, so the function returns −1.

Q: [7 marks] ★★ The array `Cities` has bounds 1 to 50 and holds the names of 50 cities in ascending alphabetical order. Write a function `FindCity(Name)` that uses a binary search to return the position of `Name` in `Cities`, or −1 if it is not there.
H: Strings can be compared with `<` and `=` just as numbers can.
H: Return from inside the loop when you find the name.
A: One possible answer:

```pseudocode
FUNCTION FindCity(Name : STRING) RETURNS INTEGER
   DECLARE Low, High, Mid : INTEGER
   Low ← 1
   High ← 50
   WHILE Low <= High
      Mid ← (Low + High) DIV 2
      IF Cities[Mid] = Name THEN
         RETURN Mid
      ENDIF
      IF Cities[Mid] < Name THEN
         Low ← Mid + 1
      ELSE
         High ← Mid - 1
      ENDIF
   ENDWHILE
   RETURN -1
ENDFUNCTION
```

- function header with a STRING parameter and RETURNS INTEGER [B1]
- `Low` set to 1 and `High` set to 50 [B1]
- loop that continues while `Low <= High` [B1]
- `Mid ← (Low + High) DIV 2` [B1]
- compares `Cities[Mid]` with `Name` and returns `Mid` when they are equal [B1]
- `Low ← Mid + 1` when `Cities[Mid] < Name` and `High ← Mid - 1` otherwise [B1]
- `RETURN -1` after the loop [B1]

(Accept a flag variable and a single RETURN at the end instead of RETURN inside the loop.)

Q: [6 marks] ★★ The array `Scores` has bounds 1 to 30 and holds 30 integers in no particular order. Write pseudocode for an insertion sort that puts `Scores` into **descending** order (largest first).
H: In descending order, a value is shifted right when it is **smaller** than the item being inserted.
H: Declare a variable to hold the item, so that it is not overwritten.
A: One possible answer:

```pseudocode
DECLARE Index, Position, Item : INTEGER

FOR Index ← 2 TO 30
   Item ← Scores[Index]
   Position ← Index - 1
   WHILE Position >= 1 AND Scores[Position] < Item
      Scores[Position + 1] ← Scores[Position]
      Position ← Position - 1
   ENDWHILE
   Scores[Position + 1] ← Item
NEXT Index
```

- outer loop from 2 to 30 [B1]
- the item being inserted stored in a variable (`Item`) [B1]
- `Position` starts at `Index - 1` [B1]
- inner loop continues while `Position >= 1` **and** `Scores[Position] < Item` (the correct direction for descending order) [B1]
- inside the loop, copies `Scores[Position]` to `Scores[Position + 1]` and decreases `Position` [B1]
- after the loop, `Scores[Position + 1] ← Item` [B1]

Q: [6 marks] ★★ The array `Data` has bounds 1 to 4 and holds 9, 4, 7, 2. The pseudocode below is an insertion sort. Complete a trace table with columns Index, Item, Position, `Data[1]`, `Data[2]`, `Data[3]` and `Data[4]`.

```pseudocode
FOR Index ← 2 TO 4
   Item ← Data[Index]
   Position ← Index - 1
   WHILE Position >= 1 AND Data[Position] > Item
      Data[Position + 1] ← Data[Position]
      Position ← Position - 1
   ENDWHILE
   Data[Position + 1] ← Item
NEXT Index
```

H: Write one row each time a value changes, and put the starting values of the array in the first row.
H: On the last pass the 2 has to move past all three other values.
A: One row per change; a blank cell means "unchanged".

| Index | Item | Position | Data[1] | Data[2] | Data[3] | Data[4] |
|---|---|---|---|---|---|---|
| 2 | 4 | 1 | 9 | 4 | 7 | 2 |
| | | 0 | | 9 | | |
| | | | 4 | | | |
| 3 | 7 | 2 | | | | |
| | | 1 | | | 9 | |
| | | | | 7 | | |
| 4 | 2 | 3 | | | | |
| | | 2 | | | | 9 |
| | | 1 | | | 7 | |
| | | 0 | | 4 | | |
| | | | 2 | | | |

- initial values: the array 9, 4, 7, 2 and `Index` 2, `Item` 4, `Position` 1 [B1]
- pass 1: 9 shifts into `Data[2]`, `Position` becomes 0, 4 is inserted in `Data[1]` [B1]
- pass 2: `Item` 7, 9 shifts into `Data[3]`, then 7 is inserted in `Data[2]` [B1]
- pass 3 starts with `Item` 2 and `Position` 3 [B1]
- pass 3 shifts 9, 7 and 4 one place right, with `Position` falling 3, 2, 1, 0 [B1]
- 2 inserted in `Data[1]`, leaving 2, 4, 7, 9 [B1]

(Rows may be split differently, as long as the values in each column appear in the correct order.)

Q: [8 marks] ★★★ A library stores the codes of its 20 000 books in a sorted array. (a) State the greatest number of comparisons a linear search needs to show that a code is not in the array. [1] (b) State the greatest number of comparisons a binary search needs on this array, and show how you worked it out. [2] (c) State two conditions that must hold before the library can use binary search. [2] (d) The library also keeps a separate array of 30 codes of books returned today, in the order they arrived. A member of staff suggests sorting these 30 codes first and then using binary search to look up one code. Justify why a linear search is better here. [3]
H: For (b), find the smallest power of 2 above 20 000.
H: For (d), compare the cost of sorting with the cost of one linear search.
A: (a) 20 000 comparisons [B1], because every element is checked.

(b) \(2^{14} = 16\,384\) is less than 20 000 and \(2^{15} = 32\,768\) is more [B1], so the worst case is \(14 + 1 = 15\) comparisons [B1].

(c) The data must be sorted [B1] and held in a structure with direct access by position, such as an array [B1].

(d) The 30 codes are not in order, so a binary search could not be used until they had been sorted [B1]. Sorting 30 items takes far more comparisons (up to \(\tfrac{30 \times 29}{2} = 435\) for insertion sort) than a single linear search of at most 30 [B1]. For one look-up in so small a list, sorting first costs much more than it saves, so a linear search is better [B1].

Q: [9 marks] ★★★ A bus company keeps its ticket prices (in whole dollars) in a sorted Python list `prices` holding 5, 9, 14, 18, 23, 27, 31, 36, 40 and 45. Write program code in Python for a function `binary_search(prices, target)` that returns the index of `target` (counting from 0), or −1 if it is not in the list. Use the function to search for 27, 10, 45 and 5, printing the result for each, and show the output.
H: A Python list counts from 0, so `low` starts at 0 and `high` at `len(prices) - 1`.
H: Use `//` for integer division.
A: One possible answer:

```python
prices = [5, 9, 14, 18, 23, 27, 31, 36, 40, 45]


def binary_search(prices, target):
    low = 0
    high = len(prices) - 1
    while low <= high:
        mid = (low + high) // 2
        if prices[mid] == target:
            return mid
        if prices[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


for target in [27, 10, 45, 5]:
    index = binary_search(prices, target)
    if index == -1:
        print(target, "not found")
    else:
        print(target, "found at index", index)
```

Output:

```output
27 found at index 5
10 not found
45 found at index 9
5 found at index 0
```

- function header with a list parameter and a target parameter [B1]
- `low` set to 0 and `high` set to `len(prices) - 1` [B1]
- a loop that continues while `low <= high` [B1]
- `mid` calculated with integer division [B1]
- returns `mid` when `prices[mid]` equals the target [B1]
- `low = mid + 1` or `high = mid - 1`, the correct way round [B1]
- returns −1 after the loop [B1]
- calls the function for 27, 10, 45 and 5 and prints each result [B1]
- correct output for all four values [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A sorted list may hold the same value more than once. A plain binary search for 4 in `[2, 4, 4, 4, 7, 9, 9, 12, 15, 15, 15, 20]` may return any of the three positions that hold a 4. Write a Python function `first_position(sorted_list, target)` that returns the index of the **first** occurrence (counting from 0), or −1, and show that it returns 1 for the target 4 where the ordinary function returns 2.
H: When you find the target, do not stop: remember the index and keep searching the left half.
H: To search the left half, set `high` to `mid - 1`.
A: When `sorted_list[mid]` equals the target, record `mid` as a possible answer but carry on searching to the left, because an earlier occurrence may exist.

```python
numbers = [2, 4, 4, 4, 7, 9, 9, 12, 15, 15, 15, 20]


def plain_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        if sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def first_position(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    answer = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            answer = mid
            high = mid - 1
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return answer


print(plain_search(numbers, 4), first_position(numbers, 4), first_position(numbers, 15), first_position(numbers, 5))
```

Output:

```output
2 1 8 -1
```

- an extra variable that stores the best index found so far, starting at −1 [B1]
- when the target is found, stores `mid` [B1]
- sets `high` to `mid - 1` so that the search continues in the left half [B1]
- the other branches move `low` or `high` as in an ordinary binary search [B1]
- returns the stored index after the loop ends [B1]
- output shows 1 for the first function against 2 for the plain search [B1]

Q: [5 marks] ★★★ A shop owner has 1000 unsorted product codes and will look up codes one at a time. Sorting the array once with an insertion sort costs at most \(\tfrac{1000 \times 999}{2} = 499\,500\) comparisons. After that each look-up by binary search costs at most 10 comparisons, while each look-up by linear search without sorting costs at most 1000. Using these worst-case figures, what is the smallest number of look-ups \(k\) for which sorting first and then using binary search needs fewer comparisons than using linear search every time? Show your working.
H: Write the total cost of each plan in terms of \(k\): \(499\,500 + 10k\) and \(1000k\).
H: Solve \(499\,500 + 10k < 1000k\) for a whole number \(k\).
A: Plan A (sort, then binary search) costs \(499\,500 + 10k\) comparisons [B1]. Plan B (linear search every time) costs \(1000k\) comparisons [B1]. Plan A is cheaper when \(499\,500 + 10k < 1000k\) [B1]. That gives \(499\,500 < 990k\), so \(k > 504.5\ldots\) [B1]. The smallest whole number is \(k = 505\) [B1]. The shop would have to expect more than about 500 look-ups before sorting pays off.
:::

:::quiz
? Which condition must be true before a binary search is used?
- The array must contain no repeated values.
- The array must have an even number of elements.
+ The array must be sorted.
- The target must be in the array.
> Each comparison with the middle element throws away half of the array, which is only correct if the elements are in order. Repeated values, an odd length and an absent target do not stop a binary search working.
? What is the greatest number of comparisons a binary search needs for 1000 sorted items?
- 9
+ 10
- 500
- 1000
> \(2^9 = 512 < 1000 < 1024 = 2^{10}\), so \(\lfloor \log_2 1000 \rfloor = 9\) and the worst case is \(9 + 1 = 10\). Answering 9 forgets the last comparison; 500 and 1000 are linear search figures.
? What is `Mid` when `Low` is 6 and `High` is 11, using `Mid ← (Low + High) DIV 2`?
- 5
+ 8
- 9
- 17
> \(6 + 11 = 17\) and \(17 \text{ DIV } 2 = 8\). The answer 9 rounds 8.5 up; DIV always rounds down.
? A binary search sets `Low ← Mid` instead of `Low ← Mid + 1`. What can go wrong?
- It returns the wrong position every time.
- It runs out of memory.
+ The loop may never end, because `Low` can stay the same.
- It only works on sorted data.
> If `Low` is 10, `High` is 11 and the target is larger than `Values[10]`, then `Mid` is 10, `Low` is set to 10 again and the range never shrinks.
? An insertion sort is run on an array that is already in ascending order of \(n\) items. How many comparisons does it make?
- \(n^2\)
- \(\tfrac{n(n-1)}{2}\)
- 0
+ \(n - 1\)
> Each element after the first is compared once with the element on its left, found to be in place, and not moved. That is \(n - 1\) comparisons and 0 shifts: the best case, \(O(n)\).
? What is the Big O of two nested loops, each running from 1 to \(n\), with a single assignment inside?
- \(O(n)\)
- \(O(2n)\)
+ \(O(n^2)\)
- \(O(\log n)\)
> The assignment runs \(n \times n\) times. \(O(2n)\) is not written, because constants are dropped; and it would describe two loops one after the other, not inside one another.
? The step count of an algorithm is \(3n^2 + 5n + 2\). What is its Big O?
- \(O(3n^2 + 5n + 2)\)
- \(O(n)\)
+ \(O(n^2)\)
- \(O(3n^2)\)
> Keep the fastest-growing term (\(3n^2\)) and then drop its constant multiplier. The smaller terms \(5n\) and 2 are dropped too.
? What does it mean to say that an algorithm sorts "in place"?
- It sorts without making any comparisons.
- It uses a stack to remember where it is.
+ It rearranges the data in the array it was given, using only a few extra variables.
- It makes a sorted copy and keeps the original.
> In-place sorts such as bubble sort and insertion sort need only variables like `Temp`, `Item` and `Position`, so their extra space is \(O(1)\).
? A student says "\(O(\log n)\) means the logarithm is to base 10". What is wrong with this?
- Nothing: it is always base 10.
- It is always base \(e\).
+ The base does not matter, because changing it only multiplies by a constant, and Big O ignores constants.
- Logarithms are not used in Big O.
> \(\log_{10} n\) and \(\log_2 n\) differ by a constant factor, so both are written \(O(\log n)\).
:::

:::checklist What you can now do
- [ ] I can write a linear search and a binary search in pseudocode and Python, and trace them.
- [ ] I can state the conditions for a binary search: sorted data with direct access by position.
- [ ] I can explain how the number of comparisons in a binary search changes with the number of items (one more when the data doubles).
- [ ] I can write an insertion sort in pseudocode and Python and complete a trace table for it.
- [ ] I can write the efficient bubble sort and compare it with insertion sort.
- [ ] I can explain how the performance of each sort depends on the initial order of the data and the number of items.
- [ ] I can use Big O notation (\(O(1)\), \(O(\log n)\), \(O(n)\), \(O(n \log n)\), \(O(n^2)\), \(O(2^n)\)) for the time complexity of an algorithm.
- [ ] I can compare algorithms by time and by memory, and say what an in-place algorithm is.
- [ ] I can give the best case and the worst case of a search or a sort.
- [ ] I can write binary search and insertion sort as working Python programs and test them.
:::

:::recap
- Linear search: \(O(n)\), any data. Binary search: needs **sorted** data with direct access; each pass halves the range; worst case \(\lfloor \log_2 n \rfloor + 1\) comparisons (10 for 1000 items); doubling \(n\) adds one.
- Binary search: `Mid ← (Low + High) DIV 2`; compare; `Low ← Mid + 1` or `High ← Mid - 1`; stop when found or `Low > High`.
- Insertion sort builds a sorted part: take `Item`, shift larger elements right, insert in the gap. Best case sorted (\(n - 1\) comparisons), worst case reversed (\(\tfrac{n(n-1)}{2}\)).
- Efficient bubble sort (boundary and flag) is also \(O(n)\) on sorted data and \(O(n^2)\) in the worst case. The basic bubble sort is always \(O(n^2)\). Swaps in bubble sort and shifts in insertion sort are equal.
- Big O keeps the fastest-growing term and drops constants; it describes the growth of time (time complexity) or memory (space complexity), usually for the worst case.
- Classes in order of growth: \(O(1)\), \(O(\log n)\), \(O(n)\), \(O(n \log n)\), \(O(n^2)\), \(O(2^n)\). Loops in sequence add; nested loops multiply; halving gives \(\log n\).
- Bubble sort and insertion sort are in-place, with \(O(1)\) extra space. A recursive binary search uses \(O(\log n)\) stack space.
:::

:::links
- practise: [Algorithms: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/19-computational-thinking-and-problem-solving-/algorithms/exam-questions/) · Save My Exams · 9618-style questions on searching, sorting and Big O with mark schemes [paid]
- explore: [Sorting animations](https://visualgo.net/en/sorting) · VisuAlgo · watch bubble and insertion sort run, then try the faster sorts
- read: [Binary search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search) · Khan Academy · binary search explained step by step
- read: [Insertion sort](https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/) · GeeksforGeeks · insertion sort in several languages
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on algorithms by university computer scientists

Links checked 13 November 2026.
:::

Next: [Abstract data types: stacks, queues, lists, trees and graphs](#cs.adts)
