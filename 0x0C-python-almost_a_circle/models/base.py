#!/usr/bin/python3
'''base class of all child classes'''

import json


class Base:
    __nb_objects = 0

    '''class atrributes'''
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    '''returns the JSON string representation of list_dictionaries'''
    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    '''method that writes the json representation to a file'''
    @classmethod
    def save_to_file(cls, list_objs):
        if not list_objs:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])
            file.write(json_string)

    '''method that returns the list of json representation'''
    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    '''returns an instance with all atrributes'''
    @classmethod
    def create(cls, **dictionary):
        dummy_1 = cls(1, 1)
        dummy_1.update(**dictionary)
        return dummy_1

    '''returns a list of all instances'''
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
                list_dict = cls.from_json_string(json_string)
                instance = [cls.create(**o) for o in list_dict]
                return instance
        except FileNotFoundError:
            raise FileNotFoundError("file not found")
