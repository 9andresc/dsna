# DSNA (Data Structures 'N' Algorithms)

My practices of Data Structures and Algorithms using several languages
(just for fun) in the long run.

> The Big O describes how much an algorithm slows down as the input grows.

## Data Structures

### Binary Search Tree

#### Description

Is a special kind of binary tree in which all nodes are ordered, this means
that every node must be greater than or equal to any node in left sub-tree, and
less than or equal to any node in the right sub-tree.

#### Time complexity in the average case

| Search    | Insertion | Deletion  |
| --------- | --------- | --------- |
| O(log(n)) | O(log(n)) | O(log(n)) |

#### Time complexity in the worst case

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(n)   | O(n)      | O(n)     |

#### Implementations

- Python 3

### Binary Tree

#### Description

It a simple kind of tree in which parent nodes have at most two child nodes,
which are referred to as the left child and the right child. There a few ways
to traverse a tree, the two most general ways are:

- BFS (Breadth-first search): It starts at the tree root and explores all of
  the siblings nodes at the present level prior to moving on to the nodes at the
  next level.

- DFS (Depth-first search): It starts at the tree root and explores as far as
  possible along each branch before backtracking. This method has different
  options to traverse a tree, which are:

  - Pre-order: Check off a node as you see it before you traverse any further
    in the tree.
  - In-order: Check off a node when you've seen its left child and come back to
    it.
  - Post-order: Check off a node after you've seen all its children and come
    back to it.

#### Time complexity

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(n)   | O(log(n)) | O(n)     |

#### Implementations

- Python 3

### Graph

#### Description

Is a set of **vertices** that can contain data, these vertices can be connected
through a series of **edges**, which could hold data as well. Graphs are used to
solve many real-life problems, one of the most common are networks.

Edges can have a **direction**, meaning the relationship between two nodes only
applies one way and not the other. Thus, a **directed graph** is a graph where
its edges have a sense of direction.

Unlike trees, graphs can have **cycles**. A cycle happens when you can start at
one node and follow edges all the way back to that node. Cycles can be harmful
while programming because they can cause infinite loops. One way to avoid cycles
is working with a **directed acyclic graph** (DAG).

A **disconnected graph** has some vertex or group of vertices that is
disconnected from the rest of the graph. Thus, a **connected graph** has no
disconnected vertices.

A directed graph is **weakly connected** when only replacing all of the
directed edges with undirected edges can cause it to be connected.

**Strongly connected** directed graphs must have a path from every node and
every other node. So, there must be a path from A to B and B to A.

There are several ways to represent connections on graphs that only use lists,
those are:

- Edge list: the edges themselves are represented by a list of two elements,
  these elements are normally the IDs of the vertices.
- Adjacency list: the vertices normally have an ID number that corresponds to
  an index in the array, in which each slot is used to store a list of nodes
  that the node with our ID is adjacent to.
- Adjacency matrix: the indices in the outer array and inner arrays represent
  nodes with those IDs. If there's an edge between two nodes, a 1 goes into the
  two slots that intersect the corresponding indices.

#### Time complexity

| Search                 |
| ---------------------- |
| O( \| E \| + \| N \| ) |

#### Implementations

- Python 3

### Hash Table

#### Description

Is a kind of list which stores unordered key/value pairs. To select where to
store each incoming value there's a function called **hash function** which
maps the values with each key. To measure how loaded a Hash Table is, you
should divide the number of possible values by the size of the table, this is
often called the **load factor**. It is possible that some values map to the
same keys twice or more, in that case a **collusion** occurs. To resolve such
collisions there are **rehashing functions**.

#### Time complexity in the average case

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(1)   | O(1)      | O(1)     |

#### Time complexity in the worst case

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(n)   | O(n)      | O(n)     |

#### Implementations

- Python 3

### Heap

#### Description

