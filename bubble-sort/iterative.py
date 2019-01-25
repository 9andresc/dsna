def bsi(input_list):
    """
    Sorts the list comparing adjacent pairs of elements to move all the 
    bigger elements to the right side.
    """

    def swap(a, b):
        """Swaps elements of the list by using their indexes"""
        input_list[a], input_list[b] = input_list[b], input_list[a]

    n = len(input_list)

    for i in range(1, n):
        for j in range(0, n - i):
            if input_list[j] > input_list[j + 1]:
                swap(j, j + 1)
