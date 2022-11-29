from interface import input_data, print_result, check_time


@check_time
def selection_sort(sequence: list, direction: str):
    result = None
    if direction == "asc":
        result = _selection_sort_asc(sequence)

    elif direction == "dsc":
        result = _selection_sort_dsc(sequence)

    return result


def _selection_sort_asc(sequence: list):
    indexing_range = range(0, len(sequence) - 1)
    for i in indexing_range:
        min_value = i

        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[min_value]:
                min_value = j

        if min_value != i:
            sequence[i], sequence[min_value] = sequence[min_value], sequence[i]

    return sequence


def _selection_sort_dsc(sequence: list):
    indexing_range = range(0, len(sequence) - 1)
    for i in indexing_range:
        max_value = i

        for j in range(i + 1, len(sequence)):
            if sequence[j] > sequence[max_value]:
                max_value = j

        if max_value != i:
            sequence[i], sequence[max_value] = sequence[max_value], sequence[i]

    return sequence


if __name__ == "__main__":
    print_result(selection_sort(*input_data()))
