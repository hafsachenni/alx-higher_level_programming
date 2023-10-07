#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        my_list = []

    reverse = list(reversed(my_list))
    for num in reverse:
        print("{}".format(num))
