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
                type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
