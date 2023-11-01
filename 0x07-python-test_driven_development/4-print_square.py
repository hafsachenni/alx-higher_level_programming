#!/usr/bin/python3
"""a function that prints a square with the char #
size must be an integer, otherwise raise a TypeError
if size is less than 0, raise a ValueError
if size is a float and is less than 0, raise a TypeError"""


def print_square(size):
    """this function  prints a square with the character #
    size is the size length of the square
    size must be an integer, and if its < 0 raise valueerror
    if size is a float and is less than 0, raise a TypeError"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for o in range(size):
            print("#", end="")
        print()
