def bsr(input_list, hi=None):
    """
    Sorts the list comparing adjacent pairs of elements to move all the 
    bigger elements to the right side.
    """

    if hi == None:
        hi = len(input_list) - 1
    elif hi == 0:
        return

    for i in range(0, hi):
        if input_list[i] > input_list[i + 1]:
            input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]

    bsr(input_list, hi - 1)
