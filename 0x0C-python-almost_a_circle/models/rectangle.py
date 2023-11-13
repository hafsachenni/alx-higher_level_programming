#!/usr/bin/python3
'''rectangle class that inherits from the base class'''

from models.base import Base


class Rectangle(Base):
    '''defining class attributes'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width attr getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width atrr setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height attr getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height attr setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''x attr getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x attr setter'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''y attr getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y attr setter'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''method that returns the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''method that prints in stdout the rectangle with # char'''
        for a in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''method that prints the str representation'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
             self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''method that assigns a key/value args to attr'''
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary represenation of the rectangle'''
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
