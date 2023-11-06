#!/usr/bin/python3
'''module'''


def is_kind_of_class(obj, a_class):
    '''returns True if the object is an instance of a class'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
