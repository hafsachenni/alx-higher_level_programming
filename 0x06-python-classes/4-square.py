#!/usr/bin/python3
'''class square'''


class Square:
    '''initializes square with specified size'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError("size must be an integer")
        if new_value < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_value

    def area(self):
        _area = self.__size * self.__size
        return _area
