#!/usr/bin/python3
'''
def a function that writs es to a txt file
'''


def write_file(filename="", text=""):
    '''
    writes to a txt file
    and returns num of chars
    '''
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(text)
        return len(text)
