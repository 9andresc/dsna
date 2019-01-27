def msr(input_list):
    if len(input_list) > 1:
        mid = int(len(input_list) / 2)
        left_side = input_list[:mid]
        right_side = input_list[mid:]

        msr(left_side)
        msr(right_side)

        i = 0
        j = 0
        k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                input_list[k] = left_side[i]
                i += 1
            else:
                input_list[k] = right_side[j]
                j += 1

            k += 1

        while i < len(left_side):
            input_list[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            input_list[k] = right_side[j]
            j += 1
            k += 1
