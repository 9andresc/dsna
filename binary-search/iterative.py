def bsi(input_list, value):
    """Returns the middle index if value matches, otherwise -1"""
    lo = 0
    hi = len(input_list) - 1

    while lo <= hi:
        mid = int((lo + hi) / 2)

        if input_list[mid] == value:
            return mid
        elif input_list[mid] < value:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
