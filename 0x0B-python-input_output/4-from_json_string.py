#!/usr/bin/python3
'''
returns an obj represented by json
'''
import json


def from_json_string(my_str):
    '''returns the json representation back into an obj
    '''
    return json.loads(my_str)
