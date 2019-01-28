def msi(items):
    """
    It breaks down the list into n sublists, each containing one element. Then, 
    it repeatdely merges adjacent sublists to produce new sorted sublists 
    until there's only one sublist remaining.
    """
    n = len(items)
    size = 1

    while size <= n:
        lo = 0
        while lo < n - size:
            mid = lo + size
            hi = min(lo + 2 * size, n)
            left_side = items[lo:mid]
            right_side = items[mid:hi]

            i = 0
            j = 0
            k = lo

            while i < len(left_side) and j < len(right_side):
                if left_side[i] < right_side[j]:
                    items[k] = left_side[i]
                    i += 1
                else:
                    items[k] = right_side[j]
                    j += 1

                k += 1

            while i < len(left_side):
                items[k] = left_side[i]
                i += 1
                k += 1

            while j < len(right_side):
                items[k] = right_side[j]
                j += 1
                k += 1

            lo += 2 * size

        size *= 2
