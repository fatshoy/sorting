from interface import input_data, print_result, check_time


@check_time
def quick_sort(sequence, direction):
    result = None
    if direction == "asc":
        result = _quick_sort_asc(sequence)

    elif direction == "dsc":
        result = _quick_sort_dsc(sequence)

    return result


def _quick_sort_asc(sequence):
    if len(sequence) <= 1:
        return sequence

    pivot = sequence[0]
    lower_part = [x for x in sequence if x < pivot]
    center = [x for x in sequence if x == pivot]
    greater_part = [x for x in sequence if x > pivot]

    return _quick_sort_asc(lower_part) + center + _quick_sort_asc(greater_part)


def _quick_sort_dsc(sequence):
    if len(sequence) <= 1:
        return sequence

    pivot = sequence[0]
    lower_part = [x for x in sequence if x < pivot]
    center = [x for x in sequence if x == pivot]
    greater_part = [x for x in sequence if x > pivot]

    return _quick_sort_dsc(greater_part) + center + _quick_sort_dsc(lower_part)


if __name__ == "__main__":
    print_result(quick_sort(*input_data()))
