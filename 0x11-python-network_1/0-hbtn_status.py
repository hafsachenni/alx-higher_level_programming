#!/usr/bin/python3
"""python script that fetches url"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        me = res.read()
    print('Body Response:')
    print("\t- type: {}".format(type(me)))
    print('\t- content: {}'.format(me))
    print('\t- utf8 content: {}'.format(me.decode("utf-8")))
