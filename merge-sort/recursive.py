def msr(items):
    """
    It breaks down the list into n sublists, each containing one element. Then, 
    it repeatdely merges adjacent sublists to produce new sorted sublists 
    until there's only one sublist remaining.
    """
    if len(items) > 1:
        mid = int(len(items) / 2)
        left_side = items[:mid]
        right_side = items[mid:]

        msr(left_side)
        msr(right_side)

        i = 0
        j = 0
        k = 0

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
