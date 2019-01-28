def bsr(items, value, lo=0, hi=None):
    """Returns the middle index if value matches, otherwise -1"""
    if hi == None:
        hi = len(items) - 1

    if lo > hi:
        return -1

    mid = int((lo + hi) / 2)

    if items[mid] == value:
        return mid
    elif items[mid] > value:
        return bsr(items, value, 0, mid - 1)
    else:
        return bsr(items, value, mid + 1, hi)
