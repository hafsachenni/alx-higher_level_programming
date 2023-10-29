#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for a in range(len(text)):
        if text[a] in [".", "?", ":"]:
            print("{}\n".format(text[a]))
        elif text[a] == " " and text[a - 1] in [".", "?", ":"]:    
            continue
        else:
            print("{}".format(text[a]), end="")
