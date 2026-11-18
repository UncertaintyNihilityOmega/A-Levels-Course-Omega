@chapter cs.ai
@title Graphs and pathfinding: Dijkstra and A*
@level a2
@paper CAIE 9618 Paper 3
@time 5–7 hours
@summary A graph is a set of points joined by weighted lines, and it can model a road map, a game level, a puzzle or a robot's world. You will learn the vocabulary of graphs and apply Dijkstra's algorithm and the A* algorithm by hand, with tables, to find the shortest path, and you will explain why A* usually searches less than Dijkstra.

:::why
A route planner, a video game character and a warehouse robot all need the same thing: the cheapest way from here to there across a map. Computer scientists turn the map into a graph, and then one of two famous algorithms, Dijkstra's or A*, finds the route. Paper 3 asks you to apply both by hand, to say which nodes they visit and in what order, and to explain why one searches less than the other. These are marks you can collect with careful table work and a few exact definitions.
:::

**Before you start**, you should know arrays from [Data types, records and arrays](#cs.datatypes) and queues from [Text files, stacks, queues and linked lists](#cs.structures). The effects of AI on society were covered in [Ethics, ownership and the impact of AI](#cs.ethics). This chapter is the "how" of finding routes; the next chapter, [Machine learning and neural networks](#cs.ml), is the "how" of learning from data.

:::try Warm-up
Q: Write the pseudocode to declare a 2D array Maze of BOOLEAN values with 4 rows and 5 columns, and the element in row 3, column 2. (from [Data types, records and arrays](#cs.datatypes))
A: `DECLARE Maze : ARRAY[1:4, 1:5] OF BOOLEAN`. The element is `Maze[3, 2]`: the row first, then the column.
Q: In a queue, which item leaves first? (from [Text files, stacks, queues and linked lists](#cs.structures))
A: The item that has been waiting longest. A queue is first in, first out (FIFO).
Q: Give one benefit and one concern of using AI to make decisions about people. (from [Ethics, ownership and the impact of AI](#cs.ethics))
A: Benefit: decisions can be made faster and more cheaply. Concern: bias, because a system trained on unfair or incomplete data can treat some groups of people unfairly.
:::

:::note What the syllabus asks
You must understand how graphs can be used to aid AI, know the purpose and structure of a graph, and use A* and Dijkstra's algorithms to perform searches on a graph. You are not required to write algorithms to set up, access or search a graph. So this chapter teaches you to apply the algorithms by hand. One optional Python program, clearly marked, shows how a computer does the same work.
:::

## Graphs: vertices, edges and weights

A **graph** in this chapter is not a chart with axes. It is a drawing of points joined by lines, like a map of a metro system where the stations are the points and the tracks between them are the lines. Mathematicians and computer scientists use the same word, so you must be able to tell the two meanings apart by the context.

:::def Graph
A set of **vertices** (nodes) joined by **edges**. A graph models objects and the connections between them.
:::

:::def Vertex (node)
One point of a graph. It represents an object, such as a town, a junction, a square of a game board or a state of a puzzle. Vertices are also called nodes.
:::

:::def Edge
A line that joins two vertices of a graph. It represents a connection between the two objects, such as a road, a corridor or a legal move.
:::

Two vertices joined by an edge are **neighbours** (or adjacent). In the graph below, the neighbours of C are A, B and D.

:::html
<figure class="fig small"><svg viewBox="0 0 314 246" role="img" aria-label="A weighted undirected graph with four vertices A, B, C and D and four edges. The edge from A to B has weight 4, A to C has weight 2, B to C has weight 5 and C to D has weight 3."><line class="ln" x1="43" y1="123" x2="138" y2="43"/><line class="ln" x1="43" y1="123" x2="138" y2="203"/><line class="ln" x1="138" y1="43" x2="138" y2="203"/><line class="ln" x1="138" y1="203" x2="271" y2="123"/><text class="tl tc halo" x="90" y="87">4</text><text class="tl tc halo" x="90" y="167">2</text><text class="tl tc halo" x="138" y="127">5</text><text class="tl tc halo" x="204" y="167">3</text><circle class="f1 s-acc sw2" cx="43" cy="123" r="17"/><text class="tl tc tb" x="43" y="128">A</text><circle class="f1 s-acc sw2" cx="138" cy="43" r="17"/><text class="tl tc tb" x="138" y="48">B</text><circle class="f1 s-acc sw2" cx="138" cy="203" r="17"/><text class="tl tc tb" x="138" y="208">C</text><circle class="f1 s-acc sw2" cx="271" cy="123" r="17"/><text class="tl tc tb" x="271" y="128">D</text></svg><figcaption>A weighted graph with four vertices (A to D) and four edges. Each edge carries a weight. The neighbours of C are A, B and D.</figcaption></figure>
:::

The numbers on the edges are **weights**. A weight is the cost of using that edge: a distance in kilometres, a journey time in minutes, a price, or any quantity you want to keep small.

:::def Weighted graph
A graph in which every edge has a number, its weight (or cost), attached. The weight might be a distance, a time or a price.
:::

:::def Path
A sequence of vertices in which each vertex is joined to the next by an edge. The **cost** of a path is the sum of the weights of its edges.
:::

In the graph above, A, B, C, D is a path with cost \(4 + 5 + 3 = 12\), and A, C, D is a path with cost \(2 + 3 = 5\). The second path is cheaper, so it is the better route from A to D. The **shortest path** between two vertices is the path with the lowest cost. "Shortest" means lowest total weight, not fewest edges: a path of three cheap edges can beat a path of one expensive edge.

Edges do not always work in both directions. A one-way street can be driven in one direction only.

:::def Directed graph
A graph in which each edge has a direction, drawn as an arrow. An edge from S to T can be followed from S to T but not from T to S. In an **undirected** graph every edge works in both directions.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 246 198" role="img" aria-label="A directed weighted graph with three vertices S, T and U. An arrow goes from S to T with weight 3, an arrow from T to U with weight 2 and an arrow from U to S with weight 4."><line class="c1 sw2" x1="60" y1="43" x2="183" y2="43" marker-end="url(#ah)"/><line class="c1 sw2" x1="193" y1="57" x2="135" y2="139" marker-end="url(#ah)"/><line class="c1 sw2" x1="113" y1="141" x2="55" y2="59" marker-end="url(#ah)"/><text class="tl tc halo" x="123" y="60">3</text><text class="tl tc halo" x="152" y="95">2</text><text class="tl tc halo" x="94" y="95">4</text><circle class="f1 s-acc sw2" cx="43" cy="43" r="17"/><text class="tl tc tb" x="43" y="48">S</text><circle class="f1 s-acc sw2" cx="203" cy="43" r="17"/><text class="tl tc tb" x="203" y="48">T</text><circle class="f1 s-acc sw2" cx="123" cy="155" r="17"/><text class="tl tc tb" x="123" y="160">U</text></svg><figcaption>A directed graph: each edge is an arrow that can be followed in one direction only. You can go from S to T, but there is no edge from T back to S.</figcaption></figure>
:::

In the directed graph, the cost of going from S to U is \(3 + 2 = 5\) (S, T, U), but the cost of going from U to S is 4, the single arrow from U. The cost of a route can depend on which way you travel.

### How graphs help AI

A graph is useful in AI because many AI problems are really the question "what is the best sequence of steps from where I am to where I want to be?". If you can draw the situation as vertices and edges, an algorithm can search the graph for the answer without knowing anything about maps, games or robots.

| Problem | Vertices | Edges | Weights |
|---|---|---|---|
| Route finding on a road map | towns and junctions | roads | distance or journey time |
| Character moving through a game level | squares of a grid | steps between neighbouring squares | 1 for each step (or more for mud or water) |
| Robot in a warehouse | junctions of aisles | aisles | length of the aisle or time to drive it |
| Solving a puzzle | every arrangement of the puzzle | one legal move | 1 for each move |

The puzzle row is the surprising one. In the sliding-tile puzzle with eight numbered tiles on a 3 × 3 board, every arrangement of the tiles is a vertex. Two arrangements are joined by an edge when one move turns one into the other. A solution is a path from the scrambled arrangement to the sorted one, and the shortest path is the solution with the fewest moves. The graph of this small puzzle has 181,440 reachable arrangements, far too many to draw, but an algorithm can search it without anyone drawing it.

:::eg Using a graph to model a warehouse robot
A warehouse in Rotterdam has a robot that carries boxes between shelving areas. The aisles connect junctions, and some aisles are one-way. Explain how a graph could be used to find the quickest route for the robot. [4 marks]

Say what the vertices, the edges, the weights and the direction represent, then say what the algorithm does.

- Each junction (or shelving area) is a vertex. [B1]
- Each aisle between two junctions is an edge. [B1]
- The weight of each edge is the time (or distance) the robot needs to travel along that aisle. [B1]
- One-way aisles are directed edges, so the graph is directed; a search of the graph finds the path with the lowest total weight from the robot's vertex to the destination. [B1]

The last mark needs both ideas: direction for the one-way aisles, and a search for the lowest total weight. "The robot finds its way" earns nothing, because it does not say what the graph does.
:::

### Representing a graph

A drawing is for people. A program needs the graph stored in memory. You will not be asked to write this code, but you should recognise the two usual ways. Take the four-vertex graph above.

An **adjacency matrix** is a 2D array with one row and one column for every vertex. The entry in row X and column Y is the weight of the edge from X to Y, or 0 if there is no edge. This table is that matrix:

| | A | B | C | D |
|---|---|---|---|---|
| **A** | 0 | 4 | 2 | 0 |
| **B** | 4 | 0 | 5 | 0 |
| **C** | 2 | 5 | 0 | 3 |
| **D** | 0 | 0 | 3 | 0 |

Because the graph is undirected, the matrix is symmetrical: the entry in row A, column B equals the entry in row B, column A. A directed graph can have a matrix that is not symmetrical. A matrix always has \(n \times n\) entries for \(n\) vertices, even when most are 0.

An **adjacency list** stores, for every vertex, only the neighbours that it has, each with its weight:

| Vertex | Neighbours (with weights) |
|---|---|
| A | B (4), C (2) |
| B | A (4), C (5) |
| C | A (2), B (5), D (3) |
| D | C (3) |

A list uses less memory than a matrix when the graph has few edges, which is typical of road maps. A matrix answers "is there an edge between X and Y?" in one step. The graph as an abstract data type is covered in [Abstract data types: stacks, queues, lists, trees and graphs](#cs.adts).

For readers who like to see it, here is the adjacency list as a Python dictionary of dictionaries. This code is not examined.

```python
small = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 5},
    "C": {"A": 2, "B": 5, "D": 3},
    "D": {"C": 3},
}
print(small["C"])
print(list(small["C"]))
print(small["A"]["B"])
```

Output:

```output
{'A': 2, 'B': 5, 'D': 3}
['A', 'B', 'D']
4
```

The first line is every neighbour of C with its weight. The second lists only the neighbour names. The third is the weight of the edge from A to B.

## Dijkstra's algorithm

Suppose you want the shortest path from town A to town G in the map below. You could list every path and add up its cost, but the number of possible paths grows very quickly as towns are added. Dijkstra's algorithm avoids listing them. It finds the shortest path from the start to every vertex in order of distance, starting with the nearest, a bit like ripples spreading out from a stone dropped in a pond.

:::html
<figure class="fig small"><svg viewBox="0 0 364 306" role="img" aria-label="A road map drawn as a weighted graph with seven towns A to G. Roads and their lengths in kilometres: A to B 5, A to C 9, A to D 6, B to D 3, B to E 6, C to D 9, C to F 7, D to E 4, D to F 8, E to G 5, F to G 8."><line class="ln" x1="67" y1="153" x2="139" y2="273"/><line class="ln" x1="67" y1="153" x2="163" y2="33"/><line class="ln" x1="67" y1="153" x2="187" y2="193"/><line class="ln" x1="139" y1="273" x2="187" y2="193"/><line class="ln" x1="139" y1="273" x2="259" y2="273"/><line class="ln" x1="163" y1="33" x2="187" y2="193"/><line class="ln" x1="163" y1="33" x2="259" y2="73"/><line class="ln" x1="187" y1="193" x2="259" y2="273"/><line class="ln" x1="187" y1="193" x2="259" y2="73"/><line class="ln" x1="259" y1="273" x2="331" y2="153"/><line class="ln" x1="259" y1="73" x2="331" y2="153"/><text class="tl tc halo" x="103" y="217">5</text><text class="tl tc halo" x="115" y="97">9</text><text class="tl tc halo" x="127" y="177">6</text><text class="tl tc halo" x="163" y="237">3</text><text class="tl tc halo" x="199" y="277">6</text><text class="tl tc halo" x="175" y="117">9</text><text class="tl tc halo" x="211" y="57">7</text><text class="tl tc halo" x="223" y="237">4</text><text class="tl tc halo" x="223" y="137">8</text><text class="tl tc halo" x="295" y="217">5</text><text class="tl tc halo" x="295" y="117">8</text><circle class="f1 s-acc sw2" cx="67" cy="153" r="17"/><text class="tl tc tb" x="67" y="158">A</text><circle class="f1 s-acc sw2" cx="139" cy="273" r="17"/><text class="tl tc tb" x="139" y="278">B</text><circle class="f1 s-acc sw2" cx="163" cy="33" r="17"/><text class="tl tc tb" x="163" y="38">C</text><circle class="f1 s-acc sw2" cx="187" cy="193" r="17"/><text class="tl tc tb" x="187" y="198">D</text><circle class="f1 s-acc sw2" cx="259" cy="273" r="17"/><text class="tl tc tb" x="259" y="278">E</text><circle class="f1 s-acc sw2" cx="259" cy="73" r="17"/><text class="tl tc tb" x="259" y="78">F</text><circle class="f1 s-acc sw2" cx="331" cy="153" r="17"/><text class="tl tc tb" x="331" y="158">G</text></svg><figcaption>The town graph used in the worked examples. The number on each edge is the length of the road in kilometres.</figcaption></figure>
:::

:::def Dijkstra's algorithm
An algorithm that finds the shortest path from a start vertex to every other vertex of a weighted graph (or to one chosen destination). It repeatedly visits the unvisited vertex with the smallest known distance from the start, and uses it to improve the distances of its neighbours.
:::

For every vertex the algorithm keeps two facts: its **current shortest distance** from the start, and its **previous vertex**, the vertex just before it on the best route found so far. At the start the distance of every vertex except the start is unknown, which we write as ∞ (infinity), because "unknown" must be bigger than any real distance.

:::key Dijkstra's algorithm by hand
1. Give the start vertex distance 0. Give every other vertex distance ∞ and no previous vertex. No vertex is visited yet.
2. Choose the **unvisited vertex with the smallest distance**. If two are equal, take the one that comes first alphabetically. Mark it visited.
3. For each **unvisited neighbour** of the chosen vertex, work out *new distance = distance of the chosen vertex + weight of the edge*. If the new distance is **smaller** than the neighbour's current distance, replace the distance and set the neighbour's previous vertex to the chosen vertex. If it is equal or larger, change nothing.
4. Repeat from step 2 until the **destination is chosen in step 2**. (To find the distance to every vertex, continue until all are visited.)
5. Read the path backwards: start at the destination, follow the previous vertices to the start, then reverse the list. The destination's distance is the cost.
:::

A visited vertex is final: its distance can never be improved, because every other route to it would have to pass through a vertex that is at least as far away. That is why the algorithm chooses the smallest distance each time.

The tie rule in step 2 is this chapter's choice, so that every table has exactly one correct answer. Where an exam question gives its own rule for ties, use that one.

:::eg Dijkstra's algorithm on the town graph
Use Dijkstra's algorithm to find the shortest path from A to G in the town graph, and state its length in kilometres. [6 marks]

Record the table after each vertex is visited. A cell is blank when nothing changed in that step. A cell such as `5 A` means distance 5 with previous vertex A.

| Step | Visit | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|---|
| 0 |  | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A |  | 5 A | 9 A | 6 A |  |  |  |
| 2 | B |  |  |  |  | 11 B |  |  |
| 3 | D |  |  |  |  | 10 D | 14 D |  |
| 4 | C |  |  |  |  |  |  |  |
| 5 | E |  |  |  |  |  |  | 15 E |
| 6 | F |  |  |  |  |  |  |  |
| 7 | G |  |  |  |  |  |  |  |

Step by step, with the reasons:

- Step 0: A is the start, so A is 0 and all the rest are ∞. [B1]
- Step 1: the smallest distance is A (0), so visit A. Its neighbours get distances: B \(0 + 5 = 5\), C \(0 + 9 = 9\), D \(0 + 6 = 6\), each with previous vertex A. [B1]
- Step 2: the smallest unvisited distance is B (5). B's neighbours: D would be \(5 + 3 = 8\), which is not smaller than 6, so no change; E gets \(5 + 6 = 11\) via B. [B1]
- Step 3: the smallest unvisited is D (6). E would now be \(6 + 4 = 10\), which is smaller than 11, so E's distance becomes 10 and its previous vertex changes from B to D. F gets \(6 + 8 = 14\) via D. C would be \(6 + 9 = 15\), not smaller than 9. [B1]
- Steps 4 and 5: visit C (9): its neighbour F would be \(9 + 7 = 16\), not smaller than 14, so nothing changes. Visit E (10): G gets \(10 + 5 = 15\) via E. [B1]
- Steps 6 and 7: visit F (14): G would be \(14 + 8 = 22\), no change. G (15) is now the smallest, so G is chosen and the algorithm stops.

The final values are in this table. Follow the previous column back from G: G ← E ← D ← A. Reversed, the shortest path is **A, D, E, G**, with length \(6 + 4 + 5 = 15\) km. [B1]

| Node | Shortest distance | Previous node | Visited in order |
|---|---|---|---|
| A | 0 | none | 1 |
| B | 5 | A | 2 |
| C | 9 | A | 4 |
| D | 6 | A | 3 |
| E | 10 | D | 5 |
| F | 14 | D | 6 |
| G | 15 | E | 7 |

Check the answer by adding the edge weights of the path back up: 6, 4 and 5 give 15. Dijkstra's algorithm visited all 7 vertices before it stopped.
:::

The shortest path A, D, E, G has three edges. The route A, B, E, G has the same number of edges but costs \(5 + 6 + 5 = 16\), and the first road out of A that looks cheapest (A to B, 5 km) is not on the best route at all. A "go to the nearest neighbour" rule fails, and this is exactly why E's distance had to be improved in step 3.

:::warn Stop when the destination is chosen, not when it first gets a distance
A destination can receive a distance long before it is visited, and that first distance may not be the best. Only when the destination is the unvisited vertex with the smallest distance is its value final. Look at the small graph with edges S–T 10, S–U 3, U–V 2 and V–T 2, and a search from S to T:

| Step | Visit | S | T | U | V |
|---|---|---|---|---|---|
| 0 |  | 0 | ∞ | ∞ | ∞ |
| 1 | S |  | 10 S | 3 S |  |
| 2 | U |  |  |  | 5 U |
| 3 | V |  | 7 V |  |  |
| 4 | T |  |  |  |  |

After step 1, T already has a distance, 10, but it is not the smallest, so T is not chosen. Two more steps find the route S, U, V, T with length 7. A student who stopped at step 1 would answer 10.
:::

:::warn Update the previous vertex too
When you replace a distance, replace the previous vertex in the same step. If E's distance becomes 10 but its previous vertex stays B, the path you trace back is wrong (A, B, E, G) and no longer matches the distance you give. Equal is not better: when a new distance only equals the old one, change nothing.
:::

### A program that does the same

You will not write this in an exam, but it shows that the table method is exactly what a computer does. It stores the town graph as a dictionary of dictionaries and uses a standard library tool, `heapq`, to find the entry with the smallest value quickly. The function `search` is written to cover A* as well, which is the next section: give every vertex h = 0 and it is Dijkstra's algorithm.

```python
import heapq

town = {
    "A": {"B": 5, "C": 9, "D": 6},
    "B": {"A": 5, "D": 3, "E": 6},
    "C": {"A": 9, "D": 9, "F": 7},
    "D": {"A": 6, "B": 3, "C": 9, "E": 4, "F": 8},
    "E": {"B": 6, "D": 4, "G": 5},
    "F": {"C": 7, "D": 8, "G": 8},
    "G": {"E": 5, "F": 8},
}
straight_line = {"A": 11, "B": 8, "C": 7, "D": 6, "E": 4, "F": 3, "G": 0}
zero = {name: 0 for name in town}


def search(graph, h, start, goal):
    best = {start: 0}
    previous = {start: None}
    waiting = [(h[start], start)]
    done = []
    while waiting:
        f, node = heapq.heappop(waiting)
        if node in done:
            continue
        done.append(node)
        if node == goal:
            break
        for neighbour, weight in graph[node].items():
            g = best[node] + weight
            if neighbour not in done and (neighbour not in best or g < best[neighbour]):
                best[neighbour] = g
                previous[neighbour] = node
                heapq.heappush(waiting, (g + h[neighbour], neighbour))
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous[node]
    return done, best[goal], path[::-1]


print(search(town, zero, "A", "G"))
print(search(town, straight_line, "A", "G"))
```

Output:

```output
(['A', 'B', 'D', 'C', 'E', 'F', 'G'], 15, ['A', 'D', 'E', 'G'])
(['A', 'D', 'B', 'E', 'G'], 15, ['A', 'D', 'E', 'G'])
```

Each line shows the vertices in the order they were chosen, the cost, and the path. The first line (all h = 0, so Dijkstra's algorithm) matches the table above: visit order A, B, D, C, E, F, G. The second line uses the straight-line distances, which turns the search into A*, and it chooses only five vertices. The next section explains why.

## The A* algorithm

Dijkstra's algorithm has no sense of direction. On the town graph it visited F and C, which are not on the way to G, because they were close to A. When a graph is huge, such as a country's road network, visiting everything that is close to the start wastes a lot of time.

A* (said "A star") fixes this by adding a hint: an estimate of how far each vertex is from the destination. It then prefers vertices that are close to the start **and** look close to the destination.

:::def Heuristic
An estimate, given or calculated, of the cost of the cheapest path from a vertex to the destination. A heuristic is a rule of thumb that is quick to find and usually helpful, but is not guaranteed to be exact.
:::

For map problems the usual heuristic is the straight-line distance to the destination, because no road can be shorter than a straight line. On a grid, the usual heuristic is the **Manhattan distance**, explained in the next section. In an exam the heuristic values are given to you in a table or on the diagram.

:::def g-cost
The cost of the best path found so far from the start vertex to a vertex. It is known: it is the total of the edge weights actually travelled.
:::

:::def h-cost
The heuristic: the estimated cost from a vertex to the destination. It is a guess, and it is given.
:::

:::def f-cost
The total estimated cost of a path through a vertex: \(f = g + h\). A* always expands the open vertex with the lowest f-cost.
:::

:::def A* algorithm
A shortest-path algorithm that expands the vertex with the lowest \(f = g + h\), where g is the cost from the start and h is a heuristic estimate of the cost to the destination. It keeps an **open list** of vertices seen but not yet expanded, and a **closed list** of vertices already expanded.
:::

The open list holds the candidates: vertices you have found a way to reach, but have not yet "dealt with". The closed list holds vertices that are finished. To **expand** a vertex means to take it from the open list, move it to the closed list, and look at its neighbours.

:::key A* by hand
1. Put the start vertex in the open list with \(g = 0\) and \(f = h\). The closed list is empty.
2. Take the vertex in the open list with the **lowest f**. If two are equal, take the one that comes first alphabetically. Move it to the closed list. This is *expanding* it.
3. If it is the destination, stop: the path is found.
4. For each neighbour that is **not in the closed list**: work out *g = g of the expanded vertex + weight of the edge*, and \(f = g + h\) using the neighbour's own h. If the neighbour is not in the open list, add it, with the expanded vertex as its previous vertex. If it is already in the open list and the new g is **smaller**, replace its g, f and previous vertex. Otherwise change nothing.
5. Repeat from step 2. When the destination is expanded, trace the path back with the previous vertices. The cost is the destination's g.
:::

Compare this with the Dijkstra key box: it is the same method with one change. Dijkstra chooses the smallest g. A* chooses the smallest \(g + h\). With \(h = 0\) everywhere, A* is Dijkstra's algorithm.

The figure shows the town graph with its straight-line distances to G.

:::html
<figure class="fig small"><svg viewBox="0 0 364 320" role="img" aria-label="A road map drawn as a weighted graph with seven towns A to G. Roads and their lengths in kilometres: A to B 5, A to C 9, A to D 6, B to D 3, B to E 6, C to D 9, C to F 7, D to E 4, D to F 8, E to G 5, F to G 8. Beside each town is its straight-line distance h to G: A 11, B 8, C 7, D 6, E 4, F 3, G 0."><line class="ln" x1="67" y1="153" x2="139" y2="273"/><line class="ln" x1="67" y1="153" x2="163" y2="33"/><line class="ln" x1="67" y1="153" x2="187" y2="193"/><line class="ln" x1="139" y1="273" x2="187" y2="193"/><line class="ln" x1="139" y1="273" x2="259" y2="273"/><line class="ln" x1="163" y1="33" x2="187" y2="193"/><line class="ln" x1="163" y1="33" x2="259" y2="73"/><line class="ln" x1="187" y1="193" x2="259" y2="273"/><line class="ln" x1="187" y1="193" x2="259" y2="73"/><line class="ln" x1="259" y1="273" x2="331" y2="153"/><line class="ln" x1="259" y1="73" x2="331" y2="153"/><text class="tl tc halo" x="103" y="217">5</text><text class="tl tc halo" x="115" y="97">9</text><text class="tl tc halo" x="127" y="177">6</text><text class="tl tc halo" x="163" y="237">3</text><text class="tl tc halo" x="199" y="277">6</text><text class="tl tc halo" x="175" y="117">9</text><text class="tl tc halo" x="211" y="57">7</text><text class="tl tc halo" x="223" y="237">4</text><text class="tl tc halo" x="223" y="137">8</text><text class="tl tc halo" x="295" y="217">5</text><text class="tl tc halo" x="295" y="117">8</text><circle class="f1 s-acc sw2" cx="67" cy="153" r="17"/><text class="tl tc tb" x="67" y="158">A</text><circle class="f1 s-acc sw2" cx="139" cy="273" r="17"/><text class="tl tc tb" x="139" y="278">B</text><circle class="f1 s-acc sw2" cx="163" cy="33" r="17"/><text class="tl tc tb" x="163" y="38">C</text><circle class="f1 s-acc sw2" cx="187" cy="193" r="17"/><text class="tl tc tb" x="187" y="198">D</text><circle class="f1 s-acc sw2" cx="259" cy="273" r="17"/><text class="tl tc tb" x="259" y="278">E</text><circle class="f1 s-acc sw2" cx="259" cy="73" r="17"/><text class="tl tc tb" x="259" y="78">F</text><circle class="f1 s-acc sw2" cx="331" cy="153" r="17"/><text class="tl tc tb" x="331" y="158">G</text><text class="tl tc" x="25" y="154">h = 11</text><text class="tl tc" x="139" y="305">h = 8</text><text class="tl tc" x="202" y="34">h = 7</text><text class="tl tc" x="226" y="194">h = 6</text><text class="tl tc" x="259" y="305">h = 4</text><text class="tl tc" x="259" y="50">h = 3</text><text class="tl tc" x="292" y="154">h = 0</text></svg><figcaption>The town graph again, with the straight-line distance h from each town to G written beside it. These are the h-values A* uses.</figcaption></figure>
:::

Every h is less than or equal to the real road distance to G (for example, from D the shortest road to G is 9 km and h is 6), which is what makes the hints trustworthy.

:::eg A* on the town graph
Use the A* algorithm to find the shortest path from A to G in the town graph, using the straight-line distances as h. List the order in which the vertices are expanded. [6 marks]

In the table, each open-list entry is written `node g+h=f`, for example `B 5+8=13`. The open list is shown after each step, sorted by f.

| Step | Expand | Open list after the step (node: g + h = f) | Closed list |
|---|---|---|---|
| 0 |  | A 0+11=11 | empty |
| 1 | A | D 6+6=12; B 5+8=13; C 9+7=16 | A |
| 2 | D | B 5+8=13; E 10+4=14; C 9+7=16; F 14+3=17 | A D |
| 3 | B | E 10+4=14; C 9+7=16; F 14+3=17 | A D B |
| 4 | E | G 15+0=15; C 9+7=16; F 14+3=17 | A D B E |
| 5 | G | C 9+7=16; F 14+3=17 | A D B E G |

The reasoning:

- Step 0: A goes in the open list with \(g = 0\), \(h = 11\), so \(f = 11\). [B1]
- Step 1: expand A (the only one). Its neighbours: B \(g = 5\), \(f = 5 + 8 = 13\); C \(g = 9\), \(f = 9 + 7 = 16\); D \(g = 6\), \(f = 6 + 6 = 12\). [B1]
- Step 2: the lowest f is D (12), so expand D. E gets \(g = 6 + 4 = 10\), \(f = 10 + 4 = 14\); F gets \(g = 6 + 8 = 14\), \(f = 14 + 3 = 17\). B is already open with \(g = 5\); going through D would give \(6 + 3 = 9\), which is not smaller, so B is unchanged. C through D gives \(6 + 9 = 15\), not smaller than 9. [B1]
- Step 3: the lowest f is now B (13), so expand B, even though it is not on the final route. Its neighbour E through B would have \(g = 5 + 6 = 11\), which is not smaller than 10, so E is unchanged. [B1]
- Step 4: the lowest f is E (14). G gets \(g = 10 + 5 = 15\), \(f = 15 + 0 = 15\). [B1]
- Step 5: the lowest f is G (15), the destination, so stop. Trace back: G ← E ← D ← A. The order of expansion is **A, D, B, E, G**; the path is A, D, E, G, length 15 km. [B1]
:::

:::warn Do not add h twice
The g of a neighbour is the **g of the expanded vertex plus the edge weight**, never its f. The heuristic is added exactly once, for the neighbour you are looking at. If you expand D (g = 6, h = 6, f = 12) and use f = 12 as the base for E, you get \(12 + 4 + 4\), which counts the estimate for D inside E's cost and is wrong. The correct values are \(g = 6 + 4 = 10\) and \(f = 10 + 4 = 14\).
:::

On the same graph, from A to G, the two algorithms agree on the answer and differ in the effort.

| | Dijkstra's algorithm | A* with straight-line h |
|---|---|---|
| Order in which vertices are chosen | A, B, D, C, E, F, G | A, D, B, E, G |
| Number of vertices chosen | 7 | 5 |
| Vertices never needed | none | C and F |
| Path and length | A, D, E, G; 15 km | A, D, E, G; 15 km |

A* never chose C or F, because their f-values (16 and 17) stayed larger than G's 15. The hint told it that those towns were not worth exploring. This is the saving. On a seven-town map it is small; on a map with millions of junctions it is the difference between an instant answer and a long wait.

Use the widget to run both algorithms yourself, step by step. Choose Dijkstra and A* in turn on the town graph with the same start and destination, press Next until the end, and compare the "vertices chosen" counts. Then change the graph to the grid and the start and destination, and watch the difference grow.

:::html
<div class="widget" data-w="cs-path" data-graph="town" data-algo="astar" data-from="A" data-to="G"></div>
:::

### Why A* can be more efficient

Dijkstra's algorithm explores in every direction at once, in circles around the start, so it visits every vertex closer than the destination, including those on the far side. A* is pulled towards the destination by the heuristic, so it visits fewer vertices that do not lie on the way. The better the heuristic, the more it saves.

The guarantee matters too. A* finds a shortest path as long as the heuristic **never overestimates** the real remaining cost. Such a heuristic is called *admissible*. Straight-line distance and Manhattan distance on a grid never overestimate, because no route is shorter than a straight line or a path that ignores walls. A heuristic that sometimes guesses too high can trick A* into giving up on the true shortest path, as the stretch question shows. You do not need the word "admissible" in the exam, but you do need to know that a poor heuristic can give a poor answer.

## A* on a grid

Many game levels and robot floors are grids of squares. Each square is a vertex, and each move to a neighbouring square (up, down, left or right) is an edge with weight 1. Walls are squares that cannot be entered, so they are simply not vertices.

:::def Manhattan distance
On a grid, the distance between two squares counted as the number of columns apart plus the number of rows apart, moving only up, down, left and right. It is named after the street grid of Manhattan.
:::

Name squares by column letter and row number. The Manhattan distance from C2 to F5 is \(3 + 3 = 6\): three columns across (C to F) and three rows down (2 to 5). With walls in the way the real distance can be longer, but never shorter, so Manhattan distance is a safe heuristic.

:::eg A* on a grid
A game character stands on A1 of a grid with 6 columns (A to F) and 5 rows (1 to 5). The squares B1, B2, B3, B4, D5 and F4 are walls. The character may move up, down, left or right into a square that is not a wall, and each move costs 1. Use A* with Manhattan distance to F5 as the heuristic to find the shortest path from A1 to F5. If two squares tie on f, take the one that comes first alphabetically (A1, A2, …, B1, B2, …). [6 marks]

The start A1 has \(h = 5 + 4 = 9\): the goal F5 is five columns across (A to F) and four rows down (1 to 5). Each row of the table gives the square that was expanded and what it added to the open list.

| Step | Expand | g | h | f | Added to or updated in the open list (node: g + h = f) |
|---|---|---|---|---|---|
| 0 | | | | | A1 0+9=9 |
| 1 | A1 | 0 | 9 | 9 | A2 1+8=9 |
| 2 | A2 | 1 | 8 | 9 | A3 2+7=9 |
| 3 | A3 | 2 | 7 | 9 | A4 3+6=9 |
| 4 | A4 | 3 | 6 | 9 | A5 4+5=9 |
| 5 | A5 | 4 | 5 | 9 | B5 5+4=9 |
| 6 | B5 | 5 | 4 | 9 | C5 6+3=9 |
| 7 | C5 | 6 | 3 | 9 | C4 7+4=11 |
| 8 | C4 | 7 | 4 | 11 | D4 8+3=11; C3 8+5=13 |
| 9 | D4 | 8 | 3 | 11 | E4 9+2=11; D3 9+4=13 |
| 10 | E4 | 9 | 2 | 11 | E5 10+1=11; E3 10+3=13 |
| 11 | E5 | 10 | 1 | 11 | F5 11+0=11 |
| 12 | F5 | 11 | 0 | 11 | none |

- The wall B1 to B4 blocks the direct way across, so the f-values stay at 9 while A* walks down column A, where each step is both closer to the goal and cheaper. [B1]
- At A5 the way forward is B5 (f = 9) and then C5 (f = 9); every step still has \(g + h = 9\). [B1]
- At C5 the wall D5 blocks the route. The only neighbour that is not a wall or closed is C4, with \(g = 7\) and \(h = 4\) (the Manhattan distance from C4 to F5 is \(3 + 1\)), so \(f = 11\). The estimate has risen from 9 to 11 because the wall forced a detour of two extra moves. [B1]
- From C4 the path goes D4, E4, E5, each with \(f = 11\), because from here the Manhattan distance is exact. [B1]
- F5 is expanded at step 12, so the algorithm stops. Trace back: F5, E5, E4, D4, C4, C5, B5, A5, A4, A3, A2, A1. [B1]
- The path has 11 moves, so its cost is 11. [B1]
:::

:::html
<figure class="fig small"><svg viewBox="0 0 278 236" role="img" aria-label="A grid of 6 columns A to F and 5 rows 1 to 5. Solid cells are walls: B1, B2, B3, B4, D5 and F4. Twelve cells hold the order number in which A star expanded them, from 1 at A1 to 12 at F5, and all twelve are on the shortest path. Nine more cells carry a dot: Dijkstra's algorithm expanded them but A star did not. The shortest path goes down column A to A5, along row 5 to C5, up to C4, along row 4 to E4, then down to E5 and along to F5."><text class="tl tc ts" x="46" y="16">A</text><text class="tl tc ts" x="86" y="16">B</text><text class="tl tc ts" x="126" y="16">C</text><text class="tl tc ts" x="166" y="16">D</text><text class="tl tc ts" x="206" y="16">E</text><text class="tl tc ts" x="246" y="16">F</text><text class="tl tc ts" x="14" y="48">1</text><text class="tl tc ts" x="14" y="88">2</text><text class="tl tc ts" x="14" y="128">3</text><text class="tl tc ts" x="14" y="168">4</text><text class="tl tc ts" x="14" y="208">5</text><rect class="f1 s-acc sw2" x="26" y="24" width="40" height="40"/><text class="tl tc tb" x="46" y="48">S 1</text><rect class="fi s-acc sw2" x="66" y="24" width="40" height="40"/><rect class="fm s-acc sw2" x="106" y="24" width="40" height="40"/><text class="tl tc" x="126" y="48">·</text><rect class="fm s-acc sw2" x="146" y="24" width="40" height="40"/><text class="tl tc" x="166" y="48">·</text><rect class="fp s-acc sw2" x="186" y="24" width="40" height="40"/><rect class="fp s-acc sw2" x="226" y="24" width="40" height="40"/><rect class="f1 s-acc sw2" x="26" y="64" width="40" height="40"/><text class="tl tc tb" x="46" y="88">2</text><rect class="fi s-acc sw2" x="66" y="64" width="40" height="40"/><rect class="fm s-acc sw2" x="106" y="64" width="40" height="40"/><text class="tl tc" x="126" y="88">·</text><rect class="fm s-acc sw2" x="146" y="64" width="40" height="40"/><text class="tl tc" x="166" y="88">·</text><rect class="fm s-acc sw2" x="186" y="64" width="40" height="40"/><text class="tl tc" x="206" y="88">·</text><rect class="fp s-acc sw2" x="226" y="64" width="40" height="40"/><rect class="f1 s-acc sw2" x="26" y="104" width="40" height="40"/><text class="tl tc tb" x="46" y="128">3</text><rect class="fi s-acc sw2" x="66" y="104" width="40" height="40"/><rect class="fm s-acc sw2" x="106" y="104" width="40" height="40"/><text class="tl tc" x="126" y="128">·</text><rect class="fm s-acc sw2" x="146" y="104" width="40" height="40"/><text class="tl tc" x="166" y="128">·</text><rect class="fm s-acc sw2" x="186" y="104" width="40" height="40"/><text class="tl tc" x="206" y="128">·</text><rect class="fm s-acc sw2" x="226" y="104" width="40" height="40"/><text class="tl tc" x="246" y="128">·</text><rect class="f1 s-acc sw2" x="26" y="144" width="40" height="40"/><text class="tl tc tb" x="46" y="168">4</text><rect class="fi s-acc sw2" x="66" y="144" width="40" height="40"/><rect class="f1 s-acc sw2" x="106" y="144" width="40" height="40"/><text class="tl tc tb" x="126" y="168">8</text><rect class="f1 s-acc sw2" x="146" y="144" width="40" height="40"/><text class="tl tc tb" x="166" y="168">9</text><rect class="f1 s-acc sw2" x="186" y="144" width="40" height="40"/><text class="tl tc tb" x="206" y="168">10</text><rect class="fi s-acc sw2" x="226" y="144" width="40" height="40"/><rect class="f1 s-acc sw2" x="26" y="184" width="40" height="40"/><text class="tl tc tb" x="46" y="208">5</text><rect class="f1 s-acc sw2" x="66" y="184" width="40" height="40"/><text class="tl tc tb" x="86" y="208">6</text><rect class="f1 s-acc sw2" x="106" y="184" width="40" height="40"/><text class="tl tc tb" x="126" y="208">7</text><rect class="fi s-acc sw2" x="146" y="184" width="40" height="40"/><rect class="f1 s-acc sw2" x="186" y="184" width="40" height="40"/><text class="tl tc tb" x="206" y="208">11</text><rect class="f1 s-acc sw2" x="226" y="184" width="40" height="40"/><text class="tl tc tb" x="246" y="208">G 12</text></svg><figcaption>A* on the grid from the start A1 (S) to the goal F5 (G). Solid cells are walls. The numbers give the order in which A* expanded each cell, and all 12 lie on the shortest path (11 moves). A dot marks a cell that Dijkstra's algorithm expanded but A* did not (9 cells). Blank cells were expanded by neither.</figcaption></figure>
:::

Dijkstra's algorithm on this grid expands 21 of the 24 open squares before it reaches F5, because with every edge costing 1 it spreads out like a flood. A* expands 12, and every one of them is on the shortest path. In the figure, the numbered squares are the 12 that A* expanded and the dotted squares are the 9 extra squares that Dijkstra's algorithm expanded.

:::note Diagonal moves
Some games let the character move diagonally. Then the Manhattan distance would overestimate, so a different heuristic is used. In this chapter, and in the questions on this topic, moves are up, down, left and right only.
:::

## Choosing between them

| | Dijkstra's algorithm | A* algorithm |
|---|---|---|
| Needs a heuristic? | No | Yes, a good estimate of the distance to the destination |
| Chooses next | the unvisited vertex with the smallest distance from the start | the open vertex with the smallest \(f = g + h\) |
| Searches | outwards in all directions | towards the destination |
| Vertices visited | usually more | usually fewer, if the heuristic is good |
| Finds the shortest path? | Yes | Yes, if h never overestimates |
| Best when | there is no useful estimate, or the distances to *all* vertices are wanted | there is one destination and a good estimate (maps, game levels) |

:::exam How to write Dijkstra and A* answers
- Always lay out a table with one column per vertex (Dijkstra) or an open and a closed list (A*), and show the working in it. A marker gives a mark for each correct step, so a table with one wrong cell early on can still earn the later marks if your method is right.
- State your tie rule in a few words ("ties broken alphabetically") if you meet one.
- Keep the **previous vertex** next to every distance. You need it to trace the path.
- Check your answer by adding the weights along your path. That total must equal the destination's final distance.
- Write the path forwards, from start to destination, even though you traced it backwards.
- Do not stop early: Dijkstra's ends when the destination is *chosen*, and A* ends when the destination is *expanded*.
- For "explain why A* is more efficient": a heuristic gives the direction to the destination, so fewer vertices are visited. Both halves earn a mark.
:::

:::eg Spot the error: Dijkstra's algorithm on the town graph
Question: Use Dijkstra's algorithm to find the shortest path from A to G in the town graph. [4 marks]

A student's final answer was:

| Node | Shortest distance | Previous node |
|---|---|---|
| A | 0 | none |
| B | 5 | A |
| C | 9 | A |
| D | 6 | A |
| E | 11 | B |
| F | 14 | D |
| G | 16 | E |

"The shortest path is A, B, E, G with length 16."

The first row and the distances of B, C and D are correct (A, then A's three neighbours) [B1]. The order of choosing the vertices is correct: A, then B (5), then D (6) [B1]. **E's distance should have changed to 10 with previous vertex D when D was visited, because \(6 + 4 = 10 < 11\). The student never updated E, so E stays 11 via B** [B0]. As a result G is 16 and the path A, B, E, G is not the shortest, so the final answer is wrong [B0]. The answer scores 2 out of 4.

The correct path is A, D, E, G with length 15. The slip is the one the second warning describes: a neighbour's distance must be compared again every time one of its neighbours is visited, and replaced when the new route is shorter.
:::

:::try Start easy, finish at exam standard
Q: A graph has vertices W, X, Y and Z and edges W–X, W–Y, X–Y and Y–Z. (a) How many vertices and how many edges does it have? (b) Which vertices are the neighbours of Y? (c) Is the graph weighted?
A: (a) 4 vertices and 4 edges. (b) W, X and Z: each is joined to Y by an edge. (c) No: no edge has a number, so it is not weighted.
Q: This adjacency matrix has rows and columns in the order A, B, C, D: row A is 0 3 0 2; row B is 3 0 4 0; row C is 0 4 0 6; row D is 2 0 6 0. (a) Write the adjacency list. (b) What is the cost of the path A, B, C, D? (c) Is the graph directed?
A: (a) A: B (3), D (2). B: A (3), C (4). C: B (4), D (6). D: A (2), C (6). (b) \(3 + 4 + 6 = 13\). (c) No: the matrix is symmetrical, so every edge works in both directions.
Q: On a grid, find the Manhattan distance (a) from C2 to F5, and (b) from D4 to B1.
A: (a) Three columns (C to F) and three rows (2 to 5): \(3 + 3 = 6\). (b) Two columns (D to B) and three rows (4 to 1): \(2 + 3 = 5\).
Q: In an A* search, vertex K has \(g = 7\) and \(h = 5\), and vertex M has \(g = 9\) and \(h = 2\). Work out each f-cost and say which vertex is expanded first.
A: K: \(f = 7 + 5 = 12\). M: \(f = 9 + 2 = 11\). M has the lower f-cost, so M is expanded first, even though its g is larger.
Q: The graph has edges V–W 4, V–X 1, X–W 2, W–Y 5, X–Y 8, Y–Z 3 and W–Z 9. Use Dijkstra's algorithm to find the shortest path from V to Z and its length.
A: Show the table, then trace back.

| Step | Visit | V | W | X | Y | Z |
|---|---|---|---|---|---|---|
| 0 |  | 0 | ∞ | ∞ | ∞ | ∞ |
| 1 | V |  | 4 V | 1 V |  |  |
| 2 | X |  | 3 X |  | 9 X |  |
| 3 | W |  |  |  | 8 W | 12 W |
| 4 | Y |  |  |  |  | 11 Y |
| 5 | Z |  |  |  |  |  |

Trace back from Z: Z ← Y ← W ← X ← V. The shortest path is V, X, W, Y, Z with length \(1 + 2 + 5 + 3 = 11\).
Q: Edges are directed: M to N costs 5, N to M costs 8, N to O costs 2, and O to M costs 1. What is the cheapest cost from M to O, and from O to M?
A: From M the only edge goes to N (5), then N to O (2): \(5 + 2 = 7\). From O there is one edge, directly to M: cost 1. The costs differ because the edges are directed.
Q: The final table of a Dijkstra search from A is: A 0, none; B 4, A; C 7, B; D 5, A; E 9, D; F 12, E. Write the shortest path from A to F, and its length.
A: Follow the previous column from F: F ← E ← D ← A. Reversed, the path is A, D, E, F, with length 12 (the distance of F).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A metro company in Santiago wants a program that finds the quickest route between two stations. Describe how a graph could represent the metro network.
A: One mark for each of three points:

- each station is a vertex (node) [B1]
- each section of track joining two stations is an edge [B1]
- the weight of an edge is the journey time (or distance) between the two stations [B1]

(Accept distance, time or cost as the weight. Do not accept "the graph shows the stations" without saying what the edges are.)

Q: [2 marks] ★ Explain why the A* algorithm may be more efficient than Dijkstra's algorithm.
A: Two points:

- A* uses a heuristic (an estimate of the cost from each vertex to the destination) to choose which vertex to expand next [B1]
- so it moves towards the destination and visits fewer vertices than Dijkstra's algorithm, which searches in every direction [B1]

Q: [3 marks] ★ A graph of five vertices A to E is stored in this adjacency matrix. The rows and columns are in the order A, B, C, D, E: row A is 0 6 0 0 3; row B is 6 0 2 0 0; row C is 0 2 0 7 0; row D is 0 0 7 0 5; row E is 3 0 0 5 0. (a) State what a 0 in the matrix shows. [1] (b) State how the matrix shows that the graph is undirected. [1] (c) State the cost of the path A, B, C, D. [1]
A: (a) There is no edge between those two vertices [B1]. (b) The matrix is symmetrical: the entry for row X, column Y equals the entry for row Y, column X [B1]. (c) \(6 + 2 + 7 = 15\) [B1].

Q: [6 marks] ★★ The diagram shows a network of six depots, P to U, with the distances between them in kilometres. Use Dijkstra's algorithm to find the shortest route from P to U. Show your working in a table, state the route and give its length. If two vertices have the same distance, take the one that comes first alphabetically.

:::html
<figure class="fig small"><svg viewBox="0 0 356 226" role="img" aria-label="A weighted graph of six depots P to U with road lengths in kilometres: P to Q 5, P to R 8, P to S 9, Q to S 5, Q to T 6, R to S 5, R to U 9, S to T 8, S to U 9, T to U 5."><line class="ln" x1="43" y1="99" x2="124" y2="183"/><line class="ln" x1="43" y1="99" x2="151" y2="43"/><line class="ln" x1="43" y1="99" x2="205" y2="127"/><line class="ln" x1="124" y1="183" x2="205" y2="127"/><line class="ln" x1="124" y1="183" x2="286" y2="183"/><line class="ln" x1="151" y1="43" x2="205" y2="127"/><line class="ln" x1="151" y1="43" x2="313" y2="71"/><line class="ln" x1="205" y1="127" x2="286" y2="183"/><line class="ln" x1="205" y1="127" x2="313" y2="71"/><line class="ln" x1="286" y1="183" x2="313" y2="71"/><text class="tl tc halo" x="84" y="145">5</text><text class="tl tc halo" x="97" y="75">8</text><text class="tl tc halo" x="124" y="117">9</text><text class="tl tc halo" x="164" y="159">5</text><text class="tl tc halo" x="205" y="187">6</text><text class="tl tc halo" x="178" y="89">5</text><text class="tl tc halo" x="232" y="61">9</text><text class="tl tc halo" x="246" y="159">8</text><text class="tl tc halo" x="259" y="103">9</text><text class="tl tc halo" x="300" y="131">5</text><circle class="f1 s-acc sw2" cx="43" cy="99" r="17"/><text class="tl tc tb" x="43" y="104">P</text><circle class="f1 s-acc sw2" cx="124" cy="183" r="17"/><text class="tl tc tb" x="124" y="188">Q</text><circle class="f1 s-acc sw2" cx="151" cy="43" r="17"/><text class="tl tc tb" x="151" y="48">R</text><circle class="f1 s-acc sw2" cx="205" cy="127" r="17"/><text class="tl tc tb" x="205" y="132">S</text><circle class="f1 s-acc sw2" cx="286" cy="183" r="17"/><text class="tl tc tb" x="286" y="188">T</text><circle class="f1 s-acc sw2" cx="313" cy="71" r="17"/><text class="tl tc tb" x="313" y="76">U</text></svg><figcaption>The depot network for exam practice question 4. The numbers are distances in kilometres.</figcaption></figure>
:::

H: Start with P = 0 and everything else ∞, then always visit the unvisited depot with the smallest distance.
H: When a visited depot gives a neighbour an equal distance, do not change anything.
A: One possible table:

| Step | Visit | P | Q | R | S | T | U |
|---|---|---|---|---|---|---|---|
| 0 |  | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | P |  | 5 P | 8 P | 9 P |  |  |
| 2 | Q |  |  |  |  | 11 Q |  |
| 3 | R |  |  |  |  |  | 17 R |
| 4 | S |  |  |  |  |  |  |
| 5 | T |  |  |  |  |  | 16 T |
| 6 | U |  |  |  |  |  |  |

- P = 0 and the others ∞; P visited, giving Q 5, R 8, S 9 [B1]
- Q visited (5): T gets 11 via Q; S is not improved (5 + 5 = 10 is larger than 9) [B1]
- R visited (8): U gets 17 via R [B1]
- S visited (9): no improvement (T would be 17, U would be 18) [B1]
- T visited (11): U is improved to 16 via T [B1]
- route P, Q, T, U with length 16 km [B1]

Q: [6 marks] ★★ The diagram shows six nodes, H to N, with edge weights. The table gives the heuristic h, the estimated distance from each node to N. Use the A* algorithm from H to N. (a) List, in order, the nodes that are expanded. [3] (b) State the path found and its length. [1] (c) N is first added to the open list with one g-value and later given a different one. State both values and explain the change. [2] If two nodes have the same f-value, take the one that comes first alphabetically.

| Node | H | J | K | L | M | N |
|---|---|---|---|---|---|---|
| h | 10 | 8 | 6 | 4 | 4 | 0 |

:::html
<figure class="fig small"><svg viewBox="0 0 356 226" role="img" aria-label="A weighted graph of six nodes H to N with edge weights: H to J 7, H to K 5, H to L 8, J to L 8, J to M 6, K to L 5, K to N 9, L to M 4, L to N 5, M to N 8."><line class="ln" x1="43" y1="99" x2="124" y2="183"/><line class="ln" x1="43" y1="99" x2="151" y2="43"/><line class="ln" x1="43" y1="99" x2="205" y2="127"/><line class="ln" x1="124" y1="183" x2="205" y2="127"/><line class="ln" x1="124" y1="183" x2="286" y2="183"/><line class="ln" x1="151" y1="43" x2="205" y2="127"/><line class="ln" x1="151" y1="43" x2="313" y2="71"/><line class="ln" x1="205" y1="127" x2="286" y2="183"/><line class="ln" x1="205" y1="127" x2="313" y2="71"/><line class="ln" x1="286" y1="183" x2="313" y2="71"/><text class="tl tc halo" x="84" y="145">7</text><text class="tl tc halo" x="97" y="75">5</text><text class="tl tc halo" x="124" y="117">8</text><text class="tl tc halo" x="164" y="159">8</text><text class="tl tc halo" x="205" y="187">6</text><text class="tl tc halo" x="178" y="89">5</text><text class="tl tc halo" x="232" y="61">9</text><text class="tl tc halo" x="246" y="159">4</text><text class="tl tc halo" x="259" y="103">5</text><text class="tl tc halo" x="300" y="131">8</text><circle class="f1 s-acc sw2" cx="43" cy="99" r="17"/><text class="tl tc tb" x="43" y="104">H</text><circle class="f1 s-acc sw2" cx="124" cy="183" r="17"/><text class="tl tc tb" x="124" y="188">J</text><circle class="f1 s-acc sw2" cx="151" cy="43" r="17"/><text class="tl tc tb" x="151" y="48">K</text><circle class="f1 s-acc sw2" cx="205" cy="127" r="17"/><text class="tl tc tb" x="205" y="132">L</text><circle class="f1 s-acc sw2" cx="286" cy="183" r="17"/><text class="tl tc tb" x="286" y="188">M</text><circle class="f1 s-acc sw2" cx="313" cy="71" r="17"/><text class="tl tc tb" x="313" y="76">N</text></svg><figcaption>The graph for exam practice question 5. The heuristic values h are in the table above the figure.</figcaption></figure>
:::

H: Write the open list after every expansion, sorted by f.
H: When L is expanded, compare the new g of N with the one it already has.
A: The open list after each step:

| Step | Expand | Open list after the step (node: g + h = f) | Closed list |
|---|---|---|---|
| 0 |  | H 0+10=10 | empty |
| 1 | H | K 5+6=11; L 8+4=12; J 7+8=15 | H |
| 2 | K | L 8+4=12; N 14+0=14; J 7+8=15 | H K |
| 3 | L | N 13+0=13; J 7+8=15; M 12+4=16 | H K L |
| 4 | N | J 7+8=15; M 12+4=16 | H K L N |

(a) The order is H, K, L, N. H is expanded first, then K (f = 11, the lowest), then L (f = 12), then N (f = 13, lower than J's 15 and M's 16) [B1] [B1] [B1].

(b) The path is H, L, N with length \(8 + 5 = 13\) [B1].

(c) N first gets \(g = 14\), found through K (\(5 + 9 = 14\)) [B1]. When L is expanded, the route through L gives \(g = 8 + 5 = 13\), which is smaller, so N's g and previous node are replaced [B1].

Q: [5 marks] ★★ A game uses a grid of 5 columns (A to E) and 4 rows (1 to 4). The squares A3, B1, C3 and D2 are walls. A character moves up, down, left or right, each move costing 1, from A1 to E4. The A* algorithm uses the Manhattan distance to E4 as h. If two squares have the same f, take the one that comes first alphabetically (A1, A2, …, B1, …).

```text
     A  B  C  D  E
 1   S  #  .  .  .
 2   .  .  .  #  .
 3   #  .  #  .  .
 4   .  .  .  .  G
```

(a) State the value of h for A1. [1] (b) List the first six squares that are expanded, in order. [3] (c) State the number of moves in the shortest path. [1]
H: The Manhattan distance counts columns across plus rows down.
H: At the start the f-value is the same for several squares, so the alphabetical rule decides.
A: (a) A1 is 4 columns from E and 3 rows from 4, so \(h = 4 + 3 = 7\) [B1].

(b) The first six squares expanded are A1, A2, B2, B3, B4, C2.

- A1, A2 and B2 are expanded first, each with f = 7 [B1]
- B3 and C2 both have f = 7 after B2; B3 comes first alphabetically, and then B4 (also f = 7) comes before C2 [B1]
- C2 is the sixth square expanded [B1]

(c) The shortest path is A1, A2, B2, B3, B4, C4, D4, E4, which is 7 moves [B1].

Q: [4 marks] ★★★ A delivery company runs a drone that flies between landing pads, each pad joined to several others by flight routes with known lengths. Each request gives one pickup pad and one destination pad, and the straight-line distance from any pad to any other is available. Justify the use of the A* algorithm rather than Dijkstra's algorithm for this system.
H: Think about what A* needs, and what it saves.
A: Four points, each linked to the scenario:

- each request has only one destination, so the system does not need the shortest distances to all the pads, which is all that Dijkstra's extra work provides [B1]
- the straight-line distance between any two pads is known, so it can be used as the heuristic h [B1]
- a straight line can never be longer than the flight route, so h never overestimates and A* still finds the shortest route [B1]
- A* expands fewer pads than Dijkstra, so a route is found faster and requests are answered quickly [B1]

Q: [5 marks] ★★★ Describe how Dijkstra's algorithm finds the shortest path between two vertices of a weighted graph. Any five points.
H: Think of the table: the starting values, the repeated step, what is updated, when it stops, and how the path is read.
A: One mark for each of five points:

- the start vertex is given a distance of 0 and every other vertex a distance of ∞ (unknown) [B1]
- the unvisited vertex with the smallest distance is chosen and marked visited [B1]
- for each unvisited neighbour of the chosen vertex, the chosen vertex's distance plus the edge weight is calculated, and if it is smaller than the neighbour's current distance, the distance is replaced and the neighbour's previous vertex is set to the chosen vertex [B1]
- the choosing and updating repeat until the destination is the vertex chosen (visited) [B1]
- the path is found by following the previous vertices back from the destination to the start [B1]

(Replacing the distance and recording the previous vertex may be marked as two separate points, with the other points merged. Any five of the points earn the marks.)
:::

:::try Stretch for A*
Q: [5 marks] ★★★ Run A* from S to G on this graph: S–A 1, A–G 6, S–B 4, B–G 4. The heuristic values are h(S) = 6, h(A) = 20, h(B) = 4 and h(G) = 0. (a) List the vertices expanded, in order, and give the path and its length that A* returns. [3] (b) Find the true shortest path from S to G and its length. [1] (c) State which h-value is wrong and what rule it breaks. [1]
H: Write the open list after each step. A's f-value is very large; see what that does.
H: For (c), the real distance from A to G is 6.
A: (a) Expand S, which adds A (\(1 + 20 = 21\)) and B (\(4 + 4 = 8\)). Expand B (8), which adds G (\(g = 8\), \(f = 8\)). Expand G (8) and stop. The order is S, B, G and the path is S, B, G with length 8 [B1] [B1] [B1].

| Step | Expand | Open list after the step (node: g + h = f) | Closed list |
|---|---|---|---|
| 0 |  | S 0+6=6 | empty |
| 1 | S | B 4+4=8; A 1+20=21 | S |
| 2 | B | G 8+0=8; A 1+20=21 | S B |
| 3 | G | A 1+20=21 | S B G |

(b) The shortest path is S, A, G with length \(1 + 6 = 7\) [B1].

(c) h(A) = 20 is wrong: the real distance from A to G is 6, so the heuristic overestimates. A heuristic must never be larger than the true remaining cost; this one made A* ignore A, and it returned a path that is not the shortest [B1].

Q: [5 marks] ★★★ A courier's one-way streets form a directed graph with these edges (from, to, cost in minutes): S to A 2, A to B 3, B to S 1, S to B 9, B to T 4 and A to T 8. (a) Find the cheapest route from S to T and its cost. [2] (b) Find the cheapest cost from B to A. [2] (c) Explain why there is no route from T to S. [1]
H: Only follow an edge in the direction of its arrow.
H: For (b), the only edge leaving B that leads back is B to S.
A: (a) S, A, B, T costs \(2 + 3 + 4 = 9\); the alternatives cost more (S, B, T costs \(9 + 4 = 13\); S, A, T costs \(2 + 8 = 10\)) [B1]. The cheapest route is S, A, B, T with cost 9 [B1].

(b) From B the only way on that does not end at T is B to S (1), then S to A (2): cost \(1 + 2 = 3\) [B1] [B1].

(c) No edge leaves T, so once you are at T you cannot move anywhere [B1].
:::

:::quiz
? Which statement describes a weighted graph?
- Every vertex has the same number of edges.
- Every edge can be followed in one direction only.
+ Every edge has a number, such as a distance or a time, attached.
- Every vertex has a number attached.
> The weights are on the edges, and they are the costs a path adds up. One-way edges describe a directed graph, which is a different property.
? When does Dijkstra's algorithm stop?
- As soon as the destination is given a distance.
+ When the destination is chosen as the unvisited vertex with the smallest distance.
- When every edge has been used once.
- When the start vertex has been visited twice.
> A distance given to the destination early can still be improved. The distance is final only once the destination has the smallest distance among the unvisited vertices and is chosen.
? In A*, a vertex has \(g = 9\) and \(h = 4\). What is its f-cost?
- 5
- 9
+ 13
- 36
> \(f = g + h = 9 + 4 = 13\). 5 is the difference \(g - h\), 9 forgets h, and 36 multiplies instead of adding.
? What is the Manhattan distance between squares D2 and A4 on a grid?
- 3
- 6
+ 5
- 2
> Three columns (D to A) and two rows (2 to 4): \(3 + 2 = 5\). Answers 3 and 2 count only one direction, and 6 multiplies the two distances.
? What happens to A* if every vertex has h = 0?
- It never finds the destination.
+ It behaves exactly like Dijkstra's algorithm.
- It finds a longer path than Dijkstra's algorithm.
- It visits fewer vertices than before.
> With h = 0, \(f = g + 0 = g\), so A* always chooses the smallest g, which is Dijkstra's rule. It loses its sense of direction but still finds the shortest path.
? The adjacency matrix of an undirected graph is always...
- full of non-zero numbers.
- zero on every row.
+ symmetrical: the entry for row X, column Y equals the entry for row Y, column X.
- zero only on the main diagonal and nowhere else.
> An undirected edge from X to Y is also an edge from Y to X, so both entries hold the same weight. A matrix that is not symmetrical describes a directed graph.
? What is the previous-vertex column of a Dijkstra table used for?
- To record the order in which vertices were visited.
- To store the heuristic of each vertex.
+ To trace the shortest path back from the destination to the start.
- To show which edges were never used.
> Following the previous vertices from the destination back to the start gives the shortest path in reverse, which you then write forwards. The visit order is a different column.
? Why can A* return a path that is not the shortest?
- It never checks the weights of the edges.
- It stops after expanding five vertices.
+ The heuristic overestimates the cost from some vertex to the destination.
- The closed list contains the start vertex.
> A* trusts h. If h is larger than the true remaining cost, a vertex on the best path can get a large f-value and be ignored. The stretch question shows this with h(A) = 20.
:::

:::checklist What you can now do
- [ ] I can explain the purpose of a graph and use the terms vertex (node), edge, weight, path, cost, neighbour, directed and undirected.
- [ ] I can describe how a graph can model a road map, a game level, a puzzle or a robot's world.
- [ ] I can read an adjacency matrix and an adjacency list and say what they show.
- [ ] I can apply Dijkstra's algorithm by hand with a table of distances and previous vertices, and write the shortest path and its cost.
- [ ] I can state when Dijkstra's algorithm stops and why a destination's first distance may not be final.
- [ ] I can define a heuristic and the g-cost, h-cost and f-cost, and use \(f = g + h\).
- [ ] I can apply the A* algorithm by hand with an open list and a closed list and say the order in which vertices are expanded.
- [ ] I can find the Manhattan distance on a grid and use it as the heuristic.
- [ ] I can explain why A* may be more efficient than Dijkstra's algorithm, and when a heuristic can fail.
:::

:::recap
- A graph is a set of vertices (nodes) joined by edges. A weighted graph has a cost on every edge; a directed graph has one-way edges. The cost of a path is the sum of its edge weights.
- Graphs model road maps, game levels (grids), puzzle states and robot worlds. A graph is stored as an adjacency matrix (symmetrical for an undirected graph) or an adjacency list.
- Dijkstra's algorithm: start 0, others ∞; repeatedly visit the unvisited vertex with the smallest distance and improve its neighbours' distances and previous vertices; stop when the destination is chosen; read the path back with the previous column.
- A destination's first distance may not be final; an equal new distance changes nothing.
- A*: expand the open vertex with the lowest \(f = g + h\). g is the cost so far, h is the heuristic estimate to the destination; it uses an open list and a closed list; it stops when the destination is expanded.
- Dijkstra is A* with h = 0. A* usually visits fewer vertices because the heuristic points it at the destination; it finds the shortest path when h never overestimates.
- Manhattan distance is columns apart plus rows apart; straight-line distance is the usual heuristic on maps.
:::

:::links
- practise: [AI: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/18-artificial-intelligence-ai-/artificial-intelligence-ai/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- explore: [Shortest paths animated](https://visualgo.net/en/sssp) · VisuAlgo · watch Dijkstra's algorithm choose vertices one at a time
- explore: [Dijkstra worked through](https://www.101computing.net/dijkstras-shortest-path-algorithm/) · 101 Computing · step through Dijkstra's algorithm on a graph
- explore: [A* worked through](https://www.101computing.net/a-star-search-algorithm/) · 101 Computing · A* on a grid, step by step
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists, including searching and routes
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste the program from this chapter and watch the search run

Links checked 13 November 2026.
:::

Next: [Machine learning and neural networks](#cs.ml)
