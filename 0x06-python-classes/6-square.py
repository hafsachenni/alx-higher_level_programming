#!/usr/bin/python3
'''class square'''


class Square:
    '''initializes square with specified size'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value or not all (num>= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value    



    def area(self):
        _area = self.__size * self.__size
        return _area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
