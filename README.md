# DSNA (Data Structures 'N' Algorithms)

My practices of Data Structures and Algorithms using several languages
(just for fun) in the long run.

> The Big O describes how much an algorithm slows down as the input grows.

## Data Structures

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

### Stack

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
