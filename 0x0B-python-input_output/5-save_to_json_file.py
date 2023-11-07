#!/usr/bin/python3
'''
writs n obj to a txt file
'''
import json


def save_to_json_file(my_obj, filename):
    '''writes the obj to a text file'''
    with open(filename, 'a', encoding="utf_8") as file:
        json.dump(my_obj, file)
