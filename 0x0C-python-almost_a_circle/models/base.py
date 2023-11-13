#!/usr/bin/python3
'''base class of all child classes'''

import json
import os


class Base:
    '''base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''The class constructor
        Args:
            id (int, optional): The id of the object
            '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''method that writes the json representation to a file'''
        if not list_objs:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''method that returns the list of json representation'''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all atrributes'''
        if cls.__name__ == "Rectangle":

            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of all instances'''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
                list_dict = cls.from_json_string(json_string)
                instance = [cls.create(**o) for o in list_dict]
                return instance
        except FileNotFoundError:
            raise FileNotFoundError("file not found")
