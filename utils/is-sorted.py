def is_sorted(items):
    """Checks whether the list is sorted or not"""
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))
