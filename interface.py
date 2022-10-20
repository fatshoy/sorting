from time import time


def input_data():
    massive = list(input("Input massive:").replace(" ", ""))
    direction = input("Enter 'asc' or 'dsc':")
    while direction not in ["asc", "dsc"]:
        direction = input("You enter wrong value. Do enter 'asc' or 'dsc':")
    return massive, direction


def check_time(function):
    def wrapper(*args, **kwargs):
        start = time()
        func_result = function(*args, **kwargs)
        end = time()
        print("___Time of work: ", end - start)
        return func_result

    return wrapper


def print_result(massive):
    print("Sorted massive: ", *massive, sep="")
