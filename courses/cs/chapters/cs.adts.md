@chapter cs.adts
@title Abstract data types: stacks, queues, lists, trees and graphs
@level a2
@paper CAIE 9618 Papers 3 and 4
@time 7–9 hours
@summary You will write the operations of the stack, queue, linked list and binary search tree in pseudocode and Python, add the dictionary and the graph, and learn how one abstract data type can be built from another, such as a queue from two stacks.
:::why
Almost every large program stores its data in a stack, a queue, a list, a tree, a dictionary or a graph, and a programmer chooses between them by the operations the job needs, not by how they are stored. Paper 3 asks you to write the operations in pseudocode, to follow pointers in arrays, and to justify a choice of structure. Paper 4 asks you to write them as working code and test them.
:::

**Before you start**, you should know stacks, queues and linked lists stored in arrays from [Text files, stacks, queues and linked lists](#cs.structures), records and arrays from [Data types, records and arrays](#cs.datatypes), and the Big O ideas from [Searching, sorting and Big O](#cs.algorithms2).

:::try Warm-up
Q: A stack holds 12, 7 and 5, with 5 on top. What does a pop return, and what does the stack hold afterwards? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: A pop returns 5, the most recently added item (last in, first out). The stack then holds 12 and 7.
Q: In a linked list stored in arrays, what does the pointer value 0 mean, and what does `StartPointer = 0` tell you? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: 0 is the null pointer: it points to no node, so the node holding it is the last in the list. `StartPointer = 0` means the list is empty.
Q: `Library` is `ARRAY[1:500] OF Book`. What does `Library[3].Title` mean? (from [Data types, records and arrays](#cs.datatypes))
A: The Title field of the third record in the array.
:::

:::note How code appears in this chapter
Pseudocode follows the Cambridge Pseudocode Guide. As in the AS chapter, arrays start at 1, the null pointer is 0, the list nodes are in arrays `Data` and `Pointer`, and the variables are `StartPointer` and `FreePointer`. In Python, a pointer array has an unused element 0, so that the pointer 0 means "nothing" and the list index equals the node number. Paper 4 allows a class to be used as a record and a list as an array. Every Python program in this chapter has been run and its output block is exactly what it prints.
:::

## Abstract data types

:::def Abstract data type (ADT)
A collection of data together with the operations that can be performed on it, described without saying how the data is stored. The user of an ADT needs to know only what the operations do.
:::

A stack is an ADT. Its description says: items go on the top, items come off the top, and you can look at the top item. It does not say whether the items live in an array, a linked list or a library. That is what "abstract" means. The same ADT can have several **implementations**, and you can swap one for another without changing the programs that use the ADT.

| ADT | Order of items | Main operations |
|---|---|---|
| Stack | last in, first out | push, pop, peek, is empty, is full |
| Queue | first in, first out | enqueue, dequeue, is empty, is full |
| Linked list | order given by pointers | find, insert, delete, traverse (output in order) |
| Binary tree | each node has up to two children | insert, find, traverse |
| Dictionary | unordered pairs of key and value | add, look up by key, delete |
| Graph | a set of vertices joined by edges | add a vertex, add an edge, find the neighbours |

This chapter writes the operations for each one, and finishes by building one ADT out of another. The sections on stacks, queues and linked lists extend the AS chapter: there you followed the algorithms; here you must be able to **write** them, in pseudocode and in Python.

## Stacks

A stack is last in, first out (LIFO). The implementation here is an array and a **top pointer**, the index of the top item (0 when the stack is empty). Pushing onto a full stack is **overflow**; popping from an empty one is **underflow**. Both must be checked.

```pseudocode
DECLARE Stack : ARRAY[1:5] OF INTEGER
DECLARE TopPointer : INTEGER

TopPointer ← 0

FUNCTION IsEmpty() RETURNS BOOLEAN
   RETURN TopPointer = 0
ENDFUNCTION

FUNCTION Push(NewItem : INTEGER) RETURNS BOOLEAN
   IF TopPointer = 5 THEN
      RETURN FALSE
   ENDIF
   TopPointer ← TopPointer + 1
   Stack[TopPointer] ← NewItem
   RETURN TRUE
ENDFUNCTION

FUNCTION Pop() RETURNS INTEGER
   DECLARE Item : INTEGER
   IF TopPointer = 0 THEN
      RETURN -1
   ENDIF
   Item ← Stack[TopPointer]
   TopPointer ← TopPointer - 1
   RETURN Item
ENDFUNCTION
```

`Push` returns FALSE on overflow, so the caller knows the item was not stored. `Pop` returns −1 on underflow, which is safe only if −1 is never a stored value; a program that stores any integer should call `IsEmpty()` before it pops. Popping does not clear the array element: `Stack[TopPointer]` still holds the old value, but it is above the top pointer, so the stack no longer contains it.

**Reading a class.** A **class** groups data and the functions that work on that data into one unit. A function written inside a class is called a **method**. `def __init__(self, size):` is the special method that runs when a new object is made: it sets up the starting values. `self` is the object that is being used: `self.top_pointer` means "the `top_pointer` belonging to this stack", so two stacks keep their own pointers. `stack = Stack(5)` makes a new stack that can hold 5 items, and `stack.push(7)` calls the `push` method on that stack, with 7 as `new_item` (Python supplies `self` itself). The same pattern is used for `CircularQueue`, `LinkedList` and the other classes in this chapter. You do not need more than this to follow them; [Object-oriented programming](#cs.oop) explains classes and objects fully.

Paper 4 tasks usually ask for a class. This `Stack` class holds a list with an unused element 0, and the same fields and logic as the pseudocode. The program tests it: five pushes fit, a sixth fails, three pops, then it empties the stack.

```python
class Stack:
    def __init__(self, size):
        self.items = [None] * (size + 1)
        self.size = size
        self.top_pointer = 0

    def is_empty(self):
        return self.top_pointer == 0

    def is_full(self):
        return self.top_pointer == self.size

    def push(self, new_item):
        if self.is_full():
            return False
        self.top_pointer = self.top_pointer + 1
        self.items[self.top_pointer] = new_item
        return True

    def pop(self):
        if self.is_empty():
            return None
        item = self.items[self.top_pointer]
        self.top_pointer = self.top_pointer - 1
        return item


stack = Stack(5)
for value in [12, 7, 30, 45, 8, 19]:
    if stack.push(value):
        print("Pushed", value)
    else:
        print("Stack full, could not push", value)
for count in range(3):
    print("Popped", stack.pop())
print("Top pointer:", stack.top_pointer, "Items:", stack.items[1:stack.top_pointer + 1])
stack.push(22)
while not stack.is_empty():
    print("Popped", stack.pop())
print("Pop on an empty stack gives", stack.pop())
```

Output:

```output
Pushed 12
Pushed 7
Pushed 30
Pushed 45
Pushed 8
Stack full, could not push 19
Popped 8
Popped 45
Popped 30
Top pointer: 2 Items: [12, 7]
Popped 22
Popped 7
Popped 12
Pop on an empty stack gives None
```

In Python the underflow signal is `None`, which cannot be mistaken for a stored integer. Python lists also have `append` and `pop`, which already behave as a stack with no size limit; use your own class when a question asks you to write Push and Pop.

## Queues

A queue is first in, first out (FIFO). Items join at the rear and leave from the front. An array needs a **front pointer** and a **rear pointer**.

In a **linear queue**, the rear pointer only moves right. The queue is empty when the front pointer has gone past the rear pointer, and it is "full" when the rear pointer reaches the end of the array, even if places at the front have been freed by dequeues.

```pseudocode
DECLARE Queue : ARRAY[1:5] OF STRING
DECLARE FrontPointer, RearPointer : INTEGER

FrontPointer ← 1
RearPointer ← 0

FUNCTION Enqueue(NewItem : STRING) RETURNS BOOLEAN
   IF RearPointer = 5 THEN
      RETURN FALSE
   ENDIF
   RearPointer ← RearPointer + 1
   Queue[RearPointer] ← NewItem
   RETURN TRUE
ENDFUNCTION

FUNCTION Dequeue() RETURNS STRING
   DECLARE Item : STRING
   IF FrontPointer > RearPointer THEN
      RETURN ""
   ENDIF
   Item ← Queue[FrontPointer]
   FrontPointer ← FrontPointer + 1
   RETURN Item
ENDFUNCTION
```

The wasted places make a linear queue a poor choice. A **circular queue** wraps the pointers round with MOD, so freed places are reused, and a **count** of the items tells "full" (count = size) from "empty" (count = 0). For a queue of `Size` places, the position after `p` is `(p MOD Size) + 1`.

```pseudocode
DECLARE Queue : ARRAY[1:4] OF STRING
DECLARE FrontPointer, RearPointer, Count : INTEGER

FrontPointer ← 1
RearPointer ← 0
Count ← 0

FUNCTION Enqueue(NewItem : STRING) RETURNS BOOLEAN
   IF Count = 4 THEN
      RETURN FALSE
   ENDIF
   RearPointer ← (RearPointer MOD 4) + 1
   Queue[RearPointer] ← NewItem
   Count ← Count + 1
   RETURN TRUE
ENDFUNCTION

FUNCTION Dequeue() RETURNS STRING
   DECLARE Item : STRING
   IF Count = 0 THEN
      RETURN ""
   ENDIF
   Item ← Queue[FrontPointer]
   FrontPointer ← (FrontPointer MOD 4) + 1
   Count ← Count - 1
   RETURN Item
ENDFUNCTION
```

The Python class below mirrors it. The test fills a queue of 4 places, removes two items, then adds two more, which land in the places at the front of the array.

```python
class CircularQueue:
    def __init__(self, size):
        self.items = [None] * (size + 1)
        self.size = size
        self.front = 1
        self.rear = 0
        self.count = 0

    def enqueue(self, new_item):
        if self.count == self.size:
            return False
        self.rear = self.rear % self.size + 1
        self.items[self.rear] = new_item
        self.count = self.count + 1
        return True

    def dequeue(self):
        if self.count == 0:
            return None
        item = self.items[self.front]
        self.front = self.front % self.size + 1
        self.count = self.count - 1
        return item


queue = CircularQueue(4)
for letter in ["A", "B", "C", "D", "E"]:
    if not queue.enqueue(letter):
        print("Queue full, could not add", letter)
print(queue.items[1:], "front", queue.front, "rear", queue.rear, "count", queue.count)
print("Removed", queue.dequeue(), "and", queue.dequeue())
queue.enqueue("E")
queue.enqueue("F")
print(queue.items[1:], "front", queue.front, "rear", queue.rear, "count", queue.count)
```

Output:

```output
Queue full, could not add E
['A', 'B', 'C', 'D'] front 1 rear 4 count 4
Removed A and B
['E', 'F', 'C', 'D'] front 3 rear 2 count 4
```

The queue now holds C, D, E, F, in that order, from place 3 round to place 2. The rear pointer wrapped from 4 to 1 because \(4 \bmod 4 + 1 = 1\).

You can step through a queue and a linked list in this widget, from the AS chapter.

:::html
<div class="widget" data-w="cs-stack" data-type="circular" data-size="4" data-items="A,B,C,D"></div>
:::

## Linked lists

A linked list keeps its order in pointers, so an insertion or a deletion changes pointers and moves no data. The nodes are in two arrays, `Data` and `Pointer`, with `StartPointer` for the first node and `FreePointer` for the first unused node. **Unused nodes are chained together into a free list.** Every node is in exactly one of the two lists, and keeping the free list correct is where most marks are lost.

Setting up an empty list of 6 nodes chains node 1 to node 2, node 2 to node 3 and so on, with the last holding the null pointer 0:

```pseudocode
DECLARE Data : ARRAY[1:6] OF INTEGER
DECLARE Pointer : ARRAY[1:6] OF INTEGER
DECLARE StartPointer, FreePointer : INTEGER

PROCEDURE InitialiseList()
   DECLARE Index : INTEGER
   StartPointer ← 0
   FreePointer ← 1
   FOR Index ← 1 TO 5
      Pointer[Index] ← Index + 1
   NEXT Index
   Pointer[6] ← 0
ENDPROCEDURE
```

**Find.** Start at the first node and follow the pointers until the data matches or the pointer is 0. The function returns the node number, or 0 if the item is not in the list.

```pseudocode
FUNCTION FindItem(Target : INTEGER) RETURNS INTEGER
   DECLARE Current : INTEGER
   Current ← StartPointer
   WHILE Current <> 0 AND Data[Current] <> Target
      Current ← Pointer[Current]
   ENDWHILE
   RETURN Current
ENDFUNCTION
```

**Insert in order.** Take a node from the free list, store the item, walk to the first node whose data is not smaller, and splice the new node in. The new node must point to the **rest of the list first**, then the previous node points to the new node.

```pseudocode
FUNCTION InsertItem(NewItem : INTEGER) RETURNS BOOLEAN
   DECLARE NewNode, Previous, Current : INTEGER
   IF FreePointer = 0 THEN
      RETURN FALSE
   ENDIF
   NewNode ← FreePointer
   FreePointer ← Pointer[NewNode]
   Data[NewNode] ← NewItem
   Previous ← 0
   Current ← StartPointer
   WHILE Current <> 0 AND Data[Current] < NewItem
      Previous ← Current
      Current ← Pointer[Current]
   ENDWHILE
   Pointer[NewNode] ← Current
   IF Previous = 0 THEN
      StartPointer ← NewNode
   ELSE
      Pointer[Previous] ← NewNode
   ENDIF
   RETURN TRUE
ENDFUNCTION
```

**Delete.** Find the node and its previous node, make the previous node skip it (or move `StartPointer` on), then **return the node to the free list**.

```pseudocode
FUNCTION DeleteItem(OldItem : INTEGER) RETURNS BOOLEAN
   DECLARE Previous, Current : INTEGER
   Previous ← 0
   Current ← StartPointer
   WHILE Current <> 0 AND Data[Current] <> OldItem
      Previous ← Current
      Current ← Pointer[Current]
   ENDWHILE
   IF Current = 0 THEN
      RETURN FALSE
   ENDIF
   IF Previous = 0 THEN
      StartPointer ← Pointer[Current]
   ELSE
      Pointer[Previous] ← Pointer[Current]
   ENDIF
   Pointer[Current] ← FreePointer
   FreePointer ← Current
   RETURN TRUE
ENDFUNCTION
```

**Output in order.** Follow the pointers from the start:

```pseudocode
PROCEDURE OutputList()
   DECLARE Current : INTEGER
   Current ← StartPointer
   WHILE Current <> 0
      OUTPUT Data[Current]
      Current ← Pointer[Current]
   ENDWHILE
ENDPROCEDURE
```

:::warn Where the marks go wrong
- **The free list.** Taking a node must move `FreePointer` on (`FreePointer ← Pointer[NewNode]`) and deleting a node must put it back at the front of the free list. Forget either and nodes are lost or used twice.
- **The first node.** Inserting before the first node or deleting the first node changes `StartPointer`, not a `Pointer` element. Test for `Previous = 0`.
- **The empty list and the end of the list.** `Current <> 0` must be tested before `Data[Current]` is read, because there is no node 0.
- **`StartPointer` and `FreePointer` are different things** (a tree has `RootPointer`): do not mix them up.
:::

The Python class has the same logic. The test inserts five numbers into a list of 6 nodes, deletes two, finds two values and inserts one more, printing the arrays each time.

```python
class LinkedList:
    def __init__(self, size):
        self.size = size
        self.data = [None] * (size + 1)
        self.pointer = [0] * (size + 1)
        self.start_pointer = 0
        self.free_pointer = 1
        for index in range(1, size):
            self.pointer[index] = index + 1
        self.pointer[size] = 0

    def find(self, target):
        current = self.start_pointer
        while current != 0 and self.data[current] != target:
            current = self.pointer[current]
        return current

    def insert(self, new_item):
        if self.free_pointer == 0:
            return False
        new_node = self.free_pointer
        self.free_pointer = self.pointer[new_node]
        self.data[new_node] = new_item
        previous = 0
        current = self.start_pointer
        while current != 0 and self.data[current] < new_item:
            previous = current
            current = self.pointer[current]
        self.pointer[new_node] = current
        if previous == 0:
            self.start_pointer = new_node
        else:
            self.pointer[previous] = new_node
        return True

    def delete(self, old_item):
        previous = 0
        current = self.start_pointer
        while current != 0 and self.data[current] != old_item:
            previous = current
            current = self.pointer[current]
        if current == 0:
            return False
        if previous == 0:
            self.start_pointer = self.pointer[current]
        else:
            self.pointer[previous] = self.pointer[current]
        self.pointer[current] = self.free_pointer
        self.free_pointer = current
        return True

    def output(self):
        items = []
        current = self.start_pointer
        while current != 0:
            items.append(self.data[current])
            current = self.pointer[current]
        return items


def show(linked):
    print("Data:", linked.data[1:])
    print("Pointer:", linked.pointer[1:])
    print("Start", linked.start_pointer, "Free", linked.free_pointer, "List:", linked.output())


numbers = LinkedList(6)
for item in [40, 15, 62, 28, 51]:
    numbers.insert(item)
show(numbers)
numbers.delete(15)
numbers.delete(62)
show(numbers)
print("Find 28:", numbers.find(28), "Find 99:", numbers.find(99))
numbers.insert(33)
show(numbers)
```

Output:

```output
Data: [40, 15, 62, 28, 51, None]
Pointer: [5, 4, 0, 1, 3, 0]
Start 2 Free 6 List: [15, 28, 40, 51, 62]
Data: [40, 15, 62, 28, 51, None]
Pointer: [5, 6, 2, 1, 0, 0]
Start 4 Free 3 List: [28, 40, 51]
Find 28: 4 Find 99: 0
Data: [40, 15, 33, 28, 51, None]
Pointer: [5, 6, 1, 3, 0, 0]
Start 4 Free 2 List: [28, 33, 40, 51]
```

:::eg Reading the arrays of a linked list
Use the first and second parts of the output above. (a) Write out the list from the arrays after the five insertions. (b) Explain every change to the `Pointer` array when 15 and then 62 are deleted. (c) Which node does `InsertItem(33)` use, and why?

(a) `StartPointer` is 2, so the first node is 2 (`Data[2]` = 15). `Pointer[2]` is 4, so next is node 4 (28). `Pointer[4]` is 1 (40), `Pointer[1]` is 5 (51), and `Pointer[5]` is 3 (62), whose pointer is 0. The list is 15, 28, 40, 51, 62. [B1]

(b) Deleting 15: it is the first node, so `StartPointer` takes `Pointer[2]`, which is 4. Node 2 joins the front of the free list: `Pointer[2]` becomes the old `FreePointer`, 6, and `FreePointer` becomes 2. Deleting 62 (node 3): the previous node is 5, so `Pointer[5]` takes `Pointer[3]`, which is 0. Node 3 joins the free list: `Pointer[3]` becomes 2 and `FreePointer` becomes 3. [B1] The free list is now 3, 2, 6. [B1] The data is untouched, so `Data[2]` and `Data[3]` still hold 15 and 62, but no pointer reaches them from the list. [B1]

(c) The free list is 3, 2, 6, so the new item goes into node 3, overwriting the old 62. [B1] That is why `Pointer` shows `FreePointer` moving to 2 afterwards.
:::

### An object-oriented version

A linked list written with objects needs no arrays: each node is an object holding its data and a reference to the next node (`None` plays the part of the null pointer), and the list keeps the first node, `head`. This is the same ADT with a different implementation. Classes and objects are covered in [Object-oriented programming](#cs.oop); here only the shape matters.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:
    def __init__(self):
        self.head = None

    def insert(self, new_item):
        node = Node(new_item)
        if self.head is None or new_item < self.head.data:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_item:
                current = current.next
            node.next = current.next
            current.next = node

    def to_list(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items


names = OrderedList()
for name in ["Kofi", "Amina", "Zainab", "Chidi"]:
    names.insert(name)
print(names.to_list())
```

Output:

```output
['Amina', 'Chidi', 'Kofi', 'Zainab']
```

There is no free list because Python finds memory for each new node itself, so the program never meets "list full".

## Binary trees

A linked list has one pointer per node, so it can only go one way. A node with **two** pointers gives a **binary tree**.

:::def Binary tree
A hierarchical data structure in which each node holds data and has at most two child nodes, a left child and a right child. One node, the root, has no parent.
:::

:::def Binary search tree
A binary tree in which, for every node, all the values in its left subtree are smaller than the node's value and all the values in its right subtree are larger (or equal: this course puts equal values on the right).
:::

:::def Root, leaf and subtree
The **root** is the top node, from which every other node can be reached. A **leaf** is a node with no children. A **subtree** is a node together with all the nodes below it; every node is the root of its own subtree.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 214" role="img" aria-label="A binary search tree of seven nodes. The root holds 27. Its left child holds 14, with children 10 and 19. Its right child holds 35, with children 31 and 42. Every value in a left subtree is smaller than its parent and every value in a right subtree is larger. The root and one leaf, 10, are labelled."><line class="ln" x1="170" y1="34" x2="90" y2="100"/><line class="ln" x1="170" y1="34" x2="250" y2="100"/><line class="ln" x1="90" y1="100" x2="50" y2="166"/><line class="ln" x1="90" y1="100" x2="130" y2="166"/><line class="ln" x1="250" y1="100" x2="210" y2="166"/><line class="ln" x1="250" y1="100" x2="290" y2="166"/><circle class="f1 s-acc sw2" cx="170" cy="34" r="18"/><text class="tl tc" x="170" y="39">27</text><circle class="fm s-acc sw2" cx="90" cy="100" r="18"/><text class="tl tc" x="90" y="105">14</text><circle class="fm s-acc sw2" cx="250" cy="100" r="18"/><text class="tl tc" x="250" y="105">35</text><circle class="fm s-acc sw2" cx="50" cy="166" r="18"/><text class="tl tc" x="50" y="171">10</text><circle class="fm s-acc sw2" cx="130" cy="166" r="18"/><text class="tl tc" x="130" y="171">19</text><circle class="fm s-acc sw2" cx="210" cy="166" r="18"/><text class="tl tc" x="210" y="171">31</text><circle class="fm s-acc sw2" cx="290" cy="166" r="18"/><text class="tl tc" x="290" y="171">42</text><text class="tl" x="196" y="24">root</text><text class="tl tc" x="50" y="204">leaf</text></svg><figcaption>A binary search tree. The root is 27. The nodes 14, 10 and 19 form the left subtree of the root, and 35, 31 and 42 form its right subtree. Leaves (10, 19, 31, 42) have no children.</figcaption></figure>
:::

To search for a value, start at the root: if the target equals the node, stop; if it is smaller, go left; if it is larger, go right. Each step throws away a whole subtree, like binary search throws away half an array. A balanced tree of \(n\) nodes has about \(\log_2 n\) levels, so a search is \(O(\log n)\). But the shape depends on the order the values arrive, and a tree built from values already in order is just a linked list (see the stretch question).

### A tree stored in arrays

The nodes go in an array of records, each with a `LeftPointer`, a `Data` field and a `RightPointer`. A pointer is the array index of a child, and 0 means "no child". `RootPointer` holds the index of the root (0 if the tree is empty). Unused nodes are chained through their `LeftPointer` fields into a free list, with `FreePointer` at the front, just as in a linked list.

```pseudocode
TYPE TreeNode
   DECLARE LeftPointer : INTEGER
   DECLARE Data : INTEGER
   DECLARE RightPointer : INTEGER
ENDTYPE

DECLARE Tree : ARRAY[1:7] OF TreeNode
DECLARE RootPointer, FreePointer : INTEGER

PROCEDURE InitialiseTree()
   DECLARE Index : INTEGER
   RootPointer ← 0
   FreePointer ← 1
   FOR Index ← 1 TO 6
      Tree[Index].LeftPointer ← Index + 1
      Tree[Index].RightPointer ← 0
   NEXT Index
   Tree[7].LeftPointer ← 0
   Tree[7].RightPointer ← 0
ENDPROCEDURE
```

**Insert.** Take a node from the free list, store the item with both pointers 0, then walk down from the root (left if smaller, right otherwise) until you reach a null pointer. The last node visited is the parent, and the new node becomes its left or right child.

```pseudocode
PROCEDURE InsertNode(NewItem : INTEGER)
   DECLARE NewNode, Current, Parent : INTEGER
   DECLARE GoLeft : BOOLEAN
   IF FreePointer = 0 THEN
      OUTPUT "Tree full"
   ELSE
      NewNode ← FreePointer
      FreePointer ← Tree[NewNode].LeftPointer
      Tree[NewNode].Data ← NewItem
      Tree[NewNode].LeftPointer ← 0
      Tree[NewNode].RightPointer ← 0
      IF RootPointer = 0 THEN
         RootPointer ← NewNode
      ELSE
         Current ← RootPointer
         WHILE Current <> 0
            Parent ← Current
            IF NewItem < Tree[Current].Data THEN
               GoLeft ← TRUE
               Current ← Tree[Current].LeftPointer
            ELSE
               GoLeft ← FALSE
               Current ← Tree[Current].RightPointer
            ENDIF
         ENDWHILE
         IF GoLeft = TRUE THEN
            Tree[Parent].LeftPointer ← NewNode
         ELSE
            Tree[Parent].RightPointer ← NewNode
         ENDIF
      ENDIF
   ENDIF
ENDPROCEDURE
```

The order matters: the free node's `LeftPointer` is read (to move `FreePointer` on) **before** it is overwritten with 0.

**Find.** Follow the pointers without changing anything. The function returns the node number, or 0 when it reaches a null pointer.

```pseudocode
FUNCTION FindNode(Target : INTEGER) RETURNS INTEGER
   DECLARE Current : INTEGER
   Current ← RootPointer
   WHILE Current <> 0 AND Tree[Current].Data <> Target
      IF Target < Tree[Current].Data THEN
         Current ← Tree[Current].LeftPointer
      ELSE
         Current ← Tree[Current].RightPointer
      ENDIF
   ENDWHILE
   RETURN Current
ENDFUNCTION
```

:::eg Inserting 31 into a tree held in arrays
The tree holds 27, 14, 35 and 10, inserted in that order into the arrays of 7 nodes, so `RootPointer` is 1 and `FreePointer` is 5. Show the arrays after `InsertNode(31)`.

Node 5 is the free node, so `FreePointer` becomes `Tree[5].LeftPointer`, which is 6. The new node holds 31 with both pointers 0. Walk from the root: 31 > 27, so go right to node 3 (35); 31 < 35, so go left, and `Tree[3].LeftPointer` is 0, a null pointer. The parent is node 3 and the direction is left, so `Tree[3].LeftPointer ← 5`.

| Node | LeftPointer before | Data before | RightPointer before | LeftPointer after | Data after | RightPointer after |
|---|---|---|---|---|---|---|
| 1 | 2 | 27 | 3 | 2 | 27 | 3 |
| 2 | 4 | 14 | 0 | 4 | 14 | 0 |
| 3 | 0 | 35 | 0 | 5 | 35 | 0 |
| 4 | 0 | 10 | 0 | 0 | 10 | 0 |
| 5 | 6 | | 0 | 0 | 31 | 0 |
| 6 | 7 | | 0 | 7 | | 0 |
| 7 | 0 | | 0 | 0 | | 0 |

Three cells changed: `Tree[5]` was filled, `Tree[3].LeftPointer` became 5, and `FreePointer` moved from 5 to 6. [B1] [B1] [B1]
:::

### Traversing a tree

A **traversal** visits every node once. The three standard orders differ in when the node's own data is output, compared with the left and right subtrees.

:::def Traversal
Visiting every node of a tree exactly once, in a systematic order. In-order visits the left subtree, then the node, then the right subtree. Pre-order visits the node, then the left subtree, then the right subtree. Post-order visits the left subtree, then the right subtree, then the node.
:::

For a binary search tree, **in-order traversal outputs the values in ascending order**. Traversal is naturally recursive: the tree is a node with two smaller trees below it. A **recursive** procedure is one that calls itself; each call deals with a smaller tree, and a call with a null pointer does nothing, which stops the chain of calls. (Recursion has its own chapter, [Recursion](#cs.recursion), which explains this in full; here you only need to follow the calls.)

```pseudocode
PROCEDURE InOrder(Node : INTEGER)
   IF Node <> 0 THEN
      CALL InOrder(Tree[Node].LeftPointer)
      OUTPUT Tree[Node].Data
      CALL InOrder(Tree[Node].RightPointer)
   ENDIF
ENDPROCEDURE

CALL InOrder(RootPointer)
```

The call with a null pointer does nothing and returns, which stops the recursion. Moving the `OUTPUT` line gives the other orders: to the first line inside the IF for pre-order, and to the last for post-order.

The tree in the figure was built by inserting 27, 14, 35, 10, 31, 19, 42 in that order, so node numbers follow the order of insertion. Its arrays, and the three traversals, come from the Python program below, which is the same algorithm. It uses three lists with element 0 unused.

```python
size = 7
left = [0] * (size + 1)
data = [None] * (size + 1)
right = [0] * (size + 1)
root_pointer = 0
free_pointer = 1
for index in range(1, size):
    left[index] = index + 1


def insert_node(new_item):
    global root_pointer, free_pointer
    if free_pointer == 0:
        print("Tree full")
        return
    new_node = free_pointer
    free_pointer = left[new_node]
    data[new_node] = new_item
    left[new_node] = 0
    right[new_node] = 0
    if root_pointer == 0:
        root_pointer = new_node
    else:
        current = root_pointer
        while current != 0:
            parent = current
            if new_item < data[current]:
                go_left = True
                current = left[current]
            else:
                go_left = False
                current = right[current]
        if go_left:
            left[parent] = new_node
        else:
            right[parent] = new_node


def find_node(target):
    current = root_pointer
    while current != 0 and data[current] != target:
        if target < data[current]:
            current = left[current]
        else:
            current = right[current]
    return current


def in_order(node):
    if node == 0:
        return []
    return in_order(left[node]) + [data[node]] + in_order(right[node])


def pre_order(node):
    if node == 0:
        return []
    return [data[node]] + pre_order(left[node]) + pre_order(right[node])


def post_order(node):
    if node == 0:
        return []
    return post_order(left[node]) + post_order(right[node]) + [data[node]]


for value in [27, 14, 35, 10, 31, 19, 42]:
    insert_node(value)
print("Left: ", left[1:])
print("Data: ", data[1:])
print("Right:", right[1:])
print("Root", root_pointer, "Free", free_pointer)
print("Find 31:", find_node(31), "Find 50:", find_node(50))
print("In-order:  ", in_order(root_pointer))
print("Pre-order: ", pre_order(root_pointer))
print("Post-order:", post_order(root_pointer))
```

Output:

```output
Left:  [2, 4, 5, 0, 0, 0, 0]
Data:  [27, 14, 35, 10, 31, 19, 42]
Right: [3, 6, 7, 0, 0, 0, 0]
Root 1 Free 0
Find 31: 5 Find 50: 0
In-order:   [10, 14, 19, 27, 31, 35, 42]
Pre-order:  [27, 14, 10, 19, 35, 31, 42]
Post-order: [10, 19, 14, 31, 42, 35, 27]
```

| Node | LeftPointer | Data | RightPointer |
|---|---|---|---|
| 1 | 2 | 27 | 3 |
| 2 | 4 | 14 | 6 |
| 3 | 5 | 35 | 7 |
| 4 | 0 | 10 | 0 |
| 5 | 0 | 31 | 0 |
| 6 | 0 | 19 | 0 |
| 7 | 0 | 42 | 0 |

The in-order output is sorted, which is why a binary search tree is a way of sorting as well as searching. Pre-order outputs a node before its children, so it is the order for copying a tree. Post-order outputs the children first: for an expression tree it gives Reverse Polish notation (see the stretch question). `FreePointer` is 0 because all 7 nodes are used.

:::exam Deleting from a tree
Deleting a node from a binary tree is **not** one of the operations the syllabus asks you to write: finding and inserting are. Know what a delete would have to do (reconnect the children of the removed node), but spend your revision time on insert, find and traversals.
:::

### An object-oriented version

Paper 4 may ask for the tree as a class. Each node is an object with `left`, `data` and `right` fields, and the recursive functions are the same as in pseudocode. This program also finds the **height** of a tree (the number of levels) for a balanced tree and for one built from sorted data.

```python
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def insert(node, new_item):
    if node is None:
        return TreeNode(new_item)
    if new_item < node.data:
        node.left = insert(node.left, new_item)
    else:
        node.right = insert(node.right, new_item)
    return node


def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


balanced = None
for value in [27, 14, 35, 10, 31, 19, 42]:
    balanced = insert(balanced, value)
skewed = None
for value in [10, 14, 19, 27, 31, 35, 42]:
    skewed = insert(skewed, value)
print(in_order(balanced), "height", height(balanced))
print(in_order(skewed), "height", height(skewed))
```

Output:

```output
[10, 14, 19, 27, 31, 35, 42] height 3
[10, 14, 19, 27, 31, 35, 42] height 7
```

Both trees hold the same seven values and give the same in-order output, but searching the skewed tree may need 7 comparisons against at most 3 in the balanced one. A tree built from sorted data has every node with only a right child: it behaves as a linked list, and a search is \(O(n)\) instead of \(O(\log n)\).

## Dictionaries

:::def Dictionary
An abstract data type that stores data as pairs, each made of a key and a value, and finds the value from its key. Each key appears only once.
:::

A phone book is a dictionary: the name is the key, the number is the value. You look up by key, not by position. The operations are **add** a pair, **look up** a value by its key, and **delete** a pair.

A dictionary can be built from arrays. The simplest way is an array of records with a `Key` and a `Value` field, searched with a linear search, which takes \(O(n)\) comparisons.

```pseudocode
TYPE Entry
   DECLARE Key : STRING
   DECLARE Value : STRING
ENDTYPE

DECLARE Phonebook : ARRAY[1:50] OF Entry

FUNCTION LookUp(SearchKey : STRING) RETURNS STRING
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 50
      IF Phonebook[Index].Key = SearchKey THEN
         RETURN Phonebook[Index].Value
      ENDIF
   NEXT Index
   RETURN "not found"
ENDFUNCTION
```

A faster way is a **hash table**. A **hash function** turns the key into an array position, so the look-up goes straight to the right place, in about one step, whatever the size of the dictionary. For an integer key and a table of 7 places, a simple hash function is \((\text{Key MOD } 7) + 1\), which always gives a position from 1 to 7.

Two keys can hash to the same position. This is a **collision**. One way of handling it is **linear probing**: try the next place, wrapping round from the last to the first, until a free place (or the key itself) is found. A place holding 0 here means "empty".

```pseudocode
DECLARE Keys : ARRAY[1:7] OF INTEGER
DECLARE Values : ARRAY[1:7] OF STRING

FUNCTION HashIndex(Key : INTEGER) RETURNS INTEGER
   RETURN (Key MOD 7) + 1
ENDFUNCTION

FUNCTION AddEntry(Key : INTEGER, Value : STRING) RETURNS BOOLEAN
   DECLARE Index, Tried : INTEGER
   Index ← HashIndex(Key)
   Tried ← 0
   WHILE Keys[Index] <> 0 AND Keys[Index] <> Key AND Tried < 7
      Index ← (Index MOD 7) + 1
      Tried ← Tried + 1
   ENDWHILE
   IF Tried = 7 THEN
      RETURN FALSE
   ENDIF
   Keys[Index] ← Key
   Values[Index] ← Value
   RETURN TRUE
ENDFUNCTION

FUNCTION GetValue(Key : INTEGER) RETURNS STRING
   DECLARE Index, Tried : INTEGER
   Index ← HashIndex(Key)
   Tried ← 0
   WHILE Keys[Index] <> 0 AND Keys[Index] <> Key AND Tried < 7
      Index ← (Index MOD 7) + 1
      Tried ← Tried + 1
   ENDWHILE
   IF Keys[Index] = Key THEN
      RETURN Values[Index]
   ELSE
      RETURN "not found"
   ENDIF
ENDFUNCTION
```

The Python version adds four product codes. 1042 and 1049 both leave a remainder of 6 when divided by 7, so both hash to position 7: a collision. The program then does the same with Python's built-in dictionary, `dict`, which does all this for you.

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [0] * (size + 1)
        self.values = [None] * (size + 1)

    def hash_index(self, key):
        return key % self.size + 1

    def add(self, key, value):
        index = self.hash_index(key)
        tried = 0
        while self.keys[index] != 0 and self.keys[index] != key and tried < self.size:
            index = index % self.size + 1
            tried = tried + 1
        if tried == self.size:
            return False
        self.keys[index] = key
        self.values[index] = value
        return True

    def get(self, key):
        index = self.hash_index(key)
        tried = 0
        while self.keys[index] != 0 and self.keys[index] != key and tried < self.size:
            index = index % self.size + 1
            tried = tried + 1
        if self.keys[index] == key:
            return self.values[index]
        return "not found"


table = HashTable(7)
for code, name in [(1042, "lamp"), (2317, "desk"), (3085, "chair"), (1049, "shelf")]:
    table.add(code, name)
print(table.keys[1:])
print(table.values[1:])
print(table.get(1049), table.get(2317), table.get(9999))
shop = {1042: "lamp", 2317: "desk", 3085: "chair", 1049: "shelf"}
print(shop[1049], shop.get(9999, "not found"), len(shop))
```

Output:

```output
[2317, 1049, 0, 0, 0, 3085, 1042]
['desk', 'shelf', None, None, None, 'chair', 'lamp']
shelf desk not found
shelf not found 4
```

Follow 1049: its hash position is \((1049 \bmod 7) + 1 = 7\), which holds 1042. Probing moves on and wraps to position 1, which holds 2317, then to position 2, which is free. So 1049 is stored at position 2, and `get` follows the same path to find it. A hash table gives \(O(1)\) look-up on average, but a table that is nearly full has long probe chains, and deleting an entry needs care so the chain is not broken. Deletion from a hash table is not asked at this level.

## Graphs

:::def Graph
An abstract data type made of a set of vertices (nodes) joined by edges. An edge can carry a weight, such as a distance or a cost, and can be directed (one way only) or undirected (both ways).
:::

A graph models things that are **connected in any pattern**: towns joined by roads, routers joined by cables, people joined by friendships. Unlike a tree, a graph has no root, a vertex can have any number of edges, and there can be several routes between two vertices, even a **cycle**, a route that returns to its start.

:::html
<figure class="fig small"><svg viewBox="0 0 340 190" role="img" aria-label="A weighted undirected graph with five vertices A, B, C, D and E and six edges. A to B has weight 4. A to C has weight 2. B to C has weight 1. B to D has weight 5. C to D has weight 8. D to E has weight 3."><line class="ln" x1="50" y1="95" x2="140" y2="35"/><line class="ln" x1="50" y1="95" x2="140" y2="155"/><line class="ln" x1="140" y1="35" x2="140" y2="155"/><line class="ln" x1="140" y1="35" x2="235" y2="95"/><line class="ln" x1="140" y1="155" x2="235" y2="95"/><line class="ln" x1="235" y1="95" x2="310" y2="95"/><text class="tl tc" x="88" y="56">4</text><text class="tl tc" x="88" y="142">2</text><text class="tl tc" x="126" y="99">1</text><text class="tl tc" x="195" y="56">5</text><text class="tl tc" x="195" y="142">8</text><text class="tl tc" x="272" y="84">3</text><circle class="fm s-acc sw2" cx="50" cy="95" r="16"/><text class="tl tc tb" x="50" y="100">A</text><circle class="fm s-acc sw2" cx="140" cy="35" r="16"/><text class="tl tc tb" x="140" y="40">B</text><circle class="fm s-acc sw2" cx="140" cy="155" r="16"/><text class="tl tc tb" x="140" y="160">C</text><circle class="fm s-acc sw2" cx="235" cy="95" r="16"/><text class="tl tc tb" x="235" y="100">D</text><circle class="fm s-acc sw2" cx="310" cy="95" r="16"/><text class="tl tc tb" x="310" y="100">E</text></svg><figcaption>A weighted graph: five vertices (A to E) and six edges. The number on each edge is its weight, for example the distance in kilometres between two towns.</figcaption></figure>
:::

There are two standard ways to store a graph.

:::def Adjacency matrix
A two-dimensional array with one row and one column for each vertex. The element in row \(i\) and column \(j\) holds the weight of the edge from vertex \(i\) to vertex \(j\) (or 1 for an unweighted edge), and 0 when there is no edge. For an undirected graph the matrix is symmetric.
:::

:::def Adjacency list
For each vertex, a list of the vertices it is joined to (with the edge weights). Only the edges that exist are stored.
:::

For the graph in the figure, the matrix has 5 rows and 5 columns (rows and columns in the order A, B, C, D, E):

| | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 4 | 2 | 0 | 0 |
| B | 4 | 0 | 1 | 5 | 0 |
| C | 2 | 1 | 0 | 8 | 0 |
| D | 0 | 5 | 8 | 0 | 3 |
| E | 0 | 0 | 0 | 3 | 0 |

and the adjacency list is: A: B(4), C(2); B: A(4), C(1), D(5); C: A(2), B(1), D(8); D: B(5), C(8), E(3); E: D(3). This program builds both from the list of edges.

```python
vertices = ["A", "B", "C", "D", "E"]
edges = [("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "D", 8), ("D", "E", 3)]
size = len(vertices)
matrix = [[0] * size for row in range(size)]
adjacency = {}
for vertex in vertices:
    adjacency[vertex] = []
for start, end, weight in edges:
    i = vertices.index(start)
    j = vertices.index(end)
    matrix[i][j] = weight
    matrix[j][i] = weight
    adjacency[start].append((end, weight))
    adjacency[end].append((start, weight))
for row in matrix:
    print(row)
print(adjacency["D"])
print("Edges:", len(edges), "Matrix entries used:", sum(1 for row in matrix for x in row if x != 0))
```

Output:

```output
[0, 4, 2, 0, 0]
[4, 0, 1, 5, 0]
[2, 1, 0, 8, 0]
[0, 5, 8, 0, 3]
[0, 0, 0, 3, 0]
[('B', 5), ('C', 8), ('E', 3)]
Edges: 6 Matrix entries used: 12
```

Each undirected edge fills two matrix cells (12 for 6 edges). The matrix answers "is there an edge between these two?" in one step, but always uses \(n^2\) cells, mostly zeros when the graph has few edges. The list uses memory in proportion to the vertices and edges, so it suits a **sparse** graph with few edges, such as a road network.

:::key Using a graph, and why not a tree
- Use a **graph** when items are joined in a many-to-many pattern with no single top item: road maps, computer networks, social networks, the states of a puzzle. Weights let you ask for the shortest or cheapest route ([Graphs and pathfinding: Dijkstra and A\*](#cs.ai) shows Dijkstra's algorithm and A\* working on graphs).
- Use a **tree** when the data is a hierarchy: each item has exactly one parent except the root, there are no cycles, and there is exactly one path from the root to any node (folders in a file system, a family tree down the generations, a sorted collection for searching).
- A tree is a special graph: connected, with no cycles. If items can be joined in more than one way or form loops, a tree cannot show it.
:::

No code is asked for on graphs: you must know the features, be able to read or complete an adjacency matrix or list, and justify choosing a graph.

## Building one ADT from another

An ADT is defined by its operations, so it can be built from any structure that can do the work. The syllabus asks you to understand how a stack, queue, linked list, dictionary and binary tree can be implemented from another ADT or from the built-in types, and to give the reasoning.

| ADT | Implemented from | How, and the reasoning |
|---|---|---|
| Stack | an array and a top pointer | the pointer moves up on push and down on pop, so each operation is \(O(1)\); the size is fixed |
| Stack | a linked list | push inserts a node at the front, pop deletes the front node; \(O(1)\) and no fixed size, as long as there are free nodes |
| Queue | an array and two pointers (circular) | the pointers wrap round, so no space is wasted |
| Queue | two stacks | an in-stack takes enqueues, an out-stack gives dequeues; useful when only a stack is available |
| Priority queue | a list kept in order of priority | insert in the right place; dequeue takes the front |
| Linked list | two arrays (data and pointers) | pointers are array indexes; a free list reuses nodes |
| Dictionary | an array of key–value records, or a hash table | linear search is simple but \(O(n)\); hashing is \(O(1)\) on average |
| Binary tree | an array of records with left and right pointers | as in this chapter; no memory is allocated while the program runs |

**A stack from a linked list.** The top of the stack is the front of the list, so both operations work on `StartPointer` and take one step each, whatever the size.

```pseudocode
FUNCTION PushOnList(NewItem : INTEGER) RETURNS BOOLEAN
   DECLARE NewNode : INTEGER
   IF FreePointer = 0 THEN
      RETURN FALSE
   ENDIF
   NewNode ← FreePointer
   FreePointer ← Pointer[NewNode]
   Data[NewNode] ← NewItem
   Pointer[NewNode] ← StartPointer
   StartPointer ← NewNode
   RETURN TRUE
ENDFUNCTION

FUNCTION PopFromList() RETURNS INTEGER
   DECLARE OldNode, Item : INTEGER
   IF StartPointer = 0 THEN
      RETURN -1
   ENDIF
   OldNode ← StartPointer
   Item ← Data[OldNode]
   StartPointer ← Pointer[OldNode]
   Pointer[OldNode] ← FreePointer
   FreePointer ← OldNode
   RETURN Item
ENDFUNCTION
```

**A queue from two stacks.** Dequeuing needs the **oldest** item, which is at the bottom of a stack. Two stacks solve this, because moving every item from one stack to another **reverses** their order.

:::steps
1. **Enqueue**: push the item onto the in-stack.
2. **Dequeue**: if the out-stack is empty, pop every item from the in-stack and push it onto the out-stack. The oldest item is now on top of the out-stack.
3. Pop the out-stack and return the item. (If both stacks are empty, the queue is empty.)
4. Items already on the out-stack are older than anything on the in-stack, so they are always taken first.
:::

In the class below, `[]` is an empty list, `append` adds an item at the end of a list (a push) and `pop()` removes the last item (a pop). An empty list counts as `False` in an `if`, so `if not self.out_stack` means "the out-stack is empty".

```python
class QueueFromStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack.pop()


queue = QueueFromStacks()
for letter in ["A", "B", "C"]:
    queue.enqueue(letter)
print("In:", queue.in_stack, "Out:", queue.out_stack)
print("Dequeue:", queue.dequeue(), "In:", queue.in_stack, "Out:", queue.out_stack)
queue.enqueue("D")
print("In:", queue.in_stack, "Out:", queue.out_stack)
print("Dequeue:", queue.dequeue(), queue.dequeue(), queue.dequeue())
print("Dequeue:", queue.dequeue())
```

Here a Python list is used only through `append` (push) and `pop` (pop from the end), so it behaves as a stack. The lists print with the bottom of the stack first.

Output:

```output
In: ['A', 'B', 'C'] Out: []
Dequeue: A In: [] Out: ['C', 'B']
In: ['D'] Out: ['C', 'B']
Dequeue: B C D
Dequeue: None
```

The items leave in the order A, B, C, D, which is the order they arrived, so it is a queue. An item is moved at most once, so each operation costs \(O(1)\) on average.

**A priority queue from a list.** In a priority queue each item has a priority, and the item with the highest priority leaves first (here 1 is the highest, and items of equal priority leave in the order they arrived). The list is kept in priority order by inserting each item after those of the same or higher priority, so the front of the list is always the next item to leave.

```python
jobs = []


def add_job(priority, name):
    position = 0
    while position < len(jobs) and jobs[position][0] <= priority:
        position = position + 1
    jobs.insert(position, (priority, name))


for priority, name in [(2, "report"), (1, "invoice"), (3, "photo"), (1, "payslip"), (2, "memo")]:
    add_job(priority, name)
print(jobs)
while len(jobs) > 0:
    print("Print next:", jobs.pop(0)[1])
```

Output:

```output
[(1, 'invoice'), (1, 'payslip'), (2, 'report'), (2, 'memo'), (3, 'photo')]
Print next: invoice
Print next: payslip
Print next: report
Print next: memo
Print next: photo
```

:::eg Choosing an ADT and justifying it (exam style)
State the most suitable abstract data type for each task, and give a reason. [4 marks]

(a) A word processor keeps a record of each change so the user can undo the most recent change first.
(b) A bus company stores the connections between 30 towns, with the distance for each connection, to plan routes.
(c) A school stores each pupil's telephone number, found by typing the pupil's name.
(d) A print server receives jobs from many users and must print them in the order received.

(a) A stack [B1] because the most recent change must be undone first: last in, first out.

(b) A graph [B1] because the towns are connected in a many-to-many pattern, and each connection has a weight (the distance).

(c) A dictionary [B1] because the data is stored as pairs, and the telephone number (the value) is found from the name (the key).

(d) A queue [B1] because the first job received must be the first printed: first in, first out.

Each answer needs the structure **and** a reason taken from the scenario.
:::

## Spot the error

:::eg Spot the error: a linked list insertion at the front
Question: A linked list stored in the arrays `Data` and `Pointer` has the variables `StartPointer` and `FreePointer`. The list is not full. Write a procedure `InsertAtFront(NewItem)` that adds `NewItem` as the new first node. [5 marks]

A student wrote:

```pseudocode
01  PROCEDURE InsertAtFront(NewItem : STRING)
02     DECLARE NewNode : INTEGER
03     NewNode ← FreePointer
04     Data[NewNode] ← NewItem
05     Pointer[NewNode] ← StartPointer
06     StartPointer ← NewNode
07  ENDPROCEDURE
```

Line 03 takes the first free node [B1]. Line 04 stores the item in it [B1]. Line 05 makes the new node point to the old first node [B1]. Line 06 makes the new node the first node [B1]. **The procedure never moves `FreePointer` on to the next free node, so the free list still starts at the node that has just been used** [B0]. The answer scores 4 out of 5.

The damage shows on the second call. Take 3 nodes, with `StartPointer` 0, `FreePointer` 1, and `Pointer` holding 2, 3, 0. The first call uses node 1: `Data[1]` is set, `Pointer[1]` becomes 0 and `StartPointer` becomes 1; `FreePointer` is still 1. The second call takes node 1 **again**: it overwrites `Data[1]`, sets `Pointer[1]` to `StartPointer`, which is 1, and the node points to itself. The first item is lost and a traversal would repeat the new item for ever. The fix is one line placed **before** line 05, because line 05 overwrites `Pointer[NewNode]`, which still holds the free list's next node: `FreePointer ← Pointer[NewNode]`.
:::

## Try it yourself

:::try Start easy, finish at exam standard
Q: Explain what is meant by an abstract data type, using a stack as the example.
A: An ADT is a collection of data with a set of operations on it, described without saying how it is stored. A stack is defined by push, pop and peek on a last in, first out collection; it could be an array or a linked list, and the user of the stack need not know which.
Q: An empty stack of integers has the operations push 5, push 9, pop, push 2, push 7, pop, pop applied in order. List what each pop returns and what remains.
A: The first pop returns 9, the second returns 7 and the third returns 2. The stack then holds just 5, with the top pointer at 1.
Q: A circular queue has 5 places. The rear pointer is 5. Which position does the next item go in? Give the calculation.
A: \((5 \bmod 5) + 1 = 0 + 1 = 1\), so it wraps round to position 1 (provided the queue is not full).
Q: What does the null pointer 0 stored in the last node of a linked list tell a traversal, and why is 0 a safe choice?
A: It tells the traversal that there is no next node, so it stops. 0 is safe because array indexes start at 1, so no real node has the number 0.
Q: A binary search tree is built by inserting 50, 30, 70, 20, 40 in that order. State the root, the leaves and the in-order traversal.
A: The root is 50. The leaves are 20, 40 and 70 (nodes with no children). The in-order traversal is 20, 30, 40, 50, 70, in ascending order.
Q: Using the hash function \((\text{Key MOD } 7) + 1\) with linear probing, where does each of the keys 15 and 22 go in an empty table of 7 places, when 15 is added first?
A: \(15 \bmod 7 = 1\), so 15 goes to position 2. \(22 \bmod 7 = 1\) also, so 22 hashes to position 2 too; that is occupied, so it moves to position 3.
Q: Draw the adjacency matrix for an unweighted undirected graph with vertices A, B, C and edges A–B and B–C, using 1 for an edge.
A: Rows and columns in the order A, B, C. Row A is 0, 1, 0. Row B is 1, 0, 1. Row C is 0, 1, 0. The matrix is symmetric.
Q: Name the best ADT for each: (a) the pages you have visited in a browser, so that Back goes to the most recent; (b) customers waiting for a bank cashier; (c) a map of train stations with journey times; (d) looking up a word's meaning by the word.
A: (a) a stack; (b) a queue; (c) a weighted graph; (d) a dictionary.
Q: Why is a binary search a poor choice for the data of a linked list, even if the list is in order?
A: A binary search needs direct access to the middle element. A linked list has no index: finding the middle means following pointers from the start, so there is no saving over a linear search. (See [Searching, sorting and Big O](#cs.algorithms2).)
Q: A balanced binary search tree holds 1000 values. About how many comparisons does a search need at most? And a tree built from sorted data?
A: A balanced tree with 10 levels can hold up to \(2^{10} - 1 = 1023\) nodes (and 9 levels only 511), so a search needs at most 10 comparisons. A tree built from sorted data is a chain of 1000 nodes, so up to 1000.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ Describe what is meant by an abstract data type and give one example.
A: A collection of data [B1] together with the operations that can be performed on it [B1], described independently of how it is stored or implemented [B1]. (Example: a stack, with push and pop; or a queue with enqueue and dequeue.)

Q: [4 marks] ★★ A linked list of town names is stored in the arrays `Data` and `Pointer`, with `StartPointer` and `FreePointer`. The null pointer is 0. The state of the arrays is shown below.

| Index | Data | Pointer |
|---|---|---|
| 1 | Market | 5 |
| 2 | Harbour | 1 |
| 3 | Temple | 0 |
| 4 | Station | 3 |
| 5 | School | 4 |
| 6 | | 7 |
| 7 | | 0 |

`StartPointer` is 2 and `FreePointer` is 6. The items "School" and then "Harbour" are deleted, using the algorithm in this chapter. Complete the `Pointer` column, `StartPointer` and `FreePointer` after both deletions.
H: Deleting a node changes the pointer of the node before it, and then puts the deleted node at the front of the free list.
H: "Harbour" is the first node of the list.
A: After both deletions the `Pointer` column is 4, 5, 0, 3, 6, 7, 0, with `StartPointer` 1 and `FreePointer` 2.

| Index | Data | Pointer |
|---|---|---|
| 1 | Market | 4 |
| 2 | Harbour | 5 |
| 3 | Temple | 0 |
| 4 | Station | 3 |
| 5 | School | 6 |
| 6 | | 7 |
| 7 | | 0 |

- `Pointer[1]` is 4, so Market skips School [B1]
- `Pointer[5]` is 6 and `Pointer[2]` is 5, so the two deleted nodes are chained into the free list [B1]
- `StartPointer` is 1, because Harbour was the first node [B1]
- `FreePointer` is 2, because Harbour was the last node deleted [B1]

Q: [5 marks] ★★ A binary search tree is built by inserting the values 8, 3, 10, 1, 6, 14, 4 in that order into an empty tree. (a) State the output of an in-order traversal. [1] (b) State the output of a post-order traversal. [2] (c) A search is made for the value 4. List the values it is compared with, in order, and state how many comparisons are made. [2]
H: The tree is: root 8; left child 3 (children 1 and 6, where 6 has a left child 4); right child 10 (with a right child 14).
H: A post-order traversal outputs the left subtree, then the right subtree, then the node.
A: (a) 1, 3, 4, 6, 8, 10, 14 [B1] (ascending order).

(b) 1, 4, 6, 3, 14, 10, 8. [B2] (B1 if the order is almost right, for example one subtree reversed or the root not last.)

(c) 4 is compared with 8, then 3, then 6, then 4 [B1]: 4 comparisons [B1].

Q: [5 marks] ★★ A delivery company has four depots P, Q, R and S. The roads between them (in both directions) and their lengths in kilometres are: P to Q 6, P to R 3, Q to R 2, R to S 5. (a) Complete an adjacency matrix for the network, using rows and columns in the order P, Q, R, S and 0 where there is no road. [3] (b) Justify the use of a graph rather than a tree to store this network. [2]
H: A road in both directions means the matrix is symmetric.
A: (a)

| | P | Q | R | S |
|---|---|---|---|---|
| P | 0 | 6 | 3 | 0 |
| Q | 6 | 0 | 2 | 0 |
| R | 3 | 2 | 0 | 5 |
| S | 0 | 0 | 5 | 0 |

- every road shown in both directions (the matrix is symmetric about the diagonal) [B1]
- rows P and Q correct [B1]
- rows R and S correct, with 0 on the diagonal and where there is no road [B1]

(b) Depots P, Q and R are all joined to each other, forming a cycle [B1], and a tree has no cycles and only one route between two nodes; a graph can also store the weights of the roads (lengths) and has no single root [B1].

Q: [6 marks] ★★ A queue is implemented using two stacks, `InStack` and `OutStack`, both empty at the start. Enqueue 5, enqueue 8, dequeue, enqueue 2, dequeue, dequeue are carried out in this order. Complete a table showing the contents of each stack (bottom item first) after each operation, and the value returned by each dequeue.
H: Items move from `InStack` to `OutStack` only when a dequeue finds `OutStack` empty, and they move one at a time.
A: One row for each operation.

| Operation | InStack (bottom first) | OutStack (bottom first) | Value returned |
|---|---|---|---|
| Enqueue 5 | 5 | | |
| Enqueue 8 | 5, 8 | | |
| Dequeue | | 8 | 5 |
| Enqueue 2 | 2 | 8 | |
| Dequeue | 2 | | 8 |
| Dequeue | | | 2 |

- Enqueue 5 and Enqueue 8 both go on `InStack` [B1]
- the first dequeue moves 8 then 5 to `OutStack`, so 5 is on top, and returns 5 [B1]
- after the first dequeue `InStack` is empty and `OutStack` holds 8 [B1]
- Enqueue 2 goes on `InStack`; `OutStack` is unchanged [B1]
- the second dequeue returns 8 from `OutStack` without moving anything [B1]
- the third dequeue finds `OutStack` empty, moves 2 across and returns 2, leaving both stacks empty [B1]

Q: [6 marks] ★★ A linked list of whole numbers is stored in the arrays `Value` and `NextPtr`, with `StartPtr` pointing at the first node. The null pointer is 0. The list is not in any particular order. Write a function `CountAbove(Limit)` that returns the number of items in the list that are greater than `Limit`.
H: Follow the pointers from `StartPtr`, as `OutputList` does, and count instead of outputting.
H: You must visit every node, so there is no early exit.
A: One possible answer:

```pseudocode
FUNCTION CountAbove(Limit : INTEGER) RETURNS INTEGER
   DECLARE Current, Total : INTEGER
   Total ← 0
   Current ← StartPtr
   WHILE Current <> 0
      IF Value[Current] > Limit THEN
         Total ← Total + 1
      ENDIF
      Current ← NextPtr[Current]
   ENDWHILE
   RETURN Total
ENDFUNCTION
```

- function header with an integer parameter, returning an integer [B1]
- counter initialised to 0 [B1]
- current pointer starts at `StartPtr` [B1]
- loop that continues until the pointer is 0 [B1]
- compares `Value[Current]` with `Limit` and increments the counter [B1]
- moves to the next node with `NextPtr[Current]` inside the loop, and returns the counter after the loop [B1]

Q: [7 marks] ★★★ A binary search tree of names is stored in three arrays of size 20: `Names : ARRAY[1:20] OF STRING`, `LeftPtr : ARRAY[1:20] OF INTEGER` and `RightPtr : ARRAY[1:20] OF INTEGER`. The variable `RootPtr` holds the index of the root, and is 0 while the tree is empty. The variable `NextFree` holds the index of the next unused node and starts at 1; nodes are used in order and never reused. A name that is alphabetically before a node's name goes to the left; any other name goes to the right. Write a procedure `AddName(NewName)` that adds a name to the tree, or outputs "Tree full" if all 20 nodes are used.
H: The new node always goes at a null pointer: walk down until you reach one, remembering the last node you left.
H: Set both pointers of the new node to 0, and do not forget to move `NextFree` on.
A: One possible answer:

```pseudocode
PROCEDURE AddName(NewName : STRING)
   DECLARE Current, Parent : INTEGER
   DECLARE GoLeft : BOOLEAN
   IF NextFree > 20 THEN
      OUTPUT "Tree full"
   ELSE
      Names[NextFree] ← NewName
      LeftPtr[NextFree] ← 0
      RightPtr[NextFree] ← 0
      IF RootPtr = 0 THEN
         RootPtr ← NextFree
      ELSE
         Current ← RootPtr
         WHILE Current <> 0
            Parent ← Current
            IF NewName < Names[Current] THEN
               GoLeft ← TRUE
               Current ← LeftPtr[Current]
            ELSE
               GoLeft ← FALSE
               Current ← RightPtr[Current]
            ENDIF
         ENDWHILE
         IF GoLeft = TRUE THEN
            LeftPtr[Parent] ← NextFree
         ELSE
            RightPtr[Parent] ← NextFree
         ENDIF
      ENDIF
      NextFree ← NextFree + 1
   ENDIF
ENDPROCEDURE
```

- tests whether the tree is full (`NextFree > 20`) and outputs "Tree full" [B1]
- stores the name in `Names[NextFree]` and sets both pointers of the new node to 0 [B1]
- if `RootPtr` is 0, makes the new node the root [B1]
- otherwise starts at the root and loops until a null pointer is reached [B1]
- compares `NewName` with `Names[Current]` to move to the left or right child [B1]
- keeps the last node visited (the parent) and the direction taken [B1]
- sets the parent's left or right pointer to the new node, and increments `NextFree` [B1]

Q: [9 marks] ★★★ A text editor keeps its last four actions in a stack, so that the user can undo them. Write program code in Python for a stack of at most 4 strings, using a list and a top pointer, with a function `push(item)` that returns `False` if the stack is full, and a function `pop()` that returns `None` if it is empty. Then write code that pushes "type", "bold", "paste", "delete" and "copy" in order (printing a message for any push that fails), undoes (pops) two actions, pushes "italic", and finally pops and prints every remaining action. Show the output.
H: Use a list of 5 with element 0 unused, so that the top pointer is the index of the top item and starts at 0.
H: The fifth push fails because the stack is full when the top pointer is 4.
A: One possible answer:

```python
history = [None] * 5
top_pointer = 0


def push(item):
    global top_pointer
    if top_pointer == 4:
        return False
    top_pointer = top_pointer + 1
    history[top_pointer] = item
    return True


def pop():
    global top_pointer
    if top_pointer == 0:
        return None
    item = history[top_pointer]
    top_pointer = top_pointer - 1
    return item


for action in ["type", "bold", "paste", "delete", "copy"]:
    if push(action):
        print("Stored", action)
    else:
        print("History full, could not store", action)
print("Undo:", pop())
print("Undo:", pop())
push("italic")
item = pop()
while item is not None:
    print("Undo:", item)
    item = pop()
print("Nothing left to undo")
```

Output:

```output
Stored type
Stored bold
Stored paste
Stored delete
History full, could not store copy
Undo: delete
Undo: paste
Undo: italic
Undo: bold
Undo: type
Nothing left to undo
```

- a list of 4 usable elements and a top pointer starting at 0 [B1]
- `push` returns `False` when the stack is full (top pointer 4) [B1]
- `push` increments the top pointer, stores the item and returns `True` [B1]
- `pop` returns `None` when the top pointer is 0 [B1]
- `pop` reads the item at the top, decrements the pointer and returns the item [B1]
- the five actions are pushed, with a message for the failed push of "copy" [B1]
- two pops are made and the correct items, "delete" and "paste", are printed [B1]
- "italic" is pushed and every remaining action is popped and printed until the stack is empty [B1]
- the output is correct: italic, bold, type, then the final message [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ The arithmetic expression \((6 + 2) \times (9 - 3)\) is stored as a binary tree in arrays. Each internal node holds an operator and each leaf holds a number, all stored as strings. The root is node 1.

| Node | LeftPointer | Data | RightPointer |
|---|---|---|---|
| 1 | 2 | * | 3 |
| 2 | 4 | + | 5 |
| 3 | 6 | - | 7 |
| 4 | 0 | 6 | 0 |
| 5 | 0 | 2 | 0 |
| 6 | 0 | 9 | 0 |
| 7 | 0 | 3 | 0 |

(a) State the output of a post-order traversal. [2] (b) Treat the output of (a) as an expression in Reverse Polish notation and evaluate it with a stack, showing the stack after each item. [3] (c) Say how the in-order traversal of this tree relates to the expression. [1]
H: Post-order outputs the left subtree, the right subtree, then the node.
H: In Reverse Polish notation a number is pushed; an operator pops two numbers (the first popped is the right-hand operand) and pushes the result.
A: (a) The post-order output is 6, 2, +, 9, 3, -, * [B2] (B1 if only one operator or number is in the wrong place).

(b) The stack after each item (bottom first): 6; 6, 2; then `+` pops 2 and 6 and pushes 8, giving 8; then 8, 9; 8, 9, 3; then `-` pops 3 and 9 and pushes 6, giving 8, 6; then `*` pops 6 and 8 and pushes 48, giving 48. The result is 48. [B1] [B1] [B1] (one mark for correct stack states up to `+`, one for the states up to `-`, one for the final `*` and the result 48).

(c) The in-order traversal outputs 6, +, 2, *, 9, -, 3: the original expression, but without the brackets, which the tree shape holds instead. [B1]

Q: [5 marks] ★★★ Values are inserted into an empty binary search tree in the order 5, 10, 15, 20, 25, 30, 35. A second tree is built from the same values inserted in the order 20, 10, 30, 5, 15, 25, 35. (a) State the number of levels in each tree. [2] (b) State how many comparisons it takes to find 35 in each tree. [2] (c) Use Big O notation to state the time complexity of a search in a tree of \(n\) values of each shape. [1]
H: Inserting the values in ascending order, every value is larger than all those already in the tree.
A: (a) The first tree has 7 levels, because each new value is larger than everything before it and goes to the right of the previous one, so the tree is a single chain [B1]. The second tree has 3 levels (20 at the root, 10 and 30 below, then 5, 15, 25 and 35) [B1].

(b) In the first tree, 35 is compared with every value, 7 comparisons [B1]; in the second it is compared with 20, 30 and 35, 3 comparisons [B1].

(c) \(O(n)\) for the first (chain) shape and \(O(\log n)\) for the balanced shape [B1].
:::

:::quiz
? Which statement best describes an abstract data type?
- A data structure stored in an array.
+ A collection of data and the operations on it, described without saying how it is stored.
- A data type built into a programming language.
- A structure that can only hold integers.
> An ADT is defined by its operations. The same ADT (a stack, for example) can be implemented with an array, a linked list or a library, so how it is stored is not part of its definition.
? A stack of 5 places holds 3 items. Which statement about its top pointer and a push is correct?
- The top pointer is 5 and a push causes overflow.
+ The top pointer is 3, and a push stores the item at index 4 and makes the pointer 4.
- The top pointer is 0 and the stack is empty.
- The top pointer is 3, and a push stores the item at index 3.
> The top pointer is the index of the top item, so it is 3. A push first adds 1 to it and then stores at that index. Storing at index 3 would overwrite the top item.
? In a circular queue of 6 places, the rear pointer is 6 and the queue is not full. Where does the next item go?
- Place 7
- Place 6
+ Place 1
- The item cannot be added.
> \((6 \bmod 6) + 1 = 1\): the pointer wraps round to the start of the array, which is the point of a circular queue. Place 7 does not exist.
? A node is deleted from a linked list stored in arrays. What must happen to the deleted node's place in the array?
- It is cleared and left alone.
- It is moved to the end of the list.
+ It is added to the free list, so that it can be used again.
- Nothing: the pointers are enough.
> If the node is not returned to the free list, its place can never be used again. The data may stay in the array, but no pointer leads to it from the list, so it is ignored until the node is reused.
? Which order of traversal outputs the values of a binary search tree in ascending order?
- Pre-order
- Post-order
+ In-order
- Level by level, from the root down
> In-order visits the left subtree (smaller values), then the node, then the right subtree (larger values). Pre-order and post-order output the root first or last.
? What does a `LeftPointer` of 0 mean in a binary tree stored in arrays?
- The node is the root.
+ The node has no left child.
- The left child is node 0.
- The node is a free node.
> 0 is the null pointer: it points to no node, because array indexes start at 1. A node with both pointers 0 is a leaf. The root is identified by `RootPointer`, not by a pointer value.
? Why is a tree built by inserting 1, 2, 3, 4, 5, 6, 7 into a binary search tree a poor structure for searching?
- It is not a binary search tree.
- It uses more memory than a balanced tree.
+ Every value goes to the right of the last, so the tree is a chain and a search is \(O(n)\).
- The in-order traversal is not sorted.
> The tree is still a valid binary search tree, with a sorted in-order output, but its height is 7, not 3, so a search can make up to 7 comparisons. For \(n\) values the height can be \(n\), against about \(\log_2 n\) for a balanced tree.
? A queue is built from two stacks, with in-stack holding A, B, C (C on top) and out-stack empty. What does a dequeue return?
- C
- B
+ A
- Nothing: the queue is empty.
> The dequeue moves C, then B, then A onto the out-stack, reversing the order, so A, the oldest, is on top and is returned.
? Why might a graph be used instead of a tree to store a bus network?
- A graph always uses less memory.
- A tree cannot store text.
+ Routes between stops can form loops and there is no single top stop, and a graph can store a weight (such as a distance) on each connection.
- A graph can only be stored as an adjacency matrix.
> A tree has a root and exactly one path between any two nodes. A real network has cycles and many routes. A graph can be stored as an adjacency matrix or as an adjacency list.
:::

:::checklist What you can now do
- [ ] I can explain what an abstract data type is and give the operations of a stack, queue, linked list, binary tree, dictionary and graph.
- [ ] I can write pseudocode and Python to push onto and pop from a stack, checking for overflow and underflow.
- [ ] I can write pseudocode and Python to add to and remove from a linear queue and a circular queue.
- [ ] I can write algorithms to find an item in, insert into, delete from and output a linked list stored in arrays, keeping the free list correct.
- [ ] I can write algorithms to find a value in, and insert a value into, a binary search tree stored in arrays.
- [ ] I can state the in-order, pre-order and post-order traversals of a binary tree.
- [ ] I can explain the key features of a graph, read an adjacency matrix and adjacency list, and justify using a graph.
- [ ] I can describe how a dictionary is implemented, using arrays or a hash table.
- [ ] I can explain how one ADT can be implemented from another, for example a queue from two stacks and a stack from a linked list.
- [ ] I can write the same ADTs in Python, using lists and classes, and test them.
:::

:::recap
- An **ADT** is data plus operations, independent of how it is stored. Stack (LIFO), queue (FIFO), linked list, binary tree, dictionary and graph are the ones in the syllabus.
- Stack: `TopPointer` is 0 when empty; push adds 1 then stores; pop reads then subtracts 1; check overflow and underflow. Circular queue: `p ← (p MOD Size) + 1` and a count for full or empty.
- Linked list in arrays: `Data`, `Pointer`, `StartPointer`, `FreePointer`; null pointer 0. Insert: take a free node (move `FreePointer` on), store, point the new node at the rest, then the previous node at the new node. Delete: skip the node, then put it at the front of the free list.
- Binary search tree: left subtree smaller, right subtree larger. Arrays of `LeftPointer`, `Data`, `RightPointer`, with `RootPointer`. Insert walks down to a null pointer and links the new node to the parent. Find follows left or right until found or a null pointer. In-order traversal gives ascending order; a balanced tree has a search of \(O(\log n)\), a chain \(O(n)\).
- Dictionary: key–value pairs, found by key; a hash table finds the place with a hash function and handles collisions by probing (\(O(1)\) on average); a linear search of an array is \(O(n)\).
- Graph: vertices, edges, weights, directed or undirected; stored as an adjacency matrix (\(n^2\) cells) or adjacency list (suits few edges). Use a graph for many-to-many connections and cycles; a tree for a hierarchy.
- One ADT from another: queue from two stacks (reverse by moving), stack from a linked list (push and pop at the front), priority queue from an ordered list.
:::

:::links
- practise: [Introduction to abstract data types: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/exam-questions/) · Save My Exams · AS-level stack, queue and linked list questions with mark schemes [paid]
- practise: [Algorithms: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/19-computational-thinking-and-problem-solving-/algorithms/exam-questions/) · Save My Exams · A Level questions on ADTs, trees and Big O [paid]
- explore: [Linked lists, stacks and queues](https://visualgo.net/en/list) · VisuAlgo · animated insert and delete on lists, stacks and queues
- explore: [Binary search trees](https://visualgo.net/en/bst) · VisuAlgo · insert, search and traversals of a binary search tree
- explore: [Data structure animations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) · USF · stacks, queues, trees, hash tables and graphs
- read: [Data structures in Python](https://docs.python.org/3/tutorial/datastructures.html) · Python.org · lists as stacks and queues, and dictionaries

Links checked 13 November 2026.
:::

Next: [Recursion](#cs.recursion)
