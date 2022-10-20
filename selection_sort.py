from time import time


def check_time(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print("___Time of work: ", end - start)
        return result
    return wrapper


@check_time
def selection_sort(massive: list, direction: str):
    number_of_replaces = 0
    indexing_range = range(0, len(massive) - 1)
    if direction == "asc":

        for i in indexing_range:
            min_value = i

            for j in range(i+1, len(massive)):
                if massive[j] < massive[min_value]:
                    min_value = j

            if min_value != i:
                massive[i], massive[min_value] = massive[min_value], massive[i]
                number_of_replaces += 1

    elif direction == "dsc":

        for i in indexing_range:
            max_value = i

            for j in range(i + 1, len(massive)):
                if massive[j] > massive[max_value]:
                    max_value = j

            if max_value != i:
                massive[i], massive[max_value] = massive[max_value], massive[i]
                number_of_replaces += 1
    else:
        raise TypeError("You enter wrong direction")
    return massive, number_of_replaces


def print_result(massive, total_changes: int):
    print("Sorted massive: ", *massive, sep="")
    print("Total changes = ", total_changes)


def input_data():
    massive = list(input("Input massive:").replace(" ", ""))
    direction = input("Enter 'asc' or 'dsc':")
    while direction not in ["asc", "dsc"]:
        direction = input("You enter wrong value. Do enter 'asc' or 'dsc':")
    return massive, direction


if __name__ == "__main__":
    print_result(*selection_sort(*input_data()))
