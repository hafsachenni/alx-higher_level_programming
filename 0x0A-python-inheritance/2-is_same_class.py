#!/usr/bin/python3
'''define function'''


def is_same_class(obj, a_class):
    '''
    returns True if the object is an instance of secified class
    return true or false
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
