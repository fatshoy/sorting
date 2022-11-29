from time import time
import os


class Colors:
    INPUT = "\033[94m\033[1m"
    SUCCESS = '\033[92m\033[1m'
    WARNING = '\033[93m\033[1m'
    FAIL = '\033[91m\033[1m'
    END = '\033[0m'


def input_data():
    massive = list(input(Colors.INPUT + "Input massive (with or without spaces):" + Colors.END).replace(" ", ""))
    direction = input(Colors.INPUT + "Enter 'asc' or 'dsc':" + Colors.END)
    while direction not in ["asc", "dsc"]:
        direction = input(Colors.WARNING + "You enter wrong value. Enter 'asc' or 'dsc':" + Colors.END)
    return massive, direction


def check_time(function):
    def wrapper(*args, **kwargs):
        start = time()
        func_result = function(*args, **kwargs)
        end = time()
        duration = end - start
        meta_header = Colors.SUCCESS + f"\nTime of work '{function.__name__}' function:" + Colors.END
        meta = meta_header + f" {duration} seconds"
        return func_result, meta

    return wrapper


def print_result(massive, meta=None):
    term_size = os.get_terminal_size()
    print('=' * term_size.columns)
    print()
    print(Colors.SUCCESS + "Sorted massive: " + Colors.END, *massive, sep="", end="\n")
    if meta is not None:
        print(meta)
    print()
    print('=' * term_size.columns)
