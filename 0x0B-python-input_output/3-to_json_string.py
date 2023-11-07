#!/usr/bin/python3
'''
defines a func that returns the json representation of an obj
'''


import json
def to_json_string(my_obj):
    '''returns the representation'''
    return json.dumps(my_obj)

