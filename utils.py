def is_sorted(input_list):
    """Checks whether the list is sorted or not"""
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))
