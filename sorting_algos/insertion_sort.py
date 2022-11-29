from interface import input_data, print_result, check_time


@check_time
def insertion_sort(sequence, direction):
    result = None
    if direction == "asc":
        result = _insertion_sort_asc(sequence)
    else:
        result = _insertion_sort_dsc(sequence)
    return result


def _insertion_sort_asc(sequence):
    list_of_indexes = range(1, len(sequence))
    for i in list_of_indexes:

        while sequence[i - 1] > sequence[i] and i > 0:
            sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
            i -= 1

    return sequence


def _insertion_sort_dsc(sequence):
    list_of_indexes = range(1, len(sequence))
    for i in list_of_indexes:

        while sequence[i - 1] < sequence[i] and i > 0:
            sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
            i -= 1

    return sequence


if __name__ == "__main__":
    print_result(*insertion_sort(*input_data()))
