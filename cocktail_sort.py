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
def cocktail_sort(array, direction):
    number_of_replaces = 0
    left = 0
    right = len(array) - 1

    if direction == "asc":
        while left <= right:
            for i in range(left, right):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    number_of_replaces += 1
            right -= 1

            for i in range(right, left, -1):
                if array[i-1] > array[i]:
                    array[i-1], array[i] = array[i], array[i-1]
                    number_of_replaces += 1
            left += 1
    else:
        while left <= right:
            for i in range(left, right):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    number_of_replaces += 1
            right -= 1

            for i in range(right, left, -1):
                if array[i - 1] < array[i]:
                    array[i - 1], array[i] = array[i], array[i - 1]
                    number_of_replaces += 1
            left += 1
    return array, number_of_replaces


def print_result(massive, total_replaces):
    print("Sorted massive: ", *massive, sep="")
    print("Total replaces = ", total_replaces)


def input_data():
    massive = list(input("Input massive:").replace(" ", ""))
    direction = input("Enter 'asc' or 'dsc':")
    while direction not in ["asc", "dsc"]:
        direction = input("You enter wrong value. Do enter 'asc' or 'dsc':")
    return massive, direction


if __name__ == "__main__":
    print_result(*cocktail_sort(*input_data()))
