#!/usr/bin/python3
'''
def a function that writs es to a txt file
'''


def append_write(filename="", text=""):
    '''
    writes to a txt file
    and returns num of chars
    '''
    with open(filename, 'a', encoding="UTF8") as file:
        file.write(text)
        return len(text)
