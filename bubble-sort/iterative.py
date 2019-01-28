def bsi(items):
    """
    Sorts the list comparing adjacent pairs of elements to move all the 
    bigger elements to the right side.
    """

    for hi in range(len(items) - 1, 0, -1):
        for i in range(0, hi):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
