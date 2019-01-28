def bsi(items, value):
    """Returns the middle index if value matches, otherwise -1"""
    lo = 0
    hi = len(items) - 1

    while lo <= hi:
        mid = int((lo + hi) / 2)

        if items[mid] == value:
            return mid
        elif items[mid] < value:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