Is a tree-based data structure which is essentially an almost **complete tree**
that satisfies the **heap property**: if P is a parent node of node N, then the
value of P is either greater than or equal to (in **max heap**) or less than or
equal to (in a **min heap**) the value of N. The heap is a very efficient
implementation of a **priority queue**, and if fact priority queues are often
referred to as "heaps", regardless of how they may be implemented.
In a heap, the highest (or lowest) priority value is always stored at the root.
However, a heap is not a sorted structure; it can be regarded as being
partially ordered. A heap is a useful data structure when it is necessary to
repeatedly remove the node with the highest (or lowest) priority.

#### Time complexity

| Search | Insertion | Deletion  |
| ------ | --------- | --------- |
| O(n)   | O(log(n)) | O(log(n)) |

#### Implementations

- Python 3

### Linked List

#### Description

Is a linear collection of data elements, whose order is not given by their
physical placement in memory. Instead, each element points to the next.

#### Time complexity

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(n)   | O(1)      | O(1)     |

#### Implementations

- Python 3

### Queue

#### Description

Is a collection in which the elements are kept in order and the principal
operations on the collection are the addition of elements to the rear terminal
position, known as **enqueue**, and removal of elements from the front terminal
position, known as **dequeue**.

#### Time complexity

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(n)   | O(1)      | O(1)     |

#### Implementations

- Python 3

### Red-Black Tree

#### Description

It's the most common example of a self-balancing tree, which tries to minimize
the number of levels that it uses, and its nodes might have some additional
properties. A RBT have a few rules to ensure that it never gets too unbalanced,
which are:

- Every node has a property called color which can be either red or black.
- The root node must be black.
- There are no two adjacent red nodes (A red node cannot have a red parent or
  red child).
- Every path from a node to its descendant null nodes must contain the same
  number of black nodes.

It also follows the rules of a Binary Search Tree.

#### Time complexity

| Search    | Insertion | Deletion  |
| --------- | --------- | --------- |
| O(log(n)) | O(log(n)) | O(log(n)) |

#### Implementations

- Python 3

### Stack

#### Description

Is a basic data structure that can be logically thought of as a linear
structure represented by a real physical stack or pile, a structure where
insertion and deletion of items takes place at one end called top of the stack.

#### Time complexity

| Search | Insertion | Deletion |
| ------ | --------- | -------- |
| O(n)   | O(1)      | O(1)     |

#### Implementations

- Python 3

## Algorithms

### Binary Search

#### Description

It halves your **ordered** array and compares your value with the middle
element. If your value is equal to the middle element it returns
**the index of the later**, but if it's less than the middle element, it
should do the same process in the left halve, and if it's greater, it will
search on the right halve. This task will go on until it matches the element
with your value or there are no more halves, in which case, it will return **-1**.

#### Time complexity

| Average      | Worst        |
| ------------ | ------------ |
| O(n\*log(n)) | O(n\*log(n)) |

#### Iterative implementations

- Python 3

#### Recursive implementations

- Python 3

### Bubble Sort

#### Description

It iterates through your whole array comparing adjacent pair of elements to
move all the bigger elements to the right side and leave the remaining elements
in the left side. This same process is repeatedly made until the list is fully sorted.

#### Time complexity

| Average | Worst  |
| ------- | ------ |
| O(n^2)  | O(n^2) |

#### Iterative implementations

- Python 3

#### Recursive implementations

- Python 3

### Merge Sort

#### Description

It breaks down your array into n subarrays, each containing one element. Then, it
repeatedly merges adjacent subarrays to produce new sorted subarrays until there's
only one subarray remaining. This will be your sorted array.

#### Time complexity

| Average      | Worst        |
| ------------ | ------------ |
| O(n\*log(n)) | O(n\*log(n)) |

#### Iterative implementations

- Python 3

#### Recursive implementations

- Python 3

### Quick Sort

#### Description

It chooses the **last element** of your array as a pivot and starts to iterate from
the first element comparing all the elements with the pivot. The ones that are less
than the pivot will be in the left side of the final position of the pivot and the
others that are greater will be in the right side of the pivot. This same process
will happen on the **left** and **right** side until all the elements are in their
final positions.

#### Time complexity

| Average      | Worst  |
| ------------ | ------ |
| O(n\*log(n)) | O(n^2) |

#### Iterative implementations

- Python 3

#### Recursive implementations

- Python 3
