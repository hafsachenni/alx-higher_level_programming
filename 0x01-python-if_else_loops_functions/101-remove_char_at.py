#!/usr/bin/env python3
def remove_char_at(str, n):
    strr = ""
    for count, a in enumerate(str):
        if count != n:
            strr += a
    return strr
