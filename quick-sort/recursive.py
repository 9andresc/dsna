def qsr(items, lo=0, hi=None):
    """It sorts the items using Quick Sort with the Hoare partition algorithm"""
    if hi == None:
        hi = len(items) - 1

    if lo >= hi:
        return

    elem_idx, pivot_idx = lo, hi
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

    qsr(items, lo, pivot_idx - 1)
    qsr(items, pivot_idx + 1, hi)

