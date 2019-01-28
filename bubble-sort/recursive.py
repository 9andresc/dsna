def bsr(items, hi=None):
    """
    Sorts the list comparing adjacent pairs of elements to move all the 
    bigger elements to the right side.
    """

    if hi == None:
        hi = len(items) - 1
    elif hi == 0:
        return

    for i in range(0, hi):
        if items[i] > items[i + 1]:
            items[i], items[i + 1] = items[i + 1], items[i]

    bsr(items, hi - 1)
