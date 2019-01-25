# DSNA (Data Structures 'N' Algorithms)

My practices of Data Structures and Algorithms using several languages
(just for fun) in the long run.

> The Big O describes how much an algorithm slows down as the input grows.

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

It iterates through your whole array comparing adjacents pair of elements to
move all the bigger elements to the right side and leave the remaining elements
in the left side. This same process is repeatedly made until the list is fully sorted.

#### Time complexity

| Average | Worst  |
| ------- | ------ |
| O(n^2)  | O(n^2) |

#### Iterative implementations

- Python 3
