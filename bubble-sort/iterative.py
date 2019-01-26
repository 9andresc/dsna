def bsi(input_list):
    """
    Sorts the list comparing adjacent pairs of elements to move all the 
    bigger elements to the right side.
    """

    for hi in range(len(input_list) - 1, 0, -1):
        for i in range(0, hi):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
