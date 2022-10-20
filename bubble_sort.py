from interface import input_data, print_result, check_time


@check_time
def bubble_sort(sequence: list, direction: str):
    result = None
    if direction == "asc":
        result = _bubble_sort_asc(sequence)

    elif direction == "dsc":
        result = _bubble_sort_dsc(sequence)

    return result


def _bubble_sort_asc(sequence: list):
    replacements_happened = True
    while replacements_happened:
        replacements_happened = False
        for i in range(len(sequence) - 1):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                replacements_happened = True
    return sequence


def _bubble_sort_dsc(sequence: list):
    replacements_happened = True
    while replacements_happened:
        replacements_happened = False
        for i in range(len(sequence) - 1):
            if sequence[i] < sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                replacements_happened = True
    return sequence


if __name__ == "__main__":
    print_result(bubble_sort(*input_data()))
