#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height, self.width)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        if args:
            arg_list = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, arg_list[i], value)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
     
    def __str__(self):
         return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height, self.width)


    def to_dictionary(self):
        return {
                "id" : self.id,
                "x" : self.x,
                "size" : self.size,
                "y" : self.y
                }
