#!/usr/bin/python3
'''class that inherits from rectangle'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class that represents a square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''defining attr of the square class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str representation of the square'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height, self.width)

    @property
    def size(self):
        '''size attr getter'''
        return self.height

    @size.setter
    def size(self, value):
        '''size attr setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''methods that assign attr'''
        if args:
            arg_list = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, arg_list[i], value)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''str representation'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height, self.width)

    def to_dictionary(self):
        '''method that returns the dic representation'''
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }
