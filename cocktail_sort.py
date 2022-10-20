from interface import input_data, print_result, check_time


@check_time
def cocktail_sort(sequence: list, direction: str):
    result = None
    if direction == "asc":
        result = _cocktail_sort_asc(sequence)

    elif direction == "dsc":
        result = _cocktail_sort_dsc(sequence)

    return result


def _cocktail_sort_asc(sequence):
    left = 0
    right = len(sequence) - 1

    while left <= right:

        for i in range(left, right):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
        right -= 1

        for i in range(right, left, -1):
            if sequence[i - 1] > sequence[i]:
                sequence[i - 1], sequence[i] = sequence[i], sequence[i - 1]
        left += 1

    return sequence


def _cocktail_sort_dsc(sequence):
    left = 0
    right = len(sequence) - 1

    while left <= right:

        for i in range(left, right):
            if sequence[i] < sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
        right -= 1

        for i in range(right, left, -1):
            if sequence[i - 1] < sequence[i]:
                sequence[i - 1], sequence[i] = sequence[i], sequence[i - 1]
        left += 1

    return sequence


if __name__ == "__main__":
    print_result(cocktail_sort(*input_data()))
