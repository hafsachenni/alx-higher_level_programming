#!/usr/bin/python3
'''
square class
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    represent the square using triangle
    '''

    def __init__(self, size):
        '''
        instantiation with size
        '''
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        return "[square] {}/{}".format(self.__size, self.__size)
