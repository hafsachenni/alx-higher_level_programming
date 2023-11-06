#!/usr/bin/python3
'''
rectangle module
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    rectangle
    '''
    def __init__(self, width, height):
        '''
        idth and height must be positive integers
        '''
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        '''
        returs rectangles area
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        rectangle's description
        '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
