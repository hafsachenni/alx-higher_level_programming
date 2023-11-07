#!/usr/bin/python3
'''
defines a func that creates an obj from json
'''
import json


def load_from_json_file(filename):
    '''creates it'''
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
