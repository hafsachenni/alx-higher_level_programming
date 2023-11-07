#!/usr/bin/python3
'''
defines a fucntion that reads  txt file
'''


def read_file(filename=""):
    '''reads a txt file and prints it'''

    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
