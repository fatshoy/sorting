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
def bubble_sort(massive: list, direction: str):
    number_of_replaces = 1
    total_replaces = 0
    if direction == "asc":
        while number_of_replaces:
            number_of_replaces = 0
            for i in range(len(massive)-1):
                if massive[i] > massive[i + 1]:
                    massive[i], massive[i + 1] = massive[i + 1], massive[i]
                    number_of_replaces += 1
            total_replaces += number_of_replaces
    elif direction == "dsc":
        while number_of_replaces:
            number_of_replaces = 0
            for i in range(len(massive) - 1):
                if massive[i] < massive[i + 1]:
                    massive[i], massive[i + 1] = massive[i + 1], massive[i]
                    number_of_replaces += 1
            total_replaces += number_of_replaces
    else:
        raise TypeError("You enter wrong direction")
    return massive, total_replaces


def print_result(massive, total_changes):
    print("Sorted massive: ", *massive, sep="")
    print("Total changes = ", total_changes)


def input_data():
    massive = list(input("Input massive:").replace(" ", ""))
    direction = input("Enter 'asc' or 'dsc':")
    while direction not in ["asc", "dsc"]:
        direction = input("You enter wrong value. Do enter 'asc' or 'dsc':")
    return massive, direction


if __name__ == "__main__":
    print_result(*bubble_sort(*input_data()))
