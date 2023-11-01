#!/usr/bin/python3
"""function that adds 2 ints
a and b must be integers otherwise raise TypeError
if one of them is float cast it to an int
b is equal to 98 by default
return the sum"""


def add_integer(a, b=98):
    """casts a and b t ints if they are floats
    if a or b are not integers then raise
    typeerror, and return the addition"""

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
