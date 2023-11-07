#!/usr/bin/python3
'''
class student that defines a student
'''


class Student:
    '''
    represents a student with his first and lst name and age
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if (type(attrs) == list and all(
                type(u) == str for u in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
