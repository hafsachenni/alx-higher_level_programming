#!/usr/bin/python3
'''rectangle class that inherits from the base class'''
from models.base import Base


class Rectangle(Base):
    '''defining class attributes'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    '''width attr getter'''
    @property
    def width(self):
        return self.__width

    '''width atrr setter'''
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    '''height attr getter'''
    @property
    def height(self):
        return self.__height

    '''height attr setter'''
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    '''x attr getter'''
    @property
    def x(self):
        return self.__x

    '''x attr setter'''
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    '''y attr getter'''
    @property
    def y(self):
        return self.__y

    '''y attr setter'''
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    '''method that returns the area of the rectangle instance'''
    def area(self):
        return self.__width * self.__height

    '''method that prints in stdout the rectangle with # char'''
    def display(self):
        for a in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    '''method that prints the str representation of the rectangle'''
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height)

    '''methos that assigns a key/value args to attr'''
    def update(self, *args, **kwargs):
         if args:
             attr = ["id", "width", "height", "x", "y"]
             for i, value in enumerate(args):
                 setattr(self, attr[i], value)

         else:
             for key, value in kwargs.items():
                 setattr(self, key, value)

    '''returns the dictionary represenation of the rectangle'''
    def to_dictionary(self):
        return {
                'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width
                }
