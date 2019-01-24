def bsr(input_list, value, lo=0, hi=None):
    """Returns the middle index if value matches, otherwise -1"""
    if hi == None:
        hi = len(input_list) - 1

    if lo > hi:
        return -1

    mid = int((lo + hi) / 2)

    if input_list[mid] == value:
        return mid
    elif input_list[mid] > value:
        return bsr(input_list, value, 0, mid - 1)
    else:
        return bsr(input_list, value, mid + 1, hi)
