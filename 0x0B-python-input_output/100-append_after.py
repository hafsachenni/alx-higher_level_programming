#!/usr/bin/python3
'''
inserts a line of text to a file
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    inserts a line of text to a file
    '''
    with open(filename, 'r', encoding="utf-8") as file:
        string = ""
        for line in file:
            string += line
            if search_string in line:
                string += new_string
        file.seek(0)
        file.write(string)
