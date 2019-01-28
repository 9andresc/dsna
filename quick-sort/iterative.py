class Stack(list):
    push = list.append


def qsi(items):
    """It sorts the items using Quick Sort with the Hoare partition algorithm"""
    n = len(items)

    if n < 2:
        return

    unsorted = Stack([(0, n - 1)])

    while unsorted:
        elem_idx, pivot_idx = left_idx, right_idx = unsorted.pop()
        elem = items[elem_idx]
        pivot = items[pivot_idx]

        while pivot_idx > elem_idx:
            if elem > pivot:
                items[pivot_idx] = elem
                pivot_idx -= 1
                items[elem_idx] = elem = items[pivot_idx]
            else:
                elem_idx += 1
                elem = items[elem_idx]

        items[pivot_idx] = pivot

        left_size = pivot_idx - left_idx
        right_size = right_idx - pivot_idx

        if left_size > 1:
            unsorted.push((left_idx, pivot_idx - 1))

        if right_size > 1:
            unsorted.push((pivot_idx + 1, right_idx))
