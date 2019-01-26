def msi(input_list):
    """
    It breaks down the list into n sublits, each containing one element. Then, 
    it repeatdely merges adjacent sublists to produce new sorted sublists 
    until there's only one sublist remaining.
    """
    n = len(input_list)
    size = 1

    while size <= n:
        lo = 0
        while lo < n - size:
            mid = lo + size
            hi = min(lo + 2 * size, n)
            left_side = input_list[lo:mid]
            right_side = input_list[mid:hi]

            i = 0
            j = 0
            k = lo

            while i < len(left_side) and j < len(right_side):
                if left_side[i] < right_side[j]:
                    input_list[k] = left_side[i]
                    i += 1
                    k += 1
                else:
                    input_list[k] = right_side[j]
                    j += 1
                    k += 1

            while i < len(left_side):
                input_list[k] = left_side[i]
                i += 1
                k += 1

            while j < len(right_side):
                input_list[k] = right_side[j]
                j += 1
                k += 1

            lo += 2 * size

        size *= 2
