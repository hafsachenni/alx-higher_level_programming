#!/usr/bin/python3
'''
defines square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square'''
    def __init__(self, size):
        '''Instantiation with size'''
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)
