#!/usr/bin/python3
"""a function that prints the full name
first_name and last_name must be strings
otherwise raise typeerror"""


def say_my_name(first_name, last_name=""):
    """will print My name is <first name> <last name>
    while handling errors"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
