#!/usr/bin/python3
'''
function that prints a text with 2 new lines
after these chars: .,? and:
text must be a str else raise TypeError
There should be no space at the beginning
or at the end of each printed line
'''


def text_indentation(text):
    '''
    this function prints a text with 2 new lines.
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for a in range(len(text)):
        if text[a] in [".", "?", ":"]:
            print("{}\n".format(text[a]))
        elif text[a] == " " and text[a - 1] in [".", "?", ":"]:
            continue
        else:
            print("{}".format(text[a]), end="")
