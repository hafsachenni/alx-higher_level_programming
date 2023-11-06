#!/usr/bin/python3
'''empty class'''


class BaseGeometry:
    '''empty geometry class'''
    def area(self):
        '''raises a msg err'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''it validates value'''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
